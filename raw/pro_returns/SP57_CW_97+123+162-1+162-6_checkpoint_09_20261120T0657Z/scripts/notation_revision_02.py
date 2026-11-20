"""Pre-freeze comparison of the physical circled-x forms on 123/002 and 123/018."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path(__file__).resolve().parents[1]
p=O/'pages/C123-01_123_scan002.tex';rp=O/'decisions/C123-01_123_scan002.json'
r=json.loads(rp.read_text());d=next(x for x in r['differences'] if x['id']=='R3-D44')
old=d['final'];new=r'\mathbin{\text{\textcircled{x}}}'
assert old.startswith('\\unsure{') and p.read_text().count(old)==1
before=hashlib.sha256(p.read_bytes()).hexdigest();p.write_text(p.read_text().replace(old,new));after=hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
evidence='An upright oval and a separate serifed typewriter x are both clear, with the x feet projecting beyond the oval. The existing R3 crop was compared with the two resolved physical forms on 123/018. The transcription records that visible circled-x construction; its possible tensor-product meaning does not require an uncertainty mark on the physical reading.'
d.update(final=new,confidence='high',evidence=evidence,readers='R1: definite circled x; R2: otimes | circled x; R3: circled x | otimes. Root initially retained the symbol-interpretation alternative. On pre-freeze comparison with 123/018, root resolves the physical O-plus-x form consistently, while leaving its mathematical function to the notes.',crop='readers/C123-01_123_scan002/R3/18_tensor.png')
r.setdefault('post_decision_revisions',[]).append(dict(date=now,locus='R3-D44',old=old,new=new,crop=d['crop'],reason='Separate physical form from semantic interpretation and apply recurring notation consistently.',sha256_before=before,sha256_after=after))
r['remaining_doubts']=[x for x in r['remaining_doubts'] if x['place']!='Bottom composite']
for q in r['c_doubts']:
 if 'otimes' in str(q) or 'tensor' in q.get('place','').lower():q.update(decision='Resolved physical circled x after cross-page comparison.',evidence=evidence,crop=d['crop'],confidence='high')
r['notes']+='\nPre-freeze notation comparison resolves the bottom product mark as the visible typewriter oval-plus-serifed-x construction, matching both occurrences on 123/018. The earlier tensor-sign alternative concerned interpretation, not unreadable physical strokes, and is therefore removed from the in-place doubt.\n'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2))
np=O/'briefs/notation.md';s=np.read_text();s=s.replace('`\\unsure{\\mathbin{\\text{\\textcircled{x}}}\\|\\otimes}` at first occurrence.','`\\mathbin{\\text{\\textcircled{x}}}`, resolved in the recorded pre-freeze comparison with 123/018; its possible tensor meaning is not a reading alternative.')
s=s.replace('Earlier local doubt on 123/002 awaits final comparative review.','The same physical form on 123/002 was resolved in the recorded pre-freeze comparison.')
np.write_text(s)
with (O/'progress.log').open('a') as f:f.write('notation revision 02 '+now+' 123/002 circled x resolved consistently with 123/018; existing crops only; SHA256 '+before+' -> '+after+'; transcription not yet frozen\n')
with (O/'SP57_CW_97+123+162-1+162-6_workflow.md').open('a') as f:f.write('\n### Pre-freeze notation revision 02 — '+now+'\n\nThe existing R3 bottom-product crop on 123/002 was viewed alongside the already-read 123/018 crop observations. All show the same oval-plus-serifed-x construction. Root removed the earlier semantic tensor alternative from the transcription while preserving the prior decision in the revision record. This comparison made the repeated physical glyph consistent without importing a mathematical normalization. No new crop was made.\n')
pending=O/'decisions/notation_review_pending.md';s=pending.read_text();s+='\n## Completed during page 7 work\n\n- Revision 01: the existing first-Lie crop on 123/016 was revisited and the definite doubled L is now mathbb, as required. Old/new forms and hashes are retained.\n- Revision 02: the existing 123/002 R3 bottom-product crop was compared with the already-viewed 123/018 forms. The identical physical circled x is now definite on both pages; no new crop was made.\n- Remaining later-page notation comparison remains due before the final freeze.\n';pending.write_text(s)
print(json.dumps({'date':now,'before':before,'after':after,'locus':'123/002 circled x'}))
