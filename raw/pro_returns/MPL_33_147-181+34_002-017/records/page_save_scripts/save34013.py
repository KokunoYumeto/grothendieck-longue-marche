import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{13}
\mspage{11}

Il convient de déterminer l'hom.
\[
(3.8)\qquad I'_t\simeq\prod_{\ell\ne\unsure{p}}\mathbf Z_\ell(1)\longrightarrow\inserted{I_t\simeq}\prod_{\ell\ne p}\mathbf Z_\ell(1)
\]
où on identifie, grâce à l'inclusion $\bar K\subset\bar K'$, les \deleted{\unsure{deux}} groupes $\mathbf Z_\ell(1)$ définis à l'aide de $\bar K$ ou de $\bar K'$ (savoir $T_\ell(\bar K^*)$ et $T_\ell(\bar K'^*)$).

Pour ceci, on regarde les sous-corps (pour $(n,p)=1$)
\[
(3.9)\qquad\begin{cases}
 K_n=\widetilde K(\unsure{\Theta}_n)\subset\bar K_t&\text{où }\Theta_n^n=t,\\
 K'_n=\widetilde K'(\Theta'_n)\subset\bar K'_t&\text{où }\Theta_n'^n=t'
\end{cases}
\]
et on regarde comment
\[
\operatorname{Gal}(K'_n/\widetilde K')\simeq\mu_n(\widetilde K')\xleftarrow{\sim}\mu_n(\widetilde K)
\]
(groupe des racines nièmes $\varepsilon$ de 1 dans $\widetilde K$) opère sur $K_n$. Si $\varepsilon_{K'}$ désigne l'opération sur $K'_n$ définie par $\varepsilon$, donc
\[
\varepsilon_{K'_n}(\Theta'_n)=\varepsilon\Theta'_n
\]
on trouve, si
\[
(3.\unsure{10})\qquad t=\deleted{\unsure{t}}u't'^e\qquad\uline{(e\in\mathbf N,\ u'\in V^*)}
\]
\inserted{$0<e$}
\margin{d'où $\Longleftarrow\boxed{\begin{array}{c}\deleted{\mathfrak m\widetilde V=\unsure{\mathfrak m'^e}}\\\mathfrak mV=\mathfrak m'^e\end{array}}$}
que
\[
\Theta_n^n=u'(\Theta_n'^e)^n
\]
donc, si on pose
\[
(3.\unsure{11})\qquad\Theta_n=\lambda\Theta_n'^e,\qquad\uline{(\lambda\in K'_n)}
\]
on aura
\[
\deleted{(3.\unsure{12})}\qquad\lambda^n=u',
\]
donc \deleted{\unsure{elle}} $\lambda\in\widetilde V'$ \deleted{\unsure{est}} donc $\varepsilon_{K'}(\lambda)=\lambda$
et on trouve
\[
\varepsilon_{K'_n}(\Theta_n)=\underbrace{\varepsilon_{K'_n}(\lambda)}_{\substack{\Vert\\\lambda}}\varepsilon_{K'_n}(\Theta_n'^e)=\lambda(\varepsilon\Theta'_n)^e=\unsure{\varepsilon}^e\unsure{\Theta_n}
\]
\margin{par (3.10)}
\margin{12}
'''
e=[('text','top','Il convient de déterminer l’hom'),('display','top','(3.8) I′_t ≃ product Zℓ(1) → I_t'),('insertion','above right product','I_t≃'),('text','upper','où on identifie grâce à l’inclusion'),('deletion','upper','deux'),('text','upper-middle','Pour ceci on regarde les sous-corps'),('display','middle','(3.9) K_n; K′_n; Theta root equations'),('text','middle','et on regarde comment'),('display','middle','Gal(K′_n/Ktilde′) ≃ μn(Ktilde′) ← μn(Ktilde)'),('text','middle-lower','groupe des racines nièmes'),('display','middle-lower','epsilon_K′_n(Theta′_n)=epsilon Theta′_n'),('text','lower','on trouve si'),('display','lower','(3.10) t=u′t′^e'),('deletion','3.10 after equality','t'),('insertion','under natural-number condition','0<e'),('margin note','right beside 3.10','d’où; boxed mV=m′^e'),('deletion','boxed note upper line','m Vtilde=m′^e'),('text','lower','que'),('display','lower','Theta_n^n=u′(Theta′_n^e)^n'),('text','lower','donc si on pose'),('display','lower','(3.11) Theta_n=lambda Theta′_n^e'),('text','lower','on aura'),('display','lower','lambda^n=u′'),('deletion','left of lambda^n','(3.12)'),('text','bottom','donc lambda in Vtilde′'),('deletion','bottom before lambda','elle'),('deletion','bottom after Vtilde′','est'),('display','bottom','epsilon_K′_n(Theta_n) product calculation'),('margin note','bottom right','par (3.10)'),('margin note','bottom left','12')]
save_page(34,13,tex,e,remarks='The unit condition visibly has V* without a secure prime, and the boxed ideal equation has mV, also without a prime; neither has been corrected. The small insertion below the condition appears 0<e and is tentative in attachment. Theta and the last epsilon are overwritten. The final equality carries a marginal par (3.10) pointer.')
