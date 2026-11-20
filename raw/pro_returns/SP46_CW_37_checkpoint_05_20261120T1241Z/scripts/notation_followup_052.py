"""Supplement collation after the scan 053 upper-rule convention comparison.
The consolidated scan 052 transcription is unchanged.
"""
from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
O=Path(__file__).resolve().parents[1];p=O/'decisions/scan052.json';d=json.loads(p.read_text())
page=O/'pages/H37-01_37_scan052.tex';before=hashlib.sha256(page.read_bytes()).hexdigest()
prefix='Notation comparison: upper rule'
assert not any(x['place'].startswith(prefix) for x in d['decisions'])
for name,numeral,crop in [('first entry','VII','crops/scan052/vii_upper_rule.jpg'),('second entry','V/VI','readers/scan052/C/01_second_numeral.jpg'),('fourth entry','IV','crops/scan052/iv_upper_rule.jpg'),('projective-systems entry','VI','crops/scan052/vi_upper_rule.jpg')]:
 d['decisions'].append(dict(place=f'{prefix} at {name}',c_reading=f'{numeral} with upper and lower transverse rules',h_reading=f'Italic {numeral}; note says exposé numbers are underlined',reading=f'{numeral} with upper and lower transverse rules',diff_c=False,diff_h=True,c_doubt=False,unresolved=False,alternatives='',confidence='high',kind='drawing or diagram',marked_in_H='yes' if numeral=='V/VI' else 'no',scan_shows='A separate horizontal stroke lies above the numeral as well as the lower rule. All three returns already preserve it. The distinction established on scan 053 is applied consistently: H’s italic convention represents underlining but not this additional upper stroke. The numeral reading itself is unchanged and any local numeral doubt remains in its separate row.',crop=crop,readers={a:'Upper and lower rules present in returned reading and inventory' for a in 'ABC'}))
d['main_crops']=json.loads((O/'crops/scan052/manifest.json').read_text())
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d['check_events'].append(dict(statement_id='S052-UPPER-RULE-COLLATION',date=now,who='GPT-6 Astra Pro; effort not exposed; main notation comparison after scan 053',type='used and rechecked in this run',outcome='Four H graphic-omission rows added after comparing the upper-rule convention across scans 052 and 053. Three new tight crops and the already inspected second-numeral crop support the rows. This is documentary collation only; no mathematical proof check. The page transcription SHA-256 is unchanged.'))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert hashlib.sha256(page.read_bytes()).hexdigest()==before
with (O/'progress.log').open('a') as f:f.write(f'scan 052 collation supplemented {now}; four upper-rule rows; page transcription unchanged; three new graphic-locus crops\n')
q=O/'notation_review_pending.json';q.write_text('[]\n')
with (O/'workflow_assessment.txt').open('a') as f:f.write('\nAfter scan 053, comparison of the Roman-heading convention identified four upper-rule omissions in H not separately logged on scan 052. Four collation rows were added, using one existing crop and three new graphic-locus crops. The scan 052 transcription did not change. Its main additional crop total is therefore twelve, including the later notation comparison.\n')
print('Added four graphic collation rows; transcription unchanged.')
