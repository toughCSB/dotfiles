#!/bin/bash
# ============================================
# Claude Code 설정 설치 스크립트
# 새 PC에서 실행: bash install.sh
# ============================================

DOTFILES_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="$HOME/.claude"

echo "📁 Claude 설정 동기화 시작..."

# ~/.claude 디렉토리 존재 확인
if [ ! -d "$CLAUDE_DIR" ]; then
  echo "❌ ~/.claude 디렉토리가 없습니다. Claude Code를 먼저 설치하세요."
  exit 1
fi

# 파일 복사
cp "$DOTFILES_DIR/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md"
echo "✅ CLAUDE.md 복사 완료"

cp "$DOTFILES_DIR/claude-dashboard.local.json" "$CLAUDE_DIR/claude-dashboard.local.json"
echo "✅ claude-dashboard.local.json 복사 완료"

# settings.json: 기존 statusLine 보존하면서 나머지만 병합
SETTINGS_FILE="$CLAUDE_DIR/settings.json"
DOTFILES_SETTINGS="$DOTFILES_DIR/settings.json"

if [ -f "$SETTINGS_FILE" ]; then
  # 기존 statusLine 추출 후 dotfiles settings와 병합
  python3 -c "
import json, sys
with open('$SETTINGS_FILE') as f:
    existing = json.load(f)
with open('$DOTFILES_SETTINGS') as f:
    new = json.load(f)
# dotfiles 설정을 기본으로, 기존 statusLine 보존
merged = {**new}
if 'statusLine' in existing:
    merged['statusLine'] = existing['statusLine']
with open('$SETTINGS_FILE', 'w') as f:
    json.dump(merged, f, indent=2, ensure_ascii=False)
print('✅ settings.json 병합 완료 (statusLine 보존)')
"
else
  cp "$DOTFILES_SETTINGS" "$SETTINGS_FILE"
  echo "✅ settings.json 복사 완료"
fi

echo ""
echo "🎉 설치 완료!"
echo ""
echo "📌 다음 단계 (Claude Code에서):"
echo "  1. 플러그인 설치: plugins-list.txt 참고"
echo "  2. 대시보드 경로 갱신: /claude-dashboard:update"
