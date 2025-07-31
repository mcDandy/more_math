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
        4,1,44,268,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,3,0,23,8,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,1,3,1,3,
        1,3,1,3,1,3,3,3,61,8,3,1,4,1,4,1,4,1,4,1,4,3,4,68,8,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,81,8,5,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,3,6,203,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,233,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,9,4,9,249,8,9,11,9,12,9,250,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,4,9,260,8,9,11,9,12,9,261,1,9,1,9,3,9,266,8,9,1,9,0,2,2,4,10,0,
        2,4,6,8,10,12,14,16,18,0,0,302,0,22,1,0,0,0,2,24,1,0,0,0,4,38,1,
        0,0,0,6,60,1,0,0,0,8,67,1,0,0,0,10,80,1,0,0,0,12,202,1,0,0,0,14,
        232,1,0,0,0,16,234,1,0,0,0,18,265,1,0,0,0,20,23,3,10,5,0,21,23,3,
        2,1,0,22,20,1,0,0,0,22,21,1,0,0,0,23,1,1,0,0,0,24,25,6,1,-1,0,25,
        26,3,4,2,0,26,35,1,0,0,0,27,28,10,3,0,0,28,29,5,35,0,0,29,34,3,4,
        2,0,30,31,10,2,0,0,31,32,5,36,0,0,32,34,3,4,2,0,33,27,1,0,0,0,33,
        30,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,3,1,0,0,
        0,37,35,1,0,0,0,38,39,6,2,-1,0,39,40,3,6,3,0,40,52,1,0,0,0,41,42,
        10,4,0,0,42,43,5,37,0,0,43,51,3,6,3,0,44,45,10,3,0,0,45,46,5,38,
        0,0,46,51,3,6,3,0,47,48,10,2,0,0,48,49,5,39,0,0,49,51,3,6,3,0,50,
        41,1,0,0,0,50,44,1,0,0,0,50,47,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,
        0,52,53,1,0,0,0,53,5,1,0,0,0,54,52,1,0,0,0,55,56,3,8,4,0,56,57,5,
        40,0,0,57,58,3,6,3,0,58,61,1,0,0,0,59,61,3,8,4,0,60,55,1,0,0,0,60,
        59,1,0,0,0,61,7,1,0,0,0,62,63,5,35,0,0,63,68,3,8,4,0,64,65,5,36,
        0,0,65,68,3,8,4,0,66,68,3,10,5,0,67,62,1,0,0,0,67,64,1,0,0,0,67,
        66,1,0,0,0,68,9,1,0,0,0,69,81,3,12,6,0,70,81,3,14,7,0,71,81,3,16,
        8,0,72,81,3,18,9,0,73,81,5,43,0,0,74,81,5,42,0,0,75,81,5,41,0,0,
        76,77,5,1,0,0,77,78,3,0,0,0,78,79,5,2,0,0,79,81,1,0,0,0,80,69,1,
        0,0,0,80,70,1,0,0,0,80,71,1,0,0,0,80,72,1,0,0,0,80,73,1,0,0,0,80,
        74,1,0,0,0,80,75,1,0,0,0,80,76,1,0,0,0,81,11,1,0,0,0,82,83,5,4,0,
        0,83,84,5,1,0,0,84,85,3,0,0,0,85,86,5,2,0,0,86,203,1,0,0,0,87,88,
        5,5,0,0,88,89,5,1,0,0,89,90,3,0,0,0,90,91,5,2,0,0,91,203,1,0,0,0,
        92,93,5,6,0,0,93,94,5,1,0,0,94,95,3,0,0,0,95,96,5,2,0,0,96,203,1,
        0,0,0,97,98,5,7,0,0,98,99,5,1,0,0,99,100,3,0,0,0,100,101,5,2,0,0,
        101,203,1,0,0,0,102,103,5,8,0,0,103,104,5,1,0,0,104,105,3,0,0,0,
        105,106,5,2,0,0,106,203,1,0,0,0,107,108,5,9,0,0,108,109,5,1,0,0,
        109,110,3,0,0,0,110,111,5,2,0,0,111,203,1,0,0,0,112,113,5,11,0,0,
        113,114,5,1,0,0,114,115,3,0,0,0,115,116,5,2,0,0,116,203,1,0,0,0,
        117,118,5,12,0,0,118,119,5,1,0,0,119,120,3,0,0,0,120,121,5,2,0,0,
        121,203,1,0,0,0,122,123,5,13,0,0,123,124,5,1,0,0,124,125,3,0,0,0,
        125,126,5,2,0,0,126,203,1,0,0,0,127,128,5,14,0,0,128,129,5,1,0,0,
        129,130,3,0,0,0,130,131,5,2,0,0,131,203,1,0,0,0,132,133,5,15,0,0,
        133,134,5,1,0,0,134,135,3,0,0,0,135,136,5,2,0,0,136,203,1,0,0,0,
        137,138,5,16,0,0,138,139,5,1,0,0,139,140,3,0,0,0,140,141,5,2,0,0,
        141,203,1,0,0,0,142,143,5,17,0,0,143,144,5,1,0,0,144,145,3,0,0,0,
        145,146,5,2,0,0,146,203,1,0,0,0,147,148,5,18,0,0,148,149,5,1,0,0,
        149,150,3,0,0,0,150,151,5,2,0,0,151,203,1,0,0,0,152,153,5,19,0,0,
        153,154,5,1,0,0,154,155,3,0,0,0,155,156,5,2,0,0,156,203,1,0,0,0,
        157,158,5,20,0,0,158,159,5,1,0,0,159,160,3,0,0,0,160,161,5,2,0,0,
        161,203,1,0,0,0,162,163,5,21,0,0,163,164,5,1,0,0,164,165,3,0,0,0,
        165,166,5,2,0,0,166,203,1,0,0,0,167,168,5,26,0,0,168,169,5,1,0,0,
        169,170,3,0,0,0,170,171,5,2,0,0,171,203,1,0,0,0,172,173,5,27,0,0,
        173,174,5,1,0,0,174,175,3,0,0,0,175,176,5,2,0,0,176,203,1,0,0,0,
        177,178,5,28,0,0,178,179,5,1,0,0,179,180,3,0,0,0,180,181,5,2,0,0,
        181,203,1,0,0,0,182,183,5,29,0,0,183,184,5,1,0,0,184,185,3,0,0,0,
        185,186,5,2,0,0,186,203,1,0,0,0,187,188,5,30,0,0,188,189,5,1,0,0,
        189,190,3,0,0,0,190,191,5,2,0,0,191,203,1,0,0,0,192,193,5,31,0,0,
        193,194,5,1,0,0,194,195,3,0,0,0,195,196,5,2,0,0,196,203,1,0,0,0,
        197,198,5,33,0,0,198,199,5,1,0,0,199,200,3,0,0,0,200,201,5,2,0,0,
        201,203,1,0,0,0,202,82,1,0,0,0,202,87,1,0,0,0,202,92,1,0,0,0,202,
        97,1,0,0,0,202,102,1,0,0,0,202,107,1,0,0,0,202,112,1,0,0,0,202,117,
        1,0,0,0,202,122,1,0,0,0,202,127,1,0,0,0,202,132,1,0,0,0,202,137,
        1,0,0,0,202,142,1,0,0,0,202,147,1,0,0,0,202,152,1,0,0,0,202,157,
        1,0,0,0,202,162,1,0,0,0,202,167,1,0,0,0,202,172,1,0,0,0,202,177,
        1,0,0,0,202,182,1,0,0,0,202,187,1,0,0,0,202,192,1,0,0,0,202,197,
        1,0,0,0,203,13,1,0,0,0,204,205,5,32,0,0,205,206,5,1,0,0,206,207,
        3,0,0,0,207,208,5,3,0,0,208,209,3,0,0,0,209,210,5,2,0,0,210,233,
        1,0,0,0,211,212,5,10,0,0,212,213,5,1,0,0,213,214,3,0,0,0,214,215,
        5,3,0,0,215,216,3,0,0,0,216,217,5,2,0,0,217,233,1,0,0,0,218,219,
        5,24,0,0,219,220,5,1,0,0,220,221,3,0,0,0,221,222,5,3,0,0,222,223,
        3,0,0,0,223,224,5,2,0,0,224,233,1,0,0,0,225,226,5,25,0,0,226,227,
        5,1,0,0,227,228,3,0,0,0,228,229,5,3,0,0,229,230,3,0,0,0,230,231,
        5,2,0,0,231,233,1,0,0,0,232,204,1,0,0,0,232,211,1,0,0,0,232,218,
        1,0,0,0,232,225,1,0,0,0,233,15,1,0,0,0,234,235,5,34,0,0,235,236,
        5,1,0,0,236,237,3,0,0,0,237,238,5,3,0,0,238,239,3,0,0,0,239,240,
        5,3,0,0,240,241,3,0,0,0,241,242,5,2,0,0,242,17,1,0,0,0,243,244,5,
        22,0,0,244,245,5,1,0,0,245,248,3,0,0,0,246,247,5,3,0,0,247,249,3,
        0,0,0,248,246,1,0,0,0,249,250,1,0,0,0,250,248,1,0,0,0,250,251,1,
        0,0,0,251,252,1,0,0,0,252,253,5,2,0,0,253,266,1,0,0,0,254,255,5,
        23,0,0,255,256,5,1,0,0,256,259,3,0,0,0,257,258,5,3,0,0,258,260,3,
        0,0,0,259,257,1,0,0,0,260,261,1,0,0,0,261,259,1,0,0,0,261,262,1,
        0,0,0,262,263,1,0,0,0,263,264,5,2,0,0,264,266,1,0,0,0,265,243,1,
        0,0,0,265,254,1,0,0,0,266,19,1,0,0,0,13,22,33,35,50,52,60,67,80,
        202,232,250,261,265
    ]

class MathExprParser ( Parser ):

    grammarFileName = "MathExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'sin'", "'cos'", 
                     "'tan'", "'asin'", "'acos'", "'atan'", "'atan2'", "'sinh'", 
                     "'cosh'", "'tanh'", "'asinh'", "'acosh'", "'atanh'", 
                     "'abs'", "'sqrt'", "'ln'", "'log'", "'exp'", "'smin'", 
                     "'smax'", "'tmin'", "'tmax'", "'tnorm'", "'snorm'", 
                     "'floor'", "'ceil'", "'round'", "'gamma'", "'pow'", 
                     "'sigmoid'", "'clamp'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN", "ATAN2", 
                      "SINH", "COSH", "TANH", "ASINH", "ACOSH", "ATANH", 
                      "ABS", "SQRT", "LN", "LOG", "EXP", "SMIN", "SMAX", 
                      "TMIN", "TMAX", "TNORM", "SNORM", "FLOOR", "CEIL", 
                      "ROUND", "GAMMA", "POWE", "SIGM", "CLAMP", "PLUS", 
                      "MINUS", "MULT", "DIV", "MOD", "POW", "CONSTANT", 
                      "NUMBER", "VARIABLE", "WS" ]

    RULE_expr = 0
    RULE_addExpr = 1
    RULE_mulExpr = 2
    RULE_powExpr = 3
    RULE_unaryExpr = 4
    RULE_atom = 5
    RULE_func1 = 6
    RULE_func2 = 7
    RULE_func3 = 8
    RULE_funcN = 9

    ruleNames =  [ "expr", "addExpr", "mulExpr", "powExpr", "unaryExpr", 
                   "atom", "func1", "func2", "func3", "funcN" ]

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
    SMIN=22
    SMAX=23
    TMIN=24
    TMAX=25
    TNORM=26
    SNORM=27
    FLOOR=28
    CEIL=29
    ROUND=30
    GAMMA=31
    POWE=32
    SIGM=33
    CLAMP=34
    PLUS=35
    MINUS=36
    MULT=37
    DIV=38
    MOD=39
    POW=40
    CONSTANT=41
    NUMBER=42
    VARIABLE=43
    WS=44

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


        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)


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
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.addExpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_addExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToMulContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 25
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.AddExpContext(self, MathExprParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 27
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 28
                        self.match(MathExprParser.PLUS)
                        self.state = 29
                        self.mulExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.SubExpContext(self, MathExprParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 30
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 31
                        self.match(MathExprParser.MINUS)
                        self.state = 32
                        self.mulExpr(0)
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_mulExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToPowContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 39
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.MulExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 41
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 42
                        self.match(MathExprParser.MULT)
                        self.state = 43
                        self.powExpr()
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.DivExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 44
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 45
                        self.match(MathExprParser.DIV)
                        self.state = 46
                        self.powExpr()
                        pass

                    elif la_ == 3:
                        localctx = MathExprParser.ModExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 47
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 48
                        self.match(MathExprParser.MOD)
                        self.state = 49
                        self.powExpr()
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_powExpr)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = MathExprParser.PowExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.unaryExpr()
                self.state = 56
                self.match(MathExprParser.POW)
                self.state = 57
                self.powExpr()
                pass

            elif la_ == 2:
                localctx = MathExprParser.ToUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
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
        self.enterRule(localctx, 8, self.RULE_unaryExpr)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                localctx = MathExprParser.UnaryPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(MathExprParser.PLUS)
                self.state = 63
                self.unaryExpr()
                pass
            elif token in [36]:
                localctx = MathExprParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(MathExprParser.MINUS)
                self.state = 65
                self.unaryExpr()
                pass
            elif token in [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 41, 42, 43]:
                localctx = MathExprParser.ToAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 66
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


    class Func3ExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func3(self):
            return self.getTypedRuleContext(MathExprParser.Func3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc3Exp" ):
                listener.enterFunc3Exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc3Exp" ):
                listener.exitFunc3Exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc3Exp" ):
                return visitor.visitFunc3Exp(self)
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
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 26, 27, 28, 29, 30, 31, 33]:
                localctx = MathExprParser.Func1ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.func1()
                pass
            elif token in [10, 24, 25, 32]:
                localctx = MathExprParser.Func2ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.func2()
                pass
            elif token in [34]:
                localctx = MathExprParser.Func3ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.func3()
                pass
            elif token in [22, 23]:
                localctx = MathExprParser.FuncNExpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.funcN()
                pass
            elif token in [43]:
                localctx = MathExprParser.VariableExpContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.match(MathExprParser.VARIABLE)
                pass
            elif token in [42]:
                localctx = MathExprParser.NumberExpContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.match(MathExprParser.NUMBER)
                pass
            elif token in [41]:
                localctx = MathExprParser.ConstantExpContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.match(MathExprParser.CONSTANT)
                pass
            elif token in [1]:
                localctx = MathExprParser.ParenExpContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 76
                self.match(MathExprParser.T__0)
                self.state = 77
                self.expr()
                self.state = 78
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


    class SigmoidFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIGM(self):
            return self.getToken(MathExprParser.SIGM, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSigmoidFunc" ):
                listener.enterSigmoidFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSigmoidFunc" ):
                listener.exitSigmoidFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSigmoidFunc" ):
                return visitor.visitSigmoidFunc(self)
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


    class TNormFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TNORM(self):
            return self.getToken(MathExprParser.TNORM, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTNormFunc" ):
                listener.enterTNormFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTNormFunc" ):
                listener.exitTNormFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTNormFunc" ):
                return visitor.visitTNormFunc(self)
            else:
                return visitor.visitChildren(self)


    class SNormFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SNORM(self):
            return self.getToken(MathExprParser.SNORM, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSNormFunc" ):
                listener.enterSNormFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSNormFunc" ):
                listener.exitSNormFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSNormFunc" ):
                return visitor.visitSNormFunc(self)
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
        self.enterRule(localctx, 12, self.RULE_func1)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = MathExprParser.SinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(MathExprParser.SIN)
                self.state = 83
                self.match(MathExprParser.T__0)
                self.state = 84
                self.expr()
                self.state = 85
                self.match(MathExprParser.T__1)
                pass
            elif token in [5]:
                localctx = MathExprParser.CosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(MathExprParser.COS)
                self.state = 88
                self.match(MathExprParser.T__0)
                self.state = 89
                self.expr()
                self.state = 90
                self.match(MathExprParser.T__1)
                pass
            elif token in [6]:
                localctx = MathExprParser.TanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.match(MathExprParser.TAN)
                self.state = 93
                self.match(MathExprParser.T__0)
                self.state = 94
                self.expr()
                self.state = 95
                self.match(MathExprParser.T__1)
                pass
            elif token in [7]:
                localctx = MathExprParser.AsinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.match(MathExprParser.ASIN)
                self.state = 98
                self.match(MathExprParser.T__0)
                self.state = 99
                self.expr()
                self.state = 100
                self.match(MathExprParser.T__1)
                pass
            elif token in [8]:
                localctx = MathExprParser.AcosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.match(MathExprParser.ACOS)
                self.state = 103
                self.match(MathExprParser.T__0)
                self.state = 104
                self.expr()
                self.state = 105
                self.match(MathExprParser.T__1)
                pass
            elif token in [9]:
                localctx = MathExprParser.AtanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 107
                self.match(MathExprParser.ATAN)
                self.state = 108
                self.match(MathExprParser.T__0)
                self.state = 109
                self.expr()
                self.state = 110
                self.match(MathExprParser.T__1)
                pass
            elif token in [11]:
                localctx = MathExprParser.SinhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 112
                self.match(MathExprParser.SINH)
                self.state = 113
                self.match(MathExprParser.T__0)
                self.state = 114
                self.expr()
                self.state = 115
                self.match(MathExprParser.T__1)
                pass
            elif token in [12]:
                localctx = MathExprParser.CoshFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 117
                self.match(MathExprParser.COSH)
                self.state = 118
                self.match(MathExprParser.T__0)
                self.state = 119
                self.expr()
                self.state = 120
                self.match(MathExprParser.T__1)
                pass
            elif token in [13]:
                localctx = MathExprParser.TanhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 122
                self.match(MathExprParser.TANH)
                self.state = 123
                self.match(MathExprParser.T__0)
                self.state = 124
                self.expr()
                self.state = 125
                self.match(MathExprParser.T__1)
                pass
            elif token in [14]:
                localctx = MathExprParser.AsinhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 127
                self.match(MathExprParser.ASINH)
                self.state = 128
                self.match(MathExprParser.T__0)
                self.state = 129
                self.expr()
                self.state = 130
                self.match(MathExprParser.T__1)
                pass
            elif token in [15]:
                localctx = MathExprParser.AcoshFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 132
                self.match(MathExprParser.ACOSH)
                self.state = 133
                self.match(MathExprParser.T__0)
                self.state = 134
                self.expr()
                self.state = 135
                self.match(MathExprParser.T__1)
                pass
            elif token in [16]:
                localctx = MathExprParser.AtanhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 137
                self.match(MathExprParser.ATANH)
                self.state = 138
                self.match(MathExprParser.T__0)
                self.state = 139
                self.expr()
                self.state = 140
                self.match(MathExprParser.T__1)
                pass
            elif token in [17]:
                localctx = MathExprParser.AbsFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 142
                self.match(MathExprParser.ABS)
                self.state = 143
                self.match(MathExprParser.T__0)
                self.state = 144
                self.expr()
                self.state = 145
                self.match(MathExprParser.T__1)
                pass
            elif token in [18]:
                localctx = MathExprParser.SqrtFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 147
                self.match(MathExprParser.SQRT)
                self.state = 148
                self.match(MathExprParser.T__0)
                self.state = 149
                self.expr()
                self.state = 150
                self.match(MathExprParser.T__1)
                pass
            elif token in [19]:
                localctx = MathExprParser.LnFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 152
                self.match(MathExprParser.LN)
                self.state = 153
                self.match(MathExprParser.T__0)
                self.state = 154
                self.expr()
                self.state = 155
                self.match(MathExprParser.T__1)
                pass
            elif token in [20]:
                localctx = MathExprParser.LogFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 157
                self.match(MathExprParser.LOG)
                self.state = 158
                self.match(MathExprParser.T__0)
                self.state = 159
                self.expr()
                self.state = 160
                self.match(MathExprParser.T__1)
                pass
            elif token in [21]:
                localctx = MathExprParser.ExpFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 162
                self.match(MathExprParser.EXP)
                self.state = 163
                self.match(MathExprParser.T__0)
                self.state = 164
                self.expr()
                self.state = 165
                self.match(MathExprParser.T__1)
                pass
            elif token in [26]:
                localctx = MathExprParser.TNormFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 167
                self.match(MathExprParser.TNORM)
                self.state = 168
                self.match(MathExprParser.T__0)
                self.state = 169
                self.expr()
                self.state = 170
                self.match(MathExprParser.T__1)
                pass
            elif token in [27]:
                localctx = MathExprParser.SNormFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 172
                self.match(MathExprParser.SNORM)
                self.state = 173
                self.match(MathExprParser.T__0)
                self.state = 174
                self.expr()
                self.state = 175
                self.match(MathExprParser.T__1)
                pass
            elif token in [28]:
                localctx = MathExprParser.FloorFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 20)
                self.state = 177
                self.match(MathExprParser.FLOOR)
                self.state = 178
                self.match(MathExprParser.T__0)
                self.state = 179
                self.expr()
                self.state = 180
                self.match(MathExprParser.T__1)
                pass
            elif token in [29]:
                localctx = MathExprParser.CeilFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 21)
                self.state = 182
                self.match(MathExprParser.CEIL)
                self.state = 183
                self.match(MathExprParser.T__0)
                self.state = 184
                self.expr()
                self.state = 185
                self.match(MathExprParser.T__1)
                pass
            elif token in [30]:
                localctx = MathExprParser.RoundFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 22)
                self.state = 187
                self.match(MathExprParser.ROUND)
                self.state = 188
                self.match(MathExprParser.T__0)
                self.state = 189
                self.expr()
                self.state = 190
                self.match(MathExprParser.T__1)
                pass
            elif token in [31]:
                localctx = MathExprParser.GammaFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 23)
                self.state = 192
                self.match(MathExprParser.GAMMA)
                self.state = 193
                self.match(MathExprParser.T__0)
                self.state = 194
                self.expr()
                self.state = 195
                self.match(MathExprParser.T__1)
                pass
            elif token in [33]:
                localctx = MathExprParser.SigmoidFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 24)
                self.state = 197
                self.match(MathExprParser.SIGM)
                self.state = 198
                self.match(MathExprParser.T__0)
                self.state = 199
                self.expr()
                self.state = 200
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



    class TMaxFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TMAX(self):
            return self.getToken(MathExprParser.TMAX, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTMaxFunc" ):
                listener.enterTMaxFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTMaxFunc" ):
                listener.exitTMaxFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTMaxFunc" ):
                return visitor.visitTMaxFunc(self)
            else:
                return visitor.visitChildren(self)


    class PowFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def POWE(self):
            return self.getToken(MathExprParser.POWE, 0)
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


    class TMinFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TMIN(self):
            return self.getToken(MathExprParser.TMIN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTMinFunc" ):
                listener.enterTMinFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTMinFunc" ):
                listener.exitTMinFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTMinFunc" ):
                return visitor.visitTMinFunc(self)
            else:
                return visitor.visitChildren(self)



    def func2(self):

        localctx = MathExprParser.Func2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func2)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                localctx = MathExprParser.PowFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(MathExprParser.POWE)
                self.state = 205
                self.match(MathExprParser.T__0)
                self.state = 206
                self.expr()
                self.state = 207
                self.match(MathExprParser.T__2)
                self.state = 208
                self.expr()
                self.state = 209
                self.match(MathExprParser.T__1)
                pass
            elif token in [10]:
                localctx = MathExprParser.Atan2FuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(MathExprParser.ATAN2)
                self.state = 212
                self.match(MathExprParser.T__0)
                self.state = 213
                self.expr()
                self.state = 214
                self.match(MathExprParser.T__2)
                self.state = 215
                self.expr()
                self.state = 216
                self.match(MathExprParser.T__1)
                pass
            elif token in [24]:
                localctx = MathExprParser.TMinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.match(MathExprParser.TMIN)
                self.state = 219
                self.match(MathExprParser.T__0)
                self.state = 220
                self.expr()
                self.state = 221
                self.match(MathExprParser.T__2)
                self.state = 222
                self.expr()
                self.state = 223
                self.match(MathExprParser.T__1)
                pass
            elif token in [25]:
                localctx = MathExprParser.TMaxFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.match(MathExprParser.TMAX)
                self.state = 226
                self.match(MathExprParser.T__0)
                self.state = 227
                self.expr()
                self.state = 228
                self.match(MathExprParser.T__2)
                self.state = 229
                self.expr()
                self.state = 230
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


    class Func3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_func3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ClampFuncContext(Func3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def CLAMP(self):
            return self.getToken(MathExprParser.CLAMP, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClampFunc" ):
                listener.enterClampFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClampFunc" ):
                listener.exitClampFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClampFunc" ):
                return visitor.visitClampFunc(self)
            else:
                return visitor.visitChildren(self)



    def func3(self):

        localctx = MathExprParser.Func3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func3)
        try:
            localctx = MathExprParser.ClampFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MathExprParser.CLAMP)
            self.state = 235
            self.match(MathExprParser.T__0)
            self.state = 236
            self.expr()
            self.state = 237
            self.match(MathExprParser.T__2)
            self.state = 238
            self.expr()
            self.state = 239
            self.match(MathExprParser.T__2)
            self.state = 240
            self.expr()
            self.state = 241
            self.match(MathExprParser.T__1)
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



    class SMaxFuncContext(FuncNContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncNContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SMAX(self):
            return self.getToken(MathExprParser.SMAX, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSMaxFunc" ):
                listener.enterSMaxFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSMaxFunc" ):
                listener.exitSMaxFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSMaxFunc" ):
                return visitor.visitSMaxFunc(self)
            else:
                return visitor.visitChildren(self)


    class SMinFuncContext(FuncNContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncNContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SMIN(self):
            return self.getToken(MathExprParser.SMIN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSMinFunc" ):
                listener.enterSMinFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSMinFunc" ):
                listener.exitSMinFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSMinFunc" ):
                return visitor.visitSMinFunc(self)
            else:
                return visitor.visitChildren(self)



    def funcN(self):

        localctx = MathExprParser.FuncNContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcN)
        self._la = 0 # Token type
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = MathExprParser.SMinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(MathExprParser.SMIN)
                self.state = 244
                self.match(MathExprParser.T__0)
                self.state = 245
                self.expr()
                self.state = 248 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 246
                    self.match(MathExprParser.T__2)
                    self.state = 247
                    self.expr()
                    self.state = 250 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                self.state = 252
                self.match(MathExprParser.T__1)
                pass
            elif token in [23]:
                localctx = MathExprParser.SMaxFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(MathExprParser.SMAX)
                self.state = 255
                self.match(MathExprParser.T__0)
                self.state = 256
                self.expr()
                self.state = 259 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 257
                    self.match(MathExprParser.T__2)
                    self.state = 258
                    self.expr()
                    self.state = 261 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                self.state = 263
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
        self._predicates[1] = self.addExpr_sempred
        self._predicates[2] = self.mulExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def addExpr_sempred(self, localctx:AddExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mulExpr_sempred(self, localctx:MulExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




