Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "1/2 Compiling ANTLR Grammars" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan

Write-Host "Compiling legacy version (ANTLR 4.9.3)..." -ForegroundColor Yellow
antlr4 -v 4.9.3 -Dlanguage=Python3 -visitor -o ./legacy MathExpr.g4

Write-Host "Compiling modern version (ANTLR 4.13.2)..." -ForegroundColor Yellow
antlr4 -v 4.13.2 -Dlanguage=Python3 -visitor -o ./grammer MathExpr.g4

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "2/2 Generating Python and JS Token Sets" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan

$g4Path = "MathExpr.g4"
if (-not (Test-Path $g4Path)) {
    Write-Error "MathExpr.g4 not found!"
    exit 1
}

# 1. Načtení a očištění gramatiky od komentářů
$content = [System.IO.File]::ReadAllText($g4Path, [System.Text.Encoding]::UTF8)
$content = $content -replace '//.*', ''
$content = $content -replace '/\*[\s\S]*?\*/', ''

# 2. Vytažení všech alfabetických řetězců v apostrofech
$matches = [regex]::Matches($content, "'([a-zA-Z_][a-zA-Z0-9_]*)'")
$allSymbols = @()
foreach ($m in $matches) {
    $allSymbols += $m.Groups[1].Value
}
$allSymbols = $allSymbols | Sort-Object -Unique

# 3. Definice pevných množin
$keywords = @('if', 'else', 'while', 'for', 'in', 'break', 'continue', 'return', 'none', 'None', 'null', 'NULL') | Sort-Object -Unique
$constants = @('pi', 'PI', 'e', 'E') | Sort-Object -Unique

# Vše ostatní, co jsou slova a nejsou klíčová slova ani konstanty, jsou funkce
$functions = @()
foreach ($sym in $allSymbols) {
    if ($sym -notin $keywords -and $sym -notin $constants) {
        $functions += $sym
    }
}
$functions = $functions | Sort-Object -Unique

# 4. Formátování a zápis do PYTHON souboru (do kořene/aktuální složky vedle .g4)
$pyPath = "inbuilt_symbols.py"
$pyContent = @(
    "# Generated automatically by compile.ps1. Do not edit.",
    "INBUILT_KEYWORDS = {" + (($keywords | foreach { "'$_'" }) -join ", ") + "}",
    "INBUILT_CONSTANTS = {" + (($constants | foreach { "'$_'" }) -join ", ") + "}",
    "INBUILT_FUNCTIONS = {" + (($functions | foreach { "'$_'" }) -join ", ") + "}"
) -join [Environment]::NewLine

[System.IO.File]::WriteAllText($pyPath, $pyContent, [System.Text.Encoding]::UTF8)
Write-Host "-> Exported Python symbols to root: $pyPath" -ForegroundColor Green

# 5. Formátování a zápis do JAVASCRIPT souboru (odskok do složky web)
# Pokud máš složku web hned vedle .g4, změň '..\web' na 'web'
$jsDir = "..\..\web" 
if (-not (Test-Path $jsDir)) {
    New-Item -ItemType Directory -Force -Path $jsDir | Out-Null
}
$jsPath = Join-Path $jsDir "inbuilt_symbols.js"

$jsContent = @(
    "// Generated automatically by compile.ps1. Do not edit.",
    "",
    "export const KEYWORDS = new Set([" + (($keywords | foreach { "`"$_`"" }) -join ", ") + "]);",
    "",
    "export const CONSTANTS = new Set([" + (($constants | foreach { "`"$_`"" }) -join ", ") + "]);",
    "",
    "export const FUNCTIONS = new Set([" + (($functions | foreach { "`"$_`"" }) -join ", ") + "]);"
) -join [Environment]::NewLine

[System.IO.File]::WriteAllText($jsPath, $jsContent, [System.Text.Encoding]::UTF8)
Write-Host "-> Exported JS symbols to: $jsPath" -ForegroundColor Green

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "Compilation and Generation Successful!" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan
