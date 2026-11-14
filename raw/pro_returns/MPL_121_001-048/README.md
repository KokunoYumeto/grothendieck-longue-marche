# MPL_121_001-048

## Deliverable

This package contains the diplomatic LaTeX transcription of all **43 retained scans** supplied for cote 121, with a second visual reading of every page and a cross-page notation comparison completed before the context was opened. The five blank scans omitted in the supplied source description are 003, 025, 029, 038 and 040.

| File or folder | Contents |
|---|---|
| `MPL_121_001-048_transcription.tex` | All retained pages in order, beginning with the cote and scan markers; a fragment without a preamble. |
| `pages/` | One LaTeX fragment for each retained scan. |
| `MPL_121_001-048_doubts.md` | Shared notation table, localized doubtful readings, abbreviation list and legibility assessment. |
| `MPL_121_001-048_inventory.csv` | 825 element rows, each marked `yes`. |
| `MPL_121_001-048_notes.md` | 115 separately identified research items, the four requested questions, standing sections and bibliography. |
| `progress.log` | UTC page-completion and audit entries, checkpoint records, freeze hashes, context opening and final verification. |
| `records/` | Page records, source and search ledgers, research assembly and validation scripts, checkpoint receipts and integrity evidence. |

## Transcription conventions and limits

The page fragments use the requested editorial macros, standard LaTeX and TikZ/tikz-cd. The package records **43 diagram blocks and 43 drawing blocks**; drawings are encoded in TikZ. The transcription includes uncertain readings, deletions, insertions and marginal writing in place. Its 317 grouped doubt entries document 440 occurrences of `\unsure`; the five `\illegible` occurrences concern unreadable words.

The main transcriber performed both visual passes in one stream. Helpers did not transcribe or visually audit any cote 121 page. Subsequent parallel work concerned research sources and review of the separate notes; the technical helper checked syntax without choosing manuscript readings.

All 43 page fragments passed the recorded LaTeX syntax check. The validation environment lacked `ulem.sty`, so its harness used transparent wrappers for underlining and editorial markup; this check establishes syntax under that documented harness, and does not certify visual fidelity of those wrappers or replace the image-by-image audits. No PDF compilation is offered as a substitute for the requested fragments.

## Freeze and records

The transcription was frozen on **14 November 2026 at 17:14:12 UTC**, after all second audits and notation checks. `records/frozen_sha256.json` contains the hashes of all 43 page files and the combined fragment. The combined SHA-256 is:

```
27f80a98251c590926e0855ce159fd55970124bdbb70420b2904efbb7c7047b0
```

The context-opening entry follows the freeze entry. Research did not modify any frozen file; the final verification is recorded in `progress.log` and `records/final_validation.json`.

The scripts that originally saved and audited pages are retained as historical work records. Running those writing scripts creates a new working version; the delivered frozen copy is identified by the manifest above. Research assembly scripts operate on the English notes only.

The user-supplied scans and context, inspection crops, and external source PDFs/images are excluded from this package. The notes cite their locations precisely; source ledgers retain retrieval and inspection evidence. Earlier working research memos have been integrated into the main notes and consolidated as source-inspection records.
