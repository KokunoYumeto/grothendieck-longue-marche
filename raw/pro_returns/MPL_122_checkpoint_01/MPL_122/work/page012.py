from record import save
save(12,r'''
\scanpage{12}
\margin{\unsure{W|11}}
\begin{center}- 46 -\end{center}
\hfill n$^\circ$ 387

de $A$-modules isomorphes, soit à $K$, soit à $K/A$ (\uline{Alg.}, chap. VII, § 2, exerc. 3). En outre, tout $A$-module monogène est isomorphe à un sous-module de $K/A$. On appelle \uline{dual torique} (\uline{algébrique}) d'un $A$-module $M$ le $A$-module $\operatorname{Hom}_A(M,K/A)$, que l'on note $M^*$ ; l'application canonique $c_M:M\longrightarrow M^{**}$ est injective (\uline{Alg.}, chap. II, 3$^{\mathrm e}$ éd., § 2, exerc. 13 b)). Pour tout sous-module $N$ de $M$, le sous-module $N^\circ$ de $M^*$ formé des $u$ tels que $u(x)=0$, est appelé l'\uline{orthogonal} de $N$ dans $M^*$ ; le dual de $M/N$ s'identifie canoniquement à $N^\circ$ et le dual de $N$ à $M^*/N^\circ$. Le dual torique d'une limite inductive $\varinjlim M_\alpha$ est canoniquement isomorphe à la limite projective $\varprojlim M_\alpha^*$.

a) On sait que les $A$-modules de rang un (\uline{Alg.}, chap. VII, § 4, exerc. 22) sont isomorphes à un module de l'une des formes $A$, $K$, $K/A$ ou $A/\pi^h A$. Montrer que les duals toriques algébriques de $K$ ou de $A/\pi^h A$ leur sont respectivement isomorphes, que le dual torique de $A$ est isomorphe à $K/A$ et que celui de $K/A$ est isomorphe à $A$ (on utilisera la connaissance des sous-$A$-modules de $K$ et le fait que $A$ est complet (pour le dual de $K/A$)). En déduire que pour tout $A$-module $M$ de rang fini, $M^*$ est un module de même rang et que l'homomorphisme canonique $c_M$ est bijectif.

b) Soient $M$ un $A$-module, $N$ un sous-module de rang fini de $M$. Montrer que l'orthogonal de $N^\circ$ dans $M^{**}$ s'identifie (par $c_M$) à $N$ (utiliser a)).

c) Montrer qu'un $A$-module qui est noethérien (resp. artinien) est de rang fini (plonger $M$ dans son enveloppe injective (\uline{Alg.}, chap. II, 3$^{\mathrm e}$ éd., § 2, exerc. 18)) $M^*$ est alors artinien (resp. noethérien).

d) On désigne par $\sigma(M^*,M)$ la topologie (sur $M^*$) de la convergence simple dans $M$ ($K/A$ étant muni de la topologie discrète). Montrer que si $N$ est un sous-module de $M$, $\sigma(N^\circ,M/N)$ est induite sur $N^\circ$ par $\sigma(M^*,M)$, et que $\sigma(M^*/N^\circ,N)$ est quotient par $N^\circ$ de la topologie $\sigma(M^*,M)$. (Pour le second point, on notera que si $P$ est un sous-module de $M$ tel que $N\subset P\subset M$, le dual de $P/N$ s'identifie à $N^\circ/P^\circ$). Si $M=\varinjlim M_\alpha$ la top ologie $\sigma(M^*,M)$ est limite projective des topologies $\sigma(M_\alpha^*,M_\alpha)$.

e) Les topologies $\sigma(K,K)$ et $\sigma(A,K/A)$ sont les topologies $\pi$-adiques ; les topologies $\sigma(A/\pi^h A,A/\pi^h A)$ et $\sigma(K/A,A)$ sont les topologies discrètes. En déduire que pour tout $A$-module $M$, le module $M^*$, muni de $\sigma(M^*,M)$ est \uline{linéairement compact} (chap. III, § 2, exerc. 15 ; on considérera $M$ comme module quotient d'un $A$-module libre).
''',[
('margin note','top right','W or 11'),('text','top centre','- 46 -'),('text','top right','n° 387'),('text','upper','de A-modules isomorphes; dual torique'),('text','upper middle','a) On sait que les A-modules de rang un'),('text','middle','b) Soient M un A-module'),('text','middle','c) Montrer qu’un A-module'),('text','lower middle','d) On désigne par sigma'),('text','lower','e) Les topologies sigma')],
[('pencil upper-right','W','11; the mark resembles a W rather than two digits, so retained as a marginal mark.','low'),('d, final sentence','top ologie','Visible internal space retained.','high'),('orthogonal notation','N circle','Small round exponent, not silently converted to zero.','high')],
['Reused typescript p.46 n°387, continuation of scan004 exercise9; algebraic toric duality and linearly compact topology.','Potential conceptual parallel to duality notes, but reused substrate is not evidence of intentional connection.'],sheet_kind='reused_typed')
