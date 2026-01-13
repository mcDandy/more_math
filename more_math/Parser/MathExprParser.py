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
        4,1,85,558,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        3,0,29,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,12,1,55,9,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,66,8,2,10,2,12,2,69,9,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,83,8,3,10,3,12,3,86,
        9,3,1,4,1,4,1,4,1,4,1,4,3,4,93,8,4,1,5,1,5,1,5,1,5,1,5,3,5,100,8,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,110,8,6,10,6,12,6,113,9,6,
        1,6,1,6,5,6,117,8,6,10,6,12,6,120,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,142,8,
        7,10,7,12,7,145,9,7,1,7,1,7,3,7,149,8,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,346,8,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,425,8,9,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,472,8,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,5,12,
        490,8,12,10,12,12,12,493,9,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        5,12,502,8,12,10,12,12,12,505,9,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,4,12,514,8,12,11,12,12,12,515,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,4,12,525,8,12,11,12,12,12,526,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,4,12,536,8,12,11,12,12,12,537,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,556,8,12,
        1,12,0,4,2,4,6,12,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,635,0,
        28,1,0,0,0,2,30,1,0,0,0,4,56,1,0,0,0,6,70,1,0,0,0,8,92,1,0,0,0,10,
        99,1,0,0,0,12,101,1,0,0,0,14,148,1,0,0,0,16,345,1,0,0,0,18,424,1,
        0,0,0,20,471,1,0,0,0,22,473,1,0,0,0,24,555,1,0,0,0,26,29,3,14,7,
        0,27,29,3,2,1,0,28,26,1,0,0,0,28,27,1,0,0,0,29,1,1,0,0,0,30,31,6,
        1,-1,0,31,32,3,4,2,0,32,53,1,0,0,0,33,34,10,7,0,0,34,35,5,71,0,0,
        35,52,3,4,2,0,36,37,10,6,0,0,37,38,5,70,0,0,38,52,3,4,2,0,39,40,
        10,5,0,0,40,41,5,73,0,0,41,52,3,4,2,0,42,43,10,4,0,0,43,44,5,72,
        0,0,44,52,3,4,2,0,45,46,10,3,0,0,46,47,5,74,0,0,47,52,3,4,2,0,48,
        49,10,2,0,0,49,50,5,75,0,0,50,52,3,4,2,0,51,33,1,0,0,0,51,36,1,0,
        0,0,51,39,1,0,0,0,51,42,1,0,0,0,51,45,1,0,0,0,51,48,1,0,0,0,52,55,
        1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,3,1,0,0,0,55,53,1,0,0,0,56,
        57,6,2,-1,0,57,58,3,6,3,0,58,67,1,0,0,0,59,60,10,3,0,0,60,61,5,64,
        0,0,61,66,3,6,3,0,62,63,10,2,0,0,63,64,5,65,0,0,64,66,3,6,3,0,65,
        59,1,0,0,0,65,62,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,
        0,68,5,1,0,0,0,69,67,1,0,0,0,70,71,6,3,-1,0,71,72,3,8,4,0,72,84,
        1,0,0,0,73,74,10,4,0,0,74,75,5,66,0,0,75,83,3,8,4,0,76,77,10,3,0,
        0,77,78,5,67,0,0,78,83,3,8,4,0,79,80,10,2,0,0,80,81,5,68,0,0,81,
        83,3,8,4,0,82,73,1,0,0,0,82,76,1,0,0,0,82,79,1,0,0,0,83,86,1,0,0,
        0,84,82,1,0,0,0,84,85,1,0,0,0,85,7,1,0,0,0,86,84,1,0,0,0,87,88,3,
        10,5,0,88,89,5,69,0,0,89,90,3,8,4,0,90,93,1,0,0,0,91,93,3,10,5,0,
        92,87,1,0,0,0,92,91,1,0,0,0,93,9,1,0,0,0,94,95,5,64,0,0,95,100,3,
        10,5,0,96,97,5,65,0,0,97,100,3,10,5,0,98,100,3,12,6,0,99,94,1,0,
        0,0,99,96,1,0,0,0,99,98,1,0,0,0,100,11,1,0,0,0,101,102,6,6,-1,0,
        102,103,3,14,7,0,103,118,1,0,0,0,104,105,10,2,0,0,105,106,5,80,0,
        0,106,111,3,0,0,0,107,108,5,79,0,0,108,110,3,0,0,0,109,107,1,0,0,
        0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,
        0,113,111,1,0,0,0,114,115,5,81,0,0,115,117,1,0,0,0,116,104,1,0,0,
        0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,13,1,0,0,0,
        120,118,1,0,0,0,121,149,3,16,8,0,122,149,3,18,9,0,123,149,3,20,10,
        0,124,149,3,22,11,0,125,149,3,24,12,0,126,149,5,84,0,0,127,149,5,
        83,0,0,128,149,5,82,0,0,129,130,5,77,0,0,130,131,3,0,0,0,131,132,
        5,78,0,0,132,149,1,0,0,0,133,134,5,76,0,0,134,135,3,0,0,0,135,136,
        5,76,0,0,136,149,1,0,0,0,137,138,5,80,0,0,138,143,3,0,0,0,139,140,
        5,79,0,0,140,142,3,0,0,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,
        1,0,0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,147,
        5,81,0,0,147,149,1,0,0,0,148,121,1,0,0,0,148,122,1,0,0,0,148,123,
        1,0,0,0,148,124,1,0,0,0,148,125,1,0,0,0,148,126,1,0,0,0,148,127,
        1,0,0,0,148,128,1,0,0,0,148,129,1,0,0,0,148,133,1,0,0,0,148,137,
        1,0,0,0,149,15,1,0,0,0,150,151,5,1,0,0,151,152,5,77,0,0,152,153,
        3,0,0,0,153,154,5,78,0,0,154,346,1,0,0,0,155,156,5,2,0,0,156,157,
        5,77,0,0,157,158,3,0,0,0,158,159,5,78,0,0,159,346,1,0,0,0,160,161,
        5,3,0,0,161,162,5,77,0,0,162,163,3,0,0,0,163,164,5,78,0,0,164,346,
        1,0,0,0,165,166,5,4,0,0,166,167,5,77,0,0,167,168,3,0,0,0,168,169,
        5,78,0,0,169,346,1,0,0,0,170,171,5,5,0,0,171,172,5,77,0,0,172,173,
        3,0,0,0,173,174,5,78,0,0,174,346,1,0,0,0,175,176,5,6,0,0,176,177,
        5,77,0,0,177,178,3,0,0,0,178,179,5,78,0,0,179,346,1,0,0,0,180,181,
        5,8,0,0,181,182,5,77,0,0,182,183,3,0,0,0,183,184,5,78,0,0,184,346,
        1,0,0,0,185,186,5,9,0,0,186,187,5,77,0,0,187,188,3,0,0,0,188,189,
        5,78,0,0,189,346,1,0,0,0,190,191,5,10,0,0,191,192,5,77,0,0,192,193,
        3,0,0,0,193,194,5,78,0,0,194,346,1,0,0,0,195,196,5,11,0,0,196,197,
        5,77,0,0,197,198,3,0,0,0,198,199,5,78,0,0,199,346,1,0,0,0,200,201,
        5,12,0,0,201,202,5,77,0,0,202,203,3,0,0,0,203,204,5,78,0,0,204,346,
        1,0,0,0,205,206,5,13,0,0,206,207,5,77,0,0,207,208,3,0,0,0,208,209,
        5,78,0,0,209,346,1,0,0,0,210,211,5,14,0,0,211,212,5,77,0,0,212,213,
        3,0,0,0,213,214,5,78,0,0,214,346,1,0,0,0,215,216,5,15,0,0,216,217,
        5,77,0,0,217,218,3,0,0,0,218,219,5,78,0,0,219,346,1,0,0,0,220,221,
        5,16,0,0,221,222,5,77,0,0,222,223,3,0,0,0,223,224,5,78,0,0,224,346,
        1,0,0,0,225,226,5,17,0,0,226,227,5,77,0,0,227,228,3,0,0,0,228,229,
        5,78,0,0,229,346,1,0,0,0,230,231,5,18,0,0,231,232,5,77,0,0,232,233,
        3,0,0,0,233,234,5,78,0,0,234,346,1,0,0,0,235,236,5,23,0,0,236,237,
        5,77,0,0,237,238,3,0,0,0,238,239,5,78,0,0,239,346,1,0,0,0,240,241,
        5,24,0,0,241,242,5,77,0,0,242,243,3,0,0,0,243,244,5,78,0,0,244,346,
        1,0,0,0,245,246,5,25,0,0,246,247,5,77,0,0,247,248,3,0,0,0,248,249,
        5,78,0,0,249,346,1,0,0,0,250,251,5,26,0,0,251,252,5,77,0,0,252,253,
        3,0,0,0,253,254,5,78,0,0,254,346,1,0,0,0,255,256,5,27,0,0,256,257,
        5,77,0,0,257,258,3,0,0,0,258,259,5,78,0,0,259,346,1,0,0,0,260,261,
        5,28,0,0,261,262,5,77,0,0,262,263,3,0,0,0,263,264,5,78,0,0,264,346,
        1,0,0,0,265,266,5,30,0,0,266,267,5,77,0,0,267,268,3,0,0,0,268,269,
        5,78,0,0,269,346,1,0,0,0,270,271,5,32,0,0,271,272,5,77,0,0,272,273,
        3,0,0,0,273,274,5,78,0,0,274,346,1,0,0,0,275,276,5,33,0,0,276,277,
        5,77,0,0,277,278,3,0,0,0,278,279,5,78,0,0,279,346,1,0,0,0,280,281,
        5,34,0,0,281,282,5,77,0,0,282,283,3,0,0,0,283,284,5,78,0,0,284,346,
        1,0,0,0,285,286,5,35,0,0,286,287,5,77,0,0,287,288,3,0,0,0,288,289,
        5,78,0,0,289,346,1,0,0,0,290,291,5,40,0,0,291,292,5,77,0,0,292,293,
        3,0,0,0,293,294,5,78,0,0,294,346,1,0,0,0,295,296,5,41,0,0,296,297,
        5,77,0,0,297,298,3,0,0,0,298,299,5,78,0,0,299,346,1,0,0,0,300,301,
        5,42,0,0,301,302,5,77,0,0,302,303,3,0,0,0,303,304,5,78,0,0,304,346,
        1,0,0,0,305,306,5,43,0,0,306,307,5,77,0,0,307,308,3,0,0,0,308,309,
        5,78,0,0,309,346,1,0,0,0,310,311,5,44,0,0,311,312,5,77,0,0,312,313,
        3,0,0,0,313,314,5,78,0,0,314,346,1,0,0,0,315,316,5,36,0,0,316,317,
        5,77,0,0,317,318,3,0,0,0,318,319,5,78,0,0,319,346,1,0,0,0,320,321,
        5,54,0,0,321,322,5,77,0,0,322,323,3,0,0,0,323,324,5,78,0,0,324,346,
        1,0,0,0,325,326,5,55,0,0,326,327,5,77,0,0,327,328,3,0,0,0,328,329,
        5,78,0,0,329,346,1,0,0,0,330,331,5,56,0,0,331,332,5,77,0,0,332,333,
        3,0,0,0,333,334,5,78,0,0,334,346,1,0,0,0,335,336,5,57,0,0,336,337,
        5,77,0,0,337,338,3,0,0,0,338,339,5,78,0,0,339,346,1,0,0,0,340,341,
        5,58,0,0,341,342,5,77,0,0,342,343,3,0,0,0,343,344,5,78,0,0,344,346,
        1,0,0,0,345,150,1,0,0,0,345,155,1,0,0,0,345,160,1,0,0,0,345,165,
        1,0,0,0,345,170,1,0,0,0,345,175,1,0,0,0,345,180,1,0,0,0,345,185,
        1,0,0,0,345,190,1,0,0,0,345,195,1,0,0,0,345,200,1,0,0,0,345,205,
        1,0,0,0,345,210,1,0,0,0,345,215,1,0,0,0,345,220,1,0,0,0,345,225,
        1,0,0,0,345,230,1,0,0,0,345,235,1,0,0,0,345,240,1,0,0,0,345,245,
        1,0,0,0,345,250,1,0,0,0,345,255,1,0,0,0,345,260,1,0,0,0,345,265,
        1,0,0,0,345,270,1,0,0,0,345,275,1,0,0,0,345,280,1,0,0,0,345,285,
        1,0,0,0,345,290,1,0,0,0,345,295,1,0,0,0,345,300,1,0,0,0,345,305,
        1,0,0,0,345,310,1,0,0,0,345,315,1,0,0,0,345,320,1,0,0,0,345,325,
        1,0,0,0,345,330,1,0,0,0,345,335,1,0,0,0,345,340,1,0,0,0,346,17,1,
        0,0,0,347,348,5,29,0,0,348,349,5,77,0,0,349,350,3,0,0,0,350,351,
        5,79,0,0,351,352,3,0,0,0,352,353,5,78,0,0,353,425,1,0,0,0,354,355,
        5,7,0,0,355,356,5,77,0,0,356,357,3,0,0,0,357,358,5,79,0,0,358,359,
        3,0,0,0,359,360,5,78,0,0,360,425,1,0,0,0,361,362,5,21,0,0,362,363,
        5,77,0,0,363,364,3,0,0,0,364,365,5,79,0,0,365,366,3,0,0,0,366,367,
        5,78,0,0,367,425,1,0,0,0,368,369,5,22,0,0,369,370,5,77,0,0,370,371,
        3,0,0,0,371,372,5,79,0,0,372,373,3,0,0,0,373,374,5,78,0,0,374,425,
        1,0,0,0,375,376,5,38,0,0,376,377,5,77,0,0,377,378,3,0,0,0,378,379,
        5,79,0,0,379,380,3,0,0,0,380,381,5,78,0,0,381,425,1,0,0,0,382,383,
        5,52,0,0,383,384,5,77,0,0,384,385,3,0,0,0,385,386,5,79,0,0,386,387,
        3,0,0,0,387,388,5,78,0,0,388,425,1,0,0,0,389,390,5,53,0,0,390,391,
        5,77,0,0,391,392,3,0,0,0,392,393,5,79,0,0,393,394,3,0,0,0,394,395,
        5,78,0,0,395,425,1,0,0,0,396,397,5,59,0,0,397,398,5,77,0,0,398,399,
        3,0,0,0,399,400,5,79,0,0,400,401,3,0,0,0,401,402,5,78,0,0,402,425,
        1,0,0,0,403,404,5,60,0,0,404,405,5,77,0,0,405,406,3,0,0,0,406,407,
        5,79,0,0,407,408,3,0,0,0,408,409,5,78,0,0,409,425,1,0,0,0,410,411,
        5,61,0,0,411,412,5,77,0,0,412,413,3,0,0,0,413,414,5,79,0,0,414,415,
        3,0,0,0,415,416,5,78,0,0,416,425,1,0,0,0,417,418,5,62,0,0,418,419,
        5,77,0,0,419,420,3,0,0,0,420,421,5,79,0,0,421,422,3,0,0,0,422,423,
        5,78,0,0,423,425,1,0,0,0,424,347,1,0,0,0,424,354,1,0,0,0,424,361,
        1,0,0,0,424,368,1,0,0,0,424,375,1,0,0,0,424,382,1,0,0,0,424,389,
        1,0,0,0,424,396,1,0,0,0,424,403,1,0,0,0,424,410,1,0,0,0,424,417,
        1,0,0,0,425,19,1,0,0,0,426,427,5,31,0,0,427,428,5,77,0,0,428,429,
        3,0,0,0,429,430,5,79,0,0,430,431,3,0,0,0,431,432,5,79,0,0,432,433,
        3,0,0,0,433,434,5,78,0,0,434,472,1,0,0,0,435,436,5,37,0,0,436,437,
        5,77,0,0,437,438,3,0,0,0,438,439,5,79,0,0,439,440,3,0,0,0,440,441,
        5,79,0,0,441,442,3,0,0,0,442,443,5,78,0,0,443,472,1,0,0,0,444,445,
        5,39,0,0,445,446,5,77,0,0,446,447,3,0,0,0,447,448,5,79,0,0,448,449,
        3,0,0,0,449,450,5,79,0,0,450,451,3,0,0,0,451,452,5,78,0,0,452,472,
        1,0,0,0,453,454,5,51,0,0,454,455,5,77,0,0,455,456,3,0,0,0,456,457,
        5,79,0,0,457,458,3,0,0,0,458,459,5,79,0,0,459,460,3,0,0,0,460,461,
        5,78,0,0,461,472,1,0,0,0,462,463,5,63,0,0,463,464,5,77,0,0,464,465,
        3,0,0,0,465,466,5,79,0,0,466,467,3,0,0,0,467,468,5,79,0,0,468,469,
        3,0,0,0,469,470,5,78,0,0,470,472,1,0,0,0,471,426,1,0,0,0,471,435,
        1,0,0,0,471,444,1,0,0,0,471,453,1,0,0,0,471,462,1,0,0,0,472,21,1,
        0,0,0,473,474,5,48,0,0,474,475,5,77,0,0,475,476,3,0,0,0,476,477,
        5,79,0,0,477,478,3,0,0,0,478,479,5,79,0,0,479,480,3,0,0,0,480,481,
        5,79,0,0,481,482,3,0,0,0,482,483,5,78,0,0,483,23,1,0,0,0,484,485,
        5,19,0,0,485,486,5,77,0,0,486,491,3,0,0,0,487,488,5,79,0,0,488,490,
        3,0,0,0,489,487,1,0,0,0,490,493,1,0,0,0,491,489,1,0,0,0,491,492,
        1,0,0,0,492,494,1,0,0,0,493,491,1,0,0,0,494,495,5,78,0,0,495,556,
        1,0,0,0,496,497,5,20,0,0,497,498,5,77,0,0,498,503,3,0,0,0,499,500,
        5,79,0,0,500,502,3,0,0,0,501,499,1,0,0,0,502,505,1,0,0,0,503,501,
        1,0,0,0,503,504,1,0,0,0,504,506,1,0,0,0,505,503,1,0,0,0,506,507,
        5,78,0,0,507,556,1,0,0,0,508,509,5,45,0,0,509,510,5,77,0,0,510,513,
        3,0,0,0,511,512,5,79,0,0,512,514,3,0,0,0,513,511,1,0,0,0,514,515,
        1,0,0,0,515,513,1,0,0,0,515,516,1,0,0,0,516,517,1,0,0,0,517,518,
        5,78,0,0,518,556,1,0,0,0,519,520,5,46,0,0,520,521,5,77,0,0,521,524,
        3,0,0,0,522,523,5,79,0,0,523,525,3,0,0,0,524,522,1,0,0,0,525,526,
        1,0,0,0,526,524,1,0,0,0,526,527,1,0,0,0,527,528,1,0,0,0,528,529,
        5,78,0,0,529,556,1,0,0,0,530,531,5,47,0,0,531,532,5,77,0,0,532,535,
        3,0,0,0,533,534,5,79,0,0,534,536,3,0,0,0,535,533,1,0,0,0,536,537,
        1,0,0,0,537,535,1,0,0,0,537,538,1,0,0,0,538,539,1,0,0,0,539,540,
        5,78,0,0,540,556,1,0,0,0,541,542,5,49,0,0,542,543,5,77,0,0,543,544,
        3,0,0,0,544,545,5,79,0,0,545,546,3,0,0,0,546,547,5,78,0,0,547,556,
        1,0,0,0,548,549,5,50,0,0,549,550,5,77,0,0,550,551,3,0,0,0,551,552,
        5,79,0,0,552,553,3,0,0,0,553,554,5,78,0,0,554,556,1,0,0,0,555,484,
        1,0,0,0,555,496,1,0,0,0,555,508,1,0,0,0,555,519,1,0,0,0,555,530,
        1,0,0,0,555,541,1,0,0,0,555,548,1,0,0,0,556,25,1,0,0,0,22,28,51,
        53,65,67,82,84,92,99,111,118,143,148,345,424,471,491,503,515,526,
        537,555
    ]

class MathExprParser ( Parser ):

    grammarFileName = "MathExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sin'", "'cos'", "'tan'", "'asin'", "'acos'", 
                     "'atan'", "'atan2'", "'sinh'", "'cosh'", "'tanh'", 
                     "'asinh'", "'acosh'", "'atanh'", "'abs'", "'sqrt'", 
                     "'ln'", "'log'", "'exp'", "'smin'", "'smax'", "'tmin'", 
                     "'tmax'", "'tnorm'", "'snorm'", "'floor'", "'ceil'", 
                     "'round'", "'gamma'", "'pow'", "'sigm'", "'clamp'", 
                     "'fft'", "'ifft'", "'angle'", "'print'", "<INVALID>", 
                     "'lerp'", "'step'", "'smoothstep'", "'fract'", "'relu'", 
                     "'softplus'", "'gelu'", "'sign'", "'map'", "<INVALID>", 
                     "<INVALID>", "'swap'", "<INVALID>", "<INVALID>", "'range'", 
                     "'topk'", "'botk'", "'pinv'", "'sum'", "'mean'", "'std'", 
                     "'var'", "<INVALID>", "<INVALID>", "'quantile'", "'dot'", 
                     "'moment'", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", 
                     "'>='", "'>'", "'<='", "'<'", "'=='", "'!='", "'|'", 
                     "'('", "')'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "SIN", "COS", "TAN", "ASIN", "ACOS", 
                      "ATAN", "ATAN2", "SINH", "COSH", "TANH", "ASINH", 
                      "ACOSH", "ATANH", "ABS", "SQRT", "LN", "LOG", "EXP", 
                      "SMIN", "SMAX", "TMIN", "TMAX", "TNORM", "SNORM", 
                      "FLOOR", "CEIL", "ROUND", "GAMMA", "POWE", "SIGM", 
                      "CLAMP", "SFFT", "SIFFT", "ANGL", "PRNT", "PRINT_SHAPE", 
                      "LERP", "STEP", "SMOOTHSTEP", "FRACT", "RELU", "SOFTPLUS", 
                      "GELU", "SIGN", "MAP", "EZCONV", "CONV", "SWAP", "PERM", 
                      "RESHAPE", "RANGE", "TOPK", "BOTK", "PINV", "SUM", 
                      "MEAN", "STD", "VAR", "QUARTILE", "PERCENTILE", "QUANTILE", 
                      "DOT", "MOMENT", "PLUS", "MINUS", "MULT", "DIV", "MOD", 
                      "POW", "GE", "GT", "LE", "LT", "EQ", "NE", "PIPE", 
                      "LPAREN", "RPAREN", "COMMA", "LBRACKET", "RBRACKET", 
                      "CONSTANT", "NUMBER", "VARIABLE", "WS" ]

    RULE_expr = 0
    RULE_compExpr = 1
    RULE_addExpr = 2
    RULE_mulExpr = 3
    RULE_powExpr = 4
    RULE_unaryExpr = 5
    RULE_indexExpr = 6
    RULE_atom = 7
    RULE_func1 = 8
    RULE_func2 = 9
    RULE_func3 = 10
    RULE_func4 = 11
    RULE_funcN = 12

    ruleNames =  [ "expr", "compExpr", "addExpr", "mulExpr", "powExpr", 
                   "unaryExpr", "indexExpr", "atom", "func1", "func2", "func3", 
                   "func4", "funcN" ]

    EOF = Token.EOF
    SIN=1
    COS=2
    TAN=3
    ASIN=4
    ACOS=5
    ATAN=6
    ATAN2=7
    SINH=8
    COSH=9
    TANH=10
    ASINH=11
    ACOSH=12
    ATANH=13
    ABS=14
    SQRT=15
    LN=16
    LOG=17
    EXP=18
    SMIN=19
    SMAX=20
    TMIN=21
    TMAX=22
    TNORM=23
    SNORM=24
    FLOOR=25
    CEIL=26
    ROUND=27
    GAMMA=28
    POWE=29
    SIGM=30
    CLAMP=31
    SFFT=32
    SIFFT=33
    ANGL=34
    PRNT=35
    PRINT_SHAPE=36
    LERP=37
    STEP=38
    SMOOTHSTEP=39
    FRACT=40
    RELU=41
    SOFTPLUS=42
    GELU=43
    SIGN=44
    MAP=45
    EZCONV=46
    CONV=47
    SWAP=48
    PERM=49
    RESHAPE=50
    RANGE=51
    TOPK=52
    BOTK=53
    PINV=54
    SUM=55
    MEAN=56
    STD=57
    VAR=58
    QUARTILE=59
    PERCENTILE=60
    QUANTILE=61
    DOT=62
    MOMENT=63
    PLUS=64
    MINUS=65
    MULT=66
    DIV=67
    MOD=68
    POW=69
    GE=70
    GT=71
    LE=72
    LT=73
    EQ=74
    NE=75
    PIPE=76
    LPAREN=77
    RPAREN=78
    COMMA=79
    LBRACKET=80
    RBRACKET=81
    CONSTANT=82
    NUMBER=83
    VARIABLE=84
    WS=85

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
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLtExp" ):
                listener.enterLtExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLtExp" ):
                listener.exitLtExp(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExp" ):
                listener.enterEqExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExp" ):
                listener.exitEqExp(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeExp" ):
                listener.enterGeExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeExp" ):
                listener.exitGeExp(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeExp" ):
                listener.enterLeExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeExp" ):
                listener.exitLeExp(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeExp" ):
                listener.enterNeExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeExp" ):
                listener.exitNeExp(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGtExp" ):
                listener.enterGtExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGtExp" ):
                listener.exitGtExp(self)

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

            self.state = 31
            self.addExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.GtExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 33
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 34
                        self.match(MathExprParser.GT)
                        self.state = 35
                        self.addExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.GeExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 36
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 37
                        self.match(MathExprParser.GE)
                        self.state = 38
                        self.addExpr(0)
                        pass

                    elif la_ == 3:
                        localctx = MathExprParser.LtExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 39
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 40
                        self.match(MathExprParser.LT)
                        self.state = 41
                        self.addExpr(0)
                        pass

                    elif la_ == 4:
                        localctx = MathExprParser.LeExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 42
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 43
                        self.match(MathExprParser.LE)
                        self.state = 44
                        self.addExpr(0)
                        pass

                    elif la_ == 5:
                        localctx = MathExprParser.EqExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 45
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 46
                        self.match(MathExprParser.EQ)
                        self.state = 47
                        self.addExpr(0)
                        pass

                    elif la_ == 6:
                        localctx = MathExprParser.NeExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 48
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 49
                        self.match(MathExprParser.NE)
                        self.state = 50
                        self.addExpr(0)
                        pass


                self.state = 55
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_addExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToMulContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 57
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 65
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.AddExpContext(self, MathExprParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 59
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 60
                        self.match(MathExprParser.PLUS)
                        self.state = 61
                        self.mulExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.SubExpContext(self, MathExprParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 62
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 63
                        self.match(MathExprParser.MINUS)
                        self.state = 64
                        self.mulExpr(0)
                        pass


                self.state = 69
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_mulExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToPowContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 71
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 82
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.MulExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 73
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 74
                        self.match(MathExprParser.MULT)
                        self.state = 75
                        self.powExpr()
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.DivExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 76
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 77
                        self.match(MathExprParser.DIV)
                        self.state = 78
                        self.powExpr()
                        pass

                    elif la_ == 3:
                        localctx = MathExprParser.ModExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 79
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 80
                        self.match(MathExprParser.MOD)
                        self.state = 81
                        self.powExpr()
                        pass


                self.state = 86
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
        self.enterRule(localctx, 8, self.RULE_powExpr)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = MathExprParser.PowExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.unaryExpr()
                self.state = 88
                self.match(MathExprParser.POW)
                self.state = 89
                self.powExpr()
                pass

            elif la_ == 2:
                localctx = MathExprParser.ToUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 91
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


    class ToIndexContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def indexExpr(self):
            return self.getTypedRuleContext(MathExprParser.IndexExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToIndex" ):
                listener.enterToIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToIndex" ):
                listener.exitToIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToIndex" ):
                return visitor.visitToIndex(self)
            else:
                return visitor.visitChildren(self)



    def unaryExpr(self):

        localctx = MathExprParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unaryExpr)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                localctx = MathExprParser.UnaryPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(MathExprParser.PLUS)
                self.state = 95
                self.unaryExpr()
                pass
            elif token in [65]:
                localctx = MathExprParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(MathExprParser.MINUS)
                self.state = 97
                self.unaryExpr()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 76, 77, 80, 82, 83, 84]:
                localctx = MathExprParser.ToIndexContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.indexExpr(0)
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


    class IndexExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_indexExpr


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IndexExpContext(IndexExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.IndexExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def indexExpr(self):
            return self.getTypedRuleContext(MathExprParser.IndexExprContext,0)

        def LBRACKET(self):
            return self.getToken(MathExprParser.LBRACKET, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def RBRACKET(self):
            return self.getToken(MathExprParser.RBRACKET, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexExp" ):
                listener.enterIndexExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexExp" ):
                listener.exitIndexExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExp" ):
                return visitor.visitIndexExp(self)
            else:
                return visitor.visitChildren(self)


    class ToAtomContext(IndexExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.IndexExprContext
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



    def indexExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathExprParser.IndexExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_indexExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToAtomContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 102
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MathExprParser.IndexExpContext(self, MathExprParser.IndexExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indexExpr)
                    self.state = 104
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 105
                    self.match(MathExprParser.LBRACKET)
                    self.state = 106
                    self.expr()
                    self.state = 111
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==79:
                        self.state = 107
                        self.match(MathExprParser.COMMA)
                        self.state = 108
                        self.expr()
                        self.state = 113
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 114
                    self.match(MathExprParser.RBRACKET) 
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc4Exp" ):
                listener.enterFunc4Exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc4Exp" ):
                listener.exitFunc4Exp(self)

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

        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class AbsExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.PIPE)
            else:
                return self.getToken(MathExprParser.PIPE, i)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbsExp" ):
                listener.enterAbsExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbsExp" ):
                listener.exitAbsExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbsExp" ):
                return visitor.visitAbsExp(self)
            else:
                return visitor.visitChildren(self)


    class ListExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACKET(self):
            return self.getToken(MathExprParser.LBRACKET, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def RBRACKET(self):
            return self.getToken(MathExprParser.RBRACKET, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExp" ):
                listener.enterListExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExp" ):
                listener.exitListExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExp" ):
                return visitor.visitListExp(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = MathExprParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 40, 41, 42, 43, 44, 54, 55, 56, 57, 58]:
                localctx = MathExprParser.Func1ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.func1()
                pass
            elif token in [7, 21, 22, 29, 38, 52, 53, 59, 60, 61, 62]:
                localctx = MathExprParser.Func2ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.func2()
                pass
            elif token in [31, 37, 39, 51, 63]:
                localctx = MathExprParser.Func3ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.func3()
                pass
            elif token in [48]:
                localctx = MathExprParser.Func4ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 124
                self.func4()
                pass
            elif token in [19, 20, 45, 46, 47, 49, 50]:
                localctx = MathExprParser.FuncNExpContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 125
                self.funcN()
                pass
            elif token in [84]:
                localctx = MathExprParser.VariableExpContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 126
                self.match(MathExprParser.VARIABLE)
                pass
            elif token in [83]:
                localctx = MathExprParser.NumberExpContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 127
                self.match(MathExprParser.NUMBER)
                pass
            elif token in [82]:
                localctx = MathExprParser.ConstantExpContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 128
                self.match(MathExprParser.CONSTANT)
                pass
            elif token in [77]:
                localctx = MathExprParser.ParenExpContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 129
                self.match(MathExprParser.LPAREN)
                self.state = 130
                self.expr()
                self.state = 131
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [76]:
                localctx = MathExprParser.AbsExpContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 133
                self.match(MathExprParser.PIPE)
                self.state = 134
                self.expr()
                self.state = 135
                self.match(MathExprParser.PIPE)
                pass
            elif token in [80]:
                localctx = MathExprParser.ListExpContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 137
                self.match(MathExprParser.LBRACKET)
                self.state = 138
                self.expr()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==79:
                    self.state = 139
                    self.match(MathExprParser.COMMA)
                    self.state = 140
                    self.expr()
                    self.state = 145
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 146
                self.match(MathExprParser.RBRACKET)
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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoftplusFunc" ):
                listener.enterSoftplusFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoftplusFunc" ):
                listener.exitSoftplusFunc(self)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class SqrtFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SQRT(self):
            return self.getToken(MathExprParser.SQRT, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class MeanFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def MEAN(self):
            return self.getToken(MathExprParser.MEAN, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeanFunc" ):
                listener.enterMeanFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeanFunc" ):
                listener.exitMeanFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeanFunc" ):
                return visitor.visitMeanFunc(self)
            else:
                return visitor.visitChildren(self)


    class CeilFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def CEIL(self):
            return self.getToken(MathExprParser.CEIL, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class GeluFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def GELU(self):
            return self.getToken(MathExprParser.GELU, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeluFunc" ):
                listener.enterGeluFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeluFunc" ):
                listener.exitGeluFunc(self)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintFunc" ):
                listener.enterPrintFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintFunc" ):
                listener.exitPrintFunc(self)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class ReluFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def RELU(self):
            return self.getToken(MathExprParser.RELU, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReluFunc" ):
                listener.enterReluFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReluFunc" ):
                listener.exitReluFunc(self)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class LnFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def LN(self):
            return self.getToken(MathExprParser.LN, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class StdFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def STD(self):
            return self.getToken(MathExprParser.STD, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStdFunc" ):
                listener.enterStdFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStdFunc" ):
                listener.exitStdFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStdFunc" ):
                return visitor.visitStdFunc(self)
            else:
                return visitor.visitChildren(self)


    class AcosFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ACOS(self):
            return self.getToken(MathExprParser.ACOS, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class AnglFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ANGL(self):
            return self.getToken(MathExprParser.ANGL, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnglFunc" ):
                listener.enterAnglFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnglFunc" ):
                listener.exitAnglFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnglFunc" ):
                return visitor.visitAnglFunc(self)
            else:
                return visitor.visitChildren(self)


    class SumFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUM(self):
            return self.getToken(MathExprParser.SUM, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumFunc" ):
                listener.enterSumFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumFunc" ):
                listener.exitSumFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumFunc" ):
                return visitor.visitSumFunc(self)
            else:
                return visitor.visitChildren(self)


    class SignFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIGN(self):
            return self.getToken(MathExprParser.SIGN, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignFunc" ):
                listener.enterSignFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignFunc" ):
                listener.exitSignFunc(self)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class PinvFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def PINV(self):
            return self.getToken(MathExprParser.PINV, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPinvFunc" ):
                listener.enterPinvFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPinvFunc" ):
                listener.exitPinvFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPinvFunc" ):
                return visitor.visitPinvFunc(self)
            else:
                return visitor.visitChildren(self)


    class SifftFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIFFT(self):
            return self.getToken(MathExprParser.SIFFT, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSifftFunc" ):
                listener.enterSifftFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSifftFunc" ):
                listener.exitSifftFunc(self)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFractFunc" ):
                listener.enterFractFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFractFunc" ):
                listener.exitFractFunc(self)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class VarFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(MathExprParser.VAR, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarFunc" ):
                listener.enterVarFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarFunc" ):
                listener.exitVarFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarFunc" ):
                return visitor.visitVarFunc(self)
            else:
                return visitor.visitChildren(self)


    class AsinFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ASIN(self):
            return self.getToken(MathExprParser.ASIN, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class SfftFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SFFT(self):
            return self.getToken(MathExprParser.SFFT, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSfftFunc" ):
                listener.enterSfftFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSfftFunc" ):
                listener.exitSfftFunc(self)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class ExpFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXP(self):
            return self.getToken(MathExprParser.EXP, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class PrintShapeFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT_SHAPE(self):
            return self.getToken(MathExprParser.PRINT_SHAPE, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintShapeFunc" ):
                listener.enterPrintShapeFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintShapeFunc" ):
                listener.exitPrintShapeFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintShapeFunc" ):
                return visitor.visitPrintShapeFunc(self)
            else:
                return visitor.visitChildren(self)



    def func1(self):

        localctx = MathExprParser.Func1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func1)
        try:
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = MathExprParser.SinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(MathExprParser.SIN)
                self.state = 151
                self.match(MathExprParser.LPAREN)
                self.state = 152
                self.expr()
                self.state = 153
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [2]:
                localctx = MathExprParser.CosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(MathExprParser.COS)
                self.state = 156
                self.match(MathExprParser.LPAREN)
                self.state = 157
                self.expr()
                self.state = 158
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [3]:
                localctx = MathExprParser.TanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(MathExprParser.TAN)
                self.state = 161
                self.match(MathExprParser.LPAREN)
                self.state = 162
                self.expr()
                self.state = 163
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [4]:
                localctx = MathExprParser.AsinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.match(MathExprParser.ASIN)
                self.state = 166
                self.match(MathExprParser.LPAREN)
                self.state = 167
                self.expr()
                self.state = 168
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [5]:
                localctx = MathExprParser.AcosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 170
                self.match(MathExprParser.ACOS)
                self.state = 171
                self.match(MathExprParser.LPAREN)
                self.state = 172
                self.expr()
                self.state = 173
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [6]:
                localctx = MathExprParser.AtanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 175
                self.match(MathExprParser.ATAN)
                self.state = 176
                self.match(MathExprParser.LPAREN)
                self.state = 177
                self.expr()
                self.state = 178
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [8]:
                localctx = MathExprParser.SinhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 180
                self.match(MathExprParser.SINH)
                self.state = 181
                self.match(MathExprParser.LPAREN)
                self.state = 182
                self.expr()
                self.state = 183
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [9]:
                localctx = MathExprParser.CoshFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 185
                self.match(MathExprParser.COSH)
                self.state = 186
                self.match(MathExprParser.LPAREN)
                self.state = 187
                self.expr()
                self.state = 188
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [10]:
                localctx = MathExprParser.TanhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 190
                self.match(MathExprParser.TANH)
                self.state = 191
                self.match(MathExprParser.LPAREN)
                self.state = 192
                self.expr()
                self.state = 193
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [11]:
                localctx = MathExprParser.AsinhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 195
                self.match(MathExprParser.ASINH)
                self.state = 196
                self.match(MathExprParser.LPAREN)
                self.state = 197
                self.expr()
                self.state = 198
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [12]:
                localctx = MathExprParser.AcoshFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 200
                self.match(MathExprParser.ACOSH)
                self.state = 201
                self.match(MathExprParser.LPAREN)
                self.state = 202
                self.expr()
                self.state = 203
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [13]:
                localctx = MathExprParser.AtanhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 205
                self.match(MathExprParser.ATANH)
                self.state = 206
                self.match(MathExprParser.LPAREN)
                self.state = 207
                self.expr()
                self.state = 208
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [14]:
                localctx = MathExprParser.AbsFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 210
                self.match(MathExprParser.ABS)
                self.state = 211
                self.match(MathExprParser.LPAREN)
                self.state = 212
                self.expr()
                self.state = 213
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [15]:
                localctx = MathExprParser.SqrtFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 215
                self.match(MathExprParser.SQRT)
                self.state = 216
                self.match(MathExprParser.LPAREN)
                self.state = 217
                self.expr()
                self.state = 218
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [16]:
                localctx = MathExprParser.LnFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 220
                self.match(MathExprParser.LN)
                self.state = 221
                self.match(MathExprParser.LPAREN)
                self.state = 222
                self.expr()
                self.state = 223
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [17]:
                localctx = MathExprParser.LogFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 225
                self.match(MathExprParser.LOG)
                self.state = 226
                self.match(MathExprParser.LPAREN)
                self.state = 227
                self.expr()
                self.state = 228
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [18]:
                localctx = MathExprParser.ExpFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 230
                self.match(MathExprParser.EXP)
                self.state = 231
                self.match(MathExprParser.LPAREN)
                self.state = 232
                self.expr()
                self.state = 233
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [23]:
                localctx = MathExprParser.TNormFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 235
                self.match(MathExprParser.TNORM)
                self.state = 236
                self.match(MathExprParser.LPAREN)
                self.state = 237
                self.expr()
                self.state = 238
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [24]:
                localctx = MathExprParser.SNormFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 240
                self.match(MathExprParser.SNORM)
                self.state = 241
                self.match(MathExprParser.LPAREN)
                self.state = 242
                self.expr()
                self.state = 243
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [25]:
                localctx = MathExprParser.FloorFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 20)
                self.state = 245
                self.match(MathExprParser.FLOOR)
                self.state = 246
                self.match(MathExprParser.LPAREN)
                self.state = 247
                self.expr()
                self.state = 248
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [26]:
                localctx = MathExprParser.CeilFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 21)
                self.state = 250
                self.match(MathExprParser.CEIL)
                self.state = 251
                self.match(MathExprParser.LPAREN)
                self.state = 252
                self.expr()
                self.state = 253
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [27]:
                localctx = MathExprParser.RoundFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 22)
                self.state = 255
                self.match(MathExprParser.ROUND)
                self.state = 256
                self.match(MathExprParser.LPAREN)
                self.state = 257
                self.expr()
                self.state = 258
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [28]:
                localctx = MathExprParser.GammaFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 23)
                self.state = 260
                self.match(MathExprParser.GAMMA)
                self.state = 261
                self.match(MathExprParser.LPAREN)
                self.state = 262
                self.expr()
                self.state = 263
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [30]:
                localctx = MathExprParser.SigmoidFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 24)
                self.state = 265
                self.match(MathExprParser.SIGM)
                self.state = 266
                self.match(MathExprParser.LPAREN)
                self.state = 267
                self.expr()
                self.state = 268
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [32]:
                localctx = MathExprParser.SfftFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 25)
                self.state = 270
                self.match(MathExprParser.SFFT)
                self.state = 271
                self.match(MathExprParser.LPAREN)
                self.state = 272
                self.expr()
                self.state = 273
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [33]:
                localctx = MathExprParser.SifftFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 26)
                self.state = 275
                self.match(MathExprParser.SIFFT)
                self.state = 276
                self.match(MathExprParser.LPAREN)
                self.state = 277
                self.expr()
                self.state = 278
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [34]:
                localctx = MathExprParser.AnglFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 27)
                self.state = 280
                self.match(MathExprParser.ANGL)
                self.state = 281
                self.match(MathExprParser.LPAREN)
                self.state = 282
                self.expr()
                self.state = 283
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [35]:
                localctx = MathExprParser.PrintFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 28)
                self.state = 285
                self.match(MathExprParser.PRNT)
                self.state = 286
                self.match(MathExprParser.LPAREN)
                self.state = 287
                self.expr()
                self.state = 288
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [40]:
                localctx = MathExprParser.FractFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 29)
                self.state = 290
                self.match(MathExprParser.FRACT)
                self.state = 291
                self.match(MathExprParser.LPAREN)
                self.state = 292
                self.expr()
                self.state = 293
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [41]:
                localctx = MathExprParser.ReluFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 30)
                self.state = 295
                self.match(MathExprParser.RELU)
                self.state = 296
                self.match(MathExprParser.LPAREN)
                self.state = 297
                self.expr()
                self.state = 298
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [42]:
                localctx = MathExprParser.SoftplusFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 31)
                self.state = 300
                self.match(MathExprParser.SOFTPLUS)
                self.state = 301
                self.match(MathExprParser.LPAREN)
                self.state = 302
                self.expr()
                self.state = 303
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [43]:
                localctx = MathExprParser.GeluFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 32)
                self.state = 305
                self.match(MathExprParser.GELU)
                self.state = 306
                self.match(MathExprParser.LPAREN)
                self.state = 307
                self.expr()
                self.state = 308
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [44]:
                localctx = MathExprParser.SignFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 33)
                self.state = 310
                self.match(MathExprParser.SIGN)
                self.state = 311
                self.match(MathExprParser.LPAREN)
                self.state = 312
                self.expr()
                self.state = 313
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [36]:
                localctx = MathExprParser.PrintShapeFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 34)
                self.state = 315
                self.match(MathExprParser.PRINT_SHAPE)
                self.state = 316
                self.match(MathExprParser.LPAREN)
                self.state = 317
                self.expr()
                self.state = 318
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [54]:
                localctx = MathExprParser.PinvFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 35)
                self.state = 320
                self.match(MathExprParser.PINV)
                self.state = 321
                self.match(MathExprParser.LPAREN)
                self.state = 322
                self.expr()
                self.state = 323
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [55]:
                localctx = MathExprParser.SumFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 36)
                self.state = 325
                self.match(MathExprParser.SUM)
                self.state = 326
                self.match(MathExprParser.LPAREN)
                self.state = 327
                self.expr()
                self.state = 328
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [56]:
                localctx = MathExprParser.MeanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 37)
                self.state = 330
                self.match(MathExprParser.MEAN)
                self.state = 331
                self.match(MathExprParser.LPAREN)
                self.state = 332
                self.expr()
                self.state = 333
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [57]:
                localctx = MathExprParser.StdFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 38)
                self.state = 335
                self.match(MathExprParser.STD)
                self.state = 336
                self.match(MathExprParser.LPAREN)
                self.state = 337
                self.expr()
                self.state = 338
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [58]:
                localctx = MathExprParser.VarFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 39)
                self.state = 340
                self.match(MathExprParser.VAR)
                self.state = 341
                self.match(MathExprParser.LPAREN)
                self.state = 342
                self.expr()
                self.state = 343
                self.match(MathExprParser.RPAREN)
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



    class TopkFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOPK(self):
            return self.getToken(MathExprParser.TOPK, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopkFunc" ):
                listener.enterTopkFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopkFunc" ):
                listener.exitTopkFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopkFunc" ):
                return visitor.visitTopkFunc(self)
            else:
                return visitor.visitChildren(self)


    class BotkFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOTK(self):
            return self.getToken(MathExprParser.BOTK, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBotkFunc" ):
                listener.enterBotkFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBotkFunc" ):
                listener.exitBotkFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBotkFunc" ):
                return visitor.visitBotkFunc(self)
            else:
                return visitor.visitChildren(self)


    class PercentileFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def PERCENTILE(self):
            return self.getToken(MathExprParser.PERCENTILE, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPercentileFunc" ):
                listener.enterPercentileFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPercentileFunc" ):
                listener.exitPercentileFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPercentileFunc" ):
                return visitor.visitPercentileFunc(self)
            else:
                return visitor.visitChildren(self)


    class TMaxFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TMAX(self):
            return self.getToken(MathExprParser.TMAX, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class DotFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MathExprParser.DOT, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDotFunc" ):
                listener.enterDotFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDotFunc" ):
                listener.exitDotFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDotFunc" ):
                return visitor.visitDotFunc(self)
            else:
                return visitor.visitChildren(self)


    class StepFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def STEP(self):
            return self.getToken(MathExprParser.STEP, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStepFunc" ):
                listener.enterStepFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStepFunc" ):
                listener.exitStepFunc(self)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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


    class QuantileFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUANTILE(self):
            return self.getToken(MathExprParser.QUANTILE, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantileFunc" ):
                listener.enterQuantileFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantileFunc" ):
                listener.exitQuantileFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantileFunc" ):
                return visitor.visitQuantileFunc(self)
            else:
                return visitor.visitChildren(self)


    class QuartileFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUARTILE(self):
            return self.getToken(MathExprParser.QUARTILE, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuartileFunc" ):
                listener.enterQuartileFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuartileFunc" ):
                listener.exitQuartileFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuartileFunc" ):
                return visitor.visitQuartileFunc(self)
            else:
                return visitor.visitChildren(self)


    class TMinFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TMIN(self):
            return self.getToken(MathExprParser.TMIN, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        self.enterRule(localctx, 18, self.RULE_func2)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = MathExprParser.PowFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(MathExprParser.POWE)
                self.state = 348
                self.match(MathExprParser.LPAREN)
                self.state = 349
                self.expr()
                self.state = 350
                self.match(MathExprParser.COMMA)
                self.state = 351
                self.expr()
                self.state = 352
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [7]:
                localctx = MathExprParser.Atan2FuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(MathExprParser.ATAN2)
                self.state = 355
                self.match(MathExprParser.LPAREN)
                self.state = 356
                self.expr()
                self.state = 357
                self.match(MathExprParser.COMMA)
                self.state = 358
                self.expr()
                self.state = 359
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [21]:
                localctx = MathExprParser.TMinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.match(MathExprParser.TMIN)
                self.state = 362
                self.match(MathExprParser.LPAREN)
                self.state = 363
                self.expr()
                self.state = 364
                self.match(MathExprParser.COMMA)
                self.state = 365
                self.expr()
                self.state = 366
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [22]:
                localctx = MathExprParser.TMaxFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 368
                self.match(MathExprParser.TMAX)
                self.state = 369
                self.match(MathExprParser.LPAREN)
                self.state = 370
                self.expr()
                self.state = 371
                self.match(MathExprParser.COMMA)
                self.state = 372
                self.expr()
                self.state = 373
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [38]:
                localctx = MathExprParser.StepFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 375
                self.match(MathExprParser.STEP)
                self.state = 376
                self.match(MathExprParser.LPAREN)
                self.state = 377
                self.expr()
                self.state = 378
                self.match(MathExprParser.COMMA)
                self.state = 379
                self.expr()
                self.state = 380
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [52]:
                localctx = MathExprParser.TopkFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 382
                self.match(MathExprParser.TOPK)
                self.state = 383
                self.match(MathExprParser.LPAREN)
                self.state = 384
                self.expr()
                self.state = 385
                self.match(MathExprParser.COMMA)
                self.state = 386
                self.expr()
                self.state = 387
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [53]:
                localctx = MathExprParser.BotkFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 389
                self.match(MathExprParser.BOTK)
                self.state = 390
                self.match(MathExprParser.LPAREN)
                self.state = 391
                self.expr()
                self.state = 392
                self.match(MathExprParser.COMMA)
                self.state = 393
                self.expr()
                self.state = 394
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [59]:
                localctx = MathExprParser.QuartileFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 396
                self.match(MathExprParser.QUARTILE)
                self.state = 397
                self.match(MathExprParser.LPAREN)
                self.state = 398
                self.expr()
                self.state = 399
                self.match(MathExprParser.COMMA)
                self.state = 400
                self.expr()
                self.state = 401
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [60]:
                localctx = MathExprParser.PercentileFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 403
                self.match(MathExprParser.PERCENTILE)
                self.state = 404
                self.match(MathExprParser.LPAREN)
                self.state = 405
                self.expr()
                self.state = 406
                self.match(MathExprParser.COMMA)
                self.state = 407
                self.expr()
                self.state = 408
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [61]:
                localctx = MathExprParser.QuantileFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 410
                self.match(MathExprParser.QUANTILE)
                self.state = 411
                self.match(MathExprParser.LPAREN)
                self.state = 412
                self.expr()
                self.state = 413
                self.match(MathExprParser.COMMA)
                self.state = 414
                self.expr()
                self.state = 415
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [62]:
                localctx = MathExprParser.DotFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 417
                self.match(MathExprParser.DOT)
                self.state = 418
                self.match(MathExprParser.LPAREN)
                self.state = 419
                self.expr()
                self.state = 420
                self.match(MathExprParser.COMMA)
                self.state = 421
                self.expr()
                self.state = 422
                self.match(MathExprParser.RPAREN)
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



    class MomentFuncContext(Func3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOMENT(self):
            return self.getToken(MathExprParser.MOMENT, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMomentFunc" ):
                listener.enterMomentFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMomentFunc" ):
                listener.exitMomentFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMomentFunc" ):
                return visitor.visitMomentFunc(self)
            else:
                return visitor.visitChildren(self)


    class LerpFuncContext(Func3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def LERP(self):
            return self.getToken(MathExprParser.LERP, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLerpFunc" ):
                listener.enterLerpFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLerpFunc" ):
                listener.exitLerpFunc(self)

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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSmoothstepFunc" ):
                listener.enterSmoothstepFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSmoothstepFunc" ):
                listener.exitSmoothstepFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmoothstepFunc" ):
                return visitor.visitSmoothstepFunc(self)
            else:
                return visitor.visitChildren(self)


    class RangeFuncContext(Func3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def RANGE(self):
            return self.getToken(MathExprParser.RANGE, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeFunc" ):
                listener.enterRangeFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeFunc" ):
                listener.exitRangeFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeFunc" ):
                return visitor.visitRangeFunc(self)
            else:
                return visitor.visitChildren(self)


    class ClampFuncContext(Func3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def CLAMP(self):
            return self.getToken(MathExprParser.CLAMP, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

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
        self.enterRule(localctx, 20, self.RULE_func3)
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = MathExprParser.ClampFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.match(MathExprParser.CLAMP)
                self.state = 427
                self.match(MathExprParser.LPAREN)
                self.state = 428
                self.expr()
                self.state = 429
                self.match(MathExprParser.COMMA)
                self.state = 430
                self.expr()
                self.state = 431
                self.match(MathExprParser.COMMA)
                self.state = 432
                self.expr()
                self.state = 433
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [37]:
                localctx = MathExprParser.LerpFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(MathExprParser.LERP)
                self.state = 436
                self.match(MathExprParser.LPAREN)
                self.state = 437
                self.expr()
                self.state = 438
                self.match(MathExprParser.COMMA)
                self.state = 439
                self.expr()
                self.state = 440
                self.match(MathExprParser.COMMA)
                self.state = 441
                self.expr()
                self.state = 442
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [39]:
                localctx = MathExprParser.SmoothstepFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 444
                self.match(MathExprParser.SMOOTHSTEP)
                self.state = 445
                self.match(MathExprParser.LPAREN)
                self.state = 446
                self.expr()
                self.state = 447
                self.match(MathExprParser.COMMA)
                self.state = 448
                self.expr()
                self.state = 449
                self.match(MathExprParser.COMMA)
                self.state = 450
                self.expr()
                self.state = 451
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [51]:
                localctx = MathExprParser.RangeFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 453
                self.match(MathExprParser.RANGE)
                self.state = 454
                self.match(MathExprParser.LPAREN)
                self.state = 455
                self.expr()
                self.state = 456
                self.match(MathExprParser.COMMA)
                self.state = 457
                self.expr()
                self.state = 458
                self.match(MathExprParser.COMMA)
                self.state = 459
                self.expr()
                self.state = 460
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [63]:
                localctx = MathExprParser.MomentFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 462
                self.match(MathExprParser.MOMENT)
                self.state = 463
                self.match(MathExprParser.LPAREN)
                self.state = 464
                self.expr()
                self.state = 465
                self.match(MathExprParser.COMMA)
                self.state = 466
                self.expr()
                self.state = 467
                self.match(MathExprParser.COMMA)
                self.state = 468
                self.expr()
                self.state = 469
                self.match(MathExprParser.RPAREN)
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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwapFunc" ):
                listener.enterSwapFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwapFunc" ):
                listener.exitSwapFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwapFunc" ):
                return visitor.visitSwapFunc(self)
            else:
                return visitor.visitChildren(self)



    def func4(self):

        localctx = MathExprParser.Func4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func4)
        try:
            localctx = MathExprParser.SwapFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(MathExprParser.SWAP)
            self.state = 474
            self.match(MathExprParser.LPAREN)
            self.state = 475
            self.expr()
            self.state = 476
            self.match(MathExprParser.COMMA)
            self.state = 477
            self.expr()
            self.state = 478
            self.match(MathExprParser.COMMA)
            self.state = 479
            self.expr()
            self.state = 480
            self.match(MathExprParser.COMMA)
            self.state = 481
            self.expr()
            self.state = 482
            self.match(MathExprParser.RPAREN)
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
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)

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


    class MapFuncContext(FuncNContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncNContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MAP(self):
            return self.getToken(MathExprParser.MAP, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapFunc" ):
                listener.enterMapFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapFunc" ):
                listener.exitMapFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapFunc" ):
                return visitor.visitMapFunc(self)
            else:
                return visitor.visitChildren(self)


    class EzConvFuncContext(FuncNContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncNContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EZCONV(self):
            return self.getToken(MathExprParser.EZCONV, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEzConvFunc" ):
                listener.enterEzConvFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEzConvFunc" ):
                listener.exitEzConvFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEzConvFunc" ):
                return visitor.visitEzConvFunc(self)
            else:
                return visitor.visitChildren(self)


    class PermuteFuncContext(FuncNContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncNContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PERM(self):
            return self.getToken(MathExprParser.PERM, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPermuteFunc" ):
                listener.enterPermuteFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPermuteFunc" ):
                listener.exitPermuteFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPermuteFunc" ):
                return visitor.visitPermuteFunc(self)
            else:
                return visitor.visitChildren(self)


    class ReshapeFuncContext(FuncNContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncNContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RESHAPE(self):
            return self.getToken(MathExprParser.RESHAPE, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(MathExprParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReshapeFunc" ):
                listener.enterReshapeFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReshapeFunc" ):
                listener.exitReshapeFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReshapeFunc" ):
                return visitor.visitReshapeFunc(self)
            else:
                return visitor.visitChildren(self)


    class SMinFuncContext(FuncNContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncNContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SMIN(self):
            return self.getToken(MathExprParser.SMIN, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)

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


    class ConvFuncContext(FuncNContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncNContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONV(self):
            return self.getToken(MathExprParser.CONV, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConvFunc" ):
                listener.enterConvFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConvFunc" ):
                listener.exitConvFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConvFunc" ):
                return visitor.visitConvFunc(self)
            else:
                return visitor.visitChildren(self)



    def funcN(self):

        localctx = MathExprParser.FuncNContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcN)
        self._la = 0 # Token type
        try:
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = MathExprParser.SMinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.match(MathExprParser.SMIN)
                self.state = 485
                self.match(MathExprParser.LPAREN)
                self.state = 486
                self.expr()
                self.state = 491
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==79:
                    self.state = 487
                    self.match(MathExprParser.COMMA)
                    self.state = 488
                    self.expr()
                    self.state = 493
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 494
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [20]:
                localctx = MathExprParser.SMaxFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 496
                self.match(MathExprParser.SMAX)
                self.state = 497
                self.match(MathExprParser.LPAREN)
                self.state = 498
                self.expr()
                self.state = 503
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==79:
                    self.state = 499
                    self.match(MathExprParser.COMMA)
                    self.state = 500
                    self.expr()
                    self.state = 505
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 506
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [45]:
                localctx = MathExprParser.MapFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.match(MathExprParser.MAP)
                self.state = 509
                self.match(MathExprParser.LPAREN)
                self.state = 510
                self.expr()
                self.state = 513 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 511
                    self.match(MathExprParser.COMMA)
                    self.state = 512
                    self.expr()
                    self.state = 515 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==79):
                        break

                self.state = 517
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [46]:
                localctx = MathExprParser.EzConvFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 519
                self.match(MathExprParser.EZCONV)
                self.state = 520
                self.match(MathExprParser.LPAREN)
                self.state = 521
                self.expr()
                self.state = 524 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 522
                    self.match(MathExprParser.COMMA)
                    self.state = 523
                    self.expr()
                    self.state = 526 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==79):
                        break

                self.state = 528
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [47]:
                localctx = MathExprParser.ConvFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 530
                self.match(MathExprParser.CONV)
                self.state = 531
                self.match(MathExprParser.LPAREN)
                self.state = 532
                self.expr()
                self.state = 535 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 533
                    self.match(MathExprParser.COMMA)
                    self.state = 534
                    self.expr()
                    self.state = 537 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==79):
                        break

                self.state = 539
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [49]:
                localctx = MathExprParser.PermuteFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 541
                self.match(MathExprParser.PERM)
                self.state = 542
                self.match(MathExprParser.LPAREN)
                self.state = 543
                self.expr()
                self.state = 544
                self.match(MathExprParser.COMMA)
                self.state = 545
                self.expr()
                self.state = 546
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [50]:
                localctx = MathExprParser.ReshapeFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 548
                self.match(MathExprParser.RESHAPE)
                self.state = 549
                self.match(MathExprParser.LPAREN)
                self.state = 550
                self.expr()
                self.state = 551
                self.match(MathExprParser.COMMA)
                self.state = 552
                self.expr()
                self.state = 553
                self.match(MathExprParser.RPAREN)
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
        self._predicates[6] = self.indexExpr_sempred
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


    def indexExpr_sempred(self, localctx:IndexExprContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 2)





