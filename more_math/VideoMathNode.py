from .helper_functions import generate_dim_variables, parse_expr, getIndexTensorAlongDim, as_tensor, normalize_to_common_shape, make_zero_like, get_v_variable, get_f_variable, checkLazyNew
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io
from .Stack import MrmthStack
from .ParseTree import MrmthParseTree
import copy

class VideoMathNode(io.ComfyNode):
    """
    Enables math expressions on Audio.

    Inputs:
        I: Autogrow image inputs (I0, I1, ...)
        F: Autogrow float inputs (F0, F1, ...)
        Image: Expression
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ag_VideoMathNode",
            category="More math",
            display_name="Video math",
            inputs=[
                io.Autogrow.Input(id="V",template=io.Autogrow.TemplatePrefix(io.Video.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),
                io.MultiType.Input(
                    io.String.Input("Expression", default="I0*(1-F0)+I1*F0", multiline=False),
                    types=[io.String,MrmthParseTree],
                    tooltip="Expression to apply on tensor part of conditioning",
                ),
                io.MultiType.Input(
                    io.String.Input("Expression_pi", default="I0*(1-F0)+I1*F0", multiline=False),
                    types=[io.String,MrmthParseTree],
                    tooltip="Expression to apply on pooled_input part of conditioning",
                )
                , io.Combo.Input(
                    id="length_mismatch",
                    options=["do nothing","error","tile", "pad"],
                    display_name="on size mismatch",
                    default="error",
                    tooltip="How to handle mismatched video lengths. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing frames as zero."
                ),
                MrmthStack.Input(id="stack", tooltip="Access stack between nodes",optional=True)
            ],
            outputs=[
                io.Video.Output(),
                MrmthStack.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Expression,Expression_pi, V, F, length_mismatch="tile",stack={}):
        d = checkLazyNew(Expression,V,F)
        b = checkLazyNew(Expression_pi,V,F)
        return d|b

    @classmethod
    def execute(cls, V, F, Expression, Expression_pi, length_mismatch="tile",stack={}):
        tensor_keys = [k for k, v in V.items() if v is not None]
        if not tensor_keys:
             raise ValueError("At least one input is required.")

        tensors = [V[k][0] for k in tensor_keys]

        # Normalize all tensors together to find the common target shape
        normalized_tensors = normalize_to_common_shape(*tensors, mode=length_mismatch)
        V_norm = dict(zip(tensor_keys, normalized_tensors))

        # Use first normalized tensor to establish the reference shape
        ref_tensor = normalized_tensors[0]
        common_shape = ref_tensor.shape
        stack = copy.deepcopy(stack) if stack is not None else {}

        # Setup legacy variables a, b, c, d
        ae = V_norm.get("V0", make_zero_like(ref_tensor))
        be = V_norm.get("V1", make_zero_like(ae))
        ce = V_norm.get("V2", make_zero_like(ae))
        de = V_norm.get("V3", make_zero_like(ae))

        # Ensure legacy variables are normalized in case they were zero-initialized
        ae, be, ce, de = normalize_to_common_shape(ae, be, ce, de, mode=length_mismatch)

        if(length_mismatch == "error"):
            for name, tensor in V.items():
                if tensor is not None and tensor.shape[0] != common_shape[0]:
                    raise ValueError(f"Input '{name}' has shape {tensor.shape[0]}, expected {common_shape[0]} to match input.")

        variables = {
            "a": ae, "b": be, "c": ce, "d": de,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "X": getIndexTensorAlongDim(ae, 2),
            "Y": getIndexTensorAlongDim(ae, 1),
            "B": getIndexTensorAlongDim(ae, 0),
            "batch": getIndexTensorAlongDim(ae, 0),
            "C": getIndexTensorAlongDim(ae, 3),
            "channel": getIndexTensorAlongDim(ae, 3),
            "W": float(ae.shape[2]),
            "width": float(ae.shape[2]),
            "H": float(ae.shape[1]),
            "height": float(ae.shape[1]),
            "T": float(ae.shape[0]),
            "batch_count": float(ae.shape[0]),
            "N": float(ae.shape[3]),
            "channel_count": float(ae.shape[3]),
        } | generate_dim_variables(ae)

        v_stacked, v_cnt = get_v_variable(V_norm, length_mismatch=length_mismatch)
        if v_stacked is not None:
             variables["V"] = v_stacked
             variables["Vcnt"] = float(v_cnt)
             variables["V_count"] = float(v_cnt)

        f_stacked, f_cnt = get_f_variable(F)
        if f_stacked is not None:
             variables["F"] = f_stacked
             variables["Fcnt"] = float(f_cnt)
             variables["F_count"] = float(f_cnt)

        # Add all dynamic inputs
        variables.update(V_norm)

        for k, val in F.items():
            variables[k] = val if val is not None else 0.0

        tree = None
        if isinstance(Expression,str):
            tree = parse_expr(Expression)
        else:
            tree = Expression
        visitor = UnifiedMathVisitor(variables, ae.shape,ae.device,state_storage=stack)
        result_video = visitor.visit(tree)
        result_video = as_tensor(result_video, ae.shape)




        waveforms = {k: V[k]["waveform"] for k in tensor_keys}
        sample_rates = {k + "sr": V[k].get("sample_rate", 44100) for k in tensor_keys}

        # Normalize all waveforms together
        normalized_waveforms = normalize_to_common_shape(*waveforms.values(), mode=length_mismatch)
        V_norm_waveforms = dict(zip(tensor_keys, normalized_waveforms))

        ref_waveform = normalized_waveforms[0]
        common_shape = ref_waveform.shape
        sample_rate = V[tensor_keys[0]].get("sample_rate", 44100)

        if(length_mismatch == "error"):
            for name in tensor_keys:
                if waveforms[name].shape != common_shape:
                     raise ValueError(f"Input '{name}' has shape ({waveforms[name].shape[0]}, {waveforms[name].shape[2]}), expected ({common_shape[0]}, {common_shape[2]}) to match input.")

        # Setup legacy variables a, b, c, d
        a_w = V_norm_waveforms.get("V0", make_zero_like(ref_waveform))
        b_w = V_norm_waveforms.get("V1", make_zero_like(a_w))
        c_w = V_norm_waveforms.get("V2", make_zero_like(a_w))
        d_w = V_norm_waveforms.get("V3", make_zero_like(a_w))

        # Ensure legacy are normalized
        a_w, b_w, c_w, d_w = normalize_to_common_shape(a_w, b_w, c_w, d_w, mode=length_mismatch)

        variables = {
            "a": a_w, "b": b_w, "c": c_w, "d": d_w,
            "w": F.get("F0", 0.0) if F.get("F0") is not None else 0.0,
            "x": F.get("F1", 0.0) if F.get("F1") is not None else 0.0,
            "y": F.get("F2", 0.0) if F.get("F2") is not None else 0.0,
            "z": F.get("F3", 0.0) if F.get("F3") is not None else 0.0,
            "B": getIndexTensorAlongDim(a_w, 0),
            "C": getIndexTensorAlongDim(a_w, 1),
            "channel": getIndexTensorAlongDim(a_w, 1),
            "S": getIndexTensorAlongDim(a_w, 2),
            "sample": getIndexTensorAlongDim(a_w, 2),
            "R": sample_rate,
            "sample_rate": sample_rate,
            "batch": getIndexTensorAlongDim(a_w, 0),
            "T": float(a_w.shape[0]),
            "batch_count": float(a_w.shape[0]),
        } | generate_dim_variables(a_w) | V_norm_waveforms | sample_rates

        v_stacked, v_cnt = get_v_variable(V_norm_waveforms, length_mismatch=length_mismatch)
        if v_stacked is not None:
             # This 'variables' is the one for the second eval in VideoMathNode
             variables["V"] = v_stacked
             variables["Vcnt"] = float(v_cnt)
             variables["V_count"] = float(v_cnt)

        f_stacked, f_cnt = get_f_variable(F)
        if f_stacked is not None:
             variables["F"] = f_stacked
             variables["Fcnt"] = float(f_cnt)
             variables["F_count"] = float(f_cnt)

        for k, val in F.items():
            variables[k] = val if val is not None else 0.0

        tree_pi = None
        if isinstance(Expression_pi,str):
            tree_pi = parse_expr(Expression_pi)
        else:
            tree_pi = Expression_pi
        visitor = UnifiedMathVisitor(variables, a_w.shape,a_w.device,state_storage=stack)
        result_waveform = visitor.visit(tree_pi)
        result_waveform = as_tensor(result_waveform, a_w.shape)

        return ([result_video,{"waveform":result_waveform,"sample_rate":sample_rate}],stack)
