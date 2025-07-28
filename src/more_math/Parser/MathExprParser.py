# Generated from MathExpr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,42,273,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,3,0,27,8,0,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,9,1,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,3,1,3,1,3,1,3,1,3,1,3,
        5,3,57,8,3,10,3,12,3,60,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        5,4,71,8,4,10,4,12,4,74,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,5,5,88,8,5,10,5,12,5,91,9,5,1,6,1,6,1,6,1,6,1,6,3,6,
        98,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,107,8,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,3,8,119,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,231,8,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,247,8,10,1,11,1,
        11,1,11,1,11,1,11,4,11,254,8,11,11,11,12,11,255,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,4,11,265,8,11,11,11,12,11,266,1,11,1,11,3,11,271,
        8,11,1,11,0,5,2,4,6,8,10,12,0,2,4,6,8,10,12,14,16,18,20,22,0,0,304,
        0,26,1,0,0,0,2,28,1,0,0,0,4,39,1,0,0,0,6,50,1,0,0,0,8,61,1,0,0,0,
        10,75,1,0,0,0,12,97,1,0,0,0,14,106,1,0,0,0,16,118,1,0,0,0,18,230,
        1,0,0,0,20,246,1,0,0,0,22,270,1,0,0,0,24,27,3,16,8,0,25,27,3,2,1,
        0,26,24,1,0,0,0,26,25,1,0,0,0,27,1,1,0,0,0,28,29,6,1,-1,0,29,30,
        3,4,2,0,30,36,1,0,0,0,31,32,10,2,0,0,32,33,5,36,0,0,33,35,3,4,2,
        0,34,31,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,3,1,
        0,0,0,38,36,1,0,0,0,39,40,6,2,-1,0,40,41,3,6,3,0,41,47,1,0,0,0,42,
        43,10,2,0,0,43,44,5,37,0,0,44,46,3,6,3,0,45,42,1,0,0,0,46,49,1,0,
        0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,5,1,0,0,0,49,47,1,0,0,0,50,51,
        6,3,-1,0,51,52,3,8,4,0,52,58,1,0,0,0,53,54,10,2,0,0,54,55,5,35,0,
        0,55,57,3,8,4,0,56,53,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,
        1,0,0,0,59,7,1,0,0,0,60,58,1,0,0,0,61,62,6,4,-1,0,62,63,3,10,5,0,
        63,72,1,0,0,0,64,65,10,3,0,0,65,66,5,30,0,0,66,71,3,10,5,0,67,68,
        10,2,0,0,68,69,5,31,0,0,69,71,3,10,5,0,70,64,1,0,0,0,70,67,1,0,0,
        0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,9,1,0,0,0,74,72,1,
        0,0,0,75,76,6,5,-1,0,76,77,3,12,6,0,77,89,1,0,0,0,78,79,10,4,0,0,
        79,80,5,32,0,0,80,88,3,12,6,0,81,82,10,3,0,0,82,83,5,33,0,0,83,88,
        3,12,6,0,84,85,10,2,0,0,85,86,5,34,0,0,86,88,3,12,6,0,87,78,1,0,
        0,0,87,81,1,0,0,0,87,84,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,
        1,0,0,0,90,11,1,0,0,0,91,89,1,0,0,0,92,93,3,14,7,0,93,94,5,22,0,
        0,94,95,3,12,6,0,95,98,1,0,0,0,96,98,3,14,7,0,97,92,1,0,0,0,97,96,
        1,0,0,0,98,13,1,0,0,0,99,100,5,30,0,0,100,107,3,14,7,0,101,102,5,
        31,0,0,102,107,3,14,7,0,103,104,5,38,0,0,104,107,3,14,7,0,105,107,
        3,16,8,0,106,99,1,0,0,0,106,101,1,0,0,0,106,103,1,0,0,0,106,105,
        1,0,0,0,107,15,1,0,0,0,108,119,3,18,9,0,109,119,3,20,10,0,110,119,
        3,22,11,0,111,119,5,41,0,0,112,119,5,40,0,0,113,119,5,39,0,0,114,
        115,5,1,0,0,115,116,3,0,0,0,116,117,5,2,0,0,117,119,1,0,0,0,118,
        108,1,0,0,0,118,109,1,0,0,0,118,110,1,0,0,0,118,111,1,0,0,0,118,
        112,1,0,0,0,118,113,1,0,0,0,118,114,1,0,0,0,119,17,1,0,0,0,120,121,
        5,4,0,0,121,122,5,1,0,0,122,123,3,0,0,0,123,124,5,2,0,0,124,231,
        1,0,0,0,125,126,5,5,0,0,126,127,5,1,0,0,127,128,3,0,0,0,128,129,
        5,2,0,0,129,231,1,0,0,0,130,131,5,6,0,0,131,132,5,1,0,0,132,133,
        3,0,0,0,133,134,5,2,0,0,134,231,1,0,0,0,135,136,5,7,0,0,136,137,
        5,1,0,0,137,138,3,0,0,0,138,139,5,2,0,0,139,231,1,0,0,0,140,141,
        5,8,0,0,141,142,5,1,0,0,142,143,3,0,0,0,143,144,5,2,0,0,144,231,
        1,0,0,0,145,146,5,9,0,0,146,147,5,1,0,0,147,148,3,0,0,0,148,149,
        5,2,0,0,149,231,1,0,0,0,150,151,5,11,0,0,151,152,5,1,0,0,152,153,
        3,0,0,0,153,154,5,2,0,0,154,231,1,0,0,0,155,156,5,12,0,0,156,157,
        5,1,0,0,157,158,3,0,0,0,158,159,5,2,0,0,159,231,1,0,0,0,160,161,
        5,13,0,0,161,162,5,1,0,0,162,163,3,0,0,0,163,164,5,2,0,0,164,231,
        1,0,0,0,165,166,5,14,0,0,166,167,5,1,0,0,167,168,3,0,0,0,168,169,
        5,2,0,0,169,231,1,0,0,0,170,171,5,15,0,0,171,172,5,1,0,0,172,173,
        3,0,0,0,173,174,5,2,0,0,174,231,1,0,0,0,175,176,5,16,0,0,176,177,
        5,1,0,0,177,178,3,0,0,0,178,179,5,2,0,0,179,231,1,0,0,0,180,181,
        5,17,0,0,181,182,5,1,0,0,182,183,3,0,0,0,183,184,5,2,0,0,184,231,
        1,0,0,0,185,186,5,18,0,0,186,187,5,1,0,0,187,188,3,0,0,0,188,189,
        5,2,0,0,189,231,1,0,0,0,190,191,5,19,0,0,191,192,5,1,0,0,192,193,
        3,0,0,0,193,194,5,2,0,0,194,231,1,0,0,0,195,196,5,20,0,0,196,197,
        5,1,0,0,197,198,3,0,0,0,198,199,5,2,0,0,199,231,1,0,0,0,200,201,
        5,21,0,0,201,202,5,1,0,0,202,203,3,0,0,0,203,204,5,2,0,0,204,231,
        1,0,0,0,205,206,5,25,0,0,206,207,5,1,0,0,207,208,3,0,0,0,208,209,
        5,2,0,0,209,231,1,0,0,0,210,211,5,26,0,0,211,212,5,1,0,0,212,213,
        3,0,0,0,213,214,5,2,0,0,214,231,1,0,0,0,215,216,5,27,0,0,216,217,
        5,1,0,0,217,218,3,0,0,0,218,219,5,2,0,0,219,231,1,0,0,0,220,221,
        5,28,0,0,221,222,5,1,0,0,222,223,3,0,0,0,223,224,5,2,0,0,224,231,
        1,0,0,0,225,226,5,29,0,0,226,227,5,1,0,0,227,228,3,0,0,0,228,229,
        5,2,0,0,229,231,1,0,0,0,230,120,1,0,0,0,230,125,1,0,0,0,230,130,
        1,0,0,0,230,135,1,0,0,0,230,140,1,0,0,0,230,145,1,0,0,0,230,150,
        1,0,0,0,230,155,1,0,0,0,230,160,1,0,0,0,230,165,1,0,0,0,230,170,
        1,0,0,0,230,175,1,0,0,0,230,180,1,0,0,0,230,185,1,0,0,0,230,190,
        1,0,0,0,230,195,1,0,0,0,230,200,1,0,0,0,230,205,1,0,0,0,230,210,
        1,0,0,0,230,215,1,0,0,0,230,220,1,0,0,0,230,225,1,0,0,0,231,19,1,
        0,0,0,232,233,5,22,0,0,233,234,5,1,0,0,234,235,3,0,0,0,235,236,5,
        3,0,0,236,237,3,0,0,0,237,238,5,2,0,0,238,247,1,0,0,0,239,240,5,
        10,0,0,240,241,5,1,0,0,241,242,3,0,0,0,242,243,5,3,0,0,243,244,3,
        0,0,0,244,245,5,2,0,0,245,247,1,0,0,0,246,232,1,0,0,0,246,239,1,
        0,0,0,247,21,1,0,0,0,248,249,5,23,0,0,249,250,5,1,0,0,250,253,3,
        0,0,0,251,252,5,3,0,0,252,254,3,0,0,0,253,251,1,0,0,0,254,255,1,
        0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,257,1,0,0,0,257,258,5,
        2,0,0,258,271,1,0,0,0,259,260,5,24,0,0,260,261,5,1,0,0,261,264,3,
        0,0,0,262,263,5,3,0,0,263,265,3,0,0,0,264,262,1,0,0,0,265,266,1,
        0,0,0,266,264,1,0,0,0,266,267,1,0,0,0,267,268,1,0,0,0,268,269,5,
        2,0,0,269,271,1,0,0,0,270,248,1,0,0,0,270,259,1,0,0,0,271,23,1,0,
        0,0,16,26,36,47,58,70,72,87,89,97,106,118,230,246,255,266,270
    ]

class MathExprParser ( Parser ):

    grammarFileName = "MathExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'sin'", "'cos'", 
                     "'tan'", "'asin'", "'acos'", "'atan'", "'atan2'", "'sinh'", 
                     "'cosh'", "'tanh'", "'asinh'", "'acosh'", "'atanh'", 
                     "'abs'", "'sqrt'", "'ln'", "'log'", "'exp'", "'pow'", 
                     "'min'", "'max'", "'norm'", "'floor'", "'ceil'", "'round'", 
                     "'gamma'", "'+'", "'-'", "'*'", "'/'", "'%'", "'&'", 
                     "'|'", "'^'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN", "ATAN2", 
                      "SINH", "COSH", "TANH", "ASINH", "ACOSH", "ATANH", 
                      "ABS", "SQRT", "LN", "LOG", "EXP", "POW", "MIN", "MAX", 
                      "NORM", "FLOOR", "CEIL", "ROUND", "GAMMA", "PLUS", 
                      "MINUS", "MULT", "DIV", "MOD", "AND", "OR", "XOR", 
                      "NOT", "CONSTANT", "NUMBER", "VARIABLE", "WS" ]

    RULE_expr = 0
    RULE_orExpr = 1
    RULE_xorExpr = 2
    RULE_andExpr = 3
    RULE_addExpr = 4
    RULE_mulExpr = 5
    RULE_powExpr = 6
    RULE_unaryExpr = 7
    RULE_atom = 8
    RULE_func1 = 9
    RULE_func2 = 10
    RULE_funcN = 11

    ruleNames =  [ "expr", "orExpr", "xorExpr", "andExpr", "addExpr", "mulExpr", 
                   "powExpr", "unaryExpr", "atom", "func1", "func2", "funcN" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    SIN=4
    COS=5
    TAN=6
    ASIN=7
    ACOS=8
    ATAN=9
    ATAN2=10
    SINH=11
    COSH=12
    TANH=13
    ASINH=14
    ACOSH=15
    ATANH=16
    ABS=17
    SQRT=18
    LN=19
    LOG=20
    EXP=21
    POW=22
    MIN=23
    MAX=24
    NORM=25
    FLOOR=26
    CEIL=27
    ROUND=28
    GAMMA=29
    PLUS=30
    MINUS=31
    MULT=32
    DIV=33
    MOD=34
    AND=35
    OR=36
    XOR=37
    NOT=38
    CONSTANT=39
    NUMBER=40
    VARIABLE=41
    WS=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(MathExprParser.AtomContext,0)


        def orExpr(self):
            return self.getTypedRuleContext(MathExprParser.OrExprContext,0)


        def getRuleIndex(self):
            return MathExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MathExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.orExpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_orExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ToXorContext(OrExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.OrExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def xorExpr(self):
            return self.getTypedRuleContext(MathExprParser.XorExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToXor" ):
                listener.enterToXor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToXor" ):
                listener.exitToXor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToXor" ):
                return visitor.visitToXor(self)
            else:
                return visitor.visitChildren(self)


    class OrExpContext(OrExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.OrExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def orExpr(self):
            return self.getTypedRuleContext(MathExprParser.OrExprContext,0)

        def OR(self):
            return self.getToken(MathExprParser.OR, 0)
        def xorExpr(self):
            return self.getTypedRuleContext(MathExprParser.XorExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExp" ):
                listener.enterOrExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExp" ):
                listener.exitOrExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExp" ):
                return visitor.visitOrExp(self)
            else:
                return visitor.visitChildren(self)



    def orExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathExprParser.OrExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_orExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToXorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 29
            self.xorExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MathExprParser.OrExpContext(self, MathExprParser.OrExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_orExpr)
                    self.state = 31
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 32
                    self.match(MathExprParser.OR)
                    self.state = 33
                    self.xorExpr(0) 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class XorExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_xorExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class XorExpContext(XorExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.XorExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def xorExpr(self):
            return self.getTypedRuleContext(MathExprParser.XorExprContext,0)

        def XOR(self):
            return self.getToken(MathExprParser.XOR, 0)
        def andExpr(self):
            return self.getTypedRuleContext(MathExprParser.AndExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXorExp" ):
                listener.enterXorExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXorExp" ):
                listener.exitXorExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXorExp" ):
                return visitor.visitXorExp(self)
            else:
                return visitor.visitChildren(self)


    class ToAndContext(XorExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.XorExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def andExpr(self):
            return self.getTypedRuleContext(MathExprParser.AndExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToAnd" ):
                listener.enterToAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToAnd" ):
                listener.exitToAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToAnd" ):
                return visitor.visitToAnd(self)
            else:
                return visitor.visitChildren(self)



    def xorExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathExprParser.XorExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_xorExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToAndContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 40
            self.andExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MathExprParser.XorExpContext(self, MathExprParser.XorExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_xorExpr)
                    self.state = 42
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 43
                    self.match(MathExprParser.XOR)
                    self.state = 44
                    self.andExpr(0) 
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_andExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExpContext(AndExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AndExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def andExpr(self):
            return self.getTypedRuleContext(MathExprParser.AndExprContext,0)

        def AND(self):
            return self.getToken(MathExprParser.AND, 0)
        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExp" ):
                listener.enterAndExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExp" ):
                listener.exitAndExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExp" ):
                return visitor.visitAndExp(self)
            else:
                return visitor.visitChildren(self)


    class ToAddContext(AndExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AndExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToAdd" ):
                listener.enterToAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToAdd" ):
                listener.exitToAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToAdd" ):
                return visitor.visitToAdd(self)
            else:
                return visitor.visitChildren(self)



    def andExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathExprParser.AndExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_andExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToAddContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 51
            self.addExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MathExprParser.AndExpContext(self, MathExprParser.AndExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpr)
                    self.state = 53
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 54
                    self.match(MathExprParser.AND)
                    self.state = 55
                    self.addExpr(0) 
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_addExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddExpContext(AddExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AddExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)

        def PLUS(self):
            return self.getToken(MathExprParser.PLUS, 0)
        def mulExpr(self):
            return self.getTypedRuleContext(MathExprParser.MulExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExp" ):
                listener.enterAddExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExp" ):
                listener.exitAddExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExp" ):
                return visitor.visitAddExp(self)
            else:
                return visitor.visitChildren(self)


    class ToMulContext(AddExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AddExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulExpr(self):
            return self.getTypedRuleContext(MathExprParser.MulExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToMul" ):
                listener.enterToMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToMul" ):
                listener.exitToMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToMul" ):
                return visitor.visitToMul(self)
            else:
                return visitor.visitChildren(self)


    class SubExpContext(AddExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AddExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)

        def MINUS(self):
            return self.getToken(MathExprParser.MINUS, 0)
        def mulExpr(self):
            return self.getTypedRuleContext(MathExprParser.MulExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExp" ):
                listener.enterSubExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExp" ):
                listener.exitSubExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubExp" ):
                return visitor.visitSubExp(self)
            else:
                return visitor.visitChildren(self)



    def addExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathExprParser.AddExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_addExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToMulContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 62
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 70
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.AddExpContext(self, MathExprParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 64
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 65
                        self.match(MathExprParser.PLUS)
                        self.state = 66
                        self.mulExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.SubExpContext(self, MathExprParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 67
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 68
                        self.match(MathExprParser.MINUS)
                        self.state = 69
                        self.mulExpr(0)
                        pass

             
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_mulExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulExpContext(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.MulExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulExpr(self):
            return self.getTypedRuleContext(MathExprParser.MulExprContext,0)

        def MULT(self):
            return self.getToken(MathExprParser.MULT, 0)
        def powExpr(self):
            return self.getTypedRuleContext(MathExprParser.PowExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExp" ):
                listener.enterMulExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExp" ):
                listener.exitMulExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExp" ):
                return visitor.visitMulExp(self)
            else:
                return visitor.visitChildren(self)


    class ModExpContext(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.MulExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulExpr(self):
            return self.getTypedRuleContext(MathExprParser.MulExprContext,0)

        def MOD(self):
            return self.getToken(MathExprParser.MOD, 0)
        def powExpr(self):
            return self.getTypedRuleContext(MathExprParser.PowExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModExp" ):
                listener.enterModExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModExp" ):
                listener.exitModExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModExp" ):
                return visitor.visitModExp(self)
            else:
                return visitor.visitChildren(self)


    class DivExpContext(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.MulExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulExpr(self):
            return self.getTypedRuleContext(MathExprParser.MulExprContext,0)

        def DIV(self):
            return self.getToken(MathExprParser.DIV, 0)
        def powExpr(self):
            return self.getTypedRuleContext(MathExprParser.PowExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExp" ):
                listener.enterDivExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExp" ):
                listener.exitDivExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivExp" ):
                return visitor.visitDivExp(self)
            else:
                return visitor.visitChildren(self)


    class ToPowContext(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.MulExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def powExpr(self):
            return self.getTypedRuleContext(MathExprParser.PowExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToPow" ):
                listener.enterToPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToPow" ):
                listener.exitToPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToPow" ):
                return visitor.visitToPow(self)
            else:
                return visitor.visitChildren(self)



    def mulExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathExprParser.MulExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_mulExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToPowContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 76
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 87
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.MulExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 78
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 79
                        self.match(MathExprParser.MULT)
                        self.state = 80
                        self.powExpr()
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.DivExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 81
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 82
                        self.match(MathExprParser.DIV)
                        self.state = 83
                        self.powExpr()
                        pass

                    elif la_ == 3:
                        localctx = MathExprParser.ModExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 84
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 85
                        self.match(MathExprParser.MOD)
                        self.state = 86
                        self.powExpr()
                        pass

             
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PowExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_powExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PowExpContext(PowExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.PowExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryExpr(self):
            return self.getTypedRuleContext(MathExprParser.UnaryExprContext,0)

        def POW(self):
            return self.getToken(MathExprParser.POW, 0)
        def powExpr(self):
            return self.getTypedRuleContext(MathExprParser.PowExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowExp" ):
                listener.enterPowExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowExp" ):
                listener.exitPowExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowExp" ):
                return visitor.visitPowExp(self)
            else:
                return visitor.visitChildren(self)


    class ToUnaryContext(PowExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.PowExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryExpr(self):
            return self.getTypedRuleContext(MathExprParser.UnaryExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToUnary" ):
                listener.enterToUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToUnary" ):
                listener.exitToUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToUnary" ):
                return visitor.visitToUnary(self)
            else:
                return visitor.visitChildren(self)



    def powExpr(self):

        localctx = MathExprParser.PowExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_powExpr)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = MathExprParser.PowExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.unaryExpr()
                self.state = 93
                self.match(MathExprParser.POW)
                self.state = 94
                self.powExpr()
                pass

            elif la_ == 2:
                localctx = MathExprParser.ToUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.unaryExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_unaryExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NotExpContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MathExprParser.NOT, 0)
        def unaryExpr(self):
            return self.getTypedRuleContext(MathExprParser.UnaryExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExp" ):
                listener.enterNotExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExp" ):
                listener.exitNotExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExp" ):
                return visitor.visitNotExp(self)
            else:
                return visitor.visitChildren(self)


    class UnaryPlusContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(MathExprParser.PLUS, 0)
        def unaryExpr(self):
            return self.getTypedRuleContext(MathExprParser.UnaryExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPlus" ):
                listener.enterUnaryPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPlus" ):
                listener.exitUnaryPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryPlus" ):
                return visitor.visitUnaryPlus(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MathExprParser.MINUS, 0)
        def unaryExpr(self):
            return self.getTypedRuleContext(MathExprParser.UnaryExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class ToAtomContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(MathExprParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToAtom" ):
                listener.enterToAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToAtom" ):
                listener.exitToAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToAtom" ):
                return visitor.visitToAtom(self)
            else:
                return visitor.visitChildren(self)



    def unaryExpr(self):

        localctx = MathExprParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_unaryExpr)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                localctx = MathExprParser.UnaryPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(MathExprParser.PLUS)
                self.state = 100
                self.unaryExpr()
                pass
            elif token in [31]:
                localctx = MathExprParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(MathExprParser.MINUS)
                self.state = 102
                self.unaryExpr()
                pass
            elif token in [38]:
                localctx = MathExprParser.NotExpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.match(MathExprParser.NOT)
                self.state = 104
                self.unaryExpr()
                pass
            elif token in [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 39, 40, 41]:
                localctx = MathExprParser.ToAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Func2ExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func2(self):
            return self.getTypedRuleContext(MathExprParser.Func2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc2Exp" ):
                listener.enterFunc2Exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc2Exp" ):
                listener.exitFunc2Exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc2Exp" ):
                return visitor.visitFunc2Exp(self)
            else:
                return visitor.visitChildren(self)


    class VariableExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MathExprParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExp" ):
                listener.enterVariableExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExp" ):
                listener.exitVariableExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExp" ):
                return visitor.visitVariableExp(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExp" ):
                listener.enterParenExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExp" ):
                listener.exitParenExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExp" ):
                return visitor.visitParenExp(self)
            else:
                return visitor.visitChildren(self)


    class ConstantExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONSTANT(self):
            return self.getToken(MathExprParser.CONSTANT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExp" ):
                listener.enterConstantExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExp" ):
                listener.exitConstantExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantExp" ):
                return visitor.visitConstantExp(self)
            else:
                return visitor.visitChildren(self)


    class Func1ExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func1(self):
            return self.getTypedRuleContext(MathExprParser.Func1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc1Exp" ):
                listener.enterFunc1Exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc1Exp" ):
                listener.exitFunc1Exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc1Exp" ):
                return visitor.visitFunc1Exp(self)
            else:
                return visitor.visitChildren(self)


    class FuncNExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcN(self):
            return self.getTypedRuleContext(MathExprParser.FuncNContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncNExp" ):
                listener.enterFuncNExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncNExp" ):
                listener.exitFuncNExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncNExp" ):
                return visitor.visitFuncNExp(self)
            else:
                return visitor.visitChildren(self)


    class NumberExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(MathExprParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExp" ):
                listener.enterNumberExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExp" ):
                listener.exitNumberExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExp" ):
                return visitor.visitNumberExp(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = MathExprParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atom)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 25, 26, 27, 28, 29]:
                localctx = MathExprParser.Func1ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.func1()
                pass
            elif token in [10, 22]:
                localctx = MathExprParser.Func2ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.func2()
                pass
            elif token in [23, 24]:
                localctx = MathExprParser.FuncNExpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.funcN()
                pass
            elif token in [41]:
                localctx = MathExprParser.VariableExpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.match(MathExprParser.VARIABLE)
                pass
            elif token in [40]:
                localctx = MathExprParser.NumberExpContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 112
                self.match(MathExprParser.NUMBER)
                pass
            elif token in [39]:
                localctx = MathExprParser.ConstantExpContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.match(MathExprParser.CONSTANT)
                pass
            elif token in [1]:
                localctx = MathExprParser.ParenExpContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 114
                self.match(MathExprParser.T__0)
                self.state = 115
                self.expr()
                self.state = 116
                self.match(MathExprParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_func1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TanFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(MathExprParser.TAN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTanFunc" ):
                listener.enterTanFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTanFunc" ):
                listener.exitTanFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanFunc" ):
                return visitor.visitTanFunc(self)
            else:
                return visitor.visitChildren(self)


    class TanhFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TANH(self):
            return self.getToken(MathExprParser.TANH, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTanhFunc" ):
                listener.enterTanhFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTanhFunc" ):
                listener.exitTanhFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanhFunc" ):
                return visitor.visitTanhFunc(self)
            else:
                return visitor.visitChildren(self)


    class AcoshFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ACOSH(self):
            return self.getToken(MathExprParser.ACOSH, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcoshFunc" ):
                listener.enterAcoshFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcoshFunc" ):
                listener.exitAcoshFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcoshFunc" ):
                return visitor.visitAcoshFunc(self)
            else:
                return visitor.visitChildren(self)


    class GammaFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def GAMMA(self):
            return self.getToken(MathExprParser.GAMMA, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGammaFunc" ):
                listener.enterGammaFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGammaFunc" ):
                listener.exitGammaFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGammaFunc" ):
                return visitor.visitGammaFunc(self)
            else:
                return visitor.visitChildren(self)


    class CosFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def COS(self):
            return self.getToken(MathExprParser.COS, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosFunc" ):
                listener.enterCosFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosFunc" ):
                listener.exitCosFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosFunc" ):
                return visitor.visitCosFunc(self)
            else:
                return visitor.visitChildren(self)


    class SqrtFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SQRT(self):
            return self.getToken(MathExprParser.SQRT, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqrtFunc" ):
                listener.enterSqrtFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqrtFunc" ):
                listener.exitSqrtFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqrtFunc" ):
                return visitor.visitSqrtFunc(self)
            else:
                return visitor.visitChildren(self)


    class FloorFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOOR(self):
            return self.getToken(MathExprParser.FLOOR, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloorFunc" ):
                listener.enterFloorFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloorFunc" ):
                listener.exitFloorFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloorFunc" ):
                return visitor.visitFloorFunc(self)
            else:
                return visitor.visitChildren(self)


    class RoundFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROUND(self):
            return self.getToken(MathExprParser.ROUND, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoundFunc" ):
                listener.enterRoundFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoundFunc" ):
                listener.exitRoundFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoundFunc" ):
                return visitor.visitRoundFunc(self)
            else:
                return visitor.visitChildren(self)


    class CeilFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def CEIL(self):
            return self.getToken(MathExprParser.CEIL, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCeilFunc" ):
                listener.enterCeilFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCeilFunc" ):
                listener.exitCeilFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCeilFunc" ):
                return visitor.visitCeilFunc(self)
            else:
                return visitor.visitChildren(self)


    class AsinFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ASIN(self):
            return self.getToken(MathExprParser.ASIN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsinFunc" ):
                listener.enterAsinFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsinFunc" ):
                listener.exitAsinFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsinFunc" ):
                return visitor.visitAsinFunc(self)
            else:
                return visitor.visitChildren(self)


    class AsinhFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ASINH(self):
            return self.getToken(MathExprParser.ASINH, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsinhFunc" ):
                listener.enterAsinhFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsinhFunc" ):
                listener.exitAsinhFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsinhFunc" ):
                return visitor.visitAsinhFunc(self)
            else:
                return visitor.visitChildren(self)


    class AbsFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ABS(self):
            return self.getToken(MathExprParser.ABS, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbsFunc" ):
                listener.enterAbsFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbsFunc" ):
                listener.exitAbsFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbsFunc" ):
                return visitor.visitAbsFunc(self)
            else:
                return visitor.visitChildren(self)


    class AtanFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ATAN(self):
            return self.getToken(MathExprParser.ATAN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtanFunc" ):
                listener.enterAtanFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtanFunc" ):
                listener.exitAtanFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtanFunc" ):
                return visitor.visitAtanFunc(self)
            else:
                return visitor.visitChildren(self)


    class SinhFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SINH(self):
            return self.getToken(MathExprParser.SINH, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinhFunc" ):
                listener.enterSinhFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinhFunc" ):
                listener.exitSinhFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinhFunc" ):
                return visitor.visitSinhFunc(self)
            else:
                return visitor.visitChildren(self)


    class LogFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOG(self):
            return self.getToken(MathExprParser.LOG, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogFunc" ):
                listener.enterLogFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogFunc" ):
                listener.exitLogFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogFunc" ):
                return visitor.visitLogFunc(self)
            else:
                return visitor.visitChildren(self)


    class AtanhFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ATANH(self):
            return self.getToken(MathExprParser.ATANH, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtanhFunc" ):
                listener.enterAtanhFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtanhFunc" ):
                listener.exitAtanhFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtanhFunc" ):
                return visitor.visitAtanhFunc(self)
            else:
                return visitor.visitChildren(self)


    class LnFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def LN(self):
            return self.getToken(MathExprParser.LN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLnFunc" ):
                listener.enterLnFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLnFunc" ):
                listener.exitLnFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLnFunc" ):
                return visitor.visitLnFunc(self)
            else:
                return visitor.visitChildren(self)


    class NormFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def NORM(self):
            return self.getToken(MathExprParser.NORM, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormFunc" ):
                listener.enterNormFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormFunc" ):
                listener.exitNormFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormFunc" ):
                return visitor.visitNormFunc(self)
            else:
                return visitor.visitChildren(self)


    class SinFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(MathExprParser.SIN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinFunc" ):
                listener.enterSinFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinFunc" ):
                listener.exitSinFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinFunc" ):
                return visitor.visitSinFunc(self)
            else:
                return visitor.visitChildren(self)


    class ExpFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXP(self):
            return self.getToken(MathExprParser.EXP, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpFunc" ):
                listener.enterExpFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpFunc" ):
                listener.exitExpFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpFunc" ):
                return visitor.visitExpFunc(self)
            else:
                return visitor.visitChildren(self)


    class AcosFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ACOS(self):
            return self.getToken(MathExprParser.ACOS, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcosFunc" ):
                listener.enterAcosFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcosFunc" ):
                listener.exitAcosFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcosFunc" ):
                return visitor.visitAcosFunc(self)
            else:
                return visitor.visitChildren(self)


    class CoshFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def COSH(self):
            return self.getToken(MathExprParser.COSH, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoshFunc" ):
                listener.enterCoshFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoshFunc" ):
                listener.exitCoshFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoshFunc" ):
                return visitor.visitCoshFunc(self)
            else:
                return visitor.visitChildren(self)



    def func1(self):

        localctx = MathExprParser.Func1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func1)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = MathExprParser.SinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(MathExprParser.SIN)
                self.state = 121
                self.match(MathExprParser.T__0)
                self.state = 122
                self.expr()
                self.state = 123
                self.match(MathExprParser.T__1)
                pass
            elif token in [5]:
                localctx = MathExprParser.CosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(MathExprParser.COS)
                self.state = 126
                self.match(MathExprParser.T__0)
                self.state = 127
                self.expr()
                self.state = 128
                self.match(MathExprParser.T__1)
                pass
            elif token in [6]:
                localctx = MathExprParser.TanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.match(MathExprParser.TAN)
                self.state = 131
                self.match(MathExprParser.T__0)
                self.state = 132
                self.expr()
                self.state = 133
                self.match(MathExprParser.T__1)
                pass
            elif token in [7]:
                localctx = MathExprParser.AsinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.match(MathExprParser.ASIN)
                self.state = 136
                self.match(MathExprParser.T__0)
                self.state = 137
                self.expr()
                self.state = 138
                self.match(MathExprParser.T__1)
                pass
            elif token in [8]:
                localctx = MathExprParser.AcosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.match(MathExprParser.ACOS)
                self.state = 141
                self.match(MathExprParser.T__0)
                self.state = 142
                self.expr()
                self.state = 143
                self.match(MathExprParser.T__1)
                pass
            elif token in [9]:
                localctx = MathExprParser.AtanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 145
                self.match(MathExprParser.ATAN)
                self.state = 146
                self.match(MathExprParser.T__0)
                self.state = 147
                self.expr()
                self.state = 148
                self.match(MathExprParser.T__1)
                pass
            elif token in [11]:
                localctx = MathExprParser.SinhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 150
                self.match(MathExprParser.SINH)
                self.state = 151
                self.match(MathExprParser.T__0)
                self.state = 152
                self.expr()
                self.state = 153
                self.match(MathExprParser.T__1)
                pass
            elif token in [12]:
                localctx = MathExprParser.CoshFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 155
                self.match(MathExprParser.COSH)
                self.state = 156
                self.match(MathExprParser.T__0)
                self.state = 157
                self.expr()
                self.state = 158
                self.match(MathExprParser.T__1)
                pass
            elif token in [13]:
                localctx = MathExprParser.TanhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 160
                self.match(MathExprParser.TANH)
                self.state = 161
                self.match(MathExprParser.T__0)
                self.state = 162
                self.expr()
                self.state = 163
                self.match(MathExprParser.T__1)
                pass
            elif token in [14]:
                localctx = MathExprParser.AsinhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 165
                self.match(MathExprParser.ASINH)
                self.state = 166
                self.match(MathExprParser.T__0)
                self.state = 167
                self.expr()
                self.state = 168
                self.match(MathExprParser.T__1)
                pass
            elif token in [15]:
                localctx = MathExprParser.AcoshFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 170
                self.match(MathExprParser.ACOSH)
                self.state = 171
                self.match(MathExprParser.T__0)
                self.state = 172
                self.expr()
                self.state = 173
                self.match(MathExprParser.T__1)
                pass
            elif token in [16]:
                localctx = MathExprParser.AtanhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 175
                self.match(MathExprParser.ATANH)
                self.state = 176
                self.match(MathExprParser.T__0)
                self.state = 177
                self.expr()
                self.state = 178
                self.match(MathExprParser.T__1)
                pass
            elif token in [17]:
                localctx = MathExprParser.AbsFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 180
                self.match(MathExprParser.ABS)
                self.state = 181
                self.match(MathExprParser.T__0)
                self.state = 182
                self.expr()
                self.state = 183
                self.match(MathExprParser.T__1)
                pass
            elif token in [18]:
                localctx = MathExprParser.SqrtFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 185
                self.match(MathExprParser.SQRT)
                self.state = 186
                self.match(MathExprParser.T__0)
                self.state = 187
                self.expr()
                self.state = 188
                self.match(MathExprParser.T__1)
                pass
            elif token in [19]:
                localctx = MathExprParser.LnFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 190
                self.match(MathExprParser.LN)
                self.state = 191
                self.match(MathExprParser.T__0)
                self.state = 192
                self.expr()
                self.state = 193
                self.match(MathExprParser.T__1)
                pass
            elif token in [20]:
                localctx = MathExprParser.LogFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 195
                self.match(MathExprParser.LOG)
                self.state = 196
                self.match(MathExprParser.T__0)
                self.state = 197
                self.expr()
                self.state = 198
                self.match(MathExprParser.T__1)
                pass
            elif token in [21]:
                localctx = MathExprParser.ExpFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 200
                self.match(MathExprParser.EXP)
                self.state = 201
                self.match(MathExprParser.T__0)
                self.state = 202
                self.expr()
                self.state = 203
                self.match(MathExprParser.T__1)
                pass
            elif token in [25]:
                localctx = MathExprParser.NormFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 205
                self.match(MathExprParser.NORM)
                self.state = 206
                self.match(MathExprParser.T__0)
                self.state = 207
                self.expr()
                self.state = 208
                self.match(MathExprParser.T__1)
                pass
            elif token in [26]:
                localctx = MathExprParser.FloorFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 210
                self.match(MathExprParser.FLOOR)
                self.state = 211
                self.match(MathExprParser.T__0)
                self.state = 212
                self.expr()
                self.state = 213
                self.match(MathExprParser.T__1)
                pass
            elif token in [27]:
                localctx = MathExprParser.CeilFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 20)
                self.state = 215
                self.match(MathExprParser.CEIL)
                self.state = 216
                self.match(MathExprParser.T__0)
                self.state = 217
                self.expr()
                self.state = 218
                self.match(MathExprParser.T__1)
                pass
            elif token in [28]:
                localctx = MathExprParser.RoundFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 21)
                self.state = 220
                self.match(MathExprParser.ROUND)
                self.state = 221
                self.match(MathExprParser.T__0)
                self.state = 222
                self.expr()
                self.state = 223
                self.match(MathExprParser.T__1)
                pass
            elif token in [29]:
                localctx = MathExprParser.GammaFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 22)
                self.state = 225
                self.match(MathExprParser.GAMMA)
                self.state = 226
                self.match(MathExprParser.T__0)
                self.state = 227
                self.expr()
                self.state = 228
                self.match(MathExprParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_func2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PowFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def POW(self):
            return self.getToken(MathExprParser.POW, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowFunc" ):
                listener.enterPowFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowFunc" ):
                listener.exitPowFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowFunc" ):
                return visitor.visitPowFunc(self)
            else:
                return visitor.visitChildren(self)


    class Atan2FuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ATAN2(self):
            return self.getToken(MathExprParser.ATAN2, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtan2Func" ):
                listener.enterAtan2Func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtan2Func" ):
                listener.exitAtan2Func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtan2Func" ):
                return visitor.visitAtan2Func(self)
            else:
                return visitor.visitChildren(self)



    def func2(self):

        localctx = MathExprParser.Func2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func2)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = MathExprParser.PowFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(MathExprParser.POW)
                self.state = 233
                self.match(MathExprParser.T__0)
                self.state = 234
                self.expr()
                self.state = 235
                self.match(MathExprParser.T__2)
                self.state = 236
                self.expr()
                self.state = 237
                self.match(MathExprParser.T__1)
                pass
            elif token in [10]:
                localctx = MathExprParser.Atan2FuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(MathExprParser.ATAN2)
                self.state = 240
                self.match(MathExprParser.T__0)
                self.state = 241
                self.expr()
                self.state = 242
                self.match(MathExprParser.T__2)
                self.state = 243
                self.expr()
                self.state = 244
                self.match(MathExprParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncNContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_funcN

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MinFuncContext(FuncNContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncNContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MIN(self):
            return self.getToken(MathExprParser.MIN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinFunc" ):
                listener.enterMinFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinFunc" ):
                listener.exitMinFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinFunc" ):
                return visitor.visitMinFunc(self)
            else:
                return visitor.visitChildren(self)


    class MaxFuncContext(FuncNContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncNContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MAX(self):
            return self.getToken(MathExprParser.MAX, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaxFunc" ):
                listener.enterMaxFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaxFunc" ):
                listener.exitMaxFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaxFunc" ):
                return visitor.visitMaxFunc(self)
            else:
                return visitor.visitChildren(self)



    def funcN(self):

        localctx = MathExprParser.FuncNContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcN)
        self._la = 0 # Token type
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = MathExprParser.MinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(MathExprParser.MIN)
                self.state = 249
                self.match(MathExprParser.T__0)
                self.state = 250
                self.expr()
                self.state = 253 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 251
                    self.match(MathExprParser.T__2)
                    self.state = 252
                    self.expr()
                    self.state = 255 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                self.state = 257
                self.match(MathExprParser.T__1)
                pass
            elif token in [24]:
                localctx = MathExprParser.MaxFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(MathExprParser.MAX)
                self.state = 260
                self.match(MathExprParser.T__0)
                self.state = 261
                self.expr()
                self.state = 264 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 262
                    self.match(MathExprParser.T__2)
                    self.state = 263
                    self.expr()
                    self.state = 266 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                self.state = 268
                self.match(MathExprParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.orExpr_sempred
        self._predicates[2] = self.xorExpr_sempred
        self._predicates[3] = self.andExpr_sempred
        self._predicates[4] = self.addExpr_sempred
        self._predicates[5] = self.mulExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def orExpr_sempred(self, localctx:OrExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def xorExpr_sempred(self, localctx:XorExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def andExpr_sempred(self, localctx:AndExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def addExpr_sempred(self, localctx:AddExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def mulExpr_sempred(self, localctx:MulExprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




