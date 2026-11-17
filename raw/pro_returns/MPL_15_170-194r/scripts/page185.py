from record_page import record

record(185, r'''\scanpage{185}

De plus, on a une structure \unsure{polarisée} \inserted{$\pi$} sur $G^0_{\mathbb R}$, qui est \deleted{\unsure{déf}} supposée définie par un hom
$\deleted{\unsure{\mu_{2\mathbb C}}}\quad i:\mu_{2\mathbb C}\unsure{-|\to}G^0_{\mathbb C}$
(comme on voit en envoyant un \unsure{tore} \inserted{point d'ordre 2} dedans). D'autre part, $G(s')_{\mathbb C}$ est muni de $i(s'):G_{m\mathbb C}\to G^{(s')}_{\mathbb C}$, et on obtient par conséquent
\diagram{\[
\begin{tikzcd}[column sep=large]
\unsure{v|v_q}(s')=u(s')_{\mathbb C}\circ(i(s')\mid\mu_2):\ \mu_{2\mathbb C} \arrow[r] & G^{\unsure{\xi}(s')}_{\mathbb C}
\end{tikzcd}
\]}

\deleted{D'autre part} Ceci posé, il faut que $\pi^{\unsure{\xi}(s')}$ (polarisation de $G^{\unsure{\xi}(s')}_{\mathbb R}$ déduite de $\pi$ sur $\mathbb C$ par transport) soit celle définie par les $\mu_{2\mathbb C}$.

Par conséquent, pour $s'$ \unsure{variable|variant} de façon que $\unsure{\xi}(s')$ soit constant, les polarisations \inserted{de $G^{\unsure{\xi}(s')}_{\mathbb R}$} associées aux différents $v(s')$ doivent être identiques -- ce qui donne une condition non tautologique sur la distribution des \deleted{\unsure{ces}} $u(s')$. [Noter cependant que l'ens des \deleted{classes de} polarisations d'un gpe réel \inserted{$H$}, définies en termes d'un hom $\mu_{\mathbb C}\to H_{\mathbb C}$, est \uline{fini}, [si $G$ est commutatif en tous cas !], donc la restriction n'est pas tellement draconienne.
\margin{? à vérifier}

Enfin, conformément aux conjectures de Tate \unsure{magnifiées}, La connaissance des $u(s')$ permet de retrouver la structure d'effectivité dans la catégorie

\margin{184}
''', [
('text','opening paragraph','De plus, on a une structure polarisée'),
('insertion','above opening line after polarisée','π'),
('deletion','second line before supposée','déf'),
('display','line 3','i: μ2C - G0C'),
('deletion','before i in line 3','μ2C'),
('insertion','parenthesis above dedans','point d’ordre 2'),
('text','parenthesis and D’autre part','comme on voit en envoyant'),
('display','inline in D’autre part paragraph','i(s’): GmC → G(s’)C'),
('diagram','v(s’) display','v(s’) = u(s’)C ∘ (i(s’)|μ2): μ2C → Gξ(s’)C'),
('deletion','before Ceci posé','D’autre part'),
('text','polarization compatibility paragraph','Ceci posé, il faut que'),
('text','following paragraph','Par conséquent, pour s’ variable'),
('insertion','after les polarisations','de Gξ(s’)R'),
('deletion','before u(s’)','ces'),
('text','bracketed qualification','Noter cependant que l’ens'),
('deletion','after l’ens des','classes de'),
('insertion','above gpe réel','H'),
('display','inline in bracketed qualification','μC → HC'),
('margin note','left opposite est fini','? à vérifier'),
('text','inner bracket','si G est commutatif en tous cas !'),
('text','end of bracketed qualification','donc la restriction n’est pas tellement draconienne'),
('text','last unfinished paragraph','Enfin, conformément aux conjectures de Tate'),
('margin note','bottom left pencil','184')
], sheet_kind='reused_typed', observations='''Whole image and both halves read, enlarged upper/middle/lower crops and the marginal question examined. The top-right π is an inserted name for the polarization, not a page number. Source has an outer opening square bracket before Noter and an inner bracket around si G ...; no closing outer bracket is visible and none is supplied. The margin explicitly reads ? à vérifier, attached to the assertion fini. The last homomorphism has μ_C with no clearly visible 2, unlike the earlier μ_2C; no 2 has been supplied there. The notation ξ/ζ is left uncertain consistently with 183. Handwriting is on the reverse of an unrelated typescript; mirrored print is show-through. The qualifying word after Tate is provisionally magnifiées, marked doubtful.''')
