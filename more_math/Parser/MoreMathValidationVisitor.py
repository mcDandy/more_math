from .antlr_router import get_antlr_modules
_, _, MathExprVisitor = get_antlr_modules()

class MoreMathValidationVisitor(MathExprVisitor):
    def __init__(self, initial_variables, initial_functions):
        self.variables = set(initial_variables.keys())
        self.functions = set(initial_functions.keys())
        self._scope_stack = []

    def visitIfStmt(self, ctx):
        self.visit(ctx.condition())

        self.visit(ctx.thenBody())
        if ctx.elseBody():
            self.visit(ctx.elseBody())
        return None

    def visitWhileStmt(self, ctx):
        self.visit(ctx.condition())
        self.visit(ctx.body())
        return None

    def visitFunctionDef(self, ctx):
        func_name = ctx.VARIABLE().getText()
        self.functions.add(func_name)
        return None

    def visitCallExp(self, ctx):
        func_name = ctx.VARIABLE().getText()
        if func_name not in self.functions and func_name not in self.variables:
            raise ValueError(f"{ctx.start.line}:{ctx.start.column}: unknown function or variable: {func_name}")

        if ctx.exprList():
            for e in ctx.exprList().expr():
                self.visit(e)

        return "NOT_NULL"
    def visitForStmt(self, ctx):
        iterator_name = ctx.VARIABLE().getText()
        source_expr = ctx.expr()
        self.visit(source_expr)
        self._scope_stack.append(self.variables.copy())

        self.variables.add(iterator_name)

        try:
            if ctx.block():
                self.visit(ctx.block())
            elif ctx.expr():
                self.visit(ctx.expr())
        finally:
            self.variables = self._scope_stack.pop()

        return None