from author import Page
p=Page('156-4',64)
p.replace(r'\uline{Composantes connexes \unsure{du|de} \deleted{$\unsure{\mathcal F|F}$}\unsure{Sle|site|Syst.} entier $\mathcal F$.}',r'\uline{Composantes connexes de \deleted{$\mathcal F$}la \unsure{contrée|contr.} $\mathcal F$.}')
p.replace(r'\limits_{x\in M_i\cap M_{\leq F}}x',r'\limits_{X\in M_i\cap M_{\leq F}}X')
p.replace(r'\unsure{appelle}', 'appelle')
p.replace(r'\deleted{\unsure{et ?}}',r'\deleted{et \unsure{?}}')
p.replace(r'\unsure{sont}',r'\unsure{sont|\deleted{sont}}')
p.replace(r'\unsure{Inscrivons}',r'\unsure{Inscrivons|Inversement}')
p.replace(r'\deleted{$\unsure{,C3}$}',r'\deleted{$,C3$}')
p.replace(r'\text{\unsure{est le}}',r'\text{est le}')
p.replace(r'F\unsure{\in|\subset}\mathcal F',r'F\in\mathcal F')
p.replace(r'\unsure{suiv.}','suiv.')
p.replace(r'\deleted{\unsure{\coprod|\bigcup}}\mathop{\unsure{\bigcup|\coprod}}\limits_i',r'\deleted{\coprod}\mathop{\bigcup}\limits_i')
p.replace('(réunion disj.)','(réunion disj)')
p.replace(r'Sup \unsure{quelc.}',r'Sup quelc.')
curve1=r'\margin{\begin{tikzpicture}[x=1cm,y=1cm]\draw[thin] (0,-.45) .. controls (0,.05) and (.3,0) .. (.55,0) -- (1.5,0) .. controls (1.9,-.02) and (2.1,-.28) .. (2.8,-.28);\end{tikzpicture}}'
curve2=r'\margin{\begin{tikzpicture}[x=1cm,y=1cm]\draw[thin] (0,0) -- (.8,0) .. controls (1.2,0) and (1.02,-.3) .. (1.5,-.32) .. controls (1.9,-.4) and (2.45,-.38) .. (2.8,-.34);\end{tikzpicture}}'
p.replace("$\\varnothing$.\n", "$\\varnothing$.\n"+curve1+'\n')
p.replace('Sup quelc., et aux Inf non vides}\n','Sup quelc., et aux Inf non vides}\n'+curve2+'\n')
p.change('opening paragraph final dots',r'disjointes\ldots .','disjointes…',r'disjointes\ldots .','Three small dots are followed by a separate lower terminal point.','top')
p.change('upper oblique NB',r'NB Dans tout ceci, on n\'a pas besoin de C_3',r'NB \ill{} C3 \ill{}',"NB Dans tout ceci, on n'a pas besoin de C_3",'The upright crop shows Dans tout on the first line, ceci, on n’a pas on the second, and besoin de C_3 below. NB has its own underline.','margin_top',kind=r'readable ink left as \ill{}',marked='yes')
p.change('heading preposition',r'\unsure{du|de}','de','de','The d loop ends in a short e stroke before the crossed letter.','heading',dc=True,dh=False,kind='misread word')
p.change('heading overwritten family symbol',r'\deleted{\unsure{\mathcal F|F}}','omitted',r'\deleted{\mathcal F}','A large F with a curled lower foot and swept upper bar is crossed immediately before la.','heading',dc=True,kind='omission',confidence='medium')
p.change('heading article',r'\unsure{Sle|site|Syst.}',r'\uncertain{la}','la','The tall loop of l is followed by a low rounded a; there is no initial S or further word.','heading',dc=True,kind='misread word',confidence='medium',marked='yes')
p.change('heading noun','entier','contrée',r'\unsure{contrée|contr.}','An open c and low on precede a tall t and r hump. The detached upper mark and tiny final stroke support contrée, but the compressed ending leaves contr. possible.','heading_word',dc=True,kind='misread word',confidence='medium')
p.doubt('heading noun','contrée|contr.','The last two ink marks may be an accent and compressed e ending or an abbreviated ending','heading_word')
p.change('heading final punctuation','F.','F','F.','A separate point lies at the right edge after the family symbol.','heading')
p.change('definition of F_i, variable case','x in both positions','X in both positions','X in both positions','The main X has two long crossed diagonal strokes at capital height; the index uses the same crossed shape at index size.','formula',dc=True,dh=False,kind='misread symbol or index',consequential='The defining supremum is indexed by capital X, and its summand is X.')
p.change('definition display punctuation','no terminal point','terminal point','no terminal point','Clear space follows the displayed X; there is no point there.','formula')
p.change('lower oblique margin opening',r'On \unsure{appelle} F_i la',r'\ill{} les composantes \ill{} F_i','On appelle F_i la','The upright crop shows on and the doubled p descenders followed by e/l/l/e in appelle, then F_i la on the next line.','margin_left',dc=True,kind=r'readable ink left as \ill{}',confidence='medium',marked='yes')
p.change('lower margin earlier symbol',r'\deleted{\unsure{F_i}}','omitted',r'\deleted{\unsure{F_i}}','Dense crossed vertical and horizontal strokes survive before i-composante; the older index is partly merged with the word above.','margin_left',kind='omission',confidence='low')
p.doubt('lower margin earlier symbol','F_i','The cancellation overlaps the p descenders of appelle and obscures the lower index','margin_left','low')
p.change('lower margin complete continuation','i-composante de F, ou la trace de F sur M_i (ou sur F_i)',r'fragments ... de F sur M_i','i-composante de F, ou la trace de F sur M_i (ou sur the calligraphic F_i)','The hyphen after i, full composante, comma and ou, trace with its crossed t, both sur groups, and closing family symbol with index are visible when rotated.','margin_left',kind=r'readable ink left as \ill{}',marked='yes')
p.change('after somme directe, cancelled connector',r'\unsure{et ?}',r'\ill{}',r'et \unsure{?}, deleted','The e loop and tall t are secure; the separated hooked punctuation has no clearly visible lower point.','old_et',dc=True,kind=r'readable ink left as \ill{}',confidence='medium',marked='yes')
p.doubt('after cancelled et','?','A hook and descending stroke remain, but its lower point is not visible','old_et')
p.change('finite-type sentence initial','Si','si','Si','The initial S is a tall double curve.','finite')
p.change('finite-type inserted alternative','(ou I=pi_0(M) fini!), inserted','(ou? I=pi_0(M) fini!), baseline','(ou I=pi_0(M) fini!), inserted','The small raised parenthesis begins with two connected low ou curves, then I=pi_0(M) and fini with an exclamation point.','finite',kind='insertion or placement',marked='yes')
p.change('finite-type insertion leader','omitted','omitted','curved callout line reproduced in TikZ','A thin line starts beside alors, curves beneath the raised parenthesis and continues to the right.','finite',dc=True,kind='drawing or diagram')
p.change('finite-type exception','sauf','sauf, uncertain','sauf','The initial s and rounded au run into the long f descender; all four letters remain clear.','finite',marked='yes')
p.change('finite-type predicate',r'\unsure{sont}',r'\struck{\ill{}}',r'\unsure{sont|\deleted{sont}}','The s/o/n/t strokes can be read, but the strong horizontal ink overlaps their baseline and may also be a cancellation; the state remains marked.','sont',dc=True,kind='deletion state (struck given live or live given struck)',confidence='low',marked='yes')
p.doubt('finite-type predicate',r'sont|\deleted{sont}','The horizontal stroke cannot securely be separated from the joined baseline of the word; live first, cancellation alternative','sont','low')
p.change('cancelled opening before Soit',r'\unsure{Inscrivons}','Inversement',r'\unsure{Inscrivons|Inversement}','The capital I and several low curls survive, including a rounded loop near the end; repeated horizontal cancellations cover the middle letters.','old_inverse',dc=True,kind='misread word',confidence='low')
p.doubt('cancelled opening before Soit','Inscrivons|Inversement','Repeated horizontal strikes obscure the middle consonants and final letter joins','old_inverse','low')
p.change('family paragraph ens punctuation',"l'ens", "l'ens.", "l'ens",'No detached point follows ens either at the family definition or before de ses objets.','family')
p.change('family definition agreement','telle','telles','telle','The final e trails into clear space before que; no additional s stroke follows.','family',kind='misread word',confidence='medium')
p.change('family definition inclusion',r'\overline F\subset M_i',r'F\subset M_i',r'\overline F\subset M_i','A separate horizontal bar stands above the F before subset M_i.','family',kind='misread symbol or index',consequential='The inclusion defining the family uses barred F.')
p.change('after Alors, cancelled short word',r'\unsure{si}',r'\ill{}',r'\unsure{si}, deleted','Two small looped and upright strokes survive beneath a diagonal strike; the short reading remains uncertain.','old_si',kind=r'readable ink left as \ill{}',confidence='low',marked='yes')
p.doubt('after Alors, cancelled short word','si','The crossing stroke merges the loop and the short upright ending','old_si','low')
p.change('cancelled third condition',r'\unsure{,C3}',r'\ill{}',',C3, deleted','The comma descends at left; an open C and the two curved lobes of 3 survive under the scribbled cancellation.','old_C3',dc=True,kind=r'readable ink left as \ill{}',confidence='medium',marked='yes')
p.change('cancelled phrase before diagram',"et l'application", "L'application", "et l'application",'The small initial et and the lower-case l are visible on the crossed line.','old_diagram',kind='omission')
p.change('first diagram upper row','live calligraphic F to product of calligraphic F_i','whole diagram struck','upper row live; lower mapping cancelled','The horizontal cancellation crosses the lower mapping. Its curved return borders the upper row without crossing the upper arrow or either label.','old_diagram',kind='deletion state (struck given live or live given struck)')
p.change('first diagram surviving labels and cancellation','two-row TikZ diagram with curved cancellation','fragmentary struck formula and illegible text','two-row TikZ diagram with curved cancellation','Both upper objects, the right arrow, the lower F mapsto tuple with i in I, and the large return stroke are visible; the diagram is retained as drawn.','old_diagram',kind='drawing or diagram',marked='yes')
p.change('first diagram lower connector',r'\unsure{ou|où}',r'\ill{}',r'\unsure{ou|où}','A low ou group is crossed by the cancellation; a short mark above is fused with that line, leaving the accent unresolved.','old_tail',kind=r'readable ink left as \ill{}',confidence='low',marked='yes')
p.doubt('first diagram lower connector','ou|où','The possible accent touches the cancellation line','old_tail','low')
p.change('first diagram final words',r'\unsure{est le}',r'\ill{}','est le, deleted','Despite the crossing line, the looped e, angular s, tall t, and final l/e curve are visible.','old_tail',dc=True,kind=r'readable ink left as \ill{}',confidence='medium',marked='yes')
p.change('Si F relation',r'\unsure{\in|\subset}',r'\in',r'\in','The curved sign has a short middle horizontal stroke.','old_diagram',dc=True,dh=False,kind='misread symbol or index')
p.change('component direction abbreviation',r'\unsure{suiv.}','suivant','suiv.','A compact suiv ends in a detached point before les M_i; no ant follows.','old_diagram',dc=True,kind='abbreviation expanded or spelling modernised')
p.change('overwritten union, earlier sign',r'\unsure{\coprod|\bigcup}','omitted',r'\deleted{\coprod}','A straight base projects beyond two earlier upright strokes underneath the rounded overwrite.','union',dc=True,kind='omission',confidence='medium')
p.change('overwritten union, later sign',r'\unsure{\bigcup|\coprod}',r'\bigcup',r'\bigcup','The later heavy strokes form a continuous rounded U over the earlier straight base.','union',dc=True,dh=False,kind='misread symbol or index',confidence='medium')
p.change('union index','i','omitted','i','A dot and short stem are visible below the union symbol.','union',kind='omission')
p.change('union parenthetical punctuation','(réunion disj.)','(réunion disj.)','(réunion disj)','The j descender is followed directly by the closing parenthesis near the page edge, without a detached point.','union_end',dc=True)
p.change('fixed-component application',r'F\longrightarrow F_i',r'\mathfrak F\to\mathfrak F_i',r'F\longrightarrow F_i','The two labels have the simple upright F stems and short crossbars used for individual figures here; the later family diagram has visibly swept calligraphic stems.','bottom',kind='misread symbol or index',confidence='medium',consequential='The fixed-i application is written with the individual-figure symbols F and F_i.')
p.change('Sup abbreviation and punctuation',r'Sup \unsure{quelc.},','Sup quelc.','Sup quelc.,','The q descender, u/e/l/c sequence and point are readable; a small comma follows the abbreviation.','bottom',dc=True,kind='abbreviation expanded or spelling modernised',confidence='medium')
p.change('Inf qualifier','non vides','non vides, uncertain','non vides','The low non group is followed by v, a dotted i, tall d and the final es tail.','bottom',marked='yes')
p.change('Sup/Inf clause placement','inserted','baseline','inserted below aux','The smaller clause occupies two raised/squeezed lines at the right below the main sentence and above the mapping.','bottom',kind='insertion or placement')
p.change('Sup/Inf clause callout rule','omitted','omitted','bent underline reproduced in TikZ','A thin line passes below Sup quelc. and bends down beneath non vides.','bottom',dc=True,kind='drawing or diagram')
p.inventory([
 ('text','top continuation','de F, et celles de A'),
 ('margin note','upper left oblique','NB Dans tout ceci'),
 ('text','underlined heading','Composantes connexes de la contrée'),
 ('deletion','heading before la','calligraphic F'),
 ('text','upper middle','Soit M=coprod M_i'),
 ('text','middle','Pour toute figure F, posons'),
 ('display','middle','F_i=Sup over X in M_i cap M_leF'),
 ('margin note','middle left oblique','On appelle F_i la i-composante'),
 ('deletion','middle left note','old F_i'),
 ('text','under display','Alors F est la somme directe'),
 ('deletion','before Si','et ?'),
 ('insertion','right above alors','(ou I=pi_0(M) fini!)'),
 ('drawing','under finite-index insertion','curved callout line'),
 ('text','finite-type continuation','tous les F_i sauf un nb fini'),
 ('deletion','above Soit','Inscrivons|Inversement'),
 ('text','lower middle','Soit calligraphic F_i l’ens des F'),
 ('deletion','after Alors','si'),
 ('deletion','after C1,C2',',C3'),
 ('deletion','before old diagram','et l’application'),
 ('diagram','lower middle left','calligraphic F to product calligraphic F_i; lower cancelled mapping'),
 ('deletion','lower row of first diagram','F mapsto (F_i) indexed by I, ou F_i est le'),
 ('text','beside first diagram','Si F in calligraphic F'),
 ('text','under first diagram','alors bar F_i=bar F cap M_i'),
 ('deletion','union overwrite','old coproduct sign'),
 ('text','bottom','Pour i fixé, l’application'),
 ('insertion','bottom right','Sup quelc., et aux Inf non vides'),
 ('drawing','under Sup/Inf insertion','bent underline'),
 ('text','bottom left','L’application'),
 ('diagram','bottom','calligraphic F to product calligraphic F_i; F mapsto (F_i)'),
 ('text','last two lines','est injective, et la relation d’ordre'),
])
p.notation('capital X in a supremum', 'X','Two straight crossing diagonals; the main summand is capital height, and the same shape appears in the index.')
p.notation('union over an older coproduct',r'\deleted{\coprod}\bigcup','A rounded heavy U overlays two earlier upright stems and a projecting straight horizontal base.')
p.r['abbreviations']=[dict(abbreviation=a,expansion=b,evidence='156-4:064; manuscript form retained') for a,b in [('comp.','composante(s)'),('t.f.','type fini'),('nb','nombre'),('ens','ensemble'),('suiv.','suivant'),('disj','disjointe'),('quelc.','quelconques'),('contr.','contrée; alternative reading of heading')]]
p.save()
