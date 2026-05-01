#!/usr/bin/env bash
# =============================================================================
# Morphic AI Engineering Framework — Linux / macOS Bootstrap Installer
# Usage: bash ./scripts/install.sh [--skip-cognee] [--skip-codanna] [--quiet]
# =============================================================================
set -euo pipefail

VERSION="0.10.7"
SKIP_COGNEE=false
SKIP_CODANNA=false
QUIET=false

for arg in "$@"; do
  case "$arg" in
    --skip-cognee)  SKIP_COGNEE=true ;;
    --skip-codanna) SKIP_CODANNA=true ;;
    --quiet)        QUIET=true ;;
  esac
done

# ── Helpers ───────────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
CYAN='\033[0;36m'; GRAY='\033[0;37m'; NC='\033[0m'

step() { echo -e "\n  ${CYAN}▸ $1${NC}"; }
ok()   { echo -e "    ${GREEN}✅  $1${NC}"; }
warn() { echo -e "    ${YELLOW}⚠️  $1${NC}"; }
fail() { echo -e "    ${RED}❌  $1${NC}"; }
info() { if [ "$QUIET" = false ]; then echo -e "    ${GRAY}   $1${NC}"; fi; }

has() { command -v "$1" &>/dev/null; }

detect_os() {
  case "$(uname -s)" in
    Linux*)  echo "linux" ;;
    Darwin*) echo "mac" ;;
    *)       echo "unknown" ;;
  esac
}

OS=$(detect_os)
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# ─── Banner ───────────────────────────────────────────────────────────────────
echo ""
echo -e "  ${CYAN}╔═══════════════════════════════════════════════════╗${NC}"
echo -e "  ${CYAN}║   Morphic AI Engineering Framework v${VERSION}       ║${NC}"
echo -e "  ${CYAN}║   Linux / macOS Bootstrap Installer (Bash)        ║${NC}"
echo -e "  ${CYAN}╚═══════════════════════════════════════════════════╝${NC}"
echo ""
info "Project root: $ROOT"
info "OS detected: $OS"

# ─── 1. Dolt (Beads Database Engine) ─────────────────────────────────────────
step "Checking Dolt (Beads database engine)..."
if has dolt; then
    ok "Dolt already installed: $(dolt version | head -1)"
else
    info "Installing Dolt..."
    if [ "$OS" = "mac" ] && has brew; then
        brew install dolt 2>/dev/null && ok "Dolt installed via Homebrew" || fail "Dolt install failed"
    else
        # Official Linux installer
        curl -L https://github.com/dolthub/dolt/releases/latest/download/install.sh | sudo bash 2>/dev/null \
            && ok "Dolt installed" \
            || fail "Dolt install failed. Manual: https://docs.dolthub.com/introduction/installation"
    fi
fi

# ─── 2. Node.js ──────────────────────────────────────────────────────────────
step "Checking Node.js..."
if has node; then
    ok "Node.js already installed: $(node --version)"
else
    if has nvm; then
        info "Installing Node.js LTS via nvm..."
        nvm install --lts 2>/dev/null && ok "Node.js installed via nvm" || warn "nvm install failed"
    elif [ "$OS" = "mac" ] && has brew; then
        brew install node 2>/dev/null && ok "Node.js installed via Homebrew" || fail "Node.js install failed"
    else
        info "Installing Node.js via NodeSource (apt)..."
        curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - 2>/dev/null
        sudo apt-get install -y nodejs 2>/dev/null \
            && ok "Node.js installed: $(node --version)" \
            || fail "Node.js install failed. Manual: https://nodejs.org"
    fi
fi

# ─── 3. Beads (bd) ───────────────────────────────────────────────────────────
step "Checking Beads (bd) CLI..."
if has bd; then
    ok "Beads (bd) already installed"
else
    if has npm; then
        info "Installing @beads/bd globally via npm..."
        npm install -g @beads/bd 2>/dev/null \
            && ok "Beads (bd) installed" \
            || fail "Beads install failed. Try: npm install -g @beads/bd"
    else
        fail "npm not available — install Node.js first, then: npm install -g @beads/bd"
    fi
fi

# ─── 4. Bun ──────────────────────────────────────────────────────────────────
step "Checking Bun (JS runtime)..."
if has bun; then
    ok "Bun already installed: $(bun --version)"
else
    info "Installing Bun via official installer..."
    curl -fsSL https://bun.sh/install | bash 2>/dev/null \
        && export PATH="$HOME/.bun/bin:$PATH" \
        && ok "Bun installed: $(bun --version 2>/dev/null || echo 'restart shell to use')" \
        || warn "Bun not installed. Optional but recommended: https://bun.sh"
fi

# ─── 5. uv (Python package manager) ─────────────────────────────────────────
step "Checking uv (Python package manager)..."
if has uv; then
    ok "uv already installed: $(uv --version)"
else
    info "Installing uv via official installer..."
    curl -LsSf https://astral.sh/uv/install.sh | sh 2>/dev/null \
        && export PATH="$HOME/.cargo/bin:$PATH" \
        || true
    # Try pip fallback
    if ! has uv; then
        if has pip3; then pip3 install uv --quiet 2>/dev/null; fi
    fi
    if has uv; then
        ok "uv installed: $(uv --version)"
    else
        fail "uv not installed. Manual: https://docs.astral.sh/uv/getting-started/installation/"
    fi
fi

# ─── 6. Python venv + dependencies ───────────────────────────────────────────
step "Setting up Python virtual environment..."
if [ ! -d ".venv" ]; then
    if has uv; then
        uv venv 2>/dev/null && ok "Created .venv via uv" || warn "venv creation failed"
    else
        warn ".venv not created — uv not available"
    fi
else
    ok ".venv already exists"
fi

if [ -f "pyproject.toml" ] && has uv; then
    info "Installing Python project dependencies..."
    uv sync --quiet 2>/dev/null && ok "Python deps synced (uv sync)" || warn "uv sync failed"
fi

# ─── 7. Cognee ───────────────────────────────────────────────────────────────
if [ "$SKIP_COGNEE" = false ]; then
    step "Checking Cognee (semantic memory)..."
    cognee_check=$(uv run python -c "import cognee; print('ok')" 2>&1 || true)
    if echo "$cognee_check" | grep -q "ok"; then
        ok "Cognee already installed in venv"
    else
        info "Installing Cognee..."
        if [ -f "pyproject.toml" ]; then
            uv add cognee --quiet 2>/dev/null || true
        else
            uv pip install cognee --quiet 2>/dev/null || true
        fi
        cognee_check2=$(uv run python -c "import cognee; print('ok')" 2>&1 || true)
        if echo "$cognee_check2" | grep -q "ok"; then
            ok "Cognee installed"
        else
            fail "Cognee install failed. See docs/cognee_install.md"
        fi
    fi
fi

# ─── 8. Codanna ──────────────────────────────────────────────────────────────
if [ "$SKIP_CODANNA" = false ]; then
    step "Checking Codanna (physical code analysis)..."
    if has codanna; then
        ok "Codanna already installed: $(codanna --version 2>&1 | head -1)"
    else
        info "Attempting to install Codanna via uv..."
        uv pip install codanna --quiet 2>/dev/null || true
        if has codanna; then
            ok "Codanna installed"
        else
            warn "Codanna not available via pip. Check: https://docs.codanna.sh/installation"
        fi
    fi
fi

# ─── 9. Lefthook ─────────────────────────────────────────────────────────────
step "Checking Lefthook (Git hooks)..."
if has lefthook; then
    ok "Lefthook already installed"
else
    if has npm; then
        info "Installing lefthook via npm..."
        npm install -g @arkweid/lefthook 2>/dev/null \
            && ok "Lefthook installed" \
            || warn "Lefthook install failed. Try: npm install -g @arkweid/lefthook"
    elif [ "$OS" = "mac" ] && has brew; then
        brew install lefthook 2>/dev/null && ok "Lefthook installed via Homebrew" || warn "Lefthook install failed"
    else
        warn "Lefthook not installed — npm not available"
    fi
fi

if has lefthook && [ -f "lefthook.yml" ]; then
    info "Activating git hooks..."
    lefthook install 2>/dev/null && ok "Git hooks installed (lefthook)" || warn "lefthook install failed"
fi

# ─── 10. Directory Structure ──────────────────────────────────────────────────
step "Ensuring framework directory structure..."
dirs=(
    ".agents/rules"
    ".agents/workflows"
    ".agents/skills"
    ".gemini/agents"
    ".gemini/commands"
    "docs/track/specs"
    "docs/memory/specs"
    "docs/memory/architecture"
    "docs/memory/lessons"
    "docs/architecture"
)
for d in "${dirs[@]}"; do
    if [ ! -d "$d" ]; then
        mkdir -p "$d"
        info "Created $d"
    fi
done
ok "Directory structure verified"

# ─── 11. Environment File ─────────────────────────────────────────────────────
step "Checking .env file..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp ".env.example" ".env"
        ok "Created .env from .env.example — fill in your API keys!"
    else
        warn ".env.example not found — create .env manually"
    fi
else
    ok ".env already exists"
fi

# ─── 12. .gitignore Guards ────────────────────────────────────────────────────
step "Verifying .gitignore entries..."
gitignore_entries=(".cognee/" ".env" ".venv/" "__pycache__/" "dist/" "*.pyc")
added=()
for entry in "${gitignore_entries[@]}"; do
    if [ ! -f ".gitignore" ] || ! grep -qF "$entry" ".gitignore" 2>/dev/null; then
        echo "$entry" >> .gitignore
        added+=("$entry")
    fi
done
if [ ${#added[@]} -gt 0 ]; then
    ok "Added to .gitignore: ${added[*]}"
else
    ok ".gitignore entries already present"
fi

# ─── File permissions ─────────────────────────────────────────────────────────
chmod +x scripts/install.sh 2>/dev/null || true
chmod +x scripts/hal-sync.sh 2>/dev/null || true

# ─── Summary ──────────────────────────────────────────────────────────────────
echo ""
echo -e "  ${GREEN}╔═══════════════════════════════════════════════════╗${NC}"
echo -e "  ${GREEN}║   Bootstrap complete — Morphic v${VERSION}          ║${NC}"
echo -e "  ${GREEN}╚═══════════════════════════════════════════════════╝${NC}"
echo ""
echo "  Next steps:"
echo "   1. Fill in your API keys in .env"
echo "   2. Run: bd init  (first time only)"
echo "   3. Run: codanna init && codanna index ."
echo "   4. Run: uv run python scripts/cognee/indexer.py --full"
echo "   5. Run the /init workflow in your AI assistant to complete setup"
echo ""
