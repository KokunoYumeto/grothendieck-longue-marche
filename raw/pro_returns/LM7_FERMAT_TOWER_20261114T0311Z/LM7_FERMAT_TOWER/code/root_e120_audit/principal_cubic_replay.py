#!/usr/bin/env python3
"""Replay the frozen framed cubic-cover comparison in a source-only tree."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys

B=Path(__file__).resolve().parent
A=B.parent/'research_e120'
mp=A/'ledger/a_principal_cubic_cover_manifest.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(mp)=='e26f6e1ab7d3998b0d530a2f8e0be3c5aeb41c20a7255c74afab6b0ea5de18f3'
m=json.loads(mp.read_text())
assert len(m['owned'])==5 and len(m['immutable_inputs'])==7
def check():
    for x in m['owned']+m['immutable_inputs']:
        p=A/x['path'];assert p.stat().st_size==x['bytes'] and sha(p)==x['sha256'],x['path']
check()
shutil.copy2(mp,B/'principal_cubic_author_manifest.json')
shutil.copy2(A/'notes/principal_cubic_cover.md',B/'principal_cubic_author_note.md')
T=B/'principal_cubic_fresh';T.mkdir()
for x in m['immutable_inputs']:
    p=T/x['path'];p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(A/x['path'],p)
name='a_principal_cubic_cover.py'
p=T/'code'/name;shutil.copy2(A/'code'/name,p)
r=subprocess.run([sys.executable,str(p)],cwd=T,capture_output=True)
p.with_suffix('.out').write_bytes(r.stdout);p.with_suffix('.err').write_bytes(r.stderr)
assert r.returncode==0 and r.stderr==b''
outputs=[]
for suffix in ['.out','.err','.json']:
    q=p.with_suffix(suffix);a=(A/'code'/name).with_suffix(suffix)
    assert q.read_bytes()==a.read_bytes(),suffix
    outputs.append({'file':q.name,'bytes':q.stat().st_size,'sha256':sha(q),'complete_byte_identity':True})
check()
out={'status':'PASS','manifest_sha256':sha(mp),
     'whole_note_sha256':sha(B/'principal_cubic_author_note.md'),
     'owned_files_checked_before_and_after':5,'immutable_inputs_checked_before_and_after':7,
     'program_sha256':sha(p),'exit_code':r.returncode,'outputs':outputs,
     'excluded_fields':[],'author_sources_modified':False}
s=json.dumps(out,indent=2)+'\n';(B/'principal_cubic_replay_audit.json').write_text(s);print(s,end='')
