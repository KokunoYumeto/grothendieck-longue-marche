from workflow import save_page
save_page(83,r'''\scanpage{83}
% archive foliation: 82
\deleted{$\unsure{X_0/S}$} d'une situation $X_0/I_0/\unsure{x_0|k_0}/k_0$
où $k_0$ est un sous-corps. [OPS \unsure{disons} que
$k$ est une clôture alg. de $k_0\ldots$].
Alors $\Gamma=\operatorname{Gal}(k/k_0)$ opère sur
$\Sigma^{\mathrm{ext}}$ par transport de structure, donc on a
une \deleted{\unsure{la}} opération aussi sur $P(X/I/k)$,
\deleted{donc}\inserted{ou encore} un hom
\[
\Gamma\longrightarrow{}^{P(X/I/k)}\widetilde\Gamma_\nu
\simeq\operatorname{Aut}(\Sigma^{\mathrm{ext}})
\]
qui par image inverse \inserted{d'extensions} donne naissance
à l'extension
\[
1-\pi_1(X\setminus I,x)-\pi_1(X_0\setminus I_0,x_0)
\longrightarrow\pi_1(k_0/k)-1
\]
$\ldots\quad\Gamma\xrightarrow{\chi}\operatorname{Aut}(T)\simeq\widehat{\mathbf Z}^{*}$
est l'hom de Kummer-Tate $\ldots$

\textcircled{II} \uline{Plus} précisément supposons $k_0=\mathbf Q$, $X_0=\mathbf P^1_{\mathbf Q}$,
\inserted{$\overline{\mathbf Q}$ clôture alg. de $\mathbf Q$ dans $\mathbf C$},
\[
I=\mu_{\nu+1}(\overline{\mathbf Q})=\mu_{\nu+1}(\mathbf C^{*})
\subset\overline{\mathbf Q}
=\unsure{\mathbf E|\mathbf A}^1_{\overline{\mathbf Q}}(\overline{\mathbf Q})
\subset\mathbf P^1_{\overline{\mathbf Q}}(\overline{\mathbf Q})
\]
On trouve un isomorphisme canonique,
via l'exponentielle et les lacets
\deleted{$\unsure{I\simeq[0,\nu]|I\simeq[0,1]}$},
\[
\Sigma(X/I/k)^{\mathrm{ext}}\simeq L_\nu^{\mathrm{ext}}
\]
donc $P(X,I/k)=$ torseur trivial
''',[
('deletion','top-left','X₀/S'),
('text','top','d’une situation X₀/I₀/x₀/k₀'),
('text','upper','où k₀ est un sous-corps [OPS...]'),
('text','upper-middle','Alors Γ=Gal(k/k₀) opère sur Σext'),
('deletion','middle','la'),
('deletion','middle','donc'),
('insertion','middle above deleted donc','ou encore'),
('display','middle','Γ → twisted Γtilde_ν≃Aut(Σext)'),
('text','middle','qui par image inverse donne naissance'),
('insertion','above donne','d’extensions'),
('display','lower-middle','fundamental-group extension'),
('display','lower-middle','Γ→χ Aut(T)≃Zhat*'),
('text','lower-middle','est l’hom de Kummer-Tate'),
('text','lower','II Plus précisément supposons k₀=Q'),
('insertion','lower interlinear','Qbar clôture alg. de Q dans C'),
('display','lower','I=μ_{ν+1}(Qbar)=μ_{ν+1}(C*)'),
('text','lower','On trouve un isomorphisme canonique'),
('deletion','near bottom','I≃[0,ν]'),
('display','bottom','Σ(X/I/k)ext≃L_νext'),
('text','bottom','donc P(X,I/k)=torseur trivial')])
