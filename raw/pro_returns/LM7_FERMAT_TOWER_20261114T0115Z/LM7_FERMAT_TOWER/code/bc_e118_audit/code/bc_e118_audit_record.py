"""Record the complete proof audit and exact fresh no-input reconstruction."""
from pathlib import Path
import hashlib,json
BASE=Path(__file__).resolve().parents[2]
HERE=BASE/'bc_e118_audit';AUTHOR=BASE/'research_e118'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
proof=AUTHOR/'sections/E_quartic_five_numerical.tex'
expected='142d07c7f19d79b5044ae37208f226031595c97b1060c023bf9da3b734f1a0f2'
assert sha(proof)==expected
names=['e_quartic_five_numerical.gp','e_quartic_five_numerical.out','e_quartic_five_numerical.err','e_quartic_five_numerical_verify.py','e_quartic_five_numerical_verify.out','e_quartic_five_numerical_verify.json']
comparisons={}
for n in names:
    p,q=AUTHOR/'code'/n,HERE/'code'/n
    assert p.read_bytes()==q.read_bytes(),n
    comparisons[n]={'byte_identical':True,'sha256':sha(q)}
independent=json.loads((HERE/'code/bc_corestriction_check.json').read_text())
assert independent['status']=='PASS' and independent['all_cocycle_identities']==640000
checks=[
 'Read the complete corrected theorem/proof, complete GP source and complete Python source.',
 'Exact degree32 compositum, point coordinates and inverse field maps; all32 actual embeddings and residual matrices.',
 'Monic integer unit equations with unit constant term, literal inverse, and tau_b(u)=w^5 u^3.',
 'The conjugate unit character and the negative second coordinate in H agree with the actual determinant character.',
 'Left-coset corestriction gives a cocycle; 3*32=1 mod5 makes its restriction H; changing representatives adds g v-v.',
 'The norm-to-degree8 map proves injectivity of the nonfifth class, and the distinct tau_a characters prove independence.',
 'The resulting actual Kummer field is normal, unramified away2,5 and has degree800 overQ; kernel equality is read through rho and H.',
 'E112 finite H1 reduction is onto and each integral H1 is free rank1; all integral generator choices are (1+5z)h.',
 'The specified degree-one prime, two fifth residue logarithms and alternating Weil-pairing sign give h1(F3121)=(3,1).',
 'The independently enumerated3200 points and actual25-element torsion span imply F-1=5D with D invertible, hence exact local order5.',
 'The toric fifth-power condition, primitive inertia and E115 exact mixed criterion give precisely5Z5^3, both directions, with all central fibres retained.',
 'Corrected tensor extension and its literal inverse are distinguished from the image of the integral inclusion; the actual finite-support rational correcting cochain gives the full rational slice.',
 'All six copied source/output files are byte-identical after a fresh no-input GP/Python reconstruction; no elapsed or other field excluded.',
 'A separately written finite group program verifies25600 corestriction terms,800 representative-change formulas and640000 cocycle identities.'
]
record={'statement':'E.118','status':'PASS','proof_sha256':expected,'full_proof_source_audit':checks,'fresh_replay':{'command':'python bc_e118_audit/code/e_quartic_five_numerical_verify.py --gp research_e52/vendor/pari-2.19.0/gp','binary_inputs':[],'exit_code':0,'comparisons':comparisons,'exclusions':[]},'independent_program':independent,'amendment':{'original_read_sha256':'73b82d7b97c559b0d4ea3c9fc98b5c87e7ea40e932ca73d6982b9b9c31a4059d','issue':'The literal inclusion5R^3 intoQ5^3 is not onto.','resolved_by':'The corrected statement supplies the actual tensor extension and inverse, and separately the E115 finite-support rational correcting cochain.','final_proof_read':True},'dependency_anchors':['E112.2 and the full finite coefficient reduction/inverse-limit proof','E115.3-6 and E115.23, actual mixed local boundary and coefficient maps','E115 final exact toric fifth-power tame-symbol calculation'],'source_scope':'E118 has an explicit algebraic/finite-field proof. The exact E112/E115 dependency maps were reread; no new blanket primary-document replay is claimed.'}
(HERE/'audit.json').write_text(json.dumps(record,indent=2)+'\n')
md='# Independent E.118 audit\n\n**PASS.** The complete corrected proof and both mathematical sources were read. A fresh reconstruction used only the two source files; no binary arithmetic input was supplied.\n\n'
md+='Reviewed proof SHA256: `'+expected+'`.\n\n## Proof checks\n\n'
md+='\n'.join('- '+x for x in checks)+'\n\n## Exact correction\n\nThe initial statement described the inclusion of the integral slice as surjective after scalar extension. The corrected text proves the tensor map `(5R^3) tensor_R Q5 -> Q5^3`, its inverse on the basis, and separately constructs the actual rational section through E115’s correcting cochain. This resolves the typing issue; no other proof correction was requested.\n\n## Fresh arithmetic replay\n\nThe full no-input GP/Python replay completed with exit0. Both source files, GP stdout/stderr, Python stdout and the full JSON are byte-identical to the author files, with zero excluded fields. The additional independent program checks all640000 cocycle identities in the actual residual semidirect group of order800.\n\n## Scope\n\nThis is a complete proof/source audit plus a fresh arithmetic replay. E112’s exact finite reduction and E115’s actual coefficient/local boundary maps were reread. It does not claim a new independent reopening of every primary source cited by those earlier statements. All audit programs and their actual outputs are retained under `code/`.\n'
(HERE/'audit.md').write_text(md)
print(json.dumps({'status':'PASS','audit_json_sha256':sha(HERE/'audit.json'),'audit_md_sha256':sha(HERE/'audit.md'),'proof_sha256':expected,'byte_identical_files':len(names),'independent_cocycle_identities':640000},indent=2))
