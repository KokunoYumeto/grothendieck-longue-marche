# SP04 administrative tooling

`manage.py` never reads scans, witness text, notes, or the context archive. It uses
the attached page map for names/order and the root reader's manually authored
page files and records. It never declares a page read or audited automatically.

## Page data

Write the LaTeX file in `out/pages/` with witness C's exact basename. Write its
record in `out/records/156-4_scan002.json`, using this schema:

```json
{
  "cote": "156-4",
  "scan": 2,
  "changes": [
    {
      "place": "line or display or margin",
      "C": "verbatim witness C reading",
      "H": "verbatim witness H reading",
      "final": "consolidated reading",
      "scan_shows": "specific visible strokes, letters, state, or placement",
      "crop": "relative crop path or coordinate reference",
      "confidence": "high",
      "differs_C": false,
      "differs_H": true,
      "kind": "misread word",
      "marked_in_H": "no",
      "consequential": "optional explanation of a mathematical correction"
    }
  ],
  "inventory": [
    {
      "element": "E01",
      "kind": "text",
      "position": "upper part",
      "first_words_or_objects": "words or objects actually present",
      "sheet_kind": "text",
      "hand": "Grothendieck",
      "transcribed": "yes"
    }
  ],
  "doubts": [
    {
      "line": "place",
      "reading": "preferred reading",
      "alternatives": ["other permissible reading"],
      "confidence": "medium",
      "comment": "optional evidence/qualification"
    }
  ],
  "notation": [
    {
      "sign": "sign or function",
      "latex": "LaTeX reading",
      "appearance": "visible form",
      "locations": "cote, scan, line",
      "alternatives": "qualification or alternatives"
    }
  ],
  "abbreviations": [
    {
      "abbreviation": "written abbreviation",
      "expansion": "editorial expansion",
      "evidence": "location/qualification"
    }
  ]
}
```

`changes`, `inventory`, and `doubts` must be explicitly supplied; the latter two
lists may be empty except that inventory must contain at least one element.
The `changes` list may contain an unchanged doubt retained after inspection:
both difference flags are then false. This does not increase correction counts.
The collation includes only `differs_H=true` rows on pages with H text. A literal
pipe is escaped only in Markdown tables, not altered in TSV or page files.

`kind` must use one of the exact collation kinds specified in the user prompt.
Use `marked_in_H` = `yes`, `no`, or `unclear` for H differences. Inventory `scan`
values default to `156-4:002` to disambiguate cotes; supply optional `scan_label`
in a page record to override. `status` is managed by explicit commands.

Global notation/abbreviations can be maintained in `out/notation.json` with
`notation` and `abbreviations` arrays using the same entry schema. The final
legibility assessment is read verbatim from optional `out/legibility.md`.
Neither file is invented or filled by the tooling.

## Commands

Root must create `out/progress.log` before the first page, with UTC time alone on
its first line, e.g. `2026-11-17 12:34:56 UTC`.

```bash
python out/scripts/manage.py mark-done 156-4 2
python out/scripts/manage.py mark-audited 156-4 2
python out/scripts/manage.py status
python out/scripts/manage.py render
python out/scripts/manage.py check
python out/scripts/manage.py freeze
python out/scripts/manage.py verify --log
python out/scripts/manage.py checkpoint
```

`mark-done` requires all preceding pages done, a nonempty page file, complete
manual metadata, and balanced LaTeX structures. It appends the current time to
the log and regenerates the derived deliverables. `mark-audited` requires all
120 pages done and preceding pages audited. It records the root's explicit
attestation only. Neither command performs a reading. A page can only be marked
once; edits remain possible before freeze, and `render` incorporates edits.

`render` writes the combined LaTeX, changes, collation, inventory, and doubts,
using completed pages in page-map order. It leaves research notes untouched.
The first line of the changes table gives every completed page's counts against
C and H, each split by confidence. Consequential explanations come only from
the caller's `consequential` fields. All page files are concatenated verbatim
apart from trailing whitespace and two newlines between fragments; the caller
controls cote macros and the page's actual text.

`check` is structural, not a LaTeX compiler. It checks braces, environments,
inline dollar parity, and display delimiters. It cannot establish correctness
of commands, mathematical content, handwriting readings, or TikZ geometry.
`check --all` additionally reports missing unfinished files.

`freeze` requires exactly 120 completed and audited records and successful
structural checks. Both status values must be canonical valid UTC timestamp
strings within this run. Every status requires exactly one matching
`progress.log` event, in a full ordered done pass followed by a full ordered
audit pass, with nondecreasing timestamps. It prepares every page and combined
SHA-256, atomically persists `freeze.sha256`, then atomically publishes the
frozen marker and complete hash block in `progress.log`. It locks
completion/audit mutations and rejects `render` when
the combined frozen text would change. `verify --log` records whether all 121
hashes still match. It does not silently repair any change.

The manifest and log are separate files. A failure after manifest persistence
leaves that manifest as a lock and does not return completed freeze success.
The timestamp/log checks validate recorded attestations, not visual reading.

`checkpoint` requires at least 3,600 seconds since the first log time or previous
checkpoint creation. It creates a never-overwritten sequential ZIP beside
`out`, with all output files and scripts, excluding ZIPs, caches, and any
subdirectories named scans, witnesses, context, or upload. It does not upload;
root must save each ZIP persistently and record upload results. An earlier ZIP
is never nested, deleted, renamed, or overwritten. A failed upload can be retried
with the same existing ZIP, without creating an extra checkpoint.

## Importable API

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path('out/scripts').resolve()))
from manage import Project, check_latex

p = Project()
p.save_record(manually_authored_dict)  # completion status preserved from disk
p.mark_done('156-4', 2)
p.mark_audited('156-4', 2, audit_note='actual reader-authored audit record')
p.render()
p.syntax_check()
p.freeze()
p.verify_freeze(log=True)
p.checkpoint()
```

Use `Project(out=..., page_map=...)` for explicit paths. The script supplies no
image reader and does not access or open the attached context packet.
