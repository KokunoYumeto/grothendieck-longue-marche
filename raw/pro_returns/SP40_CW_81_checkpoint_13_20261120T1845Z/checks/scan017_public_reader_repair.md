# Scan017 — public reader display repair

Root's approval gate found 31 missing public reader slots on 17 decision rows. All 31 slots had an already-audited `reader_tex_proposals` attachment. This repair copies each exact excerpt and its recorded scope into the public `readers` field, with a source reference. The eight source-absence notes stay within those existing spans.

Every original mapping is preserved verbatim as `decisions[].readers_report_only`; every pre-existing public reading is unchanged. The added source pointers are retained in `decisions[].public_reader_source_provenance`. All 56 decisions now account for A, B and C. No unanimity has been inferred.

- Record before repair: `ad6d9c2e4814117cc541d7ce6101648eb2825b9dc290d06f255caef9a9bab0fa`.
- Record after display repair: `ea78de31c1fd67749e3d11a5ffb99412930a99c0e0e38a76d58e86d1a7e3a055`.
- Original source audit, before its authorized addendum: `4b12b4a0920de5850c4a9dc5206f85eb19a53f9417b03b005b067e3b7bde4b7d`.
- Selected TeX remains: `fe88173436631d1c0257cd4cc5857613fcce5bd8aef1de48a4ae3a5a485aaa7f`.
- Selected source map remains: `e1f1c00e67bcc9d3234f3d24c1e580ddbfa1a89857804b5fe17d0c2ea3316ca8`.
- Counts remain C 22 / H 33; 56 decisions, 18 doubts, 39 inventory entries.
- Original approval states remain false; root approval is pending.

## Exact existing source references

Pointers below are within `scan017_record_draft.json`; character intervals and scopes are copied from the existing attachments. No source file was opened or recalculated for this repair.

| Decision | Added reader | Existing attachment pointer | Source interval | Recorded scope |
| --- | --- | --- | --- | --- |
| 017-S01 | A | `/decisions/8/reader_tex_proposals/A/0/attachment` | `A.reading.tex [269,290)` | literal current-reader closure bar; already in both witnesses |
| 017-S01 | B | `/decisions/8/reader_tex_proposals/B/0/attachment` | `B.reading.tex [311,332)` | literal current-reader closure bar; already in both witnesses |
| 017-S01 | C | `/decisions/8/reader_tex_proposals/C/0/attachment` | `C.reading.tex [278,299)` | literal current-reader closure bar; already in both witnesses |
| 017-S02 | A | `/decisions/9/reader_tex_proposals/A/0/attachment` | `A.reading.tex [315,336)` | literal current-reader closure bar; already in both witnesses |
| 017-S02 | B | `/decisions/9/reader_tex_proposals/B/0/attachment` | `B.reading.tex [357,378)` | literal current-reader closure bar; already in both witnesses |
| 017-S02 | C | `/decisions/9/reader_tex_proposals/C/0/attachment` | `C.reading.tex [324,345)` | literal current-reader closure bar; already in both witnesses |
| 017-G13 | A | `/decisions/10/reader_tex_proposals/A/0/attachment` | `A.reading.tex [340,360)` | ordinary period representation at second equality endpoint |
| 017-G13 | B | `/decisions/10/reader_tex_proposals/B/0/attachment` | `B.reading.tex [382,402)` | ordinary period representation at second equality endpoint |
| 017-P01 | A | `/decisions/11/reader_tex_proposals/A/0/attachment` | `A.reading.tex [253,374)` | exact first/second equality layout |
| 017-P01 | B | `/decisions/11/reader_tex_proposals/B/0/attachment` | `B.reading.tex [295,416)` | exact first/second equality layout |
| 017-P01 | C | `/decisions/11/reader_tex_proposals/C/0/attachment` | `C.reading.tex [262,735)` | exact first/second equality layout |
| 017-S03 | A | `/decisions/13/reader_tex_proposals/A/0/attachment` | `A.reading.tex [403,425)` | literal current-reader closure bar; already in both witnesses |
| 017-S03 | B | `/decisions/13/reader_tex_proposals/B/0/attachment` | `B.reading.tex [445,467)` | literal current-reader closure bar; already in both witnesses |
| 017-S03 | C | `/decisions/13/reader_tex_proposals/C/0/attachment` | `C.reading.tex [764,786)` | literal current-reader closure bar; already in both witnesses |
| 017-G12 | A | `/decisions/20/reader_tex_proposals/A/0/attachment` | `A.reading.tex [1369,1494)` | complete slanted-note source through closing wrapper |
| 017-G12 | C | `/decisions/20/reader_tex_proposals/C/0/attachment` | `C.reading.tex [1800,1947)` | complete slanted-note source through closing wrapper |
| 017-N04 | C | `/decisions/25/reader_tex_proposals/C/0/attachment` | `C.reading.tex [2677,2692)` | following live word and its literal accent |
| 017-N05 | C | `/decisions/30/reader_tex_proposals/C/0/attachment` | `C.reading.tex [3336,3352)` | plural word and its literal accent |
| 017-G05 | B | `/decisions/33/reader_tex_proposals/B/0/attachment` | `B.reading.tex [3378,3393)` | plain dotted j and alpha, with no separate upper-mark representation |
| 017-G05-index | A | `/decisions/34/reader_tex_proposals/A/0/attachment` | `A.reading.tex [2967,3005)` | ordinary dotted j plus separately qualified prime/dot upper mark |
| 017-G05-index | B | `/decisions/34/reader_tex_proposals/B/0/attachment` | `B.reading.tex [3378,3393)` | plain dotted j and alpha, with no separate upper-mark representation |
| 017-G11 | B | `/decisions/35/reader_tex_proposals/B/0/attachment` | `B.reading.tex [3378,3446)` | complete display endpoint to following prose; no right-pair source component |
| 017-G11-upper | B | `/decisions/36/reader_tex_proposals/B/0/attachment` | `B.reading.tex [3378,3446)` | complete display endpoint to following prose; no right-pair source component |
| 017-G11-lower | B | `/decisions/37/reader_tex_proposals/B/0/attachment` | `B.reading.tex [3378,3446)` | complete display endpoint to following prose; no right-pair source component |
| 017-N06 | C | `/decisions/38/reader_tex_proposals/C/0/attachment` | `C.reading.tex [4673,4705)` | final-paragraph word and its literal accent |
| 017-G06 | C | `/decisions/39/reader_tex_proposals/C/0/attachment` | `C.reading.tex [4710,4753)` | first-union context has no separately represented preceding point |
| 017-D12-final | B | `/decisions/49/reader_tex_proposals/B/0/attachment` | `B.reading.tex [6224,6264)` | exact complete-state alternatives, including final J |
| 017-D12-final | C | `/decisions/49/reader_tex_proposals/C/0/attachment` | `C.reading.tex [7023,7063)` | exact complete-state alternatives, including final J |
| 017-ARCHIVE | A | `/decisions/55/reader_tex_proposals/A/0/attachment` | `A.reading.tex [6452,6478)` | literal archive comment; no C text or H text change |
| 017-ARCHIVE | B | `/decisions/55/reader_tex_proposals/B/0/attachment` | `B.reading.tex [6647,6673)` | literal archive comment; no C text or H text change |
| 017-ARCHIVE | C | `/decisions/55/reader_tex_proposals/C/0/attachment` | `C.reading.tex [7334,7360)` | literal archive comment; no C text or H text change |

## Narrow verification

A single in-memory structural comparison restored the complete original record object after removing only the added metadata/provenance and restoring `readers_report_only`. It matched exactly. All original reader entries are unchanged, and every A/B/C public slot is populated. No reader file, selected TeX, selected map, count, ink decision, source attachment or approval state was changed. There was no repeated span audit, image inspection or mathematical computation.

## Root-authorized S identity propagation

After accepting all 31 public reader additions, root requested direct propagation of the already-audited source identity on the three existing zero-count rows `017-S01`, `017-S02` and `017-S03`. Each now has `S_id = SA01-K81-06` and `S_status = confirmed from root crop; current C and H already contain the overline`. The supporting root journal sections are 03 and 05. These six added fields supply the public-log source identity; no ink choice, count or source span changes.

- Record after these six metadata fields: `204ded1dd8bf551b303cb794f88a18de95fbf5a0713df51afa5df3be01ef1572`.
