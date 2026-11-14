"""Independent copied execution of the frozen E.115 certificate.

Proof and primary-source review are recorded separately; this program verifies
the full frozen manifest and actual replay outputs without ignored fields.
"""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
AUTHOR=ROOT/'research_e115'
HERE=Path(__file__).resolve().parent
REPLAY=HERE/'fresh'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path=AUTHOR/'ledger/e_quartic_mixed_five_manifest.json'
assert sha(manifest_path)=='bcdacee1fb1b149fe250d98f5fdf472c6e9b4dd5538587cc31d6d493eeb43d44'
manifest=json.loads(manifest_path.read_text())
checked=[]
for row in manifest['files']:
    p=AUTHOR/row['path']
    assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],row['path']
    checked.append(row['path'])
assert len(checked)==24
assert not REPLAY.exists()
(REPLAY/'code').mkdir(parents=True)
(REPLAY/'inputs').mkdir()
program='a_quartic_mixed_five'
shutil.copy2(AUTHOR/'code'/f'{program}.py',REPLAY/'code'/f'{program}.py')
input_hashes={}
for p in sorted((AUTHOR/'inputs').glob('*.json')):
    shutil.copy2(p,REPLAY/'inputs'/p.name)
    input_hashes[p.name]=sha(p)
assert len(input_hashes)==4
with (REPLAY/'code'/f'{program}.out').open('wb') as out, (REPLAY/'code'/f'{program}.err').open('wb') as err:
    run=subprocess.run([sys.executable,'code/'+program+'.py','--input-dir','inputs'],cwd=REPLAY,stdout=out,stderr=err)
assert run.returncode==0,run.returncode
outputs={}
for suffix in ['.json','.out','.err']:
    a=AUTHOR/'code'/(program+suffix)
    b=REPLAY/'code'/(program+suffix)
    assert a.read_bytes()==b.read_bytes(),suffix
    outputs[suffix]={'author_sha256':sha(a),'replay_sha256':sha(b),'byte_identical':True}
data=json.loads((REPLAY/'code'/(program+'.json')).read_text())
assert data['status']=='PASS' and data['statement']=='E.115'
assert data['actual_residual_translation_tests']['cocycle_equation_rank']==62
assert data['actual_residual_translation_tests']['cocycle_equations']==2048
assert data['actual_residual_translation_tests']['H1_dimension']==0
assert data['actual_CM_contraction_maps']['contraction_rank']==6
for name,digest in input_hashes.items():
    assert sha(REPLAY/'inputs'/name)==digest
    assert sha(AUTHOR/'inputs'/name)==digest
for row in manifest['files']:
    assert sha(AUTHOR/row['path'])==row['sha256']
result={'statement':'E.115','status':'PASS','manifest_sha256':sha(manifest_path),'manifest_files_verified':len(checked),'author_files_unchanged':True,'four_frozen_inputs_unchanged':True,'command':[sys.executable,'code/'+program+'.py','--input-dir','inputs'],'exit_code':run.returncode,'complete_output_comparison':outputs,'ignored_fields':[],'input_hashes':input_hashes,'proof_verification_claimed_by_this_program':False}
(HERE/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
