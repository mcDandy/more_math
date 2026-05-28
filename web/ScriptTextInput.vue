<template>
  <div
    class="mrmth-editor"
    ref="wrapperRef"
    :style="editorStyle"
  >
    <!-- Gutter / Line Numbers -->
    <div class="mrmth-gutter">
      <div
        ref="gutterContentRef"
        class="mrmth-gutter-content"
        :style="gutterStyle"
      >
        <div
          v-for="(line, idx) in gutterLines"
          :key="idx"
          class="mrmth-gutter-line"
        >
          <span v-if="line === ' '" class="mrmth-baseline-probe"></span>
          {{ line }}
        </div>
      </div>
    </div>

    <!-- Editor Container -->
    <div class="mrmth-editor-container" ref="editorContainerRef">
      <!-- Measure Layer for wrapped line calculations -->
      <pre
        ref="measureElRef"
        class="mrmth-measure"
        :style="sharedTextStyle"
        v-html="measureHtml"
      ></pre>

      <!-- Syntax Highlighting Layer -->
      <pre
        ref="syntaxLayerRef"
        class="mrmth-syntax-layer"
        :style="sharedTextStyle"
        v-html="highlightedHtml"
      ></pre>

      <!-- Textarea -->
      <textarea
        ref="textareaRef"
        v-model="modelValue"
        class="mrmth-script-textarea"
        :style="sharedTextStyle"
        spellcheck="false"
        autocapitalize="off"
        autocomplete="off"
        autocorrect="off"
        placeholder="Enter your script here..."
        @input="onInput"
        @scroll="onScroll"
        @keydown="onKeyDown"
      ></textarea>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount, nextTick, watch } from 'vue';

// Define model for value binding
const modelValue = defineModel<string>({ default: '' });

// Refs for DOM elements
const wrapperRef = ref<HTMLDivElement | null>(null);
const gutterContentRef = ref<HTMLDivElement | null>(null);
const editorContainerRef = ref<HTMLDivElement | null>(null);
const measureElRef = ref<HTMLPreElement | null>(null);
const syntaxLayerRef = ref<HTMLPreElement | null>(null);
const textareaRef = ref<HTMLTextAreaElement | null>(null);

// Reactive state
const gutterLines = ref<string[]>(['1']);
const editorHeight = ref<string>('170px');
const scrollTop = ref<number>(0);
const scrollLeft = ref<number>(0);
const textareaWidth = ref<number>(0);

// Style variables to sync with textarea computed styles
const textareaStyles = ref({
  fontFamily: 'monospace',
  fontSize: '12px',
  fontWeight: '400',
  fontStyle: 'normal',
  lineHeight: '17.4px',
  padding: '8px 10px',
});

// Escape HTML utility
const escapeHtml = (value: string): string => {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
};

// Language constructs for tokenizing
const KEYWORDS = new Set(['if', 'else', 'while', 'for', 'in', 'break', 'continue', 'return', 'none', 'None', 'null', 'NULL']);
const CONSTANTS = new Set(['pi', 'PI', 'e', 'E']);
const FUNCTIONS = new Set([
  'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2', 'sinh', 'cosh', 'tanh', 'asinh', 'acosh', 'atanh',
  'abs', 'sqrt', 'ln', 'log', 'exp', 'smin', 'smax', 'tmin', 'tmax', 'tnorm', 'snorm', 'floor', 'ceil',
  'round', 'gamma', 'pow', 'sigm', 'clamp', 'fft', 'ifft', 'angle', 'print', 'print_shape', 'pshp', 'nvl',
  'nan_to_num', 'lerp', 'step', 'smoothstep', 'fract', 'relu', 'softplus', 'gelu', 'sign', 'map', 'ezconvolution',
  'ezconv', 'convolution', 'conv', 'swap', 'permute', 'perm', 'reshape', 'rshp', 'range', 'topk', 'botk', 'pinv',
  'sum', 'mean', 'std', 'var', 'quartile', 'quartil', 'percentile', 'prcnt', 'quantile', 'dot', 'moment', 'erf', 'erfinv', 'any',
  'all', 'edge', 'blur', 'gaussian', 'median', 'mode', 'cumsum', 'cumprod', 'topk_ind', 'topk_indices', 'botk_ind',
  'botk_indices', 'cubic_ease', 'cubic', 'elastic_ease', 'elastic', 'sine_ease', 'sine', 'smootherstep', 'dist',
  'distance', 'remap', 'cossim', 'cosine_similarity', 'count', 'cnt', 'length', 'flatten', 'append', 'get_value',
  'flow_apply', 'batch_shuffle', 'shuffle', 'motion_mask', 'flow_to_image', 'overlay', 'pad', 'cross', 'matmul', 'rife',
  'bnot', 'bitwise_not', 'bitcount', 'popcount', 'popcnt', 'shape', 'band', 'bitwise_and', 'bxor', 'bitwise_xor',
  'bor', 'bitwise_or', 'tensor', 'stack_push', 'stack_pop', 'stack_clear', 'stack_has', 'stack_get', 'timestamp', 'now',
  'sort', 'argsort', 'argmin', 'argmax', 'softmax', 'softmin', 'unique', 'flip', 'cov', 'corr', 'correlation', 'entropy',
  'crop', 'cat', 'concatenate', 'concat', 'float', 'int', 'linspace', 'logspace', 'roll', 'select',
  'noise', 'randn', 'random_normal', 'rand', 'randu', 'random_uniform', 'randc', 'random_cauchy', 'rande',
  'random_exponential', 'randln', 'random_log_normal', 'randb', 'random_bernoulli', 'randp', 'random_poisson', 'randg',
  'random_gamma', 'randbeta', 'random_beta', 'randl', 'random_laplace', 'randgumbel', 'random_gumbel', 'randw',
  'random_weibull', 'randchi2', 'random_chi2', 'randt', 'random_studentt', 'perlin', 'perlin_noise', 'cellular', 'voronoi',
  'worley', 'cellular_noise', 'voronoi_noise', 'plasma', 'turbulence', 'plasma_noise', 'ridged', 'ridged_noise',
  'domain_warp', 'domain_warp_noise',
  'upper', 'lower', 'split', 'join', 'substring', 'substr', 'find', 'trim', 'replace',
  'dilate', 'erode', 'morph_open', 'morph_close',
  'rgb_to_hsv', 'hsv_to_rgb',
  'rgb_to_oklab', 'oklab_to_rgb', 'rgb_to_cielab', 'cielab_to_rgb',
  'int_to_rgb', 'rgb_to_int',
  'where', 'histogram', 'hist', 'flow_mag', 'flow_magnitude', 'flow_ang', 'flow_angle',
  'interpolate_linear', 'interpolate_area', 'interpolate_nearest', 'interpolate_nearest_exact'
]);

const BRACKET_PAIRS: Record<string, string> = { '(': ')', '[': ']', '{': '}' };
const OPENING_BRACKETS = new Set(['(', '[', '{']);
const CLOSING_BRACKETS = new Set([')', ']', '}']);

interface Token {
  type: string;
  value: string;
  depth: number;
}

// Tokenize standard input text
const tokenize = (text: string): Token[] => {
  const tokens: Token[] = [];
  const pattern = /#.*|\/\*[\s\S]*?\*\/|"(?:\\.|[^"\\\r\n])*"|'(?:\\.|[^'\\\r\n])*'|\b\d+(?:\.\d*)?(?:[eE][+-]?\d+)?\b|\B\.\d+(?:[eE][+-]?\d+)?\b|==|!=|>=|<=|<<|>>|->|\+=|-=|\*=|\/=|%=|[+\-*/%^=<>|?:,;()\[\]{}]|\b[a-zA-Z_][a-zA-Z_0-9]*\b|\s+|./g;

  const bracketStack: string[] = [];
  const depthByType: Record<string, number> = { '(': 0, '[': 0, '{': 0 };
  let m;

  while ((m = pattern.exec(text)) !== null) {
    const value = m[0];
    let type = 'text';
    let depth = 0;

    if (value.startsWith('#') || value.startsWith('/*')) {
      type = 'comment';
    } else if (value.startsWith('"') || value.startsWith("'")) {
      type = 'string';
    } else if (OPENING_BRACKETS.has(value)) {
      depth = depthByType[value] || 0;
      depthByType[value] = depth + 1;
      bracketStack.push(value);
      type = 'bracket';
    } else if (CLOSING_BRACKETS.has(value)) {
      if (bracketStack.length) {
        const lastOpen = bracketStack[bracketStack.length - 1];
        if (BRACKET_PAIRS[lastOpen] === value) {
          depth = (depthByType[lastOpen] || 1) - 1;
          depthByType[lastOpen] = depth;
          bracketStack.pop();
        }
      }
      type = 'bracket';
    } else if (/^[+\-*/%^=<>|?:,;]|==|!=|>=|<=|<<|>>|->$/.test(value)) {
      type = 'operator';
    } else if (/^(?:\d+\.\d*|\d+|\.\d+)(?:[eE][+-]?\d+)?$/.test(value)) {
      type = 'number';
    } else if (/^[a-zA-Z_]/.test(value)) {
      if (KEYWORDS.has(value)) type = 'keyword';
      else if (CONSTANTS.has(value)) type = 'constant';
      else if (FUNCTIONS.has(value)) type = 'function';
      else type = 'variable';
    }

    tokens.push({ type, value, depth });
  }
  return tokens;
};

// Generate syntax highlighted HTML
const highlightedHtml = computed(() => {
  return tokenize(modelValue.value)
    .map((t) => {
      if (t.type === 'text') return escapeHtml(t.value);
      if (t.type === 'bracket') {
        const d = t.depth % 6;
        return `<span class="mrmth-token-bracket mrmth-bracket-${d}">${escapeHtml(t.value)}</span>`;
      }
      return `<span class="mrmth-token-${t.type}">${escapeHtml(t.value)}</span>`;
    })
    .join('');
});

// Generate HTML for mirror measurement layer
const measureHtml = computed(() => {
  const lines = modelValue.value.split('\n');
  return lines
    .map((line, idx) => {
      const content = line === '' ? ' ' : line;
      return `<span class="mrmth-ln-marker" data-ln="${idx}"></span>${escapeHtml(content)}`;
    })
    .join('\n');
});

// Line height measurement utility
const getLineHeightPx = (el: HTMLTextAreaElement): number => {
  const style = window.getComputedStyle(el);
  const lh = parseFloat(style.lineHeight);
  if (Number.isFinite(lh) && lh > 0) return lh;

  const probe = document.createElement('span');
  probe.textContent = 'A';
  probe.style.position = 'absolute';
  probe.style.visibility = 'hidden';
  probe.style.fontFamily = style.fontFamily;
  probe.style.fontSize = style.fontSize;
  probe.style.fontWeight = style.fontWeight;
  probe.style.fontStyle = style.fontStyle;
  document.body.appendChild(probe);
  const h = probe.getBoundingClientRect().height || 16;
  probe.remove();
  return h;
};

// Stable delta offset tracker for smoothing
const prevOffset = ref<number>(0);
const stableCount = ref<number>(0);
const locked = ref<boolean>(false);

// Core alignment and line number updates
const refresh = () => {
  const textarea = textareaRef.value;
  const measureEl = measureElRef.value;
  const gutterContent = gutterContentRef.value;
  if (!textarea || !measureEl || !gutterContent) return;

  textareaWidth.value = textarea.clientWidth;

  // Retrieve actual styles from textarea
  const cs = window.getComputedStyle(textarea);
  textareaStyles.value = {
    fontFamily: cs.fontFamily,
    fontSize: cs.fontSize,
    fontWeight: cs.fontWeight,
    fontStyle: cs.fontStyle,
    lineHeight: cs.lineHeight,
    padding: cs.padding,
  };

  const rawLines = modelValue.value.split('\n');
  const lineCount = Math.max(1, rawLines.length);
  const totalHeight = measureEl.offsetHeight;

  const parsedLH = parseFloat(cs.lineHeight);
  const lhPx = Number.isFinite(parsedLH) && parsedLH > 0 ? parsedLH : getLineHeightPx(textarea);

  const newGutterLines: string[] = [];
  for (let i = 0; i < lineCount; i++) {
    const marker = measureEl.querySelector(`[data-ln="${i}"]`) as HTMLElement | null;
    const nextMarker = i < lineCount - 1 ? measureEl.querySelector(`[data-ln="${i + 1}"]`) as HTMLElement | null : null;

    const y0 = marker ? marker.offsetTop : i * lhPx;
    const y1 = nextMarker ? nextMarker.offsetTop : totalHeight;

    const visualLines = Math.max(1, Math.round((y1 - y0) / lhPx));
    newGutterLines.push(String(i + 1));
    for (let j = 1; j < visualLines; j++) {
      newGutterLines.push(' ');
    }
  }
  gutterLines.value = newGutterLines;

  // Perform baseline and transform alignment on next tick
  nextTick(() => {
    const firstMarker = measureEl.querySelector(`[data-ln="0"]`) as HTMLElement | null;
    const gutterFirstLine = gutterContent.firstElementChild as HTMLElement | null;
    if (!firstMarker || !gutterFirstLine) return;

    // ensure probes exist
    let measureProbe = firstMarker.querySelector('.mrmth-baseline-probe') as HTMLElement | null;
    if (!measureProbe) {
      measureProbe = document.createElement('span');
      measureProbe.className = 'mrmth-baseline-probe';
      measureProbe.style.display = 'inline-block';
      measureProbe.style.width = '0px';
      measureProbe.style.height = '0px';
      measureProbe.style.lineHeight = '0';
      measureProbe.style.verticalAlign = 'baseline';
      measureProbe.style.overflow = 'hidden';
      firstMarker.appendChild(measureProbe);
    }

    let gutterProbe = gutterFirstLine.querySelector('.mrmth-baseline-probe') as HTMLElement | null;
    if (!gutterProbe) {
      gutterProbe = document.createElement('span');
      gutterProbe.className = 'mrmth-baseline-probe';
      gutterProbe.style.display = 'inline-block';
      gutterProbe.style.width = '0px';
      gutterProbe.style.height = '0px';
      gutterProbe.style.lineHeight = '0';
      gutterProbe.style.verticalAlign = 'baseline';
      gutterProbe.style.overflow = 'hidden';
      gutterFirstLine.insertAdjacentElement('afterbegin', gutterProbe);
    }

    let baselineDelta = 0;
    try {
      const mProbeRect = measureProbe.getBoundingClientRect();
      const gProbeRect = gutterProbe.getBoundingClientRect();
      const mRect = measureEl.getBoundingClientRect();
      const gRect = gutterContent.getBoundingClientRect();
      const mOffset = mProbeRect.top - mRect.top;
      const gOffset = gProbeRect.top - gRect.top;
      baselineDelta = mOffset - gOffset;
    } catch (e) {
      baselineDelta = firstMarker.offsetTop + measureProbe.offsetTop - (gutterFirstLine.offsetTop + gutterProbe.offsetTop);
    }

    if (!Number.isFinite(baselineDelta)) baselineDelta = prevOffset.value;

    const maxJumpPerFrame = 20;
    if (locked.value) {
      baselineDelta = prevOffset.value;
    } else {
      const jump = baselineDelta - prevOffset.value;
      if (Math.abs(jump) > maxJumpPerFrame) {
        baselineDelta = prevOffset.value + Math.sign(jump) * maxJumpPerFrame;
      }
      if (Math.abs(baselineDelta) > 200) {
        baselineDelta = prevOffset.value;
      }
      const postJump = baselineDelta - prevOffset.value;
      if (Math.abs(postJump) <= 1) stableCount.value++;
      else stableCount.value = 0;

      if (stableCount.value >= 3) locked.value = true;
    }

    prevOffset.value = baselineDelta;

    const halfLineCorrection = lhPx / 2;
    const adjustedBaseline = baselineDelta - halfLineCorrection;

    // Apply translation to gutter
    gutterContent.style.transform = `translateY(${adjustedBaseline - scrollTop.value}px)`;

    // Handle height resizing of the editor component
    const contentHeight = measureEl.offsetHeight || (lhPx * lineCount);
    const parent = wrapperRef.value?.parentElement;
    const parentHeight = parent ? parent.clientHeight : null;
    const minHeight = 170;
    let maxHeight = 600;

    if (parentHeight !== null && parentHeight > 0) {
      maxHeight = Math.max(minHeight, parentHeight - 12);
    }

    const desired = Math.min(Math.max(contentHeight, minHeight), maxHeight);

    // FIX: If containing node is larger than text height (user enlarged the node), fill 100% of parent height
    if (parentHeight && parentHeight > desired + 20) {
      editorHeight.value = '100%';
    } else {
      editorHeight.value = desired + 'px';
    }
  });
};

// Event handlers
const onInput = () => {
  refresh();
};

const onScroll = () => {
  const textarea = textareaRef.value;
  const syntaxLayer = syntaxLayerRef.value;
  const gutterContent = gutterContentRef.value;
  if (!textarea) return;

  scrollTop.value = textarea.scrollTop;
  scrollLeft.value = textarea.scrollLeft;

  if (syntaxLayer) {
    syntaxLayer.scrollTop = textarea.scrollTop;
    syntaxLayer.scrollLeft = textarea.scrollLeft;
  }

  if (gutterContent) {
    const halfLineCorrection = (parseFloat(textareaStyles.value.lineHeight) || 17.4) / 2;
    const adjustedBaseline = prevOffset.value - halfLineCorrection;
    gutterContent.style.transform = `translateY(${adjustedBaseline - textarea.scrollTop}px)`;
  }
};

const onKeyDown = (e: KeyboardEvent) => {
  if (!OPENING_BRACKETS.has(e.key)) return;

  const textarea = textareaRef.value;
  if (!textarea) return;

  const start = textarea.selectionStart;
  const end = textarea.selectionEnd;
  if (start !== end) return;

  const nextChar = modelValue.value[start] ?? '';
  const closing = BRACKET_PAIRS[e.key];
  if (/[a-zA-Z0-9_]/.test(nextChar) || nextChar === closing) return;

  e.preventDefault();
  modelValue.value = `${modelValue.value.slice(0, start)}${e.key}${closing}${modelValue.value.slice(start)}`;
  
  nextTick(() => {
    textarea.selectionStart = textarea.selectionEnd = start + 1;
    refresh();
  });
};

// Computed styles
const sharedTextStyle = computed(() => {
  return {
    fontFamily: textareaStyles.value.fontFamily,
    fontSize: textareaStyles.value.fontSize,
    fontWeight: textareaStyles.value.fontWeight,
    fontStyle: textareaStyles.value.fontStyle,
    lineHeight: textareaStyles.value.lineHeight,
    padding: textareaStyles.value.padding,
    width: textareaWidth.value ? `${textareaWidth.value}px` : '100%',
    boxSizing: 'border-box' as const,
  };
});

const gutterStyle = computed(() => {
  return {
    fontFamily: textareaStyles.value.fontFamily,
    fontSize: textareaStyles.value.fontSize,
    fontWeight: textareaStyles.value.fontWeight,
    fontStyle: textareaStyles.value.fontStyle,
    lineHeight: textareaStyles.value.lineHeight,
    padding: textareaStyles.value.padding,
    boxSizing: 'border-box' as const,
  };
});

const editorStyle = computed(() => {
  return {
    height: editorHeight.value,
  };
});

// Setup observers
let resizeObserver: ResizeObserver | null = null;

onMounted(() => {
  refresh();
  // Ensure refresh also settles after parent and layout rendering
  setTimeout(refresh, 50);
  setTimeout(refresh, 200);

  if (window.ResizeObserver && editorContainerRef.value) {
    resizeObserver = new ResizeObserver(() => {
      refresh();
    });
    resizeObserver.observe(editorContainerRef.value);
  }
});

onBeforeUnmount(() => {
  if (resizeObserver) {
    resizeObserver.disconnect();
  }
});

watch(modelValue, () => {
  refresh();
});
</script>

<style scoped>
.mrmth-editor {
  display: flex;
  align-items: stretch;
  width: 100%;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 8px;
  overflow: hidden;
  background: rgba(0, 0, 0, 0.18);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.15);
  transition: border-color 0.25s ease, box-shadow 0.25s ease;
  font-family: monospace;
}

.mrmth-editor:focus-within {
  border-color: var(--p-primary-color, #4ea658);
  box-shadow: 0 0 0 2px rgba(78, 166, 88, 0.2), inset 0 2px 4px rgba(0, 0, 0, 0.15);
}

.mrmth-gutter {
  padding: 0;
  min-width: 44px;
  text-align: right;
  user-select: none;
  color: #9aa0a6;
  background: rgba(0, 0, 0, 0.35);
  border-right: 1px solid rgba(255, 255, 255, 0.12);
  box-sizing: border-box;
  overflow: hidden;
  position: relative;
}

.mrmth-gutter-content {
  white-space: pre;
  will-change: transform;
}

.mrmth-gutter-line {
  padding: 0 8px;
  display: block;
}

.mrmth-baseline-probe {
  display: inline-block;
  width: 0;
  height: 0;
  line-height: 0;
  overflow: hidden;
}

.mrmth-editor-container {
  position: relative;
  flex: 1;
  min-width: 0;
  height: 100%;
  overflow: hidden;
  background: transparent;
}

.mrmth-measure {
  position: absolute;
  visibility: hidden;
  pointer-events: none;
  inset: 0 auto auto 0;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  word-break: break-word;
  height: auto;
  margin: 0 !important;
}

.mrmth-syntax-layer {
  position: absolute;
  inset: 0;
  z-index: 3;
  pointer-events: none;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  word-break: break-word;
  overflow: hidden;
  opacity: 1;
  margin: 0 !important;
  color: #ecf0f1;
}

.mrmth-script-textarea {
  position: absolute;
  inset: 0;
  z-index: 2;
  border: 0 !important;
  outline: none !important;
  resize: none !important;
  color: transparent !important;
  caret-color: #ffffff !important;
  background: transparent !important;
  mix-blend-mode: normal;
  -webkit-text-fill-color: transparent;
  overflow-y: auto;
  scrollbar-gutter: stable;
  -webkit-overflow-scrolling: touch;
  margin: 0 !important;
}

/* Syntax Token Highlighting */
:deep(.mrmth-token-comment) { color: #7f8c8d; font-style: italic; }
:deep(.mrmth-token-number) { color: #f39c12; }
:deep(.mrmth-token-constant) { color: #f1c40f; font-weight: 500; }
:deep(.mrmth-token-keyword) { color: #e74c3c; font-weight: 500; }
:deep(.mrmth-token-function) { color: #9b59b6; }
:deep(.mrmth-token-variable) { color: #ecf0f1; }
:deep(.mrmth-token-operator) { color: #3498db; }
:deep(.mrmth-token-string) { color: #2ecc71; }
:deep(.mrmth-token-bracket) { font-weight: 700; }

:deep(.mrmth-bracket-0) { color: #ffd700; }
:deep(.mrmth-bracket-1) { color: #da70d6; }
:deep(.mrmth-bracket-2) { color: #87cefa; }
:deep(.mrmth-bracket-3) { color: #98fb98; }
:deep(.mrmth-bracket-4) { color: #ff6347; }
:deep(.mrmth-bracket-5) { color: #ffa500; }
</style>
