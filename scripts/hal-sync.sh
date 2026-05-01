#!/usr/bin/env bash
# =============================================================================
# HAL Sync — Resolve agents.yaml variables into the current shell session
# Usage: source ./scripts/hal-sync.sh   (to export to calling shell)
#        bash ./scripts/hal-sync.sh     (prints export commands only)
# =============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
HAL_FILE="$PROJECT_ROOT/agents.yaml"

if [ ! -f "$HAL_FILE" ]; then
    echo "[HAL] ERROR: agents.yaml not found at: $HAL_FILE" >&2
    return 1 2>/dev/null || exit 1
fi

echo "  [HAL] Syncing environment from agents.yaml..."

section=""
count=0

while IFS= read -r line || [ -n "$line" ]; do
    # Detect top-level section headers (no leading whitespace)
    if [[ "$line" =~ ^([a-zA-Z_][a-zA-Z0-9_]*):\ *$ ]]; then
        section="${BASH_REMATCH[1]}"
        continue
    fi

    # Parse key-value pairs inside the "variables" section
    # Handles: KEY: "value"  and  KEY: value
    if [[ "$section" == "variables" ]] && [[ "$line" =~ ^[[:space:]]+([A-Z_]+):[[:space:]]+"?([^"]+)"?[[:space:]]*$ ]]; then
        var_name="${BASH_REMATCH[1]}"
        var_value="${BASH_REMATCH[2]}"
        var_value="${var_value%\"}"  # strip trailing quote if present

        # Resolve "." to absolute project root
        if [ "$var_value" = "." ]; then
            var_value="$PROJECT_ROOT"
        elif [[ "$var_value" != /* ]]; then
            var_value="$PROJECT_ROOT/$var_value"
        fi

        # Export the variable
        export "$var_name=$var_value"
        echo "  [HAL]   $var_name = $var_value"
        (( count++ )) || true
    fi
done < "$HAL_FILE"

echo "  [HAL] Sync complete. $count variable(s) exported."
