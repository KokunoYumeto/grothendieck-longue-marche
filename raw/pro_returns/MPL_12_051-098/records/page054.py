from save_page import save_page
save_page(54,r'''\scanpage{54}
% archive foliation: 53
D'autre part, si $E\in\mathrm{Ob}\,M^{\deleted{\unsure{+}}}(X)$, \deleted{\unsure{simple}}, on trouve
\[
\mathrm{cl}(E)\in M^+(X)\Longleftrightarrow
\begin{gathered}
\forall x\text{ pt fermé de }X,\text{ le polynôme}\\
\text{caractéristique }\deleted{\text{de Frobenius}}\\
\mathrm{Frob}^{-1}_x\text{ dans }T_\ell(E)(x)\text{ est}\\
\text{à coefficients }\uline{\text{entiers}}\\
[\text{i.e. les valeurs propres de}\\
\text{Frobenius sont des}\\
\uline{\text{entiers}}\text{ algébriques}]
\end{gathered}
\]
\margin{``Conjectures de Tate''}

Par ailleurs, pour \deleted{\unsure{se limiter}, pour $\unsure{E\in}M_\alpha(X)$} $E$ ``homogène'' de degré $\alpha$, pour examiner si $E\in\mathrm{Ob}\,D_i(M(X))$, où $i\geq0$ \deleted{\unsure{on peut, par}} on note
\[
\deleted{\mathrm{cl}(E)\unsure{\in\Sigma_i}}
\qquad\deleted{\unsure{\xi_\alpha|\zeta_\alpha}\in D_\alpha M(X)}
\]
\inserted{
\[
\begin{gathered}
E\in\mathrm{Ob}\,D_iM(X)\text{ i.e.}\\
\mathrm{cl}(E)\in D_iM(X)
\end{gathered}
\Longleftrightarrow\text{ Si}
\]
}
\margin{$\Downarrow$}

[1°) $i=0$. Alors
\[
E\in\mathrm{Ob}\,D_0(M(X))\Longleftrightarrow
\begin{gathered}
E\text{ est de degré }\uline{\text{pair}}\ \alpha=2\beta\\
\text{et }E\unsure{\xi|\zeta}^{-\beta}=F\quad(\text{qui est de}\\
\text{degré }0)\text{ est }\in\mathrm{Ob}\,M^+(X)
\end{gathered}
\]
i.e. si $\rho_i(x)$ sont les valeurs propres de $\mathrm{Frob}^{-1}_x$ dans $T_\ell(\unsure{M|E}(x))$, alors les $\rho_i(x)/N(x)^\beta$ sont des entiers Algébriques]
\margin{N.B. Ce sont des racines de l'unité [\unsure{donc pr. du th. II !}]}

2°) $i\geq1$. Alors il existe une plus grande puissance $\unsure{\xi|\zeta}^{\beta}$ de $\unsure{\xi|\zeta}$ telle que $E\unsure{\xi|\zeta}^{-\beta}\inserted{=E(+\beta)}\deleted{\unsure{\in\mathrm{Ob}\,M}}$ soit de degré $i-1$ ou $i$ (suivant la parité de $\alpha$)]. On veut que \deleted{\unsure{tout}} $E(\unsure{+\beta})$ soit $\in\mathrm{Ob}\,M^+(X)$, i.e. les $\rho_i(x)/N(x)^\beta$ doivent être des entiers Alg.
''',[
('top','text',"D'autre part, si E in Ob M(X), on trouve"),
('upper-right','display','cl(E) in M^+(X) iff inverse Frobenius characteristic polynomial has integer coefficients'),
('middle','text','Par ailleurs, pour E homogène de degré alpha'),
('middle-left','display','cancelled cl(E); cancelled xi_alpha in D_alpha M(X)'),
('lower-middle','text','[1°) i=0. Alors'),
('lower-middle','display','E in Ob D_0(M(X)) iff degree alpha=2 beta and E xi^{-beta} effective'),
('lower-right','text','i.e. si rho_i(x) sont les valeurs propres'),
('bottom','text','2°) i >= 1; plus grande puissance; entiers Alg.')],remarks='Whole page and both halves checked; four enlarged crops used for overwritten middle, header, NB and last paragraph. NB remainder is especially uncertain; no inferred mathematical repair.')
