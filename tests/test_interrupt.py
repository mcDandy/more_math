import threading

import pytest
import comfy.model_management as mm

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.helper_functions import parse_expr


@pytest.mark.parametrize("expr", [
    "i = 0; while (1) { i += 1; } i",
    "f(x) -> f(x); f(1)",
    "g(x) -> { for (k in [1, 2]) { g(x); } return x; }; g(1)",
])
def test_interrupt_stops_endless_script(expr):
    tree = parse_expr(expr)
    timer = threading.Timer(0.2, mm.interrupt_current_processing)
    timer.start()
    try:
        with pytest.raises(mm.InterruptProcessingException):
            UnifiedMathVisitor({}, (1,)).visit(tree)
    finally:
        timer.cancel()
        mm.interrupt_current_processing(False)
