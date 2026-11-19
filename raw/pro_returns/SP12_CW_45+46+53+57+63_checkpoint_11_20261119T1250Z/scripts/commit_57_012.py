from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
tensor=r'\mathord{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\mathrm{x}$};\draw[line width=.5pt] ([xshift=.5pt,yshift=1.3pt]s.center) ellipse[x radius=3pt,y radius=4.5pt];}}'
arrow=r'\mathrel{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\longmapsto$};\draw[line width=.2pt,gray] ([xshift=-1pt,yshift=-1pt]s.east)--([xshift=-8pt,yshift=-22pt]s.west);}}'
points=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){is};\fill ([xshift=-1pt,yshift=5pt]s.north west) circle (.25pt);\fill ([xshift=.5pt,yshift=7pt]s.north west) circle (.25pt);}'
d={'cote':57,'scan':12,'sheet_kind':'typescript','hand':'typewriter','replace':[
 (r'\unsure{tumn|turn}',r't\unsure{\rlap{r}u\rlap{u}r|um|ur}n'),
 (r'\handwritten{\otimes}',tensor),
 (r'\handwritten{\longmapsto}',r'\handwritten{'+arrow+'}'),
 ('sufficient conditions',r'sufficie\unsure{n}% right edge cuts the last visible cell; no final t is visible'+'\n conditions'),
 ('residue field is perfect','residue field '+points+' perfect'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole image, then both halves, then C and H. Six broad 3× crops were read line by line; seventeen focused crops at 10–28× and five supplements at 16–24× covered all C doubts, H differences, mathematical signs, overprints, cancellations, the clipped edge and detached marks. The added signs and numeral were upright; no slanted prose note required rotation. The brown diffuse spot under papers was inspected but had no identifiable written stroke. No OCR, delegated reading, context or compilation was used.'}
c=(rv['WIT']/rv['row'](57,12)['codex_file']).read_text()
for tag,label in [(r'\tag*{(23)}','23'),(r'\tag*{(\unsure{34|24})}',r'\rlap{3}24')]:
 pos=c.index(tag);i=c.rfind('\\[',0,pos);j=c.index('\\]',pos)+2
 block=c[i:j];inner=block[2:block.index(tag)].strip();current=block
 for old,new in d['replace']:
  inner=inner.replace(old,new);current=current.replace(old,new)
 d['replace'].append((current,'\\[\n\\begin{aligned}\n('+label+r')\qquad\qquad & '+inner+'\n\\end{aligned}\n\\]'))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('opening candidate prose','Here is a candidate for a functor ...','same','C retained','Every word and the comma were read in top (267,188,1667,452), 3×.')
a('first turn/tumn',r'\unsure{tumn|turn}','turn',r't\unsure{\rlap{r}u\rlap{u}r|um|ur}n','The initial t and final n are clear. The two crowded middle cells show upper r-like hooks together with lower u-like bowls, but their overlapping strokes also leave the um/ur alternatives unresolved. (1227,190,1315,231), 18×; (1238,195,1307,228), 24×. No typing order is assigned.','low',True,True,'misread word')
a('ring-scheme and first A','underlined A; plain k and A','same','C retained','The A has an independent straight underline; the defining A and base k are plain. (1143,269,1184,307), 18×; top, 3×.')
a('references','Greenberg’s papers, or Serre’s in Bulletin Soc. Math.','same','C retained','The names, apostrophes, comma, abbreviation points and closing parenthesis were read in top, 3×. The first e in see is crowded but has the same bar and lower curve as the next e.')
a('diffuse brown spot below papers','not transcribed','same','C retained','The isolated brown spot has diffuse edges and no identifiable letter, pen stroke or relation to the text. It is not classified as writing. (1071,369,1094,389), 24×.','medium')
a('equation 23 label','right-side tag','right-side tag','label at left','The (23) is at the left prose margin, well before the formula. ring (267,472,1668,663), 3×.','high',True,True,'insertion or placement')
a('equation 23','A simeq underlined A(k).','same','C retained','The relation has an upper wave and an unheaded lower horizontal. The second A is independently underlined; k, parentheses and terminal point are visible. (598,473,788,524), 12×.')
a('corsider','corsider','consider','C retained','The third character is r: an upper hook, upright and broad foot, without the right stem of n. (818,546,980,584), 12×.',hc=True,k='misread word')
a('ring value','underlined A(B)','same','C retained','The A underline, B with two bowls and both parentheses are distinct. (1165,545,1256,585), 12×.')
a('clipped algebra ending','algebra','same','C retained','The last a reaches the dark edge but both its upper curve and lower bowl remain identifiable. (1521,543,1672,583), 16×.','medium')
a('base ring equality','underlined A(k)=A','same','C retained','The underline belongs only to the first A; both equality strokes, k and the point are visible. (365,620,565,664), 12×.')
a('definition of X_B','X_B dfn over equals X tensor A underlined A(B),','same','C retained; physical tensor form drawn','B is lowered under X, dfn has no abbreviation point and sits above the equality, and the tensor base is plain A. The following A is independently underlined; both parentheses and comma are visible. (730,658,1057,743), 10×.')
a('tensor in definition','tensor product','same','C retained; typed x and enclosing oval drawn','The product has a serifed typed x enclosed by a hand-drawn irregular oval; no separate hat is present. (874,689,969,742), 18×. The drawing does not change the tensor reading.')
a('second display number',r'\unsure{34|24}','24, with a note describing 34 corrected to 24','overlaid 3/2 followed by 4','Two rounded 3-like right lobes and a diagonal 2-like descent ending in a rightward foot occupy the first position. Both are retained; no chronological order is assigned solely from the overlap. (269,830,353,878), 18×; (294,832,324,876), 24×.','medium',True,True,'misread symbol or index')
a('second display number position','right-side tag','right-side tag','label at left','The overprinted parenthesized number stands at the left prose margin. eqs (267,660,1101,901), 3×.','high',True,True,'insertion or placement')
a('Picard functor map','B mapsto Pic(X_B).','same','C retained','The left bar, horizontal shaft and right head are clear, as are Pic, lowered B, parentheses and final point. (633,829,697,898), 18×; (703,825,839,886), 12×.')
a('diagonal extension below map arrow','omitted','omitted','thin diagonal extension drawn from lower arrowhead toward lower left','A tapering gray stroke continues from the lower part of the right head down and left, nearly to the next text line. It carries no second arrowhead or label. (611,831,705,919), 16×.','high',True,True,'drawing or diagram')
a('nonrepresentability and fppf prose','This of course ... even if A=k ... fppf sheaf ...','same','C retained','Every word, equality and abbreviation were checked in middle (268,901,1672,1157), 3×. Both equality strokes and plain A and k were enlarged in (1223,903,1296,939), 18×.')
a('cancelled letter in candidate',r'cand\deleted{\unsure{r}}idate','candidate','C retained','A separate x-overstruck cell lies between d and i. Its upper trace is r-like but the dense crossing prevents a secure letter identification. (1133,1042,1347,1079), 14×.','low',hc=True,k='omission')
a('clipped sufficient','sufficient','same',r'sufficie\unsure{n}; no supplied final t','The last visible cell has only its left stem and upper arch before the black edge. There is no visible t cell beyond it. The partial n is marked doubtful, and the absent t is not supplied. (1472,1113,1672,1151), 14×.','low',True,True,'misread word')
a('Artin conditions prose','necessary ... conditions for a group functor ... finite type ... decide wether','same','C retained except clipped ending','All words were read in middle and lower (268,1180,1667,1442), 3×. Wether lacks h after w, and the phrase satisfies to these is retained.')
a('old functor','functor deleted','same','C retained','The f hook, u bowl, n arch, open c, t ascender, o loop and r hook remain identifiable under the x strokes. (628,1328,773,1365), 18×.')
a('final expectation prose','If so, one may expect ... field of representatives ... residue field ...','same','C retained','Every word and point was checked in lower and end (269,1458,1643,1660), 3×.')
a('two points above before is','omitted','omitted','two detached points drawn','Two compact black points sit diagonally above the gap before is; the right point is higher. (1583,1520,1601,1536), 28×. No meaning is assigned.','high',True,True,'drawing or diagram')
a('last characteristic','car. > 0.','same','C retained','The abbreviation point, added right-pointing greater-than sign, tall zero and final period are visible. (529,1610,716,1655), 14×.')
d['unresolved']='The overlapping middle cells in the first turn/tumn remain unresolved, as does the cancelled r-like cell in candidate. The final visible n-like cell of sufficient is clipped; no unseen t is supplied. The second display retains both numeral forms without assigning their order. Detached points and the diagonal extension carry no inferred meaning.'
d['inventory']=[
 ['text','opening paragraph','Here is a candidate ... ring-scheme ... Greenberg ... Serre'],
 ['insertion','middle of first turn/tumn','overlapping middle letter forms','typewriter'],
 ['display','equation 23','A simeq underlined A(k).'],
 ['insertion','equation 23 relation','upper wave and lower unheaded horizontal','his hand'],
 ['text','ring-valued construction','For every algebra B over k, corsider ... We may thus consider'],
 ['display','unnumbered definition','X_B dfn over equals X tensor A underlined A(B),'],
 ['insertion','tensor in definition','oval enclosing typed x','his hand'],
 ['text','functor introduction','and consider the functor'],
 ['display','second numbered display','overprinted 3/2 then 4; B maps to Pic(X_B).'],
 ['insertion','first position of second number','overlaid numeral forms','his hand'],
 ['insertion','functor map','long mapsto','his hand'],
 ['drawing','below right head of mapsto','thin diagonal continuation toward lower left','his hand'],
 ['text','representability discussion','This of course ... fppf sheaf ... looked for candidate'],
 ['deletion','inside second candidate','uncertain r-like cell'],
 ['text','Artin and necessary conditions','In any case, Artin’s work ... sufficie partial n ...'],
 ['text','decision and expectation','conditions ... wether ... sheaf ... If so, one may expect ...'],
 ['deletion','before sheaf just considered','functor'],
 ['text','last three lines','local Picard schemes ... field of representatives ... perfect with car. > 0'],
 ['drawing','above gap before final is','two detached points','unidentified hand'],
 ['insertion','last characteristic condition','greater-than sign','his hand'],
 ]
rv['commit'](d)
