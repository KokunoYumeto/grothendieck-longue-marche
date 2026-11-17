from record_page import record
tex=r'''\scanpage{27}
% archive foliation: 26
\diagram{\begin{tikzcd}[column sep=large]
\operatorname{Hom}(\Psi^i_{\deleted{\unsure{*}}},\Phi(j,n))\arrow[r]&\operatorname{Hom}(\Psi^i,\Psi^j)\arrow[d,phantom,"=" description]\\
&0\text{ si }j\neq i
\end{tikzcd}}
\unsure{$\forall\alpha\in$}
donc si $j\neq i$, $\operatorname{Hom}(\Psi^i,\Phi(j,n))\xleftarrow{\sim}$
$\operatorname{Hom}(\Psi^i,\Psi^{j-1}\deleted{\unsure{\mathrm{can}}})$,
\deleted{donc}
qui est nul si
$i\neq j-1$ i.e. $j\neq i+1$; si $j=i+1$, on trouve $\simeq k$.
Pour $j=i$, la composée
$\Psi^i\xrightarrow{\alpha}\Phi(i,n)\xrightarrow{\mathrm{can}}\Psi^i$
est de la forme
$d\operatorname{id}_{\Psi^i}$, donc l'image
inverse de l'extension
\diagram{\begin{tikzcd}[column sep=large]
&&\Psi^i\arrow[d,"\alpha"']\arrow[dr]\\
0\arrow[r]&\Psi^{j-1}\arrow[r,dash]&\Phi(j,n)\arrow[r,dash]&\Psi^i\arrow[r,dash]&0
\end{tikzcd}}
$\Phi(i,n)$ est de classe $d e_{i,n}=dn e_i$,
qui est nulle, donc $dn e_i=0$, donc
$dn=0$, donc $d=0$, donc $\unsure{\alpha}$ se factorise
par $\Psi^i\longrightarrow\Psi^{i-1}$, donc est nul.
\deleted{Pour $j=i+1$, on a $\operatorname{Hom}($}
Donc
\deleted{$\unsure{\operatorname{Hom}(\Phi,\Psi)}$}
\[
\operatorname{Hom}(\Psi^i,\Phi(j,n))\simeq
\left\{\begin{array}{ll}
0&\text{si }j\neq i+1\\
k&\text{si }j=i+1\quad\text{(par l'hom can. }\Psi^i\longrightarrow\Phi(i+1,n)\text{)}
\end{array}\right.
\]
\par\bigskip\hrule\bigskip
Enfin on suppose
\[
\text{(d)}\qquad\begin{gathered}
\text{Tout objet de }C\text{ est somme}\\
\text{finie d'objets de la forme}\\
\Phi(i,n)\ \inserted{(i\geq1)}\text{ ou }\Psi^j\ (j\geq0)
\end{gathered}
\]
'''
record(27,tex,[('diagram','top','Hom(Ψ^i,Φ(j,n))→Hom(Ψ^i,Ψ^j)=0 si j≠i'),('deletion','first Ψ subscript','*'),('text','under top Hom','∀α∈'),('text','upper','donc si j≠i'),('display','upper','Hom(Ψ^i,Φ(j,n))←~Hom(Ψ^i,Ψ^(j−1))'),('deletion','after superscript','can'),('deletion','before qui est nul','donc'),('text','upper-middle','qui est nul si i≠j−1; j≠i+1; si j=i+1'),('text','middle','Pour j=i, composée; d id; image inverse extension'),('diagram','middle left','Ψ^i→Φ(j,n)→Ψ^i over extension'),('text','middle-lower','Φ(i,n) classe d e_i,n=dn e_i; dn=0; d=0; factorise'),('deletion','lower-middle line','Pour j=i+1 on a Hom('),('text','lower-middle','Donc'),('deletion','before final Hom','Hom(Φ,Ψ)'),('display','lower','Hom(Ψ^i,Φ(j,n)) cases 0 / k'),('text','below separator','Enfin on suppose'),('display','hypothesis d','Tout objet de C somme finie Φ(i,n) ou Ψ^j'),('insertion','hypothesis d above Φ','i≥1')],doubts=[('under top Hom','∀α∈','short isolated mathematical annotation; ending indistinct','low'),('upper cancelled word','can','small overwritten annotation after Ψ^(j−1)','low'),('middle diagram lower right','Ψ^i','j possible, although following case is j=i; no silent correction','medium'),('scalar','d','hand resembles δ; subsequent dn uses same scalar','medium'),('before se factorise','α','overwritten Greek symbol','low'),('second cancelled Hom','Hom(Φ,Ψ)','very heavily struck; arguments not securely readable','low'),('hypothesis d insertion','i≥1','small parenthetic condition above baseline','medium')])
