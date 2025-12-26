import math
from .MathExprVisitor import MathExprVisitor

class FloatEvalVisitor(MathExprVisitor):
    def __init__(self, variables):
        self.variables = variables

    def visitNumberExp(self, ctx):
        print("Visiting number expression:", ctx.getText())
        return float(ctx.getText())

    def visitConstantExp(self, ctx):
        name = ctx.getText().lower()
        if name == "pi":
            return 3.141592653589793
        if name == "e":
            return 2.718281828459045
        raise ValueError(f"Unknown constant: {name}")

    def visitVariableExp(self, ctx):
        name = ctx.getText()
        if name not in self.variables:
            raise ValueError(f"Variable '{name}' not found")
        return self.variables[name]

    def visitParenExp(self, ctx):
        return self.visit(ctx.expr())

    def visitUnaryPlus(self, ctx):
        return +self.visit(ctx.unaryExpr())

    def visitUnaryMinus(self, ctx):
        return -self.visit(ctx.unaryExpr())

    def visitAddExp(self, ctx):
        return self.visit(ctx.addExpr()) + self.visit(ctx.mulExpr())

    def visitSubExp(self, ctx):
        return self.visit(ctx.addExpr()) -  self.visit(ctx.mulExpr())

    def visitMulExp(self, ctx):
        print("Visiting multiplication expression:", ctx.getText())
        if ctx.mulExpr() is None or ctx.powExpr() is None:
            raise ValueError("Invalid multiplication expression")
        return self.visit(ctx.mulExpr()) * self.visit(ctx.powExpr())

    def visitDivExp(self, ctx):
        return self.visit(ctx.mulExpr()) / self.visit(ctx.powExpr())

    def visitModExp(self, ctx):
        return self.visit(ctx.mulExpr()) % self.visit(ctx.powExpr())

    def visitPowExp(self, ctx):
        return math.pow(self.visit(ctx.unaryExpr()), self.visit(ctx.powExpr()))

    def visitNeExp(self, ctx):
        return float(self.visit(ctx.compExpr()) != self.visit(ctx.addExpr()))
    def visitEqExp(self, ctx):
        return float(self.visit(ctx.compExpr()) == self.visit(ctx.addExpr()))
    def visitGtExp(self, ctx):
        return float(self.visit(ctx.compExpr()) > self.visit(ctx.addExpr()))
    def visitLtExp(self, ctx):
        return float(self.visit(ctx.compExpr()) < self.visit(ctx.addExpr()))
    def visitGeExp(self, ctx):
        return float(self.visit(ctx.compExpr()) >= self.visit(ctx.addExpr()))
    def visitLeExp(self, ctx):
        return float(self.visit(ctx.compExpr()) <= self.visit(ctx.addExpr()))

    def visitToUnary(self, ctx):
        return self.visit(ctx.unaryExpr())

    def visitToPow(self, ctx):
        return self.visit(ctx.powExpr())

    def visitToMul(self, ctx):
        return self.visit(ctx.mulExpr())

    def visitToAdd(self, ctx):
        return self.visit(ctx.addExpr())

    def visitToGt(self, ctx):
        return self.visit(ctx.gtExpr())
    def visitToLt(self, ctx):
        return self.visit(ctx.ltExpr())
    def visitToEq(self, ctx):
        return self.visit(ctx.eqExpr())
    def visitToNeq(self, ctx):
        return self.visit(ctx.neqExpr())
    def visitToGe(self, ctx):
        return self.visit(ctx.gteExpr())
    def visitToLe(self, ctx):
        return self.visit(ctx.lteExpr())

    # Single-argument functions
    def visitSinFunc(self, ctx):   return math.sin(self.visit(ctx.expr()))
    def visitCosFunc(self, ctx):   return math.cos(self.visit(ctx.expr()))
    def visitTanFunc(self, ctx):   return math.tan(self.visit(ctx.expr()))
    def visitAsinFunc(self, ctx):  return math.asin(self.visit(ctx.expr()))
    def visitAcosFunc(self, ctx):  return math.acos(self.visit(ctx.expr()))
    def visitAtanFunc(self, ctx):  return math.atan(self.visit(ctx.expr()))
    def visitSinhFunc(self, ctx):  return math.sinh(self.visit(ctx.expr()))
    def visitCoshFunc(self, ctx):  return math.cosh(self.visit(ctx.expr()))
    def visitTanhFunc(self, ctx):  return math.tanh(self.visit(ctx.expr()))
    def visitAsinhFunc(self, ctx): return math.asinh(self.visit(ctx.expr()))
    def visitAcoshFunc(self, ctx): return math.acosh(self.visit(ctx.expr()))
    def visitAtanhFunc(self, ctx): return math.atanh(self.visit(ctx.expr()))
    def visitAbsFunc(self, ctx):   return abs(self.visit(ctx.expr()))
    def visitAbsExp(self, ctx):    return abs(self.visit(ctx.expr()))
    def visitListExp(self, ctx):   return self.visit(ctx.expr(0))
    def visitSqrtFunc(self, ctx):  return math.sqrt(self.visit(ctx.expr()))
    def visitLnFunc(self, ctx):    return math.log(self.visit(ctx.expr()))
    def visitLogFunc(self, ctx):   return math.log10(self.visit(ctx.expr()))
    def visitExpFunc(self, ctx):   return math.exp(self.visit(ctx.expr()))
    def visitNormFunc(self, ctx):
        vals = self.visit(ctx.expr())
        if isinstance(vals, (list, tuple)):
             return math.sqrt(sum(x**2 for x in vals) / len(vals))
        return abs(vals)
    def visitFloorFunc(self, ctx): return math.floor(self.visit(ctx.expr()))
    def visitFractFunc(self, ctx):
        val = self.visit(ctx.expr())
        return val - math.floor(val)
    def visitSigmoidFunc(self, ctx): return 1/(1+math.exp(-self.visit(ctx.expr())))
    def visitReluFunc(self, ctx): return max(0.0, self.visit(ctx.expr()))
    def visitSoftplusFunc(self, ctx):
        # log(1 + exp(x))
        x = self.visit(ctx.expr())
        # stability check? math.log1p(math.exp(x)) is better but might overflow for large x
        if x > 20: return x
        return math.log(1 + math.exp(x))
    def visitGeluFunc(self, ctx):
        # 0.5 * x * (1 + erf(x / sqrt(2)))
        x = self.visit(ctx.expr())
        return 0.5 * x * (1 + math.erf(x / 1.4142135623730951))
    def visitSignFunc(self, ctx):
        x = self.visit(ctx.expr())
        return math.copysign(1.0, x) if x != 0 else 0.0
    def visitCeilFunc(self, ctx):  return math.ceil(self.visit(ctx.expr()))
    def visitRoundFunc(self, ctx): return round(self.visit(ctx.expr()))
    def visitGammaFunc(self, ctx): return math.gamma(self.visit(ctx.expr())).exp()
    def visitPrintFunc(self, ctx):
        val = self.visit(ctx.expr())
        print(val,end="\n")
        return val

    # Two-argument functions
    def visitPowFunc(self, ctx):
        return math.pow(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
    def visitAtan2Func(self, ctx):
        return math.atan2(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
    def visitStepFunc(self, ctx):
        x = self.visit(ctx.expr(0))
        edge = self.visit(ctx.expr(1))
        return 1.0 if x >= edge else 0.0

    # N-argument functions
    def visitSMinFunc(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        return min(args)
    def visitSMaxFunc(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        return max(args)

    def visitClampFunc(self, ctx):
        x = self.visit(ctx.expr(0))
        min_val = self.visit(ctx.expr(1))
        max_val = self.visit(ctx.expr(2))
        return max(min(x, max_val), min_val)

    def visitLerpFunc(self, ctx):
        # a + (b - a) * w
        a = self.visit(ctx.expr(0))
        b = self.visit(ctx.expr(1))
        w = self.visit(ctx.expr(2))
        return a + (b - a) * w

    def visitSmoothstepFunc(self, ctx):
        x = self.visit(ctx.expr(0))
        edge0 = self.visit(ctx.expr(1))
        edge1 = self.visit(ctx.expr(2))

        # Scale, bias and saturate x to 0..1 range
        t = (x - edge0) / (edge1 - edge0)
        t = max(0.0, min(1.0, t))
        # Evaluate polynomial
        return t * t * (3.0 - 2.0 * t)

    def visitFunc1Exp(self, ctx):
        return self.visitChildren(ctx)
    def visitFunc2Exp(self, ctx):
        return self.visitChildren(ctx)
    def visitFunc3Exp(self, ctx):
        return self.visitChildren(ctx)
    def visitFunc4Exp(self, ctx):
        return self.visitChildren(ctx)

    def visitMapFunc(self, ctx):
        return self.visit(ctx.expr(0))

    def visitConvFunc(self, ctx):
        return self.visit(ctx.expr(0))

    def visitFuncNExp(self, ctx):
        return self.visitChildren(ctx)
    def visitAtomExp(self, ctx):
        return self.visitChildren(ctx)

    def visitFunc2Expr(self, ctx):
        return self.visit(ctx.getChild(0))  # forward to Atan2Func, PowFunc, etc.

    def visitExpr(self, ctx):
       return self.visitChildren(ctx)
