from record_page import save
save(15,217,'manuscript',r'''
\mspage{216}
Lien avec la variété des modules pour des
motifs polarisés rigidifiés : si \deleted{\unsure{le}} $M$ est
une telle variété modulaire, alors
un morphisme $X\mathrel{\text{---}}M$ est déterminé
quand on connaît sa valeur \uline{en un point},
plus l'application $\pi_1(X)\mathrel{\text{---}}\pi_1(M)$ \ldots

C'est une propriété intrinsèque importante de
ces $M$, et une propriété de cette
nature mérite d'être étudiée pour ses
propres mérites \ldots Peut-être peuvent elles
\unsure{ttes} être \deleted{caractérisées}\inserted{interprétées} comme des \deleted{schémas}\inserted{variétés}
modulaires pour certains types de
motifs.

\figure{\begin{tikzpicture}\draw (0,0)--(3,0);\end{tikzpicture}}

Introduire la notion de schéma \inserted{\unsure{motiviquement}} pointé
\inserted{\figure{\begin{tikzpicture}\node[draw,ellipse,text width=3cm,align=center] {(à val. dans un anneau $h$)};\end{tikzpicture}}}, et
morphismes de tels, qui définissent des
morphismes correspondants pour les
$G(X,\xi)\mathrel{\text{---}}G(Y,\eta)$, donc pour
\diagram{\begin{tikzcd}[column sep=large]
G(X,\xi)(h)=\pi_1(X,\xi)\arrow[r,no head]&G(Y,\eta)(h)=\pi_1(Y,\eta).
\end{tikzcd}}
''',[
('text','upper','Lien avec la variété des modules pour des motifs polarisés rigidifiés'),
('text','middle','C’est une propriété intrinsèque importante de ces M'),
('drawing','middle separator','single horizontal rule'),
('text','lower','Introduire la notion de schéma motiviquement pointé'),
('diagram','bottom','G(X,xi)(h)=pi_1(X,xi) linked to G(Y,eta)(h)=pi_1(Y,eta)'),
('text','bottom left','216')], 'Arrowless horizontal relation strokes retained; actual trailing ellipses transcribed.')
