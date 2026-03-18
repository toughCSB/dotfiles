#!/bin/bash
# Claude Code 설정 → dotfiles 동기화
set -e

DOTFILES_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Syncing ~/.claude -> dotfiles..."

cp "$HOME/.claude/CLAUDE.md" "$DOTFILES_DIR/CLAUDE.md" && echo "OK: CLAUDE.md"
cp "$HOME/.claude/claude-dashboard.local.json" "$DOTFILES_DIR/claude-dashboard.local.json" && echo "OK: claude-dashboard.local.json"

python3 "$DOTFILES_DIR/sync_helper.py" "$DOTFILES_DIR"

echo ""
echo "Done. Now run:"
echo "  cd ~/dotfiles && git add -A && git commit -m 'sync claude settings' && git push"
