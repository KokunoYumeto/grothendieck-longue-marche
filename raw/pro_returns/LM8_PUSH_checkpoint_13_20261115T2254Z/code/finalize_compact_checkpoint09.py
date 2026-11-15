#!/usr/bin/env python3
"""Apply independently verified proof-prefix deduplication to checkpoint09."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,zipfile

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT.parent/'checkpoint09_compact/LM8_PUSH_checkpoint_09.zip'
OUT=ROOT.parent/'checkpoint09_compact_verified'
OUT.mkdir(exist_ok=True)
DEST=OUT/SRC.name
if DEST.exists():raise SystemExit('Refusing to overwrite '+str(DEST))
mapping=json.loads((ROOT/'code/pbc_compact_trace_reconstruction.json').read_text())
with zipfile.ZipFile(SRC) as z:
    cm=json.loads(z.read('CHECKPOINT_COMPRESSION_MAP.json'))
    prior_manifest=json.loads(z.read('PACKAGE_MANIFEST.json'))
    transforms={e['original_path']:e for e in cm['transforms']}
    omitted=set()
    reconstructed=[]
    for kind,row in mapping['reconstructions'].items():
        path='code/'+row['superseded_gzip'];entry=transforms[path]
        assert entry['decoded_sha256']==row['complete_sha256']
        assert entry['decoded_bytes']==row['complete_bytes']
        assert entry['original_sha256']==row['original_valid_gzip_sha256']
        source='code/'+row['retained_source_payload']
        row['stored_source_path']=transforms[source]['stored_path']
        row['original_path']=path
        row['kind']=kind
        omitted.add(entry['stored_path'])
        reconstructed.append(row)
    cm['transforms']=[e for e in cm['transforms'] if e['stored_path'] not in omitted]
    cm['exact_prefix_reconstructions']=reconstructed
    cm['prefix_audit']='code/pbc_checkpoint09_immutable_prefix_audit.json'
    cm['all_complete_and_partial_proof_records_retained']=True
    restore=z.read('RESTORE_LARGE_LOGS.py').decode()
    restore+='''\n# Exact independently audited reconstruction of redundant proof prefixes.
import subprocess,sys
for e in mapping.get('exact_prefix_reconstructions',[]):
    target=dest/e['original_path']
    if target.exists():
        print('EXISTS, unchanged:',target);continue
    subprocess.run([sys.executable,str(base/'code/pbc_trace_reconstruction.py'),
                    str(base/'code/pbc_compact_trace_reconstruction.json'),e['kind'],
                    str(base/e['stored_source_path']),str(target)],check=True)
'''
    note='''\n## Exact prefix deduplication in the saved compact checkpoint\n\nTwo redundant XZ payloads are represented by fully checked prefix rules instead
of duplicate bytes. The native-v1 complete log is the first16,749,555 records
of the retained boundary JSONL after ASCII-space removal; its33-byte partial
record remains separate. The native-v4 complete log is the first959,651 records
of the frozen native-v5 payload; its48-byte partial record remains separate.
Every complete and partial byte was compared directly against the immutable
original checkpoint09, and the reconstruction checks exact decoded SHA256.
The original gzip-wrapper hashes remain recorded. The saved archive includes
the executable reconstruction program and every independent equality audit.
RESTORE_LARGE_LOGS.py restores these two logs automatically after restoring
the distinct compressed payloads. The exact stored v5 input path is
code/pbc_native_modular_v5_iterated_trace.jsonl.gz.payload.xz.
This removes duplicate serialization only, with no omitted mathematical record.
'''
    additions={
        'CHECKPOINT_COMPRESSION_MAP.json':(json.dumps(cm,indent=2)+'\n').encode(),
        'RESTORE_LARGE_LOGS.py':restore.encode(),
        'code/pbc_compact_trace_reconstruction.json':(json.dumps(mapping,indent=2)+'\n').encode(),
        'code/finalize_compact_checkpoint09.py':Path(__file__).read_bytes(),
        'notes/checkpoint09_upload_recovery.md':z.read('notes/checkpoint09_upload_recovery.md')+note.encode(),
        'LM8_PUSH_report.md':z.read('LM8_PUSH_report.md')+note.encode(),
    }
    for path in [
        'code/pbc_trace_reconstruction.py',
        'code/pbc_checkpoint09_immutable_prefix_audit.json',
        'code/pbc_interrupted_stream_payload_equivalence.json',
        'code/pbc_native_boundary_payload_prefix.json',
        'code/pbc_native_v4_v5_payload_prefix.json',
        'code/pbc_verify_pack_payloads.py',
        'notes/pbc_checkpoint09_compression_audit.md',
    ]:additions[path]=(ROOT/path).read_bytes()
    entries=[]
    with zipfile.ZipFile(DEST,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as out:
        def add(name,data):
            out.writestr(name,data,compress_type=zipfile.ZIP_STORED if name.endswith('.xz') else zipfile.ZIP_DEFLATED)
            entries.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        for name in z.namelist():
            if name in omitted or name in additions or name=='PACKAGE_MANIFEST.json':continue
            add(name,z.read(name))
        for name,data in additions.items():add(name,data)
        manifest={'created_utc':datetime.now(timezone.utc).isoformat(),
                  'kind':'checkpoint09 upload-limit recovery, exact prefix deduplication',
                  'file_count':len(entries),'files':entries,
                  'original_snapshot_created_utc':mapping['immutable_snapshot_created_utc'],
                  'compression_map':'CHECKPOINT_COMPRESSION_MAP.json'}
        out.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(DEST) as z:
    bad=z.testzip();assert bad is None,bad
    assert len(z.namelist())==len(set(z.namelist()))
h=hashlib.sha256()
with DEST.open('rb') as f:
    for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
result={'file':str(DEST),'bytes':DEST.stat().st_size,'sha256':h.hexdigest(),
        'files':len(entries),'below_upload_limit':DEST.stat().st_size<=536870912}
(OUT/'repack_result.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'notes/checkpoint09_upload_recovery.md').write_bytes(additions['notes/checkpoint09_upload_recovery.md'])
(ROOT/'notes/checkpoint09_compression_map.json').write_text(json.dumps(cm,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
assert result['below_upload_limit']
