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
 * - Basic arithmetic, logical, and bitwise operations
 */
grammar MathExpr;


// Top-level entry point
start: (funcDef | varDef | stmt)* expr SEMICOLON? EOF;

funcDef:
	VARIABLE LPAREN paramList? RPAREN ARROW (block | expr) SEMICOLON # FunctionDef;

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
	| CONSTANT						# ConstantExp
	| STRING						# StringExp
	| LPAREN paramList RPAREN ARROW (block | expr)	# LambdaExp
	| LPAREN expr RPAREN			# ParenExp
	| LPAREN expr RPAREN			# ParenExp
	| PIPE expr PIPE				# AbsExp
	| LBRACKET expr (COMMA expr)* RBRACKET	# ListExp
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
          exp(x) - applies e^x to value (per element)
        */
	| EXP LPAREN expr RPAREN			# ExpFunc
        /**
          tnorm(x) - normalises tensor or list by multiplication such that sum(x^2)==1.0 for each slice. The slice is last dimension of the tensor.
        */
	| TNORM LPAREN expr RPAREN			# TNormFunc
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
          print_shape(x) - prints the shape of the tensor x
        */
	| PRINT_SHAPE LPAREN expr RPAREN		# PrintShapeFunc
        /**
          pinv(x) - computes the permutative inverse of a list x (list must have uniqe elements) -- TODO: CHECK --
        */
	| PINV LPAREN expr RPAREN			# PinvFunc
        /**
          sum(x) - computes the sum of elements of x
        */
	| SUM LPAREN expr RPAREN			# SumFunc
        /**
          mean(x) - computes the arithmetic mean of elements of x
        */
	| MEAN LPAREN expr RPAREN			# MeanFunc
        /**
          std(x) - computes the standard deviation of elements of x
        */
	| STD LPAREN expr RPAREN			# StdFunc
        /**
          var(x) - computes the variance of elements of x
        */
	| VAR LPAREN expr RPAREN			# VarFunc
        /**
          sort(x) - returns a sorted version of x (If input is tensor, it sorts the last dimension)
        */
	| SORT LPAREN expr RPAREN			# SortFunc
        /**
          any(x) - returns true if any element of x is non-zero
        */
	| ANY LPAREN expr RPAREN			# AnyFunc
        /**
          all(x) - returns true if all elements of x are non-zero
        */
	| ALL LPAREN expr RPAREN			# AllFunc
        /**
          edge(x, [matrix_size]) - detects edges in x. Matrix size denotes the size of edge detection matrix.
        */
	| EDGE LPAREN expr (COMMA expr)? RPAREN		# EdgeFunc
        /**
          median(x) - computes the median of elements of x
        */
	| MEDIAN LPAREN expr RPAREN			# MedianFunc
        /**
          mode(x) - computes the mode of elements of x
        */
	| MODE LPAREN expr RPAREN			# ModeFunc
        /**
          cumsum(x) - computes the cumulative sum over first dimension.
        */
	| CUMSUM LPAREN expr RPAREN			# CumsumFunc
        /**
          count(x) - returns the number of elements in x
        */
	| COUNT LPAREN expr RPAREN			# CountFunc
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
          stack_has(slot) - returns 1.0 if slot exists in state storage and is not empty else returns 0.0
        */
	| HAS LPAREN expr RPAREN			# HasFunc
        /**
          stack_get(slot) - returns the last pushed value in slot without popping it
        */
	| GET LPAREN expr RPAREN			# GetFunc
        /**
          argsort(x, [desc]) - returns the indices that would sort x. defaults to ascending. Uses last dimension to sort
        */
	| ARGSORT LPAREN expr (COMMA expr)? RPAREN	# ArgsortFunc
        /**
          argmin(x) - returns the index of the minimum value in flattened x
        */
	| ARGMIN LPAREN expr RPAREN			# ArgminFunc
        /**
          argmax(x) - returns the index of the maximum value in flattened x
        */
	| ARGMAX LPAREN expr RPAREN			# ArgmaxFunc
        /**
          softmax(x, [axis]) - applies the softmax function to x (sum of slice == 1.0 and max value <= 1.0). axis defaults to last.
        */
 	| SOFTMAX LPAREN expr (COMMA expr)? RPAREN	# SoftmaxFunc
        /**
          softmin(x, [axis]) - applies the softmin function to x (same as softmax(-x,[axis])). axis defaults to last.
        */
 	| SOFTMIN LPAREN expr (COMMA expr)? RPAREN	# SoftminFunc
        /**
          erf(x) - computes the error function -- TODO: MORE DESCRIPTIVE --
        */
	| ERF LPAREN expr RPAREN			# ErfFunc
        /**
          erfinv(x) - computes the inverse error function -- TODO: MORE DESCRIPTIVE --
        */
	| ERFINV LPAREN expr RPAREN			# ErfinvFunc
        /**
          unique(x) - returns the unique elements (sorted,) --TODO: FINISH --
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
          flow_to_image(x) - converts optical flow x to an RGB image. Up-Down is <COLOR1> Left-right <COLOR2>
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
	| FLOW_ANG LPAREN expr RPAREN	# FlowAngFunc;


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
          topk(x, k) - returns the k largest elements of x. For tensors it keeps them in place.
        */
	| TOPK LPAREN expr COMMA expr RPAREN			# TopkFunc
        /**
          botk(x, k) - returns the k smallest elements of x.  For tensors it keeps them in place.
        */
	| BOTK LPAREN expr COMMA expr RPAREN			# BotkFunc
        /**
          quartile(x, q) - computes the q-th quartile of x
        */
	| QUARTILE LPAREN expr COMMA expr RPAREN		# QuartileFunc
        /**
          percentile(x, p) - computes the p-th percentile of x
        */
	| PERCENTILE LPAREN expr COMMA expr RPAREN		# PercentileFunc
        /**
          quantile(x, q) - computes the q-th quantile of x
        */
	| QUANTILE LPAREN expr COMMA expr RPAREN		# QuantileFunc
        /**
          dot(x, y) - computes the dot product of x and y. Last dimension must be 3.
        */
	| DOT LPAREN expr COMMA expr RPAREN			# DotFunc
        /**
          cosine_similarity(x, y) - computes the cosine similarity between x and y.
        */
	| COSSIM LPAREN expr COMMA expr RPAREN			# CossimFunc
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
          permute(x, dims) - permutes the dimensions of tensor x according to dims
        */
	| PERM LPAREN expr COMMA expr RPAREN			# PermuteFunc
        /**
          gaussian(x, sigma, [reshape]) - applies a Gaussian blur to x with specified sigma. if reshape has value of 1.0, then it tries orienting the input such that channel is in the direction of filter. Otherwise it expect color dimension to be the last.
        */
	| GAUSSIAN LPAREN expr COMMA expr (COMMA expr)? RPAREN	# GaussianFunc
        /**
          topk_indices(x, k) - returns the indices of the k largest elements of x
        */
	| TOPK_IND LPAREN expr COMMA expr RPAREN		# TopkIndFunc
        /**
          botk_indices(x, k) - returns the indices of the k smallest elements of x
        */
	| BOTK_IND LPAREN expr COMMA expr RPAREN		# BotkIndFunc
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
          flow_apply(image, flow) - applies optical flow to an image
        */
	| FLOW_APPLY LPAREN expr COMMA expr RPAREN		# FlowApplyFunc
        /**
          rife(image1, image2, [tile_size], [iterations], [multi_scale]) - computes an intermediate frame between image1 and image2 using RIFE
          - tile_size: chuncks image to overlapping tile_size*tile_size parts to conserve memory Default is 1024x1024 when over 2MPx. When tiling size is between 0 - 1 it takes as a fraction of the resolution
          - iterations: how many times to run RIFE model. Default 12
          - multi_scale: also use low resolution of base image for giant movements
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
          substring(s, start, [end]) - returns a substring of s from start to end. If end is not supplied, it uses end of string
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
	;


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
          ifft(x, [axis]) - inverse fast Fourier transform
        */
	| SIFFT LPAREN expr (COMMA expr)? RPAREN		# SifftFunc
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
	| TEXT_IMAGE LPAREN expr COMMA expr COMMA expr (COMMA expr)? (COMMA expr)? (COMMA expr)? (COMMA expr)? (COMMA expr)? (COMMA expr)? RPAREN	# TextImageFunc;

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
	REMAP LPAREN expr COMMA expr COMMA expr COMMA expr COMMA expr RPAREN # RemapFunc;

// N-argument functions
funcN:
        /**
          smin(x, ...) - computes the minimum of inputs or elements. Tensors must have the same size or be broadcastable to same size.
        */
	SMIN LPAREN expr (COMMA expr)* RPAREN		# SMinFunc
        /**
          smax(x, ...) - computes the maximum of inputs or elements. Tensors must have the same size or be broadcastable to same size.
        */
	| SMAX LPAREN expr (COMMA expr)* RPAREN		# SMaxFunc
        /**
          map(tensor, coord1, [coord2], [coord3]) - samples/remaps input tensor using coordinates
        */
	| MAP LPAREN expr (COMMA expr)+ RPAREN		# MapFunc
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
          concatenate(x1, x2, ..., dim) - concatenates tensors along the specified dimension
        */
	| CONCAT LPAREN expr (COMMA expr)+ RPAREN	# ConcatFunc;

funcNoise:
        /**
          random_normal(seed, [shape]) - generates normally distributed random noise
        */
	NOISE LPAREN expr (COMMA expr)? RPAREN				# NoiseFunc
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
LINSPACE: 'linspace';
LOGSPACE: 'logspace';
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
CONCAT: 'cat'|'concat'|'concatenate';
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
ROLL: 'roll';
COV: 'cov';
CORR: 'corr' | 'correlation';
ENTROPY: 'entropy';
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