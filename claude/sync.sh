#!/bin/bash
# ============================================
# Claude Code 설정 → dotfiles 동기화
# 집/회사 PC에서 설정 변경 후 실행: bash sync.sh
# ============================================

DOTFILES_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="$HOME/.claude"

echo "🔄 ~/.claude → dotfiles 동기화 중..."

cp "$CLAUDE_DIR/CLAUDE.md" "$DOTFILES_DIR/CLAUDE.md"
echo "✅ CLAUDE.md"

cp "$CLAUDE_DIR/claude-dashboard.local.json" "$DOTFILES_DIR/claude-dashboard.local.json"
echo "✅ claude-dashboard.local.json"

# settings.json: statusLine 제거 후 저장 (머신별 경로 제외)
python3 -c "
import json
with open('$CLAUDE_DIR/settings.json') as f:
    s = json.load(f)
s.pop('statusLine', None)  # 머신별 경로 제거
with open('$DOTFILES_DIR/settings.json', 'w') as f:
    json.dump(s, f, indent=2, ensure_ascii=False)
print('✅ settings.json (statusLine 제외)')
"

echo ""
echo "✅ 동기화 완료! 이제 git commit & push 하세요:"
echo "  cd ~/dotfiles && git add -A && git commit -m 'sync claude settings' && git push"
