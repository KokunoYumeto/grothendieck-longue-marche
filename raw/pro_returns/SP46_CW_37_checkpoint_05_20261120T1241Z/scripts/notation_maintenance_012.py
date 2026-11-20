from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
O=Path(__file__).resolve().parents[1]
t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
files=list((O/'pages').glob('*.tex'))+[O/'SP46_CW_37_transcription.tex']
before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
p=O/'notation_review.json'; r=json.loads(p.read_text())
assert r['reviewed_through_scan']==76
r['reviewed_through_scan']=77; r['reviewed_utc']=t
for g in r['groups']:
    if g['group']=='Ruled Roman numerals':
        g['scans'].append(77)
        g['finding']+=' Scan 077 uses the same upper-and-lower-rule convention for its independently read VI, XXI, XXII and marginal XXIII. The crowded first VI/VII remains uncertain; the clear later VI does not settle it. The main reader viewed the retained first-numeral crop and separate crops of the clear groups.'
r['groups'].append({'group':'Braces and enclosed labels','scans':[53,77],'finding':'Curved grouping strokes and enclosing loops are drawn from their local paths. The upper brace of 077 has two lower return contours, whereas its lower brace has one. Neither that retracing nor the enclosing SGA 7 loop is converted to a textual deletion. All 077 shapes were personally inspected in the retained crops.'})
r['remaining_scope']='Scan 085 is being read; scans 086–098 follow in the prescribed page list. Extend this review through all 25 pages before freezing.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=O/'legibility.txt'; s=p.read_text().replace('Provisional assessment through scan 076;','Provisional assessment through scan 077;').replace('On the three fully transcribed H pages reviewed so far','On the four fully transcribed H pages reviewed so far')
s+='\nThe handwritten planning list on 077 illustrates the limits of resolving joined word endings: appendice, torsion, cohomologie and cristalline can be read, while relation/relations and Commentaires/Commentaire retain genuine local ambiguity. Its retraced first Roman group and faint accent trace also remain uncertain. The record separates the writer’s question marks from editorial doubts.\n'
p.write_text(s)
p=O/'global_check_events.json'; events=json.loads(p.read_text()); events.append(dict(statement_id='NOTATION-REVIEW-THROUGH-077',date=t,who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='used and rechecked in this run',outcome='Extended the cumulative notation comparison through twelve committed pages from completed independent visual returns and the main-reader crop adjudications. Compared ruled Roman references and graphical grouping strokes without reopening or recropping settled places. All twelve page files and combined-source bytes remained unchanged; no mathematical proof was performed.')); p.write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
assert before=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
with (O/'progress.log').open('a') as f:f.write(f'notation review through scan 077 {t}; 12 page files and combined source hashes unchanged\n')
print('Notation review extended through 077; transcription bytes unchanged.')
