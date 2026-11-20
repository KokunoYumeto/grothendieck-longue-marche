"""Final page audit: local proper-name diacritic and the body groupoid spelling."""
import json,subprocess,sys
from audit_support import load,replace_exact,commit,OUT
r,a,s=load(100)
ad=[]
for c in a['changes']:
    s=replace_exact(s,c['before'],c['after'])
    ad.append({'id':c['id'],'decision':'accepted','reading':c['after'],
        'evidence':c['scan_shows'],'crop':c['crop'],'confidence':c['confidence']})
c=a['changes'][0]
r['changes'].append({'id':'100-A01','place':c['place'],'c':c['c'],'h':c['h'],
    'final':c['after'],'c_changed':True,'h_changed':True,'category':'Words','kind':'misread word',
    'marked_in_H':False,'confidence':'medium','scan_shows':c['scan_shows'],
    'box':c['box'],'crop':c['crop'],'consequential':False,
    'math_note':'A retained disagreement at the visually preferred diacritic, not a demonstrated error excluding the witnesses’ umlaut. No mathematical consequence.'})
d=a['new_doubts'][0]
r['doubts'].append({'scan':100,'decision_id':'D100-audit-Teichmuller','place':d['place'],
    'reading':d['reading'],'alternatives':d['alternatives'],'confidence':'medium',
    'reason':d['reason'],'crop':d['crop']})
r['decisions'].append({'id':'D100-audit-Teichmuller','cote':'142','scan':100,
    'decision':'undecided','reading':d['reading'],'what_the_ink_shows':d['reason'],
    'crop':d['crop'],'confidence':'medium'})
c=a['changes'][1]
row=next(x for x in r['changes'] if x['id']=='100-19')
row.update(place='d’un groupoide after the inserted Theta',final=c['after'],c_changed=True,
    scan_shows='The phrase sits on the full-size body baseline, unlike the raised Theta. '+c['scan_shows'])
row['audit_history']='The same comparison place originally recorded only H’s insertion-state error. The full second reading adds the plain-i spelling against C and H to that existing place; it is not counted twice.'
row['math_note']='The baseline/state reading remains. One visible i point also corrects both witnesses’ diaeresis at this same noun; the crossed marginal noun remains separately doubtful.'
r['hand_log'].extend(a['hand_log_additions'])
r['notes'].extend([
    'The full second reading localizes the proper-name uncertainty to its u-mark: one connected short dark arch favors û, while ü remains possible as a joined gesture. The transcription explicitly retains both. The main reader independently inspected the first focused crop; familiar spelling is not used to supply two dots.',
    'The body noun after the inserted Theta is groupoide, with one isolated i point immediately before d. A more distant round mark belongs earlier in the word and is not another dot over i. This updates existing comparison 100-19 while preserving its baseline-versus-insertion finding; no second count is made for that same place. The crossed marginal noun remains independently doubtful.',
    'A preliminary audit message mistakenly reported a missing comma after algébriques. Direct comparison shows that both the supplied consolidated page and its root review file already contained algébriques, qui. Auditor and main reader confirm the comma in the existing marginal crop; no comma edit or witness-error count was made.',
    'All 40 inherited comparisons, 20 assigned marks, four inherited supplementary decisions, seven certainty entries and 12 inventory elements were reviewed. All nine previous doubts remain, plus the newly explicit proper-name diacritic doubt. The correct source boxes were used for the historical mislocated trial-crop loci. No missing element or new mathematical check event.'
])
p=OUT/'documentation/root_view_ledger.json';j=json.loads(p.read_text())
crop='crops/scan100_audit_teichmuller.jpg'
if crop not in j['100']['crops_seen']:j['100']['crops_seen'].append(crop)
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
p=OUT/'documentation/notation_audit_updates.json';j=json.loads(p.read_text())
x=next(x for x in j if x.get('sign','').startswith('connait;'))
x['pages']='082, 085–086, 088, 093, 096, 098–100'
x['evidence']+=' The body groupoide on 100 has one isolated i point before d; the earlier round stroke is farther left in the word and cannot serve as its second dot. The doubtful crossed marginal noun stays separate.'
j.append({'sign':r'Teichm\unsure{û|ü}ller','reading':'A single joined u-mark favors circumflex; a joined umlaut remains possible.',
    'pages':'100','evidence':'The detached short dark arch has a raised middle and no two separated points. The familiar proper-name spelling does not settle its graphic form. Both auditor and main reader independently inspected the saved first crop; this remains a local explicit doubt.'})
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(OUT/'scripts/canonical_notation.py')],check=True)
commit(100,r,a,s,
    'Complete independent second reading by reader_b. All 40 inherited comparisons, 20 assigned marks, four supplementary decisions, seven certainty entries and 12 inventory elements were reviewed. Main reader independently inspected the new proper-name crop and reused the body-noun crop. The proper name retains a new circumflex/umlaut doubt; the body groupoide updates existing 100-19 without another place count. The supposed missing marginal comma was a preliminary misreport and is confirmed unchanged. Nine prior doubts plus the new diacritic doubt remain. No missing element or new mathematical check event.',ad)
