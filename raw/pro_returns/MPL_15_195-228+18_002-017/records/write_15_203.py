from record_page import save
save(15,203,'text',r"""
En plus de la \uline{structure entière} sur le \deleted{\unsure{f}}\inserted{foncteur} de Hodge-DeRham, relatif à un pt complexe, il faut \uline{ajouter} la \uline{décomposition en types}, également de nature transcendante (elle est compatible avec la filtration canonique). On peut aussi dire que cette dernière \deleted{\unsure{associée}} \inserted{\unsure{est déterminée via filtration}} par l'\uline{opération involutive} $\tau'$ \inserted{\unsure{$\tau$} $\frac12$ linéaire,} dans $\xi_{X,\infty}$, provenant de l'écriture
\[
\xi_{x,\infty}=\xi_{x,\mathbf R}\otimes_{\mathbf R}\mathbf C
\qquad\text{où}\qquad
\xi_{x,\mathbf R}\simeq\xi_{x,\mathbf Z}\otimes_{\mathbf Z}\mathbf R.
\]

Si $k(a)$ est réel, on a une autre application $\frac12$ linéaire involutive $\tau''$, provenant de
\[
\xi_{x,\infty}\simeq\xi_{a,\infty\,\mathbf R}\otimes_{\mathbf R}\mathbf C
\]
et $\tau$ sur $(\xi_{x,\mathbf Z})_{\mathbf C}$ n'est autre que $\tau'\tau''$
\[
\tau=\underbrace{\tau'}_{\substack{\frac12\text{ linéaire}\\\text{transcendant}}}\underbrace{\tau''}_{\substack{\frac12\text{ linéaire}\\\text{algébrique}}}=\tau''\tau'
\]
\margin{à vérifier}

La situation locale \inserted{(dans le cas réel)} est connue par la connaissance de $\xi_{\unsure{x},\infty}^{\tau''}=(\xi_{a,\infty})_{\mathbf R}$ \inserted{(Hodge-DeRham réel)}, muni de $\tau=\tau'$ (involution transcendante, qui est $\mathbf R$-linéaire sur ledit espace), ou \inserted{mieux par celle de $\tau=\tau''$ opérant sur $\xi_{x,\infty}^{\tau'}\simeq\xi_{x,\mathbf R}$,} \unsure{Ou idem} de $\tau$ sur $\xi_{a,\mathbf Z}$, d'où on déduit les
\[
\boxed{\tau\text{ sur }\xi_{a,l}}
\]
[or c'est là \inserted{l'opération de} l'\unsure{élémt} de $\pi_1(X)$, \uline{frobenius} en la place réelle -- !]
\margin{à vérifier}

\mspage{202}
""",[
('text','top','En plus de la structure entière'),
('display','upper middle','xi_x,infty = xi_x,R tensor C; xi_x,R isomorphic xi_x,Z tensor R'),
('text','middle','Si k(a) est réel'),
('display','middle','xi_x,infty isomorphic xi_a,infty R tensor C'),
('text','middle','et tau sur (xi_x,Z)_C'),
('display','lower middle','tau = tau prime tau double prime = tau double prime tau prime; attached labels'),
('text','lower','La situation locale'),
('display','bottom','boxed tau sur xi_a,l'),
('text','bottom','or c\'est là ... frobenius ... réelle'),
('text','bottom left','202')
], 'Whole and supplied halves compared; dense additions inspected in separate crops; both à vérifier notes retained.')
