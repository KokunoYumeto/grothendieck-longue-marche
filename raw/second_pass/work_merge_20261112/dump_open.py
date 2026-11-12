"""Dump the 33 open fixes of second_pass/merge_fixes_open.md: snippet, Pro's replacement and note, and what the scan
page of the current file holds (bracketed descriptions, \\illegible marks, Pro's reading already present).
usage: python -I dump_open.py > open_dump.md"""
import csv
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
L = pathlib.Path(__file__).resolve().parents[2]
SP = L / "second_pass"
sys.path.insert(0, str(L))
from fixlib import group_end  # noqa: E402

items, reps, notes = {}, {}, {}
for f in sorted((L / "fixes").glob("items*.csv")):
    for r in csv.DictReader(open(f, encoding="utf-8")):
        if r["item"]:
            items[r["item"]] = r
for f in sorted((L / "answers").glob("LM_FIX_*_fixes.csv")):
    if "(1)" in f.name:
        continue
    for r in csv.DictReader(open(f, encoding="utf-8")):
        k = (r.get("item") or "").strip()
        reps[k] = r.get("replacement") or ""
        notes[k] = r.get("note") or ""
opened = re.findall(r"^- (LM_FIX_\S+) \((\S+), scan (\d+), kind (\w)\)", (SP / "merge_fixes_open.md").read_text(
    encoding="utf-8"), re.M)


def current(pkg):
    for p in (SP / f"{pkg}_checked_fixed.tex", SP / f"{pkg}_checked.tex", L / "answers" / "fixed" /
              f"{pkg}_transcription.tex"):
        if p.exists():
            return p
    return None


only = sys.argv[1:]
for iid, pkg, scan, kind in opened:
    if only and iid not in only:
        continue
    p = current(pkg)
    t = p.read_text(encoding="utf-8")
    m0 = re.search(r"\\scanpage\{" + scan + r"\b[^}]*\}", t)
    page, a = "", 0
    if m0:
        nxt = t.find("\\scanpage{", m0.end())
        a = m0.end()
        page = t[a:(nxt if nxt != -1 else len(t))]
    rep = reps.get(iid, "").strip()
    print(f"## {iid} | {pkg} | scan {scan} | kind {kind} | file {p.name} | page {'found' if m0 else 'MISSING'}"
          f" | page lines {t[:a].count(chr(10)) + 1}-{t[:a].count(chr(10)) + page.count(chr(10)) + 1}")
    print("SNIPPET:\n" + items[iid]["snippet"])
    print("REPLACEMENT:\n" + rep)
    print("NOTE: " + notes.get(iid, "").strip())
    if kind == "M":
        for mm in re.finditer(r"\\illegible\{\d+\}", page):
            print("  ILLEGIBLE on page:", repr(page[max(0, mm.start() - 70):mm.end() + 40]))
        for mm in re.finditer(r"\\unsure\{", page):
            e = group_end(page, mm.start() + len("\\unsure"))
            print("  UNSURE on page:", repr(page[max(0, mm.start() - 40):(e or mm.end()) + 10]))
    else:
        for mm in re.finditer(r"\\(diagram|figure)\{", page):
            e = group_end(page, mm.start() + len(mm.group(1)) + 1)
            blk = page[mm.start():e] if e else page[mm.start():mm.start() + 300]
            print(f"  {mm.group(1).upper()} on page ({len(blk)} chars):", repr(blk[:260]))
    print()
