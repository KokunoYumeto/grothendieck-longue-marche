from pathlib import Path
from datetime import datetime, timezone
import json
out=Path('/workspace/scratch/ae626167fbca/SP47_CW_103_work/readers/scan003/C')
reading=r'''\scanpage{3}\mspage{2}

prenant pour $A$ la ``champ'' sur $X$ formé des $F$-torseurs à droite, la (Gr)- catégorie des au\deleted{ot}to-équivalences de $A$ avec lui-même s'interprète comme la catégorie des ``b\deleted{t}itorseurs'' sous $F$, i.e. des faisceaux \inserted{\handwritten{$P$}} sur lesquels $F$ opère à la fois à droite et à gauche, ces opérations commutant et chacune d'elles faisant de $P$ un torseur (à droite ou à gauche) sous $F$, - la composition $\otimes$ étant la composition de Baer évident\deleted{\unsure{e|s}}e. Lorsque $F$ est encore de la forme $\underline{O}_{X}^{*}$ ($\underline{O}_{X}$ étant un' faisceau d'anneaux, qu'on ne suppose plus nécessairement commutatif) ces bitorseurs s'interprètent aussi en termes de bi-Modules \handwritten{``}inversibles\handwritten{''} sous $\underline{O}_{X}$.

\uline{Structure}. \deleted{\rlap{xxx}\unsure{Les|les}} Soit $C$ une (Gr)-catégorie, on lui associe

a) le groupe $\handwritten{\pi}_{0}(C)$ des classes d'isomorphisme d'objets de $C$,

b) le groupe $\handwritten{\pi}_{1}(C)$ des automorphismes de $1_C$ (objet unité de $C$)

c) une action de $\handwritten{\pi}_{0}(C)$ sur $\handwritten{\pi}_{1}(C)$, en associant à tout objet $X$ de $C$ l'automorphisme \deleted{\rlap{xxxx}de 1} $\handwritten{\rho}(X)$ de $1_C$ déduit des deux isomorphismes
\diagram{\begin{tikzcd}[ampersand replacement=\&]
\mathrm{Aut}(1_C) \handwritten{\arrow[r,shift left=.55ex]\arrow[r,shift right=.55ex]} \& \mathrm{Aut}(X)
\end{tikzcd}}
donnés par $u\handwritten{\mapsto}u\otimes\mathrm{id}_{X}$ et $u\handwritten{\mapsto}\mathrm{id}_{X}\otimes u$. On prouve que $\handwritten{\pi}_{1}(C)$ est un groupe \uline{commutatif} et que l'on obtient bien par c) une structure de $\handwritten{\pi}_{0}(C)$-module sur celui-ci. Ceci posé, si on choisit pour tout $a\handwritten{\in}\handwritten{\pi}_{0}(C)$ un représentant $L_{a}\handwritten{\in}\mathrm{Ob}\ C$ de $a$, et pour deux \deleted{\rlap{xxxxxx}objets} $a,b$ un isomorphisme
\[
\handwritten{\phi}_{a,b}: L_a\otimes L_b\handwritten{\simeq}L_{ab}\ ,
\]
alors pour trois éléments $a,b,c\handwritten{\in}\handwritten{\pi}_{0}(C)$, l'isomorphisme d'associativité
\[
(L_a\otimes L_b)\otimes L_c\handwritten{\simeq}L_a\otimes(L_b\otimes L_c)\ ,
\]
compte tenu des isomorphismes $\handwritten{\phi}_{a,b}$, $\handwritten{\phi}_{ab,c}$, $\handwritten{\phi}_{b,c}$ et $\handwritten{\phi}_{a,bc}$, peut s'interpréter comme un isomorphisme
\[
L_{abc}\handwritten{\simeq}L_{abc}\ ,
\]
ou encore comme la tensorisation \deleted{\unsure{à|a}}à gauche avec un élément bien déterminé
\[
f(a,b,c)\handwritten{\in}\handwritten{\pi}_{1}(C)\deleted{\rlap{$\mathrm{xxxxxxxxx}_{\mathrm{xxxxxx}}$}1_{C}\quad 1_{C}}\ .
\]
% No connector is recoverable between the two surviving cancelled units.
Les $\handwritten{\phi}_{a,b}$ étant choisis, on voit donc que la donnée d'un isomorphisme d'associativité fonctoriel $(L\otimes L')\otimes L''\handwritten{\simeq}L\otimes(L'\otimes L'')$ équivaut à la donnée de l'application
\[
f:\handwritten{\pi}_{0}\mathbin{\mathrm{x}}\handwritten{\pi}_{0}\mathbin{\mathrm{x}}\handwritten{\pi}_{0}\handwritten{\longrightarrow}\handwritten{\pi}_{1}\ .
\]
On vérifie alors que l'axiome \deleted{\handwritten{\unsure{(du pen}}} standard d'autocompatibilité d'une donnée d'associativité \inserted{\handwritten{(axiome du pentagone)}} s'exprime précisément par la condition que $f$ soit un \handwritten{3}-\uline{cocycle} du groupe $\handwritten{\pi}_{\deleted{1}\handwritten{0}}$ à valeurs dans le groupe $\handwritten{\pi}_{1}$. D'autre part, l'indétermination dans le choix du système d'isomorphismes $\handwritten{\phi}_{a,b}$ est précisément donnée par une 2-cochaine arbitraire, et on voit que si on change $\handwritten{\phi}$ par une 2-coc\deleted{a}h\deleted{h}aine $g$, $f$ est changé en $f+dg$ - donc l'ensemble des $f$ \deleted{p}co\deleted{s}rrespondants à des choix différents de $\handwritten{\phi}$ est exactement une classe de \handwritten{3}-cohomologie
% archive sheet number: 2
'''
(out/'reading.tex').write_text(reading,encoding='utf-8')
crops=json.loads((out/'crop_manifest.json').read_text())
crop_readings={
'c01_auto':r'au\deleted{ot}to-équivalences: round o body behind the first live t, and a tall crossbar/stem behind the live o; the transposition ot is preferable to tt.',
'c02_bitorseurs':r'b\deleted{t}itorseurs: cancelled t has a crossbar and right-curving lower foot beneath the dotted i.',
'c03_evidente':r'évident\deleted{\unsure{e|s}}e: the extra upper counter/middle bar looks most like a displaced e; s remains possible under the live e.',
'c04_un_mark':r"un' faisceau: a high separate compact apostrophe-like impression, above lowercase x-height; not a baseline period.",
'c05_structure':r'\uline{Structure}. \deleted{\rlap{xxx}\unsure{Les|les}}: underline stops before the full stop; cancelled word ends es, first tall character remains obscured.',
'c06_de1':r'\deleted{\rlap{xxxx}de 1}: d, e, a spacing position, and the flagged top/foot of 1 survive under four x impressions.',
'c07_phi':r'\phi_{a,b}: a closed small oval pierced by a single oblique stroke extending above and below; subscript has a comma between a and b.',
'c08_a_gauche':r'\deleted{\unsure{à|a}}à gauche: displaced lower-case a body and several crossing upper diagonals; the underlying accent cannot be separated from the correction.',
'c09_f_cancel':r'\deleted{1_C\quad1_C}: two flagged, footed 1s with low open C-like curves are recoverable. No intervening connector is independently legible beneath the x masks.',
'c10_pentagone':r'Cancelled \unsure{(du pen} above standard; live insertion (axiome du pentagone) attaches immediately after associativité. Thick cancellation obscures the end of the abandoned fragment.',
'c11_pi0':r'\pi_{\deleted{1}0}: old 1 has a leftward top bar and broad foot; a closed handwritten 0 crosses its stem.',
'c12_cochaine':r'2-coc\deleted{a}h\deleted{h}aine: both positions of the pair ah/ha are overstruck; the second live a has a tall h stem behind it.',
'c13_correspondants':r'\deleted{p}co\deleted{s}rrespondants: a p descender survives under first c; the first r also has the two curved parts of an s beneath it.',
'c14_O_star':r'\underline{O}_X^*: typed O, underline only beneath O, low X, and raised six-rayed typewriter star (an x-like impression with a horizontal middle stroke).'
}
for c in crops:c['reading']=crop_readings[c['id']]
changes=[]
def ch(place,c,h,reading,scan_shows,confidence,kind,against_c,against_h,crop_ids=(),marked_in_H=False):
 changes.append(dict(place=place,c=c,h=h,reading=reading,scan_shows=scan_shows,confidence=confidence,kind=kind,marked_in_H=marked_in_H,against_c=against_c,against_h=against_h,crop_ids=list(crop_ids)))
ch('Opening: quotation marks around champ',r'``champ\'\'', '« champ »',r'``champ\'\'','Half a settled this: paired upright high typewriter strokes on both sides; no chevrons.','high','misread symbol or index',False,True)
ch('Opening: space after (Gr)-', '(Gr)- catégorie','(Gr)-catégorie','(Gr)- catégorie','Half a settled this: a full typewriter blank separates the short hyphen from catégorie. The later (Gr)-catégorie after Soit has no corresponding blank.','high','other',False,True)
ch('Opening: overstruck auto-équivalences',r'au\deleted{\unsure{ot|tt}}to-équivalences','auto-équivalences',r'au\deleted{ot}to-équivalences','The third letter position contains a closed o-like round body behind the live t; the fourth contains a tall t crossbar and stem behind the live o. This supports old ot, then live to. C doubt resolved.','medium','omission',True,True,['c01_auto'])
ch('Opening: quotation marks around bitorseurs',r'``b...itorseurs\'\'','« bitorseurs »',r'``b...itorseurs\'\'','Half a and c02 show paired vertical typewriter strokes, not guillemets.','high','misread symbol or index',False,True,['c02_bitorseurs'])
ch('Opening: overstruck first i of bitorseurs',r'b\deleted{\unsure{t|l}}itorseurs','bitorseurs',r'b\deleted{t}itorseurs','A horizontal crossbar and right-curving lower foot survive below the dotted replacement i. These distinguish t from l. C doubt resolved.','high','omission',True,True,['c02_bitorseurs'])
ch('Opening: dash after sous F', '$F$, - la composition', '$F$, --- la composition', '$F$, - la composition','Half a settled this: one short typewriter hyphen occupies a single character position.','high','misread symbol or index',False,True)
ch('Opening: final e of évidente',r'évident\deleted{\unsure{s|e}}e','évidente',r'évident\deleted{\unsure{e|s}}e','Extra rounded impression extends through the upper counter and middle stroke of the live e. A displaced e is visually first; s remains possible because the live e closes part of the composite. C doubt retained with candidates reordered.','low','omission',True,True,['c03_evidente'])
ch('Opening: mark immediately after un',r"un\unsure{'|.} faisceau",'un faisceau',"un' faisceau",'The separate impression is high, slightly triangular/oblique, and lies above lowercase x-height. It is not at the full-stop baseline. C doubt resolved as an apostrophe-like stray impression; its lexical purpose is not inferred.','medium','omission',True,True,['c04_un_mark'])
ch('Opening: handwritten quotation marks around inversibles',r'\handwritten{``}inversibles\handwritten{\'\'}',r'\add{«} inversibles \add{»}',r'\handwritten{``}inversibles\handwritten{\'\'}','Half a settled this: two slanted pen strokes at each end of inversibles, rather than paired chevrons. H marks additions but gives a different quotation shape.','high','misread symbol or index',False,True,marked_in_H=True)
ch('Structure heading: endpoint of underline',r'\uline{Structure}.',r'\emph{Structure.}',r'\uline{Structure}.','The line ends immediately after the final e, before the full stop; the stop is not above the underline. This is an underline-span difference, not an emph/uline macro difference.','high','other',False,True,['c05_structure'],True)
ch('Structure heading: cancelled opening word',r'\deleted{\rlap{xxx}\unsure{Les|les}}','omitted',r'\deleted{\rlap{xxx}\unsure{Les|les}}','Three typewriter x impressions cover a three-letter group; the ending es survives, while the first tall glyph could be L or l. C doubt retained exactly.','low','omission',False,True,['c05_structure'])
ch('c): cancelled de 1 before rho(X)',r'\deleted{\rlap{xxxx}\unsure{de 1}}','omitted',r'\deleted{\rlap{xxxx}de 1}','Under the cancellation, d has a tall right stem and low round body; e has its midbar; final 1 has its top flag and broad foot. C doubt resolved.','high','omission',True,True,['c06_de1'])
ch('Choice of representatives: cancelled objets',r'\deleted{\rlap{xxxxxx}objets}','omitted',r'\deleted{\rlap{xxxxxx}objets}','Half a, also visible at top of half b, settled this: six struck typewriter letters read objets between deux and a,b.','high','omission',False,True)
phi_loci=[
 ('First isomorphism display',r'\phi_{a,b}',r'\varphi_{a,b}',['c07_phi'],'The enhanced crop shows a small closed oval pierced by one oblique continuous stroke, extending above and below.'),
 ('compte tenu: first indexed phi',r'\phi_{a,b}',r'\varphi_{a,b}',[],'Half b settled this: the handwritten symbol is a small closed oval with an oblique through-stroke; low a,b are separated by a comma.'),
 ('compte tenu: second indexed phi',r'\phi_{ab,c}',r'\varphi_{ab,c}',[],'Half b settled this: the same pierced-oval phi precedes low ab,c; comma is between ab and c.'),
 ('compte tenu: third indexed phi',r'\phi_{b,c}',r'\varphi_{b,c}',[],'Half b settled this: the same pierced-oval phi precedes low b,c.'),
 ('compte tenu: fourth indexed phi',r'\phi_{a,bc}',r'\varphi_{a,bc}',[],'Half b settled this: the same pierced-oval phi precedes low a,bc, with no comma between b and c.'),
 ('Les phi étant choisis',r'\phi_{a,b}',r'\varphi_{a,b}',[],'Half b settled this: closed oval pierced by a slanting stroke, followed by a,b below the line.'),
 ('Final paragraph: système d’isomorphismes',r'\phi_{a,b}',r'\varphi_{a,b}',[],'Half b settled this: closed pierced oval, with low a,b.'),
 ('Final paragraph: si on change phi',r'\phi',r'\varphi',['c12_cochaine'],'Half b and c12 show a closed oval pierced by one long oblique stroke.'),
 ('Final paragraph: choix différents de phi',r'\phi',r'\varphi',[],'Half b settled this: a small closed pierced oval, matching the previous phi signs.')]
for place,c,h,cids,evidence in phi_loci:
 ch(place,c,h,c,evidence,'high','misread symbol or index',False,True,cids)
ch('tensorisation à gauche: overwritten à',r'\deleted{\unsure{à|a}}à','à',r'\deleted{\unsure{à|a}}à','Two displaced a-like bodies and crossing upper diagonals form the composite. One cannot assign the surviving upper diagonal uniquely to an original grave accent rather than correction strokes. The live à is clear. C doubt retained exactly.','low','omission',False,True,['c08_a_gauche'])
ch('f(a,b,c) display: cancelled tail after pi_1(C)',r'\deleted{\rlap{$\mathrm{xxxxxxxxx}_{\mathrm{xxxxxx}}$}\unsure{1_C\quad1_C}}','omitted',r'\deleted{\rlap{$\mathrm{xxxxxxxxx}_{\mathrm{xxxxxx}}$}1_C\quad1_C}','Two typewriter 1s retain top-left flags, stems and feet above two low C-like open curves. The x masks cover other positions, with no readable connector surviving. C doubt over the two units is resolved; unrecoverable intervening material is explicitly not supplied.','medium','omission',True,True,['c09_f_cancel'])
ch('Display defining f: two product separators',r'\pi_0\mathbin{\mathrm{x}}\pi_0\mathbin{\mathrm{x}}\pi_0',r'\pi_0\times\pi_0\times\pi_0',r'\pi_0\mathbin{\mathrm{x}}\pi_0\mathbin{\mathrm{x}}\pi_0','Half b settled this: both separators are baseline lowercase typewriter x characters, with their small serifed arms. The arrow after the third factor is a separate plain right arrow.','high','misread symbol or index',False,True)
ch('Above standard: cancelled handwritten fragment',r'\deleted{\handwritten{\unsure{(du pen}}}','omitted',r'\deleted{\handwritten{\unsure{(du pen}}}','Opening left curve, a tall d, adjoining u-like stroke, and descending p survive; later small connected humps are heavily crossed. (du pen remains a tentative partial reading, with no recovered closing parenthesis. C doubt retained exactly.','low','omission',False,True,['c10_pentagone'])
ch('Final paragraph: span of cocycle underline',r'\handwritten{3}-\uline{cocycle}',r'\emph{3-cocycle}',r'\handwritten{3}-\uline{cocycle}','Half b settled this: the pen line starts under the c of cocycle and ends under its last letters; it does not extend under 3-. H emph is accepted as underline syntax, but its span differs.','high','other',False,True,marked_in_H=True)
ch('Final paragraph: corrected group subscript',r'\handwritten{\pi}_{\deleted{1}0}',r'\pi_0',r'\handwritten{\pi}_{\deleted{1}\handwritten{0}}','Old 1 has a horizontal upper flag, a central vertical stem, and a broad foot; a closed oval 0 has been drawn over the stem. This is a correction 1 to 0, not an uncorrected single 0.','high','omission',False,True,['c11_pi0'])
ch('Second cochaine: old a beneath live h',r'2-coc\deleted{\unsure{a}}haine','2-cochaine',r'2-coc\deleted{a}h\deleted{h}aine','At the first position after coc, the tall stem of the live h crosses a rounded a body with a visible inner horizontal stroke. C doubt over old a resolved.','high','omission',True,True,['c12_cochaine'])
ch('Second cochaine: old h beneath live a',r'2-coc\deleted{\unsure{a}}haine','2-cochaine',r'2-coc\deleted{a}h\deleted{h}aine','At the next position, a tall h stem and upper serif protrude above the live a. Both positions of the pair ah have therefore been corrected to ha; C represents only the first overwritten letter.','high','omission',True,True,['c12_cochaine'])
ch('Final paragraph: dash after f+dg',r'$f+dg$ - donc',r'$f+dg$ --- donc',r'$f+dg$ - donc','Half b settled this: a single short typewriter hyphen separates f+dg and donc.','high','misread symbol or index',False,True)
ch('correspondants: old p beneath first c',r'\deleted{\unsure{p}}correspondants','correspondants',r'\deleted{p}co\deleted{s}rrespondants','The first letter retains a long p descender and its foot below the c-shaped replacement; the overstruck p is readable. C doubt resolved.','high','omission',True,True,['c13_correspondants'])
ch('correspondants: old s beneath first r',r'\deleted{\unsure{p}}correspondants','correspondants',r'\deleted{p}co\deleted{s}rrespondants','The third character has an extra s-like upper curve and lower bowl behind the first live r; the following r is single. This second overstrike is absent from both witnesses.','medium','omission',True,True,['c13_correspondants'])
unresolved=[
 {'place':'Final e of évidente','reading':r'\deleted{\unsure{e|s}}e','alternatives':['e beneath live e','s beneath live e'],'confidence':'low','evidence':'c03: double rounded upper counter and a middle stroke; the live e prevents unique recovery of the other character. Candidate order is based on shape, not grammatical expectation.'},
 {'place':'Cancelled word after Structure.','reading':r'\deleted{\unsure{Les|les}}','alternatives':['Les','les'],'confidence':'low','evidence':'c05: es is readable; the first tall outline is crossed too heavily to distinguish capital L from lower-case l.'},
 {'place':'Underlying a in tensorisation à gauche','reading':r'\deleted{\unsure{à|a}}à','alternatives':['à','a'],'confidence':'low','evidence':'c08: the original a body survives, but crossed upper strokes do not identify a separate original accent.'},
 {'place':'Cancelled fragment above standard','reading':r'\deleted{\handwritten{\unsure{(du pen}}}','alternatives':['(du pen (partial reading)','(du pe… (end not recoverable)'],'confidence':'low','evidence':'c10: surviving left curve, d/u and descender of p; heavy cancellation of the later connected strokes.'},
 {'place':'Additional undertext in cancelled tail of f(a,b,c) display','reading':r'1_C\quad1_C with no supplied connector','alternatives':['No connector independently recoverable','Additional cancelled connector or text may have occupied the x-covered spaces'],'confidence':'low','evidence':'c09 resolves the two 1_C groups, but there are x-covered positions before/between them; no separate connector strokes can be isolated. No mathematically expected arrow is supplied.'}
]
inventory=[]
def inv(element,kind,position,first,hand='typewriter'):
 inventory.append({'sheet_kind':'typescript','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':True})
inv('Author page number','text','upper centre','2','unnamed hand')
inv('Continuation of bitorseur example','text','upper block','prenant pour A la "champ"', 'typewriter with handwritten additions')
inv('Overwritten ot','deletion','upper block, auto-équivalences','ot under to')
inv('Overwritten t','deletion','upper block, first bitorseurs','t under i')
inv('Inserted sheaf name','insertion','after faisceaux','P','unnamed hand')
inv('Overwritten final character of évidente','deletion','end of Baer sentence','e or s under e')
inv('Stray high impression','text','after étant un',"'",'typewriter or other impression; source not identifiable')
inv('Opening quotation strokes','insertion','before inversibles','two high strokes','unnamed hand')
inv('Closing quotation strokes','insertion','after inversibles','two high strokes','unnamed hand')
inv('Structure heading and introduction','text','below opening block','Structure. … Soit C une (Gr)-catégorie')
inv('Heading underline','insertion','under Structure, excluding full stop','one horizontal underline','unnamed hand')
inv('Cancelled opening of heading sentence','deletion','after Structure.','Les or les, covered by xxx')
inv('Item a','text','below heading','a) le groupe pi_0(C)')
inv('pi in item a','insertion','a), group name','pi','unnamed hand')
inv('Item b','text','below a)','b) le groupe pi_1(C)')
inv('pi in item b','insertion','b), group name','pi','unnamed hand')
inv('Item c','text','below b)','c) une action de pi_0(C) sur pi_1(C)')
inv('First pi in item c','insertion','c), first group name','pi','unnamed hand')
inv('Second pi in item c','insertion','c), second group name','pi','unnamed hand')
inv('Cancelled de 1','deletion','after l’automorphisme','de 1 covered by xxxx')
inv('rho in rho(X)','insertion','c), before (X)','rho','unnamed hand')
inv('Parallel isomorphism arrows','diagram','centred below c)','Aut(1_C) with two rightward arrows to Aut(X)','typewriter endpoints; unnamed hand arrows')
inv('Two diagram arrows','insertion','between Aut(1_C) and Aut(X)','two parallel right shafts and heads','unnamed hand')
inv('Mappings and commutative module statement','text','below diagram','donnés par u … On prouve que')
inv('First barred map arrow','insertion','first u mapping','mapsto','unnamed hand')
inv('Second barred map arrow','insertion','second u mapping','mapsto','unnamed hand')
inv('pi in commutativity statement','insertion','On prouve que pi_1(C)','pi','unnamed hand')
inv('Underline of commutatif','insertion','under commutatif','one horizontal underline','unnamed hand')
inv('pi in module statement','insertion','structure de pi_0(C)-module','pi','unnamed hand')
inv('Choice of representatives','text','after Ceci posé','si on choisit pour tout a …')
inv('Membership and pi after a','insertion','pour tout a in pi_0(C)','in and pi','unnamed hand')
inv('Membership after L_a','insertion','L_a in Ob C','in','unnamed hand')
inv('Cancelled objets','deletion','et pour deux … a,b','objets covered by xxxxxx')
inv('First isomorphism formula','display','below choice sentence','phi_{a,b}: L_a tensor L_b simeq L_ab,')
inv('First phi sign','insertion','start of first isomorphism display','phi','unnamed hand')
inv('First isomorphism sign','insertion','first isomorphism display','simeq','unnamed hand')
inv('Three-elements introduction','text','below first display','alors pour trois éléments a,b,c …')
inv('Membership and pi after a,b,c','insertion','three-elements sentence','in and pi','unnamed hand')
inv('Associativity formula','display','centred below three-elements sentence','(L_a tensor L_b) tensor L_c simeq L_a tensor (L_b tensor L_c),')
inv('Associativity isomorphism sign','insertion','middle of associativity display','simeq','unnamed hand')
inv('Use of four chosen isomorphisms','text','below associativity display','compte tenu des isomorphismes …')
for label in ['a,b','ab,c','b,c','a,bc']:
 inv('Handwritten phi '+label,'insertion','compte tenu des isomorphismes','phi_'+label,'unnamed hand')
inv('Automorphism of L_abc','display','below isomorphisms sentence','L_abc simeq L_abc,')
inv('L_abc isomorphism sign','insertion','middle of L_abc display','simeq','unnamed hand')
inv('Left tensorisation description','text','below L_abc display','ou encore comme la tensorisation à gauche …')
inv('Overwritten a/à','deletion','tensorisation à gauche','à or a under à')
inv('Cochain value formula','display','below tensorisation text','f(a,b,c) in pi_1(C) [cancelled units].')
inv('Membership and pi in cochain value','insertion','f(a,b,c) display','in and pi','unnamed hand')
inv('Cancelled end of cochain value formula','deletion','after pi_1(C)','1_C … 1_C under upper/lower x masks')
inv('Functorial associativity and application paragraph','text','below cochain value','Les phi_{a,b} étant choisis …')
inv('phi after Les','insertion','Les … étant choisis','phi','unnamed hand')
inv('Inline associativity isomorphism sign','insertion','after fonctoriel','simeq','unnamed hand')
inv('Definition of f','display','centred below de l’application','f: pi_0 x pi_0 x pi_0 -> pi_1.')
for i in range(1,4):inv('Domain pi '+str(i),'insertion','definition of f, factor '+str(i),'pi','unnamed hand')
inv('Function arrow','insertion','definition of f, before codomain','plain right arrow','unnamed hand')
inv('Codomain pi','insertion','definition of f','pi_1','unnamed hand')
inv('Cocycle and change-of-choice paragraph','text','last block','On vérifie alors que l’axiome standard …')
inv('Cancelled handwritten axiom fragment','deletion','above standard','(du pen (tentative partial reading)','unnamed hand')
inv('Pentagon parenthesis','insertion','after d’associativité, before s’exprime','(axiome du pentagone), with attachment line','unnamed hand')
inv('Cocycle degree','insertion','before -cocycle','3','unnamed hand')
inv('Cocycle underline','insertion','under cocycle only','one horizontal underline','unnamed hand')
inv('pi of group acting','insertion','du groupe pi_0','pi','unnamed hand')
inv('Old group subscript','deletion','pi after du groupe','1')
inv('New group subscript','insertion','pi after du groupe','0 over old 1','unnamed hand')
inv('pi of value group','insertion','à valeurs dans le groupe pi_1','pi','unnamed hand')
inv('phi of chosen system','insertion','système d’isomorphismes','phi_{a,b}','unnamed hand')
inv('phi being changed','insertion','si on change phi','phi','unnamed hand')
inv('Old a in second cochaine','deletion','first corrected letter after 2-coc','a under h')
inv('Old h in second cochaine','deletion','next corrected letter in second cochaine','h under a')
inv('Old p in correspondants','deletion','first letter of correspondants','p under c')
inv('Old s in correspondants','deletion','third letter of correspondants','s under first r')
inv('Final phi sign','insertion','choix différents de phi','phi','unnamed hand')
inv('Final cohomology degree','insertion','before -cohomologie','3','unnamed hand')
inv('Archive sheet number','text','lower left margin','2 (recorded only as a comment)','unnamed pencil hand')
notation=[
 {'place':'Items a–c and subsequent group names','sign':'pi_0, pi_1; rho','ink':'Connected two-legged pi, distinct from rho with a loop and long descending left stroke; 0 and 1 are subscripts. All occurrences were compared.','latex':r'\pi_0,\ \pi_1,\ \rho(X)'},
 {'place':'First isomorphism and eight subsequent occurrences','sign':'phi','ink':'Closed small oval pierced by a single oblique stroke, not the open-top variant; all nine occurrences checked.','latex':r'\phi_{a,b},\ \phi_{ab,c},\ \phi_{b,c},\ \phi_{a,bc},\ \phi'},
 {'place':'Diagram after c)','sign':'two parallel arrows','ink':'Two separate horizontal shafts with heads at the right; no labels or reverse arrow. Half a settled the C alert. H’s rightrightarrows has the same directional content.','latex':r'\diagram{\begin{tikzcd}[ampersand replacement=\&]\mathrm{Aut}(1_C)\arrow[r,shift left=.55ex]\arrow[r,shift right=.55ex]\&\mathrm{Aut}(X)\end{tikzcd}}'},
 {'place':'Two u formulas','sign':'maps-to','ink':'Both have a short vertical start bar, shaft, and right arrowhead.','latex':r'u\mapsto u\otimes\mathrm{id}_X;\quad u\mapsto\mathrm{id}_X\otimes u'},
 {'place':'All displayed/inline associativity isomorphisms','sign':'simeq','ink':'Hand wavy upper stroke and lower straight stroke; all four relation occurrences checked, including inline L-prime formula.','latex':r'\simeq'},
 {'place':'Opening composition and every tensor expression','sign':'tensor','ink':'Typewriter round O-like outline with crossed interior, unlike the bare product x in the f display.','latex':r'\otimes'},
 {'place':'Units, identities and object notation','sign':'1_C; id_X; Aut; Ob','ink':'Unit numeral 1 with low C; upright baseline id, Aut, Ob; X below id. No blackboard-bold or bold alphabet is present.','latex':r'1_C;\ \mathrm{id}_X;\ \mathrm{Aut};\ \mathrm{Ob}'},
 {'place':'Opening sheaf expressions','sign':'underlined O and raised star','ink':'Three single typewriter O outlines, single underline beneath O only, low X. First has a raised six-rayed typewriter star; c14 checked its strokes.','latex':r'\underline{O}_X^*;\ \underline{O}_X'},
 {'place':'Definition of f','sign':'two typed x separators and plain arrow','ink':'Both separators have typewriter x outlines on the baseline. The following pen arrow has no start bar.','latex':r'\pi_0\mathbin{\mathrm{x}}\pi_0\mathbin{\mathrm{x}}\pi_0\longrightarrow\pi_1'},
 {'place':'Associativity formulas','sign':'L indices and primes','ink':'L_a, L_b, L_c; concatenated ab and abc; inline one high stroke after L′ and two after L″. All tensor factors and parentheses compared against both witnesses.','latex':r'L_a,L_b,L_c,L_{ab},L_{abc},L\prime,L\prime\prime'},
 {'place':'Headings and emphasis','sign':'single underlines','ink':'Structure only (stop outside), commutatif, cocycle only (3- outside).','latex':r'\uline{Structure}.;\ \uline{commutatif};\ 3-\uline{cocycle}'},
 {'place':'Quoted words in opening paragraph','sign':'double quotation strokes','ink':'Paired high typed strokes around champ/bitorseurs; paired slanted hand strokes around inversibles; no guillemets.','latex':"``...''"},
 {'place':'Last paragraph','sign':'3 and corrected 0','ink':'Cocycle and cohomology 3 each have two handwritten lobes. Corrected group index has a looped 0 laid over a footed 1.','latex':r'\handwritten{3};\ \pi_{\deleted{1}\handwritten{0}}'},
 {'place':'Cancelled typescript passages','sign':'x cancellation','ink':'Typed x masks cover Les/les, de 1, objets, and the tail after pi_1(C); letter-over-letter corrections are separately preserved.','latex':r'\deleted{\rlap{xxx}...};\ \deleted{...}'},
 {'place':'Opening un','sign':'stray high impression','ink':'A high compact oblique mark immediately follows un; it is transcribed as an apostrophe without giving it a grammatical role.','latex':"un'"}
]
notes=[
 'Coverage: I opened only the assigned whole image once for layout and the supplied upper and lower halves once each in order. Every text block, every word/ending and punctuation mark, and every inline/display formula was compared against both C and H; agreed expressions were inspected too. After the halves I made one enhanced tight crop for each remaining location, with no second crop of a settled location. The 14 crops are logged with exact source boxes and processing.',
 'The sheet is a typescript with handwritten mathematical symbols, underlining, quotations, an inserted P, a cancelled handwritten fragment, and a live pentagon parenthesis. No source attribution for the handwritten contributor was supplied in this packet; inventory uses unnamed hand conservatively. There is one diagram (two arrows between Aut groups), no independent marginal drawing, no letterhead, and no date.',
 'The page number at top is 2. The separate lower-left pencil number is also 2 and is recorded only as the archive sheet-number comment. The page begins as a continuation (prenant pour A) and ends after classe de 3-cohomologie without a full stop. No total page count is written.',
 'The opening says la "champ" followed by formé. This grammatical combination is visibly present and is not repaired. bi-Modules has a capital M. Both cochaine occurrences lack a circumflex. fonctoriel visibly ends -iel. These are agreed witness readings, so they are not listed as changes.',
 'The opening discusses F-bitorsors, their left/right commuting actions and Baer composition, then the case of a ring sheaf and invertible bimodules. These are statements on the page, not independently verified mathematical claims.',
 'Structure defines pi_0(C), pi_1(C), and an action using the pair of maps from Aut(1_C) to Aut(X). The wording gives rho(X) as an automorphism de 1_C; it is transcribed without mathematical repair. The page says On prouve concerning commutativity and the module structure, but supplies no proof here.',
 'The page next chooses L_a and phi_{a,b}, associates f(a,b,c) with associativity, identifies the pentagon with a 3-cocycle condition, and describes changes by a 2-cochaine g as f+dg. Its On vérifie is a source assertion. I did not perform a proof, independent re-proof, cohomology calculation, or formal certificate; math_checks is empty.',
 'The c12 and c13 crops disclosed corrections that the C witness does not fully preserve: both letters ah were overstruck to ha in the second cochaine, and correspondants has an s beneath its first r in addition to the p beneath its first c. These are visual conclusions, not spelling corrections imposed from grammar.',
 'C doubts decided: ot, t, apostrophe after un, de 1, the two 1_C groups, a under h in the second cochaine, and p under first c are resolved from crops. The final évidente underletter is retained doubtful with e visually ahead of s. Les/les, underlying à/a, and cancelled (du pen remain doubtful. The cancelled f tail has no recoverable connector, and no arrow or other expected symbol is reconstructed.',
 'For H comparisons, emph/add and similar notation are compared by meaning, not macro name. The ordinary diagram content agrees with the two arrows and therefore has no spurious diagram-change row. Actual differences in quotation shape, underlining span, phi glyph, typewriter x, short hyphens, and omitted deletions are recorded separately. All differences settled already by a half are labelled as such in scan_shows so the main reader can make its own required adjudication crop.',
 'The report reproduces visible x-cancellation masks typographically with rlap and deletion markup. Their disposition is approximate, while the surviving undertext and its uncertainty are explicit. In the f(a,b,c) tail, the two surviving units are resolved but x-covered intervening positions remain unassignable; the blank spacing in the reading is not a claim that no intervening source mark once existed.'
]
report={
'scan':3,'reader':'C','start_utc':'2026-11-20T09:15:01.969117+00:00','end_utc':datetime.now(timezone.utc).isoformat(),'model':'GPT-6 Astra Pro','effort':'not exposed',
'viewed':[
 {'path':'/workspace/scratch/ae626167fbca/source/SP47_CW_103_scans/H103-01_103_scan003.jpg','role':'whole','count':1,'when':'between 2026-11-20T09:15:01.969117Z and 2026-11-20T09:15:10Z','note':'Opened first, exactly once, for layout. Exact separate clock sample was not taken for this call.'},
 {'path':'/workspace/scratch/ae626167fbca/source/SP47_CW_103_scans/H103-01_103_scan003_a.jpg','role':'half_a','count':1,'when':'2026-11-20T09:15:10Z','note':'Clock sampled immediately before opening; read against both witnesses, exactly once.'},
 {'path':'/workspace/scratch/ae626167fbca/source/SP47_CW_103_scans/H103-01_103_scan003_b.jpg','role':'half_b','count':1,'when':'2026-11-20T09:15:39Z','note':'Clock sampled immediately before opening; read after half_a against both witnesses, exactly once.'}],
'crops':crops,'changes':changes,'unresolved':unresolved,'inventory':inventory,'notation':notation,
'abbreviations':[{'form':'i.e.','expansion':'id est (not expanded in the reading)'},{'form':'Aut','expansion':'automorphismes'},{'form':'id','expansion':'identité'},{'form':'Ob','expansion':'objets'},{'form':'(Gr)','expansion':'not expanded on this page'}],
'notes':notes,'math_checks':[]}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'reading':str(out/'reading.tex'),'report':str(out/'report.json'),'changes':len(changes),'against_c':sum(x['against_c'] for x in changes),'against_h':sum(x['against_h'] for x in changes),'crops':len(crops),'inventory':len(inventory),'unresolved':len(unresolved)},indent=2))
