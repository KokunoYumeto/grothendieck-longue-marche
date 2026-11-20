"""Root approval after complete source/reader/crop and record-scope review."""
from pathlib import Path
import json,datetime,hashlib,collections
O=Path(__file__).resolve().parents[1]
p=O/'decisions/156-4_072.json';d=json.loads(p.read_text())
page=O/'pages'/d['filename']
assert d['brief_version']=='v08'
assert hashlib.sha256(page.read_bytes()).hexdigest()==d['final_text_sha256']
assert len(d['differences'])==69
assert sum(x['change_c'] for x in d['differences'])==38
assert sum(x['change_h'] for x in d['differences'])==63
assert d['reader_crop_counts']=={'R1':17,'R2':18,'R3':18}
assert d['adjudicator_existing_crop_views']==20 and d['adjudicator_crop_count']==5
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d['review_status']='approved by root after direct crop adjudication and complete record review'
d['root_reviewed_utc']=now
d['record_review_note']='Root read all three complete fragments and all 169 reader differences, all 69 consolidated row scopes, remaining doubts, disputes, inventory, notes and source coverage. Corrected candidate-priority flags, comparable source/final scopes, confidence, version, and literal absence wording. Supporting crop paths and scope notes are exposed by the deliverable renderer. No page reading changed during administrative record review.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (O/'decisions/156-4_072_record_audit.md').open('a') as f:f.write('\n## Root approval — '+now+'\n\nAll three complete independent readings and all consolidated scopes have been reviewed against the root crop record. Approved:69 loci,38 C/63 H changes;23 uncertainty macros covered by22 remaining-doubt loci;29 disputes;45 inventory elements. Root viewed20 existing and5 new crops. The final page hash matches; no mathematical proof check occurred.\n')
with (O/'progress.log').open('a') as f:f.write('156-4_072 root record review complete '+now+'; 69 loci; C38/H63; 20 existing crops and 5 new crops; no proof check\n')
print('Approved 156-4_072',dict(collections.Counter(x['confidence'] for x in d['differences'])))
