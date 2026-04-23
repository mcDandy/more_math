import { app } from "/scripts/app.js";

const STYLE_ID = "mrmth-script-line-numbers-unified";

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
            }

            .mrmth-script-textarea {
                display: block;
                width: 100% !important;
                height: 100% !important;
                min-height: 170px !important;
                margin: 0 !important;
                border: 0 !important;
                outline: none !important;
                resize: vertical !important;
                box-sizing: border-box !important;

                font-family: monospace !important;
                font-size: 12px !important;
                line-height: 1.45 !important;
                padding: 8px 10px !important;

                white-space: pre-wrap !important;
                overflow-wrap: anywhere !important;
                word-break: break-word !important;
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
        `;
        document.head.appendChild(style);
    }

    function escapeHtml(value) {
        return value
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#39;");
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

        const scrollbarWidth = textarea.offsetWidth - textarea.clientWidth;
        const widthPx = Math.max(0, textarea.clientWidth - scrollbarWidth);

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

        gutterContent.textContent = gutterLines.join("\n");
        gutterContent.style.transform = `translateY(${-textarea.scrollTop}px)`;
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

        parent.replaceChild(wrapper, textarea);
        wrapper.appendChild(gutter);
        wrapper.appendChild(editorContainer);
        editorContainer.appendChild(measureEl);
        editorContainer.appendChild(textarea);

        textarea.classList.add("mrmth-script-textarea");
        textarea.dataset.mrmthEnhanced = "1";
        textarea.spellcheck = false;
        textarea.autocapitalize = "off";
        textarea.autocomplete = "off";
        textarea.autocorrect = "off";

        addBracketAutoClose(textarea);
        const lineHeightPx = getLineHeightPx(textarea);

        const refresh = () => updateNumbersWrapped(textarea, gutterContent, measureEl, lineHeightPx);

        textarea.addEventListener("input", refresh);
        textarea.addEventListener("scroll", refresh);

        if (window.ResizeObserver) {
            const ro = new ResizeObserver(refresh);
            ro.observe(textarea);
        }

        requestAnimationFrame(refresh);
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