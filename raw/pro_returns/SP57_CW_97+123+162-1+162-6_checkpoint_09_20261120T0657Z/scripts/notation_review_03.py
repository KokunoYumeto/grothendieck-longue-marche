"""Record the crop-based o/0 comparison; page bytes remain unchanged."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path('out');s='C123-01_123_scan016';p=O/'decisions'/f'{s}.json'
page=O/'pages'/f'{s}.tex';before=hashlib.sha256(page.read_bytes()).hexdigest()
d=json.loads(p.read_text())
for x in d['differences']:
 if x['id'] in ['R1-D20','R1-D21','R1-D24']:
  x['evidence']+=' Cross-page review: the existing crop shows typewriter rings of the same x-height as the adjacent e/x/u, distinctly shorter than numeral zero. These typed subscripts are resolved as o, independently of the handwritten o/0 doubts. No page text changes because o was already the first candidate.'
  if x['id']!='R1-D20':x['confidence']='high'
for x in d['remaining_doubts']:
 if x['place'].startswith('Round subscripts'):
  x['place']='Handwritten round subscripts in b) and the (ii) uniqueness addition; typed occurrences resolved as o'
  x['confidence']='low'
for x in d['c_doubts']:
 if any(z in str(x) for z in ['o|0','o/0']):
  x['decision']+=' Cross-page review retains doubt only for the handwritten rings; the typed lower rings are resolved as lowercase o from x-height and matching type contours.'
d['notes']+='\n\nCross-page notation review: existing crops on this leaf resolve the typed round indices as lowercase o by their x-height. The handwritten rings in b) and the (ii) addition remain o/0 doubtful, as do the handwritten Z indices on 123/017. This clarifies the scope of the uncertainty without changing the already transcribed first-candidate o letters.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
after=hashlib.sha256(page.read_bytes()).hexdigest();assert before==after
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (O/'progress.log').open('a') as f:f.write('notation review 03 '+now+' 123/016 typed rings resolved o; handwritten rings on 123/016 and 017 retain o/0. Apparatus scope clarified; page hash unchanged '+after+'\n')
with (O/'decisions/notation_review_pending.md').open('a') as f:f.write('''\n## Round-index comparison during page 10 work\n\nRoot revisited existing 123/016 R1 crops 11_d_primes_tail, 09_b_addition, 15_unique_insertion, root basis_subscripts and ii_subscripts, plus 123/017 R3 03_left_margin. No new crop or whole/half view was made. Typed indices match adjacent lowercase x-height; they agree with the resolved typed o forms on 123/018–020. The handwritten rings do not acquire that distinction merely by comparison and retain o/0 doubt. Page text is unchanged; the 123/016 remaining-doubt entry and evidence now distinguish these two media. Continue the remaining alphabet/sign comparisons before freeze.\n''')
with (O/'briefs/notation.md').open('a') as f:f.write('| 123/016–020 cross-page review | Round indices by medium | Existing crops resolve the typed rings on 123/016 as lowercase o, matching 018–020; handwritten rings on 016–017 remain o/0 doubtful. A machine-height distinction is not transferred to pen circles. |\n')
with (O/'SP57_CW_97+123+162-1+162-6_workflow.md').open('a') as f:f.write('\nCross-page notation review during page 10: six existing crops from 123/016–017 were revisited solely for the required notation comparison. No new crop was made. Typed o is resolved independently of handwritten o/0; page bytes remain unchanged.\n')
print(json.dumps({'page_hash_unchanged':after}))
