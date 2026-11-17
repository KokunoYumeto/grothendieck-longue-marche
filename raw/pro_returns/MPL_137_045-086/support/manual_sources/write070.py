import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{70}
% archive foliation: 69
$i=0$ \unsure{seulmt}) $C^i\xrightarrow{d^i}C^{i+1}$ ait un Ker \deleted{\unsure{qui soit} tel que $Z^i\longrightarrow C^i$ est un $\Sigma$-mono (Ici, le $\Sigma$ dans $B$ est de la plus \unsure{mauvaise}, il n'y a \unsure{pas à prouver}]). Ceci dit, on se borne à de tels complexes, qui correspondent donc à des foncteurs \deleted{\unsure{de $B$}} $k$-addit. \inserted{($\Sigma$-ex. à g)} $P_0\longrightarrow B$ resp. $Q\unsure{\longrightarrow|{-}}B$.

\deleted{On se propose de \inserted{se} donner une structure multiplicative sur ceux-ci, ce qui nous oblige à donner de plus
\[
\deleted{F(\Psi^0)\otimes_B F(C^i)\longrightarrow F(\Psi^0*C^i)\quad\unsure{\text{et de plus}}}
\]
un hom de $B$, à foncteurs
\[
F(X)\otimes_B F(Y)\longrightarrow F(X*Y)
\]
sur $P_0\times P_0$ \inserted{$P$} resp $Q\times Q$. Or}

\unsure{Si notre classe $B$ est stable à} \unsure{un noyau}, alors on se ramène aux foncteurs $\Sigma$-ex. à g de $P$ dans $B$, en \deleted{prenant} \unsure{interprétant} ceux-ci comme des foncteurs $k$-additifs quelc. sur $K$ i.e. des $C^\bullet\in\operatorname{Ob}B^\bullet$. On peut l'expliciter ainsi: $\forall L\in P$ \inserted{($\in Q$, $\in P_0$)} \deleted{\unsure{on sait}} s'insère dans deux $\Sigma$-suites de $P$ ($Q,P_0$)
\[
\unsure{0}{-}L{-}I{-}L'{-}\unsure{0}
\]
\[
0{-}L'\longrightarrow J{-}L''\longrightarrow0
\]
avec $I,J\in K$, et par suite on'''
e=[('text','top','i=0 seulmt) Ci→Ci+1 ait un Ker'),('deletion','upper block','qui soit tel que Zi→Ci est un Σ-mono'),('text','upper middle','Ceci dit on se borne à de tels complexes'),('deletion','upper middle','de B'),('insertion','upper middle','(Σ-ex. à g)'),('deletion','middle large block','On se propose de se donner une structure multiplicative'),('insertion','cancelled block','se'),('display','cancelled middle','F(Ψ0)⊗B F(Ci)→F(Ψ0*Ci)'),('deletion','cancelled middle','F(Ψ0)⊗B F(Ci)→F(Ψ0*Ci) et de plus'),('text','cancelled middle','un hom de B à foncteurs'),('display','cancelled middle','F(X)⊗B F(Y)→F(X*Y)'),('insertion','cancelled block lower left','P'),('text','lower','Si notre classe B est stable à un noyau'),('deletion','lower','prenant'),('text','lower','On peut l’expliciter ainsi'),('insertion','lower','∈Q,∈P0'),('deletion','lower','on sait'),('display','bottom','0–L–I–L′–0'),('display','bottom','0–L′→J–L″→0'),('text','bottom','avec I,J∈K et par suite on')]
save(70,text,e)
