from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
def above(word,ins,shift='-2em'):
 return r'\tikz[baseline=(s.base)]{\node[inner sep=1pt](s){'+word+r'};\node[anchor=south west,inner sep=1pt](a) at ([xshift='+shift+r',yshift=7pt]s.north west){'+ins+r'};\draw ([xshift=-4pt,yshift=-3pt]s.south west) to[out=90,in=-90] ([xshift=-4pt,yshift=-2pt]s.north west);\draw ([xshift=-3pt,yshift=5pt]a.south west) to[out=210,in=180] ([xshift=-4pt,yshift=-2pt]s.north west) to[out=0,in=180] ([xshift=1pt,yshift=-2pt]a.south east) to[out=0,in=-90] ([xshift=3pt,yshift=4pt]a.south east);}'
L=r'\mathord{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$J/J^2$};\node[anchor=south east,inner sep=1pt](a) at ([xshift=0pt,yshift=8pt]s.north west){$\inserted{\underline{L}=}$};\draw ([xshift=-4pt,yshift=-3pt]s.south west) to[out=90,in=0] ([xshift=-1pt,yshift=-2pt]a.south west) to[out=180,in=-90] ([xshift=-4pt,yshift=4pt]a.south west);\draw ([xshift=-4pt,yshift=-3pt]s.south west)--([xshift=9pt,yshift=16pt]s.north west);}}'
start=r'\tikz[baseline=(s.base)]{\node[inner sep=1pt](s){,};\node[anchor=south west,inner sep=1pt](a) at ([xshift=-3em,yshift=9pt]s.north west){\inserted{\handwritten{from the start}}};\draw ([xshift=-2pt,yshift=-4pt]s.south west) to[out=90,in=180] ([xshift=1pt,yshift=-2pt]a.south east) to[out=0,in=-90] ([xshift=3pt,yshift=4pt]a.south east);}'
tensor=r'\mathord{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\scriptstyle\mathrm{x}$};\draw[line width=.4pt] ([xshift=.7pt,yshift=1.2pt]s.center) ellipse[x radius=1.8pt,y radius=3.1pt];}}'
dots=r'\tikz[baseline=-.3ex,x=1em,y=1em]{\fill (.12,-.15) circle (.3pt);\fill (.24,0) circle (.3pt);}'
arrow=r'\mathrel{\tikz[baseline=-.3ex,x=1em,y=1em]{\draw[line width=.5pt] (0,0)--(1.5,0)--(1.32,.10) (1.5,0)--(1.32,-.13);\fill (1.22,-.15) circle (.35pt);}}'
slash=r'\mathord{\tikz[baseline=-.25ex,x=1em,y=1em]{\draw[line width=.7pt] (0,-.05)--(.32,.72);\fill (.13,.45) ellipse[x radius=.06em,y radius=.08em];\fill (.14,.18) ellipse[x radius=.06em,y radius=.08em];}}'
ghost=r'\tikz[baseline=(c.base)]{\node[anchor=base west,inner sep=0pt](c){closed;};\node[anchor=base west,inner sep=0pt](b) at ([xshift=.4em]c.base east){b\rlap{y}ut};\node[anchor=base west,inner sep=0pt](t) at ([xshift=.4em]b.base east){then};\node[anchor=base west,inner sep=0pt](w) at ([xshift=.8em]t.base east){we};\draw[gray,line width=.25pt] ([xshift=-1.8em,yshift=.8em]c.west)--([xshift=-.4em,yshift=-.8em]c.west) to[out=-5,in=185] ([yshift=-.6em]b.south) to[out=5,in=180] ([xshift=-.2em]t.west);\draw[line width=.35pt] ([xshift=-.2em,yshift=.1em]t.east) to[out=-60,in=165] ([xshift=-.1em,yshift=-.1em]w.west);}'
d={'cote':57,'scan':7,'sheet_kind':'typescript','hand':'typewriter','replace':[
 (r'R^{\handwritten{\unsure{4|1}}}',r'R^{\mathord{\rlap{$1$}\handwritten{\unsure{4|1}}}}'),
 (r'f_{\handwritten{*}}',r'f_{\handwritten{\unsure{*|k}}}'),
 (r'\unsure{it} seems','it seems'),
 (r'\deleted{get}',r'\deleted{\unsure{get|gei}}'),
 (r'\inserted{invertible} ideal',above('ideal',r'\inserted{invertible}','-4em')),
 (r'\inserted{\underline{L}=}J/J^2',L),
 (r'\deleted{group}\handwritten{object}',r'\rlap{\deleted{group}}\handwritten{object}'),
 (r'\unsure{\mathbb{P}|P}',r'\unsure{P|\mathbb{P}}'),
 (r'\deleted{\unsure{are h|are}}',r'\deleted{are \unsure{h|b}}'),
 (r'\handwritten{\otimes}',tensor),
 (r'\inserted{\handwritten{from the start}},',start),
 ('\n\n'+r'\unsure{Thhs|Thus}', '\n\n'+r'\unsure{This|Thus|Thhs}'),
 ('accurately, the','accurately, '+dots+' the'),
 (r'\unsure{xase|case}',r'\rlap{x}case'),
 ('closed; but then we',ghost),
 ('closed from the start',r'closed \rlap{g}from the start'),
 (r'\inserted{\handwritten{which we will do}}.',above('.',r'\inserted{\handwritten{which we will do}}','-2em')),
 (r'\deleted{\unsure{s}}',r'\deleted{\unsure{s|e}}'),
 (r'D\handwritten{\longrightarrow}\operatorname{NS}',r'D'+arrow+r'\operatorname{NS}'),
 (r'\underline{\operatorname{NS}}_{X_o/k}',r'\underline{\operatorname{NS}}_{X_o'+slash+'k}'),
 (r'^{\unsure{o|0}}','^o'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole sheet and both halves before C and H, then read seven broad 3× crops line by line. Thirty-eight focused crops at 6–18× and seven supplemental crops at 7–18× covered all C doubts, H differences, type overprints, cancellations, added guides, formula details and detached marks. The overlaid object was rotated 2 degrees counterclockwise; from the start was rotated 2 degrees clockwise and which we will do 1 degree clockwise for upright reading. The last word of a supplemental crop fell outside the intended overprint, so no reading was inferred from that misplaced supplement. No OCR, delegated reading, context or compilation was used.'}
c=(rv['WIT']/rv['row'](57,7)['codex_file']).read_text()
for n,tag in [(11,r'\tag*{(11)}'),(12,r'\tag*{\handwritten{(12)}}')]:
 pos=c.index(tag);i=c.rfind('\\[',0,pos);j=c.index('\\]',pos)+2
 block=c[i:j];inner=block[2:block.index(tag)].strip();current=block
 for old,new in d['replace']:
  inner=inner.replace(old,new);current=current.replace(old,new)
 label='('+str(n)+')' if n==11 else r'\handwritten{(12)}'
 d['replace'].append((current,'\\[\n\\begin{aligned}\n'+label+r'\qquad\qquad & '+inner+'\n\\end{aligned}\n\\]'))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('equation 11 structure-sheaf symbol','underlined O','calligraphic O','C retained','A plain upright O has an independent lower bar and lowered X. (681,176,1021,248), 7×.',hc=True,k='misread symbol or index')
a('equation 11 remaining marks','underlined Lie(P), simeq, H-1 and point','same','C retained','Lie alone has a separate underline; the handwritten relation has an upper wave and lower line. The raised 1, parentheses, comma and final point are all visible. Same focused crop and top (264,173,1647,400), 3×.')
a('equation 11 label','right-side tag','right-side tag','typed (11) at left','The label is beside the left prose margin, before the centered formula. Top crop, 3×.','high',True,True,'insertion or placement')
a('overwritten R exponent',r'\handwritten{\unsure{4|1}}','1','typed 1 beneath handwritten unsure 4/1','A straight type stem and lower horizontal serif remain under a dark handwritten angled top and retraced right stem. The added form may be 4 or 1; the underlying type form is also retained. (329,238,420,314), 12×.','low',True,True,'misread symbol or index')
a('subscript of f','handwritten star','star',r'\handwritten{\unsure{*|k}}','The added mark has a long upright stem and two unequal right branches. It can be a compressed star or a k-like form; enlargement does not separate those readings. Same R/f crop, 12×.','low',True,True,'misread symbol or index')
a('O in direct-image expression','underlined O','calligraphic O','C retained','A separate bar lies beneath a plain O; the X is lower. (414,253,490,311), 12×.',hc=True,k='misread symbol or index')
a('punctuation after direct-image expression',r'\unsure{;}','omitted','C retained','Two dark bodies joined by a thin bent trace occupy a separate position after the parenthesis. The lower body has a tail. Semicolon remains plausible but is not securely resolved. (487,265,512,304), 18×.','low',hc=True,k='omission')
a('coherence and finite-dimensionality sentence','coherent and concentrated at the origin; sections H-1; finite dimension','same apart from O','C retained','Every word and all punctuation are typed. The section formula has a clear raised 1 and full parentheses. Top crop, 3×; (798,317,975,386), 10×.')
a('O in section formula','underlined O','calligraphic O','C retained','The plain O again has its own independent lower bar and lowered X. Same section-formula crop, 10×.',hc=True,k='misread symbol or index')
a('it before seems',r'\unsure{it}','it','it','The dot and stem of i and the separate taller t stem, crossbar and right-curved foot are visible, although closely spaced. (268,399,302,438), 18×.','high',True,False,'misread word')
a('deleted word before replacing','get','omitted',r'\unsure{get|gei} deleted','The g descender and e body survive the x strikes. The last letter has a separated round upper mark, leaving t/i uncertain under the overstrike. (934,405,1007,444), 14×.','low',True,True,'omission')
a('snitable/suitable',r'\unsure{snitable|suitable}','suitable','C retained','The first two type positions are congested: an s-like double curve and angular strokes precede a closed n/u-like body. The following itable is clear. (267,467,435,509), 12×.','low',hc=True,k='misread word')
a('dmminating/dominating',r'\unsure{dmminating|dominating}','dominating','C retained','The first d and final nating are legible; the intervening round, arched and dotted strokes overlap heavily. The two candidate words cannot be cleanly separated. (562,468,772,511), 10×; (561,469,646,509), 16×.','low',hc=True,k='misread word')
a('invertible insertion','inline insertion before ideal','same','typed invertible above ideal, with central insertion guide','All letters are typed. The guide curls up at both ends beneath invertible and descends between an and ideal from a central junction. (1381,441,1652,520), 8×.','high',True,True,'insertion or placement')
a('deleted having','having deleted','omitted','C retained','The h ascender, a bowl, v, i dot, n arch and g descender remain beneath x overstrikes. (424,537,555,584), 12×.',hc=True,k='omission')
a('support X subscript','o','0','C retained','The lowered character has the short round o body used elsewhere on this sheet, unlike the taller zero after the cohomology equality. Claim (262,400,1675,668), 3×; zero in (263,943,606,1018), 8×.',hc=True,k='misread symbol or index')
a('L insertion and guide','underlined L= inline','same','underlined L= above before J/J-2, with two-arm guide','The L has one independent underline, and equality has two bars. A curved left branch passes below the addition to the entry point, while a long oblique right branch rises beside J. (481,575,629,654), 10×.','high',True,True,'drawing or diagram')
a('ample-sheaf emphasis','ample sheaf on underlined','ample sheaf on Z emphasized','C retained','The line ends under on, well before the separate Z. (742,608,1113,672), 7×.',hc=True,k='insertion or placement')
a('replacement systems','(X-n) lower handwritten n; (Z-n=V(J power n+1)) lower handwritten n','same','C retained','Both handwritten indices have matching down-up-return strokes. All typed n, plus, 1, V, J and closing parentheses are visible. (583,678,684,743), 10×; (950,674,1250,750), 8×.')
a('deleted the','the deleted','omitted','C retained','The t upper stem, h ascender and e bowl survive typed x marks. (1535,692,1611,728), 14×.',hc=True,k='omission')
a('deleted same',r'\unsure{same}','omitted','C retained','The first letter is largely masked by an x; a faint curved left remnant supports s. The following a, m and e are clearer. (269,753,354,791), 14×.','low',hc=True,k='omission')
a('group/object correction','deleted group then handwritten object','same','handwritten object over deleted group','The old g descender and final p stem/foot remain underneath the handwritten o-b-j-e-c-t. The words occupy the same position rather than consecutive positions. (718,737,832,801), 12×, rotated 2 degrees counterclockwise.','high',True,True,'insertion or placement')
a('P of Picard',r'\unsure{\mathbb{P}|P}','P',r'\unsure{P|\mathbb{P}}','A serifed P bowl and stem are clear, but the dark retracing does not securely establish a doubled alphabet. Plain P is put first while retaining the alternative. (891,749,920,797), 18×.','low',True,False,'misread symbol or index')
a('Picard hyphen spacing','Picard -schemes','Picard-schemes','C retained','There is a visible gap before the typed hyphen, with no comparable gap after it. Systems (262,670,1675,955), 3×.',hc=True,k='other')
a('P-prime definition','P-prime sub n = underlined Pic sub Z-n/k','same','C retained','The prime is separate, and the underline belongs to Pic; Z and its further lowered n, slash and k are visible. Systems crop, 3×.')
a('deleted words before transition terms',r'\unsure{are h|are}','omitted',r'are \unsure{h|b} deleted','The letters a-r-e are visible under x strokes. After a crossed space is a further tall ascender with a low right body; it can be h or b but is not absent. (461,888,570,934), 14×.','low',True,True,'omission')
a('transition-map gap','blank between P-prime n+1 and P-prime n','arrow','C retained','The intervening paper is blank: no shaft or head is present. Both primes and the n+1 and n subscripts are complete. (596,890,788,951), 10×.',hc=True,k='text not on the page',m='yes',q='H supplies a transition arrow from P-prime n+1 to P-prime n; no arrow is written in the scan.')
a('isomorphisms emphasis','isomorphisms underlined','same emphasis','C retained','A separate hand-drawn line runs below the word and ends before the opening parenthesis. Systems crop, 3×.')
a('first cohomology L','plain L','underlined L','C retained','The first L has only its printed foot, with no separate bar below. (1337,884,1599,953), 9×.',hc=True,k='misread symbol or index',q='In the vanishing statement the first L is not underlined; the second L is underlined. H underlines both.')
a('second cohomology L','underlined L','same','C retained','A separate lower bar is clearly distinct from the foot of the second L. (263,943,606,1018), 8×.')
a('tensor signs','handwritten tensor sign before each n','tensor sign before each n','typed x with an added oval reproduced in each exponent','Each exponent contains a serifed typed x and an added oval extending above it, before a separate typed n. The literal drawing preserves both layers without changing the tensor-sign reading. (1498,882,1533,925) and (405,948,440,988), 18×.')
a('cohomology exponents and equality','H-1 and H-2; Z-o; equals zero','same except Z-zero','C retained','The cohomology degrees are clear 1 and 2. The two lowered Z indices are short round o, unlike the full-height oval zero after equality. Both parentheses, comma and final point are visible. Both cohomology crops, 8–9×.',hc=True,k='misread symbol or index')
a('first Thhs/Thus',r'\unsure{Thhs|Thus}','Thus','C retained','The third type position contains heavy overlapping upright, arched and lower curved strokes; its precise letter is not isolated. T, h and final s are clear. (620,962,705,1005), 14×.','low',hc=True,k='misread word')
a('from the start addition','inline insertion before comma','same','handwritten words above the comma, with curved guide','All four words are legible on the upright crop. A stem rises through the comma position, curves right beneath the words, and turns up at the far end. (1436,939,1655,1025), 10×, rotated 2 degrees clockwise.','high',True,True,'drawing or diagram')
a('essentially constant conclusion','pro-group (P-n); inverse limit P; group scheme locally of finite type','same','C retained','Every word, parenthesis and comma was read in the constant crop (258,945,1675,1378), 3×. No extra hypothesis is inserted into this sentence.')
a('finite-type emphasis','group scheme locally of finite type over underlined','includes k in emphasis','C retained','The underline is confined to the line ending over. The k on the next line has no underline. Constant crop, 3×.',hc=True,k='insertion or placement')
a('surface case','dim A=2, A normal; negative definiteness; components of X-o','same except zero subscript','C retained','The number 2, both commas, each word of the intersection-matrix clause and the final point are clear. The last X again has a short round lowered o. Constant crop, 3×.',hc=True,k='misread symbol or index')
a('second Thhs/Thus',r'\unsure{Thhs|Thus}','This',r'\unsure{This|Thus|Thhs}','The third position has a distinct upper i-like point together with a dark arched body. This is put first, but Thus and the literal h-like reading remain possible under the overprint. (378,1387,467,1431), 14×.','low',True,True,'misread word')
a('definability and morphism paragraph','P definable; morphism (5); morphisme','same','C retained','The words and parenthesized (5) are typed, including the final e of morphisme. Morph crop (255,1380,1665,1720), 3×.')
a('two points after accurately comma','omitted','omitted','two detached oblique points drawn','After the typed comma are two smaller points, the right one above the left one. They are separate from the comma and following t. (1457,1463,1510,1510), 14×.','high',True,True,'drawing or diagram')
a('D-to-P morphism','underlined D with handwritten right arrow to P','same','C retained','The D has a separate lower bar. The handwritten arrow has a shaft and a pointed right head; P is plain. Morph crop, 3×.')
a('case first letter',r'\unsure{xase|case}','case','x/c overprint followed by ase','An x with intersecting diagonals and serifs coexists with a rounded c body open at the right. Both are retained without a correction order. (1138,1539,1229,1574), 14×.','high',True,True,'misread word')
a('but middle letter','but','but','b, y/u overprint, t','The middle cell has the two upright sides and lower return of u, plus a separate descending y branch/loop. (417,1601,489,1644), 14×.','high',True,True,'misread word')
a('from first letter','from','from','g/f overprint followed by rom','The first cell contains the upper f loop and crossbar as well as a g lower bowl/descender. (1396,1606,1485,1654), 14×.','high',True,True,'misread word')
a('faint lower-paragraph marks','omitted','omitted','faint bent line and short darker curve reproduced','A faint line descends at the left of closed, passes below closed and but, then rises toward then. A separate darker short curve leaves the end of then toward we. No deletion or punctuation meaning is assigned. (205,1580,636,1648), 7×.','high',True,True,'drawing or diagram')
a('which we will do insertion','inline after handwritten comma','same','handwritten words above the point after start, with guide','The words which we will do are legible; the upper mark within will is the i point. The guide curls up at both ends and has a downward branch between the comma and the typed point. (317,1628,688,1675), 8×, rotated 1 degree clockwise; (365,1666,485,1717), 12×.','high',True,True,'insertion or placement')
a('punctuation before closing parenthesis','point before closing parenthesis, then point','only closing parenthesis and following point','C retained','A separate round point is visibly typed before the closing parenthesis, and another follows it. The added comma is to their left. Same punctuation crop, 12×.',hc=True,k='omission')
a('closed-immersion wish','We would be particularly happy ... or what amounts to the same','same','C retained','All words and commas are legible and were checked through the line before equation (12). Morph and end (253,1730,1670,1970) crops, 3×.')
a('deleted final letter of morphisms',r'\unsure{s}','omitted',r'\unsure{s|e} deleted','The last type position is x-overstruck; curved and bar-like remnants support s or e but do not distinguish them securely. (1331,1752,1364,1789), 18×.','low',True,True,'omission')
a('equation 12 and label','D right arrow NS(X-o), handwritten (12)','same except X-zero','C retained, label moved to left','D is plain, NS upright, and the subscript is short round o. The arrow has a distinct two-arm right head. The handwritten label has a long 1 and a heavily retraced 2, at the left prose margin. (651,1808,915,1876), 10×; (264,1806,321,1857), 16×.','high',True,True,'insertion or placement')
a('point below equation 12 arrow','omitted','omitted','detached point drawn below and left of arrowhead','A small black point is separated from the lower arrowhead arm. Its meaning is not assigned. Equation (12) crop, 10×.','high',True,True,'drawing or diagram')
a('were and NS identity','were; NS(X-o)=underlined NS-X-o/k(k)','same except zeros','C retained apart from the slash detail','Were is typed without h. The two NS forms differ by their underline exactly as in C; all parentheses and the final comma are visible. (652,1884,1367,1957), 6×.',hc=True,k='misread symbol or index')
a('slash detail in NS subscript','plain slash','plain slash','slash with two superposed rounded bodies drawn','Two distinct rounded protrusions are visible along the sloping stroke, one higher on its left and one lower on its right. The drawing retains them without assigning colon or semicolon meaning. (881,1905,956,1958), 14×.','high',True,True,'drawing or diagram')
a('Pic exponent in quotient',r'\unsure{o|0}','0','o','The raised character has a short nearly round lower-case o body, contrasted with the tall zero in the cohomology equality. (1336,1877,1366,1916), 18×; zero crop, 8×.','high',True,True,'misread symbol or index')
a('NS and Pic underlines','underlined NS=underlined Pic / underlined Pic power o','same apart from exponent','C retained','Each of the three operators has its own separate lower line. The slash and equality are clear. NS crop, 6×.')
a('last Picard-scheme formula','P=underlined Pic-Z-n/k','same','C retained','The P, two equality bars, Pic underline and nested Z/n subscripts followed by slash k are clearly typed. Bottom (255,1970,1665,2087), 3×.')
a('large repair','handwritten l and e around typed arg','large','C retained','The first l is a tall handwritten loop; the final e is a handwritten lower curve. The typed a, r and g remain between them. (1309,1962,1403,2010), 14×.')
a('last cancelled Pic','Pic deleted','same','C retained','P, dotted i and c are readable under two gray oblique looped cancellation marks. (260,2018,331,2077), 14×. No continuation is supplied.')
d['unresolved']='The handwritten 4/1 over the typed R exponent; star/k under f; semicolon-like mark after the direct image; deleted get/gei; snitable/suitable; dmminating/dominating; deleted same; P/blackboard P; cancelled h/b after are; both congested Thhs/Thus/This forms; and cancelled s/e after morphism. Overprints are represented without assigning an order. Detached points, the slash protrusions and the faint lower-paragraph lines are reproduced without semantic interpretation.'
d['inventory']=[
 ['display','top, equation 11','underlined Lie(P) simeq H-1(X,underlined O-X).'],
 ['insertion','equation 11 relation','handwritten simeq','his hand'],
 ['text','first prose sentence','As R ... coherent ... finite dimension. In fact,'],
 ['insertion','R exponent','handwritten 4/1 over typed 1','his hand'],
 ['insertion','f subscript','star/k uncertain','his hand'],
 ['text','after first direct-image expression','semicolon-like mark uncertain'],
 ['text','following clause','it seems, with a little care ... suitable/dmminating ... ideal J'],
 ['deletion','before replacing','get/gei uncertain'],
 ['insertion','above ideal','invertible'],
 ['drawing','invertible insertion','curved guide with central downward branch','his hand'],
 ['deletion','after J on X comma','having'],
 ['text','subscheme sentence','defining a subscheme Z ... same support as X-o ...'],
 ['insertion','above J/J-2','underlined L='],
 ['drawing','L insertion','curved left branch and long oblique right branch','his hand'],
 ['drawing','under ample sheaf on','underline ending before Z','his hand'],
 ['text','system replacement clause','replacing the system (X-n) ... (Z-n=V(J power n+1)) ...'],
 ['insertion','after first system parenthesis','lower n','his hand'],
 ['insertion','after second system parenthesis','lower n','his hand'],
 ['deletion','after defines','the'],
 ['deletion','start of next line','same uncertain'],
 ['deletion','after pro-','group beneath object'],
 ['insertion','over group','object','his hand'],
 ['text','following inverse-system definition','Picard -schemes ... P-prime n=underlined Pic-Z-n/k ...'],
 ['deletion','before P-prime n+1','are h/b'],
 ['drawing','under isomorphisms','underline','his hand'],
 ['text','parenthetic vanishing statement','H-1(Z-o,L tensor n)=H-2(Z-o,underlined L tensor n)=0'],
 ['insertion','first cohomology exponent','oval added over typed x','his hand'],
 ['insertion','second cohomology exponent','oval added over typed x','his hand'],
 ['text','conclusion following vanishing','Thhs/Thus it seems ... assumptions made ... inverse limit ...'],
 ['insertion','above comma after made','from the start','his hand'],
 ['drawing','from the start addition','curved insertion guide','his hand'],
 ['drawing','under finite-type conclusion','underline ending after over','his hand'],
 ['text','surface-case sentence','This is certainly so ... negative definiteness ... components of X-o.'],
 ['text','next paragraph opening','This/Thus/Thhs P seems ... morphism (5) ... morphisme'],
 ['drawing','after accurately comma','two detached oblique points','another unnamed hand'],
 ['insertion','between underlined D and P','right arrow','his hand'],
 ['text','case after descent phrase','x/c overprint'],
 ['text','but','y/u overprint'],
 ['text','from the start','g/f overprint'],
 ['drawing','around closed; but then we','faint bent line and short darker curve','another unnamed hand'],
 ['insertion','after start','comma','his hand'],
 ['insertion','above point before closing parenthesis','which we will do','his hand'],
 ['drawing','which we will do addition','long guide with downward branch','his hand'],
 ['text','closed-immersion wish','We would be particularly happy ... if the morphism'],
 ['deletion','end of morphisms','s/e uncertain'],
 ['display','equation 12','D right arrow NS(X-o)'],
 ['insertion','equation 12','handwritten label (12) and right arrow','his hand'],
 ['drawing','below equation 12 arrowhead','detached point','another unnamed hand'],
 ['text','following identity','is injective, were NS(X-o)=underlined NS-X-o/k(k), NS=Pic/Pic power o.'],
 ['drawing','NS subscript slash','slash with two rounded superposed bodies'],
 ['text','last parenthetic statement','The equivalence comes ... P=Pic-Z-n/k for some large n, and that'],
 ['insertion','first and last letters of large','handwritten l and e','his hand'],
 ['deletion','last line','Pic'],
 ['text','bottom left','6 (archive sheet number; retained as comment)','another hand'],
]
rv['commit'](d)
