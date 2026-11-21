from pathlib import Path
import csv,json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan063'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest()=='2db21fe920a6f71e43726d0f3ecf8eb67b5fbf3d3bb958b04ea2000f415690e9'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B02':'The canonical box, right-hand detail and an unresolved-adjective enlargement were viewed. The adjective has a low doubled-s opening, e/n/t, a detached i dot and two tall l loops: essentielle. Naturelle does not account for the dotted i after the t. Two short groups after the adjective contain est and a d-like loop followed by the low onc run: donc is not omitted. Comment continues at the right edge.',
'B03':'The long live verb retains its reconstituer reading, but the tiny raised opening stroke leaves reconstituer/reconstituer-with-accent uncertain. The overwritten small group after graphe was examined in its own detail: a tall upright and several short round/crossing strokes permit Gamma or an abbreviated top.; neither is securely resolved beneath the overwriting. The following colon has two distinct dots.',
'B04':'A single long cancellation crosses a reperes donne. The raised replacement has rep, the middle accent and a compressed ending, leaving reperes/repere unresolved. The final e/s under the strike of donne is not separately clear, so donne/donnes is now explicit without imposing agreement.',
'B05':'The final d has a closed lower loop and an ascender, then one long e exit with a downward hook. There is no independent additional s; groupoide remains singular, as the first crop decision recorded.',
'B06':'The cancelled lower word has a p descender, tall l and low u/s strokes, supporting plus, without the extra ascender and interior letters needed for fleches. The small raised replacement has a/v/e/c-like joins and reads avec. The adjacent baseline sa is not an added les.',
'B07':'The long strike crosses the entire des foncteurs short-word phrase. After foncteurs the last short word begins with a tall narrow loop and no securely closed d bowl, favouring les over des; the full phrase remains under doubt. The raised et and all of l-explicitation stand on the same added baseline.',
'B08':'The operation numerals have angular 4 and top-barred 5, each followed by a small degree circle and right parenthesis. The final point is separate. The readings differ only in math-mode wrappers and line breaks.',
'B09':'The whole slanted margin and its rotated view were inspected. NB alone is underlined. S precedes ou and D, both within quotation strokes, followed by a comma. The word contenus has a final low exit that can be an s; contenus/contenu is now explicit. The last line has dans and one underlined Gamma, with no extra des or point.',
'B10':'The 4 has its angled upper stroke and vertical downstroke, then a degree circle and right parenthesis. The words on both sides agree; the comparison difference is the math wrapper.',
'B12':'There are two short horizontal traces, the lower slightly wavy with a small entry hook. They do not show three independent m downstrokes. The same paired-stroke abbreviation occurs before facon in B13, and the equals form is retained in both places.',
'B13':'The two short strokes before facon are separated horizontal bars with a curved entry on the lower one. No independent m body lies beneath them. The page abbreviation remains the equals sign, not an expanded meme.',
'B14':'The small left sign is faint at its top but has a clear curved lower return. Its bottom lies visibly above the large T baseline, so its raised position is retained. S remains uncertain; g, comma, nu and plus-minus were read in the whole formula.',
'B15':'The crop and already saved same-box detail show only low joined letters after the formula, with no tall d supporting ci-dessus. The c/o and repeated n/u-like low humps favour connus; comme ens and ci-dessus remain alternatives because the joins and detached short stroke are compressed. The closing parenthesis and comma are separate.',
'B16':'After the b and oval o, the low u/c strokes lead into an h ascender with a right-hand shoulder, followed by a and a g descender: bouchage. The later short group has d and the es exit. Bordage would require a different interior letter grouping; the existing le bouchage des remains.',
'B17':'The baseline word has a tall crossed t, low r/o/u connections and a final downturned s: trous. The upper pourrait has its p descender and dotted i. Its long stroke descends to the join before s-expliciter and is an insertion leader, not a cancellation of an absent verb.',
'B18':'Before operations the cancelled line has two small groups: a looped d/e group and a separate c-like curve with a terminal s-like stroke. The primary reading is now de ces, with des retained as an alternative under the strike. The raised replacement des cas is clear and remains separate.',
'B19':'The crossed first word has an initial open c, a tall t, a rounded middle g with descending stroke, and the reduced ories ending, favouring categories over analogues. The cancellation still crosses letter joins, so the alternative remains. The following closed o and low u favour ou, not aux; the preceding comma-shaped hook remains doubtful.',
'B20':'The initial des stands to the left of the long strike and remains live. The cancelled run has a tall f/l-like group followed by a distinct point; a later curved opening stroke precedes a d/e/s-like group, then low u/n/i/t/e/s-like traces. The new doubtful reading fl. (des unites is retained with donnees as the last-word alternative. The strike prevents a secure expansion or a supplied closing parenthesis. The replacement structures stands above; the earlier illegible whole-word placeholder is no longer needed for the visible f/l strokes.',
'B21':'The word begins with an e loop and tall l, continues with low e/m/e/n and a tall t, and ends in aires. Quotation ticks flank the word and a colon follows. This supports the existing quoted elementaires, not d-une categorie.',
'B22':'The full diagram and its formula and annotation details were viewed. Both S prefixes are crossed with several vertical strokes, and the map points right. The target operator has a lower bar and upright with a heavily inked upper trace, so plus-minus/minus/plus remains unresolved; diminution does not repair it. The source has g,nu,nu-prime and a plus-minus exponent. The bracket attaches the four-line note to that source. The note opening admits les/un, and its short continuation admits avec/ou. The short word before donnee has a horizontal overstroke through its low letters; cancelled la is now first, with cancelled les and live la retained. The final e of donnee is compressed. A separate short hyphen is visible between sous and ens.; it is restored. No extra repeated source formula is supplied. The two-star tag keeps its deletion-state doubt.',
'B23':'The words read avec ou on the upper line and sans S followed by a question mark on the next. A long slightly wavering vertical separator at the left continues several text heights below them, ending in a short leftward hook. The second TikZ outline reproduces this length and hook more faithfully than the short tabular rule; the words are unchanged.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
repls={
'B03':[('reconstituer,',r'\unsure{reconstituer|réconstituer},'),(r'\unsure{\Gamma}',r'\unsure{\Gamma|\mathrm{top.}}')],
'B04':[(r'\deleted{à repères donné}',r'\deleted{à repères \unsure{donné|donnés}}')],
'B07':[(r'\unsure{des foncteurs des}',r'\unsure{des foncteurs les|des foncteurs des}')],
'B09':[('contenus déjà',r'\unsure{contenus|contenu} déjà')],
'B15':[(r'\unsure{ci-dessus|connus}',r'\unsure{connus|comme ens|ci-dessus}')],
'B18':[(r'\deleted{des opérations}',r'\deleted{\unsure{de ces|des} opérations}')],
'B19':[(r'\unsure{analogues|catégories}',r'\unsure{catégories|analogues}')],
'B20':[(r'\deleted{\unsure{\illegible{1} données|données}}',r'\deleted{\unsure{fl.} \unsure{(}des \unsure{unités|données}}')],
'B22':[(r'les $X\in',r'\unsure{les|un} $X\in'),(r'^\pm$, avec',r'^\pm$, \unsure{avec|ou}'),(r'\unsure{la|\deleted{la}} donnée',r'\unsure{\deleted{la}|\deleted{les}|la} \unsure{donnée|donné}'),('sous ens.','sous-ens.')]
}
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,rs in repls.items():
 v=C[b]['first']
 for a,z in rs:
  assert a in v and a in s,(b,a);v=v.replace(a,z);s=s.replace(a,z)
 D[b].update(choice='reading',reading=v)
a=C['B23']['first'];assert a in s;s=s.replace(a,C['B23']['second']);D['B23']['choice']='take_second'
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
def update(n,b,**kw):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02d}')
 x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],**kw)
update(1,'B02')
update(2,'B03',final=r'\deleted{$\unsure{\Gamma|\mathrm{top.}}$}')
update(5,'B07',place='Cancelled phrase below et l-explicitation',final=r'\deleted{\unsure{des foncteurs les|des foncteurs des}}',diff_c=True)
update(9,'B09',final=r'\unsure{contenus|contenu} déjà',confidence='medium')
update(16,'B15',final=r'\unsure{connus|comme ens|ci-dessus}',diff_c=True,diff_h=False)
update(20,'B19',final=r'\deleted{\unsure{catégories|analogues}\unsure{,} ou}',diff_c=True,diff_h=False)
update(22,'B20',final=r'\deleted{\unsure{fl.} \unsure{(}des \unsure{unités|données}}',confidence='low')
update(28,'B22',final=D['B22']['reading'].removeprefix('diminution\n'))
update(30,'B22',final=r'\unsure{\deleted{la}|\deleted{les}|la}',diff_c=True,diff_h=True,confidence='low')
update(32,'B22',final='sous-ens.',diff_c=True,diff_h=False,confidence='high')
for n,b in ((13,'B12'),(14,'B13'),(15,'B14'),(17,'B16'),(18,'B17'),(19,'B17'),(21,'B20'),(23,'B21'),(26,'B22'),(27,'B22')):update(n,b)
def add(n,place,c,h,final,b,kind,err,confidence='medium',diff_h=True):
 r['changes'].append(dict(id=f'{p}-{n:02d}',place=place,c=c,h=h,final=final,diff_c=True,diff_h=diff_h,kind=kind,error_kind=err,evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],confidence=confidence,marked_in_h=False,consequential=False))
add(35,'Cancelled old phrase before des cas',r'\deleted{des opérations}',r'\struck{des opérations}',r'\deleted{\unsure{de ces|des} opérations}','B18','omission','Struck text','low')
add(36,'Margin beside the lower diagram, long separator','absent','separator described in editorial note',C['B23']['second'],'B23','drawing or diagram','Drawings and diagrams','high',False)
for x in r['decisions']:
 if x['id']=='M0767':x.update(reading=r'\unsure{connus|comme ens|ci-dessus}',evidence=E['B15'],crop=f'crops/{p}_second_B15.png',box=boxes['B15'])
for x in r['doubts']:
 if x['place']=='Cancelled sign after graphe':x.update(reading=r'\unsure{\Gamma|\mathrm{top.}}',alternatives='Gamma; top.',reason=E['B03'])
 if x['place']=='Cancelled phrase below et l’explicitation':x.update(reading=r'\unsure{des foncteurs les|des foncteurs des}',alternatives='final les; des',reason=E['B07'])
 if x['place']=='Word after the second paired groupoid':x.update(reading=r'\unsure{connus|comme ens|ci-dessus}',alternatives='connus; comme ens; ci-dessus',reason=E['B15'])
 if x['place']=='Cancelled phrase before S T and T':x.update(reading='catégories',alternatives='analogues',reason=E['B19'])
 if x['place']=='Cancelled run replaced by structures':x.update(reading=r'\deleted{\unsure{fl.} \unsure{(}des \unsure{unités|données}}',alternatives='fl.; unidentified abbreviated first group; opening parenthesis; unités/données',reason=E['B20'])
 if x['place']=='Footer word la':x.update(reading=r'\unsure{\deleted{la}|\deleted{les}|la}',alternatives='cancelled la; cancelled les; live la',reason=E['B22'],confidence='low')
for place,reading,alt,b,conf in [
 ('Opening verb accent',r'\unsure{reconstituer|réconstituer}','no accent; accent','B03','medium'),
 ('Cancelled given-graph ending',r'\unsure{donné|donnés}','donné; donnés','B04','low'),
 ('NB margin, contents ending',r'\unsure{contenus|contenu}','plural s; terminal word exit','B09','medium'),
 ('Cancelled phrase before des cas',r'\deleted{\unsure{de ces|des} opérations}','de ces; des','B18','low'),
 ('Source annotation, opening and short connective',r'\unsure{les|un} ; \unsure{avec|ou}','les/un; avec/ou','B22','low'),
 ('Source annotation, donnée ending',r'\unsure{donnée|donné}','donnée; donné','B22','medium')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alt,confidence=conf,reason=E[b]))
r['notes'].append(dict(id=p+'-N-audit',text='All twenty-one unequal boxes were adjudicated after the independent second TSV was frozen. The opening adjective is essentielle: an enlarged detail shows the detached i dot after t and before the two l loops. The equals abbreviations are retained. The word after the paired groupoids now favours connus while retaining alternatives. In the cancellations, the final article after foncteurs favours les, the old phrase before des cas may contain de ces, and the run replaced by structures exposes fl.-like letters, a possible opening parenthesis, des and unités/données. These remain doubtful beneath the strike. The target operator of the diminution arrow still has a bar and an upright and is not silently replaced by the mathematically expected minus. The annotation’s sous-ens. hyphen and the long margin separator are reproduced. No assertion of reconstructibility is independently proved.'))
extra=[f'crops/{p}_second_{z}.png' for z in ('B02_right','B03_overwritten','B09_rotated','B20_cancelled','B22_formula','B22_annotation','main_opening_word')]+[f'crops/{p}_second_connus.png']
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json','additional_existing_crops_viewed':extra}
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
