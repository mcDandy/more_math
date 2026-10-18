from antlr4.tree.Tree import TerminalNode

from .antlr_router import get_antlr_modules

_, P, _ = get_antlr_modules()

# builtins that print, touch the stack or change their argument in place; calls to them are never removed
_EFFECT_TOKENS = {
    P.PRNT, P.PRINT_SHAPE, P.PUSH, P.POP, P.CLEAR, P.HAS, P.GET,
    P.ADD_KEY, P.REMOVE_KEY, P.ENABLE_TRACKING, P.DISABLE_TRACKING, P.RESET_TRACKING,
}


def remove_dead_code(tree):
    """Removes statements whose result is never read and that have no side effects. Changes and returns tree."""
    _DeadCode(tree).run()
    return tree


class _DeadCode:
    def __init__(self, tree):
        self.tree = tree
        self.defs = {}
        self.lambdas = []
        self.calls = []
        assignments = []
        # which lambdas a variable can hold, and variables that may hold one we cannot follow
        self.lam = {}
        self.unknown = set()
        todo = [tree]
        while todo:
            n = todo.pop()
            if isinstance(n, TerminalNode):
                continue
            if isinstance(n, P.VarDefContext):
                if n.EQUEALS() and not n.LBRACKET():
                    assignments.append((n.VARIABLE().getText(), n.expr(0)))
            elif isinstance(n, P.ForStmtContext):
                self.unknown.add(n.VARIABLE().getText())
            elif isinstance(n, P.FunctionDefContext):
                self.defs.setdefault(n.VARIABLE().getText(), []).append((_params(n), n.block() or n.expr()))
            elif isinstance(n, P.LambdaExpContext):
                self.lambdas.append(n)
            elif isinstance(n, P.CallExpContext):
                self.calls.append(n)
            todo.extend(n.getChildren())

        # User functions see the caller's variables, so a call reads everything its body reads.
        # Lambdas only see the variables captured when they were created, so calling one reads nothing extra.
        self.fn_reads = {name: set() for name in self.defs}
        self.fn_effect = {name: False for name in self.defs}
        self.lambda_effect = {lam: False for lam in self.lambdas}
        changed = True
        while changed:
            changed = False
            for name, expr in assignments:
                changed |= self.flow(name, self.value(expr))
            for call in self.calls:
                lams, fns, _ = self.resolve(call.VARIABLE().getText())
                args = call.exprList().expr() if call.exprList() else []
                targets = [_params(lam) for lam in lams] + [params for fn in fns for params, _ in self.defs[fn]]
                for params in targets:
                    for param, arg in zip(params, args):
                        changed |= self.flow(param, self.value(arg))
            for lam in self.lambdas:
                if not self.lambda_effect[lam] and self.scan(lam.block() or lam.expr())[1]:
                    self.lambda_effect[lam] = changed = True
            for name, defs in self.defs.items():
                reads, effect = set(), False
                for params, body in defs:
                    r, e = self.scan(body)
                    reads |= r - set(params)
                    effect |= e
                if reads != self.fn_reads[name] or effect != self.fn_effect[name]:
                    self.fn_reads[name], self.fn_effect[name] = reads, effect
                    changed = True

    def flow(self, name, value):
        lams, unknown = value
        changed = not lams <= self.lam.get(name, set()) or (unknown and name not in self.unknown)
        self.lam.setdefault(name, set()).update(lams)
        if unknown:
            self.unknown.add(name)
        return changed

    def value(self, node):
        """Lambdas an expression can evaluate to, and whether it may be one we cannot follow."""
        while True:
            if isinstance(node, P.ParenExpContext):
                node = node.expr()
            elif node.getChildCount() == 1 and not isinstance(node.getChild(0), TerminalNode):
                node = node.getChild(0)
            else:
                break
        if isinstance(node, P.LambdaExpContext):
            return {node}, False
        if isinstance(node, P.VariableExpContext):
            name = node.getText()
            return set(self.lam.get(name, ())), name in self.unknown
        if isinstance(node, P.TernaryExpContext):
            (a, ua), (b, ub) = self.value(node.expr(0)), self.value(node.expr(1))
            return a | b, ua or ub
        todo = [node]
        while todo:
            n = todo.pop()
            if isinstance(n, TerminalNode):
                continue
            if isinstance(n, (P.LambdaExpContext, P.CallExpContext)):
                return set(), True
            if isinstance(n, P.VariableExpContext) and (self.lam.get(n.getText()) or n.getText() in self.unknown):
                return set(), True
            todo.extend(n.getChildren())
        return set(), False

    def resolve(self, name):
        """Lambdas and user functions a call by this name can reach, and whether it may reach something else."""
        lams = self.lam.get(name, set())
        unknown = name in self.unknown
        fns = [name] if name in self.defs else []
        return lams, fns, unknown or not (lams or fns)

    def run(self):
        live, _ = self.scan(self.tree.expr())
        self.sweep(self.tree, live, None, apply=True, keep_last=False, skip=self.tree.expr())

    def scan(self, node):
        """Variables an expression reads, and whether evaluating it has side effects."""
        reads, effect = set(), False
        todo = [node]
        while todo:
            n = todo.pop()
            if isinstance(n, TerminalNode):
                t = n.getSymbol().type
                if t == P.VARIABLE:
                    reads.add(n.getText())
                elif t in _EFFECT_TOKENS:
                    effect = True
                continue
            if isinstance(n, P.LambdaExpContext):
                # creating a lambda only captures variables; its body runs when it is called
                reads |= self.scan(n.block() or n.expr())[0] - set(_params(n))
                continue
            if isinstance(n, P.CallExpContext):
                lams, fns, unknown = self.resolve(n.VARIABLE().getText())
                effect |= unknown or any(self.lambda_effect[lam] for lam in lams) or any(self.fn_effect[fn] for fn in fns)
                for fn in fns:
                    reads |= self.fn_reads[fn]
            todo.extend(n.getChildren())
        return reads, effect

    def sweep(self, parent, live, loop_live, apply, keep_last, skip=None):
        """Walks a statement list backwards, removing dead statements when apply is set; returns live-before."""
        stmts = [c for c in parent.children if not isinstance(c, TerminalNode) and c is not skip]
        for i in range(len(stmts) - 1, -1, -1):
            before, removable = self.stmt(stmts[i], live, loop_live, apply)
            if removable and not (keep_last and i == len(stmts) - 1):
                if apply:
                    parent.children.remove(stmts[i])
            else:
                live = before
        return live

    def stmt(self, node, live, loop_live, apply):
        """Returns (live-before if kept, whether the statement can be removed)."""
        if isinstance(node, P.VarDefStmtContext):
            node = node.varDef()
        if isinstance(node, P.VarDefContext):
            name = node.VARIABLE().getText()
            reads, effect = set(), False
            for e in node.expr():
                r, eff = self.scan(e)
                reads |= r
                effect |= eff
            if node.EQUEALS() and not node.LBRACKET():
                before = (live - {name}) | reads
            else:
                before = live | {name} | reads
            return before, name not in live and not effect
        if isinstance(node, P.ExprStatementContext):
            reads, effect = self.scan(node.expr())
            return live | reads, not effect
        if isinstance(node, P.IfStatementContext):
            node = node.ifStmt()
            reads, _ = self.scan(node.expr())
            before = reads | self.stmt_kept(node.stmt(0), live, loop_live, apply)
            if node.stmt(1):
                return before | self.stmt_kept(node.stmt(1), live, loop_live, apply), False
            return before | live, False
        if isinstance(node, P.WhileStatementContext):
            node = node.whileStmt()
            reads, _ = self.scan(node.expr())
            head = self.loop_head(node.stmt(), live | reads, None, apply)
            return head, False
        if isinstance(node, P.ForStatementContext):
            node = node.forStmt()
            reads, _ = self.scan(node.expr())
            head = self.loop_head(node.stmt(), live, node.VARIABLE().getText(), apply)
            return head | reads, False
        if isinstance(node, P.BlockStatementContext):
            return self.sweep(node.block(), live, loop_live, apply, keep_last=True), False
        if isinstance(node, (P.BreakStatementContext, P.ContinueStatementContext)):
            return set(loop_live), False
        if isinstance(node, P.ReturnStatementContext):
            expr = node.returnStmt().expr()
            return (self.scan(expr)[0] if expr else set()), False
        # function definitions and anything unexpected stay, and are assumed to read everything still live
        return live, False

    def stmt_kept(self, node, live, loop_live, apply):
        return self.stmt(node, live, loop_live, apply)[0]

    def loop_head(self, body, exit_live, loop_var, apply):
        """Fixed point of the variables live at the top of a loop; only removes once it is stable."""
        head = set(exit_live)
        while True:
            body_live = self.stmt_kept(body, head, head, apply=False)
            if loop_var is not None:
                body_live = body_live - {loop_var}
            new_head = exit_live | body_live
            if new_head == head:
                break
            head = new_head
        self.stmt_kept(body, head, head, apply)
        return head


def _params(node):
    return [v.getText() for v in node.paramList().VARIABLE()] if node.paramList() else []
