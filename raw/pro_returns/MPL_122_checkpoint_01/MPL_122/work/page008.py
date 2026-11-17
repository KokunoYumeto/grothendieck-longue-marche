from record import save
save(8,r'''
\scanpage{8}
\begin{center}- 44 -\end{center}
\hfill n$^\circ$ 387

mais que $K_{\unsure{o|0}}$ n'est pas linéairement compact (cf. § 10, exerc. 2).

6) a) Soient $A$ un anneau de valuation, $M$ un $A$-module, $M'$ un sous-module de $M$. Montrer que pour que $M'$ soit un sous-module \uline{pur} de $M$ (chap. I, § 2, exerc. 24), il faut et il suffit que pour tout $\alpha\in A$, on ait $M'\cap(\alpha M)=\alpha M'$.

b) Soit $M'$ un sous-module pur de $M$, tel que si on munit $M'$ de la topologie dont les $\alpha M'$ (où $\alpha\in A$, $\alpha\ne0$) forment un système fondamental de voisinages de $0$, $M'$ soit linéairement compact. Montrer que pour tout élément $x\in M$, il existe un $y'\in M'$ tel que $x'=x+y'$ ait la propriété suivante : pour tout $\alpha\in A$ tel que $x+M'\in\alpha(M/M')$, on a $x'\in\alpha M$. (Pour chacun des $\alpha\in A$ tels que $x+M'\in\alpha(M/M')$, considérer la partie $S_\alpha$ de $M'$ formée des $y'_\alpha$ tels que $x+y'_\alpha\in\alpha M$).

c) On suppose que $A$ soit un anneau de valuation linéairement compact ; soit $K$ le corps des fractions de $A$. Montrer que si $M$ est un $A$-module sans torsion tel que $M_{(K)}$ admette une base dénombrable, $M$ est somme directe d'une famille dénombrable de $A$-modules de rang 1. (Considérer $M$ comme réunion d'une suite croissante $(M'_i)$ de sous-modules purs tels que $M'_i$ soit de rang $i$, et pour chaque $i$, appliquer b) à $M'_i$ et à son sous-module $M'_{i-1}$).

d) Les hypothèses sur $A$ et $M$ étant les mêmes que dans c), soit $N$ un sous-module pur de $M$, de rang fini. Montrer que $N$ est facteur direct de $M$ (observer que tout $A$-module qui est somme directe d'un nombre fini de $A$-modules de rang 1 est linéairement compact et utiliser b)).

e) Les hypothèses sur $M$ et $M'$ étant celles de b), montrer que pour tout $x\in M$, il existe $y'\in M'$ tel que l'annulateur de $x'=x+y'$ soit égal à l'annulateur de l'élément $x+M'\in M/M'$. (Soit $\underline a$ l'annulateur de $x+M'$ ; pour tout $\alpha\in\underline a$, soit $T_\alpha$ la partie de $M'$ formée des $y'$ tels que $\alpha(x+y')=0$, et montrer que l'intersection des $T_\alpha$ n'est pas vide).

f) On suppose que $A$ soit un anneau de valuation tel que pour tout idéal $\underline a\ne0$, le $A$-module $A/\underline a$ soit linéairement compact (pour la topologie discrète). Montrer que tout $A$-module de torsion de type fini $M$ est somme \unsure{directe.d'un|directe d'un} nombre fini de $A$-modules monogènes. (Si $(z_i)_{1\le i\le n}$ est un système de générateurs de $M$, raisonner par récurrence sur $n$, en considérant un des $z_i$ dont l'annulateur est le plus petit et en remarquant que le sous-module de $M$ qu'il engendre est pur).
\mspage{7}
''',[
('text','top centre','- 44 -'),('text','top right','n° 387'),('text','upper','mais que K_o n’est pas'),('text','upper','6) a) Soient A un anneau de valuation'),('text','upper middle','b) Soit M prime un sous-module pur'),('text','middle','c) On suppose que A soit'),('text','middle lower','d) Les hypothèses sur A et M'),('text','lower','e) Les hypothèses sur M et M prime'),('text','bottom','f) On suppose que A soit'),('text','bottom left','7')],
[('first line','K_o','K_0; circular subscript indistinguishable in type.','medium'),('6 f)','directe.d’un','The dot may be an accidental mark rather than punctuation.','medium')],
['Reused typescript p.44 n°387, valuation-module exercises 6 a–f.'],sheet_kind='reused_typed')
