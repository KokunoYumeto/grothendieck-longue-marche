#!/usr/bin/env python3
"""Explicit root decisions after direct display of all 35 differing blind crops."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parents[1];stem='H156-01_156-7_scan007'
bs={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{stem}_boxes.tsv').open(),delimiter='\t')}
E=dict(re.findall(r'^- (B\d{3}): (.*)$',(R/'second'/f'{stem}_root_observations.md').read_text(),re.M))
E['B011']='On and laisser are separated by blank baseline space with no independent p-e-u-t sequence; the tall strokes crossing that interval belong to the lower inserted profit. Omit peut. The flattened terminal of laisser does not securely distinguish r from an exit, so mark laisser/laisse. The rightmost F modifier meets the physical image edge: its surviving left stroke cannot securely distinguish tilde from overbar; mark both. Remplacer retains its final hooked r and de la retains d loop, tall l and a exit. The two punctuation marks between At1 and At3 are a semicolon (confirmed in B030). Font/M mapping and insertion au profit agree.'
E['B012']='The cancelled fermée has f plus extended e/r/m humps, not the shorter finie sequence. The dark numeral/parenthesis superposition preserves the existing 1/0 doubt. The crossed qualifier admits tf/Af/4f; add uncertainty, confirmed in B031. All other words and deletion scope agree.'
E['B013']='Separate V. precedes a looped p-like group and 5, not one page word. Read V. with p/p. uncertainty, confirmed in B032. Repeated fermée has extended middle humps; retain it against finie. Condition b, compatibility star and final (page 5) agree. The crossed At group remains uncertain; a subscript is not secure under the hatching.'
for b in E:E[b]=E[b].replace('**','')
ids={'B002':['007-A01'],'B005':['007-A02'],'B011':['007-A03','007-A04','007-A05','007-A06'],'B012':['007-A08'],'B013':['007-A07'],'B016':['007-A09'],'B017':['007-A09'],'B021':['007-A10'],'B030':['007-A06'],'B031':['007-A08'],'B032':['007-A07']}
cfg={'reader':'reader_b (GPT-6 Astra Pro; effort not exposed)','patches':[],'change_updates':{},'new_changes':[],'remove_doubt_places':['first live reference to page 5','At_M1 to At_M3, range marker','cancelled definition words','cancelled sign before Omb(x)'],'new_doubts':[],'boxes':{}}
def patch(a,b):cfg['patches'].append({'old':a,'new':b,'count':1})
patch(r'\inM',r'\in M')
patch(r', posant $\Phi^{X}',r', \unsure{posant|posons} $\Phi^{X}')
patch(r'\inserted{dans} $\widetilde Y^{X}=\{Z\in\widetilde Y\mid X\ll Z\}$',r'\inserted{dans $\widetilde Y^{X}=\{Z\in\widetilde Y\mid X\ll Z\}$}')
patch('on peut laisser tomber',r'on \unsure{laisser|laisse} tomber')
patch(r"l'élément de structure $\widetilde{\mathscr F}$",r"l'élément de structure $\unsure{\widetilde{\mathscr F}|\overline{\mathscr F}}$")
patch(r'\unsure{à|:}',r';')
patch(r'\unsure{page|p.} 5',r'V. \unsure{p|p.} 5')
patch(r'\,(\mathrm{tf})',r'\,(\unsure{\mathrm{tf}|\mathrm{Af}|4f})')
patch(r'\unsure{formées}',r'\unsure{formées|fermées}')
patch(r'\deleted{\unsure{X}}',r'\deleted{\unsure{X|\Phi}}')
for b,e in E.items():cfg['boxes'][b]={'crop':f'crops/second_scan007_{b}.png','box_coords':bs[b],'decision':'revise or mark uncertainty' if b in ids else 'retain after ink comparison','evidence':e,'changed_place_ids':ids.get(b,[])}
def upd(i,b,**kw):cfg['change_updates'][i]={'crop':cfg['boxes'][b]['crop'],'box':bs[b],**kw}
upd('S007-020','B005',place='inserted dans and whole definition of tilde Y superscript X',final=r'\inserted{dans $\widetilde Y^{X}=\{Z\in\widetilde Y\mid X\ll Z\}$}',scan_shows=E['B005'],against_C=True,confidence='high')
upd('S007-026','B011',final=r'on \unsure{laisser|laisse} tomber',scan_shows=E['B011'],against_C=True,confidence='medium')
upd('S007-027','B011',final=r'\unsure{\widetilde{\mathscr F}|\overline{\mathscr F}}',scan_shows=E['B011'],confidence='low')
upd('S007-031','B031',final=r'(\unsure{\mathrm{tf}|\mathrm{Af}|4f})',scan_shows=E['B031'],confidence='low')
upd('S007-033','B032',final=r'V. \unsure{p|p.} 5',scan_shows=E['B032'],against_C=True,against_H=True,confidence='medium')
upd('S007-040','B017',final=r'\deleted{\unsure{formées|fermées} \unsure{t.q.}}',scan_shows=E['B017'],confidence='low')
upd('S007-048','B021',final=r'\deleted{\unsure{X|\Phi}}',scan_shows=E['B021'],confidence='low')
# A semicolon is a source reading change; uncertainty-only additions are not new C/H substantive rows.
cfg['new_changes'].append({'id':'S007-058','place':'between At_M1 and At_M3 in D’autre part paragraph','C':'à','H':'à','final':';','scan_shows':E['B030'],'confidence':'high','kind':'misread symbol or index','crop':'crops/second_scan007_B030.png','box':bs['B030'],'against_C':True,'against_H':True,'marked_in_H':False,'consequential':False})
for place,reading,alts,b in [
 ('cancelled opening axiom, participle before Phi superscript X','posant',['posons'],'B002'),
 ('D’autre part paragraph, verb after on','laisser',['laisse'],'B011'),
 ('family modifier after élément de structure',r'\widetilde{\mathscr F}',[r'\overline{\mathscr F}'],'B011'),
 ('first live reference to page 5, abbreviation after V.','p',['p.'],'B032'),
 ('cancelled parenthesized axiom qualifier','tf',['Af','4f'],'B031'),
 ('cancelled definition words','formées t.q.',['fermées t.q.; second abbreviation remains uncertain'],'B017'),
 ('cancelled sign before Omb(x)','X',[r'\Phi'],'B021')]:cfg['new_doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':'low','reason':E[b]})
# First excerpts may omit surrounding markup already in the page; record exact retained page context.
cfg['boxes']['B036']['final']=r'\uline{page 32})'
cfg['boxes']['B034']['final']=r'$\mathrm{At}_{M}\,4,5,6$,'
cfg['boxes']['B035']['final']='p. 28,'
(R/'second'/f'{stem}_decisions.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
print(len(E),'decisions',len(set(x for z in ids.values() for x in z)),'unique changed places')
