import csv, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
L = pathlib.Path(__file__).resolve().parents[2]; SP = L / "second_pass"
reps = {}
for f in sorted((L / "answers").glob("LM_FIX_*_fixes.csv")):
    if "(1)" in f.name: continue
    for r in csv.DictReader(open(f, encoding="utf-8")):
        reps[(r.get("item") or "").strip()] = (r.get("replacement") or "").strip()
for iid, pkg, b, a in [x.split(":") for x in sys.argv[1:]]:
    t = (SP / f"{pkg}_checked_fixed.tex").read_text(encoding="utf-8")
    i = t.find(reps[iid]); j = i + len(reps[iid])
    pre = t[:i].split("\n"); post = t[j:].split("\n")
    print(f"=== {iid} {pkg} line {t[:i].count(chr(10))+1}")
    print("\n".join(pre[-int(b):]) + "<<<FIX ... FIX>>>" + "\n".join(post[:int(a)]))
