import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{75}
% archive foliation: 74
\uline{Catégories} \uline{hypopolynomiales}.

Une \uline{catégorie polynomiale} est une catégorie $P$, munie d'une sous-catégorie (pas pleine en général) $P_1$, avec les axiomes suivants
\margin{Notation $P(X,Y)$ pour $\operatorname{Hom}_P(X,Y)$.}

a) $P$ admet des produits finis, \deleted{et l'objet final.}

b) $\operatorname{Ob}P_1=\operatorname{Ob}P$, \deleted{\unsure{le produit et pour deux objets} dans $P_1$, leur produit dans $P$ est un produit dans $P_1$ (i.e. si $X,Y,Z\in\operatorname{Ob}P_1$ \unsure{une} \inserted{\unsure{$X\times Y\in\operatorname{Ob}P_1$}} \unsure{flèche} $Z\longrightarrow X\times Y$ de $P$ est de $P_1$ \inserted{(i.e. si $X,Y,Z\in\operatorname{Ob}P_1$ une $P$-flèche)} \unsure{$u=(u_1,u_2):X\longrightarrow Y\times Z$ est dans $P_1$ ssi}}
(donc $P_1$ est décrite par un ens $\operatorname{Fl}_1\subset\operatorname{Fl}(P)=\operatorname{Fl}$ contenant les identités, et stable par composition.) On veut de plus que \deleted{$\operatorname{Fl}_1$ \unsure{contienne les iso, et que}} pour $X,Y\in\operatorname{Ob}P$, leur produit $X\times Y$ soit un produit de $P_1$ (i.e. une flèche $u=(u_1,u_2):Z\longrightarrow X\times Y$ est ``de degré $1$'' ssi ses composantes $X,Y$ le sont), \inserted{enfin si $0$ est l'objet final, tt $X\longrightarrow0$ est de degré $1$ (donc $0$ objet final de $P_1$)}.

c) $P_1$ est une catégorie additive.

Cela implique que \deleted{pour tt objet l'on a un hom de monoïdes
\diagram{\begin{tikzcd}
\mathbf Z \arrow[r] & \operatorname{End}(\operatorname{id}P_1) & \operatorname{End}(\operatorname{id}P) \arrow[l]
\end{tikzcd}}
\unsure{qui pour tt} $\unsure{n}\in\unsure{\mathbf Z}$, $X,Y\in\operatorname{Ob}P_1$, \unsure{$n\cdot X$} \inserted{i.e. pour tt $X$}}
les $\operatorname{Hom}_P(X,Y)$ sont des groupes abéliens (car les objets \deleted{$Y$} \inserted{de $P$} sont des objets groupes abéliens de $P$), dépendant fonctoriellt de $X$, mais pas de $Y$ (i.e. on a
\[
\boxed{(f+g)\circ h=f\unsure{\circ}h+g\circ h}
\]
mais \deleted{\unsure{on a en général}} \inserted{on n'a pas} \unsure{la formule}
\[
f\circ(g+h)\ne f\circ g+f\circ h\qquad !
\]
Il en résulte aussi que $\mathbf Z^\times$ opère sur $P$ i.e. on a un homomorphisme multiplicatif
\diagram{\begin{tikzcd}
\mathbf Z^\times \arrow[r] & \operatorname{End}(P_1) & \operatorname{End}(P) \arrow[l,no head]
\end{tikzcd}}
qui à $n\in\mathbf Z$ et $X\in\operatorname{Ob}P_1=\operatorname{Ob}P$ associe $n\operatorname{id}_X$.
Ainsi $\mathbf Z$ opère dans \deleted{\unsure{$\operatorname{Hom}$}} $P(X,Y)$ par
\[
\mu_n(f)=f\circ(n\operatorname{id}_Y)
\]'''
e=[('text','heading','Catégories hypopolynomiales'),('text','top','Une catégorie polynomiale est une catégorie P'),('margin note','upper right','Notation P(X,Y) pour HomP(X,Y)'),('text','upper','a) P admet des produits finis'),('deletion','upper','et l’objet final'),('text','upper','b) ObP1=ObP'),('deletion','upper middle','le produit et pour deux objets dans P1'),('insertion','within cancelled block','X×Y∈ObP1'),('insertion','within cancelled block','i.e. si X,Y,Z∈ObP1 une P-flèche'),('text','middle','donc P1 est décrite par un ens Fl1'),('deletion','middle','Fl1 contienne les iso et que'),('text','middle','pour X,Y∈ObP leur produit X×Y'),('insertion','middle','enfin si 0 est l’objet final'),('text','middle','c) P1 est une catégorie additive'),('text','lower middle','Cela implique que'),('deletion','lower middle','pour tt objet l’on a un hom de monoïdes'),('diagram','cancelled lower middle','Z→End(id P1)←End(id P)'),('insertion','cancelled lower middle','i.e. pour tt X'),('text','lower','les HomP(X,Y) sont des groupes abéliens'),('deletion','lower','Y'),('insertion','lower right','de P'),('display','lower','(f+g)∘h=fh+g∘h'),('deletion','lower','on a en général'),('insertion','lower','on n’a pas'),('display','lower','f∘(g+h)≠f∘g+f∘h'),('text','bottom','Il en résulte aussi que Z× opère sur P'),('diagram','bottom','Z×→End(P1)–End(P)'),('text','bottom','qui à n∈Z et X∈ObP1=ObP'),('text','bottom','Ainsi Z opère dans P(X,Y)'),('deletion','bottom','Hom'),('display','bottom','μn(f)=f∘(n idY)')]
save(75,text,e)
