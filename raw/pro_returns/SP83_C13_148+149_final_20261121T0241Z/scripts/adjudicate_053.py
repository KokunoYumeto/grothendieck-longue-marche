from pathlib import Path
import csv,json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan053'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B01':'The numeral has a closed upper loop and a long descending hooked tail: 9. The mspage wrapper records the same ink.',
'B04':'The opening pair of quote ticks and the accent over the first e are distinct. The final letter has a rising stroke and rightward cross/return reaching the black scan edge, supporting the existing terminal t. Only one closing quote stroke is wholly exposed; the closing quote count is now explicitly uncertain rather than silently supplied.',
'B05':'At left the oval/u-like group is crossed by oblique marginal ink; the apparent tall stroke can belong to that crossing. The first ou/du candidates remain, but the independent live les reading cannot be excluded, so deletion state is also marked uncertain. In the second group two separate descending p-like stems survive the long horizontal strike, one at the start and one near the middle, with a tall l after the latter. This favours two words pour plus/par plus over the former single-word plutot/purement candidates; buried letters remain doubtful.',
'B06':'The large G, short r and point, pond with its point, and rep ending at the descending p before the parenthesis agree. Math/text alphabet and spacing wrappers do not change that reading.',
'B07':'The old alors group has a tall l and a heavy low continuous stroke, but the crossing diagonal marginal letters make the cancellation extent uncertain. The first deletion is retained as the leading possibility, with a live alternative. On aura is clearly separate; the later p-descender belongs to the short crossed par group, not a live longer word.',
'B08':'A low three-hump une run and a longer group ending in descending/returning strokes remain under the cancellation. Une description stays a provisional reading rather than being replaced by an unqualified illegible token. The raised l-equivalent de has its own baseline and agrees in both readings.',
'B11':'Under the strike the d bowl/stem, apostrophe, rounded o, u and separate grave stroke favour d-ou, not deja. The live abbreviation has dotted i followed by a short intervening point/connector and an open e ending in a point: i.e., not ici.',
'B13':'The word ends with low -ent and a tall crossed t; its beginning and medial ascender intersect the oblique marginal note. Equivalent remains the leading tentative reading, but evident is a better surviving alternative than au-dessus. Evidemment is longer than the recoverable middle run. No complete word is asserted as certain.',
'B14':'The closing parenthesis is on the first line immediately after R prime. The two smaller lines de sommets- / reperes lie below sous ens., without a second closing parenthesis. Their added position is recorded as an insertion while the literal line placement and first-line parenthesis are retained; they are not moved to a reconstructed continuous parenthesis.',
'B15':'The short crossed word after et begins with a tall d; its low middle and final c-like return favour donc, as independently read, over d-ou. The strike still obscures the middle so both candidates are retained. The curved leader puts decrire before un foncteur. The quoted name continues just below the target line and is not removed merely because this crop trims that continuation.',
'B16':'The upper small word has an open first loop and two reduced joined groups; ens remains preferred, with avec now explicit as an alternative. The old large R has a lower loop that can be part of the letter or a zero, so R/R_0 remains doubtful. The cleaner R prime is raised to its right and is now marked inserted. The label has a short detached stroke to the right of R, with no distinct digit foot; in the repeated local R-prime notation it is retained as a low prime. Two arrowheads on one shaft are preserved.',
'B17':'The strike crosses Cela and the whole s-exprime, sur le line. The verbal ending reaches a short e-like return before the comma; there is no extra ra run. The first s-exprime reading is retained.',
'B19':'All five arrows and the two diagonal converging shafts agree. In the left arrow label the old R-like body is overwritten at the start of marquage, with the cleaner R prime below; marquage and that R prime are recorded as the replacement insertion. The crossed glyph after the lower D admits sharp/R and is not regularized to a new category index. At the bottom the hatching reaches the tall b-like group but stops before the separate dotted upright i; i is live. The side note starts gr. plus une (short gr with point, then p descender/l ascender and a separate une), not graphes avec. Its weight glyph has a closed low oval and a long top return: sigma is the primary local candidate, gamma retained as an explicit alternative. The following mais/non par r and trailing comma remain.',
'B21':'The pale 5 has a detached top bar and lower bowl; the 2 has a curved head, diagonal and long foot. The mspage wrapper records the same 52.',
'B22':'The fine oblique baseline has NB, Cette operation, a l-air d-un, the underlined affaiblissement, de structure, then mais and the repeated affaiblissement. The small cet is covered by crossing darker main text and is now doubtful. The initial sur/pour remains unresolved. The separate component capital C, Sigma plus, quoted gomme and underlined tous belong to the margin. The following C is a short open capital, not the main-line word contour imported from a crossing baseline. Existing uncertainty on the tiny cancelled ce is retained. Overlapping lower context read in the second TSV is covered by the following boxes and is not duplicated.',
'B23':'The fine-line opening has an s-shaped turn and dotted i before non: sinon, followed by c-est au contraire. The p descender/l/t/acute-o/t of plutot and the separate dans le sens d-un run are visible. Renforcement de structure and the next dash/ou plutot, des form consecutive lines. Mais and added lower fragments in the blind reading partly result from crossing main text or overlap with B22/B24; no duplicate marginal lines are inserted.',
'B24':'The large fine-pen R-prime_C=R-prime cap C lies on the continuation of the preceding marginal phrase; there is no visible leader establishing a separate insertion. The category line has categories isotopiques, with its g/p/q descenders distinct from the heavier crossing diagram. The raised l-operation de gommage et celles is above the cancelled phrase; surmarquage and the parenthetic plus bas follow. These are not sous-groupes or les images. The uncertain early marquages/groupoides, du nombre de/du meme type, buried cancelled phrase and correspondantes remain explicitly provisional. The inverse and equivalence clauses are separate visible fine baselines.',
'B25':'The final fine lines read Il faudrait separer les deux cas, pour distinguer ces. Separer has an s start, accented e and a p descender, rather than an extra distinguer bien. Operations de gommage and essentielles have distinct underline strokes. Below them the g/p descenders in groupe distinguish it from genre; the abbreviated autom. and closing parenthesis are visible farther right on the oblique line. The last line reads et les autres, not contours. Canonical B25 and the already existing wide clause-3 crop were both inspected to include the partly trimmed line ends.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
repls={
'B04':[("``réconstruit''",r"``réconstruit\unsure{''|'}")],
'B05':[(r'\deleted{\unsure{ou|du}}',r'\unsure{\deleted{\unsure{ou|du}}|les}'),(r'\deleted{\unsure{plutôt|purement}}',r'\deleted{\unsure{pour plus|par plus}}')],
'B07':[(r'\deleted{\unsure{alors}}',r'\unsure{\deleted{alors}|alors}')],
'B13':[(r'\unsure{équivalent|au-dessus}',r'\unsure{équivalent|évident}')],
'B14':[(r'\text{de sommets-}',r'\inserted{\text{de sommets-}}'),(r'\text{repères}',r'\inserted{\text{repères}}')],
'B15':[(r"\deleted{\unsure{d'où}}",r"\deleted{\unsure{donc|d'où}}")],
'B16':[(r'\text{ens}',r'\text{\unsure{ens|avec}}'),(r"\deleted{\unsure{R_0|R}}R'",r"\deleted{\unsure{R|R_0}}\inserted{R'}")],
'B19':[(r"\text{ marquage}\\R'",r"\inserted{\text{ marquage}}\\\inserted{R'}"),(r'\deleted{\unsure{\#}}',r'\deleted{\unsure{\#|R}}'),(r'\deleted{\unsure{\mathrm{bi}}}\mathrm{pond}',r'\deleted{\unsure{\mathrm{b}|\mathrm{ph}}}\mathrm{i\ pond}'),(r'\text{graphes avec}',r'\text{gr. plus une}'),(r'\gamma',r'\unsure{\sigma|\gamma}')],
'B22':[(r'mais cet affaiblissement',r'mais \unsure{cet} affaiblissement')]}
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,rs in repls.items():
 v=C[b]['first']
 for a,z in rs:
  assert a in v,(b,a);v=v.replace(a,z)
  if a in s:s=s.replace(a,z)
  else:assert z in s,(b,a)
 D[b].update(choice='reading',reading=v)
# Keep the separately visible underline strokes without changing the reading count.
a=r'\uline{opérations de gommage essentielles}';z=r'\uline{opérations de gommage} \uline{essentielles}'
assert a in s;s=s.replace(a,z)
D['B25'].update(choice='reading',reading=C['B25']['first'].replace(a,z))
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
def update(n,b,**kw):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02d}')
 x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],**kw)
update(3,'B04',final=r"``réconstruit\unsure{''|'}",confidence='medium')
update(4,'B05',final=r'\unsure{\deleted{\unsure{ou|du}}|les}')
update(5,'B05',final=r'\deleted{\unsure{pour plus|par plus}}',diff_h=True)
update(8,'B07',final=r'\unsure{\deleted{alors}|alors}')
update(16,'B13',final=r'\unsure{équivalent|évident}')
update(18,'B14',final=r"\begin{gathered}(\text{à sous ens. marqué }R')\\\inserted{\text{de sommets-}}\\\inserted{\text{repères}}\end{gathered}",confidence='medium')
update(19,'B15',final=r"et \deleted{\unsure{donc|d'où}}",diff_c=True,kind='misread word',error_kind='Struck text',confidence='low')
update(20,'B16',final=r"\overset{\text{\unsure{ens|avec}}}{\deleted{\unsure{R|R_0}}\inserted{R'}}",confidence='medium')
update(21,'B16',final=r"\deleted{\unsure{R|R_0}}\inserted{R'}")
update(25,'B19',final=D['B19']['reading'])
update(26,'B19',final=r"\text{oubli du }\deleted{\unsure{R'}}\inserted{\text{ marquage }R'}",diff_c=True,kind='insertion or placement',error_kind='Insertions put in the wrong place')
update(27,'B19',final=r'S_*\mathcal TD\deleted{\unsure{\#|R}}_{\mathrm{top}}^\pm')
update(28,'B19',final=r'\mathrm{Gra}\deleted{\unsure{\mathrm{b}|\mathrm{ph}}}\mathrm{i\ pond}')
update(29,'B19',final=r'\deleted{\unsure{\mathrm{b}|\mathrm{ph}}}\mathrm{i}',diff_c=True,confidence='medium')
update(34,'B22',final=r'\unsure{cet} affaiblissement',confidence='low')
update(58,'B25',final=z)
for n,place,c,h,final,kind,error,conf,cons in [
 (61,'Lower diagram side note opening','graphes avec','graphes avec','gr. plus une','misread word','Words','high',False),
 (62,'Lower diagram weighting symbol',r'\gamma',r'\gamma',r'\unsure{\sigma|\gamma}','misread symbol or index','Symbols and indices','medium',True)]:
 r['changes'].append(dict(id=f'{p}-{n:02d}',place=place,c=c,h=h,final=final,diff_c=True,diff_h=True,kind=kind,error_kind=error,evidence=E['B19'],crop=f'crops/{p}_second_B19.png',box=boxes['B19'],confidence=conf,marked_in_h=False,consequential=cons))
for x in r['decisions']:
 if x['id']=='M0715':x.update(reading=r'\unsure{équivalent|évident}',evidence=E['B13'],crop=f'crops/{p}_second_B13.png',box=boxes['B13'])
for x in r['doubts']:
 old=x['reading']
 for b,rs in repls.items():
  for a,z1 in rs:old=old.replace(a,z1)
 x['reading']=old
 if x['place']=='Main cancelled first word':x.update(alternatives='cancelled ou/du; live les; cancellation extent uncertain',reason=E['B05'])
 if x['place']=='Main cancelled second word':x.update(alternatives='pour plus; par plus',reason=E['B05'])
 if x['place']=='Main cancelled alors':x.update(alternatives='alors cancelled; alors live',reason=E['B07'])
 if x['place']=='Main word after groupoïde':x.update(alternatives='équivalent; évident; not every initial letter separable',reason=E['B13'])
 if x['place']=='Main later cancelled d’où':x.update(alternatives="donc; d'où",reason=E['B15'])
 if x['place']=='Horizontal diagram old marked-set symbol':x.update(reading=r'\deleted{\unsure{R|R_0}}',alternatives='R; R_0',reason=E['B16'])
 if x['place']=='Lower diagram extra cancelled object sign':x.update(alternatives='sharp; R-like old glyph',reason=E['B19'])
 if x['place']=='Lower graph object cancelled bi':x.update(reading=r'\deleted{\unsure{\mathrm{b}|\mathrm{ph}}}\mathrm{i}',alternatives='old b; ph; adjacent dotted i live',reason=E['B19'])
for place,reading,alt,conf,b in [
 ('Closing quote at right scan edge',r"\unsure{''|'}",'two ticks; one visible tick','medium','B04'),
 ('Small word over horizontal marked-set source',r'\unsure{ens|avec}','ens; avec','medium','B16'),
 ('Weight symbol in diagram side note',r'\unsure{\sigma|\gamma}','sigma; gamma','medium','B19'),
 ('Crossed overlap after marginal mais',r'\unsure{cet}','cet, letters partly covered','low','B22')]:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alt,confidence=conf,reason=E[b]))
for x in r['inventory']:
 if x['element']=='E03':x['first_words_or_objects']='ou/du versus live les; cancelled pour plus/par plus'
 if x['element']=='E10':x['first_words_or_objects']=x['first_words_or_objects'].replace('équivalent / au-dessus','équivalent / évident')
 if x['element']=='E13':x['first_words_or_objects']="donc / d'où"
 if x['element']=='E19':x['first_words_or_objects']='Three S_*TD objects converge through Gra / cancelled b or ph / live i pond, then arrow to gr. plus une pondération par sigma/gamma, mais non par r'
 if x['element']=='E21':x['first_words_or_objects']='b / ph cancelled, adjacent dotted i live'
for after,elem,pos,words in [('E11','E28','Below first-line parenthetical qualifier','de sommets- / repères'),('E16','E29','Raised to right of cancelled old R in horizontal source',"R'"),('E20','E30','Replacement of old arrow-label R and continuation below',"marquage R'")]:
 i=next(i for i,x in enumerate(r['inventory']) if x['element']==after)+1
 r['inventory'].insert(i,dict(element=elem,sheet_kind='text',hand='his hand',kind='insertion',position=pos,first_words_or_objects=words,transcribed='yes'))
for x in r['notation']:
 if x['sign']==r'\gamma':x.update(sign=r'\unsure{\sigma|\gamma}',meaning_or_form='The low closed oval and long top return favour sigma locally; gamma remains an explicit alternative pending consistency review.',universality='One overlapping local occurrence; no global substitution is made.',witness_errors='Both witnesses give gamma here; independent reading and main crop review preserve sigma/gamma uncertainty.')
 if x['sign']=='Gra, Gr.; cancelled bi':x.update(sign='Gra, Gr.; cancelled b/ph, live i',meaning_or_form='The first target is Gr. pond. rep without final point. The bottom target is Gra, then a hatched b/ph-like group and a separate live dotted i before pond.',witness_errors='Both witnesses extend or misrepresent the bottom cancellation; i lies outside the hatching.')
r['notes'].append(dict(id=p+'-N-audit',text='The blind reading was frozen before token comparison. Every unequal box was re-viewed. The lower side note is gr. plus une, and the hatching excludes the adjacent dotted i. Its weight glyph is now sigma/gamma rather than unqualified gamma; the mathematical weighting context does not erase the visible loop/top-bar ambiguity. The two descenders in the opening cancellation favour pour plus/par plus. Additional insertion states and remaining overlap uncertainties are explicit. The diagonal margin is read by its fine baselines: categories isotopiques, the gommage/surmarquage insertion, separate inverse/equivalence clauses, separer les deux cas, essentielles, groupe des autom., and et les autres. Large crossing main symbols and repeated contextual fragments are not imported into that note.'))
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json','additional_existing_crops_viewed':[f'crops/{p}_second_detail_{v}.png' for v in ['upper','middle','lower','end']]+[f'crops/{p}_margin_clause3.png',f'crops/{p}_margin1.png']}
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+r['second_main_review']['additional_existing_crops_viewed']))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
