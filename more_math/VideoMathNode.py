from inspect import cleandoc

from comfy_api.latest import io
from comfy_api.input_impl import VideoFromComponents
from comfy_api.util import VideoComponents


from .helper_functions import generate_dim_variables, getIndexTensorAlongDim, eval_tensor_expr, make_zero_like, commonLazy

class VideoMathNode(io.ComfyNode):
    """
    Enables math expressions on Video (images + audio).

    Inputs:
        a, b, c, d: Video inputs (b, c, d default to zero if not provided)
        w, x, y, z: Float variables for expressions
        Audio: Expression for audio component
        Images: Expression for image component

    Outputs:
        VIDEO: Result of applying expressions to input videos
    """

    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_VideoMathNode",
            display_name="Video math",
            category="More math",
            inputs=[
                io.Video.Input(id="a"),
                io.Video.Input(id="b", optional=True),
                io.Video.Input(id="c", optional=True),
                io.Video.Input(id="d", optional=True),
                io.Float.Input(id="w", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, force_input=True),
                io.String.Input(id="Audio", default="a*(1-w)+b*w", tooltip="Expression to apply on audio part of video"),
                io.String.Input(id="Images", default="a*(1-w)+b*w", tooltip="Expression to apply on image part of video"),
            ],
            outputs=[
                io.Video.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def check_lazy_status(cls, Audio, Images, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0):
        tensor_needs = set(commonLazy(Audio, a, b, c, d, w, x, y, z))
        pooled_needs = set(commonLazy(Images, a, b, c, d, w, x, y, z))
        return list(tensor_needs.union(pooled_needs))

    @classmethod
    def execute(cls, Audio, Images, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0) -> io.NodeOutput:
        ac = a.get_components()

        bc = b.get_components() if b is not None else make_zero_like(ac)
        cc = c.get_components() if c is not None else make_zero_like(ac)
        dc = d.get_components() if d is not None else make_zero_like(ac)

        # Process images (permute to B, C, H, W)
        imgs_a = ac.images.permute(0, 3, 1, 2)
        imgs_b = bc.images.permute(0, 3, 1, 2)
        imgs_c = cc.images.permute(0, 3, 1, 2)
        imgs_d = dc.images.permute(0, 3, 1, 2)

        img_vars = {
            "a": imgs_a,
            "b": imgs_b,
            "c": imgs_c,
            "d": imgs_d,
            "w": w,
            "x": x,
            "y": y,
            "z": z,
            "X": getIndexTensorAlongDim(imgs_a, 3),
            "Y": getIndexTensorAlongDim(imgs_a, 2),
            "B": getIndexTensorAlongDim(imgs_a, 0),
            "frame": getIndexTensorAlongDim(imgs_a, 0),
            "C": getIndexTensorAlongDim(imgs_a, 1),
            "channel": getIndexTensorAlongDim(imgs_a, 1),
            "W": imgs_a.shape[3],
            "width": imgs_a.shape[3],
            "H": imgs_a.shape[2],
            "height": imgs_a.shape[2],
            "R": float(ac.frame_rate),
            "frame_rate": float(ac.frame_rate),
            "T": imgs_a.shape[0],
            "frame_count": imgs_a.shape[0],
            "N": imgs_a.shape[1],
            "channel_count": imgs_a.shape[1],
        } | generate_dim_variables(imgs_a)

        result_imgs = eval_tensor_expr(Images, img_vars, imgs_a.shape)
        result_imgs = result_imgs.permute(0, 2, 3, 1)  # Back to B, H, W, C

        # Process audio
        audio_a = ac.audio["waveform"]
        audio_b = bc.audio["waveform"]
        audio_c = cc.audio["waveform"]
        audio_d = dc.audio["waveform"]

        audio_vars = {
            "a": audio_a,
            "b": audio_b,
            "c": audio_c,
            "d": audio_d,
            "w": w,
            "x": x,
            "y": y,
            "z": z,
            "B": getIndexTensorAlongDim(audio_a, 0),
            "batch": getIndexTensorAlongDim(audio_a, 0),
            "C": getIndexTensorAlongDim(audio_a, 1),
            "channel": getIndexTensorAlongDim(audio_a, 1),
            "S": getIndexTensorAlongDim(audio_a, 2),
            "sample": getIndexTensorAlongDim(audio_a, 2),
            "R": ac.audio["sample_rate"],
            "sample_rate": ac.audio["sample_rate"],
            "T": audio_a.shape[2],
            "sample_count": audio_a.shape[2],
            "N": audio_a.shape[1],
            "channel_count": audio_a.shape[1],
        } | generate_dim_variables(audio_a)

        result_audio = eval_tensor_expr(Audio, audio_vars, audio_a.shape)

        output = VideoFromComponents(
            VideoComponents(
                images=result_imgs,
                audio={"waveform": result_audio, "sample_rate": ac.audio["sample_rate"]},
                frame_rate=ac.frame_rate,
                metadata=ac.metadata,
            )
        )
        return (output,)
