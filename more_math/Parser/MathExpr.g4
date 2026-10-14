/**
 * MathExpr.g4
 *
 * This grammar defines the syntax for a mathematical expression language.
 * It supports:
 * - Variable and function definitions
 * - Control flow statements (if, while, for)
 * - A wide range of mathematical functions (trigonometric, hyperbolic, etc.)
 * - Tensor operations (matmul, dot, reshape, etc.)
 * - Noise functions (perlin, cellular, etc.)
  * - Basic arithmetic, comparison, and bitwise function operations
 */
grammar MathExpr;


// Top-level entry point
start: (funcDef | varDef | stmt)* expr SEMICOLON? EOF;

funcDef:
	VARIABLE LPAREN paramList? RPAREN ARROW (expr | block) SEMICOLON # FunctionDef;

varDef:
	VARIABLE (LBRACKET expr (COMMA expr)* RBRACKET)* (EQUEALS | PLUS_EQ | MINUS_EQ | MULT_EQ | DIV_EQ | MOD_EQ) expr SEMICOLON;

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

dictEntryList: dictEntry (COMMA dictEntry)*;
dictEntry: VARIABLE COLON expr
	| STRING COLON expr
	| NUMBER COLON expr;

breakStmt: BREAK SEMICOLON;
continueStmt: CONTINUE SEMICOLON;
returnStmt: RETURN expr? SEMICOLON;

expr: ternaryExpr | compExpr;

ternaryExpr: compExpr QUESTION expr COLON expr # TernaryExp;

compExpr:
	compExpr EQ relationalExpr	# EqExp
	| compExpr NE relationalExpr	# NeExp
	| relationalExpr		# ToRelational;

relationalExpr:
	relationalExpr GT shiftExpr	# GtExp
	| relationalExpr GE shiftExpr	# GeExp
	| relationalExpr LT shiftExpr	# LtExp
	| relationalExpr LE shiftExpr	# LeExp
	| shiftExpr			# ToShift;

addExpr:
	addExpr PLUS mulExpr	# AddExp
	| addExpr MINUS mulExpr	# SubExp
	| mulExpr			# ToMul;

mulExpr:
	mulExpr MULT powExpr	# MulExp
	| mulExpr DIV powExpr	# DivExp
	| mulExpr MOD powExpr	# ModExp
	| powExpr			# ToPow;

shiftExpr:
	shiftExpr LSHIFT addExpr	# LShiftExp
	| shiftExpr RSHIFT addExpr	# RShiftExp
	| addExpr			# ToAdd;

powExpr: unaryExpr POW powExpr # PowExp | unaryExpr # ToUnary;

unaryExpr:
	PLUS unaryExpr		# UnaryPlus
	| MINUS unaryExpr	# UnaryMinus
	| indexExpr			# ToIndex;

indexExpr:
	indexExpr LBRACKET sliceElement (COMMA sliceElement)* RBRACKET	# IndexExp
	| atom								# ToAtom;

sliceElement:
	expr COLON expr COLON expr		# SliceWithStep
	| expr COLON expr				# Slice
	| COLON expr COLON expr			# SliceColonStartStep
	| COLON expr					# SliceColonStart
	| expr COLON COLON expr			# SliceExprColonStep
	| expr COLON					# SliceExpr
	| COLON COLON expr				# SliceColonStep
	| COLON						# SliceOnly
	| expr							# IndexOnly;

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
	| CONSTANT						# ConstantExp
	| STRING						# StringExp
	| LPAREN paramList RPAREN ARROW (expr | block)	# LambdaExp
	| LPAREN expr RPAREN			# ParenExp
	| LPAREN expr RPAREN			# ParenExp
	| PIPE expr PIPE				# AbsExp
	| LBRACKET expr (COMMA expr)* RBRACKET	# ListExp
	| LBRACE dictEntryList? RBRACE	# DictExp
	| VARIABLE LPAREN exprList? RPAREN	# CallExp
	| NONE							# NoneExp
	| BREAK							# BreakExp
	| CONTINUE						# ContinueExp;

exprList: expr (COMMA expr)*;

func0:
		/**
		  timestamp() - returns the current system timestamp
		*/
	TIMESTAMP LPAREN RPAREN # TimestampFunc;
// Single-argument functions
func1:
		/**
		  sin(x) - applies sinus function to value or each element of value
		*/
	SIN LPAREN expr RPAREN				# SinFunc
		/**
		  cos(x) - applies cosinus function to value or each element of value
		*/
	| COS LPAREN expr RPAREN			# CosFunc
		/**
		  tan(x) - applies tangents function to value or each element of value
		*/
	| TAN LPAREN expr RPAREN			# TanFunc
		/**
		  asin(x) - applies arcus sinus function to value or each element of value
		*/
	| ASIN LPAREN expr RPAREN			# AsinFunc
		/**
		  acos(x) - applies arcus cosinus function to value or each element of value
		*/
	| ACOS LPAREN expr RPAREN			# AcosFunc
		/**
		  atan(x) - applies arcus tangents function to value or each element of value
		*/
	| ATAN LPAREN expr RPAREN			# AtanFunc
		/**
		  sinh(x) - applies hyperbolic sinus function to value or each element of value
		*/
	| SINH LPAREN expr RPAREN			# SinhFunc
		/**
		  cosh(x) - applies hyperbolic cosinus function to value or each element of value
		*/
	| COSH LPAREN expr RPAREN			# CoshFunc
		/**
		  tanh(x) - applies hyperbolic tangents function to value or each element of value
		*/
	| TANH LPAREN expr RPAREN			# TanhFunc
		/**
		  asinh(x) - applies hyperbolic arcus sinus function to value or each element of value
		*/
	| ASINH LPAREN expr RPAREN			# AsinhFunc
		/**
		  acosh(x) - applies hyperbolic arcus cosinus function to value or each element of value
		*/
	| ACOSH LPAREN expr RPAREN			# AcoshFunc
		/**
		  atanh(x) - applies hyperbolic arcus tangents function to value or each element of value
		*/
	| ATANH LPAREN expr RPAREN			# AtanhFunc
		/**
		  abs(x) - applies per element absolute value function. Same as |x| for numbers.
		*/
	| ABS LPAREN expr RPAREN			# AbsFunc
		/**
		  sqrt(x) - applies sqere root per element. Negative numbers return NaN (not a number)
		*/
	| SQRT LPAREN expr RPAREN			# SqrtFunc
		/**
		  ln(x) - applies natural logarithm to value (per element). Negative numbers return NaN (not a number)
		*/
	| LN LPAREN expr RPAREN				# LnFunc
		/**
		  log(x) - applies base 10 logarithm to value (per element). Negative numbers return NaN (not a number)
		*/
	| LOG LPAREN expr RPAREN			# LogFunc
		/**
		  log2(x) - applies base 2 logarithm to value (per element). Negative numbers return NaN (not a number)
		*/
	| LOG2 LPAREN expr RPAREN			# Log2Func
		/**
		  exp(x) - applies e^x to value (per element)
		*/
		| EXP LPAREN expr RPAREN			# ExpFunc
			/**
			  log1p(x) - applies ln(1+x) accurately for values near zero
			*/
		| LOG1P LPAREN expr RPAREN			# Log1pFunc
			/**
			  expm1(x) - applies exp(x)-1 accurately for values near zero
			*/
		| EXPM1 LPAREN expr RPAREN			# Expm1Func
		/**
		  cbrt(x) - computes the real cube root of each value, including negative values
		*/
		| CBRT LPAREN expr RPAREN			# CbrtFunc
		/**
		  reciprocal(x) - computes 1/x element-wise
		*/
		| RECIPROCAL LPAREN expr RPAREN		# ReciprocalFunc
			/**
			  isnan(x) - returns 1.0 for NaN values and 0.0 otherwise
			*/
		| ISNAN LPAREN expr RPAREN			# IsnanFunc
			/**
			  isinf(x) - returns 1.0 for infinite values and 0.0 otherwise
			*/
		| ISINF LPAREN expr RPAREN			# IsinfFunc
			/**
			  isfinite(x) - returns 1.0 for finite values and 0.0 otherwise
			*/
		| ISFINITE LPAREN expr RPAREN			# IsfiniteFunc
		/**
		  tnorm(x, [dim]) - normalises tensor or list by multiplication such that sum(x^2)==1.0 for each slice. Defaults to the last dimension; dim selects a different slicing dimension.
		*/
		| TNORM LPAREN expr (COMMA expr)? RPAREN			# TNormFunc
		/**
		  floor(x) - returns the largest integer less than or equal to x
		*/
	| FLOOR LPAREN expr RPAREN			# FloorFunc
		/**
		  ceil(x) - returns the smallest integer greater than or equal to x
		*/
	| CEIL LPAREN expr RPAREN			# CeilFunc
		/**
		  round(x) - rounds x to the nearest integer
		*/
	| ROUND LPAREN expr RPAREN			# RoundFunc
		/**
		  gamma(x) - computes the gamma function (per element)
		*/
	| GAMMA LPAREN expr RPAREN			# GammaFunc
		/**
		  sigm(x) - applies the sigmoid function: 1 / (1 + exp(-x))
		*/
	| SIGM LPAREN expr RPAREN			# sigmoidFunc
		/**
		  angle(x) - returns the angle of a complex number or vector
		*/
	| ANGL LPAREN expr RPAREN			# anglFunc
		/**
		  print(x) - prints the value of x to the console while passing output unchanged
		*/
	| PRNT LPAREN expr RPAREN			# printFunc
		/**
		  fract(x) - returns the fractional part of x: x - floor(x)
		*/
	| FRACT LPAREN expr RPAREN			# FractFunc
		/**
		  relu(x) - applies rectified linear unit function: max(0, x)
		*/
	| RELU LPAREN expr RPAREN			# ReluFunc
		/**
		  softsign(x) - applies x / (1 + abs(x)) element-wise
		*/
	| SOFTSIGN LPAREN expr RPAREN			# SoftsignFunc
		/**
		  softplus(x) - applies the softplus function: ln(1 + exp(x))
		*/
	| SOFTPLUS LPAREN expr RPAREN			# SoftplusFunc
		/**
		  gelu(x) - applies the Gaussian Error Linear Unit (GELU) activation function
		*/
	| GELU LPAREN expr RPAREN			# GeluFunc
		/**
		  sign(x) - returns the sign of x: -1, 0, or 1
		*/
	| SIGN LPAREN expr RPAREN			# SignFunc
		/**
	  degrees(x) - converts radians to degrees (per element)
	*/
	| DEGREES LPAREN expr RPAREN			# DegreesFunc
		/**
	  radians(x) - converts degrees to radians (per element)
	*/
	| RADIANS LPAREN expr RPAREN			# RadiansFunc
		/**
	  logical_not(x) - returns 1.0 where x is zero and 0.0 otherwise
	*/
	| LOGICAL_NOT LPAREN expr RPAREN		# LogicalNotFunc
		/**
		  print_shape(x) - prints the shape of the tensor x
		*/
	| PRINT_SHAPE LPAREN expr RPAREN		# PrintShapeFunc
		/**
		  pinv(x) - computes the permutative inverse of a list x (list must have uniqe elements) -- TODO: CHECK --
		*/
	| PINV LPAREN expr RPAREN			# PinvFunc
		/**
		  inv(x, [pseudo]) - computes the matrix inverse; when pseudo is truthy, computes the Moore-Penrose pseudoinverse instead
		*/
	| INV LPAREN expr (COMMA expr)? RPAREN		# InvFunc
		/**
		  matrix_rank(x, [tol]) - computes the numerical rank of each matrix using optional absolute tolerance tol
		*/
	| MATRIX_RANK LPAREN expr (COMMA expr)? RPAREN	# MatrixRankFunc
		/**
		  sum(x, [dims]) - computes the sum of elements of x, optionally along one or more dimensions
		*/
	| SUM LPAREN expr (COMMA expr)? RPAREN		# SumFunc
		/**
		  mean(x, [dims]) - computes the arithmetic mean of elements of x globally or along one or more dimensions
		*/
	| MEAN LPAREN expr (COMMA expr)? RPAREN		# MeanFunc
		/**
		  std(x, [dims]) - computes the sample standard deviation of elements of x globally or along one or more dimensions
		*/
	| STD LPAREN expr (COMMA expr)? RPAREN		# StdFunc
		/**
		  var(x, [dims]) - computes the sample variance of elements of x globally or along one or more dimensions
		*/
	| VAR LPAREN expr (COMMA expr)? RPAREN		# VarFunc
		/**
		  prod(x, [dims]) - computes the product of elements of x globally or along one or more dimensions
		*/
	| PROD LPAREN expr (COMMA expr)? RPAREN		# ProdFunc
		/**
		  sort(x, [desc], [dim]) - returns a sorted version of x (If input is tensor, it sorts the last dimension)
		*/
	| SORT LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN			# SortFunc
		/**
		  any(x) - returns 1 if any element of x is non-zero otherwise 0
		*/
	| ANY LPAREN expr RPAREN			# AnyFunc
		/**
		  all(x) - returns 1 if all elements of x are non-zero otherwise 0
		*/
	| ALL LPAREN expr RPAREN			# AllFunc
		/**
		  edge(x, [matrix_size]) - detects edges in x. Matrix size denotes the size of edge detection matrix.
		*/
	| EDGE LPAREN expr (COMMA expr)? RPAREN		# EdgeFunc
		/**
		  median(x, [dim]) - computes the median globally or along one dimension
		*/
	| MEDIAN LPAREN expr (COMMA expr)? RPAREN			# MedianFunc
		/**
		  mode(x, [dim]) - computes the mode globally or along one dimension
		*/
	| MODE LPAREN expr (COMMA expr)? RPAREN			# ModeFunc
		/**
		  cumsum(x, [dim]) - computes the cumulative sum, defaulting to the first dimension.
		*/
	| CUMSUM LPAREN expr (COMMA expr)? RPAREN	# CumsumFunc
		/**
		  count(x) - returns the number of elements in x
		*/
	| COUNT LPAREN expr RPAREN			# CountFunc
		/**
		  keys(x) - returns a list of dictionary keys in insertion order
		*/
	| KEYS LPAREN expr RPAREN			# KeysFunc
		/**
		  enable_tracking(d) - enables change tracking for ChangeTrackingDict d (returns d)
		*/
	| ENABLE_TRACKING LPAREN expr RPAREN	# EnableTrackingFunc
		/**
		  disable_tracking(d) - disables change tracking for ChangeTrackingDict d (returns d)
		*/
	| DISABLE_TRACKING LPAREN expr RPAREN	# DisableTrackingFunc
		/**
		  reset_tracking(d) - resets change tracking state for ChangeTrackingDict d (returns d)
		*/
	| RESET_TRACKING LPAREN expr RPAREN		# ResetTrackingFunc
		/**
		  repeat(x, count, [dims]) - repeats tensor elements; count may be scalar or per-dim list
		*/
	| REPEAT LPAREN expr COMMA expr (COMMA expr)? RPAREN	# RepeatFunc
		/**
		  cumprod(x) - computes the cumulative product over first dimension.
		*/
	| CUMPROD LPAREN expr RPAREN			# CumprodFunc
		/**
		  stack_pop(slot) - removes and returns the last element of slot stack
		*/
	| POP LPAREN expr RPAREN			# PopFunc
		/**
		  stack_clear(slot) - clears the contents of slot stack
		*/
	| CLEAR LPAREN expr RPAREN			# ClearFunc
		/**
		  stack_has(slot) - returns 1.0 if slot exists in stack and is not empty else returns 0.0
		*/
	| HAS LPAREN expr RPAREN			# HasFunc
		/**
		  stack_get(slot) - returns the last pushed value in slot without popping it
		*/
	| GET LPAREN expr RPAREN			# GetFunc
		/**
		  argsort(x, [desc], [dim]) - returns the indices that would sort x. desc defaults to ascending and dim defaults to the last dimension.
		*/
	| ARGSORT LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN	# ArgsortFunc
		/**
		  argmin(x, [as_position], [dim]) - returns the minimum index globally or along dim; as_position returns global coordinates
		*/
	| ARGMIN LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN		# ArgminFunc
		/**
		  argmax(x, [as_position], [dim]) - returns the maximum index globally or along dim; as_position returns global coordinates
		*/
	| ARGMAX LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN		# ArgmaxFunc
		/**
		  softmax(x, [axis]) - applies the softmax function to x (sum of slice == 1.0 and max value <= 1.0). axis defaults to last.
		*/
	| SOFTMAX LPAREN expr (COMMA expr)? RPAREN	# SoftmaxFunc
		/**
		  softmin(x, [axis]) - applies the softmin function to x (same as softmax(-x,[axis])). axis defaults to last.
		*/
	| SOFTMIN LPAREN expr (COMMA expr)? RPAREN	# SoftminFunc
		/**
		  erf(x) - computes the error function (torch.erf)
		*/
	| ERF LPAREN expr RPAREN			# ErfFunc
		/**
		  erfinv(x) - computes the inverse error function (torch.erfinv)
		*/
	| ERFINV LPAREN expr RPAREN			# ErfinvFunc
		/**
		  unique(x) - returns the unique elements (sorted, flatened)
		*/
	| UNIQUE LPAREN expr RPAREN			# UniqueFunc
		/**
		  flatten(x) - flattens tensor into a 1D tensor
		*/
	| FLATTEN LPAREN expr RPAREN			# FlattenFunc
		/**
		  motion_mask(x) - generates a motion mask from optical flow
		*/
	| MOTION_MASK LPAREN expr RPAREN		# MotionMaskFunc
		/**
		  flow_to_image(x) - converts optical flow x to an RGB image. Up-Down is blue-yellow Left-right green-magenta.
		*/
	| FLOW_TO_IMAGE LPAREN expr RPAREN		# FlowToImageFunc
		/**
		  bnot(x) - computes the bitwise NOT
		*/
	| BNOT LPAREN expr RPAREN			# BitNotFunc
		/**
		  bitcount(x) - returns the number of set bits
		*/
	| BITCOUNT LPAREN expr RPAREN			# BitCountFunc
		/**
		  shape(x) - returns the shape of tensor as a list
		*/
	| SHAPE LPAREN expr RPAREN			# ShapeFunc
		/**
		  upper(x) - converts string to uppercase
		*/
	| UPPER LPAREN expr RPAREN			# UpperFunc
		/**
		  lower(x) - converts string to lowercase
		*/
	| LOWER LPAREN expr RPAREN			# LowerFunc
		/**
		  trim(x) - removes leading and trailing whitespace from string
		*/
	| TRIM LPAREN expr RPAREN			# TrimFunc
		/**
		  entropy(x) - computes shanon entropy
		*/
	| ENTROPY LPAREN expr RPAREN			# EntropyFunc
		/**
		  fft(x) - computes  fast Fourier transform of x
		*/
	| SFFT LPAREN expr RPAREN			# SfftFunc
		/**
		  dilate(x, [kernel]) - applies dilation to x. kernel is optional.
		*/
	| DILATE LPAREN expr (COMMA expr)? RPAREN	# DilateFunc
		/**
		  erode(x, [kernel]) - applies erosion to x. kernel is size of used matrix.
		*/
	| ERODE LPAREN expr (COMMA expr)? RPAREN	# ErodeFunc
		/**
		  morph_open(x, [kernel]) - applies morphological opening to x. kernel is size of used matrix.
		*/
	| MORPH_OPEN LPAREN expr (COMMA expr)? RPAREN	# MorphOpenFunc
		/**
		  morph_close(x, [kernel]) - applies morphological closing to x. kernel is size of used matrix.
		*/
	| MORPH_CLOSE LPAREN expr (COMMA expr)? RPAREN	# MorphCloseFunc
		/**
		  int(x) - casts x to integer
		*/
	| INT LPAREN expr RPAREN    # IntFunc
		/**
		  float(x) - casts x to float
		*/
	| FLOAT LPAREN expr RPAREN    # FloatFunc
		/**
		  flow_magnitude(x) - computes the magnitude of optical flow (or any other structure with last dimension of 2)
		*/
	| FLOW_MAG LPAREN expr RPAREN	# FlowMagFunc
		/**
		  flow_angle(x) - computes the angle of optical flow (basically angle() but real and imaginery is separate in 2 dimensions)
		*/
	| FLOW_ANG LPAREN expr RPAREN	# FlowAngFunc
	    /**
		    as_nested(x) - converts a list to a nested tensor (special object containing tensors of different shapes behaving like a tensor)
		  */
	| AS_NESTED LPAREN expr RPAREN	# AsNestedFunc
		/**
		  svd(x, [full_matrices]) - computes the singular value decomposition of x. Returns a list of 3 tensors: U, S, V such that x = matmul(matmul(U, diagonal_matrix(S,shape(U))), V)
		*/
		| SVD LPAREN expr (COMMA expr)? RPAREN	# SvdFunc;

func2:
		/**
		  pow(x, y) - computes x raised to the power of y
		*/
	POWE LPAREN expr COMMA expr RPAREN			# PowFunc
		/**
		  atan2(y, x) - computes the arc tangent of y/x, using the signs of both arguments to determine the quadrant
		*/
	| ATAN2 LPAREN expr COMMA expr RPAREN			# Atan2Func
		/**
		  hypot(x, y) - computes the element-wise Euclidean distance from the origin
		*/
	| HYPOT LPAREN expr COMMA expr RPAREN			# HypotFunc
		/**
		  logaddexp(x, y) - computes log(exp(x) + exp(y)) element-wise using a numerically stable method
		*/
	| LOGADDEXP LPAREN expr COMMA expr RPAREN		# LogaddexpFunc
		/**
		  logical_and(x, y) - returns 1.0 if both values are non-zero, else 0.0
		*/
	| LOGICAL_AND LPAREN expr COMMA expr RPAREN		# LogicalAndFunc
		/**
		  logical_or(x, y) - returns 1.0 if either value is non-zero, else 0.0
		*/
	| LOGICAL_OR LPAREN expr COMMA expr RPAREN		# LogicalOrFunc
		/**
		  isclose(a, b, [rtol], [atol]) - elementwise approximate equality test
		*/
	| ISCLOSE LPAREN expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN	# IscloseFunc
		/**
		  allclose(a, b, [rtol], [atol]) - returns 1.0 if all elements are approximately equal, else 0.0
		*/
	| ALLCLOSE LPAREN expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN	# AllcloseFunc
		/**
		  tmin(x, y) - elementwise minimum of tensor or list. min(x,y) when inputs are floats
		*/
	| TMIN LPAREN expr COMMA expr RPAREN			# TMinFunc
		/**
		  tmax(x,y) - elementwise maximum of tensor or list. max(x,y) when inputs are floats
		*/
	| TMAX LPAREN expr COMMA expr RPAREN			# TMaxFunc
		/**
		  snorm(x,[dim]) - frobenius norm of tensor. Along dimension if dimension specified. Dimension can be a list. Defaults to no dimension.
		*/
	| SNORM LPAREN expr (COMMA expr)? RPAREN		# SNormFunc
		/**
		  step(x, edge) - returns 0 if x < edge, else 1
		*/
	| STEP LPAREN expr COMMA expr RPAREN			# StepFunc
		/**
		  topk(x, k, [dim]) - returns the k largest elements along dim. For tensors it keeps them in place; dim defaults to the last.
		*/
	| TOPK LPAREN expr COMMA expr (COMMA expr)? RPAREN			# TopkFunc
		/**
		  botk(x, k, [dim]) - returns the k smallest elements along dim. For tensors it keeps them in place; dim defaults to the last.
		*/
	| BOTK LPAREN expr COMMA expr (COMMA expr)? RPAREN			# BotkFunc
		/**
		  quartile(x, q, [dim]) - computes the q-th quartile globally or along dim
		*/
	| QUARTILE LPAREN expr COMMA expr (COMMA expr)? RPAREN		# QuartileFunc
		/**
		  percentile(x, p, [dim]) - computes the p-th percentile globally or along dim
		*/
	| PERCENTILE LPAREN expr COMMA expr (COMMA expr)? RPAREN		# PercentileFunc
		/**
		  quantile(x, q, [dim]) - computes the q-th quantile globally or along dim
		*/
	| QUANTILE LPAREN expr COMMA expr (COMMA expr)? RPAREN		# QuantileFunc
		/**
		  dot(x, y) - computes the dot product of x and y after flattening both to 1D. Use cross(x, y) if you need a per-vector product with the last dimension kept.
		*/
	| DOT LPAREN expr COMMA expr RPAREN			# DotFunc
		/**
		  outer(x, y) - computes the outer product of flattened x and y
		*/
	| OUTER LPAREN expr COMMA expr RPAREN		# OuterFunc
		/**
		  cosine_similarity(x, y) - computes the cosine similarity between x and y.
		*/
	| COSSIM LPAREN expr COMMA expr RPAREN			# CossimFunc
		/**
		  startswith(text, prefix) - returns 1 if text starts with prefix, else 0
		*/
	| STARTSWITH LPAREN expr COMMA expr RPAREN		# StartswithFunc
		/**
		  endswith(text, suffix) - returns 1 if text ends with suffix, else 0
		*/
	| ENDSWITH LPAREN expr COMMA expr RPAREN			# EndswithFunc
		/**
		  logsumexp(x, [dims]) - computes log(sum(exp(x))) stably, optionally reducing along one or more dimensions
		*/
	| LOGSUMEXP LPAREN expr (COMMA expr)? RPAREN		# LogsumexpFunc
		/**
		  rfft(x, [dim]) - computes the one-dimensional real-input FFT along dim (default: last dimension)
		*/
	| RFFT LPAREN expr (COMMA expr)? RPAREN		# RfftFunc
		/**
		  trace(x) - sums the main diagonal of each square matrix in x
		*/
	| TRACE LPAREN expr RPAREN			# TraceFunc
		/**
		  det(x) - computes the determinant of each square matrix in x
		*/
	| DET LPAREN expr RPAREN			# DetFunc
		/**
		  flip(x, dims) - reverses the order of elements along the specified dimensions. Works also for text and list with dims=0
		*/
	| FLIP LPAREN expr COMMA expr RPAREN			# FlipFunc
		/**
		  cov(x, y) - computes the covariance matrix of x and y
		*/
	| COV LPAREN expr COMMA expr RPAREN			# CovFunc
		/**
		  correlation(x, y) - computes the correlation between x and y
		*/
	| CORR LPAREN expr COMMA expr RPAREN			# CorrFunc
		/**
		  append(x, y) - appends y to the end of x. If inputs are tensors use concatenate(x,...,dim)
		*/
		| APPEND LPAREN expr COMMA expr RPAREN			# AppendFunc
			/**
			  add_key(dict, key, value) - adds or replaces a dictionary entry and returns the updated dictionary
			*/
		| ADD_KEY LPAREN expr COMMA expr COMMA expr RPAREN	# AddKeyFunc
			/**
			  permute(x, dims) - permutes the dimensions of tensor x according to dims
			*/
		| PERM LPAREN expr COMMA expr RPAREN			# PermuteFunc
		/**
		  gaussian(x, sigma, [reshape]) - applies a Gaussian blur to x with specified sigma. if reshape has value of 1.0, then it tries orienting the input such that channel is in the direction of filter. Otherwise it expect color dimension to be the last.
		*/
	| GAUSSIAN LPAREN expr COMMA expr (COMMA expr)? RPAREN	# GaussianFunc
		/**
		  topk_indices(x, k, [dim]) - returns the indices of the k largest elements along dim; dim defaults to the last
		*/
	| TOPK_IND LPAREN expr COMMA expr (COMMA expr)? RPAREN		# TopkIndFunc
		/**
		  botk_indices(x, k, [dim]) - returns the indices of the k smallest elements along dim; dim defaults to the last
		*/
	| BOTK_IND LPAREN expr COMMA expr (COMMA expr)? RPAREN		# BotkIndFunc
		/**
		  batch_shuffle(x, indices) - shuffles and duplicates or skips the batch dimension of x according to indices
		*/
	| BATCH_SHUFFLE LPAREN expr COMMA expr RPAREN		# BatchShuffleFunc
		/**
		  stack_push(slot, val) - pushes val onto the end of slot stack
		*/
	| PUSH LPAREN expr COMMA expr RPAREN			# PushFunc
		/**
		  get_value(slot) - returns the value at slot from stack
		*/
	| GET_VALUE LPAREN expr COMMA expr RPAREN		# GetValueFunc
		/**
		  tensor(shape, [value], [dtype_template]) - creates a tensor with specified shape and optional value/type. Default value is 0 and default format FP32
		*/
	| TENSOR LPAREN indexExpr (COMMA expr (COMMA expr)? )? RPAREN	# EmptyTensorFunc
		/**
		  zeros(shape, [dtype_template]) - creates a zero-filled tensor on the current device
		*/
	| ZEROS LPAREN expr (COMMA expr)? RPAREN	# ZerosFunc
		/**
		  ones(shape, [dtype_template]) - creates a one-filled tensor on the current device
		*/
	| ONES LPAREN expr (COMMA expr)? RPAREN		# OnesFunc
		/**
		  eye(n, [dtype_template]) - creates an n-by-n identity matrix
		*/
	| EYE LPAREN expr (COMMA expr)? RPAREN		# EyeFunc
		/**
		  one_hot(indices, classes) - converts integer class indices to float32 one-hot vectors
		*/
	| ONE_HOT LPAREN expr COMMA expr RPAREN		# OneHotFunc
		/**
		  mse(a, b, [reduction]) - mean squared error; reduction is mean (default), sum, or none
		*/
	| MSE LPAREN expr COMMA expr (COMMA expr)? RPAREN	# MseFunc
		/**
		  mae(a, b, [reduction]) - mean absolute error; reduction is mean (default), sum, or none
		*/
	| MAE LPAREN expr COMMA expr (COMMA expr)? RPAREN	# MaeFunc
		/**
		  psnr(a, b, [data_range]) - peak signal-to-noise ratio in dB; data_range defaults to 1
		*/
	| PSNR LPAREN expr COMMA expr (COMMA expr)? RPAREN	# PsnrFunc
		/**
		  weighted_mean(x, weights, [dims]) - computes the weighted mean globally or along one or more dimensions
		*/
	| WEIGHTED_MEAN LPAREN expr COMMA expr (COMMA expr)? RPAREN	# WeightedMeanFunc
		/**
		  huber_loss(prediction, target, [delta], [reduction]) - computes Huber loss; delta defaults to 1 and reduction to mean
		*/
	| HUBER_LOSS LPAREN expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN	# HuberLossFunc
		/**
		  cross_entropy(logits, target, [dim], [reduction]) - computes cross-entropy from class logits and class indices or target probabilities
		*/
	| CROSS_ENTROPY LPAREN expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN	# CrossEntropyFunc
		/**
		  leaky_relu(x, [negative_slope]) - applies leaky ReLU element-wise; negative_slope defaults to 0.01
		*/
	| LEAKY_RELU LPAREN expr (COMMA expr)? RPAREN		# LeakyReluFunc
		/**
		  pad(x, padding) - pads tensor x with specified padding (dim 0 neg, dim 0 pos, dim 1 ...)
		*/
	| PAD LPAREN expr COMMA expr RPAREN			# PadFunc
		/**
		  cross(x, y) - computes the cross product of x and y. Last dimension must be 3
		*/
	| CROSS LPAREN expr COMMA expr RPAREN			# CrossFunc
		/**
		  matmul(x, y) - computes the matrix multiplication of x and y
		*/
	| MATMUL LPAREN expr COMMA expr RPAREN			# MatmulFunc
		/**
		  solve(A, b) - solves the square linear system A*x=b without explicitly forming A inverse
		*/
	| SOLVE LPAREN expr COMMA expr RPAREN		# SolveFunc
		/**
		  flow_apply(image, flow) - applies optical flow to an image
		*/
	| FLOW_APPLY LPAREN expr COMMA expr RPAREN		# FlowApplyFunc
		/**
		  rife(image1, image2, [tiling_size], [iterations], [multi_scale]) - computes the optical flow field ([H, W, 2]) between image1 and image2 using a RAFT-based model
		  - tiling_size: chuncks image to overlapping tiling_size*tiling_size parts to conserve memory. Default is 0 (auto: enables 1024x1024 tiling when over 2MPx). When tiling_size is between 0 - 1 it takes as a fraction of the resolution
		  - iterations: how many times to run the flow model. Default 12
		  - multi_scale: also use low resolution of base image for giant movements. Default false
		*/
	| RIFE LPAREN expr COMMA expr (COMMA expr (COMMA expr (COMMA expr)?)?)? RPAREN # RifeFunc
		/**
		  bitwise_and(x, y) - computes the element-wise bitwise AND of x and y
		*/
	| BAND LPAREN expr COMMA expr RPAREN			# BitAndFunc
		/**
		  bitwise_xor(x, y) - computes the element-wise bitwise XOR of x and y
		*/
	| XOR LPAREN expr COMMA expr RPAREN			# BitXorFunc
		/**
		  bitwise_or(x, y) - computes the element-wise bitwise OR of x and y
		*/
	| BOR LPAREN expr COMMA expr RPAREN			# BitOrFunc
		/**
		  split(x, [delimiter]) - splits string to list of strings based on delimiter. Default is space.
		*/
	| SPLIT LPAREN expr (COMMA expr)? RPAREN		# SplitFunc
		/**
		  join(x, [separator]) - joins strings in list using separator. Defalut separator is "". If you want to join tensors use concatinate(...)
		*/
	| JOIN LPAREN expr (COMMA expr)? RPAREN			# JoinFunc
		/**
		  substring(s, start, [length]) - returns length characters of s starting at start. If length is not supplied, it returns the rest of the string
		*/
	| SUBSTRING LPAREN expr COMMA expr (COMMA expr)? RPAREN # SubstringFunc
		/**
		  find(s, sub) - returns the index of the first occurrence of sub in s. -1 if not found. Works only for strings.
		*/
	| FIND LPAREN expr COMMA expr RPAREN			# FindFunc
		/**
		  replace(s, old, new) - replaces occurrences of old with new in s. Mostly for strings but can work with lists and tensors.
		*/
	| REPLACE LPAREN expr COMMA expr COMMA expr RPAREN	# ReplaceFunc
		/**
		  int_to_rgb(val) - converts an integer to an RGB color. If input is tensor it stacks the resulting R, G and B tensors using last dimension. If It is list, List of lists is returned and if value, 3 long list is returned.
		*/
	| INT_TO_RGB LPAREN expr RPAREN				# Int_to_rgbFunc
		/**
		  rgb_to_int(r, [g, b]) - converts RGB components to an integer It uses last dimension of tensor (or list) as R,G,B if one value. Othervise uses whole thing as channel.
		*/
	| RGB_TO_INT LPAREN expr ( COMMA expr COMMA expr)? RPAREN	# Rgb_to_intFunc
		/**
		  interpolate_linear(x, y) - performs linear interpolation on X. Assumes that dim 0 is batch and dim 1 = channel
		*/
	| INTERPOLATE_LINEAR LPAREN expr COMMA expr RPAREN	# InterpolateLinearFunc
		/**
		  interpolate_area(x, y) - performs area interpolation X. Assumes that dim 0 is batch and dim 1 = channel
		*/
	| INTERPOLATE_AREA LPAREN expr COMMA expr RPAREN	# InterpolateAreaFunc
		/**
		  interpolate_nearest_exact(x, y) - performs nearest neighbor interpolation X. Assumes that dim 0 is batch and dim 1 = channel
		*/
	| INTERPOLATE_NEAREST LPAREN expr COMMA expr RPAREN	# InterpolateNearestExactFunc
		/**
		  remove_key(dict, key) - removes a dictionary entry and returns the updated dictionary
		*/
	| REMOVE_KEY LPAREN expr COMMA expr RPAREN	# RemoveKeyFunc;


func3:
		/**
		  clamp(x, min, max) - clamps x between min and max per element
		*/
	CLAMP LPAREN expr COMMA expr COMMA expr RPAREN		# ClampFunc
		/**
		  lerp(a, b, t) - linear interpolation between a and b by t per element. t can be float or tensor.
		*/
	| LERP LPAREN expr COMMA expr COMMA expr RPAREN		# LerpFunc
		/**
		  smoothstep(x, edge0, edge1) - smooth interpolation between edge0 and edge1
		*/
	| SMOOTHSTEP LPAREN expr COMMA expr COMMA expr RPAREN	# SmoothstepFunc
		/**
		  transpose(x, dim0, dim1) / swapaxes(x, dim0, dim1) - swaps two tensor dimensions
		*/
	| TRANSPOSE LPAREN expr COMMA expr COMMA expr RPAREN	# TransposeFunc
		/**
		  range(start, stop, step) - creates a range of values between start (inclusive) and stop (exclusive) using step. Use linspace if you want value count.
		*/
	| RANGE LPAREN expr COMMA expr COMMA expr RPAREN	# RangeFunc
		/**
		  moment(x, a, k) - computes the k-th moment of x around a
		*/
	| MOMENT LPAREN expr COMMA expr COMMA expr RPAREN	# MomentFunc
		/**
		  cubic_ease(a, b, t) - cubic ease between a and b
		*/
	| CUBIC_EASE LPAREN expr COMMA expr COMMA expr RPAREN	# CubicEaseFunc
		/**
		  elastic_ease(a, b, t) - elastic ease between a and b
		*/
	| ELASTIC_EASE LPAREN expr COMMA expr COMMA expr RPAREN	# ElasticEaseFunc
		/**
		  sine_ease(a, b, t) - sine easing between a and b
		*/
	| SINE_EASE LPAREN expr COMMA expr COMMA expr RPAREN	# SineEaseFunc
		/**
		  smootherstep(x, edge0, edge1) - smoother interpolation between edge0 and edge1
		*/
	| SMOOTHERSTEP LPAREN expr COMMA expr COMMA expr RPAREN	# SmootherstepFunc
		/**
		  crop(x, start, size) - crops tensor x. Take size and begin at start. start should be the low corner. The result is at most size (if size is bigger then rest of tensor).
		*/
	| CROP LPAREN expr COMMA expr COMMA expr RPAREN		# CropFunc
		/**
		  ifft(x, [shape]) - inverse fast Fourier transform of x. shape (defaults to the node's tensor shape) sizes the K/Kx/Ky/.../frequency variables made available while evaluating x, it does not resize x itself.
		*/
	| SIFFT LPAREN expr (COMMA expr)? RPAREN		# SifftFunc
		/**
		  irfft(x, [n], [dim]) - computes the inverse one-dimensional real FFT along dim (default: last dimension)
		*/
	| IRFFT LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN	# IrfftFunc
		/**
		  overlay(base, overlay, offset, [opacity]) - overlays overlay on base at offset. Opacity controls blending. It can be tensor or float. If it is tensor it should be the same shape as overlay.
		*/
	| OVERLAY LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# OverlayFunc
		/**
		  linspace(start, stop, num) - creates num linearly spaced values from start to stop (inclusive). Use range if you want to control the step between values.
		*/
	| LINSPACE LPAREN expr COMMA expr COMMA expr RPAREN	# LinspaceFunc
		/**
		  roll(x, shifts, [axis]) - rolls tensor x along axis
		*/
	| ROLL LPAREN expr COMMA expr (COMMA expr)? RPAREN	# RollFunc
		/**
		  rgb_to_oklab(r, [g], [b]) - converts RGB to OKLab. It has 2 modes. Aither 1 or 3 parameters. With 1 parameter it expects last dimension of 3 and with 3 it concatinates them after converting.
		*/
	| RGB_TO_OKLAB LPAREN expr (COMMA expr COMMA expr)? RPAREN	# RgbToOklabFunc
		/**
		  rgb_to_cielab(r, [g], [b]) - converts RGB to CIELAB. It has 2 modes. Aither 1 or 3 parameters. With 1 parameter it expects last dimension of 3 and with 3 it concatinates them after converting.
		*/
	| RGB_TO_CIELAB LPAREN expr (COMMA expr COMMA expr)? RPAREN	# RgbToCielabFunc
		/**
		  rgb_to_hsv(rgb, [degrees]) / rgb_to_hsv(r, g, b, [degrees]) - converts RGB to HSV. It has 2 modes. Aither 1 or 3 parameters. With 1 parameter it expects last dimension of 3 and with 3 it concatinates them after converting. If degrees is specified and nonzero it returns hue as 0-360 instead of 0-1
		*/
	| RGB_TO_HSV LPAREN expr (COMMA expr COMMA expr)? (COMMA expr)? RPAREN	# RgbToHsvFunc
		/**
		  hsv_to_rgb(hsv, [degrees]) / hsv_to_rgb(h, s, v, [degrees]) - converts HSV to RGB. It has 2 modes. Aither 1 or 3 parameters. With 1 parameter it expects last dimension of 3 and with 3 it concatinates them after converting.
		*/
	| HSV_TO_RGB LPAREN expr (COMMA expr COMMA expr)? (COMMA expr)? RPAREN	# HsvToRgbFunc
		/**
		  where(condition, x, y) - returns x if condition is true, else y. Runs per element.
		*/
	| WHERE LPAREN expr COMMA expr COMMA expr RPAREN			# WhereFunc
		/**
		  oklab_to_rgb(oklab) / oklab_to_rgb(l, a, b) - converts OKLab to RGB. It has 2 modes. Aither 1 or 3 parameters. With 1 parameter it expects last dimension of 3 and with 3 it concatinates them after converting.
		*/
	| OKLAB_TO_RGB LPAREN expr (COMMA expr COMMA expr)? RPAREN		# OklabToRgbFunc
		/**
		  cielab_to_rgb(cielab) / cielab_to_rgb(l, a, b) - converts CIELAB to RGB. It has 2 modes. Aither 1 or 3 parameters. With 1 parameter it expects last dimension of 3 and with 3 it concatinates them after converting.
		*/
	| CIELAB_TO_RGB LPAREN expr (COMMA expr COMMA expr)? RPAREN		# CielabToRgbFunc
		/**
		  text_image(text, font, size, [max_width], [weight], [rotation_angle], [line_spacing], [italic], [underline]) - renders text to an 2D tensor
		*/
	| TEXT_IMAGE LPAREN expr COMMA expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN	# TextImageFunc
	    /**
		  coords(shape, dim, [dtype]) - generates a tensor with the specified shape whose values are the coordinates of each element along the specified dimension. The dtype can be specified to control the data type of the output tensor.
		*/
	| COORDS LPAREN expr COMMA expr (COMMA expr)? RPAREN	# CoordsFunc
	    /**
		   gather(x, dim, idx) - gathers elements along dim using the indices specified in idx. The output tensor has the same shape as idx.
		   */
	| GATHER LPAREN expr COMMA expr COMMA expr RPAREN	# GatherFunc
	    /**
		  scatter(x, dim, idx, src) - scatters elements from src into x along dim using the indices specified in idx. The output tensor has the same shape as x.
		*/
	| SCATTER LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# ScatterFunc
		/**
		  scatter_add(x, dim, idx, src) - scatters elements from src into x along dim using the indices specified in idx, adding to existing values. The output tensor has the same shape as x.
		*/
	| SCATTER_ADD LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# ScatterAddFunc;

func4:
		/**
		  swap(x, dim, idx1, idx2) - swaps elements along dim between idx1 and idx2
		*/
	SWAP LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# SwapFunc
		/**
		  nan_to_num(x, nan, pos_inf, neg_inf) - null value replacement - inspired by NVL
		*/
	| NVL LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# NvlFunc
		/**
		  logspace(start, stop, num, base) - creates logarithmically spaced values
		*/
	| LOGSPACE LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# LogspaceFunc
		/**
		  distance(x1, y1, x2, y2) - computes Euclidean distance between (x1, y1) and (x2, y2)
		*/
	| DIST LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# DistFunc
		/**
		  histogram(x, bins, min, max) - computes histogram
		*/
	| HISTOGRAM LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# HistogramFunc;

func5:
		/**
		  remap(v, i_min, i_max, o_min, o_max) - remaps values from input range to output range
		*/
	REMAP LPAREN expr COMMA expr COMMA expr COMMA expr COMMA expr RPAREN # RemapFunc
    	/**
		  diagonal_matrix(x, shape, [offset], [dim1], [dim2]) - creates a diagonal matrix from x with specified shape. offset is the diagonal offset. dim1 and dim2 are the dimensions to place the diagonal on.
		  */
		  | DIAG LPAREN expr COMMA expr (COMMA expr (COMMA expr (COMMA expr)?)?)? RPAREN # DiagonalMatrixFunc;

// N-argument functions
funcN:
		/**
		  norm(x, [p], [dims]) - computes the p-norm globally or along one or more dimensions (default p=2)
		*/
	NORM LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN	# NormFunc
		/**
		  normalize(x, [p], [dim], [eps]) - normalizes x along dim using the p-norm (defaults: p=2, dim=-1, eps=1e-12)
		*/
	| NORMALIZE LPAREN expr (COMMA expr (COMMA expr (COMMA expr)?)?)? RPAREN	# NormalizeFunc
		/**
		  smin(x, ...) - computes the minimum of inputs or elements. Tensors must have the same size or be broadcastable to same size. When called as smin(x, dims) with x a tensor/list, reduces x along dims (a single dim or list of dims) instead.
		*/
	| SMIN LPAREN expr (COMMA expr)* RPAREN		# SMinFunc
		/**
		  smax(x, ...) - computes the maximum of inputs or elements. Tensors must have the same size or be broadcastable to same size. When called as smax(x, dims) with x a tensor/list, reduces x along dims (a single dim or list of dims) instead.
		*/
	| SMAX LPAREN expr (COMMA expr)* RPAREN		# SMaxFunc
		/**
		  map(tensor, coord1, [coord2], [coord3]) - samples/remaps input tensor using coordinates
		*/
	| MAP LPAREN expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN		# MapFunc
		/**
		  ezconvolution(tensor, [kernel_sizes...], kernel) - applies convolution with kernel. Attempts to correctly convolve over size dimensions.
		*/
	| EZCONV LPAREN expr (COMMA expr)+ RPAREN	# EzConvFunc
		/**
		  convolution(tensor, [kernel_sizes...], kernel) - applies convolution with kernel. Expects [batch,channel, ...]
		*/
	| CONV LPAREN expr (COMMA expr)+ RPAREN		# ConvFunc
		/**
		  reshape(x, shape) - reshapes tensor x to the specified shape
		*/
	| RESHAPE LPAREN expr COMMA expr RPAREN		# ReshapeFunc
		/**
		  squeeze(x, [dim]) - removes size-1 dimensions from tensor x, optionally at dim
		*/
	| SQUEEZE LPAREN expr (COMMA expr)? RPAREN		# SqueezeFunc
		/**
		  unsqueeze(x, dim) - inserts a size-1 dimension into tensor x at dim
		*/
	| UNSQUEEZE LPAREN expr COMMA expr RPAREN		# UnsqueezeFunc
		/**
		  concatenate(x, ..., dim) - concatenates one or more tensors along the specified dimension
		*/
	| CONCAT LPAREN expr (COMMA expr)+ RPAREN	# ConcatFunc
		/**
		  stack(tensors, [dim]) - stacks a list of tensors along a new dimension
		*/
	| STACK LPAREN expr (COMMA expr)? RPAREN	# StackFunc
		/**
		  nonzero(x) - returns an N-by-rank tensor of coordinates for nonzero elements
		*/
	| NONZERO LPAREN expr RPAREN			# NonzeroFunc
		/**
		  get_changed_keys(d) - returns list of keys that were modified or added in ChangeTrackingDict d
		*/
	| GET_CHANGED_KEYS LPAREN expr RPAREN		# GetChangedKeysFunc
		/**
		  get_added_keys(d) - returns list of keys that were added (newly created) in ChangeTrackingDict d
		*/
	| GET_ADDED_KEYS LPAREN expr RPAREN			# GetAddedKeysFunc
		/**
		  get_removed_keys(d) - returns list of keys that were removed from ChangeTrackingDict d
		*/
	| GET_REMOVED_KEYS LPAREN expr RPAREN		# GetRemovedKeysFunc
		/**
		  get_unchanged_keys(d) - returns list of keys that remain unchanged in ChangeTrackingDict d
		*/
	| GET_UNCHANGED_KEYS LPAREN expr RPAREN		# GetUnchangedKeysFunc;

funcNoise:
		/**
		  random_normal(seed, [shape]) - generates normally distributed random noise
		*/
	NOISE LPAREN expr (COMMA expr)? RPAREN				# NoiseFunc
		/**
		  pink_noise(seed, [shape]) - generates deterministic pink noise (approximately 1/f power spectrum), normalised per row
		*/
	| PINK_NOISE LPAREN expr (COMMA expr)? RPAREN		# PinkNoiseFunc
		/**
		  brown_noise(seed, [shape]) - generates deterministic brown noise (approximately 1/f^2 power spectrum), normalised per row
		*/
	| BROWN_NOISE LPAREN expr (COMMA expr)? RPAREN		# BrownNoiseFunc
		/**
		  random_uniform(seed, [shape]) - generates uniformly distributed random noise
		*/
	| RAND LPAREN expr (COMMA expr)? RPAREN				# RandFunc
		/**
		  random_exponential(seed, lambda, [shape]) - generates exponentially distributed random values
		*/
	| EXPONENTIAL LPAREN expr COMMA expr (COMMA expr)? RPAREN	# ExponentialFunc
		/**
		  random_bernoulli(seed, probability, [shape]) - generates Bernoulli distributed random values (0 or 1). Probability can be a tensor
		*/
	| BERNOULLI LPAREN expr COMMA expr (COMMA expr)? RPAREN		# BernoulliFunc
		/**
		  random_poisson(seed, lambda, [shape]) - generates Poisson distributed random values.
		*/
	| POISSON LPAREN expr COMMA expr (COMMA expr)? RPAREN		# PoissonFunc
		/**
		  random_cauchy(seed, median, sigma, [shape]) - generates Cauchy distributed random values.
		*/
	| CAUCHY LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# CauchyFunc
		/**
		  random_log_normal(seed, mean, std, [shape]) - generates log-normally distributed random values.
		*/
	| LOGNORMAL LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# LogNormalFunc
		/**
		  random_gamma(seed, shape_param, scale, [shape]) - generates Gamma distributed random values.
		*/
	| GAMMADIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# GammaDistFunc
		/**
		  random_beta(seed, alpha, beta, [shape]) - generates Beta distributed random values
		*/
	| BETADIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# BetaDistFunc
		/**
		  random_laplace(seed, loc, scale, [shape]) - generates Laplace distributed random values
		*/
	| LAPLACEDIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# LaplaceDistFunc
		/**
		  random_gumbel(seed, loc, scale, [shape]) - generates Gumbel distributed random values
		*/
	| GUMBELDIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# GumbelDistFunc
		/**
		  random_weibull(seed, scale, concentration, [shape]) - generates Weibull distributed random values
		*/
	| WEIBULLDIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# WeibullDistFunc
		/**
		  random_chi2(seed, df, [shape]) - generates Chi-squared distributed random values
		*/
	| CHI2DIST LPAREN expr COMMA expr (COMMA expr)? RPAREN	# Chi2DistFunc
		/**
		  random_studentt(seed, df, [shape]) - generates Student-t distributed random values
		*/
	| STUDENTTDIST LPAREN expr COMMA expr (COMMA expr)? RPAREN	# StudentTDistFunc
		/**
		  perlin_noise(seed, scale, [octaves], [offset], [shape]) - generates Perlin noise
		*/
	| PERLIN LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# PerlinFunc
		/**
		  cellular_noise(seed, scale, [jitter], [offset], [shape]) - generates Cellular/Voronoi noise
		*/
	| CELLULAR LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# CellularFunc
		/**
		  plasma_noise(seed, scale, [octaves], [offset], [shape]) - generates Plasma/Turbulence noise - same as perlin but default octaves 4
		*/
	| PLASMA LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# PlasmaFunc
		/**
		  ridged_noise(seed, scale, [octaves], [offset], [shape]) - generates ridged multi-fractal noise
		*/
	| RIDGED LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# RidgedFunc
		/**
		  domain_warp_noise(seed, scale, warp_scale, warp_strength, [octaves], [warp_octaves], [offset], [shape]) - generates domain warped noise
		*/
	| DOMAIN_WARP LPAREN expr COMMA expr COMMA expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN	# DomainWarpFunc;

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
LOG2: 'log2';
EXP: 'exp';
LOG1P: 'log1p';
EXPM1: 'expm1';
CBRT: 'cbrt';
RECIPROCAL: 'reciprocal';
LOGADDEXP: 'logaddexp';
LOGSUMEXP: 'logsumexp';
NORM: 'norm';
NORMALIZE: 'normalize';
OUTER: 'outer';
TRACE: 'trace';
DET: 'det';
RFFT: 'rfft';
IRFFT: 'irfft';
ISNAN: 'isnan';
ISINF: 'isinf';
ISFINITE: 'isfinite';
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
SOFTSIGN: 'softsign';
LEAKY_RELU: 'leaky_relu';
SOFTPLUS: 'softplus';
GELU: 'gelu';
SIGN: 'sign';
DEGREES: 'degrees';
RADIANS: 'radians';
LOGICAL_NOT: 'logical_not';
LOGICAL_AND: 'logical_and';
LOGICAL_OR: 'logical_or';
HYPOT: 'hypot';
MAP: 'map';
EZCONV: 'ezconvolution' | 'ezconv';
CONV: 'convolution' | 'conv';
SWAP: 'swap';
TRANSPOSE: 'transpose' | 'swapaxes';
PERM: 'permute' | 'perm';
RESHAPE: 'reshape' | 'rshp';
RANGE: 'range';
LINSPACE: 'linspace';
LOGSPACE: 'logspace';
TOPK: 'topk';
BOTK: 'botk';
PINV: 'pinv';
INV: 'inv';
SUM: 'sum';
MEAN: 'mean';
STD: 'std';
VAR: 'var';
PROD: 'prod';
ISCLOSE: 'isclose';
ALLCLOSE: 'allclose';
QUARTILE: 'quartile' | 'quartil';
PERCENTILE: 'percentile' | 'prcnt';
QUANTILE: 'quantile';
DOT: 'dot';
MOMENT: 'moment';
ERF: 'erf';
ERFINV: 'erfinv';

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
KEYS: 'keys';
ENABLE_TRACKING: 'enable_tracking' | 'track_on';
DISABLE_TRACKING: 'disable_tracking' | 'track_off';
RESET_TRACKING: 'reset_tracking' | 'track_reset';
GET_CHANGED_KEYS: 'get_changed_keys' | 'changed_keys';
GET_ADDED_KEYS: 'get_added_keys' | 'added_keys';
GET_REMOVED_KEYS: 'get_removed_keys' | 'removed_keys';
GET_UNCHANGED_KEYS: 'get_unchanged_keys' | 'unchanged_keys';
REPEAT: 'repeat';
FLATTEN: 'flatten';
APPEND: 'append';
GET_VALUE: 'get_value';
FLOW_APPLY: 'flow_apply';
BATCH_SHUFFLE: 'batch_shuffle' | 'shuffle' | 'select';
MOTION_MASK: 'motion_mask';
FLOW_TO_IMAGE: 'flow_to_image';
FLOW_MAG: 'flow_mag' | 'flow_magnitude';
FLOW_ANG: 'flow_ang' | 'flow_angle';
WHERE: 'where';
HISTOGRAM: 'histogram' | 'hist';
OVERLAY: 'overlay';
PAD: 'pad';
CROSS: 'cross';
MATMUL: 'matmul';
SOLVE: 'solve';
MATRIX_RANK: 'matrix_rank';
RIFE: 'rife';
BNOT: 'bnot' | 'bitwise_not';
BITCOUNT: 'bitcount' | 'popcount' | 'popcnt';
SHAPE: 'shape';
BAND: 'band' | 'bitwise_and';
XOR: 'bxor' | 'bitwise_xor';
BOR: 'bor' | 'bitwise_or';
TENSOR: 'tensor';
ZEROS: 'zeros';
ONES: 'ones';
EYE: 'eye';
ONE_HOT: 'one_hot';
MSE: 'mse';
MAE: 'mae';
PSNR: 'psnr';
WEIGHTED_MEAN: 'weighted_mean';
HUBER_LOSS: 'huber_loss';
CROSS_ENTROPY: 'cross_entropy';
ADD_KEY: 'add_key';
REMOVE_KEY: 'remove_key' | 'rm_key';
PUSH: 'stack_push';
POP: 'stack_pop';
CLEAR: 'stack_clear';
HAS: 'stack_has';
GET: 'stack_get';
CONCAT: 'cat'|'concat'|'concatenate';
STACK: 'stack';
NONZERO: 'nonzero';
INT: 'int';
FLOAT: 'float';

UPPER: 'upper';
LOWER: 'lower';
TRIM: 'trim';
SPLIT: 'split';
JOIN: 'join';
SUBSTRING: 'substring'|'substr';
FIND: 'find';
REPLACE: 'replace';
DILATE: 'dilate';
ERODE: 'erode';
MORPH_OPEN: 'morph_open';
MORPH_CLOSE: 'morph_close';
RGB_TO_OKLAB: 'rgb_to_oklab';
RGB_TO_CIELAB: 'rgb_to_cielab';
OKLAB_TO_RGB: 'oklab_to_rgb';
CIELAB_TO_RGB: 'cielab_to_rgb';
RGB_TO_HSV: 'rgb_to_hsv';
HSV_TO_RGB: 'hsv_to_rgb';
INT_TO_RGB: 'int_to_rgb';
RGB_TO_INT: 'rgb_to_int';
INTERPOLATE_LINEAR: 'interpolate_linear';
INTERPOLATE_AREA: 'interpolate_area';
INTERPOLATE_NEAREST: 'interpolate_nearest' | 'interpolate_nearest_exact';
TEXT_IMAGE: 'text_image';
AS_NESTED: 'as_nested_tensor' | 'as_nested';
SVD: 'svd'|'singular_value_decomposition';
DIAG: 'diagonal_matrix'|'diag';

IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
IN: 'in';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
TIMESTAMP: 'timestamp'|'now';
SORT: 'sort';
ARGSORT: 'argsort';
ARGMIN: 'argmin';
ARGMAX: 'argmax';
SOFTMAX: 'softmax';
SOFTMIN: 'softmin';
UNIQUE: 'unique';
FLIP: 'flip';
STARTSWITH: 'startswith';
ENDSWITH: 'endswith';
SQUEEZE: 'squeeze';
UNSQUEEZE: 'unsqueeze';
ROLL: 'roll';
COV: 'cov';
CORR: 'corr' | 'correlation';
ENTROPY: 'entropy';
CROP: 'crop';
NONE: 'none'|'None'|'null'|'NULL';
COORDS: 'coords'|'coordinates';
GATHER: 'gather';
SCATTER: 'scatter';
SCATTER_ADD: 'scatter_add';

NOISE: 'noise' | 'randn' | 'random_normal';
PINK_NOISE: 'pink_noise' | 'pink';
BROWN_NOISE: 'brown_noise' | 'brown';
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
RIDGED: 'ridged' | 'ridged_noise';
DOMAIN_WARP: 'domain_warp'|'domain_warp_noise';

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
PLUS_EQ: '+=';
MINUS_EQ: '-=';
MULT_EQ: '*=';
DIV_EQ: '/=';
MOD_EQ: '%=';
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
STRING: '"' (~["\\\r\n] | '\\' .)* '"'
	   | '\'' (~['\\\r\n] | '\\' .)* '\''
	   ;
VARIABLE: [a-zA-Z_] [a-zA-Z_0-9]*;

SL_COMMENT: '#' ~[\r\n]* -> skip;
ML_COMMENT: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;
