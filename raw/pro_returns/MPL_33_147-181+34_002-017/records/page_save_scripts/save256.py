import sys
sys.path.insert(0,'MPL_57_226-270/scripts')
from record_page import save_page
save_page(256,r'''\scanpage{256}
diagramme de suites exactes
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
H^i(X_0,\mathbb Z)\arrow[r]\arrow[d,"u^i"]&R^if_*(\underline O_X)_y\arrow[r]\arrow[d,"v^i"]&R^if_*(\underline O_X^*)_y\arrow[r,dash,"\delta^i"]\arrow[d,"w^i"]&H^{i+1}(X_0,\mathbb Z)\arrow[r,"\alpha^{i+1}"]\arrow[d,"u^{i+1}"]&R^{i+1}f_*(\underline O_X)_y\arrow[d,"v^{i+1}"]\\
H^i(X_0,\mathbb Z)\arrow[r,dash]\arrow[d]&R^if_*(\underline O_X)_y^\wedge\arrow[r,dash]\arrow[d]&\varprojlim H^i(X_n,O_{X_n}^{\unsure{\wedge|*}})\arrow[r,dash,"\widehat\delta^i"]\arrow[d]&H^{i+1}(X_0,\mathbb Z)\arrow[r,"\widehat\alpha^{i+1}"]\arrow[d]&R^{i+1}f_*(\underline O_X)_y^\wedge\\
\deleted{H^i(X_{\unsure{n|0}},\mathbb Z)}\arrow[r]&\deleted{H^i(X_n,O_{X_n})_{\unsure{n\geq0}}}\arrow[r]&\deleted{H^i(X_n,O_{X_n}^*)_{\unsure{n\geq0}}}\arrow[r]&\deleted{H^{i+1}(X_0,\mathbb Z)}\arrow[r]&\deleted{H^{i+1}(X_n,O_{X_n})_{\unsure{n\geq0}}}
\end{tikzcd}}
\margin{(D)}
On en conclut, grâce au lemme des 5

\inserted{a) $R^if_*(\underline O_X^{\unsure{\wedge|*}})_y\longrightarrow\varprojlim_n H^i(X_n,O_{X_n}^{\unsure{\wedge|*}})$ est \uline{injectif}, et les deux ont \unsure{$=$ images} dans $H^i(X_n,O_{X_n}^*)$}

\uline{Corollaire} 1.6. \inserted{b) Pour} \deleted{Supposons} que $R^if_*(\underline O_X)_y$ soit artinien i.e. $y$ un pt isolé de $\operatorname{Supp}R^if_*(\underline O_X)$.
\deleted{Alors} \inserted{\unsure{de}: $\varinjlim_{U\ni y}H^i(f^{-1}(U),\underline O_U^*)=$}
\[
R^if_*(\underline O_X^{\unsure{\wedge|*}})\longrightarrow\varprojlim H^i(X_n,O_{X_n}^{\unsure{\wedge|*}})\quad\text{soit}
\]
un \uline{isomorphisme}.

\margin{\deleted{\unsure{Comment la définition projective}\illegible{1}}}
\margin{\unsure{Autre résultat}: pour $n$ grand \unsure{Néron Séveri} $(X_n)$ est constant, car isom. à $\operatorname{Ker}(H^{\unsure{2|i+1}}(X_0,\mathbb Z)\longrightarrow R^{\unsure{2|i+1}}f_*(\underline O_X)_y)$}

\deleted{\uline{\unsure{Preuve du fait}}}. \inserted{a)} Le lemme des 5 montre également que
\[
R^if_*(\underline O_X^{\unsure{\wedge|*}})\longrightarrow\varprojlim H^i(X_n,O_{X_n}^{\unsure{\wedge|*}})
\]
est toujours un monomorphisme.

\margin{Comme $v^{i+1}$ est inj., $\operatorname{Ker}\alpha^{i+1}=\operatorname{Ker}\widehat\alpha^{i+1}$, donc $\operatorname{Im}\delta^i=\operatorname{Im}\widehat\delta^i$ donc pour}
\deleted{$\forall\xi\in\varprojlim H^i(X_n,O_{X_n}^{\unsure{\wedge|*}})$, il existe un}
\deleted{\unsure{donc le système} syst. proj. $(H^i(X_n,O_{X_n}^*))_n$ satisfait M.L.A.R.}

\margin{$\unsure{\eta}\in(R^if_*\underline O_X)_y$ ayant même image dans $H^{i+1}(X_0,\mathbb Z)$ (\unsure{condition}\illegible{1}). D'où \unsure{$\xi-\eta$ est dans} $\varprojlim H^i(X_n,\underline O_{X_n})$. \uuline{Or} $R^if_*\underline O_X\longrightarrow H^i(X_n,\underline O_{X_n})$ est surjectif \unsure{en passant}, ce qui prouve, O.K.}

Le cas le plus important pour nous est celui où $i=1$, qui donne le

\uline{Th.} $1.\deleted{\unsure{8}}\inserted{7}$. Soit $f:X\longrightarrow Y$ une application propre d'espaces analytiques sur $\mathbb C$, $y\in Y$, $X_n=X\mathbin{\mathrm{x}}_Y Y_n$, \inserted{$Y_n=\operatorname{Specan}O_y/\mathfrak m_y^{n+1}$,} \deleted{Alors} posons \inserted{$\operatorname{Pic}(X_y)=\varinjlim_{U\ni y}\operatorname{Pic}(f^{-1}(U))$} $=R^1f_*(\underline O_X^{\unsure{\wedge|*}})_y$, \deleted{Alors l'homomorphisme l'hom}
\[
\operatorname{Pic}(\widehat X_y)=\varprojlim\operatorname{Pic}(X_n).
\]
\margin{255}
''','text',[
('text','top','diagramme de suites exactes'),('diagram','top','three rows, comparison of exponential sequences'),('deletion','diagram third row','H^i(X_n,Z) → H^i(X_n,O_Xn)'),('margin note','upper left','(D)'),('text','upper','On en conclut, grâce au lemme des 5'),('insertion','upper','a) R^if_*(O_X^*)_y → lim'),('text','upper middle','Corollaire 1.6.'),('insertion','upper middle','b) Pour'),('deletion','upper middle','Supposons'),('text','upper middle','que R^if_*(O_X)_y soit artinien'),('deletion','middle left','Alors'),('insertion','middle left','de: lim_U H^i(f^-1(U),O_U^*)='),('display','middle','R^if_*(O_X^*) → lim H^i'),('text','middle','un isomorphisme'),('margin note','far left vertical','cancelled Comment la définition projective'),('deletion','far left vertical','Comment la définition projective'),('margin note','left oblique','Autre résultat; Néron Séveri'),('deletion','lower middle','Preuve du fait'),('insertion','lower middle','a)'),('text','lower middle','Le lemme des 5 montre également'),('display','lower middle','R^if_*(O_X^*) → lim H^i'),('margin note','right middle','Comme v^{i+1} est inj.'),('deletion','lower middle','∀ ξ ∈ lim H^i, il existe un'),('deletion','lower middle','syst. proj. satisfies M.L.A.R.'),('margin note','lower left enclosed','η∈(R^if_*O_X)_y ayant même image'),('text','lower','Le cas le plus important'),('text','bottom','Th. 1.7. Soit f:X→Y'),('deletion','theorem number','8'),('insertion','theorem number','7'),('insertion','bottom left','Y_n=Specan O_y/m_y^{n+1}'),('deletion','bottom','Alors'),('insertion','bottom right','Pic(X_y)=lim_U Pic(f^-1(U))'),('deletion','bottom','Alors l’homomorphisme l’hom'),('display','bottom','Pic(Xhat_y)=lim Pic(X_n)'),('margin note','bottom left','255')
],[('diagram, cancelled third row','X_n; n≥0','X_0','low'),('all unit exponents shaped as caret','∧','*','low'),('a), last clause','= images','','medium'),('insertion beside corollary display','de:','','low'),('left cancelled marginal line','Comment la définition projective; one unreadable word','','low'),('left oblique marginal note','Autre résultat; Néron Séveri (X_n); exponents 2','i+1','low'),('cancelled heading below corollary','Preuve du fait','','low'),('cancelled middle text','donc le système','','low'),('lower left enclosed note','η; condition; ξ−η est dans; en passant','','low'),('theorem number','7 over deleted 8','','medium'),('last deleted words','Alors l’homomorphisme l’hom','','low')])
