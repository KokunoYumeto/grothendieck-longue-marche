from workflow import save_page
save_page(81,r'''\scanpage{81}
% archive foliation: 80
donnant naissance à
\[
\widetilde A_\nu\longrightarrow\unsure{\mathfrak S}_{\nu+1}\times\widehat{\mathbf Z}^{*}
\]
qui est \uline{surjectif}. Le noyau de $\widetilde A_\nu\to\mathfrak S_{\nu+1}$
est noté $A_\nu$, celui de $\widetilde A_\nu\to\mathfrak S_{\nu+1}\times\widehat{\mathbf Z}^{*}$
est noté $A_\nu^\circ$. D'ailleurs on a
un homomorphisme injectif
\[
\pi\longrightarrow A_\nu^\circ\subset A_\nu
\]
via automorphismes intérieurs. Le conoyau
\inserted{de $\pi\to A_\nu^\circ$ ($\pi\to A_\nu$, $\pi\to\widetilde A_\nu$)}
se \deleted{\unsure{on}} note $\Gamma_\nu^\circ$ \inserted{($\Gamma_\nu$, $\widetilde\Gamma_\nu$)}, d'où on a des
suites exactes
\diagram{$\left\{\begin{array}{l}
1-\pi\longrightarrow A_\nu^\circ\longrightarrow\Gamma_\nu\longrightarrow1\\
\deleted{\unsure{1-\pi-}}\\
1\longrightarrow A_\nu\longrightarrow\widetilde A_\nu\longrightarrow\mathfrak S_{\nu+1}-1
\end{array}\right.$}
\[
1\unsure{\Longrightarrow|\longrightarrow} A_\nu^\circ\longrightarrow A_\nu-\widehat{\mathbf Z}^{*}-1
\]
\[
\overbrace{\pi\quad\Gamma_\nu^\circ\quad\widehat{\mathbf Z}^{*}\quad\mathfrak S_{\nu+1}}^{\widetilde A^{\unsure{\nu|\vphantom{\nu}}}}
\qquad\text{filtration}
\]
\uline{Exemples} \textcircled{I} Soit $X$ droite projective sur
$k$ alg. clos de car. $0$, $I\subset X(k)$, $\operatorname{card}I=\nu+1$
\[
T=\unsure{T_{\bullet}}(k)=\varprojlim_n\mu_n(k),\qquad
\pi=\pi_1(X\setminus I,x)
\]
où $x\in X(k)-I$. Il \deleted{\unsure{que}} y a par Kummer
''',[
('text','top','donnant naissance à'),
('display','upper','Atilde_ν→S_{ν+1}×Zhat*'),
('text','upper-middle','qui est surjectif. Le noyau'),
('display','middle','π→A_ν°⊂A_ν'),
('text','middle','via automorphismes intérieurs. Le conoyau'),
('insertion','interlinear','de π→A_ν° (π→A_ν, π→Atilde_ν)'),
('deletion','middle before note','on'),
('insertion','after Γ_ν°','(Γ_ν,Γtilde_ν)'),
('diagram','lower-middle','two exact sequences with left brace'),
('deletion','between sequences','1−π−'),
('display','lower-middle','1⇒A_ν°→A_ν−Zhat*−1'),
('display','lower','filtration π,Γ_ν°,Zhat*,S_{ν+1}'),
('text','lower','Exemples I Soit X droite projective'),
('display','bottom','T=Tbullet(k)=lim μ_n(k), π=π₁(X∖I,x)'),
('text','bottom','où x∈X(k)−I. Il y a par Kummer'),
('deletion','bottom','que')])
