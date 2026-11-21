"""Generate only an exact source-selection plan; never mutate frozen artifacts.

The separate replay entry point is for root's independent source replay.
"""
from pathlib import Path
import json,hashlib,sys
sys.dont_write_bytecode=True
B=Path('/workspace/scratch/94548b74fbe0');D=B/'out/checks'
sys.path.insert(0,str(D));import scan024_source_support as support
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes) else x.encode()).hexdigest()
cache={};parsers={};files={};fileids={}
def text(p):
    if p not in cache:cache[p]=(B/p).read_text()
    return cache[p]
def data(p):return json.loads(text(p))
def fileid(p):
    if p not in fileids:
        k=f'F{len(files)+1:03d}';fileids[p]=k;files[k]=dict(path=p,sha256_utf8=sha(text(p)),characters=len(text(p)),bytes=len(text(p).encode()))
    return fileids[p]
def ptr(x,p):
    for k in p.split('/')[1:]:
        k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
    return x
def esc(k):return str(k).replace('~','~0').replace('/','~1')
def sr(p,a,b,pointer=None):
    t=text(p);r=dict(file=fileid(p),chars=[a,b],utf8_bytes=[len(t[:a].encode()),len(t[:b].encode())],sha256_utf8=sha(t[a:b]))
    if pointer is not None:r['json_pointer']=pointer
    return r
def jr(p,pointer):
    if p not in parsers:parsers[p]=support.JSONSpans(text(p))
    a,b=parsers[p].spans[pointer];return sr(p,a,b,pointer)
P='out/checks/scan024_source_public_projection_v02.json';PROJ=data(P)
RPATH=PROJ['record_path'];R=data(RPATH)
S=data('out/checks/scan024_source_row_skeleton_v01.json');POOL=S['source_reference_pool']
FP='out/checks/scan024_source_reader_frame_projection.json';F=data(FP)['frames']
def poolref(rid):
    q=POOL[rid]['exact_source_ref'];return sr(q['source_path'],q['character_start'],q['character_end_exclusive'],q.get('json_pointer'))
def ref_value(r):return json.loads(text(files[r['file']]['path'])[r['chars'][0]:r['chars'][1]])
OWN=['id','reading','alternatives','qualification','C_doubt_status','source_group','source_groups','mark_hand','mark_role','scope_note','separate_scope','role_confidence','complete_phrase_candidates','complete_group_reading','complete_group_alternatives','complete_group_states','group_owned_words_and_marks','group_qualification','contextual_recurrence','role','hand','attachment','surface_origin','local_details','recurring_print_rule','local_components','hand_scope','source_row_context','sublocus','source_row_component_status']
IK=['element','hand','kind','position','first_words_or_objects','role','component_of','source_refs','source_groups','source_group']
REPAIRS={'A':[2,4,6,25,31,36,38,41,48],'B':[38],'C':[26,43]}
inventories={}
for role,indices in REPAIRS.items():
    p=f'out/readers/024/{role}/report.json';v=data(p)
    for i in indices:
        obj=v['inventory'][i];key=f'{role}:inventory:{i}'
        inventories[key]=dict(reader=role,original_identity=obj['element'],source=jr(p,f'/inventory/{i}'),ordered_fields=[k for k in IK if k in obj],hand_source=jr(p,f'/inventory/{i}/hand'))
groups={};frame_entries=[]
for fk,f in F.items():
    role=fk[0];ff=f['exact_source'];grefs=[]
    for gi,g in enumerate(f['group_projection']):
        gid=g['group_id'];grefs.append(dict(group=gid,group_projection_pointer=f'/frames/{esc(fk)}/group_projection/{gi}',public_range_in_projected_literal=[g['public_start'],g['public_end']]))
        if gid in groups:continue
        st=S['complete_own_group_candidate_scopes'][role][gid];rawref=poolref(st['complete_own_TeX_ref']);srcpath=files[rawref['file']]['path'];a,b=rawref['chars'];rawtext=text(srcpath)[a:b]
        fields=[dict(name=k,source=poolref(st['raw_state_field_refs'][k])) for k in st['raw_own_state_fields']]
        comments=[];pos=a
        for line in rawtext.splitlines(keepends=True):
            bare=line.rstrip('\r\n')
            if bare.startswith('%') and 'BEGIN' not in bare and 'END' not in bare:comments.append(sr(srcpath,pos,pos+len(bare)))
            pos+=len(line)
        children=[]
        for cg,cs in S['complete_own_group_candidate_scopes'][role].items():
            cf=poolref(cs['complete_own_TeX_ref'])
            if cg!=gid and cf['file']==rawref['file'] and a<=cf['chars'][0] and cf['chars'][1]<=b:
                children.append(dict(group=cg,ordered_fields=[dict(name=k,source=poolref(cs['raw_state_field_refs'][k])) for k in cs['raw_own_state_fields']]))
        invkeys=[]
        for key,inv in inventories.items():
            if inv['reader']!=role:continue
            obj=ref_value(inv['source']);owned=obj.get('source_refs',[])+obj.get('source_groups',[])+([obj['source_group']] if obj.get('source_group') else [])
            if set(owned)&{gid,*[x['group'] for x in children]}:invkeys.append(key)
        groups[gid]=dict(reader=role,literal_group_source=rawref,ordered_fields=fields,comment_line_sources=comments,contained_group_fields=children,inventory_clauses=invkeys,expected_public_sha256_utf8=sha(g['public_value']),expected_public_source=jr(FP,f'/frames/{esc(fk)}/group_projection/{gi}/public_value'))
    ids=[k for k,v in PROJ['values'].items() if v==f['public']]
    archive=next((k for k in inventories if k==role+':inventory:'+str({'A':48,'B':38,'C':43}[role])),None) if '% archive sheet number: 23' in ff['literal'] and len(ff['literal'])<250 else None
    frame_entries.append(dict(frame=fk,reader=role,public_pool_ids=ids,original_source=sr(ff['path'],ff['char_start'],ff['char_end']),existing_frame_source=jr(FP,f'/frames/{esc(fk)}'),group_substitutions=grefs,archive_inventory_clause=archive))
frame_value_ids={v for f in frame_entries for v in f['public_pool_ids']}
used={k for d in PROJ['public_fields']['decisions'] for role in 'ABC' for k in d['readers'][role]['concat']}
appendices={};other={};bindings=[];issues=[]
prefix='Own local report/doubt fields (verbatim values; complete source/group scopes above remain controlling): '
absence='The inspected complete difference list has no row for this source correspondence; the exact own TeX frame above supplies this reader’s actual text. This absence statement is bounded by that complete report and frame.'
for di,d in enumerate(R['decisions']):
    for role in 'ABC':
        binding=PROJ['public_fields']['decisions'][di]['readers'][role]['concat']
        b=dict(decision_id=d['id'],reader=role,record_pointer=f'/decisions/{di}/readers/{role}',projection_pointer=f'/public_fields/decisions/{di}/readers/{role}',pool_ids=binding,expected_reader_sha256_utf8=sha(d['readers'][role]))
        if d['source_locus_id'].startswith('SRC024-L'):
            row=S['rows'][int(d['source_locus_id'].split('L')[1])-1];own=row['readers'][role];entries=[];objects=[]
            for section,rids in [('differences',own['raw_own_difference_refs']),('doubts',own['raw_own_doubt_refs'])]:
                for rid in rids:
                    ref=poolref(rid);obj=ref_value(ref);keys=[k for k in OWN if k in obj];value={k:obj[k] for k in keys}
                    emitted=objects.index(value) if section=='doubts' and value in objects else len(objects)
                    duplicate=emitted<len(objects)
                    if not duplicate:objects.append(value)
                    entries.append(dict(section=section,original_id=obj.get('id'),source=ref,ordered_fields=keys,emitted_object_index=emitted,duplicate_existing_value=duplicate))
            expected='\n\n'+prefix+json.dumps(objects,ensure_ascii=False,separators=(',',':')) if objects else '\n\n'+absence
            if objects:
                ids=[pid for pid in binding if PROJ['values'][pid]==expected]
                if len(ids)!=1:issues.append(dict(decision=d['id'],reader=role,issue='local appendix has no unique exact binding',matching_pool_ids=ids))
                for pid in ids:
                    if pid not in appendices:appendices[pid]=dict(reader=role,source_entries=entries,leading_editorial_literal='\n\n'+prefix,expected_value_sha256_utf8=sha(PROJ['values'][pid]),v02_pool_pointer='/values/'+pid,uses=[])
                    appendices[pid]['uses'].append(dict(decision_id=d['id'],record_pointer=b['record_pointer']))
            else:b['bounded_absence_basis']=dict(complete_own_report_differences=jr(f'out/readers/024/{role}/report.json','/differences'),complete_own_contexts=[poolref(x) for x in own['complete_own_literal_scope_refs']],exact_source_correspondence=jr('out/checks/scan024_source_row_skeleton_v01.json',f'/rows/{int(d["source_locus_id"].split("L")[1])-1}/readers/{role}'))
        else:
            b['source_only_S_basis']=dict(whole_own_reader_source=sr(f'out/readers/024/{role}/reading.tex',0,len(text(f'out/readers/024/{role}/reading.tex'))),S_scope=jr('out/checks/scan024_S_scope.json',f'/row_scopes/{int(d["id"].split("S")[-1])-1}'))
        bindings.append(b)
for pid in sorted(used-frame_value_ids-set(appendices)):
    value=PROJ['values'][pid]
    kind='editorial_join_separator' if value=='\n\n' else 'bounded_report_absence_statement' if value=='\n\n'+absence else 'source_only_S_reader_scope_statement'
    other[pid]=dict(kind=kind,value=value,expected_sha256_utf8=sha(value),scope_rule='This is explicitly editorial/source-scope wording, not a manuscript quotation. Per-reader source bases are retained in field bindings.')
focus=[]
for key,inv in inventories.items():
    gids=[gid for gid,g in groups.items() if key in g['inventory_clauses']];frames=[x['frame'] for x in frame_entries if x['archive_inventory_clause']==key or any(y['group'] in gids for y in x['group_substitutions'])]
    focus.append(dict(component=key,original_identity=inv['original_identity'],original_hand_source=inv['hand_source'],group_descriptions=gids,frame_ids=frames,public_pool_ids=sorted({pid for f in frame_entries if f['frame'] in frames for pid in f['public_pool_ids']})))
ad29=dict(source_fields=[jr('out/readers/024/A/report.json',p) for p in ['/differences/28/mark_hand','/differences/28/role_confidence','/differences/28/alternatives','/doubts/18/separate_scope']],appendix_pool_ids=[pid for pid,a in appendices.items() if any(files[e['source']['file']]['path']=='out/readers/024/A/report.json' and e['source'].get('json_pointer') in ['/differences/28','/doubts/18'] for e in a['source_entries'])],scope='Exact A-owned candidate-specific hand/role fields; no transfer from reader C.')
plan=dict(scan=24,source_only=True,status='Mapping generated for root independent replay; no replay/test run by source clerk.',projection=dict(path=P,sha256_utf8=sha(text(P))),record=dict(path=RPATH,sha256_utf8=sha(text(RPATH))),existing_frame_projection=dict(path=FP,sha256_utf8=sha(text(FP))),frozen_source_files=files,serialization=dict(ensure_ascii=False,separators=[',',':'],ordered_fields='The listed field order is exact; raw selected field values are loaded from their own original JSON pointers.'),group_description_recipes=groups,existing_frame_bindings=frame_entries,appendix_recipes=appendices,other_chunk_recipes=other,reader_field_bindings=bindings,restored_inventory_clauses=inventories,twelve_inventory_focus=focus,A_D29_focus=ad29,counts=dict(current_reader_fields=len(bindings),unique_referenced_reader_pool_values=len(used),frames=len(frame_entries),group_substitution_occurrences=sum(len(x['group_substitutions']) for x in frame_entries),unique_group_descriptions=len(groups),local_appendices=len(appendices),other_chunks=len(other),restored_inventory_scopes=len(focus)),mapping_issues=issues,role_rule='Every original JSON/text selector retains its reader role. Existing pool equality is only a codec; each field binding keeps the proper role/source basis.',limits='No image access, source mutation, ink/hand/count selection, rendering, compilation, mathematical work, delegation or optional test pass.')
for p in [P,RPATH,FP,'out/checks/scan024_source_build_record.py','out/checks/scan024_root_reader_frame_replay.json']:
    fileid(p)
plan['frozen_source_files']=files
out=D/'scan024_source_reader_binding_plan_v01.json';out.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
lines=[json.dumps(dict(kind='metadata',**{k:v for k,v in plan.items() if k not in ['frozen_source_files','group_description_recipes','existing_frame_bindings','appendix_recipes','other_chunk_recipes','reader_field_bindings','restored_inventory_clauses','twelve_inventory_focus']}),ensure_ascii=False)]
for name in ['frozen_source_files','group_description_recipes','restored_inventory_clauses','appendix_recipes','other_chunk_recipes']:
    lines.extend(json.dumps(dict(kind=name,id=k,value=v),ensure_ascii=False) for k,v in plan[name].items())
for name in ['existing_frame_bindings','reader_field_bindings','twelve_inventory_focus']:
    lines.extend(json.dumps(dict(kind=name,value=v),ensure_ascii=False) for v in plan[name])
(D/'scan024_source_reader_binding_plan_v01.jsonl').write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(path=str(out.relative_to(B)),sha256_utf8=sha(out.read_bytes()),counts=plan['counts'],mapping_issues=issues),indent=2))
