"""Bind an existing nested execution record to its retained consumer."""
from pathlib import Path
import hashlib,json

BASE=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=BASE/'code/root_e120_audit/theta_distribution_fresh/code/a_e120_exact.py'
s=p.with_name(p.stem+'_status.json');data=json.loads(s.read_text())
e=data['execution']
assert data['status']=='silent module executed successfully'
assert data['exit_code']==e['exit_code']==0 and e['program']==p.name
assert e['arguments']==[] and e['source_sha256']==sha(p)
for kind,suffix in [('stdout','.out'),('stderr','.err')]:
    q=p.with_suffix(suffix)
    assert q.read_bytes()==b'' and e[kind+'_bytes']==0
    assert sha(q)==e[kind+'_sha256']
c=p.parent/'a_theta_principal_distribution.py'
assert 'a_e120_exact' in c.read_text()
assert c.with_suffix('.out').stat().st_size>0
assert c.with_suffix('.err').read_bytes()==b''
result={'status':'PASS','bindings':{
    str(p.relative_to(BASE)):{'status_file':str(s.relative_to(BASE)),
    'status_sha256':sha(s),'source_sha256':sha(p),
    'consumer':str(c.relative_to(BASE)),'consumer_source_sha256':sha(c),
    'consumer_stdout_sha256':sha(c.with_suffix('.out')),
    'consumer_stderr_sha256':sha(c.with_suffix('.err'))}}}
dest=BASE/'ledger/silent_consumer_bindings229.json'
assert not dest.exists()
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
