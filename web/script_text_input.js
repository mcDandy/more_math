import { app } from "/scripts/app.js";

const NODE_IDS = new Set(["mrmth_ScriptInput"]);
const NODE_NAMES = new Set(["Script input", "ScriptTextInput", "STEW"]);
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
    "worley", "cellular_noise", "voronoi_noise", "plasma", "turbulence", "plasma_noise"
]);

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
    const pattern = /#.*|\/\*[\s\S]*?\*\/|\b\d+(?:\.\d*)?(?:[eE][+-]?\d+)?\b|\B\.\d+(?:[eE][+-]?\d+)?\b|==|!=|>=|<=|<<|>>|->|[+\-*/%^=<>|?:,;()\[\]{}]|\b[a-zA-Z_][a-zA-Z_0-9]*\b|\s+|./g;
    let match;
    while ((match = pattern.exec(text)) !== null) {
        const value = match[0];
        let type = "text";
        if (value.startsWith("#") || value.startsWith("/*")) {
            type = "comment";
        } else if (/^[+\-*/%^=<>|?:,;()\[\]{}]|==|!=|>=|<=|<<|>>|->$/.test(value)) {
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
        tokens.push({ type, value });
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
    if (NODE_IDS.has(nodeData.node_id) || NODE_IDS.has(nodeData.name)) {
        return true;
    }
    if (NODE_NAMES.has(nodeData.name) || NODE_NAMES.has(nodeData.display_name)) {
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
            background: rgba(0, 0, 0, 0.2);
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
            min-height: 120px;
        }
        .mrmth-line-input {
            position: relative;
            z-index: 3;
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
            color: rgba(255, 255, 255, 1.0);
            caret-color: var(--mrmth-caret-color, #ffffff) !important;
            text-shadow: none;
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
            color: var(--mrmth-text-color, #e0e0e0);
            background: transparent;
        }
        .mrmth-token-comment { color: #7f8c8d; }
        .mrmth-token-number { color: #f39c12; }
        .mrmth-token-constant { color: #f1c40f; }
        .mrmth-token-keyword { color: #e74c3c; }
        .mrmth-token-function { color: #8e44ad; }
        .mrmth-token-variable { color: #ecf0f1; }
        .mrmth-token-operator { color: #95a5a6; }
    `;
    document.head.appendChild(style);
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
    editorContainer.style.minHeight = inputStyle.height;
    const inputTextColor = inputStyle.color || "#e0e0e0";
    syntaxLayer.style.fontFamily = inputStyle.fontFamily;
    syntaxLayer.style.fontSize = inputStyle.fontSize;
    syntaxLayer.style.lineHeight = inputStyle.lineHeight;
    syntaxLayer.style.padding = `${inputStyle.paddingTop} ${inputStyle.paddingRight} ${inputStyle.paddingBottom} ${inputStyle.paddingLeft}`;
    syntaxLayer.style.color = inputTextColor;
    editorContainer.style.setProperty("--mrmth-text-color", inputTextColor);
    editorContainer.style.setProperty("--mrmth-caret-color", inputTextColor || "#ffffff");
    inputEl.style.setProperty("caret-color", inputTextColor || "#ffffff", "important");
    inputEl.style.background = "transparent";
    inputEl.style.color = "rgba(255, 255, 255, 0.02)";
    inputEl.style.textShadow = "none";

    const updateNumbers = () => {
        const lineCount = Math.max(1, inputEl.value.split("\n").length);
        gutterContent.textContent = Array.from({ length: lineCount }, (_, i) => String(i + 1)).join("\n");
        gutter.style.height = `${editorContainer.clientHeight}px`;
        gutterContent.style.transform = `translateY(${-inputEl.scrollTop}px)`;
    };

    const updateHighlight = () => {
        const highlighted = renderHighlight(inputEl.value);
        syntaxLayer.innerHTML = highlighted || "\n";
        syntaxLayer.scrollTop = inputEl.scrollTop;
        syntaxLayer.scrollLeft = inputEl.scrollLeft;
    };

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

    updateNumbers();
    updateHighlight();
    return true;
}

function attachLineNumbersWithRetry(node) {
    const widget = node.widgets?.find((w) => w.name === "script");
    if (!widget) {
        return;
    }

    if (attachLineNumbers(widget)) {
        return;
    }

    requestAnimationFrame(() => {
        attachLineNumbersWithRetry(node);
    });
}

app.registerExtension({
    name: "mrmth.ScriptTextInput.SyntaxHighlight",
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
