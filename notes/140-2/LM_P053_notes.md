# LM_P053 — Transcription notes

## 1. Source, scope, and conventions

The transcription covers all ten supplied manuscript images, **scans 521–530**, in their given order. Their archive page labels are 520–529. The author's separate folio numbers **266, 267, 268, 269, and 270** are visible on scans 521, 523, 525, 527, and 529 respectively; no number in that series has been supplied on the intervening pages. Archive footer text and the later lower-left foliation are not treated as manuscript prose.

The French LaTeX fragment is a diplomatic reading of these images. It preserves explicit uncertainty, visible revision layers, nonuniform indices and superscripts, and apparently incomplete or surprising expressions. It neither completes the opening or closing passage nor reconciles the mathematics. Page joins that continue a sentence remain continuations. No published transcription, later manuscript page, or external literature was used to supply a reading.

The fragment has no preamble and uses the requested editorial macros, standard mathematical LaTeX, and `tikz-cd`. A host document must define those editorial macros and provide the mathematical packages. Temporary wrapper definitions were used only to check LaTeX syntax; neither the wrapper nor its PDF is included. In diagrams, `ampersand replacement=\&` makes the `tikz-cd` body safe inside the argument of `\diagram`.

## 2. Table of doubts

Locations refer approximately to physical handwritten lines from the top, with display rows counted where useful; marginal notes are located separately. Because mathematical annotations occupy several levels, equation numbers and descriptive loci are often more reliable than a bare line number. **Confidence concerns the reading of the ink, not the validity of the mathematics.** “High” includes clear source peculiarities deliberately retained; “medium” indicates a probable reading with unresolved strokes; “low” indicates substantial ambiguity. Word counts in illegible and cancelled spans are estimates. Related occurrences are sometimes grouped in one row.

| Scan | Approximate line or location | Reading in the transcription | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 521–523 | Recurrent group symbol in (32)–(35) | `\unsure{\mathfrak S}_3` | A very cursive S; calligraphic rather than Gothic S remains possible. The letter's font cannot be established as securely as the subscript 3. | medium |
| 521–523 | Recurrent extension and Teichmüller symbols | `\mathcal E`, `\mathcal T` | These are the chosen LaTeX equivalents of the visibly cursive capitals, not evidence of a particular printed font. E versus an epsilon-like hand and the exact calligraphic shape of T should be checked against a wider autograph sample. | medium |
| 521–523 | Recurrent linear-group abbreviation | `Sl` | Second letter has a looped lower-case-l shape; `SL` is an alternative typographical interpretation. No capitalization has been inferred from conventional notation. | medium |
| 521 | l. 1, above “d'indice” | inserted `ouvert` plus one illegible word/sign | The short material to the right may be a continuation or a correction/attachment stroke, rather than an additional lexical word; word-count 1 is deliberately provisional. | low |
| 521 | l. 4, before (32) | `iso` + cancelled illegible prefix + `morphisme` | Revision of the prefix is clear, but the original prefix is not. “homo” is a possible cancelled reading and is not supplied in the fragment. | low |
| 521 | (32), T subscripts | upper `1,1`; lower `11` | An independent enlarged-image audit recovered a clear comma in the upper kernel's subscript; no secure comma is visible in the lower kernel's subscript. The difference is retained. | high |
| 521 | l. 14 | `trivialement` | Final contracted strokes could represent an abbreviated ending. | medium |
| 521 | l. 16, after “loin de” | `22` or `??` | Two small curved signs; their status as a reference number or question marks is unresolved. | low |
| 521 | l. 17 | `(27)` | Second digit is read as 7 but is very compressed. | medium |
| 521 | l. 19 | `non` | Overworked short word before “dans”; not confidently a cancellation. | medium |
| 521 | l. 21 | `revienne` | Beginning and ending are reduced to connected strokes. | medium |
| 522 | ll. 1–2, word split across lines | `compatible` | An independent reading favors “com-patible”: the second-line initial has a p-like descender. “convenable” and “raisonnable” were also considered; the word remains doubtful and its unusual construction with “à” is not corrected. | low |
| 522 | l. 2 | `(27)` | Compressed second digit, as on the preceding page. | medium |
| 522 | l. 2 | `extension` | Middle strokes and final ending are compressed. | medium |
| 522 | l. 7 | `analytique` or `topologique` | The beginning is overworked; neither a silent correction nor a reconstructed earlier word is supplied. | low |
| 522 | (34), identification under T | `Sl(2,Z/2Z)/±1` | Both Z-shaped characters and the intervening /2 appear in the ink. This is retained despite the different identification under T in (35); the discrepancy is not repaired. | high |
| 522 | (35), terminal punctuation | `,)` or `.,` | Two separate marks appear after 1: a small dot/comma and a larger curved stroke. Both are preserved; their exact identification is uncertain. | low |
| 522 | l. 15, cancelled word above “On” | `qui` | Cancellation crosses most of the letters. | medium |
| 522 | l. 16 | `aux` | Overwritten short linking word before “suites exactes”. | medium |
| 522 | l. 17 | diagramme `(9)` | The digit might be 3; its descending shape favors 9. | medium |
| 522 | l. 19, between two group symbols | `à` or `:` | Two tiny marks, with no securely visible letter body. | low |
| 522 | l. 19 | `tantôt` | “bientôt” is a possible alternative; compressed beginning. | medium |
| 522 | l. 20 | `hom` | No terminal period is securely visible. | medium |
| 523 | l. 1 | `hom` | No terminal period is securely visible. | medium |
| 523 | l. 2, after the isomorphism sign | cancelled illegible material | A short overwritten symbol or prefix; not reconstructed from the target group. | low |
| 523 | l. 6 | `gén` | Likely abbreviation for générateurs; no final period securely visible. Initial descender supports g. | medium |
| 523 | l. 7, cancelled expression | `l'indétermination à` | Several letters and the final preposition are crossed through; the inserted replacement “d'exactement” is clearer. | low |
| 523 | l. 9 | `respectent` | Final verbal ending is compressed. | medium |
| 523 | l. 9 | `niveaux` | “noyaux” is a possible alternative; the central strokes are not decisive. | low |
| 523 | l. 10 | `respectant` | Ending is overwritten. | medium |
| 523 | l. 12, after `M'_{1,1}` | cancelled illegible symbol(s) | Possibly a subscript or further label; no reconstruction is attempted. | low |
| 523 | l. 13, superscript after M | `t` or `\ell` | Small curled superscript; possibly an altered/stray mark. Its presence is preserved. | low |
| 523 | l. 13, before `Z/2-gerbe` | cancelled illegible word | Dense short stroke after “une”; lexical content unresolved. | low |
| 523 | l. 15 | `yoga` | Initial y and the descending g are visible; the final letter is less distinct. | medium |
| 523 | l. 17, after the target group | cancelled illegible material | Too heavily overdrawn for a dependable symbolic reading. | low |
| 523 | l. 18 | `commutant` | Ending is rewritten over the earlier strokes; an earlier ending cannot be isolated. | medium |
| 523 | l. 21, below-line insertion | `exactement` | Initial “exact-” is clearer than the contracted ending; caret places it before “l'existence”. | medium |
| 523 | lower-left margin | `pg` | “pge” or “p.” may be intended; not expanded in the transcription. | low |
| 523 | lower-left margin | `raisonnable` | Final syllables run into nearby main-text strokes. | medium |
| 524 | 1–2 | `corresponde` | The final letters are reduced; `correspond` is less likely. | medium |
| 524 | 7, insertion before `Sl` | `T̂⁺₁₁ =` | The manuscript's calligraphic letter is provisionally rendered `\mathcal T`; the insertion mark points before the linear-group expression. | medium |
| 524 | 9, interlinear replacement | `raisonnable à vrai dire` | `licite` is clearly deleted; the replacement's internal strokes are faint. | medium |
| 524 | 9 | `vouloir` | Several letters collapse into a horizontal stroke. | low |
| 524 | 9, quoted words | `tout exprimer` | Independent visual comparison supports this reading, but it is not secure enough to remove the doubt mark. | medium |
| 524 | 9, after quotation | `par` | `pour` was also considered. | medium |
| 524 | 10 and 19 | `op.` | The abbreviation is readable; a full stop after `op` is not certain at both occurrences. | medium |
| 524 | 11–16, formula indices | `11` and `1,1` retained as visible | Commas are not uniformly written. No systematic normalization to one index form has been made. | medium |
| 524 | 17, deletion | `choisissant un` | The deleted ending is obscured; the sequence may instead contain another form of `choisir`. | low |
| 524 | 19 | `apprécier` | The middle letters are run together. | medium |
| 524 | 21, before the last morphism | `de` | The short word is overwritten or darkened; whether an intentional deletion is present is unclear. | low |
| 524 | 22 | `interprétés` | The lower edge is close to the word; `considérés` was considered and rejected as less compatible with the visible initial strokes. | medium |
| 525 | 4, deletion | `divisant` | The word is heavily crossed. | medium |
| 525 | 4, insertion above the deletion | `2 ou 4` | The first numeral is partially entangled with the deleted word below; `3` is a less likely visual alternative. | medium |
| 525 | 5, deleted material before `4` | `\illegible{1}` | The mark may be a very short word or a cancellation stroke rather than a complete word. | low |
| 525 | 5, two revision levels | Deleted `4, tel que`; inserted and then deleted `4! = 24,`; inserted `qui` | The values and surviving `qui` are legible; the exact temporal ordering of the revisions cannot be recovered fully. | medium |
| 525 | 6, between `extension` and `finie` | `\deleted{\illegible{1}}` | A crossed fragment is visible, but not enough letters survive for a reading. | low |
| 525 | 12, cancelled morphism | `E₀,₃ → E₁₁` | The first group letter is almost covered by hatching; subscripts and arrow are more legible. | low |
| 525 | 13, superscripts | `G` on both extension symbols | The two superscript glyphs resemble a capital G, but their alphabet or case is not secure. | low |
| 525 | 13, opening parenthesis | `germes` | `groupes` is a possible contextual temptation; the visible word lacks a clear second descender and favours `germes`. | medium |
| 525 | 14, insertion | `ouverts` / `ouvert` | The final s is not separately distinguishable. | medium |
| 525 | 14, following `E₀,₃` | `\deleted{\illegible{1}}` | A short crossed word, possibly beginning with p or f, is unrecoverable. | low |
| 525 | 15, before `les sous-groupes` | `∀` / `tt` | The compact symbol may be a quantifier or an abbreviation for `tous`; it is not expanded in the transcription. | low |
| 525 | 16, after `L'obstruction` | Deleted `à` plus about three unreadable words; inserted `à remonter sur` | The surviving superscribed phrase is clearer than the cancelled baseline; confidence in the insertion alone is medium. | low |
| 525 | 17, after `E₀,₃` | Three unreadable deleted words; inserted `lui m̄` | A stroke associated with the replacement could resemble an arrow; it has not been promoted to a mathematical relation. | low |
| 525 | 17 | `scinder` | The final letters are abbreviated strokes; the word is visibly underlined. | medium |
| 525 | 18, before `±1` | Deleted `Z` | The dense cancellation may hide a further index or quotient sign. | low |
| 525 | 17–18, parentheses | Closing parenthesis after `±1` retained | An opening parenthesis is not securely visible in the corrected sentence; none has been silently supplied. | low |
| 525 | 19, formula (36) | `Z_{/2}` | Slash and 2 are written low; the transcription preserves that placement. The formula is framed on three sides, not rendered as a newly closed rectangle. | medium |
| 526 | 1, deletion | `l'objet` / `bientôt` | The cancellation crosses nearly all the connecting strokes. Two independent readings favoured different alternatives. | low |
| 526 | 2 | `cherchées` | The final syllable is compressed into a short stroke. | medium |
| 526 | 3, first U | `U₀,₂` / `U₀,₃` | The visible final digit resembles 2; the next occurrence has a clearer 3. The apparent discrepancy is retained, not corrected from the surrounding mathematics. | medium |
| 526 | 4, deleted band before `-gerbe` | `{±1}` | Curved enclosing marks can be seen, but the symbols inside are largely covered by hatching. | low |
| 526 | 4, inserted band | `Z_{/2}` | The lowered slash and 2 are retained; no coefficient system is supplied beyond the ink. | medium |
| 526 | 9, before `affine` | `\deleted{\illegible{1}}` | A crossed short fragment is visible but unreadable. | low |
| 526 | 9 | `suffirait` | `suffit` is a possible alternative; the long tail favours the conditional form. | medium |
| 526 | 10, after the parenthesis | `il s'ensuit` | The initial `il` and the middle of the following word are condensed. | medium |
| 526 | 14 | `doit` | The word is overwritten and the first letters are dark. | medium |
| 526 | 16 | `intuition` / `intention` | The dots and medial joins favour `intuition`, but context has not been used to settle the reading. | medium |
| 526 | 16, deletion after `que` | `le` | A loop and a short following stroke survive beneath the deletion. | low |
| 526 | 18 | `arithmético-géométriques` / `arithmético-géométrique` | The last s is not securely distinguishable before the parenthesis. | medium |
| 526 | 19 | `multiplicités` | The middle and the ending are compressed; the accent is faint. | medium |
| 527 | 1 | `vrai`; `connu` | Both words are strongly compressed into short, shallow strokes. | medium |
| 527 | 3 | `passant` | The middle consonants and the ending are abbreviated in the handwriting. | medium |
| 527 | 4, after `du` | Deleted `Q` | A small round overwritten symbol is present; its exact alphabet is uncertain. | medium |
| 527 | 6, equation (38), first argument of `H^p` | Deleted `\overline U_{0,3}`, replaced by `\mathbb Q` | The first argument has been overwritten in place; portions of the bar, U-like stroke, and subscript remain. | low |
| 527 | 6, right end of equation (38) | One closing parenthesis, with two as an alternative | The formula reaches the black right border. One lower curved ending and two clipped upper strokes are visible; `\unsure{)\|))}` records the unresolved count instead of silently supplying the two expected closings. | low |
| 527 | 9, cancelled sequence, first term | `H^1(\mathbb Q)` | The superscript and the argument are crossed over several times. | low |
| 527 | 9, cancelled sequence, middle term | `H^1(U_{0,3},\mathbb Z_{/2})` | The coefficient and punctuation are particularly obscured by cancellation. | low |
| 527 | 9, cancelled sequence, last term | `H^1(\overline U_{0,3},-)` | The superscript, final mark, and final punctuation are uncertain. | low |
| 527 | 10, middle of surviving sequence | Deleted `E` before `H^2(U_{0,3})` | An earlier letter is overdrawn by H; E is a tentative reading of the remaining horizontal strokes. | low |
| 527 | 11, below `E_2^{0,1}` | `H^0(\mathbb Q,H^1(\overline U)` | Only one closing parenthesis is visible after U. The missing outer closing parenthesis has **not** been supplied. | high |
| 527 | 11, coefficient below `E_2^{3,0}` | `\mathbb Z_{/2}` | `\mathbb F_2`; the letter is heavily retraced or overwritten. | low |
| 527 | 13 | `rends` | The final consonant strokes are compressed. | medium |
| 527 | 14, after `d'un` | Deleted illegible word | Approximately one short word; no reliable reading recovered. | low |
| 527 | 17 | `la` | `le`; the small terminal stroke is ambiguous. | medium |
| 527 | 18, first factor under the radical | `x` | `\dot x`; a separate dark point is visible over the first x, but it could be a pen mark or part of the letter. The subsequent polynomial has an ordinary x. | medium |
| 528 | 1 | `on passe` | The first word is almost a single stroke; the internal letters of `passe` are abbreviated. | medium |
| 528 | 3, cancelled word before `Je` | `pour` | `puis`; only the p and a few short upper strokes are legible beneath the cancellation. | low |
| 528 | 3, after `ici` | Full stop | A comma is possible; the mark is very small. | medium |
| 528 | 4 | `dans` | The word's final s-like mark is detached. | medium |
| 528 | 5, cancelled beginning / replacement | Deleted `Une fois`, with inserted `Il` above | The first deleted word and the precise attachment of the replacement are not completely secure. | low |
| 528 | 5–6, line-break cancellation | `homomorphis-` followed by deleted `me extérieur` | The strike seems to extend over the continuation `me`; it may have been intended to cancel only `extérieur`. The transcription preserves the doubtful visible boundary instead of restoring the full word silently. | low |
| 528 | 6 | `tout` | The middle letters are a short stroke. | medium |
| 528 | 8 | `hom.` | `hom` without a full stop; no secure dot can be separated from nearby annotation strokes. | medium |
| 528 | 9, upper annotation of diagram (40) | `N_{0,4}^{!}` | Calligraphic N is also possible. The exclamation mark is visible, but the alphabet cannot be distinguished securely from this handwriting alone. | medium |
| 528 | 12, lower annotation of diagram (40) | `N_{1,1}` | Calligraphic N is also possible. The comma in the subscript is visible. | medium |
| 528 | 12, after `N_{1,1}` | Deleted `\simeq\mathrm{Sl}(2,\mathbb Z)^{\wedge}` | The entire expression is crossed through; the initial relation and terminal completion mark are especially uncertain. | low |
| 528 | 12, 14, and 20, linear-group notation | `Sl` | `SL`; the second letter looks looped and lower-case, but distinguishing the intended case is insecure. Each occurrence is marked. | medium |
| 528 | 13 | `autom.` | `autom` without a full stop; the final abbreviation mark is unclear. | medium |
| 528 | 13 | `intérieure` | The internal vowels and the word ending are rapidly written. | medium |
| 528 | 15 | `discrets` | `discret`; the final s may be no more than a short trailing stroke. | medium |
| 528 | 17, cancelled phrase | `mais` | Its letters merge with the cancellation line; the remainder `il n'est plus tellement` is more legible. | medium |
| 528 | 19–20, display (42) | `\mathfrak S_3`; `\Gamma_2` | The cursive permutation-group symbol and the heavily retraced overbrace label admit other typographic realizations. These are tentative alphabet identifications, not corrections from the mathematical context. | medium |
| 528 | 23 | `deuxième` | The middle strokes and accent are compressed. | medium |
| 528 | 23 | `niv.` | `niv` without a dot; a longer word cannot be excluded, but no reliable `eau` has been recovered. | low |
| 528 | 23, before `noté` | Deleted `\Gamma` | The erased glyph is heavily looped and may instead be another group symbol. | low |
| 528 | 23 | `noté` | The last letter and accent are not individually distinct. | medium |
| 528 | 23, after the group label | `soit` | `est`; the first stroke favors s, but the interior letters are compressed. No article is supplied before the following `produit`. | medium |
| 528 | 24 | `ce` | `le`; the small loop before `sous-groupe` is ambiguous. | low |
| 528 | 24 | `sous-groupe` | `sous-groupes`; the terminal stroke does not securely distinguish singular from plural. | medium |
| 529 | 1 | `exactement` | The compressed ending is not resolved letter by letter. | medium |
| 529 | 2 | `réalisent` | The ending is a compact stroke; `réalisent` is the probable reading. | medium |
| 529 | 3 | `de` in `faire de jaloux` | `des`; the end of the short word is indistinct. | medium |
| 529 | 5–6 | `un sous-groupe Γ₂` | No `de` is visible between `sous-groupe` and the next-line `Γ₂`; none has been supplied. | high |
| 529 | 8 | An uncertain deletion of `Z_{/2}` before `Centre(Γ₂)={±1}` | The heavy strokes may be cancellation, or an overworked but retained `Z_{/2}`. No equality has been supplied before `Centre`. | low |
| 529 | 8 | `Centre` | The middle and ending are compressed; the word may be abbreviated. | medium |
| 529 | Upper margin, line 1 | `Ça` | The first character resembles a large S-like stroke; a short symbol or abbreviation cannot be excluded. | medium |
| 529 | Upper margin, formula | `Sl(2,Z)` with a hat or star-like superscript | `*` versus `∧`; the ink is overworked. | low |
| 529 | 10–11 | `Ça m'étonnerait` | `Je m'étonnerais`; the initial word and final ending are uncertain. No missing `ne` has been supplied. | low |
| 529 | 12–13 | `le groupe des commutateurs … d'indice 4` | The words and numeral are retained despite the apparent mathematical difficulty; no replacement has been made. | high |
| 529 | 14 | `situation` | The beginning is partly crowded by the diagonal marginal writing, and the ending is abbreviated by a stroke. | medium |
| 529 | Middle margin, line 2 | `≃` after `c'est` | Possibly the barred-m abbreviation; the sign is represented with explicit alternatives. | low |
| 529 | Lower margin, line 2 | Uncertain cancellation of `si Π₀,₃` | A long line crosses the phrase; whether it cancels the entire phrase is uncertain. | low |
| 529 | Lower margin, line 3 | `tant` in `en tant que` | The word is strongly compressed and overworked. | medium |
| 529 | Lower margin, line 4 | Deleted illegible symbol or word before `T⁺₁,₁` | The deletion cannot be reconstructed responsibly. | low |
| 529 | Lower margin, lines 7, 8, 13 | Gothic/script `S₃`, rendered as `\mathfrak S_3` with uncertainty | The intended typographic alphabet is not uniquely recoverable from the large looping glyph. | medium |
| 529 | Lower margin, line 13 | `intéressante` | The opening is crowded at the page edge and the ending is a continuous stroke. | medium |
| 529 | 17 | `mod autom. intérieurs` | `intérieurs` versus `extérieurs`; `mod` and the abbreviation `autom.` are also explicitly uncertain. | low |
| 529 | 18 | `l₀,l₁,l₂` | The letterform and small middle subscript are not perfectly distinct; `h` is a possible letterform alternative. | medium |
| 530 | 2 | `T̂₁,₁^{+′}=T̂₁,₁/(±1)` | The order `+′` is visible, while the proof uses `′+`; no plus is visible on the right-hand numerator and none has been supplied. | high |
| 530 | 9 | `Π̂₀,₃′` | A small prime is visible to the right of the Pi expression; the Pi itself is slightly overworked but not treated as a cancellation. | high |
| 530 | 18 | Uncertain deletion of one illegible token after `hom` | It may be an overwritten word or abbreviation, possibly `can.`; the transcription does not silently supply that plausible reading. | low |
| 530 | 19 | `composé` | The last accented ending is very abbreviated; the word is marked uncertain and no continuation or punctuation has been added. | medium |

### Placement and notation observations

- The identification with `\mathbb F_2^2` on scan 527 is placed below the **inner** `H^1(\overline U)` in the annotation below `E_2^{1,1}`. It is not transcribed as an identification of the entire outer `H^1(\mathbb Q,H^1(\overline U))` term.
- Equation (38) has a left-pointing double arrow. All arrows in the surviving exact sequence point to the right.
- Diagram (40) has no visible vertical arrows at either pair of endpoint 1s. Its arrows between the two central groups point downward, while the two Γs are connected by an equality sign.
- The subscript on the Teichmüller and arithmetic-extension symbols in diagram (40) is written `11` without a secure comma; the subscript on the lower N annotation is `1,1`. The later maps (41) and (42) visibly use `1,1`.
- The number (41) is cancelled, but its map is not. The phrase below it is cancelled and replaced below by `et même`.
- Vertical identifications are rendered by equal signs / `\Vert`; their short handwritten strokes sometimes curl. The chosen `\mathcal T`, `\mathcal E`, and `\mathfrak S` typography is a visual interpretation of cursive letter forms and should be checked against the wider manuscript rather than taken as uniquely established by these two pages.

## 3. Abbreviations and abbreviated signs met

Expansions below belong only to these notes. They have not been substituted in the transcription; doubtful points and endings remain doubtful there.

| As written or tentatively read | Proposed expansion or meaning | Qualification |
|---|---|---|
| `ss-groupe` | sous-groupe | Recurrent. |
| `hom.` / `hom` | homomorphisme, or homomorphismes according to context | The presence of a point is not uniform or always clear. |
| `Ker` | kernel / noyau | Mathematical operator; retained as written. |
| `Sl` | special linear group notation | `SL` remains a possible typographic interpretation of the handwriting. |
| `Rem.` | Remarque | Scan 522. |
| `gén` | générateurs | Scan 523; reading and absence of a point remain qualified. |
| `tjrs` | toujours | Scan 523. |
| `op.` | opérations | Some abbreviation points are doubtful. |
| `NB` | nota bene | Underlined where visible. |
| `tt` | tout / tous | In one passage, the alternative reading is a universal-quantifier sign. |
| `cf` | confer / comparez | Scan 523; no point supplied. |
| `pg` | page | Uncertain; `pge` or `p.` may be intended. |
| `m̄`, rendered `overline{mathrm m}` | même | The sign is retained in the French text. |
| `ext.` | extérieur / extérieure / extérieures | Expansion depends on the accompanying noun. |
| `l'ens` | l'ensemble | Scan 524; E is inserted after it. |
| `p.r.` | par rapport | Scan 525. |
| `i.e.` | id est | Recurrent. |
| `et` | étale | Scan 526, in the site subscript; no accent supplied in the transcription. |
| `alg.` | algébrique | Scan 526. |
| `iso.` | isomorphisme | Scan 526. |
| `±` in prose | plus ou moins | Scan 526, “être ± trivial”; distinct from the mathematical ±1. |
| `coeff` | coefficients | Scan 527; no secure terminal point. |
| `mod` | modulo | Scans 528–529; the scan 529 reading is doubtful. |
| `autom.` / `autom` | automorphisme(s) | Exact ending and point are uncertain in places. |
| `niv.` / `niv` | niveau | Scan 528; low-confidence abbreviation. |
| `Aut ext` | automorphismes extérieurs | Scan 530; no expansion inside the formula. |
| `≃` or barred `m` | equivalence-like sign, or même | Scan 529's short marginal note remains ambiguous. |

## 4. Legibility assessment

The main prose and large displayed expressions are substantially more readable than the compressed word endings, small index separators, and overwritten corrections. The least secure passages are the first insertion and corrected prefix on scan 521; the split opening adjective on scan 522; the small M-superscript and rewritten phrases on scan 523; the layered index and obstruction revisions on scan 525; the abandoned cohomology sequence and clipped formula ending on scan 527; the cancellation crossing “homomorphis-/me extérieur” and final congruence-subgroup wording on scan 528; and several oblique marginal passages on scan 529. On scan 530, the overworked token after “hom” remains unresolved.

Enlarged and rotated views were used for the margins and crowded formulas. Independent comparison recovered a comma in the upper T-subscript of (32) and a second punctuation stroke after (35). Other doubtful characters remain marked. Cursive mathematical alphabets cannot always be identified uniquely from this hand. The source's unbalanced parentheses, differing quotient labels, superscript-order changes, and index-4 statement were preserved, with their interpretation kept separate in the research notes. This is a cautious working transcription, not a claim that every letter or revision layer has been recovered.

## 5. Research notes — English, separate from the transcription

Each item identifies its scan location and one of the requested kinds. “Conjecture” includes explicit questions, doubts, and expectations; “unproved claim” includes deferred work and claims whose local justification is only a sketch. A point may be reconsidered or resolved later in the supplied sequence or elsewhere in the manuscript: it remains recorded at the place where it is raised. These notes do not establish novelty or the state of the later literature. **Own ideas** are proposed checks or constructions, with confidence and reasons; none changes the transcription. All source references are to Grothendieck (1981), using the scan numbering specified in the task.

1. **Scan 521, ll. 15–21 — unproved claim.** “cet hom. (27) n'a rien d'injectif, par contre il est surjectif” reverses an apparent expectation about the earlier map; the number 27 is itself a marked reading. A proof would first require recovering that map from the preceding manuscript pages, then computing its kernel and image with the distinction between `Sl(2,Z)` and its quotient by ±1 maintained. The local passage supplies an assertion and a correction of viewpoint, not those computations. (Grothendieck, 1981, scan 521).

2. **Scans 521–522, page transition — conjecture.** “Il faudra donc que je revienne encore sur une façon de donner un sens arithmético-géométrique …” records an explicit intention to revisit the earlier construction. The doubtful adjective at the start of scan 522 is not settled from the argument; what is clear is the wish to supply a geometric interpretation and an extension to profinite groups. (Grothendieck, 1981, scans 521–522).

3. **Scan 522, ll. 5–10, (34) — unproved claim.** “les arguments faits dans le cadre schématique, marchent aussi dans le cas transcendant” asserts transport of the earlier argument to the complex setting. Verification would require specifying the objects and comparison maps and checking that kernels and the central quotient are respected. The literal label under the first T in (34) differs from the corresponding label in (35), so a proof must first distinguish a manuscript notation issue from a substantive assertion without altering the diplomatic record. (Grothendieck, 1981, scan 522).

4. **Scan 522, ll. 15–19 — conjecture.** “On aimerait interpréter (35) et (33) …” and “J'y reviendrai …” defer the proposed identification with the exact sequences associated with the earlier diagram, read tentatively as (9). The missing earlier diagram is essential to testing whether the proposed identifications commute with all maps and with completion. (Grothendieck, 1981, scan 522).

5. **Scans 522–523, final remark and opening — conjecture.** “On peut se demander si l'hom … se remonte (de façon plus ou moins naturelle)” asks for a lift through the quotient by ±1, in both profinite and discrete forms. The upper margin of scan 523 answers that a lift is possible and “plus ou moins trivial”; the body immediately separates mere existence from compatibility with Γ. (Grothendieck, 1981, scans 522–523).

6. **Scan 523, ll. 5–9 — unproved claim.** Freeness “avec deux gén” is invoked to assert “d'exactement quatre façons” to lift, and the parenthesis claims compatibility with the discrete objects inside the profinite setting. A proof would need to specify the equivalence relation on lifts, select the two generators, and check whether their independent central signs exhaust the choices. The word transcribed as “niveaux” in that parenthesis is uncertain, so its precise comparison claim should be verified before formalization. (Grothendieck, 1981, scan 523).

7. **Scan 523, ll. 10–14 — conjecture.** “Mais peut-on le faire en respectant les op. de Γ?” asks for arithmetic equivariance after the elementary lifting observation. The proposed sufficient condition is a lift of the map from `U_{0,3}` to the elliptic moduli object across the `Z/2`-gerbe. Testing sufficiency requires retaining the arithmetic fundamental-group extensions and the effect of basepoint choices, rather than only a map of geometric groups. (Grothendieck, 1981, scan 523).

8. **Scan 523, ll. 14–19 and lower margin — conjecture.** “je suspecte … que l'inverse doit être vrai” proposes an anabelian converse: a Γ-compatible group-theoretic lift should arise from a geometric lift. The marginal “pas tout à fait … pour une formulation plus raisonnable” qualifies that expectation and directs attention to the next page. Any investigation should record this qualification and specify whether maps are actual homomorphisms or outer homomorphisms. (Grothendieck, 1981, scan 523).

9. **Scan 523, ll. 19–22 — unproved claim.** The existence of the geometric lift “signifierait [exactement] l'existence d'une famille de courbes elliptiques …”. The inserted adverb is doubtful. A proof should identify the moduli functor, the level structure continued on the next page, and the residual automorphisms so that the equivalence is stated at the appropriate groupoid level. (Grothendieck, 1981, scan 523).

10. **Scan 523, “quatre façons” and Γ-question — own idea.** Treat the four lifts, conditional on the manuscript's count, as a finite Γ-set and compare its fixed points with sections of the arithmetic lifting problem. This could isolate the difference between the existence of an invariant geometric lifting class and a homomorphism of the full arithmetic extensions. **Confidence: medium**: the finite action is suggested directly by the four choices and the equivariance question, but the precise action and equivalence relation still require construction; this is an investigation, not a claim of novelty or a proved result.

11. **Scan 524, lines 1–6 — conjecture.** Grothendieck writes, “Je doute qu'il en existe une,” about the proposed rigidification, and adds that he doubts the corresponding lift in profinite groups with operations can be made. The preceding page must be retained when specifying exactly which rigidification and compatibility conditions are meant; this is a recorded expectation, not a nonexistence argument (Grothendieck, 1981, scan 524).

12. **Scan 524, lines 7–16 — unpursued implication.** The observation that the profinite linear group “n'a plus de centre trivial” leads him back to the extension and to the question whether the displayed map to `E′₁,₁` “se remonte” to `E₁₁`. The source thus distinguishes the arithmetic extension from its outer action; a study of this passage should identify precisely the information that the central quotient loses (Grothendieck, 1981, scan 524).

13. **Scan 524, lines 17–22; scan 525, lines 1–2 — unproved claim.** The extension lift is described as “plus fort” than a lift compatible with the exterior operations, and the weak question is whether the set E of four lifts has “un élément … invariant par Γ.” A proof should spell out the action on those four outer-homomorphism classes and then isolate the additional compatibility needed to obtain a homomorphism of the full extensions (Grothendieck, 1981, scans 524–525).

14. **Scan 525, lines 3–10 — unproved claim.** The revised index is provisionally read “2 ou 4,” followed by the assertion that after a larger finite extension all “quatre” lifts commute with the exterior action. Once continuity of the action on the four-element set is established, orbit–stabilizer and the kernel of the permutation action are the natural proof requirements; the crossed `4! = 24` is evidence of a revision and must not be treated as the final asserted degree (Grothendieck, 1981, scan 525).

15. **Scan 525, lines 11–19 — conjecture.** He writes “rien ne prouve que l'on puisse trouver un” followed by the inserted expression “grand relèvement,” and records the obstruction as α in the displayed second cohomology group (36). His concluding hesitation is that “rien ne dit” the class vanishes after passage to an open subgroup; the exact allowed restriction matters because the parenthesis distinguishes subgroups containing the geometric kernel from a broader class, although some wording in that parenthesis is uncertain (Grothendieck, 1981, scan 525).

16. **Scan 525, lines 14–22 — own idea; confidence: medium.** Compare restriction to arbitrary open subgroups with restriction only to those obtained by extending the base field. A useful first experiment would write the central-extension class as a continuous finite-valued cocycle and check which open subgroup restrictions kill it; the reason for this suggestion is the manuscript's explicit contrast between the two subgroup conditions, not an assertion that either required lift exists.

17. **Scan 526, lines 1–7 — unproved claim.** The sought relative elliptic curves are said to “forment les sections d'un champ,” identified after correction as a `Z_{/2}`-gerbe, with obstruction β in (37). A proof should construct this gerbe with the exact rigidification data, verify its local nonemptiness and band, and establish that its neutralizations are precisely the desired families; the uncertain first subscript `U₀,₂`/`U₀,₃` should be resolved before making a literal global statement (Grothendieck, 1981, scan 526).

18. **Scan 526, lines 8–14 — unproved claim.** The canonical map from group cohomology to cohomology of U is asserted to be “un iso.” with “coefficients de torsion quelconques,” following a parenthesis excluding type `0,0`. A proof must make the fundamental-group coefficient category, continuity, and the hypotheses on the curve and base field explicit; the manuscript does not provide that argument here (Grothendieck, 1981, scan 526).

19. **Scan 526, lines 14–21 — unproved claim.** Grothendieck says it “doit être ± trivial” that β is the image of α, then draws the expected passage from a lifting at the level of arithmetic–geometric profinite fundamental groups to a relative elliptic curve. The natural verification is a comparison of the central-extension obstruction and the banded-gerbe obstruction under the displayed cohomology map, including the exact meaning of a lift on each side (Grothendieck, 1981, scan 526).

20. **Scan 526, lines 5–7 — own idea; confidence: medium.** Before identifying the displayed obstruction group with a Brauer group, compare its order-two coefficient system with multiplicative coefficients and track the image of β. A useful check would ask whether the relevant coefficient-change sequence leaves a contribution from line bundles; this is suggested by the phrase “groupe de Brauer” beside `H²(U₀,₃,Z_{/2})`, not offered as a correction of the transcription or a calculation of that contribution.

21. **Scan 527, lines 1–4 — unproved claim.** Grothendieck says that a torsion cohomology class “s'efface” after passage to “une extension finie” of the base field. A proof would need to locate the class of (37) in the displayed spectral sequence and distinguish the geometric vanishing from the restriction argument in continuous Galois cohomology; it should specify whether the assertion concerns this particular affine curve and coefficient system or a broader class of objects. (Grothendieck, 1981, scan 527).

22. **Scan 527, lines 7–12 — unproved claim.** The statement `H^q(\overline U_{0,3})=0` for `q\geq2` is used to obtain “une suite exacte.” A complete proof should make the omitted coefficient system explicit outside the transcription, justify the geometric vanishing, and derive the displayed segment, including the maps from `E_2^{0,1}` to `E_2^{2,0}` and from `E_2^{1,1}` to `E_2^{3,0}`. (Grothendieck, 1981, scan 527).

23. **Scan 527, annotations below the exact sequence — unpursued implication.** The manuscript identifies the inner geometric group `H^1(\overline U)` with `\mathbb F_2^2`, but does not explain here the Galois action on this two-dimensional space. Determining that action is necessary before using the displayed vector-space identification to simplify the outer Galois-cohomology term; the two identifications must not be conflated. (Grothendieck, 1981, scan 527).

24. **Scan 527, lines 13–21 — unproved claim.** The existence of the elliptic curve is called “tout à fait triviale,” followed by “il suffit” and the explicit cubic equation. To verify that this answers the preceding lifting problem, one must check more than the existence of an affine equation: smoothness over the intended parameter base, the projective completion and section, the required level data, and the induced map on the relevant arithmetic extensions must all be compared with the requested lift. (Grothendieck, 1981, scan 527).

25. **Scan 528, lines 3–4 — conjecture.** Grothendieck explicitly declines to “approfondir la question” of the extent to which the displayed choice is “naturel.” The issue invites a precise formulation of naturality: which changes of parameter, permutations of branch data, or identifications of the moduli objects should commute with the chosen family, and in what sense of equality or isomorphism? (Grothendieck, 1981, scan 528).

26. **Scan 528, equation (39) and diagram (40) — unproved claim.** The map of moduli objects is immediately followed by a map “d'extensions,” with the two copies of Γ identified. A proof should specify basepoints or the corresponding outer-homomorphism convention and show that the family induces the displayed geometric map while acting as the identity on the arithmetic quotient. (Grothendieck, 1981, scan 528).

27. **Scan 528, lines 13–16 — unproved claim.** The induced homomorphism is described as “défini mod” an inner-automorphism ambiguity, and a discrete counterpart is then displayed. One should verify the exact conjugating group and show that the discrete realization is compatible with the profinite realization; the wording on the page does not itself establish either comparison. (Grothendieck, 1981, scan 528).

28. **Scan 528, display (42) and the following parenthesis — unproved claim.** The manuscript gives an injection into the indicated kernel and adds “et itou pour les groupes profinis.” A proof would have to identify the image of the discrete monodromy and justify the corresponding profinite injection; preservation of injectivity under completion should be verified in this setting rather than treated as formal. (Grothendieck, 1981, scan 528).

29. **Scan 528, final three lines — unproved claim.** The page begins an assertion that the congruence subgroup is a “produit direct” involving `\Pi_{0,3}`; the final factor continues onto the next scan. After reading that continuation, a proof should check generation, trivial intersection, and the commuting of the proposed factors, and should keep the chosen embedding of `\Pi_{0,3}` explicit. (Grothendieck, 1981, scan 528).

30. **Scans 527–528, cubic equation and naturality question — own idea.** Compare the given family with quadratic twists obtained by multiplying its equation by an invertible function on the parameter base, and test whether the same branch or level data survive while the lifted monodromy changes by a central character. **Confidence: medium:** the displayed square-root construction makes such twists a concrete source of alternative choices, but their admissibility for the precise moduli problem and their equivalence relations still need to be checked.

31. **Scan 528, display (42) — own idea.** Compute the monodromy around the missing parameter values using an explicit homology basis and test the candidate matrices `\left(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\right)` and `\left(\begin{smallmatrix}1&0\\-2&1\end{smallmatrix}\right)`, with signs and orientations treated as choices to verify. **Confidence: medium:** the two degenerations visible in the cubic suggest this direct calculation, but neither the matrices nor their relation to the manuscript's chosen generators has been established by the pages transcribed here.

32. **Scan 527, inner `\mathbb F_2^2` annotation — own idea.** If the intended `U_{0,3}` is the punctured-line parameter model suggested by the equation, compute the Galois action on its two geometric cohomology generators explicitly and test whether the outer term decomposes into two spaces of quadratic characters. **Confidence: medium:** the displayed vector-space dimension supports the proposed check, while equivariance and the exact coefficient convention remain essential unresolved inputs.

33. **Scan 529, lines 1–8 — unproved claim.** The text says that there are “quatre sous-groupes” realizing the preceding decomposition and describes their intersection through four homomorphisms to the central order-two group (the overwritten target needs paleographic caution). A proof would have to identify the relevant splittings, explain why precisely four occur, and verify the stated bounds on the intersection's index rather than infer them solely from the count of splittings. (Grothendieck, 1981, scan 529.)

34. **Scan 529, upper margin — unproved claim.** The marginal “doit être le noyau” identifies the intersection with a kernel of reduction to `Sl(2,Z/4Z)`, although the decoration on the source group is uncertain. A proof would need an explicit reduction calculation and a distinction between the discrete and completed groups if that decoration is a completion hat. (Grothendieck, 1981, scan 529, upper margin.)

35. **Scan 529, lines 10–14 and middle margin — conjecture.** In the main text, the phrase immediately preceding “pas que ce soit juste” is uncertain, but the proposed identification with “le groupe des commutateurs” and the statement “d'indice 4” are visible. The nearby marginal “c'est vrai” appears to endorse a nearby claim without supplying its proof; its exact attachment should be checked before treating it as a resolution of the commutator question. (Grothendieck, 1981, scan 529.)

36. **Scan 529, lines 12–13 — own idea.** If the symbol here denotes an ordinary free group of rank two, abelianizing that group gives an infinite quotient, whereas reducing that abelianization modulo two gives a quotient with four elements. Comparing the ordinary commutator subgroup with the kernel of this latter map is therefore a useful diagnostic for the stated index 4, without changing the transcription or deciding what Grothendieck intended. **Confidence: high for the conditional group calculation; low for its relevance to the intended wording**, because the local conventions and marginal attachment still require checking.

37. **Scan 529, lower margin, lines 1–10 — conjecture.** The marginal question begins “Il n'est pas clair” and later says “je présume que oui,” asking whether the displayed copy of `Π₀,₃` is invariant in the Teichmüller group and stable under the exterior `S₃` action. A proof must distinguish invariance of a subgroup, invariance of its conjugacy class, and the existence of compatible representatives of outer automorphisms. (Grothendieck, 1981, scan 529, lower margin.)

38. **Scan 529, lower margin, lines 11–14 — unpursued implication.** The proposed quotient “serait une extension centrale intéressante” of `S₃` by `{±1}`. Before constructing or identifying this extension, one must establish the normality needed for the quotient and then verify that the surviving kernel is precisely the stated central subgroup. (Grothendieck, 1981, scan 529, lower margin.)

39. **Scan 529, lower margin — own idea.** Compute how the relevant permutations act on the four complements or splittings described at the top of the page, together with their characters into `{±1}`. A fixed complement would be a concrete candidate for the invariant subgroup contemplated in the lower margin; an action without a fixed complement would expose a needed qualification. **Confidence: medium**, because the proposed finite calculation is natural from the page's four-splitting discussion, but its interpretation depends on the precise action and subgroup identifications.

40. **Scan 529, lines 15–19 — unproved claim.** Grothendieck says “il faudrait aussi expliciter l'homomorphisme (42)” by its values on the three indicated generators and adds “j'y reviendrai peut-être tantôt.” The deferred work is an explicit generator calculation, with particular care over the uncertain parenthetical qualification concerning the ambiguity in the homomorphism. (Grothendieck, 1981, scan 529.)

41. **Scan 530, lines 1–10 — unproved claim.** The theorem states that the natural exterior action of `Γ_Q` is “fidèle,” even after the displayed central quotient, and refers to “la proposition du début” for the argument. A self-contained proof on these pages would need the earlier proposition and a precise statement explaining how the compatible exterior injection transfers faithfulness to the larger target; an arbitrary subgroup inclusion alone does not explain that transfer. (Grothendieck, 1981, scan 530.)

42. **Scan 530, lines 11–19 — unproved claim.** The corollary declares the canonical surjections `Γ_Q → Γ_{1,ν}` for `ν≥1` to be “injectifs, donc des isomorphismes.” The written proof reduces to `ν=1` and starts to form a composite into an exterior automorphism group, but the page ends before that composite is written out and the deduction completed. (Grothendieck, 1981, scan 530.)

43. **Scan 530, theorem and corollary — unpursued implication.** The words “et même sur” assert that passage to the indicated central quotient does not destroy the faithfulness used in the argument. It would be useful to isolate the exact group-theoretic criterion preventing a nontrivial arithmetic action from becoming inner after this quotient, rather than assume faithfulness automatically survives a central quotient. (Grothendieck, 1981, scan 530.)

44. **Scan 530, lines 15–19 — own idea.** Write the three maps in the corollary's factorization explicitly and compare the kernel of the composite with the kernel of `Γ_Q → Γ_{1,1}`. If the composite is exactly the faithful action from the theorem, the kernel inclusion gives the required injectivity; the substantive check is equality of the actions with their outer-automorphism ambiguities. **Confidence: high as a conditional kernel argument**, because this is the reduction suggested by the visible proof, not a claim that the omitted compatibility has already been verified.

## Reference

Grothendieck, A. (1981). *La longue marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2; supplied scans 521–530 of the archive file described as “pages 1–292”]. Université de Montpellier.

The date, title, and archival attribution follow the supplied task description; the readings and scan locations were checked against the supplied images.
