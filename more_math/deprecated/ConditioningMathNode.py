from ..helper_functions import commonLazy,parse_expr, generate_dim_variables, as_tensor, prepare_inputs, getIndexTensorAlongDim, normalize_to_common_shape
from comfy_api.latest import io
import torch

from ..Parser.UnifiedMathVisitor import UnifiedMathVisitor

class ConditioningMathNodeOLD(io.ComfyNode):
    """
    Enables math operations on conditionings.

    Inputs:
        a, b, c, d: Conditioning inputs (b, c, d default to zero if not provided)
        w, x, y, z: Float variables for expressions
        Tensor: Expression for the tensor part (describes image composition)
        pooled_output: Expression for the pooled output (condensed representation)

    Outputs:
        CONDITIONING: Result of applying expressions to input conditionings
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ConditioningMathNode",
            display_name="Conditioning math",
            is_deprecated=True,
            inputs=[
                io.Conditioning.Input(id="a"),
                io.Conditioning.Input(id="b", optional=True, lazy=True),
                io.Conditioning.Input(id="c", optional=True, lazy=True),
                io.Conditioning.Input(id="d", optional=True, lazy=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="Tensor", default="a*(1-w)+b*w", tooltip="Expression for tensor part (image composition)"),
                io.String.Input(
                    id="pooled_output", default="a*(1-w)+b*w", tooltip="Expression for pooled output (condensed representation)"
                ),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["tile", "error", "pad"],
                    default="error",
                    tooltip="How to handle mismatched conditioning segment counts. tile: repeat shorter inputs; error: raise error on mismatch; pad: treat missing as zero."
                )
            ],
            outputs=[
                io.Conditioning.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Tensor, pooled_output, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0, length_mismatch="tile"):
        tensor_needs = set(commonLazy(Tensor, a, b, c, d, w, x, y, z))
        pooled_needs = set(commonLazy(pooled_output, a, b, c, d, w, x, y, z))
        return list(tensor_needs.union(pooled_needs))

    @classmethod
    def execute(cls, Tensor, pooled_output, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0, length_mismatch="tile"):
        # Default missing conditionings to zero
        a_c, b_c, c_c, d_c = prepare_inputs(a, b, c, d)

        # We process the first segment of each conditioning
        ta_full, da = a_c[0]
        tb_full, db = b_c[0]
        tc_full, dc = c_c[0]
        td_full, dd = d_c[0]

        ta, tb, tc, td = normalize_to_common_shape(ta_full, tb_full, tc_full, td_full, mode=length_mismatch)

        B_val = getIndexTensorAlongDim(ta, 0)
        variables = {
            "a": ta, "b": tb, "c": tc, "d": td, "w": w, "x": x, "y": y, "z": z,
            "B": B_val, "batch": B_val,
            "T": ta.shape[0], "batch_count": ta.shape[0],
            "N": ta.shape[1], "channel_count": ta.shape[1],
        } | generate_dim_variables(ta)

        tree = parse_expr(Tensor)
        visitor = UnifiedMathVisitor(variables, ta.shape)
        result_tensor = as_tensor(visitor.visit(tree), ta.shape)

        new_dict = da.copy()
        pa = da.get("pooled_output")
        if pa is not None:
            pb = db.get("pooled_output")
            pc = dc.get("pooled_output")
            pd = dd.get("pooled_output")

            pb = pb if pb is not None else torch.zeros_like(pa)
            pc = pc if pc is not None else torch.zeros_like(pa)
            pd = pd if pd is not None else torch.zeros_like(pa)

            pa, pb, pc, pd = normalize_to_common_shape(pa, pb, pc, pd, mode=length_mismatch)

            variables_pooled = {"a": pa, "b": pb, "c": pc, "d": pd, "w": w, "x": x, "y": y, "z": z} | generate_dim_variables(pa)
            tree_p = parse_expr(pooled_output)
            visitor_p = UnifiedMathVisitor(variables_pooled, pa.shape)
            result_pooled = as_tensor(visitor_p.visit(tree_p), pa.shape)
            new_dict["pooled_output"] = result_pooled

        # Create new conditioning list
        output_cond = [(result_tensor, new_dict)]
        if len(a) > 1:
            output_cond.extend(a[1:])

        return (output_cond,)
