from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
def above(word,ins):
 return r'\tikz[baseline=(s.base)]{\node[inner sep=1pt](s){'+word+r'};\node[anchor=south west,inner sep=1pt](a) at ([xshift=1pt,yshift=7pt]s.north west){'+ins+r'};\draw ([xshift=-5pt,yshift=-3pt]s.south west) to[out=90,in=190] ([xshift=1pt,yshift=-2pt]a.south west)--([xshift=1pt,yshift=-2pt]a.south east) to[out=0,in=-90] ([xshift=3pt,yshift=4pt]a.south east);}'
overpq=r'\mathord{\rlap{$\deleted{P}$}\handwritten{Q}}'
qp=r'\unsure{\mathord{\rlap{$P$}Q}|\mathbb{Q}}'
anddot=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){and};\fill ([xshift=0pt,yshift=3pt]s.north) circle (.35pt);}'
dots=r'\tikz[baseline=-.3ex,x=1em,y=1em]{\fill (.12,-.35) circle (.35pt);\fill (.23,-.20) circle (.35pt);}'
d={'cote':57,'scan':5,'sheet_kind':'typescript','hand':'typewriter','replace':[
 (r'H^{\unsure{o|0}}',r'H^o'),
 (r'fi\unsure{el|le}d',r'fi\rlap{l}e\rlap{e}ld'),
 (r'\deleted{\unsure{of}}',r'\deleted{of}'),
 (r'\inserted{\handwritten{then}} $k\prime=k$',r'UNUSED'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole sheet and both halves before C and H, then read six broad crops at 3–4× line by line. Twenty-five focused crops at 5–16× and seven supplemental crops at 2–18× covered every C doubt, difference, cancellation, formula exponent, overwritten letter and added guide; three supplemental views located and examined two detached ink points. The then insertion was rotated 2 degrees clockwise to an upright baseline. Other type and additions were horizontal. The short round cohomology exponent was compared directly with the taller zero in the typed equation label. All agreed prose was read, including it\'s, separable closed, termes, and makes a sense. No OCR, delegated reading, context or compilation was used.'}
# Replace the actual apostrophe-bearing expression, preserving its guide and attachment.
d['replace'].pop()
d['replace'] += [
 ("\\inserted{\\handwritten{then}} $k'=k$",above("$k'=k$",r'\inserted{\handwritten{then}}')),
 (r'\unsure{\mathbb{Q}|Q}',r'\unsure{Q|\mathbb{Q}}'),
 (r'\deleted{\unsure{P}}\handwritten{Q}',overpq),
 (r'\inserted{Galois} descent',above('descent',r'\inserted{Galois}')),
 (r'\unsure{A\prime|A(}',r'UNUSED'),
]
d['replace'].pop()
d['replace'] += [
 (r"\unsure{A'|A(}",r"A\mathord{\rlap{${}'$}(}"),
 (r'$, and if',r'$, '+anddot+' if'),
 (r'\deleted{\operatorname{Pic}}\mathbb{Q}(k)',r'\deleted{\operatorname{Pic}}'+qp+'(k)'),
 (r'\unsure{This is perf}','This is perf'),
 (r'for instance (5) injective,}',r'for instance (5)\,'+dots+r' injective\unsure{,|.}}'),
 (r'\unsure{the|ahe}',r'\rlap{a}the'),
]
c=(rv['WIT']/rv['row'](57,5)['codex_file']).read_text()
for n in (9,10):
 tag='\\tag*{('+str(n)+')}'
 pos=c.index(tag);start=c.rfind('\\[',0,pos);end=c.index('\\]',pos)+2
 block=c[start:end];inner=block[2:block.index(tag)].strip();current=block
 for old,new in d['replace']:
  inner=inner.replace(old,new);current=current.replace(old,new)
 d['replace'].append((current,'\\[\n\\begin{aligned}\n('+str(n)+')\\qquad\\qquad & '+inner+'\n\\end{aligned}\n\\]'))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('first H exponent',r'\unsure{o|0}','0','o','The raised body is a short nearly round lower-case o, distinctly shorter than the full-height oval zero in label (10). The same short type body recurs in both later cohomology expressions. (740,181,939,261), 9×; zero (306,1394,329,1427), 14×.','high',True,True,'misread symbol or index')
a('first structure-sheaf symbol','underlined O','calligraphic O','C retained','The O is a plain upright oval with a separate horizontal line below; the subscript is X with a further lower n. Same first-H crop.',hc=True,k='misread symbol or index')
a('first sentence and connectedness','B-n=H-o(X-n,O-X-n); U hence X hence X-n','same apart from noted symbols','C retained','The B and n, equality, comma, all nested subscripts and closing parenthesis are visible. The next clause explicitly has U hence X hence X-n, and the apostrophe in it\'s is present. Top (268,182,1668,442), 3×.')
a('deleted thus','thus deleted','omitted','C retained','The t cross/stem, h ascender/arch, u bottom and s curved remnants survive beneath four typed x overstrikes. (1425,333,1514,374), 12×.',hc=True,k='omission')
a('first limit','P(k)=lim P-n(k)','same','C retained','This first lim has neither a lower index nor an arrow. Both P letters, lower n, parentheses, equality and following comma are clearly typed. Top crop, 3×.')
a('deleted letter inside various',r'vari\deleted{\unsure{e}}ous','various','C retained','A separate type position between i and o is overstruck by x. Curved interior remnants support e, but the body and opening are heavily masked. (1093,409,1152,442), 14×.','low',hc=True,k='omission')
a('overtyped middle of field',r'fi\unsure{el|le}d','field','fi followed by e/l overlays in both positions, then d','Each of the two positions has a tall serifed l-like stem and a lower e-like curved body with a middle bar. Both are represented in overlay; no order of overtyping is assigned. (274,538,373,579), 12×.','high',True,True,'misread word')
a('intersection and index','k-prime equals cap-n k-n','same','C retained','The handwritten intersection has two long sides joined by an upper arch. Beneath it is an n-like up-and-down return, matching the index under the later limit. Both typed primes/subscripts are separate. (448,526,487,599), 12×; upper (267,468,1664,718), 3×.')
a('second H exponent','o','0','C retained','The raised round letter repeats the short lower-case o of the first expression; it is shorter than the typed zero comparison. (797,534,960,587), 10×.',hc=True,k='misread symbol or index')
a('second structure-sheaf symbol','underlined O-X','calligraphic O-X','C retained','A plain upright O has a separate lower bar; its subscript X has no n in this occurrence. Same crop.',hc=True,k='misread symbol or index')
a('second limit','left arrow below lim; n below arrow','projective-limit notation','C retained','A horizontal shaft has a distinct pointed left head with two unequal arms. The n is on a lower level, clear of the arrow. (1012,543,1089,611), 12×.')
a('third H exponent','o','0','C retained','The raised o has the same short round body as the preceding two; the X has lower n. (1090,533,1295,613), 9×.',hc=True,k='misread symbol or index')
a('third structure-sheaf symbol','underlined O-X-n','calligraphic O-X-n','C retained','The plain O and independent lower line are visible, followed by X and a further lowered n. Same crop.',hc=True,k='misread symbol or index')
a('deleted of',r'\unsure{of}','of','of deleted','The first old body retains a circular outer left and bottom; the second has a tall hooked f top, stem and crossbar under the x strokes. (1308,548,1356,584), 14×.','medium',True,False,'other')
a('normalisation and normal clause','normalisation of A; normal underlined','same','C retained','All words are visible. An independent line runs beneath normal only, followed by a typed comma. The final Brauer group expression is Br(k) with both parentheses and a point. Upper crop, 3×.')
a('then insertion','then inline before k-prime=k','same','then above k-prime=k with its curved guide','The handwritten t-h-e-n is above the equality. Its guide rises beside the first k, passes below the addition and curls up at the right. (1290,580,1416,665), 10×, rotated 2 degrees clockwise.','high',True,True,'drawing or diagram')
a('Q in defining phrase',r'\unsure{\mathbb{Q}|Q}','Q',r'\unsure{Q|\mathbb{Q}}','The typed Q outer oval, upper serifs and tail are clear. Faint internal strokes do not securely establish a doubled alphabet; Q is put first, retaining the alternative. (936,759,964,795), 16×.','low',True,False,'misread symbol or index')
a('injectivity paragraph','injective homomorphism (6) ... even if (5) ... (6) bijective','same','C retained','Each parenthesized reference and every intervening word are plainly typed. Middle (263,745,1667,1068), 3×.')
a('overtyped is',r'\unsure{is|ss}','is','C retained','The first position has an i-like upper point and stem amid a low curved body; the second is heavily congested, with an s-like lower curve. The alternatives cannot be securely separated. (1267,902,1312,938), 14×.','low',hc=True,k='misread word')
a('separable closed','separable closed','same','C retained','The word ends in e, with no final ly, before the separate closed and full point. Middle crop, 3×.')
a('deleted get','get deleted','omitted','C retained','The g descender, e body and t ascender/cross remain visible under the typed x strikes. (663,969,728,1005), 12×.',hc=True,k='omission')
a('first P beneath Q',r'\deleted{\unsure{P}} followed by Q','Q only','deleted P overlaid by handwritten Q','A serifed vertical stem and upper P bowl remain within the larger handwritten Q outline and descending right tail. The forms occupy the same position. (1243,968,1285,1011), 14×.','high',True,True,'omission')
a('second P beneath Q',r'\deleted{\unsure{P}} followed by Q','Q only','deleted P overlaid by handwritten Q','Again the upper bowl and vertical P stem are visible inside the Q loop, before the separate parenthesis of (k). (1539,968,1585,1016), 14×.','high',True,True,'omission')
a('termes and Galois wording','in termes ... in terms of Galois descent','same','C retained','The first termes has an e before s; the second terms has no e. The added Galois is clearly typed and complete. Middle and display crops, 3×; Galois (1146,1006,1303,1081), 10×.')
a('Galois insertion position and guide','inline insertion before descent','same','typed Galois above descent with handwritten guide','The capitalized word is directly above descent. A curved line rises from beside d, passes below Galois and turns up at its right. Same focused crop.','high',True,True,'drawing or diagram')
a('completion and punctured spectrum','A-prime; U-prime=S-prime-{s-prime}','same','C retained','The primes are separate short marks. Both handwritten braces have pointed middle returns, and the subtraction is one bar. (1462,1106,1548,1157), 10×; display (262,1065,1643,1438), 3×.')
a('Spec argument',r'\unsure{A\prime|A(}','A-prime','A followed by superposed prime and opening parenthesis','A full-height opening curve is visible between A and the final closing parenthesis; a thick short upper stroke occupies the prime position on that curve. Both are reproduced, with no inferred correction sequence. (581,1174,640,1218), 12×.','high',True,True,'misread symbol or index')
a('point above and before if','omitted','omitted','point drawn above the n of and','A separate small black round point lies above the middle of and, not attached to any letter. It is reproduced without assigning punctuation. (676,1163,740,1218), 12×.','high',True,True,'drawing or diagram')
a('equation 9','pi=Gal(bar k/k),','same','C retained','The handwritten pi has a top bar and two descending legs, the right curving outward. A separate bar is above the first k; the slash and unbarred second k are clear. (652,1240,954,1295), 9×.')
a('equation 9 label','right-side tag','right-side tag','typed (9) at left','The typed parenthesized 9 is near the left prose margin, before the centered formula. Display crop, 3×.','high',True,True,'insertion or placement')
a('deleted Pic in equation 10','Pic deleted','omitted','C retained','P stem/bowl, dotted i and c opening remain visible beneath typed x overstrikes, before Q(k). (694,1370,1136,1442), 8×.',hc=True,k='omission')
a('Q form in equation 10','blackboard Q','Q',qp,'The outer Q loop and lower tail enclose a second straight left stem and a separate middle bar meeting the right outline, producing a P-shaped internal structure. A P/Q overlay is put first as a literal candidate, with blackboard Q retained as an alternative; no order of overtyping is assigned. (772,1393,805,1435), 18×.','low',True,True,'misread symbol or index')
a('underlined Pic in equation 10','underlined Pic','plain Pic','C retained','A separate heavy horizontal lies below all three letters of Pic and ends before the opening parenthesis. Equation crop, 8×.',hc=True,k='misread symbol or index',q='Equation (10) has underlined Pic in the image; H omits the underline.')
a('remaining equation 10 marks','simeq, U-prime, superscript pi, comma','same','C retained','The relation has a distinct upper wave and lower bar. The prime is a short upper stroke; pi is above and right of the closing parenthesis and repeats equation (9). The comma has a descending tail. Equation crop, 8×.')
a('equation 10 label','right-side tag','right-side tag','typed (10) at left','The parenthesized 10 is near the left prose margin, before the cancelled Pic and Q(k). Display crop, 3×.','high',True,True,'insertion or placement')
a('cancelled sentence prefix',r'\unsure{This is perf}','This is perfectly true','This is perf','The surviving type is T-h-i-s, space, i-s, space, p-e-r-f; the f has a visible high loop and is followed directly by space and provided. No ectly or true occupies the intervening space. (266,1459,503,1501), 10×; (452,1459,524,1518), 12×.','high',True,True,'text not on the page')
a('cancellation of sentence','whole sentence deleted','same','C retained','The short prefix has typed x overstrikes. A separate long hand-drawn line crosses the entire sentence through its final word; the latter part is retraced. Cancel crop (265,1455,1640,1514), 4×.')
a('cancelled sentence main clause','provided D-prime is torsion free, for instance (5) injective','same','C retained','All letters and the separate prime, comma after free and parenthesized (5) survive the crossing line. There is no hyphen between torsion and free. (507,1459,1633,1517), 5×.')
a('cancelled sentence final punctuation','comma','point',r'\unsure{,|.}','The final mark descends below the baseline, but a heavy turn of the crossing stroke overlaps it. Comma is the first candidate and point remains possible. (1568,1470,1630,1517), 14×.','low',True,True,'other')
a('two points beneath cancelled sentence','omitted','omitted','two oblique detached points drawn below the gap after (5)','Two small dark points lie separately below the baseline, the right one above the left one, in the gap before injective. A full narrow locating strip was followed by (1397,1497,1424,1524), 16×. No sign meaning is inferred.','high',True,True,'drawing or diagram')
a('global Picard paragraph','global underlined; familiar phenomena; Q looks like','same','C retained','Every word and point is visible. An independent underline runs beneath global only. End (261,1524,1653,1995), 3×.')
a('first letter of the',r'\unsure{the|ahe}','the','a and t overlaid, followed by he','A tall t stem and crossbar coexist with the two low bowls of a in the first position; h and e are distinct. Both forms are retained without assigning a correction order. (1558,1616,1623,1647), 14×.','high',True,True,'misread word')
a('deleted Picard before local','Picard deleted','omitted','C retained','The P bowl, dotted i, c opening, a body, r shoulder and d ascender survive the x overstrikes. (854,1677,980,1716), 12×.',hc=True,k='omission')
a('last paragraph','makes a sense ... should check ... choice of','same','C retained','All four lines were read against the enlarged ink. The parenthesized P-n and references (5) and (10), canonical isomorphism, comma and final incomplete phrase choice of are visible; no continuation is supplied. End crop, 3×.')
d['unresolved']='The cancelled e within various; Q / blackboard Q in the defining phrase; is/ss in the congested type; the P/Q overlay versus blackboard Q in equation (10); and the final punctuation of the cancelled sentence. The e/l and a/t overprints and the prime/open-parenthesis overlay are reproduced without claiming their typing order.'
d['inventory']=[
 ['text','opening continuation','of the Artin ring B-n ... residue field k-n.'],
 ['text','following sentence','Of course ... these vari[e deleted]ous obstructions ...'],
 ['deletion','after Of course comma','thus'],
 ['deletion','inside various','e uncertain'],
 ['text','within residue field phrase','two e/l overprinted positions'],
 ['insertion','k-prime definition','handwritten intersection and lower n','his hand'],
 ['insertion','limit in ring formula','left arrow and lower n','his hand'],
 ['deletion','after ring formula','of'],
 ['text','end of first paragraph','which is just the normalisation ... Br(k).'],
 ['insertion','above k-prime=k','then','his hand'],
 ['drawing','then insertion','curved guide','his hand'],
 ['text','second paragraph start','Whatever this be ... separable closed.'],
 ['text','next sentence','Therefore ... describe Q ... in termes ... completion ...'],
 ['deletion','after still','get'],
 ['deletion','first Q after describe','old P beneath Q'],
 ['insertion','first Q after describe','Q over old P','his hand'],
 ['deletion','Q before (k)','old P beneath Q'],
 ['insertion','Q before (k)','Q over old P','his hand'],
 ['insertion','above descent','Galois'],
 ['drawing','Galois insertion','curved guide','his hand'],
 ['insertion','around s-prime','handwritten braces','his hand'],
 ['text','Spec argument','prime and opening-parenthesis overlay after A'],
 ['drawing','above and if','isolated point above n'],
 ['display','equation 9','pi=Gal(bar k/k),'],
 ['insertion','equation 9','pi','his hand'],
 ['text','between equations','we will have an isomorphism'],
 ['display','equation 10','deleted Pic; Q(k) simeq underlined Pic(U-prime) power pi,'],
 ['deletion','start of equation 10','Pic'],
 ['insertion','equation 10','handwritten simeq and pi','his hand'],
 ['deletion','line beneath equation 10','This is perf provided D-prime is torsion free ... injective'],
 ['drawing','below gap after (5) in cancelled line','two detached oblique points','another unnamed hand'],
 ['text','next paragraph','This is perfectly natural ... local Picard scheme.'],
 ['text','first letter of the before natural','a/t overprint'],
 ['deletion','before local Picard scheme','Picard'],
 ['text','last paragraph','To make sure ... does not depend on the choice of'],
 ['text','bottom left','4 (archive sheet number; retained as comment)','another hand'],
]
rv['commit'](d)
