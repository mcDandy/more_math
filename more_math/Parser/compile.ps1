<#
.SYNOPSIS
    Build script for the more_math ANTLR grammar and its generated symbol tables.

.DESCRIPTION
    1. Compiles more_math/Parser/MathExpr.g4 into more_math/Parser/grammer
       (the parser antlr_router.py loads for current antlr4-python3-runtime
       versions), using whatever ANTLR toolchain is available on this
       machine (an 'antlr4' launcher on PATH, or 'java -jar <jar>').
    2. Parses MathExpr.g4 itself (keywords, constants, function tokens and
       their doc-comment signatures/descriptions) and regenerates:
         - more_math/Parser/inbuilt_symbols.py
         - web/inbuilt_symbols.js
       so that the Python interpreter and the web autocomplete UI both read
       an up-to-date, identical view of the language's built-in symbols.

.PARAMETER SkipAntlr
    Skip step 1 (grammar compilation) and only regenerate the symbol tables.

.PARAMETER AntlrJar
    Path to an antlr-*-complete.jar to use for step 1. Defaults to
    $env:ANTLR_JAR, then tools\antlr.jar next to this script.

.PARAMETER AntlrLegacyJar
    Optional path to an ANTLR 4.9.x complete jar. When given (and Java is
    available), also regenerates more_math/Parser/legacy for the old
    antlr4-python3-runtime==4.9.x compatibility path used by antlr_router.py.
    Defaults to $env:ANTLR_LEGACY_JAR. Skipped entirely if not supplied.

.PARAMETER AntlrVersion
    ANTLR release to use when the 'antlr4' launcher comes from the
    antlr4-tools pip package (it otherwise queries Maven Central for the
    latest release on every run). Defaults to $env:ANTLR4_TOOLS_ANTLR_VERSION,
    then '4.13.2' to match the version more_math/Parser/grammer was last
    generated with. Ignored when using a plain jar/java invocation.
#>
[CmdletBinding()]
param(
    [switch]$SkipAntlr,
    [string]$AntlrJar = $env:ANTLR_JAR,
    [string]$AntlrLegacyJar = $env:ANTLR_LEGACY_JAR,
    [string]$AntlrVersion = $(if ($env:ANTLR4_TOOLS_ANTLR_VERSION) { $env:ANTLR4_TOOLS_ANTLR_VERSION } else { '4.13.2' })
)

$ErrorActionPreference = 'Stop'

# This script lives at more_math/Parser/compile.ps1, two levels under the
# node root (more_math/Parser -> more_math -> node root).
$ParserDir     = $PSScriptRoot
$NodeRoot      = Split-Path (Split-Path $ParserDir -Parent) -Parent
$GrammarFile   = Join-Path $ParserDir 'MathExpr.g4'
$GrammarOutDir = Join-Path $ParserDir 'grammer'
$LegacyOutDir  = Join-Path $ParserDir 'legacy'
$WebDir        = Join-Path $NodeRoot 'web'
$PySymbolsPath = Join-Path $ParserDir 'inbuilt_symbols.py'
$JsSymbolsPath = Join-Path $WebDir 'inbuilt_symbols.js'

if (-not (Test-Path $GrammarFile)) {
    throw "Grammar file not found: $GrammarFile"
}

# ---------------------------------------------------------------------------
# Step 1: ANTLR compilation
# ---------------------------------------------------------------------------

function Invoke-AntlrCompile {
    # Runs with cwd = $ParserDir and passes ANTLR just the grammar's leaf
    # filename, so the "# Generated from MathExpr.g4 by ANTLR ..." header it
    # writes into the output files stays a plain relative name instead of
    # embedding this machine's local absolute path.
    param(
        [Parameter(Mandatory)][string]$Grammar,
        [Parameter(Mandatory)][string]$OutDir,
        [string]$Jar
    )

    $grammarLeaf = Split-Path -Leaf $Grammar

    $antlrCmd = Get-Command antlr4 -ErrorAction SilentlyContinue
    if ($antlrCmd) {
        # antlr4-tools (the pip-installed launcher) otherwise hits Maven
        # Central on every invocation to resolve "latest"; pin it so the
        # build is reproducible and doesn't need that network call.
        $previousVersionEnv = $env:ANTLR4_TOOLS_ANTLR_VERSION
        $env:ANTLR4_TOOLS_ANTLR_VERSION = $AntlrVersion
        Push-Location $ParserDir
        try {
            Write-Host "[antlr] antlr4 (v$AntlrVersion) -Dlanguage=Python3 -visitor -o `"$OutDir`" `"$grammarLeaf`""
            & $antlrCmd.Source -Dlanguage=Python3 -visitor -o $OutDir $grammarLeaf
            if ($LASTEXITCODE -ne 0) { throw "antlr4 failed with exit code $LASTEXITCODE" }
        } finally {
            Pop-Location
            $env:ANTLR4_TOOLS_ANTLR_VERSION = $previousVersionEnv
        }
        return $true
    }

    $javaCmd = Get-Command java -ErrorAction SilentlyContinue
    if (-not $javaCmd) {
        return $false
    }

    if (-not $Jar) {
        $default = Join-Path $NodeRoot 'tools\antlr.jar'
        if (Test-Path $default) { $Jar = $default }
    }

    if (-not $Jar -or -not (Test-Path $Jar)) {
        return $false
    }

    Push-Location $ParserDir
    try {
        Write-Host "[antlr] java -jar `"$Jar`" -Dlanguage=Python3 -visitor -o `"$OutDir`" `"$grammarLeaf`""
        & $javaCmd.Source -jar $Jar -Dlanguage=Python3 -visitor -o $OutDir $grammarLeaf
        if ($LASTEXITCODE -ne 0) { throw "ANTLR jar invocation failed with exit code $LASTEXITCODE" }
    } finally {
        Pop-Location
    }
    return $true
}

if ($SkipAntlr) {
    Write-Host "[antlr] Skipping grammar compilation (-SkipAntlr)."
} else {
    $ok = Invoke-AntlrCompile -Grammar $GrammarFile -OutDir $GrammarOutDir -Jar $AntlrJar
    if (-not $ok) {
        Write-Warning ("ANTLR toolchain not found (no 'antlr4' on PATH and no usable jar). " +
            "Skipping grammar compilation; '$GrammarOutDir' was left untouched. " +
            "Install Java + antlr4-tools ('pip install antlr4-tools'), or set `$env:ANTLR_JAR " +
            "to an antlr-*-complete.jar, then re-run.")
    }

    if ($AntlrLegacyJar) {
        if (Test-Path $AntlrLegacyJar) {
            $javaCmd = Get-Command java -ErrorAction SilentlyContinue
            if ($javaCmd) {
                $grammarLeaf = Split-Path -Leaf $GrammarFile
                Push-Location $ParserDir
                try {
                    Write-Host "[antlr] java -jar `"$AntlrLegacyJar`" -Dlanguage=Python3 -visitor -o `"$LegacyOutDir`" `"$grammarLeaf`" (ANTLR 4.9 target)"
                    & $javaCmd.Source -jar $AntlrLegacyJar -Dlanguage=Python3 -visitor -o $LegacyOutDir $grammarLeaf
                    if ($LASTEXITCODE -ne 0) { throw "Legacy ANTLR jar invocation failed with exit code $LASTEXITCODE" }
                } finally {
                    Pop-Location
                }
            } else {
                Write-Warning "AntlrLegacyJar was given but Java is not available; skipping legacy grammar regeneration."
            }
        } else {
            Write-Warning "AntlrLegacyJar '$AntlrLegacyJar' does not exist; skipping legacy grammar regeneration."
        }
    }
}

# ---------------------------------------------------------------------------
# Step 2: parse MathExpr.g4 for its built-in symbol table
# ---------------------------------------------------------------------------

function Get-GrammarSections {
    param([Parameter(Mandatory)][string]$Text)

    $funcStart = $Text.IndexOf('func0:')
    $lexerMarker = '// LEXER RULES'
    $lexerStart = $Text.IndexOf($lexerMarker)
    if ($funcStart -lt 0 -or $lexerStart -lt 0 -or $lexerStart -le $funcStart) {
        throw "Could not locate expected grammar sections ('func0:' / '$lexerMarker') - has MathExpr.g4's layout changed?"
    }

    [pscustomobject]@{
        FuncSection  = $Text.Substring($funcStart, $lexerStart - $funcStart)
        LexerSection = $Text.Substring($lexerStart)
    }
}

function Get-LexerTokens {
    # Returns an ordered map of TOKEN_NAME -> raw string-literal alternatives,
    # for every lexer rule that defines at least one word-like literal
    # (i.e. skips punctuation/operator tokens and regex-only tokens like
    # NUMBER/STRING/VARIABLE/WS/comments, which have no literal alternatives).
    param([Parameter(Mandatory)][string]$LexerSection)

    $tokenRegex = [regex]'(?ms)^[ \t]*([A-Z][A-Z0-9_]*)[ \t]*:[ \t]*(.*?);'
    $literalRegex = [regex]"'([a-zA-Z_][a-zA-Z0-9_]*)'"

    $tokens = [ordered]@{}
    foreach ($m in $tokenRegex.Matches($LexerSection)) {
        $name = $m.Groups[1].Value
        $body = $m.Groups[2].Value
        $literals = @($literalRegex.Matches($body) | ForEach-Object { $_.Groups[1].Value })
        if ($literals.Count -gt 0) {
            $tokens[$name] = $literals
        }
    }
    return $tokens
}

function Get-FunctionTokenNames {
    # A token counts as a "function" token when it is used as `TOKEN LPAREN`
    # inside the func0..funcNoise rules (the atom productions for calls).
    # This deliberately excludes structural keywords like IF/WHILE/FOR, which
    # are also followed by LPAREN but in ifStmt/whileStmt/forStmt, outside
    # this section.
    param([Parameter(Mandatory)][string]$FuncSection)

    $names = New-Object System.Collections.Generic.HashSet[string]
    foreach ($m in [regex]::Matches($FuncSection, '\b([A-Z][A-Z0-9_]*)\s+LPAREN\b')) {
        [void]$names.Add($m.Groups[1].Value)
    }
    return $names
}

function Get-UniqueLowerWords {
    # De-duplicates literal alternatives that only differ by case (e.g.
    # 'pi'/'PI', 'none'/'None'/'null'/'NULL') down to one lowercase spelling
    # per distinct word, preserving first-seen order.
    param([string[]]$Words)

    $seen = New-Object System.Collections.Generic.HashSet[string]
    $result = New-Object System.Collections.Generic.List[string]
    foreach ($w in $Words) {
        $lw = $w.ToLowerInvariant()
        if ($seen.Add($lw)) { [void]$result.Add($lw) }
    }
    return $result
}

function Get-FunctionDocEntries {
    # Pairs each `/** ... */` doc comment in the func section with the
    # lexer token of the call it documents (the `TOKEN LPAREN` that follows
    # the comment, skipping over an optional leading `|` alternation).
    param([Parameter(Mandatory)][string]$FuncSection)

    $pattern = [regex]'(?s)/\*\*(?<doc>.*?)\*/\s*\|?\s*(?<token>[A-Z][A-Z0-9_]*)\s+LPAREN'
    $entries = New-Object System.Collections.Generic.List[object]
    foreach ($m in $pattern.Matches($FuncSection)) {
        $lines = @($m.Groups['doc'].Value -split "`r?`n" | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' })
        if ($lines.Count -eq 0) { continue }
        $entries.Add([pscustomobject]@{
            Token     = $m.Groups['token'].Value
            FirstLine = $lines[0]
        })
    }
    return $entries
}

function Split-ArgSpec {
    # Parses a comma-separated arg list like "x, [dims]" or "x, ..." into
    # min/max argument counts and display names (brackets/ellipsis stripped).
    param([string]$ArgsText)

    if ([string]::IsNullOrWhiteSpace($ArgsText)) {
        return [pscustomobject]@{ Min = 0; Max = 0; Variadic = $false; Display = @() }
    }

    $min = 0
    $max = 0
    $variadic = $false
    $display = New-Object System.Collections.Generic.List[string]

    foreach ($raw in ($ArgsText -split ',')) {
        $p = $raw.Trim()
        if ($p -eq '') { continue }
        if ($p -eq '...') { $variadic = $true; [void]$display.Add('...'); continue }
        $isOptional = $p.StartsWith('[') -and $p.EndsWith(']')
        $clean = $p.Trim('[', ']').Trim()
        [void]$display.Add($clean)
        $max++
        if (-not $isOptional) { $min++ }
    }

    [pscustomobject]@{ Min = $min; Max = $max; Variadic = $variadic; Display = $display.ToArray() }
}

function ConvertTo-FunctionSignature {
    # Parses a doc-comment first line such as:
    #   "sum(x, [dims]) - computes the sum of elements of x, ..."
    #   "rgb_to_hsv(rgb, [degrees]) / rgb_to_hsv(r, g, b, [degrees]) - converts ..."
    # into arg-count bounds, display arg names (from the first signature) and
    # the trailing description text.
    param([Parameter(Mandatory)][string]$Line)

    $sigMatch = [regex]::Match($Line, '^[a-zA-Z_][a-zA-Z0-9_]*\((?<args>.*?)\)')
    if (-not $sigMatch.Success) { return $null }

    $rest = $Line.Substring($sigMatch.Index + $sigMatch.Length)
    $spec1 = Split-ArgSpec -ArgsText $sigMatch.Groups['args'].Value

    # Some functions document two call forms separated by " / "; fold the
    # second form's bounds in so min/max cover both (e.g. rgb_to_hsv).
    $altMatch = [regex]::Match($rest, '^\s*/\s*[a-zA-Z_][a-zA-Z0-9_]*\((?<args>.*?)\)')
    $spec2 = $null
    if ($altMatch.Success) {
        $spec2 = Split-ArgSpec -ArgsText $altMatch.Groups['args'].Value
        $rest = $rest.Substring($altMatch.Index + $altMatch.Length)
    }

    $descMatch = [regex]::Match($rest, '^\s*-\s*(?<desc>.*)$')
    $desc = if ($descMatch.Success) { $descMatch.Groups['desc'].Value.Trim() } else { $rest.Trim() }

    $min = $spec1.Min
    $variadic = $spec1.Variadic
    $max = $spec1.Max
    if ($spec2) {
        if ($spec2.Min -lt $min) { $min = $spec2.Min }
        if ($spec2.Variadic) { $variadic = $true }
        if ($spec2.Max -gt $max) { $max = $spec2.Max }
    }

    [pscustomobject]@{
        MinArgs     = $min
        MaxArgs     = if ($variadic) { $null } else { $max }
        ArgNames    = $spec1.Display
        Description = $desc
    }
}

Write-Host "[symbols] Parsing $GrammarFile"
$grammarText = Get-Content -Raw -LiteralPath $GrammarFile
$sections = Get-GrammarSections -Text $grammarText
$allTokens = Get-LexerTokens -LexerSection $sections.LexerSection
$functionTokenNames = Get-FunctionTokenNames -FuncSection $sections.FuncSection

$constantWords = @()
$keywordWords = New-Object System.Collections.Generic.List[string]
$functionWords = New-Object System.Collections.Generic.List[string]
$functionTokenToWords = [ordered]@{}

$tokenNames = @($allTokens.psbase.Keys)
foreach ($name in $tokenNames) {
    $words = Get-UniqueLowerWords -Words $allTokens[$name]
    if ($name -eq 'CONSTANT') {
        $constantWords = $words
        continue
    }
    if ($functionTokenNames.Contains($name)) {
        $functionTokenToWords[$name] = $words
        foreach ($w in $words) { [void]$functionWords.Add($w) }
    } else {
        foreach ($w in $words) { [void]$keywordWords.Add($w) }
    }
}

$KEYWORDS  = @($keywordWords  | Sort-Object -Unique)
$CONSTANTS = @($constantWords | Sort-Object -Unique)
$FUNCTIONS = @($functionWords | Sort-Object -Unique)

$docEntries = Get-FunctionDocEntries -FuncSection $sections.FuncSection
$sigByToken = @{}
foreach ($e in $docEntries) {
    $sig = ConvertTo-FunctionSignature -Line $e.FirstLine
    if ($sig) { $sigByToken[$e.Token] = $sig }
}

$functionTokens = @($functionTokenToWords.psbase.Keys)
$undocumented = @($functionTokens | Where-Object { -not $sigByToken.ContainsKey($_) })
if ($undocumented.Count -gt 0) {
    Write-Warning "No parsable doc comment found for function token(s): $($undocumented -join ', '). They will get placeholder metadata."
}

$FUNCTION_META = [ordered]@{}
foreach ($token in $functionTokens) {
    $sig = $sigByToken[$token]
    foreach ($alias in $functionTokenToWords[$token]) {
        if ($sig) {
            $snippet = if ($sig.ArgNames.Count -gt 0) { "$alias($($sig.ArgNames -join ', '))" } else { "$alias()" }
            $FUNCTION_META[$alias] = [pscustomobject]@{
                MinArgs     = $sig.MinArgs
                MaxArgs     = $sig.MaxArgs
                Snippet     = $snippet
                Description = $sig.Description
            }
        } else {
            $FUNCTION_META[$alias] = [pscustomobject]@{
                MinArgs     = 0
                MaxArgs     = $null
                Snippet     = "$alias()"
                Description = ''
            }
        }
    }
}

# ---------------------------------------------------------------------------
# Step 3: emit the generated files
# ---------------------------------------------------------------------------

function Set-Utf8NoBom {
    # Windows PowerShell 5.1's Set-Content has no utf8NoBOM encoding, so write
    # the file directly via .NET to avoid a BOM in the generated .py/.js files.
    param([string]$Path, [string]$Content)
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

function ConvertTo-JsString {
    param([string]$Value)
    $escaped = $Value.Replace('\', '\\').Replace('"', '\"')
    return '"' + $escaped + '"'
}

function ConvertTo-PyString {
    param([string]$Value)
    $escaped = $Value.Replace('\', '\\').Replace("'", "\'")
    return "'" + $escaped + "'"
}

function Write-JsSymbols {
    param(
        [string]$Path,
        [string[]]$Keywords,
        [string[]]$Constants,
        [string[]]$Functions,
        [System.Collections.Specialized.OrderedDictionary]$FunctionMeta
    )

    $sb = New-Object System.Text.StringBuilder
    [void]$sb.AppendLine('// Generated automatically by compile.ps1. Do not edit.')
    [void]$sb.AppendLine()
    [void]$sb.AppendLine('export const KEYWORDS = new Set([')
    [void]$sb.AppendLine(($Keywords  | ForEach-Object { ConvertTo-JsString $_ }) -join ', ')
    [void]$sb.AppendLine(']);')
    [void]$sb.AppendLine()
    [void]$sb.AppendLine('export const CONSTANTS = new Set([')
    [void]$sb.AppendLine(($Constants | ForEach-Object { ConvertTo-JsString $_ }) -join ', ')
    [void]$sb.AppendLine(']);')
    [void]$sb.AppendLine()
    [void]$sb.AppendLine('export const FUNCTIONS = new Set([')
    [void]$sb.AppendLine(($Functions | ForEach-Object { ConvertTo-JsString $_ }) -join ', ')
    [void]$sb.AppendLine(']);')
    [void]$sb.AppendLine()
    [void]$sb.AppendLine('export const FUNCTION_META = {')
    foreach ($name in @($FunctionMeta.psbase.Keys)) {
        $meta = $FunctionMeta[$name]
        $maxArgsJs = if ($null -eq $meta.MaxArgs) { 'null' } else { $meta.MaxArgs }
        [void]$sb.AppendLine("    $(ConvertTo-JsString $name): { minArgs: $($meta.MinArgs), maxArgs: $maxArgsJs, snippet: $(ConvertTo-JsString $meta.Snippet), description: $(ConvertTo-JsString $meta.Description) },")
    }
    [void]$sb.AppendLine('};')

    Set-Utf8NoBom -Path $Path -Content $sb.ToString()
}

function Write-PySymbols {
    param(
        [string]$Path,
        [string[]]$Keywords,
        [string[]]$Constants,
        [string[]]$Functions,
        [System.Collections.Specialized.OrderedDictionary]$FunctionMeta
    )

    $sb = New-Object System.Text.StringBuilder
    [void]$sb.AppendLine('# Generated automatically by compile.ps1. Do not edit.')
    [void]$sb.AppendLine('INBUILT_KEYWORDS = {')
    [void]$sb.AppendLine(($Keywords  | ForEach-Object { ConvertTo-PyString $_ }) -join ', ')
    [void]$sb.AppendLine('}')
    [void]$sb.AppendLine('INBUILT_CONSTANTS = {')
    [void]$sb.AppendLine(($Constants | ForEach-Object { ConvertTo-PyString $_ }) -join ', ')
    [void]$sb.AppendLine('}')
    [void]$sb.AppendLine('INBUILT_FUNCTIONS = {')
    [void]$sb.AppendLine(($Functions | ForEach-Object { ConvertTo-PyString $_ }) -join ', ')
    [void]$sb.AppendLine('}')
    [void]$sb.AppendLine()
    [void]$sb.AppendLine('INBUILT_FUNCTION_META = {')
    foreach ($name in @($FunctionMeta.psbase.Keys)) {
        $meta = $FunctionMeta[$name]
        $maxArgsPy = if ($null -eq $meta.MaxArgs) { 'None' } else { $meta.MaxArgs }
        [void]$sb.AppendLine("    $(ConvertTo-PyString $name): {'min_args': $($meta.MinArgs), 'max_args': $maxArgsPy, 'snippet': $(ConvertTo-PyString $meta.Snippet), 'description': $(ConvertTo-PyString $meta.Description)},")
    }
    [void]$sb.AppendLine('}')

    Set-Utf8NoBom -Path $Path -Content $sb.ToString()
}

Write-Host "[symbols] Writing $PySymbolsPath"
Write-PySymbols -Path $PySymbolsPath -Keywords $KEYWORDS -Constants $CONSTANTS -Functions $FUNCTIONS -FunctionMeta $FUNCTION_META

Write-Host "[symbols] Writing $JsSymbolsPath"
Write-JsSymbols -Path $JsSymbolsPath -Keywords $KEYWORDS -Constants $CONSTANTS -Functions $FUNCTIONS -FunctionMeta $FUNCTION_META

Write-Host "[symbols] $($FUNCTIONS.Count) functions, $($KEYWORDS.Count) keywords, $($CONSTANTS.Count) constants."
Write-Host 'Done.'
