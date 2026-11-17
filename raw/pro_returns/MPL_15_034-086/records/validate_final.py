"""Read-only checks of the frozen transcription; write only validation and guide files."""
from pathlib import Path
import argparse
import collections
import csv
import hashlib
import json
import re

PACKAGE = Path(__file__).resolve().parent.parent
PREFIX = "MPL_15_034-086"
SCANS = [34,36,38,40,42,44,46,48,50,52,54,56,60,61,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,85,86]

def check_markdown_tables(text):
    expected = None
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("|"):
            cells = re.split(r"(?<!\\)\|", line)[1:-1]
            if expected is None:
                expected = len(cells)
            assert len(cells) == expected, (n, line)
        else:
            expected = None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stamp", required=True)
    args = parser.parse_args()
    expected = json.loads((PACKAGE / "records/frozen_sha256.json").read_text())
    assert len(expected) == 32
    for name, digest in expected.items():
        assert hashlib.sha256((PACKAGE / name).read_bytes()).hexdigest() == digest, name
    pages = sorted((PACKAGE / "pages").glob("*.tex"))
    assert [int(re.search(r"scan(\d+)", p.name).group(1)) for p in pages] == SCANS
    combined = (PACKAGE / f"{PREFIX}_transcription.tex").read_text()
    assert combined == "\n\n".join(p.read_text().rstrip() for p in pages) + "\n"
    assert combined.startswith("\\cotefile{15}\n\\scanpage{34}")
    assert [int(x) for x in re.findall(r"\\scanpage\{(\d+)\}", combined)] == SCANS
    assert "\\documentclass" not in combined
    with (PACKAGE / f"{PREFIX}_inventory.csv").open(newline="") as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames == ["cote","scan","sheet_kind","element","kind","position","first_words_or_objects","transcribed"]
        rows = list(reader)
    assert len(rows) == 644
    assert all(r["transcribed"] == "yes" and r["cote"] == "15" for r in rows)
    assert sorted({int(r["scan"]) for r in rows}) == SCANS
    allowed = {"text","display","diagram","drawing","margin note","insertion","deletion"}
    assert {r["kind"] for r in rows} <= allowed
    sheets = {}
    for scan in SCANS:
        kinds = {r["sheet_kind"] for r in rows if int(r["scan"]) == scan}
        assert len(kinds) == 1
        sheets[scan] = kinds.pop()
    assert collections.Counter(sheets.values()) == {"text":23, "reused_typed":8}
    doubts = (PACKAGE / f"{PREFIX}_doubts.md").read_text()
    occurrences = len(re.findall(r"\\(?:unsure|illegible)\{", combined))
    assert occurrences == 415
    assert len(re.findall(r"^\| 15 \|", doubts, re.M)) == occurrences
    notes = (PACKAGE / f"{PREFIX}_notes.md").read_text()
    counts = {"MB":16,"D":18,"B":21,"R":14,"X":8}
    for prefix, number in counts.items():
        found = [int(x) for x in re.findall(r"^#{2,4} "+prefix+r"(\d+)\b", notes, re.M)]
        assert found == list(range(1,number+1)), (prefix, found)
    for prefix, number in {"U":22,"P":18}.items():
        found = [int(x) for x in re.findall(r"^(?:\| |\*\*)"+prefix+r"(\d+)\b", notes, re.M)]
        assert found == list(range(1,number+1)), (prefix, found)
    assert len(re.findall(r"^# ",notes,re.M)) == 1
    assert not re.search(r"turn\d+(?:view|search)\d+|Research draft|Working research report", notes)
    check_markdown_tables(notes)
    check_markdown_tables(doubts)
    progress = (PACKAGE / "progress.log").read_text()
    assert sorted(map(int,re.findall(r"15 scan (\d+) done",progress))) == SCANS
    assert sorted(map(int,re.findall(r"scan (\d+) audited",progress))) == SCANS
    assert progress.index("transcription frozen") < progress.index("context opened")
    defect = r"\mathbf{v}érifient"
    assert defect in (PACKAGE / "pages/MPL_15_034-086_15_scan069.tex").read_text()
    words = len(notes.split())
    report = f"""# Final validation — {PREFIX}

Checked {args.stamp}.

## Integrity and coverage

- All 31 page fragments and the combined transcription match all 32 SHA-256 values recorded before the context opened.
- The combined file is the exact ordered concatenation of the page fragments, apart from its documented blank-line separators; it starts with the required cote and scan commands and has no preamble.
- The actual supplied scan list contains 31 pages; the later reference to 49 pages in the prompt does not match the attachment manifest.
- Inventory: 644 rows, all transcribed=yes, with the required eight column names and all seven permitted element kinds represented.
- Sheet classifications: 23 handwritten subject sheets and 8 reused typed/printed sheets.
- Doubts: 415 occurrences of the doubt macros in the transcription and 415 corresponding register rows.
- Progress log: 31 page-completion entries and 31 second-reading audit entries; freeze precedes context opening.

## Research report

The final report has {words:,} whitespace-separated words and 77 individually identified research notes: MB01–MB16, D01–D18, B01–B21, R01–R14 and X01–X08. It also has the 22-entry unverified-step register U01–U22 and the 18-entry title/page-number register P01–P18. The planning answers, linear/nonlinear comparison, cautious A–D concordance, arithmetic Nori sequence, and S15 scope table are included. Markdown table column counts were checked; the report has one top-level title and contains no working-status banner or raw retrieval IDs.

The primary agent reviewed the research sections, checked the cited primary-source passages, and independently checked the main explicit examples and calculations. A second mathematical review checked the special-ideal tensor inverse, the generator-change argument, the monoidal counterexample and adjusted tensorator, the Dedekind localization converse, and the norm/character/cocharacter qualifications. These checks do not confer archival review status on the supplied first-pass contextual notes or solve the open ledger items.

## Limits of validation

The primary agent visually read every supplied whole image and both halves, then audited each page against its image before freezing. No OCR was used on those images and no parallel worker transcribed or changed a page.

Structural LaTeX checks passed before the freeze, but a full LaTeX compile and rendered output were unavailable because the installed executable lacks its format and required package tree. After the context opened, scan 069 was found to encode the initial v of the prose word vérifient as a math-font command outside math mode. This known markup defect is preserved under the user's strict freeze rule and described in X08; successful compilation is not claimed. Hash equality proves preservation, not that every difficult reading is correct.

The archive builder separately checks ZIP integrity and excludes the supplied attachments, extracted source files, source images and image renders. Work records, scripts, notes and logs are retained.
"""
    (PACKAGE / "records/final_validation.md").write_text(report)
    guide = f"""# {PREFIX}

## Contents

- {PREFIX}_transcription.tex: the combined diplomatic LaTeX fragment in archive scan order.
- pages/: the 31 separately saved page fragments.
- {PREFIX}_doubts.md: shared notation, 415 doubt entries, abbreviations and legibility assessment.
- {PREFIX}_inventory.csv: 644 element rows; every row is marked transcribed=yes.
- {PREFIX}_notes.md: the {words:,}-word English research report, including the planning tables and standing registers.
- progress.log: page completion, second-reading audits, transcription freeze, context opening and checkpoint/final-package records.
- records/: supporting notes, mathematical research drafts, source locators, validation records, hashes and work scripts.

## Reading the research report

The opening tables answer the planning questions and state the limits of the available evidence. The detailed notes then follow the principal subjects: Deuring gerbes and crystalline orientations, Brandt/Picard categories, compact tori and norms, and reused typed/printed material. Neighboring contextual notes remain first-pass leads, and research-return statuses are not silently promoted to reviewed results.

## Frozen transcription and validation

The transcription was frozen on 17 November 2026 at 20:48:04 UTC; the context was opened at 20:48:11 UTC. All 32 frozen hashes were checked unchanged at final validation. No research correction has been applied to the transcription.

A full LaTeX compilation could not be performed with the available installation. One post-freeze prose/math-font markup defect on scan 069 is disclosed in note X08 and records/final_validation.md. Difficult or uncertain readings are identified in the transcription and doubts register; the delivery does not claim that hash or structural checks establish their correctness.

The attached scans and context sources are excluded from the archive, as requested. The scripts in records document the work; finalize_pre_context.py is a historical script and must not be rerun on the frozen delivery.
"""
    (PACKAGE / "README.md").write_text(guide)
    with (PACKAGE / "progress.log").open("a") as log:
        log.write(f"final validation {args.stamp}; all 32 frozen SHA-256 hashes unchanged; 31 pages, 644 complete inventory rows, 415 registered doubts, 77 research notes; full compile unavailable; scan069 markup limitation disclosed\n")
    print(json.dumps({"frozen_hashes_unchanged":32,"pages":31,"inventory_rows":644,"doubts":415,"research_notes":77,"research_words":words,"standing_entries":40,"validation_time":args.stamp},indent=2))

if __name__ == "__main__":
    main()
