"""Record the completed E105 root proof, source and exact execution audit."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
AUTHOR = ROOT / 'research_e105'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
enc = lambda x: json.dumps(x,indent=2,ensure_ascii=False)+'\n'
fresh = json.loads((HERE / 'comparison.json').read_text())
assert fresh['status'] == 'PASS' and fresh['excluded_fields'] == []
manifest_path = AUTHOR / 'ledger/e_quartic_class2_manifest.json'
assert sha(manifest_path) == fresh['author_manifest_sha256']
manifest = json.loads(manifest_path.read_text())
for relative, item in manifest['files'].items():
    assert sha(AUTHOR / relative) == item['sha256'], relative
for rec in fresh['records']:
    assert rec['exit_code'] == 0
    for row in rec['comparisons']:
        assert row['entire_file_byte_identical']
        assert (HERE / row['path']).read_bytes() == (AUTHOR / row['path']).read_bytes()
peer = json.loads((ROOT / 'bc_e105_audit/audit.json').read_text())
assert peer['audit_status'] == 'PASS' and peer['section_sha256'] == fresh['proof_sha256']
assert peer['excluded_fields'] == []

checks = [
 'The source is the actual plus Fermat quartic, with the twelve literal tangent-one cusp charts, origin B0 and the E103 generalized-Jacobian splitting. Each tangent line has its displayed order4 divisor; the121 frame values are computed in Q(zeta8), with both root-of-unity and sqrt2 coordinates retained.',
 'The odd division formula4a+mb=1 yields actual simultaneous m-divisions of z_d and fourth divisions of t_d. Their proper coordinates are H-fixed four-torsion, so their compact Kummer coordinate is literally zero in the specified splitting. The return path lifts the actual abelian path torsor.',
 'The vector-frame endpoint sign is separately epsilon_d, with+1 at d and-1 at every other non-O cusp. Its character is(-1)^(m_d+m_O). Its coherent odd roots are H-fixed; at2 its actual Kummer carry is d(sigma_d/2). The final rational-two shift is b_d/4+K_column/32+sigma_d/2, including the term invisible in the fourth-power frame matrix.',
 'The peripheral BCH action is derived from the literal returned loops and their path cocycles. The matrices L and L_v=L+v wedge(-), the actual orbit-average vector v, and the central origin cochain kappa2^2*L(v)/2 satisfy the full group and cocycle equations.',
 'The index4 average is applied in the pullback over the fixed E103 abelian section, whose geometric kernel is the abelian central module Lambda2 A. The averaging identity and inverse origin transport are proved with actual coset lifts. No nonabelian averaging step is assumed.',
 'The rational pushout is formed from the actual class-two source with its closed diagonal subgroup. The path and origin shifts are actual inner transports in that pushout. At2 the residual coordinate-unit cocycle is exactly d(1/8,0), using zero H-invariants to justify the global comparison.',
 'L_v annihilates the explicit two-coordinate section iota. The cochain z=-(k+alpha*beta/2)*omega supplies a lift from a continuous cup primitive. The actual curve map t=-(x/z)^4 yields the converse obstruction16*alpha cup beta;16 is invertible in precisely the claimed coefficient rings.',
 'The local tame relation retains q*((q-1)c+D) and the specified Frobenius/root coordinates. Changing roots changes the correction by the displayed restricted coboundary, and changes of Frobenius by inertia leave D fixed. The global criterion retains the same cochain topology.',
 'For odd primes>=5, the exact Kummer twist selects omega^(-1). The odd S-unit eigenspace and Ribet Main1.1 at k2, with B2=1/6, give the finite base cohomology vanishing. The finite Euler characteristic and devissage are used in the stated order. The3-primary base is the proved E32 calculation.',
 'Finite-support direct sums are taken before the derived inverse limit. The resulting correction criterion is c0/(q-1)c0 with no closure. For rational coefficients, compactness of cochain domains gives the exact bounded-denominator scalar extension, while Hain-Matsumoto AppendixB supplies the separate finite-S vanishing for every prime, including2.',
 'The explicit phantom input has coefficients tending to0 and unique correction-1 on infinitely many primes. It passes each separate finite/local test and fails the actual continuous correction criterion. For rational numbers, the support is the union of the numerator/denominator prime supports, retaining cancellations in their product.',
 'The fibre over any fixed liftable abelian section is the actual H1 of the central module. Its stabilizer is trivial because H0(A)=0. The central decomposition has ranks55+66+6+9=136; the six determinant maps and their inverse columns are explicit. The compact arithmetic action and the arbitrary mixed-input obstruction are retained as subsequent work.'
]
audit = {
 'status':'PASS','statement':'E.105','complete_proof_read':True,
 'proof_lines':len((AUTHOR / manifest['section']).read_text().splitlines()),
 'proof_sha256':fresh['proof_sha256'],'all_three_mathematical_programs_read':True,
 'author_manifest_sha256':fresh['author_manifest_sha256'],
 'manifest_files_checked':18,'complete_fresh_rebuild':fresh,
 'proof_checks':checks,'received_independent_peer_audit':peer,
 'received_peer_audit_md_sha256':sha(ROOT / 'bc_e105_audit/audit.md'),
 'primary_source_checks':[
   {'key':'E105_Ribet1976','url':'https://math.berkeley.edu/~ribet/Articles/invent_34.pdf',
    'scope':'Original Main Theorem1.1, printed151--152, actually viewed as page images. The used Herbrand direction, even range and k2 coefficient are explicit.',
    'root_refs':['turn871view1','turn872view0','turn872view1']},
   {'key':'E_HainMatsumoto','url':'https://arxiv.org/pdf/math/0006158',
    'scope':'Complete AppendixB, printed37--39, including B1,B2/B3 full finite-S comparison proof, B4 and its explicit ell2 paragraph, and B5 through its final localization proof.',
    'root_refs':['turn876view0','turn877view0','turn877view1','turn877view2','turn878view0']},
   {'key':'E_Wickelgren','url':'https://sites.math.duke.edu/~kgw/papers/3NilP1.pdf',
    'scope':'Proposition7 with full cocycle calculation and Corollary8, PDF13--14; Section12.4.5 Proposition26, rational tame-symbol formulas and Remark28, PDF27--28.',
    'root_refs':['turn911view0','turn911view1','turn911view2']},
   {'keys':['E_MilneADT','E_JannsenContinuous'],
    'scope':'The exact E32 finite-S, localization, Euler, arithmetic-etale and derived-inverse-limit source passages remain recorded in ledger/e_completed_source_evidence.json. This audit reads that complete ledger and verifies the E105 use of the same comparisons.'}
 ],
 'author_corrections':json.loads((AUTHOR / 'ledger/e_quartic_class2_author_corrections.json').read_text()),
 'scope':'Actual class-two origin and complete two-coordinate toric image, with continuous obstruction evaluated. No arbitrary compact-handle or mixed abelian input is claimed to be computed here.'
}
(HERE / 'audit.json').write_text(enc(audit))
lines=['# Completed root audit: E.105','','Result: PASS.','',
 'The entire proof and all three mathematical programs were read. A fresh copied execution reproduced every complete stdout and JSON byte for byte with no exclusions. The independent bc_fermat audit has been received and passed on this same frozen proof.','',
 '## Exact proof and map checks','']
for check in checks: lines.extend(['- '+check,''])
lines.extend(['## Reading scope','',
 'The original Ribet theorem and complete Hain–Matsumoto AppendixB were read; Wickelgren Proposition7 and its proof, Proposition26 and Remark28 were independently reopened. The finite-S and continuous-cohomology passages retain their exact earlier E32 evidence.','',
 'The separate endpoint-sign correction and every author-draft correction are retained. Final whole-paper layout verification follows integration.',''])
(HERE / 'README.md').write_text('\n'.join(lines))
print(enc({'status':'PASS','statement':'E.105','proof_lines':audit['proof_lines'],
           'manifest_files_checked':18,'audit_sha256':sha(HERE / 'audit.json'),
           'complete_output_byte_equality':True,'excluded_fields':[]}))
