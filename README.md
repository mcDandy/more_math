# More Math

Adds math nodes for numbers and types which do not need it. I got inspired by was_extras node.

## WARNING This node is not compatible to ComfyUI-Impact-Pack and ComfyUI-Ovi which forces older antlr version via omegaconf

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Clone this repository into `ComfyUI/custom_nodes`.
1. open command prompt/terminal/bash in your comfy folder
1. activate environment `./venv/Scripts/activate`
1. go to more_math folder `cd ./custom_nodes/more_math/`
1. install requirements `pip install -r requirements.txt`
1. Restart ComfyUI.

You can also get the node from comfy manager under the name of More math.

## Features

- functions and variables in math expressions
- Conversion between INT and FLOAT; INT and BOOLEAN; AUDIO and IMAGE (red - real - strenght of cosine of frequency; blue - imaginary - strenght of sine of frequency; green - log1p of amplitude - just so it looks good to humans)
- Nodes for FLOAT, STRING, CONDITIONING, LATENT, IMAGE, MASK, NOISE, AUDIO, VIDEO, MODEL, CLIP, VAE, SIGMAS and GUIDER
- Vector Math: Support for List literals `[v1, v2, ...]` and operations between lists/scalars/tensors
- Custom functions `funcname(variable,variable,...)->expression;` they can be used in any later defined custom function or in expression. Shadowing inbuilt functions do not work. **Be careful with recursion. There is no stack limit. Got to 700 000 iterations before I got bored.**
- Custom variables `varname=expression;` They can be used in any later assigment or final expression. Compound assignments (`+=`, `-=`, `*=`, `/=`, `%=`) are also supported.
- Support for **indexed assignment**: `a[i, j, ...] = expression;`. Supports multidimensional tensors and nested lists.
  - **Scalar Filling**: If the assigned value has only 1 element (scalar, 1-element list/tensor), it fills the entire selected slice.
  - **Rank Matching**: Automatically squeezes leading ones from the value to match the rank of the target slice (e.g., assigning a 4D tensor with `dim0=1` to a 3D slice).
- Support for control flow statements including `if/else`, `while` loops, blocks `{}`, and `return` statements. `if`/`else`/`while` do not work like ternary operator or other inbuilts. They colapse tensors and list to single value using any.
- Support for stack. Stack survives between field evaluations and can be passed around using stack connection.
  - Usefull in GuiderMath node to store variables between steps.
- comments `#...` and `/*...*/`
- In places which expact only tensors you can use lists of lists.

### Control Flow Statements

- **If/Else**: `if (condition) statement [else statement]`
- **While Loops**: `while (condition) statement`
- **Blocks**: `{ statement1; statement2; ... }`
  - New variables defined in blocks are isolated and don't leak to outer scope
  - Modifications to existing variables persist to outer scope
- **Return Statements**: `return [expression];`
  - Early return from functions or top-level expressions
- **For Loops**: `for (variable in expression) statement`
  - Iterates over elements of a list or a tensor (along dimension 0)
- **Break/Continue**: `break;`, `continue;`
  - Control loop execution (works in `while` and `for` loops)

## Operators

- Math: `+`, `-`, `*`, `/`, `%`, `^`, `|x|` (norm/abs)
- Assignment: `=`, `+=`, `-=`, `*=`, `/=`, `%=`
- Boolean: `<`, `<=`, `>`, `>=`, `==`, `!=`
  (`false = 0.0`, `true = 1.0`)
- Bitwise Shifts: `<<`, `>>` (left shift, right shift)
- Indexing: `x[i]` or `x[i, j, ...]` - Selects a sublist (if index count < number of dimensions) or value at position.
- Lists: `[v1, v2, ...]` (Vector math supported, mostly usefull in `conv` and `permute`)
  - You can also use lists to do math with input tensor (image, noise, conditioing, latent, audio) which results in batched output as long as batch size is different to list size.
  - print_shape(a) = torch.Shape[1,1024,1024,3]; b = a*[0,0.2,-0.3]; print_shape(b) = torch.Shape[3,1024,1024,3]
  - You can &lt;operator&gt; batched tensor with another tensor which is not batched (dim[0] = 1) - the non batched tensor will be duplicated along batch dimension
  - In imageMath node you can use 3 element list to specify a color of image. You cannot use any imput tensor, doing so will result in behaviour in subpoint 1 in list
- **Length Mismatch Handling**: All math nodes (except Model, Clip, Vae which default to broadcast) include a `length_mismatch` option to handle inputs with different batch sizes, sample counts, or list lengths. The target length is determined by the **maximum length** among all provided inputs (`a`, `b`, `c`, `d`).
  - `do nothing`: dones **no validation** on input
  - `tile`: Repeats shorter inputs to match the maximum length.
  - `error` (Default): Raises a `ValueError` if any input lengths differ.
  - `pad`: Shorter inputs are padded with zeros to match the maximum length.

## Functions

> Functions are grouped by purpose.  
> Each function has a short, practical description.

### 1) Core Math

#### 1.1 Elementary & Numeric
- `abs(x)` or `|x|`: Absolute value (`|x|` is norm-style usage for tensors - (vector magnitude)).
- `sqrt(x)`: Square root.
- `ln(x)`: Natural logarithm.
- `log(x)`: Base-10 logarithm.
- `exp(x)`: Exponential `e^x`.
- `pow(x, y)`: Power `x^y`.
- `floor(x)`: Round down.
- `ceil(x)`: Round up.
- `round(x)`: Round to nearest integer.
- `fract(x)`: Fractional part (`x - floor(x)`).
- `sign(x)`: Sign (`-1`, `0`, `1`).
- `gamma(x)`: Gamma function.
- `clamp(x, min, max)`: Clamp to interval.
- `step(x, edge)`: Step function (`x >= edge` -> `1`, else `0`).
- `dist(x1, y1, x2, y2)` / `distance`: Euclidean distance between 2D points.

#### 1.2 Trigonometric
- `sin(x)`: Sine (radians).
- `cos(x)`: Cosine (radians).
- `tan(x)`: Tangent (radians).
- `asin(x)`: Arc-sine.
- `acos(x)`: Arc-cosine.
- `atan(x)`: Arc-tangent.
- `atan2(y, x)`: Quadrant-aware arc-tangent.

#### 1.3 Hyperbolic
- `sinh(x)`: Hyperbolic sine.
- `cosh(x)`: Hyperbolic cosine.
- `tanh(x)`: Hyperbolic tangent.
- `asinh(x)`: Inverse hyperbolic sine.
- `acosh(x)`: Inverse hyperbolic cosine.
- `atanh(x)`: Inverse hyperbolic tangent.

#### 1.4 Activation / ML
- `relu(x)`: `max(0, x)`.
- `gelu(x)`: Gaussian Error Linear Unit.
- `softplus(x)`: Smooth ReLU-like function.
- `sigm(x)`: Sigmoid.
- `softmax(x, [dim])`: Softmax normalization.
- `softmin(x, [dim])`: Softmin normalization.
- `erf(x)`: Error function.
- `erfinv(x)`: Inverse error function.

#### 1.5 Interpolation & Remap
- `lerp(a, b, t)`: Linear interpolation.
- `smoothstep(x, e0, e1)`: 3rd-order smooth transition.
- `smootherstep(x, e0, e1)`: 5th-order smoother transition.
- `cubic_ease(a, b, t)` / `cubic`: Cubic easing interpolation.
- `sine_ease(a, b, t)` / `sine`: Sine easing interpolation.
- `elastic_ease(a, b, t)` / `elastic`: Elastic easing interpolation.
- `remap(v, i_min, i_max, o_min, o_max)`: Map value from one interval to another.

---

### 2) Tensor, Stats & Data Ops

#### 2.1 Element-wise / Tensor Math
- `tmin(x, y)`: Element-wise minimum.
- `tmax(x, y)`: Element-wise maximum.
- `tnorm(x)`: L2 normalization along the last dimension.
- `snorm(x)`: Scalar/tensor norm magnitude.
- `cossim(a, b)` / `cosine_similarity`: Cosine similarity.
- `cov(x, y)`: Covariance.
- `corr(x, y)` / `correlation`: Pearson correlation.
- `entropy(x)`: Shannon entropy.
- `flip(x, dims)`: Flip along selected dimensions.
- `swap(tensor, dim, i1, i2)`: Swap two indices/slices along dimension `dim`.

#### 2.2 Reductions & Statistical Aggregates
- `sum(x)`: Sum.
- `mean(x)`: Mean.
- `std(x)`: Standard deviation.
- `var(x)`: Variance.
- `median(x)`: Median.
- `mode(x)`: Mode.
- `quartile(x, k)`: Quartile (`k` in 0..4).
- `percentile(x, p)`: Percentile (`p` in 0..100).
- `quantile(x, q)`: Quantile (`q` in 0..1).
- `moment(x, a, k)`: k-th moment around center `a`.
- `any(x)`: True if any element is non-zero.
- `all(x)`: True if all elements are non-zero.
- `count(x)` / `length(x)` / `cnt(x)`: Number of elements / length.
- `cumsum(x)`: Cumulative sum.
- `cumprod(x)`: Cumulative product.
- `smin(x, ...)`: Scalar minimum across inputs.
- `smax(x, ...)`: Scalar maximum across inputs.

#### 2.3 Sorting / Selection / Indices
- `sort(x)`: Sort values.
- `argsort(x, [descending])`: Sorting indices.
- `argmin(x)`: Index of minimum.
- `argmax(x)`: Index of maximum.
- `topk(x, k)`: Top-K values.
- `botk(x, k)`: Bottom-K values.
- `topk_ind(x, k)` / `topk_indices`: Top-K indices.
- `botk_ind(x, k)` / `botk_indices`: Bottom-K indices.
- `unique(x)`: Unique values.
- `where(cond, a, b)`: Conditional selection (`a` where true, else `b`).
- `histogram(x, bins, min, max)` / `hist`: Histogram counts in range.

#### 2.4 Shape / Structure / Layout
- `shape(x)`: Return shape.
- `flatten(x)`: Flatten tensor/list.
- `reshape(tensor, shape)` / `rshp`: Reshape.
- `permute(tensor, dims)` / `perm`: Reorder dimensions.
- `crop(tensor, position, size)`: Extract region.
- `pad(tensor, padding)`: Pad tensor.
- `overlay(base, overlay, offset, [opacity])`: Overlay one value/tensor onto another.
- `append(a, b)`: Append items/slices.
- `batch_shuffle(tensor, indices)` / `shuffle` / `select`: Reorder batch dimension.
- `concatenate(..., dim)` / `concat` / `cat`: Concatenate tensors/lists.
- `roll(tensor, shifts, [dims])`: Circular shift.
- `tensor(shape, [value, [type]])`: Create filled tensor.

#### 2.5 Linear Algebra
- `dot(a, b)`: Dot product.
- `matmul(a, b)`: Matrix multiplication.
- `cross(a, b)`: Cross product.
- `pinv(x)`: Permutation inverse (for permutation-like inputs).

#### 2.6 Mapping / Sampling
- `map(tensor, c1, ...)`: Coordinate remapping.
- `get_value(tensor, position)`: Read value at N-D position.

---

### 3) Imaging & Spatial Processing

#### 3.1 Filters & Convolution
- `blur(x, sigma)` / `gaussian`: Gaussian blur.
- `edge(x, [kernel_size])`: Sobel-style edge detection.
- `ezconvolution(tensor, ...)` / `ezconv`: Convolution with auto layout handling.
- `convolution(tensor, ...)` / `conv`: Direct convolution.

#### 3.2 Mask Morphology
- `dilate(x, [kernel_size])`: Dilation.
- `erode(x, [kernel_size])`: Erosion.
- `morph_open(x, [kernel_size])`: Opening (erosion then dilation).
- `morph_close(x, [kernel_size])`: Closing (dilation then erosion).

---

### 4) Optical Flow
- `rife(img1, img2, [tiling_size, iterations, multi_scale])`: Compute optical flow.
- `motion_mask(flow)`: Motion/occlusion mask from flow.
- `flow_to_image(flow)`: Visualize flow as RGB.
- `flow_apply(image, flow)`: Warp image by flow.
- `flow_mag(flow)` / `flow_magnitude`: Flow vector magnitude.
- `flow_ang(flow)` / `flow_angle`: Flow vector angle in radians (`atan2(dy, dx)`).

---

### 5) Frequency Domain (FFT)
- `fft(x)`: Fast Fourier Transform.
- `ifft(x, [shape])`: Inverse FFT.
- `angle(x)`: Phase angle of complex values.

---

### 6) Random & Noise

#### 6.1 Random Distributions
- `random_normal(seed, [shape])` / `randn` / `noise`: Normal distribution.
- `random_uniform(seed, [shape])` / `rand` / `randu`: Uniform distribution.
- `random_exponential(seed, lambda, [shape])` / `rande`: Exponential distribution.
- `random_cauchy(seed, median, sigma, [shape])` / `randc`: Cauchy distribution.
- `random_log_normal(seed, mean, std, [shape])` / `randln`: Log-normal distribution.
- `random_bernoulli(seed, p, [shape])` / `randb`: Bernoulli distribution.
- `random_poisson(seed, lambda, [shape])` / `randp`: Poisson distribution.
- `random_gamma(seed, shape, scale, [shape])` / `randg`: Gamma distribution.
- `random_beta(seed, alpha, beta, [shape])` / `randbeta`: Beta distribution.
- `random_laplace(seed, loc, scale, [shape])` / `randl`: Laplace distribution.
- `random_gumbel(seed, loc, scale, [shape])` / `randgumbel`: Gumbel distribution.
- `random_weibull(seed, scale, concentration, [shape])` / `randw`: Weibull distribution.
- `random_chi2(seed, df, [shape])` / `randchi2`: Chi-squared distribution.
- `random_studentt(seed, df, [shape])` / `randt`: Student’s t distribution.

#### 6.2 Procedural Noise
- `perlin(seed, scale, [octaves, [offset, [shape]]])` / `perlin_noise`: Perlin noise.
- `voronoi(seed, scale, [jitter], [offset], [shape])` / `cellular` / `worley` / `voronoi_noise` / `cellular_noise`: Voronoi/cellular noise.
- `plasma(seed, scale, [octaves, [offset, [shape]]])` / `turbulence` / `plasma_noise`: Plasma/turbulence noise.

---

### 7) Bitwise

#### 7.1 Shift Operators
- `a << b`: Bitwise left shift.
- `a >> b`: Bitwise right shift.

#### 7.2 Bitwise Functions
- `band(a, b)` / `bitwise_and`: Bitwise AND.
- `bor(a, b)` / `bitwise_or`: Bitwise OR.
- `bxor(a, b)` / `bitwise_xor`: Bitwise XOR.
- `bnot(a)` / `bitwise_not`: Bitwise NOT.
- `bitcount(a)` / `popcount` / `popcnt`: Number of set bits.

---

### 8) Strings
- `upper(str)`: Convert to uppercase.
- `lower(str)`: Convert to lowercase.
- `trim(str)`: Trim surrounding whitespace.
- `split(str, [delimiter])`: Split string.
- `join(list, [separator])`: Join list into string.
- `substring(str, start, [length])` / `substr`: Substring extraction.
- `find(str, search)`: First match position.
- `replace(str, search, replacement)`: Replace occurrences.

---

### 9) Color
- `rgb_to_hsv(...)`: Convert RGB to HSV.
- `hsv_to_rgb(...)`: Convert HSV to RGB.
- `int_to_rgb(value)`: Convert packed integer color to RGB.
- `rgb_to_int(...)`: Convert RGB to packed integer color.

---

### 10) Utility & Conversion
- `print(x)`: Print value and return it.
- `print_shape(x)` / `pshp`: Print shape and return value.
- `range(start, end, step)`: Numeric sequence.
- `linspace(start, end, count)`: Evenly spaced sequence.
- `logspace(start, end, count, base)`: Log-spaced sequence.
- `nan_to_num(x, nan, posinf, neginf)` / `nvl`: Replace `NaN` / infinities.
- `timestamp()` / `now`: Current Unix timestamp.
- `int(x)`: Convert to int32.
- `float(x)`: Convert to float.

---

### 11) State / Stack
- `stack_push(id, value)`: Push into stack slot.
- `stack_pop(id)`: Pop from stack slot.
- `stack_get(id)`: Read top value without pop.
- `stack_clear(id)`: Clear stack slot.
- `stack_has(id)`: Check slot existence/non-empty state.

## Variables

- **Common variables (except FLOAT, MODEL, VAE and CLIP)**:
  - `D{N}` - position in n-th dimension of tensor (for example D0, D1, D2, ...)
  - `S{N}` - size of n-th dimension of tensor (for example S0, S1, S2, ...)
  - `V{N}` - value input (for example V0, V1, V2, ...) - input type
  - `V` - list of value inputs
  - `F{N}` - float input (for example F0, F1, F2, ...) - float type
  - `F` - list of float inputs
  - `Fcnt` or `F_count`: Number of float inputs.
  - `Vcnt` or `V_count`: Number of value inputs.
  - `depth`: Current recursion depth (0 at top level)
- **common inputs** (legacy):
  - `a`, `b`, `c`, `d`
- **Extra floats** (legacy):
  - `w`, `x`, `y`, `z`
- **INSIDE IFFT**
  - `F` or `frequency_count` – frequency count (freq domain, iFFT only)
  - `K` or `frequency` - isotropic frequency (Euclidean norm of indices, iFFT only)
  - `Kx`, `Ky`, `K_dimN` - frequency index for specific dimension
  - `Fx`, `Fy`, `F_dimN` - frequency count for specific dimension
- **IMAGE and LATENT**:
  - `C` or `channel` - channel of image
  - `X` - position X in image. 0 is in top left
  - `Y` - position Y in image. 0 is in top left
  - `W` or `width` - width of image. y/width = 1
  - `H` or `height`- height of image. x/height = 1
  - `B` or `batch` - position in batch
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
  - `T` or `sample_count` - audio lenght in samples
  - `R` or `sample_rate` - sample rate

- **VIDEO**
  - refer to `IMAGE and LATENT` for visual part (but `batch` is `frame` and `batch_count` is `frame_count`)
  - refer to `AUDIO` for sound part
- **NOISE**
  - refer to `IMAGE and LATENT` for most variables
  - `I` or `input_latent` - latent used as input to generate noise before noise is generated into it
- **GUIDER**
  - refer to `IMAGE and LATENT`
  - `sigma` - current sigma value
  - `seed` - seed used for noise generation
  - `steps` - total number of sampling steps
  - `current_step` - current step index (0 to steps)
  - `sample` - tensor input to guider or output from sampling

- **CONDITIONING, SIGMAS and FLOAT**
  - no additional variables
- **MODEL, CLIP and VAE**
  - `L` or `layer` - a position of layer from beginning of object
  - `LC` or `layer_count` - a count of layers
  - `K` or `key` - a string key for layer (for example "conv1.weight" or "blocks.5.attn.q_proj.weight")
- **Constants**: `e`, `pi`

## SelectiveGuiderMathNode (hooking)

Adds support for hooking into specific layers/blocks of the model during guided diffusion.

Current implementation details:

- `hook_target` supports runtime filtering in node UI.
- `layer_x` is used as direct index match (`idx == layer_x`) for current hook context.
- For guiders with `original_conds`, base conditions are restored before reattaching hooks to avoid hook accumulation across reruns/interrupted runs.
- Active hook paths currently include:
  - Attention override (`attn1` / `attn2` / `double_block_attn` / `single_block_attn` / `attn_unknown`)
  - DiT block replace (`dit.double_block`, `dit.single_block`)
  - UNet block patches (`input_block_patch`, `middle_patch`, `output_block_patch`)
  - Timestep embedding start via `emb_patch` (`block_name="time_emb"`, `layer_x=0`)
  - Whole-model edges via diffusion-model wrapper (`model_begin`, `model_end`)

### Side behavior (positive / negative)

When guider has `original_conds`, hooks are attached separately for:

- `positive`
- `negative`

Runtime variables expose side information:

- `cond_side`: `"positive" | "negative" | "mixed" | "unknown"`
- `cond_index`: `0 | 1 | -1`
- `is_positive`: `1.0` or `0.0`
- `is_negative`: `1.0` or `0.0`

### Variable reference (`SelectiveGuiderMathNode`)

The following variables are available in `Expression`.

| Variable | Type | Description |
|---|---|---|
| `inp` | tensor | Current tensor received by the active hook. |
| `sample` | tensor | Alias of `inp`. |
| `F0..Fn` | float/tensor | Individual float inputs from the node. |
| `F` | list/tensor | Collection of all float inputs. |
| `D0..Dn` | tensor | Per-dimension index tensors from `generate_dim_variables`. |
| `S0..Sn` | float | Per-dimension sizes from `generate_dim_variables`. |
| `hook_kind` | string | Active hook identifier: `attn1`, `attn2`, `double_block_attn`, `single_block_attn`, `attn_unknown`, `dit_block`, `unet_block`, `model_begin`, `model_end`, or `unknown`. |
| `hook_domain` | string | High-level domain: `attention`, `diffusion`, or `unknown`. |
| `attn_kind` | string | Attention kind: `attn1`, `attn2`, `double_block_attn`, `single_block_attn`, `attn_unknown`, or `none` outside attention hooks. |
| `transformer_index` | float | Attention sub-block index inside a UNet block (`-1` if unavailable). |
| `is_attn1` | float (0/1) | `1` when current hook is `attn1`, else `0`. |
| `is_attn2` | float (0/1) | `1` when current hook is `attn2`, else `0`. |
| `is_attn1_hook` | float (0/1) | `1` when `attn_kind=="attn1"`, else `0`. |
| `is_attn2_hook` | float (0/1) | `1` when `attn_kind=="attn2"`, else `0`. |
| `is_dit` | float (0/1) | `1` when current hook is DiT block hook, else `0`. |
| `is_unet_block` | float (0/1) | `1` when current hook is UNet block hook, else `0`. |
| `is_time_emb` | float (0/1) | `1` when current hook is timestep embedding entry (`block_name=="time_emb"`), else `0`. |
| `block_name` | string | Block/stage name (`input`, `middle`, `output`, `time_emb`, `model`, DiT block type, etc.). |
| `layer_id` | float | Numeric block/layer id used by current hook context. |
| `layer` | float | Alias of `layer_id`. |
| `i` | float | Alias of `layer_id`. |
| `layer_key` | string | Composite identifier for debug/filtering (for example `output.6.attn2.0`, `unet.time_emb.0`, `model.begin`). |
| `total_blocks` | float | Total blocks in stream if available, otherwise `-1`. |
| `has_qkv` | float (0/1) | `1` in attention hooks where `q/k/v` are valid; `0` in diffusion/block hooks. |
| `q` | tensor | Query tensor in attention hooks; fallback placeholder otherwise. |
| `k` | tensor | Key tensor in attention hooks; fallback placeholder otherwise. |
| `v` | tensor | Value tensor in attention hooks; fallback placeholder otherwise. |
| `heads` | float | Number of attention heads (attention hooks only, else `0`). |
| `dim_head` | float | Per-head channel size (`q.shape[-1] / heads`) when available. |
| `activations_shape` | list | Raw shape from transformer context. Empty list if unavailable. |
| `activation_b` | float | Batch dimension from `activations_shape[0]` (or `-1`). |
| `activation_c` | float | Channel dimension from `activations_shape[1]` (or `-1`). |
| `activation_h` | float | Height dimension from `activations_shape[2]` (or `-1`). |
| `activation_w` | float | Width dimension from `activations_shape[3]` (or `-1`). |
| `attn_mode` | string | Legacy compatibility field (default `unknown`). |
| `attention_relation` | string | Inferred semantic relation: `self`, `cross`, or `unknown`. |
| `is_self_attention` | float (0/1) | `1` when the active attention is self-attention. |
| `is_cross_attention` | float (0/1) | `1` when the active attention is cross-attention. |
| `has_context` | float (0/1) | `1` when attention context appears to be present. |
| `query_tokens` | float | Query sequence length. |
| `context_tokens` | float | Context sequence length. |
| `value_tokens` | float | Value sequence length. |
| `activation_rank` | float | Rank of `activations_shape`. |
| `activation_t` | float | Temporal dimension for video-like activations (`-1` if unavailable). |

#### Practical notes

- On SD1.x, repeated hits on the same `layer_id` are normal in attention because one UNet block can contain multiple transformer sub-blocks.
- Use `transformer_index` to target exactly one sub-block.
- For timestep-begin hooking use `layer_x=0` and filter by `block_name=="time_emb"` (or `layer_key=="unet.time_emb.0"`).
- For model-edge hooks filter by `hook_kind=="model_begin"` or `hook_kind=="model_end"`.
- For model-agnostic expressions, prefer guard variables: `has_qkv`, `is_dit`, `is_unet_block`, `is_attn1`, `is_attn2`.
- `attn2` is only a hook label, not guaranteed to mean real cross-attention.
- Use `is_cross_attention` only as an inferred relation from runtime metadata.
- Use `attention_relation` for semantic relation (`self`/`cross`) and `attn_kind` for hook-path classification.

- Selective guider math:
  - `hook_target`: `all`, `dit_block`, `unet_block`, `attn1`, `attn2`,
    `double_block_attn`, `single_block_attn`, `model_begin`, `model_end`
