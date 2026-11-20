# H162-01_162-1_scan004 — text-only comparison audit

Status: complete, including the root-authorized final preview/spec audit. No material text-level blocker remains. This file makes no ink decision.

## Scope and method

The initial reader-union audit read only this page's `C.tex`, `H.tex`, `C_questions.md`, and the three readers' `reading.tex` / `report.json` files. At root's later explicit request, the current-page `preview.tex` and `spec.json` were read for the focused final check; root crop filenames were listed only to reference the newly authorized metadata. No image, OCR, web source, other page, or other root decision content was used. Statements about shapes below describe the readers' encoded text and their own reports, not an independent observation of the manuscript. R1's 53 difference IDs are the comparison backbone. A missing R1 scope is identified explicitly instead of being silently folded into a neighboring row.

For the lexical comparison, coordinate wrappers, font sizes, `\resizebox`, node fragmentation, and mathematically equivalent brace formatting were ignored. `\unsure` scope, candidate order, capitalization, punctuation, and deletion state were retained. A candidate order change is distinguished from a different candidate set. Graphics are compared by explicit commands and local uncertainty wrappers. Counts exclude whatever the supplied `\deleted` macro itself draws, because its definition is outside the authorized text-only sources.

## Findings requiring root attention

1. R1 has lexical and punctuation scopes that must be broadened if a different reader is adopted: R3's doubtful `Lecture`, initial `V/v`, `abéliennes`, Weil separator, and accent alternatives in `arithmétiques`; R2/R3's definite `thy`; R2's definite `Harder,`; and R3's coupled alternatives `Harder,` / `Hardy`.
2. All three texts have a period after `Mumford`, while H gives a comma. R1 has no dedicated Mumford-separator row. All three omit H's colon between `Borel` and `Lecture Notes`; R1 D21 covers only the title words and D22 is geometry-only. All three also omit H's comma after `Koszul`; R2-D20 and final R3-D58 report that gap, while original R1 has no row.
3. R2 alone adds an uncertain oblique trace at Borel. R3 alone adds two explicit tracks over the Deligne adjacent mark, three terminal Serre tracks, and a short spur attached to the lower-left point. These are genuine presence differences between saved texts.
4. Parenthetical cancellation differs in both encoding and uncertainty: R1 has a sweep plus a continuous looping path without a local graphic `\unsure`; R2 has six oblique paths plus a bent terminal path inside `\unsure`; R3 has four oblique paths and a sweep, without a local graphic `\unsure`. R1 alone adds `questions` as a lexical candidate in that parenthesis.
5. R1's saved text and inventory contain a separate long cancellation through the Lettre entry, but D37–D40 do not report that geometry: D40 is the low wavy underline only. D51 starts at Weil. The short Qui/Que strike is also explicitly drawn although D41 scopes only the omitted cancelled text.
6. R3 places the full stops after the Serre and Weil entries outside `\deleted`; R1 and R2 place both inside their deleted text. This is a deletion-boundary difference, even though every reader has the periods.
7. All 407 nonempty C/H fields across the final three reader reports pass exact packet-substring tests. The final root spec also passes its literal-field check; the detailed counts and focused final audit appear below.

## Exact lexical and punctuation variance

The snippets below are exact local LaTeX from the saved readings, excluding only the layout wrappers stated above. An adjacent stable word may be retained to clarify scope. Every differing lexical/uncertainty/punctuation locus in the three complete texts is listed.

| Locus / R1 anchor | R1 | R2 | R3 | Nature of difference |
|---|---|---|---|---|
| Theta title word — D01 | `\unsure{fonction\|function}` | `f\unsure{o\|u}nction` | `\unsure{function\|fonction}` | Same two complete words. R1/R2 prefer the o form, R3 the u form. R2 confines doubt to one vowel. |
| Artin — D03 | `\unsure{Artin}-Winters` | `\unsure{Artin}-Winters` | `Ar\unsure{ti}n-Winters` | Same spelling; R3 narrows doubt to `ti`, whereas R1/R2 mark the whole first name. |
| First Monsky-Washnitzer — D04 | `\unsure{Monsky-Washnitzer}` | `\unsure{Monsky-Washnitzer}` | `Monsky-Washni\unsure{tz}er` | Same spelling; R3 narrows doubt to `tz`. Second occurrence is definite and identical in all three. |
| Hartshorne letters — D07 | `\unsure{lettres\|lettre} Hartshorne` | `lettres` / `Hartshorne` | `lettres` / `Hartshorne` | R1 retains singular as an alternative; R2/R3 resolve plural. All have lowercase initial l. |
| Quillen letters — D10 | `\unsure{Lettre\|Lettres} Quillen` | `Lettres` / `Quillen` | `Lettres` / `Quillen` | R1 prefers singular and retains plural; R2/R3 resolve plural. |
| Extensions adjective — D11 | `\unsure{infinitésimales}` | `infinitésimales` | `\unsure{infinitésimales}` | R2 removes the doubt retained by R1/R3. |
| Cancelled Notes noun — D12 | `\unsure{tapis\|topis}` | `t\unsure{a\|o}pis` | `t\unsure{a\|o}pis` | Same two candidates/order; R2/R3 localize uncertainty to the first vowel. All remove C's `topos` candidate. |
| Cancelled Notes parenthesis — D13 | `(\unsure{pluriel\|Gabriel}) Quillen` | `(pluriel)` / `Quillen` | `(\unsure{pluriel}) Quillen` | R1 keeps two candidates; R2 resolves `pluriel`; R3 keeps one tentative candidate. All place Quillen after the closing parenthesis. |
| Bourbaki opening — D15 | `R.\ \unsure{Wood} Bourbaki calcul différentiel` | `R. Wood` / `Bourbaki` / `calcul différentiel` | `R. W\unsure{oo}d Bourbaki calcul différentiel` | Same words; R2 has no lexical doubt, R3 confines doubt to `oo`. All omit H's `à` and comma after Bourbaki. |
| Borel title — D21 | `\deleted{Lecture Notes}` | `\deleted{Lecture Notes}` | `\deleted{\unsure{Lecture} Notes}` | R3 alone introduces a lexical doubt on `Lecture`. |
| Parenthesis below Deligne — D25 | `\deleted{(\unsure{questions\|suite\|suiten})}` | `\deleted{(\unsure{suite\|suiten})}` | `\deleted{(\unsure{suite\|suiten})}` | `questions` is unique to R1 and is its first candidate. All mark the entire parenthesis deleted. |
| Separator after Serre — D28 | `\unsure{.\|:}` | `\unsure{:\|.}` | `\unsure{.\|:}` | Same candidate set; R2 reverses preferred order. |
| Serre abbreviation — D29 | `\unsure{Ch.\|Coh.}` | `Ch.` | `\unsure{Ch.\|Coh.}` | R2 resolves `Ch.`; R1/R3 retain `Coh.` as alternative. |
| Vect. initial — D30 | `Vect.` | `Vect.` | `\unsure{V\|v}ect.` | R3 alone introduces case doubt. R1 D30 explicitly asserts a capital V. |
| Serre adjective — D31 | `abéliennes` | `abéliennes` | `\unsure{abéliennes}` | R3 alone adds a whole-word doubt. R1 D31 calls the reading high confidence. |
| English abbreviation — D39 | `th\unsure{y\|.}` | `thy` | `thy` | R2/R3 resolve the final y. R1 keeps `th.` as an alternative. |
| Short cancelled start — D41 | `\unsure{Qui\|Que}` | `\unsure{Que\|Qui}` | `\unsure{Qui\|Que}` | Same candidate set; R2 reverses preference. |
| Separator after Weil — D42 | `Weil :` | `Weil :` | `Weil` / `\unsure{.\|:}` | R3 alone doubts the colon and prefers a period. |
| Lichtenbaum adjective — D48 | `\unsure{arithmétiques}` | `\unsure{arithmétiques}` | `arithm\unsure{è\|é\|e}tiques` | R3 narrows the uncertainty to the vowel/accent but adds grave and unaccented candidates, with grave preferred. |
| Final surname and separator — D49/D50 | `\unsure{Harder\|Hardy}\unsure{,}` | `Harder,` | `Hard\unsure{er,\|y}` | R1 has surname alternatives plus an independently doubtful comma; R2 resolves `Harder,`; R3 couples comma to `Harder`, while `Hardy` has no added comma. |
| Serre terminal period — D32/D34 | Inside `\deleted{...$p\unsure{\ne\|>}0$.}` | Inside `\deleted{$p\unsure{\ne\|>}0$.}` | Separate live node `{.}` at `(1598,1110)` | Same punctuation character, different deletion boundary. |
| Weil terminal period — D43/D51 | Inside `\deleted{Weil : Jacobiennes \unsure{intermédiaires}.}` | Inside `\deleted{\unsure{intermédiaires}.}` | Separate live node `{.}` at `(1292,1258)` | Same punctuation character, different deletion boundary. |

Apart from these loci, all three have the same lexical content and punctuation after layout normalization: the headings and their definite numerals; `Mumford .`, `Papiers Kiehl`; `Hartshorne : Affine duality`; the stable surrounding wording of the Notes and Bourbaki rows; `Complexe cot` with the same low star/plus candidates; capital `L'extension`; definite `pour`; `Koszul 2 articles`; definite `Borel`; the same Deligne `1/2/?` candidates; definite second `Monsky-Washnitzer`; `var.`, `en car`, and the same `p` relation/zero; paired quotes and four points in the Griffiths title; the same uncertain `Rietzly/Rietzley` and `class`, definite `Chapin, field`; `Jacobiennes` and uncertain `intermédiaires`; `Papiers d'Artin (13)`; `Lichtenbaum, surfaces`; the full Manin entry and its `(2 articles)`; and `sur conjecture de Weil`. Every reader preserves archive `3` only as a comment.

## Graphics, uncertainty, count, and placement

Coordinates are quoted from the saved code in the common source-coordinate system. They do not constitute an image measurement by this auditor. Ordinary small coordinate differences are shown where they matter to extent or attachment. Commands are explicit additional paths, excluding state-macro rendering.

| Locus / R1 anchor | R1 encoded form | R2 encoded form | R3 encoded form | Audit implication |
|---|---|---|---|---|
| Top enclosure — D02 | One open curved path, `(1085,47)` to `(1074,60)`, around top I. | One open curved path, `(1082,45)` to `(1069,58)`. | One open curved path, `(1083,48)` to `(1062,57)`. | Presence/count agree. All encode an enclosing path, not an insertion leader; differing shape needs only root's chosen schematic. |
| Ruled Roman numerals — D02/D05 | Overline and underline on both I and II, each occurrence. | Same. | Same, with lower pair split across nodes. | Four numerals, each with two rules; comma between each pair. No presence difference. |
| Hartshorne slash — D06 | One straight path `(452,606)` to `(507,553)`. | `(455,608)` to `(506,553)`. | `(453,608)` to `(505,555)`. | Count/placement agree; all left of letter entry and extend toward next row. |
| Quillen slash — D09 | One curved path `(457,730)` to `(511,680)`. | One straight path `(454,733)` to `(511,680)`. | One straight path `(455,731)` to `(510,679)`. | Shape differs: R1 curved, others straight. |
| Notes cancellation — D14 | One continuous path anchored to the whole deleted node. | One continuous path `(527,779)` to `(1211,772)`. | One continuous path `(530,782)` to `(1213,771)`. | Presence/count agree. R1's endpoint depends on actual typeset node width; R2/R3 give source-coordinate ends. |
| Atiyah tail — D19 | Two filled ellipses, then one curved dash plus filled endpoint: four primitives, three disconnected units. First point centered `(1334,946)`; terminal end `(1387,948)`. | Short dash `(1332,947)` to `(1338,948)`, one filled point, curved dash plus filled endpoint: four primitives, three units. | Short dash `(1332,945)` to `(1339,947)`, one filled point, curved dash ending `(1388,949)`: three primitives, three units. | First unit is point-like in R1 versus dash-like in R2/R3. R1/R2 separately thicken the last endpoint; R3 does not. No local graphic uncertainty in any text. |
| Borel/title cancellation — D22 | Two separated additional paths, one across Borel and one across title. | Two separated paths. | Two separated paths. | Presence/count and deliberate gap agree. No reader types a colon between Borel and title. |
| Extra Borel oblique — no R1 scope | Absent. | One separately drawn oblique trace inside `\unsure`, nested node at `(556,1030)`, local path `(-10,10)` to `(16,-12)`. | Absent. | Real presence/uncertainty difference. Its affiliation to lettering/cancellation is explicitly uncertain in R2. |
| Divider — D23 | Two paths, `(244,1072)` to `(713,1051)` and `(735,1048)` to `(1094,1031)`. | Two paths, `(244,1072)` to `(713,1050)` and `(735,1046)` to `(1094,1030)`. | Two paths, `(245,1072)` to `(710,1052)` and `(735,1048)` to `(1096,1031)`. | All agree on two disjoint segments and gap. |
| Deligne adjacent mark — D24 | Only textual `\unsure{1\|2\|?}` at `(408,1105)`. | Only textual candidates at `(406,1106)`. | Textual candidates at `(405,1106)` plus two unwrapped curved paths around `(404–424,1070–1107)`. | R3 adds two graphic tracks absent in R1/R2. Textual doubt does not automatically make these two added tracks locally doubtful. |
| Parenthetical mesh — D27 | Two additional draw commands: one sweep plus one continuous five-return looping path, without a local graphic `\unsure`. | Seven additional draw commands inside graphic `\unsure`: six straight obliques and one bent terminal path. | Five additional draw commands: four obliques plus one sweep, without local graphic `\unsure`. | Different count, geometry, and certainty. R1 report says decomposition into passes is uncertain, while only R2 carries an explicit graphic uncertainty wrapper. These are not merely font changes. |
| Serre low rules — D33 | `\uuline{Serre}`. | `\uuline{Serre}`. | `\uuline{Serre}`. | Two low rules in all texts. |
| Serre long cancellation — D34 | One long path anchored to whole Serre node. | One path `(531,1140)` to `(1593,1095)`. | One path `(533,1144)` to `(1593,1094)`. | Count agrees. R1 text-width-dependent endpoint differs structurally from source-coordinate paths. |
| Serre terminal mesh — no R1 standalone scope | Absent as separately drawn paths. | Absent as separately drawn paths. | Three unwrapped short paths: `(1541,1090)` to `(1559,1104)`, `(1547,1096)` to `(1549,1110)`, `(1553,1092)` to `(1556,1110)`. | Three-track presence difference. The unresolved relation is a separate lexical/symbol locus and does not itself encode this mesh. |
| Griffiths quote pair / four points — D35/D36 | Inline paired opening/closing quotes and literal `....` in a rotated whole node. | Quotes, title, four points, and closing quotes are separate nodes. | Same components as R2, independently placed. | Character/count agree. R2/R3 explicitly place the quote pairs high; R1 relies on typeset inline position/rotation. |
| Lettre long strike — missing R1 difference scope | One additional long path anchored to Lettre node. Inventory explicitly lists it. | One long path `(535,1227)` to `(1197,1185)`. | One long path `(530,1231)` to `(1196,1185)`. | Presence/count agree across texts but R1's report has no local difference row for this geometry. D40 covers only the separate low wave. |
| Lettre low wave — D40 | Starts `(670,1240)`, ends `(932,1226)`; comment says under both names. | Starts `(698,1244)`, ends `(930,1226)`; comment says starts within first name. | Starts `(702,1241)`, ends `(936,1224)`; comment says starts inside first name. | R2/R3 begin about 28–32 coordinate units farther right than R1. All one continuous wavy path below name region. C's macro underlines whole first-name-plus-Chapin span; partial-start adoption should be recorded as a placement change. |
| Qui/Que strike — D41 text scope | One straight additional path, anchored to deleted node. | One path `(532,1264)` to `(601,1254)`. | One path `(531,1262)` to `(596,1254)`. | Presence/count agree; R1 D41's reading field contains only deleted text, not path geometry. |
| Weil cancellation — D51 | One long anchored path. | One long path. | One long path. | Count agrees. R3's separate full stop is outside deletion macro. |
| Artin cancellation pair — D45 | Two anchored paths; second has width `.35pt`. | Two paths, both `.5pt`. | Two paths, `.55pt` and `.3pt`. | Two full-length paths agree; R1 D51's broad reading block repeats this already itemized pair. |
| Artin 13 underline — D44 | `\uuline{13}` within parentheses. | Same. | Same. | Two short low rules plus the two independent long cancellation paths. Do not merge the two kinds of line count. |
| Lichtenbaum/Manin/final cancellation — D51 | One per row, with opacity adjustments on first two. | One per row. | One per row; Lichtenbaum and Manin use `gray`. | Presence/count agree; color/opacity choices differ. R1 D51's literal C/H witness fields quote only the Weil row although its declared scope includes these other rows. |
| Far-right detached point — D52 | `\unsure` circle `.35pt` at `(1608,1155)`. | `\unsure` circle `.3pt` at `(1608,1156)`. | `\unsure` circle local radius `.65` with one-point units at `(1606,1157)`. | Same presence and uncertainty; size differs. |
| Lower-left detached point — D53 | `\unsure` ellipse `.55pt` by `.35pt`, `(246,1763)`. | `\unsure` circle `.45pt`, `(245,1763)`. | `\unsure` ellipse `.8` by `.65` with a connected left spur, `(246,1764)`. | R3 alone has spur. R2 is circular, R1/R3 elliptical; all mark ink/surface status uncertain. |

### Layout-only distinctions

R1 uses a bare grouped TikZ picture at `.0088cm` per source unit and `\footnotesize`, with several whole-line nodes and a few rotations. R2 wraps the picture in `\figure`, uses `.0075cm` units and an explicit 8.3/9.6 font, and splits most rows into word-level nodes. R3 wraps in `\figure`, uses `.009cm` units and `\small`, and applies many local `\resizebox` widths. These are not lexical differences, but they make anchored text-end paths non-equivalent to source-coordinate paths; render QA belongs to root. R1 and R2 finish with `\clearpage`; R3 does not.

## Report union, literal-field checks, and internal consistency

The complete mapping, literal checks, and report/inventory findings are given below. R3’s final late additions (D42 comma scope and D58 Koszul separator) are included.

## C question coverage

The packet has 32 table rows plus the recovered question-mark note. Two loci occur twice: the low cot mark (rows 4 and 17) and the Serre relation (rows 8 and 24). Thus R1's 30 `c_doubts` entries can cover the 32 table rows without a count discrepancy. The recovered note repeats the existing Deligne `1/2/?` locus rather than adding another written mark.

| C question row(s) | Local question | R1 difference scope / c_doubts item |
|---|---|---|
| 1 | Theta | Agreement; c_doubts 1 |
| 2 | Ruled I/II and Raynaud oval | D02, D05; c_doubts 2 |
| 3 | Both left slashes | D06, D09; c_doubts 3 |
| 4, 17 | Low star/plus after cot | D16; c_doubts 4 |
| 5 | Omega with raised 1 | Agreement; c_doubts 5 |
| 6 | Opening/closing quote pairs | D35; c_doubts 6 |
| 7 | Two rules under 13 | D44; c_doubts 7 |
| 8, 24 | Serre relation and zero | D32; c_doubts 8 |
| 9 | function/fonction | D01; c_doubts 9 |
| 10 | Artin | D03; c_doubts 10 |
| 11 | First Monsky-Washnitzer | D04; c_doubts 11 |
| 12 | lettres/lettre Hartshorne | D07; c_doubts 12 |
| 13 | Lettres/Lettre Quillen | D10; c_doubts 13 |
| 14 | infinitésimales | D11; c_doubts 14 |
| 15 | tapis/topis/topos | D12; c_doubts 15 |
| 16 | pluriel/Gabriel | D13; c_doubts 16 |
| 18 | pour/par | D18; c_doubts 17 |
| 19 | Atiyah tail marks | D19; c_doubts 18 |
| 20 | Borel | D20; c_doubts 19 |
| 21 plus recovered prose note | Deligne adjacent 1/2/? | D24; c_doubts 20 |
| 22 | suite/suiten | D25–D27; c_doubts 21 |
| 23 | Coh./Ch. | D29; c_doubts 22 |
| 25 | Four points / ellipsis | D36; c_doubts 23 |
| 26 | Rietzly/Rietzley | D37; c_doubts 24 |
| 27 | class | D39; c_doubts 25 |
| 28 | th + y/period | D39; c_doubts 26 |
| 29 | Qui/Que | D41; c_doubts 27 |
| 30 | intermédiaires | D43; c_doubts 28 |
| 31 | arithmétiques | D48; c_doubts 29 |
| 32 | Harder/Hardy; possible comma | D49–D50; c_doubts 30 |

## R1 report-to-text and report-to-inventory observations

- **No hard literal-field failure:** the 81 nonempty C and 48 nonempty H strings are literal packet substrings, including embedded newlines where required. Byte-for-byte equality between a reading and its witness field is not the test of a change flag: equivalent mathematical brace formatting, schematic coordinates, and neighboring independently scoped changes do not by themselves make a local lexical flag true.
- **Unreported common punctuation:** the period after Mumford and absence of Borel's H colon are present in the saved reading but not separately scoped in the 53 rows. D21 does not include the Borel separator, and D22 expressly concerns the two cancellation runs.
- **Unreported Lettre line geometry:** inventory item 34 says the long Lettre strike is transcribed, and the text contains it. D40 only reports the independent low wave. D51's place, witnesses, and evidence cover Weil and lower entries. A separate scope or an explicit extension is needed for the Lettre strike.
- **Short-start geometry:** the text has an additional straight line through Qui/Que; D41's reading field contains only the deletion wrapper and words. Its omission claim covers the absent H text, but it does not explicitly account for geometry newly drawn beyond C's generic deletion wrapper.
- **Overlapping H lexical fields:** D38's local subject is `Chapin`, but its H field is `chapitre de` plus newline plus `familles`; D39 separately uses `de` plus newline plus `familles`. Both are literal and their local `marked_in_H=false` flags are defensible, but the witness scopes overlap. D38 can be narrowed to the literal H substring `chapitre` if disjoint local comparisons are required.
- **Broad D51 with narrow witness fields:** its reading block contains Weil, Artin, Lichtenbaum, Manin, and final-row cancellations, while its C/H witness fields contain only the Weil row. The Artin pair already has D45. This is not a substring failure; it is a scope/duplication issue. Separate row-level geometry scopes are clearer, particularly when mapping other readers' rows.
- **Parenthesis graphic certainty:** D27's evidence says decomposition into pen passes is uncertain, while the saved drawing is not locally wrapped in `\unsure`; the word itself is doubtful. The report also calls the paths schematic. Root should distinguish uncertainty about exact tracing from uncertainty about the existence of the cancellation rather than transfer the word's doubt automatically to all neighboring strokes.
- **Pooled detached-point doubt:** one `remaining_doubts` entry is called “Two isolated points” but reproduces only the far-right circle form, not the lower-left ellipse. D52/D53 and the inventory do keep the two positions separate; the pooled remaining-doubt row is abbreviated rather than a complete encoding of both local readings.
- **Inventory shorthand loses some uncertainty:** the Lettre entry's `first_words_or_objects` ends in `thy` although the text and D39 retain `th.` as an alternative; the final entry's inventory shows a comma after `Harder/Hardy` without the text's independent comma doubt. These summaries should not be treated as a more certain adjudication than the reading/report rows.
- **Local H markers are correctly separated in R1:** the first-name `\ill` does not mark `Chapin` or `class field ...`; the Lichtenbaum `\ill` covers `surfaces`, not the following definite H `arithmétiques`; the post-Jacobiennes `\ill` covers the adjective, not the separate earlier Qui/Que entry; the final surname's undivided unread span can include its ambiguous separator. Graphic D40 remains unmarked even though its contextual H field contains the first-name `\ill`.

## Complete report-difference union mapped to R1 IDs
R1 has 53 difference rows, R2 has 58, and final R3 has 58. All 116 R2/R3 rows are mapped below or in the uncovered-scope table; a programmatic ID-set check found no unmapped row. `R3-Dnn` below denotes R3’s raw JSON ID `Dnn`. Multiple references for a row indicate split or overlapping local scopes, not extra independent observations.
| R1 ID | R1 scope | R2 rows | R3 rows | Scope/variance note |
|---|---|---|---|---|
| D01 | Raynaud title, word following Theta | R2-D02 | R3-D01 | Candidate order and doubt granularity differ; see exact table. |
| D02 | Raynaud title, circled I and following II | R2-D03 | R3-D03 | Open-contour versus symbolic-circle treatment gives inconsistent C-change flags across reports. |
| D03 | Raynaud third item, Artin | R2-D04 | R3-D04 | R3 narrows doubt to ti. |
| D04 | Illusie first item, surname pair | R2-D05 | R3-D05 | R3 narrows doubt to tz. |
| D05 | Illusie first item, ruled Roman numerals | R2-D06 | R3-D06 | Equivalent ruled numerals; graphic/omission kind labels differ only. |
| D06 | Illusie, slash before Hartshorne letters | R2-D08 | R3-D08 | R2 reports source-position change from baseline slash; R1/R3 retain C flag false. |
| D07 | Illusie, letters to Hartshorne | R2-D07 | R3-D07 | R2/R3 resolve lowercase plural. |
| D08 | Illusie, Hartshorne title separator | — | R3-D09 | Absent from R2 differences although R2 text/inventory give the colon. |
| D09 | Illusie, slash before Quillen letters | R2-D10 | R3-D11 | R2 reports source-position change; R1 uses a curve, others a straight path. |
| D10 | Illusie, Lettre(s) Quillen | R2-D09 | R3-D10 | R1 prefers singular; R2/R3 resolve plural. |
| D11 | Illusie, extensions adjective | R2-D11 | R3-D12 | R2 resolves; R1/R3 retain doubt. |
| D12 | Cancelled Notes entry, tapis/topis | R2-D12 | R3-D13 | Same remaining candidates; R2/R3 localize vowel doubt. |
| D13 | Cancelled Notes entry, parenthesis and following Quillen | R2-D13 | R3-D14 | R1 two doubtful words; R2 definite pluriel; R3 tentative pluriel. |
| D14 | Cancelled Notes entry, long strike geometry | R2-D14 | — | No R3 difference row; R3 text/inventory 17 contain the path. |
| D15 | Bourbaki line, opening words and separators | R2-D15 | R3-D15 | Same lexical opening with different Wood certainty; all remove H à and comma. |
| D16 | Complexe entry, cot and low mark | R2-D16 | R3-D16 | Same abbreviated cot and unresolved low sign. |
| D17 | Atiyah entry, initial L of extension | R2-D17 | R3-D17 | Capital L agreed. |
| D18 | Atiyah entry, pour/par | R2-D18 | R3-D18 | All resolve pour. |
| D19 | Atiyah entry, tail after Omega-one | R2-D19 | R3-D19 | First shape and terminal endpoint encoding differ; three disconnected units in all. |
| D20 | Cancelled Borel name | R2-D21 | R3-D20 | All resolve Borel. |
| D21 | Cancelled Borel title | R2-D22 | R3-D21 | R2 also covers Borel colon (U03); R3 doubts Lecture. |
| D22 | Borel and Lecture Notes, separated cancellation runs | R2-D23 | R3-D22 | R2 includes extra lower oblique (U04). |
| D23 | Thin divider between Illusie and Deligne | R2-D24 | R3-D23 | Two divider segments in all. |
| D24 | Deligne label, adjacent heavy mark | R2-D25 | R3-D24 | R3 extends scope to two overlapping graphic tracks (U06). |
| D25 | Small parenthetical below Deligne, wording | R2-D26 | R3-D25 | R2/R3 word alternatives are embedded in their deletion-state rows; only R1 adds questions. |
| D26 | Small parenthetical below Deligne, cancellation state | R2-D26 | R3-D25 | Deleted parenthesis against H live form; explicit in all. |
| D27 | Small parenthetical below Deligne, meshed cancellation | R2-D27 | R3-D26 | R1 looped path; R2 six hatches plus return, locally unsure; R3 four hatches plus sweep. |
| D28 | Serre entry, separator after name | R2-D29 | R3-D28 | Same colon/period alternatives with R2 preference reversed. |
| D29 | Serre entry, first abbreviation | R2-D30 | R3-D29 | R2 resolves Ch.; R3 H field also covers des, which R1 places in D30. |
| D30 | Serre entry, Vect. Witt | R2-D31 | R3-D29, R3-D30 | R3 introduces V/v doubt; R3-D29 accounts for H des and D30 for vecteurs de. |
| D31 | Serre entry, var. abéliennes | R2-D32 | R3-D31 | R3 introduces abéliennes doubt. |
| D32 | Serre entry, car and p condition | R2-D33, R2-D34 | R3-D32, R3-D33, R3-D35 | R2/R3 split abbreviation from relation. R3-D35 adds live terminal-period decision (U08). |
| D33 | Serre name, two low rules | R2-D28 | R3-D27 | Two underlines agreed. |
| D34 | Serre entry, long sloping cancellation | R2-D35 | R3-D35 | R3 has no report row for the long Serre path; D35 only covers point deletion state. See U08. |
| D35 | Griffiths title, quotation marks | R2-D36 | R3-D36, R3-D37, R3-D39 | R3 splits opening and closing pairs, then adds positional scope U09. |
| D36 | Griffiths title, four trailing marks | R2-D37 | R3-D38 | All resolve four points. |
| D37 | Cancelled Lettre entry, first name | R2-D39 | R3-D41 | Same first-name candidates; H unread marker local to this name. |
| D38 | Cancelled Lettre entry, Chapin | R2-D40 | R3-D42 | R2/R3 narrow H to chapitre. Final R3-D42 explicitly includes following comma. |
| D39 | Cancelled Lettre entry, class field thy | R2-D41 | R3-D43, R3-D44 | R2 resolves thy; R3 splits class field and thy but reuses undivided H de familles. |
| D40 | Cancelled Lettre entry, low wavy rule | R2-D42 | R3-D45 | R2/R3 explicitly begin wave inside first name and set C-change true. |
| D41 | Short cancelled start before Weil | R2-D44 | R3-D46 | R2 reverses candidate order. None separately reports the short additional strike geometry. |
| D42 | Weil entry, name and title separator | R2-D45 | R3-D47, R3-D48 | R3 splits surname from separator and adds period/colon doubt. |
| D43 | Weil entry, final adjective | R2-D46, R2-D47 | R3-D49, R3-D50 | R2 separates adjective and tail-deletion state. R3 separates adjective and final live point (U10). |
| D44 | Papiers d Artin, double underline beneath 13 | R2-D49 | R3-D51 | Two underlines agreed. |
| D45 | Papiers d Artin, two cancellation lines | R2-D50 | R3-D52 | Two long cancellations agreed. |
| D46 | Lichtenbaum entry, name | R2-D51 | R3-D53 | Lichtenbaum agreed. |
| D47 | Lichtenbaum entry, surfaces | R2-D52 | R3-D54 | surfaces agreed; H unread marker applies here. |
| D48 | Lichtenbaum entry, arithmétiques doubt | R2-D53 | R3-D55 | R3 localizes to è/é/e with grave preferred. |
| D49 | Final entry, surname | R2-D56 | R3-D56 | R2 resolves Harder; R3 has coupled ending alternatives. |
| D50 | Final entry, possible comma after surname | R2-D56 | R3-D56 | R2/R3 combine comma with surname choice; R1 isolates doubtful comma. |
| D51 | Lower block, long cancellation paths not otherwise itemized | R2-D48, R2-D54, R2-D55, R2-D57 | — | R2 has separate Weil/Lichtenbaum/Manin/Harder geometry rows. R3 encodes/inventories those paths but reports none of them as difference rows. Artin repetition in R1 D51 is already D45. |
| D52 | Detached point at far right beside Griffiths level | R2-D38 | R3-D40 | All preserve doubtful detached right point. |
| D53 | Detached point below list, left side | R2-D58 | R3-D57 | R3 adds connected left spur; R1 ellipse vs R2 circle. |

### Scopes not fully represented by the original R1 row definitions
| Audit scope | Report origin | Relationship to R1 | Local handling |
|---|---|---|---|
| U01: Period after Mumford | R2-D01; R3-D02 | Near D01, but a separate punctuation scope is absent in R1. | All three texts agree on a period; C agrees, H has comma. Local C-change false, H-change true, H-marked false. |
| U02: Gap after Koszul | R2-D20; R3-D58 | No R1 difference scope. | All three texts/C have a gap; H has comma. Local C-change false, H-change true, H-marked false. |
| U03: No colon between Borel and title | R2-D22 | Extend D21 explicitly or add a local separator row; D22 is geometry-only. | R2 reports the absent H colon directly. R1/R3 text also omit it, but their title-word rows omit this separator scope. C-change false for the separator alone. |
| U04: Extra uncertain Borel oblique trace | R2-D23 | Extend D22 explicitly or separate the uncertain trace. | Absent from R1/R3 text/inventory. If adopted, C/H change true and H-marked false for the graphic; preserve local uncertainty. |
| U05: Long Lettre cancellation | R2-D43 | No R1 difference scope. D40 is the separate low wave; D51 begins at Weil. | All three texts/inventories have the line. R2 supplies the missing C/H geometry comparison with both changed and H-marked false. |
| U06: Two Deligne overlaid tracks | R3-D24 | Extend D24 beyond the unchanged textual candidates. | R3 alone draws two explicit tracks. If adopted as added geometry, C-change true even though numeral candidates are unchanged. |
| U07: Three Serre terminal-mesh tracks | R3-D34 | New local graphic scope adjacent to D32/D34. | R3 alone draws these three paths. Do not treat symbol uncertainty as automatically deciding presence, count, or assignment of the paths. |
| U08: Serre final period outside deletion | R3-D35 | Explicitly extend/split D32 or D34; R1 has the period but keeps it deleted. | A real state alternative, not an omitted character. If choosing R3’s live period, C-change true; H omits the point and has no local unread marker. |
| U09: Griffiths title/closing-quote placement | R3-D39 | Extend D35 with placement or add a separate row; R1 D35 concerns quotation shape only. | R3 explicitly reports the rising line and high closing pair. R2 text/inventory also place them separately, without a difference row for that placement. |
| U10: Weil final period outside deletion | R3-D50 | Explicitly extend/split D43; R1 keeps the period in the deleted adjective span. | The H unread tail may cover the point, so H-marked true is local and definite omission from H should not be claimed. Choosing a live point changes C state. |

**Additional text/inventory-only scope:** the short Qui/Que cancellation path is encoded in all three texts and appears separately in R2 inventory 39 / R3 inventory 46, but no reader has a distinct geometry difference row for it. R1 D41, R2-D44 and R3-D46 report the absent/uncertain cancelled text. This is outside the report-difference union. Root explicitly adjudicated that this simple local line is covered by D41’s deleted-state scope, so no separate geometry row is required in the final apparatus.

## Final literal C/H field validation
Every nonempty string under a `C` or `H` key anywhere in each report was tested directly with Python substring membership against that page’s corresponding packet, without whitespace normalization or removal of macros. Empty strings were excluded as absent-witness spans.
| Reader | Difference rows | Nonempty C fields | Nonempty H fields | Invalid fields |
|---|---:|---:|---:|---:|
| R1 | 53 | 81 | 48 | 0 |
| R2 | 58 | 86 | 51 | 0 |
| R3 | 58 | 90 | 51 | 0 |

The finalized R3-D42 C field is the literal substring `Chapin},`, preserving C’s closing wave-wrapper brace before the comma. It is valid; it must not be normalized to a fabricated C substring `Chapin,`. R3-D58 is the late-added Koszul separator row.

### Source snapshot digests

These digests identify the files used in this completed report-union audit. A later reader revision requires only an adaptive recheck of changed files.

| Reader | File | SHA-256 |
|---|---|---|
| R1 | reading.tex | `3b76fbd051d311b9f50fc2bfeb91b936a9dedfaeee08148517594902376ce8e6` |
| R1 | report.json | `d4a2ba85e5080df142d30e63f527a541b75af751958a1a73a726ca5e23578381` |
| R2 | reading.tex | `34420544ef79daa5ef92b751c60e5c96f504097b22d5d9c65d61d80a08fb9eec` |
| R2 | report.json | `040e1481362d2e866c24f0a218cb0caf1a7cb0339d4a068ec143aa8685089e7e` |
| R3 | reading.tex | `e6593b8c15419869c84c6ac31fa70ef325e5f49bf346baa3db65412c3b99b294` |
| R3 | report.json | `deb71e9e83ce541c993337bcb529c376fa77898f4be90438258c6af58df52c19` |


## R2 and R3 text/report/inventory consistency

### R2

R2's 18 explicit `\unsure` occurrences correspond to its 18 remaining-doubt entries, including the Borel oblique, parenthetical hatching, and two detached points. Its 52 inventory rows all have `transcribed: yes`, and the extra Borel trace and six hatch diagonals plus terminal return are present in its saved text. No hard lexical contradiction between R2's text, decisions, and remaining-doubt list was found. Inventory names use descriptive shorthand, so they should not supersede the reading's uncertainty wrappers.

Two report-coverage gaps remain in raw R2 but are filled by the union: it has no Hartshorne-title colon-versus-comma row although its text and inventory item 10 give the colon (R1 D08 / R3-D09 cover it), and it independently positions the Griffiths quotes at the heights described in inventory item 33 without a placement difference row (R3-D39 supplies that scope). Its distinct Lettre strike is correctly and separately reported by R2-D43. Its short Qui/Que strike is inventoried separately but is accepted under root's D41 deletion-state scope.

R2's C-change flags for the enclosure and both diagonals deliberately count their newly explicit shape/position, unlike original R1's narrower equivalence convention. Root's final spec adopts that explicit graphic convention for D02, D06 and D09. R2's partial-start wave likewise sets C-change true and is adopted in final D40. These are cross-reader scope conventions, not literal-field failures.

### R3

Final R3 contains 58 difference rows. Its late D58 covers the Koszul comma; its revised D42 explicitly includes the comma after Chapin and uses the valid literal C fragment `Chapin},`. All 90 nonempty C and 51 nonempty H fields pass. Its 25 explicit uncertainty wrappers correspond to 25 remaining-doubt entries, and all 60 inventory rows are marked transcribed. Its four parenthetical hatches, three terminal mesh tracks, two Deligne overlay tracks, live terminal periods, and lower-point spur agree with its saved text and inventory descriptions.

Raw R3 draws and inventories several long cancellation paths without individual difference rows: Notes (inventory 17), Serre (36), Lettre (43), Weil (48), Lichtenbaum (54), Manin (56), and the last entry (58). Their omission from its apparatus does not mean they are absent from its text. R1/R2 supply these union scopes, and root's final spec reports them individually. R3 also omits a local Borel-colon comparison, which R2-D22 supplies and final D21 now includes.

R3's `c_doubts` entry 23 is labeled a suite/suiten word doubt but has high confidence inherited from the deletion-state decision, whereas its remaining-doubt entry 11 gives the word low confidence. The distinction should be local: deletion is secure, wording remains doubtful. Root's selected metadata uses low confidence for the wording and treats state separately. R3's terminal-mesh doubt concerns assignment of tracks to sign/cancellation; the three paths themselves are unwrapped. This is consistent with inventory 37's “allocation uncertain” wording, and root preserves that distinction rather than applying the relation's doubt to track presence automatically.

R3 inventory shorthand omits some accents or wrappers (for example `infinitesimales` and `arithmetiques`), while its actual text and remaining doubts preserve the intended accented candidates. Root's reconciled inventory now carries the chosen local readings. Raw R3 lacks a final `\clearpage`; the root preview restores it.

## Final root preview/spec audit

The focused check used the regenerated files `H162-01_162-1_scan004_preview.tex` and `H162-01_162-1_scan004_spec.json`. Root supplied the ink choices; this check only tested their faithful expression and apparatus consistency.

| Check | Result |
|---|---|
| Consolidated scopes | 61: 52 retained R1 IDs (D50 merged into D49) plus ROOT-D54 through ROOT-D62 |
| Reader-union coverage | All 169 raw reader rows accounted for; no uncovered material scope remains |
| C-change count | 41 |
| H-change count | 59 |
| Distinct C-question decisions | 30, covering all 32 table rows plus the repeated recovered note |
| Inventory | 61 entries, all `transcribed: yes` |
| Remaining doubts | 26 entries matching 26 local uncertainty spans |
| Lexical/symbol uncertainty spans | 22, including both separately placed period/colon doubts |
| Graphic uncertainty spans | 4: Borel lower trace, parenthetical mesh, far-right point, lower-left point/spur |
| Literal witness fields | No nonempty C/H field fails exact packet-substring membership |
| Graphic excerpt consistency | Every final field containing node/draw/fill code is an exact preview substring |
| Stale R1 anchors | None (`.base west` / `.base east` references removed) |
| Spec replacement text | Exactly equals the saved preview |

### Final destinations of the union extensions

| Earlier audit scope | Final consolidated scope |
|---|---|
| U01: Mumford period | ROOT-D54 |
| U02: Koszul gap | ROOT-D55 |
| U03: Borel gap instead of colon | D21, explicitly broadened |
| U04: uncertain short Borel trace | D22, explicitly broadened |
| U05: separate long Lettre strike | ROOT-D56 |
| U06: two Deligne overlay tracks | D24, explicitly broadened |
| U07: three Serre terminal tracks | ROOT-D59 |
| U08: live Serre final period | ROOT-D57 |
| U09: rising Griffiths title and raised closing quotes | D35, explicitly broadened |
| U10: live Weil final period | ROOT-D58 |
| Original broad D51 lower-row geometry | D51 now only Weil; ROOT-D60 Lichtenbaum, ROOT-D61 Manin, ROOT-D62 final entry |
| Original D50 independent comma doubt | Merged into the coupled surname/tail alternatives of D49 |
| Short Qui/Que local strike | Covered by D41's deletion-state scope, as explicitly directed by root |

### Local H-marker scope

The only six final scopes marked locally unread in H are D19 (Atiyah tail), D37 (first Lettre name), D43 (Weil adjective), D47 (surfaces), D49 (final surname/tail), and ROOT-D58 (Weil final point within the undivided unread tail). The geometric scopes whose contextual H fields contain `\ill` correctly remain unmarked: the name wave, long Lettre cancellation, Weil path, Lichtenbaum path, and last-entry path. H's unread marker before `arithmétiques` does not mark the adjective itself uncertain. The separate short Qui/Que entry is not covered by a neighboring unread span.

### Adaptive fixes confirmed

The first preview exposed two reading-field presentation issues and a nested-position ambiguity. The regenerated spec fixes D21 to the literal reading `Lecture Notes`, keeping the blank-gap explanation in evidence; D24 now includes the full actual mark node before its two paths; and the shortened Borel trace uses an explicit base-west anchor at `(549,1042)` with a local baseline and path `(0,0)` to `(12,-9)`. The parenthetical graphic now has an explicit invisible bounding box fixing the intended northwest source origin. The final geometry excerpts match the preview after those changes.

All selected reader variants are represented: root's localized o/u, whole Artin/Monsky doubts, plural letter entries, tentative infinitésimales/pluriel/oo, clear Lecture, questions/suite/suiten with locally uncertain looped mesh, both local punctuation alternatives, Ch./Coh., V/v, abéliennes doubt, three Serre tracks, live terminal periods, definite y in thy, partial-start wave, Que-first short start, è/é/e accent doubt, coupled surname/comma choice, and the low-point spur. No separate comma doubt or discarded graphic hatch count survives in the preview or final remaining-doubt list.

**Final finding:** no material text-level blocker remains. This pass does not independently confirm ink or rendering and did not view images, run OCR, search external sources, or compile TeX.

Final reviewed preview SHA-256: `0a2e593320d301a552c9312457a0f9ce67f60cbf5e823b67b403acd04abdf23a`.

Final reviewed spec SHA-256: `d0ad6f4ee00b8ead3f873a31e8270dc969ae9f97c7d6b41847a9fa79483278c9`.

Root post-audit metadata note: the shorthand brief field v15 was normalized to reader_v15.md in the spec and final record. No page text, reading decision, count or audited witness field changed.
