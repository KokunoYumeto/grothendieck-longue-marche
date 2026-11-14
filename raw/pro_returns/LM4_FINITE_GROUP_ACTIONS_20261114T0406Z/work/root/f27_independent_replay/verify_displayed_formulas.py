"""Root cross-check of the exact formulas printed in F27 against audited rows."""
from pathlib import Path
import hashlib,json,runpy

HERE=Path(__file__).resolve().parent
helpers=runpy.run_path(str(HERE/'affine_product_one_two_parameter_independent_audit.py'),run_name='f27_checked_helpers')
parse=helpers['parse'];pm=helpers['parse_matrix'];mm=helpers['matrix_mul']
sub=helpers['matrix_sub'];sm=helpers['scalar_mul'];det=helpers['determinant']
symbolic=json.loads((HERE/'affine_product_one_two_parameter_stage_output.json').read_text())
flags=[pm(r['action_flag_6']) for r in symbolic['source_records']]
H=pm([
 ['0','0','0','-(t+1)/t','s*t'],
 ['0','s','-1/t','0','0'],
 ['0','-1/t','0','s*t+1','0'],
 ['(s-1)/(s*t**2)','s*(s-1)','-(s-1)/t','s-1','0'],
 ['(t+1)/(s*t**2)','0','0','0','s*t']])
g=parse('(s-1)*(t-1)')
rows=[]
for j in [2,4,5,6,7]:
    comm=sub(mm(flags[1],flags[j]),mm(flags[j],flags[1]))
    assert all(not x for row in comm[1:] for x in row)
    assert not comm[0][0]
    rows.append(comm[0][1:])
assert rows==sm(g,H)
assert det(H)==parse('(s-1)*(t-1)*(t+1)/t**4')
assert det(rows)==parse('(s-1)**6*(t-1)**6*(t+1)/t**4')
corrections=['0','-s*t','s*t**2','0','0','0','s*(s*t-t-1)','s*t**2','0','0','0']
for rec,value in zip(symbolic['source_records'],corrections):
    assert parse(rec['principal_correction'])==parse(value)
seed=next(r for r in symbolic['seed_records'] if r['index']==25)
assert seed['label']=='cross_4_-1_1'
assert parse(seed['scalar'])==parse('1/(s*t)')
assert parse(seed['socle_value'])==parse('s*t-1')
result={
 'status':'PASS_EXACT_DISPLAYED_FORMULAS',
 'proof_source_sha256_read_by_root':'91dbd2e919ebda809dcfaa61f05d2ee465ef67739252b34991fb29fc44c9d21f',
 'symbolic_input_sha256':hashlib.sha256((HERE/'affine_product_one_two_parameter_stage_output.json').read_bytes()).hexdigest(),
 'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'source_commutator_indices':[2,4,5,6,7],
 'F27_16_matrix_exact':True,'F27_17_both_determinants_exact':True,
 'F27_15_all_eleven_principal_corrections_exact':True,
 'F27_18_named_seed_label_scalar_and_value_exact':True,
 'method':'Integral Laurent arithmetic from the separately read independent checker; all five explicit rows and all eleven printed corrections compared with their literal-word-audited matrices.'}
(HERE/'displayed_formulas_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
