# Scan 032 — independent reader B

## Identity, time, scope

- Identity: independent reader B; model inherited; effort not exposed.
- UTC start: 2026-11-20T09:58:09Z, first recorded timestamp after reading the brief and supplied text inputs.
- UTC end: 2026-11-20T10:02:59+00:00.
- Read the entire v06 brief, this scan's C.tex, H.tex, C_prior_questions.md, the supplied notation snapshot, PREAMBLE.tex, and the crop helper's implementation. Prior notes served only as questions to revisit.
- No other-page image, other-reader file, root decision, OCR, text-recognition service, outside source, or TeX compiler was used.

## Viewing sequence and crop record

The full image was opened once for layout, followed by half `_a` once at its supplied resolution, followed by half `_b` once at its supplied resolution. Neither a full source nor a half was reopened or enlarged. Four newly generated crops were opened once each. Source metadata gives full dimensions **1679 × 2362**; each supplied half is **1679 × 1261**.

The following tight crops were made with the documented positional `crop.py` interface. All use width 2800, rotation 0, autocontrast, LANCZOS enlargement and `UnsharpMask(1.0,130,3)`. Exact source boxes and generation times are in `crops.tsv`.

| Crop | Full-image box | Open issue and result |
|---|---|---|
| `B_prose_fields.png` | `[970,425,1190,488]` | Two mixed-impression F glyphs and their indices; regular typed cores with outer handwritten strokes. The short dash is also visible. |
| `B_first_display.png` | `[420,597,1158,682]` | First group alphabet, typed/handwritten boundaries of three Fs; the A alphabet remains fraktur/calligraphic. |
| `B_second_display.png` | `[420,688,986,759]` | Local alphabet and hand boundary of S plus two Fs; S is fraktur, and F cores/digits are typed. |
| `B_deux_punctuation.png` | `[257,296,479,343]` | Pale baseline mark in the cell after `deux`; point versus unassigned trace remains open. |

The first three filenames and boxes were sent early to the main reader. The fourth was sent as soon as its punctuation issue was isolated while writing the detailed prose record. Every crop is in `/workspace/scratch/888e3fda13a9/crops/scan032/B/`.

## Layout and full inventory

This is a portrait typescript sheet with a five-line paragraph near the top and a separate two-row mathematical display below it. The paragraph runs approximately from x265 to x1598, y238 to y535. The displays occupy roughly x431 to x1143, y608 to y749. Most of the sheet is blank. The lower-left archive numeral is 31, at approximately x46–100, y2284–2322; it is represented only by the archive-number comment.

The typed paragraph is inventoried separately from the typed display rows. The two hand-drawn group capitals are separate additions. Each of the seven outer-left F doubling strokes is separately inventoried, leaving its base F and lowered digit in type. The pale mark after `deux` has an inventory entry with unknown origin and doubtful textual status. All these elements are represented in page.tex. The detailed inventory is in review.json.

There is no heading, letterhead, signature, manuscript page number, recoverable deletion or overtyping, underline, caret, arrow, diagram, or textual marginal note. The blank area and sheet edges were read on the full view and `_b`. Isolated dark specks were visible near x559 y96, x1469 y1608 and x1504 y1750; faint traces or fibres occur near x1060 y1978 and x41 y2202. They furnish no letter or articulated drawing, and their verbal role and physical origin are unassigned. No graphic reconstruction is supplied from these isolated specks. The lower-left 31 has no adjacent coherent opaque shape comparable to the one described in the supplied prior-page notes; no other-page image was consulted.

## Line-by-line reading record

### Paragraph, line 1

`En relation avec l'icosaèdre, nous découvrirons que les corps de caractéristique`

All characters read on `_a`. The opening E and following n are clear. The apostrophe after l is a single high type stroke. `icosaèdre` has the grave accent, then a comma. `découvrirons` has the acute over its first e; its ending is `-rirons`. `caractéristique` ends in `-tique`, with the acute on é. The faint brownish trace below/right of the terminal e is outside the typed baseline; no punctuation reading is supplied there. C and H agree on the words and accents.

### Paragraph, line 2

`deux[optional point] et cinq jouent un rôle très particulier, tant pour l'étude des réalisations`

The x in `deux`, q in `cinq`, full `jouent`, and endings `particulier` and `réalisations` were inspected. `rôle` has a circumflex; `très` has a grave. The comma after `particulier` and the apostrophe/acute in `l'étude` are clear. `réalisations` has the opening acute.

A pale compact oval is visible on the baseline in the typewriter cell between x and the e of `et`. The dedicated crop separates it from the x serif. It is much lighter than the surrounding type. It can be read as a faint point or left as an unassigned trace. This is retained locally as `deux\unsure{.|} et`: the empty second alternative denotes absence of a linguistic point. This is the sole recommended change from C, and it is doubtful. Neither grammar nor an expected sentence supplies the point. Confidence: low.

### Paragraph, line 3

`géométriques, que pour l'étude combinatoire abstraite, qui peut s'expliciter`

Both acute accents in `géométriques` were inspected, with the comma immediately after the final s. The apostrophe and acute in `l'étude` repeat clearly. The end of `combinatoire` is `-toire`; `abstraite` has a comma. `qui peut` and the single apostrophe in `s'expliciter` are clear. The terminal word ends `-citer`. C and H match this line.

### Paragraph, line 4

`par des notions de géométrie sur les corps F₄ et F₅ - ces deux dictionnaires`

`notions`, both accents of `géométrie`, `sur les corps`, and the double n in `dictionnaires` were read. The first field is F with a lowered 4 and the next is F with a lowered 5. Each F has its ordinary typed stem and right arms, with an extra left stroke. The first added stroke bows from the upper-left corner to the foot; the second is much paler and partly discontinuous near the top. The digits repeat the regular typed outlines visible in the formulas. The dash is one short typewriter stroke. C keeps a short dash; H's `--` would lengthen it. Both witnesses contain the same words. The handwritten boundary differs from H at each field.

### Paragraph, line 5

`étant subordonnés aux "isomorphismes exceptionnels" :`

The opening é in `étant` and the acute in `subordonnés` are visible. The spelling `isomorphismes exceptionnels` was read through each ending, including the double n in `exceptionnels`. There is a visible blank typewriter cell between `aux` and the opening double-quote cell. Each quotation endpoint is a pair of high strokes. The closing pair follows the final s; a spaced colon follows. C and H's quote notation differs syntactically but encodes the same paired marks. No missing passage occurs.

### First displayed row

The handwritten first capital has a rounded open outer enclosure, an inner oblique and a returning right foot. I retain C's first-candidate `\mathfrak A` with `\mathcal A` as the ink-supported alphabet alternative. The low 5 is typewritten, with a flat top and curved lower bowl. No cross-page shape comparison was performed.

The row continues with a wave above one straight rule, then typed `Sl`: uppercase S followed by a lower-case l with a square top and flat foot. A blank follows before the opening parenthesis. I read `(2, F₄)`, then an enclosing opening parenthesis, a second wave-over-rule sign, `GP(1, F₄)`, a third wave-over-rule sign, and `SO(3, F₄))`. The last two closing parentheses are both visible. There is no terminal period on this row.

All three field Fs have two right arms. In the Sl argument the outer left stroke is lighter and narrowly upright, with an irregular thickening at its upper join. The GP argument has a small pointed/thickened upper-left join and a slightly slanted outer edge. The SO argument has a more closed left rectangle with an uneven lower-left corner. Each base F and lowered 4 remains typed. Both G/P and S/O are full-height plain capitals, and O has no slash. The three first arguments are 2, 1, 3 in that order; the digits were read individually.

### Second displayed row

The initial handwritten capital has a high turning top, broad left bow and folded inner/lower S return. I read fraktur S securely from its own strokes. The low 5 remains typed. The following sign has one wave and one straight rule, followed by `GP (1, F₅)`. An enclosing parenthesis starts the last member: wave-over-rule sign, `SO(3, F₅))`. Two closing parentheses and the spaced terminal period are visible. The last mark is a compact dark point.

The two Fs have the same regular typed arms as the earlier fields. Their outer left strokes have different upper and lower joins: the first has a pale irregular left edge and a dark bottom join; the second has an oblique upper-left connection and rounded lower-left bend. Each lowered 5 has a flat top and rounded bottom. Both group-name strings use ordinary typed capitals.

### Lower half and archive numeral

`_b` contains no additional prose or formula. The lower-left handwritten archive numeral reads 31: the 3 has two curving lobes and the 1 is a long rising/descending stem with its entry stroke. It is transcribed as `% archive sheet number: 31`; the H `\page{31}` wrapper is excluded from textual differences under the supplied convention. The rest of the lower half was inspected for notes, marks, insertions and cancellations as recorded in the inventory section.

## Complete differences and C-doubt disposition

The structured loci B032-01 through B032-11 contain exact source strings, evidence, confidence, crop files and boxes.

| Locus | C | H | Recommended reading and state |
|---|---|---|---|
| B032-01, after `deux` | No point | No point | Optional faint point, `\unsure{.|}`, low confidence; textual status remains open. |
| B032-02, prose F₄ | Extra left stroke marked handwritten | Whole mathbb glyph without hand state | Retain C's mixed typed/handwritten boundary. |
| B032-03, prose F₅ | Extra left stroke marked handwritten | Whole mathbb glyph without hand state | Retain C's mixed typed/handwritten boundary. |
| B032-04, prose dash | Short `-` | `--` | Single short typed dash. |
| B032-05, first capital | Handwritten frak A / cal A doubt | Unqualified frak A | Retain C's doubt and its handwritten scope; typed 5 remains outside. |
| B032-06, Sl field | Extra left stroke marked handwritten | Whole mathbb glyph without hand state | Retain C; typed F core and 4. |
| B032-07, first GP field | Extra left stroke marked handwritten | Whole mathbb glyph without hand state | Retain C; typed F core and 4. |
| B032-08, first SO field | Extra left stroke marked handwritten | Whole mathbb glyph without hand state | Retain C; typed F core and 4. |
| B032-09, second capital | Handwritten frak S | Frak S without hand state | Retain C; typed 5 outside hand scope. |
| B032-10, second GP field | Extra left stroke marked handwritten | Whole mathbb glyph without hand state | Retain C; typed F core and 5. |
| B032-11, second SO field | Extra left stroke marked handwritten | Whole mathbb glyph without hand state | Retain C; typed F core and 5. |

The only explicit uncertainty macro in C concerns the first capital. It is retained, with `diff_C: false`, `diff_H: true`, `H_marked: false`, and `unresolved: true`. The added local point doubt is marked against both witnesses. H has no uncertainty macro or explicit uncertainty statement at these loci. No H passage is absent; H supplies the whole paragraph and both formulas.

The handwriting-state differences are substantive state boundaries, even though `\handwritten` renders as identity under the supplied preamble. All seven F glyphs preserve the typed core through C's `\handwritten{\mathbb}{F}` arrangement. Page-wrapper, align-environment and quotation syntax differences are excluded where they preserve the same reading and state. No other character, spelling, punctuation, deletion, insertion, alphabet, index or parenthesis change is proposed.

## Remaining doubts, notation and mathematical record

Two doubts remain: the alphabet of the first handwritten A, at medium confidence, and the textual status of the pale mark after `deux`, at low confidence. The seven F identities, seven associated indices, group-name letter cases, five comparison signs, commas, terminal punctuation and parentheses have high reading confidence. The assignment of each additional F left stroke to handwriting has medium confidence because the ink densities vary, while each typed core stays visually regular.

Proposed notation additions are local records: retain first A as frak/cal; record seven composite F constructions with typed cores and handwritten outer strokes; record the optional pale point after `deux` without propagating it into a general notation rule. `Sl`, `GP`, `SO` are the observed undotted group-name strings. No prose abbreviation needs expansion, and no expansion has been inserted.

No mathematical proof or numerical calculation was performed. Reading the two displayed assertions and inspecting their signs, indices and parse did not verify those assertions. Accordingly `check_events` is empty. No conditional theorem, hypothesized correction or mathematical reconstruction is proposed.

Static verification was performed only on the return files: braces balance; one unescaped display opener and closer; four inline dollar delimiters; aligned environment begin/end match; all eleven review loci carry every required field. Backslash parity was used for display delimiters. No TeX compiler was invoked.

## Workflow feedback

A prose punctuation issue emerged while preparing the detailed record after an early message had described the prose as settled. It was isolated in one new tight crop, without reopening any source image or recropping any locus. Improvement: complete the punctuation-by-punctuation record before sending a blanket settled-prose status. No other workflow problem occurred.
