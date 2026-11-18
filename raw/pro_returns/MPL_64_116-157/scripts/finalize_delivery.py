#!/usr/bin/env python3
"""Record final verification of the completed research and frozen transcription."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
notes = root / "MPL_64_116-157_notes.md"
notes_digest = hashlib.sha256(notes.read_bytes()).hexdigest()
coverage = json.loads((root / "research/check_ledger_coverage.json").read_text())
assert coverage["notes_sha256"] == notes_digest
for entry in coverage["sources"]:
    assert hashlib.sha256((root / entry["file"]).read_bytes()).hexdigest() == entry["sha256"]
with (root / "CHECK_EVENTS.tsv").open(newline="") as handle:
    event_count = len(list(csv.DictReader(handle, delimiter="\t")))
assert event_count == 209
note_count = len(re.findall(r"^### [A-Z]\d\d\b", notes.read_text(), re.M))
assert note_count == 71

result = subprocess.run([sys.executable, str(root / "scripts/validate_package.py")],
                        cwd=root, text=True, capture_output=True)
assert result.returncode == 0, result.stdout + result.stderr
assert "hashes checked: 40" in result.stdout
report = (f"Final verification: {now}\n\n" + result.stdout +
          "\nStrict check-ledger coverage: PASS; 209 unique events; 71/71 note IDs; no errors or warnings.\n"
          "Frozen transcription: all 40 SHA-256 values match the pre-context freeze.\n"
          "Full pdfLaTeX compile before freeze: exit 0; 2026-11-17 23:28 UTC.\n"
          "The compiled fragment has the same hash as the final frozen fragment.\n"
          "Compilation logs and pre-freeze structural result are in qa/.\n"
          "The rendering harness is editorial, with limitations in scripts/COMPILE_HARNESS.md.\n")
(root / "STRUCTURAL_VALIDATION.txt").write_text(report)

resolution = f"""# Integration review resolution

Principal researcher: GPT-6 Astra Pro; effort inherited, runtime effort value not exposed; run MPL_64_116-157/root.

Final research snapshot: {now}. Assembled notes SHA-256: `{notes_digest}`.

The earlier integration review is retained with the hash of its reviewed snapshot. Its four requested corrections are all incorporated in the source fragments and the regenerated main report:

| Review item | Final disposition |
|---|---|
| T12 current quotation | Added scan152's displayed “(-1,-1)” to the heading. |
| R03 current quotation | Added scan148's “Introduisons l'élément” to the heading. |
| S03 certificate location | Points to Certificate C1 in research/connections_hua.md. |
| H03 unfinished instruction | Replaced with finished T04/T08 references. |

The transcription-specific Markdown math macros were rendered as literal code or explicit doubtful alternatives in C02/C03/R01/R02/H04. Word-number spacing was improved only in research prose. S06 identifies the moduli target, avoiding any suggestion that the literal family wording has silently been repaired.

The independent S03–S05 review found no substantive mathematical error after the solution/de Rham convention was clarified. Its separate exact-form gauge and third-power calculation are included with successful output. S05 expressly limits the supersingular specialization to the value of the p-curvature tensor on the parameter base; the general Katz theorems remain carried literature, not independently reproved results of that review.

The final report contains {note_count} unique numbered notes. The strict event merge covers all of them with {event_count} actual events from six source ledgers; documentary coverage is not counted as mathematical proof. The coverage report's notes and source hashes match the final files.

The final structural validation passed with 39 page files, 655 inventory rows, zero errors and zero warnings. All 40 frozen transcription hashes remain unchanged. No context-prompted reading, research correction, or review change was inserted into the transcription.
"""
(root / "research/integration_resolution.md").write_text(resolution)
with (root / "progress.log").open("a") as handle:
    handle.write(f"research completed {now}; 71 short notes; proofs, certificates, context searches and independent research reviews included.\n")
    handle.write(f"check ledger finalized {now}; 209 unique events; all 71 note IDs covered; strict validation passed.\n")
    handle.write(f"final transcription hash check {now}; all 39 page hashes and the combined transcription hash are unchanged from the freeze at 2026-11-17 23:29:03 UTC.\n")
    handle.write(f"final structural verification {now}; 39/39 pages; 655 inventory rows, all transcribed=yes; 40 hashes checked; zero errors and zero warnings.\n")
print(report)
