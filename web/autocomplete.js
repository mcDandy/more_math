import { FUNCTIONS, KEYWORDS, CONSTANTS, FUNCTION_META } from "./inbuilt_symbols.js";

const AUTOCOMPLETE_STYLE_ID = "mrmth-script-autocomplete-styles";

function ensureAutocompleteStyles() {
    if (document.getElementById(AUTOCOMPLETE_STYLE_ID)) return;

    const style = document.createElement("style");
    style.id = AUTOCOMPLETE_STYLE_ID;
    style.textContent = `
        .mrmth-autocomplete {
            position: absolute;
            z-index: 20;
            min-width: 180px;
            max-width: min(420px, 100%);
            max-height: 220px;
            overflow-y: auto;
            margin: 0;
            padding: 4px 0;
            list-style: none;
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 8px;
            background: rgba(18, 20, 24, 0.97);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
            font-family: monospace;
            font-size: 12px;
        }

        .mrmth-autocomplete-item {
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            gap: 12px;
            padding: 5px 10px;
            cursor: pointer;
            color: #ecf0f1;
        }

        .mrmth-autocomplete-item.is-selected {
            background: rgba(142, 68, 173, 0.35);
        }

        .mrmth-autocomplete-item .mrmth-ac-kind {
            flex-shrink: 0;
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: #9aa0a6;
        }

        .mrmth-autocomplete-item .mrmth-ac-name {
            color: #c39bd3;
            font-weight: 600;
        }

        .mrmth-autocomplete-item.is-keyword .mrmth-ac-name {
            color: #e74c3c;
        }

        .mrmth-autocomplete-item.is-constant .mrmth-ac-name {
            color: #f1c40f;
        }

        .mrmth-autocomplete-item .mrmth-ac-hint {
            color: #7f8c8d;
            font-size: 11px;
            white-space: nowrap;
        }
    `;
    document.head.appendChild(style);
}

function isCursorInStringOrComment(text, cursor) {
    let inString = false;
    let stringChar = "";
    let inLineComment = false;
    let inBlockComment = false;

    for (let i = 0; i < cursor; i++) {
        const ch = text[i];
        const next = text[i + 1];

        if (inLineComment) {
            if (ch === "\n") inLineComment = false;
            continue;
        }
        if (inBlockComment) {
            if (ch === "*" && next === "/") {
                inBlockComment = false;
                i++;
            }
            continue;
        }
        if (inString) {
            if (ch === "\\") {
                i++;
                continue;
            }
            if (ch === stringChar) inString = false;
            continue;
        }
        if (ch === "#") {
            inLineComment = true;
            continue;
        }
        if (ch === "/" && next === "*") {
            inBlockComment = true;
            i++;
            continue;
        }
        if (ch === '"' || ch === "'") {
            inString = true;
            stringChar = ch;
        }
    }

    return inString || inBlockComment;
}

function getWordPrefix(text, cursor) {
    const before = text.slice(0, cursor);
    const match = before.match(/[a-zA-Z_][a-zA-Z0-9_]*$/);
    if (!match) return null;
    return { word: match[0], start: cursor - match[0].length };
}

function formatArgHint(meta) {
    if (!meta) return "";
    if (meta.maxArgs === null) {
        if (meta.minArgs <= 1) return "(…)";
        return `(${meta.minArgs}+ args)`;
    }
    if (meta.minArgs === meta.maxArgs) {
        if (meta.minArgs === 0) return "()";
        if (meta.minArgs === 1) return "(x)";
        return `(${meta.minArgs} args)`;
    }
    return `(${meta.minArgs}–${meta.maxArgs} args)`;
}

function buildSuggestions(prefix) {
    const lower = prefix.toLowerCase();
    const items = [];

    for (const name of FUNCTIONS) {
        if (!name.toLowerCase().startsWith(lower)) continue;
        const meta = FUNCTION_META[name];
        items.push({
            name,
            kind: "function",
            hint: meta?.snippet || `${name}()`,
            detail: formatArgHint(meta),
            insertText: meta?.snippet || `${name}()`,
        });
    }
    for (const name of KEYWORDS) {
        if (!name.toLowerCase().startsWith(lower)) continue;
        items.push({
            name,
            kind: "keyword",
            hint: name,
            detail: "",
            insertText: name,
        });
    }
    for (const name of CONSTANTS) {
        if (!name.toLowerCase().startsWith(lower)) continue;
        items.push({
            name,
            kind: "constant",
            hint: name,
            detail: "",
            insertText: name,
        });
    }

    items.sort((a, b) => {
        const kindOrder = { function: 0, constant: 1, keyword: 2 };
        const ka = kindOrder[a.kind] ?? 9;
        const kb = kindOrder[b.kind] ?? 9;
        if (ka !== kb) return ka - kb;
        return a.name.localeCompare(b.name);
    });

    return items.slice(0, 40);
}

function getCaretCoordinates(textarea, position) {
    const style = window.getComputedStyle(textarea);
    const div = document.createElement("div");
    const props = [
        "fontFamily", "fontSize", "fontWeight", "fontStyle", "lineHeight",
        "letterSpacing", "textTransform", "wordSpacing", "textIndent",
        "whiteSpace", "wordBreak", "overflowWrap", "paddingTop", "paddingRight",
        "paddingBottom", "paddingLeft", "borderTopWidth", "borderRightWidth",
        "borderBottomWidth", "borderLeftWidth", "boxSizing",
    ];
    div.style.position = "absolute";
    div.style.visibility = "hidden";
    div.style.whiteSpace = "pre-wrap";
    div.style.overflowWrap = style.overflowWrap;
    div.style.wordBreak = style.wordBreak;
    div.style.width = `${textarea.clientWidth}px`;
    for (const prop of props) {
        div.style[prop] = style[prop];
    }

    const text = textarea.value.substring(0, position);
    const span = document.createElement("span");
    span.textContent = text;
    div.appendChild(span);
    const marker = document.createElement("span");
    marker.textContent = textarea.value.substring(position) || ".";
    div.appendChild(marker);
    document.body.appendChild(div);

    const top = marker.offsetTop;
    const left = marker.offsetLeft;
    div.remove();
    return { top, left };
}

/**
 * Attach identifier autocomplete to a script textarea.
 * @param {HTMLTextAreaElement} textarea
 * @param {HTMLElement} containerEl - positioned parent (e.g. .mrmth-editor-container)
 * @returns {{ destroy: () => void, close: () => void }}
 */
export function attachAutocomplete(textarea, containerEl) {
    ensureAutocompleteStyles();

    const dropdown = document.createElement("ul");
    dropdown.className = "mrmth-autocomplete";
    dropdown.hidden = true;
    containerEl.appendChild(dropdown);

    let items = [];
    let selectedIndex = 0;
    let prefixInfo = null;
    let open = false;

    const close = () => {
        open = false;
        dropdown.hidden = true;
        dropdown.innerHTML = "";
        items = [];
        selectedIndex = 0;
        prefixInfo = null;
    };

    const render = () => {
        dropdown.innerHTML = "";
        items.forEach((item, index) => {
            const li = document.createElement("li");
            li.className = `mrmth-autocomplete-item is-${item.kind}${index === selectedIndex ? " is-selected" : ""}`;
            li.dataset.index = String(index);

            const left = document.createElement("span");
            left.className = "mrmth-ac-name";
            left.textContent = item.name;

            const right = document.createElement("span");
            right.className = "mrmth-ac-hint";
            right.textContent = item.detail || item.hint;

            const kind = document.createElement("span");
            kind.className = "mrmth-ac-kind";
            kind.textContent = item.kind;

            li.appendChild(left);
            li.appendChild(right);
            li.appendChild(kind);
            li.addEventListener("mousedown", (e) => {
                e.preventDefault();
                selectedIndex = index;
                applySelected();
            });
            dropdown.appendChild(li);
        });
    };

    const positionDropdown = () => {
        if (!prefixInfo) return;
        const coords = getCaretCoordinates(textarea, prefixInfo.start);
        dropdown.style.left = `${coords.left}px`;
        dropdown.style.top = `${coords.top + 18}px`;
    };

    const openWith = (nextItems, nextPrefix) => {
        if (!nextItems.length) {
            close();
            return;
        }
        items = nextItems;
        selectedIndex = 0;
        prefixInfo = nextPrefix;
        open = true;
        dropdown.hidden = false;
        render();
        positionDropdown();
    };

    const applySelected = () => {
        if (!open || !prefixInfo || !items[selectedIndex]) return;

        const item = items[selectedIndex];
        const before = textarea.value.slice(0, prefixInfo.start);
        const after = textarea.value.slice(textarea.selectionEnd);
        const insert = item.insertText;
        textarea.value = `${before}${insert}${after}`;

        const cursorPos = before.length + insert.length;
        if (item.kind === "function" && insert.endsWith("()")) {
            textarea.selectionStart = textarea.selectionEnd = cursorPos - 1;
        } else {
            textarea.selectionStart = textarea.selectionEnd = cursorPos;
        }

        textarea.dispatchEvent(new Event("input", { bubbles: true }));
        close();
    };

    const maybeOpen = (force = false) => {
        const cursor = textarea.selectionStart;
        if (cursor !== textarea.selectionEnd) {
            close();
            return;
        }
        if (isCursorInStringOrComment(textarea.value, cursor)) {
            close();
            return;
        }

        const info = getWordPrefix(textarea.value, cursor);
        if (!info || (!force && info.word.length < 1)) {
            close();
            return;
        }

        const suggestions = buildSuggestions(info.word);
        if (!suggestions.length) {
            close();
            return;
        }
        openWith(suggestions, info);
    };

    const onInput = () => {
        if (!open) {
            const info = getWordPrefix(textarea.value, textarea.selectionStart);
            if (info && info.word.length >= 2) {
                maybeOpen(false);
            }
            return;
        }
        maybeOpen(false);
    };

    const onKeyDown = (e) => {
        if (e.ctrlKey && e.key === " ") {
            e.preventDefault();
            maybeOpen(true);
            return;
        }

        if (!open) return;

        if (e.key === "ArrowDown") {
            e.preventDefault();
            selectedIndex = (selectedIndex + 1) % items.length;
            render();
            return;
        }
        if (e.key === "ArrowUp") {
            e.preventDefault();
            selectedIndex = (selectedIndex - 1 + items.length) % items.length;
            render();
            return;
        }
        if (e.key === "Enter" || e.key === "Tab") {
            e.preventDefault();
            applySelected();
            return;
        }
        if (e.key === "Escape") {
            e.preventDefault();
            close();
        }
    };

    const onBlur = () => {
        setTimeout(close, 120);
    };

    const onScroll = () => {
        if (open) positionDropdown();
    };

    textarea.addEventListener("input", onInput);
    textarea.addEventListener("keydown", onKeyDown);
    textarea.addEventListener("blur", onBlur);
    textarea.addEventListener("scroll", onScroll);

    return {
        close,
        destroy() {
            close();
            dropdown.remove();
            textarea.removeEventListener("input", onInput);
            textarea.removeEventListener("keydown", onKeyDown);
            textarea.removeEventListener("blur", onBlur);
            textarea.removeEventListener("scroll", onScroll);
        },
    };
}

export { buildSuggestions, getWordPrefix, isCursorInStringOrComment, formatArgHint };
