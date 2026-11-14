#!/usr/bin/env python3
"""Restore every binary certificate of the checked archive and compare all bytes."""
from pathlib import Path
import hashlib,json,subprocess,sys,zipfile
from materialize_archive_files import plan_binary_aliases,inside,materialize

R=Path(__file__).resolve().parent
Z=R.parent/'LM7_FERMAT_TOWER.zip'
T=R/'fresh229_binary'
assert not T.exists()
payload={};sizes={}
with zipfile.ZipFile(Z) as z:
    for i in z.infolist():
        rel=i.filename.removeprefix('LM7_FERMAT_TOWER/')
        if Path(rel).suffix in {'.bin','.npz','.npy'}:
            payload[rel]=z.read(i);sizes[rel]=i.compress_size
plan=plan_binary_aliases(payload)
names={x['path'] for x in plan['aliases']}
assert len(names)>0
for name,b in payload.items():
    if name in names:continue
    p=T/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
(T/'ledger').mkdir()
(T/'ledger/archive_binary_aliases.json').write_text(json.dumps(plan,indent=2)+'\n')
script=R/'materialize_archive_files.py'
p=subprocess.run([sys.executable,str(script),'--root',str(T)],capture_output=True)
script.with_suffix('.out').write_bytes(p.stdout);script.with_suffix('.err').write_bytes(p.stderr)
assert p.returncode==0 and p.stderr==b''
first=json.loads(p.stdout)
assert first['counts']['binary']['files_created']==len(names)
for name,b in payload.items():assert (T/name).read_bytes()==b,name
q=subprocess.run([sys.executable,str(script),'--root',str(T),'--verify-only'],capture_output=True)
(R/'materialize_archive_files_verify.out').write_bytes(q.stdout)
(R/'materialize_archive_files_verify.err').write_bytes(q.stderr)
assert q.returncode==0 and q.stderr==b''
assert json.loads(q.stdout)['counts']['binary']['files_created']==0

# Exact safety properties of the restorer on separate owned fixtures.
for name in ['../outside.bin','/outside.bin','code/../outside.bin','code/not_data.py']:
    try:inside(T,name,'binary')
    except AssertionError:pass
    else:raise AssertionError('unsafe path accepted: '+name)
fixture=R/'negative229_binary';fixture.mkdir()
(fixture/'code').mkdir();(fixture/'ledger').mkdir()
(fixture/'code/source.bin').write_bytes(b'original certificate')
(fixture/'code/target.bin').write_bytes(b'different certificate')
row={'path':'code/target.bin','storage_path':'code/source.bin','bytes':20,
     'sha256':hashlib.sha256(b'original certificate').hexdigest()}
assert len(b'original certificate')==20
(fixture/'ledger/archive_binary_aliases.json').write_text(json.dumps({'format_version':1,'aliases':[row]}))
try:materialize(fixture)
except AssertionError:pass
else:raise AssertionError('different target overwritten')
assert (fixture/'code/target.bin').read_bytes()==b'different certificate'
(fixture/'code/link.bin').symlink_to('source.bin')
try:inside(fixture,'code/link.bin','binary')
except AssertionError:pass
else:raise AssertionError('symlink accepted')

out={'status':'PASS','archive_sha256':hashlib.sha256(Z.read_bytes()).hexdigest(),
     'logical_binary_files':len(payload),'physical_binary_files':len(payload)-len(names),
     'restored_aliases':len(names),'every_complete_original_byte_string_equal':True,
     'logical_binary_bytes':sum(map(len,payload.values())),
     'compressed_binary_bytes_avoided':sum(sizes[n] for n in names),
     'first_execution':first,'verify_only_execution':json.loads(q.stdout),
     'rejects_escaping_paths_wrong_suffix_symlinks_and_nonmatching_existing_target':True,
     'plan':plan}
s=json.dumps(out,indent=2)+'\n'
(R/'binary_roundtrip229.json').write_text(s)
print(json.dumps({k:v for k,v in out.items() if k!='plan'},indent=2))
