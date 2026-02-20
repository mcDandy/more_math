import { app } from "/scripts/app.js";

const NODE_IDS = new Set(["mrmth_ScriptInput"]);
const NODE_NAMES = new Set(["ScriptTextInput"]);
const STYLE_ID = "mrmth-script-line-numbers";

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

    parent.replaceChild(wrapper, inputEl);
    wrapper.appendChild(gutter);
    gutter.appendChild(gutterContent);
    wrapper.appendChild(inputEl);

    inputEl.classList.add("mrmth-line-input");
    inputEl.dataset.mrmthLineNumbers = "true";

    const inputStyle = getComputedStyle(inputEl);
    gutter.style.fontFamily = inputStyle.fontFamily;
    gutter.style.fontSize = inputStyle.fontSize;
    gutter.style.lineHeight = inputStyle.lineHeight;
    gutter.style.paddingTop = inputStyle.paddingTop;
    gutter.style.paddingBottom = inputStyle.paddingBottom;

    const updateNumbers = () => {
        const lineCount = Math.max(1, inputEl.value.split("\n").length);
        gutterContent.textContent = Array.from({ length: lineCount }, (_, i) => String(i + 1)).join("\n");
        gutter.style.height = `${inputEl.clientHeight}px`;
        gutterContent.style.transform = `translateY(${-inputEl.scrollTop}px)`;
    };

    inputEl.addEventListener("input", updateNumbers);
    inputEl.addEventListener("scroll", () => {
        gutterContent.style.transform = `translateY(${-inputEl.scrollTop}px)`;
    });

    if (window.ResizeObserver) {
        const resizeObserver = new ResizeObserver(() => updateNumbers());
        resizeObserver.observe(inputEl);
    }

    requestAnimationFrame(updateNumbers);
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
