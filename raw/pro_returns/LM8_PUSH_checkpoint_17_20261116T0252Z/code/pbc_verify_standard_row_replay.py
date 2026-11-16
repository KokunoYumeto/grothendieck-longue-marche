#!/usr/bin/env python3
"""Compare EVERY decoded byte of the completed fresh standard-row proof log."""
from pathlib import Path
import gzip,hashlib,json,subprocess,tempfile,time
root=Path(__file__).resolve().parents[1];c=root/'code';cache=root.parent/'checkpoint14_standard_replay';cache.mkdir(exist_ok=True)
trace=c/'pbc_quotient86_standard2_trace.jsonl.gz';data=c/'pbc_quotient86_standard2.dat';rows=c/'pbc_quotient86_standard2_rows.dat'
cpp=c/'pbc_native_primary_search.cpp';exe=c/'pbc_native_primary_search'
def sha(p):
    p=Path(p)
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
prep=json.loads((c/'pbc_quotient86_standard2_preparation.json').read_text())
assert sha(data)==prep['input_sha256'] and sha(rows)==prep['rows_sha256']
start=time.time();h=hashlib.sha256();size=records=0;next_report=100000000
log=cache/'pbc_standard2_replay_native.out'
with tempfile.TemporaryDirectory(prefix='standard_rows_',dir=cache) as td,log.open('w') as err:
    cmd=[str(exe),str(data),'/dev/stdout',str(Path(td)/'certificate.json'),str(rows),'2']
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=err)
    try:
        with gzip.open(trace,'rb') as orig,gzip.GzipFile(fileobj=proc.stdout,mode='rb') as fresh:
            for b in iter(lambda:fresh.read(1<<20),b''):
                expected=orig.read(len(b));assert b==expected,('exact byte mismatch',size)
                h.update(b);size+=len(b);records+=b.count(b'\n')
                if size>=next_report:print(json.dumps({'matched_bytes':size,'seconds':time.time()-start}),flush=True);next_report+=100000000
            assert orig.read(1)==b''
        assert proc.wait()==0
    except BaseException:proc.kill();proc.wait();raise
scope='Exact lossless serialization of the fresh standard-GAP-row modular search. This storage certificate is independent of its mathematical source-replay and full lifting gates.'
m=dict(codec='PBC_REPLAY01',kind='gzip_payload',prime=2,
       original_path=str(trace.relative_to(root)),original_sha256=sha(trace),original_bytes=trace.stat().st_size,
       decoded_sha256=h.hexdigest(),decoded_bytes=size,original_records=records,
       entire_original_byte_comparison=True,entire_decoded_byte_hash_verified=True,
       source_dat=str(data.relative_to(root)),source_dat_sha256=sha(data),
       identity_rows_path=str(rows.relative_to(root)),identity_rows_sha256=sha(rows),identity_rows=9000,
       replay_source=str(cpp.relative_to(root)),replay_source_sha256=sha(cpp),
       replay_executable=str(exe.relative_to(root)),replay_executable_sha256=sha(exe),
       build_dependencies=[dict(path='code/pbc_positive_collector_control.hpp',sha256=sha(c/'pbc_positive_collector_control.hpp'))],
       verification_command=cmd,verifier_sha256=sha(__file__),seconds=time.time()-start,scope=scope)
recipe=c/'pbc_quotient86_standard2_replay_recipe.json';recipe.write_text(json.dumps(m,indent=2)+'\n')
ledger={k:m[k] for k in ('codec','kind','original_path','original_sha256','original_bytes','decoded_sha256','decoded_bytes','entire_decoded_byte_hash_verified')}
ledger.update(stored_path=str(recipe.relative_to(root)),local_encoded_file=str(recipe),stored_sha256=sha(recipe),stored_bytes=recipe.stat().st_size,
              additional_payloads=[],restore_command=['{python}','{archive}/code/pbc_restore_standard_row_replay.py','{archive}/'+str(recipe.relative_to(root)),'{target}','--sha256',h.hexdigest()],note=scope)
for dest in (c/'pbc_quotient86_standard2_replay_transform.json',cache/'pbc_quotient86_standard2_replay_transform.json'):
    dest.write_text(json.dumps(ledger,indent=2)+'\n')
print(json.dumps(dict(status='PASS',decoded_bytes=size,decoded_sha256=h.hexdigest(),records=records,seconds=m['seconds'],transform=str(cache/'pbc_quotient86_standard2_replay_transform.json')),indent=2),flush=True)
