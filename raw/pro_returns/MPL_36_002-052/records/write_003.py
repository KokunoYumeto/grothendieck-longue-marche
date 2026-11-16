from save_page import save
tex=r'''
\cotefile{36}
\scanpage{3}
\mspage{1}

\uline{Remarques.\qquad SGA 7 $\boxed{\mathrm{IX}}$}

0.

i).\quad Dire que $\ell$ est un nombre premier à $p$ (pour que $\ell\,6$ soit OK p.e.)

Pourquoi $S$ \unsure{Limélien|hensélien} ?
\margin{$\ell\,7$\quad ii) $\ell\,3$}

$0.1,\ \ell\,9$ : pourquoi seulement à isogénie près ? (si $\ell\ne p$ : sinon ce ne veut rien dire)

$\ell\,14$ : il semble clair\qquad est un peu optimiste.

ii).\quad $\ell\,14$\quad français :\qquad et qui\qquad ($\,;\,$ il\quad ?)

iii).\quad
\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=3pt] (t) {$\ell\,6$};\draw[rotate=28] (0,0) ellipse (0.55 and 0.34);\end{tikzpicture}}
une référence ou définition pour réduction semi-stable d'une courbe (seule la terminologie de ``réduction stable'' se trouve dans [3])

iv)\quad $\ell\,12$\quad orthographe ?\qquad \unsure{système}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=3pt] (t) {$\ell\,15$};\draw[rotate=20] (0,0) ellipse (0.62 and 0.38);\end{tikzpicture}}
vider la Rmq sur les $H^i$ (qui n'est ni
\figure{\begin{tikzpicture}[baseline=(t.base)]\node[anchor=west,inner sep=0pt] (t) at (0,0) {lié à la \inserted{?}monodromie};\draw (1.05,0.08) ellipse (1.20 and 0.31);\end{tikzpicture}}, ni fondé sur des théorèmes)

\figure{\begin{tikzpicture}\draw (0,0)--(12,0);\draw (0,-0.08)--(12,-0.08);\draw (0,-0.16)--(12,-0.16);\end{tikzpicture}}

1.

\uline{p 0.}\quad titre :\qquad $\ell'$ (minuscule)

$(1.0)\ \ell\,5$\qquad donc\qquad ?

\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=3pt] (t) {$\ell\,7$};\draw[rotate=20] (0,0) ellipse (0.45 and 0.32);\end{tikzpicture}}
à quel concept se rapporte ``lequel''.

\rule{\linewidth}{0.3pt}

\uline{p.1}\quad $\ell\,12$\quad français : choisie\quad ; ``qui est'' tend à faire croire qu'on impose une condition supplémentaire

$\ell\,16$\quad $=B$ donc le symbole est \unsure{malheureux};\quad $=A'_K$ de toute façon.

\rule{\linewidth}{0.3pt}

p2\quad $\ell\,2$\quad pourquoi
\figure{\begin{tikzpicture}[baseline=(t.base)]\node[anchor=west,inner sep=0pt] (t) at (0,0) {Groupe};\draw (0.13,0.02) ellipse (0.18 and 0.25);\end{tikzpicture}}
\quad -- épimorphisme n'est pas la définition d'isogénie --

$\ell\,15$\quad -- supprimer séparé type fini au bénéfice du seul quasi projectif.

-- que $A\mathbin{\underset{S}{\times}}\operatorname{Spec}(K)\xrightarrow{\sim}A_K$ est une trivialité

\margin{2}
'''
e=[
('text','upper right','1'),('text','top centre','Remarques. SGA 7 IX'),('text','upper left','0.'),
('text','upper body i','Dire que ell est un nombre premier à p'),('text','upper body i, next line','Pourquoi S Limélien ?'),('margin note','under parenthesis, upper right','ell 7; ii) ell 3'),
('text','upper body, 0.1 l9','pourquoi seulement à isogénie près ?'),('text','upper body, l14','il semble clair est un peu optimiste'),
('text','upper middle ii','français : et qui (; il ?)'),('drawing','middle left iii, circled','ell 6'),('text','middle iii','une référence ou définition'),
('text','middle iv l12','orthographe ? système'),('drawing','middle iv l15, circled','ell 15'),('text','middle iv l15','vider la Rmq sur les H^i'),('drawing','middle right, oval around phrase','lié à la ?monodromie'),('insertion','inside oval before monodromie','?'),
('drawing','horizontal divider below upper notes','three parallel horizontal strokes'),('text','lower section heading','1.'),('text','lower p0 title','titre : ell prime (minuscule)'),('text','lower (1.0) l5','donc ?'),('drawing','lower left circled reference','ell 7'),('text','lower l7','à quel concept se rapporte lequel'),
('text','lower p1 l12','français : choisie ; qui est'),('text','lower p1 l16','=B donc le symbole est malheureux'),('text','bottom p2 l2','pourquoi Groupe - épimorphisme'),('drawing','bottom p2 l2, circled initial','G'),('text','bottom p2 l15','supprimer séparé type fini'),('display','bottom final line','A x_S Spec(K) -> A_K'),('margin note','bottom left pencil','2')]
d=[{'line':'i), second line','reading':'Limélien','alternatives':'hensélien','confidence':'low'}, {'line':'iv), l12','reading':'système','alternatives':'systême (accent shape)','confidence':'medium'},{'line':'p.1, l16','reading':'malheureux','alternatives':'compressed ending','confidence':'medium'}]
save(3,tex,e,d,'Editorial questions: why assume S henselian (reading uncertain); why only up to isogeny when ell != p; “il semble clair” judged “un peu optimiste”; request for reference/definition of semi-stable reduction; remove a remark on H^i as unrelated to monodromy and unsupported by theorems; quasi-projective in place of separated finite type. Title: Remarques. SGA 7 IX. Manuscript page 1; lower pencil 2.')
