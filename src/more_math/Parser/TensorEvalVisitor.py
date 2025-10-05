import re
from tkinter import SE
import torch
import torch.special

from ..helper_functions import freq_to_time, getIndexTensorAlongDim, time_to_freq
from .MathExprVisitor import MathExprVisitor

class TensorEvalVisitor(MathExprVisitor):
    def __init__(self, variables,shape):
        self.variables = variables
        self.shape = shape

    def visitNumberExp(self, ctx):
        return torch.full(self.shape,float(ctx.getText()))

    def visitConstantExp(self, ctx):
        name = ctx.getText().lower()
        if name == "pi":
            return torch.full(self.shape,3.141592653589793,)
        if name == "e":
            return torch.full(self.shape,2.718281828459045)
        raise ValueError(f"Unknown constant: {name}")

    def visitVariableExp(self, ctx):
        name = ctx.getText()
        if name not in self.variables:
            raise ValueError(f"Variable '{name}' not found")
        if not isinstance(self.variables[name], torch.Tensor):  return torch.full(self.shape,self.variables[name])
        return self.variables[name]

    def visitParenExp(self, ctx):
        return self.visit(ctx.expr())

    def visitUnaryPlus(self, ctx):
        return +self.visit(ctx.unaryExpr())

    def visitUnaryMinus(self, ctx):
        return -self.visit(ctx.unaryExpr())


    def visitAddExp(self, ctx):
        return torch.add(self.visit(ctx.addExpr()), self.visit(ctx.mulExpr()))

    def visitSubExp(self, ctx):
        return torch.sub(self.visit(ctx.addExpr()), self.visit(ctx.mulExpr()))

    def visitMulExp(self, ctx):
        print("Visiting multiplication expression:", ctx.getText())
        if ctx.mulExpr() is None or ctx.powExpr() is None:
            raise ValueError("Invalid multiplication expression")
        return torch.mul(self.visit(ctx.mulExpr()), self.visit(ctx.powExpr()))

    def visitDivExp(self, ctx):
        return torch.div(self.visit(ctx.mulExpr()), self.visit(ctx.powExpr()))
    

    def visitModExp(self, ctx):
        return torch.fmod(self.visit(ctx.mulExpr()), self.visit(ctx.powExpr()))

    def visitPowExp(self, ctx):
        return torch.pow(self.visit(ctx.unaryExpr()), self.visit(ctx.powExpr()))

    def visitToUnary(self, ctx):
        return self.visit(ctx.unaryExpr())

    def visitToPow(self, ctx):
        return self.visit(ctx.powExpr())

    def visitToMul(self, ctx):
        return self.visit(ctx.mulExpr())

    def visitToAdd(self, ctx):
        return self.visit(ctx.addExpr())

    def visitToAnd(self, ctx):
        return self.visit(ctx.andExpr())

    def visitToXor(self, ctx):
        return self.visit(ctx.xorExpr())

    def visitOrExp(self, ctx):
        return torch.logical_or(self.visit(ctx.orExpr()).bool(), self.visit(ctx.xorExpr()).bool())

    def visitXorExp(self, ctx):
        return torch.pow(self.visit(ctx.xorExpr()), self.visit(ctx.andExpr()))

    def visitAndExp(self, ctx):
        return torch.logical_and(self.visit(ctx.andExpr()).bool(), self.visit(ctx.addExpr()).bool())

    def visitNeExp(self, ctx):
        return torch.ne(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()
    def visitEqExp(self, ctx):
        return torch.eq(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()
    def visitGtExp(self, ctx):
        return torch.gt(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()
    def visitLtExp(self, ctx):
        return torch.lt(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()
    def visitGeExp(self, ctx):
        return torch.ge(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()
    def visitLeExp(self, ctx):
        return torch.le(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()

    # Single-argument functions
    def visitSinFunc(self, ctx):   return torch.sin(self.visit(ctx.expr()))
    def visitCosFunc(self, ctx):   return torch.cos(self.visit(ctx.expr()))
    def visitTanFunc(self, ctx):   return torch.tan(self.visit(ctx.expr()))
    def visitAsinFunc(self, ctx):  return torch.asin(self.visit(ctx.expr()))
    def visitAcosFunc(self, ctx):  return torch.acos(self.visit(ctx.expr()))
    def visitAtanFunc(self, ctx):  return torch.atan(self.visit(ctx.expr()))
    def visitSinhFunc(self, ctx):  return torch.sinh(self.visit(ctx.expr()))
    def visitCoshFunc(self, ctx):  return torch.cosh(self.visit(ctx.expr()))
    def visitTanhFunc(self, ctx):  return torch.tanh(self.visit(ctx.expr()))
    def visitAsinhFunc(self, ctx): return torch.asinh(self.visit(ctx.expr()))
    def visitAcoshFunc(self, ctx): return torch.acosh(self.visit(ctx.expr()))
    def visitAtanhFunc(self, ctx): return torch.atanh(self.visit(ctx.expr()))
    def visitAbsFunc(self, ctx):   return torch.abs(self.visit(ctx.expr()))
    def visitSqrtFunc(self, ctx):  return torch.sqrt(self.visit(ctx.expr()))
    def visitLnFunc(self, ctx):    return torch.log(self.visit(ctx.expr()))
    def visitLogFunc(self, ctx):   return torch.log10(self.visit(ctx.expr()))
    def visitExpFunc(self, ctx):   return torch.exp(self.visit(ctx.expr()))
    def visitTNormFunc(self, ctx): return torch.nn.functional.normalize(self.visit(ctx.expr()), p=2, dim=-1)
    def visitSNormFunc(self, ctx): return torch.full(self.shape,torch.linalg.norm(self.visit(ctx.expr())).data[0])
    def visitFloorFunc(self, ctx): return torch.floor(self.visit(ctx.expr()))
    def visitCeilFunc(self, ctx):  return torch.ceil(self.visit(ctx.expr()))
    def visitRoundFunc(self, ctx): return torch.round(self.visit(ctx.expr()))
    def visitGammaFunc(self, ctx): return torch.special.gamma(self.visit(ctx.expr())).exp()
    def visitSigmoidFunc(self, ctx): return torch.sigmoid(self.visit(ctx.expr()))
    def visitAnglFunc(self, ctx): return torch.angle(self.visit(ctx.expr()))
    def visitPrintFunc(self, ctx):
        val = self.visit(ctx.expr())
        print(val,"\n")
        return val
    
    def visitSfftFunc(self, ctx):
       hop_length = 256
       n_fft = 512
   
       # Must start in freq-domain
       if len(self.shape) != 4:
           raise ValueError(f"SFFT input must be 4D freq-domain, got {len(self.shape)}D")
       B, C, F, T_spec = self.shape
       T = T_spec * hop_length
       old_shape = self.shape
   
       # --- Switch to time-domain for child ---
       time_shape = (B, C, T)
       time_shape = self.variables['a'].shape if 'a' in self.variables else time_shape
       self.shape = time_shape
       shp_time = torch.zeros(time_shape, device=self.variables.get('device', 'cpu'))
       self.variables['S'] = getIndexTensorAlongDim(shp_time, 2)
       self.variables['T'] = torch.full_like(shp_time, self.shape[2])
       self.variables['B'] = getIndexTensorAlongDim(shp_time, 0)
       self.variables['C'] = getIndexTensorAlongDim(shp_time, 1)
       self.variables['R'] = torch.full_like(shp_time, self.variables['R'].flatten()[0].item())
   
       # Child sees time-domain
       val = self.visit(ctx.expr())
       if val.ndim != 3:
           raise ValueError(f"SFFT child must return 3D time-domain, got {val.ndim}D")

       # --- Back to freq-domain after child ---
       num_freq_bins = n_fft // 2 + 1
       num_frames = T // hop_length + 1
       freq_shape = (B, C, num_freq_bins, num_frames)
       freq_shape = old_shape
       self.shape = freq_shape
       shp_freq = torch.zeros(freq_shape, device=shp_time.device)
       self.variables['S'] = getIndexTensorAlongDim(shp_freq, 3)  # now frame index
       self.variables['T'] = torch.full_like(shp_freq, shp_freq.shape[3])  # now num frames
       self.variables['B'] = getIndexTensorAlongDim(shp_freq, 0)
       self.variables['C'] = getIndexTensorAlongDim(shp_freq, 1)
       self.variables['F'] = getIndexTensorAlongDim(shp_freq, 2)
       self.variables['K'] = shp_freq.shape[2]
       self.variables['R'] = torch.full_like(shp_freq, self.variables['R'].flatten()[0].item())
   
       # Convert time→freq
       freq_val = time_to_freq(val, n_fft=n_fft, hop_length=hop_length)
   
       # Restore caller’s view
       self.shape = old_shape
       return freq_val
    
    def visitSifftFunc(self, ctx):
        hop_length = 256
        n_fft = 512
     
        # Must start in time-domain
        if len(self.shape) != 3:
            raise ValueError(f"SIFFT input must be 3D time-domain, got {len(self.shape)}D")
        B, C, T = self.shape
        old_shape = self.shape
     
        # --- Switch to freq-domain for child ---
        num_freq_bins = n_fft // 2 + 1
        num_frames = T // hop_length + 1
        freq_shape = (B, C, num_freq_bins, num_frames)
        self.shape = freq_shape
        shp_freq = torch.zeros(freq_shape, device=self.variables.get('device', 'cpu'))
        self.variables['K'] = getIndexTensorAlongDim(shp_freq, 2)
        self.variables['F'] = shp_freq.shape[2]
        self.variables['T'] = getIndexTensorAlongDim(shp_freq, 3)
        self.variables['B'] = getIndexTensorAlongDim(shp_freq, 0)
        self.variables['C'] = getIndexTensorAlongDim(shp_freq, 1)
        self.variables['S'] = getIndexTensorAlongDim(shp_freq, 2)
        self.variables['R'] = torch.full_like(shp_freq, self.variables['R'].flatten()[0].item())
     
        # Child sees freq-domain
        val = self.visit(ctx.expr())
        if val.ndim != 4:
            raise ValueError(f"SIFFT child must return 4D freq-domain, got {val.ndim}D")
     
        # --- Back to time-domain after child ---
        self.shape = old_shape
        shp_time = torch.zeros(old_shape, device=shp_freq.device)
        self.variables['T'] = getIndexTensorAlongDim(shp_time, 2)
        self.variables['B'] = getIndexTensorAlongDim(shp_time, 0)
        self.variables['C'] = getIndexTensorAlongDim(shp_time, 1)
        self.variables['S'] = getIndexTensorAlongDim(shp_freq, 2)
        self.variables['R'] = torch.full_like(shp_time, self.variables['R'].flatten()[0].item())
     
        # Convert freq→time
        wav = freq_to_time(val, n_fft=n_fft, hop_length=hop_length, time=T)
     
        return wav
    
    # Two-argument functions
    def visitPowFunc(self, ctx):
        return torch.pow(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
    def visitAtan2Func(self, ctx):
        return torch.atan2(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitClampFunc(self, ctx): return torch.clamp(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.expr(2)))
    # N-argument functions
    def visitSMinFunc(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        return torch.full(self.shape,torch.min(torch.stack(args)))
    def visitSMaxFunc(self, ctx):
        args = [torch.reshape(self.visit(e),self.shape) for e in ctx.expr()]
        return torch.full(self.shape,torch.max(torch.stack(args)))

    def visitTMinFunc(self, ctx):
        return torch.minimum(self.visit(ctx.expr(0)),self.visit(ctx.expr(1)))
    def visitTMaxFunc(self, ctx):
        return torch.maximum(self.visit(ctx.expr(0)),self.visit(ctx.expr(1)))

    def visitFunc1Exp(self, ctx):
        return self.visitChildren(ctx)
    def visitFunc2Exp(self, ctx):
        return self.visitChildren(ctx)
    def visitFuncNExp(self, ctx):
        return self.visitChildren(ctx)
    def visitAtomExp(self, ctx):
        return self.visitChildren(ctx) 

    def visitFunc2Expr(self, ctx):
        return self.visit(ctx.getChild(0))  # forward to Atan2Func, PowFunc, etc.

    def visitExpr(self, ctx):
       return self.visitChildren(ctx)
