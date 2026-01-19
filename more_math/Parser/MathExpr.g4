grammar MathExpr;

// Top-level entry point
start: funcDef* expr EOF;

funcDef:
	VARIABLE LPAREN paramList? RPAREN ARROW expr SEMICOLON # FunctionDef;

paramList: VARIABLE (COMMA VARIABLE)*;

expr: atom | compExpr;

compExpr:
	compExpr GT addExpr		# GtExp
	| compExpr GE addExpr	# GeExp
	| compExpr LT addExpr	# LtExp
	| compExpr LE addExpr	# LeExp
	| compExpr EQ addExpr	# EqExp
	| compExpr NE addExpr	# NeExp
	| addExpr				# ToAdd;

addExpr:
	addExpr PLUS mulExpr	# AddExp
	| addExpr MINUS mulExpr	# SubExp
	| mulExpr				# ToMul;

mulExpr:
	mulExpr MULT powExpr	# MulExp
	| mulExpr DIV powExpr	# DivExp
	| mulExpr MOD powExpr	# ModExp
	| powExpr				# ToPow;

powExpr: unaryExpr POW powExpr # PowExp | unaryExpr # ToUnary;

unaryExpr:
	PLUS unaryExpr		# UnaryPlus
	| MINUS unaryExpr	# UnaryMinus
	| indexExpr			# ToIndex;

indexExpr:
	indexExpr LBRACKET expr (COMMA expr)* RBRACKET	# IndexExp
	| atom											# ToAtom;

// Atoms: function calls, variable, number, constant, or parenthesized expression
atom:
	func1									# Func1Exp
	| func2									# Func2Exp
	| func3									# Func3Exp
	| func4									# Func4Exp
	| funcN									# FuncNExp
	| VARIABLE								# VariableExp
	| NUMBER								# NumberExp
	| CONSTANT								# ConstantExp
	| LPAREN expr RPAREN					# ParenExp
	| PIPE expr PIPE						# AbsExp
	| LBRACKET expr (COMMA expr)* RBRACKET	# ListExp
	| VARIABLE LPAREN exprList? RPAREN		# CallExp;

exprList: expr (COMMA expr)*;

// Single-argument functions
func1:
	SIN LPAREN expr RPAREN				# SinFunc
	| COS LPAREN expr RPAREN			# CosFunc
	| TAN LPAREN expr RPAREN			# TanFunc
	| ASIN LPAREN expr RPAREN			# AsinFunc
	| ACOS LPAREN expr RPAREN			# AcosFunc
	| ATAN LPAREN expr RPAREN			# AtanFunc
	| SINH LPAREN expr RPAREN			# SinhFunc
	| COSH LPAREN expr RPAREN			# CoshFunc
	| TANH LPAREN expr RPAREN			# TanhFunc
	| ASINH LPAREN expr RPAREN			# AsinhFunc
	| ACOSH LPAREN expr RPAREN			# AcoshFunc
	| ATANH LPAREN expr RPAREN			# AtanhFunc
	| ABS LPAREN expr RPAREN			# AbsFunc
	| SQRT LPAREN expr RPAREN			# SqrtFunc
	| LN LPAREN expr RPAREN				# LnFunc
	| LOG LPAREN expr RPAREN			# LogFunc
	| EXP LPAREN expr RPAREN			# ExpFunc
	| TNORM LPAREN expr RPAREN			# TNormFunc
	| SNORM LPAREN expr RPAREN			# SNormFunc
	| FLOOR LPAREN expr RPAREN			# FloorFunc
	| CEIL LPAREN expr RPAREN			# CeilFunc
	| ROUND LPAREN expr RPAREN			# RoundFunc
	| GAMMA LPAREN expr RPAREN			# GammaFunc
	| SIGM LPAREN expr RPAREN			# sigmoidFunc
	| SFFT LPAREN expr RPAREN			# sfftFunc
	| SIFFT LPAREN expr RPAREN			# sifftFunc
	| ANGL LPAREN expr RPAREN			# anglFunc
	| PRNT LPAREN expr RPAREN			# printFunc
	| FRACT LPAREN expr RPAREN			# FractFunc
	| RELU LPAREN expr RPAREN			# ReluFunc
	| SOFTPLUS LPAREN expr RPAREN		# SoftplusFunc
	| GELU LPAREN expr RPAREN			# GeluFunc
	| SIGN LPAREN expr RPAREN			# SignFunc
	| PRINT_SHAPE LPAREN expr RPAREN	# PrintShapeFunc
	| PINV LPAREN expr RPAREN			# PinvFunc
	| SUM LPAREN expr RPAREN			# SumFunc
	| MEAN LPAREN expr RPAREN			# MeanFunc
	| STD LPAREN expr RPAREN			# StdFunc
	| VAR LPAREN expr RPAREN			# VarFunc
	| SORT LPAREN expr RPAREN			# SortFunc;

// Two-argument functions Two-argument functions
func2:
	POWE LPAREN expr COMMA expr RPAREN			# PowFunc
	| ATAN2 LPAREN expr COMMA expr RPAREN		# Atan2Func
	| TMIN LPAREN expr COMMA expr RPAREN		# TMinFunc
	| TMAX LPAREN expr COMMA expr RPAREN		# TMaxFunc
	| STEP LPAREN expr COMMA expr RPAREN		# StepFunc
	| TOPK LPAREN expr COMMA expr RPAREN		# TopkFunc
	| BOTK LPAREN expr COMMA expr RPAREN		# BotkFunc
	| QUARTILE LPAREN expr COMMA expr RPAREN	# QuartileFunc
	| PERCENTILE LPAREN expr COMMA expr RPAREN	# PercentileFunc
	| QUANTILE LPAREN expr COMMA expr RPAREN	# QuantileFunc
	| QUANTILE LPAREN expr COMMA expr RPAREN	# QuantileFunc
	| DOT LPAREN expr COMMA expr RPAREN			# DotFunc
	| COSSIM LPAREN expr COMMA expr RPAREN		# CossimFunc
	| FLIP LPAREN expr COMMA expr RPAREN		# FlipFunc
	| COV LPAREN expr COMMA expr RPAREN			# CovFunc;

func3:
	CLAMP LPAREN expr COMMA expr COMMA expr RPAREN			# ClampFunc
	| LERP LPAREN expr COMMA expr COMMA expr RPAREN			# LerpFunc
	| SMOOTHSTEP LPAREN expr COMMA expr COMMA expr RPAREN	# SmoothstepFunc
	| RANGE LPAREN expr COMMA expr COMMA expr RPAREN		# RangeFunc
	| MOMENT LPAREN expr COMMA expr COMMA expr RPAREN		# MomentFunc;

func4:
	SWAP LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN # SwapFunc;

// N-argument functions
funcN:
	SMIN LPAREN expr (COMMA expr)* RPAREN		# SMinFunc
	| SMAX LPAREN expr (COMMA expr)* RPAREN		# SMaxFunc
	| MAP LPAREN expr (COMMA expr)+ RPAREN		# MapFunc
	| EZCONV LPAREN expr (COMMA expr)+ RPAREN	# EzConvFunc
	| CONV LPAREN expr (COMMA expr)+ RPAREN		# ConvFunc
	| PERM LPAREN expr COMMA expr RPAREN		# PermuteFunc
	| RESHAPE LPAREN expr COMMA expr RPAREN		# ReshapeFunc;

// LEXER RULES

SIN: 'sin';
COS: 'cos';
TAN: 'tan';
ASIN: 'asin';
ACOS: 'acos';
ATAN: 'atan';
ATAN2: 'atan2';
SINH: 'sinh';
COSH: 'cosh';
TANH: 'tanh';
ASINH: 'asinh';
ACOSH: 'acosh';
ATANH: 'atanh';
ABS: 'abs';
SQRT: 'sqrt';
LN: 'ln';
LOG: 'log';
EXP: 'exp';
SMIN: 'smin';
SMAX: 'smax';
TMIN: 'tmin';
TMAX: 'tmax';
TNORM: 'tnorm';
SNORM: 'snorm';
FLOOR: 'floor';
CEIL: 'ceil';
ROUND: 'round';
GAMMA: 'gamma';
POWE: 'pow';
SIGM: 'sigm';
CLAMP: 'clamp';
SFFT: 'fft';
SIFFT: 'ifft';
ANGL: 'angle';
PRNT: 'print';
PRINT_SHAPE: 'print_shape' | 'pshp';
LERP: 'lerp';
STEP: 'step';
SMOOTHSTEP: 'smoothstep';
FRACT: 'fract';
RELU: 'relu';
SOFTPLUS: 'softplus';
GELU: 'gelu';
SIGN: 'sign';
MAP: 'map';
EZCONV: 'ezconvolution' | 'ezconv';
CONV: 'convolution' | 'conv';
SWAP: 'swap';
PERM: 'permute' | 'perm';
RESHAPE: 'reshape' | 'rshp';
RANGE: 'range';
TOPK: 'topk';
BOTK: 'botk';
PINV: 'pinv';
SUM: 'sum';
MEAN: 'mean';
STD: 'std';
VAR: 'var';
QUARTILE: 'quartile' | 'quartil';
PERCENTILE: 'percentile' | 'prcnt';
QUANTILE: 'quantile';
DOT: 'dot';
MOMENT: 'moment';

COSSIM: 'cossim';
FLIP: 'flip';
COV: 'cov';
SORT: 'sort';

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
POW: '^';

GE: '>=';
GT: '>';
LE: '<=';
LT: '<';
EQ: '==';
NE: '!=';
PIPE: '|';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
SEMICOLON: ';';
ARROW: '->';
LBRACKET: '[';
RBRACKET: ']';

CONSTANT: ('pi' | 'PI' | 'e' | 'E');
NUMBER: [0-9]+ ('.' [0-9]+)?;
VARIABLE: [a-zA-Z_] [a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;
