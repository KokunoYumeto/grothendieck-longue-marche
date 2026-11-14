"""Bounded expand-cache equivalence controls; no production archive or review."""
from __future__ import annotations
import argparse, ast, collections, copy, hashlib, importlib.util, json, sys, types
from pathlib import Path

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--project-root',required=True)
args=parser.parse_args()
ROOT=Path(args.project_root).resolve(); STAGE=Path(__file__).resolve().parent
if STAGE.is_relative_to(ROOT): raise ValueError('The preparation stage must remain external.')
sys.path[:0]=[str(ROOT/'work/scripts'),str(STAGE)]
import restore_checkpoint as recovery
import prototype_support as support

sha=lambda data:hashlib.sha256(data).hexdigest()
enc=lambda value:(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
def ref(path):
    data=path.read_bytes()
    return dict(path=str(path.relative_to(STAGE)),bytes=len(data),sha256=sha(data))
def load(label):
    path=STAGE/label/'checkpoint_inheritance.py'
    spec=importlib.util.spec_from_file_location('expand_'+label,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

before=load('before'); after=load('proposed'); checks=[]
active_paths=[ROOT/'work/scripts'/n for n in ('checkpoint_inheritance.py','restore_checkpoint.py','native_checkpoint_recipes.py','package_release.py')]
active_pins={str(p.relative_to(ROOT)):dict(bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in active_paths}
def passed(name,**extra):
    checks.append(dict(test=name,status='PASS',**extra));print(name,flush=True)

source_before=(STAGE/'before/checkpoint_inheritance.py').read_text()
source_after=(STAGE/'proposed/checkpoint_inheritance.py').read_text()
ta=ast.parse(source_before);tb=ast.parse(source_after)
assert len(ta.body)==len(tb.body)
for a,b in zip(ta.body,tb.body):
    if isinstance(a,ast.FunctionDef) and a.name=='expand':continue
    assert ast.dump(a,include_attributes=False)==ast.dump(b,include_attributes=False)
def nested(tree,name):
    return next(n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name==name)
for name in ('data','add'):
    assert ast.dump(nested(ta,name),include_attributes=False)==ast.dump(nested(tb,name),include_attributes=False)
for call in ('prior.recipe_bytes(recipe, native_documents)','prior.recipe_bytes(dependency, native_documents)'):
    assert source_before.count(call)==source_after.count(call)==1
assert "return (prior.archive_sha256, pin['object_path'], pin['sha256'], pin['bytes'])" in source_after
passed('Only expand changes; general data/add, both primitive calls and four-part immutable key are preserved')

def read_fixture(path):
    prior=recovery.CompactArchive(path)
    try:
        result={}
        docs={}
        try:
            for name,row in prior.logical.items():
                canonical=prior.logical[row['target_path']] if row['storage_kind']=='alias' else row
                result[name]=(prior.recipe_bytes(prior.recipes[canonical['recipe_id']],docs)
                              if canonical['storage_kind']=='png_recipe' else prior.logical_bytes(name))
        finally:
            for doc in docs.values():doc.close()
        return result,copy.deepcopy(prior.recipes),copy.deepcopy(prior.descriptor)
    finally:prior.close()

first=STAGE/'fixtures/legacy_synthetic_delta.zip'
third=STAGE/'fixtures/legacy_synthetic_generation3.zip'
assert sha(first.read_bytes())=='82b1ab82026912dab607cfa39cd8c0b2f6285d0f999531cff8afad9ef008e869'
assert sha(third.read_bytes())=='de94dd32e95ce33a451b28c58f1f8fa34c2f6c73fae73c9e0fad3fd76a0cdb55'
payloads,recipes,descriptor=read_fixture(first)
third_payloads,_,_=read_fixture(third)
passed('Existing 72KB and 119KB synthetic delta fixtures retain exact previously recorded hashes',fixtures=[ref(first),ref(third)])

# Extend only the existing small synthetic fixture with exact inline full-page
# primitives, one shared trace, ledger/PDF/metadata aliases and a prior native
# panel path. No production PDF or original archived payload is changed.
full=next(r for r in recipes.values() if r['kind']==recovery.FULL_PAGE_KIND)
source=copy.deepcopy(full['source_pdf']);book=Path(source['logical_path']).stem
trace_path='work/verification/'+book+'.verification.json'
trace_alias='work/data/synthetic_trace_alias.json'
trace_data=enc({'sha256':source['sha256'],'fixture':'bounded cache control; no review claim'})
payloads[trace_path]=payloads[trace_alias]=trace_data
ledger=full['qualification']['ledger_logical_path'];ledger_alias='work/data/synthetic_ledger_alias.tsv'
rows=[copy.deepcopy(full['qualification']['reviewed_row'])]
new_full={full['physical_page']:copy.deepcopy(full)}
prior=recovery.CompactArchive(first)
docs={}
try:
    for overview in recipes.values():
        if overview['kind']!=recovery.OVERVIEW_KIND:continue
        for panel in overview['panels']:
            primitive=panel.get('source_render')
            if not primitive or primitive['physical_page'] not in (1,2,3,4) or primitive['physical_page'] in new_full:continue
            image=recovery.recover_recipe(primitive,prior.object_bytes,None,docs)
            q=copy.deepcopy(primitive);q['kind']=recovery.FULL_PAGE_KIND;q['render']['target_width_px']=900
            image_path='work/verification/'+book+'/page_'+str(q['physical_page']).zfill(4)+'.png'
            payloads[image_path]=image
            row={k:str(v) for k,v in dict(page=q['physical_page'],status='reviewed',reviewer='synthetic control only',observations='Synthetic fixture; no publication review claim.',pdf_sha256=q['source_pdf']['sha256'],png_sha256=q['expected']['png_sha256'],rendered_pixel_sha256=q['expected']['dimensioned_rgb_sha256'],image_width=q['expected']['width'],image_height=q['expected']['height'],full_page_image=Path(image_path).name).items()}
            rows.append(row);q['qualification']=dict(ledger_logical_path=ledger,reviewed_row=row,new_visual_review_claims=False)
            new_full[q['physical_page']]=q
finally:
    for doc in docs.values():doc.close()
    prior.close()
assert len(new_full)==4
ledger_data=support.tsv(rows,list(rows[0]));payloads[ledger]=payloads[ledger_alias]=ledger_data
for page,q in new_full.items():
    q['qualification']['ledger_logical_path']=ledger if page%2 else ledger_alias
    q['qualification']['ledger_sha256']=sha(ledger_data)
    q['source_scan_trace']=dict(logical_path=trace_path if page%2 else trace_alias,bytes=len(trace_data),sha256=sha(trace_data),pdf_sha256=source['sha256'])
pdf_alias='work/data/synthetic_primary_alias.pdf';payloads[pdf_alias]=payloads[source['logical_path']]
meta_path='work/layout_probes/synthetic/metadata.json';meta_alias='work/data/synthetic_metadata_alias.json';payloads[meta_alias]=payloads[meta_path]
native_rows=[r for r in recipes.values() if r['kind']==recovery.NATIVE_KIND]
native_rows[-1]['source_pdf']['logical_path']=pdf_alias
native_rows[-1]['qualification']['metadata']['logical_path']=meta_alias
primitive=native_rows[0];primitive_h=primitive['expected']['png_sha256']
primitive_payload=next(b for b in payloads.values() if sha(b)==primitive_h)
primitive_path='work/data/checkpoint_recovery_inputs/native_panels/'+primitive_h+'.png';payloads[primitive_path]=primitive_payload
native_inputs=copy.deepcopy(descriptor['native_recovery_inputs'])
native_inputs.append(dict(path=primitive_path,bytes=len(primitive_payload),sha256=primitive_h,kind='native_source_png'))
extended_recipes={q['expected']['png_sha256']:q for _,q in sorted(new_full.items())}
extended_recipes.update({r['expected']['png_sha256']:r for r in recipes.values() if r['kind']!=recovery.FULL_PAGE_KIND})
prior=recovery.CompactArchive(first)
try:
    deltas=copy.deepcopy(list(prior.pdf_deltas.values()));streams={r['delta']['sha256']:prior.zip.read(r['delta']['object_path']) for r in deltas}
finally:prior.close()
augmented=STAGE/'fixtures/augmented_repeated_inputs.zip'
support.make_archive(augmented,payloads,png_recipes=extended_recipes,delta_records=deltas,delta_streams=streams,recovery_inputs=descriptor['inherited_recovery_inputs'],native_inputs=native_inputs)
probe=recovery.CompactArchive(augmented)
assert len(probe.recipes)==11 and set(r['kind'] for r in probe.recipes.values())==recovery.RECIPE_KINDS
probe.close()
passed('Augmented bounded fixture validates four trace-sharing full pages, aliases, all four image families and a prior primitive native panel',fixture=ref(augmented))

def run(module,path,values,mutate=None,reprove=False):
    prior=recovery.CompactArchive(path);stats=dict(object_calls=collections.Counter(),zip_calls=collections.Counter(),zip_bytes=0,primitive_calls=collections.Counter(),trace_parses=collections.Counter(),current_reads=0,delta_info=0)
    phase={'primitive':False};items={n:(b,support.ROLE) for n,b in values.items()};hook={}
    orig_object=prior.object_bytes;orig_recipe=prior.recipe_bytes;orig_zip=prior.zip.read;orig_info=prior.pdf_object_info
    def read_object(pin):
        stats['object_calls'][(phase['primitive'],pin['object_path'])]+=1
        data=orig_object(pin)
        if hook.get('after_object'):hook['after_object'](pin,prior)
        return data
    def read_zip(name,*a,**k):
        data=orig_zip(name,*a,**k);stats['zip_calls'][(phase['primitive'],name)]+=1;stats['zip_bytes']+=len(data);return data
    def read_recipe(recipe,documents=None):
        stats['primitive_calls'][recipe['id']]+=1
        was=phase['primitive'];phase['primitive']=True
        try:return orig_recipe(recipe,documents)
        finally:phase['primitive']=was
    def info(pin):stats['delta_info']+=1;return orig_info(pin)
    prior.object_bytes=read_object;prior.recipe_bytes=read_recipe;prior.zip.read=read_zip;prior.pdf_object_info=info
    def loads(data,*a,**k):stats['trace_parses'][sha(data if isinstance(data,bytes) else data.encode())]+=1;return json.loads(data,*a,**k)
    old_json=module.json;module.json=types.SimpleNamespace(loads=loads,dumps=json.dumps)
    def read_current(path):stats['current_reads']+=1;return Path(path).read_bytes()
    if mutate:mutate(prior,items,hook)
    try:
        expanded,history=module.expand(items,prior,read_current)
        ordered=[dict(path=n,bytes=len(b if isinstance(b,bytes) else read_current(b)),sha256=sha(b if isinstance(b,bytes) else read_current(b)),role=role) for n,(b,role) in expanded.items()]
        result=dict(item_order=list(expanded),item_manifest=enc(ordered),history_bytes=enc(history))
        fresh=0
        if reprove:
            docs={}
            try:
                def read_pin(pin):
                    b=expanded[pin['logical_path']][0]
                    assert isinstance(b,bytes) and len(b)==pin['bytes'] and sha(b)==pin['sha256'];return b
                for h,recipe in history['recipes'].items():
                    data=recovery.recover_recipe(recipe,read_pin,read_pin,docs);fresh+=1
                    assert sha(data)==h
                    original=next(b for b,_ in expanded.values() if isinstance(b,bytes) and sha(b)==h)
                    assert data==original
            finally:
                for doc in docs.values():doc.close()
        result['fresh_reproof_count']=fresh
        return result,stats
    finally:
        module.json=old_json;prior.close()

def summary(stats):
    return dict(archive_object_calls=sum(stats['object_calls'].values()),distinct_archive_objects=len({k[1] for k in stats['object_calls']}),archive_zip_reads=sum(stats['zip_calls'].values()),archive_uncompressed_bytes_returned=stats['zip_bytes'],nonprimitive_object_calls=sum(n for (phase,_),n in stats['object_calls'].items() if not phase),nonprimitive_zip_reads=sum(n for (phase,_),n in stats['zip_calls'].items() if not phase),primitive_calls=dict(stats['primitive_calls']),trace_json_parses=sum(stats['trace_parses'].values()),trace_parses_by_sha=dict(stats['trace_parses']),delta_info_calls=stats['delta_info'],current_reads=stats['current_reads'])

comparisons=[]
for label,path,values,fresh in [('existing_synthetic_delta',first,read_fixture(first)[0],False),('existing_third_generation',third,third_payloads,False),('augmented_repetitions',augmented,payloads,True)]:
    a,sa=run(before,path,values,reprove=fresh);b,sb=run(after,path,values,reprove=fresh)
    assert a==b,label
    assert sa['primitive_calls']==sb['primitive_calls'],label
    assert sum(sb['zip_calls'].values())<sum(sa['zip_calls'].values()),label
    if fresh:assert a['fresh_reproof_count']==b['fresh_reproof_count']==11
    row=dict(fixture=label,ordered_items=len(a['item_order']),item_manifest_sha256=sha(a['item_manifest']),history_json_sha256=sha(a['history_bytes']),fresh_reproof_count=a['fresh_reproof_count'],before=summary(sa),proposed=summary(sb));comparisons.append(row)
    passed(label+' exact item bytes/order, serialized metadata and primitive invocations equal',comparison=row)
aug=comparisons[-1]
assert aug['before']['trace_json_parses']==4 and aug['proposed']['trace_json_parses']==1
passed('Four identical trace parses collapse to one exact immutable trace identity',before=4,proposed=1)

def reject_both(label,mutate):
    errors=[]
    for module in (before,after):
        try:run(module,augmented,payloads,mutate=mutate)
        except (ValueError,RuntimeError,KeyError,AttributeError) as e:errors.append((type(e).__name__,str(e)))
        else:raise AssertionError('Accepted '+label+' in '+module.__name__)
    assert errors[0]==errors[1],(label,errors)
    passed(label+' rejected equally',error_type=errors[0][0],error=errors[0][1])
def full_rows(p):return [r for r in p.recipes.values() if r['kind']==recovery.FULL_PAGE_KIND]
def natives(p):return [r for r in p.recipes.values() if r['kind']==recovery.NATIVE_KIND]
reject_both('Wrong repeated PDF SHA after valid first use',lambda p,i,h:full_rows(p)[1]['source_pdf'].update(sha256='0'*64))
reject_both('Wrong repeated PDF size after valid first use',lambda p,i,h:full_rows(p)[1]['source_pdf'].update(bytes=full_rows(p)[1]['source_pdf']['bytes']+1))
def wrong_object(p,i,h):
    q=p.logical['work/build/LM_FR_diplomatique.pdf'];q=p.logical[q['target_path']] if q['storage_kind']=='alias' else q
    full_rows(p)[1]['source_pdf']['object_path']=q['object_path']
reject_both('Wrong repeated immutable object association',wrong_object)
reject_both('Wrong native logical association despite cached valid source hash',lambda p,i,h:natives(p)[-1]['source_pdf'].update(logical_path='work/build/LM_FR_diplomatique.pdf'))
reject_both('Wrong repeated metadata SHA',lambda p,i,h:natives(p)[-1]['qualification']['metadata'].update(sha256='1'*64))
reject_both('Wrong repeated metadata size',lambda p,i,h:natives(p)[-1]['qualification']['metadata'].update(bytes=natives(p)[-1]['qualification']['metadata']['bytes']+1))
def conflict(p,items,hook):
    name=next(n for n,r in p.logical.items() if n.startswith(before.INPUT_PREFIX) and r['storage_kind']=='blob' and n.endswith('.pdf'))
    items[name]=(b'conflicting current auxiliary bytes',support.ROLE)
reject_both('Conflicting current immutable auxiliary path',conflict)
def bad_primitive_kind(p,items,hook):
    row=p.logical[primitive_path];row=p.logical[row['target_path']] if row['storage_kind']=='alias' else row
    p.recipes[row['recipe_id']]['kind']=recovery.COMPOSITE_KIND
reject_both('Unbounded prior auxiliary primitive kind',bad_primitive_kind)
def altered_delta_association(p,items,hook):
    obj=full_rows(p)[0]['source_pdf']['object_path'];done=[]
    def mutate(pin,prior):
        if pin['object_path']==obj and not done:
            prior.pdf_delta_objects[obj]['target_bytes']+=1;done.append(True)
    hook['after_object']=mutate
reject_both('Changed delta association on cached repeated source',altered_delta_association)

def equivalent_semantic(label,mutate):
    a,sa=run(before,augmented,payloads,mutate=mutate);b,sb=run(after,augmented,payloads,mutate=mutate)
    assert a==b and sa['primitive_calls']==sb['primitive_calls']
    passed(label+' preserves exact output and primitive count',before_parses=sum(sa['trace_parses'].values()),proposed_parses=sum(sb['trace_parses'].values()))
def missing_trace(p,items,hook):
    for row in full_rows(p):row['source_scan_trace']['logical_path']='work/data/nonexistent_trace.json'
equivalent_semantic('Missing recorded trace remains absent without fallback invention',missing_trace)
def mismatched_trace(p,items,hook):
    # This is the existing optional fallback branch: no explicit trace pin,
    # but a valid retained JSON object whose parsed source SHA does not match.
    for row in full_rows(p):row.pop('source_scan_trace',None)
    original=p.logical[meta_path];original=p.logical[original['target_path']] if original['storage_kind']=='alias' else original
    p.logical[trace_path]=dict(original,path=trace_path)
equivalent_semantic('Mismatched parsed fallback trace identity remains unadopted',mismatched_trace)

# One file-backed current PNG checks the untouched data() path without keeping
# every current PNG in the cache. Its path is external and synthetic only.
current_png=STAGE/'fixtures/current_png_source.png';current_png.write_bytes(payloads['work/verification/'+book+'/page_0001.png'])
def file_backed(p,items,hook):items['work/verification/'+book+'/page_0001.png']=(current_png,support.ROLE)
a,sa=run(before,augmented,payloads,mutate=file_backed);b,sb=run(after,augmented,payloads,mutate=file_backed)
assert a==b and sa['current_reads']==sb['current_reads']
passed('General current PNG reads remain uncached with identical invocation count',before_reads=sa['current_reads'],proposed_reads=sb['current_reads'])

for path,pin in active_pins.items():
    data=(ROOT/path).read_bytes();assert len(data)==pin['bytes'] and sha(data)==pin['sha256']
assert (ROOT/'work/scripts/checkpoint_inheritance.py').read_bytes()==(STAGE/'before/checkpoint_inheritance.py').read_bytes()
passed('All active helper bytes remain unchanged; proposal stays temporary and uninstalled')
report=dict(schema='temporary-expand-immutable-cache-controls-v1',status='PASS_TEMPORARY_PROPOSAL_NOT_INSTALLED',passed=len(checks),failed=0,controls=checks,comparisons=comparisons,active_dependencies=active_pins,checked_files=[ref(p) for p in (Path(__file__),STAGE/'before/checkpoint_inheritance.py',STAGE/'proposed/checkpoint_inheritance.py',STAGE/'prototype_support.py',STAGE/'CHANGE.json')],fixture_files=[ref(p) for p in (first,third,augmented)],scope='Only existing and augmented small synthetic fixtures were opened/rendered. No real production archive, collection, PDF or restore was rerun.',new_visual_review_claims=False,project_writes=False)
out=STAGE/'CONTROLS.json';out.write_bytes(enc(report));print(json.dumps(ref(out),indent=2))
