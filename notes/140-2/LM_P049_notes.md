# LM_P049 — Transcription notes

## 1. Source, scope, and conventions

This file accompanies `LM_P049_transcription.tex`, a diplomatic working transcription of the ten supplied manuscript images. The transcription preserves French wording, abbreviations, cancellations, insertions, visible emphasis, and unresolved readings; mathematical interpretation is confined to section 5 below. No published transcription or outside mathematical account was used to supply missing text.

All manuscript references in these notes refer to **Grothendieck (1981)**, identified by the supplied filename's **scan number** and, where possible, an approximate handwritten line. The bibliographic identification comes from the attached task prompt; the images themselves supply the text and page-state evidence. Approximate lines count the main handwriting baselines from the top, excluding folio numbers and counting a displayed formula as a line; small additions are located by their host line.

The scan number is distinct from the lighter handwritten bottom-left numeral and the printed number beneath the image. The lower handwritten numerals are preserved using `\margin`; they are not attributed to Grothendieck's original foliation. Printed archive URLs and institutional footers are not transcribed as manuscript text.

| Filename scan | Upper manuscript folio visible | Lower-left numeral / printed footer |
|---|---|---|
| 481 | None visible | 480 |
| 482 | 244 | 481 |
| 483 | 245 | 482 |
| 484 | None visible | 483 |
| 485 | 246, possibly 245 | 484 |
| 486 | None visible | 485 |
| 487 | 247 | 486 |
| 488 | None visible | 487 |
| 489 | 248 | 488 |
| 490 | None visible | 489 |

A vertical bar inside `\unsure{reading|alternative}` separates competing readings; it is not a mathematical operator. Repeated notational doubts are grouped in the tables where indicated. Confidence is confidence in reading the ink, not in the truth of the mathematical statement. The counts in `\illegible{n}` are estimated word counts, including where a cancelled mathematical expression cannot be recovered.

The LaTeX file is intentionally a fragment: it has no preamble, document class, or definitions of the requested editorial macros. Its syntax was checked in a temporary wrapper with those macros and `tikz-cd`; that wrapper is not included. Different visible indices and numbers of hats have not been normalized to a single scheme.

## 2. Table of doubts
### Scans 481–482

Approximate line numbers count the main handwritten text lines from the top, excluding pagination and interlinear additions. The inserted words are attached to their host line. Confidence rates the proposed reading, not the mathematical claim.

| Scan | Approx. line | Proposed reading | Alternative or difficulty | Confidence |
|---|---:|---|---|---|
| 481 | 3, 4 | `\mathcal{N}_{g,\nu}`, `\mathcal{N}_a` | Plain `N`; the sweeping handwritten capital does not securely determine the alphabet. | medium |
| 481 | 3 | `une` | `un`; the terminal stroke is indistinct. | low |
| 481 | 4, cancelled above `relèvement` | `quand` | One deleted word; the cancellation makes this reading unreliable. | low |
| 481 | 4 | `en` | `un`, following `\Pi_a`. | low |
| 481 | 5 | `ssi` | The abbreviation is extremely compressed. | medium |
| 481 | 7 | `ss-groupe` | `ss groupe`; a p-descender and terminal e support the full word after `ss`, but the hyphen is insecure. | medium |
| 481 | 9 | `et` | The initial word is overwritten. | medium |
| 481 | 9, before `ouvert` | `\Gamma` | Tall isolated glyph, possibly a superseded letter or a word-initial stroke; no confident deletion boundary. | low |
| 481 | 10 | `action` | The word is reworked in dark ink; it is not clearly struck through as a whole. | medium |
| 481 | 10, beneath `de \Gamma''` | deleted `admissible` | Cancelled word under the line; the same word is more legibly inserted above. | low |
| 481 | 12 | `laisse` | Final strokes are faint; the reading is not supplied from the expected invariance condition. | medium |
| 481 | 13, insertion | `et le germe d'action de \Gamma' dessus` | The single prime is retained as seen; it is not changed to the nearby double prime. | medium |
| 481 | 15, insertion | `(et oubli d'une action effective au profit de l'action extérieure)` | `oubli` and the end of `extérieure` are crowded by the insertion connector and the next main line. | medium |
| 481 | 17, insertion | `algébriquement` | The small ending is uncertain. | medium |
| 481 | 20, cancellation | `\mathbb{Q}` | Heavily overwritten field symbol before `le corps`. | low |
| 481 | 20 | `U_{0,3}` | Doubled/overworked initial strokes make the alphabet uncertain. | medium |
| 482 | 4, 18 | `\mathcal{N}_{g,\nu}` | Plain `N`; same alphabet ambiguity as scan 481. | medium |
| 482 | 4 | `\Pi_{g,\nu}` | `\Gamma_{g,\nu}`; the upper-case letter is compressed. | low |
| 482 | 6 | `\widehat{\widehat{\mathcal{T}}}_{g,\nu}` | Initial script letter is overwritten; two separate caret-like strokes are visible over the letters in this formula. | medium |
| 482 | 6 | `\twoheadrightarrow` | `\longrightarrow`; a second apparent arrowhead may be a pen stroke. | low |
| 482 | 11–12 | `correspondant` | Word split across the original lines; the first part is faint. | medium |
| 482 | 13 | `décide` | `décrète`; enlarged reading suggests a dotted i and tall d, but the compressed middle remains uncertain. | medium |
| 482 | 13, cancellation | `\mathcal{T}_{03}` | Crossed-out symbol; its alphabet and subscript are insecure. | low |
| 482 | 15 | `commute` | The start is overwritten and the internal strokes are compressed; no alternative is secure. | low |
| 482 | 18, cancellation | `\widehat{\mathcal{T}}` | Scribbled symbol before the final `N`; hat and script letter are uncertain. | low |

### Scans 483–485

Approximate line numbers below count the main handwritten lines from the top of each scan, including the heading and mathematical display but excluding inserted lines. They are locators, not diplomatic line numbers. The lower left numerals 482, 483, 484 are preserved as marginal material; only the upper original folio is encoded with `\mspage`.

| Scan | Approx. line(s) | Reading retained | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 483 | 2 | `définies`; deleted `Q` | Ending of `définies` is compressed; the cancelled letter is densely overwritten. | medium / low |
| 483 | 3 | `\overline{\mathbb Q}_0/\mathbb Q` | The subscript is read as 0; preserved rather than silently replacing this by a more familiar field notation. | medium |
| 483 | 4, insertion | `(par commodité)` after `connexes` | Insertion line points between `connexes` and `anabéliennes`; attachment to the preceding adjective is the best visual reading. | medium |
| 483 | 5 | `!` after `provisoire` | Heavily retraced sign; possibly a cancelled punctuation mark. | low |
| 483 | 5–6 | `la façon`; `condition` | `restriction` is also possible for the latter; the compressed initial letters and two tall strokes do not resolve it securely. | medium / low |
| 483 | 7 | `universel`; one deleted word | The ending is a short stroke; the deleted word before `U` cannot be read. | medium / low |
| 483 | 9–11 | `\Gamma'` | `\Gamma^{+}`; alternatively some apparent superscript marks may be part of the heavy upper-right serif of the letter. | low |
| 483 | 10 | label `(2)` | `(1')`; later reference to `(1')` is itself unclear and has not been used to correct this label. | low |
| 483 | 10, parenthesis | `image`; `repéré` | Small crowded parenthesis; endings are not fully distinct. | medium |
| 483 | 13 | `Centre` | Cursive operator name before `(π)=1` is compressed. | medium |
| 483 | 16–17 | overwritten small sign after `les`; `\mathcal E` after `données` and `U` | First sign treated as a cancellation; the two latter E-like signs may also be alterations rather than intended mathematical symbols. They have not been silently removed. | low |
| 483 | 17 | `(1')` | `(2)` is also conceivable; the reference is indistinct. | low |
| 483 | 19 | `invariante` | Final letters are compressed. | medium |
| 483 | 20, 22–25 | `\Gamma'` or `\Gamma` | A right-hand serif can be mistaken for a prime; these occurrences remain explicitly doubtful. | low |
| 483 | 20 | `\Gamma^{\flat}` | `\Gamma^{\natural}`; the small superscript looks angular and 4-like. | low |
| 483 | left lower margin | `et tout sous-groupe ≠1 … unique L_i…` | Initial `et` is uncertain. The note has no unambiguous insertion pointer and is retained as a margin note. | medium |
| 483 | 22 | `dans π` inserted after `maximaux` | Pointer is clear, but its relation to the adjacent comma is less certain. | medium |
| 483 | 24 | cancelled `d'`, replaced with inserted `entre` | The cancelled character is crossed heavily; `entre` is legible. | low / high |
| 484 | 5–6 | `sera`; map letter `u` | Short cursive forms, especially the isolated map letter. | medium |
| 484 | 9, insertion | `(morphismes les applications dominantes)` | Tiny inserted text; the two last word endings are compressed. | medium |
| 484 | 15 | inserted `étales` | The final letters lie close to the insertion stroke. | medium |
| 484 | 16 | `[\widetilde U étant choisi]` | `étant choisi` remains uncertain; the mark on U is read as a tilde. | medium |
| 484 | 19 | inserted `can.` | The abbreviation is legible, but no expansion is inserted in the transcription. | medium |
| 484 | 20 | `sous-groupe` | `ss-groupe`; the middle letters are reduced to strokes. | low |
| 484 | 24–25 | selected `I` | Possibly `\overline I`; the large selected-set symbol has a heavy upper stroke, but an additional bar cannot be distinguished securely from its serif. Both the selection and the complement are marked. | low |
| 484 | 24, insertion | `2g+Card(I)≥3` | Operator letters in `Card` are overwritten. The inequality itself reads ≥, not ≤. | medium |
| 484 | 24, two insertions | `tel que …`, then `stable par Γ, et` | The first long insertion line terminates after the set expression; the second leads to the phrase `on “bouche…”`. Their attachment is retained without repairing punctuation. | medium |
| 484 | 8 | no underline on `signifierait` | The short low horizontal stroke appears continuous with the descending g rather than a separate emphasis line. | medium |
| 485 | upper folio | `246` | `245`; last digit is not fully closed, so no sequential-number inference is used to make it certain. | low |
| 485 | 2 | deleted `peut` | Crossed-out word is mostly erased. | low |
| 485 | 3 | underlined `courbe` | Word and long lower stroke are overwritten; possibly an insertion over an earlier reading. | low |
| 485 | 4 | `ponctuée` | This is the visible reading, not `pointée`; underlining retained. | high |
| 485 | 8 | `proviennent` | Overwriting at the beginning and compressed final letters. | medium |
| 485 | 9 | `rat/K` | No separate dot is securely visible after `rat`; not silently expanded. | medium |
| 485 | 11 | underlined `monomorphismes` | Initial syllables are compressed; cannot exclude a different compound ending in `-morphismes`. | medium |
| 485 | 14, 20 | one deleted word/sign at each position | Neither overwrite is readable. | low |
| 485 | 15, 21 | double-hatted calligraphic T | Two separate hats are visibly present; the alphabet of the large cursive base glyph is interpreted as `\mathcal T`. | high / medium |
| 485 | 16 | `\mathfrak S_3` | `\mathcal S_3`; the highly curved group letter does not securely distinguish the alphabet. | low |
| 485 | 16 | `moins sans espoir` | Unusual phrasing is retained with a doubt mark rather than rewritten. | medium |
| 485 | 18, 23, 25 | `authentisation`, `authentisés`, `authentisations` | No f descender is visible in the recurring word; do not silently substitute `authentification`. The first instance is divided over two manuscript lines. | medium |
| 485 | 19 | `explicité` | Final accent/ending is faint. | medium |
| 485 | 21 | `donc` | Thick compressed stroke after the dash. | medium |
| 485 | 21–22 | `N(π)` | `\mathcal N(π)`; cursive capital alphabet is not secure. | low |
| 485 | 22–23 | inserted `pour`; map `π′→π` placed with `hom` | The word insertion has a pointer; the map is placed below `un` at the right and is treated as an insertion identifying the homomorphism. | medium |
| 485 | 24 | `il` | Opening letters are retraced. | medium |

### Scans 486–488

| Scan | Approx. line | Reading retained | Alternatives / grounds of doubt | Confidence |
|---|---:|---|---|---|
| 486 | 1, 14, 17, 19–20 | `authentisation`, plural `authentisations` | Initially liable to be read as *authentification*. The recurring word lacks the conspicuous descending *f* found in nearby words; its compressed medial letters still warrant a doubt mark. | medium |
| 486 | 1–2 | `déduite`; `induite` | Endings and medial strokes are compressed; `induite` is not supplied merely from the expected mathematics. | medium |
| 486 | 3 | Deleted `L'intérêt` | The cancellation crosses most of the word; no secure alternative. | low |
| 486 | 4 | One cancelled word left illegible | Dense overwrite after `que` and before `non seulement`; estimated one word. | low |
| 486 | Between 5–6 | `\widehat{\mathcal T}(\pi)` | Script letter and accent are crowded into the insertion. The clearer formula on scan 487 has one caret over a script T, but the crowded occurrence itself remains marked. | medium |
| 486 | Between 5–6 | `tt` | Apparently an abbreviation before `sous-groupe`; no expansion is made in the transcription. | medium |
| 486 | 7, 10 | `\mathfrak S_3` | Rounded handwritten S-like glyph; exact alphabet is uncertain. | medium |
| 486 | 12 | `présume` | Final syllable is reduced to a short group of strokes. | medium |
| 486 | 15 | `hom` | No secure terminal dot or plural mark; retained without either. | medium |
| 486 | 17 | `automatiquement` | First portion of the word is faint and compressed. | medium |
| 486 | 20 | Deleted `Ici`, `comme`, and `\Pi_\pi =` | The entire line is crossed, with another condition inserted above it; precise ordering of the abandoned start is uncertain. | low |
| 486 | Above 20 | `si \Gamma=\Pi_{\mathbb Q},` | The subscript of the second group is overwritten; Q is the tentative reading. | low |
| 486 | 20–21 | A cancelled glyph after `de`; `est`; `décrite` | A glyph is unreadable. `est` appears replaced by the marginal insertion `doit être`; `décrite` is partly crossed. | low |
| 486 | 22–23 | `du fait qu'…`; `En fait, on va` | The replacement might read `on se`; abandoned words after `qu'` cannot be recovered. | low |
| 486 | 23 | `orient.` | The ending is abbreviated in the inserted text, unlike the preceding full `orientée`. | medium |
| 486 | 24 | Three illegible words and tentative `point de base` | This line is separately struck and also falls within the diagonally cancelled block; neither the word count nor the proposed phrase is secure. | low |
| 487 | 1 | `me` in `Je me pose` | The short word consists of very few strokes; `re` would change the reading to `Je repose`. | medium |
| 487 | 2 | Deleted `simple et`; inserted `simpliste` | `simple` is also possible for the inserted word. The ending looks longer than `-ple`, but the new word overlaps the cancellation. | low |
| 487 | 3 | One cancelled word | The initial overwritten word before `Ici` is not securely readable. | low |
| 487 | 4 | `fixe` | The medial crossing is faint. | medium |
| 487 | Between 4–5 | `et une authent.` | The abbreviation's ending is compressed; its expansion is not imposed in the text. | medium |
| 487 | 5 | `invariées` / `invariés` | Neither the number of medial/end strokes nor the accent is secure; no grammatical regularization is made. | low |
| 487 | 5 | Two cancelled words before `sorte que` | Estimated two words; cannot securely recover the cancelled formulation. | low |
| 487 | 6 | `injective` | Final strokes could disguise another nominal/verbal ending; the map is transcribed independently of the word. | medium |
| 487 | 7–8 | Cancelled words before `i.e.` and after `de` | One estimated word at each place, no secure reading. | low |
| 487 | 10 | `Soit`; two cancelled words before `si` | Initial word is overwritten; cancelled phrase cannot be read confidently. | medium / low |
| 487 | 11, 20 | Inserted `\Gamma^\natural`- | Angular superscript resembles a natural sign; exact sign remains uncertain. | medium |
| 487 | 12 | `déduit` | Terminal stroke could be misread as an additional letter; the singular reading is retained with doubt. | medium |
| 487 | 13 | Cancelled word plus `g\geq1` | The word before the visible inequality is overwritten. The subsequent live condition is `g=1`. | low |
| 487 | 13–14 | Cancelled `cette`, cancelled `bouchant`, inserted `en bouchant` | First cancellation is especially dense. The amendment's larger meaning is clear, but the original rejected words are not. | low |
| 487 | 17 | `\alpha=3`, with `\nu=3` as alternative | The left symbol has an alpha-like loop, retained as the first reading; a nu remains possible. The following condition is visibly a strict `\nu>3`, not `\nu\geq3`. | low for first symbol; high for strict inequality |
| 487 | 17–18 | `mettons`; one cancelled word before `partie` | Ending of `mettons` is compressed; cancelled word illegible. | medium / low |
| 487 | 19 | `de` / `dans` | Short final word before the next line's set difference is not secure. | low |
| 487 | 20, twice | `I\setminus I'` | The short separation mark is visibly oblique; a backslash is retained, still marked for the compressed notation. | medium |
| 487 | 20 | `du` / `de` before `\pi` | The final vowel is reduced to a stroke. | low |
| 487 | 24 | `relèvements` | The pale ending runs close to the right margin. | medium |
| 488 | 1–2 | `brutal`; `correspondent` | First word's final stroke and second word's long compressed ending are not completely secure. | medium |
| 488 | 3–4 | `pas`, twice | The author's p-and-short-strokes form is retained as a tentative reading; it may represent a scribal abbreviation rather than fully written letters. | medium |
| 488 | Above 8 | `germes de` | This is an insertion before `scindages`; the first word is compressed. It is not read as `géométrique`. | medium |
| 488 | Diagram, 10–11 | `\Pi_{\mathbb Q}`; `\wr` on upward arrow | Exact Q alphabet is uncertain. The upward arrow is clear; the adjacent curved isomorphism mark is rendered by `\wr` with doubt. | medium |
| 488 | 13 | `plutôt ici` | Dense initial lettering; no unambiguous separate cancellation is visible within the parenthesis. | medium |
| 488 | 14 | `M_{g,\nu\,\mathbb Q}` / `M_{g,\nu,\mathbb Q}` | The small moduli subscript is overwritten; punctuation and index grouping are not secure. | low |
| 488 | 20 | One cancelled word after `pour` | A small black overwrite before `une description`; estimated one word. | low |
| 488 | 22–24 | `travaillera`; `sous la` / `sur la`; `forme`; `constructive` | Final sentence is cramped against the lower border. The last quoted word appears to be `constructive`, but the lower strokes are the least secure part of this page. | medium for `travaillera`; low for final phrase |

### Scans 489–490

Line counts refer to main handwriting baselines from the top, excluding folio numbers and insertions; the final short line of scan 489 is line 24. Confidence is confidence in the proposed reading, not in the underlying mathematical assertion. Repeated uncertain symbols share one row.

| Scan | Approx. line | Reading in transcription | Alternatives / reason for doubt | Confidence |
|---|---:|---|---|---|
| 489 | 1 | `(gν)` | `(g,ν)`; a separating comma is not securely visible. | medium |
| 489 | 3 | `π_x` | The small subscript may be a different letter or a pen tail; `x` is plausible but not secure. | medium |
| 489 | 3 | `orientée` | Final ending is a compressed trailing stroke. | medium |
| 489 | 3–4 | `invariant` | `invariante`; no final *e* can be identified confidently at the start of line 4. Gender has not been silently corrected. | low |
| 489 | 4 | `!` after `bien sûr` | Closing parenthesis; the high curved stroke is ambiguous. | medium |
| 489 | 4–5 | `authentisation` | Split across the line boundary; no second *f* descender is visible. This spelling is retained rather than normalized to *authentification*. | medium |
| 489 | 5 | `va` | Very short compressed verb after `On`; the inserted barred *m* appears to attach here. | medium |
| 489; 490 | 489: 6, 9, 11, 14; 490: 3, 5, 11 | `Γ` with a natural-like superscript | Flat-like superscript; the repeated mark resembles an angular zigzag. The transcription preserves this as an explicit symbol doubt rather than assigning a technical meaning. | low |
| 489 | 6, insertion | `(relevant l'action ext. donnée)` | Attachment appears to precede `définir`; the extended connecting stroke is an insertion mark, not taken as ordinary underlining. | medium |
| 489 | 7 | `correspondante` | Compressed middle and ending. | medium |
| 489 | 8 | `remplacée`, `conjuguée` | Last letters and accents are faint; proposed feminine endings remain doubtful. | medium |
| 489 | 9, deletion | `l'action` | Crossing stroke prevents secure separation of the final letters. | low |
| 489 | 12, insertion | `pré-` before `discrétification` | A small connecting stroke may be a hyphen or part of the insertion sign. | medium |
| 489 | 16 | `1 → π′ → ℰ′ → Γ′ → 1` | Most arrowheads are very small; the rightward sequence is the visual reading. | medium |
| 489 | 17 | `π`/`Π` in the hatted `03` group and the intersection with the discrete `03` group | The small two-stem glyph is not securely distinct from uppercase Π. Both occurrences are explicitly marked, with lowercase preferred. | medium |
| 489 | 16–18 | Subscripts `03` | No comma is securely distinguished between the digits in these occurrences; no comma is supplied. | medium |
| 489 | 20–21 | `i ∈ I′ ⊂ I(π′)`; `en I′` | The latter has been retained literally; no complement sign is securely visible and none has been supplied from context. | medium |
| 489 | 21–22, insertion/deletion | `d'où π, une` replacing `et on regarde`, with `action ext.` cancelled inside the insertion | The insertion lies above the cancelled baseline phrase; it is attached at that replacement point. | medium |
| 489 | 23–24 | `grâce à i. On trouve bien ainsi une` | `grâce` reaches the right edge and the last line is close to the lower frame, but the continuation is readable. | medium |
| 490 | 1, insertion | `— une discrétification or.` | The leading dash is short; the long line beneath the insertion serves as its placement marker. | medium |
| 490 | 2 | `ont` | The compressed word could not be resolved into separate letters. | low |
| 490 | 3 | `autom.` | `autos`; the final compressed strokes and presence of a period are uncertain. The abbreviation is not expanded. | low |
| 490 | 3 | `transforment` | Final plural ending is a fast terminal stroke. | medium |
| 490 | 6 | `classes` | Compressed *-sses*; context alone is not treated as sufficient certainty. | medium |
| 490 | 6 | `font` | `forment`; middle strokes are reduced. | low |
| 490 | 7 | `bitorseur` | Several middle letters are compressed. | medium |
| 490 | 8, deletion | Two illegible words | The cancellation is too heavy to support a secure reading; the count is approximate. | low |
| 490 | 9 | `prend en masse` | Entire phrase remains uncertain; `joint` is also visually possible for the first verb. | low |
| 490 | 12 | `connexe` (underlined) | Underline is clear, word ending less secure. Only one underline is seen. | medium |
| 490 | 13 | `fera` | Short word after `On`; possible `fait`, but not enough distinct letters. | low |

## 3. Abbreviations encountered

These expansions are interpretive and appear only here. They are not substituted for the written forms in the transcription. A form marked uncertain in the transcription remains uncertain in this list.

| Form as written | Suggested expansion or function | Location / qualification |
|---|---|---|
| `ssi` | si et seulement si | Scan 481; reading uncertain. |
| `ss-` / `ss` before `groupe` | sous | Scan 481; the presence of the hyphen is uncertain. |
| `sous-gr.` | sous-groupe | Scan 483. |
| `ss-groupe`, `ss-groupes` | sous-groupe, sous-groupes | Scans 483–484 and 489. |
| `ext.`, `ext`, `(ext)` | extérieur, extérieure, extérieurs, or extérieures | Depends on the noun; punctuation is preserved locally. |
| `ext` with raised `t` | extérieurement | Scan 482. |
| `op.` | opération | Scans 484 and 489. |
| `op. ext.` | opération extérieure | Scan 486, cancelled passage. |
| `isom`, `isom.` | isomorphisme | Scans 481 and 489 respectively. |
| `pts` | points | Scans 481, 487, 489–490; quotation marks are retained where written. |
| `pt` | point | Scan 485. |
| `rat.`, `rat` | rationnel(s) | Scans 481 and 485; the latter occurs before `/K` without a securely visible dot. |
| `\overline{\mathrm m}` | même | Scans 482 and 489–490; includes the form after `lui-`. |
| `hom` | homomorphisme(s) | Several pages; no terminal dot or plural ending is added. |
| `alg.` | algébrique(s) | Scans 482–483 and 488. |
| `rev.` | revêtement(s) | Scans 482–484. |
| `géom.` | géométriquement | Scan 483, modifying `connexes`. |
| `cf` | confer / compare | Scan 483; no point is securely visible. |
| `i.e.` | id est | Scans 483, 485, 487–488. |
| `can.` | canonique | Scan 484, insertion. |
| `conj.` | conjugaison | Scan 485. |
| `NB` | nota bene | Scans 485 and 487. |
| `Norm` | normalisateur | Scan 483; mathematical operator. |
| `Card` | cardinal | Scan 484; operator reading uncertain. |
| `card` | cardinal | Scan 487. |
| `autom.` / `autos` | automorphismes | Scan 486 and the uncertain abbreviation on scan 490. |
| `tt` | tout | Scan 486, inserted centralizer remark; reading uncertain. |
| `authent.` | authentisation | Scan 487; proposed expansion inherits the uncertainty in the recurring full word. |
| `orient.` | orientée | Scan 486, cancelled passage. |
| `or.` | orientée | Scans 489–490, with discrétification / prédiscrétification. |
| `prédiscr.` | prédiscrétification | Scan 489. |
| `ens.` | ensemble | Scan 490. |

## 4. Legibility and limits

Most main-line prose is recoverable, but compressed endings, brief function words, mathematical alphabets, and corrections require more caution. The least trustworthy areas are the cancellations and interlinear additions on scan 481; the transition arrow and overwritten verb on scan 482; the crowded parenthesis and altered signs on scan 483; the intertwined set-selection insertions at the foot of scan 484; the superscripts and group-letter alphabets on scan 485; the extensively cancelled lower paragraph of scan 486; the revisions to the proposed criterion on scan 487; and the moduli subscript and cramped final sentence on scan 488. On scans 489–490 the repeated Γ superscript, the small subscript after π, and several short verbs remain uncertain.

The recurring spelling provisionally read as **authentisation** has not been modernized to *authentification*. The unusual phrase **moins sans espoir** is likewise retained under doubt. Some letters resembling bars or extra hats cannot be distinguished securely from serifs or overwriting; those local uncertainties remain visible. No accuracy percentage is claimed. The cancelled lower passage on scan 486 is transcribed as a cancelled draft, not as an endorsed conclusion. The large blank area at the end of scan 490 contains no omitted manuscript paragraph.

## 5. Research notes — English, separate from the transcription

These notes distinguish the author's conjectures, questions, expectations, unsupported assertions, and deferred work from implications and ideas proposed here. Brief quotations inherit any uncertainty recorded in the diplomatic text. A proposed proof obligation or test is not a theorem, an attribution of an error, or a claim of novelty. Definitions and arguments may occur elsewhere in the manuscript; none has been silently imported into these pages.


### Scans 481–482 (Grothendieck, 1981)

#### R481.1 — Scan 481, approximately lines 16–21, continued on scan 482, line 1

**Kind: conjecture / question.** The text says that one must “préciser … action ‘admissible’” and then “On peut conjecturer”, with a continuation about “bouchage des trous”. The open task is to make precise the proposed recognition of effective actions associated with rational points of the three-punctured curve over the field determined by the indicated subgroup. A proof would need an exact definition of admissibility and a careful comparison of effective actions, their conjugacy classes, and the exterior actions obtained by forgetting the effective lifting; the cramped insertion should not be used to assert a stronger correspondence than the text supports.

#### R482.1 — Scan 482, approximately lines 2–6

**Kind: conjecture / expectation.** “Il semble qu'on puisse … donner une description” proposes describing the groups denoted by `N` in terms of the group with subscript `0,3`. The page invokes transition homomorphisms but does not prove that the resulting description determines the desired groups or is independent of the choices. The precise script letters and completion marks remain a transcription issue, separate from this mathematical question.

#### R482.2 — Scan 482, approximately lines 7–10

**Kind: unproved claim.** For fixed genus the author asks for puncture numbers “assez grands pour qu'il existe une courbe” admitting the stated étale covering of `U_{0,3}` over `Q`. A proof would need to construct covers with the required genus and to track their punctures and field of definition. The wording on these pages should not silently be strengthened to “every sufficiently large puncture number”; whether a cofinal family suffices is itself worth checking.

#### R482.3 — Scan 482, approximately lines 11–18

**Kind: unproved claim.** The final paragraph proposes that, under the stated compatibility of exterior actions, “le sous groupe … engendré” is the group written `N_{g,ν}`. To justify this identification one would need to define the ambient groups and the lift of the arithmetic group precisely, prove both inclusions, and show that the outcome does not depend on the chosen covering and embedding. The uncertain verb after the displayed homomorphism is a material limitation on how precisely the hypothesis can be restated.

#### R482.4 — Scans 481–482, the covering and hole-filling construction

**Kind: own idea. Confidence: medium. Reason:** the proposed description explicitly passes between a covering, an embedding, and transition maps. Compare two admissible covering presentations after a common refinement, then check whether the proposed generated subgroups have the same image under the relevant transition homomorphisms. This is a possible test of choice-independence, not a claim that such a refinement argument works or is new.

#### R481.2 — Scan 481, the rational-point interpretation near the end

**Kind: own idea. Confidence: low. Reason:** the precise meaning of admissibility is still requested on the page. If the intended class of liftings includes boundary or tangential constructions, compare them with liftings from ordinary rational points using their action on the peripheral subgroups. Such a comparison could test whether the proposed recognition criterion distinguishes the required types of points; the inclusion of those constructions in the author's domain is not established here.

### Scans 483–485 (Grothendieck, 1981)

1. **Scan 483, approximately lines 15–20 — Conjecture / question.** Grothendieck asks whether one must include the peripheral or “lacet” structure among the data describing the curve, and answers under `Conjecture`: “Ce n'est pas la peine.” The stated expectation is that the given outer action determines a unique invariant lacet structure. A proof would have to establish this intrinsic recovery, not merely the invariance of an already supplied geometric family.

2. **Scan 483, approximately lines 21–23 and the left margin — Conjecture.** The proposed description uses maximal subgroups whose normalizers in the extension have open image in the arithmetic quotient: “comme image un ss-groupe ouvert.” The margin also proposes containment in a unique L_i for a nontrivial subgroup with the property. The precise allowed class of subgroups needs checking against definitions outside these pages before this criterion is stated as a theorem.

3. **Scan 483, approximately lines 21–23 — Own idea. Confidence: high as a formal diagnostic, conditional on the reading.** Test the normalizer condition against the whole geometric group π: in an extension with kernel π, its normalizer is the entire extension, so the normalizer’s image in the quotient is open. The displayed condition alone would therefore not isolate peripheral groups unless further restrictions on admissible subgroups are understood. This is a question about the scope of the written criterion, not a correction to it and not a claim that Grothendieck overlooked definitions supplied elsewhere.

4. **Scan 483, approximately line 24, continuing on scan 484, lines 1–3 — Conjecture.** “Je présume aussi que tout hom” introduces an expectation that homomorphisms of the indicated extensions with open image preserve the lacet structure and arise from a unique homomorphism of algebraic curves. The uniqueness is described parenthetically as already known (“unique, on le sait”), but no proof of either preservation or existence is given here. A proof would need a precise category of extension homomorphisms and the correct equivalence by inner conjugacy.

5. **Scan 484, approximately lines 4–7 — Unproved claim.** Conditional on the normalizer description, he says “il sera clair” that a lacet group maps either to (1) or into a unique L′_j. This needs a functorial argument for the normalizer’s open-image property and a separate uniqueness argument for the target peripheral subgroup. The conditional wording matters: this passage does not independently establish the initial description.

6. **Scan 484, approximately lines 8–14 — Unpursued implication.** “Ceci signifierait” relates the preceding conjecture to full faithfulness of the curve-to-outer-action functor, with dominant applications specified in an insertion. Base-field extension is then associated with restriction from Γ to an open subgroup Γ′. A fuller treatment should verify that this restriction is compatible with the particular notion of morphism and with the conjugacy ambiguities of outer actions.

7. **Scan 484, approximately lines 15–16 — Unproved claim.** “Les rev. … finis de U correspondent aux E-ensembles” invokes a correspondence between finite étale covers and sets acted on by the extension. The inserted `étales` and the bracketed choice of the universal covering object are relevant to a precise formulation. One would need to state the continuity and finiteness conditions on the E-sets; those conditions should not be inserted into the transcription simply because the correspondence is recognizable.

8. **Scan 484, approximately lines 17–25 — Unproved claim.** For the essential image, he asserts “on n'est pas réduit aux conjectures” and describes an open subgroup of the extension associated with the (0,3) case, followed by the operation “bouche les trous.” The written insertions impose a Γ-stability condition on a chosen subset of lacets and a numerical inequality provisionally read as 2g+Card(I)≥3. A proof of this characterization would need both descent of the action through the filling operation and exhaustivity of the construction for the intended curves.

9. **Scan 485, approximately lines 1–11 — Conjecture / question.** The discussion distinguishes an admissible effective lift from a claim that all conjugacy classes of admissible lifts come from rational points: “Ceci ne signifie pas pour autant.” He then expects the latter assertion to follow from full faithfulness for the morphisms provisionally read as `monomorphismes`. The relationship among these formulations should be established without silently identifying an abstract lift with a rational point.

10. **Scan 484, approximately line 9, and scan 485, approximately line 11 — Own idea. Confidence: medium.** Check the ambient category when using the final full-faithfulness assertion to discuss rational points: the earlier insertion restricts curve morphisms to dominant applications, whereas the later line invokes monomorphisms. These may concern different categories or an enlargement explained elsewhere. The apparent change of scope is visible, but these pages alone do not settle its intended resolution.

11. **Scan 485, approximately lines 12–16 — Conjecture / question.** Even for the automorphisms of U_(0,3), the author says the claimed full faithfulness “n'est pas du tout claire” and that “Il faudrait prouver” a specific commutant assertion. The proposed commutant is the group with subscript 3 provisionally transcribed as a Gothic S, inside the visibly double-hatted Teichmüller-type group. The excerpt gives a target reduction, not a proof of the commutant calculation.

12. **Scan 485, approximately lines 15–16 — Own idea. Confidence: medium.** One could test the proposed commutant statement on finite quotients compatible with the relevant action and boundary data. Such tests might reveal additional centralizing candidates or clarify which structural hypotheses are necessary. Agreement at finitely many levels would not prove the profinite equality, since compatible inverse-system behavior would still need to be controlled.

13. **Scan 485, approximately lines 17–25 — Unpursued implication.** The text makes the situation “moins sans espoir” by adding the structure provisionally read as an `authentisation`, invariant under Γ, and demanding that homomorphisms be compatible with it. A careful analysis should determine how much information this additional structure supplies beyond the outer action and the lacet structure, and whether compatibility can itself be recognized intrinsically. The page breaks before the full image/quotient compatibility condition is completed, so this item must be checked against the next scan.

### Scans 486–488 (Grothendieck, 1981)

#### 486-R1 — Scan 486, lines 1–6 — Unpursued implication

The convention `il est sous-entendu` strengthens the requirement on external automorphisms: commuting with Γ is accompanied by membership in N(π), while the preceding sentence requires compatibility with `passage au quotient`. A useful question is whether these requirements constitute independent structure or follow from the outer action once “authentisation” (the tentative spelling) is fixed. These lines state the convention but do not themselves establish redundancy.

#### 486-R2 — Scan 486, insertion between lines 5–6 — Unproved claim

The inserted justification ends with the claim that the centralizer of an open subgroup of Ππ `est (1) !`. A proof needs a precise identification of the ambient Ππ and the class of open subgroups involved before one can infer the stated restriction on automorphisms. The small script-group symbol in the same insertion remains palaeographically uncertain.

#### 486-R3 — Scan 486, lines 7–10 — Unproved claim

The decomposition written as N₀,₃ ≃ S₃ × Π₀,₃, together with `le centre … est trivial`, leads to the assertion that the automorphism group of the structure reduces to the displayed S₃-like group. Checking this argument requires tracking which automorphisms preserve the additional structure and how the centralizer calculation is used. The alphabet of the S₃-like glyph is uncertain in the transcription; no identification beyond what the page supports is imposed here.

#### 486-R4 — Scan 486, lines 11–14 — Conjecture

The phrase `on présume` introduces the expectation of a unique Γ-invariant “authentisation” for a given outer action. The page offers no construction proving existence or comparison proving uniqueness. Establishing this would determine whether the extra datum can be recovered intrinsically from the action.

#### 486-R5 — Scan 486, lines 14–19 — Conjecture

The same expectation includes the assertion that admissible homomorphisms of admissible external Γ-groups preserve the extra datum automatically. Grothendieck explicitly allows the opposite outcome: one would then have to `introduire les authentisations dans la structure` (the spelling remains uncertain). A proof must address morphisms as well as the uniqueness question for objects.

#### 486-R6 — Scan 486, cancelled lines 20–26 — Unpursued implication

The cancelled draft tries to relate the extra datum to a `prédiscrétification orientée` and an admissible lift of the given outer operation. Because the whole passage is cancelled and its revisions are not fully legible, it is evidence of an attempted route, not an endorsed assertion on this page. The potential relationship between an oriented discrete model and the “authentisation” deserves examination without repairing the abandoned text.

#### 487-R1 — Scan 487, lines 1–9 — Conjecture

The question is to `trouver une description` of admissible outer actions, starting from the chosen loop structure and added datum and interpreting Γ as a partial splitting, or `germe de scindage`, of the displayed extension. A precise formulation must specify equivalence of such germs, including restriction to open subgroups and any permitted conjugation. These conventions affect the later use of “points” and their distinctness.

#### 487-R2 — Scan 487, lines 10–15 — Conjecture

For positive genus, `le critère le plus simple` is presented in terms of distinct Γ-type points after all holes have been filled. The parenthetical g=1 case acknowledges that the resulting case is abelian and says `ça ne fait rien`, without giving a proof of why the proposed criterion remains adequate. Both the meaning of the marked points in that case and sufficiency of their distinctness remain to be justified.

#### 487-R3 — Scan 487, lines 16–21 — Conjecture

For genus zero the draft says `il n'y a pas de condition` in the apparent three-puncture case, then singles out a three-element subset I′ when ν>3 and imposes distinctness after filling the other holes. The first numeral condition's left symbol is uncertain in the transcription; its apparent ν-reading should be checked before formalizing the statement. A proof would also need to show that the proposed condition does not depend on the chosen three-element subset in an unintended way.

#### 487-R4 — Scan 487, lines 22–24 — Unpursued implication

In the explicitly `conjecturale` viewpoint, the boundary types (g,0) with g≥2, (1,1), and (0,3) carry `aucune condition a priori` on lifts. This is a strong consequence of the proposed simplification, not a theorem established here. Scan 488 immediately questions whether such unrestricted lifts might fail to be geometric.

#### 488-R1 — Scan 488, lines 1–5 — Conjecture

Grothendieck raises the possibility of lifts which fail to correspond to an algebraic curve and therefore are not admissible, `même s'ils le paraissent`. This is an explicit doubt about the preceding proposed criterion. A candidate sufficiency argument must therefore distinguish genuine geometric realization from merely satisfying its formal distinctness conditions.

#### 488-R2 — Scan 488, lines 6–16 — Conjecture

The proposed way forward interprets admissible germs of splittings as corresponding `aux points algébriques` of a moduli object, described as a variety with a parenthetical preference for a “multiplicité.” The page identifies N as its arithmetic fundamental group and the hatted script group as its geometric fundamental group, but does not supply the moduli construction or prove the correspondence. Establishing this route requires specifying that moduli object, the role of automorphisms of represented objects, and the equivalence relation on splitting germs.

#### 488-R3 — Scan 488, lines 17–24 — Conjecture

The intention `J'aimerais examiner cette situation de plus près` defers the moduli interpretation, while the warning against `conjectures hâtives` defers a direct description of admissible outer operations. The final cramped sentence appears to retain the construction via U₀₃ for the time being. The exact final adjective is uncertain, so that reading should not bear interpretive weight beyond the clearly stated contrast between direct description and the route via U₀₃.

#### 487/488-R4 — Scans 487–488 — Own idea

Try the first genus-zero case beyond three punctures: choose a three-element I′ and track the remaining Γ-type point after filling the fourth hole. Compare the proposed distinctness criterion with the route via U₀₃, explicitly keeping the equivalence of splitting germs and any stabilizers. **Confidence: medium as a useful test, not as a counterexample**, because it is the smallest case to which the new condition applies and the following page already warns that formal admissibility may be insufficient.

#### 486/488-R5 — Scans 486 and 488 — Own idea

Keep separate an object-level uniqueness problem for the extra datum and a morphism-level preservation problem, then ask whether a moduli interpretation resolves one without the other. A comparison groupoid of choices and their admissible isomorphisms could make that distinction precise. **Confidence: medium as a way to organize the problem**, because the manuscript explicitly states both expectations but provides neither a proof nor a reason that one implies the other.

### Scans 489–490 (Grothendieck, 1981)

These notes are separate from the diplomatic transcription. Source labels use the filename scan numbers, not the archive footer numbers; quotations reproduce the reading accepted here and may inherit explicitly noted transcription uncertainty. No assertion below is offered as a verified theorem or as a claim of novelty.

1. **Scan 489, lines 1–5 — conjecture / expectation.** The phrase “on prévoit qu'il y aura une prédiscrétification” presents a canonical oriented pre-discretification for an admissible outer action as an expectation. A proof would need an intrinsic characterization of the proposed structure from the outer action, together with a careful distinction between invariance of a chosen discrete realization and invariance of its associated “authentisation.” The parenthetical qualification about non-invariance must be checked against earlier definitions before formulating a theorem.

2. **Scan 489, lines 5–13 — unproved claim.** In “toutes ces discrétifications or. … définissent une … prédiscrétification orientée,” different effective lifts and points of the indicated B-object are asserted to produce one oriented pre-discretification, further qualified as “stricte.” Establishing this requires a comparison of lifts under conjugation and an explanation of why the equivalence relation used for pre-discretifications identifies every resulting oriented discrete subgroup. The full significance of “stricte” remains dependent on definitions outside these two pages.

3. **Scan 489, lines 14–18 — unproved claim.** “L'action effective … peut s'obtenir … en prenant un sous-groupe … ouvert” proposes a construction from an open subgroup of the displayed extension for the type-(0,3) object. A proof would have to justify that every intended admissible effective action is recovered, including the passage from the subgroup to its geometric kernel and the displayed equality between the profinite kernel and a completion of its discrete intersection.

4. **Scan 489, lines 18–24 — unproved claim.** The construction makes the action on the indicated I-set trivial after replacing Γ′ by an open subgroup, chooses an element i, and says the resulting outer action “est relevée en une action effective grâce à i.” One should isolate the group-theoretic mechanism by which this chosen element supplies a lift, and check its dependence on the preceding filling operation. The transcription's `en I′` is not silently changed to a complementary set in order to make a guessed argument work.

5. **Scan 490, lines 1–4 — unproved claim.** “Je dis qu'elle ne dépend pas des choix” asserts independence of the oriented discretification from the choices in the preceding construction. The following automorphism statement is a particularly concrete test: the specified automorphisms should preserve the resulting π₀ inside π. It would be useful to list separately the choices of open subgroup, lift, distinguished element and filled holes, and verify independence for each allowed change.

6. **Scan 490, lines 5–12 — unproved claim.** Among paths between two points, the manuscript singles out those whose associated isomorphism sends π₀(x) into π₀(y), then assembles a subgroupoid described as “connexe à lacets.” A proof must address existence of such paths for every object pair, stability under composition and inversion, and the compatibility of the retained loop structure. In particular, the written inclusion into π₀(y) should not be replaced by equality without an argument.

7. **Scan 490, lines 13–15 — unpursued implication.** The explicit warning that Γ “n'opère pas” on this groupoid although it acts on “l'ens. de ses objets” separates symmetry of the object set from preservation of the chosen arrows. This raises a precise functoriality question: which part of the discretified structure is transported by Γ, and which part only survives after passing to an equivalence class or to a larger ambient groupoid? These pages do not supply that comparison.

8. **Scans 489–490 — own idea; confidence: medium.** To test choice-independence, organize all allowed constructions of the same outer action as objects of a comparison category, with elementary changes of lift, subgroup and puncture data as arrows. If every elementary change preserves the claimed pre-discretification and all choices can be connected through such changes, the global claim may reduce to explicit local checks. Confidence is medium because this follows the manuscript's list of choices, but connectedness of that comparison category is itself an additional task.

9. **Scan 490, lines 5–15 — own idea; confidence: low.** A possible test of the final Γ-warning is to construct a small example in the type-(0,3) setting and compare Γ-translates of the selected path subset inside the ambient profinite path torsor. Failure of stability could reveal exactly which choice of oriented discrete realization prevents an action on the subgroupoid. Confidence is low because the requisite definitions of admissibility and pre-discretification are not fully given on these two pages.

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished handwritten manuscript; Montpellier archive, cote 140-2, file described as “pages 1–292”; supplied scans 481–490]. Université de Montpellier.

The author, year, title, cote, and file description follow the supplied task metadata. The transcription and local readings are based on the attached images; the broader archive identification has not been independently verified.
