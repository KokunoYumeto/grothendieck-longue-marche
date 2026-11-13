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
