# Post-freeze research report: cote 18, scans 005–017

Research agent report to the principal transcriber; not an alternative transcription. The canonical page fragments were read as frozen, without opening any manuscript image or editing any transcription. The supplied `context/README.md` and `context/notes/RESULTS_STATE.md` were read before these notes; the earlier archive transcription and notes remain first-pass claims. All page-line references below refer to `pages/MPL_15_195-228+18_002-017_18_scanNNN.tex`, not to the combined file.

## Main finding and distinctions

The live sheet 18/011 explicitly bears **“Conj. de transcendance forte”**, followed by the equality `trdeg k(α,β)/k = g+u` under `k⊂Qbar` (lines65–67). Its intended consequence `trdeg k(α)/k=g` is an ordinary period-conjecture statement, but the frozen text honestly retains an uncertain denominator `K|k` in lines70–71; the stronger equality additionally concerns the Hodge splitting β. The entirely cancelled body of 18/012 contains a normalized determinant-one version, whereas 18/013 separately asks for full period transcendence degree, generation of the group by the period locus, and transcendence of the Hodge splitting. These three questions must not be conflated.

The manuscript question on the algebraicity of the elliptic Hodge splitting has a particularly close later primary witness: Katz (1976), **Question4.0.8, p501**, asks whether algebraic descent of that splitting forces complex multiplication; his **Lemma4.0.7** proves the CM direction. No assertion about a current resolution of the converse is warranted by the literature checked here.

## Context search audit

The following literal/regex searches were run on `context/MPL_16+47+54+44_transcription.tex` and checked against its cote/scan markers; the corresponding research notes were searched for the same objects. These are contextual comparisons, not independent verification of the earlier readings.

| Query family | Actual context witness / absence | Use below |
|---|---|---|
| `transcend`, `périod`, `period`, `Conj. de transcendance` | No period-conjecture statement in the earlier transcription: “transcendante” at16/021 concerns the transcendental part of H²; “périodicité” at16/035 concerns Bott periodicity | P15–P23, P26 |
| `torseur`, `torsor`, `Isom`, `Levi`, `Lévi`, `unipotent`, `Fil`, `Big` | The `C`-torsor pairings at47/003 concern integral transforms, not comparison isomorphisms; no matching Fil/Big period-torsor construction | P10–P17 |
| `Hodge`, `DeRham`, `de Rham`, `extension`, `splitting` |54/003,005,007: Hodge–de Rham extension, universal vector extension, duality and reconstruction from p-torsion; earlier notes D01–D05 discuss these; Oda supplied PDF, Cor5.11, printedp131 | P01–P04, P24–P25 |
| `crist`, `cryst`, `Dieud`, `Frobenius`, `Verschiebung` | No crystal-classification statement in the earlier transcription;54/005,007 have Cartier duality and F/V; earlier notes D03–D05; Oda Cor5.11 | P03–P06 |
| `Tate`, `poids`, `twist`, `bigrad`, `graduation` |16/003–006 concern gradings/projectors,16/021 uses Z_l[1],44/008 uses H^(2i−1)(X,Z_l(i)); no mixed-Hodge twist formula in that transcription | P09, P14, P31 |
| `spécialisation`, `Chow`, `torsion`, `cycles` |16/026 has a different specialization correction;16/021 tracks NS/Brauer torsion,47/009 rational versus integral correspondence cycles; no matching SGA specialization square | P07–P08 |
| `2i\\pi`, `résidu`, `fondamentale`, `Poincaré`, `cup` |16/052 gives the analytic Kummer generator exp(2iπ/n);54/003,005 give duality without this normalization; no identical local fundamental-class proof | P27–P30 |
| `ellip`, `Schneider`, `multiplication complexe`, `Gl(2`, `Sl(2` | No Schneider or elliptic full-period conjecture in the earlier transcription;16/014–018 gives a different Lefschetz operator algebra, and54/003,005 the abelian de Rham extension | P18–P26 |

Each P item below identifies the relevant context result and relation explicitly. For the period-specific items the closest register entry is **WG2 §2.4 #3**, an unchecked planning question about the motives folders; the supplied register contains no dedicated period-conjecture item. This is a broad project connection, not a claim that the entry already establishes anything about periods.

## Candidate observations (each prose observation is at most four sentences)

### P01 — Six conjectural realization descriptions

**Location:**18/005, lines2–16. **Kind:**conjecture. **Quote:**“Descriptions conjecturales de motifs”. **Context search/relation:**`Hodge|DeRham|Gauss|Tate`; context54/003,005,007 and notesD01–D05: **adds** a six-way classification programme to particular abelian comparisons. **RESULTS_STATE:**LM7 C.1 [Known, return's claim]; MPL_14_002-044 M01 [first-pass lead]; WG2 §2.4 #3 [unchecked plan].

The numbered Betti–deRham, Betti–Hodge, Hodge, Betti–Gauss–Manin, Betti–Tate and filtered crystalline descriptions are explicitly conjectural, not stated equivalences with specified essential images. Relative to the register's explicit realizations of one Fermat1-motive, this sheet adds a general classification question, without supplying a functorial construction or proving that arbitrary compatible realization data come from motives.

### P02 — Missing local analogues

**Location:**18/005, lines18–28. **Kind:**self-flagged. **Quote:**“Par quoi remplacer1',4'??”. **Context search/relation:**`crist|Hodge|de Rham|Tate`; context54/003,007/OdaCor5.11: **adds** unanswered local-field analogues, not a restatement of their characteristic-p comparison. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; LM7 C.1 [Known, return's claim, only realization background].

The sheet explicitly leaves the p-adic analogues of its first and fourth descriptions unidentified. Its phrase “mod isogénie” and allowance for finite extension of the local field are substantive restrictions; none of the supplied context fills these two numbered gaps.

### P03 — Filtered crystals need an admissibility condition

**Location:**18/005, lines18–26. **Kind:**unpursued implication. **Quote:**“cristal filtré”. **Context search/relation:**`crist|Frobenius|filtr`; context54/005,007 and OdaCor5.11: **differs**, because those concern characteristic-p finite group schemes rather than the local-field essential image. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; MPL_7_061-072+8_001-078 Scan061(§66) [first-pass neutralization lead].

Colmez and Fontaine's theorem identifies weakly admissible filtered(φ,N)-modules with semistable p-adic representations, providing a precise later comparison for one part of this programme (Colmez & Fontaine,2000, TheoremA and §4). The sheet itself does not impose weak admissibility or distinguish crystalline from semistable objects, so that theorem cannot be quoted as establishing every proposed equivalence or as classifying all geometric motives.

### P04 — What Oda actually supplies

**Location:**18/005, lines18–26; compare18/011, lines5–7. **Kind:**unpursued implication. **Quote:**“groupes p-divisibles mod isogénie”. **Context search/relation:**`Dieudonné|p^A|extension`; context54/007 and notesD05, supplied OdaPDFCor5.11,p131: **adds** a local-field programme to a solved characteristic-p realization comparison. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 M24a [first-pass abelian-scheme lead].

Oda's Corollary5.11 canonically compares the Dieudonné module of the p-torsion of an abelian variety over a perfect field of characteristicp with H¹_dR, compatibly with the Hodge exact sequence (Oda,1969,p131). This verifies a sharply delimited comparison behind the supplied context54/007 question, while leaving the local lift, the rational p-adic representation and the essential image in18/005 as additional problems.

### P05 — The ℓ-adic line in a p-divisible list

**Location:**18/005, line24. **Kind:**reading question. **Quote:**“module galoisien ℓ-adique”. **Context search/relation:**`Tate|p-divisible|Dieudonné`; context44/008 has a genuine ℓ-adic Tate-module statement, whereas54/007 and OdaCor5.11 concern p-torsion: **differs** in coefficient prime. **RESULTS_STATE:**LM7 C.1 [Known, return's claim]; WG2 §2.4 #3 [unchecked plan].

The frozen line uses ℓ, although the surrounding local classification and N in line20 are p-adic. A prime-to-p Tate module of a p-divisible group cannot carry the same information, so this is a notation or scope question to collate, not a license to replace ℓ byp in the transcription.

### P06 — Recovering the cyclotomic kernel needs a hypothesis

**Location:**18/006, lines35–45. **Kind:**unproved claim. **Quote:**“Keru…connu”. **Context search/relation:**`Tate|cyclot|Kummer|Ker`; context16/052 (analytic Kummer generator) and44/008 (twisted Tate module): **adds** a comparison of two splittings. **RESULTS_STATE:**LM7 C.1 [Known, return's claim]; MPL_14_002-044 B04 [first-pass lead]; LM6 A.22 [Open, return's claim, distinct normalizer problem].

The formula φ(γ)=u(γ)j₂(χ(γ))⁻¹ immediately gives φ=u on kerχ, but the displayed equality keru=kerχ∩kerφ additionally needs keru⊂kerχ. A sufficient omitted structural reason would be that the Tate character χ factors through the realization u; this condition should be checked before using the p-adic analytic quotient, and the calculation does not settle LM6 A.22.

### P07 — Integral specialization is a separate problem

**Location:**18/007, lines10–17. **Kind:**self-flagged. **Quote:**“on n'a pas développé…une théorie de la spécialisation pour l'anneau de Chow”. **Context search/relation:**`spécialisation|Chow|torsion`; context16/021 and47/009: **adds** a distinct integral-specialization obstruction to their torsion warnings. **RESULTS_STATE:**WG2 S28(§1.7) [unchecked plan]; WG2 §2.3 #3 [unchecked plan concerning an integral counterexample].

This annotated typescript explicitly separates the established rational compatibility from the stronger integral Chow statement that would retain torsion. Its surviving fallback uses raw cycles and an inserted smooth-proper hypothesis, so an integral ring-level compatibility must not be attributed to the page merely from the rational diagram.

### P08 — An explicit weakening on the annotated typescript

**Location:**18/007, line10. **Kind:**withdrawn in the same text. **Quote:**deleted“on est”; inserted“il semble qu'on sera”. **Context search/relation:**`spécialisation|torsion`; context16/021 and47/009: **adds** a local qualification, with no matching earlier wording. **RESULTS_STATE:**WG2 S28(§1.7) [unchecked plan].

The author weakens necessity of passing to the Chow ring from an assertion to a tentative expectation on the same scan. This is a revision of epistemic force, not a retraction of the rational commutative squares or proof that the future integral programme is impossible.

### P09 — The associated-graded twist has an index problem

**Location:**18/009, lines8–21. **Kind:**reading question. **Quote:**“Twist de Tate sur structures de Hodge mixtes”. **Context search/relation:**`Tate|poids|graduation`; context16/003–006 and44/008: **adds** mixed-Hodge conventions; the ledgerMPL_14_002-044 B04 is only a prior lead. **RESULTS_STATE:**LM7 C.1 [Known, return's claim]; MPL_14_002-044 B04 [first-pass lead].

The general displayed convention W_i(E(n))=W_{i+2n}(E), F^i(E(n))=F^{i+n}(E) agrees with a twist of weight−2n (Deligne,1971,§2.1.13). Under that convention the associated-graded formula should be interpreted as Gr_i^W(E(−1))≅(Gr_{i−2}^W E)(−1), while the frozen line14 retains unshifted indices and its incomplete parenthesis; the mathematical reconciliation belongs only in this note.

### P10 — Filtrations and splittings are different parameter spaces

**Location:**18/011, lines20–38,46–49. **Kind:**unproved claim. **Quote:**“Big…torseur sur Fil”. **Context search/relation:**`Fil|Big|bigrad|torseur`; context54/003,005 has the Hodge extension, while47/003 has unrelated C-torsors: **adds** the parabolic/Levi parameter spaces. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 M01 [first-pass lead].

The asserted map Big→Fil is modeled on G/L→G/B with unipotent fibre B/L, giving dimensions g−ℓ and g−b when B has LeviL and unipotent radicalU of dimensionu=b−ℓ. A proof must identify the tensor filtrations of the fixed type with those homogeneous spaces and the relative unipotent group; it is not merely the statement that every individual filtered vector space has a splitting.

### P11 — The overloaded Q and missing Tate normalization

**Location:**18/011, lines6,25–29,38,51–52. **Kind:**reading question. **Quote:**“Q=fibré des sous groupes de Lévi”. **Context search/relation:**`Lévi|Levi|torseur|Tate`; no corresponding Q in context; nearest54/003 Hodge extension: **adds**, with an internal interpretation tension. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 B04 [first-pass lead].

Line6 treats Q as an H′-reduction of an isomorphism torsor, whereas the margin identifies it with the space of Levi subgroups and defines H′ as the inverse image of a central TateG_m inB′/U′. On those descriptions dimH′=u+1 but the Levi-space dimension isu, so a Tate normalization, a quotient or a change in the use ofQ has to be specified before the field bounds are treated as a proof. The frozen symbols should remain untouched.

### P12 — The type field resembles a reflex-field construction

**Location:**18/011, lines24,30–31,63. **Kind:**own idea. **Quote:**“Q(φ₁) est indépendant du plongement”. **Confidence:**medium; the quotient by conjugacy and the Galois-twisted Weyl orbit are visible, but the final margin is partly illegible. **Context search/relation:**`Γ/W|type|déployé|Hodge`; context16/003–006 gives gradings,54/003 gives Hodge cohomology; **adds** arithmetic descent of a conjugacy class. **RESULTS_STATE:**MPL_14_002-044 B04 [first-pass lead]; WG2 §2.4 #3 [unchecked plan].

A useful comparison is to define the smallest field of definition of the conjugacy class of the Hodge cocharacter and compare it with Q(φ₁), rather than identifying the two without proof. The proposed Weyl-orbit description is the evidence for this route, but neither the unfinished independence sentence nor the supplied context proves that it has all properties of a modern reflex field.

### P13 — A direction discrepancy in the filtration map

**Location:**18/011, lines30 and36. **Kind:**reading question. **Quote:**“F→Φ induitA≃B”. **Context search/relation:**`filtrat|bigrad`; context54/003,005 has an extension without a canonical algebraic splitting, and notesD01–D02 emphasize that distinction: **differs** from an unqualified map choosing splittings. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan].

The main diagram has Big→Fil, whereas the margin literally gives F→Φ for the unrestricted spaces. Forgetting a splitting gives a natural map in the former direction; a reverse map requires extra data, so the margin may concern only the induced bijection of types or may contain a slip, neither of which justifies altering the frozen arrow.

### P14 — A section of the Tate character is not automatically a central weight cocharacter

**Location:**18/011, lines27–29,38. **Kind:**unpursued implication. **Quote:**“hom central(Tate)”;“ε…∘j=id”. **Context search/relation:**`graduation|Tate|centre`; context16/003–006,018 and ledgerB04: **adds** a precise Levi-quotient section to their grading data. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 B04 [first-pass lead]; MPL_14_087-132 M04 [first-pass subgroup-inclusion lead].

The written centrality is in the Levi quotient B′/U′, and the equation ε∘j=id supplies a splitting of its Tate character there. It does not by itself put a chosen lift centrally insideG′, identify that lift with the weight cocharacter of the full category, or embed the unrelated Lefschetzsl₂ of cote16 intoG′.

### P15 — The explicit strong period conjecture

**Location:**18/011, lines65–76. **Kind:**conjecture. **Quote:**“Conj. de transcendance forte”;“alors?”. **Context search/relation:**`transcend|period|torseur`; no matching conjecture in context16/021 or47/003; `README.md`, planning section, specifically asks for it: **adds** an explicit written witness. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan; broad connection]; no dedicated period entry.

For k⊂Qbar the sheet asks whether trdeg_k k(α,β)=g+u, with g=dimG andu=dimU′. This includes the expected maximal transcendence of the Betti–deRham comparisonα and an additional independence assertion for the Hodge-splitting comparisonβ, so it is stronger in content than simply the standard equality trdeg k(periods)=dimG (compare Bost & Charles,2016,§2.2).

### P16 — The consequences are a maximality calculation, conditional on the bounds

**Location:**18/011, lines49–56,67–76. **Kind:**own idea. **Quote:**“g+u”. **Confidence:**high for the stated conditional calculation, because transcendence degree is additive in towers; medium for applying all written bounds untilQ is clarified. **Context search/relation:**`transcend|Fil|Big`; no period tower in context, nearest54/003 is an extension of realizations: **adds** an explicit dependency calculation. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan].

If the diagram really supplies trdeg k(α)/k≤g and trdegK/k(α)≤u, equality trdegK/k=g+u forces both bounds to be sharp. Repeating that argument through the filtration and splitting quotients gives the intended dimensions g−b andg−ℓ, without constituting evidence that the initial strong equality is true.

### P17 — The denominators K|k must remain a reading question

**Location:**18/011, lines70–71. **Kind:**reading question. **Quote:**`deg tr.k(α)/\unsure{K|k}`. **Context search/relation:**`transcend|period`; no counterpart in the earlier transcription; READMEperiod question: **adds** a local ambiguity within the new witness. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan].

The first two displayed consequences have a frozen uppercase/lowercase ambiguity. Since K=k(α,β) lies above k(α), reading their denominator asK would not define the displayed field extensions in the usual sense; lowercasek is therefore the mathematically natural interpretation, but this is contextual evidence only and cannot replace the recorded ink-based alternatives.

### P18 — A cancelled normalized version is still a conjectural witness

**Location:**18/012, lines2–24, especially5–11,18–23; compare18/011,65–76 and18/013,4–6. **Kind:**withdrawn in the same text. **Quote:**“Conjecture…de transcendance”;“la seule relation”. **Context search/relation:**`transcend|period|Sl`; earlier16/014–018 is a different Lefschetz construction and contains no period conjecture: **adds** a cancelled formulation. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; MPL_14_087-132 M04 [first-pass lead, only warning to distinguishsl₂roles].

The entire body of scan012 is cancelled, including the claimed normalized transcendence degree dimG−1 and the elliptic determinant-one example. Scans011 and013 show related live questions, but their juxtaposition does not establish a revision chronology or prove that the author rejected the truth of the cancelled conjecture rather than this formulation.

### P19 — A group-generation corollary requires the density interpretation

**Location:**18/012, lines9–11. **Kind:**unproved claim. **Quote:**“le k-groupe algébrique engendré parg₀”. **Context search/relation:**`groupe algébrique|semi-simple|transcend`; context16/049 concerns semisimplicity of a motive category, not generation by a comparison point: **adds** a separate group-generation consequence. **RESULTS_STATE:**LM1 A.8 [Refuted, return's claim, warns against forgetting determinant data]; WG2 §2.4 #3 [unchecked plan].

If g₀ is scheme-theoretically generic in the normalized connected group, every k-closed subgroup containing it must equal that group, which explains the first generation consequence conditionally. The further claim that one pointg generatesG under semisimplicity and transcendence ofπ requires a careful argument about the central torus and the normalization; it is not supplied by the dimensions alone.

### P20 — Schneider is a consequence, not an equality theorem

**Location:**18/012, lines13–22. **Kind:**unproved claim. **Quote:**“Contient le th.deSchneider”. **Context search/relation:**`Schneider|ellip|transcend`; no matching context theorem;54/003,005 only gives abelian deRham comparison: **adds** a proposed transcendence consequence. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan].

The cancelled claim of transcendence degree3 for four normalized elliptic periods, subject only to determinant1, is substantially stronger than mere transcendence of individual periods or the classical CM criterion for an algebraic period ratio. Grothendieck's published1966 note already distinguishes Schneider's theorem from conjectural algebraic independence of periods and quasiperiods (p102,n10), so the phrase must not be presented as a proof of the displayed degree.

### P21 — The transcendental-j line has a changed base-field issue

**Location:**18/012, line23 and margins25–26. **Kind:**self-flagged. **Quote:**“Si l'invariantj est transcendant”;“π nonAlg.surk?”. **Context search/relation:**`transcend|ellip`; no counterpart in context; READMEperiod question: **adds** a tentative extension beyond algebraic ground fields. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan].

The cancelled draft addsj to the normalized period tuple and predicts total transcendence degree4, while the margin questions the field condition onπ and a special algebraic-τ case. Modern André–Grothendieck formulations over transcendental ground fields also count transcendence of the ground field, but that is a comparison of formulations rather than a retrospective identification of the uncertain “pré-minimal” condition (Bakker & Tsimerman,2025,Conjecture1.2).

### P22 — The elliptic period conjecture is explicitly written

**Location:**18/013, lines2–6. **Kind:**conjecture. **Quote:**“degré de transcendance égal àdimG(4ou2)?”. **Context search/relation:**`period|ellip|Gl`; no matching earlier context statement; READMEplanning asks for the witness: **adds** a direct elliptic formulation. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; no dedicated period entry.

The live sheet explicitly distinguishes the non-CMGL₂ case, predicting degree4, from the CM torus case, predicting degree2. In a modern torsor formulation this is the corresponding Grothendieck period conjecture; the CM elliptic case is known, while the full non-CM degree4 assertion is not supplied by the weaker deRham–Betti results cited here (Bost & Charles,2016,§2.2).

### P23 — Generation of the elliptic period locus is weaker than genericity

**Location:**18/013, lines8–10. **Kind:**conjecture. **Quote:**“A-t-onH=G”. **Context search/relation:**`torseur|groupe engendré|ellip`; context47/003 torsors and16/049 semisimplicity do not ask this: **adds** a separate weaker question. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; LM1 A.8 [Refuted, return's claim, only determinant-data boundary].

After choosing a Qbar-point of the period locus and translating it to the identity, the smallest algebraic subgroup containing that translated locus expresses the smallest algebraic torsor generated by the period point. For a single elliptic curve, Kreutz,Shen,andVial's coefficient-field version of the deRham–Betti theorem supplies an affirmative modern route after making that torsor identification precise (§3.1 andTheorem5.13,2026v3), but it does not prove that the original locus itself is the full torsor or that its dimension is4.

### P24 — The Hodge-splitting question matches Katz's later question

**Location:**18/013, line12. **Kind:**conjecture. **Quote:**“Peut-on avoirh∈Qbar”. **Context search/relation:**`Hodge|extension|splitting`; context54/003,005 gives the deRham extension, notesD01–D02 discuss its comparison: **adds** arithmetic transcendence of its analytic splitting. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 M24a [first-pass abelian-comparison lead].

For a non-CM elliptic curve overQbar, the page asks whether the Hodge splitting can descend to algebraic coefficients. Katz's Question4.0.8 asks precisely whether an elliptic curve over a number field with algebraically defined Hodge decomposition must haveCM (Katz,1976,p501); this later explicit question is a close literature link, without a claim of priority or a claim that its converse has been resolved in this research pass.

### P25 — The CM margin has a concrete eigenspace proof

**Location:**18/013, line14. **Kind:**unproved claim. **Quote:**“siC est à multiplication complexe…h∈Qbar!”. **Context search/relation:**`Hodge|duaux|extension`; context54/003,005 and notesD01–D02: **adds** a special splitting mechanism. **RESULTS_STATE:**MPL_14_002-044 M24a [first-pass lead]; WG2 §2.4 #3 [unchecked plan].

After adjoining the CM endomorphisms and their eigenvalues, a non-scalar CM endomorphism acts onH¹_dR with two distinct algebraic eigenlines, whose complexifications areH¹⁰ andH⁰¹. Katz's Lemma4.0.7 gives this argument explicitly, thereby verifying the CM direction under its natural field-of-definition enlargement (Katz,1976,p501).

### P26 — The normalized period and “pre-minimal” notation cannot be recovered from the published relation alone

**Location:**18/012, lines5–9,15–22. **Kind:**reading question. **Quote:**`\unsure{pré-minimal|pré-maximal}`;`\unsure{ζ|ξ}^{−1}`. **Context search/relation:**`pré-min|pré-max|Schneider|period`; no matching definition in the earlier context: **adds** unresolved notation. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan].

The Legendre relation in Grothendieck(1966,p102,n10) explains why a determinant-one normalization would remove a Tate scalar, but does not identify this sheet's ζ/ξ, its chosen square root, or its “pre-minimal” field condition. Those missing definitions prevent promoting the cancelled normalized formula to a fully specified theorem statement and leave the diplomatic alternatives intact.

### P27 — The scalar 2πi is computed, but its globalization remains a proof obligation

**Location:**18/015, lines16–24;18/017, lines4–17. **Kind:**unproved claim. **Quote:**“∫dz/z=2iπ”. **Context search/relation:**`2i\\pi|Poincaré|résidu`; context16/052 has exp(2iπ/n),54/003,005 has unnormalized duality: **adds** the local cycle-class normalization. **RESULTS_STATE:**LM7 C.1 [Known, return's claim]; MPL_14_002-044 A36 [first-pass normalization/duality lead].

The one-dimensional residue calculation fixesP_an=2πiP_top for the chosen orientation, and multiplicativity predicts the codimension-p factor(2πi)^p. This agrees with keeping Tate twists in Betti–deRham comparison, where ignoring the Tate factor changes the comparison by that scalar (Deligne,1982,§1); the local integral alone does not verify every supported-cohomology map in the global diagram.

### P28 — The transversal dimension is inconsistent with the stated point reduction

**Location:**18/015, line19. **Kind:**reading question. **Quote:**“X'^{n-p} transversale”. **Context search/relation:**`codimension|transvers|Poincaré`; no matching argument in context54/003,005 or16/052: **adds** a dimension-check question. **RESULTS_STATE:**WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 A36 [first-pass duality lead].

IfX has dimensionn andY has codimensionp, a transversal meetingY at an isolated point normally has dimensionp. The frozenX′^{n−p} may use an unstated convention or be a draft slip; dimension counting raises the question but cannot authorize silently substitutingp.

### P29 — The global Gysin degree needs collation

**Location:**18/017, lines21–25. **Kind:**reading question. **Quote:**“Il est commutatif”. **Context search/relation:**`Poincaré|codimension|2p`; no matching global comparison in supplied context, nearest54/003,005 is duality: **adds** an internal degree discrepancy. **RESULTS_STATE:**MPL_14_002-044 A36 [first-pass lead]; WG2 §2.4 #3 [unchecked plan].

The earlier local diagram uses cohomological degree2p, whereas the frozen global diagram displaysi+p on its top row. Under ordinary singular-cohomology grading a codimension-p Gysin morphism shifts by2p, so the mismatch needs either a stated regrading or a correction recorded only as commentary; overwritten support indices introduce additional uncertainty.

### P30 — The author explicitly requests the final argument

**Location:**18/015, line20;18/017, lines2,25. **Kind:**self-flagged. **Quote:**“faire le raisonnement”;“Provient de la comm.de”. **Context search/relation:**`Poincaré|commut|dual`; context54/003,005 and notesD01–D02 are different incomplete comparison arguments: **adds** a specific local-to-global proof gap. **RESULTS_STATE:**MPL_14_002-044 A36 [first-pass lead]; WG2 §2.4 #3 [unchecked plan].

The NB onscan015 is conditional on existence of a universal multiplicative scalarλ^p, andscan017 explicitly asks for the reasoning before ending its commutativity explanation mid-sentence. A complete proof would establish compatibility with local orientations, cup products, support morphisms and gluing, not merely reuse the scalar calculation.

### P31 — Retaining the abstract lattice is different from retaining its embedding

**Location:**18/009, line5;18/011, line61;18/017, lines11–17. **Kind:**unpursued implication. **Quote:**“même…module surZ”;“(2iπ)^n”. **Context search/relation:**`Tate|Z_l|2i\\pi`; context44/008 and16/052: **adds** the distinction between a coefficient module and its comparison embedding. **RESULTS_STATE:**LM7 C.1 [Known, return's claim]; MPL_14_002-044 B04 [first-pass lead].

Keeping an abstract integral module while shifting its filtrations is compatible with the written twist convention, but comparison with a complex realization also remembers the Tate period. Deligne's explicit latticeZ(n)=(2πi)^nZ and the manuscript's residue calculation make clear why these two choices should be tracked separately (Deligne,1971,§2.1.13–14).

## Standalone self-flagged-step index for these scans

| Scan, TeX lines | Wording | Classification / caution |
|---|---|---|
|005,28|“Par quoi remplacer1',4'??”|Missing local analogues; P02|
|007,10|“il semble qu'on sera”;“on n'a pas développé…”|Tentative Chow requirement and undeveloped specialization theory; P07–P08|
|007,17|“qu'on laisse…au lecteur…le soin d'écrire”|Deferred analogous cycle-specialization square; not a proof supplied on this page|
|011,67|“alors?”|Explicit question on the strong transcendence equality; P15|
|012,5–24|“Conjecture”; cancelled body|Withdrawn draft of a conjecture, not an established theorem; P18|
|012,25–26|uncertain“connu!”/“?!”;“π nonAlg.surk?”|Marginal special-case and field-condition checks; P21|
|013,6|“4ou2?”|Full elliptic period transcendence question; P22|
|013,9|“A-t-onH=G”|Locus-generation question; P23|
|013,12|“Peut-on avoirh∈Qbar”|Algebraic Hodge-splitting question; P24|
|015,20|conditional/uncertain NB onλ^p|Universality and multiplicativity assumed in reduction; P30|
|017,2,25|“faire le raisonnement”; unfinished“Provient de la comm.de”|Global commutativity proof requested, then left unfinished; P30|

No literal “à vérifier” is needed to flag the question mark on a mathematical step; ordinary explanatory assertions without such a signal are classified above as unproved claims or reading questions, not author-flagged gaps.

## Titles and numbering in the assigned range

| Scan | Heading / title | Pagination |
|---|---|---|
|005|Descriptions conjecturales…; local p-divisible analogue list|Manuscript4|
|006|No separate title; comparison of splittings|Manuscript5|
|007|Remarque7.13.11; equations7.13.10–12|Typescript18 and manuscript6|
|009|Twist de Tate sur structures de Hodge mixtes|Manuscript8|
|010|degrés de transcendance liés aux filtrations et bigraduations(comparaison deBetti,DeRham,Hodge)|Title sheet; manuscript9|
|011|Conj.de transcendance forte(internal heading)|Manuscript10|
|012|Conjecture de transcendance(cancelled)|Manuscript11|
|013|Questions sur courbes elliptiques surQbar|Manuscript12|
|014|Le foncteur de Hodge sur la catégorie des motifs(Comparaison des deux fonct.alg.et transcendants)|Title sheet; manuscript13|
|015|Comparaison de classes fondamentales analytiques(=alg)et topologiques(=transc.)|Manuscript14|
|016|Reused formal-group typescript; not a period continuation|Typescriptn°413,A-21; manuscript15|
|017|Continuation and global comparison|Manuscript16|

No total page count appears in these title sheets; manuscript pagination is not a statement that the present extract contains that many original leaves. Root should integrate cover scans002,004 and reused scan003 separately.

## Primary bibliography and exact verification scope

The URLs below were opened or searched in the live research tools; the source IDs are supplied for the principal agent's independent opening before citation. No secondary discussion site is used as evidence.

1. **Bakker, B., & Tsimerman, J. (2025).** Functional transcendence of periods and the geometric André–Grothendieck period conjecture. *Forum of Mathematics, Sigma*. https://doi.org/10.1017/fms.2025.10036 . Primary article: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/functional-transcendence-of-periods-and-the-geometric-andregrothendieck-period-conjecture/6B3E39BB9BC68DC2BC6E793D15B0735B . Verified Conjectures1.1–1.2 and4.1–4.2; used only to distinguish number-field equality from transcendental-base inequality. Source `turn1search0` / `turn1search5`.
2. **Bost, J.-B., & Charles, F. (2016).** Some remarks concerning the Grothendieck period conjecture. *Journal für die reine und angewandte Mathematik,714*,175–208. https://doi.org/10.1515/crelle-2014-0025 . Primary full text: https://arxiv.org/abs/1307.1045 . Verified §2.1–2.2, inclusions Z_X⊂Ω_X⊂Ω_X^T⊂Ω_X^And⊂Ω_X^mot, Conjecture2.12 and Proposition2.13; these explicitly separate full genericity from fullness. Sources `turn3view3`, `turn7view3`; metadata `turn26search10` (publisher).
3. **Colmez, P., & Fontaine, J.-M. (2000).** Construction des représentations p-adiques semi-stables. *Inventiones mathematicae,140*(1),1–43. https://doi.org/10.1007/s002220000042 . Author PDF https://webusers.imj-prg.fr/~pierre.colmez/CF.pdf . Verified TheoremA, introduction and§4, not a classification of all motives. Source `turn3view1`; author publication list `turn26search3`.
4. **Deligne, P. (1971).** Théorie de Hodge:II. *Publications mathématiques de l'IHÉS,40*,5–57. https://doi.org/10.1007/BF02684692 . Primary PDF https://www.numdam.org/item/PMIHES_1971__40__5_0.pdf . Verified §2.1.13–14 onTate lattice/weight/orientation, §2.1.15–16 polarization, §2.2 classical Hodge decomposition. Sources `turn30view1`, `turn32view2`, `turn32view3`.
5. **Deligne, P. (1982).** Hodge cycles on abelian varieties (notes by J.S.Milne). In P.Deligne,J.S.Milne,A.Ogus,&K.-Y.Shih,*Hodge cycles,motives,andShimura varieties* (Lecture Notes in Mathematics,900,pp9–100). Springer. Author/editor-maintained corrected PDF https://www.jmilne.org/math/Documents/Deligne82.pdf . Verified §1 (PDFpp9–11) Tate objects and comparison factors. Sources `turn15view3`; do not repeat extracted typographical oddities aboutH²(P¹).
6. **Grothendieck, A. (1966).** On the deRham cohomology of algebraic varieties. *Publications mathématiques de l'IHÉS,29*,95–103. https://doi.org/10.1007/BF02684807 . Primary PDF https://www.numdam.org/article/PMIHES_1966__29__95_0.pdf . Verified pp101–103, especiallyp102,n10: period/quasiperiod relation and algebraic-independence expectation, and arithmetic significance of Hodge-extension splitting. Sources `turn15view0`, `turn18view0`.
7. **Katz, N.M. (1976).** p-adic interpolation of real analytic Eisenstein series. *Annals of Mathematics,104*(3),459–571. Primary author PDF https://web.math.princeton.edu/~nmk/old/padicinterp.pdf ; publisher https://annals.math.princeton.edu/1976/104-3/p06 . Verifiedp501,Lemma4.0.7 andQuestion4.0.8; also4.0.5–6 for a coordinate on the antiholomorphic line. Sources `turn30view0`, `turn32view0`, `turn32view1`.
8. **Kreutz, T., Shen, M., & Vial, C. (2026).** *DeRham–Betti classes with coefficients* (arXiv:2206.08618v3) [Preprint]. https://arxiv.org/abs/2206.08618 ; current fulltext https://arxiv.org/html/2206.08618v3 . The abstract page reports last revision21January2026 while the HTML title block gives24August2026; cite the version identifier rather than inventing a journal publication. Verified §3.1,Conjectures4.5/4.7,Theorem5.13 and its coefficient-field restriction; the older author PDF is titled*Around the deRham–Betti conjecture* and has different numbering, so use the version actually checked. Sources `turn15view2`, `turn18view1`, `turn20view1`, `turn20view2`; exact Proposition3.1 andTheorem5.13 fully verified in `turn44view0` and `turn44view1`.
9. **Oda, T. (1969).** The first deRham cohomology group and Dieudonné modules. *Annales scientifiques de l'École Normale Supérieure,4e série,2*(1),63–135. https://doi.org/10.24033/asens.1175 . Supplied context PDF; online exact primary witness https://www.numdam.org/article/ASENS_1969_4_2_1_63_0.pdf . VerifiedCorollary5.11,p131,and its Hodge-sequence compatibility; no generalization to arbitrary cohomological degree or arbitrary local-field lift claimed. Sources `turn3view0`, `turn9view0`.

## Limits and handoff

- The question of a full period conjecture is positively answered as a **written conjectural witness**, not as a theorem.
- No chronology of the three period sheets has been proved from their scan order.
- The exact `Q`/`H′`/Levi interpretation and the “pré-minimal” convention remain open reading/interpretation questions.
- The local σ-semilinear “cristal” does not state the modern weak-admissibility criterion.
- No image was read, no OCR was run on manuscript scans, and no frozen transcription was edited by this research agent.
