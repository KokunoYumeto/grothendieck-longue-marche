# LM_C3-283-301 — Editorial and research notes

## 1. Source, scope, and pagination

The accompanying LaTeX fragment covers all **19 supplied scan files, 283–301, in filename order**. The source is the manuscript identified in the supplied prompt as Alexander Grothendieck's *La Longue Marche à travers la théorie de Galois* (1981), Montpellier archive cote 140-3, in the file described there as “La Longue Marche, pages 293–650.” This identification follows the supplied material. The reading record and research observations below refer to that source (Grothendieck, 1981).

The filename scan numbers differ from the visible pagination. `\scanpage{N}` follows the filename; `\mspage{n}` records the handwritten numbers at their respective positions. Both visible handwritten numbering layers have been retained, without assigning them to different hands or dates. The printed Montpellier institutional footer is not part of the manuscript transcription.

| Filename scan | Lower handwritten number | Upper handwritten number, where present |
|---|---|---|
| 283 | 282 | — |
| 284 | 283 | 443 |
| 285 | 284 | — |
| 286 | 285 | 444 / 449, uncertain |
| 287 | 286 | — |
| 288 | 287 | 445 |
| 289 | 288 | — |
| 290 | 289 | 446 |
| 291 | 290 | — |
| 292 | 291 | 447 |
| 293 | 292 | — |
| 294 | 293 | 448 |
| 295 | 294 | — |
| 296 | 295 | 449 |
| 297 | 296 | — |
| 298 | 297 | 450 |
| 299 | 298 | — |
| 300 | 299 | 451 / 351, uncertain |
| 301 | 300 | — |

Each scan was inspected as a whole, transcribed from the image with enlarged regions as needed, and reread against the fragment. Selected difficult passages received an independent second reading. No published transcription was used to supply missing text. Deletions, additions, marginal notes, underlining, and uncertain readings use the prescribed macros. Where revision strokes overlap, the proposed attachment or cancellation scope is recorded as a doubt. Unreadable-word counts are estimates; a compact unreadable mathematical group can be counted as one unit.

The transcription is a UTF-8 LaTeX **fragment**, with no preamble or macro definitions. It expects definitions of the editorial macros in the containing document; its mathematical displays use conventional LaTeX/AMS notation and the clear diagram uses `tikz-cd`. Equation numbering, repeated labels, incomplete punctuation, apparent discrepancies between adjacent formulas, and uncertain alphabets have not been reconciled by mathematical inference. The proposed mathematical investigations appear only in section 5 of this notes file.

## 2. Table of doubts

Locations refer to the supplied scan images. Approximate line counts include displayed formulas; an equation number, margin, or quoted anchor is often the more precise locator. **Confidence means confidence in the reading, not confidence in the mathematical assertion.** A dash or an unreadable mark indicates that no responsible alternative was recovered. Closely related doubts are grouped in a single row where they occupy the same passage.

### Scans 283–287

The approximate positions count visual written lines and displayed formulas together; a named equation or margin is more reliable than a line number. Confidence refers to the proposed reading, not to the truth of any mathematical assertion. `—` means no responsible alternative could be identified.

| Scan | Approximate line / location | Reading retained | Alternative / unresolved point | Confidence |
|---|---|---|---|---|
| 283 | 1 | `suppose` | Final strokes do not establish whether the verb ends here. | low |
| 283 | 1, cancellation and replacement | `que`; inserted `(29)`, `1,ρ,σ`, `sont lin.` | Approximately four cancelled words and one cancelled number are unreadable; insertion placement partly overlaps the deletion. | low |
| 283 | 4, cancelled ending | `\illegible{4}` | Replaced by the condition `(30) Tr N₁ρ inversible.` | low |
| 283 | upper left margin | `1,ρ⁻¹,ε₁(=1+N₁)` and `1,σ⁻¹,ε₁(=1+N₁)` | Short surrounding notes / ditto-like strokes cannot be resolved. | medium |
| 283 | diagonal margin, heading | `29)`, `30)`, `primo` | Numerals resemble `2°)`, `3°)`; approximately five further words are unreadable. | low |
| 283 | diagonal margin, matrix calculation | cancelled symbol; `N₁ρ = ⋯` | The marks between the second and third equality signs could contain a minus sign or another term. | low |
| 283 | diagonal margin, starred ending | `normalisant` | Ending partly compressed. | medium |
| 283 | crossed paragraph beneath conjugation formulas | `Soit B₀ le normalisateur de …`; `L₀ = ss-g` | The crossed object after `de` is unreadable; `ss-g` is tentative. | low |
| 283 | immediately before ε₀(λ) | cancelled `posons`, added `posons` | The cancellation is heavy; the second word is much clearer. | medium |
| 283 | exact sequence and adjacent prose | `B₀` without prime | The displayed and adjacent symbols do not show a clear prime, although the preceding definition names `B′₀`; the transcription does not repair this. | medium |
| 283 | final target | `E¹` | `E′`; the raised stroke is vertical and not decisive. | low |
| 284 | 2 | crossed `des` | The overstroke may conceal a different preposition. | low |
| 284 | after (79) | cancelled `Cor.` | The initial abbreviation is heavily overwritten. | low |
| 284 | (79), isomorphism sign | `≃` | A rightward arrow with a tilde is also possible; the lower stroke ends thickly without a clearly resolved arrowhead. | medium |
| 284 | after (79) | `aussi` | `ainsi` | medium |
| 284 | both projection sources | `X_ρ` | No second subscript is visible; retained without adding `σ`. | high |
| 284 | insertion below first trace condition | `−N₁σ = N₁ρ = ρN₀ = −σN₀` | The first two products have overwritten symbols; the insertion is linked to the preceding `ρ+σ` by a brace-like mark. | medium |
| 284 | above and before (80) | cancelled `…det(u)=` and one cancelled symbol | The cancelled initial expression is unreadable; the underline on `u` is faint. | low |
| 284 | final line | `groupe` | `groupes`; the final stroke is inconclusive. | medium |
| 285 | second correspondence row | `μ′` | `μ″`; the superscript is an ink blot. | low |
| 285 | multiplication-law equation number | `81` | `21`; the first digit has a small angular upper loop. The sequence alone does not settle the written shape. | medium |
| 285 | below (81), conjugation notation | `x` | `X`; both occurrences have reinforced/corrected strokes. | medium |
| 285 | below conjugation notation | cancelled `pour` | Could be a connective correction stroke rather than a completely readable word. | low |
| 285 | heading | `III` with upper and lower strokes | Roman numeral is clear; overline and underline reproduce the two strokes. | high |
| 285 | membership condition following (82) | `E¹_S` | `𝒪*_S`; the glyph is overwritten and the raised stroke is not secure. | low |
| 285 | (83), input third coordinate | `μ` | Overwriting prevents identifying the earlier symbol. | medium |
| 285 | (83), second output coordinate | `σ` over cancelled `ρ` | The surviving descender is consistent with an earlier `ρ`, but this earlier reading is uncertain. | medium |
| 285 | last line, before `un épimorphisme` | `\illegible{1}` | Cancelled short word. | low |
| 286 | upper manuscript number | `444` | `449`; the last digit is rounded. | medium |
| 286 | (84), vertical isomorphism mark | `\wr` | It is a vertical wavy isomorphism mark beside the upward arrow. | high |
| 286 | after “diagonale” | cancelled `forme` | The overstroke obscures the middle letters. | low |
| 286 | insertion after `(u,μ)` | `μ∈ΓE¹` | `μ∈ΓE′`; the raised mark is short. | medium |
| 286 | immediately after (85) | `tâchera` | `tâche`; the final connected strokes are faint. | medium |
| 286 | paragraph before theorem | `formée` | `fournie`; retained as an alternative instead of choosing by syntax. | low |
| 286 | immediately following `formée/fournie` | `des` | `par`; short connecting strokes and syntax are not decisive. | low |
| 286 | unnumbered solution tuple / (86) | `(u a,u b,μ=det u)` / `(u a⁻¹,u b⁻¹,det u)` | The inverse exponents occur in (86) but are not visible in the preceding tuple. | high |
| 286 | target of (86) | `𝔼¹` | Plain `E¹`; doubled left stem suggests a distinct alphabet, but its type is uncertain. | medium |
| 287 | first word | `Elle` | Heavily reinforced/overwritten; an earlier form cannot be separated reliably. | medium |
| 287 | below `De façon plus précise, soit` | cancelled `localement` | Final letters are obscured by the cancellation. | medium |
| 287 | existence sentence | `alors`, added `d'` before `uniques` | The first word is compressed; the elevated small mark is compatible with `d'` but not fully clear. The preceding sentence also ends in `alors`; both are retained. | medium |
| 287 | cancelled formula above (88) | `α a = β b (soit u)` | The cancellation crosses the equality sign and final parenthesis. | medium |
| 287 | cancelled formula below (88) | `β b` followed by `\illegible{2}` | The remaining symbols may contain `∈ Γ`; approximately two symbolic groups are unreadable. | low |
| 287 | unnumbered commutator-pair equation | left second entry `[β,ρ]` | The symbol has a clear descender and is retained as `ρ`, despite the `σ` in adjacent constructions. | high |
| 287 | same equation, right second entry | `σ` over cancelled `ρ` | The descender suggests an earlier `ρ`; the final overdrawn symbol is read as `σ`. Earlier state remains uncertain. | medium |
| 287 | `est donc det u … ; donc` | one cancelled item unreadable | Small overwritten symbol after `u`. | low |
| 287 | equation number after determinant sentence | `89` | The second digit and the lower part of the first digit are overwritten; no secure alternative is offered. | medium |
| 287 | cancelled heading before proof | `Dém. Il` | Heavy crossing prevents complete confidence in either word. | low |
| 287 | proof, uniqueness sentence | `α,β` | Greek letters are visible; the transcription does not replace them with underlined `a,b` from (88). | high |

### Scans 288–292

Approximate line numbers count the body from the top and are supplemented by equation numbers or physical locations. Repeated alphabet doubts are grouped by occurrence and location. “High” means the proposed reading is strongly supported but a small graphical uncertainty remains; “medium” means plausible with incomplete letter-level support; “low” means the ink does not choose securely between the stated possibilities. An illegible deletion does not receive a fabricated reconstruction.

| Scan | Approximate line / location | Reading in the fragment | Alternatives / unresolved detail | Confidence |
|---|---|---|---|---|
| 288 | Between (91) and (92) | `\overline{\mathrm m}` | The sign resembles two nearly horizontal strokes; it may be the manuscript's shorthand for *même*, but the lower stroke is not a clearly formed m. | medium |
| 288 | (93), above the underlined a | `\underline a` | A small mark above a could be an overtrace or an added symbol; no exponent has been silently supplied. | medium |
| 288 | Immediately before the first pair of matrices | `numérique` | Several medial strokes are compressed; *numérique* is the best reading, not fully letter-secure. | medium |
| 288 | Reference before (94), and last paragraph | `398′` | `398¹`; the raised final mark is not securely a prime rather than a superscript numeral. | medium |
| 288 | Explanation to the right of (94) | `coeff coin` | *coin* is probable; its initial strokes are partly retraced. | medium |
| 288 | Matrix for η beside (95) | `U` | Lowercase `u`; the separately written denominator uses a larger U-like form. | medium |
| 288 | Last line, α as a function of μ | `α₂` | The first glyph could be Latin a rather than Greek α; subscript 2 and argument μ are clearer. | medium |
| 288 | Supplementary denominator forms under (94) and (95) | Marked as insertions | The placement and darker writing support later additions, but their exact writing sequence cannot be established from the scan alone. | medium |
| 289 | Line 3, far right | `je` | The word is close to the right boundary; its e is not fully separable. | medium |
| 289 | Lines 6–7, before “avec la possibilité” | `des [illegible: 1 word]` | The word after the article has a large curved initial and strokes resembling “Cart…”; no confident completion is offered. The article may be *du*. | low |
| 289 | First displayed equation | `ℓ₁^ν` | `e₁^ν`; the looped base letter is unclear. The annotation explicitly gives ε₁(μ−1) in the current notation. | medium |
| 289 | Left margin beside first equation | One deleted word after `sont` | The word under the horizontal cancellation cannot be recovered reliably. | low |
| 289 | After underlined “généralisation” | `p.r.` | The compressed abbreviation is likely *par rapport*; its punctuation and second initial are faint. | medium |
| 289 | “Il faudra donc … reprendre” | `tantôt` | The middle vowel group is compressed; this is a tentative word, not an expansion of the sentence. | medium |
| 289 | Number of second displayed equation | `(95)` | `(96)`; the first part of the label has been overwritten. The possible repetition of the preceding page's (95) is retained rather than corrected. | low |
| 289 | Lower correction after “deux membres” | Deleted `ε²=1` followed by one illegible item | A final extra sign or letter is crossed out; it is not recoverable with confidence. | low |
| 289 | Immediately above the uncancelled ε²=1 | One deleted item | Dense short crossing makes the original item unreadable. | low |
| 290 | First paragraph, name after “d’” | `Azumay.` | `Azumaya`; the last mark after y looks like a dot, but may be an extremely reduced final a. | medium |
| 290 | First paragraph, “droites …” | `projectives` | The ending is partly covered by a darker stroke. | medium |
| 290 | All three standalone bundle symbols | `\mathcal P` | Plain P; the rounded loop and curved stem suggest a script letter, but handwritten alphabet distinction is not decisive. | medium |
| 290 | After “Borel convenable)” | One deleted word before inserted L | No secure reading under the cancellation. | low |
| 290 | NB paragraph, first inserted and subsequent `ens.` | `ens.` | The abbreviation is probable but several strokes are very short. | medium |
| 290 | “sections N … de M” | One deleted item | May be a fragment of a nonzero condition; its mathematical content is not supplied. | low |
| 290 | “sur … fibre” | `tte` | The abbreviation probably means *toute*; the second t is overwritten. | medium |
| 290 | “strictement …” | `nilpotentes` | The beginning of the word is retraced. | medium |
| 290 | “à toute telle section … un sous groupe” | `correspondra` | `correspond`; the final strokes are not secure enough to force the tense. | medium |
| 290 | Additive group in the sentence before (2) | `\mathbf G_a` | Ordinary roman `G_a`; the heavier G may be retracing rather than intended bold alphabet. | medium |
| 290 | Inserted name of the map in (2) | `e_N(λ)` | The e is heavily retraced. The exp(λN) that follows is intact, not deleted. | medium |
| 291 | Top continuation, “définissent le …” | `\overline{\mathrm m}` | Same compressed shorthand issue as scan 288. | medium |
| 291 | After Tr N=0 in the first paragraph | One deleted word | Cancellation obscures the lettering. | low |
| 291 | Two occurrences of trace-zero module | `{}_1\mathcal M` | Baseline `1\mathcal M`; the prefixed glyph resembles 1, but its placement relative to M is ambiguous. | low |
| 291 | Deleted word before “conique” | `quadrique` | Only the initial and some medial strokes are clearly visible under the line. | medium |
| 291 | Definition e=e_N=…e_N(1) | One deleted item | Perhaps an abbreviation indicating definition, but not confidently legible. | low |
| 291 | Final prose, after “Tr et det” | `de deux` | `des`; the following line itself begins *deux*, so the apparent repetition has not been silently removed. | low |
| 291 | Final prose, name of N and e | `opérateurs` | `opérations`; compressed terminal strokes permit both. | medium |
| 291 | Final prose before “déterminent” | Deleted `se` | The deletion is clear; the two-letter reading is probable. | medium |
| 291 | Last trace display | `2 Tr λ`, `−2 Tr λ` | The extra Tr signs are visibly present. This is an interpretive issue rather than a doubtful reading: they have not been replaced with 2λ. | high |
| 292 | First paragraph, deleted adjective before “unipotentes” | `strictes` | `strictement`; terminal strokes lie under a long cancellation. | low |
| 292 | First line of (4), overwritten definition notation | Inserted `def` | `dfn`; the abbreviation and underlying cancelled item are crowded together. | low |
| 292 | First line of (4), cancelled item after e^λ | One illegible item | The crossing is too dense to reconstruct the former notation. | low |
| 292 | Additive and multiplicative group letters in (4) | `\mathbf G_a`, `\mathbf G_m` | Ordinary roman G; heavier stems may reflect retracing. | medium |
| 292 | Crossed side remark in (4) | `on aura` and one unreadable word | Only the first words are tentatively recoverable. | low |
| 292 | Side remark, under the crossed line | `néc.` with raised `t` | The exact terminal abbreviation is uncertain; likely *nécessairement*. | medium |
| 292 | Bundle symbol in the correspondence paragraph and last paragraph | `\mathcal P` | Plain P; same rounded-letter ambiguity as scan 290. | medium |
| 292 | Name of the chosen section and its occurrence in (5) | `x_∞` | The subscript is heavily retraced; x with an unclear subscript is certain, ∞ less so. | medium |
| 292 | Last paragraph after deleted “voir” | `considérer` | Ending at the right margin is faint. | medium |
| 292 | Deleted item immediately before (5) | About three items illegible | Formula-like writing is crossed repeatedly; its symbols are not reconstructed. | low |
| 292 | Cancelled bottom passage | `Un fibré vectoriel … vectoriel des translations … inversible D` | Only the quoted islands are readable; the extent of cancellation around the upper-right opening is also uncertain. Counts of missing words are approximate. | low |

### Scans 293–297

Locations are approximate main-text lines or the manuscript's displayed-equation labels. “Unresolved” means that no defensible alternative reading was found. Repeated uncertainty about the alphabet of the projective-space symbol is grouped by scan; it is marked at each occurrence in the transcription. The scan labels are filename numbers. The lower handwritten numbers are respectively 292–296; upper handwritten 448 and 449 also occur on scans 294 and 296.

| Scan | Approximate line / location | Reading retained | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 293 | Lines 4–5, after the first display | `additif` | First letters overwritten; no secure alternative. | medium |
| 293 | Display (7), parenthesis | `nilpotent` | Very compressed ending may be an abbreviation rather than the full word. | low |
| 293 | Line introducing (8) | `s-groupe` | Abbreviated form is compressed; no secure expansion has been imposed. | medium |
| 293 | Display (8), second member | `\underline e(\lambda)` | `e_{\lambda}(\lambda)`; a small, dark, overwritten mark lies under/beside the opening parenthesis. | low |
| 293 | Paragraph after (8) | `intrinsèquement` | Ending is a nearly horizontal stroke; `intrinsèque...` remains possible. | medium |
| 293 | “fibré vectoriel (...)” | `respectée` | Initial strokes are crowded. | medium |
| 293 | After “dans G)” | Deleted word; `à` | One crossed word is unresolved; following mark could be a colon rather than `à`. | low |
| 293 | Paragraph before (9) | `canonique` | Compressed ending might be an abbreviated adverb. | medium |
| 293 | Inclusion before (9) | `{}_1M` | Position and shape of the left-hand subscript are faint. | low |
| 293 | Immediately after that inclusion | Deleted `sous` | Crossed word is only partly recoverable. | low |
| 294 | Top paragraph, deletion after `L^*` | `partout` and a crossed inequality sign | Final sign is overwritten; no following numeral is securely visible. | low |
| 294 | Top paragraph, last line | `tte` | Abbreviated “toute” reading; the middle strokes are compressed. | medium |
| 294 | Left margin | `cano.` | Final letter/abbreviation punctuation is faint. | medium |
| 294 | Left margin | `isom` | Initial stroke could belong to an opening parenthesis; the rest suggests the abbreviation. | medium |
| 294 | Left margin, affine complement | `\mathbb P` or `P`; `x` | Projective symbol's alphabet is not secure; the point may have an infinity subscript. | low |
| 294 | Paragraph beginning “Revenons”; final paragraph | `(82)` | `(32)`; the first numeral is open and resembles a 3. Both alternatives are recorded instead of supplying a reference from context. | low |
| 294 | After “modulo” | `transformations` | Terminal stroke does not securely distinguish singular from plural. | medium |
| 294 | Deleted clause after the commutators | `les données` | These words lie under the replacement “On peut l'exprimer en”; deletion is partly obscured. | low |
| 294 | Display (10), first automorphism subscript | `Sgr` | `S-gr`; a hyphen is not securely separable from the preceding letter. | low |
| 294 | Same display, third automorphism subscript | `Sgr` | `Sg`; right-edge crowding and the descender obscure the last letter. | low |
| 294 | Same display, final object | `\mathbb P` | `P`; alphabet distinction is unresolved. | low |
| 294 | Number of the automorphism display | `(10)` | `(40)`; the first numeral is overwritten. | low |
| 294 | Final paragraph, deleted phrase | `faux fibré` | Both words are crossed; the first is especially uncertain. | low |
| 295 | Opening reference | `(82)` | `(32)`, as in scan 294. | low |
| 295 | Display (12), first commutator | Deleted `\beta`, replaced by `\alpha` | The lower remnant looks like a beta; the current alpha is clear. | medium |
| 295 | After “Considérons l'image” | Deleted `\widetilde L_1` | `\widetilde L_0`; the crossed index is unclear. | low |
| 295 | Display (13), just after `PG` | Deleted illegible symbol | A small, cramped remnant cannot be identified. | low |
| 295 | Display (14), annotation above equality | `dfn` | Last letter may be only a flourish. | medium |
| 295 | Display (14), annotation at left-pointing isomorphism arrow | `can` | Small letters overlie the arrow; exact spelling/abbreviation is not secure. Arrow direction is visibly leftward. | low |
| 295 | Deleted sentence following (14) | “Je dis que [illegible] la relation” | One dark, overwritten item between “que” and “la” is not recoverable. | low |
| 295 | Before “en termes de” | Deleted `et` | Crossed item could contain an additional short word. | low |
| 295 | Annotation below (16) | “par commodité” | The words are readable, but attachment of the insertion to the minus sign or ensuing dash/parenthesis is uncertain. | medium |
| 295 | Lower-left NB, “plus ...” | `gén` with superscript `t` | Very compressed abbreviation. | low |
| 295 | Same NB, following `si 2` | `élément` | Small overwritten letters; the phrase “régulier de Γ(S,O_S)” is much firmer. | low |
| 295 | Same NB, after underlined “Mais” | `en car. 2` | Underlined phrase is compressed and partly crossed by other strokes. | low |
| 295 | Same NB, two following underlined lines | Two illegible spans, approximately five and four words | No dependable reconstruction; strokes touch the page edge and other notes. | low |
| 295 | Same NB, final mathematical mark | `\mu_2`, followed by emphatic punctuation | Symbol and punctuation are heavily overwritten. | low |
| 296 | Opening group name | `Gl(2)_S` | `GL(2)_S`; case of the second letter is not secure in the handwriting. | medium |
| 296 | Sentence after (17) | `local` with superscript `t` | Compressed abbreviation, possibly a longer abbreviated form. | medium |
| 296 | Throughout, including (18) | Generic projective symbol `\mathbb P` or `P` | Generic symbol and bold/checked projectivization symbols are visually different, but the exact alphabets cannot be guaranteed. | low |
| 296 | “Mais ... P se réalise” | `la` | `le`; small vowel is overwritten. | low |
| 296 | After “comme”, before (18) | Deleted illegible symbol | Possibly an abandoned projective symbol, but not transcribed as a certain P. | low |
| 296 | Display (18) | `\mathbf P(F)` and `\check{\mathbf P}(F)` | Plain P variants; the check on the third symbol is visible. | medium |
| 296 | Before “les sections” | Deleted `Ainsi`, inserted `i.e.` | Current small abbreviation is clearer than the deleted word. | low |
| 296 | Display (19), before the surviving isomorphism sign | Deleted illegible mark | A small overwritten relation sign cannot be distinguished. | low |
| 296 | “x_D de P ... n'est autre que” | Deleted `est` | Only a short crossed remnant remains. | low |
| 296 | Immediately before (20) | Deleted illegible symbol | Indeterminate mathematical glyph. | low |
| 297 | Rewritten proposition, opening group name | `Gl(2)_S` | `GL(2)_S`. | medium |
| 297 | Rewritten proposition, after “soit section” | Inserted illegible word; `unipot.`; deleted `régulière` | Several writing layers intersect. The position and exact extent of the tiny inserted item are uncertain. | low |
| 297 | Rewritten proposition, before “relation (16)” | `liée`, `par la` | Crowded insertion crosses the older line; exact small words are not secure. | low |
| 297 | Condition (i), after “est” | Approximately two deleted words; inserted “section” | Deleted words cannot be recovered. | low |
| 297 | Condition (i), before inserted `≠1` | Deleted illegible item | Dark over-writing obscures the previous symbol/word. | low |
| 297 | Condition (i), parentheses | Both visible closing parentheses retained | The punctuation appears unmatched after the first parenthetical clause; no editorial repair was made. | medium |
| 297 | Condition (i) and left NB | `\mathbb P` or `P` | Alphabet uncertainty as above. | low |
| 297 | Condition (ii) and right-margin addition | `Itou` | `Item`; the handwritten middle/final strokes are not fully distinct. | medium |
| 297 | Condition (ii), final `\widetilde\rho` | No inverse exponent is transcribed | No `−1` is visible there, although one might be expected from comparison with (i). This is a retained textual discrepancy, not an emendation. | high |
| 297 | Condition (iii), last word | `inversible` | Final letters reach the scan edge. | medium |
| 297 | Proof, insertion after “normalise ...” | “ou ce qui revient au” `m̄`, `L_1` | Phrase and its attachment are crowded; the overlined m sign and `L_1` are more distinct. | medium |
| 297 | Numbered equality of inverse images of `x_1` | Deleted `\widetilde\rho^{-1}`, replaced by `\widetilde\sigma^{-1}` | Descender of the earlier rho remains under the replacement sigma. | medium |
| 297 | Number of that equality | `(22)` | `(24)`; strongly overwritten digits. | low |
| 297 | Parenthesis “quitte ... à remplacer” | Deleted illegible word | Horizontal cancellation masks its letter shapes. | low |
| 297 | “on aurait” | Deleted `Tr` | Retouched letters may include more than the trace abbreviation. | low |
| 297 | Before inserted OPS near the bottom | Deleted illegible word | Not enough ink survives to choose among plausible verbs. | low |
| 297 | Final two lines | Deleted `op`, inserted `endom` | Abbreviations are compressed; no punctuation has been added to them. | medium |

### Scans 298–301

| Scan | Approximate line or location | Reading retained | Alternative / unresolved issue | Confidence |
|---|---|---|---|---|
| 298–300 | Projective-bundle symbol, in prose and formulas | `\mathcal P` / `P` | Rounded looped letter does not securely distinguish alphabet. Explicit alternatives have been retained. | medium |
| 298 | First line | `un`; deleted `opérateur`; inserted `endom.` | The overwritten noun and abbreviation are not securely legible; one deleted word remains unreadable. | low |
| 298 | Second line, after `alors` | Deleted unreadable text | Estimated two words. | low |
| 298 | Fourth line, before `Prenons` | Deleted `sss` | The three characters are densely overwritten. | low |
| 298 | Matrix calculation, line beginning `Tr N₁σ` | `σ e₁ = a e₀ + b e₁` | Index on the first `e` is uncertain; retained without correcting it to fit conventional matrix multiplication. | low |
| 298 | Same line, right edge | `D + σD = D + b O_S e₂` | Final index could be `0`; ink is crowded at the edge. | low |
| 298 | After `conditions équivalentes` | Deleted `dans P` | The crossed-out last character may be another symbol. | low |
| 298 | Equation (23) | Second operator `σ̃⁻¹` | Operator is overwritten and can resemble `ρ̃⁻¹`. | medium |
| 298 | After (23) | `définissent` | Ending is faint and partly at the right edge. | medium |
| 298 | After (24) | Deleted `qui`, then one unreadable deleted word | The deleted word before `intersection` cannot be recovered. | low |
| 298 | Last line | Tentative `l'image inverse du s.-groupe (privilégié`, inserted `torique` | `des s.-groupes`, `privilégiés`, and `toriques` remain alternatives. A second visual reading supports `inverse`, but the connecting words, number, and parenthetical ending are faint; all disputed elements remain marked. | low |
| 299 | First word | `dit` / `dont` | The cross-page connector remains uncertain after an independent visual reading; neither alternative is asserted as secure. | low |
| 299 | First paragraph, deleted words | `points`; `permet de` | Both are crossed through; the former is more legible than the latter. | medium |
| 299 | First paragraph, after `x₁` | Closing parenthesis | A closing parenthesis is visible; its opening is not securely identifiable. | medium |
| 299 | Equation (26), right-hand annotation | `produit ½ direct` | The word `produit` is written with a marked internal separation; the fractional form has been preserved. | medium |
| 299 | Left diagonal margin | `couple de Killing` | The name's central letters are not wholly distinct. | medium |
| 299 | Line after (26) | `alors`, `comme un`, inserted `correspondant à`, `l'unique` | The insertion's relation to the retained words is ambiguous; no grammatical smoothing was attempted. | low |
| 299 | Parenthesis after `T = B₀ ∩ B₁` | `précédente` | The central and final strokes are faint. | medium |
| 299 | Lower paragraph, deleted line | `qui permet alors d'identifier U₁` | The cancelled verb phrase remains doubtful; the superposed replacement is recorded separately. | low |
| 299 | Replacement above deleted line | `isom.` | Abbreviation is faint; nearby formula supports only a tentative reading. | medium |
| 299 | Equation (27), above equals | `dfn` | Small abbreviation read as a definition marker. | medium |
| 300 | Top pagination | `451` / `351` | First digit is dark and malformed; no sequence-based correction has been made. | low |
| 300 | First and final occurrences near tensoring | `OPS` | Letters appear to abbreviate “on peut supposer”; the first is in the cancelled block. | medium |
| 300 | Middle cancelled block | Inserted `on a N₁\|D₀:` | Exact attachment and scope of the cancellation are uncertain. | low |
| 300 | Cancelled block, after `d'où` | Unreadable material | One unit estimated; the visible equations on either side are retained. | low |
| 300 | Cancelled block, final line of braces | `OPS` | Dense crossing obscures the word; two readings independently support this tentative abbreviation. | medium |
| 300 | Cancelled equation label | `(29)` | Label is crossed by the block-cancellation line. | low |
| 300 | Cancelled first line of braces, beside `O_S²` | Isolated `x` | Separate small mark below/right of the exponent could be an intended symbol or a local correction mark; it is not silently discarded. | low |
| 300 | End of cancelled block | `N₁ = (` followed by unreadable/incomplete material | No complete matrix is supplied in this abandoned occurrence. | low |
| 300 | Equation (29) | Second operator `σ⁻¹` | First letter is overwritten and resembles `ρ`. | medium |
| 300 | Deleted number above (30) | `(30)` | Densely overwritten; number is uncertain. | low |
| 301 | Deleted phrase after `D'autre part` | `on aura ρD₀ = σ…` | Last symbol is not recoverable. | low |
| 301 | First relation below that phrase | `ρD₀ = σD₀ = D₁` | The first equality sign has an overstroke that could be a not-equal sign. Both readings are recorded. | low |
| 301 | Upper-right replacement | `Nous choisissons … sections en Gl(2)) … satisfaisant …` | The final letters of `choisissons` are near the edge; `satisfaisant` is overwritten; the opening parenthesis paired with the visible closing one is not securely found. | low |
| 301 | Revision structure above (33) | Main relations followed by cancelled old lift-choice paragraph and an inserted replacement | Bracketing and movement strokes overlap. Only visibly struck passages are treated as deleted; the exact order of revision is not established. | low |
| 301 | Parenthesis after (33) | `elle =` / `elle m̄` | Two short parallel strokes may be the author's abbreviated sign for “même”; not expanded in the fragment. | low |
| 301 | Same parenthesis | Inserted `termes`; `σ̃` before `resp.` | The replacement is clearer than the heavily overwritten operator. | medium |
| 301 | Matrix (*) and determinant | `u, v, w` / `U, V, W` | Heavy overwriting makes letter case uncertain. | medium |
| 301 | Final prose line | `ambiguité` / `ambiguïté`; deleted `écrivant` | Accent placement and the struck verb are not securely legible. | low |
| 301 | Matrix (34) and final condition | `v, w` / `V, W` | Same case ambiguity as (*); the condition's unit-group membership is retained. | medium |

## 3. Abbreviations met

Expansions are proposed here only. The fragment retains the abbreviated forms. The lists are grouped by scan range so that uncertain forms, punctuation, capitalization, and local qualifications remain visible; an abbreviation can therefore recur in more than one group.

### Scans 283–287

| As written | Possible expansion (notes only) |
|---|---|
| `lin.` | linéairement / linéaire, according to syntax |
| `indép.` | indépendants / indépendantes |
| `i.e.` | id est, c'est-à-dire |
| `NB` | nota bene |
| `inv.` | inversible |
| `int` | automorphisme intérieur / conjugaison |
| `Tr` | trace |
| `det` | déterminant |
| `ss-g` (uncertain) | sous-groupe |
| `iso` | isomorphisme |
| `mono` | monomorphisme |
| `Cor.` (cancelled, uncertain) | corollaire |
| `m̄` | même |
| `th.` | théorème |
| `Th.` | théorème |
| `Dém.` | démonstration |
| `df` over `=` | définition / égalité par définition |

### Scans 288–292

| Written form | Probable meaning, for these notes only |
|---|---|
| `cf` | *confer*, “compare / see.” |
| `p.` | page. |
| `coeff` | coefficient. |
| `loc. cit`, `loc. cit.` | *loco citato*, at the place already cited. |
| `i.e.` | *id est*, that is. |
| `p.r.` (doubtful reading) | *par rapport*. |
| `dét.` | déterminants, in the instruction to take the determinants of both sides. |
| `NB.` | *nota bene*. |
| `ens.` | ensembles. |
| `tte` (doubtful reading) | toute. |
| `1-par.` | à un paramètre. |
| `dim` | dimension. |
| `def`, possibly `dfn` | definition label above an equals sign. Exact written forms remain distinguished or marked in the fragment. |
| `néc.` with raised `t` (doubtful reading) | nécessairement. |
| `\overline{\mathrm m}` (doubtful graphical readings) | même. |
| `Azumay.` (possible abbreviation) | Azumaya; the apparent final dot might instead be a reduced a. |
| `Tr` | trace. |
| `det` | déterminant. |
| `exp` | exponentielle. |
| `Gl`, `Sl`, `GP` | Notations for the linear, special linear, and projective groups; the scan expressly writes GP(1) in the inserted clause. |

### Scans 293–297

Expansions below are explanatory proposals only. They do not alter the transcription.

| As written / provisionally read | Proposed meaning | Scans / qualification |
|---|---|---|
| `s-groupe` | sous-groupe | 293; the abbreviation itself is doubtful. |
| `i.e.` | id est | 294–297; in 296 the inserted abbreviation is marked doubtful. |
| `tte` | toute | 294; doubtful abbreviation before “fibre”. |
| `cano.` | canoniquement / canonique | 294, margin; exact grammatical expansion depends on the neighbouring doubtful `isom`. |
| `isom` | isomorphe | 294, margin; uncertain reading. |
| `Aut` | automorphismes | 294, 296; mathematical operator, underlined in the manuscript. |
| `gr` | groupes | 294; some subscripts remain doubtful. |
| `Alg` | algèbres | 294, automorphism subscript. |
| `dfn` | définition | 295, above an equality; final letter uncertain. |
| `can` | canonique | 295, isomorphism-arrow annotation; uncertain. |
| `NB` | nota bene | 295, 297; underlined. |
| `inv.` | inversible | 295, lower-left NB. |
| `gén` with superscript `t` | généralement | 295, lower-left NB; doubtful exact abbreviation. |
| `car.` | caractéristique | 295, lower-left NB; doubtful surrounding words. |
| `Gl` / `GL` | groupe linéaire | 296–297; letter case is not secure. |
| `Mod` / `mod` | modules | 296, operator subscripts. |
| `local` with superscript `t` | localement | 296; exact abbreviation is doubtful. |
| `rg` | rang | 296. |
| `End` | endomorphismes | 296; underlined mathematical operator. |
| `unipot.` | unipotente | 297, rewritten proposition; word is partly crossed. |
| `Dém.` | démonstration | 297. |
| `m̄` (`\overline{\mathrm m}`) | même | 297, proof and insertion. |
| `OPS`, `OPS.` | on peut supposer | 297; retained in the compact manuscript form. |
| `alg` | algébriquement | 297, “corps alg clos”. |
| `Tr` | trace | 297. |
| `op` | opérateur | 297, deleted; uncertain. |
| `endom` | endomorphisme | 297, inserted; uncertain. |

### Scans 298–301

| As written | Tentative expansion |
|---|---|
| `endom.` (uncertain insertion) | endomorphisme |
| `Tr` | trace |
| `sss` | si et seulement si |
| `i.e.` | id est |
| `inv.` | inversible |
| `cqfd.` | ce qu'il fallait démontrer |
| `s.-groupes` | sous-groupes |
| `isom.` (uncertain) | isomorphisme |
| `dfn` | définition |
| `OPS` (uncertain) | on peut supposer |
| `resp.` | respectivement |
| `Gl` | groupe linéaire (notation, not expanded in the transcription) |
| `GP` | groupe projectif (tentative expansion of the manuscript notation) |
| `=` / `m̄` after `elle` (uncertain) | même |

## 4. Legibility and reliability

The main argument, many numbered displays, and most unoverwritten matrix entries are substantially more legible than the faint connecting prose and the revisions. The least secure regions are the upper cancellations and diagonal note on scan 283; the unnamed equation in scan 289; the cancelled bottom of scan 292; the densely underlined lower-left NB on scan 295; the rewritten proposition opening on scan 297; the first and last lines of scan 298; the cancelled derivation on scan 300; and the lift-choice replacement on scan 301. These areas retain explicit doubt or illegibility marks.

Short endings, rho/sigma overwriting, small inverse signs and indices, and distinctions between a plain, calligraphic, or double-stemmed letter remain recurring risks. In particular, the standalone projective-bundle symbol and several unit-object glyphs cannot always be assigned a secure alphabet. The manuscript's written `2 Tr λ`, unexpected commutator letters, and ambiguous basis-vector indices have been retained rather than resolved by algebra. Overlapping cancellation, insertion, and movement strokes also leave some uncertainty about revision order. The final scan was given the same full-page and enlarged-region inspection as the earlier pages, through its last matrix and unit condition.

## 5. Research notes — English

These notes are separate from the diplomatic transcription. Their scan references are filename-based locators in Grothendieck (1981), as described in section 1. They record the author's questions or expectations, claims requiring proof within the supplied excerpt, implications to pursue, and explicitly labelled ideas of the transcriber. Short quotations anchor notes about the author's words. “Unproved claim” describes the supplied passage; a proof may occur elsewhere in the manuscript. The proposed investigations are leads for checking against the rest of the manuscript and the literature, with no claim of priority or novelty. An uncertainty in the transcription is never resolved by a research note.

### Scans 283–287

#### 283-R1 — Scan 283, upper conditions and diagonal margin — Unproved claim

The margin says, with uncertain numerals, “29) est conséquence de 30)”. The written matrix calculation seems intended to connect the invertibility condition on `Tr N₁ρ` to fiberwise linear independence; the unreadable intervening prose prevents treating it as a complete recovered proof. A check would need to follow the permitted basis changes and normalizations over the base scheme, rather than only over a field.

#### 283-R2 — Scan 283, lower half — Unproved claim

The phrase “s'insère dans une suite exacte” introduces `1 → L₀ → B₀ → G_m → 1`, followed by the asserted action `u(N₀) = det(u)N₀`. The preceding definition uses `B′₀`, while the adjacent displayed symbols appear unprimed; identifying exactly which subgroup each assertion concerns is a prerequisite to checking the sequence and conjugation character. This is a notation question raised by the ink, not a proposed correction.

#### 283-R3 — Scan 283, final morphism — Own idea

One could check the final morphism from `B′₀` by computing its commutator coordinates in the displayed marginal normalization and then testing whether those computations descend independently of the chosen basis. Confidence: medium, because the page explicitly supplies both a normal form and a coordinate-free-looking morphism, but the subgroup definition is not fully present on this page. This is a suggested verification, not a claim of novelty or an established result.

#### 284-R1 — Scan 284, (79) and Corollaire — Unproved claim

“Induit un iso” asserts the isomorphism `B′₀ → X_{ρ,σ}`, and the corollary says each displayed projection “est un mono” with the specified determinant, trace, and invertibility conditions. This page states these results without supplying their proofs, while “Rappelons … pour mémoire” signals reliance on preceding work. A verification should reconstruct the inverse over general test schemes and check the precise open condition, without replacing a scheme-theoretic statement by a set-theoretic one.

#### 284-R2 — Scan 284, (80) and Scholie — Unpursued implication

The equality ending in “`1/μ`” suggests that, on the displayed invertibility locus, the third coordinate can be recovered from either projected matrix. The “transport de structure” then gives a way of comparing the induced group operations on the two images. This is a consequence worth spelling out from the asserted isomorphism; the explicit group law begins on the following scan.

#### 285-R1 — Scan 285, (81) — Unpursued implication

“En l'explicitant, on trouve” introduces the transported multiplication, whose first two commutator coordinates involve conjugation by `u′`. One can ask for a formula written entirely in the displayed coordinates `(ζ,η,μ)`, using the inverse of (79), and for the corresponding identity and inverse formulas. This would clarify how much of the auxiliary element `u′` remains necessary when using the equation scheme alone.

#### 285-R2 — Scan 285, (83), last paragraph — Unproved claim

The assertion that the map of solution schemes is “un épimorphisme” is attributed to “du th. précédent”, without a proof on this page. The next scan announces a canonical section, so the scope of the claim should be checked together with that construction, including its behavior under base change. No topology for the epimorphism has been supplied in the transcription where the manuscript itself does not specify one.

#### 286-R1 — Scan 286, (84)–(85) — Unproved claim

“On a une section canonique” supplies a proposed splitting of (83), taking values in the diagonal locus. The following phrase, read tentatively as “qu'on tâchera de déterminer aussi”, expressly leaves the description of all diagonal solutions for further work. Verifying that the displayed section solves (85) and determining whether its image exhausts any natural part of that locus are separate questions.

#### 286-R2 — Scan 286, unnumbered tuple and (86) — Unpursued implication

The discussion of “la solution générale” gives a parametrization by a common `u` and two independent elements from `T_ρ` and `T_σ`. The unnumbered tuple and the theorem's map use different inverse conventions, which can be compared algebraically without changing either transcription. One should check the precise uniqueness statement on the next page before interpreting this as a product decomposition.

#### 287-R1 — Scan 287, (87)–(90), final paragraph — Unproved claim

The asserted “isomorphisme” is reduced, for uniqueness, to `T_ρ ∩ B′₀ = T_σ ∩ B′₀ = {1}`, which the author says he “avait oublié d'expliciter dans (II)”. These intersection identities still need to be checked in the stated setting, including on test schemes with nilpotents if a scheme-theoretic result is intended. The transcription retains the proof's visible `α,β` without replacing them by the parameters from (88).

#### 287-R2 — Scan 287, (87), product parametrization — Own idea

The displayed product isomorphism invites checking the multiplication induced on the parameters `(u,a,b)` if a group structure is carried over from the solution construction; it does not by itself establish a direct product of groups. Confidence: medium, because the preceding scans explicitly transport a group law to the intermediate scheme, while the present formula gives only the displayed isomorphism and unique factorization. Any compatibility claim would require a separate calculation, rather than being inferred from the product notation.

### Scans 288–292

These items are reading leads, not claims of novelty or completed mathematical results. Page references identify the supplied scan files; quotations reproduce only short, sufficiently legible pieces of the source. References to earlier pages or future arguments are not claims to have inspected them.

1. **Scan 288, equations (94)–(95). Kind: unproved claim.** Grothendieck prefaces the explicit normalizing formulas with “sauf erreur.” A verification should multiply out both displayed 2×2 cases and separately establish, from the hypotheses of the preceding discussion, that the denominators δD and δ′U are units; the formulas alone do not state those hypotheses here (Grothendieck, 1981, scan 288).

2. **Scan 288, left margin beside (94)–(95). Kind: unproved claim (deferred work).** “Il faudra revenir sur ces formules dans le cas général” explicitly leaves the non-specialized construction to be revisited. A general treatment would need to explain how the chosen normalizations and their coefficients descend when the algebra or projective-line bundle is not given by a fixed matrix trivialization (Grothendieck, 1981, scan 288).

3. **Scans 288–289, final and opening paragraphs. Kind: conjecture (author's doubt/expectation).** The “seul ennui” is the factor τ∞^α in the earlier cited calculation, and he initially sees an apparent incompatibility while expecting the factor to have “de très bonnes raisons d'être là.” Scan 289 itself identifies the formerly allowed sign as the reason to enlarge the equation, so this should be traced against the earlier reference rather than presented as an unresolved conjecture at the end of the passage (Grothendieck, 1981, scans 288–289).

4. **Scan 289, paragraph before the second numbered equation. Kind: unproved claim (deferred work).** The intention to “reprendre la théorie précédente” concerns ζ=εηε₁(μ−1), with ε a section of the base ring and ε²=1. The earlier description of the solution space and its factorizations should be checked anew with this central parameter, including whether the same decomposition survives on every base and in every ε-fiber (Grothendieck, 1981, scan 289).

5. **Scan 289, final paragraph. Kind: own idea. Confidence: high for the elementary calculation; no novelty claim.** A test for the qualification about not assuming ε∈{±1} is A=F₂[t]/(t²), ε=1+t: direct multiplication gives ε²=1, while ε≠1=−1. This suggests testing the generalized equation with ε as a section of the group scheme of square roots of unity, rather than replacing it by a globally chosen sign; the explicit calculation is the reason for the confidence rating.

6. **Scan 290, first paragraph. Kind: unproved claim.** The assertion “revient à la donnée” relates the indicated forms of groups, an Azumaya algebra, and a bundle of projective lines. A formal proof should make the exact meaning of *forme* and the permitted descent data explicit, and check whether any central or outer twisting is being excluded or identified by the surrounding conventions (Grothendieck, 1981, scan 290).

7. **Scan 290, NB paragraph. Kind: unproved claim.** The canonical morphisms SG→G→PG “induisent des bijections” on the specified Borel and one-parameter subgroup data. A proof should identify the corresponding relative parameter functors and verify compatibility with arbitrary base change, rather than stopping at a bijection of geometric points (Grothendieck, 1981, scan 290).

8. **Scans 290–291, exp(λN), homothetic sections, and the conic. Kind: own idea. Confidence: medium.** It would be useful to formulate explicitly the quotient of the regular trace-zero, determinant-zero locus by invertible scalar multiplication and compare it with the conic in the checked projective bundle. The local matrix calculation suggests the construction, but representability, descent, and behavior over nonreduced bases would still need to be checked; this is a proposed formulation, not a claim of a new result.

9. **Scan 291, top insertion. Kind: unproved claim.** The inserted remark strengthens a∈Γ(S,O_S) to a∈Γ(S,O_S*) for two homothetic regular sections. A local proof should use their nonvanishing on every fiber to show that a is a unit, and should explain the passage between a choice of generator and the underlying line subbundle (Grothendieck, 1981, scan 291).

10. **Scan 291, final display. Kind: own idea. Confidence: medium.** The written trace identities contain `2 Tr λ` and `−2 Tr λ`; the transcription deliberately preserves them. An audit should check whether a particular convention for the scalar λ is in force or whether this is an uncorrected slip, comparing the trace identities with the simultaneously displayed determinant identities; the clear ink but incomplete surrounding convention explains the confidence rating.

11. **Scan 292, side remark beside (4). Kind: unproved claim.** The text asserts λ∈ΓG_m when regular unipotent sections are related by e′=1+λ(e−1). The proof should be obtained from the fiberwise regularity condition and the analogous unit-scalar observation on scan 291, with the possible distinction between local and global parametrizations made explicit (Grothendieck, 1981, scans 291–292).

12. **Scan 292, correspondence paragraph. Kind: unproved claim.** The phrase “en prenant les normalisateurs de ceux-ci” identifies the corresponding Borels from the additive subgroups. The needed relative assertion is an equality of subgroup schemes or subgroup functors under the hypotheses actually used, including compatibility with twisting and change of base (Grothendieck, 1981, scan 292).

13. **Scan 292, last paragraph and cancelled bottom. Kind: unpursued implication.** A chosen section gives the affine-line bundle E=\(\mathcal P\setminus\{x_\infty\}\), and the cancelled text explicitly mentions “vectoriel des translations.” The next issue to follow is the line bundle acting by translations and the relation between a second section, a trivialization of the associated torsor, and a further pinning; the cancelled passage is too uncertain to attribute a full classification statement to Grothendieck here (Grothendieck, 1981, scan 292).

### Scans 293–297

These are separate from the transcription. Source statements are attributed to the supplied manuscript identified as Grothendieck (1981); scan numbers refer to filenames, not the differing handwritten pagination. Quotations preserve only wording that is sufficiently legible to support the note. Questions about scope or counterexamples below are proposals for investigation, not claims of error, established results, or novelty.

1. **Scan 293, paragraph following (8). Kind: unproved claim.** The assertion “L est muni canoniquement d'une structure de fibré vectoriel” deserves a proof that is independent of the local choice of the regular unipotent section. One should track changes of the generator N, verify that the resulting scalar transitions glue the line bundle, and check that the normalizer action respects this structure. The formula (9) records the proposed intrinsic identification.

2. **Scan 294, left margin. Kind: unproved claim.** The margin identifies L with the “fibré vectoriel des translations” of the complementary affine-line fibration. A proof should describe the translation action in local coordinates and show that the identifications descend across changes of affine coordinate. The surrounding abbreviation `isom` is uncertain in the transcription; the quoted noun phrase is clearer.

3. **Scan 294, automorphism display (provisionally numbered 10). Kind: unproved claim.** After “et d'ailleurs on a”, the manuscript lists identifications of PG with several relative automorphism objects. To assess them, recover the exact subscripts and specify whether each object represents all group automorphisms, automorphisms preserving supplementary data, algebra automorphisms, or projective-scheme automorphisms. The required representability and compatibility with arbitrary base change are not proved on this page.

4. **Scan 294, same display. Kind: own idea. Confidence: high as a diagnostic calculation; interpretation remains open.** In the split case G = GL₂, test the map g ↦ det(g)⁻¹g against the precise automorphism functor meant in the display. A direct determinant calculation makes this map an involutive group homomorphism, so it is a useful candidate for detecting a missing restriction if the notation is intended to mean every group automorphism. The reading and earlier hypotheses must be settled before treating this as a counterexample to anything Grothendieck intended.

5. **Scan 295, (14)–(16). Kind: unproved claim.** The words “Cette section provient donc d'une section bien déterminée” assert a canonical lift from the projective root subgroup. A complete argument should show that the map from the specified L₁ to its projective image is an isomorphism of group schemes, rather than only a bijection on geometric points, and should explain how the lift determines the scalar in (16). This is distinct from merely imposing trace and determinant conditions on an arbitrary lift.

6. **Scan 295, lower-left NB. Kind: unproved claim.** The legible part says “λ₀ est uniquement déterminé” and gives a condition beginning “si 2 inv.”, followed by the more general regular-element condition. A proof should isolate the equation that forces uniqueness and explain exactly where regularity of 2 is used. The dense characteristic-two caveat is partly illegible, so no assertion about its full content is extracted here.

7. **Scan 295, same NB. Kind: own idea. Confidence: high as a test construction, not as a conclusion about the manuscript.** Over R = k[δ]/(δ²) in characteristic two, try rescaling a unipotent 2 × 2 matrix by 1 + δ. Since (1 + δ)² = 1, this gives a direct way to distinguish determinant/trace normalization from actual membership in a prescribed root subgroup L₁. Whether the rescaled matrix meets all of the manuscript's hypotheses must be checked separately.

8. **Scan 296, after (17). Kind: unproved claim.** “C'est le cas dès qu'on a une section x” is followed by the proposed construction of F as an extension of the structure sheaf by the translation line. A proof should construct the extension from the affine-line fibration, identify its projectivization with the given projective object, and establish the resulting group-scheme identification. The exact class of “formes” under discussion should be retained from the earlier manuscript context.

9. **Scan 296, (20)–(21). Kind: own idea. Confidence: medium.** Compare the line D° ⊗ D with the relative tangent or cotangent line along the corresponding section of the projective bundle. The reason to try this is the common Hom-type expression involving D and F/D, but the conventions for P(F) and checked P(F) can reverse the relevant dual. This is a proposed comparison, not an identification imposed on the transcription.

10. **Scan 297, proof after the equality of inverse images. Kind: unproved claim.** The reduction begins “OPS que S est le spectre d'un corps alg clos”. To justify this step over a general base, show that each condition under comparison is detected on geometric fibres and that this suffices for invertibility of the trace expression and for the required line-subbundle transversality. Equality of sections over a nonreduced scheme requires separate attention; the next-page calculation may supply the necessary scheme-level argument.

11. **Scan 297, proposition, condition (iii). Kind: unpursued implication.** The condition “c = λ₀ Tr ρ + Tr σ est inversible” suggests a principal open locus on which the two projective sections appearing in (i) are disjoint. It would be useful to formulate that open locus functorially and compare it with the moduli of the resulting ordered Borel or pinning data. This consequence requires a scheme-level version of the equivalence, not merely the geometric-point statement.

No explicit conjecture or future-work expectation was securely read in these five scans; the items above therefore remain claims to justify, implications to examine, or explicitly labelled suggestions.

### Scans 298–301

- **Scan 298, matrix calculation; kind: own idea.** A useful verification would separate the visible basis-vector indices from the invariant claim that invertibility of `Tr(N₁σ)` detects the transversality of `D` and `σD`. **Confidence: high that this is worth checking; reason:** the displayed matrices allow a direct calculation, whereas the indices in the following line are less legible and apparently do not immediately match a conventional column-vector reading. This observation is a check to perform, not an emendation of the transcription.
- **Scan 298, equations (23)–(25); kind: unproved claim.** The passage says that the two Borels have intersection a “tore (maximal).” The relative statement could be checked by locally identifying the two transverse lines with a decomposition of a rank-two module and then verifying descent over the base; this would also distinguish a maximal torus from a globally chosen split coordinate torus.
- **Scan 299, paragraph after (26); kind: unproved claim.** The text states that Borels transverse to `B₁` “correspondent biuni-voquement aux tores maximaux” of `B₁`. A proof over a general base would need to formulate the correspondence functorially, check the existence and uniqueness of the other Borel containing a given torus, and explain which fibrewise transversality hypothesis is used.
- **Scan 299, equation (27); kind: unpursued implication.** The choice of an additional section is expressed as an identification of the affine-line bundle `U₁` with the “fibré vectoriel L₁ de ses translations.” This invites a separate check of how the identification changes with the chosen section and what obstruction remains when no global section is given; the present page proceeds with the choice rather than analysing that obstruction.
- **Scan 300, equation (28) and following paragraph; kind: unproved claim.** The author concludes that “on a donc un épinglage complet de la situation” because `ε₁` is a section of `L₁*`. It would be useful to spell out the induced third section of the projective-line bundle, the resulting trivialization, and the exact dependence of that construction on the earlier regularity hypotheses.
- **Scan 300, equations (29)–(31); kind: own idea.** Check explicitly whether tensoring by `D₁^{⊗−1}` yields a canonical normalized rank-two model, or only a model after choices of generators. **Confidence: medium; reason:** the page supplies a decomposition and an isomorphism between its two line summands, but the relation between those data and the displayed named basis vectors merits a functorial comparison. This is a proposed verification, not a correction or a claim of novelty.
- **Scan 301, replacement paragraph and (33); kind: unproved claim.** The author chooses linear lifts so that `ρσ⁻¹ = −ε₁` and says this “détermine chacune des deux sections … en fonction de l'autre.” A fuller verification would specify the residual common scalar freedom and check that the proposed normalization is compatible with passage from the projective data to linear lifts over the entire base.
- **Scan 301, (*) and (34); kind: own idea.** Starting from the visible normalized matrix, compute the other lift from (33) and check the resulting formulas over rings, including characteristic two. **Confidence: high as a feasible check; reason:** the page gives explicit matrices and the unit condition on the lower-left parameter, so this can be tested directly without reconstructing faint prose. The significance of the minus sign and the canonicity of the normalization should be investigated, not assumed from field-valued examples.

## 6. Reference

Grothendieck, A. (1981). *La longue marche à travers la théorie de Galois* [Handwritten manuscript; cote 140-3, archive file described as “La Longue Marche, pages 293–650”; supplied scan files 283–301]. Université de Montpellier.
