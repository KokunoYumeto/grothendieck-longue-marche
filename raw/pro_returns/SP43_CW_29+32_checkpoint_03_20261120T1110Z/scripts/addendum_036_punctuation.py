"""Add a missing H punctuation-gap row; retain the decided page unchanged."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
O=Path(__file__).resolve().parents[1];s='C29-04_29_scan036';p=O/'decisions'/f'{s}.json';d=json.loads(p.read_text())
assert not any(x['id']=='MAIN-036-faithful-gap' for x in d['differences'])
page=O/'pages'/f'{s}.tex';before=hashlib.sha256(page.read_bytes()).hexdigest();src=f'crops/{s}/faithful_semicolon.png'
d['differences'].append(dict(id='MAIN-036-faithful-gap',place='L8, after fully faithful',C='faithful;',H='faithful ;',reading='faithful;',diff_C=False,diff_H=True,kind='other',marked_in_H='no',evidence='The semicolon is in the next typewriter position after the final l, without an intervening blank. The new narrow crop confirms all three complete readings; their original difference lists did not include this H spacing discrepancy.',source=src,bbox=[1050,650,1510,730],confidence='high',mathematical=False,readers={r:'faithful;' for r in ('r1','r2','r3')}))
d['main_crops'].append(src);d['main_views'].append(src)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
note=f' Post-decision collation addendum {now}: a text audit after 114 found the omitted H faithful ; discrepancy. One new local crop was inspected once, showing adjacency. The page text was already correct and is unchanged. Totals are now 21 effective main inspections: fourteen existing reader crops and seven new main crops.'
d['adjudication']+=note;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert hashlib.sha256(page.read_bytes()).hexdigest()==before
with (O/'progress.log').open('a') as f:f.write(f'collation addendum 29/036 {now}; one H semicolon-gap row; one new crop; page text unchanged SHA256 {before}\n')
(O/'adjudication_inputs'/f'{s}_punctuation_addendum.md').write_text('# Punctuation collation addendum\n\n'+note+'\n\n'+src+'\n')
print('Added 29/036 punctuation row; page unchanged',before)
