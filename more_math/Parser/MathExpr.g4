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

// A lambda binds loosest, so its body takes the whole following expression, ternaries included.
expr: lambdaExpr | ternaryExpr | compExpr;

lambdaExpr: LPAREN paramList RPAREN ARROW (expr | block) # LambdaExp;

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
		  sin(x) - applies sine function to value or each element of value
		  - x: angle in radians (number, list or tensor)
		*/
	SIN LPAREN expr RPAREN				# SinFunc
		/**
		  cos(x) - applies cosine function to value or each element of value
		  - x: angle in radians (number, list or tensor)
		*/
	| COS LPAREN expr RPAREN			# CosFunc
		/**
		  tan(x) - applies tangent function to value or each element of value
		  - x: angle in radians (number, list or tensor)
		*/
	| TAN LPAREN expr RPAREN			# TanFunc
		/**
		  asin(x) - applies arcus sine function to value or each element of value
		  - x: value in -1..1 (number, list or tensor)
		*/
	| ASIN LPAREN expr RPAREN			# AsinFunc
		/**
		  acos(x) - applies arcus cosine function to value or each element of value
		  - x: value in -1..1 (number, list or tensor)
		*/
	| ACOS LPAREN expr RPAREN			# AcosFunc
		/**
		  atan(x) - applies arcus tangent function to value or each element of value
		  - x: number, list or tensor; applied to each element
		*/
	| ATAN LPAREN expr RPAREN			# AtanFunc
		/**
		  sinh(x) - applies hyperbolic sine function to value or each element of value
		  - x: number, list or tensor; applied to each element
		*/
	| SINH LPAREN expr RPAREN			# SinhFunc
		/**
		  cosh(x) - applies hyperbolic cosine function to value or each element of value
		  - x: number, list or tensor; applied to each element
		*/
	| COSH LPAREN expr RPAREN			# CoshFunc
		/**
		  tanh(x) - applies hyperbolic tangent function to value or each element of value
		  - x: number, list or tensor; applied to each element
		*/
	| TANH LPAREN expr RPAREN			# TanhFunc
		/**
		  asinh(x) - applies hyperbolic arcus sine function to value or each element of value
		  - x: number, list or tensor; applied to each element
		*/
	| ASINH LPAREN expr RPAREN			# AsinhFunc
		/**
		  acosh(x) - applies hyperbolic arcus cosine function to value or each element of value
		  - x: value >= 1 (number, list or tensor)
		*/
	| ACOSH LPAREN expr RPAREN			# AcoshFunc
		/**
		  atanh(x) - applies hyperbolic arcus tangent function to value or each element of value
		  - x: value in -1..1 (number, list or tensor)
		*/
	| ATANH LPAREN expr RPAREN			# AtanhFunc
		/**
		  abs(x) - applies per element absolute value function. Same as |x| for numbers.
		  - x: number, list or tensor; applied to each element
		*/
	| ABS LPAREN expr RPAREN			# AbsFunc
		/**
		  sqrt(x) - applies square root per element. Negative numbers return NaN (not a number)
		  - x: non-negative values (number, list or tensor)
		*/
	| SQRT LPAREN expr RPAREN			# SqrtFunc
		/**
		  ln(x) - applies natural logarithm to value (per element). Negative numbers return NaN (not a number)
		  - x: positive values (number, list or tensor)
		*/
	| LN LPAREN expr RPAREN				# LnFunc
		/**
		  log(x) - applies base 10 logarithm to value (per element). Negative numbers return NaN (not a number)
		  - x: positive values (number, list or tensor)
		*/
	| LOG LPAREN expr RPAREN			# LogFunc
		/**
		  log2(x) - applies base 2 logarithm to value (per element). Negative numbers return NaN (not a number)
		  - x: positive values (number, list or tensor)
		*/
	| LOG2 LPAREN expr RPAREN			# Log2Func
		/**
		  exp(x) - applies e^x to value (per element)
		  - x: number, list or tensor; applied to each element
		*/
		| EXP LPAREN expr RPAREN			# ExpFunc
			/**
			  log1p(x) - applies ln(1+x) accurately for values near zero
			  - x: values greater than -1 (number, list or tensor)
			*/
		| LOG1P LPAREN expr RPAREN			# Log1pFunc
			/**
			  expm1(x) - applies exp(x)-1 accurately for values near zero
			  - x: number, list or tensor; applied to each element
			*/
		| EXPM1 LPAREN expr RPAREN			# Expm1Func
		/**
		  sinc(x) - computes the normalized sinc function sin(pi*x)/(pi*x), with sinc(0)=1
		  - x: number, list or tensor; applied to each element
		*/
		| SINC LPAREN expr RPAREN			# SincFunc
		/**
		  cbrt(x) - computes the real cube root of each value, including negative values
		  - x: number, list or tensor; applied to each element
		*/
		| CBRT LPAREN expr RPAREN			# CbrtFunc
		/**
		  reciprocal(x) - computes 1/x element-wise
		  - x: number, list or tensor; applied to each element
		*/
		| RECIPROCAL LPAREN expr RPAREN		# ReciprocalFunc
			/**
			  isnan(x) - returns 1.0 for NaN values and 0.0 otherwise
			  - x: number, list or tensor; applied to each element
			*/
		| ISNAN LPAREN expr RPAREN			# IsnanFunc
			/**
			  isinf(x) - returns 1.0 for infinite values and 0.0 otherwise
			  - x: number, list or tensor; applied to each element
			*/
		| ISINF LPAREN expr RPAREN			# IsinfFunc
			/**
			  isfinite(x) - returns 1.0 for finite values and 0.0 otherwise
			  - x: number, list or tensor; applied to each element
			*/
		| ISFINITE LPAREN expr RPAREN			# IsfiniteFunc
		/**
		  tnorm(x, [dim]) - normalises tensor or list by multiplication such that sum(x^2)==1.0 for each slice. Defaults to the last dimension; dim selects a different slicing dimension.
		  - x: tensor or list to normalise
		  - dim: dimension whose slices are normalised (default: last)
		*/
		| TNORM LPAREN expr (COMMA expr)? RPAREN			# TNormFunc
		/**
		  floor(x) - returns the largest integer less than or equal to x
		  - x: number, list or tensor; applied to each element
		*/
	| FLOOR LPAREN expr RPAREN			# FloorFunc
		/**
		  ceil(x) - returns the smallest integer greater than or equal to x
		  - x: number, list or tensor; applied to each element
		*/
	| CEIL LPAREN expr RPAREN			# CeilFunc
		/**
		  round(x) - rounds x to the nearest integer
		  - x: number, list or tensor; applied to each element
		*/
	| ROUND LPAREN expr RPAREN			# RoundFunc
		/**
		  gamma(x) - computes the gamma function (per element)
		  - x: number, list or tensor; applied to each element
		*/
	| GAMMA LPAREN expr RPAREN			# GammaFunc
		/**
		  sigm(x) - applies the sigmoid function: 1 / (1 + exp(-x))
		  - x: number, list or tensor; applied to each element
		*/
	| SIGM LPAREN expr RPAREN			# sigmoidFunc
		/**
		  angle(x) - returns the angle of a complex number or vector
		  - x: complex or real values (number, list or tensor)
		*/
	| ANGL LPAREN expr RPAREN			# anglFunc
		/**
		  print(x) - prints the value of x to the console while passing output unchanged
		  - x: value to print; it is also returned unchanged
		*/
	| PRNT LPAREN expr RPAREN			# printFunc
		/**
		  fract(x) - returns the fractional part of x: x - floor(x)
		  - x: number, list or tensor; applied to each element
		*/
	| FRACT LPAREN expr RPAREN			# FractFunc
		/**
		  relu(x) - applies rectified linear unit function: max(0, x)
		  - x: number, list or tensor; applied to each element
		*/
	| RELU LPAREN expr RPAREN			# ReluFunc
		/**
		  softsign(x) - applies x / (1 + abs(x)) element-wise
		  - x: number, list or tensor; applied to each element
		*/
	| SOFTSIGN LPAREN expr RPAREN			# SoftsignFunc
		/**
		  softplus(x) - applies the softplus function: ln(1 + exp(x))
		  - x: number, list or tensor; applied to each element
		*/
	| SOFTPLUS LPAREN expr RPAREN			# SoftplusFunc
		/**
		  gelu(x) - applies the Gaussian Error Linear Unit (GELU) activation function
		  - x: number, list or tensor; applied to each element
		*/
	| GELU LPAREN expr RPAREN			# GeluFunc
		/**
		  silu(x) - applies the Sigmoid Linear Unit activation element-wise
		  - x: number, list or tensor; applied to each element
		*/
	| SILU LPAREN expr RPAREN			# SiluFunc
		/**
		  sign(x) - returns the sign of x: -1, 0, or 1
		  - x: number, list or tensor; applied to each element
		*/
	| SIGN LPAREN expr RPAREN			# SignFunc
		/**
	  degrees(x) - converts radians to degrees (per element)
	  - x: angle in radians (number, list or tensor)
	*/
	| DEGREES LPAREN expr RPAREN			# DegreesFunc
		/**
	  radians(x) - converts degrees to radians (per element)
	  - x: angle in degrees (number, list or tensor)
	*/
	| RADIANS LPAREN expr RPAREN			# RadiansFunc
		/**
	  logical_not(x) - returns 1.0 where x is zero and 0.0 otherwise
	  - x: values; zero counts as false (number, list or tensor)
	*/
	| LOGICAL_NOT LPAREN expr RPAREN		# LogicalNotFunc
		/**
		  print_shape(x) - prints the shape of the tensor x
		  - x: value whose shape is printed; it is also returned unchanged
		*/
	| PRINT_SHAPE LPAREN expr RPAREN		# PrintShapeFunc
		/**
		  pinv(permutation) - computes the inverse permutation: where permutation[i] == j the result has result[j] == i. Not the matrix pseudoinverse; use inv(matrix, 1) for that
		  - permutation: list or tensor holding each index exactly once
		*/
	| PINV LPAREN expr RPAREN			# PinvFunc
		/**
		  inv(x, [pseudo]) - computes the matrix inverse; when pseudo is truthy, computes the Moore-Penrose pseudoinverse instead
		  - x: matrix, or a batch of matrices in the last two dimensions
		  - pseudo: truthy to compute the Moore-Penrose pseudoinverse, which also works for singular and non-square matrices (default: false)
		*/
	| INV LPAREN expr (COMMA expr)? RPAREN		# InvFunc
		/**
		  matrix_rank(x, [tol]) - computes the numerical rank of each matrix using optional absolute tolerance tol
		  - x: matrix, or a batch of matrices in the last two dimensions
		  - tol: absolute tolerance below which singular values count as zero
		*/
	| MATRIX_RANK LPAREN expr (COMMA expr)? RPAREN	# MatrixRankFunc
		/**
		  sum(x, [dims]) - computes the sum of elements of x, optionally along one or more dimensions
		  - x: values to add up (number, list or tensor)
		  - dims: dimension or list of dimensions to reduce (default: all elements)
		*/
	| SUM LPAREN expr (COMMA expr)? RPAREN		# SumFunc
		/**
		  mean(x, [dims]) - computes the arithmetic mean of elements of x globally or along one or more dimensions
		  - x: values to average (number, list or tensor)
		  - dims: dimension or list of dimensions to reduce (default: all elements)
		*/
	| MEAN LPAREN expr (COMMA expr)? RPAREN		# MeanFunc
		/**
		  std(x, [dims]) - computes the sample standard deviation of elements of x globally or along one or more dimensions
		  - x: values (number, list or tensor)
		  - dims: dimension or list of dimensions to reduce (default: all elements)
		*/
	| STD LPAREN expr (COMMA expr)? RPAREN		# StdFunc
		/**
		  var(x, [dims]) - computes the sample variance of elements of x globally or along one or more dimensions
		  - x: values (number, list or tensor)
		  - dims: dimension or list of dimensions to reduce (default: all elements)
		*/
	| VAR LPAREN expr (COMMA expr)? RPAREN		# VarFunc
		/**
		  prod(x, [dims]) - computes the product of elements of x globally or along one or more dimensions
		  - x: values to multiply (number, list or tensor)
		  - dims: dimension or list of dimensions to reduce (default: all elements)
		*/
	| PROD LPAREN expr (COMMA expr)? RPAREN		# ProdFunc
		/**
		  sort(x, [descending], [dim]) - returns x sorted ascending, or descending when descending is truthy. Tensors are sorted along dim (default: last dimension); lists use Python sorting
		  - x: list or tensor to sort
		  - descending: truthy to sort from largest to smallest (default: false)
		  - dim: dimension to sort along (default: last)
		*/
	| SORT LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN			# SortFunc
		/**
		  any(x) - returns 1 if any element of x is non-zero otherwise 0
		  - x: values to test (number, list or tensor)
		*/
	| ANY LPAREN expr RPAREN			# AnyFunc
		/**
		  all(x) - returns 1 if all elements of x are non-zero otherwise 0
		  - x: values to test (number, list or tensor)
		*/
	| ALL LPAREN expr RPAREN			# AllFunc
		/**
		  edge(x, [kernel_size]) - detects edges in x with a Sobel filter. kernel_size must be odd and at least 3 (default 3).
		  - x: image or tensor
		  - kernel_size: odd Sobel kernel size, at least 3 (default: 3)
		*/
	| EDGE LPAREN expr (COMMA expr)? RPAREN		# EdgeFunc
		/**
		  distance_transform(mask, [threshold]) - Euclidean distance in pixels from each pixel inside the mask to the nearest pixel outside it; outside pixels are 0. Use distance_transform(1 - mask) for the distance outside the mask
		  - mask: mask or image; values above threshold count as inside
		  - threshold: inside/outside cutoff (default: 0.5)
		*/
	| DISTANCE_TRANSFORM LPAREN expr (COMMA expr)? RPAREN	# DistanceTransformFunc
		/**
		  grayscale(image) - replaces the R, G, B entries of the last dimension with their Rec.709 luminance, keeping the shape and extra channels such as alpha
		  - image: colors with R, G, B as the first three entries of the last dimension
		*/
	| GRAYSCALE LPAREN expr RPAREN			# GrayscaleFunc
		/**
		  median(x, [dim]) - computes the median globally or along one dimension
		  - x: values (list or tensor)
		  - dim: dimension to reduce (default: all elements)
		*/
	| MEDIAN LPAREN expr (COMMA expr)? RPAREN			# MedianFunc
		/**
		  mode(x, [dim]) - computes the mode globally or along one dimension
		  - x: values (list or tensor)
		  - dim: dimension to reduce (default: all elements)
		*/
	| MODE LPAREN expr (COMMA expr)? RPAREN			# ModeFunc
		/**
		  cumsum(x, [dim]) - computes the cumulative sum, defaulting to the first dimension.
		  - x: list or tensor
		  - dim: dimension to accumulate along (default: 0)
		*/
	| CUMSUM LPAREN expr (COMMA expr)? RPAREN	# CumsumFunc
		/**
		  count(x) - returns the number of elements in x
		  - x: list, tensor, dictionary or value
		*/
	| COUNT LPAREN expr RPAREN			# CountFunc
		/**
		  keys(dict) - returns a list of dictionary keys in insertion order
		  - dict: dictionary
		*/
	| KEYS LPAREN expr RPAREN			# KeysFunc
		/**
		  enable_tracking(dict) - enables change tracking for a ChangeTrackingDict and returns it
		  - dict: ChangeTrackingDict (other values are returned unchanged)
		*/
	| ENABLE_TRACKING LPAREN expr RPAREN	# EnableTrackingFunc
		/**
		  disable_tracking(dict) - disables change tracking for a ChangeTrackingDict and returns it
		  - dict: ChangeTrackingDict (other values are returned unchanged)
		*/
	| DISABLE_TRACKING LPAREN expr RPAREN	# DisableTrackingFunc
		/**
		  reset_tracking(dict) - resets the change tracking state of a ChangeTrackingDict and returns it
		  - dict: ChangeTrackingDict (other values are returned unchanged)
		*/
	| RESET_TRACKING LPAREN expr RPAREN		# ResetTrackingFunc
		/**
		  repeat(x, count, [dims]) - repeats tensor elements; count may be scalar or per-dim list
		  - x: text, list or tensor to repeat
		  - count: number of repeats, or a list with one count per dimension
		  - dims: dimension or list of dimensions to repeat along; without it a number repeats each element of the flattened input and a list tiles the whole tensor
		*/
	| REPEAT LPAREN expr COMMA expr (COMMA expr)? RPAREN	# RepeatFunc
		/**
		  cumprod(x) - computes the cumulative product over first dimension.
		  - x: list or tensor
		*/
	| CUMPROD LPAREN expr RPAREN			# CumprodFunc
		/**
		  stack_pop(slot) - removes and returns the last element of slot stack
		  - slot: stack number (any integer)
		*/
	| POP LPAREN expr RPAREN			# PopFunc
		/**
		  stack_clear(slot) - clears the contents of slot stack
		  - slot: stack number (any integer)
		*/
	| CLEAR LPAREN expr RPAREN			# ClearFunc
		/**
		  stack_has(slot) - returns 1.0 if slot exists in stack and is not empty else returns 0.0
		  - slot: stack number (any integer)
		*/
	| HAS LPAREN expr RPAREN			# HasFunc
		/**
		  stack_get(slot) - returns the last pushed value in slot without popping it
		  - slot: stack number (any integer)
		*/
	| GET LPAREN expr RPAREN			# GetFunc
		/**
		  argsort(x, [descending], [dim]) - returns the indices that would sort x. descending defaults to false and dim defaults to the last dimension.
		  - x: list or tensor
		  - descending: truthy to sort from largest to smallest (default: false)
		  - dim: dimension to sort along (default: last)
		*/
	| ARGSORT LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN	# ArgsortFunc
		/**
		  argmin(x, [as_position], [dim]) - returns the minimum index globally or along dim; as_position returns global coordinates
		  - x: list or tensor to search
		  - as_position: truthy to return the coordinates of the minimum instead of a flat index
		  - dim: dimension to search along; cannot be combined with as_position
		*/
	| ARGMIN LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN		# ArgminFunc
		/**
		  argmax(x, [as_position], [dim]) - returns the maximum index globally or along dim; as_position returns global coordinates
		  - x: list or tensor to search
		  - as_position: truthy to return the coordinates of the maximum instead of a flat index
		  - dim: dimension to search along; cannot be combined with as_position
		*/
	| ARGMAX LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN		# ArgmaxFunc
		/**
		  softmax(x, [dim]) - applies the softmax function to x (each slice sums to 1.0). dim defaults to the last dimension.
		  - x: scores (list or tensor)
		  - dim: dimension whose slices sum to 1 (default: last)
		*/
	| SOFTMAX LPAREN expr (COMMA expr)? RPAREN	# SoftmaxFunc
		/**
		  softmin(x, [dim]) - applies the softmin function to x (same as softmax(-x, [dim])). dim defaults to the last dimension.
		  - x: scores (list or tensor)
		  - dim: dimension whose slices sum to 1 (default: last)
		*/
	| SOFTMIN LPAREN expr (COMMA expr)? RPAREN	# SoftminFunc
		/**
		  erf(x) - computes the error function (torch.erf)
		  - x: number, list or tensor; applied to each element
		*/
	| ERF LPAREN expr RPAREN			# ErfFunc
		/**
		  erfc(x) - computes the complementary error function (torch.special.erfc)
		  - x: number, list or tensor; applied to each element
		*/
	| ERFC LPAREN expr RPAREN			# ErfcFunc
		/**
		  erfinv(x) - computes the inverse error function (torch.erfinv)
		  - x: value in -1..1 (number, list or tensor)
		*/
	| ERFINV LPAREN expr RPAREN			# ErfinvFunc
		/**
		  unique(x) - returns the sorted unique elements of x (tensors are flattened first)
		  - x: list or tensor
		*/
	| UNIQUE LPAREN expr RPAREN			# UniqueFunc
		/**
		  flatten(x) - flattens tensor into a 1D tensor
		  - x: tensor or nested list
		*/
	| FLATTEN LPAREN expr RPAREN			# FlattenFunc
		/**
		  motion_mask(flow) - generates a motion mask from optical flow
		  - flow: optical flow [..., 2], e.g. from rife()
		*/
	| MOTION_MASK LPAREN expr RPAREN		# MotionMaskFunc
		/**
		  flow_to_image(flow) - converts optical flow to an RGB image. Up-down is blue-yellow, left-right is green-magenta.
		  - flow: optical flow [..., 2], e.g. from rife()
		*/
	| FLOW_TO_IMAGE LPAREN expr RPAREN		# FlowToImageFunc
		/**
		  bnot(x) - computes the bitwise NOT
		  - x: integer values (number, list or tensor)
		*/
	| BNOT LPAREN expr RPAREN			# BitNotFunc
		/**
		  bitcount(x) - returns the number of set bits
		  - x: integer values (number, list or tensor)
		*/
	| BITCOUNT LPAREN expr RPAREN			# BitCountFunc
		/**
		  shape(x) - returns the shape of tensor as a list
		  - x: tensor, list or value
		*/
	| SHAPE LPAREN expr RPAREN			# ShapeFunc
		/**
		  upper(text) - converts string to uppercase
		  - text: text
		*/
	| UPPER LPAREN expr RPAREN			# UpperFunc
		/**
		  lower(text) - converts string to lowercase
		  - text: text
		*/
	| LOWER LPAREN expr RPAREN			# LowerFunc
		/**
		  trim(text) - removes leading and trailing whitespace from string
		  - text: text
		*/
	| TRIM LPAREN expr RPAREN			# TrimFunc
		/**
		  entropy(logits) - computes the Shannon entropy (in nats) of softmax(logits) over all elements
		  - logits: scores (list or tensor)
		*/
	| ENTROPY LPAREN expr RPAREN			# EntropyFunc
		/**
		  fft(x) - computes  fast Fourier transform of x
		  - x: tensor, transformed over all dimensions
		*/
	| SFFT LPAREN expr RPAREN			# SfftFunc
		/**
		  dilate(x, [kernel_size]) - applies morphological dilation to x with a square kernel (default size 3).
		  - x: mask or image with values 0-1
		  - kernel_size: size of the square kernel (default: 3)
		*/
	| DILATE LPAREN expr (COMMA expr)? RPAREN	# DilateFunc
		/**
		  erode(x, [kernel_size]) - applies morphological erosion to x with a square kernel (default size 3).
		  - x: mask or image with values 0-1
		  - kernel_size: size of the square kernel (default: 3)
		*/
	| ERODE LPAREN expr (COMMA expr)? RPAREN	# ErodeFunc
		/**
		  morph_open(x, [kernel_size]) - applies morphological opening (erosion then dilation) to x with a square kernel (default size 3).
		  - x: mask or image with values 0-1
		  - kernel_size: size of the square kernel (default: 3)
		*/
	| MORPH_OPEN LPAREN expr (COMMA expr)? RPAREN	# MorphOpenFunc
		/**
		  morph_close(x, [kernel_size]) - applies morphological closing (dilation then erosion) to x with a square kernel (default size 3).
		  - x: mask or image with values 0-1
		  - kernel_size: size of the square kernel (default: 3)
		*/
	| MORPH_CLOSE LPAREN expr (COMMA expr)? RPAREN	# MorphCloseFunc
		/**
		  int(x) - casts x to integer
		  - x: value to convert; lists convert each item and text is parsed
		*/
	| INT LPAREN expr RPAREN    # IntFunc
		/**
		  float(x) - casts x to float
		  - x: value to convert; lists convert each item and text is parsed
		*/
	| FLOAT LPAREN expr RPAREN    # FloatFunc
		/**
		  flow_magnitude(flow) - computes the magnitude of optical flow (or any other structure with last dimension of 2)
		  - flow: optical flow [..., 2], e.g. from rife()
		*/
	| FLOW_MAG LPAREN expr RPAREN	# FlowMagFunc
		/**
		  flow_angle(flow) - computes the angle atan2(dy, dx) of optical flow (like angle(), with real and imaginary parts in the last dimension)
		  - flow: optical flow [..., 2], e.g. from rife()
		*/
	| FLOW_ANG LPAREN expr RPAREN	# FlowAngFunc
	    /**
		    as_nested(values) - converts a list to a nested tensor (special object containing tensors of different shapes behaving like a tensor)
		    - values: list of tensors; their shapes may differ
		  */
	| AS_NESTED LPAREN expr RPAREN	# AsNestedFunc
		/**
		  svd(x, [full_matrices]) - computes the singular value decomposition of x. Returns a list of 3 tensors U, S, Vh such that x = matmul(matmul(U, diagonal_matrix(S, shape(U))), Vh)
		  - x: matrix, or a batch of matrices in the last two dimensions
		  - full_matrices: truthy to return full-size U and Vh (default: false)
		*/
		| SVD LPAREN expr (COMMA expr)? RPAREN	# SvdFunc;

func2:
		/**
		  pow(base, exponent) - computes base raised to the power of exponent
		  - base: number, list or tensor to raise
		  - exponent: power to raise base to; tensors broadcast
		*/
	POWE LPAREN expr COMMA expr RPAREN			# PowFunc
		/**
		  atan2(y, x) - computes the arc tangent of y/x, using the signs of both arguments to determine the quadrant
		  - y: y coordinate (numerator)
		  - x: x coordinate (denominator)
		*/
	| ATAN2 LPAREN expr COMMA expr RPAREN			# Atan2Func
		/**
		  hypot(x, y) - computes the element-wise Euclidean distance from the origin
		  - x: first coordinate (number, list or tensor)
		  - y: second coordinate (number, list or tensor)
		*/
	| HYPOT LPAREN expr COMMA expr RPAREN			# HypotFunc
		/**
		  logaddexp(x, y) - computes log(exp(x) + exp(y)) element-wise using a numerically stable method
		  - x: first log-space value (number, list or tensor)
		  - y: second log-space value (number, list or tensor)
		*/
	| LOGADDEXP LPAREN expr COMMA expr RPAREN		# LogaddexpFunc
		/**
		  logical_and(x, y) - returns 1.0 if both values are non-zero, else 0.0
		  - x: values; non-zero counts as true
		  - y: values; non-zero counts as true
		*/
	| LOGICAL_AND LPAREN expr COMMA expr RPAREN		# LogicalAndFunc
		/**
		  logical_or(x, y) - returns 1.0 if either value is non-zero, else 0.0
		  - x: values; non-zero counts as true
		  - y: values; non-zero counts as true
		*/
	| LOGICAL_OR LPAREN expr COMMA expr RPAREN		# LogicalOrFunc
		/**
		  isclose(a, b, [rtol], [atol]) - elementwise approximate equality test
		  - a: first values to compare
		  - b: second values to compare
		  - rtol: relative tolerance (default: 1e-5)
		  - atol: absolute tolerance (default: 1e-8)
		*/
	| ISCLOSE LPAREN expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN	# IscloseFunc
		/**
		  allclose(a, b, [rtol], [atol]) - returns 1.0 if all elements are approximately equal, else 0.0
		  - a: first values to compare
		  - b: second values to compare
		  - rtol: relative tolerance (default: 1e-5)
		  - atol: absolute tolerance (default: 1e-8)
		*/
	| ALLCLOSE LPAREN expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN	# AllcloseFunc
		/**
		  tmin(a, b) - element-wise minimum of a and b; min(a, b) for plain numbers
		  - a: first values; tensors broadcast
		  - b: second values; tensors broadcast
		*/
	| TMIN LPAREN expr COMMA expr RPAREN			# TMinFunc
		/**
		  tmax(a, b) - element-wise maximum of a and b; max(a, b) for plain numbers
		  - a: first values; tensors broadcast
		  - b: second values; tensors broadcast
		*/
	| TMAX LPAREN expr COMMA expr RPAREN			# TMaxFunc
		/**
		  snorm(x, [dim]) - frobenius norm of tensor. Along dimension if dimension specified. Dimension can be a list. Defaults to no dimension.
		  - x: number, list or tensor
		  - dim: dimension or list of dimensions to reduce (default: all elements)
		*/
	| SNORM LPAREN expr (COMMA expr)? RPAREN		# SNormFunc
		/**
		  step(x, edge) - returns 0 if x < edge, else 1
		  - x: values to test (number, list or tensor)
		  - edge: threshold; the result is 1 where x >= edge, otherwise 0
		*/
	| STEP LPAREN expr COMMA expr RPAREN			# StepFunc
		/**
		  topk(x, k, [dim]) - returns the k largest elements along dim. For tensors it keeps them in place; dim defaults to the last.
		  - x: list or tensor
		  - k: number of elements to keep
		  - dim: dimension to select along (default: last)
		*/
	| TOPK LPAREN expr COMMA expr (COMMA expr)? RPAREN			# TopkFunc
		/**
		  botk(x, k, [dim]) - returns the k smallest elements along dim. For tensors it keeps them in place; dim defaults to the last.
		  - x: list or tensor
		  - k: number of elements to keep
		  - dim: dimension to select along (default: last)
		*/
	| BOTK LPAREN expr COMMA expr (COMMA expr)? RPAREN			# BotkFunc
		/**
		  quartile(x, q, [dim]) - computes the q-th quartile globally or along dim
		  - x: values (list or tensor)
		  - q: quartile number 0-4 (0 = minimum, 2 = median, 4 = maximum)
		  - dim: dimension to reduce (default: all elements)
		*/
	| QUARTILE LPAREN expr COMMA expr (COMMA expr)? RPAREN		# QuartileFunc
		/**
		  percentile(x, p, [dim]) - computes the p-th percentile globally or along dim
		  - x: values (list or tensor)
		  - p: percentile 0-100
		  - dim: dimension to reduce (default: all elements)
		*/
	| PERCENTILE LPAREN expr COMMA expr (COMMA expr)? RPAREN		# PercentileFunc
		/**
		  quantile(x, q, [dim]) - computes the q-th quantile globally or along dim
		  - x: values (list or tensor)
		  - q: quantile 0-1
		  - dim: dimension to reduce (default: all elements)
		*/
	| QUANTILE LPAREN expr COMMA expr (COMMA expr)? RPAREN		# QuantileFunc
		/**
		  dot(x, y) - computes the dot product of x and y after flattening both to 1D. Use cross(x, y) if you need a per-vector product with the last dimension kept.
		  - x: first tensor; flattened before multiplying
		  - y: second tensor with the same number of elements
		*/
	| DOT LPAREN expr COMMA expr RPAREN			# DotFunc
		/**
		  outer(x, y) - computes the outer product of flattened x and y
		  - x: first tensor; flattened first
		  - y: second tensor; flattened first
		*/
	| OUTER LPAREN expr COMMA expr RPAREN		# OuterFunc
		/**
		  cosine_similarity(x, y) - computes the cosine similarity between x and y.
		  - x: vectors along the last dimension
		  - y: vectors along the last dimension
		*/
	| COSSIM LPAREN expr COMMA expr RPAREN			# CossimFunc
		/**
		  startswith(text, prefix) - returns 1 if text starts with prefix, else 0
		  - text: text to check
		  - prefix: start to look for
		*/
	| STARTSWITH LPAREN expr COMMA expr RPAREN		# StartswithFunc
		/**
		  endswith(text, suffix) - returns 1 if text ends with suffix, else 0
		  - text: text to check
		  - suffix: ending to look for
		*/
	| ENDSWITH LPAREN expr COMMA expr RPAREN			# EndswithFunc
		/**
		  logsumexp(x, [dims]) - computes log(sum(exp(x))) stably, optionally reducing along one or more dimensions
		  - x: values (list or tensor)
		  - dims: dimension or list of dimensions to reduce (default: all elements)
		*/
	| LOGSUMEXP LPAREN expr (COMMA expr)? RPAREN		# LogsumexpFunc
		/**
		  rfft(x, [dim]) - computes the one-dimensional real-input FFT along dim (default: last dimension)
		  - x: real-valued signal
		  - dim: dimension to transform (default: last)
		*/
	| RFFT LPAREN expr (COMMA expr)? RPAREN		# RfftFunc
		/**
		  trace(x) - sums the main diagonal of each square matrix in x
		  - x: matrix, or a batch of matrices in the last two dimensions
		*/
	| TRACE LPAREN expr RPAREN			# TraceFunc
		/**
		  det(x) - computes the determinant of each square matrix in x
		  - x: matrix, or a batch of matrices in the last two dimensions
		*/
	| DET LPAREN expr RPAREN			# DetFunc
		/**
		  flip(x, dims) - reverses the order of elements along the specified dimensions. Text is reversed as a whole
		  - x: tensor, list or text
		  - dims: dimension or list of dimensions to reverse
		*/
	| FLIP LPAREN expr COMMA expr RPAREN			# FlipFunc
		/**
		  cov(x, y) - computes the sample covariance of the flattened x and y (which must have the same number of elements)
		  - x: first values; flattened
		  - y: second values with the same number of elements
		*/
	| COV LPAREN expr COMMA expr RPAREN			# CovFunc
		/**
		  correlation(x, y) - computes the Pearson correlation coefficient between x and y
		  - x: first values
		  - y: second values
		*/
	| CORR LPAREN expr COMMA expr RPAREN			# CorrFunc
		/**
		  append(list, item) - adds item to the end of list. To join tensors along a dimension use concatenate(...)
		  - list: list, tensor or value to extend
		  - item: item, list or tensor added to the end of list
		*/
		| APPEND LPAREN expr COMMA expr RPAREN			# AppendFunc
			/**
			  add_key(dict, key, value) - adds or replaces a dictionary entry and returns the updated dictionary
			  - dict: dictionary to change; it is also returned
			  - key: entry name
			  - value: entry value
			*/
		| ADD_KEY LPAREN expr COMMA expr COMMA expr RPAREN	# AddKeyFunc
			/**
			  permute(x, dims) - permutes the dimensions of tensor x according to dims
			  - x: tensor
			  - dims: new order of the dimensions, e.g. [0, 2, 1]
			*/
		| PERM LPAREN expr COMMA expr RPAREN			# PermuteFunc
		/**
		  gaussian(x, sigma, [auto_channels]) - applies a separable Gaussian blur to x. Channels are expected last unless auto_channels is truthy
		  - x: image or tensor to blur
		  - sigma: blur strength as the standard deviation in elements; 0 or less returns x unchanged
		  - auto_channels: truthy to find the channel dimension automatically; otherwise channels must be last (default: false)
		*/
	| GAUSSIAN LPAREN expr COMMA expr (COMMA expr)? RPAREN	# GaussianFunc
		/**
		  topk_indices(x, k, [dim]) - returns the indices of the k largest elements along dim; without dim, returns indices into flatten(x)
		  - x: list or tensor
		  - k: number of indices to return
		  - dim: dimension to select along (default: indices into flatten(x))
		*/
	| TOPK_IND LPAREN expr COMMA expr (COMMA expr)? RPAREN		# TopkIndFunc
		/**
		  botk_indices(x, k, [dim]) - returns the indices of the k smallest elements along dim; without dim, returns indices into flatten(x)
		  - x: list or tensor
		  - k: number of indices to return
		  - dim: dimension to select along (default: indices into flatten(x))
		*/
	| BOTK_IND LPAREN expr COMMA expr (COMMA expr)? RPAREN		# BotkIndFunc
		/**
		  batch_shuffle(x, indices) - shuffles and duplicates or skips the batch dimension of x according to indices
		  - x: tensor whose first dimension is the batch
		  - indices: batch indices to take, in order; batches may repeat or be skipped
		*/
	| BATCH_SHUFFLE LPAREN expr COMMA expr RPAREN		# BatchShuffleFunc
		/**
		  stack_push(slot, val) - pushes val onto the end of slot stack
		  - slot: stack number (any integer)
		  - val: value to push; it is also returned
		*/
	| PUSH LPAREN expr COMMA expr RPAREN			# PushFunc
		/**
		  get_value(tensor, position) - reads the value at an N-D position of tensor. Superseded by tensor[position] indexing
		  - tensor: tensor to read from
		  - position: list with one index per dimension
		*/
	| GET_VALUE LPAREN expr COMMA expr RPAREN		# GetValueFunc
		/**
		  tensor(shape, [value], [dtype_template]) - creates a tensor with specified shape and optional value/type. Default value is 0 and default format FP32
		  - shape: list of dimension sizes
		  - value: fill value (default: 0)
		  - dtype_template: tensor whose dtype the result uses (default: float32)
		*/
	| TENSOR LPAREN indexExpr (COMMA expr (COMMA expr)? )? RPAREN	# EmptyTensorFunc
		/**
		  zeros(shape, [dtype_template]) - creates a zero-filled tensor on the current device
		  - shape: list of dimension sizes
		  - dtype_template: tensor whose dtype the result uses (default: float32)
		*/
	| ZEROS LPAREN expr (COMMA expr)? RPAREN	# ZerosFunc
		/**
		  ones(shape, [dtype_template]) - creates a one-filled tensor on the current device
		  - shape: list of dimension sizes
		  - dtype_template: tensor whose dtype the result uses (default: float32)
		*/
	| ONES LPAREN expr (COMMA expr)? RPAREN		# OnesFunc
		/**
		  eye(n, [dtype_template]) - creates an n-by-n identity matrix
		  - n: number of rows and columns
		  - dtype_template: tensor whose dtype the result uses (default: float32)
		*/
	| EYE LPAREN expr (COMMA expr)? RPAREN		# EyeFunc
		/**
		  one_hot(indices, classes) - converts integer class indices to float32 one-hot vectors
		  - indices: integer class indices
		  - classes: number of classes, i.e. the length of each one-hot vector
		*/
	| ONE_HOT LPAREN expr COMMA expr RPAREN		# OneHotFunc
		/**
		  mse(a, b, [reduction]) - mean squared error; reduction is mean (default), sum, or none
		  - a: first values (broadcast against b)
		  - b: second values
		  - reduction: "mean" (default), "sum", or "none" for element-wise values
		*/
	| MSE LPAREN expr COMMA expr (COMMA expr)? RPAREN	# MseFunc
		/**
		  mae(a, b, [reduction]) - mean absolute error; reduction is mean (default), sum, or none
		  - a: first values (broadcast against b)
		  - b: second values
		  - reduction: "mean" (default), "sum", or "none" for element-wise values
		*/
	| MAE LPAREN expr COMMA expr (COMMA expr)? RPAREN	# MaeFunc
		/**
		  psnr(a, b, [data_range]) - peak signal-to-noise ratio in dB; data_range defaults to 1
		  - a: first image
		  - b: second image
		  - data_range: difference between the largest and smallest possible value (default: 1)
		*/
	| PSNR LPAREN expr COMMA expr (COMMA expr)? RPAREN	# PsnrFunc
		/**
		  weighted_mean(x, weights, [dims]) - computes the weighted mean globally or along one or more dimensions
		  - x: values (list or tensor)
		  - weights: weight of each element, broadcast against x
		  - dims: dimension or list of dimensions to reduce (default: all elements)
		*/
	| WEIGHTED_MEAN LPAREN expr COMMA expr (COMMA expr)? RPAREN	# WeightedMeanFunc
		/**
		  huber_loss(prediction, target, [delta], [reduction]) - computes Huber loss; delta defaults to 1 and reduction to mean
		  - prediction: predicted values
		  - target: expected values
		  - delta: error size where the loss changes from quadratic to linear (default: 1)
		  - reduction: "mean" (default), "sum", or "none" for element-wise values
		*/
	| HUBER_LOSS LPAREN expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN	# HuberLossFunc
		/**
		  cross_entropy(logits, target, [dim], [reduction]) - computes cross-entropy from class logits and class indices or target probabilities
		  - logits: unnormalised class scores
		  - target: class indices, or class probabilities with the same shape as logits
		  - dim: class dimension (default: 1, or 0 for a single vector)
		  - reduction: "mean" (default), "sum", or "none" for element-wise values
		*/
	| CROSS_ENTROPY LPAREN expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN	# CrossEntropyFunc
		/**
		  leaky_relu(x, [negative_slope]) - applies leaky ReLU element-wise; negative_slope defaults to 0.01
		  - x: number, list or tensor; applied to each element
		  - negative_slope: slope used for negative inputs (default: 0.01)
		*/
	| LEAKY_RELU LPAREN expr (COMMA expr)? RPAREN		# LeakyReluFunc
		/**
		  pad(x, padding) - pads tensor x with specified padding (dim 0 neg, dim 0 pos, dim 1 ...)
		  - x: tensor to pad
		  - padding: amounts as [dim0_before, dim0_after, dim1_before, dim1_after, ...]
		*/
	| PAD LPAREN expr COMMA expr RPAREN			# PadFunc
		/**
		  cross(x, y) - computes the cross product of x and y. Last dimension must be 3
		  - x: vectors with 3 components in the last dimension
		  - y: vectors with 3 components in the last dimension
		*/
	| CROSS LPAREN expr COMMA expr RPAREN			# CrossFunc
		/**
		  matmul(x, y) - computes the matrix multiplication of x and y
		  - x: left matrix or batch of matrices
		  - y: right matrix or batch of matrices
		*/
	| MATMUL LPAREN expr COMMA expr RPAREN			# MatmulFunc
		/**
		  solve(A, b) - solves the square linear system A*x=b without explicitly forming A inverse
		  - A: square coefficient matrix
		  - b: right-hand side
		*/
	| SOLVE LPAREN expr COMMA expr RPAREN		# SolveFunc
		/**
		  flow_apply(image, flow) - applies optical flow to an image
		  - image: image to warp
		  - flow: per-pixel displacement [..., 2], e.g. from rife()
		*/
	| FLOW_APPLY LPAREN expr COMMA expr RPAREN		# FlowApplyFunc
		/**
		  rife(image1, image2, [tiling_size], [iterations], [multi_scale]) - computes the optical flow field ([H, W, 2]) between image1 and image2 using a RAFT-based model
		  - image1: first frame
		  - image2: second frame
		  - tiling_size: splits the image to overlapping tiling_size*tiling_size parts to conserve memory. Default is 0 (auto: enables 1024x1024 tiling when over 2MPx). When tiling_size is between 0 - 1 it takes as a fraction of the resolution
		  - iterations: how many times to run the flow model. Default 12
		  - multi_scale: also use low resolution of base image for giant movements. Default false
		*/
	| RIFE LPAREN expr COMMA expr (COMMA expr (COMMA expr (COMMA expr)?)?)? RPAREN # RifeFunc
		/**
		  bitwise_and(x, y) - computes the element-wise bitwise AND of x and y
		  - x: integer values (number, list or tensor)
		  - y: integer values (number, list or tensor)
		*/
	| BAND LPAREN expr COMMA expr RPAREN			# BitAndFunc
		/**
		  bitwise_xor(x, y) - computes the element-wise bitwise XOR of x and y
		  - x: integer values (number, list or tensor)
		  - y: integer values (number, list or tensor)
		*/
	| XOR LPAREN expr COMMA expr RPAREN			# BitXorFunc
		/**
		  bitwise_or(x, y) - computes the element-wise bitwise OR of x and y
		  - x: integer values (number, list or tensor)
		  - y: integer values (number, list or tensor)
		*/
	| BOR LPAREN expr COMMA expr RPAREN			# BitOrFunc
		/**
		  split(text, [delimiter]) - splits string to list of strings based on delimiter. Default is space.
		  - text: text to split
		  - delimiter: text to split on (default: a space)
		*/
	| SPLIT LPAREN expr (COMMA expr)? RPAREN		# SplitFunc
		/**
		  join(items, [separator]) - joins items as text using separator (default ""). Use concatenate(...) to join tensors
		  - items: list or tensor of items to join
		  - separator: text placed between the items (default: "")
		*/
	| JOIN LPAREN expr (COMMA expr)? RPAREN			# JoinFunc
		/**
		  substring(text, start, [length]) - returns length characters of text starting at start. If length is not supplied, it returns the rest of the string
		  - text: source text
		  - start: index of the first character
		  - length: number of characters (default: the rest of the text)
		*/
	| SUBSTRING LPAREN expr COMMA expr (COMMA expr)? RPAREN # SubstringFunc
		/**
		  find(text, search) - returns the index of the first occurrence of search in text, or -1 if it is not found
		  - text: text to search in
		  - search: text to look for
		*/
	| FIND LPAREN expr COMMA expr RPAREN			# FindFunc
		/**
		  replace(value, old, new) - replaces every occurrence of old with new; works on text, lists and tensors
		  - value: text, list or tensor
		  - old: text or value to look for
		  - new: replacement
		*/
	| REPLACE LPAREN expr COMMA expr COMMA expr RPAREN	# ReplaceFunc
		/**
		  regex_search(text, pattern) - returns the index of the first match of the regular expression pattern in text, or -1 if there is none
		  - text: text to search in
		  - pattern: Python regular expression
		*/
	| REGEX_SEARCH LPAREN expr COMMA expr RPAREN		# RegexSearchFunc
		/**
		  regex_replace(text, pattern, replacement) - replaces every match of the regular expression pattern in text; replacement may refer to groups as \1
		  - text: text to change
		  - pattern: Python regular expression
		  - replacement: replacement text
		*/
	| REGEX_REPLACE LPAREN expr COMMA expr COMMA expr RPAREN	# RegexReplaceFunc
		/**
		  to_json(value) - serializes a value as JSON; tensors become nested arrays
		  - value: JSON-compatible value, dictionary, list, or tensor
		*/
	| TO_JSON LPAREN expr RPAREN				# ToJsonFunc
		/**
		  from_json(text) - parses JSON; objects become dictionaries and arrays become lists
		  - text: JSON text; decoded arrays remain ordinary lists
		*/
	| FROM_JSON LPAREN expr RPAREN			# FromJsonFunc
		/**
		  format(value, [spec]) - formats numbers as text. spec is a number of decimals or a Python format spec such as ".3e" (default: shortest form, "g"); lists and tensors are formatted per element
		  - value: number, list or tensor
		  - spec: decimal count or format spec text
		*/
	| FORMAT LPAREN expr (COMMA expr)? RPAREN		# FormatFunc
		/**
		  int_to_rgb(color) - unpacks 0xRRGGBB integers into 0-1 RGB colors. Tensors get R, G, B stacked in a new last dimension, lists return a list of colors and a number returns a 3-item list
		  - color: packed 0xRRGGBB integer, list or tensor
		*/
	| INT_TO_RGB LPAREN expr RPAREN				# Int_to_rgbFunc
		/**
		  rgb_to_int(rgb) / rgb_to_int(r, g, b) - packs 0-1 RGB components into 0xRRGGBB integers. With one argument the last dimension (or a 3-item list) holds R, G, B; with three, each argument is one channel
		  - rgb: colors with R, G, B (0-1) in the last dimension, or a 3-item list
		  - r: red channel 0-1
		  - g: green channel 0-1
		  - b: blue channel 0-1
		*/
	| RGB_TO_INT LPAREN expr ( COMMA expr COMMA expr)? RPAREN	# Rgb_to_intFunc
		/**
		  interpolate_linear(x, scale) - resizes x [N, C, ...] with (bi/tri)linear interpolation. A number scales every spatial dimension; a list is the target spatial size
		  - x: tensor shaped [N, C, ...] with 1-3 spatial dimensions
		  - scale: a number scales every spatial dimension; a list gives the target spatial size
		*/
	| INTERPOLATE_LINEAR LPAREN expr COMMA expr RPAREN	# InterpolateLinearFunc
		/**
		  interpolate_area(x, scale) - resizes x [N, C, ...] with area interpolation. A number scales every spatial dimension; a list is the target spatial size
		  - x: tensor shaped [N, C, ...] with 1-3 spatial dimensions
		  - scale: a number scales every spatial dimension; a list gives the target spatial size
		*/
	| INTERPOLATE_AREA LPAREN expr COMMA expr RPAREN	# InterpolateAreaFunc
		/**
		  interpolate_nearest_exact(x, scale) - resizes x [N, C, ...] with nearest-neighbour interpolation. A number scales every spatial dimension; a list is the target spatial size
		  - x: tensor shaped [N, C, ...] with 1-3 spatial dimensions
		  - scale: a number scales every spatial dimension; a list gives the target spatial size
		*/
	| INTERPOLATE_NEAREST LPAREN expr COMMA expr RPAREN	# InterpolateNearestExactFunc
		/**
		  remove_key(dict, key) - removes a dictionary entry and returns the updated dictionary
		  - dict: dictionary to change; it is also returned
		  - key: entry name to remove; missing keys are ignored
		*/
	| REMOVE_KEY LPAREN expr COMMA expr RPAREN	# RemoveKeyFunc;


func3:
		/**
		  clamp(x, min, max) - clamps x between min and max per element
		  - x: number, list or tensor; applied to each element
		  - min: lower bound
		  - max: upper bound
		*/
	CLAMP LPAREN expr COMMA expr COMMA expr RPAREN		# ClampFunc
		/**
		  lerp(a, b, t) - linear interpolation between a and b by t per element. t can be float or tensor.
		  - a: value at t = 0
		  - b: value at t = 1
		  - t: progress from 0 (gives a) to 1 (gives b)
		*/
	| LERP LPAREN expr COMMA expr COMMA expr RPAREN		# LerpFunc
		/**
		  smoothstep(x, edge0, edge1) - smooth interpolation between edge0 and edge1
		  - x: input values
		  - edge0: value mapped to 0
		  - edge1: value mapped to 1
		*/
	| SMOOTHSTEP LPAREN expr COMMA expr COMMA expr RPAREN	# SmoothstepFunc
		/**
		  transpose(x, dim0, dim1) / swapaxes(x, dim0, dim1) - swaps two tensor dimensions
		  - x: tensor
		  - dim0: first dimension to swap
		  - dim1: second dimension to swap
		*/
	| TRANSPOSE LPAREN expr COMMA expr COMMA expr RPAREN	# TransposeFunc
		/**
		  range(start, stop, step) - creates a range of values between start (inclusive) and stop (exclusive) using step. Use linspace if you want value count.
		  - start: first value
		  - stop: end of the range (not included)
		  - step: distance between consecutive values
		*/
	| RANGE LPAREN expr COMMA expr COMMA expr RPAREN	# RangeFunc
		/**
		  moment(x, center, order) - computes the order-th moment of x around center: mean((x - center)^order)
		  - x: values (list or tensor)
		  - center: centre the moment is taken around
		  - order: order of the moment
		*/
	| MOMENT LPAREN expr COMMA expr COMMA expr RPAREN	# MomentFunc
		/**
		  cubic_ease(a, b, t) - cubic ease between a and b
		  - a: value at t = 0
		  - b: value at t = 1
		  - t: progress from 0 (gives a) to 1 (gives b)
		*/
	| CUBIC_EASE LPAREN expr COMMA expr COMMA expr RPAREN	# CubicEaseFunc
		/**
		  elastic_ease(a, b, t) - elastic ease between a and b
		  - a: value at t = 0
		  - b: value at t = 1
		  - t: progress from 0 (gives a) to 1 (gives b)
		*/
	| ELASTIC_EASE LPAREN expr COMMA expr COMMA expr RPAREN	# ElasticEaseFunc
		/**
		  sine_ease(a, b, t) - sine easing between a and b
		  - a: value at t = 0
		  - b: value at t = 1
		  - t: progress from 0 (gives a) to 1 (gives b)
		*/
	| SINE_EASE LPAREN expr COMMA expr COMMA expr RPAREN	# SineEaseFunc
		/**
		  smootherstep(x, edge0, edge1) - smoother interpolation between edge0 and edge1
		  - x: input values
		  - edge0: value mapped to 0
		  - edge1: value mapped to 1
		*/
	| SMOOTHERSTEP LPAREN expr COMMA expr COMMA expr RPAREN	# SmootherstepFunc
		/**
		  crop(x, start, size) - crops the region of x beginning at start (the low corner). The result always has shape size; parts outside x are zero-filled. On text, returns at most size characters
		  - x: tensor or text
		  - start: low corner of the region, one index per dimension
		  - size: size of the result, one value per dimension
		*/
	| CROP LPAREN expr COMMA expr COMMA expr RPAREN		# CropFunc
		/**
		  ifft(x, [shape]) - inverse fast Fourier transform of x. shape (defaults to the node's tensor shape) sizes the K/Kx/Ky/.../frequency variables made available while evaluating x, it does not resize x itself.
		  - x: spectrum to transform back; may use the K/Kx/Ky/frequency variables
		  - shape: shape used for the K/Kx/Ky frequency variables (default: the node's input shape)
		*/
	| SIFFT LPAREN expr (COMMA expr)? RPAREN		# SifftFunc
		/**
		  irfft(x, [n], [dim]) - computes the inverse one-dimensional real FFT along dim (default: last dimension)
		  - x: complex half-spectrum, e.g. from rfft()
		  - n: length of the output signal (default: 2 * (input length - 1))
		  - dim: dimension to transform (default: last)
		*/
	| IRFFT LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN	# IrfftFunc
		/**
		  overlay(base, overlay, offset, [opacity], [mode]) - overlays overlay on base at offset. Opacity controls blending. It can be tensor or float. If it is tensor it should be the same shape as overlay. For tensors, mode picks a blend mode like blend()
		  - base: background value, list, text or tensor
		  - overlay: value placed on top of base
		  - offset: position of the overlay's low corner in base, one value per dimension
		  - opacity: 0-1 blend amount; a number or a tensor shaped like overlay (default: 1)
		  - mode: blend mode name for tensors, see blend() (default: "normal")
		*/
	| OVERLAY LPAREN expr COMMA expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN	# OverlayFunc
		/**
		  blend(base, top, mode, [opacity]) - blends top onto base with a blend mode, like layers in an image editor. Shapes broadcast; use overlay() to place a smaller layer at an offset. Modes: normal, multiply, screen, overlay, soft_light, hard_light, darken, lighten, difference, exclusion, add, subtract, color_dodge, color_burn
		  - base: bottom layer
		  - top: top layer
		  - mode: blend mode name, e.g. "screen"
		  - opacity: 0-1 amount of the blended result; a number or a broadcastable tensor (default: 1)
		*/
	| BLEND LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# BlendFunc
		/**
		  interp(x, xs, ys, [mode]) - keyframe interpolation: the value at x of the curve through the points (xs, ys), holding the first/last value outside the keys. Modes: linear (default), smooth (eases in and out of every key), step (holds a value until the next key)
		  - x: position such as a frame index; a number or tensor
		  - xs: key positions
		  - ys: values at the keys; they may be tensors (e.g. images) when x is a number
		  - mode: "linear", "smooth" or "step" (default: "linear")
		*/
	| INTERP LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# InterpFunc
		/**
		  sigm_karras(steps, sigma_min, sigma_max, [rho]) - Karras noise schedule: steps sigmas from sigma_max down to sigma_min, followed by a final 0
		  - steps: number of sampling steps
		  - sigma_min: smallest non-zero sigma
		  - sigma_max: largest sigma
		  - rho: curvature of the schedule (default: 7)
		*/
	| SIGM_KARRAS LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# SigmKarrasFunc
		/**
		  sigm_exponential(steps, sigma_min, sigma_max) - exponential noise schedule (evenly spaced in log sigma), followed by a final 0
		  - steps: number of sampling steps
		  - sigma_min: smallest non-zero sigma
		  - sigma_max: largest sigma
		*/
	| SIGM_EXPONENTIAL LPAREN expr COMMA expr COMMA expr RPAREN	# SigmExponentialFunc
		/**
		  sigm_polyexponential(steps, sigma_min, sigma_max, [rho]) - polynomial-in-log-sigma noise schedule, followed by a final 0
		  - steps: number of sampling steps
		  - sigma_min: smallest non-zero sigma
		  - sigma_max: largest sigma
		  - rho: polynomial power; 1 is the exponential schedule (default: 1)
		*/
	| SIGM_POLYEXPONENTIAL LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# SigmPolyexponentialFunc
		/**
		  sigm_laplace(steps, sigma_min, sigma_max, [mu], [beta]) - Laplace noise schedule of steps sigmas; like ComfyUI's LaplaceScheduler it has no final 0
		  - steps: number of sampling steps
		  - sigma_min: smallest non-zero sigma
		  - sigma_max: largest sigma
		  - mu: location of the Laplace distribution in log sigma (default: 0)
		  - beta: scale of the Laplace distribution (default: 0.5)
		*/
	| SIGM_LAPLACE LPAREN expr COMMA expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN	# SigmLaplaceFunc
		/**
		  linspace(start, stop, count) - creates count evenly spaced values from start to stop (both included). Use range to control the step instead.
		  - start: first value
		  - stop: last value (included)
		  - count: number of values
		*/
	| LINSPACE LPAREN expr COMMA expr COMMA expr RPAREN	# LinspaceFunc
		/**
		  roll(x, shifts, [dim]) - circularly shifts tensor x along dim (default 0)
		  - x: tensor
		  - shifts: number of places to shift; elements pushed off one end come back at the other
		  - dim: dimension to shift along (default: 0)
		*/
	| ROLL LPAREN expr COMMA expr (COMMA expr)? RPAREN	# RollFunc
		/**
		  rgb_to_oklab(rgb) / rgb_to_oklab(r, g, b) - converts 0-1 sRGB to OKLab. With one argument its last dimension holds R, G, B; with three, the channels are stacked into the last dimension of the result
		  - rgb: sRGB colors (0-1) with R, G, B in the last dimension, or a 3-item list
		  - r: red channel 0-1
		  - g: green channel 0-1
		  - b: blue channel 0-1
		*/
	| RGB_TO_OKLAB LPAREN expr (COMMA expr COMMA expr)? RPAREN	# RgbToOklabFunc
		/**
		  rgb_to_cielab(rgb) / rgb_to_cielab(r, g, b) - converts 0-1 sRGB to CIELAB (D65) divided by 100, so L is 0-1. With one argument its last dimension holds R, G, B; with three, the channels are stacked into the last dimension of the result
		  - rgb: sRGB colors (0-1) with R, G, B in the last dimension, or a 3-item list
		  - r: red channel 0-1
		  - g: green channel 0-1
		  - b: blue channel 0-1
		*/
	| RGB_TO_CIELAB LPAREN expr (COMMA expr COMMA expr)? RPAREN	# RgbToCielabFunc
		/**
		  luminance(rgb) / luminance(r, g, b) - Rec.709 luminance 0.2126 R + 0.7152 G + 0.0722 B of gamma-encoded colors. With one argument the first three entries of its last dimension are R, G, B and that dimension is removed
		  - rgb: colors (0-1) with R, G, B in the last dimension, or a 3-item list
		  - r: red channel 0-1
		  - g: green channel 0-1
		  - b: blue channel 0-1
		*/
	| LUMINANCE LPAREN expr (COMMA expr COMMA expr)? RPAREN	# LuminanceFunc
		/**
		  rgb_to_hsv(rgb, [degrees]) / rgb_to_hsv(r, g, b, [degrees]) - converts RGB to HSV. With one color argument its last dimension holds R, G, B; with three, the channels are stacked into the last dimension of the result. If degrees is truthy, hue is 0-360 instead of 0-1
		  - rgb: colors (0-1) with R, G, B in the last dimension, or a 3-item list
		  - degrees: truthy to use hue in 0-360 instead of 0-1
		  - r: red channel 0-1
		  - g: green channel 0-1
		  - b: blue channel 0-1
		*/
	| RGB_TO_HSV LPAREN expr (COMMA expr COMMA expr)? (COMMA expr)? RPAREN	# RgbToHsvFunc
		/**
		  hsv_to_rgb(hsv, [degrees]) / hsv_to_rgb(h, s, v, [degrees]) - converts HSV to RGB. With one color argument its last dimension holds H, S, V; with three, the channels are stacked into the last dimension of the result. If degrees is truthy, hue is read as 0-360 instead of 0-1
		  - hsv: colors with H, S, V in the last dimension, or a 3-item list
		  - degrees: truthy to use hue in 0-360 instead of 0-1
		  - h: hue 0-1 (0-360 with degrees)
		  - s: saturation 0-1
		  - v: value (brightness) 0-1
		*/
	| HSV_TO_RGB LPAREN expr (COMMA expr COMMA expr)? (COMMA expr)? RPAREN	# HsvToRgbFunc
		/**
		  where(condition, if_true, if_false) - returns if_true where condition is non-zero, otherwise if_false. Runs per element
		  - condition: non-zero selects if_true, zero selects if_false
		  - if_true: value used where condition is non-zero
		  - if_false: value used where condition is zero
		*/
	| WHERE LPAREN expr COMMA expr COMMA expr RPAREN			# WhereFunc
		/**
		  oklab_to_rgb(oklab) / oklab_to_rgb(l, a, b) - converts OKLab to 0-1 sRGB. With one argument its last dimension holds L, a, b; with three, the channels are stacked into the last dimension of the result
		  - oklab: OKLab colors with L, a, b in the last dimension, or a 3-item list
		  - l: lightness
		  - a: green-red axis
		  - b: blue-yellow axis
		*/
	| OKLAB_TO_RGB LPAREN expr (COMMA expr COMMA expr)? RPAREN		# OklabToRgbFunc
		/**
		  cielab_to_rgb(cielab) / cielab_to_rgb(l, a, b) - converts CIELAB divided by 100 (as returned by rgb_to_cielab) to 0-1 sRGB. With one argument its last dimension holds L, a, b; with three, the channels are stacked into the last dimension of the result
		  - cielab: CIELAB colors / 100 with L, a, b in the last dimension, or a 3-item list
		  - l: lightness / 100 (0-1)
		  - a: green-red axis / 100
		  - b: blue-yellow axis / 100
		*/
	| CIELAB_TO_RGB LPAREN expr (COMMA expr COMMA expr)? RPAREN		# CielabToRgbFunc
		/**
		  text_image(text, font, size, [max_width], [weight], [rotation_angle], [line_spacing], [italic], [underline]) - renders text to a 2D tensor with values 0-1
		  - text: text to render; line breaks start new lines
		  - font: font name to look up in the system fonts, or a path to a font file in a system font folder or the ComfyUI input folder
		  - size: font size in pixels
		  - max_width: wrap lines wider than this many pixels (default: 0, no wrapping)
		  - weight: font weight 100-900 as in CSS (default: 400)
		  - rotation_angle: rotation in degrees, counter-clockwise (default: 0)
		  - line_spacing: line distance as a multiple of the line height (default: 1)
		  - italic: truthy for italic text (default: false)
		  - underline: truthy to underline the text (default: false)
		*/
	| TEXT_IMAGE LPAREN expr COMMA expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN	# TextImageFunc
	    /**
		  coords(shape, dim, [dtype_template]) - generates a tensor with the specified shape whose values are the coordinates of each element along dim. An optional tensor supplies the output dtype (default float32).
		  - shape: list of dimension sizes
		  - dim: dimension whose index becomes the value
		  - dtype_template: tensor whose dtype the result uses (default: float32)
		*/
	| COORDS LPAREN expr COMMA expr (COMMA expr)? RPAREN	# CoordsFunc
	    /**
		   gather(x, dim, indices) - gathers elements of x along dim at the given indices. The result has the shape of indices.
		   - x: source tensor
		   - dim: dimension to gather along
		   - indices: indices along dim; the result has their shape
		   */
	| GATHER LPAREN expr COMMA expr COMMA expr RPAREN	# GatherFunc
	    /**
		  scatter(x, dim, indices, src) - writes the elements of src into x along dim at the given indices. The result has the shape of x.
		  - x: tensor to write into
		  - dim: dimension to scatter along
		  - indices: position along dim for each element of src
		  - src: values to write
		*/
	| SCATTER LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# ScatterFunc
		/**
		  scatter_add(x, dim, indices, src) - adds the elements of src into x along dim at the given indices. The result has the shape of x.
		  - x: tensor to add into
		  - dim: dimension to scatter along
		  - indices: position along dim for each element of src
		  - src: values to add
		*/
	| SCATTER_ADD LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# ScatterAddFunc;

func4:
		/**
		  swap(x, dim, index1, index2) - swaps the elements at index1 and index2 along dim
		  - x: tensor
		  - dim: dimension to swap along
		  - index1: first position
		  - index2: second position
		*/
	SWAP LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# SwapFunc
		/**
		  nan_to_num(x, nan, pos_inf, neg_inf) - replaces NaN, +inf and -inf in x with the given values (named after SQL NVL)
		  - x: values to clean
		  - nan: replacement for NaN
		  - pos_inf: replacement for +infinity
		  - neg_inf: replacement for -infinity
		*/
	| NVL LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# NvlFunc
		/**
		  logspace(start, stop, count, base) - creates count values from base^start to base^stop, evenly spaced in the exponent
		  - start: exponent of the first value
		  - stop: exponent of the last value
		  - count: number of values
		  - base: base of the exponent
		*/
	| LOGSPACE LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# LogspaceFunc
		/**
		  distance(x1, y1, x2, y2) - computes Euclidean distance between (x1, y1) and (x2, y2)
		  - x1: x of the first point
		  - y1: y of the first point
		  - x2: x of the second point
		  - y2: y of the second point
		*/
	| DIST LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# DistFunc
		/**
		  histogram(x, bins, min, max) - counts the elements of flatten(x) in bins equal-width bins over [min, max]
		  - x: values; flattened
		  - bins: number of equal-width bins
		  - min: lower edge of the first bin
		  - max: upper edge of the last bin
		*/
	| HISTOGRAM LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN	# HistogramFunc;

func5:
		/**
		  remap(x, in_min, in_max, out_min, out_max) - remaps values from input range to output range
		  - x: values to remap (number, list or tensor)
		  - in_min: start of the input range
		  - in_max: end of the input range
		  - out_min: value in_min maps to
		  - out_max: value in_max maps to
		*/
	REMAP LPAREN expr COMMA expr COMMA expr COMMA expr COMMA expr RPAREN # RemapFunc
    	/**
		  diagonal_matrix(values, shape, [offset], [dim1], [dim2]) - creates a tensor of the given shape with values on a diagonal and zeros elsewhere
		  - values: values placed on the diagonal
		  - shape: shape of the result
		  - offset: diagonal offset: positive above, negative below the main diagonal (default: 0)
		  - dim1: first dimension of the matrix (default: -2)
		  - dim2: second dimension of the matrix (default: -1)
		  */
		  | DIAG LPAREN expr COMMA expr (COMMA expr (COMMA expr (COMMA expr)?)?)? RPAREN # DiagonalMatrixFunc;

// N-argument functions
funcN:
		/**
		  norm(x, [p], [dims]) - computes the p-norm globally or along one or more dimensions (default p=2)
		  - x: number, list or tensor
		  - p: norm order (default: 2)
		  - dims: dimension or list of dimensions to reduce (default: all elements)
		*/
	NORM LPAREN expr (COMMA expr (COMMA expr)?)? RPAREN	# NormFunc
		/**
		  slerp(a, b, t, [dim]) - interpolates vector directions spherically and magnitudes linearly. Without dim, all elements form one vector; dim selects a vector-component axis and other axes identify independent vectors.
		  - a: vectors at t = 0
		  - b: vectors at t = 1
		  - t: progress from 0 (gives a) to 1 (gives b)
		  - dim: dimension holding the vector components (default: all elements form one vector)
		*/
	| SLERP LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# SlerpFunc
		/**
		  normalize(x, [p], [dim], [eps]) - normalizes x along dim using the p-norm (defaults: p=2, dim=-1, eps=1e-12)
		  - x: list or tensor
		  - p: norm order (default: 2)
		  - dim: dimension to work along (default: last)
		  - eps: smallest allowed divisor (default: 1e-12)
		*/
	| NORMALIZE LPAREN expr (COMMA expr (COMMA expr (COMMA expr)?)?)? RPAREN	# NormalizeFunc
		/**
		  group_norm(x, groups, [weight], [bias], [eps]) - applies channel-first GroupNorm to [N, C, ...] input
		  - x: tensor shaped [N, C, ...]
		  - groups: number of channel groups; must divide the channel count
		  - weight: per-channel scale, length C (default: none)
		  - bias: per-channel shift, length C (default: none)
		  - eps: value added to the variance for stability (default: 1e-5)
		*/
	| GROUP_NORM LPAREN expr COMMA expr (COMMA expr (COMMA expr (COMMA expr)?)?)? RPAREN	# GroupNormFunc
		/**
		  smin(x, ...) - computes the minimum of inputs or elements. Tensors must have the same size or be broadcastable to same size. When called as smin(x, dims) with x a tensor/list, reduces x along dims (a single dim or list of dims) instead.
		  - x: values; one list or tensor gives its smallest element, several values give the smallest of all
		*/
	| SMIN LPAREN expr (COMMA expr)* RPAREN		# SMinFunc
		/**
		  smax(x, ...) - computes the maximum of inputs or elements. Tensors must have the same size or be broadcastable to same size. When called as smax(x, dims) with x a tensor/list, reduces x along dims (a single dim or list of dims) instead.
		  - x: values; one list or tensor gives its largest element, several values give the largest of all
		*/
	| SMAX LPAREN expr (COMMA expr)* RPAREN		# SMaxFunc
		/**
		  map(tensor, coord1, [coord2], [coord3]) - samples/remaps input tensor using coordinates
		  - tensor: tensor to sample from
		  - coord1: sample positions (element indices) along the first mapped dimension; mapped dimensions are the last ones of tensor
		  - coord2: sample positions along the second mapped dimension
		  - coord3: sample positions along the third mapped dimension
		*/
	| MAP LPAREN expr COMMA expr (COMMA expr (COMMA expr)?)? RPAREN		# MapFunc
		/**
		  ezconvolution(tensor, size_x, kernel) / ezconvolution(tensor, size_x, size_y, kernel) / ezconvolution(tensor, size_x, size_y, size_z, kernel) - convolves tensor with a 1D, 2D or 3D kernel, guessing whether channels come first or last. kernel is evaluated over the kernel grid with kx/ky/kz coordinates
		  - tensor: input, channels first or last
		  - size_x: kernel size along the first spatial dimension
		  - kernel: expression for the kernel weights, evaluated over the kernel grid with kx/ky/kz offsets from its centre
		  - size_y: kernel size along the second spatial dimension
		  - size_z: kernel size along the third spatial dimension
		*/
	| EZCONV LPAREN expr (COMMA expr)+ RPAREN	# EzConvFunc
		/**
		  convolution(tensor, size_x, kernel) / convolution(tensor, size_x, size_y, kernel) / convolution(tensor, size_x, size_y, size_z, kernel) - convolves tensor [batch, channel, spatial...] with a 1D, 2D or 3D kernel. kernel is evaluated over the kernel grid with kx/ky/kz coordinates
		  - tensor: input shaped [batch, channel, spatial...]
		  - size_x: kernel size along the first spatial dimension
		  - kernel: expression for the kernel weights, evaluated over the kernel grid with kx/ky/kz offsets from its centre
		  - size_y: kernel size along the second spatial dimension
		  - size_z: kernel size along the third spatial dimension
		*/
	| CONV LPAREN expr (COMMA expr)+ RPAREN		# ConvFunc
		/**
		  reshape(x, shape) - reshapes tensor x to the specified shape
		  - x: tensor
		  - shape: new shape; the total number of elements must stay the same
		*/
	| RESHAPE LPAREN expr COMMA expr RPAREN		# ReshapeFunc
		/**
		  squeeze(x, [dim]) - removes size-1 dimensions from tensor x, optionally at dim
		  - x: tensor
		  - dim: only remove this dimension, if it has size 1
		*/
	| SQUEEZE LPAREN expr (COMMA expr)? RPAREN		# SqueezeFunc
		/**
		  unsqueeze(x, dim) - inserts a size-1 dimension into tensor x at dim
		  - x: tensor
		  - dim: position of the new size-1 dimension
		*/
	| UNSQUEEZE LPAREN expr COMMA expr RPAREN		# UnsqueezeFunc
		/**
		  concatenate(x, ..., dim) - concatenates one or more tensors along the specified dimension
		  - x: first tensor or list; more may follow before dim. A single list of tensors joins its elements
		  - dim: dimension to join along (the last argument)
		*/
	| CONCAT LPAREN expr (COMMA expr)+ RPAREN	# ConcatFunc
		/**
		  stack(tensors, [dim]) / stack(x, ..., dim) - stacks tensors along a new dimension
		  - tensors: list of tensors with equal shapes
		  - x: first tensor; more may follow before dim
		  - dim: position of the new dimension (default: 0 for a list; required after separate tensors)
		*/
	| STACK LPAREN expr (COMMA expr)* RPAREN	# StackFunc
		/**
		  nonzero(x) - returns an N-by-rank tensor of coordinates for nonzero elements
		  - x: tensor
		*/
	| NONZERO LPAREN expr RPAREN			# NonzeroFunc
		/**
		  get_changed_keys(dict) - returns the keys that were modified or added in a ChangeTrackingDict
		  - dict: ChangeTrackingDict
		*/
	| GET_CHANGED_KEYS LPAREN expr RPAREN		# GetChangedKeysFunc
		/**
		  get_added_keys(dict) - returns the keys that were newly added to a ChangeTrackingDict
		  - dict: ChangeTrackingDict
		*/
	| GET_ADDED_KEYS LPAREN expr RPAREN			# GetAddedKeysFunc
		/**
		  get_removed_keys(dict) - returns the keys that were removed from a ChangeTrackingDict
		  - dict: ChangeTrackingDict
		*/
	| GET_REMOVED_KEYS LPAREN expr RPAREN		# GetRemovedKeysFunc
		/**
		  get_unchanged_keys(dict) - returns the keys that are unchanged in a ChangeTrackingDict
		  - dict: ChangeTrackingDict
		*/
	| GET_UNCHANGED_KEYS LPAREN expr RPAREN		# GetUnchangedKeysFunc;

funcNoise:
		/**
		  random_normal(seed, [shape]) - generates normally distributed random noise
		  - seed: random seed; the same seed always gives the same values
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	NOISE LPAREN expr (COMMA expr)? RPAREN				# NoiseFunc
		/**
		  pink_noise(seed, [shape]) - generates deterministic pink noise (approximately 1/f power spectrum) with zero mean and unit variance per row
		  - seed: random seed; the same seed always gives the same values
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| PINK_NOISE LPAREN expr (COMMA expr)? RPAREN		# PinkNoiseFunc
		/**
		  brown_noise(seed, [shape]) - generates deterministic brown noise (approximately 1/f^2 power spectrum) with zero mean and unit variance per row
		  - seed: random seed; the same seed always gives the same values
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| BROWN_NOISE LPAREN expr (COMMA expr)? RPAREN		# BrownNoiseFunc
		/**
		  random_uniform(seed, [shape]) - generates uniformly distributed random noise
		  - seed: random seed; the same seed always gives the same values
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| RAND LPAREN expr (COMMA expr)? RPAREN				# RandFunc
		/**
		  random_exponential(seed, rate, [shape]) - generates exponentially distributed random values
		  - seed: random seed; the same seed always gives the same values
		  - rate: events per unit; the mean is 1 / rate
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| EXPONENTIAL LPAREN expr COMMA expr (COMMA expr)? RPAREN	# ExponentialFunc
		/**
		  random_bernoulli(seed, probability, [shape]) - generates Bernoulli distributed random values (0 or 1). Probability can be a tensor
		  - seed: random seed; the same seed always gives the same values
		  - probability: chance of a 1; a tensor gives one probability per element and sets the shape
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| BERNOULLI LPAREN expr COMMA expr (COMMA expr)? RPAREN		# BernoulliFunc
		/**
		  random_poisson(seed, rate, [shape]) - generates Poisson distributed random values.
		  - seed: random seed; the same seed always gives the same values
		  - rate: expected count; a tensor gives one rate per element and sets the shape
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| POISSON LPAREN expr COMMA expr (COMMA expr)? RPAREN		# PoissonFunc
		/**
		  random_cauchy(seed, median, sigma, [shape]) - generates Cauchy distributed random values.
		  - seed: random seed; the same seed always gives the same values
		  - median: centre of the distribution
		  - sigma: half width at half maximum
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| CAUCHY LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# CauchyFunc
		/**
		  random_log_normal(seed, mean, std, [shape]) - generates log-normally distributed random values.
		  - seed: random seed; the same seed always gives the same values
		  - mean: mean of the underlying normal distribution
		  - std: standard deviation of the underlying normal distribution
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| LOGNORMAL LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# LogNormalFunc
		/**
		  random_gamma(seed, concentration, scale, [shape]) - generates Gamma distributed random values.
		  - seed: random seed; the same seed always gives the same values
		  - concentration: shape (concentration) k
		  - scale: scale theta; the mean is k * theta
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| GAMMADIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# GammaDistFunc
		/**
		  random_beta(seed, alpha, beta, [shape]) - generates Beta distributed random values
		  - seed: random seed; the same seed always gives the same values
		  - alpha: first concentration
		  - beta: second concentration
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| BETADIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# BetaDistFunc
		/**
		  random_laplace(seed, loc, scale, [shape]) - generates Laplace distributed random values
		  - seed: random seed; the same seed always gives the same values
		  - loc: centre of the distribution
		  - scale: spread (diversity)
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| LAPLACEDIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# LaplaceDistFunc
		/**
		  random_gumbel(seed, loc, scale, [shape]) - generates Gumbel distributed random values
		  - seed: random seed; the same seed always gives the same values
		  - loc: mode of the distribution
		  - scale: spread
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| GUMBELDIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# GumbelDistFunc
		/**
		  random_weibull(seed, scale, concentration, [shape]) - generates Weibull distributed random values
		  - seed: random seed; the same seed always gives the same values
		  - scale: scale lambda
		  - concentration: shape k
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| WEIBULLDIST LPAREN expr COMMA expr COMMA expr (COMMA expr)? RPAREN	# WeibullDistFunc
		/**
		  random_chi2(seed, df, [shape]) - generates Chi-squared distributed random values
		  - seed: random seed; the same seed always gives the same values
		  - df: degrees of freedom
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| CHI2DIST LPAREN expr COMMA expr (COMMA expr)? RPAREN	# Chi2DistFunc
		/**
		  random_studentt(seed, df, [shape]) - generates Student-t distributed random values
		  - seed: random seed; the same seed always gives the same values
		  - df: degrees of freedom
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| STUDENTTDIST LPAREN expr COMMA expr (COMMA expr)? RPAREN	# StudentTDistFunc
		/**
		  perlin_noise(seed, scale, [octaves], [offset], [shape]) - generates Perlin gradient noise in 0-1 (default 1 octave)
		  - seed: random seed; the same seed always gives the same values
		  - scale: feature size in elements; larger values give smoother noise
		  - octaves: number of detail layers, each half the size of the previous (default: 1)
		  - offset: shift of the sampling grid, one value per dimension (default: 0)
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| PERLIN LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# PerlinFunc
		/**
		  cellular_noise(seed, scale, [jitter], [offset], [shape]) - generates Cellular/Voronoi noise in 0-1: distance to the nearest feature point (jitter 0-1, default 0.5)
		  - seed: random seed; the same seed always gives the same values
		  - scale: cell size in elements
		  - jitter: 0-1 randomness of the cell points (default: 0.5)
		  - offset: shift of the sampling grid, one value per dimension (default: 0)
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| CELLULAR LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# CellularFunc
		/**
		  plasma_noise(seed, scale, [octaves], [offset], [shape]) - generates Plasma/Turbulence noise in 0-1 - same as perlin but default octaves 4
		  - seed: random seed; the same seed always gives the same values
		  - scale: feature size in elements; larger values give smoother noise
		  - octaves: number of detail layers, each half the size of the previous (default: 4)
		  - offset: shift of the sampling grid, one value per dimension (default: 0)
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| PLASMA LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# PlasmaFunc
		/**
		  ridged_noise(seed, scale, [octaves], [offset], [shape]) - generates ridged multi-fractal noise in 0-1 (default 4 octaves)
		  - seed: random seed; the same seed always gives the same values
		  - scale: feature size in elements; larger values give smoother noise
		  - octaves: number of detail layers, each half the size of the previous (default: 4)
		  - offset: shift of the sampling grid, one value per dimension (default: 0)
		  - shape: output shape as a list (default: the shape of the node's input)
		*/
	| RIDGED LPAREN expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN		# RidgedFunc
		/**
		  domain_warp_noise(seed, scale, warp_scale, warp_strength, [octaves], [warp_octaves], [offset], [shape]) - generates domain warped Perlin noise in 0-1 (defaults: 4 octaves, 2 warp octaves)
		  - seed: random seed; the same seed always gives the same values
		  - scale: feature size in elements; larger values give smoother noise
		  - warp_scale: feature size of the warp field in elements
		  - warp_strength: how far the warp field displaces the coordinates
		  - octaves: detail layers of the base noise (default: 4)
		  - warp_octaves: detail layers of the warp field (default: 2)
		  - offset: shift of the sampling grid, one value per dimension (default: 0)
		  - shape: output shape as a list (default: the shape of the node's input)
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
SINC: 'sinc';
CBRT: 'cbrt';
RECIPROCAL: 'reciprocal';
LOGADDEXP: 'logaddexp';
LOGSUMEXP: 'logsumexp';
NORM: 'norm';
NORMALIZE: 'normalize';
GROUP_NORM: 'group_norm';
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
SIGM_KARRAS: 'sigm_karras';
SIGM_EXPONENTIAL: 'sigm_exponential';
SIGM_POLYEXPONENTIAL: 'sigm_polyexponential';
SIGM_LAPLACE: 'sigm_laplace';
CLAMP: 'clamp';
SFFT: 'fft';
SIFFT: 'ifft';
ANGL: 'angle';
PRNT: 'print';
PRINT_SHAPE: 'print_shape' | 'pshp';
NVL: 'nvl' | 'nan_to_num';
LERP: 'lerp';
INTERP: 'interp';
SLERP: 'slerp';
STEP: 'step';
SMOOTHSTEP: 'smoothstep';
FRACT: 'fract';
RELU: 'relu';
SOFTSIGN: 'softsign';
LEAKY_RELU: 'leaky_relu';
SOFTPLUS: 'softplus';
GELU: 'gelu';
SILU: 'silu';
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
ERFC: 'erfc';
ERFINV: 'erfinv';

ANY: 'any';
ALL: 'all';
EDGE: 'edge';
DISTANCE_TRANSFORM: 'distance_transform';
GRAYSCALE: 'grayscale';
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
BLEND: 'blend';
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
REGEX_SEARCH: 'regex_search';
REGEX_REPLACE: 'regex_replace';
FORMAT: 'format';
TO_JSON: 'to_json' | 'json_encode';
FROM_JSON: 'from_json' | 'json_decode';
DILATE: 'dilate';
ERODE: 'erode';
MORPH_OPEN: 'morph_open';
MORPH_CLOSE: 'morph_close';
RGB_TO_OKLAB: 'rgb_to_oklab';
LUMINANCE: 'luminance';
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
