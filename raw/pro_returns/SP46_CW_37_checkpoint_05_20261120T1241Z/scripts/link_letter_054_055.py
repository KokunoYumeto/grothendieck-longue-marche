"""Add the now-readable signature context to documentary metadata, not the text."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path(__file__).resolve().parents[1]
p=O/'decisions/scan054.json';d=json.loads(p.read_text())
assert 'attributed from the signed continuation' not in d['notes']
page=O/'pages/H37-01_37_scan054.tex';before=hashlib.sha256(page.read_bytes()).hexdigest()
body={'Handwritten date','Salutation','First letter paragraph','Second letter paragraph','Short cancelled word in second paragraph','Cancelled category in second paragraph','Third letter paragraph','Fourth letter paragraph'}
for x in d['inventory']:
 if x['element'] in body:x['hand']='R. Hartshorne, attributed from signed continuation scan 055'
d['notes']=d['notes'].replace('Hands remain unnamed because this sheet alone has no signature. No other page or reader output was consulted. ','')
d['notes']+=' After scan 055 was independently read, the letter body is attributed from the signed continuation to R. Hartshorne. This is a documentary connection between the adjacent unsigned first leaf and the leaf marked 2, not independent handwriting authentication. The pencil annotations, isolated marks and archival number remain unattributed.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert hashlib.sha256(page.read_bytes()).hexdigest()==before
t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
g=O/'global_check_events.json';events=json.loads(g.read_text())
events.append(dict(statement_id='S054-055-DOCUMENTARY-LINK',date=t,who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='used and rechecked in this run',outcome='The three independent readings of scan 055 agree on manuscript page 2 and the signature R. Hartshorne. The adjoining scan 054 is an unsigned first letter leaf; its body inventory now carries the explicit attribution from the signed continuation. Marginal marks remain unnamed. Documentary metadata only; the scan 054 transcription SHA-256 did not change.'))
g.write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
with (O/'progress.log').open('a') as f:f.write('scan 054 documentary attribution updated from signed scan 055 '+t+'; page transcription unchanged\n')
