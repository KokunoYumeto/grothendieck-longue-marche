from save_page import save
text=r'''
\scanpage{29}
% archive foliation: 28
\uline{NB} Il semble \uline{faux} que $(\mathrm{Cat})\longrightarrow\overline{\mathrm{Cat}}$ commute aux sommes infinies --- Il suffit de prendre \deleted{de} \unsure{une} \unsure{foule|famille}
\diagram{\begin{tikzcd}[column sep=large]
\begin{gathered}f_n\\g_n\end{gathered} & X_n\arrow[r,shift left=.5ex]\arrow[r,shift right=.5ex]&Y
\end{tikzcd}}
$(n\in\mathbb N)$ telles que $f_n\underset{\unsure{h}}\sim g_n$, mais qu'il faut une suite d'au moins $n$ homotopies él. pour les joindre (prendre p.ex. $X_n=\Delta_0$, $f_n,g_n$ définis par des pts de $Y$, prendre
\[
Y=I_\infty=(
\]
\diagram{\begin{tikzcd}[column sep=small]
{}\arrow[r]\arrow[rr,phantom,"\underbrace{\hspace{1.35cm}}"'] & {} & {}\arrow[l]\arrow[r]\arrow[rr,phantom,"\underbrace{\hspace{1.35cm}}"'] & {} & {}\arrow[l] & \cdots
\end{tikzcd}}
somme amalgamée d'une infinité de copies de $X_n$, \deleted{Mais} \deleted{\unsure{je soup}} la somme $\coprod X_n$ \uline{n'est pas} une somme dans $\overline{\mathrm{Cat}}$, car Je soupçonne pourtant que dans $\mathrm{Hot}(\underline W)$, les sommes quelconques existent et que $\mathrm{Cat}\longrightarrow\mathrm{Hot}(\underline W)$ y commute??

\margin{\unsure{Jobs au Trave|Jobs au Travail}}
'''
elements=[
('text','top','NB Il semble faux'),
('deletion','upper','de'),
('diagram','upper middle','f_n,g_n: X_n ⇒ Y; n in N'),
('text','middle','telles que f_n ~ g_n'),
('display','middle','X_n = Delta_0'),
('text','middle lower','f_n,g_n définis par des pts'),
('display','lower middle','Y = I_infinity = ('),
('diagram','lower middle','right left right left arrows, two underbraces, dots'),
('text','lower','somme amalgamée d’une infinité'),
('deletion','lower','Mais'),
('deletion','lower','je soup'),
('text','lower to foot','la somme coproduct X_n n’est pas ... Je soupçonne pourtant'),
('margin note','foot left inverted pencil','Jobs au Trave'),
]
save(29,text,'text',elements,'This NB contrasts the homotopy quotient with Hot(W), and ends with an explicit double question mark about arbitrary sums. The faint inverted pencil words, the noun preceding the parallel pair, and cancelled words after Mais are especially uncertain. The targets and the stated copies de X_n are retained from the ink.')
