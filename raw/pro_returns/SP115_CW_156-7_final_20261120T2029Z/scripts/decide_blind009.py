#!/usr/bin/env python3
"""Root decisions after direct inspection of every differing blind crop of scan009."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parents[1];stem='H156-01_156-7_scan009'
bs={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{stem}_boxes.tsv').open(),delimiter='\t')}
E=dict(re.findall(r'^- (B\d{3}): (.*)$',(R/'second'/f'{stem}_root_observations.md').read_text(),re.M))
ids={'B003':['009-A01'],'B004':['009-A02','009-A03'],'B006':['009-A02','009-A03'],'B007':[f'009-A{i:02d}' for i in range(4,11)],'B009':['009-A11'],'B010':['009-A11'],'B012':['009-A12'],'B016':['009-A12'],'B024':['009-A13'],'B025':['009-A14','009-A15'],'B029':['009-A16','009-A17'],'B030':['009-A18']}
cfg={'reader':'reader_b (GPT-6 Astra Pro; effort not exposed)','patches':[],'change_updates':{},'new_changes':[],'remove_doubt_places':['NB first Z refinement','NB second Z refinement','NB final implication','Live axiom altered label','Live axiom separator','NB cancelled word'],'new_doubts':[],'boxes':{}}
def patch(a,b,count=1):cfg['patches'].append({'old':a,'new':b,'count':count})
patch(r'\inM',r'\in M')
patch(r'avec $X\deleted',r"avec $\unsure{X|X'}\deleted")
patch(r"\deleted{$Y'\ll Y\Longrightarrow X'\parallel Y'$}",r"\deleted{$Y'\ll Y\Longrightarrow X'\parallel\unsure{Y'|Y}$}")
patch(r"pour $Z\leq X,Y$)",r"pour $Z\leq X,Y$")
patch(r"Z\ll\unsure{X'|X},\,\unsure{Z'|Z}\ll\unsure{Y'|Y}",r"Z\ll X,\,Z\ll\unsure{Y'|Y}")
patch(r"Z\leq X'\parallel L\Longrightarrow Z\parallel L",r"Z\leq X'\parallel L\underset{\mathrm{At}}{\Longrightarrow}Z\parallel L")
patch(r'\deleted{\unsure{impossible}}',r"c'est \deleted{\unsure{impossible}}")
patch(r'\unsure{Z^{+}\leq L|Z+\leq L|Z\leq L}',r' Z^{+}\leq L')
patch(r'\deleted{\unsure{absurde}}',r'\unsure{\deleted{absurde}|absurde}')
graphic=r'\tikz[x=.45em,y=.45em]{\draw (0,0)--(4,0);\draw (3.4,.2)--(3.6,-10);\draw (1.4,-6.4)--(3.9,-8.7);}'
patch(r'car \uline{$Z\cap L=\phi$ !}}%',r'car \uline{$Z\cap L=\phi$ !}}%'+'\n% Connected thin upper, right-side and lower-oblique strokes crossing/bordering the NB note.\n'+r'\margin{'+graphic+'}')
patch(r'\deleted{$\unsure{L=\underset',r'\deleted{\unsure{avec} $\unsure{L=\underset')
oldstroke=r'\noindent\tikz[x=1em,y=1em]{\draw (0,.03) .. controls (2,.15) and (4,.18) .. (6,.12) .. controls (8,-.04) and (10,-.10) .. (11.1,-.08) .. controls (11.45,.55) and (11.55,.95) .. (12.2,1.18);}'
newstroke=oldstroke[:-1]+r'\draw (-.18,-.03)--(.95,1.32);}'
patch(oldstroke,newstroke)
patch('% Editing stroke beneath the preceding cancelled draft, with rising right end.','% Editing stroke beneath the preceding cancelled draft, with left oblique and rising right end.')
patch(r"At $\parallel$, et a fortiori",r"At $\unsure{\parallel|11}$, et a fortiori")
patch(r'\unsure{DD|CD|DC}',r'DD')
patch(r'\unsure{o|et|,}',r'\&')
patch(r'\uline{Cor. Main}',r'\uline{\unsure{Cor. Main|Corollaire}}',2)
patch("1 \\quad la ``propriété''",r"1 \quad \unsure{la|le} ``propriété''")
for b,e in E.items():cfg['boxes'][b]={'crop':f'crops/second_scan009_{b}.png','box_coords':bs[b],'decision':'revise or mark uncertainty' if b in ids else 'retain after ink comparison','evidence':e,'changed_place_ids':ids.get(b,[])}
def upd(i,b,**kw):cfg['change_updates'][i]={'crop':cfg['boxes'][b]['crop'],'box':bs[b],**kw}
upd('009-08','B006',final=r"(i.e. $X'\parallel Z$ pour $Z\leq X,Y$",scan_shows=E['B006'],confidence='high',against_C=True)
upd('009-15','B007',final=r"Z\ll X,\,Z\ll\unsure{Y'|Y}",scan_shows=E['B007'],confidence='low')
upd('009-20','B007',final=r'\Longrightarrow Z^{+}\leq L',scan_shows=E['B007'],confidence='high')
upd('009-21','B007',final=r'\unsure{\deleted{absurde}|absurde}',scan_shows=E['B007'],confidence='low')
upd('009-30','B010',final=r'\deleted{\unsure{avec} $\unsure{L=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z}$}',scan_shows=E['B010'],confidence='low',against_C=True)
upd('009-40','B016',final='% Editing stroke beneath the preceding cancelled draft, with left oblique and rising right end.\n'+newstroke,scan_shows=E['B016'],confidence='high')
upd('009-61','B024',final=r'At $\unsure{\parallel|11}$',scan_shows=E['B024'],confidence='low')
upd('009-65','B025',final='DD',scan_shows=E['B025'],confidence='high')
upd('009-67','B025',final=r'\&',scan_shows=E['B025'],confidence='medium',against_C=True,against_H=True)
upd('009-73','B029',final=r'\uline{\unsure{Cor. Main|Corollaire}} 1',scan_shows=E['B029'],confidence='low')
upd('009-74','B029',final=r"\unsure{la|le} ``propriété'' ci dessus",scan_shows=E['B029'],confidence='low')
upd('009-75','B030',final=r'\uline{\unsure{Cor. Main|Corollaire}} 2',scan_shows=E['B030'],confidence='low')
review=json.loads((R/'review'/'scan009_final.json').read_text())
for id in ['009-83','009-84']:
 old=next(x['final'] for x in review['changes'] if x['id']==id);new=old
 for p in cfg['patches']:new=new.replace(p['old'],p['new'])
 cfg['change_updates'].setdefault(id,{})['final']=new
for i,place,c,h,final,b,kind,confidence in [
 ('009-87','NB implication label','', '',r'\underset{\mathrm{At}}{\Longrightarrow}','B007','omission','high'),
 ('009-88','NB phrase before impossible','', r'\ill{}',"c'est",'B007','omission','high'),
 ('009-89','NB connected thin strokes','', '',graphic,'B007','other','high')]:
 cfg['new_changes'].append({'id':i,'place':place,'C':c,'H':h,'final':final,'scan_shows':E[b],'confidence':confidence,'kind':kind,'crop':cfg['boxes'][b]['crop'],'box':bs[b],'against_C':True,'against_H':True,'marked_in_H':False,'consequential':i!='009-89'})
# Replace the two identically labelled historical word doubts with individually identified current records.
for place,reading,alts,b in [
 ('At DC 1 X after avec','X',["X'"],'B003'),
 ('At DC 1 cancelled old conclusion, Y prime',"Y'",['Y'],'B006'),
 ('NB second Z refinement',r"Z\ll Y'",[r'Z\ll Y'],'B007'),
 ('NB cancelled word (impossible)','impossible',['internal letters partly obscured'],'B007'),
 ('NB absurde cancellation state',r'\deleted{absurde}',['absurde'],'B007'),
 ('Cor 2 cancelled introductory word','avec',['letters partly masked by hatching'],'B010'),
 ('Lower margin first At label',r'\parallel',['11'],'B024'),
 ('First live corollary heading','Cor. Main',['Corollaire'],'B029'),
 ('First live corollary article','la',['le'],'B029'),
 ('Second live corollary heading','Cor. Main',['Corollaire'],'B030')]:cfg['new_doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':'low','reason':E[b]})
# Explicit full excerpts where a wider page patch cannot match a narrower initial excerpt.
cfg['boxes']['B003']['final']=next(x['first'] for x in json.loads((R/'second'/f'{stem}_comparison.json').read_text())['rows'] if x['box']=='B003').replace(r'\inM',r'\in M').replace(r'avec $X\deleted',r"avec $\unsure{X|X'}\deleted")
cfg['boxes']['B006']['final']=r"\deleted{\inserted{avec $X'\parallel X\cap Y=L$, (i.e. $X'\parallel Z$ pour $Z\leq X,Y$}}"
cfg['boxes']['B007']['final']=next(x['first'] for x in json.loads((R/'second'/f'{stem}_comparison.json').read_text())['rows'] if x['box']=='B007')
for p in cfg['patches']:cfg['boxes']['B007']['final']=cfg['boxes']['B007']['final'].replace(p['old'],p['new'])
cfg['boxes']['B007']['final']+=' '+r'\margin{'+graphic+'}'
(R/'second'/f'{stem}_decisions.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
print(len(E),'decisions',len(set(x for a in ids.values() for x in a)),'unique changed places')
