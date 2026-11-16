from page_work import save_page
text=r'''\scanpage{110}
IV 7 Oubli au n\textsuperscript{o} 7.6.

\uline{Proposition} 6.7. Soient $f:X\longrightarrow Y$ un morphisme
\deleted{de présentation finie} \deleted{et} propre,
\inserted{avec $Y$ loc. noeth.,}
$F$ un Module \deleted{de présentation finie} \inserted{cohérent}
sur $X$. \inserted{de support $X$,} Pour tout $y\quad Y$,
Soit $\ell(y)$ la somme des \deleted{long} multiplicités \deleted{tota}
géométriques totales \inserted{sur $k(y)$} de
$F_y$ en les points maximaux de $\operatorname{supp}F_y$.
\inserted{On suppose $f$ univ. ouvert en les pts maximaux de $X_{y_0}$,
et $F_{y_0}$ sans \unsure{idéaux} premiers ass. immergés}
Alors la fonction $\unsure{z|y}\mapsto\ell(\unsure{z|y})$ sur
$Y$ est semi-continue supérieurement\inserted{en $y_0$}.
\margin{?}

Le procédé breveté nous ramène au cas où $Y$ est noethérien. On sait
(réf) que la fonction $\ell$ est constructible, il reste donc (réf) à prouver
que $y\in\overline{y'}$ implique $\ell(y)\geq\ell(y')$. Le procédé habituel nous permet
alors de nous ramener au cas où $Y$ est le spectre d'un anneau de valuation
discrète, dont $y$ ($y'$) est le point fermé (générique), et \deleted{\unsure{à prouver}}
à prouver dans ce cas l'inégalité correspondante sur les longueurs:

\uline{Lemme} 6.8. Soit $f:X\quad Y$ un morphisme propre, avec $Y$ spectre d'un anneau
de valuation discrète, $F$ un Module cohérent sur $X$, \inserted{de support $X$,}
$F_0$ et $F_1$ les \deleted{fibr}
Modules induits sur la fibre spéciale resp. la fibre générique, $x_i$
($x'_j$) les points maximaux de $\operatorname{supp}F_0$ ($\operatorname{supp}F_1$).
\inserted{(Supposons que tt comp. de $X$ domine $Y$ et $F_0$ soit $(S_1)$.)}
Alors on a
\[
\operatorname{long} F_{0\,x_i}\unsure{\geq|>}\sum_i\operatorname{long}F_{1\,x'_j}
\]
Si l'inégalité est vérifiée, alors $F$ est plat sur $Y$ aux points \deleted{\unsure{génériques}}
maximaux de $\operatorname{supp}F_0$, \deleted{donc toute composante de $\operatorname{supp}F$ domine $Y$,}

Soit $t$ une uniformisante pour $V=\underline O_{Y,y}$, soit $N$ le sous-Module
de $F$ réunion des annulateurs des $t^n$, donc on a une suite exacte
\[
0\mathrel{-}N\mathrel{-}F\mathrel{-}G\mathrel{-}0
\]
d'où une suite exacte (grâce au fait que $t$ est $G$-régulier):
\[
0\mathrel{-}N/tN\mathrel{-}F/tF\mathrel{-}G/tG\mathrel{-}0
\]
\unsure{Qela|Cela} montre que les deux sommes \deleted{pour} relatives à $F$ qu'il s'agit de
comparer, s'obtiennent en ajoutant les sommes analogues pour $N,G$.
Comme $N_1=0$, pour prouver notre inégalité, il suffit donc de
prouver l'inégalité analggue pour $G$; et on ne peut avoir égalité
que si $N/tN$ \deleted{est} $=N_0$ est nul aux points maximaux de $\operatorname{supp}$
\unsure{$\cdots$}

\margin{\figure{\begin{tikzpicture}[x=.5cm,y=.5cm]
\draw (0,0)..controls(-.1,2)and(.3,9)..(.9,11);
\draw (4,-1)..controls(4.7,1)and(3.5,8)..(6,15);
\draw (8,0)..controls(8.5,3)and(6.8,7)..(7.5,12);
\end{tikzpicture}}}

\margin{N.B. J'ignore si les assertions sont vraies si on ne
suppose pas déjà $F$ plat$/Y$ aux pts maximaux
de $X_y$. Question liée: $A$ anneau local noeth., $M$ module de
type fini sur $A$, $t\in A$, $\unsure{t\notin\mathfrak p}$\deleted{\unsure{minimal}} pour tt $\mathfrak p$ associé,
on suppose $\operatorname{supp}M=\operatorname{Spec}A$, $\dim\unsure{A/\mathfrak p_0}=1$,
prouver $\mathfrak m\in\operatorname{Ass}M/tM$ !}
\mspage{109}
'''
save_page(110,text,[('text','top title','IV 7 Oubli au no7.6'),('text','upper proposition','Proposition6.7 Soient f:X→Y'),('deletion','proposition first condition','de présentation finie'),('deletion','proposition second line','et'),('insertion','proposition second line above','avec Y loc. noeth.'),('deletion','module hypothesis','de présentation finie'),('insertion','module hypothesis','cohérent'),('insertion','after sur X','de support X'),('deletion','multiplicities first overtype','long'),('deletion','multiplicities second overtype','tota'),('insertion','above totales de','sur k(y)'),('insertion','top right with reference marks','On suppose f univ. ouvert ... sans idéaux premiers ass. immergés'),('insertion','end proposition','en y0'),('margin note','left proposition','?'),('text','upper middle proof','Le procédé breveté nous ramène'),('deletion','right edge proof','à prouver'),('text','middle lemma','Lemme6.8 Soit f:X Y'),('insertion','after coherent sur X','de support X'),('deletion','lemma before Modules','fibr'),('insertion','between lemma lines bracketed','Supposons que tt comp. de X domine Y et F0 soit S1'),('display','lemma inequality','long F0 xi >= sum i long F1 xprimej'),('text','lemma consequence','Si l’inégalité est vérifiée'),('deletion','right edge consequence','génériques'),('deletion','end consequence','donc toute composante de supp F domine Y'),('text','lower proof','Soit t une uniformisante'),('display','first exact sequence','0 - N - F - G - 0'),('text','between exact sequences','d’où une suite exacte'),('display','second exact sequence','0 - N/tN - F/tF - G/tG - 0'),('text','bottom proof','Qela montre que les deux sommes'),('deletion','bottom proof overtype','pour'),('deletion','bottom proof equality','est'),('drawing','over typed text','three long vertical oblique strokes'),('margin note','bottom handwritten','N.B. J’ignore si les assertions sont vraies'),('deletion','bottom note regularity word','minimal'),('text','bottom left page number','109')],sheet_kind='reused_typed',observations='Whole and both halves read, with enlarged top-right and lower handwritten additions. Typed blanks in Pour tout y Y and f:X Y have not been supplied with absent relation signs. Typed analggue is retained. The exact-sequence connectors have no visible heads. Three long overlying strokes are reproduced; local word cancellations are marked separately. The lower N.B. explicitly expresses uncertainty. The handwritten additions and formula index remain marked where weak.')
