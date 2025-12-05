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
- Other: `floor`, `ceil`, `round`, `gamma`, `clamp`, `sigm` (sigmoid) `fft` (N-D FFT on non-batch/channel dims), `ifft` (Inverse N-D FFT, returns real component), `angle` (in ifft only)

## Variables
- **common inputs** (matches node input type):
  - `a`, `b`, `c`, `d` 
- **Extra floats**:
  - `w`, `x`, `y`, `z`   
- **IMAGE and LATENT**:
  - `C` or `channel` - channel of image 
  - `X` - position X in image. 0 is in top left
  - `Y` - position Y in image. 0 is in top left
  - `W` or `width` - width of image. y/width = 1
  - `H` or `height`- height of image. x/height = 1
  - `B` or 'batch' - position in batch
  - 'T' or 'batch_count` - number of batches
  - `N` or `channel_count` - count of channels
  - `F` or `frequency_count` – frequency count (freq domain, iFFT only)
  - `K` or `frequency` – isotropic frequency (Euclidean norm of indices, iFFT only)
  - `Kx`, `Ky`, `K_dimN` - frequency index for specific dimension
  - `Fx`, `Fy`, `F_dimN` - frequency count for specific dimension
- **AUDIO**:
  - `B` or 'batch' - position in batch
  - `N` or `channel_count` - count of channels
  - `S` or `sample` – current audio sample
  - 'T' or 'sample_count` - audio lenght in samples
  - `R` or `sample_rate` – sample rate

  - `F` – frequency count (freq domain, iFFT only)
  - `K` – isotropic frequency (freq domain, iFFT only)
- **VIDEO**
  - refer to `IMAGE and LATENT` for visual part (but `batch` is `frame` and `batch_count` is `frame_count`)
  - refer to `AUDIO` for sound part
- **NOISE**
  - refer to `IMAGE and LATENT` for most variables
  - `I` or `input_latent` – latent used as input to generate noise before noise is generated into it
- **CONDITIONING and FLOAT**
  - no additional variables

- Constants: `e`, `pi`
