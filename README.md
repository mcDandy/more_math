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
- Nodes for CONDITIONING, LATENT, IMAGE, NOISE, FLOAT, and AUDIO

## Operators
- Math: `+`, `-`, `*`, `/`, `%`, `^`
- Boolean: `<`, `<=`, `>`, `>=`, `==`, `!=`  
  (`false = 0.0`, `true = 1.0`)

## Functions
- Basic: `abs`, `sqrt`, `ln`, `log`, `exp`, `pow`
- Trigonometric: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2`
- Hyperbolic: `sinh`, `cosh`, `tanh`, `asinh`, `acosh`, `atanh`
- Aggregates: `smin`, `smax` , `snorm` (scalar), `tmin`, `tmax`, `tnorm` (elementwise)
- Other: `floor`, `ceil`, `round`, `gamma`, `clamp`, `sigm` (sigmoid), `angle` (in ifft only)
- Audio-specific: `fft` (short-time FFT), `ifft` (inverse sFFT **always return audio back to time domain**)

## Variables
- **Inputs**: `a`, `b`, `c`, `d` (matches node input type)  
- **Extra floats**: `w`, `x`, `y`, `z`   
- **Tensor positions**:  `C` (channel), `B` (batch), `X`, `Y`, `W` (width), `H` (height) (not for FLOAT/AUDIO/CONDITIONING)
- **Special**:
  - `I` – sampler init tensor (for NOISE only)  
  - `S` – current audio sample (AUDIO only)  
  - `T` – audio length  (AUDIO only)  
  - `R` – sample rate (AUDIO only)  
  - `F` – frequency count (freq domain, iFFT only)  
  - `K` – current frequency (freq domain, iFFT only)  
- Constants: `e`, `pi`
