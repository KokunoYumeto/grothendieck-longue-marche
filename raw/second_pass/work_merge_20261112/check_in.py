"""For each open fix: is Pro's replacement already in the current file verbatim (or up to whitespace)?"""
import csv, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
L = pathlib.Path(__file__).resolve().parents[2]; SP = L / "second_pass"
reps = {}
for f in sorted((L / "answers").glob("LM_FIX_*_fixes.csv")):
    if "(1)" in f.name: continue
    for r in csv.DictReader(open(f, encoding="utf-8")):
        reps[(r.get("item") or "").strip()] = (r.get("replacement") or "").strip()
opened = re.findall(r"^- (LM_FIX_\S+) \((\S+), scan (\d+), kind (\w)\)", (SP / "merge_fixes_open.md").read_text(encoding="utf-8"), re.M)
ws = lambda s: re.sub(r"\s+", "", s)
for iid, pkg, scan, kind in opened:
    t = (SP / f"{pkg}_checked_fixed.tex").read_text(encoding="utf-8")
    rep = reps[iid]
    print(iid, pkg, kind, "exact" if rep in t else ("ws-equal" if ws(rep) in ws(t) else "-"), "| in _checked.tex:", rep in (SP / f"{pkg}_checked.tex").read_text(encoding="utf-8"))
