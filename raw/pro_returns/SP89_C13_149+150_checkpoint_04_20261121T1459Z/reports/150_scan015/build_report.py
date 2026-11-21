from pathlib import Path
import json,csv,re
R=Path('/workspace/scratch/8759b8008681'); P='150_scan015'; O=R/'work/reports'/P
C=(R/'packets'/P/'C.tex').read_text(); H=(R/'packets'/P/'H.tex').read_text(); D=(O/'draft.tex').read_text()
B=json.loads((O/'crop_boxes.json').read_text())
changes=[]
cats={'misread symbol or index':1,'misread word':2,'omission':3,'drawing or diagram':4,'readable ink left as \\ill{}':5,'insertion or placement':6,'deletion state (struck given live or live given struck)':7,'abbreviation expanded or spelling modernised':8,'text not on the page':9,'other':10}
def ch(id,place,c,h,final,evidence,confidence='high',kind='misread symbol or index',against_c=True,against_h=False,marked_in_h=False,consequential=False):
    p=id.split('_')[0]
    changes.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,crop=f'crops/{P}_{p}.png',box=B[p],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,marked_in_h=marked_in_h,consequential=consequential,error_category=cats[kind]))
ch('P01_a','Opening ordinary T',r'\deleted{On dit}\inserted{Soit} $\bar T$ un voisinage',r'\struck{On dit} \add{Soit} $T$ un voisinage',r'\deleted{On dit}\inserted{Soit} $T$ un voisinage',
   'T has one long cap and a separate descending stem, without an additional upper bar. On dit is crossed on its baseline; Soit is raised above it and live. The other opening revision is the crossed tubulaire with conique above it, retained in its own inventory/audit scope.')
ch('P02_a','Complete formula (11)',r'(11)\qquad X^*=X\setminus\mathring T=(X\setminus\bar T)\cup\dot T',r'(11)\qquad X^{*}=X\setminus\overset{\circ}{T}=(X\setminus T)\cup\dot T',r'(11)\qquad X^*=X\setminus\mathring T=(X\setminus T)\cup\dot T',
   'The middle parenthetical T has one cap and stem, whereas the left interior T has a separate hollow circle and the final boundary T a separate filled dot. Two upright digits form 11. The star has several crossing arms, both set-difference strokes are oblique, and the union is an open U without a base foot.', 'high','misread symbol or index',True,False,False,True)
ch('P03_a','Proposition where/given clause and final punctuation',r'\uline{Prop.} Conditions équivalentes (où $\lambda\in]0,1[$ donné)',r'\emph{Prop.} Conditions équivalentes (\uncertain{si} $\lambda\in\,]0,1[$ \uncertain{donné}) :',r'\uline{Prop\unsure{.}} Conditions équivalentes (où $\lambda\in]0,1[$ donné)',
   'The first short word has an o body and low u with a separate upper accent, supporting où rather than si. Donné has the tall d and the final accent stroke. The closing parenthesis is followed by blank paper, with no colon. A stop after Prop is not secure and remains a separate local doubt; that added doubt alone is not counted against C.', 'high','misread word',False,True,True)
ch('P03_b','Condition a, partie-bord',r'une partie-bord de $X^*=X\setminus\mathring T$',r'une partie bordante de $X^{*}=X\setminus\overset{\circ}{T}$',r'une partie-bord de $X^*=X\setminus\mathring T$',
   'A separate horizontal hyphen follows partie. Bord has a tall b, low o/r and final d, followed immediately by de; there is no ante continuation. The adjacent whole formula has a visible star and hollow interior circle.', 'high','misread word',False,True,False,True)
ch('P04_a','Condition b, avec rather than sur',r'un homéomorphisme de $X$ avec lui-$=$',r'un homéomorphisme de $X$ sur lui-même',r'un homéomorphisme de $X$ avec lui-$=$',
   'The second baseline begins with the small a body and the v/e/c sequence, not s/u/r. The following lui has a looped l and dotted i. Two separate horizontal strokes follow a hyphen as the written same-word abbreviation.', 'high','misread word',False,True)
ch('P04_b','Condition b, equals-sign abbreviation',r'lui-$=$',r'lui-même',r'lui-$=$',
   'A short hyphen is followed by two distinct horizontal strokes. No letters m/ê/m/e are written after lui.', 'high','abbreviation expanded or spelling modernised',False,True)
ch('P04_c','Condition b, source and target pair with crossed prefix',r'transformant $\bar T,\dot T$ en $\deleted{\unsure{\lambda}}(\bar T_\lambda,\dot T_\lambda)$',r'transformant $T,\dot T$ en $(T_\lambda,\dot T_\lambda)$',r'transformant $T,\dot T$ en $\deleted{\unsure{\lambda}}T_\lambda,\dot T_\lambda)$',
   'The ordinary T forms have one cap each; the two boundary dots are separate filled marks. The prefix before the target has a lambda-like lower fork crossed by oblique hatching and remains unresolved. No independent live opening parenthesis can be isolated: the short downturned tip is continuous with the target T cap and adjacent curved traces belong to the crossed group. The clear final closing parenthesis is retained alone. A possible absorbed opening parenthesis is noted without supplying a live arc.', 'medium','misread symbol or index',True,True,False,True)
ch('P05_a','Condition b-prime, induit',r"que l'homéomorphisme induit l'identité",r"que l'homéomorphisme induise l'identité",r"que l'homéomorphisme induit l'identité",
   'After the initial i/n, the verb has the tall d, u body, dotted i and compact final t cross/body. There is no extra s/e run before the space preceding l’identité.', 'high','misread word',False,True)
ch('P05_b','Condition b-prime, fixed smaller member and where clause',r"sur $\bar T_{\lambda'}$ (où \deleted{$0<\lambda'<\lambda$} $\lambda'$ est donné, $0<\lambda'<\lambda$).",r"sur $T_{\lambda'}$ (\uncertain{si} \struck{$0<\lambda'<\lambda$} $\lambda'$ est donné, $0<\lambda'<\lambda$).",r"sur $T_{\lambda'}$ (où \deleted{$0<\lambda'<\lambda$} $\lambda'$ est donné, $0<\lambda'<\lambda$).",
   'T has one cap and a lowered lambda with a separate prime. The short prose word repeats the o/u plus upper accent of où. One continuous stroke cancels exactly the first 0<lambda-prime<lambda. The rewritten lambda-prime est donné and the second inequality are live; each prime, inequality sign, zero and closing parenthesis was read in the whole passage.', 'high','misread word',True,True,True)
ch('P06_a','Condition c, circumflex and T-prime',r'\deleted{tubulaire} conique $\bar T\'$',r'\struck{tubulaire} conique $T\'$',r'\deleted{tubulaire} cônique $T\'$',
   'Above the o in cônique is a short detached arch, separate from the c/o baseline bodies. It is retained as a circumflex. The following T has one cap and a separate raised prime, not an overbar. The old tubulaire has a horizontal cancellation through its bodies.', 'high','abbreviation expanded or spelling modernised',True,True)
ch('P06_b','Cancelled words before tel que',r'\deleted{tel que et \unsure{a}}',r'\struck{tel que et \ill{}}',r'\deleted{tel que et \unsure{a}}',
   'The long stroke crosses tel que et and a final low oval/return compatible with a. The surrounding words have identifiable stems and the q descender, but the final token remains obscured and is not resolved from grammar.', 'medium','readable ink left as \\ill{}',False,True,True)
ch('P06_c','Condition c, rescaling equality',r'tel que $\bar T=\lambda\bar T\'$,',r'tel que $T=\lambda T\'$,',r'tel que $T=\lambda T\'$,',
   'Both T forms have single cap strokes, with the right prime separate above the stem. The equals sign has two bars, lambda has its long upper limb and lower fork, and a comma follows T-prime.', 'high','misread symbol or index',True,False,False,True)
ch('P07_a','Compatibility sentence, singular l’isomorphisme',r"l'isomorphisme étant",r"d'isomorphismes étant",r"l'isomorphisme étant",
   'The initial upright has the narrow lower return of l, with a separate apostrophe; it lacks a d bowl. The final e ends in a low return without another s body. The following étant has its separate accent.', 'high','misread word',False,True)
ch('P07_b','Compatibility sentence, singular compatible',r'compatible avec les',r'compatibles avec les',r'compatible avec les',
   'The word has a descending p, tall b/l sequence and terminal e return. No separate s follows before the space and avec.', 'high','misread word',False,True)
ch('P07_c','Compatibility sentence, côniques',r'structures de voisinages coniques.',r'structures de voisinages coniques.',r'structures de voisinages côniques.',
   'A detached short arch sits above the o, distinct from the baseline c/o and the following dotted i. The plural ending and final full stop are visible. Both witnesses omit this circumflex.', 'high','abbreviation expanded or spelling modernised',True,True)
ch('P08_a','Definition of strict, plain T',r'On dit alors que $\bar T$ est un vois.',r'On dit alors que $T$ est un vois.',r'On dit alors que $T$ est un vois.',
   'T has a single cap and vertical stem. Vois. ends in a distinct stop. Transverse marginal letters overlap the beginning of the line but are inventoried separately, not duplicated as part of On dit alors.')
ch('P08_b','End of strict definition, no final stop',r'\uline{strict} dans $X$.',r'\emph{strict} dans $X$',r'\uline{strict} dans $X$',
   'One underline lies only beneath strict. After the two crossing strokes of the final X there is blank paper; no independent stop is present.', 'high','text not on the page',True,False)
ch('P09_a','Marginal opening and defining verb',r'Il vaut mieux de définir les voisinages coniques',r'Il vaut mieux \uncertain{partir} de \uncertain{la} \uncertain{notion} de voisinage \uncertain{conique}',r'Il vaut mieux de definir les voisinages côniques',
   'Il vaut mieux de is a continuous legible first line. The next line has d/e/f/i/n/i/r, with a tall f and two i positions; no independent acute over the first e is secure, so definir is retained. Les and the plural voisinages are visible. The marginal côniques has a detached arch above o, matching the locally written circumflex forms. No partir, la or notion sequence is present.', 'medium','misread word',True,True,True)
ch('P09_b','Marginal strict ending',r'stricts comme',r'strict comme',r'\unsure{strict|stricts} comme',
   'The last tall t and its cross/return are visible, but an independent terminal s cannot be separated. Strict is preferred with stricts retained as alternative. The distinct final s of stricts in P12 provides a local comparison; grammar is not used to add one here.', 'medium','misread word',True,False)
ch('P09_c','Marginal germes phrase and underline',r'comme \unsure{des} \uline{germes} de voisinage',r'comme \uncertain{fondamentale}, \uncertain{et} définir les voisinages \emph{\uncertain{stricts}} \ill{}',r'comme \unsure{des} \uline{germes} de voisinage',
   'Comme has the open c and joined low bodies. The short des candidate remains obscured by neighbouring upright main-text Corollaire ink and is not resolved. The following germes has a long g descender and a single independent underline; de voisinage continues on the same transverse baseline. The underline belongs to germes, not strict(s). H’s longer fundamental/definition wording is unsupported by this sequence.', 'medium','misread word',False,True,True,True)
ch('P09_d','Marginal larger-neighbourhood formula',r'plus grand $(1+\varepsilon)\bar T\unsure{-R_{>0}}$ $(\varepsilon>0)$',r'$T$ \uncertain{partie} $E_\varepsilon(T)$ \ldots\ ($\varepsilon>0$)',r'plus grand $(1+\varepsilon)T\unsure{-R_{>0}}$ $(\varepsilon>0)$',
   'Plus grand has a descending p/g and terminal d. In the following complete formula, the parentheses, 1, plus, epsilon-like small body and ordinary single-cap T are visible. A separate short minus is followed by a looped R-like glyph and a cramped lowered >0-like group; the whole ending remains unresolved. The final separate parenthesis reads epsilon>0. H’s E_epsilon(T) and partie are not the written sequence.', 'medium','misread symbol or index',True,True,True,True)
ch('P10_a','First corollary, ordinary T forms',r'Quand $\bar T$ est vois. \deleted{tub.} con. strict dans $X$, $\dot T$ est la frontière de $\bar T$ dans $X$.',r'Quand $T$ est vois. \struck{tub.} con. strict dans $X$, $\dot T$ est la frontière de $T$ dans $X$.',r'Quand $T$ est vois. \deleted{tub.} con. strict dans $X$, $\dot T$ est la frontière de $T$ dans $X$.',
   'Both ordinary T forms have one cap each; the left T of the second line has a separate filled boundary dot. The prose abbreviation con. has its own final stop. A comma follows the first X and a full stop the final X. The ambient-frontier assertion is retained literally.', 'high','misread symbol or index',True,False,False,True)
ch('P11_a','Second corollary, replacement T and extra triangular group',r'Si \deleted{il est}\inserted{$\bar T$} voisinage',r'Si \struck{\ill{}} $T$ \add{est un} voisinage',r'Si \deleted{il est} \unsure{\deleted{$A$}|$A$}\inserted{$T$} voisinage',
   'The old il est lies on a long cancellation. A further group has two oblique legs meeting at a high apex plus a short mid-height crossbar; the cancellation crosses its feet. It is retained as A-like ink with token/state uncertainty and a possible insertion-caret interpretation, not read as un from grammar. T is raised after/above it and has a single cap. No est un is visible after the replacement T. The arrow-like diagonal above comes from the preceding frontière f descender and is not a second mark.', 'low','insertion or placement',True,True,True,True)
ch('P12_a','Second corollary, scaled members and interval',r'dans $X$, les $\bar T_\lambda$ $(\lambda\in]0,1[)$',r'dans $X$, les $T_\lambda$ ($\lambda\in\,]0,1[$)',r'dans $X$, les $T_\lambda$ $(\lambda\in]0,1[)$',
   'T_lambda has one cap and a lowered lambda, without a further bar. Both interval endpoints, 0 and 1, the surrounding parentheses and the comma after X are visible.', 'high','misread symbol or index',True,False)
ch('P12_b','Second corollary, final punctuation',r'\deleted{tubulaires}\inserted{coniques} stricts.',r'\struck{tubulaires} \add{coniques} stricts',r'\deleted{tubulaires}\inserted{coniques} stricts',
   'The old plural tubulaires is crossed and coniques is raised above it. Stricts has a small final s after its last t; beyond that s lies blank paper, with no independent full stop.', 'high','text not on the page',True,False)
ch('P13_a','Thin lower-left foliation',r'\margin{14}',r'\add{coniques} stricts',r'\margin{14}',
   'A thin pale hand writes a slanted-topped 1 and an open 4 at the lower-left sheet edge. H has no source transcription of that foliation. Its hand is not attributed to the author.', 'high','omission',False,True)
for q in changes:
    for k in ('c','h','final'):q[k]=q[k].replace("\\'", "'")

def de(id,reading,evidence,confidence='medium'):
    return dict(id=id,cote='150',scan='15',decision='undecided',reading=reading,evidence=evidence,crop=f'crops/{P}_P09.png',box=B['P09'],confidence=confidence)
decisions=[
 de('M0331',r'\unsure{des}','The short group between comme and germes is obscured by adjoining main-text Corollaire strokes. Des remains a possible source reading, but the letters cannot all be isolated.','low'),
 de('M0332',r'(1+\varepsilon)T\unsure{-R_{>0}}','The whole formula was inspected. Parentheses, 1, plus, epsilon-like body and single-cap T are visible; a separate minus and R-like loop/leg are followed by a cramped low group compatible with >0. The ending is not secure enough to resolve.','medium')
]
inv=[]
def iv(n,kind,position,first,hand='his hand'):
    inv.append(dict(scan=P,sheet_kind='text',hand=hand,element=f'E{n:02d}',kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
iv(1,'text','Opening two baselines; P01','Soit T un voisinage conique de Y subset X dans X, posons')
iv(2,'deletion','Opening left; P01','On dit')
iv(3,'insertion','Above opening cancellation; P01','Soit')
iv(4,'deletion','Opening right; P01','tubulaire')
iv(5,'insertion','Above opening tubulaire; P01','conique')
iv(6,'display','Upper display; P02','(11) X*=X minus circled T=(X minus T) union dotted T')
iv(7,'text','Below (11); P02','c’est une partie fermée de X.')
iv(8,'deletion','After closedness sentence; P02/P03 overlap','On dit que')
iv(9,'text','Proposition heading; P03','Prop.; Conditions équivalentes, where lambda lies in ]0,1[')
iv(10,'text','Condition a; P03','dotted T est une partie-bord')
iv(11,'text','Condition b; P04','homéomorphisme de X avec lui-=')
iv(12,'deletion','Condition b target prefix; P04','Crossed lambda-like group, possible absorbed parenthesis')
iv(13,'text','Condition b-prime; P05','Comme b, mais ... induit l’identité')
iv(14,'deletion','First inequality in b-prime; P05','0<lambda-prime<lambda')
iv(15,'text','Condition c; P06/P07','voisinage cônique T-prime; compatibility of conic structures')
iv(16,'deletion','Condition c first line; P06','tubulaire')
iv(17,'deletion','Condition c second line; P06','tel que et a-like token')
iv(18,'text','Definition following c; P08','On dit alors ... strict dans X')
iv(19,'deletion','Strict-definition line; P08','tub.')
iv(20,'margin note','Long transverse lower-left note; P09','Il vaut mieux de definir ... germes de voisinage plus grand')
iv(21,'text','First corollary; P10','Quand T est vois. ... dotted T est la frontière de T dans X.')
iv(22,'deletion','First corollary first line; P10','tub.')
iv(23,'text','Second corollary; P11/P12','Si T voisinage conique ... les T_lambda ... stricts')
iv(24,'deletion','Second corollary opening; P11','il est')
iv(25,'deletion','Below/left of raised replacement T; P11','Additional A-like triangular group; state/token/caret function uncertain')
iv(26,'insertion','Second corollary opening; P11','T')
iv(27,'deletion','Second corollary first line; P11','tubulaire')
iv(28,'insertion','Above second-corollary tubulaire; P11','conique')
iv(29,'display','Inline second-corollary parameter expression; P12','T_lambda, lambda in ]0,1[')
iv(30,'deletion','Last main line; P12','tubulaires')
iv(31,'insertion','Above last cancelled word; P12','coniques')
iv(32,'margin note','Extreme lower-left corner; P13','14','attribution indeterminate')

aud=[]
def au(n,kind,box,reading,scope=''):
    a=dict(box=f'B{n:02d}',kind=kind,xyxy=box,reading=reading)
    if scope:a['scope']=scope
    aud.append(a)
au(1,'insertion; struck passage; C/H different words',B['P01'],r'''\deleted{On dit}\inserted{Soit} $T$ un voisinage
\deleted{tubulaire}\inserted{conique} de $Y\subset X$
dans $X$, posons''')
au(2,'struck passage; handwritten number; C/H different words',[280,220,1625,490],r'''\[
(11)\qquad X^*=X\setminus\mathring T=(X\setminus T)\cup\dot T
\]
c'est une partie fermée de $X$. \deleted{On dit que}''','Formula (11), closedness sentence, and full cancelled On dit que. The low q descender is completed in P03’s upper overlap.')
au(3,'handwritten number; C/H different words; less than high confidence departure',B['P03'],r'''\uline{Prop\unsure{.}} Conditions équivalentes (où $\lambda\in]0,1[$ donné)
a) $\dot T$ est une partie-bord de $X^*=X\setminus\mathring T$''','Heading and condition a; the previous cancelled q tail at the upper edge is context only.')
au(4,'struck passage; doubtful formula; C/H different words; less than high confidence departure',B['P04'],r'''b) Il existe un homéomorphisme de $X$
avec lui-$=$, transformant $T,\dot T$ en
$\deleted{\unsure{\lambda}}T_\lambda,\dot T_\lambda)$''')
au(5,'struck passage; handwritten number; C/H different words',B['P05'],r'''b') Comme b, mais en supposant de plus
que l'homéomorphisme induit l'identité
sur $T_{\lambda'}$ (où \deleted{$0<\lambda'<\lambda$}
$\lambda'$ est donné, $0<\lambda'<\lambda$).''')
au(6,'struck passage; C/H different words; less than high confidence departure',B['P06'],r'''c) Il existe un voisinage \deleted{tubulaire} cônique $T'$
de $Y$ dans $X$, \deleted{tel que et \unsure{a}} tel que $T=\lambda T'$,''')
au(7,'C/H different words',B['P07'],r'''l'isomorphisme étant compatible avec les
structures de voisinages côniques.''','Two main compatibility baselines; transverse marginal fragments at the bottom are excluded.')
au(8,'struck passage; C/H different words',B['P08'],r'''On dit alors que $T$ est un vois. \deleted{tub.} conique
\uline{strict} dans $X$''','Main strict-definition baseline only; overlapping transverse note and preceding q descender are excluded.')
au(9,'margin note; doubtful formula; handwritten number; C/H different words; less than high confidence departure',B['P09'],r'''\margin{Il vaut mieux de definir les voisinages côniques
\unsure{strict|stricts} comme \unsure{des} \uline{germes} de voisinage
plus grand $(1+\varepsilon)T\unsure{-R_{>0}}$
$(\varepsilon>0)$}''','Only the transverse marginal note, rotated clockwise 35 degrees. Main On dit, Corollaire headings, boundary T and other upright main text visible in the frame are excluded.')
au(10,'struck passage; C/H different words',B['P10'],r'''\uline{Corollaire} Quand $T$ est vois. \deleted{tub.} con. strict dans $X$,
$\dot T$ est la frontière de $T$ dans $X$.''','The two main corollary baselines; transverse marginal formula fragments at the left are excluded.')
au(11,'insertion; struck passage; doubtful formula; C/H different words; less than high confidence departure',B['P11'],r'''\uline{Corollaire} Si \deleted{il est}
\unsure{\deleted{$A$}|$A$}\inserted{$T$} voisinage
\deleted{tubulaire}\inserted{conique} de $Y$''','Whole first line of second corollary with both raised replacements and the uncertain triangular group. The upper diagonal belonging to the previous f descender is excluded as independent ink.')
au(12,'insertion; struck passage; handwritten number; C/H different words',B['P12'],r'''dans $X$, les $T_\lambda$ $(\lambda\in]0,1[)$ sont des voisinages
\deleted{tubulaires}\inserted{coniques} stricts''')
au(13,'margin note; handwritten number',B['P13'],r'\margin{14}')

doubts=[
 dict(place='P03 proposition abbreviation stop',reading=r'\uline{Prop\unsure{.}}',alternatives='Stop after Prop possible; no secure independent point.',confidence='medium',reason='The few tiny marks after/above the p differ in darkness from the written letters; the underline is clear. No certainty-only collation row is created.'),
 dict(place='P04 crossed prefix and opening-parenthesis scope',reading=r'\deleted{\unsure{\lambda}}T_\lambda,\dot T_\lambda)',alternatives='Lambda-like crossed token preferred; it may absorb an opening-parenthesis trace. No separate live opening arc is supplied.',confidence='medium',reason='Oblique hatching crosses a lower fork; the nearby short downturned stroke is continuous with T’s cap. The final closing parenthesis is clear.'),
 dict(place='P06 cancelled final token',reading=r'\deleted{tel que et \unsure{a}}',alternatives='a-like predecessor after tel que et.',confidence='medium',reason='The low oval and return are crossed; every stroke cannot be isolated.'),
 dict(place='P09 marginal strict ending',reading=r'\unsure{strict|stricts}',alternatives='Strict preferred; stricts possible.',confidence='medium',reason='No independent final s can be separated after the t, unlike the distinct small s in the final main stricts.'),
 dict(place='P09 marginal des',reading=r'\unsure{des}',alternatives='des candidate retained; not resolved.',confidence='low',reason='The small group is obscured by overlapping upright main-text Corollaire ink.'),
 dict(place='P09 marginal final mathematical group',reading=r'\unsure{-R_{>0}}',alternatives='Minus followed by R-like glyph and low >0-like group; exact token/subscript unresolved.',confidence='medium',reason='The minus is clear, but the loop/leg and lower shapes are cramped. The whole surrounding formula was inspected.'),
 dict(place='P11 extra triangular ink',reading=r'\unsure{\deleted{$A$}|$A$}',alternatives='Cancelled A-like token, live A-like token, or nonlexical insertion caret; no reading as un is supplied.',confidence='low',reason='Two oblique legs, high apex and middle crossbar are visible, with a cancellation across the feet. Token identity and state/function cannot be certified.')
]
notes=[
 dict(id='N01',text='Undated handwritten page: formula (11) defines X*=X minus circled T=(X minus T) union dotted T and calls it a closed part of X. The proposition lists a), b), b-prime), and c) as equivalent conditions for a given 0<lambda<1; it then names a strict conic neighbourhood. A transverse note proposes germs of larger neighbourhoods. Two corollaries assert an ambient-frontier identity and strictness of scaled neighbourhoods. This is a transcription-only content account, not a proof of those statements.'),
 dict(id='N02',text='Local source distinctions: every ordinary T has one cap and stem, without a further bar. Hollow-circle interior and filled-dot boundary symbols are distinct. Circumflexes are retained in cônique/côniques where visible; the author’s lui-= abbreviation is not expanded. Condition b has a clear final closing parenthesis but no separate live opening arc. Missing final stops after the strict definition and the last corollary are preserved. The additional triangular group in the second corollary is retained with token/state/caret uncertainty.'),
 dict(id='N03',text='Conditional root counterexample to the opening closedness claim, using the literal cone-neighbourhood interpretation supplied by root (the first reader did not inspect another leaf): let X=([0,1]×{0}) union ({3/8}×[0,1]), Y={(0,0)}, T=[0,1/2]×{0}, dotted T={(1/2,0)}, with scalar action lambda·(t,0)=(lambda t,0). T is a closed neighbourhood of Y carrying the absolute cone structure. Its circled part is [0,1/2)×{0}. Therefore X*=X minus circled T omits the junction q=(3/8,0), but contains points (3/8,s) for s>0 tending to q. X* is not closed in X, although the displayed set identity (11) remains valid. The literal sentence “c’est une partie fermée de X” is unchanged.'),
 dict(id='N04',text='Conditional root counterexample to the proposed equivalence in the same space, at the proposition parameter lambda=1/2: condition a holds under the collar interpretation supplied by root, since dotted T has the collar [1/2,1]×{0} inside X*. Condition c holds with T-prime=[0,1]×{0}; then T=lambda T-prime and the scalar structures agree. Condition b fails because every homeomorphism of X fixes its unique valence-three point q=(3/8,0), whereas q lies in T but not lambda T=[0,1/4]×{0}. Consequently b-prime, which adds requirements to b, also fails. These facts refute equivalence under the stated literal hypotheses; no corrected equivalence is claimed.'),
 dict(id='N05',text='Qualification of the first frontier corollary in the same conditional example: the ambient frontier of T is {q,(1/2,0)}, whereas dotted T is only {(1/2,0)}. Thus if strictness is assigned by either a or c as proposed equivalent criteria, that corollary fails in this example. This does not assert failure under a definition that independently requires b. The obstruction is missing control of the ambient openness of circled T, not an error to be silently repaired in the transcription. No general sufficiency theorem for an added hypothesis is proved here.'),
 dict(id='N06',text='The root supplied the example and its cone/collar interpretation; reader_a rechecked the coordinate membership, limiting vertical points, and valence obstruction in the course of recording it. Other-page definitions were not independently read. The second corollary and the marginal germ proposal are preserved without a separate general proof. The terminal marginal -R_{>0}-like group remains a reading doubt and receives no mathematical expansion.'),
 dict(id='N07',text='Layout and hand attribution: the transverse note overlaps rectangular frames of main On dit and Corollaire text, which are not duplicated as marginal words. The small arrow-like stroke above the raised second-corollary T is the descender of the preceding frontière f, not an independent insertion arrow. The lower portion of the leaf is blank apart from thin foliation 14, whose hand attribution is indeterminate.')
]
checks=[
 dict(statement_id=P+'.N01',type='carried as background without fault found',outcome='Transcription-only summary; the stated equivalence and corollaries are not certified by this item.'),
 dict(statement_id=P+'.N02',type='used and rechecked in this run',outcome='Local visual comparison of ordinary/decorated T, written accents, abbreviations, parentheses and punctuation. No mathematical emendation.'),
 dict(statement_id=P+'.N03',type='refuted, with refined id',outcome='Root supplied the explicit branched-interval example; reader_a rechecked that vertical points in X* converge to the excluded junction. Closedness fails under the supplied literal cone interpretation. The missing ambient-interior control is discussed in N05.'),
 dict(statement_id=P+'.N04',type='refuted, with refined id',outcome='Root’s collar/scaling construction supplies a and c; the unique valence-three junction obstructs b and hence b-prime at lambda=1/2. This is a targeted counterexample, conditional on the cone/collar interpretation, not a re-proof of preceding definitions. The refined ambient-interior issue is N05.'),
 dict(statement_id=P+'.N05',type='targeted proof check',outcome='In the same example the two-point ambient frontier differs from dotted T. The corollary diagnostic is explicitly conditional on strictness being assigned via a or c; no assertion of a sufficient corrected hypothesis.'),
 dict(statement_id=P+'.N07',type='used and rechecked in this run',outcome='Visual/layout comparison separated crossing margin text from upright main text and traced the upper diagonal to the preceding f descender.')
]
notation=[
 dict(form=r'X^*=X\setminus\mathring T=(X\setminus T)\cup\dot T',meaning='Definition (11) of the exterior-with-boundary set; the claimed ambient closedness is recorded separately.',evidence='P02 complete formula with 11, star, hollow circle, plain T and filled dot.'),
 dict(form=r'T, T_\lambda, T_{\lambda\'}, T\'',meaning='Ordinary cone-neighbourhood symbols, with locally written lambda/prime decorations and no independent overbar.',evidence='P01/P02/P04–P06/P08/P10–P12: each ordinary T has one cap and stem.'),
 dict(form=r'\mathring T,\ \dot T',meaning='Interior/circled part and boundary/dotted part distinguished by hollow versus filled upper marks.',evidence='P02/P03 and the paired forms in P04/P10.'),
 dict(form='lui-=',meaning='lui-même, written with a hyphen and equals sign.',evidence='P04 short hyphen followed by two horizontal strokes.'),
 dict(form='partie-bord',meaning='Written term in condition a; not expanded to bordante.',evidence='P03 separate hyphen and four-letter bord followed immediately by de.'),
 dict(form=r'(1+\varepsilon)T\unsure{-R_{>0}}',meaning='Marginal larger-neighbourhood expression; ending remains unresolved and is not mathematically expanded.',evidence='P09 full transverse formula and separate final (epsilon>0).'),
 dict(form=r'\unsure{\deleted{$A$}|$A$}',meaning='Additional triangular group in the second-corollary revision; token/state and possible insertion-caret function are unresolved.',evidence='P11 high apex, two legs, middle crossbar and old cancellation at the feet.')
]
for q in notation:q['form']=q['form'].replace("\\'", "'")
abbreviations=[
 dict(form=r'Prop\unsure{.}',expansion='Proposition; presence of the stop remains doubtful.'),
 dict(form='vois.',expansion='voisinage'),dict(form='tub.',expansion='tubulaire; cancelled locally'),
 dict(form='con.',expansion='conique'),dict(form='lui-=',expansion='lui-même; source equals-sign abbreviation retained')
]
hand=[
 dict(habit='Ordinary T has one long cap, sometimes detached from the descending stem; dots and hollow circles are separate marks.',places='All T occurrences in P01–P12',consistency='No independent bar found on an ordinary T anywhere on this assigned leaf.',witness_errors='C repeatedly supplies a bar; H plain T is supported locally.'),
 dict(habit='A short flat arch above o is a genuine circumflex in several conic words.',places='P06 cônique, P07 côniques, and marginal P09 côniques',consistency='Three detached arches; other conique/coniques occurrences have no such separate mark.',witness_errors='Both witnesses normalize these locally accented forms to conique/coniques.'),
 dict(habit='Compact word endings can be short terminal returns rather than additional plural letters.',places='P07 isomorphisme/compatible; P09 strict(s); P12 stricts',consistency='P07 singular endings are clear; marginal strict(s) remains uncertain; P12 has a distinct terminal s.',witness_errors='H adds plural s to isomorphisme and compatible. C’s marginal stricts is not secure.'),
 dict(habit='Upper descenders and transverse notes can cross later main-text objects.',places='P08/P09 margin overlap; P10/P11 frontière f descender',consistency='Crossing strokes were traced before assigning cancellation or insertion-arrow function.',witness_errors='H’s marginal wording/order incorporates unsupported expansions; the f-descender tip must not be counted as a separate arrow.'),
 dict(habit='A target T roof can have a downturned end resembling an opening parenthesis.',places='P04 target pair',consistency='No independent opening arc is separable from the roof or cancelled prefix.',witness_errors='Both witnesses supply a live opening parenthesis; only the final closing parenthesis is secure.'),
 dict(habit='Equals sign can stand for même in prose.',places='P04 lui-=',consistency='Two explicit horizontal strokes after a hyphen.',witness_errors='H expands the written abbreviation to lui-même.')
]
reviews=[
 dict(text='On dit / Soit',scope_attachment='On dit cancelled; Soit inserted above as the opening replacement.',evidence='P01 separate raised word above the long baseline cancellation.'),
 dict(text='Opening tubulaire / conique',scope_attachment='Whole tubulaire cancelled, conique inserted above it.',evidence='P01 the horizontal strike crosses old letters; the raised conique bodies are live.'),
 dict(text='On dit que',scope_attachment='Whole phrase after the closedness sentence cancelled.',evidence='P02 long stroke through the phrase; q descender completed by the P03 overlap.'),
 dict(text='Condition b lambda-like prefix',scope_attachment='Crossed group retained; no separate live opening parenthesis added.',evidence='P04 lower fork under oblique hatching; adjacent roof hook belongs to T.'),
 dict(text='First b-prime inequality',scope_attachment='Only the first 0<lambda-prime<lambda is cancelled; the rewritten parameter statement and final inequality remain live.',evidence='P05 continuous crossing ends before the live lambda-prime.'),
 dict(text='Condition c tubulaire',scope_attachment='Cancelled before live cônique T-prime; cônique is on the main baseline.',evidence='P06 strike through old word and detached circumflex over the live o.'),
 dict(text='tel que et a-like token',scope_attachment='Whole old phrase cancelled before the repeated live tel que.',evidence='P06 long stroke traverses all old words and the final doubtful token.'),
 dict(text='Strict-definition tub.',scope_attachment='Only tub. cancelled; conique strict remains live and strict underlined.',evidence='P08 strike through short abbreviation, followed by live word bodies and independent underline.'),
 dict(text='First-corollary tub.',scope_attachment='Short tub. cancelled; con. and subsequent strict remain live.',evidence='P10 local crossing followed by a separate con. stop.'),
 dict(text='Second-corollary il est and triangular group',scope_attachment='il est cancelled; the following triangular token/state or caret function remains explicitly uncertain; T raised as replacement.',evidence='P11 separate apex/legs/crossbar beneath the raised T. The previous f descender is not an independent arrow.'),
 dict(text='Second-corollary tubulaire / conique',scope_attachment='tubulaire cancelled; conique inserted above it.',evidence='P11 long baseline strike and live raised word; its q descender crosses the old line without cancelling the insertion.'),
 dict(text='Final tubulaires / coniques',scope_attachment='Plural tubulaires cancelled; plural coniques raised above it.',evidence='P12 strike through old plural bodies, with distinct live replacement and final stricts.')
]
rows=list(csv.DictReader((R/'packets'/P/'differences.tsv').open(),delimiter='\t'))
assert len(rows)==22,len(rows)
disp={
1:'H editorial leaf-order note excluded; no other pages inspected.',2:'Continuation of H editorial note excluded.',
3:'Macro-only hollow-circle notation; P02 verifies the actual circle.',4:'P03_a: où, not si; C candidate supported.',
5:'Macro-only TeX thin space \\,; no literal comma.',6:'P03_a: no colon after the closing parenthesis.',
7:'P03_b: literal partie-bord, not bordante.',8:'Macro-only hollow-circle notation; P03 whole formula read.',
9:'P04_a: avec, not sur.',10:'P04_b: written equals abbreviation retained.',
11:'P04_c: crossed lambda-like group retained; opening-parenthesis scope separately corrected.',
12:'P05_a: induit, not induise.',13:'P05_b: où, not si; whole crossed/live inequalities read.',
14:'P06_b: crossed a-like candidate retained unresolved, not omitted.',
15:'P07_a: singular l’isomorphisme.',16:'P07_b: singular compatible.',
17:'P08_b removes unsupported final stop; P09_a–d retain the full transverse note with local doubts and accents.',
18:'P11_a: il est cancelled, additional triangular group retained, T raised; no unsupported est un after T.',
19:'P11_a: source rewrite and extra group preserved; H’s un not visible.',
20:'Macro-only TeX thin space \\,; no literal comma.',
21:'P09_a–d read the continuous margin; P12_b no terminal stop; P13_a foliation14. H explanatory note is not source text.',
22:'P13_a foliation14 retained; H editorial statement about blank lower leaf excluded.'}
diff=[dict(row=i,disposition=disp[i]) for i in range(1,23)]
report=dict(page=P,reader='reader_a',line_count=sum(bool(x.strip()) and not x.lstrip().startswith('%') for x in D.splitlines()),
 line_count_basis='Nonempty logical draft rows excluding comments, including display delimiters; not a claimed count of physical manuscript baselines.',
 changes=changes,decisions=decisions,inventory=inv,audit_boxes=aud,doubts=doubts,notes=notes,check_events=checks,notation=notation,abbreviations=abbreviations,hand=hand,diff_coverage=diff,deletion_insertion_review=reviews,
 inspection=dict(source='source/SP89_C13_149+150_scans/150_scan015.jpg',source_size=[1685,2362],whole_image_views=1,native_half_views=[1,1],native_half2_offset_y=1063,crop_count=13,crop_views={k:1 for k in B},crop_transform={'P09':{'rotation_degrees_clockwise':35}},ocr=False,outside_research=False,tex_compilation=False,other_page_access=False,crop_view_note='All thirteen stable frames inspected once by reader_a; root independently reviewed all thirteen. No new framing, recropping or first-reader image rereading. Root reopened the same P11 frame solely for the still-open triangular-group scope.'),
 completion_status='First-reader artifacts prepared; root finalization required.')
(O/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
def norm(s):return re.sub(r'\s+',' ','\n'.join(x for x in s.splitlines() if not x.lstrip().startswith('%'))).strip()
problems=[]
for q in changes:
    for k,s in [('c',C),('h',H),('final',D)]:
        if norm(q[k]) not in norm(s):problems.append((q['id'],k,q[k]))
for q in decisions:
    if norm(q['reading']) not in norm(D):problems.append((q['id'],'reading',q['reading']))
for q in aud:
    if norm(q['reading']) not in norm(D):problems.append((q['box'],'reading',q['reading']))
print(json.dumps({'changes':len(changes),'marks':len(decisions),'inventory':len(inv),'audit_boxes':len(aud),'diff_rows':len(diff),'logical_rows':report['line_count'],'excerpt_problems':problems},ensure_ascii=False,indent=2))
