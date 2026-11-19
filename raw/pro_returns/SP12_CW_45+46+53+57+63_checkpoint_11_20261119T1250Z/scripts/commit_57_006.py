from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
the=r't\rlap{e}h\rlap{h}e'
speck=r'\operatorname{Spec}\mathord{\rlap{$k$}(}k)'
note=r'\tikz[baseline=(s.base)]{\node[inner sep=1pt](s){I};\node[anchor=south west,inner sep=1pt](a) at ([xshift=-6em,yshift=7pt]s.north west){\inserted{\handwritten{so that two resolutions can be dominated by \unsure{-|a} third one.}}};\draw ([xshift=-4pt,yshift=-3pt]s.south west) to[out=90,in=190] ([xshift=1pt,yshift=-2pt]a.south west)--([xshift=1pt,yshift=-2pt]a.south east) to[out=0,in=-90] ([xshift=3pt,yshift=4pt]a.south east);}'
dotd=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){d};\fill ([xshift=-1pt,yshift=2pt]s.north west) circle (.3pt);}'
frame=r'''\figure{\begin{tikzpicture}[x=.44em,y=1.7em,every node/.style={anchor=base west,inner sep=0pt}]
\node at (10,0) {\deleted{In terms of \deleted{$\unsure{X|Y}_o$ or rather $B_o=H^o(X_o,\underline{O}_{X_o})$}, this can be defined}};
\node at (23,.60) {\deleted{\inserted{the components $X_o^i$ of $X_o$,}}};
\node at (0,-1) {\deleted{as THE direct image, under the morphism $\operatorname{Spec}(B_{o\,\mathrm{sep}})\quad SPECK$, of}};
\node at (0,-2) {\deleted{the constant sheaf $\underline{Z}$ on \deleted{Sp} the spectrum of the largest separable sub-}};
\node at (0,-3) {\deleted{algebra $B_{o\,\mathrm{sep}}$ of $B_o$}};
\draw (73,.31) to[out=170,in=0] (51,.38) to[out=180,in=-35] (49,.58)--(27,.51)--(10,.28)--(9.8,-.59) to[out=-90,in=0] (8.8,-.70)--(-.3,-.92)--(-.3,-3.37) to[out=-90,in=180] (1,-3.40)--(21,-3.40) to[out=0,in=-90] (23,-3.28)--(23.6,-2.38) to[out=90,in=185] (25,-2.28)--(74,-2.16);
\draw (4,-.92) to[out=-55,in=135] (12,-3.02);
\draw (20,.44) to[out=-60,in=120] (29,-2.17);
\draw (52,.32)--(57.5,-2.10);
\draw (68,-.15)--(70.5,-1.32);
\end{tikzpicture}}'''.replace('THE',the).replace('SPECK',speck)
c=(rv['WIT']/rv['row'](57,6)['codex_file']).read_text()
start=c.index(r'\deleted{In terms of')
end=c.index(' This can be made explicit',start)
oldframe=c[start:end]
d={'cote':57,'scan':6,'sheet_kind':'typescript','hand':'typewriter','replace':[
 (r'\unsure{the|thh}',the),
 (r'\deleted{\unsure{t}}',r'\deleted{t}'),
 (r'\inserted{\handwritten{so that two resolutions can be dominated by \unsure{-|a} third one.}} I',note),
 (r'\unsure{thh|the} constant',r'th\rlap{h}e constant'),
 (oldframe,frame),
 (r'\unsure{fields|fielde}','fiel'+dotd+'e'),
 (r'\operatorname{Spec}(k)$',r'\operatorname{Spec}(k\unsure{)})$'),
 ('Lie algebras Hf','Lie algebras '+r'\rlap{H}of'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole sheet and both halves before C and H, then read six broad crops at 3× line by line. All twenty-seven focused crops at 5–18× and six supplemental crops at 14–18× were actually inspected; four images from a truncated output were redisplayed before being used. The handwritten addition was rotated 0.5 degrees clockwise to an upright baseline. Every C doubt, H difference, cancellation, interline, math-deciding sign and clipped edge was enlarged. The old line and its replacement were read independently. No OCR, delegated reading, context or compilation was used.'}
# The uncertain clipped parenthesis is itself the closing delimiter; do not add a second one.
d['replace'][-2]=(r'\operatorname{Spec}(k)$',r'\operatorname{Spec}(k\unsure{)}$')
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('opening word',r'\unsure{the|thh}','the','t followed by two e/h overprinted positions','Both final positions contain tall h ascenders and low e bodies with middle bars. The overlaid forms are retained without assigning their typing order. (272,234,339,265), 14×.','high',True,True,'misread word')
a('deleted letter before should',r'\unsure{t}','omitted','t deleted','The old letter has an upper ascender and a crossbar beneath the x overstrike. (682,234,711,264), 16×.','medium',True,True,'omission')
a('resolution sentence','existence of resolutions in the strong sense of Hironaka','same','C retained','Each word is visible, with the comma after Hironaka. Top (269,226,1653,429), 3×.')
a('of if','of if','same','C retained','Both words end in f with a high loop and crossbar. The second begins with a separately dotted i. (270,374,374,406), 12×.')
a('punctuation after dim A=2','comma','point','C retained','The mark has a distinct descending comma tail, separate from the insertion guide. (568,381,590,417), 16×.',hc=True,k='other')
a('handwritten addition text','so that two resolutions can be dominated by unsure dash/a third one.','so that two resolutions can be dominated by a third one','C retained apart from placement','The letters and the final separate point were read on the upright crop; there is no initial handwritten comma. (387,324,1359,370), 5×, rotated 0.5 degrees clockwise.',hc=True,k='other')
a('glyph before third',r'\unsure{-|a}','a','C retained','The small mark is a flat thick elongated body with no clear aperture. It may be a dash or a very compressed a; enlargement does not distinguish them. (1099,329,1128,351), 18×.','low',hc=True,k='misread word',m='no')
a('attachment and guide of addition','inline before I','attached after Hironaka','above the line, attached immediately before I, with guide','The left stem begins beside I after the comma following dim A=2, rises, runs beneath the addition and turns upward at its right. The full note is left-shifted above this point. Top crop and upright note crop.','high',True,True,'insertion or placement')
a('algebraic-structure clause','depends in an essential way on the choice of the lifting','same','C retained','All words, the typed Pic(U), parentheses and semicolon were read; no extra qualification is inserted. First (267,430,1639,837), 3×.')
a('example and dependance','example; dependance','same','C retained','The x in example is heavy but no independent deletion crosses it. Dependance has a after d. (1428,504,1573,538), 10×; first crop, 3×.')
a('projecting cone and curve words','projecting cone; elliptic ... el liptic','projecting cone; elliptic ... elliptic','C retained','Projecting ends in ing. The second occurrence of el liptic has a visible gap after el; the earlier occurrence is continuous. First crop, 3×.',hc=True,k='misread word')
a('given lifting and punctuation','given underlined; k ...).','same','C retained','The independent underline is under given only. Three separate points precede the closing parenthesis, followed by a full point. First crop, 3×.')
a('wase/case',r'\unsure{wase|case}','case','C retained','The first position has congested low curved and angular strokes; the remaining ase is legible. The first letter cannot be isolated confidently. (629,936,711,974), 12×.','low',hc=True,k='misread word')
a('the before constant',r'\unsure{thh|the}','the','th followed by h/e overprint','The last cell contains an h ascender and low e body with a bar. The first t and h are separate. (1002,1000,1073,1035), 14×.','high',True,True,'misread word')
a('twisted constant group scheme','D-k replaced by underlined D; occuring','same','C retained','The lower k is separate, and the replacement D has an independent bar underneath. Occuring has one r. Second (274,854,1639,1182), 3×.')
a('withdrawal of central definition','whole block deleted','whole block struck','C retained with drawing added','The irregular outline surrounds four typewritten lines, including the superseded old line and its replacement above; four separate descending diagonals cross it. The right edge is clipped and no closure is invented. Frame (271,1178,1674,1484), 3×.')
a('central cancellation drawing','not reproduced','described in a note','irregular stepped frame and four diagonal strokes reproduced','The upper boundary steps up after closure.; its lower boundary steps down around the short final line. The frame stops at the scan edge on the right. Same frame crop.','high',True,True,'drawing or diagram')
a('superseded phrase before B',r'\unsure{former ring|the ring}','omitted',r'$\unsure{X|Y}_o$ or rather','A capital with upper branches precedes a separate lowered round o; then distinct o-r and r-a-t-h-e-r survive the two rows of x overstrikes. The capital is masked by a diagonal, so X/Y remains open. (690,1214,946,1272), 10×; three overlapping supplements (690,1214,783,1274), (779,1214,868,1274), (858,1214,954,1274), 14×.','low',True,True,'misread word')
a('old formula H exponent',r'\unsure{o|0}','omitted','o','The raised letter has a short round body matching the other lower-case o type, rather than a full-height zero. It survives above the cancellation row. (943,1202,1244,1280), 9×.','high',True,True,'misread symbol or index')
a('old formula and punctuation','B-o=H-o(X-o,underlined O-X-o) without following old comma','omitted','same formula, with separate comma after the inner deletion','B, equality, H, all o subscripts, the plain underlined O and both parentheses remain legible through x rows. A distinct comma follows the old closing parenthesis, outside the x strikes but inside the larger withdrawn block. Formula crop, 9×; (1225,1215,1263,1275), 16×.','high',True,True,'omission')
a('replacement above old line','components phrase inline after old formula','components phrase as main text of withdrawn block','typed replacement above the old line','The typed words the components, the two X letters, raised i, lowered round o letters and final comma form one line above the old formula. (709,1178,1183,1226), 7×; frame crop.','high',True,True,'insertion or placement')
a('subscripts in inserted components','o','0','C retained','The small lowered characters are round lower-case o type, like the o in of and the final B-o, with no tall zero body. Same inserted-line crop.',hc=True,k='misread symbol or index')
a('the in withdrawn direct image clause',r'\unsure{thh|the}','the','t and two e/h overprinted positions','Both second and third positions show an h ascender and a low e bar/bowl. A diagonal crosses the first two letters but does not account for those type forms. (343,1291,408,1327), 14×.','high',True,True,'misread word')
a('gap between spectra','blank gap','arrow','C retained','Between the closing parenthesis of B-o-sep and the next Spec there is blank paper crossed only by the long diagonal cancellation stroke. No arrow shaft or head appears. (1274,1275,1380,1349), 10×.',hc=True,k='text not on the page',m='yes',q='In the withdrawn definition H supplies an arrow between the spectra; the scan has a blank crossed by the cancellation diagonal.')
a('first target spectrum argument',r'\unsure{(k)|kk)}','(k)','k/open-parenthesis overlay, then k and closing parenthesis','The first position retains a serifed k stem and arms plus a taller opening curve extending above and below it. The next k and final closing curve are separate. Both superposed forms are retained without inferring a typing sequence. (1377,1280,1517,1330), 12×; (1453,1282,1499,1327), 18×.','high',True,True,'misread symbol or index')
a('deleted Sp',r'\unsure{Sp}','omitted','Sp deleted','The capital S outer curves and p descender/bowl remain distinct under typed x strikes; the further x is a cancellation mark. (750,1358,816,1395), 14×.','high',True,True,'omission')
a('underlined Z in withdrawn definition','underlined Z','same','C retained','A distinct short line is below the upright Z. The phrase constant sheaf and the following on are clearly typed. Frame crop, 3×.')
a('sub-algebra and end of withdrawn block','sub-algebra ... B-o without point','subalgebra ... B-0.','C retained','A hyphen is typed after sub at the line end. The final B has a short round lowered o and no following punctuation before the frame turns upward. (639,1430,719,1483), 12×; frame crop.',hc=True,k='other')
a('deleted of in live revision','of deleted','omitted','C retained','A round o and the upper loop, ascender and crossbar of f survive under x overstrikes. (849,1498,895,1532), 14×.',hc=True,k='omission')
a('function fielde',r'\unsure{fields|fielde}','fields','fielde','The last body has a closed upper e bowl and a separate middle horizontal ending at its right; below is the open lower e curve. No independent s form can be separated. (1438,1494,1499,1530), 14×; (1440,1492,1507,1535), 18×.','high',True,True,'misread word')
a('point above d in fielde','omitted','omitted','small detached point drawn above and left of d','A small dark triangular-round point is separate above the left part of d, away from the earlier dotted i. Its meaning is not assigned. Same focused and supplemental crops.','high',True,True,'drawing or diagram')
a('components in live revision','X-o superscript i of X-o','X-zero superscript i of X-zero','C retained','The raised i has a separate point and short serifed stem; both lowered o letters are short and round. (731,1550,901,1616), 10×.',hc=True,k='misread symbol or index')
a('deleted product phrase','product of the schemes deleted','same','C retained','Each word survives beneath the x strikes, including the p descender, f top, th ascenders and final s. (1083,1566,1522,1601), 8×.')
a('constant sheaf in live revision','underlined Z','same','C retained','The upright Z has a separate lower bar; the surrounding direct image and under the projection are clearly typed. Below (278,1490,1674,1699), 3×.')
a('product and index in live spectrum','handwritten product; typed k-i','product k-i','C retained','The added mark has an upper horizontal and two descending legs. No product index is written. The separate lower i belongs to k and has a dot. (1373,1622,1475,1684), 10×.')
a('arrow in live spectrum','handwritten right arrow','right arrow','C retained','A horizontal hand-drawn shaft ends in a filled pointed right head. This differs visibly from the blank in the cancelled line. (1485,1622,1679,1692), 10×.')
a('right-edge closing parenthesis','plain closing parenthesis','closing parenthesis and point',r'\unsure{)} with no supplied point','Only upper and lower curved remnants remain beside the black clipped scan edge. They suggest a closing parenthesis, but the whole glyph and any following punctuation are unavailable. Same right-edge crop.','low',True,True,'other')
a('affine-transition paragraph','inverse system (P-n), SGA 6 XII, affine transitions','same','C retained','All words, the parenthesized citation and symbols were read in the end crop. End (280,1720,1674,2037), 3×.')
a('deleted letter before transition',r'\unsure{s}','omitted','C retained','The congested old body has an s-like lower double curve but an upper stem and crossbar overlap it. The masked character is not confidently resolved. (462,1801,490,1839), 16×.','low',hc=True,k='omission')
a('inverse limit arrow','lim with handwritten left arrow below','projective-limit notation','C retained','The shaft has a distinct two-arm left head beneath lim. No index is written underneath. (364,1872,437,1938), 12×.')
a('Lie algebra sentence','It\'s Lie algebra','same','C retained','The apostrophe is typed, and all surrounding words were read. The next phrase explicitly says inverse limit of the Lie algebras. End crop, 3×.')
a('overprinted of','Hf','of','H and o overlaid, followed by f','A full-height serifed H with a crossbar shares its position with a round lower-case o whose lower and side curves remain visible. The f is separate. Both letterforms are represented without assigning their order. (811,1940,863,1978), 14×.','high',True,True,'misread word')
a('last cohomology formula','H-1(X-n,underlined O-X-n)','H-1(X-n,calligraphic O-X-n)','C retained','The raised 1 has an upper serif and long lower foot. The O is a plain oval with a separate lower bar, followed by lower X and further lowered n; all commas and parentheses are visible. (1243,1921,1424,2003), 10×.',hc=True,k='misread symbol or index')
a('page ending','therefore we get','same','C retained','These three words are typed at the end of the last line. No continuation is supplied on this page. End crop, 3×.')
d['unresolved']='The handwritten dash/a before third; wase/case; X/Y in the superseded phrase before or rather; the clipped closing parenthesis at the right edge; and the cancelled s-like character before transition. The e/h, k/open-parenthesis and H/o overlaps are reproduced without claiming a typing order. The detached point above d is preserved without assigning meaning.'
d['inventory']=[
 ['text','opening continuation','the resolution; this ... Hironaka, for instance in char.0 of if dim A=2,'],
 ['text','opening word','two e/h overprinted positions'],
 ['deletion','before should','t'],
 ['insertion','above first paragraph, attached before I','so that two resolutions can be dominated by dash/a third one.','his hand'],
 ['drawing','beneath handwritten addition','long guide with upward turns','his hand'],
 ['text','first paragraph middle','I should point out ... choice of the lifting of the residue field;'],
 ['text','first paragraph end','an instructive example ... projecting cone ... el liptic ...'],
 ['drawing','under given','underline'],
 ['text','second paragraph opening','I have to correct ... defining Q ... wase/case ... (10).'],
 ['text','next sentence','One will then have to replace ... separable closure.'],
 ['text','the before constant','h/e overprinted last letter'],
 ['deletion','central four-line definition','In terms of ... largest separable sub-algebra ... B-o'],
 ['drawing','around central deletion','irregular stepped frame with clipped right edge','his hand'],
 ['drawing','across central deletion','four descending diagonal cancellation strokes','his hand'],
 ['deletion','nested old phrase in first line of central block','X/Y-o or rather B-o=H-o(X-o,underlined O-X-o)'],
 ['insertion','above old formula in withdrawn block','the components X-o superscript i of X-o,'],
 ['text','the in withdrawn direct-image clause','two e/h overprinted positions'],
 ['text','target spectrum in withdrawn line','k and opening-parenthesis overprint before k)'],
 ['deletion','after on in withdrawn line','Sp'],
 ['drawing','under Z in withdrawn line','underline'],
 ['text','live replacement below frame','This can be made explicit ... function fielde ... irreducible components ...'],
 ['deletion','after separable algebraic closures','of'],
 ['drawing','above d in fielde','small detached point','another unnamed hand'],
 ['deletion','after as the','product of the schemes'],
 ['text','following phrase','direct image of the constant sheaf Z under the projection'],
 ['drawing','under live Z','underline'],
 ['insertion','first live spectrum argument','product sign','his hand'],
 ['insertion','between live spectra','right arrow','his hand'],
 ['text','clipped right edge','Spec(k and uncertain closing parenthesis'],
 ['text','last paragraph beginning','To study the inverse system (P-n), use the fact (SGA 6 XII) ...'],
 ['deletion','before transition','s-like character uncertain'],
 ['insertion','beneath lim in P definition','left arrow','his hand'],
 ['text','last paragraph end','It\'s Lie algebra ... Lie algebras [H/o overlay]f ... therefore we get'],
 ['text','of in Lie-algebras sentence','H/o overprint'],
 ['text','bottom left','5 (archive sheet number; retained as comment)','another hand'],
]
rv['commit'](d)
