"""Independent read-only approval/public-field replay; writes only postcommit proofs."""
from pathlib import Path
import collections
import copy
import csv
import hashlib
import io
import json
import re
import sys

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out'
CHECKS=OUT/'checks'
P='scan026_release_postcommit_'
csv.field_size_limit(sys.maxsize)
def sha(b):return hashlib.sha256(b).hexdigest()
def enc(v):return (json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
def compact(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def save(name,value):
    assert name.startswith(P)
    b=enc(value);(CHECKS/name).write_bytes(b);return {'path':'out/checks/'+name,'sha256':sha(b),'bytes':len(b)}
def read(path):return json.loads(path.read_bytes())
def escape_pointer(k):return str(k).replace('~','~0').replace('/','~1')
def public_esc(value):
    if value is None:return '—'
    if isinstance(value,(dict,list)):value=json.dumps(value,ensure_ascii=False)
    return str(value).replace('|','\\|').replace('\n','<br>')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(public_esc(x) for x in row)+' |\n' for row in rows)
def field_text(value):return '' if value is None else str(value)
def text_proof(value):
    b=value.encode();return {'utf8_bytes':len(b),'characters':len(value),'sha256':sha(b)}

inputs={}
def captured(path):
    b=path.read_bytes();inputs[str(path.relative_to(BASE))]={'sha256':sha(b),'bytes':len(b)};return b
frozen_path=CHECKS/'scan026_release_record_proposal_v03.json';frozen_bytes=captured(frozen_path);frozen=json.loads(frozen_bytes)
assert sha(frozen_bytes)=='4c9896319b19e1b6adc4a70b93e7ed3a212dc31e26ee0742a6f2de8c151b60f8'
approval_bytes=captured(CHECKS/'scan026_root_approval.json');approval=json.loads(approval_bytes)
fingerprint_bytes=captured(CHECKS/'scan026_reader_fingerprints.json');fingerprints=json.loads(fingerprint_bytes)
fingerprint_files=fingerprints['files'] if 'files' in fingerprints else fingerprints
assert len(fingerprint_files)==107
fingerprint_pairs=[]
for key,value in fingerprint_files.items():
    if isinstance(value,str):path,digest=key,value
    else:path,digest=value['path'],value['sha256']
    assert isinstance(path,str) and isinstance(digest,str) and len(digest)==64
    fingerprint_pairs.append({'path':path,'sha256':digest})
draft_bytes=captured(CHECKS/'scan026_final_draft.tex');page=draft_bytes.decode();page_sha=sha(draft_bytes)
assert page_sha==approval['sha256']=='318b043580aba18b302169e52d7c3570208e8211cc7f32f8828cc070ee743615'
record_bytes=captured(OUT/'records/scan026.json');record=json.loads(record_bytes)
assert captured(OUT/'pages'/frozen['filename'])==draft_bytes
assert captured(CHECKS/'scan026_record_draft.json')==frozen_bytes
approve_code=captured(OUT/'scripts/approve_page.py');builder_code=captured(OUT/'scripts/build_records.py')
crop_audit=json.loads(captured(CHECKS/'scan026_root_crop_audit.json'))
source_audit_bytes=captured(CHECKS/'scan026_source_audit.md')
source_map=json.loads(captured(CHECKS/'scan026_final_source_map.json'))
assert source_map['draft_sha256_utf8']==page_sha

# Reproduce the observed approval mutations without executing the approval script.
expected=copy.deepcopy(frozen);page_ref='pages/'+expected['filename'];bindings=[]
def bind(value,path=''):
    if isinstance(value,dict):
        if value.get('path')=='checks/scan026_final_draft.tex' and 'char_start' in value:
            start,end=value['char_start'],value['char_end'];assert 0<=start<end<=len(page)
            before_keys=list(value);old_manifest=value.get('manifest','root.final_draft.tex')
            value['source_manifest']=value.pop('manifest','root.final_draft.tex')
            value.update(path=page_ref,sha256=page_sha,body_sha256=sha(page[start:end].encode()))
            bindings.append({'record_pointer':path,'char_start':start,'char_end':end,'body_sha256':sha(page[start:end].encode()),'before_keys':before_keys,'after_keys':list(value),'source_manifest':old_manifest})
        for k,child in value.items():bind(child,path+'/'+escape_pointer(k))
    elif isinstance(value,list):
        for i,child in enumerate(value):bind(child,path+'/'+str(i))
bind(expected)
for d in expected['decisions']:
    d['main_approved']=True;d['root_source_attachment_status']='Root approved complete selected-source attachment.'
    d['count_status']='Root approved physical-cluster count; raw reader proposals remain in provenance.'
for item in expected['inventory']:
    item['main_approved']=True;item['selection_status']='Root approved the selected source content.'
    item['hand_status']='root approved; qualified or mixed attribution remains explicit'
for item in expected.get('doubts',[]):item['main_approved']=True
for field in ['selected_graphical_groups','source_locus_coverage','abbreviations']:
    for item in expected.get(field,[]):item['main_approved']=True
for field in ['attributed_content_note','root_selected_content_note']:
    if isinstance(expected.get(field),dict):expected[field]['main_approved']=True
for row in expected.get('C_source_rows',[]):
    for part in row.get('source_parts',[]):
        if 'decision_status' in part:part.setdefault('original_source_decision_status',part['decision_status'])
        part['decision_status']='Root approved the recorded original-doubt outcome.';part['main_approved']=True
now=approval['approved_utc']
expected.update(main_adjudicated=True,main_approved=True,main_approved_utc=now,root_page_text_exact=page,root_actions_pending=[],reader_fingerprints=fingerprints,
    root_approval_status='Root approved the final record and selected text.',count_status='Root approved all C/H physical counts and scalar confidences with the selected record.',root_approved_decision_entries=len(expected['decisions']),
    root_crop_audit='checks/scan026_root_crop_audit.json',root_source_audit='checks/scan026_source_audit.md',
    final_page=dict(path=page_ref,sha256=page_sha,selected_draft='checks/scan026_final_draft.tex',relation='byte-for-byte identical; character offsets preserved'),
    source_attachment_status='Root approved after the targeted source audit; final-page attachments use exact selected-draft offsets.')
c=approval['counts'];expected['counts']=dict(C=c['C'],H=c['H'],decision_loci=c['decision_loci'],remaining_doubt_loci=c['remaining_doubt_loci'],inventory_elements=c['inventory_elements'],check_events=c['check_events'])
assert enc(expected)==record_bytes,'Complete committed record differs from independently reproduced approval projection.'
expected_approval=dict(scan=26,approved_utc=now,page=page_ref,sha256=page_sha,counts=expected['counts'],root_crops=approval['root_crops'],
    C_confidence=dict(collections.Counter(d['confidence'] for d in expected['decisions'] if d['diff_C'])),
    H_confidence=dict(collections.Counter(d['confidence'] for d in expected['decisions'] if d['diff_H'])),
    validation_scope='Root reviewed the selected text, decisions, doubts, inventory and source audit; commit_page.py supplies the required structural gate.',
    source_audit_sha256=sha(source_audit_bytes),reviewed_record_sha256=sha(frozen_bytes))
assert enc(expected_approval)==approval_bytes

def csv_rows(path,delimiter):
    raw=captured(path);text=raw.decode();physical=text.splitlines(keepends=True);starts=[0]
    for line in physical:starts.append(starts[-1]+len(line))
    reader=csv.reader(io.StringIO(text,newline=''),delimiter=delimiter);header=next(reader);header_end=reader.line_num
    rows=[];previous=reader.line_num
    for index,values in enumerate(reader):
        end=reader.line_num;assert len(values)==len(header)
        a,b=starts[previous],starts[end];rows.append({'index':index,'values':dict(zip(header,values)),'raw_text':text[a:b],
             'span':{'char_start':a,'char_end':b,'utf8_byte_start':len(text[:a].encode()),'utf8_byte_end':len(text[:b].encode())}})
        previous=end
    return header,rows,''.join(physical[:header_end]),raw

inventory_header,inventory_all,inventory_header_raw,inventory_bytes=csv_rows(OUT/'SP40_CW_81_inventory.csv',',')
inventory_actual=[x for x in inventory_all if x['values']['scan']=='26'];assert len(inventory_actual)==106
inventory_fields=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'];assert inventory_header==inventory_fields
inventory_proof=[]
for i,(current,actual) in enumerate(zip(record['inventory'],inventory_actual)):
    wanted={'scan':26,**current};field_checks=[]
    for field in inventory_fields:
        expected_text=field_text(wanted[field]);observed=actual['values'][field];assert observed==expected_text,(i,current['element'],field)
        field_checks.append({'public_column':field,'record_pointer':'/scan' if field=='scan' else f'/inventory/{i}/'+field,'exact_complete_text_equal':True,**text_proof(observed)})
    assert current['page_order']==i+1
    inventory_proof.append({'record_index':i,'element':current['element'],'public_csv_row_index':actual['index'],'public_raw_row_span':actual['span'],'full_hand_exact_equal':actual['values']['hand']==current['hand'],'fields':field_checks})
inventory_excerpt=(inventory_header_raw+''.join(x['raw_text'] for x in inventory_actual)).encode()
(CHECKS/(P+'inventory_exact.csv')).write_bytes(inventory_excerpt)

def evidence_text(d):
    evidence=d.get('evidence','')
    if d.get('qualification'):evidence+=' '+d['qualification']
    if d.get('crop'):evidence+=' Image: '+str(d['crop'])+'.'
    if d.get('C_doubt_status'):evidence+=' C doubt: '+d['C_doubt_status']+'.'
    if d.get('S_id'):evidence+=' Witness S '+d['S_id']+': '+d.get('S_status','reviewed')+'.'
    return evidence
collation_header,collation_all,collation_header_raw,collation_bytes=csv_rows(OUT/'SP40_CW_81_collation.tsv','\t')
collation_actual=[x for x in collation_all if x['values']['our_scan']=='26']
H_decisions=[(i,d) for i,d in enumerate(record['decisions']) if d.get('diff_H') and record['hua_has']=='text']
assert len(collation_actual)==len(H_decisions)==82
collation_fields=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'];assert collation_header==collation_fields
collation_proof=[]
for (i,d),actual in zip(H_decisions,collation_actual):
    wanted={'folder':record['folder'],'their_page':record['their_page'],'our_scan':26,'line':d['location'],'their_reading':d.get('H',''),'codex_reading':d.get('C',''),'final_reading':d['final'],'scan_shows':evidence_text(d),'kind':d['kind'],'marked_in_H':d.get('marked_in_H','no'),'confidence':d['confidence']}
    pointers={'folder':'/folder','their_page':'/their_page','our_scan':'/scan','line':f'/decisions/{i}/location','their_reading':f'/decisions/{i}/H','codex_reading':f'/decisions/{i}/C','final_reading':f'/decisions/{i}/final','kind':f'/decisions/{i}/kind','marked_in_H':f'/decisions/{i}/marked_in_H','confidence':f'/decisions/{i}/confidence'}
    field_checks=[]
    for field in collation_fields:
        observed=actual['values'][field];assert observed==field_text(wanted[field]),(d['id'],field)
        field_checks.append({'public_column':field,'record_pointer':pointers.get(field),'derived_constructor':'evidence_text' if field=='scan_shows' else None,'exact_complete_text_equal':True,**text_proof(observed)})
    collation_proof.append({'decision_index':i,'decision_id':d['id'],'public_tsv_row_index':actual['index'],'public_raw_row_span':actual['span'],'complete_final_string_exact_equal':actual['values']['final_reading']==d['final'],'fields':field_checks})
collation_excerpt=(collation_header_raw+''.join(x['raw_text'] for x in collation_actual)).encode()
(CHECKS/(P+'collation_exact.tsv')).write_bytes(collation_excerpt)

changes_bytes=captured(OUT/'SP40_CW_81_changes.md');changes_text=changes_bytes.decode();change_rows=[];change_indices=[]
for i,d in enumerate(record['decisions']):
    readers=d.get('readers',{});reader_text='; '.join(f'{k}: {v}' for k,v in readers.items()) if isinstance(readers,dict) else str(readers)
    if d.get('diff_C') or d.get('diff_H') or d.get('C_doubt_status') or d.get('S_id') or d.get('log_decision'):
        change_rows.append([d['id'],d['location'],d.get('C'),d.get('H'),d['final'],reader_text,evidence_text(d),d['confidence']]);change_indices.append(i)
assert len(change_rows)==len(change_indices)==91
change_headers=['ID','Place','Witness C','Witness H','Final','Three readings','What the scan shows / decision','Confidence']
doubt_headers=['Place','Reading','Alternatives','Confidence','Reason']
doubt_rows=[[d['location'],d['reading'],d.get('alternatives','—'),d['confidence'],d.get('reason','')] for d in record['doubts']]
assert len(doubt_rows)==66
expected_section='\n'.join(['\n## Scan 026\n',table(change_headers,change_rows),'\n### Still unresolved\n',table(doubt_headers,doubt_rows)])+'\n'
section_start=changes_text.index('\n## Scan 026\n');assert changes_text[section_start:]==expected_section
change_proof=[];cursor=section_start+len('\n## Scan 026\n\n')+len('| '+' | '.join(change_headers)+' |\n| '+' | '.join('---' for _ in change_headers)+' |\n')
for index,values in zip(change_indices,change_rows):
    rendered='| '+' | '.join(public_esc(v) for v in values)+' |\n';assert changes_text[cursor:cursor+len(rendered)]==rendered
    checks=[{'column':name,'exact_rendered_complete_field_equal':True,**text_proof(public_esc(value))} for name,value in zip(change_headers,values)]
    change_proof.append({'decision_index':index,'decision_id':record['decisions'][index]['id'],'public_char_start':cursor,'public_char_end':cursor+len(rendered),'fields':checks});cursor+=len(rendered)

doubts_bytes=captured(OUT/'SP40_CW_81_doubts.md');doubts_text=doubts_bytes.decode()
doubt_begin=doubts_text.index('\n## Remaining doubts\n\n')+len('\n## Remaining doubts\n\n')
doubt_end=doubts_text.index('\n## Abbreviations\n\n',doubt_begin)
remaining_text=doubts_text[doubt_begin:doubt_end]
actual_doubt_lines=[line for line in remaining_text.splitlines(keepends=True) if line.startswith('| 026 | ')]
expected_doubt_lines=['| '+' | '.join(public_esc(x) for x in ['026']+row)+' |\n' for row in doubt_rows]
assert actual_doubt_lines==expected_doubt_lines
doubt_proof=[];search_at=doubt_begin
for i,(q,line) in enumerate(zip(record['doubts'],expected_doubt_lines)):
    a=doubts_text.index(line,search_at);search_at=a+len(line)
    doubt_proof.append({'doubt_index':i,'decision_id':q['decision_id'],'record_reading_pointer':f'/doubts/{i}/reading','complete_reading_render_equal':True,'raw_record_reading':text_proof(q['reading']),'public_rendered_reading':text_proof(public_esc(q['reading'])),'public_row_char_start':a,'public_row_char_end':a+len(line),'all_six_public_fields_equal':True})
abbr_begin=doubt_end;abbr_end=doubts_text.index('\n## Legibility and witnesses\n\n',abbr_begin)
actual_abbr=[line for line in doubts_text[abbr_begin:abbr_end].splitlines(keepends=True) if line.startswith('| 26 | ')]
expected_abbr=['| '+' | '.join(public_esc(v) for v in [26,a['form'],a['expansion']])+' |\n' for a in record['abbreviations']]
assert actual_abbr==expected_abbr and len(actual_abbr)==5

notes_text=captured(OUT/'SP40_CW_81_notes.md').decode();notes_section='\n## Scan 026\n\n'+record['notes']+'\n';assert notes_text.endswith(notes_section)
consequence_lines=[f"- Scan 026, {d['location']}: {d['mathematical_consequence']}" for d in record['decisions'] if d.get('mathematical_consequence') and (d.get('diff_C') or d.get('diff_H'))]
assert len(consequence_lines)==14 and all(changes_text.count(line)==1 for line in consequence_lines)
workflow_text=captured(OUT/'SP40_CW_81_workflow.md').decode();workflow_begin=workflow_text.index('## Per-page record\n');workflow_end=workflow_text.index('\n## Brief versions\n',workflow_begin)
reader_crop_counts={role:len(read(OUT/'readers/026'/role/'report.json').get('crops',[])) for role in 'ABC'}
owners=collections.Counter();seen=set()
for entry in crop_audit['viewed_once']:
    if entry['successful_display_count']<=0:continue
    path=entry['path']
    if path in seen:continue
    seen.add(path);owners['root' if path.startswith(('crops/026/','crops/scan026_')) else path.split('/')[2]]+=1
basis=f'Formal audit: checks/scan026_root_crop_audit.json; viewed_once successful paths; reused A {owners["A"]}, B {owners["B"]}, C {owners["C"]}.'
workflow_values=[26,record.get('brief_version','v01'),reader_crop_counts['A'],reader_crop_counts['B'],reader_crop_counts['C'],len(seen),owners['root'],sum(owners[r] for r in 'ABC'),basis,record.get('workflow_note','')]
workflow_row='| '+' | '.join(public_esc(x) for x in workflow_values)+' |\n'
assert workflow_text[workflow_begin:workflow_end].count(workflow_row)==1

# Scan026 contributes no page event rows. Verify the actual event table against
# the current record/global input values without running or writing the builder.
assert record['check_events']==[]
event_rows=[]
for path in sorted((OUT/'records').glob('scan*.json')):event_rows.extend(read(path).get('check_events',[]))
global_path=CHECKS/'global_check_events.json'
if global_path.exists():event_rows.extend(json.loads(captured(global_path)))
event_fields=['statement_id','date','who','type','outcome'];stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=event_fields,delimiter='\t',extrasaction='ignore');writer.writeheader();writer.writerows(event_rows)
actual_events=captured(OUT/'CHECK_EVENTS.tsv');assert stream.getvalue().encode()==actual_events

for path,snapshot in inputs.items():assert sha((BASE/path).read_bytes())==snapshot['sha256'],('input changed during verification',path)
binding_file=save(P+'approval_binding_maps.json',{'source_bindings':bindings,'approval_timestamp_exact':now,'fingerprint_manifest_pairs':fingerprint_pairs,'fingerprint_manifest_exact_in_record':compact(record['reader_fingerprints'])==compact(fingerprints)})
field_file=save(P+'public_field_maps.json',{'csv_serialization_rule':'None becomes the empty string; every other value uses str(value), exactly as csv.DictWriter in the reviewed builder. Hand/final strings are compared in their entirety.','markdown_serialization_rule':'None→em dash; dict/list→json.dumps(ensure_ascii=False); then str, every pipe→backslash-pipe and newline→<br>.','inventory':inventory_proof,'H_collation':collation_proof,'changes':change_proof,'doubts':doubt_proof})
proof=save(P+'proof.json',{
    'scope':'Read-only independent approval and public-field verification; no approval, commit, builder, validator or image operation executed.',
    'approved_record':{'path':'out/records/scan026.json','sha256':sha(record_bytes),'bytes':len(record_bytes)},
    'frozen_proposal_sha256':sha(frozen_bytes),'approval_timestamp_exact':now,'complete_approved_record_byte_replay':True,'complete_approval_JSON_byte_replay':True,
    'fingerprint_manifest_pairs':len(fingerprint_pairs),'fingerprint_manifest_exact_key_order_and_values_in_record':compact(record['reader_fingerprints'])==compact(fingerprints),
    'source_binding_count':len(bindings),'source_binding_maps':binding_file,
    'inventory_rows':len(inventory_proof),'inventory_current_order_exact':True,'all_inventory_public_fields_exact':True,'all_106_complete_hand_strings_exact':True,
    'H_collation_rows':len(collation_proof),'all_H_public_fields_exact':True,'all_82_complete_final_strings_exact':True,
    'changes_decision_entries':len(change_proof),'all_91_full_changes_rows_exact':True,'complete_scan026_changes_section_exact':True,
    'doubt_rows':len(doubt_proof),'all_66_full_doubt_readings_and_fields_exact':True,'abbreviation_rows':len(actual_abbr),'all_abbreviation_fields_exact':True,
    'notes_exact':True,'consequential_lines_exact':len(consequence_lines),'workflow_all_10_fields_exact':True,'page_check_events':0,'complete_current_CHECK_EVENTS_TSV_exact':True,
    'inventory_exact_source_excerpt':{'path':'out/checks/'+P+'inventory_exact.csv','sha256':sha(inventory_excerpt),'bytes':len(inventory_excerpt)},
    'collation_exact_source_excerpt':{'path':'out/checks/'+P+'collation_exact.tsv','sha256':sha(collation_excerpt),'bytes':len(collation_excerpt)},
    'public_field_maps':field_file,'observed_input_fingerprints':inputs,'all_observed_inputs_stable':True,'concrete_defects':[],
})
print(json.dumps({'proof':proof,'record_sha256':sha(record_bytes),'bindings':len(bindings),'inventory':len(inventory_proof),'H_collation':len(collation_proof),'changes':len(change_proof),'doubts':len(doubt_proof),'concrete_defects':[]},ensure_ascii=False))
