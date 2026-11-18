"""Package the completed deliverable, excluding supplied inputs and checkpoints."""
from pathlib import Path
import collections
import csv
import datetime
import hashlib
import json
import subprocess
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
now = lambda: datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
notes = json.loads((root / "research/note_entries.json").read_text())
with (root / "CHECK_EVENTS.tsv").open(newline="") as f:
    events = list(csv.DictReader(f, delimiter="\t"))
with (root / "MPL_98_inventory.csv").open(newline="") as f:
    inventory = list(csv.DictReader(f))
assert len(inventory) == 694 and all(r["transcribed"] == "yes" for r in inventory)
assert len({r["scan"] for r in inventory}) == 43
freeze = json.loads((root / "research/frozen_sha256.json").read_text())
assert len(freeze["files"]) == 44

if "--metadata" in sys.argv:
    (root / "README.md").write_text(f"""# MPL_98 — Complete transcription and research return

**Archive file:** 98.pdf, supplied scans 002–044, cote 98.  
**Scope:** all 43 supplied scan faces.  
**Completed research:** {len(notes)} numbered notes; {len(events)} check events.

## Main files

| File | Contents |
|---|---|
| [MPL_98_transcription.tex](MPL_98_transcription.tex) | All pages, in supplied order, as one LaTeX fragment without a preamble |
| pages/ | 43 individual scan fragments, named MPL_98_98_scanNNN.tex |
| [MPL_98_doubts.md](MPL_98_doubts.md) | Shared notation table, 464 marked doubt occurrences, contextual reading issues, abbreviations, and legibility limits |
| [MPL_98_inventory.csv](MPL_98_inventory.csv) | 694 element records, all marked transcribed |
| [MPL_98_notes.md](MPL_98_notes.md) | {len(notes)} concise research notes, explicit self-flags, titles/page counts, register dispositions, and APA references |
| [CHECK_EVENTS.tsv](CHECK_EVENTS.tsv) | {len(events)} mathematical and research-source check events, with actual scope and provenance |
| [progress.log](progress.log) | Sequential completion/audit times, freeze hashes, checkpoint history, and final integrity verification |

The root alone read and transcribed every whole image and both halves, in one sequential stream, and performed the subsequent visual audits. No OCR was used on the supplied manuscript images. The transcription was frozen at **{freeze['frozen_utc']}**, before the supplied context was opened. The final integrity check verifies all 43 fragments and the combined fragment against their frozen SHA-256 values.

The remaining doubt marks are part of the deliverable, not a claim that every word is certain. All source wording, corrections, deletions, and incomplete passages remain separate from proposed mathematical repairs in the notes. Archival foliation is recorded as comments; reused printed page numbers remain ordinary source text. No authorial handwritten page number was confidently identified for an mspage entry.

## Research documentation

The research/ directory contains the extended norm, cohomology, boundedness, and additional proof memoranda; independent reviews; actual per-note context searches; note data and indices; the primary-source verification ledger; computation records; validation reports; and the frozen hash manifest. The concise notes distinguish source questions, unproved claims, contextual differences, and this run's own examples. Supplied results-register statuses remain originating-run claims unless an actual narrower check is recorded.

The scripts/ directory documents transcription bookkeeping, structural and syntax validation, research assembly, final validation, and packaging. The syntax harness is a validation aid, not a replacement edition or a claim of facsimile layout; its limitations are recorded in scripts/VALIDATION.md. It does not change the requested preamble-free fragment.

## Scope of validation

The full transcription syntax check passed before the freeze. Final mechanical checks verify matching note/search registries, one-to-four authored sentences per note, explicit confidence and reasons for own examples, event schema, local links, and unchanged frozen bytes. They do not certify every palaeographic reading or replace the stated mathematical proofs and source comparisons.

The supplied scan/context archives, extracted images and context files, external source PDFs, and earlier checkpoint ZIPs are not included. The two hourly checkpoints already saved remain separate. This ZIP contains the completed return and its working documentation.
""")
    (root / "CHECKPOINT_STATE.md").write_text(f"""# Final completion state

Updated {now()}.

- All 43 scans 002–044 were transcribed in one root stream and visually audited.
- All 44 transcription hashes remain governed by the freeze at {freeze['frozen_utc']}; do not edit those files from context.
- The research return is complete: {len(notes)} notes, one actual context search per note, extended proofs and primary-source records, and {len(events)} check events.
- The final notes include the self-flag, title/page-count, and supplied-register disposition sections.
- Checkpoint 01 and checkpoint 02 were saved at their logged hourly boundaries; they are not copied into the final ZIP.
- Correction to the earlier checkpoint-02 research summary: input flatness is PRESENT in frozen scan039. The counterexample establishes its necessity, not an omission; see B19 and R09.
- Final packaging and integrity results are recorded in progress.log and research/final_package_validation.json.
""")
    print("Final metadata written.")
    raise SystemExit(0)

report = json.loads((root / "research/final_package_validation.json").read_text())
assert report["status"] == "passed" and not report["errors"]
assert report["counts"]["note_entries"] == len(notes)
assert report["counts"]["check_events"] == len(events)
subprocess.run([sys.executable, "-B", str(root / "scripts/verify_frozen.py"), "--log"], check=True)
with (root / "progress.log").open("a") as f:
    f.write(f"final research and package checks passed {now()}: {len(notes)} notes, {len(events)} events, 694 inventory rows; all 44 frozen hashes unchanged\n")
    f.write(f"final ZIP prepared {now()}; supplied inputs, extracted sources, earlier checkpoints, and bytecode caches excluded\n")

def package_files():
    return sorted(p for p in root.rglob("*") if p.is_file()
                  and "__pycache__" not in p.parts
                  and p.suffix not in {".pyc", ".zip"})

manifest = {
    "prepared_utc": now(),
    "transcription_frozen_utc": freeze["frozen_utc"],
    "notes": len(notes), "check_events": len(events), "inventory_rows": len(inventory),
    "files": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in package_files() if p.name != "PACKAGE_MANIFEST.json"},
    "manifest_excludes_itself": True,
}
(root / "PACKAGE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
destination = root.parent / "MPL_98.zip"
with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in package_files():
        z.write(p, p.relative_to(root))
with zipfile.ZipFile(destination) as z:
    assert z.testzip() is None
    assert len([n for n in z.namelist() if n.startswith("pages/") and n.endswith(".tex")]) == 43
    for name, digest in freeze["files"].items():
        assert hashlib.sha256(z.read(name)).hexdigest() == digest
    for name, digest in manifest["files"].items():
        assert hashlib.sha256(z.read(name)).hexdigest() == digest
    names = z.namelist()
print(json.dumps({"zip": str(destination), "bytes": destination.stat().st_size,
                  "members": len(names), "crc": "passed",
                  "all_member_sha256": "passed", "frozen_hashes": 44}))
