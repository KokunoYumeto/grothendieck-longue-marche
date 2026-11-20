# Page reader contract

Read only the scan assigned by the coordinator. If explicitly assigned a subset of mark IDs, inspect and submit every ID in that subset only, in source order; another reader handles the rest of this same page. Save to the explicit unique submission filename provided by the coordinator, so readers never overwrite one another. The coordinator merges disjoint submissions only after every mark on the page is covered. No later scan may begin until all marks on the current page are committed. This task is diplomatic transcription of Grothendieck's handwriting from supplied scans. Every decision must come from visually inspecting its own ink. OCR, text recognition, external transcription services, and PDF text layers are prohibited. Use Pillow only to crop, enlarge, adjust contrast or rotate for inspection, and view_image to look. Do not use ImageGen.

Sources relative to /workspace/scratch/18ee30ea2ccf:
- source/DM01_1_001-160_scans/1_scanNNN.jpg
- source/DM01_1_001-160_texts/pages/1_scanNNN.tex
- source/DM01_1_001-160_texts/MARKS.tsv
- source/DM01_1_001-160_texts/hua/hua_1_scanNNN.tex

Read the current page's marks and text, inspect its image, and locate every mark. The short deliverable/audit/READING_GUIDE.md records a few confirmed distinctions from earlier pages; it is an optional comparison aid, not authority for a new occurrence. Hua is optional comparison only; it is known to contain errors. Check actual image dimensions (scan003 is 1746x2230, despite the prompt's generic 1668x2150). Crop coordinates always refer to the actual unscaled source image, as x0,y0,x1,y1 with right/bottom excluded. A full-page view may settle clear text, but zoom small formulas, indices, accents, deletion remnants or ambiguous strokes. Several adjacent marks may share a crop. Full-page merely locating a word is not proof: look closely enough to distinguish proposed alternatives.

Write work/scanNNN.json with a top-level object:
- scan: integer
- reader: 'GPT-6 Astra Pro; effort not exposed; run /root/ACTUAL_AGENT_NAME'
- started_utc, finished_utc: actual UTC timestamps
- rows: a list of {id,scan,decision,reading,'what the ink shows',crop,confidence}
- views: list of {path,box,scale,contrast,purpose}; include only views actually inspected
- other_errors: list of {scan,place,'the reading','what the ink shows'} (no edits). Here 'the reading' is the EXISTING source text that appears wrong; 'what the ink shows' describes the visible correction and its distinguishing strokes.
- patterns: list of {name,marks,description} supported by this page's own ink
- notes: concise limitations, disagreements or workflow insights

The primary `finished_utc` is the actual finish of the final own-ink primary review, including any later targeted revision of your assigned mark. Preserve the initial report and initial finish time before revision, and record the extra actual view and revision interval. A separately assigned independent check of another reader's IDs has its own report, times and views; do not add those views to the primary log. Elapsed primary intervals may include waiting between phases and must not be described as continuous active-reading time.

Decisions:
first = literal first candidate with only the unsure wrapper removed.
alternative = a listed candidate after the first, without wrapper.
other = another reading, supported by ink.
undecided = retained/narrowed uncertainty where the ink does not distinguish. Use \unsure{...} around only the unclear part where possible; a wholly unreadable original \illegible{n} can stay as is. Do not force resolution; do not claim ink fails merely because you have not zoomed enough. Confidence high/medium/low relates to the reading, and uncertain readings are normally low.

Use a concrete observation in 'what the ink shows' for EACH mark, such as loop, crossbar, downstroke, dot, accent, positional index, visible word sequence. Avoid empty formulae like 'matches the first reading' or generic copied claims. It is fine to say a feature is obscured or absent where inspected. For alternatives and new readings say how the visible strokes distinguish them. Do not infer from mathematical correctness or linguistic grammar alone. All mathematical background used for location remains subordinate to the handwriting.

Keep each observation concise, normally one or two sentences containing the actual distinguishing strokes and any material obstruction. Keep view-purpose notes short and specific; relative workspace image paths are sufficient in the view log, while decision rows require source-pixel coordinates. Compact tuple-to-dictionary code may reduce repetitive serialization, but every row must explicitly supply its own inspected decision, reading, evidence, crop and confidence; never fill unread rows or bulk-assign a decision. Concision changes annotation overhead, not inspection depth.

For a targeted peer check with a supplied source box, start with that box and enough neighboring ink to establish the location. Use a full-page locator only if needed, and add another view only to resolve a named remaining feature. There is no fixed crop limit: sufficient own-ink inspection remains mandatory.

For formula alternatives differing in repeated letters or powers, account separately for every baseline letter and superscript at adequate magnification before assigning high confidence. A cancellation stroke may conceal a second baseline letter; a concrete same-page superscript/number comparison can discriminate a looped star from 2. No extra view is required when the existing inspected crop already resolves these features.

Preserve spelling, abbreviations, accents, deletions, insertions and LaTeX structure. Do not fix unmarked text. Record unmarked errors separately. Before labeling an observation as an other_error, confirm it lies outside EVERY listed mark on the page, not merely outside your assigned subset; send a concern about another assigned mark to the coordinator instead. If an observation needs adding/removing a word outside the mark, log it; only the original mark span may be replaced.

MARKS.tsv contains nested marks M0771/M0772, M0779/M0780, M2170/M2171 and a few escaped-brace/truncated entries M1340, M2152, M2285 plus newline normalization M2534. Use the balanced actual source span, coordinate with the reconciliation script, and still provide a row for every listed ID. Parent and child readings must be consistent.

Never generate defaults that mark unread ink 'first', 'undecided', or 'checked'. Every written row must have been personally inspected. Never fabricate timing or crop viewing. For hard cases ask the coordinator for independent reading while continuing the other marks on this same page. An independent check is useful when a plausible new reading competes with the original, rather than for every clear instance.

Keep image context scoped to this page. Do not commit or open the next page unless the coordinator explicitly authorizes it. Return the JSON path, counts by decision, hard IDs needing review, and any meaningful pattern. Root handles compilation, progress.log and checkpoints.

Return plain paths and a concise result to the coordinator; do not offer individual downloads. The user receives only the final combined ZIP.
