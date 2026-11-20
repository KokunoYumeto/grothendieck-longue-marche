# SP44_CW_36 — reading workflow

## Run and independence

The main reader is GPT-6 Astra Pro. The runtime does not expose a numerical reasoning-effort setting, so none is invented. Each page is assigned, in scan order, to three newly spawned agents, R1, R2 and R3, with no conversation-history fork. Each receives the current brief, only that page's images and witness extracts, C's relevant prior doubts/notes, and a snapshot of the notation table already decided. The readers are forbidden to inspect one another's files. They finish their page and take no later page. The main reader retains their written returns and views local crops to adjudicate all disagreements. Agents use the inherited model; model/effort metadata are reported only where exposed.

No OCR, PDF text extraction, text-recognition library, web search, or published text is used. The three source images for a page are opened once each by each reader. Subsequent image views are documented local crops, not enlarged re-readings of whole halves. Crop files and their JSON sidecars record source coordinates and operations. Reading text is never labelled a proof check.

## Brief versions

The complete first brief is `briefs/brief_v01_scan010.md`. All later versions, if any, are retained beside it with the scan first using them. Changes and reasons are recorded below as pages are adjudicated. The latest brief currently in use is `briefs/brief_v07_scan016.md`; the final record will identify the last version used.

| Version | First scan | Change and reason |
|---|---:|---|
| v01 | 010 | Initial explicit visual sequence, macro conventions, independent return schema, full inventory and honest mathematical-check classification. |
| v02 | 011 | Scan010: all readers lacked the preamble path; chi/ell, heavy E/Z, retained d, old/new closes and nonalphabetic prefix diverged. Added explicit path and guidance, clarified H macro equivalence and check-event categories, and removed duplicated report/JSON tables while retaining complete records. |
| v03 | 012 | Scan011: R2 alone retained three small old-letter layers; readers differed on typed/pen 2, round o/0 and paragraphing. Added stroke-based overprint/numeral comparison, underline encoding, whole-image bboxes for half-settled differences, paragraph cues, and explicit no-compilation reminder. |
| v04 | 013 | Scan012: credit H’s global chi-shaped-ell and emphasis conventions; distinguish editorial commentary from ink assertions, x-outs from hidden letters, uncertain correction chronology, and insertion guides from punctuation. Use small image batches. |
| v05 | 014 | Scan013: a rule begins inside et; readers diverged on the inserted Q source layer and a handwritten accent. Added partial-word underlining, separate type/guide provenance, literal accents, consistent C-doubt flags, product-glyph loci and paragraph/display placement. |

| v06 | 015 | Scan014: distinguish unchanged C confirmations from resolved doubts, different local overprint structures from recurring glyphs, prose correction layers, attached b retouch and survival of both pen/typed commas. |

| v07 | 016 | Scan015: require uncertainty agreement between complete text and JSON, distinguish identical repeated overlaps from clean later glyphs, and narrow clipped-word doubts to the unresolved ending. |

## Page record

This table is populated only after a page has been decided. Counts refer to actual saved crops; a crop may contain one crowded formula with several overwritten glyphs. Images viewed repeatedly are reported if such an exception occurs.

| Scan | R1 crops | R2 crops | R3 crops | Main-reader new crops | Brief | Observations |
|---|---:|---:|---:|---:|---|---|
| 010 | 12 | 13 | 13 | 3 | v01 | 38 independent crops (12/13/13); main reused 15 distinct reader crops and made 3 new loci. Disagreements exposed alphabet, retained-letter and parenthesis-layer issues. Preamble path and macro-equivalence guidance added for scan011. |
| 011 | 5 | 9 | 8 | 5 | v02 | 22 independent crops (5/9/8); main reused 9 reader crops and made 5 new loci. One five-image tool output was truncated before inspection; the same saved crops were then delivered in small batches and actually inspected, without recropping. v03 adds overtyping/numeral guidance, half-only bboxes and underline convention. |
| 012 | 14 | 13 | 15 | 7 | v03 | 42 reader crops (14/13/15); main reused 13 and made 7. A four-image output was truncated before inspection; the same four files were delivered in two-image batches, without recropping. v04 will clarify H global conventions, editorial notes, x-out semantics and uncertain old/live chronology. |
| 013 | 13 | 13 | 15 | 7 | v04 | 41 reader crops (13/13/15); main reused 13 and made 7. Every image was delivered in a one- or two-image batch. Disagreements exposed partial-word underline, typed prefix versus pen guide, literal accent and C-doubt counting issues; v05 clarifies them for scan014. |
| 014 | 22 | 16 | 16 | 5 | v05 | 54 reader crops (22/16/16); main reused 21 and made 5. One two-image output was truncated before inspection; the SAME saved trace_old/adherence_old files were resent individually, with no recropping. The page exposed distinct layers at apparently recurring capitals, overprints inside ordinary prose, and the need to separate unchanged C confirmations from actual C-doubt resolutions. v06 carries these clarifications. |
| 015 | 12 | 13 | 17 | 11 | v06 | 42 reader crops (12/13/17); main reused 15 and made 11. Two new coefficient images had a truncated initial delivery before inspection and were resent unchanged, one at a time. R2’s table and complete text disagreed about marking two small underline endpoints. v07 will require in-place and table doubts to agree, and will clarify identical-overprint shorthand and localizing clipped-word doubt. |

## Preservation and reproducibility

The supplied sweep correction table has six physical TSV records relevant to scans 010–027. Its joint `36/14, 36/16` record contains two separate loci, giving seven correction items before expanding the `36/18-26` scope. The prompt calls these seven rows. All six exact `where` identifiers are retained in `validation/S_scope.json`; the joint record is reviewed at both pages. Out-of-scope cote-36 rows are not imported into this transcription.

The supplied archive is extracted once into `source/`; it is not copied into deliverables. `scripts/prepare_packets.py` recreates page-local witness packets from the attachment. Such packets, original scans, original witnesses and sweep context are excluded from checkpoints and the final ZIP. Independent reader transcriptions/reports, adjudications, local crops, scripts and all cumulative deliverables are included. Checkpoints are new ZIPs at 45-minute intervals, with no earlier checkpoint inside a later one. The original UTC start appears on the first line of `progress.log`.

`scripts/build_records.py` only formats hand-authored decisions; it does not decide readings. Per-page decisions are committed before the next page is sent to new readers. Transcription hashes are frozen after all pages and syntax checks; the final verification checks those same hashes without changing the text.

## What worked and what did not

To be completed from the actual run, including disagreements and any workflow exceptions.


### Brief v04, first used on scan 013

Scan 012 exposed three recurring convention issues: H's global chi-shaped-ell note, its source-emphasis macro, and its clearly editorial explanation of g. The next brief credits these instead of miscounting them as source errors. It also distinguishes x-out characters from hidden old letters, uncertain chronology from certain deletion, and insertion hooks from punctuation. Small image batches reduce truncated outputs. The complete version is retained in briefs/brief_v04_scan013.md.

### Brief v06 — first used on scan 015

Scan014 exposed false C-change flags on unchanged literal typos, distinct correction structures at two superficially recurring product capitals, and overprinted prose letters. v06 clarifies actual C-doubt resolutions, local structural alternatives without invented chronology, attached letter retouches versus detached drawings, and survival of both inserted and typed commas.

### Brief v07 — first used on scan 016

Scan015 exposed a table/text inconsistency at two short underlines and different uses of first-occurrence overprint shorthand. v07 adds a direct final consistency check and explicit occurrence descriptions; it also localizes residual clipping uncertainty to the unresolved final glyph. No second inspection of a decided locus is requested.
