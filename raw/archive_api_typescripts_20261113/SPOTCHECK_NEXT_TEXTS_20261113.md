# Spot check of the next texts against the scans

13 November 2026. Checked by Claude Opus 5.5 at effort max (sub-agent of the main session; no sub-agents of its own;
effort set at launch by the main session). The transcriptions were made by Claude Opus 5.5 at effort high over the
Message Batches API (batches brown_full, mtl129_full, t162_full, esq119_full, r119_full), one request per page, and
written by parse.py. No transcription file was changed and no API call was made.

## Result

| Text | Page (key) | Words | Word | Formula | Missed handwriting | Markup | All | All per 100 words | Reading errors per 100 words | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| brown | `brown_134-2_122` | 532 | 0 | 9 | 0 | 0 | 9 | 1.7 | 1.7 | second pass, limited to the letter F (sites 122–126) |
| mtl129 | `mtl129_129_050` | 226 | 0 | 0 | 0 | 5 | 5 | 2.2 | 0 | good enough as is (scripted markup fix) |
| t162 | `t162_162-5_014` | 325 | 0 | 2 | 0 | 4 | 6 | 1.8 | 0.6 | second pass on the handwritten layer |
| esq119 | `esq119_119_091` | 317 | 0 | 0 | 0 | 8 | 8 | 2.5 | 0 | good enough as is (scripted LaTeX fix, shared with copy 1) |
| r119 | `r119_119_273` | 213 | 1 | 0 | 1 | 6 | 8 | 3.8 | 0.9 | good enough as is (fix page 273) |

- Reading errors are word + formula + missed handwriting. Markup covers hand/typed marking, misuse of the macros and
  LaTeX syntax.
- Every occurrence counts as one error. The number of causes is much smaller: brown 1, mtl129 1, t162 5, esq119 1,
  r119 3.
- No typed word was misread on any of the five pages. The one word-class error is the length of a typed ornament.
- Words: tokens of the page body with macro names stripped; formula pieces count as tokens.

## Method

- Pages: the page of each text with the most handwriting macros, deletions and doubt marks in its `NOTES.tsv`, outside
  the 15 pages of `PILOT_NEXT_20261113.json`.
- Each page file was compared line by line with `work/img/<key>_a.jpg` and `_b.jpg`. Every symbol in doubt was cropped
  and enlarged 2–4 times; the boxes below are pixel boxes (x0,y0,x1,y1) in those images.
- An item that the crops could not settle is listed as doubtful and not counted.
- File line numbers are those of the page file (`cat -n`, the three comment lines included).

## brown_134-2_122: translation of the letter to Breen of 17/2/1975, first page

Typed English with formulas, two pencil notes in the left margin, handwritten archive number.

**Errors (9, one cause).** The typist used two forms of F:
- a serif F for the sheaf: "sheaves of groups F", "H^i(Y, F)", "f*(F)" in the cohomology;
- a sans-serif F for the gerbe and the champ, the letter that is presumably script in the French original.

The transcription writes `$F$` for both, so the distinction is lost. Rule 3 of the prompt ("the same letters,
alphabets") requires it. The model did keep the typist's italic element (`\textit{cohomological}` etc.), but not this
letter. The sans-serif F occurs at:

| File line | Transcription | Scan |
|---|---|---|
| 24 | n-gerbes `$F$` on | sans-serif F |
| 25 | `$F(Y) \to F(X)$` | both F sans-serif |
| 26 | such `$F$` and | sans-serif F (probable; read on the full image only) |
| 29 | n-champ `$F$` on | sans-serif F |
| 30 | `$F(Y) \to f^{*}(F)(X)$` | both F sans-serif |
| 34 | `$F \to f^{*}(F)$` | both F sans-serif |

Crops: a 300,845,1000,885 (serif F of the sheaves); a 880,880,1650,990; a 300,1050,1120,1120; b 300,105,1000,140.

**Right.**
- Every typed word, the quotation marks, the spacing before punctuation, `\xrightarrow{\cong}` (tilde over two bars on
  the arrow), Π_n, π_i, H^{n+1}(Π_{n-1}(X), π_n), the italics.
- The margin note "Stack" (underlined) at (A).

**Doubtful, not counted.** `\margin{topoi}` (line 20): the pencil shows t-o-p-i with a stroke above, and a second o is
not clearly there. The intended word is plainly "topoi", but the reading deserved `\unsure{topoi}`. Crop a 80,735,230,805.

## mtl129_129_050: Montréal notes, chapter II, typed page II.22

Typed French with formulas. Handwritten: II.22 at the top right, the λ's and x's in relation iii), a cross in the
margin, and the archive number 50.

**Errors (5 markup, one cause): typed special characters marked as handwriting.**

| File line | Transcription | Scan |
|---|---|---|
| 10, 13, 35 | `\hand{\mathcal{D}}` (3 times) | script D typed with a special type element: black, crisp, the same glyph all three times, unlike the grey hand strokes of the λ's |
| 13, 35 | `\underset{\hand{\to}}{\mathbb{W}}` (2 times) | small arrow typed half a line down, same ink as the type |

Crops: a 660,410,760,450; a 860,645,1060,695; b 1100,880,1240,935; b 600,700,840,770 (hand λ for comparison).

The same characters are marked inconsistently across the text:
- `\hand{\mathcal{D}}` occurs only on pages 041, 044 and 050 (3 each);
- 11 other pages give `\mathcal{D}` plain;
- the arrow under 𝕎 is `\underset{\rightarrow}` or `\underset{\to}` on 16 pages, `\hand` only on 050.

Pages 041 and 044 were not checked against the scans.

**Right.**
- Every typed word, all formulas: T_{F(x)} = T_x^p, the S_N and P_N relations with λ_1^{p^{1-N}} …, 𝔼, 𝕎_{N+1}, ℤ.
- The hand λ's and x's marked `\hand`, the margin cross, II.22.

## t162_162-5_014: Tapis de Quillen, copy 1, typed page 13

The hardest page of the five. Typescript with typewriter corrections, a diagram with handwritten labels, many
handwritten symbols, insertions between the lines and three margin notes.

**Errors (6).**

| File line | Kind | Transcription | Scan | Crop |
|---|---|---|---|---|
| 8 | markup | `\inserted{le composé}` (hand) | typed between the lines, in the typewriter's type: `\inserted[typed]{le composé}` | a 270,180,820,262 |
| 9 | formula (probable) | `\hand{)}` after the last `$\overline{T}'$` | no closing parenthesis after T̄'; the line goes on "ne dépend pas" | a 450,180,620,262 |
| 28 | formula | `$H^{\hand{\unsure{B}}}(X)$` | typed H• (the bullet as in H•(X) on lines 38 and 40) with a small hand mark above it, B or * (the margin NB writes H*(X)); the typed bullet is dropped | a 840,912,1250,965 |
| 40 | markup | `\Lambda` unmarked | Λ by hand, the same hand as lines 24 and 48, which are marked `\hand` | b 380,232,1300,305 |
| 40 | markup | `\simeq` unmarked | ≃ drawn by hand (thin pen strokes) | b 1270,232,1460,300 |
| 54–55 | markup (syntax) | `\uline{quas` never closed | brace imbalance; `COMPILE_FIXES.tsv` patches it at compile time | – |

**Doubtful, not counted.**
- Line 44 `\deleted{Le\xout{xx}}`: no stroke through "Le" is visible. The hand "(" and the arc belong to the insertion
  above; a tall hand "[" before them is not transcribed. Crop b 380,343,800,420.
- Line 18 `\hand{\Gamma}`: the Γ of "= Γ^! i_s" looks typed (crisp, serifed), unlike the hand Γ in the diagram.
- Line 38, insertion "il est d'ailleurs `\unsure{unique s'il existe}`": the second part looks like two short words
  ("…-il soit"?). It is marked `\unsure`, as it should be. Crop b 500,128,1360,208.

**Right.**
- Every typed word, with the typos kept ("strcture", "ppouve", "degréz" overtyped, "négatifsx" overtyped).
- The diagram with its labels α_s, α_s, i_s and the right-hand label marked `\unsure`.
- The margin notes, all three read correctly: "NB H*(X) (=H*(X,F_2))", "en fait H(X)≃B.(X)/Λ⁺B.(X)" and "i.e.
  l'enveloppe "Karoubienne"".
- The two "?" in the margin, the insertion "(à une infinité de générateurs X_i …)" with an honest `\illegible{2}`,
  the hand B above "abélienne-associée", and the hand <, ≤, ∈, the parentheses and the wavy underlining.

## esq119_119_091: Esquisse, copy 2, typescript page 13

Typed French with the handwritten symbols of the common original (ℙ, ℂ, ∈, ℚ, Q̄, the Galois group 𝕀Γ), which copy 2
reproduces.

**Reading: no error.** Every typed line and every symbol agrees with the scan.

**Copy 2's own annotations on this page.**
- The only one is the archive number "91" at the bottom left. It is recorded as `\margin{91}`; DIFFERENCES gives it as
  hand-missing and copy 1's "15" as addition.
- I found no other mark: the dots on the page are specks.

**Errors (8 markup, LaTeX syntax only, one cause).**
- Eight `\hand{$…$}` groups stand inside math mode: lines 12 (2), 14 (2), 25, 27, 29 (2). The inner `$` ends the
  math mode, so LaTeX reports errors.
- The model took this verbatim from the draft: copy 1's `esquisse/pages/esq_119_015.tex` has the same lines.
- Copy 1's combined build `work/compile/esquisse_combined.log` has 51 errors of this family ("Display math should end
  with $$", "\mathbb allowed only in math mode", "Missing $ inserted").
- A script can fix both copies (drop the inner `$` when `\hand` is already in math).

### Are copy 2's annotations recorded? (the whole text, sites 79–135)

Copy 2 was compared with copy 1 by image difference:
- every copy 2 half-image against copy 1's at site − 76, registered by phase correlation;
- copy 1's ink dilated by 6 px;
- clusters of ink present only in copy 2 reported in two passes: dark ink (grey < 150, clusters ≥ 120 px) and faint
  ink (grey < 195, ≥ 50 px).

The dark pass found 20 clusters on 13 pages, the faint pass 131 on 33 pages.

Most clusters are not annotations:
- specks in the top corners (checked on 079 and 135: the same speck is in copy 1, displaced);
- misregistration bands (130: 53 clusters at the line starts; 127 and 111: the cut between the half images);
- the archive numbers at the bottom left.

Every other cluster lies on an annotation that the transcription records:
- 079: title and author struck;
- 080: n struck in "inadéquante";
- 085: the blue n struck, with its margin sign; the only blue ink in copy 2, found by a separate colour test;
- 086: asterisk, margin sign, the move mark for "dans ce jeu";
- 088: margin "n";
- 090: "re" inserted;
- 095: two margin "?", the circled (*);
- 102: margin "x";
- 114: s struck;
- 118: "espacer" and the brackets;
- 119: margin "x";
- 122: "trois" over "deux";
- 124: "algébrique" inserted;
- 125: "les" inserted;
- 131: margin "/".

**One mark is not transcribed: site 123** (typescript p. 45).
- A pen dot stands in the left margin beside the line "dant par piété", where the hand corrected "pitié" to "piété".
  Copy 1 has no dot there.
- The model saw it and called it a speck in NOTES. It sits on the corrected line, as the margin signs of the other
  corrections do, so it is probably a mark.
- The correction itself, `pi\over{ti}{\unsure{ét}}é`, is right. Crop b 150,360,700,420 (copy 1: `esq_119_047_b.jpg`,
  same box).

**Limit of this test.**
- Hand corrections written over typed letters (the `\over` corrections of 087, 088, 121, 123, 124, 128) and light
  pencil inside the text block are hidden by copy 1's ink, so the image difference does not test them.
- Of these, only 123 was looked at on the scan.

**Conclusion: copy 2's annotations are recorded.** Every copy-2-only mark that the difference shows is in the
transcription, except the probable margin dot of site 123.

## r119_119_273: proposal on the doctorat d'État, second page

The upper half is typed. The lower half has pencil notes, four of them ringed, and two ruled lines.

**Errors (8).**

| File line | Kind | Transcription | Scan | Crop |
|---|---|---|---|---|
| 24 | word (trivial) | `-:-:-:-:-:-:-:-:-:-:-` (11 dashes, 10 colons) | 12 dashes and 11 colons, counted by blob detection | b 680,110,1110,150 |
| 38 | missed handwriting | `\margin{\unsure{recherche enseignement}}` | a separate C-shaped sign stands between the words (c, ⊂ or similar): "recherche C enseignement" | b 180,555,760,620 |
| 26, 32, 38 | markup (4) | `\margin{(encircled) …}` | the oval is drawn round the note; "(encircled)" is a description written as if it were the pencil's words | – |
| 36, 42 | markup (2) | `\margin{(line drawn under the above)}` | a ruled pencil line; a description written as handwriting | – |

**Right.**
- Every typed word: "esr" and "decision" kept, `\unsure{responsabilite|responsabilité}` honest.
- The pencil readings are right as far as the scan shows: "assistants pas à l'ancienneté", "un peu de recherche",
  "option momentanée", "nominations par étudiants", "thèse --", "enseignants parallèles (diversification)", "décision
  des étudiants", "mandarinat".
- `\unsure{pas|par}` and `\unsure{comp.|sup.}` are honest marks; NOTES lists every uncertain reading.

The descriptions inside `\margin` occur only on this page of r119.

## Systematic findings

1. **The hand/typed decision for single characters is unreliable in both directions.**
   - Typed 𝒟, typed arrows and a typed insertion are marked as handwriting (mtl129, t162).
   - A hand Λ and a hand ≃ are left unmarked (t162).
   - The decision is taken per occurrence, so the same glyph is marked differently on one page or across pages.
   - This matters most where the handwriting is the point (the copy 2 pages of t162, the offprints of r119 and t162).
2. **A change of letterform within one alphabet is not kept** (brown: sans-serif F for the champ against serif F for
   the sheaf). Italic words are kept.
3. **Descriptions are improvised inside content macros** where the macro list has nothing for them: ringed notes and
   ruled lines (r119 273). They belong in `% NOTE:` lines.
4. **LaTeX syntax.**
   - `\hand{$…$}` inside math in esq119, inherited from copy 1, which has the same defect.
   - An unclosed `\uline{` in t162 014, patched at compile time.
   - Both can be found and fixed by script.
5. **The archive number is encoded four ways:**
   - `\mspage{123}` (brown);
   - `\mspage{\hand{50}}` (mtl129);
   - `\margin{14}` next to `\mspage{13}` for the author's number (t162);
   - `\margin{91}` (esq119), `\mspage{\hand{273}}` (r119).

   Not counted as errors; a script can make them uniform before the combined files are used.
6. **Doubt marking works.** The hard readings carry `\unsure`, and NOTES name the places to look (t162 014's
   insertions, r119 273's pencil, the dot of esq119 123). No confident misreading of a typed word was found.

## Verdicts

- **brown: needs a second pass, limited to the letter F.** The words are right and so are the formulas otherwise.
  - On the February letter (sites 122–126), mark the sans-serif F of the gerbes and champs as a letter distinct from
    the serif F of the sheaves (e.g. `\mathsf{F}`).
  - Check the July letter (128–143) for the same distinction.
  - Pilot page 124 belongs to the same letter.
- **mtl129: good enough as is.**
  - Remove `\hand` around the typed `\mathcal{D}` (pages 041, 044, 050, after a look at 041 and 044) and around the
    arrows under 𝕎 on 050.
- **t162: needs a second pass on the handwritten layer** (by eye, not a rerun).
  - The typed text and the margin notes are good.
  - The hand/typed marking and the short insertions need a look on every annotated page, first the 16 pages with
    long handwriting or ten or more `\unsure` marks in NOTES: sites 2, 4, 8, 9, 11, 14, 15, 17, 34, 38, 39, 41, 45,
    47, 48, 58 (8, 41 and 48 are pilot pages).
  - Above all, look at copy 2 (32–48), whose annotations are the point.
- **esq119: good enough as is.** Copy 2's annotations are recorded.
  - Add the probable margin dot of site 123.
  - Fix the nested `$` by script in both copies.
- **r119: good enough as is.**
  - On page 273, turn "(encircled)" and "(line drawn …)" into `% NOTE:` lines and add the sign between "recherche"
    and "enseignement".
  - This rests on one page of a 154-page text that is mostly typed or printed.

## Files

- Page files: `brown_translations_134-2/pages/brown_134-2_122.tex`, `montreal_seminar_129/pages/mtl129_129_050.tex`,
  `tapis_de_quillen_162-5/pages/t162_162-5_014.tex`, `esquisse_copy2/pages/esq119_119_091.tex`,
  `cote119_rest/pages/r119_119_273.tex`.
- Images: `work/img/<key>_a.jpg`, `_b.jpg`; copy 1: `work/img/esq_119_<site>_a.jpg`, `_b.jpg`.
- Also read: `NOTES.tsv`, `COMPILE_FIXES.tsv` of each text; `esquisse_copy2/DIFFERENCES.tsv`;
  `esquisse/pages/esq_119_015.tex`; `work/compile/esquisse_combined.log`; `scripts/prompt_system.txt`;
  `scripts/preamble.tex`.
- The crops and the two helper scripts (crop montage, copy 2 / copy 1 image difference) are in the session scratchpad,
  `C:\Users\user\AppData\Local\Temp\claude\f2c80a22394db22f\9fc52c26-b302-4eb7-b4c2-be7f7bbafcc9\scratchpad\`
  (`cropstack.py`, `copydiff.py`). They are not kept in the job folder; the boxes above reproduce every crop.
