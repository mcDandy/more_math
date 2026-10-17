import importlib.metadata


def get_antlr_modules():
    if importlib.metadata.version("antlr4-python3-runtime").startswith("4.9"):
        from .legacy.MathExprLexer import MathExprLexer
        from .legacy.MathExprParser import MathExprParser
        from .legacy.MathExprVisitor import MathExprVisitor
    else:
        from .grammer.MathExprLexer import MathExprLexer
        from .grammer.MathExprParser import MathExprParser
        from .grammer.MathExprVisitor import MathExprVisitor

    return MathExprLexer, MathExprParser, MathExprVisitor
