import sys
import antlr4

def get_antlr_modules():
    runtime_version = "0.0.0"

    try:
        if sys.version_info >= (3, 8):
            import importlib.metadata
            runtime_version = importlib.metadata.version("antlr4-python3-runtime")
        else:
            import pkg_resources
            runtime_version = pkg_resources.get_distribution("antlr4-python3-runtime").version
    except Exception:
        runtime_version = getattr(antlr4, "__version__", "4.13.2")

    if runtime_version.startswith("4.9"):
        from .legacy.MathExprLexer import MathExprLexer
        from .legacy.MathExprParser import MathExprParser
        from .legacy.MathExprVisitor import MathExprVisitor
    else:
        from .grammer.MathExprLexer import MathExprLexer
        from .grammer.MathExprParser import MathExprParser
        from .grammer.MathExprVisitor import MathExprVisitor

    return MathExprLexer, MathExprParser, MathExprVisitor
