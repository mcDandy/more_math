# More Math

Adds math nodes for numbers and types which do not need it. I got inspired by was_extras node.

#WARNING This node is not compatible to ComfyUI-Impact-Pack which forces older antlr version.

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Clone this repository into `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

You can also get the node from comfy manager under the name of More math.

# Features

- functions and variables in math expressions
- Nodes for CONDITIONING, LATENT, IMAGE, NOISE, FLOAT, VIDEO and AUDIO

## Operators
- Math: `+`, `-`, `*`, `/`, `%`, `^`, `||`
- Boolean: `<`, `<=`, `>`, `>=`, `==`, `!=`
  (`false = 0.0`, `true = 1.0`)

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
- `smin(x, y, ...)`: **Scalar** minimum. Returns the single smallest value across all input tensors/values.
- `smax(x, y, ...)`: **Scalar** maximum. Returns the single largest value across all input tensors/values.
- `tnorm(x)`: **Tensor** Normalizes x (L2 norm along last dimension).
- `snorm(x)`: **Scalar** L2 norm of the entire tensor.
- `swap(tensor, dim, index1, index2)`: Swaps two slices of a tensor along a specified dimension. (Tensor only)

### FFT (Tensor Only)
- `fft(x)`: Fast Fourier Transform (Time to Frequency).
- `ifft(x)`: Inverse Fast Fourier Transform (Frequency to Time).
- `angle(x)`: Returns the element-wise angle (phase) of the complex tensor.

### Utility
- `print(x)`: Prints the value of x to the console and returns x.

## Variables
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
  - 'T' or 'batch_count` - number of batches
  - `N` or `channel_count` - count of channels

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
  - `F` or `frequency_count` – frequency count (freq domain, iFFT only)
  - `K` or `frequency` – isotropic frequency (Euclidean norm of indices, iFFT only)
  - `Kx`, `Ky`, `K_dimN` - frequency index for specific dimension
  - `Fx`, `Fy`, `F_dimN` - frequency count for specific dimension
- Constants: `e`, `pi`
