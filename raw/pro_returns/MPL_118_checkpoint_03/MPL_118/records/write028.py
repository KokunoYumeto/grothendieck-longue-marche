from save_page import save
text=r'''
\scanpage{28}
% archive foliation: 27
\uline{Lemme} \unsure{Soit} $(M,h)$ structure homotopique par intervalles (homotopy interval structure), avec $M$ stable par sommes [finies], et les sommes [finies] étant universelles. Alors $M\longrightarrow W_h^{-1}M$ commute aux sommes finies.

\margin{\uline{NB} $M$ stable par produits finis}

Cela revient à ceci: pour
\diagram{\begin{tikzcd}[column sep=large]
\begin{gathered}f=(f_j)_{j\in J}:\\g=(g_j)_{j\in J}\end{gathered}
& \underbrace{\coprod_J X_j}_{X}\arrow[r,shift left=.5ex,"f"]\arrow[r,shift right=.5ex,"g"'] &Y
\end{tikzcd}}
\[
f\underset h\sim g\quad\unsure{\text{ssi}|\text{sss}}\quad f_j\underset h\sim g_j\quad\forall j\in J.
\]
\uline{Dém} $\Rightarrow$ trivial, pour prouver $\Leftarrow$ on note qu'il existe \uline{un $\unsure{=}$ intervalle} $I$ tel que $f_j\underset{h_I}\sim g_j$ \deleted{$\unsure{(I\subset)}$} (car $J$ est fini), \deleted{on prend} comme
\[
I\times X=\coprod_J I\times X_j
\]
on trouve homotopie composée
\deleted{$\unsure{I\times}$}
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
I_N\times X\arrow[r]&X\\
\cup&\cup\\
I_N\times X_j\arrow[r]&X_j
\end{tikzcd}}
(avec $N$ assez grand pour convenir pour tous les $j$\ldots). On gagne!
'''
elements=[
('text','top','Lemme Soit (M,h) structure homotopique'),
('margin note','upper left','NB M stable par produits finis'),
('display','upper middle','M → W_h^-1 M'),
('text','middle','Cela revient à ceci: pour'),
('diagram','middle','f=(f_j), g=(g_j), coproduct X_j ⇒ Y'),
('display','middle','f ~_h g ssi f_j ~_h g_j'),
('text','lower middle','Dém ⇒ trivial'),
('deletion','lower middle after g_j','(I subset)'),
('deletion','lower middle','on prend'),
('display','lower','I × X = coproduct I × X_j'),
('text','lower','on trouve homotopie composée'),
('deletion','above bottom diagram','I ×'),
('diagram','near foot','I_N × X → X; I_N × X_j → X_j'),
('text','foot','avec N assez grand ... On gagne!'),
]
save(28,text,'text',elements,'The printed-looking equal sign before intervalle and cancelled parenthesis beside the homotopy are uncertain. The upper and lower targets of the final diagram are read X and X_j, without correcting them to Y. Bracketed finies is retained. This page has been read, not mathematically checked.')
