from pathlib import Path
import json
out=Path('edition/reviews');out.mkdir(parents=True,exist_ok=True)
tex=r'''\scanpage{6}
P.ex. il suffit de se limiter aux extensions de type fini du corps premier $\mathbb{Q}$ -- on trouve un foncteur conservatif de la cat. de ces corps dans celle des groupoïdes \inserted{(ou des topos)}, au sens : un morphisme de corps qui donne une équivalence de groupoïdes (ou de \unsure{topos|Topos}) est un \uline{iso}.

\margin{en car $p>0$ le foncteur est conservatif si de plus on passe à la catégorie quot$^t$ de celle des corps où une extension radicielle finie est considérée comme triviale... (le foncteur $K-B_K$ ou $K-\Pi_K$ se factorise par cette cat. quotient\unsure{..|...})}

Quand on prend des corps quelconques, le 2-foncteur $K-B_K$ ou $K\longrightarrow\Pi_K$ \inserted{ou $(K,\bar K)\unsure{-|\longrightarrow}E_{\bar K/K}$} est cependant loin d'être fidèle. Ainsi, si $K$ est sép clos, $B_K$ est le ``topos ponctuel'', $\Pi_K$ le groupoïde ponctuel, $E_{\bar K/K}\simeq(1)$ -- il est clair que les morphismes entre corps sép. clos ne sont pas décrits par les morphismes entre leurs topos étales, ou groupoïdes fondamentaux ! Pour cette raison, il y a lieu d'associer à un corps $K$ un objet plus fin que $B_K$ ou $\Pi_K$,
\mspage{5}
'''
(out/'149_scan006.tex').write_text(tex,encoding='utf-8')
boxes={'c01':[18,209,529,1290],'c02':[274,475,797,619],'c03':[758,1067,1590,1172],'c04':[283,1144,875,1236],'c05':[615,1285,924,1395],'c06':[262,1267,1567,1511],'c07':[270,845,531,957],'c08':[20,2290,107,2347],'c09':[580,269,681,356],'c10':[1033,431,1394,557],'c11':[1352,378,1615,475]}
def crop(n): return 'crops/149_scan006_'+n+'.png'
changes=[]
def ch(i,place,C,H,final,evidence,cr,confidence,ac,ah,kind,cat,mh=False,math=False):
 changes.append(dict(id=i,place=place,C=C,H=H,final=final,evidence=evidence,crop=crop(cr),box=boxes[cr],confidence=confidence,against_C=ac,against_H=ah,kind=kind,error_category=cat,marked_in_H=mh,mathematical=math))
ch('c01','Main line 3, corps premier',r'$Q$',r'$\mathbb{Q}$',r'$\mathbb{Q}$','The oval Q has its diagonal tail and a distinct additional upright just inside the left boundary. This is a deliberate doubled left stroke; it is not a second character.','c09','high',True,False,'misread symbol or index','Symbols and indices',math=True)
ch('c02','Main line 5, after ces corps','dans',', vers','dans','The initial has an ascender followed by the low a-shaped loop and a joined terminal ns. No v-shaped first letter or separate r shoulder is visible. The initial is partly crossed by the diagonal note, but the upright and following low letters support dans.','c02','high',False,True,'misread word','Words')
ch('c03','Main line 4 end, ces corps','corps','corps,','corps','The terminal s bends down and stops. The blank space to its right and beneath it contains no independent comma. Crop c02 then reads the next-line word dans.','c11','high',False,True,'text not on the page','Text that is not on the page')
ch('c04','Main line 8, parenthetic topos','Topos','topos',r'\unsure{topos|Topos}','The initial has a tall narrow ascender and a low crossing into the following o, like the lowercase t of the inserted topos. A capital cannot be ruled out solely from its size; retain the case doubt, with lowercase first.','c07','medium',True,False,'misread word','Words')
ch('c05','Diagonal note, first line',r'en car $\unsure{p>0|p\ne0}$ le foncteur',r'\ill{}',r'en car $p>0$ le foncteur','After rotation the words en car, le and foncteur are visible. The formula has a p descender, a right-facing wedge, and a rounded zero; there are no paired equality strokes or a diagonal cancellation through them.','c01','high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',True,True)
ch('c06','Diagonal note, lines 2–3','si de plus on passe à la',r'\ill{}','si de plus on passe à la','The end of the second line reads si de. The next line begins plus, then separate on and passe; the small à la at the line end is partly crossed by horizontal main text but its accent, short a and tall l remain visible.','c01','high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',True)
ch('c07','Diagonal note, line 4',r'\unsure{quot$^t$|quotient}','quotient',r'quot$^t$','The word is short, with q descender, compact u/o strokes, a t, and a raised crossed terminal t. There is no long sequence corresponding to ient. The raised abbreviation is retained.','c01','high',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised')
ch('c08','Diagonal note, line 9, both map strokes',r'$K\unsure{-|\longrightarrow}B_K$ ou $K\unsure{-|\longrightarrow}\Pi_K$',r'$K\mapsto B_K$ ou $K\mapsto\Pi_K$',r'$K-B_K$ ou $K-\Pi_K$','Both signs are single shafts ending in a small downward pen thickening. Neither has a left upright bar or a separately formed two-sided arrowhead. The letters B and capital Pi and their low K indices remain visible in the same complete formula row.','c01','high',False,True,'misread symbol or index','Symbols and indices',math=True)
ch('c09','Diagonal note, final line punctuation','quotient.)','quotient…) ',r'quotient\unsure{..|...})','The closing parenthesis is clear. Before it, two separated dark terminal marks can be seen, one dot-like and one short horizontal mark; the preceding terminal t and a possible third point are not cleanly separable. The count of points stays doubtful. No editorial words from H are source text.','c01','low',True,True,'other','Other')
ch('c10','Main line 10, first map',r'$K\unsure{-|\longrightarrow}B_K$',r'$K\mapsto B_K$',r'$K-B_K$','A straight horizontal shaft stops in a broad rounded tip with no returning arrowhead wing. Its left end has no vertical mapsto bar. B and subscript K are present.','c03','high',False,True,'misread symbol or index','Symbols and indices',math=True)
ch('c11','Main line 10, second map',r'$K\longrightarrow\Pi_K$',r'$K\mapsto\Pi_K$',r'$K\longrightarrow\Pi_K$','The right end has a separate curved chevron/return that forms an arrowhead. The left end of the shaft is bare, without a mapsto upright. Capital Pi has its broad roof and two downstrokes.','c03','high',False,True,'misread symbol or index','Symbols and indices',math=True)
ch('c12','Insertion above main line 11',r'\inserted{ou $(K,\bar K)\unsure{-|\longrightarrow}E_{\bar K/K}$}',r'\add{ou $(K,\overline K)\mapsto E_{\overline K/K}$}',r'\inserted{ou $(K,\bar K)\unsure{-|\longrightarrow}E_{\bar K/K}$}','The small insertion contains ou, the parenthesized pair with a bar only above the second K, and E with the fraction-like subscript bar K/K. The shaft has no left upright. Its thick right tip contains a small angle, but not enough to distinguish an arrowhead from the pen finish; C’s dash/arrow doubt is retained. The insertion sits between the full map row and est cependant, attaching after the second map.','c04','medium',False,True,'misread symbol or index','Symbols and indices',math=True)
ch('c13','Main line 12, first sép clos','sép clos','sép. clos','sép clos','The p has a large closed descender and heavy retracing. The space following its right loop is blank before clos: no separate stop is visible. The acute accent above é is clear. None of the retraced strokes strikes the abbreviation out.','c05','high',False,True,'text not on the page','Text that is not on the page')
ch('c14','Main lines 12–13, quotation marks',r'``topos ponctuel\'\'', '« topos ponctuel »',r'``topos ponctuel\'\'','The opening and closing each consist of two short raised strokes. They are quotation marks, not angle-shaped guillemets. The words topos and ponctuel are clear across the line break.','c06','high',False,True,'misread symbol or index','Symbols and indices')
ch('c15','Bottom-left manuscript folio',r'\margin{5}','(nothing)',r'\mspage{5}','A handwritten 5 has a short top, descending middle and rounded lower stroke. This is source foliation in the bottom-left corner. The change from C’s margin macro to mspage is rendering-only; the omission in H is substantive.','c08','high',False,True,'omission','Omissions')
# Normalize only literal quote strings in this report, not manuscript text.
changes[13]['C']="``topos ponctuel''";changes[13]['final']="``topos ponctuel''"
decisions=[]
def dec(i,d,r,e,cr,conf):decisions.append(dict(id=i,decision=d,reading=r,evidence=e,crop=crop(cr),box=boxes[cr],confidence=conf))
dec('M0960','first',r'p>0','The p descends; the relation is a wedge with its point rightward, followed by an oval zero. No equality bars or slash.','c01','high')
dec('M0961','first',r'quot$^t$','Compact q/u/o/t body followed by a raised crossed t; the full letter sequence quotient is not written.','c01','high')
dec('M0962','first','-','First marginal sign is one uninterrupted shaft with a small terminal pen thickening, without a discernible arrowhead.','c01','high')
dec('M0963','first','-','Second marginal sign has the same unheaded shaft; the low K and full capital Pi are present.','c01','high')
dec('M0964','first','-','Main first shaft has a blunt rounded endpoint and no returning wing. The adjacent second sign shows the distinct arrowhead that is absent here.','c03','high')
dec('M0965','undecided',r'\unsure{-|\longrightarrow}','The right tip of this much smaller inserted shaft has an angular nib/return. It cannot be securely separated into an arrowhead; no mapsto bar is present.','c04','medium')
inv=[]
def elem(e,k,pos,first):inv.append(dict(scan=6,sheet_kind='handwritten mathematical notes',hand='main manuscript hand',element=e,kind=k,position=pos,first_words_or_objects=first,transcribed='yes'))
elem('e01','text paragraph','main lines 1–8, upper body','P.ex. il suffit de se limiter')
elem('e02','insertion','above main line 5, after groupoïdes','(ou des topos)')
elem('e03','marginal note','upper-left diagonal, eleven short lines','en car p>0 le foncteur')
elem('e04','text paragraph','main lines 9–20, lower body','Quand on prend des corps quelconques')
elem('e05','insertion','above main line 11; after main-line maps',r'ou $(K,\bar K)\unsure{-|\longrightarrow}E_{\bar K/K}$')
elem('e06','source folio','bottom-left corner','5')
margin=r'en car $p>0$ le foncteur est conservatif si de plus on passe à la catégorie quot$^t$ de celle des corps où une extension radicielle finie est considérée comme triviale... (le foncteur $K-B_K$ ou $K-\Pi_K$ se factorise par cette cat. quotient\unsure{..|...})'
audit=[]
def ab(i,k,b,r):audit.append(dict(box=i,kind=k,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=r))
ab('b01','diagonal marginal note; read the diagonal writing, excluding crossing main-text lines',boxes['c01'],r'\margin{'+margin+'}')
ab('b02','main formula row with C doubt and handwritten numeral 2',[280,1067,1590,1172],r'le 2-foncteur $K-B_K$ ou $K\longrightarrow\Pi_K$')
ab('b03','inserted complete formula with unresolved C doubt',boxes['c04'],r'\inserted{ou $(K,\bar K)\unsure{-|\longrightarrow}E_{\bar K/K}$}')
ab('b04','whole formula containing handwritten numeral 1',[277,1517,626,1635],r'$E_{\bar K/K}\simeq(1)$')
ab('b05','handwritten source folio',boxes['c08'],r'\mspage{5}')
ab('b06','insertion and its curved attachment stroke',boxes['c10'],r'\inserted{(ou des topos)}')
ab('b07','C/H different word; horizontal main-text line only',boxes['c02'],'dans celle des')
ab('b08','medium-confidence departure from C; lowercase/capital initial of topos',boxes['c07'],r'\unsure{topos|Topos})')
ab('b09','C/H different abbreviation punctuation',boxes['c05'],'sép clos,')
ab('b10','C/H quotation signs across complete two-line phrase',boxes['c06'],r'''si $K$ est sép clos, $B_K$ est le ``topos ponctuel'', $\Pi_K$ le groupoïde ponctuel,''')
ab('b11','alphabet of the rational-field symbol',boxes['c09'],r'$\mathbb{Q}$')
ab('b12','C/H added comma after corps',boxes['c11'],'corps')
coverage=[
(1,'editorial-only','',r'The 6 is the \scanpage metadata, not manuscript text.'),
(2,'material','c02','The word is dans. H’s additional comma is separately recorded at c03.'),
(3,'material','c05','Opening of diagonal note recovered, including p>0.'),
(4,'material','c06','The words si de plus on passe à la are readable.'),
(5,'material','c07','The source uses the raised-t abbreviation.'),
(6,'reading-agrees','','Three written points after triviale are represented by C’s three stops and H’s typographic ellipsis.'),
(7,'material','c08','First marginal map stroke is unheaded and has no mapsto bar.'),
(8,'material','c08','Second marginal map stroke is likewise unheaded.'),
(9,'material','c09','Closing punctuation remains doubtful; H’s following explanatory note is editorial and excluded.'),
(10,'reading-agrees','','Both complete witness texts contain the closing parenthesis; the alignment split is not a source difference.'),
(11,'material','c10','Main first map is a literal dash.'),
(12,'material','c11','Main second map is an arrow, with no initial mapsto bar.'),
(13,'material','c12','Inserted map has no initial bar; dash/arrow doubt remains.'),
(14,'material','c13','No stop follows the first sép.'),
(15,'material','c14','Opening quotes are two raised strokes.'),
(16,'material','c14','Closing quotes are two raised strokes.'),
(17,'material','c15','Source folio 5 is visible at the foot.')]
obj=dict(scan=6,reader='/root/reader_b',lines_read=34,changes=changes,decisions=decisions,inventory=inv,
 notes=[
 'Scan 006, source folio 5. Twenty main manuscript lines, eleven diagonal marginal lines, two separate insertion lines, and the folio were inspected (34 line units). No date or title is present.',
 'The upper paragraph states conservativity for finite-type extensions of the prime field, described through groupoids or topoi. The diagonal note adds the positive-characteristic quotient by finite radicial extensions. These are transcribed claims, not checked theorems.',
 'The lower paragraph says the construction is far from faithful for arbitrary fields, using separably closed fields and their point-like associated objects, then asks for an object finer than B_K or Pi_K. No mathematical re-proof was undertaken.',
 'No deletion is present. The heavy retracing in the first sép is not a strike. The curved line under the inserted (ou des topos) runs to the position immediately following groupoïdes; it is an attachment leader, not underlining of that insertion.',
 'Reading decisions used local pen shapes only: doubled Q, the plain map shafts versus the one clear main-line arrowhead, and local lowercase t forms. No mathematical necessity was used to replace the written signs. The inserted small map endpoint and diagonal-note terminal points remain in doubt.'
 ],checks=[],
 hand=[
 dict(habit='Map shafts may be left without an arrowhead. A complete arrow has a curved return at the right; none of the map signs has an initial mapsto bar.',pages=[6],consistency='Observed in both marginal maps and both main maps; the smaller inserted endpoint remains doubtful, so the habit is not asserted to decide that occurrence.',misread='H renders all five signs as mapsto; C marks four of the five as dash/arrow choices.'),
 dict(habit='Capital Pi is a broad horizontal roof over two downstrokes, the left sometimes ending in a small hook.',pages=[6],consistency='Consistent at the four occurrences on this leaf (margin, main map, point-groupoid clause, final clause).',misread='No local Pi/pi swap found.'),
 dict(habit='Small K indices can be rounded and resemble an n; the low right arm is compressed.',pages=[6],consistency='Visible in B_K, Pi_K and the subscript of E; locally compared with clearer full K forms. This is a local identification, not a general rule for later pages.',misread='No witness divergence here; caution for subsequent leaves.'),
 dict(habit='Short two-stroke quotation marks appear above the text.',pages=[6],consistency='Both sides of topos ponctuel.',misread='H turns them into French angle guillemets.'),
 ],
 notation=[
 dict(written='Q with doubled left stroke',rendering=r'\mathbb{Q}',meaning='prime field named in the opening paragraph',evidence='Main line 3, crop c09.'),
 dict(written='capital Pi with low K',rendering=r'\Pi_K',meaning='groupoid associated to K, as the text says',evidence='Explicit le groupoïde ponctuel on main line 13; four locally visible occurrences.'),
 dict(written='E with subscript bar K/K',rendering=r'E_{\bar K/K}',meaning='object included alongside B_K and Pi_K',evidence='Inserted map and main-line formula E_{bar K/K} ≃ (1). Bar only on the first subscript K.'),
 dict(written='short horizontal shaft',rendering='-',meaning='literal written mapping shaft without an arrowhead',evidence='Two marginal maps and main first map.'),
 ],
 abbreviations=[dict(form='P.ex.',expansion='Par exemple',place='main line 1'),dict(form='cat.',expansion='catégorie',place='main line 4 and diagonal note line 10'),dict(form='car',expansion='caractéristique',place='diagonal note line 1'),dict(form=r'quot$^t$',expansion='quotient',place='diagonal note line 4'),dict(form='iso',expansion='isomorphisme',place='main line 8, underlined'),dict(form='sép',expansion='séparablement',place='main line 12, without a stop'),dict(form='sép.',expansion='séparablement',place='main line 15, with a stop')],
 doubts=[dict(place='main line 8, topos',reading='topos',alternatives=['Topos'],confidence='medium',reason='Initial t resembles local lowercase forms but its large ascender prevents certainty about case.'),dict(place='diagonal note last line',reading='..',alternatives=['...'],confidence='low',reason='Two dark terminal marks precede the parenthesis; separation of the preceding t finish and a possible third point is uncertain.'),dict(place='insertion above main line 11',reading='-',alternatives=[r'\longrightarrow'],confidence='medium',reason='Tiny angular right end could be nib finish or arrowhead; source has no initial mapsto upright.')],audit_boxes=audit,
 diff_coverage=[dict(row=n,classification=c,change_id=i,reason=r) for n,c,i,r in coverage])
(out/'149_scan006.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote',out/'149_scan006.tex',out/'149_scan006.json')
print('Changes',len(changes),'marks',len(decisions),'inventory',len(inv),'audit boxes',len(audit),'diff rows',len(coverage))
