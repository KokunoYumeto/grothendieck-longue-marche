from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path(__file__).resolve().parents[1]
t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
files=list((O/'pages').glob('*.tex'))+[O/'SP46_CW_37_transcription.tex']
before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
p=O/'decisions/scan052.json';d=json.loads(p.read_text())
for x in d['decisions']:
 if x.get('consequential') and x.get('unresolved'):
  x['math_uncertainty']=x.pop('consequential')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=O/'notation_review.json';r=json.loads(p.read_text())
r['reviewed_through_scan']=72;r['reviewed_utc']=t
for g in r['groups']:
 if g['group']=='Raised and lowered solid points':
  g['scans']=[69,70,71];g['finding']+=' The two Gr expressions in 071 retain raised solid points, as confirmed by all three half readings.'
 if g['group']=='Quotation pairs and atypical clusters':
  g['scans'] += [71,72];g['finding']+=' The 071 quoted correction pairs and the 072 quotations/ellipses retain the same convention; no new disagreement of quotation identity arose.'
 if g['group']=='Detached marginal points':
  g['scans'] += [71,72];g['finding']+=' Main-viewed 071 and 072 crops establish different shapes: a high oblique pair and faint over-letter traces on 071, and two irregular lobes plus a small satellite on 072. They are drawn separately, with origin and meaning uncertain, rather than normalized to a colon.'
r['groups'].append({'group':'Superscript or baseline abbreviation letters','scans':[52,72],'finding':'The raised letter in the handwritten 052 abbreviation and the baseline typed pt in 072 are distinct physical forms. All three 072 readings confirm both pt letters on the baseline; no superscript is transferred from the earlier hand.'})
r['remaining_scope']='Scans 074–098 remain to be processed in the prescribed order.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=O/'global_check_events.json';events=json.loads(p.read_text())
events.append(dict(statement_id='NOTATION-REVIEW-THROUGH-072',date=t,who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='used and rechecked in this run',outcome='Extended recurring-sign comparison to eight committed pages using their completed independent visual records and already-viewed main crops. Distinct graphic shapes and baseline/raised abbreviation forms retained. Reclassified unresolved mathematical reading alternatives separately from established consequential corrections; no page text changed. No mathematical proof was performed.'))
events.append(dict(statement_id='STRUCTURAL-VALIDATION-THROUGH-072',date=t,who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='computation or formal certificate',outcome='Validated eight page fragments and the combined source for balanced delimiters, grouping, environments, markers, report and inventory structure and retained crop paths. Added resolution for reader paths relative to the workspace or archive. No TeX compilation.'))
p.write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
assert before=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
with (O/'progress.log').open('a') as f:f.write(f'notation review through scan 072 and metadata-only consequence classification {t}; eight page and combined hashes unchanged\n')
print('Extended notation review through 072; page and combined bytes unchanged.')
