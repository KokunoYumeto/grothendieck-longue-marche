#!/usr/bin/env python3
"""Restore original paths from verified reversible checkpoint storage."""
from pathlib import Path
import argparse,gzip,hashlib,json,lzma,shutil,subprocess,sys
ap=argparse.ArgumentParser();ap.add_argument('--destination',type=Path);a=ap.parse_args()
base=Path(__file__).resolve().parent;dest=(a.destination or base).resolve()
mapping=json.loads((base/'CHECKPOINT_COMPRESSION_MAP.json').read_text())
for e in mapping['transforms']:
 target=dest/e['original_path'];target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists():
  print('EXISTS, unchanged:',target);continue
 if e.get('restore_command'):
  values={'python':sys.executable,'archive':str(base),'destination':str(dest),'target':str(target)}
  subprocess.run([part.format(**values) for part in e['restore_command']],check=True)
 elif e.get('codec')=='PBCBIN01':
  subprocess.run([sys.executable,str(base/'code/pbc_trace_binary_decode.py'),
                  str(base/e['stored_path']),str(target),'--sha256',e['decoded_sha256']],check=True)
 else:
  h=hashlib.sha256();count=0
  with lzma.open(base/e['stored_path'],'rb') as inp,target.open('xb') as raw:
   out=gzip.GzipFile(filename='',mode='wb',fileobj=raw,compresslevel=1,mtime=0) if e['kind']=='gzip_payload' else raw
   for b in iter(lambda:inp.read(1024*1024),b''):
    h.update(b);count+=len(b);out.write(b)
   if out is not raw:out.close()
  assert h.hexdigest()==e['decoded_sha256'] and count==e['decoded_bytes']
 reader=gzip.open(target,'rb') if e['kind']=='gzip_payload' else target.open('rb')
 h=hashlib.sha256();count=0
 with reader:
  for b in iter(lambda:reader.read(1024*1024),b''):h.update(b);count+=len(b)
 assert h.hexdigest()==e['decoded_sha256'] and count==e['decoded_bytes']
 print('RESTORED verified original payload:',target)
for e in mapping.get('exact_prefix_reconstructions',[]):
 target=dest/e['original_path']
 if target.exists():
  print('EXISTS, unchanged:',target);continue
 target.parent.mkdir(parents=True,exist_ok=True)
 if e.get('restore_command'):
  values={'python':sys.executable,'archive':str(base),'destination':str(dest),'target':str(target)}
  subprocess.run([part.format(**values) for part in e['restore_command']],check=True)
 else:
  subprocess.run([sys.executable,str(base/'code/pbc_trace_reconstruction.py'),
                  str(base/'code/pbc_compact_trace_reconstruction.json'),e['kind'],
                  str(dest/'code'/e['retained_source_payload']),str(target)],check=True)
 if e.get('decoded_sha256'):
  reader=target.open('rb') if e.get('payload_encoding')=='raw' else gzip.open(target,'rb')
  h=hashlib.sha256();count=0
  with reader:
   for b in iter(lambda:reader.read(1024*1024),b''):h.update(b);count+=len(b)
  assert h.hexdigest()==e['decoded_sha256'] and count==e['decoded_bytes']
for e in mapping.get('exact_file_copies',[]):
 target=dest/e['original_path'];source=dest/e['source_path']
 if not source.exists():source=base/e['source_path']
 if target.exists():
  print('EXISTS, unchanged:',target);continue
 target.parent.mkdir(parents=True,exist_ok=True)
 with source.open('rb') as src,target.open('xb') as out:shutil.copyfileobj(src,out)
 assert hashlib.sha256(target.read_bytes()).hexdigest()==e['sha256']
 print('RESTORED exact duplicate:',target)
print('Partial proof records are already retained separately. Superseded compression wrappers are explicitly documented; all original mathematical record bytes are retained or exactly reconstructable.')
