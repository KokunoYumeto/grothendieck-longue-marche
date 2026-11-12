"""Write the staging spec (raw_publish_20261111/tools_local/spec_LMSP_CLOSE.json) for the close of the second pass:
the outputs of the twelve passes of 12 Nov afternoon (checked text, changes, checked notes, prompt), the five new
_checked_fixed.tex, the index, the close report and the close's work folder (scripts and tables; no build files).
Crops and page images are left out. usage: python -I make_spec.py"""
import json
import pathlib

W = pathlib.Path(__file__).resolve().parent
SP = W.parent
CLONE = "C:/Users/user/Documents/raw_publish_20261111/grothendieck-longue-marche"
NEW = ["LM_C1-001-019", "LM_C1-020-037", "LM_C4-134-152", "LM_C4-153-171", "LM_C4-172-190", "LM_C4-191-209",
       "LM_C4-210-228", "LM_C4-229-247", "LM_C4-248-266", "LM_C4-267-280", "LM_P04", "LM_P05"]
items = []


def add(p):
    p = pathlib.Path(p)
    assert p.is_file(), p
    items.append({"src": p.as_posix(), "dst": "raw/second_pass/" + p.relative_to(SP).as_posix()})


for k in NEW:
    for suf in ("_checked.tex", "_changes.md", "_notes_checked.md"):
        add(SP / f"{k}{suf}")
    add(SP / f"PROMPT_{k}.md")
for k in ("LM_P046", "LM_P065", "LM_P068-069", "LM_C3-302-320", "LM_C3-321-339"):
    add(SP / f"{k}_checked_fixed.tex")
add(SP / "CURRENT_TEXT_INDEX.tsv")
add(SP / "SECOND_PASS_CLOSE_REPORT.md")
for p in sorted(W.iterdir()):
    if p.is_file() and p.suffix in (".py", ".tsv", ".tex", ".log", ".md"):
        add(p)
out = pathlib.Path("C:/Users/user/Documents/raw_publish_20261111/tools_local/spec_LMSP_CLOSE.json")
out.write_text(json.dumps({"clone": CLONE, "items": items}, indent=1, ensure_ascii=False), encoding="utf-8")
print(len(items), "items ->", out)

