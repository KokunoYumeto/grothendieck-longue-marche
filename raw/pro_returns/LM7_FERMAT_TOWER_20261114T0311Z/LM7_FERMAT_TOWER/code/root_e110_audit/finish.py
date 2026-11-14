"""Record the complete E110 replay and the exact binary-deserialization comparison."""
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[1]
HERE=Path(__file__).resolve().parent
SRC=ROOT/'research_e110'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=SRC/'ledger/e_pure_tower_manifest.json'
mf=json.loads(manifest.read_text())
for r in mf['files']:
    p=SRC/r['path']
    assert sha(p)==r['sha256'] and p.stat().st_size==r['bytes']
first=(HERE/'verify.out').read_text()
assert 'AssertionError: e_pure_tower_base.bin' in first
assert 'assert actual.read_bytes()==expected.read_bytes(),name' in first
checks=[]
for name in ['e_pure_tower.out','e_pure_tower.json','e_pure_tower_base_gp.out']:
    old=SRC/'code'/name;new=HERE/'fresh/code'/name
    assert old.read_bytes()==new.read_bytes(),name
    checks.append({'file':name,'complete_byte_equality':True,'sha256':sha(new)})
binary=(HERE/'binary_compare.out').read_text()
assert '***' not in binary
assert 'Full readbin vectors equal: 1' in binary
assert 'Exact identity test: 1' in binary
assert 'Top-level components: 7' in binary
assert binary.count('identical=1')==7
a=SRC/'code/e_pure_tower_base.bin';b=HERE/'fresh/code/e_pure_tower_base.bin'
ab,bb=a.read_bytes(),b.read_bytes()
assert len(ab)==len(bb) and ab!=bb
record={'status':'PASS after exact deserialization comparison',
        'manifest_sha256':sha(manifest),'manifest_files_verified':len(mf['files']),
        'proof_sha256':sha(SRC/'sections/E_pure_tower_complete.tex'),
        'complete_math_execution_exit_code':0,
        'first_audit_driver_exit_code':1,
        'first_audit_failure':'Raw PARI writebin bytes differed; retained complete failing driver and its actual output.',
        'checks':checks,'excluded_fields_in_text_or_JSON':[],
        'binary_comparison':{'raw_bytes_equal':False,'bytes_each':len(ab),
          'byte_difference_count':sum(x!=y for x,y in zip(ab,bb)),
          'frozen_sha256':sha(a),'fresh_sha256':sha(b),
          'actual_morphism':'PARI read(file) deserializes both retained binary files into full GEN vectors.',
          'full_deserialized_exact_identity':True,'all_seven_components_identical':True,
          'proof_program':'binary_compare.gp','actual_output':'binary_compare.out',
          'actual_compare_exit_code':0},
        'root_read_scope':'Entire E110 statement and proof and both mathematical source programs; Kato Theorem1.1(1), its coherent definition, the complete unconditional rank argument in Section3.2, and the actual norm/cohomology comparison and proof passages opened at turn937view0, turn938view0-3 and turn939view0-3.',
        'mathematical_audit':'PASS: literal local corestriction fixes the common-root characters at every height; ambiguous classes vanish; degree-two maps and negative conjugation give the pure class and unit statements. Compact unit fibres give every coherent divisor. The actual character maps evaluate the compact kernel, whose unbounded ranks follow from the cited unconditional universal-norm theorem. Substitution into the two actual norm formulas proves both toric inclusions and all fibre inverses, including kappa7 and unit multiples of the first class.',
        'retained_scope':'Exact H target with first unit multiple of kappa3(17); unrestricted and intrinsic source tasks remain active.'}
(HERE/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
