"""Bounded lookup and exact-source-delta controls; no integration or recovery."""
from pathlib import Path
import ast,copy,difflib,hashlib,importlib.util,io,json,zipfile

BASE=Path(__file__).resolve().parent
ROOT=Path.cwd()
spec=importlib.util.spec_from_file_location('staged_captured_gate',BASE/'checkpoint_gate_adapter.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
q=json.loads((BASE/'CLASSIFICATION.json').read_bytes())
snapshot=json.loads((ROOT/a.SNAPSHOT).read_bytes())
controls=[]

def passed(label):controls.append(dict(control=label,status='PASS'))
def rejected(label, action):
 try:action()
 except (ValueError,KeyError):passed(label)
 else:raise AssertionError('Accepted invalid control: '+label)

original=(BASE/'integrate_revision864_residuals.before.py').read_text()
assert a.sha(original.encode())==a.ORIGINAL_SHA
assert original==(ROOT/a.ORIGINAL).read_text()
assert original.count(a.OLD_SPAN)==1
proposed=original.replace(a.OLD_SPAN,a.NEW_SPAN,1)
assert proposed.replace(a.NEW_SPAN,a.OLD_SPAN,1)==original
oldtree=ast.parse(original);newtree=ast.parse(proposed)
assert len(oldtree.body)==len(newtree.body)
changed=[]
for before,after in zip(oldtree.body,newtree.body):
 if ast.dump(before)!=ast.dump(after):changed.append(getattr(before,'name',None))
assert changed==['checkpoint_gate']
passed('Exactly reversible assertion-span replacement; only checkpoint_gate AST differs')
assert a.sha((BASE/'CLASSIFICATION.json').read_bytes())==a.CLASSIFICATION_SHA
assert len(q['rows'])==950 and len({x['original_path'] for x in q['rows']})==950
assert q['absent_original_names']==950 and q['unique_archived_primitive_payloads_checked']==754
passed('Closed qualification pins all 950 mappings and 754 independently read primitive payloads')
for r in q['rows']:
 s=snapshot['files'][r['snapshot_file_index']]
 assert all(s[k]==r[k] for k in ('original_path','snapshot_path','sha256','bytes'))
 assert (s['snapshot_sha256'],s['snapshot_bytes'])==(r['sha256'],r['bytes'])
passed('Every qualification matches the exact immutable snapshot row and index')

approved=q['rows'][0];row=snapshot['files'][approved['snapshot_file_index']];data=(ROOT/approved['original_path']).read_bytes()
expected=dict(sha256=approved['sha256'],bytes=approved['bytes'])
canonical=dict(path=approved['canonical_logical_path'],storage_kind='blob',object_path=approved['archive_object_path'],**expected)
captured=dict(path=approved['snapshot_path'],storage_kind='alias',target_path=canonical['path'],**expected)
logical={canonical['path']:canonical,captured['path']:captured}

def container(payload):
 stream=io.BytesIO()
 with zipfile.ZipFile(stream,'w',compression=zipfile.ZIP_DEFLATED) as z:z.writestr(approved['archive_object_path'],payload)
 stream.seek(0)
 return zipfile.ZipFile(stream)

with container(data) as z:
 lookup=a.CapturedLookup(q);lookup(z,logical,row,expected,approved['snapshot_file_index'])
 assert lookup.used=={row['original_path']} and len(lookup.objects)==1
 passed('Qualified absent name resolves only through exact snapshot one-hop alias and hashed primitive bytes')
 rejected('Repeated use of an approved mapping is rejected',lambda:lookup(z,logical,row,expected,approved['snapshot_file_index']))
 def run(l=logical,r=row,e=expected,i=approved['snapshot_file_index']):a.CapturedLookup(q)(z,l,r,e,i)
 bad=copy.deepcopy(logical);bad[row['original_path']]=dict(path=row['original_path'],**expected)
 rejected('An authority whose original unexpectedly becomes present is rejected',lambda:run(l=bad))
 badrow=dict(row,original_path='synthetic/unqualified.tex')
 rejected('An unlisted absent original is rejected',lambda:run(r=badrow))
 rejected('Wrong snapshot row index is rejected',lambda:run(i=approved['snapshot_file_index']+1))
 rejected('Wrong snapshot copy locator is rejected',lambda:run(r=dict(row,snapshot_path='synthetic/wrong-copy.tex')))
 rejected('Changed packaged length is rejected',lambda:run(e=dict(expected,bytes=expected['bytes']+1)))
 bad=copy.deepcopy(logical);bad[row['snapshot_path']]['sha256']='0'*64
 rejected('Changed captured logical identity is rejected',lambda:run(l=bad))
 bad=copy.deepcopy(logical);bad[canonical['path']]['storage_kind']='alias'
 rejected('A chained alias or recipe cannot replace the qualified primitive',lambda:run(l=bad))
 direct=dict(original_path='synthetic/present.tex');directlogical={direct['original_path']:dict(expected)}
 k=a.CapturedLookup(q);k(z,directlogical,direct,expected,1);assert k.direct==1 and not k.used
 passed('Present originals retain the exact direct-name check without captured fallback')
 bad=copy.deepcopy(directlogical);bad[direct['original_path']]['sha256']='0'*64
 rejected('Present-but-mismatching original is rejected even if a captured row could exist',lambda:run(l=bad,r=direct))
with container(data[:-1]+bytes([data[-1]^1])) as z:
 rejected('Same-length corrupted primitive bytes are rejected by SHA256',lambda:a.CapturedLookup(q)(z,logical,row,expected,approved['snapshot_file_index']))

patch=''.join(difflib.unified_diff(original.splitlines(True),proposed.splitlines(True),fromfile='original-integrator9bc6751a/checkpoint_gate',tofile='explicit-post-CP11-captured-lookup/checkpoint_gate'))
(BASE/'CHECKPOINT_GATE_ONLY.diff').write_text(patch)
result=dict(schema='revision864-cp11-gate-adapter-bounded-controls-v1',status='PASS',controls=controls,counts=dict(passed=len(controls),failed=0),scope='Exact original-function reversibility/AST and bounded in-memory logical/primitive payload controls. No original full gate, source integration, restore, publication rendering, or observations executed.',pins=[dict(artifact=p.name,sha256=a.digest(p),bytes=p.stat().st_size) for p in [BASE/'checkpoint_gate_adapter.py',BASE/'CLASSIFICATION.json',BASE/'integrate_revision864_residuals.before.py',BASE/'CHECKPOINT_GATE_ONLY.diff',Path(__file__)]],production_inputs_modified=False)
with (BASE/'CONTROLS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(dict(status='PASS',controls=len(controls),adapter_sha256=a.digest(BASE/'checkpoint_gate_adapter.py'),controls_sha256=a.digest(BASE/'CONTROLS.json'),patch_sha256=a.digest(BASE/'CHECKPOINT_GATE_ONLY.diff'))))
