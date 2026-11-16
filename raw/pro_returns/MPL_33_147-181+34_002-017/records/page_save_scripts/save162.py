import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,162,r'''\scanpage{162}
\margin{\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&\unsure{\overline{T}|T}\times_Z T'\arrow[dl]\arrow[dr]&\\
T\arrow[dr]&&T'\arrow[dl]\\
&X\times_S Y=Z&
\end{tikzcd}}\quad\unsure{f}\quad *}
À vrai dire, \deleted{\unsure{et}} si $\overline{T}$ est l'image de $T$ dans $Z=X\times_S Y$, on voit que $\overline{\alpha^0}$ ``est'' dans \deleted{l'image}
\[
\mathrm{R}^0\Gamma_{\overline{T}}(\mathrm{R}\mathcal{H}om(\mathrm{pr}_1^*(F),\mathrm{pr}_2^!(G_\bullet))
=\mathrm{R}^0\Gamma_{X\times_S Y}(\mathrm{R}^0\underline{\Gamma}_{\overline{T}}\mathrm{R}\mathcal{H}om(\,,))
\]
et de même $\overline{\beta^0}$ ``est \deleted{\unsure{dans l'image}}\inserted{même}'' dans
\[
\mathrm{R}^0\Gamma_{\overline{T}'}(\mathrm{R}\mathcal{H}om(\mathrm{pr}_2^*(G),\mathrm{pr}_1^!(F))
=\mathrm{R}^0\Gamma_{X\times_S Y}(\mathrm{R}^0\underline{\Gamma}_{\overline{T}'},\mathrm{R}\mathcal{H}om
\]
Ainsi, on peut définir un cup-produit
\[
\overline{\alpha^0}\cup\overline{\beta^0}\in
\mathrm{R}^0\Gamma_{\overline{T}\cap\overline{T}'}K_{\unsure{\infty}X\times_S Y}^{\bullet}
\simeq\mathrm{R}^0\Gamma_{\overline{T}\cap\overline{T}'}K_{\overline{T}\times_S\overline{T}'}^{\bullet}
\]
Ceci permet donc de définir, si
\[
\overline{T}\cap\overline{T}'=\bigcup_\alpha S_\alpha,
\]
\deleted{\unsure{réunion}} les $S_\alpha$ ouverts deux à deux disjoints (en nb fini) de définir des composantes canoniques
\[
(\overline{\alpha^0}\cup\overline{\beta^0})_\alpha:
\deleted{\unsure{\in H^0(S_\alpha,K_{S_\alpha}^{\bullet})}}
\]
et des $\deleted{\unsure{\operatorname{Tr}_{S_\alpha}}}\langle\xi^0,\eta^0\rangle_{S_\alpha}$ telles que
\[
\langle\xi^0,\eta^0\rangle=\sum_\alpha\langle\xi^0,\eta^0\rangle_{S_\alpha}
\]
\uline{Exemple}. Supposons $\overline{T}\cap\overline{T}'=\varnothing$. Alors le nb de Lefschetz est nul.
\margin{161}
''',[
('diagram','upper left margin','T times_Z T prime, T, T prime, X times_S Y=Z'),('margin note','beside diagram','f, asterisk'),('text','top','À vrai dire, si T bar est l’image'),('deletion','top','et'),('deletion','upper','l’image'),('display','upper','R0Gamma_Tbar RHom'),('text','upper middle','et de même beta bar'),('deletion','upper middle','dans l’image'),('insertion','upper middle','même'),('display','upper middle','R0Gamma_Tbarprime RHom'),('text','middle','Ainsi on peut définir'),('display','middle','cup product supported on intersection'),('text','middle','Ceci permet donc de définir'),('display','middle','Tbar intersection Tbarprime union S_alpha'),('deletion','middle','réunion'),('text','lower middle','les S_alpha ouverts deux à deux'),('display','lower middle','component alpha'),('deletion','lower middle display','overwritten component target'),('text','lower','et des ... telles que'),('deletion','lower','Tr_Salpha'),('display','lower','pairing equals sum local pairings'),('text','bottom','Exemple. Supposons intersection empty'),('margin note','bottom left','161')],remarks='Whole, halves and enlarged formula/prose/deletions examined. The upper RHS expressions reach the physical right edge; the second ends visibly after RHom without a legible argument, and no missing argument is manufactured. The dualizing-complex subscript at the right of the cup-product line visibly uses a product of the barred supports, retained although an intersection might be expected. Two cancelled mathematical fragments are low-confidence best readings. Research lead: support-sensitive local decomposition, disjoint supports give vanishing Lefschetz number.')
