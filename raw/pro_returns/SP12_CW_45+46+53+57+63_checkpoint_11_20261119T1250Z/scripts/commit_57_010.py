from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
def above(word,ins,shift='0em'):
 return r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){'+word+r'};\node[anchor=south west,inner sep=1pt](a) at ([xshift='+shift+r',yshift=7pt]s.north west){'+ins+r'};\draw ([xshift=-3pt,yshift=-2pt]s.south west) to[out=90,in=180] ([xshift=0pt,yshift=-2pt]a.south west)--([xshift=0pt,yshift=-2pt]a.south east) to[out=0,in=-90] ([xshift=3pt,yshift=3pt]a.south east);}'
tensor=r'\mathord{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\mathrm{x}$};\draw[line width=.5pt] ([xshift=.5pt,yshift=1.3pt]s.center) ellipse[x radius=3pt,y radius=4.5pt];}}'
oldright=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){which};\node[anchor=south west,inner sep=0pt] at ([xshift=-1em,yshift=9pt]s.north west){\inserted{\deleted{$=X\widehat{'+tensor+r'}_k B$}}};}'
oval=r'\mathord{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\underline{D}$};\node[anchor=south west,inner sep=3pt](a) at ([xshift=-.2em,yshift=6pt]s.north west){\inserted{\handwritten{$(\operatorname{Pic}(B)+$}}};\draw[line width=.4pt] ([xshift=2pt,yshift=-2pt]a.south west) to[out=160,in=180] ([xshift=-2pt]a.west) to[out=90,in=180] (a.north) to[out=0,in=90] ([xshift=3pt]a.east) to[out=-90,in=0] ([xshift=-2pt,yshift=-2pt]a.south west);\draw ([xshift=-4pt,yshift=-5pt]s.south west) to[out=90,in=-140] ([xshift=-1pt,yshift=-2pt]a.south west);}}'
arrow=r'\mathrel{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\unsure{\hookrightarrow|\longleftrightarrow}$};\fill ([xshift=1pt,yshift=-5pt]s.south) circle (.3pt);}}'
points=r'\qquad\qquad\mathord{\tikz[x=1em,y=1em,baseline=-.8ex]{\fill (0,0) circle (.3pt);\fill (.13,.19) circle (.3pt);}}'
d={'cote':57,'scan':10,'sheet_kind':'typescript','hand':'typewriter','replace':[
 ('to filtering','to '+r'\rlap{d}filtering'),
 (r'\deleted{\unsure{are}}',r'\deleted{are}'),
 (r'\inserted{\handwritten{(i.e. noetherian)}} arguments',above('arguments',r'\inserted{\handwritten{(i.e. noetherian)}}','-1em')),
 (r'\deleted{namely}',r'\deleted{namely}\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){x};}'),
 (r'\unsure{X_T|Y}',r'\unsure{X_{TB}|X_T|Y_B|Y}'),
 (r'\inserted{\handwritten{X\widehat{\otimes}_k B}}=',r'\mathord{'+above('$=$',r'\inserted{\handwritten{$X\widehat{\otimes}_k B$}}','-4em')+'}'),
 (r'\inserted{\deleted{\handwritten{$\unsure{=X\widehat{\otimes}_k B}$}}}, which',', '+oldright),
 (r'\handwritten{\widehat{\otimes}}',r'\handwritten{\widehat{'+tensor+'}}'),
 (r'\handwritten{\otimes}',tensor),
 (r'\deleted{\unsure{\longrightarrow P(B)}}',r'\deleted{\unsure{\longrightarrow}P(B)}'),
 (r'\unsure{n|k}','k'),
 ('and thus on','and thus '+r'\rlap{P}on'),
 (r'\handwritten{/\operatorname{Pic}(B)}',r'\handwritten{/\operatorname{Pic}\unsure{(}B)}'),
 (r'\inserted{\handwritten{which is a \uline{separated} presheaf,}} this',above('this',r'\inserted{\handwritten{which is a \uline{separated} presheaf,}}')),
 ('the group for obstructions','the group fcr obstructions'),
 (r'\unsure{beleng|belong}',r'\unsure{beleng|belang|belong}'),
 (r'\deleted{\unsure{Q(B)}}',r'\deleted{Q(B\unsure{)}}'),
 (r'\deleted{\unsure{sheaf}}',r'\deleted{\unsure{sehaf|sheaf}}'),
 (r'\inserted{\handwritten{(\operatorname{Pic}(B)+}}\underline{D}',oval),
 (r'\handwritten{\unsure{\hookrightarrow|\longleftrightarrow}}',r'\handwritten{'+arrow+'}'),
 (r'\inserted{\handwritten{for instance}} if',above('if',r'\inserted{\handwritten{for instance}}','-1em')),
 ('$X_o$ has','$X_o$ '+r'\unsure{hes|has}'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole page and both halves before C and H, then read seven broad 3× crops line by line. Thirty-eight focused crops at 7–28× and five supplements at 18–24× covered all C doubts, H differences, mathematical signs, cancellations, additions and detached marks. Focused crops 23–25 were redisplayed after a truncated output, and were actually seen. The first description crop missed its initial d, so a corrected 24× crop was inspected. The additions (i.e. noetherian), the equation-19 right formula, separated and both for-instance phrases were rotated 1–1.5 degrees clockwise; the cancelled right formula 3 degrees counterclockwise and the oval addition 5 degrees counterclockwise. No OCR, delegated reading, context or compilation was used.'}
c=(rv['WIT']/rv['row'](57,10)['codex_file']).read_text()
for number in (19,20):
 tag=r'\tag*{('+str(number)+')}'
 pos=c.index(tag);i=c.rfind('\\[',0,pos);j=c.index('\\]',pos)+2
 block=c[i:j];inner=block[2:block.index(tag)].strip();current=block
 for old,new in d['replace']:
  inner=inner.replace(old,new);current=current.replace(old,new)
 if number==20:inner+=points
 d['replace'].append((current,'\\[\n\\begin{aligned}\n('+str(number)+r')\qquad\qquad & '+inner+'\n\\end{aligned}\n\\]'))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('opening continuation','on the other hand ... finite presentation ...','same','C retained','Every word and the plain P and k were read in top (260,183,1665,438), 3×; the sentence begins as a continuation.')
a('afunctor spacing','afunctor','a functor','C retained','The a is followed immediately by f in consecutive typewriter cells, with no intervening blank. (527,260,702,294), 12×.',hc=True,k='other')
a('initial filtering overprint','filtering','filtering','overlaid d and f, followed by iltering','The initial cell has a left bowl and high left serif together with the right upper curve and crossbar of f. Both forms are retained without assigning their order. (784,260,824,296), 22×.','medium',True,True,'omission')
a('therefore across line break','therefore','same','C retained','The next line begins with the crowded f and o of fore; there is no separately identifiable additional letter. (268,328,318,365), 20×.')
a('restriction and finite type prose',"it's restriction ... a fortiori",'same','C retained','The apostrophe, words and k were checked directly in top, 3×; the wording is not corrected.')
a('old are',r'\unsure{are} deleted','omitted','are deleted','The initial a bowl, r hook and final e bar and lower curve survive the overstrikes. (1019,408,1089,436), 18×.','medium',True,True,'omission')
a('noetherian qualification placement','inline before arguments','same','above arguments with long curved guide','The parenthesized hand phrase is above arguments. Its guide rises on the left, passes below the words and turns upward at the right. (1443,356,1666,447), 8×, rotated 1 degree clockwise.','high',True,True,'insertion or placement')
a('existence theorem prose','using the existence theorem ... (18)','same','C retained','All words and the parenthesized 18 were checked in existence (264,448,1635,747), 3×.')
a('cancelled namely','namely deleted','same','C retained','All six letters remain legible beneath the typed x strokes. (1468,542,1620,581), 14×.')
a('overstrike after namely','omitted','omitted','additional x-shaped overstrike drawn','An additional full x stands after the cancelled y and before the blank. No underlying letter is inferred. Same 14× crop.','high',True,True,'drawing or diagram')
a('T and first ring definition','T=Spec(B); C=A hatted tensor k B=lim A-n tensor k B','same','C retained; tensor x and oval forms drawn','T, equals, Spec, B and parentheses are clear. In the display only the first tensor has a separate hat; lim has no written index or arrow; n is under A and k under both products. (697,610,932,651), 10×; (639,665,1138,742), 8×. The tensor drawing changes only the encoding.')
a('augmentation prose','which is an adic ... definition','same','C retained','Every word, parenthesis and the plain B were checked in consider (264,751,1655,931), 3×.')
a('cancelled expression after Consider',r'\unsure{X_T|Y} deleted',r'\ill{} deleted',r'\unsure{X_{TB}|X_T|Y_B|Y} deleted','A large crossed upper character and two lower cells survive; the lower left has a T-like top and foot, while the lower right has two B-like enclosed spaces. Dense overstrikes prevent a secure reconstruction. (1171,826,1232,883), 18×; (1170,819,1236,887), 22×.','low',True,True,'misread symbol or index',m='yes')
a('replacement X completed tensor k B','inline before equals','same','above equals and old expression, with guide','The addition is above the cancelled expression and equality. Its guide descends just before equals and rises at the far right. X, hat, tensor, k and B are readable. (1158,781,1298,886), 10×.','high',True,True,'insertion or placement')
a('right equality X tensor A C','X tensor A C','same','C retained; physical tensor form drawn','The lowered A, capital C, equality and uncapped oval around the typed x are visible. (1271,825,1390,883), 12×.')
a('cancelled right interline addition',r'\unsure{=X\widehat{\otimes}_k B} deleted after base formula','omitted','=X completed tensor k B, cancelled above which','The equality strokes, serifed X, enclosing oval and hat, lowered serifed k and B with two bowls remain visible through long oblique cancellations. The expression lies above which. (1389,777,1513,839), 14×, rotated 3 degrees counterclockwise.','medium',True,True,'omission')
a('proper scheme prose','which is a proper scheme over C. We then have','same','C retained','The phrase and punctuation were read in consider, 3×.')
a('equation 19 label','right-side tag','right-side tag','label at left','The typed (19) is at the left margin, before the formula. eq19 (268,944,1675,1040), 3×.','high',True,True,'insertion or placement')
a('equation 19 first relation','wave over right arrow','simeq','C retained','The upper wave and the lower shaft with a right-pointing head are separate. The first Pic, tensor hat and k are clear. (644,947,872,1031), 12×.',hc=True,k='misread symbol or index',q='Equation (19) has a right-pointing arrow beneath the wave; H replaces it with simeq.')
a('equation 19 inverse limit','left arrow below lim, n below arrow; Pic(X-nB),','same','C retained','The arrowhead points left, n is beneath it, and the lowered nB, both parentheses and comma are visible. (880,961,1126,1028), 12×.')
a('equation 19 cancelled ending',r'\unsure{\longrightarrow P(B)} deleted',r'\ill{} deleted',r'\unsure{\longrightarrow}P(B) deleted','The P stem and bowl, both parenthesis curves and B bowls remain legible. The earlier horizontal sign is crossed by dense blue hatching, so its direction remains uncertain. (1123,958,1281,1010), 16×.','low',True,True,r'readable ink left as \ill{}',m='yes')
a('equation 19 added formula placement','at right of same display','outside display after it','C retained','The handwritten Pic quotient and hooked arrow occupy the right side of the same horizontal line. (1279,956,1674,1024), 8×, rotated 1.5 degrees clockwise.',hc=True,k='insertion or placement')
a('equation 19 added tensor base',r'\unsure{n|k}','k','k','The lowered character has a tall left stem and two right arms, rather than an n arch. (1370,987,1409,1014), 24×.','high',True,False,'misread symbol or index',q='The handwritten base index in the right addition to (19) is k; C had left n/k unresolved.')
a('equation 19 added quotient and arrow','Pic completed tensor quotient Pic(B), hook to P(B)','same','C retained','The hand P/i/c forms, hat, slash, both arguments and right arrowhead are readable; the left end returns upward. The terminal closing parenthesis remains visible at the dark edge. Same right formula crop, 8×.')
a('on overprint after and thus','on','on','P and o overlaid, followed by n','A capital P top, bowl and stem overlap a lower o loop in the first cell. The following n is separate. (453,1038,508,1080), 20×.','high',True,True,'omission')
a('noetherian underline','underlined','emphasis','C retained','A separate line runs below noetherian. (509,1042,718,1081), 10×. H emphasis carries the same intended emphasis, so no macro-only collation row is counted.')
a('functor map and first Pic expression','B mapsto Pic(X completed tensor k B)','same','C retained','The left bar, shaft and right head, Pic letters, hat, lowered k and parentheses are visible. (709,1090,1005,1163), 10×.')
a('added Pic(B) left parenthesis','certain opening parenthesis','same','opening parenthesis uncertain','A very crowded vertical/curved trace immediately precedes the B stem; it cannot be cleanly separated from that stem. The closing curve is visible. (935,1095,1003,1155), 24×.','low',True,True,'misread symbol or index')
a('comma after quotient','none','comma','C retained','There is no comma between the added Pic(B) and the insertion guide; the visible oblique stroke belongs to the guide. (998,1062,1498,1177), 7×, rotated 1 degree clockwise.',hc=True,k='text not on the page')
a('separated qualification placement','inline before this','same','above this with long curved guide','The hand clause lies above this. The guide descends on the left and turns upward beyond its right end; its final comma is visible. Same 7× upright crop.','high',True,True,'insertion or placement')
a('separated underline','underlined separated','plain separated','C retained','A short independent line is directly beneath separated, distinct from the much longer insertion guide. Same crop.',hc=True,k='omission')
a('initial d of description','description','same','C retained','The apparent detached mark is the top serif and upper piece of a weakly printed d ascender, above its bowl. (411,1171,450,1215), 24×. The earlier (447,1180,479,1214) crop showed s instead and did not support this decision.')
a('group fcr obstructions','group for obstructions','same','group fcr obstructions','The middle character is open on the right, with two separated rounded terminals; it reads c. (1467,1180,1538,1215), 20×.','high',True,True,'misread word')
a('crowded vowel before ng',r'\unsure{beleng|belong}','belong',r'\unsure{beleng|belang|belong}','A middle bar gives an e-like form, while a heavy right side and lower foot also leave an a-like shape. The crowded printing does not settle a single vowel. (661,1249,805,1289), 14×; (654,1243,809,1294), 18×.','low',True,True,'misread word')
a('last Pic expression of P paragraph','Pic(X completed tensor k B)','same','C retained','The separate hat, added oval around x, lowered k, B and both parentheses are visible. (855,1229,1048,1298), 10×.')
a('old Q(B) before B mapsto Q(B)',r'\unsure{Q(B)} deleted','omitted',r'Q(B\unsure{)} deleted','The Q loop and descending tail, opening curve and B bowls can be identified under the x strokes. The final closing curve is obscured in the last crossed cell. (548,1315,639,1362), 18×.','low',True,True,'omission')
a('old word before etale sheaf',r'\unsure{sheaf} deleted','omitted',r'\unsure{sehaf|sheaf} deleted','The tall h-like stem appears in the third cell, after an e-like second cell; the first s and last a/f forms are crossed heavily. The unusual letter order remains uncertain. (1214,1321,1325,1360), 18×.','low',True,True,'omission')
a('equation 20 label','right-side tag','right-side tag','label at left','The typed (20) precedes the formula at the left prose margin. eq20 (264,1314,1640,1518), 3×.','high',True,True,'insertion or placement')
a('equation 20 base formula','B longmapsto Pic(X completed tensor k B)/underlined D(B))','same','C retained','The left bar and right head, Pic, tensor hat, k, slash, underlined D, B and two closing parentheses are visible. (584,1439,980,1514), 9×.')
a('equation 20 oval addition','inline inserted (Pic(B)+','inline Pic(B)+ with preceding parenthesis treated as live','(Pic(B)+ above D, enclosed in an oval and linked by a descending guide','The opening parenthesis belongs to the raised hand addition. The oval surrounds the whole addition, with an open lower-left tip and a guide descending beside D. (849,1364,1042,1518), 10×, rotated 5 degrees counterclockwise.','high',True,True,'insertion or placement')
a('equation 20 arrow',r'\unsure{\hookrightarrow|\longleftrightarrow}','hookrightarrow','C retained','The right head is clear. The left end has a long upper curved stroke and a short dark lower projection; its return-versus-head shape is not secure enough to remove the doubt. (984,1457,1090,1513), 16×.','low',hc=True,k='misread symbol or index')
a('point below equation 20 arrow','omitted','omitted','point drawn below arrow','A detached oblique dark point lies beneath the middle of the arrow. (1027,1506,1045,1521), 28×.','high',True,True,'drawing or diagram')
a('two points at right of equation 20','omitted','omitted','two oblique points drawn','Two dark points lie well to the right of the formula; the right one is higher. (1525,1493,1549,1520), 24×.','high',True,True,'drawing or diagram')
a('twisted group and obstruction prose','where underlined D ... first hand side ... successive obstructions','same','C retained','Every word, both Q(B) expressions and underlined D were checked in end (246,1523,1668,2011), 3×; first hand side is retained.')
a('first obstruction group','H-1(Spec(B),underlined D)','same','C retained','The raised one-stroke numeral with foot, nested parentheses, comma and independent underline below D are visible. (1076,1659,1345,1722), 10×.')
a('first for instance placement','inline before if','same','above if with guide','The hand words sit above if; the left descending curve and long right arm with an upward tip are visible. (245,1712,481,1790), 9×, rotated 1 degree clockwise.','high',True,True,'insertion or placement')
a('second for instance placement','inline before if','same','above if with guide','The hand words sit above the second if; the guide descends immediately before i and ends in an upward curve to the right. (1176,1774,1419,1861), 9×, rotated 1 degree clockwise.','high',True,True,'insertion or placement')
a('first X subscript','X-o','X-0','C retained','The lowered rounded character has the short body of the typed lower-case o, rather than the taller zero. (1291,1814,1351,1874), 18×.',hc=True,k='misread symbol or index')
a('word after first X-o','has','has',r'\unsure{hes|has}','The middle cell has a conspicuous upper loop, middle stroke and open lower-right e-like form; a small lower-right foot leaves an a-like alternative. No order of possible overprinting is inferred. (1360,1817,1452,1860), 22×.','low',True,True,'misread word')
a('zero-cycle at edge','zero-cycle','same','C retained','The hyphen is distinct; the final e is clipped at the dark edge but its left curve and middle trace remain. (1460,1814,1673,1858), 12×.','medium')
a('second X subscript','X-o','X-0','C retained','The final lowered character again has the short rounded o body. (1485,1957,1545,2012), 18×.',hc=True,k='misread symbol or index')
a('closing prose','separably closed ... B normal ... Brauer group ... degree 1 ... Assume for simplicity ...','same','C retained','The words, parentheses, plain B, numeral 1 and unfinished final sentence were read line by line in end, 3×.')
d['unresolved']='The cancelled Consider expression and its lower cells; the cancelled arrow before P(B) in (19); the crowded opening parenthesis of the inline added Pic(B); the vowel in beleng/belang/belong; the final parenthesis of old Q(B); the old word sehaf/sheaf; the left end of the arrow in (20); and hes/has remain uncertain. No chronological order is asserted for overlaid letter forms. Detached points and the extra x-shaped overstrike are reproduced without assigning a meaning.'
d['inventory']=[
 ['text','opening continuation','on the other hand ... locally of finite presentation ...'],
 ['insertion','initial cell of filtering','overlaid d and f','typewriter'],
 ['text','restriction and noetherian arguments','direct limits ... restriction ... finite type ... a fortiori'],
 ['deletion','before noetherian','are'],
 ['insertion','above arguments','(i.e. noetherian)','his hand'],
 ['drawing','beneath noetherian addition','curved left entry and long right arm with upturned end','his hand'],
 ['text','existence theorem and affine argument','using the existence theorem ... Assume for simplicity ...'],
 ['deletion','before Assume','namely'],
 ['drawing','after cancelled namely','additional x-shaped overstrike','typewriter'],
 ['display','ring definition','C=A completed tensor k B=lim A-n tensor k B,'],
 ['insertion','two products in ring definition','enclosing ovals and first hat','his hand'],
 ['text','adic ring paragraph','which is an adic noetherian ring ... Consider ...'],
 ['deletion','after Consider','uncertain X/Y and lowered T/B forms'],
 ['insertion','above cancelled expression and equals','X completed tensor k B','his hand'],
 ['drawing','under new left expression','long insertion guide descending before equals','his hand'],
 ['text','right equality and conclusion','equals X tensor A C, which is a proper scheme over C. We then have'],
 ['insertion','right equality product','oval around typed x','his hand'],
 ['deletion','interline above which','equals X completed tensor k B'],
 ['display','equation 19, label at left','Pic(X completed tensor k B) wave-over-right-arrow lim-n Pic(X-nB), ...'],
 ['insertion','first product in equation 19','oval and hat','his hand'],
 ['insertion','first relation in equation 19','wave and right arrow','his hand'],
 ['insertion','below lim in equation 19','left arrow and n','his hand'],
 ['deletion','after comma in equation 19','uncertain right arrow P(B)'],
 ['insertion','right side of equation 19','Pic(X completed tensor k B)/Pic(B) hooked arrow P(B)','his hand'],
 ['text','sheafification paragraph','and thus on noetherian arguments B, P appears ...'],
 ['insertion','first cell of on','overlaid P and o','typewriter'],
 ['drawing','under noetherian','underline','his hand'],
 ['insertion','inline functor expression','mapsto, oval, hat and slash Pic(B)','his hand'],
 ['insertion','above this','which is a separated presheaf,','his hand'],
 ['drawing','under separated','short underline','his hand'],
 ['drawing','beneath whole separated clause','long guide with descending left side and upturned right end','his hand'],
 ['text','obstruction conclusion for P','this statement being complemented ... group fcr obstructions ...'],
 ['insertion','last product in P paragraph','oval and hat','his hand'],
 ['text','Q paragraph','As for ... B mapsto Q(B), this appears ...'],
 ['deletion','after As for','Q(B and uncertain closing parenthesis'],
 ['insertion','B to Q(B)','mapsto','his hand'],
 ['deletion','before etale sheaf','uncertain sehaf/sheaf'],
 ['text','introduction to equation 20','etale sheaf associated with the functor'],
 ['display','equation 20, label at left','B longmapsto Pic(X completed tensor k B)/D(B)) (uncertain arrow Q(B))'],
 ['insertion','equation 20 first arrow and product','longmapsto, oval and hat','his hand'],
 ['insertion','above D in equation 20','(Pic(B)+','his hand'],
 ['drawing','around equation 20 addition','oval with lower-left opening and descending guide','his hand'],
 ['insertion','parenthetical relation in equation 20','uncertain hooked or two-headed arrow','his hand'],
 ['drawing','below equation 20 arrow','detached oblique point','another unnamed hand'],
 ['drawing','far right of equation 20','two oblique points','another unnamed hand'],
 ['text','two obstructions','where D is the twisted constant group ... H-1(Spec(B),D) ...'],
 ['insertion','above first if','for instance','his hand'],
 ['drawing','beneath first for instance','curved insertion guide','his hand'],
 ['text','constant group and Brauer obstruction','D is constant ... B normal ... Brauer group ...'],
 ['insertion','above second if','for instance','his hand'],
 ['drawing','beneath second for instance','curved insertion guide','his hand'],
 ['text','zero-cycle criterion','if X-o hes/has a zero-cycle of degree 1.'],
 ['text','last unfinished sentence','Assume for simplicity that the irreducible components of X-o are'],
 ]
rv['commit'](d)
