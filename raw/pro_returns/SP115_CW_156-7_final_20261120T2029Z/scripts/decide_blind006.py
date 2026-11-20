#!/usr/bin/env python3
"""Root's explicit decisions after direct display of all 47 differing blind crops."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parents[1]; stem='H156-01_156-7_scan006'
bs={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{stem}_boxes.tsv').open(),delimiter='\t')}
E=dict(re.findall(r'^- (B\d{3}): (.*)$',(R/'second'/f'{stem}_root_observations.md').read_text(),re.M))
E['B009']='Retain At_M2 with underline across both letters; the 2 has a curved shoulder and flat base. Only text/math wrappers differ.'
E['B010']='Retain At_M3 with underline across both letters; the 3 has two curved lobes. Only text/math wrappers differ.'
ids={'B008':['006-A01'],'B011':['006-A02'],'B014':['006-A03'],'B019':['006-A04'],'B021':['006-A05'],'B022':['006-A05'],'B025':['006-A02'],'B029':['006-A06','006-A07'],'B033':['006-A08'],'B035':['006-A09','006-A10','006-A11','006-A12'],'B036':['006-A10','006-A11'],'B037':['006-A11'],'B038':['006-A12'],'B041':['006-A13'],'B044':['006-A01']}
cfg={'reader':'reader_c (GPT-6 Astra Pro; effort not exposed)','patches':[],'change_updates':{},'new_changes':[],'remove_doubt_places':['Upright after relations sentence','Opening tuple, relation word','At 3, deleted small x','Definition arrow label','At 5 marginal note, crossed words'],'new_doubts':[],'boxes':{}}
def patch(a,b):cfg['patches'].append({'old':a,'new':b,'count':1})
patch(r'\text{\uline{At}}_{M}\,1',r'\text{\uline{A}t}_{M}\,1')
patch(r'\unsure{1}', '1')
patch(r'\unsure{relation|rel\textsuperscript{tion}} réflexive',r'\unsure{rel b.|rel\textsuperscript{tion}}, réflexive')
patch(r'compatibles (pour $',r'compatibles (\unsure{pour|p. r.} $')
patch(r'\forall\deleted{\unsure{x}}X',r'\forall\deleted{\unsure{x|de}}X')
arch=r'\tikz[x=.6em,y=.6em]{\draw (0,0)..controls(.6,.45)and(1.5,.58)..(2,.35); \draw (2.03,.57)--(2.3,.57);}\enspace '
patch(r'\margin{Axiome de la plus petite strate',r'\margin{'+arch+r'Axiome de \unsure{la|le} plus petite strate')
patch(r'\unsure{dfn|defn|défn|déf}',r'\unsure{dfn|df|defn|défn|déf}')
elbow=r'\tikz[x=.6em,y=.6em]{\draw (0,0)--(.25,1.15)..controls(.32,1.45)and(.55,1.45)..(.8,1.48)--(3.3,1.62); \draw (3.3,1.62)--(3.52,1.77)--(3.68,1.58)--(3.43,1.43)--cycle;} '
patch(r'\inserted{Si $G,H$,} \deleted{\illegible{2}}',r'\inserted{Si $G,H$,} '+elbow+r'\deleted{\unsure{Axiome}} :')
patch(r'(\uline{Critère du raffinement \unsure{extrinsèq.|intrinsèq.} de figures})',r'(\uline{Critère du raffinement \unsure{extrinsèq.|intrinsèq.}} de \uline{figures})')
longline=r'\tikz[x=.6em,y=.6em]{\draw (0,0)--(5,-.25); \draw (.45,.12)--(.12,0)--(.4,-.12);}\enspace '
patch(r'\margin{\uline{Transitivité}',r'\margin{'+longline+r'\uline{Transitivité}')
for b,e in E.items():cfg['boxes'][b]={'crop':f'crops/second_scan006_{b}.png','box_coords':bs[b],'decision':'revise or mark uncertainty' if b in ids else 'retain after ink comparison','evidence':e,'changed_place_ids':ids.get(b,[])}
def upd(i,b,**kw):cfg['change_updates'][i]={'crop':cfg['boxes'][b]['crop'],'box':bs[b],**kw}
upd('006-019','B011',final='1',scan_shows=E['B011'],confidence='high') if False else None
upd('006-19','B011',final='1',scan_shows=E['B011'],confidence='high')
upd('006-18','B022',final=r'\forall\deleted{\unsure{x|de}}X',scan_shows=E['B022'],confidence='low')
upd('006-29','B033',final=r'\unsure{dfn|df|defn|défn|déf}',scan_shows=E['B033'],confidence='low')
upd('006-38','B037',final=r'\deleted{\unsure{Axiome}}',scan_shows=E['B037'],confidence='low',against_C=True,against_H=True,kind=r'readable ink left as \ill{}')
upd('006-79','B035',final=r'\uline{Critère du raffinement \unsure{extrinsèq.|intrinsèq.}} de \uline{figures}',scan_shows=E['B035'],confidence='medium',against_C=True)
upd('006-84','B044',final=r'\text{\uline{A}t}_M 1',scan_shows=E['B044'],confidence='high',against_C=True)
def new(i,place,b,final,kind,confidence='high',C='(omitted)',H='(omitted)'):
 cfg['new_changes'].append({'id':i,'place':place,'C':C,'H':H,'final':final,'scan_shows':E[b],'confidence':confidence,'kind':kind,'crop':cfg['boxes'][b]['crop'],'box':bs[b],'against_C':True,'against_H':True,'marked_in_H':False,'consequential':False})
new('006-87','opening tuple, abbreviated relation label and following comma','B014',r'\unsure{rel b.|rel\textsuperscript{tion}},','abbreviation expanded or spelling modernised','low','relation','relation')
new('006-88','short arch and detached dash above Axiome in the minimum-stratum margin','B029',arch,'drawing or diagram')
new('006-89','thin elbow connector ending in angular loop beside Si G,H','B035',elbow,'drawing or diagram')
new('006-90','colon after the cancelled row in the At5 margin','B036',':','omission')
new('006-91','long connector above Transitivité','B041',longline,'drawing or diagram','medium')
for place,reading,alts,b in [
 ('Opening tuple, abbreviated relation word','rel b.',[r'rel\textsuperscript{tion}'],'B014'),
 ('Initial left margin, preposition before compatibility symbol','pour',['p. r.'],'B019'),
 ('At 3, deleted small group','x',['de'],'B022'),
 ('Minimum-stratum marginal note, article before plus','la',['le'],'B029'),
 ('Definition arrow label','dfn',['df','defn','défn','déf'],'B033'),
 ('At 5 marginal note, crossed word','Axiome',['underlying word uncertain under heavy hatching'],'B037')]:cfg['new_doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':'low','reason':E[b]})
# Explicit final excerpts where the frozen first excerpt was partial or empty.
initial=(R/'second'/f'{stem}_initial.tex').read_text()
start=initial.index(r'\text{\uline{At}}_{M}\,3')
end=initial.index(r'\end{aligned}',start)
cfg['boxes']['B047']['final']=initial[start:end].strip()
cfg['boxes']['B008']['final']=r'\text{\uline{A}t}_M 1'
cfg['boxes']['B036']['final']=r'\inserted{Si $G,H$,} '+elbow+r'\deleted{\unsure{Axiome}} :'
cfg['boxes']['B037']['final']=r'\deleted{\unsure{Axiome}}'
cfg['boxes']['B038']['final']=r'de \uline{figures})'
(R/'second'/f'{stem}_decisions.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
print(len(E),'decisions',len(set(x for a in ids.values() for x in a)),'unique changed places')
