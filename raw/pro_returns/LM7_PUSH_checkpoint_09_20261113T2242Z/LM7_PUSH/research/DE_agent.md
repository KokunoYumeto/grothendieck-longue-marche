# Parts D/E: audit and results

| Task | Result |
|---|---|
| D.1 | Open in this return. D.21 excludes dimension two by the exact geometric S3 action, leaving dimensions one or three. Full profinite peripheral lifting remains unproved. |
| D.2 | Open in this return; no full profinite realization or exclusion of the extra weight-nine line. |
| D.3 | Proved in the complete weight-nine stratum: compatible class-ten exponent101 quotients give gentle/pentagon dimensions 37/2 and leading metabelian dimensions 2/1; the exact rational certificate and D.20 derive R9 in weight nine. |
| E.1 | Completed: independent program confirms every requested count and both exact Smith forms; it also checks actual integral cusp gauges, both hexagons, centralizer recovery, and 24 distinct resulting automorphisms. |
| E.2 | Full CM existence remains open. A common class-two refinement excludes all twelve original extra representatives (and every other original representative except identity). Nevertheless all 24 whole CM fibres survive the entire relative class-two tower with multiplier one (E.15). E.16 extends these families simultaneously through all finite collections of nonabelian simple quotients, and separately through each finite perfect quotient. An explicit solvable class-three quotient remains outside this enlarged family. The original representatives do not exhaust the matrix fibres. |
| E.3 | Full image remains open. The five simultaneous distribution projections pass. E.17 tests the full pentagon in a pure four-strand quotient of order 5184: it excludes 15 selected E.14 representatives, but every whole CM matrix fibre has a verified replacement. The pentagon cuts one affine equation in the 18-parameter three-primary presentation. |

## Source audit

The full task and the attached LM7 D.11--D.26, corresponding source programs, and relevant portions of the review were read. The authority scans are not attached; only the transcription was available. No fresh inspection of manuscript scans is claimed.

- **R8:** `d_metabelian.py` was rerun unchanged in an isolated output directory and reproduces the four exact rational rows. The quotient map is from solutions in the free Lie algebra to the metabelian quotient; solving directly in the metabelian quotient would discard part of the equations. The existing integral pro-ell lifting proof was checked at the point that successive lower-central corrections converge in every finite ell-group. This verifies the stated pro-ell mechanism and gives no lift through arbitrary finite groups.
- **R9:** Furusho's attached primary source was opened at Corollary 0.3, Theorem 0.5, Proposition 5.1, Lemma 5.2. Its gamma consequence gives the checked upper bound, with the explicit Fox coefficient map `M(p[x,y])=XYp`. Hain--Matsumoto's attached primary source was opened at Theorem 8.4, Section 8.4, Lemma 8.5 and Remark 8.6. Remark 8.6 explicitly invokes Ihara for nontriviality; it does not itself display the depth-one coefficient formula. Brown's opened primary preprint displays the motivic formula (1.3). The later primary-source audit opens Ihara, ICM 1990 lecture, Section 6.2, the theorem in Section 6.3 and equation (6.4.4). D.20 now proves the lower bound, including the exact Fox normalization and extraction in the actual compact Galois image. The derivative proof was peer-reviewed; the nilpotent target was enlarged by one class to retain the degree-m multiplier on the degree-two commutator. The `actual_Galois_and_GT_rational_rank` field in the old gamma program is a literature-populated label, not an independent computation of the Galois group.
- **R10:** Dolgushev--Guynee's attached source was opened at Theorem 5.2, Corollary 5.4, Proposition 5.5. Harbater--Schneps' complete author PDF was opened at its Main Theorem and relevant definitions. Bleher--Chinburg--Lubotzky's attached source was opened at Lemma 2.3 and Corollary 2.4. The old finite A5 counterexample program was rerun successfully. The exhibited unrestricted lift fails the peripheral condition; this does not disprove existence of another lift meeting that condition.
- **R11:** The finite sign extraction used here was checked against LM7 D.25's explicit torsion formulas. The fields are `Q(E3[4])=Q(i,(3/4)^(1/4))=Q(x(E4[3]))`; the E3[12] rational-three-torsion sign rule supplies the full four-torsion action. The global CM reciprocity and full adelic image in D.15--D.17 were not re-proved here. No correction to their finite sign test was found.
- **R12:** The original scripts were rerun and the finite matrix/path/Smith calculation was independently implemented. The integral correction proof of D.26 was checked. Its coherent choice of the level-six cusp gauge is retained: the proof does not assert extension for every unrelated choice of a finite representative. The noncofinality is independently witnessed by the new A5 quotient.

## Established theorem added to the literature audit

Benjamin Enriquez, *Quasi-reflection algebras and cyclotomic associators*, arXiv `math/0408035v2`, Theorem 8.1 and Remark 8.6, proves `GT_K=GT_hat` for the full profinite group and the relations `delta_N(f)=y^{c_N(f)} f`, `c_MN=c_M+c_N`. The complete primary PDF and proof were opened. The exact comparison of its positive Schreier basis with LM7's negative Schreier basis is written in D.5. This strengthens the Galois-only use of cyclic-cover compatibility in LM7 D.20. It does not settle either of the requested full profinite image problems.

Searches included combinations of `Grothendieck Teichmuller Kummer distribution relations Ihara`, `GT_K Enriquez`, `GT0 CM elliptic extra coset`, `gentle GT shadows genuine`, and `weight nine special derivations metabelian gamma`. The primary works inspected also include Dolgushev--Le--Lorenz, Appendix B, Theorem B.2, and the attached 2026 v3 dihedral-shadow paper. The former has an abelian pure-quotient hypothesis. For the latter the pure image embeds in a product of three dihedral groups and is metabelian. The CM target `H=C2^2 x SL2(F3)` has nontrivial second derived subgroup. Since a surjection maps each derived subgroup onto the corresponding derived subgroup, these families do not dominate this specified target. No claim of priority is made for the additional finite tests.

An October 2026 arXiv result entitled *CM Elliptic Analogue of the Coleman--Ihara Formula* appeared in search metadata. Opening its primary page and HTML returned tool errors, so it was not used as a verified theorem. The original 1989 Ihara paper was located bibliographically, but its full primary text was not opened. These failed retrievals do not establish anything about the missing comparison.

## Programs actually executed

Original code was copied under `code/de_source/` and executed there. Its provenance is distinct from the independent verifier:

| Program | Status and salient output |
|---|---|
| `de_source/d_cm_shadow.py` | Exit 0; 48 matrix pairs, 24 certified G6 automorphisms, 12 extra. |
| `de_source/d_cm_refine.py` | Exit 0; Smith `(1^96,2)` and `(1^97)`, HNF identity, 384 general-multiplier hexagons through powers 2,4,8,16 and 3,9,27,81. |
| `de_source/d_metabelian.py` | Exit 0; all rational rows in R8 reproduced. |
| `de_source/d_gamma.py` | Exit 0; 224 Lyndon Fox identities, weight-nine coordinates `(15/2,9/2)`. |
| `de_source/d_lifting.py` | Exit 0; finite unrestricted-lift peripheral counterexample checked. |
| `de_verify_cm.py` | Exit 0; independent matrix enumeration, reconstructed spanning tree and integral cycle basis, every cusp solvability count, both Smith forms, all certificate ranks, 48 gauged hexagons, 24 distinct automorphisms, centralizer image orders 1 and 1. Imports no source program. |
| `de_a5_refinement.py` | Exit 0; A5 order 60, simple and perfect, cusp order 5, Q derived-series orders 576,96,8,1; all 24 shadows extend to `G6 x A5`, all 12 extra survive. |
| `de_distribution_test.py` | Exit 0; reconstructs integral free words and the N=2 projection; 12/12 candidates pass. |
| `de_distribution_more.py` | Exit 0; exact individual projections for N=2,3,4,6,12; all candidates pass with corrections in `[N_B,N_B]`. |
| `de_distribution_joint.py` | Exit 0; exact joint correction image order 42,467,328; all 24 pass simultaneously, including c4=2c2, c6=c2+c3, c12=2c2+c3 modulo 6. |
| `de_s3_core.py` | Exit 0; fully specified S3-core J, exact kernel F3^288 over G6, cusp order 72, all 24 deterministic cusp solutions have full generation rank 288; both gauged hexagons verified and all 12 extra candidates survive. |

The outputs are `.out` and `.json` beside the programs. The source reruns use `.rerun.out`. Finite records are preserved, not merely aggregate counts. The independent checker reads the original proposed witnesses and verifies them; it does not independently search for a replacement set of witnesses.

## New finite refinement

The homomorphism `B -> A5`, `s -> (12)(34)`, `r -> (135)` is onto. The diagonal quotient with G6 is exactly `G6 x A5`, by the common-quotient criterion and solvability of G6. The image of `[N_B,N_B]` is all A5, so its kernel is outside the homology family. The extension of each certified shadow is explicit: use the product of its G6 automorphism with identity on A5, multiplier one, and conjugator `(f6,1)`. The image of the pure group is the product of its two images, so this conjugator is represented by a genuine discrete commutator word. This proves a successful finite shadow test, without a cofinality assertion. The S3-core calculation is recorded separately below.

## New finite distribution projections

For each N in 2,3,4,6,12, the induced wreath representation computes the exact image of `[N_B,N_B]` under `(q delta_N,c_N mod6)`. The image orders are 8,48,48,48,48. The corresponding full K6 image orders are 8,144,96,144,288. Every one of the 24 candidate cosets meets the required distribution target using a correction in `[N_B,N_B]`, preserving both its commutator nature and its image in G6. The exact simultaneous permutation-group calculation then computes the joint image of N_B' in all five targets, of order 42,467,328, and proves that one common correcting word works for each candidate. The common word can satisfy c4=2c2, c6=c2+c3, c12=2c2+c3 modulo 6 as well. No generation at a new quotient carrying all these projections, complete finite pentagon identity, or all-positive-integer-N conclusion is asserted.

## Exact remaining barriers

1. D.1: construct peripheral-preserving full profinite lifts of the extra weight-five directions or produce a finite obstruction bounding their image.
2. D.2: do the same for the invariant extra weight-nine line, with generation retained.
3. E.2: determine the full CM matrix fibres beyond the relative class-two tower, or prove nonemptiness at every finite quotient. E.15 supplies coherent lifts through that entire tower with multiplier one. E.16 adds every finite collection of nonabelian simple quotients and each fixed finite perfect quotient. The natural quotient by gamma4(N) N^5 gives an explicit solvable class-three comparison outside this enlarged family; higher commutator lifting remains unproved.
4. E.3: test the full pentagon in the relevant CM refinements or prove an all-finite-quotient theorem for a surviving matrix fibre. The distribution tests give additional necessary projections only. The weight-nine pentagon comparison of D.3 is proved separately.

The finite set compactness theorem supplies a single finite obstruction
for a fixed finite list of representatives. This obstruction has now been
constructed for the original twelve extra representatives. A conclusion
about the full CM coset requires the whole matrix fibres; E.11 explicitly
shows why the representatives cannot be substituted for them.

## The requested S3-core J

Statement E.7 fixes the free basis that LM7 D.26 leaves to be chosen and computes its exact core quotient. The basis is the ordered fundamental-cycle basis of the independent verifier. Its first generator is `(s r^-1)^12`; both first words are saved explicitly in `de_s3_core.json`. The map from N_B to S3 sends the first two basis generators to the affine transpositions `z -> -z` and `z -> -z+1` on F3 and the remaining generators to one. The normal core is represented faithfully by the diagonal of G6 and the induced S3 wreath representation over Q.

The kernel above G6 is an elementary abelian group of exact dimension 288 over F3. The proof and program obtain it as the stable span of the commutators of all 97 basis images under the two B-generator actions; every generator of the span is the image of an actual commutator word. The cusp has order 72. For all 24 candidates the linear cusp correction map has rank 288 and its first deterministic solution has generation rank 288. The correction elements lift to N_B', so the original integral cusp gauge still applies; the program verifies both hexagons after that gauge. Every certified base shadow therefore has a surjective shadow above it at this J, including all twelve extra CM candidates.

This computes the requested initial quotient and the reduction fibres over the named 24 candidates. It does not enumerate every other shadow at J or identify the full image at every finer quotient. No random-search success or failure is promoted to a theorem: every case succeeds at the first deterministic solution.
# Update: class-two refinements exclude every recorded extra representative

The newest formal additions are E.8--E.10, in `sections/E_class2_agent.tex`,
input by `sections/E_agent.tex`. They supersede the earlier statement that
the genuineness of the twelve *specified* extra shadows was uncomputed.

Define `J3=(gamma3(N_B) N_B^3) intersect (N_B' N_B^2)` and
`J2=(gamma3(N_B) N_B^4) intersect (N_B' N_B^3)`. Their inverse images
in `B3` are finite-index normal subgroups contained in `PB3`; both lie
below the original level-six kernel. The kernels above `G6` have dimensions
4656 over F3 and 4753 over F2. The cusps have orders 72 and 144.

The actual complete finite gentle equations were solved, rather than
assuming that finite torsion lifts preserve conjugacy classes. After
undoing the recorded gauge, all lifts are `S=S0*k`, `R=k^-1*R0(lambda)`.
Their equations are `(1+S)k=0` and `(1+R+R^2)k=R0(lambda)^3`.
These are algebraically equivalent to the pair of finite hexagons.
For the 2-refinement the exact two-dimensional commutator condition was
included, using `im(N_B -> F^ab) = [[6,4],[0,2]] Z^2` and
`im(J2 -> F^ab)=12 im(N_B -> F^ab)`. Both multiplier residues 1 and
73 modulo 144 were tested. Frattini-quotient invertibility proves generation
for every retained solution.

The 3-refinement retains indices 0,1,2,3, with coefficient rank 1542
and augmented rank 1547. The 2-refinement retains indices 0,16, with
coefficient rank 3927 and augmented rank 3932. All retained solutions
were substituted into the original equations. Their common refinement
retains only index 0, the identity. The indices are zero-based in
`de_source/d_cm_shadow.json`, filtering for `mod6_beta_cycles`.
Thus all twelve recorded extra shadows are nongenuine. This is a negative
finite witness and requires no cofinality claim. Files:

- `de_class2_refinement.py/.out/.json` and its `.npz` certificate:
  exterior-square peripheral equations, Jordan reduction, all centralizer
  variations; coinvariant dimension 8, centralizer variation rank 3.
- `de_class2_direct_check.py/.out/.json`: independent full 9312 by 4656
  matrix, rank 4648, the same eight dual invariants and four survivors.
- `de_class2_two.py/.out/.json` and its `.npz` certificate: quadratic
  coinvariants, dimension 16; s-centralizer variation rank 11.
- `de_class2_gentle.py/.out/.json`: complete 3-refinement gentle equations.
- `de_class2_two_gentle.py/.out/.json`: complete 2-refinement equations,
  both multiplier residues, exact commutator-image condition.
- `de_gf3.c`: bit-packed exact eliminations, checked against the independent
  Python routine on four rectangular matrices for each prime.

The *full CM existence question* has not thereby been settled. The
original source chose a single point in each admissible matrix fibre.
`de_affine_fibres.py/.out/.json/.npz` now records the complete linear
spaces. At p=2,3 respectively they have dimensions 98,97; quotienting
conjugator centralizers leaves 17,18; quotienting by actual cusp powers
leaves 16,17. Quotienting all finite inner conjugacies would leave 8,9,
but the associated finite centralizer elements need not lift as
centralizers. Their fibres cannot be discarded in the higher problem.
Invertibility remains an additional condition. R11's genuine arithmetic
points in every compatible CM fibre and the excluded compatible recorded
points give concrete evidence that CM matrices do not determine a G6 shadow.
The prompt's claimed equivalence with one of twelve particular points is
an unproved reduction, not a reason to ignore the other points.

The full profinite torsion-conjugacy comparison is also supplied:
Harbater--Schneps Proposition 4, proof of (i) implies (iii), author PDF
pages 14--15, extends the full gentle action to profinite B3 and maps
its central generator to its lambda-th power. Scheiderer's Appendix
Corollary, printed p.598 of Lochak--Schneps (1997), puts every finite
subgroup of the free profinite product into a factor. E.8 derives the
conjugacy and the Fhat-conjugator assertion explicitly. Primary PDFs:
https://webusers.imj-prg.fr/~leila.schneps/HS.pdf and
https://webusers.imj-prg.fr/~pierre.lochak/textes/inventiones.pdf .

That next computation is now complete: E.11 proves that **all 24 whole
CM matrix fibres have replacement points at the common refinement**.
`de_fibre_three.py` and `de_fibre_two.py` construct and directly check five
quadratic obstruction polynomials on the 18- and 17-dimensional parameter
spaces. Each produces a verified zero of full generation rank in all
24 fibres. `de_fibre_crt_verify.py` combines their changes by CRT, reruns
both complete norm systems including the commutator rows, and directly
substitutes all 48 hexagons in a faithful class-two collector. Every
retained common multiplier is 1 modulo 144. Its JSON retains literal CRT
conjugator words, explicit factored correction words, an actual correction
in Jstar that makes f a word of Fprime, and the common integral gauge.
The searches are used only for these positive witnesses. Their failed
trials carry no exclusion claim.

The entire three-primary class-two tower is now covered by E.12.
`de_fibre_three_smooth.py/.out/.json` computes the actual eight-component
quadratic obstruction Jacobian and appends the available r-centralizer
directions. It has rank eight at every one of the 24 retained points.
Together with the 97 homology equations and 4648 central equations, this
is a full derivative of rank 4753. The formal proof lifts by successive
3-adic correction and takes the complete limit. Thus all 24 CM pairs
have coherent lifts at every exponent 3^k in the class-two tower, with
a coherent gauge. The assertion includes exponents nine and 27.
The tower still kills gamma3(N_B); this does not settle full profinite
existence. The two-primary integral Jacobian requires a separate proof.

## Complete finite pentagon calculation (D.7--D.8)

Task D.3 now has a complete computation in the precise stratum that
defines weight-nine leading terms. Set
`K_n=gamma11(PB_n) PB_n^101`, for n=2,3,4. Characteristicity makes
these normal braid kernels. Every insertion/cabling homomorphism
preserves them, and the forget-strand retraction proves that the induced
three-strand kernel of K4 is exactly K3. Thus the three- and four-strand
finite shadow definitions use the same data. The multiplier is one,
and f ranges over the entire gamma9 subgroup of the free factor quotient.

The full hexagon equations have 155 logarithmic variables of degrees
nine and ten. `de_gentle_weight9.py` solves all 3072 coefficients:
solution dimension 37, leading degree-nine dimension four, metabelian
image dimension two. This also retains a degree-ten correction for
each of the four leading basis vectors. `de_pentagon10_finite.py`
computes the actual four-strand pentagon using the literal pure Artin
action in `PB4/Z = F3 semidirect F2`. Its derivations include the
degree-raising-two terms obtained from exact conjugation words; no
homogeneous-associator comparison is assumed. The run finished in
501.307 seconds. Degree-nine pentagon equations reduce 37 to 34;
the complete degree-ten equations reduce 34 to 2. Their leading image
has dimension one, and its metabelian image is exactly F101 G9.
All retained basis vectors were substituted into every hexagon and
pentagon coefficient. The JSON contains both full shadow logarithms;
the NPZ contains all matrices. The Frattini quotient argument verifies
generation, and Dolgushev--Le--Lorenz Proposition 2.10 supplies the
equivalent four-strand generation condition.

`de_pentagon9.py` separately constructs the graded pentagon matrix.
`de_pentagon9_rational.py` evaluates it anew over the integers and
computes exact rational kernels and Smith forms. The special-invariant
constraint matrix has Smith factors 1 repeated 52 times; the selected
four-column kernel basis has factors 1,1,2,24. A 3 by 3 pentagon minor
is 27648=2^10*3^3. The vector (-3299,1326,-1613,432) vanishes in all
19683 pentagon tensor coefficients. Its metabelian coordinate is
-96*(9,36,84,126,126,84,36,9)=-96G9. The metabelian matrix itself has
nonzero Smith factors 1,4. These certificates work over every field
of characteristic zero or at least five. Applying the explicit leading
map from the full profinite pentagon equation gives the rational upper
line for every ell>=5. The actual arithmetic lower bound in D.20
supplies equality, deriving R9 in weight nine.

Other multiplier and lower-leading-weight strata are not counted by
this program: their images do not belong to the weight-nine leading
piece defined in Part D. The exact filtered comparison explaining this
restriction is in D.8. The finite gentle extra direction is present,
but its lifting to every finite quotient remains D.2. No cofinality
conclusion is drawn from the class-ten quotient.

Additional primary sources opened for this computation:

- Cohen--Falk--Randell, *Pure braid groups are not residually free*,
  equations (2.1)--(2.3), printed pp.214--215, and (4.1), printed p.223.
  The author PDF and institutional publication metadata were opened.
- Lazard, *Sur les groupes nilpotents et les anneaux de Lie*, Chapter II,
  Theorems (4.2), (4.3), Corollary (4.4), Lemma (4.5), and Theorem (4.6),
  printed pp.175--180. Numdam's cached full primary text was opened after
  the direct large PDF fetch failed.
- Dolgushev--Le--Lorenz, arXiv:2008.00066v2, Definition 2.9 and
  Proposition 2.10, pages17--18 of the PDF, opened and compared with the
  attached full source; its compatible-kernel construction and actual
  pentagon are used, as well as its generation equivalence.

## Exponent eight: complete correction fibres and common witnesses (E.13)

The exponent-eight image of `N' N^6`, retaining `N_ab/3`, is the abelian
group `(Z/4)^4753` with basis `n_i^6`, `[n_i,n_j]^3`. Therefore the entire
central correction fibre over a fixed affine G6 homology shadow is one
linear system over Z/4, even though arbitrary selected exponent-four
corrections can fail at the next level. `de_class2_eight_fibres.py` solves
this system for all 24 affine points from E.11. The binary rank is3927
and nullspace dimension827 (including the multiplier); the second-layer
coefficient rank is3953 in every case. Every fibre is nonempty, and all
retained solutions have multiplier1 modulo288. The exact abelian-image
rows are included, and both full order equations are substituted.

`de_fibre_eight_crt_verify.py` combines these new two-primary corrections
with the earlier three-primary corrections. Its explicit common word is
`k = product n_i^(6 k2_i) product [n_i,n_j]^(3 k2_ij+4 k3_ij)`.
An explicit product of twenty-fourth powers corrects its F-abelianization
to zero. Both complete braid hexagons are then evaluated in the faithful
exponent-eight and exponent-three collectors: 96 component checks pass.
All literal base words and factored corrections are retained. The common
kernel is `(gamma3(N_B) N_B^8) intersect (gamma3(N_B) N_B^3)`, so this
refines Jstar and establishes E.13 for every whole admissible matrix fibre.

The normal-form block action is independently checked against16 literal
expanded conjugate words, including a nontrivial change of section.
Two implementation corrections were made before E.13 was recorded:
the norm matrix is used before the cusp gauge (conjugation by x^g fixes t),
and the shortest-word section is converted to the streaming spanning-tree
section by `tau_tree=tau_short-c wedge A`. Initial failed intermediate
counts from before these corrections are superseded by the rerun outputs;
they are not used as mathematical claims. Earlier E.9--E.12 used central
kernel actions, where that section difference acts trivially.

The corrected `de_class2_eight.py` also checks the complete fibres above
the24 particular E.11 exponent-four witnesses. Their negative tests concern
only those particular corrections. E.13's positive whole correction-fibre
calculation explicitly supplies replacements with the same G6 homology
image. The subsequent E.14--E.15 calculations and integral lifting
proof settle the two-primary and full relative class-two towers;
full profinite lifting remains to be determined.

## Further primary-source comparison for E.3

Nakamura--Tsunogai--Yasuda III, JIMJ 9 (2010), 431--448, was opened
in full from Nakamura's author-uploaded PDF. Proposition 4.4 constructs
the GT action on the Mordell triangle-cover Tate module through the
adelic beta function. Theorem 4.16 identifies that action with the
equianharmonic h-matrix for Galois elements. Proposition 4.13 likewise
states its braid formulas for Galois elements; the introduction, p.432,
expressly leaves their full-GT validity undetermined.

The remaining comparison must therefore identify the triangle-cover
beta action and the normalizer h-coordinate on the entire GT source.
The two constructed actions alone do not furnish this equality.
The actual comparison on the Galois subgroup is already accounted for
by R11; extending it is precisely the unproved step in this approach.

Marin's complete primary paper, arXiv:0801.2507, was also opened.
Section 4, Lemmas 4.1--4.3, supplies profinite rigidity for the standard
B3-to-SL2 representation and a Kummer cocycle. Sections 5--6 concern
the formal characteristic-zero Burau representation. These results
do not supply the missing beta-to-h formula in the checked statements.

Searches additionally used the exact titles of the harmonic/equianharmonic
papers together with `distribution`, `Enriquez`, `Burau rigidity`, and
the theorem identifiers above. The RIMS 1267 (2002) primary account was
also opened: its Theorems 1--2 concern the Galois image, and Proposition
5.1 relates two Kummer extensions using the extra harmonic equation.

The new primary preprint Lochak--Nakamura--Schneps,
arXiv:2602.12462 (12 February 2026), was opened at Theorem 1.1,
Theorems 2.1--2.5, and Section 8. It constructs full-GT actions on
the mapping class groups with zero or one marked point. Section 8,
p.19, explicitly leaves the indicated cutting-map compatibility
unresolved; that compatibility is not included in Theorem 1.1.
The checked statements therefore do not give the beta-to-h comparison.

## E.14--E.16: complete relative class-two lifting and simple quotients

`de_class2_sixteen_fibres.py` solves the entire exponent-sixteen
correction fibre above each of the 24 retained affine G6 points.
There are 801 lower binary parameters and 827 upper parameters;
the projection of the former to homology and the multiplier has
rank 15. All 32768 choices of those 15 parameters survive in every
case. The remaining linear system has rank 3953 and its reduced
quadratic obstruction has rank 0. The actual words use sixth
powers, the listed central commutators, and an exact adjustment
by forty-eighth powers. `de_fibre_sixteen_crt_verify.py` verifies
96 complete hexagon components, not merely their linearized norms.

E.15 uses integral first-kind coordinates on the subgroup with even
homology, where the bracket is divisible by 12. The order-two and
order-three equations compress into primitively embedded fixed
lattices of ranks 2361 and 1591; one independent commutator row
gives target rank 3953. The full integral Jacobian modulo 4 has
3927 unit elementary divisors and 26 of valuation 1. The complete
fixed-multiplier check `de_two_hensel_fixed.py` recomputes the
826-dimensional binary kernel after deleting the multiplier
column, and obtains the same ranks at all 24 points (29.454s).
Newton corrections from the exponent-sixteen points converge with
multiplier exactly 1. The compression, divisibility estimates and
Newton proof were separately audited by the parent agent.

The adelic gluing is performed before the cusp gauge, when all
components act identically on Q. One adelic exponent then supplies
the common gauge. Its components outside 2 and 3 are zero. The
normalized f can have a nontrivial Q-coordinate: independently,
`de_adelic_gauge.py` checks all 24 and records I, [[1,4],[4,5]],
or [[1,8],[8,5]] according to the gauge modulo 6. The exact
abelianization formula proves that the common element lies in
the image of the actual profinite commutator subgroup. This
corrects an intermediate draft that incorrectly placed every
normalized component in N and took all other-prime normalized
actions to be identity.

E.16 extends these compatible families through all nonabelian
simple quotients simultaneously. A finite joint image of simple
targets is a product with diagonal repetitions identified; its
perfection and the solvability of the relative class-two target
give the exact product comparison by a proved subdirect-product
argument. The same reasoning treats each fixed finite perfect
target. The family still omits the natural solvable quotient
B/(gamma4(N) N^5). The word [[n0,n1],n0] has image I+2E14
in UT4(F5), verified by `de_solvable_barrier.py`; hence gamma3(N)
is not killed there. Every solvable quotient of the constructed
product kills its perfect factor, proving the stated failure of
factorization through this larger family.

## Fermat-cover comparison supplied to Part A

`de_fermat_schreier.py` constructs the actual rank 10 kernel of
F2→(Z/3)^2 and its class-two collector, including all 45 central
coordinates of the unknown Ihara conjugator. Its coefficient
certificate retains the quadratic dependence on the 10 homology
coordinates and the exact linear dependence on the 45 central
coordinates. The eight-dimensional cusp lattice is primitive;
the explicit proper-curve quotient has Smith form (1,1). All nine
complex-conjugation cusp identities are verified by free-word
reduction, including the infinity permutation a↦−a−1. The module
and its certificate were supplied to the arithmetic agent for the
intrinsic Johnson-coordinate comparison; no unknown arithmetic
conjugator was assigned a value by this geometric calculation.


## E.17: complete finite four-strand pentagon and all affine fibres

The exact representation B4→F3²⋊SL2(F3) sends the three braid
generators to (0,A), (0,B), (e1,A), where A and B are the two
standard transvections. Adjoining the actual permutation map to
S4 gives a pure normal kernel and quotient of order 5184, verified
by complete generation. All five pentagon factors and the third
braid-generator conjugator are evaluated simultaneously. The
97 Schreier generators of N have commuting exponent-three
images in all six targets, checked by all 4656 commutators. Thus
these evaluations factor through the actual G6 conjugator image,
and a failed representative cannot be repaired by changing its lift.

Among the 24 E.14 affine G6 representatives, only indices
3,4,5,7,8,14,15,17,23 pass; the extra-coset indices are 4,7,15.
These are the E.14 replacements, not the original E.1 records.
The whole-fibre calculation retains every one of E.10's 18
three-primary parameters. Its image in the auxiliary logarithms
and gauge has dimension two; all nine values are enumerated in
every matrix fibre. The full pentagon is one rank-one affine
equation, leaving a 17-dimensional parameter hyperplane before
the cusp quotient. In every fibre the program retains a point
with full generation rank 97 and vanishing five class-two cusp
obstructions. Actual commutator words, all nine auxiliary values,
the exact linear matrix, its section and kernel, and all coordinates
are saved. Literal substitution checks every pentagon, all three
braid relations, the cusp relation in G6, and the unchanged mod2
generation matrix. These are complete checks in the stated finite
quotient; the full profinite GT image remains unresolved.


## E.18 and E.19: Ferrari central layer and complete modulus-nine corrections

The next actual Ferrari quotient is H_3(F3) semidirect SL2(F3), of
order 648, with pure normal four-strand quotient of order 15552.
Its central coordinate is related to the ordinary free class-two
coordinate by z=z0-u-2v. All six evaluation maps still kill N-prime
and N cubed. The complete 18-parameter CM image has rank two and
the same kernel as E.17; all 216 auxiliary values were checked.
The higher central pentagon has exactly the old zero set, and all
24 E.17 literal words pass and generate the order-648 target.

At modulus nine the actual Jacobi target has order 472392. All
six F2 evaluation maps are induced through all six B/F2 cosets;
intersecting their core with ker(B→G6) defines an exact finite
normal three-strand kernel. Its correction image is F3^4. The
whole image of its intersection with F2-prime is F3^3, computed
using the integral rank95 kernel of the N-to-F2 abelianization
matrix; the pivot columns 0 and8 have determinant1. No power
corrections are discarded. The gentle norm equations have rank2;
the pentagon has rank3 and selects one correction in every one
of the 24 retained G6 fibres. All27 correction values per fibre
were checked against the exact affine equations. Every retained
word then passes complete direct hexagon and pentagon substitution,
all three braid relations, and source kernel generation rank4.
The four-strand matrix image has order648 and the Ferrari
homology determinant is nonzero modulo3, proving generation of
the full Jacobi target. The source core kills N-prime and all
ninth powers, so it is a quotient of G18; this is an additional
four-strand condition, not new cofinal three-strand coverage.

## Exact full group-pentagon assistance to Part A

The actual pure Artin model PB4/Z→Aut(F3), its generator conventions,
faithfulness on the free fibre, and the exact truncated Magnus
comparison are documented in research/DE_fermat_pentagon.md.
The unpruned and optimized evaluators agree on every coefficient.
Both retain all source degree6 and degree7 kernel corrections;
the complete automorphism residual through degree8 has 29520
coordinates. The resulting affine solution spaces were supplied
to Part A. Independent de_fermat_scalar_audit.py then checks the
integral source coefficient 3 f2=m(m+1)/2 and the true-kernel
contributions [3,0,0,0,0]. For all three scalar-filtered branches,
the particular point and entire homogeneous space still satisfy
every one of the 29520 saved group-pentagon equations. The scalar
uses the torsion-free integral Z3 identity before reduction mod9.
Part A owns the resulting arithmetic conjugacy and section claims.


## E.21: actual fourth-degree characteristic-three Ferrari target

The free Ferrari kernel is mapped to the units of the actual truncated
noncommutative F3 algebra, retaining X cubed and Y cubed. The B3 action
is evaluated on complete generator series, so it retains all changes
beyond its SL2 homology action. The degree3 model has Ferrari kernel
order2187, B3 automorphism image1944, and total target4251528; its joint
core with mod9 still has dimensions4 and3 and all24 pass. Degree4 gives
a larger common core: full kernel overG6 dimension7, image ofN-prime
rank3, and entire F-prime correction image rank6. Norm rank4 and pentagon
rank5 leave one affine line in each retained G6 fibre. Every selected
literal word passes both complete hexagons, both pentagons, all braids,
and direct source kernel generation rank7. The full run took227.419s.

A separate complete Schreier calculation over the E18 group of order648
computes the entire joint four-strand kernel as F3^12 and hence the
actual target order344373768. It repeats this calculation on all24
corrected triples, obtains the same full image, and checks preservation
of the three- and four-strand full twists. All generators have order
dividing9, so the target has cyclic odd abelianization. Every nontrivial
S4 quotient has a C2 abelian quotient; Goursat therefore gives the exact
direct product withS4 and pure normal quotient order8264970432. This
independent generation calculation took30.783s. The source lower-central
image dimensions are3 atweight2 and0 atweight3; the core kills gamma3N
andN18. Thus the three-strand component remains within E15's proven
relative class-two tower. The new information is the finite four-strand
pentagon and generation check, with all three old correction points
available for a next-degree lift. No full profinite consequence is drawn.


## Withdrawn initial degree-five negatives and exact correction

The first degree-five calculation formed Rbase=Sbase*t. At that stage
Sbase is a lift of an involution and can have a nonzero top-layer square,
so this formula did not preserve Sbase*Rbase=t. A separate gentle-only
verification caught the product error before E.22 was written. The
correct formula is Rbase=Sbase^-1*t; both corrected solvers now assert
the product identity before constructing the norm equations. Every
initial negative conclusion was withdrawn. The four initial positive
words had passed complete direct hexagon/pentagon and generation checks
and remain valid positive witnesses, but they do not validate the
incorrect negative systems.

The unchanged original JSON and NPZ are preserved as
code/de_ferrari_degree5_failed_initial.json and its certificate. The
original solver was reconstructed by reversing exactly this line change;
its output destinations alone are renamed for a failed-initial rerun.
The original stdout file had already been opened for the corrected rerun
when the retention instruction arrived, so its replacement failed-initial
stdout is explicitly a rerun, not claimed to be the original byte file.
The original identity/separation and generation outputs are retained
under failed_initial_input names. Corrected outputs supersede these;
checkpoint04 is to include only the already audited statements through
E.21 until the corrected degree-five calculation is completed and audited.

## E.22: corrected complete degree-five refinement

The corrected calculation is complete. Both the entire top kernel and
the image of its intersection with F2-prime have dimension six. Their
complete normal presentations retain 5460 and 5354 relations, respectively,
including all old basis cubes, commutators, and N-conjugation relations.
All 72 points of the 24 old correction lines are tested. The exact norm
system has rank four and is consistent at all 72 points; the pentagon
matrix has rank five and the combined matrix has rank six. Precisely
one point in every old line has a simultaneous solution, and its top
correction is unique. Thus all 24 particular E.17 G6 shadows survive,
including all twelve extra-coset points. The corrected run took 140.829s.

Every retained literal F2-prime word passes both full hexagons in all
36 induced coordinates, both target pentagons, all braid relations,
and source kernel generation rank 13. The actual lower-central images
of N have dimensions 9, 3, 0 in weights 2, 3, 4. In particular this
specified source quotient has a nonzero relative third-commutator image.
Its natural quotient map cannot factor through any finite E.20 quotient:
the relative prime-to-six factor maps trivially to its relative
{2,3}-kernel, while the remaining class-two factor kills gamma3N.
The proof uses these explicit quotient maps and the nonzero retained
third-commutator witness.

An independent complete Schreier calculation computes the joint
four-strand target kernel over E.18 as a class-two exponent-three group
with Lie dimension 21 and commutator dimension 9. Its order is
6,778,308,875,544; adjoining the exact S4 permutation coordinate gives
pure normal quotient order 162,679,413,013,056. All 24 corrected triples
generate the entire target and preserve both full twists. This calculation
took 27.784s. A separate gentle-only calculation constructs actual
surjective witnesses in all 24 fibres in 91.857s.

The control program checks the literal identity, distinguishes the E.17
index-zero G6 point from the E.1 identity, and retains a provisional
involution whose nonzero top square makes S0t fail the cusp product.
It verifies S0 inverse times t instead. The combined cusp has exact
order 72, the pure peripheral powers have orders dividing 36, and the
four-strand generators have orders dividing 9. Therefore all multiplier
lifts of these retained G6 shadows give exactly the same finite tests.
Other G6 points and multiplier residues in the whole CM fibres are not
enumerated here; the 24 positive witnesses already prove those fibres
nonempty at this specified refinement. The full profinite lifting
question remains unresolved. The formal statement and proof are
sections/E_ferrari_degree5_agent.tex.

The all-72 gentle-lift statement also has an exact generation proof,
added as (E.22.10). The actual relative N-image is (N_ab/2) times a
finite three-group P. Its 97 generators map onto N_ab/3 of rank97,
so the kernel of P to that quotient is exactly its Frattini subgroup.
Every norm solution already induces the fixed G6 automorphism and hence
surjects onto this Frattini quotient and the independent two-primary
factor. Thus every norm solution is surjective, in addition to the
selected direct rank13 certificates. This proof uses E.18's verified
elementary-abelian N-image and the three-group kernels of the actual
mod9/Magnus reductions.

## E.23: complete degree-six correction planes

The next compatible Ferrari quotient has complete top kernel F3^6,
again entirely represented by F2-prime words. The normal presentation
retains 5993 relations for the old rank12 F-prime image and 6105 for
the old rank13 full image; both old images are checked elementary
abelian before using this presentation. The full source kernel over
G6 now has dimension19 and is elementary abelian. The actual successive
N lower-central images have dimensions15,6,3,0, so this specified source
quotient has relative class four and its natural map does not factor
through the preceding relative class-three quotient.

All24 degree-five simultaneous points lift. At every point the norm,
pentagon, and combined ranks are4 on the complete six-dimensional
correction space. Each fibre is an affine plane with all9 points retained.
The selected-word run took315.047s and checks actual F-prime words,
both full source hexagons in all36 coordinates, both target pentagons,
all braids, and source generation rank19. The Frattini argument in
E.22.10 proves source surjectivity for every solution of every plane.

The entire four-strand target has kernel Lie dimension30 over E.18,
with derived dimension18, and order133,417,453,597,332,552. Its pure
normal quotient has order3,202,018,886,335,981,248. The selected full
generation run took56.986s. A further complete plane audit took156.692s:
all216 points pass full source/target relations, generate the entire
same four-strand group, and preserve both full twists. The retained
Schreier logarithm matrix is affine in the two parameters; its differences
lie in the central degree-six kernel, so the actual derived space is
constant. Appending it gives rank30 at all9 values in every plane.
Both the affine matrices and the individual rank checks are retained.
Only the class-two exponent-three kernel over E.18 is logarithmized;
the relative class-four N-image is never subjected to a class-less-than-p
assumption. The exact source cusp period remains72.

The new formal statement is sections/E_ferrari_degree6_agent.tex.
The full profinite tasks remain open. The next active finite direction
is the characteristic-two Ferrari tensor-algebra model, retaining all
squares and using actual group collection. Its degree2 target has
order1536; the degree2,3,4 evaluations all kill K6 and all24 retained
G6 points pass. Complete binary degree5/6 F-prime correction images
have dimensions4/7, full kernel images6/9, and commutator images3/6.
Cubing every binary correction basis word preserves its binary image
and kills the entire characteristic-three degree-six core, verified
by literal induced evaluation; this supplies the exact joint comparison.

## E.24: complete joint binary and ternary Ferrari fibres

The characteristic-two calculation is complete and written in
sections/E_ferrari_two_agent.tex. All squares are retained in the actual
truncated tensor algebra. Binary degree6 has full kernel9 and F-prime
correction image7 above G6. Its exact induced cusp order is16, so the
common cusp period is144 and every multiplier lift of a retained G6
shadow is represented by1 or73. For both residues in every fibre, the
gentle rank is5, the pentagon rank5, and the combined rank6. Each has
exactly two solutions. Every one of the128 binary parameter values is
substituted to verify the affine maps; every solution passes both full
hexagons, the complete pentagon, all braids, and both full-twist equations.
The final run with the full-twist assertions took142.299s.

The common-word construction is exact. A binary basis word v cubed
keeps its binary image and kills the entire ternary degree6 core.
A ternary-plane word u raised to−2 keeps its ternary image and kills
its binary image. Both are actual F2-prime words, and every basis
comparison is checked in all36 induced coordinates. This retains every
one of the old9 ternary points with both binary solutions at both
multiplier residues. The common source is the exact fibre product over
G6, with kernel F2^9 times F3^19. There are36 finite pairs per retained
CM point and864 total. The relative N-image product and its rank97
Frattini quotients prove source generation at every point.

Binary target generation is proved without logarithms. The kernel U
of the linear S3 quotient is generated by xi1,xi2,a²,b²,(ab)³. The exact
positive-weight collector retains squares and commutators and verifies
all triangular relations, giving |U|=2^40. Its target order is
6,597,069,766,656. Full independent enumeration agrees with collection
at degrees2,3,4 (target orders1536,12288,6291456). At degree2, U has
order2^8 and its Frattini subgroup order2^3. Thus the five-generator
Frattini quotient is already detected, and unchanged degree2 braid
generators prove full generation at degree6 for every solution.

The binary and ternary targets have cyclic abelianizations of orders
dividing8 and9. Every common quotient is solvable and has trivial
abelianization, hence is trivial. Their actual joint B4 image is therefore
the full direct product, of order880,164,249,471,192,366,606,672,986,112.
The binary degree1 affine action is exactly the standard S4 permutation
action (the three generators are the adjacent transpositions on the
four explicitly ordered vectors), so the common kernel is already pure.
The full-twist orders are8,4 in the binary factor and6,9 in the ternary
factor; both multiplier residues preserve the required powers. These
exact comparisons and the family counts are retained in
code/de_ferrari_two_joint_control.json. The full profinite question
remains open. The next finite target under construction is the actual
Nielsen action on the generating-pair set of S3, so that the Ferrari
free kernel has a nonnilpotent finite image.


## E.27: exact S3 generating-pair Ferrari target

The actual simultaneous image of the Ferrari free group in S3 over all eighteen generating pairs has order108, derived subgroup C3^3, and gamma3 equal to that derived subgroup. Its Nielsen image has order162, giving a faithfully enumerated four-strand target of order17496. This free image is nonnilpotent. Nevertheless the six actual pure evaluation pairs commute and have exponent3. Therefore all six maps kill F-prime, and the induced six-coset B map is exactly B/(F-prime F^3), of order54. The exact G6 reduction kills all4656 N commutators and97 sixth powers; its N image has order3. Every commutator f has six identity values. Both unit multiplier residues modulo6 give full target generation and the required full-twist powers. Thus all24 retained points, and all their lifts, pass this target. This supplies an exact factorization limitation, not an additional cofinal lifting theorem. Formal statement: sections/E_ferrari_s3_agent.tex. Executed certificates: code/de_ferrari_s3_model.py and de_ferrari_s3_factor.py, with .out/.json/.npz.

## Primary audit: matrix versus distribution Kummer extensions

No earlier D.5/E.6 proof uses an equality between Marin's matrix cocycle and the distribution coefficient. D.5 uses the literal cyclic-cover map and identifies its negative coefficient with the arithmetic Kummer cocycle only on the Galois normalization. E.6 evaluates that literal coefficient.

Marin, arXiv:0801.2507, Section4 (printed pp.8--9), constructs its matrix cocycle for full GT; the equality with -8 kappa_2 is explicitly stated for Galois elements and obtained from Nakamura's Corollary4.13. The following sentence calls it an alternative extension, without asserting an equality of all extensions.

The cited Nakamura--Schneps, Invent.Math.141(2000),503--560, was opened in the author's uploaded full text: https://www.researchgate.net/publication/227209468_On_a_subgroup_of_the_Grothendieck-Teichmuller_group_acting_on_the_tower_of_profinite_Teichmuller_modular_groups . Section5 Definition5.1 and (5.1) define rho_2 from the abelianization of g_F. Proposition5.3 (p.523) identifies that coefficient with -A_F(-1,1) only for F in I-Gamma-prime, using relationIII-prime. The closing paragraph (p.524) identifies the Fox extension -A_F(-1,1) with Ihara's Psi_2^(0), referring to [I3] Section2.6(6) and Proposition2.2.3. Remark6.2 (pp.525--526) derives the matrix ratio beta=-8 rho_2 alpha by specializing relationIV in GL2(A_fin); its stated scope retainsIV. Opened web refs turn381view0 and turn380view2 supply these exact passages. The checked comparison chain therefore leaves the full-GT matrix/distribution equality unestablished. No finite matrix/Kummer exclusion is inferred from it.


## E.32: full binary torsion-conjugacy fibre test

All96 E.24 binary branch/line inputs pass the necessary order-two torsion test from E.30, for both lambda1 and73. They have exactly two distinct delta-prime-squared images. Both are conjugate to delta-squared already in T2,6, without a central correction; among all four central translates only exponent0 passes. The exact central-filtration algorithm retains the full centralizer at each step, with log2 dimensions40,40,38,37,34,31,27 and layer ranks0,2,1,3,3,4 in all six outer cosets. Its degree2 implementation was independently compared against all1536 target elements and the fully enumerated conjugacy class of size12. A separate program imports no conjugacy solver, rebuilds the40 polycyclic basis elements from original braid words, extracts literal B4 conjugators, and verifies all96 equalities. Hence all864 joint E.24 points pass this binary test; the9 ternary parameters have identity binary image by the verified CRT words. Formal proof: sections/E_ferrari_torsion_agent.tex. Programs: de_ferrari_two_conjugacy.py, de_ferrari_two_torsion.py, de_ferrari_two_torsion_words.py.

## A5 generating-pair target, current exact stage

The model `de_ferrari_a5_model.py` enumerates 2280 ordered generating pairs, 19 kernels modulo Aut(A5)=S5, and Nielsen orbits of sizes 9 and 10. The free image is A5^19. The exact Nielsen image has order 2159912272896000000000000; the four-strand target has order 13161635810573860462563164160000000000000000000000000000000, in a faithful 190-point representation. All six actual pure evaluation pairs are noncommuting. The complete induced 36-coordinate B image has order 16325204454686195712000000000000000000000, computed on 6840 points by `de_ferrari_a5_source.py` (162.176 s). Individual N images at indices 0,1,3,5 have order 16200000 with derived order 216000 and abelianization 75; at indices 2,4 they are perfect of order 1079956136448000000000000. The following full-image computation supersedes the initial component-only stage; no representative failure was used as a CM exclusion.

## E.29: complete A5 correction fibres and simultaneous generation

All seven exact finite programs completed successfully. `de_ferrari_a5_source_compress.py` gives a faithful compression from 6840 to 1980 points by saved intertwiners between duplicate transitive B-sets; the group order is unchanged. `de_ferrari_a5_corrections.py` computes the whole N image P, its derived subgroup C, the image K of K6, and the image of K6∩F′. The latter is exactly C: all 95 primitive integral-F-abelianization-kernel sixth-power products add no further generators. In contrast, the full sixth-power image adds a quotient K/C of order 25. The exact indices are |G/P|=72, |P/C|=75, |G/K|=216 and |G/C|=5400. Runtime 267.715 s.

`de_ferrari_a5_compare.py` independently proves C′=C and |im(F′)/C|=4. All 144 Schreier kernel words identify the actual quotient G/P with PSL2(Z/6), using s↦[[0,1],[-1,0]] and r↦[[0,-1],[1,-1]]. Reduction modulo 3 then identifies im(F′)/C with V4. Every retained E.17 G6 word belongs to one of the three actual Galois matrix cosets Mκ=[[1,−8κ],[-8κ,1+64κ²]] modulo 3, κ=0,1,2, with eight indices in each coset. All subsequent E.24 parameters preserve this coordinate. Runtime 361.120 s.

Actual χ=1 Galois elements realize each κ: the splitting field Q(ζ3,∛2) has S3 group, and its intersection with the full cyclotomic extension is exactly its maximal abelian subfield Q(ζ3). Nakamura–Schneps Theorem 2.5 therefore supplies actual fσ values in the three required cosets. This uses the theorem only on G_Q, and does not use the unproved full-GT comparison between its Kummer extension and the distribution extension. For a retained f0, the difference ρ(f0)^−1ρ(fσ) lies in C=ρ(N′). Since C is perfect and the N′ image in the retained 2/3 target is solvable, their joint image is the full product. Thus an N′ correction matches fσ in all 36 induced A5 coordinates while preserving the entire old finite point. It preserves all 432 multiplier-one points, not just one selected point per fibre. The same product argument preserves the component maps and equations after the proved solvable boundary refinements, with compactness for their inverse limits. The joint-generation claim is restricted to the exact D23 and T23 common refinements below; no additional common-source generation with a boundary modulus admitting the 5-primary quotient of G/C is inferred.

Surjectivity is proved in both actual common refinements. The three-strand image is D23×_{G/K}G: any common quotient is solvable, kills C, and then kills the normal 5-group K/C because D23 has only primes 2 and 3. `de_ferrari_a5_solvable.py` computes T_A′ of index 2 and proves T_A′ perfect; all three braid generators have the same nontrivial parity. Hence the four-strand image is T23×_{C2}T_A, and component surjectivity plus this exact common-quotient bound proves joint surjectivity. Runtime 92.029 s. Its kernel lies in PB4 because the old binary factor already retains the standard S4 map.

The formal proof is `sections/E_ferrari_a5_agent.tex`. The new correction is an existence construction from actual Galois images and exact finite subgroup surjectivity; no unevaluated literal Galois word is described as a saved numerical witness. This adds a concrete nonsolvable finite pentagon test. It does not settle the full profinite question or give cofinality.

Primary sources reopened for this step: Nakamura–Schneps author PDF `https://webusers.imj-prg.fr/~leila.schneps/newGT.pdf`, Theorem 2.5 and Remark 2.7 on manuscript p.11 (PDF index10), §2(2.1) for the Ihara convention, and §1(1.1) for the full braid action. The exact input matrices agree with the displayed modular map above. Collas, JTNB 24(2012), `https://www.numdam.org/article/JTNB_2012__24_3_605_0.pdf`, introductory braid display on printed p.607 was independently reopened: its written conjugation order is opposite to NS(1.1). The parent uses Collas's action-independent torsion classification and the actual NS action, avoiding an unsupported identification of these f coordinates.

## E.35: complete order-three torsion test on all joint fibres

The new complete conjugacy solver uses the exact kernel J of T3,6→T3,2, with base order648, class-two exponent-three kernel logarithm dimension30, and central derived dimension18. Every base conjugator is enumerated. The first equation modulo Jprime has rank8 and retains the entire22-dimensional centralizer; the exact central equation has rank12 and retains its entire10-dimensional kernel. The base epsilon class has72 elements and9 base conjugators for each. Logarithms are used only on this previously verified class-two exponent-three kernel, with no degree-six Lazard assumption.

`de_ferrari_three_torsion.py` reconstructs every one of the216 ternary parameter points and tests all9 full-twist translates. All pass. Within each indexed plane epsilon-prime is independent of both parameters; there are15 distinct values across24 indices, hence135 distinct translated targets. Exactly j=0,3,6 give conjugacy to epsilon in every case. The45 positive comparisons have actual literal B4 conjugators of lengths6–912. Runtime47.718s. `de_ferrari_three_torsion_words.py` imports no conjugacy solver: it independently substitutes all45 words, checks both multiplier equalities, and reconstructs all216 input values. Runtime26.485s. The auxiliary class-two control exhaustively compares all243 targets against all243 conjugators; its two ranks1/1 and class size9 agree.

The binary factor is settled by an elementary center induction, written in E.35: modulo the order-four full twist, the preimage of the prescribed C3 generator has normal2-group and two order-three complements. Reduction by Omega1 of the center and the explicit averaging solution w=alpha(v) over F2 conjugate the complements with the same generator orientation. Lifting and cubing kills the remaining central translate because3 is invertible modulo4. The orientation comparison is literal: epsilon maps to BA in SL2(F2), all retained triples have the same degree-two images, and lambda≡1 modulo3. Since E.24 proves the actual full product of the binary and ternary targets, the conjugators pair to prove the required equality in the joint target itself.

Thus all864 E.24 points and every compatible multiplier lift lambda≡1 modulo72 satisfy the full order-three test. The higher-lift comparison is epsilon^lambda=epsilon*z4^((lambda−1)/3), and all residues of this exponent lie in the certified translate set{0,3,6}. No fixed retained fibre is removed. The formal proof is `sections/E_ferrari_three_torsion_agent.tex`; the complete base and kernel search supplies exact failure certificates for the other six central translates.

## E.38: complete SL2(F5) central-cover Ferrari refinement

The exact universal free quotient for all76 epimorphism kernels onto SL2(F5) is SL2(F5)^19×C2². One lift of each of the19 A5 kernels gives the full perfect product; the remaining57 evaluations are recovered by the two global parity characters. The literal Nielsen action retains all38 parity-to-center cross terms, as well as the full GL2(F2) action. The actual base of the four-strand image is T_A×_(C2)S4, and its elementary kernel has dimension55, comprising19 free central signs and36 actual Nielsen cross-term directions. The four-strand target order is2^117·3^36·5^31·7².

The full36-coordinate induced source has elementary kernel44 over G_A and order2^82·3^26·5^21·7². The complete N image P and its derived image C both have kernel41; the full second-derived calculation also has kernel41, proving C perfect. The full Fprime image E has kernel42. Thus |G_L/P|=576, |P/C|=75, |E/C|=8 and |G_L/C|=43200. The exact lifted relation counts for Nprime, Nprimeprime and Fprime are20880,21640,18600. Every retained actual word DAG is independently replayed. Module commutators [C,V] alone have rank34 in V of dimension41: the remaining seven central directions are supplied by the full second-derived presentation, not omitted. The total derived-program runtime was1186.028s, including the slower base-generator search; its three lifted stages took120.787s,141.927s,68.940s. Exhaustive small-group controls compare the entire kernel sets in A4 and in the order-eight Heisenberg group, including extra-lift normal closure.

The actual Q=SL2(Z/12)/±1 comparison follows from the index576 and all97 literal N words. In SL2(Z/12), the F image has order96 and its derived image is Q8 of order8, consisting of matrices equal to I modulo4. This fixes the sign. Every retained E.17 word has one of the three exact matrices [[1,−8κ],[−8κ,1+64κ²]] modulo12 with the same complete κ=0/1/2 table as E.29. The new modular program checks every one of the24 old corrections and all13 binary/ternary basis words, with the actual cusp gauge, proving the Q value for all864 points. Independently, pi^−1(C_A)∩P=C and E_A∩P_A=C_A prove E∩P=C, so the source quotient E/C is exactly this Q8.

For every compatible profinite multiplier lambda≡1 mod72, actual Galois elements with that exact cyclotomic value realize all three Kummer values modulo3. NS Theorem2.5 applies with lambda≡1 mod12 and supplies the required signed Q value. The difference in the complete induced source lies in C. Perfectness of C and solvability of the old Nprime image give an actual discrete Nprime correction matching the entire Galois source image while preserving every old finite coordinate. This proves survival of all864 points and every retained CM fibre. It uses the arithmetic matrix theorem only on actual Galois elements and avoids the unproved full-GT matrix/distribution identification.

The half-multiplier comparison is explicit: the old cusp has order144 and x,y,z have order72; the old braid-generator orders divide8 and9. The two finite branches can be represented by1 and the actual profinite unit eta73 with p-adic entries73 at p=2,3,5,7 and1 elsewhere. All finite group orders have only those prime divisors, so every required lambda and (lambda−1)/2 power, including source permutations, is exactly the integer73 or36 power. For an arbitrary compatible profinite lambda the new component uses the same lambda as the chosen Galois element.

The complete comparison also proves joint generation. Projection identifies P/C with its A5 counterpart, so K=im(K6) has |K/C|=25, im(K6∩Fprime)=C, and |G_L/K|=1728. Every common quotient with the old2/3 source kills C and then K/C, giving exactly D23×_(G_L/K)G_L. The maximal solvable four-strand quotient has order96: after killing SL2(F5)^19, a faithful251-point representation has derived indices1,2,6,96,96. An exhaustive check of all1536 elements and all generator edges of the binary degree-two target proves its map onto this exact96-element quotient. Thus the actual four-strand refinement is T23×_(S96)T_L, and the corrected triples generate it. No extra boundary-generation assertion is included.

Formal proof: `sections/E_ferrari_sl2_5_agent.tex`. Programs and complete outputs: `de_ferrari_sl2_5_model`, `nielsen`, `source`, `N`, `derived`, `coinvariants`, `modular`, `solvable`; lifted presentation modules `de_lifted_schreier_kernel.py`, `de_lifted_schreier_extra.py`, and exhaustive `de_lifted_schreier_control.py`. The particular arithmetic correction is an existence construction from the exact product image, not a claimed saved literal Galois word. The detailed proof ledger and source searches are in `research/DE_sl2_5.md`.

Opened primary sources for this step include Guillot arXiv1407.3112v3, §2.1 Lemma2.1 and generating-pair construction; its introduction p.2 and §2.3 explicitly give GT0 and the inverse limit over all finite groups. Guillot arXiv1604.04415 Theorem1.1 addresses PSL2(q); its SL2 trace discussion does not give this induced Ferrari-source calculation. Searches included Grothendieck Teichmuller SL(2,5), GT-shadows SL Ferrari, and Guillot SL2(q). NS Theorem2.5 and equation(1.1) were reopened in the author's PDF. No claim of priority is made. The full profinite E.2/E.3 question remains undecided; this additional finite refinement supplies no cofinality theorem.

## E.38 complete certificate replay without the discovery search

The separate `de_ferrari_sl2_5_derived_replay.py` reads immutable chosen-generator records from a supplied expected directory. It reconstructs each nested literal B expression, checks both its complete component image and its faithful base permutation, freshly computes the base group order, then reruns all original main commutators, all module-basis commutators, all conjugation residuals, the full lifted Schreier presentation and normal closure. Only the slow discovery of a small base generating set is skipped. Both inclusions of the final kernel spans are checked. The executed replay took335.035s and gave identical41/41/42 dimensions and75/8/576/43200 quotient orders. Its outputs are isolated in `code/de_sl2_5_replay_check`; the original certificates are unchanged. Root's first source audit also passed mathematically; its broad file guard separately detected a different terminal-subgroup generating list and the then-active replay stdout. The terminal-subgroup comparison is by mutual containment in the same Sym(251), keeping the identical generator map and entire96-element Cayley quotient. The transient stdout is kept separate from the frozen original source data.

## E.43: the exact shared solvable quotient and simultaneous full boundary factors

`de_sl2_boundary_quotient.py` independently verifies that the literal x,y have order15 in the original1980-point A5 source. The elementary2 kernel and the exact signed modular order6 then give order30 in the SL2 source. Its F-image abelianization has order900, so the specified ordinary exponent-sum map modulo30 is an isomorphism onto (Z/30)^2. Combining it with the signed SL2(F3) map is injective modulo C, because q3 is injective on E/C=Q8. The exact7200-element F-image is therefore SL2(F3)×_(C3)(Z/30)^2, with the relation kappa3(g)=a+b modulo3.

The ten literal rank-ten Fermat Schreier words generate precisely the800-element H image Q8×C10². Its third lower-central subgroup is trivial and its exponent is20. The actual Sylow projection powers are h^5 and h^16, of orders32 and25; they commute and multiply back to h for every one of the800 elements. The exact H-generator images and all7200 F elements are retained. The code finishes in0.047s; geometry independently replayed every comparison without modifying the protected inputs, and root's isolated replay passed in0.177s with all JSON/NPZ entries equal.

These literal source maps prove that S=G_L/C is a quotient of P20=B/(gamma3(H)H^20). The Hall-coordinate CRT map identifies P20 with P4×_(B/H)P5, so it is already in E.42's full boundary family. S is the maximal solvable source quotient because C is perfect and S is solvable. Finite old common sources containing P20 are cofinal within that specified family and have exact joint image G_old×_S G_L. This closes the former5² common-quotient generation gap for the E.42 family; it does not assert generation for an unspecified family.

For a fixed arithmetic correction value c in C, each closed derived term N^[r], r>=1, maps onto C. Nested compact preimage sets give one k in their intersection mapping to c. Since N^[r+1]⊂H^[r], k lies in the full prosolvable residual R_H of H. Conversely its image is contained in C because S is solvable, so the exact map R_H→C is onto. This single k preserves every finite solvable H image: the entire retained source, both full class-two2/3 towers, and every full pro-p H factor for p>=5. Matching the new source with an actual Galois image gives all required finite hexagons and the Ferrari pentagon. The maximal common quotient S then proves generation in every actual old/new common source. Four-strand generation remains the exact T23×_(S_L)T_L comparison of E.38.

Thus every432 multiplier-one source point, every prescribed full two-adic and three-adic class-two fibre, and all the E.42 identity factors coexist with the complete SL2(F5) Ferrari test. Formal proof: `sections/E_sl2_boundary_agent.tex`. Geometry and root both read the full proof and found no substantive gap; the residual morphism and quotient typing were made explicit. This remains a specified noncofinal family for the full profinite problem.


## E.45: complete A6 kernel/outer targets

The new standalone fragment `sections/E_a6_kernel_agent.tex` proves the whole-fibre result for the exact53-kernel permutation action and its actual outer-V4 refinement. All36 source evaluations are retained. Both full commutator correction images are perfect and equal the entire F-prime image. The exact source solvable quotient is B/(F-prime F^30), with216-element common quotient B/(F-prime F^6) over D23. All864 retained points and compatible multiplier lifts survive; multiplier-one also glues simultaneously with the entire E.42 boundary family via the actual P20 quotient. The subsequent full inner/free A6 result is E48 below. Details, exact runtimes, primary-source comparison, and the preserved initial metadata-key failure are in `research/DE_a6.md`.

## E.48: full A6 source and every retained D23 fibre

`sections/E_a6_full_agent.tex` now proves the full53-factor A6 Ferrari test for all864 old points and all compatible multipliers. Its actual source has perfect normal residual C and successive solvable layers (Z/120)^2, F3^9, F2^6. The complete old correction image equals rho(gamma5 N)=rho(N-prime), with literal word preimages independently checked in both old collectors. Every fixed old fibre has18 norm values and16 generating values in the full solvable quotient; all affine freedoms are retained. The identity-only restriction reaches288 of864 points and supplies no exclusion of the other576.

The exact double-cover coefficient is c2(f_sigma)=+kappa2(sigma), proved from Nakamura--Schneps equation(2.4), Lemma2.3 and the literal c2([x,y])=-1 calculation. Its value on the complete norm kernel is the actual E/rho(N-prime) quotient parameter. Selecting the positive-root cubic Kummer value on the cyclotomic kernel and lifting the remaining difference through gamma5 N gives the complete Galois value in the new source while retaining D23. The source-generation proof uses the actual common source and its nilpotent Frattini quotients; the four-strand target is T23×_(C2)T6.

The same literal scalar agrees with all E38 positive-root labels, checked on all24 base words and every one of their864 retained old points. The simultaneous G_L/boundary source is not asserted yet: it requires its own actual combined-source morphism. The stable dependency/replay map is `research/DE_a6_replay.md`; detailed proof provenance and the remaining joint-source calculation are in `research/DE_a6.md`.
