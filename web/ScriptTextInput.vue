<template>
  <div
    class="mrmth-editor mrmth-editor-v2"
    data-mrmth-script-widget="vue"
  >
    <!-- Gutter / Line Numbers -->
    <div class="mrmth-gutter">
      <div class="mrmth-gutter-content" :style="gutterStyle">{{ gutterText }}</div>
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
        spellcheck="false"
        autocapitalize="off"
        autocomplete="off"
        autocorrect="off"
        placeholder="Enter your script here..."
        @scroll="onScroll"
        @blur="cursor = -2"
      ></textarea>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount, nextTick, watch } from 'vue';
import { app } from '/scripts/app.js';
import { attachAutocomplete, escapeHtml, handleEditingKey, renderHighlight } from './autocomplete.js';

const modelValue = defineModel<string>({ default: '' });

const editorContainerRef = ref<HTMLDivElement | null>(null);
const measureElRef = ref<HTMLPreElement | null>(null);
const syntaxLayerRef = ref<HTMLPreElement | null>(null);
const textareaRef = ref<HTMLTextAreaElement | null>(null);

const gutterText = ref('1');
const scrollTop = ref(0);
// Collapsed caret position while focused, used to outline the bracket pair at the cursor.
const cursor = ref(-2);

// Layout-relevant textarea styles, copied so overlay, mirror and textarea wrap identically.
const textStyle = ref<Record<string, string>>({});
const textWidth = ref(0);
const gutterPaddingTop = ref('0px');

const highlightedHtml = computed(() => renderHighlight(modelValue.value, cursor.value));

// Empty lines need content to produce a line box in the mirror.
const measureHtml = computed(() =>
  modelValue.value
    .split('\n')
    .map((line) => `<span class="mrmth-ln-marker"></span>${escapeHtml(line || ' ')}`)
    .join('\n')
);

const sharedTextStyle = computed(() => ({
  ...textStyle.value,
  width: textWidth.value ? `${textWidth.value}px` : '100%',
}));

const gutterStyle = computed(() => ({
  fontFamily: textStyle.value.fontFamily,
  fontSize: textStyle.value.fontSize,
  lineHeight: textStyle.value.lineHeight,
  paddingTop: gutterPaddingTop.value,
  transform: `translateY(${-scrollTop.value}px)`,
}));

const updateLineNumbers = () => {
  const measureEl = measureElRef.value;
  if (!measureEl) return;

  const lineHeightPx = parseFloat(textStyle.value.lineHeight);
  const markers = measureEl.querySelectorAll<HTMLElement>('.mrmth-ln-marker');
  const contentBottom = measureEl.clientHeight - parseFloat(getComputedStyle(measureEl).paddingBottom);
  const lines: string[] = [];
  for (let i = 0; i < markers.length; i++) {
    const y0 = markers[i].offsetTop;
    const y1 = i + 1 < markers.length ? markers[i + 1].offsetTop : contentBottom;
    lines.push(String(i + 1));
    const visualLines = Math.max(1, Math.round((y1 - y0) / lineHeightPx));
    for (let j = 1; j < visualLines; j++) lines.push('');
  }
  gutterText.value = lines.join('\n');
};

const refresh = () => {
  const textarea = textareaRef.value;
  if (!textarea) return;

  const cs = window.getComputedStyle(textarea);
  textStyle.value = {
    fontFamily: cs.fontFamily,
    fontSize: cs.fontSize,
    fontWeight: cs.fontWeight,
    fontStyle: cs.fontStyle,
    letterSpacing: cs.letterSpacing,
    lineHeight: cs.lineHeight,
    tabSize: cs.tabSize,
    padding: `${cs.paddingTop} ${cs.paddingRight} ${cs.paddingBottom} ${cs.paddingLeft}`,
    borderWidth: `${cs.borderTopWidth} ${cs.borderRightWidth} ${cs.borderBottomWidth} ${cs.borderLeftWidth}`,
  };
  // Same border-box width as the textarea minus its scrollbar.
  textWidth.value = textarea.clientWidth + parseFloat(cs.borderLeftWidth) + parseFloat(cs.borderRightWidth);
  gutterPaddingTop.value = `${parseFloat(cs.paddingTop) + parseFloat(cs.borderTopWidth)}px`;

  // Measure once the mirror has re-rendered with the new text and styles.
  nextTick(updateLineNumbers);
};

const syncScroll = () => {
  const textarea = textareaRef.value;
  const syntaxLayer = syntaxLayerRef.value;
  if (!textarea || !syntaxLayer) return;
  syntaxLayer.scrollTop = textarea.scrollTop;
  syntaxLayer.scrollLeft = textarea.scrollLeft;
};

const onScroll = () => {
  scrollTop.value = textareaRef.value?.scrollTop ?? 0;
  syncScroll();
};

const onKeyDown = (e: KeyboardEvent) => {
  if (textareaRef.value && handleEditingKey(textareaRef.value, e)) e.preventDefault();
};

const onSelectionChange = () => {
  const textarea = textareaRef.value;
  if (!textarea || document.activeElement !== textarea) return;
  cursor.value = textarea.selectionStart === textarea.selectionEnd ? textarea.selectionStart : -2;
};

let resizeObserver: ResizeObserver | null = null;
let autocompleteController: { destroy: () => void } | null = null;

onMounted(() => {
  const textarea = textareaRef.value!;
  // Autocomplete first: its keydown handler must run before the editing keys.
  autocompleteController = attachAutocomplete(textarea, (id) => app.extensionManager?.setting?.get(id));
  textarea.addEventListener('keydown', onKeyDown);
  document.addEventListener('selectionchange', onSelectionChange);

  resizeObserver = new ResizeObserver(refresh);
  resizeObserver.observe(editorContainerRef.value!);
  refresh();
});

onBeforeUnmount(() => {
  autocompleteController?.destroy();
  resizeObserver?.disconnect();
  textareaRef.value?.removeEventListener('keydown', onKeyDown);
  document.removeEventListener('selectionchange', onSelectionChange);
});

watch(modelValue, refresh);
// Replacing the overlay's content can reset its scroll position.
watch(highlightedHtml, syncScroll, { flush: 'post' });
</script>

<style scoped>
.mrmth-editor {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
  min-height: 0;
  box-sizing: border-box;
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
  position: absolute;
  inset: 0 auto 0 0;
  padding: 0;
  width: 44px;
  min-height: 0;
  text-align: right;
  user-select: none;
  color: #9aa0a6;
  background: rgba(0, 0, 0, 0.35);
  border-right: 1px solid rgba(255, 255, 255, 0.12);
  box-sizing: border-box;
  overflow: hidden;
}

.mrmth-gutter-content {
  padding: 0 8px;
  white-space: pre;
  will-change: transform;
}

.mrmth-editor-container {
  position: absolute;
  inset: 0 0 0 44px;
  min-width: 0;
  min-height: 0;
  overflow: hidden;
  background: transparent;
}

.mrmth-measure,
.mrmth-syntax-layer {
  margin: 0 !important;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  word-break: break-word;
  box-sizing: border-box;
  border-style: solid;
  border-color: transparent;
}

.mrmth-measure {
  position: absolute;
  visibility: hidden;
  pointer-events: none;
  inset: 0 auto auto 0;
  height: auto;
}

.mrmth-syntax-layer {
  position: absolute;
  inset: 0;
  z-index: 3;
  pointer-events: none;
  overflow: hidden;
  color: #ecf0f1;
}

/* Extra scroll room so the last line can scroll as far as in the textarea */
.mrmth-syntax-layer::after {
  content: "";
  display: block;
  height: 1em;
}

.mrmth-script-textarea {
  position: absolute;
  inset: 0;
  z-index: 2;
  line-height: 1.45;
  border: 0 !important;
  outline: none !important;
  resize: none !important;
  color: transparent !important;
  caret-color: #ffffff !important;
  background: transparent !important;
  -webkit-text-fill-color: transparent;
  overflow-y: auto;
  scrollbar-gutter: stable;
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

:deep(.mrmth-bracket-unmatched) {
  color: #ff4d4d;
  text-decoration: underline wavy #ff4d4d;
}

:deep(.mrmth-bracket-active) {
  outline: 1px solid rgba(255, 255, 255, 0.6);
  border-radius: 2px;
  background: rgba(255, 255, 255, 0.12);
}
</style>
