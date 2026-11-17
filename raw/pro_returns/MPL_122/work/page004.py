from record import save
save(4,r'''
\scanpage{4}
\begin{center}- 45 -\end{center}
\hfill n$^\circ$ 387

7) Soient $K$ un corps, $v$ une valuation discrète sur $K$ tel que $K$ soit \uline{complet} pour $T_v$ ; on désigne par $A$ et $\underline p$ l'anneau et l'idéal de $v$, par $U=A-\underline p$ l'ensemble des éléments inversibles de $A$. Soit $u$ un isomorphisme de $K$ sur un sous-corps de $K$.

a) Montrer que l'on a $u(\underline p)\subset A$ et $u(U)\subset U$. (Pour prouver le premier point observer pour tout $z\in\underline p$, l'équation $x^n=1+z$ admet une solution dans $A$ pour tout $n>0$, en utilisant le lemme de Hensel ; si on avait $v(u(z))<0$, en déduire que l'entier $v(u(z))$ devrait être divisible par tout entier $n>0$. Déduire alors la seconde assertion de la première).

b) Déduire de a) que, ou bien $u(K^*)\subset U$, ou bien $u$ est continu (considérer l'image par $u$ d'une uniformisante de $v$).

c) Donner un exemple de corps algébriquement clos $\Omega$ tel qu'en prenant $K=\Omega((X))$, $K$ soit isomorphe à un sous-corps de $K$ contenu dans $U\cup\{0\}$ (cf. \uline{Alg.}, chap. V, § 5, exerc. 13).

8) a) Soient $K$ un corps, $v$ une valuation de hauteur 1 sur $K$, $A$ son anneau. Soient $H$ une partie compacte de $K$ (pour la topologie $T_v$) $a\ne0$ un point de $K$. Montrer qu'il existe un polynôme $f\in K[X]$ sans terme constant et tel que $f(a)=1$, $f(H)\subset A$. (Prouver qu'on peut prendre pour $f$ un polynôme de la forme
\[
1-(1-a^{-1}X)(1-c_1^{-1}X)^{n(1)}\ ..\ (1-c_r^{-1}X)^{n(r)}
\]
où les $c_i$ sont des éléments de $H$ tels que $v(c_i)<v(a)$, convenablement choisis, et les $n(i)$ des entiers $>0$ assez grands).

b) Soit $X$ un espace compact totalement discontinu ; on munit l'anneau $C(X;K)$ des applications continues de $X$ dans $K$ de la topologie de la convergence uniforme. Soit $B$ un sous-anneau de $C(X;K)$ contenant les constantes et séparant les points de $X$ ; montrer que $B$ est dense dans $C(X;K)$ (utiliser a) et \uline{Top. gén.}, chap. X, 2$^{\mathrm e}$ éd., § 4, exerc. 21 b)).

9) Soient $A$ un anneau de valuation discrète, $\pi$ une uniformisante de $A$, $K$ le corps des fractions de $A$ ; on suppose $A$ \uline{complet} pour la topologie $\pi$-adique. Les $A$-modules injectifs (\uline{Alg.}, chap. II, 3$^{\mathrm e}$ éd., § 2, exerc. 11) sont identiques aux $A$-modules divisibles (\uline{Alg.}, chap. VII, § 2, exerc. 3) et sont sommes directes
\mspage{3}
''',[
('text','top centre','- 45 -'),('text','top right','n° 387'),('text','upper','7) Soient K un corps'),('text','upper middle','a) Montrer que l’on a'),('text','middle','b) Déduire de a)'),('text','middle','c) Donner un exemple'),('text','lower middle','8) a) Soient K un corps'),('display','lower middle','1-(1-a^-1 X)(1-c_1^-1 X)^n(1)'),('text','lower middle','où les c_i sont des éléments'),('text','lower','b) Soit X un espace compact'),('text','bottom','9) Soient A un anneau'),('text','bottom left','3')],
[('7, throughout','underlined p','Underline preserved literally; no conversion to Gothic type.','high'),('8 polynomial display','two dots between factors','Two printed dots are visible, not silently changed to three.','high'),('pencil lower-left number','3','Attribution of pencil foliation to Grothendieck is not established.','medium')],
['Reused typescript: printed p.45, n°387; exercises 7–9, final sentence continues.','Do not infer that the valuation problems belong to the handwritten argument.'],sheet_kind='reused_typed')
