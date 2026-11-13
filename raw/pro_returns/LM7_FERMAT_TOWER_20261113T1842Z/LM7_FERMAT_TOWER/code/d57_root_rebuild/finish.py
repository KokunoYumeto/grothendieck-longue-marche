"""Record the completed root proof and six-stage execution audit of D57."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'D57_EXPERIMENTS'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
enc = lambda x: json.dumps(x, indent=2, ensure_ascii=False) + '\n'
comparison = json.loads((HERE / 'comparison.json').read_text())
assert comparison['status'] == 'PASS'
assert comparison['excluded_fields'] == ['elapsed_seconds']
manifest_path = AUTHOR / 'ledger/d_arithmetic_class2_repair_manifest.json'
manifest = json.loads(manifest_path.read_text())
assert sha(manifest_path) == comparison['manifest_sha256']
for row in manifest['files'] + manifest['immutable_inputs']:
    assert sha(AUTHOR / row['path']) == row['sha256'], row['path']
assert len(comparison['checks']) == 6
for row in comparison['checks']:
    assert row['exit_code'] == 0
    assert row['entire_json_equal_except_elapsed_seconds']
    assert row['entire_stdout_equal_except_elapsed_seconds']

checks = [
 'The marked rank-nine source is the actual genus-three curve y^4=x^3+1. The 48 deck states and 96 edges give the branch types 2^24,3^16,12^4, four cusps and the specified integral homology marking.',
 'The degree-eight E3 map is the literal y-square quotient followed by multiplication by two. Its two rational functions satisfy v^2=u^3+1 and beta=v^2, and the s/r action is computed on those functions. The two additional elliptic quotients have independent differentials, giving the actual isogeny and its Q8 action.',
 'The original arithmetic element h=[g,tau] acts trivially on the Ei two-adic Tate source by the inertia-three comparison. The finite Hom lattice and its actual centralization reduce the middle scalar to the four fourth roots of unity. The exact centralizer has dimension five. The integral conjugator equations retain the two branches J and J^3.',
 'The negative conjugator decisions exhaust integral solutions: every rref denominator is 1,3 or6, so its two-primary denominator is at most2. Changing a free coordinate by4 changes each pivot by an integral two-adic value. Consequently all1024 residues of the five free coordinates modulo4 cover every integrality possibility. The rejected branches have the recorded obstruction; no finite residue sample is used without this proof.',
 'The actual common quotient uses T2-star and the class-two rank-nine quotient, with the original arithmetic action (id,h). The invariant cusp lattice is primitive, so the literal inner conjugation by t^(-12z) aligns the peripheral loop. Its inverse is retained in the final marking.',
 'The order3888 source has homology rank649, moving rank640 and invariant central rank2560. The actual G-coinvariant central quotient has rank74, the full norm has rank40 and its compact part rank6. Local correction has rank64, leaving ten explicit equations.',
 'All780 quadratic coefficients, all40 linear coefficients and the constant term are retained for each branch. The computed coefficient rank is9 with the displayed output relation. Both literal zeros are verified. The sixteen framed source words retain their full letters, abelian sums, all74 moving coinvariants and the exact marked homology maps.',
 'The printed words do not record the plus-compact central coordinate. The separate surjection from the full invariant exterior square performs the actual central alignment while preserving the74 already solved coordinates. The remaining error lies in the precise Z-star intersection, and its zero coinvariant class supplies the augmentation correction.',
 'The corrected finite map is an automorphism by its full Frattini rank. Fourth-power corrections in Rh then lift the prescribed integral homology without changing T2-star or the arithmetic source. The constructed automorphism is on the explicitly defined X-star quotient, with all original conjugators restored.',
 'The exact quotient map from X54 to X-star is obtained from the stated subgroup containment, and its kernel is retained. The commutator-square witness survives in the supplied class-two quotient with abelian exponent8 and central exponent4. Thus the new quotient result is not used as a completed full-profinite realization.',
 'Every one of the six final mathematical programs was read. The complete final proof, the final rref amendment and both immutable D56 inputs were checked. The fresh copied execution ran the dependent stages in order and compared every complete JSON and stdout, excluding only the named elapsed_seconds values.',
 'Historical unoptimized and optimized attempts, nested actual stdout, the pre-amendment proof and conjugator source/output, and the exact final diffs remain preserved. The final boundary program records its nested local-transgression computation without replacing the standalone output.'
]
audit = {
 'status':'PASS', 'statement':'D.57', 'complete_proof_read':True,
 'proof_lines':len((AUTHOR/'sections/D_arithmetic_class2_repair.tex').read_text().splitlines()),
 'proof_sha256':comparison['proof_sha256'],
 'all_six_mathematical_programs_read':True,
 'manifest_sha256':comparison['manifest_sha256'],
 'manifest_files_and_inputs_checked':len(manifest['files'])+len(manifest['immutable_inputs']),
 'fresh_execution':comparison, 'proof_checks':checks,
 'source_scope':'The new maps are proved by the owned explicit geometry and exact module calculations. The previous arithmetic source inputs are D46 and D49--D56, with their existing primary-source records; no newly opened external proof is claimed in this audit.',
 'author_source_evidence':json.loads((AUTHOR/'ledger/d_arithmetic_class2_repair_source_evidence.json').read_text()),
 'final_rref_amendment':'Read in full; maximum two-primary rref denominator2 proves the complete mod4 search.',
 'remaining_original_tasks':['D.13','D.19'],
 'scope':'An actual arithmetic automorphism on X-star, retaining every solved invariant class-two coordinate. Full G3 homology and the remaining full-profinite lifting problem remain separate subsequent tasks.'
}
(HERE/'audit.json').write_text(enc(audit))
text=['# Completed root audit: D.57','','Result: PASS.','',
 'The entire final proof and all six mathematical programs were read. The exact rref denominators prove the residue search exhaustive. The fresh six-stage copied execution returned exit0 at every stage; every complete JSON and stdout agrees after removing only explicitly named elapsed_seconds values.','',
 '## Proof and actual-map checks','']
for check in checks: text.extend(['- '+check,''])
text.extend(['## Scope','',audit['scope'],'',audit['source_scope'],''])
(HERE/'README.md').write_text('\n'.join(text))
print(enc({'status':'PASS','statement':'D.57','proof_lines':audit['proof_lines'],
           'manifest_files_and_inputs_checked':audit['manifest_files_and_inputs_checked'],
           'audit_sha256':sha(HERE/'audit.json'),'excluded_fields':['elapsed_seconds']}))
