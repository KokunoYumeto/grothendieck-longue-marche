# D.23–D.24: primary-source audit

All opens below were made on 14 November 2026. The argument uses D.6 and the checked local theorem D.19; it does not attribute that input to the papers below.

## Borne–Emsalem–Stix

**Opened:** *Lifting Galois sections along torsors*, primary arXiv:1301.4429v2, <https://arxiv.org/pdf/1301.4429>. Local PDF and text: `tmp/D_BorneEmsalemStix2015.pdf` and `.txt`. Full relevant passages: Definition2.1 p.3; Proposition3.1 p.5; Propositions3.4–3.5 pp.5–6; Proposition4.2 p.7; Proposition4.4 pp.8–9; Lemma4.5 p.9. Journal metadata: *Mathematische Nachrichten* 288(17–18) (2015), 1939–1951, DOI10.1002/mana.201400251.

The diagonal torsor is defined for a smooth curve. The exact homotopy sequence and extension-class statement explicitly require geometric connectedness, geometric unibranchness, characteristic zero and vanishing étale π2, all satisfied for the hyperbolic curve in D.23. The later proper-curve specialization does not restrict those general propositions. The main published theorem over Q imposes a torsion-packet condition; D.23 obtains a stronger conditional consequence because D.19 is a new input within this manuscript. It must not be presented as the published theorem.

Compatibility across disjoint divisors in D.23 follows directly from the displayed definition of F_D and from the exact kernel/quotient sequences. The older 28-page expanded primary preprint `tmp/D_BorneEmsalemStix2013.pdf` also contains that product comparison (Lemmas28–29), but the proof here does not need its older numbering.

## Brauer injectivity

**Opened:** Milne, *Class Field Theory*, v4.03, 6August2020, <https://www.jmilne.org/math/CourseNotes/CFT.pdf>, ChapterVIII Theorem4.2, printed p.241 (PDF p.249). This gives the exact Brauer–Hasse–Noether sequence. In D.23 it is applied separately to each fixed number field k(d), at each finite Kummer level. The transition maps on H1(E,μ_n) are surjective; no finiteness of H1(E,μ_n) is claimed.

## Exact Saïdi passage and scope

**Opened:** Saïdi, *Good Sections of Arithmetic Fundamental Groups*, arXiv:1010.1313v1, <https://arxiv.org/pdf/1010.1313>, proof of Theorem2.6(ii), pp.35–38. Local PDF/text: `tmp/D_Saidi2010.pdf` and `.txt`.

The permutation-module map on p.36 sends each upstairs inertia copy identically to its downstairs copy: it is the trace, hence induces the norm in Kummer H1. The surjectivity statement on p.37 when all residue fields are k-rational is correct. The unsupported assertion is that the map remains surjective after taking Gal(k_S/k)-invariants (pp.37–38), and the alternative statement that H1(G_k,M1)→H1(G_k,M2) is surjective (p.38). For Q(i)/Q the full Tate-module invariants under G_Q(i) vanish, so the source's inflation–restriction identifications are valid; the norm counterexample therefore addresses precisely the asserted invariant-surjectivity. The associated H2-injectivity claim also fails by the connecting class of3. D.24 refutes these general steps, not the existence of compatible sections and not any published theorem under additional hypotheses.

An independent group-theoretic defect appears later on p.38: an arbitrary nonsimple Galois cover cannot be assumed to be the fibre product of proper nontrivial Galois intermediates. For a cyclic degree4 cover there is only one such intermediate, of degree2; every fibre product of copies has connected components with function field equal to that degree2 field, so cannot recover the degree4 cover. Equivalently, the intersection of all proper nontrivial normal subgroups of C4 is its nontrivial subgroup C2. This note audits that sentence only and is not needed in D.24.

**Not opened:** the full published 2012 revision, *The cuspidalisation of sections of arithmetic fundamental groups*, *Advances in Mathematics* 230(4–6),1931–1954, DOI10.1016/j.aim.2012.04.002. The primary publisher abstract and metadata were opened, but the full-text request returned403. Its abstract has an additional finiteness hypothesis; no theorem from the inaccessible full text is invoked. The old v1 is deliberately identified as such.

**Opened:** Saïdi, *The cuspidalisation of sections of arithmetic fundamental groups II*, arXiv:1909.08318v1, <https://arxiv.org/pdf/1909.08318>, Definition2.3.3 and Lemma2.3.4 including proof, pp.14–15. Local PDF/text: `tmp/D_Saidi2019.pdf` and `.txt`. Its (HΣ) hypothesis is explicit: H1 for every finite module supported onΣ is finite. The proof then passes to an inverse limit of nonempty finite sets of splittings. Number-field Kummer groups violate this hypothesis for every nonemptyΣ.

## Residue certificate

`code/D_norm_compatibility_certificate.py` enumerates all nine pairs in F3² and verifies that a²+b²=0 only at(0,0). Together with the valuation argument in D.24, this proves that the Kummer class3 modulo squares is not a norm from Q(i). It also verifies that the two-coset trace modulo2 is surjective and invariant under the coset swap. The output is `audit/D_norm_compatibility_certificate.json`. The computation checks the elementary residue and module facts; no computational test substitutes for the cohomological proof.
