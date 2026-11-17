from author import Page
p=Page('156-4',47)
p.replace(r'\unsure{\mathcal M|M}', 'M')
p.replace(r'\mathcal M',' M')
p.replace(r'\unsure{\mathcal F|\mathscr F}',r'\mathcal F')
p.replace(r'\unsure{une sorte de symétrie|deux sortes de symétries}','une sorte de symétrie')
p.replace(r'\unsure{ou bien|comme}',r'\unsure{en tant|ou bien|comme}')
p.replace(r'par \unsure{les axiomes des}',r'\unsure{axiomatique des|par les axiomes des}')
p.replace(r'\unsure{Cela étant}','Cela étant')
p.replace(r'\ll\unsure{Y}',r'\ll Y')
p.replace('équivaut à','équivaut :')
p.replace(r'\uline{sont compatibles}',r'sont \uline{compatibles}')
p.replace(r'\unsure{soient|sont}','soient')
p.replace(r'\unsure{4|9}','4')
p.replace(r'\unsure{intervertir}','intervertir')
p.replace(r'\unsure{implique}','implique')
p.replace(r'\node[inner sep=1pt] (a) {intervertir}; \draw[<->] (a.north east) .. controls +(-.7,.2) and +(-.7,-.2) .. (a.south east);',r'\node[inner sep=1pt] (a) {intervertir}; \draw[->] (a.north) .. controls +(0,.6) and +(-.5,0) .. (1.4,1); \draw[->] (a.south) .. controls +(0,-.6) and +(-.5,0) .. (1.4,-1);')
p.replace('% Two vertical emphasis strokes.',r'\margin{\tikz{\draw (0,0)--(0,.8);\draw (.06,0)--(.06,.8);}}')
# Each remaining C doubt was examined in the recorded enlarged regions.
p.change('marginal opening','Ainsi, M/cal M','Donc, M s’identifie ill.','Ainsi, M s’identifie à un ens de parties de F…','The rotated note begins with A followed by insi and a comma; its live lines include the set-of-parts wording and both F_X and figures élémentaires.','margin_all',dc=True,kind='misread word',marked='yes')
p.change('marginal alphabet',r'\mathcal M and unsure F/script F',r'\mathcal M',r'M; \mathcal F','M has two unornamented uprights; the family F has a hooked foot and curved head. This maps the glyphs to the running notation table.','margin_all',dc=True,dh=False)
p.change('first deleted marginal paragraph','full paragraph, three doubts','fragments in editorial note','full deleted paragraph, doubts retained','Diagonal cancellation traverses the paragraph beginning Donc on peut considérer. It remains readable in substantial part, including subdivision and relation d’ordre.','margin_portee',kind='omission',marked='yes')
p.change('deleted portée',r'\unsure{portée}','not transcribed',r'\unsure{portée}','The p descender and later raised strokes survive, but cancellation joins the middle letters.','margin_portee',confidence='low',kind='omission',marked='yes')
p.change('deleted family subscript',r'\unsure{él|el}','not transcribed',r'\unsure{él|el}','The small e/l group has a raised stroke; the line crossing it prevents a firm accent decision.','margin_portee',confidence='medium',kind='omission',marked='yes')
p.change('deleted Sigma',r'\unsure{\Sigma}','not transcribed',r'\unsure{\Sigma}','The heavy zigzag-like sign is struck through and partly retraced.','margin_portee',confidence='low',kind='omission',marked='yes')
p.change('second deleted marginal paragraph',r'\unsure{une sorte de symétrie|deux sortes de symétries}','omitted','une sorte de symétrie','The rotated line shows une followed by singular sorte, de, and symétrie.','margin_work',dc=True,kind='omission',marked='yes')
p.change('after on travaille sur F',r'\unsure{ou bien|comme}', 'omitted',r'\unsure{en tant|ou bien|comme}','The first short word has an open e and n-like terminal; the following strokes are crossed. The visible en is reflected in the preferred uncertain reading.','margin_workright',dc=True,confidence='low',kind='misread word',marked='yes')
p.change('raised words over on travaille',r'par \unsure{les axiomes des}','omitted',r'\unsure{axiomatique des|par les axiomes des}','The raised group contains a visible -tique-like run and des; its beginning and attachment are crossed. The whole group is now explicitly doubtful.','margin_work',dc=True,confidence='low',kind='misread word',marked='yes')
p.change('end of crossed marginal phrase',r'\unsure{et tantôt}','omitted',r'\unsure{et tantôt}','The horizontal cancellation and other baselines intersect this group; its wording remains unresolved.','margin_workright',confidence='low',kind='omission',marked='yes')
p.change('crossed marginal order symbol',r'\unsure{C\prime|\leq}','omitted',r'\unsure{C\prime|\leq}','The curved sign and raised short stroke are cut by a long diagonal; their exact identity remains uncertain. The following subdivision, raffinement and ens. de parties lines are retained.','margin_order',confidence='low',kind='omission',marked='yes')
p.change('opening cancelled prose',r'\deleted{\unsure{Cela étant}}','omitted',r'\deleted{Cela étant}','The horizontal cancellation crosses Cela and étant; the initial loop, l and final t are separable from the oblique marginal writing.','cela',dc=True,kind='omission')
p.change('cancelled opening formula',r'\unsure{X}\ll\unsure{Y}\quad\unsure{F\prime}\unsure{\supset|\subset}F_X',r'\ill{} F_X',r'\unsure{X}\ll Y\quad\unsure{F\prime}\unsure{\supset|\subset}F_X','Y has a clear fork and descending stem; X, the second figure sign and the inclusion orientation are crossed by repeated zigzags.','cancel_top',dc=True,kind='readable ink left as \\ill{}',confidence='medium',marked='yes')
p.change('first live word','Si',r'\ill{}','Si','The S and separate i dot remain visible at the left edge of the live line.','cancel_top',kind='readable ink left as \\ill{}',marked='yes')
p.change('cancelled subscript after X in F',r'F_{\deleted{\unsure{X|x}}}','F',r'F_{\deleted{\unsure{X|x}}}','A small crossed angular letter lies below F; its size and cancellation prevent a secure case decision.','cancel_top',kind='deletion state (struck given live or live given struck)',confidence='medium')
p.change('équivaut punctuation','équivaut à','équivaut à :','équivaut :','The word ends before a separate colon; the intervening space contains no à.','equiv',dc=True,kind='text not on the page')
p.change('raised equivalent order condition',r'\inserted{i.e. Y\leq X}','(i.e. Y ≤ X)',r'\inserted{i.e. Y\leq X}','The words and inequality are raised over the line with a placement leader, without enclosing written parentheses.','top',kind='insertion or placement')
p.change('compatibility underline',r'\uline{sont compatibles}',r'sont \emph{compatibles}',r'sont \uline{compatibles}','The underline begins under compatibles and leaves sont outside it.','compat',dc=True,dh=False)
p.change('upper axiom overwrite',r'C deleted unsure 2/3, unsure 3/2','C 2 (written on another numeral)','C deleted unsure 2/3, unsure 3/2','Both 2 and 3 components are visible, superposed and offset; stroke order remains uncertain.','renumber_top',confidence='medium',kind='misread symbol or index',marked='yes')
p.change('quantified first letter',r'\unsure{x|X}','X',r'\unsure{x|X}','The cross is smaller than the following Y and F, but case is not settled by its shape.','c2',confidence='medium',kind='misread symbol or index')
p.change('end of upper axiom',r'\unsure{soient|sont}','soient','soient','The separate dotted i in the first run and final ent ending support soient despite retracing.','soient',dc=True,dh=False)
p.change('reference in left margin',r'Fig \unsure{4|9}','Fig 4','Fig 4','The rotated digit has an open angular head and descending vertical, with no closed bowl.','inter',dc=True,dh=False)
p.change('corollary cancellation','live Cor; deleted En particulier si X; live Pour que…','entire corollary struck','live Cor; deleted En particulier si X; live Pour que…','One oblique rule crosses only the abandoned higher line; Cor and the subsequent proposition have clear live baselines.','cor',kind='deletion state (struck given live or live given struck)')
p.change('corollary abandoned opening','En particulier si X',r'\ill{}','En particulier si X','The crossed line shows the full En particulier si X, including its final X.','cor',kind='readable ink left as \\ill{}',marked='yes')
p.change('corollary appartiennent','double underline under app',r'\ill{} appartiennent','double underline under app','Two distinct short rules lie under the app group; no separate missing word precedes appartiennent.','cor',kind='text not on the page',marked='yes')
p.change('abandoned C 3 line','C 3 Si F est.',r'C 3 \ill{}','C 3 Si F est.','Beneath the corollary the zigzag cancellation crosses C 3, Si, F and est; each survives.','c3',kind='readable ink left as \\ill{}',marked='yes')
p.change('instruction between axioms',r'\unsure{intervertir}','uncertain intersection','intervertir','The rotated word has the sequence inter-vert-ir; its final tall t and short ir are visible.','inter',dc=True,kind='misread word',marked='yes')
p.change('two marginal instruction arrows','one curved bidirectional path','described as arrows','two curved arrows directed upward and downward from the note','Two separate curved arms run from the note toward the upper and lower double rules; both arrowheads are visible.','inter',dc=True,kind='drawing or diagram')
p.change('double rules beside axioms','comments only','described in notes','TikZ pairs of vertical strokes','Each axiom block has two long parallel emphasis strokes in its left margin.','c3',dc=True,kind='drawing or diagram')
p.change('lower axiom overwrite','C deleted unsure 3/2, unsure 2/3','C 3 (written on another numeral)','C deleted unsure 3/2, unsure 2/3','The lower numeral has both a descending 3-like curve and a broad 2-like foot. Their superposition remains marked.','renumber_bottom',confidence='medium',kind='misread symbol or index',marked='yes')
p.change('lower axiom abbreviation','tte','toute','tte','Two t uprights share a high crossbar and end in a small e; no ou is written.','tte',kind='abbreviation expanded or spelling modernised')
p.change('lower axiom predicate','est aussi une figure','est une figure','est aussi une figure','A distinct aussi follows est at the end of the line before une figure.','c3',kind='omission')
p.change('lower axiom emphasis',r'\uline{suffit}','suffit',r'\uline{suffit}','A separate horizontal line runs beneath suffit.','c3')
p.change('Sous-figures overwritten verb',r'\deleted{\unsure{signifie}} \unsure{implique}','implique',r'\deleted{\unsure{signifie}} implique','The crossed lower word begins sign- but its later letters are obscured; the live upper word ends in the clear plique run.','implique',dc=True,kind='deletion state (struck given live or live given struck)',confidence='medium')
p.change('cancelled si F at foot','si F',r'\ill{}','si F','The short si and hooked F are crossed immediately before ou.','bottom',kind='readable ink left as \\ill{}',marked='yes')
p.change('final phrase emphasis and abbreviation','underlined figure vide; existe tjrs','underlined figure vide existe toujours','underlined figure vide; existe tjrs','The rule ends under vide; existe and the compact tjrs lie beyond it.','bottom',kind='abbreviation expanded or spelling modernised')
for place,reading,why,crop in [
 ('deleted marginal portée','portée','Central letters share the cancellation stroke','margin_portee'),
 ('deleted marginal subscript',r'\mathrm{él}|\mathrm{el}','Small accent-like stroke is crossed','margin_portee'),
 ('deleted marginal symbol',r'\Sigma','Heavy retracing hides its exact outline','margin_portee'),
 ('marginal words after F','en tant|ou bien|comme','Several letter bodies coincide with cancellation','margin_workright'),
 ('marginal raised phrase','axiomatique des|par les axiomes des','The middle -tique-like ending is more legible than the opening','margin_work'),
 ('marginal end phrase','et tantôt','Crossing baselines obscure the word sequence','margin_workright'),
 ('marginal order sign',r"C'|\leq",'A diagonal crosses the curved sign and its raised stroke','margin_order'),
 ('cancelled formula first letter','X','Repeated zigzag obscures one arm','cancel_top'),
 ('cancelled formula second figure',"F'",'Prime and letter overlap a long cancellation','cancel_top'),
 ('cancelled formula inclusion',r'\supset|\subset','Direction cannot be securely separated from the zigzag','cancel_top'),
 ('first F cancelled subscript','X|x','Small crossed angular letter','cancel_top'),
 ('upper axiom prior numeral','2|3','Superposed numeral components','renumber_top'),
 ('upper axiom live numeral','3|2','Order of the superposed strokes remains uncertain','renumber_top'),
 ('upper axiom quantified letter','x|X','Case cannot be fixed from the small cross alone','c2'),
 ('lower axiom prior numeral','3|2','Superposed numeral components','renumber_bottom'),
 ('lower axiom live numeral','2|3','Order of the superposed strokes remains uncertain','renumber_bottom'),
 ('Sous-figures cancelled verb','signifie','The visible sign- is clear; later strokes are overwritten','implique')]:p.doubt(place,reading,why,crop)
p.inventory([
 ('margin note','upper and left oblique','Ainsi, M s’identifie…'),('deletion','inside upper margin','Donc on peut considérer…'),('deletion','inside upper margin, second part','Il y a une sorte de symétrie…'),('insertion','inside crossed oblique note','axiomatique des… (uncertain)'),
 ('deletion','top main baseline','Cela étant'),('deletion','top main formula','X ≪ Y … F_X'),('text','first paragraph','Si F est une figure…'),('deletion','subscript of first F','X/x'),('insertion','above first paragraph middle','i.e. Y ≤ X'),
 ('text','second paragraph','On dit que deux figures…'),('insertion','above figures','F,G'),('text','upper axiom','C 3/2 Pour que…'),('deletion','upper axiom label','old 2/3'),('drawing','beside upper axiom','double vertical rule'),('margin note','left of upper axiom','correspond à Fig 4'),
 ('text','corollary','Cor Pour que X,Y…'),('deletion','above corollary','En particulier si X'),('deletion','line below corollary','C 3 Si F est.'),('margin note','between axiom blocks','intervertir'),('drawing','around intervertir','upward and downward curved arrows'),
 ('text','lower axiom','C 2/3 Soit F…'),('deletion','lower axiom label','old 3/2'),('drawing','beside lower axiom','double vertical rule'),('text','last paragraph','Sous-figures…'),('deletion','first verb in last paragraph','signifie (uncertain)'),('deletion','after M=emptyset','cela implique que'),('insertion','above deleted clause','on aura F=emptyset'),('deletion','before ou','si F'),('margin note','bottom left oblique','Contrée vide si M=emptyset')])
p.notation('underlying set', 'M','Two plain tall uprights with a central valley; no calligraphic flourishes.')
p.notation('family of figures',r'\mathcal F','Curved head and hooked foot, unlike the straight-bar F used for an individual figure.')
p.r['abbreviations']=[dict(abbreviation='tte',expansion='toute',evidence='Two t uprights and final e in lower axiom'),dict(abbreviation='tjrs',expansion='toujours',evidence='Compact final group after existe'),dict(abbreviation='il f et s.',expansion='il faut et suffit',evidence='Corollary and upper axiom retain the written abbreviations')]
p.save()
