"""Check only the authorized scan023 public-repair closure and its mutations."""
from pathlib import Path
import collections
import copy
import hashlib
import json
import re

ROOT=Path('/workspace/scratch/94548b74fbe0')
P=ROOT/'out/checks'
EXPECTED={
 'scan023_record_draft.json':'40fbc60b1bfbf1ad186f53e635fe0b6a0b2bb6dd4da35f64594c833c2538e840',
 'scan023_record_public_repair_closure.json':'2d299e8fe05998cfc5b418de0e95a4885010155c9d48277acdc8f745105749de',
 'scan023_record_gate.json':'9939f45a042899d1ae8d1491e811095644ec6af2401f0ea2df50249aa6599f9f',
 'scan023_record_release.json':'3657baec1ddb9dca370f8fdabe299a862e6c721b59ffd82f960c5484f04c05a1',
 'scan023_root_public_repair_authorization.json':'988322521bcf2fd8b30c6f20b5760c94bd6e668f1a6ecc2d5241f807205ab97c',
 'scan023_root_public_repair_mirror_scope.json':'3ecd648b26426dbd68c670c44284959eeadf6d4ef9d24b992b1df2037b6180e4',
 'scan023_source_audit.json':'323eb5bfe03de3afff22ab8e100c9a1a12a4a9e4bfe40b727b10441c3ff3fdc7',
 'scan023_source_audit.md':'fdce0ff2240ef026e8ae271f47b7607acc3c65b44fa9ea5262f5f94079ad8f64',
}
cache={};bindings={};errors=[];checks={}

def digest(x):return hashlib.sha256(x).hexdigest()
def data(path):
    path=str(path)
    assert Path(path).suffix in {'.json','.md','.tex','.txt','.py','.tsv'}
    assert 'crop_audit' not in path
    if path not in cache:cache[path]=(ROOT/path).read_bytes()
    bindings[path]=digest(cache[path])
    return cache[path]
def obj(name):return json.loads(data('out/checks/'+name))
def require(ok,pointer,message):
    if not ok:errors.append({'pointer':pointer,'message':message})
def get(value,path):
    for token in path.lstrip('/').split('/') if path else []:
        token=token.replace('~1','/').replace('~0','~')
        value=value[int(token)] if isinstance(value,list) else value[token]
    return value
def put(value,path,op,replacement=None):
    base,_,token=path.rpartition('/');parent=get(value,base)
    token=token.replace('~1','/').replace('~0','~')
    if isinstance(parent,list):
        token=int(token)
        if op=='add':parent.insert(token,copy.deepcopy(replacement))
        elif op=='remove':parent.pop(token)
        else:parent[token]=copy.deepcopy(replacement)
    elif op=='remove':del parent[token]
    else:parent[token]=copy.deepcopy(replacement)
def encode(value):return (json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
def walk(value,path=''):
    yield path,value
    if isinstance(value,dict):
        for k,v in value.items():
            if k=='root_crop_audit':continue
            yield from walk(v,path+'/'+str(k).replace('~','~0').replace('/','~1'))
    elif isinstance(value,list):
        for i,v in enumerate(value):yield from walk(v,path+'/'+str(i))

for name,want in EXPECTED.items():require(digest(data('out/checks/'+name))==want,name,'Frozen closure input hash differs.')
current=obj('scan023_record_draft.json')
closure=obj('scan023_record_public_repair_closure.json')
auth=obj('scan023_root_public_repair_authorization.json')
audit=obj('scan023_source_audit.json')
gate=obj('scan023_record_gate.json');release=obj('scan023_record_release.json')
baseline_path=closure['baseline_files']['scan023_record_draft.json']['snapshot']['path']
baseline=json.loads(data(baseline_path))

for name,item in closure['baseline_files'].items():
    require(digest(data(item['snapshot']['path']))==item['snapshot']['sha256']==item['original_sha256'],name,'Preserved pre-repair bytes differ.')
for name,item in closure['unchanged_text_files'].items():
    require(digest(data(item['path']))==item['sha256'],name,'Protected text artifact changed.')
old_bindings=dict(audit['mechanical_validation']['checks']['checked_text_source_hashes'])
old_bindings.update(audit['additional_text_source_hashes'])
replaced={'out/checks/scan023_record_draft.json','out/checks/scan023_record_review.md','out/checks/scan023_record_gate.json','out/checks/scan023_record_release.json'}
for path,want in old_bindings.items():
    if path not in replaced:
        require(digest(data(path))==want,path,'Pre-existing text source/history hash differs from the frozen audit.')
checks['preserved_baseline_files']=len(closure['baseline_files'])
checks['protected_preexisting_text_files']=len(set(old_bindings)-replaced)

targets={}
for finding in audit['findings']:
    for item in finding['targets']:
        targets[item['pointer']]={'before':item['before'],'after':item['proposed_after'],'finding':finding['id']}
for item in auth['overrides']+auth['additional_targets']:
    targets[item['pointer']]={'before':item['before'],'after':item['after'],'finding':'root-explicit'}
require(len(targets)==92,'authorized-targets','Expected 92 distinct explicit targets.')
declared={x['pointer']:x for x in closure['exact_authorized_targets']}
require(set(declared)==set(targets),'authorized-targets','Closure target set differs from root authority.')
for pointer,item in targets.items():
    require(get(baseline,pointer)==item['before'],pointer,'Explicit baseline value differs.')
    require(get(current,pointer)==item['after'],pointer,'Explicit authorized replacement differs.')
    require(declared[pointer]['before']==item['before'] and declared[pointer]['after']==item['after'],pointer,'Closure target declaration differs from authority.')
checks['exact_authorized_targets']=len(targets)

ops=closure['forward_operations']
require(len(ops)==399 and len({x['path'] for x in ops})==399,'forward_operations','Operation list must have 399 unique paths.')
replay=copy.deepcopy(baseline)
for op in ops:
    if op['op']!='add':require(get(replay,op['path'])==op['before'],op['path'],'Forward before-value differs.')
    put(replay,op['path'],op['op'],op.get('after'))
require(encode(replay)==data('out/checks/scan023_record_draft.json'),'forward-replay','Forward replay differs from frozen current bytes.')
inverse=copy.deepcopy(current)
for op in reversed(ops):
    reverse={'replace':'replace','add':'remove','remove':'add'}[op['op']]
    put(inverse,op['path'],reverse,op.get('before'))
require(encode(inverse)==data(baseline_path),'inverse-replay','Inverse replay differs from frozen baseline bytes.')
checks['forward_operations']=len(ops)
checks['operation_types']=dict(collections.Counter(x['op'] for x in ops))
checks['forward_replay_sha256']=digest(encode(replay))
checks['inverse_replay_sha256']=digest(encode(inverse))

# Mutation boundary: this closes the existing repair only and does not reread
# source loci or reconsider any earlier ink/candidate decision.
mirrors=closure['mirror_selection']['accepted_current_mirrors']
mirror_paths={x['destination'] for x in mirrors}
add_parents={x['pointer'].rsplit('/',1)[0] for x in closure['local_reference_additions']}
require({x['path'] for x in ops}==set(targets)|mirror_paths|add_parents,'operation-scope','An operation is outside explicit targets, declared mirrors or authorized local-reference additions.')
require(len(mirror_paths-set(targets))==282,'mirror-scope','Expected 282 distinct non-target mirror fields.')

baseline_decisions={d['id']:d for d in baseline['decisions']}
def component_closure(ids):
    result=set(ids);pending=list(ids)
    while pending:
        did=pending.pop()
        for component in baseline_decisions[did].get('selected_component_readings',[]):
            child=component['decision_id']
            if child not in result:
                result.add(child);pending.append(child)
    return result

def identity_set(pointer):
    parts=pointer.strip('/').split('/')
    if parts[0]=='decisions':
        d=baseline['decisions'][int(parts[1])]
        if 'selected_component_readings' in parts:
            q=parts.index('selected_component_readings')
            return {d['selected_component_readings'][int(parts[q+1])]['decision_id']}
        ids={d['id']}
        if parts[2]=='evidence':ids=component_closure(ids)
        return ids
    if parts[0]=='source_locus_coverage':
        lc=baseline['source_locus_coverage'][int(parts[1])]
        ids=set(lc['decision_ids'])
        return component_closure(ids) if parts[2]=='evidence' else ids
    if parts[0]=='selected_graphical_groups':
        group=baseline['selected_graphical_groups'][int(parts[1])]
        if parts[2]=='current_readings':return {group['current_readings'][int(parts[3])]['decision_id']}
        ids=set(group['decision_ids'])
        return component_closure(ids) if parts[2]=='evidence' else ids
    if parts[0]=='doubts':return set(baseline['doubts'][int(parts[1])]['decision_ids'])
    if parts[0]=='inventory':return set(baseline['inventory'][int(parts[1])]['decision_ids'])
    if parts[0]=='C_source_rows':return set(baseline['C_source_rows'][int(parts[1])]['source_parts'][int(parts[3])]['decision_ids'])
    return set()

for item in mirrors:
    origin=item['origin'];destination=item['destination']
    require(origin in targets,destination,'Mirror origin is not an explicitly authorized target.')
    require(item['origin_locus'] in identity_set(destination),destination,'Mirror lacks the required explicit decision/component identity.')
checks['mirror_edges']=len(mirrors)
checks['identity_mirror_fields']=len(mirror_paths-set(targets))
checks['excluded_equality_candidates']=len(closure['mirror_selection']['excluded_equality_candidates'])
checks['containing_evidence_identity_rule']='A containing evidence field follows its explicit decision_ids and those decisions\' explicit selected_component_readings/decision_id links; current_readings rows retain their individual decision identity.'

unauthorized_witness=[];unauthorized_readers=[]
for index,(old,new) in enumerate(zip(baseline['decisions'],current['decisions'])):
    for who in ['C','H']:
        pointer=f'/decisions/{index}/{who}'
        if pointer not in targets and old[who]!=new[who]:unauthorized_witness.append(pointer)
    for who in ['A','B','C']:
        pointer=f'/decisions/{index}/readers/{who}'
        if pointer not in targets and old['readers'][who]!=new['readers'][who]:unauthorized_readers.append(pointer)
checks['non_target_witness_changes']=unauthorized_witness
checks['non_target_own_reader_changes']=unauthorized_readers
for pointer in unauthorized_witness:require(False,pointer,'A selected-reading mirror changed a witness cell outside the explicit C/H target set.')
for pointer in unauthorized_readers:require(False,pointer,'Own-reader value changed outside the six explicit reader additions.')

# All protected fields must be exactly equal, including raw sources, attached
# literal contexts and complete historical provenance objects.
protected={'provenance','reader_source_details','source_attachments','complete_witness_contexts','witness_source_references','selected_source','selected_draft','selected_source_map','source_map_reference','selected_source_map_reference','root_crop_evidence','root_viewing_scope','root_count_authorization','root_scope_authorization','counts','confidence','physical_count_parent','diff_C','diff_H','H_marker_ids','H_marker_basis','marked_in_H','C_doubt_status','C_source_row_ids','C_source_part_ids','selected_status','outcome','main_approved','root_approved','selected_page_approved','main_adjudicated','check_events','root_count_basis','hand','hand_scope','hand_status','selected_group_ids','inventory_ids','decision_ids'}
protected_count=0
for pointer,value in walk(baseline):
    if pointer.rsplit('/',1)[-1] in protected:
        protected_count+=1
        require(get(current,pointer)==value,pointer,'A protected attachment, history, identity or decision-control value changed.')
checks['protected_field_comparisons']=protected_count
checks['counts']=current['counts']

observations={x['observation'] for d in baseline['decisions'] for x in d['root_crop_evidence']}
observation_corruptions=[]
for op in ops:
    if op['op']!='replace' or not isinstance(op['before'],str):continue
    if not (op['path'].endswith('/evidence') or op['path'].endswith('/reason')):continue
    lost=[s for s in observations if op['before'].count(s)>op['after'].count(s)]
    if lost:
        observation_corruptions.append({'pointer':op['path'],'lost_observation_count':len(lost)})
        require(False,op['path'],'Root observation wording was altered by an embedded witness-cell substitution.')
checks['root_observation_corruptions']=observation_corruptions

# Close only the added reference fields: exact C/H bytes, their local range and
# the explicitly corresponding public value. Existing broad contexts stay fixed.
additions=closure['local_reference_additions'];ref_count=0
require(len(additions)==44 and len(add_parents)==25,'local_reference_additions','Expected 44 local-reference fields in 25 newly added maps.')
for entry in additions:
    pointer=entry['pointer'];value=entry['after']
    require(get(current,pointer)==value,pointer,'Added reference field differs from closure.')
    require(value['corresponding_public_field']==entry['origin'] and entry['origin'] in targets,pointer,'Local reference lacks an explicit public target.')
    require(get(current,value['retained_complete_context_pointer'])==get(baseline,value['retained_complete_context_pointer']),pointer,'Pre-existing complete witness context changed.')
    public=get(current,entry['origin'])
    for ref in value['exact_local_sources']:
        ref_count+=1
        raw=data(ref['path']);full=raw.decode('utf-8')
        require(digest(raw)==ref['sha256_utf8'],pointer,'Added reference file hash differs.')
        require(full[ref['char_start_zero_based']:ref['char_end_exclusive']]==ref['literal'],pointer,'Added exact local source span differs.')
        require(digest(ref['literal'].encode())==ref['span_sha256_utf8'],pointer,'Added local literal hash differs.')
        require(ref['literal'] in public,pointer,'Added exact excerpt is absent from its corresponding authorized public field.')
checks['added_local_reference_fields']=len(additions)
checks['added_decision_reference_maps']=len(add_parents)
checks['added_exact_text_spans']=ref_count

# Baseline-aligned selected mirrors must follow the same decision and field.
current_d={d['id']:d for d in current['decisions']}
old_d={d['id']:d for d in baseline['decisions']}
selected_mirror_checks=0
for root in ['source_locus_coverage','selected_graphical_groups','decisions','doubts']:
    for index,old in enumerate(baseline[root]):
        new=current[root][index]
        candidates=[]
        if root=='source_locus_coverage':candidates=[(old,new,old['locus_id'],f'/{root}/{index}')]
        elif root=='selected_graphical_groups':candidates=[(x,new['current_readings'][j],x['decision_id'],f'/{root}/{index}/current_readings/{j}') for j,x in enumerate(old['current_readings'])]
        elif root=='decisions':candidates=[(x,new['selected_component_readings'][j],x['decision_id'],f'/{root}/{index}/selected_component_readings/{j}') for j,x in enumerate(old.get('selected_component_readings',[]))]
        else:
            candidates=[(old,new,did,f'/{root}/{index}') for did in old['decision_ids']]
        for oldrow,newrow,did,ptr in candidates:
            for field,decisionfield in [('reading','final'),('alternatives','alternatives')]:
                if field in oldrow and oldrow[field]==old_d[did][decisionfield]:
                    selected_mirror_checks+=1
                    require(newrow[field]==current_d[did][decisionfield],ptr+'/'+field,'Selected current mirror lost its decision field identity.')
checks['baseline_aligned_selected_mirror_comparisons']=selected_mirror_checks

for name,item in release['current_files'].items():
    require(digest(data(item['path']))==item['sha256'],name,'Current release text-file hash differs.')
require(gate['record']['sha256']==EXPECTED['scan023_record_draft.json'],'gate/record','Gate binds a different record.')
require(release['main_approved'] is False and gate['root_approved'] is False,'approval','Approval must remain false.')

# Root has confirmed these two semantic defects. Keep the exact first attempt
# frozen and propose only the four resulting field repairs.
bad_h=targets['/decisions/34/H']['after']
good_h=targets['/decisions/34/H']['before']
repair_paths=['/decisions/35/C','/decisions/34/evidence','/source_locus_coverage/34/evidence','/selected_graphical_groups/14/evidence']
repairs=[]
for pointer in repair_paths:
    before=get(current,pointer)
    after=get(baseline,pointer) if pointer!='/selected_graphical_groups/14/evidence' else before.replace(bad_h,good_h)
    require(before!=after,pointer,'Expected concrete closure repair is not present.')
    repairs.append({'pointer':pointer,'before':before,'proposed_after':after,
      'repair_basis':'Restore the exact baseline witness C value.' if pointer=='/decisions/35/C' else 'Restore baseline root observation/absence wording; preserve every other authorized selected-reading update.',
      'restores_full_baseline_field':after==get(baseline,pointer)})

report={'scan':23,'stage':'bounded_public_repair_closure_check','verdict':'bounded_closure_requires_four_field_repair' if errors else 'pass',
 'main_approved':False,'scope':'Only the 399-operation authorized repair closure, its 92 targets, identity mirrors, preserved inputs/controls, added local references and exact forward/inverse byte correspondence. No broad second audit, images, image metadata, ink work, mathematical/coordinate checks, compilation, rendering, research, installation or delegation.',
 'bound_inputs':EXPECTED,'checks':checks,'concrete_failures':errors,'bounded_repairs':repairs,
 'preservation':'Keep the current 40fbc60b record and 2d299e8f closure as the first attempted repair; preserve the original audit and all older histories. Apply only root-authorized follow-up field corrections and append a new exact closure.',
 'text_file_bindings_checked':bindings}
(P/'scan023_source_audit_bounded_closure.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
lines=['# Scan023 — bounded repair closure check','',
 '**Verdict: four exact field repairs remain. Approval remains false.**','',
 'The 92 explicit authorized values are applied correctly. The 399 listed operations reconstruct the current bytes exactly and invert to the frozen baseline bytes. The remaining defects arise in semantic mirror selection: one selected value entered a witness-C field, and one witness-H replacement entered three root-evidence fields.','',
 '## Concrete remaining defects','',
 '| Field | Required bounded repair |','|---|---|',
 '| `/decisions/35/C` | Restore the baseline C reading `\\inserted{$\\exists\\alpha\\in K$ tel que}`. The selected live/deleted-que candidates belong in selected-reading fields; this C cell retains its original live inserted clause. |',
 '| `/decisions/34/evidence` | Restore this entire field to its baseline value. The H-cell wording was inserted into “No separate dans un follows”, altering the root observation and the selected absence description. |',
 '| `/source_locus_coverage/34/evidence` | Restore the same exact baseline evidence as the decision. |',
 '| `/selected_graphical_groups/14/evidence` | Replace only the injected full H-cell string with its original `dans un` token. Preserve the other authorized current selected-reading updates in this group. |','',
 'The JSON companion gives all four exact current and proposed replacement strings. The U35 H field itself remains the explicitly authorized cancelled-tail value. The U36 final field retains its authorized full selected candidates.','',
 '## Closure gates','',
 '- Exact equality passed for all 91 audit targets, with the root U56 final override, plus the additional U62 C-comment target: 92 targets total.',
 '- All 399 operations are enumerated: 374 replacements and 25 added local-reference maps. Their scope is the explicit targets, 282 distinct current-mirror fields and the authorized additions. The 348 mirror edges retain explicit locus/component associations; the two semantic exceptions above still require repair.',
 '- Every own-reader field outside the six explicit additions remains at baseline. The sole witness C/H change outside explicit targets is `/decisions/35/C`, identified above.',
 '- Pre-existing source attachments, complete witness contexts, raw reader detail and provenance remain exact. Counts, parents, confidences, C outcomes, H-marker values, hand scopes, identity links and approval values remain unchanged.',
 '- All 44 added local-reference fields in 25 decision maps match exact original C/H source bytes and their associated authorized public readings. They contain '+str(ref_count)+' exact text spans. Prior attachments and broad contexts are preserved.',
 '- Forward replay SHA-256: `'+checks['forward_replay_sha256']+'`. Inverse replay SHA-256: `'+checks['inverse_replay_sha256']+'`.',
 '- Original audit JSON/MD, selected TeX/map, root authorizations, preserved pre-repair files and previous history hashes remain unchanged. No broad audit or prohibited source/image work was performed.','',
 '## Frozen first-attempt bindings','', '| File | SHA-256 |','|---|---|']
for name,want in EXPECTED.items():lines.append('| '+name+' | `'+want+'` |')
lines += ['','Preserve this first repair attempt and its closure. A follow-up may change only the four listed fields after root authorization, with exact old/new history and approval still false.','']
(P/'scan023_source_audit_bounded_closure.md').write_text('\n'.join(lines))
print(json.dumps({'verdict':report['verdict'],'concrete_failures':errors,'repairs':repair_paths,'checks':checks,
 'outputs':{name:digest((P/name).read_bytes()) for name in ['scan023_source_audit_bounded_closure.md','scan023_source_audit_bounded_closure.json']}},ensure_ascii=False,indent=2))
