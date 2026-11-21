"""Source-only finalization readiness. Writes only final_readiness026_*.

No builder, validator, approval, commit or finalization script is executed,
imported or compiled. No image bytes are read. Proposal replay stays in memory.
"""
from __future__ import annotations
import collections
import copy
import csv
import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out'
EXPECTED = [2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
CACHE = {}

def sha(data): return hashlib.sha256(data).hexdigest()
def read(path):
    path = str(path)
    assert Path(path).suffix.lower() not in {'.png','.jpg','.jpeg','.webp','.gif','.pdf','.zip'}
    if path not in CACHE: CACHE[path] = (BASE/path).read_bytes()
    return CACHE[path]
def txt(path): return read(path).decode('utf-8')
def obj(path): return json.loads(read(path))
def meta(path):
    data = read(path)
    return {'path':str(path),'bytes':len(data),'sha256':sha(data)}
def jsonbytes(value): return (json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
def get(doc, pointer):
    for bit in pointer.split('/')[1:]:
        bit = bit.replace('~1','/').replace('~0','~')
        doc = doc[int(bit)] if isinstance(doc,list) else doc[bit]
    return doc
def replace(doc, pointer, value):
    bits = pointer.split('/')[1:]
    for bit in bits[:-1]:
        bit = bit.replace('~1','/').replace('~0','~')
        doc = doc[int(bit)] if isinstance(doc,list) else doc[bit]
    key = bits[-1].replace('~1','/').replace('~0','~')
    doc[int(key) if isinstance(doc,list) else key] = copy.deepcopy(value)
def patch(doc, operations):
    result = copy.deepcopy(doc)
    for op in operations:
        assert op['op'] in ('test','replace')
        if op['op']=='test': assert get(result,op['path'])==op['value'],op['path']
        else: replace(result,op['path'],op['value'])
    return result
def differences(a,b,path=''):
    if type(a) is not type(b): return [path]
    if isinstance(a,dict):
        if list(a)!=list(b): return [path]
        return [p for key in a for p in differences(a[key],b[key],path+'/'+key.replace('~','~0').replace('/','~1'))]
    if isinstance(a,list):
        if len(a)!=len(b): return [path]
        return [p for index,(x,y) in enumerate(zip(a,b)) for p in differences(x,y,path+'/'+str(index))]
    return [] if a==b else [path]

scripts = [meta('out/scripts/'+name+'.py') for name in ('finalize','validate','build_records','approve_page','commit_page')]
progress = txt('out/progress.log')
record_paths = [str(path.relative_to(BASE)) for path in sorted((OUT/'records').glob('scan*.json'))]
records = [obj(path) for path in record_paths]
scans = [record['scan'] for record in records]
assert scans==EXPECTED[:-1],scans

# Independent literal implementation of the inspected structural gate.
def uncomment(text): return '\n'.join(re.split(r'(?<!\\)%',line,maxsplit=1)[0] for line in text.splitlines())
def structure(text):
    source = uncomment(text)
    errors=[]; depth=0
    for match in re.finditer(r'\\.|[{}]',source):
        token=match.group()
        if token=='{': depth+=1
        elif token=='}':
            depth-=1
            if depth<0: errors.append('unmatched closing brace');depth=0
    if depth: errors.append('unclosed braces: '+str(depth))
    stack=[]
    for match in re.finditer(r'\\(begin|end)\{([^}]+)\}',source):
        kind,name=match.groups()
        if kind=='begin': stack.append(name)
        elif not stack or stack.pop()!=name: errors.append('environment mismatch at '+match.group())
    if stack: errors.append('unclosed environments '+repr(stack))
    for left,right in [('\\[','\\]'),('\\(','\\)')]:
        sequence=[token for token in re.findall(r'\\(?:[A-Za-z]+|.)',source) if token in (left,right)]
        depth=0
        for token in sequence:
            depth+=1 if token==left else -1
            if depth<0: errors.append('math delimiter order '+left);depth=0
        if depth: errors.append('math delimiters '+left)
    if len(re.findall(r'(?<!\\)\$',source))%2: errors.append('odd dollar count')
    forbidden=re.findall(r'\\(?:documentclass|usepackage|newcommand|renewcommand|input|include|includegraphics)\b',source)
    if forbidden: errors.append('non-fragment commands '+repr(forbidden))
    return errors

inventory_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
collation_kinds={'misread word','misread symbol or index','omission','text not on the page',
    'deletion state (struck given live or live given struck)','insertion or placement',
    'abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
pages=[]; readers=[]; record_checks=[]; issues=[]
for path,record in zip(record_paths,records):
    n=record['scan']; page='out/pages/'+record['filename']; text=txt(page); local=[]
    if record.get('main_adjudicated') is not True: local.append('main_adjudicated is not true')
    done=[line for line in progress.splitlines() if line.startswith(f'scan {n:03d} done ')]
    if len(done)!=1: local.append('completion line count '+str(len(done)))
    errors=structure(text)
    if errors: local.extend(errors)
    ids=[entry['id'] for entry in record['decisions']]
    if len(ids)!=len(set(ids)): local.append('duplicate decision IDs')
    for entry in record['inventory']:
        if entry['transcribed']!='yes' or entry['kind'] not in inventory_kinds: local.append('inventory gate failure')
    for entry in record['decisions']:
        if set(entry['readers'])!={'A','B','C'}: local.append('reader alternatives gate '+entry['id'])
        if entry['kind'] not in collation_kinds: local.append('collation kind '+entry['id'])
        if entry['confidence'] not in {'high','medium','low'}: local.append('confidence '+entry['id'])
        if entry.get('C_doubt_status') not in {None,'resolved','retained'}: local.append('C doubt status '+entry['id'])
        if entry.get('diff_H') and record['hua_has']!='text': local.append('H row without H text '+entry['id'])
    for entry in record['doubts']:
        if not all(key in entry for key in ('location','reading','confidence')): local.append('doubt gate failure')
    for entry in record.get('abbreviations',[]):
        if not all(key in entry for key in ('form','expansion')): local.append('abbreviation gate failure')
    if record.get('root_page_text_exact') is not None and text!=record['root_page_text_exact']:
        local.append('root_page_text_exact mismatch')
    final=record.get('final_page')
    if isinstance(final,dict) and 'sha256' in final and final['sha256']!=sha(read(page)):
        local.append('final_page sha256 mismatch')
    current_counts={'C':sum(bool(d.get('diff_C')) for d in record['decisions']),
                    'H':sum(bool(d.get('diff_H')) for d in record['decisions']),
                    'decision_loci':len(record['decisions']), 'remaining_doubt_loci':len(record['doubts']),
                    'inventory_elements':len(record['inventory']), 'check_events':len(record.get('check_events',[]))}
    for key,value in record.get('counts',{}).items():
        if key in current_counts and value!=current_counts[key]:local.append('stored count mismatch '+key)
    for role in 'ABC':
        directory=f'out/readers/{n:03d}/{role}'
        report=obj(directory+'/report.json')
        files=[meta(directory+'/report.json'),meta(directory+'/reading.tex')]
        if (BASE/(directory+'/reading.md')).exists():files.append(meta(directory+'/reading.md'))
        attested=all(report.get(key) for key in ('full_image_viewed','halves_viewed','complete_visual_read'))
        if not attested:local.append('reader completeness attestation '+role)
        readers.append({'scan':n,'role':role,'complete_attestation':attested,'files':files})
    pages.append(meta(page))
    record_checks.append({'scan':n,'record':meta(path),'page':meta(page),'completion_lines':done,
                          'main_adjudicated':record.get('main_adjudicated'),'counts':current_counts,'issues':local})
    issues.extend({'scan':n,'issue':item} for item in local)

combined='out/SP40_CW_81_transcription.tex'
target='\n'.join(txt(page['path']).rstrip()+'\n' for page in pages).encode('utf-8')
combined_checks={'file':meta(combined),'exact_page_concatenation':read(combined)==target,
    'expected_concatenation_sha256':sha(target),'structural_errors':structure(txt(combined)),
    'cote_marker_count':len(re.findall(r'\\cotefile\{81\}',uncomment(txt(combined)))),
    'scan_markers':[int(n) for n in re.findall(r'\\scanpage\{(\d+)\}',uncomment(txt(combined)))]}
assert combined_checks['scan_markers']==scans
cached_validation=obj('out/checks/structural_validation.json')

# NREV exact guarded JSON-patch replay and every supplied source/span binding.
nrev_path='out/checks/notation_NREV01_NREV02_public_report_proposal_v01.json'
nrev=obj(nrev_path)
assert sha(read(nrev_path))=='499af7497dbe39609400f3ea6d2cb62a6d3ff090e1cff906868065c387c446ce'
nrev_sources=[]
for key in ('source_preparation','historical_map_dependency'):
    item=nrev[key]; actual=meta(item['path']); assert actual['sha256']==item['sha256_utf8'];nrev_sources.append(actual)
for item in nrev['page_invariants']:
    actual=meta(item['path']);assert actual['sha256']==item['sha256_utf8'];nrev_sources.append(actual)
span_checks=[]
for catalog_name in ('root_authority_catalog','selected_source_catalog'):
    for identifier,item in nrev[catalog_name].items():
        data=read(item['path']); text=data.decode('utf-8')
        assert sha(data)==item['file_sha256_utf8'],identifier
        fragment=text[item['char_start_zero_based']:item['char_end_exclusive']]
        supplied_literal = item['literal'] if 'literal' in item else get(obj(item['record_binding_path']),item['record_binding_json_pointer'])
        assert fragment==supplied_literal,identifier
        assert data[item['utf8_byte_start']:item['utf8_byte_end_exclusive']]==fragment.encode('utf-8'),identifier
        assert sha(fragment.encode('utf-8'))==item['span_sha256_utf8'],identifier
        span_checks.append({'catalog':catalog_name,'id':identifier,'path':item['path'],
                            'file_sha256':sha(data),'span_sha256':item['span_sha256_utf8'],
                            'char_start':item['char_start_zero_based'],'char_end':item['char_end_exclusive'],
                            'exact_char_byte_literal_hash_match':True})
nrev_replays=[]; nrev_mapping=[]
for plan in nrev['record_patches']:
    raw=read(plan['path']); before=json.loads(raw);assert sha(raw)==plan['before_sha256_utf8']
    assert jsonbytes(before)==raw
    after=patch(before,plan['forward_json_patch']); after_bytes=jsonbytes(after)
    inverse=patch(after,plan['inverse_json_patch']); inverse_bytes=jsonbytes(inverse)
    assert sha(after_bytes)==plan['proposed_after_sha256_utf8']
    assert inverse_bytes==raw
    changed=differences(before,after)
    allowed=[operation['path'] for operation in plan['forward_json_patch'] if operation['op']=='replace']
    assert set(changed)==set(allowed) and len(changed)==plan['replacement_count']
    for locus_index,locus in enumerate(nrev['loci']):
        if locus['record_path']!=plan['path']:continue
        for pointer in (locus['decision_final_pointer'],locus['doubt_reading_pointer']):
            assert get(before,pointer)==locus['before']
            assert get(after,pointer)==locus['proposed_after']
            nrev_mapping.append({'proposal_locus_pointer':'/loci/'+str(locus_index),
                'decision_id':locus['decision_id'],'record_path':plan['path'],'target_pointer':pointer,
                'exact_old_value':locus['before'],'exact_new_value':locus['proposed_after'],
                'root_authority_id':locus['root_authority_id']})
        decision=get(before,locus['decision_final_pointer'].rsplit('/',1)[0])
        for key,value in locus['preserved_local_fields'].items():assert decision.get(key)==value,(locus['decision_id'],key)
    nrev_replays.append({'path':plan['path'],'before_sha256':sha(raw),'proposed_after_sha256':sha(after_bytes),
                         'replacement_count':len(changed),'exact_changed_pointers':changed,
                         'forward_after_hash_matches':True,'inverse_original_bytes_exact':True})
assert len(nrev_mapping)==40
dependency=obj(nrev['historical_map_dependency']['path'])
historical=dependency['historical_scan018_map']; hmap=obj(historical['path'])
assert sha(read(historical['path']))==historical['sha256_utf8']
assert get(hmap,historical['snapshot_reading_json_pointer'])==historical['snapshot_reading_verbatim']
def scalar_paths(value, predicate, path=''):
    if isinstance(value,dict):return [p for key,item in value.items() for p in scalar_paths(item,predicate,path+'/'+key.replace('~','~0').replace('/','~1'))]
    if isinstance(value,list):return [p for index,item in enumerate(value) for p in scalar_paths(item,predicate,path+'/'+str(index))]
    return [path] if predicate(value) else []
equal_digest_paths=scalar_paths(obj('out/records/scan018.json'),lambda value:value==historical['sha256_utf8'])
assert len(equal_digest_paths)==historical['existing_record_equal_digest_leaf_count']==263
assert sha(read(dependency['scan021_map']['path']))==dependency['scan021_map']['sha256_utf8']

# Workflow exact replacement replay. Proposed code remains inert text.
wf_dir='out/checks/wf_root_crop_counts_through025_proposal/'
wf_forward=obj(wf_dir+'forward.patch.json');wf_inverse=obj(wf_dir+'inverse.patch.json')
wf_raw=read(wf_forward['target']);wf_text=wf_raw.decode('utf-8')
assert sha(wf_raw)==wf_forward['expected_file_sha256']
assert wf_text.count(wf_forward['old_text'])==wf_forward['expected_occurrences']==1
wf_after=wf_text.replace(wf_forward['old_text'],wf_forward['new_text'],1).encode('utf-8')
assert sha(wf_after)==wf_forward['result_file_sha256']
assert wf_after==read(wf_dir+'build_records.proposed.py')
assert wf_raw==read(wf_dir+'build_records.before.py')
assert sha(wf_after)==wf_inverse['expected_file_sha256']
assert wf_after.decode('utf-8').count(wf_inverse['old_text'])==wf_inverse['expected_occurrences']==1
wf_back=wf_after.decode('utf-8').replace(wf_inverse['old_text'],wf_inverse['new_text'],1).encode('utf-8')
assert wf_back==wf_raw and sha(wf_back)==wf_inverse['result_file_sha256']
start=wf_text.index(wf_forward['old_text']);end=start+len(wf_forward['old_text'])
new_end=start+len(wf_forward['new_text'])
assert wf_text[:start]==wf_after.decode('utf-8')[:start]
assert wf_text[end:]==wf_after.decode('utf-8')[new_end:]
wf_evidence=obj(wf_dir+'evidence.json');source_bindings=[]
def check_source_metadata(value,path=''):
    if isinstance(value,dict):
        if isinstance(value.get('path'),str) and isinstance(value.get('sha256'),str):
            actual=meta(value['path']);source_bindings.append({'evidence_pointer':path,'path':value['path'],
                'expected_sha256':value['sha256'],'current_sha256':actual['sha256'],
                'exact_hash_match':actual['sha256']==value['sha256'],
                'expected_bytes':value.get('bytes'),'current_bytes':actual['bytes']})
        for key,item in value.items():check_source_metadata(item,path+'/'+key)
    elif isinstance(value,list):
        for index,item in enumerate(value):check_source_metadata(item,path+'/'+str(index))
check_source_metadata(wf_evidence)
formal=[]
def owner(scan,path):
    if path.startswith(f'crops/{scan:03d}/') or path.startswith(f'crops/scan{scan:03d}_'):return 'root'
    if path.startswith(f'readers/{scan:03d}/') and path.split('/')[2] in 'ABC':return path.split('/')[2]
    raise AssertionError(path)
for page in wf_evidence['formal_pages']:
    audit=obj(page['audit_source']['path']); scan=page['scan'];assert audit['scan']==scan
    fields=[key for key in ('images','viewed_once') if key in audit];assert fields==[page['success_array']]
    selected=[(index,row) for index,row in enumerate(audit[fields[0]]) if row['successful_display_count']>0]
    seen={};eligible=[]
    for index,row in selected:
        crop=row['path'];who=owner(scan,crop)
        assert type(row['successful_display_count']) is int and row['successful_display_count']==1
        if 'created_by_root' in row:assert type(row['created_by_root']) is bool and row['created_by_root']==(who=='root')
        identity=(row.get('sha256'),who)
        if crop in seen:assert seen[crop]==identity
        seen[crop]=identity
        eligible.append({'json_pointer':f'/{fields[0]}/{index}','path':crop,'recorded_sha256':row.get('sha256'),
             'successful_display_count':row['successful_display_count'],'owner_from_exact_path':who,
             'created_by_root':row.get('created_by_root'),'decision_sections':row.get('decision_sections')})
    assert eligible==page['eligible_rows']
    totals=collections.Counter(who for _,who in seen.values())
    count={'total':len(seen),'root_created':totals['root'],'reused':sum(totals[role] for role in 'ABC'),
           'reused_by_role':{role:totals[role] for role in 'ABC'}}
    assert count==page['counts']
    for key in ('total_distinct','successful_distinct_crops'):
        if key in audit:assert audit[key]==len(seen)
    for key,value in page.get('excluded_failure_records',{}).items():assert audit[key]==value
    formal.append({'scan':scan,'audit':meta(page['audit_source']['path']),'success_array':fields[0],
                   'counts':count,'eligible_paths_exact':True,'failure_records_preserved_exact':True})
historical_checks=[]
for page in wf_evidence['earlier_pages']:
    scan=page['scan'];record=obj(page['record_source']['path'])
    record_value=get(record,page['record_selector'])
    assert record_value.count(page['exact_record_excerpt'])==1
    excerpt_start=record_value.index(page['exact_record_excerpt'])
    if 'journal_source' in page:
        lines=txt(page['journal_source']['path']).splitlines()
        for line in page.get('historical_display_failure_lines',[]):assert lines[line['line']-1]==line['text']
    enumeration=page.get('historical_path_enumeration',page.get('root_created_path_enumeration'))
    result={'scan':scan,'counts':page['counts'],'exact_record_excerpt_matches':True,
            'record_excerpt_character_start':excerpt_start,
            'record_excerpt_character_end':excerpt_start+len(page['exact_record_excerpt']),
            'evidence_basis':page['basis'],'enumeration_selector':page.get('enumeration_selector')}
    if enumeration:
        paths=enumeration['exact_paths'];assert len(paths)==len(set(paths))
        counts=collections.Counter(owner(scan,path) for path in paths)
        assert len(paths)==enumeration['total'] and counts['root']==enumeration['root_created']
        assert sum(counts[role] for role in 'ABC')==enumeration['reused']
        assert {role:counts[role] for role in 'ABC'}==enumeration['reused_by_role']
        result.update({'enumerated_paths':len(paths),'path_owner_counts_exact':True})
    historical_checks.append(result)

def csv_bytes(fields,rows,delimiter):
    stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=fields,delimiter=delimiter,extrasaction='ignore')
    writer.writeheader();writer.writerows(rows);return stream.getvalue().encode('utf-8')
events=[event for record in records for event in record.get('check_events',[])]+obj('out/checks/global_check_events.json')
event_fields=['statement_id','date','who','type','outcome']
events_expected=csv_bytes(event_fields,events,'\t')
events_current=list(csv.DictReader(io.StringIO(txt('out/CHECK_EVENTS.tsv')),delimiter='\t'))
expected_ids=[event.get('statement_id','') for event in events];current_ids=[event['statement_id'] for event in events_current]
incomplete_public_event_rows=[]
public_event_index=0
for record,path in zip(records,record_paths):
    for index,event in enumerate(record.get('check_events',[])):
        missing=[field for field in event_fields if field not in event]
        if missing:
            emitted={field:event.get(field,'') for field in event_fields}
            incomplete_public_event_rows.append({'record_path':path,'record_sha256':sha(read(path)),
                'record_pointer':'/check_events/'+str(index),'emitted_zero_based_data_row':public_event_index,
                'missing_public_keys':missing,'source_id':event.get('id'),'source_actor':event.get('actor'),
                'source_keys':list(event),'exact_emitted_public_fields':emitted,
                'current_tsv_row':events_current[public_event_index],
                'current_tsv_row_matches_exact_projection':events_current[public_event_index]==emitted,
                'source_coordinate_or_result_values_recalculated':False})
        public_event_index+=1
inventory=[{'scan':record['scan'],**item} for record in records for item in record['inventory']]
inventory_fields=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
inventory_expected=csv_bytes(inventory_fields,inventory,',')
collation=[]
for record in records:
    for decision in record['decisions']:
        if not decision.get('diff_H') or record['hua_has']!='text':continue
        evidence=decision.get('evidence','')
        if decision.get('qualification'):evidence+=' '+decision['qualification']
        if decision.get('crop'):evidence+=' Image: '+str(decision['crop'])+'.'
        if decision.get('C_doubt_status'):evidence+=' C doubt: '+decision['C_doubt_status']+'.'
        if decision.get('S_id'):evidence+=' Witness S '+decision['S_id']+': '+decision.get('S_status','reviewed')+'.'
        collation.append({'folder':record['folder'],'their_page':record['their_page'],'our_scan':record['scan'],
            'line':decision['location'],'their_reading':decision.get('H',''),'codex_reading':decision.get('C',''),
            'final_reading':decision['final'],'scan_shows':evidence,'kind':decision['kind'],
            'marked_in_H':decision.get('marked_in_H','no'),'confidence':decision['confidence']})
collation_fields=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
collation_expected=csv_bytes(collation_fields,collation,'\t')
required=['SP40_CW_81_transcription.tex','SP40_CW_81_changes.md','SP40_CW_81_collation.tsv',
          'SP40_CW_81_doubts.md','SP40_CW_81_inventory.csv','SP40_CW_81_notes.md',
          'progress.log','SP40_CW_81_workflow.md','CHECK_EVENTS.tsv']
required_files=[meta('out/'+name) for name in required]
missing026=[path for path in [
    'out/checks/scan026_record_draft.json','out/checks/scan026_reader_fingerprints.json',
    'out/checks/scan026_root_crop_audit.json','out/checks/scan026_source_audit.md',
    'out/checks/scan026_final_draft.tex','out/checks/scan026_final_source_map.json',
    'out/checks/scan026_root_approval.json','out/records/scan026.json'] if not (BASE/path).exists()]
reader026=[]
for role in 'ABC':
    directory=f'out/readers/026/{role}';report=obj(directory+'/report.json')
    reader026.append({'role':role,'complete_attestation':all(report.get(key) for key in ('full_image_viewed','halves_viewed','complete_visual_read')),
                      'files':[meta(directory+'/'+name) for name in ('reading.tex','reading.md','report.json')]})

report={
    'checked_utc':datetime.now(timezone.utc).isoformat(),
    'scope':'Source-only readiness through025. No proposal applied, root approval supplied, image read, source script executed, compilation, rendering, event/history/progress edit, freeze, archive or upload.',
    'scripts':scripts,
    'through025':{'scan_sequence':scans,'expected_sequence':EXPECTED[:-1],'record_checks':record_checks,
        'reader_returns':readers,'gate_issues':issues,'combined':combined_checks,
        'cached_structural_validation':{'file':meta('out/checks/structural_validation.json'),
             'complete_scans':cached_validation['complete_scans'],'tex_ok':cached_validation['tex_ok'],
             'record_issues':cached_validation['record_issues'],'matches_current_scan_sequence':cached_validation['complete_scans']==scans},
        'current_structural_gate_incomplete_issue':'Only 23 of 24 scans complete'},
    'nrev':{'proposal':meta(nrev_path),'status':nrev['status'],'applied':nrev['applied'],
        'record_replays':nrev_replays,'exact_allowed_field_mapping':nrev_mapping,
        'source_bindings':nrev_sources,'catalog_span_checks':span_checks,
        'historical_scan018_map':meta(historical['path']),'historical_map_digest_reference_count':len(equal_digest_paths),
        'historical_map_digest_reference_paths':equal_digest_paths,
        'historical_map_preserved':True,'new_ink_decisions':0},
    'workflow_proposal':{'files':[meta(wf_dir+name) for name in ['proposal.md','preview.md','evidence.json','forward.diff','inverse.diff','forward.patch.json','inverse.patch.json','build_records.before.py','build_records.proposed.py','source_replay.json']],
        'target':meta(wf_forward['target']),'expected_before_sha256':wf_forward['expected_file_sha256'],
        'expected_after_sha256':wf_forward['result_file_sha256'],'exact_forward_to_proposed_bytes':True,'exact_inverse_to_original_bytes':True,
        'bounded_character_mapping':{'old_start':start,'old_end':end,'new_start':start,'new_end':new_end,
            'identical_prefix_characters':start,'identical_suffix_characters':len(wf_text)-end},
        'source_metadata_checks':source_bindings,'formal_pages':formal,'historical_pages':historical_checks,
        'formal_totals':{key:sum(page['counts'][key] for page in formal) for key in ('total','root_created','reused')},
        'source_only_inconsistency':{'pointer':'/earlier_pages/2/enumeration_selector',
            'actual_value':wf_evidence['earlier_pages'][2]['enumeration_selector'],
            'row_scan':wf_evidence['earlier_pages'][2]['scan'],
            'actual_row_journal':wf_evidence['earlier_pages'][2]['journal_source']['path'],
            'actual_row_failure_line_numbers':[item['line'] for item in wf_evidence['earlier_pages'][2]['historical_display_failure_lines']],
            'description':'The scan004 evidence-row selector mentions scan003 journal line31. Its own source metadata and failure excerpt point to scan004 journal line3. The proposed builder fallback for scan004 already points to scan004 line3.'}},
    'cumulative_source_checks':{
        'required_archive_files':required_files,
        'inventory_csv_exact_from_current_records':read('out/SP40_CW_81_inventory.csv')==inventory_expected,
        'inventory_rows':len(inventory),
        'collation_tsv_exact_from_current_records':read('out/SP40_CW_81_collation.tsv')==collation_expected,
        'collation_rows':len(collation),
        'check_events_tsv_exact_from_current_inputs':read('out/CHECK_EVENTS.tsv')==events_expected,
        'current_check_events_rows':len(events_current),'current_input_check_events_rows':len(events),
        'missing_event_ids':[identifier for identifier in expected_ids if identifier not in current_ids],
        'unexpected_event_ids':[identifier for identifier in current_ids if identifier not in expected_ids],
        'expected_events_sha256_from_current_inputs':sha(events_expected),
        'incomplete_public_event_rows':incomplete_public_event_rows,
        'global_events_file':meta('out/checks/global_check_events.json')},
    'remaining026':{'missing_paths_at_check':missing026,'reader_returns':reader026,
        'completion_line_present':'scan 026 done ' in progress,
        'freeze_manifest_exists':(OUT/'freeze_manifest.json').exists(),
        'final_zip_exists':(BASE/'SP40_CW_81.zip').exists(),
        'counts_and_selected_draft_hash_available':(OUT/'checks/scan026_record_draft.json').exists() and (OUT/'checks/scan026_final_draft.tex').exists()},
    'source_read_manifest':[meta(path) for path in sorted(CACHE)],
}
changed_during_read=[]
for path,data in CACHE.items():
    if (BASE/path).read_bytes()!=data:changed_during_read.append(path)
report['source_inputs_changed_during_check']=changed_during_read
result=OUT/'checks/final_readiness026_audit.json'
result.write_bytes(jsonbytes(report))
print(json.dumps({'audit_path':str(result.relative_to(BASE)),'audit_sha256':sha(result.read_bytes()),
    'current_scans':scans,'gate_issues':issues,'combined':combined_checks,
    'nrev_replays':nrev_replays,'workflow_source_mismatches':[entry for entry in source_bindings if not entry['exact_hash_match']],
    'formal_counts':report['workflow_proposal']['formal_totals'],
    'cumulative_checks':{key:value for key,value in report['cumulative_source_checks'].items() if key not in ['required_archive_files']},
    'remaining026':{key:value for key,value in report['remaining026'].items() if key!='reader_returns'},
    'source_inputs_changed_during_check':changed_during_read},ensure_ascii=False,indent=2))
