from save_page import save
tex=r'''
\scanpage{43}
\diagram{\begin{tikzcd}[column sep=huge,row sep=small]
\mathcal H^1(X;A)\arrow[d,no head]&\operatorname{Ext}^1(A,\operatorname{Pic})\\
\text{\unsure{pt singuliers}}&
\end{tikzcd}}
\[
\boxed{\mathcal H^1(X,G)\simeq\operatorname{Hom}(D(G),\underline{\operatorname{Pic}}_X)}
\]
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) .. controls (-.7,.7) and (.5,1.6) .. (1.1,1.5) .. controls (1.2,.7) and (.3,-.3) .. (0,0);
\draw (-.12,.65) .. controls (.2,1.35) and (.7,1.65) .. (1.1,1.5);
\fill (1.1,1.5) circle (.045);\node at (.71,1.2) {$-$};
\draw (2,1.2) .. controls (2.1,1.8) and (2.6,2.2) .. (2.8,2.15)
.. controls (3.4,2.4) and (3.35,.75) .. (2.8,1.05)
.. controls (2.45,1.2) and (2.65,2.7) .. (3.3,2.8);
\fill (2.8,2.15) circle (.045);
\end{tikzpicture}}
\[\mathcal H^i(X,D(G))\simeq\operatorname{Ext}^i(G,\underline{\operatorname{Pic}}_X)\]
\[\operatorname{Ext}^i_X(f^!(G),G_m)\simeq\operatorname{Ext}^i_Y(G,f_!(G_m))\]
\[
\boxed{\underline{\operatorname{Ext}}^i_X(f^*(G_{\bullet}),H^{\bullet})\simeq
\underline{\operatorname{Ext}}^i_Y(G_{\bullet},f_!(H^{\bullet}))}
\]
\diagram{\begin{tikzcd}X\arrow[d,"f"']\\Y\end{tikzcd}}
\[H=G_m\]
\[
\underline{\operatorname{Ext}}^i_X(\underset{\inserted{\unsure{R}}}{f^*}(G),G_m)
\simeq\underline{\operatorname{Ext}}^i_Y(G,
\overset{\text{\unsure{les supérieurs}}}{\boxed{\underline{\operatorname{Pic}}^{\bullet}_{X/Y}}})
\]
\margin{$\deleted{\unsure{R\Gamma(X,}}$}
\figure{\begin{tikzpicture}\draw (0,1.1)--(.02,.4)--(.18,0);\draw (.2,1.1)--(.21,.4)--(.18,0);\draw (2,1)--(2,0);\draw (2.08,1)--(2.08,0);\end{tikzpicture}}
\[
\boxed{G\ \text{\uline{affine}},\ \text{alors}\quad H^i(X,D(G))\Longleftarrow
\deleted{\unsure{E}}\operatorname{Ext}^{\unsure{i}}(G,\operatorname{Pic}^{\unsure{(q)|(1)}}_{X/Y})}
\]
\[
\begin{array}{rll}
i=0&H^0(X,D(G))=&\deleted{\operatorname{Hom}}D(G)\\
i=1&H^1(X,D(G))=&\deleted{\unsure{\operatorname{Ext}}}\operatorname{Hom}(G,\operatorname{Pic}^{(1)})\\
i=2&H^2(X,D(G))\neq&\operatorname{Ext}^1(G,\operatorname{Pic}^{(1)}_{X/Y})+\operatorname{Hom}(G,\underline{\operatorname{Pic}}^{\unsure{(2)}}_{\unsure{X}})
\end{array}
\]
\margin{$!$}
\figure{\begin{tikzpicture}\draw (0,.15)..controls (3,-.1) and (6,-.1)..(8,0);\end{tikzpicture}}
$G$ abélien, alors \deleted{$\unsure{H}$}
\[H^{\unsure{i-1|i+j}}(X,G')\Longleftarrow\operatorname{Ext}^{\unsure{p}}_{\unsure{g}}(G,\operatorname{Pic}^{q}_{X/Y})\]
\[
\begin{array}{rl}i=0&0\longrightarrow0\\i=1&H^0(X,G')=\end{array}
\]
\margin{42}
'''
e=[('diagram','top','H¹(X;A); Ext¹(A,Pic); pt singuliers'),('display','upper box','H¹(X,G) ≃ Hom(D(G),Pic_X)'),('drawing','upper left','two looped curves with marked points; minus in left loop'),('display','under first box','H^i(X,D(G)) ≃ Ext^i'),('display','middle','Ext_X^i(f^!(G),G_m)'),('display','middle boxed','underlined Ext_X^i(f*(G_•),H^•)'),('diagram','middle left','X → Y, f'),('display','below boxed adjunction','H=G_m'),('display','lower middle','Ext_X^i(f*(G),G_m) ≃ Ext_Y^i(G,Pic^•)'),('insertion','under f*','R'),('margin note','above circled Pic term','les supérieurs'),('deletion','under left Ext','RΓ(X,'),('drawing','between displays','two pairs of downward strokes'),('display','long lower box','G affine, alors H^i ⇐ Ext'),('deletion','before Ext in long box','E'),('display','lower right, three rows','i=0; i=1; i=2'),('deletion','i=0, i=1 rows','Hom; Ext'),('margin note','under ≠ row','!'),('drawing','under three rows','horizontal separating stroke'),('text','bottom left','G abélien, alors'),('deletion','after alors','H'),('display','bottom right','H^(i−1)(X,G′) ⇐ Ext'),('display','bottom edge','i=0: 0→0; i=1: H⁰(X,G′)='),('margin note','bottom left','42')]
d=[{'line':'top below H¹','reading':'pt singuliers','alternatives':'pt singulier; ending not distinct','confidence':'medium'},{'line':'boxed adjunction, complex arguments','reading':'G_•; H^•','alternatives':'dots occupy different heights; not normalized to uniform superscripts','confidence':'medium'},{'line':'above circled Pic^•','reading':'les supérieurs','alternatives':'abbreviated compressed final word','confidence':'low'},{'line':'insertion under f* and nearby deletion','reading':'R; RΓ(X,','alternatives':'overwriting makes both uncertain','confidence':'low'},{'line':'boxed G affine formula, right degrees','reading':'Ext^i; Pic^(q)','alternatives':'Pic^(1); Ext superscript indistinct','confidence':'low'},{'line':'i=2 far-right term at page edge','reading':'underlined Pic^(2)_X','alternatives':'rightmost index partly cut by page edge; no missing continuation supplied','confidence':'low'},{'line':'last displayed spectral expression','reading':'H^(i−1); Ext^p_g','alternatives':'H^(i+j); Ext indices compressed','confidence':'low'}]
save(43,tex,e,d,'Several candidate dualities are stated without hypotheses/proofs, with a shift emerging only in the last formula. The degree-two affine line explicitly has ≠ and a separate exclamation mark; this is not an equality or an established direct-sum decomposition. Both f^! and f_! have visible exclamation dots, whereas f* appears in the subsequent boxed expression. Dotted Pic, its encircling, “les supérieurs”, and the final double-left arrows are possible derived/spectral-sequence leads, not permission to correct the indices. The two loop drawings may relate to the top note “pt singuliers” but have no explicit labels establishing their meaning.')
