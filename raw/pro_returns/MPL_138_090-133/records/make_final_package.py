#!/usr/bin/env python3
"""Finalize the research ledger, check frozen bytes, and create the final ZIP.

This script never edits transcription, doubts, or inventory files.
Supplied scans/context and prior ZIPs remain outside the deliverable.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "records"
PREFIX = "MPL_138_090-133"
STAMP = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
WHO = "GPT-6 Astra Pro; effort not separately exposed; run MPL_138_090-133/root"
HEAD = ["statement_id", "date", "who", "type", "outcome"]
OUT = ROOT.parent / (PREFIX + ".zip")

if OUT.exists():
    raise SystemExit("Final archive already exists; refusing an unreviewed overwrite.")
frozen = json.loads((RECORDS / "frozen_hashes.json").read_text())["sha256"]
observed = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in frozen}
assert len(observed) == 44 and observed == frozen, "Frozen transcription changed"
notes = (ROOT / (PREFIX + "_notes.md")).read_text()
note_ids = re.findall(r"^### ((?:ER|MM|AR|BC|OP|SR)\d\d) —", notes, re.M)
assert len(note_ids) == len(set(note_ids)) == 127
with (ROOT / (PREFIX + "_inventory.csv")).open(newline="") as f:
    inventory = list(csv.DictReader(f))
assert len(inventory) == 992 and all(r["transcribed"] == "yes" for r in inventory)

with (ROOT / "progress.log").open("a") as f:
    f.write(f"research assembly completed {STAMP}; 127 item-level notes; exact computations, context comparisons, and bounded peer checks recorded\n")
    f.write(f"final frozen hashes verified unchanged {STAMP}; all 44 of 44 SHA-256 values equal the pre-context freeze\n")
(RECORDS / "final_integrity.json").write_text(json.dumps({
    "time": STAMP, "files_checked": 44, "unchanged": True,
    "observed_sha256": observed,
    "note_count": len(note_ids), "inventory_rows": len(inventory),
}, ensure_ascii=False, indent=2) + "\n")

events = [
    ["PACKAGE-FROZEN-HASHES", STAMP, WHO, "computation or formal certificate",
     "Recomputed all 43 page-file hashes and the combined-fragment hash; all 44 equal the SHA-256 values recorded before context was opened. This is byte integrity, not a reading-accuracy proof."],
    ["PACKAGE-NOTE-INVENTORY-COUNTS", STAMP, WHO, "computation or formal certificate",
     "127 unique item-note IDs; 992 inventory rows all marked yes. These checks establish record consistency, not visual completeness."],
    ["Stacks 03SF", "2026-11-17", WHO, "carried as background without fault found",
     "Primary section 58.7 opened by root; finite Galois-cover/normal-subgroup dictionary used as standard background. Its Galois-category premises were not independently reproved."],
    ["AR16", STAMP, WHO, "targeted proof check",
     "Final editorial review restored the explicit hypothesis deg(phi)>deg(psi) from frozen112:24. The squarefree-denominator numerator has leading coefficient sum(p_i)-sum(q_j)>0 and hence degree a+b-1 under that hypothesis."],
    ["AR13", STAMP, WHO, "used and rechecked in this run",
     "Field wording checked against the certified mutual rational formulas: Q(c)=Q(t), t^3=2, for the corresponding root t. The three embedded fields are abstractly isomorphic; no equality of every embedded field with the real cube-root field is intended."],
]
with (RECORDS / "final_check_events.tsv").open("w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(HEAD)
    w.writerows(events)
subprocess.run([sys.executable, str(RECORDS / "assemble_check_events.py")], check=True,
               stdout=subprocess.DEVNULL)

spec = importlib.util.spec_from_file_location("package_validator", RECORDS / "validate_package.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
validation = module.Validator(ROOT, False).run()
assert validation["issue_counts"] == {"error": 0, "warning": 0, "info": 0}, validation["issues"]
(RECORDS / "mechanical_validation_final.json").write_text(
    json.dumps(validation, ensure_ascii=False, indent=2) + "\n")
with (ROOT / "progress.log").open("a") as f:
    f.write(f"final mechanical validation passed {STAMP}; 0 errors, 0 warnings; 43 pages, 992 inventory rows, 335 uncertainty occurrences; no TeX rendering claimed\n")
    f.write(f"final archive prepared {STAMP}; source scans, supplied context, and earlier checkpoint archives excluded\n")

(RECORDS / "RESUME.md").write_text("""# Final package state

All 43 specified scans (90, 91, 93–133) were transcribed by root in one stream,
with every whole-page and half-page image viewed and a second visual audit of
each page recorded. No OCR was used. The 43 page files and combined fragment
were frozen at 2026-11-17 23:02:39 UTC, before context was opened at 23:02:52 UTC.
Their final hashes are unchanged. Do not rerun historical page-writing scripts
over these frozen deliverables. The context may suggest reading questions but
must never be used to modify this transcription.

The final research deliverable contains 127 item-level notes and the standing
sections on self-flagged steps and title/page-count evidence. CHECK_EVENTS.tsv
records actual computations, scoped proof checks, background uses and
refutations; the earlier context's unreviewed claims remain unreviewed.

The supplied scans/context and checkpoint archives are not embedded. Historical
work records remain under records/. Reproduction commands for research
certificates are in the notes. The TeX compilation attempt failed because the
available runtime lacked its format and class/package files; structural checks
are not a successful TeX rendering or a guarantee of palaeographic accuracy.
""")
(ROOT / "README.txt").write_text("""MPL_138_090-133 — final deliverable

43 supplied scans: 138/90, 138/91, 138/93–133. Scan 92 was omitted at source.

MPL_138_090-133_transcription.tex  Combined diplomatic LaTeX fragment.
pages/                            One frozen fragment for each scan.
MPL_138_090-133_doubts.md           Notation, uncertainties, abbreviations, limits.
MPL_138_090-133_inventory.csv       992 inventory elements, all marked transcribed.
MPL_138_090-133_notes.md            127 research notes, comparisons and references.
CHECK_EVENTS.tsv                  Typed evidence/check ledger.
progress.log                      Chronology, freeze and final hash verification.
records/                          Work records, proofs, scripts and check outputs.

The transcription is frozen and has not changed since context was opened.
All 44 frozen SHA-256 values were checked again during final assembly.
Research corrections occur only in the notes and supporting research records.
Uncertain readings remain explicitly marked. The LaTeX was structurally checked
but could not be compiled with the incomplete TeX runtime available here.
""")

files = [p for p in ROOT.rglob("*") if p.is_file()
         and "__pycache__" not in p.parts
         and p.suffix not in {".pyc", ".zip"}
         and p.name != "package_manifest.json"]
manifest = {str(p.relative_to(ROOT)): {
    "bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()
} for p in sorted(files)}
(RECORDS / "package_manifest.json").write_text(json.dumps({
    "time": STAMP,
    "scope": "All final archive members except this manifest itself.",
    "files": manifest,
}, ensure_ascii=False, indent=2) + "\n")
files.append(RECORDS / "package_manifest.json")
assert sum(p.parent == ROOT / "pages" for p in files) == 43
assert not any(p.suffix.lower() in {".jpg", ".jpeg", ".png"} for p in files)
with zipfile.ZipFile(OUT, "x", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(files):
        z.write(p, p.relative_to(ROOT))
with zipfile.ZipFile(OUT) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(files)
    for name, entry in manifest.items():
        assert hashlib.sha256(z.read(name)).hexdigest() == entry["sha256"]
assert all(hashlib.sha256((ROOT / n).read_bytes()).hexdigest() == h
           for n, h in frozen.items())
print(json.dumps({
    "path": str(OUT), "bytes": OUT.stat().st_size,
    "files": len(files), "sha256": hashlib.sha256(OUT.read_bytes()).hexdigest(),
    "validation": validation["issue_counts"],
    "check_events": validation["counts"]["check_events"],
    "frozen_hashes_unchanged": True,
}))
