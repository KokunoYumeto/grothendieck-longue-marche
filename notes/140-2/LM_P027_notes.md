# LM_P027 — Editorial notes and research notes

## Source and pagination

**Source consulted:** the ten supplied JPEG scans, read visually with enlarged crops and rotated crops of the diagonal notes. No published transcription or outside source has been used to complete a reading.

The transcription is a UTF-8 LaTeX **fragment**, not a standalone document. It begins with `\scanpage{261}`, uses the requested editorial macros, and leaves their definitions to the enclosing document. The `tikz-cd` environments use `ampersand replacement=\&` so that they can occur inside the `\diagram{…}` argument. Syntax was checked with a temporary LaTeX wrapper; that wrapper is not part of the deliverable.

The scan numbers are those supplied in the task, not the printed reproduction numbers. The small lower-left foliation matches the reproduction sequence 260–269; it is not treated as the author’s upper running pagination. The Montpellier reproduction footer and that lower-left foliation are not included as manuscript prose. Only the visible upper running numbers are encoded with `\mspage`.

| Supplied scan | Reproduction/lower-left number | Visible upper manuscript number |
|---|---:|---:|
| 261 | 260 | 131 |
| 262 | 261 | — |
| 263 | 262 | 132 |
| 264 | 263 | 133 |
| 265 | 264 | — |
| 266 | 265 | 134 |
| 267 | 266 | — |
| 268 | 267 | 135 |
| 269 | 268 | — |
| 270 | 269 | 136 |

Line references below are approximate **physical manuscript lines**, excluding the upper page number and, on scan 264, the section heading. “Margin” references are separate from the running prose. A high confidence entry may record a deliberately retained, apparently surprising notation rather than an uncertain reading. Word counts in `\illegible{n}` are estimates, including estimates for cancelled symbols.

## Table of doubts and notation checks

| Scan | Approximate line/location | Reading retained or marked | Alternatives / unresolved point | Confidence |
|---|---|---|---|---|
| 261 | 1–3 | The displayed indices include 3,0; 2,0; 1,0. | These have not been exchanged to fit the later discussion of M_{0,i}. | high |
| 261 | 3 | \widetilde M_{00} | The separator could be a faint comma: M_{0,0}. | medium |
| 261 | 4 | conservent | The beginning is crowded and retraced. | medium |
| 261 | 6 | isotopes | isomorphes is a possible visual competitor; the shorter reading is preferred. | medium |
| 261 | 7 | isom. | The first of the two occurrences is compressed; no longer word has been supplied. | low |
| 261 | 19 | U_{g,\nu} | The initial letter is overwritten; its exact original shape is uncertain. | medium |
| 262 | 2 | pourtant | The middle letters of the adverb are compressed. | medium |
| 262 | 5 | \overline{\mathrm m} | The mark resembles two short horizontal strokes rather than a fully formed m. | medium |
| 262 | 6 | Deleted telle façon; deleted insertion de telle façon. | The first wording and the succession of the two cancellations are not completely secure. | low |
| 262 | 7 | avec; inserted surj. | The first word and the ending of the interlinear abbreviation are weak. | medium |
| 262 | 11 | \deleted{\illegible{1}} before U_{g,\nu} | A cancelled character or short expression, not recoverable as a word. | low |
| 262 | 13 | \mathcal X | A cursive X is visible; the precise alphabet is uncertain. | medium |
| 263 | 2 | le | The article is retraced, not confidently separable into a cancellation and a replacement. | medium |
| 263 | 2, 4, 7 | \mathcal X | Same alphabet uncertainty as on scan 262. | medium |
| 263 | 7 | The second fundamental-group subscript is read as 1. | Its hook can look like another small character. | medium |
| 263 | 9 | essentiellement \| inévitablement | The initial and medial letters do not settle the reading. | low |
| 263 | 9 | \Gamma'_{g,\nu} | No +1 is visible here, unlike the earlier displayed extension; it has not been added. | high |
| 264 | heading | groupe \| groupes | The final stroke does not securely distinguish the number. | medium |
| 264 | 6 | Deleted notons qu’une | The ending of the cancelled expression is weak. | low |
| 264 | 7 | orientées | The final inflection is compressed. | medium |
| 264 | 7–8 | Deleted à [one illegible word]; deleted bornées. | The first cancelled noun is not recoverable; bornées remains provisional. | low |
| 264 | 11 | One illegible word after comme des. | A long word or compact expression; no mathematical reconstruction is substituted. | low |
| 264 | 13 | One cancelled character or word before homéomorphismes. | The crossing conceals the original. | low |
| 264 | 13 | U \rightrightarrows U' \| U \Rightarrow U' | Two horizontal strokes are visible; the exact arrow form is uncertain. | medium |
| 264 | 17 | Deleted pro | Possibly only the start of a longer word, rather than an abbreviation. | low |
| 264 | 19 | (g,\nu) \ne 0,0 \| (g,\nu) \ne (0,0) | An opening inner parenthesis is not clearly visible. | medium |
| 264 | 19 | K(\Pi,1) \| K(\pi,1) | Capital versus lower-case pi is uncertain. | medium |
| 265 | 4 | notés | The final s is not fully distinct. | medium |
| 265 | 10 | ess. comm. \| en. comm. | The first abbreviation is compressed; its expansion is not inserted into the transcription. | medium |
| 265 | diagram, approximately 11–13 | Square with downward vertical maps and an upward-right curved alpha arrow. | The upper horizontal arrowhead and the precise endpoints of the curved alpha stroke are weak; the diagram is described rather than regularized. | medium |
| 265 | 14 | One cancelled item after et. | The ink is insufficient to identify it. | low |
| 265 | 16 | Deleted les [one illegible word]. | The second cancelled word cannot be recovered. | low |
| 266 | 3 | \Delta_1 above the braced arrow category. | The delta is heavily retraced. | medium |
| 266 | 7–14 | \Pi, \Pi_{D^*}, \Pi_U | The repeatedly doubled or boxed strokes make the exact alphabet uncertain; ordinary pi is retained under doubt marks. | medium |
| 266 | 7 | Deleted catégorie; inserted catégorie cofibrée. | The two writing levels overlap, so the exact cancelled wording is not certain. | medium |
| 266 | 8–9 | Deleted formée; deleted des [approximately two words] (. | The second cancellation remains largely unreadable. | low |
| 266 | 14 | Deleted iso | The tiny cancelled item may have had additional letters or punctuation. | low |
| 266 | 15 | \Pi_{B_U} | Possible competitors include a differently nested subscript or \Pi_U; it has not been corrected to fit the arrow formula. | low |
| 266 | 17 | cofibrant | cofibré would be a possible competing ending; the longer visible ending is preferred. | medium |
| 266 | 17 | One cancelled item after et. | Unrecoverable short item beneath the insertion. | low |
| 266 | 17 | tt | Possibly an abbreviated toutes, or a quantifier-like sign; no expansion is made in the fragment. | low |
| 266 | 17 | de before \Pi | The small overwritten word could be read differently; no missing verb is supplied. | medium |
| 267 | 1 | repère | The initial syllable is faint; the whole word is marked. | medium |
| 267 | 6 | Deleted co | A small cancellation immediately before fibrée; it may contain more than these two letters. | low |
| 267 | 9 | ch raised t | Possibly a more compact chgt-type abbreviation. | medium |
| 267 | 9 | exact \| exacts | The final inflection cannot be established from the stroke. | medium |
| 267 | 10 | lim with a rightward arrow below it. | The lower stroke might be read as an underline; its right-hand end favors an arrow. | medium |
| 267 | 16 | On peut | The beginning of the main line is interfered with by the diagonal marginal writing. | low |
| 267 | 17 | par la | The beginning of this main line is also interfered with by the margin. | low |
| 267 | 19 | Inserted (objets admissibles de M). | The last two elements, read as de M, are the least secure part of the insertion. | low |
| 267 | lower-left margin | The i.e. continuation involving \Pi_{D^*}=\varnothing and \Pi_U equivalent to a point category. | The order, punctuation, and empty-set sign are less secure than the preceding phrases topos vide and topos ponctuel. | low |
| 268 | upper-left margin, beginning | Il n’y a …; two cancelled passages, one possibly beginning structure. | Approximately three surviving words and two cancelled groups of about four and two words remain unreadable. | low |
| 268 | upper-left margin, formula | T \| \mathbf Z before the comparison with H^2. | The capital has a horizontal head and a short descending stroke; it is not silently replaced by an integer symbol. | low |
| 268 | upper-left margin, formula | H^2(U_i,Z) | The argument subscript and the form of U are provisional. | medium |
| 268 | upper-left margin | tte composante connexe | The abbreviated first word is uncertain; one following item is not readable. | medium |
| 268 | upper-left margin | Automorph. [one illegible item] orientation ! | The capitalized abbreviation and its relation to the following word cannot be fully recovered. | low |
| 268 | upper-left margin, ending | il n’en est plus de the m-bar sign, bien sûr… | The phrase il n’en est is weak; the m-bar sign has not been expanded in the fragment. | medium |
| 268 | 10 | Closing ] \| ) after the second \Gamma | The visible closing stroke is angular; it has not been silently balanced. | medium |
| 268 | 14–15 | Two cancelled items before Mais. | Each is estimated as one word. | low |
| 269 | 4 | One cancelled symbol before inserted \Pi. | The replacement is clear but the cancelled symbol is not. | low |
| 269 | 9–10 | le \| les; multigaloisien \| multigaloisiens; correspondant \| correspondants | The number endings are weak; agreement has not been imposed. | medium |
| 269 | 10 | Inserted hat-pi with superscript circle \| zero. | The superscript’s meaning is not inferred; in particular it is not silently normalized as an opposite or completion notation. | medium |
| 269 | 11 | One cancelled item before diagrammes. | Unrecoverable short cancellation. | low |
| 269 | left margin | Rigidité | The first word of the diagonal note is uncertain. | low |
| 269 | left margin | représentation \| représentations | The plural ending, opening punctuation, and note boundary are weak. | low |
| 270 | 2 | One cancelled item after B_{D_i^*}. | The overwritten item cannot be read. | low |
| 270 | 2 | f_i \| \rho_i on the first arrow. | The tall loop can be read as either letter. | medium |
| 270 | 2 | \widetilde B_{\Pi_i} | The subscript is overwritten; the later occurrence is clearer. | medium |
| 270 | 8 | Inserted fibres \| fibrés | The interlinear word is compact and its accent/ending is uncertain. | medium |
| 270 | 8–10 | Deleted Soit [one illegible item]; deleted S la catégorie des. | The first cancelled symbol is unreadable; the order of the replacement is inferred from the visible insertion levels, not from a corrected sentence. | low |
| 270 | 12 | Deleted restrictions pleines; surviving catégories. | The crossing and the start of the surviving noun overlap. | low |
| 270 | 17 | The right-hand M appears to have a tilde. | The mark could instead be a small stray or abandoned stroke; it is retained under a doubt mark. | low |
| 270 | 17 | Calligraphic R at the left, plainer R at the right. | The visible typographic difference is retained rather than made uniform. | medium |
| 270 | 19 | Je conjecture que c’est une | The supplied image ends before the noun or proposition; no completion is available in these scans. | high |

## Abbreviations met

Expansions here are interpretative aids only. They are not substituted into the transcription. Entries marked tentative depend on a doubtful reading of the abbreviation itself.

| Form on the page / in the fragment | Proposed expansion or sense | Qualification |
|---|---|---|
| autom. | automorphismes | Scan 261. |
| i.e. | id est; c’est-à-dire | Latin abbreviation. |
| isom. | isomorphes / isomorphisme | The first occurrence on scan 261 is doubtful; the grammatical use differs between the two occurrences. |
| pt | point | Scan 261. |
| Th. | théorème | Scan 261. |
| m with a short bar (`\overline{\mathrm m}`) | même | Also in lui-m-bar; the sign is retained in the fragment. |
| hom. | homomorphisme | Scan 262. |
| surj. | surjectif | Tentative interlinear reading on scan 262. |
| rev. | revêtement | Scans 262 and 269. |
| NB | nota bene | Appears in the running text and a marginal note. |
| cat.; 2-cat. | catégorie; 2-catégorie | Inflection depends on the sentence. |
| tte | toute | In composante connexe and, provisionally, the scan 268 margin. |
| tt | toutes | Tentative; on scan 266 it could instead be a quantifier-like sign. |
| ess. comm. | essentiellement commutatifs | Tentative; en. comm. is the competing literal reading on scan 265. |
| resp. | respectivement | Scan 266. |
| ds | dans | Scan 266. |
| iso / iso. | isomorphisme(s) | The tiny deleted iso on scan 266 is uncertain; iso. also occurs in the scan 268 margin. |
| ch with raised t | changement | Tentative reading on scan 267. |
| quelconq. | quelconques | Scan 267. |
| morph. | morphisme | Scan 268. |
| op. | opération | Scan 268. |
| comp. | composante | Scan 269. |
| Automorph. | automorphismes | Tentative marginal reading on scan 268. |
| Ob | objets | Mathematical notation, notably in the scan 266 construction. |
| Aut | automorphismes | Mathematical notation in scan 270, with the base specified by its subscript. |
| Isom | isomorphismes | Name of the space on scan 264; retained under its visible underlining. |

## Legibility and reliability

The main prose is substantially more legible than the corrections and margins, but this is not a clean copy. The least reliable regions are the crossed opening of the diagonal note on scan 268, the overlap between the lower-left note and running text on scan 267, the long unread expression on scan 264, and the rewritten categorical definitions on scans 266 and 270. Short inflections, faint punctuation, overwritten subscripts, and distinctions between a calligraphic letter and a rapidly retraced ordinary capital also remain vulnerable. The diagram with the curved alpha stroke on scan 265 and the braced arrow-category notation on scan 266 are described rather than forced into more precise mathematical diagrams than the ink warrants.

Open parentheses, abbreviated forms, changes of indices, and the unfinished final conjectural sentence have not been repaired. In particular, the differing appearances of the extension index on scans 261 and 263, and the possible extra mark over the final M on scan 270, are not harmonized. Unmarked words should not be taken as a guarantee against residual reading errors; the table identifies the doubts that were recognized during this transcription.

---

# Research notes — separate from the transcription

These are source-based reading notes and explicitly labeled proposals for further work, not a literature review or a claim that an idea is established or new. They do not supply missing manuscript words. A quotation from a doubtful region is restricted to the legible words; the uncertain connective text is not promoted into a proposition.

## R01 — Scan 261, approximately lines 1–11 — Unproved claim

The passage treats the low-genus cases as comparatively immediate and contrasts them with “c’est le cas $g\geq 2$ qui est profond.” A proof would need the precise definitions of the spaces and equivalence relations from the preceding manuscript, together with a justification of the assertion about complex structures on the sphere and the orientation-preserving action. The displayed indices must first be checked against those definitions, rather than silently reversed to fit familiar notation (Grothendieck, 1981, scan 261).

## R02 — Scans 261–262, approximately 261:12–23 and 262:1–8 — Unproved claim

The proposed interpretation is as a “groupe fondamental mixte,” replacing the earlier difficulty that the quotient group did not itself act on the original surface. The accompanying discussion of a quotient by the infinitely connected identity subgroup and of a lifted extension is a program for comparing two constructions, not a complete comparison proof on these pages. A proof should specify the acting groups, their topologies, the lifted action, and the map between the two extensions (Grothendieck, 1981, scans 261–262).

## R03 — Scan 262, approximately lines 9–17 — Unproved claim

The construction begins with “un $A_{g,\nu}^0$-torseur” and uses it to twist the surface into the displayed associated bundle over $\widetilde M$. The local-triviality or fibration hypotheses, the convention for the diagonal action, and the residual group action should be made explicit. The parenthetical identification with the universal family with Teichmüller rigidification is also asserted without a construction in this excerpt (Grothendieck, 1981, scan 262).

## R04 — Scan 263, approximately lines 1–3 — Unproved claim

From the infinite connectedness statements, the text concludes that inclusion of a fibre “est un homotopisme.” A proof should distinguish the homotopy-group argument from whatever additional hypotheses justify the stated homotopy-equivalence conclusion. In particular, the manuscript’s term “$\infty$-connexe” should not simply be replaced by “contractible” without examining the spaces and the intended category (Grothendieck, 1981, scan 263).

## R05 — Scan 263, approximately lines 4–10 — Unproved claim explicitly left without details

The residual action produces an extension by the displayed fundamental group, after which the author writes “je me dispense de donner le détail.” The omitted step is the identification with the already named primed extension, including the choices of base point, lifts, and identifications of the kernel. The visible subscript here differs from the earlier $\nu+1$ notation; this is a question to resolve from the wider manuscript, not a correction made in the fragment (Grothendieck, 1981, scan 263).

## R06 — Scan 264, approximately lines 12–19 — Unproved claim

The proposed 2-morphisms are “les classes d’homotopie de chemins” in a space of isomorphisms, whose connected components are then described using torsors and a $K(\Pi,1)$-type assertion, with the pi glyph itself uncertain. A full construction should specify endpoints in the path homotopies, horizontal and vertical composition, and the treatment of disconnected surfaces. The homotopy-type assertion needs to be checked with exactly the exceptional cases and admissibility condition visible here (Grothendieck, 1981, scan 264).

## R07 — Scan 264, approximately lines 8–11 — Unpursued implication

The condition that a component “de genre $0$ rencontre $S$” is an explicit part of the chosen admissibility definition. It warrants a separate examination of low-complexity components and of how the construction handles disjoint unions. Nothing on these pages licenses substituting a stronger stability inequality for this particular condition (Grothendieck, 1981, scan 264).

## R08 — Scans 264–265, approximately 264:20 and 265:1–5 — Unproved claim

“On trouve un $2$-foncteur” introduces the passage from surfaces to morphisms of multigaloisian topoi, or to groupoid morphisms. To substantiate that statement, one needs the precise construction of the source object labeled $D^*$, the map to the surface object, and its behavior under both homeomorphisms and the path-class 2-morphisms. Those definitions are not all supplied in the present ten scans (Grothendieck, 1981, scans 264–265).

## R09 — Scan 265, approximately lines 6–17 — Unproved claim

The square includes “une donnée de commutativité,” while morphisms between such objects are left “définis ad hoc.” Writing out those morphisms and their compositions would determine which coherence data are retained, rather than merely asserting that the square commutes. The direction of the displayed comparison and its compatibility with composition need particular care (Grothendieck, 1981, scan 265).

## R10 — Scan 266, approximately lines 7–18 — Unproved claim

The passage constructs a total category by a disjoint union of object sets, with within-fibre morphisms and cross-fibre morphisms described through the indicated transport functor. It then asserts a “foncteur canonique” to the arrow category and a cocartesian property. A verification should spell out identities, composition, the allowed directions of cross-fibre morphisms, and the asserted universal property; the heavily rewritten groupoid subscripts should be settled before doing so (Grothendieck, 1981, scan 266).

## R11 — Scans 266–267, approximately 266:18 and 267:1–10 — Unpursued implication

The alternative description using inverse images is accompanied by “trois foncteurs adjoints,” followed by exactness and limit/colimit language. This suggests checking explicitly how the cofibred groupoid description and the fibred-topos description encode the same arrow without inadvertently reversing the geometric-morphism convention. The lower arrow in the limit notation is a reading doubt and must be resolved before treating that particular preservation statement as fixed (Grothendieck, 1981, scans 266–267).

## R12 — Scan 267, approximately lines 11–19 — Unproved claim

The essential image is described through the condition “structure à lacets,” yielding the named sub-2-category. These pages do not enumerate a complete intrinsic list of conditions on an arbitrary arrow of multigaloisian topoi. A useful next step is to separate the conditions on its objects, its morphisms, and its 2-morphisms, and determine which of those have actually been established earlier (Grothendieck, 1981, scan 267).

## R13 — Scan 267, lower-left marginal note — Unproved claim / excluded example

The legible marginal wording says “on exclut” and contrasts “topos vide” with “topos ponctuel.” The accompanying groupoid formulas are less secure, so they do not support a more detailed assertion here. The mathematical issue worth checking is why this degeneration is excluded and whether the exclusion follows from the stated surface admissibility condition or from an additional condition on the target category (Grothendieck, 1981, scan 267, margin).

## R14 — Scan 268, approximately lines 1–4 — Unproved claim

The author says that the functor is “$2$-fidèle” and consequently gives an equivalence with the indicated essential image. One must recover the author’s meaning of that 2-categorical fidelity term before translating the statement into a modern combination of faithfulness, fullness, and essential surjectivity. A proof should make clear which data recover the surface isomorphisms and which recover their 2-morphisms (Grothendieck, 1981, scan 268).

## R15 — Scan 268, diagonal upper-left marginal note — Unpursued implication, textually insecure

The note brings an $H^2$ expression into proximity with “orientation !” and “Dans l’analogue arithmétique.” The beginning, several connecting words, and the coefficient/comparison glyph are not sufficiently legible to extract a precise orientation or arithmetic assertion. This is a priority passage for renewed image examination or comparison with surrounding authorial definitions before proposing a theorem or conjecture from it (Grothendieck, 1981, scan 268, margin).

## R16 — Scan 268, approximately lines 5–18 — Unproved claim

For a group action, the text says that the data “équivaut à celle” of the displayed diagram ending in $B_\Gamma$. A proof should specify whether the starting action is strict or coherent up to isomorphism and show how the chosen notion is reconstructed from the diagram. It should also compare morphisms and 2-morphisms, rather than prove only a correspondence of objects (Grothendieck, 1981, scan 268).

## R17 — Scan 269, approximately lines 1–18 — Unpursued implication

The reason for replacing the group by a groupoid is explicitly tied to “quand on fait varier $\Gamma$,” with the groupoid “jouant le rôle d’un groupoïde fondamental.” This invites an examination of functoriality under change of the base groupoid and of how different choices of objects in a connected component affect the resulting surface families. The target diagram formulation should be compared with the source representation formulation at that varying-base level (Grothendieck, 1981, scan 269).

## R18 — Scans 269–270, approximately 269:19–21 and 270:1–6 — Unproved claim

The footnote pulls back along universal coverings and asserts that the family indexed by $i$ “permet de récupérer la situation complète.” The missing proof is a reconstruction or descent argument retaining the deck-group actions as well as the componentwise diagrams. It should establish independence from the chosen universal coverings and compare the reconstruction on morphisms, not only on objects (Grothendieck, 1981, scans 269–270).

## R19 — Scan 270, approximately lines 7–11 — Unproved claim

Admissibility of the global diagram is defined by requiring the displayed local diagrams to be “admissibles,” after which the restricted target 2-category and functor are written down. One needs to check independence of all choices used to obtain those local diagrams and closure under the appropriate isomorphisms and 2-morphisms. The inserted noun before the local diagram reference is itself doubtful, so no extra categorical meaning is inferred from that noun (Grothendieck, 1981, scan 270).

## R20 — Scan 270, approximately lines 12–19 — Conjecture / stated program, incomplete in the supplied material

The author restricts to base groupoids with finite fundamental groups and proposes to study “ses propriétés de fidélité.” The last line begins “Je conjecture que c’est une” but does not contain the completion. These images therefore support the existence of a conjectural continuation, not a claim that the finite-base functor is an equivalence, fully faithful, or any other particular property (Grothendieck, 1981, scan 270).

## R21 — Scans 261–263 — Own idea

Try a direct path-lifting model for the mixed fundamental group: record an acting-group element together with a path relating a chosen base point to its image, and compare multiplication with the earlier lifted extension. This could turn the author’s omitted identification into an explicit comparison of lifts and factor systems. **Confidence: medium as a proof strategy**, because the visible argument already supplies an action and a candidate kernel, but the needed topology and coherence hypotheses have not been fixed in the excerpt.

## R22 — Scans 264 and 267 — Own idea

Test the proposed intrinsic admissibility conditions first on arrows of groupoids with empty source and trivial or nontrivial connected target, then compare them with the exact surface condition written on scan 264. This is a way to isolate the role of the excluded empty/point example without imposing a stability convention from outside the manuscript. **Confidence: medium as a diagnostic**, because the example and the componentwise surface condition are explicit, while the full “structure à lacets” axioms are not.

## R23 — Scans 265–266 and 268 — Own idea

As a coherence test, investigate whether two choices of equivariant comparison data on the same underlying arrow can become indistinguishable after passage to the target diagram. Work out an explicit small groupoid example before treating this as a potential obstruction to fidelity. **Confidence: low**, because the manuscript has not yet specified all morphism and 2-morphism conventions; the proposed ambiguity may disappear once those conventions are fixed.

## R24 — Scans 269–270 — Own idea

For the finite-base restriction, begin with a one-object base groupoid for a small finite cyclic group and track local diagrams, deck actions, and their automorphism groupoids through the universal-cover reconstruction. Compare the trivial-action case with a nontrivial action, without assuming what the unfinished conjecture asserts. **Confidence: medium as a test construction**, because the componentwise reconstruction and finite-base restriction are visible, but there is not yet a proof that this test captures every possible coherence issue.

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2; supplied scans 261–270 of the archive file “pages 1–292”]. Université de Montpellier.
