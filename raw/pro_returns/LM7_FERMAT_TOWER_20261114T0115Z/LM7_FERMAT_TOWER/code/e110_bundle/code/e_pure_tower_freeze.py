#!/usr/bin/env python3
"""Retain the complete pure tower proof, exact arithmetic and positional maps."""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parent.parent
LEDGER=ROOT/'ledger'
LEDGER.mkdir(exist_ok=True)
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,value):
    (LEDGER/name).write_text(json.dumps(value,indent=2)+'\n')

proof=ROOT/'sections/E_pure_tower_complete.tex'
program=ROOT/'code/e_pure_tower.py'
summary=ROOT/'code/e_pure_tower.json'
d=json.loads(summary.read_text())
assert d['status']=='PASS'
assert d['actual_character_matrix']==[[2,2,2],[2,2,0],[2,0,2],[0,2,2]]
assert d['ordinary_unit_image_rank']==3
assert d['pure_plus_dimension']==1 and d['minus_dimension']==2
assert d['all_character_vectors']==27
assert d['full_positional_toric_inverse_checks']==531441
assert d['eligible_pure_root_transition_checks']==792
assert summary.read_bytes()==(ROOT/'code/e_pure_tower.out').read_bytes()
for name,digest in d['input_sha256'].items():
    assert sha(ROOT/'inputs'/name)==digest
tex=proof.read_text()
assert [int(n) for n in re.findall(r'\\tag\{E110\.(\d+)\}',tex)]==list(range(1,25))
assert len(re.findall(r'(?m)^\\\[$',tex))==len(re.findall(r'(?m)^\\\]$',tex))==24
assert not any(ord(c)<32 and c not in '\n\t' for c in tex)
gp=[json.loads(s) for s in (ROOT/'code/e_pure_tower_base_gp.out').read_text().splitlines() if s.startswith('{')]
assert gp[-1]=={'type':'completion','status':'PASS'}
assert gp[0]['certification_flag']==0 and gp[0]['certification_return']==1

save('e_pure_tower_results.json',[{
 'id':'E.110','status':'Proved',
 'statement':(
  'All three-primary class groups of M_d=Q(zeta3,17^(1/3^d)) and '
  'F_d=Q(17^(1/3^d)) vanish. Three explicit ordinary units give the full '
  'four-place reciprocity hyperplane at every height through the actual '
  'Kummer corestriction norm square. The adjacent ordinary-unit norm '
  'cokernels are C3^3 over M and C3 over F. Every compatible pure divisor '
  'has a coherent completed multiplicative lift. The entire pure norm '
  'system is a split extension of Z3^3 plus the restricted module at '
  'primes with v3(ord_p17)=0 by a countably infinite product of Z3, with '
  'specified character and divisor maps. Combining it with E107 '
  'evaluates the complete global H section set with first class '
  'kappa3(17), and with every unit multiple of that first class. '
  'The exact second toric image is the restricted Kummer module on '
  '{3,17} and primes with v3(ord_p17)<=1; every fiber and inverse '
  'coordinate map is given explicitly.'),
 'where_proved':'sections/E_pure_tower_complete.tex, E110.1--24 and complete proof; code/e_pure_tower.py and e_pure_tower_base.gp with complete outputs and binary certificate.',
 'depends_on':['E.38','E.46','E.65','E.69','E.72','E.88','E.107',
               'E_MilneCFT','E_LemmermeyerAmbiguous','E_KatoUniversalNorms'],
 'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178, equations371--379, through the actual positional norm and scaled toric maps.'],
 'depends_on_doubtful_reading':False,
 'notes':(
  'The all-level class induction uses a proved norm square and the finite '
  'three-group fixed-point argument. The pure compact unit group is '
  'evaluated with actual finite-level norm-character maps and a chosen '
  'Pruefer basis; no stabilization of a finite unit projection is '
  'asserted. Compactness is applied only to unit fibers, not to the '
  'restricted divisor module. The global H result is complete at the '
  'specified first classes. Its image from intrinsic metabelian/marked '
  'sections is governed by their actual quotient maps and is not '
  'identified with the whole H set.')
}])

save('e_pure_tower_coverage.json',{
 'statement':'E.110',
 'addresses':[{
  'task':'Part E(c),(d), Item2/Lead3 through the actual H quotient',
  'status':'Complete pure positional factor and full fixed kappa17 H section set, including unit multiples',
  'exact_maps':[
   'Actual Kummer corestriction with N(alpha_d)=alpha1 at every labeled completion.',
   'Ideal extension followed by norm equals2 from F_d to M_d.',
   'Complex-conjugation invariants of the exact ordinary-unit norm sequence.',
   'Completed principal-divisor sequence and compact-fiber coherent lifting.',
   'Character direct limit under the transposes of the actual unit norm matrices.',
   'Pure divisor product splitting and its coordinate-change homomorphism.',
   'The literal E107 phase combined with the two pure three-prime valuations.',
   'Kummer-Shapiro total-norm cube condition and the scaled toric map.',
   'Arithmetic-equivariant H automorphism (a,v(T)) to (r*a,v(T^r)) for unit r.']}],
 'closed_previous_steps':[
  'All pure tower three-class groups and adjacent ordinary unit norm cokernels are evaluated.',
  'All completed compatible pure divisors lift coherently.',
  'The separate pure norm factor left by E107 is fully evaluated as a topological group with exact maps.',
  'The entire fixed-first kappa17 H toric image and every section fiber are evaluated.',
  'The E107 pure=1 phase restriction is transferred by an explicit pure3 valuation correction, including the kappa7 witness.'],
 'remaining':[
  'The H section sets for first classes outside the proved families, including nonunit multiples of kappa17, remain separate.',
  'The complete intrinsic metabelian and marked-depth image over these H sections remains the residual problem recorded in E23.',
  'No numerical ordinary-unit basis at every higher individual field, or numerical description of each finite-level projection of the coherent unit kernel, is asserted. These are not needed for the proved full product and toric fiber maps.']
})

save('e_pure_tower_source_evidence.json',{
 'statement':'E.110',
 'sources':[
  {'key':'E_MilneCFT','url':'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
   'opened_passages':[
    'III Section2 formulas29,30 with their proof, and Theorem3.1 complete Res/Cor cup-product compatibility: turn925view3 and turn930view4.',
    'III Section4, Kummer pairing and Theorem4.4 with proof: turn927view3.',
    'VIII Theorem3.1, complete cyclic Hasse norm proof: turn932view0.'],
   'usage':'Exact common-root local Kummer norm square, arithmetic Artin calibration and the local-global kernel for cyclic field norms.',
   'precision':'The proof uses the proved projection formula and inv composed with Cor equals inv. It does not claim a complete printed proof for III Lemma3.2, which says Proof.To be added.'},
  {'key':'E_LemmermeyerAmbiguous','url':'https://arxiv.org/pdf/1309.1071',
   'opened_passages':[
    'Theorem1 both formulas, Proposition1 and its full ideal Hilbert90 proof: turn923view0.',
    'Complete ideal/Herbrand derivation through the end of Section3: turn925view2, turn932view3; source relies on the stated standard unit Herbrand theorem.'],
   'usage':'The exact ambiguous three-class induction and actual ordinary-unit norm quotient.',
   'precision':'The already recorded Am_st/Am typo in the Proposition1 surjectivity paragraph is handled by its actual ideal map. Only the ambiguous quotient is used.'},
  {'key':'E_KatoUniversalNorms','url':'https://ems.press/content/book-chapter-files/27477',
   'opened_passages':[
    'The actual coherent definition and Theorem1.1(1): turn925view0.',
    'Sections2.2--2.6, actual norm cohomology and divisor comparisons: turn925view1 and turn926view0.',
    'Section3.2, unconditional rank computation from the torsion cyclotomic module: turn926view1, lines395--428.',
    'Proposition4.2 and its proof Sections4.3--4.6: turn927view0--1 and turn932view1.',
    'Theorem5.1/Corollary5.2 and the complete proof in Sections5.4--5.5: turn927view2 and turn932view2.'],
   'usage':'Unbounded actual finite-level ranks of the coherent pure ordinary-unit kernel, via restriction from full false-Tate coherent three-unit norms.',
   'precision':'The application is Theorem1.1 part1, not the one-prime part2. The pure field has two places over3; the exact rank is obtained from Section3.2 and its proof without a conjectural regulator assertion.'}
 ],
 'internal_exact_inputs':[
  'E65: literal pure fields, two3-prime labeling, complete local wild norm quotient and certified first ordinary-unit norm.',
  'E72: actual surviving prime divisor branches and residue-degree norm transitions.',
  'E69: coherent norm definitions and actual recursive complex unit kernel maps.',
  'E88 and E107: actual complex class phase, full complex divisor/unit coordinates and the normalized phase -sum ell*t/3.',
  'E46 and E38: actual positional Kummer-Shapiro comparison, first cocycle and scaled toric map.'
 ],
 'author_arithmetic':'PASS. The finite certification, complete four-character inverse, exact unit identities, genuine norm rows and all toric inverse outputs are retained.',
 'peer_status':'Focused local corestriction/class-induction mechanism checked by a_structure; complete written proof sent for peer/root audit. No unreceived full audit is asserted.'
})

save('e_pure_tower_dependencies.json',{
 'portable_rebuild':'python code/e_pure_tower.py --gp /absolute/path/to/gp',
 'existing_workspace_command':'python research_e110/code/e_pure_tower.py --gp research_e52/vendor/pari-2.19.0/gp',
 'finite_recheck_without_PARI':'python code/e_pure_tower.py',
 'Python_dependencies':['sympy'],
 'PARI_version_used':'2.19.0; official source build already retained with E52',
 'actual_binary':'code/e_pure_tower_base.bin',
 'binary_contents':'[certified M1 BNF, alpha, zeta, three explicit units, actual certified unit coordinates, all3 primes, all17 primes]',
 'immutable_inputs':[{'path':'inputs/'+n,'sha256':h} for n,h in sorted(d['input_sha256'].items())],
 'old_BNF_status':'Original superseded sessions24024/40565 were stopped with actual exit130 and retained in E101. No duplicate upper BNF was started; only the new small degree6 M1 base certification ran.',
 'history_routing':'Exact exploratory sources retain their original workspace-relative paths; their complete outputs and original dependencies are preserved under code/history/initial_exploration. The final two-source rebuild is portable and self-contained apart from the three retained inputs.'
})

save('e_pure_tower_computation_status.json',{
 'statement':'E.110','status':'PASS','actual_final_exit_code':0,
 'main':'code/e_pure_tower.py','stdout':'code/e_pure_tower.out','JSON':'code/e_pure_tower.json',
 'GP':'code/e_pure_tower_base.gp','GP_stdout':'code/e_pure_tower_base_gp.out',
 'unconditional_certification':'bnfcertify default flag0 returns1',
 'three_primary_character_image_rank':3,
 'image_vectors_and_inverse_checks':27,
 'actual_mixed_unit_checks':27,
 'tested_rational_primes':166,
 'actual_pure_root_transition_checks':792,
 'full_positional_toric_inverse_checks':531441,
 'retained_failures':[
  {'source':'code/history/e110_first_certificate_failure.py','output':'code/history/e110_first_certificate_failure.out','exit_code':1,'cause':'All arithmetic assertions had passed; JSON serialization of SymPy One failed. The corrected source converts the two exact matrices to Python integers.'},
  {'source':'code/history/initial_exploration/history/pure_cyclotomic_json_failure.py','output':'code/history/initial_exploration/history/pure_cyclotomic_json_failure.out','exit_code':1,'cause':'Initial exploratory matrix JSON serialization; corrected exact integer export retained.'},
  {'source':'code/history/initial_exploration/history/pure_m1_basis_domain_failure.py','output':'code/history/initial_exploration/history/pure_m1_basis_domain_failure.out','exit_code':1,'cause':'The exact inline Groebner calculation used the default integer coefficient domain. Its actual tool stdout is preserved verbatim from chunk348335; the successful QQ-domain version and complete output are retained.'}
 ],
 'initial_exploratory_denominator_field':'The original small GP export printed denominator(polynomial)=1. That unused auxiliary field is corrected in the final GP to the lcm of coefficient denominators; all rational coefficients and exact unit computations were preserved.',
 'proof_vs_computation':'All-height class vanishing, coherent divisor lifting and compact-unit product coordinates are proved mathematically. The finite code certifies actual arithmetic inputs and coordinate maps; it does not infer an infinite statement from a finite table.'
})

(LEDGER/'e_pure_tower_refs.bib').write_text(
 '% verified: E110 reuses E_MilneCFT, E_LemmermeyerAmbiguous and E_KatoUniversalNorms. Exact freshly opened theorem/proof passages and the new use of Kato1.1(1), Section3.2, are recorded in e_pure_tower_source_evidence.json. No duplicate bibliography entries.\n')
(LEDGER/'e_pure_tower_report.md').write_text("""# E.110 — The complete fixed-seventeen H section set

Every three-primary class group in the pure radical tower vanishes.
This provides a coherent lift of every compatible pure divisor and,
combined with E107, evaluates the entire H section set with first
Kummer class kappa3(17), including every second toric fiber.
The exact arithmetic automorphism (a,v(T)) -> (r*a,v(T^r)) gives
the same complete evaluation for every unit r in Z3.

## Arithmetic input and all-level proof

The three literal M1 units have four local characters

    2 2 2
    2 2 0
    2 0 2
    0 2 2

at the three labeled places over3 and the place over17.
The first three rows have determinant -8, so the image is the
entire product-one hyperplane. The local norm of alpha_d to
alpha1 and the exact Kummer projection formula preserve those
characters at every height, with no degree multiplier.

There are four totally ramified places at each vertical step.
Chevalley's formula therefore gives unchanged ambiguous
three-class order. The initial M1 three-class group is zero
by a separate one-ramified-prime argument, and the finite
three-group fixed-point lemma proves that the full groups
remain zero. Extension and norm with composite2 give the
pure F_d assertion.

The same exact ambiguous/strongly-ambiguous sequence gives
ordinary-unit norm cokernels C3^3 over M and C3 over F.
The proof retains their actual local maps. In particular it
does not replace the genuine first pure unit norm row
(0,3,0,0) by a surjective map; the next wild character row
is (0,2,0,0).

## Entire pure positional factor

Every completed divisor is principal because the finite class
group has order prime to3. Compatible completed divisors lift
coherently by the finite intersection property applied to
compact ordinary-unit torsors.

The surviving divisor coordinates are the two three-prime
chains, the seventeen chain, and one degree-one chain at
each prime p with v3(ord_p17)=0. Their exact rational norm is

    (B,C,e,t) -> 3^(B+C) 17^e product p^t_p.

The infinite prime exponents form the restricted, prodiscrete
multiplication completion. The unit kernel is compact and
has a specified topological isomorphism with a countably
infinite product of Z3: choose a Pruefer basis of its actual
character direct limit under transposed unit norm matrices.
Finite character equations give the forward map and unique
inverse. Its infinite rank follows unconditionally from
Kato1.1(1) and the exact rank computation in Section3.2,
through restriction to the actual pure norm chain.

## Full second toric image and inverse

The allowed prime support is precisely {3,17} together with
the primes whose 17-residue order has three-part at most3.
For an arbitrary target with coefficients B3,B17,r_p, put

    t_L=3*r|P1, t_F=3*r|P0,
    e=3*B17-2*b,
    C=3*B3-3*z+sum ell_p*r_p-B.

Here b,z,B are arbitrary Z3 parameters. The section is the
actual positional pair

    x_L=beta^b e_L^z k_L s_L*(t_L),
    x_F=k_F s_F(B,C,e,t_F).

Its total norm is exactly the cube of the target. Every section
has exactly these coordinates, by the actual complex coordinate
inverse and pure divisor inverse. Thus every fiber is
Z3^3 times the complete pure unit product times the complete
complex base-zero unit product.

For kappa3(7), E107 gives ell7=8. The concrete pure correction
a1^8 has norm3^8 and the complex factor s_L*(3[7]) has norm
7^3/3^8. Their combination gives the exact requested toric
coordinate, including the phase excluded in the pure=1 locus.

## Certificate and scope

The portable full rebuild is:

    python code/e_pure_tower.py --gp /absolute/path/to/gp

It executes the small degree6 certified GP calculation and
retains the full binary object. The self-contained Python
then verifies the literal units, four local characters,
all27 image inverses and mixed-unit products,792 compatible
prime-root transitions, and531441 full toric inverse checks.
The historical failed exports and their actual outputs are
retained with their precise causes. No expensive upper BNF
was restarted.

The entire H set at the stated first classes is evaluated.
The actual image from intrinsic metabelian or marked-depth
sections remains a further lifting problem through E38's
quotient maps. Nonunit multiples of kappa17 and first
classes outside the proved families are not included in this
theorem.
""")

manifest={'statement':'E.110','files':[]}
excluded={'ledger/e_pure_tower_manifest.json','code/e_pure_tower_freeze.out'}
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:
        continue
    rel=p.relative_to(ROOT).as_posix()
    if rel in excluded:
        continue
    manifest['files'].append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
save('e_pure_tower_manifest.json',manifest)
print(json.dumps({
 'statement':'E.110','status':'AUTHOR_FREEZE_PASS',
 'file_count':len(manifest['files']),
 'section_sha256':sha(proof),'program_sha256':sha(program),
 'GP_sha256':sha(ROOT/'code/e_pure_tower_base.gp'),
 'summary_sha256':sha(summary),
 'manifest_sha256':sha(LEDGER/'e_pure_tower_manifest.json'),
 'complete_scope':'All pure norm classes and the entire global H section set for first kappa3(17), including unit multiples.',
 'full_positional_inverse_checks':531441
},indent=2))
