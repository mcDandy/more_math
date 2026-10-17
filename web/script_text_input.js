import { app } from "/scripts/app.js";
import { attachAutocomplete, escapeHtml, handleEditingKey, renderHighlight } from "./autocomplete.js";

const STYLE_ID = "mrmth-script-line-numbers-unified";

// `widget.element` of every mrmth_ScriptInput script widget; only these get enhanced.
const scriptTextareas = new WeakSet();
const editors = new WeakMap();

if (!window.__mrmthScriptInputUnifiedInit) {
    window.__mrmthScriptInputUnifiedInit = true;

    function ensureStyles() {
        if (document.getElementById(STYLE_ID)) return;

        const style = document.createElement("style");
        style.id = STYLE_ID;
        style.textContent = `
            .mrmth-editor:not(.mrmth-editor-v2) {
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
                min-width: 44px;
                text-align: right;
                user-select: none;
                color: #9aa0a6;
                background: rgba(0,0,0,0.35);
                border-right: 1px solid rgba(255,255,255,0.12);
                box-sizing: border-box;
                overflow: hidden;
            }

            .mrmth-gutter-content {
                padding: 0 6px;
                white-space: pre;
                will-change: transform;
            }

            .mrmth-editor:not(.mrmth-editor-v2) .mrmth-editor-container {
                position: relative;
                flex: 1;
                min-width: 0;
                min-height: 170px;
                overflow: hidden;
                background: transparent;
            }

            .mrmth-editor.mrmth-editor-v2 {
                position: relative;
                display: block;
                width: 100%;
                height: 100%;
                min-height: 0;
                box-sizing: border-box;
                border: 1px solid rgba(255,255,255,0.14);
                border-radius: 10px;
                overflow: hidden;
                background: rgba(0,0,0,0.18);
            }

            .mrmth-editor-v2 .mrmth-gutter {
                position: absolute;
                inset: 0 auto 0 0;
                width: 44px;
            }

            .mrmth-editor-v2 .mrmth-editor-container {
                position: absolute;
                inset: 0 0 0 44px;
                min-width: 0;
                min-height: 0;
            }

            .mrmth-syntax-layer,
            .mrmth-measure {
                margin: 0 !important;
                white-space: pre-wrap;
                overflow-wrap: anywhere;
                word-break: break-word;
                box-sizing: border-box;
                border-style: solid;
                border-color: transparent;
            }

            .mrmth-syntax-layer {
                position: absolute;
                inset: 0;
                z-index: 3;
                pointer-events: none;
                overflow: hidden;
            }

            /* Extra scroll room so the last line can scroll as far as in the textarea */
            .mrmth-syntax-layer::after {
                content: "";
                display: block;
                height: 1em;
            }

            .mrmth-syntax-layer span {
                white-space: pre-wrap;
                overflow-wrap: anywhere;
                word-break: break-word;
                hyphens: none;
            }

            .mrmth-measure {
                position: absolute;
                visibility: hidden;
                pointer-events: none;
                inset: 0 auto auto 0;
                height: auto;
            }

            .mrmth-script-textarea {
                position: absolute;
                inset: 0;
                z-index: 2;
                line-height: 1.45;

                color: transparent !important;
                caret-color: #ffffff !important;
                background: transparent !important;
                -webkit-text-fill-color: transparent;

                /* Reserve scrollbar space to avoid layout jumps when it appears */
                overflow-y: auto;
                scrollbar-gutter: stable;
            }

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
            .mrmth-bracket-unmatched {
                color: #ff4d4d;
                text-decoration: underline wavy #ff4d4d;
            }
            .mrmth-bracket-active {
                outline: 1px solid rgba(255,255,255,0.6);
                border-radius: 2px;
                background: rgba(255,255,255,0.12);
            }
        `;
        document.head.appendChild(style);
    }

    function hideNearbyScriptLabels(textarea) {
        const root = textarea.closest("div, section, article") ?? textarea.parentElement;
        if (!root) return;
        const labels = root.querySelectorAll("label, .label, .input-label, .property_name, .v-label, span, div");
        for (const el of labels) {
            if (el.dataset.mrmthHiddenLabel === "1") continue;
            if ((el.textContent || "").trim().toLowerCase() === "script") {
                el.style.display = "none";
                el.dataset.mrmthHiddenLabel = "1";
            }
        }
    }

    // Copy everything that affects text layout so overlay, mirror and textarea wrap identically.
    function syncTextStyle(cs, el) {
        el.style.fontFamily = cs.fontFamily;
        el.style.fontSize = cs.fontSize;
        el.style.fontWeight = cs.fontWeight;
        el.style.fontStyle = cs.fontStyle;
        el.style.letterSpacing = cs.letterSpacing;
        el.style.lineHeight = cs.lineHeight;
        el.style.tabSize = cs.tabSize;
        el.style.padding = `${cs.paddingTop} ${cs.paddingRight} ${cs.paddingBottom} ${cs.paddingLeft}`;
        el.style.borderWidth = `${cs.borderTopWidth} ${cs.borderRightWidth} ${cs.borderBottomWidth} ${cs.borderLeftWidth}`;
    }

    function updateLineNumbers(textarea, gutterContent, measureEl, lineHeightPx) {
        const lines = textarea.value.split("\n");
        // Empty lines need content to produce a line box in the mirror.
        measureEl.innerHTML = lines.map((l) => `<span class="mrmth-ln-marker"></span>${escapeHtml(l || " ")}`).join("\n");

        const markers = measureEl.querySelectorAll(".mrmth-ln-marker");
        const contentBottom = measureEl.clientHeight - parseFloat(getComputedStyle(measureEl).paddingBottom);
        const gutterLines = [];
        for (let i = 0; i < markers.length; i++) {
            const y0 = markers[i].offsetTop;
            const y1 = i + 1 < markers.length ? markers[i + 1].offsetTop : contentBottom;
            gutterLines.push(String(i + 1));
            const visualLines = Math.max(1, Math.round((y1 - y0) / lineHeightPx));
            for (let j = 1; j < visualLines; j++) gutterLines.push("");
        }
        gutterContent.textContent = gutterLines.join("\n");
    }

    function findBoundingAncestor(el) {
        let node = el.parentElement;
        while (node && node !== document.body && node !== document.documentElement) {
            const cs = getComputedStyle(node);
            // An ancestor with an explicit height, max-height or constrained overflow bounds the editor.
            if ((cs.height && cs.height !== "auto") || (cs.maxHeight && cs.maxHeight !== "none") || (cs.overflowY && cs.overflowY !== "visible")) {
                return node;
            }
            node = node.parentElement;
        }
        return document.documentElement;
    }

    function attachToTextarea(textarea) {
        if (!scriptTextareas.has(textarea)) return;

        // The frontend re-mounts widget.element into a fresh container (e.g. after
        // subgraph navigation); move the editor along with it.
        const existing = editors.get(textarea);
        if (existing) {
            if (!existing.wrapper.contains(textarea)) {
                textarea.replaceWith(existing.wrapper);
                existing.container.appendChild(textarea);
                requestAnimationFrame(existing.refresh);
            }
            return;
        }

        const parent = textarea.parentElement;
        if (!parent) return;

        const isVueWidget = !!(app.ui?.settings?.getSettingValue?.("Comfy.VueNodes.Enabled") || document.getElementById("vue-app"));

        ensureStyles();
        hideNearbyScriptLabels(textarea);

        const wrapper = document.createElement("div");
        wrapper.className = "mrmth-editor";
        if (isVueWidget) wrapper.classList.add("mrmth-editor-v2");

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
        textarea.spellcheck = false;
        textarea.autocapitalize = "off";
        textarea.autocomplete = "off";
        textarea.autocorrect = "off";

        // Autocomplete first: its keydown handler must run before the editing keys.
        const autocomplete = attachAutocomplete(textarea);
        textarea.addEventListener("keydown", (e) => {
            if (handleEditingKey(textarea, e)) e.preventDefault();
        });

        const syncScroll = () => {
            gutterContent.style.transform = `translateY(${-textarea.scrollTop}px)`;
            syntaxLayer.scrollTop = textarea.scrollTop;
            syntaxLayer.scrollLeft = textarea.scrollLeft;
        };

        const updateHighlight = () => {
            const focused = document.activeElement === textarea && textarea.selectionStart === textarea.selectionEnd;
            syntaxLayer.innerHTML = renderHighlight(textarea.value, focused ? textarea.selectionStart : -2);
            syncScroll();
        };

        const refresh = () => {
            const cs = getComputedStyle(textarea);
            syncTextStyle(cs, syntaxLayer);
            syncTextStyle(cs, measureEl);
            gutterContent.style.fontFamily = cs.fontFamily;
            gutterContent.style.fontSize = cs.fontSize;
            gutterContent.style.lineHeight = cs.lineHeight;
            gutterContent.style.paddingTop = `${parseFloat(cs.paddingTop) + parseFloat(cs.borderTopWidth)}px`;

            // Same border-box width as the textarea minus its scrollbar, so text wraps identically.
            const widthPx = textarea.clientWidth + parseFloat(cs.borderLeftWidth) + parseFloat(cs.borderRightWidth);
            measureEl.style.width = `${widthPx}px`;
            syntaxLayer.style.width = `${widthPx}px`;

            const lineHeightPx = parseFloat(cs.lineHeight);
            updateLineNumbers(textarea, gutterContent, measureEl, lineHeightPx);
            updateHighlight();

            if (isVueWidget) {
                wrapper.style.minHeight = "0";
                wrapper.style.height = "100%";
                editorContainer.style.minHeight = "0";
                editorContainer.style.height = "100%";
                return;
            }

            // Reactive height: size wrapper and editor container to content, clamped to parent's height
            const contentHeight = measureEl.offsetHeight || (lineHeightPx * Math.max(1, textarea.value.split("\n").length));
            const bounding = findBoundingAncestor(wrapper) || parent || document.documentElement;
            const parentHeight = bounding && bounding.clientHeight ? bounding.clientHeight : null;
            const minHeight = 60;
            let maxHeight = 600;

            if (parentHeight !== null) {
                maxHeight = Math.max(60, parentHeight - 12);

                // If the viewport is the bound, prefer a higher static ancestor so the editor doesn't grow with itself.
                if (bounding === document.documentElement) {
                    const staticAncestor = findBoundingAncestor(bounding);
                    if (staticAncestor && staticAncestor !== document.documentElement) {
                        maxHeight = Math.max(60, staticAncestor.clientHeight - 12);
                    }
                }
            }

            const desired = Math.min(Math.max(contentHeight, minHeight), maxHeight);

            wrapper.style.minHeight = "170px";
            // A node enlarged beyond the content height lets the editor fill it; otherwise match content size.
            if (parentHeight && parentHeight > desired + 20) {
                wrapper.style.height = "100%";
                editorContainer.style.height = "100%";
            } else {
                wrapper.style.height = desired + "px";
                editorContainer.style.height = desired + "px";
            }
        };

        const onSelectionChange = () => {
            if (document.activeElement === textarea) updateHighlight();
        };

        textarea.addEventListener("input", refresh);
        textarea.addEventListener("scroll", syncScroll);
        textarea.addEventListener("blur", updateHighlight);
        document.addEventListener("selectionchange", onSelectionChange);

        const ro = new ResizeObserver(refresh);
        ro.observe(editorContainer);

        editors.set(textarea, {
            wrapper,
            container: editorContainer,
            refresh,
            destroy() {
                ro.disconnect();
                autocomplete.destroy();
                document.removeEventListener("selectionchange", onSelectionChange);
            },
        });

        requestAnimationFrame(refresh);
    }

    app.registerExtension({
        name: "mrmth.ScriptTextInput.Unified",
        nodeCreated(node, app) {
            if (node.comfyClass !== "mrmth_ScriptInput" && node.type !== "mrmth_ScriptInput") return;
            const widget = node.widgets?.find(w => w.name === "script");
            if (!(widget?.element instanceof HTMLTextAreaElement)) return;

            const isVue = app.ui?.settings?.getSettingValue?.("Comfy.VueNodes.Enabled") || document.getElementById("vue-app");
            // No Vue component is registered for this type, so Nodes 2.0 mounts the
            // DOM widget's own textarea, which is then enhanced like in the classic UI.
            if (isVue) widget.type = "scriptinput";

            const textarea = widget.element;
            scriptTextareas.add(textarea);
            if (textarea.isConnected) attachToTextarea(textarea);

            // Loading a workflow sets the value without an input event.
            const onConfigure = node.onConfigure;
            node.onConfigure = function () {
                const r = onConfigure?.apply(this, arguments);
                const editor = editors.get(textarea);
                if (editor) requestAnimationFrame(editor.refresh);
                return r;
            };

            const onRemoved = node.onRemoved;
            node.onRemoved = function () {
                editors.get(textarea)?.destroy();
                editors.delete(textarea);
                return onRemoved?.apply(this, arguments);
            };
        },
        async setup() {
            // Script widgets are mounted into the DOM after nodeCreated; enhance them once they appear.
            const observer = new MutationObserver((mutations) => {
                for (const m of mutations) {
                    for (const node of m.addedNodes) {
                        if (!(node instanceof Element)) continue;
                        if (node instanceof HTMLTextAreaElement) attachToTextarea(node);
                        else node.querySelectorAll("textarea").forEach(attachToTextarea);
                    }
                }
            });

            observer.observe(document.body, { childList: true, subtree: true });
        },
    });
}
