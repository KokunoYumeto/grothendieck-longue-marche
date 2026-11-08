# LM_C4-020-038 — Editorial and research notes

## Source, scope, and conventions

**Primary source (APA reference).** Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, Montpellier archive cote 140-4; supplied scans 20–38]. Université de Montpellier.

The bibliographic identity and date above are supplied by the attached task prompt. All readings in the transcription were made from the 19 supplied images. No published transcription or external edition was used to complete the handwriting. Citations within the research notes refer to this primary source by the supplied scan number and, where available, the manuscript's equation number or an approximate position.

The accompanying LaTeX file is a fragment beginning with `\scanpage{20}`. It preserves the French text, abbreviated forms, displayed formulas, repeated equation numbers, cancellations, insertions, and marginalia, with uncertainty marked in place. The original top foliation is entered only when visible; overwritten digits retain their alternatives. The smaller handwritten or pencilled numerals inside the lower border are included as marginal marks because their authorship cannot be established from these images. The printed institutional credit and pagination outside the manuscript border are archival additions and are excluded from the manuscript text.

The inventory contains **336 elements** across scans **20–38**, with every entry marked `yes`. This status records inclusion in the transcription; doubtful readings retain the confidence qualifications below. Margin notes are placed beside the corresponding passage in the linear reading order, and their physical positions are recorded in the inventory. Literal ellipses and repeated ditto strokes are retained when they occur in the manuscript.

## Overall legibility and verification

The principal prose and large formulas are generally more legible than their insertions and cancellations. The least secure material is the overlapping marginal writing on scan 20, the overwritten top foliation, several tiny subscripts and superscripts, the extensively revised algebra on scans 33–34, and the cancelled calculation on scan 38. Enlarged and rotated inspection was used for the difficult passages. Each page was reread against its transcription and inventory, followed by an independent visual audit of the page groups.

The fragment uses the requested editorial macros, standard mathematical LaTeX, `tikz-cd` for diagrams, and native TikZ for graphical enclosures and handwritten graphic marks. The host document must provide the editorial-macro definitions and the corresponding mathematics and TikZ packages. Delimiter and environment balance, scan coverage, allowed inventory kinds, and archive contents were checked. Full TeX compilation was unavailable because the installed engine lacked its format files and TeX packages; no compilation success is claimed.

The page-specific tables record readings, alternatives, and confidence. The abbreviation expansions belong only to these notes. Research notes remain separate from the transcription; proposed proofs, tests, and connections do not alter the source readings. Items marked **own idea** are suggestions with stated confidence and reasons, without claims of novelty or established validity. A claim may be proved or revised elsewhere in the manuscript; the notes concern what is left open on these supplied pages.

---

## Scan 20

### Doubts

| Scan | Approximate line or location | Reading | Alternatives / difficulty | Confidence |
|---|---|---|---|---|
| 20 | Opening line | en se donnant | Highly compressed small words between « aide » and « un système ». | medium |
| 20 | Below (35), first line | reconstitue | Ending is reduced to a horizontal stroke. | medium |
| 20 | Before « l'image inverse » | deleted = | Overwritten/cancelled mark may contain letters rather than an equality sign. | low |
| 20 | Before (36) | deleted schémas | Word crossed out underneath the replacement « Groupes sur S ». | medium |
| 20 | Below (36) | de fait | Visible words; their syntactic attachment to the preceding sentence is not supplied editorially. | high |
| 20 | Before « suites exactes » | des | Left end of the line overlaps the marginal note. | low |
| 20 | Lower-left note, opening | faite | Runs across the beginning of the main text. | medium |
| 20 | Lower-left note, second line | nul | nuls; singular/plural ending is compressed. | medium |
| 20 | Lower-left note | images inverses | Endings compressed; could be singular. | medium |
| 20 | Lower-left note, penultimate line | évidemment | d'ailleurs; cramped pale writing overlaps (37). | low |
| 20 | Middle object of (37) | (A) | (/A); a slanting stroke immediately before A may be a parenthesis or slash. | low |

### Abbreviations met

- `iso.`: isomorphisme.
- `schém.`: schéma.
- `conn.`: connexe.
- `∀`, in « sur ∀ schém. »: tout.

### Legibility

The central text, quotient comparison, and exact sequences are comparatively legible. The small cancellation before « l'image inverse » and the lower-left marginal note are substantially less secure; the note overlaps the main prose and the label (37). The pencilled `19` at lower left is retained as a marginal numeral, not identified with the top manuscript foliation.

### Research notes (English)

1. **Scan 20, below (35); unproved claim.** The text says that (34) « se reconstitue à partir de (35) » and gives an induced isomorphism of quotients. A proof would need to check both recovery of the extension data and compatibility of the recovered action with the morphism Φ; the preceding definition of (34) lies outside this assigned page.
2. **Scan 20, lower-left marginal note; unproved claim.** The note calls the vanishing hypothesis on H¹ « entièrement inutile » and says the relevant M-torsors are trivial. This stronger point deserves a separate proof explaining why the torsors arising as inverse images of h ∈ H are trivial over S₀, rather than merely becoming trivial over affine bases.
3. **Scan 20, (36)–(37); own idea.** Compare exactness on sections directly with the torsor obstruction for an arbitrary base S, retaining only the particular torsors produced by this extension. **Confidence: medium:** this follows the distinction explicitly made by the marginal note, but identifying the exact trivializations requires the earlier construction.

Final rereading: the replacement before (36) ends in plain S, with no visible subscript; the O in the H¹ formula has a visible underline, now retained as `\underline{\mathcal O}_S`.

Independent visual audit: the complete scan and enlarged difficult passages were compared with the transcription. No additional securely readable omitted text was found; the existing uncertain readings remain uncertain.

---

## Scan 21

### Doubts

| Scan | Approximate line or location | Reading | Alternatives / difficulty | Confidence |
|---|---|---|---|---|
| 21 | Top manuscript folio | 658 | Middle digit is retraced; top of numeral partly touches the border. | medium |
| 21 | Opening line | diagramme | Ending is a long horizontal stroke, possibly an abbreviation. | medium |
| 21 | Right vertical link in (38) | downward double arrow | Could be a vertical identity/isomorphism mark; retained with doubt inside diagram. | low |
| 21 | Right vertical link in (39) | downward double arrow | Curved double-stroke mark, possibly a vertical isomorphism sign. | low |
| 21 | Left marginal note | sans | Contracted writing immediately after the opening parenthesis. | medium |
| 21 | Left marginal note, cancelled word | schéma | Crossed through under replacement « faisceau ». | medium |
| 21 | Main paragraph after (39) | S₀-schéma | Base symbol is retraced and could be S alone. | medium |
| 21 | Same paragraph | manifestement | Ending highly compressed. | medium |
| 21 | Before « à cette dernière » | p.r. | par.; the abbreviation is compact. | low |
| 21 | Before (40) | hom. | The abbreviation's final stop is unclear. | medium |

### Abbreviations met

- `comm.`: commutatif.
- `diag.`: diagramme.
- `iso`: isomorphisme.
- `NB`: nota bene.
- `p.r.` (uncertain): par rapport.
- `hom.` (uncertain): homomorphisme.

### Legibility

The two ordinary commutative diagrams and the main paragraphs are relatively clear. The sloping marginal note has been read from an enlarged, rotated working view; its cancellation/replacement is uncertain. The double-stroke vertical signs at the H-terms are preserved as uncertain symbols rather than silently interpreted as equalities.

### Research notes (English)

1. **Scan 21, lower half; unproved claim.** The construction is described as « manifestement fonctorielle » with respect to a morphism of exact sequences. A complete verification should construct the induced morphism of the associated group schemes and establish compatibility with identities, compositions, and all maps of the extension diagram.
2. **Scan 21, left marginal note; unproved claim.** The note identifies the underlying sheaf with the « faisceau somme des H copies de M » and concludes representability when M is representable. It would be useful to specify the choices, if any, in the stated isomorphism and check that the sheaf coproduct is represented by the corresponding disjoint union.
3. **Scan 21, (38)–(39); unpursued implication.** Comparing the scheme-level extension and its section diagram suggests separating functoriality of the representing object from exactness after taking sections. The relationship between these two assertions is especially relevant to the removed H¹ hypothesis on scan 20.

Independent visual audit: the complete scan and enlarged difficult passages were compared with the transcription. No additional securely readable omitted text was found; the existing uncertain readings remain uncertain.

---

## Scan 22

### Doubts

| Scan | Approximate line or location | Reading | Alternatives / difficulty | Confidence |
|---|---|---|---|---|
| 22 | (41), second row, start of first arrow | deleted 1 | A small symbol is overdrawn by the thickened arrow; 1 is the best reading. | low |
| 22 | (41), third row, M | superscript dot | Clearly visible dot, but possibly incidental ink rather than notation. | low |
| 22 | (41), vertical Hₛ₀ link | vertical double stroke | Exact decoration is unclear where the horizontal row intersects it. | low |
| 22 | (41), third row, after final 1 | deleted 1 | Blackened displaced numeral at right. | medium |
| 22 | §4, before Z-module | deleted g | A visible descender remains below the overwritten initial letter; no complete deleted word is supplied. | low |
| 22 | Paragraph after (42) | gén. | Final stop not clearly separable from the following comma. | medium |
| 22 | Same paragraph | distingué | Initial letters retraced; no definite separate cancellation established. | medium |
| 22 | Below (43) | est une | Both words compressed, with « est » near the right edge and « une » at next line's start. | medium |

### Abbreviations met

- `gén.`: généralement.
- `i.e.`: id est.
- `∀`, before sous-module and sous-groupe: tout.

### Legibility

The large staggered extension diagram is readable but contains overdrawn elements, an isolated dot next to the unprimed M, and an ambiguous double vertical stroke at Hₛ₀. The prose is mostly clear; the correction at the beginning of « Z-module » was preserved at letter level because no complete underlying word can be read. The lower-left pencilled numeral is 21.

### Research notes (English)

1. **Scan 22, (41); unpursued implication.** The staggered four-row diagram makes compatibility between a morphism of extensions and the passage to associated group schemes explicit. A useful further check is whether the two possible routes around each face give strict equality of morphisms or require choices from the construction.
2. **Scan 22, (43)–(44); unproved claim.** The quotient Hᵢ is called « une extension » of H by M/Mᵢ, obtained from (27) by M → M/Mᵢ. A complete argument would verify the normality condition expressed by « distingué dans G i.e. stable par H » and identify the quotient extension with the induced pushout.
3. **Scan 22, §4; own idea.** Distinguish the collection of all finite-index subgroups of M from its H-stable subcollection before forming the later inverse system. **Confidence: high:** the H-stability condition is written explicitly here, and any cofinality assertion must account for the action rather than treat the two index sets as identical by definition.

Independent visual audit: the complete scan and enlarged difficult passages were compared with the transcription. No additional securely readable omitted text was found; the existing uncertain readings remain uncertain.

---

## Scan 23

### Doubts

| Scan | Approximate line or location | Reading | Alternatives / difficulty | Confidence |
|---|---|---|---|---|
| 23 | Top folio | 659 | Middle digit retraced, as on scan 21. | medium |
| 23 | Deleted second line | ayant un nb fini de gén., pour H fini | Cancellation crosses almost every letter; « ayant », « nb », and « gén. » are especially uncertain. | low |
| 23 | Cofinality sentence | ens | Final abbreviation mark absent or indistinct. | medium |
| 23 | Paragraph after (45) | progroupes | Prefix retraced; no certain hyphen visible. | medium |
| 23 | Cancelled line below « En particulier » | Remarque G underline | Le pro-groupe G underline; heavily overstruck and underlined. | low |
| 23 | Cancelled word before final map | image | Almost all letter bodies struck through, but i-dot and probable g-descender remain. | low |
| 23 | First symbol of final map | E | Overwritten initial; reading agrees with the clearly written target E but is not certain independently. | medium |
| 23 | Under target of final map | vertical equality | Could be a vertical isomorphism sign. | low |

### Abbreviations met

- `nb` (in deleted text): nombre.
- `gén.` (in deleted text, uncertain): générateurs.
- `ens`: ensemble.
- `sch.`: schémas.
- `syst.`: système.
- `etc`: et cetera.
- `hom`: homomorphisme.
- `ext.`: extension.
- `Spec`: spectre.

### Legibility

The main argument and final diagram are legible at enlarged scale. The two lines struck out near the top and the second cancelled line around the middle are the least secure passages. The handwritten marginal instruction « prendre les nM ! » is clear and has not been incorporated into the body as an editorial correction.

### Research notes (English)

1. **Scan 23, opening paragraph and left margin; unproved claim.** The H-stable finite-index subgroups are asserted to be cofinal among all finite-index subgroups of M, after a more restrictive hypothesis on H is deleted. The note « prendre les nM ! » supplies a proof direction: for N of finite index, choose n annihilating M/N, so nM ⊆ N; the subgroups nM are invariant under every automorphism of M.
2. **Scan 23, below (45); unproved claim.** The extension sequences « forment un syst. projectif d'extensions ». A full construction should specify its ordering and transition maps, then verify the compatibility of the quotient extensions and associated scheme morphisms.
3. **Scan 23, lower half; unproved claim.** The transition maps « sont affines », with the verification reduced locally on Gᵢ to a morphism E(Mᵢ,Mⱼ) → E(Mᵢ,Mᵢ). To complete this reduction, one needs to identify the relevant local models and show that the stated map between them is affine.
4. **Scan 23, final paragraph; own idea.** Track whether the affine-transition assertion is independent of the chosen cofinal family nM. **Confidence: medium:** cofinal replacement should preserve the represented inverse-limit functor, but a proof about the actual transition maps is stronger than a statement about that limit alone.

Independent visual audit: the complete scan and enlarged difficult passages were compared with the transcription. No additional securely readable omitted text was found; the existing uncertain readings remain uncertain.

---

## Scan 24

### Doubts and alternative readings

| Scan | Approximate line or position | Reading | Alternatives / qualification | Confidence |
|---|---|---|---|---|
| 24 | Middle, after « à la limite » | carrément | The initial c and final -ment are clear; the central shallow cursive strokes are compressed. | medium |
| 24 | Remark, after « S₀ = Spec » | \(\mathcal G\) | \(\mathbb Z\); the visible character resembles the distinctive group-G glyph. The transcription puts this visible reading first; the earlier base notation is not used to correct it. | medium |
| 24 | Remark, interlinear cancellation after « sous-groupes » | invariants abéliens | The first word is not entirely recoverable beneath the strike; abéliens is clearer. The phrase lies above modulo commensurabilité and is represented as an insertion that is also deleted; the revision order is not independently established. | medium |
| 24 | Last line, replacement above cancelled « les » | un des | ∀ des; the first sign is angular and may be u/n or a quantifier, while des is clearer. | low |

### Abbreviations preserved

| As written | Tentative expansion |
|---|---|
| t.f. | type fini; locally « de type fini » |
| i.e. | id est; c’est-à-dire |

### Legibility and coverage

The upper prose and the end of the remark are mostly legible, with extremely shallow joins typical of this hand. The page has no numbered display and no diagram. The underlined « Remarque », the canceled G after « du », the canceled interlinear subgroup adjectives, the canceled « libres », its later underlined occurrence, the replacement above « les », and the pencilled lower-left 23 are represented. The continuation after the final comma belongs to the next scan. No top manuscript folio is visible. Printed institutional footer material outside the manuscript frame is excluded consistently with the edition plan.

The symbol following Spec is recorded without correction: the source visibly uses the same rounded group-G shape seen elsewhere. The final replacement remains particularly doubtful. No unreadable-word placeholder was necessary on this page.

### Research notes — English

1. **Scan 24, first two paragraphs — unproved claim.** The justification “comme somme finie de schémas affines” finishes the preceding affineness argument, followed by the assertion that “le foncteur limite projective ... est représentable”. A proof would need to state the precise existence theorem for the inverse limit and verify its hypotheses for this transition system.
2. **Scan 24, middle paragraph before Remarque — conjecture (tentative working expectation).** “Il n'est peut être pas absurde de passer à la limite” presents working with the actual limit group scheme as a possible replacement for the pro-object, rather than as a formal conjecture. The qualification “pas de t.f.” explicitly withholds finite type; further work should compare what the two objects retain in the intended applications.
3. **Scan 24, Remarque — unproved claim.** The assertion “ne dépend que du ... groupe discret ... muni d'une classe de sous-groupes ... modulo commensurabilité” makes independence from a chosen subgroup representative a structural claim. The cancellations of “invariants abéliens” and the first “libres” accompany a reformulation involving finitely generated integer modules and smaller free subgroups; a proof should specify the invariant indexing data and compare the resulting pro-objects. The finite-index sentence continues onto scan 25.

### Independent visual audit

The complete scan and enlarged difficult passages were compared with the transcription. No additional securely readable omitted text was found; the existing uncertain readings remain uncertain.

---

## Scan 25

### Doubts

| Scan | Approximate line or position | Reading | Alternatives / qualification | Confidence |
|---|---|---|---|---|
| 25 | Top manuscript folio | 660 | 680; the second numeral is overwritten and cannot safely be recovered by sequencing the folios | medium |
| 25 | Upper paragraph, line 2 | soumis | The highly compressed first half of the word remains uncertain | medium |
| 25 | Left of the deleted heading | 3 | A small handwritten sign which could instead be a paragraph/insertion mark | low |
| 25 | Above “métabélien” | inserted \(\mathcal G\) | Its interlinear position is clear; attachment is taken after “groupe discret” | medium |
| 25 | Interlinear expansion of “proschéma en groupes” | syst. proj. de schémas en groupes affines, | The long curved connector is treated as an insertion connector, not as an extra literal parenthesis | medium |
| 25 | After (46), line 3 | fonctoriellement | The ending is compressed into a stroke | medium |
| 25 | After (46), line break after d'exacti- | d'exactitudes | d'exactitude; the next-line ending appears to include an s, but the reduced terminal stroke remains uncertain | medium |
| 25 | After (46), line 5 | intéressantes | Several internal letters and the ending are abbreviated by the pen | medium |
| 25 | (47), arrow | \(\xrightarrow{\sim}\) | A second short parallel stroke may indicate a double-shaft arrow | medium |
| 25 | (48), three right-hand connections | Headless shafts | The source has no reliably distinguishable arrowheads; no heads have been supplied | medium |
| 25 | (49), first Env | Underlined Env | A heavy low stroke has been treated as an underline rather than a cancellation | medium |
| 25 | (49), final term | 1 | The term abuts the scan's black border and is partly clipped | medium |

### Abbreviations met

| As written | Tentative expansion |
|---|---|
| \(\overline{\mathrm m}\) | même |
| t.f. | type fini |
| syst. proj. | système projectif |
| ens | ensemble |
| comm. | commutatifs |
| p. ex. | par exemple |
| Env | enveloppe |
| \(\forall\) in the prose phrase “pour \(\forall\) groupe” | tout |

### Legibility

The main paragraph and the mathematical objects are mostly legible. The overwritten folio, the small sign beside the deleted heading, the insertion connector, and the right edge of (49) are the least reliable features. Arrow shafts without visible heads have been preserved as headless connections rather than completed from the expected exact-sequence notation.

### Research notes — separate from the transcription

1. **Scan 25, opening paragraph — unproved claim.** “Ce proobjet ne dépend que de \(\mathcal G\)” asserts independence from the auxiliary choices used to construct it. A proof would need to compare the indexing systems attached to different finite-index commutative subgroups and show that their transition systems yield equivalent pro-objects.
2. **Scan 25, paragraph around (46) — unproved claim.** “Ce pro-groupe dépend fonctoriellement de \(\mathcal G\)” asserts functoriality without spelling out its action on a general group homomorphism on this page. A verification should specify how inverse images and finite-index subgroups enter the induced morphism of projective systems.
3. **Scan 25, (47) — unproved claim.** The phrase “il est multiplicatif” is followed by the asserted comparison for a direct product. A proof would need to establish that the product indexing system is cofinal in the system used for the product group, and identify the finite-level group schemes.
4. **Scan 25, (48)–(49) — unproved claim.** “Une suite exacte pour les enveloppes” is asserted, with the sense of exactness deferred to the continuation on scan 26. The proof must distinguish the finite-level statement from the statement after projective limit, especially the meaning of surjectivity.
5. **Scan 25, definition of “métabélien” — own idea; confidence: high as a reading issue.** The displayed condition is the existence of a finite-index commutative subgroup finitely generated over \(\mathbb Z\). A later comparison with other usages of “metabelian” should start from this condition rather than substitute a meaning based solely on the name; this is prompted by the explicit condition in the manuscript, not a claim of mathematical novelty.

---

## Scan 26

### Doubts

| Scan | Approximate line or position | Reading | Alternatives / qualification | Confidence |
|---|---|---|---|---|
| 26 | End of first line | à | The two small strokes resemble a colon; the following word is read as “l'occasion” | medium |
| 26 | Opening paragraph, fourth line | on a bel et bien un hom fid plat | “on a” and “bel” are heavily abbreviated by the pen; the full phrase was checked at enlarged scale | medium |
| 26 | Second paragraph, line 2 | assez | Internal letters are compressed | medium |
| 26 | (50), connections | Headless shafts | No arrowheads are clearly written, including the labelled multiplication-by-\(n\) connection | high |
| 26 | First line after (50), deletion | construire | The crossing stroke obscures the middle and ending | low |
| 26 | Lower paragraph, line with \(\mathbb Z[T]\) | isomorphisme | The final letters meet the right border | medium |
| 26 | Lower paragraph, following line | choisissant | The middle letters are compressed, though the word shape supports this reading | medium |
| 26 | Lower paragraph, penultimate line | l'ens | l'un; the following line begins “des entiers” | medium |

### Abbreviations met

| As written | Tentative expansion |
|---|---|
| hom | homomorphisme(s) |
| fid | fidèlement |
| ens | ensemble |
| \(\forall\) before “entier” | tout |

### Legibility

The formula and the lower paragraph are substantially legible. The opening punctuation or reduced “à”, the struck-through verb, and the final letters at the right edge require caution. This scan has no visible top manuscript folio; the handwritten lower-left “25” has been retained separately from the archive footer.

### Research notes — separate from the transcription

1. **Scan 26, opening paragraph — unproved claim.** “Un hom fid plat dont le noyau est le bon” specifies the intended exactness for the associated inverse-limit group schemes. Establishing this needs both faithful flatness of the resulting homomorphism and identification of its kernel, rather than only a formal appeal to exactness of each finite-stage sequence.
2. **Scan 26, second paragraph — unproved claim.** The general case is said to reduce “de façon assez immédiate” to \(\mathcal G=M=\mathbb Z\). A full proof should identify the reductions through a finite-index free abelian subgroup, products, and the residual finite quotient action.
3. **Scan 26, lower paragraph — unproved claim.** The coordinate ring of \(\underline{\mathcal G}_n\) is asserted to be a product of \(n\) copies of \(\mathbb Z[T]\), “de façon pas bien canonique”. The proposed set-theoretic section explains the source of noncanonicity, but the induced multiplication and its independence from that section have not yet been written out here.
4. **Scan 26, chosen representatives — own idea; confidence: high as a concrete calculation to try.** With the representatives \(0,\ldots,n-1\), one can try writing the extension law using the carry \(\lfloor(r+s)/n\rfloor\). Deriving the corresponding cocycle directly from the displayed inclusion \(n:\mathbb Z\to\mathbb Z\) would test signs and normalizations before comparing the transition maps on scan 27; this is a proposed verification, not a claim of novelty.

---

## Scan 27

### Doubts

| Scan | Approximate line or position | Reading | Alternatives / qualification | Confidence |
|---|---|---|---|---|
| 27 | Top manuscript folio | 661 | 681; the central digit is overwritten | medium |
| 27 | Line before “de \(2^\circ\))” | vus | The last letter is only a short stroke | medium |
| 27 | Same line, cancellation | des + \(\S b\) | The cancelled second unit resembles a section/reference sign followed by a b-like stroke; this is a tentative visible-stroke reading, and the cancellation prevents a secure identification | low |
| 27 | After “chose étrange” | la | The article is retraced and close to the insertion connector | medium |
| 27 | Above \(\mathbb Z\)-algèbre | sous- | “sous” is reasonably clear; the ending stroke may be a connector rather than a literal hyphen | medium |
| 27 | Next line, after \(\mathbb Q[T]\) | formé | formée; final gender ending is not distinguishable | medium |
| 27 | Opening of last paragraph | description | Several central strokes have been retraced | medium |

### Abbreviations met

| As written | Tentative expansion |
|---|---|
| hom | homomorphismes |
| dfn above the equality | définition |
| \(\overline{\mathrm m}\) after “lui” | même |
| \(2^\circ\)) | second numbered item or subdivision |

### Legibility

The equations are clear, and the two principal prose blocks are substantially readable. The cancelled material before the reference to \(2^\circ\)), the overwritten manuscript folio, and the interlinear addition before “\(\mathbb Z\)-algèbre” are the weakest readings. The large descending stroke near the end belongs to the word “polynômes”; it has not been converted into an independent check mark.

### Research notes — separate from the transcription

1. **Scan 27, opening lines — unproved claim.** The transition homomorphisms “n'ont rien de plat bien sûr”. A useful verification would identify their restrictions to the additive parts and examine special fibres at primes dividing the transition multiplier.
2. **Scan 27, first display and following paragraph — unproved claim.** The inverse limit is asserted to be an extension of the displayed profinite constant group scheme by a limit of additive group schemes. A proof should justify passage to the inverse limit and identify the kernel through the transition maps, without presuming flatness of those transitions.
3. **Scan 27, polynomial display — unproved claim.** “Chose étrange” introduces the claim that the direct-limit ring is the subring of \(\mathbb Q[T]\) whose constant coefficient is integral. Verifying this reduces to comparing \(\bigcup_n\mathbb Z[T/n]\) with that subring and checking that a common choice of \(n\) absorbs all nonconstant denominators.
4. **Scan 27, final paragraph — unproved claim.** “On a une description analogue” asserts the multivariable version for \(\mathbb Z^n\). A proof would need a precise relation between products of the rank-one systems and the indicated subring of \(\mathbb Q[T_1,\ldots,T_n]\), together with the asserted neutral-component description.
5. **Scan 27, “attention à l'abus de notation” — unpursued implication.** The explicit warning invites a distinction between the projective limit of finite constant group schemes and whatever is denoted by the constant object associated to the profinite group \(\widehat{\mathbb Z}^{\,n}\). The comparison should record which topology or category gives meaning to each notation.
6. **Scan 27, integral-constant-term ring — own idea; confidence: high as a proposed check.** Compute the fibres of \(\operatorname{Spec}(\mathbb Z+T\mathbb Q[T])\) directly from the ring: the nonconstant ideal is divisible by every prime, while rationalization restores the full polynomial ring. This suggests checking the contrast between the generic additive fibre and the special fibres explicitly; scan 28 continues this issue.

### Independent visual audit

A separate rereading found no clear missing block or formula. A final enlargement of the cancelled unit before “de \(2^\circ\))” supports the tentative reading `\unsure{\S b}` in place of an illegibility mark; no contextual reference has been supplied to complete it.

---

## Scan 28

### Doubts

| Scan | Approximate line or position | Reading | Alternatives / qualification | Confidence |
|---|---|---|---|---|
| 28 | Top paragraph, third line | générique | The word is retraced; no independent cancellation has been distinguished from its letter strokes | medium |
| 28 | Before “Dans le cas” | deleted Et | A short cancelled word; its strokes could also be read as another opening conjunction | low |
| 28 | Second paragraph, second line | désignant | désignons; the final stroke does not settle the ending | medium |
| 28 | Second paragraph, final base symbol | \(S_0\) | The capital is heavily overwritten | medium |
| 28 | Line before (51) | en | The initial letter is retraced | medium |
| 28 | Cancelled mark above the thick arrow in (51) | dfn | The mark resembles an overwritten definition label; other small letter labels cannot be excluded | low |
| 28 | Deleted words after “de \(\mathcal G\)” | tels q | tel q; the ending of the first word is crossed through | low |
| 28 | (53), signs over \(V\) and \(M\) | carons: \(\check V,\check M\) | Both marks are visibly small downward vees, not dots | high |
| 28 | (53), surrounding stroke | Upper enclosure open below | It is reproduced in TikZ with the visible top and short ends; a bottom stroke has not been supplied | high |
| 28 | Last line, abbreviation | cov. | The last letter supports v; can. is a less likely reading | medium |
| 28 | Upper paragraph, before profini | complétifié | The long f-like stroke and additional dotted letter favor this form over complété; the central letters are compressed | high |

### Abbreviations met

| As written | Tentative expansion |
|---|---|
| dfn | définition |
| comp. | composante |
| i.e. | id est |
| t.f. | type fini |
| q in deleted “tels q” | que |
| cov. | covariant |
| Spec | spectre |
| Sym | algèbre symétrique |
| Env | enveloppe |

### Legibility

The displayed formulae are generally clear. The most vulnerable details are the two small cancellations, the overwritten base symbol, and the ending of “désignant/désignons”. Formula (53) is reproduced with its visible upper enclosure rather than converted into a closed box. The repeated formula number (50), already used on scan 26, has been preserved.

### Research notes — separate from the transcription

1. **Scan 28, opening paragraph — unproved claim.** “Toutes les fibres sont réduites au groupe unité, sauf la fibre générique” describes the extreme fibre behaviour of the neutral group scheme just constructed. A verification should be carried out on the integral-constant-term coordinate ring and should check the scheme structure, not only its field-valued points.
2. **Scan 28, (50)–(51) — unproved claim.** The text announces “une suite exacte canonique” with quotient the profinite completion and kernel \(\operatorname{Env}^{0}(\mathcal G)\). One must justify that the indicated morphism is the relevant quotient, that its kernel is the neutral component, and that these identifications are independent of the chosen indexing system.
3. **Scan 28, (52) — unproved claim.** The two expressions for \(\operatorname{Env}^{0}(\mathcal G)\) identify the system of finite-index free abelian subgroups with the system \(nM_0\). The required comparison is a cofinality argument, together with compatibility of the associated vector-group morphisms.
4. **Scan 28, (53) — unpursued implication.** The explicit covariant construction \(\check V(M)=\operatorname{Spec}\operatorname{Sym}_{\mathbb Z}(\check M)\) makes the variance of lattice maps relevant to the transition system. Writing these maps on coordinate rings would help separate the covariant group-scheme maps from the contravariant algebra maps and check every inverse/direct-limit direction.
5. **Scan 28, special fibres and (51) — own idea; confidence: medium.** One can test whether the special fibres of the full inverse-limit envelope are exhausted by the profinite quotient once the neutral fibre becomes trivial. The opening fibre calculation suggests this comparison, but it should be verified using the exact sequence and the behaviour of its formation under base change rather than assumed from pointwise intuition.

---

## Scan 29

### Doubts

| Scan | Approximate line or position | Reading | Alternatives / qualification | Confidence |
|---|---|---|---|---|
| 29 | Top manuscript folio | 662 | 682; the middle numeral is overwritten | medium |
| 29 | (54), inside the last parenthesis of the first line | Extra superscript 0 after \(\operatorname{Env}^{0}(\mathbb Z)\) | A small round mark is visible in addition to the superscript on Env; it has been retained rather than algebraically simplified | medium |
| 29 | (54)–(56), exotic rank-one scheme | \(\mathcal E^1\) | The flowing E is distinguished from the visibly double-stroked \(\mathbb E^1\) in the limit system | medium |
| 29 | Marginal reference mark and marker in (55) | dagger | The mark is slanted and could instead be a matching insertion/reference sign | medium |
| 29 | Marginal transition diagram, first index | mn | nm; the first letter is overwritten | low |
| 29 | Marginal diagram, second index | Double-underlined n | Two short strokes below the index are visible | high |
| 29 | (55), second line | Inserted limit expression | The smaller interlinear writing and its reference marker support treating it as an insertion | medium |
| 29 | (56), after equality | Deleted projective-limit symbol | Its letters and the lower leftward arrow are overwritten | low |
| 29 | (56), final quantifier | \(\mathbb N^*\) | The last strokes are clipped at the right border | medium |
| 29 | Lower paragraph, relation after \(nA\) | \(\geq\) | \(\simeq\), or a heavily retraced equality; the mark cannot be resolved securely from the ink and has not been corrected using the next sentence | low |
| 29 | Same line, cancelled word | précis. | Only parts of the word survive the strike-through | low |
| 29 | Following line, cancellation before “il existe” | c'est | ceci is also possible; the letters are crossed by a heavy line | low |
| 29 | Consequence in lower paragraph | \(\mathcal E^1(A)=\{1\}\) | The digit is retained as 1, not changed to an additive zero | high |
| 29 | Final condition | A de car 0 | No missing “corps” or other condition has been supplied | high |

### Abbreviations met

| As written | Tentative expansion |
|---|---|
| syst. | système |
| iso | isomorphisme |
| car. / car | caractéristique(s) |
| précis. in the cancellation | possibly précisément |
| Env | enveloppe |
| Spec | spectre |

### Legibility

The main formulae can be followed, including the compatibility equation in (56). The upper folio, the extra round superscript in (54), two short cancellations, the first index in the sloping marginal diagram, and especially the relation after \(nA\) remain uncertain. The margin was inspected after rotation and the condition after \(nA\) was independently checked by a second reader; neither reader could securely resolve the latter mark.

### Research notes — separate from the transcription

1. **Scan 29, upper paragraph and (54) — unproved claim.** The system of multiples \(nM_0\) is described as “cofinal dans celui de tous les \(M_i\)”, and a basis gives the displayed rank-one product decomposition. A proof should verify this cofinality in the actual indexing category and specify which parts of the resulting isomorphism depend on the chosen basis.
2. **Scan 29, (55)–(56) — unproved claim.** The scheme is said to “qui représente le foncteur en groupes” given by compatible sequences. This can be checked by expressing an algebra homomorphism out of the direct-limit coordinate ring as compatible choices of images of the variables \(T_n\), including the relation \(x_n=mx_{mn}\).
3. **Scan 29, (56) — own idea; confidence: high.** Test the identification of the compatible-sequence functor with \(\operatorname{Hom}_{\mathbb Z}(\mathbb Q,A_{\mathrm{add}})\), using \(x_n=f(1/n)\). The written relation is exactly the compatibility that this construction would require, making it a useful independent check on the limit directions and scalar factors.
4. **Scan 29, lower bracketed paragraph — unproved claim.** “Il existe sans doute un tel \(n\)” is asserted when all residual characteristics are positive. The exact preceding relation after \(nA\) remains palaeographically unresolved, so it must be established before attributing a precise algebraic condition; a possible proof strategy is to examine \(A\otimes_{\mathbb Z}\mathbb Q\) and the existence of an integer annihilator.
5. **Scan 29, final line — own idea; confidence: high as a hypothesis check.** The phrase “\(A\) de car \(0\)” needs interpretation before accepting \(\mathcal E^1(A)\simeq A\): a \(\mathbb Q\)-algebra and an arbitrary ring of characteristic zero give different tests. In particular, compare a field of characteristic zero with \(A=\mathbb Z\) directly in (56), where the compatibility forces every integer coordinate to be divisible by arbitrarily large integers; this proposed check must not alter the transcription.

---

## Scan 30

### Doubts

| Scan | Approximate line / place | Reading | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 30 | 5 | `loc.` | `loc`; the abbreviation is clear but its terminal point is not distinct. | medium |
| 30 | 6 | `hom.` | `hom`; the ending and punctuation are reduced to short strokes. | medium |
| 30 | 9, deleted | `quasi-` | The opening descender and surviving dots support *quasi*, but the deletion obscures the ending. | medium |
| 30 | 10 | `élt` | `élem.`; the abbreviation following the universal-quantifier sign is compressed. | medium |
| 30 | 14 | `hom.` | `hom`; point uncertain. | medium |
| 30 | 17 | `hom.` | `hom`; point uncertain. | medium |
| 30 | 18, deleted | `associé` | The inserted words and strike-through intersect the original word. | low |

### Abbreviations met

- `loc.`: locally / *localement*.
- `prés.`: *présentation*.
- `hom.`: *homomorphisme*.
- `resp.`: *respectivement*.
- `élt`: *élément* (tentative reading of this abbreviation).
- `∀`: mathematical quantifier used within the French sentence, not expanded in the transcription.

### Legibility

The heading, principal definitions, and three morphism displays are relatively clear. The least reliable parts are the word deleted before *unipotent*, the compact abbreviation following `∀`, and the word replaced by *qui lui correspond*. The lower-left number `29` is reproduced as a marginal mark; its archival or authorial provenance cannot be established from this scan alone.

### Research notes — English

1. **Scan 30, approximately lines 9–13 — unproved claim.** The definition is followed by “ce qui se vérifie fibre par fibre.” A proof would need to specify the intended points and fibres and justify equivalence between the pointwise unipotence condition and its fibrewise formulation, including the quasi-unipotent variant.
2. **Scan 30, approximately lines 15–20 — unpursued implication.** The condition on a discrete-group homomorphism is transferred to the corresponding morphism `G_S → G` through “qui lui correspond.” This invites a precise comparison of the group-theoretic condition on sections with the scheme-theoretic condition after base change; the page gives the definition but does not pursue its behavior under a change of base.
3. **Scan 30, approximately lines 9–20 — own idea; confidence: medium.** Test the fibrewise formulation first for a nonreduced affine base and a matrix group, so that the image of a section and its reductions can be compared directly. The reason for choosing this test is that the statement refers to fibres while the homomorphism is defined over the whole base; this is a suggested verification, not a claim of failure or novelty.

---

## Scan 31

### Doubts

| Scan | Approximate line / place | Reading | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 31 | Top original folio | `663` | `683`; middle digit is retraced or overwritten. | medium |
| 31 | 7, notation after *noté* | `Env_{underlined S}` | `Env_S`; a short line is visible under the subscript, but may be a letter flourish. | low |
| 31 | 10 | `loc.` | `loc`; terminal point uncertain. | medium |
| 31 | (58), lower left | `Hom` | First letter is heavily retraced; the word is interpreted as the same operator appearing above. | medium |
| 31 | 15, deleted | `un` | A small crossed-out word immediately precedes *hom.*; only parts of the strokes survive. | low |
| 31 | 15 | `hom.` | `hom`; point uncertain. | medium |
| 31 | (59), deleted before L | `varprojlim` | The crossed-out object contains a leftward arrow and tall letter strokes, but is densely overwritten. | low |
| 31 | 17 | `changement` | Possibly an abbreviated form; internal letters are very compressed. | medium |
| 31 | 17 | `hom.` | `hom`; point uncertain. | medium |
| 31 | Final line | `hom.` | `hom`; point uncertain. | medium |

The leftward arrow under `lim` in the lower-left part of (58) is retained. The right-hand object in (58) is transcribed without an `L` before `Env`, since no distinct `L` is visible; neither feature is silently changed to agree with a preferred mathematical convention.

### Abbreviations met

- `syst.`: *systèmes*.
- `loc.`: *localement*.
- `prés.`: *présentation*.
- `progr/S`: category of pro-groups over `S` (expansion inferred only for this list).
- `def`: *définition*, written beside the vertical equality in (58).
- `hom.`: *homomorphisme*.
- `can.`: *canoniques*.
- `Env`: *enveloppe*.
- `L`: notation for the represented limit, not expanded in the transcription.

### Legibility

The principal prose and (57) are fairly legible. The initial folio digit, the retraced `Hom` in (58), and especially the deleted object in (59) are less secure. The original direction of the limit symbol in (58) and the apparent absence of `L` in its right-hand term are preserved as visual readings rather than regularized. The lower-left `30` is retained as a marginal mark.

### Research notes — English

1. **Scan 31, approximately lines 1–11 and (57)–(58) — unproved claim.** The phrase “d'après les propriétés des ... syst. projectifs filtrants” invokes a factorization statement for morphisms from an inverse limit of schemes with affine transition morphisms to a locally finitely presented group scheme. A proof would need to identify the exact hypotheses on the base and the source stages, and then show that the group-homomorphism identities descend at a finite stage as well as the underlying scheme morphism.
2. **Scan 31, (57) — unpursued implication.** The equality `LEnv_S(G) = LEnv(G) ×_{S_0} S` makes base change central to the construction. It would be useful to separate the existence of the represented limit from the assertion that its formation commutes with this base change, since the manuscript compresses both into one display.
3. **Scan 31, (58) — own idea; confidence: medium.** Audit the index-category convention before comparing (58) with the usual definition of morphisms from a pro-object into a constant target. The visible limit arrow points leftward, and the right-hand term appears without `L`; comparison with the subsequent displays may determine whether these are convention-dependent shorthand or local slips, but the diplomatic transcription preserves the ink.
4. **Scan 31, (59)–(59 bis) — unpursued implication.** The canonical homomorphism is said to be “déduit par changement de base.” Its injectivity, kernel on points, and scheme-theoretic behavior are not addressed on this page, and are natural questions to distinguish before using it as a universal map.

---

## Scan 32

### Doubts

| Scan | Approximate line / place | Reading | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 32 | Below left part of (60) | `1` | An isolated short upright ink stroke; it may be an incidental pen mark rather than a numeral. | low |
| 32 | Before (61) | `Composant` | *Comparant* is a possible lexical alternative, although the visible middle strokes favor *Composant*. | medium |
| 32 | (61), after leftmost `Hom` | `ℓ` | A small looped glyph or correction immediately follows the operator; its identity is not clear. | low |
| 32 | Theorem heading, deleted | `Si` | A densely overwritten short word; the tall opening and dot suggest *Si*. | low |
| 32 | Theorem hypothesis | `schéma` | A terminal point or abbreviation stroke may follow the second occurrence. | medium |
| 32 | Deleted qualification | `me` | `se`; the short word between *pas* and *fatiguer* lies on the cancellation line. | low |
| 32 | Theorem conclusion | `l'ens.` | `l'ens`; compressed ending and point. | medium |
| 32 | Theorem conclusion | `hom.` | `hom`; point not distinct. | medium |
| 32 | Final line | `noeth.` | The middle letters are contracted into low strokes. | medium |

The two underlined group symbols in the first morphism are preserved even though the first source was not underlined in (59 bis) on the preceding scan. The left marginal rule alongside the theorem is reproduced as a TikZ stroke.

### Abbreviations met

- `gr`: *groupes*.
- `pro-S-gr`: pro-group schemes over `S` (inferred expansion for this list only).
- `loc.`: *localement*.
- `prés.`: *présentation*.
- `l'ens.`: *l'ensemble*.
- `hom.`: *homomorphismes*.
- `noeth.`: *noethérien*.

### Legibility

The Hom displays and the final surviving theorem assertion are mostly legible. The leftmost Hom expression in (61) contains a small unexplained glyph. The theorem has two distinct cancellations and a replacement above the line; the crossed-out short word in “pour ne pas ... fatiguer” is particularly insecure. The isolated stroke under (60) has been retained with doubt rather than silently discarded.

### Research notes — English

1. **Scan 32, theorem — unproved claim.** The surviving assertion says that the canonical application is “injective, et a comme image” the quasi-unipotent homomorphisms. A proof would have to establish uniqueness of the extension to the envelope and existence exactly for that stated class of discrete-group homomorphisms.
2. **Scan 32, final lines — unproved claim.** The qualification “du moins si on suppose ... que S est noeth. et G affine sur S” limits the stated theorem. This leaves open on this page whether noetherianness, affineness, or both are essential to existence, to uniqueness, or merely to the intended proof.
3. **Scan 32, theorem revision — unpursued implication.** The earlier assertion “bijective” is cancelled and replaced by injectivity together with a description of the image. The revision makes the quasi-unipotence restriction substantive; it should not be read as a theorem asserting universality for all discrete-group homomorphisms.
4. **Scan 32, theorem — own idea; confidence: medium.** Check the statement separately for a cyclic source with target the additive and multiplicative group over an affine base. These elementary target choices could isolate which part of the envelope controls unipotent images and which part permits finite-order behavior, without presuming that the broader theorem or its strongest hypotheses have already been proved.

---

## Scan 33

### Doubts

| Scan | Approximate line / place | Reading | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 33 | Top folio | `664` | `684`; middle digit is blackened or overwritten. | medium |
| 33 | Section number | `50` | The second digit is heavily retraced. | high |
| 33 | Upper-right `G_0` superscript | Deleted hat | The dark superscript resembles a cancelled hat, but its precise original form and cancellation state are not fully secure. | low |
| 33 | (1), each of three Z's | Deleted hat | The three dark marks are transcribed as cancelled hats; their status is less clear than the underlying Z's. | medium |
| 33 | (1), under the sum | Deleted underbrace labelled `M` | The brace and `M` are obscured by repeated diagonal cancellation strokes. | medium |
| 33 | (3), before `[λ_0,λ_1]` | Deleted `ρ` | The short overwritten symbol has a loop and descending stroke; another original symbol is possible. | low |
| 33 | Definition of `λ_0`, last exponent | Deleted `−1` | Deleted `4`; the exponent has been blackened. | low |
| 33 | Paragraph before (4) | `dont` | `donc`; the terminal letter is a reduced stroke. | medium |
| 33 | Final paragraph | `revanche` | The word is compressed; the phrase is read as *en remplaçant en revanche un*. | medium |
| 33 | Final parenthesis | `n` with superscript `b` | `nb` on the line; placement of the small second letter is uncertain. | medium |

The apparently cancelled hats are not used to regularize the unstruck phrase *groupes profinis*. The original group-presentation delimiter is left open, as no closing outer brace is visible to the right of the relations. The manuscript's rectangular bracket naming `H` in (2) is retained as a TikZ bracket within the diagram.

### Abbreviations met

- `dfn`: *définition*.
- `ab`: *abélianisé* / *abélianisation*.
- `gén.`: *générateurs*.
- `rel.`: *relations*.
- `nᵇ` / `nb`: *nombre*.
- `GL`: general linear group, as mathematical notation.

### Legibility

The main French argument is legible, and the matrices in the margin can be read directly. Several superscripts and one symbol in the presentation are overwritten; these are the weakest readings. The cancelled underbrace in (1) and the exponent at the end of the first `λ_0` expression should be checked against the original scan before any mathematical use. The passage is not regularized to make its discrete and profinite terminology agree.

### Research notes — English

1. **Scan 33, paragraph before (1) and marginal matrices — unproved claim.** The manuscript asserts that quotienting by `[Π_0,Π_0]` produces the stated extension and records that `Π_0` is “engendré par les λ_i = −l_i.” A proof would need to identify the subgroup from the displayed matrices, determine its abelianization, and verify the diagonal relation in (1).
2. **Scan 33, (2) — unproved claim.** The quotient labelled `H` is identified with `GL(2,Z/4Z)/(dot l_0,dot l_1)` without a derivation here. The claim calls for an explicit reduction-modulo-4 computation together with the kernel comparison needed to recover the abstract quotient written above it.
3. **Scan 33, (3)–(5) — unproved claim.** The words “Par générateurs et relations on a” introduce a presentation, followed by a reformulation of the commutation relation. A proof would need both directions: the displayed generators and relations must hold in the quotient, and the resulting presented group must not introduce an additional kernel.
4. **Scan 33, final paragraph — unpursued implication.** The discussion of “le jeu des signes −” explains how replacing an odd number of occurrences of `σ` by `σ^{-1}` affects the formula. This invites a systematic bookkeeping rule for the central sign, especially before comparing the alternative expressions on the next page.
5. **Scan 33, (3)–(5) — own idea; confidence: high as a verification strategy, not as a new claim.** Use the explicitly printed relations `ρ^3=σ^2`, `ρ^6=1`, and `σ^4=1` to check each sign and exponent in the proposed reformulations independently. This could distinguish an ink-reading problem from a genuine correction in the manuscript; any resulting simplification belongs in the research apparatus, not in the transcription.

---

## Scan 34

### Doubts

| Scan | Approximate line / place | Reading | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 34 | First (6), cancelled expression following `λ_∞` | `=−ℓ_∞` | Extremely dense crossing strokes obscure the original symbol; an earlier `λ_∞` expression is also possible. | low |
| 34 | Upper-right NB, second commutator, left side | `σ` with cancelled subscript `∞`, comma, `ℓ_∞` | The subscript is blackened, and the separator is not secure. The underbrace label `σ` is retained. | low |
| 34 | First main paragraph, insertion before `pts` | `Ẑ-` | `Z-`; the small upper stroke may belong to the insertion mark. | medium |
| 34 | First main paragraph, parenthetic insertion | `à un isom. près` | The middle word is heavily crossed by surrounding handwriting; `disons` is another possible visual reading. | low |
| 34 | First (8), additive group glyph | `𝔾_a` represented as `\mathbb{G}_a` | The retraced character resembles `\mathbb{E}_a`; no change is made on mathematical grounds. | low |
| 34 | Middle-left marginal note | `noter` | Final letters are compressed. | medium |
| 34 | After “On va faire opérer” | Deleted `G/M` | The cluster is overwritten; the slash and last character are not wholly secure. | low |
| 34 | Number immediately before (4) | Deleted `(4)` | The old number has been overwritten. | low |
| 34 | (4), deletion following `G` | `=GL(2,Z)` | Cancellation strokes obscure the equality and part of the group name. | medium |
| 34 | After “sur M” | Deleted `=underlined G°` | The original symbol is visible beneath multiple diagonal strokes. | low |
| 34 | Before inserted “à travers” | Deleted `en décrivant ainsi` | Beginning and endings lie on the deletion stroke. | medium |
| 34 | (5), subscript of `μ` | `τ` | `2`; the shape is tau-like but may be the writer's digit. | low |
| 34 | (5), superscript of `μ` | Deleted `2` | The small mark has been blackened. | low |
| 34 | (5), label below product | `Γ_{0,3}` | The capital's curved stem could represent another alphabet. | medium |
| 34 | (5), cancelled cluster after `M` | `Ẑ` | The original character and its attachment to `M` are uncertain. | low |
| 34 | Introduction of dotted lambdas | Overbrace over `dot λ_0, dot λ_1` | The wavy overstroke may instead be cancelled or retraced accents. The visible stroke is retained explicitly. | low |
| 34 | “dans … G” | Deleted `M` | The small crossed cluster could be an earlier group glyph. | low |
| 34 | Second (6), separator after `dot λ_0` | Comma | The ink resembles `>`; both readings are recorded. | medium |
| 34 | Second (6), first and second group-scheme symbols | `G°` overwritten by `M` | The old curved glyph and degree sign remain visible beneath the heavier M. | medium |
| 34 | Second (6), tensor subscript | Dot | A very compressed `Z` is possible; the dot-like mark is not suppressed. | low |
| 34 | Second (6), last ring symbol | `Z` | `Ẑ`; no separate hat can be made out at this location. | medium |
| 34 | Encircled lower-left note | `Alors` | `Abus`; the middle letters are reduced. | low |
| 34 | Before “canoniques” | Deleted `bases` | The deletion obscures most of the word; inserted `gén.` is clearer. | low |
| 34 | Before the final list of dotted lambdas | Deleted `λ_0` | The overwritten cluster could be a short word; its first curved stroke and small loop suggest the formula reading. | low |
| 34 | Bottom-left marginal note | `s'en déduit` | The connective is compressed and intersects the adjacent line. | medium |

The round dot accents above the lambdas have been retained as dots, rather than normalized to degree signs. The repeated equation numbers `(4)`–`(8)` are preserved. The symbol with subscript 3 is transcribed in the same calligraphic alphabet as the surrounding group glyph; identifying it with a differently lettered permutation group would require editorial interpretation. The final right-hand identification of the two tau symbols is set as a tikz-cd diagram because the manuscript places the equality signs vertically. The pencilled `33` within the border is retained as a marginal mark, with no claim that it is an original folio number.

### Abbreviations met

- `NB`: *nota bene*.
- `dfn`: *définition*.
- `pts`: *points*.
- `isom.` (uncertain): *isomorphisme*.
- `int`: *intérieur* / the inner automorphism notation in the displayed identity.
- `GL`: general linear group, as mathematical notation.
- `gén.`: *générateurs*.
- `déf.`: *définition*.

### Legibility

This is the most heavily revised page of scans 30–34. The unstruck formulas at the top and the final action formulas are comparatively clear, but the middle paragraph contains several genuinely difficult cancellations, and some group notation has been overwritten rather than cleanly replaced. The parenthetic insertion above `seront`, the first cancelled expression after `λ_∞`, the symbol following `M` in (5), and the encircled annotation are the readings I trust least. Each was inspected in an enlarged crop and has an explicit uncertainty mark; none was silently completed from the anticipated mathematics.

### Research notes — English

1. **Scan 34, first (6)–(7) — unproved claim.** The words “sous la forme” identify the previous relation with `[σ,λ_∞]=1` after introducing the displayed expression for `λ_∞`. A proof would need to check every conjugation convention and the sign in the chain of equalities, using the preceding presentation without discarding its central signs.
2. **Scan 34, upper-right NB — unproved claim.** “On trouve” introduces identities expressing commutators as cubes and relating them by `int(σρ^{-1})`. These algebraic identities are asserted without computation here; checking them independently could also clarify which overwritten subscript belongs to the first factor in the second commutator.
3. **Scan 34, first main paragraph and (8) — unproved claim.** The manuscript proposes to “définir un schéma en groupes” and describes its integral or completed-integral points, then gives a quotient by the diagonal for the neutral part. The construction needs a precise comparison of the points functor with the group written as `Ĝ`; the parenthetical qualification is too uncertain to treat as a settled hypothesis.
4. **Scan 34, middle (4)–(5) — unproved claim.** The phrase “faire opérer … à travers” asserts that the action factors through the quotient and product written in (5). Verifying this would require showing that the indicated normal subgroup acts trivially and identifying the induced action on the quotient of the three additive factors.
5. **Scan 34, second (6)–(8) and bottom margin — unproved claim.** The text says that the three distinguished elements have sum zero and records the actions of `σ`, `ρ`, and `τ`; the margin adds “Ceci se voit d'abord pour i=0,1.” A proof would need to verify the first two generators directly and justify the passage to the infinity generator using the displayed relation, while tracking the change to additive notation.
6. **Scan 34, second (6)–(8) — own idea; confidence: high as a checking procedure, not as a new claim.** Model the three displayed generators by three formal symbols modulo their stated diagonal relation and implement the printed permutations and sign change literally. Comparing these operators with the earlier relations could isolate a transcription issue or a genuine incompatibility in the provisional construction; this calculation must not be used to overwrite the source reading.

---

## Scan 35

### Doubts

| Scan | Approximate line or position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 35 | Top folio | 665 | 685; the middle digit is overwritten | low |
| 35 | Opening, line 2 | développé | développée; no final *e* securely distinguishable | medium |
| 35 | Under (9) | check accent on V | breve accent | medium |
| 35 | Before (10) | ∀ | the abbreviation *tt* | medium |
| 35 | Definition in (10), two occurrences | subscript S | S₀; overwritten small strokes are difficult to separate | low |
| 35 | Definition in (10), canonical homomorphism | underlined calligraphic G | underlined calligraphic E; initial part overwritten | low |
| 35 | (11), cancellation immediately before Γ | A | another cancelled single mathematical symbol | low |
| 35 | (11), beneath underbrace | cancelled A, inserted M | M retraced over an earlier form of itself | low |

### Abbreviations met

| As written | Possible expansion |
|---|---|
| § | paragraphe |
| 3°) | troisième subdivision |
| dfn | définition |
| i.e. | id est |
| hom. | homomorphisme |
| loc. cit. | loco citato |
| iso. | isomorphisme |
| can. | canonique |
| Spec | spectre |

### Legibility

The main paragraph and the last paragraph are substantially legible. The overwritten folio, the subscripts in the definition of the diagonal subset, and the two cancellations in (11) are the least secure readings. In the mathematical formulas, the visibly drawn short strokes beneath O are retained as underlining; the character is not silently replaced with a modern typographical convention. The small handwritten 34 inside the border is retained as a marginal numeral; its authorship is not established here.

### Research notes (English)

- **Scan 35, (11)–(12); kind: unproved claim.** The words “on aura un iso. canonique” assert a contracted-product description of the diagonal part of the group of sections, followed by an exact sequence. A proof would need to specify the action used for the contracted product, identify its relation to the extension constructed in § 50, and distinguish arbitrary bases from the affine case invoked under the brace.
- **Scan 35, last paragraph and (13); kind: unproved claim.** “c'est encore un fait général” introduces the identification of a profinite completion with the diagonal part of the associated scheme's points over the profinite integers. Checking the claim requires recovering the hypotheses on the abelian kernel and the quotient from the surrounding construction; the displayed statement alone should not be promoted to an assertion about arbitrary extensions.
- **Scan 35, (10)–(13); kind: unpursued implication.** The use of a diagonal subgroup makes the distinction between constant quotient elements and all sections of a constant group scheme central to the comparison. A useful further check is how this restriction behaves for a disconnected affine base, particularly the spectrum of the profinite integers.
- **Scan 35, (13); kind: own idea; confidence: medium.** Test the claimed comparison first for a split extension of a finite group by a finite-rank free abelian group, then for a nonsplit extension with a known cocycle. These examples should isolate the respective roles of completion of the lattice, preservation of the quotient, and the cocycle, but the test is a proposal rather than a proof or a novelty claim.

### Independent visual audit

The step-shaped rule accompanying « S affine d'anneau A » below (11), alongside (12), is retained as a native TikZ drawing with that caption. The caption has been moved out of the underbrace's text so that it occurs once; the rule's upper arm, curved descent at the left of the caption, and lower horizontal arm are all represented, without turning it into a closed rectangle. The underlining of O is confirmed directly by enlargement. The uncertainty about the definition's H subscripts and overwritten G/E remains.

---

## Scan 36

### Doubts

| Scan | Approximate line or position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 36 | Opening, first displayed map | subscript 0 | bullet | low |
| 36 | Before (14), cancelled character | calligraphic G | another retraced single group letter | low |
| 36 | (14) and throughout | superscript natural sign | another handwritten distinguishing sign; the sign is unusually horizontal | low |
| 36 | Paragraph after (14) | dispensera | dispense | medium |
| 36 | Same paragraph, after “Pour” | ∀ A | tt A; another short sign or abbreviated word | low |
| 36 | Same phrase | il y aura | The preceding short word is now distinguished from the ∀A-like sign; confidence in that earlier sign remains low. | high |
| 36 | Upper left marginal note | soulignés | soulignements | medium |
| 36 | Upper left marginal note | indiqueront | Earlier alternative indiquent withdrawn after enlarged rotated rereading. | high |
| 36 | (15), cancelled sign before a) | 1° | an earlier a) | low |
| 36 | (15)c), cancelled superscript before G | Π₀ | another group symbol | low |
| 36 | (15)c), cancelled parenthesis at right | equivalence L₀^Π₀ = L₀^natural | the first member may already contain u; several overwritten strokes | low |
| 36 | Right margin at (16) | M semidirect-product cancelled {1,τ}, inserted μ₂ | product sign and overwritten second factor cannot be separated securely | low |

### Abbreviations met

| As written | Possible expansion |
|---|---|
| § | paragraphe |
| VI, with bars | sixth subdivision |
| dfn | définition |
| p.ex. | par exemple |
| etc. | et cetera |
| Aut | automorphismes |
| gr. | groupe |

### Legibility

The long main paragraph is mostly recoverable, but one short phrase beginning “Pour” remains especially uncertain. Rotation makes the two left marginal notes substantially more legible. The superscript distinguishing the subgroup has been marked wherever it occurs because its exact graphical identity is not certain. The cancelled part of (15)c) and the group decomposition at the right edge of (16) are the least trustworthy formulas. The repeated short strokes in (15)b) are manuscript ditto marks; they have not been expanded into a mathematically inferred membership condition. No original top folio is visible; the handwritten lower-left 35 is retained without attributing it to Grothendieck.

### Research notes (English)

- **Scan 36, upper left margin; kind: unproved claim (deferred comparison).** “Je pense à la fin comparer les deux constructions possibles” explicitly defers a comparison. The adjoining text distinguishes working in a schematic setting from working in a profinite one, so the comparison should determine what the respective constructions retain and whether the relevant completion or points operation respects the additional structure.
- **Scan 36, (15)d); kind: unproved claim.** The word “automatique” labels preservation of the distinguished subgroup as automatic. A proof would need to recover its defining characterization, and show that the other automorphism conditions force that preservation; it is unsafe to replace this with a general assertion about all subgroups generated by conjugacy classes.
- **Scan 36, left margin at (15); kind: unpursued implication.** “l'existence locale” explicitly qualifies the existential conditions on α and β. This raises a descent question: the automorphism functor must retain locally available conjugators without requiring a globally chosen one, and the topology intended by “locale” needs to be recovered from the larger manuscript.
- **Scan 36, final paragraph and (16); kind: unproved claim.** “u est déterminé par les valeurs” reduces the automorphism to its values on the two displayed generators. One must also impose the defining relations and any sheaf or continuity requirements before interpreting arbitrary pairs of coefficients as automorphisms; the following page begins the promised conditions.
- **Scan 36, (15); kind: own idea; confidence: medium.** Describe the locally available conjugators as torsors under the corresponding centralizers, then compare their descent data with the functor defined by (15). This is suggested by the explicit local-existence qualification and may clarify representability, but is a proposed approach rather than a result asserted on this page.

### Independent visual audit

The definition in (15) is open on the right: only condition d)'s square bracket is present in the scan. Its typesetting now uses an invisible right delimiter rather than adding a closing set brace. The distinguishing superscript remains flagged: its two opposed slanting stems and loop/bar resemble a natural sign more closely than a single-stem flat, but its horizontal drawing prevents a secure typographic identification; flat remains an alternative worth checking in earlier pages. The word « il » is visibly present before « y aura » and has been restored, without resolving the preceding ∀A-like strokes. The rotated first marginal note supports « indiqueront » clearly.

---

## Scan 37

### Doubts

| Scan | Approximate line or position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 37 | Top folio | 666 | 686, with overwritten middle digit | low |
| 37 | (17)a), group after “via” | underlined G | overwritten M/G | low |
| 37 | (17)a) and (19), distinguished subgroup sign | natural | another handwritten distinguishing superscript | low |
| 37 | (17)c), heading | lacets | Confirmed in enlarged rereading; the repeated heading on the following page agrees visually. | high |
| 37 | Cancelled line before Remarque | N | The two stems and diagonal are visible beneath the strike; earlier M alternative withdrawn. | high |
| 37 | Remarque, centre | μ | μ₂; no separate 2 is discernible in the enlarged crop, so the visible unsubscripted reading is placed first. | medium |
| 37 | Remarque, cancelled words before ωx | l'élém. | l'élé. | low |
| 37 | (19), both far-right case conditions | −1 | final digit partly crowded against the right border | medium |
| 37 | (19 bis), last group | M | M′; short stroke near the right parenthesis | low |

### Abbreviations met

| As written | Possible expansion |
|---|---|
| dfn | définition |
| l'élém. (cancelled, uncertain) | l'élément |
| i.e. | id est |
| bis | second occurrence of the equation number |

### Legibility

The main remark is much clearer than the small side conditions of (19). The second case of each calculation extends to the right edge, so the terminal −1 conditions are flagged. The open brace and the literal ditto strokes in (17) are preserved without supplying repeated words. The overwritten group glyph in (17)a) is not silently changed to agree with the preceding page. The pencil 36 is preserved as a marginal numeral.

### Research notes (English)

- **Scan 37, (17)c); kind: unproved claim.** The “équation des lacets” expresses the relation between the two coefficients by a power of the displayed loop, with μ = 2ν + 1 required to be invertible. A proof must explain the meaning of this exponent for scheme-valued points and how the condition encodes the relevant loop-preservation requirement in (15).
- **Scan 37, after (18); kind: unproved claim.** “ρ et ρ⁻¹ ne sont conjugués sur aucune fibre” is used to justify the well-defined signs, with the corresponding assertion made for σ. This calls for a fiberwise conjugacy analysis in the exact group scheme under discussion, including its special-characteristic fibers.
- **Scan 37, Remarque; kind: unpursued implication.** The distinction between multiplication by the central element ω and additive inversion in M is made explicit: “ωx ≠ −x”. Later formulas that use a minus sign should be checked against this distinction, especially calculations moving between the ambient group and its abelian subgroup.
- **Scan 37, (19)–(19 bis); kind: unpursued implication.** The displayed calculations put ξ in the neutral subgroup and η in a coset determined by the second sign. This may organize the parameter space into components and makes the component constraint a necessary part of any proposed representation of the automorphism functor.
- **Scan 37, conjugacy assertion after (18); kind: own idea; confidence: medium.** Work out the images of ρ, σ, and their inverses separately in fibers of characteristics 2 and 3, while retaining the nontrivial component data. Those characteristics are natural stress tests for the small-order generators, but this is a verification proposal and does not assert that the manuscript's claim fails there.

### Independent visual audit

The page was reread in full, including both case calculations and the small bottom display. « lacets » and the canceled ΓN are now read without uncertainty marks. The centre's letter is retained as uncertain μ/μ₂, with μ first because no subscript numeral can be separated visually. The underbrace scopes and the crowded right-edge −1 cases remain as in the initial transcription; the final M/M′ ambiguity is unresolved. No omitted prose, equation, or marginal annotation was found.

---

## Scan 38

### Doubts

| Scan | Approximate line or position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 38 | (20), after i.e. | equivalence sign | an overwritten short symbol | low |
| 38 | (22), small writing above the target | que | cste; the first visible sign descends like q, and three compact strokes follow. Its function remains unclear. | low |
| 38 | Immediately below (22), cancelled sign | ε | another overwritten short Greek symbol | low |
| 38 | Text after (22) | morphismes | homomorphismes; initial strokes are overdrawn | medium |
| 38 | Following line | liés | Earlier mais alternative withdrawn after enlarged reading of the tall initial, dot, and accent. | high |
| 38 | Cancelled character after “groupes” | μ | another overdrawn short Greek symbol | low |
| 38 | Unnumbered map before (23) | ε₁ | ε₂; the tiny first index resembles 1 | low |
| 38 | (23), two blackened operations | + | dot or retraced operation | medium |
| 38 | (23), cancellation following 1 | +1 | another short abandoned continuation | low |
| 38 | Reference before cancelled block | 24 | 21; the last digit has an angular open shape, unlike the clearer 1 of the preceding reference (21). | medium |
| 38 | (24), annotation beneath brace | λ₁ | Confirmed despite the nearby cancellation stroke. | high |
| 38 | Cancelled word before écrire | pour ainsi | pourra | low |
| 38 | (26), superscript of λ₁ | 2ν′ | overwritten earlier exponent | medium |
| 38 | (26), cancelled aside at right | pour ν₂ = 0 i.e. ε₂ = 1 | ν₂ = 1; several strokes blackened and touching the right edge | low |
| 38 | Last line | unicité | No separate article is visible; the enlarged crop supports unicité. | high |

### Abbreviations met

| As written | Possible expansion |
|---|---|
| i.e. | id est |
| cste (uncertain) | constante |
| hom. | homomorphismes |

### Legibility

The first two equations are reasonably legible. Small annotations, overwritten operations, and the indices of the maps are less secure. The block beginning at (24) is cancelled by large diagonal strokes; its formulas and prose are nevertheless transcribed, with internal cancellations retained as nested deletions. The doubtful aside to the right of (26) is the weakest local reading. The top number is read directly as 676 and is not changed to make a consecutive sequence; the small lower-left 37 is retained separately.

### Research notes (English)

- **Scan 38, (21)–(23); kind: unproved claim.** “morphismes de schémas bien définis” and “hom. de groupes” distinguish the parameter maps from the multiplicative and sign characters. Establishing the claim would require defining the parameter maps functorially on all base schemes and verifying the group law for the latter characters, rather than inferring it solely from their pointwise formulas.
- **Scan 38, (20)–(22); kind: unpursued implication.** The decomposition ν = 2ν′ + ν₂ connects an additive parameter with a two-valued component invariant. Its integral meaning deserves checking in characteristic 2, where ordinary numerical division by 2 cannot define ν′; the manuscript asserts a scheme-level construction rather than merely a characteristic-zero equality.
- **Scan 38, cancelled block, (24)–(26); kind: unproved claim (abandoned calculation).** The cancelled work rewrites powers of the loop using an abelian factor and the central element ω. Because the entire block is struck out, none of these equalities is treated here as an endorsed conclusion; a later manuscript comparison should determine whether the cancellation concerns correctness, presentation, or the choice of coordinates.
- **Scan 38, cancelled final paragraph; kind: unproved claim (deferred computation).** “il faut les développer en combinaisons linéaires” proposes an explicit expression for the aᵢ in terms of the three λ's, with two used if uniqueness is wanted. The computation would need the actual relation among those generators and the precise interpretation of the abelian group law; the cancellation must remain part of the evidential status of this proposal.
- **Scan 38, (21) and cancelled (25); kind: own idea; confidence: medium.** Compare the ν-decomposition and the proposed aᵢ-coordinates over the integers, over a field of characteristic 2, and over a ring with nonzero 2-torsion. This could reveal which parameter choices are intrinsic and which require extra structure; it is a suggested test, not a claimed obstruction or a novel theorem.

### Independent visual audit

The whole final page and the entire canceled block were reread, with the small map annotations and the last line enlarged separately. « liés » and the interlinear « entre eux et » are both visually supported, so the former is no longer flagged. The tiny word above the target in (22) now puts the visible que-like reading before cste, without interpreting its mathematical role. The reference before the cancellation puts 24 first, preserving possible nonconsecutive or self-referential source numbering rather than correcting it from the argument. The label beneath the brace in (24) is λ₁ and the last word is unicité without a visible article. The two blackened operators in (23), the small sign after i.e. in (20), and the canceled aside at the right of (26) remain uncertain.
