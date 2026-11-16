from record import draft

draft(97,r'''
\cotefile{84}
\scanpage{97}
\diagram{\begin{tikzcd}
0 \arrow[r,no head] & L \arrow[r,no head] \arrow[d,"-\mathrm{id}"'] & E \arrow[r,no head] \arrow[d,"g","?"'] & \underline{\mathcal O} \arrow[r] \arrow[d,"\mathrm{id}"] & 0\\
0 \arrow[r,no head] & L \arrow[r,no head] & \mathcal A\otimes L \arrow[r,"\varphi\otimes\mathrm{id}_L"] & \underline{\mathcal O} \arrow[r] & 0
\end{tikzcd}}
\margin{Attention au \unsure{signe}.}

Prouvons d'abord
\[
\varphi\otimes\mathrm{id}_L\bigl(\underbrace{g(x)}_{\mathcal A\otimes L=\operatorname{Hom}(E,L)}\bigr)=\psi(x)\qquad \forall x\in\Gamma(E).
\]
Cela signifie que $\forall x\in E$,
\[
g(x)|L=(u\mapsto\psi(x)u)
\]
\deleted{\illegible{1}} i.e.
\[
\begin{array}{c}
g(x)(u)=\psi(x)u\\[-2pt]
\Vert\\[-2pt]
\psi(x).u-\underbrace{\psi(u)}_{0}x
\end{array}
\qquad\text{pour tout }u\in\Gamma L\subset\Gamma E
\]
c'est OK.

Prouvons ensuite que pour $x\,\deleted{\unsure{x}}\in\Gamma L$, ---
$g(x):E\longrightarrow L$ est \uline{nul} sur $L$, et que \unsure{l'on a}
en \unsure{quo} induit $\lambda\mapsto-\lambda x$ de $\mathcal O$ sur $x$,
\margin{\unsure{signe}}
i.e.
\[
g(x)(y)=-\psi(y)x,
\]
mais c'est aussi OK.

Ceci vu, l'isom. d'ext. $g$ définit
\[
\operatorname{Quad}(E,L^{\otimes2})\simeq\operatorname{Quad}(\mathcal A,\mathcal O)
\]
\[
\deleted{\unsure{\operatorname{Quad}(E)}\otimes L^{\otimes2}\ \unsure{\simeq}\ \unsure{\mathcal A^{\otimes2}}}.
\]
\uline{dès que $\unsure{\varphi}$ est iso}, \uline{$N$} et \uline{$Q$ se correspondent}.
\margin{\unsure{lorsque} $E$ provient d'un \unsure{truc du type}, d'où $N$ sur $\mathcal A$, $Q$ sur $E$.}
Pour le prouver, \unsure{on} $E$ scindé en
\[
E\simeq L\oplus\underline{\mathcal O}.x_0
\]
d'où
\[
\mathcal A\simeq\underline{\mathcal O}\oplus L^\vee
\qquad\text{i.e. }\mathcal A\otimes L\simeq L\oplus\underbrace{L\otimes L^\vee}_{\underline{\mathcal O}_X}.
\]
\mspage{96}
''')
