import torch
from .helper_functions import generate_dim_variables, getIndexTensorAlongDim, comonLazy, eval_tensor_expr, make_zero_like

from comfy_api.latest import io


from .MathNodeBase import MathNodeBase

class AudioMathNode(MathNodeBase):
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
    def execute(cls, AudioExpr, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
        av = a['waveform']
        sample_rate = a['sample_rate']

        a, b, c, d = cls.prepare_inputs(a, b, c, d)

        bv, cv, dv = b['waveform'], c['waveform'], d['waveform']

        variables = {
            'a': av, 'b': bv, 'c': cv, 'd': dv,
            'w': w, 'x': x, 'y': y, 'z': z,
            'B': getIndexTensorAlongDim(av, 0),
            'C': getIndexTensorAlongDim(av, 1),
            'S': getIndexTensorAlongDim(av, 2),
            'R': torch.full_like(av, sample_rate, dtype=torch.float32),
            'T': torch.full_like(av, av.shape[2], dtype=torch.float32),
            'N': av.shape[1],
            'batch': getIndexTensorAlongDim(av, 0),
            'channel': getIndexTensorAlongDim(av, 1),
            'sample': getIndexTensorAlongDim(av, 2),
            'sample_rate': torch.full_like(av, sample_rate, dtype=torch.float32),
            'sample_count': torch.full_like(av, av.shape[2], dtype=torch.float32),
            'channel_count': av.shape[1],
        } | generate_dim_variables(av)


        result_tensor = eval_tensor_expr(AudioExpr, variables, av.shape)

        return ({'waveform': result_tensor, 'sample_rate': sample_rate},)
