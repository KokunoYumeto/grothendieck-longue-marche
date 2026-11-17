import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\cotefile{137}
\scanpage{45}
% archive foliation: 44
produits $\prod$ aussi --- ce qui est \unsure{automatique} si le $K^\bullet$ est nul sauf en nb fini\unsure{...}]

\deleted{Comme le \unsure{foncteur} $\operatorname{Hom}_{\unsure{k}}^\bullet(K_{\unsure{i}}^\bullet,C^\bullet)$
$(\unsure{B}^\circ\longrightarrow(Ab))$ \unsure{définit} un \unsure{fonct.} additif des
$K$, \unsure{il est représentable par} $K^\bullet$.}

\unsure{Définissons} un hom dans $\widehat{\unsure{B}}$
\[
(1)\qquad F(x)\unsure{\longrightarrow|=}\operatorname{Hom}_{\unsure{k}}^\bullet(\unsure{K}(x),C_F^\bullet)
=\operatorname{Hom}_{\unsure{k}}^\bullet(\unsure{K}(x),F(C^\bullet))
\]
i.e. un hom dans $\widehat{\unsure{B}}^\bullet$
\[
(1')\qquad \underbrace{F(x)\otimes\unsure{k}^\bullet(x)}_{\unsure{resp.}}\longrightarrow C^\bullet=F(C^\bullet)
\]
\margin{\unsure{repr. en les} $\unsure{x}$\unsure{,} \unsure{d'où}\unsure{\simeq} \unsure{l'isom. de V.f.}}
\[
(1'')\qquad
\underset{\substack{\rotatebox{90}{$\in$}\\\widehat{\unsure{B}}}}{F(x)}
\otimes\underset{\substack{\rotatebox{90}{$\in$}\\Ab_{\unsure{k}}^\bullet}}{\operatorname{Hom}(x,C^\bullet)}
\xrightarrow[\mathrm{can}]{}F(C^\bullet)
\]
qui provient de l'hom fonctoriel en $x\in\operatorname{Ob}\unsure{K}$
\[
F(x)\otimes\operatorname{Hom}(x,C)\longrightarrow F(C).
\]
L'hom (1''), donc (1) est fonctoriel en $K$,
et les deux membres sont des foncteurs
additifs en $K$, pour prouver que \unsure{(1)}
est un iso, $\forall F$, il suffit de le voir
pour $K$ de la forme $\unsure{k}C^\bullet$. Or on a
alors
\[
(2)\qquad F(C^\bullet)\longrightarrow\operatorname{Hom}_{K}^\bullet
(C_{\unsure{\bullet}}^\bullet,\deleted{\unsure{C}}F(C^\bullet))
\]
Or on a aussi un
\[
\operatorname{Hom}_{\unsure{k}}^\bullet
\left(C_{\unsure{\bullet}}^\bullet,\underset{\substack{\rotatebox{90}{$\in$}\\Ab^\bullet}}{P^\bullet}\right)
\simeq C^\bullet
\]
et on voit de suite que moyennant cet is.,
(2) va à l'identité, qfd.
'''
save(45,text,[
('text','top, continuation','produits'),
('deletion','upper quarter','Comme le foncteur'),
('text','upper middle','Définissons un hom'),
('display','upper middle','(1) F(x)'),
('text','below (1)','i.e. un hom'),
('display','middle','(1′) F(x) tensor k'),
('margin note','left of (1′′)','repr. en les'),
('display','middle','(1′′) F(x) tensor Hom'),
('text','below (1′′)','qui provient'),
('display','below middle','F(x) tensor Hom(x,C)'),
('text','lower middle','L’hom (1′′)'),
('display','lower quarter','(2) F(C)'),
('deletion','inside (2)','C overwritten before F'),
('text','below (2)','Or on a aussi un'),
('display','bottom','Hom(C,P) ≃ C'),
('text','bottom conclusion','et on voit de suite')])
