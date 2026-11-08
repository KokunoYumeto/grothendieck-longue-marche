# LM_P048 — Editorial and research notes

## 1. Scope, pagination, and conventions

The accompanying `LM_P048_transcription.tex` is a diplomatic LaTeX fragment of the ten supplied images. It starts with `\scanpage{471}`, has no preamble or macro definitions, and preserves the supplied sequence. The opening page is the end of a preceding discussion; section 33 begins on the next image. The final sentence is unfinished at the end of scan 480 and has not been completed.

**Pagination discrepancy:** the filenames and task labels are one higher than the archival footer numbers actually visible in the images. The required filename-based labels are used in `\scanpage`; the author's visible upper page numbers are recorded with `\mspage`. The printed institutional footer and the lower archival numbering are not treated as manuscript prose.

| Requested scan / filename suffix | Visible archive footer | Visible upper manuscript number |
|---|---:|---:|
| 471 | 470 | 238 |
| 472 | 471 | 239 |
| 473 | 472 | — |
| 474 | 473 | 240 |
| 475 | 474 | — |
| 476 | 475 | 241 |
| 477 | 476 | — |
| 478 | 477 | 242 |
| 479 | 478 | — |
| 480 | 479 | 243 |

A dash in the last column means that no upper manuscript number is visible; none has been supplied by inference. All research-note citations below use the **requested scan label**, with this table providing the correspondence to the visible footer.

The manuscript's words and notation were read from the supplied images, with enlarged inspection of difficult areas. No published transcription, later work, or external reconstruction was used to settle the handwriting. Ordinary line breaks inside paragraphs have generally been joined; the unusual divided word at the end of the batch remains divided because its reading is uncertain.

`\unsure{...}` indicates a tentative reading, including uncertainty about a symbol's alphabet, decoration, punctuation, or cancellation state. Alternatives are separated by `|` only where a second reading can be proposed. `\illegible{n}` gives an estimated count; for an unreadable mathematical mark, the estimate counts a symbolic unit rather than a lexical word. Repeated occurrences of the same uncertain glyph are grouped in the doubt tables, but remain marked individually in the transcription.

The doubled-stem Gamma-like signs are provisionally rendered as `\unsure{\Gamma}`; this is **not** a secure identification of their alphabet. Clearly single-stem forms are distinguished where the ink permits it. The large rounded G-like signs also retain alphabet doubts, and one hat, two stacked hats, and a superscript plus have been distinguished where visible. The diagram in scan 473 is described within `\diagram{[...]}` because its horizontal links have left curls without secure arrowheads; the clearer diagrams use `tikz-cd`.

The fragment was checked in a temporary LaTeX wrapper with definitions for the requested editorial macros and standard mathematical packages. This is a syntax check, not a claim that the doubtful readings have been resolved. Only the requested fragment and this notes file are included in the archive.

## 2. Table of doubts

Confidence is confidence in the retained reading, not in the mathematical claim. Line numbers approximate handwritten baselines, not lines in the LaTeX source. For scans 471–476 and 479–480, displays count as text rows and upper page numerals do not; the special counting convention for scans 477–478 is stated with their table. Marginal and interlinear locations are identified separately.


### Scan 471

| Scan | Approximate line | Reading in the transcription | Alternative or unresolved feature | Confidence |
|---|---|---|---|---|
| 471 | 2, after « l'aise » | `tant` | The internal strokes are compressed; no secure alternative. | medium |
| 471 | 5, beginning | `\frac{1}{2} simples` | The stacked sign looks like one-half; its lexical meaning is not expanded. | medium |
| 471 | 5, final word | `\uline{topologie}` | `topologie` without emphasis: the apparent underline may belong to the descending letter stroke. | low |

### Scan 472

| Scan | Approximate line | Reading in the transcription | Alternative or unresolved feature | Confidence |
|---|---|---|---|---|
| 472 | 2, title | `\mathcal N_{g,\nu}` | Ordinary `N`; exact alphabet not secure. | medium |
| 472 | 4, cancellation after π | `,a` | Small cancelled symbol after π cannot be securely identified. | low |
| 472 | 5, after π′ | `ss-grpe` | `ss-grp`; last abbreviated letter is compressed. | medium |
| 472 | 6 | `régulière` | Ending and middle strokes are not fully separated. | medium |
| 472 | 7, both function names | `Discrét` | Accent and exact abbreviated ending are uncertain. | medium |
| 472 | 7, connector | `\hookrightarrow` / `\longleftarrow` | Visible line has a curled left end; the right end has no clear arrowhead. Direction is not silently supplied. | low |
| 472 | 9, cancelled phrase at right | `des` plus one illegible word | Most of the phrase is crossed through and overwritten. | low |
| 472 | 8–9, interlinear replacement at right | `de l'arithmétisabilité` | The end is crowded at the right edge; attachment to « relation d'équivalence » is probable. | low |
| 472 | 10, cancelled word | `prouver` | Deletion intersects the word. | medium |
| 472 | 10, before « arithmétisation » | `\forall e` | `tte`; the small final mark and abbreviation/allograph cannot be resolved. | low |
| 472 | 12, cancelled beginning after « les » | `discre` | Incomplete cancelled word, not expanded. | low |
| 472 | 16, A-map | Rightward arrow, marked doubtful | Horizontal shaft is clear; arrowhead is not. | low |
| 472 | 19, before « caractéristique » | Deleted `invariant` | The initial letters and cancellation are compressed. | low |
| 472 | 20, reference after « diagramme 7 » | `ff` | Two tall f-like strokes are visible; no expansion assumed. | high |
| 472 | 20, last word | `Choisissant` | `Choisissons`; ending is not secure. | medium |

### Scan 473

| Scan | Approximate line | Reading in the transcription | Alternative or unresolved feature | Confidence |
|---|---|---|---|---|
| 473 | 1, between π and π′₀ | `donc` | Last strokes are abbreviated. | medium |
| 473 | 2, 4, diagram right column, final identities | `\widehat{\widehat{\mathcal G}}` | Two stacked small marks are visible; the exact calligraphic/Gothic alphabet of the large glyph remains uncertain. | medium |
| 473 | 4, homomorphism | Rightward arrow, marked doubtful | The right end is a short dark stroke rather than a clearly resolved point. | low |
| 473 | 7, parenthesis | `parent` | The beginning is retraced; no secure alternative. | medium |
| 473 | 8–9, diagram left column and final identities | `\widehat{\mathcal G}^{+}` | One hat and an elevated cross are visible; the alphabet and the lower-left cross's shape remain uncertain. | medium |
| 473 | 9, lower middle of diagram | `M` followed by an illegible raised mark | Possibly a cancelled or overwritten symbol; it is not silently removed or interpreted as a prime. | low |
| 473 | 8–9, four horizontal diagram links | Described by shape rather than assigned arrow direction | Each left end is curled; no clear horizontal arrowhead can be read. All three vertical arrowheads point down. | low |
| 473 | 12, before π₀ | `que` | `par`; the opening descender is unclear. | medium |
| 473 | 13, above π′₁ | Inserted `discrét` | Shortened word and final mark, not expanded. | medium |
| 473 | 16, first map | `P` with superscript + | Initial capital is overwritten, possibly over a different letter. | medium |
| 473 | 17 | `exprimer` | `examiner` is less well supported because a p-like descender is visible; the compressed word remains marked. | medium |

### Scan 474

Line estimates count main handwriting lines from the top, including displays, excluding the page number; interlinear insertions belong to the adjacent line.

| Scan | Approx. line | Reading retained | Alternatives / difficulty | Confidence |
|---|---:|---|---|---|
| 474 | 1 | `autom.` | Word appears abbreviated; terminal point is faint. | medium |
| 474 | 1 | `π⁺` | Short raised stroke at right of π could belong to the letter rather than be a plus. | low |
| 474 | 2–3, 6 | `\widehat{\mathcal G}` | Rounded, looped G-like glyph with a hat; exact script alphabet is not fully recoverable. | medium |
| 474 | 2 | Two deleted words illegible | The strike crosses an initial short group resembling `i.e.` and a final descending stroke; no complete reading retained. | low |
| 474 | 4 | One deleted word illegible | Dense horizontal cancellation. | low |
| 474 | 4–5 | `propre` (possibly `propré` in first occurrence); inserted `non` before the second occurrence | Reading of *propre* is plausible but the medial letters are compressed; `non` is interlinear and its connector points to the second occurrence. | medium |
| 474 | 6–7 | `\Gamma` | Gamma-shaped sign has a doubled vertical stroke; the typeface assignment, including the Q subscript alphabet, is uncertain. | medium |
| 474 | 12 | `arithm.` | Beginning of the word is overwritten, and the terminal abbreviation point is weak. | medium |
| 474 | 13 | `(3)` after `l'iso.` | The closing parenthesis is clear; opening parenthesis is faint or merged with numeral. | medium |
| 474 | 14–15 | `inv. car.` | First abbreviation looks like `inv.`; no expansion adopted in the transcription. | medium |
| 474 | 17–18 insertion | `arithm. extérieures,` | Insertion belongs after *correspondances*; final comma may instead be part of the connector. | medium |

### Scan 475

| Scan | Approx. line | Reading retained | Alternatives / difficulty | Confidence |
|---|---:|---|---|---|
| 475 | 2 | Deleted `)` after `p.ex.,` | A hooked, overwritten sign occurs before *qui*. It may be a canceled closing parenthesis, relocated to the next line. | low |
| 475 | 3 | `can.` | Ink is darkly overwritten; final point is not secure. | medium |
| 475 | 4–5, 13, 17 | `\Gamma` where doubled; ordinary `\Gamma` where single | Several Gamma-like signs have a clearly doubled stem, others a single stem. The alphabet assignment remains uncertain rather than silently homogenized. | medium |
| 475 | 5 | `un` before `l'isom.` | A short wavy word appears here; reading retained with doubt despite the awkward resulting syntax. | low |
| 475 | 5 insertion | `canonique` | Initial letters are overwritten; connector attaches after `l'isom.`. | medium |
| 475 | 6 deletion | `multiple commun` | The cancellation runs through these words; not expanded to *multiplicité*. | medium |
| 475 | 7 | `regardant` | Medial letters and final compressed ending are not all separately visible. | medium |
| 475 | 8 deletion | `N de 2g−2+ν et 2g′−2+ν′` | Cancellation partly coincides with the lower horizontal strokes. The displayed primes and plus signs are probable; the `et` is small. | medium |
| 475 | 12 | `et` before `d'où` | Thick short sign could be a hurried `et` or a canceled fragment. | low |
| 475 | 17 | `hom` | No secure terminal point; the abbreviation has not been silently expanded. | medium |
| 475 | 17 insertion | `can.` | Word clear enough as `can`; terminal point doubtful. | medium |
| 475 | 17 formula | Rightward arrow | Horizontal connecting stroke is clear but arrowhead weak; no claim of an equality is made. | medium |
| 475 | 21 | `inv.` before `car.` | Overwritten initial strokes and uncertain punctuation. | low |
| 475 | 21 formula | `\widehat{\widehat{\mathcal G}}` followed by single-hatted `\mathcal G^{+}` | Two separate carets visibly occur over the first G-like glyph; one caret plus `+` over each following glyph. Exact letter alphabet remains uncertain. | medium |

### Scan 476

| Scan | Approx. line | Reading retained | Alternatives / difficulty | Confidence |
|---|---:|---|---|---|
| 476 | 4–12 formulas | `\Gamma` / `\Gamma` | Doubled-stem and single-stem Gamma-like forms are retained with alphabet uncertainty. | medium |
| 476 | 6 deletion | `s'envoie` | Initial stroke could be `l'envoie`; deletion passes through its body. | low |
| 476 | 8, right | Marginal `! − A` | Heavy exclamation-like mark with a dot joins a horizontal stroke to an A/triangle-like overdrawn sign. It may be a canceled fragment or emphatic mark; exact reading and state uncertain. | low |
| 476 | 10, deleted block opening | `défaut` / `à défaut` | First loop, ascenders and final horizontal strokes partly coincide with cancellation. | low |
| 476 | 10, deleted block | `je vais montrer` | Several very compressed strokes under the cancellation line. | medium |
| 476 | 12, deleted block | `ds` | Could be a hurried full *dans*; no expansion supplied. | low |
| 476 | 12, deleted block | `finie` / `fini` | Final stroke not fully distinct; word is independently underlined. | medium |
| 476 | 10–13 cancellation scope | Deleted text through `ce qui signifie aussi`; inserted `iso pour ∀(g,ν)` | The large rectangular/diagonal cancellation and replacement are layered. The active replacement's reading is clear, but its exact insertion status is less secure. | medium |
| 476 | 15 deletion | `puisse` | Canceled word following `(g,ν)`; interior letters indistinct. | medium |
| 476 | 17 | `étale` | Initial accented letters are overwritten. | medium |
| 476 | 17 formula | `\mathcal U_{0,3}` | Overdrawn capital resembles a script U but might be X; alphabet uncertain. | low |
| 476 | 18 insertion | `(avec sa str. à lacets)` | First words are compressed; *avec str.* is also possible. Connector attaches after *se réalise*, before *comme*. | low |
| 476 | 19 | `ss-groupe` / `ss: groupe` | Punctuation after the two s-like letters resembles a colon rather than a simple hyphen. | low |
| 476 | 19 deletion | `d'in` | Short canceled fragment to the right of the inserted *d'indice fini*; incomplete word retained without completion. | low |
| 476 | 20 deletion | `prenant` | Horizontal strike obscures the middle letters. | medium |
| 476 | 20 insertion | `π″ ≃ π_{g″,ν″}` | Relation is small and written on the line below; `∼` possible instead of `≃`. | medium |
| 476 | 20 formula | `π″ ⊂ π_{g,ν′}` / `π″ ∈ π_{g,ν′}` | Inclusion/membership sign has been heavily retraced; no semantic correction made. | low |

### Scans 477–478

Here “scan” follows the supplied filename and requested sequence. The printed footer of file `LM_P048_scan477.jpg` is 476; that of file `LM_P048_scan478.jpg` is 477. Approximate line numbers count main handwriting lines, excluding diagrams and marginal additions; on scan 477, line 1 begins “d'où notre…”. On scan 478, line 1 begins “ν en ν′…”, and the cancelled line below the underlined sentence is counted as line 3.

| Scan | Approximate line/location | Reading retained | Alternatives or source of doubt | Confidence |
|---|---|---|---|---|
| 477 | Opening diagram and throughout | `Γ` | The left stem is doubled in these symbols. Ordinary Gamma versus a deliberately double-stroke alphabet is not settled; each such occurrence is marked. The plainly single-stroke `Γ=Γ_K` near the bottom is distinguished. | medium |
| 477 | Opening diagram, right upward arrow | `\wr` | The glyph looks like a small 2; a vertical isomorphism mark is plausible but not imposed. Arrow direction upward is clear. | low |
| 477 | Beside opening diagram | `diagramme comm.` | The middle of “diagramme” is a cursive wave; “comm.” is clearer. | medium |
| 477 | 1 | `assertion` | Several inner letters are short strokes. | medium |
| 477 | 3 | `factorise` | Ending and middle are compressed. | medium |
| 477 | 3, 9 | `p.ex.` | Exact letter and dot pattern is small; the abbreviation is not expanded in the transcription. | medium |
| 477 | Above 3 | `(ν≥ν′)` | An insertion after “factorise”; ≥ and the prime are visible. The curved guide is treated as an insertion guide, not as emphasis. | high |
| 477 | 5, after “Mais” | `il` plus about three unreadable deleted words, and one deleted interlinear word | Heavy cancellation obscures both the wording and the revision order. The estimated word counts should not be treated as exact. | low |
| 477 | 9 | `éventuelle` | The initial syllable is retraced/overwritten. | medium |
| 477 | 10, map to `Γ_{g,0}` | rightward arrow, alternative plain stroke | Only a horizontal stroke is unambiguous; an arrowhead cannot be securely distinguished. | low |
| 477 | 10 | `ou` | A short cursive wave between the two displayed maps. | medium |
| 477 | Lower left margin | `On va faire un peu d'… conjecturer (établir) pour l'injectivité du (3)` | “faire”, “conjecturer”, “(établir)”, “pour”, “injectivité”, and “(3)” are all provisional; one word after “d'” is unreadable. The close, oblique writing makes even the relative order of the middle words uncertain. | low |
| 477 | 11, insertion; 15, formula | `U` | Ordinary versus calligraphic capital U is not resolved from the ductus. | medium |
| 477 | 13 | `donc` | Alternative `d'où`; the final cursive stroke favors “donc”, but not securely. | medium |
| 477 | 16, cancellation after `K` | `en K′, OPS que` | “en” and “que” are tentative; the intervening acronym is probably the same `OPS` as on the following page, but is crossed through. | medium |
| 477 | 16, final word | `agrandir` | Ending is compressed at the right edge. | medium |
| 478 | Throughout, curve symbols | `U`, `U′` | Ordinary versus calligraphic U remains uncertain. | medium |
| 478 | 1, insertion | `pour trouver U′` | “trouver” has compressed middle letters; insertion is attached inside the parenthesis after “trous”. | medium |
| 478 | 2, before `(U_{0,3})_K` | deleted `P¹_K` | The reading as projective P with exponent 1 is plausible; the exact cancellation/retracing state is also uncertain and is wrapped in `\unsure`. | low |
| 478 | Left margin | `π′=π₁(U′_{Q̄₀})`, `π=π₁(U_{Q̄})` | The second formula has no securely visible subscript 0 after Q̄. It has therefore not been supplied to match the first formula. | high |
| 478 | Right edge near 2, cancelled | `Choisissons` | The end meets the black border; only the beginning is secure. | low |
| 478 | Right edge / 3, cancelled | `Considé-rons` | “Considé-” is clearer at the edge; the next line's cancelled initial strokes are read provisionally as its continuation “rons”. The original hyphen is retained. | medium |
| 478 | 3, cancelled | `π` | Alternative capital `Π`; the tall, retraced glyph is not securely distinguishable. | low |
| 478 | 3, cancelled | `rel/K` | “rel” is provisional; possibly another abbreviation. | low |
| 478 | 3, cancelled | `Γ′` | Prime and exact stroke alphabet are affected by the cancellation. | low |
| 478 | 3, cancelled | `effectivement` | The cancellation crosses much of the word; no alternative is secure. | medium |
| 478 | 4 | `Θ` | A small upper-right stroke could be a prime or a remnant of the cancelled line above. | low |
| 478 | Display after 4 | `Γ′` | Alternative `Γ`; the right end of the heavily retraced top bar may imitate a prime. The literal cap-shaped inclusion mark below the left object is preserved separately. | low |
| 478 | 5, 7 | `autom.` | Alternative unpunctuated `autom`; a full stop is not consistently separable from the final stroke. | medium |
| 478 | 5, first hatted π | subscript `03` | Alternative `0,3`; no comma is securely visible in this occurrence, whereas the later one has a clearer comma. | medium |
| 478 | 6, before “image” | deleted `son`, inserted `l'` | “son” is partly overwritten by the short replacement. | low |
| 478 | Above 6 | `Θ′=Γ′∩Θ` | The intersection-shaped mark is sharply pointed, potentially `∧`; neither is silently normalized. | medium |
| 478 | Above 9 | `N(π) et dans` | The alphabet of N is uncertain: ordinary versus calligraphic. The guide places the insertion before the following `Γ_π`. | medium |
| 478 | 10 | `base` | Alternative `bon`; the compact ending does not permit a confident choice. | low |
| 478 | 11 | `effective` | The final letters are compressed. | medium |
| 478 | 11, preposition before π₁ | `dans` | Alternative `de`. | low |
| 478 | 11, π₁ formula | `π₁(U,P)` | Alternative `π₁(U′,P)`; U is retraced and a possible prime/opening parenthesis is not cleanly separable. | low |
| 478 | 13, between `U` and `{P}` | backslash | Alternative short dash; the inscription is a very short, thick descending stroke, almost dot-like. | low |
| 478 | 14, deleted phrase | `si (g,ν) est tel` | Last word “tel” is provisional. | low |
| 478 | 16 | `la` | Alternative `les`, before “V.A. A”. | medium |
| 478 | 20 | `devient` | Initial letters are retraced; reading is probable but not certain. | medium |
| 478 | 20 | `d'imaginer` | The vowel and middle sequence are compressed. | medium |
| 478 | 21, after “il” | possibly deleted `Θ` | An isolated overwritten glyph has the general outline of Theta; both identification and cancellation state are uncertain. | low |
| 478 | 22, final words | `J'ai` | The end lies close to the page frame and the letters are heavily retraced. | medium |

### Scans 479–480

| Requested scan | Approximate line | Reading used | Alternatives / limitation | Confidence |
|---|---:|---|---|---|
| 479 | 3 | Deleted `crois je` | The strike obscures the middle letters; `crois-je` is possible, but no hyphen is securely visible. | low |
| 479 | 4 | `Cela` | `Cel`; the terminal letter is not separately resolved. | medium |
| 479 | 4 | `signifierait` | Medial and final compressed strokes are not all resolved; no dependable alternative. | medium |
| 479 | 4–5, 9–10, 13–14 | `$\Gamma_{\mathbb Q}$`, `$\Gamma_{0,3}$`, `$\Gamma_{g,\nu}$` | These have a conspicuously doubled left stem. The transcription marks each occurrence as uncertain because ordinary versus doubled-stem Gamma typography, and ordinary versus blackboard-style Q, are unresolved. | medium |
| 479 | 6 | `$\pi_1$` | `$\Pi_1$`; handwritten case is uncertain. | medium |
| 479 | 6, above line | Inserted `$\simeq\overline{\pi}_{g,\nu}$` | `$\simeq\overline{\Pi}_{g,\nu}$`; the horizontal bar is visible and was not converted into a hat. | medium |
| 479 | 8 | `de` before `l'extension` | `des` cannot be fully excluded from the terminal curved stroke. | medium |
| 479 | 9, above line | Inserted `$N_{g,\nu}$` | `$\mathcal N_{g,\nu}$`; insertion and index are clearer than alphabet. | medium |
| 479 | 9 | `$\widehat{\mathcal T}_{g,\nu}$` | `$\widehat{\mathcal C}_{g,\nu}$` or another ornate G-like form; this glyph has a left angular top and a large curved right-hand portion. | low |
| 479 | 10 | `$M_{g,\nu}$` | `$\mathcal M_{g,\nu}$`; ordinary versus calligraphic alphabet. | medium |
| 479 | 11 | `$\widehat{\mathcal G}_{g,\nu}$` | `$\widehat{\mathcal C}_{g,\nu}$`; the ornate form differs visibly from the first kernel symbol. | low |
| 479 | 14 | `caractériser` | Several medial letters are compressed; no reliable alternative word is offered. | medium |
| 479 | 15 | `$N_{g,\nu}$` | `$\mathcal N_{g,\nu}$`; here the initial stroke is also overwritten. | medium |
| 479 | 18 | `correspondant` | Word ending is a short stroke; no reliable alternative. | medium |
| 480 | 1 | `que` followed by deleted `il suffit` | `qu'`; the visible deletion line starts over `il`, leaving the first short word less clearly cancelled. | low |
| 480 | 1 | Deleted `il suffit` | Reading is plausible under the crossing; extent of the original phrase remains uncertain. | medium |
| 480 | 1 | `en tout excluant` | `en tant excluant`; the short words are especially unclear, and this tentative sequence has not been made grammatical. | low |
| 480 | 2 | `donnée` | `donné`; final e not separately resolved. | medium |
| 480 | 3 | `ss-groupe` | `ss-groupes`; possible final s. | medium |
| 480 | 3, insertion below | `$\widehat{\pi}_{0,3}^{\Gamma''+}$` | `$\widehat{\Pi}_{0,3}^{\Gamma''+}$`; the double prime and plus are visible, but case and precise alphabet are uncertain. | medium |
| 480 | 3, insertion below | Deleted unreadable material between the preceding expression and `$(1)$` | Estimated one mathematical token/word. No equality or inequality has been supplied through the obliteration. | low |
| 480 | 4 | `concevable` | Some medial strokes are compressed. | medium |
| 480 | 9 | Deleted `en termes` | The horizontal crossing obscures the smaller letters. | low |
| 480 | 9, above deletion | Inserted `sans avoir` | Placement is above the deleted phrase; no alternative proposed. | high |
| 480 | 10–11 | `s'endea-` / `vorer` | `s'ende-` / `vorer`; a rare or nonstandard verb appears to be divided across the lines. The line-break hyphen is retained and the word is not replaced by a usual French synonym. | low |
| 480 | 13 | `sur` in `bien sur` | `sûr`; a circumflex is not securely visible. | medium |
| 480 | 14, 21 | `$\Gamma''$` | This Gamma appears to have a single stem, unlike the doubled forms on scan 479; exact alphabet remains marked. | medium |
| 480 | 14 | Deleted unreadable mathematical symbol before `$\widehat{\pi}_{0,3}$` | A pi-like base is partly visible, but its decoration/index is obliterated; estimated one token. | low |
| 480 | 14, 16, 19 | `$\widehat{\pi}_{0,3}$` | `$\widehat{\Pi}_{0,3}$`; lower- versus upper-case pi. | medium |
| 480 | 16, above line | Inserted `$\pi'$` | `$\Pi'$`; prime is visible. The insertion belongs after `donné` and before `de`. | medium |
| 480 | 17 | `supposer` | Infinitive ending compressed; no dependable alternative. | medium |
| 480 | 18 | Deleted `compatible` | Some inner letters are crossed out; final tall loops remain visible. | medium |
| 480 | 18, above deletion | Inserted `de telle façon que` | The last `que` is small and near the descending stroke of `qu'il` in the row above; insertion placement is nonetheless fairly clear. | high |
| 480 | 19 | Deleted `avec` | Heavily crossed short word; reading follows remaining strokes only. | medium |
| 480 | 19 | `$\pi'\longrightarrow\widehat{\pi}_{0,3}$` | Upper-case pi remains possible; arrow points right and prime is visible. | medium |
| 480 | 21 | `$\pi$` after `sur` | `$\Pi$`; **no prime is securely visible here**, so none was added. | medium |
| 480 | 21 | `déduise` | Ending compressed; no dependable alternative. The page then ends with `de`. | medium |

## 3. Abbreviations met

The expansions below are contextual proposals only. They are not substituted into the transcription; unresolved forms remain unresolved.

| As written | Tentative expansion or interpretation | Scans |
|---|---|---|
| `\frac{1}{2} simples` | Fractional shorthand, perhaps « demi-simples » or « semi-simples »; uncertain. | 471 |
| `ext.` | extérieur(s), extérieure(s), or extérieurement, according to context. | 472, 475, 480 |
| `ss-grpe` / `ss-grp` | sous-groupe; final abbreviated letter uncertain. | 472 |
| `ss-groupe` / `ss: groupe` / possible `ss-groupes` | sous-groupe(s); punctuation or ending uncertain in the indicated occurrences. | 476, 480 |
| `Discrét` | Notation referring to discrétifications; exact written accent/ending uncertain. | 472 |
| `\forall e` / `tte` | Possibly « toute »; universal-quantifier-like sign versus abbreviated word unresolved. | 472 |
| `\overline{\mathrm m}` | même. | 472–475, 478 |
| `Cf` | Confer / comparer. | 472 |
| `ff` | Unresolved; retained provisionally without an expansion. | 472 |
| `hom` / `hom.` | homomorphisme(s); punctuation varies or is uncertain. | 473–475, 477–478 |
| `resp.` | respectivement. | 473–474 |
| `discrét` | discrétification, probably. | 473 |
| `prédiscr.` | prédiscrétification. | 473 |
| `or.` | orientée. | 473 |
| `arithm.` | arithmétisation(s) or arithmétique(s), according to the local construction. | 473–474 |
| `i.e.` / `i.e` | *id est*, c'est-à-dire; final point is not uniform. | 474, 476, 478–479 |
| `autom.` / `autom` | automorphisme(s); terminal point sometimes uncertain. | 474, 478 |
| `can.` | canonique / canoniquement. | 474–475 |
| `iso.` / `iso` / `isom.` | isomorphisme; adjectival use possible in « est iso ». | 474–476, 479 |
| `inv. car.` | invariant caractéristique, tentatively; first abbreviation is uncertain. | 474–475 |
| `car.` | caractéristique. | 476 |
| `p.ex.` / `p.ex,` | par exemple; the points and comma are retained according to the reading. | 474–475, 477 |
| `ds` (deleted, uncertain) | dans. | 476 |
| `rev.` | revêtement. | 476, 478 |
| `str.` (uncertain insertion) | structure. | 476 |
| `comm.` | commutatif, in « diagramme comm. ». | 477 |
| `OPS` | on peut supposer; no separating points are securely visible. | 477–478 |
| `rel` (deleted, uncertain) | relatif; possibly describing a fundamental group relative to K. | 478 |
| `int.` | intérieurs. | 478 |
| `rat/K` | rationnel sur K; no point after `rat` is securely visible. | 478 |
| `V.A.` | variété abélienne. | 478 |
| `mod iso` | modulo isomorphisme. | 480 |

## 4. Honest assessment of legibility

Most uncancelled prose is readable at moderate confidence. The short scan 471 is comparatively clear, except for the fractional shorthand and the possible underline under *topologie*. On scans 472–475, the principal risks are cramped abbreviations, an insertion at the right edge, overwritten capitals, and the distinction between hats, plus signs, and letter flourishes. The horizontal links in the six-object diagram on scan 473 are described by their visible shape rather than assigned a confident direction.

The least trustworthy areas are the large cancelled block and small interlinear qualifications on scan 476; the oblique marginal note and layered cancellations on scan 477; the cancelled opening, initial primes, and retraced final symbol on scan 478; and the opening syntax, inserted formula, and unusual divided verb on scan 480. The deletion in that last formula is not recoverable from the supplied pixels. Scan 479's prose is clearer than its ornate group symbols.

The tables intentionally retain more doubt than a smooth reading edition would. They do not certify the exact historical alphabet of every group symbol or the precise order of every overwritten stroke. Apparent surprises such as « sous-groupes finis », incomplete clauses, a missing subscript or prime, and the final unfinished « de » have not been repaired from mathematical expectations. The research interpretations below remain separate from the transcription.

## 5. Research notes — English

These are manuscript-based research prompts, not a literature review or a claim that an idea is new. A statement is classified according to how it appears on these pages: a proposed or conditional result is not promoted to a proved theorem. References to §28 and to an unnamed Russian's result are left for source investigation because those sources were not supplied. The only bibliographic source used here is the supplied manuscript (Grothendieck, 1981), identified in the reference below.

Each item names its location and kind. Items labelled **own idea** give a confidence and reason; their proposed constructions or checks do not modify any reading in the transcription.


### R01

**Scan 472, approximately lines 8–12 — conjecture / desired result.** Grothendieck writes « on voudrait prouver qu'elle est compatible » for the map between the displayed sets of discrétifications, and then discusses arithmétisations and prédiscrétifications. The precise right-hand insertion is uncertain, so the intended equivalence relation must be checked before formulating a theorem. A proof would have to show that the construction is independent of representatives for that relation, not only that individual representatives can be sent across (Grothendieck, 1981, supplied scan 472).

### R02

**Scan 472, approximately lines 13–17 — conjecture / desired result.** The phrase « On voudrait établir » introduces injectivity of the displayed maps on oriented prédiscrétifications and arithmétisations. The page states this goal without completing the argument. The arrowhead in the A-display is pale, although the subsequent discussion supports treating the display as a map only at the interpretive level (Grothendieck, 1981, supplied scan 472).

### R03

**Scan 472, approximately lines 18–20 — unproved claim.** « on est ramené au cas où » introduces the reduction to a characteristic subgroup, with a reference to §28 and diagram 7. A proof requires checking both the existence of a suitable characteristic subgroup in the present category and that the desired compatibility and injectivity descend from the chosen reduction. The cited earlier section is outside the supplied batch (Grothendieck, 1981, supplied scan 472).

### R04

**Scan 473, approximately lines 4–9 — unproved claim.** The first circled assertion says the homomorphism « envoie M(π₀) dans M(π′₀) », after which a six-object diagram is written. The exact definitions of the groups and the homomorphism would be needed to verify this preservation statement and the diagram. The uncertain horizontal links and the overwritten lower middle object are transcription problems to resolve before treating the diagram as a formal proof (Grothendieck, 1981, supplied scan 473).

### R05

**Scan 473, approximately lines 10–16 — unproved claim.** « qui … implique » connects the diagram with independence of the induced prédiscrétification or arithmétisation under changing a discrétification. The claim appears to be a well-definedness step before the separate question of injectivity. A proof should identify precisely which orbit or equivalence relation each of the two group levels represents (Grothendieck, 1981, supplied scan 473).

### R06

**Scan 473, approximately lines 16–19 — unproved claim.** « l'injectivité, qui revient aux relations » introduces two subgroup-intersection identities, labelled (2). Their equivalence to injectivity is asserted rather than demonstrated on this page. One must check the embeddings and ambient group in which each intersection is being taken, especially because the manuscript maps cannot be silently replaced by inclusions (Grothendieck, 1981, supplied scan 473).

### R07

**Scan 473, final identities — own idea. Confidence: high for the conditional elementary argument, low for identifying the manuscript objects with it.** Once the relevant inclusions are established, test the manuscript's reduction against the coset map H/(H∩K) → G/K for H,K ≤ G. Equality of two image cosets means that the quotient of their H-representatives lies in H∩K, which proves injectivity in this conditional model. This supplies a check of the reduction's form; it does not supply the missing manuscript definitions or prove either displayed identity.

### R08

**Scans 472–473 — own idea. Confidence: medium.** Separate the proof obligations into preservation of the distinguished subgroup, well-definedness on equivalence classes, and injectivity after passage to those classes. This organization follows the order of the written claims and could prevent an unproved embedding from being used implicitly in the intersection formula. It is a proposed way to audit the argument, with no claim of novelty.

### R09

**Scan 474, lines 4–9; kind: unproved claim / conditional expectation.** The text says “est injectif,” then “Par construction ... c'est aussi surjectif,” and “l'hom. canonique (3) est bijectif,” under the preceding asserted hypothesis. A proof should separate the kernel/intersection assertion required for injectivity from the construction through the arithmetic group used for surjectivity, and should verify the exact source and target of the displayed quotients (Grothendieck, 1981, supplied scan 474).

### R10

**Scan 474, lines 10–13; kind: unproved claim / conditional expectation.** “on trouverait aussi une bijection” is stated for the sets displayed in (4), with compatibility “avec l'iso.” The conditional wording should be retained: the needed proof must establish both directions of the induced correspondence and its equivariance for the preceding quotient-group isomorphism; the written letter in (4) is P and has not been replaced on semantic grounds (Grothendieck, 1981, supplied scan 474).

### R11

**Scan 474, lines 14–16; kind: unproved claim.** The proposed extension to “un ... ouvert quelconque” is introduced by “s'étendrait aussitôt.” A proof would need an appropriate characteristic finite-index refinement and a check that the relevant construction descends or restricts independently of the chosen refinement; the abbreviated hypothesis before `car.` is uncertain (Grothendieck, 1981, supplied scan 474).

### R12

**Scan 474, lines 17–18; kind: unpursued implication.** The instruction to proceed by “correspondances,” qualified by the inserted “arithm. extérieures,” points back to §28 and continues onto the next page. A useful verification is to compare the actual correspondence data and their composition in that earlier section, without presuming definitions or coherence statements not present on this page (Grothendieck, 1981, supplied scan 474).

### R13

**Scan 475, lines 1–4; kind: unproved claim, within the preceding conditional construction.** The proposed correspondences give “un groupoïde connexe,” whose exterior fundamental group is the “valeur commune” of the displayed Γ-groups. Verification requires defining the relevant objects and arrows, proving connectedness, and distinguishing a common outer isomorphism class from a strictly canonical identification (Grothendieck, 1981, supplied scan 475).

### R14

**Scan 475, lines 5–13; kind: unproved claim / proposed construction.** He proposes to obtain an isomorphism by regarding both groups, after increasing the puncture parameters, as “sous-groupes finis du [m̄] π₀,₃.” The phrase is transcribed literally; a proof must establish precisely what subgroup condition is intended, construct the two realizations, and show that the induced comparison does not depend on their choices (Grothendieck, 1981, supplied scan 475).

### R15

**Scan 475, lines 14–18; kind: conjecture / question about independence of hypotheses.** “On aimerait maintenant voir ce qui ... est indépendant de notre conjecture” explicitly opens a separate problem about removing the conjectural input. The text then says “n'est pas établi” about the canonical maps between the Γ-groups; the sentence is compressed, so the transcription does not supply an unstated predicate such as bijectivity (Grothendieck, 1981, supplied scan 475).

### R16

**Scan 475, lines 19–21; kind: conjecture / conditional premise.** “si on savait que” introduces the displayed intersection equality for a characteristic subgroup situation, with a double-hatted first G-like symbol. This isolates a concrete group-theoretic assertion to investigate before the subsequent conclusions; the distinction between one and two hats must be settled from the manuscript's definitions (Grothendieck, 1981, supplied scan 475).

### R17

**Scan 475, lines 5–13; kind: own idea. Confidence: medium. Reason: the page proposes comparisons through a common auxiliary object but does not check their coherence here.** A useful diagnostic is to choose three curve types and two different common refinements, then compare the composite identifications around the resulting triangle up to inner automorphism. Failure of this test would expose a choice-dependence obstruction to the asserted canonical outer comparison; no claim is made that this obstruction occurs or that this test is new.

### R18

**Scan 476, lines 1–6; kind: conjecture / conditional consequence.** The preceding intersection premise is called “un énoncé de nature relativement anodin,” and he says “on conclurait à la bijectivité,” then to triviality of the image of the kernel of Γ_Q → Γ₀,₃ in the Γ-groups. The task is to prove the actual group-theoretic intersection assertion and track the induced quotient maps; the page does not license promoting the conditional conclusion to a proved statement (Grothendieck, 1981, supplied scan 476).

### R19

**Scan 476, lines 7–14; kind: unproved claim / conditional expectation.** He proposes that the action pass “par l'intermédiaire” of Γ₀,₃ and that the map be “iso” for “ν assez grand.” A verification must distinguish factorization from injectivity and identify the dependence of the required puncture count on the genus (Grothendieck, 1981, supplied scan 476).

### R20

**Scan 476, lines 10–13, canceled; kind: unproved claim in a canceled draft, not a standing assertion.** A crossed-out block proposes to “montrer au moins que l'image du noyau” is finite, with the final adjective read uncertainly as *finie*. Its cancellation should be preserved when studying the evolution of the argument: it records a weaker intermediate goal, not an additional established result (Grothendieck, 1981, supplied scan 476).

### R21

**Scan 476, lines 14–19; kind: unproved claim / proposed sufficient construction.** “il suffit que” introduces a realization as an étale cover, with ν′ ≤ ν and an inserted qualification about a structure “à lacets.” A proof must construct a compatible cover, verify the puncture inequality, and keep the additional loop data when passing to the finite-index subgroup (Grothendieck, 1981, supplied scan 476).

### R22

**Scan 476, lines 19–21; kind: unpursued implication / proof-sketch step.** The page ends by “considérant un” further subgroup, of finite index and characteristic in π₀,₃, and continues “on aura” on the next scan. The characteristic-refinement step should be checked against the inherited loop structure and against the later diagram; the ambiguous inclusion sign must not be used as independent evidence for a particular categorical relation (Grothendieck, 1981, supplied scan 476).

### R23

**Scan 476, lines 14–19; kind: own idea. Confidence: medium. Reason: the claimed cover has simultaneous genus, puncture and index constraints.** A first diagnostic would compute the Euler-characteristic index relation and the puncture-cycle data for explicit finite covers of the thrice-punctured base, then test how adding punctures changes the admissible cases. This could clarify whether the displayed inequality alone captures the needed hypothesis; it is a proposed check, not a result or a novelty claim.

### R24

**Scan 477, diagram and lines 1–5 — kind: unproved claim.** Grothendieck concludes that the maps `Γ_{0,ν} → Γ_{0,3}` for `ν≥3` are “alors bijectifs”. The word “alors” makes this a conclusion within the preceding argument, not an independently proved unconditional theorem on this page; a reconstruction must first identify the right vertical morphism in the opening diagram and the hypotheses under which the comparison is an isomorphism (Grothendieck, 1981, scan 477).

### R25

**Scan 477, lines 6–10 — kind: unpursued implication.** The explicit qualification “ceci ne dit rien” leaves open the faithfulness of the comparison with `Γ_{g,0}=Γ_g` for `g≥2` and with `Γ_{1,1}=Γ_1`. The page therefore distinguishes the puncture range `ν≥3` from the closed-curve and once-punctured genus-one cases; these cases should be tracked separately when comparing later manuscript arguments (Grothendieck, 1981, scan 477).

### R26

**Scan 477, lines 6–10 — kind: own idea.** An audit could compare the kernel before and after forgetting marked points, rather than assume that a statement established after adding punctures descends to the unpunctured case. **Confidence: medium**, because the explicitly retained restriction `ν≥3` signals precisely this gap, while the needed comparison maps and their kernels are not developed on this page.

### R27

**Scan 478, lines 1–2 — kind: unproved claim.** The emphatic “OPS que” introduces the assertion that, after enlarging the field and making additional holes, `U′` is an étale cover of `(U_{0,3})_K`. A proof would need a finite morphism with all unwanted ramification removed by the chosen punctures, together with control of the field over which the morphism and punctures are defined; the page gives the reduction rather than its construction (Grothendieck, 1981, scan 478).

### R28

**Scan 478, lines 5–9 — kind: unproved claim.** The image associated with the kernel in the exterior automorphism group of `π′` is said to be “un sous-groupe fini”, followed by corresponding finiteness statements in `Γ_{π′}`, `N(π)`, and `Γ_π`. Establishing this step requires tracking which subgroup is stabilized and which inner automorphisms become trivial after passing to the exterior automorphism group; the uncertain primes at the start of the argument should be settled before formalizing it (Grothendieck, 1981, scan 478).

### R29

**Scan 478, lines 5–9 — kind: own idea.** A useful group-theoretic calculation is to set `G=π̂_{0,3}` and `H=π′` and examine the map from `N_G(H)` to `Out(H)`, whose inner-conjugation image factors through `N_G(H)/(H C_G(H))`. If `H` is open, this quotient is finite, which could isolate the finite-image step once the action and stabilizer hypotheses have been checked. **Confidence: high for this conditional calculation**, because it follows from the definition of an inner automorphism and finite index; its applicability to every symbol in the manuscript remains to be verified.

### R30

**Scan 478, lines 9–13 — kind: unproved claim.** For the effective operation with a chosen rational base point, he writes that “il suffit d'appliquer le résultat précédent” to the punctured curve `U\{P}`, reading the uncertain short mark as set subtraction. A complete argument would specify the comparison between the outer action on the newly punctured curve and the based action on the original curve, including the compatibility of the chosen point with the field and subgroup actions (Grothendieck, 1981, scan 478).

### R31

**Scan 478, lines 13–15 — kind: unproved claim.** He concludes that the kernels of `Γ_{0,ν} → Γ_{0,3}` for `ν≥3` “sont finis”, with “finis” underlined. This is stronger than merely having finite image in individual targets, so a proof audit should identify the exact common quotient or uniformity statement that yields the finiteness of the kernel itself (Grothendieck, 1981, scan 478).

### R32

**Scan 478, lines 16–19 — kind: unproved claim.** “On voit facilement” precedes the claim that the operation of `Θ′` on `∏_ℓ T_ℓ(A)` factors through “un groupe quotient fini”. The product over all primes matters: a proof must provide a common finite quotient for the product action, not only a separate finite image at each prime (Grothendieck, 1981, scan 478).

### R33

**Scan 478, lines 20–22 — kind: conjecture.** The closing phrase “très difficile d'imaginer” expresses an expectation that the kernel should act “trivialement !”. This is an expectation motivated by the preceding finite-image conclusions, not a proof that the remaining finite obstruction is trivial; the sentence continues onto the next supplied page (Grothendieck, 1981, scan 478).

### R34

**Scan 478, lines 13–22 — kind: own idea.** Separate two possible residual gaps: obtaining one finite image from a family of finite images, and proving that this finite image is trivial. **Confidence: high as a logical distinction**, because inverse limits of finite groups may be infinite and a finite group may be nontrivial; neither observation alone determines whether Grothendieck's intended geometric hypotheses already close the gaps.

### R35

**Scan 479, lines 1–4 — conjecture / expectation.** Grothendieck says he has « l'impression que je peux montrer » that the displayed map from the Q-indexed Gamma group to the `(0,3)`-indexed Gamma group « est iso ! », invoking an unnamed Russian's result communicated by Deligne. This is a stated expectation, not a proof on this page; checking it would require identifying precisely the invoked result and the two directions of the proposed isomorphism without importing a later identification into the transcription. (Grothendieck, 1981, requested scan 479.)

### R36

**Scan 479, lines 4–11 — unpursued implication.** The conditional passage says that outer actions « peuvent s'interpréter » as splittings, at least for sufficiently large `ν` with `g` fixed, and distinguishes the extensions denoted by an N-like and an M-like letter when the actions are effective. A detailed argument would need to identify the two extension sequences, the relevant conjugacy equivalence on splittings, and the sense of effectiveness; the uncertain handwritten kernel alphabets should first be settled. (Grothendieck, 1981, requested scan 479.)

### R37

**Scan 479, lines 12–20 — conjecture / programmatic question.** The stated « question essentielle » is an algebraic description of the `(0,3)`-indexed Gamma group and the N-like groups, together with « une description algébrique » of the « scindages “admissibles” ». The final qualification requires these splittings to correspond to algebraic curves over fields of algebraic numbers, so an eventual criterion must explain the arithmetic realization condition as well as the group-theoretic splitting. The isomorphism with the Q-indexed group is explicitly admitted as a hypothesis here. (Grothendieck, 1981, requested scan 479.)

### R38

**Scan 480, lines 1–3 and insertion — conjecture / tentative criterion.** The legible condition includes « normalisent aucun » and « à lacets », followed by an inserted formula ending in `(1)`. The opening syntax and the relation in that formula are too damaged for a confident formal proposition; a research check should determine exactly which proposed exclusions or fixed-element condition Grothendieck intended before testing sufficiency. (Grothendieck, 1981, requested scan 480, ms. p. 243.)

### R39

**Scan 480, lines 4–6 — conjecture / expectation.** The parenthetical warning allows « des conditions plus subtiles », specifically « faisant intervenir les Frobenius ». This leaves an explicit problem of formulating additional arithmetic constraints and explaining why the preceding purely group-theoretic condition may fail to suffice. No particular Frobenius condition is formulated on these lines. (Grothendieck, 1981, requested scan 480, ms. p. 243.)

### R40

**Scan 480, lines 6–12 — conjecture / programmatic question.** « On peut se proposer de trouver » a description of admissible outer actions « sans avoir à passer par des actions effectives admissibles ». This asks for a condition stated intrinsically for outer actions, and the following appeal to a plausible definition emphasizes its provisional status. A proof would have to establish agreement with whichever arithmetic realization criterion is eventually adopted. (Grothendieck, 1981, requested scan 480, ms. p. 243.)

### R41

**Scan 480, lines 13–16 — unproved claim.** The difficulty is that an outer action on the displayed completed `(0,3)` group « n'opère pas extérieurement pour autant » on a given open subgroup. A proof must track the ambiguity in choosing representatives of an outer automorphism and then restricting them, even when a representative preserves the subgroup. The text states the obstruction but supplies no calculation on this page. (Grothendieck, 1981, requested scan 480, ms. p. 243.)

### R42

**Scan 480, lines 17–21 — unpursued implication.** The following step explicitly assumes that a suitable action « existe » and that the displayed inclusion/map « soit compatible avec les actions extérieures ». The additional condition on the action at the end is cut off after « de », so its completion cannot be inferred from this page. Further study should distinguish an assumed lifting or compatibility datum from a canonically induced outer action. (Grothendieck, 1981, requested scan 480, ms. p. 243.)

### R43

**Scan 480, lines 13–16 — own idea; confidence: high for the elementary test, not for its adequacy in the manuscript's setting.** Test the restriction ambiguity in the finite pair `C₃ ⊂ S₃`: conjugation by a transposition is inner on `S₃`, but takes a 3-cycle to its inverse and is therefore non-inner on the abelian subgroup `C₃`. This direct calculation makes the representative ambiguity concrete without assuming any specific property of the manuscript's profinite groups. It is proposed as a diagnostic example, with no claim of novelty.

### R44

**Scan 480, lines 13–21 — own idea; confidence: medium.** For an open subgroup `H` of a profinite group `P`, examine the residual outer action, namely the induced map `N_P(H)/H → Out(H)`, after choosing representatives that preserve `H`. The self-normalizing case `N_P(H)=H` is a useful first test for canonical restriction, because the remaining conjugations then restrict to inner automorphisms of `H`; continuity and the precise hypotheses for these manuscript groups would still need checking. The reason for this suggestion is the elementary representative ambiguity illustrated in the preceding item, not an asserted identification with a known theorem.

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished mathematical manuscript, cote 140-2, archive file “pages 1–292”; supplied images LM_P048_scan471.jpg–LM_P048_scan480.jpg, bearing archive footers 470–479 and visible upper manuscript numbers 238–243]. Université de Montpellier.
