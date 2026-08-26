from inspect import cleandoc
from comfy_api.latest import io
from .helper_functions import (
    generate_dim_variables,
    getIndexTensorAlongDim,
    parse_expr,
    as_tensor,
    normalize_to_common_shape,
    make_zero_like,
    get_v_variable,
    get_f_variable,
    checkLazyNew
)
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
import torch
from comfy.nested_tensor import NestedTensor
from .Stack import MrmthStack
from .ParseTree import MrmthParseTree
import copy

class LatentMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Latents using Autogrow inputs.
    """

    def __init__(self):
        pass

    @classmethod
    def define_schema(cls) -> io.Schema:
        """ """
        return io.Schema(
            node_id="mrmth_ag_LatentMathNode",
            display_name="Latent math",
            category="More math",
            inputs=[
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.Latent.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.MultiType.Input(
                    io.String.Input("Expression", default="V0", multiline=False),
                    types=[io.String,MrmthParseTree],
                    tooltip="Expression to apply on input latents",
                ),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["do nothing","error","tile", "pad"],
                    display_name="on size mismatch",
                    default="error",
                    tooltip="How to handle mismatched latent batch sizes. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                ),
                io.Int.Input(id="batching"),
                io.Boolean.Input(
                    id="remember_stack",
                    default=False,
                    display_name="Remember stack across batch",
                    tooltip=(
                        "If enabled, stack is copied at output leading to changes being remembered during batch operations (node runs multiple times in sucession). If disabled each batch gets it's own copy of the stack."
                    ),
                ),
                MrmthStack.Input(id="stack", tooltip="Access stack between nodes",optional=True)
            ],
            outputs=[
                io.Latent.Output(is_output_list=True),
                MrmthStack.Output(),

            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, Expression, V, F,batching, length_mismatch="tile",remember_stack=False,stack={}):
        return checkLazyNew(Expression,V,F)

    @classmethod
    def execute(cls, V, F, Expression,batching, length_mismatch="tile",remember_stack=False,stack={}) -> io.NodeOutput:
        # Determine reference latent
        ref_latent = None
        for lat in V.values():
            if lat is not None:
                ref_latent = lat
                break

        if ref_latent is None:
             raise ValueError("At least one input is required.")
        stack = stack if remember_stack else (copy.deepcopy(stack) if stack is not None else {})

        # Identify all present tensors and their keys.
        # NestedTensor inputs keep their original latent dict under the base key (V0, V1, ...)
        # so downstream nodes receive the original NestedTensor, while individual components
        # are also exposed as V0_0, V0_1, ... for math expressions.
        tensor_keys = []
        V_norm_samples = {}
        nested_component_keys = {}  # maps original key -> list of expanded component variable names
        for k, v in V.items():
            if v is None:
                continue
            samples = v.get("samples")
            if getattr(samples, "is_nested", False):
                component_names = []
                for idx, t in enumerate(samples.tensors):
                    comp_key = f"{k}_{idx}"
                    V_norm_samples[comp_key] = t
                    component_names.append(comp_key)
                nested_component_keys[k] = component_names
                # Keep the original NestedTensor under the base key so V0 returns it unchanged
                tensor_keys.append(k)
                V_norm_samples[k] = samples
            else:
                tensor_keys.append(k)
                V_norm_samples[k] = samples

        # Normalize all together; NestedTensor base entries are skipped but other non-tensor values are still supported
        at_list = [V_norm_samples[k] for k in tensor_keys if torch.is_tensor(V_norm_samples[k])]
        if at_list:
            normalized_samples = normalize_to_common_shape(*at_list, mode=length_mismatch)
            norm_iter = iter(normalized_samples)
            for key in tensor_keys:
                if not torch.is_tensor(V_norm_samples[key]):
                    continue
                V_norm_samples[key] = next(norm_iter)

        # Add nested component variables to the list of available inputs for variable binding
        tensor_keys.extend([c for components in nested_component_keys.values() for c in components])

        def _resolve_alias(base):
            # Aliases a/b/c/d should point to the first tensor component of a NestedTensor input
            components = nested_component_keys.get(base)
            if components:
                return V_norm_samples[components[0]]
            return V_norm_samples.get(base)

        first_sample = next(iter(V_norm_samples.values()))
        if not torch.is_tensor(first_sample):
            # If the first value is a NestedTensor, grab its first component for metadata
            first_sample = first_sample.tensors[0]
        ae_res = _resolve_alias("V0")
        ae = ae_res if ae_res is not None else make_zero_like(first_sample)
        be_res = _resolve_alias("V1")
        be = be_res if be_res is not None else make_zero_like(ae)
        ce_res = _resolve_alias("V2")
        ce = ce_res if ce_res is not None else make_zero_like(ae)
        de_res = _resolve_alias("V3")
        de = de_res if de_res is not None else make_zero_like(ae)

        # Ensure legacy are normalized
        ae, be, ce, de = normalize_to_common_shape(ae, be, ce, de, mode=length_mismatch)

        if length_mismatch == "error":
            for name in tensor_keys:
                sample = V_norm_samples.get(name)
                if sample is None:
                    continue
                if not torch.is_tensor(sample):
                    continue
                if sample.shape[0] != ae.shape[0]:
                    raise ValueError(f"Input '{name}' has shape {sample.shape[0]}, expected {ae.shape[0]} to match input.")

        # parse expression once
        tree = None
        if isinstance(Expression,str):
            tree = parse_expr(Expression)
        else:
            tree = Expression

        ndim = ae.ndim
        batch_dim = 0
        channel_dim = -3
        height_dim = -2
        width_dim = -1
        time_dim = None
        if ndim >= 5:
            time_dim = -4

        frame_count = ae.shape[time_dim] if time_dim is not None else ae.shape[batch_dim]

        variables = {
            "a": ae, "b": be, "c": ce, "d": de,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "X": getIndexTensorAlongDim(ae, width_dim),
            "Y": getIndexTensorAlongDim(ae, height_dim),
            "B": getIndexTensorAlongDim(ae, batch_dim),
            "batch": getIndexTensorAlongDim(ae, batch_dim),
            "C": getIndexTensorAlongDim(ae, channel_dim),
            "channel": getIndexTensorAlongDim(ae, channel_dim),
            "W": float(ae.shape[width_dim]),
            "width": float(ae.shape[width_dim]),
            "H": float(ae.shape[height_dim]),
            "height": float(ae.shape[height_dim]),
            "T": float(frame_count),
            "batch_count": float(ae.shape[batch_dim]),
            "N": float(ae.shape[channel_dim]),
            "channel_count": float(ae.shape[channel_dim]),
        } | generate_dim_variables(ae)

        if time_dim is not None:
            F_idx = getIndexTensorAlongDim(ae, time_dim)
            variables.update({"frame_idx": F_idx, "frame": F_idx, "frame_count": frame_count})

        # Add all dynamic inputs
        variables.update(V_norm_samples)

        v_stacked, v_cnt = get_v_variable(V_norm_samples, length_mismatch=length_mismatch)
        if v_stacked is not None:
             variables["V"] = v_stacked
             variables["Vcnt"] = float(v_cnt)
             variables["V_count"] = float(v_cnt)

        f_stacked, f_cnt = get_f_variable(F)
        if f_stacked is not None:
             variables["F"] = f_stacked
             variables["Fcnt"] = float(f_cnt)
             variables["F_count"] = float(f_cnt)

        for k, v in F.items():
            variables[k] = v if v is not None else 0.0

        visitor = UnifiedMathVisitor(variables, ae.shape,ae.device,state_storage=stack)
        raw_result = visitor.visit(tree)
        result_t = as_tensor(raw_result, ae.shape)

        result_latent = ref_latent.copy()

        # If the visitor produced a NestedTensor (whole-tensor arithmetic on a NestedTensor
        # input), propagate that through as a single downstream-compatible latent.
        if getattr(result_t, "is_nested", False):
            rl = result_latent.copy()
            rl["samples"] = result_t
            stack = stack if remember_stack else copy.deepcopy(stack)
            return ([rl], stack)

        # If the visitor produced a list/tuple, emit each element as a separate latent.
        if isinstance(result_t, (list, tuple)) and result_t and isinstance(result_t[0], torch.Tensor):
            results = []
            for comp in result_t:
                rl = result_latent.copy()
                rl["samples"] = comp
                results.append(rl)
                stack = stack if remember_stack else copy.deepcopy(stack)
            return (results, stack)

        if batching > 0:
            res = torch.split(result_t, batching)
            results = []
            for result_tensor in res:
                rl = result_latent.copy()
                rl["samples"] = result_tensor
                results.append(rl)
                stack = stack if remember_stack else copy.deepcopy(stack)
            return (results, stack)
        rl = result_latent.copy()
        rl["samples"] = result_t
        stack = stack if remember_stack else copy.deepcopy(stack)
        return ([rl], stack)
