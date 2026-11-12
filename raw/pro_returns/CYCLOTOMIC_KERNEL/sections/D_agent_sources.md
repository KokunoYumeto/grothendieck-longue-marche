# Source and computation record: D(c)–(e), local contribution to E(d)

Prepared for the combined research paper by the cyclotomic-coverings workstream. This record describes opened sources and actual computations; it claims no priority. The mathematical contributions are in `sections/D_agent.tex` (D1–D13) and `sections/E_local_agent.tex` (D14–D15). The bibliographic entries are in `sections/D_agent_refs.bib`; every entry is marked **Verified** there. The shared Nakamura entry is maintained by the inertia workstream.

## Outcome and scope

| Requested part | Delivered result | Remaining task |
|---|---|---|
| D(c), abelianization | D1 gives the exact equal-class pairs, including the proof that a distinct pair forces a split genus-zero boundary. | None for the stated cyclotomic base. |
| D(c), explicit pair | D3 proves equality of the fibre Galois sets for every prescribed two-step cover; 7,800 exact finite checks were run. D4 supplies a degree-81 finite étale cover separating the full sections. | None for this pair. |
| D(c), all hyperbolic curves | D2 proves full point-section injectivity over every finite extension of the cyclotomic base and every finitely generated extension. | Section surjectivity is not part of this injectivity result. |
| D(d), Theorem 1 | D8, using B12, proves the open-subgroup centralizer assertion in the full stated field generality. | None in that assertion. |
| D(d), Theorem 2 | D6 proves faithfulness for morphisms of fields over the specified cyclotomic base. | No claim about unrelated actions on the coefficient field is substituted. |
| D(d), Theorem 3 | D7 refutes the cyclotomic extension by the points 1 and ζ6 of Gm; D1, D2 give the precise replacements for curves. | None for this refutation. |
| D(d), Proposition 54 and precisions | D9 transfers the hyperbolic packet and centralizer statements and retains the type (0,2) counterexample. | No exhaustion of all sections is inferred. |
| D(d), Conjecture A | D5 refutes the proposed extension by the proper genus-four curve t⁶+2y³+4=0. It has no cyclotomic rational point and has a continuous section, with section existence proved. | None for this refutation. |
| D(e) | D10 proves common finite covers and canonical functorial completion; D11 proves continuous descent with the exact finite-extension quantifiers; D12 describes automorphisms for proper curves. | **Unfinished:** no construction or exclusion of a discontinuous number-field action normalizing no finite-level deck group; no affine commensurator-completion theorem proved. D13 gives the exact cocycle problem for U03. |
| E(d) | D14 computes the entire maximal prime-to-p fixed group for good marked reduction, integral points avoiding the boundary, integral tangent sections and all their cuspidal twists. | **Unfinished:** the full group even in the specified U03/Q5 example, and both groups for the specified bad-marked-reduction example. D15 proves the exact nonabelian H¹ lifting obstruction. |

D13 and D15 have status `Open` in the machine-readable result ledger and explicit partly-settled/unfinished headings in the paper. These statuses record the work left in this response; they do not assert a literature-wide impossibility result.

## Primary sources opened and used

### Tsujimura: AVKF and cyclotomic fields

**Verified.** Shota Tsujimura, *Birational anabelian Grothendieck conjecture for curves over arbitrary cyclotomic extension fields of number fields*, Advances in Mathematics 435 (2023), article 109380, DOI `10.1016/j.aim.2023.109380`. The opened primary text was the author preprint RIMS-1957 of 24 February 2022:

<https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1957.pdf>

The paper uses the numbering of this opened text and says so in the bibliography.

- Proposition 1.2(ii): a finitely generated extension of an AVKF field is AVKF.
- Proposition 4.2: for a hyperbolic curve over an AVKF field of characteristic zero, its geometric points are separated by germs of the point-defined sections; its stated bijection has the subset of point-defined germs as target.
- Theorem 4.7 was also read to check scope. It assumes TKND–AVKF in characteristic zero and an additional surjection from the multiplicative group to Z in its birational reconstruction setting. That theorem was not used as a section-surjectivity assertion.

D2 supplies its own positive-genus covering and descent proof, and compares it with these statements. In particular, it does not turn the target of Proposition 4.2 into all section germs.

### Hoshi–Mochizuki–Tsujimura

**Verified.** Yuichiro Hoshi, Shinichi Mochizuki and Shota Tsujimura, *Combinatorial Construction of the Absolute Galois Group of the Field of Rational Numbers*, Journal of Mathematical Sciences, The University of Tokyo 32(1) (2025), 1–125:

<https://www.ms.u-tokyo.ac.jp/journal/32-1-1.pdf>

Both the downloaded author manuscript dated 29 July 2024 and the published text were opened. The following statements were checked in the published text:

- Definition 3.3(vi), the ISC condition: the point-defined geometric-conjugacy decomposition classes of every hyperbolic curve over every finite extension distinguish its rational points.
- Proposition 6.4, printed p.108: an AVKF subfield of Qbar satisfies ISC and the paper's CS condition.
- Proposition 6.3(i), printed p.103: the stated sparse Galois extensions of a number field's compositum with Qab satisfy its AVKF conclusions. Its exact sparsity hypothesis is retained; no arbitrary larger-extension inference is made.

Only Proposition 6.4 and Definition 3.3(vi) are needed in D2. Published bibliographic year and volume were checked rather than inferred from the author-manuscript date.

### Elliptic-curve arithmetic used for the degree-81 cover

**Verified.** James S. Milne, *Elliptic Curves*, second edition, World Scientific, 2021, author-hosted text:

<https://www.jmilne.org/math/Books/EC2.pdf>

- II, Proposition 6.3: prime-to-characteristic n-torsion is a rank-two Z/n-module.
- II, Proposition 6.4: the characteristic polynomial and determinant of an elliptic endomorphism on the Tate module, with determinant its degree.
- V, Proposition 8.1: the ℓ-adic torsion representation is unramified at good primes different from ℓ.
- V, Proposition 8.3: the Frobenius trace at such a prime is p+1−#E(Fp).

The text at II pp.70–71 and V pp.220–221 was opened. These statements are applied to Y²=X³−432, ℓ=3, p=7. The calculation #E(F7)=9 is independently enumerated. The commutator with complex conjugation fixes Q(μ∞) because cyclotomic extensions are abelian; the proof does **not** require an unverified invocation of Kronecker–Weber.

### The no-point curve and section-existence proof

**Verified.** Pete L. Clark, *Abelian points on algebraic curves*, arXiv `math/0604263`, version 1, 11 April 2006:

<https://arxiv.org/pdf/math/0604263>

Theorem 1: for p≡−1 modulo 3 and integers a,b,c prime to p, the diagonal cubic aX³+bpY³+cp²Z³=0 has no point over Qp^ab. D5 uses p=2, a=b=c=1 and reproduces the valuation obstruction directly in every Q(μN); the local abelian-field theorem is not a substitute for that comparison. The proper map from the genus-four curve is explicitly [t²:y:1].

**Verified.** James S. Milne, *Class Field Theory*, version 4.03, 6 August 2020:

<https://www.jmilne.org/math/CourseNotes/CFT.pdf>

- VII, Proposition 7.2: every Brauer class of a number field is split by a finite cyclic cyclotomic extension.
- VII, Lemma 7.3: the accompanying construction supplies a totally complex cyclic cyclotomic extension with specified divisibility of the local degrees at a prescribed finite set of places.
- III, Theorem 2.1: the local invariant identifies the nonarchimedean local Brauer group with Q/Z, with restriction multiplying invariants by the local extension degree.
- VIII, Theorem 4.2: the number-field Brauer local-global exact sequence, in particular injectivity into the sum of the local groups.
- II, Proposition 1.30: restriction followed by corestriction multiplies by the subgroup index.

D5 proves the required consequences instead of quoting a bare cohomological-dimension/projectivity assertion. Every Brauer class over a finite extension of Q(μ∞) descends to a number field, and the cyclotomic splitting extension is already contained in that larger field. The proof then establishes H² vanishing for every finite module by the pro-ℓ Sylow reduction and gives a finite Frattini-kernel argument solving the finite embedding problems. Recursive lifting through a countable cofinal characteristic system in the geometric curve group constructs a continuous section. This avoids invoking the freeness of the absolute Galois group of Qab or any section conjecture.

### Poincaré-cover automorphisms in the proper case

**Verified.** Amir Džambić and Gabino González-Diez, *Galois action on Fuchsian surface groups and their solenoids*, Forum Mathematicum 33(2) (2021), 375–395, DOI `10.1515/forum-2020-0148`; opened author text:

<https://arxiv.org/pdf/2006.02817>

- Theorem 7 identifies the holomorphic automorphism group of the inverse-limit solenoid with the Belyaev completion of the uniformizing lattice's commensurator.
- Proposition 3 gives the compact open profinite completion of the lattice, the deck-times-commensurator decomposition and the corresponding coset description.
- The hypothesis used throughout is a **compact** Riemann surface of genus at least two. D12 keeps that hypothesis. The construction around equations (11)–(14) was also read to identify the commensurator map on finite covers.
- The arithmeticity index criterion is explicitly recorded in the opened Introduction, p.3, and used in the discussion of Corollary 11: the commensurator has infinite index over the lattice in the arithmetic case and finite index otherwise. The original Margulis book was not separately opened; no invented Margulis theorem number is supplied.

D12 proves the comparison between the analytic inverse-limit object and the algebraic pro-curve through finite covers. Its use of the compact-surface theorem gives no proof of the affine case. That exact missing extension is retained in D13.

### SGA 1 and the algebraic comparisons

**Verified.** *Revêtements étales et groupe fondamental (SGA 1)*, recomposed and annotated edition, Documents Mathématiques 3, Société Mathématique de France, 2003, arXiv version 2 of 4 January 2004:

<https://arxiv.org/pdf/math/0206203>

The following statements and their surrounding hypotheses were opened:

- XII, Corollary 4.5: full faithfulness of analytification for proper complex schemes.
- XII, **Theorem 5.1**: Riemann existence, finite étale covers of a complex scheme locally of finite type versus finite analytic coverings. The theorem number was checked against the displayed statement. An earlier draft's `5.2` reference was corrected.
- XIII, Corollary 2.9: the local constancy and base-change result for the relevant prime-to-residue-characteristic torsors under smooth proper variation with relative normal-crossings boundary; this also supplies the characteristic-zero algebraically closed base-extension comparison used for finite covers.
- XIII, 2.10: specialization construction.
- XIII, Lemma 2.11: compatibility of specialization with the inertia groups at the boundary.
- XIII, 2.12 and its proof were read for context, especially the prime-to-p fundamental-group comparison.

For D14, the hypothesis is a smooth proper model with **finite étale boundary**. A point section is required to come from a point integral on the open model. A K-rational point reducing into the boundary is not silently covered by the unramified based-action argument. An integral tangent vector is required to have nonzero reduction. The proof then explicitly computes the effect of every completed Kummer twist.

**Verified.** The following Stacks Project statements were opened on 12 November 2026:

| Tag | Number in opened text | Exact use |
|---|---|---|
| [01YV](https://stacks.math.columbia.edu/tag/01YV) | Lemma 32.2.2 | Existence of inverse limits with affine transition maps. |
| [01ZB](https://stacks.math.columbia.edu/tag/01ZB) | Proposition 32.6.1(3) | Factorization of a morphism from a quasi-compact, quasi-separated affine-transition inverse limit to a locally finitely presented target; equality after refinement. |
| [05K0](https://stacks.math.columbia.edu/tag/05K0) | Lemma 37.43.3 | Zariski's main theorem for a quasi-finite separated map. |
| [0BY1](https://stacks.math.columbia.edu/tag/0BY1) | Theorem 53.2.6 | Equivalence between function fields in one variable and normal proper curves with nonconstant maps. |
| [0C0R](https://stacks.math.columbia.edu/tag/0C0R) | Theorem 58.30.3 | Prime-to-p specialization isomorphism for smooth proper curves. |

D10 proves the missing finiteness of the descended common-level map; it is not inferred merely from dominance. D11 identifies the function-stabilizer topology with the Krull topology on the arithmetic group and proves compactness of the section image directly.

### Local centralizers and the scope of Mochizuki's lemma

**Verified, shared primary text.** Hiroaki Nakamura (1994), the paper recorded under the shared key `Nakamura1994`. The text at §2.1, printed pp.94–97, was read from the supplied/extracted source `source_text/nakamura.txt`, and checked with the inertia workstream.

- The full class of finite groups is required to be closed under subgroups, quotients and extensions. All finite groups of order prime to p meet these hypotheses.
- Lemma (2.1.2): in a free pro-C group, the centralizer of a nonidentity element of a free-generator subgroup is that subgroup.
- Corollary (2.1.3) and the peripheral comparison give the needed separation of cusp inertia.
- The last paragraph of the proof of Lemma (2.1.4) handles a single cusp by passing to an unramified compact mod-ℓ homology cover of degree ℓ^(2g). Taking ℓ≠p stays inside the prime-to-p class and creates several cusps.

D14 therefore uses a theorem about the **maximal prime-to-p group itself**. It does not deduce that group's centralizer from the centralizers of the separate pro-ℓ quotients. The boundary-separation proof from A2 is also transferred with its comparison maps and the coefficient ring ∏ℓ≠p Zℓ.

**Verified, supplied primary PDF.** Shinichi Mochizuki, *The Absolute Anabelian Geometry of Hyperbolic Curves*, in *Galois Theory and Modular Forms*, Developments in Mathematics 11, Kluwer, 2004, 77–122. The supplied PDF is in `background/literature/mochizuki-absolute-anabelian/absolute_anabelian.pdf`; its extracted text is recorded below. Lemmas 1.3.7–1.3.9, author-manuscript pp.18–20, were opened.

- Lemma 1.3.7 treats the commensurable terminality of inertia in the indicated full and pro-ℓ groups.
- Lemma 1.3.8 identifies the arithmetic quotient group-theoretically.
- Lemma 1.3.9 starts from an isomorphism of arithmetic fundamental groups of hyperbolic curves over finite extensions of p_i-adic local fields and proves equality of types and preservation of cusp inertia, in full and pro-ℓ geometric groups.

D15 states this arithmetic-isomorphism hypothesis explicitly. The comparison with a specified section is the map q:π→π^(p′), giving q(π^Δ)⊆(π^(p′))^Δ and an H¹ obstruction for equality on each element. The paper does not claim that Lemma 1.3.9 computes these fixed subgroups. A request for the author's public PDF URL returned no usable text; the supplied PDF was the primary text actually used.

## Exact computations and what they prove

### `code/D_coverings.py`

The code uses rational polynomial arithmetic and exact finite enumeration. Its actual output is saved as `code/D_coverings_output.txt`.

1. It simplifies the two-step radicand comparison to the exact zero polynomial and checks all n,m from 1 to 12 and every ζ∈μn: **7,800** branch checks. It verifies the equivariant branch formula from D3. The general identity in the proof, not the finite range by itself, establishes the conclusion for all n,m.
2. It computes in Q[a]/(a⁶−a³+1), with a=ζ18. On Y²=X³−432 it gives 3P=(0,24a³−12), hence P has exact order 9.
3. For the nine points over ζ6, the orders of Q−P are `{1:1,3:8}`. For the nine points over ζ6⁻¹, every Q−P has exact order 9 and has triple 3P. All nine individual rows are printed.
4. It enumerates #E(F7)=9.
5. It verifies the matrix of multiplication by 3+6ω, its Smith form `(3,9)`, and its kernels modulo 9, 27 and 81. Each enumerated kernel has 27 elements and is killed by 9.

The matrix computations support the arithmetic proof that every F-rational 3-power torsion point is killed by 9. The separating conclusion uses that proof and the exact order-9 fibre differences: a point in the second degree-81 fibre would have order 27. The map from an actual arithmetic section to its permutation action on this finite étale fibre is stated in D4; a fixed-point-count discrepancy therefore disproves conjugacy of the full sections.

### `code/D_cyclotomic_counterexample.py`

The code checks the polynomial identity for the morphism to the diagonal cubic, computes gcd(t⁶+4,6t⁵)=1, checks the degree-three ramification calculation giving genus 4, and verifies the residue obstruction for powers of 2 modulo 3. Its saved output is `code/D_cyclotomic_counterexample_output.txt`.

The program is a finite certificate for these algebraic computations. The absence of points at every cyclotomic level and the existence of the continuous section are proved in D5; those infinite assertions are not inferred from a bounded search.

### Local calculations

D14 is proved by unramified pointed specialization, the exact Kummer valuation decomposition and the full-class inertia-centralizer theorem. It does not claim a finite computation of the wild kernel. The root workstream's Heisenberg computations check the relevant finite inner-conjugation formula; they do not settle D15's H¹ lifting classes. The full-group and bad-reduction tasks remain explicitly unfinished.

## Manuscript readings and page-number correction

The scans used for the cyclotomic claims are `scan062_a`, `scan062_b`, `scan063_a`, `scan063_b`, and `scan032_a`. These were visually inspected. The transcript at scan 22 was also checked to determine the groupoid-over-the-base hypothesis of Theorem 2. Earlier broad pages were read with the other workstreams' direct scan checks.

- **Scan 62 is manuscript p.30**, not p.61. The footer/archive count must not be used as manuscript pagination. All local TeX and ledger references were corrected.
- Scans 13–15 correspond to manuscript pp.6–7; scan 22 to p.10; scan 32 to p.15; scan 63 to p.31.
- The words “tous nos beaux énoncés” in scan 62 do not by themselves specify which assertions should survive. D5 and D7 give concrete mathematical refutations of the blanket reading, while D2 and D6–D9 list the assertions proved.
- Theorem 2 is a statement about the functor to groupoids **over the base groupoid**. D6 therefore names its F-linear field embeddings. The proof handles the inner ambiguity through its induced Kummer maps; it does not assume that unrelated coefficient-field embeddings agree.
- Theorem 3's principal assertion is sufficient for the Gm counterexample; no uncertain marginal word is used to manufacture its scope.
- Scan 63 explicitly discusses actions for which normalization of a finite-level profinite deck group is not assumed. D11 proves normalization only after the stated open-stabilizer hypothesis and passage to an open subgroup. D13 retains the unrestricted problem.
- The fixed-point notion used throughout D10–D13 is the inverse limit of the geometric points of the finite-level smooth proper completions. Counting the generic scheme point would change the assertion and is explicitly excluded by that definition.

No reading is declared settled solely by the mathematics. The global editorial ledger records the corresponding mathematical evidence.

## Searches and attempts that did not settle the remaining parts

For D(e), we examined the compact-surface solenoid/commensurator theorem and its finite-level construction, searched the commensurator and universal-cover literature, and proved the rational-function continuity descent directly. A tentative modular-translation idea over a cyclotomic field did not produce a checked number-field semilinear action and is **not** included as a theorem or counterexample. The remaining exact task is the abstract cocycle equation and non-normalization condition in D13, already for U03 over Qbar. The compact theorem's hypotheses do not establish the affine automorphism description.

For E(d), we proved the good-marked prime-to-p answer for points and every cusp twist and compared it with the full group through a genuine nonabelian cocycle. The attempted lift requires vanishing of each class `[h⁻¹σ(h)]` in H¹(Δ,ker q); no proof or computation for all these classes was obtained. The smallest retained good full-group case is U03/Q5 with point 2 or the unit tangent at 0. A concrete bad-marked case is P1 minus {0,1,5,∞} over Q5 with point 2; the boundary sections 0 and 5 meet in the special fibre. Neither its full nor its prime-to-5 fixed group has been computed here.

The supplied research notes, unreviewed transcriber arguments and first-pass manuscript transcription were treated as claims to test, not as theorem sources. In particular, abelianized equality of ζ6 and ζ6⁻¹ was not promoted to equality of full sections: D4 proves the opposite by a finite covering.

## Source files and hashes

Downloaded third-party source PDFs and extracted texts were moved **outside the deliverable package** to `source_text/D_sources/`. They are not redistributed in `code/`. Their SHA-256 records are in `sections/D_source_hashes.json`:

| Source file | SHA-256 |
|---|---|
| Clark2006.pdf | `5f004abba40394d2c98778516f33f417847106f5b884fb16bf7a070e10fd607c` |
| Clark2006.txt | `6e07e36f88572e551dfc52682cc1dd2be4b857a455cc8ef6002430926e909752` |
| HMT.pdf | `321fbfcc4d5bc9900aa6540b5618211b78cdfa72fa539915b069569f4dc053fe` |
| HMT.txt | `36d86a2bd9eb1eabee7116ff1be8ecbc37e9ad6ffaa78d9bb32bca6334214f28` |
| Mochizuki2004.txt | `3eece5e0ed787ca0056902805d7f4cdd23e5907299d3e22e0650955ddb86ecd9` |
| MurotaniOzeki2025.pdf | `ca42c45742442eb182dc44979673aae90eb083ed040f5eea427b830adba7ff13` |
| MurotaniOzeki2025.txt | `b9d4981ca61a0db28fbd71509c19ba1d0c757c42ff5dd8b9f740a0c3932580ab` |
| Tsujimura2022.pdf | `82ccc5e0c87bc36a1e41f09ab8084ee0c59ecd0176b2a14c9a56fe3c6b025342` |
| Tsujimura2022.txt | `9de148c529de72d6692ea5582e88ac5ce576a6ab0f9ce4d48c123b7998a3e9f7` |

Murotani–Ozeki was downloaded for the shared arithmetic-input workstream. Its theorem application and bibliographic record are owned by that workstream; D1–D15 do not cite it as a separate unchecked input. The Milne, Stacks, SGA and solenoid sources were opened through the web reader. A local Milne download was unavailable, but the relevant theorem text was available and read through that reader.

Independent D4 source check: Milne, Elliptic Curves, II, Proposition 6.7 was also opened and used for the faithful endomorphism action on the Tate module.
