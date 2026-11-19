from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
def above(word,ins,shift='0em'):
 return r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){'+word+r'};\node[anchor=south west,inner sep=1pt](a) at ([xshift='+shift+r',yshift=7pt]s.north west){'+ins+r'};\draw ([xshift=-3pt,yshift=-2pt]s.south west) to[out=90,in=180] ([xshift=0pt,yshift=-2pt]a.south west)--([xshift=0pt,yshift=-2pt]a.south east) to[out=0,in=-90] ([xshift=3pt,yshift=3pt]a.south east);}'
tensor=r'\mathord{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\mathrm{x}$};\draw[line width=.5pt] ([xshift=.5pt,yshift=1.3pt]s.center) ellipse[x radius=3pt,y radius=4.5pt];}}'
geometric=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){\deleted{smooth of formally}};\node[anchor=south west,inner sep=0pt] at ([yshift=2pt]s.north west){\inserted{\handwritten{geometrically regular}}};} \deleted{smooth}'
margin=r'''\margin{\figure{\handwritten{\begin{tikzpicture}[rotate=22,transform shape]
\node[inner sep=2pt,align=left](s){Affineness of\\$T$ used to\\have $H^1(T,\underline{\unsure{U|O}}_T)=$\\$H^2(T,\underline{O}_T)=0$};
\draw[line width=.4pt] ([xshift=-.3em,yshift=.6em]s.north west)--([xshift=.5em,yshift=.7em]s.north east) to[out=0,in=90] ([xshift=1em]s.east) to[out=-90,in=0] ([xshift=.4em,yshift=-.7em]s.south east)--([xshift=-.3em,yshift=-.7em]s.south west);
\end{tikzpicture}}}}'''
product=r'\mathord{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\mathrm{x}_{\unsure{\mathbb{k}|k}}$};\fill ([xshift=-.4em,yshift=-.25em]s.center) circle (.3pt);\fill ([xshift=-.5em,yshift=-.55em]s.center) circle (.3pt);}}'
picT=r'\handwritten{/\operatorname{Pic}\mathord{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$(T)$};\fill ([xshift=-1pt,yshift=-5pt]s.south east) circle (.3pt);}}}'
precise=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){precise};\fill ([xshift=1pt,yshift=-2pt]s.south west) circle (.3pt);\fill ([xshift=3pt,yshift=-2pt]s.south west) circle (.3pt);}'
we=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){we};\draw[line width=.45pt] ([xshift=-.5em,yshift=.3em]s.south east) to[out=180,in=90] ([xshift=-.6em,yshift=-.08em]s.south east) to[out=-90,in=180] ([xshift=.4em,yshift=-.15em]s.south east);}'
d={'cote':57,'scan':9,'sheet_kind':'typescript','hand':'typewriter','replace':[
 (r'\uline{scheme}',r'\uline{sche\`{m}e}'),
 (r'\inserted{over $k$},',above(',',r'\inserted{over $k$}','-2em')),
 (r'\inserted{(tautological, and\deleted{)} is )} in',above('in',r'\inserted{(tautological, and\deleted{)} is )}','-3em')),
 (r'\unsure{separable}',r'separabl\unsure{e}'),
 (r'\handwritten{\otimes}',tensor),
 (r'\deleted{smooth of formally smooth}\inserted{\handwritten{geometrically regular}}',geometric),
 (r'\deleted{\unsure{taht}}',r'\deleted{taht}'),
 (r'\unsure{definition}','definition'),
 (r'\inserted{\handwritten{more or less,}} for',above('for',r'\inserted{\handwritten{more or less,}}','-2em')),
 (r'\inserted{\handwritten{affine}} scheme',above('scheme',r'\inserted{\handwritten{affine}}')),
 (r'\handwritten{/\operatorname{Pic}(T)}',picT),
 (r'\mathrm{x}_{\unsure{\mathbb{k}|k}}',product),
 (r'\deleted{\unsure{left hand}}',r'\deleted{left ha\unsure{n}}'),
 ('more precise statement','more '+precise+' statement'),
 (r'\handwritten{\unsure{(}}',r'\deleted{\handwritten{(}}'),
 (r'H^{\handwritten{2}}',r'H^{\unsure{\rlap{$\scriptstyle1$}\handwritten{2}|\rlap{$\scriptstyle2$}\handwritten{1}}}'),
 (r'H^{\handwritten{3}}',r'H^{\unsure{\rlap{$\scriptstyle2$}\handwritten{3}|\rlap{$\scriptstyle3$}\handwritten{2}}}'),
 (r'\handwritten{\unsure{)}}',r'\deleted{\handwritten{)}}'),
 ('As we have seen','As '+we+' have seen'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole page and both halves before C and H, then read seven broad 3× crops line by line. Thirty-five focused crops at 7–22× and five supplements at 9–24× covered all C doubts, H differences, corrections, mathematical signs and detached marks. The margin was rotated 22 degrees clockwise at 6× and 9×; geometrically regular 1 degree clockwise, more or less 2 degrees counterclockwise and affine 2 degrees clockwise. Focused crops 5–10 were redisplayed after an earlier tool output was truncated; they were actually seen in the later calls. One narrow k crop omitted its left edge, so a wider 20× supplement was inspected before retaining the doubt. No OCR, delegated reading, context or compilation was used.'}
c=(rv['WIT']/rv['row'](57,9)['codex_file']).read_text()
i=c.index(r'\margin{');j=c.index('\n\\[',i)
d['replace'].append((c[i:j],margin))
tag=r'\tag*{\handwritten{(18)}}';pos=c.index(tag);i=c.rfind('\\[',0,pos);j=c.index('\\]',pos)+2
block=c[i:j];inner=block[2:block.index(tag)].strip();current=block
for old,new in d['replace']:
 inner=inner.replace(old,new);current=current.replace(old,new)
d['replace'].append((current,'\\[\n\\begin{aligned}\n'+r'\handwritten{(18)}\qquad\qquad & '+inner+'\n\\end{aligned}\n\\]'))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('opening paragraph','The previous constructions ... caracterising Q','same','C retained','Every word was checked in top (262,161,1665,504), 3×. The spelling caracterising and the plain Q are visible.')
a('accent-like mark on scheme','scheme','scheme','sche followed by grave-marked m, then e','A short descending oblique mark is above the m, not above the preceding e. It is retained in that position without normalizing the word. The underline is separate. (1062,266,1317,371), 7×; (1121,286,1187,350), 20×.','high',True,True,'omission')
a('over k insertion','inline before comma','same','typed above comma with curved guide','The addition is typed above the line; a guide rises from the comma position, passes beneath the insertion and turns up at the right. Same 7× crop.','high',True,True,'insertion or placement')
a('tautological insertion position','inline before in','same','typed above in with guide','The phrase sits in the interline space. The guide begins before in, runs beneath the insertion and turns up at its right end. (883,409,1397,503), 7×.','high',True,True,'insertion or placement')
a('cancelled parenthesis after and','deleted closing parenthesis','omitted','C retained','The closing curve is overstruck by x strokes between and and is; the final live parenthesis remains separate. Same insertion crop, 7×.',hc=True,k='omission')
a('deleted rather','rather deleted','same','C retained','All six letters remain identifiable beneath the overstrikes. (930,519,1060,553), 14×.')
a('description pf','pf','of','C retained','The first letter has a clear descender below its bowl and a foot, followed by f. It is p, not o. (1341,517,1386,555), 18×; (1351,511,1385,554), 24×.',hc=True,k='misread word')
a('old To before One','To deleted','omitted','C retained','The capital T top and stem and the rounded lower-case o survive the x overstrikes. (361,587,412,627), 18×.',hc=True,k='omission')
a('D to P map','underlined D; right arrow; P','same','C retained','D has an independent lower line; the hand arrow has a clear right head, followed by plain P and a point. (451,657,608,710), 12×.')
a('arguments final letter',r'argument\unsure{s}','arguments','C retained','The page edge and black border obscure the last position after t; the s cannot be fully isolated. (1510,658,1675,701), 12×.','low',hc=True,k='misread word')
a('separable at right edge',r'\unsure{separable}','separable',r'separabl\unsure{e}','The first eight letters are legible; the last e merges into the dark page edge. The doubt is narrowed to that last letter. (1499,725,1675,767), 12×.','low',True,True,'misread word')
a('first tensor sign','tensor','hatted tensor','typed x with added enclosing oval, no hat','The thin added oval surrounds a serifed x; its rounded top is continuous with the sides and is not a separate hat. The k index and both primes are clear. (559,868,724,927), 12×. The drawing retains the same tensor reading as C.','high',False,True,'misread symbol or index',q='The first base-change tensor has no separate completion hat; H supplies one.')
a('second tensor sign','tensor','tensor','same reading, physical x-and-oval form drawn','The second sign has the same typed x and added enclosing oval, followed by lowered k and k-prime. (1420,866,1525,926), 14×. This is an encoding refinement, not a changed reading.')
a('geometrically regular insertion','after cancelled smooth of formally smooth','same','above cancelled smooth of formally; second smooth remains on following line','The hand phrase is above the first cancelled line, beginning over smooth. The deletion crosses the three words there and smooth at the next line start. (1231,1045,1638,1124), 8×, rotated 1 degree clockwise; (268,1158,404,1200), 12×.','high',True,True,'insertion or placement')
a('cancelled old wording','smooth of formally smooth','same','C retained','The old middle word has o and f, with an ascender and crossbar in f; of is retained. Same two deletion crops.')
a('old taht',r'\unsure{taht} deleted','omitted','taht deleted','The first and last t crossbars, the a bowl and the tall h stem remain visible under the x overstrikes. (621,1160,707,1200), 18×.','high',True,True,'omission')
a('regularity and power-series paragraph','so that ... interest ...','same','C retained','Every word, X, both Q symbols, k-prime and the three typed dots was checked in regular (267,1048,1635,1347), 3×; no grammatical normalization is made.')
a('definition',r'\unsure{definition}','defintion','definition','A narrow dotted i is visible between n and t, crowded against t. The final n is partly at the edge but its left stem and arch remain. (1445,1360,1675,1408), 12×.','high',True,True,'misread word')
a('more or less placement','inline before for','same','above for with curved guide','The hand words and comma sit above for; the guide rises to their left, passes below them and curves upward at the far right. (214,1404,405,1492), 10×, rotated 2 degrees counterclockwise.','high',True,True,'insertion or placement')
a('affine placement','inline before scheme','same','above scheme with curved guide','The two f ascenders, dotted i and final ne are clear. A curved left entry and long lower arm with an upward right tip guide the insertion above scheme. (412,1400,550,1488), 10×, rotated 2 degrees clockwise.','high',True,True,'insertion or placement')
a('margin initial letter','Affineness','affineness','C retained','The first letter is a tall capital A, followed by two long f stems; it is not a small a. Margin (22,1461,244,1747), 6× and 9×, rotated 22 degrees clockwise.',hc=True,k='misread word')
a('margin have','have',r'\uncertain{have}','C retained','The h ascender and shoulder, a loop, v turn and e ending are readable after rotation. Same margin crop.',hc=True,k=r'readable ink left as \ill{}',m='yes')
a('margin first sheaf letter','underlined O','calligraphic O','underlined uncertain U or O','The first letter is open across its top, with two upright sides joined by a lower turn; it looks U-shaped. A separate short lower bar is visible. The closed O in the next line is different. Same margin crop, 9× upright.','low',True,True,'misread symbol or index',q='The first sheaf letter in the margin is open at the top; U versus O remains a reading question.')
a('margin second sheaf letter','underlined O','calligraphic O','C retained','The second letter is a closed round O with a distinct lower bar, followed by lowered T. Same margin crop.',hc=True,k='misread symbol or index')
a('margin degrees and equalities','H-1 equals H-2 equals 0','same','C retained','The first raised digit is a single downstroke; the second has a curved top and lower turn. Both equality pairs and the final round zero are clear. Same margin crop.')
a('margin layout and enclosure','frame with aligned formula rows; 14-degree tilt','unframed inline margin text','four lines at approximately 22-degree tilt, with rounded right enclosure','The second H formula begins at the left below have. The enclosure is open on the left, with long upper and lower arms and a rounded right side. Whole page and rotated margin, 6× and 9×.','high',True,True,'drawing or diagram')
a('equation 18 label','right-side tag','right-side tag','handwritten label at left','The handwritten (18) is at the prose left margin, before the centered formula. (261,1504,343,1557), 12×; formula (263,1351,1675,1583), 3×.','high',True,True,'insertion or placement')
a('equation 18 limits and connecting arrow','two left limits, second with n; hookleftarrow','same','C retained','Both limit arrows point left; only the second has a separate n underneath. The long connecting arrow has a left head and a rounded return at the right. P, T, the first lowered n, equality and parentheses are visible. (442,1503,917,1582), 7×.')
a('equation 18 cancelled formula',r'\unsure{,\underline{O}_{X_{nT}}} deleted','omitted; note only says a cancelled formula ending','C retained','Several typed bodies, an X-like cross and T-like top survive under dense diagonal and looping cancellations, but the comma, O and full subscript cannot be separated securely. The live X has n with a further lowered T. (971,1502,1270,1583), 10×.','low',hc=True,k='omission')
a('equation 18 Pic(T) addition','slash Pic(T)','same','C retained','The added oblique slash, P loop and stem, dotted i, open c, large T and both parentheses are visible. Same 10× formula crop.')
a('point beneath final Pic(T) parenthesis','omitted','omitted','detached point drawn','A small round dark point lies below the closing parenthesis of the added Pic(T). Same formula crop, 10×.','high',True,True,'drawing or diagram')
a('equation 18 product glyph','literal typed x','times','C retained','The product is a serifed lower-case x, not a separate hand multiplication sign. The X-n-T and X-n indices and closing punctuation are legible. (1317,1501,1675,1568), 8×.',hc=True,k='misread symbol or index')
a('equation 18 product base',r'\unsure{\mathbb{k}|k}','k','C retained','The k-shaped body is heavily darkened with an additional lower-left stroke; single versus doubled left structure is not securely separable. (1514,1522,1583,1573), 20×; the earlier narrow crop (1550,1533,1582,1571) omitted its left edge.','low',hc=True,k='misread symbol or index')
a('two points below product x','omitted','omitted','two oblique points drawn','Two detached points lie below the x and to the left of k; the upper one is farther right. Product crop, 8×; wider k crop, 20×.','high',True,True,'drawing or diagram')
a('colon after Sch expression','colon','omitted','C retained','Two vertically separated points follow the outer closing parenthesis. Both parentheses, Sch and the lowered slash-k are visible. (582,1643,841,1708), 9×.',hc=True,k='omission')
a('old left hand',r'\unsure{left hand} deleted','omitted',r'left ha\unsure{n} deleted','The cancelled cells show l, e, f, t, a space, h, a and one final congested cell with n-like remnants. No separate tall d cell follows before the blank and live right-hand. (1212,1642,1377,1689), 14×; (1204,1634,1420,1702), 12×.','low',True,True,'omission')
a('two points below precise','omitted','omitted','two points drawn below initial p','Two round dark bodies lie side by side beneath the initial p of precise. They are reproduced without assigning a punctuation meaning. (1025,1727,1077,1769), 20×.','high',True,True,'drawing or diagram')
a('cancelled Pic expression before limit',r'\operatorname{Pic}(X_{\unsure{nT|2T}}) deleted','omitted','C retained','The Pic and capital X are visible under x overstrikes. The lowered first character has a rounded and angled body compatible with n or 2, followed by T; the overstrike prevents a firm choice. (265,1850,415,1917), 14×; end (265,1841,1674,2057), 3×.','low',hc=True,k='omission')
a('live limit and Pic expression','left limit indexed n; Pic(X-nT)','same','C retained','The hand arrow points left and the n sits beneath it. The typed Pic, X, lowered nT and both parentheses are readable. (423,1847,668,1931), 10×.')
a('obstruction group','H-2(T-et, underlined G-m)','same','C retained','The raised 2, accent on et, comma, plain capital G with an independent lower bar and lowered m are distinct. (893,1838,1107,1918), 10×.')
a('opening parenthesis before at least','handwritten opening parenthesis','opening parenthesis','C retained','A long curved hand stroke opens the parenthesis before at least. (1108,1841,1161,1915), 16×.')
a('inner parenthesis before which',r'handwritten \unsure{(} live','omitted','cancelled handwritten opening parenthesis','The opening curve survives beneath several blue horizontal and diagonal overmarks across it. Its cancellation state is now retained. (269,1925,310,1984), 20×.','medium',True,True,'omission')
a('first overwritten cohomology exponent','handwritten 2','1; note says typed 2 corrected to 1','overlaid 1 and 2, order uncertain','A central upright stem and long foot overlap a rightward upper curve and lower turn. The two layers cannot be securely ordered from the dark merged strokes. The primary representation is 2 over 1, with the reverse explicitly alternative. (960,1908,1014,1954), 22×.','low',True,True,'misread symbol or index',q='The first final cohomology exponent contains overlapping 1/2 forms; its correction order remains uncertain.')
a('second overwritten cohomology exponent','handwritten 3','2; note says typed 3 corrected to 2','overlaid 2 and 3, order uncertain','The raised body has a long lower foot, upper curve, middle bar and overlapping lower right curve. Ink density prevents a secure separation of the typed and added forms. The primary representation is 3 over 2, with the reverse alternative. (1090,1908,1145,1953), 22×.','low',True,True,'misread symbol or index',q='The second final cohomology exponent contains overlapping 2/3 forms; its correction order remains uncertain.')
a('last structure sheaf','underlined O','calligraphic O','C retained','The typed O is a plain closed oval with an independent underline and lowered T. (1436,1931,1497,1984), 18×.',hc=True,k='misread symbol or index')
a('inner closing parenthesis after vanish',r'handwritten \unsure{)} live','omitted','cancelled handwritten closing parenthesis','The curved closing stroke remains visible with blue cross strokes over its upper and middle portions, corresponding to the cancelled inner opening curve. (1612,1918,1675,1985), 18×.','medium',True,True,'omission')
a('punctuation before For simplicity','comma','period','C retained','The dark point at the edge has a descending tail; an additional oblique tail extends below it. The written punctuation is a comma. Same right-edge crop, 18×.',hc=True,k='other')
a('closing parenthesis after normal','handwritten closing parenthesis then point','same','C retained','The long curved closing stroke is followed by a separate round point. (1278,1981,1325,2056), 16×.')
a('mark on final we','omitted','omitted','curved stroke on e with lower right tail','A curved stroke loops at the lower left of the typed e and extends beneath it to the right. It is reproduced without interpreting it as a letter or cancellation. (1419,1997,1474,2043), 18×.','high',True,True,'drawing or diagram')
a('final prose','which is used to insure that it\'s ... normal ... As we have seen','same prose','C retained','The words insure and it\'s, capital For, assumption of normality and unfinished continuation were checked line by line in etale (265,1578,1625,1847) and end (265,1841,1674,2057), 3×.')
d['unresolved']='The clipped final s of arguments and e of separable; the first margin sheaf letter U/O; the densely cancelled formula ending in (18); the dark product base k/bb-k; the final n-like cancelled cell in left han; the nT/2T index in the old Pic expression; and both final overlaid cohomology exponents remain uncertain. No correction order is asserted for the exponent layers. Detached points and the curved stroke on we are reproduced without assigning a meaning.'
d['inventory']=[
 ['text','opening continuation','The previous constructions ... field of representatives ... caracterising Q ...'],
 ['drawing','above m and below first scheme','grave-shaped mark and underline'],
 ['insertion','above comma after scheme','over k'],
 ['drawing','beneath over k','curved insertion guide','his hand'],
 ['text','functor discussion','i.e. as a functor ... this functor is ... in terms ...'],
 ['insertion','above in terms','(tautological, and old closing parenthesis is )'],
 ['deletion','inside added phrase after and','closing parenthesis'],
 ['drawing','beneath tautological phrase','long curved insertion guide','his hand'],
 ['deletion','after gives','rather'],
 ['text','description and cokernel','a description pf P rather than Q. ... One then ...'],
 ['deletion','before One then','To'],
 ['insertion','D to P map','right-pointing arrow','his hand'],
 ['text','extension arguments','As a matter of fact ... arguments k-prime ... separable ...'],
 ['text','base change and regularity','A-prime equals A tensor k-prime ... X tensor k-prime ...'],
 ['drawing','two tensor positions','typed x with enclosing handwritten oval','his hand'],
 ['text','geometric descriptions','However ... algebras which are ... over k ...'],
 ['deletion','two successive lines','smooth of formally smooth'],
 ['insertion','above first line of cancelled phrase','geometrically regular','his hand'],
 ['deletion','after so','taht'],
 ['text','regularity and power series','that tensoring ... Thus, the case ... By definition ...'],
 ['insertion','above for any','more or less,','his hand'],
 ['drawing','beneath more or less','curved left entry and right arm','his hand'],
 ['insertion','above scheme T','affine','his hand'],
 ['drawing','beneath affine','curved insertion guide','his hand'],
 ['text','end of introduction to formula','for any ... scheme T over k, we have'],
 ['margin note','left of equation 18','Affineness of T used to have H-1=H-2=0','his hand'],
 ['drawing','around margin note','open-left enclosure with rounded right side','his hand'],
 ['display','equation 18, left handwritten label','P(T)=left lim P-n(T) hooked left arrow left lim-n Pic(X-n-sub-T) ...'],
 ['insertion','equation 18 label','(18)','his hand'],
 ['insertion','two limits in equation 18','left arrows and second n','his hand'],
 ['insertion','equation 18 connecting relation','hooked left arrow','his hand'],
 ['deletion','equation 18 after X-n-sub-T','uncertain comma and underlined O formula ending'],
 ['insertion','equation 18 after cancellation','slash Pic(T)','his hand'],
 ['drawing','beneath added Pic(T) closing parenthesis','detached point','another unnamed hand'],
 ['drawing','below product x in parenthesis','two oblique points','another unnamed hand'],
 ['text','sheafification paragraph','In fact ... étale sheaf (on (Sch)/k): associated ...'],
 ['deletion','before right-hand','left ha and uncertain final n'],
 ['text','obstruction statement','This comes from the more precise statement ...'],
 ['drawing','below initial p of precise','two detached points','another unnamed hand'],
 ['deletion','before live limit Pic expression','Pic(X-nT/2T)'],
 ['insertion','live lower limit','left arrow and n','his hand'],
 ['text','obstruction group and affine parenthesis','lies in H-2(T-et, underlined G-m) ... at least for T affine, ...'],
 ['insertion','before at least','opening parenthesis','his hand'],
 ['deletion','before which','handwritten inner opening parenthesis','his hand'],
 ['text','vanishing and normality conclusion','which is used to insure ... with values in underlined O-T vanish ...'],
 ['insertion','first H exponent in vanishing clause','overlaid 1 and 2, order uncertain','his hand'],
 ['insertion','second H exponent in vanishing clause','overlaid 2 and 3, order uncertain','his hand'],
 ['deletion','after vanish','handwritten inner closing parenthesis','his hand'],
 ['text','last sentence','For simplicity, I have assumed here that A is normal). As we have seen'],
 ['insertion','after normal','closing parenthesis','his hand'],
 ['drawing','over and below e of final we','curved stroke with right tail','his hand'],
 ]
for x in d['decisions']:
 if x['place']=='margin have':x['kind']='other'
rv['commit'](d)
