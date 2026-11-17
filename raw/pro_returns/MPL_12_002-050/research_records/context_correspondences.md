# Context comparison: correspondence rings, Lefschetz operators and positivity

**Intermediate research record.** The reconciled conclusions and narrowed register connections are in `../MPL_12_002-050_notes.md`; see this directory's `README.md`. In particular, final notes N069–N071 distinguish the frozen 12/042–043 readings from Hua's reconstruction.

Prepared after the transcription freeze and context opening. No source scans were inspected and no frozen transcription file was changed. I read `context/README.md` and the complete `context/notes/RESULTS_STATE.md` before writing this report.

## Source keys and evidential status

- **T12**: the frozen `work/pages/MPL_12_002-050_12_scanNNN.tex`, identified below by cote/scan.
- **CT**: `context/MPL_16+47+54+44_transcription.tex`; every older cote/scan reference below is to this supplied, unreviewed transcription, not a newly inspected image.
- **CN**: `context/MPL_16+47+54+44_notes.md`; all editorial calculations and literature comparisons in this file are earlier-run claims/leads, not newly established results.
- **RS**: `context/notes/RESULTS_STATE.md`; a cited returned-package excerpt is a lead whose original full note/proof is generally absent. The referee-checked LM4/LM7 entries named in RS do not establish any of the motivic comparisons below.

## Direct answers and proposed note items

### CC01 — A correspondence-based construction is suggested but not supplied in the selected cote 12 leaves

**Kind:** reading question. **Witness:** 12/002, §2 and §5; 12/006, §8; 12/023, §1. **Quote:** “par propriété universelle”; “On définit”; “est associé une … catégorie abélienne”. **Search:** `correspond|Lefschetz|motif|pseudo-abélienne|C(X)` in T12 and CT. **Bears on:** RS **WG2 §2.4 #3**, **MPL_11_043-058+56 N031**, **MPL_15_087-138 §2**, **MPL_60_002-035 C01** (all planning/first-pass leads).

CT **16/018** explicitly defines an “anneau … de correspondances Lefschetzien”, following the universal graded-ring discussion in **16/014–017**, whereas T12 begins by outlining a category and its realizations and later stipulates categories over bases axiomatically. The relation is **adds to**, at the level of categorical formalism, but the selected leaves supply neither a full choice of rational/homological/numerical correspondence equivalence nor the explicit idempotent-completion construction that would identify these categories with CT’s rings. T12 **12/006** writes `C(X)=C(X_eta)` without furnishing that missing definition, so it should not be expanded into a categorical construction by editorial inference. RS’s **N031** is the appropriate lead for an explicit Chow projector splitting, but its underlying text/proof is not attached here and should not be reproduced as verified.

### CC02 — The relation to cote 16 is strongest at algebraic inverses and semisimplicity

**Kind:** unpursued implication. **Witness:** 12/002–005, especially 12/003 level decomposition and 12/005 characteristic-zero reductivity criterion. **Quote:** “se décompose … en somme de motifs purs”; “demi-simple” is represented in the source by the written fraction `1/2`. **Search:** `semi-simple|left-inverse|motives|monomorphism|inverse` in CT/CN. **Bears on:** RS **WG2 §2.3 #7**, **WG2 §2.4 #3**, **MPL_14_087-132 M23**.

CT **16/048–049** first treats algebraicity of inverses to algebraic isomorphisms and then explicitly says that extending this to monomorphisms seems to need the Hodge index relation; **16/049** calls the complete “yoga” a semisimple category of motives. T12’s semisimple category and decomposition language **restate/use** that goal, while T12 **12/003**’s hyperplane reduction is related to CT **16/045–046**’s algebraic left inverse to restriction. CN **S13–S16** already develops the conditional positivity/splitting/numerical-motive discussion, so the new contribution is the location of the categorical assertions in cote 12, not a new proof of those earlier calculations. In particular, a later theorem about numerical motives cannot, without an equivalence comparison, certify all the homological realization assertions in T12.

### CC03 — The central weight cocharacter obstructs the proposed literal SL₂ inclusion

**Kind:** own idea / comparison, **confidence high** for the incompatibility of the two stated actions, since centrality makes conjugation on the Lie algebra trivial. **Witness:** 12/015–016; CT 16/014–018. **Quote:** “l'hom … est central”; “poids 2”; `epsilon(gamma(lambda))=lambda^2`. **Search:** `graduation|central|Lefschetz|Phi|sl` in T12, CT, CN and RS. **Bears on:** RS **WG2 §2.3 #2**, **WG2 §2.4 #3**, **MPL_14_087-132 M04**, **MPL_15_087-138 L07** and **§111**.

T12 **12/015** makes the canonical motivic grading a central cocharacter, while CT **16/014–018** has a correspondence operator `L` of degree two, so this **differs from** a nontrivial Lefschetz SL₂ inside that same motivic group with that same weight cocharacter as its diagonal torus. On a graded realization the degree-two operator satisfies `gamma(t)L gamma(t)^(-1)=t^2 L`, whereas an element of the Lie algebra of the motivic group would be fixed under conjugation by a central gamma; the Tate-corrected correspondence is instead a morphism between appropriately twisted motives. RS **M04** and **§111** already report a projective-line obstruction, and that computation should be cited as an earlier unreviewed lead, not rederived or claimed here as new. This answer does not exclude other SL₂ morphisms in other automorphism or correspondence settings, including the distinct published morphism mentioned by RS **L07**.

### CC04 — Even the phrase “the sl₂ of cote 16” has a normalization qualification

**Kind:** reading question. **Witness:** CT 16/014–017, compared with 12/015. **Quote:** “sur Z !”; “condition essentielle !”; “Il faut donc se donner en même temps L et les pi_i”. **Search:** `normal|integral|contraction|sl₂|unit-shift` in CN, especially **S2–S5**. **Bears on:** RS **WG2 §2.3 #2**, **WG2 §2.4 #3**.

CN **S2–S5** warns that the literal exterior-algebra contraction on an integral lattice and the unit-step lowering/matrix-unit model are not automatically identical; its matrix-algebra calculation is conditional on a stated normalization. T12’s central grading **adds a further distinction** between the grading on cohomology and the shifted Lefschetz grading, rather than resolving that integral issue. CT **16/017** itself rejects uniqueness from `L` alone and insists on the degree projectors, so neither forgetting the grading nor importing a normalized SL₂ without specifying it is supported by the manuscript. The RS description of `Phi tensor Q` should therefore remain a credited planning interpretation with the normalization explicitly stated.

### CC05 — Safe dictionary of standard-conjecture lettering

**Kind:** reading question. **Witness:** 12/004 (“conjectures standards” with a spelling doubt), compared with CT 16/040, 042, 044–050. **Search:** `A(X)|B(X)|C(X)|D(X)|index|inverse|projectors` in CT/CN. **Bears on:** RS **WG2 §2.4 #3**, **MPL_14_087-132 M01**.

The selected cote 12 leaves name standard conjectures but do **not** define their A–D lettering, so they **do not add** a complete dictionary to the earlier packet. CT **16/040, 042, 045–048** identifies its draft `C` operationally by algebraicity of Lefschetz inverse/lowering operators, which CN **S1** compares with published **B**; draft `A`’s algebraic-class Lefschetz content corresponds to published **A**. CN **S1** explicitly leaves draft **B** and **D** without secure standalone definitions in the supplied text, and the inferences from CT **16/044**’s `A + index implies B` or **16/048**’s rational-characteristic-polynomial consequence do not by themselves prove a full permutation. RS **MPL_14_087-132 M01** points to a notation table on **14/117**, but that table itself is absent and must be treated as a retrieval lead.

| Printed label in CN S1’s comparison | Content | Safe manuscript comparison |
|---|---|---|
| A | Lefschetz statement on algebraic classes | Draft A is compatible with this; CT 16/044–047, 050 |
| B | Algebraicity of the Lefschetz lowering/inverse operator | Draft C; CT 16/040, 042, 045–048 |
| C | Algebraic Künneth projectors | Must not be conflated with draft C |
| D | Homological equivalence equals numerical equivalence | No secure draft B/D assignment from supplied text alone |
| I | Positivity on primitive algebraic classes | Compare the actual pairing/sign, CT 16/044–045, 049 |

**Verification limit:** The printed-letter meanings above were found in CN S1, which cites Grothendieck (1969), §§2–3, and Kleiman (1968), §3; this child task did not independently reopen those publications. The parent should verify a primary source if using the printed dictionary as an external factual claim.

### CC06 — Singular hypersurfaces: explicit programme in 16, no evidence here that 14 carries it out

**Kind:** unpursued implication / scope limit. **Witness:** 12/023–029 and 12/042; CT 16/047. **Quote:** CT “one will have to work also with singular ones”; T12 “À tout préschéma noeth”; “Attention … infinis”. **Search:** `singular|hypersurface|Serre|simply connected|14` in CT/CN/RS. **Bears on:** RS **WG2 §2.4 #3**, **WG2 §3.2 #7**.

CT **16/047** explicitly abandons the proposed smooth-hypersurface reduction after Serre’s simple-connectedness objection and asks for standard conjectures reformulated on singular varieties; CN’s notes at that scan treat this as a programme without a chosen replacement formalism. T12 **12/023–029** **adds** a proposed motivic formalism for general noetherian bases with derived operations, but **12/042** still insists on projectivity in the coniveau comparison and does not give the requested singular-hypersurface reduction. No full cote 14 source is attached, and the RS excerpts mentioning **14/002–044**, **14/092**, and **14/117** do not state that the programme of **16/047** is carried out. The defensible answer is therefore **not established by this packet**, not a historical assertion that cote 14 contains no such work.

### CC07 — Rational traces supply a direct link to the earlier inverse argument

**Kind:** unpursued implication. **Witness:** 12/030–031; CT 16/048–049. **Quote:** T12 “polynômes caractéristiques”; “à inclure dans le formalisme tensoriel”. **Search:** `characteristic polynomial|Hamilton|rational|Tr|contraction` in CT/CN. **Bears on:** RS **WG2 §2.4 #3**, **WG2 §2.3 #7**.

CT **16/048–049** uses rational characteristic-polynomial coefficients in a Cayley–Hamilton argument making an inverse correspondence algebraic, while T12 **12/030–031** **adds** a tensor-categorical route to rational, realization-independent traces and characteristic polynomials. The source reduces traces to contraction and `End(1_X)=Q` for connected `X`, and explicitly asks that contraction be built into the tensor formalism. CN **S11** already checks the conditional polynomial inversion, so these pages identify a proposed source of its rationality premise rather than provide a new inversion proof. This does not make every displayed coefficient or every derived operation unconditional.

### CC08 — Polarization is stronger than the written complex-conjugacy condition

**Kind:** unpursued implication. **Witness:** 12/016–019; CT 44/002, 008–009. **Quote:** T12 “les deux graduations de Hodge sont conjuguées complexes”; “Structures de positivité”; CT “A prouver que cette dernière est positive !”. **Search:** `polarisation|positive|Hodge|conjugu|symmetric` in T12, CT and CN. **Bears on:** RS **WG H9**, **WG2 §2.3 #12**, **MPL_15_195-228+18_002-017 B03**, **MPL_14_002-044 A36**, **MPL_60_002-035 F21–F22**.

T12 **12/016** supplies conjugacy of the two Hodge gradings, and **12/017–018** works with polarizable Hodge structures, but **12/019** ends with only the heading “Structures de positivité”; the selected range does not supply a positive form from a real structure alone. This **differs from** and should be compared with CT **44/008–009**, where the symmetric self-duality of an intermediate Jacobian is separated explicitly from the still-unproved positivity/ample-polarization assertion, with a margin requiring primitive decomposition. CT **44/002**, Theorem 4, is a programme statement and its “Connu tel quel” annotation does not remove the narrower uncertainty expressed in the dated letter. RS **B03** already makes the polarization/real-section distinction, while **F21–F22** flags parity/sign issues; no equivalence between positivity and anabelian real-section reconstruction is established here.

### CC09 — Semisimplicity is not triviality of centres

**Kind:** own idea / scope clarification, **confidence high** because the source itself provides central nontrivial structures. **Witness:** 12/005, 012–016. **Quote:** “si K de car. nulle”; “central”; `epsilon(gamma(lambda))=lambda^2`. **Search:** `réductif|centre|central|trivial centre` in T12/CT/RS. **Bears on:** RS **WG2 §2.3 #7**, **LM4_SUCCESSOR B.29–B.51** (headline constraints, unreviewed here).

T12 **12/005** relates semisimplicity to reductivity in characteristic zero, while **12/012–013** puts Frobenius in a centre and **12/015–016** supplies a central weight cocharacter with nontrivial Tate character. These pages therefore **differ from** a claim of trivial centre: the pairing with the profinite centre-free statements in RS is an analogy between structural restrictions, not a formal equivalence. CT **16/049** and CN **S13–S16** concern radical/semisimplicity arguments and do not imply centre-freeness either. The contribution to the requested linear/nonlinear table should retain this explicit failure of a naive translation.

## Bounded negative findings and query record

I searched the supplied CT and CN for `sl`, `sl₂`, `Lefschetz`, `lefschetzien`, `Phi`, `graduation`, `central`, `motif`, `semi-simple`, `conjecture`, `A(X)`, `B(X)`, `C(X)`, `D(X)`, `index`, `polarisation`, `singular`, `hypersurface`, `Serre`, and `period`; exact source scan boundaries were recovered from CT’s `cotefile` and `scanpage` markers. The decisive correspondence-ring definition is **16/018**, the algebraic-inverse/semisimplicity bridge is **16/048–050**, and the singular-hypersurface programme is **16/047**. The supplied evidence does not contain the actual **14/117** notation table; the only access to it is RS’s **MPL_14_087-132 M01** excerpt. No claim in this report imports a missing referenced return or treats the filenames listed in RS as files actually read.
