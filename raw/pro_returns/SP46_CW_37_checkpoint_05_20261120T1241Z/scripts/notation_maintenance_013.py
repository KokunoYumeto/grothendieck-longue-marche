from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path(__file__).resolve().parents[1]
t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
files=list((O/'pages').glob('*.tex'))+[O/'SP46_CW_37_transcription.tex']
before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
p=O/'notation_review.json';r=json.loads(p.read_text());assert r['reviewed_through_scan']==77
r['reviewed_through_scan']=85;r['reviewed_utc']=t
for g in r['groups']:
    if g['group']=='Detached marginal points':
        g['scans'].append(85)
        g['finding']+=' On 085, the detached low dash belongs to a local two-component marginal configuration with a long upper hook. The main-viewed crop does not fix its textual function; its shape and relative placement are drawn rather than normalized to a question mark or colon.'
r['groups'].append({'group':'Undistinguished typed O/0 forms','scans':[54,85],'finding':'The circular character in an EGA reference on 054 and the chapter oval on 085 each retain O/0 alternatives where their local outline does not distinguish letter from digit. Chapter-number expectation does not determine the 085 glyph. These are separate local uncertainties, preserved under the same notation convention.'})
r['groups'].append({'group':'Overprinted letters and duplicate impressions','scans':[69,70,71,85],'finding':'Recoverable underlying letters use deleted immediately before the replacement; unresolved identities remain unsure inside that state. The 085 r/p pair follows this convention. Its terminal pale s is separately uncertain in typing state: single repeated impression, corrected underprint, or closely overlapping live letters. The graphic presence is preserved without assuming a correction operation from a familiar word.'})
r['remaining_scope']='Scan 086 is being read; scans 087–098 follow in the prescribed page list. Extend this review through all 25 pages before freezing.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=O/'legibility.txt';s=p.read_text().replace('Provisional assessment through scan 077;','Provisional assessment through scan 085;')
s+='\nThe contents page on 085 is generally legible. Its main vulnerabilities are the interpretation of overlaid typing and a sparse marginal graphic. The underlying r remains partly merged with its replacement, and an extra pale s impression is physically visible without a securely established typing state. Those distinctions are retained instead of being reduced to ordinary spelling.\n';p.write_text(s)
p=O/'global_check_events.json';ev=json.loads(p.read_text())
ev.append(dict(statement_id='NOTATION-REVIEW-THROUGH-085',date=t,who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='used and rechecked in this run',outcome='Extended cumulative notation comparison through thirteen committed pages from completed independent visual reports and the main-viewed retained crops. Compared typed oval uncertainty, marginal mark geometry and overprint state. Thirteen page files and combined source were unchanged. This was documentary notation review, not mathematical proof.'))
for n in [77,85]:
    assert all(not json.loads((O/f'readers/scan{n:03}/{a}/report.json').read_text())['check_events'] for a in 'ABC')
ev.append(dict(statement_id='CHECK-EVENT-COVERAGE-THROUGH-085',date=t,who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='used and rechecked in this run',outcome='Extended the reader-event coverage audit beyond scan 076 to all three reports on each of 077 and 085. All six check_events arrays are empty, consistently with their reports of no mathematical proof or computation. No mathematical event was added merely for reading headings or claims.'))
p.write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n')
assert before=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
with (O/'progress.log').open('a') as f:f.write(f'notation and check-event coverage review through scan 085 {t}; 13 page files and combined source hashes unchanged\n')
print('Notation and event coverage reviewed through 085; source hashes unchanged.')
