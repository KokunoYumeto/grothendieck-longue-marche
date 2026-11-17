from workflow import save_page
save_page(80,r'''\scanpage{80}
% archive foliation: 79
Groupe profini \uline{spécial}

\unsure{1} C'est un système \inserted{$\Sigma=$}
$(T,\pi,I,(\Phi_i)_{i\in I}\in(\operatorname{Homext}(T,\pi))^I)$
avec
\[
\Sigma\left\{\begin{array}{l}
T\ \text{groupe profini}\ \simeq\widehat{\mathbf Z}\\
\pi\ \text{groupe profini}\\
I\ \text{ensemble fini}\\
\Phi_i\in\operatorname{Homext}(T,\pi)\qquad\text{pour }i\in I
\end{array}\right.
\]
avec l'axiome que ce système est \deleted{\unsure{spécial}}\inserted{isomorphe}
à l'un des systèmes $\Sigma_\nu$ ($\nu\in\mathbf N$, $\nu\geq1$)
suivants :
\[
\Sigma_\nu\left\{\begin{array}{l}
T=\widehat{\mathbf Z}\\
\pi=\text{groupe profini }\inserted{\pi_\nu=}\widehat L_\nu,\quad
\text{où }L_\nu=\{\lambda_0,\ldots,\lambda_\nu\mid\lambda_0\lambda_1\cdots\lambda_\nu=\unsure{1}\}\\
\qquad(\text{donc }\pi\text{ prolibre à }\nu\text{ générateurs})\\
\unsure{I|\Phi}=[0,\nu]_{\mathbf N}\\
\Phi_i=\text{classe de l'hom }\widehat{\mathbf Z}\xrightarrow{\varphi_i}\pi
\quad\text{tel que }\varphi_i(1)=\lambda_i
\end{array}\right.
\]
\uline{NB} $I$ peut être interprété comme une \uline{partie} de $\operatorname{Homext}(T,\pi)$.
Si $\Sigma\simeq\Sigma_\nu$, $\nu$ est uniquement déterminé
comme $\operatorname{card}I-1$, ou \deleted{\unsure{le}}
\deleted{\unsure{le rang}}, comme rang profini de $\pi_{\mathrm{ab}}$. Pour
$\nu$ fixé, la catégorie des $\Sigma$ correspondants
est équivalente à la catégorie des torseurs
sous
\[
\widetilde A_\nu=\operatorname{Aut}(\Sigma_\nu)
\]
On a des homomorphismes
\[
\widetilde A_\nu\longrightarrow\unsure{\mathfrak S}_{\nu+1}
\quad(=\operatorname{Aut}(I_\nu))
\]
\[
\widetilde A_\nu\xrightarrow{\chi}\operatorname{Aut}\widehat{\mathbf Z}
\simeq\widehat{\mathbf Z}^{*}
\]
''',[
('text','top','Groupe profini spécial'),
('text','upper','C’est un système'),
('insertion','above tuple','Σ='),
('display','upper-middle','Σ: T,π,I,Φ_i'),
('text','middle','avec l’axiome que ce système est'),
('deletion','middle','spécial'),
('insertion','middle above deleted word','isomorphe'),
('display','middle','Σ_ν definition'),
('insertion','over widehat Lν','π_ν='),
('text','lower-middle','NB I peut être interprété comme une partie'),
('text','lower','Si Σ≃Σν, ν est uniquement déterminé'),
('deletion','lower','le; le rang'),
('display','lower','Atilde_ν=Aut(Σν)'),
('text','bottom','On a des homomorphismes'),
('display','bottom','Atilde_ν→S_{ν+1}'),
('display','bottom','Atilde_ν→χ Aut Zhat≃Zhat*')])
