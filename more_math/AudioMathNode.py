import torch
from .helper_functions import generate_dim_variables,parse_expr, getIndexTensorAlongDim, as_tensor, commonLazy, normalize_to_common_shape,prepare_inputs
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io


class AudioMathNode(io.ComfyNode):
    """
    Enables math expressions on Audio.

    Inputs:
        a, b, c, d: Audio inputs (b, c, d default to zero if not provided)
        w, x, y, z: Float variables for expressions
        Audio: Expression to apply on input audio

    Outputs:
        AUDIO: Result of applying expression to input audio
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_AudioMathNode",
            category="More math",
            display_name="Audio math",
            inputs=[
                io.Audio.Input(id="a"),
                io.Audio.Input(id="b", optional=True, lazy=True),
                io.Audio.Input(id="c", optional=True, lazy=True),
                io.Audio.Input(id="d", optional=True, lazy=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="Audio", default="a*(1-w)+b*w", tooltip="Expression to apply on input audio waveforms"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["tile", "error", "pad"],
                    default="tile",
                    tooltip="How to handle mismatched audio sample counts. broadcast: repeat shorter inputs; error: raise error on mismatch; pad: treat missing samples as zero."
                )
            ],
            outputs=[
                io.Audio.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Audio, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0, length_mismatch="tile"):
        return commonLazy(Audio, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, Audio, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0, length_mismatch="tile") -> io.NodeOutput:
        a, b, c, d = prepare_inputs(a, b, c, d)

        av = a["waveform"]
        sample_rate = a["sample_rate"]

        bv = None if b is None else b["waveform"]
        cv = None if c is None else c["waveform"]
        dv = None if d is None else d["waveform"]

        print(f"DEBUG: EXECUTE mismatch='{length_mismatch}' shapes av={av.shape[2]} bv={bv.shape[2] if bv is not None else 'N'} cv={cv.shape[2] if cv is not None else 'N'} dv={dv.shape[2] if dv is not None else 'N'}", flush=True)

        if(length_mismatch == "error"):
            # For audio, we check the length dimension (last one) as well as batch
            tensors_to_check = [t for t in [av, bv, cv, dv] if t is not None]
            max_batch = max(t.shape[0] for t in tensors_to_check)
            max_len = max(t.shape[-1] for t in tensors_to_check)
            for tensor, name in zip([av, bv, cv, dv], ["a", "b", "c", "d"]):
                if tensor is not None:
                    if tensor.shape[0] != max_batch or tensor.shape[-1] != max_len:
                        raise ValueError(f"Input '{name}' has shape ({tensor.shape[0]}, {tensor.shape[-1]}), expected ({max_batch}, {max_len}) to match largest input.")
        ae, be, ce, de = normalize_to_common_shape(av, bv, cv, dv, mode=length_mismatch)

        variables = {
            "a": ae, "b": be, "c": ce, "d": de,
            "w": w, "x": x, "y": y, "z": z,
            "C": getIndexTensorAlongDim(ae, 1),
            "channel": getIndexTensorAlongDim(ae, 1),
            "S": getIndexTensorAlongDim(ae, 2),
            "sample": getIndexTensorAlongDim(ae, 2),
            "R": torch.full_like(ae, sample_rate, dtype=torch.float32),
            "sample_rate": torch.full_like(ae, sample_rate, dtype=torch.float32),
            "T": torch.full_like(ae, ae.shape[2], dtype=torch.float32),
            "sample_count": torch.full_like(ae, ae.shape[2], dtype=torch.float32),
            "N": ae.shape[1],
            "channel_count": ae.shape[1],
        } | generate_dim_variables(ae)
        tree = parse_expr(Audio);
        visitor = UnifiedMathVisitor(variables, ae.shape)
        result = visitor.visit(tree)
        final_res = as_tensor(result, ae.shape)
        return ({"waveform": final_res, "sample_rate": sample_rate},)
