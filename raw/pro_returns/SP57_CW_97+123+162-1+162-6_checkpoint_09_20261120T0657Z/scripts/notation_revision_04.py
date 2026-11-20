"""Unify the recurring closed crossed-oval form after existing-crop comparison."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
glyph=r'\begin{tikzpicture}[baseline=-.15ex,x=1ex,y=1ex]\draw[line width=.35pt] (.42,.53) ellipse (.32 and .46);\draw[line width=.35pt] (-.02,-.16)--(.84,1.27);\end{tikzpicture}'
configs=[
 ('C123-01_123_scan018',r'\varnothing',3,['D21','D28','D35'],['readers/C123-01_123_scan018/R1/crops/09_filtration_symbol_il_est.png','readers/C123-01_123_scan018/R1/crops/11_ou_encore_symbol_leader.png','readers/C123-01_123_scan018/R1/crops/14_display.png']),
 ('C123-01_123_scan019',r'\varnothing',3,['R3-D06','R3-D07','R3-D13'],['readers/C123-01_123_scan019/R1/crops/04_deligne_map.jpg','readers/C123-01_123_scan019/R3/crops/07_main_diagram_bottom.png','readers/C123-01_123_scan019/R1/crops/23_paragraph_par.jpg']),
 ('C123-02_123_scan022',r'\phi',2,['D12','D15'],['readers/C123-02_123_scan022/R1/07_first_count_W.png','readers/C123-02_123_scan022/R1/08_insertions_euler.png'])]
receipt=[]
for stem,old,count,ids,crops in configs:
 p=O/'pages'/(stem+'.tex');rp=O/'decisions'/(stem+'.json');r=json.loads(rp.read_text());s=p.read_text()
 assert s.count(old)==count,(stem,s.count(old))
 assert not any(z.get('revision')=='04' for z in r.get('post_decision_revisions',[]))
 before=hashlib.sha256(p.read_bytes()).hexdigest();p.write_text(s.replace(old,glyph));after=hashlib.sha256(p.read_bytes()).hexdigest()
 for d in r['differences']:
  if d['id'] in ids:
   d['final']=d['final'].replace(old,glyph)
   d['evidence']+=' Cross-page notation review 04 compares this same closed oval/ascending crossing-shaft family on 123/018, 019 and 022. A literal common TikZ form now avoids choosing a semantic empty-set or Greek-letter label; the separate underline remains where observed. This is an encoding harmonization, not a new witness-reading locus.'
   d['readers']+=' Pre-freeze root review: replace the typographic label by the common physical drawing, without altering the recorded independent readings.'
 for q in r['c_doubts']:
  for k in ['decision']:
   if old in q.get(k,''):q[k]=q[k].replace(old,glyph)
 for x in r['inventory']:
  if old in x.get('first_words_or_objects',''):x['first_words_or_objects']=x['first_words_or_objects'].replace(old,'closed oval with ascending crossing shaft')
  if stem.endswith('scan022') and x.get('element') in ['First Euler phi fill','Second Euler phi fill']:
   x['first_words_or_objects']='closed oval with ascending crossing shaft; no underline'
 r['notes']+='\nPre-freeze notation review 04 uses the same literal closed oval with an ascending crossing shaft for this recurring handwritten family across 123/018, 019 and 022. Underlines are retained only on 018/019. This reconciles the previous typographic labels varnothing and phi without imposing an empty-set interpretation or changing the mathematical reading. The open looped footer varphi on 022 is different and remains unchanged. Existing crops only; no new crop or whole/half image view.\n'
 rev=dict(revision='04',date=now,loci=ids,old=old,new=glyph,occurrences=count,crops=crops,reason='Common physical glyph encoded identically across pages, with local underlines preserved; no new underlying reading/count.',sha256_before=before,sha256_after=after)
 r.setdefault('post_decision_revisions',[]).append(rev);rp.write_text(json.dumps(r,ensure_ascii=False,indent=2))
 receipt.append(dict(stem=stem,**rev))
 with (O/'progress.log').open('a') as f:f.write('notation revision 04 '+now+' '+stem+' '+str(count)+' recurring closed-crossed-oval forms; existing crops only; SHA256 '+before+' -> '+after+'; transcription not yet frozen\n')
np=O/'briefs/notation.md';s=np.read_text()
s=s.replace('Closed oval with a distinct diagonal slash and separate underline, resolved as `\\underline{\\varnothing}` in all three occurrences; this is a physical form, not an empty-set interpretation.','Closed oval with a distinct ascending crossing shaft and separate underline. Revision 04 uses a shared literal TikZ glyph on 123/018, 019 and 022; retain the underline on 018/019. No semantic empty-set interpretation is assigned.')
s=s.replace('Body symbols are closed crossed ovals, `\\phi`; footer symbol is open and looped with a descending stroke, `\\varphi`. Alphabet distinction is graphic, not semantic.','Body symbols are closed crossed ovals with an ascending shaft, now the same literal TikZ form as 123/018–019, without their underline. Footer symbol is open and looped with a descending stroke, `\\varphi`; it remains distinct. This is a graphic distinction, not a change to the stated indicatrix.')
s+='\n## Shared closed-crossed-oval encoding (revision 04)\n\nUse this literal glyph, with `\\underline{...}` only where a separate low rule is visible. It describes strokes without selecting an empty-set or Greek-letter semantic label. No new macro is introduced.\n\n```tex\n'+glyph+'\n```\n'
np.write_text(s)
pending=O/'decisions/notation_review_pending.md';pending.write_text(pending.read_text()+'\n## Completed revision 04\n\nAll eight existing crops for the three 123/018 forms, three 123/019 forms and two 123/022 body forms were compared. They share a closed oval crossed by an ascending shaft. A shared literal TikZ form replaces the inconsistent typographic labels, with underlines retained only where written. The open 123/022 footer varphi remains distinct. This encoding change does not create new reading loci or alter counts. Old/new hashes and evidence are recorded per page.\n')
with (O/'SP57_CW_97+123+162-1+162-6_workflow.md').open('a') as f:f.write('\n### Pre-freeze notation revision 04 — '+now+'\n\nEight existing local crops on 123/018, 019 and 022 were compared. The same physical closed oval with an ascending crossing shaft had been encoded varnothing on the first two pages and phi on the third. A shared literal TikZ drawing now preserves that family without a semantic glyph choice; the independently visible underlines remain on 018/019. The open footer varphi on 022 is distinct. No new crops were made, no image-recognition tool was used, and no underlying-reading difference or count was added for this representation change. Every changed page has before/after hashes in its decision record.\n')
(O/'decisions/notation_revision_04.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2))
print(json.dumps([{'stem':x['stem'],'before':x['sha256_before'],'after':x['sha256_after']} for x in receipt]))
