from pathlib import Path
from datetime import datetime, timezone
import csv, json, subprocess, sys

root=Path(__file__).resolve().parents[1]
p='148_scan012'
f={r['box']:r['reading'] for r in csv.DictReader((root/'second'/f'{p}_first.tsv').open(),delimiter='\t')}
s={r['box']:r['reading'] for r in csv.DictReader((root/'second'/f'{p}_second.tsv').open(),delimiter='\t')}
report_path=root/'work'/f'{p}_final.json'
report=json.loads(report_path.read_text())
assert not report.get('audit')
signature=s['B05'].replace('\\figure{','\\unsure{',1).replace('x=0.0023cm,y=-0.0023cm','x=0.00083cm,y=-0.00083cm')
page_path=root/'pages'/f'{p}.tex'
page=page_path.read_text()
assert page.count(f['B05'])==1
page_path.write_text(page.replace(f['B05'],signature))
evidence={
'B01':'Thirteen separate keyed circumflex marks appear below DU LANGUEDOC. Both readings give the same count; font wrappers and explicit empty macro arguments make the token difference.',
'B02':'The heading has the same words, and the separate keyed row has 52 pairs of short horizontal bars. The difference concerns spacing and line-break serialization only.',
'B03':'The complete open e has its crossbar and lower curve; the following s has its own upper and lower curves, beginning early and overlapping the e. Both letters remain readable. Their typing order and any correction state remain unresolved, so the existing local uncertainty and overlap are retained.',
'B05':'The crop shows the large open left curve, inner oval with a low leftward tail, long vertical, rightward sweep and small right terminal loop, together with a detached short upright and the separate dot preceding the lower flourish. The blind paths preserve additional short interruptions in the tall stem and the narrow upper loop, and the gap before the right upturn. Those observed breaks are adopted. The pale grey spot beside the left curve remains unassigned. The letter sequence remains unresolved.'}
choices=[]
for b in ['B01','B02','B03','B05']:
 c=dict(box=b,choice='literal' if b=='B05' else 'first',changed=b=='B05',evidence=evidence[b],confidence='medium' if b in ('B03','B05') else 'high')
 if b=='B05': c['final']=signature
 choices.append(c)
for ch in report['changes']:
 if ch['id']==p+'-02':
  ch['final']=signature;ch['evidence']+=' Blind audit: '+evidence['B05'];ch['crop']=p+'_second_B05.png';ch['box']=[894,1723,1047,1846]
for d in report['decisions']:
 if d['id']=='M0108':
  d['reading']=signature;d['evidence']+=' Blind audit confirms the unresolved alphabetic interpretation and refines the observed gaps.';d['crop']=p+'_second_B05.png [894,1723,1047,1846]'
for d in report['doubts']:
 if d['reading']==f['B05']:d['reading']=signature;d['reason']+=' Blind audit preserves the further short interruptions in the vertical and upper loop.'
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(root/'work'/f'{p}_audit_choices.json').write_text(json.dumps(dict(reader='audit_c',choices=choices),ensure_ascii=False,indent=2)+'\n')
stamp=datetime.now(timezone.utc).isoformat()
with (root/'work/root_views.tsv').open('a') as out:
 for b in range(1,7):out.write(f'{stamp}\t{p}_second_B{b:02d}.png\tRoot personally displayed and inspected the complete blind crop; all six read before adjudication.\n')
subprocess.run([sys.executable,str(root/'scripts/prepare_audit_decisions.py'),p],check=True)
subprocess.run([sys.executable,str(root/'scripts/record_audit.py'),p],check=True)
