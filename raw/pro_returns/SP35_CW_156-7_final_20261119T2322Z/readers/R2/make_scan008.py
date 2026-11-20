from pathlib import Path
import json
from datetime import datetime, timezone

root=Path('/workspace/scratch/2b715fe259c4/SP35_CW_156-7/readers/R2')
manifest=json.loads((root/'scan008_crops.json').read_text())
cm={Path(x['file']).stem.replace('scan008_',''):x for x in manifest}
compat=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
# Guide curves represent interlinear additions, not lexical underlining.
def guided(words):
    return (r'\tikz[baseline=(g.base),every node/.style={inner sep=0pt}]{'
        r'\node (g) at (0,0) {}; '
        r'\node[anchor=base west] (a) at (.1em,1.8ex) {\inserted{'+words+r'}}; '
        r'\draw (0,-.15ex) .. controls (.2em,1.1ex) and ([xshift=-.6em,yshift=-.5ex]a.base east) .. ([xshift=.1em,yshift=-.35ex]a.base east);}')
tex=r'''\scanpage{8}\mspage{7}
Je voudrais maintenant faire passer les axiomes de disjonction-compatibilité avant ceux sur les lieux, pour ne pas @AIR@ les en faire dépendre. Les axiomes sont ``facultatifs'' pour un atelier, et il y aura pas mal des' implications mutuelles avec les axiomes sur les lieux.

Une notion essentielle ici est celle de ``$F$ et $G$ \uline{disjoints}''
\[
 F\parallel G\ \overset{\mathrm{dfn}}{\Longleftrightarrow}\ F@COMPAT@G\quad\text{et}\quad F\cap G=\varnothing_F
\]
notion qui ne dépend que de $\leq$. On a d'ailleurs
\[
 F\parallel G\ \Longleftrightarrow\ \forall X\in\widetilde F,\ Y\in\widetilde G,\quad X\parallel Y
\]
donc interprétation en \unsure{termes|terme} de $X\parallel Y$ dans $M$, qui y signifie
\[
\begin{aligned}
X\mathrel{\underset{M}{\parallel}}Y\ \Longleftrightarrow\
 X\mathrel{\underset{M}{@COMPAT@}}Y\quad &\text{et}\quad\{X,Y\}\ \text{n'est \uline{pas}}\\
&\text{minoré dans } M,\leq\\
&\text{i.e. }\nexists Z\ \text{avec }Z\leq X,Z\leq Y
\end{aligned}
\]

% First NB verb: only the t/ending region is overwritten. The earlier suffix
% tera is conjectural; the shared initial resul- is not separately struck.
(\uline{NB} Il résul\deleted{\unsure{tera}}\inserted{te} des axiomes @PRECEDENTS@ que ça implique que $\nexists Z$ avec $Z\ll X,Z\ll Y$, \deleted{i.e. c'est un $\exists$} et \deleted{la} réciproque résultera \unsure{d'axiome|d'axiomes} ci-dessous\ldots)

% The following At DC1/Cor draft is crossed by three long diagonal strokes.
% One of those strokes begins in, and crosses, the slanted left-margin note.
% Global cancellations are represented by deleted; nested deleted records
% the smaller local cancellations that predate the global abandonment.
\reversemarginpar
\margin{\deleted{Un atelier sera dit \uline{spacieux} s'il satisfait cette condition. Contre-ex. : les ateliers simpliciaux\ldots}}%
\normalmarginpar
\deleted{\uline{At DC} 1 \quad (\uline{Axiome des ateliers spacieux}) Soient $X,Y\in M$, \inserted{soit} \deleted{\unsure{et}} $K=X\cap Y=\underset{Z\in\widetilde X\cap\widetilde Y}{\mathrm{Sup}}\,Z$. \deleted{\unsure{Il}} Supposons que \inserted{pour $X',Y'\in M$}}
\[
\deleted{\deleted{\forall}\ X'\ll X,\ X'\parallel K,\ Y'\ll Y,\ Y'\parallel K\ \Longrightarrow\ X'\parallel Y'.}
\]
\deleted{Alors [NB et alors seulement\ldots\
\tikz[baseline=(b.base),every node/.style={inner sep=0pt}]{\node (b) at (0,0) {}; \node[anchor=base west] at (0,-1.6ex) {\inserted{cf Cor}}; \path (0,0)--(3.6em,0);}
] $X@COMPAT@Y$.}

% The first overwritten index shows F on X, without a securely detached tilde.
% A single visible wave is above the second G/Y correction; its attribution
% to the old Y layer is unresolved, hence the old-layer alternative below.
\deleted{\uline{Cor} Soient $F,G\in\mathscr F$, $K=F\cap G=\underset{Z\in\deleted{X}\inserted{F}\cap\deleted{\unsure{\widetilde Y|Y}}\inserted{\widetilde G}}{\mathrm{Sup}}\,Z$.}
\[
\begin{aligned}
&\deleted{\text{Alors } F@COMPAT@G\quad \text{\tikz[baseline=(s.base)]{\node[inner sep=1pt] (s) {ses};\draw (s.center) ellipse [x radius=1.05em,y radius=.72em];}}\quad \forall X,\deleted{\unsure{\varphi|y}}\inserted{Y}\in M}\\
&\deleted{X\ll F,\ Y\ll G,\ X\parallel K,\ Y\parallel K\ \Longrightarrow\ X\parallel Y}
\end{aligned}
\]
'''
tex=tex.replace('@COMPAT@',compat).replace('@AIR@',guided("avoir l'air de")).replace('@PRECEDENTS@',guided('précédents'))
(root/'scan008.tex').write_text(tex)

rows=[]
def add(place,C,H,reading,dc,dh,kind,conf,evidence,crop=None,doubt='not applicable',marked=False,math=None):
    x={'id':f'R2-008-{len(rows)+1:02d}','place':place,'C':C,'H':H,'reading':reading,'diff_C':dc,'diff_H':dh,'kind':kind,'marked_in_H':marked,'confidence':conf,'evidence':evidence,'crop':cm[crop]['file'] if crop else None,'crop_coordinates':cm[crop]['box'] if crop else None,'C_doubt_status':doubt,'math_consequence':math}
    rows.append(x); return x['id']

add('opening paragraph before avant','no insertion here','inserted uncertain moins élégants','no moins élégants',False,True,'text not on the page','high','The small interlinear words occur later, above pour ne pas / les en faire dépendre; no group saying moins élégants is written before avant.',marked=True)
add('opening paragraph after pour ne pas',r'\inserted{avoir l’air de}','omitted','interlinear avoir l’air de, anchored before les en faire dépendre',False,True,'omission','high','The four small words avoir l’air de are legible above the baseline and belong after pour ne pas.')
add('guide beneath avoir l’air de','addition marked, guide undrawn','addition omitted','curved insertion guide drawn',True,True,'drawing or diagram','high','A low curved stroke leads from the insertion position and passes beneath the interlinear phrase; it is not a straight lexical underline.')
add('quotes around facultatifs',"``facultatifs''",'« facultatifs »',"``facultatifs''",False,True,'other','high','Both sides have paired short high strokes, rather than angle-shaped guillemets.')
d_des=add('opening line before implications',r"\unsure{des'|des|d'}","d'", "des'",True,True,'misread word','medium','A d-like loop continues through a low e/s-like stretch, followed by a separate raised apostrophe. The extra connected strokes are retained although the resulting phrase is unusual.','des','resolved')
add('quotes around F et G disjoints',"``F et G disjoints''",'« F et G disjointes »',"``F et G disjoints''",False,True,'other','high','Paired short quotation strokes enclose the expression; the closing marks are not guillemets.')
add('word disjoints','disjoints','disjointes','disjoints, underlined',False,True,'misread word','high','The ending runs from t directly to s; no intervening e loop is present. The word is underlined.')
d_def=add('label above first equivalence',r'\unsure{\mathrm{defn}|\mathrm{défn}}',r'\mathrm{déf}',r'\mathrm{dfn}',True,True,'abbreviation expanded or spelling modernised','medium','Three connected groups give d, a tall f, and a short terminal n. No separately formed e, accent, or final full word is visible.','defn','changed')
d_empty=add('subscript under first empty sign',r'\unsure{\mathscr F|\mathcal F|F}',r'\mathfrak F','F',True,True,'misread symbol or index','high','A plain F has one stem, a straight top arm, and a second cross-arm; it lacks the loops of the later figure-family capital.','emptyF','resolved')
add('sentence before second equivalence','On a d’ailleurs','On a d’autre part','On a d’ailleurs',False,True,'misread word','high','The compressed single word after d’ is ailleurs; there is no second word part.')
add('transition after second equivalence','donc interprétation','d’où interprétation','donc interprétation',False,True,'misread word','high','The leading word ends in a short c, not an accented où.')
d_terms=add('transition en termes',r'\unsure{termes|terme}','termes',r'\unsure{termes|terme}',False,True,'other','medium','The terminal low wave can include a compressed s, but it does not separate that letter securely from the end of e. The plural remains preferred, with singular retained.','termes','retained')
d_M=add('M in transition, relation subscripts, and subsequent quantifications',r'\unsure{M|\mathcal M} initially; M subsequently',r'\mathcal M','M throughout this page',True,True,'misread symbol or index','medium','Two rising strokes joined by a bowed valley form the familiar M. This occurrence has no additional calligraphic loop or flourish; plain M is selected locally.','M','resolved')
add('stratum non-minoration statement','n’est underlined pas','n’est pas','n’est underlined pas',False,True,'omission','high','A short rule lies directly under pas; no comparable rule is under the adjacent words.')
add('parenthetical NB heading','NB underlined','NB without underline','NB underlined',False,True,'omission','high','The small separate horizontal rule lies below NB.',crop='NB')
d_oldverb=add('first NB verb: old layer and extent of correction',r'\deleted{\unsure{résultera}} followed by another entire verb','no old layer',r'résul\deleted{\unsure{tera}}\inserted{te}',True,True,'deletion state (struck given live or live given struck)','low','The initial résul- is legible and not separately cancelled. Dense overlapping bars and loops affect the t/ending region only. An earlier tera is possible, but not all of its letters can be recovered independently; no second full verb is written. The suffix segmentation is a diplomatic approximation to an in-place overwrite.','NB','changed')
d_liveverb=add('first NB verb: current layer',r'\unsure{résulte|résultera}','résultera','résulte',True,True,'misread word','medium','After the legible résul-, a tall t-like stem and final e-shaped horizontal return give résulte. The current word has no separately continuing ra group.','NB','resolved')
add('précédents insertion guide','inserted précédents; no drawn guide','inserted précédents; no drawn guide','interlinear précédents with curved insertion guide, not underline',True,True,'drawing or diagram','high','The curved stroke starts at the gap between axiomes and que and rises beneath the added word. Its low left attachment marks insertion; the curve is distinct from the straight underline below NB.','NB')
add('NB after que','ça',r'\ill{}','ça',False,True,r'readable ink left as \ill{}','high','The small ç-shaped first letter and following a are visible before implique.','NB')
add('NB verb after ça','implique','uncertain indique','implique',False,True,'misread word','high','The central tall descending loop belongs to p, followed by the l/i/q/u/e sequence; indique would not account for the long p descender.','NB',marked=True)
d_ie=add('cancelled NB clause: initial abbreviation',r'\unsure{i.e.}','i.e.','i.e.',True,False,'other','medium','Two short letter strokes with separated point marks remain below the cancellation rule.','NB','resolved')
add('cancelled NB clause: words after i.e.',"c’est un",r'\ill{}',"c’est un",False,True,r'readable ink left as \ill{}','medium','The c, apostrophe/t group, and final joined un are still distinguishable under the single long horizontal cancellation.','NB')
d_exists=add('cancelled NB clause: final sign',r'\unsure{\exists}',r'\ill{}',r'\exists',True,True,'misread symbol or index','medium','A right-hand upright with leftward bars gives a reversed-E existential sign. The horizontal cancellation crosses it but does not supply a new negation stroke.','NB','resolved')
d_la=add('NB article before réciproque',r'\deleted{\unsure{la}}','live la',r'\deleted{la}',True,True,'deletion state (struck given live or live given struck)','medium','A tall looping l and short following a sit under a dense local horizontal cancellation, distinct from the line above.','NB','resolved')
add('NB second occurrence of résultera','résultera','uncertain résultera','résultera',False,True,'other','high','The second word is uncancelled and shows the full continuing tera ending.','NB',marked=True)
d_axiom=add('NB final line at page edge',r"\unsure{d'axiome|d'axiomes}","d'axiome",r"\unsure{d'axiome|d'axiomes}",False,True,'other','low','The readable stem is d’axiome. Its low ending approaches the edge and does not securely distinguish e alone from es; no grammar-based resolution is made.','NB','retained')
add('entire At DC1 and Cor lower draft','entire draft deleted','live text plus note describing three cancellation strokes','entire draft deleted; local earlier deletions retained separately',False,True,'deletion state (struck given live or live given struck)','high','Three long oblique strokes traverse the At DC1 statement, its implication, and the Cor section. They cancel the whole lower draft, beyond the smaller local cancellations.',math='The lower material is an abandoned formulation, not an additional live axiom on this sheet.')
add('slanted left-margin note: cancellation state','live marginal note','live note, with editorial observation that one deletion line cuts it','whole marginal note cancelled with lower draft',True,True,'deletion state (struck given live or live given struck)','medium','In the rotated crop a long stroke crosses the sera / s’il / condition region and continues into the At DC1 area below. It is the continuation of a global cancellation, not a letter or lexical underline.','margin')
add('margin adjective','spacieux','spécieux','spacieux, underlined',False,True,'misread word','high','The third letter has a rounded a form; no accent is visible. A straight rule underlines the word.','margin')
add('margin demonstrative','cette','uncertain cette','cette',False,True,'other','high','The short initial c and double tall t group followed by e are readable.','margin',marked=True)
add('margin punctuation after condition','condition.',r'condition \ill{}','condition.',False,True,r'readable ink left as \ill{}','medium','A small terminal dot follows condition; there is no additional word before Contre-ex.','margin')
add('margin abbreviation','Contre-ex. :','uncertain contre-ex. :','Contre-ex. :',False,True,'other','high','The initial C is capital, the internal hyphen and final abbreviation point are visible, followed by a colon.','margin',marked=True)
add('margin example noun','les ateliers','les lieux','les ateliers',False,True,'misread word','high','After les, the longer a/t/e/l/i/e/r/s sequence occupies the next slanted line; it is not lieux.','margin')
add('margin final adjective','simpliciaux',r'\ill{} \ill{}','simpliciaux…',False,True,r'readable ink left as \ill{}','high','The connected word has the central pl/i/c group and terminal aux followed by three dots.','margin')
add('At DC1 underline extent','At DC underlined; numeral 1 outside','At DC 1 all emphasized','At DC underlined; numeral 1 outside',False,True,'other','high','The ruled segment finishes with DC; the numeral 1 is separately written beyond the rule.')
add('At DC1 title adjective','spacieux','spécieux','spacieux',False,True,'misread word','high','The letter after sp is a, without an accent, as in the margin note.')
d_soient=add('At DC1 initial verb',r'\unsure{Soient}','Soient','Soient',True,False,'other','medium','The initial S, joined o/i/e/n sequence and final tall t are visible despite the crossing oblique stroke and an overdrawn terminal stroke.','Soient','resolved')
d_soit=add('At DC1 left interlinear addition before K',r'\inserted{\unsure{soit}}','omitted',r'\inserted{soit}',True,True,'omission','high','The small added word shows s, a rounded o, a dotted i and crossed t. It lies left and slightly below the main K line.','soitet','resolved')
d_et=add('At DC1 old conjunction before K',r'\deleted{\unsure{et}}','omitted',r'\deleted{\unsure{et}}',False,True,'omission','low','A short elongated loop and low return remain under a heavy horizontal cancellation immediately before K. No independent tall t is secure; et is retained only as a doubtful reconstruction, not from grammar.','soitet','retained')
add('At DC1 K placement','baseline K','inserted K','baseline K; soit is the interlinear addition',False,True,'insertion or placement','high','The K stands on the main formula baseline, with the little added soit separate to its left.','soitet')
d_Il=add('At DC1 old word before Supposons',r'\deleted{\unsure{Il}}','omitted',r'\deleted{\unsure{Il}}',False,True,'omission','low','A small dense locally crossed group has tall looped strokes consistent with Il, but its interior is too merged for certainty.','Il','retained')
add('At DC1 quantification addition',r'\inserted{pour X′,Y′∈M}','live pour; inserted tous; live X′,Y′∈M','whole pour X′,Y′∈M is interlinear',False,True,'insertion or placement','high','The entire short phrase including pour and both primed variables occupies the added line, beneath Supposons que.')
add('At DC1 claimed tous','no tous','inserted tous','no tous',False,True,'text not on the page','high','No separate tous group lies between pour and the clearly primed X′.')
d_forall=add('At DC1 old quantifier before X′',r'\deleted{\unsure{\forall}}','omitted from text; note says a sign is crossed',r'\deleted{\forall}',True,True,'omission','medium','The remaining two sloping legs, lower meeting point, and transverse bar identify the inverted-A quantifier despite the dense local crossing.','forall','resolved')
add('At DC1 concluding NB bracket','et alors seulement…','il [ill.] dans tous les cas…','et alors seulement…',False,True,'misread word','high','The first two words are et alors and the following single word is seulement; the drawn sequence does not contain dans tous les cas.',math='The manuscript claims the converse too, but the whole assertion is cancelled.')
add('At DC1 bracket cross-reference punctuation','cf Cor','cf. Cor','cf Cor',False,True,'other','high','No dot is drawn after cf; Cor follows as a separate group.')
add('At DC1 bracket cross-reference placement','inserted cf Cor in running text','text plus note saying below bracket','inserted cf Cor below bracket',True,False,'insertion or placement','high','The small cf Cor sits beneath the end of the bracketed NB; the TeX preserves this lower position.')
add('Cor figure-set alphabet',r'\mathscr F',r'\mathfrak F',r'\mathscr F',False,True,'misread symbol or index','medium','The family capital has the looping, flowing form used for the figure family, rather than a blackletter structure. This differs from the plain lowered F at the top.')
d_oldX=add('Cor Sup index: first old object',r'\deleted{\unsure{\widetilde X|X}}','old object omitted',r'\deleted{X}',True,True,'omission','medium','Two diagonal X strokes survive under the added F. The marks above belong to the u/p of Sup; no detached tilde can be assigned to X.','cor_index','resolved')
d_newF=add('Cor Sup index: first replacement',r'\unsure{\widetilde F|F}',r'\widetilde F',r'\inserted{F}',True,True,'misread symbol or index','medium','The vertical stem and two rightward arms give F over X. The high curved stroke is connected to the descending p of Sup, unlike the detached wave above G; the first replacement is rendered without a tilde.','cor_index','resolved',math='With figures and their deployments kept distinct, the literal first F in Z∈F∩G-tilde omits the set/deployment decoration expected by the surrounding notation. It is not silently supplied.')
d_oldY=add('Cor Sup index: second old object',r'\deleted{\unsure{\widetilde Y|Y}}','old object omitted',r'\deleted{\unsure{\widetilde Y|Y}}',False,True,'omission','low','A fork survives within the G-shaped correction. There is one wave above the combined Y/G locus, but its chronological attribution to the old Y cannot be established.','cor_index','retained')
add('Cor Sup index: G replacement state','G-tilde after deleted old Y, not explicitly marked added','clean G-tilde','G-tilde explicitly marked as replacement',True,True,'insertion or placement','high','The G loop overlaps the old fork at the same location; the detached wave above it is clear. The notation records an overwrite, not two independent live adjacent symbols.','cor_index')
add('Cor equivalence abbreviation','ses','(ssi), note calls reading uncertain','ses',False,True,'abbreviation expanded or spelling modernised','high','Inside the oval the three groups are s, a small e loop, s; there is no final dotted i. No expansion is inserted.',marked=True,math='The likely equivalence meaning belongs to a note only; the literal abbreviation remains ses.')
add('Cor equivalence enclosure','oval drawn with TikZ','parentheses plus editorial note describing a circle','hand-drawn oval around ses',False,True,'drawing or diagram','high','A continuous oval encloses the abbreviation; it is not a pair of text parentheses.',marked=True)
d_oldphi=add('Cor quantified pair: old second letter',r'\deleted{\unsure{\varphi|y}}','omitted',r'\deleted{\unsure{\varphi|y}}',False,True,'omission','low','A rounded loop crossed by a stem remains under the new fork. It can be read as phi or a looped y, and no separate crop resolves the earlier layer further.','cor_variables','retained')
d_liveY=add('Cor quantified pair: replacement letter',r'\unsure{Y|y}','Y',r'\inserted{Y}',True,False,'other','medium','The surviving upper branches meet in a descending stroke and resemble the capital Y forms elsewhere in the displayed pairings. The old rounded loop is independently marked deleted.','cor_variables','resolved')
add('Cor quantified pair: punctuation after M','no comma','comma','no comma',False,True,'other','high','The quantified line ends at M; there is no separate comma before the following implication display.')
add('final implication: punctuation','no terminal full stop','terminal full stop','no terminal full stop',False,True,'other','high','The final Y is followed by blank paper, without a discrete period.')

rowmap={r['id']:r for r in rows}
def aud(C,place,status,rid):
    r=rowmap[rid]
    return {'C_reading':C,'place':place,'status':status,'evidence':r['evidence'],'crop':r['crop'],'crop_coordinates':r['crop_coordinates'],'difference_id':rid}
audits=[
 aud("des'|des|d'",'opening before implications','resolved',d_des),
 aud('defn|défn','first equivalence label','changed',d_def),
 aud('mathscr F|mathcal F|F','empty-figure subscript','resolved',d_empty),
 aud('termes|terme','transition','retained',d_terms),
 aud('M|mathcal M','transition after dans','resolved',d_M),
 aud('deleted résultera','NB old verb layer','changed',d_oldverb),
 aud('résulte|résultera','NB current verb','resolved',d_liveverb),
 aud('deleted i.e.','NB cancelled clause','resolved',d_ie),
 aud('deleted exists','NB cancelled final symbol','resolved',d_exists),
 aud('deleted la','NB before réciproque','resolved',d_la),
 aud("d’axiome|d’axiomes",'NB at right edge','retained',d_axiom),
 aud('Soient','At DC1 opening','resolved',d_soient),
 aud('inserted soit','At DC1 before K','resolved',d_soit),
 aud('deleted et','At DC1 before K','retained',d_et),
 aud('deleted Il','At DC1 before Supposons','retained',d_Il),
 aud('deleted forall','At DC1 implication line','resolved',d_forall),
 aud('deleted X-tilde|X','Cor first old index','resolved',d_oldX),
 aud('F-tilde|F','Cor first new index','resolved',d_newF),
 aud('deleted Y-tilde|Y','Cor second old index','retained',d_oldY),
 aud('deleted varphi|y','Cor old second quantified letter','retained',d_oldphi),
 aud('Y|y','Cor current second quantified letter','resolved',d_liveY)
]
end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
model='GPT-6 Astra Pro; inherited effort setting not exposed; R2'
report={
 'reader':'R2','scan':8,'start_utc':'2026-11-19 22:26:30 UTC','end_utc':end,'model':model,
 'images_viewed':['H156-01_156-7_scan008.jpg','H156-01_156-7_scan008_a.jpg','H156-01_156-7_scan008_b.jpg']+[x['file'] for x in manifest],
 'workflow_note':'Whole and both supplied halves viewed once. Thirteen unresolved loci were cropped once each. A combined tool response attempting the first five crop displays was fully truncated and conveyed no crop images to the model; the already-created files were then displayed in smaller batches, without recropping. Every crop listed was actually inspected using view_image. No scan009 manuscript, other reader output, main decision, or new S row was read.',
 'coverage':[
  'page number 7, entire opening paragraph, all paired quotation strokes, literal des\' and the exact avoir l’air de anchor and curved guide',
  'complete definition of F parallel G, dfn label, all relation strokes, equality, intersection, and plain lowered F',
  'complete all-strata equivalence: only one written forall, capital X/Y, both tildes, punctuation and double implication',
  'complete transition and M-disjointness characterization, both lowered M indices, braces, underline pas, lack of added parentheses around M,≤, and literal unqualified exists variable Z',
  'NB opening/closing parentheses, underline, in-place first-verb overwrite, inserted précédents and guide, ça implique, both refinements, entire locally erased clause, erased la, second résultera and final edge ending',
  'entire rotated left margin, exact spacieux and simpliciaux, underline, hyphen/point/colon/ellipsis, and crossing global cancellation',
  'three large diagonal cancellation strokes across the entire lower At DC1/Cor draft, distinguished from local erased ink',
  'At DC1 underline span, title, Soient, every variable and M, inserted soit, old et, baseline K, both deployed strata in Sup, old Il and added quantification without tous',
  'At DC1 cancelled forall, all four antecedent conditions, every prime, and non-negated final parallel relation despite the passing global diagonal',
  'At DC1 full Alors/et alors seulement bracket, cf Cor spelling and lowered insertion position, final compatibility relation',
  'Cor title, figure-family alphabet, F/G/K formula, all overwritten Sup indices, one visible second wave, lack of separate first tilde',
  'Cor literal ses within a drawn oval, quantifier, old phi/y and replacement Y, M and lack of trailing comma',
  'Cor final implication: all unprimed X/Y, lower F/G in refinement, disjointness with K, double implication arrow and lack of terminal full stop',
  'all 21 C doubt occurrences adjudicated; C notes relevant to this scan read; all agreed C/H words and signs inspected as well as differences'
 ],
 'notation':[
  {'form':'disjointness','reading':'parallel strokes; lowered M for stratum relation','evidence':'two roughly parallel short vertical/oblique strokes; no added negation at the lower consequent'},
  {'form':'compatibility','reading':'the same crossed pair of chevrons as earlier pages','evidence':'four angled arms meeting around the centre; drawn in TikZ'},
  {'form':'definition abbreviation','reading':'dfn','evidence':'three letter groups, no independent e or accent'},
  {'form':'empty figure subscript','reading':'plain F','evidence':'one stem and two straight arms; distinguished from Cor figure-family script F'},
  {'form':'M','reading':'plain M selected locally','evidence':'two stems with bowed join, without extra flourish; earlier page-font uncertainty is not silently rewritten'},
  {'form':'Cor equivalence abbreviation','reading':'ses in oval','evidence':'literal s-e-s, no dotted i; likely si et seulement si only as an interpretive expansion'},
  {'form':'insertion guides','reading':'avoir l’air de and précédents accompanied by curved guides','evidence':'curves link their interlinear words to the baseline positions; not lexical underlines'},
  {'form':'Cor first deployment index','reading':'plain F on old X','evidence':'overhead high curve belongs to p in Sup; the second G alone has a detached wave'}
 ],
 'math_notes':[
  {'type':'summary, not proof check','text':'Defines disjoint figures by compatibility and empty intersection, reduces disjointness to strata, and expresses the stratum relation as compatibility plus absence of a common lower bound. The NB discusses absence of a common refinement. A prospective spaciousness axiom and corollary, together with the marginal definition/example, are cancelled.'},
  {'type':'targeted proof check','statement_id':'R2-008-M1','text':'The displayed all-strata disjointness criterion follows from the prior bounded-sup/strata axioms and At3. Forward: compatibility descends to strata, and any common lower stratum of X≤F and Y≤G would lie below F∩G, contradicting emptiness. Reverse: pairwise stratum compatibility gives F compatible G by At3. If F∩G were nonempty, At2 would supply a stratum Z below both; taking X=Y=Z contradicts the assumed disjointness of every pair. The proof uses that strata are nonempty strictly irreducible figures and the empty figure is bottom. It does not establish any new spaciousness axiom.'},
  {'type':'targeted local check','statement_id':'R2-008-M2','text':'Using the already-read AtM0, ≤ implies ≪, absence of a common refinement implies absence of a common lower stratum: W≤X,Y would give W≪X,Y. This checks only the non-minoration component of the NB reciprocal. It does not establish X compatible Y, so it does not prove the full disjointness conclusion without an additional hypothesis.'},
  {'type':'conditional targeted proof check','statement_id':'R2-008-M3','text':'For the NB forward direction, under the minimal/minimum interpretation of the revised AtM4(a) on scan007: from Z≪X and Z≪Y choose minimal A≤X and B≤Y among the respective strata refined by Z. Their minimality makes Z an internal refinement of A and B. If X and Y are compatible, heredity gives A compatible B; the already-read AtM4(b) yields A=B, a common lower stratum. Thus compatible strata without a common lower bound have no common refinement, under that stated existence/minimality reading. This is conditional because R2’s scan007 inserted adjective remained minimal|minimum|privilégié; it does not settle that earlier ink or certify a formulation based only on an arbitrary distinguished member.'},
  {'type':'literal notation issue retained','text':'In the Cor Sup index the first replacement is plain F while the second is G-tilde. If figures and their deployments are kept formally distinct, the first decoration is missing. The writing may rely on an identification or may be a slip; no tilde is supplied and the cancelled corollary is not used as a proved result.'},
  {'type':'limits','text':'No independent proof of the cancelled At DC1, its claimed et alors seulement converse, or the cancelled Cor was attempted. No S row applies directly to scan008. No external mathematics or later manuscript page was consulted.'}
 ],
 'author_qualifications':[
  'Les axiomes sont ``facultatifs\'\' pour un atelier',
  "il y aura pas mal des' implications mutuelles avec les axiomes sur les lieux",
  'et [deleted la] réciproque résultera d’axiome|d’axiomes ci-dessous…',
  '[cancelled] Un atelier sera dit spacieux s’il satisfait cette condition.',
  '[cancelled] Contre-ex. : les ateliers simpliciaux…',
  '[cancelled] [NB et alors seulement… cf Cor]'
 ],
 'author_explicit_verification_requests':[],
 'unresolved':[
  {'place':'en termes ending','reading':r'\unsure{termes|terme}','confidence':'medium'},
  {'place':'first NB verb earlier suffix','reading':r'résul\deleted{\unsure{tera}}\inserted{te}','confidence':'low','limit':'Earlier résultera is plausible only; no duplicate full-word deletion is claimed.'},
  {'place':'NB final right-edge ending','reading':r"\unsure{d'axiome|d'axiomes}",'confidence':'low'},
  {'place':'old conjunction before K','reading':r'\deleted{\unsure{et}}','confidence':'low'},
  {'place':'old word before Supposons','reading':r'\deleted{\unsure{Il}}','confidence':'low'},
  {'place':'Cor second old index','reading':r'\deleted{\unsure{\widetilde Y|Y}}','confidence':'low','limit':'One wave is visible above the correction, but its old-layer attribution is unknown.'},
  {'place':'Cor old second quantified variable','reading':r'\deleted{\unsure{\varphi|y}}','confidence':'low'}
 ],
 'differences':rows,'C_doubt_audit':audits,
 'new_omissions_from_both':[
  {'place':'first NB verb','reading':'overwrite restricted to t/ending; shared résul- remains outside the deletion','confidence':'medium'},
  {'place':'avoir l’air de and précédents','reading':'curved insertion-guide strokes drawn explicitly','confidence':'high'},
  {'place':'left margin','reading':'global cancellation state applied to the note rather than left live','confidence':'medium'},
  {'place':'Cor first new index','reading':'plain F selected; do not supply a tilde from the expected formula','confidence':'medium'}
 ],
 'parent_requested_checks':[
  {'place':'first NB verb','reading':'current résulte; initial résul- shared; old tera only conjectural','evidence':'Overlapping bars and loops confined to the t/ending region.','crop':cm['NB']['file']},
  {'place':'précédents guide','reading':'insertion curve, not underline','evidence':'Starts at the baseline gap axiomes/que and turns under the interlinear word.','crop':cm['NB']['file']}
 ],
 'crop_manifest':manifest,
 'check_events':[
  {'statement_id':'R2-008-M1','date':end,'who':model,'type':'targeted proof check','outcome':'All-strata disjointness equivalence verified from At2/At3, hereditary compatibility and bottom/nonempty-stratum properties; no spaciousness result used.'},
  {'statement_id':'R2-008-M2','date':end,'who':model,'type':'targeted proof check','outcome':'No common refinement implies no common lower stratum using AtM0; compatibility component of disjointness expressly not proved.'},
  {'statement_id':'R2-008-M3','date':end,'who':model,'type':'targeted proof check','outcome':'NB forward implication proved conditionally on the minimal/minimum reading of scan007 AtM4(a), with hereditary compatibility and AtM4(b) uniqueness. Earlier adjective uncertainty limits certification.'}
 ]
}
(root/'scan008.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

md=['# R2 — scan 008 / manuscript page 7','',f"Independent reading: {report['start_utc']} – {end}.",
    '',f"**{len(rows)} difference/audit rows; {sum(r['diff_C'] for r in rows)} differences from C; {sum(r['diff_H'] for r in rows)} from H. All {len(audits)} C doubt occurrences audited. Thirteen crops.**",'',
    '## Principal readings','',
    '- Literal **des\'**, **dfn**, plain lowered **F**, **disjoints**, **d’ailleurs**, and **donc**.',
    '- Both interlinear additions have curved insertion guides. In particular the curve below **précédents** is not a lexical underline.',
    '- The first NB verb is corrected **within the t/ending region**. The shared **résul-** is not a separately cancelled full word. Current **résulte** is preferred; old **tera** remains conjectural.',
    '- The cancelled NB clause reads **i.e. c’est un ∃**, followed on the next line by a locally cancelled **la** before **réciproque**.',
    '- The full lower At DC1/Cor block is cancelled by three long diagonals. The left-margin note is crossed by one of those same strokes and is marked cancelled too.',
    '- The rotated margin reads **Un atelier sera dit spacieux s’il satisfait cette condition. Contre-ex. : les ateliers simpliciaux…**.',
    '- In At DC1, **soit** is added, **K** is baseline, **pour X′,Y′∈M** is interlinear, and no **tous** is written. The earlier **∀** is locally cancelled.',
    '- The Cor first index is **F** overwritten on **X**, with no separately detached tilde; the second correction has a visible wave above G/Y. The first apparent high curve belongs to **Sup**.',
    '- The oval contains literal **ses**, not ssi. The final quantified replacement is **Y**, over an unresolved older **φ|y**. No final comma after M or full stop after the final implication is supplied.',
    '', '## Remaining uncertainties','']
for u in report['unresolved']:
    md.append(f"- {u['place']}: `{u['reading']}` ({u['confidence']})."+((' '+u['limit']) if 'limit' in u else ''))
md+=['','## Mathematics and limits','']
for note in report['math_notes']:
    md.append(f"**{note['type']}**"+(f" ({note['statement_id']})" if 'statement_id' in note else '')+'. '+note['text']+'\n')
md+=['## Full collation','', '| ID | Place | C | H | R2 | Evidence / confidence |','|---|---|---|---|---|---|']
def esc(s): return str(s).replace('|','\\|').replace('\n',' ')
for r in rows:
    md.append('| '+' | '.join(esc(v) for v in [r['id'],r['place'],r['C'],r['H'],r['reading'],r['evidence']+' ['+r['confidence']+']'+(' Crop: '+r['crop'] if r['crop'] else ' From supplied half.')])+' |')
md+=['','## C doubt audit','', '| C reading | Place | Outcome | R2 row |','|---|---|---|---|']
for a in audits:
    md.append('| '+' | '.join(esc(v) for v in [a['C_reading'],a['place'],a['status'],a['difference_id']])+' |')
md+=['','## Inspection record','',report['workflow_note'],'', 'Complete coverage, notation, author qualifications, crop coordinates, and actual check events are recorded in `scan008.json`. No later scan has been read.']
(root/'scan008.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'rows':len(rows),'diff_C':sum(r['diff_C'] for r in rows),'diff_H':sum(r['diff_H'] for r in rows),'C_doubts':len(audits),'crop_count':len(manifest),'end_utc':end},ensure_ascii=False))
