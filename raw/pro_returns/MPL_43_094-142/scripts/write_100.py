from page_work import save_page
text=r'''\scanpage{100}
\margin{$S\gamma=(D\Delta\gamma_K)(1)$}
\[
\underset{\sim}{\operatorname{Ext}}^i_{K/k}(G,S\underline\gamma)
\xrightarrow{\sim}
\underset{\sim}{\operatorname{Ext}}^{i\unsure{*}}_{k\text{-gr}}
(\Gamma^{\deleted{\unsure{*}}}G^*,\unsure{\gamma})
\]
isom si $G$ \uline{affine} sans \unsure{composantes} $G_a$
\[
\underset{\sim}{\underline{\operatorname{Ext}}}^{i}_{K/k}(G,S\gamma)
\longrightarrow
\underset{\sim}{\underline{\operatorname{Ext}}}^{2i}(\Gamma^*G,\gamma)
\]
pour
\[
\underline{\operatorname{Ext}}^i_{K/k}(G,S\gamma)
\longrightarrow \underline{\operatorname{Ext}}^i
\]
\margin{\deleted{$\unsure{\Gamma}_{K/k}G$}\quad $R^*f_{K/k}$}

\noindent 1) $K$-\uline{groupes algébriques}.
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
 & \text{nul pr }i>2\arrow[d,dash,bend right] & \\
\operatorname{Ext}\arrow[d,dash] &
\underline{\operatorname{Ext}}\arrow[d] & H^p\arrow[d]\\
\begin{gathered}\text{nature arithmétique}\\\text{ie ``globale''}\end{gathered} &
\begin{gathered}\text{nature}\\\text{géom.}\end{gathered} &
\begin{gathered}\text{nature arithmétique}\\\text{ie. ``globale''}\end{gathered}
\end{tikzcd}}
\uline{de $K$-groupes algébriques}

\noindent 2) \uline{Dualité de Cartier}. Extension aux
$\unsure{\mathcal K|\mathcal R}\operatorname{Gr}_K$

\margin{\figure{\begin{tikzpicture}\draw (0,0)--(.4,.25);\draw (.02,-.04)--(.42,.21);\end{tikzpicture}}}
\noindent 3) \unsure{Quasi-groupes} algébriques, leurs
$\operatorname{Ext},\underline{\operatorname{Ext}},H^p$

\noindent 4) \uline{Dualité de Serre-\unsure{Pontrjagin}}

\noindent 5) Le foncteur $\underline\Gamma_{K/k}$
\inserted{de Néron-\unsure{Weil}}

\margin{\figure{\begin{tikzpicture}\draw (0,0)--(.4,.25);\draw (.02,-.04)--(.42,.21);\end{tikzpicture}}}
\noindent 6) Les foncteurs \deleted{$\unsure{\Gamma}_{K/k}$}
\[
\underset{\sim}{\underline{\operatorname{Ext}}}^{*}_{K/k}(F,G),
\quad\underset{\sim}{\underline H}^{*}_{K/k}(G)
\]
\inserted{\[
E^*_{K/k}(F,G)\qquad E_{K/k}(G)
\]}
\margin{nul pr $i>3$}

\noindent 7) L'hom. fondamental.

\margin{\figure{\begin{tikzpicture}\draw (0,0)--(.4,.12);\draw (.02,-.04)--(.42,.08);\end{tikzpicture}}}
\noindent 8) Le th. de dualité.
\mspage{99}
'''
save_page(100,text,[('margin note','top left loop with line toward top formula','S gamma=(D Delta gamma K)(1)'),('display','top','Ext i K/k(G,S gamma) to Ext i star k-gr'),('deletion','top formula above Gamma','star'),('text','upper','isom si G affine sans composantes G a'),('display','upper middle','Ext i K/k to Ext 2i'),('text','middle','pour'),('display','middle incomplete formula','Ext i K/k(G,S gamma) to Ext i'),('margin note','left middle','Gamma K/k G; R star f K/k'),('deletion','left middle','Gamma K/k G'),('text','lower item 1','K-groupes algébriques'),('diagram','lower item 1 annotations','Ext; underlined Ext; H p; nature'),('text','lower item 2','Dualité de Cartier'),('text','lower item 3','Quasi-groupes algébriques'),('drawing','left item 3','double oblique strokes'),('text','lower item 4','Dualité de Serre-Pontrjagin'),('text','lower item 5','Le foncteur Gamma K/k'),('insertion','beside item 5 bracketed','de Néron-Weil'),('text','lower item 6','Les foncteurs'),('deletion','item 6 before Ext','Gamma K/k'),('display','item 6','Ext star K/k(F,G); H star K/k(G)'),('insertion','beneath item 6 formulas','E star K/k(F,G); E K/k(G)'),('margin note','above right item 6','nul pr i>3'),('drawing','left items 5–6','double oblique strokes'),('text','bottom item 7','L’hom. fondamental'),('text','bottom item 8','Le th. de dualité'),('drawing','left item 8','double oblique strokes'),('text','bottom middle page number','99')],observations='Full sheet and both halves examined. Extra crops resolve the arithmetic/geometric annotation words and top altered exponents. Wavy underlining is retained as an underset tilde, independently of the straight underline. The first top exponent placement G star versus Gamma star is transcribed from its visible placement with the overwritten earlier star retained. Final Ext formula is unfinished on the sheet.')
