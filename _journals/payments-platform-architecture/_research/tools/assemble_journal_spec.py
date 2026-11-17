"""Assemble journal-spec.json from _research/journal-spec-parts/top.json and one fragment per part.

  python3 assemble_journal_spec.py                 # write ../../journal-spec.json from all fragments
  python3 assemble_journal_spec.py --only part-3 --check
        # build a scratch spec holding only that part, validate it against the schema, and print
        # the errors that concern it (errors caused by the other parts being absent are dropped)

Standard library only. Uses the repository's own validator (_wiring/outcome_specs.py).
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[2]                      # the journal folder
REPO = ROOT.parents[1]
PARTS_DIR = ROOT / "_research" / "journal-spec-parts"
ORDER = ["preface"] + [f"part-{i}" for i in range(1, 11)] + ["reference"]

sys.path.insert(0, str(REPO / "_wiring"))


def load(only=None):
    spec = json.loads((PARTS_DIR / "top.json").read_text(encoding="utf-8"))
    parts = []
    for pid in ORDER:
        if only and pid != only:
            continue
        f = PARTS_DIR / f"{pid}.json"
        if not f.exists():
            print(f"[missing] {f.name}", file=sys.stderr)
            continue
        part = json.loads(f.read_text(encoding="utf-8"))
        if part.get("id") != pid:
            print(f"[warn] {f.name}: id is {part.get('id')!r}, expected {pid!r}", file=sys.stderr)
        parts.append(part)
    spec["parts"] = parts
    return spec


def schema_errors(spec):
    import outcome_specs as oc
    return list(oc.schema_errors(spec, "journal-spec.schema.json"))


def main():
    args = sys.argv[1:]
    only = args[args.index("--only") + 1] if "--only" in args else None
    spec = load(only)
    if "--check" in args:
        errs = schema_errors(spec)
        for e in errs:
            print(e)
        print(f"{len(errs)} schema error(s) for {only or 'all parts'}")
        # cheap semantic checks local to the part
        for part in spec["parts"]:
            claims = {c["id"] for c in part.get("thesis", {}).get("supporting_claims", [])}
            used = set()
            for i, post in enumerate(part.get("posts", [])):
                sup = post.get("role", {}).get("supports", [])
                used.update(sup)
                for s in sup:
                    if s not in claims:
                        print(f"[semantic] {post['id']}: supports unknown claim {s}")
                if post.get("kind") in ("chapter", "walkthrough", "case") and not sup:
                    print(f"[semantic] {post['id']}: arguing page supports no claim (orphan)")
                if i > 0 and "transition_in" not in post:
                    print(f"[semantic] {post['id']}: missing transition_in")
            for c in sorted(claims - used):
                print(f"[semantic] {part['id']}: claim {c} has no supporting page (gap)")
            jclaims = {c["id"] for c in spec["thesis"]["supporting_claims"]}
            for s in part.get("role", {}).get("supports", []):
                if s not in jclaims:
                    print(f"[semantic] {part['id']}: role supports unknown journal claim {s}")
        return
    out = ROOT / "journal-spec.json"
    out.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {out} with {len(spec['parts'])} parts, "
          f"{sum(len(p['posts']) for p in spec['parts'])} posts")


if __name__ == "__main__":
    main()
