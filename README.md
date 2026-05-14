# More Math

Adds math nodes for numbers and types which do not need it. Inspired by the `was_extras` node.

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

- Functions and variables in math expressions.
- Conversion between `INT` and `FLOAT`, `INT` and `BOOLEAN`, and `AUDIO` and `IMAGE`
  - image/audio conversion encodes frequency content into RGB channels.
- Node support for `FLOAT`, `STRING`, `CONDITIONING`, `LATENT`, `IMAGE`, `MASK`, `NOISE`, `AUDIO`, `VIDEO`, `MODEL`, `CLIP`, `VAE`, `SIGMAS`, and `GUIDER`.
- Vector math with list literals `[v1, v2, ...]` and mixed operations between lists, scalars, and tensors.
- Custom functions `funcname(variable, variable, ...)->expression;`
  - can be used later in expressions and in other custom functions,
  - shadowing built-in functions is not supported,
  - recursion is allowed, so be careful.
- Custom variables `varname=expression;`
  - can be used later in the same expression chain,
  - compound assignments are supported: `+=`, `-=`, `*=`, `/=`, `%=`.
- Indexed assignment `a[i, j, ...] = expression;`
  - supports multidimensional tensors and nested lists,
  - scalar values and 1-element tensors/lists fill the selected slice,
  - leading singleton dimensions are squeezed when needed to match target rank.
- Control flow:
  - `if/else`
  - `while`
  - `for`
  - blocks `{ ... }`
  - `return`
  - `break`
  - `continue`
- Stack support shared across evaluations through stack connections.
  - useful for `GuiderMath` state between steps.
- Comments:
  - line comments `# ...`
  - block comments `/* ... */`
- When a tensor is expected, lists can often be used instead and will be promoted automatically.

### Control Flow Statements

- **If/Else**: `if (condition) statement [else statement]`
- **While Loops**: `while (condition) statement`
- **Blocks**: `{ statement1; statement2; ... }`
  - New variables defined in blocks are isolated and don't leak to outer scope
  - Modifications to existing variables persist to outer scope
- **Return Statements**: `return [expression];`
  - Early return from functions or top-level expressions
- **For Loops**: `for (variable in expression) statement`
  - Iterates over list elements
  - Iterates over tensor elements along dimension `0`
  - Scalars are treated as one-item iterables
- **Break/Continue**: `break;`, `continue;`
  - Control loop execution (works in `while` and `for` loops)

## Operators

- Math: `+`, `-`, `*`, `/`, `%`, `^`, `|x|` (abs / norm-style magnitude)
- Assignment: `=`, `+=`, `-=`, `*=`, `/=`, `=`
- Boolean: `<`, `<=`, `>`, `>=`, `==`, `!=`
  (`false = 0.0`, `true = 1.0`)
- Bitwise shifts: `<<`, `>>`
- Indexing: `x[i]` or `x[i, j, ...]`
  - works on tensors, nested lists, and strings,
  - supports scalar, tensor, and list indices.
- Lists: `[v1, v2, ...]`
  - vector math is supported,
  - lists can broadcast across tensor operations in many cases,
  - lists can be used for color triples, coordinates, kernel sizes, and permutations.
- **Length Mismatch Handling**: All math nodes (except Model, Clip, Vae which default to broadcast) include a `length_mismatch` option to handle inputs with different batch sizes, sample counts, or list lengths. The target length is determined by the **maximum length** among all provided inputs (`a`, `b`, `c`, `d`).
  - `do nothing`: dones **no validation** on input
  - `tile`: Repeats shorter inputs to match the maximum length.
  - `error` (Default): Raises a `ValueError` if any input lengths differ.
  - `pad`: Shorter inputs are padded with zeros to match the maximum length.

## Functions

> Functions are grouped by purpose.  
> The descriptions below reflect the runtime behavior implemented in `UnifiedMathVisitor.py`.

### 1) Core Math

#### 1.1 Elementary & Numeric
- `abs(x)` or `|x|`: absolute value; tensor/list inputs are handled element-wise.
- `sqrt(x)`: square root.
- `ln(x)`: natural logarithm.
- `log(x)`: base-10 logarithm.
- `exp(x)`: exponential `e^x`.
- `pow(x, y)`: power `x^y`.
- `floor(x)`: round down.
- `ceil(x)`: round up.
- `round(x)`: round to nearest integer.
- `fract(x)`: fractional part (`x - floor(x)`).
- `sign(x)`: sign (`-1`, `0`, `1`).
- `gamma(x)`: gamma function.
- `clamp(x, min, max)`: clamp to interval.
- `step(x, edge)`: returns `1` when `x >= edge`, otherwise `0`.
- `dist(x1, y1, x2, y2)` / `distance`: Euclidean distance between 2D points.

#### 1.2 Trigonometric
- `sin(x)`: sine in radians.
- `cos(x)`: cosine in radians.
- `tan(x)`: tangent in radians.
- `asin(x)`: inverse sine.
- `acos(x)`: inverse cosine.
- `atan(x)`: inverse tangent.
- `atan2(y, x)`: quadrant-aware inverse tangent.

#### 1.3 Hyperbolic
- `sinh(x)`: hyperbolic sine.
- `cosh(x)`: hyperbolic cosine.
- `tanh(x)`: hyperbolic tangent.
- `asinh(x)`: inverse hyperbolic sine.
- `acosh(x)`: inverse hyperbolic cosine.
- `atanh(x)`: inverse hyperbolic tangent.

#### 1.4 Activation / ML
- `relu(x)`: `max(0, x)`.
- `gelu(x)`: Gaussian Error Linear Unit.
- `softplus(x)`: smooth ReLU-like function.
- `sigm(x)`: sigmoid.
- `softmax(x, [dim])`: softmax normalization.
- `softmin(x, [dim])`: softmin normalization.
- `erf(x)`: error function.
- `erfinv(x)`: inverse error function.

#### 1.5 Interpolation & Remap
- `lerp(a, b, t)`: linear interpolation.
- `smoothstep(x, e0, e1)`: 3rd-order smooth transition.
- `smootherstep(x, e0, e1)`: 5th-order smoother transition.
- `cubic_ease(a, b, t)` / `cubic`: cubic easing interpolation.
- `sine_ease(a, b, t)` / `sine`: sine easing interpolation.
- `elastic_ease(a, b, t)` / `elastic`: elastic easing interpolation.
- `remap(v, i_min, i_max, o_min, o_max)`: map value from one interval to another.

---

### 2) Tensor, Stats & Data Ops

#### 2.1 Element-wise / Tensor Math
- `tmin(x, y)`: element-wise minimum.
- `tmax(x, y)`: element-wise maximum.
- `tnorm(x)`: L2 normalization along the last dimension.
- `snorm(x)`: scalar/tensor norm magnitude.
- `cossim(a, b)` / `cosine_similarity`: cosine similarity.
- `cov(x, y)`: covariance.
- `corr(x, y)` / `correlation`: Pearson correlation.
- `entropy(x)`: Shannon entropy.
- `flip(x, dims)`: flip selected dimensions; `dims` can be a single dimension, list, or tensor of dimensions, so multiple axes can be flipped at once.
- `swap(tensor, dim, i1, i2)`: swap two indices along dimension `dim`.

#### 2.2 Reductions & Statistical Aggregates
- `sum(x)`: sum.
- `mean(x)`: mean.
- `std(x)`: standard deviation.
- `var(x)`: variance.
- `median(x)`: median.
- `mode(x)`: mode.
- `quartile(x, k)`: quartile (`k` in `0..4`).
- `percentile(x, p)`: percentile (`p` in `0..100`).
- `quantile(x, q)`: quantile (`q` in `0..1`).
- `moment(x, a, k)`: k-th moment around center `a`.
- `any(x)`: `1.0` if any element is non-zero.
- `all(x)`: `1.0` if all elements are non-zero.
- `count(x)` / `length(x)` / `cnt(x)`: number of elements or length.
- `cumsum(x)`: cumulative sum along dimension `0`.
- `cumprod(x)`: cumulative product along dimension `0`.
- `smin(x, ...)`: scalar minimum across inputs.
- `smax(x, ...)`: scalar maximum across inputs.

#### 2.3 Sorting / Selection / Indices
- `sort(x)`: tensors are sorted along the last dimension (`dim=-1`); lists use Python sorting.
- `argsort(x, [descending])`: returns indices along the last dimension, default `descending=false`.
- `argmin(x)`: global minimum index for tensors; list index for lists.
- `argmax(x)`: global maximum index for tensors; list index for lists.
- `topk(x, k)`: tensors keep the same shape and all non-top-k values are zeroed; lists return the sorted top-k slice.
- `botk(x, k)`: same as `topk`, but for smallest values.
- `topk_ind(x, k)` / `topk_indices`: global top-k indices from `flatten()`.
- `botk_ind(x, k)` / `botk_indices`: global bottom-k indices from `flatten()`.
- `unique(x)`: sorted unique values for tensors and lists.
- `where(cond, a, b)`: tensor broadcasting for tensor inputs; recursive truthy selection for lists/scalars.
- `histogram(x, bins, min, max)` / `hist`: histogram counts from `flatten()` in the given interval.

#### 2.4 Shape / Structure / Layout
- `shape(x)`: returns shape as a Python list.
- `flatten(x)`: flattens tensor or nested list.
- `reshape(tensor, shape)` / `rshp`: reshape with element-count validation.
- `permute(tensor, dims)` / `perm`: reorder dimensions.
- `crop(tensor, position, size)`: extract a region from tensor or string.
- `pad(tensor, padding)`: pad tensor.
- `overlay(base, overlay, offset, [opacity])`: overlay one value/tensor onto another.
- `append(a, b)`: append or concatenate items, lists, and tensors.
- `batch_shuffle(tensor, indices)` / `shuffle` / `select`: reorder along batch dimension.
- `concatenate(..., dim)` / `concat` / `cat`: concatenate tensors or lists.
- `roll(tensor, shifts, [dim])`: circular shift.
- `tensor(shape, [value, [type]])`: create a filled tensor; `type` a tensor to copy its dtype to self when being created.
- `interpolate_linear(tensor, scale)`: linear interpolation-based resizing. Scale can be a single float or a list. When it is a list, it is interpreted as the target output size.
- `interpolate_area(tensor, scale)`: area interpolation-based resizing.
- `interpolate_nearest(tensor, scale)`: nearest neighbor interpolation-based resizing.

#### 2.5 Linear Algebra
- `dot(a, b)`: dot product after flattening.
- `matmul(a, b)`: matrix multiplication.
- `cross(a, b)`: cross product; last dimension must be `3`.
- `pinv(x)`: permutation inverse for permutation-like values.

#### 2.6 Mapping / Sampling
- `map(tensor, c1, ...)`: coordinate remapping via `grid_sample`.
  - supports up to `3` coordinate inputs,
  - uses sampling coordinates derived from the provided coordinate tensors,
  - intended for spatial remapping / resampling.
- `get_value(tensor, position)`: read value at an N-D position using flat offset math.

---

### 3) Imaging & Spatial Processing

#### 3.1 Filters & Convolution
- `blur(x, sigma)` / `gaussian`: Gaussian blur using separable convolution.
- `edge(x, [kernel_size])`: Sobel-style edge detection.
- `ezconvolution(tensor, ...)` / `ezconv`: convolution with auto layout handling.
- `convolution(tensor, ...)` / `conv`: direct convolution.

#### 3.2 Mask Morphology
- `dilate(x, [kernel_size])`: dilation.
- `erode(x, [kernel_size])`: erosion.
- `morph_open(x, [kernel_size])`: opening = erosion followed by dilation.
- `morph_close(x, [kernel_size])`: closing = dilation followed by erosion.

---

### 4) Optical Flow
- `rife(img1, img2, [tiling_size, iterations, multi_scale])`: compute optical flow.
- `motion_mask(flow)`: motion/occlusion mask from flow.
- `flow_to_image(flow)`: visualize flow as RGB.
- `flow_apply(image, flow)`: warp image by flow.
- `flow_mag(flow)` / `flow_magnitude`: flow vector magnitude (or anything else, uses first 2 positions of last dimension).
- `flow_ang(flow)` / `flow_angle`: flow vector angle in radians (`atan2(dy, dx)`).  (or anything else, uses first 2 positions of last dimension)

---

### 5) Frequency Domain (FFT)
- `fft(x)`: fast Fourier transform across all dimensions.
- `ifft(x, [shape])`: inverse FFT.
- `angle(x)`: phase angle of complex values.

---

### 6) Random & Noise

#### 6.1 Random Distributions
- All random generators are seeded and deterministic for a given seed.
- All use the current node shape by default (based on shape of input to the node), but an optional `shape` argument can be provided to specify a different output shape.
- all use `rand<dist>(seed, [shape])` / `random_<distribution>` naming convention. `noise`/`randn`/`random_normal` is the same generator as in `Random Noise` node.
- If `shape` is omitted, the current node shape is used.
- `noise` / `randn` / `random_normal`: normal distribution.
- `rand` / `randu` / `random_uniform`: uniform distribution.
- `rande` / `random_exponential`: exponential distribution.
- `randc` / `random_cauchy`: Cauchy distribution.
- `randln` / `random_log_normal`: log-normal distribution.
- `randb` / `random_bernoulli`: Bernoulli distribution.
- `randp` / `random_poisson`: Poisson distribution.
- `randg` / `random_gamma`: gamma distribution.
- `randbeta` / `random_beta`: beta distribution.
- `randl` / `random_laplace`: Laplace distribution.
- `randgumbel` / `random_gumbel`: Gumbel distribution.
- `randw` / `random_weibull`: Weibull distribution.
- `randchi2` / `random_chi2`: chi-squared distribution.
- `randt` / `random_studentt`: Student’s t distribution.

#### 6.2 Procedural Noise
- `perlin(seed, scale, [octaves, [offset, [shape]]])` / `perlin_noise`:
  - smooth gradient noise,
  - supports arbitrary dimensional grids.
- `voronoi(seed, scale, [jitter], [offset], [shape])` / `cellular` / `worley` / `voronoi_noise` / `cellular_noise`:
  - cellular / Voronoi noise,
  - `jitter` is clamped to `0..1`.
- `plasma(seed, scale, [octaves, [offset, [shape]]])` / `turbulence` / `plasma_noise`:
  - high-frequency turbulence-style noise.

---

### 7) Bitwise

#### 7.1 Shift Operators
 - `a << b`: Bitwise left shift.
 - `a >> b`: Bitwise right shift.

 #### 7.2 Bitwise Functions
- `band(a, b)` / `bitwise_and`: bitwise AND.
- `bor(a, b)` / `bitwise_or`: bitwise OR.
- `bxor(a, b)` / `bitwise_xor`: bitwise XOR.
- `bnot(a)` / `bitwise_not`: bitwise NOT.
- `bitcount(a)` / `popcount` / `popcnt`: number of set bits.

---

### 8) Strings
- `upper(str)`: convert to uppercase.
- `lower(str)`: convert to lowercase.
- `trim(str)`: trim surrounding whitespace.
- `split(str, [delimiter])`: split string.
- `join(list, [separator])`: join list into string.
- `substring(str, start, [length])` / `substr`: substring extraction.
- `find(str, search)`: first match position.
- `replace(str, search, replacement)`: replace occurrences.

---

### 9) Color
- `rgb_to_hsv(...)`: convert RGB to HSV.
  - accepts packed tensor/list input or separate `r, g, b`,
  - optional fourth boolean argument enables hue in degrees.
- `hsv_to_rgb(...)`: convert HSV to RGB.
  - accepts packed tensor/list input or separate `h, s, v`,
  - optional fourth boolean argument treats hue as degrees.
- `rgb_to_oklab(...)`: convert RGB to OKLab.
   - accepts packed tensor/list input or separate `r, g, b`.
- `oklab_to_rgb(...)`: convert OKLab to RGB.
   - accepts packed tensor/list input or separate `L, a, b`.
-  `rgb_to_cielab(...)`: convert RGB to CIELAB.
   - accepts packed tensor/list input or separate `r, g, b`.
-  `cielab_to_rgb(...)`: convert CIELAB to RGB.
   - accepts packed tensor/list input or separate `L, a, b`.
- `int_to_rgb(value)`: convert packed integer color to RGB triplet.
- `rgb_to_int(...)`: convert RGB triplet to packed integer color.

---

### 10) Utility & Conversion
- `print(x)`: print value and return it.
- `print_shape(x)` / `pshp`: print shape and return value.
- `range(start, end, step)`: numeric sequence as a list.
- `linspace(start, end, count)`: evenly spaced sequence.
- `logspace(start, end, count, base)`: logarithmically spaced sequence.
- `nan_to_num(x, nan, posinf, neginf)` / `nvl`: replace `NaN` and infinities.
- `timestamp()` / `now`: current Unix timestamp.
- `int(x)`: convert to int32 or nested int values.
- `float(x)`: convert to float or nested float values.

---

### 11) State / Stack
- `stack_push(id, value)`: push into stack slot.
- `stack_pop(id)`: pop from stack slot.
- `stack_get(id)`: read top value without removing it.
- `stack_clear(id)`: clear stack slot.
- `stack_has(id)`: check whether slot exists and is non-empty.

## Variables

 - **Common variables (except FLOAT)**:
-  - `D{N}` - position in n-th dimension of tensor, for example `D0`, `D1`, `D2`
-  - `S{N}` - size of n-th dimension of tensor, for example `S0`, `S1`, `S2`
-  - `V{N}` - value input, for example `V0`, `V1`, `V2`
-  - `V` - list of value inputs
-  - `F{N}` - float input, for example `F0`, `F1`, `F2`
-  - `F` - list of float inputs
-  - `Fcnt` or `F_count`: number of float inputs
-  - `Vcnt` or `V_count`: number of value inputs
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
   - `X` - X position in image, origin in top-left
   - `Y` - Y position in image, origin in top-left
   - `W` or `width` - image width
   - `H` or `height` - image height
   - `B` or `batch` - batch index
   - `T` or `batch_count` - number of batches
   - `N` or `channel_count` - channel count
 - **IMAGE KERNEL**:
   - `kX`, `kY` - position in kernel, centered at `0.0`
   - `kW`, `kernel_width` - kernel width
   - `kH`, `kernel_height` - kernel height
   - `kD`, `kernel_depth` - kernel depth

 - **AUDIO**:
   - `B` or `batch` - batch index
   - `N` or `channel_count` - channel count
   - `C` or `channel` - audio channel
   - `S` or `sample` - current sample
   - `T` or `sample_count` - audio length in samples
   - `R` or `sample_rate` - sample rate

 - **VIDEO**
   - refer to `IMAGE and LATENT` for the visual part
   - `batch` means `frame`
   - `batch_count` means `frame_count`
   - refer to `AUDIO` for sound part
 - **NOISE**
   - refer to `IMAGE and LATENT` for most variables
   - `I` or `input_latent` - latent used as input to generate noise
 - **GUIDER**
   - refer to `IMAGE and LATENT`
   - `sigma` - current sigma value
   - `seed` - seed used for noise generation
   - `steps` - total number of sampling steps
   - `current_step` - current step index, `0..steps`
   - `sample` - tensor input to guider or output from sampling

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
