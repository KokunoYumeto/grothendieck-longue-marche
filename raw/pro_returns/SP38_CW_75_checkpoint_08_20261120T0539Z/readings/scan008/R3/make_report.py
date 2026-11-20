import json
from pathlib import Path
from datetime import datetime,timezone
root=Path('out/readings/scan008/R3')
log=json.loads((root/'crop_log.json').read_text())
for x in log:x['viewed']=True
(root/'crop_log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
cm={x['id'].split('_',1)[0]:x for x in log}
F=[]
def add(id,place,c,h,final,evidence,confidence='high',kind='other',marked=False,dc=False,dh=False,box=None,cr='',doubt='',math=''):
    if cr:
        item=cm[cr];box=box or item['bbox'];crop='readings/scan008/R3/crops/'+Path(item['file']).name
    else:crop=''
    assert box and len(box)==4
    F.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,confidence=confidence,kind=kind,marked_in_H=marked,diff_c=dc,diff_h=dh,bbox=box,crop=crop,doubt_action=doubt,s_id='',math_note=math))
# Every original C uncertainty has an explicit disposition.
add('D01','Opening, after pour',r'\unsure{tte|les|toute}','toute',r'\unsure{tte|toute}','Two tall strokes with a compressed intermediate loop; tte remains first. The second tall stroke rules against les; a compressed toute remains possible.','medium','abbreviation expanded or spelling modernised',dc=True,dh=True,cr='01',doubt='retain')
add('D02','Overwriting immediately before (a) in origine',r'\deleted{\unsure{o|\omega}}\sigma(a)',r'\sigma(a)',r'\deleted{\unsure{\omega|o}}\sigma(a)','The final sigma has its broad upper exit; under it are two adjacent low loops, favouring omega over o without recovering the overwritten form securely.','low','deletion state (struck given live or live given struck)',dc=True,dh=True,cr='02',doubt='retain')
add('D03','First canceled sign in slanted marginal formula',r'\deleted{\unsure{\exists1|\exists}}','No transcription of this canceled sign; note says some crossed words are illegible',r'\deleted{\unsure{\exists1|\exists}}','Rotation separates the existential-like left strokes and a possible following upright. The cancellation prevents a decision about the 1.','low','readable ink left as \\ill{}',marked=True,dh=True,cr='03',doubt='retain')
add('D04','Second, wholly canceled row of slanted note',r'\deleted{\unsure{\forall s\in S|\forall a\in S},\exists1\,a\in A,}','No transcription; note says some crossed words are illegible',r'\deleted{\unsure{\forall s\in S|\forall a\in S},\exists1\,a\in A,}','The universal sign, membership, S, existential with following upright, a in A, and final comma survive the rule. The first small variable remains crossed and ambiguous.','low','readable ink left as \\ill{}',marked=True,dh=True,cr='03',doubt='retain')
add('D05','Condition label',r'(\unsure{O|0})','(O)',r'(\unsure{O|0})','Open round loop inside parentheses; shape alone does not distinguish the letter and the numeral.','medium',cr='04',doubt='retain')
add('D06','First proposition, orientations',r'(\unsure{\omega|w}\text{ et }-\omega)',r'(\omega\text{ et }-\omega)',r'(\omega\text{ et }-\omega)','The first full-size glyph has the two rounded lower lobes and inward curled endings of omega. The half settles it.','high','misread symbol or index',dc=True,box=[1168,538,1388,593],doubt='resolve')
add('D07','First canceled expression before live u_omega(s)',r'\deleted{\unsure{\omega(s)|w(s)}}',r'\struck{\ill{}}',r'\deleted{\unsure{\omega(s)|w(s)}}','A low wave followed by a parenthesized s is visible under the long stroke; omega versus Roman w cannot be separated.','low','readable ink left as \\ill{}',marked=True,dh=True,cr='05',doubt='retain')
add('D08','Second canceled expression and replacement u_omega',r'\deleted{\unsure{u_{\omega}|u}}\inserted{u_{\omega}}',r'\struck{\ill{}}\ u_\omega',r'\deleted{\unsure{u_{\omega}|u}}\inserted{u_{\omega}}','The second dark patch retains a u-like body but does not securely expose its subscript. A distinct u with small omega is written above it as replacement.','low','insertion or placement',marked=True,dh=True,cr='05',doubt='retain')
add('D09','Cancellation between qui ait and s comme origine',r'\deleted{\unsure{comme}}',r'arête \struck{\ill{}}\ \sigma^{-1}(s)\text{ qui ait }s\text{ comme origine}',r'qui ait \deleted{\unsure{comme}} $s$ comme origine','The heavy rule lies after ait and before the live s. Its surviving low humps suggest comme, but do not disclose every letter; it is not a separate cancellation after arête.','low','insertion or placement',marked=True,dh=True,cr='06',doubt='retain')
add('D10','Edge definition, l’unique arc de S',r'\unsure{arc|ar} de S','arc de S','arc de S','Three small letter groups survive; the last is a separate shallow c. S has a large upper and lower bend, not the legs of A.','high','misread word',dc=True,cr='07',doubt='resolve',math='The visible S is retained despite the immediately preceding a in A; no emendation to A.')
add('D11','Overwritten second component in first pair after Alors',r'(S,\deleted{\unsure{R|B}}A)','(S,A)',r'(S,\deleted{\unsure{R|B}}A)','The dark correction includes a prior upright and right bowl/diagonal. R is favoured, but the lower closed stroke also permits B.','low','omission',dh=True,cr='09',doubt='retain')
add('D12','Connector between the two pairs in Alors',r'\unsure{-|\to}',r'\to',r'\unsure{-|\to}','A short horizontal shaft has a small downward end and no separately resolved upper wing. Do not supply a complete arrowhead from the map interpretation.','medium','misread symbol or index',dh=True,cr='09',doubt='retain')
add('D13','Word introducing u_omega unequal to u_minus_omega',r'\unsure{flèche|et}','Donc',r'\unsure{flèche|et}','A conspicuous looped ascender/descender followed by low connected strokes remains difficult. The crop does not support the securely written Donc supplied by H.','low','misread word',dh=True,cr='11',doubt='retain')
add('D14','After n greater than or equal to 3 and semicolon',r'\unsure{donc|alors}','donc',r'\unsure{donc|alors}','The opening low curl and tall following stroke favour d, but can also be compressed al; the remainder is nearly horizontal.','low',cr='13',doubt='retain')
add('D15','Name of orientation set',r'\unsure{\operatorname{or}|{\rm Or}}',r'\operatorname{Or}',r'\operatorname{or}','The first oval is distinctly low compared with the adjacent capital S, A and R; the following letter is a short r shoulder.','medium','misread symbol or index',dc=True,dh=True,cr='14',doubt='resolve')
add('D16','Word linking or(S,A,R) and l’ens',r'\unsure{avec|sur}','avec',r'\unsure{avec|sur}','A small oval followed by two flattened groups favours avec; the reduced middle and terminal strokes do not exclude sur.','low',cr='15',doubt='retain')
add('D17','Closing delimiter after references to conditions',r'\unsure{$1^{\circ}$ ou $2^{\circ}\big\}$|$1^{\circ}$ ou $2^{\circ})$}',r'1^{\circ},2^{\circ}\}',r'1^{\circ}\text{ [connector] }2^{\circ}\text{ [small hook] }\big\}','The tall final sign has a clear central inward notch and both outer bends: it is a right brace. The smaller separate hook is recorded independently as N22.','high','misread symbol or index',dc=True,cr='16',doubt='resolve',math='The closing brace has no matching opening brace visible on the preceding line; the reading does not add one.')
add('D18','Cyclic group abbreviation',r'\unsure{gpe|grpe}','groupe',r'\unsure{gpe|grpe}','A long g descender is followed by a flat shoulder and p/e-like ending. There are too few separately formed letters for the full word groupe; gpe versus grpe remains open.','medium','abbreviation expanded or spelling modernised',dh=True,cr='17',doubt='retain')
add('D19','Canceled word after est and interlinear replacement',r'\deleted{\unsure{formé|form}}\inserted{le}',r'le \struck{\ill{}}',r'\deleted{formé}\inserted{le}','Long f, low o/r/m remnants, and a detached acute at the right support formé. The small le stands above the canceled word, rather than as ordinary text before it.','medium','readable ink left as \\ill{}',marked=True,dc=True,dh=True,cr='19',doubt='resolve')
add('D20','Inserted G superscript',r'G^{\unsure{0|\circ}}','G^0',r'G^{\unsure{0|\circ}}','A small closed round loop does not decide zero versus circle. Its later repeated occurrence is given as the first candidate under the recurring-glyph convention.','medium',cr='20',doubt='retain')
add('D21','Interlinear gloss following the tuple',r'\inserted{\unsure{lire|les} de $S,A,R;\omega)$}',r'(i.e.\ de $(S,A,R;\omega)$)\text{ before }de\ (S,A,R,\omega)',r'\inserted{\unsure{lire|les} de $S,A,R;\omega)$}','The first group begins with a tall l-like stroke, then a flattened tail, not clearly dotted i.e. The curved connector originates after the main tuple. No opening parenthesis occurs before the added S; the final closing one is visible.','low','insertion or placement',dh=True,cr='21',doubt='retain')
add('D22','Overwriting after ensemble',r'\deleted{\unsure{où}} à','à',r'\deleted{\unsure{où}} à','A small closed left body and right low strokes under the dark correction allow où, with a detached grave stroke above; the prior form remains obscured.','low','omission',dh=True,cr='23',doubt='retain')
add('D23','Noun after à n',r'\unsure{élément|éléments}','éléments',r'\unsure{élément|éléments}','The ending visibly reaches t and a long down-curving exit. That exit gives no secure independent s, but can conceal a contracted s.','medium','misread word',dh=True,cr='24',doubt='retain')
add('D24','Raised mark after ordre, before circulaire',r'\unsure{$^{\times}$|$^{*}$}',r'« circulaire »',r'\unsure{$^{\times}$|$^{*}$} circulaire.','The raised mark has intersecting strokes, not an opening guillemet. Two crossings favour a cross, while the dense centre permits an asterisk. There is a period after circulaire and no closing guillemet.','medium','misread symbol or index',dh=True,cr='25',doubt='retain')
# Other substantive differences and new doubts.
add('N01','Opening quotation marks',r'``orientation de $a$\'\'',r'« orientation de $a$ »',r'``orientation de $a$\'\'','Both opening and closing marks are paired high ticks; they are not angular guillemets.','high','misread symbol or index',dh=True,box=[985,148,1347,217])
add('N02','Slanted map decoration',r'A\xrightarrow{\substack{\sigma\\\sim}}S',r'A\xrightarrow{\sigma}S',r'A\xrightarrow{\substack{\sigma\\\sim}}S','After rotation, sigma, a separate wave, and the arrow shaft/head occupy three distinct heights. H omits the separate wave.','high','omission',dh=True,cr='03')
add('N03','Punctuation after A in first slanted row',r'\forall a\in A,',r'\forall a\in A,',r'\forall a\in A','The space between the capital A and the canceled existential contains no independent comma.','medium','text not on the page',dc=True,dh=True,cr='03')
add('N04','Left slanted note and its separator strokes','Default margin placement, no separator drawing','Left diagonal margin; note mentions a separating stroke','Explicit left margin with diagram, two formula rows, and separator strokes reproduced in TikZ','The note occupies the upper left margin. A long oblique separator and a shorter stroke at its opposite end are visible around it. C supplies no separator geometry or explicit left-margin selection.','high','drawing or diagram',dc=True,box=[25,105,300,545],cr='03')
add('N05','Unique existence sign in the main condition',r'\exists1',r'\exists !',r'\exists1','The following stroke is a continuous upright with no detached dot. This is the written numeral 1, not an exclamation mark.','high','misread symbol or index',dh=True,box=[1300,296,1372,358])
add('N06','Wrapped equality at end of main condition',r'\begin{aligned}\cdots\text{ tel que}\\s=\sigma(a).\end{aligned}','One-line condition ending s=σ(a)',r'\begin{aligned}\cdots\text{ tel que}\\s=\sigma(a).\end{aligned}','The first line runs to the right edge; s=σ(a) is on its own following line at the left. The wrapping is retained.','high','insertion or placement',dh=True,box=[270,278,1650,410])
# C actually includes its period in the aligned equality; only H omits it.
add('N07','Point following s=σ(a)',r's=\sigma(a).',r's=\sigma(a)',r's=\sigma(a).','A distinct dark round point stands after the closing parenthesis at the equation baseline; it is retained as the period already present in C.','high','omission',dh=True,cr='26')
add('N08','Second proposition, singular contour','orientation du contour','orientation des contours','orientation du contour','The short article is du, and contour ends without a plural s.','high','misread word',dh=True,box=[985,650,1340,720])
add('N09','Three left-margin sketches','Three centered figure macros','H_drawings/01-3.tex: all three sketches, described as left-margin drawings','Three figure macros explicitly placed in the left margin','The whole and upper half show the two-arrow sketch, the s sketch, and the a sketch in the left margin. Their nodes, arrow directions and labels agree with C and H’s supplied redraw; only C placement is changed.','high','insertion or placement',dc=True,box=[64,493,383,1105])
add('N10','Underline beneath extrémité',r'l’\uline{extrémité}','l’extrémité',r'l’\uline{extrémité}','A short horizontal underline is clearly separate from the letters below extrémité.','high','omission',dh=True,box=[943,747,1137,808])
add('N11','Sigma inverse insertion above arête',r'arête \inserted{$\sigma^{-1}(s)$} qui',r'arête \struck{\ill{}}\ \sigma^{-1}(s)\text{ qui}',r'arête \inserted{$\sigma^{-1}(s)$} qui','The small sigma inverse expression is above the line, with a curved connector into the gap after arête. H renders its wording on the line; its second cancellation belongs later, before s.','high','insertion or placement',dh=True,box=[277,794,510,907])
add('N12','Punctuation after origine before first bracket','origine [','origine. [','origine [','The dark terminal body is the final e of origine. There is no separate point in the gap before the square bracket.','medium','text not on the page',dh=True,cr='27')
add('N13','First bracketed incidence condition',r'\left[\begin{aligned}(u_\omega(s),\sigma^{-1}(s))&\in R,\\u_\omega(s)&\ne s\end{aligned}\right]',r'[(u_\omega(s),\sigma^{-1}(s))\in R,\ u_\omega(s)\ne s]',r'\left[\begin{aligned}(u_\omega(s),\sigma^{-1}(s))&\in R,\\u_\omega(s)&\ne s\end{aligned}\right]','The inequality occupies a second, short line below the right-hand end of the incidence pair. C preserves this wrap; H flattens it.','high','insertion or placement',dh=True,box=[1223,816,1568,925])
add('N14','Second bracketed incidence condition',r'(\sigma u_\omega(a),a)\in R,\ \sigma u_\omega(a)\ne\sigma a\\\text{i.e. }u_\omega(a)\ne a',r'(\sigma u_\omega(a),a)\in R,\ \sigma u_\omega(a)\ne\sigma a\ \text{i.e. }u_\omega(a)\ne a',r'(\sigma u_\omega(a),a)\in R,\ \sigma u_\omega(a)\ne\sigma a\\\text{i.e. }u_\omega(a)\ne a','The i.e. and final inequality form a second line inside the brackets. The dark a in the pair is ordinary readable a, with no distinct prior glyph recoverable.','high','insertion or placement',dh=True,box=[790,988,1620,1117],math='The repeated a and the two inequalities were checked against the ink; no mathematical repair was made.')
add('N15','Marginal brace beside Alors and the following line',r'\margin{$\big\}$}','No marginal brace',r'\reversemarginpar\margin{$\big\}$}\normalmarginpar','A thin right-facing curly brace stands to the left of the two lines across the horizontal fold. C lacks explicit left-margin selection; H omits it.','high','omission',dc=True,dh=True,box=[244,1140,279,1262])
add('N16','First autom abbreviation, Alors sentence','autom','automorphisme','autom','The word stops after the contracted m-like horizontal strokes; the letters orphisme are not present.','high','abbreviation expanded or spelling modernised',dh=True,box=[1060,1123,1235,1174])
add('N17','Les autom, before two u symbols','autom','autom.','autom','The short final horizontal exit is followed by a wide blank before u; no detached full stop is visible.','high','text not on the page',dh=True,box=[1165,1206,1335,1264])
add('N18','Canceled phrase before conditions équivalentes',r'\deleted{fait que}',r'\struck{faits que}',r'\deleted{fait que}','The first word ends with a raised t-return followed by blank space; there is no independent terminal s before que.','medium','misread word',dh=True,cr='10')
add('N19','No period after the statement of order','est n','est n.','est n','The line ends in the n-shaped trace without a separate point.','medium','text not on the page',dh=True,box=[1427,1523,1565,1602])
add('N20','Shorthand between the unequal translations and n≠2','sss','ssi','sss','Three joined curved/returning strokes are present. The final one continues down and has no separate i dot.','medium','abbreviation expanded or spelling modernised',dh=True,cr='12')
add('N21','Connector between 1° and 2° in prose references','ou',',',r'\unsure{ou|$-$}','The two separated low strokes can be a highly compressed ou or a dash-like trace. They are not the single curved comma printed by H. This is a new C doubt.','low','misread symbol or index',dc=True,dh=True,cr='16')
add('N22','Small hook immediately before tall right brace','No separate hook','No separate hook',r'\unsure{)}\big\}','A short, detached curved stroke stands just to the left of the tall brace. It may be a closing parenthesis, a comma-like remnant, or a pen remnant. It is preserved under doubt rather than absorbed silently into the brace.','low','omission',dc=True,dh=True,cr='16')
add('N23','Before g in the automorphism-set clause',r'g\in\operatorname{Aut}(S,A,R)',r'\{g\in\operatorname{Aut}(S,A,R)',r'g\in\operatorname{Aut}(S,A,R)','The half shows the descending g, membership sign and Aut, with no opening curly brace to the left of g.','high','text not on the page',dh=True,box=[1274,1701,1607,1787],math='An unmatched later closing brace is retained; no balancing sign is supplied.')
add('N24','ens abbreviation','l’ens','l’ens.','l’ens','The contracted ending has no detached point before des.','medium','text not on the page',dh=True,box=[1058,1704,1190,1776])
add('N25','Et following the closing brace','Et','et','Et','The initial letter is large, upright and repassed, retaining the capital form.','high','misread word',dh=True,box=[1412,1785,1501,1855])
add('N26','Alphabet in the first cyclic-group quotient',r'\mathbb{Z}/n\mathbb{Z}',r'\mathbf{Z}/n\mathbf{Z}',r'\unsure{Z|\mathbb{Z}}/nZ','Both forms here have a continuous top/diagonal/bottom outline; a distinct second diagonal is not securely separated from the pen width. Plain Z is my first candidate. This concerns actual ink, not H’s declared bold encoding for double-stroke fields.','low','misread symbol or index',dc=True,dh=True,cr='18')
add('N27','Inserted group name near left margin',r'\inserted{gpe $G^0$}',r'groupe G^0\text{ (note: added in margin)}',r'\inserted{gpe $G^{\unsure{0|\circ}}$}','The small marginal word is contracted, with a g-descender and p-like downstroke; it is the same gpe/grpe ambiguity first marked in the preceding line. The insertion curve joins before des. H records insertion in its note but expands the word.','medium','abbreviation expanded or spelling modernised',dh=True,cr='20')
add('N28','autom before inserted orientés','autom','automorphismes','autom','The ink stops at the contracted m and has no succeeding orphismes. The interlinear orientés and its caret are retained.','high','abbreviation expanded or spelling modernised',dh=True,box=[453,1983,779,2062])
add('N29','Canceled sentence starter near bottom',r'\deleted{Se donner un}',r'\struck{La donnée d’un}',r'\deleted{Se donner un}','The middle word ends with the returning r-shaped stroke of donner. The last word begins u directly, without d-apostrophe. The first short group reads Se.','medium','misread word',dh=True,cr='22')
add('N30','Insertion above torsor quotient',r'\inserted{$(n\geq1)$}',r'(n\geq1)',r'\inserted{$(n\geq1)$}','The parenthesized condition stands above the line and a long curved connector points to the gap between the quotient and the equals sign.','high','insertion or placement',dh=True,box=[891,2166,1059,2305])

add('N31','Detached small loop beneath S in S et A',r'S',r'S',r'\underset{\unsure{\circ}}{S}','The context included in the gloss crop exposes a distinct small blue loop below the capital S. Its rounded shape is visible, but its status as an intentional sign or a pen remnant is uncertain; it is retained underneath without calling it a subscript.','low','omission',dc=True,dh=True,box=[1090,1998,1158,2060],cr='21')

inventory=[]
def inv(element,kind,position,first,hand='his hand'):
    inventory.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('Page title','text','top, x230–800 y65–124',"Orientation d’un contour.")
inv('Opening definition','text','upper block, y140–282',"Choix pour tte/toute arête a∈A")
inv('Overwritten origin symbol','deletion','x450–503 y212–257','omega/o beneath sigma')
inv('Slanted marginal map','diagram','upper left margin, y230–348','A to S, sigma and separate tilde')
inv('Slanted marginal incidence row','margin note','upper left margin, y140–449','∀a∈A, canceled existential, (σ(a),a)∈R')
inv('Canceled sign in slanted note','deletion','within first marginal formula','exists1/exists')
inv('Canceled second marginal row','deletion','upper left diagonal, y309–524','∀s∈S/∀a∈S, ∃1 a∈A,')
inv('Separating marginal strokes','drawing','around slanted upper-left block','long oblique line and shorter end stroke')
inv('Orientation condition','display','y283–407','(O/0) Si ... s∈S, ∃1 a∈R{s} ... s=σ(a).')
inv('Canceled hypothesis in condition','deletion','x638–1112 y279–335','R{s}={a,b}, alors exists')
inv('Reduction line','text','y412–457','Réduction au cas connexe')
inv('First proposition','text','y463–600','Prop Si (S,A,R) est un contour connexe')
inv('Two directed arcs joined at a dot','drawing','left margin, x155–375 y495–574','arrow, filled point, upward-right arrow')
inv('Single directed edge with labels','drawing','left margin, x90–255 y651–755','s, sigma inverse s, u_omega(s)')
inv('Second proposition','text','y652–725','Prop Soit omega orientation du contour')
inv('Canceled first Prop','deletion','x275–374 y649–712','Prop')
inv('Vertex successor definition','text','y741–891','∀s∈S, soit ... l’extrémité de l’unique arête')
inv('Two canceled names before successor','deletion','x630–815 y762–790','omega(s)/w(s), u_omega/u')
inv('Replacement u_omega','insertion','x780–824 y731–771','u_omega above canceled name')
inv('Edge inverse name','insertion','x385–480 y806–856','sigma inverse (s), with curved connector')
inv('Canceled comme','deletion','x653–790 y858–881','comme')
inv('Vertex incidence bracket','display','right of definition, y823–922','(u_omega(s),sigma inverse(s)) in R; u_omega(s) not equal s')
inv('Edge successor definition','text','y925–1043','∀a∈A, soit u_omega(a) l’unique arc de S')
inv('Two successive labeled arcs','drawing','left margin, x61–280 y931–1108','sigma a, a, sigma u_omega(a), u_omega(a)')
inv('Edge incidence bracket','display','x785–1620 y990–1116','(sigma u_omega(a),a) in R ... i.e. u_omega(a) not equal a')
inv('Automorphism paragraph','text','y1116–1377','Alors u_omega:(S,A) ... Les autom ... conditions équivalentes')
inv('Overwritten object in first pair','deletion','x560–595 y1115–1161','R/B beneath A')
inv('Marginal brace','margin note','left beside fold, x248–276 y1149–1262','right-facing curly brace')
inv('Canceled fait que','deletion','x848–1060 y1300–1373','fait que')
inv('First numbered condition','text','y1393–1451','1°) ∀s∈S, s lié à gs')
inv('Second numbered condition','text','y1458–1520','2°) ∀a∈A, a lié à ga')
inv('Order statement','text','y1532–1602','Si n=card S=card A ... est n')
inv('Comparison, bijection and group paragraph','text','y1625–2139','flèche/et ... or(S,A,R) ... gpe cyclique ... torseurs sous G^0')
inv('Canceled formé','deletion','x1524–1628 y1898–1981','formé')
inv('Interlinear le','insertion','x1543–1587 y1876–1918','le')
inv('Group name added in margin','insertion','x210–389 y1956–2041','gpe G^0/circle with connector')
inv('Interlinear orientés','insertion','x595–753 y1959–2030','orientés and insertion caret')
inv('Interlinear tuple gloss','insertion','x950–1295 y1938–2055','lire/les de S,A,R;omega) with connector')
inv('Detached loop below S','insertion','x1090–1158 y1998–2060','small loop under S, retained as an uncertain independent mark')
inv('Canceled sentence starter','deletion','x443–789 y2187–2230','Se donner un')
inv('Torsor and circular-order paragraph','text','y2243–2353','Torseur sous double-stroke Z/n double-stroke Z = ensemble ...')
inv('n condition added above line','insertion','x895–1057 y2175–2306','(n greater than or equal to 1) and curved connector')
inv('Overwritten word after ensemble','deletion','x1203–1245 y2250–2288','où beneath à')
inv('Raised cross or asterisk','insertion','x638–660 y2302–2323','raised cross/asterisk immediately before circulaire')
inv('Archive foliation','margin note','bottom left, x40–82 y2290–2341','7; transcribed only as archive comment','unnamed hand')

notation=[
 dict(sign='sigma',reading=r'\sigma',ink='Low loop with a long top exit; an overwritten origin symbol must be treated separately.',place='Opening definition, slanted map, all incidence formulas and drawings'),
 dict(sign='omega',reading=r'\omega',ink='Two rounded lower lobes and curled ends in the full-size proposition; compressed to a short wave in subscripts.',place='First proposition and successor symbols'),
 dict(sign='exists1',reading=r'\exists1',ink='Separate continuous upright after existential; no exclamation-dot in the main condition.',place='Main condition; both crossed marginal occurrences'),
 dict(sign='O/0 label',reading=r'\unsure{O|0}',ink='Open circular loop in parentheses has no decisive alphabet cue.',place='Orientation condition label'),
 dict(sign='sigma inverse',reading=r'\sigma^{-1}(s),\ \sigma^{-1}s',ink='Raised minus and small upright; parentheses occur in insertion/formula but not in sketch label.',place='Vertex sketch, arête insertion, first bracket'),
 dict(sign='dash / map arrow',reading=r'\unsure{-|\to}',ink='Short flat shaft and a single downward tip, without a resolved upper wing.',place='Alors map between two pairs'),
 dict(sign='sss',reading='sss',ink='Three connected short returning strokes; no detached final i dot.',place='Order comparison sentence'),
 dict(sign='or',reading=r'\operatorname{or}',ink='Low oval much shorter than adjacent capital S, A, R, followed by r shoulder.',place='Bijection clause'),
 dict(sign='gpe / grpe',reading=r'\unsure{gpe|grpe}',ink='Long descending g, flattened middle, p-like drop and e-like ending; recurring insertion given with first candidate.',place='Cyclic group line and marginal group insertion'),
 dict(sign='G round superscript',reading=r'G^{\unsure{0|\circ}}',ink='Closed near-round raised loop; first occurrence marked and later occurrence given with 0.',place='Marginal group insertion and torseur conclusion'),
 dict(sign='Z alphabet in first quotient',reading=r'\unsure{Z|\mathbb{Z}}/nZ',ink='The first quotient has broad single-looking diagonal forms; separate doubling cannot be securely distinguished from pen width. The bottom torsor quotient has clearer doubled strokes in the half.',place='Cyclic group line, contrasted with bottom torsor line'),
 dict(sign='raised crossing mark',reading=r'\unsure{{}^{\times}|{}^{*}}',ink='Two crossing directions and a dense centre; neither opening nor closing guillemet.',place='Before circulaire at bottom')]
abbreviations=[dict(written='tte (uncertain against toute)',expansion='toute'),dict(written='i.e.',expansion='id est'),dict(written='Prop',expansion='Proposition'),dict(written='autom',expansion='automorphisme(s)'),dict(written='sss',expansion='si et seulement si'),dict(written='ens',expansion='ensemble'),dict(written='équiv.',expansion='équivalentes'),dict(written='gpe / grpe',expansion='groupe'),dict(written='card',expansion='cardinal'),dict(written='or',expansion='orientations')]
checks=[
 dict(statement='The written edge description says arc de S after taking a in A.',event_type='local type consistency check',reasoning='The page itself uses a in A and places sigma(a) in S, so its edge/vertex roles make S in arc de S locally anomalous. The crop nevertheless shows the upper and lower bends of S.',outcome='Anomaly recorded; S retained exactly. No correction to A and no external definition used.'),
 dict(statement='The two written edge inequalities are equivalent if the marginal sigma map is bijective.',event_type='conditional symbolic check',reasoning='For injective sigma, sigma(u_omega(a))=sigma(a) iff u_omega(a)=a; negating gives the two inequalities appearing on the two display lines.',outcome='Locally consistent under the bijection indicated by the marginal tilde. The check does not establish the entire proposition.'),
 dict(statement='If u_omega has order n, compare u_omega and its inverse.',event_type='conditional algebraic check',reasoning='u=u^(-1) iff u^2=1. For an element of finite order n, this is equivalent to n dividing 2. If n is at least 2, inequality is equivalent to n not equal to 2 and to n at least 3.',outcome='The displayed bound is consistent subject to n at least 2; the page’s later n at least 1 concerns the separately begun torsor statement. The unclear introductory word and shorthand were decided from ink, not from this calculation.')]
notes=[
 'One handwritten text sheet in his hand. Title: Orientation d’un contour. A separate un-underlined line says Réduction au cas connexe. There are two live Prop labels; an earlier Prop before the second is canceled. No date appears.',
 'The page defines an orientation using an origin map, states that a connected contour has two orientations, defines successor maps on vertices and edges, and discusses their order and the group acting on vertex and edge sets. It then starts a torsor/circular-order statement and ends mid-sentence at Se donner un contour.',
 'Archive foliation 7 appears in a lower corner and is included only as a comment, not mspage. There is no cotefile marker on this isolated continuation page.',
 'The actual diagrams/drawings are one slanted A-to-S diagram, three directed-arc sketches, separating strokes by the slanted note, and a marginal brace. H’s supplied 01-3 redraw was read and agrees on all three sketch topologies, dots, labels and directions; stylistic coordinates are not counted as differences.',
 'All original C uncertainties are explicitly accounted for in D01–D24. N21, N22, N26 and N31 are new doubts; their doubt_action fields are empty. The main-condition point was already present in C and is not counted as a C omission.',
 'The written arc de S is kept despite its local type mismatch. The closing brace in the automorphism clause is unmatched on this sheet, and the added tuple gloss has a closing parenthesis without a visible opening one. Neither is silently completed.',
 'No authorial question mark or explicit doubt word is securely present. The difficult word before the inequality remains flèche/et; it has not been replaced with a mathematically expected connective.',
 'H expands several abbreviations, changes sss to ssi, substitutes guillemets for high quote ticks and for the bottom raised crossing mark, and changes the canceled bottom starter. These are recorded separately from equivalent macro syntax such as H’s declared bold encoding for double-stroke number symbols.',
 'S.json is an empty array: there are no sweep rows to confirm or overturn.',
 'Only the supplied notation snapshot, this page packet, its H drawing supplement, and its three images were used. No OCR, recognition library, external text, web, other page, or other reader was consulted.',
 '27 distinct tight crops were generated and successfully viewed exactly once each. The slanted-note crop was rotated -57 degrees. Crops were enhanced with LANCZOS, autocontrast, and unsharp mask; crop_log.json preserves every original bbox, rotation and reason.',
 'Whole-image dimensions are 1694 by 2366 pixels. Each supplied half is 1694 by 1263; the lower half begins at whole-image y=1103. All report bboxes are in whole-image coordinates.'
]
unresolved=[
 dict(place=f['place'],reading=f['final'],alternatives=f['final'] if f['id'].startswith('D') else ('closing parenthesis; comma-like remnant; pen remnant' if f['id']=='N22' else f['final']),confidence=f['confidence'])
 for f in F if (f['doubt_action']=='retain' or f['id'] in ('N21','N22','N26','N31'))
]
coverage=[
 dict(block='Title and opening two lines',bbox=[225,65,1595,285],result='Every word, quote, accent, formula and overwrite compared with C and H.'),
 dict(block='Upper-left slanted note',bbox=[25,105,300,545],result='Map decoration, both formula rows, two cancellations and separating strokes covered; rotation crop used.'),
 dict(block='Orientation condition and reduction line',bbox=[270,278,1650,457],result='Both wrapped condition lines, canceled hypothesis, existential numeral and punctuation checked; separate reduction line retained.'),
 dict(block='Two propositions and first two drawings',bbox=[90,460,1530,755],result='Both Prop labels, cancellation, singular article, underlines, omega, nodes/arrows/labels compared.'),
 dict(block='Vertex definition and bracket',bbox=[257,727,1570,926],result='Cancellations, two insertions, underline, indices, inequalities and display wrap checked.'),
 dict(block='Edge definition, bracket and third drawing',bbox=[60,916,1625,1118],result='All text, visible S, pair a, commas, inequalities, i.e. wrap, labels and arrows checked.'),
 dict(block='Automorphism paragraph and two conditions',bbox=[245,1110,1555,1521],result='Map correction, connector, marginal brace, contractions, inverse signs, canceled phrase, numbering and g-variables checked.'),
 dict(block='Order, bijection, group and torsor conclusion',bbox=[209,1525,1635,2140],result='Every line compared; small words, sss, case, unmatched delimiter, number-symbol alphabet, insertions and cancellations covered.'),
 dict(block='Bottom canceled starter and incomplete paragraph',bbox=[293,2163,1640,2355],result='Canceled words, added n-condition, overwritten small word, noun ending, raised mark, period and incomplete final phrase checked.'),
 dict(block='Foliation',bbox=[40,2289,83,2344],result='Archive 7 recorded only as comment.'),
]
report=dict(scan=8,reader='R3',start_utc='2026-11-20 01:07:04 UTC',end_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),images_viewed=[
'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-01_75_scan008.jpg',
'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-01_75_scan008_a.jpg',
'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-01_75_scan008_b.jpg'],reading_file='out/readings/scan008/R3/reading.tex',crop_count=len(log),findings=F,inventory=inventory,notation=notation,abbreviations=abbreviations,notes=notes,checks=checks,unresolved=unresolved,coverage=coverage,
verification_events=[
 dict(sequence=1,event_type='inputs read',detail='Brief v08, conventions, PREAMBLE, notation snapshot, metadata, C, H, C_context, empty S, and H_drawings/01-3.tex read.'),
 dict(sequence=2,event_type='whole viewed',detail='1694x2366 whole page viewed once for layout and complete inventory.'),
 dict(sequence=3,event_type='upper half viewed',detail='Upper supplied half viewed once, with line-by-line C/H comparison.'),
 dict(sequence=4,event_type='lower half viewed',detail='Lower supplied half viewed once, with line-by-line C/H comparison.'),
 dict(sequence=5,event_type='tight crops viewed',detail='Crops 01–25 individually displayed once in small batches. All output images successfully displayed.'),
 dict(sequence=6,event_type='punctuation follow-up crops viewed',detail='Crops 26–27 displayed once for two still-open punctuation loci. No repeated whole/half or same-locus crop.'),
 dict(sequence=7,event_type='mathematical checks',detail='Three limited checks recorded above; no proof of the whole page asserted.'),
 dict(sequence=8,event_type='output completeness check',detail='Original C doubts enumerated D01–D24; empty S confirmed; all drawings and correction elements included; JSON, braces and environments checked without LaTeX compilation.')],
counts=dict(findings=len(F),original_c_doubts=24,c_doubts_resolved=sum(f['doubt_action']=='resolve' for f in F),c_doubts_retained=sum(f['doubt_action']=='retain' for f in F),diff_c=sum(f['diff_c'] for f in F),diff_h=sum(f['diff_h'] for f in F)))
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['counts'],ensure_ascii=False));print('crop_count',report['crop_count'])
