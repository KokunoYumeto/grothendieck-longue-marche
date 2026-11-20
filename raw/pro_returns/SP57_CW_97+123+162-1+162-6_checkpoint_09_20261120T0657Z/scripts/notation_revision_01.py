"""Recorded, pre-freeze correction to apply the required double-strike convention."""
from pathlib import Path
from datetime import datetime, timezone
import json,hashlib
O=Path(__file__).resolve().parents[1]
p=O/'pages/C123-01_123_scan016.tex';rp=O/'decisions/C123-01_123_scan016.json'
r=json.loads(rp.read_text());d=next(x for x in r['differences'] if x['id']=='R1-D09')
old=d['final'];new=r'\mathop{\mathbb{L}\mathrm{ie}}'
assert 'tikzpicture' in old and p.read_text().count(old)==1
before=hashlib.sha256(p.read_bytes()).hexdigest()
p.write_text(p.read_text().replace(old,new))
after=hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d.update(final=new,confidence='high',evidence='Two parallel typewriter stems enclosing a narrow white channel, with offset top and foot, are visible in L; i and e are ordinary single impressions. The explicit source convention requires mathbb for this definite same-letter double strike.',readers='R1: double-struck L via mathbb; R2: ordinary Lie; R3: ordinary Lie. Root first drew the doubled L as an overlay, then on the recorded pre-freeze notation review applied the required mathbb convention. The existing crop was revisited; no new crop was made.')
r.setdefault('post_decision_revisions',[]).append(dict(date=now,locus='R1-D09',old=old,new=new,crop=d['crop'],reason='Required double-strike convention, consistent with the double O on 97/019; no change to the neighboring letters or mathematical content.',sha256_before=before,sha256_after=after))
r['notes']+='\nPre-freeze notation review: the first L of Lie(i)(1) has two distinct offset stems and is transcribed with mathbb under the stipulated double-strike convention. The initial TikZ overlay was revised to the required alphabet representation; ordinary later Lie occurrences are unchanged.\n'
for e in r['inventory']:
 if e['element']=='Double impression of first L in Lie(i)(1)':e['first_words_or_objects']='double-struck L, rendered mathbb, followed by ordinary ie'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2))
np=O/'briefs/notation.md';s=np.read_text();s=s.replace('A small TikZ overlay retains them without creating a new blackboard-bold operator; later Lie is ordinary.','The required convention gives `\\mathop{\\mathbb{L}\\mathrm{ie}}`; later Lie is ordinary. The initial TikZ overlay was corrected in the recorded pre-freeze notation review.')
np.write_text(s)
with (O/'progress.log').open('a') as f:f.write('notation revision 01 '+now+' 123/016 first doubled L: TikZ overlay -> mathbb per required convention; existing crop revisited, no new crop; SHA256 '+before+' -> '+after+'; transcription not yet frozen\n')
with (O/'SP57_CW_97+123+162-1+162-6_workflow.md').open('a') as f:f.write('\n### Pre-freeze notation revision 01 — '+now+'\n\nThe main reader revisited the existing 123/016 first-Lie crop during work on page 7. The two offset L stems are definite. The earlier graphic overlay preserved the ink but did not follow the explicit mathbb convention, so only that L was changed to mathbb. The decision record retains the old/new forms and hashes. This is an honest correction to the main reader’s treatment, not a new reading from an unseen scan or a new crop. It also agrees with the established double-O treatment on 97/019. The v07 brief had already corrected the overly broad warning; no page-7 reading was supplied to its independent readers.\n')
print(json.dumps({'date':now,'before':before,'after':after,'locus':'123/016 first L'}))
