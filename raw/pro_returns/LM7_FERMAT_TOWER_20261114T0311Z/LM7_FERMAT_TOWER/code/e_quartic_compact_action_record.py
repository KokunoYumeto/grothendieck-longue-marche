#!/usr/bin/env python3
"""Record E109's actual arithmetic, coefficient maps and original-source scope."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT.parent
LEDGER = ROOT / 'ledger'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(name, value):
    (LEDGER / name).write_text(json.dumps(value, indent=2) + '\n')

proof = ROOT / 'sections/E_quartic_compact_action.tex'
tex = proof.read_text()
assert re.findall(r'\\tag\{E109\.(\d+)\}', tex) == [str(i) for i in range(1, 25)]
assert len(re.findall(r'(?m)^\\\[$', tex)) == len(re.findall(r'(?m)^\\\]$', tex))
assert not any(ord(c) < 32 and c not in '\n\t' for c in tex)
d = json.loads((ROOT / 'code/e_quartic_ceresa_shadow.json').read_text())
r = json.loads((ROOT / 'code/e_quartic_ceresa_final_replay.json').read_text())
assert d['status'] == r['status'] == 'PASS'
assert r['actual_exit_code'] == 0 and r['excluded_fields'] == []
assert all(x['complete_byte_equality'] for x in r['checks'])
for check in r['checks']:
    assert sha(ROOT / 'code' / check['file']) == check['sha256']
assert sha(ROOT / 'code/e_quartic_ceresa_shadow.py') == r['source_sha256']
assert d['five_primary_detection']['exact_order'] == 5
assert len(d['shadow_records']) == 14

save('e_quartic_compact_action_results.json', [{
    'id': 'E.109', 'status': 'Proved',
    'statement': (
        'For the actual compact plus-quartic pro-five class-two arithmetic action, '
        'the entire outer central action class is carried by the rank-two pure-CM '
        'module M. An explicit integral coefficient projector Pi has a left inverse '
        'identity on the Johnson map, hence also on continuous cohomology. The class '
        'beta_Q=2 Pi[c_C]_out satisfies 2[c_C]_out=fbar beta_Q and restricts over '
        'Q(zeta8) to the pure-CM Abel--Jacobi class of the Ceresa cycle. The actual '
        'affine-to-compact map, its coordinate correction J and every inner correction '
        'give beta_Q=2[Pi(p_B c_A j)]. Literal curve and Jacobian maps identify its '
        'cycle with Bloch\'s. The recomputed point 4 delta_19 has exact order5, '
        'and the Frobenius invariant calculation at11 proves that beta_Q is nontorsion.'),
    'where_proved': (
        'sections/E_quartic_compact_action.tex, E109.1--24 and complete proof; '
        'code/e_quartic_ceresa_shadow.py/.out/.json, with the complete final '
        'byte-identical fresh execution recorded by e_quartic_ceresa_final_replay.'),
    'depends_on': ['E.103', 'E.105', 'E109_Bloch', 'E109_HainMatsumoto',
                   'E109_BisognoLiLittSrinivasan'],
    'manuscript_passages': [
        'LM section51.16; folios733v--736v; scans172--178; the compact factor of '
        'the generalized Jacobian and the next arithmetic approximation in Part E(c),(d).'],
    'depends_on_doubtful_reading': False,
    'notes': (
        'The full action statement uses the order16 coordinate-automorphism projector '
        'and restriction/corestriction of degree4. The factor2 is retained. '
        'The translation in the Bloch curve map is removed by the literal doubling '
        'identity and multiplication8 on H3, with all maps invertible at5. '
        'The unrestricted mixed quartic cup obstruction and section fibres remain '
        'active in E23; the theorem evaluates their specified actual action coefficient.')
}])

source_rows = [
    {
        'key': 'E109_Bloch',
        'url': 'https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0350/LOG_0009.pdf',
        'local_original': 'source_route_raw/bloch1984.pdf',
        'sha256': '9eb338771cda7e4e33f638e69dffda0afc092f9f2e0268e92f3d1b18359707a0',
        'actually_read': [
            'Original printed pages96--106 visually read from the retained page images.',
            'Section1 Corollary1.2 and Proposition1.3; Section2 Proposition2.1 '
            'and Corollary2.2; Section3 Lemmas3.1--3.2, Theorem3.4 and Lemma3.5; '
            'Section4 Theorem4.1 full proof; Section5 Lemma5.1.',
            'Formula3.3 and the literal formula3.6 comparison, the three quartic '
            'maps, the pure-CM projector and the Frobenius invariant argument.'],
        'scope_limit': (
            'The introduction on printed pages94--95 was inspected through OCR only. '
            'Printed pages107--108 were not claimed as read. The current web PDF '
            'reader failed; the successful earlier original GDZ download and its '
            'visual reading supply the source evidence.'),
        'use': 'Actual cycle nonvanishing from the finite correspondence and its nontorsion invariant test.'
    },
    {
        'key': 'E109_HainMatsumoto',
        'url': 'https://arxiv.org/pdf/math/0306037',
        'local_original': 'source_route_raw/hain_matsumoto2005.pdf',
        'sha256': '590d6fddaf48b9b6deb931930c7ad3ac081b03366dd5aa8355273de34a25b089',
        'actually_read': [
            'Entire Sections4.1--4.5.',
            'Sections5.1--5.3, including Lemmas5.2--5.4 and Proposition5.5.',
            'Section6.3 Proposition6.4 with its full mapping-torus proof; '
            'Section6.4 Proposition6.5 and Corollaries6.6--6.7.',
            'Section8 Theorem8.1 and the complete proof of Theorem3; Sections10.2--10.5.'],
        'scope_limit': (
            'Theorem10.5 itself refers to the pointed argument rather than repeating '
            'it. E109 supplies the actual inner quotient and finite res/cor transfer '
            'used in the unpointed statement.'),
        'use': 'Integral action--cycle comparison with its literal factor2 and the Magnus/Johnson convention.'
    },
    {
        'key': 'E109_BisognoLiLittSrinivasan',
        'url': 'https://epiga.episciences.org/11131/pdf',
        'local_original': 'source_route_raw/bisogno_li_litt_srinivasan2023.pdf',
        'sha256': '487e1012dadbac34cacb2809ffbe6ca1c6302c03f6ce05c077b88099fcc09b6c',
        'actually_read': [
            'Entire Sections2.1--2.3, with all proofs through Corollary2.17 '
            'and the complete comparison in Proposition2.23.'],
        'scope_limit': 'The surface class-two presentation used here is proved directly in E109.',
        'use': 'Continuous augmentation-ideal action class, inner quotient and exact Ceresa comparison.'
    }
]
for row in source_rows:
    assert sha(WORK / row['local_original']) == row['sha256']
save('e_quartic_compact_action_source_evidence.json', {
    'statement': 'E.109', 'sources': source_rows,
    'internal_exact_inputs': [
        'E103 actual maps Phi and Psi, their [4] composites, adjoint polarization, '
        'and the actual equivariant affine homology section j_*/4.',
        'E105 actual pro-five arithmetic section, central BCH coordinates and '
        'the source quotient from the affine arithmetic fundamental group.'],
    'author_reading': 'Full proof and all coefficient transports checked by the author; final certificate replay PASS.',
    'independent_review': 'd_galois is completing its full proof/source audit; no unreceived final verdict is asserted.'
})

save('e_quartic_compact_action_computation_status.json', {
    'statement': 'E.109', 'status': 'PASS',
    'final_program': 'code/e_quartic_ceresa_shadow.py',
    'final_output': 'code/e_quartic_ceresa_shadow.out',
    'final_json': 'code/e_quartic_ceresa_shadow.json',
    'actual_exit_code': 0,
    'fresh_execution': r,
    'finite_scope': {
        'primes': d['all_primes_3_mod4_at_most103'],
        'five_primary_detection': d['five_primary_detection'],
        'complete_coefficient_data': [
            'all exterior and Hom matrices, inner map and quotient',
            'alternation, pure-CM projector and its cohomology left inverse',
            'all20 exterior characters and the actual order16 average',
            'literal curve, translation, doubling and isogeny identities']},
    'history': [
        'code/e109_initial_shadow retains the first actual source, full output, JSON and provenance.',
        'replay retains the fresh execution of that first source, driven by code/e_quartic_ceresa_replay.py.',
        'code/e109_cohomology_left_inverse retains the next actual source, full output, JSON and provenance.',
        'replay_verified retains the complete fresh execution of the final source.'],
    'proof_scope': (
        'The finite calculations certify their literal inputs and maps. The full '
        'arithmetic action identity and nontorsion inference use the separately '
        'proved coefficient comparison and the original source theorems.')
})

save('e_quartic_compact_action_coverage.json', {
    'statement': 'E.109', 'tasks': ['E.c', 'E.d', 'E.followup4'],
    'settled_step': 'Entire compact class-two outer arithmetic action over Z5, via the actual affine comparison.',
    'maps_with_transfers': [
        'continuous filling map (x,z) -> (px,p_B z+Jx)',
        'actual equivariant section j with pj=identity',
        'cochain equality c_C=p_B c_A j+Jj-g(Jj)',
        'inner correction killed by Pi, with Pi fbar|M=identity',
        'order16 average on the exact exterior coefficient module',
        'restriction to F followed by corestriction equals4',
        'explicit plus/minus quartic and elliptic isomorphisms',
        'literal [2]rho=([2]Phi_B)i_b and pushforward multiplication8',
        'restriction from Q(i) to F followed by corestriction equals2'],
    'remaining': [
        'Evaluate the mixed compact/peripheral obstruction and all section fibres for the unrestricted quartic inputs.',
        'Continue the original unrestricted cubic, metabelian and marked-depth section classification in E23.']
})

(LEDGER / 'e_quartic_compact_action_report.md').write_text('''# E.109: compact quartic arithmetic action

The theorem evaluates the entire outer central action class of the actual compact
pro-five class-two group. Its coefficient projection has an explicit integral
left inverse. The affine comparison retains the linear coordinate correction
and all inner terms. Averaging the sixteen actual coordinate automorphisms
projects the entire class onto the two pure CM lines; restriction/corestriction
returns that equality to the original rational arithmetic source.

The comparison to Bloch uses literal curve maps. The two-torsion translation is
retained and removed by the displayed doubling identity. The corresponding
pushforward on degree-three cohomology is multiplication by eight. The original
action--cycle comparison contributes a factor of two, which remains explicit.

The program computes every prime congruent to three modulo four up to103,
including every trace-one summand and the alternate finite formula. At19 the
point delta has order10 and four times that point has order5. The original
comparison theorem and the Frobenius invariant test at11 then prove that the
integral arithmetic class has infinite order. The complete matrix certificate
includes all twenty exterior characters and the actual order16 projector.

The final source was run afresh. Both complete stdout and complete JSON are
byte-identical, with no excluded fields. Earlier source versions and their
actual outputs remain preserved. The source-evidence ledger gives the precise
original passages read and the limits of each reading claim.

The mixed compact/peripheral obstruction, its unrestricted zero locus and all
central fibres remain active under E.23. The independent full audit is in
progress; this record does not anticipate its final verdict.
''')
print(json.dumps({
    'status': 'PASS', 'statement': 'E.109',
    'proof_sha256': sha(proof),
    'final_program_sha256': sha(ROOT / 'code/e_quartic_ceresa_shadow.py'),
    'written_ledgers': sorted(p.name for p in LEDGER.iterdir()),
    'source_hashes_checked': len(source_rows),
    'final_replay_complete_byte_equality': True
}, indent=2))
