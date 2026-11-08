# LM_C3-644-662 — Editorial and research notes

## Scope, source, and reading conventions

This package transcribes the nineteen supplied manuscript images named `LM_C3-644-662_scan644.jpg` through `LM_C3-644-662_scan662.jpg`. The transcription follows the supplied images, including cancelled passages, overwritten readings, interlinear additions, marginal notes, mathematical displays, and diagrams. The editorial notes and the English research notes below are separate from the French transcription.

**Source reference (APA style, from the supplied task metadata):** Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Manuscript excerpt, supplied scans 644–662]. Cote 140-3, archive file labelled “La Longue Marche, pages 293–650,” Université de Montpellier.

No published transcription has been used to fill gaps. Earlier pages cited within the manuscript have not been supplied in this package; references to them in the research notes identify checks still to be made. Research proposals below are neither claims of novelty nor assertions that a missing proof has been established.

The `scanpage` number follows the image filename, as required. It is one greater than the handwritten lower page number in these attachments. The distinct upper manuscript numbers are also retained with `mspage` where present. The printed repository footer is archival presentation metadata, not handwritten manuscript content, and is not reproduced as manuscript text.

| Scan | Visible handwritten pagination, top-to-bottom | Inventoried elements |
|---|---|---:|
| 644 | 643 | 17 |
| 645 | 625, 644 | 18 |
| 646 | 645 | 19 |
| 647 | 626, 646 | 24 |
| 648 | 647 | 18 |
| 649 | 627, 648 | 18 |
| 650 | 649 | 14 |
| 651 | 628, 650 | 24 |
| 652 | 651 | 10 |
| 653 | 629, 652 | 32 |
| 654 | 653 | 30 |
| 655 | 630, 654 | 38 |
| 656 | 655 | 28 |
| 657 | 631, 656 | 41 |
| 658 | 657 | 22 |
| 659 | 632, 658 | 29 |
| 660 | 659 | 25 |
| 661 | 633, 660 | 34 |
| 662 | 661 | 23 |


There are **464 inventory records**, all marked `yes`. Here `yes` means that the element is represented in the fragment, including any explicit uncertainty; it does not certify that every letter has been securely read. An element and its local deletion or insertion may have separate records. Reused equation numbers, visibly incomplete punctuation, manuscript ellipses, repetition rules, and mathematically surprising indices or compositions are retained.

## Legibility and notation

The principal prose and larger formulas are substantially more legible than the cancelled text, small superscripts, and angled marginal revisions. The least secure material includes scan 644's overwritten determinant diagram and final action paragraph; the inserted correction on scan 645; the middle revision on scan 651; the definition and margins on scan 653; the dense margins and final remark on scans 656–657; the revised paths in scan 660's (31); the cancelled corollary on scan 661; and the reworked paragraph and last phrase on scan 662. Enlargement and, where appropriate, rotation improved many readings, but several passages remain low-confidence.

The recurring angular subgroup superscript is represented as `\unsure{\natural|\sharp}`. This is a typographic uncertainty in the repeated handwritten sign; it has not been silently settled by mathematical expectation. The arithmetic quotient's initial Greek capital is marked where Γ/Π remains uncertain. Several arguments of M have a visibly two-lobed form; those are marked as ω/0 alternatives, while clear round zeros are retained as zeros. Exclamation marks, question marks, primes, circles, and bars over j are distinguished locally rather than normalized.

Confidence labels in the page-level tables are qualitative: **high** means a secure reading, **medium** a probable but unresolved reading, and **low** a substantially ambiguous or overwritten reading. The complete in-text uncertainty register supplies exact fragment-line locators for every marked doubt in addition to the approximate manuscript positions in those tables. The sole `\illegible{2}` denotes two cancelled words on scan 644; it is not used for a mathematical symbol.

The transcription is a LaTeX fragment, with no preamble. Its host document must define the prescribed editorial macros so that they can contain paragraphs, displays, and mathematics. Standard AMS mathematics/fonts, TikZ, and `tikz-cd` are used; the circled label on scan 656 uses TikZ's `shapes.geometric` library. Diagram separators use `ampersand replacement=\&` so that diagrams remain valid inside the required macros. All nineteen scans were compiled together with temporary definitions of those macros for checking; those definitions and the checking PDF are not part of the requested package.

## Page-level doubt tables and palaeographic notes

### Scans 644–647

#### Doubts

| Scan | Approximate line or position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 644 | First line, first symbol | v | σ; opening continuation is not securely identified | low |
| 644 | First line, quotient | Im Π̂₀ with a superscript circle | A stray punctuation dot; original ink has both a hat and a detached mark | low |
| 644 | First line | factorisé | factorisation; letter sequence is compressed | low |
| 644 | Left margin, deleted opening | two unreadable words | ink struck through beyond resolution | low |
| 644 | Left margin, next deletion | commut.; et | first abbreviation remains partly covered | low |
| 644 | Left margin | correction ε₃ | condition ε₃ | low |
| 644 | Left margin | définition (47) | déf. or définition; second numeral could be 5 | medium |
| 644 | Second diagram, overwritten objects | GL, GL(2,Z),Z | several letters overlap the replacement objects and arrows | low |
| 644 | Second diagram, lower object | GL(2,Z/4Z)* | star may belong to the overwritten predecessor | low |
| 644 | Bottom paragraph, deletion/insertion | régulière / de groupe top. | de quotients; overwritten wording and exact attachment are uncertain | low |
| 644 | Bottom paragraph | automs | autos; no expansion supplied in transcription | low |
| 644 | Bottom paragraph, subgroup argument | ω | 0; two-lobed ink form, unlike the clear round zeros elsewhere | medium |
| 644 | Last line, reference | 554 | 594; second digit is contracted | medium |

#### Legibility

Scan 644 is readable in its main body but opens in mid-sentence. The diagonal marginal afterthought and the overwritten determinant diagram have the lowest confidence. Several overwritten words at the bottom remain tentative despite cropped enlargement; their uncertainty is retained in the fragment.

#### Scan 645 additional doubts

| Scan | Approximate line or position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 645 | Line 1 and first diagram, overwritten subscript | deleted 0 | a; the strokes are overwritten | low |
| 645 | Line 2 | G/Π₀ | G[Π₀]; delimiters are overwritten | low |
| 645 | Line 5, quotient | fraktur S₃ | calligraphic G₃; the letter has a broad swash | medium |
| 645 | Added note after M°!(0) | reconnaît | wording compressed to connecting strokes | low |
| 645 | Added note, cancellation after Ker | précisé | word almost entirely overstruck | low |
| 645 | Added note continuing in left margin | en fait μ | en effet μ | medium |
| 645 | Added note, punctuation after μ | ; | !; long upper stroke and lower detached mark | low |
| 645 | Beginning of canceled passage | trouve | trouvons; preceding on is not separately visible | low |
| 645 | Canceled upper arrow, overwritten object | M | overstruck letter possibly a different capital | low |
| 645 | Canceled three-object diagram, argument | −j̄ | −j, bar not secure here | low |

##### Scan 645 legibility

The main upper paragraph and the lower canceled argument are mostly readable. The subscript of the first two occurrences of M is overwritten; the inserted kernel correction is much smaller and least secure. Diagonal strokes cancel the lower argument, which continues onto scan 646; the text remains transcribed inside deletion markup.

#### Scan 646 additional doubts

| Scan | Approximate line or position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 646 | Line 2 | essayons | word after dash has compressed middle letters | medium |
| 646 | First filtration, decorations | superscript wedge after G and Π₀ | asterisk after G; both small marks are uncertain | low |
| 646 | Filtration factors | fraktur S₃ | calligraphic G₃ | medium |
| 646 | Before isomorphismes | des | overwritten word may have an extra canceled stroke | medium |
| 646 | First uncanceled display | ≃ | = | medium |
| 646 | First uncanceled display, corrected M | M₀″! replacing M°! | exact overwritten degree mark and separate canceled a remain uncertain | low |
| 646 | Last display | M′(−j̄) | M!(−j̄); no dot is secure in this occurrence | low |
| 646 | Last line, reference | (46) | (45) | medium |

##### Scan 646 legibility

The diagonal cancellation runs from the opening continuation through the proposition and its conclusion about M°!. It stops above “Admettant ce point”; the bottom calculation is not covered by those diagonal strokes and has local overwritten corrections instead. The superscripts in that calculation are a principal paleographic risk.

#### Scan 647 additional doubts

| Scan | Approximate line or position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 647 | Heading d), canceled object | script Mρ,σ | overwritten capital uncertain | low |
| 647 | Above (49), canceled object | calligraphic Gρ,σ | another decorated G or M | low |
| 647 | (49), annotation under M(0) | M₀,₃~(0) | M₀,₁~(0) | low |
| 647 | (49), arithmetic quotient, repeated in (52) | Γ̃_Q | Π̃_Q; doubled left stem is clear but alphabet not certain | medium |
| 647 | (49), last row | Nσ* | superscript is compressed | medium |
| 647 | (50), first letter on second row | N over canceled A | overwritten capital may be N in both layers | low |
| 647 | (50), before Zρ! | canceled ρ | unidentified small overstruck symbol | low |
| 647 | (51), after Nρ? | canceled 0 | overwritten subscript or punctuation | low |
| 647 | (52), canceled expression before 1 → μ | Ker Nρ? = μ | final relation could be an arrow; heavily struck through | low |

##### Scan 647 legibility

The running text and principal diagrams are readable; several formulas carry compact interlinear annotations. The superscript question mark on Nρ? is visibly hooked and dotted and is retained, as distinct from the exclamation decoration on Z. In (50) the final subgroup visibly has σ, not ρ; that reading is preserved without repairing the apparent mismatch. The canceled expression before the final exact sequence is least reliable.

### Scans 648–652

#### Pagination

Scan identifiers follow the attachment filenames. They are one greater than the handwritten number at the lower edge of the reproduced sheet and the printed archive footer. The lower handwritten numbers are retained as `\mspage` at their position; separate upper manuscript numbers, when present, are retained at the top. Printed repository footers are not manuscript text.

#### Doubts

Approximate line locations count manuscript text lines, with displays and additions separately identified. Confidence refers to the proposed reading, not to the mathematical plausibility of a corrected statement.

| Scan | Approximate line / location | Reading | Alternatives / qualification | Confidence |
|---|---|---|---|---|
| 648 | (53), first superscript and subsequent instances | `\natural` | `\sharp`; the zigzag is clear as a repeated glyph, but its typographical identity is uncertain. | low |
| 648 | (53), first factor | `N_\rho^{?}` | The letter is overtraced; the question-mark decoration is more legible than the underlying letter. | medium |
| 648 | line before (54), cancellation | `hom.` | The cancelled strokes may include an additional final letter. | low |
| 648 | left of the three embeddings | `les` | Very small cancelled word. | low |
| 648 | right of the lower branch of the embeddings | `)` | A closing curve is visible; no matching opening parenthesis is clearly visible. | low |
| 648 | last line | `hom.` | `hom` without a full stop; the final mark is unclear. | medium |
| 649 | first prose line | `Évidemment` | The opening letters and accent are less secure than the word ending. | medium |
| 649 | after `SG_{rho,sigma}` | `\simeq` | The relation is overtraced. | medium |
| 649 | (57), top kernel | cancelled `+` | The decoration is heavily inked and crossed. | medium |
| 649 | (57), bottom quotient | `\gamma_{rho,sigma}` | `\Gamma_{rho,sigma}`; the initial letter has been overwritten. | low |
| 649 | paragraph after (57), displayed subgroup | denominator `\mu_\sigma` | `\mu_\rho`; sigma is the stronger visual reading, despite the rho quotients elsewhere. | medium |
| 649 | same line, final subscript of script G | `\sigma` | Overwritten. | medium |
| 649 | (58), annotation above left group | `\mathcal G_{rho,sigma}^{+}` | Plain `G_{rho,sigma}^{+}`. | medium |
| 649 | (58), middle horizontal arrow from script G+ | `\sim` | The small dark decoration could contain a cancellation; its squiggle has been retained without repairing the mathematics. | low |
| 649 | prose before (59) | `hom.` | A terminal stop is uncertain. | medium |
| 649 | final two lines | `bisection` | Its ending overlaps the cancelled quotient. | medium |
| 649 | below gamma in (59), cancelled object | `\Gamma_{rho,sigma}^{\natural}/\mu_\rho` | Dense diagonal cancellations; the qualifier is not fully secure. | low |
| 649 | final line, first factor in the intersection | `SZ_\rho` | The preceding cancellation overlaps the first letter. | medium |
| 650 | (60), arithmetic quotient beneath the second factor | `\widetilde\Gamma_{\mathbb Q}` | `\widetilde\Pi_{\mathbb Q}`; the left stroke is doubled, whereas the far-right leg is not clear. | medium |
| 650 | first subgroup list, third item | `M_a^![0]` | The lower `a` is small and could be an overtraced `0`. | medium |
| 650 | first subgroup list, fourth item | `M_0^![0]` | The exclamation-like decoration is heavily overtraced; extra prime strokes cannot be excluded. | low |
| 650 | middle column of added equalities | `M^\Pi[0]` | An added heavy stroke beside the Pi could be a subscript or a cancellation. | medium |
| 650 | right column of added equalities | `M^{\Pi_0}[0]` | The last bracket and part of the zero run into the reproduced page edge. | medium |
| 650 | three lowest added equalities, argument of M | `\omega` | `0`, possibly `\infty`; the glyph is distinctly two-lobed here, unlike the clear zero of the main `M(0)` at the start of the list. Its typographical identity remains unresolved. | low |
| 650 | right-column cancelled expression | `M(\omega)L_0` | `M(0)L_0`; dense overwriting; the later inserted term with superscript `\Pi_0` is clearer. | low |
| 650 | first term of second subgroup list | `{M(1/2)}` | `M(1/2)` without braces; strokes flanking the overtraced M and closing parenthesis may be delimiters or corrections. | low |
| 651 | heading, final word | `raffinements` | `raffinement`; the final short upstroke is not a secure plural ending. | medium |
| 651 | first prose line, section reference | `V` | `IV`; an extra left-hand stroke is overwritten. | medium |
| 651 | (1) and the next paragraph | subscript `0` on script G | `a`; the two small forms are retained with doubt rather than removed by reference to later notation. | medium |
| 651 | end of (1) | superscript `*` | The small dark mark is not fully separable into strokes. | medium |
| 651 | middle insertion over `qui` | `formé` | `formés`; the number of the word is unclear. | medium |
| 651 | middle revised normalis-word | `normalisent`, cancelled `ateur de` | The unstruck stem is `normalis`; `normalisateur de` is a strong reading of the earlier wording, while `ent le` is another possible cancelled ending. The final state and exact cancellation boundary are uncertain. | low |
| 651 | inserted line after the normalis-word | `trivialt` | Abbreviation for trivialement; exact final superscript/terminal stroke uncertain. | medium |
| 651 | cancelled line after `qui est` | `néct.` | Possibly a different contracted adverb; the heavy cancellation intersects the middle letters. | low |
| 651 | arithmetic quotient, two occurrences | `\widetilde\Gamma_{\mathbb Q}` | `\widetilde\Pi_{\mathbb Q}`; same alphabet ambiguity as in (60). | medium |
| 651 | bottom cancellation | `On peut` | First word is more obscured than `peut`. | medium |
| 652 | second line, initial symbol | `\mathcal G` | A large earlier letter, possibly M, remains inside the overtraced script G; no separable cancellation or certain alternative symbol can be identified. | medium |
| 652 | fifth line, script-G decoration | `+` | `*`; the short mark is overtraced. | low |
| 652 | sixth line | `peut être` | Both words are strongly contracted; the separate short upper stroke over the second word supports `être`. No hyphen is visible. | medium |
| 652 | eighth line, underlined verb | `paraphraser` | The middle `ph` is clearer than the shortened opening and ending; the reading remains marked in place. | medium |

#### Legibility

Scan 648 is relatively open and legible, but the overtraced first factor in (53), the small cancelled word beside the embeddings, and the identity of the repeated zigzag superscript remain uncertain. The duplicated equation number (55) is retained.

Scan 649 is legible in its main prose but considerably less secure in the corrections to (57)–(59). The lower cancelled quotient is represented in the diagram at its relation to the upward arrow, together with the overlapping continuation of the prose; this preserves the mathematical objects rather than substituting a verbal description. Several visibly surprising labels and indices are left as written or explicitly marked as doubtful.

Scan 650 has a large blank lower region. Its substantial uncertainty is concentrated in the compact equality annotations against the right edge, the overwritten `M(1/2)` term, and the precise alphabet of the arithmetic quotient symbol. The final inclusion into the unquotiented `\mathcal M_{rho,sigma}` has been retained exactly as displayed, without changing it to match the preceding page.

Scan 651 has readable main prose, but the middle revision is the least secure continuous textual passage in these five pages. The stem `normalis` and the inserted quotient-action condition are legible; the boundary between retained letters and the cancelled old ending is not. The fragment marks both a proposed retained reading and the cancelled tail instead of silently choosing a fluent corrected sentence. The indices, alphabet ambiguity and spelling/abbreviation doubts remain visible in place.

Scan 652 is mainly continuous prose with little cancellation. The overtraced initial group symbol, the exponent after the later script G, and the very contracted `peut être` are the least certain details. The opening parenthesis before `dans ce cas` has no clearly visible closing parenthesis in this paragraph and has been left open; punctuation has not been supplied after `schématique`. The insertion `entiers` is placed after `adéliques`, as indicated by its small guide. The final equation and its overbrace label are comparatively clear.

### Scans 653–657

The scan numbers refer to the filenames, not the lower manuscript/archive pagination. Scan 653 bears 629 at the top and 652 at the lower left; scan 654 bears lower 653; scan 655 bears top 630 and lower 654; scan 656 bears lower 655; scan 657 bears top 631 and lower 656. These numbers are transcribed at their positions. Printed repository footers are not manuscript text.

#### Doubt register

| Scan | Approximate position | Reading | Alternatives / difficulty | Confidence |
|---|---|---|---|---|
| 653–657 | Repeated subgroup superscript | natural sign | Sharp sign; the repeated zigzag is not securely distinguishable | low |
| 653 | (4), cancelled line above a) | “u normalise … et induit l'identité dans …” | Overwritten by dense horizontal loops; each mathematical part is marked in place | low |
| 653 | (4), added d) clause | “et induit l'identité sur (G⁺/G^natural)/Im Π” | Separation of insertion marker from quotient strokes is uncertain | medium |
| 653 | Right margin beside (4) | “cf. page 635 suite … cette condition” | Cropped edge, crossings and interlinear overprinting obscure the rest | low |
| 653 | Left margin beside (4) | “La dernière condition rajoutée … conséquence … induite par” | Entire note cancelled; “rajoutée”, parenthesis and some connecting words insecure | low |
| 653 | First proof sentence | “évidemment”; “Compte tenu que” | Very compressed endings | medium |
| 653 | Unnumbered formula before (5) | τ(σ)=-σ | Final sigma resembles epsilon | medium |
| 653 | (5) | (5*), deleted ε₂, overwritten parenthesis | Small star and stages of correction unclear | low |
| 653 | After (5) | “condition c')” | Possibly “b')”; the visible rounded initial was retained as a doubt | low |
| 653 | Lower half | Auxiliary fraktur g_(b) | Could be ordinary capital G; revised subscripts partly buried | low |
| 653 | Lower proof | “sous-grpe”; “à montrer”; “de sorte” | Abbreviation and compressed strokes insecure | medium |
| 654 | Addition to (6) | α_G(α') | Possibly ε_G(α'); the handwritten initial is different from the preceding epsilon | low |
| 654 | First proof sentence | g_(a)(b); “aussi à (b)” | Revised group subscript; the cited condition could be (a) | low |
| 654 | After (7) | “on gagne” | Compressed word ending | medium |
| 654 | Formula beginning u(ρ) | σ⁻¹(ρ⁻¹) | Superscript of sigma partly overwritten; retained with doubt | low |
| 654 | (8), cancellation | u'(α₀σ)α'στ | Dense crossing hides most individual symbols | low |
| 654 | Below (8) | Deleted τ' under στ | Could be a different abandoned factor | low |
| 654 | Central-subgroup relation | Hooked inclusion arrow | Could be a double implication-style arrow | low |
| 654 | Final sentence | Product G_tau^natural G⁺ | Possible quotient slash; “en” may be underlined or corrected | low |
| 655 | Cancelled sentence above cases | “on aurait, puisque στ=-τσ” | First verb is crossed; replacement reads “On distingue encore deux cas” | medium |
| 655 | Cancelled expression in case 1 | Dotted ε, u'(σ), α', τ | The horizontal cancellation hides a possible additional sigma | low |
| 655 | (9) before “soit encore” | Deleted “ou” | Could be an abandoned equivalence sign | low |
| 655 | After (9) | “signifie” replaced by “implique” | Crossing affects the original word | medium |
| 655 | Coefficient after u'(σ) | Dotted ε₂' | Dot, prime and cancellation overlap | low |
| 655 | Choice of sign | Right-hand ε₂' with possible dot | The tiny superscript could be ink from the prime | low |
| 655 | Formula before (10) | Deleted (10); deleted τ inside u' | Revision is too dense to distinguish both former symbols securely | low |
| 655 | Before (11) | “est dans” replaced by “satisfait” | Original words partly hidden | medium |
| 655 | Penultimate line | First case marker (*) | Strongly retraced / overwritten | low |
| 656 | Cancelled opening remark | “multiplicative”; “tte” | Diagonal cancellation and compressed ending | medium |
| 656 | Case a) | Deleted G before SL; “Condition”; “retombe” | The deleted noun and capitalisation are insecure; no missing pronoun has been supplied | low |
| 656 | Left margin at (13) | “A priori on a plutôt”; M with possible tilde | Independent rotated reading resolves the words; tilde over the first M remains less clear than over the diagram's M | medium |
| 656 | Left marginal diagram | M_0,3(0) and circled G_0,3 | Overwritten subscript and letter form | low |
| 656–657 | Several M arguments: 656 cancelled formula and left marginal diagram; 657 last braced equality and marginal formulas | ω / 0, with order reflecting the local shape | Some arguments are distinctly two-lobed while others are round; no uniform zero normalisation has been imposed | low |
| 656 | (14) and marginal equality | M![0] | Could be M'![0]; right-hand upstroke merges with superscript | low |
| 656 | Left margin at (14) | “trivial” followed by superscript mt; cancelled “tous les sous-groupes … contenus par” | Multiple vertical cancellation strokes; final formula very uncertain | low |
| 656 | Right margin at (14) | “expliciter à nouveau pourquoi …” | Narrow margin and clipped right edge; not-in versus in is unresolved | low |
| 656 | Case c), last lines | p.r.v. / p.r. au; deleted “avant” | Abbreviation and overwritten comparison phrase | low |
| 657 | Upper text | “caractère”; black superscript on ε₂ | The compressed noun and heavily retraced mark are insecure; the latter is represented as # / prime rather than silently omitted | low |
| 657 | Upper-left cancelled note | “induise” / “produise”; “Dans la nouvelle version” | Cancellation intersects letters and some connectors remain ambiguous | low |
| 657 | Upper-left cancelled note, formula | M[0] with lower 0 and upper ! | Possible absence of the upper !; lower writing overlaps the preceding line | low |
| 657 | Cancelled note ending beside (15) | “trop grand”; “un peu tr.”; “(ancienne version)”; “un peu trop petit!” | Two writing angles and an underlined interline phrase cross; relative revision order uncertain | low |
| 657 | Cancelled upper-right note | “On aurait pu introduire”; M![0]₀; last factor L₀^Π₀ | The last symbol is heavily rewritten and could be Π₀; the additional prime on M is uncertain | low |
| 657 | Before (16) | Cancelled Z | Heavily overdrawn letter before the subgroup symbol | low |
| 657 | End of (16) | Cancelled inclusion / leftward double arrow | Small black remnant to the right of μ | low |
| 657 | Before (17) | Cancelled G with lower 0τ | Cancellation obscures the precise lower characters | low |
| 657 | Bottom revised remark | Deleted “sont compatibles”; “avec”; “si on suppose”; cancelled “voit” and ρ,σ | Multiple overwritten lines; the main replacement reading was independently checked, but the abandoned wording and tail remain uncertain | low |

#### Legibility

The main calculation is substantially more readable than the heavily overwritten definition and marginal material. Confidence is lowest in the cancelled clause above (4), the additions at the right edge of scan 653, the multiple revisions of auxiliary subgroup notation, the angled notes on scans 656–657, the last revised remark of scan 657, and the zigzag subgroup superscript. The marginal writing was inspected after rotation and enlargement; several remnants nevertheless support only tentative readings. Uncertainty has been retained in the transcription rather than resolved from mathematical expectations.

### Scans 658–662

The scan identifiers are those in the supplied filenames. Their visible lower manuscript/archival handwritten numbers run 657–661; the independently written upper numbers 632 and 633 are retained where visible. The repository footer is not manuscript text.

#### Table of doubts

| Scan | Approximate line or location | Reading | Alternative / difficulty | Confidence |
|---|---|---|---|---|
| 658 | Opening line | qu'en se restreignant | qu'on; cursive vowel and ending are compressed | medium |
| 658 | All occurrences of the angular superscript | \natural | \sharp; the manuscript glyph is lightning-like | low |
| 658 | (18), canceled original right side | \(L_0\cap\mathcal G^{\natural}\) | Initial symbol heavily overwritten | low |
| 658 | (18), parenthetical | l'ens | Abbreviation's ending is abbreviated to a stroke | medium |
| 658 | Left margin, final two lines | ce qui surprend | Second word group partly reduced to strokes | low |
| 658 | (19), arrow label | i | Tiny overwritten letter | low |
| 658 | Before the tuple-to-characters diagram | déduites | Ending compressed | medium |
| 658 | Canceled (24), second kernel | \(\varepsilon_{2,\sigma}\) | \(\varepsilon_{2\gamma}\); an apparent sigma is retained as the first reading | low |
| 658 | Canceled (24), last right parenthesis | ) | Right edge clipped | low |
| 659 | All selected-subgroup superscripts | \natural | \sharp; same angular glyph as scan 658 | low |
| 659 | (24), deleted term before gamma prime | \(Z_\rho\) | A Z and a descending subscript are overwritten | low |
| 659 | Paragraph below (24) | 1, ou 2 ou quatre; respt | First ou and the superscripted abbreviation are compressed | medium |
| 659 | Marginal generalization beside (25), condition a) | est \(\varepsilon[\tau](\rho)\), deleted | Heavy cancellation; the replacement conjugacy wording is clearer | low |
| 659 | Marginal generalization, first word | Plus | The word is retraced | medium |
| 659 | After (25), final word before congruences | aura | a; final strokes compressed | medium |
| 659 | Lower left margin | ds.; ce qui me ferait perdre | dans; on ferait; rotated and partly crowded text | low |
| 659 | Before the unnumbered action map | page 577 | 579 | medium |
| 659 | (28), arrow label | \(i_{L_0,S_0G}\) | \(i_{L_0,G}\); stacked small subscripts | low |
| 659 | (28), deleted first factor | \(\iota(l)\) | \(i(l)\); heavily overwritten | low |
| 660 | All selected-subgroup superscripts | \natural | \sharp; same unresolved angular glyph | low |
| 660 | (29), last denominator | \(L_0^{\natural}\) | Right edge is cramped and clipped | medium |
| 660 | (31), canceled central object and arrows | \(G_{\rho,\sigma}\) and canceled arrows | Overlapping original and revised paths; canceled edges carry crossed arrow marks in the typeset diagram | low |
| 660 | Above the character definitions following (33) | \(\varepsilon_G=\varepsilon_\gamma\delta_G\), deleted | Most of the original is scribbled over | low |
| 660 | Second character definition following (33) | chi overwritten by epsilon | The long descending first stroke remains under the replacement | low |
| 660 | (34), last parenthetical | noté | Cursive word and number of ellipsis marks are uncertain | medium |
| 660 | Left margin by (34) | idem avec | Second word is reduced to strokes | medium |
| 661 | All selected-subgroup superscripts | \natural | \sharp; same unresolved angular glyph | low |
| 661 | Opening continuation | ds | dans; compressed cursive | medium |
| 661 | (36), source of the first displayed arrow | \(G_{\rho,\sigma}\) | G retraced over an earlier glyph | medium |
| 661 | (38), canceled superscript of the second G | \natural | \sharp; nearly obliterated | low |
| 661 | Proposition, word after “des” | quadruples | quadrupliens; apparent canceled “couples” under the beginning | low |
| 661 | (39), b) sign subscript | \(\varepsilon_2\) | \(\varepsilon_\tau\); small subscript resembles a tau | medium |
| 661 | (40), deleted prefix before the brace | \(f^{-1}\underline u\) | First f and exponent heavily crossed | low |
| 661 | (40), tuple variable | underlined u over a canceled f | Small black overwritten letter below the underline | low |
| 661 | Canceled first (41), isolated symbol above display | E | calligraphic E; heavily retraced | low |
| 661 | Canceled first (41), left side and annotation | \(Z_0\), with Ker inserted above | Overlapping diagonal cancellation makes the left side uncertain | low |
| 661 | Canceled first (41), lower centralizer | \(\operatorname{Centr}_{\mathcal G^\natural}(\varepsilon_0)\) | Subscript might be \(\mathcal G\); closing parenthesis not securely visible | low |
| 661 | Surviving (41), inserted parenthesis at right edge | \(Z_{\rho,\sigma}^{\circ+}\) and closing delimiters | The far right is cramped and clipped; suffix and delimiters marked uncertain | low |
| 662 | All selected-subgroup superscripts | \natural | \sharp; same unresolved angular glyph | low |
| 662 | Following (42), canceled word before inserted elle | dont | déf.; the crossing line obscures the middle | low |
| 662 | Canceled insertion above the main canceled sentence | image inverse de \(Z_0\), then canceled \(L_0\) | First mathematical object overwritten; may be \(L_0\) | low |
| 662 | Canceled sentence below (42) | injectif par proj. au quotient \(L_0^\natural\) | “passage” possible for proj.; several strokes merge with cancellation lines | low |
| 662 | Canonical-map label near (28) and in the kernel display | \(i_{L_0,SG}\) | \(i_{L_0,S_0G}\); tiny stacked subscript | low |
| 662 | Remark, first sentence | projection | présentation; middle letters are rapidly compressed | medium |
| 662 | Remark, before “simplement” | définirait | définissait; ending and medial r/ss uncertain | medium |
| 662 | Final parenthesis, after the barred m | a | en; two short strokes; original order retained | low |
| 662 | Last line, verb following pr | desserrer | donner; an earlier tentative reading was dessiner | low |
| 662 | Last line, final noun | moule | modèle; the tall stroke may be d followed by é rather than l | low |

#### Legibility

Every ellipsis in this fragment represents dots visible in the manuscript: the margin of scan 658 after ci-dessus, the three right sides in its canceled (24), the final parenthesis and margin by (34) on scan 660, and the final parenthesis of scan 662. No ellipsis stands for omitted text. The precise number of dots following noté on scan 660 is itself uncertain and marked as such.

The main text and uncanceled displays on scan 658 are substantially legible. The angular superscript distinguishing the selected subgroup, the overwritten original right side of (18), and the rotated marginal afterthought are less secure. The canceled (24) is retained, including the ellipses actually written in the manuscript.

On scan 659, the small characters in (24) and the two rotated marginal notes require more caution than the main prose. The long horizontal mark in condition b) of (25) is retained as a rule, without expanding its repeated wording. The abbreviations and the quotient written without a plus after (25bis) have not been normalized.

On scan 660, the revised central paths of (31) and the tiny canceled character formula below (33) are the least reliable areas. Unarrowed connectors and the downward double arrows in (32) are retained as drawn. In the last character formula after (33), the order \(\delta_G\varepsilon_{3\gamma}\) follows the visible ink; it has not been silently reordered.

Scan 661 contains a deeply canceled first corollary, followed by a surviving corollary with the number (41) reused. Both are represented. The original/replacement word for the tuples in the proposition and the little annotation over the first canceled left side remain uncertain after enlargement. The horizontal repetition rule in (39) b) is retained without supplying repeated words. Closing delimiters at the far right of the final insertion are uncertain; the transcription explicitly marks them rather than presenting them as clearly visible.

The main argument on scan 662 is relatively legible, including the element map (42), the quotient injection (43), and the five-term exact sequence (44). The canceled and reworked sentence below (42) remains substantially less reliable: every readable fragment and best tentative word is retained with doubt marks. The final remark was enlarged separately, including its last line; the barred-m abbreviation, its following short word, and the final verb/noun phrase remain explicitly uncertain. Membership and inclusion signs written vertically under formulas are retained as rotated symbols in the diagrams.

## Abbreviations met

Expansions are proposed here only and are not inserted into the manuscript text. Variant forms are retained in the records for their respective scans.

### Scans 644–647

#### Abbreviations met

| As written | Tentative expansion |
|---|---|
| comm. | commutatif |
| NB | nota bene |
| déf… | définition (ending uncertain) |
| cf | confer / comparer |
| can. | canonique |
| hom | homomorphisme |
| automs | automorphismes (reading itself uncertain) |
| p. | page |

##### Scan 646 abbreviations

- `can.`: canonique.
- `hom`: homomorphisme.
- `cqfd.`: ce qu’il fallait démontrer.

##### Scan 647 abbreviations

- `iso`: isomorphisme.
- `cqfd.`: ce qu’il fallait démontrer.
- `déf`: définition.
- `Norm`: normalisateur.

### Scans 648–652

#### Abbreviations met

| As written | Proposed expansion, here only |
|---|---|
| `déf` | définition |
| `hom.` | homomorphisme(s) |
| `épi` | épimorphisme |
| `hom` | homomorphisme |
| `i.e.` | id est |
| `p.` | page |
| `trivialt` | trivialement |
| `néct.` (doubtful, deleted) | nécessairement |
| `pts` | points |
| `s-groupe` | sous-groupe |
| `etc` | et cetera |

### Scans 653–657

#### Abbreviations met

| As written | Proposed expansion |
|---|---|
| Aut | automorphismes |
| def | définition |
| Im | image |
| Dém. | démonstration |
| prop. | proposition |
| sous-grpe (uncertain) | sous-groupe |
| cf. | confer / comparez |
| i.e. | id est / c'est-à-dire |
| mod | modulo |
| l'hyp. | l'hypothèse |
| m with overbar | même |
| l'hom | l'homomorphisme |
| p. | page |
| NB | nota bene |
| tte (uncertain) | toute |
| trivial with superscript mt (uncertain) | trivialement |
| p.r.v. / p.r. au (uncertain) | perhaps “par rapport au”; expansion insecure |
| n° | numéro |
| p.ex. | par exemple |
| op. | opération |
| ss-groupe | sous-groupe |
| déf | définition |
| tr. (uncertain, abandoned phrase) | trop, possibly only an interrupted beginning |

### Scans 658–662

#### Abbreviations met

| Form as written | Proposed expansion (notes only) |
|---|---|
| p. ex. | par exemple |
| NB | nota bene |
| cf. | confer / voir |
| ens | ensemble |
| hom | homomorphisme |
| ssi | si et seulement si |
| int | automorphisme intérieur |
| Centr | centre in Centr(G^+); centralisateur in \(\operatorname{Centr}_{\mathcal G^+}(L_0)\) |
| Ker | noyau |
| inv. | inverses |
| respt | respectivement |
| etc | et cetera (written in the manuscript) |
| conj. | conjugué |
| i.e. | id est |
| ds. | dans |
| dfn | définition |
| Im | image |
| idem | de même |
| pr | pour |
| \(\overline{\mathrm m}\) | même |
| autom. | automorphismes |
| proj. | projection (only a doubtful reading inside a cancellation) |

## Complete in-text uncertainty register

This supplementary register lists every occurrence of `\unsure` and `\illegible`, including repetitions and small punctuation doubts. The line number is an **exact line in the supplied LaTeX fragment**, not a claim about manuscript lineation; the scan and the page-level tables above locate the corresponding manuscript passage. A vertical bar within a marked reading separates the proposed alternatives. Confidence and palaeographic qualifications are supplied in the page-level tables; repeated signs share the qualifications stated there.

| Scan | LaTeX fragment line | Marked content |
|---|---:|---|
| 644 | 3 | `\unsure{v\|\sigma}` |
| 644 | 3 | `\unsure{\circ}` |
| 644 | 3 | `\unsure{factorisé}` |
| 644 | 10 | `\illegible{2}` |
| 644 | 10 | `\unsure{commut.}` |
| 644 | 10 | `\unsure{correction\|condition}` |
| 644 | 10 | `\unsure{inition}` |
| 644 | 15 | `\unsure{\mathrm{GL}}` |
| 644 | 16 | `\unsure{*}` |
| 644 | 16 | `\unsure{\mathrm{GL}(2,\mathbb Z),\mathbb Z}` |
| 644 | 26 | `\unsure{régulière}` |
| 644 | 26 | `\unsure{de groupe top.\|de quotients}` |
| 644 | 26 | `\unsure{automs}` |
| 644 | 26 | `\unsure{\omega\|0}` |
| 644 | 26 | `\unsure{554\|594}` |
| 645 | 34 | `\unsure{0\|a}` |
| 645 | 34 | `\unsure{\mathcal G/\Pi_0\|\mathcal G[\Pi_0]}` |
| 645 | 34 | `\unsure{\mathfrak S_3\|\mathcal G_3}` |
| 645 | 37 | `\unsure{0\|a}` |
| 645 | 42 | `\unsure{reconnaît}` |
| 645 | 42 | `\unsure{précisé}` |
| 645 | 42 | `\unsure{fait\|effet}` |
| 645 | 42 | `\unsure{;\|!}` |
| 645 | 44 | `\unsure{trouve\|trouvons}` |
| 645 | 47 | `\unsure{M}` |
| 645 | 57 | `\unsure{\bar\jmath\|\jmath}` |
| 646 | 68 | `\unsure{essayons}` |
| 646 | 70 | `\unsure{\wedge\|*}` |
| 646 | 70 | `\unsure{\wedge}` |
| 646 | 70 | `\unsure{\mathfrak S_3\|\mathcal G_3}` |
| 646 | 70 | `\unsure{\mathfrak S_3\|\mathcal G_3}` |
| 646 | 77 | `\unsure{des}` |
| 646 | 83 | `\unsure{\simeq\|=}` |
| 646 | 83 | `\unsure{\circ}` |
| 646 | 83 | `\unsure{a}` |
| 646 | 93 | `\unsure{\prime\|!}` |
| 646 | 96 | `\unsure{(46)\|(45)}` |
| 647 | 106 | `\unsure{\mathcal M}` |
| 647 | 115 | `\unsure{\mathcal G}` |
| 647 | 119 | `\unsure{3\|1}` |
| 647 | 120 | `\unsure{\widetilde{\Gamma}_{\mathbb Q}\|\widetilde{\Pi}_{\mathbb Q}}` |
| 647 | 121 | `\unsure{*}` |
| 647 | 130 | `\unsure{A}` |
| 647 | 130 | `\unsure{\rho}` |
| 647 | 139 | `\unsure{0}` |
| 647 | 146 | `\unsure{\widetilde{\Gamma}_{\mathbb Q}\|\widetilde{\Pi}_{\mathbb Q}}` |
| 647 | 148 | `\unsure{\operatorname{Ker}}` |
| 647 | 148 | `\unsure{=\mu\|\longrightarrow\mu}` |
| 647 | 150 | `\unsure{\widetilde{\Gamma}_{\mathbb Q}\|\widetilde{\Pi}_{\mathbb Q}}` |
| 648 | 162 | `\unsure{\natural\|\sharp}` |
| 648 | 165 | `\unsure{N_{\rho}^{?}}` |
| 648 | 171 | `\unsure{hom.}` |
| 648 | 181 | `\unsure{les}` |
| 648 | 186 | `\unsure{)}` |
| 648 | 190 | `\unsure{\natural\|\sharp}` |
| 648 | 196 | `\unsure{\natural\|\sharp}` |
| 648 | 200 | `\unsure{\natural\|\sharp}` |
| 648 | 205 | `\unsure{\natural\|\sharp}` |
| 648 | 209 | `\unsure{hom.}` |
| 649 | 219 | `\unsure{\natural\|\sharp}` |
| 649 | 224 | `\unsure{\natural\|\sharp}` |
| 649 | 226 | `\unsure{\natural\|\sharp}` |
| 649 | 229 | `\unsure{Évidemment}` |
| 649 | 230 | `\unsure{\natural\|\sharp}` |
| 649 | 231 | `\unsure{\simeq}` |
| 649 | 235 | `\unsure{+}` |
| 649 | 237 | `\unsure{\natural\|\sharp}` |
| 649 | 242 | `\unsure{\gamma_{\rho,\sigma}\|\Gamma_{\rho,\sigma}}` |
| 649 | 247 | `\unsure{\sigma\|\rho}` |
| 649 | 248 | `\unsure{\sigma}` |
| 649 | 257 | `\unsure{\mathcal{G}_{\rho,\sigma}^{+}\|G_{\rho,\sigma}^{+}}` |
| 649 | 264 | `\unsure{\sim}` |
| 649 | 265 | `\unsure{\natural\|\sharp}` |
| 649 | 266 | `\unsure{\natural\|\sharp}` |
| 649 | 271 | `\unsure{hom.}` |
| 649 | 278 | `\unsure{\text{bisection}}` |
| 649 | 279 | `\unsure{\Gamma_{\rho,\sigma}^{\natural}/\mu_{\rho}}` |
| 649 | 280 | `\unsure{\natural\|\sharp}` |
| 649 | 282 | `\unsure{SZ_{\rho}}` |
| 650 | 292 | `\unsure{\natural\|\sharp}` |
| 650 | 295 | `\unsure{\natural\|\sharp}` |
| 650 | 298 | `\unsure{\natural\|\sharp}` |
| 650 | 299 | `\unsure{\widetilde{\Gamma}_{\mathbb{Q}}\|\widetilde{\Pi}_{\mathbb{Q}}}` |
| 650 | 312 | `\unsure{\omega\|0}` |
| 650 | 316 | `\unsure{a}` |
| 650 | 318 | `\unsure{\Pi}` |
| 650 | 320 | `\unsure{\omega\|0}` |
| 650 | 324 | `\unsure{!}` |
| 650 | 326 | `\unsure{[0]}` |
| 650 | 328 | `\unsure{M(\omega)L_{0}\|M(0)L_{0}}` |
| 650 | 329 | `\unsure{\omega\|0}` |
| 650 | 334 | `\unsure{\{M(\tfrac12)\}\|M(\tfrac12)}` |
| 650 | 344 | `\unsure{\natural\|\sharp}` |
| 651 | 356 | `\unsure{raffinements\|raffinement}` |
| 651 | 358 | `\unsure{V\|IV}` |
| 651 | 366 | `\unsure{0\|a}` |
| 651 | 366 | `\unsure{\natural\|\sharp}` |
| 651 | 368 | `\unsure{*}` |
| 651 | 372 | `\unsure{0\|a}` |
| 651 | 372 | `\unsure{\natural\|\sharp}` |
| 651 | 374 | `\unsure{\natural\|\sharp}` |
| 651 | 375 | `\unsure{formé\|formés}` |
| 651 | 376 | `\unsure{normalisent}` |
| 651 | 376 | `\unsure{ateur de\|ent le}` |
| 651 | 377 | `\unsure{\natural\|\sharp}` |
| 651 | 378 | `\unsure{trivialt}` |
| 651 | 379 | `\unsure{\natural\|\sharp}` |
| 651 | 380 | `\unsure{néct.}` |
| 651 | 382 | `\unsure{\widetilde{\Gamma}_{\mathbb{Q}}\|\widetilde{\Pi}_{\mathbb{Q}}}` |
| 651 | 384 | `\unsure{\widetilde{\Gamma}_{\mathbb{Q}}\|\widetilde{\Pi}_{\mathbb{Q}}}` |
| 651 | 384 | `\unsure{\natural\|\sharp}` |
| 651 | 388 | `\unsure{\natural\|\sharp}` |
| 651 | 389 | `\unsure{\natural\|\sharp}` |
| 651 | 393 | `\unsure{\natural\|\sharp}` |
| 651 | 394 | `\unsure{\natural\|\sharp}` |
| 651 | 398 | `\unsure{\natural\|\sharp}` |
| 651 | 399 | `\unsure{\natural\|\sharp}` |
| 651 | 402 | `\unsure{On peut}` |
| 652 | 408 | `\unsure{\mathcal{G}}` |
| 652 | 411 | `\unsure{+\|*}` |
| 652 | 412 | `\unsure{peut être}` |
| 652 | 413 | `\unsure{paraphraser}` |
| 652 | 416 | `\unsure{\natural\|\sharp}` |
| 652 | 420 | `\unsure{\natural\|\sharp}` |
| 652 | 420 | `\unsure{\natural\|\sharp}` |
| 652 | 423 | `\unsure{\natural\|\sharp}` |
| 652 | 424 | `\unsure{\natural\|\sharp}` |
| 652 | 429 | `\unsure{\natural\|\sharp}` |
| 652 | 431 | `\unsure{\natural\|\sharp}` |
| 653 | 451 | `\unsure{u\ \text{normalise}\ \mathcal{G}^{\natural}\ \text{et induit l'identité dans}\ \mathcal{G}^{+}/\mathcal{G}^{\natural}}` |
| 653 | 453 | `\unsure{\natural\|\sharp}` |
| 653 | 456 | `\unsure{\natural\|\sharp}` |
| 653 | 460 | `\unsure{\natural\|\sharp}` |
| 653 | 462 | `\unsure{\natural\|\sharp}` |
| 653 | 466 | `\unsure{cf. page}` |
| 653 | 466 | `\unsure{635}` |
| 653 | 466 | `\unsure{suite}` |
| 653 | 467 | `\unsure{une condition plus faible}` |
| 653 | 468 | `\unsure{cette condition}` |
| 653 | 469 | `\unsure{rajoutée}` |
| 653 | 470 | `\unsure{en principe}` |
| 653 | 470 | `\unsure{conséquence}` |
| 653 | 472 | `\unsure{auquel cas}` |
| 653 | 472 | `\unsure{\natural\|\sharp}` |
| 653 | 473 | `\unsure{induite par}` |
| 653 | 474 | `\unsure{où}` |
| 653 | 479 | `\unsure{évidemment}` |
| 653 | 481 | `\unsure{Compte tenu que}` |
| 653 | 483 | `\unsure{\sigma}` |
| 653 | 487 | `\unsure{(5^{*})}` |
| 653 | 488 | `\unsure{\natural\|\sharp}` |
| 653 | 490 | `\unsure{\varepsilon_2}` |
| 653 | 491 | `\unsure{\varepsilon_2\sigma}` |
| 653 | 493 | `\unsure{c')\|b')}` |
| 653 | 496 | `\unsure{\mathfrak{g}_{(b)}\|G_{(b)}}` |
| 653 | 497 | `\unsure{\mathfrak{g}_{(a,b)}}` |
| 653 | 498 | `\unsure{grpe}` |
| 653 | 499 | `\unsure{a)}` |
| 653 | 499 | `\unsure{à montrer}` |
| 653 | 500 | `\unsure{\mathfrak{g}\|G}` |
| 653 | 500 | `\unsure{(a,b,c)}` |
| 653 | 502 | `\unsure{\mathfrak{g}\|G}` |
| 653 | 502 | `\unsure{(a,b)}` |
| 653 | 504 | `\unsure{\mathfrak{g}_{(b)}\|G_{(b)}}` |
| 653 | 508 | `\unsure{\natural\|\sharp}` |
| 653 | 509 | `\unsure{de sorte}` |
| 654 | 520 | `\unsure{\alpha_{\mathcal{G}}\|\varepsilon_{\mathcal{G}}}` |
| 654 | 523 | `\unsure{Prouvons}` |
| 654 | 524 | `\unsure{\mathfrak{g}_{(a)(b)}\|G_{(a,b)}}` |
| 654 | 525 | `\unsure{(b)\|(a)}` |
| 654 | 527 | `\unsure{\natural\|\sharp}` |
| 654 | 542 | `\unsure{\natural\|\sharp}` |
| 654 | 549 | `\unsure{\natural\|\sharp}` |
| 654 | 552 | `\unsure{gagne}` |
| 654 | 555 | `\unsure{\natural\|\sharp}` |
| 654 | 560 | `\unsure{-1}` |
| 654 | 566 | `\unsure{(u'u)(\rho)}` |
| 654 | 574 | `\unsure{\rho^{-1}}` |
| 654 | 581 | `\unsure{u'(\alpha_0\sigma)\alpha'\sigma\tau}` |
| 654 | 589 | `\unsure{\natural\|\sharp}` |
| 654 | 591 | `\unsure{\natural\|\sharp}` |
| 654 | 592 | `\unsure{\tau'}` |
| 654 | 595 | `\unsure{\hookrightarrow\|\Rightarrow}` |
| 654 | 599 | `\unsure{est}` |
| 654 | 600 | `\unsure{\natural\|\sharp}` |
| 654 | 602 | `\unsure{\mathcal{G}^{\natural}_\tau\mathcal{G}^{+}\| \mathcal{G}^{\natural}_\tau/\mathcal{G}^{+}}` |
| 654 | 604 | `\unsure{\uline{en}}` |
| 655 | 611 | `\unsure{\natural\|\sharp}` |
| 655 | 612 | `\unsure{\natural\|\sharp}` |
| 655 | 622 | `\unsure{on aurait}` |
| 655 | 623 | `\unsure{encore}` |
| 655 | 626 | `\unsure{\dot{\varepsilon}\,u'(\sigma)^{\cdot} \dot{\alpha}'\dot{\tau}}` |
| 655 | 644 | `\unsure{\text{ou}}` |
| 655 | 651 | `\unsure{signifie}` |
| 655 | 654 | `\unsure{\varepsilon_2'}` |
| 655 | 655 | `\unsure{(\varepsilon'_2)^{\cdot}}` |
| 655 | 658 | `\unsure{\dot{\varepsilon}'_2\|\varepsilon'_2}` |
| 655 | 665 | `\unsure{(10)}` |
| 655 | 668 | `\unsure{\tau}` |
| 655 | 681 | `\unsure{est dans}` |
| 655 | 684 | `\unsure{\natural\|\sharp}` |
| 655 | 689 | `\unsure{(*)}` |
| 656 | 699 | `\unsure{multiplicative}` |
| 656 | 700 | `\unsure{tte}` |
| 656 | 701 | `\unsure{\natural\|\sharp}` |
| 656 | 705 | `\unsure{\natural\|\sharp}` |
| 656 | 719 | `\unsure{\natural\|\sharp}` |
| 656 | 720 | `\unsure{\mathcal{G}}` |
| 656 | 721 | `\unsure{Condition\|condition}` |
| 656 | 725 | `\unsure{retombe}` |
| 656 | 727 | `\unsure{\omega\|0}` |
| 656 | 737 | `\unsure{\widetilde{M}_{0,3}\|M_{0,3}}` |
| 656 | 741 | `\unsure{\omega\|0}` |
| 656 | 742 | `\unsure{M_{0,3}(0)}` |
| 656 | 744 | `\unsure{\mathcal{G}_{0,3}}` |
| 656 | 748 | `\unsure{\natural\|\sharp}` |
| 656 | 753 | `\unsure{M^{!}[0]\|M^{\prime!}[0]}` |
| 656 | 758 | `\unsure{trivial\textsuperscript{mt}}` |
| 656 | 759 | `\unsure{\natural\|\sharp}` |
| 656 | 761 | `\unsure{NB}` |
| 656 | 761 | `\unsure{tous les sous-groupes}` |
| 656 | 762 | `\unsure{contenus par}` |
| 656 | 763 | `\unsure{\mathcal{G}^{\natural}=M(0)_2.L_0^\Pi\| \mathcal{G}^{\natural}=M(\omega)_2.L_0^\Pi}` |
| 656 | 765 | `\unsure{M^{!}[0]\|M^{\prime!}[0]}` |
| 656 | 766 | `\unsure{expliciter}` |
| 656 | 767 | `\unsure{(i.e. pourquoi)}` |
| 656 | 768 | `\unsure{\notin\|\in}` |
| 656 | 770 | `\unsure{\natural\|\sharp}` |
| 656 | 772 | `\unsure{p.r.v.\|p.r. au}` |
| 656 | 773 | `\unsure{avant}` |
| 657 | 785 | `\unsure{caractère}` |
| 657 | 786 | `\unsure{\#\|\prime}` |
| 657 | 796 | `\unsure{\omega\|0}` |
| 657 | 803 | `\unsure{induise\|produise}` |
| 657 | 804 | `\unsure{\natural\|\sharp}` |
| 657 | 806 | `\unsure{Dans la nouvelle version}` |
| 657 | 807 | `\unsure{\natural\|\sharp}` |
| 657 | 808 | `\unsure{\natural\|\sharp}` |
| 657 | 812 | `\unsure{M[0]^!_0\|M[0]_0}` |
| 657 | 813 | `\unsure{\omega\|0}` |
| 657 | 815 | `\unsure{trop}` |
| 657 | 816 | `\unsure{un peu tr.}` |
| 657 | 817 | `\unsure{(ancienne version)}` |
| 657 | 826 | `\unsure{introduire}` |
| 657 | 827 | `\unsure{M^![0]_0\|M^{\prime!}[0]_0}` |
| 657 | 828 | `\unsure{0\|\omega}` |
| 657 | 828 | `\unsure{L_0^{\Pi_0}\|\Pi_0}` |
| 657 | 831 | `\unsure{\natural\|\sharp}` |
| 657 | 836 | `\unsure{$Z$}` |
| 657 | 836 | `\unsure{\natural\|\sharp}` |
| 657 | 837 | `\unsure{\natural\|\sharp}` |
| 657 | 841 | `\unsure{\natural\|\sharp}` |
| 657 | 842 | `\unsure{\natural\|\sharp}` |
| 657 | 843 | `\unsure{\subset\|\Leftarrow}` |
| 657 | 848 | `\unsure{\natural\|\sharp}` |
| 657 | 850 | `\unsure{\mathcal{G}^{\natural}_{0\tau}}` |
| 657 | 853 | `\unsure{\natural\|\sharp}` |
| 657 | 855 | `\unsure{\natural\|\sharp}` |
| 657 | 862 | `\unsure{sont compatibles}` |
| 657 | 864 | `\unsure{\natural\|\sharp}` |
| 657 | 866 | `\unsure{si on suppose}` |
| 657 | 868 | `\unsure{\natural\|\sharp}` |
| 657 | 871 | `\unsure{voit}` |
| 657 | 873 | `\unsure{$\rho,\sigma$}` |
| 658 | 879 | `\unsure{en}` |
| 658 | 879 | `\unsure{restreignant}` |
| 658 | 887 | `\unsure{\natural\|\sharp}` |
| 658 | 888 | `\unsure{L_0}` |
| 658 | 888 | `\unsure{\natural\|\sharp}` |
| 658 | 893 | `\unsure{ens}` |
| 658 | 896 | `\unsure{\natural\|\sharp}` |
| 658 | 896 | `\unsure{\natural\|\sharp}` |
| 658 | 897 | `\unsure{\ldots}` |
| 658 | 898 | `\unsure{\natural\|\sharp}` |
| 658 | 899 | `\unsure{\natural\|\sharp}` |
| 658 | 900 | `\unsure{ce qui}` |
| 658 | 900 | `\unsure{surprend}` |
| 658 | 905 | `\unsure{\natural\|\sharp}` |
| 658 | 906 | `\unsure{i}` |
| 658 | 913 | `\unsure{\natural\|\sharp}` |
| 658 | 918 | `\unsure{\natural\|\sharp}` |
| 658 | 924 | `\unsure{\natural\|\sharp}` |
| 658 | 941 | `\unsure{)}` |
| 658 | 941 | `\unsure{déduites}` |
| 658 | 959 | `\unsure{\varepsilon_{2,\sigma}\|\varepsilon_{2\gamma}}` |
| 658 | 967 | `\unsure{)}` |
| 659 | 986 | `\unsure{Z_\rho}` |
| 659 | 992 | `\unsure{ou}` |
| 659 | 993 | `\unsure{respt}` |
| 659 | 1004 | `\unsure{\natural\|\sharp}` |
| 659 | 1009 | `\unsure{,}` |
| 659 | 1011 | `\unsure{Plus}` |
| 659 | 1020 | `\unsure{\text{est }\varepsilon[\tau](\rho)}` |
| 659 | 1021 | `\unsure{\natural\|\sharp}` |
| 659 | 1024 | `\unsure{\natural\|\sharp}` |
| 659 | 1029 | `\unsure{,}` |
| 659 | 1032 | `\unsure{\natural\|\sharp}` |
| 659 | 1033 | `\unsure{aura}` |
| 659 | 1036 | `\unsure{\natural\|\sharp}` |
| 659 | 1037 | `\unsure{\natural\|\sharp}` |
| 659 | 1043 | `\unsure{\natural\|\sharp}` |
| 659 | 1046 | `\unsure{\natural\|\sharp}` |
| 659 | 1047 | `\unsure{\natural\|\sharp}` |
| 659 | 1054 | `\unsure{ds.}` |
| 659 | 1055 | `\unsure{\natural\|\sharp}` |
| 659 | 1056 | `\unsure{ce qui}` |
| 659 | 1056 | `\unsure{me ferait\|on ferait}` |
| 659 | 1059 | `\unsure{\natural\|\sharp}` |
| 659 | 1059 | `\unsure{\natural\|\sharp}` |
| 659 | 1061 | `\unsure{577\|579}` |
| 659 | 1072 | `\unsure{\natural\|\sharp}` |
| 659 | 1073 | `\unsure{\natural\|\sharp}` |
| 659 | 1078 | `\unsure{\natural\|\sharp}` |
| 659 | 1079 | `\unsure{i_{L_0,S_0G}\|i_{L_0,G}}` |
| 659 | 1080 | `\unsure{\natural\|\sharp}` |
| 659 | 1083 | `\unsure{\iota(l)\|i(l)}` |
| 660 | 1095 | `\unsure{\natural\|\sharp}` |
| 660 | 1097 | `\unsure{\natural\|\sharp}` |
| 660 | 1098 | `\unsure{\natural\|\sharp}` |
| 660 | 1099 | `\unsure{L_0^{\natural}\|L_0^{\sharp}}` |
| 660 | 1105 | `\unsure{\natural\|\sharp}` |
| 660 | 1106 | `\unsure{\natural\|\sharp}` |
| 660 | 1107 | `\unsure{\natural\|\sharp}` |
| 660 | 1109 | `\unsure{\natural\|\sharp}` |
| 660 | 1118 | `\unsure{\longrightarrow}` |
| 660 | 1120 | `\unsure{\natural\|\sharp}` |
| 660 | 1123 | `\unsure{\natural\|\sharp}` |
| 660 | 1125 | `\unsure{G_{\rho,\sigma}}` |
| 660 | 1126 | `\unsure{\natural\|\sharp}` |
| 660 | 1127 | `\unsure{\natural\|\sharp}` |
| 660 | 1128 | `\unsure{\longrightarrow}` |
| 660 | 1137 | `\unsure{\natural\|\sharp}` |
| 660 | 1141 | `\unsure{\natural\|\sharp}` |
| 660 | 1142 | `\unsure{\natural\|\sharp}` |
| 660 | 1163 | `\unsure{\varepsilon_G=\varepsilon_\gamma\delta_G}` |
| 660 | 1167 | `\unsure{\chi}` |
| 660 | 1181 | `\unsure{noté}` |
| 660 | 1181 | `\unsure{\ldots}` |
| 660 | 1185 | `\unsure{avec}` |
| 660 | 1185 | `\unsure{\natural\|\sharp}` |
| 660 | 1189 | `\unsure{\natural\|\sharp}` |
| 661 | 1197 | `\unsure{ds\|dans}` |
| 661 | 1206 | `\unsure{G_{\rho,\sigma}}` |
| 661 | 1208 | `\unsure{\natural\|\sharp}` |
| 661 | 1210 | `\unsure{\natural\|\sharp}` |
| 661 | 1234 | `\unsure{\natural\|\sharp}` |
| 661 | 1236 | `\unsure{\natural\|\sharp}` |
| 661 | 1247 | `\unsure{$G_{\rho,\sigma}$}` |
| 661 | 1248 | `\unsure{\natural\|\sharp}` |
| 661 | 1250 | `\unsure{couples}` |
| 661 | 1250 | `\unsure{quadruples\|quadrupliens}` |
| 661 | 1261 | `\unsure{\natural\|\sharp}` |
| 661 | 1265 | `\unsure{\varepsilon_2\|\varepsilon_\tau}` |
| 661 | 1267 | `\unsure{\natural\|\sharp}` |
| 661 | 1270 | `\unsure{\natural\|\sharp}` |
| 661 | 1279 | `\unsure{f^{-1}\uline{u}}` |
| 661 | 1281 | `\unsure{\natural\|\sharp}` |
| 661 | 1284 | `\unsure{f}` |
| 661 | 1285 | `\unsure{\natural\|\sharp}` |
| 661 | 1296 | `\unsure{E\|\mathcal E}` |
| 661 | 1298 | `\unsure{\operatorname{Ker}}` |
| 661 | 1298 | `\unsure{Z_0}` |
| 661 | 1299 | `\unsure{\natural\|\sharp}` |
| 661 | 1300 | `\unsure{\natural\|\sharp}` |
| 661 | 1301 | `\unsure{\}}` |
| 661 | 1304 | `\unsure{\natural\|\sharp}` |
| 661 | 1305 | `\unsure{\mathcal G^{\natural}\|\mathcal G}` |
| 661 | 1306 | `\unsure{)}` |
| 661 | 1314 | `\unsure{\natural\|\sharp}` |
| 661 | 1315 | `\unsure{\natural\|\sharp}` |
| 661 | 1319 | `\unsure{\natural\|\sharp}` |
| 661 | 1321 | `\unsure{Z_{\rho,\sigma}^{\circ+}\|Z_{\rho,\sigma}}` |
| 661 | 1321 | `\unsure{\}}` |
| 661 | 1321 | `\unsure{)}` |
| 661 | 1324 | `\unsure{\natural\|\sharp}` |
| 662 | 1328 | `\unsure{\natural\|\sharp}` |
| 662 | 1334 | `\unsure{\natural\|\sharp}` |
| 662 | 1335 | `\unsure{\natural\|\sharp}` |
| 662 | 1336 | `\unsure{\natural\|\sharp}` |
| 662 | 1344 | `\unsure{\natural\|\sharp}` |
| 662 | 1345 | `\unsure{\natural\|\sharp}` |
| 662 | 1350 | `\unsure{dont\|déf.}` |
| 662 | 1352 | `\unsure{Z_0\|L_0}` |
| 662 | 1352 | `\unsure{L_0}` |
| 662 | 1353 | `\unsure{injectif}` |
| 662 | 1353 | `\unsure{par}` |
| 662 | 1354 | `\unsure{proj.\|passage}` |
| 662 | 1354 | `\unsure{au}` |
| 662 | 1354 | `\unsure{quotient}` |
| 662 | 1355 | `\unsure{\natural\|\sharp}` |
| 662 | 1357 | `\unsure{\natural\|\sharp}` |
| 662 | 1358 | `\unsure{\natural\|\sharp}` |
| 662 | 1359 | `\unsure{i_{L_0,SG}\|i_{L_0,S_0G}}` |
| 662 | 1360 | `\unsure{\natural\|\sharp}` |
| 662 | 1361 | `\unsure{\natural\|\sharp}` |
| 662 | 1363 | `\unsure{i_{L_0,SG}\|i_{L_0,S_0G}}` |
| 662 | 1364 | `\unsure{\natural\|\sharp}` |
| 662 | 1366 | `\unsure{\natural\|\sharp}` |
| 662 | 1367 | `\unsure{\natural\|\sharp}` |
| 662 | 1374 | `\unsure{\natural\|\sharp}` |
| 662 | 1374 | `\unsure{\natural\|\sharp}` |
| 662 | 1375 | `\unsure{\natural\|\sharp}` |
| 662 | 1385 | `\unsure{\natural\|\sharp}` |
| 662 | 1386 | `\unsure{\natural\|\sharp}` |
| 662 | 1387 | `\unsure{\natural\|\sharp}` |
| 662 | 1388 | `\unsure{\natural\|\sharp}` |
| 662 | 1396 | `\unsure{\natural\|\sharp}` |
| 662 | 1400 | `\unsure{projection\|présentation}` |
| 662 | 1402 | `\unsure{\natural\|\sharp}` |
| 662 | 1403 | `\unsure{où}` |
| 662 | 1404 | `\unsure{définirait\|définissait}` |
| 662 | 1406 | `\unsure{a\|en}` |
| 662 | 1408 | `\unsure{desserrer\|donner}` |
| 662 | 1408 | `\unsure{moule\|modèle}` |


## Research notes — English

These notes concern questions, tentative expectations, assertions left unproved here, and possible further checks suggested by this excerpt. The categories describe the status of the passage on these pages, not its status elsewhere in the manuscript or literature. Cancelled claims are identified as cancelled. Notes labelled **own idea** are proposed investigations with stated confidence and reasons, not amendments to the transcription.

### Scans 644–647

#### Research notes (English)

- **Scan 644, first diagram — unproved claim / question.** The bottom arrow is labelled “?”. The surrounding text reduces a kernel statement involving `M°(−j̄)` to the existence of a commutative factorization through `μ × μ`; checking the map requires the earlier definition (45), which is outside this package. The question mark is retained as a written uncertainty rather than interpreted as an asserted construction.
- **Scan 644, middle — unproved claim.** “n’est autre que ε₂” identifies the displayed composite with a sign character. A proof would need to compare that character with the reduction modulo 4 appearing in the diagram, keeping the overwritten stages distinct from the final arrows.
- **Scan 644, bottom — unproved claim.** “est donnée par ε₂(u)” refers the action computation to an earlier page. Checking the reference would require the earlier page, provisionally read as 554 (alternative 594), and the exact convention for the action induced by (45); these scans alone do not supply it.

##### Scan 645 research notes (English)

- **Scan 645, after the first diagram — conjecture / verification requested.** “il faudrait vérifier que cet hom … n’est autre que ε₃” explicitly leaves the identification to be checked. The inserted correction changes the proposed kernel, so the nearby canceled argument should not be used as an established proof of that identification.
- **Scan 645, insertion — unproved claim / deferred correction.** “le noyau n’est pas Ker(ε₃ | M″!) … mais M₀″!” is followed by “on va y revenir plus bas”. Establishing this correction would require the definitions of the decorated subgroups and a direct comparison of the homomorphism’s kernel with the sign character’s kernel. The exact lead-in and one canceled word are low-confidence readings.
- **Scan 645, canceled lower half — unproved claim in a discarded argument.** “il est donc 1, ou d’ordre 2” follows the trivial-intersection claim for the subgroup denoted Dρ. The canceled passage is worth checking as an index-two subgroup argument, but its canceled status and the correction above preclude treating it as a final assertion here.

##### Scan 646 research notes (English)

- **Scan 646, canceled proposition — unproved claim in a discarded formulation.** “induit … isomorphismes évidents sur les facteurs” asserts compatibility with two three-step filtrations. A proof would compare the maps on the two sign factors and the middle factor, then deduce the kernel; the diagonal cancellation and the revised kernel notation below must be respected when assessing the statement.
- **Scan 646, lower half — unproved claim.** “Admettant ce point” makes the ensuing kernel computation conditional on the preceding identification. The calculation intersects the corrected kernel with Nρ*; validating it requires the definitions of M₀″!, M₀!, and Zρ₀! from earlier pages.
- **Scan 646, last lines — unpursued implication.** “on a bien un hom injectif” uses the intersection computation to eliminate the residual kernel considered on the preceding page. The conclusion continues onto scan 647, where equal finite orders are invoked; the precise numbered reference is (46) or (45), not securely distinguished in the ink.

##### Scan 647 research notes (English)

- **Scan 647, opening continuation — unproved claim.** “ont même ordre 24” upgrades the preceding injective homomorphism to an isomorphism. The order count is not repeated here; checking it needs the preceding constructions and the exact group intended by the numbered map.
- **Scan 647, (49) and (52) — unproved claim.** The marked isomorphism from Zσ₀! to γρ,σ and the sequence labelled “exacte” summarize assertions cited at pages 615 and 616. A full proof would verify that the displayed homomorphisms have the stated image and kernel, using the original normalization and central-subgroup conventions.
- **Scan 647, (48)–(52) — own idea.** The displayed isomorphism and central extension suggest testing whether this fiber-product construction can be reconstructed as a pullback of the second sequence along the first map. **Confidence: medium**, because the fiber products and maps are visible, but the definitions of their common quotient and all structural maps are not given in full on this page. This is a proposed verification, not a claim of novelty or an established result.

### Scans 648–652

#### Research notes (English; separate from the transcription)

##### 648-R1 — Unproved claim — scan 648, lower quarter, before the second (55)

“Il est clair alors par (52)” introduces the asserted exact sequence with kernel `\mu_\rho`. A proof would need to check the kernel and surjectivity of the projection from the fibre-product subgroup defined in (53), with the exact maps of (52), rather than infer exactness merely from the displayed inclusions.

##### 648-R2 — Unpursued implication — scan 648, (54)–(55)

The phrase “plongement central” and the displayed intersection select two of the three central sign factors inside the distinguished subgroup. It is worth tracking how each of those two factors survives the later quotient by `\mu_\rho`; the intersection identity alone does not identify their subsequent roles.

##### 649-R1 — Unproved claim — scan 649, first prose paragraph and (57)

“Évidemment le sous-groupe” introduces a containment followed by a diagram of exact sequences. Verifying this claim requires checking the indicated maps on the two central factors and the swashed-G factor, including the kernel written beneath the upper row; the overwritten letter at the lower quotient should be settled from adjacent definitions before using the diagram as a formal proof.

##### 649-R2 — Unpursued implication — scan 649, (56), (58)

The isomorphism in (56) is stated to respect the indicated subgroup: “il s'envoie isomorphiquement”. One can therefore ask whether the diagram (58), with its accompanying identifications, gives a canonical comparison of the extensions or depends on the earlier choices implicit in the notation; these pages alone do not spell out that dependence.

##### 649-R3 — Unproved claim — scan 649, (59) and the last lines

The epimorphism “admet une ‘bisection’”, and its proposed bisection meets the kernel in `\mu_\rho\times1`. A proof must establish both the surjectivity from that subgroup onto the quotient and the stated intersection; the crossed-out quotient in this passage is important evidence of the distinction between a bisection before quotienting and a section after quotienting.

##### 650-R1 — Unproved claim — scan 650, (60)

The two displayed product decompositions and the intersection `\Gamma^\natural\cap S\Gamma=\mu_\rho` are stated without an accompanying argument on this page. A proof must check generation by the two factors, their intersection, and what the dot in the second line is intended to assert about the product after quotienting; the transcription does not upgrade that dot to a direct or semidirect product symbol.

##### 650-R2 — Unpursued implication — scan 650, final paragraph

“il faudrait d'abord introduire les groupes adéquats” identifies the postponed task of following the listed distinguished subgroups through the homomorphism. The later definitions should be checked against each subgroup in this list, including the inserted equality annotations, rather than only against the ambient groups.

##### 650-R3 — Own idea — scan 650, (60); confidence: medium

As a possible way to organize the verification, first pass to the quotient by the displayed central `\mu_\rho`, establish the intersection and action there, and only then ask what additional data recover the group before quotienting. This is a suggested proof strategy, not an asserted result: its motivation is precisely the difference between the two lines of (60), and it depends on the earlier exact sequences being correct.

##### 651-R1 — Unproved claim — scan 651, middle revised paragraph

The revised subgroup is said to be “un sous-groupe ouvert”, and its image in the arithmetic quotient is also called “ouvert”. Establishing this requires specifying the topology on the acting group and checking that the revised condition, including trivial action on the displayed finite quotient, defines an open subgroup; the normalizer wording crossed out nearby should not be silently substituted for that stronger condition.

##### 651-R2 — Conjecture (proposed investigation, not a theorem) — scan 651, lower middle

Grothendieck writes “on peut se proposer d'étudier les représentations” of the resulting open subgroup in suitable profinite groups. The concrete choices of target groups, the representations of interest, and what arithmetic information they are intended to preserve are left unspecified on this page.

##### 651-R3 — Unproved claim — scan 651, last three displays

The examples introduced by “Un cas intéressant sera celui où” identify the resulting `M`-subgroups for the choices `\Pi_0`, `\Pi`, and the ambient swashed `G`. Checking these identifications requires comparing the revised quotient-action condition with the earlier definitions of the decorated `M`-groups; the final choice is transcribed without supplying an absent plus sign.

##### 652-R1 — Conjecture (tentative claim) — scan 652, first paragraph, lines 4–7

The qualification “peut être seulement un s-groupe ouvert” makes the claim about the subgroup generated by the indicated elements tentative. To turn this into a statement, one would need the precise group scheme and integral adelic group, the intended meaning of generation, and the hypotheses ensuring that the generated subgroup is open; none of those verifications is supplied on this page.

##### 652-R2 — Unpursued implication — scan 652, first paragraph, lines 7–10

The proposed adaptation to “le cas schématique” is explicitly deferred by “J'y reviendrai par la suite.” A later treatment should distinguish which constructions are carried out on the group scheme from those carried out on its adelic points, and check that the maps and quotients used here survive that change of setting.

##### 652-R3 — Own idea — scan 652, first paragraph, final two lines; confidence: high as a clarification task

The suggestion to choose the “composante neutre” for the distinguished subgroup should be made precise in the scheme setting before interpreting it at the level of adelic points. The reason for this clarification is the explicit shift to a scheme immediately before that suggestion; these scans do not say which object the connected component is taken in, and the note asserts no equality between different notions of connected component.

##### 652-R4 — Own idea — scan 652, last paragraph and (3); confidence: medium

Since the distinguishing superscript is deliberately suppressed in subsequent notation, retain the chosen invariant subgroup as an explicit parameter when comparing constructions. One useful check would be to vary that subgroup by inclusion and determine whether the products with `\{1,\tau\}` in (3), and later group constructions, admit compatible comparison maps; this is a proposed test motivated by the displayed dependence, not a result established here.

### Scans 653–657

#### Research notes (English; separate from transcription)

- **Scan 653, proof after (5) — conjecture / expressed doubt.** “Je ne pense pas que la condition a) définisse à elle seule un sous-groupe.” Grothendieck explicitly doubts that condition a) is closed under the group operation on its own; the following proof instead uses condition b) to control composition. A useful check would isolate a finite quotient in which a) alone fails, without reading such a counterexample into the manuscript.
- **Scan 653, (4) and left marginal addition — unproved claim.** The cancelled note claims that the last condition added to d) follows from a) and b) when ε₂ε₃=1 (the precise connecting words are uncertain). The relevant verification is the induced action on the indicated quotient by G^natural; cancellation makes this a record of a working claim, not a settled assertion.
- **Scan 654, (8), final paragraph — conjecture / local existence problem.** The sign ε is to be chosen so that α'' lies in the required subgroup, with the explicit qualification “si possible”. This is a local problem in the proof: the next scan attempts to choose that sign after reduction modulo the distinguished subgroup, so this wording should not be presented as an independent global conjecture.
- **Scan 654, (7)–(8) — own idea.** The two composition formulas could be checked in a finite quotient that retains the central signs and the images of ρ, σ and τ, thereby separating errors of transcription from a possible sign obstruction. Confidence: medium; the formulas explicitly reduce the problem to membership and signs, but the precise subgroup hypotheses must first be read securely.
- **Scan 655, (9)–(11) — unpursued implication.** The sign choice is made explicit as ε=-ε₂'ε₃', followed by the composition formula (10) and “Cela achève la démonstration”. This supplies a concrete way to test whether the exceptional composition case depends only on the two sign characters; the manuscript does not isolate that dependence here as a separate statement.
- **Scan 656, cancelled opening remark — unproved claim.** The crossed-out remark says that, for b) to be multiplicative, one does not need a) “dans … sa force” and that it suffices to normalise the image of Lσ in the quotient. A proof would compare the stated normalisation condition with the conjugator required in the preceding composition calculation; the cancellation must remain part of any account of this claim.
- **Scan 656, (12) — unproved claim.** “Si G est ‘assez gros’, l'hom de projection est injectif”, with a reference to p. 578. These pages do not state a formal largeness hypothesis; checking the referenced page is necessary before treating injectivity as a theorem under explicit assumptions.
- **Scan 656, right margin beside (14) — conjecture / question.** The margin asks to “expliciter à nouveau pourquoi” and mentions the tuple (ε₀,1,1,1) and Zρ,σ. The membership symbol and intervening words are uncertain, so the note identifies a requested clarification without deciding whether membership or non-membership was being asserted.
- **Scan 657, cancelled upper-left note — conjecture / expectation.** “Mais je voudrais obtenir” introduces the displayed group M^Π₀[0], while the examples are described tentatively as too large and too small. The note records a desired outcome during revision of the definition; its cancellation and uncertain connecting phrases prevent treating it as a stable specification.
- **Scan 657, cancelled upper-right note — unproved claim.** “Avec la nouvelle définition … on aura finalement” precedes Zρ,σ=M![0], said to agree with the preceding case b). The surrounding changes to condition (4) must be tracked before proving this equality; the cancelled note is evidence of a proposed correction rather than a final conclusion.
- **Scan 657, (16)–(17) — conjecture / proposed construction.** The examples “suggèrent l'opportunité” of introducing a subgroup G₀^natural invariant in G with G^natural=G₀^natural×μ, and then choosing the conjugators α,β in μτ G₀^natural. A proof would need to check whether the earlier closure argument survives this additional restriction and how it depends on the chosen complement.
- **Scan 657, final remark — unproved claim.** The simpler definition from p. 578 is said to make the subgroup property evident, but the revised text denies that the conditions give a trivial action on G⁺/Π, even under the indicated containment hypothesis. The next page continues the sentence; the statement should be assessed with that continuation and with the crossed-out formulation kept distinct.
- **Scan 657, (16)–(17) — own idea.** Compare the groups obtained from two invariant complements to μ, when two such complements exist, to determine whether the refinement depends on the complement or only on the ambient extension. Confidence: medium; the manuscript explicitly chooses extra subgroup data but does not address uniqueness or change of choice on this page.

### Scans 658–662

#### Research notes (English; separate from the transcription)

- **Scan 658, opening paragraph — unpursued implication.** “Il est vrai … que \(u(\rho)\) est conjugué dans \(\mathcal G^+\) … mais en général il ne le sera pas par un élément … de \(\pi\).” The manuscript distinguishes ambient conjugacy from conjugacy by the smaller subgroup. An explicit comparison of the two orbits would clarify exactly where the restriction on the sign \(\varepsilon_3\) becomes necessary.
- **Scan 658, left margin beside (18) — unpursued implication.** “l'inclusion peut être stricte” records that the subgroup defined through inner automorphisms can be larger than \(L_0\cap\mathcal G^{\natural}\), with a reference to example c). This is worth checking directly against the earlier example, since the replacement of the original right side of (18) changes the construction.
- **Scan 658, (19)–(20) — unproved claim.** “injectif ssi on a” introduces the trivial-center-intersection criterion. A proof requires identifying the kernel of the inner-automorphism map on \(L_0^{\natural}\) with its intersection with the center of \(\mathcal G^+\); one must also retain the explicit character coordinates in (19).
- **Scan 658, after (20) — unproved claim.** “l'image invariante” is stated without a proof on this page. The required verification is that conjugation by each element of \(Z_{\rho,\sigma}\) preserves the embedded copy of \(L_0^{\natural}\), so that the quotient in (21) is defined.
- **Scan 659, (24) and following paragraph — unproved claim.** “l'indice 4 ne pouvant se présenter que pour” the circle-marked subgroups summarizes the index calculation without displaying it. A proof can be organized by the image of the pair of sign characters and then compared with the inverse images in \(Z_{\rho,\sigma}\).
- **Scan 659, remark 1, (25)–(25bis) — unproved claim.** “La condition d) de (4) … est conséquence ici de a) b) c)” is followed by the generator congruences. The step from those congruences to every \(x\in\mathcal G^+\) requires checking the applicable generation and continuity hypotheses in the preceding setup.
- **Scan 659, lower left margin beside (26) — conjecture / expectation.** “C'est une raison de plus pour ne pas exiger …” records Grothendieck's choice to avoid a stronger trivial-action requirement because it would exclude \(\tau\). The exact final wording is uncertain, but the explicit obstruction represented by the distinguished element is worth tracking through the definitions.
- **Scan 659, (27)–(28) — own idea.** A useful check is to write the semidirect-product multiplication in the manuscript's factor order and verify directly that the anti-diagonal assignment in (28) is a homomorphism. **Confidence: high as a verification strategy**, because both its formula and its target are displayed here; this is a proposed check, not a claim that the subsequent construction has been independently proved.
- **Scan 660, (29)–(32) — unproved claim.** “d'où suites exactes” and “diagramme commutatif” assert the quotient sequences and their compatibility. A proof would need normality of the anti-diagonal image, injectivity of the indicated subgroup maps after taking the quotient, and verification of the common quotient \(\gamma_{\rho,\sigma}\).
- **Scan 660, (31)–(32) — own idea.** The diagram suggests checking a universal property for the quotient built by identifying the two copies of \(L_0^{\natural}\) inside the semidirect product. **Confidence: medium**, because the diagram displays the relevant identifications, but no universal property is stated on this page and the action conventions must first be fixed.
- **Scan 660, (33)–(34) — unpursued implication.** “On a maintenant” introduces the sign kernels and the kernel of \(\chi_G\). A systematic comparison of these subgroups with their counterparts in \(\gamma_{\rho,\sigma}\) could clarify which index assertions are inherited directly from (24), while preserving the manuscript's distinction between primes, the circle, and the plus sign.
- **Scan 661, proposition (38)–(40) — unproved claim.** “l'image … est formée des” introduces an image characterization by the four conditions in (39), followed by a kernel description. Neither assertion is proved on this page; a proof must establish both that the displayed homomorphism satisfies those conditions and that every admissible tuple lifts to the selected group.
- **Scan 661, (39) d) — unproved claim.** “automatique vu a), b) si \(\varepsilon_2=\varepsilon_3\)” gives an automatic-stability assertion. Its exact dependence on the two conjugacy conditions and on the equal-sign assumption should be checked before treating condition d) as redundant in that case.
- **Scan 661, surviving corollary (41) — unpursued implication.** “\(Z_0=\operatorname{Centr}_{\mathcal G^+}(L_0)\)” replaces a canceled attempt to describe the obstruction. This makes the relation between the kernel in (40) and the centralizer of \(L_0\) the next explicit question; the continuation on scan 662 should be read together with this revised definition.
- **Scan 662, (42) — unproved claim.** “Cette application est un hom de groupes” asserts multiplicativity of \(f\mapsto f^{-1}\underline u(f)\). A direct verification must use the action defining the semidirect product and should also explain the inserted equality with the product in the opposite order.
- **Scan 662, (43)–(44) — unproved claim.** “dont l'image est le noyau de (38)” identifies the quotient of the centralizer with the kernel. Together with the image characterization (39), this would require verifying both the kernel of (42) after passage to \(G_{\rho,\sigma}^{\natural}\) and surjectivity onto the described image group.
- **Scan 662, final remark — unpursued implication.** “la construction … est plus fine que celle où on le définirait simplement comme un groupe d'autom.” records the distinction between the constructed group and its automorphism/character image. The displayed sequence (44) makes the centralizer quotient a concrete obstruction to recovering the constructed group solely from that image; an example with a nontrivial quotient would illustrate the distinction.
- **Scan 662, (44) — own idea.** One can seek examples where \(Z_0^{\natural}/L_0^{\natural}\) vanishes and examples where it does not, while keeping the same four-condition image description. **Confidence: medium as a research direction**, because the sequence isolates exactly this quotient, but these pages supply no explicit nontrivial example and no claim of novelty is made.
