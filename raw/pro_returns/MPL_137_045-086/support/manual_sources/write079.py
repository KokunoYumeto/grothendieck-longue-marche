import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{79}
% archive foliation: 78
On est obligé de renforcer la propriété universelle de $\otimes$ et $\Gamma^p$, pour avoir les propriétés d'assoc. etc qu'on souhaite.

Soit $X\times Y\longrightarrow\deleted{\unsure{P|Q}}T$ un morphisme de bidegré $(1,1)$, alors pour tt $Z$, on a
\[
X\times Y\times Z\longrightarrow T\times Z
\]
d'où pour tt $M$
\[
P_{1,n}(T,Z;M)\longrightarrow P_{1,1,n}(X,Y,Z;M).
\]
On dit que $T$ est un produit \uline{tensoriel strict} de $X$ et $Y$ si l'hom précédent est un iso \deleted{\unsure{et alors $X\otimes Y=T$}} pour tt $n$ et tout $M$. Faisons $n=0$, $Z=0$, on trouve
\[
P_{1,\deleted{\unsure{0}}}(T,M)\simeq P_{1,1}(X,Y;M)
\]
donc $T$ est un produit tensoriel. C'est en exigeant qu'on a des $\otimes$ \uline{stricts} \deleted{que} \inserted{\unsure{définis}} \inserted{\unsure{pour des facteurs} (\deleted{\unsure{qui}} \unsure{il faut que la condition précédente} \unsure{soit prise} \unsure{pour un nombre} \unsure{quelconque de facteurs})} qu'on obtient une structure \unsure{sur $P_1$} ass. comm. compatible avec
\[
\deleted{\unsure{\operatorname{Hom}_{P_1}}}\quad P_1(X_1\otimes\cdots\otimes X_r;M)\simeq P_{1,\ldots,1}(X_1,\ldots,X_r;M).
\]
On sait qu'un objet unité (\unsure{sans recours à une} donnée d'associativité) si elle existe, est unique. \margin{?} Il faut examiner pourquoi ça devrait être $\Gamma^0(0)$.

Revenons aux $\Gamma^n$, soit $X=X_1\times\cdots\times X_r$, tel que $\Gamma^n(X)$ existe. Considérons les sous foncteurs $\unsure{P|\Gamma}_{\nu=(\nu_1,\ldots,\nu_r)}(X_1,\ldots,X_r;M)$ du foncteur \inserted{$P_1\longrightarrow(\operatorname{Ab})$} (can. représenté par $\Gamma^n(X)$), supposons qu'ils soient aussi cor (automatique si $P_1$ est karoubienne) alors $\Gamma^{\nu_1,\ldots,\nu_r}(X_1,\ldots,X_r)=\Gamma^\nu(X_1,\ldots,X_r)$ l'\deleted{\unsure{produit}} \inserted{\unsure{objet}} qui le représente. \deleted{\unsure{qui}}
(On va définir les \unsure{isom.} d'existence des $\Gamma^{\nu_i}X_i$ \deleted{\unsure{produits}} \inserted{et des} tensoriels, \unsure{ou} dans $\check P_1=\widehat{P_1^\circ}{}^\circ$ si'''
e=[('text','top','On est obligé de renforcer la propriété universelle'),('text','upper','Soit X×Y→T un morphisme de bidegré (1,1)'),('deletion','upper formula','P or Q'),('display','upper','X×Y×Z→T×Z'),('text','upper middle','d’où pour tt M'),('display','middle','P1,n(T,Z;M)→P1,1,n(X,Y,Z;M)'),('text','middle','On dit que T est un produit tensoriel strict'),('deletion','middle','et alors X⊗Y=T'),('text','middle','Faisons n=0 Z=0'),('display','middle','P1,(T,M)≃P1,1(X,Y;M)'),('deletion','middle subscript','0'),('text','middle','donc T est un produit tensoriel C’est en exigeant'),('deletion','middle','que'),('insertion','above middle','définis'),('insertion','crowded middle','pour des facteurs il faut que la condition précédente'),('deletion','crowded middle','qui'),('text','middle lower','qu’on obtient une structure ass comm compatible'),('display','lower middle','P1(X1⊗…⊗Xr;M)≃P1,…,1(X1,…,Xr;M)'),('deletion','before lower display','HomP1'),('text','lower','On sait qu’un objet unité'),('margin note','left lower','?'),('text','lower','Il faut examiner pourquoi ça devrait être Γ0(0)'),('text','lower','Revenons aux Γn soit X=X1×…×Xr'),('insertion','lower','P1→(Ab)'),('text','bottom','supposons qu’ils soient aussi cor automatique si P1 est karoubienne'),('deletion','bottom','produit'),('insertion','bottom','objet'),('deletion','bottom right','qui'),('text','bottom','On va définir les isom d’existence'),('deletion','bottom','produits'),('insertion','bottom left','et des')]
save(79,text,e)
