import torch
import torch.special

from ..helper_functions import freq_to_time, time_to_freq
from .MathExprVisitor import MathExprVisitor

class TensorEvalVisitor(MathExprVisitor):
    def __init__(self, variables, shape, device=None):
        self.variables = variables
        self.spatial_variables = variables.copy()
        self.shape = shape
        # Infer device from variables if not provided
        if device is None:
             self.device = next((v.device for v in variables.values() if isinstance(v, torch.Tensor)), torch.device("cpu"))
        else:
             self.device = device

    def visitNumberExp(self, ctx):
        return torch.full(self.shape, float(ctx.getText()), device=self.device)

    def visitConstantExp(self, ctx):
        name = ctx.getText().lower()
        if name == "pi":
            return torch.full(self.shape, 3.141592653589793, device=self.device)
        if name == "e":
            return torch.full(self.shape, 2.718281828459045, device=self.device)
        raise ValueError(f"Unknown constant: {name}")

    def visitVariableExp(self, ctx):
        name = ctx.getText()
        if name not in self.variables:
            raise ValueError(f"Variable '{name}' not found")
        if not isinstance(self.variables[name], torch.Tensor):  return torch.full(self.shape, self.variables[name], device=self.device)
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
    def visitNormExp(self, ctx):   return torch.full(self.shape, torch.linalg.norm(self.visit(ctx.expr())).item(), device=self.device)
    def visitSqrtFunc(self, ctx):  return torch.sqrt(self.visit(ctx.expr()))
    def visitLnFunc(self, ctx):    return torch.log(self.visit(ctx.expr()))
    def visitLogFunc(self, ctx):   return torch.log10(self.visit(ctx.expr()))
    def visitExpFunc(self, ctx):   return torch.exp(self.visit(ctx.expr()))
    def visitTNormFunc(self, ctx): return torch.nn.functional.normalize(self.visit(ctx.expr()), p=2, dim=-1)
    def visitSNormFunc(self, ctx): return torch.full(self.shape, torch.linalg.norm(self.visit(ctx.expr())).data[0], device=self.device)
    def visitFloorFunc(self, ctx): return torch.floor(self.visit(ctx.expr()))
    def visitCeilFunc(self, ctx):  return torch.ceil(self.visit(ctx.expr()))
    def visitRoundFunc(self, ctx): return torch.round(self.visit(ctx.expr()))
    def visitGammaFunc(self, ctx): return torch.special.gamma(self.visit(ctx.expr())).exp()
    def visitSigmoidFunc(self, ctx): return torch.sigmoid(self.visit(ctx.expr()))
    def visitReluFunc(self, ctx): return torch.relu(self.visit(ctx.expr()))
    def visitSoftplusFunc(self, ctx): return torch.nn.functional.softplus(self.visit(ctx.expr()))
    def visitGeluFunc(self, ctx): return torch.nn.functional.gelu(self.visit(ctx.expr()))
    def visitSignFunc(self, ctx): return torch.sign(self.visit(ctx.expr()))
    def visitFractFunc(self, ctx):
        val = self.visit(ctx.expr())
        return val - torch.floor(val)

    def visitAnglFunc(self, ctx): return torch.angle(self.visit(ctx.expr()))
    def visitPrintFunc(self, ctx):
        val = self.visit(ctx.expr())
        print(val,end="\n")
        return val

    def visitSfftFunc(self, ctx):
        old_vars = self.variables
        self.variables = self.spatial_variables.copy()
        try:
            val = self.visit(ctx.expr())
            return time_to_freq(val)
        finally:
            self.variables = old_vars


    def visitSwapFunc(self, ctx):
        tsr = self.visit(ctx.expr(0))
        # Evaluate arguments for dim, idx1, idx2. They return full tensors, so we take scalar value.
        # We use .data.flatten()[0] to get the scalar safely from any shape
        dim_t = self.visit(ctx.expr(1))
        idx1_t = self.visit(ctx.expr(2))
        idx2_t = self.visit(ctx.expr(3))

        dim = int(dim_t.flatten()[0].item())
        i = int(idx1_t.flatten()[0].item())
        j = int(idx2_t.flatten()[0].item())

        # Handle negative dim
        if dim < 0: dim += tsr.ndim

        # Create permuted index
        indices = torch.arange(tsr.shape[dim], device=tsr.device)
        # Swap
        # Check bounds? Torch index_select will check bounds or crash.
        # Support python style negative indexing for indices
        if i < 0: i += tsr.shape[dim]
        if j < 0: j += tsr.shape[dim]

        val_i = indices[i].clone()
        indices[i] = indices[j]
        indices[j] = val_i

        return torch.index_select(tsr, dim, indices)

    def visitSifftFunc(self, ctx):
        old_vars = self.variables
        # Switch to freq variables
        self.variables = self.variables.copy()

        # Inject Freq variables based on shape
        # Dimensions being transformed are 2 onwards
        # We use a reference tensor from existing variables to get device/dtype if possible,
        # or use val from a visit? We need vars BEFORE visit.
        # We can construct index tensors using torch.arange like getIndexTensorAlongDim does.
        # We need the device. 'a' is a safe bet for device source.
        device = self.spatial_variables['a'].device if 'a' in self.spatial_variables else torch.device('cpu')

        dims = range(2, len(self.shape))
        for d in dims:
            # Create index tensor for dim d
            # Shape: ones with size at dim d
            # getIndexTensorAlongDim logic:
            #   shape = tensor.shape
            #   values = torch.arange(shape[dim], ...)
            #   reshape and expand
            size_d = self.shape[d]
            values = torch.arange(size_d, dtype=torch.float32, device=device)
            view_shape = [1] * len(self.shape)
            view_shape[d] = size_d
            values = values.view(*view_shape).expand(*self.shape)

            # Bind variables
            if d == 2:
                self.variables['K'] = values
                self.variables['F'] = size_d
                self.variables['Ky'] = values
                self.variables['Fy'] = size_d
                self.variables['frequency'] = self.variables['K'] # K is index
                self.variables['frequency_count'] = self.variables['F'] # F is scalar
            if d == 3:
                self.variables['Kx'] = values
                self.variables['Fx'] = size_d

            # Generic fallback
            self.variables[f'K_dim{d}'] = values
            self.variables[f'F_dim{d}'] = size_d

        # Calculate isotropic K (Euclidean distance from DC)
        # K = sqrt(K_2^2 + K_3^2 + ...)
        k_sq_sum = torch.zeros(self.shape, device=device)
        dims = range(2, len(self.shape))
        for d in dims:
             # Re-access the K variable for this dim (safe way)
             k_val = self.variables.get(f'K_dim{d}')
             if k_val is not None:
                k_sq_sum = torch.add(k_sq_sum, torch.pow(k_val, 2))

        self.variables['K'] = torch.sqrt(k_sq_sum)
        self.variables['frequency'] = self.variables['K']

        try:
            val = self.visit(ctx.expr())
            return freq_to_time(val)
        finally:
            self.variables = old_vars

    # Two-argument functions
    def visitPowFunc(self, ctx):
        return torch.pow(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
    def visitAtan2Func(self, ctx):
        return torch.atan2(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitClampFunc(self, ctx): return torch.clamp(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.expr(2)))
    def visitLerpFunc(self, ctx):
        a = self.visit(ctx.expr(0))
        b = self.visit(ctx.expr(1))
        w = self.visit(ctx.expr(2))
        return torch.lerp(a, b, w)

    def visitSmoothstepFunc(self, ctx):
        x = self.visit(ctx.expr(0))
        edge0 = self.visit(ctx.expr(1))
        edge1 = self.visit(ctx.expr(2))

        # Scale, bias and saturate x to 0..1 range
        t = torch.clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
        # Evaluate polynomial
        return t * t * (3.0 - 2.0 * t)

    def visitStepFunc(self, ctx):
        x = self.visit(ctx.expr(0))
        edge = self.visit(ctx.expr(1))
        # step(edge, x) = 1 if x >= edge else 0
        return torch.where(x >= edge, 1.0, 0.0)
    # N-argument functions
    def visitSMinFunc(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        return torch.full(self.shape, torch.min(torch.stack(args)), device=self.device)
    def visitSMaxFunc(self, ctx):
        args = [torch.reshape(self.visit(e), self.shape) for e in ctx.expr()]
        return torch.full(self.shape, torch.max(torch.stack(args)), device=self.device)

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
    def visitFunc3Exp(self, ctx):
        return self.visitChildren(ctx)
    def visitFunc4Exp(self, ctx):
        return self.visitChildren(ctx)
    def visitAtomExp(self, ctx):
        return self.visitChildren(ctx)

    def visitFunc2Expr(self, ctx):
        return self.visit(ctx.getChild(0))  # forward to Atan2Func, PowFunc, etc.

    def visitExpr(self, ctx):
       return self.visitChildren(ctx)
