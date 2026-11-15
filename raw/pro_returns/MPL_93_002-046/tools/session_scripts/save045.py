import sys
sys.path.insert(0,'MPL_93_002-046_work/tools')
from save_page import save_page
save_page(45,r"""
\scanpage{45}
\[
\mathbb D^*(A)_{S'}=\deleted{R^1f}\underline{\mathrm H}^1_{\mathrm{DR}}(A'/S')\quad\deleted{\unsure{*}}.
\]
On notera que d'après un théorème connu (cf. livre de Mumford Geometric Invariant theory) il existe toujours un $A'$ pour $S$ affine; le fait que \deleted{\unsure{A}}\inserted{$\mathrm H^1(A'/S')$} ne dépende, à isomorphisme près, pas du prolongement choisi de $A$, peut être considéré ici comme conséquence du tapis de la cohomologie cristalline.

En fait, utilisant la filtration de \deleted{De Rham}\inserted{Hodge} sur la cohomologie de De Rham, on trouve une filtration sur $\mathbb D^*(A)_{\unsure{S|S'}}$, savoir
\[
0\longrightarrow R^0f_*(\underline\Omega^1_{A/S})\longrightarrow
\underline{\mathrm H}^1_{\mathrm{DR}}(A/S)\longrightarrow R^1f_*(\underline{\mathrm O}_S)\longrightarrow0,
\]
qu'on peut interpréter comme
\diagram{\begin{tikzcd}[column sep=small]
(**) & 0\arrow[r] & \underline t_A^\vee\arrow[r]\arrow[d,equal] & \mathbb D^*(A)_S\arrow[r] & \underline t_{A^*}\arrow[r] & 0 & \unsure{-}.\\
&&\underline\omega_A
\end{tikzcd}}

Le foncteur $(*)$ et la suite exacte $(**)$ sont fonctoriels en $A$ et \unsure{compatibles} avec image inverse. On peut \deleted{envisager} considérer que le foncteur $(*)$ se factorise en
\[
\mathbb D^*:\text{Schémab}(S)\longrightarrow\mathrm{Crisloclib}_{\mathrm{nilp}}\mathrm{fil}(S)
\]
vers les cristaux en modules localement libres ``filtrés''(en deux crans localement libres). Utilisant cette factorisation, on trouve que pour un objet $S'$ du site cristallin nilpotent de $S$, la donnée d'un prolongement de $A$ en un schéma \inserted{abélien} $A'$ sur $S'$ revient à la donnée d'un prolongement de la filtration canonique $(**)$ de $D^*(A)_S$ en une filtration (à quotients localement libres) de $D^*(A)_{S'}$. Plus précisément, on a le

\uline{Théorème de déformation pour les schémas abéliens}. Soient $S$ un schéma, $S'$ un voisinage à puissances div. loc. nilp. de $S$, alors le foncteur naturel
\diagram{\begin{tikzcd}[column sep=small]
\text{Schémab}(S')\arrow[r] & \begin{gathered}
\text{catégorie des couples }(A,\deleted{\unsure{\Phi}}\,\unsure{\mathrm{Fil}}^1)\text{ d'un schéma abélien}\\
A\text{ sur }S\text{ et d'un sous-module localement facteur direct}\\
\mathrm{Fil}^1\ \inserted{\text{de }\mathbb D^*(A)_{S'}}\text{ prolongeant }\mathrm{Fil}^1\mathbb D^*(A)_S\simeq\underline\omega_A
\end{gathered}
\end{tikzcd}}
est une équivalence de catégories.

\inserted{b)} On peut donner une deuxième interprétation du foncteur $\unsure{\mathbb D|D}^*$ sur les
\margin{44}
""",'typed',[
('display','top','D*(A)_Sprime = H1_DR(Aprime/Sprime)'),
('deletion','top display, after equal','R1 f'),
('deletion','top display, before period','*'),
('text','upper','On notera que d’après un théorème connu'),
('deletion','upper, after le fait que','A'),
('insertion','upper right','H1(Aprime/Sprime)'),
('text','upper middle','En fait, utilisant la filtration'),
('deletion','after filtration de','De Rham'),
('insertion','above deletion','Hodge'),
('display','middle','0 to R0 f*(Omega1) to H1_DR to R1 f*(O_S) to 0'),
('text','middle','qu’on peut interpréter comme'),
('diagram','middle','(**) 0 to t_A dual = omega_A to D* to t_Astar to 0; final dash'),
('text','middle','Le foncteur (*) et la suite exacte (**)'),
('deletion','middle, after On peut','envisager'),
('display','middle','D*: Schémab(S) to Crisloclib_nilp fil(S)'),
('text','lower middle','vers les cristaux en modules'),
('insertion','after schéma','abélien'),
('text','lower','Théorème de déformation pour les schémas abéliens'),
('diagram','lower','Schémab(Sprime) to category of pairs (A,Fil1)'),
('deletion','target, before Fil1','Phi'),
('insertion','target, before prolongeant','de D*(A)_Sprime'),
('text','lower','est une équivalence de catégories'),
('insertion','bottom left','b)'),
('text','bottom','On peut donner une deuxième interprétation'),
('margin note','bottom left','44')
],[
('top formula, canceled final sign','*','','low','The typed star-like mark has been crossed through.'),
('first paragraph, canceled subject','A','','low','Typed x marks and the insertion leader obscure the old subject.'),
('filtration paragraph, evaluation subscript','S','Sprime','medium','The punctuation to the right is probably the paragraph comma; the index has been retraced.'),
('exact-sequence diagram, after final zero','-','','low','A pale horizontal stroke has no visible arrowhead and is kept as a dash.'),
('paragraph after diagram','compatibles','','medium','Overtyping at the clipped right edge affects the last letters before the line break.'),
('deformation theorem, canceled symbol before Fil1',r'\Phi','F','low','A heavily blackened, canceled character remains; its rounded central part suggests Phi.'),
('deformation theorem, Fil1','Fil','','medium','The first letter has been overtyped.'),
('last line, functor',r'\mathbb D','D','medium','The D is retraced and doubled, unlike the plain D in part of the preceding paragraph.')
])
