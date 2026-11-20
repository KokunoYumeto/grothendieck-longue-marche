# Second-pass workflow

## Scope and independence

The 27 scans are handled in the supplied page-map order. For each page the main reader launches three fresh, separate subagents with no inherited conversation. Each receives that page’s images, C and H texts, C’s page-specific doubts/notes, the conventions, and the shared notation table as it stands before the page. Readers are forbidden to inspect one another’s files or other pages. Each supplies a full LaTeX reading and a structured report; those original returns are retained under readers/.

The main reader compares the three full readings and their evidence, inspects their tight crops or makes a single additional tight crop when none was supplied, and records the selected reading with all three alternatives. Consensus is not substituted for ink evidence. Agreed readings are supported by three independent whole/half readings; disagreements are adjudicated from retained crops. No OCR, text-recognition library, PDF text extraction, external transcription or web research is used.

## Reader brief, first version

The full first-used brief is preserved in briefs/brief_v01.md, first used for scan 009. Conventions are in briefs/conventions.md, extracted from the supplied prompt’s transcription rules. The current task’s three-reader method supersedes the former prompt’s one-reader workflow.

## Reader brief, last version

Currently brief_v15.md, first used scan 031. The final version and every intermediate version remain under briefs/. Page records identify the version actually supplied.

## Brief changes and their causes

Scan 009 led to version 02 (first used scan 010): supply the omitted H kind enum; count resolved/narrowed C doubts consistently; distinguish doubt marks from ordinary H notes; require close evidence before discarding punctuation as noise; distinguish separate raised entries from textual insertions; keep literal reading fields and short content notes. The same-page enum clarification was sent equally to all three readers and is preserved separately. The lower 39 period, insertion status of the test-category line, and differing doubt counts motivated these changes.

## Crop accounting

Each crop records source, original-pixel box, rotation, output width, reason and UTC creation time in crops.jsonl alongside the resulting JPEG or PNG. The whole and halves are viewed once by each reader and are not counted as crops. Crops made by different independent readers of the same locus count separately. The main reader reuses an existing crop whenever possible. Per-page totals will be listed here after adjudication.

## Page completion and checkpoints

A page file, decision record, assembled changes/collation/inventory/notes and a progress line are saved before the next page begins. Every 45 minutes, a new numbered checkpoint ZIP is saved, excluding source attachments, convenience witness input copies, and earlier checkpoints. The final ZIP contains all deliverables and retained work documentation. Page and combined-transcription SHA-256 values are recorded when frozen and rechecked at the end.

## Mathematical checks

Readers follow mathematical syntax and the local argument, but the visible ink determines the transcription even when a statement looks false or malformed. CHECK_EVENTS.tsv records only checks or substantive use that actually occurred, with the model/run and the exact type. Merely transcribing a statement is not labeled a proof or check. Notes report the page’s own qualifications and questions without resolving them from outside sources.

## What worked and what did not

To be completed from the actual run.


### Crop counts through scan 009

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 009 | 10 | 14 | 14 | 11 | 14 | 49 |

Scan 010 led to version 03 (first used scan 011): constrain inventory sheet_kind/kind to the requested enums; compare H together with its explanatory notes rather than counting flattened but explicitly documented interlineations as omissions; distinguish cancelled-letter certainty from deletion extent; retain all C-context decisions; display crops in smaller groups after one output-truncation incident. The cancelled n was resolved by A/B but retained by C and the main reader; this was an ink uncertainty, not a majority vote.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 010 | 4 | 5 | 4 | 9 | 5 | 22 |

Scan 011 led to version 04 (first used scan 013): literal quote shapes must not be excluded as macro equivalence (A/B excluded them, C included them); inherited H notes must accompany the page they govern; cancelled-word letters must be distinguished from secure deletion extent and live replacement; distinguish physical block evidence from TeX reflow. The main reader recovered H’s preceding note about the red stroke after started and excluded that claimed omission. This revealed an input-context limitation, recorded here rather than attributed to H.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 011 | 9 | 8 | 7 | 8 | 9 | 32 |

Scan 013 led to version 05 (first used scan 014): resolving a contextual alternative while retaining identical literal C text does not count as a C change. The same-page clarification was sent equally to all three readers and is retained in briefs/clarification_scan013.md. One reader’s initial counting interpretation caused it; no peer reading was disclosed. The three texts agreed exactly after removing cote wrappers. Real mathematical checks were recorded separately: exponential construction and grading scope, without changing the manuscript.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 013 | 3 | 1 | 0 | 0 | 0 | 4 |

After scan 014, no brief change: all three full texts were byte-identical to C and no procedural ambiguity was reported. The alphabet crops settled individual visual questions; their agreement did not require root re-cropping. Three local low-degree/variance checks and the main reader’s recheck were logged with their limits.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 014 | 3 | 4 | 4 | 0 | 0 | 11 |

After scan 015, version 05 remains unchanged. All three readings confirmed C, including the awkward wording and handwritten note. A/B settled the capitals in the halves; C used two tight crops for its remaining capital/index questions. Each followed the once-per-view rule. The groupoid-classifier question received bounded mathematical checks, separately recorded from transcription.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 015 | 0 | 0 | 2 | 0 | 0 | 2 |

After scan 017, version 05 remains unchanged. The underline and quotation changes were unanimous; B retained the plus alternative that A/C and the main reader excluded from the closed loop. This was an ink judgement, not a brief ambiguity. The main reader reused three crops. One earlier output was truncated and did not count as a view; those three crops were subsequently displayed singly.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 017 | 5 | 7 | 5 | 0 | 3 | 17 |

Scan 018 led to version 06 (first used scan 019): mark a recurring uncertainty at every occurrence whose own ink remains uncertain. All three reports doubted both Latin initials but retained C’s convention of marking only the first; the main reader inspected both and marked the second too. Also compare exact witness text before claiming a difference: reader C withdrew a preliminary comma-omission claim after its final literal diff showed the commas already present. No false comma rows entered the final apparatus. The other differences were ink judgements, with retained doubts where spacing and fused strokes stayed ambiguous.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 018 | 11 | 9 | 15 | 0 | 10 | 35 |

After scan 019, version 06 remains unchanged. The three full readings were identical, with one resolved period/comma doubt and one retained closing-quote doubt. The exact-diff requirement produced no false collation claims. Root reused one crop. A transient exec transport failure during this page recovered on the next retry with the workspace intact; no restoration or extra checkpoint was necessary.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 019 | 5 | 4 | 3 | 0 | 1 | 12 |

Scan 021 led to version 07 (first used scan 022): explicitly prohibit compilation, format building and installation, as the supplied source prompt already required. That instruction lay outside the excerpted Absolute rules. Reader A attempted a compile and it failed at the missing-format stage; no compilation completed. Its diagnostic is retained in readers/021/A/qa/. The main reader used static checks and added the rule to the brief.

The new witness folder also exposed an input-extraction defect: C notation used the scan in the second table column and C notes used numeric table rows. Missing current-page rows were supplied equally to all three readers in C_context_addendum.md during their crop stage, without peer output or reopening images. Extraction was repaired for future inputs and restoration; briefs/context_correction_scan021.md records the incident.

The root confirmed two long side rules, a faint additional far-left trace and a small isolated wavy stroke absent from C. Four new drawing crops were needed because readers settled those marks from the halves. The long narrow crops were rotated 90 degrees for practical full-length viewing. The faint trace is reproduced without claiming a material origin or exact endpoints. No missing top-line phrase was reconstructed. Reader C’s invalid-coordinate crop command produced no image; its corrected one is counted once.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 021 | 18 | 18 | 21 | 4 | 14 | 61 |

Scan 022 led to version08 (first used scan023): preserve the physical side of marginal notes, since only readerA explicitly placed the cancelled p122 note on the left while the others retained a normally right-side margin macro. The brief also makes explicit that one physical punctuation group is represented once when its line attachment is uncertain. All three readers recognized C's duplicate assignment of the pair between the first two entries, but proposed different placements; root retained the low physical position with attachment doubt. This was an ink ambiguity rather than evidence for two pairs.

Root resolved the cancelled does, st and work from surviving letter contours, recorded the dissenting readings, and retained uncertainty for buried fragments, fused quote groups and the low hooked sign. The minor syntax error in the root adjudication script was corrected before it wrote a page record. A preliminary period-omission suggestion was excluded after literal C comparison showed the period already present. Static validation and literal C/final checks passed. The 45-minute checkpoint02 was created while this page was in progress, at10:27:27UTC, and its durable save was acknowledged at10:27:59UTC.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 022 | 26 | 23 | 26 | 3 | 30 | 78 |


Scan 023 led to version 09 (first used scan 024): check quote strokes separately at each edge of cancelled phrases. All three readers retained C’s cancellation of the opening pair before now or never; root’s crop shows that pair clearly outside the zigzag, while the words and closing group lie inside. This prompted a more explicit scope instruction. The different old-digit and opening-quote readings were ink judgements, each decided and recorded. A raised isolated point is reproduced without assigning its function; a separate low mark after the first reference remains comma/stop. The three round superscripts are independently marked.

Root reused 18 reader crops and made three narrow geometry crops (left arrow and two long rules). The first attempt to display A07–08 was fully truncated; they were then displayed successfully and counted only once. The reader returns, full-text differences, context decisions, inventory and all 15 final literal differences were checked before commitment. No compilation or mathematical verification was claimed for the isolated map.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 023 | 17 | 13 | 11 | 3 | 18 | 44 |

### Scan024 review and brief_v10 (first use025)
Three fresh readers returned independently. Root settled26 C changes and retained C against two reader proposals. All three initially separated full-height rules from the text; root anchored them to the reference/text columns and clarified that geometry relationship for025. The p205 upper streak/low point are represented once each without declaring their function. A fully truncated combined crop output was not counted as viewed; the crops were re-displayed singly. One very tall existing crop was rotated for inspection without recropping or enhancing again; its derivative is logged separately and counts as reuse. Seven bounded variance/type checks are recorded; none selects uncertain handwriting.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 024 | 24 | 28 | 25 | 3 | 30 | 80 |


### Scan025 review and brief_v11 (first use026)
Three fresh readers completed whole/halves and their frozen crops independently. Root settled31 C changes and retained C against two reader proposals. A third index, a cancelled delimiter and the terminal exclamation state remained independently uncertain. The high cancellation and wavy continuation were restored, also moved to its observed lower level, and the raised it/caret preserved. The long rules are anchored in the same layout as the text. Version11 distinguishes an uncrossed mark outside a cancellation from separated parts straddling a cancellation path. Four limited reader mathematical checks are recorded; root made no independent proof claim. A root-script quotation syntax error was corrected before any page record was written. The fully truncated rule-image display was not treated as inspection; both existing crops were successfully re-displayed. Checkpoint03 was created at11:13:48UTC and its durable receipt acknowledged at11:14:29UTC.

| Scan | A | B | C | Main new | Main reused | Total distinct crops |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 025 | 28 | 21 | 22 | 3 | 31 | 74 |

### Version12 — first used scan027

Scan026 readers all printed the corrected278 reference as complete old18 followed by17, although the root crop shows one shared leading1 and overlapping final digits. Version12 makes the once-only glyph rule explicit for overwritten references. ReaderB also extended the faint left trace much farther than readerC; its existing middle crop did not establish the endpoints. The next brief asks readers to record the observed extent. Root used a separate narrow endpoint crop and followed the shorter visible trace.

### Brief version 13 — first used scan028

Scan027 exposed different treatment of the same clipped note: A printed the readable fragment certa, while B/C retained certain as an alternative despite the missing continuation. Readers also ordered the single/double alternatives at the cut quotation differently. Version13 distinguishes uncertain surviving ink from absent continuation and asks that the visible stroke count lead the alternatives. The three-reader comparison also caught would’nt, a cancellation-state disagreement at313, and geometry omitted from C. Root reused40 existing reader crops and made2 narrow full-extent rule crops (28/27/21 reader crops;78 distinct). Existing A04/A08/A12/A13/A14 crops were re-displayed only while respective decisions were open; A21/A22 were recovered singly after a truncated output. No second crop of a decided locus was made. The faint circular margin features were recognized as material holes, not ink drawings.

### Brief version14 — first used scan029

On scan028 reader A treated pale circles as material features, while B/C reproduced them as drawings of unspecified origin. B additionally connected several faint flecks into a curve/line that the root crops did not support. Root preserved distinct dark marks with unassigned origin, rejected invented continuity and kept material appearance out of the ink drawing. Version14 makes that distinction explicit without permitting omission of faint ink. Root made18 new crops and reused24 reader crops; image-output truncations were recovered by redisplaying the same existing files, not recropping. All38 decisions, including three unchanged-C decisions rejecting reader proposals, were documented.

### Scan029 review — brief14 retained for030

The three returns differed on the cancelled Formulae ending, formula signs, faded reference numerals, joined quotes and isolated marks. Root used37 existing reader crops, no new crops, and recorded31 decisions (29 changes from C). Four inherited C doubts were resolved from surviving strokes; the terminal formula alternatives were reordered, and uncertainty was retained elsewhere. The existing local-count and material-feature guidance already covered these disagreements, so no new brief version was needed. A null crop-field exception stopped the first adjudication-script invocation before any page/record write; the corrected invocation and static/literal checks completed. A truncated A26 image output was redisplayed from its existing file.

### Scan030 context correction during reading

A numeric row-ID collision and a corner-number collision introduced two unrelated rows into030 C_context. The extractor now locates the Scan column from each table header. The wrong rows were removed, every genuine030 doubt retained, and the same addendum sent to all three readers without reopening whole/half images. Future031–038 contexts were rebuilt. The correction is documented in context_correction_scan030.md.

### Review after scan030; brief_v15 first used031

Three independent readers made26,25 and28 crops. Root reused39 and made one crop of the previously uncovered380 closing area after B omitted a closer on an opener-focused crop. The broader local evidence separates the preceding ff descenders from one detached closing slant; single/fused-double remains marked. Root also corrected a provisional mistaken identification of the faint first-row group as the already-transcribed4 by comparing source coordinates. No new crop was needed for that correction. The header-aware C_context fix was sent equally to all three readers. Final030 has25 C changes,27 decisions,75 inventory entries and16 remaining reading doubts, with no H rows or mathematical check events.

Brief_v15 requires full disputed-edge coverage before asserting absence and a source-coordinate comparison before merging faint nearby groups. The original reader files remain unchanged. Root final evidence paths name the crops actually viewed.

### Scan031 reflection

All three final returns compared. Long fading traces were preserved with origin unassigned after endpoint crops; circular material impressions were excluded. Root retained unresolved overwritten letters against majority resolution, distinguished numeral identity from cancellation scope, and added small detached remnants omitted in the returns. Brief v15 retained for032: these are ink judgments covered by the existing guidance, not a new instruction gap. A table row-spacing construct exposed a false positive in static display counting; the validator now tokenizes control sequences. No compilation.


### Scan032 reflection

All three readers completed19,23 and14 crops. Root reused29 distinct reader crops and made8 crops of newly frozen loci, including previously uncovered rule tops and small far-right marks. The final record has33 decisions,32 C changes,99 inventory elements and11 doubts. Live quotation edges and uncertain terminal cancellation at440 were decided separately; the455 mark is drawn geometrically with its function unassigned. A single actual conditional mathematical counterexample was checked, explicitly without deciding the M/m ink or the undefined indexed category. Brief v15 retained: existing instructions cover the remaining difficulties. One non-unique replacement assertion stopped the first script before any output write; precommit review then corrected two drawing anchors without changing the ink decisions. No compilation.


### Main-reader scope correction at033

Root additionally displayed033 whole and both halves once, recorded in root_033_working.md, before comparing the reader returns. On rereading the full instruction, subsequent root work is restricted to the returns and local crops; the prescribed whole/half sequence belongs to the three fresh isolated readers. No repeat full-page/half view or extra image processing was made. This extra root viewing is a documented procedural deviation, not represented as part of the three-reader protocol.
