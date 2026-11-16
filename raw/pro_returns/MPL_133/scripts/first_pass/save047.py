import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(47,r"""\scanpage{47}
\mspage{2}

Condition pour que $N'=\uline{\operatorname{Cent}}G$

\unsure{a|*}) Il faut que $N'\subset\uline{\operatorname{Cent}}G$, i.e. op. \inserted{$\theta'$} de $M'$ sur $N'$
triviale ($\Longrightarrow N'$ commutatif et $d'(N')\subset\uline{\operatorname{Cent}}(M')$)

b) D'ailleurs, l'image du centre de $G$ dans $K$ \inserted{$=G/\pi_1$} est
contenue dans $\uline{\operatorname{Cent}}(K)$ \inserted{$\supset N'/\pi_1$ i.e. son image dans $M$ contenue dans $\uline{\operatorname{Cent}}(K)/(N'/\pi_1)$}, et aussi dans
$\operatorname{Ker}(\theta:M\longrightarrow\uline{\operatorname{Aut}}_{\mathrm{gr}}(N))$. Soit
\[
\zeta=\deleted{\uline{\operatorname{Cent}}(M)}\inserted{\uline{\operatorname{Cent}}(K)/(N'/\pi_1)}\cap\operatorname{Ker}\theta
\]
et soit $\overline{N}'$ \deleted{\unsure{son}} l'image inverse dans $G$ \inserted{le ss-groupe invariant de $G$ \unsure{déf.}},
\inserted{$(N'\subset\uline{\operatorname{Cent}}(G)\subset\overline{N}')$}
qui est donc
une extension de $\zeta$ par $N'$. L'opération de
$G$ sur $\overline{N}'$, via $M$, par automorphismes, est triviale
sur $\unsure{N'}$ et sur $\zeta=\overline{N}'/N'$ \inserted{(car $\zeta\subset\uline{\operatorname{Cent}}(M)$)}, donc se définit par un
hom
\[
M\longrightarrow\uline{\operatorname{Hom}}_{\mathrm{gr}}(\zeta,N')
\]
prenant en fait ses valeurs dans $\uline{\operatorname{Hom}}_{\mathrm{gr}}(\zeta,\pi_1)$
\deleted{$\unsure{\operatorname{Hom}_{\mathrm{gr}}(M,\pi_1)}$}
(lequel, par construction de $\zeta$, est aussi trivial
sur $d(N)\subset M$ ($\zeta\subset\operatorname{Ker}\theta$). Donc l'hom
se factorise en
\[
\varphi_G:\pi_0\longrightarrow\uline{\operatorname{Hom}}_{\mathrm{gr}}(\zeta,\pi_1)
\qquad\deleted{\unsure{Z^1}}
\]
qui s'interprète \inserted{aussi} comme
\[
\psi_G:\zeta\longrightarrow\uline{\operatorname{Hom}}_{\mathrm{gr}}(\pi_0,\pi_1)
\qquad\deleted{\unsure{\operatorname{Hom}_{\mathrm{gr}}}}
\]
Soit $\zeta_G=\operatorname{Ker}\psi_G$, et $\overline{N}'_G$ l'image inverse de
$\zeta_G$ dans $G$, il est clair alors que
\[
\overline{N}'_G=\uline{\operatorname{Cent}}(G)
\]
donc $N'=\uline{\operatorname{Cent}}(G)$ équivaut à la condition
\[
\boxed{\zeta_G=\operatorname{Ker}\psi_G=1\quad\text{i.e. }\psi_G\text{ injectif}}
\]

Soit $G_1$ une deuxième sol. du Pb initial,
différant de $G$ par une extension \deleted{$\unsure{E}$} $E$ de $\pi_0$ par $\pi_1$
(op. triviale de $\pi_0$ sur $\pi_1$ i.e. extension centrale),

\margin{\uline{\unsure{donc plus}} :
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
\zeta=\operatorname{Ker}\theta\cap\operatorname{Cent}M\arrow[d]\\
Z^1(\pi_0,\pi_1)
\end{tikzcd}}
$M\simeq G/N'$\par
$\zeta\subset\unsure{\zeta'}=\operatorname{Im}\uline{\operatorname{Cent}}(K)$}
\mspage{46}
""",'text',[
('text','top title','Condition pour que N prime=CentG'),('text','upper third','a) Il faut que'),('insertion','above op.','theta prime'),('text','upper third','b) D’ailleurs'),('insertion','over K and after Cent(K)','=G/pi_1; superset N prime/pi_1'),('display','upper middle','zeta=Cent(M) intersection Ker theta'),('deletion','zeta definition','Cent(M)'),('insertion','above zeta definition','Cent(K)/(N prime/pi_1)'),('text','middle','et soit N bar prime'),('deletion','before image inverse','son'),('insertion','above image inverse','le ss-groupe invariant de G'),('insertion','right of image inverse','N prime subset Cent(G) subset N bar prime'),('text','middle','une extension de zeta'),('insertion','under quotient','car zeta subset Cent(M)'),('display','middle','M to Hom_gr(zeta,N prime)'),('text','middle lower','prenant en fait'),('deletion','right middle','Hom_gr(M,pi_1)'),('display','lower middle','phi_G; psi_G'),('deletion','right of phi and psi','Z^1; Hom_gr'),('text','lower third','Soit zeta_G=Ker psi_G'),('display','lower third','N bar prime_G=Cent(G)'),('display','boxed near bottom','zeta_G=Ker psi_G=1'),('text','bottom','Soit G_1 une deuxième sol.'),('deletion','before E at bottom','E'),('margin note','left oblique','donc plus; zeta; M=G/N prime'),('text','folios','2;46')],doubts=[('interlinear image inverse','le ss-groupe invariant de G déf.','Final two or three strokes overwritten; relation to l’image inverse is uncertain','low'),('left margin heading','donc plus','Oblique and abbreviated; possible autre reading','low')],observations='Centrality criterion expressed as injectivity of psi_G; comparison by an extension E begins at foot.')
