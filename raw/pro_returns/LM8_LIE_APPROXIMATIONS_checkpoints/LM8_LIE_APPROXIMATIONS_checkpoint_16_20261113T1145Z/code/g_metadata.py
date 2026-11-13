#!/usr/bin/env python3
"""Build the Part G results/coverage/readings/report ledgers from checked text."""
from pathlib import Path
import csv,json,re
root=Path(__file__).resolve().parents[1]
sec=root/'sections'
tex=(sec/'G.tex').read_text()
info={
1:('The unrestricted D_m notation is not an intrinsic Johnson homomorphism; the correctly filtered Johnson map is injective and special on boundary-fixing automorphisms.',[], 'Modern prompt G(a)', 'An expansion is required for arbitrary homogeneous logarithmic terms; actual graded images use A_m/A_{m+1}.'),
2:('A genuine CM order-four lift gives odd vanishing and the character condition a=b modulo4; Delta and G1 have identical rational graded spans.',['G.1'],'G(a)(2),(3); CK E1','The equality is rational; no integral-index equality is asserted.'),
3:('Special derivations have an exact integral kernel presentation; degree2 is the central line Z5 ad(omega).',[],'G(a)(1); G(e)','The bracket map is integrally surjective, so all ambient modules are finite free.'),
4:('For t=X/Y, the degree2 coefficient is kappa_64/12=kappa_2/2=kappa_(1+i), and its image on Delta is Z5.',['G.3','Nakamura2013Eisenstein, Theorem6.10.3'],'G(a) coefficient; CK E3 first obstruction','Boundary inversion and tangent sign are checked; the valuation argument proves surjectivity on the actual commutator Galois subgroup.'),
5:('Every cusp-packet twist adds its Kummer cocycle to the degree2 coefficient; precisely one packet class cancels it on Delta.',['G.4'],'G(a) every packet','Restriction H1(GK,Z5(1)) to Delta is injective because the cyclotomic image contains a value differing from1 by a unit.'),
6:('The degree4 special module has three character lines, but the two outer lines vanish in the CM Galois image; only T=[F,epsilon4] survives.',['G.2','G.3'],'G(c)','This refutes the three-nonzero-components lead. Explicit primitive Lyndon vectors are verified.'),
7:('The middle degree4 coefficient equals kappa_11/48, with the determinant and published factor12 corrections in the conductor-four Soule comparison, and is nonzero on Delta.',['G.6','Nakamura1995, Corollary4.12','Nakamura2013Eisenstein, p492 Errata to N95','Ishii2025, Corollary4.10','IshiiGoto2026, Theorem1.7'],'G(c)','The lattice-eigenbasis determinant and Nakamura2013 p492 correction of 1995 (3.11.4) are retained: 12 kappa_11=d chiell22, so b0=-d chi_2^(4)/48. Polylogarithm specialization sources are checked without inferring nonvanishing from a syntomic formula alone.'),
8:('Every multihomogeneous special derivation with nonzero metabelian image has constants exactly the boundary line; this includes each epsilon_m and T.',['G.3'],'G(b) exceptional packet','Complete free-Lie/Lazard proof; marked-letter substitutions are injective by least left-word length, eliminating cancellation.'),
9:('At split primes the actual rational graded Delta image contains an unbounded family of extreme epsilon derivations.',['G.2','Ishii2025, Theorem1.5(4)','Nakamura1995, Claim4.14.1'],'G(b),(e)','The inner degree2 term is removed explicitly; no freeness conjecture is invoked.'),
10:('For every prime ell, including inert primes and2, every cusp-packet section has P_ell^(s Delta)=inertia.',['G.3','G.8','Nakamura1995, Lemma3.12 and proofCorollary4.15'],'G(b); CK E3','Nonzero metabelian arithmetic derivations exist at every prime; CM Frobenius projectors extract one weight. This is a full pro-ell assertion, not only finite-class fixed layers.'),
11:('A primitive CM eigenline lifts with open arithmetic normalizer through N4 and stops at N5.',['G.3','G.7'],'G(d); CK E2; LM3b D.5; LM section34 scan483','The sole nonzero b0 is sufficient: T(x) is not in [x,L4]. Class4 logarithmic denominators are units at5.'),
12:('A procyclic subgroup with open arithmetic normalizer has first lower-central term a nonzero boundary multiple in degree2 at every prime.',['G.7','G.11','Nakamura1994, finite-cover weight argument'],'G(d); LM3b D.4; LM section34 scan483','Finite-cover detection forces first degree1 or2 by Frobenius weights. Inert/2 homology is irreducible; split eigenlines have the degree4 obstruction.'),
13:('At every prime, a procyclic subgroup of P_ell with open arithmetic normalizer is conjugate into actual inertia.',['G.12','Nakamura1994, Theorem2.1.1'],'G(d); LM3b D.4','The degree2 first term forces the power character to be exactly cyclotomic, including on the geometric kernel.'),
14:('Ambient special modules, all CM characters and lower bracket ranks are computed exactly through even degree14; Lyndon ranks through14 are rerun.',['G.3'],'G(e); CK E3; LM3b A.7,A.12-A.16','All lower-degree brackets at14 have rank153, versus147 from even degrees only. CM bracket maps at10,12,14 are injective.'),
15:('The rational outer CM Galois dimensions through degrees2,4,...,14 are 0,1,3,3,8,11,24, with the full character multiplicity table.',['G.14','Ishii2026Graded, Theorem1.2 and Lemma1.5'],'G(e)','Uses an explicitly labelled opened2026 preprint. Its arithmetic hypotheses are independently verified; no unbounded freeness assumption. Standard genuine action adds central degree2.'),
16:('Exact embedded generator coordinates beyond degree6 and their integral arithmetic indices are not all determined. The degree8 middle line is reduced to one unique unknown scalar lambda in A8+lambda B8.',['G.14','G.15','G.21','DorigoniEtAl2026, Theorem5.4.1(v),(vii), equations5.43,5.46,7.22','HainMatsumoto2020, Proposition29.1','GotoIshii2026Coleman, Theorem1.1/Corollary5.5 and Remark5.6'],'G(e)','G.21 resolves the degree6 (3,3) line. In degree8, A8=F^3 epsilon8/120 and B8=[epsilon4,F^2 epsilon4]/2 give the exact family; the coefficient is d^3 chi4^(4)/267840. Boundary, CM/conjugation symmetry, metabelian coefficients, universal geometric membership and every verified rank through14 are independent of lambda. The exact Tate term Sigma3[8]=[epsilon4,F epsilon4]/480 has M-weight minus6 and zero constant quotient, so it does not supply the CM weight4 coefficient. Its defining lift is checked through length9. Imposing the Tate N-commutation on A8+lambda B8 would exclude every lambda, as F(A8),F(B8) have rank2. The local Coleman-Ihara formula has scalar minus6048 at (4,4) in its own normalization and still factors through the metabelian character, so it cannot detect B8 or determine lambda. Its integral use additionally needs a Coates-Wiles image lattice and the Johnson-subgroup comparison. Actual CM specialization and higher placement remain unknown.'),
17:('For the specified tangent abelian class-field factorization holds exactly at N1,N2; first failure at N3 is kappa_(1+i) ad(omega), cutting out K^ab((1+i)^(1/5^infty)).',['G.4','G.5','G.7'],'G(f)','For the cancelling packet first failure is N5, and its conductor-four cyclotomic-unit Kummer field is also explicitly given.'),
18:('The finite-idelic CM symmetry quotient is G_K^ab; the cyclotomic-kernel quotient is the norm kernel, and this describes N2 but not higher standard-tangent actions.',['G.17','ConnesMarcolliRamachandran2005, Theorem5.1'],'G(f); CM-system lead','Artin reciprocity convention is stated. Published volume11 appears in2006; source label KMSCM is Theorem5.1.'),
19:('In the full profinite group, one nonzero maximal-pro-ell image suffices to recognize a procyclic subgroup with open arithmetic normalizer as peripheral.',['G.13','Nakamura1994, Theorem2.1.1 and Lemma2.1.2','Asada2001, Lemma1'],'G(d) full profinite partial result','First recognize the actual ell-component via Nakamura, then use its full peripheral centralizer to control every other component; no full-character leap.'),
20:('Full profinite fixed subgroups and undetected procyclic normalizers remain undecided; their precise residual cases lie in the common kernel of all maximal pro-ell quotients.',['G.10','G.19'],'G(b),(d) full profinite','Finite-cover detectors were constructed and source hypotheses audited. The unresolved step is eliminating a Delta-fixed Jacobian/CM component in such a detecting cover, or obtaining a cyclotomic component for an undetected normalizer.'),
21:('The actual rational arithmetic (3,3) line in degree6 is spanned by V6=([F,[F,epsilon6]]-192Z3)/6; its coefficient is chi3/1536. The full degree6 rational embedding is explicit.',['G.7','G.14','HainMatsumoto2020, sections6-7 and20-22, Proposition29.1 and Corollary29.2','Nakamura2013Eisenstein, Theorem5.2.6 and p492 Errata','IshiiGoto2026, Theorem1.7','DorigoniEtAl2026, equations5.41,5.46,5.47'],'G(e) actual degree6 placement','The universal constant mixed Tate quotient identifies the invariant coefficient at every smooth fibre; the geometric coefficient is computed separately from the corrected raw theta character. W and relative M are distinguished: both the W-degree4 Tate component and W-degree6 invariant component come from the same one-dimensional M-weight6 source; only the quotient coefficient is transported. Exact boundary, SL2, metabelian, Pollack-tree and defining-Tate-equation checks pass. No integral image index is claimed.')}
records=[]
for ident,status,title in re.findall(r'\\begin\{statement\}\{(G\.\d+)\}\{([^}]+)\}\{([^}]+)\}',tex):
 n=int(ident.split('.')[1]); statement,deps,passage,notes=info[n]
 records.append(dict(id=ident,statement=statement,status=status,where_proved=f'sections/G.tex, {ident}',depends_on=deps,manuscript_passages=[passage],depends_on_doubtful_reading=False,notes=notes))
assert len(records)==len(info)==21
(sec/'G_results.json').write_text(json.dumps(records,indent=2)+'\n')
coverage=[]
def cov(task,requested,results,status='complete',remaining=None):
 coverage.append(dict(task=task,requested=requested,status=status,results=results,remaining=remaining or []))
cov('G(a)','Degree2, odd vanishing, equal rational graded spans, explicit tangent and every packet.',['G.1','G.2','G.3','G.4','G.5'],'complete_with_definition_correction')
cov('G(a)(1)','Determine every degree2 special derivation and continuity of its coefficient.',['G.1','G.3','G.4'])
cov('G(a)(2)','Odd-degree vanishing.',['G.1','G.2'],'complete_for_intrinsic_graded_images_and_the_specified_equivariant_expansion')
cov('G(a)(3)','Equality of Delta and G1 rational graded spans.',['G.2'])
cov('G(a).packet','Explicit coefficient for t=X/Y and every cuspidal packet class.',['G.4','G.5'])
cov('G(b)','Fixed subgroup for every packet at5, non-split primes, and full profinite.',['G.8','G.10','G.20'],'partial',['Full profinite residual fixed subgroup R^(s Delta), R=intersection kernels(pi to P_ell), is not shown trivial.'])
cov('G(b).pro5','Every pro5 packet has fixed subgroup inertia.',['G.7','G.8','G.10'])
cov('G(b).nonsplit','Every pro-ell packet at inert primes and the ramified prime2 has fixed subgroup inertia.',['G.8','G.10'])
cov('G(b).full','Full profinite fixed subgroup.',['G.20'],'Open',['Eliminate nonidentity Delta-fixed elements in R; a finite-cover homology detector can meet a CM Jacobian summand.'])
cov('G(c)','Degree4 module, characters, component cocycles and proposed nonvanishing.',['G.6','G.7'],'refuted_and_corrected',['The proposed nonvanishing of both outer lines is false; those lines are exactly zero.'])
cov('G(d)','Procyclic normalizers, exact nilpotent stopping level, full profinite version.',['G.11','G.12','G.13','G.19','G.20'],'partial',['Full profinite procyclic subgroups wholly in R remain undecided.'])
cov('G(d).pro5','No nonperipheral pro5 subgroup has open arithmetic normalizer.',['G.12','G.13'])
cov('G(d).stopping','Largest nilpotence class admitting the primitive CM eigenline.',['G.11'],'complete_r_equals_4')
cov('G(d).full','Full profinite normalizer criterion.',['G.19','G.20'],'partial',['Proved if even one maximal pro-ell quotient detects C; remains for nontrivial C contained in R.'])
cov('G(e)','Special modules, CM characters, lower brackets, arithmetic placement, and Lyndon computation through14.',['G.14','G.15','G.16','G.21'],'partial',['Exact rational embedded generator coordinates beyond degree6 and integral arithmetic indices are not all computed.'])
cov('G(e).ambient','All even ambient special modules and CM character ranks through14.',['G.3','G.14'])
cov('G(e).brackets','Exact rational lower bracket images by character through14, including odd7+7 contribution.',['G.14'])
cov('G(e).rational_dimensions','Exact actual arithmetic rational character multiplicities through14.',['G.15'],'complete_using_verified_preprint_theorem')
cov('G(e).degree6_embedding','Resolve the first repeated-character arithmetic placement.',['G.21'],'complete_over_Q5')
cov('G(e).embedded_lattice','Actual embedded arithmetic vectors and integral indices.',['G.16','G.21'],'Open',['Degree8 character(4,4) is the first remaining rational placement: its unique parameter lambda in F^3 epsilon8/120 + lambda [epsilon4,F^2 epsilon4]/2 is not determined by any verified symmetry, metabelian, or rank test through14. A specialized iterated-Eisenstein coefficient is missing. Integral indices remain undetermined.'])
cov('G(e).Lyndon','Rerun free-Lie Lyndon ranks through14.',['G.14'])
cov('G(f)','Decide abelian factorization at every N_r, first obstruction and field, CM symmetry norm kernel.',['G.17','G.18'])
(sec/'G_coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
with (sec/'G_readings.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['cote','scan','folio','equation','reading','resolution','used_by','doubtful'])
 w.writerows([
 ['Modern prompt','Part G(a)','','D_m','Degree-m part on every G1 element','Requires filtration or a specified expansion; intrinsic Johnson map is given.','G.1-G.2','no manuscript ambiguity; mathematical typing correction'],
 ['CK return','E1','','class-two involution','The genuine involution at odd prime5 kills the shear','Entire supplied proof read; order4 CM lift strengthens it. Do not transfer its integral path to prime2.','G.2;G.17','no'],
 ['CK return','E2; LM3b D.5','','eigenline normalizer','Class-two nonperipheral cyclic normalizer','Entire proof read; lifted to N4 and obstructed at N5 by the middle degree4 line.','G.11','no'],
 ['CK return','E3','','inverse limit','Terminal fixed layers do not themselves form a compatible tower','Entire proof and Lyndon algorithm read; ranks rerun through14 and full pro-ell fixed subgroup proved.','G.10;G.14','no'],
 ['C2 / LM3b','483','245','section34','Bare arithmetic normalizer proposal','Supplied discussion D.1-D.5 read; exponent gap is closed for every pro-ell group and for full subgroups detected at one prime.','G.11-G.13;G.19-G.20','no dependence on a doubtful word; original image not used here'],
 ['CK return / cote149','55-56;61','27;30','A6-A7','Cyclotomic-kernel centralizer theorem','Supplied proofs and Stix source hypotheses inspected; they do not apply to Delta over K^ab because CM Tate modules are fixed.','G.20','no'],
 ['LM3b return','A.7-A.8;A.12-A.16','','elliptic tables','Ambient, geometric universal, and arithmetic images differ','Kernel formula rederived; compare PartB18; do not equate epsilon-generated geometric algebra with specialized CM image.','G.14-G.16','no'],
 ['Modern prompt','G(c)','','three nonzero components','All three degree4 characters proposed nonzero','Actual CM automorphism forces outer two to vanish; surviving character explicitly identified.','G.6-G.7','no; lead refuted'],
 ['Modern prompt','G(f)','','first obstruction','Elliptic Soule character suggested first','For specified genuine tangent the discriminant Kummer character occurs first at N3; outer Soule term first after packet cancellation at N5.','G.17-G.18','no; lead corrected'],
 ['Nakamura2013','final PDF p492','','Errata to N95 (3.11.4)','The raw theta-product Kummer exponent equals 12 kappa_ij','Published erratum directly opened; factor12 inserted in degree4 and degree6 comparisons.','G.7;G.21','no; published correction'],
 ['Dorigoni et al2026','sections5.3-5.5','','(5.41),(5.46),(5.47),(5.53)','The degree6 arithmetic invariant has an explicit Lyndon formula','Boundary and defining-lift checks verify 5.46 and5.47; the minus sign on sigma3(b) in5.53 fails the boundary equation and is not used.','G.21','no manuscript ambiguity; exact algebra detects a published sign inconsistency'],
 ['Hain-Matsumoto2020','sections20,22,29','','Proposition29.1;Corollary29.2','The M-graded Tate section need not respect ordinary elliptic W','The ordinary degree4 and degree6 parts of Sigma3 both have M-weight minus6. Only degree6 survives modulo geometry; one-dimensionality of GrMminus6 of the mixed Tate Lie algebra calibrates the full constant coefficient from the Tate degree4 term.','G.21','no'],
 ['Mochizuki Galois Sections in Absolute Anabelian Geometry','pages5,18','','Theorem1.3;Lemma4.6','Local-field cuspidal decomposition-group recognition and Jacobian Tate-module invariants','Opened primary author PDF. The theorem preserves already-characterized cuspidal decomposition groups over local fields; it gives no new bare procyclic recognition for the residual subgroup R over the maximal abelian extension. Not invoked as a proof.','G.20 attempted route','no; hypotheses do not supply the missing inference'],
 ['Dorigoni et al2026','sections5.4,5.5.1,7.4.3','','Theorem5.4.1(v),(vii);(5.43),(5.46),(7.22)','Exact degree8 term of the Tate lift and the monodromy commutation constraint','Sigma3[8]=[epsilon4,F epsilon4]/480 is verified through word length9 and has relative M-weight minus6. It is geometric and has zero constant quotient. The Tate N-commutation has no solution in the CM family A8+lambda B8 because F(A8),F(B8) are independent; transferring it would be invalid.','G.16','no; exact failed-transfer constraint identified']])
report='''INCOMPLETE

# Part G: CM arithmetic image and inertia

| Task | Statements | State reached |
|---|---|---|
| G(a) | G.1–G.5 | Complete after correcting the unrestricted D_m notation. |
| G(b), pro-ell at every prime | G.8, G.10 | Proved for every cusp packet, including inert primes and2. |
| G(b), full profinite | G.20 | Reduced to the fixed subgroup in the common kernel R; unresolved. |
| G(c) | G.6–G.7 | Three-dimensional special module; outer two arithmetic components exactly zero; middle component explicit and nonzero. |
| G(d), pro-ell | G.11–G.13 | Proved at every prime; primitive split eigenline has maximum class4. |
| G(d), full profinite | G.19–G.20 | Proved when one maximal pro-ell quotient detects the subgroup; unresolved for C contained in R. |
| G(e), ambient/characters/brackets/Lyndon | G.3, G.14 | Exact computations completed through14. |
| G(e), arithmetic dimensions | G.15 | Exact rational character dimensions completed, using opened2026 preprint with verified hypotheses. |
| G(e), embedding through degree6 | G.21 | The first repeated-character line is explicitly determined using the universal mixed-Tate quotient and the corrected Kummer comparison. |
| G(e), higher embedded vectors/integral indices | G.16 | Not fully determined; first remaining rational placement is degree8 character(4,4). |
| G(f) | G.17–G.18 | All standard-tangent N_r decided; first cocycle and field explicit; exceptional packet also computed. |

## Strongest results

The standard tangent has a_s=kappa_(1+i), not a vanishing degree2 term. Its restriction to Delta is surjective Z5, and packet twisting adds the packet Kummer cocycle. Exactly one packet class cancels this coefficient. At degree4, the CM order-four automorphism kills the (3,1) and (1,3) components; b0=kappa_11/48 is nonzero. The conductor-four comparison is b0=-d chi_2^(4)/48: both the determinant correction and Nakamura2013 p492's factor12 erratum to 1995 (3.11.4) are necessary. The raw theta-product character is twelve times the analytic coefficient character.

The actual arithmetic line of degree6 and character(3,3) is now resolved: V6=([F,[F,epsilon6]]-192Z3)/6, with coefficient chi3/1536. Z3 is the explicit invariant derivation in Dorigoni et al2026 (5.47), equal to Pollack's tree divided by12. The proof uses the constant mixed-Tate quotient of the universal lisse realization to transport only the invariant coefficient; the geometric coefficient is separately evaluated on the CM fibre by the factorization theorem. Ordinary elliptic W and relative Tate M are distinguished: the degree4 and degree6 Tate components have the same M-weight6, and Hain-Matsumoto Proposition29.1 identifies only the latter modulo geometry. Thus the degree4 term measures the single constant coefficient without transplanting that geometric term to CM. The projector eigenbasis is explicitly rescaled to be symplectic. The raw-Theta factor12 correction is essential. The first remaining rational-coordinate question is in degree8, character(4,4).

A new free-Lie argument proves that any multihomogeneous special derivation with nonzero metabelian image has kernel precisely the boundary line. This proves the fixed-subgroup assertion for every cusp packet at every prime: Nakamura's actual metabelian nonvanishing theorem supplies a derivation at every prime, and CM Frobenius projectors isolate a homogeneous character. No integral eigenbasis is needed at inert primes or2.

For normalizers, a finite-cover detector makes the same power character occur in a cover's homology, forcing the first lower-central degree to be1 or2 by weights. Inert and2-adic CM homology is irreducible; split eigenlines are obstructed by the surviving degree4 derivation. Thus the first degree is2 and the character is exactly cyclotomic. Nakamura1994 Theorem2.1.1 then places the subgroup in actual pro-ell inertia. The class5 obstruction needs b0 alone; b_minus is zero.

In the full profinite group one nonzero pro-ell image is enough for recognition: first apply Nakamura to the actual ell-component, then use the peripheral centralizer (including prime-supported exponents) to absorb the entire procyclic subgroup. The remaining full profinite groups lie in the common kernel of maximal pro-ell quotients.

## Exact computed rows

For degrees2,4,6,8,10,12,14:

- Special dimensions: 1,3,6,13,37,99,284.
- CM-fixed dimensions: 1,1,4,5,21,45,150.
- All lower bracket ranks: 0,0,0,3,15,47,153.
- Even-lower bracket ranks: 0,0,0,3,15,47,147.
- CM lower-even bracket ranks: 0,0,0,0,4,11,41.
- Actual rational outer arithmetic dimensions: 0,1,3,3,8,11,24.
- New arithmetic generator counts: 0,1,3,3,5,5,7.

The three complete ambient CM bracket maps at10,12,14 are injective. Restricting them to the actual arithmetic spaces determines the rational dimensions without assuming freeness in unbounded degree or choosing unknown generator coordinates. The2026 generation theorem's hypotheses are checked by proving h(Q(zeta20))=1 with a Minkowski bound and an explicit norm5 element, and that K(25) has exactly two primes above5 using the ray group and Frobenius cosets.

The free-Lie ranks through14 are 2,1,2,3,6,9,18,30,56,99,186,335,630,1161. Every standard Lyndon expansion through14 has leading coefficient1; Witt character counts are checked through16 where needed for the derivation kernels.

## Programs and executions

- `g_lie_core.py`: self-contained exact Lyndon/associative algebra utilities adapted with attribution from the supplied LM3b implementation.
- `g_special.py`, `g_special.out`, `g_special_results.json`: exact ambient character kernels and lower-even brackets.
- `g_kernel.py`, `g_kernel.out`, `g_kernel_results.json`: T-kernels through degree10, and the extra odd7+7 contribution at14.
- `g_arithmetic.py`, `g_arithmetic.out`, `g_arithmetic_results.json`: exact arithmetic character dimensions, ray-class hypothesis certificates, and separating Frobenius point counts.
- `g_embedding.py`, `g_embedding.out`, `g_embedding_results.json`: explicit degree6 arithmetic vector; exact boundary, SL2, metabelian, Pollack-tree, and defining Tate-lift checks, with source normalization corrections recorded.
- `g_degree8.py`, `g_degree8.out`, `g_degree8_results.json`: exact one-parameter reduction of the degree8 middle line, including its Kummer normalization and a certificate that the verified finite tests do not distinguish the parameter. No parameter is asserted to be realized arithmetically.
- `g_metadata.py`: reproducible PartG ledgers.

All listed programs were run. Rational rank calculations are explicitly distinguished from integral saturation assertions. The finite T-kernel checks are supplementary; the infinite fixed-subgroup result uses the proof in G.8.

## Remaining obligations and approaches actually tried

1. Full profinite fixed subgroup: all primewise images are inertia, so remove the single matching profinite inertia exponent. The remaining element is in R. A finite quotient and its cyclic subgroup always give an open-cover abelianization detecting a nonzero residual element. Descending this cover makes its class Delta-fixed. However its Jacobian may have fixed CM factors (it already has E as an isogeny quotient). The missing step is a cofinal detecting-cover construction eliminating the relevant CM component, not the existence of an abelianization detector. Nakamura/Stix recognition hypotheses were opened and checked; Stix's torus-versus-abelian-variety hypothesis fails over K^ab explicitly.
2. Full profinite normalizer: every subgroup detected at one prime is now recognized. For C contained in R, a finite-cover detector allows a weight-one Jacobian line as well as weight-two boundary. No argument here excludes the weight-one alternative in all such covers. Peripheral centralizers help only after a nonzero inertia component has been located.
3. Arithmetic placement: metabelian characters and ambient bracket injectivity determine all rational dimensions through14. The degree6 ambiguity was resolved in G.21 by combining the universal constant mixed-Tate quotient with the CM elliptic-character factorization, including the factor12 erratum. The degree8 middle projection is exactly d^3 chi4^(4)/267840 times (A8+lambda B8), with A8=F^3 epsilon8/120, B8=[epsilon4,F^2 epsilon4]/2 and a unique unknown scalar lambda. The new exact program shows all boundary, CM/conjugation symmetry, metabelian, universal-geometric and rank tests through14 are independent of lambda. The further Tate-formula attack is explicit: Dorigoni equations5.46 and7.22 give Sigma3[8]=[epsilon4,F epsilon4]/480, verified against the defining lift through word length9. This term has relative M-weight minus6 and zero image in the constant quotient, so it does not supply the missing CM weight4 coefficient. The additional Tate relation [Sigma,N]=0 cannot be transported to this CM generator: N begins with minusF, and F(A8),F(B8) are independent, so it would exclude every lambda. There is no even-weight constant mixed-Tate generator to determine the coefficient by the G.21 argument. The October2026 local Coleman-Ihara formula was also specialized at (4,4), giving scalar minus6048 in its own normalization. Its character vanishes on B8, so it supplies no equation for lambda; integral indices still require the Coates-Wiles image lattice and the comparison with the eighth Johnson subgroup. Remark5.6 corrects the older Coleman-Ihara corollary, not the Theorem1.7 factorization used in G.25. Exact higher iterated-Eisenstein specialization coordinates and integral indices are still missing.
4. Earlier inert-prime and integral-Malcev-conjugacy obstacles were resolved, not left open: the general metabelian kernel lemma handles the former, and cyclotomic normalization plus Nakamura handles the latter.

## Source audit

Opened and inspected the attached Nakamura1995, Tsunogai1995 and Pollack2009 documents, the CK E1–E3 and A6–A7 proofs, and LM3b D.1–D.5/A.7–A.16. Downloaded/read Nakamura's RIMS1691 preprint of the final2013 paper, Ishii2025, Ishii–Goto2026, Ishii2026 graded Lie preprint, Nakamura1994, Bannai–Kobayashi–Tsuji2010, and the October2026 Coleman–Ihara preprint. The final2013 PDF p492 erratum was independently opened and applied. Brown2015, the supplied Hain–Matsumoto source, and the primary HTML/PDF of Dorigoni et al2026 were inspected for G.21. The latter's equation5.53 sign inconsistency is detected by an exact boundary calculation, and equations5.41/5.46 fix the used normalization. Bibliography entries identify precisely which opened results are used and which remain only attempted routes. Recent preprints are marked as such.

Downloaded third-party PDFs/TXTs in `notes/g_*` are reading material. The parent may omit those copies from the deliverable ZIP; their exact primary URLs and theorem references remain in the bibliography. No downloaded source is treated as a new mathematical artifact or as a substitute for a proof.
'''
(sec/'G_report.md').write_text(report)
print(f'wrote {len(records)} statement records, {len(coverage)} coverage rows, readings and report')
