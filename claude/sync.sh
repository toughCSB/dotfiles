#!/bin/bash
# Claude Code 설정 → dotfiles 동기화

DOTFILES_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Syncing ~/.claude -> dotfiles..."

if [ -f "$HOME/.claude/CLAUDE.md" ]; then
    cp "$HOME/.claude/CLAUDE.md" "$DOTFILES_DIR/CLAUDE.md" && echo "OK: CLAUDE.md"
else
    echo "SKIP: CLAUDE.md (not in ~/.claude, run install.sh first)"
fi

if [ -f "$HOME/.claude/claude-dashboard.local.json" ]; then
    cp "$HOME/.claude/claude-dashboard.local.json" "$DOTFILES_DIR/claude-dashboard.local.json" && echo "OK: claude-dashboard.local.json"
else
    echo "SKIP: claude-dashboard.local.json (not in ~/.claude)"
fi

python3 "$DOTFILES_DIR/sync_helper.py" "$DOTFILES_DIR"

echo ""
echo "Sync complete."
