"""Root decisions for 123/019, assembled only after comparing all three returns."""
from pathlib import Path
import json, copy

O=Path('out');stem='C123-01_123_scan019'
R={r:json.loads((O/'readers'/stem/r/'report.json').read_text()) for r in ('R1','R2','R3')}
T={r:(O/'readers'/stem/r/'reading.tex').read_text() for r in R}
r1=f'readers/{stem}/R1/crops/';r2=f'readers/{stem}/R2/crops/';r3=f'readers/{stem}/R3/crops/';rc=f'decisions/rootcrops/{stem}/'
t=T['R3']
def replace(old,new,count=1):
    global t
    assert t.count(old)==count,(old,t.count(old))
    t=t.replace(old,new)

replace(r'i_{\unsure{o|0}}',r'i_o')
replace(r'{$Z_o$}',r'{$Z_{\unsure{o|0}}$}')
replace(r'\unsure{\mathbin{.}}e',r'\unsure{\mathord{\cdot}}e')
# The faint U-shaped lower trace is visible separately below the main arrowhead.
trace=T['R2'][T['R2'].index(r'\arrow[d,draw=gray'):T['R2'].index('\n\\& \\operatorname{Dyn}_c')]
replace(r'\handwritten{\arrow[d]} \& \operatorname{Dyn}_c',
        '\\handwritten{\\arrow[d]}\n'+trace+'\n\\& \\operatorname{Dyn}_c')
# A lower closed oval is superposed on the n of the later Dyn.
dyn=T['R2'].split('en existe un de $',1)[1].split('$ \\deleted{i.e.',1)[0]
replace(r'en existe un de $\operatorname{Dyn}_c$',r'en existe un de $'+dyn+'$')
replace(r'\deleted{i.e. que $G$ soit quasi-déployé;}',r'\deleted{i.e. que $G$ soit quasi-déployé\unsure{;}}')
replace(r'(i.e., si $Z_o=e$',r'(i.e.,, si $Z_o=e$')
replace(r'\deleted{les $i$}',r'\deleted{\unsure{les|des} $i$}'+
        r'\begin{tikzpicture}[baseline=-.1ex]\draw[line width=.3pt](0,0)--(.48em,.8ex);\draw[line width=.3pt](0,.8ex)--(.48em,0);\end{tikzpicture}')
replace(r'\deleted{point rationnel}',r'\deleted{point rationnel}'+
        r'\begin{tikzpicture}[baseline=-.1ex]\draw[line width=.3pt](0,0)--(.48em,.8ex);\draw[line width=.3pt](0,.8ex)--(.48em,0);\end{tikzpicture}')
replace(r'$\unsure{\overline{m}|\overline{me}}$',r'$\overline{m}$')
# Retain the strong horizontal crossing stroke on the crowded final parenthesis.
replace(r'{Kostant\unsure{)}};',r'{Kostant\unsure{)}};'+'\n'+
        r'\draw[line width=.65pt] ([xshift=-.48em,yshift=.4ex]kostant.base east)--++(.62em,.03ex);')
# Preserve the e-like body and its extra upper-right trace without inventing an order.
ending=r'invariant\unsure{\begin{tikzpicture}[baseline=(endletter.base)]\node[inner sep=0pt,anchor=base] (endletter) at (0,0) {e};\draw[line width=.3pt] ([xshift=.37em,yshift=.82ex]endletter.base west)--++(-.04em,.5ex)--++(-.1em,.12ex);\draw[line width=.25pt] ([xshift=.40em,yshift=.45ex]endletter.base west) .. controls +(.02em,-.25ex) and +(.12em,-.02ex) .. ([xshift=.23em,yshift=.05ex]endletter.base west);\end{tikzpicture}}'
replace(r'\unsure{invariantè|invariante}',ending)
pm=T['R2'].split('donné\n',1)[1].split('\négalement',1)[0]
replace(r'\deleted{p}marche',pm)
replace(r'[rotate=20,transform shape]',r'[rotate=24,transform shape]')
replace(r'pour $A_2,A_4$',r'pour $\unsure{A|\mathbb{A}}_2,A_4$')
replace(r'si\unsure{:|'+ "''"+'}',r'si:')
replace(r'\inserted{classes \handwritten{de}}',r'\inserted{classes\,\raisebox{.45ex}{\handwritten{de}}}')
oldstroke=r'\begin{tikzpicture}[baseline=-.2ex]\draw[line width=.7pt] (0,-.025) -- (.25,.045);\end{tikzpicture}'
newstroke=r'\begin{tikzpicture}[baseline=-.2ex]\draw[line width=.7pt] (0,-.025) -- (.25,.045);\draw[line width=.2pt,gray!50] (.025,.07)--(.25,.17);\end{tikzpicture}'
replace(oldstroke,newstroke)
replace(r'\deleted{aux}',r'\deleted{\unsure{aue|aux}}')

# The three complete readings have been compared. Apparatus follows below.
spec=dict(stem=stem,base_reader='R3',brief='reader_v07.md',main_new_crops=1,
          text_edits=[dict(old=T['R3'],new=t)],difference_overrides={},additional_differences=[])
def ov(n,**kw):spec['difference_overrides'].setdefault(f'R3-D{n:02}',{}).update(kw)
cropmap={
1:r3+'29_des_top.png',2:r3+'29_des_top.png',3:r1+'01_maps.jpg',4:r1+'01_maps.jpg',5:r1+'01_maps.jpg',
6:r1+'04_deligne_map.jpg',7:r2+'06_main_square.png',8:r2+'06_main_square.png',
9:r2+'07_margin_square.png',10:r2+'07_margin_square.png',11:r2+'07_margin_square.png',
12:r1+'07_cancelled_dyn.jpg',13:r1+'23_paragraph_par.jpg',14:r1+'09_condition_end.jpg',
15:r1+'08_condition_start.jpg',16:r1+'09_condition_end.jpg',17:r1+'10_ceci.jpg',
18:r1+'12_point_rationnel.jpg',19:r2+'14_levi_insert.png',20:r2+'14_levi_insert.png',
21:r2+'14_levi_insert.png',22:rc+'deleted_aux.png',23:r3+'16_g2_deleted_clause.png',
24:r3+'16_g2_deleted_clause.png',25:r3+'16_g2_deleted_clause.png',26:r2+'16_dynkin_kostant.png',
27:r2+'16_dynkin_kostant.png',28:r1+'18_de_c.jpg',29:r3+'19_invariante_gamma.png',
30:r1+'16_marche.jpg',31:r2+'20_margin_note.png',32:r2+'20_margin_note.png',
33:r2+'20_margin_note.png',34:r2+'20_margin_note.png',35:r3+'23_des.png',
36:r2+'21_classes_parabol.png',37:r2+'21_classes_parabol.png',38:r1+'21_si.jpg',
39:r1+'20_autext.jpg',40:r1+'22_fib.jpg'}
for n,crop in cropmap.items():ov(n,crop=crop)
ov(1,confidence='low')
ov(2,confidence='low',evidence='The cell has an e-like upper counter and middle bar plus a serifed left upright and closed lower contour. The n/e overlay is tentative; an a-like or damaged repeated impression remains possible. No chronology is imposed.')
ov(4,confidence='high',evidence='The second sign has a compact pointed right terminal with short returning branches, unlike the blunt first endpoint. The later c-to-c-prime crop provides a local comparison of the same rightward tip.')
ov(5,final='i_o and u_o',c_changed=True,confidence='high',evidence='Both lowered typewriter rings have lowercase x-height, matching the ordinary o in nearby typed words and smaller than the capitals. They are resolved as o. Handwritten rings are treated separately.')
ov(8,c_changed=True,evidence='A definite round full stop stands on the lower row to the right of Un_c. C serializes it after the small square; H omits it. The final puts it beside its source object.')
ov(9,final='Doubtful Z with extra central/lower strokes drawn.',evidence='The upper bar, diagonal and lower bar support Z; a dense central upright extends through and below the lower bar. Its predecessor and chronology are unresolved. The detached handwritten ring is collated separately.')
ov(11,final=r'(\unsure{\mathord{\cdot}}e)',evidence='A detached small black point lies between the opening parenthesis and e at about mid-letter height. It is drawn as a point with doubt about its function, not asserted to be multiplication.',confidence='low')
ov(13,evidence='The heavy form retains a closed outer oval, a diagonal lower-left-to-upper-right slash and an independent underline. Its extra interior ink does not create a vertical phi stem; the slashed-oval form is resolved.')
ov(14,evidence='The handwritten replacement has e-s-t, not the s-o-i-t of H. It occupies the line above the cancelled typed condition, and its closing parenthesis has its own colon. The final serializes old cancelled wording then the upper replacement; H serializes these in the reverse order. The same correction anchor is understood, so that serialization alone is not counted as another error.')
ov(16,final=r'\deleted{i.e. que $G$ soit quasi-déployé\unsure{;}}',h_changed=True,confidence='low',kind='other',
   evidence='The heavy terminal stroke masks the old punctuation. A top point/lower tail supports a semicolon, but its full form is not separable from the cancellation. The new raised closing parenthesis and colon are distinct.')
ov(17,final=r'\deleted{\unsure{les|des} $i$}',confidence='medium',
   evidence='An initial ascender, e/s contours, a gap and a dotted i survive the x row. Ceci is not supported. The first covered cell still permits l or d, so the les/des doubt remains; a final separate x is collated independently.')
ov(20,final=r'ou ce qui revient au $\overline{m}$',confidence='high',
   evidence='After au there is one compact two-humped m-like form under a detached bar. No separate e or following m/e sequence is recoverable. The barred abbreviation is retained; même is offered only as an editorial expansion.')
ov(22,final=r'\deleted{\unsure{aue|aux}}',c_changed=True,confidence='low',kind='misread word',
   evidence='Root’s new local crop shows an a-like first bowl, a heavily crossed middle cell supporting u, and an e-like final counter/middle bar with a lower open return. A clean final x is not secure. The tentative aue reading and the readers’ aux alternative are both retained; no grammatical repair is made.')
ov(27,final='Doubtful closing parenthesis with a strong transverse stroke drawn through it.',c_changed=True,kind='drawing or diagram',
   evidence='The tall right-curving form supports a parenthesis, but a thick horizontal stroke crosses its middle and the lower end is overdrawn. Both the curve and crossing are retained; no hidden predecessor is supplied.')
ov(29,final='invariant followed by a doubtful e-like body and extra upper-right/closing traces drawn in TikZ.',c_changed=True,
   evidence='The final cell has an e-like counter/bar, a partly closed lower contour and a short rising trace at its upper right. It is not a clean detached centered grave. The contours are preserved graphically without choosing an accent or a chronological e/d-type overprint.')
ov(30,final='m and p contours superposed in the same cell, followed by arche; chronology uncertain.',
   confidence='medium',kind='deletion state (struck given live or live given struck)',
   evidence='The p descender and basal serif are definite beneath the m-like shoulders. The overlapping strokes establish both contours but not their order. The final preserves the same-cell overlap instead of serializing a definitely deleted p before a live m.')
ov(33,C="(cela l'est pour $A_3$)",H="(\\uncertain{cela vaut} pour $A_3$)",final="(cela l'est pour $A_3$)")
ov(34,C=R['R3']['differences'][33]['C'].replace("\\'","'"),H=R['R3']['differences'][33]['H'].replace("\\'","'"))
ov(35,confidence='high',evidence='The d bowl/right ascender and a separate interior l-like upright with its own top serif coexist. Both are retained graphically. C and H each simplify one contour; the sequence of impressions remains undetermined.')
ov(36,final='Typed classes with handwritten de raised at its right, plus the connected lower curve.',
   evidence='The regular typed classes baseline is lower than the small handwritten de. The thin curve starts before sous-groupes, bows under the addition and turns up below de. The different heights and connected shape are retained.')
ov(37,final='Dark rising connector and a fainter oblique trace above it, both drawn with doubt.',
   evidence='A dark stroke joins the lower b region to the left side of o across the enlarged gap; a separate pale oblique trace rises above it. Both are drawn. Their lexical force and correction order remain unresolved.')
ov(38,final='si:',c_changed=False,confidence='high',
   evidence='Two distinct compact points are present, one slightly above/right of the other. Neither shows a clear long quotation stem or tail. Root resolves the tilted colon, retaining C’s punctuation against H’s omission.')
ov(39,confidence='high',evidence='The lowered typewriter ring has the same lowercase x-height as the opening o indices. The capital A in Autext and G have ordinary single contours. The literal name is Autext, with t.')

# Exact reader alternatives are retained even when the root chooses a fourth form.
lookup={r:{d['id']:d['reading'] for d in R[r]['differences']} for r in R}
def rd(r,key):
    return lookup[r].get(key,key)
links={
1:('des without an overprint representation','R2-01'),2:('des without an overprint representation','R2-01'),
3:('R1-D01','R2-02'),4:('R1-D03','R2-03'),5:('R1-D02','R2-04'),
6:('R1-D05','R2-06'),7:('R1-D06','R2-07'),8:('R1-D07','Period retained after the diagram block; omitted from R2 difference list'),
9:('R1-D08','R2-09'),10:('R1-D10','R2-11'),11:('R1-D11','R2-12'),
12:('R1-D12','R2-13'),13:('R1-D13','R2-14'),14:('R1-D16','R2-17'),15:('R1-D15','R2-18'),
16:('R1-D17','R2-16'),17:('R1-D18','R2-19'),18:('R1-D20','R2-21'),
19:('R1-D22','R2-22'),20:('R1-D23','R2-23'),21:('R1-D24','R2-24'),
22:('R1-D25','R2-25'),23:('R1-D26','R2-26'),24:('(2), no underline doubt','(2), no underline doubt'),
25:('R1-D27','R2-27'),26:('R1-D28','R2-28'),27:('R1-D29','R2-29'),
28:('R1-D30','R2-30'),29:('R1-D31','R2-31'),30:('R1-D32','R2-32'),
31:('R1-D33','R2-33'),32:('R1-D34','R2-34'),33:('R1-D35','R2-35'),
34:('R1-D37','R2-36'),35:('R1-D38','R2-37'),36:('R1-D39','R2-38'),
37:('R1-D40','R2-39'),38:('R1-D41','R2-40'),39:('R1-D42','R2-41'),40:('R1-D43','R2-42')}
for n,(one,two) in links.items():
    d=R['R3']['differences'][n-1]; assert d['id']==f'R3-D{n:02}'
    final=spec['difference_overrides'][d['id']].get('final',d['reading'])
    readings='R1: '+rd('R1',one)+'; R2: '+rd('R2',two)+'; R3: '+d['reading']+'. Root: '+final
    if n==5:readings+=' R1 and R2 also independently resolve u_o; R3 carries the initial o/0 doubt to u.'
    ov(n,readers=readings)

def add(source,ident,newid,**kw):
    d=copy.deepcopy(next(d for d in R[source]['differences'] if d['id']==ident))
    d.update(id=newid,final=d.pop('reading'),marked_in_H='no')
    d.update(kw);spec['additional_differences'].append(d)
add('R1','R1-D14','ROOT-01',final='(i.e.,, si',confidence='high',
    readers='R1: two commas | one; R2: one comma; R3: one comma. Root retains both visible comma strokes.',
    evidence='Two separate low strokes with descending tails occur after the e stop and before si. Both are in the handwritten addition, above the cancelled typed line. They are retained as a source double-comma slip.',crop=r1+'08_condition_start.jpg')
add('R1','R1-D19','ROOT-02',final='A separate cancelling x reproduced by two drawn diagonal strokes.',readers='R1: separate final x; R2: same; R3: no separate representation. Root draws the additional cancelling cell.',crop=r1+'10_ceci.jpg')
add('R1','R1-D21','ROOT-03',readers='R1: additional x after the final l; R2: no separate representation; R3: no separate representation. Root retains the visible extra cell.',crop=r1+'12_point_rationnel.jpg')
add('R1','R1-D36','ROOT-04',readers=r'R1: \unsure{A|\mathbb{A}}_2; R2: A_2; R3: A_2. Root retains the local double-contour doubt.',crop=r2+'20_margin_note.png')
add('R2','R2-08','ROOT-05',final='Faint U-shaped trace drawn below the dark downward arrowhead; its origin is not assigned.',
    readers='R1: not represented; R2: faint U trace; R3: not represented. Root draws the visible pale contour without assigning it another arrow or label.',crop=r2+'06_main_square.png')
add('R2','R2-15','ROOT-06',readers='R1: Dyn_c; R2: uncertain n/o overlay after Dy; R3: Dyn_c. Root preserves the local mixed contours with uncertainty.',crop=r2+'10_dyn_body.png')
add('R1','R1-D09','ROOT-07',readers='R1: handwritten o|0; R2: handwritten o|0; R3: o under the earlier general ring doubt. Root keeps a separate first handwritten o|0 doubt here.',crop=r2+'07_margin_square.png')

ov(37,readers='R1: one dark stroke drawn; R2: dark stroke plus pale upper trace drawn; R3: one stroke drawn although its report describes the pale trace. Root preserves both visible traces.')
spec['difference_overrides']['R3-D14']['readers']+=' R2 explicitly wraps the colon as handwritten; R1 and R3 leave that same colon unwrapped. The final retains the unwrapped character while the inventory records its hand and raised position. This wrapper-only distinction is not counted as a separate change.'

cd=copy.deepcopy(R['R1']['c_doubts'])
for d in cd:
    ident=d['id']
    if ident=='R1-CQ07':d['decision']=r'Prefer \mathfrak z, retain z/Z; preserve a doubtful mid-height point before e without assigning it mathematical meaning.'
    if ident=='R1-CQ10':d.update(decision=spec['difference_overrides']['R3-D27']['final'],evidence=spec['difference_overrides']['R3-D27']['evidence'],crop=r2+'16_dynkin_kostant.png')
    if ident=='R1-CQ11':d.update(decision=spec['difference_overrides']['R3-D29']['final'],evidence=spec['difference_overrides']['R3-D29']['evidence'],crop=r3+'19_invariante_gamma.png')
    if ident=='R1-CQ12':d.update(decision=spec['difference_overrides']['R3-D30']['final'],evidence=spec['difference_overrides']['R3-D30']['evidence'],confidence='medium')
    if ident=='R1-CQ14':d.update(decision=spec['difference_overrides']['R3-D37']['final'],evidence=spec['difference_overrides']['R3-D37']['evidence'],crop=r2+'21_classes_parabol.png')
spec['c_doubts']=cd
spec['remaining_doubts']=[
dict(place='Opening des, first cell',reading='u/d-like contours superposed',alternatives='damaged or repeated d; chronology not established',confidence='low'),
dict(place='Opening des, second cell',reading='n/e-like contours superposed',alternatives='a-like lower contour or damaged repeated e; order unresolved',confidence='low'),
dict(place='First map sign',reading='barred shaft',alternatives='mapsto; right terminal not resolved',confidence='medium'),
dict(place='Faint U below main left arrowhead',reading='pale U-shaped trace',alternatives='earlier ink or scan/paper trace; no extra arrow asserted',confidence='low'),
dict(place='Small square upper-right letter',reading='Z-like form plus central/lower overprint',alternatives='predecessor and order not separable',confidence='low'),
dict(place='Small square handwritten index',reading='o',alternatives='0; later handwritten Z uses the same first candidate',confidence='medium'),
dict(place='Small square lower-right letter',reading=r'\mathfrak z',alternatives='z; Z',confidence='medium'),
dict(place='Small square before e',reading='detached point',alternatives='intentional mark or incidental pen spot',confidence='low'),
dict(place='Later Dyn final cell',reading='n/o overlay',alternatives='damaged or repeated n; order unknown',confidence='low'),
dict(place='Cancelled quasi-déployé terminal',reading=';',alternatives='covered punctuation/cancellation trace',confidence='low'),
dict(place='Cancelled group after choisi',reading='les i',alternatives='des i',confidence='medium'),
dict(place='Cancelled word before s’adaptent',reading='aue',alternatives='aux; middle cell strongly crossed, final contour e-like',confidence='low'),
dict(place='Lie-algebra letter',reading=r'\mathfrak g',alternatives=r'\mathscr G',confidence='medium'),
dict(place='Numeral in g(2)',reading='2',alternatives='underlined 2 or retraced lower foot',confidence='low'),
dict(place='Closing mark after Kostant',reading=') with a transverse stroke',alternatives='covered additional form inseparable',confidence='medium'),
dict(place='Final cell of invariante',reading='e-like body with upper-right trace',alternatives='grave-like accent; e/d-type overprint; chronology unknown',confidence='medium'),
dict(place='First cell of marche',reading='m and p superposed',alternatives='order of impressions undetermined',confidence='medium'),
dict(place='First A in margin',reading='A',alternatives=r'\mathbb A or retracing',confidence='low'),
dict(place='Inside paraboliques',reading='dark connector plus pale upper trace',alternatives='lexical hyphen or joining correction; order unknown',confidence='medium')]

inv=copy.deepcopy(R['R3']['inventory'])
for d in inv:
    d['hand']=d['hand'].replace('typewritten','typewriter').replace('handwritten','unnamed hand')
    if d['element']=='Overtyped p beneath marche':d.update(kind='drawing',element='Same-cell m/p overlap in marche',first_words_or_objects='m and p contours; no chronological state assigned')
    if d['element']=='Cancelled aux':d.update(element='Cancelled three-letter word before s’adaptent',first_words_or_objects='aue | aux, uncertain under x strikes')
    if d['element']=='Replacement quasi-deployed condition':d['first_words_or_objects']="(i.e.,, si Z_o=e, / que G est quasi-déployé)"
    if d['element']=='Equivalence insertion and connected curve':d['first_words_or_objects']='ou ce qui revient au barred m'
    if d['element']=='Two marks after si':d['first_words_or_objects']='colon resolved from two points'
    if d['element']=='Joining stroke between b and o':d['first_words_or_objects']='dark rising connector and faint upper oblique trace'
    if d['element']=='classes de addition and connected curve':d['first_words_or_objects']='typed classes with handwritten de raised at right, and connected curve'
    if d['element']=='Main commutative square and terminal period':d['element']='Main commutative square'
extra=[
('typewriter','Main square terminal period','text',[1183,517,1207,539],'. beside Un_c'),
('faint trace, medium undetermined','Pale trace below main arrowhead','drawing',[674,476,699,498],'U-shaped contour'),
('unnamed hand','Small square detached point','drawing',[1567,462,1582,477],'small point before e, function uncertain'),
('typewriter overlap','Later Dyn final-cell overlap','drawing',[1331,637,1369,674],'n/o-like contours'),
('unnamed hand','Replacement condition live colon','text',[660,671,676,696],': after raised parenthesis'),
('typewriter cancelling impression','Separate x after cancelled group','deletion',[1231,708,1263,732],'x beyond i; no hidden letter supplied'),
('typewriter cancelling impression','Separate x after point rationnel','deletion',[608,766,638,797],'x beyond final l; no hidden letter supplied'),
('typewriter/overlapping trace','Final e-like cell of invariante','drawing',[735,1354,762,1387],'e body, closed lower contour, upper-right trace')]
for hand,element,kind,pos,first in extra:inv.append(dict(sheet_kind='typescript',hand=hand,element=element,kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
def coord(d):
    p=d['position'];p=p[0] if isinstance(p[0],list) else p
    return p[1],p[0]
inv.sort(key=coord)
for d in inv:d['position']='whole-image box '+str(d['position'])
spec['inventory']=inv
ab=copy.deepcopy(R['R3']['abbreviations'])
for a in ab:
    if 'overline' in a['form']:a['form']=r'\overline{m}';a['expansion']='même (editorial expansion; the transcription retains the barred m)'
spec['abbreviations']=ab

notes=(O/'decisions'/f'{stem}_pending_notes.md').read_text().split('\nFinal notes must add')[0]
notes=notes.replace('Their seven events were logged when performed and are not to be duplicated at finalization.','Their seven events were logged when performed.')
spec['notes']=notes+r'''

**Ink decisions.** The second opening map has a rightward tip; the first retains a barred-shaft/mapsto doubt. The three filtration symbols are resolved as underlined slashed ovals, consistently with 123/018, without assigning an empty-set meaning. Typed o indices are resolved by their x-height; handwritten Z rings retain a separate o/0 doubt. The small square's upper Z overprint and lower looped z-like alphabet remain uncertain, and the small point before e is preserved without a mathematical interpretation. A pale U-shaped trace below the main arrowhead is drawn but not assigned an extra arrow.

The condition reads “est”, retains two visible comma strokes after i.e., and has its own raised colon; the cancelled lower semicolon remains tentative. The cancelled group after choisi is read les/des i, followed by a separate cancelling x. Another x extends beyond point rationnel. The last period of cancelled i.e remains live. The interlinear equivalence ends with a barred m; both witnesses expand it to même, which is confined here to the abbreviations list. The complete curved leaders under this phrase, Dynkin-, de c and classes de are drawn. Handwritten de is slightly higher than typed classes.

The root crop of the cancellation before s'adaptent did not confirm the readers' confident aux: an e-like counter, middle stroke and lower return survive in the last cell. The final preserves aue/aux with low confidence, rather than deciding from expected wording. The 2 in g(2) retains a local lower-foot/underline doubt. The closing Kostant mark is reproduced with its transverse overstroke. Mixed contours in the opening word, the later Dyn, the arithmetic des/les cell and the m/p cell of marche are preserved without an invented correction order. The final e-like cell of invariante is drawn with its extra trace; an accent or older letter is not supplied as certain. The literal “de cette classe rationnel” is unchanged.

The slanted four-line margin is restored as “Il ... pas le cas, p.ex. ... cela l'est ...”; its first A retains a local doubled-contour doubt. The colon after si is resolved from two compact dots. The dark connector and faint upper trace within paraboliques are both drawn with their function uncertain. The cancelled fib remains legible and transcribed. Mathematical expectations did not settle any of these readings.

No title, composition date, signature or total page count appears. The three readers identify the lower-left 18 as archive numbering, retained in a comment. The opening continues scan 018; the final source word ends “der-” and is left as der% under the supplied line-wrap joining convention so that the next consecutive scan can complete it. R2's isolated-page retention of the hyphen is documented as a convention discrepancy, not counted as a substantive witness error. No external material was researched.
'''
spec['check_events']=[
dict(statement_id='123-019-square-endpoint-consistency',who='GPT-6 Astra Pro; inherited effort (not exposed); independent R1, R2, R3 runs',
     type='used and rechecked in this run',
     outcome='All three readers separately compared arrow directions and route endpoints: the main paths run Dyn_c to the slashed-oval object and the small paths run the upper-right Z-like object to P. This is a diagram-incidence comparison only; no commutativity, morphism identification or stabilizer theorem was proved.')]
spec['consequential']=[
'The second opening map is resolved as mapsto; all three filtration glyphs are underlined slashed ovals. Typed o and handwritten o/0 are distinguished locally.',
'The condition says que G est; the cancelled phrase is les/des i rather than ceci. The equivalence insertion ends with a barred m, not a fully written même.',
'The A₃ marginal clause remains literal with its antecedent unresolved. The explicit weight examples refute only an injectivity interpretation of that clause, not every possible reference of the note.']
spec['workflow_note']='Three fresh readers used v07 and each viewed the whole and both halves once. Their crop counts were 23, 22 and 29. Root compared all three complete texts and reports, viewed all 23 existing R1 crops, ten R2 crops and six R3 crops, and made one new crop for the uncropped cancellation before s’adaptent. That crop contradicted the confident aux shared by all readers, so a local low-confidence aue/aux reading remains. A failed initial display of R1 crop22 was displayed successfully from the same file after the context boundary; it was not recropped. One overly long text report output was truncated and the omitted sections were reread in compact textual form; no missing output was claimed read. An auxiliary text-only audit exposed missing period accounting in R2 and inventory gaps when combining graphic details. Root restored both faint paraboliques traces and the extra cancellation cells, and treated the p/m as an overlap rather than an inferred deleted/live sequence. v08 will emphasize whole-shorthand stroke reading, retention of faint secondary traces in both text and inventory, and separation of source line-wrap hyphens from substantive collation.'
(O/'decisions'/f'{stem}_spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2))
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
print('Specification and preview saved; not yet finalized.')
