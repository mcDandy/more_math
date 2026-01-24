// Generated from d:\stability\Data\Packages\ComfyUI\custom_nodes\more_math\more_math\Parser\MathExpr.g4 by ANTLR 4.9.2
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
	 * Enter a parse tree produced by the {@code ToPow}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
	 * @param ctx the parse tree
	 */
	void enterToPow(MathExprParser.ToPowContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ToPow}
	 * labeled alternative in {@link MathExprParser#mulExpr}.
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
	 * Enter a parse tree produced by the {@code sfftFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSfftFunc(MathExprParser.SfftFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sfftFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSfftFunc(MathExprParser.SfftFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code sifftFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterSifftFunc(MathExprParser.SifftFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sifftFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitSifftFunc(MathExprParser.SifftFuncContext ctx);
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
	 * Enter a parse tree produced by the {@code NoiseFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterNoiseFunc(MathExprParser.NoiseFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NoiseFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitNoiseFunc(MathExprParser.NoiseFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RandFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void enterRandFunc(MathExprParser.RandFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RandFunc}
	 * labeled alternative in {@link MathExprParser#func1}.
	 * @param ctx the parse tree
	 */
	void exitRandFunc(MathExprParser.RandFuncContext ctx);
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
	 * Enter a parse tree produced by the {@code ExponentialFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterExponentialFunc(MathExprParser.ExponentialFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExponentialFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitExponentialFunc(MathExprParser.ExponentialFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BernoulliFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterBernoulliFunc(MathExprParser.BernoulliFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BernoulliFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitBernoulliFunc(MathExprParser.BernoulliFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PoissonFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void enterPoissonFunc(MathExprParser.PoissonFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PoissonFunc}
	 * labeled alternative in {@link MathExprParser#func2}.
	 * @param ctx the parse tree
	 */
	void exitPoissonFunc(MathExprParser.PoissonFuncContext ctx);
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
	 * Enter a parse tree produced by the {@code CauchyFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterCauchyFunc(MathExprParser.CauchyFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CauchyFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitCauchyFunc(MathExprParser.CauchyFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogNormalFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void enterLogNormalFunc(MathExprParser.LogNormalFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogNormalFunc}
	 * labeled alternative in {@link MathExprParser#func3}.
	 * @param ctx the parse tree
	 */
	void exitLogNormalFunc(MathExprParser.LogNormalFuncContext ctx);
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
	 * Enter a parse tree produced by the {@code PermuteFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void enterPermuteFunc(MathExprParser.PermuteFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PermuteFunc}
	 * labeled alternative in {@link MathExprParser#funcN}.
	 * @param ctx the parse tree
	 */
	void exitPermuteFunc(MathExprParser.PermuteFuncContext ctx);
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
}