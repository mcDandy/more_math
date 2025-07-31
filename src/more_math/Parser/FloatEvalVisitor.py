import math
from tkinter import SE
from sympy import true
import torch
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
        return self.visit(ctx.orExpr()).bool() | self.visit(ctx.xorExpr()).bool()

    def visitXorExp(self, ctx):
        return self.visit(ctx.xorExpr()).bool() ^ self.visit(ctx.andExpr()).bool()

    def visitAndExp(self, ctx):
        return self.visit(ctx.andExpr()).bool() & self.visit(ctx.addExpr()).bool()

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
    def visitAbsFunc(self, ctx):   return math.abs(self.visit(ctx.expr()))
    def visitSqrtFunc(self, ctx):  return math.sqrt(self.visit(ctx.expr()))
    def visitLnFunc(self, ctx):    return math.log(self.visit(ctx.expr()))
    def visitLogFunc(self, ctx):   return math.log10(self.visit(ctx.expr()))
    def visitExpFunc(self, ctx):   return math.exp(self.visit(ctx.expr()))
    def visitNormFunc(self, ctx):  return math.sqrt(math.avg(x**2 for x in self.visit(ctx.expr())))
    def visitFloorFunc(self, ctx): return math.floor(self.visit(ctx.expr()))
    def visitCeilFunc(self, ctx):  return math.ceil(self.visit(ctx.expr()))
    def visitRoundFunc(self, ctx): return math.round(self.visit(ctx.expr()))
    def visitGammaFunc(self, ctx): return math.gamma(self.visit(ctx.expr())).exp()

    # Two-argument functions
    def visitPowFunc(self, ctx):
        return math.pow(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
    def visitAtan2Func(self, ctx):
        return math.atan2(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    # N-argument functions
    def visitSMinFunc(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        return math.min(args)
    def visitSMaxFunc(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        return math.max(args)

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
       print("Visiting expression:", ctx.getText())
       return self.visitChildren(ctx)
