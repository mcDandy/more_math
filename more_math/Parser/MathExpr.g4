grammar MathExpr;

// Top-level entry point
start: (funcDef | varDef | stmt)* expr SEMICOLON? EOF;

funcDef:
	VARIABLE LPAREN paramList? RPAREN ARROW (block | expr) SEMICOLON # FunctionDef;

varDef:
	VARIABLE (LBRACKET expr (COMMA expr)* RBRACKET)* EQUEALS expr SEMICOLON;

paramList: VARIABLE (COMMA VARIABLE)*;

stmt:
	ifStmt				# IfStatement
	| whileStmt			# WhileStatement
	| block				# BlockStatement
	| breakStmt			# BreakStatement
	| continueStmt		# ContinueStatement
	| returnStmt		# ReturnStatement
	| varDef			# VarDefStmt
	| forStmt			# ForStatement
	| expr SEMICOLON	# ExprStatement;

ifStmt: IF LPAREN expr RPAREN stmt (ELSE stmt)?;
whileStmt: WHILE LPAREN expr RPAREN stmt;
forStmt: FOR LPAREN VARIABLE IN expr RPAREN stmt;
block: LBRACE stmt* RBRACE;
breakStmt: BREAK SEMICOLON;
continueStmt: CONTINUE SEMICOLON;
returnStmt: RETURN expr? SEMICOLON;

expr: ternaryExpr | atom | compExpr;

ternaryExpr: compExpr QUESTION expr COLON expr # TernaryExp;

compExpr:
	compExpr GT addExpr		# GtExp
	| compExpr GE addExpr	# GeExp
	| compExpr LT addExpr	# LtExp
	| compExpr LE addExpr	# LeExp
	| compExpr EQ addExpr	# EqExp
	| compExpr NE addExpr	# NeExp
	| addExpr			# ToAdd;

addExpr:
	addExpr PLUS mulExpr	# AddExp
	| addExpr MINUS mulExpr	# SubExp
	| mulExpr			# ToMul;

mulExpr:
	mulExpr MULT shiftExpr	# MulExp
	| mulExpr DIV shiftExpr	# DivExp
	| mulExpr MOD shiftExpr	# ModExp
	| shiftExpr			# ToShift;

shiftExpr:
	shiftExpr LSHIFT powExpr	# LShiftExp
	| shiftExpr RSHIFT powExpr	# RShiftExp
	| powExpr			# ToPow;

powExpr: unaryExpr POW powExpr # PowExp | unaryExpr # ToUnary;

unaryExpr:
	PLUS unaryExpr		# UnaryPlus
	| MINUS unaryExpr	# UnaryMinus
	| indexExpr			# ToIndex;

indexExpr:
	indexExpr LBRACKET expr (COMMA expr)* RBRACKET	# IndexExp
	| atom								# ToAtom;

// Atoms: function calls, variable, number, constant, or parenthesized expression
atom:
	func0							# Func0Exp
	| func1							# Func1Exp
	| func2							# Func2Exp
	| func3							# Func3Exp
	| func4							# Func4Exp
	| func5							# Func5Exp
	| funcN							# FuncNExp
	| funcNoise						# FuncNoiseExp
	| VARIABLE						# VariableExp
	| NUMBER						# NumberExp
	| CONSTANT					# ConstantExp
	| LPAREN expr RPAREN		# ParenExp
	| PIPE expr PIPE		# AbsExp
	| LBRACKET expr (COMMA expr)* RBRACKET	# ListExp
	| VARIABLE LPAREN exprList? RPAREN	# CallExp
	| NONE						# NoneExp
	| BREAK						# BreakExp
	| CONTINUE					# ContinueExp;

exprList: expr (COMMA expr)*;

func0: TIMESTAMP LPAREN RPAREN # TimestampFunc;
// Single-argument functions
func1:
	SIN LPAREN expr RPAREN					# SinFunc
	| COS LPAREN expr RPAREN				# CosFunc
	| TAN LPAREN expr RPAREN				# TanFunc
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
	| ANGL LPAREN expr RPAREN			# anglFunc
	| PRNT LPAREN expr RPAREN			# printFunc
	| FRACT LPAREN expr RPAREN			# FractFunc
	| RELU LPAREN expr RPAREN			# ReluFunc
	| SOFTPLUS LPAREN expr RPAREN		# SoftplusFunc
	| GELU LPAREN expr RPAREN			# GeluFunc
	| SIGN LPAREN expr RPAREN			# SignFunc
	| PRINT_SHAPE LPAREN expr RPAREN	# PrintShapeFunc
	| PINV LPAREN expr RPAREN		# PinvFunc
	| SUM LPAREN expr RPAREN			# SumFunc
	| MEAN LPAREN expr RPAREN		# MeanFunc
	| STD LPAREN expr RPAREN			# StdFunc
	| VAR LPAREN expr RPAREN			# VarFunc
	| SORT LPAREN expr RPAREN			# SortFunc
	| ANY LPAREN expr RPAREN			# AnyFunc
	| ALL LPAREN expr RPAREN			# AllFunc
	| EDGE LPAREN expr (COMMA expr)? RPAREN	# EdgeFunc
	| MEDIAN LPAREN expr RPAREN		# MedianFunc
	| MODE LPAREN expr RPAREN			# ModeFunc
	| CUMSUM LPAREN expr RPAREN		# CumsumFunc
	| COUNT LPAREN expr RPAREN		# CountFunc
	| CUMPROD LPAREN expr RPAREN		# CumprodFunc
	| POP LPAREN expr RPAREN			# PopFunc
	| CLEAR LPAREN expr RPAREN		# ClearFunc
	| HAS LPAREN expr RPAREN			# HasFunc
	| GET LPAREN expr RPAREN			# GetFunc
	| ARGSORT LPAREN expr (COMMA expr)? RPAREN	# ArgsortFunc
	| ARGMIN LPAREN expr RPAREN		# ArgminFunc
	| ARGMAX LPAREN expr RPAREN		# ArgmaxFunc
	| SOFTMAX LPAREN expr RPAREN		# SoftmaxFunc
	| SOFTMIN LPAREN expr RPAREN		# SoftminFunc
	| UNIQUE LPAREN expr RPAREN		# UniqueFunc
	| FLATTEN LPAREN expr RPAREN		# FlattenFunc
	| MOTION_MASK LPAREN expr RPAREN	# MotionMaskFunc
	| FLOW_TO_IMAGE LPAREN expr RPAREN	# FlowToImageFunc
	| BNOT LPAREN expr RPAREN		# BitNotFunc
	| BITCOUNT LPAREN expr RPAREN	# BitCountFunc
	| SHAPE LPAREN expr RPAREN		# ShapeFunc;

func2:
	POWE LPAREN expr COMMA expr RPAREN				# PowFunc
	| ATAN2 LPAREN expr COMMA expr RPAREN			# Atan2Func
	| TMIN LPAREN expr COMMA expr RPAREN			# TMinFunc
	| TMAX LPAREN expr COMMA expr RPAREN			# TMaxFunc
	| STEP LPAREN expr COMMA expr RPAREN			# StepFunc
	| TOPK LPAREN expr COMMA expr RPAREN			# TopkFunc
	| BOTK LPAREN expr COMMA expr RPAREN			# BotkFunc
	| QUARTILE LPAREN expr COMMA expr RPAREN		# QuartileFunc
	| PERCENTILE LPAREN expr COMMA expr RPAREN		# PercentileFunc
	| QUANTILE LPAREN expr COMMA expr RPAREN		# QuantileFunc
	| DOT LPAREN expr COMMA expr RPAREN			# DotFunc
	| COSSIM LPAREN expr COMMA expr RPAREN		# CossimFunc
	| FLIP LPAREN expr COMMA expr RPAREN			# FlipFunc
	| COV LPAREN expr COMMA expr RPAREN			# CovFunc
	| APPEND LPAREN expr COMMA expr RPAREN		# AppendFunc
	| GAUSSIAN LPAREN expr COMMA expr (COMMA expr)? RPAREN	# GaussianFunc
	| TOPK_IND LPAREN expr COMMA expr RPAREN		# TopkIndFunc
	| BOTK_IND LPAREN expr COMMA expr RPAREN		# BotkIndFunc
	| BATCH_SHUFFLE LPAREN expr COMMA expr RPAREN	# BatchShuffleFunc
	| PUSH LPAREN expr COMMA expr RPAREN		# PushFunc
	| GET_VALUE LPAREN expr COMMA expr RPAREN	# GetValueFunc
	| TENSOR LPAREN indexExpr (COMMA expr (COMMA expr)? )? RPAREN	# EmptyTensorFunc
	| PAD LPAREN expr COMMA expr RPAREN		# PadFunc
	| CROSS LPAREN expr COMMA expr RPAREN		# CrossFunc
	| MATMUL LPAREN expr COMMA expr RPAREN		# MatmulFunc
	| FLOW_APPLY LPAREN expr COMMA expr RPAREN	# FlowApplyFunc
	| RIFE LPAREN expr COMMA expr (COMMA expr (COMMA expr (COMMA expr)?)?)? RPAREN # RifeFunc
	| BAND LPAREN expr COMMA expr RPAREN		# BitAndFunc
	| XOR LPAREN expr COMMA expr RPAREN		# BitXorFunc
	| BOR LPAREN expr COMMA expr RPAREN		# BitOrFunc;

func3:
	CLAMP LPAREN expr COMMA expr COMMA expr RPAREN	# ClampFunc
	| LERP LPAREN expr COMMA expr COMMA expr RPAREN	# LerpFunc
	| SMOOTHSTEP LPAREN expr COMMA expr COMMA expr RPAREN	# SmoothstepFunc
	| RANGE LPAREN expr COMMA expr COMMA expr RPAREN	# RangeFunc
	| MOMENT LPAREN expr COMMA expr COMMA expr RPAREN	# MomentFunc
	| CUBIC_EASE LPAREN expr COMMA expr COMMA expr RPAREN	# CubicEaseFunc
	| ELASTIC_EASE LPAREN expr COMMA expr COMMA expr RPAREN	# ElasticEaseFunc
	| SINE_EASE LPAREN expr COMMA expr COMMA expr RPAREN	# SineEaseFunc
	| SMOOTHERSTEP LPAREN expr COMMA expr COMMA expr RPAREN	# SmootherstepFunc
	| CROP LPAREN expr COMMA expr COMMA expr RPAREN	# CropFunc
	| SIFFT LPAREN expr (COMMA expr)? RPAREN		# sifftFunc;
func4:
	SWAP LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# SwapFunc
	| NVL LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# NvlFunc
	| DIST LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# DistFunc;

func5:
	REMAP LPAREN expr COMMA expr COMMA expr COMMA expr COMMA expr RPAREN # RemapFunc;

// N-argument functions
funcN:
	SMIN LPAREN expr (COMMA expr)* RPAREN	# SMinFunc
	| SMAX LPAREN expr (COMMA expr)* RPAREN	# SMaxFunc
	| MAP LPAREN expr (COMMA expr)+ RPAREN	# MapFunc
	| EZCONV LPAREN expr (COMMA expr)+ RPAREN	# EzConvFunc
	| CONV LPAREN expr (COMMA expr)+ RPAREN	# ConvFunc
	| PERM LPAREN expr COMMA expr RPAREN	# PermuteFunc
	| RESHAPE LPAREN expr COMMA expr RPAREN	# ReshapeFunc;

funcNoise:
	NOISE LPAREN expr (COMMA expr)? RPAREN				# NoiseFunc
	| RAND LPAREN expr (COMMA expr)? RPAREN				# RandFunc
	| EXPONENTIAL LPAREN expr COMMA expr (COMMA expr)? RPAREN	# ExponentialFunc
	| BERNOULLI LPAREN expr COMMA expr (COMMA expr)? RPAREN	# BernoulliFunc
	| POISSON LPAREN expr COMMA expr (COMMA expr)? RPAREN		# PoissonFunc
	| CAUCHY LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# CauchyFunc
	| LOGNORMAL LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# LogNormalFunc
	| GAMMADIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# GammaDistFunc
	| BETADIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# BetaDistFunc
	| LAPLACEDIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# LaplaceDistFunc
	| GUMBELDIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# GumbelDistFunc
	| WEIBULLDIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# WeibullDistFunc
	| CHI2DIST LPAREN expr COMMA expr (COMMA expr)? RPAREN	# Chi2DistFunc
	| STUDENTTDIST LPAREN expr COMMA expr (COMMA expr)? RPAREN	# StudentTDistFunc
	| PERLIN LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# PerlinFunc
	| CELLULAR LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# CellularFunc
	| PLASMA LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# PlasmaFunc;

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
NVL: 'nvl' | 'nan_to_num';
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
ANY: 'any';
ALL: 'all';
EDGE: 'edge';
GAUSSIAN: 'blur' | 'gaussian';
MEDIAN: 'median';
MODE: 'mode';
CUMSUM: 'cumsum';
CUMPROD: 'cumprod';
TOPK_IND: 'topk_ind' | 'topk_indices';
BOTK_IND: 'botk_ind' | 'botk_indices';
CUBIC_EASE: 'cubic_ease' | 'cubic';
ELASTIC_EASE: 'elastic_ease' | 'elastic';
SINE_EASE: 'sine_ease' | 'sine';
SMOOTHERSTEP: 'smootherstep';
DIST: 'dist' | 'distance';
REMAP: 'remap';
COSSIM: 'cossim' | 'cosine_similarity';
COUNT: 'count' | 'cnt' | 'length';
FLATTEN: 'flatten';
APPEND: 'append';
GET_VALUE: 'get_value';
FLOW_APPLY: 'flow_apply';
BATCH_SHUFFLE: 'batch_shuffle' | 'shuffle';
MOTION_MASK: 'motion_mask';
FLOW_TO_IMAGE: 'flow_to_image';
OVERLAY: 'overlay';
PAD: 'pad';
CROSS: 'cross';
MATMUL: 'matmul';
RIFE: 'rife';
BNOT: 'bnot' | 'bitwise_not';
BITCOUNT: 'bitcount' | 'popcount' | 'popcnt';
SHAPE: 'shape';
BAND: 'band' | 'bitwise_and';
XOR: 'bxor' | 'bitwise_xor';
BOR: 'bor' | 'bitwise_or';
TENSOR: 'tensor';
PUSH: 'stack_push';
POP: 'stack_pop';
CLEAR: 'stack_clear';
HAS: 'stack_has';
GET: 'stack_get';

IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
IN: 'in';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
TIMESTAMP: 'timestamp';
SORT: 'sort';
ARGSORT: 'argsort';
ARGMIN: 'argmin';
ARGMAX: 'argmax';
SOFTMAX: 'softmax';
SOFTMIN: 'softmin';
UNIQUE: 'unique';
FLIP: 'flip';
COV: 'cov';
CROP: 'crop';
NONE: 'none'|'None'|'null'|'NULL';

NOISE: 'noise' | 'randn' | 'random_normal';
RAND: 'rand' | 'randu' | 'random_uniform';
CAUCHY: 'randc' | 'random_cauchy';
EXPONENTIAL: 'rande' | 'random_exponential';
LOGNORMAL: 'randln' | 'random_log_normal';
BERNOULLI: 'randb' | 'random_bernoulli';
POISSON: 'randp' | 'random_poisson';
GAMMADIST: 'randg' | 'random_gamma';
BETADIST: 'randbeta' | 'random_beta';
LAPLACEDIST: 'randl' | 'random_laplace';
GUMBELDIST: 'randgumbel' | 'random_gumbel';
WEIBULLDIST: 'randw' | 'random_weibull';
CHI2DIST: 'randchi2' | 'random_chi2';
STUDENTTDIST: 'randt' | 'random_studentt';
PERLIN: 'perlin' | 'perlin_noise';
CELLULAR: 'cellular' | 'voronoi' | 'worley' | 'cellular_noise'|'voronoi_noise';
PLASMA: 'plasma' | 'turbulence' | 'plasma_noise';

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
POW: '^';
LSHIFT: '<<';
RSHIFT: '>>';

GE: '>=';
GT: '>';
LE: '<=';
LT: '<';
EQ: '==';
EQUEALS: '=';
NE: '!=';
PIPE: '|';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
SEMICOLON: ';';
ARROW: '->';
LBRACKET: '[';
RBRACKET: ']';
QUESTION: '?';
COLON: ':';
LBRACE: '{';
RBRACE: '}';

NUMBER: ([0-9]+ ('.' [0-9]*)? | '.' [0-9]+) ([eE][+-]? [0-9]+)?;
CONSTANT: ('pi' | 'PI' | 'e' | 'E');
VARIABLE: [a-zA-Z_] [a-zA-Z_0-9]*;

SL_COMMENT: '#' ~[\r\n]* -> skip;
ML_COMMENT: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;