"""Temporary reduced-scope archive fixtures, never a production checkpoint."""
from pathlib import Path
import collections,copy,csv,hashlib,io,json,zipfile
import restore_checkpoint as recovery

ROLE='temporary storage prototype; no publication or visual-review approval'
FIELDS=['path','bytes','sha256','role']
DFIELDS=['source_archive','source_namespace','source_path','source_bytes','source_sha256','disposition','target_namespace','target_path','target_bytes','target_sha256','reason']

def enc(value):return (json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
def sha(data):return hashlib.sha256(data).hexdigest()
def tsv(rows,fields):
 out=io.StringIO();writer=csv.DictWriter(out,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows);return out.getvalue().encode()
def pin(name,data):return dict(logical_path=name,bytes=len(data),sha256=sha(data))
def varint(n):
 out=bytearray()
 while n>=128:out.append((n&127)|128);n>>=7
 out.append(n);return bytes(out)
def literal_delta(base,target):return varint(len(base))+varint(len(target))+b''.join(bytes([len(target[i:i+127])])+target[i:i+127] for i in range(0,len(target),127))
def delta_recipe(base,target,delta,reader,base_reader=None):
 base_reader=base_reader or reader;h=sha(target);bh=sha(base);dh=sha(delta)
 return dict(id='pdf-delta-'+h,kind=recovery.PDF_DELTA_KIND,base_sha256=bh,base_bytes=len(base),
  base_object_path='objects/sha256/'+bh,base_reader=base_reader,base_logical_path_at_capture='work/build/'+base_reader+'.pdf',
  target_sha256=h,target_bytes=len(target),target_object_path='objects/sha256/'+h,target_reader=reader,
  logical_path_at_capture='work/build/'+reader+'.pdf',delta=dict(object_path='objects/pdf-delta-sha256/'+dh,bytes=len(delta),sha256=dh))
def rehash(data):
 descriptor=json.loads(data[recovery.DESCRIPTOR])
 for key,name in [('logical_manifest',recovery.LOGICAL),('alias_inventory',recovery.ALIASES),('png_recipes',recovery.RECIPES),('source_checkpoint_dispositions',recovery.SOURCE_DISPOSITIONS),('recovery_helper',recovery.HELPER)]:
  descriptor[key].update(bytes=len(data[name]),sha256=sha(data[name]))
 data[recovery.DESCRIPTOR]=enc(descriptor)
 data[recovery.PHYSICAL]=tsv([dict(path=n,bytes=len(b),sha256=sha(b),role=ROLE) for n,b in sorted(data.items()) if n!=recovery.PHYSICAL],FIELDS)
 return data

def write_zip(path,data):
 path=Path(path)
 with zipfile.ZipFile(path,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for name,b in sorted(data.items()):z.writestr(name,b)
 return path

def make_archive(path,payloads,*,png_recipes=None,delta_records=None,delta_streams=None,recovery_inputs=None,native_inputs=None,inherited=None):
 payloads=dict(payloads);png_recipes=copy.deepcopy(png_recipes or {});delta_records=copy.deepcopy(delta_records or [])
 helper=Path(recovery.__file__).read_bytes();payloads['work/scripts/restore_checkpoint.py']=helper
 groups=collections.defaultdict(list)
 for n,b in payloads.items():recovery.safe_name(n);groups[sha(b)].append(n)
 deltas={r['target_sha256']:r for r in delta_records};logical=[];aliases=[];physical={}
 for h,names in sorted(groups.items()):
  canonical='work/scripts/restore_checkpoint.py' if h==sha(helper) else min(names)
  for n in sorted(names):
   row=dict(path=n,bytes=len(payloads[n]),sha256=h,role=ROLE,storage_kind='',object_path='',target_path='',recipe_id='')
   if n!=canonical:
    row.update(storage_kind='alias',target_path=canonical);aliases.append(dict(alias_path=n,target_path=canonical,bytes=row['bytes'],sha256=h))
   elif h in deltas:row.update(storage_kind='pdf_delta',object_path=deltas[h]['target_object_path'],recipe_id=deltas[h]['id'])
   elif h in png_recipes:row.update(storage_kind='png_recipe',recipe_id=png_recipes[h]['id'])
   else:
    obj=recovery.HELPER if h==sha(helper) else 'objects/sha256/'+h
    row.update(storage_kind='blob',object_path=obj);physical[obj]=payloads[n]
   logical.append(row)
 by_name={r['path']:r for r in logical}
 import native_checkpoint_recipes as native
 for r in png_recipes.values():native.bind_object_pins(r,by_name)
 for r in delta_records:
  content=delta_streams[r['delta']['sha256']]
  if len(content)!=r['delta']['bytes'] or sha(content)!=r['delta']['sha256']:raise ValueError('Fixture delta stream mismatch')
  physical[r['delta']['object_path']]=content
 logical_data=tsv(sorted(logical,key=lambda r:r['path']),recovery.LOGICAL_FIELDS)
 alias_data=tsv(aliases,['alias_path','target_path','bytes','sha256'])
 recipe_data=enc(dict(schema='lm-checkpoint-png-recipes-v3',recipes=list(png_recipes.values()),rendering_is_not_visual_inspection=True))
 dispositions=[]
 if inherited:
  for old in inherited['prior_inventory']:
   name=old['path'];h=old['sha256']
   if old.get('exact_target_path'):target=by_name[old['exact_target_path']];state='PRESERVED_EXACT_AT_OTHER_PATH'
   elif name in by_name:target=by_name[name];state='PRESERVED_EXACT' if target['sha256']==h else 'SUPERSEDED_CURRENT_LOGICAL_PATH'
   elif h in groups:target=by_name[min(groups[h])];state='PRESERVED_EXACT_AT_OTHER_PATH'
   else:raise ValueError('Fixture lost a prior path: '+name)
   dispositions.append(dict(source_archive=inherited['origin']['filename'],source_namespace=old['namespace'],source_path=name,source_bytes=old['bytes'],source_sha256=h,disposition=state,target_namespace='logical',target_path=target['path'],target_bytes=target['bytes'],target_sha256=target['sha256'],reason='Exact bounded synthetic lineage control.'))
 disp_data=tsv(dispositions,DFIELDS)
 def ref(n,b,**extra):return dict(path=n,bytes=len(b),sha256=sha(b),**extra)
 descriptor=dict(schema=recovery.SCHEMA,checkpoint_kind='TEMPORARY_REDUCED_SCOPE_STORAGE_PROTOTYPE_NOT_CHECKPOINT',
  logical_manifest=ref(recovery.LOGICAL,logical_data,count=len(logical)),alias_inventory=ref(recovery.ALIASES,alias_data,count=len(aliases)),
  png_recipes=ref(recovery.RECIPES,recipe_data,count=len(png_recipes)),source_checkpoint_dispositions=ref(recovery.SOURCE_DISPOSITIONS,disp_data,count=len(dispositions)),
  source_checkpoint=dict(filename='synthetic_origin_not_checkpoint.zip',bytes=0,sha256=sha(b''),entries=0),
  source_pdfs=[dict(reader=book,**pin('work/build/'+book+'.pdf',payloads['work/build/'+book+'.pdf'])) for book in sorted(recovery.BOOKS)],
  recovery_helper=ref(recovery.HELPER,helper),inherited_recovery_inputs=recovery_inputs or [],native_recovery_inputs=native_inputs or [],
  new_visual_review_claims=False,source_checkpoint_required_for_recovery=False)
 if delta_records:descriptor['pdf_delta_recovery']=dict(schema=recovery.PDF_DELTA_SCHEMA,codec=recovery.PDF_DELTA_KIND,maximum_depth=1,generator_required_for_recovery=False,new_visual_review_claims=False,recipes=delta_records)
 if inherited:
  descriptor['source_checkpoint']=dict(filename=inherited['origin']['filename'],bytes=inherited['origin']['bytes'],sha256=inherited['origin']['sha256'],entries=len(dispositions),inventory_kind='compact logical payloads and exact control metadata',logical_manifest_sha256=inherited['origin']['logical_manifest_sha256'],logical_entries=sum(r['namespace']=='logical' for r in inherited['prior_inventory']),container_entries=sum(r['namespace']=='container' for r in inherited['prior_inventory']))
  descriptor['preserved_prior_controls']=inherited['preserved_control_metadata']
 physical.update({recovery.DESCRIPTOR:enc(descriptor),recovery.LOGICAL:logical_data,recovery.ALIASES:alias_data,recovery.RECIPES:recipe_data,recovery.SOURCE_DISPOSITIONS:disp_data,recovery.README:b'Temporary reduced-scope storage prototype. No publication or visual-review claim.\n'})
 rehash(physical);write_zip(path,physical)
 return payloads,physical

def rewrite(source,target,mutate):
 with zipfile.ZipFile(source) as z:data={n:z.read(n) for n in z.namelist()}
 mutate(data);rehash(data);return write_zip(target,data)
