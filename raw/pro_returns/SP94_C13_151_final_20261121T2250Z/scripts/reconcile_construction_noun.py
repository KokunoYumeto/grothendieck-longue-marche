"""Post-blind cross-page ink comparison; original first/second readings stay untouched."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json
W=Path(__file__).resolve().parents[1];stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');log=[]
for n,newid,old,new,crop,box,place in [
(42,'r21',r'\unsure{pièces|pierres|pavés}',r'\unsure{pierres|pièces|pavés}','crops/151_scan042_r18.jpg',[306,2042,1642,2278],'final list, quoted construction noun'),
(44,'r34',r'\unsure{desdites|des dites} pièces.',r'\unsure{desdites|des dites} \unsure{pierres|pièces}.','crops/151_scan044_b12.jpg',[310,1424,891,1522],'main line 12, noun after desdites')]:
 p=f'151_scan{n:03d}';rp=W/'reports'/f'{p}.json';r=json.loads(rp.read_text());tp=W/'pages'/f'{p}.tex';t=tp.read_text();assert old in t;t=t.replace(old,new)
 ev=('Cross-page ink comparison with scan040 both occurrences, scan044 first quoted noun and scan058 both occurrences: the low angular double shoulders after pi/e correspond to this hand\'s paired r forms, clearly separated in scan058. No separate grave accent is secure. The local ink admits pierres, now preferred consistently; pièces remains possible.' if n==44 else 'Cross-page ink comparison with scan040, scan044 and the clearer paired r forms of scan058: the compressed middle low turns are compatible with the same pierres word. No independent grave accent is secure. Prefer pierres consistently, while retaining pièces and the blind pavés proposal because this local word is more compressed.')
 final=r'\unsure{pierres|pièces}' if n==44 else new
 r['changes'].append({'id':newid,'place':place,'c':'pièces','h':'pièces','final':final,'evidence':ev,'confidence':'medium','kind':'misread word','error_category':2,'diff_c':True,'diff_h':True,'marked_h':False,'crop':crop,'box':box,'consequential':''})
 if n==42:
  for q in r['doubts']:
   if q.get('reading')=='pièces':q.update(reading='pierres',alternatives='pièces; pavés',reason=ev)
  for q in r['changes']:
   if q['id']=='r18a':q['final']=q['final'].replace(old,new)
  for q in r.get('second_changes',[]):
   if q['box_id']=='b18':q['final']=q['final'].replace(old,new);q['evidence']+=' Final cross-page review: '+ev
  r['notes'].append('scan042.N12. Final cross-page ink comparison gives pierres priority in the compressed quoted noun, consistently with scans040/044/058; pièces and pavés remain explicit local alternatives. The earlier blind choice is preserved in its documentary record and superseded in the final page and changes table.')
 else:
  r['doubts'].append({'place':place,'reading':'pierres','alternatives':'pièces','confidence':'medium','reason':ev})
  r['notes'].append('scan044.N12. A final cross-page comparison also reopens the second noun after desdites: its two angular low shoulders match the first quoted occurrence and the clearer rr forms on scan058. Both now prefer pierres with pièces as alternative. First and blind readers had agreed on pièces at this second occurrence; that agreement did not settle it. This later notation correction is separate from the completed blind-audit count.')
 r['hand'].append({'habit':'The paired r strokes in pierres can collapse to low angular shoulders and be mistaken for c in pièces.','evidence':ev,'every_occurrence':'Compared across both scan040 and scan044 occurrences, scan042 and both scan058 occurrences; later occurrences are retained for final review.','misread_places':'Both witnesses have pièces at this local occurrence.'})
 tp.write_text(t);rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');log.append({'page':p,'old':old,'final':new,'evidence':ev,'crop':crop,'box':box,'utc':stamp})
(W/'audit'/'construction_noun_consistency.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
with (W/'progress.log').open('a') as f:f.write('notation review '+stamp+': compared construction noun on scans040,042,044,058; revised preferred noun on042 and second occurrence on044; original blind readings unchanged\n')
with (W/'notation.md').open('a') as f:f.write('\n## Cross-page construction noun review\n\nThe compressed paired r forms in pierres were compared on scans040,042,044 and058. The earlier three pages now consistently prefer pierres while retaining local alternatives; the two clearer scan058 forms separate the r strokes. This is an ink comparison, not replacement from the building metaphor. See audit/construction_noun_consistency.json.\n')
