"""Explicit main-reader decisions after viewing all 21 differing scan028 boxes."""
from pathlib import Path
import csv,hashlib,json
r=Path(__file__).resolve().parents[1];p=r/'pages/J156-5-04_156-5_scan028.tex'
rec=json.loads((r/'review/scan028_adjudicated.json').read_text())
comp=json.loads((r/'second/J156-5-04_156-5_scan028_comparison.json').read_text())
old_diagram=next(x['first'] for x in comp if x['box']=='028-B20')
new_diagram=r'\unsure{'+old_diagram.replace(r'\arrow[dddl,"\varphi"',r'\arrow[dddl,<->,"\varphi"')+'|'+old_diagram+'}'
edits=[
 {'old':r'\deleted{\unsure{H}}induites','new':r'\deleted{\unsure{H}}\unsure{induites|induite}'},
 {'old':r'\deleted{des} pour','new':r'\deleted{\unsure{des|de}} pour'},
 {'old':r'\deleted{\unsure{A_k}}\,C_k','new':r'\deleted{\unsure{A_k}}\unsure{.}\,C_k'},
 {'old':r"\deleted{T}S'",'new':r"\deleted{\unsure{T}}S'"},
 {'old':old_diagram,'new':new_diagram},
 {'old':'\navec\n','new':'\n'+r'\unsure{avec}'+'\n'},
 {'old':'où on pose','new':r'\unsure{et|où} on pose'},
 {'old':r"\deleted{\unsure{A}}\unsure{B_j'|A_j'}",'new':r"\unsure{\deleted{\unsure{A}}B_j'|\deleted{\unsure{B}}A_j'}"}]
def tr(s):
 for e in edits:s=s.replace(e['old'],e['new'])
 return s
O={
2:('19:55:19','The long oblique cancellations begin at the abandoned Cons and the following formula, below the live opening Soient ... ens. de L. The heading has its own local strikes. G retains an inward hook; the L is looped. The subordinate induites/des endings and the dark point before C_k are revised in their individual boxes, without extending the cancellation over the opening.','medium',True),
3:('19:55:34','Short diagonal strokes cross Proposition and a separate underline lies below it. They establish one locally cancelled underlined heading, not an independently evidenced second layer of cancellation over the opening sentence.','high',False),
4:('19:55:34','No cancellation crosses ens. de L. The ambient letter has a round lower loop, curved upright and long foot, supporting the calligraphic L. Retain this live continuation of the opening.','high',False),
5:('19:55:34','The initial C, low o and n/s run survive beneath the horizontal and oblique strikes. The final blob joins the crossing, so no detached full stop is established. Retain Cons/Con, not a certain Cons.','medium',False),
7:('19:55:43','The older I has broad horizontal top and bottom serifs around a straight central stem, not a J hook. The G ends inward; the raised A/B marks are circles. The empty sign is an oval pierced by a long stem, the phi-shaped sign used on these sheets.','high',False),
8:('19:55:43','The first group has a low left bowl, a tall central ascender and a low e exit, as in de elsewhere on this sheet. The next word has the s hook, compressed or, tall crossed t and low e: sorte. It does not expose separate c/e/l/a and v/e/u/t groups. Retain de sorte que under the global cancellation.','medium',False),
9:('19:55:43','The inner bar and cap after F overlap into an m-like cluster, so the two existing bar/cap alternatives remain. Both serifs of old I survive beneath K. The coproduct has the single squared-U form; circles and cap on the right are visible. No mathematical cleanup of the bars is warranted.','medium',False),
13:('19:56:11','The old cluster retains two H-like uprights and a joining stroke. The following long low stroke can belong to the compressed in beginning, so a separate hyphen is not established. The terminal e/s runs into the oblique cancellation; add induites/induite uncertainty while preserving induites first.','low',True),
14:('19:56:11','Both R forms have a large loop and swept foot, unlike plain roman R; retain the calligraphic/script uncertainty. The subscript G has an inward-ending open bowl. Par is already present immediately before this excerpt in the page.','medium',False),
16:('19:56:11','A looped d is readable, but the low terminal letters lie under a thick strike. The crop cannot distinguish des from de with certainty; add that alternative inside the existing local deletion. The k=(A,B) group remains clear.','low',True),
17:('19:56:30','The old capital has triangular legs and a crossbar consistent with A, with its subscript obscured. A separate point between the cancelled group and C_k is as dark as the adjacent ink and has a plausible separating position; preserve it as a doubtful point. C_k=A cap B is otherwise clear.','low',True),
18:('19:56:30','The right node has a clear S curve and separate high prime. An older horizontal bar and stem may be T, but their overlap does not make the old letter certain; restore its doubt. The small crossed k/n survives below. Both oblique inclusions are headless signs and the two labelled vertical arrows point down.','medium',True),
19:('19:57:09','I has two bilateral serifs; J has a right stem and left-returning base. Ens. ord. remains readable. The margin wrapper is a difference of excerpt layout; the full page already places this annotation to the right of the diagram.','high',False),
20:('19:57:09','The four inclusion arrows have hooked starts and pointed ends. The psi shaft has no terminal head; L is angular. The long phi edge has a clear lower head at I and a narrow upper fork just below S, with two arms beside its shaft. Prefer a head at both ends, retaining the down-only alternative because the upper fork may include retracing. The existing object positions and the old J beneath K remain.','medium',True),
21:('19:59:50','The older glyph has a right-hand vertical descending into a long left-returning hook. A central I stem with a bilateral bottom serif is absent. The curved lower stroke is the J base, not a rectangular enclosure; retain cancelled J beneath K.','high',False),
22:('19:59:55','The opening a-like curve, broad shallow v and joined e/c ending are extremely compressed and partly disconnected. Avec remains preferred, but not every letter is secure; add a doubt mark. The following K is the start of the next formula and is already transcribed.','medium',True),
23:('20:00:06','The full formula has an unprimed J in the image target, then I times I-prime in the comprehension. The second coordinate has a deep left-hooking descender and a separate prime, establishing j-prime. The overwritten second factor exposes A legs and B bowls, so retain its existing alternatives; the empty sign is phi-shaped.','medium',False),
24:('20:00:11','The second coordinate is long and hooked below the baseline, unlike the first short i, and its prime is separate. The factor after the cap is heavily overwritten with triangular and looped strokes; the subscript is not clear enough to discard the existing B/j-prime alternative. Retain the old-letter doubt and the visible high prime and circle.','low',False),
25:('20:00:11','The opening s has a compact low loop with a rising entry, followed by the dotted i; it is much smaller than the capital S in Soient. Retain lowercase si. The j hook, pair i/i-prime, comma and low on aura movements remain.','medium',False),
26:('20:00:19','The whole boxed equality has A_j, A_i, cap and A-prime with a separately primed i subscript; no circles occur. The low looped opening si is retained. The rectangle surrounds only the equality, with its hand-drawn right side retraced.','high',False),
27:('20:00:19','Before on pose, a very short first mark and a separate crossed ascending stroke favour et; a closed o and two u strokes are not independently visible, so retain où as an alternative. The first A has a distinct high prime. In the second left side, A legs/crossbar and B bowls overlap without a secure writing order: preserve both old-A/live-B and old-B/live-A states. Both final indices have long j hooks; the inverse exponents and lower bars of the order signs remain.','low',True)
}
with (r/'second/J156-5-04_156-5_scan028_boxes.tsv').open(newline='') as f:bs={x['box']:x for x in csv.DictReader(f,delimiter='\t')}
def evidence(k):
 b=bs[f'028-B{k:02}'];return {'evidence':O[k][1],'crop':f'crops/second_scan028_028-B{k:02}.png','box':[int(b[z]) for z in ('x0','y0','x1','y1')],'main_decision':'Main-reader decision after independent blind reading; see first/second/final audit.'}
dec=[]
for x in comp:
 if not x['different']:continue
 k=int(x['box'][-2:]);tm,ev,conf,ch=O[k];v=tr(x['first'])
 if k==22:v=r'\unsure{avec}'
 dec.append({'box':x['box'],'changed':ch,'final':v,'evidence':ev,'confidence':conf,'crop':f'crops/second_scan028_{x["box"]}.png','viewed_utc':f'2026-11-20 {tm} UTC'})
updates=[]
def up(id,k,**kw):updates.append({'id':id,'fields':{**kw,**evidence(k)}})
up('028-015',13,final=r'\deleted{\unsure{H}}\unsure{induites|induite}',confidence='low')
up('028-021',18,final=r"\deleted{\unsure{T}}S'",confidence='medium')
up('028-027',22,final=r'\unsure{avec}',confidence='medium')
up('028-035',27,final=r"\unsure{\deleted{\unsure{A}}B_j'|\deleted{\unsure{B}}A_j'}",confidence='low',review_only=True,merged_into='028-036',against_C=False,against_H=False,certainty_only=False)
up('028-036',27,final=r"\unsure{\deleted{\unsure{A}}B_j'|\deleted{\unsure{B}}A_j'}",confidence='low')
new=[]
def add(id,k,place,C,H,final,kind,confidence,consequential=False):
 new.append({'id':id,'place':place,'C':C,'H':H,'final':final,'kind':kind,'confidence':confidence,'against_C':True,'against_H':True,'H_marked':False,'certainty_only':False,'consequential':consequential,'rotation_degrees':0,**evidence(k)})
add('028-BL01',17,'cancelled C_k display, point before C_k','no point','no point',r'\unsure{.}','omission','low')
add('028-BL02',20,'second diagram, long phi edge from S to I','downward arrow','downward arrow',new_diagram,'drawing or diagram','medium',True)
add('028-BL03',27,'bottom definition lead-in','où on pose','où on pose',r'\unsure{et|où} on pose','misread word','low')
u=[]
for x in rec['unresolved']:
 x=dict(x)
 if x['place']=='second definition, overdrawn left side':x.update(reading=r"\deleted{A}B_j'",alternatives=[r"\deleted{B}A_j'"],reason=O[27][1])
 u.append(x)
for k,place,reading,alts in [
 (13,'induites ending','induites',['induite']),
 (16,'cancelled word before pour','des',['de']),
 (17,'point before C_k','point',['no punctuation']),
 (18,'first diagram, older capital','T',[]),
 (20,'second diagram, upper end of phi edge','arrowhead at both ends',['down-only arrow']),
 (22,'lead-in to image formula','avec',[]),
 (27,'lead-in to final definitions','et',['où'])]:
 u.append({'place':place,'reading':reading,'alternatives':alts,'reason':O[k][1],'confidence':O[k][2]})
inv=[]
for q in rec['inventory']:
 q=dict(q);el=q['element']
 if el=='des':q['first_words_or_objects']='cancelled des/de'
 if el=='Ck-display':q['first_words_or_objects']='crossed A_k; doubtful point; C_k=A∩B'
 if el=='diagram-1-overwrite':q['first_words_or_objects']='doubtful old T overwritten by S′, small k/n below'
 if el=='diagram-2':q['first_words_or_objects']='S∩T, S, T, ordinary L, I, I′, K over J; ψ headless; φ edge with doubtful upper head'
 if el=='image-set':q['first_words_or_objects']='doubtful avec; K=Im(S∩T→I×J)={(i,j′)∈I×I′ | ...}'
 if el=='definitions':q['first_words_or_objects']='et/où on pose A_i′=φ^{-1}(I_{≤i}); old-A/live-B or old-B/live-A_j′=φ′^{-1}(I′_{≤j})'
 inv.append(q)
out={'scan':28,'page_before_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'edits':edits,'decisions':dec,'record_updates':updates,'new_changes':new,'unresolved_replace':u,'inventory_replace':inv,'changed_loci':['028-induites-certainty','028-des-certainty','028-BL01','028-021-certainty','028-BL02','028-027-certainty','028-BL03','028-036-state-certainty'],'notes_append':['The blind audit detects a possible upper head on the long phi edge from S to I. The transcription now prefers a bidirectional edge but retains the down-only form, because the upper fork may be retracing. This does not supply an inverse map or a new mathematical assertion. The final overwritten A/B definition now explicitly retains both possible cancellation orders; the short lead-in prefers et with où as an alternative. The very compressed avec and two struck endings remain doubtful. A dark separated point before C_k is kept with doubt, not inferred as a mathematical operation.']}
(r/'second/scan028_adjudication_input.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(dec),'decisions;',len(edits),'edits')
