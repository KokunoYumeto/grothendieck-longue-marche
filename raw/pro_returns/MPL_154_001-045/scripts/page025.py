from workflow import save_page
tex=r'''\scanpage{25}
\mspage{13}
\margin{24}

Il ne semble pas que la structure de graphe orienté cellularisé pondéré de $\Gamma^*(\underline\Sigma)$ permette de distinguer, parmi les \deleted{sommets} arêtes issues d'un sommet $D$ i.e. les sommets de $\operatorname{Pol}^*(D)$, celles et ceux qui correspondent à des triangles de ps. spécialisation (parmi les \deleted{\unsure{paires de sommets}} \inserted{sommets incidents} à des arêtes \deleted{\unsure{de poids}} de $\operatorname{Pol}^*(D)$ de poids nul, dont \deleted{\unsure{l'antipodique est un sommet}} l'un au moins soit sommet de générisation).

\margin{mais si ! cf ci-contre !}

Cette distinction peut se déduire si on dispose des applications de spécialisation \deleted{\unsure{et des}} $\operatorname{Pol}^*(D)\longrightarrow\operatorname{Pol}^*(D')$ : les sommets de ps. spécialisation sont distingués, parmi les précédents, comme \deleted{aux} les ``spécialisés'' des sommets de spécialisation véritables.

La prochaine question est donc si les applications de spécialisation
\[
\operatorname{Pol}^*(D)\longrightarrow\operatorname{Pol}^*(D')
\]
sont déductibles des structures précédentes. \uline{Mais bien sûr}, via l'\deleted{effet} isom correspondant sur les polygônes déployés, car il suffit de

\unsure{a)} savoir \unsure{qu'ils sont} de $=$ ordre (\unsure{calculable|découle})

b) de savoir \deleted{l'effet} du morphisme sur l'ens des deux orientations, ce qui est connu, et

c) de savoir l'image d'un sommet particulier \inserted{$(D,a)$} de $\widehat{\operatorname{Pol}}^*(D)$, qui est à savoir l'antipodique, dans $\widehat{\operatorname{Pol}}(D')$, du sommet $(D',a)$ !

En fait, chaque fois qu'on a une 2-carte \inserted{(avec bouts isolés i.e. arêtes libres)} dont les \deleted{\unsure{deux}} (vrais) sommets sont d'ordre $\unsure{2|\ge2}$, et dont les arêtes et coins sont pondérés [avec pondérations des arêtes $\ge0$], \deleted{\unsure{et où}} et la pondération totale de chaque sommet \deleted{est} (somme des pondérations des \deleted{\unsure{inc}} \inserted{arcs} et coins incidents) est cte, on trouve des isom de transport entre les polygônes locaux déployés, qui forment donc un syst. local sur la surface sous-jacente à la carte !
'''
e=[('text','left upper','Il ne semble pas que la structure'),('deletion','left upper','sommets'),('text','left upper middle','triangles de ps. spécialisation'),('deletion','left middle','paires de sommets; de poids; l’antipodique est un sommet'),('insertion','left middle','sommets incidents'),('margin note','gutter upper','mais si ! cf ci-contre !'),('text','left middle','Cette distinction peut se déduire'),('deletion','left middle','et des; aux'),('display','left middle','Pol star(D) → Pol star(D prime)'),('text','left lower middle','La prochaine question est donc si'),('display','left lower','Pol star(D) → Pol star(D prime)'),('text','left lower','Mais bien sûr; polygônes déployés'),('deletion','left lower','effet'),('text','left bottom','a) savoir qu’ils sont de = ordre'),('text','right upper','b) de savoir du morphisme sur l’ens'),('deletion','right upper','l’effet'),('text','right upper middle','c) de savoir l’image d’un sommet'),('insertion','right upper middle','(D,a)'),('display','right upper middle','Pol hat star(D); Pol hat(D prime); (D prime,a)'),('text','right middle','En fait, chaque fois qu’on a une 2-carte'),('insertion','right middle','avec bouts isolés i.e. arêtes libres'),('deletion','right middle','deux; et où'),('display','right middle','ordre 2; poids ≥0'),('text','right lower','pondération totale; syst. local'),('deletion','right lower','est; inc'),('insertion','right lower','arcs')]
d=[('left parenthesis cancellations','paires de sommets; de poids; l’antipodique est un sommet','Crossing strokes obscure several syllables','low'),('bottom left a clause','a) savoir qu’ils sont; calculable / découle','Abbreviated clause at page edge over show-through; first enumerator uncertain','low'),('right local-system assertion','ordre 2 / ≥2','The 2 is clear; a possible inequality before it is not distinct; no mathematical correction supplied','low'),('right inserted/cancelled words','deux; et où; inc','Short heavily overwritten cancellations','low')]
obs='Self-correction within page: initial “Il ne semble pas...” about intrinsic distinction is marginally rebutted “mais si ! cf ci-contre !”; later “Mais bien sûr” asserts specialization transport follows from deployed polygon order, orientation and one specified vertex. General assertion that weighted 2-carte with constant total weight gives local transport and a local system on underlying surface. Degree condition is a reading question (2 versus ≥2) and must not be silently repaired. This is a potentially substantial unproved local/global compatibility claim.'
save_page(25,tex,e,d,obs,sheet_kind='reused_typed')
