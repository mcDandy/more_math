import torch
import math
from .helper_functions import (
    generate_dim_variables,
    getIndexTensorAlongDim,
    parse_expr,
    commonLazy,
    normalize_to_common_shape,
    as_tensor,
    prepare_inputs
)

from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from comfy_api.latest import io
from comfy_api.latest import VideoComponents, VideoFromComponents


class VideoMathNode(io.ComfyNode):
    """
    Enables math expressions on Videos (Images + Audio).
    Video object is expected to have 'images' and 'audio' components.
    Expressions for 'Images' and 'Audio' are handled separately.
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_VideoMathNode",
            category="More math",
            display_name="Video math",
            inputs=[
                io.Video.Input(id="a"),
                io.Video.Input(id="b", optional=True, lazy=True),
                io.Video.Input(id="c", optional=True, lazy=True),
                io.Video.Input(id="d", optional=True, lazy=True),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="Images", default="a*(1-w)+b*w", tooltip="Expression for the image frames"),
                io.String.Input(id="Audio", default="a*(1-w)+b*w", tooltip="Expression for the audio component"),
                io.Combo.Input(
                    id="length_mismatch",
                    options=["tile", "error", "pad"],
                    default="tile",
                    tooltip="How to handle mismatched frame/sample counts. broadcast: repeat shorter inputs; error: raise error on mismatch; pad: treat missing as zero."
                )
            ],
            outputs=[
                io.Video.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, Images, Audio, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0, length_mismatch="tile"):
        return commonLazy(Images, a, b, c, d, w, x, y, z) + commonLazy(Audio, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, Images, Audio, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0, length_mismatch="tile") -> io.NodeOutput:

        ac, bc, cc, dc = prepare_inputs(a,b,c,d)
        imgs_ae = ac.images
        imgs_be = bc.images
        imgs_ce = cc.images
        imgs_de = dc.images
        imgs_ae, imgs_be, imgs_ce, imgs_de = normalize_to_common_shape(imgs_ae, imgs_be, imgs_ce, imgs_de, mode=length_mismatch)

        img_vars = {
            "a": imgs_ae, "b": imgs_be, "c": imgs_ce, "d": imgs_de,
            "w": w, "x": x, "y": y, "z": z,
            "B": getIndexTensorAlongDim(imgs_ae, 0),
            "frame": getIndexTensorAlongDim(imgs_ae, 0),
            "C": getIndexTensorAlongDim(imgs_ae, 1),
            "channel": getIndexTensorAlongDim(imgs_ae, 1),
            "H": imgs_ae.shape[2],
            "height": imgs_ae.shape[2],
            "W": imgs_ae.shape[3],
            "width": imgs_ae.shape[3],
            "T": imgs_ae.shape[0],
            "frame_count": imgs_ae.shape[0],
            "R": float(ac.frame_rate),
            "frame_rate": float(ac.frame_rate),
            "N": imgs_ae.shape[1],
            "channel_count": imgs_ae.shape[1],
        } | generate_dim_variables(imgs_ae)

        tree = parse_expr(Images);
        visitor = UnifiedMathVisitor(img_vars, imgs_ae.shape)
        result_tensor = visitor.visit(tree)
        result_imgs = as_tensor(result_tensor, imgs_ae.shape)

        # --- Process Audio ---
        wav_a = ac.audio["waveform"]
        sample_rate = ac.audio["sample_rate"]
        wav_b = bc.audio["waveform"] if bc is not None else None
        wav_c = cc.audio["waveform"] if cc is not None else None
        wav_d = dc.audio["waveform"] if dc is not None else None

        # Determine target_wav_len as max of all provided audio
        wav_lengths = [wav_a.shape[2]]
        if bc is not None: wav_lengths.append(wav_b.shape[2])
        if cc is not None: wav_lengths.append(wav_c.shape[2])
        if dc is not None: wav_lengths.append(wav_d.shape[2])
        target_wav_len = max(wav_lengths)

        def resolve_wav(tensor, comp, name):
            if comp is None:
                return 0.0

            curr_len = tensor.shape[2]
            if curr_len == target_wav_len:
                return tensor

            if length_mismatch == "tile":
                return tensor.repeat(1, 1, math.ceil(target_wav_len / curr_len))[:, :, :target_wav_len]
            elif length_mismatch == "pad":
                out = torch.zeros((tensor.shape[0], tensor.shape[1], target_wav_len), device=tensor.device, dtype=tensor.dtype)
                out[:, :, :curr_len] = tensor
                return out
            else: # error
                raise ValueError(f"Audio samples mismatch in {name}: expected {target_wav_len} to match longest input, got {curr_len}. Set length_mismatch to 'broadcast' or 'pad' to handle this.")

        wav_ae = resolve_wav(wav_a, True, "input a")
        wav_be = resolve_wav(wav_b, bc, "input b")
        wav_ce = resolve_wav(wav_c, cc, "input c")
        wav_de = resolve_wav(wav_d, dc, "input d")

        wav_ae, wav_be, wav_ce, wav_de = normalize_to_common_shape(wav_ae, wav_be, wav_ce, wav_de, mode=length_mismatch)

        wav_vars = {
            "a": wav_ae, "b": wav_be, "c": wav_ce, "d": wav_de,
            "w": w, "x": x, "y": y, "z": z,
            "B": getIndexTensorAlongDim(wav_ae, 0),
            "batch": getIndexTensorAlongDim(wav_ae, 0),
            "C": getIndexTensorAlongDim(wav_ae, 1),
            "channel": getIndexTensorAlongDim(wav_ae, 1),
            "S": getIndexTensorAlongDim(wav_ae, 2),
            "sample": getIndexTensorAlongDim(wav_ae, 2),
            "R": sample_rate,
            "sample_rate": sample_rate,
            "T": wav_ae.shape[2],
            "sample_count": wav_ae.shape[2],
            "N": wav_ae.shape[1],
            "channel_count": wav_ae.shape[1],
        } | generate_dim_variables(wav_ae)

        tree = parse_expr(Audio);
        visitor = UnifiedMathVisitor(wav_vars, wav_ae.shape)
        result_tensor = visitor.visit(tree)
        result_audio_wav = as_tensor(result_tensor, wav_ae.shape)

        output = VideoFromComponents(
            VideoComponents(
                images=result_imgs, audio={"waveform": result_audio_wav, "sample_rate": sample_rate}, frame_rate=ac.frame_rate
            )
        )

        return (output,)
