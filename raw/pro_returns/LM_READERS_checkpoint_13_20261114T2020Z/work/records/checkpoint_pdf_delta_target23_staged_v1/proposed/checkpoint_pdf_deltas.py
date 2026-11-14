"""Optional explicit depth-one PDF storage plan; never a PDF rewrite.

This builder-only module uses Git to generate a COPY/LITERAL stream, then the
standalone standard-library decoder proves the original target bytes exactly.
Only up to twenty-three explicitly pinned retained book-PDF targets are considered.
All bases must already be retained full PDF objects and cannot be targets.
"""
from __future__ import annotations
import base64,hashlib,json,os,re,shutil,subprocess,tempfile,zlib
from pathlib import Path
import restore_checkpoint as recovery

PLAN_SCHEMA='lm-checkpoint-pdf-delta-plan-v1'

def digest(data):return hashlib.sha256(data).hexdigest()
def deflate_size(data):
 encoder=zlib.compressobj(6,zlib.DEFLATED,-15);return len(encoder.compress(data)+encoder.flush())

def parse_forward_delta(stdout):
 lines=stdout.splitlines()
 if lines.count(b'GIT binary patch')!=1:raise ValueError('Expected exactly one binary PDF comparison.')
 i=lines.index(b'GIT binary patch')+1
 header=re.fullmatch(rb'(delta|literal) ([0-9]+)',lines[i]) if i<len(lines) else None
 if not header or header[1]!=b'delta':raise ValueError('PDF comparison did not yield the bounded delta codec.')
 expected=int(header[2]);recovery.pdf_delta_uint(expected,'generated stream length');i+=1;chunks=[]
 while i<len(lines) and lines[i]:
  line=lines[i];i+=1
  n=line[0]-64 if 65<=line[0]<=90 else line[0]-70 if 97<=line[0]<=122 else -1
  if not 1<=n<=52 or len(line[1:])!=((n+3)//4)*5:raise ValueError('Invalid generated binary-patch line.')
  chunks.append(base64.b85decode(line[1:])[:n])
 packed=b''.join(chunks)
 if len(packed)>recovery.PDF_DELTA_MAX_BYTES:raise ValueError('Generated packed stream exceeds its limit.')
 decoder=zlib.decompressobj();delta=decoder.decompress(packed,recovery.PDF_DELTA_MAX_BYTES+1)
 if (not decoder.eof or decoder.unused_data or decoder.unconsumed_tail or len(delta)!=expected):
  raise ValueError('Generated PDF-delta stream is truncated, oversized or ambiguous.')
 return delta

def generate(base,target,git_executable):
 env=dict(os.environ,GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=os.devnull,GIT_CONFIG_SYSTEM=os.devnull,GIT_ATTR_NOSYSTEM='1',LC_ALL='C')
 with tempfile.TemporaryDirectory(prefix='lm-pdf-delta-generator-') as directory:
  path=Path(directory);left=path/'base.pdf';right=path/'target.pdf';left.write_bytes(base);right.write_bytes(target)
  result=subprocess.run([git_executable,'-c','core.attributesFile='+os.devnull,'diff','--no-index','--binary',
   '--no-ext-diff','--no-textconv','--no-color','--',str(left),str(right)],cwd=path,env=env,
   stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60)
  if result.returncode!=1:raise RuntimeError('Bounded PDF-delta generator did not return a binary comparison.')
  return parse_forward_delta(result.stdout)

def book_authorities(entries,inherited=None):
 """Derive only exact current-book or already-validated inherited book pins."""
 inherited=inherited or {};rows=[]
 for reader in sorted(recovery.BOOKS):
  name='work/build/'+reader+'.pdf';entry=entries.get(name)
  if entry:rows.append(dict(reader=reader,path=name,logical_path_at_capture=name,bytes=entry['bytes'],sha256=entry['sha256']))
 rows += [row for row in inherited.get('recovery_inputs',[]) if row.get('kind')=='source_pdf']
 rows += [dict(row,reader=row.get('publication_reader')) for row in inherited.get('native_recovery_inputs',[])
          if row.get('kind')=='native_source_pdf' and row.get('publication_reader')
          and row.get('logical_path_at_capture')=='work/build/'+row['publication_reader']+'.pdf']
 found=[]
 for row in rows:
  reader=row.get('reader');name=row.get('path');entry=entries.get(name)
  if (reader not in recovery.BOOKS or not entry or entry['sha256']!=row.get('sha256') or
      entry['bytes']!=row.get('bytes') or row.get('logical_path_at_capture')!='work/build/'+reader+'.pdf'):
   raise ValueError('A named-book authority differs from its exact collected PDF input.')
  found.append(dict(reader=reader,logical_path=name,bytes=entry['bytes'],sha256=entry['sha256']))
 return found


def qualify(items,entries,groups,read_payload,plan,source_checkpoint,authorities):
 """Qualify an already-collected exact plan; return recipes, streams, report."""
 if (not isinstance(plan,dict) or set(plan)!={'schema','maximum_depth','source_checkpoint','targets'} or
     plan['schema']!=PLAN_SCHEMA or type(plan['maximum_depth']) is not int or plan['maximum_depth']!=1 or
     not isinstance(plan['targets'],list) or not 1<=len(plan['targets'])<=recovery.PDF_DELTA_MAX_TARGETS):
  raise ValueError('Unsupported explicit PDF-delta storage plan.')
 path=Path(source_checkpoint);source=plan['source_checkpoint']
 if (set(source)!={'filename','bytes','sha256'} or source['filename']!=path.name or type(source['bytes']) is not int or
     path.stat().st_size!=source['bytes'] or digest(path.read_bytes())!=source['sha256']):
  raise ValueError('PDF-delta plan does not pin the exact prior checkpoint.')
 exe=shutil.which('git')
 if not exe:raise RuntimeError('The optional PDF-delta builder requires Git; recovery never does.')
 generator=subprocess.check_output([exe,'--version'],text=True).strip()
 rows=plan['targets'];target_hashes=set();base_hashes=set();cache={};recipes={};streams={};evidence=[]
 authorized={(row['reader'],row['sha256'],row['bytes']) for row in authorities}
 def data(pin):
  if not isinstance(pin,dict) or set(pin)!={'sha256','bytes','reader'}:raise ValueError('Unsupported planned PDF pin.')
  h=recovery.pdf_delta_sha(pin['sha256']);recovery.pdf_delta_uint(pin['bytes'],'planned PDF length')
  if (pin['reader'],h,pin['bytes']) not in authorized:
   raise ValueError('Planned PDF has no exact current or retained named-book authority.')
  names=groups.get(h,[])
  if not names or pin['reader'] not in recovery.BOOKS or any(Path(n).suffix.lower()!='.pdf' for n in names):
   raise ValueError('Planned PDF is absent or has a non-PDF logical alias.')
  for n in names:
   if entries[n]['sha256']!=h or entries[n]['bytes']!=pin['bytes']:raise ValueError('Planned PDF logical byte pin differs.')
  if h not in cache:
   src=items[names[0]][0];content=src if isinstance(src,bytes) else read_payload(src)
   if len(content)!=pin['bytes'] or digest(content)!=h or not content.startswith(b'%PDF-'):
    raise ValueError('Planned PDF differs from original exact collected bytes.')
   cache[h]=content
  return cache[h]
 for row in rows:
  if not isinstance(row,dict) or set(row)!={'base','target'}:raise ValueError('Unsupported planned target fields.')
  base=data(row['base']);target=data(row['target']);bh=digest(base);h=digest(target)
  expected={'LM_FR_master_annotated':'LM_FR_corrige_apparat','LM_EN_master_annotated':'LM_EN_corrected_apparatus'}.get(row['target']['reader'],row['target']['reader'])
  if row['base']['reader']!=expected or h in target_hashes or bh==h:raise ValueError('Planned target duplicates or leaves the bounded named-book profile.')
  target_hashes.add(h);base_hashes.add(bh)
 if target_hashes&base_hashes:raise ValueError('Planned PDF chains or cycles are forbidden.')
 for row in rows:
  base=data(row['base']);target=data(row['target']);h=digest(target);delta=generate(base,target,exe)
  if recovery.apply_pdf_delta(base,delta,len(target))!=target:raise ValueError('Fresh PDF-delta exact-byte proof failed.')
  full_size=deflate_size(target);delta_size=deflate_size(delta)
  if delta_size>=full_size:raise ValueError('Explicit PDF-delta target does not save compressed payload bytes.')
  dh=digest(delta);r=dict(id='pdf-delta-'+h,kind=recovery.PDF_DELTA_KIND,base_sha256=digest(base),base_bytes=len(base),
   base_object_path='objects/sha256/'+digest(base),base_reader=row['base']['reader'],base_logical_path_at_capture='work/build/'+row['base']['reader']+'.pdf',
   target_sha256=h,target_bytes=len(target),target_object_path='objects/sha256/'+h,target_reader=row['target']['reader'],
   logical_path_at_capture='work/build/'+row['target']['reader']+'.pdf',delta=dict(object_path='objects/pdf-delta-sha256/'+dh,bytes=len(delta),sha256=dh))
  recipes[h]=r;streams[r['delta']['object_path']]=delta
  evidence.append(dict(target_sha256=h,base_sha256=digest(base),delta_sha256=dh,base_bytes=len(base),target_bytes=len(target),delta_bytes=len(delta),
   exact_target_bytes_and_sha256_verified=True,full_pdf_deflate6_bytes=full_size,delta_deflate6_bytes=delta_size))
 report=dict(schema='lm-checkpoint-pdf-delta-fresh-proof-v1',generator=generator,target_count=len(recipes),primitive_base_count=len(base_hashes),
  maximum_depth=1,all_bases_already_retained=True,additional_base_payload_bytes=0,exact_target_bytes_and_sha256_verified=True,
  full_pdf_deflate6_bytes=sum(r['full_pdf_deflate6_bytes'] for r in evidence),delta_deflate6_bytes=sum(r['delta_deflate6_bytes'] for r in evidence),
  savings_before_descriptor_manifest_helper_growth=sum(r['full_pdf_deflate6_bytes']-r['delta_deflate6_bytes'] for r in evidence),targets=evidence,
  generator_required_for_recovery=False,pdf_logical_bytes_modified=False,new_visual_review_claims=False)
 return recipes,streams,report
