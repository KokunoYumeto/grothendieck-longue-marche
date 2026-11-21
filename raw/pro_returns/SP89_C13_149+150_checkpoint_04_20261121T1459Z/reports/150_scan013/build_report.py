from pathlib import Path
import csv,json,re
R=Path('/workspace/scratch/8759b8008681')
P='150_scan013'
out=R/'work/reports'/P
C=(R/'packets'/P/'C.tex').read_text()
H=(R/'packets'/P/'H.tex').read_text()
D=(out/'draft.tex').read_text()
boxes=json.loads((out/'crop_boxes.json').read_text())
changes=[]
def ch(id,place,c,h,final,evidence,confidence='high',kind='misread symbol or index',against_c=True,against_h=False,marked_in_h=False,consequential=False):
    cat={'misread symbol or index':1,'misread word':2,'omission':3,'drawing or diagram':4,'readable ink left as \\ill{}':5,'insertion or placement':6,'deletion state (struck given live or live given struck)':7,'abbreviation expanded or spelling modernised':8,'text not on the page':9,'other':10}[kind]
    crop=id.split('_')[0]
    changes.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,crop=f'crops/{P}_{crop}.png',box=boxes[crop],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,marked_in_h=marked_in_h,consequential=consequential,error_category=cat))
ch('P01_a','Old parenthesized number and cancelled Soit T',r'\deleted{$(\unsure{6})$ Soit $\bar T$}',r'(6) \struck{Soit $T$}',r'\unsure{\deleted{(6)}|(6)} \deleted{Soit $T$}',
   'The old numeral has looped and diagonal overwork separate from the horizontal stroke through Soit T. Its state is not established by blackness; the first alternative retains cancellation, with live-number alternative explicit. The T has one cap and a stem; the crossing stroke is the cancellation, not an additional overbar.', 'medium','deletion state (struck given live or live given struck)',True,True)
ch('P02_a','NB first indexed T and closed interval',r'\uline{NB} Les $\bar T_\lambda$ $(\lambda\in[0,1])$',r'\emph{NB} Les $T_\lambda$ ($\lambda\in[0,1]$)',r'\uline{NB} Les $T_\lambda$ $(\lambda\in[0,1])$',
   'The first T has a single long cap and a detached descending stem. No second horizontal stroke lies above it. Both square endpoints and the digits 0,1 are visible. NB has one underline.')
ch('P02_b','T after parties fermées de',r'parties fermées de $\bar T$',r'parties fermées de $T$',r'parties fermées de $T$',
   'The cap over this T is the sole horizontal member of the letter; the separate hollow circles on the following T forms provide a local comparison for genuine added marks.')
ch('P02_c','First interior definition, label and cancelled subscript',r'\mathring T_\lambda\overset{\mathrm{déf}}= \lambda\mathring T\deleted{\unsure{_\lambda}}',r'\overset{\circ}{T}_\lambda\overset{\text{déf}}{=}\lambda\overset{\circ}{T}',r'\mathring T_\lambda\overset{\mathrm{def}}= \lambda\mathring T\deleted{\unsure{_\lambda}}',
   'Both upper circles are hollow. A small crossed group follows the right T at subscript height; lambda remains a candidate under the dense crossing and is not resolved. The raised label has joined d/e bodies and a long f descender, with no separate acute over e. The descending f is not another mathematical symbol.', 'medium','omission',True,True)
ch('P03_a','Interior clause and topologique attachment',r"l'intérieur \inserted{topologique} de $\bar T_\lambda$ dans $\bar T$",r"l'intérieur \add{topologique} \struck{de} $T_\lambda$ dans $T$",r"l'intérieur \inserted{topologique} de $T_\lambda$ dans $T$",
   'The raised word has the t/o/p/o/l/o/g/i/q/u/e sequence. Its lower curve runs back as an attachment leader above and beside de; no independent strike through de is isolated. Both ordinary T forms have only their own cap strokes.', 'high','deletion state (struck given live or live given struck)',True,True)
ch('P03_b','Inserted top. and following T1',r'\inserted{top.} de $\bar T_1$ dans',r'\add{top.} de $T_1$ dans',r'\inserted{top.} de $T_1$ dans',
   'The small top. is raised and attached by a slanted leader before de. Its abbreviated ending and stop are retained. T1 has one cap and a lowered single upright 1, without an additional bar.')
ch('P04_a','T1=T after espace topologique',r"l'espace topologique $\bar T_1=\bar T$",r"l'espace topologique $T_1=T$",r"l'espace topologique $T_1=T$",
   'Each of the two T forms has one cap; the first has a clear lowered 1. The ordinary letters lack the separate upper circle or filled dot seen nearby.')
ch('P04_b','Overworked subscript after on n’a pas',r'\mathring T\deleted{\unsure{_1}}=\bar T',r'\overset{\circ}{T}_1=T',r'\mathring T\unsure{\deleted{_1}|_1}=T',
   'The interior circle is hollow, and the final T is plain. The lowered group at the first T contains a short upright and several dark loops, compatible with 1 but with no secure independent cancellation stroke. The preferred cancelled state and the live alternative are both retained.', 'medium','deletion state (struck given live or live given struck)',True,True)
ch('P04_c','Sauf, empty-set glyph, and Y=T',r'sauf si $\dot T=\varnothing$ i.e. $Y=\bar T$.',r'\uncertain{sauf} si $\dot T=\emptyset$ i.e. $Y=T$.',r'sauf si $\dot T=\phi$ i.e. $Y=T$.',
   'Sauf has a low s/a/u run followed by the tall descending f. The empty-set glyph is an oval crossed by a long slanted stem, hence phi as written. The boundary dot is filled and the final T has only its own cap.', 'high','misread symbol or index',True,True,True)
ch('P05_a','Current brace-definition number',r'(\unsure{6})\qquad',r'\left\lbrace \begin{array}{l}',r'(\unsure{6})\qquad',
   'A parenthesized, overworked numeral stands at the left of the brace. Its loop favours 6 but superposed strokes prevent certainty or recovery of an earlier digit. H supplies no number at this location; the separate old top number does not replace this ink.', 'medium','omission',False,True)
ch('P05_b','First row of thickening definition',r'\bar T\setminus\mathring T_\lambda &\overset{\mathrm{déf}}=\deleted{\unsure{E}} \mathrm{Ep}^{(T)}_{1-\lambda=\varepsilon}',r'T\setminus\overset{\circ}{T}_\lambda\overset{\text{déf}}{=}E_{1-\lambda=\varepsilon}(T)',r'T\setminus\mathring T_\lambda &\overset{\mathrm{def}}=\deleted{\unsure{E}} \mathrm{Ep}^{(T)}_{1-\lambda=\varepsilon}',
   'The left T is plain. A heavily crossed E-like predecessor remains before the live Ep; its letter is not resolved. The live p has a distinct long descender. The lowered index reads 1-lambda=epsilon. (T) is raised relative to that index and slightly above the main Ep baseline; superscript placement is preferred, with geometric uncertainty noted. This def label has no separate acute.', 'medium','misread symbol or index',True,True,False,True)
ch('P05_c','Quoted thickening description and de T',r'\quad\text{``épaississement d\'indice $\varepsilon$\'\'}\\ &\hspace{4em}\text{du bord $\dot T$ de $\bar T$}',r'« épaississement d\'indice $\varepsilon$ » du bord $\dot T$ dans $T$',r'\quad\text{``épaississement d\'indice $\varepsilon$\'\'}\\ &\hspace{4em}\text{du bord $\dot T$ de $T$}',
   'The quotation marks are paired upper ticks. After bord and dotted T, the short joined d/e is visible; it does not contain the additional a/n/s of dans. The final T has a single cap. The annotation is to the right of the first row, with du bord continued below it.', 'high','misread word',True,True)
ch('P05_d','Complete lower thickening-boundary row',r'\dot{\mathrm{Ep}}_\varepsilon^{(T)} &\overset{\mathrm{déf}}=\dot T\unsure{\amalg|\cup}(1-\varepsilon).\dot T',r'\dot E_\varepsilon(T)\overset{\text{déf}}{=}\dot T\cup(1-\varepsilon)\dot T',r'\dot{\mathrm{Ep}}_\varepsilon^{(T)} &\overset{\mathrm{déf}}=\dot T\unsure{\amalg|\cup}(1-\varepsilon).\dot T',
   'A separate filled oval above the E upper arm (original about 598,1197) supplies the dot; the arm itself is not that dot. The p descends below the lowered epsilon. A small detached stroke above e supports the accent in this label. The union-like sign has an overtraced U body and short left foot, leaving amalg/cup unresolved. There is a separate multiplication point after the closing parenthesis. (T) is raised relative to epsilon.', 'medium','misread symbol or index',False,True,False,True)
ch('P06_a','Frontier prose ambient T',r'La frontière de $E_\varepsilon$ dans $\bar T$ est',r'La frontière de $E_\varepsilon$ dans $T$ est',r'La frontière de $E_\varepsilon$ dans $T$ est',
   'The ambient T has one cap and stem, with no overbar. Both prose E_epsilon forms lack the p visible in the adjacent displayed Ep; this local notational variation is preserved.')
ch('P06_b','Formula (7), Ep and raised parenthesized T',r'(7)\qquad\mathrm{Ep}_\varepsilon^{(T)} \simeq[\underbrace{1-\varepsilon}_{\lambda},1]\times\dot T',r'(7)\qquad E_\varepsilon(T)\simeq[\underbrace{1-\varepsilon}_{\lambda},1]\times\dot T',r'(7)\qquad\mathrm{Ep}_\varepsilon^{(T)} \simeq[\underbrace{1-\varepsilon}_{\lambda},1]\times\dot T',
   'The displayed p has a long descending stem beside E. (T) is above the low epsilon and is retained as a superscript, with baseline-argument placement a geometric alternative. The 7, two square endpoints, both written 1s, underbrace lambda, multiplication cross and filled dot above the last T are all visible.', 'medium','misread symbol or index',False,True)
ch('P07_a','Marginal opening Y, inserted dotted T, compacts',r'\uline{NB} Si $Y,\dot T$ \unsure{compacts}',r'\emph{NB} Si \struck{$\dot T$} $Y$ (\uncertain{ou} \ill{})',r'\uline{NB} Si $Y,\inserted{\dot T}$ compacts',
   'The comma follows Y. A dotted T is raised after it, with a curved attachment leader around the following word; its cap is intrinsic, with no independent cancellation. Compacts has c/o/m, a descending p, then a/c/t and final s. This resolves C’s word doubt at medium confidence and preserves the insertion.', 'medium','insertion or placement',True,True,True)
ch('P07_b','Marginal cancelled predecessor and compact conclusion',r'\deleted{\unsure{les}} alors $\bar T$ compact, et les $\bar T_\varepsilon$',r'les $T_\varepsilon$',r'\deleted{\unsure{les}} alors $T$ compact, et les $T_\varepsilon$',
   'The small l/e/s-like group before alors is crossed and remains uncertain. Alors has a tall looped l followed by low o/r/s; compact has its descending p and terminal t. The two T forms have single caps. H omits the compact conclusion and the crossed predecessor.', 'medium','omission',True,True)
ch('P07_c','Marginal interval right endpoint',r'(\varepsilon\in]0,1\unsure{[|]})',r'($\varepsilon\in\,]0,1]$)',r'(\varepsilon\in]0,1])',
   'The right upright has both its upper and lower feet extending left. Despite retracing of the upright, these feet support a closing ] rather than [. The complete epsilon membership, 0,1 and surrounding parenthesis were read together.', 'medium','misread symbol or index',True,False)
ch('P07_d','Marginal fundamental-system phrase',r'un syst. fond. de voisinages de $Y$ dans $\bar T$',r'\uncertain{un} \ill{} \uncertain{de} voisinages de $Y$ dans $T$',r'un syst. fond. de voisinages de $Y$ dans $T$',
   'The genuine un is at the far left of this transverse note (original about 31,1973), outside the main-text area. Syst. and fond. each end in a separate stop; fond. has the long f and a final d stem. Voisinages, Y and dans are readable, and T has one cap. Apparent additional material near forment belongs to the main formula number and is excluded.', 'medium','readable ink left as \\ill{}',True,True,True)
ch('P07_e','Marginal fermés/ouverts revision',r'\deleted{fermés}\inserted{\unsure{ouverts}}.',r'(\struck{\ill{}}) \uncertain{\ill{}}',r'\deleted{\unsure{fermés}}\inserted{ouverts}.',
   'The baseline word is crossed; its f and ending are compatible with fermés but the crossing obscures interior letters, so a new local doubt is retained. Above it, ouverts has an open o, u/v run, e/r, tall t and final s. Its raised position makes it the replacement. No literal parenthesis pair surrounds the cancellation.', 'medium','readable ink left as \\ill{}',True,True,True)
ch('P07_f','Additional marginal fragment below syst. fond.',r'\inserted{\unsure{ouverts}}. (\unsure{ainsi que voisinages}',r'(\struck{\ill{}}) \uncertain{\ill{}} \uncertain{tubulaires}',r'\unsure{plus|plein} : $T$',
   'Below syst. fond. and before the lower parenthetical line is a live short word with descending p and ascending l, followed by compressed low bodies. Plus is preferred to plein; the letters do not securely settle it. Two separated points form a colon, followed by an ordinary T with one cap. The fragment is preserved at that line without assigning a semantic attachment.', 'low','omission',True,True,True,True)
ch('P07_g','Marginal parenthetical ending; removal of spurious T_epsilon',r'(\unsure{ainsi que voisinages} $\unsure{\bar T_\varepsilon}$ tubulaires absolus de $Y$)',r'\uncertain{tubulaires}',r'(\unsure{ainsi que voisinages} tubulaires absolus de $Y$)',
   'The opening parenthesis, a compressed ainsi/que run and voisinages remain locally doubtful, partly interrupted in the frame by adjacent main text. Tubulaires has tall b/l bodies and the compressed aires ending; absolus de Y and the closing parenthesis are clear. C’s alleged T_epsilon after voisinages maps to the separately transcribed main-text underlined NB at about original 269,1351; it is not a second marginal symbol.', 'medium','text not on the page',True,True,True,True)
ch('P08_a','Circled section number',r'\textcircled{2} Soit',r'(2) Soit',r'\textcircled{2} Soit',
   'The 2 is enclosed by a continuous closed circular outline, not by two separated parentheses. The small terminal bulge touches the circle and is not treated as a separate full stop.', 'high','misread symbol or index',False,True)
ch('P08_b','Hooked unheaded inclusion connector',r'$Y\hookrightarrow X$',r'$Y\hookrightarrow X$',r'$Y\lhook\joinrel\relbar X$',
   'The connector has a curved source hook joining a short horizontal shaft. Its right end stops bluntly before X; no two-arm arrowhead is visible. The missing head is preserved without supplying one from the word inclusion.', 'high','misread symbol or index',True,True,False,True)
ch('P08_c','Definition underline scopes',r'\uline{voisinage conique} de \uline{$Y$ dans} $X$',r'\emph{voisinage conique de $Y$ dans $X$}',r'\uline{voisinage conique} de \uline{$Y$ dans} $X$',
   'The first underline begins under voisinage and ends after conique, before de. A separate lower-line stroke covers Y dans and stops before X. Un and the final X are not included.', 'high','other',False,True)
ch('P08_d','T in the ambient-neighbourhood definition',r'est un voisinage $\bar T$ de $Y$ dans $X$',r'est un voisinage $T$ de $Y$ dans $X$',r'est un voisinage $T$ de $Y$ dans $X$',
   'The central T is formed by one long cap and a vertical stem; there is no second horizontal overbar.')
ch('P09_a','Operation (1), interval I and unheaded action shaft',r"muni d'une opération (1) $I\times\bar T\longrightarrow\bar T$",r"muni d'une opération (1) $\mathbf{I}\times T\to T$",r"muni d'une opération (1) $I\times T\mathrel{\relbar\joinrel\relbar}T$",
   'The label is a parenthesized 1. I has one thin stem with short top and bottom serifs, rather than a doubled or heavily filled body. Both Ts have their own single caps. The action connector is a single horizontal shaft ending in a blunt tip, with no secure arrowhead.', 'high','misread symbol or index',True,True,False,True)
ch('P09_b','Live raised replacement and nested tub./coniq. revision',r'\inserted{faisant de $\bar T$ un vois. \deleted{tub.}\inserted{coniq.} absolu de $Y$.}',r'\struck{faisant de $T$ un vois.} \add{conique} \struck{\ill{}} \struck{absolu de $Y$}',r'\inserted{faisant de $T$ un vois. \deleted{tub.}\inserted{coniq.} absolu de $Y$.}',
   'Faisant de T un vois. and absolu de Y lie above the long cancellation of the old baseline and are live. Only the short tub. group is crossed within this replacement; coniq. is placed above it with a bent leader. The latter ends in a descending q and short stop, without the full u/e continuation of conique. T has one cap, and the final stop after Y is visible.', 'medium','deletion state (struck given live or live given struck)',True,True,True,True)
ch('P09_c','Cancelled conditions ending',r'\deleted{satisfaisant les conditions id.}',r'\struck{satisfaisant les conditions dites.}',r'\deleted{satisfaisant les conditions \unsure{dites.|id.}}',
   'The long baseline stroke crosses satisfaisant les conditions and the final word. That ending extends over several low bodies to a final stop, favouring dites. over the shorter id.; overlaps with the raised words obscure individual loops, so the reading remains explicit uncertainty.', 'medium','misread word',True,False)
ch('P10_a','Family lambda T=T_lambda',r'$\lambda\bar T=\bar T_\lambda$ $(\lambda\in]0,1])$',r'$\lambda T=T_\lambda$ ($\lambda\in\,]0,1]$)',r'$\lambda T=T_\lambda$ $(\lambda\in]0,1])$',
   'Both ordinary T forms have one cap. The lambda subscripts and the membership interval with left-open/right-closed endpoints are visible. The following word tubulaires has a tall b and l and is retained literally despite the earlier coniq. revision.', 'high','misread symbol or index',True,False,False,True)
ch('P10_b','Final asserted ambient frontier, ordinary T forms',r'\quad\text{est la frontière de }\bar T_\lambda=\lambda\bar T\text{ dans }X.',r'est la frontière de $T_\lambda=\lambda T$ dans $X$.',r'\quad\text{est la frontière de }T_\lambda=\lambda T\text{ dans }X.',
   'The source explicitly says est la frontière de T_lambda=lambda T dans X, with a final stop. The two T forms on the right have only their cap strokes; the two boundary T forms on the left have separate filled dots. The initial lower lambda meets the physical sheet edge; P12 adds only the black scanner border, no missing continuation.', 'high','misread symbol or index',True,False,False,True)
ch('P11_a','Thin lower-left foliation',r'\margin{12}',r'\note{Le numéro « (8) » est surchargé ; on lit aussi « absolu de $Y$ » dans la ligne biffée, dont « conique » est ajouté au-dessus.}',r'\margin{12}',
   'The pale thin hand writes a slanted-topped 1 followed by a curved 2 with a lower foot. H gives no source transcription of this foliation. Its hand is not identified as the author’s.', 'high','omission',False,True)

# Repair quotation strings represented above using Python raw literal escapes.
for row in changes:
    for k in ('c','h','final'):
        row[k]=row[k].replace("\\'", "'")

def decision(id,reading,evidence,crop,decision='undecided',confidence='medium'):
    return dict(id=id,cote='150',scan='13',decision=decision,reading=reading,evidence=evidence,crop=f'crops/{P}_{crop}.png',box=boxes[crop],confidence=confidence)
decisions=[
 decision('M0317',r'(\unsure{6})','The current left number has a looped 6-like body under overwork; no unique clean digit or prior state is recoverable. This is separate from the old top number.','P05'),
 decision('M0318',r'\dot{\mathrm{Ep}}_\varepsilon^{(T)} &\overset{\mathrm{déf}}=\dot T\unsure{\amalg|\cup}(1-\varepsilon).\dot T','The whole lower row was read. The U-like union body is heavily filled and has a short left foot; neither amalg nor cup can be excluded. The Ep dot, p descender, epsilon, raised (T), both dotted Ts and multiplication point are retained.','P05'),
 decision('M0319','compacts','The word has c/o/m, a descending p, a/c/t and a terminal s. No letters require grammatical completion.','P07','first','medium'),
 decision('M0320',r'(\varepsilon\in]0,1])','Both feet of the right interval bracket extend left from its upright, supporting ] despite retracing of the upright.','P07','alternative','medium'),
 decision('M0321',r'\inserted{ouverts}','The raised replacement has open o, u/v, e/r, tall t and final s above the crossed baseline word.','P07','first','medium'),
 decision('M0322',r'\unsure{ainsi que voisinages}','The compressed opening and portions of the voisinages run are obscured/overlapped; the source supports the C candidate but does not expose every letter sufficiently for resolution.','P07'),
 decision('M0323',r'\unsure{ainsi que voisinages} tubulaires','No separate T_epsilon belongs between these words. Inverse mapping of the apparent group places it at the main-text underlined NB (P06, original about 269,1351), already transcribed there. A different genuine T occurs before the parenthesis in the plus/plein fragment.','P07','other','high')
]

inventory=[]
def inv(element,kind,position,first,hand='his hand'):
    inventory.append(dict(scan=P,sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('E01','deletion','Top first baseline; P01','2. Soit X un espace, Y un sous-espace fermé.')
inv('E02','deletion','Top old-number fragment; P01','Old (6), state uncertain; Soit T cancelled')
inv('E03','text','Upper NB; P02–P04','NB Les T_lambda; increasing closed/open families and interior caveat')
inv('E04','deletion','First interior definition; P02','Crossed doubtful lambda subscript after lambda circleT')
inv('E05','margin note','Left of upper interior paragraph; P03','Two vertical emphasis strokes')
inv('E06','insertion','Above first interior statement; P03','topologique')
inv('E07','insertion','Above second interior statement; P03','top.')
inv('E08','deletion','After on n’a pas; P04','Subscript 1 with uncertain cancellation state')
inv('E09','text','Above central brace; P05','Posons, pour lambda in ]0,1[')
inv('E10','display','Central brace definition; P05','Overworked (6); thickening Ep and dotted Ep formulas, two-row brace')
inv('E11','deletion','Before live Ep in first brace row; P05','Crossed doubtful E')
inv('E12','text','Right of upper brace row; P05','Paired-tick épaississement d’indice epsilon; du bord dotted T de T')
inv('E13','text','Below brace; P06','NB La frontière de E_epsilon dans T')
inv('E14','display','Middle formula; P06','(7) Ep_epsilon^(T) approximately [1-epsilon,1] times dotted T')
inv('E15','margin note','Long transverse left note; P07','NB Si Y, dotted T compacts; one continuous note including compactness, neighbourhoods and parenthesis')
inv('E16','insertion','Marginal opening; P07','Raised dotted T after Y, with curved leader')
inv('E17','deletion','Marginal opening before alors; P07','Crossed doubtful les')
inv('E18','deletion','Marginal end of neighbourhood sentence; P07','Crossed doubtful fermés')
inv('E19','insertion','Above marginal cancelled fermés; P07','ouverts')
inv('E20','margin note','Below marginal syst. fond.; P07','plus/plein : T, attachment uncertain')
inv('E21','text','Lower definition; P08–P09','Circled 2; closed inclusion and conic neighbourhood definition')
inv('E22','display','Inline in definition; P08','Y hooked unheaded shaft X')
inv('E23','display','Inline action; P09','(1) I times T, unheaded shaft to T')
inv('E24','insertion','Raised line above old conditions; P09','faisant de T un vois. ... absolu de Y.')
inv('E25','deletion','Within raised replacement; P09','tub.')
inv('E26','insertion','Above cancelled tub.; P09','coniq.')
inv('E27','deletion','Old lower baseline; P09','satisfaisant les conditions dites./id.')
inv('E28','text','Final paragraph; P10','Alors les lambda T=T_lambda ... voisinages tubulaires')
inv('E29','display','Final baseline at paper edge; P10/P12','Overworked (8); dotted T_lambda=lambda dotted T, asserted frontier in X')
inv('E30','margin note','Extreme lower-left foot; P11','12','attribution indeterminate')

# Audit scope strings are literal targeted draft content; nearby rotated/partial context is explicitly excluded.
audit=[]
def au(id,kind,box,reading,scope=''):
    a=dict(box=id,kind=kind,xyxy=box,reading=reading)
    if scope:a['scope']=scope
    audit.append(a)
au('B01','struck passage; handwritten number; C/H different words; less than high confidence departure',[230,75,1663,290],r'''\deleted{2. Soit $X$ un espace, $Y$ un sous-espace fermé.}
\unsure{\deleted{(6)}|(6)} \deleted{Soit $T$}
\uline{NB} Les $T_\lambda$ $(\lambda\in[0,1])$ forment''','Top two complete baselines, including the old fragment and start of NB.')
au('B02','struck passage; doubtful formula; handwritten number; C/H different words; less than high confidence departure',[247,285,1605,532],r'''une famille croissante de parties fermées de
$T$, les $\mathring T_\lambda\overset{\mathrm{def}}=
\lambda\mathring T\deleted{\unsure{_\lambda}}$ $(\lambda\in]0,1])$
une famille croissante de parties ouvertes. Si $\lambda\in]0,1[$, alors''','Three full main-text baselines; the left vertical marginal strokes have their own box.')
au('B03','margin note',[177,490,223,692],r'\margin{$\Vert$}','Only the two upright marginal emphasis strokes.')
au('B04','insertion; handwritten number; C/H different words',[250,515,1660,734],r'''$\mathring T_\lambda$ est bel et bien l'intérieur \inserted{topologique}
de $T_\lambda$ dans $T$,
mais bien sûr $\mathring T_1=\mathring T$ n'est pas l'intérieur
\inserted{top.} de $T_1$ dans''','Two main baselines with both raised insertions and their attachments; partial preceding baseline at the upper edge is context only.')
au('B05','struck passage; doubtful formula; handwritten number; C/H different words; less than high confidence departure',boxes['P04'],r'''l'espace topologique $T_1=T$, i.e. on n'a pas
$\mathring T\unsure{\deleted{_1}|_1}=T$ sauf
si $\dot T=\phi$ i.e. $Y=T$.''','The two main baselines; transverse marginal fragments at lower left are excluded.')
au('B06','struck passage; doubtful formula; handwritten number; C/H different words; less than high confidence departure',boxes['P05'],r'''Posons, pour $\lambda\in]0,1[$
\[
(\unsure{6})\qquad
\left\{\begin{aligned}
T\setminus\mathring T_\lambda
&\overset{\mathrm{def}}=\deleted{\unsure{E}}
\mathrm{Ep}^{(T)}_{1-\lambda=\varepsilon}
\quad\text{``épaississement d'indice $\varepsilon$''}\\
&\hspace{4em}\text{du bord $\dot T$ de $T$}\\
\dot{\mathrm{Ep}}_\varepsilon^{(T)}
&\overset{\mathrm{déf}}=\dot T\unsure{\amalg|\cup}(1-\varepsilon).\dot T
\end{aligned}\right.
\]''','Complete brace definition and its prose annotation; transverse marginal text is excluded.')
au('B07','doubtful formula; handwritten number; C/H different words; less than high confidence departure',boxes['P06'],r'''\uline{NB} La frontière de $E_\varepsilon$ dans $T$ est
$(1-\varepsilon)\dot T$, et $E_\varepsilon$
est un voisinage de $\dot T$. On a
\[
(7)\qquad\mathrm{Ep}_\varepsilon^{(T)}
\simeq[\underbrace{1-\varepsilon}_{\lambda},1]\times\dot T
\]''','The main NB and formula (7); crossing transverse note fragments at the left are excluded.')
margin=D[D.index(r'\margin{\uline{NB} Si'):D.index('% P07 scope check:')].strip()
margin='\n'.join(x for x in margin.splitlines() if not x.startswith('%'))
au('B08','margin note; insertion; struck passage; doubtful formula; handwritten number; C/H different words; less than high confidence departure',boxes['P07'],margin,'Only the continuous transverse margin note. Main-text (6), main-text underlined NB, circled 2, (7), and other perpendicular text visible in this frame are excluded. Rotation clockwise 70 degrees.')
au('B09','handwritten number; C/H different words',boxes['P08'],r'''\textcircled{2} Soit $Y\lhook\joinrel\relbar X$ une inclusion fermée d'espaces
 topologiques. Un \uline{voisinage conique} de \uline{$Y$ dans} $X$
est un voisinage $T$ de $Y$ dans $X$''')
au('B10','insertion; struck passage; handwritten number; C/H different words; less than high confidence departure',[242,1888,1639,2081],r'''muni d'une opération (1) $I\times T\mathrel{\relbar\joinrel\relbar}T$
\inserted{faisant de $T$ un vois. \deleted{tub.}\inserted{coniq.}
absolu de $Y$.} \deleted{satisfaisant les conditions \unsure{dites.|id.}}
Alors les''','Operation line, raised replacement with its nested revision, crossed old line, and Alors les.')
au('B11','doubtful formula; handwritten number; C/H different words; less than high confidence departure',[241,2071,1670,2361],r'''$\lambda T=T_\lambda$ $(\lambda\in]0,1])$
forment d'autres voisinages
tubulaires de $Y$ dans $X$ (famille croissante) et
on voit que pour $\lambda\in]0,1[$, on a
\[
(\unsure{8})\qquad\dot T_\lambda=\lambda\dot T
\quad\text{est la frontière de }T_\lambda=\lambda T\text{ dans }X.
\]''','Final three prose baselines and complete final formula to the physical paper edge; P12 confirms no continuation below it.')
au('B12','margin note; handwritten number',boxes['P11'],r'\margin{12}')

doubts=[
 dict(place='P01 old number',reading=r'\unsure{\deleted{(6)}|(6)}',alternatives='Cancelled old (6), or live overworked (6); underlying revision not recoverable.',confidence='medium',reason='The looped numeral and diagonal overwork are separate from the horizontal Soit T strike; darkness alone does not determine cancellation.'),
 dict(place='P02 cancelled right subscript',reading=r'\deleted{\unsure{_\lambda}}',alternatives='lambda-like lowered predecessor; exact strokes obscured.',confidence='medium',reason='The small group is crossed and every constituent stroke is not exposed.'),
 dict(place='P04 overwritten subscript',reading=r'\unsure{\deleted{_1}|_1}',alternatives='Cancelled 1, or live overworked 1.',confidence='medium',reason='Loops and retracing obscure both the body and an independent deletion stroke.'),
 dict(place='P05 current definition number',reading=r'(\unsure{6})',alternatives='6 preferred; no secure alternative numeral or previous state.',confidence='medium',reason='The loop and several superposed stems do not isolate a clean final digit.'),
 dict(place='P05 cancelled E',reading=r'\deleted{\unsure{E}}',alternatives='E-like predecessor; lower loops heavily crossed.',confidence='low',reason='The broad black upper crossing and curved lower strokes do not expose the entire letter.'),
 dict(place='P05 lower union-like sign',reading=r'\unsure{\amalg|\cup}',alternatives='amalg or cup.',confidence='medium',reason='A short left foot favours amalg, while the filled rounded U body admits cup. No mathematical disjointness argument settles the ink.'),
 dict(place='P05/P06 parenthesized T placement',reading=r'\mathrm{Ep}_\varepsilon^{(T)}',alternatives=r'Raised (T) preferred; a baseline argument \mathrm{Ep}_\varepsilon(T) remains geometrically possible.',confidence='medium',reason='The (T) forms sit above the low epsilon/index, but their large height approaches that of the main E.'),
 dict(place='P07 crossed les',reading=r'\deleted{\unsure{les}}',alternatives='les-like predecessor.',confidence='low',reason='The long l and low bodies are crossed too densely for a certainty resolution.'),
 dict(place='P07 crossed fermés',reading=r'\deleted{\unsure{fermés}}',alternatives='fermés preferred; internal letters obscured.',confidence='medium',reason='The baseline crossing hides part of the word, although the f and ending favour the candidate.'),
 dict(place='P07 extra fragment and attachment',reading=r'\unsure{plus|plein} : $T$',alternatives='plus or plein; attachment to the surrounding margin remains unassigned.',confidence='low',reason='Descending p and tall l are clear, but the low ending is compressed. The fragment sits below syst. fond. and before the lower parenthesis.'),
 dict(place='P07 parenthetical opening',reading=r'\unsure{ainsi que voisinages}',alternatives='C’s phrase is preferred; not every letter is visible.',confidence='medium',reason='Small joined letters and interference by perpendicular main-text ink obscure the full sequence.'),
 dict(place='P09 crossed final word',reading=r'\unsure{dites.|id.}',alternatives='dites. preferred; id. retained as witness alternative.',confidence='medium',reason='Several low bodies extend to the full stop, but the long strike and raised-word descenders obscure their individual shapes.'),
 dict(place='P10 current number (8)',reading=r'(\unsure{8})',alternatives='8 preferred; previous numeral/state unreadable.',confidence='medium',reason='Two loop-like bodies are heavily retraced; no clean recoverable older digit is introduced.')
]
notes=[
 dict(id='N01',text='Undated handwritten continuation: the page distinguishes the increasing closed T_lambda from the open circled-T_lambda, states the interior caveat at lambda=1, defines the Ep thickening and its dotted boundary, gives formula (7), adds a transverse compactness/neighbourhood note, and introduces conic neighbourhoods of a closed inclusion Y into X. This is a source-content description; the first reader did not prove these claims or inspect the preceding leaf.'),
 dict(id='N02',text='Source and notation check: all ordinary T forms on this leaf have a single cap and stem; C’s repeated bars are not supported by a second horizontal stroke. The hollow-circle and filled-dot forms supply local comparisons. The written empty set is phi. Prose E_epsilon and displayed Ep_epsilon coexist and are preserved. First two small labels read def without an independent accent, while the lower brace label has a separate mark supporting déf.'),
 dict(id='N03',text='Layout/scope check of P07: the one continuous transverse note overlaps the frame of neighbouring main text. Inverse rotation maps the apparent blob after forment to the current formula number (6), about original (245,1062), and the alleged T_epsilon after voisinages to the main-text underlined NB, about (269,1351). Those elements are transcribed once in the main text, not duplicated as marginal cancellations. The genuine un at about (31,1973) belongs to the margin, as does the separate plus/plein : T fragment near (52–115,1900–1740), whose attachment remains uncertain.'),
 dict(id='N04',text='The source retains the literal word “tubulaires” in the final family paragraph after the earlier inserted replacement coniq. for cancelled tub. The final assertion reads “est la frontière de T_lambda=lambda T dans X”. Both inline map connectors lack a secure arrowhead. The old (6), current (6), and final (8) show overwork; no invented chronological sequence or earlier numeral is supplied. Thin foliation 12 has indeterminate attribution.'),
 dict(id='N05',text='Root targeted counterexample, conditional on the cone-action interpretation supplied by root from the preceding page (not independently read by this first reader): take X=([0,1]×{0}) union ({1/2}×[0,1]), T=[0,1]×{0}, Y={(0,0)}, dotted T={(1,0)}, and lambda·(t,0)=(lambda t,0). T is closed in X and contains a neighbourhood of Y; it is the cone on dotted T→Y. At lambda=3/4, T_lambda=[0,3/4]×{0}. Its ambient boundary in X consists of the junction (1/2,0) and the endpoint (3/4,0), whereas lambda dotted T consists only of (3/4,0). Thus the final ambient-frontier assertion fails under these hypotheses. Root confirmed the exact final ink in P10 before this diagnostic was added. The transcription is unchanged.'),
 dict(id='N06',text='Refinement of N05: the issue is the distinction between the interior in T and the ambient interior in X. In the counterexample, the junction belongs to the former but not the latter. An additional hypothesis controlling ambient openness of the cone interior would be needed to exclude this obstruction; no general sufficiency theorem is asserted here. This check does not verify the compactness/fundamental-system marginal claim or all preceding cone identities.'),
 dict(id='N07',text='Footer scope check: the final lambda meets the physical sheet edge. Completing strip P12 contains only that edge and black scanner background below it; it adds no source letters or indices. No diagram or unrelated drawing occurs on this leaf; the two marginal vertical strokes and the unheaded inline connectors are retained as written symbols.')
]
checks=[
 dict(statement_id=P+'.N01',type='carried as background without fault found',outcome='Transcription-only content summary. No theorem verification is claimed for the interior statements, thickening construction, formula (7), or marginal compactness assertions.'),
 dict(statement_id=P+'.N02',type='used and rechecked in this run',outcome='Local visual comparison of every plain/circled/dotted T occurrence, Ep/E usage, and small definition labels on the assigned leaf; not a mathematical proof.'),
 dict(statement_id=P+'.N03',type='used and rechecked in this run',outcome='Coordinate/layout comparison of the stable margin crop with the already-read main formulas identified shared ink and prevented duplicate transcription.'),
 dict(statement_id=P+'.N05',type='refuted, with refined id',outcome='Root supplied and checked the explicit branched-interval counterexample to the final ambient-boundary assertion under the stated cone interpretation. The first reader verified only the assigned page’s exact wording and records the root check with its assumptions. Refined issue is N06.'),
 dict(statement_id=P+'.N06',type='targeted proof check',outcome='Root isolated ambient versus relative interior as the obstruction. The report does not claim a proof that any proposed extra hypothesis is generally sufficient.'),
 dict(statement_id=P+'.N07',type='used and rechecked in this run',outcome='One completing footer strip inspected by first reader and root; no additional text beyond the physical paper edge.')
]
notation=[
 dict(form=r'T, T_\lambda',meaning='Cone neighbourhood and its scaled members; plain T as written, without an independent bar.',evidence='All ordinary occurrences in P01–P10 have one cap and stem, including detached-cap forms.'),
 dict(form=r'\mathring T_\lambda=\lambda\mathring T',meaning='Interior/circled part specified for lambda in ]0,1]; the text warns about its relation to topological interior at lambda=1.',evidence='P02 hollow circles and first defining equality; P03–P04 interior prose.'),
 dict(form=r'\dot T',meaning='Boundary called bord; filled dot above T.',evidence='P04–P06 and P10, explicit bord and frontière language.'),
 dict(form=r'\phi',meaning='Empty set; ϕ : l’ensemble vide.',evidence='P04 small oval crossed by a long slanted stem.'),
 dict(form=r'\mathrm{Ep}^{(T)}_{1-\lambda=\varepsilon},\ \dot{\mathrm{Ep}}_\varepsilon^{(T)}',meaning='Quoted épaississement d’indice epsilon and its dotted companion, with raised (T) preferred.',evidence='P05 two-row brace, p descenders and separate dot above lower E.'),
 dict(form=r'E_\varepsilon',meaning='The prose notation used in the frontier/neighbourhood sentence; not silently changed to Ep.',evidence='P06 both prose capital E forms lack the p of formula (7).'),
 dict(form=r'\unsure{\amalg|\cup}',meaning='Unresolved union-like sign between the two boundary terms.',evidence='P05 heavy U body and short left foot.'),
 dict(form=r'\lhook\joinrel\relbar,\ \mathrel{\relbar\joinrel\relbar}',meaning='Unheaded hooked inclusion shaft and unheaded action shaft, respectively.',evidence='P08/P09 blunt right endpoints without visible arrowhead arms.'),
 dict(form=r'I',meaning='Interval/action parameter in (1); one-stem serif capital as written.',evidence='P09 has thin top and bottom caps and one upright stem; no doubling.'),
 dict(form=r'\Vert',meaning='Marginal emphasis by two upright strokes; not a horizontal equality.',evidence='P03 left margin.'),
 dict(form='paired upper quotation ticks',meaning='Literal double quotes around épaississement d’indice epsilon.',evidence='P05 separate upper tick pairs.')
]
abbreviations=[
 dict(form='NB',expansion='nota bene'),dict(form='def / déf',expansion='définition; written labels retained with their local accent state'),
 dict(form='top.',expansion='topologique'),dict(form='i.e.',expansion='id est'),dict(form='syst.',expansion='système'),
 dict(form='fond.',expansion='fondamental'),dict(form='vois.',expansion='voisinage'),dict(form='tub.',expansion='tubulaire; cancelled'),
 dict(form='coniq.',expansion='conique; inserted'),dict(form=r'\unsure{dites.|id.}',expansion='No expansion imposed on the uncertain cancelled ending.')
]
hand=[
 dict(habit='Ordinary T often has a long detached cap above its stem; genuine circle/dot marks are additional small shapes.',places='P01–P10 throughout',consistency='Every ordinary T on this leaf has only one cap; no independent overbar found.',witness_errors='C repeatedly interprets the inherent cap as an overbar; H plain T is supported.'),
 dict(habit='The p in Ep descends clearly below the main baseline beside a block E.',places='P05 both rows and P06 formula (7)',consistency='All three displayed Ep occurrences show p; prose E_epsilon lacks it.',witness_errors='H drops the displayed p and treats (T) as a baseline argument.'),
 dict(habit='Curved insertion leaders can pass near or through adjoining baseline letters.',places='P03 topologique/top.; P07 dotted T; P09 coniq.',consistency='Leader paths and word states were distinguished independently at each location.',witness_errors='H strikes de beneath topologique and treats the raised replacement in P09 as cancelled.'),
 dict(habit='A dark overworked group does not by itself identify cancellation or an earlier numeral.',places='P01 old6, P04 subscript1, P05 current6, P10 current8',consistency='Reading/state uncertainties retained where independent strikes or prior forms cannot be isolated.',witness_errors='C gives definite cancellation to the overworked subscript; H gives it live. Neither settles the state.'),
 dict(habit='Long slanted margin writing crosses the rectangular frame of upright main text.',places='P07 compared with P05/P06',consistency='Coordinate identity separates main (6)/NB from the continuous marginal note.',witness_errors='C’s putative marginal T_epsilon is the neighbouring main NB; H describes two notes and leaves much readable text illegible.'),
 dict(habit='Map shafts may end bluntly without arrowheads.',places='P08 inclusion and P09 action',consistency='Both right endpoints lack a secure two-arm head.',witness_errors='Both witnesses supply arrowheads.'),
 dict(habit='Small definition labels can lack an accent; f has a long descending stroke.',places='P02 and P05',consistency='First two labels lack a separate acute; lower P05 label has a separate short mark.',witness_errors='Both witnesses standardize every label to déf.')
]
reviews=[
 dict(text='Top 2. Soit X ... fermé.',scope_attachment='Entire first line cancelled, including written 2 and terminal stop.',evidence='P01 one long cancellation traverses the full line.'),
 dict(text='Old (6), Soit T',scope_attachment='Soit T cancelled; separate number state left uncertain.',evidence='P01 number overwork is not joined to the Soit T cancellation.'),
 dict(text='Subscript after lambda circleT',scope_attachment='Crossed lowered lambda-like group retained, unresolved.',evidence='P02 small hatched subscript after the right-hand circleT.'),
 dict(text='topologique',scope_attachment='Inserted before the live de T_lambda; no independent deletion of de.',evidence='P03 raised letters and continuous bent leader.'),
 dict(text='top.',scope_attachment='Inserted before de T1 in the following interior clause.',evidence='P03 slanted leader from the raised abbreviation.'),
 dict(text='Subscript after on n’a pas circleT',scope_attachment='Reading 1 and state uncertain between cancelled/live; no forced chronology.',evidence='P04 retraced lowered loop/body without independent strike.'),
 dict(text='E-like predecessor in first brace row',scope_attachment='Cancelled before the live Ep; exact letter remains doubtful.',evidence='P05 broad crossing hides the upper body.'),
 dict(text='Marginal dotted T',scope_attachment='Live insertion after Y and its comma, before compacts.',evidence='P07 raised dotted T and curved leader; no independent strike.'),
 dict(text='Marginal les-like predecessor',scope_attachment='Cancelled immediately before alors.',evidence='P07 short l/e/s-like run under a crossing.'),
 dict(text='Marginal fermés / ouverts',scope_attachment='Baseline fermés candidate cancelled; raised ouverts replaces it.',evidence='P07 horizontal crossing through lower word and clear raised o/u/v/e/r/t/s sequence.'),
 dict(text='plus/plein : T',scope_attachment='Preserved as a separate live marginal fragment; its connection with the surrounding sentence remains uncertain.',evidence='P07 physical position below syst. fond.; no secure deletion line through it.'),
 dict(text='Apparent extra groups after forment/voisinages in P07 frame',scope_attachment='No additional marginal deletions: these are main-text (6) and underlined NB already transcribed.',evidence='P07 inverse coordinate mapping to P05/P06, recorded in N03.'),
 dict(text='faisant de T un vois. ... absolu de Y.',scope_attachment='Whole raised line is a live insertion after the action expression, replacing the old conditions sentence.',evidence='P09 old cancellation runs below the live replacement rather than through its bodies.'),
 dict(text='tub. / coniq.',scope_attachment='Only tub. is deleted inside the replacement; coniq. inserted above it.',evidence='P09 short crossed group and bent leader to raised coniq.'),
 dict(text='satisfaisant les conditions dites./id.',scope_attachment='Whole old baseline sentence cancelled; final word remains doubtful.',evidence='P09 continuous long strike through all old words.'),
 dict(text='Current formula numbers (6), (8)',scope_attachment='Overwork retained as uncertainty; no recoverable earlier digit or definite sequence supplied.',evidence='P05 and P10 superposed loops/stems.'),
]
rows=list(csv.DictReader((R/'packets'/P/'differences.tsv').open(),delimiter='\t'))
disp={
 1:'H editorial leaf-order note excluded from source text; no other leaves inspected.',2:'Continuation of H editorial note excluded.',
 3:'Macro-only circle notation; P02 verifies hollow circle.',4:'Macro-only circle notation; P02 verifies hollow circle.',
 5:'P02_c: crossed subscript retained.',6:'Macro-only TeX thin space \\,; no literal comma.',7:'Macro-only TeX thin space \\,; no literal comma.',
 8:'Macro-only circle notation; P03.',9:'Macro-only circle notation; P03.',10:'Macro-only circle notation; P03.',11:'Macro-only circle notation; P04; subscript state separately P04_b.',
 12:'P03/B03: actual vertical marginal strokes retained; H explanatory note itself excluded.',13:'Macro-only TeX thin space \\,; no literal comma.',
 14:'P05_a: current overworked (6) retained; aligned/array macro variants excluded.',15:'Macro-only circle notation; P05.',
 16:'P05_b: live Ep and crossed predecessor retained; raised (T) preferred.',17:'P05_c plus P05_b: quotation annotation and superscript placement.',
 18:'P05_c/P05_d: de rather than dans, p in lower Ep; array spacing excluded.',19:'P05_d: raised (T) preferred, geometric doubt retained.',
 20:'M0318/P05_d: amalg/cup unresolved; vertical separator is uncertainty syntax, not extra ink.',21:'P05_d: explicit multiplication point retained.',
 22:'Macro-only aligned/array difference.',23:'P05_c: literal paired upper ticks and de T; annotation attached to first row.',
 24:'P06_b: Ep includes p.',25:'P06_b: raised (T) preferred with placement doubt.',
 26:'P07_a: raised live dotted T after Y, not a struck predecessor.',27:'P07_a: no independent parenthetical ou; curved stroke is insertion leader.',
 28:'P07_a/P07_b: compacts, crossed les-like group, alors T compact, et retained.',29:'Macro-only TeX thin space \\,; no literal comma.',
 30:'P07_c/M0320: right ] resolved from left-extending feet.',31:'P07_d: syst. fond. readable with both stops.',
 32:'P07_e/P07_f/P07_g: full continuous margin read; fermés/ouverts revision and local fragment retained; H editorial second-note description excluded.',
 33:'P07_g/M0322/M0323: parenthesis retained, alleged T_epsilon excluded as neighbouring main NB; H section-number token handled P08_a.',
 34:'P08_a: circled 2 retained.',35:'P09_b: cancelled tub. plus inserted coniq., not expanded conique.',36:'P09_b: final stop after Y visible.',
 37:'P09_c: preferred dites. under strike with id. alternative.',38:'Macro-only TeX thin space \\,; no literal comma.',39:'Macro-only TeX thin space \\,; no literal comma.',
 40:'Display-vs-prose boundary only; same written final clause, P10_b.',41:'P11_a thin12 retained; source overwork of (8) noted separately; H editorial note not transcribed.'
}
assert len(rows)==41,(len(rows),rows[-1])
diff=[dict(row=i,disposition=disp[i]) for i in range(1,42)]
line_count=sum(1 for x in D.splitlines() if x.strip() and not x.lstrip().startswith('%'))
report=dict(page=P,reader='reader_a',line_count=line_count,
 line_count_basis='Nonempty logical draft rows excluding comments, including displayed-formula rows and markup delimiters; not a claimed count of physical manuscript baselines.',
 changes=changes,decisions=decisions,inventory=inventory,audit_boxes=audit,doubts=doubts,notes=notes,check_events=checks,notation=notation,abbreviations=abbreviations,hand=hand,diff_coverage=diff,deletion_insertion_review=reviews,
 inspection=dict(source='source/SP89_C13_149+150_scans/150_scan013.jpg',source_size=[1685,2361],whole_image_views=1,native_half_views=[1,1],crop_count=12,
 crop_views={k:(2 if k=='P07' else 1) for k in boxes},crop_view_note='P03’s first delivery failed through context truncation and was redelivered before its first actual visual inspection. P07 was reopened once solely for its still-open margin fragment/bracket/scope; no new framing or recrop. Root separately reviewed every stable frame. P12 is one completing strip for previously clipped footer extent and contains only paper edge/scanner background.',
 crop_transform={'P07':{'rotation_degrees_clockwise':70}},ocr=False,outside_research=False,tex_compilation=False,other_page_access=False),
 completion_status='First-reader artifacts prepared; root finalization required.')
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# Check local excerpt fidelity without treating macro spelling as a collation change.
def norm(s):return re.sub(r'\s+',' ', '\n'.join(x for x in s.splitlines() if not x.lstrip().startswith('%'))).strip()
problems=[]
for q in changes:
    for k,src in [('c',C),('h',H)]:
        if norm(q[k]) not in norm(src):problems.append((q['id'],k,q[k]))
    if norm(q['final']) not in norm(D):problems.append((q['id'],'final',q['final']))
for q in decisions:
    if norm(q['reading']) not in norm(D):problems.append((q['id'],'reading',q['reading']))
# audit B02 intentionally removes the intervening margin macro, so allow ordered exact segments there.
for q in audit:
    if q['box']=='B02':
        a,b=q['reading'].split('une famille croissante de parties ouvertes.')
        if norm(a) not in norm(D) or norm('une famille croissante de parties ouvertes.'+b) not in norm(D):problems.append((q['box'],'reading',q['reading']))
    elif norm(q['reading']) not in norm(D):problems.append((q['box'],'reading',q['reading']))
print(json.dumps({'changes':len(changes),'marks':len(decisions),'inventory':len(inventory),'audit_boxes':len(audit),'diff_rows':len(diff),'logical_rows':line_count,'excerpt_problems':problems},ensure_ascii=False,indent=2))
