// Generated from ./MathExpr.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MathExprParser}.
 */
public interface MathExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MathExprParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(MathExprParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(MathExprParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FunctionDef}
	 * labeled alternative in {@link MathExprParser#funcDef}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDef(MathExprParser.FunctionDefContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FunctionDef}
	 * labeled alternative in {@link MathExprParser#funcDef}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDef(MathExprParser.FunctionDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#varDef}.
	 * @param ctx the parse tree
	 */
	void enterVarDef(MathExprParser.VarDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#varDef}.
	 * @param ctx the parse tree
	 */
	void exitVarDef(MathExprParser.VarDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(MathExprParser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(MathExprParser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IfStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(MathExprParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IfStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(MathExprParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code WhileStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(MathExprParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code WhileStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(MathExprParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BlockStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterBlockStatement(MathExprParser.BlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BlockStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitBlockStatement(MathExprParser.BlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BreakStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakStatement(MathExprParser.BreakStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BreakStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakStatement(MathExprParser.BreakStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ContinueStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(MathExprParser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ContinueStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(MathExprParser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ReturnStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(MathExprParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ReturnStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(MathExprParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code VarDefStmt}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterVarDefStmt(MathExprParser.VarDefStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code VarDefStmt}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitVarDefStmt(MathExprParser.VarDefStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ForStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(MathExprParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ForStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(MathExprParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterExprStatement(MathExprParser.ExprStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprStatement}
	 * labeled alternative in {@link MathExprParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitExprStatement(MathExprParser.ExprStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(MathExprParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(MathExprParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(MathExprParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(MathExprParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void enterForStmt(MathExprParser.ForStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void exitForStmt(MathExprParser.ForStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(MathExprParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(MathExprParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakStmt(MathExprParser.BreakStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakStmt(MathExprParser.BreakStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void enterContinueStmt(MathExprParser.ContinueStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void exitContinueStmt(MathExprParser.ContinueStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnStmt(MathExprParser.ReturnStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnStmt(MathExprParser.ReturnStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MathExprParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MathExprParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TernaryExp}
	 * labeled alternative in {@link MathExprParser#ternaryExpr}.
	 * @param ctx the parse tree
	 */
	void enterTernaryExp(MathExprParser.TernaryExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TernaryExp}
	 * labeled alternative in {@link MathExprParser#ternaryExpr}.
	 * @param ctx the parse tree
	 */
	void exitTernaryExp(MathExprParser.TernaryExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LtExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void enterLtExp(MathExprParser.LtExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LtExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void exitLtExp(MathExprParser.LtExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EqExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void enterEqExp(MathExprParser.EqExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EqExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void exitEqExp(MathExprParser.EqExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ToAdd}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void enterToAdd(MathExprParser.ToAddContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ToAdd}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void exitToAdd(MathExprParser.ToAddContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GeExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void enterGeExp(MathExprParser.GeExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GeExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void exitGeExp(MathExprParser.GeExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LeExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void enterLeExp(MathExprParser.LeExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LeExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void exitLeExp(MathExprParser.LeExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NeExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void enterNeExp(MathExprParser.NeExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NeExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void exitNeExp(MathExprParser.NeExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GtExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void enterGtExp(MathExprParser.GtExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GtExp}
	 * labeled alternative in {@link MathExprParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void exitGtExp(MathExprParser.GtExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddExp}
	 * labeled alternative in {@link MathExprParser#addExpr}.
	 * @param ctx the parse tree
	 */
	void enterAddExp(MathExprParser.AddExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddExp}
	 * labeled alternative in {@link MathExprParser#addExpr}.
	 * @param ctx the parse tree
	 */
	void exitAddExp(MathExprParser.AddExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ToMul}
	 * labeled alternative in {@link MathExprParser#addExpr}.
	 * @param ctx the parse tree
	 */
	void enterToMul(MathExprParser.ToMulContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ToMul}
	 * labeled alternative in {@link MathExprParser#addExpr}.
	 * @param ctx the parse tree
	 */
	void exitToMul(MathExprParser.ToMulContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SubExp}
	 * labeled alternative in {@link MathExprParser#addExpr}.
	 * @param ctx the parse tree
	 */
	void enterSubExp(MathExprParser.SubExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SubExp}
	 * labeled alternative in {@link MathExprParser#addExpr}.
	 * @param ctx the parse tree
	 */
	void exitSubExp(MathExprParser.SubExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ToShift}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 */
	void enterToShift(MathExprParser.ToShiftContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ToShift}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 */
	void exitToShift(MathExprParser.ToShiftContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulExp}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 */
	void enterMulExp(MathExprParser.MulExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulExp}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 */
	void exitMulExp(MathExprParser.MulExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ModExp}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 */
	void enterModExp(MathExprParser.ModExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ModExp}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 */
	void exitModExp(MathExprParser.ModExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DivExp}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 */
	void enterDivExp(MathExprParser.DivExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DivExp}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 */
	void exitDivExp(MathExprParser.DivExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RShiftExp}
	 * labeled alternative in {@link MathExprParser#shiftExpr}.
	 * @param ctx the parse tree
	 */
	void enterRShiftExp(MathExprParser.RShiftExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RShiftExp}
	 * labeled alternative in {@link MathExprParser#shiftExpr}.
	 * @param ctx the parse tree
	 */
	void exitRShiftExp(MathExprParser.RShiftExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LShiftExp}
	 * labeled alternative in {@link MathExprParser#shiftExpr}.
	 * @param ctx the parse tree
	 */
	void enterLShiftExp(MathExprParser.LShiftExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LShiftExp}
	 * labeled alternative in {@link MathExprParser#shiftExpr}.
	 * @param ctx the parse tree
	 */
	void exitLShiftExp(MathExprParser.LShiftExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ToPow}
	 * labeled alternative in {@link MathExprParser#shiftExpr}.
	 * @param ctx the parse tree
	 */
	void enterToPow(MathExprParser.ToPowContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ToPow}
	 * labeled alternative in {@link MathExprParser#shiftExpr}.
	 * @param ctx the parse tree
	 */
	void exitToPow(MathExprParser.ToPowContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PowExp}
	 * labeled alternative in {@link MathExprParser#powExpr}.
	 * @param ctx the parse tree
	 */
	void enterPowExp(MathExprParser.PowExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PowExp}
	 * labeled alternative in {@link MathExprParser#powExpr}.
	 * @param ctx the parse tree
	 */
	void exitPowExp(MathExprParser.PowExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ToUnary}
	 * labeled alternative in {@link MathExprParser#powExpr}.
	 * @param ctx the parse tree
	 */
	void enterToUnary(MathExprParser.ToUnaryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ToUnary}
	 * labeled alternative in {@link MathExprParser#powExpr}.
	 * @param ctx the parse tree
	 */
	void exitToUnary(MathExprParser.ToUnaryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryPlus}
	 * labeled alternative in {@link MathExprParser#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryPlus(MathExprParser.UnaryPlusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryPlus}
	 * labeled alternative in {@link MathExprParser#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryPlus(MathExprParser.UnaryPlusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link MathExprParser#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMinus(MathExprParser.UnaryMinusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link MathExprParser#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMinus(MathExprParser.UnaryMinusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ToIndex}
	 * labeled alternative in {@link MathExprParser#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void enterToIndex(MathExprParser.ToIndexContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ToIndex}
	 * labeled alternative in {@link MathExprParser#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void exitToIndex(MathExprParser.ToIndexContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IndexExp}
	 * labeled alternative in {@link MathExprParser#indexExpr}.
	 * @param ctx the parse tree
	 */
	void enterIndexExp(MathExprParser.IndexExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IndexExp}
	 * labeled alternative in {@link MathExprParser#indexExpr}.
	 * @param ctx the parse tree
	 */
	void exitIndexExp(MathExprParser.IndexExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ToAtom}
	 * labeled alternative in {@link MathExprParser#indexExpr}.
	 * @param ctx the parse tree
	 */
	void enterToAtom(MathExprParser.ToAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ToAtom}
	 * labeled alternative in {@link MathExprParser#indexExpr}.
	 * @param ctx the parse tree
	 */
	void exitToAtom(MathExprParser.ToAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Func0Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterFunc0Exp(MathExprParser.Func0ExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Func0Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitFunc0Exp(MathExprParser.Func0ExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Func1Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterFunc1Exp(MathExprParser.Func1ExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Func1Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitFunc1Exp(MathExprParser.Func1ExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Func2Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterFunc2Exp(MathExprParser.Func2ExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Func2Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitFunc2Exp(MathExprParser.Func2ExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Func3Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterFunc3Exp(MathExprParser.Func3ExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Func3Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitFunc3Exp(MathExprParser.Func3ExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Func4Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterFunc4Exp(MathExprParser.Func4ExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Func4Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitFunc4Exp(MathExprParser.Func4ExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Func5Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterFunc5Exp(MathExprParser.Func5ExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Func5Exp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitFunc5Exp(MathExprParser.Func5ExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FuncNExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterFuncNExp(MathExprParser.FuncNExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FuncNExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitFuncNExp(MathExprParser.FuncNExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FuncNoiseExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterFuncNoiseExp(MathExprParser.FuncNoiseExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FuncNoiseExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitFuncNoiseExp(MathExprParser.FuncNoiseExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code VariableExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterVariableExp(MathExprParser.VariableExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code VariableExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitVariableExp(MathExprParser.VariableExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NumberExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterNumberExp(MathExprParser.NumberExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NumberExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitNumberExp(MathExprParser.NumberExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ConstantExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterConstantExp(MathExprParser.ConstantExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ConstantExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitConstantExp(MathExprParser.ConstantExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StringExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterStringExp(MathExprParser.StringExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StringExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitStringExp(MathExprParser.StringExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterParenExp(MathExprParser.ParenExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitParenExp(MathExprParser.ParenExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AbsExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAbsExp(MathExprParser.AbsExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AbsExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAbsExp(MathExprParser.AbsExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ListExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterListExp(MathExprParser.ListExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ListExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitListExp(MathExprParser.ListExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CallExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterCallExp(MathExprParser.CallExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CallExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitCallExp(MathExprParser.CallExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NoneExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterNoneExp(MathExprParser.NoneExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NoneExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitNoneExp(MathExprParser.NoneExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BreakExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterBreakExp(MathExprParser.BreakExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BreakExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitBreakExp(MathExprParser.BreakExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ContinueExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterContinueExp(MathExprParser.ContinueExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ContinueExp}
	 * labeled alternative in {@link MathExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitContinueExp(MathExprParser.ContinueExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link MathExprParser#exprList}.
	 * @param ctx the parse tree
	 */
	void enterExprList(MathExprParser.ExprListContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathExprParser#exprList}.
	 * @param ctx the parse tree
	 */
	void exitExprList(MathExprParser.ExprListContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TimestampFunc}
	 * labeled alternative in {@link MathExprParser#func0}.
	 * @param ctx the parse tree
	 */
	void enterTimestampFunc(MathExprParser.TimestampFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TimestampFunc}
	 * labeled alternative in {@link MathExprParser#func0}.
	 * @param ctx the parse tree
	 */
	void exitTimestampFunc(MathExprParser.TimestampFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SinFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSinFunc(MathExprParser.SinFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SinFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSinFunc(MathExprParser.SinFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CosFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterCosFunc(MathExprParser.CosFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CosFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitCosFunc(MathExprParser.CosFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TanFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterTanFunc(MathExprParser.TanFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TanFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitTanFunc(MathExprParser.TanFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AsinFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterAsinFunc(MathExprParser.AsinFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AsinFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitAsinFunc(MathExprParser.AsinFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AcosFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterAcosFunc(MathExprParser.AcosFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AcosFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitAcosFunc(MathExprParser.AcosFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AtanFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterAtanFunc(MathExprParser.AtanFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AtanFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitAtanFunc(MathExprParser.AtanFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SinhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSinhFunc(MathExprParser.SinhFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SinhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSinhFunc(MathExprParser.SinhFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CoshFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterCoshFunc(MathExprParser.CoshFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CoshFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitCoshFunc(MathExprParser.CoshFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TanhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterTanhFunc(MathExprParser.TanhFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TanhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitTanhFunc(MathExprParser.TanhFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AsinhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterAsinhFunc(MathExprParser.AsinhFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AsinhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitAsinhFunc(MathExprParser.AsinhFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AcoshFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterAcoshFunc(MathExprParser.AcoshFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AcoshFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitAcoshFunc(MathExprParser.AcoshFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AtanhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterAtanhFunc(MathExprParser.AtanhFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AtanhFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitAtanhFunc(MathExprParser.AtanhFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AbsFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterAbsFunc(MathExprParser.AbsFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AbsFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitAbsFunc(MathExprParser.AbsFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SqrtFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSqrtFunc(MathExprParser.SqrtFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SqrtFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSqrtFunc(MathExprParser.SqrtFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LnFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterLnFunc(MathExprParser.LnFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LnFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitLnFunc(MathExprParser.LnFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterLogFunc(MathExprParser.LogFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitLogFunc(MathExprParser.LogFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExpFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterExpFunc(MathExprParser.ExpFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExpFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitExpFunc(MathExprParser.ExpFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TNormFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterTNormFunc(MathExprParser.TNormFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TNormFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitTNormFunc(MathExprParser.TNormFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SNormFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSNormFunc(MathExprParser.SNormFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SNormFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSNormFunc(MathExprParser.SNormFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FloorFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterFloorFunc(MathExprParser.FloorFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FloorFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitFloorFunc(MathExprParser.FloorFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CeilFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterCeilFunc(MathExprParser.CeilFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CeilFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitCeilFunc(MathExprParser.CeilFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RoundFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterRoundFunc(MathExprParser.RoundFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RoundFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitRoundFunc(MathExprParser.RoundFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GammaFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterGammaFunc(MathExprParser.GammaFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GammaFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitGammaFunc(MathExprParser.GammaFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code sigmoidFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSigmoidFunc(MathExprParser.SigmoidFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sigmoidFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSigmoidFunc(MathExprParser.SigmoidFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code anglFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterAnglFunc(MathExprParser.AnglFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code anglFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitAnglFunc(MathExprParser.AnglFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterPrintFunc(MathExprParser.PrintFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitPrintFunc(MathExprParser.PrintFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FractFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterFractFunc(MathExprParser.FractFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FractFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitFractFunc(MathExprParser.FractFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ReluFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterReluFunc(MathExprParser.ReluFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ReluFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitReluFunc(MathExprParser.ReluFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SoftplusFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSoftplusFunc(MathExprParser.SoftplusFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SoftplusFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSoftplusFunc(MathExprParser.SoftplusFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GeluFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterGeluFunc(MathExprParser.GeluFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GeluFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitGeluFunc(MathExprParser.GeluFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SignFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSignFunc(MathExprParser.SignFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SignFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSignFunc(MathExprParser.SignFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PrintShapeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterPrintShapeFunc(MathExprParser.PrintShapeFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PrintShapeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitPrintShapeFunc(MathExprParser.PrintShapeFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PinvFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterPinvFunc(MathExprParser.PinvFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PinvFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitPinvFunc(MathExprParser.PinvFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SumFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSumFunc(MathExprParser.SumFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SumFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSumFunc(MathExprParser.SumFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MeanFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterMeanFunc(MathExprParser.MeanFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MeanFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitMeanFunc(MathExprParser.MeanFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StdFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterStdFunc(MathExprParser.StdFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StdFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitStdFunc(MathExprParser.StdFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code VarFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterVarFunc(MathExprParser.VarFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code VarFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitVarFunc(MathExprParser.VarFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SortFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSortFunc(MathExprParser.SortFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SortFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSortFunc(MathExprParser.SortFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AnyFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterAnyFunc(MathExprParser.AnyFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AnyFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitAnyFunc(MathExprParser.AnyFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AllFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterAllFunc(MathExprParser.AllFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AllFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitAllFunc(MathExprParser.AllFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EdgeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterEdgeFunc(MathExprParser.EdgeFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EdgeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitEdgeFunc(MathExprParser.EdgeFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MedianFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterMedianFunc(MathExprParser.MedianFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MedianFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitMedianFunc(MathExprParser.MedianFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ModeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterModeFunc(MathExprParser.ModeFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ModeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitModeFunc(MathExprParser.ModeFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CumsumFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterCumsumFunc(MathExprParser.CumsumFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CumsumFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitCumsumFunc(MathExprParser.CumsumFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CountFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterCountFunc(MathExprParser.CountFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CountFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitCountFunc(MathExprParser.CountFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CumprodFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterCumprodFunc(MathExprParser.CumprodFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CumprodFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitCumprodFunc(MathExprParser.CumprodFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PopFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterPopFunc(MathExprParser.PopFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PopFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitPopFunc(MathExprParser.PopFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ClearFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterClearFunc(MathExprParser.ClearFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ClearFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitClearFunc(MathExprParser.ClearFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code HasFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterHasFunc(MathExprParser.HasFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code HasFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitHasFunc(MathExprParser.HasFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GetFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterGetFunc(MathExprParser.GetFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GetFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitGetFunc(MathExprParser.GetFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArgsortFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterArgsortFunc(MathExprParser.ArgsortFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArgsortFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitArgsortFunc(MathExprParser.ArgsortFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArgminFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterArgminFunc(MathExprParser.ArgminFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArgminFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitArgminFunc(MathExprParser.ArgminFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArgmaxFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterArgmaxFunc(MathExprParser.ArgmaxFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArgmaxFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitArgmaxFunc(MathExprParser.ArgmaxFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SoftmaxFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSoftmaxFunc(MathExprParser.SoftmaxFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SoftmaxFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSoftmaxFunc(MathExprParser.SoftmaxFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SoftminFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSoftminFunc(MathExprParser.SoftminFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SoftminFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSoftminFunc(MathExprParser.SoftminFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ErfFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterErfFunc(MathExprParser.ErfFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ErfFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitErfFunc(MathExprParser.ErfFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ErfinvFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterErfinvFunc(MathExprParser.ErfinvFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ErfinvFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitErfinvFunc(MathExprParser.ErfinvFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UniqueFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterUniqueFunc(MathExprParser.UniqueFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UniqueFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitUniqueFunc(MathExprParser.UniqueFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FlattenFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterFlattenFunc(MathExprParser.FlattenFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FlattenFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitFlattenFunc(MathExprParser.FlattenFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MotionMaskFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterMotionMaskFunc(MathExprParser.MotionMaskFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MotionMaskFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitMotionMaskFunc(MathExprParser.MotionMaskFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FlowToImageFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterFlowToImageFunc(MathExprParser.FlowToImageFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FlowToImageFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitFlowToImageFunc(MathExprParser.FlowToImageFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitNotFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterBitNotFunc(MathExprParser.BitNotFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitNotFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitBitNotFunc(MathExprParser.BitNotFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitCountFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterBitCountFunc(MathExprParser.BitCountFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitCountFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitBitCountFunc(MathExprParser.BitCountFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ShapeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterShapeFunc(MathExprParser.ShapeFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ShapeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitShapeFunc(MathExprParser.ShapeFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UpperFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterUpperFunc(MathExprParser.UpperFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UpperFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitUpperFunc(MathExprParser.UpperFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LowerFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterLowerFunc(MathExprParser.LowerFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LowerFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitLowerFunc(MathExprParser.LowerFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TrimFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterTrimFunc(MathExprParser.TrimFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TrimFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitTrimFunc(MathExprParser.TrimFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EntropyFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterEntropyFunc(MathExprParser.EntropyFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EntropyFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitEntropyFunc(MathExprParser.EntropyFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SfftFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSfftFunc(MathExprParser.SfftFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SfftFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSfftFunc(MathExprParser.SfftFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DilateFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterDilateFunc(MathExprParser.DilateFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DilateFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitDilateFunc(MathExprParser.DilateFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ErodeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterErodeFunc(MathExprParser.ErodeFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ErodeFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitErodeFunc(MathExprParser.ErodeFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MorphOpenFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterMorphOpenFunc(MathExprParser.MorphOpenFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MorphOpenFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitMorphOpenFunc(MathExprParser.MorphOpenFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MorphCloseFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterMorphCloseFunc(MathExprParser.MorphCloseFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MorphCloseFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitMorphCloseFunc(MathExprParser.MorphCloseFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IntFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterIntFunc(MathExprParser.IntFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IntFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitIntFunc(MathExprParser.IntFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FloatFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterFloatFunc(MathExprParser.FloatFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FloatFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitFloatFunc(MathExprParser.FloatFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FlowMagFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterFlowMagFunc(MathExprParser.FlowMagFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FlowMagFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitFlowMagFunc(MathExprParser.FlowMagFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FlowAngFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterFlowAngFunc(MathExprParser.FlowAngFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FlowAngFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitFlowAngFunc(MathExprParser.FlowAngFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PowFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterPowFunc(MathExprParser.PowFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PowFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitPowFunc(MathExprParser.PowFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Atan2Func}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterAtan2Func(MathExprParser.Atan2FuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Atan2Func}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitAtan2Func(MathExprParser.Atan2FuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TMinFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterTMinFunc(MathExprParser.TMinFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TMinFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitTMinFunc(MathExprParser.TMinFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TMaxFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterTMaxFunc(MathExprParser.TMaxFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TMaxFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitTMaxFunc(MathExprParser.TMaxFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StepFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterStepFunc(MathExprParser.StepFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StepFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitStepFunc(MathExprParser.StepFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TopkFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterTopkFunc(MathExprParser.TopkFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TopkFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitTopkFunc(MathExprParser.TopkFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BotkFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterBotkFunc(MathExprParser.BotkFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BotkFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitBotkFunc(MathExprParser.BotkFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code QuartileFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterQuartileFunc(MathExprParser.QuartileFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code QuartileFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitQuartileFunc(MathExprParser.QuartileFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PercentileFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterPercentileFunc(MathExprParser.PercentileFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PercentileFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitPercentileFunc(MathExprParser.PercentileFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code QuantileFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterQuantileFunc(MathExprParser.QuantileFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code QuantileFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitQuantileFunc(MathExprParser.QuantileFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DotFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterDotFunc(MathExprParser.DotFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DotFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitDotFunc(MathExprParser.DotFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CossimFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterCossimFunc(MathExprParser.CossimFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CossimFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitCossimFunc(MathExprParser.CossimFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FlipFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterFlipFunc(MathExprParser.FlipFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FlipFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitFlipFunc(MathExprParser.FlipFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CovFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterCovFunc(MathExprParser.CovFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CovFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitCovFunc(MathExprParser.CovFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CorrFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterCorrFunc(MathExprParser.CorrFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CorrFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitCorrFunc(MathExprParser.CorrFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AppendFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterAppendFunc(MathExprParser.AppendFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AppendFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitAppendFunc(MathExprParser.AppendFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PermuteFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterPermuteFunc(MathExprParser.PermuteFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PermuteFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitPermuteFunc(MathExprParser.PermuteFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GaussianFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterGaussianFunc(MathExprParser.GaussianFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GaussianFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitGaussianFunc(MathExprParser.GaussianFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TopkIndFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterTopkIndFunc(MathExprParser.TopkIndFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TopkIndFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitTopkIndFunc(MathExprParser.TopkIndFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BotkIndFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterBotkIndFunc(MathExprParser.BotkIndFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BotkIndFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitBotkIndFunc(MathExprParser.BotkIndFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BatchShuffleFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterBatchShuffleFunc(MathExprParser.BatchShuffleFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BatchShuffleFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitBatchShuffleFunc(MathExprParser.BatchShuffleFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PushFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterPushFunc(MathExprParser.PushFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PushFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitPushFunc(MathExprParser.PushFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GetValueFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterGetValueFunc(MathExprParser.GetValueFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GetValueFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitGetValueFunc(MathExprParser.GetValueFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EmptyTensorFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterEmptyTensorFunc(MathExprParser.EmptyTensorFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EmptyTensorFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitEmptyTensorFunc(MathExprParser.EmptyTensorFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PadFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterPadFunc(MathExprParser.PadFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PadFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitPadFunc(MathExprParser.PadFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CrossFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterCrossFunc(MathExprParser.CrossFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CrossFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitCrossFunc(MathExprParser.CrossFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MatmulFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterMatmulFunc(MathExprParser.MatmulFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MatmulFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitMatmulFunc(MathExprParser.MatmulFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FlowApplyFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterFlowApplyFunc(MathExprParser.FlowApplyFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FlowApplyFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitFlowApplyFunc(MathExprParser.FlowApplyFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RifeFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterRifeFunc(MathExprParser.RifeFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RifeFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitRifeFunc(MathExprParser.RifeFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitAndFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterBitAndFunc(MathExprParser.BitAndFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitAndFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitBitAndFunc(MathExprParser.BitAndFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitXorFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterBitXorFunc(MathExprParser.BitXorFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitXorFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitBitXorFunc(MathExprParser.BitXorFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitOrFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterBitOrFunc(MathExprParser.BitOrFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitOrFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitBitOrFunc(MathExprParser.BitOrFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SplitFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterSplitFunc(MathExprParser.SplitFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SplitFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitSplitFunc(MathExprParser.SplitFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code JoinFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterJoinFunc(MathExprParser.JoinFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code JoinFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitJoinFunc(MathExprParser.JoinFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SubstringFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterSubstringFunc(MathExprParser.SubstringFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SubstringFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitSubstringFunc(MathExprParser.SubstringFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FindFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterFindFunc(MathExprParser.FindFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FindFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitFindFunc(MathExprParser.FindFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ReplaceFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterReplaceFunc(MathExprParser.ReplaceFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ReplaceFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitReplaceFunc(MathExprParser.ReplaceFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Int_to_rgbFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterInt_to_rgbFunc(MathExprParser.Int_to_rgbFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Int_to_rgbFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitInt_to_rgbFunc(MathExprParser.Int_to_rgbFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Rgb_to_intFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterRgb_to_intFunc(MathExprParser.Rgb_to_intFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Rgb_to_intFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitRgb_to_intFunc(MathExprParser.Rgb_to_intFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InterpolateLinearFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterInterpolateLinearFunc(MathExprParser.InterpolateLinearFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InterpolateLinearFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitInterpolateLinearFunc(MathExprParser.InterpolateLinearFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InterpolateAreaFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterInterpolateAreaFunc(MathExprParser.InterpolateAreaFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InterpolateAreaFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitInterpolateAreaFunc(MathExprParser.InterpolateAreaFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InterpolateNearestExactFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterInterpolateNearestExactFunc(MathExprParser.InterpolateNearestExactFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InterpolateNearestExactFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitInterpolateNearestExactFunc(MathExprParser.InterpolateNearestExactFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ClampFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterClampFunc(MathExprParser.ClampFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ClampFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitClampFunc(MathExprParser.ClampFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LerpFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterLerpFunc(MathExprParser.LerpFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LerpFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitLerpFunc(MathExprParser.LerpFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SmoothstepFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterSmoothstepFunc(MathExprParser.SmoothstepFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SmoothstepFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitSmoothstepFunc(MathExprParser.SmoothstepFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RangeFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterRangeFunc(MathExprParser.RangeFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RangeFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitRangeFunc(MathExprParser.RangeFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MomentFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterMomentFunc(MathExprParser.MomentFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MomentFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitMomentFunc(MathExprParser.MomentFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CubicEaseFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterCubicEaseFunc(MathExprParser.CubicEaseFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CubicEaseFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitCubicEaseFunc(MathExprParser.CubicEaseFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ElasticEaseFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterElasticEaseFunc(MathExprParser.ElasticEaseFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ElasticEaseFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitElasticEaseFunc(MathExprParser.ElasticEaseFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SineEaseFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterSineEaseFunc(MathExprParser.SineEaseFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SineEaseFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitSineEaseFunc(MathExprParser.SineEaseFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SmootherstepFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterSmootherstepFunc(MathExprParser.SmootherstepFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SmootherstepFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitSmootherstepFunc(MathExprParser.SmootherstepFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CropFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterCropFunc(MathExprParser.CropFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CropFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitCropFunc(MathExprParser.CropFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SifftFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterSifftFunc(MathExprParser.SifftFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SifftFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitSifftFunc(MathExprParser.SifftFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code OverlayFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterOverlayFunc(MathExprParser.OverlayFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code OverlayFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitOverlayFunc(MathExprParser.OverlayFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LinspaceFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterLinspaceFunc(MathExprParser.LinspaceFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LinspaceFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitLinspaceFunc(MathExprParser.LinspaceFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RollFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterRollFunc(MathExprParser.RollFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RollFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitRollFunc(MathExprParser.RollFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RgbToOklabFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterRgbToOklabFunc(MathExprParser.RgbToOklabFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RgbToOklabFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitRgbToOklabFunc(MathExprParser.RgbToOklabFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RgbToCilabFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterRgbToCilabFunc(MathExprParser.RgbToCilabFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RgbToCilabFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitRgbToCilabFunc(MathExprParser.RgbToCilabFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RgbToHsvFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterRgbToHsvFunc(MathExprParser.RgbToHsvFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RgbToHsvFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitRgbToHsvFunc(MathExprParser.RgbToHsvFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code HsvToRgbFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterHsvToRgbFunc(MathExprParser.HsvToRgbFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code HsvToRgbFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitHsvToRgbFunc(MathExprParser.HsvToRgbFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code WhereFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterWhereFunc(MathExprParser.WhereFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code WhereFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitWhereFunc(MathExprParser.WhereFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code OklabToRgbFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterOklabToRgbFunc(MathExprParser.OklabToRgbFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code OklabToRgbFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitOklabToRgbFunc(MathExprParser.OklabToRgbFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CilabToRgbFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterCilabToRgbFunc(MathExprParser.CilabToRgbFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CilabToRgbFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitCilabToRgbFunc(MathExprParser.CilabToRgbFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SwapFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 */
	void enterSwapFunc(MathExprParser.SwapFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SwapFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 */
	void exitSwapFunc(MathExprParser.SwapFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NvlFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 */
	void enterNvlFunc(MathExprParser.NvlFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NvlFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 */
	void exitNvlFunc(MathExprParser.NvlFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogspaceFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 */
	void enterLogspaceFunc(MathExprParser.LogspaceFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogspaceFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 */
	void exitLogspaceFunc(MathExprParser.LogspaceFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DistFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 */
	void enterDistFunc(MathExprParser.DistFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DistFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 */
	void exitDistFunc(MathExprParser.DistFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code HistogramFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 */
	void enterHistogramFunc(MathExprParser.HistogramFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code HistogramFunc}
	 * labeled alternative in {@link MathExprParser#func4}.
	 * @param ctx the parse tree
	 */
	void exitHistogramFunc(MathExprParser.HistogramFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RemapFunc}
	 * labeled alternative in {@link MathExprParser#func5}.
	 * @param ctx the parse tree
	 */
	void enterRemapFunc(MathExprParser.RemapFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RemapFunc}
	 * labeled alternative in {@link MathExprParser#func5}.
	 * @param ctx the parse tree
	 */
	void exitRemapFunc(MathExprParser.RemapFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SMinFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void enterSMinFunc(MathExprParser.SMinFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SMinFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void exitSMinFunc(MathExprParser.SMinFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SMaxFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void enterSMaxFunc(MathExprParser.SMaxFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SMaxFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void exitSMaxFunc(MathExprParser.SMaxFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MapFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void enterMapFunc(MathExprParser.MapFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MapFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void exitMapFunc(MathExprParser.MapFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EzConvFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void enterEzConvFunc(MathExprParser.EzConvFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EzConvFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void exitEzConvFunc(MathExprParser.EzConvFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ConvFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void enterConvFunc(MathExprParser.ConvFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ConvFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void exitConvFunc(MathExprParser.ConvFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ReshapeFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void enterReshapeFunc(MathExprParser.ReshapeFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ReshapeFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void exitReshapeFunc(MathExprParser.ReshapeFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ConcatFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void enterConcatFunc(MathExprParser.ConcatFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ConcatFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void exitConcatFunc(MathExprParser.ConcatFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NoiseFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterNoiseFunc(MathExprParser.NoiseFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NoiseFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitNoiseFunc(MathExprParser.NoiseFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RandFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterRandFunc(MathExprParser.RandFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RandFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitRandFunc(MathExprParser.RandFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExponentialFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterExponentialFunc(MathExprParser.ExponentialFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExponentialFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitExponentialFunc(MathExprParser.ExponentialFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BernoulliFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterBernoulliFunc(MathExprParser.BernoulliFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BernoulliFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitBernoulliFunc(MathExprParser.BernoulliFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PoissonFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterPoissonFunc(MathExprParser.PoissonFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PoissonFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitPoissonFunc(MathExprParser.PoissonFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CauchyFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterCauchyFunc(MathExprParser.CauchyFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CauchyFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitCauchyFunc(MathExprParser.CauchyFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogNormalFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterLogNormalFunc(MathExprParser.LogNormalFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogNormalFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitLogNormalFunc(MathExprParser.LogNormalFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GammaDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterGammaDistFunc(MathExprParser.GammaDistFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GammaDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitGammaDistFunc(MathExprParser.GammaDistFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BetaDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterBetaDistFunc(MathExprParser.BetaDistFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BetaDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitBetaDistFunc(MathExprParser.BetaDistFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LaplaceDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterLaplaceDistFunc(MathExprParser.LaplaceDistFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LaplaceDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitLaplaceDistFunc(MathExprParser.LaplaceDistFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GumbelDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterGumbelDistFunc(MathExprParser.GumbelDistFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GumbelDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitGumbelDistFunc(MathExprParser.GumbelDistFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code WeibullDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterWeibullDistFunc(MathExprParser.WeibullDistFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code WeibullDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitWeibullDistFunc(MathExprParser.WeibullDistFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Chi2DistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterChi2DistFunc(MathExprParser.Chi2DistFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Chi2DistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitChi2DistFunc(MathExprParser.Chi2DistFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StudentTDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterStudentTDistFunc(MathExprParser.StudentTDistFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StudentTDistFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitStudentTDistFunc(MathExprParser.StudentTDistFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PerlinFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterPerlinFunc(MathExprParser.PerlinFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PerlinFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitPerlinFunc(MathExprParser.PerlinFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CellularFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterCellularFunc(MathExprParser.CellularFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CellularFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitCellularFunc(MathExprParser.CellularFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PlasmaFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void enterPlasmaFunc(MathExprParser.PlasmaFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PlasmaFunc}
	 * labeled alternative in {@link MathExprParser#funcNoise}.
	 * @param ctx the parse tree
	 */
	void exitPlasmaFunc(MathExprParser.PlasmaFuncContext ctx);
}