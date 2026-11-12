"""For every LM fix item with a replacement: where does it stand in the current second-pass text?
Prints a TSV: item, package, scan, kind, input(fixed/original), in_first_pass_input, current_file, state."""
import csv, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
L = pathlib.Path(r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104")
SP = L / "second_pass"
sys.dont_write_bytecode = True
sys.path.insert(0, str(L))
from fixlib import reading

items, reps = {}, {}
for f in sorted((L / "fixes").glob("items*.csv")):
    for r in csv.DictReader(open(f, encoding="utf-8")):
        if r["item"]:
            items[r["item"]] = r
for f in sorted((L / "answers").glob("LM_FIX_*_fixes.csv")):
    if "(1)" in f.name:
        continue
    for r in csv.DictReader(open(f, encoding="utf-8")):
        reps[(r.get("item") or "").strip()] = r.get("replacement") or ""
open12 = set(re.findall(r"^- (LM_FIX_\S+) ", (SP / "merge_fixes_open.md").read_text(encoding="utf-8"), re.M))
ws = lambda s: re.sub(r"\s+", " ", s).strip()
out = []
for iid, it in sorted(items.items()):
    pkg, rep, s = it["package"], reps.get(iid, "").strip(), it["snippet"]
    if not rep:
        out.append((iid, pkg, it["scan"], it["kind"], "", "", "", "no replacement"))
        continue
    pr = SP / f"PROMPT_{pkg}.md"
    inp = ""
    if pr.exists():
        inp = "fixed" if "answers\\fixed\\" in pr.read_text(encoding="utf-8") else "original"
    fx = L / "answers" / "fixed" / f"{pkg}_transcription.tex"
    infp = ""
    if fx.exists():
        ft = fx.read_text(encoding="utf-8")
        if it["kind"] == "M":
            m = re.search(r"\\illegible\{\d+\}", s)
            rd = reading(rep, s[:m.start()]) if m else None
            infp = "rep" if (rd and rd in ft) else ("snip" if s in ft else "neither")
        else:
            infp = "rep" if ws(rep) in ws(ft) else ("snip" if s in ft else "neither")
    cur = SP / f"{pkg}_checked_fixed.tex"
    if not cur.exists():
        cur = SP / f"{pkg}_checked.tex"
    if not cur.exists():
        out.append((iid, pkg, it["scan"], it["kind"], inp, infp, "", "NO SECOND PASS"))
        continue
    t = cur.read_text(encoding="utf-8")
    if it["kind"] == "M":
        m = re.search(r"\\illegible\{\d+\}", s)
        rd = reading(rep, s[:m.start()]) if m else None
        st = "rep in" if (rd and rd in t) else ("snippet x%d" % t.count(s))
    else:
        st = "rep in" if ws(rep) in ws(t) else ("snippet x%d" % t.count(s))
    if iid in open12:
        st += " | 12Nov outcome"
    out.append((iid, pkg, it["scan"], it["kind"], inp, infp, cur.name, st))
for r in out:
    print("\t".join(r))
