"""Claude Code dotfiles sync helper"""
import sys, json, os, shutil

sys.stdout.reconfigure(encoding="utf-8")

DOTFILES = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
DOTFILES = os.path.normpath(DOTFILES)
CLAUDE = os.path.normpath(os.path.expanduser("~/.claude"))

# settings.json: statusLine/hooks 제거 후 저장
src = os.path.join(CLAUDE, "settings.json")
dst = os.path.join(DOTFILES, "settings.json")
with open(src, encoding="utf-8") as f:
    s = json.load(f)
for key in ("statusLine", "hooks"):
    s.pop(key, None)
with open(dst, "w", encoding="utf-8") as f:
    json.dump(s, f, indent=2, ensure_ascii=False)
print("OK: settings.json (statusLine/hooks excluded)")

# skills 동기화
EXCLUDE = {"playwright-best-practices"}
skills_src = os.path.join(CLAUDE, "skills")
skills_dst = os.path.join(DOTFILES, "skills")
os.makedirs(skills_dst, exist_ok=True)

src_names = set(os.listdir(skills_src))
dst_names = set(os.listdir(skills_dst))

# 삭제된 스킬 제거
for name in dst_names - src_names:
    shutil.rmtree(os.path.join(skills_dst, name), ignore_errors=True)

# 추가/변경된 스킬 복사
count = 0
for name in src_names:
    if name in EXCLUDE:
        continue
    s = os.path.join(skills_src, name)
    d = os.path.join(skills_dst, name)
    if os.path.isdir(s):
        if os.path.exists(d):
            shutil.rmtree(d)
        shutil.copytree(s, d)
        count += 1

print(f"OK: skills/ ({count} skills synced)")

# templates 동기화
templates_src = os.path.join(CLAUDE, "templates")
templates_dst = os.path.join(DOTFILES, "templates")
if os.path.isdir(templates_src):
    if os.path.exists(templates_dst):
        shutil.rmtree(templates_dst)
    shutil.copytree(templates_src, templates_dst)
    print(f"OK: templates/ ({len(os.listdir(templates_dst))} templates synced)")

# commands 동기화
commands_src = os.path.join(CLAUDE, "commands")
commands_dst = os.path.join(DOTFILES, "commands")
if os.path.isdir(commands_src):
    if os.path.exists(commands_dst):
        shutil.rmtree(commands_dst)
    shutil.copytree(commands_src, commands_dst)
    print(f"OK: commands/ ({len(os.listdir(commands_dst))} commands synced)")

# agents 동기화
agents_src = os.path.join(CLAUDE, "agents")
agents_dst = os.path.join(DOTFILES, "agents")
if os.path.isdir(agents_src):
    if os.path.exists(agents_dst):
        shutil.rmtree(agents_dst)
    shutil.copytree(agents_src, agents_dst)
    print(f"OK: agents/ ({len(os.listdir(agents_dst))} agents synced)")
