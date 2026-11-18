from save_page import save_page

save_page(101, r'''
\scanpage{101}
% archive foliation: 100
\textcircled{1}

$X$ schéma

$D_i$ diviseurs de Cartier $\geq0$ \hfill $1\leq i\leq r$

$n_i$ entiers $\geq1$ \hfill $1\leq i\leq r$

$\Gamma$ schém. en groupes sur $S$

$\deleted{\unsure{\mu=}}\mu_{\underline n}=\prod\mu_{n_i}$ \quad $(\underline n=(n_1,\ldots,n_r))$ sur $X$

Extension de groupes sur $X$
\diagram{\begin{tikzcd}[column sep=small]
1 \arrow[r] & \mu \arrow[r,dash] & G \arrow[r,dash] & \Gamma \arrow[r,dash] & 1
\end{tikzcd}}

\diagram{\begin{tikzcd}[column sep=small]
X' \arrow[r] & \widetilde X_{\unsure{1}} \arrow[r] & X
\end{tikzcd}}
morphisme de schémas sur $X$, à op. $G$.

On suppose a) que $G$ opère sur $\widetilde X_{\unsure{1}}$ que $\mu$ y opère trivialement, que \deleted{$\unsure{G}$} $\widetilde X_1$ devient \uline{torseur} sous $\Gamma$

b) En tant que fibré à opérateurs $\mu_{\widetilde X_{\unsure{1}}}\inserted{=\mu_{\underline n,\widetilde X}}$, $X'\unsure{/}$ sur $X$, est loc. \deleted{\unsure{à}} (sur $\widetilde X_{\unsure{1}}$) de type Kummérien relatif aux images inverses $\widetilde D_i$ des $D_i$ (supposés être encore diviseurs)\inserted{d'exposant $n_i$} i.e. de la forme
\[
\widetilde X[T_1,\ldots,T_r]/(T_1^{n_1}-a_1,\ldots,T_r^{n_r}-a_r),
\]
où les $a_i$ sont des équations des $\widetilde D_i$ (locales).

b$^2$) \deleted{$\Gamma$ opère sur $\mu$, \unsure{défini par}} On a donc un isom $\widetilde X\mathbin{\times}^{\Gamma}\mu\simeq\mu_n$.

\margin{\diagram{\begin{tikzcd}[column sep=small,row sep=small]
B_G \arrow[d] & B_\mu \arrow[l] \arrow[d] & B_{\unsure{\Gamma}}/(\widetilde X,\unsure{G}) \arrow[dl] \\
B_\Gamma & (\widetilde X,\Gamma) \arrow[l] \arrow[r,phantom,"\simeq"] & X
\end{tikzcd}}}

L'extension\inserted{$G$} de $\Gamma$ par $\mu$ définit une classe $\alpha\in H^2(B_\Gamma,\mu)\deleted{\unsure{\simeq\prod H^2(B_\Gamma,\mu_{n_i})}}$. On a un hom canonique, qui au\inserted{$\Gamma$-torseur} $X$
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
H^2(B_\Gamma,\mu) \arrow[r,"\varphi"] & H^2(X,\mu_n) \arrow[r,phantom,"\simeq"] \arrow[d,phantom,"\unsure{\wr}"] & \prod H^2(X,\mu_{n_i}) \\
& H^2(B_\Gamma/(\widetilde X,\unsure{\Gamma}),\mu) &
\end{tikzcd}}

On veut prouver que \unsure{si}
\[
\varphi(\alpha)=(\xi_i)_{1\leq i\leq r}\qquad
\xi_i=c(\underline{O}_X(D_i))\quad(\bmod n_i).
\]
\margin{la classe de Chern mod $n_i$\deleted{\illegible{1}}}

\textcircled{2} Variantes schémas formels (ou topos loc. annelés généraux)
''', [
('text','top, numbered setup','1; X schéma'),
('text','upper, divisor family','D_i diviseurs de Cartier geq 0; 1 leq i leq r'),
('text','upper, integer family','n_i entiers geq 1; 1 leq i leq r'),
('text','upper, group scheme','Gamma schém. en groupes sur S'),
('display','upper, roots of unity notation','mu_n = product mu_n_i; n vector'),
('deletion','upper, before mu_n','mu='),
('text','upper-middle, extension label','Extension de groupes sur X'),
('diagram','upper-middle, extension','1 to mu - G - Gamma - 1'),
('diagram','upper-middle, morphisms of schemes','X prime to X tilde_1 to X'),
('text','upper-middle, morphism description','morphisme de schémas sur X à op. G'),
('text','middle, condition a)','On suppose que G opère'),
('deletion','middle, before tilde X devient','G'),
('text','middle, condition b)','En tant que fibré à opérateurs'),
('insertion','middle-right, identification of operators','mu_{n,X tilde}'),
('deletion','middle, after loc.','à'),
('insertion','middle-right, after diviseurs','d\u0027exposant n_i'),
('display','middle-lower, Kummer algebra','X tilde[T_1,...,T_r]/(T_1^n_1-a_1,...)'),
('text','middle-lower, equations of divisors','où les a_i sont des équations'),
('text','lower-middle, b squared','On a donc un isom'),
('deletion','lower-middle, before On a donc','Gamma opère sur mu défini par'),
('diagram','left margin, rotated in scan','B_G; B_mu; B_Gamma; (X tilde,Gamma); X; quotient topos'),
('text','lower, extension class','L\u0027extension de Gamma par mu définit une classe'),
('insertion','lower, after L\u0027extension','G'),
('deletion','lower, after H^2(B_Gamma,mu)','simeq product H^2(B_Gamma,mu_n_i)'),
('text','lower, canonical homomorphism introduction','On a un hom canonique qui au X'),
('insertion','lower-right, above X','Gamma-torseur'),
('diagram','lower, cohomology restriction','H^2(B_Gamma,mu) phi to H^2(X,mu_n); quotient topos equality'),
('text','bottom, desired conclusion','On veut prouver que si'),
('display','bottom, Chern class equation','phi(alpha)=(xi_i); xi_i=c(O_X(D_i)) mod n_i'),
('margin note','bottom-right below c','la classe de Chern mod n_i'),
('deletion','bottom-right, under O_X(D_i)','one unreadable word'),
('text','bottom edge, numbered variant','2 Variantes schémas formels')
], [
('X tilde subscripts throughout','1','Several 1-like strokes are overwritten or could be deleted subscripts','low'),
('extension connectors','plain dashes after mu','No arrowheads visible on these three connectors','high'),
('condition b), X prime','slash before sur X','May be a correction/leader stroke rather than division','low'),
('condition b), inserted exponent','d\u0027exposant n_i','Exposant compressed','medium'),
('condition b squared, deleted ending','défini par','Heavy crossing','low'),
('left-margin topos diagram','B_Gamma/(X tilde,G)','The final group and B subscript are overwritten; topology retained','low'),
('cohomology, coefficient subscript','mu_n','Underlining of n not visible here although vector n was underlined above','medium'),
('cohomology quotient denominator','Gamma','Overwritten letter may be G','low'),
('desired conclusion introduction','si','Could be a short unfinished word or punctuation','low'),
('under Chern class formula','one cancelled word unreadable','Crosshatching hides it even enlarged','low'),
('torseur insertion and X','qui au Gamma-torseur X','Phrase unfinished as written; no missing verb supplied','medium')
], [
'Extension class alpha in H^2(B_Gamma,mu), a Gamma-torsor, and a local Kummer algebra attached to effective Cartier divisors lead to a desired relation phi(alpha)_i=c(O_X(D_i)) mod n_i. The page says On veut prouver; no proof is on this leaf.',
'The bottom line explicitly proposes variants for formal schemes or general locally ringed topoi.',
'No title sheet or page count: circled 1 and 2 are internal numbered items, not assigned manuscript page numbers.'
])
