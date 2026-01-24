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
        4,1,101,715,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,
        0,41,9,0,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,0,1,1,1,1,1,1,
        3,1,55,8,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,
        3,70,8,3,10,3,12,3,73,9,3,1,4,1,4,3,4,77,8,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        5,5,100,8,5,10,5,12,5,103,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,5,6,114,8,6,10,6,12,6,117,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,5,7,131,8,7,10,7,12,7,134,9,7,1,8,1,8,1,8,1,8,1,
        8,3,8,141,8,8,1,9,1,9,1,9,1,9,1,9,3,9,148,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,158,8,10,10,10,12,10,161,9,10,1,10,1,10,
        5,10,165,8,10,10,10,12,10,168,9,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,5,11,190,8,11,10,11,12,11,193,9,11,1,11,1,11,1,11,1,11,1,11,
        3,11,200,8,11,1,11,3,11,203,8,11,1,12,1,12,1,12,5,12,208,8,12,10,
        12,12,12,211,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,3,13,423,8,13,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,3,14,551,8,14,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,3,15,616,8,15,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,3,16,640,8,16,1,17,1,17,1,17,1,17,1,17,5,
        17,647,8,17,10,17,12,17,650,9,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,5,17,659,8,17,10,17,12,17,662,9,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,4,17,671,8,17,11,17,12,17,672,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,4,17,682,8,17,11,17,12,17,683,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,4,17,693,8,17,11,17,12,17,694,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,713,8,
        17,1,17,0,4,10,12,14,20,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,0,0,807,0,39,1,0,0,0,2,51,1,0,0,0,4,61,1,0,0,0,6,66,
        1,0,0,0,8,76,1,0,0,0,10,78,1,0,0,0,12,104,1,0,0,0,14,118,1,0,0,0,
        16,140,1,0,0,0,18,147,1,0,0,0,20,149,1,0,0,0,22,202,1,0,0,0,24,204,
        1,0,0,0,26,422,1,0,0,0,28,550,1,0,0,0,30,615,1,0,0,0,32,639,1,0,
        0,0,34,712,1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,41,1,0,0,0,39,
        37,1,0,0,0,39,40,1,0,0,0,40,45,1,0,0,0,41,39,1,0,0,0,42,44,3,4,2,
        0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,
        1,0,0,0,47,45,1,0,0,0,48,49,3,8,4,0,49,50,5,0,0,1,50,1,1,0,0,0,51,
        52,5,100,0,0,52,54,5,91,0,0,53,55,3,6,3,0,54,53,1,0,0,0,54,55,1,
        0,0,0,55,56,1,0,0,0,56,57,5,92,0,0,57,58,5,95,0,0,58,59,3,8,4,0,
        59,60,5,94,0,0,60,3,1,0,0,0,61,62,5,100,0,0,62,63,5,88,0,0,63,64,
        3,8,4,0,64,65,5,94,0,0,65,5,1,0,0,0,66,71,5,100,0,0,67,68,5,93,0,
        0,68,70,5,100,0,0,69,67,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,
        1,0,0,0,72,7,1,0,0,0,73,71,1,0,0,0,74,77,3,22,11,0,75,77,3,10,5,
        0,76,74,1,0,0,0,76,75,1,0,0,0,77,9,1,0,0,0,78,79,6,5,-1,0,79,80,
        3,12,6,0,80,101,1,0,0,0,81,82,10,7,0,0,82,83,5,84,0,0,83,100,3,12,
        6,0,84,85,10,6,0,0,85,86,5,83,0,0,86,100,3,12,6,0,87,88,10,5,0,0,
        88,89,5,86,0,0,89,100,3,12,6,0,90,91,10,4,0,0,91,92,5,85,0,0,92,
        100,3,12,6,0,93,94,10,3,0,0,94,95,5,87,0,0,95,100,3,12,6,0,96,97,
        10,2,0,0,97,98,5,89,0,0,98,100,3,12,6,0,99,81,1,0,0,0,99,84,1,0,
        0,0,99,87,1,0,0,0,99,90,1,0,0,0,99,93,1,0,0,0,99,96,1,0,0,0,100,
        103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,11,1,0,0,0,103,101,
        1,0,0,0,104,105,6,6,-1,0,105,106,3,14,7,0,106,115,1,0,0,0,107,108,
        10,3,0,0,108,109,5,77,0,0,109,114,3,14,7,0,110,111,10,2,0,0,111,
        112,5,78,0,0,112,114,3,14,7,0,113,107,1,0,0,0,113,110,1,0,0,0,114,
        117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,13,1,0,0,0,117,115,
        1,0,0,0,118,119,6,7,-1,0,119,120,3,16,8,0,120,132,1,0,0,0,121,122,
        10,4,0,0,122,123,5,79,0,0,123,131,3,16,8,0,124,125,10,3,0,0,125,
        126,5,80,0,0,126,131,3,16,8,0,127,128,10,2,0,0,128,129,5,81,0,0,
        129,131,3,16,8,0,130,121,1,0,0,0,130,124,1,0,0,0,130,127,1,0,0,0,
        131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,15,1,0,0,0,134,
        132,1,0,0,0,135,136,3,18,9,0,136,137,5,82,0,0,137,138,3,16,8,0,138,
        141,1,0,0,0,139,141,3,18,9,0,140,135,1,0,0,0,140,139,1,0,0,0,141,
        17,1,0,0,0,142,143,5,77,0,0,143,148,3,18,9,0,144,145,5,78,0,0,145,
        148,3,18,9,0,146,148,3,20,10,0,147,142,1,0,0,0,147,144,1,0,0,0,147,
        146,1,0,0,0,148,19,1,0,0,0,149,150,6,10,-1,0,150,151,3,22,11,0,151,
        166,1,0,0,0,152,153,10,2,0,0,153,154,5,96,0,0,154,159,3,8,4,0,155,
        156,5,93,0,0,156,158,3,8,4,0,157,155,1,0,0,0,158,161,1,0,0,0,159,
        157,1,0,0,0,159,160,1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,
        163,5,97,0,0,163,165,1,0,0,0,164,152,1,0,0,0,165,168,1,0,0,0,166,
        164,1,0,0,0,166,167,1,0,0,0,167,21,1,0,0,0,168,166,1,0,0,0,169,203,
        3,26,13,0,170,203,3,28,14,0,171,203,3,30,15,0,172,203,3,32,16,0,
        173,203,3,34,17,0,174,203,5,100,0,0,175,203,5,99,0,0,176,203,5,98,
        0,0,177,178,5,91,0,0,178,179,3,8,4,0,179,180,5,92,0,0,180,203,1,
        0,0,0,181,182,5,90,0,0,182,183,3,8,4,0,183,184,5,90,0,0,184,203,
        1,0,0,0,185,186,5,96,0,0,186,191,3,8,4,0,187,188,5,93,0,0,188,190,
        3,8,4,0,189,187,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,
        1,0,0,0,192,194,1,0,0,0,193,191,1,0,0,0,194,195,5,97,0,0,195,203,
        1,0,0,0,196,197,5,100,0,0,197,199,5,91,0,0,198,200,3,24,12,0,199,
        198,1,0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,203,5,92,0,0,202,
        169,1,0,0,0,202,170,1,0,0,0,202,171,1,0,0,0,202,172,1,0,0,0,202,
        173,1,0,0,0,202,174,1,0,0,0,202,175,1,0,0,0,202,176,1,0,0,0,202,
        177,1,0,0,0,202,181,1,0,0,0,202,185,1,0,0,0,202,196,1,0,0,0,203,
        23,1,0,0,0,204,209,3,8,4,0,205,206,5,93,0,0,206,208,3,8,4,0,207,
        205,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,
        25,1,0,0,0,211,209,1,0,0,0,212,213,5,1,0,0,213,214,5,91,0,0,214,
        215,3,8,4,0,215,216,5,92,0,0,216,423,1,0,0,0,217,218,5,2,0,0,218,
        219,5,91,0,0,219,220,3,8,4,0,220,221,5,92,0,0,221,423,1,0,0,0,222,
        223,5,3,0,0,223,224,5,91,0,0,224,225,3,8,4,0,225,226,5,92,0,0,226,
        423,1,0,0,0,227,228,5,4,0,0,228,229,5,91,0,0,229,230,3,8,4,0,230,
        231,5,92,0,0,231,423,1,0,0,0,232,233,5,5,0,0,233,234,5,91,0,0,234,
        235,3,8,4,0,235,236,5,92,0,0,236,423,1,0,0,0,237,238,5,6,0,0,238,
        239,5,91,0,0,239,240,3,8,4,0,240,241,5,92,0,0,241,423,1,0,0,0,242,
        243,5,8,0,0,243,244,5,91,0,0,244,245,3,8,4,0,245,246,5,92,0,0,246,
        423,1,0,0,0,247,248,5,9,0,0,248,249,5,91,0,0,249,250,3,8,4,0,250,
        251,5,92,0,0,251,423,1,0,0,0,252,253,5,10,0,0,253,254,5,91,0,0,254,
        255,3,8,4,0,255,256,5,92,0,0,256,423,1,0,0,0,257,258,5,11,0,0,258,
        259,5,91,0,0,259,260,3,8,4,0,260,261,5,92,0,0,261,423,1,0,0,0,262,
        263,5,12,0,0,263,264,5,91,0,0,264,265,3,8,4,0,265,266,5,92,0,0,266,
        423,1,0,0,0,267,268,5,13,0,0,268,269,5,91,0,0,269,270,3,8,4,0,270,
        271,5,92,0,0,271,423,1,0,0,0,272,273,5,14,0,0,273,274,5,91,0,0,274,
        275,3,8,4,0,275,276,5,92,0,0,276,423,1,0,0,0,277,278,5,15,0,0,278,
        279,5,91,0,0,279,280,3,8,4,0,280,281,5,92,0,0,281,423,1,0,0,0,282,
        283,5,16,0,0,283,284,5,91,0,0,284,285,3,8,4,0,285,286,5,92,0,0,286,
        423,1,0,0,0,287,288,5,17,0,0,288,289,5,91,0,0,289,290,3,8,4,0,290,
        291,5,92,0,0,291,423,1,0,0,0,292,293,5,18,0,0,293,294,5,91,0,0,294,
        295,3,8,4,0,295,296,5,92,0,0,296,423,1,0,0,0,297,298,5,23,0,0,298,
        299,5,91,0,0,299,300,3,8,4,0,300,301,5,92,0,0,301,423,1,0,0,0,302,
        303,5,24,0,0,303,304,5,91,0,0,304,305,3,8,4,0,305,306,5,92,0,0,306,
        423,1,0,0,0,307,308,5,25,0,0,308,309,5,91,0,0,309,310,3,8,4,0,310,
        311,5,92,0,0,311,423,1,0,0,0,312,313,5,26,0,0,313,314,5,91,0,0,314,
        315,3,8,4,0,315,316,5,92,0,0,316,423,1,0,0,0,317,318,5,27,0,0,318,
        319,5,91,0,0,319,320,3,8,4,0,320,321,5,92,0,0,321,423,1,0,0,0,322,
        323,5,28,0,0,323,324,5,91,0,0,324,325,3,8,4,0,325,326,5,92,0,0,326,
        423,1,0,0,0,327,328,5,30,0,0,328,329,5,91,0,0,329,330,3,8,4,0,330,
        331,5,92,0,0,331,423,1,0,0,0,332,333,5,32,0,0,333,334,5,91,0,0,334,
        335,3,8,4,0,335,336,5,92,0,0,336,423,1,0,0,0,337,338,5,33,0,0,338,
        339,5,91,0,0,339,340,3,8,4,0,340,341,5,92,0,0,341,423,1,0,0,0,342,
        343,5,34,0,0,343,344,5,91,0,0,344,345,3,8,4,0,345,346,5,92,0,0,346,
        423,1,0,0,0,347,348,5,35,0,0,348,349,5,91,0,0,349,350,3,8,4,0,350,
        351,5,92,0,0,351,423,1,0,0,0,352,353,5,41,0,0,353,354,5,91,0,0,354,
        355,3,8,4,0,355,356,5,92,0,0,356,423,1,0,0,0,357,358,5,42,0,0,358,
        359,5,91,0,0,359,360,3,8,4,0,360,361,5,92,0,0,361,423,1,0,0,0,362,
        363,5,43,0,0,363,364,5,91,0,0,364,365,3,8,4,0,365,366,5,92,0,0,366,
        423,1,0,0,0,367,368,5,44,0,0,368,369,5,91,0,0,369,370,3,8,4,0,370,
        371,5,92,0,0,371,423,1,0,0,0,372,373,5,45,0,0,373,374,5,91,0,0,374,
        375,3,8,4,0,375,376,5,92,0,0,376,423,1,0,0,0,377,378,5,36,0,0,378,
        379,5,91,0,0,379,380,3,8,4,0,380,381,5,92,0,0,381,423,1,0,0,0,382,
        383,5,55,0,0,383,384,5,91,0,0,384,385,3,8,4,0,385,386,5,92,0,0,386,
        423,1,0,0,0,387,388,5,56,0,0,388,389,5,91,0,0,389,390,3,8,4,0,390,
        391,5,92,0,0,391,423,1,0,0,0,392,393,5,57,0,0,393,394,5,91,0,0,394,
        395,3,8,4,0,395,396,5,92,0,0,396,423,1,0,0,0,397,398,5,58,0,0,398,
        399,5,91,0,0,399,400,3,8,4,0,400,401,5,92,0,0,401,423,1,0,0,0,402,
        403,5,59,0,0,403,404,5,91,0,0,404,405,3,8,4,0,405,406,5,92,0,0,406,
        423,1,0,0,0,407,408,5,75,0,0,408,409,5,91,0,0,409,410,3,8,4,0,410,
        411,5,92,0,0,411,423,1,0,0,0,412,413,5,65,0,0,413,414,5,91,0,0,414,
        415,3,8,4,0,415,416,5,92,0,0,416,423,1,0,0,0,417,418,5,66,0,0,418,
        419,5,91,0,0,419,420,3,8,4,0,420,421,5,92,0,0,421,423,1,0,0,0,422,
        212,1,0,0,0,422,217,1,0,0,0,422,222,1,0,0,0,422,227,1,0,0,0,422,
        232,1,0,0,0,422,237,1,0,0,0,422,242,1,0,0,0,422,247,1,0,0,0,422,
        252,1,0,0,0,422,257,1,0,0,0,422,262,1,0,0,0,422,267,1,0,0,0,422,
        272,1,0,0,0,422,277,1,0,0,0,422,282,1,0,0,0,422,287,1,0,0,0,422,
        292,1,0,0,0,422,297,1,0,0,0,422,302,1,0,0,0,422,307,1,0,0,0,422,
        312,1,0,0,0,422,317,1,0,0,0,422,322,1,0,0,0,422,327,1,0,0,0,422,
        332,1,0,0,0,422,337,1,0,0,0,422,342,1,0,0,0,422,347,1,0,0,0,422,
        352,1,0,0,0,422,357,1,0,0,0,422,362,1,0,0,0,422,367,1,0,0,0,422,
        372,1,0,0,0,422,377,1,0,0,0,422,382,1,0,0,0,422,387,1,0,0,0,422,
        392,1,0,0,0,422,397,1,0,0,0,422,402,1,0,0,0,422,407,1,0,0,0,422,
        412,1,0,0,0,422,417,1,0,0,0,423,27,1,0,0,0,424,425,5,29,0,0,425,
        426,5,91,0,0,426,427,3,8,4,0,427,428,5,93,0,0,428,429,3,8,4,0,429,
        430,5,92,0,0,430,551,1,0,0,0,431,432,5,7,0,0,432,433,5,91,0,0,433,
        434,3,8,4,0,434,435,5,93,0,0,435,436,3,8,4,0,436,437,5,92,0,0,437,
        551,1,0,0,0,438,439,5,21,0,0,439,440,5,91,0,0,440,441,3,8,4,0,441,
        442,5,93,0,0,442,443,3,8,4,0,443,444,5,92,0,0,444,551,1,0,0,0,445,
        446,5,22,0,0,446,447,5,91,0,0,447,448,3,8,4,0,448,449,5,93,0,0,449,
        450,3,8,4,0,450,451,5,92,0,0,451,551,1,0,0,0,452,453,5,39,0,0,453,
        454,5,91,0,0,454,455,3,8,4,0,455,456,5,93,0,0,456,457,3,8,4,0,457,
        458,5,92,0,0,458,551,1,0,0,0,459,460,5,53,0,0,460,461,5,91,0,0,461,
        462,3,8,4,0,462,463,5,93,0,0,463,464,3,8,4,0,464,465,5,92,0,0,465,
        551,1,0,0,0,466,467,5,54,0,0,467,468,5,91,0,0,468,469,3,8,4,0,469,
        470,5,93,0,0,470,471,3,8,4,0,471,472,5,92,0,0,472,551,1,0,0,0,473,
        474,5,60,0,0,474,475,5,91,0,0,475,476,3,8,4,0,476,477,5,93,0,0,477,
        478,3,8,4,0,478,479,5,92,0,0,479,551,1,0,0,0,480,481,5,61,0,0,481,
        482,5,91,0,0,482,483,3,8,4,0,483,484,5,93,0,0,484,485,3,8,4,0,485,
        486,5,92,0,0,486,551,1,0,0,0,487,488,5,62,0,0,488,489,5,91,0,0,489,
        490,3,8,4,0,490,491,5,93,0,0,491,492,3,8,4,0,492,493,5,92,0,0,493,
        551,1,0,0,0,494,495,5,63,0,0,495,496,5,91,0,0,496,497,3,8,4,0,497,
        498,5,93,0,0,498,499,3,8,4,0,499,500,5,92,0,0,500,551,1,0,0,0,501,
        502,5,72,0,0,502,503,5,91,0,0,503,504,3,8,4,0,504,505,5,93,0,0,505,
        506,3,8,4,0,506,507,5,92,0,0,507,551,1,0,0,0,508,509,5,73,0,0,509,
        510,5,91,0,0,510,511,3,8,4,0,511,512,5,93,0,0,512,513,3,8,4,0,513,
        514,5,92,0,0,514,551,1,0,0,0,515,516,5,74,0,0,516,517,5,91,0,0,517,
        518,3,8,4,0,518,519,5,93,0,0,519,520,3,8,4,0,520,521,5,92,0,0,521,
        551,1,0,0,0,522,523,5,76,0,0,523,524,5,91,0,0,524,525,3,8,4,0,525,
        526,5,93,0,0,526,527,3,8,4,0,527,528,5,92,0,0,528,551,1,0,0,0,529,
        530,5,68,0,0,530,531,5,91,0,0,531,532,3,8,4,0,532,533,5,93,0,0,533,
        534,3,8,4,0,534,535,5,92,0,0,535,551,1,0,0,0,536,537,5,70,0,0,537,
        538,5,91,0,0,538,539,3,8,4,0,539,540,5,93,0,0,540,541,3,8,4,0,541,
        542,5,92,0,0,542,551,1,0,0,0,543,544,5,71,0,0,544,545,5,91,0,0,545,
        546,3,8,4,0,546,547,5,93,0,0,547,548,3,8,4,0,548,549,5,92,0,0,549,
        551,1,0,0,0,550,424,1,0,0,0,550,431,1,0,0,0,550,438,1,0,0,0,550,
        445,1,0,0,0,550,452,1,0,0,0,550,459,1,0,0,0,550,466,1,0,0,0,550,
        473,1,0,0,0,550,480,1,0,0,0,550,487,1,0,0,0,550,494,1,0,0,0,550,
        501,1,0,0,0,550,508,1,0,0,0,550,515,1,0,0,0,550,522,1,0,0,0,550,
        529,1,0,0,0,550,536,1,0,0,0,550,543,1,0,0,0,551,29,1,0,0,0,552,553,
        5,31,0,0,553,554,5,91,0,0,554,555,3,8,4,0,555,556,5,93,0,0,556,557,
        3,8,4,0,557,558,5,93,0,0,558,559,3,8,4,0,559,560,5,92,0,0,560,616,
        1,0,0,0,561,562,5,38,0,0,562,563,5,91,0,0,563,564,3,8,4,0,564,565,
        5,93,0,0,565,566,3,8,4,0,566,567,5,93,0,0,567,568,3,8,4,0,568,569,
        5,92,0,0,569,616,1,0,0,0,570,571,5,40,0,0,571,572,5,91,0,0,572,573,
        3,8,4,0,573,574,5,93,0,0,574,575,3,8,4,0,575,576,5,93,0,0,576,577,
        3,8,4,0,577,578,5,92,0,0,578,616,1,0,0,0,579,580,5,52,0,0,580,581,
        5,91,0,0,581,582,3,8,4,0,582,583,5,93,0,0,583,584,3,8,4,0,584,585,
        5,93,0,0,585,586,3,8,4,0,586,587,5,92,0,0,587,616,1,0,0,0,588,589,
        5,64,0,0,589,590,5,91,0,0,590,591,3,8,4,0,591,592,5,93,0,0,592,593,
        3,8,4,0,593,594,5,93,0,0,594,595,3,8,4,0,595,596,5,92,0,0,596,616,
        1,0,0,0,597,598,5,67,0,0,598,599,5,91,0,0,599,600,3,8,4,0,600,601,
        5,93,0,0,601,602,3,8,4,0,602,603,5,93,0,0,603,604,3,8,4,0,604,605,
        5,92,0,0,605,616,1,0,0,0,606,607,5,69,0,0,607,608,5,91,0,0,608,609,
        3,8,4,0,609,610,5,93,0,0,610,611,3,8,4,0,611,612,5,93,0,0,612,613,
        3,8,4,0,613,614,5,92,0,0,614,616,1,0,0,0,615,552,1,0,0,0,615,561,
        1,0,0,0,615,570,1,0,0,0,615,579,1,0,0,0,615,588,1,0,0,0,615,597,
        1,0,0,0,615,606,1,0,0,0,616,31,1,0,0,0,617,618,5,49,0,0,618,619,
        5,91,0,0,619,620,3,8,4,0,620,621,5,93,0,0,621,622,3,8,4,0,622,623,
        5,93,0,0,623,624,3,8,4,0,624,625,5,93,0,0,625,626,3,8,4,0,626,627,
        5,92,0,0,627,640,1,0,0,0,628,629,5,37,0,0,629,630,5,91,0,0,630,631,
        3,8,4,0,631,632,5,93,0,0,632,633,3,8,4,0,633,634,5,93,0,0,634,635,
        3,8,4,0,635,636,5,93,0,0,636,637,3,8,4,0,637,638,5,92,0,0,638,640,
        1,0,0,0,639,617,1,0,0,0,639,628,1,0,0,0,640,33,1,0,0,0,641,642,5,
        19,0,0,642,643,5,91,0,0,643,648,3,8,4,0,644,645,5,93,0,0,645,647,
        3,8,4,0,646,644,1,0,0,0,647,650,1,0,0,0,648,646,1,0,0,0,648,649,
        1,0,0,0,649,651,1,0,0,0,650,648,1,0,0,0,651,652,5,92,0,0,652,713,
        1,0,0,0,653,654,5,20,0,0,654,655,5,91,0,0,655,660,3,8,4,0,656,657,
        5,93,0,0,657,659,3,8,4,0,658,656,1,0,0,0,659,662,1,0,0,0,660,658,
        1,0,0,0,660,661,1,0,0,0,661,663,1,0,0,0,662,660,1,0,0,0,663,664,
        5,92,0,0,664,713,1,0,0,0,665,666,5,46,0,0,666,667,5,91,0,0,667,670,
        3,8,4,0,668,669,5,93,0,0,669,671,3,8,4,0,670,668,1,0,0,0,671,672,
        1,0,0,0,672,670,1,0,0,0,672,673,1,0,0,0,673,674,1,0,0,0,674,675,
        5,92,0,0,675,713,1,0,0,0,676,677,5,47,0,0,677,678,5,91,0,0,678,681,
        3,8,4,0,679,680,5,93,0,0,680,682,3,8,4,0,681,679,1,0,0,0,682,683,
        1,0,0,0,683,681,1,0,0,0,683,684,1,0,0,0,684,685,1,0,0,0,685,686,
        5,92,0,0,686,713,1,0,0,0,687,688,5,48,0,0,688,689,5,91,0,0,689,692,
        3,8,4,0,690,691,5,93,0,0,691,693,3,8,4,0,692,690,1,0,0,0,693,694,
        1,0,0,0,694,692,1,0,0,0,694,695,1,0,0,0,695,696,1,0,0,0,696,697,
        5,92,0,0,697,713,1,0,0,0,698,699,5,50,0,0,699,700,5,91,0,0,700,701,
        3,8,4,0,701,702,5,93,0,0,702,703,3,8,4,0,703,704,5,92,0,0,704,713,
        1,0,0,0,705,706,5,51,0,0,706,707,5,91,0,0,707,708,3,8,4,0,708,709,
        5,93,0,0,709,710,3,8,4,0,710,711,5,92,0,0,711,713,1,0,0,0,712,641,
        1,0,0,0,712,653,1,0,0,0,712,665,1,0,0,0,712,676,1,0,0,0,712,687,
        1,0,0,0,712,698,1,0,0,0,712,705,1,0,0,0,713,35,1,0,0,0,29,39,45,
        54,71,76,99,101,113,115,130,132,140,147,159,166,191,199,202,209,
        422,550,615,639,648,660,672,683,694,712
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
                     "<INVALID>", "'lerp'", "'step'", "'smoothstep'", "'fract'", 
                     "'relu'", "'softplus'", "'gelu'", "'sign'", "'map'", 
                     "<INVALID>", "<INVALID>", "'swap'", "<INVALID>", "<INVALID>", 
                     "'range'", "'topk'", "'botk'", "'pinv'", "'sum'", "'mean'", 
                     "'std'", "'var'", "<INVALID>", "<INVALID>", "'quantile'", 
                     "'dot'", "'moment'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'cossim'", "'flip'", "'cov'", "'sort'", "'append'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'>='", "'>'", 
                     "'<='", "'<'", "'=='", "'='", "'!='", "'|'", "'('", 
                     "')'", "','", "';'", "'->'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "SIN", "COS", "TAN", "ASIN", "ACOS", 
                      "ATAN", "ATAN2", "SINH", "COSH", "TANH", "ASINH", 
                      "ACOSH", "ATANH", "ABS", "SQRT", "LN", "LOG", "EXP", 
                      "SMIN", "SMAX", "TMIN", "TMAX", "TNORM", "SNORM", 
                      "FLOOR", "CEIL", "ROUND", "GAMMA", "POWE", "SIGM", 
                      "CLAMP", "SFFT", "SIFFT", "ANGL", "PRNT", "PRINT_SHAPE", 
                      "NVL", "LERP", "STEP", "SMOOTHSTEP", "FRACT", "RELU", 
                      "SOFTPLUS", "GELU", "SIGN", "MAP", "EZCONV", "CONV", 
                      "SWAP", "PERM", "RESHAPE", "RANGE", "TOPK", "BOTK", 
                      "PINV", "SUM", "MEAN", "STD", "VAR", "QUARTILE", "PERCENTILE", 
                      "QUANTILE", "DOT", "MOMENT", "NOISE", "RAND", "CAUCHY", 
                      "EXPONENTIAL", "LOGNORMAL", "BERNOULLI", "POISSON", 
                      "COSSIM", "FLIP", "COV", "SORT", "APPEND", "PLUS", 
                      "MINUS", "MULT", "DIV", "MOD", "POW", "GE", "GT", 
                      "LE", "LT", "EQ", "EQUEALS", "NE", "PIPE", "LPAREN", 
                      "RPAREN", "COMMA", "SEMICOLON", "ARROW", "LBRACKET", 
                      "RBRACKET", "CONSTANT", "NUMBER", "VARIABLE", "WS" ]

    RULE_start = 0
    RULE_funcDef = 1
    RULE_varDef = 2
    RULE_paramList = 3
    RULE_expr = 4
    RULE_compExpr = 5
    RULE_addExpr = 6
    RULE_mulExpr = 7
    RULE_powExpr = 8
    RULE_unaryExpr = 9
    RULE_indexExpr = 10
    RULE_atom = 11
    RULE_exprList = 12
    RULE_func1 = 13
    RULE_func2 = 14
    RULE_func3 = 15
    RULE_func4 = 16
    RULE_funcN = 17

    ruleNames =  [ "start", "funcDef", "varDef", "paramList", "expr", "compExpr", 
                   "addExpr", "mulExpr", "powExpr", "unaryExpr", "indexExpr", 
                   "atom", "exprList", "func1", "func2", "func3", "func4", 
                   "funcN" ]

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
    NVL=37
    LERP=38
    STEP=39
    SMOOTHSTEP=40
    FRACT=41
    RELU=42
    SOFTPLUS=43
    GELU=44
    SIGN=45
    MAP=46
    EZCONV=47
    CONV=48
    SWAP=49
    PERM=50
    RESHAPE=51
    RANGE=52
    TOPK=53
    BOTK=54
    PINV=55
    SUM=56
    MEAN=57
    STD=58
    VAR=59
    QUARTILE=60
    PERCENTILE=61
    QUANTILE=62
    DOT=63
    MOMENT=64
    NOISE=65
    RAND=66
    CAUCHY=67
    EXPONENTIAL=68
    LOGNORMAL=69
    BERNOULLI=70
    POISSON=71
    COSSIM=72
    FLIP=73
    COV=74
    SORT=75
    APPEND=76
    PLUS=77
    MINUS=78
    MULT=79
    DIV=80
    MOD=81
    POW=82
    GE=83
    GT=84
    LE=85
    LT=86
    EQ=87
    EQUEALS=88
    NE=89
    PIPE=90
    LPAREN=91
    RPAREN=92
    COMMA=93
    SEMICOLON=94
    ARROW=95
    LBRACKET=96
    RBRACKET=97
    CONSTANT=98
    NUMBER=99
    VARIABLE=100
    WS=101

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(MathExprParser.EOF, 0)

        def funcDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.FuncDefContext)
            else:
                return self.getTypedRuleContext(MathExprParser.FuncDefContext,i)


        def varDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.VarDefContext)
            else:
                return self.getTypedRuleContext(MathExprParser.VarDefContext,i)


        def getRuleIndex(self):
            return MathExprParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = MathExprParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 36
                    self.funcDef() 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 42
                    self.varDef() 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 48
            self.expr()
            self.state = 49
            self.match(MathExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_funcDef


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionDefContext(FuncDefContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncDefContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MathExprParser.VARIABLE, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)
        def ARROW(self):
            return self.getToken(MathExprParser.ARROW, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def SEMICOLON(self):
            return self.getToken(MathExprParser.SEMICOLON, 0)
        def paramList(self):
            return self.getTypedRuleContext(MathExprParser.ParamListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDef" ):
                return visitor.visitFunctionDef(self)
            else:
                return visitor.visitChildren(self)



    def funcDef(self):

        localctx = MathExprParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            localctx = MathExprParser.FunctionDefContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MathExprParser.VARIABLE)
            self.state = 52
            self.match(MathExprParser.LPAREN)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==100:
                self.state = 53
                self.paramList()


            self.state = 56
            self.match(MathExprParser.RPAREN)
            self.state = 57
            self.match(MathExprParser.ARROW)
            self.state = 58
            self.expr()
            self.state = 59
            self.match(MathExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(MathExprParser.VARIABLE, 0)

        def EQUEALS(self):
            return self.getToken(MathExprParser.EQUEALS, 0)

        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MathExprParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MathExprParser.RULE_varDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDef" ):
                listener.enterVarDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDef" ):
                listener.exitVarDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDef" ):
                return visitor.visitVarDef(self)
            else:
                return visitor.visitChildren(self)




    def varDef(self):

        localctx = MathExprParser.VarDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(MathExprParser.VARIABLE)
            self.state = 62
            self.match(MathExprParser.EQUEALS)
            self.state = 63
            self.expr()
            self.state = 64
            self.match(MathExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.VARIABLE)
            else:
                return self.getToken(MathExprParser.VARIABLE, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathExprParser.COMMA)
            else:
                return self.getToken(MathExprParser.COMMA, i)

        def getRuleIndex(self):
            return MathExprParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MathExprParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(MathExprParser.VARIABLE)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==93:
                self.state = 67
                self.match(MathExprParser.COMMA)
                self.state = 68
                self.match(MathExprParser.VARIABLE)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_compExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToAddContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 79
            self.addExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 99
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.GtExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 81
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 82
                        self.match(MathExprParser.GT)
                        self.state = 83
                        self.addExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.GeExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 84
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 85
                        self.match(MathExprParser.GE)
                        self.state = 86
                        self.addExpr(0)
                        pass

                    elif la_ == 3:
                        localctx = MathExprParser.LtExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 87
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 88
                        self.match(MathExprParser.LT)
                        self.state = 89
                        self.addExpr(0)
                        pass

                    elif la_ == 4:
                        localctx = MathExprParser.LeExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 90
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 91
                        self.match(MathExprParser.LE)
                        self.state = 92
                        self.addExpr(0)
                        pass

                    elif la_ == 5:
                        localctx = MathExprParser.EqExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 93
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 94
                        self.match(MathExprParser.EQ)
                        self.state = 95
                        self.addExpr(0)
                        pass

                    elif la_ == 6:
                        localctx = MathExprParser.NeExpContext(self, MathExprParser.CompExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compExpr)
                        self.state = 96
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 97
                        self.match(MathExprParser.NE)
                        self.state = 98
                        self.addExpr(0)
                        pass


                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_addExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToMulContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 105
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 113
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.AddExpContext(self, MathExprParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 107
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 108
                        self.match(MathExprParser.PLUS)
                        self.state = 109
                        self.mulExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.SubExpContext(self, MathExprParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 110
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 111
                        self.match(MathExprParser.MINUS)
                        self.state = 112
                        self.mulExpr(0)
                        pass


                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_mulExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToPowContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 119
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 130
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.MulExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 121
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 122
                        self.match(MathExprParser.MULT)
                        self.state = 123
                        self.powExpr()
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.DivExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 124
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 125
                        self.match(MathExprParser.DIV)
                        self.state = 126
                        self.powExpr()
                        pass

                    elif la_ == 3:
                        localctx = MathExprParser.ModExpContext(self, MathExprParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 127
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 128
                        self.match(MathExprParser.MOD)
                        self.state = 129
                        self.powExpr()
                        pass


                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_powExpr)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = MathExprParser.PowExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.unaryExpr()
                self.state = 136
                self.match(MathExprParser.POW)
                self.state = 137
                self.powExpr()
                pass

            elif la_ == 2:
                localctx = MathExprParser.ToUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 139
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
        self.enterRule(localctx, 18, self.RULE_unaryExpr)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [77]:
                localctx = MathExprParser.UnaryPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(MathExprParser.PLUS)
                self.state = 143
                self.unaryExpr()
                pass
            elif token in [78]:
                localctx = MathExprParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(MathExprParser.MINUS)
                self.state = 145
                self.unaryExpr()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 90, 91, 96, 98, 99, 100]:
                localctx = MathExprParser.ToIndexContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 146
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_indexExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MathExprParser.ToAtomContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 150
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MathExprParser.IndexExpContext(self, MathExprParser.IndexExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indexExpr)
                    self.state = 152
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 153
                    self.match(MathExprParser.LBRACKET)
                    self.state = 154
                    self.expr()
                    self.state = 159
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==93:
                        self.state = 155
                        self.match(MathExprParser.COMMA)
                        self.state = 156
                        self.expr()
                        self.state = 161
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 162
                    self.match(MathExprParser.RBRACKET) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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


    class CallExpContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MathExprParser.VARIABLE, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)
        def exprList(self):
            return self.getTypedRuleContext(MathExprParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExp" ):
                listener.enterCallExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExp" ):
                listener.exitCallExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExp" ):
                return visitor.visitCallExp(self)
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
        self.enterRule(localctx, 22, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = MathExprParser.Func1ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.func1()
                pass

            elif la_ == 2:
                localctx = MathExprParser.Func2ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.func2()
                pass

            elif la_ == 3:
                localctx = MathExprParser.Func3ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.func3()
                pass

            elif la_ == 4:
                localctx = MathExprParser.Func4ExpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 172
                self.func4()
                pass

            elif la_ == 5:
                localctx = MathExprParser.FuncNExpContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 173
                self.funcN()
                pass

            elif la_ == 6:
                localctx = MathExprParser.VariableExpContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 174
                self.match(MathExprParser.VARIABLE)
                pass

            elif la_ == 7:
                localctx = MathExprParser.NumberExpContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 175
                self.match(MathExprParser.NUMBER)
                pass

            elif la_ == 8:
                localctx = MathExprParser.ConstantExpContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 176
                self.match(MathExprParser.CONSTANT)
                pass

            elif la_ == 9:
                localctx = MathExprParser.ParenExpContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 177
                self.match(MathExprParser.LPAREN)
                self.state = 178
                self.expr()
                self.state = 179
                self.match(MathExprParser.RPAREN)
                pass

            elif la_ == 10:
                localctx = MathExprParser.AbsExpContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 181
                self.match(MathExprParser.PIPE)
                self.state = 182
                self.expr()
                self.state = 183
                self.match(MathExprParser.PIPE)
                pass

            elif la_ == 11:
                localctx = MathExprParser.ListExpContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 185
                self.match(MathExprParser.LBRACKET)
                self.state = 186
                self.expr()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==93:
                    self.state = 187
                    self.match(MathExprParser.COMMA)
                    self.state = 188
                    self.expr()
                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 194
                self.match(MathExprParser.RBRACKET)
                pass

            elif la_ == 12:
                localctx = MathExprParser.CallExpContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 196
                self.match(MathExprParser.VARIABLE)
                self.state = 197
                self.match(MathExprParser.LPAREN)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -2) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 124755410943) != 0):
                    self.state = 198
                    self.exprList()


                self.state = 201
                self.match(MathExprParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return MathExprParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = MathExprParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.expr()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==93:
                self.state = 205
                self.match(MathExprParser.COMMA)
                self.state = 206
                self.expr()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


    class SortFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def SORT(self):
            return self.getToken(MathExprParser.SORT, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSortFunc" ):
                listener.enterSortFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSortFunc" ):
                listener.exitSortFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSortFunc" ):
                return visitor.visitSortFunc(self)
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


    class NoiseFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOISE(self):
            return self.getToken(MathExprParser.NOISE, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoiseFunc" ):
                listener.enterNoiseFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoiseFunc" ):
                listener.exitNoiseFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoiseFunc" ):
                return visitor.visitNoiseFunc(self)
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


    class RandFuncContext(Func1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def RAND(self):
            return self.getToken(MathExprParser.RAND, 0)
        def LPAREN(self):
            return self.getToken(MathExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRandFunc" ):
                listener.enterRandFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRandFunc" ):
                listener.exitRandFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandFunc" ):
                return visitor.visitRandFunc(self)
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
        self.enterRule(localctx, 26, self.RULE_func1)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = MathExprParser.SinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(MathExprParser.SIN)
                self.state = 213
                self.match(MathExprParser.LPAREN)
                self.state = 214
                self.expr()
                self.state = 215
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [2]:
                localctx = MathExprParser.CosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(MathExprParser.COS)
                self.state = 218
                self.match(MathExprParser.LPAREN)
                self.state = 219
                self.expr()
                self.state = 220
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [3]:
                localctx = MathExprParser.TanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.match(MathExprParser.TAN)
                self.state = 223
                self.match(MathExprParser.LPAREN)
                self.state = 224
                self.expr()
                self.state = 225
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [4]:
                localctx = MathExprParser.AsinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 227
                self.match(MathExprParser.ASIN)
                self.state = 228
                self.match(MathExprParser.LPAREN)
                self.state = 229
                self.expr()
                self.state = 230
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [5]:
                localctx = MathExprParser.AcosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 232
                self.match(MathExprParser.ACOS)
                self.state = 233
                self.match(MathExprParser.LPAREN)
                self.state = 234
                self.expr()
                self.state = 235
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [6]:
                localctx = MathExprParser.AtanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 237
                self.match(MathExprParser.ATAN)
                self.state = 238
                self.match(MathExprParser.LPAREN)
                self.state = 239
                self.expr()
                self.state = 240
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [8]:
                localctx = MathExprParser.SinhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 242
                self.match(MathExprParser.SINH)
                self.state = 243
                self.match(MathExprParser.LPAREN)
                self.state = 244
                self.expr()
                self.state = 245
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [9]:
                localctx = MathExprParser.CoshFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 247
                self.match(MathExprParser.COSH)
                self.state = 248
                self.match(MathExprParser.LPAREN)
                self.state = 249
                self.expr()
                self.state = 250
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [10]:
                localctx = MathExprParser.TanhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 252
                self.match(MathExprParser.TANH)
                self.state = 253
                self.match(MathExprParser.LPAREN)
                self.state = 254
                self.expr()
                self.state = 255
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [11]:
                localctx = MathExprParser.AsinhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 257
                self.match(MathExprParser.ASINH)
                self.state = 258
                self.match(MathExprParser.LPAREN)
                self.state = 259
                self.expr()
                self.state = 260
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [12]:
                localctx = MathExprParser.AcoshFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 262
                self.match(MathExprParser.ACOSH)
                self.state = 263
                self.match(MathExprParser.LPAREN)
                self.state = 264
                self.expr()
                self.state = 265
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [13]:
                localctx = MathExprParser.AtanhFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 267
                self.match(MathExprParser.ATANH)
                self.state = 268
                self.match(MathExprParser.LPAREN)
                self.state = 269
                self.expr()
                self.state = 270
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [14]:
                localctx = MathExprParser.AbsFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 272
                self.match(MathExprParser.ABS)
                self.state = 273
                self.match(MathExprParser.LPAREN)
                self.state = 274
                self.expr()
                self.state = 275
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [15]:
                localctx = MathExprParser.SqrtFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 277
                self.match(MathExprParser.SQRT)
                self.state = 278
                self.match(MathExprParser.LPAREN)
                self.state = 279
                self.expr()
                self.state = 280
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [16]:
                localctx = MathExprParser.LnFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 282
                self.match(MathExprParser.LN)
                self.state = 283
                self.match(MathExprParser.LPAREN)
                self.state = 284
                self.expr()
                self.state = 285
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [17]:
                localctx = MathExprParser.LogFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 287
                self.match(MathExprParser.LOG)
                self.state = 288
                self.match(MathExprParser.LPAREN)
                self.state = 289
                self.expr()
                self.state = 290
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [18]:
                localctx = MathExprParser.ExpFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 292
                self.match(MathExprParser.EXP)
                self.state = 293
                self.match(MathExprParser.LPAREN)
                self.state = 294
                self.expr()
                self.state = 295
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [23]:
                localctx = MathExprParser.TNormFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 297
                self.match(MathExprParser.TNORM)
                self.state = 298
                self.match(MathExprParser.LPAREN)
                self.state = 299
                self.expr()
                self.state = 300
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [24]:
                localctx = MathExprParser.SNormFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 302
                self.match(MathExprParser.SNORM)
                self.state = 303
                self.match(MathExprParser.LPAREN)
                self.state = 304
                self.expr()
                self.state = 305
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [25]:
                localctx = MathExprParser.FloorFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 20)
                self.state = 307
                self.match(MathExprParser.FLOOR)
                self.state = 308
                self.match(MathExprParser.LPAREN)
                self.state = 309
                self.expr()
                self.state = 310
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [26]:
                localctx = MathExprParser.CeilFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 21)
                self.state = 312
                self.match(MathExprParser.CEIL)
                self.state = 313
                self.match(MathExprParser.LPAREN)
                self.state = 314
                self.expr()
                self.state = 315
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [27]:
                localctx = MathExprParser.RoundFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 22)
                self.state = 317
                self.match(MathExprParser.ROUND)
                self.state = 318
                self.match(MathExprParser.LPAREN)
                self.state = 319
                self.expr()
                self.state = 320
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [28]:
                localctx = MathExprParser.GammaFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 23)
                self.state = 322
                self.match(MathExprParser.GAMMA)
                self.state = 323
                self.match(MathExprParser.LPAREN)
                self.state = 324
                self.expr()
                self.state = 325
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [30]:
                localctx = MathExprParser.SigmoidFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 24)
                self.state = 327
                self.match(MathExprParser.SIGM)
                self.state = 328
                self.match(MathExprParser.LPAREN)
                self.state = 329
                self.expr()
                self.state = 330
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [32]:
                localctx = MathExprParser.SfftFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 25)
                self.state = 332
                self.match(MathExprParser.SFFT)
                self.state = 333
                self.match(MathExprParser.LPAREN)
                self.state = 334
                self.expr()
                self.state = 335
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [33]:
                localctx = MathExprParser.SifftFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 26)
                self.state = 337
                self.match(MathExprParser.SIFFT)
                self.state = 338
                self.match(MathExprParser.LPAREN)
                self.state = 339
                self.expr()
                self.state = 340
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [34]:
                localctx = MathExprParser.AnglFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 27)
                self.state = 342
                self.match(MathExprParser.ANGL)
                self.state = 343
                self.match(MathExprParser.LPAREN)
                self.state = 344
                self.expr()
                self.state = 345
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [35]:
                localctx = MathExprParser.PrintFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 28)
                self.state = 347
                self.match(MathExprParser.PRNT)
                self.state = 348
                self.match(MathExprParser.LPAREN)
                self.state = 349
                self.expr()
                self.state = 350
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [41]:
                localctx = MathExprParser.FractFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 29)
                self.state = 352
                self.match(MathExprParser.FRACT)
                self.state = 353
                self.match(MathExprParser.LPAREN)
                self.state = 354
                self.expr()
                self.state = 355
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [42]:
                localctx = MathExprParser.ReluFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 30)
                self.state = 357
                self.match(MathExprParser.RELU)
                self.state = 358
                self.match(MathExprParser.LPAREN)
                self.state = 359
                self.expr()
                self.state = 360
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [43]:
                localctx = MathExprParser.SoftplusFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 31)
                self.state = 362
                self.match(MathExprParser.SOFTPLUS)
                self.state = 363
                self.match(MathExprParser.LPAREN)
                self.state = 364
                self.expr()
                self.state = 365
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [44]:
                localctx = MathExprParser.GeluFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 32)
                self.state = 367
                self.match(MathExprParser.GELU)
                self.state = 368
                self.match(MathExprParser.LPAREN)
                self.state = 369
                self.expr()
                self.state = 370
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [45]:
                localctx = MathExprParser.SignFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 33)
                self.state = 372
                self.match(MathExprParser.SIGN)
                self.state = 373
                self.match(MathExprParser.LPAREN)
                self.state = 374
                self.expr()
                self.state = 375
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [36]:
                localctx = MathExprParser.PrintShapeFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 34)
                self.state = 377
                self.match(MathExprParser.PRINT_SHAPE)
                self.state = 378
                self.match(MathExprParser.LPAREN)
                self.state = 379
                self.expr()
                self.state = 380
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [55]:
                localctx = MathExprParser.PinvFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 35)
                self.state = 382
                self.match(MathExprParser.PINV)
                self.state = 383
                self.match(MathExprParser.LPAREN)
                self.state = 384
                self.expr()
                self.state = 385
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [56]:
                localctx = MathExprParser.SumFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 36)
                self.state = 387
                self.match(MathExprParser.SUM)
                self.state = 388
                self.match(MathExprParser.LPAREN)
                self.state = 389
                self.expr()
                self.state = 390
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [57]:
                localctx = MathExprParser.MeanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 37)
                self.state = 392
                self.match(MathExprParser.MEAN)
                self.state = 393
                self.match(MathExprParser.LPAREN)
                self.state = 394
                self.expr()
                self.state = 395
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [58]:
                localctx = MathExprParser.StdFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 38)
                self.state = 397
                self.match(MathExprParser.STD)
                self.state = 398
                self.match(MathExprParser.LPAREN)
                self.state = 399
                self.expr()
                self.state = 400
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [59]:
                localctx = MathExprParser.VarFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 39)
                self.state = 402
                self.match(MathExprParser.VAR)
                self.state = 403
                self.match(MathExprParser.LPAREN)
                self.state = 404
                self.expr()
                self.state = 405
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [75]:
                localctx = MathExprParser.SortFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 40)
                self.state = 407
                self.match(MathExprParser.SORT)
                self.state = 408
                self.match(MathExprParser.LPAREN)
                self.state = 409
                self.expr()
                self.state = 410
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [65]:
                localctx = MathExprParser.NoiseFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 41)
                self.state = 412
                self.match(MathExprParser.NOISE)
                self.state = 413
                self.match(MathExprParser.LPAREN)
                self.state = 414
                self.expr()
                self.state = 415
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [66]:
                localctx = MathExprParser.RandFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 42)
                self.state = 417
                self.match(MathExprParser.RAND)
                self.state = 418
                self.match(MathExprParser.LPAREN)
                self.state = 419
                self.expr()
                self.state = 420
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


    class ExponentialFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXPONENTIAL(self):
            return self.getToken(MathExprParser.EXPONENTIAL, 0)
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
            if hasattr( listener, "enterExponentialFunc" ):
                listener.enterExponentialFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponentialFunc" ):
                listener.exitExponentialFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponentialFunc" ):
                return visitor.visitExponentialFunc(self)
            else:
                return visitor.visitChildren(self)


    class PoissonFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def POISSON(self):
            return self.getToken(MathExprParser.POISSON, 0)
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
            if hasattr( listener, "enterPoissonFunc" ):
                listener.enterPoissonFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoissonFunc" ):
                listener.exitPoissonFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPoissonFunc" ):
                return visitor.visitPoissonFunc(self)
            else:
                return visitor.visitChildren(self)


    class CovFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def COV(self):
            return self.getToken(MathExprParser.COV, 0)
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
            if hasattr( listener, "enterCovFunc" ):
                listener.enterCovFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCovFunc" ):
                listener.exitCovFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCovFunc" ):
                return visitor.visitCovFunc(self)
            else:
                return visitor.visitChildren(self)


    class BernoulliFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def BERNOULLI(self):
            return self.getToken(MathExprParser.BERNOULLI, 0)
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
            if hasattr( listener, "enterBernoulliFunc" ):
                listener.enterBernoulliFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBernoulliFunc" ):
                listener.exitBernoulliFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBernoulliFunc" ):
                return visitor.visitBernoulliFunc(self)
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


    class CossimFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def COSSIM(self):
            return self.getToken(MathExprParser.COSSIM, 0)
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
            if hasattr( listener, "enterCossimFunc" ):
                listener.enterCossimFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCossimFunc" ):
                listener.exitCossimFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCossimFunc" ):
                return visitor.visitCossimFunc(self)
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


    class AppendFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def APPEND(self):
            return self.getToken(MathExprParser.APPEND, 0)
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
            if hasattr( listener, "enterAppendFunc" ):
                listener.enterAppendFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAppendFunc" ):
                listener.exitAppendFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAppendFunc" ):
                return visitor.visitAppendFunc(self)
            else:
                return visitor.visitChildren(self)


    class FlipFuncContext(Func2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLIP(self):
            return self.getToken(MathExprParser.FLIP, 0)
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
            if hasattr( listener, "enterFlipFunc" ):
                listener.enterFlipFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlipFunc" ):
                listener.exitFlipFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlipFunc" ):
                return visitor.visitFlipFunc(self)
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
        self.enterRule(localctx, 28, self.RULE_func2)
        try:
            self.state = 550
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = MathExprParser.PowFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(MathExprParser.POWE)
                self.state = 425
                self.match(MathExprParser.LPAREN)
                self.state = 426
                self.expr()
                self.state = 427
                self.match(MathExprParser.COMMA)
                self.state = 428
                self.expr()
                self.state = 429
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [7]:
                localctx = MathExprParser.Atan2FuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.match(MathExprParser.ATAN2)
                self.state = 432
                self.match(MathExprParser.LPAREN)
                self.state = 433
                self.expr()
                self.state = 434
                self.match(MathExprParser.COMMA)
                self.state = 435
                self.expr()
                self.state = 436
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [21]:
                localctx = MathExprParser.TMinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.match(MathExprParser.TMIN)
                self.state = 439
                self.match(MathExprParser.LPAREN)
                self.state = 440
                self.expr()
                self.state = 441
                self.match(MathExprParser.COMMA)
                self.state = 442
                self.expr()
                self.state = 443
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [22]:
                localctx = MathExprParser.TMaxFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 445
                self.match(MathExprParser.TMAX)
                self.state = 446
                self.match(MathExprParser.LPAREN)
                self.state = 447
                self.expr()
                self.state = 448
                self.match(MathExprParser.COMMA)
                self.state = 449
                self.expr()
                self.state = 450
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [39]:
                localctx = MathExprParser.StepFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 452
                self.match(MathExprParser.STEP)
                self.state = 453
                self.match(MathExprParser.LPAREN)
                self.state = 454
                self.expr()
                self.state = 455
                self.match(MathExprParser.COMMA)
                self.state = 456
                self.expr()
                self.state = 457
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [53]:
                localctx = MathExprParser.TopkFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 459
                self.match(MathExprParser.TOPK)
                self.state = 460
                self.match(MathExprParser.LPAREN)
                self.state = 461
                self.expr()
                self.state = 462
                self.match(MathExprParser.COMMA)
                self.state = 463
                self.expr()
                self.state = 464
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [54]:
                localctx = MathExprParser.BotkFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 466
                self.match(MathExprParser.BOTK)
                self.state = 467
                self.match(MathExprParser.LPAREN)
                self.state = 468
                self.expr()
                self.state = 469
                self.match(MathExprParser.COMMA)
                self.state = 470
                self.expr()
                self.state = 471
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [60]:
                localctx = MathExprParser.QuartileFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 473
                self.match(MathExprParser.QUARTILE)
                self.state = 474
                self.match(MathExprParser.LPAREN)
                self.state = 475
                self.expr()
                self.state = 476
                self.match(MathExprParser.COMMA)
                self.state = 477
                self.expr()
                self.state = 478
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [61]:
                localctx = MathExprParser.PercentileFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 480
                self.match(MathExprParser.PERCENTILE)
                self.state = 481
                self.match(MathExprParser.LPAREN)
                self.state = 482
                self.expr()
                self.state = 483
                self.match(MathExprParser.COMMA)
                self.state = 484
                self.expr()
                self.state = 485
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [62]:
                localctx = MathExprParser.QuantileFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 487
                self.match(MathExprParser.QUANTILE)
                self.state = 488
                self.match(MathExprParser.LPAREN)
                self.state = 489
                self.expr()
                self.state = 490
                self.match(MathExprParser.COMMA)
                self.state = 491
                self.expr()
                self.state = 492
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [63]:
                localctx = MathExprParser.DotFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 494
                self.match(MathExprParser.DOT)
                self.state = 495
                self.match(MathExprParser.LPAREN)
                self.state = 496
                self.expr()
                self.state = 497
                self.match(MathExprParser.COMMA)
                self.state = 498
                self.expr()
                self.state = 499
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [72]:
                localctx = MathExprParser.CossimFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 501
                self.match(MathExprParser.COSSIM)
                self.state = 502
                self.match(MathExprParser.LPAREN)
                self.state = 503
                self.expr()
                self.state = 504
                self.match(MathExprParser.COMMA)
                self.state = 505
                self.expr()
                self.state = 506
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [73]:
                localctx = MathExprParser.FlipFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 508
                self.match(MathExprParser.FLIP)
                self.state = 509
                self.match(MathExprParser.LPAREN)
                self.state = 510
                self.expr()
                self.state = 511
                self.match(MathExprParser.COMMA)
                self.state = 512
                self.expr()
                self.state = 513
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [74]:
                localctx = MathExprParser.CovFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 515
                self.match(MathExprParser.COV)
                self.state = 516
                self.match(MathExprParser.LPAREN)
                self.state = 517
                self.expr()
                self.state = 518
                self.match(MathExprParser.COMMA)
                self.state = 519
                self.expr()
                self.state = 520
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [76]:
                localctx = MathExprParser.AppendFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 522
                self.match(MathExprParser.APPEND)
                self.state = 523
                self.match(MathExprParser.LPAREN)
                self.state = 524
                self.expr()
                self.state = 525
                self.match(MathExprParser.COMMA)
                self.state = 526
                self.expr()
                self.state = 527
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [68]:
                localctx = MathExprParser.ExponentialFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 529
                self.match(MathExprParser.EXPONENTIAL)
                self.state = 530
                self.match(MathExprParser.LPAREN)
                self.state = 531
                self.expr()
                self.state = 532
                self.match(MathExprParser.COMMA)
                self.state = 533
                self.expr()
                self.state = 534
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [70]:
                localctx = MathExprParser.BernoulliFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 536
                self.match(MathExprParser.BERNOULLI)
                self.state = 537
                self.match(MathExprParser.LPAREN)
                self.state = 538
                self.expr()
                self.state = 539
                self.match(MathExprParser.COMMA)
                self.state = 540
                self.expr()
                self.state = 541
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [71]:
                localctx = MathExprParser.PoissonFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 543
                self.match(MathExprParser.POISSON)
                self.state = 544
                self.match(MathExprParser.LPAREN)
                self.state = 545
                self.expr()
                self.state = 546
                self.match(MathExprParser.COMMA)
                self.state = 547
                self.expr()
                self.state = 548
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


    class CauchyFuncContext(Func3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def CAUCHY(self):
            return self.getToken(MathExprParser.CAUCHY, 0)
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
            if hasattr( listener, "enterCauchyFunc" ):
                listener.enterCauchyFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCauchyFunc" ):
                listener.exitCauchyFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCauchyFunc" ):
                return visitor.visitCauchyFunc(self)
            else:
                return visitor.visitChildren(self)


    class LogNormalFuncContext(Func3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOGNORMAL(self):
            return self.getToken(MathExprParser.LOGNORMAL, 0)
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
            if hasattr( listener, "enterLogNormalFunc" ):
                listener.enterLogNormalFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogNormalFunc" ):
                listener.exitLogNormalFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogNormalFunc" ):
                return visitor.visitLogNormalFunc(self)
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
        self.enterRule(localctx, 30, self.RULE_func3)
        try:
            self.state = 615
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = MathExprParser.ClampFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.match(MathExprParser.CLAMP)
                self.state = 553
                self.match(MathExprParser.LPAREN)
                self.state = 554
                self.expr()
                self.state = 555
                self.match(MathExprParser.COMMA)
                self.state = 556
                self.expr()
                self.state = 557
                self.match(MathExprParser.COMMA)
                self.state = 558
                self.expr()
                self.state = 559
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [38]:
                localctx = MathExprParser.LerpFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 561
                self.match(MathExprParser.LERP)
                self.state = 562
                self.match(MathExprParser.LPAREN)
                self.state = 563
                self.expr()
                self.state = 564
                self.match(MathExprParser.COMMA)
                self.state = 565
                self.expr()
                self.state = 566
                self.match(MathExprParser.COMMA)
                self.state = 567
                self.expr()
                self.state = 568
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [40]:
                localctx = MathExprParser.SmoothstepFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 570
                self.match(MathExprParser.SMOOTHSTEP)
                self.state = 571
                self.match(MathExprParser.LPAREN)
                self.state = 572
                self.expr()
                self.state = 573
                self.match(MathExprParser.COMMA)
                self.state = 574
                self.expr()
                self.state = 575
                self.match(MathExprParser.COMMA)
                self.state = 576
                self.expr()
                self.state = 577
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [52]:
                localctx = MathExprParser.RangeFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 579
                self.match(MathExprParser.RANGE)
                self.state = 580
                self.match(MathExprParser.LPAREN)
                self.state = 581
                self.expr()
                self.state = 582
                self.match(MathExprParser.COMMA)
                self.state = 583
                self.expr()
                self.state = 584
                self.match(MathExprParser.COMMA)
                self.state = 585
                self.expr()
                self.state = 586
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [64]:
                localctx = MathExprParser.MomentFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 588
                self.match(MathExprParser.MOMENT)
                self.state = 589
                self.match(MathExprParser.LPAREN)
                self.state = 590
                self.expr()
                self.state = 591
                self.match(MathExprParser.COMMA)
                self.state = 592
                self.expr()
                self.state = 593
                self.match(MathExprParser.COMMA)
                self.state = 594
                self.expr()
                self.state = 595
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [67]:
                localctx = MathExprParser.CauchyFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 597
                self.match(MathExprParser.CAUCHY)
                self.state = 598
                self.match(MathExprParser.LPAREN)
                self.state = 599
                self.expr()
                self.state = 600
                self.match(MathExprParser.COMMA)
                self.state = 601
                self.expr()
                self.state = 602
                self.match(MathExprParser.COMMA)
                self.state = 603
                self.expr()
                self.state = 604
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [69]:
                localctx = MathExprParser.LogNormalFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 606
                self.match(MathExprParser.LOGNORMAL)
                self.state = 607
                self.match(MathExprParser.LPAREN)
                self.state = 608
                self.expr()
                self.state = 609
                self.match(MathExprParser.COMMA)
                self.state = 610
                self.expr()
                self.state = 611
                self.match(MathExprParser.COMMA)
                self.state = 612
                self.expr()
                self.state = 613
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



    class NvlFuncContext(Func4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.Func4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def NVL(self):
            return self.getToken(MathExprParser.NVL, 0)
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
            if hasattr( listener, "enterNvlFunc" ):
                listener.enterNvlFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNvlFunc" ):
                listener.exitNvlFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNvlFunc" ):
                return visitor.visitNvlFunc(self)
            else:
                return visitor.visitChildren(self)


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
        self.enterRule(localctx, 32, self.RULE_func4)
        try:
            self.state = 639
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                localctx = MathExprParser.SwapFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 617
                self.match(MathExprParser.SWAP)
                self.state = 618
                self.match(MathExprParser.LPAREN)
                self.state = 619
                self.expr()
                self.state = 620
                self.match(MathExprParser.COMMA)
                self.state = 621
                self.expr()
                self.state = 622
                self.match(MathExprParser.COMMA)
                self.state = 623
                self.expr()
                self.state = 624
                self.match(MathExprParser.COMMA)
                self.state = 625
                self.expr()
                self.state = 626
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [37]:
                localctx = MathExprParser.NvlFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 628
                self.match(MathExprParser.NVL)
                self.state = 629
                self.match(MathExprParser.LPAREN)
                self.state = 630
                self.expr()
                self.state = 631
                self.match(MathExprParser.COMMA)
                self.state = 632
                self.expr()
                self.state = 633
                self.match(MathExprParser.COMMA)
                self.state = 634
                self.expr()
                self.state = 635
                self.match(MathExprParser.COMMA)
                self.state = 636
                self.expr()
                self.state = 637
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
        self.enterRule(localctx, 34, self.RULE_funcN)
        self._la = 0 # Token type
        try:
            self.state = 712
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = MathExprParser.SMinFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 641
                self.match(MathExprParser.SMIN)
                self.state = 642
                self.match(MathExprParser.LPAREN)
                self.state = 643
                self.expr()
                self.state = 648
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==93:
                    self.state = 644
                    self.match(MathExprParser.COMMA)
                    self.state = 645
                    self.expr()
                    self.state = 650
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 651
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [20]:
                localctx = MathExprParser.SMaxFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 653
                self.match(MathExprParser.SMAX)
                self.state = 654
                self.match(MathExprParser.LPAREN)
                self.state = 655
                self.expr()
                self.state = 660
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==93:
                    self.state = 656
                    self.match(MathExprParser.COMMA)
                    self.state = 657
                    self.expr()
                    self.state = 662
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 663
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [46]:
                localctx = MathExprParser.MapFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 665
                self.match(MathExprParser.MAP)
                self.state = 666
                self.match(MathExprParser.LPAREN)
                self.state = 667
                self.expr()
                self.state = 670 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 668
                    self.match(MathExprParser.COMMA)
                    self.state = 669
                    self.expr()
                    self.state = 672 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==93):
                        break

                self.state = 674
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [47]:
                localctx = MathExprParser.EzConvFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 676
                self.match(MathExprParser.EZCONV)
                self.state = 677
                self.match(MathExprParser.LPAREN)
                self.state = 678
                self.expr()
                self.state = 681 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 679
                    self.match(MathExprParser.COMMA)
                    self.state = 680
                    self.expr()
                    self.state = 683 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==93):
                        break

                self.state = 685
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [48]:
                localctx = MathExprParser.ConvFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 687
                self.match(MathExprParser.CONV)
                self.state = 688
                self.match(MathExprParser.LPAREN)
                self.state = 689
                self.expr()
                self.state = 692 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 690
                    self.match(MathExprParser.COMMA)
                    self.state = 691
                    self.expr()
                    self.state = 694 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==93):
                        break

                self.state = 696
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [50]:
                localctx = MathExprParser.PermuteFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 698
                self.match(MathExprParser.PERM)
                self.state = 699
                self.match(MathExprParser.LPAREN)
                self.state = 700
                self.expr()
                self.state = 701
                self.match(MathExprParser.COMMA)
                self.state = 702
                self.expr()
                self.state = 703
                self.match(MathExprParser.RPAREN)
                pass
            elif token in [51]:
                localctx = MathExprParser.ReshapeFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 705
                self.match(MathExprParser.RESHAPE)
                self.state = 706
                self.match(MathExprParser.LPAREN)
                self.state = 707
                self.expr()
                self.state = 708
                self.match(MathExprParser.COMMA)
                self.state = 709
                self.expr()
                self.state = 710
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
        self._predicates[5] = self.compExpr_sempred
        self._predicates[6] = self.addExpr_sempred
        self._predicates[7] = self.mulExpr_sempred
        self._predicates[10] = self.indexExpr_sempred
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





