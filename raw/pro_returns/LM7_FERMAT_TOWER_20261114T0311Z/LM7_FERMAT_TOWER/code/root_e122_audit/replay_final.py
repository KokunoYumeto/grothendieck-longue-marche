#!/usr/bin/env python3
"""Root replay of the frozen E122 complete certificate, preserving author bytes."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys

W=Path(__file__).resolve().parents[1]
R=W/'research_e122'
A=Path(__file__).resolve().parent
M=R/'ledger/e_fiftythree_higher_manifest.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(M)=='9f63758a401fad7db429d657ab7008f98d0f4e864580b9ca517876597735cd9e'
m=json.loads(M.read_text())
def check_frozen():
    for f in m['files']:
        p=R/f['path']
        assert p.stat().st_size==f['bytes'] and sha(p)==f['sha256'],f['path']
check_frozen()
C=A/'final_replay_reference'
D=A/'final_fresh_replay'
assert not C.exists() and not D.exists()
(C/'code').mkdir(parents=True)
shutil.copytree(R/'inputs',C/'inputs')
sources=['e53_higher_replay.py','e53_higher_maps.py','e53_literal_unit_ring.py',
         'e53_higher_local.gp','e53_higher_genus.gp','e53_upper_witness_verify.gp']
outputs=['e53_higher_maps.out','e53_higher_maps.json','e53_literal_unit_ring.out',
         'e53_literal_unit_ring.json']
for n in ['e53_higher_local','e53_higher_genus','e53_upper_witness_verify']:
    outputs += [n+'.out',n+'.bin']
for f in sources+outputs:shutil.copyfile(R/'code'/f,C/'code'/f)
shutil.copyfile(M,A/'final_author_manifest.json')
shutil.copyfile(R/'sections/E_fiftythree_higher_action.tex',A/'final_author_proof.tex')
gp=W/'research_e52/vendor/pari-2.19.0/Olinux-x86_64/gp-dyn'
cmd=[sys.executable,str(C/'code/e53_higher_replay.py'),'--gp',str(gp),'--destination',str(D)]
run=subprocess.run(cmd,cwd=C,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(A/'final_complete_replay.out').write_bytes(run.stdout)
(A/'final_complete_replay.err').write_bytes(run.stderr)
assert run.returncode==0,(run.returncode,run.stderr.decode()[-5000:])
assert not run.stderr,run.stderr.decode()
d=json.loads((D/'replay.json').read_text())
assert d['status']=='PASS' and d['excluded_fields']==[] and d['excluded_GEN_components']==[]
assert len(d['texts'])==7 and all(v['byte_identical'] for v in d['texts'].values())
assert len(d['binary_objects'])==3 and all(v['complete_decoded_GEN_identity'] for v in d['binary_objects'].values())
check_frozen()
result={'status':'PASS','frozen_manifest_sha256':sha(M),'frozen_file_count':len(m['files']),
        'proof_sha256':sha(A/'final_author_proof.tex'),'root_command':cmd,
        'exit_code':run.returncode,'root_stderr_bytes':len(run.stderr),
        'all_author_manifest_hashes_rechecked_after_execution':True,
        'whole_replay':d,'replay_json_sha256':sha(D/'replay.json'),
        'reading_scope':'Root read all624 final proof lines and all five mathematical sources; three minimum witness sources had already been independently replayed.'}
t=json.dumps(result,indent=2)+'\n'
(A/'final_replay_audit.json').write_text(t)
print(t,end='')
