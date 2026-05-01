#!/usr/bin/env pwsh
# =============================================================================
# HAL Sync — Resolve agents.yaml variables into the current PowerShell session
# Usage: . ./scripts/hal-sync.ps1   (dot-source to export to calling shell)
#        ./scripts/hal-sync.ps1     (run directly — sets Process-scope env vars)
# =============================================================================

$halFile = Join-Path (Get-Item $PSScriptRoot).Parent.FullName "agents.yaml"

if (-not (Test-Path $halFile)) {
    Write-Error "HAL configuration file not found at: $halFile"
    exit 1
}

# Derive the project root (parent of /scripts)
$projectRoot = (Get-Item $PSScriptRoot).Parent.FullName

Write-Host "  [HAL] Syncing environment from agents.yaml..." -ForegroundColor Cyan

$section       = ""
$resolvedVars  = @{}

Get-Content $halFile | ForEach-Object {
    $line = $_.TrimEnd()

    # Detect top-level section headers (no leading spaces)
    if ($line -match '^(\w[\w_]*):\s*$') {
        $section = $matches[1]
        return
    }

    # Parse key-value pairs inside the "variables" section
    # Handles both: KEY: "value"  and  KEY: value
    if ($section -eq "variables" -and $line -match '^\s+(\w+):\s+"?([^"]+)"?\s*$') {
        $varName  = $matches[1].Trim()
        $varValue = $matches[2].Trim().Trim('"')

        # Resolve "." to the absolute project root
        if ($varValue -eq ".") {
            $varValue = $projectRoot
        } elseif (-not [System.IO.Path]::IsPathRooted($varValue)) {
            $varValue = Join-Path $projectRoot $varValue
        }

        $resolvedVars[$varName] = $varValue

        # Set for the current process
        [System.Environment]::SetEnvironmentVariable($varName, $varValue, "Process")

        # Also set as a PowerShell variable so dot-sourced callers can use $ROOT etc.
        Set-Variable -Name $varName -Value $varValue -Scope Global -Force

        Write-Host "  [HAL]   $varName = $varValue" -ForegroundColor Gray
    }
}

# Convenience: expose as $env:ROOT, $env:AGENTS, $env:DOCS, $env:TRACK
foreach ($key in $resolvedVars.Keys) {
    Set-Item -Path "env:$key" -Value $resolvedVars[$key] -Force
}

Write-Host "  [HAL] Sync complete. $($resolvedVars.Count) variable(s) exported." -ForegroundColor Green
