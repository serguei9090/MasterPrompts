# Assume Role: @devops
# Purpose: Sync HAL variables to the current environment session.

$halFile = "agents.yaml"
if (-not (Test-Path $halFile)) {
    Write-Error "HAL configuration file not found at $halFile"
    exit 1
}

# Simple YAML parser for the variables section (assuming flat structure for variables)
$variablesFound = $false
Get-Content $halFile | ForEach-Object {
    if ($_ -match "^variables:") {
        $variablesFound = $true
    } elseif ($variablesFound -and $_ -match "^\s+(\w+):\s+`"(.+)`"") {
        $varName = $matches[1]
        $varValue = $matches[2]
        
        # Resolve "." to absolute path
        if ($varValue -eq ".") {
            $varValue = (Get-Item $PSScriptRoot).Parent.FullName
        } else {
            $varValue = Join-Path (Get-Item $PSScriptRoot).Parent.FullName $varValue
        }

        Write-Host "Setting ENV:$varName to $varValue"
        [System.Environment]::SetEnvironmentVariable($varName, $varValue, "Process")
    } elseif ($variablesFound -and $_ -match "^\S") {
        $variablesFound = $false
    }
}

Write-Host "HAL environment sync complete."
