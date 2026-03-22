---
name: dotfiles-sync
description: Claude Code 설정을 GitHub dotfiles와 수동 동기화
user_invocable: true
invocation: dotfiles-sync
---

# Dotfiles Sync

Claude Code 설정(CLAUDE.md, settings, skills, templates)을 GitHub dotfiles repo와 즉시 동기화한다.

## 실행 절차

1. `bash ~/dotfiles/claude/sync.sh` 실행 (로컬 → dotfiles 복사)
2. `cd ~/dotfiles && git add -A && git status` 로 변경사항 확인
3. 변경이 있으면 `git commit -m 'manual sync' && git push` 실행
4. 변경이 없으면 "이미 최신 상태입니다" 출력

## 출력 형식

```
동기화 완료:
- CLAUDE.md: ✅
- settings.json: ✅
- skills: ✅ (N개)
- templates: ✅ (N개)
- GitHub push: ✅ (커밋 해시)
```
