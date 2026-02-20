import { app } from "/scripts/app.js";

const NODE_IDS = new Set(["mrmth_ScriptInput"]);
const NODE_NAMES = new Set(["Audio -> Spectrogram", "ScriptTextInput", "STEW"]);
const STYLE_ID = "mrmth-script-line-numbers";
const ACE_SCRIPT_SRC = "/extensions/more_math/ace/ace.js";
let aceLoader = null;

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
        .mrmth-line-input {
            flex: 1;
            font-family: monospace;
            line-height: 1.4;
        }
        .mrmth-ace-editor {
            width: 100%;
            min-height: 120px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 4px;
        }
    `;
    document.head.appendChild(style);
}

function loadAce() {
    if (window.ace) {
        return Promise.resolve(window.ace);
    }
    if (aceLoader) {
        return aceLoader;
    }

    aceLoader = new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = ACE_SCRIPT_SRC;
        script.async = true;
        script.onload = () => resolve(window.ace);
        script.onerror = () => reject(new Error("Failed to load Ace editor"));
        document.head.appendChild(script);
    });

    return aceLoader;
}

function attachAceEditor(widget) {
    const inputEl = widget?.inputEl;
    if (!inputEl) {
        return false;
    }

    if (widget.mrmthAceEditor) {
        if (widget.value !== undefined && widget.mrmthAceEditor.getValue() !== widget.value) {
            widget.mrmthAceEditor.setValue(String(widget.value), -1);
        }
        return true;
    }

    const parent = inputEl.parentElement;
    if (!parent) {
        return false;
    }

    ensureStyles();
    const inputStyle = getComputedStyle(inputEl);
    const parentStyle = getComputedStyle(parent);

    inputEl.style.display = "none";

    const editorEl = document.createElement("div");
    editorEl.className = "mrmth-ace-editor";
    editorEl.style.height = `${inputEl.offsetHeight}px`;
    editorEl.style.background = inputStyle.backgroundColor;
    editorEl.style.color = inputStyle.color;
    editorEl.style.borderColor = inputStyle.borderColor || parentStyle.borderColor;
    editorEl.style.borderRadius = inputStyle.borderRadius || parentStyle.borderRadius;
    editorEl.style.fontFamily = inputStyle.fontFamily;
    editorEl.style.fontSize = inputStyle.fontSize;
    editorEl.style.lineHeight = inputStyle.lineHeight;
    editorEl.style.letterSpacing = inputStyle.letterSpacing;
    parent.appendChild(editorEl);

    const aceEditor = window.ace.edit(editorEl, {
        showLineNumbers: true,
        showGutter: true,
        wrap: true,
        useWorker: false,
    });

    if (inputStyle.fontFamily) {
        aceEditor.setOption("fontFamily", inputStyle.fontFamily);
    }
    const fontSize = parseFloat(inputStyle.fontSize);
    const lineHeightPx = parseFloat(inputStyle.lineHeight);
    if (Number.isFinite(fontSize)) {
        aceEditor.setOption("fontSize", fontSize);
    }
    if (Number.isFinite(lineHeightPx) && Number.isFinite(fontSize) && fontSize > 0) {
        aceEditor.setOption("lineHeight", lineHeightPx / fontSize);
    }

    const paddingLeft = parseFloat(inputStyle.paddingLeft);
    const paddingRight = parseFloat(inputStyle.paddingRight);
    if (Number.isFinite(paddingLeft)) {
        aceEditor.renderer.setPadding(paddingLeft, Number.isFinite(paddingRight) ? paddingRight : paddingLeft);
    }

    const themeBackground = inputStyle.backgroundColor || parentStyle.backgroundColor;
    const themeForeground = inputStyle.color || parentStyle.color;
    const gutterBackground = parentStyle.backgroundColor || themeBackground;
    const gutterForeground = parentStyle.color || themeForeground;

    aceEditor.renderer.setStyle(`
        .ace_editor {
            background: ${themeBackground} !important;
            color: ${themeForeground} !important;
        }
        .ace_scroller {
            background: ${themeBackground} !important;
        }
        .ace_gutter {
            background: ${gutterBackground} !important;
            color: ${gutterForeground} !important;
        }
        .ace_gutter-layer {
            background: ${gutterBackground} !important;
        }
        .ace_gutter-cell {
            background: ${gutterBackground} !important;
            color: ${gutterForeground} !important;
        }
        .ace_gutter-active-line {
            background: ${themeBackground} !important;
        }
        .ace_cursor {
            color: ${themeForeground} !important;
        }
    `);

    aceEditor.renderer.updateFontSize();
    aceEditor.renderer.onResize(true);

    aceEditor.setValue(String(widget.value ?? inputEl.value ?? ""), -1);
    aceEditor.on("change", () => {
        const value = aceEditor.getValue();
        widget.value = value;
        inputEl.value = value;
    });

    if (window.ResizeObserver) {
        const resizeObserver = new ResizeObserver(() => {
            editorEl.style.height = `${inputEl.offsetHeight}px`;
            aceEditor.resize();
        });
        resizeObserver.observe(inputEl);
    }

    widget.mrmthAceEditor = aceEditor;
    return true;
}

function attachLineNumbersWithRetry(node) {
    const widget = node.widgets?.find((w) => w.name === "script");
    if (!widget) {
        return;
    }

    loadAce()
        .then(() => attachAceEditor(widget))
        .catch(() => attachLineNumbers(widget));

    requestAnimationFrame(() => {
        if (widget.mrmthAceEditor) {
            return;
        }
        loadAce()
            .then(() => attachAceEditor(widget))
            .catch(() => attachLineNumbers(widget));
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
