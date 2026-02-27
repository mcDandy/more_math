# Generated from MathExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MathExprParser import MathExprParser
else:
    from MathExprParser import MathExprParser

# This class defines a complete generic visitor for a parse tree produced by MathExprParser.

class MathExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MathExprParser#start.
    def visitStart(self, ctx:MathExprParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#FunctionDef.
    def visitFunctionDef(self, ctx:MathExprParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#varDef.
    def visitVarDef(self, ctx:MathExprParser.VarDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#paramList.
    def visitParamList(self, ctx:MathExprParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#IfStatement.
    def visitIfStatement(self, ctx:MathExprParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#WhileStatement.
    def visitWhileStatement(self, ctx:MathExprParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BlockStatement.
    def visitBlockStatement(self, ctx:MathExprParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BreakStatement.
    def visitBreakStatement(self, ctx:MathExprParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ContinueStatement.
    def visitContinueStatement(self, ctx:MathExprParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ReturnStatement.
    def visitReturnStatement(self, ctx:MathExprParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#VarDefStmt.
    def visitVarDefStmt(self, ctx:MathExprParser.VarDefStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ForStatement.
    def visitForStatement(self, ctx:MathExprParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ExprStatement.
    def visitExprStatement(self, ctx:MathExprParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ifStmt.
    def visitIfStmt(self, ctx:MathExprParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#whileStmt.
    def visitWhileStmt(self, ctx:MathExprParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#forStmt.
    def visitForStmt(self, ctx:MathExprParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#block.
    def visitBlock(self, ctx:MathExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#breakStmt.
    def visitBreakStmt(self, ctx:MathExprParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#continueStmt.
    def visitContinueStmt(self, ctx:MathExprParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#returnStmt.
    def visitReturnStmt(self, ctx:MathExprParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#expr.
    def visitExpr(self, ctx:MathExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#TernaryExp.
    def visitTernaryExp(self, ctx:MathExprParser.TernaryExpContext):
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


    # Visit a parse tree produced by MathExprParser#ToShift.
    def visitToShift(self, ctx:MathExprParser.ToShiftContext):
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


    # Visit a parse tree produced by MathExprParser#RShiftExp.
    def visitRShiftExp(self, ctx:MathExprParser.RShiftExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#LShiftExp.
    def visitLShiftExp(self, ctx:MathExprParser.LShiftExpContext):
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


    # Visit a parse tree produced by MathExprParser#ToIndex.
    def visitToIndex(self, ctx:MathExprParser.ToIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#IndexExp.
    def visitIndexExp(self, ctx:MathExprParser.IndexExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ToAtom.
    def visitToAtom(self, ctx:MathExprParser.ToAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#Func0Exp.
    def visitFunc0Exp(self, ctx:MathExprParser.Func0ExpContext):
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


    # Visit a parse tree produced by MathExprParser#Func4Exp.
    def visitFunc4Exp(self, ctx:MathExprParser.Func4ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#Func5Exp.
    def visitFunc5Exp(self, ctx:MathExprParser.Func5ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#FuncNExp.
    def visitFuncNExp(self, ctx:MathExprParser.FuncNExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#FuncNoiseExp.
    def visitFuncNoiseExp(self, ctx:MathExprParser.FuncNoiseExpContext):
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


    # Visit a parse tree produced by MathExprParser#StringExp.
    def visitStringExp(self, ctx:MathExprParser.StringExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ParenExp.
    def visitParenExp(self, ctx:MathExprParser.ParenExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AbsExp.
    def visitAbsExp(self, ctx:MathExprParser.AbsExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ListExp.
    def visitListExp(self, ctx:MathExprParser.ListExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CallExp.
    def visitCallExp(self, ctx:MathExprParser.CallExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#NoneExp.
    def visitNoneExp(self, ctx:MathExprParser.NoneExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BreakExp.
    def visitBreakExp(self, ctx:MathExprParser.BreakExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ContinueExp.
    def visitContinueExp(self, ctx:MathExprParser.ContinueExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#exprList.
    def visitExprList(self, ctx:MathExprParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#TimestampFunc.
    def visitTimestampFunc(self, ctx:MathExprParser.TimestampFuncContext):
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


    # Visit a parse tree produced by MathExprParser#anglFunc.
    def visitAnglFunc(self, ctx:MathExprParser.AnglFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#printFunc.
    def visitPrintFunc(self, ctx:MathExprParser.PrintFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ReluFunc.
    def visitReluFunc(self, ctx:MathExprParser.ReluFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SoftplusFunc.
    def visitSoftplusFunc(self, ctx:MathExprParser.SoftplusFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#GeluFunc.
    def visitGeluFunc(self, ctx:MathExprParser.GeluFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SignFunc.
    def visitSignFunc(self, ctx:MathExprParser.SignFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PrintShapeFunc.
    def visitPrintShapeFunc(self, ctx:MathExprParser.PrintShapeFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PinvFunc.
    def visitPinvFunc(self, ctx:MathExprParser.PinvFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SumFunc.
    def visitSumFunc(self, ctx:MathExprParser.SumFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#MeanFunc.
    def visitMeanFunc(self, ctx:MathExprParser.MeanFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#StdFunc.
    def visitStdFunc(self, ctx:MathExprParser.StdFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#VarFunc.
    def visitVarFunc(self, ctx:MathExprParser.VarFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SortFunc.
    def visitSortFunc(self, ctx:MathExprParser.SortFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AnyFunc.
    def visitAnyFunc(self, ctx:MathExprParser.AnyFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AllFunc.
    def visitAllFunc(self, ctx:MathExprParser.AllFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#EdgeFunc.
    def visitEdgeFunc(self, ctx:MathExprParser.EdgeFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#MedianFunc.
    def visitMedianFunc(self, ctx:MathExprParser.MedianFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ModeFunc.
    def visitModeFunc(self, ctx:MathExprParser.ModeFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CumsumFunc.
    def visitCumsumFunc(self, ctx:MathExprParser.CumsumFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CountFunc.
    def visitCountFunc(self, ctx:MathExprParser.CountFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CumprodFunc.
    def visitCumprodFunc(self, ctx:MathExprParser.CumprodFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PopFunc.
    def visitPopFunc(self, ctx:MathExprParser.PopFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ClearFunc.
    def visitClearFunc(self, ctx:MathExprParser.ClearFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#HasFunc.
    def visitHasFunc(self, ctx:MathExprParser.HasFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#GetFunc.
    def visitGetFunc(self, ctx:MathExprParser.GetFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ArgsortFunc.
    def visitArgsortFunc(self, ctx:MathExprParser.ArgsortFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ArgminFunc.
    def visitArgminFunc(self, ctx:MathExprParser.ArgminFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ArgmaxFunc.
    def visitArgmaxFunc(self, ctx:MathExprParser.ArgmaxFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SoftmaxFunc.
    def visitSoftmaxFunc(self, ctx:MathExprParser.SoftmaxFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SoftminFunc.
    def visitSoftminFunc(self, ctx:MathExprParser.SoftminFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#UniqueFunc.
    def visitUniqueFunc(self, ctx:MathExprParser.UniqueFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#FlattenFunc.
    def visitFlattenFunc(self, ctx:MathExprParser.FlattenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#MotionMaskFunc.
    def visitMotionMaskFunc(self, ctx:MathExprParser.MotionMaskFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#FlowToImageFunc.
    def visitFlowToImageFunc(self, ctx:MathExprParser.FlowToImageFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BitNotFunc.
    def visitBitNotFunc(self, ctx:MathExprParser.BitNotFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BitCountFunc.
    def visitBitCountFunc(self, ctx:MathExprParser.BitCountFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ShapeFunc.
    def visitShapeFunc(self, ctx:MathExprParser.ShapeFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#UpperFunc.
    def visitUpperFunc(self, ctx:MathExprParser.UpperFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#LowerFunc.
    def visitLowerFunc(self, ctx:MathExprParser.LowerFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#TrimFunc.
    def visitTrimFunc(self, ctx:MathExprParser.TrimFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#EntropyFunc.
    def visitEntropyFunc(self, ctx:MathExprParser.EntropyFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#DilateFunc.
    def visitDilateFunc(self, ctx:MathExprParser.DilateFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ErodeFunc.
    def visitErodeFunc(self, ctx:MathExprParser.ErodeFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#MorphOpenFunc.
    def visitMorphOpenFunc(self, ctx:MathExprParser.MorphOpenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#MorphCloseFunc.
    def visitMorphCloseFunc(self, ctx:MathExprParser.MorphCloseFuncContext):
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


    # Visit a parse tree produced by MathExprParser#StepFunc.
    def visitStepFunc(self, ctx:MathExprParser.StepFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#TopkFunc.
    def visitTopkFunc(self, ctx:MathExprParser.TopkFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BotkFunc.
    def visitBotkFunc(self, ctx:MathExprParser.BotkFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#QuartileFunc.
    def visitQuartileFunc(self, ctx:MathExprParser.QuartileFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PercentileFunc.
    def visitPercentileFunc(self, ctx:MathExprParser.PercentileFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#QuantileFunc.
    def visitQuantileFunc(self, ctx:MathExprParser.QuantileFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#DotFunc.
    def visitDotFunc(self, ctx:MathExprParser.DotFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CossimFunc.
    def visitCossimFunc(self, ctx:MathExprParser.CossimFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#FlipFunc.
    def visitFlipFunc(self, ctx:MathExprParser.FlipFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CovFunc.
    def visitCovFunc(self, ctx:MathExprParser.CovFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CorrFunc.
    def visitCorrFunc(self, ctx:MathExprParser.CorrFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#AppendFunc.
    def visitAppendFunc(self, ctx:MathExprParser.AppendFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#GaussianFunc.
    def visitGaussianFunc(self, ctx:MathExprParser.GaussianFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#TopkIndFunc.
    def visitTopkIndFunc(self, ctx:MathExprParser.TopkIndFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BotkIndFunc.
    def visitBotkIndFunc(self, ctx:MathExprParser.BotkIndFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BatchShuffleFunc.
    def visitBatchShuffleFunc(self, ctx:MathExprParser.BatchShuffleFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PushFunc.
    def visitPushFunc(self, ctx:MathExprParser.PushFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#GetValueFunc.
    def visitGetValueFunc(self, ctx:MathExprParser.GetValueFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#EmptyTensorFunc.
    def visitEmptyTensorFunc(self, ctx:MathExprParser.EmptyTensorFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PadFunc.
    def visitPadFunc(self, ctx:MathExprParser.PadFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CrossFunc.
    def visitCrossFunc(self, ctx:MathExprParser.CrossFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#MatmulFunc.
    def visitMatmulFunc(self, ctx:MathExprParser.MatmulFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#FlowApplyFunc.
    def visitFlowApplyFunc(self, ctx:MathExprParser.FlowApplyFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#RifeFunc.
    def visitRifeFunc(self, ctx:MathExprParser.RifeFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BitAndFunc.
    def visitBitAndFunc(self, ctx:MathExprParser.BitAndFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BitXorFunc.
    def visitBitXorFunc(self, ctx:MathExprParser.BitXorFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BitOrFunc.
    def visitBitOrFunc(self, ctx:MathExprParser.BitOrFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SplitFunc.
    def visitSplitFunc(self, ctx:MathExprParser.SplitFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#JoinFunc.
    def visitJoinFunc(self, ctx:MathExprParser.JoinFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SubstringFunc.
    def visitSubstringFunc(self, ctx:MathExprParser.SubstringFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#FindFunc.
    def visitFindFunc(self, ctx:MathExprParser.FindFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ReplaceFunc.
    def visitReplaceFunc(self, ctx:MathExprParser.ReplaceFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ClampFunc.
    def visitClampFunc(self, ctx:MathExprParser.ClampFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#LerpFunc.
    def visitLerpFunc(self, ctx:MathExprParser.LerpFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SmoothstepFunc.
    def visitSmoothstepFunc(self, ctx:MathExprParser.SmoothstepFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#RangeFunc.
    def visitRangeFunc(self, ctx:MathExprParser.RangeFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#MomentFunc.
    def visitMomentFunc(self, ctx:MathExprParser.MomentFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CubicEaseFunc.
    def visitCubicEaseFunc(self, ctx:MathExprParser.CubicEaseFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ElasticEaseFunc.
    def visitElasticEaseFunc(self, ctx:MathExprParser.ElasticEaseFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SineEaseFunc.
    def visitSineEaseFunc(self, ctx:MathExprParser.SineEaseFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SmootherstepFunc.
    def visitSmootherstepFunc(self, ctx:MathExprParser.SmootherstepFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CropFunc.
    def visitCropFunc(self, ctx:MathExprParser.CropFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#sifftFunc.
    def visitSifftFunc(self, ctx:MathExprParser.SifftFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#OverlayFunc.
    def visitOverlayFunc(self, ctx:MathExprParser.OverlayFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#RgbToHsvFunc.
    def visitRgbToHsvFunc(self, ctx:MathExprParser.RgbToHsvFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#HsvToRgbFunc.
    def visitHsvToRgbFunc(self, ctx:MathExprParser.HsvToRgbFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SwapFunc.
    def visitSwapFunc(self, ctx:MathExprParser.SwapFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#NvlFunc.
    def visitNvlFunc(self, ctx:MathExprParser.NvlFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#DistFunc.
    def visitDistFunc(self, ctx:MathExprParser.DistFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#RemapFunc.
    def visitRemapFunc(self, ctx:MathExprParser.RemapFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SMinFunc.
    def visitSMinFunc(self, ctx:MathExprParser.SMinFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#SMaxFunc.
    def visitSMaxFunc(self, ctx:MathExprParser.SMaxFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#MapFunc.
    def visitMapFunc(self, ctx:MathExprParser.MapFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#EzConvFunc.
    def visitEzConvFunc(self, ctx:MathExprParser.EzConvFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ConvFunc.
    def visitConvFunc(self, ctx:MathExprParser.ConvFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PermuteFunc.
    def visitPermuteFunc(self, ctx:MathExprParser.PermuteFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ReshapeFunc.
    def visitReshapeFunc(self, ctx:MathExprParser.ReshapeFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#NoiseFunc.
    def visitNoiseFunc(self, ctx:MathExprParser.NoiseFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#RandFunc.
    def visitRandFunc(self, ctx:MathExprParser.RandFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#ExponentialFunc.
    def visitExponentialFunc(self, ctx:MathExprParser.ExponentialFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BernoulliFunc.
    def visitBernoulliFunc(self, ctx:MathExprParser.BernoulliFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PoissonFunc.
    def visitPoissonFunc(self, ctx:MathExprParser.PoissonFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CauchyFunc.
    def visitCauchyFunc(self, ctx:MathExprParser.CauchyFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#LogNormalFunc.
    def visitLogNormalFunc(self, ctx:MathExprParser.LogNormalFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#GammaDistFunc.
    def visitGammaDistFunc(self, ctx:MathExprParser.GammaDistFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#BetaDistFunc.
    def visitBetaDistFunc(self, ctx:MathExprParser.BetaDistFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#LaplaceDistFunc.
    def visitLaplaceDistFunc(self, ctx:MathExprParser.LaplaceDistFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#GumbelDistFunc.
    def visitGumbelDistFunc(self, ctx:MathExprParser.GumbelDistFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#WeibullDistFunc.
    def visitWeibullDistFunc(self, ctx:MathExprParser.WeibullDistFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#Chi2DistFunc.
    def visitChi2DistFunc(self, ctx:MathExprParser.Chi2DistFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#StudentTDistFunc.
    def visitStudentTDistFunc(self, ctx:MathExprParser.StudentTDistFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PerlinFunc.
    def visitPerlinFunc(self, ctx:MathExprParser.PerlinFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#CellularFunc.
    def visitCellularFunc(self, ctx:MathExprParser.CellularFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathExprParser#PlasmaFunc.
    def visitPlasmaFunc(self, ctx:MathExprParser.PlasmaFuncContext):
        return self.visitChildren(ctx)



del MathExprParser