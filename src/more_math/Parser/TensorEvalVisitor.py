from tkinter import SE
import torch
import torch.special

from ..helper_functions import freq_to_time, time_to_freq
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
    
    def visitSfftFunc(self, ctx):
        s = self.shape
        
        hop_length = 256
        n_fft = 512
        if len(s) < 4:
            raise ValueError("Input tensor must have at least 4 dimensions for SFFT operation. You might be forgetting to to use inverse function before leaving node.")
        self.shape=(s[0],
        s[1],
        s[3] * hop_length)
        
        val = self.visit(ctx.expr());
        self.shape = s;
        return time_to_freq(val, n_fft, hop_length)
    def visitSifftFunc(self, ctx):
        s = self.shape

        hop_length = 256
        n_fft = 512

        
        self.shape = (s[0],
        s[1],
        n_fft // 2 + 1,  # Frequency bins
        s[2]//hop_length+1)

        val = self.visit(ctx.expr())
        return freq_to_time(val, n_fft, hop_length)
        self.shape = s;



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
