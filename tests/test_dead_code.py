import io
import contextlib

import torch

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.Parser.dead_code import remove_dead_code
from more_math.helper_functions import parse_expr, checkLazyNew


def run(script, variables=None, optimize=True, stack=None):
    tree = parse_expr(script)
    if optimize:
        remove_dead_code(tree)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        result = UnifiedMathVisitor(dict(variables or {}), (1,), state_storage=stack if stack is not None else {}).visit(tree)
    return result, out.getvalue(), tree.getText()


def same_as_unoptimized(script, variables=None):
    plain, plain_out, _ = run(script, variables, optimize=False, stack={})
    result, out, text = run(script, variables, stack={})
    assert out == plain_out
    if torch.is_tensor(plain):
        torch.testing.assert_close(result, plain)
    else:
        assert result == plain
    return text


def test_removes_unused_assignments_and_expression_statements():
    text = same_as_unoptimized("a = V0 * 2; b = V0 + 1; V0 * 3; b", {"V0": torch.ones(4)})
    assert "a=" not in text and "V0*3;" not in text and "b=V0+1" in text


def test_keeps_side_effects():
    stack = {1: [7]}
    result, out, text = run("x = print(1); stack_push(1, 2); y = stack_pop(1) + stack_get(1); pshp(3); 5", stack=stack)
    assert "x=print(1)" in text and "stack_push(1,2)" in text and "y=" in text and "pshp(3)" in text
    assert result == 5 and stack[1] == [7] and "1" in out


def test_keeps_variables_read_by_called_functions():
    text = same_as_unoptimized("p = V0 * 2; q = V0 * 9; f() -> p + 1; f()", {"V0": torch.ones(2)})
    assert "p=V0*2" in text and "q=" not in text


def test_function_with_side_effects_is_kept():
    text = same_as_unoptimized("f(x) -> print(x); unused = f(3); 1")
    assert "unused=f(3)" in text


def test_lambdas_are_pure_or_impure_by_their_body():
    text = same_as_unoptimized("g = (x) -> x * 2; y = g(3); 1")
    assert "y=" not in text and "g=" not in text
    text = same_as_unoptimized("g = (x) -> print(x); y = g(3); 1")
    assert "y=g(3)" in text
    # a lambda reaching another one captured when it was created
    text = same_as_unoptimized("p = (x) -> print(x); g = (x) -> p(x) + 1; h = g; y = h(2); 1")
    assert "y=h(2)" in text


def test_recursive_lambdas_through_parameters():
    pure = "f = (g, n) -> (n <= 1 ? 1 : n * g(g, n - 1)); r = f(f, 4); 1"
    assert "r=" not in same_as_unoptimized(pure)
    impure = "f = (g, n) -> (n <= 1 ? print(1) : n * g(g, n - 1)); r = f(f, 4); 1"
    assert "r=f(f,4)" in same_as_unoptimized(impure)
    # a and b only reach each other through their parameters; the side effect is in b
    mutual = "a = (p, q, n) -> (n <= 0 ? 0 : q(q, p, n - 1)); b = (p, q, n) -> (n <= 0 ? print(n) : q(q, p, n - 1)); r = a(a, b, 3); 1"
    assert "r=a(a,b,3)" in same_as_unoptimized(mutual)
    assert "r=" not in same_as_unoptimized(mutual.replace("print(n)", "n"))


def test_lambdas_passed_to_functions_and_unknown_lambdas():
    assert "r=h(k)" in same_as_unoptimized("h(p) -> p(3); k = (x) -> print(x); r = h(k); 1")
    assert "r=" not in same_as_unoptimized("h(p) -> p(3); k = (x) -> x * 2; r = h(k); 1")
    # a lambda returned from a function is not followed, so calls through it stay
    assert "y=f(2)" in same_as_unoptimized("mk() -> (x) -> x * 2; f = mk(); y = f(2); 1")


def test_loops_keep_loop_carried_values_and_drop_dead_ones():
    text = same_as_unoptimized("s = 0; t = 0; for (i in [1, 2, 3]) { t = t + i; s = s + i; } s")
    assert "t=t+i" not in text and "t=0" not in text and "s=s+i" in text
    text = same_as_unoptimized("i = 0; j = 0; while (i < 3) { j = i * 2; i = i + 1; } i")
    assert "j=i*2" not in text and "i=i+1" in text
    text = same_as_unoptimized("acc = 0; for (v in [1, 2]) { tmp = v * 2; acc = acc + tmp; } acc")
    assert "tmp=v*2" in text


def test_break_and_conditional_assignments():
    script = "x = 1; for (i in [1, 2, 3]) { if (i == 2) { x = i; break; } } x"
    text = same_as_unoptimized(script)
    assert "x=i" in text and "x=1" in text
    text = same_as_unoptimized("x = 5; if (V0 > 0) x = 2; x", {"V0": 1.0})
    assert "x=5" in text


def test_compound_and_indexed_assignments_read_the_target():
    text = same_as_unoptimized("a = [1, 2, 3]; a[0] = 5; a += 1; a")
    assert "a[0]=5" in text and "a=[1,2,3]" in text
    text = same_as_unoptimized("a = [1, 2, 3]; a[0] = 5; 1")
    assert "a[0]=5" not in text and "a=[1,2,3]" not in text


def test_last_statement_of_a_block_stays():
    text = same_as_unoptimized("if (1) { a = 2; b = 3; } 7")
    assert "a=2" not in text and "b=3" in text


def test_unused_inputs_are_no_longer_requested():
    tree = remove_dead_code(parse_expr("u = V1 * 2; V0"))
    assert checkLazyNew(tree, {"V0": None, "V1": None}, {}) == {"V0"}
