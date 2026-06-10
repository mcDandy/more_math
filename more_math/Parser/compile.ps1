param(
    [switch]$SkipAntlr
)

if (-not $SkipAntlr) {
    Write-Host "===================================================" -ForegroundColor Cyan
    Write-Host "1/2 Compiling ANTLR Grammars" -ForegroundColor Cyan
    Write-Host "===================================================" -ForegroundColor Cyan

    Write-Host "Compiling legacy version (ANTLR 4.9.3)..." -ForegroundColor Yellow
    antlr4 -v 4.9.3 -Dlanguage=Python3 -visitor -o ./legacy MathExpr.g4

    Write-Host "Compiling modern version (ANTLR 4.13.2)..." -ForegroundColor Yellow
    antlr4 -v 4.13.2 -Dlanguage=Python3 -visitor -o ./grammer MathExpr.g4
}

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "2/2 Generating Python and JS Token Sets" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan

$g4Path = "MathExpr.g4"
if (-not (Test-Path $g4Path)) {
    Write-Error "MathExpr.g4 not found!"
    exit 1
}

$rawContent = [System.IO.File]::ReadAllText($g4Path, [System.Text.Encoding]::UTF8)
$content = $rawContent -replace '//.*', ''
$content = $content -replace '/\*[\s\S]*?\*/', ''

function Get-LexerNames([string]$grammarText) {
    $map = @{}
    foreach ($line in ($grammarText -split "`r?`n")) {
        $t = $line.Trim()
        if ($t -notmatch '^([A-Z][A-Z0-9_]*)\s*:\s*(.+);\s*$') { continue }
        $token = $matches[1]
        $rhs = $matches[2]
        $names = @(
            [regex]::Matches($rhs, "'([^']*)'") | ForEach-Object { $_.Groups[1].Value.ToLower() }
        ) | Sort-Object -Unique
        if ($names.Count -gt 0) {
            $map[$token] = $names
        }
    }
    return $map
}

function Get-ArgBounds([string]$inner) {
    $inner = $inner.Trim()
    if ([string]::IsNullOrWhiteSpace($inner)) {
        return @{ min = 0; max = 0 }
    }

    $exprCount = ([regex]::Matches($inner, '\b(expr|indexExpr)\b')).Count
    $optExpr = 0
    foreach ($g in [regex]::Matches($inner, '\([^()]*\)\?')) {
        $optExpr += ([regex]::Matches($g.Value, '\b(expr|indexExpr)\b')).Count
    }

    $hasStar = $inner -match '\(COMMA (expr|indexExpr)\)\*'
    $hasPlus = $inner -match '\(COMMA (expr|indexExpr)\)\+'

    $min = $exprCount - $optExpr
    if ($hasStar) {
        $min = [Math]::Max(1, $exprCount - 1 - $optExpr)
        return @{ min = $min; max = $null }
    }
    if ($hasPlus) {
        $min = [Math]::Max(1, $exprCount - $optExpr)
        return @{ min = $min; max = $null }
    }

    return @{ min = $min; max = $exprCount }
}

function New-Snippet([string]$name) {
    return "${name}()"
}

function Add-FunctionRuleLine([hashtable]$meta, [hashtable]$lexerMap, [string]$line) {
    $clean = (($line -split '\s+#')[0]).Trim().TrimEnd(';')
    if ($clean -notmatch 'LPAREN') { return }
    if ($clean -notmatch '(?:^\s*\|\s*)?(\w+)\s+LPAREN\s*(.*?)\s+RPAREN\s*$') { return }

    $token = $matches[1]
    $inner = $matches[2].Trim()
    $bounds = Get-ArgBounds $inner
    $names = $lexerMap[$token]
    if (-not $names) { return }

    foreach ($fn in $names) {
        $entry = @{
            minArgs = $bounds.min
            snippet = (New-Snippet $fn)
        }
        if ($null -eq $bounds.max) {
            $entry.maxArgs = $null
        } else {
            $entry.maxArgs = $bounds.max
        }
        $meta[$fn] = $entry
    }
}

function Get-FunctionMeta([string]$grammarText, [hashtable]$lexerMap) {
    $meta = @{}
    $inFunc = $false

    foreach ($line in ($grammarText -split "`r?`n")) {
        if ($line -match '^\s*//\s*LEXER') { $inFunc = $false }
        if ($line -match '^\s*(func0|func1|func2|func3|func4|func5|funcN|funcNoise)\s*:\s*(.*)$') {
            $inFunc = $true
            $inline = $matches[2].Trim()
            if ($inline -and $inline -match 'LPAREN') {
                Add-FunctionRuleLine $meta $lexerMap $inline
            }
            continue
        }
        if (-not $inFunc) { continue }

        Add-FunctionRuleLine $meta $lexerMap $line
    }

    return $meta
}

# 1. Extract quoted symbols for keyword/function lists
$matches = [regex]::Matches($content, "'([a-zA-Z_][a-zA-Z0-9_]*)'")
$allSymbols = @()
foreach ($m in $matches) {
    $allSymbols += $m.Groups[1].Value
}
$allSymbols = $allSymbols | Sort-Object -Unique

# 2. Fixed sets
$keywords = @('if', 'else', 'while', 'for', 'in', 'break', 'continue', 'return', 'none', 'None', 'null', 'NULL') | Sort-Object -Unique
$constants = @('pi', 'PI', 'e', 'E') | Sort-Object -Unique

$functions = @()
foreach ($sym in $allSymbols) {
    if ($sym -notin $keywords -and $sym -notin $constants) {
        $functions += $sym.ToLower()
    }
}
$functions = $functions | Sort-Object -Unique

# 3. Function metadata from grammar rules
$lexerMap = Get-LexerNames $content
$functionMeta = Get-FunctionMeta $content $lexerMap

# Ensure every listed function has meta (fallback: variadic unknown)
foreach ($fn in $functions) {
    if (-not $functionMeta.ContainsKey($fn)) {
        $functionMeta[$fn] = @{
            minArgs = 1
            maxArgs = $null
            snippet = (New-Snippet $fn)
        }
    }
}

$sortedMetaKeys = $functionMeta.Keys | Sort-Object

# 4. Python export
$pyMetaLines = @()
foreach ($key in $sortedMetaKeys) {
    $m = $functionMeta[$key]
    $maxPart = if ($null -eq $m.maxArgs) { "None" } else { [string]$m.maxArgs }
    $pyMetaLines += "    '$key': {'min_args': $($m.minArgs), 'max_args': $maxPart, 'snippet': '$($m.snippet)'},"
}

$pyPath = "inbuilt_symbols.py"
$pyContent = @(
    "# Generated automatically by compile.ps1. Do not edit.",
    "INBUILT_KEYWORDS = {" + (($keywords | ForEach-Object { "'$_'" }) -join ", ") + "}",
    "INBUILT_CONSTANTS = {" + (($constants | ForEach-Object { "'$_'" }) -join ", ") + "}",
    "INBUILT_FUNCTIONS = {" + (($functions | ForEach-Object { "'$_'" }) -join ", ") + "}",
    "",
    "INBUILT_FUNCTION_META = {",
    ($pyMetaLines -join [Environment]::NewLine),
    "}"
) -join [Environment]::NewLine

[System.IO.File]::WriteAllText($pyPath, $pyContent, [System.Text.Encoding]::UTF8)
Write-Host "-> Exported Python symbols to root: $pyPath" -ForegroundColor Green

# 5. JavaScript export
$jsDir = "..\..\web"
if (-not (Test-Path $jsDir)) {
    New-Item -ItemType Directory -Force -Path $jsDir | Out-Null
}
$jsPath = Join-Path $jsDir "inbuilt_symbols.js"

$jsMetaLines = @()
foreach ($key in $sortedMetaKeys) {
    $m = $functionMeta[$key]
    if ($null -eq $m.maxArgs) {
        $jsMetaLines += "    $key`: { minArgs: $($m.minArgs), maxArgs: null, snippet: `"$($m.snippet)`" },"
    } else {
        $jsMetaLines += "    $key`: { minArgs: $($m.minArgs), maxArgs: $($m.maxArgs), snippet: `"$($m.snippet)`" },"
    }
}

$jsContent = @(
    "// Generated automatically by compile.ps1. Do not edit.",
    "",
    "export const KEYWORDS = new Set([" + (($keywords | ForEach-Object { "`"$_`"" }) -join ", ") + "]);",
    "",
    "export const CONSTANTS = new Set([" + (($constants | ForEach-Object { "`"$_`"" }) -join ", ") + "]);",
    "",
    "export const FUNCTIONS = new Set([" + (($functions | ForEach-Object { "`"$_`"" }) -join ", ") + "]);",
    "",
    "export const FUNCTION_META = {",
    ($jsMetaLines -join [Environment]::NewLine),
    "};"
) -join [Environment]::NewLine

[System.IO.File]::WriteAllText($jsPath, $jsContent, [System.Text.Encoding]::UTF8)
Write-Host "-> Exported JS symbols to: $jsPath" -ForegroundColor Green
Write-Host "-> Function metadata entries: $($sortedMetaKeys.Count)" -ForegroundColor Green

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "Compilation and Generation Successful!" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan
