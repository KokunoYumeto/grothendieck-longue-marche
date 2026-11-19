from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
def above(word,ins,shift='0em'):
 return r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){'+word+r'};\node[anchor=south west,inner sep=1pt](a) at ([xshift='+shift+r',yshift=7pt]s.north west){'+ins+r'};\draw ([xshift=-3pt,yshift=-2pt]s.south west) to[out=90,in=180] ([xshift=0pt,yshift=-2pt]a.south west)--([xshift=0pt,yshift=-2pt]a.south east) to[out=0,in=-90] ([xshift=3pt,yshift=3pt]a.south east);}'
tensor=r'\mathord{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\mathrm{x}$};\draw[line width=.5pt] ([xshift=.5pt,yshift=1.3pt]s.center) ellipse[x radius=3pt,y radius=4.5pt];}}'
raised_e=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){e};\draw[line width=1pt] ([xshift=.2pt,yshift=-.5pt]s.north)--++(0,3pt);}'
oldleft=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){\deleted{\unsure{right}}};\node[anchor=south,inner sep=0pt] at ([yshift=3pt]s.north){\inserted{\deleted{left}}};}'
extra_x=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){x};}'
d={'cote':57,'scan':11,'sheet_kind':'typescript','hand':'typewriter','replace':[
 (r'\unsure{geometricqlly|geometrically}','geometricqlly'),
 ('irreducible','irr'+raised_e+'ducible'),
 (r'\deleted{the first condition}',r'\deleted{the}'+extra_x+r'\deleted{first condition}'+extra_x+r'\deleted{\unsure{t|i}}'),
 (r'\unsure{togetther|together}',r'tog\rlap{t}e\rlap{e}ther'),
 (r'\deleted{the \deleted{\unsure{right}}\inserted{left} hand side of (20)}',r'\deleted{the} '+oldleft+r'\deleted{ hand side of (20)}'),
 (r'\inserted{\handwritten{$\operatorname{Pic}(X\widehat{\otimes}_k B)/\underline{D}(B)$}} is',above('is',r'\inserted{\handwritten{$\operatorname{Pic}(X\widehat{\otimes}_k B)/\underline{D}(B)$}}','-4em')),
 (r'\deleted{\unsure{ge}}',r'\deleted{g\unsure{e}}'),
 (r'\handwritten{\widehat{\otimes}}',r'\handwritten{\widehat{'+tensor+'}}'),
 (r'\inserted{\handwritten{/\operatorname{Pic}(B)}}$ is',r'$ '+above('is',r'\inserted{\handwritten{$/\operatorname{Pic}(B)$}}','-.5em')),
 ('Thus, under very',r'Thus, unde\rlap{e}r very'),
 ('have stated that',r'have sta\rlap{e}ted that'),
 ('the following',r'the foll\rlap{w}o\rlap{o}wing'),
 (r'\uline{$\unsure{\mathbb{P}|P|B}$roblem}',r'\uline{\rlap{B}Problem}'),
 ('Give a ``natural\'\' construction','Give a ``natural\'\' constructio'+r'\unsure{n}'),
 (r'H^{\unsure{o|0}}',r'H^o'),
 (r'\unsure{closed|closee}',r'close\rlap{e}d'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole page and both halves before reading C and H, then read seven broad 3× crops line by line. All forty-four focused crops at 5–28× were actually displayed and read; the final three were redisplayed after their earlier tool output was entirely truncated. A further 22× supplement covered the two overstruck cells after condition. The first formula addition was rotated 0.7 degrees counterclockwise and the second quotient addition 2 degrees clockwise. All C doubts, H differences, mathematical signs, deleted material, additions and the margin stroke were enlarged. No OCR, delegated reading, context or compilation was used.'}
c=(rv['WIT']/rv['row'](57,11)['codex_file']).read_text()
for number in (21,22):
 tag=r'\tag*{('+str(number)+')}'
 pos=c.index(tag);i=c.rfind('\\[',0,pos);j=c.index('\\]',pos)+2
 block=c[i:j];inner=block[2:block.index(tag)].strip();current=block
 for old,new in d['replace']:
  inner=inner.replace(old,new);current=current.replace(old,new)
 d['replace'].append((current,'\\[\n\\begin{aligned}\n('+str(number)+r')\qquad\qquad & '+inner+'\n\\end{aligned}\n\\]'))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('first word',r'\unsure{geometricqlly|geometrically}','geometrically','geometricqlly','The disputed character has a right descender and foot below the baseline, distinct from the adjacent l stems. (261,180,527,218), 10×.','high',True,True,'misread word')
a('first e in irreducible','plain e','same','e with short upright above it','A dark upright projects from the upper middle of the e body; no additional complete letter can be securely identified. It is drawn rather than assigned a meaning. (583,176,635,217), 20×.','high',True,True,'drawing or diagram')
a('first-line regularity assumptions','underlined D; constant; and assume B ... k','same','C retained','The independent D underline, letters and plain B and k were checked in top (256,177,1667,375), 3×. The a/n/d cells are ordinary, with no securely separate overlaid letter. (1181,179,1248,218), 18×.')
a('first two completed products','X and U with hatted tensor, base k and B','same','C retained; physical x and oval forms drawn','Each typed x is enclosed by a handwritten oval with a separate hat above it; k is lowered and B follows. (1313,230,1413,304), 14×; (574,299,665,370), 14×. This is a drawing-level encoding of the same tensor reading.')
a('cancelled the first condition','the first condition deleted','same','C retained','The letters remain readable beneath the x-shaped overstrikes. (1447,323,1649,360), 12×; (261,391,492,427), 12×.')
a('extra overstrike after the','omitted','omitted','additional x drawn','A full x occupies the space between the cancelled the and first. No underlying character is supplied. (1447,323,1649,360), 12×.','high',True,True,'drawing or diagram')
a('two cells after condition','omitted','omitted',r'x-shaped overstrike followed by deleted \unsure{t|i}','The first extra cell is a clear x; the next has an upper upright or dot and a curved lower-right foot through another x. The masked second character remains t/i. (261,391,492,427), 12×; supplement (425,389,492,431), 22×.','low',True,True,'omission')
a('together overprints',r'\unsure{togetther|together}','together','two middle cells retain overlaid e/t forms','There are two cells between g and h. Both show an e bowl and bar together with a tall t stem and crossbar. The transcription overlays the forms without asserting typing order. (597,385,758,429), 16×.','high',True,True,'misread word')
a('cancelled the before old right','the deleted','same','C retained','The t/h/e outlines are visible through the horizontal strike. (1506,394,1585,429), 18×.')
a('cancelled old right',r'\unsure{right} deleted','omitted','C retained','The five cells are largely occupied by dense x strokes; fragments of curves and stems do not settle the word. (262,460,373,493), 20×.','low',hc=True,k='omission')
a('cancelled replacement left','inserted inline, then included in deletion','left deleted, old word omitted','left above the cancelled old word, itself cancelled','The typed left is on the line above the old word; the later horizontal strike passes through it. Its placement is preserved separately from the lower hand side of (20). (260,441,730,498), 9×.','high',True,True,'insertion or placement')
a('remaining cancelled phrase','hand side of (20) deleted','same','C retained','Every letter, parentheses and 20 are readable under the strike. Same 9× crop.')
a('replacement Pic quotient placement','inline before is','same','above is, with curved insertion guide','The handwritten formula lies above is. Its guide descends at the left before is and extends rightward with an upturned end. (627,422,916,518), 9×, rotated 0.7 degrees counterclockwise.','high',True,True,'insertion or placement')
a('D in replacement quotient','underlined D','plain D','C retained','A short independent underline lies below the capital D; both parentheses of B are visible. Same upright 9× crop.',hc=True,k='omission',q='The replacement quotient above is uses underlined D(B); H drops the underline.')
a('isomorphic to Pic U completed product','Pic(U hatted tensor k B)','same','C retained; physical tensor form drawn','The capital U, added oval and separate hat, lowered k, B and closing parenthesis are visible. (1100,441,1296,516), 12×.')
a('o n spacing','o n','on','C retained','The o and n are separated by a full blank typewriter cell. (254,533,318,571), 20×.',hc=True,k='other')
a('old ge',r'\unsure{ge} deleted','omitted',r'g\unsure{e} deleted','The first cell has a g loop and descending lower bowl. The second has an e-like bar but is congested by overstriking, so only the g is resolved. (1142,534,1192,574), 24×.','low',True,True,'omission')
a('presheaf introduction','noetherian ... geometrically regular ... Q ... etale sheaf ...','same','C retained','All words, the accent on étale and the capital Q were checked in cancel (256,381,1667,650), 3×.')
a('equation 21 label','right-side tag','right-side tag','label at left','The typed (21) is at the left prose margin. eq21 (257,654,1605,805), 3×.','high',True,True,'insertion or placement')
a('equation 21 map and Pic argument','B mapsto Pic(U completed tensor k B)','same','C retained','The initial bar and right arrowhead, Pic letters, U, added oval and hat, lowered k and B are all visible. (633,655,922,728), 10×.')
a('equation 21 added quotient','added /Pic(B)','same','C retained','The slash, Pic letters and both parentheses of B are visible. The left parenthesis is thin but separate. (915,666,995,729), 20×.')
a('equation 21 cancelled old parenthesis',r'\deleted{\unsure{(}}','omitted','C retained','A dense black vertical form with a small lower loop and upper bend remains under cancellation; it does not securely settle the original parenthesis. (965,673,991,713), 26×.','low',hc=True,k='omission')
a('equation 21 new opening and hook','added opening parenthesis and hook arrow to Q(B))','same','C retained','The new opening curve is separate from the returning upper-left end of the arrow. Its right head, Q and B parentheses and terminal point are visible. (993,656,1079,725), 18×; eq21, 3×.')
a('next Pic product','Pic(U completed tensor k B)','same','C retained; physical tensor form drawn','The U, x enclosed by oval and separate hat, lowered k, B and closing parenthesis are clear. (1275,728,1458,796), 12×.')
a('second added quotient placement','inline after Pic expression','same','above is with insertion guide','The hand /Pic(B) is raised above is, with a left descending curve and right upturned guide. (1454,703,1587,795), 12×, rotated 2 degrees clockwise.','high',True,True,'insertion or placement')
a('under overprint','under','same','unde followed by overlapping r/e forms','The last cell has an r upper hook and serif as well as a rounded e-like lower curve and middle trace. Both forms are retained without choosing their order. (873,816,979,858), 18×.','medium',True,True,'omission')
a('Brauer obstruction and local groups prose','Br(B); Q(B); actual local Picard groups','same','C retained','Every word, the parentheses and capitals were read in interpret (256,811,1666,1222), 3×.')
a('stated overprint','stated','same','sta followed by overlaid t/e then ed','The second t position shows a tall stem and crossbar together with an e bowl. (1257,957,1388,996), 16×.','high',True,True,'omission')
a('last U completed product','U hatted tensor k B','same','C retained; physical tensor form drawn','U, the added oval and hat, lowered k and B are visible. (263,1006,347,1074), 14×.')
a('initial of Spec',r'\unsure{\mathbb{S}|S}','S','C retained','The initial has overlapping serifed strokes and a crowded lower body; the alphabet or precise overlay cannot be securely separated. (261,1095,297,1136), 26×.','low',hc=True,k='misread symbol or index')
a('Spec argument and resolution prose','A completed tensor k B; independently ... resolution','same','C retained; physical tensor form drawn','The A, oval around x, separate hat and lowered k were enlarged in (351,1079,462,1151), 14×. The remaining words and punctuation were read in interpret, 3×.')
a('cancelled without','without deleted','same','C retained','All seven letters are identifiable beneath the crossing strokes. (1334,1258,1485,1298), 16×.')
a('non-equicharacteristic condition','equi-caracteristic; car.k > 0','same','C retained','The spelling lacks h after c. The added greater-than sign has a right-pointing vertex, and zero has a tall oval body. (1298,1329,1480,1366), 12×; wish (253,1251,1668,1518), 3×.')
a('likely construction for perfect k','It seems likely that ...','same','C retained','Every word was checked in wish, 3×. The initial t of that has a weak upper stem but a complete crossbar and lower foot; no extra letter is securely present. (403,1395,438,1435), 24×.')
a('cancelled seems','seems deleted','omitted','C retained','The two s forms, two e bodies and m arches remain identifiable through overstriking. (1532,1400,1640,1441), 18×.',hc=True,k='omission')
a('cancelled to','to deleted','omitted','C retained','The t ascender and crossbar and the rounded o survive the x strokes. (259,1471,311,1507), 24×.',hc=True,k='omission')
a('schemes P subscript n','P_n','same','C retained','P has its upper bowl; the n is a distinct lowered arch. (925,1472,975,1527), 20×.')
a('following overprints','following','same','foll followed by two overlaid o/w cells then ing','Each of the two cells after foll has upper w-like serifs together with a rounded o body. Their order of typing is not inferred. (1454,1469,1642,1511), 14×.','high',True,True,'omission')
a('Problem initial',r'\unsure{\mathbb{P}|P|B}roblem','Problem','overlaid B/P followed by roblem','The initial has two B-like bowls as well as the displaced stem and upper bowl of P. Both visible forms are preserved without deciding their order. (258,1537,412,1583), 16×; (264,1539,291,1572), 28×.','medium',True,True,'misread word')
a('Problem heading punctuation','no period','period','C retained','There is no point between the final m and the following blank; the underline runs below the heading. (258,1537,412,1583), 16×.',hc=True,k='text not on the page')
a('Artin ring and characteristic','A; perfect residue field k; car. p > 0','same','C retained','The letters, car. point, hand greater-than sign and tall zero were read directly. (461,1607,557,1648), 18×; problem (237,1532,1667,1798), 3×.')
a('clipped construction ending','construction','same',r'constructio\unsure{n}','The final cell is cut by the dark page edge; only a left upright and upper trace remain. The complete n is therefore not asserted. (1440,1611,1672,1658), 12×.','low',True,True,'misread word')
a('remaining problem prose','group scheme locally of finite type P over k ... imbedding','same','C retained','All words, the two-backtick/two-apostrophe quotation marks around natural, and plain P and k were checked in problem, 3×.')
a('left margin stroke','TikZ vertical irregular line','described in a note','C drawing retained','A long nearly vertical line begins below the heading and extends alongside the problem, wavering slightly left and right. It has no arrowhead or label. (232,1583,265,1995), 5×.',hc=True,k='drawing or diagram')
a('equation 22 label','right-side tag','right-side tag','label at left','The typed (22) is aligned with the left prose margin. end (235,1808,1621,2033), 3×.','high',True,True,'insertion or placement')
a('equation 22 formula','Pic(X) hookarrow P(k),','same','C retained','Pic, capital X, both parentheses, the upper returning hook and right arrowhead, P(k) and comma are visible. (673,1821,977,1865), 10×.')
a('beling','beling','same','C retained','The disputed cell has an i stem with a separate dot; the spelling is beling. (1077,1893,1192,1936), 16×.')
a('added opening parenthesis','hand opening before being','same','C retained','A separate tall blue opening curve follows the typed closing parenthesis of Pic(X). (1381,1880,1431,1942), 18×.')
a('last cohomology exponent',r'H^{\unsure{o|0}}','H^0','H^o','The raised oval has the short body of lower-case o; the ordinary zeros in the two characteristic conditions are taller. (260,1952,485,2012), 14×, compared with (461,1607,557,1648), 18×.','high',True,True,'misread symbol or index',q='The exponent in the final Br H expression is the typed lower-case o; C left o/0 unresolved and H reads zero.')
a('last structure sheaf','underlined O_X','calligraphic O_X','C retained','The O is a plain tall oval with a separate straight underline; X is lowered to its right. (260,1952,485,2012), 14×.',hc=True,k='misread symbol or index',q='The final structure-sheaf symbol is underlined O_X, not H’s calligraphic O_X.')
a('added closing parenthesis','hand closing after hence','same','C retained','The long blue closing curve lies between hence and vanishing. (705,1948,747,2017), 16×.')
a('last word overprint',r'\unsure{closed|closee}','closed','close followed by overlaid d/e','The last cell has the tall right ascender and lower bowl of d together with a displaced e bowl and middle bar. Both forms are kept without assigning order. (1380,1968,1508,2004), 18×.','high',True,True,'misread word')
a('final clause','and hence ... vanishing if k is algebraically ...','same','C retained except recorded overprint','Every word and the final point were checked in end, 3×. The archive pencil number is retained only as a comment, as in C.')
d['unresolved']='The cancelled final cell after condition remains t/i, with no underlying letter assigned to the preceding extra x. Old right remains uncertain; the second letter of old ge is unresolved; the cancelled parenthesis in (21), the crowded initial of Spec, and the clipped n of construction remain uncertain. The upright above e is drawn without a letter identification. No typing order is assigned to any overlapping letter forms.'
d['inventory']=[
 ['text','opening continuation','geometricqlly irreducible ... underlined D ...'],
 ['drawing','above first e in irreducible','short dark upright','typewriter'],
 ['text','regularity and inverse image','This second condition ... U ... this scheme'],
 ['insertion','first X tensor','oval and separate hat around typed x','his hand'],
 ['insertion','first U tensor','oval and separate hat around typed x','his hand'],
 ['deletion','first two prose lines','the first condition'],
 ['drawing','after old the','extra x-shaped overstrike','typewriter'],
 ['drawing','after old condition','extra x-shaped overstrike','typewriter'],
 ['deletion','last old cell after condition','t/i'],
 ['insertion','two middle cells in together','overlaid e/t forms','typewriter'],
 ['text','before old equation-20 reference','this together with the first condition implies that'],
 ['deletion','equation-20 reference','the old right and hand side of (20)'],
 ['insertion','above old right','left, subsequently cancelled','typewriter'],
 ['deletion','raised replacement word','left'],
 ['insertion','above is','Pic(X completed tensor k B)/underlined D(B)','his hand'],
 ['drawing','beneath replacement Pic quotient','curved insertion guide with right upturn','his hand'],
 ['text','Picard group and presheaf introduction','is isomorphic to Pic(U ...). This shows that o n ...'],
 ['insertion','tensor in isomorphic-to Pic expression','oval and separate hat','his hand'],
 ['deletion','before noetherian','g and uncertain e'],
 ['display','equation 21','B maps to Pic(U completed tensor k B)/Pic(B) ... Q(B)'],
 ['insertion','equation 21 map','long mapsto','his hand'],
 ['insertion','equation 21 tensor','oval and separate hat','his hand'],
 ['insertion','equation 21 quotient','/Pic(B)','his hand'],
 ['deletion','equation 21 before new hook','uncertain old opening parenthesis'],
 ['insertion','equation 21 before Q(B)','new opening parenthesis and hook arrow','his hand'],
 ['text','Brauer obstruction','The obstruction for an element of Q(B) ... Br(B)'],
 ['insertion','tensor in obstruction Pic expression','oval and separate hat','his hand'],
 ['insertion','above is in obstruction sentence','/Pic(B)','his hand'],
 ['drawing','beneath added /Pic(B)','curved insertion guide','his hand'],
 ['text','stringent conditions and local groups','Thus, under very stringent conditions ...'],
 ['insertion','last cell of under','overlaid r/e','typewriter'],
 ['text','interpretation and independence','I should have stated ... inverse image ... resolution'],
 ['insertion','second t of stated','overlaid t/e','typewriter'],
 ['insertion','last U tensor','oval and separate hat','his hand'],
 ['insertion','tensor inside Spec','oval and separate hat','his hand'],
 ['text','other characteristic and expectation','One may wish ... It seems likely ...'],
 ['deletion','before also in case','without'],
 ['insertion','car.k relation','greater-than sign','his hand'],
 ['deletion','after The key-point here','seems'],
 ['deletion','next line before is','to'],
 ['text','construction of schemes','is the construction of schemes P_n ... following'],
 ['insertion','following middle cells','two overlaid o/w forms','typewriter'],
 ['text','underlined heading and problem','Problem ... Let A be a local Artin ring ...'],
 ['insertion','initial of Problem','overlaid B/P forms','typewriter'],
 ['insertion','p relation','greater-than sign','his hand'],
 ['margin note','left of problem','long vertical slightly wavering stroke','his hand'],
 ['display','equation 22','Pic(X) hookarrow P(k),'],
 ['insertion','equation 22 relation','hook arrow','his hand'],
 ['text','last two lines','the obstruction ... beling ... Br H^o(X, underlined O_X) ...'],
 ['insertion','after Pic(X) before being','opening parenthesis','his hand'],
 ['insertion','after hence','closing parenthesis','his hand'],
 ['insertion','last cell of closed','overlaid d/e','typewriter'],
 ]
rv['commit'](d)
