from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
def above(word,ins,shift='0em',guide=False):
 s=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){'+word+r'};\node[anchor=south west,inner sep=1pt](a) at ([xshift='+shift+r',yshift=6pt]s.north west){'+ins+r'};'
 if guide:s+=r'\draw ([xshift=-3pt,yshift=-3pt]s.south west) to[out=100,in=180] ([xshift=0pt,yshift=-2pt]a.south west)--([xshift=0pt,yshift=-2pt]a.south east) to[out=0,in=-70] ([xshift=5pt,yshift=5pt]a.south east);'
 return s+'}'
ie=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){i};\draw[line width=.6pt] ([xshift=-1.5pt,yshift=3pt]s.north)--([xshift=1.5pt,yshift=3pt]s.north) ([yshift=3pt]s.north)--([yshift=4.2pt]s.north);\fill ([yshift=-2pt]s.south) circle (.5pt);\draw[line width=.7pt] ([xshift=-1pt,yshift=-3.2pt]s.south)--([xshift=.4pt,yshift=-3.5pt]s.south);}.e.'
hmark=r'T\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){h};\draw[line width=.7pt] ([xshift=.2pt,yshift=2pt]s.south west) to[out=150,in=130] ([xshift=.6pt,yshift=-5pt]s.south west) to[out=70,in=140] ([xshift=-1pt,yshift=-2pt]s.south east)--([xshift=-.2pt,yshift=-5.5pt]s.south east); }at'
arrow=r'\mathrel{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\to$};\draw[gray,line width=.25pt] ([xshift=1pt,yshift=.5pt]s.west) to[out=30,in=180] ([xshift=5pt,yshift=2pt]s.west);}}'
spoints=r'\mathord{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$S$};\fill ([xshift=1pt,yshift=-3pt]s.south) circle (.25pt);\fill ([xshift=-1pt,yshift=-5pt]s.south) circle (.22pt);}}'
base=r'b\kern-.2em\raisebox{-.6ex}{\inserted{\handwritten{\unsure{a}}}}\kern-.2em se'
d={'cote':57,'scan':20,'sheet_kind':'letter','hand':'typewriter','replace':[
 (r'\deleted{\unsure{make}}\unsure{give}',r'\rlap{\deleted{\unsure{make}}}gi\unsure{v}e'),
 (r'$X$ and $Y$ \inserted{locally} of',r'$X$ and $Y$ '+above('of',r'\inserted{locally}','-.75em',True)),
 (r'\deleted{Y}\handwritten{S}',r'\rlap{\deleted{$Y$}}\handwritten{S}'),
 (r'$X$ \inserted{locally} of',r'$X$ '+above('of',r'\inserted{locally}','-2em')),
 ('Assume that the',r'Assume t\rlap{a}h\rlap{h}at the'),
 (r'\inserted{R=}X',r'\mathord{'+above('$X$',r'\inserted{$R=$}','-1em')+'}'),
 ('defined by',r'define\rlap{\deleted{e}}\handwritten{d} by'),
 (r'\unsure{exists}',r'exis\unsure{t}% clipped by right edge; no final s is visible'+'\n'),
 (r'\unsure{i.e.}',ie),
 (r'\deleted{type}\inserted{pres.}',above(r'\deleted{type}',r'\inserted{pres.}')),
 (r'\deleted{Y}S',r'\mathord{\rlap{$Y$}\raisebox{-.15ex}{$S$}}'),
 (r'$Z\handwritten{\to}Y$',r'$Z\handwritten{'+arrow+r'}Y$'),
 ('can be expressed by','can be expres-\nsed by'),
 ('That is in fact',hmark+' is in fact'),
 ('finite type over $S$, $H$',r'finite type over $'+spoints+r'$, $H$'),
 (r'closed \inserted{and flat} sub-group',r'closed '+above('sub-group',r'\inserted{and flat}','-2em')),
 (r'\deleted{\unsure{affi}}',r'\deleted{affi}'),
 ('fibre, then $G$',r'fibre, th\rlap{e}an $G$'),
 (r'b\unsure{a}se',base),
 ('to the case when',r'to the c\rlap{q}ase when'),
 ('quasi-affiness','quasi-affinness'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole scan, then both halves, then C and H. Seven broad 3× crops were read line by line. Thirty-seven focused crops at 12–28× covered every C doubt, H difference, symbol deciding the mathematics, raised addition, cancellation, overprint, clipped ending and detached mark. The inserted base-letter candidate was also checked at 22× rotated 30 degrees counterclockwise, and the first corrected base at 20× rotated 12 degrees clockwise. No OCR, delegated reading, context or compilation was used.'}
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('salutation and opening','Dear Murre, ... I am glad to hear ...','same','C retained','The salutation, comma and every agreed word were checked in top (240,208,1570,535), 3×. No date or signature occurs on this sheet.')
a('overwritten make candidate',r'\deleted{\unsure{make}}','omitted','C retained, overlapped with replacement','The m-like arches, a bowl and tall k-like stem support make, but the double typing prevents a secure separation of all old strokes. (1287,286,1382,323), 20×.','low',hc=True,k='omission')
a('replacement give',r'\unsure{give}','give',r'gi\unsure{v}e','The descender loop of g, high i dot and final e are identifiable; the third letter is still obscured by the tall overprinted stem and feet. (1287,286,1382,323), 20×.','low',True,True,'misread word')
a('make/give placement','sequential old and new words','give only','overlapping word forms','The two sets of characters occupy the same typewriter cells rather than adjacent positions. (1287,286,1382,323), 20×.','high',True,True,'insertion or placement')
a('opening idiom','Here what I can say to your questions.','same','C retained','The ink has Here what without an intervening is. top, 3×.')
a('first following',r'foll\unsure{owing|hwing}','following','C retained','The crowded cell after foll has a high upright or dot-like top and a dark rounded body; the ordinary o and h alternatives are not securely separated. The wing and colon are clear. (252,498,449,533), 16×.','low',hc=True,k='misread word')
a('Theorem punctuation','Theorem underlined, no point','Theorem with a point','C retained','There is one continuous underline and blank space after the final m, with no punctuation point. (252,566,408,606), 18×.',hc=True,k='text not on the page')
a('first morphism','f:X arrow Y','same','C retained','Both colon points, plain capitals and right arrowhead are present. (507,568,652,602), 16×.')
a('first locally placement','inline insertion before of','inline insertion replacing of','locally raised above live of, with curved guide','The addition is on a higher baseline. Its curved guide enters at the left of of, runs below locally and turns up at the right. (388,601,564,684), 14×.','high',True,True,'insertion or placement')
a('of deletion state','of live','of deleted','C retained','The same guide crosses only the edge of o; there is no cancellation across the word. The f remains wholly clear. (388,601,564,684), 14×.',hc=True,k='deletion state (struck given live or live given struck)',q='Of remains live after the raised locally; H wrongly treats it as cancelled.')
a('first corrected base','deleted Y then handwritten S','same with reservation','C retained, forms overlapped','The typed fork and foot of Y are crossed by the larger hand-drawn upper and lower curves of S. (949,630,998,681), 20×, also rotated 12 degrees clockwise.','high',True,True,'insertion or placement',m='yes')
a('second locally placement','inline insertion after X','same','locally raised above X and the following of','The entire word is on the higher line, beginning to the left of of; no independent guide is present. (1361,603,1515,643), 14×; theorem (244,561,1616,765), 3×.','high',True,True,'insertion or placement')
a('loc noeth abbreviation','loc noeth','same','C retained','Neither loc nor noeth has an abbreviation point. theorem, 3×.')
a('mark above Y after type over',r"Y\handwritten{\unsure{'}}",'Y','C retained','A short oblique stroke stands above and to the right of Y. It is thicker at the upper left and narrows downward; the prime-like reading remains tentative. (446,696,480,742), 20×.','low',hc=True,k='omission')
a('Assume','Assume','same','C retained','The two m arches are ink-heavy but show no independently identifiable second character. (504,713,625,743), 20×.')
a('that after Assume','that','same',r't\rlap{a}h\rlap{h}at','Both middle cells combine an h ascender and an a bowl and crossbar, in opposite relative positions. Both forms are retained without a typing order. (641,708,727,743), 20×.','high',True,True,'misread word')
a('R equals placement','inline insertion before product','same','R equals above the first X, slightly to its left','The R and two equality strokes are on the raised baseline. (1203,676,1339,759), 14×.','high',True,True,'insertion or placement')
a('equivalence-relation product','X lowercase x over Y X','same product','C retained','The product sign is a short serifed x and Y is lowered; the two outer X letters are tall. (1203,676,1339,759), 14×. No change of the fibre-product reading is counted for the witnesses’ typographical macro choice.')
a('defined final letter','defined','same',r'define\rlap{\deleted{e}}\handwritten{d}','The last cell retains the typed e bar and lower curve, with a hand-drawn tall upright and right closing stroke forming d over it. (1350,697,1495,744), 16×.','high',True,True,'omission')
a('flat projection','pr_1:X x_Y X arrow X','same','C retained','The lowered serifed 1, colon, lowered Y and plain right arrow were all checked. (640,775,905,828), 12×.')
a('first quotient','X/R','same','C retained','The diagonal is a slash between plain X and R, with no subscript. (1478,776,1550,820), 18×.')
a('clipped exists',r'\unsure{exists}','exists',r'exis\unsure{t}; no unseen final s','The e, x, i and s are complete. A portion of the next t-like cell is visible at the black edge, but there is no visible final s. (1574,778,1680,818), 18×.','low',True,True,'misread word')
a('i.e. reading',r'\unsure{i.e.}','i.e.','i.e.','The i, e and both baseline points are clear despite the marks above and below i. (933,836,1018,897), 18×.','high',True)
a('marks around i of i.e.','omitted','omitted','upper short bar and upright; lower point and short stroke drawn','A short horizontal with a central upward projection lies above the i dot. A detached point and another short stroke lie below its foot. No punctuation meaning is assigned. (933,836,1018,897), 18×.','high',True,True,'drawing or diagram')
a('compositum formula','X blank Z blank Y','X arrow Z arrow Y, with a note that arrows are absent','C retained','Both intervals contain blank paper, without shafts or heads. (479,914,742,959), 12×. H inserts arrows in its text while noting their absence.',hc=True,k='text not on the page',q='The compositum is written X, Z, Y with blank gaps; the arrows supplied by H are absent from the scan.')
a('object after with',r'\unsure{\mathbb{X}|\mathbb{Y}}','X','C retained','The heavy glyph has multiple upright and diagonal strokes, including an extra right upright. They do not securely separate into one plain X or Y, nor establish an overtyping sequence. (870,918,907,952), 24×.','low',hc=True,k='misread symbol or index')
a('gap before faithfully flat target','uncertain object blank Z','X arrow Z, with an absence note','C retained','The gap before Z is unmarked; no arrow shaft or head is visible. (863,914,1021,959), 16×.',hc=True,k='text not on the page',q='The gap before the faithfully flat target Z is blank; H supplies an absent arrow.')
a('cancelled type','type deleted','same','C retained','The t curve, descending y, p bowl and descender, and final e remnants can be distinguished beneath the x strikes. (1051,977,1150,1030), 18×.')
a('pres. placement','inline insertion after type','same','pres. raised above cancelled type','The abbreviation is on the higher baseline with a terminal point; there is no separate guide. (1051,977,1150,1030), 18×.','high',True,True,'insertion or placement')
a('second overprinted base','deleted Y followed by S','deleted S followed by Y, with reservation','overprinted Y and S, order unassigned','The top fork and upright of Y coexist with the two rounded S curves; the S is slightly lower. The dense intersection does not establish which was typed last. Both are preserved without declaring either the live base. (1244,991,1277,1027), 26×.','medium',True,True,'deletion state (struck given live or live given struck)',m='yes',q='The base after finite pres. contains both Y and S; the opposite correction orders asserted by C and H are not settled by the ink.')
a('parenthetical finite-presentation statement','in fact ... over S if X is so','same','C retained','Every word, plain S and X, both parentheses and final and were checked in flat (245,771,1688,1105), 3×.')
a('monomorphism arrow','Z arrow Y','same','C retained','The main arrow has a single right head and runs from Z toward Y. (954,1063,1061,1101), 16×.')
a('faint upper stroke by monomorphism arrow','omitted','omitted','short gray curve above left portion of shaft drawn','A thin gray stroke rises above the left part of the black arrow shaft and bends right, without an identifiable separate head or label. (954,1063,1061,1101), 16×.','medium',True,True,'drawing or diagram')
a('andthe','andthe','same','C retained','There is no full word space between d and t. (1109,1136,1220,1171), 16×.')
a('expressed line break','expressed','same','expres- / sed','The upper line ends with expres and a visible short hyphen at the clipped edge; the next line starts sed. (1546,1136,1682,1177), 16×; unique (247,1126,1688,1315), 3×.','high',True,True,'abbreviation expanded or spelling modernised')
a('quotient-sheaf prose','for the fpqc topology; X/R; representable','same','C retained','The letters fpqc, parentheses and the repeated plain X/R were checked in (1167,1204,1456,1241), 12× and (1458,1200,1540,1245), 16×; all surrounding words were read in unique, 3×.')
a('mark attached to h in That','omitted','omitted','loop and two lower extensions drawn at h','A dark loop joins the lower left of h and descends, with another downward branch at its right. The shape is drawn without treating it as an additional readable letter. (540,1272,631,1314), 18×.','high',True,True,'drawing or diagram')
a('Raynaud paragraph opening','Raynaud has recently ... discrete valuation ring ...','same','C retained','Every word, comma, parenthesis and named letter was read in ray (245,1337,1648,1519), 3×; the faint application letters remain identifiable.')
a('two detached points below S','omitted','omitted','two points below S drawn','Two compact dark points lie diagonally below S before the H clause; the right one is higher. (1520,1517,1545,1547), 28×. No meaning is assigned.','high',True,True,'drawing or diagram')
a('and flat placement','inline insertion after closed','same','raised and flat above the closed/sub-group boundary','Both words are on a higher baseline, starting over the end of closed and extending over the first part of sub-group. No guide is visible. (322,1519,491,1554), 16×; application (245,1519,1665,1814), 3×.','high',True,True,'insertion or placement')
a('generic quotient','G_t/H_t','same','C retained','Both lowered characters have the ascender, crossbar and lower curve of t; the oblique between G and H is a slash. (949,1552,1059,1609), 16×.')
a('cancelled affi',r'\deleted{\unsure{affi}}','affine deleted','affi deleted','The cancelled fragment has the a bowl, two separate f hooks and a dotted i. Only four cells occur before the following space; there is no n or e. (1125,1555,1216,1593), 18×.','high',True,True,'misread word')
a('first then and quotient','then G/H','same','C retained','The e has a middle bar and lower curve; the capitals and slash are clear. (774,1628,962,1664), 14×.')
a('affineness prose','quasi-affine and flat S-scheme ... H is invariant ...','same','C retained','Every agreed word, hyphen, capital S/H/G and parenthesis was read in application, 3×.')
a('then/than after generic fibre','then','than',r'th\rlap{e}an','The disputed cell combines a rounded e body and bar with the lower bowl and right foot of a. Both forms are retained without assigning their order. (1515,1774,1608,1808), 18×.','medium',True,True,'misread word')
a('inserted a candidate in base',r'b\unsure{a}se','base',r'b with low inserted handwritten \unsure{a}, then se','The machine text reads bse. A lower, sloping hand-drawn loop and long exit stroke lie between b and s; a remains tentative. (1127,1838,1194,1880), 22×, also rotated 30 degrees counterclockwise.','low',True,True,'insertion or placement')
a('case overprint','case','same',r'c\rlap{q}ase','The second cell has the a bowl and foot together with a q-like right descender ending in a horizontal foot below the baseline. No typing order is assigned. (1464,1914,1548,1952), 20×.','high',True,True,'misread word')
a('quasi-affinness','quasi-affiness','quasi-affinness','quasi-affinness','Two separate n arches and stems follow the i before e. (502,1984,898,2024), 12×.','high',True)
a('last clause and quotient','namely to construct still G/H','same','C retained','All words were read in end (244,1826,1677,2028), 3×; the last quotient has plain G and H with a slash and no terminal punctuation. (1558,1982,1630,2027), 20×.')
d['unresolved']='The overwritten make candidate, third letter of give, first following overprint, prime-like mark by Y, clipped t-like cell of exists, heavy object after with, and low handwritten a-like addition in base remain doubtful. The Y/S typing order in the second base correction cannot be settled. Other paired overprints retain both forms without order; detached marks carry no inferred meaning.'
d['inventory']=[
 ['text','salutation','Dear Murre,'],
 ['text','opening paragraph','I am glad ... unramified functors ... questions.'],
 ['deletion','before the talk','uncertain make overprinted'],
 ['insertion','over old make','gi uncertain v e'],
 ['text','numbered item 1','The theorem about passage ... foll uncertain owing/hwing:'],
 ['text','theorem opening','Theorem Let f:X to Y ... morphisme of S-preschemes ...'],
 ['drawing','under Theorem','one horizontal underline','his hand'],
 ['insertion','first morphism','right arrow','his hand'],
 ['text','first alternative','X and Y ... of finite presentation over ...'],
 ['insertion','above first of','locally'],
 ['drawing','under first locally','curved insertion guide crossing edge of live of','his hand'],
 ['deletion','first base correction','typed Y'],
 ['insertion','over first Y','handwritten S','his hand'],
 ['text','second alternative','or Y loc noeth and X ... of finite type over Y'],
 ['insertion','above second X/of','locally'],
 ['drawing','above Y after type over','prime-like oblique stroke','his hand'],
 ['text','relation assumption','Assume that the equivalence relation ... defined by f ...'],
 ['insertion','middle two cells of that','overlapping a/h and h/a'],
 ['insertion','above first X of product','R equals'],
 ['deletion','last cell of defined','typed e'],
 ['insertion','over last cell of defined','handwritten d','his hand'],
 ['text','flatness and quotient','is flat ... pr_1 ... Then the quotient X/R exis partial t'],
 ['insertion','projection morphism','plain right arrow','his hand'],
 ['text','factorization sentence','in the strongest reasonable sense, i.e. ... compositum X blank Z blank Y ...'],
 ['drawing','above and below i of i.e.','upper bar/upright and two lower marks','unidentified hand'],
 ['text','properties of factorization','with uncertain heavy object blank Z faithfully flat ...'],
 ['deletion','before over second base','type'],
 ['insertion','above cancelled type','pres.'],
 ['insertion','second base','overprinted Y/S forms, order unassigned'],
 ['text','parenthetical and monomorphism','in fact ... over S ... Z arrow Y a monomorphism.'],
 ['insertion','monomorphism arrow','right arrow','his hand'],
 ['drawing','above monomorphism arrow shaft','short faint gray curve','unidentified hand'],
 ['text','uniqueness paragraph','Of course ... andthe theorem ... expres- / sed ... quotient sheaf ...'],
 ['text','end of uniqueness paragraph','That is in fact how the theorem is proved.'],
 ['drawing','attached below h in That','loop and two descending extensions','unidentified hand'],
 ['text','Raynaud application introduction','Raynaud has recently ... discrete valuation ring ... G ... H ...'],
 ['drawing','below S before H','two detached points','unidentified hand'],
 ['insertion','above closed/sub-group boundary','and flat'],
 ['text','subgroup assumption','closed ... sub-group scheme ... G_t/H_t ... quasi-affine ...'],
 ['deletion','before first quasi-affine','affi'],
 ['text','quotient conclusion','then G/H ... quasi-affine and flat S-scheme ... invariant ...'],
 ['insertion','then/than after generic fibre','overprinted e/a'],
 ['text','one-dimensional base and current work','This extends immediately ... bse with added letter ... Raynaud is now trying ...'],
 ['insertion','low between b and s of base','uncertain a','his hand'],
 ['insertion','case second cell','overprinted q/a'],
 ['text','last line','he drops the quasi-affinness assumption, namely to construct still G/H'],
 ]
rv['commit'](d)
