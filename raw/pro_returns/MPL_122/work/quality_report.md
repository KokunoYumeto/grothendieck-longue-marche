# MPL_122 — final quality record

## Scope and provenance

- Archive file: 122.pdf.
- Supplied nonblank faces: 32, scans 003–018 and 020–035.
- Omitted blanks as specified by the task: 002 and 019.
- All supplied full images and both halves were read directly, without OCR, by one primary transcription stream.
- Every page received the later image-against-text audit recorded in progress.log.
- Transcription frozen: 2026-11-17 11:24:06 UTC.
- Context opened: 2026-11-17 11:24:15 UTC.
- Final verification: all 33 frozen file hashes (32 pages plus combined fragment) unchanged, as logged.

## Deliverables and checks

| Item | Result |
|---|---|
| Combined transcription | Exact concatenation of the 32 fragments, in scan order; no preamble |
| Page files | 32 of 32 expected filenames and scan markers |
| Inventory | 503 rows; all transcribed=yes |
| Sheet classifications | 17 text, 15 reused_typed; no supplied cover or entirely cancelled_draft face |
| Inventory element classes | 203 text, 87 deletion, 63 margin note, 58 diagram, 52 display, 20 insertion, 20 drawing |
| Doubts | Package notation table; manual reading table; exhaustive uncertainty-macro locators; abbreviation register; legibility/format limits |
| Research notes | 69 individually located notes; 11 labelled own ideas with confidence and reasons/assumptions |
| Context checking | 69 executed queries, including zero matches where applicable; exact context file/line locations saved in context_searches.json |
| Research-register disposition | All five displayed matched Open rows and all eight displayed planning rows individually addressed |
| Standing questions | Authorial check/proof requests and unfinished/revised material; title and numbering register for all 32 faces |
| Structural validation | 0 errors, 0 warnings; output in final_validation.txt |
| TikZ-cd coordinate validation | 52 diagram environments, 278 arrows, 0 coordinate findings, 3 permitted explicit-empty targets; output in final_diagram_check.txt |

The inventory's 58 diagram elements also includes array/table structures; the coordinate checker counts only the 52 TikZ-cd environments. These are different counts of different objects.

## Limits

Mechanical checks establish source structure, ordering, inventory coverage, and hash identity. They do not prove every palaeographical reading. The least secure passages, coefficient and degree alternatives, and cancelled material are explicitly located in MPL_122_doubts.md.

A successful full TeX compilation was not available: the installed engines lacked the required formats and package files. The requested fragment requires a host document with the editorial macros, standard mathematics, TikZ/TikZ-cd, ulem, and the shapes.geometric library, including wrappers able to accept mathematical and block material. The text has been visually collated and source-checked, not certified by a rendered document.

The research audits were conducted after the freeze from the immutable text and supplied context. They are mathematical/contextual checks, not additional image readings or permission to alter the transcription.

## Work files

The work directory preserves page records, historical drafting scripts, notation/abbreviation/legibility working files, the frozen hash manifest, context-query records, and separate research/validation audits. Historical page-writing scripts are a record of drafting and can predate later visual corrections; **the frozen page fragments and their logged hashes are authoritative**. Do not regenerate them from a historical script and mistake that for the audited version.

The final ZIP excludes all supplied attachments, extracted context sources, scan images, enlarged crops, bytecode caches, and earlier checkpoint archives. The user's source images and context remain the external inputs needed to reproduce source comparisons.

