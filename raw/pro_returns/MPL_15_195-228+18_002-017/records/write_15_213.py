from record_page import save
save(15,213,'manuscript',r'''
\mspage{212}
\uline{Groupe fondamental motivique discret}

Soit $\xi\in\mathbb T(\mathbb Z)$, on pose
\[
\pi_1(X,\xi)=\operatorname{Aut}(\xi).
\qquad =\unsure{G_\xi(\mathbb Z)|G_\xi(\mathbb Z)'}
\]
\uline{N.B.} En vertu de Borel\inserted{-\unsure{Harish}}, il n'y a qu'un
nb fini de $\xi\in T_\alpha(\mathbb Z)$ possibles, pour $\alpha$
donné. D'où un nb fini de \uline{groupes
fondamentaux discrets}. Sont-ils tous
\unsure{isom's} à des \deleted{\illegible{1}} près ??

$\xi\in T_\alpha(k)$, $k$ un anneau

$M$ motif $\in\operatorname{Ob}\mathbb M_\alpha$

$M_\xi$ fibre en $\xi$,\qquad $M_\xi=\xi(M)$
\[
\pi_1(X,\xi)_{\unsure{\alpha}}=\operatorname{Aut}(\xi),\qquad
G(X,\xi)=\underline{\operatorname{Aut}}(\xi)
\]
\deleted{$\unsure{G_\xi}$}
\[
\pi_1(X,\xi)_\alpha\simeq G(X,\xi)(k)
\]
Comparaison avec $\pi_1(\unsure{X^t_v|X^\tau_v},\bar a)$ quand $\xi$ \unsure{provient d'une}
\uline{fibre} en $a$ \ldots

\uline{Ex}. $X$ connexe sur $\mathbb C$, $\xi$ défini par un pt de
$X$ à valeurs dans $C$. Le foncteur $\xi_C\deleted{\unsure{C}}$ a une
structure \uline{filtrée}. $\xi$ considéré comme
foncteur à valeurs dans les modules
sous $\pi_1(X,\xi)$ munis d'une \uline{structure de
Hodge} est \unsure{plt} fidèle \ldots
''',[
('text','top','Groupe fondamental motivique discret'),
('text','upper','Soit xi dans T(Z), on pose'),
('display','upper right','pi_1(X,xi)=Aut(xi)=G_xi(Z)'),
('text','upper-middle','N.B. En vertu de Borel-Harish'),
('text','middle','xi dans T_alpha(k), k un anneau; M motif; M_xi fibre'),
('display','lower-middle','pi_1(X,xi)_alpha=Aut(xi); G(X,xi)=Aut underlined'),
('display','lower-middle','pi_1(X,xi)_alpha isomorphic G(X,xi)(k)'),
('text','lower','Comparaison avec pi_1'),
('text','bottom','Ex. X connexe sur C; structure filtrée; structure de Hodge'),
('text','bottom left','212')], 'Two explicit source ellipses retained. Severely cancelled prose word is marked illegible after enlarged inspection.')
