// Generated from ./MathExpr.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MathExprParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MathExprVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MathExprParser#start}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStart(MathExprParser.StartContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FunctionDef}
	 * labeled alternative in {@link MathExprParser#funcDef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionDef(MathExprParser.FunctionDefContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#varDef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarDef(MathExprParser.VarDefContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#paramList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParamList(MathExprParser.ParamListContext ctx);
	/**
	 * Visit a parse tree produced by the {@code IfStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStatement(MathExprParser.IfStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code WhileStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStatement(MathExprParser.WhileStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BlockStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlockStatement(MathExprParser.BlockStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BreakStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreakStatement(MathExprParser.BreakStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ContinueStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContinueStatement(MathExprParser.ContinueStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ReturnStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStatement(MathExprParser.ReturnStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code VarDefStmt}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarDefStmt(MathExprParser.VarDefStmtContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ForStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForStatement(MathExprParser.ForStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprStatement(MathExprParser.ExprStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#ifStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStmt(MathExprParser.IfStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#whileStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStmt(MathExprParser.WhileStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#forStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForStmt(MathExprParser.ForStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(MathExprParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#breakStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreakStmt(MathExprParser.BreakStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#continueStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContinueStmt(MathExprParser.ContinueStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#returnStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStmt(MathExprParser.ReturnStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(MathExprParser.ExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TernaryExp}
	 * labeled alternative in {@link MathExprParser#ternaryExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTernaryExp(MathExprParser.TernaryExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LtExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLtExp(MathExprParser.LtExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code EqExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEqExp(MathExprParser.EqExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ToAdd}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitToAdd(MathExprParser.ToAddContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GeExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGeExp(MathExprParser.GeExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LeExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLeExp(MathExprParser.LeExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code NeExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNeExp(MathExprParser.NeExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GtExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGtExp(MathExprParser.GtExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AddExp}
	 * labeled alternative in {@link MathExprParser#addExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddExp(MathExprParser.AddExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ToMul}
	 * labeled alternative in {@link MathExprParser#addExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitToMul(MathExprParser.ToMulContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SubExp}
	 * labeled alternative in {@link MathExprParser#addExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubExp(MathExprParser.SubExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ToShift}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitToShift(MathExprParser.ToShiftContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MulExp}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMulExp(MathExprParser.MulExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ModExp}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModExp(MathExprParser.ModExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code DivExp}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDivExp(MathExprParser.DivExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RShiftExp}
	 * labeled alternative in {@link MathExprParser#shiftExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRShiftExp(MathExprParser.RShiftExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LShiftExp}
	 * labeled alternative in {@link MathExprParser#shiftExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLShiftExp(MathExprParser.LShiftExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ToPow}
	 * labeled alternative in {@link MathExprParser#shiftExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitToPow(MathExprParser.ToPowContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PowExp}
	 * labeled alternative in {@link MathExprParser#powExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPowExp(MathExprParser.PowExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ToUnary}
	 * labeled alternative in {@link MathExprParser#powExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitToUnary(MathExprParser.ToUnaryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code UnaryPlus}
	 * labeled alternative in {@link MathExprParser#unaryExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryPlus(MathExprParser.UnaryPlusContext ctx);
	/**
	 * Visit a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link MathExprParser#unaryExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryMinus(MathExprParser.UnaryMinusContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ToIndex}
	 * labeled alternative in {@link MathExprParser#unaryExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitToIndex(MathExprParser.ToIndexContext ctx);
	/**
	 * Visit a parse tree produced by the {@code IndexExp}
	 * labeled alternative in {@link MathExprParser#indexExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndexExp(MathExprParser.IndexExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ToAtom}
	 * labeled alternative in {@link MathExprParser#indexExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitToAtom(MathExprParser.ToAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Func0Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc0Exp(MathExprParser.Func0ExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Func1Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc1Exp(MathExprParser.Func1ExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Func2Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc2Exp(MathExprParser.Func2ExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Func3Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc3Exp(MathExprParser.Func3ExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Func4Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc4Exp(MathExprParser.Func4ExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Func5Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc5Exp(MathExprParser.Func5ExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FuncNExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncNExp(MathExprParser.FuncNExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FuncNoiseExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncNoiseExp(MathExprParser.FuncNoiseExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code VariableExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariableExp(MathExprParser.VariableExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code NumberExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumberExp(MathExprParser.NumberExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ConstantExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstantExp(MathExprParser.ConstantExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StringExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStringExp(MathExprParser.StringExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ParenExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParenExp(MathExprParser.ParenExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AbsExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAbsExp(MathExprParser.AbsExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ListExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListExp(MathExprParser.ListExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CallExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCallExp(MathExprParser.CallExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code NoneExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNoneExp(MathExprParser.NoneExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BreakExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreakExp(MathExprParser.BreakExpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ContinueExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContinueExp(MathExprParser.ContinueExpContext ctx);
	/**
	 * Visit a parse tree produced by {@link MathExprParser#exprList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprList(MathExprParser.ExprListContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TimestampFunc}
	 * labeled alternative in {@link MathExprParser#func0}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTimestampFunc(MathExprParser.TimestampFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SinFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSinFunc(MathExprParser.SinFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CosFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCosFunc(MathExprParser.CosFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TanFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTanFunc(MathExprParser.TanFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AsinFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAsinFunc(MathExprParser.AsinFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AcosFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAcosFunc(MathExprParser.AcosFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AtanFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtanFunc(MathExprParser.AtanFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SinhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSinhFunc(MathExprParser.SinhFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CoshFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCoshFunc(MathExprParser.CoshFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TanhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTanhFunc(MathExprParser.TanhFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AsinhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAsinhFunc(MathExprParser.AsinhFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AcoshFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAcoshFunc(MathExprParser.AcoshFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AtanhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtanhFunc(MathExprParser.AtanhFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AbsFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAbsFunc(MathExprParser.AbsFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SqrtFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSqrtFunc(MathExprParser.SqrtFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LnFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLnFunc(MathExprParser.LnFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LogFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogFunc(MathExprParser.LogFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExpFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpFunc(MathExprParser.ExpFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TNormFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTNormFunc(MathExprParser.TNormFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SNormFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSNormFunc(MathExprParser.SNormFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FloorFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFloorFunc(MathExprParser.FloorFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CeilFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCeilFunc(MathExprParser.CeilFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RoundFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoundFunc(MathExprParser.RoundFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GammaFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGammaFunc(MathExprParser.GammaFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code sigmoidFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSigmoidFunc(MathExprParser.SigmoidFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code anglFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAnglFunc(MathExprParser.AnglFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code printFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrintFunc(MathExprParser.PrintFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FractFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFractFunc(MathExprParser.FractFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ReluFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReluFunc(MathExprParser.ReluFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SoftplusFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSoftplusFunc(MathExprParser.SoftplusFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GeluFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGeluFunc(MathExprParser.GeluFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SignFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSignFunc(MathExprParser.SignFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PrintShapeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrintShapeFunc(MathExprParser.PrintShapeFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PinvFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPinvFunc(MathExprParser.PinvFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SumFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSumFunc(MathExprParser.SumFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MeanFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMeanFunc(MathExprParser.MeanFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StdFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStdFunc(MathExprParser.StdFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code VarFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarFunc(MathExprParser.VarFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SortFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSortFunc(MathExprParser.SortFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AnyFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAnyFunc(MathExprParser.AnyFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AllFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAllFunc(MathExprParser.AllFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code EdgeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEdgeFunc(MathExprParser.EdgeFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MedianFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMedianFunc(MathExprParser.MedianFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ModeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModeFunc(MathExprParser.ModeFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CumsumFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCumsumFunc(MathExprParser.CumsumFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CountFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCountFunc(MathExprParser.CountFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CumprodFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCumprodFunc(MathExprParser.CumprodFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PopFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPopFunc(MathExprParser.PopFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ClearFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClearFunc(MathExprParser.ClearFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code HasFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHasFunc(MathExprParser.HasFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GetFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGetFunc(MathExprParser.GetFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ArgsortFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgsortFunc(MathExprParser.ArgsortFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ArgminFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgminFunc(MathExprParser.ArgminFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ArgmaxFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgmaxFunc(MathExprParser.ArgmaxFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SoftmaxFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSoftmaxFunc(MathExprParser.SoftmaxFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SoftminFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSoftminFunc(MathExprParser.SoftminFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ErfFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitErfFunc(MathExprParser.ErfFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ErfinvFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitErfinvFunc(MathExprParser.ErfinvFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code UniqueFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUniqueFunc(MathExprParser.UniqueFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FlattenFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlattenFunc(MathExprParser.FlattenFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MotionMaskFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMotionMaskFunc(MathExprParser.MotionMaskFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FlowToImageFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlowToImageFunc(MathExprParser.FlowToImageFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BitNotFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitNotFunc(MathExprParser.BitNotFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BitCountFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitCountFunc(MathExprParser.BitCountFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ShapeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShapeFunc(MathExprParser.ShapeFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code UpperFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUpperFunc(MathExprParser.UpperFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LowerFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLowerFunc(MathExprParser.LowerFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TrimFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTrimFunc(MathExprParser.TrimFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code EntropyFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEntropyFunc(MathExprParser.EntropyFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SfftFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSfftFunc(MathExprParser.SfftFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code DilateFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDilateFunc(MathExprParser.DilateFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ErodeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitErodeFunc(MathExprParser.ErodeFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MorphOpenFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMorphOpenFunc(MathExprParser.MorphOpenFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MorphCloseFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMorphCloseFunc(MathExprParser.MorphCloseFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code IntFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntFunc(MathExprParser.IntFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FloatFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFloatFunc(MathExprParser.FloatFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FlowMagFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlowMagFunc(MathExprParser.FlowMagFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FlowAngFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlowAngFunc(MathExprParser.FlowAngFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PowFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPowFunc(MathExprParser.PowFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Atan2Func}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtan2Func(MathExprParser.Atan2FuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TMinFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTMinFunc(MathExprParser.TMinFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TMaxFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTMaxFunc(MathExprParser.TMaxFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StepFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStepFunc(MathExprParser.StepFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TopkFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTopkFunc(MathExprParser.TopkFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BotkFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBotkFunc(MathExprParser.BotkFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code QuartileFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuartileFunc(MathExprParser.QuartileFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PercentileFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPercentileFunc(MathExprParser.PercentileFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code QuantileFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuantileFunc(MathExprParser.QuantileFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code DotFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDotFunc(MathExprParser.DotFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CossimFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCossimFunc(MathExprParser.CossimFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FlipFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlipFunc(MathExprParser.FlipFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CovFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCovFunc(MathExprParser.CovFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CorrFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCorrFunc(MathExprParser.CorrFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AppendFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAppendFunc(MathExprParser.AppendFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PermuteFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPermuteFunc(MathExprParser.PermuteFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GaussianFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGaussianFunc(MathExprParser.GaussianFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TopkIndFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTopkIndFunc(MathExprParser.TopkIndFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BotkIndFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBotkIndFunc(MathExprParser.BotkIndFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BatchShuffleFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBatchShuffleFunc(MathExprParser.BatchShuffleFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PushFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPushFunc(MathExprParser.PushFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GetValueFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGetValueFunc(MathExprParser.GetValueFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code EmptyTensorFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEmptyTensorFunc(MathExprParser.EmptyTensorFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PadFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPadFunc(MathExprParser.PadFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CrossFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCrossFunc(MathExprParser.CrossFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MatmulFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMatmulFunc(MathExprParser.MatmulFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FlowApplyFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlowApplyFunc(MathExprParser.FlowApplyFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RifeFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRifeFunc(MathExprParser.RifeFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BitAndFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitAndFunc(MathExprParser.BitAndFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BitXorFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitXorFunc(MathExprParser.BitXorFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BitOrFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitOrFunc(MathExprParser.BitOrFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SplitFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSplitFunc(MathExprParser.SplitFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code JoinFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitJoinFunc(MathExprParser.JoinFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SubstringFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubstringFunc(MathExprParser.SubstringFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FindFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFindFunc(MathExprParser.FindFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ReplaceFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReplaceFunc(MathExprParser.ReplaceFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Int_to_rgbFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInt_to_rgbFunc(MathExprParser.Int_to_rgbFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Rgb_to_intFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRgb_to_intFunc(MathExprParser.Rgb_to_intFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code InterpolateLinearFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInterpolateLinearFunc(MathExprParser.InterpolateLinearFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code InterpolateAreaFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInterpolateAreaFunc(MathExprParser.InterpolateAreaFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code InterpolateNearestExactFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInterpolateNearestExactFunc(MathExprParser.InterpolateNearestExactFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ClampFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClampFunc(MathExprParser.ClampFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LerpFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLerpFunc(MathExprParser.LerpFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SmoothstepFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSmoothstepFunc(MathExprParser.SmoothstepFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RangeFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRangeFunc(MathExprParser.RangeFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MomentFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMomentFunc(MathExprParser.MomentFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CubicEaseFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCubicEaseFunc(MathExprParser.CubicEaseFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ElasticEaseFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElasticEaseFunc(MathExprParser.ElasticEaseFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SineEaseFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSineEaseFunc(MathExprParser.SineEaseFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SmootherstepFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSmootherstepFunc(MathExprParser.SmootherstepFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CropFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCropFunc(MathExprParser.CropFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SifftFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSifftFunc(MathExprParser.SifftFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code OverlayFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOverlayFunc(MathExprParser.OverlayFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LinspaceFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLinspaceFunc(MathExprParser.LinspaceFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RollFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRollFunc(MathExprParser.RollFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RgbToOklabFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRgbToOklabFunc(MathExprParser.RgbToOklabFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RgbToCilabFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRgbToCilabFunc(MathExprParser.RgbToCilabFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RgbToHsvFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRgbToHsvFunc(MathExprParser.RgbToHsvFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code HsvToRgbFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHsvToRgbFunc(MathExprParser.HsvToRgbFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code WhereFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhereFunc(MathExprParser.WhereFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code OklabToRgbFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOklabToRgbFunc(MathExprParser.OklabToRgbFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CilabToRgbFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCilabToRgbFunc(MathExprParser.CilabToRgbFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SwapFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSwapFunc(MathExprParser.SwapFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code NvlFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNvlFunc(MathExprParser.NvlFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LogspaceFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogspaceFunc(MathExprParser.LogspaceFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code DistFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDistFunc(MathExprParser.DistFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code HistogramFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHistogramFunc(MathExprParser.HistogramFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RemapFunc}
	 * labeled alternative in {@link MathExprParser#func5}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRemapFunc(MathExprParser.RemapFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SMinFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSMinFunc(MathExprParser.SMinFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code SMaxFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSMaxFunc(MathExprParser.SMaxFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MapFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMapFunc(MathExprParser.MapFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code EzConvFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEzConvFunc(MathExprParser.EzConvFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ConvFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConvFunc(MathExprParser.ConvFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ReshapeFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReshapeFunc(MathExprParser.ReshapeFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ConcatFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConcatFunc(MathExprParser.ConcatFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code NoiseFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNoiseFunc(MathExprParser.NoiseFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RandFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRandFunc(MathExprParser.RandFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExponentialFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExponentialFunc(MathExprParser.ExponentialFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BernoulliFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBernoulliFunc(MathExprParser.BernoulliFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PoissonFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPoissonFunc(MathExprParser.PoissonFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CauchyFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCauchyFunc(MathExprParser.CauchyFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LogNormalFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogNormalFunc(MathExprParser.LogNormalFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GammaDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGammaDistFunc(MathExprParser.GammaDistFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BetaDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBetaDistFunc(MathExprParser.BetaDistFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LaplaceDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLaplaceDistFunc(MathExprParser.LaplaceDistFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GumbelDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGumbelDistFunc(MathExprParser.GumbelDistFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code WeibullDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWeibullDistFunc(MathExprParser.WeibullDistFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Chi2DistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChi2DistFunc(MathExprParser.Chi2DistFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StudentTDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStudentTDistFunc(MathExprParser.StudentTDistFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PerlinFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPerlinFunc(MathExprParser.PerlinFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CellularFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCellularFunc(MathExprParser.CellularFuncContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PlasmaFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPlasmaFunc(MathExprParser.PlasmaFuncContext ctx);
}