"""Explicit final record/syntax repairs; no original reading file is modified."""
from pathlib import Path
import json,copy
from datetime import datetime,timezone
W=Path(__file__).resolve().parents[1];stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');events=[]
def report(p):return json.loads((W/'reports'/f'{p}.json').read_text())
def save(p,r):(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
for p,old,new,reason in [
 ('151_scan040',r'\unsure{V|\mathcal V|Z}^*_{z,Z}',r'{\unsure{V|\mathcal V|Z}}^*_{z,Z}','Group the uncertain atom, whose macro already adds a question-mark superscript, before applying the written star.'),
 ('151_scan056',r'\uuline{$\alpha(\unsure{0|\omega})=0$}',r'\text{\uuline{$\alpha(\unsure{0|\omega})=0$}}','Make text-mode ulem wrapping explicit inside the displayed formula.'),
 ('151_scan058',r'\uline{$k$}',r'\text{\uline{$k$}}','Make text-mode ulem wrapping explicit in the displayed union index.'),
 ('151_scan058',r'\uline{$\mathcal{V}_{i,i}=\mathcal{V}_{i,i}^*=X_i^*$}',r'\text{\uline{$\mathcal{V}_{i,i}=\mathcal{V}_{i,i}^*=X_i^*$}}','Make text-mode ulem wrapping explicit for the last displayed equality chain.')]:
 f=W/'pages'/f'{p}.tex';s=f.read_text();assert s.count(old)==1,(p,old);f.write_text(s.replace(old,new));events.append({'page':p,'kind':'syntax only','old':old,'new':new,'reason':reason})
# Two distinct disk labels are two physical alphabet occurrences.
p='151_scan039';r=report(p);rows=[]
for q in r['changes']:
 if q['id']!='r08a':rows.append(q);continue
 r.setdefault('historical_grouped_rows',[]).append(copy.deepcopy(q))
 for ident,where,star in [('r08a','upper-left','^*'),('r08a2','upper-right','')]:
  v=copy.deepcopy(q);v.update(id=ident,place=f'diagram (23), {where} disk alphabet',c=r'\mathbb D'+star+r'_{\infty}',h='D'+star+r'_{\infty}',final=r'\mathbb D'+star+r'_{\infty}',evidence=f'The {where} D has two closely spaced upright strokes at the left of a separate rounded bowl. '+('Its star is visibly raised above this object. ' if star else 'This disk has no star. ')+'The small infinity subscript has paired loops. The already reviewed shared diagram crop supports this separate physical occurrence.');rows.append(v)
r['changes']=rows;save(p,r);events.append({'page':p,'kind':'physical-place accounting','old_ids':['r08a'],'new_ids':['r08a','r08a2'],'delta_c':0,'delta_h':1,'reason':'Separate the two already reviewed disk alphabets; no transcription change.'})
# Opening and closing quote pairs are separate endpoints; the noun already has r21.
p='151_scan042';r=report(p);rows=[]
for q in r['changes']:
 if q['id']!='r18a':rows.append(q);continue
 r.setdefault('historical_grouped_rows',[]).append(copy.deepcopy(q))
 for ident,where,c,h in [('r18a','opening','``','«'),('r18a2','closing',"''",'»')]:
  v=copy.deepcopy(q);v.update(id=ident,place=f'{where} quotation pair around construction noun',c=c,h=h,final=c,evidence=f'The {where} pair consists of two short raised near-vertical straight strokes, not a guillemet. The same already reviewed crop shows this endpoint separately. The noun reading is accounted for only in r21.');rows.append(v)
r['changes']=rows
for i,n in enumerate(r['notes']):
 if n.startswith('scan042.N12'):r['notes'][i]=n+' The final quote-endpoint rows r18a/r18a2 describe marks only; r21 accounts for the noun.'
save(p,r);events.append({'page':p,'kind':'physical-place accounting','old_ids':['r18a'],'new_ids':['r18a','r18a2'],'delta_c':0,'delta_h':1,'reason':'Separate the two quote endpoints; exclude the separately counted noun from their scope.'})
# Accent and placement describe one def annotation, counted once.
p='151_scan048';r=report(p);r.setdefault('historical_grouped_rows',[]).extend(copy.deepcopy(q) for q in r['changes'] if q['id'] in ['r14','r15'])
r['changes']=[q for q in r['changes'] if q['id']!='r15']
for q in r['changes']:
 if q['id']=='r14':q.update(place='display (11), spelling and placement of the definition annotation',c=r'\overset{\mathrm{def}}{=}',h=r'\underset{\text{déf}}{=}',final=r'\overset{\mathrm{def}}{=}',evidence='One d-e-f annotation is written above the two equality bars, with its f descender approaching them. No independent accent stands above the small e. Both its unaccented spelling and its position above equality differ from H; these are two properties of one physical annotation and are counted once.',kind='insertion or placement',error_category=6)
save(p,r);events.append({'page':p,'kind':'physical-place accounting','old_ids':['r14','r15'],'new_ids':['r14'],'delta_c':0,'delta_h':-1,'reason':'Merge spelling/placement of one written definition annotation; original row evidence is retained historically.'})
# A resolved word choice is not a remaining doubt.
p='151_scan049';r=report(p);resolved=[q for q in r['doubts'] if q.get('status')=='resolved first at medium'];assert len(resolved)==1;r.setdefault('resolved_doubt_history',[]).extend(resolved);r['doubts']=[q for q in r['doubts'] if q not in resolved];save(p,r);events.append({'page':p,'kind':'remaining-doubt scope','place':resolved[0]['place'],'reason':'Retain the resolved first reading in its decision and historical record, not in the remaining-doubts table.'})
# Fix an ambiguity in the account of the two independent encodings of the same drawing.
p='151_scan059';r=report(p);r['notes']=[n.replace('The second drawing omits a visible small upper dot; the first drawing retains it.','The independent second reader’s encoding of the large drawing omits a visible small upper dot; the retained first encoding includes it.') for n in r['notes']];save(p,r)
# New abbreviation alternatives remain expansions only in the explanatory list.
p='151_scan060';r=report(p)
for a in r.get('abbreviations',[]):
 if a['form']=='succ.':a['form']=r'\unsure{succ.|success.}';a['expansion']='successeur; both abbreviated readings remain possible in the text'
r.setdefault('abbreviations',[]).append({'form':r'\unsure{topos|topo}','expansion':'topos, with the presence of final s uncertain; no expansion supplied in the text'})
save(p,r)
(W/'audit/final_record_repairs.json').write_text(json.dumps({'utc':stamp,'events':events,'original_first_second_and_boxes':'unchanged','tex_compilation':'not performed'},ensure_ascii=False,indent=2)+'\n')
with (W/'progress.log').open('a') as f:f.write('final record reconciliation '+stamp+': physical-place count scope and remaining doubts corrected; four LaTeX-only grouping/mode repairs, no ink-reading changes; no TeX compilation\n')
print('Applied',len(events),'documented final record/syntax repairs.')
