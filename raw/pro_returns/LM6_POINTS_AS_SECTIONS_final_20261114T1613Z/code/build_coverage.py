#!/usr/bin/env python3
"""Explicit task coverage, retaining every unresolved clause as unresolved."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
rows=[]
def add(task,statements,state):rows.append(dict(task=task,statements=statements,state=state))
add('Item 1','D.1–D.11; E.4–E.12','INCOMPLETE: finiteness diagram, Stoll range, local bounds and Fermat implications proved; unrestricted global finiteness remains D.8.')
add('Item 2','B.1–B.42; F.1,F.35','INCOMPLETE: injections, deletion fibres over geometric points, affine modular cuspidality, local classification, unramification over every smooth p-adic base, the sub-p-adic image trichotomy, and the complete isotrivial theorem over finitely generated p-adic fields proved; intrinsic global point-surjectivity remains B.27.')
add('Item 3','C.1–C.19','INCOMPLETE: real curve sections, fixed groups, boundary order, counts and genus-three real-type injection proved; extra profinite involutions and remaining centralizers are C.12,C.15,C.18.')
add('Item 4','E.1–E.39','INCOMPLETE: exact extensions, full-section Fermat cuspidality using stipulated inputs, class-three criterion, evaluated rational Kummer coordinates and exact Ross-edge comparison, intrinsic finite-coefficient inverse-limit obstruction, full pronilpotent counterexamples and full-metabelian three/five-power families proved; unrestricted tower image is E.21.')
add('Item 5','F.1–F.47','INCOMPLETE: centralizers, curve-target image trichotomy, valuation corrections, lifting at potentially good base cusps and global recognition of ordinary tangent parameters by two open Hom maps proved; higher-dimensional reconstruction, field reduction and abstract fixed-point existence remain specified.')
add('Lead 1','A.1,A.4–A.7,A.26–A.28; F.35','(b), with proved replacement: exact boundary groupoid maps and relative Hom scope; the unrestricted identification and attribution are corrected.')
add('Lead 2','B.1–B.15; D.1; F.1,F.7,F.13–F.14,F.27,F.35','(a) for the exact comparison and stated known ranges; the unrestricted global section assertion is separately retained as an unresolved task.')
add('Lead 3','C.1–C.6,C.11','(a), with correction to the maximal-subgroup wording: real classification and section bijection proved in the stated form; maximum abelian rank and a smaller maximal cyclic subgroup computed.')
add('Lead 4','E.1,E.15–E.25; A.10,A.46–A.49','(b) for the literal first-Lie identification, with exact toric, metabelian, nilpotent and rational-unipotent comparison maps proved.')
add('A(a)','A.1,A.5–A.7,A.23–A.24','(a)/(b): typed category and corrected naturality; open-image rigidity and exact finite-type slimness; finite fields and unrestricted preliminary rigidity refuted.')
add('A(b)','A.2–A.4,A.23–A.26,A.37–A.45','INCOMPLETE: relative cases and number-field absolute Hom proved with stated inputs; local noninjective absolute Hom and general positive-transcendence-degree or prime kernels remain.')
add('A(c)','A.14,A.27–A.28','(a): nonrational boundary recovery, transporter, Kummer ambiguity and affine-to-proper comparison maps proved.')
add('A(d)','A.29–A.32','INCOMPLETE: all geometric axioms, every profinite multiplier, explicit minus-one action and same-handle criterion proved; two redundancies refuted; remaining implication lattice open.')
add('A(e)','A.8–A.22,A.35–A.36,A.46–A.67','INCOMPLETE: cyclotomic recognition, loop uniqueness, pro-two commutant, prosolvable commutant and exact third-to-second and fourth-to-third derived peripheral images proved; unrestricted last-layer classes and their peripheral failure proved, and arbitrary-character normalizers reduced to an exact prime-complement non-splitting extension for affine and proper curves; sparse-support residual and same-level peripheral kernel remain.')
add('B(a)','B.3–B.6,B.8; F.17–F.24,F.39,F.45–F.46','INCOMPLETE: packets, abelian fibres, ramification, local closures and intrinsic global ordinary-tangent recognition by two open Hom maps proved; every unequal-degree finite-etale variant selects exactly the rational tangents ±16; the broader automorphism-only GT formula remains F.24.')
add('B(b)','B.1–B.2','(a)/(b): semi-abelian Kummer injectivity proved from nondivisibility; false finite-generation input and larger-field injectivity refuted with explicit points.')
add('B(c)','B.7,B.10–B.15,B.28–B.30; F.1,F.35','INCOMPLETE: exact six axioms, geometric implications and local instances proved; over the geometric locus deletion/configuration fibres are fully determined; intrinsic unrestricted global admissibility remains.')
add('B(d)','B.7–B.10,B.13,B.19,B.27,B.32–B.33,B.38–B.42','INCOMPLETE: finite p-adic fields and exceptional complete types computed; generic sections over every smooth p-adic base descend uniquely to relative sections, the sub-p-adic trichotomy holds, and the isotrivial section theorem is complete over finitely generated p-adic fields. B.42 exhibits a closed-fibre-invisible Tate tower; nonisotrivial algebraic realization remains.')
add('B(e)','B.16–B.18,B.23–B.24,B.26–B.27,B.29–B.30,B.32–B.35,B.38–B.42','INCOMPLETE: constant-family decomposition, proper local graph bijection, universal punctured obstruction, tautological nonlifting and generic/relative group-section bijection over all smooth p-adic bases and full isotrivial realization proved; the exact Tate-cover obstruction to a closed-fibre argument is computed. Nonisotrivial realization and arbitrary moduli finite covers remain.')
add('B(f)','B.19,B.25,B.27–B.30,B.36–B.37; F.38','INCOMPLETE: necessary moduli tests, local equivalence and nonrealizability of the entire closed stable-boundary packet set proved; global type (0,4), intrinsic sufficiency and unrestricted stack section existence remain the identified section problem.')
add('B(g)','B.20,B.31; C.7','(b), with proved replacement: complex embeddings produce the lattices; the oriented stabilizer is trivial and the unoriented stabilizer is the exact archimedean decomposition group.')
add('C(a)','C.3–C.6','(a): discrete and profinite real section bijections, all-genus fixed groups and exact boundary incidence/cyclic order proved; cusp sign collision corrected.')
add('C(b)','C.7','(a): typed prediscretization, complex-conjugation and archimedean-place bijections proved.')
add('C(c)','C.8–C.9','(a): localization compatibility, three tripod involutions and all six tangential identifications explicitly computed and checked.')
add('C(d)','C.1,C.10–C.19','INCOMPLETE: real counts, all-genus marked injection, twisted nonabelian-cohomology fibres, hyperelliptic genus-three range and five positive-oval congruence centralizers proved; fixed-point-free N4 density and extra full-profinite classes remain.')
add('D(a)','D.1–D.3','(a): exact implication/equivalence diagram and complete abelian/Selmer calculation, with explicit infinite examples.')
add('D(b)','D.4','(a), using the stipulated local theorem: modular and Stoll-range finiteness with explicit genus-two and genus-three curves.')
add('D(c)','D.5–D.11','INCOMPLETE: local finiteness and strong-density rigidity derived; uniformity obstruction exhibited; global pro-three nongeometric section constructed; literal least quotient refuted in general. Global localization fibres remain open.')
add('E(a)','E.1–E.4','(a): extensions (371)–(373), their exact kernels and section maps, equivariant splitting and the Fermat implication proved.')
add('E(b)','E.5,E.13–E.39','INCOMPLETE: integral class-two origins, class-three lift test and fibres, explicit failure at class three, rational Kummer values 1/3 and 1/2, exact Ross-edge comparison, integral detector, zero-abelian obstruction at19, intrinsic finite-coefficient inverse-limit failure, full pronilpotent counterexamples and full-metabelian families at every three/five-power level proved. E.39 computes the exact torsion kernel of the compact/unit path comparison. The Ross value, actual integral path data and complete mixed-prime image remain E.21.')
add('E(c)','E.6–E.12','(a), using stated checked/preprint inputs and the stipulated local theorem: full-section cuspidality for all odd exponents at least three; even plus curves have no real section; prime exponents three and five included.')
add('F(a)','F.1,F.3–F.4,F.30–F.31,F.35; A.1–A.7,A.26; B.10–B.13','(a): explicit comparison diagram and curve-target equivalence; added cyclotomic-kernel precision and the exact boundary shrinkings identified.')
add('F(b)','F.1–F.6,F.29–F.34','INCOMPLETE: (1)–(5) proved in the stated corrected form with local input; smallest remaining higher-dimensional reconstruction case retained at (6).')
add('F(c)','F.1,F.6,F.36–F.37','INCOMPLETE: cyclotomic precisions and exact known field-reduction ranges proved; generic proper-family descent remains equivalent to a specified non-open curve-to-surface reconstruction problem.')
add('F(d)','F.7–F.12,F.41,F.47','INCOMPLETE: continuous fixed-point comparison, uniqueness, cyclotomic nonsplitting and descent obstruction proved; literal discrete assertion refuted and repaired; discontinuous finite-form descent refuted directly on every open subgroup of the cyclotomic kernel, while the constructed action still has exactly one fixed pro-point; universal abstract fixed-point existence remains open.')
add('F(e)','F.13–F.15,F.25–F.28,F.37–F.38,F.40,F.42–F.44','INCOMPLETE: one-variable equivalence, valuation structure/finite-residue qualification and proper/good-boundary polycurve lifting proved; arbitrary-rank compatible valuation and bad-boundary induction remain.')
add('F(f)','F.16; A.19–A.22,A.35–A.36','(a) for the requested checked potentially-good-marked-reduction theorem; later tasks assigned by the prompt to ANABELIAN_149_PUSH are recorded without claiming its missing return.')
add('F(g)','F.17–F.24,F.39,F.45–F.46','INCOMPLETE: extension/torsor frame, local-global tests and their exact unit defect, four-puncture transport, smooth-trait specialization and intrinsic ordinary-tangent recognition by two open Hom maps proved; all unequal-degree finite-etale tests over Q select exactly ±16; the general automorphism-only GT parameter relation remains.')

# Explicit nested tasks, including the prompt's added numbered blocks.
for name,ids in [('I','A.3,A.26'),('II','A.3,A.26'),('III','A.3; B.7,B.27; F.3,F.30'),('IV(a)','A.3,A.23,A.26'),('IV(b)','A.2,A.23'),('IV(c)','A.3,A.26'),('IV(d)','A.3,A.25,A.26')]:
    add('A(b), case '+name,ids,'Exact case reduction proved; case III retains the global point-source assertion recorded in Part B.' if name=='III' else '(a): exact hypothesis and reduction proved in the cited statement.')
for task,ids,state in [
 ('A(a), slimness in characteristic p','A.24','(a)/(b): positive-transcendence-degree finite-type fields proved slim; finite-field counterexample retained.'),
 ('A(b), absolute Hom over number fields','A.37–A.38','(a), using the stipulated unrefereed absolute Galois Hom theorem and the checked open-map step.'),
 ('A(b), absolute Hom over p-adic fields','A.39–A.40','INCOMPLETE: dimension-zero counterexample and local curve Isom/injective-open cases proved; noninjective open Hom remains.'),
 ('A(b), positive-transcendence-degree kernel','A.41–A.42,A.45','INCOMPLETE: constant kernel, divisorial inertia and universal-moduli congruence-kernel formula proved; arbitrary-family exact kernel remains.'),
 ('A(b), pro-prime kernels including two','A.43–A.45','INCOMPLETE: nontriviality at every prime and the exact odd regular-prime tripod range proved; full description elsewhere remains.'),
 ('A(e)(1)','A.14,A.17','(a): exact cyclotomic normalizer criterion and transporter proved.'),
 ('A(e)(1 bis)','A.16–A.17; F.1','(a): centralizer form and its precise comparison to (1) proved.'),
 ('A(e)(2)','A.19–A.22,A.35–A.36,A.50–A.53,A.61–A.65','INCOMPLETE: CM pro-prime and detected-prime cases proved; residual full-profinite group narrowed, cofinite support and no-CM normalizer fields settled, and virtual splitting reduced to an exact pro-prime-to-ell kernel extension; proper-curve replacements proved. Sparse-support existence remains.'),
 ('A(e)(3)','A.15','(a): unique Galois-invariant cyclotomic loop structure proved.'),
 ('A(e)(4)','A.18,A.26','(a): exact local full-profinite cusp-recovery replacement and dominant full faithfulness proved.'),
 ('A(e), pro-two commutant','A.8','(a): full pro-two tripod commutant is S3 by the exact relative Hom construction.'),
 ('A(e), least solvable length','A.9–A.12,A.46–A.67','INCOMPLETE: length one computed, length two has a closed profinite-unit subgroup of the commutant, three-layer images and prosolvable limit settled; the third-to-second and fourth-to-third peripheral images are exactly S3, and every one-layer projection is elementwise class-preserving after its cusp permutation is removed. An unrestricted last-layer family fails the peripheral test and normal Haar blocks cannot remove that defect; the same-level peripheral kernel remains unresolved.'),
 ('B(c), axiom (1)','B.13','(a) for geometric actions; intrinsic scope and quantifiers retained.'),
 ('B(c), axiom (2)','B.13','(a) for geometric actions by the exact filling map.'),
 ('B(c), axiom (3)','B.10,B.13; F.1','(a): fixed group vanishes for every full section over the stated finite-type or local field.'),
 ('B(c), axiom (4)','B.13','(a) for geometric outer actions by a closed point and finite base extension.'),
 ('B(c), axiom (5)(a)','B.13,B.29','(a): deleted-point exclusion and exact full-section fibre proved.'),
 ('B(c), axiom (5)(b)','B.13,B.29','(a): injectivity on the geometric locus proved.'),
 ('B(c), axiom (5)(c)','B.7,B.13–B.15,B.29','INCOMPLETE globally outside the specified finite-descent range; local and geometric-locus lifting proved.'),
 ('B(c), axiom (6)','B.12–B.13,B.30','INCOMPLETE in unrestricted intrinsic form; geometric/configuration descent proved; fixed-kernel-only implication refuted by an executed finite example, agreeing with scan421.'),
 ('B(c), scan431–433 (a)','B.10–B.11; F.1','(a): full-group and cyclotomic-kernel fixed groups computed separately through the exact restrictions.'),
 ('B(c), scan431–433 (b)','B.13,B.29','(a) on the geometric locus; unrestricted intrinsic assertion retains B.27.'),
 ('B(c), scan431–433 (c)','B.13,B.27','INCOMPLETE: geometric/local ranges proved; intrinsic global admissibility remains.'),
 ('B(c), scan431–433 (d)','B.16–B.17,B.29–B.30','(b) for unrestricted families, with exact deletion/configuration replacement proved.'),
 ('B(c), equation (25)','B.28; C.10','(b) for unrestricted lifts: explicit collision over Q((t)); corrected admissible/geometric domain proved.'),
 ('B(d), positive transcendence degree over Qp','B.27,B.38–B.42','INCOMPLETE: generic/relative section bijection for proper smooth families over every smooth p-adic base proved, and the geometric-image trichotomy extended by exact countable descent. The isotrivial theorem is complete; B.42 proves an exact failure of the closed-fibre finite-cover realization principle. Nonisotrivial realization remains.'),
 ('B(e), finite étale multisections','B.17–B.18,B.24,B.27','INCOMPLETE: tautological cusp nonlifting survives all finite étale covers; explicit low-genus multisections constructed; arbitrary new sections unclassified.'),
 ('B(e), n=0 and g≤2','B.23–B.24','INCOMPLETE in the full quantified range: unpointed genus≥3 obstruction and explicit elliptic/genus-two covers proved.'),
 ('Added cote148 scan43','B.21','(a)/(b): pointwise algebraic-point section germ proved; universal rational-descent interpretation refuted; both textual alternatives remain provisional.'),
 ('Added cote143 scan2','B.21','(a): exact constants extension and finite descent/effectivity qualification stated and proved.'),
 ('Added cote143 scans4–5','B.1–B.2','(a) over the stated finite-type fields: point determined by germ through semi-abelian Kummer maps; exceptional-field limits explicit.'),
 ('Added cote143 scans6–8','B.22; F.17,F.25','(a): curve boundary inertia and normal-crossing replacement with Chern transgression and specified inertia lattice proved.'),
 ('Added cote143 scan12','B.22','(a): exact finite-cover maps and compatible Kummer boundary data proved.'),
 ('Added cote143 scans29–31, two-point stabilizer','A.33–A.34','(a)/(b): stabilizer is G_Q(sqrt(-3)) for one chosen root, contained in ker Delta; asserted containment of C^phi refuted by complex conjugation. Unordered-root variant also computed.'),
 ('D(c), least quotient','D.9–D.11','(b) in the stated quotient category: two explicit incomparable C2 geometric quotients have no least successful common quotient; locally soluble trivial quotient and a global pro-three failure are proved.'),
 ('LM7-E.23(i)','E.18–E.21,E.23–E.39','INCOMPLETE: exact class-three image criterion and all fibres; whole zero-abelian slice reduced to one arithmetic class; two rational Kummer coordinates evaluated as1/3 and1/2, remaining elliptic class identified with the Ross cup edge, integral detector and explicit zero-abelian local/inverse-limit obstructions proved. E.39 gives the exact lost path torsion, (F3)^8 over Q(zeta3) and (F3)^3 over Q. The Ross value, actual integral torsion data and complete image remain.'),
 ('LM7-E.23(ii)','E.20–E.21,E.37','INCOMPLETE: explicit restored-kernel obstruction, class-three counterexample and zero-abelian counterexample at19 proved; complete lift image from the two small quotients remains.'),
 ('LM7-E.23(iii)','E.5,E.16,E.21–E.22,E.31–E.34','INCOMPLETE: even-real obstruction, noncuspidal full pronilpotent sections at every three/five-power level and full-metabelian zero-abelian families of rank (n²−1)(n²+3)/4 at every three/five-power level proved; complete section sets and the other odd levels remain.'),
 ('LM7-E.23(iv)','E.13–E.15,E.17','(a): exact CM local-order densities, polarization/cross term, and actual quartic coefficient map/origin proved, with executed finite and symbolic certificates.'),
 ('F(b)(1)','F.1–F.2','(a): geometric morphisms imply both centralizer readings by the proved curve and fibration comparisons.'),
 ('F(b)(2)','F.4','(a): open curve-target Hom and condition b proved in the exact range.'),
 ('F(b)(3)','F.3,F.30','(a): point-source form and universal curve-target form reduced exactly to F2.'),
 ('F(b)(4)','F.3,F.17–F.18','(a): cusp-factor maps fail b; unit construction and openness comparison proved.'),
 ('F(b)(5)','F.29–F.31','(a), using the stipulated local theorem: geometric image is open, trivial, or nontrivial cusp inertia; b excludes the last branch, giving the requested exact reduction.'),
 ('F(b)(6)','F.5–F.6,F.32–F.34','INCOMPLETE: precise Hoshi/Schmidt–Stix/HSS ranges and dimension-two counterexample to open-image dominance; non-product surface reconstruction with uncontrolled kernel remains.'),
 ('F(d), added cyclotomic nonsplitting/descent','F.10–F.12','(a)/(b): no open cyclotomic quotient splits; exact normalizer obstruction; explicit invariant cusp class 1+i has order-two failure of descent.'),
 ('F(e)(1)','F.13,F.27','(a)/(b): exact one-variable equivalence and centralizer test; formulas (32),(33) refuted with L and proved with U.'),
 ('F(e)(2)','F.14,F.27,F.37','(a) for the exact implications and their field quantifiers; the two cited Bresciani titles/identifiers are one paper; universal unproved assertion is not assumed.'),
 ('F(e)(3)','F.15,F.25–F.26,F.40','INCOMPLETE: full inertia and coarsening formula, finite-residue criterion and explicit infinite-residue/identical-inertia examples proved; general compatible valuation reconstruction remains.'),
 ('F(e)(4)','F.15,F.28,F.38,F.42–F.44','INCOMPLETE: proper intermediate bases and potentially good marked reduction over a selected cusp proved; bad marked reduction requires a missing compatible component/log-valuation selection.'),
 ('F(g)(1)','B.3; F.17','(a): normal-line Chern extension, two torsors and frame injection with sign conventions proved.'),
 ('F(g)(2)','F.18','(a): cocycle-twist automorphisms and the ambient packet-coordinate injection proved.'),
 ('F(g)(3)','F.19','(a): rational local geometricity plus almost-all integrality criterion proved through actual Kummer maps.'),
 ('F(g)(3 bis)','F.19–F.22','(a)/(b): exact completed-idele decomposition, real sign and unit obstruction; unrestricted local-family version refuted.'),
 ('F(g)(4)','F.19–F.20','(a)/(b): completed units supply the local-global defect; one chosen infinite-order unit need not exhaust it.'),
 ('F(g)(5)','F.23–F.24,F.39,F.45–F.46','INCOMPLETE: smooth-trait specialization, prescribed four-puncture transport and global recognition of all ordinary tangent parameters by two open Hom maps proved; all unequal-degree finite-etale tests select precisely ±16 over Q; the general automorphism-only GT relation remains.'),
 ('Added LM5 topoi and normal-tube comparisons','B.22; F.17,F.25,F.38,F.42–F.43; source audits','The used normal-tube, Chern and flag-inertia maps are checked with exact hypotheses. Topos fullness claims are not used to infer fundamental-group fullness; the source audit records their different specified morphism data.'),
 ('Added LM8 finite/nilpotent inverse limits','E.16,E.18,E.20–E.22,E.38; A.47–A.49','(a) for each used transfer: compact nonabelian H1 tower stated; unrestricted continuous H2 uses the literal nonclosed image. E.38 gives an actual intrinsic cubic zero-abelian section whose obstruction vanishes at every finite coefficient level and is nonzero continuously.')]:add(task,ids,state)
(R/'coverage.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'coverage_rows':len(rows)}))
