from workflow import save_page
save_page(85,r'''\scanpage{85}
% archive foliation: 84
se déduit de l'hom évident
\[
\mu_n(\overline{\mathbf Q})\xrightarrow{\rho_\nu}\widetilde A_\nu
\]
provenant de la permutation circulaire des
gén. de $\widehat L_\nu$ --- l'opération de
$\mathbf Z/2$ dans $\unsure{\widetilde{\mathcal T}_\nu|\widetilde\Gamma_\nu}$ provient de $=$ de
l'opération
\[
\mathbf Z/2-\widetilde A_\nu
\]
\deleted{\unsure{par}}
\[
\left\{\begin{aligned}
(\lambda_0,\lambda_1,\ldots,\lambda_\nu)&\xrightarrow{t_\nu}
\deleted{(\unsure{\lambda_0},\lambda_\nu,\lambda_{\nu-1},\ldots,\lambda_1)}\\
&\inserted{(\lambda_0,q_\nu\lambda_\nu q_\nu^{-1},
q_{\nu-1}\lambda_{\nu-1}q_{\nu-1}^{-1},\ldots,
\unsure{q_2}\lambda_2q_2^{-1},\lambda_1)}\\
&\text{où }\unsure{q_i|g_i}=\lambda_{\unsure{0|1}}\cdots\lambda_{i-1}
\end{aligned}\right.
\]
qui renverse l'ordre circulaire.
\margin{\uline{vérifier ?}}
Ceci dit donc que l'hom
\diagram{\begin{tikzcd}[column sep=large]
\Gamma\arrow[r,"i_\nu"]&\unsure{\widetilde{\mathcal T}_\nu|\widetilde\Gamma_\nu}\arrow[r,dotted,dash,"\varepsilon_\nu"]&\mathfrak S_n\supset(\mathbf Z/n)^*
\end{tikzcd}}
\deleted{$\unsure{\mu_n(\overline{\mathbf Q})}$}
satisfait, en plus de
\[
\left[\varepsilon_\nu i_\nu=\chi_n\right.\quad\unsure{aux|ou}
\]
la relation
\[
\left\{\begin{aligned}
&i_\nu(\Gamma)\text{ commute à }t_\nu\\
&i_\nu(\gamma)\rho_\nu(i)\unsure{i_\nu|t_\nu}(\gamma)^{-1}
=\rho_\nu(\chi_n(\gamma)i)
\end{aligned}\right.
\]
''',[
('text','top','se déduit de l’hom évident'),
('display','upper','μ_n(Qbar)→ρ_ν Atilde_ν'),
('text','upper-middle','provenant de la permutation circulaire'),
('display','middle','Z/2−Atilde_ν'),
('deletion','left of tuple','par'),
('display','middle','(λ₀,λ₁,...,λν)→tν'),
('deletion','middle tuple image','(λ₀,λν,λν−1,...,λ₁)'),
('insertion','above and right of tuple','λ₀,qνλνqν⁻¹,...'),
('display','below tuple','q_i=λ₀...λ_{i−1}'),
('text','below tuple','qui renverse l’ordre circulaire'),
('margin note','left-middle','vérifier ?'),
('text','lower-middle','Ceci dit donc que l’hom'),
('diagram','lower-middle','Γ→iν Ttilde_ν dotted line to S_n'),
('deletion','right below diagram','μ_n(Qbar)'),
('text','lower','satisfait, en plus de'),
('display','lower','ε_νi_ν=χ_n'),
('text','lower','la relation'),
('display','bottom','iν(Γ) commute à tν; conjugation relation')])
