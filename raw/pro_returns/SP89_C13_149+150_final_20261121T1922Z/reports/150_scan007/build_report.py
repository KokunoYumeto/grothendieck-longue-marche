from pathlib import Path
import csv
import json
import re

ROOT = Path('/workspace/scratch/8759b8008681')
OUT = ROOT / 'work/reports/150_scan007'
C = (ROOT / 'packets/150_scan007/C.tex').read_text()
H = (ROOT / 'packets/150_scan007/H.tex').read_text()
BOXES = json.loads((OUT / 'crop_boxes.json').read_text())

# This is a first-reader builder. Do not rerun after root takes ownership.
FIG1 = r'''\figure{\begin{tikzpicture}[x=0.012cm,y=-0.012cm,line cap=round,line join=round]
\draw[line width=2.3pt] plot[smooth] coordinates {(436,274) (416,250) (391,240) (333,235) (285,258) (267,310) (281,368) (324,408) (380,415) (437,386) (446,369)};
\draw (436,274) .. controls (458,310) and (459,342) .. (446,369);
\draw (303,311) .. controls (314,258) and (378,251) .. (410,300);
\draw (292,314) .. controls (327,252) and (395,258) .. (417,326);
\draw (310,293) .. controls (284,350) and (301,384) .. (334,395);
\draw (342,395)--(349,394);
\draw (414,303)--(472,297) (408,301)--(434,280);
\draw (436,274)--(730,257) (368,332)--(700,309) (446,369)--(704,350);
\draw[line width=1pt] (375,323)--(381,321) (354,373)--(361,372);
\fill (369,332) circle (4.5);
\node at (558,157) {$\Sigma_2$};\node at (313,216) {$\Sigma_{02}$};
\node at (463,257) {$\Sigma_{012}$};\node at (596,251) {$\Sigma_{12}$};
\node at (349,351) {$\Sigma_0$};\node at (415,345) {$c_{01}$};
\node at (484,338) {$\Sigma_{01}$};\node at (597,304) {$\Sigma_1$};
\node at (473,395) {$\Sigma_{012}$};\node at (616,377) {$\Sigma_{12}$};
\end{tikzpicture}}'''

FIG2 = r'''\figure{\begin{tikzpicture}[x=0.025cm,y=-0.025cm,line cap=round,line join=round]
\draw (1212,195)--(1373,258)--(1368,195)--(1219,321)--(1216,258);
\draw (1212,195)--(1216,258);
\draw[->] (1212,195)--(1215,244);
\draw[->] (1216,258)--(1288,258);
\draw (1303,262)--(1373,258);
\draw (1213,210)--(1219,217) (1368,210)--(1361,218);
\fill (1212,195) circle (3.2);
\fill (1216,258) circle (5.5);
\fill (1219,321) circle (3.6);
\fill (1368,195) circle (3.3);
\fill (1373,258) circle (5.8);
\fill (1211,184) circle (1.1);
\fill[white] (1216,258) ellipse (0.65 and 1.7);
\fill[white] (1219,321) ellipse (0.5 and 1.1);
\fill[white] (1373,258) ellipse (0.8 and 1.7);
\node[left] at (1203,179) {$\unsure{i}$};
\node[left] at (1206,258) {$1$};\node[below] at (1298,270) {$0$};
\end{tikzpicture}}'''

TUPLE = r"(i_0,\unsure{{:}\ldots|i_1\ldots},i_n)"
TUB = r"\mathop{\overset{\unsure{\bullet|\deleted{\circ}}}{\mathrm{T}}\mathrm{ub}}\nolimits^{\circ}"
FORM1 = r"\Sigma_i=X_i'=X_i\setminus\left(X_i\cap\bigcup_{k<i}" + TUB + r"(X_k,X_i)\right)"
RANGE = r"\substack{\deleted{\unsure{k<j}}\quad\deleted{\unsure{i<k|j<k}}\\\deleted{\unsure{k\ne i}}\\\inserted{i<k<j}}"
FORM2 = r"\Sigma_{(i,j)}=\deleted{\unsure{\partial}}\operatorname{Tub}^{\bullet}\left(X_i',X_j\deleted{\unsure{\varnothing}}\setminus\bigcup_{" + RANGE + r"}\operatorname{Tub}(X_k,X_j)\right)\hookrightarrow X_j'=\Sigma_j"

MSQUARE = r'''\diagram{\begin{tikzcd}
\Sigma_\delta\arrow[r,hook]\arrow[d]&\Sigma_{\delta'}\arrow[d]\\
\Sigma_d\arrow[r,hook]&\Sigma_{d'}
\end{tikzcd}}'''
MARRAY = r"\diagram{\[\begin{array}{ccc}d&\supset&d'\\&&\cap\\\unsure{\delta|d}&&\delta'\end{array}\]}"
MPOINT = r"\diagram{\begin{tikzcd}\bullet\arrow[d]\\d'\end{tikzcd}}"
MARGIN = '\\margin{' + MSQUARE + '\n' + MARRAY + '\ncofinaux\n' + MPOINT + '}'
DELETED_T = r"\deleted{$\Sigma_{i,j}=T.$}"

VDIAG = r'''\diagram{\begin{tikzcd}[column sep=small,row sep=large]
&\mathcal V_{i,j}\arrow[d]&{}=\mathcal V(X_i^*,X_j)\setminus\displaystyle\bigcup_{i\leq k<j}\mathcal V(\unsure{X_i^*|X_i'},X_j)\cap X_k\arrow[r,hook]&X_j^*\\
X&X_i^*&&
\end{tikzcd}}'''

LOWER = r'''\diagram{\begin{tikzcd}[row sep=large,column sep=large,execute at end picture={\draw (branchend) ++(0.10,0.13)--(branchend)--++(0.16,-0.03);}]
\mathcal V_{ijk}\arrow[r]\arrow[d]&\mathcal V_{jk}\arrow[d]\arrow[r,hook,no head]&X_k^*\arrow[d,""{name=branch,coordinate,pos=.55}]\\
\mathcal V_{ij}\arrow[r,hook]\arrow[d]&\mathcal V(X_j^*,X_k)\arrow[r,phantom,"\deleted{\xrightarrow{\unsure{\sim}}}" description]&\deleted{X_k}\\
X_i^*&&
\arrow[from=branch,to=2-2,dashed,no head,to path={(\tikztostart)--++(-1.5,-0.45) coordinate (branchend)\tikztonodes},"\unsure{\sim|r}"']
\end{tikzcd}}'''
LAMBDA1 = r"\lambda_i'\unsure{T'|T^i}=\lambda''T''"
LAMBDA2 = r"a\leq\operatorname{Inf}(\lambda',\lambda_i')"
LAMBDAS = '\\margin{$' + LAMBDA1 + '$\\qquad\n$' + LAMBDA2 + '$}'

DRAFT = '\n\n'.join([
    r'\scanpage{7}' + '\n' + r'\margin{\unsure{S|5}}',
    FIG1, r"\margin{$\unsure{\supset d'}$}", FIG2,
    r'$\Sigma_{i_0i_1\ldots i_n}$\qquad\deleted{\unsure{covariant}} foncteur contravariant' + '\n' + r'par rapport aux drapeaux' + '\n' + 'variables $' + TUPLE + '$',
    '\\[\n' + FORM1 + '\n\\]', '\\[\n' + FORM2 + '\n\\]',
    r'\[i<k<j\]', MARGIN, DELETED_T, VDIAG,
    r'\noindent $\mathcal V_{ijk}$\par', LOWER, LAMBDAS, r'\margin{\uline{6}}'
]) + '\n'

def flat(s):
    return re.sub(r'\s+', ' ', s).strip()

def exact_present(s, witness):
    return not s or flat(s) in flat(witness)

changes = []
def change(id, crop, place, c, h, final, evidence, confidence='high', kind='misread symbol or index', against_c=False, against_h=True, marked_in_h=False, consequential=False, error_category='1'):
    assert exact_present(c,C), (id,'C',c)
    assert exact_present(h,H), (id,'H',h)
    changes.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,
                        crop=f'crops/150_scan007_{crop}.png',box=BOXES[crop],confidence=confidence,kind=kind,
                        against_c=against_c,against_h=against_h,marked_in_h=marked_in_h,
                        consequential=consequential,error_category=error_category))

change('P01','P01','Upper thin mark',r'\mspage{5}','« S »',r'\margin{\unsure{S|5}}',
       'One continuous upper curve, diagonal transition and lower curve favor S; no separate angular upper bar establishes 5. The thin pen differs from the body, so author hand and pagination function are not asserted.',
       'low','misread symbol or index',True,False)
change('P02a','P02','Upper-left drawing: upper junction label',r'\unsure{\Sigma_{012}}',r'$\Sigma_{012}$',r'\Sigma_{012}',
       'Closed 0, separate short upright 1 and curved 2 are individually visible after Sigma. This is a cropped certainty resolution of C.',against_c=True,against_h=False)
change('P02b','P02','Upper-left drawing: c label beside center',r'\unsure{c_{01}}',r'$c_{01}$',r'c_{01}',
       'The initial c has an open right side; the lower 0 is closed and the adjacent 1 is a separate short stroke. C doubt resolved on the crop.',against_c=True,against_h=False)
CFIG1=C[C.index('\\figure{'):C.index(r"\margin{$\unsure{\supset d'}$}")].strip()
HFIG1=H[H.index('À gauche'):H.index('À droite, un petit graphe')].strip()
change('P02c','P02','Upper-left drawing: boundary, connectors, interior strokes',CFIG1,HFIG1,FIG1,
       'The heavy outer arc runs around the left, top and bottom but the boundary between the right junctions is thin. A short oblique connector reaches the upper junction. Interior arcs have return strokes and a pen gap, without paired arrowheads; two isolated dark dashes lie above the central ray near the filled point and below center. All ten labels and three rays retained.',
       'medium','drawing or diagram',True,True,False,True,'4')
change('P03','P03','Small rotated upper-left fragment',r"\margin{$\unsure{\supset d'}$}",'',r"\margin{$\unsure{\supset d'}$}",
       'A long hooked relation-like stroke and a short d-prime-like group are present, omitted by H. Overlap prevents a secure order or a new arrow interpretation; inherited uncertainty remains.',
       'low','omission',False,True,False,False,'3')
CFIG2=C[C.index('\\figure{',C.index('\\figure{')+1):C.index(r'$\Sigma_{i_0i_1\ldots i_n}$')].strip()
change('P04a','P04','Upper-right graph: labels',r'\node[left] at (0,2.2) {$\unsure{i}$};\node[left] at (0,1) {$1$};\node[below] at (1.1,1) {$0$};',
       'sans légende lisible',r'\unsure{i};\quad1;\quad0',
       'Midleft 1 is a single upright; lower 0 is a closed loop. Upper i-like label has a tall stroke and displaced raised curve, still not secure. H leaves all three labels unread.',
       'medium','readable ink left as \\ill{}',False,True,True,False,'5')
change('P04b','P04','Upper-right graph: gap, small marks and pen gaps',CFIG2,'un petit graphe de cinq points reliés par des flèches, sans légende lisible.',FIG2,
       'Five principal blobs and two crossing diagonals are present, without a vertex at either crossing. The horizontal arrow stops before its crossing and a separate segment resumes to the right. A small isolated dot sits immediately above the upper-left blob. One-sided branches beneath both upper vertices lack paired heads and are copied as strokes; white holes in three blobs are pen gaps.',
       'medium','drawing or diagram',True,True,False,True,'4')
change('P05','P05','Cancelled word before foncteur',r'\deleted{\unsure{covariant}}',r'\struck{\ill{}}',r'\deleted{\unsure{covariant}}',
       'The strike masks low letter joins and several internal tall strokes remain. The inherited covariant candidate is not resolved; it cannot be certified by the following live contravariant. This explicit unresolved reading differs from H illegible.',
       'low','misread word',False,True,True,False,'2')
change('P06a','P06','Live first prose line',r'foncteur contravariant',r'fonctions continues \uncertain{variant}',r'foncteur contravariant',
       'The first word has f descender, o loop, joined nc, tall t and compact eur ending; the second has a continuous contra- opening and the following variant sequence. There is no separate continues word.',
       kind='misread word',marked_in_h=True,consequential=True,error_category='2')
change('P06b','P06','Second and third prose lines',r'par rapport aux drapeaux variables',r'par rapport au drapeau variable',r'par rapport aux drapeaux variables',
       'The short aux has a terminal crossed return; drapeaux has its p descender and terminal x-shaped return; variables has the compressed terminal continuation. The plural sequence is visible without grammatical completion.',
       kind='misread word',error_category='2')
change('P06c','P06','Tuple endpoint indices',r'$(i_0,\ldots,i_n)$',r"$(i'_0,\ldots,i'_n)$",TUPLE,
       'Each endpoint i has one displaced raised tittle but no second independent prime stroke. The subscript 0 is a closed loop and n has its low shoulder; retain unprimed endpoints. Internal cluster is separately logged at P06d.',
       'high','misread symbol or index',False,True,False,True,'1')
change('P06d','P06','Tuple internal cluster after first comma',r'$(i_0,\ldots,i_n)$',r"$(i'_0,\ldots,i'_n)$",TUPLE,
       'There are five marks: an upper round dot over a low horizontal pill, followed by three low marks (dot, short dash, dot). A colon-like group plus ellipsis is favored. No secure i stem or separate subscript 1 establishes i_1; preserve the alternative locally. This newly opened sub-place was assessed in the saved crop without recropping.',
       'low','omission',True,True,False,False,'3')
change('P07a','P07','First Sigma formula: open circle position',r'\unsure{\operatorname{Tub}^{\circ}|\mathring{\operatorname{Tub}}}',r'\overset{\circ}{\mathrm{Tub}}',TUB,
       'The open ring has a white center and lies above/right of b, distinct from the separate dark mark above T. Resolve C choice in favor of upper-right circ; H moves the open circle above the whole operator. The upper dark mark remains separately uncertain.',
       'high','misread symbol or index',True,True,False,True,'1')
change('P07b','P07','First Sigma formula: separate mark above T',r'\unsure{\operatorname{Tub}^{\circ}|\mathring{\operatorname{Tub}}}',r'\overset{\circ}{\mathrm{Tub}}',TUB,
       'A second dark filled/overtraced mark is visible above the T, separate from the open right circle. Blackness does not establish cancellation: retain bullet versus cancelled-circle state as a local alternative, with no chronology asserted.',
       'low','omission',True,True,False,True,'3')
change('P08a','P08','Second Sigma formula: cancelled symbol before Tub',r'\deleted{\unsure{\partial}}',r'\struck{\ill{}}\,\mathrm{Tub}^{\bullet}',r'\deleted{\unsure{\partial}}\operatorname{Tub}^{\bullet}',
       'A compact looped symbol is crossed before the live Tub. The crossing prevents secure recovery of every part of partial; keep the inherited candidate explicit, while H leaves the cancelled ink illegible.',
       'low','misread symbol or index',False,True,True,False,'1')
change('P08b','P08','Second Sigma formula: cancelled mark after X_j',r'X_j\deleted{\unsure{\varnothing}}\setminus',r'X_j\setminus',r'X_j\deleted{\unsure{\varnothing}}\setminus',
       'A small crossed loop/stroke lies between the live X_j and the broad live setminus; it is not part of the latter. The empty-set-like candidate remains uncertain and is absent from H.',
       'low','omission',False,True,False,False,'3')
change('P08c','P08','Second Sigma formula: cancelled and inserted index groups',r'\substack{\deleted{\unsure{k<j}}\\\deleted{\unsure{k\ne i}}\\\inserted{i<k<j}}',
       'sous la seconde réunion, un indice longuement raturé ; ce qui reste lisible est « $i<k<j$ », repris seul plus bas sur la page.',RANGE,
       'Upper k<j and lower k-not-equal-i remain crossed and doubtful. A further crossed group to the right has an i/j-like first stroke, a distinct angle and k-like last stroke: i<k|j<k, omitted by both witnesses. The clear lower i<k<j is live, with a curved leader attaching it to the union index. Its leader is not a parenthesis or another cancellation.',
       'low','omission',True,True,True,True,'3')
change('P10a','P10','Rotated marginal relation array',r"\begin{array}{ccc}d&\supset&d'\\\cap&&\cap\\\delta&&\delta'\end{array}",
       r"$\delta'\subset\bar\delta$ \ill{}, $d\supset\delta$",MARRAY,
       'Upper d, superset and d-prime are distinct. The lower row has a delta/d-like left label and delta-prime at right. Only one independent vertical cap is visible, above the right lower delta-prime; no separate left cap under d is supported. Completing P16, at [280,763,430,1168], preserves the lower extent and its main-text context is excluded. The left delta remains locally uncertain rather than being supplied from the square.',
       'medium','drawing or diagram',True,True,True,True,'4')
change('P10b','P10','Rotated marginal word',r'cofinaux','',r'cofinaux',
       'Open c, o loop, tall f, i tittle, joined naux sequence are visible in the rotated margin; the word is absent from H.',
       'high','omission',False,True,False,False,'3')
change('P10c','P10','Rotated marginal point-to-d-prime diagram',r"\diagram{\begin{tikzcd}\unsure{\bullet}\arrow[d]\\d'\end{tikzcd}}",'',MPOINT,
       'An isolated filled spot stands above a downward shaft with arrowhead, ending at d-prime. No letter strokes emerge from the point. Resolve the bullet doubt at medium confidence; H omits the mini diagram.',
       'medium','drawing or diagram',True,True,False,True,'4')
change('P10d','P10','Rotated marginal square: orientation and arrows',r"\Sigma_\delta\arrow[r,hook]\arrow[d]&\Sigma_{\delta'}\arrow[d]\\ \Sigma_d\arrow[r,hook]&\Sigma_{d'}",
       r"$\Sigma_{\delta'}\to\Sigma_{d'}$ au-dessus de $\Sigma_{\delta}\to\Sigma_{d}$, reliés par deux inclusions verticales",MSQUARE,
       'In the natural reading orientation of the rotated writing, Sigma_delta and Sigma_delta-prime form the upper row, Sigma_d and Sigma_d-prime the lower. Both horizontal shafts have hooks at their left ends and pointed right ends; the two plain shafts descend to the corresponding d objects. H describes the square with a different row orientation and vertical inclusions. All four labels, both hooks and both down arrows are retained explicitly.',
       'high','drawing or diagram',False,True,True,True,'4')
change('P11','P11','Cancelled Sigma formula and surviving final stop',r'\deleted{$\Sigma_{i,j}=\unsure{T}$}',r'\struck{\Sigma_{i,j}=T.}',DELETED_T,
       'The T has its full horizontal roof and vertical stem, both recoverable under the diagonal strike. A separate dark period follows it. The entire formula remains cancelled; C doubt resolves and its omitted stop is restored.',
       'high','misread symbol or index',True,False,False,False,'1')
change('P12a','P12','First V formula: initial subscript separator',r'\mathcal V_{ij}=',r'V_{i,j}=',r'\mathcal V_{i,j}=',
       'An independent short low comma separates i and j in the first subscript, distinct from the descending j. C suppresses that comma.',against_c=True,against_h=False)
change('P12b','P12','First V formula: lower bound',r'\bigcup_{i\leq k<j}',r'\bigcup_{i<k<j}',r'\bigcup_{i\leq k<j}',
       'The first relation has an angled upper stroke and a separate lower bar. The second relation is a plain angle. Thus i<=k<j, without normalization to the nearby strict range.',consequential=True)
change('P12c','P12','First V formula: downward arrow attachment',r"\mathcal V_{ij}=\mathcal V(X_i^*,X_j)\setminus\displaystyle\bigcup_{i\leq k<j}\mathcal V(\unsure{X_i^*|X_i'},X_j)\cap X_k\arrow[r,hook]\arrow[d]&X_j^*\\ X_i^*&",
       r'sous $V_{i,j}$, une flèche descend vers $X_i^{*}$, avec $X$ écrit à gauche',VDIAG,
       'The vertical shaft descends directly from the initial far-left V_i,j to X_i-star. A single long formula cell in C would center it under the whole right-hand side. The revised cells attach it to the initial term and place the separate X to the left of its target.',
       'high','drawing or diagram',True,False,False,True,'4')
change('P12d','P12','Bare X and standalone V_ijk placement',r'X\qquad\mathcal V_{ijk}',r'$X$ écrit à gauche ; $V_{ijk}$ est écrit seul en dessous.',r'X\quad X_i^*'+'; '+r'\noindent $\mathcal V_{ijk}$\par',
       'The full lower half shows bare X left of the downward arrow target; standalone V_ijk sits below and farther right on a separate baseline. They are not a single displayed pair as in C.',
       'high','insertion or placement',True,False,False,False,'6')
change('P13a','P13','Lower diagram: top hook without head',r'\mathcal V_{jk}\arrow[d]\arrow[r,hook]',r"X_k^{*} \arrow[l, hook'] \arrow[d]",r'\mathcal V_{jk}\arrow[d]\arrow[r,hook,no head]',
       'The left endpoint has a curved hook; the shaft reaches rightward without a pointed head at either end. C code supplies a right head and H code a left-directed arrow, although H note explicitly records no point. No direction is inferred from expected maps.',
       'high','drawing or diagram',True,True,True,True,'4')
change('P13b','P13','Lower diagram: dashed diagonal branch and annotation',r'''X_k^*\arrow[d,"\unsure{\sim}"']''',
       r"une flèche en pointillé marquée $r$ part de la flèche verticale $X_k^*\to X_k$ vers la gauche ; son but n'est pas marqué.",LOWER,
       'A diagonal branch has separated dashed segments from the right vertical shaft toward an unlabelled lower-left endpoint. Two short angular strokes at that endpoint are reproduced literally on a no-head dashed path, rather than declaring a standard arrowhead. A nearby wavy continuation and separate lower curve favor tilde but leave r possible. C omits this branch and places its doubtful tilde on the vertical arrow instead. Direction and annotation interpretation remain uncertain; no destination object is supplied.',
       'low','drawing or diagram',True,True,False,True,'4')
change('P13c','P13','Lower diagram: cancelled lower horizontal edge and label',r'\mathcal V(X_j^*,X_k)\arrow[r,"\deleted{\unsure{\sim}}"]',
       'Après $V(X_j^*,X_k)$, une flèche vers $X_k$ est biffée avec un mot illisible.',r'\mathcal V(X_j^*,X_k)\arrow[r,phantom,"\deleted{\xrightarrow{\unsure{\sim}}}" description]',
       'Heavy crossing zigzags pass through the lower horizontal shaft as well as its crowded annotation. The edge is cancelled, not only the label. The label remains explicitly uncertain; neither a complete word nor all strokes of a tilde are secure.',
       'low','deletion state (struck given live or live given struck)',True,True,True,True,'7')
change('P13d','P13','Lower diagram: crossed lower-right X_k',r'\deleted{X_k}',r'V(X_j^{*},X_k) & X_k',r'\deleted{X_k}',
       'The crossing extends across the lower-right X body and index, not only through the shaft approaching it. C cancellation state retained; H code leaves the object live.',
       'high','deletion state (struck given live or live given struck)',False,True,True,False,'7')
change('P14a','P14','Slanted marginal equality',r"\lambda_i'T'=\lambda_i''T''",r"\marginal{\ill{} $=$ \ill{} $\le\Sigma(\lambda',\lambda'')$}",LAMBDA1,
       'Left lambda has a low i stroke and one raised prime. First T has a separate roof and stem; its raised mark has a detached dot and a short curved body, so T-prime is preferred with T-to-i alternative. Right lambda has two raised strokes and no independent lower i; right T has two raised strokes. The literal asymmetry is not regularized.',
       'medium','readable ink left as \\ill{}',True,True,True,True,'5')
change('P14b','P14','Slanted marginal inequality',r"a\leq\operatorname{Inf}(\lambda_i',\lambda_i'')",r"\le\Sigma(\lambda',\lambda'')",LAMBDA2,
       'Initial a is a closed small loop with tail; relation has angle plus lower bar. Operator has I foot, n shoulder and long looped f descender, not Sigma. First argument has one raised prime without a lower i; final argument has one raised prime and a low i-like stroke. No second upper prime is supplied from the equality above.',
       'medium','misread symbol or index',True,True,True,True,'1')
change('P15','P15','Lower thin numeral with underline',r'\margin{6}','',r'\margin{\uline{6}}',
       'Ascending curve turns into a closed lower loop of 6. A separate dark line runs fully underneath it. Hand remains unassigned; C omits underline and H omits mark.',
       'high','omission',True,True,False,False,'3')

decisions=[]
def decision(id,reading,evidence,crop,decision='undecided',confidence='low'):
    decisions.append(dict(id=id,cote='150',scan='7',decision=decision,reading=reading,evidence=evidence,crop=f'crops/150_scan007_{crop}.png',box=BOXES[crop],confidence=confidence))
decision('M0294',r'\Sigma_{012}','Closed 0, distinct upright 1, curved 2 after Sigma at upper junction.','P02','first','high')
decision('M0295',r'c_{01}','Open c, closed lower 0 and separate short 1 beside center.','P02','first','high')
decision('M0296',r"\unsure{\supset d'}",'Hooked long relation-like stroke and d-prime-like group remain inseparable; no secure extra arrow.','P03')
decision('M0297',r'\unsure{i}','Tall upper graph label plus displaced raised stroke remains ambiguous; 1 and 0 elsewhere do not settle it.','P04')
decision('M0298',TUB,'Open circle clearly lies at upper right of Tub, resolving first choice. Separate over-T black mark has uncertain bullet/cancelled-circle state.','P07','first','high')
decision('M0299',r'\bullet','Small filled point is isolated, without recoverable letter strokes, above a clear down arrow to d-prime.','P10','first','medium')
decision('M0300',r"\unsure{X_i^*|X_i'}",'Raised mark is forked rather than a single clean tick; a compact star is favored but prime cannot be excluded. Whole formula and i<=k<j read.','P12')
decision('M0301',r'\unsure{\sim|r}','Wavy annotation belongs to the dashed diagonal branch rather than the right vertical arrow. A V-like endpoint and small lower curve prevent secure letter/sign distinction.','P13')

inventory=[]
def inv(kind,position,text,hand='his hand'):
    inventory.append(dict(scan='150_scan007',sheet_kind='text',hand=hand,element=f'E{len(inventory)+1:02d}',kind=kind,position=position,first_words_or_objects=text,transcribed='yes'))
inv('margin note','top, thin mark',r'\unsure{S|5}','uncertain hand')
inv('drawing','upper left','Disk, three rays, ten labels, central filled point and interior strokes')
inv('margin note','far upper left, rotated',r"\unsure{\supset d'}")
inv('drawing','upper right','Five principal points, crossing segments, two clear arrows, one small dot and labels')
inv('text','three lines below drawings',r'\Sigma_{i_0i_1\ldots i_n}; foncteur contravariant par rapport aux drapeaux variables')
inv('deletion','before live foncteur',r'\unsure{covariant}')
inv('display','first Sigma formula',FORM1)
inv('text','separate mark above T in first Tub',r'\unsure{\bullet|\deleted{\circ}}')
inv('display','second Sigma formula',FORM2)
inv('deletion','before live Tub-bullet',r'\unsure{\partial}')
inv('deletion','after X_j, before live setminus',r'\unsure{\varnothing}')
inv('deletion','union index cluster, upper and middle rows',r'\unsure{k<j};\unsure{i<k|j<k};\unsure{k\ne i}')
inv('insertion','lower union index with curved leader',r'i<k<j')
inv('display','separate range below second formula',r'i<k<j')
inv('margin note','rotated left margin','Square, relation array, cofinaux, separate point-down-arrow-d-prime diagram')
inv('diagram','within rotated margin',MSQUARE)
inv('diagram','within rotated margin below square',MARRAY)
inv('diagram','within rotated margin, separate mini diagram',MPOINT)
inv('deletion','above V formula',r'\Sigma_{i,j}=T.')
inv('diagram','long V formula and downward arrow',VDIAG)
inv('text','left of downward arrow target',r'X')
inv('text','standalone below-left of large lower diagram',r'\mathcal V_{ijk}')
inv('diagram','large lower diagram',LOWER)
inv('deletion','lower horizontal edge, label and right object',r'\xrightarrow{\unsure{\sim}};X_k')
inv('margin note','slanted bottom left',LAMBDA1+'; '+LAMBDA2)
inv('margin note','bottom left, thin underlined mark',r'\uline{6}','uncertain hand')

audit=[]
def aud(kind,box,reading):
    audit.append(dict(box=f'B{len(audit)+1:02d}',kind=kind,xyxy=box,reading=reading))
aud('margin note; handwritten number; less than high confidence departure',BOXES['P01'],r'\unsure{S|5}')
aud('handwritten number; doubtful formula; less than high confidence departure',BOXES['P02'],FIG1)
aud('margin note; doubtful formula',BOXES['P03'],r"\unsure{\supset d'}")
aud('handwritten number; doubtful formula; less than high confidence departure',BOXES['P04'],FIG2)
aud('handwritten number',[244,500,539,610],r'\Sigma_{i_0i_1\ldots i_n}')
aud('struck passage; C/H different words',BOXES['P05'],r'\deleted{\unsure{covariant}}')
aud('C/H different words; handwritten number; doubtful formula; less than high confidence departure',[755,493,1334,676],r'foncteur contravariant par rapport aux drapeaux variables $'+TUPLE+'$')
aud('doubtful formula; less than high confidence departure',BOXES['P07'],FORM1)
aud('doubtful formula; struck passage; insertion; less than high confidence departure',BOXES['P08'],FORM2)
aud('margin note (rotated writing only); doubtful formula; less than high confidence departure',[43,763,430,1168],MARGIN)
aud('struck passage',BOXES['P11'],r'\deleted{\Sigma_{i,j}=T.}')
aud('doubtful formula',[250,1280,1490,1618],VDIAG.replace('X&X_i^*','&X_i^*'))
aud('diagram annotation; placement',[130,1530,195,1620],r'X')
aud('diagram annotation; placement',[265,1700,430,1820],r'\mathcal V_{ijk}')
aud('doubtful formula; struck passage; less than high confidence departure',BOXES['P13'],LOWER)
aud('margin note; doubtful formula; less than high confidence departure',BOXES['P14'],LAMBDA1+'; '+LAMBDA2)
aud('margin note; handwritten number',BOXES['P15'],r'\uline{6}')

doubts=[
 dict(place='P01 upper thin mark',reading=r'\unsure{S|5}',alternatives='S | 5',confidence='low',reason='Smooth S-like curve lacks a secure angular 5 bar; hand and foliation function uncertain.'),
 dict(place='P03 rotated fragment',reading=r"\unsure{\supset d'}",alternatives='superset d-prime | unresolved short relation fragment',confidence='low',reason='Overlapping long hooked stroke and compact raised material do not separate securely.'),
 dict(place='P04 upper graph label',reading=r'\unsure{i}',alternatives='i | unresolved label',confidence='low',reason='Displaced raised curve and tall stroke do not establish another complete label.'),
 dict(place='P04 small one-sided branches',reading='geometric strokes with no extra directed arrows',alternatives='arrowhead remnants | pen returns',confidence='medium',reason='Each has one branch only; paired head strokes are not visible.'),
 dict(place='P05 cancelled word',reading=r'\deleted{\unsure{covariant}}',alternatives='covariant | unreadable cancelled word',confidence='low',reason='Several tall internal strokes and cancellation prevent every letter being recovered.'),
 dict(place='P06 tuple interior',reading=r'\unsure{{:}\ldots|i_1\ldots}',alternatives='colon-like group with low ellipsis | i_1 with ellipsis',confidence='low',reason='Five separate marks; no secure i stem or subscript 1.'),
 dict(place='P07 separate over-T mark',reading=r'\unsure{\bullet|\deleted{\circ}}',alternatives='live filled mark | cancelled circle',confidence='low',reason='Black overtracing alone does not establish deletion state.'),
 dict(place='P08 cancelled pre-Tub symbol',reading=r'\deleted{\unsure{\partial}}',alternatives='partial | unresolved cancelled symbol',confidence='low',reason='Crossing obscures part of the looped body.'),
 dict(place='P08 cancelled post-X_j symbol',reading=r'\deleted{\unsure{\varnothing}}',alternatives='empty-set-like token | unresolved cancelled symbol',confidence='low',reason='Small crossed loop has insufficient independent strokes for resolution.'),
 dict(place='P08 cancelled index groups',reading=RANGE,alternatives='k<j; i<k|j<k; k-not-equal-i under strikes',confidence='low',reason='The new right group has a first stroke overlaid by a return, leaving i/j unresolved; other crossed groups remain doubtful.'),
 dict(place='P10 lower-left array label',reading=r'\unsure{\delta|d}',alternatives='delta | d',confidence='low',reason='Lower body is d-like; the cropped extent does not securely distinguish delta from d. No extra left vertical cap is supported.'),
 dict(place='P12 second X_i exponent',reading=r"\unsure{X_i^*|X_i'}",alternatives='star | prime',confidence='low',reason='Raised mark has a fork, not a secure single tick; neighboring clear stars do not resolve it.'),
 dict(place='P13 dashed branch annotation',reading=r'\unsure{\sim|r}',alternatives='tilde/wave | r',confidence='low',reason='V-like endpoint with wavy continuation and a lower curved stroke remains ambiguous; attachment to branch retained.'),
 dict(place='P13 dashed branch endpoint',reading='no-head dashed shaft with two literal short angular strokes at lower-left endpoint',alternatives='arrowhead | local pen strokes',confidence='low',reason='The visible V-like geometry does not establish a semantic directed arrow with certainty. No destination object is supplied.'),
 dict(place='P13 cancelled lower-edge annotation',reading=r'\deleted{\unsure{\sim}}',alternatives='wave-like symbol | unresolved cancelled annotation',confidence='low',reason='Heavy zigzags obscure both label and shaft; not every underlying stroke is recoverable.'),
 dict(place='P14 first T raised mark',reading=r"\unsure{T'|T^i}",alternatives='T-prime | T-to-i',confidence='low',reason='Detached upper dot and short curved body differ from the other straight prime strokes. Prime is preferred but not forced.'),
]

notes=[
 dict(id='N01',text='The sheet contains two upper drawings, a flag-indexed contravariant construction, two Sigma formulas with revisions, cofinal marginal diagrams, a V formula and lower diagram, and a slanted marginal parameter equality/inequality. No theorem verification has been performed by this reader. The line_count of 13 counts main prose/formula/object baselines, excluding figure labels, interlinear corrections and marginal material.'),
 dict(id='N02',text='The live phrase is "foncteur contravariant par rapport aux drapeaux variables". The nearby cancelled word remains uncertain. Cofinality is stated only by the marginal word "cofinaux"; no unstated direction or universal property has been added.'),
 dict(id='N03',text='The Sigma formulas use the strict range k<i or i<k<j. The later V formula visibly uses i<=k<j. This difference is retained, as is its unresolved star/prime exponent; the formulas are not regularized into one convention.'),
 dict(id='N04',text='The lower top connector has a left hook and no head. The dashed diagonal branch starts from the right vertical edge and has no labelled destination object. Its annotation and the struck lower-edge annotation remain uncertain. No mathematical map is supplied to fill the missing destination.'),
 dict(id='N05',text='The thin top S|5 and underlined lower 6 are transcribed as marginal marks, with hand unassigned. C treated the top mark as author foliation; that attribution is not established from this leaf. H final section heading is editorial, not ink on this page.'),
 dict(id='N06',text='The bottom marginal formulas retain asymmetric subscript/prime placement as seen, rather than supplying symmetric indices. The operator reads Inf, not Sigma. The quantities are not defined on this leaf.'),
 dict(id='N07',text='Crops P03 and P10 were initially viewed in an upside-down text orientation and read mentally; their saved files were then deterministically rotated 180 degrees without rereading. P14/P15 were displayed individually after a multi-image output omitted them. P06 was reopened only for the newly identified tuple sub-place. P16 completes the clipped lower extent of the rotated margin. The main-text Sigma_(i,j) at its right is not a marginal object. The relation array has only a right vertical cap; no left cap is supplied.'),
]

notation=[
 dict(form=r'\Sigma_{i_0i_1\ldots i_n}',meaning='Flag-indexed Sigma construction called contravariant in the live prose.',evidence='150_scan007, prose immediately below upper drawings.'),
 dict(form=r"\Sigma_i=X_i'",meaning='Equality written at the start of the first Sigma formula.',evidence='150_scan007 P07.'),
 dict(form=r'\operatorname{Tub}^{\circ};\operatorname{Tub}^{\bullet}',meaning='Distinct open-circle and filled-dot decorations of Tub on this leaf; the additional over-T mark is unresolved.',evidence='150_scan007 P07/P08; no definition of the decorations on this leaf.'),
 dict(form=r'\mathcal V',meaning='V-like mathematical operator and indexed objects used in the lower formulas/diagram; not newly defined here.',evidence='150_scan007 P12/P13.'),
]
abbreviations=[dict(form='Inf',expansion='infimum (operator; source spelling retained)')]
hand=[
 dict(habit='A single i tittle can sit high and to the right like a prime.',places='150_scan007 P06 tuple endpoints.',consistency='Both endpoint i letters have one such raised stroke; no second prime stroke.',witness_errors='H reads both as primed i.'),
 dict(habit='Compact k indices can have an n-like right shoulder.',places='150_scan007 P12 X_k and P13 V_ijk.',consistency='Clearer k forms coexist on the same page; variation, not a universal substitution rule.',witness_errors='No independent witness correction is asserted from this habit alone.'),
 dict(habit='Heavy retracing does not by itself indicate cancellation.',places='150_scan007 P07 inner X_i and separate dark mark above Tub.',consistency='Inner X_i has one body; upper black mark chronology remains open.',witness_errors='Neither witness fully preserves both Tub decorations.'),
 dict(habit='Short pen branches and gaps occur in genuine drawings.',places='150_scan007 P02/P04.',consistency='One-sided return branches lack paired arrowheads; white holes occur within filled blobs.',witness_errors='C regularizes thick boundary and joins a horizontal gap; H omits labels and fine strokes.'),
]

coverage={
 1:'P01: top mark S|5, S favored; scan macro not source ink.',
 2:'Editorial prose versus TikZ syntax; upper drawing reconstructed at P02c.',
 3:'Drawing wrapper/macro difference; actual geometry covered by P02c.',
 4:'P02c: open thick arc plus thin right boundary, rather than thick closed cycle.',
 5:'P02a/P02b/P02c: all labels, center, rays and interior strokes read.',
 6:'TikZ coordinate syntax, not source text; central label retained.',
 7:'TikZ coordinate syntax versus H description; c01 resolved P02b.',
 8:'Same labels, different representation; P02c retains placement.',
 9:'Coordinate tokens are not source digits; label positions in P02c.',
 10:'Both Sigma012 occurrences retained; upper doubt resolves P02a.',
 11:'H descriptive punctuation is editorial, not source ink.',
 12:'Three rays and Sigma12/Sigma1/Sigma12 retained P02c.',
 13:'Coordinate-only tokens.',
 14:'Coordinate-only tokens; lower junction label retained.',
 15:'Coordinate-only tokens; all ten figure labels retained.',
 16:'P03 unresolved rotated fragment omitted by H; diagram wrapper difference otherwise.',
 17:'Drawing scale syntax versus editorial positioning prose.',
 18:'Upper figures rebuilt P02c/P04b; Sigma2 read in drawing.',
 19:'P04a: upper label i remains uncertain.',
 20:'P04a/P04b: five principal blobs and readable 1/0 labels, all geometry.',
 21:'P04a: lower 0 retained; remaining coordinate tokens not source text.',
 22:'P05 and P06a: cancelled covariant stays doubtful; live foncteur contravariant.',
 23:'P06b: aux drapeaux variables.',
 24:'P06c: unprimed i0; P06d logs internal five-mark cluster.',
 25:'P06c: unprimed in.',
 26:'Same Xi-prime, prime attachment macro variant.',
 27:'Same Xi-prime, prime attachment macro variant.',
 28:'P07a/P07b: right open circle and separate uncertain over-T mark.',
 29:'P07a resolves circle placement; extra over-T state remains doubtful.',
 30:'P08a: cancelled partial candidate remains unresolved.',
 31:'Same Xi-prime, macro variant.',
 32:'Same Xi-prime and comma, macro/spacing variant.',
 33:'P08b/P08c: post-Xj crossed token, full cancelled ranges and live insertion.',
 34:'Same Xj-prime, prime attachment macro variant.',
 35:'Same Xj-prime, prime attachment macro variant.',
 36:'P08c: crossed index cluster and live inserted range; H note is editorial description.',
 37:'Separate repeated i<k<j retained; rotated square begins afterwards in C.',
 38:'P10a/P10b/P10c/P10d: relation array, cofinaux, mini diagram, and explicit square orientation/arrows; P11 struck formula elsewhere.',
 39:'P11: T resolved and independent period retained.',
 40:'TikZ spacing syntax only.',
 41:'P12a: initial subscript comma retained.',
 42:'P12b: i<=k<j, distinct lower bar.',
 43:'M0300 undecided, star|prime retained; H star is the first candidate. Certainty-only difference recorded in doubts.',
 44:'P12c: hook right and vertical arrow from initial V term.',
 45:'P12c: downward target Xi-star; same content as H note.',
 46:'P12c/P12d: separate bare X at left of target.',
 47:'P12d: bare X position retained.',
 48:'P12d: standalone Vijk below on its own baseline.',
 49:'TikZ spacing syntax only.',
 50:'P13a: top hook connector without head.',
 51:'P13a: H code direction not imposed; H note recognizes no point.',
 52:'P13b and M0301: annotation moved to dashed diagonal branch, still uncertain.',
 53:'P13c/P13d: lower horizontal edge, annotation and right Xk are cancelled.',
 54:'P13b/P13c and P14a: H explanatory note versus source placement; no note prose copied.',
 55:'P10 margin and P13 branch/edge read; bottom formulas P14a/P14b, not H editorial notes.',
 56:'P14a: equality read literally, no supplied RHS lambda index.',
 57:'P14b: Inf, not Sigma.',
 58:'P14b: first lower lambda lacks a secure i index.',
 59:'P14b: literal argument primes; final H section heading is editorial.',
 60:'P14b/P15: final lambda marks literal; underlined6 retained. H final heading not source ink.'
}
diff_rows=list(csv.DictReader((ROOT/'packets/150_scan007/differences.tsv').open(),delimiter='\t'))
assert len(diff_rows)==len(coverage),(len(diff_rows),len(coverage))

reviews=[
 dict(text=r'\deleted{\unsure{covariant}}',scope_attachment='Only the word before live foncteur is struck.',evidence='P05 strike crosses its bodies; live foncteur starts after the crossed group.'),
 dict(text=r'\unsure{\bullet|\deleted{\circ}}',scope_attachment='Separate over-T mark; cancellation state remains unresolved, independent from live open upper-right circle.',evidence='P07 filled/overtraced black mark and separate hollow circle; no secure chronology.'),
 dict(text=r'\deleted{\unsure{\partial}}',scope_attachment='Only pre-Tub symbol cancelled; Tub-bullet is live.',evidence='P08 crossing localized before T.'),
 dict(text=r'\deleted{\unsure{\varnothing}}',scope_attachment='Small old token after X_j is crossed; following broad setminus remains live.',evidence='P08 distinct crossed loop versus separate live slash.'),
 dict(text=RANGE,scope_attachment='Three old groups struck; upper-right group sits beside k<j. Lower clear i<k<j is inserted under union with curved leader.',evidence='P08 crossings intersect old bodies; lower range has no independent cancellation, leader turns toward union.'),
 dict(text=DELETED_T,scope_attachment='Whole Sigma_i,j=T. formula cancelled, with independent period.',evidence='P11 diagonal line traverses formula; all T strokes and separate stop are visible.'),
 dict(text=r'\deleted{\xrightarrow{\unsure{\sim}}}',scope_attachment='Lower horizontal edge and crowded annotation cancelled together.',evidence='P13 zigzags pass across shaft and label, not only label.'),
 dict(text=r'\deleted{X_k}',scope_attachment='Lower-right object crossed; vertical arrow above remains separately live.',evidence='P13 cancellation reaches X body and index; do not infer cancellation of vertical edge.'),
]

report=dict(page='150_scan007',reader='reader_b',line_count=13,changes=changes,decisions=decisions,
            inventory=inventory,audit_boxes=audit,doubts=doubts,notes=notes,check_events=[],
            notation=notation,abbreviations=abbreviations,hand=hand,
            diff_coverage=[dict(row=i,disposition=coverage[i]) for i in sorted(coverage)],
            deletion_insertion_review=reviews)

for d in decisions:
    assert d['reading'] in DRAFT,(d['id'],d['reading'])
for x in changes:
    assert (ROOT/'work'/x['crop']).exists()
for x in audit:
    a,b,c,d=x['xyxy']; assert 0<=a<c<=1712 and 0<=b<d<=2303,x

(OUT/'draft.tex').write_text(DRAFT)
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'marks':len(decisions),'inventory':len(inventory),'audit_boxes':len(audit),'differences':len(coverage),'crops':len(BOXES)}))
