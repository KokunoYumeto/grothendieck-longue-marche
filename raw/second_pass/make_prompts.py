"""Write the second-pass prompt of each package from SECOND_PASS_PROMPT.md.
usage: python -I make_prompts.py PKGNUM...   (e.g. 11 12 13; scans are 10 per package from 101 for P011)"""
import pathlib
import sys

L = pathlib.Path(__file__).parent.parent
t = (L / "second_pass" / "SECOND_PASS_PROMPT.md").read_text(encoding="utf-8")
for n in map(int, sys.argv[1:]):
    k = f"LM_P{n:03d}" if n >= 11 else f"LM_P{n:02d}"
    first = 10 * (n - 1) + 1
    last = first + 9
    s = (t.replace("{PKG}", k).replace("{FIRST}", str(first)).replace("{LAST}", str(last))
         .replace("{FIRSTPASS}", "answers\\unzipped\\" + k + "\\" + k + "_transcription.tex")
         .replace("{NOTES}", "answers\\unzipped\\" + k + "\\" + k + "_notes.md"))
    (L / "second_pass" / f"PROMPT_{k}.md").write_text(s, encoding="utf-8")
    (L / "second_pass" / f"work_{k}").mkdir(exist_ok=True)
    print(k, first, last)
