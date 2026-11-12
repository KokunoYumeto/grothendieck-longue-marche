"""Close of the second pass (12 Nov 2026): the three fixes of the fix packages that were still not in the second-pass
texts and that the scans confirm (LM_FIX_11-022, 14-027, 16-025). Each edit is an exact, unique replacement; the result
is written to second_pass/PKG_checked_fixed.tex (created from PKG_checked.tex). usage: python -I apply_close_merge.py"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
SP = pathlib.Path(__file__).resolve().parent.parent
B = "\\"
E = [
    # scan 451 (140-2): the struck mark after -z is raised: a cancelled superscript (Pro's note; ink confirms)
    ("LM_P046", "LM_FIX_11-022",
     "(z,t)" + B + "longrightarrow(" + B + "unsure{-z}" + B + "deleted{" + B + "illegible{1}},-t)",
     "(z,t)" + B + "longrightarrow(" + B + "unsure{-z}^{" + B + "deleted{" + B + "illegible{1}}},-t)"),
    # scan 107 (140-3): a c is legible after the hatched block, left of =δ+c(δ/b+b)
    ("LM_P068-069", "LM_FIX_14-027",
     "&&&" + B + "illegible{1}=" + B + "delta+c",
     "&&&" + B + "deleted{" + B + "illegible{1}c}=" + B + "delta+c"),
    # scan 329 (140-3): after the struck «v+w^2=» only the strike line continues; no right-hand operand
    ("LM_C3-321-339", "LM_FIX_16-025",
     B + "deleted{$" + B + "unsure{v|" + B + "nu}+" + B + "unsure{w|" + B + "omega}^2=" + B + "illegible{1}$}",
     B + "deleted{$" + B + "unsure{v|" + B + "nu}+" + B + "unsure{w|" + B + "omega}^2=$}"),
]
for pkg, iid, old, new in E:
    out = SP / f"{pkg}_checked_fixed.tex"
    src = out if out.exists() else SP / f"{pkg}_checked.tex"
    t = src.read_text(encoding="utf-8")
    if new in t:
        print(iid, pkg, "already applied")
        continue
    n = t.count(old)
    if n != 1:
        print(iid, pkg, "NOT applied: found", n)
        continue
    out.write_text(t.replace(old, new), encoding="utf-8")
    print(iid, pkg, "applied ->", out.name)
