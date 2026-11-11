# Part D: arithmetic, inertia, sections, and source audit

## Scope and principal conclusions

Part D supplies 23 numbered statements. The distinction between `Known`, `Proved`, `Refuted`, and `Open` is literal: a proved implication whose antecedent is a new unverified claim is not recorded as an unconditional theorem. `Open; claimed` for proof packs 019 and 031 records the limit of this independent audit, rather than claiming to disprove the preprints or to establish that no expert verification exists. All arithmetic groups in the main assertions are full profinite étale groups. The geometric pro-p variant of the relative Hom theorem retains the full arithmetic quotient.

The literal inertia-normalizer assertion in §34 is false. The whole geometric fundamental group already has an arithmetic normalizer projecting onto the Galois group, and a proper characteristic nonprocyclic subgroup gives a second counterexample. Rational-point section images furnish a further obstruction if one allows arithmetic instead of geometric subgroups. Nakamura's actual recognition theorem adds the cyclotomic conjugation law. This law must not be silently removed.

The relative open Hom theorem is established, and its Isom consequence proves the proposed equivalence between *geometrically admissible* effective lifts and rational points. It does not prove that all sections are admissible. A complete tangential-section example on the rational tripod refutes unrestricted affine section surjectivity onto interior points.

For absolute open Hom, the source's geometric kernel does map into the target's geometric kernel unconditionally. Its image in the open target Galois subgroup is topologically finitely generated, closed, and normal, and Mochizuki's published Theorem 2.4 makes it trivial. Thus 031 is needed only to reconstruct an embedding of the base fields from the resulting open Galois homomorphism. The relative Hom theorem then finishes a rigorous conditional reduction. The exact conjugacy ambiguity is all target inner conjugacy in the absolute formulation, versus geometric inner conjugacy with a specified map to the same arithmetic quotient.

Faithfulness is known for every hyperbolic curve over a number field or p-adic local field, including proper curves. Hoshi–Mochizuki Corollary 6.4 proves the stronger statement needed for the revised arithmetic-image Teichmüller quotient, while Corollary 6.5 separates injectivity of total universal monodromy from the geometric congruence problem. Part D proves the finite-field-of-definition and ordered/unordered deductions explicitly. The quotient is by the orientation-preserving geometric image. Replacing it by an extended mapping-class group kills complex conjugation and may destroy normality, so it is a different assertion.

## Audit of proof pack 019

**Source read.** The complete main text *The p-adic section conjecture*, dated October 6, 2026, was read, including the new analytic and stable-model arguments and the deductions in Sections 7–8. The companion *Étale covers with a prescribed exterior sheet* was inspected for its statement and role but its complete proof was not independently audited. It is not used as an established theorem here. No Lean statement is needed, and no claim is made that a Lean file certifies the geometric argument. Corollary 8.4's additional arithmetic input is deliberately not used.

**Exact new bottleneck.** Theorem 1.2 is a statement about a specified embedding into a specified valued completion: the separable function-field extension must lie in the completion of the proper étale tower inside the chosen completion of the separable closure. An abstract field embedding is insufficient for the subsequent decomposition-group identification. The all-sheet formulation is also necessary. A local analytic lift on one selected sheet does not automatically give the asserted inclusion of the full algebraic extension.

**External inputs checked in primary sources.** Amini–Baker–Brugallé–Rabinoff, Theorem 7.7, was checked with the definitions of tame coverings and marked branch points. Mochizuki–Tsujimura, Theorem A and Proposition 2.4(iv), was checked in the opened RIMS 1974 version of June 16, 2023; the 019 bibliography calls its revision 2024, and that version distinction is retained. Baker–Rabinoff, Proposition 6.1 and Corollary 6.6, was checked together with the period-pairing discussion. These statements supply specific model, covering, and divisor-lifting tools. They do not automatically combine into the simultaneous analytic approximation assertion of 019.

**Proof components tested.** The model domination step, graph-bridge case, need to retain exterior sheets, normality used at the final extension step, compatibility of marked branch loci, and dependence on the fixed valuation were followed. The toric/annular root constructions and their interaction with stable-model refinements require uniform choices across the sheets and all relevant finite extensions. This audit has not independently established that uniform construction in the complete generality of Proposition 5.2 and the resulting Theorem 1.2. No explicit counterexample or decisive erroneous line was found. Consequently D.7 remains `Open; claimed`, with the precise assertion and the remaining verification task stated.

**What is proved conditionally.** D.8 gives a complete proof from the specified-embedding completion assertion to the proper local section theorem. It checks the passage from completions to decomposition groups and uses the exact statements of Koenigsmann's Proposition 2.4(2) and Pop–Stix's Theorem 26. The rank-one exclusion is reproduced using two inequivalent henselian valuations and the elements

\[
q_r=d+(1-d)\frac{z^r}{1+z^r},\qquad z=p^N/t.
\]

The valuations make this element a square at one henselian valuation and force the nonsquare constant class at the other. The quantitative Hensel threshold explicitly includes residue characteristic 2. Rank two, the horizontal coarsening, rational residue degree, and triviality of horizontal inertia in a proper étale tower are then treated separately. Injectivity is justified by the Jacobian Kummer map and the vanishing of the intersection of all integer multiples in the compact p-adic group.

D.9 proves the exact conditional global statement through Harari–Stix's Theorem 2.1 and Remark 2.2(1), in the February 11, 2011 primary preprint numbering. Modified adeles retain real connected components and omit complex places. The real section theorem is checked in Bresciani–Vistoli's primary note. Stoll's 2017 erratum is incorporated, including disconnected torsors and the treatment of real places. This argument identifies localized global sections with the finite-cover descent set; it does not show that this set is always the rational diagonal.

**Modular consequence.** D.10 combines the conditional local theorem with Stoll's Corollary 8.8, its erratum, Stix's finite-support Corollary 5, and Mazur's Introduction Theorem (7), page 35. When the compactification X_1(N) has genus at least two, a section of Y_1(N) compactifies to the section of a unique rational cusp. This is the precise consequence available for an N_{1,1} moduli section provided its image is contained in the open modular subgroup over G_Q itself. Restricting an arbitrary section to an open G_L only yields a section over L; the cited rational-point theorem over Q cannot automatically be applied over L. Compactified cuspidality does not prove the original affine section is a cuspidal section, and it does not prove that moduli sections do not exist. Tangential sections at rational cusps show why the distinction matters.

## Audit of proof pack 031

**Source read.** The complete October 5, 2026 main text, Sections 1–6, including each new lemma and proposition used in Theorem 1.1, was read. The proof was examined as a chain of arithmetic separation arguments rather than accepted from its abstract. No Lean formalization is used.

**External inputs checked.** Uchida's 1979 isomorphism theorem and Lemma 3 were opened in the primary four-page paper. Uchida's 1981 paper was opened in its entirety, including the local three-case alternative, Proposition 1, Proposition 2, Theorem 1 for source field Q, and Theorem 2 under its local condition. Hoshi's Theorem 3.4 was checked in the revised primary preprint, and its published 2025 metadata was verified. Its hypothesis of compatibility with cyclotomic characters is retained. The cited conjecture and the later known partial theorems must not be conflated.

**New arguments examined.** The zero estimate in Lemma 3.1, determinant bounds, and the numerical condition exceeding n(n−1) were followed. Proposition 3.2's passage from vanishing on infinitely many degree-one primes to vanishing of additive characters was tested against its Frobenius averaging and corestriction requirements. The construction of equivariant projections, regular-module components, and normalizer-kernel separation in Proposition 4.3 was followed. Proposition 5.3's uniform bound 2[K:Q]+2 depends on the multiplicity of one character in the relevant S-unit module, rather than a bound by the total extension degree. The Kummer prime choices and valuation independence in Lemma 5.4 and the final compactness argument producing a single conjugator were checked. No Leopoldt conjecture was silently inserted.

The generality and uniformity of the new zero/separation estimates are not independently established by this audit. Reading and tracing these arguments is evidence about their structure, not a substitute for reproducing the new arithmetic lemma in all its cases. No explicit contradiction, counterexample, or fatal gap was found. D.13 therefore records the unrestricted theorem as `Open; claimed` and identifies the exact remaining verification work. D.12 gives the complete implication from that theorem to absolute open Hom for number-field hyperbolic curves. D.11, which supplies geometric-kernel preservation, is unconditional and uses an earlier published theorem.

## Exact theorem numbering and version issues

| Source | Exact statement used | Version note |
|---|---|---|
| Nakamura (1994) | Theorem (2.1.1); Lemma (2.1.2); Corollaries (1.3.3)–(1.3.4) | Attached published text |
| Mochizuki (1999) | Theorem A = Theorem 16.5 plus following Remark; Theorem C = Theorem 19.1 | Attached published text |
| Mochizuki (2006) | Theorem 2.4; Corollary 2.2; Lemma 3.2; Proposition 3.3; Theorem 3.1 | Published journal numbering. Author PDF labels them 1.5, 1.3, 2.2, 2.4, 2.1. Journal PDF prints pages 57–71; repository metadata lists 57–72. |
| Hoshi–Mochizuki (2011) | Corollary 6.3(i), Corollary 6.4, Corollary 6.5 | Attached PDF pages 64–67 |
| Matsumoto (1996) | Theorem 2.1 and its Conjecture 2.1, printed page 191 | Actual primary scan inspected; the theorem proves the affine number-field case |
| Belyi (1980 English translation) | Theorem 4, page 255; unnumbered corollary, page 256 | Original Russian publication 1979 |
| Boggi–Zalesskii (2019) | Proposition 3.6 | Full pro-S group; nonzero profinite exponents; algebraically simple generators |
| Harari–Stix (2012 publication) | Theorem 2.1; Remark 2.2(1) | Numbering of opened February 11, 2011 author preprint |
| Pop–Stix (2017 publication) | Theorem 26; Section 6.1 | Numbering of opened August 11, 2011 author preprint |
| Stix (2015 publication) | Corollary 5 | Opened February 27, 2014 preprint |
| Stoll (2007) | Corollary 8.8 | Used with March 29, 2017 erratum |
| Mazur (1977) | Introduction Theorem (7), page 35 | Distinguished from (7′) and the complete torsion classification in (8) |

Every bibliography entry in D's fragment is marked `verified` or, where needed, described as a verified source with an unverified new proof. Source verification means that the relevant primary text was opened; it does not turn an unrefereed argument into an established theorem. The shared Boggi–Zalesskii bibliography key is supplied by Parts B–C.

## Manuscript and computational audit

The scans actually inspected are 483, 485, 496, 500, 501, 504, and 505. Readings are recorded separately in `D_readings.json`; doubtful typography is not silently resolved. In particular, the normalizer claim cannot be repaired by choosing Γ versus Γ+, and the folio245/246 discrepancy is retained. The endomorphism-versus-automorphism phrase on scan501 does not affect the rank-one calculation: the weaker endomorphism hypothesis suffices.

`code/d_counterexamples.py` is executable using the Python standard library. Its recorded output checks generation and perfectness of A5, the small finite normalizer model, the discriminant and derived-group data used for an S3 Galois quotient, and the abelian centralizer of the CM matrix modulo 2,3,4,5,8,9. The profinite conclusions are proved in D.2 and D.20; no finite computation is presented as a proof of an unbounded inverse-limit assertion.

The small nonhyperbolic types (0,0), (0,1), (0,2), and (1,0) are handled explicitly. The hyperbolic types (0,3) and (1,1) share the abstract geometric group Fhat2 but have different inertia systems. Real sections are indexed by connected components, and real Galois groups are not slim. Nonorientable topological quotients are distinguished from geometric complex-curve groups. None of the stated characteristic-zero Hom, proper local conditional, faithfulness, or simple-loop centralizer results excludes p=2 or p=3. The modular stack's 2- and 3-isotropy is retained rather than discarded via a coarse space.
