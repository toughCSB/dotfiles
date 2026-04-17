"""Claude Code dotfiles install helper"""
import sys, json, os, shutil

sys.stdout.reconfigure(encoding="utf-8")

DOTFILES = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
DOTFILES = os.path.normpath(DOTFILES)
CLAUDE = os.path.normpath(os.path.expanduser("~/.claude"))

# settings.json: 기존 statusLine/hooks 보존하며 병합
settings_file = os.path.join(CLAUDE, "settings.json")
dotfiles_settings = os.path.join(DOTFILES, "settings.json")

with open(dotfiles_settings, encoding="utf-8") as f:
    new = json.load(f)

existing = {}
if os.path.exists(settings_file):
    with open(settings_file, encoding="utf-8") as f:
        existing = json.load(f)

merged = {**new}
for key in ("statusLine", "hooks"):
    if key in existing:
        merged[key] = existing[key]

with open(settings_file, "w", encoding="utf-8") as f:
    json.dump(merged, f, indent=2, ensure_ascii=False)
print("OK: settings.json merged (statusLine/hooks preserved)")

# skills 복사
skills_src = os.path.join(DOTFILES, "skills")
skills_dst = os.path.join(CLAUDE, "skills")
if os.path.isdir(skills_src):
    os.makedirs(skills_dst, exist_ok=True)
    count = 0
    for name in os.listdir(skills_src):
        s = os.path.join(skills_src, name)
        d = os.path.join(skills_dst, name)
        if os.path.isdir(s):
            if os.path.islink(d):
                os.unlink(d)
            elif os.path.exists(d):
                shutil.rmtree(d, onerror=rm_readonly)
            shutil.copytree(s, d)
            count += 1
    print(f"OK: skills/ ({count} skills installed)")

# templates 복원
templates_src = os.path.join(DOTFILES, "templates")
templates_dst = os.path.join(CLAUDE, "templates")
if os.path.isdir(templates_src):
    os.makedirs(templates_dst, exist_ok=True)
    count = 0
    for name in os.listdir(templates_src):
        s = os.path.join(templates_src, name)
        d = os.path.join(templates_dst, name)
        shutil.copy2(s, d)
        count += 1
    print(f"OK: templates/ ({count} templates installed)")

# commands 복원
commands_src = os.path.join(DOTFILES, "commands")
commands_dst = os.path.join(CLAUDE, "commands")
if os.path.isdir(commands_src):
    if os.path.islink(commands_dst):
        os.unlink(commands_dst)
    elif os.path.exists(commands_dst):
        shutil.rmtree(commands_dst)
    shutil.copytree(commands_src, commands_dst)
    print(f"OK: commands/ ({len(os.listdir(commands_dst))} commands installed)")

# agents 복원
agents_src = os.path.join(DOTFILES, "agents")
agents_dst = os.path.join(CLAUDE, "agents")
if os.path.isdir(agents_src):
    if os.path.islink(agents_dst):
        os.unlink(agents_dst)
    elif os.path.exists(agents_dst):
        shutil.rmtree(agents_dst)
    shutil.copytree(agents_src, agents_dst)
    print(f"OK: agents/ ({len(os.listdir(agents_dst))} agents installed)")

# 자동 동기화 훅 등록 (없는 경우에만)
with open(settings_file, encoding="utf-8") as f:
    s = json.load(f)

if "hooks" not in s:
    s["hooks"] = {
        "SessionStart": [{"hooks": [{"type": "command",
            "command": "cd ~/dotfiles && git pull --ff-only 2>/dev/null; bash ~/dotfiles/claude/install.sh 2>/dev/null; echo '[dotfiles] synced'"}]}],
        "Stop": [{"hooks": [{"type": "command",
            "command": "bash ~/dotfiles/claude/sync.sh 2>/dev/null && cd ~/dotfiles && (git diff --quiet && git diff --cached --quiet) || (git add -A && git commit -m 'auto sync' && git push)"}]}]
    }
    with open(settings_file, "w", encoding="utf-8") as f:
        json.dump(s, f, indent=2, ensure_ascii=False)
    print("OK: auto-sync hooks registered")
else:
    print("INFO: hooks already exist, skipped")
