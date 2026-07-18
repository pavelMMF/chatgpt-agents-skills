[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$errors = [System.Collections.Generic.List[string]]::new()

$skillDirs = Get-ChildItem -LiteralPath (Join-Path $repoRoot 'skills') -Directory
foreach ($skillDir in $skillDirs) {
    $skillFile = Join-Path $skillDir.FullName 'SKILL.md'
    if (-not (Test-Path -LiteralPath $skillFile)) {
        $errors.Add("Missing SKILL.md: $($skillDir.Name)")
        continue
    }

    $content = [System.IO.File]::ReadAllText($skillFile)
    $declaredName = [regex]::Match($content, '(?m)^name:\s*["'']?([^\r\n"'']+)').Groups[1].Value.Trim()
    if ($declaredName -ne $skillDir.Name) {
        $errors.Add("Name mismatch: folder '$($skillDir.Name)', frontmatter '$declaredName'")
    }
    if (-not [regex]::IsMatch($content, '(?m)^description:\s*\S')) {
        $errors.Add("Missing description: $($skillDir.Name)")
    }
}

$secretPattern = 'ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY'
$textExtensions = @('.md', '.toml', '.json', '.jsonl', '.yaml', '.yml', '.txt', '.py', '.ps1', '.js', '.ts', '.tsx', '.jsx', '.css', '.html', '.sh', '.csv')
Get-ChildItem -LiteralPath $repoRoot -Recurse -File -Force |
    Where-Object {
        $_.FullName -ne $PSCommandPath -and
        $_.FullName -notmatch '[\\/]\.git[\\/]' -and
        $textExtensions -contains $_.Extension.ToLowerInvariant()
    } |
    ForEach-Object {
        $content = [System.IO.File]::ReadAllText($_.FullName)
        $relativePath = $_.FullName.Substring($repoRoot.Length).TrimStart([char[]]'\/')
        if ([regex]::IsMatch($content, $secretPattern)) {
            $errors.Add("Possible secret: $relativePath")
        }
        if ($content -match 'C:\\Users\\lolip|C:/Users/lolip') {
            $errors.Add("Machine-specific path: $relativePath")
        }
    }

if ($errors.Count) {
    $errors | ForEach-Object { Write-Error $_ }
    exit 1
}

Write-Output "Validated $($skillDirs.Count) skills with no metadata, secret, or machine-path errors."
