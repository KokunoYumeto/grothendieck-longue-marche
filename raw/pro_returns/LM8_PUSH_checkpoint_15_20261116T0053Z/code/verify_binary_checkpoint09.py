#!/usr/bin/env python3
"""Independently restore one entire frozen proof log with the portable decoder."""
from pathlib import Path
import hashlib,json,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT.parent/'checkpoint09_binary'
NAME='code/pbc_iterated_modular_trace.jsonl'
ledger=json.loads((CACHE/(NAME+'.pbcbin.xz.json')).read_text())
dest=CACHE/'root_python_verification'/Path(NAME).name
if dest.exists():
    raise SystemExit('Refusing to overwrite '+str(dest))
result=subprocess.run([sys.executable,str(ROOT/'code/pbc_trace_binary_decode.py'),
                       str(CACHE/ledger['stored_path']),str(dest),
                       '--sha256',ledger['decoded_sha256']],
                      check=True,capture_output=True,text=True)
h=hashlib.sha256()
with dest.open('rb') as f:
    for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
assert h.hexdigest()==ledger['decoded_sha256']
assert dest.stat().st_size==ledger['decoded_bytes']
report={'status':'PASS','method':'Entire-log portable Python decoder independent of the C++ encoder/decoder',
        'original_path':NAME,'decoded_bytes':dest.stat().st_size,'decoded_sha256':h.hexdigest(),
        'decoder_stdout':result.stdout,'decoder_stderr':result.stderr,
        'temporary_duplicate':'The restored verification file is byte-identical to the frozen original. It is represented in the checkpoint by that original payload and the exact reconstruction program, not by an additional duplicate copy.'}
(ROOT/'notes/checkpoint09_binary_portable_verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
