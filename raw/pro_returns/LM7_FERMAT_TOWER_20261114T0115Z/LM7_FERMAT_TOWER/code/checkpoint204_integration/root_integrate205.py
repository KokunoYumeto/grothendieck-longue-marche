"""Audit/integrate D58 and repair the observed E107 display overflow."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT=Path(__file__).resolve().parent;BASE=ROOT/'LM7_FERMAT_TOWER';AUTHOR=ROOT/'D58_EXPERIMENTS'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
enc=lambda x:json.dumps(x,indent=2,ensure_ascii=False)+'\n'
assert not (BASE/'sections/D_full_homology_repaired_block.tex').exists()
mp=AUTHOR/'ledger/d_full_homology_repaired_block_manifest.json'
assert sha(mp)=='38b76e8ad7cc02617393769709a83982cbcf5c7435daea0843f2176c2b146188'
manifest=json.loads(mp.read_text())
for row in manifest['files']:assert sha(AUTHOR/row['path'])==row['sha256'],row['path']
source=json.loads((AUTHOR/'ledger/d_full_homology_repaired_block_source_evidence.json').read_text())
for row in source['dependencies']:assert sha(ROOT/row['workspace_path'])==row['sha256'],row['statement']

history=BASE/'code/checkpoint204_first_build';history.mkdir(exist_ok=False)
for name in ['build_pdf.py','build_pdf.out','latex_pass1.out','latex_pass2.out','latex_pass3.out','bibtex.out']:
    shutil.copy2(BASE/'code'/name,history/name)
assert '42.36147pt too wide' in (history/'build_pdf.out').read_text()
shutil.copy2(BASE/'LM7_FERMAT_TOWER_paper.log',history/'paper_log.md')
shutil.copy2(BASE/'LM7_FERMAT_TOWER_paper.tex',history/'paper_master.tex.md')
shutil.copy2(BASE/'sections/E_stable_ordinary_phase.tex',history/'E_stable_ordinary_phase.tex.md')
(history/'status.json').write_text(enc({'status':'layout validation failed','observed_exit_code':1,
 'mathematical_program_failure':False,'issue':'One E107.13 display overflowed by42.36147pt; all three LaTeX passes and BibTeX had exit0.',
 'source_sha256':{str(p.relative_to(BASE)):sha(p) for p in [BASE/'LM7_FERMAT_TOWER_paper.tex']+sorted((BASE/'sections').glob('*.tex'))}}))

checks=[
 'The actual onto U-minus to U-star-minus map has free target, hence saturated kernel L of rank w-640. To realize each L element in the intersection S57, the proof chooses its Rh preimage and removes its small central image using the actual onto R50 to Z-star map.',
 'Both kernels of Y and its fibre-product presentation are computed from the original source intersections and products. The map from S57 to full U has kernel S57 intersect M-infinity, exactly the defining kernel of Y.',
 'The D57 action descends to every common Jk/Lk quotient through the invariant image of K3 in X-star and its characteristic abelian exponent2^k quotient. This retains the actual D57 conjugators without requiring a new centralizer lift into an old homology action.',
 'The initial cusp-correction map has image I_G L. The odd averaging projection annihilates L, so its A and G coinvariants vanish and the correction map is onto.',
 'The marked edge chain map has invertible vertex maps and restricts to the actual homology map. Its nilpotent Fitting summand is contained in L because the quotient homology map is already invertible. That summand is projective as a direct summand of the regular edge module.',
 'The explicit path derivation and cyclic norm correction retain the fixed cusp. The norm kernel equals the image of1-t on the projective cyclic restriction. The correction stays in L and changes T to T+e, invertible on both Fitting summands; the full original common action is preserved.',
 'The higher intersection is proved using actual preimages, then saturation gives Lk intersect2^(k-1)Uk=2^(k-1)Lk. The resulting common quotient is the exact fibre product of the preceding two quotients. Compatible lifted conjugators and augmentation corrections yield automorphisms at every level and in the inverse limit.',
 'The inclusion of the two class-two source kernels gives X to Y. Its kernel is exactly ker(Z to Z-star), with both inclusions supplied by the same R50 representatives. The retained small action and full homology intertwiner make exterior-square T preserve K, K0 and K1.',
 'The central moving correction map onto K1 is surjective because its A-coinvariants vanish. The corrected source map factors through the class-two laws and the preserved K0. Its Frattini action is invertible, and its two actual projections yield an automorphism of the exact fibre product X/K0.',
 'Odd averaging makes the fixed map Z^A to Z-star^(A-star) onto. Subtracting the target dimensions210240,2560,207680 from the full module dimensions gives all three exact kernel dimensions. The positive lower bound366080 and an actual R50 preimage detect a surviving source kernel.',
 'The complete frozen proof was read, together with the whole D50 edge-map/Fitting/path/cyclic-norm construction at the exact cited dependency. All six frozen-file hashes and all five dependency hashes match. This proof uses the actual full arithmetic G3 and no new finite surrogate or numerical execution.'
]
audit={'status':'PASS','statement':'D.58','proof_sha256':sha(AUTHOR/'sections/D_full_homology_repaired_block.tex'),
 'proof_lines':len((AUTHOR/'sections/D_full_homology_repaired_block.tex').read_text().splitlines()),
 'manifest_sha256':sha(mp),'complete_proof_read':True,'verified_frozen_files':6,'verified_dependency_files':5,
 'checks':checks,'new_numerical_execution_claim':'None; proof-only actual-source extension.',
 'received_peer_audit':False,'remaining':'The actual boundary in (K0)_G and the original full profinite image problem remain active.'}
(BASE/'ledger/root_d58_audit.json').write_text(enc(audit))
(BASE/'ledger/root_d58_audit.md').write_text('# Completed root audit: D.58\n\nResult: PASS.\n\n'+'\n\n'.join('- '+x for x in checks)+'\n\n'+audit['remaining']+'\n')
mapping=[]
for p in sorted(AUTHOR.rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts:
        rel=p.relative_to(AUTHOR);dst=BASE/rel;assert not dst.exists(),dst
        dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
        mapping.append({'source':str(p.relative_to(ROOT)),'archive':str(rel),'sha256':sha(p)})

detail=('D.58 retains the complete D57 action and actual conjugators while restoring the full integral G3 homology through a projective Fitting repair inside L=ker(U-minus to U-star-minus). '
 'The exact source Y has kernel L over X-star and Z-star over Z_h. It further extends through the entire remaining moving class-two module to X58=X/K0, '
 'where K0=ker(Z to Z-star)^A. All2560 solved invariant coordinates remain, and the exact residual invariant dimension is m^2(q-1)/2-2560, at least366080. '
 'The actual boundary in (K0)_G and the full profinite realization remain active.')
p=BASE/'ledger/d_full_homology_repaired_block_results.json';rows=json.loads(p.read_text())
rows[0]['notes']=rows[0]['notes'].replace('Proof and exact maps self-audited; parent/peer review pending.','Full root proof and dependency-map audit PASS; no new numerical computation or independent peer review is claimed.')
rows[0]['where_proved']+='; ledger/root_d58_audit.json'
p.write_text(enc(rows))
p=BASE/'ledger/d_full_homology_repaired_block_report.md';p.write_text(p.read_text()+'\n## Completed root proof audit\n\n'+detail+'\n\nThe entire frozen proof and the exact D50 repair construction were read. Every frozen file and dependency hash matches. Root audit: ledger/root_d58_audit.json.\n')
p=BASE/'LM7_FERMAT_TOWER_paper.tex';t=p.read_text();needle=r'\input{sections/D_arithmetic_class2_repair.tex}'
assert t.count(needle)==1;p.write_text(t.replace(needle,needle+'\n'+r'\input{sections/D_full_homology_repaired_block.tex}'))
p=BASE/'sections/D.tex';t=p.read_text()
addition=r'''

D.58 retains the entire D.57 action and its conjugators while
restoring the full integral arithmetic homology. The actual
projective repair stays in
$\mathcal L=\ker(U^-\to U_*^-)$.
It then extends through the remaining moving class-two module,
with exact residual kernel
$\mathcal K_0=\ker(Z\to Z_*)^A$.
All $2560$ solved invariant coordinates are retained; the remaining
dimension is $m^2(|A|-1)/2-2560$.
The next actual invariant boundary and the full profinite realization
remain to be evaluated across this specified source map.
'''
for identifier in ['D.13','D.19']:
    a=t.index(r'\begin{statement}{'+identifier+'}');b=t.index(r'\end{statement}',a);t=t[:b]+addition+t[b:]
p.write_text(t)
p=BASE/'ledger/d_results.json';rows=json.loads(p.read_text())
for row in rows:
    if row['id'] in ['D.13','D.19']:row['depends_on'].append('D.58');row['notes']+=' '+detail
p.write_text(enc(rows))
p=BASE/'ledger/d_coverage.json';rows=json.loads(p.read_text())
for row in rows:
    if row['task'] in ['D.e','D.afterLM2.1']:
        row['statement_ids'].append('D.58');row['outcome']+=' '+detail
        row['remaining_step']='Evaluate the actual residual boundary in (ker(Z to Z-star)^A)_G and lift across the remaining full profinite source kernel; decide the original GT0 and all-loop image comparison.'
p.write_text(enc(rows))

p=BASE/'sections/E_stable_ordinary_phase.tex';before=sha(p);t=p.read_text()
old=r'''\[
 \left(\kappa_3(17),\
 B_{17}\kappa_3(17)+B_3\kappa_3(3)+
                  \sum_{p\in\mathcal P}r_p\kappa_3(p)\right),
 \quad
 B_{17},B_3\in\mathbb Z_3,\quad
 r\in\mathscr R(\mathcal P),\quad
 \sum c_pr_p=0\pmod3.
 \tag{E107.13}
\]'''
new=r'''\[
 \begin{gathered}
 \left(\kappa_3(17),\
 B_{17}\kappa_3(17)+B_3\kappa_3(3)+
                  \sum_{p\in\mathcal P}r_p\kappa_3(p)\right),\\
 B_{17},B_3\in\mathbb Z_3,\qquad
 r\in\mathscr R(\mathcal P),\qquad
 \sum c_pr_p=0\pmod3.
 \end{gathered}
 \tag{E107.13}
\]'''
assert t.count(old)==1;p.write_text(t.replace(old,new))
(BASE/'ledger/e107_display_amendment.json').write_text(enc({'status':'PASS','kind':'layout only',
 'before_sha256':before,'after_sha256':sha(p),'observed_issue':'42.36147pt overfull display E107.13',
 'change':'Two gathered rows; all mathematical symbols and conditions retained.',
 'original_source_and_failed_build':'code/checkpoint204_first_build'}))
(BASE/'ledger/checkpoint205_integration.json').write_text(enc({'status':'PASS','added_statement':'D.58',
 'expected_statement_count':205,'root_audit_sha256':sha(BASE/'ledger/root_d58_audit.json'),
 'frozen_to_archive_mapping':mapping,'layout_only_amendment':'E107.13 gathered display',
 'build_status':'The failed204 layout is preserved; a complete205 build/render follows.'}))
print(enc({'status':'PASS','statement':'D.58','root_audit_sha256':sha(BASE/'ledger/root_d58_audit.json'),
           'proof_lines':audit['proof_lines'],'expected_statement_count':205,'layout_only_correction':'E107.13'}))
