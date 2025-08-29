# Generated from MathExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MathExprParser import MathExprParser
else:
    from MathExprParser import MathExprParser

# This class defines a complete generic visitor for a parse tree produced by MathExprParser.

class MathExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MathExprParser#expr.
    def visitExpr(self, ctx:MathExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#LtExp.
    def visitLtExp(self, ctx:MathExprParser.LtExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#EqExp.
    def visitEqExp(self, ctx:MathExprParser.EqExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ToAdd.
    def visitToAdd(self, ctx:MathExprParser.ToAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#GeExp.
    def visitGeExp(self, ctx:MathExprParser.GeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#LeExp.
    def visitLeExp(self, ctx:MathExprParser.LeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#NeExp.
    def visitNeExp(self, ctx:MathExprParser.NeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#GtExp.
    def visitGtExp(self, ctx:MathExprParser.GtExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AddExp.
    def visitAddExp(self, ctx:MathExprParser.AddExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ToMul.
    def visitToMul(self, ctx:MathExprParser.ToMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SubExp.
    def visitSubExp(self, ctx:MathExprParser.SubExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#MulExp.
    def visitMulExp(self, ctx:MathExprParser.MulExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ModExp.
    def visitModExp(self, ctx:MathExprParser.ModExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#DivExp.
    def visitDivExp(self, ctx:MathExprParser.DivExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ToPow.
    def visitToPow(self, ctx:MathExprParser.ToPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PowExp.
    def visitPowExp(self, ctx:MathExprParser.PowExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ToUnary.
    def visitToUnary(self, ctx:MathExprParser.ToUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#UnaryPlus.
    def visitUnaryPlus(self, ctx:MathExprParser.UnaryPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:MathExprParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ToAtom.
    def visitToAtom(self, ctx:MathExprParser.ToAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#Func1Exp.
    def visitFunc1Exp(self, ctx:MathExprParser.Func1ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#Func2Exp.
    def visitFunc2Exp(self, ctx:MathExprParser.Func2ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#Func3Exp.
    def visitFunc3Exp(self, ctx:MathExprParser.Func3ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#FuncNExp.
    def visitFuncNExp(self, ctx:MathExprParser.FuncNExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#VariableExp.
    def visitVariableExp(self, ctx:MathExprParser.VariableExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#NumberExp.
    def visitNumberExp(self, ctx:MathExprParser.NumberExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ConstantExp.
    def visitConstantExp(self, ctx:MathExprParser.ConstantExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ParenExp.
    def visitParenExp(self, ctx:MathExprParser.ParenExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SinFunc.
    def visitSinFunc(self, ctx:MathExprParser.SinFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CosFunc.
    def visitCosFunc(self, ctx:MathExprParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#TanFunc.
    def visitTanFunc(self, ctx:MathExprParser.TanFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AsinFunc.
    def visitAsinFunc(self, ctx:MathExprParser.AsinFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AcosFunc.
    def visitAcosFunc(self, ctx:MathExprParser.AcosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AtanFunc.
    def visitAtanFunc(self, ctx:MathExprParser.AtanFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SinhFunc.
    def visitSinhFunc(self, ctx:MathExprParser.SinhFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CoshFunc.
    def visitCoshFunc(self, ctx:MathExprParser.CoshFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#TanhFunc.
    def visitTanhFunc(self, ctx:MathExprParser.TanhFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AsinhFunc.
    def visitAsinhFunc(self, ctx:MathExprParser.AsinhFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AcoshFunc.
    def visitAcoshFunc(self, ctx:MathExprParser.AcoshFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AtanhFunc.
    def visitAtanhFunc(self, ctx:MathExprParser.AtanhFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AbsFunc.
    def visitAbsFunc(self, ctx:MathExprParser.AbsFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SqrtFunc.
    def visitSqrtFunc(self, ctx:MathExprParser.SqrtFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#LnFunc.
    def visitLnFunc(self, ctx:MathExprParser.LnFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#LogFunc.
    def visitLogFunc(self, ctx:MathExprParser.LogFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ExpFunc.
    def visitExpFunc(self, ctx:MathExprParser.ExpFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#TNormFunc.
    def visitTNormFunc(self, ctx:MathExprParser.TNormFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SNormFunc.
    def visitSNormFunc(self, ctx:MathExprParser.SNormFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#FloorFunc.
    def visitFloorFunc(self, ctx:MathExprParser.FloorFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CeilFunc.
    def visitCeilFunc(self, ctx:MathExprParser.CeilFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#RoundFunc.
    def visitRoundFunc(self, ctx:MathExprParser.RoundFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#GammaFunc.
    def visitGammaFunc(self, ctx:MathExprParser.GammaFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#sigmoidFunc.
    def visitSigmoidFunc(self, ctx:MathExprParser.SigmoidFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#sfftFunc.
    def visitSfftFunc(self, ctx:MathExprParser.SfftFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#sifftFunc.
    def visitSifftFunc(self, ctx:MathExprParser.SifftFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#anglFunc.
    def visitAnglFunc(self, ctx:MathExprParser.AnglFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PowFunc.
    def visitPowFunc(self, ctx:MathExprParser.PowFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#Atan2Func.
    def visitAtan2Func(self, ctx:MathExprParser.Atan2FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#TMinFunc.
    def visitTMinFunc(self, ctx:MathExprParser.TMinFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#TMaxFunc.
    def visitTMaxFunc(self, ctx:MathExprParser.TMaxFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ClampFunc.
    def visitClampFunc(self, ctx:MathExprParser.ClampFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SMinFunc.
    def visitSMinFunc(self, ctx:MathExprParser.SMinFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SMaxFunc.
    def visitSMaxFunc(self, ctx:MathExprParser.SMaxFuncContext):
        return self.visitChildren(ctx)



del MathExprParser