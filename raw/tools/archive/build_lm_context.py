"""Build the context folder that goes with an archive transcription package around La Longue Marche (user, 11 Nov
2026: the research notes should have "more bearing on our new knowledge", so the model gets what we already have).
The context is opened only after the whole transcription is written (see ARCHIVE_PROMPT_TEMPLATE.md), so it cannot
steer the readings.

Contents, from C:\\Users\\user\\Documents\\longue_marche_pro_pilot_20261104:
  LM_<cote>_text.tex   our current text of La Longue Marche, scan by scan, for cotes 140-1 to 140-4. Per scan the best
                       source that exists: second_pass LM_<KEY>_checked_fixed.tex, then LM_<KEY>_checked.tex (both
                       checked against the scans), then answers/fixed, then the first pass in answers/unzipped.
  LM_<cote>_notes.md   the research notes of the same packages (checked notes where the second pass exists).
  LM_table_of_contents.txt, LM_GLOBAL_PASS.md, LM_OVERVIEW.md, SECTIONS_STATE.md, README.md

usage: python -I build_lm_context.py OUTDIR"""
import pathlib
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
LM = pathlib.Path(r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104")
ARCH = pathlib.Path(r"C:\Users\user\Documents\grothendieck_archive_montpellier")
BS = chr(92)
SCAN = re.compile(re.escape(BS) + r"scanpage\{(\d+)\}")
STATUS = {0: "second pass, checked against the scans (with later fixes)", 1: "second pass, checked against the scans",
          2: "first pass, with mechanical fixes", 3: "first pass only (not yet checked)"}


def cote_of(key):
    m = re.fullmatch(r"LM_C(\d)-\d+-\d+", key)
    if m:
        return "140-" + m.group(1)
    m = re.fullmatch(r"LM_P(\d+)(?:-\d+)?(?:api)?", key)  # LM_P057api: the API run of P057, second-passed
    if m:
        n = int(m.group(1))
        if n <= 58:
            return "140-2"
        if n <= 71:
            return "140-3"
    return None


def sources():
    out = []
    for p in (LM / "second_pass").glob("LM_*_checked_fixed.tex"):
        out.append((0, p.name[:-len("_checked_fixed.tex")], p))
    for p in (LM / "second_pass").glob("LM_*_checked.tex"):
        out.append((1, p.name[:-len("_checked.tex")], p))
    for p in (LM / "answers" / "fixed").glob("LM_*_transcription.tex"):
        out.append((2, p.name[:-len("_transcription.tex")], p))
    for p in (LM / "answers").glob("LM_P*_transcription.tex"):  # the pilot returns P01, P02, P04 lie in answers/
        out.append((3, p.name[:-len("_transcription.tex")], p))
    for d in (LM / "answers" / "unzipped").iterdir():
        if d.is_dir() and d.name.startswith("LM_"):
            for p in d.glob("*transcription*.tex"):
                out.append((3, d.name, p))
    return out


def notes_for(key):
    for p in (LM / "second_pass" / f"{key}_notes_checked.md", LM / "answers" / "unzipped" / key / f"{key}_notes.md",
              LM / "answers" / f"{key}_notes.md", LM / "answers" / f"{key}_reading_apparatus.md"):
        if p.exists():
            return p
    return None


def main(outdir):
    out = pathlib.Path(outdir)
    out.mkdir(parents=True, exist_ok=False)
    best = {}
    skipped = set()
    for rank, key, p in sources():
        cote = cote_of(key)
        if cote is None:
            skipped.add(key)
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        parts = SCAN.split(t)
        for i in range(1, len(parts) - 1, 2):
            n = int(parts[i])
            body = parts[i + 1]
            k = (cote, n)
            if k not in best or rank < best[k][0]:
                best[k] = (rank, key, body)
    readme = ["# Context: what we already have on La Longue Marche (state: 11 Nov 2026)", "",
              "Open this only after your transcription is finished and written to disk (see the prompt).", "",
              "| File | What it is |", "|---|---|"]
    for cote in ("140-1", "140-2", "140-3", "140-4"):
        scans = sorted(n for (c, n) in best if c == cote)
        if not scans:
            continue
        lines, cur, keys = [], None, []
        for n in scans:
            rank, key, body = best[(cote, n)]
            if (key, rank) != cur:
                lines.append(f"% ===== {key}: {STATUS[rank]} =====")
                cur = (key, rank)
                if key not in keys:
                    keys.append(key)
            lines.append(BS + "scanpage{" + str(n) + "}" + body.rstrip())
        (out / f"LM_{cote}_text.tex").write_text(chr(10).join(lines) + chr(10), encoding="utf-8")
        checked = sum(1 for n in scans if best[(cote, n)][0] <= 1)
        notes = []
        for key in keys:
            p = notes_for(key)
            if p:
                kind = "checked notes" if p.name.endswith("_notes_checked.md") else "first-pass notes"
                notes.append(f"\n\n# ===== {key} ({kind}) =====\n\n" + p.read_text(encoding="utf-8", errors="replace"))
        (out / f"LM_{cote}_notes.md").write_text("".join(notes).lstrip(), encoding="utf-8")
        readme.append(f"| `LM_{cote}_text.tex` | Our diplomatic transcription of cote {cote} of *La Longue Marche*, scans "
                      f"{scans[0]}-{scans[-1]} ({len(scans)} scans; {checked} checked against the scans in a second "
                      f"pass, the rest first pass only). Same macros as your transcription. A comment line before each "
                      f"package says its source. |")
        readme.append(f"| `LM_{cote}_notes.md` | The research notes made on those packages (Grothendieck's conjectures "
                      f"and questions, claims without proof, implications not pursued, ideas of the models), checked "
                      f"against the corrected text where the second pass exists. |")
        print(cote, "scans", len(scans), "checked", checked, "packages", len(keys))
    extra = [(LM / "second_pass" / "witness" / "Grothendieck_Circle_tableLM.txt", "LM_table_of_contents.txt",
              "The author's table of contents of *La Longue Marche* (a later typed list, from the Grothendieck Circle)."),
             (LM / "second_pass" / "GLOBAL_PASS.md", "LM_GLOBAL_PASS.md",
              "Our global pass over the notes: the main topics across the manuscript, with scans."),
             (LM / "pro_prompts_draft_20261111" / "OVERVIEW.md", "LM_OVERVIEW.md",
              "A reading of the whole manuscript: its programme, its sections and what it leaves open (Claude Fable 5.2, 10 Nov 2026)."),
             (ARCH / "SECTIONS_STATE.md", "SECTIONS_STATE.md",
              "What each section of the Montpellier archive holds, how far he took it and who has edited it (10 Nov 2026).")]
    for src, name, what in extra:
        shutil.copy2(src, out / name)
        readme.append(f"| `{name}` | {what} |")
    readme += ["", "These are our working materials, not an edition: the first-pass parts have errors, and every note is "
               "a lead, not a result."]
    (out / "README.md").write_text(chr(10).join(readme) + chr(10), encoding="utf-8")
    (out / "SUMMARY.txt").write_text(  # first line goes into the prompt (build_package.py)
        "our transcription of *La Longue Marche à travers la théorie de Galois* (cotes 140-1 to 140-4, scan by scan, "
        "most of it checked against the scans), the research notes made on it, his table of contents, our overview of "
        "the manuscript and our description of the archive's sections" + chr(10), encoding="utf-8")
    if skipped:
        print("not mapped to a cote (left out):", sorted(skipped))
    print("total MB", round(sum(f.stat().st_size for f in out.iterdir()) / 1e6, 1))


if __name__ == "__main__":
    main(sys.argv[1])
