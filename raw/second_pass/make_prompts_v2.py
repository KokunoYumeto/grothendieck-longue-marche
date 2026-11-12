"""Second-pass prompts for packages whose first pass may have been fixed: the first pass given to the second pass is
the fixed transcription (answers/fixed) when one exists, else the original; the notes come from the unpacked package.
Unpacks the package if needed. usage: python -I make_prompts_v2.py PKGNUM...   (P011 and later: 10 scans each)"""
import pathlib
import sys
import zipfile

L = pathlib.Path(__file__).parent.parent
t = (L / "second_pass" / "SECOND_PASS_PROMPT.md").read_text(encoding="utf-8")
for n in map(int, sys.argv[1:]):
    k = f"LM_P{n:03d}"
    first, last = 10 * (n - 1) + 1, 10 * n
    u = L / "answers" / "unzipped" / k
    if not u.exists():
        z = [x for x in (L / "answers").glob(f"{k}*.zip") if x.stem in (k, k + "(1)")]
        z = sorted(z, key=lambda x: x.stat().st_mtime)[-1]
        u.mkdir(parents=True)
        zipfile.ZipFile(z).extractall(u)
    fixed = L / "answers" / "fixed" / f"{k}_transcription.tex"
    fp = ("answers\\fixed\\" + k + "_transcription.tex") if fixed.exists() else \
         ("answers\\unzipped\\" + k + "\\" + k + "_transcription.tex")
    notes = next((p.name for p in u.glob("*.md") if "notes" in p.name), k + "_notes.md")
    s = (t.replace("{PKG}", k).replace("{FIRST}", str(first)).replace("{LAST}", str(last))
         .replace("{FIRSTPASS}", fp).replace("{NOTES}", "answers\\unzipped\\" + k + "\\" + notes))
    if fixed.exists():
        s = s.replace("Inputs (all paths", "This first pass already includes targeted fixes of described diagrams and "
                      "illegible marks (redrawn in tikz-cd/TikZ); check them like everything else.\n\nInputs (all paths", 1)
    (L / "second_pass" / f"PROMPT_{k}.md").write_text(s, encoding="utf-8")
    (L / "second_pass" / f"work_{k}").mkdir(exist_ok=True)
    print(k, first, last, "fixed" if fixed.exists() else "original")
