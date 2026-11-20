from pathlib import Path
from datetime import datetime,timezone
import json
from build_deliverables import build
R=Path(__file__).resolve().parents[1];key='143_scan009'
p=R/'pages'/f'{key}.tex';text=p.read_text()
before=r"\inserted{et $\mathcal G'_j$ le stab. de $j$ dans $\mathcal G'$}), compatible"
after=r"""\begin{tikzpicture}[baseline=(base.base)]
\node[anchor=base west,inner sep=0] (base) at (0,0) {), compatible};
\node[anchor=base west,inner sep=0] at (-.04,.58) {\inserted{et $\mathcal G'_j$ le stab. de $j$ dans $\mathcal G'$}};
\draw[line width=.3pt] (-.17,-.10) .. controls (-.20,.24) and (.08,.35) .. (.46,.34) .. controls (1.80,.18) and (4.48,.35) .. (5.20,.47) .. controls (5.63,.54) and (5.72,.69) .. (5.73,.84);
\end{tikzpicture}"""
assert text.count(before)==1
rp=R/'reviews'/f'{key}_accepted.json';r=json.loads(rp.read_text())
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
record={'time':now,'place':'Long curved guide beneath stabilizer insertion','before':before,'after':after,'crop':'crops/143_scan009_readerB_interline_stabilizer.png','box':[1095,405,1665,505],'reason':'The existing crop shows a long shallow curve beneath the whole inserted phrase, bending downward at the left toward the closing parenthesis and curving upward at the right. Both the first report and second-reader confirmation described it; the plain inserted wrapper did not reproduce it. Main re-inspected the same crop and adds the visible headless guide.'}
r.setdefault('post_audit_main_corrections',[]).append(record)
r['changes'].append({'place':record['place'],'C':'inserted stabilizer words; no explicit guide drawing','H':'interlinear stabilizer words; no explicit guide drawing','final':after,'against_C':True,'against_H':True,'kind':'drawing or diagram','ink':record['reason'],'confidence':'high','crop':record['crop'],'box':record['box'],'marked_in_H':False,'consequential':False})
element='E'+str(max(int(x['element'][1:]) for x in r['inventory'])+1).zfill(2)
r['inventory'].append({'sheet_kind':'text','hand':'his hand','element':element,'kind':'drawing','position':'beneath interlinear stabilizer phrase; curved attachment to closing parenthesis','first_words_or_objects':'long shallow guide with bent ends, no arrowhead','transcribed':'yes'})
assert len({x['element'] for x in r['inventory']})==len(r['inventory'])
r['notes'].append({'id':'143_scan009-main-guide-N1','text':'The main cross-page insertion review adds the long headless curved guide beneath the stabilizer insertion. Its wording and prime were already recorded; this change reproduces the source stroke and the attachment to the closing parenthesis, using the existing crop.'})
r['hand_log'].append({'habit':'A long shallow curve beneath an insertion specifies its attachment without being an underline or a map arrow.','places':'143_scan009, stabilizer insertion','scope':'One visible long curve with bent ends; no arrowhead is inferred.','misreadings':'C and H preserve the inserted words but do not explicitly reproduce this source guide.'})
p.write_text(text.replace(before,after));rp.write_text(json.dumps(r,ensure_ascii=False,indent=2))
(R/'reviews'/f'{key}_main_guide_supplement.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
print(build())
with (R/'progress.log').open('a') as f:f.write('scan 009 main insertion-guide supplement '+now+' cote 143; existing crop re-inspected\n')
