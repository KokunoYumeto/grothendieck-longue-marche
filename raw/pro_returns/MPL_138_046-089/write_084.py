from workflow import save_page
save_page(84,r'''\scanpage{84}
% archive foliation: 83
d'où
\[
\Gamma=\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)
\longrightarrow\unsure{\widetilde{\mathcal T}_\nu|\widetilde\Gamma_\nu}
\]
L'hom correspondant
\[
\Gamma\longrightarrow\unsure{\mathfrak S}_{\nu+1}
\]
se fait via
\[
\Gamma\longrightarrow\mu_{\nu+1}(\mathbf C^{*})\simeq\mathbf Z/\nu+1
\xrightarrow{\mathrm{can}}\mathfrak S_{\nu+1}\ldots
\]
L'intérêt de prendre $I$ comme
dessus est d'avoir une opération
de \inserted{$\mathbf Z/2\cdot$}$\mu_{n\,\mathbf Q}$ \deleted{\unsure{trans.}} sur la situation
$(X_0/I_0/\mathbf Q)$ donc de \inserted{$\mathbf Z/2\cdot$}$\mu_n(\overline{\mathbf Q})\ (=D_n)$
sur $X/I/\mathbf Q$ --- en fait, le
produit $\tfrac12$ direct
$(\Gamma\times\deleted{\unsure{\mathbf Z/2}})\underbrace{\mu_n(\overline{\mathbf Q})}_{\subset\overline{\mathbf Q}^{*}}$\unsure{$=$}
opère sur $X/I/\overline{\mathbf Q}$ donc
\deleted{s'envoie dans}
\[
(\Gamma\times\mathbf Z/2)\cdot\mu_n(\overline{\mathbf Q})
\unsure{\Longrightarrow|\longrightarrow}
\unsure{\widetilde{\mathcal T}_\nu|\widetilde\Gamma_\nu}
\]
où l'hom $\mu_n(\overline{\mathbf Q})\longrightarrow\unsure{\widetilde{\mathcal T}_\nu|\widetilde\Gamma_\nu}$
\margin{$n=\nu+1$}
''',[
('text','top','d’où'),
('display','upper','Γ=Gal(Qbar/Q)→Ttilde_ν'),
('text','upper-middle','L’hom correspondant'),
('display','upper-middle','Γ→S_{ν+1}'),
('text','upper-middle','se fait via'),
('display','middle','Γ→μ_{ν+1}(C*)≃Z/(ν+1)→can S_{ν+1}'),
('text','middle','L’intérêt de prendre I comme dessus'),
('insertion','above μ_nQ','Z/2·'),
('deletion','middle','trans.'),
('insertion','above μ_n(Qbar)','Z/2·'),
('text','lower-middle','(X₀/I₀/Q) donc de μ_n(Qbar)'),
('display','lower-middle inline','produit 1/2 direct (Γ×...)μ_n(Qbar)'),
('deletion','lower-middle product','Z/2'),
('text','lower','opère sur X/I/Qbar donc'),
('deletion','above bottom display','s’envoie dans'),
('display','bottom','(Γ×Z/2)·μ_n(Qbar)→Ttilde_ν'),
('text','bottom','où l’hom μ_n(Qbar)→Ttilde_ν'),
('margin note','left-middle','n=ν+1')])
