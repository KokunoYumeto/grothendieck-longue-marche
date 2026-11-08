# LM_C4-134-152 — Notes to the diplomatic transcription

## Source, scope, and reading conventions

This package transcribes all 19 supplied scan files, 134–152, from Alexander Grothendieck's *La Longue Marche à travers la théorie de Galois* (1981), Montpellier archive cote 140-4. The supplied images are the sole transcription source; no published transcription or text from outside this package was used to complete a reading. The source reference appears at the end of this file.

Scan numbers follow the supplied filenames. They differ from the small handwritten and printed archive numerals, which run from 133 to 151. The author's visible top-of-page numbers are 715–723 on alternate scans, 135–151; only these are encoded by `\mspage`. The lower-left handwritten archive numerals are retained as marginal matter. Every printed institutional footer is copied, word for word, into non-rendering LaTeX comments immediately after its scan's manuscript text, so that the archive apparatus remains distinct from the manuscript.

The transcription is a fragment, without a preamble or macro definitions. It uses the requested editorial macros with ordinary LaTeX mathematics, TikZ, and tikz-cd; an enclosing document must define the editorial macros and supply the usual mathematics and graphics packages. A temporary wrapper with those definitions was used to syntax-check all 19 scans. This check does not settle a doubtful reading or guarantee the layout of another editor's wrapper.

The handwritten large double-curved group letter is rendered `\mathfrak G`, distinct from ordinary `G_{\rho,\sigma}`; the permutation-group letter is rendered `\mathfrak S_3`. The larger arithmetic group letter is represented by `\mathcal M`, and the module by `M`. The long Jacobian glyph is represented by `\mathcal J`. These typographic identifications follow the visible forms; ambiguous particular occurrences and overwritten accents remain marked. The tilde in `G_{\rho,\widetilde\sigma}` belongs to the subscript. The barred wavy m is consistently rendered `\overline{\mathrm m}`, without expanding it in the transcription.

## 1. Table of doubts

Line positions are approximate manuscript positions, not lines in the LaTeX file. Formula numbers, neighboring words, and marginal positions provide additional locators. Confidence describes the visible ink, not the plausibility of a mathematical argument. Alternatives remain candidates for checking; none is a silent correction. A single row may cover repeated instances of the same uncertain glyph or overwritten subscript on one scan.

| Scan | Approximate line / position | Reading retained | Alternative / difficulty | Confidence |
|---|---|---|---|---|
| 134 | 2, parenthesis | composé | Initial letters overwritten / ligatured | medium |
| 134 | 2, middle group | tilde over calligraphic M | bar over calligraphic M | medium |
| 134 | 3, deleted start of b) | Γ′, double-tilde calligraphic M / M | First symbol and order heavily cancelled; the final denominator may be Γ | low |
| 134 | (293), deleted quotient | double-tilde calligraphic M / M | Dense cancellation; quotient reading tentative | low |
| 134 | b), deleted quotient | double-tilde calligraphic M / M | Overwritten symbols | low |
| 134 | b), underlined word | fidèlement | Compressed ending may be abbreviation | medium |
| 134 | definition marks at (293) and b) | dfn | The small final n and tall f favour this abbreviation rather than déf | medium |
| 134 | E paragraph, before sur lequel | deleted que | Only short crossed strokes remain | low |
| 134 | E paragraph, final line | E-torseur | First letter visually E; possible M; no mathematical correction made | low |
| 134 | last two lines | profinite Z with star | Lower part overwritten, no confidently separable earlier symbol | medium |
| 135 | 6, deletion after on a | donc | Short cancelled word | medium |
| 135 | category at lines 13–14 | fraktur X′ | Handwritten alphabet not fully determined | medium |
| 135 | equivalence after (U,S₃) | ≃ | Additional small mark below and left may be part of an overwritten arrow | low |
| 135 | after insertion oubli | des op. | An independent reread supports op. from the position of the p-descender; des remains compressed. The earlier possibility du gr. was rejected after comparison. | medium |
| 136 | 3, deleted phrase | double-tilde calligraphic M, followed by extension | Barred m followed by cette extension; the two upper strokes and the tall lower humps cannot be segmented securely, and a further loop is overwritten. Both tentative readings are retained in place. | low |
| 136 | 4, group glyph | fraktur G, with + and wedge | Calligraphic rather than fraktur alphabet possible | medium |
| 136 | 4, subscript on μ | fraktur G | Plain G; the two curved strokes favour the same Gothic glyph as the numerator | medium |
| 136 | 4, deleted de H | H | Cancelled base letter / mark unclear | low |
| 136 | conjecture, last two lines | est | Retraced letter at beginning | medium |
| 136 | before C'est | deleted Et | Small heavily retraced mark | low |
| 136 | “les classes d'isomorphie des…” | classes | Could be a compressed different noun; no semantic repair | medium |
| 136 | inserted extension, relation | ≃ | Retraced relation could be equals | low |
| 136 | (294), first H⁰ term | deleted tilde Γ | Small cancelled symbol before S₃ | low |
| 136 | (294), middle term | Γ | Heavy retracing obscures any prior mark | medium |
| 136 | (295), parenthesis | et | Short ligature; “dû” less likely | medium |
| 136 | (295), subgroup | Lρ | Lj | low |
| 136 | (295), coefficient in parenthesis | hat M | bar M | medium |
| 136 | before Calculons | deleted Et | Interlaced strokes | low |
| 137 | 1 | ramène | Flattened medial strokes | medium |
| 137 | extension glyph near top | fraktur G | Possible calligraphic G | medium |
| 137 | subscript on μ in that extension | fraktur G | Plain G; the small double-curved glyph favours the Gothic letter | medium |
| 137 | (296), lower row, both coefficients | hat M | bar M; the overmarks are nearly flat | medium |
| 137 | theorem, symbol before U∞ | deleted X | Z; dense multiple cancellation | low |
| 137 | theorem, parenthesis | deleted sans | Initial strokes overlapped | medium |
| 137 | theorem, inserted replacement | oubliant | oubli with terminal attachment stroke | medium |
| 138 | deleted formula after “gros” | H¹(ΓQ,hat M) ≃ H¹(Γ | Multiple cancellations; final expression unfinished | low |
| 138 | Tate-module subscript | infinity | asterisk; tiny angular sign | medium |
| 138 | “nullité de” coefficient degree | i | Retraced exponent | medium |
| 139 | First displayed homomorphism, upper quarter | `\mathfrak G_{\bullet}^{+\wedge}` | The large double-curved capital is most probably a Gothic G; its tiny lower mark may be a dot, a subscript 0, or a terminal stroke. | low |
| 139 | Quotient in second display | `\mu_{\mathfrak G}` | The small subscript has a cramped double-curved form; its alphabet is uncertain. | medium |
| 139 | Right side of second display | `\mathfrak G^{+\wedge}/\mu_{\mathfrak G}` | Broad group glyph and the exact subscript on the kernel remain difficult; plus and completion mark are retained. | medium |
| 139 | Third display, denominator in definition of tilde-M | `\mu_{\mathfrak G_\bullet}` | The terminal lower mark could instead be a 0 or part of the preceding glyph. | low |
| 139 | Above the first G in “Le passage de…” | Deleted `\sim` | A short overwritten curved mark is present; its intended accent cannot be determined confidently. | low |
| 139 | Last text line, after “puisque le” | Deleted “élément” | The cancellation crosses most of the letter bodies; only a tentative word reading is possible. | low |
| 139 | Bottom interlinear insertion, after `\{1,` | `\omega_{H^+}` | The Greek letter and the very small subscript are crowded; omega is the best visual reading. | low |
| 139 | Bottom insertion before “de” | Deleted `H^+` | A second group-letter expression is crossed out; the superscript is particularly unclear. | low |
| 140 | Middle paragraph, before underlined “opération” | Deleted “ho” | Could be an unfinished abbreviation beginning “hom”; no additional letter is certain. | low |
| 140 | Middle paragraph, after “de” and the arithmetic M | Deleted “de H” | The last glyph and the relation of its long strike to the preceding short word are unclear. | low |
| 140 | Middle paragraph, after “ou mieux” | Deleted `\widetilde{\mathcal M}` | The canceled group letter is heavily overwritten by the replacement above it. | low |
| 140 | Diagram (298), label below the quotient group | `N'_{1,1}=\mathcal M_{0,3}` | The right side is overwritten; the M-like form and 0,3 are the preferred reading. | low |
| 141 | Upper paragraph, after “on était parti” | “de” | The very short mark could be an abandoned connector rather than a completed word. | low |
| 141 | Upper paragraph, parenthesis after §48 | “dans” / “des” | Only the initial and terminal strokes can be distinguished reliably. | low |
| 141 | Upper paragraph, “du type Lie” expression | `\mathrm{SL}(2,\widehat{\mathbb Z})'` | The final short stroke may be a prime or a neighbouring parenthesis/pen stroke. | medium |
| 141 | Upper paragraph, source of the quotient | `\mathfrak G_{0,3}^{+\wedge}` | The large capital and first subscript are overwritten; plus and completion marks are visible. | low |
| 141 | Immediately left of displayed homomorphism | Deleted `\mathcal M` | Only an M-like remainder can be read from the cancellation. | low |
| 141 | Before “l'ext.” below the display | Deleted `\mathcal M` | A separate heavily canceled M-like symbol; its original index, if any, is not recoverable confidently. | low |
| 141 | Bottom paragraph, group of lacets | `\Pi_{0,3}^{\wedge}` / `\Pi_{0,2}^{\wedge}` | The last subscript digit is a small curved mark compatible with 3 or 2. | low |
| 142 | Second paragraph opening | “présume” / “pense” | “présume” best fits the succession of small strokes, but the centre of the word is compressed. | medium |
| 142 | Second paragraph, after “de ce fait” | “n'offre” | The end of the verb is a short trace; “n'offrirait” is not supported by enough visible strokes to transcribe it. | medium |
| 142 | Interline and following word, middle paragraph | Inserted “bi-” followed by “revêtement” | The insertion is clear; the beginning and ending of the main-line word are compressed. | medium |
| 142 | First matrix-group expression of second paragraph | `\mathrm{GL}` | The first letter is overwritten and could be S; GL is a tentative reading. | low |
| 142 | Parenthetical alternative quotient | `\mathfrak G^{+\wedge}` | The broad double-curved capital is provisionally Gothic G; no extra lower index can be established. | medium |
| 142 | After underlined “non pas” | `\mathfrak G_{0,3}^{+\wedge}` | The alphabet and small lower indices have less clear ink than the following SL expression. | medium |
| 142 | Interlinear parenthesis above “comme un groupe” | “comme l'était” | The short verbal phrase is compressed and partly connected to its attachment stroke. | low |
| 142 | Last two lines, “sur quoi … opère” | “ça” / “il” | The pronoun is reduced to two short marks; both are retained as possibilities. | low |
| 143 | Upper paragraph, before “quasi-courbe” | “tte” / “tt” | The terminal tiny trace may be an e or part of the abbreviation's horizontal stroke. | medium |
| 143 | Added name of the curve, before tilde-X | Deleted `E` | The canceled form is E-like but contains several overlapping strokes. | low |
| 143 | Formula (299), canceled symbol at left | Deleted `M_2` | The lower stroke suggests 2; the entire symbol has been repeatedly crossed. | low |
| 143 | Formula (299), base of tilde-X | `S` / `B` | The base letter has a strongly looped, apparently overwritten form. The visible B-like shape is not silently replaced because the surrounding base is S. | low |
| 143 | Formula (299), subscript on first Z | `S'` / `B'` | The letter is similarly overwritten; the prime is visible. | low |
| 143 | Formula (300), canceled symbol at left | Deleted `M_2` | An M-like form and lower 2-like trace are the only recoverable parts. | low |
| 143 | Formula (300), twist factor | `\widehat{\mathbb Z}(1)` | There is a tiny mark below the capital; it may be a lower terminal stroke or a small index. An independent index cannot be read confidently. | medium |
| 143 | Lower paragraph, after “locaux” | `;` | Several tiny points suggest a semicolon, but the punctuation is not certain. | low |
| 143 | Lower paragraph, after “dépend” | “fonctoriellement” | Initial and central letters support this reading, but the final syllables are abbreviated into a long stroke. | medium |
| 144 | 5, after (301) | `chgts` | `chgt`; compressed final strokes in the abbreviation | medium |
| 144 | 18 | `jacobienne généralisée` | `jacobien généralisé`; the article appears `la`, but both word endings are rapid strokes | medium |
| 145 | after (304), first inline Tate-module expression | `T_\infty(J^0)` | The subscript resembles `\alpha` in this occurrence; the alternatives are retained in the text | medium |
| 145 | 10 | `du groupe` | `de groupe`; the vowel is compressed | medium |
| 145 | 11 | `Y-a-t-il` | `Y a-t-il`; the horizontal stroke beside the `a` may belong to the letter | medium |
| 145 | (302)–(303) | Directed arrows and bare connecting strokes | Several connectors have no separately visible arrowhead; those are transcribed as bare strokes, without supplying a direction from exactness | high |
| 146 | upper unnumbered display, three base indices | `\deleted{\mathbb Q}\inserted{\mathbb Z}` | Dense superimposed loops and diagonal strokes; a Q-to-Z correction is the best reading, but the original base letter is not fully separable | medium |
| 146 | upper display, deletion immediately before `P^1` | `\mathbb A_{\mathbb Q}` | The crossed symbol could have another base index; retained as a tentative symbolic reading rather than an illegible word | low |
| 146 | 3, at right edge | `augmenté` | `s'envoyant`; the beginning and ending of the word are compressed and the final stroke meets the edge | medium |
| 146 | (305), coefficient module under `J^0` | `M_0` | `M_\mathbb Z`; the subscript is heavily retraced | low |
| 146 | left margin, equality decoration | `df` | `dfn`; the final flourish may be a separate letter | medium |
| 146 | (306), source base index | Q overwritten by Z | The Z is visible; an underlying Q is only partly recoverable | low |
| 144–148 | Jacobian notation throughout | `\mathcal J` | Plain `J`; the looped handwritten glyph does not establish a separate alphabet with confidence. Script J is used consistently with the adjoining scans as a tentative alphabet convention | medium |
| 147 | (308), deleted codomain exponent and map value | `{0,1,\infty}`; the cyclic ratio triple | Very heavily crossed ink: the triple is a tentative reading supported in part by visible subscripts, not treated as a confident restoration | low |
| 147 | (308), product defining `J^0` | `\mathbb G_m\times_{\mathbb Z}M` | The written operator looks like a cross rather than a circled tensor sign; it has not been normalized | high |
| 147 | upper diagonal note | `via`; `non` | The first word is retraced; `pas` is a possible alternative to `non` | medium |
| 147 | lower diagonal note, opening | `Calcul correct, car il repose sur cet` | The compressed strokes after `Calcul` and after `il` are especially insecure; this proposed reading is not inferred from the mathematical validity of the argument | low |
| 147 | lower diagonal note, middle | `il semble ici qu'être` | `il semble n'y être`; the phrase is grammatically awkward and its rapid strokes do not support a confident normalization | low |
| 147 | lower diagonal note | `scindages` | An independent reread identified a long g-descender after the initially abbreviated-looking strokes; the full word is retained tentatively | medium |
| 147 | lower diagonal note, above the second cohomology expression | isolated `S` followed by a dash | Its attachment is unresolved: it may correct the adjacent cancelled S in the formula rather than belong to the prose; it is retained at its visible reading position | low |
| 147 | lower diagonal formula | `H^0(S,\mathfrak S_3,J^0)\simeq H^1(\mathfrak S_3;H^0(S,J^0))\simeq0` | The first degree reads 0, the second 1; these were retained despite their asymmetry. A cancelled initial S in the second argument list, the base S versus S_0, and the terminal leftward mark remain doubtful | low |
| 147 | invariant calculation, second set | `x\in\mathbb Z^{*\{0,1,\infty\}}` | The superscript set is visibly repeated after the scalar x and has been kept | high |
| 147 | final paragraph, opening and deletion | `(la`; cancelled `de` | Marginal ink partly overlaps the opening; the short cancelled word before `cubique` is very compressed | low |
| 148 | first display | `H^*` | `H^n`; the superscript is dark and partly touches the following parenthesis | medium |
| 148 | exact sequence, first nonzero arrow | possibly cancelled `\simeq` | The raised mark is very heavily retouched; an uncancelled isomorphism decoration remains possible | low |
| 148 | exact sequence, parenthetical term below right | `H^0`; `M_0` | `H^q`; the degree and coefficient subscript are tightly retraced | medium |
| 148 | Picard-group calculation | `Pic(S)^2` | `Pic(S_0)^2`; a possible small zero merges into the lower stroke of S | medium |
| 148 | left margin | underline on `pas` | The long emphasis stroke extends to the right of the diagonally written word; association to `pas` is inferred from its position | medium |
| 148 | (309), both module subscripts | `M_0` | `M_\alpha`; the looped subscript is heavily overwritten | medium |
| 148 | (309), first coefficient I | `I` | `I_0`; an extra lower loop may be a subscript or an uncancelled earlier pen stroke | low |
| 148 | parenthesis after (309) | `I=J^0(S)` | `I=\mathcal J^0(S)`; this shorter J is visibly unlike the long Jacobian glyph elsewhere, and no alphabet identification is forced | medium |
| 148 | same parenthesis | `quelc.` | `quelq.`; the final abbreviated consonant is reduced to a small turn | medium |
| 148 | insertion after `quelc.` | `ou I=H^1(S,\mathbb G_m)=Pic(S)` | The curved left line is treated as part of the insertion connector; it could additionally be an opening parenthesis | medium |
| 148 | (310), first argument of `H^0` | cancelled `S_0` | A surviving `S` superimposed on the cancelled base is also possible; the two states are not separable with confidence | low |
| 148 | final numbered display | `(310)` | Middle digit is retraced and partly overwritten | medium |
| 149 | 1, after “Soit” | Deleted `\mathcal J` | A small heavily overdrawn symbol; its original alphabet is uncertain. | low |
| 149 | 1, right edge | `M_0` | `M`; the lower-right stroke is cut by the black border. | low |
| 149 | 13, after `\mathcal J^*_S→\mathcal J^0_S` | “qui le factorise” | “que la factorise”; the small pronouns and final verbal strokes are compressed. | low |
| 149 | 14 | “jacobiens” | The opening and ending are legible, but medial strokes are abbreviated. | medium |
| 149 | 16, below the first `\mathcal J^0_S` | Inserted `\mathcal J^*_S` | An upward caret links this lower expression to the unretracted source; not treated as a hat over J. | medium |
| 149 | Diagonal NB, reference | “695” | A possible minute prime is not securely visible. | medium |
| 149 | Diagonal NB, before (312) | “défini” | The last strokes are compressed. | medium |
| 149 | Diagonal NB, (312), extreme right | `x_0+x_1+x_∞=0` | The final symbol and closing edge lie against the border; `0` is marked uncertain. | low |
| 150 | 1 | “Brauer” | The name's middle/final strokes are rapid. | medium |
| 150 | 4, after “soit” | Deleted `X` | A crossed letter immediately before `U`; possibly merely a retracing of the end of “soit.” | low |
| 150 | (313), identification below `J^0` | Vertical isomorphism sign, encoded by `\wr` | A wavy stroke beside a vertical straight stroke; direction is not an arrow. | medium |
| 150 | (313) and following line | `M_0` | The subscript is heavily retraced and resembles `4`; retained as a doubtful `0`. | medium |
| 150 | Line after (313) | `p_*` | `\rho_*`; descender and loop do not discriminate reliably. | medium |
| 150 | Parenthesis beginning “loc.” | Overlined `isom.` | The bar is visible over the initial part; extent and exact abbreviated letters are uncertain. | low |
| 150 | Same parenthesis | `\mathbb Z^2` | The superscript is hook-shaped. No closing parenthesis is securely visible before the following comma; none has been supplied. | medium |
| 150 | “déduit de” | `M_{0 S}` | The zero and S are crowded and partly retraced. | medium |
| 150 | Number at map `U→J^0` | `(314)` | The final digit is overwritten; it is not silently regularized. | medium |
| 150 | Last prose line, deletion | “un” | The short canceled word is heavily inked. | low |
| 150 | Last prose line | “composé” | The final syllable runs into the right margin. | medium |
| 151 | Heading | “homomorphisme” | “homorphisme”; the middle syllables are compressed. A separate heavy line under the initial `hom` is preserved. | medium |
| 151 | (315), below its source, canceled set | `{z∈ΓG_m ∣ z−1 inv}` | `Γ` is particularly insecure beneath the crossing strokes. | medium |
| 151 | (315), source rewritten below | `(G_m\{1})_{S_0}` | The left curve overlaps a canceled brace, and the closing parenthesis is not clearly separable from the closing set brace. Both parentheses are marked doubtful. | low |
| 151 | (315), label below target brace | `J^0` | A tiny inked symbol; no secure complete reading. | low |
| 151 | (315), vertical cancellation left of `U_1` | Deleted `J^1` | The symbol is extensively overwritten; this is a tentative reading only. | low |
| 151 | (315), cancellation at the upper right of the coordinate triple | Deleted `\mathbb Z` | The overwritten superscript or marginal symbol cannot be securely identified; its position is preserved. | low |
| 151 | Before “isomorphisme” | Deleted “il est” | The first short word is at an oblique angle above the more legible “est.” | medium |
| 151 | Before “correspond” | Deleted “est prolonge” | The lower canceled word may be another verbal form; the long medial descender prompted “prolonge.” | low |
| 151 | Large braced display number | `(316)` | `(314)`; the final digit looks like a crossed vertical stroke, so the numbering has not been silently regularized. | low |
| 151 | Source of the map in the braced display | `widehat U_{0,3}` | `overline U_{0,3}`; a triangular mark is retraced by a thick horizontal stroke. | medium |
| 151 | Set below `widehat U_1` | `widehat P^2_{S_0}` | `P^2_{S_0}`; a small accent above P and the overwritten subscript are uncertain. | low |
| 151 | Last line, canceled target before `M'_{1,1}` | `Spec` | The long descender looks like p, but cancellation obscures the surrounding letters. | low |
| 152 | 3, before “de Legendre” | “tapis” | A tall first letter, a long p-like descender, a dot and final s are visible; the medial vowel is compressed. | medium |
| 152 | 3, canceled denominator of the quotient | “modulo sym.” | Very heavy horizontal cancellation; “symétrie” is another possibility. This is a tentative reading of the remaining strokes, not a supplied mathematical denominator. | low |
| 152 | 9, “à partir de” | “là” | “lui”; the final upper stroke may be an accent or a dotted i. | medium |
| 152 | 10, first canceled mathematical fragment | `\wedge_{S_3}` | The small upper stroke is overwritten, though the doubled-S glyph and subscript three remain recognizable. | low |
| 152 | 10, canceled word before the comma | “et” | “ou”; cancellation obscures the short word. | low |
| 152 | 10, last canceled mathematical object | `J^0` | A minute lower dot may be a subscript or incidental ink; no additional subscript is supplied. | medium |
| 152 | Annotation below (318) | “avec notations de p. 720” | “en notations”; the first word has been reduced to a few separated strokes. | medium |
| 152 | Last line, extreme right | “axiomatiq” | Only this stem is securely within the image; the end meets the black border. “axiomatique” or “axiomatiquement” may be intended, but an unseen ending has not been supplied. | low |

## 2. Abbreviations met

Expansions are supplied only here. Dots and other marks are not inserted into the transcription where they are absent in the scan. Variant written forms are kept distinct when useful.

| As written | Probable expansion or interpretation |
|---|---|
| i.e. | id est |
| dfn | définition / equality by definition |
| Im | image |
| Aut | automorphismes |
| hyp. | hypothèse |
| n° | numéro |
| géom. | géométrique. |
| hom | homomorphisme; no period is supplied where the scan has none. |
| isom | isomorphisme. |
| rev.; rev | revêtement; both punctuated and unpunctuated forms occur |
| op. | opérations, if the doubtful reading is right. |
| ext | extension. |
| `ét` | étale |
| `p.` | page |
| `11°)` | numbered subsection, onze |
| `ext.` | extension |
| `ens` | ensemble |
| `pt` | point |
| `resp` | respectivement |
| `\overline{\mathrm m}` | même |
| `car.` | caractéristique |
| `tte` or `tt` | toute; exact abbreviated form uncertain |
| `pts` | points |
| `syst` | système |
| `iso` | isomorphismes |
| `cat.` | catégorie |
| `\S` | section or paragraphe |
| `cf` | confer / compare |
| `iso.` | isomorphisme |
| `chgts` | changements |
| `comm.` | commutatif |
| `NB` | nota bene |
| `df` / `dfn` above `=` | définition / by definition |
| `isom.` | isomorphisme |
| `inv.` | invariant in the fixed-point calculation (scan 147); inversible in the hypothesis on 2 (scan 152) |
| `p. ex.` | par exemple |
| `quelc.` / `quelq.` | quelconque |
| `i.e` | id est; c'est-à-dire |
| `diag.`; `diag_3` | diagonale; diagonale dans un produit de trois facteurs |
| `mod` | modulo |
| `dim` | dimension |
| `loc.` | localement |
| Overlined `isom.` (doubtful reading) | isomorphe |
| `hom.` | homomorphisme |
| `inv` | inversible |
| `sym.` (doubtful, canceled) | symétrie |
| th. | théorème |
| § | section or paragraphe |

## 3. Legibility and limits

The main prose and most active formulas are readable, but many word endings are reduced to short strokes. The least secure material is the abandoned quotient notation on scan 134; the cancellation and small inserted formulas on 136; central-kernel annotations on 139–140; overwritten base letters on 143 and 146; the two diagonal notes on 147; retouched cohomology symbols on 148; and the cancellations and border-adjacent writing on 149–152. The lower diagonal note on 147 remains particularly uncertain even after rotated enlargements and an independent reread. On scan 152 the last word reaches the black border: only the visible stem “axiomatiq” is retained, without supplying an unseen ending.

Each scan was read whole, transcribed, reread against the image, and inventoried. An independent comparison additionally checked scans 134–138 and the dense marginal notes on 147; selected subsequent pages were checked again during assembly. The process improved several small readings, but it cannot make the remaining overwritten ink certain. Tentative readings are retained in place, including canceled mathematical material; the doubt marks should be consulted before quoting those passages as definitive.

Apparent surprises have been preserved: the E-shaped letter in “E-torseur,” repeated “classes,” the correction of “trois” to “deux,” the asymmetrical cohomology degrees in the lower note on 147, repeated or overwritten numbering, and open or unfinished expressions. Plain connecting strokes in diagrams remain headless where no arrowhead is securely visible. Marginal emphasis strokes are reproduced in TikZ. Paragraph continuity across scan boundaries is retained, including the broken word between 137 and 138. The inventory includes the main text, subordinate displays, diagrams, marginal matter, insertions, deletions, emphasis drawings, and printed footer apparatus.

## 4. Research notes — English

These notes are separate from the diplomatic transcription and never determine its readings. Every scan locator below is a pinpoint reference to Grothendieck (1981), as identified in Section 5. “Unproved claim” means that a proof is not supplied at the cited location; it does not mean that the claim remains unproved elsewhere in the manuscript or in the literature. Questions and expectations are grouped under “conjecture.” Suggestions labelled “own idea” are exploratory, with confidence and a reason; they are not presented as established results or claims of novelty. Quoted words with paleographic uncertainty must be read with the corresponding table entry.

### Scans 134–138

- **Scan 134, conditions a)–c) and paragraph beginning “Pour un tel quotient”; unpursued implication.** The manuscript reconstructs E as “l'ensemble de tous les scindages” and relates conjugation to its torsor structure. A separate verification could formulate precisely the equivalence between quotients satisfying these three conditions and the relevant affine actions; the visible “E-torseur” has not been corrected to another group name in the transcription.
- **Scan 134, final paragraph; unproved claim / backward reference.** “Nous avons vérifié les trois relations (292)” refers to evidence outside this package. Any mathematical audit must recover those hypotheses and the earlier construction rather than treat the present backward reference as a proof contained in these scans.


- **Scan 135, “un objet de la catégorie”; unproved claim / backward reference.** The preceding corollary is invoked to construct an object “à isom unique près” from the surjective homomorphism. A proof audit should check the exact notion of morphism in that earlier category, since existence of a cover and uniqueness of an isomorphism are different assertions.
- **Scan 135, last paragraph; unproved claim, continued on scan 136.** The tower of Fermat covers is said to supply “très exactement un tel objet”. Verifying this requires matching the group action and geometric abelianization with the conditions just stated; this is a question about the construction, not a suggestion to replace the manuscript's formulas by a known version.


- **Scan 136, first paragraph; conjecture / authorial expectation.** “Je n'aurais certes pas suspecté” that the indicated subextension “soit scindée” records how the Fermat tower prompted the splitting claim. Recovering the exact subextension and its central quotient from preceding pages would clarify the geometric input into this surprise.
- **Scan 136, double-marked paragraph; conjecture.** “La conjecture qui se présente tout de suite” is that the two proétale covers are isomorphic, with a unique isomorphism. It should be tracked even though the following pages return to its resolution; the uniqueness assertion has its own cohomological content.
- **Scan 136, (294)–(295) and diagonal note; unpursued implication.** The displayed exact sequence and invariant-vanishing claim reduce the displayed H¹ to Galois invariants in H¹(S₃,hat M). A proof reconstruction should specify the coefficient topology and the meaning of continuous cohomology rather than silently import a discrete-coefficient version.
- **Scan 136, final equality; unproved claim.** The equality identifying H¹(S₃,hat M) with H¹(S₃,M) tensor profinite Z is asserted here without a separate argument. Establishing it would require a justified passage between the integral module, its completion, and degree-one cohomology.


- **Scan 137, opening question; conjecture / question.** The author asks to calculate “H¹(S₃,M) ?” and then invokes the preceding study of splittings. This local question is answered on the same page; its logical dependence on the earlier splitting theorem should remain explicit.
- **Scan 137, (296)–(297); unproved claim / backward reference.** The integral vanishing is extracted from the assertion that two splittings are conjugate by a unique element. A reconstruction should separately identify how H⁰ governs the stabilizer of a splitting and H¹ governs conjugacy classes, then justify the completion step used on the second line.
- **Scan 137, theorem; unpursued implication.** The theorem specifies geometric universal abelianization together with an arithmetic and permutation-group descent structure, and concludes uniqueness of the isomorphism after continuation onto scan 138. The restriction to that descent structure is essential to check; the bare geometric cover has a different automorphism problem.
- **Scan 137, theorem; own idea.** Compare the groupoid of descent data with the groupoid of splittings of the displayed extension, keeping automorphism groups rather than only isomorphism classes. **Confidence: medium**, because the manuscript explicitly couples unique conjugacy with vanishing in degrees zero and one, but the precise equivalence needs the omitted surrounding definitions.


- **Scan 138, first paragraph after theorem; unproved claim / backward reference.** The author says existence was obtained “de deux façons”, through the Fermat tower and the general theory of §49 III. Comparing the two constructions requires recovering that earlier theory and the hypotheses satisfied by each object; uniqueness here supplies the proposed identification.
- **Scan 138, last paragraph; unpursued implication.** The author emphasizes that the vanishing follows “sans rien connaître sur ΓQ”. This points to a formal sufficient criterion: vanishing in degrees zero and one for the permutation action can eliminate the corresponding extension-class ambiguity before any arithmetic cohomology is calculated.
- **Scan 138, display beneath “gros”; own idea.** Check the meaning of the completion symbol over Q* against the earlier definition of T∞, and distinguish full profinite completion from a completion defined by power subgroups. **Confidence: medium**, because the manuscript writes a completion-like identification under the brace, while the precise topology is not specified on this page; this is a verification task, not a claim that the displayed identification is false.

### Scans 139–143

These notes concern only what these five scans state or leave to investigate. A statement called “unproved” below is not claimed to be unproved in the whole manuscript: the proof may be in preceding or subsequent pages. Suggestions labelled **own idea** are exploratory and are neither established results nor claims of novelty.

#### 139-R1

- **Scan / location:** 139, opening paragraph and first three displays.
- **Kind:** Unproved claim.
- **Textual anchor:** “élucide complètement … la signification arithmético-géométrique”.
- **Note:** Grothendieck asserts that the preceding theorem supplies the arithmetic and geometric meaning of the algebraically obtained homomorphism, or at least of its quotient by the central kernel. A complete verification should identify the algebraic map with the action on the geometric object, retain the distinction between the original and quotient targets, and state which parts depend on the preceding theorem rather than on the present argument.

#### 139-R2

- **Scan / location:** 139, lower paragraph.
- **Kind:** Unpursued implication.
- **Textual anchor:** “opérant fidèlement” and “opérait trivialement”.
- **Note:** The passage to the quotient group is motivated by the need for a faithful action on the completed module, whereas the center of the earlier acting group acts trivially. This raises the precise question of what geometric information the faithful quotient retains and what additional data is required to detect the central kernel. The page makes the contrast explicit but does not construct that extra data here.

#### 140-R1

- **Scan / location:** 140, paragraph preceding (298).
- **Kind:** Unproved claim.
- **Textual anchor:** “ce revêtement n'est autre que le prorevêtement de Fermat”.
- **Note:** The action on the set of splittings is identified with the Fermat procover. To make this identification explicit, one would need a compatible description at finite levels, its transition maps, and the equivariance of the resulting inverse system. The handwritten insertion identifying the two fundamental groups is part of the asserted interpretation and should be checked together with the precise base and quotient conventions.

#### 140-R2

- **Scan / location:** 140, diagram (298), continuing at the top of 141.
- **Kind:** Unproved claim.
- **Textual anchor:** “comme image inverse de l'extension”.
- **Note:** Diagram (298) is used to interpret the arithmetic group as a pullback central extension. A proof should verify the cartesian property, the identification of the two displayed kernels, and compatibility with the quotient homomorphism. If the groups are being considered topologically, the category and continuity requirements should be made explicit as well.

#### 141-R1

- **Scan / location:** 141, last paragraph, continuing in the first paragraph of 142.
- **Kind:** Unpursued implication.
- **Textual anchor:** “calculs en apparence assez différents” and “canoniquement isomorphes”.
- **Note:** Two constructions of central extensions are said to produce a canonical isomorphism despite their rather different computations. It would be useful to isolate exactly which identifications make the isomorphism canonical, and to determine whether a comparison of the induced quotient maps alone suffices or whether a specified identification of the central kernels is essential. The sentence crosses the scan boundary and should be read as one claim.

#### 142-R1

- **Scan / location:** 142, middle paragraph.
- **Kind:** Conjecture / expectation.
- **Textual anchor:** “une explication générale de ce fait” and “aucune difficulté”.
- **Note:** Grothendieck expects a general explanation of the canonical agreement of the two central extensions. His suggested reason is that the starting quotient came from the larger covering group rather than from its quotient by the central involution. A rigorous formulation would need a comparison principle for these two lift constructions and a proof of its applicability to the maps under discussion; the opening verb and the exact covering noun remain paleographically uncertain.

#### 142-R2

- **Scan / location:** 142, last paragraph.
- **Kind:** Conjecture / desired construction.
- **Textual anchor:** “il faudrait interpréter” and “une ‘fibre type’ ‘pas trop grosse’”.
- **Note:** The page asks for a geometric interpretation of the original target as the automorphism group of a reasonably small fibre type on which it acts nontrivially. The problem is more specific than finding any representation: the object should explain the original homomorphism in the manner already supplied by the Fermat tower for its quotient. The manuscript explicitly says that inventing such an object is the difficulty.

#### 142-R3

- **Scan / location:** 142, last paragraph, in relation to (298) on 140.
- **Kind:** Own idea.
- **Confidence:** Low — the central extension suggests the form of an enhancement, but the pages do not supply the necessary descent or existence data.
- **Note:** One could test whether an enhancement of the splitting object by a compatible torsor under the displayed central kernel makes that kernel act nontrivially. Such an enhancement would have to be natural under the relevant base changes and recover the known quotient action after forgetting it. This is only a candidate direction for the requested fibre type, not a construction established by these scans.

#### 143-R1

- **Scan / location:** 143, formulas (299)–(300) and final paragraph.
- **Kind:** Unproved claim.
- **Textual anchor:** “dépend … de … pour iso et images inverses” and “une section cartésienne”.
- **Note:** The construction from the degree-three étale cover, the quotient of its integral permutation sheaf, and the Tate-type factor is asserted to be functorial for isomorphisms and pullbacks. A proof should identify the category of families, the pushforward and diagonal maps, and the base-change isomorphisms compatible with the quotient and tensor product. The exact base letter in (299) is overwritten, so any mathematical exposition should first resolve that transcription issue rather than silently repairing it.

#### 143-R2

- **Scan / location:** 143, formulas (299)–(300).
- **Kind:** Own idea.
- **Confidence:** Medium as a proposed local calculation — the quotient formula and rank correction visibly suggest it, but no global conclusion is asserted here.
- **Note:** After choosing a local ordering of the three sheets, one can examine the displayed quotient through the elementary model of a rank-three permutation lattice modulo its diagonal. Tracking the permutations and then the completed twist could provide an explicit check of the resulting rank-two local system and its descent. This calculation should remain separate from the diplomatic text and should not be used to replace the manuscript's canceled “trois” by its inserted “deux”.

### Scans 144–148

These are source-based reading notes, not a literature survey. Statements about the manuscript refer to the attached scans of Grothendieck (1981); speculative extensions are labelled **own idea**, with confidence and reason, and do not modify the diplomatic text.

1. **Scan 144, lines 1–12 — unpursued implication.** The Fermat tower is reformulated as the assignment of a torsor “compatible aux iso. et chgts de base,” with an additional condition that the induced homomorphism be “l'hom canonique.” A detailed reconstruction should distinguish the uniqueness of such a compatible assignment from uniqueness for an individual base and should keep track of the canonical homomorphism condition rather than dropping it.

2. **Scan 145, final paragraph — conjecture / question.** “Y-a-t-il une description remarquable du torseur de Fermat” asks for an interpretation in terms of the relative elliptic curve. The preceding exact sequence (303) suggests that the required description must include both a torsor for the Tate module of the generalized Jacobian and a section of its quotient torsor; the question is retained as open here even if later manuscript pages supply a construction.

3. **Scan 145, (302)–(304) — unproved claim.** “On en déduit une suite exacte” passes from the generalized-Jacobian extension to a sequence of full Tate modules. A proof would need to justify exactness through the inverse system, specify the transition maps in the notation `{}_nG`, and retain the connected-fibre qualification inserted into the description of the smooth commutative group scheme.

4. **Scan 145, following (304) — own idea.** One could make the torsor-and-section description a concrete descent construction, using local liftings of the quotient-torsor section to recover an `M_1`-torsor. **Confidence: high as a proof strategy**, because the displayed short exact sequence is exactly the datum such a local-lifting argument uses; no claim of novelty or of a complete proof is intended.

5. **Scan 146, (305)–(306) and final paragraph — unpursued implication.** The canonical map to the degree-one component is required to “commute aux opérations” of the permutation group. The relevant torsor therefore carries an equivariant structure, not merely its ordinary torsor structure; subsequent uniqueness assertions should be interpreted in that equivariant setting. The original shifts in base notation on this page should be resolved before using it for a statement over all schemes.

6. **Scan 147, lines 1–7 and (307) — conjecture / expectation.** “Or je présume qu'on a” introduces the vanishing of equivariant cohomology in degrees zero and one. The page begins an argument for the first vanishing and announces a spectral sequence for the second; the expectation should be tracked independently of the completion of its proof on the following page.

7. **Scan 147, upper diagonal note beside (308) — unpursued implication.** The warning says that the displayed cyclic-ratio isomorphism “commute à” the alternating subgroup, but not to the full permutation group. Any use of the quotient-torus/kernel identification in the equivariant calculation therefore needs a precise comparison of the two actions; the warning must not disappear when the formula is rewritten.

8. **Scan 147, lower diagonal note — own idea.** The equivariance warning suggests checking the action of a transposition explicitly on the cyclic-ratio map, before using the kernel model to identify fixed points. **Confidence: high as a diagnostic step**, since the note distinguishes the index-two subgroup from the full permutation group; it does not by itself establish the corrected cohomology computation, and the note's compressed prose remains uncertain.

9. **Scan 148, (309) — unproved claim / reference to earlier work.** “Les calculs faits par ailleurs montrent” asserts vanishing in degrees zero and one for the module obtained by tensoring with an arbitrary integer module. A verification needs the precise permutation-group action on the lattice and must preserve the preceding page's warning that one convenient identification is only equivariant for the alternating subgroup.

10. **Scan 148, left margin and conclusion (310) — unpursued implication.** “On n'a pas besoin de la relation” `Pic(S)=0` explicitly removes a hypothesis used in the preliminary calculation, and the conclusion is stated “pour” every scheme S. To substantiate this generality, one should follow both low-degree terms of the spectral sequence and apply (309) to the two different coefficient groups mentioned in the parenthesis, including the inserted Picard-group example.

11. **Scan 148, (309) — own idea.** A useful independent check would start with the diagonal inclusion into the three-coordinate permutation module, tensor with a completely arbitrary abelian group, and compare the resulting low-degree cohomology sequences. **Confidence: high as a verification strategy**, because it uses the quotient presentation already written in (308) and avoids treating the cyclic-ratio presentation as fully equivariant; no proof or novelty claim is being asserted here.

### Scans 149–152

These notes are source-based questions and possible lines of investigation, not verified claims about the subsequent literature. Quoted readings with paleographic uncertainty should be checked against the corresponding doubt entry.

1. **Scan 149, proposition, lines 1–6 — unproved claim.** The proposition asserts “une unique trivialisation” for every `(S_3,J^0)`-torsor over an arbitrary base. A proof audit should identify precisely the topology of the torsor and how the preceding degree-zero and degree-one vanishing statements give both existence and uniqueness uniformly after base change.
2. **Scan 149, Corollaire 1, (311) — unproved claim.** “Un unique morphisme” is asserted with compatibility under the three-point symmetry group and with the identity induced on `J^0`. Its derivation should spell out the generalized Jacobian's universal property and resolve the source correction below the displayed homomorphism without silently replacing the manuscript's notation.
3. **Scan 149, diagonal NB, (312) — unpursued implication.** The note places `U_1` in the three-coordinate torus modulo the diagonal, with equation `x_0+x_1+x_∞=0`. This gives a concrete model in which to test equivariance and the relation between the distinguished three boundary points and the map in (311).
4. **Scan 150, Corollaire 3 continued, (313)–(314) — unproved claim.** For a Brauer–Severi curve with an étale divisor of degree three, the text asserts “un unique morphisme” to the degree-zero generalized Jacobian, equivariant for the displayed automorphism group and inducing the identity on that Jacobian. The descent from a split three-point projective line should be checked, including compatibility of the morphism with changes of the local ordering of the divisor.
5. **Scan 150, description of `M_0(S'/S)` — unpursued implication.** The coefficient object is described as obtained “en le tordant” through the three-point symmetry group's action. The relation between this explicit twisted lattice and the torus appearing in (313) is worth recording functorially, with all pullback identifications made explicit.
6. **Scan 150, (313), own idea — confidence: medium.** Test the construction on bases where the three-point étale divisor is not split, using the quotient-of-permutation-lattice description to calculate transition maps. The reason for this suggestion is that the manuscript states the twisting construction but does not compute a nonsplit example on these pages; no novelty or general conclusion is claimed.
7. **Scan 151, (315)–(317) — unproved claim.** “Il suffit de prendre” introduces the coordinate formula `ψ(z)=(-z,z−1,1)` and two alternative representatives. A complete verification should check invertibility on the open curve, the three listed boundary values, and equivariance under the three-point permutations; these checks would also anchor the descent used on scan 150.
8. **Scan 151, final paragraph — unpursued implication.** The elliptic-curve datum “modulo symétrie” is related to a morphism into `M'_{1,1}`. The precise meaning of this moduli object should be recovered from the surrounding manuscript before drawing conclusions about the information retained or forgotten by that morphism.
9. **Scan 151, (317), own idea — confidence: high as a verification task only.** Work out the two basic transformations `z↦1−z` and `z↦1/z` directly on the displayed three-coordinate representative and compare the result with coordinate permutation modulo a common scalar. The formula is explicit enough to make this a useful elementary check, but no claim of a new construction is intended.
10. **Scan 152, lines 1–5 — unproved claim.** Under the hypothesis “2 inv. sur S,” the datum of `X` modulo its involution is said to correspond to `(Y,S')` together with “une section de U.” A proof should formulate the objects and their isomorphisms precisely and check both directions of this correspondence, including the dependence on the extra section.
11. **Scan 152, middle paragraph — unproved claim.** The author says that `Y` “se récupère” from the three-point étale datum, then writes the twisted projective line and the corresponding open subscheme. One should verify the descent maps and their compatibility with the subsequent canonical embedding into the generalized Jacobian.
12. **Scan 152, (318), final line — conjecture / expectation.** The canonical morphism is followed by “qui doit être aisé à caractériser” and the clipped stem “axiomatiq.” This is an explicit expectation of an axiomatic characterization; a proof would first have to state the proposed axioms and establish the claimed uniqueness or canonicity under them.
13. **Scan 152, (318), own idea — confidence: medium.** Try to characterize the displayed map by its factorization through the open three-point curve and the equivariant universal property stated on scans 149–150. The suggestion is prompted by the construction immediately preceding (318); the pages do not establish that these conditions are sufficient, so it remains a test to undertake rather than a conclusion.

## 5. Source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-4, supplied scan files 134–152; archive file described as pages 650bis–787]. Université de Montpellier.

The institution's printed source address on every supplied image is [grothendieck.umontpellier.fr](https://grothendieck.umontpellier.fr). The reference identifies the supplied primary source; no external edition or literature search was used for these transcription and research notes.
