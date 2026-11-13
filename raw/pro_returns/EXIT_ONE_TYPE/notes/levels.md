# Part 5 and Lead 6: proofs, sources and checks

The section has eleven numbered results: P5a1–P5a3, P5b1–P5b4, P5c1–P5c4.
Each is proved or explicitly refuted; no theorem silently repairs a manuscript reading.

## Scope

- The depth-two bicategorical groupoid diagram in (246) gives Z4 for the coordinate divisor in C3; depth-three flag triangles give Z3. A strict group colimit is a different construction.
- The sharp uniform cutoff is r≥k+2. L_{≤r}→L is (r−1)-connected. General étale Čech descent includes infinite discrete isotropy.
- The normal boundary is used for nonproper pairs. For C² with an axis, normal L≃S1 while the global end of C*×C has cross-section S1×S2. Proper Mbar0,n provides the stable collars needed in the independent tests.
- P5a3 requires no asphericity: Pi1 is a left adjoint and preserves the coherent colimit. The corrected target under the end-equivalence hypothesis is X star.
- Every genus has the infinite-multicurve homotopy-fibre formula; the empty multicurve is included for k≥d and gives contractibility. Borel constructions retain every stabilizer.
- Genus zero has (k−1)-connectivity for all k. Every stable genus has P0 nonempty, P1 connected and P2 simply connected, proved by residual-complexity joins and infinite rank deletion.
- The unrestricted higher-genus extrapolation is false at (g,n,k)=(2,1,3): its fibre is a nontrivial wedge of S2.
- The explicit groups are Gamma05=F3 semidirect F2 and Gamma06=F4 semidirect Gamma05. The selected kernel basis uses the mirrored Artin action.
- The finite aspherical models have counts(1,5,6) and(1,9,26,24). The24 first identities freely generate the presentation pi2 module by universal-cover exactness. Product models have12 and8 complete identities. These are not identified with pi2 of the full geometric boundary tube.
- Four elementary supports are04,11,05,12. Pointwise-fixed boundary circles are distinguished from punctures. No profinite/Galois extrapolation is asserted.

## Reproducible computations

levels_colimit.py computes nonabelian presentations and valid Tietze moves, plus exact simplex-boundary homology.
levels_braids.py verifies26 braid equalities through the faithful Artin representation and24 action compatibilities.
levels_stein.py verifies every Levi principal minor and the14/93 determinant monomial counts.
levels_syzygies.js and its Python implementation materialize all44 first identities as signed products of conjugates of relators.

Gamma06 conjugate-factor counts:
[36,64,16,26,366,640,168,144,92,178,44,52,18,42,36,12,8,36,16,26,10,92,44,52].
Maximum conjugator length171.
Gamma05×F2 counts[8,8,14,14,10,10,6,6,8,8,10,10], maximum length11.
F2³ has eight identities of six factors each, maximum length4.
Finite checks verify identities; asphericity proves completeness. Finite coarse boundary-complex homology is not used to certify the infinite fibre.

## Verified primary sources

Harer1988 full text: https://imag.umontpellier.fr/~calaque/GdT-CGEMC-Harer.pdf.
Checked Chapter1 Theorem1.1, Chapter3 Lemma3.6, Chapter4 Theorem4.1 and Corollary4.2.
Reopened web sources turn99view0, turn100view0.

Björner–Wachs–Welker2009 author manuscript:
https://www.math.miami.edu/~wachs/papers/scm.pdf.
Corollary4.4 and its finite-poset scope checked; infinite case proved directly.
Reopened turn106view1, turn108view1.

Fadell–Neuwirth1962: https://ncatlab.org/nlab/files/FadellNeuwirth-ConfigSpaces.pdf.
Theorem1 on page111 visually checked. OCR's date1982 and fibre subscript are erroneous; the scan says1962 and F_(m+1,n−1).

Shpilrain2001: https://arxiv.org/abs/math/0203167.
Full PDF TheoremA, representation(1), parameter1 checked. The2002 arXiv posting records2001 journal publication. Metadata reopened turn108view0.

Milnor1963: https://luis.impa.br/aulas/topdif/Milnor_MorseTheory.pdf.
Theorems3.2,3.5, Remark3.3, Theorem7.2 and reverse-index proof of Theorem7.4 checked.
Reopened turn107view0, turn107view1.

Hatcher–Lochak–Schneps2000: https://webusers.imj-prg.fr/~pierre.lochak/textes/crelle.pdf.
Published scan Section2 Theorem2 and Remark4 on page9 visually inspected; numbering is not taken from a recalled preprint. Reopened turn106view2.

Do not bundle copyrighted source PDFs.

## Manuscript readings and audits

The official `build/sources/147.pdf` was directly rendered and visually
rechecked in the current restored workspace at PDF pages60,151,152, with
enlarged regions and a rotated rendering of the marginal note. Adjacent
pages150 and154 were also inspected solely to resolve pagination.
The seven reading rows now distinguish direct observation, inferred
continuation numbering, and unresolved lexical readings.

**Pagination correction:** PDF page60 has printed footer59 and visible
handwritten folio29. PDF page150/footer149 visibly has folio74;
page151/footer150 is its unnumbered continuation. PDF page152/footer151,
containing equations(246) and(247), visibly has folio75, not76.
PDF page154/footer153 visibly has folio76. The earlier metadata's
75-continuation/76 for PDF151/152 was one folio too high. The enlarged
folio75 reading is supported by both neighboring numbered leaves.
This corrects locations, not mathematical statements.

On PDF page152, equation(246) displays the two-depth span with
Pi-tilde_(2,1) mapping to Pi-tilde_1 and Pi-tilde_2. The overwritten
left object retains the star-infinity superscript and its normal-tube
identification. The margin visibly discusses Pi-tilde_i for i>=3 and
draws the Pi-tilde_(3,2,1) to Pi-tilde_(3,1),Pi-tilde_(3,2) flag data.
The partly overlaid phrase previously read as `2-fleches` is kept
cautious; the full adjoining sentence is not claimed as a secure
transcription. In equation(247) the left side visibly reads Pi1 X
without a star, whereas the preceding hypothesis has
X^(star infinity) to X^star. The correction to Pi1(X^star) is therefore
kept separate from the literal reading.

The purity paragraph visibly invokes a purity-type argument and
neglecting Theta^(3). The earlier short reading `pour nous` remains
uncertain. The earlier proposed verb `represente / reconstitue` could
not be securely located on this fresh visual check and must not be
quoted as verified; the nearby instruction to replace X by
X minus Theta^(3) is visible. None of the proofs depends on resolving
those words.

On PDF page151, the lower Corollaire2 draft is visibly cancelled by
large crossing strokes; its bottom-right bound reads 1<=d_0<=3. It is
treated as a deleted draft. On PDF page60, equation(75) identifies
04 and11, and the following sentence names05 and12 as the new cases
of(74); the ensuing paragraph explicitly discusses four elementary
cases in modular dimensions at most2. The adjacent tentative word
`multiplicites` is not promoted to a confident reading.

The supplied Part1 transporter, toric and product-curve formulas passed the algebraic audit. Right source-twist cosets compose as [h]∘[g]=[hg] because g⁻¹Delta_target g is contained in Delta_source.
The stronger adjacent-inertia counterexample has all strata aspherical but full-lattice primitive kernel(1,−1).

The surface core/common-corner argument was reviewed within proper algebraic/bimeromorphic scope. The normal-torus transgression converse and the profinite restriction to recursively compatible towers were communicated and repaired.
The Mori-hyperbolicity push-off requires radius decay faster than every new boundary coordinate. The local Picard extension through finite/Kummer covers was checked for hyperbolic curve factors, not C*.

## Final recovery execution

All five programs (four Python and one Node JavaScript) executed successfully in the restored workspace. The complete expanded JSON from the Python and JavaScript implementations agrees exactly. All eleven TeX result labels match the eleven results-register rows.
