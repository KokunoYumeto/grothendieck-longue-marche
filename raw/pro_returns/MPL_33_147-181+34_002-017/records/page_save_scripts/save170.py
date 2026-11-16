import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,170,r'''\scanpage{170}
Énoncés plausibles (sur préschéma excellent de dim finie).
\diagram{$\underline{D}_X\left\{\begin{array}{l}
\underline{D}_c(X)^o\simeq\underline{D}_c(X)\\
\underline{D}_c^-(X)^o\xrightarrow{\sim}\underline{D}_c^+(X)\\
\underline{D}_c^+(X)^o\simeq\underline{D}_c^-(X)\\
\underline{D}_c^b(X)\simeq\underline{D}_c^b(X)
\end{array}\right.$}

$F_\bullet\in\operatorname{Ob}\underline{D}_c^-(X)$, \inserted{$G^{\bullet}=\underline{D}_X(F_\bullet)\in\operatorname{Ob}\underline{D}_c^+(X)$} je dis que
\[
(1)\qquad F_\bullet\text{ de Tor-dim finie}\Longleftrightarrow G^{\bullet}\text{ de pseudo dim. inj. finie}
\]
\margin{[i.e. \inserted{$\exists N$ tel que} pour tt \deleted{$\unsure{G_P}$} $P$ \deleted{$\in\operatorname{Ob}\underline{D}_c$}\inserted{faisceau} constructible, $\operatorname{Ext}^i(P,G^{\bullet})=0$ pour $i>N$]}
\margin{(**)}
\diagram{\begin{tikzcd}[row sep=small]
\text{pour }i>N\arrow[d,leftrightarrow]\\
\text{fibres géom. }G^{\bullet}_{\bar{x}}\text{ est de dim. inj. finie}\\
\text{(pour les }A\text{-Modules)}
\end{tikzcd}}

\uline{N.B.} Si $X$ de dim abs. finie \unsure{on a} pour $G^{\bullet}$ donné ; $G^{\bullet}$ pseudo-dim. inj. finie $\Longleftrightarrow G^{\bullet}$ de dim. injective finie

Dém. de (1). L'implication $\longrightarrow$ formelle, en utilisant que $R_X^{\bullet}$ est de pseudo-dim. injective finie, et
\[
\mathrm{R}\mathcal{H}om^{\bullet}(P_\bullet,\underline{D}_X(F_\bullet))
=\mathrm{R}\mathcal{H}om^{\bullet}(P_\bullet,\mathrm{R}\mathcal{H}om^{\bullet}(F_\bullet,R_X^{\bullet}))
\simeq\mathrm{R}\mathcal{H}om^{\bullet}(P_\bullet\overset{\mathrm L}{\otimes}F_\bullet,R_X^{\bullet})
\]
Pour l'implication inverse, utiliser la bidualité pour $F_\bullet\overset{\mathrm L}{\otimes}P$ ----

\uline{NB.} Si les fibres géom $A_{\bar{x}}$ sont Gorenstein, alors en admettant l'équivalence (**), on voit que si $F_\bullet\in\operatorname{Ob}\underline{D}_c(X)$ Tor-dim finie $\Longleftrightarrow$ pseudo-dim inj. finie, et $\underline{D}_X$ induit une anti-autoequivalence dans la catégorie desdits complexes ...
\margin{169}
''',[
('text','heading','Énoncés plausibles'),('diagram','upper left','D_X bracket four derived category equivalences'),('text','upper middle','F in Ob D_c minus, je dis que'),('insertion','above je dis que','G=D_X(F) in Ob D_c plus'),('display','middle','(1) Tor dimension iff pseudo injective dimension'),('margin note','right middle','i.e. Ext vanishing definition'),('insertion','definition','exists N tel que'),('deletion','definition','G_P'),('deletion','definition','in Ob D_c'),('insertion','definition','faisceau'),('margin note','middle left','(**)'),('diagram','right middle','equivalence to geometric fibre injective dimension'),('text','middle lower','N.B. Si X de dim abs. finie'),('text','lower','Dém. de (1)'),('display','lower','RHom adjunction chain'),('text','lower','Pour l’implication inverse'),('text','bottom','NB. Si les fibres géom A_xbar sont Gorenstein'),('margin note','bottom left','169')],remarks='Whole, halves and enlarged definition/NB/bottom read. Scan169 is absent as instructed; this supplied page is scan170 with archival pencil169. Heading explicitly says plausible. The fourth category line has no visible opposite-category o; retained. The equivalence (**) is expressly admitted at the bottom, and the converse proof is only an instruction to use biduality. Figure/definition overlap is represented by the marginal definition and a vertical equivalence diagram; the short endpoint phrase is repeated to retain the visible attachment, not a new proposition.')
