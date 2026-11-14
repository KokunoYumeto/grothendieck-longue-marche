"""Synthetic target-cardinality and existing codec controls; no real book plan."""
from pathlib import Path
import argparse,ast,collections,copy,hashlib,importlib.util,json,os,subprocess,sys,types,zipfile

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--project-root',required=True)
parser.add_argument('--runtime-directory',required=True)
args=parser.parse_args()
ROOT=Path(args.project_root).resolve();STAGE=Path(__file__).resolve().parent;RUNTIME=Path(args.runtime_directory).resolve()
if STAGE != ROOT/'work/records/checkpoint_pdf_delta_target23_staged_v1':
    raise ValueError('Use the explicitly authorized target23 stage.')
if RUNTIME.is_relative_to(ROOT) or RUNTIME.is_relative_to(STAGE):
    raise ValueError('Synthetic runtime must remain outside the project and stage.')
RUNTIME.mkdir(parents=True,exist_ok=True)
if any(RUNTIME.iterdir()):raise ValueError('Use a new empty synthetic runtime directory.')
sys.path[:0]=[str(STAGE/'proposed'),str(STAGE),str(ROOT/'work/scripts')]
import restore_checkpoint as recovery
import checkpoint_pdf_deltas as qualifier
import prototype_support as support
import pymupdf as fitz

sha=lambda data:hashlib.sha256(data).hexdigest()
enc=lambda value:(json.dumps(value,indent=2,ensure_ascii=False)+'\n').encode()
def ref(path):
    path=Path(path).resolve();data=path.read_bytes()
    if path.is_relative_to(STAGE):name=str(path.relative_to(STAGE))
    elif path.is_relative_to(RUNTIME):name='external-runtime/'+str(path.relative_to(RUNTIME))
    elif path.is_relative_to(ROOT):name=str(path.relative_to(ROOT))
    else:raise ValueError('Undeclared control artifact namespace.')
    return dict(path=name,bytes=len(data),sha256=sha(data))
def load_old(name):
    path=STAGE/'before'/(name+'.py');spec=importlib.util.spec_from_file_location('old_'+name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
old_recovery=load_old('restore_checkpoint');old_qualifier=load_old('checkpoint_pdf_deltas');old_qualifier.recovery=old_recovery
checks=[]
def passed(name,**extra):checks.append(dict(test=name,status='PASS',**extra));print(name,flush=True)
def rejected(name,fn):
    try:fn()
    except (ValueError,RuntimeError,KeyError) as error:
        passed(name,error_type=type(error).__name__,error=str(error));return
    raise AssertionError('Accepted negative control: '+name)

change=json.loads((STAGE/'CHANGE.json').read_text())
for row in change['changes']:
    before=(STAGE/row['before']['path']).read_text();after=(STAGE/row['proposed']['path']).read_text()
    assert after.replace(row['exact_new_literal'],row['exact_old_literal'])==before
    assert (ROOT/row['active_path']).read_bytes()==(STAGE/row['before']['path']).read_bytes()
    if Path(row['active_path']).name!='package_release.py':
        a=[ast.dump(n,include_attributes=False) for n in ast.parse(before).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))]
        b=[ast.dump(n,include_attributes=False) for n in ast.parse(after).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))]
        assert a==b
assert old_recovery.PDF_DELTA_MAX_TARGETS==16 and recovery.PDF_DELTA_MAX_TARGETS==23
assert old_recovery.PDF_DELTA_MAX_BYTES==recovery.PDF_DELTA_MAX_BYTES==64*1024*1024
passed('Exactly one cardinality constant and two documentation phrases change; all function logic and64MiB caps remain exact')

masters={'LM_FR_master_annotated':'LM_FR_corrige_apparat','LM_EN_master_annotated':'LM_EN_corrected_apparatus'}
primary=sorted(recovery.BOOKS-set(masters));assert len(primary)==5
base_bytes={}
for book in primary:
    doc=fitz.open();page=doc.new_page(width=220,height=260);page.insert_text((20,45),'Synthetic base '+book,fontsize=7)
    data=doc.tobytes(deflate=True);doc.close()
    # A valid trailing PDF comment ensures Git's binary classification without
    # changing page content. Only tiny synthetic PDFs are involved.
    data+=b'\n%\x00 bounded synthetic binary fixture\n'
    with fitz.open(stream=data,filetype='pdf') as proof:assert len(proof)==1
    base_bytes[book]=data

payloads={'work/build/'+book+'.pdf':data for book,data in base_bytes.items()}
inputs=[];targets=[];target_bytes={}
def plan_pin(book,data):return dict(reader=book,bytes=len(data),sha256=sha(data))
def append_target(book,generation,current=False):
    base_book=masters.get(book,book);base=base_bytes[base_book]
    target=base+('\n% synthetic target '+generation+' '+book+'\n').encode()
    name='work/build/'+book+'.pdf' if current else 'work/data/checkpoint_recovery_inputs/pdfs/'+sha(target)+'.pdf'
    payloads[name]=target;target_bytes[sha(target)]=target
    if not current:inputs.append(dict(path=name,bytes=len(target),sha256=sha(target),kind='source_pdf',reader=book,logical_path_at_capture='work/build/'+book+'.pdf'))
    targets.append(dict(base=plan_pin(base_book,base),target=plan_pin(book,target)))
for generation in ('synthetic-old-A','synthetic-old-B','synthetic-old-C'):
    for book in sorted(recovery.BOOKS):append_target(book,generation)
for book in sorted(masters):append_target(book,'synthetic-current',True)
assert len(targets)==23 and len({r['target']['sha256'] for r in targets})==23
assert not ({r['base']['sha256'] for r in targets}&set(target_bytes))
for i,row in enumerate(targets):payloads['work/data/synthetic_pdf_aliases/target_'+str(i)+'.pdf']=target_bytes[row['target']['sha256']]
origin=RUNTIME/'synthetic_origin_not_checkpoint.zip'
with zipfile.ZipFile(origin,'x',compression=zipfile.ZIP_DEFLATED) as z:z.writestr('README.txt','Synthetic bounded storage control. No production checkpoint or visual-review claim.\n')
plan=dict(schema=qualifier.PLAN_SCHEMA,maximum_depth=1,source_checkpoint=dict(filename=origin.name,bytes=origin.stat().st_size,sha256=sha(origin.read_bytes())),targets=targets)
items={n:(b,support.ROLE) for n,b in payloads.items()}
entries={n:dict(path=n,bytes=len(b),sha256=sha(b),role=support.ROLE) for n,b in payloads.items()};groups=collections.defaultdict(list)
for n,row in entries.items():groups[row['sha256']].append(n)
authorities=qualifier.book_authorities(entries,dict(recovery_inputs=inputs))
assert len({(r['reader'],r['sha256'],r['bytes']) for r in authorities})==28
read_payload=lambda _:(_ for _ in ()).throw(AssertionError('This bounded fixture is memory-only.'))
rejected('Original sixteen-target builder rejects the otherwise valid twenty-three-target fixture',lambda:old_qualifier.qualify(items,entries,groups,read_payload,plan,origin,authorities))
recipes,streams,fresh=qualifier.qualify(items,entries,groups,read_payload,plan,origin,authorities)
assert len(recipes)==len(streams)==fresh['target_count']==23 and fresh['primitive_base_count']==5
assert fresh['maximum_depth']==1 and fresh['all_bases_already_retained'] and fresh['exact_target_bytes_and_sha256_verified']
passed('Twenty-three named-book targets qualify against five full retained synthetic bases with actual generation and exact decoding',targets=23,bases=5,generator=fresh['generator'])

# Read a second, backward-compatible nine-row plan through the unchanged API.
legacy=copy.deepcopy(plan);legacy['targets']=legacy['targets'][:9]
legacy_recipes,_,legacy_proof=qualifier.qualify(items,entries,groups,read_payload,legacy,origin,authorities)
assert len(legacy_recipes)==legacy_proof['target_count']==9
passed('The existing nine-target profile continues to qualify unchanged',targets=9)
legacy16=copy.deepcopy(plan);legacy16['targets']=legacy16['targets'][:16]
legacy16_recipes,_,legacy16_proof=qualifier.qualify(items,entries,groups,read_payload,legacy16,origin,authorities)
assert len(legacy16_recipes)==legacy16_proof['target_count']==16
passed('The existing sixteen-target profile continues to qualify unchanged',targets=16)

archive=RUNTIME/'synthetic_twenty_three_targets.zip'
by_hash_stream={sha(data):data for data in streams.values()}
expected,physical=support.make_archive(archive,payloads,delta_records=list(recipes.values()),delta_streams=by_hash_stream,recovery_inputs=inputs)
validated=recovery.CompactArchive(archive)
try:
    assert len(validated.pdf_deltas)==23 and validated.verify_pdf_deltas()==23
    assert all(validated.logical_bytes(n)==b for n,b in expected.items())
    inventory_descriptor=copy.deepcopy(validated.descriptor);inventory_physical=copy.deepcopy(validated.physical)
finally:validated.close()
passed('Twenty-three-target archive passes exact current/inherited book authority, alias and primitive-base scope joins',logical_files=len(expected),delta_targets=23)
old_inventory=types.SimpleNamespace(descriptor=copy.deepcopy(inventory_descriptor),physical=copy.deepcopy(inventory_physical))
rejected('Original sixteen-target recovery boundary rejects the same twenty-three-target inventory',lambda:old_recovery.prepare_pdf_delta_inventory(old_inventory))

destination=RUNTIME/'standalone_restored';report=RUNTIME/'standalone_restore.json'
env=dict(os.environ,PATH='',PYTHONDONTWRITEBYTECODE='1')
run=subprocess.run([sys.executable,'-B',str(STAGE/'proposed/restore_checkpoint.py'),str(archive),'--output-dir',str(destination),'--verify','--report',str(report)],cwd=RUNTIME,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
(RUNTIME/'standalone_raw_stdout.txt').write_text(run.stdout)
assert run.returncode==0,run.stdout
restored=json.loads(report.read_text());assert restored['failure_count']==0 and restored['verified_pdf_delta_count']==23
for name,data in expected.items():assert (destination/name).read_bytes()==data
passed('Standalone standard-library delta recovery restores all twenty-three exact targets and aliases with Git absent from PATH',logical_files=len(expected),delta_targets=23,restore_report=ref(report))

def reject_before_generation(label,bad_plan,bad_authorities=None):
    calls=[];old=qualifier.generate
    def sentinel(*args):calls.append(True);raise AssertionError('Generation was reached for an invalid plan.')
    qualifier.generate=sentinel
    try:rejected(label,lambda:qualifier.qualify(items,entries,groups,read_payload,bad_plan,origin,authorities if bad_authorities is None else bad_authorities))
    finally:qualifier.generate=old
    assert not calls

extra_book='LM_FR_diplomatique';extra_base=base_bytes[extra_book];extra_target=extra_base+b'\n% synthetic twenty-fourth boundary target\n'
extra_plan=dict(base=plan_pin(extra_book,extra_base),target=plan_pin(extra_book,extra_target))
bad=copy.deepcopy(plan);bad['targets'].append(extra_plan)
reject_before_generation('Twenty-four target plans reject before any generator invocation',bad)
extra_delta=support.literal_delta(extra_base,extra_target)
assert recovery.apply_pdf_delta(extra_base,extra_delta,len(extra_target))==extra_target
extra_recipe=support.delta_recipe(extra_base,extra_target,extra_delta,extra_book)
bad_descriptor=copy.deepcopy(inventory_descriptor);bad_descriptor['pdf_delta_recovery']['recipes'].append(extra_recipe)
bad_physical=copy.deepcopy(inventory_physical);bad_physical[extra_recipe['delta']['object_path']]=dict(bytes=len(extra_delta),sha256=sha(extra_delta))
bad_archive=types.SimpleNamespace(descriptor=bad_descriptor,physical=bad_physical)
rejected('Twenty-four otherwise well-formed named targets reject at recovery inventory cardinality',lambda:recovery.prepare_pdf_delta_inventory(bad_archive))

bad=copy.deepcopy(plan);bad['maximum_depth']=2
reject_before_generation('Depth two remains rejected before generation',bad)
bad=copy.deepcopy(plan);bad['targets'][0]['target']['bytes']=recovery.PDF_DELTA_MAX_BYTES+1
reject_before_generation('A planned target above64MiB remains rejected before generation without allocation',bad)
same_book=[r for r in plan['targets'] if r['target']['reader']=='LM_FR_diplomatique']
bad=copy.deepcopy(plan);bad['targets']=copy.deepcopy(same_book);bad['targets'][1]['base']=copy.deepcopy(bad['targets'][0]['target'])
reject_before_generation('Base-target overlap and chains remain rejected before generation',bad)
bad=copy.deepcopy(plan);bad['targets'][0]['base']=plan_pin('LM_EN_corrected_apparatus',base_bytes['LM_EN_corrected_apparatus'])
if bad['targets'][0]['base']['reader']==masters.get(bad['targets'][0]['target']['reader'],bad['targets'][0]['target']['reader']):
    bad['targets'][0]['base']=plan_pin('LM_FR_diplomatique',base_bytes['LM_FR_diplomatique'])
reject_before_generation('Wrong named-book base relationship remains rejected before generation',bad)
unauthorized=plan['targets'][0]['target'];missing=[r for r in authorities if (r['reader'],r['sha256'],r['bytes'])!=(unauthorized['reader'],unauthorized['sha256'],unauthorized['bytes'])]
reject_before_generation('Missing exact target provenance remains rejected before generation',plan,missing)
bad=copy.deepcopy(plan);bad['targets'][0]['base']['bytes']=recovery.PDF_DELTA_MAX_BYTES+1
reject_before_generation('A planned base above64MiB remains rejected before generation without allocation',bad)
unauthorized_base=plan['targets'][0]['base'];missing_base=[r for r in authorities if (r['reader'],r['sha256'],r['bytes'])!=(unauthorized_base['reader'],unauthorized_base['sha256'],unauthorized_base['bytes'])]
reject_before_generation('Missing exact primitive-base provenance remains rejected before generation',plan,missing_base)
for field,new_value in [('filename','different_synthetic_origin.zip'),('bytes',origin.stat().st_size+1),('sha256',sha(b'different synthetic origin'))]:
    bad=copy.deepcopy(plan);bad['source_checkpoint'][field]=new_value
    reject_before_generation('Mismatched exact source-checkpoint '+field+' rejects before generation',bad)
bad=copy.deepcopy(plan);bad['targets'][-1]=copy.deepcopy(bad['targets'][0])
reject_before_generation('Duplicate target digest remains rejected within the23-target ceiling',bad)
missing_primitive=types.SimpleNamespace(descriptor=copy.deepcopy(inventory_descriptor),physical=copy.deepcopy(inventory_physical))
missing_primitive.physical.pop(next(iter(recipes.values()))['base_object_path'])
rejected('Recovery inventory rejects a base lacking its exact full physical object',lambda:recovery.prepare_pdf_delta_inventory(missing_primitive))


# The existing bounded decoder cases are repeated without changing the codec.
base=b'A'*65536
assert recovery.apply_pdf_delta(base,support.varint(len(base))+support.varint(len(base))+b'\x80',len(base))==base
assert recovery.apply_pdf_delta(b'abcd',support.varint(4)+support.varint(5)+b'\x91\x01\x03\x02XY',5)==b'bcdXY'
passed('Existing COPY default65536 and offset/length plus literal mixture still decode exactly')
prefix=support.varint(4)+support.varint(4)
negative={
 'truncated delta size':b'\x80',
 'nonminimal delta size':b'\x84\x00'+support.varint(4)+b'\x04abcd',
 'oversized delta size':support.varint(recovery.PDF_DELTA_MAX_BYTES+1)+support.varint(4)+b'\x04abcd',
 'wrong declared base size':support.varint(3)+support.varint(4)+b'\x04abcd',
 'wrong declared target size':support.varint(4)+support.varint(3)+b'\x03abc',
 'zero opcode':prefix+b'\x00',
 'truncated copy offset':prefix+b'\x81',
 'truncated copy length':prefix+b'\x90',
 'copy source overrun':prefix+b'\x91\x03\x04',
 'copy target overrun':prefix+b'\x90\x05',
 'truncated literal':prefix+b'\x04abc',
 'literal target overrun':prefix+b'\x05abcde',
 'incomplete output':prefix+b'\x03abc',
 'extra trailing command':prefix+b'\x04abcd\x01Z'}
for name,data in negative.items():rejected('Existing decoder case: '+name,lambda data=data:recovery.apply_pdf_delta(b'abcd',data,4))
rejected('Existing decoder rejects boolean target length',lambda:recovery.apply_pdf_delta(b'a',b'\x01\x01\x01a',True))

for row in change['changes']:assert (ROOT/row['active_path']).read_bytes()==(STAGE/row['before']['path']).read_bytes()
passed('All three active helpers remain byte-exact; no concrete revision878 plan, production collection or publication PDF was used')
output=dict(schema='staged-twenty-three-target-boundary-controls-v1',status='PASS_STAGED_PROPOSAL_NOT_INSTALLED',passed=len(checks),failed=0,controls=checks,checked_files=[ref(Path(__file__)),ref(STAGE/'prototype_support.py'),ref(STAGE/'CHANGE.json')]+[ref(STAGE/label/name) for label in ('before','proposed') for name in ('restore_checkpoint.py','checkpoint_pdf_deltas.py','package_release.py')],synthetic_profile={'target_count':23,'primitive_base_count':5,'old_generations':3,'current_master_targets':2,'all_names_from_existing_BOOKS':True,'revision878_PDFs_used':False,'actual_future_savings_claimed':False},external_runtime_artifacts=[ref(origin),ref(archive),ref(report)],synthetic_payloads_excluded_from_collection=True,active_helpers_changed=False,review_or_production_records_written=False,writes_confined_to_new_stage_and_external_synthetic_runtime=True,production_archive_or_render_or_restore_run=False,new_visual_review_claims=False)
out=STAGE/'CONTROLS.json';out.write_bytes(enc(output));print(json.dumps(ref(out),indent=2))
