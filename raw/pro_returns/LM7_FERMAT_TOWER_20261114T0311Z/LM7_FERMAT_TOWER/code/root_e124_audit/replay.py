#!/usr/bin/env python3
"""Independent full-freeze check and copied nine-stage replay for E124."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys

B=Path(__file__).resolve().parent
R=B.parent
A=R/'research_after_e123'
GP=R/'research_e52/vendor/pari-2.19.0/Olinux-x86_64/gp-dyn'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mp=A/'ledger/e_fiftythree_ordinary_manifest.json'
assert sha(mp)=='2ee0a1016536f05016a20f99b92b2fb813ebf0959330b7414cd9847cdcee943c'
m=json.loads(mp.read_text())
assert m['statement']=='E.124' and m['status']=='FROZEN'
assert len(m['owned_files'])==153 and len(m['immutable_inputs'])==8
def check():
    for x in m['owned_files']+m['immutable_inputs']:
        p=A/x['path']
        assert p.stat().st_size==x['bytes'] and sha(p)==x['sha256'],x['path']
check()
shutil.copy2(mp,B/'author_manifest.json')
shutil.copy2(A/m['proof'],B/'author_proof.tex')
assert sha(B/'author_proof.tex')=='19c6cdbe199e3011f4c6dd437d54fbf4fb6db02ae396ff6aad890210daeae671'
T=B/'replay_tree'
T.mkdir()
C=T/'code';C.mkdir()
for x in m['immutable_inputs']:
    p=T/x['path'];p.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(A/x['path'],p)
names=['e53_ordinary_kernel.gp','e53_ordinary_summary.py',
       'e53_positional_residues.py','e53_ordinary_saturation.py',
       'e53_ordinary_frobenius_input.py','e53_ordinary_frobenius.gp',
       'e53_ordinary_genus_chars.py','e53_ordinary_genus.gp',
       'e53_ordinary_maps.py']
for name in names:
    p=A/'code'/name;shutil.copy2(p,C/name)
    for s in ['.out','.err','.json','.bin']:
        q=p.with_suffix(s)
        if q.exists():shutil.copy2(q,C/q.name)
driver=C/'e53_ordinary_replay.py'
shutil.copy2(A/'code'/driver.name,driver)
p=subprocess.run([sys.executable,str(driver),'--gp',str(GP),'--label','root_fresh'],
                 cwd=T,capture_output=True)
driver.with_suffix('.out').write_bytes(p.stdout)
driver.with_suffix('.err').write_bytes(p.stderr)
assert p.returncode==0 and p.stderr==b'',(p.returncode,p.stderr.decode())
v=json.loads((T/'audit/root_fresh/verification.json').read_text())
assert v['status']=='PASS' and v['excluded_fields']==[]
assert len(v['steps'])==9
assert all(x['exit_code']==0 and x['stdout_byte_identity'] and x['stderr_byte_identity'] for x in v['steps'])
assert v['generated_input_byte_identity']
assert len(v['complete_GEN_comparisons'])==2
assert all(x['complete_GEN_identity'] for x in v['complete_GEN_comparisons'])
F=T/'audit/root_fresh/fresh/code'
sat=json.loads((F/'e53_ordinary_saturation.json').read_text())
maps=json.loads((F/'e53_ordinary_maps.json').read_text())
assert sat['status']=='PASS' and sat['rank']==9
assert maps['status']=='PASS' and maps['upper_elements_checked']==729
assert maps['lower_elements_checked']==243 and maps['all_lift_extension_checks']==729
check()
out={'status':'PASS','statement':'E.124','manifest_sha256':sha(mp),
     'whole_proof_sha256':sha(B/'author_proof.tex'),
     'owned_files_checked_before_and_after':153,'immutable_inputs_checked_before_and_after':8,
     'mathematical_stages':9,'whole_stdout_and_stderr_byte_identity':True,
     'whole_JSON_byte_identity':v['JSON_byte_identity'],
     'all_generated_input_byte_identity':True,
     'complete_GEN_comparisons':v['complete_GEN_comparisons'],
     'raw_binary_comparisons':v['raw_binary_comparisons'],
     'residue_basis_rank':sat['rank'],'upper_elements':729,'lower_elements':243,
     'all_actual_extension_lift_checks':729,'excluded_fields':[],
     'author_sources_modified':False,'upper_BNF_computation':False}
s=json.dumps(out,indent=2)+'\n'
(B/'replay_audit.json').write_text(s)
print(s,end='')
