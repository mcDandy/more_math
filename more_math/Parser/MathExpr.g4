grammar MathExpr;

// Top-level expression, with operator precedence (lowest to highest)
expr
    : atom | compExpr
    ;

compExpr
    : compExpr GT addExpr # GtExp
    | compExpr GE addExpr # GeExp
    | compExpr LT addExpr # LtExp
    | compExpr LE addExpr # LeExp
    | compExpr EQ addExpr # EqExp
    | compExpr NE addExpr # NeExp
    | addExpr # ToAdd
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
    | func4                  # Func4Exp
    | funcN                  # FuncNExp
    | VARIABLE               # VariableExp
    | NUMBER                 # NumberExp
    | CONSTANT               # ConstantExp
    | '(' expr ')'           # ParenExp
    | PIPE expr PIPE         # AbsExp
    | '[' expr (',' expr)* ']' # ListExp
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
    | TNORM  '(' expr ')'    # TNormFunc
    | SNORM  '(' expr ')'    # SNormFunc
    | FLOOR '(' expr ')'     # FloorFunc
    | CEIL  '(' expr ')'     # CeilFunc
    | ROUND '(' expr ')'     # RoundFunc
    | GAMMA '(' expr ')'     # GammaFunc
    | SIGM  '(' expr ')'     # sigmoidFunc
    | SFFT  '(' expr ')'     # sfftFunc
    | SIFFT  '(' expr ')'    # sifftFunc
    | ANGL  '(' expr ')'     # anglFunc
    | PRNT  '(' expr ')'     # printFunc
    | FRACT '(' expr ')'     # FractFunc
    | RELU  '(' expr ')'     # ReluFunc
    | SOFTPLUS '(' expr ')'  # SoftplusFunc
    | GELU  '(' expr ')'     # GeluFunc
    | SIGN  '(' expr ')'     # SignFunc
    | PRINT_SHAPE    '(' expr ')' # PrintShapeFunc
    | PINV    '(' expr ')'        # PinvFunc
    ;

// Two-argument functions
func2
    : POWE   '(' expr ',' expr ')'   # PowFunc
    | ATAN2 '(' expr ',' expr ')'   # Atan2Func
    | TMIN   '(' expr ',' expr ')'   # TMinFunc
    | TMAX   '(' expr ',' expr ')'   # TMaxFunc
    | STEP   '(' expr ',' expr ')'   # StepFunc
    | TOPK   '(' expr ',' expr ')'   # TopkFunc
    | BOTK   '(' expr ',' expr ')'   # BotkFunc
    ;

func3
    : CLAMP      '(' expr ',' expr ',' expr ')'   # ClampFunc
    | LERP       '(' expr ',' expr ',' expr ')'   # LerpFunc
    | SMOOTHSTEP '(' expr ',' expr ',' expr ')'   # SmoothstepFunc
    | RANGE      '(' expr ',' expr ',' expr ')'   # RangeFunc
    ;

func4
    : SWAP   '(' expr ',' expr ',' expr ',' expr ')'   # SwapFunc
    ;

// N-argument functions
funcN
    : SMIN   '(' expr (',' expr)* ')'   # SMinFunc
    | SMAX   '(' expr (',' expr)* ')'   # SMaxFunc
    | MAP    '(' expr (',' expr)+ ')'   # MapFunc
    | EZCONV '(' expr (',' expr)+ ')'   # EzConvFunc
    | CONV   '(' expr (',' expr)+ ')'   # ConvFunc
    | PERM   '(' expr ',' expr ')'      # PermuteFunc
    | RESHAPE '(' expr ',' expr ')'     # ReshapeFunc
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
SMIN   : 'smin';
SMAX   : 'smax';
TMIN   : 'tmin';
TMAX   : 'tmax';
TNORM  : 'tnorm';
SNORM  : 'snorm';
FLOOR : 'floor';
CEIL  : 'ceil';
ROUND : 'round';
GAMMA : 'gamma';
POWE   : 'pow';
SIGM  : 'sigm';
CLAMP : 'clamp';
SFFT : 'fft';
SIFFT : 'ifft';
ANGL : 'angle';
PRNT : 'print';
PRINT_SHAPE : 'print_shape' | 'pshp';
LERP : 'lerp';
STEP : 'step';
SMOOTHSTEP : 'smoothstep';
FRACT : 'fract';
RELU : 'relu';
SOFTPLUS : 'softplus';
GELU : 'gelu';
SIGN : 'sign';
MAP : 'map';
EZCONV : 'ezconvolution' | 'ezconv';
CONV : 'convolution' | 'conv';
SWAP : 'swap';
PERM : 'permute' | 'perm';
RESHAPE : 'reshape' | 'rshp';
RANGE : 'range';
TOPK : 'topk';
BOTK : 'botk';
PINV : 'pinv';

PLUS        : '+';
MINUS       : '-';
MULT        : '*';
DIV         : '/';
MOD         : '%';
POW         : '^';

GE          : '>=';
GT          : '>';
LE          : '<=';
LT          : '<';
EQ          : '==';
NE          : '!=';
PIPE        : '|';

CONSTANT    : ('pi'|'PI'|'e'|'E');
NUMBER      : [0-9]+ ('.' [0-9]+)?;
VARIABLE    : [a-zA-Z_] [a-zA-Z_0-9]*;
WS          : [ \t\r\n]+ -> skip;
