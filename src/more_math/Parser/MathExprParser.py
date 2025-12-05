# Generated from src/more_math/Parser/MathExpr.g4 by ANTLR 4.13.2
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
        4,1,63,382,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,3,0,27,8,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,5,1,50,8,1,10,1,12,1,53,9,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,5,2,64,8,2,10,2,12,2,67,9,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,81,8,3,10,3,12,3,84,9,3,1,4,
        1,4,1,4,1,4,1,4,3,4,91,8,4,1,5,1,5,1,5,1,5,1,5,3,5,98,8,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,112,8,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,3,7,279,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,316,8,8,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,345,8,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,4,11,363,8,
        11,11,11,12,11,364,1,11,1,11,1,11,1,11,1,11,1,11,1,11,4,11,374,8,
        11,11,11,12,11,375,1,11,1,11,3,11,380,8,11,1,11,0,3,2,4,6,12,0,2,
        4,6,8,10,12,14,16,18,20,22,0,0,433,0,26,1,0,0,0,2,28,1,0,0,0,4,54,
        1,0,0,0,6,68,1,0,0,0,8,90,1,0,0,0,10,97,1,0,0,0,12,111,1,0,0,0,14,
        278,1,0,0,0,16,315,1,0,0,0,18,344,1,0,0,0,20,346,1,0,0,0,22,379,
        1,0,0,0,24,27,3,12,6,0,25,27,3,2,1,0,26,24,1,0,0,0,26,25,1,0,0,0,
        27,1,1,0,0,0,28,29,6,1,-1,0,29,30,3,4,2,0,30,51,1,0,0,0,31,32,10,
        7,0,0,32,33,5,55,0,0,33,50,3,4,2,0,34,35,10,6,0,0,35,36,5,54,0,0,
        36,50,3,4,2,0,37,38,10,5,0,0,38,39,5,57,0,0,39,50,3,4,2,0,40,41,
        10,4,0,0,41,42,5,56,0,0,42,50,3,4,2,0,43,44,10,3,0,0,44,45,5,58,
        0,0,45,50,3,4,2,0,46,47,10,2,0,0,47,48,5,59,0,0,48,50,3,4,2,0,49,
        31,1,0,0,0,49,34,1,0,0,0,49,37,1,0,0,0,49,40,1,0,0,0,49,43,1,0,0,
        0,49,46,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,3,1,
        0,0,0,53,51,1,0,0,0,54,55,6,2,-1,0,55,56,3,6,3,0,56,65,1,0,0,0,57,
        58,10,3,0,0,58,59,5,48,0,0,59,64,3,6,3,0,60,61,10,2,0,0,61,62,5,
        49,0,0,62,64,3,6,3,0,63,57,1,0,0,0,63,60,1,0,0,0,64,67,1,0,0,0,65,
        63,1,0,0,0,65,66,1,0,0,0,66,5,1,0,0,0,67,65,1,0,0,0,68,69,6,3,-1,
        0,69,70,3,8,4,0,70,82,1,0,0,0,71,72,10,4,0,0,72,73,5,50,0,0,73,81,
        3,8,4,0,74,75,10,3,0,0,75,76,5,51,0,0,76,81,3,8,4,0,77,78,10,2,0,
        0,78,79,5,52,0,0,79,81,3,8,4,0,80,71,1,0,0,0,80,74,1,0,0,0,80,77,
        1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,7,1,0,0,0,84,
        82,1,0,0,0,85,86,3,10,5,0,86,87,5,53,0,0,87,88,3,8,4,0,88,91,1,0,
        0,0,89,91,3,10,5,0,90,85,1,0,0,0,90,89,1,0,0,0,91,9,1,0,0,0,92,93,
        5,48,0,0,93,98,3,10,5,0,94,95,5,49,0,0,95,98,3,10,5,0,96,98,3,12,
        6,0,97,92,1,0,0,0,97,94,1,0,0,0,97,96,1,0,0,0,98,11,1,0,0,0,99,112,
        3,14,7,0,100,112,3,16,8,0,101,112,3,18,9,0,102,112,3,20,10,0,103,
        112,3,22,11,0,104,112,5,62,0,0,105,112,5,61,0,0,106,112,5,60,0,0,
        107,108,5,1,0,0,108,109,3,0,0,0,109,110,5,2,0,0,110,112,1,0,0,0,
        111,99,1,0,0,0,111,100,1,0,0,0,111,101,1,0,0,0,111,102,1,0,0,0,111,
        103,1,0,0,0,111,104,1,0,0,0,111,105,1,0,0,0,111,106,1,0,0,0,111,
        107,1,0,0,0,112,13,1,0,0,0,113,114,5,4,0,0,114,115,5,1,0,0,115,116,
        3,0,0,0,116,117,5,2,0,0,117,279,1,0,0,0,118,119,5,5,0,0,119,120,
        5,1,0,0,120,121,3,0,0,0,121,122,5,2,0,0,122,279,1,0,0,0,123,124,
        5,6,0,0,124,125,5,1,0,0,125,126,3,0,0,0,126,127,5,2,0,0,127,279,
        1,0,0,0,128,129,5,7,0,0,129,130,5,1,0,0,130,131,3,0,0,0,131,132,
        5,2,0,0,132,279,1,0,0,0,133,134,5,8,0,0,134,135,5,1,0,0,135,136,
        3,0,0,0,136,137,5,2,0,0,137,279,1,0,0,0,138,139,5,9,0,0,139,140,
        5,1,0,0,140,141,3,0,0,0,141,142,5,2,0,0,142,279,1,0,0,0,143,144,
        5,11,0,0,144,145,5,1,0,0,145,146,3,0,0,0,146,147,5,2,0,0,147,279,
        1,0,0,0,148,149,5,12,0,0,149,150,5,1,0,0,150,151,3,0,0,0,151,152,
        5,2,0,0,152,279,1,0,0,0,153,154,5,13,0,0,154,155,5,1,0,0,155,156,
        3,0,0,0,156,157,5,2,0,0,157,279,1,0,0,0,158,159,5,14,0,0,159,160,
        5,1,0,0,160,161,3,0,0,0,161,162,5,2,0,0,162,279,1,0,0,0,163,164,
        5,15,0,0,164,165,5,1,0,0,165,166,3,0,0,0,166,167,5,2,0,0,167,279,
        1,0,0,0,168,169,5,16,0,0,169,170,5,1,0,0,170,171,3,0,0,0,171,172,
        5,2,0,0,172,279,1,0,0,0,173,174,5,17,0,0,174,175,5,1,0,0,175,176,
        3,0,0,0,176,177,5,2,0,0,177,279,1,0,0,0,178,179,5,18,0,0,179,180,
        5,1,0,0,180,181,3,0,0,0,181,182,5,2,0,0,182,279,1,0,0,0,183,184,
        5,19,0,0,184,185,5,1,0,0,185,186,3,0,0,0,186,187,5,2,0,0,187,279,
        1,0,0,0,188,189,5,20,0,0,189,190,5,1,0,0,190,191,3,0,0,0,191,192,
        5,2,0,0,192,279,1,0,0,0,193,194,5,21,0,0,194,195,5,1,0,0,195,196,
        3,0,0,0,196,197,5,2,0,0,197,279,1,0,0,0,198,199,5,26,0,0,199,200,
        5,1,0,0,200,201,3,0,0,0,201,202,5,2,0,0,202,279,1,0,0,0,203,204,
        5,27,0,0,204,205,5,1,0,0,205,206,3,0,0,0,206,207,5,2,0,0,207,279,
        1,0,0,0,208,209,5,28,0,0,209,210,5,1,0,0,210,211,3,0,0,0,211,212,
        5,2,0,0,212,279,1,0,0,0,213,214,5,29,0,0,214,215,5,1,0,0,215,216,
        3,0,0,0,216,217,5,2,0,0,217,279,1,0,0,0,218,219,5,30,0,0,219,220,
        5,1,0,0,220,221,3,0,0,0,221,222,5,2,0,0,222,279,1,0,0,0,223,224,
        5,31,0,0,224,225,5,1,0,0,225,226,3,0,0,0,226,227,5,2,0,0,227,279,
        1,0,0,0,228,229,5,33,0,0,229,230,5,1,0,0,230,231,3,0,0,0,231,232,
        5,2,0,0,232,279,1,0,0,0,233,234,5,35,0,0,234,235,5,1,0,0,235,236,
        3,0,0,0,236,237,5,2,0,0,237,279,1,0,0,0,238,239,5,36,0,0,239,240,
        5,1,0,0,240,241,3,0,0,0,241,242,5,2,0,0,242,279,1,0,0,0,243,244,
        5,37,0,0,244,245,5,1,0,0,245,246,3,0,0,0,246,247,5,2,0,0,247,279,
        1,0,0,0,248,249,5,38,0,0,249,250,5,1,0,0,250,251,3,0,0,0,251,252,
        5,2,0,0,252,279,1,0,0,0,253,254,5,42,0,0,254,255,5,1,0,0,255,256,
        3,0,0,0,256,257,5,2,0,0,257,279,1,0,0,0,258,259,5,43,0,0,259,260,
        5,1,0,0,260,261,3,0,0,0,261,262,5,2,0,0,262,279,1,0,0,0,263,264,
        5,44,0,0,264,265,5,1,0,0,265,266,3,0,0,0,266,267,5,2,0,0,267,279,
        1,0,0,0,268,269,5,45,0,0,269,270,5,1,0,0,270,271,3,0,0,0,271,272,
        5,2,0,0,272,279,1,0,0,0,273,274,5,46,0,0,274,275,5,1,0,0,275,276,
        3,0,0,0,276,277,5,2,0,0,277,279,1,0,0,0,278,113,1,0,0,0,278,118,
        1,0,0,0,278,123,1,0,0,0,278,128,1,0,0,0,278,133,1,0,0,0,278,138,
        1,0,0,0,278,143,1,0,0,0,278,148,1,0,0,0,278,153,1,0,0,0,278,158,
        1,0,0,0,278,163,1,0,0,0,278,168,1,0,0,0,278,173,1,0,0,0,278,178,
        1,0,0,0,278,183,1,0,0,0,278,188,1,0,0,0,278,193,1,0,0,0,278,198,
        1,0,0,0,278,203,1,0,0,0,278,208,1,0,0,0,278,213,1,0,0,0,278,218,
        1,0,0,0,278,223,1,0,0,0,278,228,1,0,0,0,278,233,1,0,0,0,278,238,
        1,0,0,0,278,243,1,0,0,0,278,248,1,0,0,0,278,253,1,0,0,0,278,258,
        1,0,0,0,278,263,1,0,0,0,278,268,1,0,0,0,278,273,1,0,0,0,279,15,1,
        0,0,0,280,281,5,32,0,0,281,282,5,1,0,0,282,283,3,0,0,0,283,284,5,
        3,0,0,284,285,3,0,0,0,285,286,5,2,0,0,286,316,1,0,0,0,287,288,5,
        10,0,0,288,289,5,1,0,0,289,290,3,0,0,0,290,291,5,3,0,0,291,292,3,
        0,0,0,292,293,5,2,0,0,293,316,1,0,0,0,294,295,5,24,0,0,295,296,5,
        1,0,0,296,297,3,0,0,0,297,298,5,3,0,0,298,299,3,0,0,0,299,300,5,
        2,0,0,300,316,1,0,0,0,301,302,5,25,0,0,302,303,5,1,0,0,303,304,3,
        0,0,0,304,305,5,3,0,0,305,306,3,0,0,0,306,307,5,2,0,0,307,316,1,
        0,0,0,308,309,5,40,0,0,309,310,5,1,0,0,310,311,3,0,0,0,311,312,5,
        3,0,0,312,313,3,0,0,0,313,314,5,2,0,0,314,316,1,0,0,0,315,280,1,
        0,0,0,315,287,1,0,0,0,315,294,1,0,0,0,315,301,1,0,0,0,315,308,1,
        0,0,0,316,17,1,0,0,0,317,318,5,34,0,0,318,319,5,1,0,0,319,320,3,
        0,0,0,320,321,5,3,0,0,321,322,3,0,0,0,322,323,5,3,0,0,323,324,3,
        0,0,0,324,325,5,2,0,0,325,345,1,0,0,0,326,327,5,39,0,0,327,328,5,
        1,0,0,328,329,3,0,0,0,329,330,5,3,0,0,330,331,3,0,0,0,331,332,5,
        3,0,0,332,333,3,0,0,0,333,334,5,2,0,0,334,345,1,0,0,0,335,336,5,
        41,0,0,336,337,5,1,0,0,337,338,3,0,0,0,338,339,5,3,0,0,339,340,3,
        0,0,0,340,341,5,3,0,0,341,342,3,0,0,0,342,343,5,2,0,0,343,345,1,
        0,0,0,344,317,1,0,0,0,344,326,1,0,0,0,344,335,1,0,0,0,345,19,1,0,
        0,0,346,347,5,47,0,0,347,348,5,1,0,0,348,349,3,0,0,0,349,350,5,3,
        0,0,350,351,3,0,0,0,351,352,5,3,0,0,352,353,3,0,0,0,353,354,5,3,
        0,0,354,355,3,0,0,0,355,356,5,2,0,0,356,21,1,0,0,0,357,358,5,22,
        0,0,358,359,5,1,0,0,359,362,3,0,0,0,360,361,5,3,0,0,361,363,3,0,
        0,0,362,360,1,0,0,0,363,364,1,0,0,0,364,362,1,0,0,0,364,365,1,0,
        0,0,365,366,1,0,0,0,366,367,5,2,0,0,367,380,1,0,0,0,368,369,5,23,
        0,0,369,370,5,1,0,0,370,373,3,0,0,0,371,372,5,3,0,0,372,374,3,0,
        0,0,373,371,1,0,0,0,374,375,1,0,0,0,375,373,1,0,0,0,375,376,1,0,
        0,0,376,377,1,0,0,0,377,378,5,2,0,0,378,380,1,0,0,0,379,357,1,0,
        0,0,379,368,1,0,0,0,380,23,1,0,0,0,16,26,49,51,63,65,80,82,90,97,
        111,278,315,344,364,375,379
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
                     "'sigm'", "'clamp'", "'fft'", "'ifft'", "'angle'", 
                     "'print'", "'lerp'", "'step'", "'smoothstep'", "'fract'", 
                     "'relu'", "'softplus'", "'gelu'", "'sign'", "'swap'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'>='", "'>'", 
                     "'<='", "'<'", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN", "ATAN2", 
                      "SINH", "COSH", "TANH", "ASINH", "ACOSH", "ATANH", 
                      "ABS", "SQRT", "LN", "LOG", "EXP", "SMIN", "SMAX", 
                      "TMIN", "TMAX", "TNORM", "SNORM", "FLOOR", "CEIL", 
                      "ROUND", "GAMMA", "POWE", "SIGM", "CLAMP", "SFFT", 
                      "SIFFT", "ANGL", "PRNT", "LERP", "STEP", "SMOOTHSTEP", 
                      "FRACT", "RELU", "SOFTPLUS", "GELU", "SIGN", "SWAP", 
                      "PLUS", "MINUS", "MULT", "DIV", "MOD", "POW", "GE", 
                      "GT", "LE", "LT", "EQ", "NE", "CONSTANT", "NUMBER", 
                      "VARIABLE", "WS" ]

    RULE_expr = 0
    RULE_compExpr = 1
    RULE_addExpr = 2
    RULE_mulExpr = 3
    RULE_powExpr = 4
    RULE_unaryExpr = 5
    RULE_atom = 6
    RULE_func1 = 7
    RULE_func2 = 8
    RULE_func3 = 9
    RULE_func4 = 10
    RULE_funcN = 11

    ruleNames =  [ "expr", "compExpr", "addExpr", "mulExpr", "powExpr", 
                   "unaryExpr", "atom", "func1", "func2", "func3", "func4", 
                   "funcN" ]

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
    SFFT=35
    SIFFT=36
    ANGL=37
    PRNT=38
    LERP=39
    STEP=40
    SMOOTHSTEP=41
    FRACT=42
    RELU=43
    SOFTPLUS=44
    GELU=45
    SIGN=46
    SWAP=47
    PLUS=48
    MINUS=49
    MULT=50
    DIV=51
    MOD=52
    POW=53
    GE=54
    GT=55
    LE=56
    LT=57
    EQ=58
    NE=59
    CONSTANT=60
    NUMBER=61
    VARIABLE=62
    WS=63

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


        def compExpr(self):
            return self.getTypedRuleContext(MathExprParser.CompExprContext,0)


        def getRuleIndex(self):
            return MathExprParser.RULE_expr

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
                self.compExpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_compExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LtExpContext(CompExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.CompExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compExpr(self):
            return self.getTypedRuleContext(MathExprParser.CompExprContext,0)

        def LT(self):
            return self.getToken(MathExprParser.LT, 0)
        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLtExp" ):
                return visitor.visitLtExp(self)
            else:
                return visitor.visitChildren(self)


    class EqExpContext(CompExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.CompExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compExpr(self):
            return self.getTypedRuleContext(MathExprParser.CompExprContext,0)

        def EQ(self):
            return self.getToken(MathExprParser.EQ, 0)
        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExp" ):
                return visitor.visitEqExp(self)
            else:
                return visitor.visitChildren(self)


    class ToAddContext(CompExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.CompExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToAdd" ):
                return visitor.visitToAdd(self)
            else:
                return visitor.visitChildren(self)


    class GeExpContext(CompExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.CompExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compExpr(self):
            return self.getTypedRuleContext(MathExprParser.CompExprContext,0)

        def GE(self):
            return self.getToken(MathExprParser.GE, 0)
        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeExp" ):
                return visitor.visitGeExp(self)
            else:
                return visitor.visitChildren(self)


    class LeExpContext(CompExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.CompExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compExpr(self):
            return self.getTypedRuleContext(MathExprParser.CompExprContext,0)

        def LE(self):
            return self.getToken(MathExprParser.LE, 0)
        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeExp" ):
                return visitor.visitLeExp(self)
            else:
                return visitor.visitChildren(self)


    class NeExpContext(CompExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.CompExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compExpr(self):
            return self.getTypedRuleContext(MathExprParser.CompExprContext,0)

        def NE(self):
            return self.getToken(MathExprParser.NE, 0)
        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeExp" ):
                return visitor.visitNeExp(self)
            else:
                return visitor.visitChildren(self)


    class GtExpContext(CompExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.CompExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compExpr(self):
            return self.getTypedRuleContext(MathExprParser.CompExprContext,0)

        def GT(self):
            return self.getToken(MathExprParser.GT, 0)
        def addExpr(self):
            return self.getTypedRuleContext(MathExprParser.AddExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGtExp" ):
                return visitor.visitGtExp(self)
            else:
                return visitor.visitChildren(self)



    def compExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathExprParser.CompExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_compExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToAddContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 29
            self.addExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 49
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.GtExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 31
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 32
                        self.match(MathExprParser.GT)
                        self.state = 33
                        self.addExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.GeExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 34
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 35
                        self.match(MathExprParser.GE)
                        self.state = 36
                        self.addExpr(0)
                        pass

                    elif la_ == 3:
                        localctx = MathExprParser.LtExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 37
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 38
                        self.match(MathExprParser.LT)
                        self.state = 39
                        self.addExpr(0)
                        pass

                    elif la_ == 4:
                        localctx = MathExprParser.LeExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 40
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 41
                        self.match(MathExprParser.LE)
                        self.state = 42
                        self.addExpr(0)
                        pass

                    elif la_ == 5:
                        localctx = MathExprParser.EqExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 43
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 44
                        self.match(MathExprParser.EQ)
                        self.state = 45
                        self.addExpr(0)
                        pass

                    elif la_ == 6:
                        localctx = MathExprParser.NeExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 46
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 47
                        self.match(MathExprParser.NE)
                        self.state = 48
                        self.addExpr(0)
                        pass

             
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_addExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToMulContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 55
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 63
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.AddExpContext(self, MathExprParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 57
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 58
                        self.match(MathExprParser.PLUS)
                        self.state = 59
                        self.mulExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.SubExpContext(self, MathExprParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 60
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 61
                        self.match(MathExprParser.MINUS)
                        self.state = 62
                        self.mulExpr(0)
                        pass

             
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_mulExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToPowContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 69
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.MulExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 71
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 72
                        self.match(MathExprParser.MULT)
                        self.state = 73
                        self.powExpr()
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.DivExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 74
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 75
                        self.match(MathExprParser.DIV)
                        self.state = 76
                        self.powExpr()
                        pass

                    elif la_ == 3:
                        localctx = MathExprParser.ModExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 77
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 78
                        self.match(MathExprParser.MOD)
                        self.state = 79
                        self.powExpr()
                        pass

             
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToUnary" ):
                return visitor.visitToUnary(self)
            else:
                return visitor.visitChildren(self)



    def powExpr(self):

        localctx = MathExprParser.PowExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_powExpr)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = MathExprParser.PowExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.unaryExpr()
                self.state = 86
                self.match(MathExprParser.POW)
                self.state = 87
                self.powExpr()
                pass

            elif la_ == 2:
                localctx = MathExprParser.ToUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToAtom" ):
                return visitor.visitToAtom(self)
            else:
                return visitor.visitChildren(self)



    def unaryExpr(self):

        localctx = MathExprParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unaryExpr)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                localctx = MathExprParser.UnaryPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(MathExprParser.PLUS)
                self.state = 93
                self.unaryExpr()
                pass
            elif token in [49]:
                localctx = MathExprParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(MathExprParser.MINUS)
                self.state = 95
                self.unaryExpr()
                pass
            elif token in [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 60, 61, 62]:
                localctx = MathExprParser.ToAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 96
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



    class Func4ExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func4(self):
            return self.getTypedRuleContext(MathExprParser.Func4Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc4Exp" ):
                return visitor.visitFunc4Exp(self)
            else:
                return visitor.visitChildren(self)


    class Func2ExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func2(self):
            return self.getTypedRuleContext(MathExprParser.Func2Context,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExp" ):
                return visitor.visitNumberExp(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = MathExprParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 26, 27, 28, 29, 30, 31, 33, 35, 36, 37, 38, 42, 43, 44, 45, 46]:
                localctx = MathExprParser.Func1ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.func1()
                pass
            elif token in [10, 24, 25, 32, 40]:
                localctx = MathExprParser.Func2ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.func2()
                pass
            elif token in [34, 39, 41]:
                localctx = MathExprParser.Func3ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.func3()
                pass
            elif token in [47]:
                localctx = MathExprParser.Func4ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.func4()
                pass
            elif token in [22, 23]:
                localctx = MathExprParser.FuncNExpContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 103
                self.funcN()
                pass
            elif token in [62]:
                localctx = MathExprParser.VariableExpContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 104
                self.match(MathExprParser.VARIABLE)
                pass
            elif token in [61]:
                localctx = MathExprParser.NumberExpContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 105
                self.match(MathExprParser.NUMBER)
                pass
            elif token in [60]:
                localctx = MathExprParser.ConstantExpContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 106
                self.match(MathExprParser.CONSTANT)
                pass
            elif token in [1]:
                localctx = MathExprParser.ParenExpContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 107
                self.match(MathExprParser.T__0)
                self.state = 108
                self.expr()
                self.state = 109
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



    class SoftplusFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SOFTPLUS(self):
            return self.getToken(MathExprParser.SOFTPLUS, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoftplusFunc" ):
                return visitor.visitSoftplusFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcoshFunc" ):
                return visitor.visitAcoshFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCeilFunc" ):
                return visitor.visitCeilFunc(self)
            else:
                return visitor.visitChildren(self)


    class GeluFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def GELU(self):
            return self.getToken(MathExprParser.GELU, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeluFunc" ):
                return visitor.visitGeluFunc(self)
            else:
                return visitor.visitChildren(self)


    class PrintFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRNT(self):
            return self.getToken(MathExprParser.PRNT, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintFunc" ):
                return visitor.visitPrintFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtanFunc" ):
                return visitor.visitAtanFunc(self)
            else:
                return visitor.visitChildren(self)


    class ReluFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def RELU(self):
            return self.getToken(MathExprParser.RELU, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReluFunc" ):
                return visitor.visitReluFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogFunc" ):
                return visitor.visitLogFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinFunc" ):
                return visitor.visitSinFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoshFunc" ):
                return visitor.visitCoshFunc(self)
            else:
                return visitor.visitChildren(self)


    class AnglFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ANGL(self):
            return self.getToken(MathExprParser.ANGL, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnglFunc" ):
                return visitor.visitAnglFunc(self)
            else:
                return visitor.visitChildren(self)


    class SignFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIGN(self):
            return self.getToken(MathExprParser.SIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignFunc" ):
                return visitor.visitSignFunc(self)
            else:
                return visitor.visitChildren(self)


    class TanFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(MathExprParser.TAN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanFunc" ):
                return visitor.visitTanFunc(self)
            else:
                return visitor.visitChildren(self)


    class SifftFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIFFT(self):
            return self.getToken(MathExprParser.SIFFT, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSifftFunc" ):
                return visitor.visitSifftFunc(self)
            else:
                return visitor.visitChildren(self)


    class FractFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def FRACT(self):
            return self.getToken(MathExprParser.FRACT, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFractFunc" ):
                return visitor.visitFractFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosFunc" ):
                return visitor.visitCosFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsinhFunc" ):
                return visitor.visitAsinhFunc(self)
            else:
                return visitor.visitChildren(self)


    class SfftFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SFFT(self):
            return self.getToken(MathExprParser.SFFT, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSfftFunc" ):
                return visitor.visitSfftFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtanhFunc" ):
                return visitor.visitAtanhFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpFunc" ):
                return visitor.visitExpFunc(self)
            else:
                return visitor.visitChildren(self)



    def func1(self):

        localctx = MathExprParser.Func1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func1)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = MathExprParser.SinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(MathExprParser.SIN)
                self.state = 114
                self.match(MathExprParser.T__0)
                self.state = 115
                self.expr()
                self.state = 116
                self.match(MathExprParser.T__1)
                pass
            elif token in [5]:
                localctx = MathExprParser.CosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(MathExprParser.COS)
                self.state = 119
                self.match(MathExprParser.T__0)
                self.state = 120
                self.expr()
                self.state = 121
                self.match(MathExprParser.T__1)
                pass
            elif token in [6]:
                localctx = MathExprParser.TanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(MathExprParser.TAN)
                self.state = 124
                self.match(MathExprParser.T__0)
                self.state = 125
                self.expr()
                self.state = 126
                self.match(MathExprParser.T__1)
                pass
            elif token in [7]:
                localctx = MathExprParser.AsinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.match(MathExprParser.ASIN)
                self.state = 129
                self.match(MathExprParser.T__0)
                self.state = 130
                self.expr()
                self.state = 131
                self.match(MathExprParser.T__1)
                pass
            elif token in [8]:
                localctx = MathExprParser.AcosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.match(MathExprParser.ACOS)
                self.state = 134
                self.match(MathExprParser.T__0)
                self.state = 135
                self.expr()
                self.state = 136
                self.match(MathExprParser.T__1)
                pass
            elif token in [9]:
                localctx = MathExprParser.AtanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.match(MathExprParser.ATAN)
                self.state = 139
                self.match(MathExprParser.T__0)
                self.state = 140
                self.expr()
                self.state = 141
                self.match(MathExprParser.T__1)
                pass
            elif token in [11]:
                localctx = MathExprParser.SinhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 143
                self.match(MathExprParser.SINH)
                self.state = 144
                self.match(MathExprParser.T__0)
                self.state = 145
                self.expr()
                self.state = 146
                self.match(MathExprParser.T__1)
                pass
            elif token in [12]:
                localctx = MathExprParser.CoshFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 148
                self.match(MathExprParser.COSH)
                self.state = 149
                self.match(MathExprParser.T__0)
                self.state = 150
                self.expr()
                self.state = 151
                self.match(MathExprParser.T__1)
                pass
            elif token in [13]:
                localctx = MathExprParser.TanhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 153
                self.match(MathExprParser.TANH)
                self.state = 154
                self.match(MathExprParser.T__0)
                self.state = 155
                self.expr()
                self.state = 156
                self.match(MathExprParser.T__1)
                pass
            elif token in [14]:
                localctx = MathExprParser.AsinhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 158
                self.match(MathExprParser.ASINH)
                self.state = 159
                self.match(MathExprParser.T__0)
                self.state = 160
                self.expr()
                self.state = 161
                self.match(MathExprParser.T__1)
                pass
            elif token in [15]:
                localctx = MathExprParser.AcoshFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 163
                self.match(MathExprParser.ACOSH)
                self.state = 164
                self.match(MathExprParser.T__0)
                self.state = 165
                self.expr()
                self.state = 166
                self.match(MathExprParser.T__1)
                pass
            elif token in [16]:
                localctx = MathExprParser.AtanhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 168
                self.match(MathExprParser.ATANH)
                self.state = 169
                self.match(MathExprParser.T__0)
                self.state = 170
                self.expr()
                self.state = 171
                self.match(MathExprParser.T__1)
                pass
            elif token in [17]:
                localctx = MathExprParser.AbsFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 173
                self.match(MathExprParser.ABS)
                self.state = 174
                self.match(MathExprParser.T__0)
                self.state = 175
                self.expr()
                self.state = 176
                self.match(MathExprParser.T__1)
                pass
            elif token in [18]:
                localctx = MathExprParser.SqrtFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 178
                self.match(MathExprParser.SQRT)
                self.state = 179
                self.match(MathExprParser.T__0)
                self.state = 180
                self.expr()
                self.state = 181
                self.match(MathExprParser.T__1)
                pass
            elif token in [19]:
                localctx = MathExprParser.LnFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 183
                self.match(MathExprParser.LN)
                self.state = 184
                self.match(MathExprParser.T__0)
                self.state = 185
                self.expr()
                self.state = 186
                self.match(MathExprParser.T__1)
                pass
            elif token in [20]:
                localctx = MathExprParser.LogFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 188
                self.match(MathExprParser.LOG)
                self.state = 189
                self.match(MathExprParser.T__0)
                self.state = 190
                self.expr()
                self.state = 191
                self.match(MathExprParser.T__1)
                pass
            elif token in [21]:
                localctx = MathExprParser.ExpFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 193
                self.match(MathExprParser.EXP)
                self.state = 194
                self.match(MathExprParser.T__0)
                self.state = 195
                self.expr()
                self.state = 196
                self.match(MathExprParser.T__1)
                pass
            elif token in [26]:
                localctx = MathExprParser.TNormFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 198
                self.match(MathExprParser.TNORM)
                self.state = 199
                self.match(MathExprParser.T__0)
                self.state = 200
                self.expr()
                self.state = 201
                self.match(MathExprParser.T__1)
                pass
            elif token in [27]:
                localctx = MathExprParser.SNormFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 203
                self.match(MathExprParser.SNORM)
                self.state = 204
                self.match(MathExprParser.T__0)
                self.state = 205
                self.expr()
                self.state = 206
                self.match(MathExprParser.T__1)
                pass
            elif token in [28]:
                localctx = MathExprParser.FloorFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 20)
                self.state = 208
                self.match(MathExprParser.FLOOR)
                self.state = 209
                self.match(MathExprParser.T__0)
                self.state = 210
                self.expr()
                self.state = 211
                self.match(MathExprParser.T__1)
                pass
            elif token in [29]:
                localctx = MathExprParser.CeilFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 21)
                self.state = 213
                self.match(MathExprParser.CEIL)
                self.state = 214
                self.match(MathExprParser.T__0)
                self.state = 215
                self.expr()
                self.state = 216
                self.match(MathExprParser.T__1)
                pass
            elif token in [30]:
                localctx = MathExprParser.RoundFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 22)
                self.state = 218
                self.match(MathExprParser.ROUND)
                self.state = 219
                self.match(MathExprParser.T__0)
                self.state = 220
                self.expr()
                self.state = 221
                self.match(MathExprParser.T__1)
                pass
            elif token in [31]:
                localctx = MathExprParser.GammaFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 23)
                self.state = 223
                self.match(MathExprParser.GAMMA)
                self.state = 224
                self.match(MathExprParser.T__0)
                self.state = 225
                self.expr()
                self.state = 226
                self.match(MathExprParser.T__1)
                pass
            elif token in [33]:
                localctx = MathExprParser.SigmoidFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 24)
                self.state = 228
                self.match(MathExprParser.SIGM)
                self.state = 229
                self.match(MathExprParser.T__0)
                self.state = 230
                self.expr()
                self.state = 231
                self.match(MathExprParser.T__1)
                pass
            elif token in [35]:
                localctx = MathExprParser.SfftFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 25)
                self.state = 233
                self.match(MathExprParser.SFFT)
                self.state = 234
                self.match(MathExprParser.T__0)
                self.state = 235
                self.expr()
                self.state = 236
                self.match(MathExprParser.T__1)
                pass
            elif token in [36]:
                localctx = MathExprParser.SifftFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 26)
                self.state = 238
                self.match(MathExprParser.SIFFT)
                self.state = 239
                self.match(MathExprParser.T__0)
                self.state = 240
                self.expr()
                self.state = 241
                self.match(MathExprParser.T__1)
                pass
            elif token in [37]:
                localctx = MathExprParser.AnglFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 27)
                self.state = 243
                self.match(MathExprParser.ANGL)
                self.state = 244
                self.match(MathExprParser.T__0)
                self.state = 245
                self.expr()
                self.state = 246
                self.match(MathExprParser.T__1)
                pass
            elif token in [38]:
                localctx = MathExprParser.PrintFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 28)
                self.state = 248
                self.match(MathExprParser.PRNT)
                self.state = 249
                self.match(MathExprParser.T__0)
                self.state = 250
                self.expr()
                self.state = 251
                self.match(MathExprParser.T__1)
                pass
            elif token in [42]:
                localctx = MathExprParser.FractFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 29)
                self.state = 253
                self.match(MathExprParser.FRACT)
                self.state = 254
                self.match(MathExprParser.T__0)
                self.state = 255
                self.expr()
                self.state = 256
                self.match(MathExprParser.T__1)
                pass
            elif token in [43]:
                localctx = MathExprParser.ReluFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 30)
                self.state = 258
                self.match(MathExprParser.RELU)
                self.state = 259
                self.match(MathExprParser.T__0)
                self.state = 260
                self.expr()
                self.state = 261
                self.match(MathExprParser.T__1)
                pass
            elif token in [44]:
                localctx = MathExprParser.SoftplusFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 31)
                self.state = 263
                self.match(MathExprParser.SOFTPLUS)
                self.state = 264
                self.match(MathExprParser.T__0)
                self.state = 265
                self.expr()
                self.state = 266
                self.match(MathExprParser.T__1)
                pass
            elif token in [45]:
                localctx = MathExprParser.GeluFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 32)
                self.state = 268
                self.match(MathExprParser.GELU)
                self.state = 269
                self.match(MathExprParser.T__0)
                self.state = 270
                self.expr()
                self.state = 271
                self.match(MathExprParser.T__1)
                pass
            elif token in [46]:
                localctx = MathExprParser.SignFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 33)
                self.state = 273
                self.match(MathExprParser.SIGN)
                self.state = 274
                self.match(MathExprParser.T__0)
                self.state = 275
                self.expr()
                self.state = 276
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowFunc" ):
                return visitor.visitPowFunc(self)
            else:
                return visitor.visitChildren(self)


    class StepFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def STEP(self):
            return self.getToken(MathExprParser.STEP, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStepFunc" ):
                return visitor.visitStepFunc(self)
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTMinFunc" ):
                return visitor.visitTMinFunc(self)
            else:
                return visitor.visitChildren(self)



    def func2(self):

        localctx = MathExprParser.Func2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func2)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                localctx = MathExprParser.PowFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(MathExprParser.POWE)
                self.state = 281
                self.match(MathExprParser.T__0)
                self.state = 282
                self.expr()
                self.state = 283
                self.match(MathExprParser.T__2)
                self.state = 284
                self.expr()
                self.state = 285
                self.match(MathExprParser.T__1)
                pass
            elif token in [10]:
                localctx = MathExprParser.Atan2FuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(MathExprParser.ATAN2)
                self.state = 288
                self.match(MathExprParser.T__0)
                self.state = 289
                self.expr()
                self.state = 290
                self.match(MathExprParser.T__2)
                self.state = 291
                self.expr()
                self.state = 292
                self.match(MathExprParser.T__1)
                pass
            elif token in [24]:
                localctx = MathExprParser.TMinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.match(MathExprParser.TMIN)
                self.state = 295
                self.match(MathExprParser.T__0)
                self.state = 296
                self.expr()
                self.state = 297
                self.match(MathExprParser.T__2)
                self.state = 298
                self.expr()
                self.state = 299
                self.match(MathExprParser.T__1)
                pass
            elif token in [25]:
                localctx = MathExprParser.TMaxFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 301
                self.match(MathExprParser.TMAX)
                self.state = 302
                self.match(MathExprParser.T__0)
                self.state = 303
                self.expr()
                self.state = 304
                self.match(MathExprParser.T__2)
                self.state = 305
                self.expr()
                self.state = 306
                self.match(MathExprParser.T__1)
                pass
            elif token in [40]:
                localctx = MathExprParser.StepFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 308
                self.match(MathExprParser.STEP)
                self.state = 309
                self.match(MathExprParser.T__0)
                self.state = 310
                self.expr()
                self.state = 311
                self.match(MathExprParser.T__2)
                self.state = 312
                self.expr()
                self.state = 313
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



    class LerpFuncContext(Func3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def LERP(self):
            return self.getToken(MathExprParser.LERP, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLerpFunc" ):
                return visitor.visitLerpFunc(self)
            else:
                return visitor.visitChildren(self)


    class SmoothstepFuncContext(Func3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SMOOTHSTEP(self):
            return self.getToken(MathExprParser.SMOOTHSTEP, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmoothstepFunc" ):
                return visitor.visitSmoothstepFunc(self)
            else:
                return visitor.visitChildren(self)


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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClampFunc" ):
                return visitor.visitClampFunc(self)
            else:
                return visitor.visitChildren(self)



    def func3(self):

        localctx = MathExprParser.Func3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func3)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                localctx = MathExprParser.ClampFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(MathExprParser.CLAMP)
                self.state = 318
                self.match(MathExprParser.T__0)
                self.state = 319
                self.expr()
                self.state = 320
                self.match(MathExprParser.T__2)
                self.state = 321
                self.expr()
                self.state = 322
                self.match(MathExprParser.T__2)
                self.state = 323
                self.expr()
                self.state = 324
                self.match(MathExprParser.T__1)
                pass
            elif token in [39]:
                localctx = MathExprParser.LerpFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.match(MathExprParser.LERP)
                self.state = 327
                self.match(MathExprParser.T__0)
                self.state = 328
                self.expr()
                self.state = 329
                self.match(MathExprParser.T__2)
                self.state = 330
                self.expr()
                self.state = 331
                self.match(MathExprParser.T__2)
                self.state = 332
                self.expr()
                self.state = 333
                self.match(MathExprParser.T__1)
                pass
            elif token in [41]:
                localctx = MathExprParser.SmoothstepFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.match(MathExprParser.SMOOTHSTEP)
                self.state = 336
                self.match(MathExprParser.T__0)
                self.state = 337
                self.expr()
                self.state = 338
                self.match(MathExprParser.T__2)
                self.state = 339
                self.expr()
                self.state = 340
                self.match(MathExprParser.T__2)
                self.state = 341
                self.expr()
                self.state = 342
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


    class Func4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_func4

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SwapFuncContext(Func4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SWAP(self):
            return self.getToken(MathExprParser.SWAP, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwapFunc" ):
                return visitor.visitSwapFunc(self)
            else:
                return visitor.visitChildren(self)



    def func4(self):

        localctx = MathExprParser.Func4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func4)
        try:
            localctx = MathExprParser.SwapFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(MathExprParser.SWAP)
            self.state = 347
            self.match(MathExprParser.T__0)
            self.state = 348
            self.expr()
            self.state = 349
            self.match(MathExprParser.T__2)
            self.state = 350
            self.expr()
            self.state = 351
            self.match(MathExprParser.T__2)
            self.state = 352
            self.expr()
            self.state = 353
            self.match(MathExprParser.T__2)
            self.state = 354
            self.expr()
            self.state = 355
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


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSMinFunc" ):
                return visitor.visitSMinFunc(self)
            else:
                return visitor.visitChildren(self)



    def funcN(self):

        localctx = MathExprParser.FuncNContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcN)
        self._la = 0 # Token type
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = MathExprParser.SMinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(MathExprParser.SMIN)
                self.state = 358
                self.match(MathExprParser.T__0)
                self.state = 359
                self.expr()
                self.state = 362 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 360
                    self.match(MathExprParser.T__2)
                    self.state = 361
                    self.expr()
                    self.state = 364 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                self.state = 366
                self.match(MathExprParser.T__1)
                pass
            elif token in [23]:
                localctx = MathExprParser.SMaxFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.match(MathExprParser.SMAX)
                self.state = 369
                self.match(MathExprParser.T__0)
                self.state = 370
                self.expr()
                self.state = 373 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 371
                    self.match(MathExprParser.T__2)
                    self.state = 372
                    self.expr()
                    self.state = 375 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==3):
                        break

                self.state = 377
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
        self._predicates[1] = self.compExpr_sempred
        self._predicates[2] = self.addExpr_sempred
        self._predicates[3] = self.mulExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def compExpr_sempred(self, localctx:CompExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def addExpr_sempred(self, localctx:AddExprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def mulExpr_sempred(self, localctx:MulExprContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




