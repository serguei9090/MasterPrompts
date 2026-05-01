#!/usr/bin/env pwsh
# =============================================================================
# Morphic AI Engineering Framework — Windows Bootstrap Installer
# Usage: ./scripts/install.ps1 [-SkipCognee] [-SkipCodanna] [-Quiet]
# =============================================================================
param(
    [switch]$SkipCognee,
    [switch]$SkipCodanna,
    [switch]$Quiet
)

$ErrorActionPreference = "Continue"
$VERSION = "0.10.7"

# ── Helpers ───────────────────────────────────────────────────────────────────
function Write-Step { param($Msg) Write-Host "`n  ▸ $Msg" -ForegroundColor Cyan }
function Write-Ok   { param($Msg) Write-Host "    ✅  $Msg" -ForegroundColor Green }
function Write-Warn { param($Msg) Write-Host "    ⚠️  $Msg" -ForegroundColor Yellow }
function Write-Fail { param($Msg) Write-Host "    ❌  $Msg" -ForegroundColor Red }
function Write-Info { param($Msg) if (-not $Quiet) { Write-Host "       $Msg" -ForegroundColor Gray } }

function Test-Command {
    param($Name)
    return [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

function Install-WithWinget {
    param($PackageId, $FriendlyName)
    if (-not (Test-Command "winget")) {
        Write-Warn "$FriendlyName: winget not available — install manually"
        return $false
    }
    Write-Info "Installing $FriendlyName via winget..."
    winget install $PackageId --accept-package-agreements --accept-source-agreements --silent 2>&1 | Out-Null
    return $true
}

# ─── Banner ───────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "  ╔═══════════════════════════════════════════════════╗" -ForegroundColor DarkCyan
Write-Host "  ║   Morphic AI Engineering Framework v$VERSION       ║" -ForegroundColor DarkCyan
Write-Host "  ║   Windows Bootstrap Installer (PowerShell)        ║" -ForegroundColor DarkCyan
Write-Host "  ╚═══════════════════════════════════════════════════╝" -ForegroundColor DarkCyan
Write-Host ""

$ROOT = (Get-Item $PSScriptRoot).Parent.FullName
Set-Location $ROOT
Write-Info "Project root: $ROOT"

# ─── 1. Dolt (Beads Database Engine) ─────────────────────────────────────────
Write-Step "Checking Dolt (Beads database engine)..."
if (Test-Command "dolt") {
    $doltVer = (dolt version 2>&1 | Select-String "dolt" | Select-Object -First 1)
    Write-Ok "Dolt already installed: $doltVer"
} else {
    Write-Info "Installing Dolt via winget..."
    $ok = Install-WithWinget "DoltHub.Dolt" "Dolt"
    if ($ok -and (Test-Command "dolt")) {
        Write-Ok "Dolt installed"
    } else {
        Write-Fail "Dolt install failed. Manual: https://docs.dolthub.com/introduction/installation"
    }
}

# ─── 2. Node.js ──────────────────────────────────────────────────────────────
Write-Step "Checking Node.js..."
if (Test-Command "node") {
    $nodeVer = node --version
    Write-Ok "Node.js already installed: $nodeVer"
} else {
    Write-Info "Installing Node.js LTS via winget..."
    Install-WithWinget "OpenJS.NodeJS.LTS" "Node.js LTS" | Out-Null
    if (Test-Command "node") {
        Write-Ok "Node.js installed: $(node --version)"
    } else {
        Write-Fail "Node.js install failed. Manual: https://nodejs.org"
    }
}

# ─── 3. Beads (bd) ───────────────────────────────────────────────────────────
Write-Step "Checking Beads (bd) CLI..."
if (Test-Command "bd") {
    Write-Ok "Beads (bd) already installed"
} else {
    if (Test-Command "npm") {
        Write-Info "Installing @beads/bd globally via npm..."
        npm install -g @beads/bd 2>&1 | Out-Null
        if (Test-Command "bd") {
            Write-Ok "Beads (bd) installed"
        } else {
            Write-Fail "Beads install failed. Try: npm install -g @beads/bd"
        }
    } else {
        Write-Fail "npm not available — install Node.js first, then run: npm install -g @beads/bd"
    }
}

# ─── 4. Bun ──────────────────────────────────────────────────────────────────
Write-Step "Checking Bun (JS runtime)..."
if (Test-Command "bun") {
    Write-Ok "Bun already installed: $(bun --version)"
} else {
    Write-Info "Installing Bun via npm..."
    if (Test-Command "npm") {
        npm install -g bun 2>&1 | Out-Null
    }
    if (Test-Command "bun") {
        Write-Ok "Bun installed: $(bun --version)"
    } else {
        Write-Warn "Bun not installed. Optional but recommended. Install: https://bun.sh"
    }
}

# ─── 5. uv (Python package manager) ─────────────────────────────────────────
Write-Step "Checking uv (Python package manager)..."
if (Test-Command "uv") {
    Write-Ok "uv already installed: $(uv --version)"
} else {
    Write-Info "Installing uv via pip..."
    if (Test-Command "pip") {
        pip install uv --quiet
    } elseif (Test-Command "pip3") {
        pip3 install uv --quiet
    } else {
        Write-Info "pip not found — trying PowerShell installer..."
        try {
            Invoke-RestMethod "https://astral.sh/uv/install.ps1" | Invoke-Expression 2>&1 | Out-Null
        } catch {
            Write-Warn "uv auto-install failed. Manual: https://docs.astral.sh/uv/getting-started/installation/"
        }
    }
    if (Test-Command "uv") {
        Write-Ok "uv installed: $(uv --version)"
    } else {
        Write-Fail "uv not installed. Required for Python deps and Cognee."
    }
}

# ─── 6. Python venv + dependencies ───────────────────────────────────────────
Write-Step "Setting up Python virtual environment..."
if (-not (Test-Path ".venv")) {
    if (Test-Command "uv") {
        uv venv 2>&1 | Out-Null
        Write-Ok "Created .venv via uv"
    } else {
        Write-Warn ".venv not created — uv not available"
    }
} else {
    Write-Ok ".venv already exists"
}

if (Test-Path "pyproject.toml") {
    Write-Info "Installing Python project dependencies..."
    if (Test-Command "uv") {
        uv sync --quiet 2>&1 | Out-Null
        Write-Ok "Python deps synced (uv sync)"
    }
}

# ─── 7. Cognee ───────────────────────────────────────────────────────────────
if (-not $SkipCognee) {
    Write-Step "Checking Cognee (semantic memory)..."
    $cogneeCheck = uv run python -c "import cognee; print('ok')" 2>&1
    if ($cogneeCheck -match "ok") {
        Write-Ok "Cognee already installed in venv"
    } else {
        Write-Info "Installing Cognee via uv..."
        if (Test-Path "pyproject.toml") {
            uv add cognee --quiet 2>&1 | Out-Null
        } else {
            uv pip install cognee --quiet 2>&1 | Out-Null
        }
        $cogneeCheck2 = uv run python -c "import cognee; print('ok')" 2>&1
        if ($cogneeCheck2 -match "ok") {
            Write-Ok "Cognee installed"
        } else {
            Write-Fail "Cognee install failed. Docs: docs/cognee_install.md"
        }
    }
}

# ─── 8. Codanna ──────────────────────────────────────────────────────────────
if (-not $SkipCodanna) {
    Write-Step "Checking Codanna (physical code analysis)..."
    if (Test-Command "codanna") {
        Write-Ok "Codanna already installed: $(codanna --version 2>&1 | Select-Object -First 1)"
    } else {
        Write-Info "Attempting to install Codanna via uv..."
        uv pip install codanna --quiet 2>&1 | Out-Null
        if (Test-Command "codanna") {
            Write-Ok "Codanna installed"
        } else {
            Write-Warn "Codanna not available via pip. Check: https://docs.codanna.sh/installation"
            Write-Info "You can skip Codanna features with -SkipCodanna flag"
        }
    }
}

# ─── 9. Lefthook (Git Hooks) ─────────────────────────────────────────────────
Write-Step "Checking Lefthook (Git hooks)..."
if (Test-Command "lefthook") {
    Write-Ok "Lefthook already installed"
} else {
    if (Test-Command "npm") {
        Write-Info "Installing lefthook globally via npm..."
        npm install -g @arkweid/lefthook 2>&1 | Out-Null
        if (Test-Command "lefthook") {
            Write-Ok "Lefthook installed"
        } else {
            Write-Warn "Lefthook install failed. Try: npm install -g @arkweid/lefthook"
        }
    } else {
        Write-Warn "Lefthook not installed — npm not available"
    }
}

# Install hooks into the repo
if (Test-Command "lefthook") {
    Write-Info "Activating git hooks..."
    lefthook install 2>&1 | Out-Null
    Write-Ok "Git hooks installed (lefthook)"
}

# ─── 10. Framework Directory Structure ───────────────────────────────────────
Write-Step "Ensuring framework directory structure..."
$dirs = @(
    ".agents/rules",
    ".agents/workflows",
    ".agents/skills",
    ".gemini/agents",
    ".gemini/commands",
    "docs/track/specs",
    "docs/memory/specs",
    "docs/memory/architecture",
    "docs/memory/lessons",
    "docs/architecture"
)
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Info "Created $dir"
    }
}
Write-Ok "Directory structure verified"

# ─── 11. Environment File ─────────────────────────────────────────────────────
Write-Step "Checking .env file..."
if (-not (Test-Path ".env")) {
    if (Test-Path ".env.example") {
        Copy-Item ".env.example" ".env"
        Write-Ok "Created .env from .env.example — fill in your API keys!"
    } else {
        Write-Warn ".env.example not found — create .env manually"
    }
} else {
    Write-Ok ".env already exists"
}

# ─── 12. .gitignore Guards ────────────────────────────────────────────────────
Write-Step "Verifying .gitignore entries..."
$gitignoreEntries = @(".cognee/", ".env", ".venv/", "__pycache__/", "dist/", "*.pyc")
$gitignoreContent = if (Test-Path ".gitignore") { Get-Content ".gitignore" -Raw } else { "" }
$added = @()
foreach ($entry in $gitignoreEntries) {
    if ($gitignoreContent -notmatch [regex]::Escape($entry)) {
        Add-Content ".gitignore" "`n$entry"
        $added += $entry
    }
}
if ($added.Count -gt 0) {
    Write-Ok "Added to .gitignore: $($added -join ', ')"
} else {
    Write-Ok ".gitignore entries already present"
}

# ─── Summary ──────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "  ╔═══════════════════════════════════════════════════╗" -ForegroundColor DarkGreen
Write-Host "  ║   Bootstrap complete — Morphic v$VERSION          ║" -ForegroundColor DarkGreen
Write-Host "  ╚═══════════════════════════════════════════════════╝" -ForegroundColor DarkGreen
Write-Host ""
Write-Host "  Next steps:" -ForegroundColor White
Write-Host "   1. Fill in your API keys in .env" -ForegroundColor Gray
Write-Host "   2. Run: bd init  (first time only)" -ForegroundColor Gray
Write-Host "   3. Run: codanna init && codanna index ." -ForegroundColor Gray
Write-Host "   4. Run: uv run python scripts/cognee/indexer.py --full" -ForegroundColor Gray
Write-Host "   5. Run the /init workflow in your AI assistant to complete setup" -ForegroundColor Gray
Write-Host ""
