"""Render notes from the separately maintained post-freeze item data."""
from pathlib import Path
import runpy, subprocess, json, re

ROOT = Path(__file__).resolve().parents[1]
data = runpy.run_path(str(ROOT / "scripts" / "build_notes.py"))
notes = sorted(data["N"], key=lambda n: n["id"])
assert len({n["id"] for n in notes}) == len(notes)
front = ROOT / "records" / "notes_frontmatter.md"
back = ROOT / "records" / "notes_backmatter.md"
parts = [front.read_text(encoding="utf-8") if front.exists() else "# Research notes\n"]
ledger = []
for n in notes:
    locs = []
    for scan in n["scans"]:
        path = ROOT / "pages" / f"MPL_137_002-044_137_scan{scan:03d}.tex"
        lines = path.read_text(encoding="utf-8").splitlines()
        found = [i for i, line in enumerate(lines, 1) if n["anchor"] in line]
        if found:
            locs.append(f"scan {scan:03d}, page-file L{found[0]} ff.")
        else:
            locs.append(f"scan {scan:03d}, related passage")
    result = subprocess.run(
        ["rg", "-n", "-i", "--", n["query"], str(ROOT.parent / "context")],
        capture_output=True, text=True, check=False)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr)
    hits = []
    for line in result.stdout.splitlines():
        m = re.match(r"(.+?):(\d+):(.*)", line)
        if m:
            hits.append({"file": str(Path(m.group(1)).relative_to(ROOT.parent)),
                         "line": int(m.group(2))})
    ledger.append({"id": n["id"], "query": n["query"], "hit_count": len(hits),
                   "locations": hits})
    parts += [f"## {n['id']} — {n['title']}\n",
              f"**Witness:** 137.pdf, {'; '.join(locs)}.  \n"
              f"**Kind:** {n['kind']}.\n",
              n["body"] + "\n"]
if back.exists():
    parts.append(back.read_text(encoding="utf-8"))
(ROOT / "MPL_137_002-044_notes.md").write_text("\n".join(parts), encoding="utf-8")
(ROOT / "records" / "context_searches.json").write_text(
    json.dumps(ledger, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
(ROOT / "records" / "notes_index.json").write_text(
    json.dumps([{"id": n["id"], "title": n["title"], "scans": n["scans"],
                 "kind": n["kind"]} for n in notes],
               ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"notes": len(notes),
    "words": len(" ".join(parts).split()),
    "context_queries": len(ledger),
    "queries_without_hits": [r["id"] for r in ledger if not r["hit_count"]]}))
