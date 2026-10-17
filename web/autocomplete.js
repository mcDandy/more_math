import { FUNCTIONS, KEYWORDS, CONSTANTS, FUNCTION_META } from "./inbuilt_symbols.js";

const AUTOCOMPLETE_STYLE_ID = "mrmth-script-autocomplete-styles";
function ensureAutocompleteStyles() {
    if (document.getElementById(AUTOCOMPLETE_STYLE_ID)) return;

    const style = document.createElement("style");
    style.id = AUTOCOMPLETE_STYLE_ID;
    style.textContent = `
        .mrmth-autocomplete-layout {
            display: flex;
            flex-direction: row;
            align-items: flex-start;
            position: fixed;
            z-index: 10000;
            pointer-events: none;
        }

        .mrmth-autocomplete-layout[hidden],
        .mrmth-signature-hint[hidden] {
            display: none;
        }

        .mrmth-autocomplete {
            width: 260px;
            max-height: 220px;
            overflow-y: auto;
            overscroll-behavior: contain;
            pointer-events: auto;
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

        .mrmth-autocomplete-item.is-variable .mrmth-ac-name {
            color: #ecf0f1;
        }

        .mrmth-autocomplete-tooltip,
        .mrmth-signature-hint {
            max-width: 320px;
            padding: 8px 10px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 8px;
            background: rgba(24, 28, 36, 0.98);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
            font-family: monospace;
            font-size: 11px;
            color: #b3b9c1;
            line-height: 1.5;
        }

        .mrmth-autocomplete-tooltip {
            min-width: 200px;
            margin-left: 8px;
            pointer-events: auto;
        }

        .mrmth-signature-hint {
            position: fixed;
            z-index: 10000;
            pointer-events: none;
        }

        .mrmth-tt-title,
        .mrmth-sig-call {
            color: #c39bd3;
            font-weight: 600;
        }

        .mrmth-tt-details {
            margin-top: 4px;
            white-space: pre-wrap;
            color: #9aa0a6;
        }

        .mrmth-sig-call .mrmth-sig-active {
            color: #ffd700;
            text-decoration: underline;
        }
    `;
    document.head.appendChild(style);
}

export function escapeHtml(value) {
    return value
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

const BRACKET_PAIRS = { "(": ")", "[": "]", "{": "}" };
const OPENING_BRACKETS = new Set(Object.keys(BRACKET_PAIRS));
const CLOSING_BRACKETS = new Set(Object.values(BRACKET_PAIRS));
const QUOTES = new Set(['"', "'"]);
const INDENT = "    ";

// Mirrors the MathExpr.g4 lexer closely enough for highlighting. Unterminated
// block comments and strings run to the end of the text/line so they show up.
const TOKEN_PATTERN = /#.*|\/\*[\s\S]*?(?:\*\/|$)|"(?:\\.|[^"\\\r\n])*"?|'(?:\\.|[^'\\\r\n])*'?|\b\d+(?:\.\d*)?(?:[eE][+-]?\d+)?|\B\.\d+(?:[eE][+-]?\d+)?|==|!=|>=|<=|<<|>>|->|\+=|-=|\*=|\/=|%=|[+\-*/%^=<>|?:,;()\[\]{}]|[a-zA-Z_][a-zA-Z_0-9]*|\s+|./g;

/**
 * Splits script text into tokens. Bracket tokens get `depth` (per bracket
 * type, for rainbow colouring) and `match` (index of the paired bracket token,
 * or -1 when unmatched).
 */
export function tokenize(text) {
    const tokens = [];
    const openStack = [];
    const depthByType = { "(": 0, "[": 0, "{": 0 };
    TOKEN_PATTERN.lastIndex = 0;
    let m;

    while ((m = TOKEN_PATTERN.exec(text)) !== null) {
        const value = m[0];
        const c = value[0];
        const token = { type: "text", value, start: m.index, depth: 0, match: -1 };

        if (c === "#" || value.startsWith("/*")) {
            token.type = "comment";
        } else if (c === '"' || c === "'") {
            token.type = "string";
        } else if (OPENING_BRACKETS.has(c)) {
            token.type = "bracket";
            token.depth = depthByType[c]++;
            openStack.push(tokens.length);
        } else if (CLOSING_BRACKETS.has(c)) {
            token.type = "bracket";
            const openIndex = openStack[openStack.length - 1];
            const open = tokens[openIndex];
            if (open && BRACKET_PAIRS[open.value] === c) {
                openStack.pop();
                token.depth = --depthByType[open.value];
                token.match = openIndex;
                open.match = tokens.length;
            }
        } else if (/^(?:[+\-*/%^=<>|?:,;]|!=)/.test(value)) {
            token.type = "operator";
        } else if (/^\.?\d/.test(value)) {
            token.type = "number";
        } else if (/^[a-zA-Z_]/.test(c)) {
            if (KEYWORDS.has(value)) token.type = "keyword";
            else if (CONSTANTS.has(value)) token.type = "constant";
            else if (FUNCTIONS.has(value)) token.type = "function";
            else token.type = "variable";
        }

        tokens.push(token);
    }
    return tokens;
}

function isBlank(token) {
    return token.type === "text" && !token.value.trim();
}

/**
 * Insert text through the browser's editing pipeline so it lands on the native
 * undo stack (plain `textarea.value = ...` assignments wipe Ctrl+Z history).
 * An empty `text` deletes the range.
 */
export function insertText(textarea, start, end, text) {
    textarea.focus();
    textarea.setSelectionRange(start, end);
    const ok = text ? document.execCommand("insertText", false, text) : document.execCommand("delete");
    if (!ok) {
        textarea.setRangeText(text, start, end, "end");
        textarea.dispatchEvent(new Event("input", { bubbles: true }));
    }
}

export function renderHighlight(text, cursor) {
    const tokens = tokenize(text);

    // Bracket next to the cursor (left side preferred) and its partner.
    const active = new Set();
    const isPairedAt = (pos) => (t) => t.type === "bracket" && t.start === pos && t.match !== -1;
    let nearIndex = tokens.findIndex(isPairedAt(cursor - 1));
    if (nearIndex === -1) nearIndex = tokens.findIndex(isPairedAt(cursor));
    if (nearIndex !== -1) {
        active.add(nearIndex);
        active.add(tokens[nearIndex].match);
    }

    return tokens.map((t, i) => {
        if (t.type === "text") return escapeHtml(t.value);
        if (t.type === "bracket") {
            let cls = t.match === -1 ? "mrmth-bracket-unmatched" : `mrmth-bracket-${t.depth % 6}`;
            if (active.has(i)) cls += " mrmth-bracket-active";
            return `<span class="mrmth-token-bracket ${cls}">${escapeHtml(t.value)}</span>`;
        }
        return `<span class="mrmth-token-${t.type}">${escapeHtml(t.value)}</span>`;
    }).join("");
}

/**
 * Editor key behaviour: bracket/quote pairing, Backspace pair delete, auto
 * indent on Enter, Tab / Shift+Tab indent. Returns true when the key was
 * handled and the caller should preventDefault. Keys already consumed by the
 * autocomplete popup arrive with `defaultPrevented` and are ignored.
 */
export function handleEditingKey(textarea, e) {
    if (e.defaultPrevented || e.ctrlKey || e.metaKey || e.altKey || e.isComposing) return false;
    const { selectionStart: start, selectionEnd: end, value } = textarea;
    const prev = value[start - 1] ?? "";
    const next = value[end] ?? "";
    const lineStart = value.lastIndexOf("\n", start - 1) + 1;
    const key = e.key;

    // Type over an already present closing bracket/quote.
    if (start === end && next === key && (CLOSING_BRACKETS.has(key) || QUOTES.has(key))) {
        textarea.setSelectionRange(start + 1, start + 1);
        return true;
    }

    if (Object.hasOwn(BRACKET_PAIRS, key) || QUOTES.has(key)) {
        const closing = BRACKET_PAIRS[key] ?? key;
        if (start !== end) {
            insertText(textarea, start, end, key + value.slice(start, end) + closing);
            textarea.setSelectionRange(start + 1, end + 1);
            return true;
        }
        if (/\w/.test(next) || (QUOTES.has(key) && /\w/.test(prev))) return false;
        insertText(textarea, start, end, key + closing);
        textarea.setSelectionRange(start + 1, start + 1);
        return true;
    }

    // `}` typed on a whitespace-only line closes one indent level.
    if (key === "}" && start === end && /^[ \t]*$/.test(value.slice(lineStart, start)) && value.slice(lineStart, start).endsWith(INDENT)) {
        insertText(textarea, start - INDENT.length, start, "}");
        return true;
    }

    if (key === "Backspace" && start === end && start > 0 && (BRACKET_PAIRS[prev] === next || (QUOTES.has(prev) && prev === next))) {
        insertText(textarea, start - 1, start + 1, "");
        return true;
    }

    if (key === "Enter" && !e.shiftKey) {
        const before = value.slice(lineStart, start);
        const lead = before.match(/^[ \t]*/)[0];
        if (before.trimEnd().endsWith("{")) {
            const inner = lead + INDENT;
            const text = next === "}" ? `\n${inner}\n${lead}` : `\n${inner}`;
            insertText(textarea, start, end, text);
            const caret = start + 1 + inner.length;
            textarea.setSelectionRange(caret, caret);
        } else {
            insertText(textarea, start, end, `\n${lead}`);
        }
        return true;
    }

    if (key === "Tab") {
        if (!e.shiftKey && start === end) {
            insertText(textarea, start, end, INDENT);
            return true;
        }
        // Indent / unindent every line touched by the selection.
        const blockEnd = end > start && value[end - 1] === "\n" ? end - 1 : end;
        const block = value.slice(lineStart, blockEnd);
        const lines = block.split("\n");
        const newLines = e.shiftKey ? lines.map((l) => l.replace(/^(?: {1,4}|\t)/, "")) : lines.map((l) => INDENT + l);
        const newBlock = newLines.join("\n");
        if (newBlock === block) return true;
        insertText(textarea, lineStart, blockEnd, newBlock);
        const firstDelta = newLines[0].length - lines[0].length;
        const totalDelta = newBlock.length - block.length;
        textarea.setSelectionRange(Math.max(lineStart, start + firstDelta), Math.max(lineStart, end + totalDelta));
        return true;
    }

    return false;
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
            if (ch === stringChar || ch === "\n") inString = false;
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

    return inString || inLineComment || inBlockComment;
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

// Names defined or used in the script itself; `name(` counts as a function.
function collectUserSymbols(text, skipStart) {
    const tokens = tokenize(text);
    const symbols = new Map();
    tokens.forEach((t, i) => {
        if (t.type !== "variable" || t.start === skipStart) return;
        let j = i + 1;
        while (tokens[j] && isBlank(tokens[j])) j++;
        if (tokens[j]?.value === "(") symbols.set(t.value, "function");
        else if (!symbols.has(t.value)) symbols.set(t.value, "variable");
    });
    return symbols;
}

const KIND_ORDER = { variable: 0, function: 1, constant: 2, keyword: 3 };

function buildSuggestions(prefix, userSymbols = new Map()) {
    const lower = prefix.toLowerCase();
    const items = [];
    const matches = (name) => name.toLowerCase().startsWith(lower);

    for (const [name, kind] of userSymbols) {
        if (matches(name)) items.push({ name, kind, detail: kind === "function" ? "user" : "" });
    }
    for (const name of FUNCTIONS) {
        if (matches(name)) items.push({ name, kind: "function", detail: formatArgHint(FUNCTION_META[name]) });
    }
    for (const name of CONSTANTS) {
        if (matches(name)) items.push({ name, kind: "constant", detail: "" });
    }
    for (const name of KEYWORDS) {
        if (matches(name)) items.push({ name, kind: "keyword", detail: "" });
    }

    items.sort((a, b) => KIND_ORDER[a.kind] - KIND_ORDER[b.kind] || a.name.localeCompare(b.name));
    return items.slice(0, 40);
}

// Innermost built-in call whose argument list contains the cursor.
function findCallContext(text, cursor) {
    const tokens = tokenize(text.slice(0, cursor));
    let depth = 0;
    let argIndex = 0;
    for (let i = tokens.length - 1; i >= 0; i--) {
        const { type, value } = tokens[i];
        if (value === "," && type === "operator") {
            if (depth === 0) argIndex++;
            continue;
        }
        if (type !== "bracket") continue;
        if (CLOSING_BRACKETS.has(value)) {
            depth++;
            continue;
        }
        if (depth > 0) {
            depth--;
            continue;
        }
        if (value !== "(") return null;

        let j = i - 1;
        while (j >= 0 && isBlank(tokens[j])) j--;
        const name = tokens[j]?.type === "function" ? tokens[j].value : null;
        return name ? { name, argIndex } : null;
    }
    return null;
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
    div.style.whiteSpace = style.whiteSpace === "none" ? "pre" : "pre-wrap";
    div.style.overflowWrap = style.overflowWrap;
    div.style.wordBreak = style.wordBreak;
    div.style.width = `${textarea.clientWidth}px`;

    for (const prop of props) {
        div.style[prop] = style[prop];
    }

    const span = document.createElement("span");
    span.textContent = textarea.value.substring(0, position);
    div.appendChild(span);
    const marker = document.createElement("span");
    marker.textContent = "​";
    div.appendChild(marker);
    document.body.appendChild(div);

    const top = marker.offsetTop;
    const left = marker.offsetLeft;
    div.remove();
    return { top, left };
}

// The node canvas may scale the textarea with a CSS transform.
function getTextareaViewportScale(textarea) {
    const layoutHeight = textarea.offsetHeight;
    if (layoutHeight <= 0) return 1;
    return textarea.getBoundingClientRect().height / layoutHeight;
}

function getViewportLineHeight(textarea, scale) {
    const lh = parseFloat(window.getComputedStyle(textarea).lineHeight);
    if (Number.isFinite(lh) && lh > 0) return lh * scale;
    return 18 * scale;
}

function getCaretScreenPosition(textarea, position) {
    const coords = getCaretCoordinates(textarea, position);
    const rect = textarea.getBoundingClientRect();
    const scale = getTextareaViewportScale(textarea);

    const x = coords.left - textarea.scrollLeft;
    const y = coords.top - textarea.scrollTop - 6;

    return {
        left: rect.left + x * scale,
        top: rect.top + y * scale,
        scale,
    };
}

/**
 * Attach identifier autocomplete and built-in signature hints to a script
 * textarea. The popups are portaled to document.body. Must be attached before
 * other keydown handlers so they can skip keys it consumed (`defaultPrevented`).
 * @param {HTMLTextAreaElement} textarea
 * @returns {{ destroy: () => void, close: () => void }}
 */
export function attachAutocomplete(textarea) {
    ensureAutocompleteStyles();

    const layoutEl = document.createElement("div");
    layoutEl.className = "mrmth-autocomplete-layout";
    layoutEl.hidden = true;

    const listEl = document.createElement("ul");
    listEl.className = "mrmth-autocomplete";
    layoutEl.appendChild(listEl);

    const tooltipEl = document.createElement("div");
    tooltipEl.className = "mrmth-autocomplete-tooltip";
    tooltipEl.style.display = "none";
    layoutEl.appendChild(tooltipEl);

    const hintEl = document.createElement("div");
    hintEl.className = "mrmth-signature-hint";
    hintEl.hidden = true;

    document.body.appendChild(layoutEl);
    document.body.appendChild(hintEl);

    let items = [];
    let selectedIndex = 0;
    let navigated = false;
    let prefixInfo = null;
    let open = false;

    listEl.addEventListener("wheel", (e) => {
        e.stopPropagation();
        const maxScroll = Math.max(0, listEl.scrollHeight - listEl.clientHeight);
        if ((e.deltaY < 0 && listEl.scrollTop <= 0) || (e.deltaY > 0 && listEl.scrollTop >= maxScroll)) {
            e.preventDefault();
        }
    }, { passive: false });

    function updateTooltip(item) {
        const meta = item.kind === "function" ? FUNCTION_META[item.name] : null;
        if (!meta?.description) {
            tooltipEl.style.display = "none";
            return;
        }

        let argsText = `Arguments: min ${meta.minArgs}`;
        argsText += meta.maxArgs === null ? "+ (variadic)" : `, max ${meta.maxArgs}`;

        tooltipEl.innerHTML = `
            <div class="mrmth-tt-title">${escapeHtml(meta.signature)}</div>
            <div class="mrmth-tt-desc">${escapeHtml(meta.description)}</div>
            ${meta.details ? `<div class="mrmth-tt-details">${escapeHtml(meta.details)}</div>` : ""}
            <div class="mrmth-tt-args">${argsText}</div>
            ${meta.aliases.length ? `<div class="mrmth-tt-args">Also: ${escapeHtml(meta.aliases.join(", "))}</div>` : ""}
        `;
        tooltipEl.style.display = "block";

        const rect = tooltipEl.getBoundingClientRect();
        const flip = rect.right > window.innerWidth;
        layoutEl.style.flexDirection = flip ? "row-reverse" : "row";
        tooltipEl.style.marginLeft = flip ? "0" : "8px";
        tooltipEl.style.marginRight = flip ? "8px" : "0";
    }

    const close = () => {
        open = false;
        layoutEl.hidden = true;
        listEl.innerHTML = "";
        tooltipEl.style.display = "none";
        items = [];
        selectedIndex = 0;
        prefixInfo = null;
    };

    const openWith = (nextItems, nextPrefix) => {
        items = nextItems;
        selectedIndex = 0;
        navigated = false;
        prefixInfo = nextPrefix;
        open = true;
        layoutEl.hidden = false;
        hideHint();
        render();
    };

    const scrollSelectedIntoView = () => {
        const selected = listEl.children[selectedIndex];
        if (!selected) return;

        const itemTop = selected.offsetTop;
        const itemBottom = itemTop + selected.offsetHeight;
        const pad = 2;
        if (itemTop < listEl.scrollTop + pad) {
            listEl.scrollTop = Math.max(0, itemTop - pad);
        } else if (itemBottom > listEl.scrollTop + listEl.clientHeight - pad) {
            listEl.scrollTop = itemBottom - listEl.clientHeight + pad;
        }
    };

    const render = () => {
        listEl.innerHTML = "";
        items.forEach((item, index) => {
            const li = document.createElement("li");
            li.className = `mrmth-autocomplete-item is-${item.kind}${index === selectedIndex ? " is-selected" : ""}`;

            const name = document.createElement("span");
            name.className = "mrmth-ac-name";
            name.textContent = item.name;

            const detail = document.createElement("span");
            detail.className = "mrmth-ac-hint";
            detail.textContent = item.detail;

            const kind = document.createElement("span");
            kind.className = "mrmth-ac-kind";
            kind.textContent = item.kind;

            li.append(name, detail, kind);

            li.addEventListener("mousedown", (e) => {
                e.preventDefault();
                selectedIndex = index;
                applySelected();
            });

            li.addEventListener("mouseenter", () => {
                selectedIndex = index;
                for (const el of listEl.children) el.classList.toggle("is-selected", el === li);
                updateTooltip(item);
            });

            listEl.appendChild(li);
        });

        scrollSelectedIntoView();
        updateTooltip(items[selectedIndex]);
        positionDropdown();
    };

    const positionDropdown = () => {
        const caret = getCaretScreenPosition(textarea, textarea.selectionStart);
        const textareaRect = textarea.getBoundingClientRect();
        const lineHeight = getViewportLineHeight(textarea, caret.scale);
        const gap = 6;
        const viewportPad = 8;
        const preferredMax = 220;
        const minListHeight = 48;
        const dropdownWidth = 260;

        const lineTop = caret.top;
        const lineBottom = lineTop + lineHeight;
        const spaceBelow = window.innerHeight - lineBottom - gap - viewportPad;
        const spaceAbove = lineTop - gap - viewportPad;
        const spaceRight = window.innerWidth - textareaRect.right - gap - viewportPad;

        let placement = "below";
        if (spaceBelow < minListHeight) {
            if (spaceRight >= 160) {
                placement = "right";
            } else if (spaceAbove > spaceBelow + 40) {
                placement = "above";
            }
        }

        let maxHeight;
        let top;
        let left = caret.left;

        if (placement === "below") {
            maxHeight = Math.min(preferredMax, Math.max(minListHeight, spaceBelow));
            top = lineBottom + gap;
        } else if (placement === "above") {
            maxHeight = Math.min(preferredMax, Math.max(minListHeight, spaceAbove));
            top = lineTop - gap - maxHeight;
            if (top < viewportPad) {
                maxHeight = Math.max(minListHeight, lineTop - gap - viewportPad);
                top = lineTop - gap - maxHeight;
            }
        } else {
            maxHeight = Math.min(preferredMax, window.innerHeight - viewportPad * 2);
            top = Math.max(viewportPad, Math.min(lineTop, window.innerHeight - maxHeight - viewportPad));
            left = textareaRect.right + gap;
        }

        listEl.style.maxHeight = `${maxHeight}px`;
        layoutEl.style.top = `${top}px`;
        layoutEl.style.left = `${Math.max(viewportPad, Math.min(left, window.innerWidth - dropdownWidth - viewportPad))}px`;
    };

    const applySelected = () => {
        const item = items[selectedIndex];
        if (!item) return;
        const end = textarea.selectionStart;
        const isCall = item.kind === "function";
        const hasParen = textarea.value[end] === "(";

        let caret = prefixInfo.start + item.name.length;
        if (isCall && hasParen) {
            insertText(textarea, prefixInfo.start, end, item.name);
            caret += 1;
        } else if (isCall) {
            insertText(textarea, prefixInfo.start, end, `${item.name}()`);
            caret += 1;
        } else {
            insertText(textarea, prefixInfo.start, end, item.name);
        }
        textarea.setSelectionRange(caret, caret);
        close();
        updateHint();
    };

    const maybeOpen = (force) => {
        const text = textarea.value;
        const cursor = textarea.selectionStart;
        if (cursor !== textarea.selectionEnd || isCursorInStringOrComment(text, cursor)) {
            close();
            return;
        }

        const info = getWordPrefix(text, cursor);
        if (!info || (!force && !open && info.word.length < 2)) {
            close();
            return;
        }

        const suggestions = buildSuggestions(info.word, collectUserSymbols(text, info.start));
        // Nothing to offer once the word is already complete.
        if (!suggestions.length || (!force && suggestions.length === 1 && suggestions[0].name === info.word)) {
            close();
            return;
        }
        openWith(suggestions, info);
    };

    function hideHint() {
        hintEl.hidden = true;
    }

    function updateHint() {
        const cursor = textarea.selectionStart;
        if (open || document.activeElement !== textarea || cursor !== textarea.selectionEnd) {
            hideHint();
            return;
        }
        const ctx = findCallContext(textarea.value, cursor);
        const meta = ctx && FUNCTION_META[ctx.name];
        if (!meta) {
            hideHint();
            return;
        }

        // A variadic arg (`...`, `[sizes...]`) absorbs every argument from its position on.
        const variadicAt = meta.args.findIndex((a) => a.includes("..."));
        let active = ctx.argIndex;
        if (variadicAt !== -1 && active >= variadicAt) active = variadicAt;
        const args = meta.args
            .map((a, i) => (i === active ? `<span class="mrmth-sig-active">${escapeHtml(a)}</span>` : escapeHtml(a)))
            .join(", ");

        hintEl.innerHTML = `
            <div class="mrmth-sig-call">${escapeHtml(ctx.name)}(${args})</div>
            ${meta.description ? `<div class="mrmth-tt-desc">${escapeHtml(meta.description)}</div>` : ""}
        `;
        hintEl.hidden = false;

        const caret = getCaretScreenPosition(textarea, cursor);
        const lineHeight = getViewportLineHeight(textarea, caret.scale);
        const hintRect = hintEl.getBoundingClientRect();
        const viewportPad = 8;
        let top = caret.top - hintRect.height - 4;
        if (top < viewportPad) top = caret.top + lineHeight + 6;
        hintEl.style.top = `${top}px`;
        hintEl.style.left = `${Math.max(viewportPad, Math.min(caret.left, window.innerWidth - hintRect.width - viewportPad))}px`;
    }

    const onInput = () => {
        maybeOpen(false);
        updateHint();
    };

    const onKeyDown = (e) => {
        if (e.ctrlKey && e.key === " ") {
            e.preventDefault();
            maybeOpen(true);
            return;
        }

        if (!open) {
            if (e.key === "Escape") hideHint();
            return;
        }

        if (e.key === "ArrowDown" || e.key === "ArrowUp") {
            e.preventDefault();
            const step = e.key === "ArrowDown" ? 1 : -1;
            selectedIndex = (selectedIndex + step + items.length) % items.length;
            navigated = true;
            render();
            return;
        }
        // Enter only accepts after the list was navigated, otherwise it would
        // swallow newlines after words like `return` that happen to match.
        if (e.key === "Tab" || (e.key === "Enter" && navigated)) {
            e.preventDefault();
            applySelected();
            return;
        }
        if (e.key === "Enter" || e.key === "Escape") {
            if (e.key === "Escape") e.preventDefault();
            close();
        }
    };

    const onSelectionChange = () => {
        if (document.activeElement === textarea) updateHint();
    };

    const onBlur = () => {
        setTimeout(close, 120);
        hideHint();
    };

    const onReposition = () => {
        if (open) positionDropdown();
        if (!hintEl.hidden) updateHint();
    };

    textarea.addEventListener("input", onInput);
    textarea.addEventListener("keydown", onKeyDown);
    textarea.addEventListener("blur", onBlur);
    textarea.addEventListener("scroll", onReposition);
    document.addEventListener("selectionchange", onSelectionChange);
    window.addEventListener("scroll", onReposition, true);
    window.addEventListener("resize", onReposition);

    return {
        close,
        destroy() {
            close();
            textarea.removeEventListener("input", onInput);
            textarea.removeEventListener("keydown", onKeyDown);
            textarea.removeEventListener("blur", onBlur);
            textarea.removeEventListener("scroll", onReposition);
            document.removeEventListener("selectionchange", onSelectionChange);
            window.removeEventListener("scroll", onReposition, true);
            window.removeEventListener("resize", onReposition);
            layoutEl.remove();
            hintEl.remove();
        },
    };
}

export { buildSuggestions, getWordPrefix, isCursorInStringOrComment, formatArgHint };
