from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
def above(word,ins,shift='0em'):
 return r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){'+word+r'};\node[anchor=south west,inner sep=1pt] at ([xshift='+shift+r',yshift=6pt]s.north west){'+ins+'};}'
leftmark=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){certainly};\draw[gray,line width=.35pt] ([xshift=-3pt,yshift=2pt]s.south west)--([xshift=-2.4pt,yshift=-2pt]s.south west);\draw[line width=.55pt] ([xshift=-3pt,yshift=2pt]s.south west)--([xshift=-2.8pt,yshift=.5pt]s.south west);}'
points=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){the};\fill ([xshift=5pt,yshift=2pt]s.north east) circle (.3pt);\fill ([xshift=7pt,yshift=5pt]s.north east) circle (.3pt);}'
d={'cote':57,'scan':21,'sheet_kind':'letter','hand':'typewriter','replace':[
 (r'\deleted{\unsure{functors}}\inserted{factors}',above(r'\deleted{\unsure{functors}}',r'\inserted{factors}')),
 ('unramifiedness','unramified-\nness'),
 (r'infinit\unsure{é|è|e|i}s\unsure{é|è|i}mal',r'infinit\rlap{i}es\rlap{i}emal'),
 ('correspondence classes','correspondance classes'),
 ('trivial whenever','trivial whene-\nver'),
 ('certainly the case',leftmark+' the case'),
 (r'\inserted{discrete} valuation',above('valuation',r'\inserted{discrete}','-1em')),
 (r'\unsure{reduced|deduced}',r'\rlap{d}reduced'),
 ('whose restriction to the','whose restriction to '+points),
 (r'\underline{\deleted{\unsure{X}}L}',r'\underline{\mathord{\rlap{$X$}L}}'),
 (r'd\unsure{e|é|è}fined',r'd\rlap{i}efined'),
 (r'\unsure{t|f}=0',r'\mathord{\rlap{$f$}t}=0'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole scan, then both halves, then C and H. Seven broad 3× crops were read line by line; twenty-nine focused crops at 12–28× and three supplementary crops at 30–32× covered every C doubt, H difference, mathematically deciding symbol, insertion, cancellation, overprint, edge hyphen and detached mark. The typed additions and cancellations are horizontal. No OCR, delegated reading, context or LaTeX compilation was used.'}
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('opening continuation','as a quasi-projective scheme over S.','same','C retained','Each word, the quasi-projective hyphen, plain capital S and final point were read in broad 01 (245,180,1688,450), 3×.')
a('item 2 opening','Theorem of the cube. I believe ... time ago ... Pic functor ...','same','C retained','Every agreed word, the two numbering/title points and comma were checked line by line in broad 01, 3×; the final e of believe is lightly printed but identifiable.')
a('cancelled word below factors',r'\deleted{\unsure{functors}}',r'\struck{\ill{}}','C retained','The eight crowded cells have remnants compatible with functors, but the heavy x cancellations obscure several individual bowls and stems. The candidate is not promoted to a certain reading. (684,392,850,444), 18×.','low',hc=True,k=r'readable ink left as \ill{}')
a('factors placement','inline insertion after cancelled word','same','factors raised above the cancelled word','The added word is on a higher baseline, with its first f directly above the old first cell. It has no insertion guide. (684,392,850,444), 18×.','high',True,True,'insertion or placement')
a('unramifiedness edge break','unramifiedness','same','unramified- / ness','After the complete d there is the visible left portion of a short horizontal hyphen at the dark edge; the next line begins ness. (1530,405,1685,450), 14×; broad 02 (245,450,1688,720), 3×.','high',True,True,'abbreviation expanded or spelling modernised')
a('first Corr underline','Corr underlined','same','C retained','One horizontal underline runs beneath all four letters and stops after the final r. (646,479,735,523), 16×.')
a('week','week','same','C retained','Both middle letters have the bar and lower open curve of e. (1208,478,1302,517), 16×.')
a('first altered cell in infinitesimal',r'infinit\unsure{é|è|e|i}',r'infinite',r'infinit\rlap{i}e','The cell combines an e body and middle bar with a high i dot, central upright and baseline serif. Both forms are retained, with no typing order assigned. (1310,478,1582,518), 16×; (1445,482,1518,515), 30×.','medium',True,True,'misread word')
a('second altered cell in infinitesimal',r's\unsure{é|è|i}mal','simal',r's\rlap{i}emal','The second disputed cell again has an e bowl/bar beside a dotted i upright and wide foot. It is preserved as an overlap, not a clean accented vowel. Same 16× and 30× crops.','medium',True,True,'misread word')
a('correspondance','correspondence','correspondance','correspondance','The vowel after d has a closed lower bowl and right upright/foot: a. It differs from the open e in the same word. (904,616,1188,662), 12×.','high',True)
a('cancelled ending after proof',r'proof\deleted{\unsure{s}}','proofs','C retained','An x strike crosses the final cell. Its remaining upright and curved fragments do not securely identify the former letter; s remains tentative. (333,683,462,728), 20×; (429,692,459,727), 32×.','low',hc=True,k='deletion state (struck given live or live given struck)')
a('manuscript-notes prose','manuscript notes I am joining ... question 4 ... handwriting is wretched ... very sketchy','same except separately logged readings','C retained','All agreed words, the numeral 4, points and commas were read in broad 02 and broad 03 (245,720,1688,1000), 3×.')
a('dash before On the other hand','one short hyphen','long dash represented by --','C retained','There is one short horizontal typewriter stroke, occupying less than one character cell. (976,837,1008,863), 24×.',hc=True,k='other')
a('first Corr_S(X,Y)','underlined Corr with lowered S, (X,Y)','same','C retained','The underline is under Corr alone. S is lowered, both capitals are plain and the punctuation is opening parenthesis, comma, closing parenthesis. (582,966,788,1023), 14×.')
a('formal-properties paragraph','for two of the three factors ... inverse limits of Artin rings is the less trivial','same','C retained','All agreed words, capitals, parentheses and the terminal point were read in broad 03 and broad 04 (245,1000,1688,1275), 3×.')
a('second Corr_S(X,Y)','underlined Corr with lowered S, (X,Y)','same','C retained','The same four-letter underline and lowered plain S are visible; both parentheses and the internal comma are present. (878,1180,1086,1237), 14×.')
a('whenever line break','whenever','same','whene- / ver','The first line ends with a complete e and a clear short hyphen; the next begins ver. (1542,1186,1681,1224), 16×; broad 05 (245,1275,1688,1550), 3×.','high',True,True,'abbreviation expanded or spelling modernised')
a('factors and question','X,Y is separated?','same','C retained','Both plain capitals, the comma, all letters and the full question mark with lower point are visible. (1074,1256,1417,1299), 12×.')
a('cancelled if before for','if deleted','omitted','C retained','The i dot and stem and the tall f hook remain visible underneath two x strikes. (620,1327,677,1363), 24×.',hc=True,k='omission')
a('small mark left of certainly','omitted','omitted','short descending stroke drawn','A short black upper stroke continues downward as a faint gray, slightly right-sloping line, just left of the c. No letter or punctuation meaning is assigned. (242,1331,265,1370), 24×.','medium',True,True,'drawing or diagram')
a('geometric-fibre and abelian prose','for X if its geometric fibers are integral, (a fortiori ... over S !).','same','C retained','Every word, both plain capitals, comma, parentheses, separated exclamation mark and terminal point were read in broad 05, 3×.')
a('discrete placement','inline insertion before valuation','same','discrete raised above valuation, slightly to its left','The addition is on the higher baseline, beginning left of the v and ending above the middle of valuation. There is no guide or separate underline. (835,1430,1034,1504), 16×.','high',True,True,'insertion or placement')
a('reduced/deduced initial cell',r'\unsure{reduced|deduced}','reduced',r'\rlap{d}reduced','The initial cell has a d ascender and closed bowl together with the shorter r shoulder and upright. Both are preserved without assigning their order. (1386,1465,1535,1506), 20×.','high',True,True,'misread word')
a('first underlined L','underlined L','same','C retained','The capital has one underline beneath its foot. (501,1532,541,1585), 22×.')
a('points above restriction-line ending','omitted','omitted','two diagonal detached points drawn','Two compact black points stand above and just right of the ending the; the right point is higher. They do not form an attached accent. (1575,1523,1596,1547), 28×.','high',True,True,'drawing or diagram')
a('generic fibre index','X_t','same','C retained','The lowered character has a rising stem, crossbar and hooked lower end, identifying t. (522,1606,577,1661), 22×.')
a('second underlined L','underlined L','same','C retained','The capital and its separate underline were checked. (916,1606,953,1659), 22×.')
a('open subset index','X_1','same','C retained','The lowered character has the typewriter 1 form: upper left serif, straight upright and broad baseline foot. It differs from the preceding hooked t. (1271,1606,1322,1667), 22×.')
a('third underlined L','underlined L','same','C retained','The capital and its separate underline are clear. (801,1679,833,1724), 24×.')
a('overprinted object before is defined',r'\underline{\deleted{\unsure{X}}L}','underlined L','underlined overlapping X and L, order unassigned','Both diagonals of X can be separated from the straight left stem and right upturned foot of L. The underline passes below their shared cell. The shapes are secure, but the dense intersections do not establish the typing order asserted by C. (1462,1677,1505,1728), 28×.','medium',True,True,'deletion state (struck given live or live given struck)',q='The object before is defined contains both underlined X and L in one cell; the order of correction is unassigned.')
a('restriction and divisor prose','invertible sheaf on X ... assumption ... Cartier divisor whose support is contained in the special fiber','same except separately logged readings','C retained','Each agreed word, plain capital X and punctuation was read in broad 05 and broad 06 (245,1550,1688,1825), 3×.')
a('first special fibre index','X_o','X_0','C retained','The lowered character is a short rounded lowercase o, smaller in height than the full zero in the equation below. (366,1821,419,1874), 22×.',hc=True,k='misread symbol or index')
a('second special fibre index','X_o','X_0','C retained','Again the lowered character is a short rounded lowercase o. (584,1821,632,1874), 22×.',hc=True,k='misread symbol or index')
a('defined altered vowel',r'd\unsure{e|é|è}fined','defined',r'd\rlap{i}efined','The dense cell has an e body/bar together with a high i dot, central upright and wide baseline serif. Both forms are retained with no typing order. (1366,1821,1517,1865), 18×; (1393,1824,1422,1861), 30×.','medium',True,True,'misread word')
a('global equation variable',r'\unsure{t|f}=0','t=0',r'\mathord{\rlap{$f$}t}=0','The cell combines the tall loop and left foot of f with the curved lower end of t. Both forms are identifiable, but their typing order is not. The equality has two strokes and the zero is full height. (661,1890,732,1934), 24×.','medium',True,True,'misread symbol or index',q='The variable in the global equation is an f/t overprint; both forms are retained without a typing order.')
a('third special fibre index','X_o','X_0','C retained','The last lowered character is the same short rounded lowercase o. (1307,1958,1359,2016), 22×.',hc=True,k='misread symbol or index')
a('final divisor letter','D','same','C retained','A plain capital D, with left upright and rounded right body, has no underline or other decoration. (938,1959,970,2003), 20×.')
a('last two lines','by a global equation ... integral subscheme of X, from this follows ... (assume for','same','C retained','Every agreed word, plain X, comma, equation closing parenthesis and final opening parenthesis was read in broad 07 (245,1825,1688,2100), 3×. The sentence continues off this sheet without closing punctuation.')
d['unresolved']='The cancelled functors candidate and cancelled s candidate after proof remain uncertain. Paired letter and mathematical overprints preserve both visible forms without assigning a typing order; in particular no single live object is selected from X/L and no single live variable from f/t. The isolated left stroke and two upper points are reproduced without a meaning.'
d['inventory']=[
 ['text','top continuation','as a quasi-projective scheme over S.'],
 ['text','item 2 opening','Theorem of the cube ... proof ... Pic functor ... representable.'],
 ['deletion','below raised factors','uncertain functors'],
 ['insertion','above cancelled word','factors'],
 ['text','item 2 unramifiedness passage','To prove unramified- / ness ... week ... theorem of the square ...'],
 ['drawing','under first Corr','one underline'],
 ['insertion','first disputed infinitesimal cell','overprinted i/e'],
 ['insertion','second disputed infinitesimal cell','overprinted i/e'],
 ['text','notes enclosed','manuscript notes ... correspondance classes ... question 4 ...'],
 ['deletion','after proof','uncertain s'],
 ['text','handwriting qualification','I hope ... handwriting is wretched ... very sketchy.'],
 ['text','formal deduction','On the other hand ... separatedness ... formal properties ... inverse limits ...'],
 ['drawing','under first Corr_S(X,Y)','underline beneath Corr alone'],
 ['text','item 3 opening','As for the separatedness ... whene- / ver ... separated?'],
 ['drawing','under second Corr_S(X,Y)','underline beneath Corr alone'],
 ['text','geometric-fibre assumption','Now this is certainly the case ... integral ... abelian scheme over S !).'],
 ['drawing','left of certainly','short dark and gray descending stroke','unidentified hand'],
 ['deletion','before for X','if'],
 ['text','valuation reduction','To show this ... spectrum of a ... valuation ring ... reduced overprint ...'],
 ['insertion','above valuation','discrete'],
 ['insertion','first reduced/deduced cell','overprinted d/r'],
 ['text','invertible sheaf and restriction','show that if underlined L ... restriction ... general fiber X_t ... trivial.'],
 ['drawing','under first L','one underline'],
 ['drawing','above the at restriction-line end','two diagonal detached points','unidentified hand'],
 ['drawing','under second L','one underline'],
 ['text','open subset and divisor','Now X_1 ... assumption on underlined L ... overprinted X/L ... Cartier divisor ... special fiber X_o.'],
 ['drawing','under third L','one underline'],
 ['insertion','object before is defined','overprinted X/L, order unassigned'],
 ['drawing','below X/L overprint','one underline'],
 ['text','Cartier property of fibre','Now X_o itself ... Cartier divisor ... global equation ... integral subscheme of X,'],
 ['insertion','defined vowel','overprinted i/e'],
 ['insertion','equation variable','overprinted f/t, order unassigned'],
 ['text','last line','from this follows ... divisor D ... multiple of X_o (assume for'],
 ]
rv['commit'](d)
