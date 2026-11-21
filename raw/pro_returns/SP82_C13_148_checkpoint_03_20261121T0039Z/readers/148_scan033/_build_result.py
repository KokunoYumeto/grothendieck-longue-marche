from pathlib import Path
import csv,json,re
p=Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan033')
out=Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan033')
C=(p/'C.tex').read_text(); H=(p/'H.tex').read_text(); final=(out/'candidate.tex').read_text()
marks=list(csv.DictReader((p/'marks.tsv').open(),delimiter='\t'))
diffs=list(csv.DictReader((p/'differences.tsv').open(),delimiter='\t'))
boxes=dict([
('table180',[74,76,590,214]),('table420',[68,209,683,444]),('table1020',[56,452,670,862]),('total',[73,878,481,1003]),('dictionary',[735,78,1051,198]),
('programme1',[771,242,1621,536]),('cancelled_start',[786,527,957,567]),('margin',[1618,307,2176,650]),('programme2',[789,542,1653,714]),('programme2_deleted',[838,700,1831,964]),('programme3',[798,958,1783,1253]),
('pants',[2285,91,2517,289]),('four_top',[2595,105,2827,295]),('four_middle',[2375,339,2565,484]),('cancelled_drawing',[2621,369,2847,520]),('five_holes',[2252,548,2555,831]),('sphere_left',[2111,949,2454,1294]),('sphere_right',[2548,959,2912,1322]),('large_surface',[1998,1457,2995,2228]),('bleedthrough',[1825,635,2243,1030]),('folio',[94,2099,228,2198]),('page',[0,0,3011,2228])])
def crop(k): return 'page' if k=='page' else 'crops/148_scan033_'+k+'.png'
changes=[]
def change(place,c,h,f,ink,k,conf,kind,ac,ah,math=False):
    assert ac or ah
    changes.append(dict(place=place,c=c,h=h,final=f,ink=ink,crop=crop(k),box=boxes[k],confidence=conf,kind=kind,against_c=ac,against_h=ah,math=math))
change('Count table, second row label',r'f_{\vec Q,a}',r'f_{\vec Q,\alpha}',r'f_{\vec Q,a}','The small final letter has a closed oval followed by a short descending exit, the same form as a; no crossed or open alpha tail is visible. The arrow over Q is explicit.','table180','high','misread symbol or index',False,True,True)
change('420 group, first equation, final factor',r'60=1\times60=\unsure{4|1}\times60',r'60=1\times60=1\times60',r'60=1\times60=4\times60','The disputed digit has a triangular closed counter on the left of a long upright, not a lone upright. All the adjacent 60s and multiplication marks are visible. This resolves M0348 to the first reading.','table420','high','misread symbol or index',True,True,True)
change('420 group, added row label and leader',r'\inserted{\tau_r^0}',r'\tau_r^0',r'\inserted{\begin{tikzpicture}[baseline=(z.base)]\node(z)at(.7,0){$\tau_r^0$};\draw(.7,0)ellipse(.36 and .22);\draw(-.4,.08)..controls(-.1,.03)and(.2,-.05)..(.34,0);\end{tikzpicture}}','The small added equation lies between the first two original rows; the label sits farther right in a closed oval with a leader running left. The leader is not assigned an arrowhead.','table420','high','insertion or placement',True,False,True)
change('420 group, fourth row label','','','','A single detached short slanted stroke stands above the gamma. It lacks the angled head and foot of the explicit superscript 1 in the lower group. This resolves M0349 to its alternative.','table420','high','misread symbol or index',True,False,True)
changes[-1]['h']=changes[-1]['final']=r"\gamma'_{\pi,s}"
# Supply exact witness C source rather than a Python apostrophe-joined spelling.
changes[-1]['c']=r"\unsure{\gamma^1_{\pi,s}|\gamma'_{\pi,s}}"
change('1020 group, replacement subtotal',r'\begin{array}{r}1020\\\deleted{\unsure{900}}\end{array}',r'1020',r'\begin{array}{r}\inserted{1020}\\\deleted{\unsure{900}}\end{array}','1020 is written above the compact crossed-out older number; the old lower row remains physically separate. The newer number is not merely a continuation of a numeral underneath.','table1020','high','insertion or placement',True,True,True)
change('1020 group, deleted former subtotal',r'\deleted{\unsure{900}}','',r'\deleted{\unsure{900}}','The lower numeral group is crossed diagonally. A leading loop and descending stroke permit 9, but the two following round shapes are partly covered; the inherited doubt is retained. Its presence and cancelled state are clear.','table1020','medium','deletion state',False,True,True)
change('1020 group, second equation middle product',r'120=\unsure{2\times60}=2\times60',r'120=2\times60=2\times60',r'120=2\times60=2\times60','The retraced 2 retains its curled head and lower horizontal foot; an oblique cross is followed by the closed lower bowl of 6 and a separate oval 0. The whole equation was read. M0350 is resolved.','table1020','high','misread symbol or index',True,False,True)
change('1020 group, third equation middle product',r'120=\unsure{1\times120}=2\times60',r'120=1\times120=2\times60',r'120=1\times120=2\times60','The current leading 1 has the high angled approach and long downstroke seen in the unretouched next row. The crossing mark and 120 follow it despite overlapping older strokes. M0351 is resolved, but the superposition reduces confidence.','table1020','medium','misread symbol or index',True,False,True)
change('1020 group, second row label',r'\unsure{\gamma}_{\pi,\rho}',r'\gamma_{\pi,\rho}',r'\gamma_{\pi,\rho}','The heavy glyph still shows two upper branches meeting above a closed lower loop; this matches the clear gamma in the local gommage key and the other row labels. The pi, comma and descending rho are separately visible. M0352 is resolved.','table1020','high','misread symbol or index',True,False,True)
change('1020 group, fifth row leading multiplier',r'3\times120',r'3\times120',r'\inserted{3\times}120','The 3 is tucked left of the row beside the brace and the cross sits lower in the narrow space before the original 120. They form a later prefix to that row, rather than sharing its original baseline.','table1020','high','insertion or placement',True,True,True)
change('1020 group, fifth row cancelled equality',r'\deleted{\unsure{2\times60=2\times60}}','',r'\deleted{\unsure{2\times60=2\times60}}','A lower equality is heavily blackened beneath the two clearly legible replacement products 3×40. Portions of 2, crosses and final rounded digits survive; the exact older equality remains doubtful and is not resolved.','table1020','medium','deletion state',False,True,True)
change('1020 group, right grouping brace','','','','The right brace begins beside the overwritten third label, below the first two labels, and ends beside the seventh. It does not enclose all seven rows.','table1020','high','drawing or diagram',True,True,True)
changes[-1]['c']=r"\left.\begin{array}{l}\tau_{\pi,\rho}\\\gamma_{\pi,\rho}\\\unsure{\tau'_r|\tau_r^1}\\\gamma_r^1\\\gamma_r^{1'}\\\gamma_r^2\\\gamma_r^{2'}\end{array}\right\}"
changes[-1]['final']=r"\begin{array}{l}\tau_{\pi,\rho}\\\gamma_{\pi,\rho}\\\left.\begin{array}{l}\unsure{\tau'_r|\tau_r^1}\\\gamma_r^1\\\gamma_r^{1'}\\\gamma_r^2\\\gamma_r^{2'}\end{array}\right\}\end{array}"
change('1020 group, last row label',r"\unsure{\gamma_r^{21}|\gamma_r^{2'}}",r"\gamma_r^{2\,\prime}",r"\gamma_r^{2'}",'The 2 is followed by a detached near-vertical short stroke without the angled head or foot of the superscript numeral 1 above. This is the alternative prime reading of M0354.','table1020','high','misread symbol or index',True,False,True)
change('Total, cancelled former value',r'\deleted{\unsure{1500|1580}}','',r'\deleted{\unsure{1580|1500}}','Two small counters survive in the third digit, making 8 preferable to 0. The cancellation covers parts of the earlier digits, so the former total is not resolved and both readings remain.','total','medium','misread symbol or index',True,True,True)
change('Total, double rule and replacement placement',r'\begin{array}{r}\deleted{\unsure{1500|1580}}\\\inserted{1620}\end{array}',r'\overline{\overline{1620}}',r'\begin{array}{r}\overline{\overline{\deleted{\unsure{1580|1500}}}}\\\inserted{1620}\end{array}','Two distinct horizontal rules stand above the crossed older total. The clearly written 1620 is on a lower line below that cancellation, not underneath the rules as an uncancelled overlined value.','total','high','insertion or placement',True,True,True)
change('Total formula, current multiplier',r'\unsure{11}',r'11',r'11','Two current long uprights, each with a high angled approach, are visible in the overwritten multiplier. A loop and broad older base cross the second upright; current 11 is preferable but only medium confidence. This resolves M0355.','total','medium','misread symbol or index',True,False,True)
change('Total formula, underlying multiplier','',r'',r'\deleted{\unsure{12}}\inserted{11}','The current second upright overlays an older curved head and broad lower stroke that admit 2. The earlier pair is retained as doubtful 12; the layered strokes are not all separable.','total','low','deletion state',True,True,True)
change('Programme 1, first word after déterminer','un','les',r'\unsure{les|un}','A tall initial looped staff is visible, unlike the short entrance of a plain u. The compressed following curves favor les, but the last letters are not secure enough to remove un as an alternative.','programme1','medium','misread word',True,False)
change('Programme 1, abbreviation after les/un','syst.','rel.','syst.','A descending y-shaped stroke lies between the initial small s and a final upright crossed t, followed by a dot. The word is abbreviated syst., not rel.','programme1','high','misread word',False,True)
change('Programme 1, adjective after syst.','fondamental','fondamentales','fondamental','The word ends in one tall looped l and its short exit. There is no separate following e and s before de; the source singular is retained despite the uncertain preceding article.','programme1','high','misread word',False,True)
change('Programme 1, first partageant clause','se','en','se','The short word starts with a small curved s stroke followed by a flat e exit. No distinct second n arch appears. The same two-letter shape occurs in the later clause.','programme1','high','misread word',False,True)
change('Programme 1, entre before 14',r'\deleted{entre}',r'\uncertain{entre}',r'\deleted{entre}','A heavy horizontal strike crosses the entire short word before 14. Its cancellation is visible independently of the later cancelled phrase.','programme1','high','deletion state',False,True)
change('Programme 1, word replaced by orbites',r'\deleted{\illegible{1}}','',r'\deleted{\unsure{paquets}}','The cancelled word has a long initial descender and a second descending loop farther right, compatible with p and q. The intervening letters are crossed; paquets remains an explicitly doubtful reading.','programme1','low',r'readable ink left as \ill{}',True,True)
change('Programme 1, last word of cancelled phrase','',r'',r'\deleted{de}','To the right of the covered word a distinct d staff rises above the strike and is followed by a short e exit. This visible final de belongs to the cancelled phrase.','programme1','high','omission',True,True)
change('Programme 1, replacement orbites',r'\inserted{orbites}','orbites',r'\inserted{orbites}','Orbites is written above the crossed lower phrase. Its letters sit on a higher baseline and the lower cancellation runs beneath it.','programme1','high','insertion or placement',False,True)
change('Programme 1, second partageant clause','se','en','se','The word after sommets has the same small initial s curve and flat e continuation as the first clause, without a separate n arch.','programme1','high','misread word',False,True)
change('Side note, composés','composés','composées','composés','After the accented é there is one final s-shaped continuation; no extra e loop intervenes. The accent is visible above the compact ending.','margin','high','misread word',False,True)
change('Side note, dimension abbreviation','dimension','dimension','dim.','Only d, a dotted i, and the low m are written before a distinct full stop and the next word. The intervening letters of dimension are not present.','margin','high','abbreviation expanded or spelling modernised',True,True)
change('Side note, adjective after dim.',r'\unsure{relative|modulaire}',r'\uncertain{modulaire}','modulaire','The word begins with low m arches, contains a d staff and a later tall l, then a dotted i and the short final re. These strokes support modulaire; M0358 is resolved to its alternative.','margin','high','misread word',True,False)
change('Programme 2, preposition before niveau','du','de','du','A d staff joins a u with a terminal rise; there is no separate e loop at the end. The source word is du.','programme2','high','misread word',False,True)
change('Cancelled paragraph, short fragment before first repeated type',r'\unsure{qui se déduit par}',r'\ill{} de type',r'\unsure{qui} de type','The visible span before the clear type is short. One loop with a descending q-like stroke and a small dot admit qui; the remaining crossed run shows a d staff and short e. It does not support the several extra words of C. The first word stays doubtful.','programme2_deleted','low','misread word',True,True)
change('Cancelled paragraph, reviennent/revient','revient','reviennent',r'\unsure{reviennent|revient}','Several low repeated humps are visible before the terminal stroke, favoring reviennent. The cancellation crosses their upper portions, so the singular alternative is retained.','programme2_deleted','medium','misread word',True,False)
change('Cancelled paragraph, à ceux',r'\unsure{à ceux}','à ceux','à ceux','Below the upper strike the short à and the separate ceux run remain legible: the c is open and the final x is crossed. The word group is resolved from the crop.','programme2_deleted','high','other',True,False)
change('Cancelled paragraph, preposition before type III1','du','de','de','The d loop and rising staff are followed by a short e stroke, before the separate t of type. There is no u-shaped second letter.','programme2_deleted','high','misread word',True,False)
change('Cancelled paragraph, punctuation after III1',r'\mathrm{III}_1.)',r'\mathrm{III}_1)',r'\mathrm{III}_1.)','A dark small point is visible immediately after the subscript 1, before the closing parenthesis. It is separate from the longer following dash.','programme2_deleted','high','omission',False,True,True)
change('Cancelled paragraph, dash after mais','','','-','There is a separate short horizontal stroke between mais and the capital A. It is not attached to either letter.','programme2_deleted','high','omission',True,True)
change('Cancelled paragraph, Attention','Attention','attention','Attention','The initial is a tall capital A with two rising sides and a crossbar, distinctly higher than the following letters.','programme2_deleted','high','abbreviation expanded or spelling modernised',False,True)
change('Cancelled paragraph, interlinear twist label',r'\inserted{\(\mathrm{tw}_{1/6}\)}','',r'\inserted{\(\mathrm{tw}_{1/6}\)}','The small tw is written above twist, with 1/6 descending to its right; it lies inside the cancelled block. H records it only in an editorial note.','programme2_deleted','high','insertion or placement',False,True,True)
change('Cancelled paragraph, word following twist',r'\unsure{relativement|relationnel}','relationnel',r'\unsure{relationnel|relativement}','The long initial l and the low middle arches make relationnel preferable. The compressed ending is not plain enough to exclude relativement under the cancellation, so neither reading is resolved.','programme2_deleted','medium','misread word',True,False)
change('Cancelled paragraph, qui donne in the last parenthesis',r'\unsure{qui donne un Autom. du même type}','qui donne',r'qui donne','The q loop and long descender, dotted i, d staff and two low n arches are visible above the lower boundary stroke. This clear initial part is separated from the still doubtful un Autom. that follows.','programme2_deleted','high','other',True,False)
change('Cancelled paragraph, final preposition','du','de','de','The short word before the two horizontal bars shows a d staff and e exit, rather than a joined u.','programme2_deleted','high','misread word',True,False)
change('Cancelled paragraph, shorthand before type','même',r'\ill{}',r'\(=\)','Two short horizontal bars are visible before type; no written m-ê-m-e letters are present. The equals sign is retained as the source shorthand.','programme2_deleted','high','abbreviation expanded or spelling modernised',True,True)
change('Programme 3, initial capital','Eliminer','Éliminer','Eliminer','The capital E has its vertical and three horizontal strokes, with no separate accent above it.','programme3','high','abbreviation expanded or spelling modernised',False,True)

prefix=final[final.index(r'\figure{\begin{tikzpicture}'):final.index('% S033 pants')]
parts={}
segments=re.split(r'% S033 ([a-z_]+)\n',final[final.index('% S033 pants'):])
for i in range(1,len(segments),2):
    code=segments[i+1]
    if r'\end{tikzpicture}}' in code: code=code.split(r'\end{tikzpicture}}',1)[0]
    parts[segments[i]]=code.rstrip()
def graphic(k): return prefix+parts[k]+'\n'+r'\end{tikzpicture}}'
cscopes=re.findall(r'\\begin\{scope\}.*?\\end\{scope\}',C,re.S)
draw_findings=[
('pants','Upper three-ended surface',0,'The front diagonal is strong black ink and ends inside the upper-right central area. A separate nearby path is black and dashed. Three oval openings, their slants, and the lighter interior construction strokes are visible.'),
('four_top','Upper four-opening surface',1,'Four openings are visible. The outer top contour has a gap at the start of the vertical dotted cut; the left contour has a separate gap below the horizontal cut. Black dashed traces accompany the green crossed paths.'),
('four_middle','Middle four-opening surface',2,'There is a fourth small opening at upper right, absent from the three ellipses drawn by C. A black dashed diagonal runs from the lower-left opening toward it. The lower-left aperture contains a short black bar, and three clear short ticks rise from the front of the top rim.'),
('cancelled_drawing','Crossed drawing at middle right',3,'Oblique pencil strokes repeatedly cross a partly visible black contour and green interior paths. The surviving right curve and broken lower contour are retained without turning the crossing strokes into labels or a regular complete surface.'),
('five_holes','Five-opening surface with green cuts',4,'Five openings bound the figure. The green routes cross at distinct heights, with continuous lower portions and dotted upper portions; faint pencil construction contours remain visible behind them. The lower green horizontal turn joins a downward stroke rather than C’s simplified zigzag.'),
('sphere_left','Left lower sphere',5,'The front horizontal paths stop at the two front openings. The rear path is interrupted by the rear opening. The lower neck has a dashed rear rim. Pencil bands, an upper oval trace, and a loop around the right front opening are visibly present beyond C’s three construction strokes.'),
('sphere_right','Right lower sphere',6,'The front paths stop at two front openings, and the rear paths meet the two rear openings without crossing their apertures. Two opposing heads occur along the lower outer rim. The dark diagonal band and paired pencil meridians have solid and broken portions.'),
('large_surface','Large lower surface and marked rim',7,'The rim contains six stars, six filled dots and twelve ticks, counted around the complete oval. C includes only six ticks. The front arc is darker than the rear pencil arc, there are parallel outline retraces, and a small portion of a lower-left opening is cut by the sheet edge.')
]
for k,place,i,ink in draw_findings:
    c=cscopes[i] if i<len(cscopes) else ''
    if k=='large_surface':
        c=C[C.index(r'\begin{scope}[shift={(-.5,-5.1)}'):C.index(r'\end{tikzpicture}',C.index(r'\begin{scope}[shift={(-.5,-5.1)}'))]
    change(place,c,'',graphic(k),ink,k,'high','drawing or diagram',True,False,True)
change('Isolated pencil arc left of lower drawing group','','',graphic('isolated_arc'),'A continuous U-shaped gray stroke crosses several rows of the pale listing. Its smooth curvature and much larger scale differ from the mirrored mechanical glyphs; it is retained without a semantic label.','bleedthrough','high','omission',True,True)
group_c=C[C.index(r'\draw[gray](-1.6,2.4)'):C.index(r'\begin{scope}[shift={(-.5,-5.1)}')]
change('Pencil grouping paths and horizontal divider',group_c,'',graphic('grouping'),'The page and both full-resolution halves show the large pencil paths grouping the upper sketches and the lower five-hole drawing with the two spheres. Their broad curves and the separate horizontal rule are reproduced in the observed layout, without treating them as extra holes.','page','high','drawing or diagram',True,False)
print_start=C.index(r'\unsure{\texttt')
print_end=C.index(r'\mspage',print_start)
change('Pale mechanical listing behind the manuscript',C[print_start:print_end].strip(),'','','The pale blue, uniformly spaced mechanical letters are laterally reversed, including backwards letter forms and reversed parentheses. They pass beneath the foreground drawing strokes and are bleed-through from the other side, not source text on this face.','bleedthrough','high','text not on the page',True,False)
change('H terminal section title','',r'\section{Systèmes spéciaux de cinq points sur une sphère complexe}','','The complete face contains the work programme and drawings; the final section title of the supplied H extract has no handwritten counterpart anywhere on this scan. No adjacent page was consulted.','page','high','text not on the page',False,True)

decisions=[]
def decide(mid,decision,reading,ink,k,conf):
    decisions.append(dict(id=mid,decision=decision,reading=reading,ink=ink,crop=crop(k),box=boxes[k],confidence=conf))
decide('M0348','first','4','The digit has a triangular left counter against its upright, unlike 1; the whole written equality is 60=1×60=4×60.','table420','high')
decide('M0349','alternative',r"\gamma'_{\pi,s}",'A single detached short sloping prime stands above gamma, with no numeral-1 foot.','table420','high')
decide('M0350','first',r'2\times60','A curled 2 with lower foot precedes a cross, a retraced 6 bowl, and an independent oval 0; adjacent equation terms were read.','table1020','high')
decide('M0351','first',r'1\times120','The current tall angled-entry 1, cross and 120 can be separated from retracing, but the layered ink lowers confidence. The whole equation was read.','table1020','medium')
decide('M0352','first',r'\gamma','Two upper branches meet above a closed lower loop, matching the local gommage key and clear gamma labels.','table1020','high')
decide('M0353','undecided',r"\unsure{\tau'_r|\tau_r^1}",'A long top bar and a curled lower stroke support tau, but the dense superposed mass at upper right prevents a secure prime-versus-1 reading.','table1020','low')
decide('M0354','alternative',r"\gamma_r^{2'}",'The short detached stroke following the 2 is a prime without the foot of numeral 1.','table1020','high')
decide('M0355','first','11','Two current uprights can be traced, but an older curved loop and base overlap the second digit; the whole total formula was inspected.','total','medium')
decide('M0356','undecided',r'\unsure{\mathfrak S_K|\mathfrak G_K}','The large curved glyph has an inward return and broad lower curve; the crop does not exclude a G-shaped reading. The small K is visible. Neither alphabetic reading is resolved.','programme1','medium')
decide('M0357','undecided',r'\unsure{aux|avec}','The parenthetical word is a short compressed run. Its three main shapes favor aux, but the middle joins are insufficient to exclude avec.','programme1','medium')
decide('M0358','alternative','modulaire','Low initial m arches, the d staff, a later tall l, dotted i, and short re ending are visible after dim.','margin','high')
for m in marks[11:]:
    decide(m['id'],'other','','This mark belongs to C’s reconstruction of the pale mechanical listing. The saved crop shows laterally reversed type and parentheses beneath foreground pencil; it is reverse-side bleed-through and absent from the diplomatic text, not illegible source ink.','bleedthrough','high')

unresolved=[]
def doubt(place,reading,issue,alts,conf,k):
    unresolved.append(dict(place=place,reading=reading,issue=issue,alternatives=alts,confidence=conf,crop=crop(k),box=boxes[k]))
doubt('1020 group, former subtotal',r'\deleted{\unsure{900}}','Diagonal cancellation covers parts of the old digits; the 9-like loop and following round forms are not all plain.',['900','other cancelled numeral'],'low','table1020')
doubt('1020 group, overwritten third label',r"\unsure{\tau'_r|\tau_r^1}",'The superposed upper-right strokes prevent a secure prime/exponent decision.',[r"\tau'_r",r'\tau_r^1'],'low','table1020')
doubt('1020 group, cancelled fifth-row equality',r'\deleted{\unsure{2\times60=2\times60}}','Heavy blackening obscures the older factors below the clear replacement. The inherited reading remains doubtful.',[r'2\times60=2\times60','another cancelled equality'],'low','table1020')
doubt('Total, cancelled former value',r'\deleted{\unsure{1580|1500}}','Surviving counters favor 8 in the third position, but not every older digit is clear under the strike.',['1580','1500'],'medium','total')
doubt('Total, former multiplier',r'\deleted{\unsure{12}}','Older curved head and base overlap the current two uprights; 12 is plausible but not securely separated.',['12','another overwritten two-digit value'],'low','total')
doubt('Programme 1, article before syst.',r'\unsure{les|un}','The tall initial favors l, but the compressed remainder does not completely exclude C’s un.',['les','un'],'medium','programme1')
doubt('Programme 1, cancelled word below orbites',r'\deleted{\unsure{paquets} de}','Two descenders support p/q, but the intervening letters are crossed. The final de is separately visible.',['paquets de','another cancelled word followed by de'],'low','programme1')
doubt('Programme 1, acting group',r'\unsure{\mathfrak S_K|\mathfrak G_K}','The large curved glyph permits S and G; no alphabetic decision is made.',[r'\mathfrak S_K',r'\mathfrak G_K'],'medium','programme1')
doubt('Programme 1, word before 542',r'\unsure{aux|avec}','The short run favors aux, but its joins do not rule out avec.',['aux','avec'],'medium','programme1')
doubt('Cancelled start between items 1 and 2',r'\deleted{2) \unsure{Réduire}}','The initial capital and some tall strokes survive, but the crossing stroke hides the remainder; C’s proposed word is retained as a doubt.',['Réduire','another cancelled word beginning R'],'low','cancelled_start')
doubt('Cancelled paragraph, initial short fragment',r'\unsure{qui} de type','A q-like descender and a dot survive. The word before de type remains crossed and uncertain.',['qui','another short word'],'low','programme2_deleted')
doubt('Cancelled paragraph, verb after second qui',r'\unsure{reviennent|revient}','Several low humps favor the plural, but their tops lie under the cancellation.',['reviennent','revient'],'medium','programme2_deleted')
doubt('Cancelled paragraph, word after twist',r'\unsure{relationnel|relativement}','The low middle arches favor relationnel; the ending is not plain enough to remove relativement.',['relationnel','relativement'],'medium','programme2_deleted')
doubt('Cancelled paragraph, beginning of last line',r'\unsure{un Autom.}','The lower frame stroke passes through this word group, hiding parts of the abbreviated ending.',['un Autom.','another cancelled abbreviation'],'low','programme2_deleted')
doubt('Programme 3, cancelled adjective',r'\deleted{\unsure{gauches}}','Initial descending loop and a later tall stroke are compatible with gauches, but the horizontal strike obscures most small letters.',['gauches','another cancelled adjective'],'low','programme3')

inventory=[]
def inv(e,kind,pos,words,hand='his hand'):
    inventory.append(dict(element=e,kind=kind,position=pos,first_words_or_objects=words,sheet_kind='reused_typed',hand=hand,transcribed='yes'))
inv('I033-01','display','upper left, first brace','180; two equations and f labels')
inv('I033-02','display','upper left, second brace','420; five equations and tau/gamma labels')
inv('I033-03','insertion','between first and second original rows of the 420 group',r'120=1\times120=1\times120; circled \tau_r^0 and leader')
inv('I033-04','display','left, third brace','1020; seven equations and tau/gamma labels')
inv('I033-05','deletion','left of third brace, lower old subtotal',r'\deleted{\unsure{900}}')
inv('I033-06','insertion','above old subtotal',r'\inserted{1020}')
inv('I033-07','insertion','left end of fifth row in 1020 group',r'\inserted{3\times}')
inv('I033-08','deletion','middle of fifth row in 1020 group',r'\deleted{\unsure{2\times60=2\times60}}')
inv('I033-09','insertion','above cancelled fifth-row equality',r'\inserted{3\times40=3\times40}')
inv('I033-10','drawing','right side of third group','brace enclosing the last five labels')
inv('I033-11','display','under the count table',r'1620=5\times60+11\times120, with former digits and double rule')
inv('I033-12','deletion','old total beneath two rules',r'\deleted{\unsure{1580|1500}}')
inv('I033-13','insertion','below old total',r'\inserted{1620}')
inv('I033-14','deletion','under current multiplier 11',r'\deleted{\unsure{12}}')
inv('I033-15','insertion','over former multiplier',r'\inserted{11}')
inv('I033-16','display','above programme heading',r'\tau = twist; \gamma = gommage')
inv('I033-17','text','centre upper','Programme de travail :')
inv('I033-18','text','item 1, five lines','1) déterminer les/un syst. fondamental')
inv('I033-19','deletion','item 1 before 14',r'\deleted{entre}')
inv('I033-20','deletion','item 1 under orbites',r'\deleted{\unsure{paquets} de}')
inv('I033-21','insertion','above cancelled phrase in item 1',r'\inserted{orbites}')
inv('I033-22','margin note','boxed/bracketed note to right of item 1','en particulier, écrire toutes les flèches')
inv('I033-23','deletion','between items 1 and 2',r'\deleted{2) \unsure{Réduire}}')
inv('I033-24','text','item 2, first three lines','2) Reprendre la question')
inv('I033-25','deletion','boxed four-line block following item 2','et II1; short fragment; repeated types; twist; un Autom. de = type')
inv('I033-26','insertion','interline above twist within cancelled block',r'\inserted{\mathrm{tw}_{1/6}}')
inv('I033-27','text','item 3, four lines','3) Eliminer de plus les pièces')
inv('I033-28','deletion','after pièces in item 3',r'\deleted{\unsure{gauches}}')
for j,(k,place,_,_) in enumerate(draw_findings,29):
    inv(f'I033-{j:02d}','deletion' if k=='cancelled_drawing' else 'drawing',place,k.replace('_',' '))
inv('I033-37','drawing','left of lower drawing group','isolated U-shaped pencil arc')
inv('I033-38','drawing','around upper and lower sketch groups','pencil grouping curves')
inv('I033-39','drawing','between the small figures and large lower surface','horizontal divider')
inv('I033-40','margin note','bottom left','32','another unnamed hand')

notes=[
dict(id='N033-01',text='The manuscript is on a reused listing sheet. The pale blue mechanical printing is laterally mirrored bleed-through; C’s 89 associated doubt/illegibility marks are removed from the diplomatic text, not classified as unreadable source writing. The foreground pencil arc crossing that printing is retained.'),
dict(id='N033-02',text='The lower-left foliation 32 is in a lighter, unassigned pencil hand and is set with the margin convention. No manuscript date is visible on this face.'),
dict(id='N033-03',text='The added 120 row in the 420 group is linked to a circled tau_r^0 label. The old third-group subtotal, cancelled fifth-row equality, replacement multiplier, and lower total are kept in their visible insertion/deletion states.'),
dict(id='N033-04',text='The 3 in the first equation, portions of 420, the third lower-group label, 1620 in item 1 and 14 show retracing or superposition. Where a distinct underlying reading cannot be separated, no earlier numeral or symbol is invented.'),
dict(id='N033-05',text='The cancelled total favors 1580 over1500 but remains doubtful. The underlying multiplier admits12 but is also left doubtful.'),
dict(id='N033-06',text='The frame and cancellation strokes cover the entire four-line paragraph beginning et II1. The interlinear tw_{1/6} belongs inside that cancelled passage.'),
dict(id='N033-07',text='The side note has dim., not the expanded dimension of both witnesses. The last cancelled line uses = as shorthand for même; the source sign is retained.'),
dict(id='N033-08',text='H’s final section title Systèmes spéciaux de cinq points sur une sphère complexe has no counterpart on scan033 and is excluded as a wrong-page inclusion. No other page was inspected to make this exclusion.'),
dict(id='N033-09',text='All eight main drawings, the isolated pencil arc, grouping curves and divider are reproduced in TikZ. The rim has6stars,6dots,12ticks. Pencil retraces are reproduced as strokes rather than interpreted as additional topological objects.'),
dict(id='S033-C01',text='The first equality in the420 group is written60=1×60=4×60. Its final product is240; the written4 is preserved.'),
dict(id='S033-C02',text='The displayed subtotals180,420,1020 add to1620.'),
dict(id='S033-C03',text='The final decomposition5×60+11×120 equals1620.'),
dict(id='S033-C04',text='The fifth row of the1020 group is written3×120=3×40=3×40. As an ordinary numerical equality it has left value360 and right values120; it is preserved without correction.')
]
checks=[
dict(statement_id='S033-C01',date='2026-11-20',who='reader A, GPT-6 Astra Pro, run SP82_C13_148; effort not exposed',type='computation or formal certificate',outcome='4×60=240, whereas60=1×60. The written equality is false and its4 is retained.'),
dict(statement_id='S033-C02',date='2026-11-20',who='root, GPT-6 Astra Pro, run20261120 (SP82_C13_148); effort not exposed',type='computation or formal certificate',outcome='180+420+1020=1620.'),
dict(statement_id='S033-C03',date='2026-11-20',who='root, GPT-6 Astra Pro, run20261120 (SP82_C13_148); effort not exposed',type='computation or formal certificate',outcome='5×60+11×120=1620.'),
dict(statement_id='S033-C04',date='2026-11-20',who='root, GPT-6 Astra Pro, run20261120 (SP82_C13_148); effort not exposed',type='computation or formal certificate',outcome='3×120=360 while3×40=120. The written chained equality is false as a numerical equality and remains unchanged.')
]
hand_log=[
dict(pages=[33],habit='Clear gamma forms have two upper branches above a closed descending loop; heavy retracing can obscure their junction.',holds_at_every_observed_occurrence='Yes for the unobscured gamma forms on this page; the heavily overwritten third lower label is not used as a counterexample or a settled gamma.',witness_effect='C M0352 is resolved from the same-page gommage key and clear labels.'),
dict(pages=[33],habit='Detached primes are short slanted or near-vertical strokes without the angled head and baseline foot of the explicit superscript1.',holds_at_every_observed_occurrence='Yes at the clear gamma prime labels; the obscured tau label remains undecided.',witness_effect='C M0349 and M0354 move to the prime alternatives; M0353 stays open.'),
dict(pages=[33],habit='In the two se partageant clauses the small s curve is followed by a flat e exit; en elsewhere has a different joined arch.',holds_at_every_observed_occurrence='Yes at both observed se partageant occurrences on this page.',witness_effect='Both H en readings are rejected in favor of the visible se.'),
dict(pages=[33],habit='Capital E in Eliminer is written without a separate accent.',holds_at_every_observed_occurrence='One occurrence observed; no general inference beyond this occurrence.',witness_effect='H Éliminer is normalized away from the source and is changed back to Eliminer.'),
dict(pages=[33],habit='The large curved group letter has an inward return that permits both S-like and G-like readings.',holds_at_every_observed_occurrence='Only one occurrence is present on this page and it remains uncertain.',witness_effect='The C doubt is retained and broadened to S_K/G_K, rather than resolved by agreement with H.')
]
notation=[
dict(form=r'\tau',meaning='The page explicitly writes tau = “twist”.',place='two-line key above the programme'),
dict(form=r'\gamma',meaning='The page explicitly writes gamma = “gommage”.',place='two-line key above the programme'),
dict(form=r'f_{B,s}, f_{\vec Q,a}',meaning='Row labels as written; no further meaning assigned on this page.',place='first two count rows'),
dict(form=r'\gamma_r^{1\prime},\gamma_r^{2\prime}',meaning='A detached prime follows the numbered superscript; it is not a further numeral1.',place='lower count group'),
dict(form=r'=',meaning='Written shorthand in de = type, with the sense même; retained as the sign.',place='last line of cancelled paragraph'),
dict(form=r'\unsure{\mathfrak S_K|\mathfrak G_K}',meaning='Unresolved acting-group glyph; no group identity is inferred.',place='item1')
]
abbreviations=[
dict(form='syst.',expansion='système(s)',place='item1',note='Expansion listed only; source article and grammatical number remain uncertain.'),
dict(form='dim.',expansion='dimension',place='side note',note='Both witnesses expanded the three-letter dotted abbreviation.'),
dict(form='Autom.',expansion='automorphisme',place='last cancelled line',note='The abbreviated source word remains doubtful under the cancellation; expansion is not inserted into the text.'),
dict(form='tw',expansion='twist',place='interlinear label tw_{1/6}',note='The small label sits over the full word twist.')
]


change('Programme 1, parenthetical word before 542',r'\unsure{aux|avec}','avec',r'\unsure{aux|avec}','The short run has three main compressed shapes, favoring aux. The joins remain insufficient to exclude avec, so the C doubt is retained rather than resolved; H supplies only avec.','programme1','medium','misread word',False,True)
change('Cancelled start, word following 2)',r'\deleted{\unsure{2) Réduire}}',r'2) \ill{}',r'\deleted{2) \unsure{Réduire}}','The large initial R and later tall strokes admit Réduire, but the horizontal cancellation covers the small letters. The proposed word stays doubtful while preserving more visible structure than H’s illegibility marker.','cancelled_start','low',r'readable ink left as \ill{}',False,True)
change('Programme 3, cancelled adjective',r'\deleted{\unsure{gauches}}',r'\struck{\ill{}}',r'\deleted{\unsure{gauches}}','The initial long descending loop and a later tall stroke are compatible with gauches; the intervening letters remain covered by the strike. The C doubt is retained, not resolved.','programme3','low',r'readable ink left as \ill{}',False,True)
change('Cancelled paragraph, un Autom. in the last line',r'\unsure{un Autom.}',r'\ill{} \ill{}',r'\unsure{un Autom.}','Low beginning arches and a capital A followed by a compressed run admit un Autom. The lower frame stroke hides parts of the abbreviation, so its letters are not claimed as fully clear.','programme2_deleted','low',r'readable ink left as \ill{}',False,True)
change('Lower-left foliation',r'\mspage{32}','',r'\margin{32}','Two large light pencil digits are visible: the first has two open rightward bowls and the second has a descending stroke turning into a long rising foot. They read32 in the unassigned foliation hand.','folio','high','omission',False,True)

second_boxes=[]
def second(name,kind,b,reading):
    second_boxes.append(dict(box='S33-'+name,kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading))
second('subtotal180','handwritten number',[77,86,173,197],r'\(180\)')
second('row180a','whole formula',[184,76,590,151],r'\(60=3\times20=2\times30\quad f_{B,s}\)')
second('row180b','C/H different word',[184,148,590,214],r'\(120=4\times30=2\times60\quad f_{\vec Q,a}\)')
second('subtotal420','handwritten number',[68,272,148,337],r'\(420\)')
second('row420a','whole doubtful formula',[186,209,598,258],r'\(60=1\times60=4\times60\quad\tau_{\pi,s}\)')
second('row420insert','insertion',[183,241,683,305],r'\inserted{\(120=1\times120=1\times120\quad\tau_r^0\)}')
second('row420b','whole formula',[187,271,600,326],r'\(60=1\times60=5\times12\quad\gamma_{\pi,s}\)')
second('row420c','whole doubtful formula',[191,320,603,390],r"\(60=1\times60=3\times20\quad\gamma'_{\pi,s}\)")
second('row420d','whole formula',[190,386,607,444],r'\(120=1\times120=6\times20\quad\gamma_r^0\)')
second('subtotal1020','insertion and deletion',[56,587,145,689],r'\(\begin{array}{r}\inserted{1020}\\\deleted{\unsure{900}}\end{array}\)')
rows1020=[
('a',[174,452,622,511],r'\(120=2\times60=1\times120\quad\tau_{\pi,\rho}\)'),
('b',[171,503,623,573],r'\(120=2\times60=2\times60\quad\gamma_{\pi,\rho}\)'),
('c',[169,562,640,650],r"\(120=1\times120=2\times60\quad\unsure{\tau'_r|\tau_r^1}\)"),
('d',[162,629,629,693],r'\(120=1\times120=2\times60\quad\gamma_r^1\)'),
('e',[144,681,633,760],r"\(\inserted{3\times}120=\deleted{\unsure{2\times60=2\times60}}\inserted{3\times40=3\times40}\quad\gamma_r^{1'}\)"),
('f',[160,750,630,818],r'\(120=2\times60=2\times60\quad\gamma_r^2\)'),
('g',[169,807,641,862],r"\(60=1\times60=2\times30\quad\gamma_r^{2'}\)")
]
for name,b,r in rows1020: second('row1020'+name,'whole doubtful formula' if name in 'bceg' else 'whole formula',b,r)
second('total','whole doubtful formula',boxes['total'],r'\(\begin{array}{r}\overline{\overline{\deleted{\unsure{1580|1500}}}}\\\inserted{1620}\end{array}=5\times60+\deleted{\unsure{12}}\inserted{11}\times120\)')
prog1=final[final.index('1) déterminer'):final.index(r'\margin{en particulier')].strip()
second('programme1','C/H different word',boxes['programme1'],prog1)
second('programme1-strikes','deletion and insertion',[822,435,1219,523],r'\deleted{entre} \(14\) \deleted{\unsure{paquets} de}\inserted{orbites}')
second('programme1-group','whole doubtful formula',[1305,437,1610,536],r'\(\unsure{\mathfrak S_K|\mathfrak G_K}\) (\unsure{aux|avec} \(542\) sommets)')
margin=final[final.index(r'\margin{en particulier'):final.index(r'\deleted{2)')].strip()
second('margin','margin note',boxes['margin'],margin)
second('cancelled-start','deletion',boxes['cancelled_start'],r'\deleted{2) \unsure{Réduire}}')
prog2live=final[final.index('2) Reprendre'):final.index(r'\deleted{et \(\mathrm{II}_1')].strip()
second('programme2-live','C/H different word',boxes['programme2'],prog2live)
prog2del=final[final.index(r'\deleted{et \(\mathrm{II}_1'):final.index('3) Eliminer')].strip()
second('programme2-deleted','deletion',boxes['programme2_deleted'],prog2del)
second('tw-insertion','insertion',[1057,811,1151,864],r'\inserted{\(\mathrm{tw}_{1/6}\)}')
prog3=final[final.index('3) Eliminer'):final.index(r'\figure{')].strip()
second('programme3','C/H different word',boxes['programme3'],prog3)
second('gauches','deletion',[867,1010,1103,1112],r'\deleted{\unsure{gauches}}')
for k,_,_,_ in draw_findings:
    second(k,'deletion' if k=='cancelled_drawing' else 'drawing',boxes[k],graphic(k))
second('isolated-arc','drawing',[1966,688,2076,770],graphic('isolated_arc'))
second('folio','margin note',boxes['folio'],r'\margin{32}')

reading_rows={
301:('Count table, f_Q subscript','Latin a preferred to H alpha; label read with whole equation.'),
303:('420 first equation','4×60 is the ink reading, including the written arithmetic discrepancy.'),
306:('420 fourth label','Detached prime resolves M0349 to the alternative.'),
311:('1020 subtotal and old number','Replacement1020 and cancelled doubtful900 retained in their positions.'),
312:('1020 fifth row','Cancelled older equality retained in doubt under the replacement.'),
314:('1020 third label','Tau prime/exponent ambiguity remains unresolved; no change row is added merely for retaining doubt.'),
321:('1020 last label','Detached prime resolves M0354.'),
323:('Old total and new1620','Former value favors1580 but remains doubtful; rules and replacement placement retained.'),
326:('Table corrections and key','H editorial notes are not source text; the visible insertion/deletion states and circled label are independently recorded.'),
331:('Programme1 opening','les|un remains doubtful; syst. is read against H rel.'),
332:('Programme1 adjective','Singular fondamental, without extra ending.'),
335:('Programme1 first clause','se, not H en.'),
338:('Programme1 cancellation and insertion','Doubtful paquets and visible de below inserted orbites.'),
341:('Programme1 parenthetical word','aux|avec retained unresolved; no certainty-only change row.'),
344:('Programme1 second clause','se, not H en.'),
347:('Cancelled start and side note','The cancelled2)Réduire remains doubtful; the note is transcribed in its own margin block. H notes are excluded as commentary.'),
348:('Side note','composés, with no extra e.'),
350:('Side-note final adjective','modulaire resolves M0358; independently observed dim. remains abbreviated.'),
353:('Cancelled start','2) clear; Réduire retained uncertain from crossed strokes. H editorial wrapper is not manuscript.'),
355:('Programme2 live preposition','du niveau0.'),
362:('Cancelled first line','Short doubtful fragment followed by de type; C longer reading unsupported.'),
364:('Cancelled verb','reviennent|revient retained with plural favored.'),
365:('Cancelled line2','de type, not du type.'),
367:('Cancelled typeIII1 punctuation','Visible point before closing parenthesis retained.'),
368:('Cancelled twist clause','relationnel|relativement remains doubtful; type label preserved.'),
369:('Cancelled final clause and interline','Clear qui donne; doubtful un Autom.; visible de = type; interlinear tw retained inside cancelled block.'),
370:('Cancelled paragraph','Reading and placement decisions logged; H explanatory note excluded.'),
371:('Programme3','Eliminer has no accent on the capital E.'),
372:('Programme3 cancelled adjective','gauches stays doubtful; no resolution is claimed from the covered letters.'),
374:('Drawings, listing, foliation, H terminal heading','Drawings reproduced; reversed printing excluded;32 retained as foliation; terminal H section title absent from this face.')
}
macro_notes={
299:'H paper description and drawing synopsis are editorial; both witnesses supply the same count-table block, with substantive differences reviewed below.',
300:'Alignment artefact: both witnesses contain the second f label.',
302:'Array spacing only.',
304:'Order of exponent and subscript only.',
305:'Order of exponent and subscript only.',
307:'Order of exponent and subscript only.',
308:'Order of exponent and subscript only.',
309:'Array spacing only.',
310:'Array wrapper only.',
313:'Invisible delimiter syntax only.',
315:'Token alignment within the label arrays; no independent extra gamma in the source.',
316:'Prime-spacing and array alignment, not a changed letter.',
317:'Token alignment within equivalent successive labels.',
318:'Token alignment of superscripts, read with complete label rows.',
319:'Token alignment of successive labels.',
320:'Prime formatting and token alignment; clear1prime and2prime labels preserved.',
322:'Array wrapper only.',
324:'Array wrapper only.',
325:'Array wrapper only.',
327:'Quotation convention: source double marks are retained in the supplied C macro convention.',
328:'Quotation convention: source double marks are retained in the supplied C macro convention.',
329:'Enumerate wrapper only.',
330:'Item wrapper only.',
333:'Math delimiter syntax only.',
334:'Math delimiter syntax only.',
336:'Math delimiter syntax only.',
337:'Math delimiter syntax only.',
339:'Math delimiter syntax only; group glyph doubt is separately retained.',
340:'Math delimiter syntax only.',
342:'Math delimiter syntax only.',
343:'Math delimiter syntax only.',
345:'Math delimiter syntax only.',
346:'Math delimiter syntax only.',
349:'Quotation convention only.',
351:'Inequality macro and misaligned H editorial words; the source has a less-than-or-equal sign and1.',
352:'Closing quote and editorial-note token alignment only.',
354:'Item wrapper only.',
356:'Math delimiter syntax only.',
357:'Math delimiter syntax only.',
358:'Math delimiter syntax only.',
359:'Math delimiter syntax only.',
360:'Math delimiter syntax only.',
361:'Math delimiter syntax only.',
363:'Math delimiter syntax only.',
366:'Math delimiter syntax only.',
373:'Math delimiter syntax only.'
}
differences_review=[]
for d in diffs:
    n=int(d['source_row'])
    if n in reading_rows:
        place,note=reading_rows[n]
        differences_review.append(dict(source_row=n,decision='reading decision',place=place,note=note))
    else:
        assert n in macro_notes,n
        differences_review.append(dict(source_row=n,decision='macro-only',place='Source difference '+str(n),note=macro_notes[n]))

label_tex=re.search(r'\\inserted\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}',final,re.S).group(0)
for b in second_boxes:
    if b['box']=='S33-row420insert':
        b['reading']=r'\inserted{\(120=1\times120=1\times120\)} '+label_tex

# Keep prose readable without modifying LaTeX, IDs, or numeric source readings.
for n in notes:
    n['text']=re.sub(r'(?<=[A-Za-z])(?=\d)',' ',n['text'])
    n['text']=re.sub(r'(?<=\d)(?=[A-Za-z])',' ',n['text'])
for ch in checks:
    ch['who']=ch['who'].replace('run20261120','run 20261120')
    ch['outcome']=re.sub(r'(?<=[A-Za-z])(?=\d)',' ',ch['outcome'])
for row in differences_review:
    row['note']=re.sub(r'(?<=[A-Za-z])(?=\d)',' ',row['note'])
    row['note']=re.sub(r'(?<=\d)(?=[A-Za-z])',' ',row['note'])
result=dict(
scan=33,reader='reader_a',lines_read=44,changes=changes,decisions=decisions,inventory=inventory,unresolved=unresolved,
notes=notes,checks=checks,hand_log=hand_log,notation=notation,abbreviations=abbreviations,second_boxes=second_boxes,differences_review=differences_review,
reader_metadata=dict(model='GPT-6 Astra Pro',effort='not exposed',run='SP82_C13_148',date='2026-11-20'),
reading_workflow=dict(
whole_page_views=1,successful_native_half_views=[1,1],
native_proxy_dimensions=[[3011,2228],[1656,2228],[1656,2228]],
native_proxy_format='JPEG quality 95, no resizing',
physical_line_count_detail='14 count rows;2 total lines;2 dictionary lines;1 heading;5 item1 lines;1 cancelled start;6 side-note lines;3 live item2 lines;4 cancelled item2 lines plus1 interlinear label;4 item3 lines;1 foliation line =44.',
crop_count=21,crop_views='All 21 saved crops viewed; no second crop of any first-pass place.',
failed_image_attempt='One half1 image return before the context rollover was truncated before a readable image arrived; the same saved proxy was then successfully viewed once.',
scope='Only scan033 packet, its whole and halves, the 21 crops, and own output were inspected. Every agreed textual character and every graphical block was checked from ink.',
omitted_non_source='The pale mirrored mechanical listing and H editorial notes/terminal heading are not source text on this face.',
no_ocr=True,no_web_research=True,no_tex_compilation=True,
root_review='Root independently viewed all 21 saved crops and reviewed candidate text; residual S/G and relationnel/relativement doubts were retained.'
))
assert len(decisions)==100
assert {x['id'] for x in decisions}=={m['id'] for m in marks}
assert len({x['id'] for x in decisions})==100
assert len(differences_review)==76
assert {x['source_row'] for x in differences_review}=={int(x['source_row']) for x in diffs}
assert len({b['box'] for b in second_boxes})==len(second_boxes)
for ch in changes:
    assert ch['against_c'] or ch['against_h']
    k='page' if ch['crop']=='page' else ch['crop'].removeprefix('crops/148_scan033_').removesuffix('.png')
    assert ch['box']==boxes[k]
for d in decisions:
    assert d['decision'] in ['first','alternative','other','undecided']
for i in inventory:
    assert i['sheet_kind'] in ['text','reused_typed','typescript','letter','list','cancelled_draft','cover']
    assert i['hand'] in ['his hand','another unnamed hand']
# Narrow structural validation only: no compilation or rendering.
assert final.count(r'\begin{tikzpicture}')==final.count(r'\end{tikzpicture}')
assert final.count(r'\begin{array}')==final.count(r'\end{array}')
assert final.count(r'\(')==final.count(r'\)')
assert r'\unsure{\mathfrak S_K|\mathfrak G_K}' in final
assert r'\unsure{relationnel|relativement}' in final
assert r'\texttt' not in final
(out/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(scan=33,changes=len(changes),decisions=len(decisions),inventory=len(inventory),unresolved=len(unresolved),checks=len(checks),second_boxes=len(second_boxes),differences=len(differences_review),lines_read=44),ensure_ascii=False))
