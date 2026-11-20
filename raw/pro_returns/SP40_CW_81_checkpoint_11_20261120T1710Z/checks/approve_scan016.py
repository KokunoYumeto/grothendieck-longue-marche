"""Bind root-approved scan016 text and audit to the required page commit.
No image, rendering, geometric calculation or manuscript theorem check occurs here.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib,json
BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r=json.loads((OUT/'checks/scan016_record_draft.json').read_text())
f=json.loads((OUT/'checks/scan016_reader_fingerprints.json').read_text())
for key,value in f['files'].items():
 path=(BASE if value['path'].startswith('packets/') else OUT)/value['path']
 assert sha(path)==value['sha256'],key
for role in 'ABC':
 d=json.loads((OUT/'readers/016'/role/'report.json').read_text())
 assert all(d[k] for k in ('full_image_viewed','halves_viewed','complete_visual_read'))
 assert not d.get('check_events')
audit_path=OUT/'checks/scan016_root_crop_audit.json'
audit=json.loads(audit_path.read_text())
assert audit['total_distinct']==20
assert len({x['path'] for x in audit['viewed_once']})==20
assert not audit['whole_or_halves_seen_by_root']
assert len(audit['failed_unseen_attempts'])==1
for item in audit['viewed_once']:
 assert sha(OUT/item['path'])==item['sha256']
 assert item['successful_display_count']==1
source_audit=OUT/'checks/scan016_source_audit.md'
assert source_audit.is_file()
assert not r['pending_root_decision_ids']
assert len(r['decisions'])==58 and len(r['inventory'])==47 and len(r['doubts'])==22
assert all(x['transcribed']=='yes' for x in r['inventory'])
assert len(r['check_events'])==1 and r['check_events'][0]['statement_id']=='SP40-016-IMAGE-FRAME'
draft=OUT/'checks/scan016_final_draft.tex'
page_bytes=draft.read_bytes();page=page_bytes.decode();page_sha=sha(draft)
assert page_sha=='21359f1198e8cffcdb2fdc05d92cd2a2d1e421dfbbd6f3b2f833ddf96d139c22'
source_map=json.loads((OUT/'checks/scan016_final_source_map.json').read_text())
assert source_map['draft_sha256_utf8']==page_sha
assert '\\unsure{é|ê}gal\\unsure{|e}' in page
assert page.count('\\overline')==14
page_ref='pages/'+r['filename']
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def finalize_attachments(value):
 if isinstance(value,dict):
  if value.get('path')=='checks/scan016_final_draft.tex' and 'char_start' in value:
   start,end=value['char_start'],value['char_end']
   assert 0<=start<end<=len(page)
   value['source_manifest']=value.pop('manifest','root.final_draft.tex')
   value.update(path=page_ref,sha256=page_sha,body_sha256=hashlib.sha256(page[start:end].encode()).hexdigest())
  for child in value.values():finalize_attachments(child)
 elif isinstance(value,list):
  for child in value:finalize_attachments(child)
finalize_attachments(r)
for d in r['decisions']:
 d['main_approved']=True
 assert set(d['readers'])=={'A','B','C'}
for item in r['inventory']:item['hand_status']='root approved; qualified attribution remains explicit'
r.update(main_adjudicated=True,main_approved_utc=now,root_page_text_exact=page,root_actions_pending=[],reader_fingerprints=f,
 root_crop_audit='checks/scan016_root_crop_audit.json',root_source_audit='checks/scan016_source_audit.md',
 final_page=dict(path=page_ref,sha256=page_sha,selected_draft='checks/scan016_final_draft.tex',relation='byte-for-byte identical; character offsets preserved'),
 source_attachment_status='Root approved; final-page attachments use exact selected-draft offsets.')
r['counts']=dict(C=sum(bool(d['diff_C']) for d in r['decisions']),H=sum(bool(d['diff_H']) for d in r['decisions']),decision_loci=len(r['decisions']),remaining_doubt_loci=len(r['doubts']),inventory_elements=len(r['inventory']),check_events=1)
assert r['counts']['C']==22 and r['counts']['H']==29,r['counts']
(OUT/page_ref).write_bytes(page_bytes)
(OUT/'records/scan016.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
approval=dict(scan=16,approved_utc=now,page=page_ref,sha256=page_sha,counts=r['counts'],root_crops=20,
 C_confidence=dict(Counter(d['confidence'] for d in r['decisions'] if d['diff_C'])),H_confidence=dict(Counter(d['confidence'] for d in r['decisions'] if d['diff_H'])),
 validation_scope='Root reviewed the full selected text and all decisions/inventory; the required structural gate is supplied by commit_page.py.',source_audit_sha256=sha(source_audit))
(OUT/'checks/scan016_root_approval.json').write_text(json.dumps(approval,ensure_ascii=False,indent=2)+'\n')
with (OUT/'progress.log').open('a') as stream:stream.write('scan016 root approval '+now+'; 20 distinct crops; byte-exact selected draft; one prior finite image-frame event; no compilation\n')
print(json.dumps(approval,ensure_ascii=False))
