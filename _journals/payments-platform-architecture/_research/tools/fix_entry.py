"""Replace text in one post's journal-spec entry and in its post spec, in step.

  python3 fix_entry.py <post-id> <old> <new>

Edits the fragment in _research/journal-spec-parts/, reassembles journal-spec.json and applies the
same replacement to the post's spec.json (intent, thesis, role only), then validates both.
"""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
pid, old, new = sys.argv[1:4]

def rep(o):
    if isinstance(o, str): return o.replace(old, new)
    if isinstance(o, list): return [rep(x) for x in o]
    if isinstance(o, dict): return {k: rep(v) for k, v in o.items()}
    return o

hit = False
for f in sorted((ROOT / "_research" / "journal-spec-parts").glob("*.json")):
    if f.name == "top.json": continue
    d = json.loads(f.read_text())
    for i, p in enumerate(d["posts"]):
        if p["id"] == pid:
            before = json.dumps(p, ensure_ascii=False)
            d["posts"][i] = rep(p)
            if json.dumps(d["posts"][i], ensure_ascii=False) == before:
                sys.exit(f"'{old}' not found in journal entry {pid}")
            f.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
            folder = p["folder"]; hit = True
if not hit: sys.exit("post id not found")
subprocess.run([sys.executable, str(ROOT / "_research/tools/assemble_journal_spec.py")], check=True)
sp = ROOT / "posts" / folder / "spec.json"
if sp.exists():
    s = json.loads(sp.read_text())
    for k in ("intent", "thesis", "role"):
        if k in s: s[k] = rep(s[k])
    s.setdefault("changelog", []).append({"date": "2026-11-17", "change": f"Journal-spec entry corrected after verification; intent, thesis and role re-synced ('{old[:60]}' -> '{new[:60]}')."})
    sp.write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n")
r = subprocess.run([sys.executable, "_wiring/validate_spec.py", "payments-platform-architecture", folder], cwd=REPO, capture_output=True, text=True)
print(r.stdout[-600:], r.stderr[-300:])
