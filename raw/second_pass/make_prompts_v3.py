"""Second-pass prompts for any package (10-scan P-packages, the 20-scan trial packages, the 19-image C1/C3/C4 packages),
for every cote. Cote and scan range come from PACKAGES.md. The first pass given to the second pass is the fixed
transcription (answers/fixed) when one exists, else the original; the notes come from the unpacked package (unpacked
here from its zip if needed). Images: second_pass/img for cote 140-2 (as before), second_pass/img_140-N for the
others (prep_images_cote.py). Adds the "develop: yes" request of the 8 Nov prompts. Never overwrites an existing
prompt unless --force. usage: python -I make_prompts_v3.py [--force] KEY...   (KEY e.g. LM_P048, LM_C3-131-149)"""
import pathlib
import re
import sys
import zipfile

L = pathlib.Path(__file__).parent.parent
SP = L / "second_pass"
FORCE = "--force" in sys.argv
keys = [a for a in sys.argv[1:] if not a.startswith("--")]
table = {}
for m in re.finditer(r"^\| (LM_[A-Z0-9-]+) \| cote (140-\d)[^|]*\| (\d+)[–-](\d+) \| (\d+) \|", (L / "PACKAGES.md").read_text(
        encoding="utf-8"), re.M):
    table[m.group(1)] = (m.group(2), int(m.group(3)), int(m.group(4)))
for k, rng in (("LM_P068-069", ("140-3", 91, 110)), ("LM_P070-071", ("140-3", 111, 130))):
    table.setdefault(k, rng)
t = (SP / "SECOND_PASS_PROMPT.md").read_text(encoding="utf-8")
DEVELOP = ("scan number, its kind and one to four sentences. Mark a note \"develop: yes\" when it is worth a Pro "
           "development prompt (an open\n  question, an unproved claim or an unpursued implication that one long, "
           "rigorous Pro run could settle or advance),\n  with the exact statement to attack in one sentence and what "
           "you know of its status in the literature.")
for k in keys:
    if k not in table:
        print(k, "not in PACKAGES.md");
        continue
    cote, first, last = table[k]
    out = SP / f"PROMPT_{k}.md"
    if out.exists() and not FORCE:
        print(k, "prompt exists, kept");
        continue
    u = L / "answers" / "unzipped" / k
    if not u.exists() or not any(u.glob("*notes*.md")):
        zs = [x for x in (L / "answers").glob(f"{k}*.zip") if x.stem in (k, k + "(1)")]
        if zs:
            u.mkdir(parents=True, exist_ok=True)
            zipfile.ZipFile(sorted(zs, key=lambda x: x.stat().st_mtime)[-1]).extractall(u)
    fixed = L / "answers" / "fixed" / f"{k}_transcription.tex"
    orig = u / f"{k}_transcription.tex"
    if fixed.exists():
        fp = "answers\\fixed\\" + k + "_transcription.tex"
    elif orig.exists():
        fp = "answers\\unzipped\\" + k + "\\" + k + "_transcription.tex"
    else:
        print(k, "NO FIRST PASS FOUND");
        continue
    notes = next((p for p in u.glob("*.md") if "notes" in p.name), None) if u.exists() else None
    if notes is None:
        print(k, "NO NOTES FOUND");
        continue
    img = "second_pass\\img" if cote == "140-2" else f"second_pass\\img_{cote}"
    s = (t.replace("{PKG}", k).replace("{FIRST}", str(first)).replace("{LAST}", str(last))
         .replace("{FIRSTPASS}", fp).replace("{NOTES}", "answers\\unzipped\\" + k + "\\" + notes.name))
    s = s.replace("(Montpellier archive, cote\n140-2)", f"(Montpellier archive, cote\n{cote})")
    s = s.replace("cote 140-2)", f"cote {cote})")
    s = s.replace("in `second_pass\\img`", f"in `{img}`")
    # The choice of what to develop is made across the whole manuscript, not per package (user, 8 Nov 2026):
    # the per-package second pass only checks the notes against the corrected text. DEVELOP is not inserted.
    if cote != "140-2":
        s = s.replace("They are evidence, never authority: the ink decides.",
                      "They are evidence, never authority: the ink decides. They may not cover these scans "
                      "(search before relying on them); where none does, the ink alone decides.", 1)
    if fixed.exists():
        s = s.replace("Inputs (all paths", "This first pass already includes targeted fixes of described diagrams and "
                      "illegible marks (redrawn in tikz-cd/TikZ); check them like everything else.\n\nInputs (all paths", 1)
    out.write_text(s, encoding="utf-8")
    (SP / f"work_{k}").mkdir(exist_ok=True)
    print(k, cote, first, last, "fixed" if fixed.exists() else "original", notes.name)
