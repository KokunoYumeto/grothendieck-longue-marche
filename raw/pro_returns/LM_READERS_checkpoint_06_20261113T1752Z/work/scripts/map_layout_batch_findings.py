"""Attach exact applied source records to the still-open visual findings."""
from pathlib import Path
import hashlib,json
from integrate_layout_pending import identifier

ROOT=Path(__file__).resolve().parents[2]
ALIASES={
 'VIS-140-3-441-117':'scan441_eq117',
 'VIS-140-3-449-137-138':'scan449_labels',
 'VIS-140-2-252-OPTIONS':'scan252_options',
 'VIS-140-3-443-121':'scan443_520_labels',
 'VIS-140-3-520-81':'scan443_520_labels',
 'VIS-140-3-637-BLUE-NOTE':'scan637_blue_note',
 'VIS-140-2-089-SECTION12':'section12',
 'VIS-140-3-186-SECTIONII':'sectionII',
 'VIS-140-3-055-3':'scan055_epimorphism',
 'VIS-140-3-221-REMARQUE':'remarque221',
 'VIS-140-1-025-HEADING-B':'scan025_B_heading',
 'VIS-140-3-408-44':'scan408_eq44',
 'VIS-140-4-75-E144-MASK':'scan75_diagram144',
 'VIS-140-3-519-TAG79-INTRO':'scan519_tag79',
}


def main():
 result=json.loads((ROOT/'work/data/layout_batch_integration_result.json').read_text())
 assert result['actual_total_records']==result['expected_total_records']
 items=json.loads((ROOT/'work/data/layout_pending_batch.json').read_text())['items']
 byname={r['name']:r for r in items};bypath={r['candidate']:r for r in items}
 applied=json.loads((ROOT/'work/data/layout_repairs_applied.json').read_text())
 lookup={(r['id'],r['language']):r for r in applied}
 path=ROOT/'work/data/final_visual_issue_closure.json';before=path.read_bytes();obj=json.loads(before)
 mapping=[]
 for finding in obj['findings']:
  if finding['id'].startswith('VIS-GENERATED-') or 'RANGEHEADING' in finding['id']:
   continue
  item=bypath.get(finding.get('candidate','')) or byname[ALIASES[finding['id']]]
  data=json.loads((ROOT/item['candidate']).read_text());rows=data['records'] if isinstance(data,dict) else data
  scan=494 if finding['id']=='VIS-140-3-495-SECTION49' else int(finding['scan'])
  rows=[r for r in rows if int(r['scan'])==scan]
  assert rows and {r['language'] for r in rows}=={'fr','en'},finding['id']
  ids=sorted({identifier(r,item['name']) for r in rows})
  source_records=[]
  for ident in ids:
   for lang in ('fr','en'):
    r=lookup[ident,lang]
    assert r['cote']==finding['cote'] and r['scan']==scan
    source_records.append({k:r[k] for k in ['id','language','package','cote','scan','source_path','source_line','source_byte_start','source_byte_end']})
  finding['candidate']=item['candidate'];finding['probe_validation']=item['validation']
  finding['repair_record_ids']=ids
  finding['source_record_languages']=['fr','en']
  finding['integration_status']='APPLIED_AWAITING_CURRENT_PUBLICATION_REVIEW'
  # Deliberately preserve status and every publication-confirmation field.
  mapping.append(dict(finding_id=finding['id'],candidate=item['candidate'],probe_validation=item['validation'],repair_record_ids=ids,source_records=source_records,publication_status=finding['status']))
 assert len(mapping)==len(obj['findings'])-4
 assert path.read_bytes()==before,'Concurrent finding-ledger edit; retry against its new bytes.'
 temporary=path.with_suffix('.json.tmp');temporary.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');temporary.replace(path)
 (ROOT/'work/data/layout_issue_source_mapping.json').write_text(json.dumps(dict(status='SOURCE_RECORDS_ATTACHED_PUBLICATION_FINDINGS_NOT_CLOSED',source_local_findings=len(mapping),source_records=sum(len(r['source_records']) for r in mapping),findings=mapping),ensure_ascii=False,indent=2)+'\n')
 print(len(mapping),'source-local findings mapped; publication statuses unchanged')


if __name__=='__main__':main()
