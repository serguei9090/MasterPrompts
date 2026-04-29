# Morphic Framework: Safe Installer
# Usage: ./scripts/install-framework.ps1

$governanceFiles = @(
    @{ template = "shipping/AGENTS.template.md"; target = "AGENTS.md" },
    @{ template = "shipping/GEMINI.template.md"; target = "GEMINI.md" },
    @{ template = "shipping/lefthook.template.yml"; target = "lefthook.yml" },
    @{ template = "shipping/README.template.md"; target = "README.md" },
    @{ template = "shipping/.env.template.example"; target = ".env.example" }
)

Write-Host "🚀 Initializing Morphic AI Engineering Framework..." -ForegroundColor Cyan

# 1. Create Core Directory Structure
$dirs = @(".agents/rules", ".agents/workflows", ".gemini/agents", "docs/track/specs", "docs/memory")
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "  [+] Created $dir" -ForegroundColor Gray
    }
}

# 2. Deploy Governance Files (Safe Mode)
foreach ($file in $governanceFiles) {
    $template = $file.template
    $target = $file.target

    if (Test-Path $target) {
        $newTarget = "$target.new"
        Copy-Item -Path $template -Destination $newTarget -Force
        Write-Host "  [!] WARNING: $target already exists. Created $newTarget for manual review." -ForegroundColor Yellow
    } else {
        Copy-Item -Path $template -Destination $target -Force
        Write-Host "  [+] Installed $target" -ForegroundColor Green
    }
}

Write-Host "`n✅ Framework core initialized. Please review any .new files and merge manually." -ForegroundColor Cyan
Write-Host "Next steps: Run 'codanna init' and 'bd init' to activate the intelligence stack." -ForegroundColor Gray
