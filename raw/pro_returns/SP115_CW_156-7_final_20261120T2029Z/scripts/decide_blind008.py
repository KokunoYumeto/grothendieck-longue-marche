#!/usr/bin/env python3
"""Explicit root decisions after direct inspection of 32 differing blind crops."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parents[1]; stem='H156-01_156-7_scan008'
bs={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{stem}_boxes.tsv').open(),delimiter='\t')}
E=dict(re.findall(r'^- (B\d{3}): (.*)$',(R/'second'/f'{stem}_root_observations.md').read_text(),re.M))
ids={'B003':['008-A01'],'B004':['008-A02'],'B006':['008-A03'],'B011':['008-A04','008-A05'],'B012':['008-A04'],'B014':['008-A05'],'B020':['008-A06'],'B021':['008-A06'],'B031':['008-A07'],'B032':['008-A07'],'B040':['008-A06','008-A07']}
cfg={'reader':'reader_a (GPT-6 Astra Pro; effort not exposed)','patches':[],'change_updates':{},'new_changes':[],'remove_doubt_places':['pas mal ... implications','First equivalence label','NB overwritten underlying verb','NB surviving verb','NB struck final mathematical symbol','At lower-left insertion','Cor surviving first Sup operand'],'new_doubts':[],'boxes':{}}
def patch(a,b):cfg['patches'].append({'old':a,'new':b,'count':1})
patch('% Root initial adjudication; blind second reading pending.','% Root adjudication after blind second reading.')
patch("``facultatifs''",r"``facultatif\unsure{s}''")
patch(r"\unsure{des'|des|d'}","des'")
patch(r'\unsure{\mathrm{dfn}|\mathrm{defn}}',r'\unsure{\mathrm{dfn}|\mathrm{defn}|\mathrm{def}}')
patch(r'\deleted{\unsure{résultera}}\unsure{résulte|résultera}',r'résul\deleted{\unsure{tera}}\inserted{te}')
patch(r"\deleted{\unsure{i.e.} c'est un $\unsure{\exists}$}",r"\deleted{\unsure{i.e.} \unsure{c'est un} $\unsure{\exists|]}$}")
patch(r'\inserted{\unsure{soit}}',r'\inserted{soit}')
patch(r'\unsure{\widetilde F|F}',r'F')
for b,e in E.items():cfg['boxes'][b]={'crop':f'crops/second_scan008_{b}.png','box_coords':bs[b],'decision':'revise or mark uncertainty' if b in ids else 'retain after ink comparison','evidence':e,'changed_place_ids':ids.get(b,[])}
def upd(i,b,**kw):cfg['change_updates'][i]={'crop':cfg['boxes'][b]['crop'],'box':bs[b],**kw}
upd('008-03','B003',final=r"``facultatif\unsure{s}''",scan_shows=E['B003'],confidence='low')
upd('008-04','B004',final="des'",scan_shows=E['B004'],confidence='medium')
upd('008-07','B006',final=r'\unsure{\mathrm{dfn}|\mathrm{defn}|\mathrm{def}}',scan_shows=E['B006'],confidence='low')
upd('008-17','B012',final=r'résul\deleted{\unsure{tera}}\inserted{te}',scan_shows=E['B012'],confidence='medium',against_C=True)
upd('008-20','B014',final=r"\deleted{\unsure{i.e.} \unsure{c'est un} $\unsure{\exists|]}$}",scan_shows=E['B014'],confidence='low')
upd('008-31','B021',final=r'\inserted{soit}',scan_shows=E['B021'],confidence='high')
upd('008-47','B032',final=r'\deleted{\unsure{\widetilde X|X}}F',scan_shows=E['B032'],confidence='low',against_C=True)
# Synchronize broader existing change records without duplicating physical counts.
review=json.loads((R/'review'/'scan008_final.json').read_text())
for id in ['008-28','008-45']:
 old=next(x['final'] for x in review['changes'] if x['id']==id);new=old
 for p in cfg['patches']:new=new.replace(p['old'],p['new'])
 cfg['change_updates'].setdefault(id,{})['final']=new
for place,reading,alts,b in [
 ('Opening facultatif(s), final letter','facultatifs',['facultatif'],'B003'),
 ('First equivalence label','dfn',['defn','def'],'B006'),
 ('NB overwritten underlying ending','tera',['old ending partly obscured'],'B012'),
 ('NB cancelled middle phrase',"c'est un",['word sequence not fully recoverable under strike'],'B014'),
 ('NB struck final mathematical symbol',r'\exists',[']'],'B014')]:cfg['new_doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':'low','reason':E[b]})
# Make local final excerpts explicit where a page-wide patch would not match the first excerpt.
cfg['boxes']['B012']['final']=r'résul\deleted{\unsure{tera}}\inserted{te}'
cfg['boxes']['B021']['final']=r'\deleted{\inserted{soit}}'
cfg['boxes']['B032']['final']=r'\deleted{\deleted{\unsure{\widetilde X|X}}F}'
(R/'second'/f'{stem}_decisions.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
print(len(E),'decisions',len(set(x for a in ids.values() for x in a)),'unique changed places')
