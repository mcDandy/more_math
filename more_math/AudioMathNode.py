import torch
from .helper_functions import getIndexTensorAlongDim, comonLazy, eval_tensor_expr, make_zero_like

from comfy_api.latest import io


class AudioMathNode(io.ComfyNode):
    """
    Enables math expressions on Audio tensors.
    
    Inputs:
        a, b, c, d: Audio inputs (b, c, d default to zero if not provided)
        w, x, y, z: Float variables for expressions
        AudioExpr: Expression to apply on audio tensors
    
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
                io.Audio.Input(id="a", tooltip="Input audio tensor"),
                io.Audio.Input(id="b", optional=True, lazy=True, tooltip="Second input audio tensor"),
                io.Audio.Input(id="c", optional=True, lazy=True, tooltip="Third input audio tensor"),
                io.Audio.Input(id="d", optional=True, lazy=True, tooltip="Fourth input audio tensor"),
                io.Float.Input(id="w", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, lazy=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, lazy=True, force_input=True),
                io.String.Input(id="AudioExpr", default="a*(1-w)+b*w", tooltip="Expression to apply on input audio tensors"),
            ],
            outputs=[
                io.Audio.Output(),
            ],
        )

    @classmethod
    def check_lazy_status(cls, AudioExpr, a, b=[], c=[], d=[], w=0, x=0, y=0, z=0):
        return comonLazy(AudioExpr, a, b, c, d, w, x, y, z)

    @classmethod
    def execute(cls, a, AudioExpr, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
        waveform = a['waveform']
        sample_rate = a['sample_rate']

        b = b if b else make_zero_like(a)
        c = c if c else make_zero_like(a)
        d = d if d else make_zero_like(a)

        bv, cv, dv = b['waveform'], c['waveform'], d['waveform']

        variables = {
            'a': waveform, 'b': bv, 'c': cv, 'd': dv,
            'w': w, 'x': x, 'y': y, 'z': z,
            'B': getIndexTensorAlongDim(waveform, 0),
            'C': getIndexTensorAlongDim(waveform, 1),
            'S': getIndexTensorAlongDim(waveform, 2),
            'R': torch.full_like(waveform, sample_rate, dtype=torch.float32),
            'T': torch.full_like(waveform, waveform.shape[2], dtype=torch.float32),
            'N': waveform.shape[1],
            'batch': getIndexTensorAlongDim(waveform, 0),
            'channel': getIndexTensorAlongDim(waveform, 1),
            'sample': getIndexTensorAlongDim(waveform, 2),
            'sample_rate': torch.full_like(waveform, sample_rate, dtype=torch.float32),
            'sample_count': torch.full_like(waveform, waveform.shape[2], dtype=torch.float32),
            'channel_count': waveform.shape[1],
        }

        result_tensor = eval_tensor_expr(AudioExpr, variables, waveform.shape)

        return ({'waveform': result_tensor, 'sample_rate': sample_rate},)
