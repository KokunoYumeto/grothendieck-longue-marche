#!/usr/bin/env python3
"""Replace generic compressed logs with fully verified reversible proof encoding."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,zipfile

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'checkpoint09_compact_verified/LM8_PUSH_checkpoint_09.zip'
CACHE=ROOT.parent/'checkpoint09_binary'
OUT=ROOT.parent/'checkpoint09_saved'
OUT.mkdir(exist_ok=True)
DEST=OUT/SOURCE.name
if DEST.exists():raise SystemExit('Refusing to overwrite '+str(DEST))
conversion=json.loads((CACHE/'binary_conversion_manifest.json').read_text())
binary={e['original_path']:e for e in conversion['transforms']}
portable=json.loads((ROOT/'notes/checkpoint09_binary_portable_verification.json').read_text())
assert portable['status']=='PASS'

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

RESTORE='''#!/usr/bin/env python3
"""Restore all original proof payloads without overwriting existing files."""
from pathlib import Path
import argparse,gzip,hashlib,json,lzma,subprocess,sys
p=argparse.ArgumentParser();p.add_argument('--destination',type=Path);a=p.parse_args()
base=Path(__file__).resolve().parent;dest=a.destination or base
mapping=json.loads((base/'CHECKPOINT_COMPRESSION_MAP.json').read_text())
for e in mapping['transforms']:
    target=dest/e['original_path'];target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():
        print('EXISTS, unchanged:',target);continue
    if e.get('codec')=='PBCBIN01':
        subprocess.run([sys.executable,str(base/'code/pbc_trace_binary_decode.py'),
                        str(base/e['stored_path']),str(target),
                        '--sha256',e['decoded_sha256']],check=True)
    else:
        h=hashlib.sha256();count=0
        with lzma.open(base/e['stored_path'],'rb') as inp,target.open('xb') as raw:
            out=gzip.GzipFile(filename='',mode='wb',fileobj=raw,compresslevel=1,mtime=0) if e['kind']=='gzip_payload' else raw
            for b in iter(lambda:inp.read(1024*1024),b''):
                h.update(b);count+=len(b);out.write(b)
            if out is not raw:out.close()
        assert count==e['decoded_bytes'] and h.hexdigest()==e['decoded_sha256']
        print('RESTORED verified payload:',target)
for e in mapping.get('exact_prefix_reconstructions',[]):
    target=dest/e['original_path']
    if target.exists():
        print('EXISTS, unchanged:',target);continue
    source=dest/'code'/e['retained_source_payload']
    subprocess.run([sys.executable,str(base/'code/pbc_trace_reconstruction.py'),
                    str(base/'code/pbc_compact_trace_reconstruction.json'),
                    e['kind'],str(source),str(target)],check=True)
print('All original complete proof records restored. Partial records were retained as separate files. Superseded compression wrappers and their original hashes are documented in CHECKPOINT_COMPRESSION_MAP.json.')
'''

NOTE='''
## Reversible proof-record encoding used for the saved archive

Generic compression and exact prefix deduplication still produced698,507,600
bytes, above the536,870,912-byte upload limit. The eight distinct large proof
logs therefore use the documented PBCBIN01 reversible binary serialization,
followed by XZ. Sequential identifiers, references and arbitrary-size integer
coefficients are encoded compactly. Every unmatched or noncanonical record is
retained verbatim. This changes storage only, not any mathematical record.

Every complete decoded log was hashed directly from the immutable original
checkpoint09, encoded, decoded again in full, and checked for equal byte count
and SHA256. The portable Python decoder was independently run against one
entire log and likewise matched its original hash. Its code, the C++ codec,
the compiler/executable provenance, all per-file ledgers and the independent
verification result are included. RESTORE_LARGE_LOGS.py restores the original
paths, including the two exactly reconstructed duplicate prefixes. All partial
records remain separate. Regenerated gzip wrappers may differ from the old
serialization, as already explicitly accounted for above.

The earlier unreleased compact candidates and the oversized original container
are superseded by this exact representation of the same18:55:35UTC frozen
snapshot. The392-page PDF and241-statement register remain unchanged. Only
recovery programs, audits and this accounting were added after the capture.
The failed candidates are not additional hourly research checkpoints.
'''

with zipfile.ZipFile(SOURCE) as old:
    mapping=json.loads(old.read('CHECKPOINT_COMPRESSION_MAP.json'))
    omitted=set();transforms=[]
    for prior in mapping['transforms']:
        row=binary[prior['original_path']]
        for k in ['original_sha256','original_bytes','decoded_sha256','decoded_bytes']:
            assert row[k]==prior[k],(prior['original_path'],k)
        assert row['entire_decoded_byte_hash_verified']
        assert digest(CACHE/row['stored_path'])==row['encoded_xz_sha256']
        omitted.add(prior['stored_path']);transforms.append(row)
    mapping['transforms']=transforms
    mapping['binary_conversion_manifest']='BINARY_CONVERSION_MANIFEST.json'
    mapping['portable_full_log_verification']='notes/checkpoint09_binary_portable_verification.json'
    for row in mapping['exact_prefix_reconstructions']:
        row['stored_source_path']=binary['code/'+row['retained_source_payload']]['stored_path']
        row['restoration_input']='Restore transforms first, then use the original decoded source path under the destination.'
    recovery=old.read('notes/checkpoint09_upload_recovery.md')+NOTE.encode()
    additions={
        'CHECKPOINT_COMPRESSION_MAP.json':(json.dumps(mapping,indent=2)+'\n').encode(),
        'BINARY_CONVERSION_MANIFEST.json':(json.dumps(conversion,indent=2)+'\n').encode(),
        'RESTORE_LARGE_LOGS.py':RESTORE.encode(),
        'notes/checkpoint09_upload_recovery.md':recovery,
        'LM8_PUSH_report.md':old.read('LM8_PUSH_report.md')+NOTE.encode(),
    }
    for name in ['code/pbc_trace_binary_codec.cpp','code/pbc_trace_binary_decode.py',
                 'code/pbc_binary_checkpoint09.py','code/pbc_binary_codec_provenance.json',
                 'code/verify_binary_checkpoint09.py','code/finish_binary_checkpoint09.py',
                 'notes/checkpoint09_binary_portable_verification.json',
                 'notes/checkpoint09_binary_portable_verification.out']:
        additions[name]=(ROOT/name).read_bytes()
    for e in transforms:
        additions[e['stored_path']+'.json']=(CACHE/(e['stored_path']+'.json')).read_bytes()
    entries=[]
    with zipfile.ZipFile(DEST,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        def add(name,data):
            z.writestr(name,data,compress_type=zipfile.ZIP_STORED if name.endswith('.xz') else zipfile.ZIP_DEFLATED)
            entries.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        for name in old.namelist():
            if name in omitted or name in additions or name=='PACKAGE_MANIFEST.json':continue
            add(name,old.read(name))
        for e in transforms:add(e['stored_path'],(CACHE/e['stored_path']).read_bytes())
        for name,data in additions.items():add(name,data)
        manifest={'created_utc':datetime.now(timezone.utc).isoformat(),
                  'kind':'checkpoint09 upload-limit recovery, exact binary proof serialization',
                  'original_snapshot_created_utc':'2026-11-15T18:55:35.266296+00:00',
                  'file_count':len(entries),'files':entries,
                  'compression_map':'CHECKPOINT_COMPRESSION_MAP.json'}
        z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(DEST) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(set(z.namelist()))
    original=json.loads(z.read('ORIGINAL_PACKAGE_MANIFEST.json'))
    originals={e['path']:e for e in original['files']}
    for name in ['LM8_PUSH_paper.pdf','LM8_PUSH_results.csv','LM8_PUSH_paper.tex','LM8_PUSH_references.bib']:
        assert hashlib.sha256(z.read(name)).hexdigest()==originals[name]['sha256']
result={'file':str(DEST),'bytes':DEST.stat().st_size,'sha256':digest(DEST),
        'files':len(entries),'below_upload_limit':DEST.stat().st_size<=536870912,
        'same_original_snapshot':True,'all_proof_payloads_exactly_reconstructable':True}
(OUT/'repack_result.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'notes/checkpoint09_upload_recovery.md').write_bytes(recovery)
(ROOT/'notes/checkpoint09_compression_map.json').write_text(json.dumps(mapping,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
assert result['below_upload_limit']
