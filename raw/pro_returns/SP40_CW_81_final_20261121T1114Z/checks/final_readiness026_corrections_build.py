"""Prepare two exact proposals; leave both actual targets unchanged."""
import copy
import csv
import hashlib
import io
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

def parent(doc,pointer):
    bits=[bit.replace('~1','/').replace('~0','~') for bit in pointer.split('/')[1:]]
    for bit in bits[:-1]:doc=doc[int(bit)] if isinstance(doc,list) else doc[bit]
    return doc,int(bits[-1]) if isinstance(doc,list) else bits[-1]

def replay(doc,ops):
    doc=copy.deepcopy(doc)
    for operation in ops:
        container,key=parent(doc,operation['path']);kind=operation['op']
        if kind=='test':assert container[key]==operation['value']
        elif kind=='add':assert key not in container;container[key]=copy.deepcopy(operation['value'])
        elif kind=='replace':assert key in container;container[key]=copy.deepcopy(operation['value'])
        elif kind=='remove':del container[key]
        else:raise AssertionError(kind)
    return doc

record_path='out/records/scan017.json'
record_before=(BASE/record_path).read_bytes()
assert sha(record_before)=='4653b2d90ba7d86e3306b4bf357c43ba9b74634e2fc97de2474d7503ef613435'
record=json.loads(record_before);assert encode(record)==record_before
event=record['check_events'][0]
assert event['id']=='SP40-017-SOURCE-COORDINATES'
assert all(key not in event for key in ('statement_id','who','outcome'))
outcome_keys=('statement_or_location','inputs','mapping','result','scope',
              'event_clock','event_clock_note','rerun_by_clerk','mathematical_theorem_check')
outcome_object={key:copy.deepcopy(event[key]) for key in outcome_keys}
outcome=json.dumps(outcome_object,ensure_ascii=False,separators=(',',':'))
assert json.dumps(json.loads(outcome),ensure_ascii=False,separators=(',',':'))==outcome
assert list(json.loads(outcome))==list(outcome_keys)
assert all(json.loads(outcome)[key]==event[key] for key in outcome_keys)
values={'statement_id':event['id'],'who':event['actor'],'outcome':outcome}
source_keys=('id','actor')+outcome_keys
forward=[{'op':'test','path':'/check_events/0/'+key,'value':copy.deepcopy(event[key])} for key in source_keys]
forward += [{'op':'add','path':'/check_events/0/'+key,'value':value} for key,value in values.items()]
inverse=[]
for key,value in reversed(list(values.items())):
    inverse.extend([{'op':'test','path':'/check_events/0/'+key,'value':value},
                    {'op':'remove','path':'/check_events/0/'+key}])
record_after=replay(record,forward);record_after_bytes=encode(record_after)
record_restored=encode(replay(record_after,inverse))
assert record_restored==record_before
assert list(record_after['check_events'][0])==list(event)+list(values)
assert all(record_after['check_events'][0][key]==value for key,value in event.items())
assert len(record_after['check_events'])==len(record['check_events'])

fields=['statement_id','date','who','type','outcome']
before_fields={field:event.get(field,'') for field in fields}
after_fields={field:record_after['check_events'][0].get(field,'') for field in fields}
stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t',extrasaction='ignore')
writer.writeheader();writer.writerow(record_after['check_events'][0])
projected_tsv=stream.getvalue().encode('utf-8')
projected_rows=list(csv.DictReader(io.StringIO(projected_tsv.decode('utf-8')),delimiter='\t'))
assert projected_rows==[after_fields]
event_proposal={
    'status':'proposal only; not applied; root decision pending after026',
    'target':record_path,'expected_before_sha256':sha(record_before),
    'proposed_after_sha256':sha(record_after_bytes),'serialization':'UTF-8 json.dumps(ensure_ascii=False, indent=2) plus LF',
    'original_copy':write(PREFIX+'scan017_record.before.json',record_before),
    'scope':'Append exactly statement_id, who and outcome to /check_events/0; preserve every existing key, value, key order and all other record content.',
    'exact_added_key_order':['statement_id','who','outcome'],
    'source_to_added_field_mapping':[
        {'target_pointer':'/check_events/0/statement_id','source_pointer':'/check_events/0/id','value':event['id']},
        {'target_pointer':'/check_events/0/who','source_pointer':'/check_events/0/actor','value':event['actor']},
        {'target_pointer':'/check_events/0/outcome',
         'construction':'Compact UTF-8 JSON text, ensure_ascii=False, separators=(comma, colon), preserving the exact ordered source keys and their copied JSON values shown below.',
         'ordered_source_fields':[{'outcome_key':key,'source_pointer':'/check_events/0/'+key,'exact_value':copy.deepcopy(event[key])} for key in outcome_keys],
         'complete_exact_value':outcome}],
    'forward_json_patch':forward,'inverse_json_patch':inverse,
    'public_event_fields_before':before_fields,'public_event_fields_after':after_fields,
    'single_event_tsv_preview':write(PREFIX+'scan017_event.proposed.tsv',projected_tsv),
    'replay':{'forward_only_three_keys_added':True,'all_original_event_fields_and_order_preserved':True,
        'all_other_record_content_preserved':True,'outcome_JSON_decodes_to_exact_copied_source_values':True,
        'inverse_recovers_original_record_bytes':record_restored==record_before,
        'no_coordinate_or_result_recalculation':True,'no_new_event_created':True,'actual_target_unchanged':True},
}

evidence_path='out/checks/wf_root_crop_counts_through025_proposal/evidence.json'
evidence_before=(BASE/evidence_path).read_bytes()
assert sha(evidence_before)=='1a1bdd82104ce0981bc6efbc3ec372ef417f676d9081245922f9f7fbc2315dab'
evidence=json.loads(evidence_before);assert encode(evidence)==evidence_before
pointer='/earlier_pages/2/enumeration_selector'
before=evidence['earlier_pages'][2]['enumeration_selector']
assert before=='root-only manifest; scan003 successful use separately attested by journal line31'
after='root-only manifest; scan004 successful use separately attested by journal line3'
assert evidence['earlier_pages'][2]['scan']==4
source=evidence['earlier_pages'][2]['journal_source']
journal=(BASE/source['path']).read_bytes();assert sha(journal)==source['sha256']
line=evidence['earlier_pages'][2]['historical_display_failure_lines'][0]
assert line['line']==3 and journal.decode('utf-8').splitlines()[2]==line['text']
wf_forward=[{'op':'test','path':pointer,'value':before},{'op':'replace','path':pointer,'value':after}]
wf_inverse=[{'op':'test','path':pointer,'value':after},{'op':'replace','path':pointer,'value':before}]
evidence_after=replay(evidence,wf_forward);evidence_after_bytes=encode(evidence_after)
evidence_restored=encode(replay(evidence_after,wf_inverse));assert evidence_restored==evidence_before
copy_after=copy.deepcopy(evidence_after);copy_after['earlier_pages'][2]['enumeration_selector']=before
assert encode(copy_after)==evidence_before
selector_proposal={
    'status':'proposal only; not applied; root decision pending after026',
    'target':evidence_path,'expected_before_sha256':sha(evidence_before),
    'proposed_after_sha256':sha(evidence_after_bytes),'serialization':'UTF-8 json.dumps(ensure_ascii=False, indent=2) plus LF',
    'original_copy':write(PREFIX+'workflow_evidence.before.json',evidence_before),
    'scope':'One exact selector-string replacement; all counts, paths, source identities, failures, historical records and builder proposal stay unchanged.',
    'target_pointer':pointer,'exact_before':before,'exact_after':after,
    'existing_evidence':{'scan_pointer':'/earlier_pages/2/scan','scan_value':4,
        'journal_metadata_pointer':'/earlier_pages/2/journal_source','journal_source':source,
        'journal_line':3,'exact_journal_line':line['text'],
        'failure_excerpt_pointer':'/earlier_pages/2/historical_display_failure_lines/0'},
    'forward_json_patch':wf_forward,'inverse_json_patch':wf_inverse,
    'replay':{'only_requested_selector_changed':True,'inverse_recovers_original_evidence_bytes':True,'actual_target_unchanged':True},
}
assert (BASE/record_path).read_bytes()==record_before
assert (BASE/evidence_path).read_bytes()==evidence_before
event_file=write(PREFIX+'scan017_event_proposal.json',encode(event_proposal))
selector_file=write(PREFIX+'workflow_selector_proposal.json',encode(selector_proposal))
print(json.dumps({'event_proposal':event_file,'event_after_sha256':sha(record_after_bytes),
    'selector_proposal':selector_file,'selector_after_sha256':sha(evidence_after_bytes),
    'exact_inverse_replays':True,'actual_targets_unchanged':True},ensure_ascii=False,indent=2))
