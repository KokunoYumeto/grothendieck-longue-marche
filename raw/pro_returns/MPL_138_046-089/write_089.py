from workflow import save_page
save_page(89,r'''\scanpage{89}
% archive foliation: 88
\uline{Groupes prolibres} spéciaux.
\[
\left\{\begin{array}{l}
\pi\ \text{groupe profini}\\
\unsure{L|T}\quad\widehat{\mathbf Z}\text{-Module libre}
\deleted{\simeq\widehat{\mathbf Z}\text{ (isomorphisme non précisé)}}\inserted{\text{de rang }1}\\
\Phi_i\in\operatorname{Homext}(L,\pi)\deleted{\unsure{\Phi}}
\qquad0\leq i\leq\nu\qquad(\nu\geq2)
\end{array}\right.
\]
\uuline{Hyp} :
\[
\left\{\begin{array}{l}
\exists\ e\in L^*\quad(\text{base de }L)\\
(\varphi_i)_{0\leq i\leq\nu}\in\displaystyle\prod_{0\leq i\leq\nu}\Phi_i
\end{array}\right\}\ \text{tels que, posant }h_i=\varphi_i(e),
\]
l'hom de
\diagram{\begin{tikzcd}
\inserted{\widehat L_\nu}\deleted{\unsure{\widehat F([0,\nu])}}\arrow[r]&\pi\\
\lambda_i\arrow[r,mapsto]&h_i
\end{tikzcd}}
\inserted{groupe prolibre \deleted{sur $[0,\nu]$}
engendré par $\lambda_0,\ldots,\lambda_\nu$ avec $\lambda_0\cdots\lambda_\nu=1$}
soit un \uline{isomorphisme}

En d'autres termes
Soit $\pi_0$ \inserted{$=\widehat L_\nu=$} \deleted{groupe pro.}
$(\lambda_0,\ldots,\lambda_\nu\mid\lambda_0\lambda_1\cdots\lambda_\nu=1)^{\wedge}$
\[
T_0=\widehat{\mathbf Z},\quad e_0=1
\]
$\Phi_{0i}$ classe de
\diagram{\begin{tikzcd}
\widehat{\mathbf Z}\arrow[r]&\pi_\nu\\
e_0\arrow[r,mapsto]&\lambda_i
\end{tikzcd}}
on veut que $(\pi,T,(\Phi_i))$ soit isom. à $(\pi_0,T_0,(\Phi_{0i}))$
\[
A_\nu=\operatorname{Aut}(\widehat L_\nu,T_0,(\Phi_{0i}))
\xrightarrow{\chi_\nu}\widehat{\mathbf Z}^{*}
\underset{\operatorname{Aut}(T_0)}{\text{''}}
\]
on \unsure{prouve} que c'est surjectif
\[
\widehat L_\nu\xrightarrow{i}\deleted{\unsure{A.}}\operatorname{Ker}\chi_\nu\subset A_\nu
\qquad\text{injectif}
\]
\[
g\longmapsto(\operatorname{int}(g),\operatorname{id}_{T_0})
\]
\[
u\,i(g)\,u^{-1}=i(u(g))
\]
i.e. $\widehat L_\nu$ invariant ds $A_\nu$
\[
A_\nu/\widehat L_\nu=\Gamma_\nu
\]
on veut élucider sa structure.
''',[
('text','top','Groupes prolibres spéciaux'),
('display','upper','π groupe profini; L Zhat-Module libre; Φ_i'),
('deletion','upper','≃Zhat (isomorphisme non précisé)'),
('insertion','upper','de rang 1'),
('deletion','after Homext formula','Φ'),
('text','upper-middle','Hyp :'),
('display','upper-middle','∃e∈L*, (φ_i)∈∏Φ_i'),
('text','upper-middle','tels que, posant h_i=φ_i(e), l’hom de'),
('diagram','middle','Lhat_ν→π, λ_i↦h_i'),
('deletion','middle diagram source','Fhat([0,ν])'),
('insertion','middle diagram source','Lhat_ν'),
('insertion','below diagram','groupe prolibre engendré par λ₀,...,λν'),
('deletion','within insertion','sur [0,ν]'),
('text','middle','soit un isomorphisme'),
('text','middle-lower','En d’autres termes. Soit π₀'),
('insertion','above π₀ definition','=Lhat_ν='),
('deletion','π₀ definition','groupe pro.'),
('display','middle-lower','(λ₀,...,λν | λ₀...λν=1)^hat'),
('display','lower-middle','T₀=Zhat,e₀=1'),
('text','lower-middle','Φ₀i classe de'),
('diagram','lower-middle','Zhat→πν,e₀↦λ_i'),
('text','lower-middle','on veut que (π,T,(Φ_i)) soit isom.'),
('display','lower','Aν=Aut(Lhatν,T₀,(Φ₀i))→χνZhat*'),
('text','lower-right','on prouve que c’est surjectif'),
('display','lower','Lhatν→i Ker χν⊂Aν injectif'),
('deletion','in injective map','A.'),
('display','lower','g↦(int(g),idT₀)'),
('display','lower-right','u i(g) u⁻¹=i(u(g))'),
('text','lower-right','i.e. Lhatν invariant ds Aν'),
('display','bottom','Aν/Lhatν=Γν'),
('text','bottom','on veut élucider sa structure')])
