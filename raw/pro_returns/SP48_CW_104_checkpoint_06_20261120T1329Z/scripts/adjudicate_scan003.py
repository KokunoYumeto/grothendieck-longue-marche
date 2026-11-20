from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'records/scan003/reader_{a}/report.json').read_text()) for a in 'ABC'}
I={a:{x['id']:x for x in R[a]['issues']} for a in 'ABC'}
mapping={
'A01':('G01','01_tick'),'A02':('T01','02_first_F'),'A03':('T02','03_upper_F1'),'A04':('T03|T04','04_upper_F2'),'A05':('', '05_labels'),'A06':('T05','06_sigma_F0'),'A07':('T06','07_sigma_tip'),'A08':('T07','08_lower_f'),'A09':('T08','09_mu4'),'A10':('','10_other_mu'),'A11':('T09','11_ell'),'A12':('T10','12_address'),'A13':('T11','13_label_stop'),'A14':('T12','16_map_placement'),'A15':('T13','14_map_circle'),'A16':('T14','15_map_letter'),'A17':('T19','33b_product_position'),'A18':('T15','28_product_dashes'),'A19':('T16','29_product_cross'),'A20':('T17','30_nested_n'),'A21':('T20','36_double_triangles|33c_product_position'),'A22':('T21','37_bottom_F0'),'A23':('T22','38_bottom_index'),'A24':('',''),'A25':('T23','39_deleted_first'),'A26':('T24','40_deleted_second'),'A27':('T25','41_live_Fl'),'A28':('',''),'A29':('T26','43_bottom_relation'),'A30':('T27','43_bottom_relation'),'A31':('T28','44_last_Fls'),'A32':('T29','44_last_Fls'),'A33':('T30','45_final_argument'),'A34':('T31','45_final_argument'),'A35':('G21','46_bottom_rule'),
'G01':('G02','17_small_oval'),'G02':('G03','19_hatching'),'G03':('G04','18_big_oval'),'G04':('',''),'G05':('G05','19_hatching'),'G06':('G06','20_four_points'),'G07':('G07','21_single_lens'),'G08':('G08','22_sphere_arcs'),'G09':('G09','23_curved_arrow'),'G10':('G10','24_two_strips'),'G11':('G11','24_two_strips'),'G12':('G12','25_three_strips'),'G13':('G13','25_three_strips'),'G14':('G14','27_axis'),'G15':('G15','26_square'),'G16':('G16','31_joined_lenses'),'G17':('G17','32_chain_endpoints'),'G18':('G18|G19','34_grid'),'G19':('G20','35_four_lobes')}
def reading(a,ids,default):
 return '; '.join(I[a][i]['reading'] for i in ids.split('|')) if ids else 'Retained witness C in reading.tex: '+default
issues=[]
for aid,(b,c) in mapping.items():
 x=copy.deepcopy(I['A'][aid]);x['final']=x.pop('reading')
 x['readers']={'A':x['final'],'B':reading('B',b,x['C']),'C':reading('C',c,x['C'])}
 x['marked_in_H']='yes' if aid in ['A25','A26'] else 'no'
 if aid in ['A01','A11','A17','A21','A35'] or aid.startswith('G') and aid not in ['G16','G18','G19']:
  x['crop']=f'crops/scan003_{aid}.png'
 else:
  num=1 if aid in ['A02','A03','A04','A05'] else 2 if aid in ['A06','A07','A08'] else 3 if aid in ['A09','A10'] else 4 if aid in ['A14','A15','A16'] else 5 if aid in ['A12','A13'] else 6 if aid in ['A18','A19','A20'] else 7 if aid in ['A22','A23','A24'] else 8 if aid in ['A25','A26','A27','A28'] else 9 if aid in ['A29','A30','A31','A32','A33','A34'] else 10 if aid=='G18' else 11 if aid=='G19' else 12
  crop=next((O/'records/scan003/reader_C/crops').glob(f'{num:02d}_*.png'))
  x['crop']=str(crop.relative_to(O))
 issues.append(x)
D={x['id']:x for x in issues}
def upd(k,**kw):D[k].update(kw)
upd('A09',confidence='high',consequential='The first mu superscript is a visible 4; H gives 1 and C leaves 4/1 unresolved.')
upd('A11',diff_H=True,kind='insertion or placement',final=r'a,\ell,r on three separate levels',evidence=D['A11']['evidence']+' H prints the three symbols in one horizontal math row, though its editorial note correctly describes their vertical placement; the source arrangement is retained. The l/ell typesetting choice alone is not a C change.')
upd('A14',final=r'I_A\circ\unsure{S|s}\longrightarrow S')
upd('A16',final=r'\unsure{S|s}',diff_C=True,confidence='medium',evidence='The tall narrow glyph has an upper loop and an open lower sweep. The main crop supports reader B\'s S/s alternatives, excluding a delta with a closed lower loop; the case remains unresolved.')
upd('A17',diff_H=True,kind='insertion or placement',H=D['A17']['H']+'; joined to the other two products in one displayed line',evidence=D['A17']['evidence']+' Main crop confirms the text; all readers place this as a separate lower-left block. H groups it inline with the long product and doubled-triangle product.')
upd('A21',evidence=D['A21']['evidence']+' This product is a separate lower-right display in the source, not the third member of one inline list as in H.')
upd('A23',final=r'\unsure{kn\prime|n\,n\prime|n\prime}',diff_C=True,evidence=D['A23']['evidence']+' The main crop retains those two candidates and adds reader C\'s alternative of a single heavily retraced n-prime; the strokes do not securely decide the decomposition.')
upd('A32',consequential='Both Fl capitals on the clipped last line are doubled-stem F; both witnesses give the second one as plain F.')
upd('A33',consequential='The final argument has two prime strokes, n-double-prime; H gives one.')
upd('G01',diff_C=True,final='Left hollow point, right filled point, inner upper arc, downward arrow and two short inward top strokes.',evidence=D['G01']['evidence']+' The main crop additionally shows two short inward strokes from the top contour at about (1122,48) and (1131,46). They are missing from all three returned traces and are added without interpreting them as labels.')
upd('G02',diff_C=True,final='Four upper and three lower hatch strokes; first upper stroke continues below the chord into a short bent return.',evidence=D['G02']['evidence']+' Main crop additionally shows the first upper hatch crossing the diameter and bending below it, to about (1097,177); all three retained C without this continuation.')
upd('G03',final='Left endpoint open; right endpoint mostly black with a tiny enclosed white counter low in the knot.',diff_C=True,evidence='All three readers proposed a filled right endpoint. The main crop shows a small enclosed white core low in that black knot, near (1490.8,75.5). C\'s uniform hollow ring is also too simple. The final trace uses a black elliptic knot and a small off-centre white counter, without asserting an ideal filled/open-node semantics.')
upd('G05',final='Three left and seven right hatches, upper-right retrace, far-right black knot containing a small white counter.',evidence=D['G05']['evidence']+' Main crop confirms a tiny white counter in the far-right black knot, as A/B noticed, but does not support a large regular hollow ring. It is drawn as a black knot with a small offset white core, not C-reader\'s fully black point.')
upd('G08',diff_C=True,final='High upper inner arc, chord, distinct lower arcs, short curled return above left junction and short descending outside stem.',evidence=D['G08']['evidence']+' Main crop also shows two short junction strokes missing from all three returned traces: a curled return above the left junction and a short stem descending outside it. Both are added.')
upd('G14',C='Main repeated strokes, no detached dot',final='Retraced graduated axis with one detached dot above the left portion and a short attached peg on the leaning stem.',evidence='Main crop shows one isolated black dot near (1738,730), agreeing with reader C. The nearer dark feature is attached to the leaning stem as a short peg, not A\'s second separate dot. B omits the detached dot. The original uneven axis and separate retraced shaft are retained; H regularizes these.')
upd('G16',final='Joined lenses with extra lower arc, axis arrow, small closed return/top stubs; gaps at first upper-right end and left chord start.',evidence=D['G16']['evidence']+' Main chooses C-reader\'s closed return and top stubs over A\'s simplified return. The crop also shows a gap from the first upper arc end near (443,1059) to the lower path at (448,1068), and a gap before the first chord at (271,1055). All three joined these locations; the final trace separates them.')
upd('G17',H='Final right point and lower point; no explicit initial knot',evidence=D['G17']['evidence']+' Main confirms visible white between the downward head and the lower point; A\'s shortened arrow is retained to preserve this gap. H\'s actual drawing does carry the final right point and lower point; the difference is its missing initial knot, not omission of the lower point.')
upd('G19',final='Four lobed cells; retain twelve differing interior strokes; add first-axis gap, separate left dot, small open ring beside central knot and short contour returns.',evidence=D['G19']['evidence']+' Main chooses C-reader\'s small open ring near the central dark joint and its contour paths. A\'s added side-hook on the fourth upper interior stroke is not visible and is rejected. The first upper-contour barb is placed near (1122,1380).')
# New stroke refinements directly visible in the already inspected G10/G12 crops.
upd('G10',diff_C=True,final='Irregular two-cell strip with upper-left gap, left stem peg, middle peg, small return below right junction and separate right-side loop.',evidence=D['G10']['evidence']+' Main crop also shows a short attached peg on the upper left stem, a small return just below the right divider junction, and an elongated right-side retrace below it. These additional visible paths were omitted in the three C-based traces and are added.')
upd('G12',diff_C=True,final='Three unequal stacked cells with separate border retraces and crossbar pegs/returns.',evidence=D['G12']['evidence']+' The main crop also confirms a small downward oblique spur below the second crossbar and short upward pegs at its right end and on the bottom edge. These visible short strokes are added to C\'s principal retraces.')
# Prime-like detached stroke noticed only by reader C.
x=copy.deepcopy(I['C']['42_prime_after_l']);x['id']='A27a';x['final']=x.pop('reading');x['crop']='records/scan003/reader_C/crops/08_second_equality.png';x['readers']={'A':'Omitted in reading.tex.','B':'Omitted in reading.tex.','C':x['final']};x['evidence']+=' Main crop confirms the isolated stroke but leaves its linguistic status uncertain.';issues.insert(27,x)
x=copy.deepcopy(I['B']['T18']);x['id']='A18p';x['final']=x.pop('reading');x['crop']='records/scan003/reader_C/crops/06_long_product.png';x['readers']={'A':'Separate block in reading.tex.','B':x['final'],'C':I['C']['33a_product_position']['reading']};issues.insert(18,x)
# Consolidated text: A's grid and arrow separation, C's two selected drawing blocks, main crop refinements.
s=(O/'records/scan003/reader_A/reading.tex').read_text()
c=(O/'records/scan003/reader_C/reading.tex').read_text()
def replace(old,new):
 global s
 if old not in s:raise ValueError('Patch anchor not present: '+old[:100])
 s=s.replace(old,new,1)
def replace_figure(anchor):
 global s
 start=s.rfind(r'\figure{\begin{tikzpicture}',0,s.index(anchor));end=s.index(r'\end{tikzpicture}}',s.index(anchor))+len(r'\end{tikzpicture}}')
 cs=c.rfind(r'\figure{\begin{tikzpicture}',0,c.index(anchor));ce=c.index(r'\end{tikzpicture}}',c.index(anchor))+len(r'\end{tikzpicture}}')
 s=s[:start]+c[cs:ce]+s[end:]
replace_figure(r'\draw (265,1054)');replace_figure(r'\draw (1010,1405)')
replace('&l\\',r'&\ell\\')
replace(r'\unsure{S|s|\delta}',r'\unsure{S|s}')
replace(r"\unsure{kn'|n\,n'}",r"\unsure{kn'|n\,n'|n'}")
replace(r'\mathrm{l}(\Delta_n)',r'\mathrm{l}^{\unsure{\prime}}(\Delta_n)')
replace('% The lower line has no visible subscript','% The detached stroke after live l is prime-like; an isolated pen mark remains possible.\n% The lower line has no visible subscript')
replace('..controls(411,1011)and(436,1041)..(448,1068)\n ..controls(417,1100)','..controls(411,1011)and(434,1036)..(443,1059);\n\\draw (448,1068)..controls(417,1100)')
replace(r'\draw (266,1055)',r'\draw (271,1055)')
replace('(1122,1383)--(1118,1387)','(1122,1380)--(1119,1384)')
replace(r'\draw (1095,68)',r'\draw (1122,48)--(1117,59) (1131,46)--(1131,50);'+'\n'+r'\draw (1095,68)')
replace('(1111,136)--(1096,168)','(1111,136)--(1096,168)..controls(1093,172)and(1094,175)..(1097,177)')
replace(r'\fill (1490,72) circle[radius=4];',r'\fill (1490,72) ellipse[x radius=4,y radius=6];\fill[white] (1490.8,75.5) circle[radius=.9];')
replace(r'\draw (1534,164) circle[radius=4.8];',r'\fill (1534,164) circle[radius=4.8];\fill[white] (1531.5,166.5) circle[radius=1.2];')
replace(r'\draw[->] (1518,281)',r'\draw (1245,294)..controls(1245,289)and(1248,284)..(1251,285)'+'\n'+r' (1237,296)..controls(1239,302)and(1235,307)..(1236,314);'+'\n'+r'\draw[->] (1518,281)')
replace(r'\draw (1871,245)',r'\draw (1683.8,244.5)--(1687.5,244.5)'+'\n'+r' (1756,306)..controls(1753,311)and(1764,313)..(1765,306)'+'\n'+r' (1758,319)..controls(1768,328)and(1765,343)..(1761,342)..controls(1757,337)and(1757,328)..(1758,319);'+'\n'+r'\draw (1871,245)')
replace(r'\draw (1512,480)',r'\draw (1273,629)--(1283,638) (1339,632)--(1341,624)'+'\n'+r' (1317,729)--(1317,723);'+'\n'+r'\draw (1512,480)')
replace(r'\fill (1730,729) circle[radius=1.3];','')
replace(r'\draw (1711,748)',r'\draw (1725.7,731)--(1730,731);'+'\n'+r'\draw (1711,748)')
(O/'pages/H104-01_104_scan003.tex').write_text(s)
inv=copy.deepcopy(R['C']['inventory'])
for x in inv:
 x['sheet_kind']='reused_typed'
 if 'typist' in x['hand']:x['hand']='typewriter'
 if x['element']=='Upper larger oval and its arrow':x['first_words_or_objects']='hollow left end; black right knot with tiny white core; down arrow'
 if x['element']=='Sideways typed address label':x['first_words_or_objects']='MR LE PROFESSEUR GROTHENDIECK ALEX.; MATHEMATIQUES with doubtful stop; 5'
 if x['element']=='First cancellation':x['first_words_or_objects']='doubtful Ob Delta_n / O Delta_n, struck through'
 if x['element']=='Four-by-three grid':x['first_words_or_objects']+='; middle-row third pair headless; lower right shafts detached'
remaining=[]
for x in issues:
 if x.get('unresolved'):
  if x['id']=='A16':x['confidence']='medium'
  remaining.append({'location':x['location'],'reading':x['final'],'alternatives':'See the in-place alternatives; for a one-reading doubt, the mark’s exact status is unresolved.','confidence':x['confidence'],'reason':x['evidence']})
notes=[
 'A landscape reused typed sheet containing a sideways address label and handwritten diagrams, cell drawings and formulas. The only securely readable type is MR LE PROFESSEUR GROTHENDIECK ALEX., MATHEMATIQUES with a doubtful terminal stop, and a separate 5. Pale grey background remnants do not establish additional continuous readable type; nothing is reconstructed from H’s show-through note.',
 'At upper left the page records paired leftward s/t arrows among F objects, a separate sigma row with a lower-case f1, and three mu terms. The first mu superscript is visibly 4. The letters a, looped l and r occupy separate levels below. A short map has only A in the subscript of I; the circle and narrow S/s glyph are at baseline.',
 'Three Delta products are separate source blocks. The long product uses two continuation strokes, a doubtful small final cross/left-angle sign, and nested n_n. Each triangle in the lower-right product has a doubled left edge. Their graphical form is retained without assigning it an abstract alphabet from expected mathematics.',
 'The lower formulas involve Ob and Fl, with two cancelled or overwritten groups before the live Fl. The crowded first Delta index is unresolved. A detached prime-like mark after the live l is included with uncertainty. On the clipped final line the initial F has no recoverable index, only one relation bar is visible, both Fl capitals have doubled stems, and the final n has two prime strokes. A final closing parenthesis has no visible opener; none is supplied.',
 'The drawings include subdivided intervals, hatched lenses, two- and three-cell strips, a curved four-cell frame, a four-column three-row grid, and four lobed cells with twelve internal marks. Cell counts and endpoint/gap observations are graphical readings, not proof checks. Thin bottom rule, small detached dots, returns and white counters in dark knots are preserved without assigning mathematical functions.',
 'H’s actual separate TikZ drawing was compared, not only its editorial description. It regularizes contours, omits marks, and gives the lower grid three columns. Its note knows the a/l/r group is vertical, but the math itself places it horizontally; this is recorded with that qualification. Equivalent l/ell macro choices are not counted as lexical errors.',
 'No theorem or calculation was proved or used as background in adjudicating this sheet, and no check events are added. No explicit author-written “à vérifier”, “sauf erreur”, “je présume”, title or date is present. No manuscript folio is identified. The lower-left 2 is an archive numeral, represented only in a comment; the typed 5 belongs to the address label.'
]
decision={'scan':3,'folder':'H104-01','issues':issues,'remaining':remaining,'inventory':inv,'notes':notes,'checks':[],'crop_counts':{'A':11,'B':11,'C':12,'main':21},'main_adjudication_complete':True}
(O/'records/scan003/decision.json').write_text(json.dumps(decision,ensure_ascii=False,indent=2)+'\n')
print('scan003 written:',len(issues),'issues,',len(remaining),'remaining doubts,',len(inv),'inventory elements')
