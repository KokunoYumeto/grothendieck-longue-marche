"""Bind a root-reviewed selected draft to its page record before commit.

Invocation supplies the exact reviewed hash and independently reviewed counts.
This script makes no ink choice, opens no image, and performs no theorem check.
"""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import argparse,hashlib,json
p=argparse.ArgumentParser()
p.add_argument('scan',type=int)
p.add_argument('--sha256',required=True)
for name in ('C','H','decisions','inventory','doubts','crops','events'):
 p.add_argument('--'+name,type=int,required=True)
a=p.parse_args();n=f'{a.scan:03d}'
OUT=Path(__file__).resolve().parents[1];BASE=OUT.parent
sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
def source_path(value):
 path=Path(value)
 if path.is_absolute():return path
 return (BASE if value.startswith(('packets/','out/','source/')) else OUT)/path
record_draft=OUT/'checks'/f'scan{n}_record_draft.json'
r=json.loads(record_draft.read_text())
f=json.loads((OUT/'checks'/f'scan{n}_reader_fingerprints.json').read_text())
for key,value in f['files'].items():assert sha(source_path(value['path']))==value['sha256'],key
for role in 'ABC':
 report=json.loads((OUT/'readers'/n/role/'report.json').read_text())
 assert all(report[k] for k in ('full_image_viewed','halves_viewed','complete_visual_read')),role
audit_path=OUT/'checks'/f'scan{n}_root_crop_audit.json'
audit=json.loads(audit_path.read_text())
assert not audit['whole_or_halves_seen_by_root']
assert audit['total_distinct']==a.crops
assert len({x['path'] for x in audit['viewed_once']})==a.crops
for item in audit['viewed_once']:
 assert item['successful_display_count']==1,item['path']
 assert sha(OUT/item['path'])==item['sha256'],item['path']
source_audit=OUT/'checks'/f'scan{n}_source_audit.md'
assert source_audit.is_file()
assert not r.get('pending_root_decision_ids')
assert len(r['decisions'])==a.decisions and len(r['inventory'])==a.inventory and len(r['doubts'])==a.doubts
assert len(r.get('check_events',[]))==a.events
assert all(i['transcribed']=='yes' for i in r['inventory'])
assert all(all(k in item for k in ('form','expansion')) for item in r.get('abbreviations',[]))
assert sum(bool(d['diff_C']) for d in r['decisions'])==a.C
assert sum(bool(d['diff_H']) for d in r['decisions'])==a.H
assert all(set(d['readers'])=={'A','B','C'} for d in r['decisions'])
draft=OUT/'checks'/f'scan{n}_final_draft.tex'
page_bytes=draft.read_bytes();page=page_bytes.decode();page_sha=sha(draft)
assert page_sha==a.sha256
source_map=json.loads((OUT/'checks'/f'scan{n}_final_source_map.json').read_text())
assert source_map['draft_sha256_utf8']==page_sha
page_ref='pages/'+r['filename']
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def bind(value):
 if isinstance(value,dict):
  if value.get('path')==f'checks/scan{n}_final_draft.tex' and 'char_start' in value:
   start,end=value['char_start'],value['char_end'];assert 0<=start<end<=len(page)
   value['source_manifest']=value.pop('manifest','root.final_draft.tex')
   value.update(path=page_ref,sha256=page_sha,body_sha256=hashlib.sha256(page[start:end].encode()).hexdigest())
  for child in value.values():bind(child)
 elif isinstance(value,list):
  for child in value:bind(child)
bind(r)
for d in r['decisions']:
 d['main_approved']=True
 d['root_source_attachment_status']='Root approved complete selected-source attachment.'
 d['count_status']='Root approved physical-cluster count; raw reader proposals remain in provenance.'
for i in r['inventory']:
 i['main_approved']=True
 i['selection_status']='Root approved the selected source content.'
 i['hand_status']='root approved; qualified or mixed attribution remains explicit'
for d in r.get('doubts',[]):d['main_approved']=True
# These are current selected record views. Raw candidate/source-group/reader
# provenance and the frozen draft/map remain historical and are not rewritten.
for field in ('selected_graphical_groups','source_locus_coverage','abbreviations'):
 for item in r.get(field,[]):
  item['main_approved']=True
for field in ('attributed_content_note','root_selected_content_note'):
 if isinstance(r.get(field),dict):r[field]['main_approved']=True
for row in r.get('C_source_rows',[]):
 for part in row.get('source_parts',[]):
  if 'decision_status' in part:
   part.setdefault('original_source_decision_status',part['decision_status'])
  part['decision_status']='Root approved the recorded original-doubt outcome.'
  part['main_approved']=True
r.update(main_adjudicated=True,main_approved=True,main_approved_utc=now,root_page_text_exact=page,root_actions_pending=[],reader_fingerprints=f,
 root_approval_status='Root approved the final record and selected text.',root_approved_decision_entries=len(r['decisions']),
 root_crop_audit=f'checks/scan{n}_root_crop_audit.json',root_source_audit=f'checks/scan{n}_source_audit.md',
 final_page=dict(path=page_ref,sha256=page_sha,selected_draft=f'checks/scan{n}_final_draft.tex',relation='byte-for-byte identical; character offsets preserved'),
 source_attachment_status='Root approved after the targeted source audit; final-page attachments use exact selected-draft offsets.')
r['counts']=dict(C=a.C,H=a.H,decision_loci=a.decisions,remaining_doubt_loci=a.doubts,inventory_elements=a.inventory,check_events=a.events)
(OUT/page_ref).write_bytes(page_bytes)
(OUT/'records'/f'scan{n}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
approval=dict(scan=a.scan,approved_utc=now,page=page_ref,sha256=page_sha,counts=r['counts'],root_crops=a.crops,
 C_confidence=dict(Counter(d['confidence'] for d in r['decisions'] if d['diff_C'])),H_confidence=dict(Counter(d['confidence'] for d in r['decisions'] if d['diff_H'])),
 validation_scope='Root reviewed the selected text, decisions, doubts, inventory and source audit; commit_page.py supplies the required structural gate.',
 source_audit_sha256=sha(source_audit),reviewed_record_sha256=sha(record_draft))
(OUT/'checks'/f'scan{n}_root_approval.json').write_text(json.dumps(approval,ensure_ascii=False,indent=2)+'\n')
with (OUT/'progress.log').open('a') as log:log.write(f'scan{n} root approval {now}; {a.crops} distinct root crops; byte-exact selected draft; {a.events} recorded check events\n')
print(json.dumps(approval,ensure_ascii=False))
