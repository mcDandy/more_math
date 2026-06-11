import { FUNCTIONS, KEYWORDS, CONSTANTS, FUNCTION_META } from "./inbuilt_symbols.js";

const AUTOCOMPLETE_STYLE_ID = "mrmth-script-autocomplete-styles";
function ensureAutocompleteStyles() {
    if (document.getElementById(AUTOCOMPLETE_STYLE_ID)) return;

    const style = document.createElement("style");
    style.id = AUTOCOMPLETE_STYLE_ID;
    style.textContent = `


.mrmth-autocomplete-tooltip {
    display: none; /* Řízeno přes JS */
    min-width: 200px;
    max-width: 320px;
    margin-left: 8px;
    padding: 10px 12px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 8px;
    background: rgba(24, 28, 36, 0.98);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    font-family: monospace;
    font-size: 11px;
    color: #b3b9c1;
    line-height: 1.5;
    pointer-events: auto;
}

.mrmth-autocomplete-layout {
    display: flex !important;
    flex-direction: row !important;
    align-items: flex-start !important;
    position: fixed !important; /* Pozici drží POUZE tento společný obal! */
    z-index: 10000 !important;
    pointer-events: none;
}

.mrmth-autocomplete {
    min-width: 180px;
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
    div.style.whiteSpace = style.whiteSpace === "none" ? "pre" : "pre-wrap";
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
    marker.textContent = "\u200B";
    div.appendChild(marker);
    document.body.appendChild(div);

    const top = marker.offsetTop;
    const left = marker.offsetLeft;
    div.remove();
    return { top, left };
}


function getTextareaViewportScale(textarea) {
    const rect = textarea.getBoundingClientRect();
    const layoutHeight = textarea.offsetHeight;
    if (layoutHeight <= 0) return 1;
    return rect.height / layoutHeight;
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
    const y = coords.top - textarea.scrollTop-6;

    return {
        left: rect.left + x * scale,
        top: rect.top + y * scale,
        scale,
    };
}
/**
 * Attach identifier autocomplete to a script textarea.
 * @param {HTMLTextAreaElement} textarea
 * @param {HTMLElement} [_containerEl] - unused; dropdown is portaled to document.body
 * @returns {{ destroy: () => void, close: () => void }}
 */
export function attachAutocomplete(textarea, _containerEl) {
    ensureAutocompleteStyles();

    // 1. Deklarace prvků nového rozvržení
    let layoutEl = null;
    let listEl = null;    // Toto plně nahradí tvůj původní samostatný "dropdown"
    let tooltipEl = null;

    // 2. Opravené vytvoření dropdownu, které se spustí ihned
    function createDropdown() {
        layoutEl = document.createElement("div");
        layoutEl.className = "mrmth-autocomplete-layout";
        layoutEl.style.position = "fixed";
        layoutEl.style.zIndex = "10000";
        layoutEl.style.display = "flex";
        layoutEl.hidden = true;

        listEl = document.createElement("ul");
        listEl.className = "mrmth-autocomplete";
        listEl.addEventListener("wheel", onDropdownWheel, { passive: false });
        layoutEl.appendChild(listEl);

        tooltipEl = document.createElement("div");
        tooltipEl.className = "mrmth-autocomplete-tooltip";
        tooltipEl.style.display = "none";
        layoutEl.appendChild(tooltipEl);

        document.body.appendChild(layoutEl);
    }

    function updateTooltip(selectedItem) {
        if (!tooltipEl || !layoutEl) return;

        const meta = FUNCTION_META[selectedItem?.name] || selectedItem;

        if (!meta || !meta.description) {
            tooltipEl.style.display = "none";
            return;
        }

        let argsText = `Arguments: min ${meta.minArgs ?? 0}`;
        if (meta.maxArgs !== undefined && meta.maxArgs !== null) {
            argsText += `, max ${meta.maxArgs}`;
        } else {
            argsText += "+ (variadic)";
        }

        tooltipEl.innerHTML = `
            <div class="mrmth-tt-title">${selectedItem.name}</div>
            <div class="mrmth-tt-desc">${meta.description}</div>
            <div class="mrmth-tt-args">${argsText}</div>
        `;

        tooltipEl.style.display = "block";

        const rect = tooltipEl.getBoundingClientRect();
        if (rect.right > window.innerWidth) {
            layoutEl.style.flexDirection = "row-reverse";
            tooltipEl.style.marginLeft = "0";
            tooltipEl.style.marginRight = "8px";
        } else {
            layoutEl.style.flexDirection = "row";
            tooltipEl.style.marginLeft = "8px";
            tooltipEl.style.marginRight = "0";
        }
    }


    const onDropdownWheel = (e) => {
        e.stopPropagation();
        const maxScroll = Math.max(0, listEl.scrollHeight - listEl.clientHeight);
        const atTop = listEl.scrollTop <= 0;
        const atBottom = listEl.scrollTop >= maxScroll;
        if ((e.deltaY < 0 && atTop) || (e.deltaY > 0 && atBottom)) {
            e.preventDefault();
        }
    };

    createDropdown();


    let items = [];
    let selectedIndex = 0;
    let prefixInfo = null;
    let open = false;

    const close = () => {
        open = false;
        if (layoutEl) {
            layoutEl.hidden = true;
            layoutEl.style.visibility = "hidden";
        }
        if (listEl) listEl.innerHTML = "";
        if (tooltipEl) tooltipEl.style.display = "none";
        items = [];
        selectedIndex = 0;
        prefixInfo = null;
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
        if (layoutEl) {
            layoutEl.hidden = false;
            layoutEl.style.display = "flex"; // ZNOVU ROZSVÍTÍ KRESLENÍ PŘI PSANÍ
        }
        render();
        positionDropdown();
    };

    const scrollSelectedIntoView = () => {
        const selected = layoutEl.querySelector(".mrmth-autocomplete-item.is-selected");
        if (!selected) return;

        const itemTop = selected.offsetTop;
        const itemBottom = itemTop + selected.offsetHeight;
        const viewTop = listEl.scrollTop;
        const viewBottom = viewTop + listEl.clientHeight;

        const pad = 2;
        if (itemTop < viewTop + pad) {
            listEl.scrollTop = Math.max(0, itemTop - pad);
        } else if (itemBottom > viewBottom - pad) {
            listEl.scrollTop = itemBottom - listEl.clientHeight + pad;
        }
    };


    const render = () => {
        listEl.innerHTML = "";
        if (!items || items.length === 0) {
            close();
            return;
        }

        listEl.innerHTML = "";
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

            li.addEventListener("mouseenter", () => {
                selectedIndex = index;
                listEl.querySelectorAll(".mrmth-autocomplete-item").forEach((el, i) => {
                    el.classList.toggle("is-selected", i === index);
                });
                updateTooltip(item);
            });

            listEl.appendChild(li);
        });

        scrollSelectedIntoView();

        if (items[selectedIndex]) {
            updateTooltip(items[selectedIndex]);
        } else {
            tooltipEl.style.display = "none";
        }

        if (open) positionDropdown();
    };

    const positionDropdown = () => {
        if (!prefixInfo || !layoutEl || !listEl) return; // Změna kontroly prvků

        const cursorPos = textarea.selectionStart;
        const caret = getCaretScreenPosition(textarea, cursorPos);
        const textareaRect = textarea.getBoundingClientRect();
        const scale = caret.scale ?? getTextareaViewportScale(textarea);
        const lineHeight = getViewportLineHeight(textarea, scale);
        const gap = 6;
        const viewportPad = 8;
        const preferredMax = 220;
        const minListHeight = 48;

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
        let left;
        const dropdownWidthTarget = Math.max(180, textareaRect.width);

        if (placement === "below") {
            maxHeight = Math.min(preferredMax, Math.max(minListHeight, spaceBelow));
            top = lineBottom + gap;
            left = caret.left;
        } else if (placement === "above") {
            maxHeight = Math.min(preferredMax, Math.max(minListHeight, spaceAbove));
            top = lineTop - gap - maxHeight;
            if (top < viewportPad) {
                maxHeight = Math.max(minListHeight, lineTop - gap - viewportPad);
                top = lineTop - gap - maxHeight;
            }
            left = caret.left;
        } else {
            maxHeight = Math.min(preferredMax, window.innerHeight - viewportPad * 2);
            top = Math.max(viewportPad, Math.min(lineTop, window.innerHeight - maxHeight - viewportPad));
            left = textareaRect.right + gap;
        }

        listEl.style.width = `260px`;

        listEl.style.maxHeight = `${maxHeight}px`;
        layoutEl.style.top = `${top}px`;

        layoutEl.style.visibility = "hidden";
        layoutEl.style.left = "0px";

        const dropdownWidth = 260;
        left = Math.max(viewportPad, Math.min(left, window.innerWidth - dropdownWidth - viewportPad));

        layoutEl.style.left = `${left}px`;
        layoutEl.style.visibility = "";
    };

    const applySelected = () => {
        if (selectedIndex < 0 || selectedIndex >= items.length) return;
        const item = items[selectedIndex];
        const text = textarea.value;
        const before = text.slice(0, prefixInfo.start);
        const after = text.slice(textarea.selectionStart);

        textarea.value = before + item.insertText + after;
        textarea.selectionStart = textarea.selectionEnd = before.length + item.insertText.length;
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
            if (typeof maybeOpen === "function") {
                maybeOpen(true);
            } else {
                const text = textarea.value;
                const cursor = textarea.selectionStart;
                const prefix = getWordPrefix(text, cursor);
                if (prefix) {
                    const suggestions = buildSuggestions(prefix.word);
                    if (suggestions.length > 0) openWith(suggestions, prefix);
                }
            }
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

    const onReposition = () => {
        if (open) positionDropdown();
    };

    textarea.addEventListener("input", typeof onInput === "function" ? onInput : () => {
        const text = textarea.value;
        const cursor = textarea.selectionStart;
        const prefix = getWordPrefix(text, cursor);
        if (!prefix) { close(); return; }
        const suggestions = buildSuggestions(prefix.word);
        if (suggestions.length > 0) openWith(suggestions, prefix);
        else close();
    });

    textarea.addEventListener("keydown", onKeyDown);
    textarea.addEventListener("blur", onBlur);
    textarea.addEventListener("scroll", onReposition);

    window.addEventListener("scroll", onReposition, true);
    window.addEventListener("resize", onReposition);

    return {
        close,
        destroy() {
            close();
            window.removeEventListener("scroll", onReposition, true);
            window.removeEventListener("resize", onReposition);

            if (layoutEl) {
                layoutEl.remove();
            }
            textarea.removeEventListener("keydown", onKeyDown);
            textarea.removeEventListener("blur", onBlur);
            textarea.removeEventListener("scroll", onReposition);
            if (typeof onInput === "function") {
                textarea.removeEventListener("input", onInput);
            }
        },
    };
}

export { buildSuggestions, getWordPrefix, isCursorInStringOrComment, formatArgHint };