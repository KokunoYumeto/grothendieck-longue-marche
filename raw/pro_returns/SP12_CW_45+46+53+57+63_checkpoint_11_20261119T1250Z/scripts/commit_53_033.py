from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
upcap=r'\mathrel{\tikz[baseline=-.3ex,x=1em,y=1em]{\draw[line width=.45pt] (0,0)--(1,0)--(1,.12);}}'
cap=r'\mathrel{\tikz[baseline=-.3ex,x=1em,y=1em]{\draw[line width=.45pt] (0,0)--(1,0) (1,-.07)--(1,.09);}}'
loopcap=r'\mathrel{\tikz[baseline=-.3ex,x=1em,y=1em]{\draw[line width=.45pt] (0,0)--(1,0)--(1,-.07) (1,0) to[out=130,in=-30] (.85,.23) to[out=150,in=130] (.94,.26) to[out=-45,in=90] (1,0);}}'
d={'cote':53,'scan':33,'sheet_kind':'text','hand':'his hand','replace':[
 (r'G_m',r'\mathbb{G}_m'),(r'G_a',r'\mathbb{G}_a'),
 (r'\mathrm{O}(Q)\unsure{.}',r'\mathrm{O}(Q).'),
 (r'\unsure{\mathrm{Sp}.|\mathrm{Ex}.}',r'\mathrm{Sp}.'),
 (r'\unsure{\simeq|\sim}',r'\simeq'),
 (r'\unsure{\mathbb{L}|\mathrm{L}}',r'\mathrm{L}'),
 (r'\unsure{\mathcal{O}|\mathscr{O}}',r'\mathbb{O}'),
 (r"k'\unsure{-|\to} k''",r"k'"+upcap+r" k''"),
 (r'égaux \unsure{:|à}',r'égaux :'),
 ('que celà implique','que cela implique'),
 (r'\unsure{donc}','donc'),
 (r'\unsure{comme|librement}',r'\unsure{librement|comme}'),
 (r'on a $R\mathrel{-}L\mathrel{-}M\mathrel{-}0$',r'$0'+upcap+'R'+upcap+'L'+upcap+'M'+cap+'0$'),
 (r'\unsure{cel|celà}','cel'),
 ('reste exact par',r'reste \unsure{ex.ct|exact} par'),
 (r'R\otimes k^I\xrightarrow{\sim}R^I',r'R\otimes k^I\overset{\sim}{'+loopcap+r'}R^I'),
 (r'\unsure{i.e.}','i.e..'),
 (r'\unsure{\relbar|\to}',upcap),
 ],'review':'The primary reader inspected the whole page and both supplied halves before reading C and H. Eight broad crops at 4–5× and forty-two focused or supplementary crops at 8–16× were then read. The first requested projective crop was truncated in tool output; it was displayed again and actually read before decisions were made. The vertical relation was rotated clockwise 90 degrees, the cancelled lower-left word clockwise 1 degree, and the L insertion twice clockwise 4 degrees. Every agreed word and sign, all C doubts, all H differences, the crossed passages, and the mathematical indices and endpoints were checked against the ink. A second view of the whole page was used to check placement and omissions before the inventory was written. The sequence opening, initially provisionally read as C, was changed only after the focused 9× and 16× views showed the rounded first object and a separate capped shaft. No OCR, context or delegated manuscript reading was used.','decisions':[],'inventory':[]}
# Preserve the interlinear position of the abandoned R--L and the detached dot.
old=r"libre \deleted{\unsure{fini|f}} \deleted{\unsure{$R\mathrel{-}L$}}"
new=r"\tikz[baseline=(s.base)]{\node[inner sep=1pt](s){libre \deleted{\unsure{fini|f}}};\node[anchor=south,inner sep=1pt] at ([yshift=4pt]s.north){\deleted{$R"+upcap+r"L$}};\fill ([xshift=12pt,yshift=-2pt]s.south) circle (.4pt);}"
d['replace'].append((old,new))
old=r"$L$\inserted{$\simeq k^{\unsure{n}}$}"
new=r"\tikz[baseline=(s.base)]{\node[inner sep=1pt](s){$L$};\node[anchor=south west,inner sep=1pt](a) at ([xshift=-2pt,yshift=3pt]s.north east){\inserted{$\simeq k^{\unsure{n}}$}};\draw ([xshift=2pt,yshift=-5pt]s.south east) to[out=90,in=210] ([yshift=-2pt]a.south east) to[out=35,in=-90] ([xshift=2pt,yshift=2pt]a.south east);}"
d['replace'].append((old,new))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('title underline','xemples … sur underlined','whole title emphasized','C retained','The straight underline begins below x and ends below sur; the initial E, final k and point lie outside it. Title (170,60,1273,150), 4×.',hc=True,k='insertion or placement')
a('first G-m alphabet','ordinary G',r'\mathbb{G}',r'\mathbb{G}','An outer thin C-shaped arc and a separate long inner upright enclose a narrow left space, unlike the single-outline G of the adjacent GL. (208,172,410,242), 10×; comparison (451,176,593,284), 10×.','high',True,False,'misread symbol or index')
a('first G-a alphabet','ordinary G',r'\mathbb{G}',r'\mathbb{G}','The outer arc returns through a second closed inner left loop before the lower right stroke. The immersion occurrence shows the same doubled construction more openly. Same first-G crop; (1040,411,1121,465), 12×.','medium',True,False,'misread symbol or index')
a('GL and SL list letters','ordinary GL and SL','same','C retained','The G has one outer outline and the L is a cursive tall loop; the S has distinct upper and lower curves. The repeated parenthesized n has the same flattened arch. (451,176,593,284), 10×; group block (184,158,1721,542), 4×.')
a('orthogonal-group label','O(Q)','same','C retained','The O has a top return loop, without a central transverse theta stroke; Q has its own descending tail and both parentheses. (638,174,809,238), 12×.')
a('point after O(Q)',r'\unsure{.} then comma','comma only','point then comma','A detached round dark point lies immediately right of the closing parenthesis, followed farther right and lower by a curved comma. Same crop.','high',True,True,'omission')
a('subgroup prefix','ss-groupe','s-groupe','C retained','Two adjacent high looped s forms precede the independent dash. (860,180,1021,233), 10×.',hc=True,k='abbreviation expanded or spelling modernised')
a('five points under tensor phrase','five points','three points','C retained','Five substantial separate points run left to right; the faint fringe beside the fourth is not a sixth principal mark. (1305,241,1396,272), 12×.',hc=True,k='omission')
a('Sp abbreviation',r'\unsure{\mathrm{Sp}.|\mathrm{Ex}.}','uncertain Sp. described in note','Sp.','The first letter has a small upper and broad lower S loop; the next has a round p bowl and a long descending stroke. A detached point follows. (205,352,258,409), 14×.','medium',True,True,'insertion or placement','yes')
a('triangular-group subscript',r'\unsure{0|o}','0','C retained','The small closed lower oval has no stroke distinguishing numeral zero from letter o. (452,348,577,401), 12×.','low')
a('Diag relation and index','Diag subscript 0; subset','same','C retained','The matching small lower oval is repeated under Diag; the relation is an open shape with a rounded left return and no middle bar. The first occurrence of the oval carries the zero/o doubt. (260,404,603,452), 10×.')
a('vertical relation',r'rotated \unsure{\simeq|\sim}',r'\wr',r'rotated \simeq','After clockwise rotation, one wavy upper stroke and a separate approximately straight lower stroke are visible. (299,449,346,492), clockwise 90 degrees, 14×.','high',True,True,'misread symbol or index')
a('lower G-m alphabet','ordinary G',r'\mathbb{G}',r'\mathbb{G}','The outer thin arc and distinct inner oblique/upright leave a clear doubled left portion, matching the first G-m. (281,483,378,536), 12×.','high',True,False,'misread symbol or index')
a('immersion placement','beside Diag line','after whole array','C retained','The word immersion begins on the same baseline as the Diag expressions, with the G-a and GL(2) continuing to the right. Group block, 4×.',hc=True,k='insertion or placement')
a('immersion G-a alphabet','ordinary G',r'\mathbb{G}',r'\mathbb{G}','The outer arc and inner heavy stem enclose a separate narrow loop on the left of G. (1040,411,1121,465), 12×.','high',True,False,'misread symbol or index')
a('immersion GL first letter',r'\mathbb{G}','ordinary G','C retained','A large outer arc surrounds a second complete inner G, unlike the single-outline upper GL examples. (1242,406,1385,480), 10×.',hc=True,k='misread symbol or index')
a('immersion GL second letter',r'\unsure{\mathbb{L}|\mathrm{L}}','ordinary L','ordinary L','The L has a single looped cursive stem and lower foot, matching the L in the upper GL and SL rather than a second straight parallel upright. Same crop and upper-GL comparison.','medium',True,False,'misread symbol or index')
a('W-definition extra glyph',r'\unsure{\{|\varepsilon}','omitted','C retained','A small glyph with a triangular upper loop, a leftward middle turn and a hooked lower stroke is present after the colon. It does not securely distinguish the proposed brace and epsilon readings. (568,653,628,714), 14×.','low',hc=True,k='omission')
a('W-definition target letter',r'\unsure{k|K} prime','k prime','C retained','The long left stem and two branches have a separate high return; case remains uncertain. The detached prime is clear. (943,641,999,706), 14×.','low')
a('parenthetical introduction','en fait un','un faisceau','C retained','A short en precedes a tall crossed f with a low ai and final t-like loop; a separate un follows. There is no sceau ending. (1111,644,1348,707) and (1107,634,1353,722), 10×.','medium',hc=True,k='misread word')
a('coefficient-ring alphabet',r'\unsure{\mathcal{O}|\mathscr{O}}',r'\mathcal{O}',r'\mathbb{O}','The oval encloses a separate full inner upright joining its upper and lower boundaries, with a top return extending right; k is clearly lowered. (1387,645,1456,724), 12×.','medium',True,True,'misread symbol or index')
a('initial bullet before Pour','point','omitted','C retained','A separate small dark point precedes the capital P. Flatness block (223,735,1673,1095), 4×.',hc=True,k='omission')
a('injection connector',r'\unsure{-|\to}',r'\to','horizontal with short upward right cap','The horizontal ends in one upward stroke, without two oblique arrowhead arms. The source has one prime and the target two. (1346,794,1516,858), 10×.','high',True,True,'drawing or diagram')
a('flat underline','lat only','whole plat','C retained','The underline begins after the descending p and extends below l/a/t only. Flatness block, 4×.',hc=True,k='insertion or placement')
a('cancelled opening after flatness',r'\unsure{So|Si}',r'\ill{}','C retained','The large initial upper curve and lower loop remain, but heavy oblique and horizontal cancellations obscure the ending. (1486,869,1548,929), 14×.','low',hc=True,k=r'readable ink left as \ill{}',m='yes')
a('product display indices and arrow','unindexed first product; target product subscript i','same','C retained','The first product has no lower i, while the second has a separate dotted lower i; every k has its prime and lower i. The connector has a two-armed right head. Flatness block, 4×.')
a('cancelled first claim','On voit que ceci','On sait que ceci','C retained','The old word after On has a low v return, o loop, dotted i and tall t; q descender and c/e/c/i remnants remain under the long cancellation. (332,1093,781,1142), 9×.','medium',hc=True,k='misread word')
a('specialization phrase','faisant tous les k-prime-i','same','C retained','The tall crossed f, a/i/s/a/n/t, separate tous and les, then branched k with prime and lowered i are visible below and right of the old line. Equality block (327,1087,1384,1237), 5×.')
a('sign after egaux',r'\unsure{:|à}','à',':','Two detached dark points are vertically separated; there is no baseline a loop. (850,1110,1102,1170), 10×.','high',True,True,'misread word')
a('power display signs','M tensor k power I; isomorphism arrow; M power I','same','C retained','The two exponent I forms have top and bottom bars. The tensor has no lower k. A separate wave lies above a right head before the crossed product. Equality block, 5×.')
a('cancelled product before M power I',r'\unsure{\prod_i|\prod}','omitted','C retained','An old top bar and upright remnants remain under dense vertical and oblique crossings immediately before M; a possible lower i is not securely separated from the crossing and adjacent line. (1022,1172,1073,1259), 12×.','low',hc=True,k='omission')
a('point after M power I','none','point','C retained','The exponent ends before blank space, without a detached point. Equality block, 5×.',hc=True,k='text not on the page')
a('live inference verb','voit','sait','C retained','The short opening v, o return, dotted i and final tall t match the old voit above. Finite-generation block (341,1237,1702,1621), 4×.',hc=True,k='misread word')
a('tout ending','tout','tout','C retained','The first crossed t and low ou are followed by a separate tall t with a short left cross-stroke. (653,1247,805,1308), 10×.')
a('cela accent','celà','cela','cela','The c/e, tall looped l and small final a are visible; no separate accent lies above the last letter. (1175,1245,1286,1307), 12×.','high',True,False,'abbreviation expanded or spelling modernised')
a('donc before quotient',r'\unsure{donc}','donc','donc','The looped d ascender and joined low o/n/c are distinct from the following heavily crossed word; no independent stroke cancels donc. (817,1311,1000,1367), 10×.','medium',True,False,'misread word')
a('cancelled article before quotient',r'\unsure{un|une}',r'\ill{}','C retained','A low opening u and flattened n-like group are crossed by heavy horizontals; the ending remains masked. Same crop.','low',hc=True,k=r'readable ink left as \ill{}',m='yes')
a('cancelled fini',r'\unsure{fini|f}','fini','C retained','The f loop and descender are clear, with dotted and upright remnants to the right under the crossing; the full ending is not secure. (1480,1325,1611,1378), 12×.','low')
a('point below cancelled fini','omitted','omitted','detached point drawn','A separate small round dark point lies below the middle of the crossed word. It is drawn without assigning a punctuation function. Same crop.','high',True,True,'drawing or diagram')
a('cancelled R-L content',r'\unsure{R--L}',r'arrow then R arrow L','R with upward-capped connector to L','The R bowl and leg, a separate low horizontal with an upward right tip, and an L upright/foot remain visible under the long crossing. The supposed first arrow in H is the descending q of the word above. (1380,1273,1584,1332), 10×.','high',True,True,'misread symbol or index')
a('cancelled R-L position','inline after old fini','inline after old fini','above libre and old fini','The abandoned expression lies on an interlinear level above libre and the cancelled following word. Finite-generation block, 4×; old R-L crop, 10×.','high',True,True,'insertion or placement')
a('cancelled lower-left word',r'\unsure{comme|librement}',r'\ill{}',r'\unsure{librement|comme}','A tall initial ascender and low looped group precede a long flattened middle and a separate final t-like upright. These favor librement, but the crossing masks the internal letters. (350,1389,569,1436), clockwise 1 degree, 12×.','low',True,True,r'readable ink left as \ill{}','yes')
a('cancelled lower-left word position','before live sequence','after live sequence','C retained','The crossed word is to the left of the live sequence on the same line, before it in page order. Finite-generation block, 4×.',hc=True,k='insertion or placement')
a('live sequence opening','on a R','0 then arrow then R','0 then upward-capped connector then R','The first object is a rounded open-topped oval, followed by one long low shaft ending in a vertical upturn; there are no separate n/a loops. It matches the capped connectors farther right. (876,1373,1311,1427), 9×; (880,1379,973,1424), 16×.','medium',True,False,'misread word',q='The sequence starts with 0 and a connector, where C reads the prose on a. The right endpoint is drawn as a cap, separately recorded.')
a('live sequence connectors','three plain dashes','four ordinary right arrows','four capped horizontals','The first three right endpoints have short upward returns; the last has a small extension above and below the shaft. No two-armed heads are visible. Sequence crop, 9×; opening, 16×.','high',True,True,'drawing or diagram')
a('word after flatness hypothesis',r'\unsure{cel|celà}','cela','cel','A short c/e group is followed by one tall l and its foot; blank space follows without an a. (900,1452,991,1508), 12×.','high',True,True,'misread word')
a('exactness word','exact','exacte',r'\unsure{ex.ct|exact}','After the initial e/x forms, a detached round point precedes the low c and final tall crossed t. A compressed a cannot be excluded, but no final e follows the t. (1125,1455,1247,1506), 10×; (1115,1434,1255,1521), 12×.','low',True,True,'abbreviation expanded or spelling modernised')
a('tensoring expression','tensor subscript k then k power I','same','C retained','The circled cross has a lower branched k; the next k has a raised I with two short bars. Finite-generation block, 4×.')
a('R comparison endpoint',r'ordinary arrow with sim',r'ordinary arrow with sim','shaft with looped right cap and sim','A small closed loop rises from the right end and rejoins it above a short lower extension; the separate wave remains above. (528,1555,600,1593), 12×.','high',True,True,'drawing or diagram')
a('donc before finite presentation','live donc','live donc','C retained','The d ascender and low o/n/c are heavily retraced but no separate cancellation crosses the word. (1290,1541,1395,1606), 10×.')
a('first finite-type abbreviation','t-f.','t.f.','C retained','A short horizontal dash separates the t and tall looped f; a detached point follows f. (665,1692,775,1771), 10×.',hc=True,k='abbreviation expanded or spelling modernised')
a('point after libre parenthesis','none','point','C retained','The large closing parenthesis is followed by blank paper. Projectivity block (338,1610,1654,1887), 4×.',hc=True,k='text not on the page')
a('i.e. punctuation',r'\unsure{i.e.}','i.e.','i.e..','A dotted i, separate low point and e are followed by two detached low points, both visible. (1276,1780,1347,1830), 12×.','high',True,True,'omission')
a('inserted L relation','inserted simeq k power n','L equals k power n inline','C retained','The upper relation stroke is curved and the lower one short and straight. The expression rises above the L baseline, beside the p descender from the previous line. (789,1811,929,1910) and (786,1784,950,1911), clockwise 4 degrees, 10×.',hc=True,k='insertion or placement')
a('inserted exponent',r'\unsure{n}','n','C retained','The small raised group has a flattened arch and right downstroke, but its opening touches the descender from the preceding line. Same two rectified crops.','low')
a('L insertion guide','omitted','omitted','long rising curved guide','A curve rises from below and right of L, passes under the inserted expression and turns upward at its far right. Same two rectified crops.','high',True,True,'drawing or diagram')
a('projector introduction','par projecteur p','par un projecteur p','C retained','The short par is followed directly by the long projecteur; there is no intervening un group. The separate p and comma are visible. (889,1831,1317,1910), 8×.',hc=True,k='text not on the page')
a('first kernel display','M tensor-k k-prime; kernel of (1-p) subscript k-prime','same','C retained','The lower k, every prime, both n exponents, parentheses, colon and two-armed arrowhead are separately visible. End block (365,1878,1160,2107), 5×.')
a('second kernel alphabet',r'\mathbb{E} twice','ordinary E twice','C retained','Both E letters have two separate parallel left uprights joined by their three horizontal strokes. (827,1963,1112,2038), 10×.',hc=True,k='misread symbol or index')
a('second kernel connector',r'\unsure{\relbar|\to}',r'\to','horizontal with upward right cap','The endpoint has a single short upward return; no lower oblique arrowhead arm is visible. The label above is clearly 1-p. Same crop.','high',True,True,'drawing or diagram')
a('closing abbreviation',"c'est repr.",'same','C retained','A c, separate high apostrophe, compressed est and the r/e/p/r group with p descender and final point are visible. (376,2051,573,2102), 10×.')
d['unresolved']='The Tr subscript zero/o; the brace/epsilon-like extra glyph after W(M); case of the target k/K; cancelled So/Si, product with or without lower i, un/une and fini/f; the cancelled lower-left word librement/comme; ex.ct/exact; the exponent n touching a descender. Ordinary versus double alphabets were compared within this page; the global comparison remains for the second visual audit. The detached point and nonstandard connector endings are drawn without assigning additional mathematical meaning.'
d['inventory']=[
 ['text','heading','Exemples de groupes algébriques affines sur k'],
 ['diagram','upper group list','G-m; G-a; GL; SL; Tr; Tr-zero/o; O(Q); Diag'],
 ['text','right of top group row','ss-groupe de GL(n) invariant des tenseurs'],
 ['drawing','under tensor phrase','five separate points'],
 ['text','left of Tr-zero/o','Sp.'],
 ['display','under O(Q)','vertical cap above GL(n)'],
 ['display','last list row','Diag-zero(n) subset Diag(n)'],
 ['display','under Diag-zero','rotated simeq; G-m'],
 ['text','right of Diag row','immersion de G-a dans GL(2)'],
 ['text','new paragraph','Soit M un k-module.'],
 ['display','definition','W(M): extra glyph; k-prime maps to M tensor-k k-prime'],
 ['text','right of definition','(en fait un O-k-Module, pas seulement un groupe)'],
 ['text','next three lines','point; Pour que ce soit représentable … plat sur k'],
 ['display','in flatness sentence','k-prime capped connector k-double-prime'],
 ['deletion','after flatness sentence','So/Si'],
 ['text','products introduction','Il faut qu’il transforme produits (infinis) d’algèbres en produits'],
 ['display','products map','M tensor-k product k-prime-i to product-i M tensor-k k-prime-i'],
 ['text','right of products map','bijectif.'],
 ['deletion','before specialization','On voit que ceci'],
 ['text','specialization','faisant tous les k-prime-i égaux : k, on trouve'],
 ['display','specialization map','M tensor k power I; isomorphism arrow; old product; M power I'],
 ['deletion','inside specialization map','product with possible lower i'],
 ['text','finite-generation argument','Et on voit tout de suite que cela implique que M est de type fini'],
 ['text','next line','donc … quotient d’un libre'],
 ['deletion','after donc','un/une'],
 ['deletion','above libre and old fini','R capped connector L'],
 ['deletion','after libre','fini/f'],
 ['drawing','below cancelled fini','detached point'],
 ['deletion','next line left','librement/comme'],
 ['display','next line center','0 capped connector R capped connector L capped connector M capped connector 0'],
 ['text','next line','et comme M est plat, cel reste ex.ct/exact par …'],
 ['display','tensoring expression','tensor-k k power I'],
 ['display','next line left','R tensor k power I; wave over loop-capped shaft; R power I'],
 ['text','finite-presentation conclusion','donc R de type fini … M projectif de t-f.'],
 ['text','parenthesis','(facteur direct d’un libre)'],
 ['text','converse paragraph','Inversement, si M projectif de t.f. i.e.. facteur direct d’un libre L'],
 ['insertion','above and right of L','simeq k power n'],
 ['drawing','under L insertion','long rising curved guide'],
 ['text','after L','par projecteur p, on a'],
 ['display','first final formula','M tensor-k k-prime equals kernel of (1-p) subscript k-prime'],
 ['display','second final formula','W(M) equals kernel of double E power n capped connector double E power n'],
 ['text','last line',"c’est repr."],
 ]
rv['commit'](d)
