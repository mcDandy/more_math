import { app } from "/scripts/app.js";

const NODE_IDS = new Set(["mrmth_ScriptInput"]);
const NODE_NAMES = new Set(["ScriptTextInput"]);
const STYLE_ID = "mrmth-script-line-numbers";

const KEYWORDS = new Set(["if", "else", "while", "for", "in", "break", "continue", "return", "none", "None", "null", "NULL"]);
const CONSTANTS = new Set(["pi", "PI", "e", "E"]);
const FUNCTIONS = new Set([
    "sin", "cos", "tan", "asin", "acos", "atan", "atan2", "sinh", "cosh", "tanh", "asinh", "acosh", "atanh",
    "abs", "sqrt", "ln", "log", "exp", "smin", "smax", "tmin", "tmax", "tnorm", "snorm", "floor", "ceil",
    "round", "gamma", "pow", "sigm", "clamp", "fft", "ifft", "angle", "print", "print_shape", "pshp", "nvl",
    "nan_to_num", "lerp", "step", "smoothstep", "fract", "relu", "softplus", "gelu", "sign", "map", "ezconvolution",
    "ezconv", "convolution", "conv", "swap", "permute", "perm", "reshape", "rshp", "range", "topk", "botk", "pinv",
    "sum", "mean", "std", "var", "quartile", "quartil", "percentile", "prcnt", "quantile", "dot", "moment", "any",
    "all", "edge", "blur", "gaussian", "median", "mode", "cumsum", "cumprod", "topk_ind", "topk_indices", "botk_ind",
    "botk_indices", "cubic_ease", "cubic", "elastic_ease", "elastic", "sine_ease", "sine", "smootherstep", "dist",
    "distance", "remap", "cossim", "cosine_similarity", "count", "cnt", "length", "flatten", "append", "get_value",
    "flow_apply", "batch_shuffle", "shuffle", "motion_mask", "flow_to_image", "overlay", "pad", "cross", "matmul", "rife",
    "bnot", "bitwise_not", "bitcount", "popcount", "popcnt", "shape", "band", "bitwise_and", "bxor", "bitwise_xor",
    "bor", "bitwise_or", "tensor", "stack_push", "stack_pop", "stack_clear", "stack_has", "stack_get", "timestamp",
    "sort", "argsort", "argmin", "argmax", "softmax", "softmin", "unique", "flip", "cov", "crop",
    "noise", "randn", "random_normal", "rand", "randu", "random_uniform", "randc", "random_cauchy", "rande",
    "random_exponential", "randln", "random_log_normal", "randb", "random_bernoulli", "randp", "random_poisson", "randg",
    "random_gamma", "randbeta", "random_beta", "randl", "random_laplace", "randgumbel", "random_gumbel", "randw",
    "random_weibull", "randchi2", "random_chi2", "randt", "random_studentt", "perlin", "perlin_noise", "cellular", "voronoi",
    "worley", "cellular_noise", "voronoi_noise", "plasma", "turbulence", "plasma_noise",
    "upper", "lower", "split", "join", "substring", "substr", "find", "trim", "replace",
    "dilate", "erode", "morph_open", "morph_close",
    "rgb_to_hsv", "hsv_to_rgb"
]);

const BRACKET_PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}'
};
const OPENING_BRACKETS = new Set(['(', '[', '{']);
const CLOSING_BRACKETS = new Set([')', ']', '}']);

function escapeHtml(value) {
    return value.replace(/[&<>"']/g, (ch) => {
        switch (ch) {
            case "&":
                return "&amp;";
            case "<":
                return "&lt;";
            case ">":
                return "&gt;";
            case '"':
                return "&quot;";
            case "'":
                return "&#39;";
            default:
                return ch;
        }
    });
}

function tokenize(text) {
    const tokens = [];
    const pattern = /#.*|\/\*[\s\S]*?\*\/|"(?:\\.|[^"\\\r\n])*"|'(?:\\.|[^'\\\r\n])*'|\b\d+(?:\.\d*)?(?:[eE][+-]?\d+)?\b|\B\.\d+(?:[eE][+-]?\d+)?\b|==|!=|>=|<=|<<|>>|->|[+\-*/%^=<>|?:,;()\[\]{}]|\b[a-zA-Z_][a-zA-Z_0-9]*\b|\s+|./g;
    let match;
    const bracketStack = [];
    const depthByType = { '(': 0, '[': 0, '{': 0 };

    while ((match = pattern.exec(text)) !== null) {
        const value = match[0];
        let type = "text";
        let depth = 0;

        if (value.startsWith("#") || value.startsWith("/*")) {
            type = "comment";
        } else if (value.startsWith('"') || value.startsWith("'")) {
            type = "string";
        } else if (OPENING_BRACKETS.has(value)) {
            depth = depthByType[value];
            depthByType[value]++;
            bracketStack.push(value);
            type = "bracket";
        } else if (CLOSING_BRACKETS.has(value)) {
            if (bracketStack.length > 0) {
                const lastOpen = bracketStack[bracketStack.length - 1];
                if (BRACKET_PAIRS[lastOpen] === value) {
                    // Use depth of bracket type being closed, before decrement
                    depth = depthByType[lastOpen] - 1;
                    depthByType[lastOpen]--;
                    bracketStack.pop();
                } else {
                    // Mismatched closing bracket
                    depth = 0;
                }
            } else {
                // Unmatched closing bracket
                depth = 0;
            }
            type = "bracket";
        } else if (/^[+\-*/%^=<>|?:,;]|==|!=|>=|<=|<<|>>|->$/.test(value)) {
            type = "operator";
        } else if (/^(?:\d+\.\d*|\d+|\.\d+)(?:[eE][+-]?\d+)?$/.test(value)) {
            type = "number";
        } else if (/^[a-zA-Z_]/.test(value)) {
            if (KEYWORDS.has(value)) {
                type = "keyword";
            } else if (CONSTANTS.has(value)) {
                type = "constant";
            } else if (FUNCTIONS.has(value)) {
                type = "function";
            } else {
                type = "variable";
            }
        }
        tokens.push({ type, value, depth });
    }
    return tokens;
}

function renderHighlight(text) {
    const tokens = tokenize(text);
    return tokens
        .map((token) => {
            if (token.type === "text") {
                return escapeHtml(token.value);
            }
            if (token.type === "bracket") {
                const depthClass = token.depth % 6;
                return `<span class="mrmth-token-bracket mrmth-bracket-${depthClass}">${escapeHtml(token.value)}</span>`;
            }
            return `<span class="mrmth-token-${token.type}">${escapeHtml(token.value)}</span>`;
        })
        .join("");
}

function hasScriptInput(nodeData) {
    const input = nodeData?.input || {};
    const required = input.required || {};
    const optional = input.optional || {};
    return Object.prototype.hasOwnProperty.call(required, "script") || Object.prototype.hasOwnProperty.call(optional, "script");
}

function isTargetNode(nodeData) {
    if (!nodeData) {
        return false;
    }
    if (NODE_IDS.has(nodeData.node_id)) {
        return true;
    }
    if (NODE_IDS.has(nodeData.name)) {
        return true;
    }
    if (NODE_NAMES.has(nodeData.name)) {
        return true;
    }
    if (NODE_NAMES.has(nodeData.display_name)) {
        return true;
    }
    return hasScriptInput(nodeData);
}

function ensureStyles() {
    if (document.getElementById(STYLE_ID)) {
        return;
    }

    const style = document.createElement("style");
    style.id = STYLE_ID;
    style.textContent = `
        .mrmth-line-editor {
            display: flex;
            align-items: stretch;
            width: 100%;
            gap: 0;
        }
        .mrmth-line-numbers {
            padding: 6px 8px;
            text-align: right;
            user-select: none;
            color: #9aa0a6;
            background: rgba(0, 0, 0, 0.4);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
            font-family: monospace;
            font-size: 12px;
            line-height: 1.4;
            white-space: pre;
            overflow: hidden;
            box-sizing: border-box;
        }
        .mrmth-line-numbers-content {
            white-space: pre;
        }
        .mrmth-editor-container {
            position: relative;
            flex: 1;
            min-height: 30px;
            overflow: hidden;
        }
        .mrmth-line-input {
            position: relative;
            z-index: 2;
            flex: 1;
            width: 100%;
            height: 100%;
            box-sizing: border-box;
            font-family: monospace;
            line-height: 1.4;
            white-space: pre-wrap;
            word-wrap: break-word;
            resize: none;
            background: transparent;
            color: transparent;
        }
        .mrmth-syntax-layer {
            position: absolute;
            inset: 0;
            margin: 0;
            z-index: 1;
            pointer-events: none;
            white-space: pre-wrap;
            word-wrap: break-word;
            overflow: hidden;
            mix-blend-mode: normal;
            opacity: 1;
        }
        .mrmth-token-comment { color: #7f8c8d; }
        .mrmth-token-number { color: #f39c12; }
        .mrmth-token-constant { color: #f1c40f; }
        .mrmth-token-keyword { color: #e74c3c; }
        .mrmth-token-function { color: #8e44ad; }
        .mrmth-token-variable { color: #ecf0f1; }
        .mrmth-token-operator { color: #95a5a6; }
        .mrmth-token-string { color: #4ea658; }
        .mrmth-token-bracket { font-weight: bold; }
        .mrmth-bracket-0 { color: #ffd700; }
        .mrmth-bracket-1 { color: #da70d6; }
        .mrmth-bracket-2 { color: #87cefa; }
        .mrmth-bracket-3 { color: #98fb98; }
        .mrmth-bracket-4 { color: #ff6347; }
        .mrmth-bracket-5 { color: #ffa500; }
    `;
    document.head.appendChild(style);
}

function measureLineHeight(inputEl) {
    const probe = document.createElement("span");
    const style = getComputedStyle(inputEl);
    probe.style.position = "absolute";
    probe.style.visibility = "hidden";
    probe.style.whiteSpace = "pre";
    probe.style.fontFamily = style.fontFamily;
    probe.style.fontSize = style.fontSize;
    probe.style.fontWeight = style.fontWeight;
    probe.style.fontStyle = style.fontStyle;
    probe.style.lineHeight = style.lineHeight;
    probe.textContent = "A";
    document.body.appendChild(probe);
    const height = probe.getBoundingClientRect().height;
    document.body.removeChild(probe);
    return height;
}

function attachLineNumbers(widget) {
    const inputEl = widget?.inputEl;
    if (!inputEl || inputEl.dataset.mrmthLineNumbers) {
        return false;
    }

    const parent = inputEl.parentElement;
    if (!parent) {
        return false;
    }

    ensureStyles();

    const wrapper = document.createElement("div");
    wrapper.className = "mrmth-line-editor";

    const gutter = document.createElement("div");
    gutter.className = "mrmth-line-numbers";

    const gutterContent = document.createElement("div");
    gutterContent.className = "mrmth-line-numbers-content";

    const editorContainer = document.createElement("div");
    editorContainer.className = "mrmth-editor-container";

    const syntaxLayer = document.createElement("pre");
    syntaxLayer.className = "mrmth-syntax-layer";

    parent.replaceChild(wrapper, inputEl);
    wrapper.appendChild(gutter);
    gutter.appendChild(gutterContent);
    wrapper.appendChild(editorContainer);
    editorContainer.appendChild(syntaxLayer);
    editorContainer.appendChild(inputEl);

    inputEl.classList.add("mrmth-line-input");
    inputEl.dataset.mrmthLineNumbers = "true";

    const inputStyle = getComputedStyle(inputEl);
    const lineHeightPx = measureLineHeight(inputEl);

    const applyAlpha = (color, alpha) => {
        const rgbaMatch = color.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/i);
        if (!rgbaMatch) {
            return `rgba(0, 0, 0, ${alpha})`;
        }
        const r = Number(rgbaMatch[1]);
        const g = Number(rgbaMatch[2]);
        const b = Number(rgbaMatch[3]);
        return `rgba(${r}, ${g}, ${b}, ${alpha})`;
    };

    const baseBackground = inputStyle.backgroundColor || "rgba(0, 0, 0, 0.4)";
    const overlayBackground = applyAlpha(baseBackground, 0.4);

    syntaxLayer.style.height = "100%";
    syntaxLayer.style.background = "transparent";
    inputEl.style.height = "100%";
    inputEl.style.background = overlayBackground;

    gutter.style.fontFamily = inputStyle.fontFamily;
    gutter.style.fontSize = inputStyle.fontSize;
    gutter.style.lineHeight = inputStyle.lineHeight;
    gutter.style.paddingTop = inputStyle.paddingTop;
    gutter.style.paddingBottom = inputStyle.paddingBottom;

    syntaxLayer.style.fontFamily = inputStyle.fontFamily;
    syntaxLayer.style.fontSize = inputStyle.fontSize;
    syntaxLayer.style.lineHeight = inputStyle.lineHeight;
    syntaxLayer.style.padding = `${inputStyle.paddingTop} ${inputStyle.paddingRight} ${inputStyle.paddingBottom} ${inputStyle.paddingLeft}`;
    syntaxLayer.style.width = "100%";
    syntaxLayer.style.boxSizing = "border-box";
    syntaxLayer.style.overflowY = "hidden";

    inputEl.style.background = overlayBackground;
    inputEl.style.color = "transparent";
    inputEl.style.caretColor = "#ffffff";
    inputEl.style.mixBlendMode = "lighten";

    const updateNumbers = () => {
        const rawLines = inputEl.value.split("\n");
        const textLineCount = Math.max(1, rawLines.length);

        const gutterLines = [];

        // Sync syntaxLayer width to match inputEl's actual content width
        const scrollbarWidth = inputEl.offsetWidth - inputEl.clientWidth;
        syntaxLayer.style.width = `calc(100% - ${scrollbarWidth}px)`;

        // Create a temporary clone
        const measureClone = syntaxLayer.cloneNode(false);
        measureClone.style.position = "absolute";
        measureClone.style.visibility = "hidden";
        measureClone.style.width = syntaxLayer.style.width;
        measureClone.style.height = "auto";
        syntaxLayer.parentElement.appendChild(measureClone);

        // Build content with simple marker at start of each line
        let html = "";
        for (let i = 0; i < textLineCount; i++) {
            html += `<span class="lm" data-ln="${i}"></span>`;
            html += renderHighlight(rawLines[i] || " ");
            if (i < textLineCount - 1) {
                html += "\n";
            }
        }
        measureClone.innerHTML = html;

        // Simply read offsetTop of each marker
        const totalHeight = measureClone.offsetHeight;

        for (let i = 0; i < textLineCount; i++) {
            const marker = measureClone.querySelector(`[data-ln="${i}"]`);
            const nextMarker = i < textLineCount - 1 ? measureClone.querySelector(`[data-ln="${i + 1}"]`) : null;

            const currentY = marker ? marker.offsetTop : i * lineHeightPx;
            const nextY = nextMarker ? nextMarker.offsetTop : totalHeight;

            const heightDiff = nextY - currentY;
            const visualLines = Math.max(1, Math.round(heightDiff / lineHeightPx));

            gutterLines.push(String(i + 1));

            for (let j = 1; j < visualLines; j++) {
                gutterLines.push(" ");
            }
        }

        measureClone.remove();

        gutterContent.textContent = gutterLines.join("\n");

        gutter.style.height = `${inputEl.clientHeight}px`;
        gutterContent.style.transform = `translateY(${-inputEl.scrollTop}px)`;
    };

    const updateHighlight = () => {
        const sourceText = inputEl.value.endsWith("\n") ? `${inputEl.value} ` : inputEl.value;
        const highlighted = renderHighlight(sourceText);
        syntaxLayer.innerHTML = highlighted;
        syntaxLayer.scrollTop = inputEl.scrollTop;
        syntaxLayer.scrollLeft = inputEl.scrollLeft;
    };

    const handleBracketAutoClose = (e) => {
        const key = e.key;
        if (!OPENING_BRACKETS.has(key)) {
            return;
        }

        const selectionStart = inputEl.selectionStart;
        const selectionEnd = inputEl.selectionEnd;

        if (selectionStart !== selectionEnd) {
            return;
        }

        const text = inputEl.value;
        const charAfter = text[selectionStart] || '';

        // Only prevent auto-close if the MATCHING closing bracket is after cursor
        const closingBracket = BRACKET_PAIRS[key];
        const isMatchingClosingBracket = charAfter === closingBracket;

        // Prevent auto-close if next char is alphanumeric or a matching closing bracket
        if (/[a-zA-Z0-9_]/.test(charAfter) || isMatchingClosingBracket) {
            return;
        }

        e.preventDefault();

        const before = text.substring(0, selectionStart);
        const after = text.substring(selectionStart);
        inputEl.value = before + key + closingBracket + after;
        inputEl.selectionStart = inputEl.selectionEnd = selectionStart + 1;

        updateNumbers();
        updateHighlight();

        const event = new Event('input', { bubbles: true });
        inputEl.dispatchEvent(event);
    };

    inputEl.addEventListener("keydown", handleBracketAutoClose);

    inputEl.addEventListener("input", () => {
        updateNumbers();
        updateHighlight();
    });
    inputEl.addEventListener("scroll", () => {
        gutterContent.style.transform = `translateY(${-inputEl.scrollTop}px)`;
        syntaxLayer.scrollTop = inputEl.scrollTop;
        syntaxLayer.scrollLeft = inputEl.scrollLeft;
    });

    if (window.ResizeObserver) {
        const resizeObserver = new ResizeObserver(() => {
            updateNumbers();
            updateHighlight();
        });
        resizeObserver.observe(inputEl);
    }

    requestAnimationFrame(() => {
        updateNumbers();
        updateHighlight();
    });

    return true;
}

function attachLineNumbersWithRetry(node) {
    const widget = node.widgets?.find((w) => w.name === "script");
    if (attachLineNumbers(widget)) {
        return;
    }

    requestAnimationFrame(() => {
        const retryWidget = node.widgets?.find((w) => w.name === "script");
        attachLineNumbers(retryWidget);
    });
}

app.registerExtension({
    name: "mrmth.ScriptTextInput.LineNumbers",
    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (!isTargetNode(nodeData)) {
            return;
        }

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            onNodeCreated?.apply(this, arguments);
            attachLineNumbersWithRetry(this);
        };

        const onConfigure = nodeType.prototype.onConfigure;
        nodeType.prototype.onConfigure = function () {
            onConfigure?.apply(this, arguments);
            attachLineNumbersWithRetry(this);
        };
    },
});
