from page_work import save_page
text=r'''\scanpage{126}
\mspage{78}
\margin{n$^\circ$ 239}
3. \uline{Faisceaux mous}.

Si X est un espace paracompact, $\mathcal F$ un faisceau de base X, Y une partie fermée de X, on a vu (th.1) que toute section de $\mathcal F$. au-dessus de Y se prolonge en une section au-dessus d'un \uline{voisinage} de Y, mais elle ne se prolonge pas nécessairement en une section au-dessus de X \uline{tout entier}.

Une raison suffisante est qu'il peut n'exister aucune section au-dessus de X tout entier (\S\ 1, exerc.1). Un autre exemple est le suivant : soient X un espace connexe séparé et paracompact, G un ensemble ayant au moins deux éléments distincts, $\mathcal F$ le faisceau constant $X\times G$, a et b deux points distincts de X, s une section au-dessus de $\{a,b\}$ telle que $s(a)=(a,\alpha)$, $s(b)=(b,\beta)$ avec $\alpha\neq\beta$ ; cette section ne peut être prolongée au-dessus de X tout entier (cf.\S\ 1, n$^\circ$ 2, \uline{Exemple}).

On va voir que, si X est paracompact, la possibilité de prolonger toute section au-dessus d'une partie fermée de X à X tout entier est une propriété \uline{locale} du faisceau $\mathcal F$.

DEFINITION 1. - \uline{Soit} X \uline{un espace localement paracompact}. \uline{On dit qu'un faisceau} $\mathcal F$ \uline{de base} X \uline{est mou s'il existe une base} $\phi$ \uline{de la topologie de} X, \uline{telle que pour tout} $U\in\phi$, $\overline U$ \uline{soit paracompact}, \uline{et, pour chaque} $U\in\phi$, \uline{un ensemble} $\psi(U)$ \uline{de parties fermées de} X \uline{contenues dans} U, \uline{satisfaisant aux conditions suivantes}. :

$(\mathrm{FM}_{\mathrm I})$ \uline{Pour tout} $U\in\phi$, \uline{toute partie fermée} M \uline{de} X, \uline{contenue dans} U, \uline{et tout voisinage} V \uline{de} M, \uline{il existe} $F\in\psi(U)$ \uline{telle que} $M\subset F\subset V$.

$(\mathrm{FM}_{\mathrm{II}})$ \uline{Quels que soient} $U\in\phi$, $F\in\psi(U)$ \uline{et la section} s \uline{de} $\mathcal F$ \uline{au-dessus de} F, \uline{il existe une section de} $\mathcal F$ \uline{au-dessus de} U \uline{prolongeant} s.
\mspage{125}
'''
save_page(126,text,[('text','top internal page number','78'),('margin note','upper right','n°239'),('text','upper heading','3. Faisceaux mous'),('text','upper paragraph','Si X est un espace paracompact F un faisceau'),('text','upper middle example','Une raison suffisante est qu’il peut n’exister aucune section'),('text','middle paragraph','On va voir que si X est paracompact'),('text','lower definition1','Soit X un espace localement paracompact'),('text','lower first condition','(FMI) Pour tout U in phi toute partie fermée M'),('text','bottom second condition','(FMII) Quels que soient U in phi F in psi(U)'),('text','original bottom left inverted page number','125')],sheet_kind='reused_typed',observations='Original whole, rotated whole, and both rotated supplied halves read. Typescript and handwritten math are clear. Underlining follows the separate printed-word spans, with math generally not underlined. The closure bar on U in Definition 1 is retained. The extra visible dot after the first paragraph F and the period followed by colon at the end of the definition are retained rather than editorially corrected.')
