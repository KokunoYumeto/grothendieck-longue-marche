from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
def before(word,ins):
 return r'\tikz[baseline=(s.base)]{\node[inner sep=1pt](s){'+word+r'};\node[anchor=south east,inner sep=1pt](a) at ([xshift=2pt,yshift=7pt]s.north west){'+ins+r'};\draw ([xshift=-8pt,yshift=-4pt]s.south west) to[out=90,in=190] ([xshift=1pt,yshift=-2pt]a.south west)--([xshift=1pt,yshift=-2pt]a.south east) to[out=0,in=-90] ([xshift=3pt,yshift=3pt]a.south east);}'
d={'cote':53,'scan':32,'sheet_kind':'text','hand':'his hand','replace':[
 (r'\pi',r'\Pi'),
 (r'comultiplication $\Pi$',r'comultiplication $\unsure{\Pi|\pi}$'),
 ("d'un monoïde",r"d'un \unsure{monoide|monoïde}"),
 (r'\unsure{assoc.}','assoc.'),
 (r'\unsure{qui en fait un}',r'\unsure{qui en fait un|qui en fait une}'),
 (r'\unsure{algèbre|algèbres}','algèbre'),
 (r'\unsure{$k$-lin|linéaires}',r'$k$-lin'),
 ('une inclusion de',r"une \unsure{inclusion|l'inclusion} de"),
 ('pratiquement jamais',r'\unsure{pratiquement|pratiquemt} jamais'),
 (r"\unsure{provient de|provient d'}","provient d'"),
 ('un groupe fini',r'un \unsure{g.pe|g.rpe} fini'),
 (r'\unsure{\dot p|p|j}',r'\dot p'),
 ],'review':'The primary reader inspected the whole scan and both supplied halves before the witnesses, then seven broad crops at 4–8×, two upright margin crops, twenty-seven focused crops at 7–14× and nine supplementary crops at 10–12×. An earlier truncated response did not display the first requested focused images; all twenty-seven were subsequently displayed in small batches and read. The two margins and three supplementary margin details were rotated clockwise 90 degrees, assoc. clockwise 1 degree and the provient insertion clockwise 3 degrees. Every agreed word and mathematical sign was compared with the ink; all C doubts, H differences, cancellations, insertions and diagram endpoints were enlarged. The final inventory was checked top to bottom, including insertion guides, the looped bracket, the extra curve along a margin arrow and its detached mark. No OCR, context or delegated manuscript reading was used.','decisions':[],'inventory':[]}
d['replace'] += [
 (r"\inserted{affine} d'un",before("d'un",r'\inserted{affine}')),
 (r'\inserted{affine $G$} sur',before('sur',r'\inserted{affine $G$}')),
 (r"\inserted{assoc. et unitaire} d'une",before("d'une",r'\inserted{assoc. et unitaire}')),
 (r"\inserted{$V(A)(k')=$} $\mathrm{Hom}_{k\text{-mod.}}(A,k')$",before(r"$\mathrm{Hom}_{k\text{-mod.}}(A,k')$",r"\inserted{$V(A)(k')=$}")),
 (r"\inserted{i.e. les hom $k$-lin $A\to k'$} sont",before('sont',r"\inserted{i.e. les hom $k$-lin $A\to k'$}")),
 (r'\inserted{[algèbre des distributions]}.',before('.',r'\inserted{[algèbre des distributions]}')),
 (r"\inserted{provient d'} un",before('un',r"\inserted{provient d'}")),
 (r'\inserted{à valeurs dans $k$} sur',before('sur',r'\inserted{à valeurs dans $k$}')),
 ]
loopbr=r'\tikz[baseline=-.2ex,x=1em,y=1em]{\draw (.36,.77)--(.12,.77)--(.12,-.08)--(.34,-.08); \draw (.12,.68) to[out=-125,in=180] (.09,-.01) to[out=-10,in=0] (.30,-.11);}'
d['replace'].append((r'\margin{[\unsure{pratiquement|pratiquemt}',r'\margin{'+loopbr+r'\unsure{pratiquement|pratiquemt}'))
old=r'to path={-- ++(1.6pt,0pt) -- ++(1.3pt,1.3pt) -- ++(-1.9pt,-2.4pt) -- ++(.7pt,1.1pt) -- (\tikztotarget) \tikztonodes -- ++(0pt,-1.1pt)}'
new=r'to path={-- (\tikztotarget) \tikztonodes (\tikztostart) ++(1.8pt,-.8pt)--++(1.6pt,2.5pt) (\tikztotarget) ++(0pt,-1.2pt)--++(0pt,2.4pt)}'
d['replace'].append((old,new))
d['replace'].append((r'to path={-- (\tikztotarget) \tikztonodes -- ++(0pt,-1.3pt)}',r'to path={-- (\tikztotarget) \tikztonodes (\tikztotarget) ++(0pt,-1.3pt)--++(0pt,2.5pt)}'))
old=r'A \& A\otimes A \arrow[l] \& A'
new=r'A \& A\otimes A \arrow[l,dash,to path={-- (\tikztotarget) \tikztonodes (\tikztotarget)--++(3pt,3pt) (\tikztotarget)--++(3pt,-2.5pt) (\tikztotarget) ++(2.3pt,0pt) to[out=110,in=-120] ++(1pt,2pt) (\tikztotarget) ++(2.3pt,0pt)--++(1pt,-1.1pt)}] \& A'
d['replace'].append((old,new))
# The marginal curve and detached mark are drawn without naming them as labels.
old=r'\arrow[d,shift left] \arrow[d,shift right]'
new=r'\arrow[d,shift left] \arrow[d,shift right,to path={-- (\tikztotarget) \tikztonodes},execute at end to={\draw ([yshift=-5pt]\tikztostart) to[out=-135,in=160] ([yshift=-11pt]\tikztostart); \fill ([xshift=-2pt,yshift=-4pt]\tikztotarget) circle (.45pt);}]'
d['replace'].append((old,new))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('opening monoide diacritic','monoïde','monoïde',r'\unsure{monoide|monoïde}','One thick, slightly double-lobed high mark is visible above the i position; two separate diaeresis dots cannot be securely separated. (889,172,1100,235), 10×.','low',True,False,'misread word')
a('first affine insertion guide','omitted','omitted','curved rising guide','The line rises from the gap before d’un beneath and to the right of affine. Top (206,127,1708,389), 4×.','high',True,True,'drawing or diagram')
a('affine G insertion guide','omitted','omitted','long bent guide and rising return','A heavy curve runs beneath affine G into the gap before sur, with a thin rising return at its right. Same top crop.','high',True,True,'drawing or diagram')
a('comma after first k','comma','none','C retained','A short downward punctuation stroke touches the lower right return of k before the opening bracket. (1177,175,1302,246), 10×.','medium',hc=True,k='misread symbol or index')
a('first cooperation letter',r'\pi',r'\pi',r'\unsure{\Pi|\pi}','The high cap joins two long descending legs; the right leg has a bent return, leaving case uncertain. (1001,219,1281,291), 10×, clockwise 1 degree.','low',True,False,'misread symbol or index')
a('inserted associative abbreviation',r'\unsure{assoc.}','ass.','assoc.','The compact a/s/s group is followed by a rounded o, an open c and a separate point. Same rectified crop.','medium',True,True,'abbreviation expanded or spelling modernised')
a('association of et unitaire','qualifies comultiplication','qualifies multiplication','C retained','The guide begins just after the cooperation letter and runs beneath assoc. et unitaire, ending before d’une; it does not originate at multiplication. Same crop and top, 4×.',hc=True,k='insertion or placement',q='The inserted associative and unitary qualification is attached to the cooperation, not to multiplication as H states.')
a('association insertion guide','omitted','treated as comma after pi','curved call line below assoc. et unitaire','The line rises from the gap after Pi, runs beneath the inserted words, and turns up at the right. Same rectified crop.','high',True,True,'drawing or diagram')
a('second associative qualification','ass. unitaire above the cancelled phrase','same, with location in note','C retained','The separate short ass. and unitaire are interlinear immediately above qui en fait un/une, following bilinéaire. Top and oldqui (214,319,625,384), 9×.')
a('cancelled qui phrase',r'\unsure{qui en fait un}','qui en fait une',r'\unsure{qui en fait un|qui en fait une}','The q descender, i dot, f ascender and t crossing survive; the last low word is covered by a long horizontal, leaving its ending unsettled. (214,319,625,384), 9×.','low',True,False,'misread word')
a('hom before algebra','hom','hom','C retained','The h ascender and low o/m are followed directly by d’ without a point. Lines (226,368,1708,706), 4×.')
a('algebra ending',r'\unsure{algèbre|algèbres}','algèbres','algèbre','The final b/r/e sequence ends in a low horizontal e return, with no further s shape. (412,382,640,438), 10×.','medium',True,True,'misread word')
a('elements abbreviation',r'\unsure{élmts|éléments}','éléments','C retained','The tall l and short high mark precede a flattened middle and tall t ending; the compressed letters do not securely settle the full versus abbreviated form. (1175,390,1412,443), 10×.','low',hc=True,k='abbreviation expanded or spelling modernised')
a('V formula insertion guide','omitted','omitted','rising curved guide before Hom','A thin curve rises just before the H of Hom and runs below the interlinear V(A)(k-prime)=. Lines, 4×; Hom (1428,384,1712,469), 9×.','high',True,True,'drawing or diagram')
a('Hom subscript','k-mod.','omitted; uncertain h-mod. above coeff','C retained','The lower group has a branched k, a dash, m/o/d and a point. It lies immediately below the Hom and is remote from coeff. (1428,384,1712,469), 9×.',hc=True,k='insertion or placement',m='yes',q='H detaches the k-mod. subscript from Hom and places a misread h-mod. beside coeff.')
a('linear abbreviation',r'\unsure{$k$-lin|linéaires}','uncertain linéaires',r'$k$-lin','A branched k and dash precede the tall l, dotted i and low n; there is no longer éaires ending. (231,426,747,490), 8×.','high',True,True,'abbreviation expanded or spelling modernised','yes')
a('point after inserted hom','none','point','C retained','The low m ends before k-lin; no separate point lies in the gap. Same interlinear crop.',hc=True,k='abbreviation expanded or spelling modernised')
a('map in interlinear explanation',r'A\to k-prime',r'A\to k-prime','C retained','The shaft ends in an uneven head with a high upper arm and a short lower return toward its rightmost tip; the target has a separate prime. (578,426,704,472), 12×.')
a('hom explanation guide','omitted','omitted','long curved guide before sont','The line rises immediately before sont, extends below the whole interlinear explanation, and turns upward at its right. (231,426,747,490), 8×.','high',True,True,'drawing or diagram')
a('verb before called','sont','s’appellent','C retained','The high initial s, round o and low n/t are written as a separate word before the two p descenders of appelés/appelées. (234,466,619,516), 10×.',hc=True,k='misread word')
a('supposed cancellation before verb','none',r'\struck{\ill{}}','C retained','The stroke before sont belongs to the long curved insertion guide; no cancelled word is present. Same crop.',hc=True,k='text not on the page',m='yes')
a('called ending',r'\unsure{appelés|appelées}','s’appellent','C retained','Two long p descenders, an l loop and accent are clear; the flattened final group does not establish one versus two e forms. Same crop.','low')
a('quotation marks','paired high strokes','guillemets','C retained','The opening and closing marks are paired high strokes, not angles. Lines, 4×; interlinear crop, 8×.',hc=True,k='misread symbol or index')
a('distributions underline','underlined','not underlined','C retained','A separate straight line runs below distributions only. Lines, 4×.',hc=True,k='omission')
a('cancelled valeurs',r'\unsure{valeurs}',r'\ill{}','C retained','A low initial loop and tall l remain, but the e/u/r/s region is masked by heavy repeated horizontals. (1223,465,1359,507), 12×.','low',hc=True,k=r'readable ink left as \ill{}',m='yes')
a('bracketed distribution-algebra insertion','whole bracketed phrase inserted','brackets outside insertion','C retained','Both brackets are on the interlinear level with algèbre des distributions, above the call line. Lines, 4×; insertion end (1119,482,1232,554), 10×.',hc=True,k='insertion or placement')
a('distribution-algebra guide','omitted','omitted','long curved call line','The line rises just after Dist(G)(k-prime), crosses above Donc and the cancelled on a, and turns up beyond the inserted closing bracket. Lines, 4× and insertion end, 10×.','high',True,True,'drawing or diagram')
a('period before Donc','period','period','C retained','A detached solid point lies just below the rising guide after the closing parenthesis of Dist(G)(k-prime). (724,522,858,584), 10×.')
a('cancelled on a',r'\unsure{on a}','on a','C retained','Two low old groups remain beneath a dense horizontal crossing; their full letter shapes stay masked. (936,531,1060,574), 12×.','low')
a('groupe revised to monoïde','old groupe; inserted monoïde','same','C retained','The g descender and p loop of groupe are crossed by a separate horizontal; monoïde above it has two visible dots. Lines, 4×.')
a('cancelled G before live G',r'\unsure{G}','omitted','C retained','A large open upper curve and lower loop are traversed by two heavy obliques before the separate live G. (734,590,781,647), 14×.','low',hc=True,k='omission')
a('second coeff point','none','point','C retained','The second f descender is followed by blank space before dans, with no detached point. Lines, 4×.',hc=True,k='abbreviation expanded or spelling modernised')
a('future phrase','et on aura une','et on a un','C retained','After the initial a loop, u/r/a occupy a separate extended group; the next word has the final e return of une. (1252,591,1660,647), 8×.',hc=True,k='misread word')
a('inclusion word opening','inclusion','homomorphisme',r"\unsure{inclusion|l'inclusion}",'A tall left stroke turns into a short raised return before the flattened n/c/l sequence; it does not resemble homomorphisme, but a separate opening l/apostrophe cannot be excluded. (250,664,790,710), 8×.','low',True,True,'misread word',q='The manuscript uses inclusion, with uncertainty at its opening, where H substitutes homomorphisme.')
a('first displayed source arguments','cancelled (k-prime)','live (k-prime)','C retained','A separate horizontal passes through both parentheses and k-prime, joining the long arrow shaft to their right. (659,715,1280,791), 7×.',hc=True,k='deletion state (struck given live or live given struck)',q='The arguments (k-prime) of the first displayed G are cancelled; H prints them as live.')
a('first exponent',r'\unsure{\times|x}',r'\times','C retained','Two thick crossing obliques have no extra vertical or horizontal arm; their shape does not distinguish a small letter x from a multiplication cross. (1213,690,1282,751), 12×.','low')
a('two inclusion arrows','hook arrows','hook arrows','C retained','Each shaft has a short curved left hook and a right head with two oblique arms. First inclusion, 7×; (695,851,1308,936), 7×.')
a('second exponent','star','star','C retained','Three crossing strokes produce six arms, distinct from the two-stroke exponent above. Second inclusion, 7×.')
a('right-note first word','pratiquement','pratiquement',r'\unsure{pratiquement|pratiquemt}','The initial p/r/a/t/i/q/u is visible, while the final long flattened group does not securely reveal all the letters of ement. (1371,853,1699,958), 8×; (1408,851,1580,916), 10×.','low',True,False,'abbreviation expanded or spelling modernised')
a('looped opening bracket','plain bracket','plain bracket','bracket with connected left curved return','A narrow loop lies to the left of the bracket upright and rejoins its lower stroke; it is drawn without asserting a cancelled letter. (1371,853,1699,958), 8×.','high',True,True,'drawing or diagram')
a('right-note remaining words','jamais un isom','same','C retained','The j descender, a/m/a/i/s, separate un, and dotted i/s/o/m are legible; no point follows isom before the closing bracket. Same crop.')
a('upright first margin objects','Dist(X) to Dist(X) times Dist(X)','same in fragments','C retained','The three Dist(X) groups have their closing parentheses and a separate product cross; the shaft has a clear right arrowhead. Margin (16,470,210,1349), clockwise 90 degrees, 5×.')
a('upright first margin old source','cancelled e','epsilon with illegible fragments','C retained','The old source has a small closed e loop under two oblique cancellation strokes; the old horizontal arrow and Dist(X) are also crossed. Same upright crop.',hc=True,k='misread symbol or index',m='yes')
a('upright first margin vertical arrow','e upward to Dist(X)','arrow omitted','C retained','The live e below is joined to a long upward shaft passing through the old source, with a two-armed head just below Dist(X). Same upright crop.',hc=True,k='drawing or diagram')
a('upright first margin cancelled target','cancelled Dist(X)','Dist(X) with illegible surrounding material','C retained','The cancellation traverses the old arrow, D/i/s/t and the lower parts of the parenthesized X. Same upright crop.',hc=True,k='deletion state (struck given live or live given struck)',m='yes')
a('upright first margin unfinished equality','Pi(x)=','same','C retained','The parenthesized lowercase x and two equality strokes are followed by blank space; no right-hand expression is supplied. Same upright crop.')
a('repeated cooperation letters',r'\pi',r'\pi',r'\Pi','The repeated top-bar and two-leg forms match the first cooperation letter. Their case uncertainty is registered at its first page occurrence. Both upright margins and main diagrams, 5–12×.','medium',True,True,'misread symbol or index')
a('example inserted origin phrase',r"\unsure{provient de|provient d'}",'omitted; uncertain postulat at end',"provient d'",'The p descender, r/o/v, dotted i and e/n/t are followed by a d ascender and a separate high short stroke, not a low e loop. (397,943,607,1008), clockwise 3 degrees, 10×.','medium',True,True,'insertion or placement','yes')
a('example origin-phrase guide','omitted','omitted','curved rising guide before un','A fine curve rises from the gap between G and un, runs beneath the inserted phrase, and turns upward at its right end. Same rectified crop; box (222,945,1620,1144), 4×.','high',True,True,'drawing or diagram')
a('example group abbreviation','groupe','groupe',r'\unsure{g.pe|g.rpe}','A separate point follows the descending g; a low arch and p/e remnants follow, partly crossed by a diagonal. The intermediate r cannot be securely separated. (474,986,595,1054), 10×.','low',True,True,'abbreviation expanded or spelling modernised')
a('example constant revision','cancelled constant with inserted ordinaire','cancelled constant with ordinaire inline','C retained','The c/o/n/s/t/a/n/t group has an independent horizontal cancellation, while ordinaire is above it and crossed only by the whole-example diagonal. (698,978,1003,1056), 8×.',hc=True,k='insertion or placement')
a('example on a alors','on a alors',r'\ill{} \ill{}','C retained','The first small o touches the diagonal, then a low n arch, a separate a and tall l with o/r/s ending remain visible. (1298,989,1592,1055), 8×.','medium',hc=True,k=r'readable ink left as \ill{}',m='yes')
a('example formulas','Gamma; G=Gamma subscript k; A=','same','C retained','The Gamma forms have a high horizontal and long left stem; k is below Gamma in the equality. A is followed by two separate horizontal equality strokes. Box, 4×; values insertion (704,1040,963,1116), 9×.')
a('example values insertion','à valeurs dans k','same','C retained','The separate accent over à, tall l in valeurs, d ascender in dans and branched k are visible above sur Gamma. (704,1040,963,1116), 9×.')
a('example values guide','omitted','omitted','curved rising guide before sur','The fine curve rises before sur and extends below the inserted phrase toward k. Same crop.','high',True,True,'drawing or diagram')
a('example supposed postulat','none','uncertain postulat after final Gamma','C retained','There is no word after the final Gamma inside the lower frame; the small phrase is the provient d’ insertion at the top. Box, 4× and rectified origin phrase, 10×.',hc=True,k='text not on the page',m='yes')
a('example enclosing frame','drawn','described only','C retained','The thin enclosure has a raised upper step and a lower-right notch around the shorter second line. Box, 4×.',hc=True,k='drawing or diagram')
a('example cancellation strokes','six oblique strokes','four described strokes','C retained','Six separate long obliques cross the enclosed example from lower left to upper right. Box, 4×.',hc=True,k='drawing or diagram')
a('identity above diagram','gg inverse equals 1','given in note only','C retained','Two g forms, the raised minus and numeral 1, two equality strokes and final numeral 1 are visible above the diagram. Diagram (286,1186,831,1470), 6×.',hc=True,k='insertion or placement')
a('first horizontal connector','small zigzag at left and downward right cap','ordinary right arrow','single oblique at left and full right cap','The left decoration is one rising oblique crossing the shaft. The right end has a short vertical extension above and below; there is no two-armed head. (339,1274,485,1326), 12×.','high',True,True,'drawing or diagram',q='H selects an arrow direction from the expected dual diagram; the ink instead has a capped horizontal with a single oblique near its left end.')
a('first connector label','id subscript G times sigma','same','C retained','The i/d are followed by a lowered G, a separate cross and a looped sigma with a right horizontal extension. Main first diagram, 6×.')
a('second horizontal connector','downward right cap','ordinary right arrow','full short right cap','The endpoint extends briefly above and below the horizontal shaft, without oblique arrowhead arms. (642,1245,757,1320), 12×.','high',True,True,'drawing or diagram')
a('first descending label',r'\unsure{\dot p|p|j}','p',r'\dot p','A separate round dot stands above the tall stem and right-side loop of p. (432,1343,482,1414), 14×.','high',True,True,'misread symbol or index')
a('first triangle diagonals and object','G to e; e to G labelled epsilon','same','C retained','The left diagonal has a head at e; the right has a head at G, with an open epsilon beside it. The lower object has one closed e loop. Main first diagram, 6×.')
a('crossed map opposite diagram','cancelled A to A tensor A','same','C retained','The arrow shaft, two A letters and circled cross remain under independent oblique and horizontal cancellation strokes. (1067,1274,1340,1340), 8×.')
a('second diagram element map','x sigma y; (x,y) maps left','reported in note only','C retained','The left x, looped sigma and descending y stand to the left of a shaft with a left head and right bar; both parentheses and comma surround x,y at the source. (317,1475,836,1760), 6×.',hc=True,k='insertion or placement')
a('second diagram left head','single left arrowhead','single left arrowhead','outer angled head with short inner curved head','An outer two-armed head is accompanied by a separate inner curved return and short lower arm. The extra strokes are reproduced without assigning surjectivity. (432,1542,536,1605), 12×.','high',True,True,'drawing or diagram')
a('second triangle objects and arrows','A; A tensor A; A; k with p and epsilon','same','C retained','The two horizontal shafts point left; the lower-left diagonal points from k to A and carries an undotted p; the right diagonal points from A to k and carries epsilon. The central tensor sign has a rounded enclosure. Second diagram, 6×.')
a('second upright margin cancelled product','cancelled X times Y','same','C retained','Both large letters and the central cross are traversed by an independent horizontal line ending before the live A. (26,1454,224,2016), clockwise 90 degrees, 6×.')
a('second upright margin objects and arrows','A left of A tensor A; two down arrows; diagonal epsilon','same','C retained','A leftward arrow joins the upper objects; two separate vertical shafts have heads below, and the diagonal from A also has its head at the lower level. Same upright crop; (106,1655,191,1750), clockwise 90 degrees, 12×.')
a('second margin diagonal label','epsilon','epsilon','C retained','The upper loop closes and the lower stroke bends left then right, matching a looped epsilon rather than an added word. (143,1800,186,1849), clockwise 90 degrees, 12×.')
a('second margin extra curve','omitted','omitted','open loop along the left descending shaft','A separate thin curve leaves the left shaft, bows left and returns close to it above the arrowhead. It is drawn without identifying a label. (106,1655,191,1750), clockwise 90 degrees, 12×.','high',True,True,'drawing or diagram')
a('second margin detached mark','omitted','omitted','small solid mark below the left arrow','A short detached dark mark lies below and slightly left of the left arrowhead, left of k. Same rotated detail.','high',True,True,'drawing or diagram')
a('second margin tensor argument','x tensor y','same','C retained','The x and descending y flank a closed oval with a central cross, beside the upper object. Complete upright margin, 6×.')
a('second margin epsilon formula',r'\unsure{\varepsilon(x)\varepsilon(y)|\varepsilon x)\varepsilon y)}',r'\varepsilon(x)\varepsilon(y)','C retained','Both epsilon forms and closing curved marks are clear. The low joined strokes before x and y do not securely separate opening parentheses from the letters themselves. (167,1479,220,1624), clockwise 90 degrees, 12×.','low')
d['unresolved']='The first monoide/monoïde diacritic; Pi/pi case at the first occurrence; the ending of cancelled qui en fait un/une; élmts/éléments; appelés/appelées; cancelled valeurs, on a and G; the opening of inclusion/l’inclusion; exponent cross/x; pratiquement/pratiquemt; the group abbreviation g.pe/g.rpe; opening parentheses in the lower margin epsilon formula. The looped bracket, extra curve on a margin arrow and detached mark are reproduced without semantic labels.'
d['inventory']=[
 ['text','first three lines','Si A est l’algèbre … Pi est un'],
 ['insertion','above l’algèbre d’un','affine'],['drawing','first affine insertion','rising curved guide'],
 ['insertion','above monoide sur','affine G'],['drawing','affine G insertion','long bent guide'],
 ['display','opening bracket inline','A; first Pi; second Pi'],
 ['insertion','above cooperation gap','assoc. et unitaire'],['drawing','under associative insertion','long curved call line'],
 ['insertion','above cancelled qui phrase','ass. unitaire'],['deletion','third line left','qui en fait un/une'],
 ['text','next line','hom d’algèbre … les élmts/éléments de Hom'],
 ['display','quantifier inline','for all k-prime'],['insertion','above Hom','V(A)(k-prime)='],
 ['drawing','V equality insertion','rising curved guide'],['display','Hom expression','Hom subscript k-mod.(A,k-prime)'],
 ['insertion','above sont','i.e. les hom k-lin A to k-prime'],['drawing','hom explanation','long curved call line'],
 ['display','inside explanation','A to k-prime'],
 ['text','distribution definition','sont appelés/appelées les distributions de G …'],
 ['deletion','after à in definition','valeurs'],['display','distribution notation','Dist(G)(k-prime)'],
 ['insertion','above Donc line','[algèbre des distributions]'],['drawing','distribution-algebra insertion','long rising call line'],
 ['text','Donc and bracketed algebra phrase','Donc … elles forment une k-prime-algèbre'],
 ['deletion','after Donc','on a'],['deletion','after l’algèbre du','groupe'],['insertion','above old groupe','monoïde'],['deletion','before live G','G'],
 ['text','inclusion introduction','et on aura une inclusion/l’inclusion de monoïdes'],
 ['display','first inclusion','G with cancelled arguments to Dist(G)(k-prime) cross/x'],
 ['deletion','first displayed G arguments','(k-prime)'],['text','between inclusions','et si G est un groupe'],
 ['display','second inclusion','G(k-prime) to Dist(G)(k-prime) star'],
 ['margin note','right of second inclusion','[pratiquement/pratiquemt jamais un isom]'],
 ['drawing','right-note opening','bracket with connected left loop'],
 ['margin note','left margin upper sideways','Dist(X), Pi(x)= and e sketch'],
 ['diagram','upper sideways margin','Dist(X) to Dist(X) times Dist(X); e upward'],
 ['deletion','upper sideways margin old bottom row','e to Dist(X)'],
 ['display','upper sideways margin right','Pi(x)='],
 ['deletion','enclosed example whole','Ex: G provient d’ un g.pe/g.rpe fini …'],
 ['text','example first line','Ex: G … fini Gamma; G=Gamma subscript k, on a alors'],
 ['insertion','above example G un','provient d’'],['drawing','example origin insertion','curved rising guide'],
 ['deletion','example after fini','constant'],['insertion','above constant','ordinaire'],
 ['display','example first-line formulas','Gamma; G=Gamma subscript k'],
 ['text','example second line','A=algèbre des fonctions … sur Gamma'],
 ['display','example second-line formulas','A=; Gamma'],
 ['insertion','above sur Gamma','à valeurs dans k'],['drawing','example values insertion','curved rising guide'],
 ['drawing','example enclosure','stepped and notched frame'],['drawing','over example','six oblique cancellation strokes'],
 ['display','above first main diagram','gg inverse equals 1'],
 ['diagram','first main triangle','G; G times G; G; e, idG times sigma, Pi, dotted p, epsilon'],
 ['deletion','opposite first diagram','A to A tensor A'],
 ['diagram','second main triangle','A; A tensor A; A; k, Pi, epsilon, p'],
 ['display','above second diagram','x sigma y mapped from (x,y)'],
 ['drawing','second diagram left horizontal','outer angled and inner curved arrowhead'],
 ['margin note','left margin lower sideways','X times Y cancellation and A, A tensor A, k sketch'],
 ['deletion','lower sideways margin opening','X times Y'],
 ['diagram','lower sideways margin','A left from A tensor A; two down arrows; diagonal epsilon to k'],
 ['drawing','left vertical margin arrow','open loop beside shaft'],
 ['drawing','below left margin arrowhead','small detached ink mark'],
 ['display','lower sideways margin beside top row','x tensor y'],
 ['display','lower sideways margin beside k','epsilon(x)epsilon(y) with doubtful opening parentheses'],
 ]
rv['commit'](d)
