import importlib.metadata


def get_antlr_modules():
    if importlib.metadata.version("antlr4-python3-runtime").startswith("4.9"):
        from .grammer.legacy.MathExprLexer import MathExprLexer
        from .grammer.legacy.MathExprParser import MathExprParser
        from .grammer.legacy.MathExprVisitor import MathExprVisitor
    else:
        from .grammer.modern.MathExprLexer import MathExprLexer
        from .grammer.modern.MathExprParser import MathExprParser
        from .grammer.modern.MathExprVisitor import MathExprVisitor

    return MathExprLexer, MathExprParser, MathExprVisitor
