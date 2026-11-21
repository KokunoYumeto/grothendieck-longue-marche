from pathlib import Path
import csv,json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan062'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest()=='a5e132017d45a1147dbe97f8bafd8e59ce6bfcbbc6c7c4b2b6fb613561025e03'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B02':'After the looped d and dotted i, the compressed turning stroke admits r/s. The last stroke is low and flat rather than a securely closed a; dise is now first, but dira remains possible. The word is not resolved by French grammar.',
'B03':'The terminal e has a downturned exit that may include a small s. The crop does not safely distinguish unique from uniques, so the existing plural-first doubt remains.',
'B04':'The initial S is an ordinary rounded S, while T has its conspicuous looped head. D retains its separate stem and lower curl. The small S subscript is looped and crossed and still permits star/f. Merely making every capital calligraphic is unsupported by the differing pen forms.',
'B05':'The abbreviation has tall crossed t, closed o and descending p: top, not rep. The singular le foncteur and un-underlined Gamma remain. The opening compressed group can be avec or sur, and this uncertainty is now explicit. The lower sign has crossing curved arms, supporting chi/f, without the right angle of Gamma. The long insertion leader remains distinct from the word strokes.',
'B06':'The range has a 1, two dots, and a 7, each with a degree circle. The last s-like stroke of leurs is overworked, but a deliberate deletion cannot be decided. The last e of variante has an exit that may contain an s; the singular is now primary under explicit doubt. The initial ou and opening parenthesis are visible.',
'B08':'The margin consists of two physical lines, each with a separate underline: a l-exception, then de 4-degree et 5-degree. The words and numerals are unchanged; the two underline spans are now represented separately.',
'B09':'The upper old exponent is blackened and internally looped: 0/infinity remains doubtful and the local cancellation is preserved within the cancellation of the whole diagram. Crossed chi-like ink survives above the horizontal shaft. The parenthesized star at the lower left belongs to the live box, not to this old vertical arrow. Ens(nu) is the old downward target. The separate lower cancelled sloping arrow was followed in the boundary-extension crop; its apparent plus-minus is made by arrow/cancellation crossings, with no complete separate destination symbol. No new node is supplied there.',
'B10':'The live row has three objects and two right-pointing arrows, bounded by top, bottom and left strokes, with no right vertical. The star tag is beside this live frame. The annotation reads on siglera and its curved attachment is a leader. In the shorthand formula, g runs directly into nu; no separate comma is visible. On the lower rule the crossed small glyph has an E-like left stem and horizontal bars, rather than a securely closed empty-set oval; E is now first, with En and empty-set alternatives under the cancellation.',
'B11':'The rotated margin and its enlarged middle detail were viewed. The opening reads Ca ne suffit pas tout a fait, pour avoir toutes les operations, with a comma after fait. The word after qui has compressed overlapping strokes admitting demande/change. A long straight diagonal crosses the old lower group, so the deletion is retained, not read as a live le. The short quoted insertion remains uncertain ou; no confident extra g/nu word is supplied. The quoted structures and circled 4 and 5 remain. The final category index has closely joined looped strokes allowing infinity/nu, so the earlier resolution to infinity is reopened.',
'B12':'The initial S has the ordinary rounded upper and lower turns, and T has a large looped head. The 1, g, comma, nu and plus-minus are all present. The calligraphic-S difference does not justify a new glyph reading.',
'B13':'The S is rounded, the T is looped, and the subscript beneath S has crossing arms, supporting the star here. The lower top abbreviation has tall t and descending p. This is the existing S-star T-top notation.',
'B14':'The two card expressions, pi-zero, boundary X, nu and the final 1 are visible. The tiny subscript after C is a short thick horizontal mark without a separately legible a stem. A dash is now first, with a or a dot retained as alternatives. The following quantified a suggests an intended a, but does not supply it to this glyph.',
'B15':'A separate long opening curve is visible to the left of the p of pour. The words pour tout and the whole a-in-pi-zero-boundary-X formula are clear; the opening parenthesis is retained.',
'B16':'The added word begins with tall b, dotted i and a long p descender; the middle low on run is followed by a d ascender and the reduced ere ending. These strokes support bipondere, not bijection/bijective. Its curved leader attaches it to graphe.',
'B17':'The old T-g-nu has several diagonal cancellation strokes. The live triple has X, a retraced tilde-Sigma and R, with two vertical equality strokes to boundary X below the middle letter. Its strong upper and lower bars and interior diagonal are compatible with the established boundary-Sigma form; the looped retracing can look B/R-like, but no separate new letter or new cancellation is securely distinguishable. The whole existing formula is retained.',
'B18':'Five ray traces, including the faint central trace, converge on one black vertex labelled g. The heavy convergence strokes do not create independent directed arrowheads. The right-hand tall doubled curly stroke groups the free ends and carries nu; it is not an f with a nu exponent. The first TikZ rendering preserves this count, vertex, faint trace and hand-drawn brace.',
'B19':'The word after ces has a low a/r opening, an accent over the middle e and a tall t, supporting aretes rather than orbites. The following parenthesis reads libres. The next line has the compressed s/on/t run followed by de and poids, not an independent r_a formula. The numeral is 1 with an angled head and long base.',
'B20':'The upper context reads de facon correspondante, via, as already in the page. The two loop-and-stem signs in the bottom triple have stems crossing their loops, supporting the existing phi-shaped empty-set glyphs; no detached prime on the second is visible. The letters after the triple read ou-grave X de type g,nu. The original scan edge cuts the lowest strokes; no missing stroke is reconstructed. The two signs are kept as written phi, not regularized to a standard empty-set macro.',
'B21':'The isolated lower folio has a closed-bowl 6 followed by a tall 1 with an angled top. It is 61 in both readings; mspage versus margin is only the editorial wrapper.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
repls={
'B02':[(r'\unsure{dira|dise}',r'\unsure{dise|dira}')],
'B05':[(r'\inserted{avec le foncteur',r'\inserted{\unsure{avec|sur} le foncteur')],
'B06':[('leurs variantes',r'leur\unsure{s|\deleted{s}} \unsure{variante|variantes}')],
'B08':[(r'\uline{à l\'exception de $4^\circ$ et $5^\circ$}',r'\uline{à l\'exception}\\\uline{de $4^\circ$ et $5^\circ$}')],
'B09':[(r'\deleted{\unsure{0}}',r'\deleted{\unsure{0|\infty}}')],
'B10':[(r'\deleted{\unsure{\varnothing}}',r'\deleted{\unsure{E|\mathrm{En}|\varnothing}}')],
'B11':[('qui demande',r'qui \unsure{demande|change}'),(r'\mathcal T_{g,\infty}',r'\mathcal T_{g,\unsure{\infty|\nu}}')],
'B14':[(r'R\cap C_a',r'R\cap C_{\unsure{-|a|\cdot}}')]
}
# Apostrophes are literal source text, not TeX accent commands.
repls['B08']=[("\\uline{à l'exception de $4^\\circ$ et $5^\\circ$}","\\uline{à l'exception}\\\\\\uline{de $4^\\circ$ et $5^\\circ$}")]
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,rs in repls.items():
 v=C[b]['first']
 for a,z in rs:
  assert a in v and a in s,(b,a);v=v.replace(a,z);s=s.replace(a,z)
 D[b].update(choice='reading',reading=v)
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
def update(n,b,**kw):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02d}')
 x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],**kw)
update(1,'B02',final=r'\unsure{dise|dira}',diff_c=True,diff_h=False,confidence='medium')
update(4,'B05',final=r'\unsure{avec|sur} le foncteur')
update(12,'B09',final=r'S_1\mathcal T_{g,\nu}^{\deleted{\unsure{0|\infty}}\pm}')
for n in (13,14,15):update(n,'B09')
update(17,'B10',final=D['B10']['reading'])
for n in (18,19,20):update(n,'B10')
update(21,'B10',final=r'$\deleted{\unsure{E|\mathrm{En}|\varnothing}}$',diff_c=True,confidence='low')
update(29,'B11',final=r'$\mathcal T_{g,\unsure{\infty|\nu}}$',confidence='medium')
for n,b in ((31,'B15'),(32,'B18'),(33,'B19'),(34,'B20'),(35,'B20'),(36,'B20'),(37,'B21')):update(n,b)
def add(n,place,c,h,final,b,kind,err,confidence='medium',consequential=False):
 r['changes'].append(dict(id=f'{p}-{n:02d}',place=place,c=c,h=h,final=final,diff_c=True,diff_h=True,kind=kind,error_kind=err,evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],confidence=confidence,marked_in_h=False,consequential=consequential))
# The variant ending changes the primary lexical reading; other additions of doubt do not create material rows.
add(38,'Parenthesis after operation range, variant ending','variantes','variantes',r'\unsure{variante|variantes}','B06','misread word','Words','low')
add(39,'Boundary-component cardinality, tiny C subscript',r'C_a',r'C_a',r'C_{\unsure{-|a|\cdot}}','B14','misread symbol or index','Symbols and indices','low',True)
for x in r['decisions']:
 if x['id']=='M0760':x.update(decision='undecided',reading=r'\unsure{demande|change}',evidence=E['B11'],crop=f'crops/{p}_second_B11.png',box=boxes['B11'],confidence='low')
 if x['id']=='M0763':x.update(decision='undecided',reading=r'$\mathcal T_{g,\unsure{\infty|\nu}}$',evidence=E['B11'],crop=f'crops/{p}_second_B11.png',box=boxes['B11'],confidence='medium')
for x in r['doubts']:
 if x['place']=='Opening paragraph, qui':x.update(reading=r'\unsure{dise|dira}',alternatives='dise; dira',reason=E['B02'])
 if x['place']=='First cancelled diagram, old superscript':x.update(reading=r'\deleted{\unsure{0|\infty}}',alternatives='0; infinity',reason=E['B09'])
 if x['place']=='Erased sign on live frame bottom bar':x.update(reading=r'\deleted{\unsure{E|\mathrm{En}|\varnothing}}',alternatives='E; En; empty-set glyph',reason=E['B10'])
for place,reading,alt,b,conf in [
 ('Inserted opening preposition',r'\unsure{avec|sur}','avec; sur','B05','low'),
 ('Parenthesis, possessive and variant endings',r'leur\unsure{s|\deleted{s}} \unsure{variante|variantes}','live/cancelled s; variante/variantes','B06','low'),
 ('Diagonal margin, verb after qui',r'\unsure{demande|change}','demande; change','B11','low'),
 ('Diagonal margin, whole final category',r'$\mathcal T_{g,\unsure{\infty|\nu}}$','infinity; nu','B11','medium'),
 ('Cardinality formula, C subscript',r'$\operatorname{card}R\cap C_{\unsure{-|a|\cdot}}=1$','dash; a; dot','B14','low')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alt,confidence=conf,reason=E[b]))
r['notes'].append(dict(id=p+'-N-audit',text='The independent second reading was frozen before comparison, and the main reader viewed all nineteen unequal boxes. The most significant reopened readings are demande/change and infinity/nu in the crowded diagonal margin. The small C subscript in the cardinality condition is dash-like, with a/dot alternatives: the quantified a suggests what may be intended but does not settle the ink. The cancelled lower sloping diagram has no separately complete destination object. The star labels the live frame, whose lower crossed sign is E/En/empty-set under doubt. The fan has five visible ray traces including a faint central ray and a hand-drawn brace labelled nu. The final triple retains two phi-shaped empty-set glyphs with no added prime. These are visual checks; no reconstruction theorem was proved.'))
extra=[f'crops/{p}_second_main_old_destination.png',f'crops/{p}_second_main_margin_detail.png']
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json','additional_existing_crops_viewed':extra}
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
