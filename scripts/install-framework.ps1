#!/usr/bin/env pwsh
# =============================================================================
# DEPRECATED: This script has been superseded by scripts/install.ps1
# =============================================================================
# This file is kept for backward compatibility only.
# The new installer handles Dolt, Node, Beads, uv, Cognee, Codanna, and 
# Lefthook automatically with platform detection and idempotent behavior.
#
# Please use:  ./scripts/install.ps1
# =============================================================================

Write-Host ""
Write-Host "  ⚠️  NOTICE: install-framework.ps1 is deprecated." -ForegroundColor Yellow
Write-Host "  Please use the new unified installer instead:" -ForegroundColor Yellow
Write-Host ""
Write-Host "     ./scripts/install.ps1" -ForegroundColor Cyan
Write-Host ""
Write-Host "  The new installer handles all tools (Dolt, Beads, uv, Cognee," -ForegroundColor Gray
Write-Host "  Codanna, Lefthook) with full idempotency and platform detection." -ForegroundColor Gray
Write-Host ""

$confirm = Read-Host "  Run ./scripts/install.ps1 now? (Y/n)"
if ($confirm -ne "n" -and $confirm -ne "N") {
    & "$PSScriptRoot/install.ps1" @args
} else {
    Write-Host "  Exiting. Run ./scripts/install.ps1 when ready." -ForegroundColor Gray
}
