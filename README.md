# More Math

Adds math nodes for numbers and types which do not need it. I got inspired by was_extras node.

## WARNING This node is not compatible to ComfyUI-Impact-Pack and ComfyUI-Ovi which forces older antlr version

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Clone this repository into `ComfyUI/custom_nodes`.
1. open command prompt/terminal/bash in your comfy folder
1. activate environment `./venv/Scripts/activate`
1. install antlr `pip install -U antlr4-python3-runtime==4.13.2`
1. Restart ComfyUI.

You can also get the node from comfy manager under the name of More math.

## Features

- functions and variables in math expressions
- Conversion between INT and FLOAT; AUDIO and IMAGE (red - real - strenght of cosine of frequency; blue - imaginary - strenght of sine of frequency; green - log1p of amplitude - just so it looks good to humans)
- Nodes for FLOAT, CONDITIONING, LATENT, IMAGE, NOISE, AUDIO, VIDEO, MODEL, CLIP and VAE

- Vector Math: Support for List literals `[v1, v2, ...]` and operations between lists/scalars/tensors

## Operators

- Math: `+`, `-`, `*`, `/`, `%`, `^`, `|x|` (norm/abs)
- Boolean: `<`, `<=`, `>`, `>=`, `==`, `!=`
  (`false = 0.0`, `true = 1.0`)
- Lists: `[v1, v2, ...]` (Vector math supported, mostly usefull in `conv` and `permute`)
  - You can also use lists to do math with input tensor (image, noise, conditioing, latent, audio) which results in batched output.
  - print_shape(a) = torch.Shape[1,1024,1024,3]; b = a*[0,0.2,-0.3]; print_shape(b) = torch.Shape[3,1024,1024,3]
  - You can <operator> batched tensor with another tensor which is not batched (dim[0] = 1) - the non batched tensor will be duplicated along batch dimension
  - In imageMath node you can use 3 element list to specify a color of image. You cannot use any imput tensor, doing so will result in behaviour in subpoint 1 in list

## Functions

### Basic Math

- `abs(x)` or `|x|`: Absolute value. For **float** `abs(x)` and `|x|` are the same. For **tensor** `abs(x)` calculates element-wise absolute value and for `|x|` it calculates L2 norm (euclidean norm).
- `sqrt(x)`: Square root.
- `ln(x)`: Natural logarithm (base e).
- `log(x)`: Logarithm base 10.
- `exp(x)`: Exponential function (e^x).
- `pow(x, y)`: Power function (x^y).
- `floor(x)`: Rounds down to nearest integer.
- `ceil(x)`: Rounds up to nearest integer.
- `round(x)`: Rounds to nearest integer.
- `fract(x)`: Returns the fractional part of x (x - floor(x)).
- `sign(x)`: Returns -1 for negative, 1 for positive, 0 for zero.
- `gamma(x)`: Gamma function.
- `range(start, end, step)`: Generates a list of values from start (inclusive) to end (exclusive) with given step.

### Trigonometric

- `sin(x)`, `cos(x)`, `tan(x)`
- `asin(x)`, `acos(x)`, `atan(x)`
- `atan2(y, x)`: Arctangent of y/x, handling quadrants.

### Hyperbolic

- `sinh(x)`, `cosh(x)`, `tanh(x)`
- `asinh(x)`, `acosh(x)`, `atanh(x)`

### Machine Learning / Activation

- `relu(x)`: Rectified Linear Unit (max(0, x)).
- `gelu(x)`: Gaussian Error Linear Unit.
- `softplus(x)`: Softplus function (log(1 + e^x)).
- `sigm(x)`: Sigmoid function (1 / (1 + e^-x)).

### Shaders / Interpolation

- `clamp(x, min, max)`: Constrains x to be between min and max.
- `lerp(a, b, w)`: Linear interpolation: `a + (b - a) * w`.
- `step(x, edge)`: Returns 1.0 if x >= edge, else 0.0.
- `smoothstep(x, edge0, edge1)`: Hermite interpolation between edge0 and edge1.

### Aggregates & Tensor Operations

- `tmin(x, y)`: Element-wise minimum of x and y.
- `tmax(x, y)`: Element-wise maximum of x and y.
- `smin(x, ...)`: **Scalar** minimum. Returns the single smallest value across all input tensors/values.
- `smax(x, ...)`: **Scalar** maximum. Returns the single largest value across all input tensors/values.
- `tnorm(x)`: **Tensor** Normalizes x (L2 norm along last dimension).
- `snorm(x)`: **Scalar** L2 norm of the entire tensor.
- `swap(tensor, dim, index1, index2)`: Swaps two slices of a tensor along a specified dimension. (Tensor only)

### Advanced Tensor Operations (Tensor Only)

- `map(tensor, c1, ...)`: Remaps `tensor` using source coordinates.
  - Up to 3 coordinate mapping functions can be provided which map to the last (up to 3) dimensions of the tensor. Rest uses identity mapping.
- `conv(tensor, kw, [kh], [kd], k_expr)`: Applies a convolution to `tensor`.
  - `k_expr` can be a math expression (using `kX`, `kY`, `kZ`) or a list literal.

- `permute(tensor, dims)`: Rearranges the dimensions of the tensor. (e.g., `permute(a, [2, 3, 0, 1])`)
- `reshape(tensor, shape)`: Reshapes the tensor to a new shape. (e.g., `reshape(a, [S0*S1, S2, S3])`)

### FFT (Tensor Only)

- `fft(x)`: Fast Fourier Transform (Time to Frequency).
- `ifft(x)`: Inverse Fast Fourier Transform (Frequency to Time).
- `angle(x)`: Returns the element-wise angle (phase) of the complex tensor.

### Utility

- `print(x)`: Prints the value of x to the console and returns x.
- `print_shape(x)` or `pshp`: Prints the shape of x to the console and returns x.

## Variables

- **Common variables (except FLOAT, MODEL, VAE and CLIP)**:
  - `D{N}` - position in n-th dimension of tensor (for example D0, D1, D2, ...)
  - `S{N}` - size of n-th dimension of tensor (for example S0, S1, S2, ...)
- **common inputs** (matches node input type):
  - `a`, `b`, `c`, `d`
- **Extra floats**:
  - `w`, `x`, `y`, `z`
- **INSIDE IFFT**
  - `F` or `frequency_count` – frequency count (freq domain, iFFT only)
  - `K` or `frequency` – isotropic frequency (Euclidean norm of indices, iFFT only)
  - `Kx`, `Ky`, `K_dimN` - frequency index for specific dimension
  - `Fx`, `Fy`, `F_dimN` - frequency count for specific dimension
- **IMAGE and LATENT**:
  - `C` or `channel` - channel of image
  - `X` - position X in image. 0 is in top left
  - `Y` - position Y in image. 0 is in top left
  - `W` or `width` - width of image. y/width = 1
  - `H` or `height`- height of image. x/height = 1
  - `B` or 'batch' - position in batch
  - `T` or `batch_count` - number of batches
  - `N` or `channel_count` - count of channels
- **IMAGE KERNEL**:
  - `kX`, `kY` - position in kernel. Centered at 0.0.
  - `kW`, `kernel_width` - width of kernel.
  - `kH`, `kernel_height` - height of kernel.
  - `kD`, `kernel_depth` - depth of kernel.

- **AUDIO**:
  - `B` or 'batch' - position in batch
  - `N` or `channel_count` - count of channels
  - `C` or `channel` - channel of audio
  - `S` or `sample` – current audio sample
  - 'T' or 'sample_count` - audio lenght in samples
  - `R` or `sample_rate` – sample rate

- **VIDEO**
  - refer to `IMAGE and LATENT` for visual part (but `batch` is `frame` and `batch_count` is `frame_count`)
  - refer to `AUDIO` for sound part
- **NOISE**
  - refer to `IMAGE and LATENT` for most variables
  - `I` or `input_latent` – latent used as input to generate noise before noise is generated into it
- **CONDITIONING and FLOAT**
  - no additional variables
- **MODEL, CLIP and VAE**
- `L` or `layer` - a position of layer from beginning of object
- `LC` or `layer_count` - a count of layers
- Constants: `e`, `pi`
