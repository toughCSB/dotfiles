#!/bin/bash
# Claude Code 설정 설치 스크립트 (새 PC에서 실행)
set -e

DOTFILES_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ ! -d "$HOME/.claude" ]; then
  echo "ERROR: ~/.claude not found. Install Claude Code first."
  exit 1
fi

echo "Installing Claude Code settings..."

cp "$DOTFILES_DIR/CLAUDE.md" "$HOME/.claude/CLAUDE.md" && echo "OK: CLAUDE.md"
cp "$DOTFILES_DIR/claude-dashboard.local.json" "$HOME/.claude/claude-dashboard.local.json" && echo "OK: claude-dashboard.local.json"

python3 "$DOTFILES_DIR/install_helper.py" "$DOTFILES_DIR"

echo ""
echo "Done!"
echo "Next steps in Claude Code:"
echo "  1. Install plugins (see plugins-list.txt)"
echo "  2. Run /claude-dashboard:update"
