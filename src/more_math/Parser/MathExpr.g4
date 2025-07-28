grammar MathExpr;

// Top-level expression, with operator precedence (lowest to highest)
expr
    : atom | orExpr
    ;

orExpr
    : orExpr OR xorExpr   # OrExp
    | xorExpr             # ToXor
    ;

xorExpr
    : xorExpr XOR andExpr # XorExp
    | andExpr             # ToAnd
    ;

andExpr
    : andExpr AND addExpr # AndExp
    | addExpr             # ToAdd
    ;

addExpr
    : addExpr PLUS mulExpr    # AddExp
    | addExpr MINUS mulExpr   # SubExp
    | mulExpr                 # ToMul
    ;

mulExpr
    : mulExpr MULT powExpr    # MulExp
    | mulExpr DIV powExpr     # DivExp
    | mulExpr MOD powExpr     # ModExp
    | powExpr                 # ToPow
    ;

powExpr
    : unaryExpr POW powExpr   # PowExp
    | unaryExpr               # ToUnary
    ;

unaryExpr
    : PLUS unaryExpr          # UnaryPlus
    | MINUS unaryExpr         # UnaryMinus
    | NOT unaryExpr           # NotExp
    | atom                    # ToAtom
    ;

// Atoms: function calls, variable, number, constant, or parenthesized expression
atom
    : func1                  # Func1Exp
    | func2                  # Func2Exp
    | funcN                  # FuncNExp
    | VARIABLE               # VariableExp
    | NUMBER                 # NumberExp
    | CONSTANT               # ConstantExp
    | '(' expr ')'           # ParenExp
    ;

// Single-argument functions
func1
    : SIN   '(' expr ')'     # SinFunc
    | COS   '(' expr ')'     # CosFunc
    | TAN   '(' expr ')'     # TanFunc
    | ASIN  '(' expr ')'     # AsinFunc
    | ACOS  '(' expr ')'     # AcosFunc
    | ATAN  '(' expr ')'     # AtanFunc
    | SINH  '(' expr ')'     # SinhFunc
    | COSH  '(' expr ')'     # CoshFunc
    | TANH  '(' expr ')'     # TanhFunc
    | ASINH '(' expr ')'     # AsinhFunc
    | ACOSH '(' expr ')'     # AcoshFunc
    | ATANH '(' expr ')'     # AtanhFunc
    | ABS   '(' expr ')'     # AbsFunc
    | SQRT  '(' expr ')'     # SqrtFunc
    | LN    '(' expr ')'     # LnFunc
    | LOG   '(' expr ')'     # LogFunc
    | EXP   '(' expr ')'     # ExpFunc
    | NORM  '(' expr ')'     # NormFunc
    | FLOOR '(' expr ')'     # FloorFunc
    | CEIL  '(' expr ')'     # CeilFunc
    | ROUND '(' expr ')'     # RoundFunc
    | GAMMA '(' expr ')'     # GammaFunc
    ;

// Two-argument functions
func2
    : POW   '(' expr ',' expr ')'   # PowFunc
    | ATAN2 '(' expr ',' expr ')'   # Atan2Func
    ;

// N-argument functions (at least 2 arguments)
funcN
    : MIN   '(' expr (',' expr)+ ')'   # MinFunc
    | MAX   '(' expr (',' expr)+ ')'   # MaxFunc
    ;

// LEXER RULES

SIN   : 'sin';
COS   : 'cos';
TAN   : 'tan';
ASIN  : 'asin';
ACOS  : 'acos';
ATAN  : 'atan';
ATAN2 : 'atan2';
SINH  : 'sinh';
COSH  : 'cosh';
TANH  : 'tanh';
ASINH : 'asinh';
ACOSH : 'acosh';
ATANH : 'atanh';
ABS   : 'abs';
SQRT  : 'sqrt';
LN    : 'ln';
LOG   : 'log';
EXP   : 'exp';
POW   : 'pow';
MIN   : 'min';
MAX   : 'max';
NORM  : 'norm';
FLOOR : 'floor';
CEIL  : 'ceil';
ROUND : 'round';
GAMMA : 'gamma';

PLUS        : '+';
MINUS       : '-';
MULT        : '*';
DIV         : '/';
MOD         : '%';
AND         : '&';
OR          : '|';
XOR         : '^';
NOT         : '!';

CONSTANT : ('pi'|'PI'|'e'|'E');
NUMBER   : [0-9]+ ('.' [0-9]+)?;
VARIABLE : [a-zA-Z_] [a-zA-Z_0-9]*;
WS       : [ \t\r\n]+ -> skip;
