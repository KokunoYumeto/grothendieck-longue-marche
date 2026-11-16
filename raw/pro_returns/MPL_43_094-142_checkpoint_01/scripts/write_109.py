from page_work import save_page
text=r'''\scanpage{109}
\uline{$2^\circ$}) $G=\mu_p$
\[
\underline{\operatorname{Ext}}^i_{k\mathrm{gr}}(G,\unsure{\mathbb Q/\mathbb Z})=
\left\{\begin{array}{l}0\\0\\0\\0\end{array}\right.
\]
\deleted{$H^0(k,\mu)$}\qquad $\mathbb Z/n\mathbb Z\quad\mu_p$
\[
\deleted{H^i}\qquad K^*/\unsure{k^{*p}|K^{*p}}
\]
\[
H^1(k,\mu_p)\qquad k^*/k^{*p}
\]
\[
H^i(k,G_m)=
\]
\diagram{\begin{tikzcd}k^*\arrow[r,"p"]&k^*\end{tikzcd}}
\figure{\begin{tikzpicture}[scale=.6]
\draw (0,2.5)..controls(-.2,.7)and(0,0)..(1,0)--(2.8,0)
..controls(4,0)and(4,1)..(4,1.8)..controls(4,2.2)and(7.5,2.1)..(8.5,2.5);
\end{tikzpicture}}
$3^\circ)$ $G=\alpha_p$
\[
x^p
\]
$3^\circ)$ $G=G_m$
\[
\underline{\operatorname{Ext}}^i(G_m,\mathbb Q/\mathbb Z)=
\left\{\begin{array}{l}0\\(\text{racines de l'unité})^\vee\\0\\0\end{array}\right.
\]
\[
1
\]
\[
\underline{\underline{\operatorname{Ext}}}^i_{k\mathrm{gr}}(G_m,\mathbb Q/\mathbb Z)=
H^{i-1}(k,\text{racines de }\unsure{1})^{\unsure{\vee|'}}
\longrightarrow\left\{\begin{array}{l}0\\\unsure{\text{racines de l'unité}}\\0\\0\end{array}\right.
\]
\margin{$1$}
\deleted{$k^*$}
\[
H^i(k,G_m)=\left\{\begin{array}{l}k^*\\0\\0\\\unsure{0}\\\unsure{0}\end{array}\right.
\]
\[
\operatorname{Ext}(G_m,\deleted{\mathbb Z/n\mathbb Z}{}_n\mu)=\mathbb Z/n\mathbb Z
\]
\[
\operatorname{Ext}(G_m,\mathbb Z/n\mathbb Z)\simeq{}_n\mu^\vee
\]
\[
\operatorname{Ext}(G_m,\unsure{\mathbb Z_{(\to)1}|\mathbb Z_{(\infty)1}})
\simeq\underset{n}{\underline{\lim}}\,{}_n\mu^\vee
\]
\[
\operatorname{Hom}(\Pi_\bullet(G_m),\mathbb Q/\mathbb Z)
\]
\margin{$\boxed{\begin{array}{c}
\operatorname{Ext}_{k\mathrm{gr}}(G_m,\mathbb Q/\mathbb Z)\\[1em]
\uline{\unsure{est de}}\quad k^*
\end{array}}$}
\margin{$\Vert\quad\operatorname{Hom}(G_m(k),\mathbb Q/\mathbb Z)$}
\mspage{108}
'''
save_page(109,text,[('text','top item','2°) G=mu p'),('display','top right','underlined Ext i kgr(G,Q/Z) four zeros'),('deletion','upper left','H0(k,mu)'),('display','upper left same line','Z/nZ mu p'),('deletion','upper left next line','H i'),('display','upper left next line','K star / k star p'),('display','upper middle','H1(k,mu p) k star/k star p'),('display','middle left','H i(k,Gm)='),('diagram','middle left below','k star p→k star'),('drawing','middle separating curve','long rounded stepped line'),('text','middle right item','3°) G=alpha p'),('display','middle right','x p'),('text','middle lower item','3°) G=Gm'),('display','middle lower','underlined Ext i(Gm,Q/Z) roots of unity dual'),('display','middle below cases','1'),('display','lower middle','double-underlined Ext i kgr(Gm,Q/Z) = H i-1(k,racines de 1) to cases'),('margin note','right beside cases below','1'),('deletion','lower left beside H','k star'),('display','lower middle','H i(k,Gm) k star and zeros'),('display','bottom first Ext','Ext(Gm,n mu)=Z/nZ'),('deletion','bottom first Ext argument','Z/nZ'),('display','bottom second Ext','Ext(Gm,Z/nZ) ≃ n mu dual'),('display','bottom third Ext','Ext(Gm,Z indexed) ≃ lim n mu dual'),('display','bottom left','Hom(Pi bullet(Gm),Q/Z)'),('margin note','bottom right boxed','Ext kgr(Gm,Q/Z) est de k star'),('margin note','bottom right below box','vertical equal Hom(Gm(k),Q/Z)'),('text','bottom left page number','108')],observations='Full sheet and both halves read, with enlarged middle and bottom formulae. Faint reversed type is bleed-through, not forward text on this side. The duplicated 3° numbering is retained. Single and double underlines, star superscripts, dual-vees and the unfinished H expression are differentiated. The low Ext argument is not confidently deciphered and remains a symbol-level alternative.')
