from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path(__file__).resolve().parents[1]
t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
files=list((O/'pages').glob('*.tex'))+[O/'SP46_CW_37_transcription.tex']
before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
p=O/'notation_review.json';r=json.loads(p.read_text());assert r['reviewed_through_scan']==85
r['reviewed_through_scan']=86;r['reviewed_utc']=t
for g in r['groups']:
    if g['group']=='Detached marginal points':
        g['scans'].append(86)
        g['finding']+=' The 086 lowered oval beside the normal period and the raised diagonal pair above a leader line are individually reproduced from the main-viewed crops. Their smaller solid forms remain distinct from the hollow typewriter leader points. The pale channel cutting a leader point is a surface disruption and is excluded after crop comparison.'
    if g['group']=='Overprinted letters and duplicate impressions':
        g['scans'].append(86)
        g['finding']+=' On 086, the same deletion-before-replacement convention preserves six overtyped positions. The crowded i position retains l/t/j, with a low residual contour whose connection to an older j is possible but unestablished. The contour is documented as part of that same correction cluster.'
r['groups'].append({'group':'Contents headings, number fields and leaders','scans':[85,86],'finding':'Ordinary section signs and decimal number fields remain typed text, with observed spacing and punctuation. Leaders are present or absent entry by entry: the replacement 2.4 on 085 and entries 3.10 and 6.8 on 086 do not receive supplied leaders. Both page fields retain their observed flanking dashes. Their manuscript page numbers are kept in supplied scan order.'})
r['remaining_scope']='Scan 087 is being read; scans 088–098 follow in the prescribed page list. Extend this review through all 25 pages before freezing.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=O/'legibility.txt';s=p.read_text().replace('Provisional assessment through scan 085;','Provisional assessment through scan 086;')
s+='\nOn 086, small typewriter underprints remain less secure than the live words. A residual lower foot allows an additional j candidate without settling the letter. The vertical pale channel that cuts a printed leader dot is distinguished from detached dark marks and is not transcribed as writing.\n';p.write_text(s)
assert all(not json.loads((O/f'readers/scan086/{a}/report.json').read_text())['check_events'] for a in 'ABC')
p=O/'global_check_events.json';ev=json.loads(p.read_text());ev.append(dict(statement_id='NOTATION-AND-EVENT-REVIEW-THROUGH-086',date=t,who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='used and rechecked in this run',outcome='Extended cumulative notation comparison through fourteen committed pages using the completed independent visual records and main-viewed crops, including the distinction between surface disruption and unassigned dark shapes. Checked all three 086 check_events arrays: none claims mathematical proof or computation. Fourteen page files and the combined fragment remained byte-identical.'))
p.write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n')
assert before=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
with (O/'progress.log').open('a') as f:f.write(f'notation and check-event coverage review through scan 086 {t}; 14 page files and combined source hashes unchanged\n')
print('Notation and event coverage reviewed through 086; source hashes unchanged.')
