import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{76}
% archive foliation: 75
d) Il existe une décomposition de $\operatorname{Hom}_P(X,Y)$ en
\[
P(X,Y)=\bigoplus_{n\geq0}P_n(X,Y)
\]
telle que pour $f_n\in P_n(X,Y)$ et $\lambda\in\mathbf Z$, on ait
\[
f_n\circ(\lambda\operatorname{id}_X)=\lambda^n f_n.
\]
Plus généralement, si $X_1,\ldots,X_r,Y$ sont des objets de $P$, on a une décomposition
\[
(*)\quad P(\unsure{\prod_i}X_1\times\cdots\times X_r,Y)=\bigoplus_{n=(n_1,\ldots,n_r)\in\mathbf N^r}P_n(X_1,\ldots,X_r;Y)
\]
avec, pour $f\in P_{n_1,\ldots,n_r}(X_1,\ldots,X_r;Y)$ et $\lambda=(\lambda_i)_{i=1,\ldots,r}\in\mathbf Z^r$, on ait
\[
f\circ(\lambda_1\operatorname{id}_{X_1},\ldots,\lambda_r\operatorname{id}_{X_r})=\lambda_1^{n_1}\cdots\lambda_r^{n_r}f.
\]
\margin{\uline{Ex} si $P$ est un groupe annulé par $p$, alors l'op. de $\mathbf Z$ par $\lambda\longmapsto\lambda\operatorname{id}_P$ ou $\lambda\longmapsto\lambda^p\operatorname{id}_{\unsure{P|\mathbf Z}}$ est la \uline{même}, donc on peut \unsure{considérer} \unsure{comme étant} \unsure{de degré $1$, ou $p$ !}}

\uline{Remarque} Cette décomposition \inserted{\unsure{n'}}est \inserted{\unsure{pas}} unique, en \uline{raison de} canulars ``arithmétiques'' --- il le serait \deleted{\uline{\unsure{toujours}} Soit $P$ un groupe abélien, et
\[
u:(\mathbf Z^\times)^r\longrightarrow\operatorname{End}(P)
\]
un hom de monoïdes. \deleted{\unsure{Pour tt $n\in\mathbf N$, $\lambda\in\mathbf Z$}}
Supposons qu'il existe une décomposition en somme directe
\[
P=\sum_{n=(n_1,\ldots,n_r)\in\mathbf N^r}P_n
\]
telle que pour $f\in P_n$, \inserted{et $\lambda=(\lambda_1,\ldots,\lambda_r)\in\mathbf Z^r$,} on ait
\[
\unsure{\varphi_n}\ u(\lambda)\cdot f=\lambda_1^{n_1}\cdots\lambda_r^{n_r}f.
\]
Alors cette décomposition est unique, plus précisément on a pour tt $n\in\mathbf N^r$
\[
P_n=\{f\in P\mid u(\lambda)f=\lambda_1^{n_1}\cdots\lambda_r^{n_r}f\quad\forall\lambda\in\mathbf Z^r\}.
\]
Il suffit de voir que si $n'\ne n$ et si $g_{n'}\in P_{n'}$ est tel que
\[
u(\lambda)g_{n'}=\lambda_1^{n_1}\cdots\lambda_r^{n_r}g_{n'}\quad\forall\lambda\in\mathbf Z^r,
\]
alors $g_{n'}=0$. Or on aura aussi
\[
\unsure{\lambda_*}\ u(\lambda)g_{n'}=\lambda_1^{n_1'}\cdots\lambda_r^{n_r'}g_{n'}.
\]
}'''
e=[('text','top','d) Il existe une décomposition de HomP(X,Y)'),('display','top','P(X,Y)=⊕n≥0 Pn(X,Y)'),('text','upper','telle que pour fn∈Pn(X,Y) et λ∈Z'),('display','upper','fn∘(λ idX)=λn fn'),('text','upper middle','Plus généralement si X1,…,Xr,Y'),('display','middle','(*) P(∏i X1×…×Xr,Y)=⊕Pn(X1,…,Xr;Y)'),('text','middle','avec pour f∈Pn1,…,nr et λ'),('display','middle','f∘(λ1 idX1,…,λr idXr)=λ1n1…λrnr f'),('margin note','left vertical','Ex si P est un groupe annulé par p'),('text','middle','Remarque Cette décomposition est unique'),('insertion','above Remarque line','n’'),('insertion','above Remarque line','pas'),('deletion','lower entire argument','toujours Soit P un groupe abélien'),('display','cancelled lower','u:(Z×)r→End(P)'),('deletion','cancelled lower','Pour tt n∈N λ∈Z'),('text','cancelled lower','Supposons qu’il existe une décomposition en somme directe'),('display','cancelled lower','P=ΣPn'),('text','cancelled lower','telle que pour f∈Pn on ait'),('insertion','cancelled lower','et λ=(λ1,…,λr)∈Zr'),('display','cancelled lower','u(λ)f=λ1n1…λrnr f'),('text','cancelled lower','Alors cette décomposition est unique'),('display','cancelled lower','Pn={f∈P | u(λ)f=… ∀λ∈Zr}'),('text','cancelled bottom','Il suffit de voir que si n′≠n'),('display','cancelled bottom','u(λ)gn′=λ1n1…λrnr gn′'),('text','cancelled bottom','alors gn′=0 Or on aura aussi'),('display','cancelled bottom','u(λ)gn′=λ1n′1…λrn′r gn′')]
save(76,text,e)
