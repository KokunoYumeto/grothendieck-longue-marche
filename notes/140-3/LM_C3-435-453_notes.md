# LM_C3-435-453 — Editorial and research notes

## 1. Scope, source, and numbering

This is a diplomatic transcription of all 19 supplied image files, in filename order, from scan 435 through scan 453. The text, formulas, diagrams, cancellations, insertions, and marginalia are transcribed from those images alone. No published transcription, other manuscript pages, or secondary literature was used to supply a reading. The research observations in Section 5 are separate from the transcription and are suggestions for subsequent verification.

The filenames and the page numerals visible in the images differ by one: file `scan435` contains the sheet numbered 434 at the foot, and file `scan453` contains the sheet numbered 452. The fragment therefore starts with `\scanpage{435}`, as requested, and preserves the visible handwritten numbers with `\mspage{...}`. The additional handwritten sequence 520–529 is also retained where it occurs. The separate printed Montpellier archive footer, including its printed page numeral, has been transcribed after each manuscript sheet; it is not treated as autograph text.

| Scan filename number | Upper handwritten number | Lower handwritten number | Printed footer number |
| --- | --- | --- | --- |
| 435 | — | 434 | 434 |
| 436 | 520 | 435 | 435 |
| 437 | — | 436 | 436 |
| 438 | 521 | 437 | 437 |
| 439 | — | 438 | 438 |
| 440 | 522 | 439 | 439 |
| 441 | 523 | 440 | 440 |
| 442 | — | 441 | 441 |
| 443 | 524 | 442 | 442 |
| 444 | — | 443 | 443 |
| 445 | 525 | 444 | 444 |
| 446 | — | 445 | 445 |
| 447 | 526 | 446 | 446 |
| 448 | — | 447 | 447 |
| 449 | 527 | 448 | 448 |
| 450 | — | 449 | 449 |
| 451 | 528 | 450 | 450 |
| 452 | — | 451 | 451 |
| 453 | 529 | 452 | 452 |

### Transcription conventions

The cursive composite groups are rendered as `\mathcal{M}` and `\mathcal{T}`; the individual groups `T_ρ`, `N′_σ`, `G`, and `G_m` retain their ordinary alphabets. The large script G/C sign on the early sheets and beneath SG on scan 452 remains explicitly doubtful. A small handwritten relation resembling “21” is represented as a rotated `\simeq` where the curved stroke is visible; genuine pairs of straight strokes remain equalities. Such alphabetic and relational decisions do not silently resolve the mathematical meaning.

Repeated equation numbers, incomplete parentheses, uncompleted diagram strokes, unprimed and primed symbols, surprising source groups, and the different signs in cancelled calculations are retained. No vertex has been invented below an unattached relation, and no arrowhead has been supplied merely because an exact sequence would normally have one. Marginal handwriting is placed at its corresponding reading position within `\margin{...}`; this is a transcription, not a facsimile of the page geometry. Drawn curves and leaders are reconstructed in TikZ, with doubtful attachments recorded below.

The inventory gives each element a stable `scan-element` identifier, including separately visible cancellations, annotations, and drawings within larger displays. Small formula annotations whose temporal status cannot be established are classified as displays rather than being asserted to be later insertions. Each printed archive footer has its own inventory row. All inventoried elements are marked `yes` because their content is represented; this flag is a coverage check, not a claim that every difficult reading is certain.

The LaTeX file is deliberately a fragment: it contains no preamble or definitions for the requested editorial macros. Its diagrams use `tikz-cd`, with escaped alignment separators inside macro arguments; its drawings use TikZ. A diagnostic wrapper supplies the editorial macros and the usual AMS mathematics, graphicx, and TikZ packages for compilation checks. The wrapper and preview PDF are not part of the requested three-file deliverable.

## 2. Table of doubts

Locations refer to approximate positions in the supplied images, not to line numbers in a printed edition. Confidence describes the visual reading: **high** means the particular feature was resolved relatively securely, **medium** means a plausible reading with residual doubt, and **low** means faint, overwritten, or materially ambiguous ink. Closely related repeated doubts may share a row. The inline `\unsure{...}` and `\illegible{...}` marks remain authoritative at their exact positions in the fragment; alternatives in this table do not correct the text.

| Scan | Approximate line / position | Reading retained | Alternative or qualification | Confidence |
| --- | --- | --- | --- | --- |
| 435 | Opening word | lié | The ending is a short, faint stroke; liée cannot be excluded. | medium |
| 435 | Opening line, after naturelle | à | The accent and main stroke are weak; the shape can resemble punctuation. | medium |
| 435 | Opening paragraph, ss-groupe | entier | Rapid medial and final strokes; the entire word is marked. | medium |
| 435 | (99), right-hand factor; repeated in (100) and extension paragraph | script G or script C | The large flourish and interior stroke do not securely identify the alphabet; do not normalize from the later quotient notation. | low |
| 435 | (100), canceled exponent of SR | + | The underlying mark is overwritten by the corrected circle. | low |
| 435 | Paragraph on a “section” | m-bar | The shorthand immediately after the quotation marks is darkened and partly merged with neighboring writing. | medium |
| 435 | Same paragraph, deleted object after de | script Tρ | The first script letter and precise subscript extent lie under a strike. | low |
| 435 | (101), canceled first word | mais | A long cancellation line crosses the middle of the word. | medium |
| 435 | (101), canceled predicate | ne commute plus | The beginning is especially faint, although commute and plus remain substantially visible. | medium |
| 435 | (101), second canceled line | donc on a une suite exacte | Long strike-through; exact positions of the short words are weak. | medium |
| 435 | Parenthetical after (101) | (trivial par définition … Ker Θ-tilde | No closing parenthesis is confidently visible at the right; none is supplied. | high |
| 436 | (102), second ε, deleted exponent | + | The exponent is almost obliterated; −1 is another possible underlying reading. The visible correction below is ε−1. | low |
| 436 | (104), label under b in first tuple | ΓN′σ or Γ* N′σ | A small star-like mark occurs between Γ and N; its status is unclear. | low |
| 436 | (104), second tuple, between b and λ | canceled ) | A small blackened sign lies above the comma; it resembles a crossed previous closing parenthesis. | low |
| 436 | (104), third tuple, immediately after λ | canceled ) | The canceled closer has a brace-like outline after overwriting. | low |
| 436 | (104), canceled condition in third line | det b / det a ∈ Γμ2 | Division slash and letters are crossed through; the ∈ Γμ2 portion is clearer. | medium |
| 436 | (104), beginning of last fiber-product line | canceled { | Several retraced strokes are present before \(T_\rho\); a brace is only a tentative reading. | low |
| 436 | Canceled (105), last group | script G or script C with circle | The main letter is canceled and intertwined with the enclosing correction strokes. | low |
| 436 | Final active diagram number | 105′ | The small prime is distinguishable from the canceled preceding (105). | high |
| 437 | (106), canceled upper-row left objects | 1, μ2 | The first object and most of the second are covered by zigzag cancellation. | low |
| 437 | After reference (96), deleted word | donc | A short dark cancellation obscures the central letters. | low |
| 437 | Same sentence, following deletion | on | Two faint horizontal strokes remain before fera. | medium |
| 437 | Same sentence | attention | The repeated tall t strokes and ending support attention; the middle is compressed. | medium |
| 437 | Same sentence, reference | (96) | Fresh enlarged inspection supports 96, rather than the earlier tentative 95. | high |
| 437 | After “Ainsi, on construit,” canceled first group | script Tρσ | Script letter and subscript remain partly visible through the strike. | medium |
| 437 | Same cancellation, second group | script Tρσ or Rρσ | The top flourish favors script T; it is not silently changed to the mathematically expected alternative. | low |
| 437 | Bracketed paragraph, immediately after et par là | (grâce à | Presence of opening parenthesis and exact accent/short-word strokes are uncertain. The closing double parenthesis after the numbered references is retained. | low |
| 437 | Parenthesis after et aussi, canceled word | simplifiant | Most of the word is crossed out; the insertion remplaçant is clearer. | low |
| 437 | Before the closing square bracket | ⇒ | A tiny blackened right-pointing sign remains; its exact decoration is uncertain. | low |
| 438 | (110), value of χ | δσ(b) or δ0(b) | The subscript is overwritten; the argument b is legible. | low |
| 438 | Below (111), before passage | par | Retraced first letters; the rest of the phrase “passage au quotient” is clearer. | medium |
| 439 | Main paragraph, structures | supplémentaires | The ending runs close to the right border and is faint. | medium |
| 439 | Main paragraph, ss-groupes | entiers | Tall t/l-like stroke and reduced ending permit this reading but not complete confidence. | medium |
| 439 | Argument of Mρσ after ss-groupes entiers | (w) or (ω) | The argument is a small w-like sign; a poorly formed integer-ring symbol cannot be ruled out, but is not supplied from context. The opening parenthesis is faint. | low |
| 439 | Underlined remark heading | Remq. or Rem. | A descending final stroke is visible; the exact abbreviation is uncertain. | medium |
| 439 | First remark line | le “composé” | The descender of p is clear. This is not transcribed as “somme.” | high |
| 440 | (116), canceled central vertical-arrow label | μ2 × μ2 | The middle of both factors is blackened; the replacement immediately above is clear. | low |
| 440 | Paragraph, en … aux composantes neutres | passant | The word is compressed and its middle strokes are faint. | medium |
| 440 | Paragraph after μ2 × μ2 and dash | idem | The opening tall stroke and following wave suggest idem; not fully secure. | medium |
| 440 | Last sentence | cart. et. cocartésiennes | A dot after et is visible and retained, without grammatical normalization. | medium |
| 441 | (117), below M+ | simeq SR_{rho,sigma} times SG | Final factor obscured by overwritten strokes | low |
| 441 | (117), arrow R0 to M0 | SG | PG | low |
| 441 | first prose line | oblique | No reliable second reading | medium |
| 441 | prose, s’identifient … | simplement | Word ending overwritten | medium |
| 441 | inserted phrase above à condition | à | Possible trailing stroke rather than a second à | low |
| 441 | (118), first right-hand factor | R | Overwritten letter, final R likely | medium |
| 441 | last prose line | aura | Other compressed verb reading possible | medium |
| 442 | opening adjective | délectable | Compressed strokes; l’utilité is not supported in context but first letters faint | medium |
| 442 | end of opening paragraph | regrettablement | Compressed medial and final letters | medium |
| 442 | Pour terminer ces gammes… | radicaux | Ending compressed; no dependable alternative | medium |
| 442 | inserted reference after lambda squared | (104) | (109) | low |
| 442 | parenthesis before expression de R0 | paraphrasée | paraphrase | medium |
| 443 | text before (121) | pleinement | joliment | low |
| 443 | before hom below (123) | h | One heavily inked cancelled initial | low |
| 443 | parenthesis beside the mu2 inclusion | et | de | medium |
| 443 | cancelled final paragraph, opening | On trouve | First short word crossed out at line start | low |
| 443 | cancelled final paragraph, terminal phrase | que + three illegible words | No reliable full reading after high-zoom inspection | low |
| 444 | (124), middle target | T_{sigma sigma} | T_{rho,sigma}; the first small subscript resembles sigma | low |
| 444 | kernel triple, first coordinate | lambda inverse | An overwritten a-like form | medium |
| 444 | cancelled connective before i.e. | c.à.d. | et | low |
| 445 | after first display | d’où | The cramped first word touches the next formula line | medium |
| 445 | R...SG=M before (128) | multiplication dot | An overwritten short sign immediately before SG | low |
| 445 | right sidebar below the faithful-action assertion | SN′σ/Tσ | SN′σ/STσ would be mathematically expected but no initial S is visible in denominator | medium |
| 445 | cancelled first line after Or on constate que | la section | First two words crossed through | medium |
| 445 | cancelled set expression | c sigma+d; second equation ends =0 | First c heavily overinked; source later writes g²=1, but here =0 is visible | medium |
| 445 | cancelled g² computation | 1 | Terminal numeral retraced; independently checked as 1 | high |
| 445 | cancelled lower brace, crossed-out left equations | c²=0; d²=1 | Heavily overwritten equations | low |
| 445 | cancelled lower brace, third line | cd=0 | First c overwritten | medium |
| 445 | cancelled enclosure lower boundary | donc; pour 2 inv. | donc si 2 inv.; cancellation line obscures word shapes | low |
| 445 | revised centre equality number | 131 | 129, apparently overwritten | low |
| 445 | revised centre equality, first fixed-point term | STσ^{μ₂} | ST glyphs overinked | medium |
| 445 | last cancelled line, final words | semi-régulier de | Last de independently confirmed; the next scan continues with O_S | medium |
| 446 | cancelled top definition, first line | mu_2 prime | Heavy local cancellation after Désignons par | medium |
| 446 | cancelled top definition, lower identification | Cent | Word beneath equality is locally overwritten and cancelled | low |
| 446 | cancelled top enclosure, last line | ce sous-groupe de | un sous-groupe de | low |
| 446 | connective after cancelled top block | finalt; savoir | finalement; soit (the first is probably abbreviated) | medium |
| 446 | under left parenthesis of Cent(M) in (128) | = sign | Two isolated short horizontal marks may instead be an altered underline | low |
| 446 | annotation under first factor of (130) | T_rho(Z) | Possibly overinked ST_rho(Z); no separate S is securely visible | medium |
| 446 | (131), integer argument delimiters | [Z] | (Z); left strokes look angular/square | medium |
| 446 | lower right node of (133), overwritten middle factor | old SN′σ, replacement μ₂ | The old glyphs and the replacement overlap heavily; possibly another old μ₂ notation | low |
| 447 | Main text, line 2, after “induit” | `sur` | The heavily retraced initial letter can resemble “d”; no separate cancelled word is recoverable. | medium |
| 447 | Main text, line 4 | `correspondant` | `correspondants`; final stroke is slight. | medium |
| 447 | Immediately below equation number (134) | `et` | A retraced or cancelled short annotation; letter shapes are insufficient to distinguish it securely. | low |
| 447 | After “pour mémoire” | `signalons` | The final syllable is compressed. | medium |
| 447 | Cancelled material left of Sigma, (135) | `\mu_2\times` | A differently shaped capital or group symbol followed by a multiplication sign; the cancellation interferes. | low |
| 448 | Upper-left diagonal note | `Où on définit` | `Qu'on définit`; the opening is cramped and slanted. | medium |
| 448 | First prose line, word after “une” | `liste` | `petite`; the leading loop and terminal strokes do not support an unqualified reading. | low |
| 448 | First prose line | `récapitulation` | `récapitulative`; the ending looks more like “tion” than “tive”, and it has not been silently regularized to fit “liste”. | medium |
| 448 | Paragraph after (134), end of second line | `passer` | The initial descending stroke is clear, but the middle letters are compressed. | medium |
| 448 | Same paragraph, next line | `revue` | The small initial strokes are weak. | medium |
| 448 | Text introducing (136) | `donnée familière` | Both endings are compressed. | medium |
| 448 | (136), horizontal map G_m to G | `j`, with hooked rightward map | Uppercase `J`; the short hook/head is indistinct, so the decoration and direction are less secure than the objects. | low |
| 448 | (136), bottom entry beneath SG | `0` | `1`; a small oval is visible, so the apparently anomalous zero is retained as the preferred reading. | low |
| 448 | (134), G_m to M | Hooked arrow labelled `j_mu` | The tail can resemble a second arrowhead; the main arrowhead at M is clear. | medium |
| 449 | First central paragraph, insertion above “somme” | `quotient de la` | Last article could read “le”; the insertion points before retained “somme”, while “amalgamée” alone has a clear strike. | medium |
| 449 | Same paragraph, inserted continuation | `immergeant` | `immergé`; the ending is contracted. | medium |
| 449 | List of four fundamental maps | `epsilon_3` | `epsilon_2`; the small subscript resembles both. | medium |
| 449 | After “quitte à vérifier”, cancelled word under new “que les” | `images` | A different word may be hidden by the superimposed correction; the placement of the replacement is uncertain. | low |
| 449 | Following “des quatre composés”, cancelled | `coïncident` | The central letters are partly overstruck. | low |
| 449 | Insertion above the same cancellation | `commutent` | Middle letters are joined and the first is retraced. | medium |
| 449 | Cancelled second row of (138), opening composite | `Theta_G j_rho` | Subscripts are partly overwritten. | low |
| 449 | Same cancelled row, first intermediate object | `S'T_rho` | `T_rho`; heavy zigzag cancellation obscures the prefix. | low |
| 449 | Same cancelled row, second intermediate object | `T_rho` | An adjacent symbol may be merged into the cancellation. | low |
| 449 | Same cancelled row, final map label | `j` | `J`; the glyph has no visible dot. | medium |
| 449 | Parenthesis below (138) | `compatibilité` | `compatibilités`; final short stroke is ambiguous. | medium |
| 449 | Revised prose above (138), immediately before `epsilon in Gamma mu_2` | Cancelled `epsilon` | An equivalence-like `≡` glyph; it has three short horizontal traces and is distinct from the following retained epsilon. | low |
| 450 | Number of first display | `(139)` | `(135)`; the terminal digit visually resembles 5, so sequential numbering has not been used to remove the doubt. | medium |
| 450 | (141), initial cancelled symbol | `Theta` | A different circled or retraced letter could underlie the cancellation. | low |
| 450 | (141), short cancelled line below the map | `epsilon_3 j_sigma` | The subscript on j and some of the first symbol are obscured by zigzag strokes. | low |
| 450 | (142), last triangle, horizontal arrow | Two-headed-direction arrow, `leftrightarrow` | Ordinary rightward arrow with a sharply retraced starting stroke; the visible small left-pointing head has been retained. | medium |
| 451 | Opening paragraph, after “s'explicitent” | `donc` | `alors`; the small word has a tall first stroke and compressed middle letters. | low |
| 451 | (144), annotation above the parenthesized equality | `dfn` | `déf`; the final character looks like a short n, but the abbreviation is compressed. | medium |
| 451 | Above “cubiques” in the final paragraph | Inserted and underlined `prismatiques --` | The central letters are compressed; the exact role of the long lower stroke as underline or insertion guide is not fully clear. | medium |
| 451 | First parenthesized reference after “cubiques” | `95` | `05`; the first digit is heavily retraced and lacks the usual long descender. | low |
| 451 | Last word before (147) | `clivages` | A reading beginning `divi-` is less likely because the later g has a clear descender and the ending is es. | medium |
| 452 | (148), two vertical strokes | Hooks at the lower ends; labels `\mu_2\times\mu_2` | The hooked lower ends are visible, but no upper arrowheads are safely visible; the strokes are rendered without heads. | low |
| 452 | Upper-right note | `c'est ici la définition de ...` | The end of *définition* reaches the scan border. | medium |
| 452 | After (149) | `définissons` | Final letter sequence is abbreviated by continuous strokes. | medium |
| 452 | (150), beneath SG | `\mathcal{G}_{\rho,\sigma}^{+}` | The script letter can also be read C. | low |
| 452 | Parenthetical lists below the sequences | `itm` | `item`; the manuscript abbreviates the middle of the word. | medium |
| 453 | First line | `iso` | The abbreviation does not clearly show a final period. | medium |
| 453 | (152), second membership sign | `\in` | Retraced/overwritten sign. | medium |
| 453 | Right annotation, (152′) | `\delta'_\sigma` | `\delta_\sigma`; the mark above the letter is entangled with a long stroke. | low |
| 453 | Right annotation, final argument of first equation | `delta_rho(a)` | a is plain here, although earlier b is underlined; no underline has been supplied. | high |
| 453 | Right annotation, final sentence | `conn.` | Contracted handwriting; do not expand in the transcription. | medium |
| 453 | Upper diagonal note | `égalités (152)' caractérisent` | `relations` is less consistent with the visible descending stroke. | medium |
| 453 | Upper diagonal note, last two lines | `compte si on n'a pas oublié, dans (135) des hyp^{ses} à faire...` | A further enlarged reading identifies the additional word as probably *oublié*; the connecting clause, reference, and abbreviated noun remain weak. | low |
| 453 | Main paragraph after (152) | `manquent cependant, dans l'optique des points entiers` | The q-descender supports *manquent*; the short article and the crowded next line remain marked. | medium |
| 453 | Membership conditions beside u, alpha, beta, alpha_0, beta_0, f | `T_0` | T is heavily retraced. | medium |
| 453 | Unnumbered relations at the foot, curved strokes at the left | Two return arrows towards the alpha and beta lines | Endpoints and exact curvature are difficult to separate from the large brace and the underlining of U. | low |
| 453 | Right-hand i.e. beside the first two bottom relations | `u = alpha overline(a) = beta b` | The short stroke is above a; b has no safely visible underline. A vertical separator stands after the two equations on the left. | medium |
| 453 | Second diagonal NB | `de ces 6 quantités (153) ... multiplicatif` | Independent rereading supports *multiplicatif*. The nearby (153) belongs to this marginal reference, not to an independently numbered main display. | medium |
| 453 | Final marginal pair of formulas | `\varepsilon`, `\sigma` | Enlarged comparison favors a plain sigma followed by an opening parenthesis, without a separate exponent on sigma; the small strokes remain doubt-marked. | low |
| 453 | Last marginal sentence | `mais peu nous chaut ici` | The short word *peu* and *chaut* are compressed. | medium |

## 3. Abbreviations and compact notations encountered

Expansions below are interpretive aids confined to these notes. They have not been substituted into the transcription. Variants are retained because punctuation and abbreviation practices differ across the sheets; some rows record a compact mathematical notation rather than a lexical abbreviation.

| Form on page | Proposed expansion or interpretation | Scan(s) |
| --- | --- | --- |
| m-bar, \(\overline{\mathrm m}\) | même | 435–440 |
| hom.; hom | homomorphisme(s) | 435–440 |
| ss-groupe; ss-groupes | sous-groupe; sous-groupes | 435–440 |
| mod | modulo | 435–440 |
| p. | page | 435–440 |
| Ker | noyau, kernel | 435–440 |
| can.; can | canonique(s) | 435–440 |
| pr₁; pr₂ | première et deuxième projections | 435–440 |
| det | déterminant | 435–440 |
| Remq. or Rem. | remarque | 435–440 |
| isom | isomorphes | 435–440 |
| cart. | cartésiennes | 435–440 |
| sup. | supérieure(s) | 435–440 |
| inf. | inférieure(s) | 435–440 |
| idem, doubtful | idem, the same statement | 435–440 |
| cf. | confer / compare | 441–446 |
| G_m | Multiplicative group notation; not expanded in transcription | 441–446 |
| SG | Special subgroup notation; meaning depends on earlier pages | 441–446 |
| sup. | supérieures | 441–446 |
| hom | homomorphisme (without a written final full stop) | 441–446 |
| can | canonique | 441–446 |
| id | identité | 441–446 |
| i.e. | id est | 441–446 |
| c.à.d. (cancelled and uncertain) | c’est-à-dire | 441–446 |
| inv. / inv | inversible | 441–446 |
| iso | isomorphisme | 441–446 |
| Cent | centre | 441–446 |
| Ker | noyau | 441–446 |
| finalt (uncertain) | finalement | 441–446 |
| cf | confer | 441–446 |
| p. | page | 441–446 |
| dim | dimension | 441–446 |
| `resp.` | respectivement | 447 |
| `Cent` | centre | 447 |
| `cart` | cartésien | 448 |
| `det` | déterminant | 448 |
| `Ker` | noyau (kernel) | 449 |
| `hom.` | homomorphismes | 449 |
| `triv.` | trivial | 449 |
| `can` / `can.` | canonique | 449 |
| `incl.` | inclusion | 449 |
| Long horizontal stroke under “comme composé” | Repetition mark for the words immediately above; it is reproduced as a stroke. | 449 |
| `can` | canonique | 450 |
| `det` | déterminant | 450 |
| `dfn` (doubtful reading) | définition | 451 |
| `Ker` | noyau (kernel) | 451 |
| `iso` | isomorphismes | 452–453 |
| `itm` / `item` | item, in the sense of similarly; reading remains uncertain | 452–453 |
| `déf` | définition | 452–453 |
| `Ker` | noyau; the author uses the Latin/English-root abbreviation | 452–453 |
| `etc` | et cetera | 452–453 |
| `NB` | nota bene | 452–453 |
| `i.e.` | id est | 452–453 |
| `conn.` | connaissance | 452–453 |
| `hyp^{ses}` | hypothèses; uncertain compressed form | 452–453 |
| `§` | paragraphe / section | 452–453 |

## 4. Legibility and limits

The broad mathematical formulas and most diagram vertices are more legible than the faint running French. The least secure material is the underlying text of cancellations, the large script G/C signs on scans 435–436, the layered prose on scans 437 and 449, the crowded labels in cubes (116)–(117), the cancelled centre calculation on scan 445, and the diagonal notes on scan 453. Several of these readings were compared independently against enlarged or rotated crops; unresolved letters, exponents, and attachment points remain marked rather than reconstructed from the expected mathematics.

Particular care was taken with the non-Cartesian-face warning on scan 437, the incomplete stroke in (121), the source's different cancelled endings `=0` and `=1` on scan 445, the revised centre formula, the small terminal symbol that looks like `0` in (136), and the missing circle in one occurrence of M in (146). The last page was checked again for its marginal abbreviations, the word *oublié*, the bar over a, the vertical separator, and the absence of a separate exponent on σ in the last formula. Those checks improve the readings but do not make this a critical edition: the low-confidence passages still require comparison with the images.

## 5. Research notes — English; separate from the transcription

All manuscript references in this section are to Grothendieck (1981), using the supplied scan filename numbers mapped in Section 1. Quoted phrases identify what is actually written; a doubtful quotation is identified as such. A label such as “unproved claim” means that the verification is not supplied in the cited passage, not that the claim is false or that its proof is absent elsewhere. The author's questions and expectations are distinguished from proposed checks and the editor's own ideas. These notes are not a literature review, do not establish priority or novelty, and never supply or correct words in the transcription.

### 1. Scan 435, (99)–(101): the commuting factors and their intersection

**Kind: unproved claim.** The manuscript states \(R_{\rho,\sigma}\cap SG=\mu_2\), says that \(R_{\rho,\sigma}\) commutes with \(SG\), and labels the latter “trivial par définition.” A complete check would recover the earlier definition of \(\widetilde\Theta\), verify the stated intersection as a group object, and explain precisely why its kernel centralizes the displayed \(SG\). The canceled line before the final commuting assertion should not be silently promoted into an additional premise.

### 2. Scan 436, (104)–(105′): explicit presentation and square-map pullback

**Kind: unproved claim.** The chain introduced by “on l'obtient” passes from a tuple with \(f\) to determinant conditions and then to fiber products; the final square is labeled “diagramme cartésien.” Verification should supply the actual mutually inverse maps for each displayed identification, their compatibility with the group law, and the recovery of the auxiliary sign \(\varepsilon'\). The image visibly uses \(\delta_\sigma\) without a prime in places where later notation might suggest another convention, so this check should begin with the manuscript's definitions rather than a normalized formula.

### 3. Scan 437, warning after (106): identifying the non-Cartesian faces

**Kind: unpursued implication.** The insertion explicitly says “n'est pas cartésienne,” followed by “ni la face inférieure,” while the preceding page labels a particular square Cartesian. This invites a precise identification of every face referred to by the earlier cubes (95)–(96), so that the pullback assertion for (105′) is not accidentally transferred to a neighboring face. A useful comparison would record which quotient or kernel description accounts for the difference; the earlier cubes must be consulted before formulating that comparison as a theorem.

### 4. Scan 438, (111)–(114): descent of the canonical morphism

**Kind: unproved claim.** After “on peut construire” \(\mathcal M_{\rho,\sigma}\) by (102), the author says the homomorphism \(\Theta\) is obtained by passage to the quotient from the two displayed homomorphisms. A proof would check agreement on the embedded \(\mu_2\), the resulting descent, and the exactness of \(1\to SG\to\mathcal M_{\rho,\sigma}\to\mathcal T_{\rho,\sigma}\to1\). The order and orientation of the maps in (112)–(114) provide the concrete data for that verification.

### 5. Scan 439, main paragraph: recovering the original sections

**Kind: conjecture / expectation.** The abstract construction is said not to require the sections \(\rho,\sigma\), but additional, more delicate structures “permettront peut-être de les retrouver.” This is a reconstruction question: which added subgroup data recover which equivalence class of the original sections? The small parameter attached to the subgroup is pale and doubtful, so the remark should not yet be treated as a precisely stated theorem about integral points.

### 6. Scan 440, final paragraph: the lateral universal properties

**Kind: unproved claim.** The author states that the lateral faces are “cart. et. cocartésiennes,” while excluding the upper and lower faces. A proof should specify the category in which these universal properties hold and verify each face from the subgroup inclusions and quotient labels in (116), including the claimed common quotient \(\mu_2\times\mu_2\). The phrase about passage to neutral components also requires the precise base and component conventions from the surrounding manuscript.

### 7. Scans 436–438, determinant and square-map constructions

**Kind: own idea. Confidence: high as a verification strategy, not as a conclusion about the manuscript.** Test the presentations on rings with square-zero elements as well as on field-valued points, with particular attention to the kernel of the square map. The reason is that the diagrams explicitly involve \(\mu_2\), and checks on reduced points alone may fail to distinguish group-object phenomena relevant to the claimed pullbacks. This is a proposed test, not an assertion of an error or of novelty.

### 8. Scan 438, quotient by \(SG\) and the three characters in (110)

**Kind: own idea. Confidence: medium.** Ask whether \(\mathcal T_{\rho,\sigma}\) has a universal property for characters of \(\mathcal M_{\rho,\sigma}\), beyond the displayed quotient property. If \(SG\) has no nontrivial characters under the precise hypotheses, every such character would factor through that quotient, making (110) a starting point for a character calculation. The confidence is conditional because the necessary property of \(SG\), and its behavior over the permitted bases, is not established on these six pages.

### 9. Scan 441, after (117) — unproved claim

“s’identifient simplement aux produits directs”: the text asserts direct-product identifications for the two positive middle terms. A verification would require checking the multiplication map, the triviality of the relevant intersection, and functorial inverse maps, rather than only comparing the displayed quotients.

### 10. Scan 441, (118) and final paragraph — unpursued implication

The replacement by “les μ₂-revêtements” is said to make the parallel face satisfy the same product behavior. The exact effect on the Cartesian and cocartesian properties of the surrounding cube warrants checking over bases where μ₂ is not étale.

### 11. Scan 442, (118)–(119) and final paragraph — unproved claim

“on a un unique hom (118)”: a canonical lift of the scalar diagonal to R⁰ is asserted using the fiber-product presentation. To verify uniqueness, one should specify the map to the auxiliary G_m factor along with the square compatibility; a lift through a μ₂-cover alone does not establish uniqueness.

### 12. Scan 442, opening continuation from (118) of preceding scan — unproved claim

The replacements are said to make “les quatre carrés” Cartesian and cocartesian. Both universal properties should be verified in the intended category of group schemes or group sheaves, and the treatment of the μ₂-intersections should be made explicit.

### 13. Scan 443, (122)–(123) — unproved claim

“d’où des décompositions en produit direct”: a section of κ is displayed before the direct-product decompositions. In addition to the section identity, the proof needs the scalar image to centralize SR; this condition distinguishes the stated direct product from a merely semidirect product.

### 14. Scan 443, (121) — unpursued implication

The announced “diagramme de suites exactes” contains only one completed horizontal row and a downward stroke in this scan. Comparison with the μ₂-cover square on neighboring pages could determine which further exact rows or vertical arrows were intended, but they must not be supplied in the transcription.

### 15. Scan 443, (123) — own idea

One can test the proposed splitting functorially over rings with nilpotents, especially in residue characteristic 2, by writing the inverse as r ↦ (r i_R(κ(r))^{-1}, κ(r)). Confidence: medium, because this gives the expected inverse if the displayed section is central and the notation indeed refers to group-scheme morphisms; those hypotheses still need verification from the manuscript.

### 16. Scan 444, (124)–(126) — unpursued implication

“μ₂ envoyé ‘diagonalement’ dans le produit triple”: the kernel calculation supplies a presentation of the quotient by a diagonal central subgroup. It would be useful to track functor-of-points exactness separately from group-scheme or sheaf exactness, because surjectivity on arbitrary ring-valued points need not be automatic from a quotient presentation.

### 17. Scan 444, right margin of (124) — own idea

The determinant annotation has a potentially ambiguous placement of squares and appears to label both underbraces by λ². Recompute the scalar determinant factors after confirming the convention for det and the source exponents; this may be a genuine manuscript slip or only ambiguous notation. Confidence: medium, because the inked exponents are visible but the manuscript’s determinant conventions may account for them.

### 18. Scan 444, (127) and final line — unpursued implication

The triple scalar map is identified with the earlier map (48), “qui n’est autre que (48)”. Checking that identification requires following all three μ₂ inclusions and their intersections through the canonical splitting, including the elementwise diagonal kernel in (125).

### 19. Scan 445, (128), question mark under the middle factor — conjecture / question

The question mark under “Cent(SN′σ)” identifies the remaining centre calculation. The ensuing invariant-subgroup argument and the cancelled elementwise computation should be distinguished as successive stages of the author’s working.

### 20. Scan 445, inserted (130) and revised centre equality — unproved claim

The replacement statement “Tσ^{μ₂} ≃ G_m” is used to obtain the centre by intersecting with STσ. A proof would need the actual μ₂-action on the torus over the permitted base, including its scheme-theoretic fixed subgroup.

### 21. Scan 445, cancelled computation and final cancelled paragraph — own idea

The abandoned argument singles out invertibility or semi-regularity of 2. Compare its elementwise equations with the replacement fixed-group argument over characteristic 2 and rings with 2-torsion; this could clarify why the revision was made, but does not establish any failure of the final claim. Confidence: medium, grounded in the author’s visible cancellations and retained fixed-point formula.

### 22. Scan 445, deduction of centre from R and SG — unpursued implication

The statement “Comme R ... commute à SG” reduces the centre of M to that of R. To formalize it for group schemes, verify that the displayed product R·SG=M is interpreted in a topology that permits descent of centrality, and that the projective group has trivial centre in the intended setting.

### 23. Scan 446, (130)–(132) — unproved claim

The return to “sections entières” identifies the relevant integral torus/normalizer points with cyclic groups of orders 6 and 4 and the scalar factor with ±1. A full verification requires the earlier definitions of the absolute modular case and the integral structures; these identifications are used here rather than rederived.

### 24. Scan 446, (133), strict inclusions — unpursued implication

The “diagramme d’inclusions strictes” separates the three-dimensional groups R and R° from the two-dimensional centre-related subgroups, with horizontal quotients μ₂² and μ₂. Investigating its behaviour on rational or integral points requires distinguishing group-scheme quotients from the quotient of point groups.

### 25. Scan 446, (131) and (132) — own idea

The displayed decompositions give centre point groups of orders 24 and 48, respectively, if read literally as products of the listed cyclic factors. Trace the inclusion of the former in the latter and its dependence on the two sign characters; this is a calculational check, not a claim of novelty. Confidence: high for the abstract orders, medium for the precise inclusion until the earlier maps are fixed.

### 26. Scan 447, opening paragraph and (134) — unproved claim

The continuation says the two horizontal arrows induce “des isomorphismes” on integral points in the absolute modular case. A verification would need the preceding square and explicit maps, not only the displayed abstract group types; it would also need to distinguish isomorphisms of point groups from statements about the underlying group objects.

### 27. Scan 447, final paragraph and (136) — conjecture / expectation

The phrase “on aura un homomorphisme canonique” announces the map into `M_{rho,sigma}(Z-hat)/Sigma`. These lines state the expected construction without supplying it; the construction and the precise role of the three sign factors should be checked in the subsequent manuscript.

### 28. Scan 447, (135)–(136) — own idea

One could test whether the quotient by the displayed sign subgroup removes the ambiguity in simultaneously choosing the three lifts suggested by the preceding decomposition. Confidence: medium as a research direction only, because the manuscript explicitly juxtaposes the three sign factors and the quotient target, but this page does not identify the ambiguity or prove that it is exactly `Sigma`.

### 29. Scan 448, paragraph after (134) — unproved claim

The statement that the diagram “se reconstruit” from the listed data announces a reconstruction whose compatibility and uniqueness conditions require checking. The next pages begin specifying these conditions, so the assertion should be tracked as a claim with its proof distributed over the continuation rather than treated as established by the diagram alone.

### 30. Scan 448, (134)–(135) — own idea

A consistency check should distinguish the symbol `delta'_sigma` in (134) from the unprimed `delta_sigma` in both occurrences in (135), without altering either reading. Confidence: high that this is a useful editorial check because the primes are visibly different here; low as to whether the difference is deliberate notation, an abbreviation in the recap, or an authorial slip.

### 31. Scan 449, first central paragraph — unproved claim

The revised description inserts “quotient de la” before “somme” and adds that `mu_2` is immersed diagonally. The exact product or sum construction, and the sense in which the displayed diagonal subgroup is a kernel, merit checking against the earlier definition; the revision should not be erased by substituting a standard categorical term.

### 32. Scan 449, second central paragraph — unproved claim

The passage reduces the description of four maps to their composites with the four indicated homomorphisms, “quitte à vérifier” additional conditions. The corrected words mention commutation and a trivial product of values on images of an element of `Gamma mu_2`; a proof would need the appropriate universal property and the precise diagonal relation.

### 33. Scan 449, (137)–(138) — own idea

Compare the visibly written target `T_sigma` after `i_rho` in (137) and the target `G_m` in the last row of (138) with the corresponding definitions elsewhere before adopting either in a mathematical reconstruction. Confidence: high as an editorial verification task because the displayed ink is clear enough to raise these questions; no claim is made here that either is an error.

### 34. Scan 450, after (139) and (140) — unproved claim

Both composite lists are followed by “compatibilités triviales”. The statement leaves the actual verification to the reader; it should be checked against the diagonal relation and commutation requirements on the preceding page, with all displayed source groups retained until possible authorial slips are assessed.

### 35. Scan 450, (143) — unproved claim

The displayed map with components `(chi, epsilon_3, epsilon_2)` is called an “épimorphisme”. A proof needs the ambient category of groups or group schemes and the intended topology: pointwise surjectivity over every ring is not supplied by this statement alone.

### 36. Scan 450, (142)–(143) — own idea

A useful verification would compute the image of each of the four earlier factor maps under the three components in (143), using the preceding composite tables, and identify what kind of local lifting proves the asserted epimorphism. Confidence: medium, since the tables furnish a natural route to this check, but the precise category and hypotheses are not all restated on this page.

### 37. Scan 451, (144) — unproved claim

The formulas give the two determinant composites in terms of `chi` and `epsilon_3`. Their verification can be reduced to the preceding factorwise composite tables, but the actual multiplication and descent through the diagonal quotient are not written out here.

### 38. Scan 451, final paragraph and (147) — unproved claim

The phrase “d'où les carrés cartésiens et cocartésiens” asserts both universal properties and refers back to several earlier diagrams, followed by the direct-product expressions called “clivages” in the preferred reading. A proof should verify both properties separately in the relevant category and identify the splitting maps, rather than infer them solely from the displayed isomorphism types.

### 39. Scan 451, marginal note beside (147) — unproved claim

The note says “dont le sens est évident sur le diagramme (134)”. This points to the earlier four-factor recap as the source of the splittings; the explicit identifications and their compatibility with all subgroup inclusions should be recovered from that diagram.

### 40. Scan 451, (145)–(147) — own idea

One could organize the named subgroups as inverse images of kernels of the three scalar/sign components, then check their intersections before testing the displayed product decompositions. Confidence: high as a verification strategy because the kernels are explicitly written here; no assertion is made that the anomalous missing circle or the order of superscripts is mathematically intended.

### 41. Scan 452, (148)–(150) — unpursued implication

The sheet places the central quotient presentation beside the definitions of four quotient groups, introduced by “d'où des structures d'extensions.” A useful subsequent check is to verify all four quotient identifications simultaneously at the level of group functors, including how the common central kernel meets the subgroups marked + and a circle. The displayed exact sequences alone do not state the topology in which quotient and exactness are intended.

### 42. Scan 453, upper diagonal margin beside (152) — unproved claim / explicit request for verification

The clear portions read “Il faudrait expliciter” and “il faudrait faire la vérification”; the intervening statement says that the equalities (152′) characterize the group as a subgroup of `G × T_ρ × N′_σ`. A proof would need both necessity and sufficiency of the equations, not merely the construction of the three component maps. The final clause of this annotation is too uncertain for a more specific attribution.

### 43. Scan 453, (152′) — unpursued implication

The author says that the auxiliary quantities are “déterminées par la seule conn.” of the three displayed images. This suggests checking that the scalar and sign maps factor through the proposed triple-coordinate realization and that the resulting map is injective on the relevant functor of points. Recovering the auxiliary characters does not by itself prove that the original group element has been recovered.

### 44. Scan 453, unnumbered relations at the foot and adjacent membership conditions — own idea

Compare the two coordinate systems by substituting the displayed relations and tracking the permitted choice of `u` and `f`; a residual central ambiguity could distinguish a parametrization from a unique normal form. **Confidence: medium.** The reason is that the page explicitly supplies several auxiliary variables and change-of-variable relations, but does not establish uniqueness on this sheet.

### 45. Scan 453, second diagonal NB — unproved claim

The revised reading of the underlined word is “multiplicatif”: the note distinguishes `u` from the six listed quantities by this property. A proof would require writing the group law in the auxiliary coordinates and checking the asserted multiplicativity; the others should not be assumed multiplicative merely because they occur in the same list. The word is still doubt-marked in the transcription.

### 46. Scan 453, last diagonal note — unpursued implication

The phrase “On pourrait introduire” precedes additional xi-, eta-, g- and h-expressions involving rho and sigma. One can investigate which expressions are invariant under changes of the auxiliary coordinates and whether they encode useful compatibility or obstruction data. The small coefficients and the sigma reading must first be settled; no invariant or cocycle identity is asserted here.

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished handwritten manuscript, Montpellier archive, cote 140-3; supplied image files for scans 435–453]. Université de Montpellier. Title, date, and archival identification follow the supplied task documentation; the readings themselves use only the attached images.
