import { app } from "/scripts/app.js";

const STYLE_ID = "mrmth-script-line-numbers-v2";
const BRACKET_PAIRS = { "(": ")", "[": "]", "{": "}" };
const OPENING_BRACKETS = new Set(["(", "[", "{"]);

function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    const style = document.createElement("style");
    style.id = STYLE_ID;
    style.textContent = `
        .mrmth-v2-editor { display:flex; width:100%; min-height:160px; border:1px solid rgba(255,255,255,.12); border-radius:8px; overflow:hidden; }
        .mrmth-v2-gutter { padding:8px 10px; min-width:40px; text-align:right; user-select:none; color:#9aa0a6; background:rgba(0,0,0,.35); border-right:1px solid rgba(255,255,255,.12); font-family:monospace; font-size:12px; line-height:1.45; white-space:pre; box-sizing:border-box; }
        .mrmth-v2-textarea { flex:1; min-height:160px !important; border:0 !important; outline:none !important; resize:vertical !important; font-family:monospace !important; font-size:12px !important; line-height:1.45 !important; padding:8px 10px !important; box-sizing:border-box !important; }
    `;
    document.head.appendChild(style);
}

function hasNearbyScriptLabel(el) {
    const container = el.closest("div, section, article");
    if (!container) return false;

    // text labels around the textarea
    const candidates = container.querySelectorAll("label, .label, .input-label, .property_name, span, div");
    for (const n of candidates) {
        const t = (n.textContent || "").trim().toLowerCase();
        if (t === "script") return true;
    }
    return false;
}

function isLikelyScriptTextarea(el) {
    if (!(el instanceof HTMLTextAreaElement)) return false;
    if (el.dataset.mrmthV2Script === "1") return false;

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

    // accept either direct attribute match OR nearby label
    return attrs.includes("script") || hasNearbyScriptLabel(el);
}

function updateGutter(textarea, gutter) {
    const lineCount = Math.max(1, textarea.value.split("\n").length);
    gutter.textContent = Array.from({ length: lineCount }, (_, i) => String(i + 1)).join("\n");
    gutter.style.transform = `translateY(${-textarea.scrollTop}px)`;
}

function addBracketAutoClose(textarea) {
    textarea.addEventListener("keydown", (e) => {
        const key = e.key;
        if (!OPENING_BRACKETS.has(key)) return;
        const start = textarea.selectionStart;
        const end = textarea.selectionEnd;
        if (start !== end) return;

        const after = textarea.value[start] ?? "";
        const closing = BRACKET_PAIRS[key];
        if (/[a-zA-Z0-9_]/.test(after) || after === closing) return;

        e.preventDefault();
        textarea.value = `${textarea.value.slice(0, start)}${key}${closing}${textarea.value.slice(start)}`;
        textarea.selectionStart = textarea.selectionEnd = start + 1;
        textarea.dispatchEvent(new Event("input", { bubbles: true }));
    });
}

function attachToTextarea(textarea) {
    if (!isLikelyScriptTextarea(textarea)) return;
    const parent = textarea.parentElement;
    if (!parent) return;

    ensureStyles();

    const wrapper = document.createElement("div");
    wrapper.className = "mrmth-v2-editor";

    const gutter = document.createElement("div");
    gutter.className = "mrmth-v2-gutter";

    parent.replaceChild(wrapper, textarea);
    wrapper.appendChild(gutter);
    wrapper.appendChild(textarea);

    textarea.classList.add("mrmth-v2-textarea");
    textarea.dataset.mrmthV2Script = "1";

    const refresh = () => updateGutter(textarea, gutter);
    textarea.addEventListener("input", refresh);
    textarea.addEventListener("scroll", refresh);

    addBracketAutoClose(textarea);
    refresh();
}

function scan(root = document) {
    root.querySelectorAll("textarea").forEach(attachToTextarea);
}

app.registerExtension({
    name: "mrmth.ScriptTextInput.V2",
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