"""Main-reader decisions for scan026 after inspecting all twenty differing boxes."""
from pathlib import Path
import csv, hashlib, json
r=Path(__file__).resolve().parents[1]
p=r/'pages/J156-5-04_156-5_scan026.tex'
rec=json.loads((r/'review/scan026_adjudicated.json').read_text())
comp=json.loads((r/'second/J156-5-04_156-5_scan026_comparison.json').read_text())
edits=[
 {'old':r'\deleted{\unsure{sur|su|sub}}subdivision','new':r'\unsure{\deleted{\unsure{su}}|su}bdivision'},
 {'old':r'F\unsure{\preceq|\leq}G','new':r'F\preceq G'},
 {'old':r'$\mathcal R_{G}$ sur $|F|=|G|$','new':r'$\mathcal R_{G}$ \unsure{dans|donc} $|F|=|G|$'},
 {'old':r'\deleted{\unsure{raff|suf}}subdivision','new':r'su\deleted{\unsure{f}}bdivision'},
 {'old':r'\deleted{b) Pour que $F$ soit une subdivision de $G$, il f','new':r'\deleted{b) Pour que $F$ soit une subdivision de $G$ il f'},
 {'old':r'\unsure{Invers\(^{\mathrm{mt}}\)}','new':r'\unsure{Inversemt|Invers\(^{\mathrm{mt}}\)|Inversement}'},
 {'old':r'\deleted{Sinon},','new':r'\deleted{\unsure{Sinon}},'},
 {'old':r'\text{ où }x\in |F|\unsure{\setminus}\,\unsure{G|F|K}\unsure{\}|,}','new':r'\text{ \unsure{avec|où} }x\in |F|\unsure{{}_{K}|\}}'}
]
# The margin formula has one math group containing both named relations.
edits[2]={'old':r'\mathcal R_{G}$ sur $|F|=|G|$','new':r'\mathcal R_{G}$ \unsure{dans|donc} $|F|=|G|$'}
def transform(s):
 for e in edits:s=s.replace(e['old'],e['new'])
 return s
O={
2:('19:43:15','Both resp. groups have p descenders; the f after loc. has a long descending loop and a compressed er continuation without a separate i dot. Idem has a dotted initial and tall d. Retain the first reading, including the unresolved final adjective ending.','medium',False),
3:('19:43:15','The left su-like group is heavily retraced and crossed, followed immediately by the clear tall b and division. A second complete su group cannot be separated in the ink. Remove the duplicated prefix supplied by the first transcription and mark whether the one surviving su group is cancelled or live as uncertain.','low',True),
4:('19:43:15','The upper surj label ends in a j descender without a separate full stop; the lower label has a distinct point. The top arrow has a hook at the left and a right head; both vertical arrows point down. The comma sits at lower right. Retain that geometry and punctuation; the remaining differences are TikZ encoding.','high',False),
5:('19:49:02','The complete rotated note was inspected again. The two signs standing for même are pairs of horizontal strokes, not the letters ens. The order sign has a bent upper angle and bowed lower bar. The final preposition has a small closed initial loop and an upright matching d in deux/d’ordre; the long low continuation favours dans, with donc still possible. Sur is not supported by that opening. Preserve the cancelled abbreviation and script-R doubt.','medium',True),
6:('19:43:48','The upper angle and its lower arm are bent, and the separate lower bar is bowed. The straight ≤ in the displayed F≤G′≼G provides a same-page contrast. Resolve this particular sign as preceq; the whole marginal formula was also inspected.','high',True),
7:('19:43:48','An initial d loop and a final below-baseline q-like hook survive the heavy strike. The intervening letters are hidden. Retain doubtful d’éq; the blind dite/dit reading does not account for the final descending trace.','low',False),
8:('19:43:48','A small closed loop is visible between phi and the slanting entry of p, but it is joined to that entry. Retain the possible composition circle with a doubt mark; no mathematical convention resolves whether it is separate ink.','medium',False),
10:('19:44:05','The source has a long upright ending in two short diverging strokes and no arrowhead. The blind crop is rotated relative to the page. Both drawings have the same three strokes; retain the edition’s page orientation and integrated marginal placement.','high',False),
11:('19:44:05','The end capital after de has a tall stem and two short rightward arms: F, not the G required by the preceding prose and following displayed chain. The corrected word begins one live su, then an overwritten tall f-like residue beside the live b. Adopt the local correction described in S026-12 while preserving the clear authorial F.','low',True),
12:('19:44:05','A low su is followed by one tall looped f-like residue, crossed/overwritten beside the live b, then division. The crop does not show a separate raff or a second complete su. Represent the old residue locally: su plus cancelled doubtful f plus bdivision.','low',True),
13:('19:44:20','Two dark distinct points to the left of F form the colon. The first relation has straight strokes; the second has a bowed lower bar. Retain the colon and F≤G′≼G. Display wrappers alone account for the rest.','high',False),
14:('19:44:20','The five long oblique strokes cancel this paragraph. In the space between G and il there is no distinct dark comma; remove the supplied comma. The broken raffine-/ment is one word continued on the following manuscript line. The blind inclusion of the next Ainsi fragment is a box-boundary difference; it is already separately transcribed and cancelled.','high',True),
15:('19:44:20','The strike crosses the middle of the word after Ainsi. A d ascender and low final run favour dans, but the other letters do not become individually clear. Retain the existing alternatives rather than resolve a cancelled doubt from context.','medium',False),
16:('19:44:37','The initial évid is readable; its compressed continuation has raised terminal strokes. Retain the short-form transcription with an uncertain ending. The blind full expansion is not established by individually legible letters.','medium',False),
17:('19:47:28','The whole proof-heading line and the tight crop show a tall I, low compressed middle groups and a final t whose base lies on the same baseline. Prefer the blind baseline short form Inversemt; keep the formerly read raised ending and full-word alternative explicitly doubtful.','medium',True),
18:('19:44:37','The strike covers the middle and final letters of Sinon. Initial S and the i dot survive, but not every cancelled letter is independently plain. Add a doubt mark to Sinon. The descending comma sits below and beyond the strike and remains live.','low',True),
19:('19:48:43','The complete two-line formula was reread. After the singleton there are three low letter groups, with an angular middle v-like return and an open final c-like ending, favouring avec over the earlier où; retain the latter as an alternative. The edge has x∈|F| followed by a lowered K-like/brace-like mark, not a separately established slash and additional G. Adopt the doubtful lowered mark. Keep the uncertain P alphabet, cancelled g, and the clear second-line index |F| minus |G|, despite its mathematical difficulty.','low',True),
20:('19:47:21','The overwritten letter has a small bowl and a long hooked descender under the crossing stroke. These support the existing doubtful g. The blind f alternative does not establish a different preferred letter; retain the first reading with its doubt.','low',False),
21:('19:47:21','After the tall bars enclosing a clear F, the ink drops down at the paper edge. The lowered cluster has a stem and two diverging arms, K-like, and might instead belong to a closing brace. There is no separately readable set-difference slash followed by G. Replace that conjectural extension by the blind lowered-K/brace alternative, without supplying a certain closing delimiter.','low',True),
22:('19:47:28','The heading underline ends beneath Dém, before the following full stop; retain that punctuation scope. The two short forms have been checked in their own crops: keep doubtful raised évid-ending, change Inversemt to a doubtful baseline short form. Supposons starts the next line beyond this box and remains in the complete page.','medium',True)
}
dec=[]
for x in comp:
 if not x['different']:continue
 k=int(x['box'][-2:]);tm,ev,conf,ch=O[k];v=transform(x['first'])
 if k==6:v=v.replace(r'\unsure{\preceq|\leq}',r'\preceq')
 if k==17:v=r'\unsure{Inversemt|Invers\(^{\mathrm{mt}}\)|Inversement},'
 if k==21:v=r'$x\in |F|\unsure{{}_{K}|\}}$'
 dec.append({'box':x['box'],'changed':ch,'final':v,'evidence':ev,'confidence':conf,'crop':f'crops/second_scan026_{x["box"]}.png','viewed_utc':f'2026-11-20 {tm} UTC'})
with (r/'second/J156-5-04_156-5_scan026_boxes.tsv').open(newline='') as f:boxes={x['box']:x for x in csv.DictReader(f,delimiter='\t')}
updates=[]
def update(id,k,**fields):
 b=boxes[f'S026-{k:02}'];fields.update(evidence=O[k][1],crop=f'crops/second_scan026_S026-{k:02}.png',box=[int(b[z]) for z in ('x0','y0','x1','y1')],main_decision='Reconsidered on the independent-reading crop; see first/second/final audit below.')
 updates.append({'id':id,'fields':fields})
update('026-06',3,C=r'\deleted{\unsure{sur|su}}\unsure{subdivision}',H=r'\struck{sub}subdivision',final=r'\unsure{\deleted{\unsure{su}}|su}bdivision',against_C=True,against_H=True,confidence='low')
update('026-07',3,final=r'\unsure{\deleted{\unsure{su}}|su}bdivision',certainty_only=False,review_only=True,merged_into='026-06',against_C=False,against_H=False,confidence='low')
update('026-17',6,final=r'\preceq',confidence='high')
update('026-21',5,final=r'\unsure{dans|donc}',against_C=True,against_H=False,confidence='medium')
update('026-26',12,C=r'\deleted{\unsure{raff|suf}}\unsure{subdivision}',H='subdivision (no cancelled residue)',final=r'su\deleted{\unsure{f}}bdivision',against_C=True,against_H=True,confidence='low')
update('026-27',12,final=r'su\deleted{\unsure{f}}bdivision',certainty_only=False,review_only=True,merged_into='026-26',against_C=False,against_H=False,confidence='low')
update('026-37',17,final=r'\unsure{Inversemt|Invers^{mt}|Inversement}',against_C=True,against_H=True,confidence='medium')
update('026-39',18,final=r'\deleted{\unsure{Sinon}},',confidence='low')
update('026-44',19,final=r'\unsure{avec|où}',against_C=True,against_H=False,confidence='medium')
update('026-46',21,final=r'\unsure{{}_{K}|\}}',confidence='low')
b=boxes['S026-14']
new=[{'id':'026-BL01','place':'cancelled item b, punctuation between G and il','C':r'$G$, il','H':r'$G$, il','final':r'$G$ il','evidence':O[14][1],'crop':'crops/second_scan026_S026-14.png','box':[int(b[z]) for z in ('x0','y0','x1','y1')],'confidence':'high','kind':'text not on the page','against_C':True,'against_H':True,'H_marked':False,'certainty_only':False,'consequential':False,'main_decision':'Comma removed after blind reading and main-reader inspection.'}]
u=[]
skip={'slanted note order sign','bottom first-line set-difference sign','bottom first-line final capital','bottom first-line terminal trace'}
for x in rec['unresolved']:
 if x['place'] in skip:continue
 x=dict(x)
 if x['place']=='top corrected prefix':x.update(reading=r'\deleted{\unsure{su}}',alternatives=['live su'],reason=O[3][1])
 if x['place']=='a) cancelled prefix':x.update(reading='f, locally overwritten after su',alternatives=[],reason=O[12][1])
 if x['place']=='proof second abbreviation':x.update(reading='Inversemt',alternatives=['Invers with raised mt','Inversement'],reason=O[17][1])
 u.append(x)
for place,read,alts,k in [('slanted note final preposition','dans',['donc'],5),('cancelled Sinon','Sinon',[],18),('bottom connective','avec',['où'],19),('bottom lowered edge mark',r'{}_{K}',[r'\}'],21)]:
 u.append({'place':place,'reading':read,'alternatives':alts,'reason':O[k][1],'confidence':O[k][2],'crop':f'crops/second_scan026_S026-{k:02}.png'})
inv=[]
for x in rec['inventory']:
 x=dict(x)
 for k,v in x.items():
  if isinstance(v,str):x[k]=transform(v)
 inv.append(x)
out={'scan':26,'page_before_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'edits':edits,'decisions':dec,'record_updates':updates,'new_changes':new,'unresolved_replace':u,'inventory_replace':inv,'changed_loci':['026-06','026-17','026-21','026-26','026-BL01','026-37','026-39-certainty','026-44','026-46'],'notes_append':['The blind audit localizes both corrections within subdivision rather than duplicating a complete prefix. The marginal order sign is now securely preceq; the final preposition is preferred as dans, with donc still possible. The bottom first-line connector is preferred as avec. At its edge, only a lowered K-like/closing-brace-like mark is supported after x∈|F|; the formerly conjectured additional set difference is withdrawn. The second-line coproduct index still clearly reads |F| minus |G|. This textual difficulty is kept and is not repaired from the expected construction.'],'abbreviations_append':[{'form':'Inversemt','expansion':'Inversement; the compressed baseline ending remains doubtful, and the full word is not substituted.'}]}
(r/'second/scan026_adjudication_input.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(dec),'decisions;',len(edits),'edits; nine changed physical loci')
