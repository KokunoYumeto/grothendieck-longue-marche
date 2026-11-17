import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{86}
% archive foliation: 85
Il y a une telle structure canonique dans le cas de l'exemple.
Ou aussi : quand peut-on enrichir la composition des morphismes de $P$
\[\deleted{\operatorname{Hom}_P}P(X,Y)\times P(Y,Z)\mathbin{-}P(X,Z)\]
($k$-linéaire en le deuxième argument) en une application linéaire
\[P(Y,Z)\longrightarrow(\text{Appl. }k\text{-polynomiales})(P(X,Y),P(X,Z))\]
(ceci aussi est acquis dans l'exemple \unsure{principal} envisagé). La construction doit se ramener pour l'essentiel à définir de telles structures suppl. sur les foncteurs $\Gamma^n$, i.e. pour tt $X,Y$
\[f\longmapsto\Gamma^p(f):\operatorname{Hom}_1(X,Y)\mathbin{-}\operatorname{Hom}_1(\Gamma^pX,\Gamma^pY)\]
doit être défini comme ``application pol. de degré $p$'' entre les $k$-modules $\operatorname{Hom}_1(X,Y)$ et $\operatorname{Hom}_1(\Gamma^{\unsure{r|p}}X,\Gamma^{\unsure{r|p}}Y)$, et non seulement comme application ensembliste.
'''
e=[('text','top','Il y a une telle structure canonique'),('text','upper','Ou aussi quand peut-on enrichir'),('display','upper','P(X,Y) times P(Y,Z) - P(X,Z)'),('deletion','upper display beginning','Hom_P'),('text','upper-middle','k-linéaire en le deuxième argument'),('display','middle','P(Y,Z) -> (Appl. k-polynomiales)(P(X,Y),P(X,Z))'),('text','middle','ceci aussi est acquis'),('display','lower','f maps Gamma^p(f): Hom1(X,Y) - Hom1(Gamma^pX,Gamma^pY)'),('text','lower','doit être défini comme application pol.')]
save(86,text,e)
