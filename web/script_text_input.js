import { app } from "/scripts/app.js";

const STYLE_ID = "mrmth-script-line-numbers-unified";

function escapeHtml(value) {
    return value
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

if (!window.__mrmthScriptInputUnifiedInit) {
    window.__mrmthScriptInputUnifiedInit = true;

    function ensureStyles() {
        if (document.getElementById(STYLE_ID)) return;

        const style = document.createElement("style");
        style.id = STYLE_ID;
        style.textContent = `
            .mrmth-editor {
                display: flex;
                align-items: stretch;
                width: 100%;
                min-height: 170px;
                border: 1px solid rgba(255,255,255,0.14);
                border-radius: 10px;
                overflow: hidden;
                background: rgba(0,0,0,0.18);
            }

            .mrmth-gutter {
                padding: 8px 10px;
                min-width: 44px;
                text-align: right;
                user-select: none;
                color: #9aa0a6;
                background: rgba(0,0,0,0.35);
                border-right: 1px solid rgba(255,255,255,0.12);
                font-family: monospace;
                font-size: 12px;
                line-height: 1.45;
                white-space: pre;
                box-sizing: border-box;
                overflow: hidden;
            }
            .mrmth-syntax-layer::after {
                content: "";
                display: block;
                height: 1em;
            }
            .mrmth-gutter-content {
                white-space: pre;
                will-change: transform;
            }

           .mrmth-editor-container {
             position: relative;
             flex: 1;
             min-width: 0;
             min-height: 170px;
             overflow: hidden;
             background: transparent; /* ⬅️ DŮLEŽITÉ */
           }

            .mrmth-syntax-layer {
              position: absolute;
              inset: 0;
              z-index: 3;              /* ⬅️ výš než textarea */
              pointer-events: none;
              white-space: pre-wrap;
              overflow-wrap: anywhere;
              word-break: break-word;
              box-sizing: border-box;
              overflow: hidden;
              opacity: 1;
            }


            .mrmth-script-textarea {
              position: absolute;       /* ⬅️ ne relative */
              inset: 0;
              z-index: 2;

              color: transparent !important;
              caret-color: #ffffff !important;
              background: transparent !important;

              mix-blend-mode: normal;   /* ⬅️ ZRUŠ lighten */
              -webkit-text-fill-color: transparent;

              /* Reserve scrollbar space to avoid layout jumps when it appears */
              overflow-y: auto;
              scrollbar-gutter: stable;
              -webkit-overflow-scrolling: touch;
            }

            .mrmth-measure {
                position: absolute;
                visibility: hidden;
                pointer-events: none;
                inset: 0 auto auto 0;
                white-space: pre-wrap;
                overflow-wrap: anywhere;
                word-break: break-word;
                box-sizing: border-box;
                height: auto;
            }

.mrmth-syntax-layer,
.mrmth-measure {
    margin: 0 !important;
}

.mrmth-gutter-line { display: block; }
.mrmth-baseline-probe { display:inline-block; width:0; height:0; line-height:0; overflow:hidden; }
.mrmth-gutter-line { padding: 0 6px; }


            .mrmth-token-comment { color: #7f8c8d; }
            .mrmth-token-number { color: #f39c12; }
            .mrmth-token-constant { color: #f1c40f; }
            .mrmth-token-keyword { color: #e74c3c; }
            .mrmth-token-function { color: #8e44ad; }
            .mrmth-token-variable { color: #ecf0f1; }
            .mrmth-token-operator { color: #95a5a6; }
            .mrmth-token-string { color: #4ea658; }
            .mrmth-token-bracket { font-weight: 700; }
            .mrmth-bracket-0 { color: #ffd700; }
            .mrmth-bracket-1 { color: #da70d6; }
            .mrmth-bracket-2 { color: #87cefa; }
            .mrmth-bracket-3 { color: #98fb98; }
            .mrmth-bracket-4 { color: #ff6347; }
            .mrmth-bracket-5 { color: #ffa500; }
        `;
        document.head.appendChild(style);
    }

    function hasNearbyScriptLabel(el) {
        const root = el.closest("div, section, article") ?? el.parentElement;
        if (!root) return false;
        const candidates = root.querySelectorAll("label, .label, .input-label, .property_name, .v-label, span, div");
        for (const n of candidates) {
            const t = (n.textContent || "").trim().toLowerCase();
            if (t === "script") return true;
        }
        return false;
    }

    function isLikelyScriptTextarea(el) {
        if (!(el instanceof HTMLTextAreaElement)) return false;
        if (el.dataset.mrmthEnhanced === "1") return false;

        const attrs = [
            el.name,
            el.id,
            el.getAttribute("data-name"),
            el.getAttribute("aria-label"),
            el.getAttribute("placeholder"),
        ]
            .filter(Boolean)
            .join(" ")
            .toLowerCase();

        return attrs.includes("script") || hasNearbyScriptLabel(el);
    }

    function hideNearbyScriptLabels(textarea) {
        const root = textarea.closest("div, section, article") ?? textarea.parentElement;
        if (!root) return;
        const labels = root.querySelectorAll("label, .label, .input-label, .property_name, .v-label, span, div");
        for (const el of labels) {
            if (el.dataset.mrmthHiddenLabel === "1") continue;
            const t = (el.textContent || "").trim().toLowerCase();
            if (t === "script") {
                el.style.display = "none";
                el.dataset.mrmthHiddenLabel = "1";
            }
        }
    }

    function addBracketAutoClose(textarea) {
        const pairs = { "(": ")", "[": "]", "{": "}" };
        const opening = new Set(Object.keys(pairs));

        textarea.addEventListener("keydown", (e) => {
            if (!opening.has(e.key)) return;

            const start = textarea.selectionStart;
            const end = textarea.selectionEnd;
            if (start !== end) return;

            const nextChar = textarea.value[start] ?? "";
            const closing = pairs[e.key];
            if (/[a-zA-Z0-9_]/.test(nextChar) || nextChar === closing) return;

            e.preventDefault();
            textarea.value = `${textarea.value.slice(0, start)}${e.key}${closing}${textarea.value.slice(start)}`;
            textarea.selectionStart = textarea.selectionEnd = start + 1;
            textarea.dispatchEvent(new Event("input", { bubbles: true }));
        });
    }

    function getLineHeightPx(textarea) {
        const style = getComputedStyle(textarea);
        const lh = parseFloat(style.lineHeight);
        if (Number.isFinite(lh) && lh > 0) return lh;

        const probe = document.createElement("span");
        probe.textContent = "A";
        probe.style.position = "absolute";
        probe.style.visibility = "hidden";
        probe.style.fontFamily = style.fontFamily;
        probe.style.fontSize = style.fontSize;
        probe.style.fontWeight = style.fontWeight;
        probe.style.fontStyle = style.fontStyle;
        document.body.appendChild(probe);
        const h = probe.getBoundingClientRect().height || 16;
        probe.remove();
        return h;
    }

    function buildMeasureHtml(lines) {
        let html = "";
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i] === "" ? " " : lines[i];
            html += `<span class="mrmth-ln-marker" data-ln="${i}"></span>${escapeHtml(line)}`;
            if (i < lines.length - 1) html += "\n";
        }
        return html;
    }

    function updateNumbersWrapped(textarea, gutterContent, measureEl, lineHeightPx) {
        const rawLines = textarea.value.split("\n");
        const lineCount = Math.max(1, rawLines.length);

        // Use clientWidth directly for mirror width to avoid rewrap when scrollbar appears/disappears
        const widthPx = textarea.clientWidth;

        const cs = getComputedStyle(textarea);
        measureEl.style.fontFamily = cs.fontFamily;
        measureEl.style.fontSize = cs.fontSize;
        measureEl.style.fontWeight = cs.fontWeight;
        measureEl.style.fontStyle = cs.fontStyle;
        measureEl.style.lineHeight = cs.lineHeight;
        measureEl.style.padding = cs.padding;
        measureEl.style.width = `${widthPx}px`;

        measureEl.innerHTML = buildMeasureHtml(rawLines);
        const totalHeight = measureEl.offsetHeight;

        const gutterLines = [];
        for (let i = 0; i < lineCount; i++) {
            const marker = measureEl.querySelector(`[data-ln="${i}"]`);
            const nextMarker = i < lineCount - 1 ? measureEl.querySelector(`[data-ln="${i + 1}"]`) : null;

            const y0 = marker ? marker.offsetTop : i * lineHeightPx;
            const y1 = nextMarker ? nextMarker.offsetTop : totalHeight;

            const visualLines = Math.max(1, Math.round((y1 - y0) / lineHeightPx));
            gutterLines.push(String(i + 1));
            for (let j = 1; j < visualLines; j++) gutterLines.push(" ");
        }

        // Render gutter lines as elements so we can measure baseline correctly
        gutterContent.innerHTML = gutterLines.map(l => `<div class="mrmth-gutter-line">${escapeHtml(l)}</div>`).join("");
        // stable baseline alignment using offsetTop sums (measure marker + probe) to avoid viewport jitter
        const firstMarker = measureEl.querySelector(`[data-ln="0"]`);
        const gutterFirstLine = gutterContent.firstElementChild;

        // ensure probes exist
        let measureProbe = firstMarker ? firstMarker.querySelector('.mrmth-baseline-probe') : null;
        if (!measureProbe && firstMarker) {
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

        let gutterProbe = gutterFirstLine ? gutterFirstLine.querySelector('.mrmth-baseline-probe') : null;
        if (!gutterProbe && gutterFirstLine) {
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

        // Prefer baseline positions computed relative to each container to avoid global jumps
        let baselineDelta;
        try {
            if (measureProbe && gutterProbe) {
                const mProbeRect = measureProbe.getBoundingClientRect();
                const gProbeRect = gutterProbe.getBoundingClientRect();
                const mRect = measureEl.getBoundingClientRect();
                const gRect = gutterContent.getBoundingClientRect();
                // probe offsets relative to their own containers
                const mOffset = mProbeRect.top - mRect.top;
                const gOffset = gProbeRect.top - gRect.top;
                baselineDelta = mOffset - gOffset;
            } else {
                const measureBaseline = (firstMarker ? firstMarker.offsetTop : 0) + (measureProbe ? measureProbe.offsetTop : 0);
                const gutterBaseline = (gutterFirstLine ? gutterFirstLine.offsetTop : 0) + (gutterProbe ? gutterProbe.offsetTop : 0);
                baselineDelta = measureBaseline - gutterBaseline;
            }
        } catch (e) {
            // fallback to previous offsetTop-based method
            baselineDelta = (firstMarker ? firstMarker.offsetTop : 0) + (measureProbe ? measureProbe.offsetTop : 0) - ((gutterFirstLine ? gutterFirstLine.offsetTop : 0) + (gutterProbe ? gutterProbe.offsetTop : 0));
        }

        // If gutterBaseline couldn't be measured for some reason, fall back to marker offset
        if (!gutterFirstLine) baselineDelta = (firstMarker ? firstMarker.offsetTop : 0) + (measureProbe ? measureProbe.offsetTop : 0);

        // Clamp and smooth extreme jumps to avoid the gutter flying away on transient layout changes
        const prevOffset = parseFloat(gutterContent.dataset.mrmthOffset || "0");
        let stableCount = parseInt(gutterContent.dataset.mrmthStableCount || "0", 10) || 0;
        const locked = gutterContent.dataset.mrmthLocked === "1";
        const maxJumpPerFrame = 20; // px

        if (locked) {
            // keep previous locked offset
            baselineDelta = prevOffset;
        } else {
            if (!Number.isFinite(baselineDelta)) baselineDelta = prevOffset;
            const jump = baselineDelta - prevOffset;
            if (Math.abs(jump) > maxJumpPerFrame) baselineDelta = prevOffset + Math.sign(jump) * maxJumpPerFrame;
            // absolute sanity clamp
            if (Math.abs(baselineDelta) > 200) baselineDelta = prevOffset;

            const postJump = baselineDelta - prevOffset;
            if (Math.abs(postJump) <= 1) stableCount++; else stableCount = 0;
            gutterContent.dataset.mrmthStableCount = String(stableCount);
            if (stableCount >= 3) gutterContent.dataset.mrmthLocked = "1";
        }

        // Keep gutter padding in sync with textarea to match vertical origin across node variants
        gutterContent.style.padding = cs.padding || '0';
        // Prefer computed CSS line-height when available, otherwise fall back to measured px
        const parsedLH = parseFloat(cs.lineHeight);
        gutterContent.style.lineHeight = Number.isFinite(parsedLH) && parsedLH > 0 ? cs.lineHeight : `${lineHeightPx}px`;
        gutterContent.style.boxSizing = 'border-box';
        gutterContent.style.fontFamily = cs.fontFamily;
        gutterContent.style.fontSize = cs.fontSize;
        gutterContent.style.fontWeight = cs.fontWeight;
        gutterContent.style.fontStyle = cs.fontStyle;

        if (window.__mrmthGutterDebug) {
            const textareaRect = textarea.getBoundingClientRect();
            const measureRect = measureEl.getBoundingClientRect();
            const gutterRect = gutterContent.getBoundingClientRect();
            const firstMarkerTop = firstMarker ? firstMarker.offsetTop : null;
            const measureProbeTop = measureProbe ? measureProbe.offsetTop : null;
            const gutterFirstLineTop = gutterFirstLine ? gutterFirstLine.offsetTop : null;
            const gutterProbeTop = gutterProbe ? gutterProbe.offsetTop : null;
            const computedTranslate = baselineDelta - textarea.scrollTop;
            console.log("mrmth-gutter-debug", {
                textareaRect,
                measureRect,
                gutterRect,
                lineHeightPx,
                lineCount,
                widthPx,
                totalHeight,
                firstMarkerTop,
                measureProbeTop,
                gutterFirstLineTop,
                gutterProbeTop,
                baselineDelta,
                computedTranslate,
                prevOffset,
                stableCount,
                locked
            });
        }

        // Apply half-line correction: shift gutter up by half the line height so numbers align with text baseline
        const parsedLHFinal = parseFloat(cs.lineHeight);
        const lineHUsedFinal = Number.isFinite(parsedLHFinal) && parsedLHFinal > 0 ? parsedLHFinal : lineHeightPx;
        const halfLineCorrection = lineHUsedFinal / 2;
        const adjustedBaseline = baselineDelta - halfLineCorrection;

        // Apply transform on next frame to avoid layout thrash
        gutterContent.dataset.mrmthOffset = String(adjustedBaseline);
        requestAnimationFrame(() => {
            gutterContent.style.transform = `translateY(${adjustedBaseline - textarea.scrollTop}px)`;
        });
    }

    function attachToTextarea(textarea) {
        if (!isLikelyScriptTextarea(textarea)) return;
        if (textarea.closest(".mrmth-editor")) {
            textarea.dataset.mrmthEnhanced = "1";
            return;
        }

        const parent = textarea.parentElement;
        if (!parent) return;

        ensureStyles();
        hideNearbyScriptLabels(textarea);

        const wrapper = document.createElement("div");
        wrapper.className = "mrmth-editor";

        const gutter = document.createElement("div");
        gutter.className = "mrmth-gutter";

        const gutterContent = document.createElement("div");
        gutterContent.className = "mrmth-gutter-content";
        gutter.appendChild(gutterContent);

        const editorContainer = document.createElement("div");
        editorContainer.className = "mrmth-editor-container";

        const measureEl = document.createElement("pre");
        measureEl.className = "mrmth-measure";

        const syntaxLayer = document.createElement("pre");
        syntaxLayer.className = "mrmth-syntax-layer";

        parent.replaceChild(wrapper, textarea);
        wrapper.appendChild(gutter);
        wrapper.appendChild(editorContainer);
        editorContainer.appendChild(measureEl);
        editorContainer.appendChild(syntaxLayer);
        editorContainer.appendChild(textarea);

        textarea.classList.add("mrmth-script-textarea");
        textarea.dataset.mrmthEnhanced = "1";
        textarea.spellcheck = false;
        textarea.autocapitalize = "off";
        textarea.autocomplete = "off";
        textarea.autocorrect = "off";

        addBracketAutoClose(textarea);
        const cs = getComputedStyle(textarea);
        syntaxLayer.style.fontFamily = cs.fontFamily;
        syntaxLayer.style.fontSize = cs.fontSize;
        syntaxLayer.style.fontWeight = cs.fontWeight;
        syntaxLayer.style.fontStyle = cs.fontStyle;
        syntaxLayer.style.lineHeight = cs.lineHeight;
        syntaxLayer.style.padding = cs.padding;
        measureEl.style.fontFamily = cs.fontFamily;
        measureEl.style.fontSize = cs.fontSize;
        measureEl.style.fontWeight = cs.fontWeight;
        measureEl.style.fontStyle = cs.fontStyle;
        measureEl.style.lineHeight = cs.lineHeight;
        measureEl.style.padding = cs.padding;
        gutterContent.style.fontFamily = cs.fontFamily;
        gutterContent.style.fontSize = cs.fontSize;
        gutterContent.style.fontWeight = cs.fontWeight;
        gutterContent.style.fontStyle = cs.fontStyle;
        gutterContent.style.padding = cs.padding;
        gutterContent.style.boxSizing = 'border-box';
        gutterContent.style.margin = '0';
        gutterContent.style.whiteSpace = 'pre';
        gutterContent.style.lineHeight = cs.lineHeight;

        const lineHeightPx = getLineHeightPx(textarea);
        const refresh = () => {
            updateNumbersWrapped(textarea, gutterContent, measureEl, lineHeightPx);
            updateHighlight(textarea, syntaxLayer);
        };

        // Force initial measurement again after a short delay to allow different node wrappers to settle
        setTimeout(refresh, 50);
        setTimeout(refresh, 200);

        textarea.addEventListener("input", refresh);
        textarea.addEventListener("scroll", () => {
            const base = parseFloat(gutterContent.dataset.mrmthOffset) || 0;
            gutterContent.style.transform = `translateY(${base - textarea.scrollTop}px)`;
            syntaxLayer.scrollTop = textarea.scrollTop;
            syntaxLayer.scrollLeft = textarea.scrollLeft;
        });

        // Also keep gutter stable on mouse enter/leave which previously caused jumps
        gutter.addEventListener('mouseenter', () => requestAnimationFrame(refresh));
        gutter.addEventListener('mouseleave', () => requestAnimationFrame(refresh));

        if (window.ResizeObserver) {
            const ro = new ResizeObserver(refresh);
            ro.observe(textarea);
        }

        requestAnimationFrame(refresh);
    }
    function updateHighlight(textarea, syntaxLayer) {
        syntaxLayer.innerHTML = renderHighlight(textarea.value);

        syntaxLayer.scrollTop = textarea.scrollTop;
        syntaxLayer.scrollLeft = textarea.scrollLeft;
    }

    function scan(root = document) {
        root.querySelectorAll("textarea").forEach(attachToTextarea);
    }

    app.registerExtension({
        name: "mrmth.ScriptTextInput.Unified",
        async setup() {
            scan(document);

            const observer = new MutationObserver((mutations) => {
                for (const m of mutations) {
                    for (const node of m.addedNodes) {
                        if (!(node instanceof Element)) continue;
                        if (node.matches?.("textarea")) attachToTextarea(node);
                        scan(node);
                    }
                }
            });

            observer.observe(document.body, { childList: true, subtree: true });
        },
    });
}

const KEYWORDS = new Set(["if", "else", "while", "for", "in", "break", "continue", "return", "none", "None", "null", "NULL"]);
const CONSTANTS = new Set(["pi", "PI", "e", "E"]);
const FUNCTIONS = new Set([
    "sin", "cos", "tan", "asin", "acos", "atan", "atan2", "sinh", "cosh", "tanh", "asinh", "acosh", "atanh",
    "abs", "sqrt", "ln", "log", "exp", "smin", "smax", "tmin", "tmax", "tnorm", "snorm", "floor", "ceil",
    "round", "gamma", "pow", "sigm", "clamp", "fft", "ifft", "angle", "print", "print_shape", "pshp", "nvl",
    "nan_to_num", "lerp", "step", "smoothstep", "fract", "relu", "softplus", "gelu", "sign", "map", "ezconvolution",
    "ezconv", "convolution", "conv", "swap", "permute", "perm", "reshape", "rshp", "range", "topk", "botk", "pinv",
    "sum", "mean", "std", "var", "quartile", "quartil", "percentile", "prcnt", "quantile", "dot", "moment", "erf", "erfinv", "any",
    "all", "edge", "blur", "gaussian", "median", "mode", "cumsum", "cumprod", "topk_ind", "topk_indices", "botk_ind",
    "botk_indices", "cubic_ease", "cubic", "elastic_ease", "elastic", "sine_ease", "sine", "smootherstep", "dist",
    "distance", "remap", "cossim", "cosine_similarity", "count", "cnt", "length", "flatten", "append", "get_value",
    "flow_apply", "batch_shuffle", "shuffle", "motion_mask", "flow_to_image", "overlay", "pad", "cross", "matmul", "rife",
    "bnot", "bitwise_not", "bitcount", "popcount", "popcnt", "shape", "band", "bitwise_and", "bxor", "bitwise_xor",
    "bor", "bitwise_or", "tensor", "stack_push", "stack_pop", "stack_clear", "stack_has", "stack_get", "timestamp", "now",
    "sort", "argsort", "argmin", "argmax", "softmax", "softmin", "unique", "flip", "cov", "corr", "correlation", "entropy",
    "crop", "cat", "concatenate", "concat", "float", "int", "linspace", "logspace", "roll", "select",
    "noise", "randn", "random_normal", "rand", "randu", "random_uniform", "randc", "random_cauchy", "rande",
    "random_exponential", "randln", "random_log_normal", "randb", "random_bernoulli", "randp", "random_poisson", "randg",
    "random_gamma", "randbeta", "random_beta", "randl", "random_laplace", "randgumbel", "random_gumbel", "randw",
    "random_weibull", "randchi2", "random_chi2", "randt", "random_studentt", "perlin", "perlin_noise", "cellular", "voronoi",
    "worley", "cellular_noise", "voronoi_noise", "plasma", "turbulence", "plasma_noise", "ridged", "ridged_noise",
    "domain_warp", "domain_warp_noise",
    "upper", "lower", "split", "join", "substring", "substr", "find", "trim", "replace",
    "dilate", "erode", "morph_open", "morph_close",
    "rgb_to_hsv", "hsv_to_rgb",
    "rgb_to_oklab", "oklab_to_rgb", "rgb_to_cielab", "cielab_to_rgb",
    "int_to_rgb", "rgb_to_int",
    "where", "histogram", "hist", "flow_mag", "flow_magnitude", "flow_ang", "flow_angle",
    "interpolate_linear", "interpolate_area", "interpolate_nearest", "interpolate_nearest_exact"]);


const BRACKET_PAIRS = { "(": ")", "[": "]", "{": "}" };
const OPENING_BRACKETS = new Set(["(", "[", "{"]);
const CLOSING_BRACKETS = new Set([")", "]", "}"]);

function tokenize(text) {
    const tokens = [];
    const pattern = /#.*|\/\*[\s\S]*?\*\/|"(?:\\.|[^"\\\r\n])*"|'(?:\\.|[^'\\\r\n])*'|\b\d+(?:\.\d*)?(?:[eE][+-]?\d+)?\b|\B\.\d+(?:[eE][+-]?\d+)?\b|==|!=|>=|<=|<<|>>|->|\+=|-=|\*=|\/=|%=|[+\-*/%^=<>|?:,;()\[\]{}]|\b[a-zA-Z_][a-zA-Z_0-9]*\b|\s+|./g;

    const bracketStack = [];
    const depthByType = { "(": 0, "[": 0, "{": 0 };
    let m;

    while ((m = pattern.exec(text)) !== null) {
        const value = m[0];
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
            if (bracketStack.length) {
                const lastOpen = bracketStack[bracketStack.length - 1];
                if (BRACKET_PAIRS[lastOpen] === value) {
                    depth = depthByType[lastOpen] - 1;
                    depthByType[lastOpen]--;
                    bracketStack.pop();
                }
            }
            type = "bracket";
        } else if (/^[+\-*/%^=<>|?:,;]|==|!=|>=|<=|<<|>>|->$/.test(value)) {
            type = "operator";
        } else if (/^(?:\d+\.\d*|\d+|\.\d+)(?:[eE][+-]?\d+)?$/.test(value)) {
            type = "number";
        } else if (/^[a-zA-Z_]/.test(value)) {
            if (KEYWORDS.has(value)) type = "keyword";
            else if (CONSTANTS.has(value)) type = "constant";
            else if (FUNCTIONS.has(value)) type = "function";
            else type = "variable";
        }

        tokens.push({ type, value, depth });
    }
    return tokens;
}

function renderHighlight(text) {
    return tokenize(text).map((t) => {
        if (t.type === "text") return escapeHtml(t.value);
        if (t.type === "bracket") {
            const d = t.depth % 6;
            return `<span class="mrmth-token-bracket mrmth-bracket-${d}">${escapeHtml(t.value)}</span>`;
        }
        return `<span class="mrmth-token-${t.type}">${escapeHtml(t.value)}</span>`;
    }).join("");
}