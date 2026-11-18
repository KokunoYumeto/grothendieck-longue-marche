from save_page import save_page

save_page(96, r'''
\scanpage{96}
\mspage{5}
% archive foliation: 95
\margin{on ait $n\gamma=\sum_0^{\unsure{r}}c_i\beta_i$}

On utilise maintenant \unsure{la théorie} de Kummer pour $\mathcal{X}/D$ pour trouver un \unsure{revêtement} de $\mathcal{X}/D_0$ qui ait comme groupe \uline{\unsure{d'inertie}} \unsure{de Galois} $J_0\inserted{\simeq\unsure{\mu_t^\infty}}$ \unsure{son} groupe d'inertie en $X_0$ .....

\margin{$\unsure{\beta^0}=n\gamma+\sum_1^r c_i\unsure{\beta^i}$\par $\unsure{\partial\simeq K^{\mathrm{ab}}}$}

\diagram{\begin{tikzcd}[column sep=small]
\pi_2^t(X_0/D'_0,\bar\xi_0) \arrow[r] \arrow[r,shift right=4ex,draw,-{Bar},start anchor=south,end anchor=south] &
\mu_{X_0,t}^{\infty}(\bar\xi_0) \arrow[r] &
\pi_1^t(\mathcal{X}/D,\bar\xi_1) \arrow[r] &
\pi_1^t(X_0/D'_0,\bar\xi_0) \arrow[r] \arrow[ll,bend right=60,start anchor=north,end anchor=north] & 0
\end{tikzcd}}

$\pi_1^t(\mathcal{X}/D,\bar\xi_1)$ comme extension de $\pi_1^t(X_0/D'_0,\bar\xi_0)$ est connu \unsure{entièrement} en termes de $X_0/D'_0$ et de la classe $\alpha\in H^2(X_0\deleted{-\unsure{D_0}},\mu_{X_0,\mathrm{tame}}^\infty)$ [self-intersection de $X_0$ dans $\mathcal{X}$] ....

\uline{Exemple I} $X_0$ courbe algébrique\inserted{lisse} sur $k$ alg. clos.

Alors $\pi_2^t(X_0-D'_0)=0$ sauf si $X_0\simeq\mathbf{P}^1_k$\inserted{, $D'_0=\varnothing$}, en quel cas $\pi_2^t(X_0,\bar\xi_0)\simeq\mu_{X_0,t}^{\infty}(\bar\xi_0)$. L'hom $\mathbf{Z}\longrightarrow\mu_t^{\deleted{\unsure{2}}\infty}$ dans ce dernier cas correspond \unsure{exactement} à la multiplication par $\unsure{n}$ (le degré). \deleted{\unsure{En tout cas}}

1°) \inserted{$\boxed{X_0-D'_0\ne\mathbf{P}^1_k}$}\deleted{\illegible{2}} $\pi_1^t(\mathcal{X}/D,\bar\xi_{\unsure{1}})$ est une extension \uline{triviale} de $\pi_1^t(X_0-D_0,\bar\xi_0)$ par $\mu_t^\infty(\bar\xi_0)$.
''', [
('margin note','top edge above opening paragraph','on ait n gamma = sum c_i beta_i'),
('text','upper, five lines','On utilise maintenant la théorie de Kummer'),
('insertion','upper, beside J_0','simeq mu_t^infty'),
('margin note','upper-right beside exact sequence','beta^0 = n gamma + sum c_i beta^i; partial simeq K^ab'),
('diagram','upper-middle, exact sequence with curved arrow and lower bracket','pi_2^t; mu^infty; pi_1^t; pi_1^t; 0'),
('text','middle, interpretation paragraph','pi_1^t comme extension'),
('deletion','middle, argument of H^2','-D_0'),
('text','lower-middle, example heading and hypothesis','Exemple I X_0 courbe algébrique'),
('insertion','above algébrique / sur','lisse'),
('text','lower, second homotopy group and map','Alors pi_2^t = 0 sauf si'),
('insertion','above exceptional case after P^1_k','D_0 prime = emptyset'),
('deletion','lower, superscript of mu','2'),
('deletion','lower-right at end of paragraph','En tout cas'),
('text','bottom, item 1','pi_1^t est une extension triviale'),
('insertion','bottom-left, boxed condition','X_0-D_0 prime neq P^1_k'),
('deletion','bottom-left, beneath boxed condition','two cancelled words')
], [
('opening paragraph','la théorie; revêtement','le théorème; very rapid pen','medium'),
('opening paragraph, fourth line','groupe d\u0027inertie de Galois; son','Second phrase particularly compressed','low'),
('insertion beside J_0','mu_t^infty','Terminal index / flourish is uncertain','low'),
('right margin','beta^0; beta^i; partial simeq K^ab','Right edge is cut; superscripts unclear','low'),
('exact sequence and later occurrences','calligraphic X; xi-bar','Script X and angular xi retained consistently','medium'),
('H^2 argument, deletion','-D_0','Overwritten superscript or prime after D_0','low'),
('lower paragraph','exactement; n','compressed word after correspond; coefficient may be another letter','low'),
('lower right deletion','En tout cas','Ends are crossed out','low'),
('bottom-left deletion','illegible, estimated two words','Heavy overstriking remains unreadable at enlarged view','low'),
('last formula','xi-bar_1; X_0-D_0','Subscript overwritten; D_0 has no clearly visible prime','medium')
], [
'Exact homotopy sequence for tame fundamental groups and a central roots-of-unity term; class alpha in H^2 described by self-intersection of X_0 in script X.',
'Exemple I treats a smooth algebraic curve over an algebraically closed field, with the P^1 and empty-boundary exception; the last item claims a trivial extension outside the displayed exceptional case. Check what assumptions from missing preceding leaves are needed.'
])
