grammar MathExpr;

// Top-level expression, with operator precedence (lowest to highest)
expr
    : atom | addExpr
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
    | atom                    # ToAtom
    ;

// Atoms: function calls, variable, number, constant, or parenthesized expression
atom
    : func1                  # Func1Exp
    | func2                  # Func2Exp
    | func3                  # Func3Exp
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
    | TNORM  '(' expr ')'     # TNormFunc
    | SNORM  '(' expr ')'     # SNormFunc
    | FLOOR '(' expr ')'     # FloorFunc
    | CEIL  '(' expr ')'     # CeilFunc
    | ROUND '(' expr ')'     # RoundFunc
    | GAMMA '(' expr ')'     # GammaFunc
    | SIGM  '(' expr ')'   # sigmoidFunc
    
    ;

// Two-argument functions
func2
    : POWE   '(' expr ',' expr ')'   # PowFunc
    | ATAN2 '(' expr ',' expr ')'   # Atan2Func
    ;
func3
    : CLAMP  '(' expr ',' expr ',' expr ')'   # ClampFunc
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
MIN   : 'min';
MAX   : 'max';
TNORM  : 'tnorm';
SNORM  : 'snorm';
FLOOR : 'floor';
CEIL  : 'ceil';
ROUND : 'round';
GAMMA : 'gamma';
POWE   : 'pow';
SIGM  : 'sigmoid';
CLAMP : 'clamp';

PLUS        : '+';
MINUS       : '-';
MULT        : '*';
DIV         : '/';
MOD         : '%';
POW         : '^';

CONSTANT : ('pi'|'PI'|'e'|'E');
NUMBER   : [0-9]+ ('.' [0-9]+)?;
VARIABLE : [a-zA-Z_] [a-zA-Z_0-9]*;
WS       : [ \t\r\n]+ -> skip;
