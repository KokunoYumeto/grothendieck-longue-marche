#!/usr/bin/env python3
"""Capture a full hourly checkpoint using explicitly verified reversible storage.

Usage: python code/package_compact_checkpoint.py NN STORAGE_PLAN.json
The plan supplies exact original hashes, encoded files and restoration commands.
Every ordinary file is retained; byte-identical large files may share one copy.
Existing archives are never overwritten.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,zipfile

ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('serial',type=int);ap.add_argument('plan',type=Path)
ap.add_argument('--final',action='store_true',help='Capture the final return with verified complete history instead of an hourly checkpoint')
args=ap.parse_args()
serial=f'{args.serial:02d}';DEST=ROOT.parent/('LM8_PUSH.zip' if args.final else f'LM8_PUSH_checkpoint_{serial}.zip')
if DEST.exists():raise SystemExit('Refusing to overwrite '+str(DEST))
plan=json.loads(args.plan.read_text())
history_path=ROOT/'checkpoint_history/HISTORY_INDEX.json'
if args.final:
 assert history_path.exists(),'Final assembly requires materialized checkpoint history'
 history=json.loads(history_path.read_text())
 catalog=json.loads((ROOT/'notes/checkpoint_saved_paths.json').read_text())
 assert history['status']=='MATERIALIZED_VERIFIED_HISTORY'
 assert history['through_checkpoint']>=max(map(int,catalog)),'History omits a saved checkpoint'
transforms={e['original_path']:e for e in plan['transforms']}
prefixes={e['original_path']:e for e in plan.get('exact_prefix_reconstructions',[])}
wrappers={e['original_path']:e for e in plan.get('superseded_compression_wrappers',[])}
excluded=('build/tex-cache/','__pycache__/','background/','inputs/')
regenerated_metadata={
 'PACKAGE_MANIFEST.json','CHECKPOINT_COMPRESSION_MAP.json',
 'ORIGINAL_PACKAGE_MANIFEST.json','RESTORE_LARGE_LOGS.py'}
omitted={
 'notes/de_compile/de_compile_check.pdf':'Isolated bibliography-free compile test; superseded by the integrated paper PDF; source/logs retained.',
 'notes/de_compile/de_prosolvable_compile.pdf':'Isolated local-proof compile test; superseded by the integrated paper PDF; source/logs retained.',
 'notes/de_compile/de_compile_D62_D63.pdf':'Isolated layout test; superseded by the integrated paper PDF; source/logs retained.',
 'notes/de_compile/de_compile_D64.pdf':'Isolated layout test; superseded by the integrated paper PDF; source/logs retained.',
 'notes/de_compile/de_compile_D60.pdf':'Isolated layout test; superseded by the integrated paper PDF; source/logs retained.',
 'notes/de_compile/de_compile_D61.pdf':'Isolated layout test; superseded by the integrated paper PDF; source/logs retained.',
 'notes/de_compile/de_compile_D65.pdf':'Isolated layout test reviewed at checkpoint08; superseded by the integrated paper PDF; source/logs and earlier checkpoint copy retained.'}
omitted.update({name:'Generated root packaging metadata is regenerated for this capture; historical versions are retained by the checkpoint-history inventory. A present resumed-root copy is accounted by its old byte hash separately and is never an exact-copy source.' for name in regenerated_metadata})

def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

RESTORE='''#!/usr/bin/env python3
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
'''

captured=datetime.now(timezone.utc).isoformat()
original_entries=[];ordinary=[];aliases=[];by_hash={};replaced_root_metadata=[]
# Operational current files must precede history objects. In particular a
# source PDF needed by a PNG transform must not become an alias to a history
# object that is only restored after the transforms.
def capture_order(p):
 rel=p.relative_to(ROOT).as_posix()
 return (rel.startswith('checkpoint_history/'),rel)
for p in sorted(ROOT.rglob('*'),key=capture_order):
 if not p.is_file():continue
 rel=p.relative_to(ROOT).as_posix()
 if any(rel.startswith(x) or ('/'+x) in rel for x in excluded) or p.suffix=='.pyc':continue
 # After extraction these four paths contain the preceding archive's metadata.
 # Never canonicalize a historical object to bytes the writer will replace.
 if rel in regenerated_metadata:
  replaced_root_metadata.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p),
                                 'reason':omitted[rel]})
  continue
 if rel in omitted:continue
 if rel in transforms or rel in prefixes or rel in wrappers:
  row=transforms.get(rel) or prefixes.get(rel) or wrappers[rel]
  expected=row.get('original_sha256',row.get('original_valid_gzip_sha256'))
  actual=sha(p)
  assert expected and actual==expected,('Changed encoded source',rel,actual,expected)
  size=p.stat().st_size
  if 'original_bytes' in row:assert size==row['original_bytes']
  original_entries.append({'path':rel,'bytes':size,'sha256':actual})
  continue
 data=p.read_bytes();digest=hashlib.sha256(data).hexdigest()
 original_entries.append({'path':rel,'bytes':len(data),'sha256':digest})
 if (len(data)>=1_000_000 or rel.startswith('checkpoint_history/objects/')) and digest in by_hash:
  aliases.append({'original_path':rel,'source_path':by_hash[digest],
                  'bytes':len(data),'sha256':digest});continue
 if digest not in by_hash:by_hash[digest]=rel
 ordinary.append((rel,data))

expected=set(transforms)|set(prefixes)|set(wrappers)
assert expected<={e['path'] for e in original_entries},'Storage plan names missing original files'
payloads={}
clean=[]
for row in transforms.values():
 item={k:v for k,v in row.items() if k not in {'local_encoded_file','additional_payloads'}}
 assert row.get('entire_decoded_byte_hash_verified'),row['original_path']
 path=Path(row['local_encoded_file'])
 expected_hash=row.get('encoded_xz_sha256',row.get('stored_sha256'))
 assert expected_hash and sha(path)==expected_hash
 payloads[row['stored_path']]=path;clean.append(item)
 for extra in row.get('additional_payloads',[]):
  p=Path(extra['local_file'])
  if extra.get('sha256'):assert sha(p)==extra['sha256']
  payloads[extra['path']]=p
for extra in plan.get('additional_payloads',[]):
 p=Path(extra['local_file'])
 if extra.get('sha256'):assert sha(p)==extra['sha256']
 payloads[extra['path']]=p
assert not (set(payloads)&regenerated_metadata),'Stored payload collides with regenerated root metadata'
# Encoded payloads can live outside ROOT until capture. Deduplicate historical
# objects against those exact stored bytes too, without aliasing operational
# current inputs. All resulting copy sources are literal archive entries.
payload_by_hash={sha(p):name for name,p in payloads.items()}
kept=[]
for name,data in ordinary:
 digest=hashlib.sha256(data).hexdigest()
 if name in payloads:
  assert digest==sha(payloads[name]),('Stored payload replaces different literal bytes',name)
 if name.startswith('checkpoint_history/objects/') and digest in payload_by_hash:
  aliases.append({'original_path':name,'source_path':payload_by_hash[digest],
                  'bytes':len(data),'sha256':digest})
 else:kept.append((name,data))
ordinary=kept
alias_sources={e['original_path']:e['source_path'] for e in aliases}
for e in aliases:
 seen={e['original_path']}
 while e['source_path'] in alias_sources:
  assert e['source_path'] not in seen,'Exact-copy cycle'
  seen.add(e['source_path']);e['source_path']=alias_sources[e['source_path']]
literal_names={name for name,_ in ordinary}|set(payloads)
assert not (literal_names&regenerated_metadata),'Stale root metadata entered literal copy sources'
assert all(e['source_path'] in literal_names for e in aliases),'Nonliteral exact-copy source'
# History references to transformed raw files are deliberately immutable.
# Validate them on every capture, before writing a new archive.
if history_path.exists():
 history=json.loads(history_path.read_text())
 for name,e in history['exact_current_restoration_dependencies'].items():
  source=ROOT/name
  assert source.stat().st_size==e['bytes'] and sha(source)==e['sha256'],('Changed historical exact dependency',name)
mapping={k:v for k,v in plan.items() if k not in {'transforms','additional_payloads'}}
mapping.update({'checkpoint':serial,'captured_utc':captured,'transforms':clean,'exact_file_copies':aliases,
                'all_complete_and_partial_proof_records_retained':True})
original_manifest={'created_utc':captured,'kind':'full hourly checkpoint before reversible serialization',
                   'file_count':len(original_entries),'files':original_entries,
                   'omitted_intermediates':omitted,
                   'replaced_root_packaging_metadata':replaced_root_metadata,
                   'exclusions':['User-attached background, extracted supplied sources and reproducible downloaded-source caches',
                                 'Reproducible TeX/font cache; scripts and hashes retained']}
metadata={
 'CHECKPOINT_COMPRESSION_MAP.json':(json.dumps(mapping,indent=2)+'\n').encode(),
 'ORIGINAL_PACKAGE_MANIFEST.json':(json.dumps(original_manifest,indent=2)+'\n').encode(),
 'RESTORE_LARGE_LOGS.py':RESTORE.encode()}
entries=[]
with zipfile.ZipFile(DEST,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 def add(name,data):
  z.writestr(name,data,compress_type=zipfile.ZIP_STORED if name.endswith(('.xz','.gz')) else zipfile.ZIP_DEFLATED)
  entries.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
 for name,data in ordinary:
  if name not in metadata and name not in payloads and name!='PACKAGE_MANIFEST.json':add(name,data)
 for name,p in payloads.items():add(name,p.read_bytes())
 for name,data in metadata.items():add(name,data)
 manifest={'created_utc':captured,'kind':'final' if args.final else 'checkpoint','file_count':len(entries),'files':entries,
           'original_file_count':len(original_entries),'original_manifest':'ORIGINAL_PACKAGE_MANIFEST.json',
           'compression_map':'CHECKPOINT_COMPRESSION_MAP.json'}
 z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(DEST) as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(set(z.namelist()))
result={'file':str(DEST),'bytes':DEST.stat().st_size,'sha256':sha(DEST),'files':len(entries),
        'original_files':len(original_entries),'exact_duplicate_copies':len(aliases),
        'below_upload_limit':DEST.stat().st_size<=536870912,'captured_utc':captured}
(ROOT/('notes/final_package_result.json' if args.final else f'notes/checkpoint{serial}_package_result.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
assert result['below_upload_limit'],'Full checkpoint exceeds upload limit; retain unchanged and recover explicitly.'
