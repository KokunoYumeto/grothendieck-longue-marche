"""Prepare exact documented-status validator proposal; change no target."""
import copy
import difflib
import hashlib
import json
from pathlib import Path

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
PREFIX='final_readiness026_'
sha=lambda data:hashlib.sha256(data).hexdigest()
encode=lambda value:(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode('utf-8')

def write(name,data):
    assert name.startswith(PREFIX)
    path=OUT/name;path.write_bytes(data)
    return {'path':str(path.relative_to(BASE)),'sha256':sha(data),'bytes':len(data)}
def get(doc,pointer):
    for key in pointer.split('/')[1:]:
        key=key.replace('~1','/').replace('~0','~')
        doc=doc[int(key)] if isinstance(doc,list) else doc[key]
    return doc
def escaped(key):return str(key).replace('~','~0').replace('/','~1')

record_bytes={scan:(BASE/f'out/records/scan{scan:03d}.json').read_bytes() for scan in [15,16,17,24]}
records={scan:json.loads(data) for scan,data in record_bytes.items()}
guard_pool={};source_rows=[];cases=[];case_evidence=[];source_files={}

for scan,record in records.items():
    row_array='C_source_rows' if scan==24 else 'actual_C_doubt_map'
    row_identity='source_id' if scan==24 else 'source_row'
    decision_field='C_source_row_ids' if scan==24 else 'source_C_doubt_rows'
    source_map={row[row_identity]:(index,row) for index,row in enumerate(record[row_array])}
    needed={identity for decision in record['decisions']
            if decision.get('C_doubt_status') not in {None,'resolved','retained'}
            for identity in decision[decision_field]}
    source_guard_ids={}
    for identity in sorted(needed,key=str):
        index,row=source_map[identity];pointer='/'+row_array+'/'+str(index)
        guard_id=f'{scan:03d}:{identity}';source_guard_ids[identity]=guard_id
        guard_keys=(['source_id','source_path','line','char_start','char_end','literal','selected_outcome','decision_ids']
                    if scan==24 else ['source_row','source_line','source_manifest','source_literal','decision_ids',
                    'primary_local_decision_ids','component_decision_ids','local_status_decision_ids','local_statuses','local_component_statuses'])
        guards=[[pointer+'/'+escaped(key),copy.deepcopy(row[key])] for key in guard_keys if key in row]
        if scan==24:
            packet_path=row['source_path'];packet=(BASE/packet_path).read_bytes();packet_text=packet.decode('utf-8')
            literal=row['literal'];assert packet_text[row['char_start']:row['char_end']]==literal
            assert packet_text.splitlines()[row['line']-1]==literal
            source_span={'line':row['line'],'char_start':row['char_start'],'char_end':row['char_end']}
            for part_index,part in enumerate(row['source_parts']):
                for key in ('part_id','selected_outcome','decision_ids'):
                    guards.append([pointer+'/source_parts/'+str(part_index)+'/'+key,copy.deepcopy(part[key])])
        else:
            fingerprints=json.loads((BASE/'out'/record['source_manifest']).read_bytes())
            packet_meta=fingerprints['files'][row['source_manifest']]
            packet_path=packet_meta['path'];packet=(BASE/packet_path).read_bytes()
            assert sha(packet)==packet_meta['sha256']
            packet_text=packet.decode('utf-8');literal=packet_text.splitlines()[row['source_line']-1]
            if 'source_literal' in row:assert row['source_literal']==literal
            char_start=sum(len(line) for line in packet_text.splitlines(keepends=True)[:row['source_line']-1])
            source_span={'line':row['source_line'],'char_start':char_start,'char_end':char_start+len(literal)}
            assert packet_text[source_span['char_start']:source_span['char_end']]==literal
        source_files[packet_path]={'path':packet_path,'sha256':sha(packet),'bytes':len(packet)}
        guard_pool[guard_id]=guards
        source_rows.append({'guard_id':guard_id,'scan':scan,'record_row_pointer':pointer,
            'original_C_file':source_files[packet_path],'original_C_span':source_span,
            'complete_original_C_row':literal,'record_outcome_guards':guards})
    for index,decision in enumerate(record['decisions']):
        status=decision.get('C_doubt_status')
        if status in {None,'resolved','retained'}:continue
        fields=[decision_field]
        fields += [key for key in ('C_source_part_ids','remaining_doubt','source_doubt_component_status') if key in decision]
        decision_values={key:copy.deepcopy(decision[key]) for key in fields}
        guards=[source_guard_ids[identity] for identity in decision[decision_field]]
        cases.append({'scan':scan,'decision_id':decision['id'],'exact_status':status,
                      'decision_fields':decision_values,'source_guards':guards})
        case_evidence.append({'scan':scan,'record_path':f'out/records/scan{scan:03d}.json',
            'record_sha256':sha(record_bytes[scan]),'decision_id':decision['id'],
            'status_pointer':'/decisions/'+str(index)+'/C_doubt_status','exact_original_status':status,
            'decision_binding_pointers':{'/decisions/'+str(index)+'/'+escaped(key):value for key,value in decision_values.items()},
            'source_guard_ids':guards,
            'recorded_root_reference_fields':{key:copy.deepcopy(decision[key]) for key in
                ('root_decision_log','root_decision_section','root_decision_heading','root_evidence_source') if key in decision},
            'exact_source_only_clarification':copy.deepcopy(decision.get('root_source_only_clarification'))})
assert len(cases)==30
assert len({(case['scan'],case['decision_id']) for case in cases})==30
rule_data={'scope':'Finite exact source-bound recognition of 30 existing committed status values; no status is rewritten or reduced to another value.',
           'cases':cases,'source_guards':guard_pool}
rule_file=write(PREFIX+'status_rule_data.json',encode(rule_data))

def recognized(record,decision):
    status=decision.get('C_doubt_status')
    if status in {None,'resolved','retained'}:return True
    matches=[case for case in rule_data['cases'] if case['scan']==record['scan'] and case['decision_id']==decision['id']]
    if len(matches)!=1:return False
    case=matches[0]
    if status!=case['exact_status']:return False
    exact=lambda left,right:json.dumps(left,ensure_ascii=False,separators=(',',':'))==json.dumps(right,ensure_ascii=False,separators=(',',':'))
    if any(key not in decision or not exact(decision[key],value) for key,value in case['decision_fields'].items()):return False
    return all(exact(get(record,pointer),value) for guard_id in case['source_guards'] for pointer,value in rule_data['source_guards'][guard_id])

finite_check=[];old_accepted=new_accepted=0
for path in sorted((BASE/'out/records').glob('scan*.json')):
    record=json.loads(path.read_bytes())
    for decision in record['decisions']:
        old=decision.get('C_doubt_status') in {None,'resolved','retained'}
        new=recognized(record,decision)
        old_accepted+=old;new_accepted+=new
        if old!=new:finite_check.append({'scan':record['scan'],'decision_id':decision['id'],
                                         'exact_status':decision['C_doubt_status'],'before_gate':old,'proposed_gate':new})
assert len(finite_check)==30
assert all(row['proposed_gate'] is True for row in finite_check)
assert new_accepted-old_accepted==30

target='out/scripts/validate.py';before=(BASE/target).read_bytes();before_text=before.decode('utf-8')
helper='''
def documented_c_doubt_status(record, decision):
    status = decision.get('C_doubt_status')
    if status in {None, 'resolved', 'retained'}:
        return True
    evidence_path = R/'checks/final_readiness026_status_rule_data.json'
    evidence_bytes = evidence_path.read_bytes()
    if hashlib.sha256(evidence_bytes).hexdigest() != 'RULE_SHA256':
        return False
    evidence = json.loads(evidence_bytes)
    matches = [case for case in evidence['cases']
               if case['scan'] == record['scan'] and case['decision_id'] == decision['id']]
    if len(matches) != 1:
        return False
    case = matches[0]
    if status != case['exact_status']:
        return False
    def exact(left, right):
        return json.dumps(left, ensure_ascii=False, separators=(',', ':')) == json.dumps(right, ensure_ascii=False, separators=(',', ':'))
    if any(key not in decision or not exact(decision[key], value) for key, value in case['decision_fields'].items()):
        return False
    try:
        for guard_id in case['source_guards']:
            for pointer, expected in evidence['source_guards'][guard_id]:
                value = record
                for key in pointer.split('/')[1:]:
                    key = key.replace('~1', '/').replace('~0', '~')
                    value = value[int(key)] if isinstance(value, list) else value[key]
                if not exact(value, expected):
                    return False
    except (KeyError, IndexError, TypeError, ValueError):
        return False
    return True

'''.replace('RULE_SHA256',rule_file['sha256'])
marker="records=[json.loads(p.read_text()) for p in sorted((R/'records').glob('scan*.json'))]"
old_line="        if d.get('C_doubt_status') not in {None,'resolved','retained'}:issues.append(f\"scan {r['scan']} invalid C doubt status at {d['id']}\")"
new_line="        if not documented_c_doubt_status(r,d):issues.append(f\"scan {r['scan']} invalid C doubt status at {d['id']}\")"
operations=[{'old_text':marker,'new_text':helper+marker,'expected_occurrences':1},
            {'old_text':old_line,'new_text':new_line,'expected_occurrences':1}]
after_text=before_text
for operation in operations:
    assert after_text.count(operation['old_text'])==operation['expected_occurrences']
    after_text=after_text.replace(operation['old_text'],operation['new_text'],1)
after=after_text.encode('utf-8');inverse=[];restored=after_text
for operation in reversed(operations):
    inverse.append({'old_text':operation['new_text'],'new_text':operation['old_text'],'expected_occurrences':1})
    assert restored.count(operation['new_text'])==1
    restored=restored.replace(operation['new_text'],operation['old_text'],1)
assert restored.encode('utf-8')==before
before_file=write(PREFIX+'validate.before.py',before)
after_file=write(PREFIX+'validate.proposed.py',after)
diff=''.join(difflib.unified_diff(before_text.splitlines(keepends=True),after_text.splitlines(keepends=True),fromfile=target,tofile='proposed/'+target)).encode('utf-8')
diff_file=write(PREFIX+'validate.diff',diff)
proposal={'status':'proposal only; root decision after026 pending; no target changed',
    'target':target,'expected_before_sha256':sha(before),'proposed_after_sha256':sha(after),
    'before_snapshot':before_file,'complete_proposed_source':after_file,'unified_diff':diff_file,
    'exact_rule_data':rule_file,
    'rule':'Retain the original three accepted values. For other current statuses, require the exact scan and decision id, exact full status string, exact source-row/part bindings and qualification fields, and every exact documented source-outcome guard. Guard-node comparison uses ordered compact JSON, retaining scalar types and object key order. The rule data file is itself SHA-256 guarded. No prefix matching or status reduction is used.',
    'forward_replacements':operations,'inverse_replacements':inverse,
    'finite_existing_record_check':{'before_accepted_decisions':old_accepted,'proposed_accepted_decisions':new_accepted,
        'exact_added_acceptances':finite_check,'other_existing_acceptances_unchanged':True,
        'proposal_code_executed_imported_or_compiled':False,
        'method':'Independently evaluate the exact equality predicate on the current record data; preserve proposed code as inert text.'},
    'replay':{'forward_proposed_bytes_sha256_matches':True,'inverse_recovers_exact_original_script_bytes':True,
              'original_status_fields_or_records_changed':False,'actual_validator_unchanged':True},
    'scope_limit':'This finite rule covers the 30 enumerated existing decisions through025. The scan026 record and its actual status values are not yet present.'}
proposal_file=write(PREFIX+'validator_status_proposal.json',encode(proposal))

catalog={'scope':'Every original exceptional C_doubt_status, exact record pointer, original C row, source binding and documented component outcome. No reclassification or normalization.',
    'records':[{'path':f'out/records/scan{scan:03d}.json','sha256':sha(data),'bytes':len(data)} for scan,data in record_bytes.items()],
    'original_C_sources':list(source_files.values()),'cases':case_evidence,'original_C_rows':source_rows,
    'validator_rule_data':rule_file,'validator_proposal':proposal_file}
catalog_file=write(PREFIX+'status_catalog.json',encode(catalog))

# Complete bounded review of every case and original row, without repeated
# whole-record data. The full catalog remains the authoritative source map.
review_rows=[{'kind':'original_C_row',**row} for row in source_rows]
review_rows += [{'kind':'status_case',**row} for row in case_evidence]
chunks=[];parts=[];size=0
def save_chunk():
    if not parts:return
    item=write(PREFIX+'status_review_%02d.jsonl'%(len(chunks)+1),b''.join(parts));item['rows']=len(parts);chunks.append(item)
for row in review_rows:
    line=(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n').encode('utf-8')
    assert len(line)<=11000
    if parts and size+len(line)>11000:save_chunk();parts=[];size=0
    parts.append(line);size+=len(line)
save_chunk()
decoded=[json.loads(line) for item in chunks for line in (BASE/item['path']).read_bytes().splitlines()]
assert decoded==review_rows
assert (BASE/target).read_bytes()==before
assert all((BASE/f'out/records/scan{scan:03d}.json').read_bytes()==data for scan,data in record_bytes.items())
index=write(PREFIX+'status_review_index.json',encode({'catalog':catalog_file,'rule_data':rule_file,'proposal':proposal_file,
    'read_order':['All numbered status_review JSONL chunks in order','validate.diff','validator_status_proposal.json replay metadata'],
    'chunks':chunks,'original_C_rows':len(source_rows),'status_cases':len(cases),'byte_inverse_replay':True,
    'actual_targets_unchanged':True,'no_proposed_source_executed_imported_or_compiled':True}))
print(json.dumps({'index':index,'catalog':catalog_file,'rule_data':rule_file,'proposal':proposal_file,'diff':diff_file,
    'chunks':chunks,'before_validator_sha256':sha(before),'after_validator_sha256':sha(after),
    'existing_decisions_before_accepted':old_accepted,'existing_decisions_proposed_accepted':new_accepted,
    'exact_source_rows':len(source_rows),'exact_status_cases':len(cases),'actual_targets_unchanged':True},ensure_ascii=False,indent=2))
