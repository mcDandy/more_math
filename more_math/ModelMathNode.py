from inspect import cleandoc
from comfy_api.latest import io
import comfy.utils
from antlr4 import CommonTokenStream, InputStream
import torch
from .helper_functions import ThrowingErrorListener
from .Parser.MathExprParser import MathExprParser
from .Parser.MathExprLexer import MathExprLexer
from .Parser.TensorEvalVisitor import TensorEvalVisitor

import copy

def calculate_patches(Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0):
    # Parse expression
    input_stream = InputStream(Model)
    lexer = MathExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    parser.addErrorListener(ThrowingErrorListener())
    tree = parser.expr()

    sd_a = a.model.state_dict()
    sd_b = b.model.state_dict() if b is not None else {}
    sd_c = c.model.state_dict() if c is not None else {}
    sd_d = d.model.state_dict() if d is not None else {}

    patches = {}
    layer_count = len(sd_a)

    from .helper_functions import getIndexTensorAlongDim
    pbar = comfy.utils.ProgressBar(layer_count)

    # Iterate over all keys in the main model 'a'
    for i, (key, tens_a) in enumerate(sd_a.items()):
        # Get corresponding tensors from other models, defaulting to zeros if missing or models not provided
        tens_b = sd_b.get(key, None)
        if tens_b is None: tens_b = torch.zeros_like(tens_a,device=tens_a.device)
        else: tens_b = tens_b.to(tens_a.device)

        tens_c = sd_c.get(key, None)
        if tens_c is None: tens_c = torch.zeros_like(tens_a,device=tens_a.device)
        else: tens_c = tens_c.to(tens_a.device)

        tens_d = sd_d.get(key, None)
        if tens_d is None: tens_d = torch.zeros_like(tens_a,device=tens_a.device)
        else: tens_d = tens_d.to(tens_a.device)

        # Variables for the visitor
        variables = {
            'a': tens_a,
            'b': tens_b,
            'c': tens_c,
            'd': tens_d,
            'w': w, 'x': x, 'y': y, 'z': z,
            'L': i, 'layer': i,
            'LC': layer_count, 'layer_count': layer_count
        }

        for dim_idx in range(tens_a.ndim):
             idx_tensor = getIndexTensorAlongDim(tens_a, dim_idx)
             idx_tensor = idx_tensor.to(tens_a.device)
             variables[f'D{dim_idx}'] = idx_tensor
             variables[f'dim_{dim_idx}'] = idx_tensor

        visitor = TensorEvalVisitor(variables, tens_a.shape)
        result_tensor = visitor.visit(tree)

        # Calculate difference for patching
        # The patch should be: result - original
        # Because ComfyUI applies: original + patch
        diff = result_tensor - tens_a

        # Allow skipping zero patches to save memory
        if torch.all(diff == 0):
            continue

        # Store patch. ComfyUI expects { key: (tensor,) } usually
        patches[key] = (diff,)

        pbar.update(1)
    
    return patches

class ModelMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on Model weights (state_dict).
    Functionally acts as a custom model merge.
    """
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_ModelMathNode",
            display_name="Model Math",
            category="More math",
            inputs=[
                io.Model.Input(id="a", tooltip="Main model (base)"),
                io.Model.Input(id="b", optional=True, tooltip="Optional 2nd model"),
                io.Model.Input(id="c", optional=True, tooltip="Optional 3rd model"),
                io.Model.Input(id="d", optional=True, tooltip="Optional 4th model"),
                io.Float.Input(id="w", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, force_input=True),
                io.String.Input(id="Model", default="a*(1-w)+b*w", tooltip="Expression to apply on weights"),
            ],
            outputs=[
                io.Model.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def execute(cls, Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0) -> io.NodeOutput:
        patches = calculate_patches(Model, a, b, c, d, w, x, y, z)
        out_model = a.clone()
        if patches:
            out_model.add_patches(patches, 1.0, 1.0)
        return (out_model,)

class CLIPMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on CLIP weights.
    """
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_CLIPMathNode",
            display_name="CLIP Math",
            category="More math",
            inputs=[
                io.Clip.Input(id="a", tooltip="Main CLIP (base)"),
                io.Clip.Input(id="b", optional=True, tooltip="Optional 2nd CLIP"),
                io.Clip.Input(id="c", optional=True, tooltip="Optional 3rd CLIP"),
                io.Clip.Input(id="d", optional=True, tooltip="Optional 4th CLIP"),
                io.Float.Input(id="w", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, force_input=True),
                io.String.Input(id="Model", default="a*(1-w)+b*w", tooltip="Expression to apply on weights"),
            ],
            outputs=[
                io.Clip.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def execute(cls, Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0) -> io.NodeOutput:
        patcher_a = a.patcher
        patcher_b = b.patcher if b else None
        patcher_c = c.patcher if c else None
        patcher_d = d.patcher if d else None
        
        patches = calculate_patches(Model, patcher_a, patcher_b, patcher_c, patcher_d, w, x, y, z)
        
        out_clip = a.clone()
        if patches:
            out_clip.add_patches(patches, 1.0, 1.0)
        return (out_clip,)

class VAEMathNode(io.ComfyNode):
    """
    This node enables the use of math expressions on VAE weights.
    """
    @classmethod
    def define_schema(cls) -> io.Schema:
        return io.Schema(
            node_id="mrmth_VAEMathNode",
            display_name="VAE Math",
            category="More math",
            inputs=[
                io.Vae.Input(id="a", tooltip="Main VAE (base)"),
                io.Vae.Input(id="b", optional=True, tooltip="Optional 2nd VAE"),
                io.Vae.Input(id="c", optional=True, tooltip="Optional 3rd VAE"),
                io.Vae.Input(id="d", optional=True, tooltip="Optional 4th VAE"),
                io.Float.Input(id="w", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="x", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="y", default=0.0, optional=True, force_input=True),
                io.Float.Input(id="z", default=0.0, optional=True, force_input=True),
                io.String.Input(id="Model", default="a*(1-w)+b*w", tooltip="Expression to apply on weights"),
            ],
            outputs=[
                io.Vae.Output(),
            ],
        )

    tooltip = cleandoc(__doc__)

    @classmethod
    def execute(cls, Model, a, b=None, c=None, d=None, w=0.0, x=0.0, y=0.0, z=0.0) -> io.NodeOutput:
        patcher_a = a.patcher
        patcher_b = b.patcher if b else None
        patcher_c = c.patcher if c else None
        patcher_d = d.patcher if d else None
        
        patches = calculate_patches(Model, patcher_a, patcher_b, patcher_c, patcher_d, w, x, y, z)
        
        # VAE does not have a clone method, so we shallow copy and clone the patcher
        out_vae = copy.copy(a)
        out_vae.patcher = a.patcher.clone()
        
        if patches:
            out_vae.patcher.add_patches(patches, 1.0, 1.0)
            
        return (out_vae,)
