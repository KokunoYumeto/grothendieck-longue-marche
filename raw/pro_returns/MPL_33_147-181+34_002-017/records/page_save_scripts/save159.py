import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,159,r'''\scanpage{159}
\mspage{4.}
\margin{158}
\uline{les} $j_\alpha$ \uline{sont des immersions ouvertes dont les images recouvrent} $Z$ (ceci est bien une prétopologie). \uline{Cette topologie s'appelle la} topologie de Zariski \uline{sur} $(\mathrm{Sch})_{/X}$ \uline{et le site correspondant sera noté} $(\mathrm{Sch}/X,\mathrm{Zar})$. \uline{Toute notion associée à ce site sera qualifiée ``de Zariski''} (faisceaux, cribles couvrants etc. )

\uline{Remarque.} -- Si $Z\longrightarrow X$ est un morphisme dans $(\mathrm{Sch})$, nous avons $(\mathrm{Sch})_{/Z}=(\mathrm{Sch})_{/X}\big/ Z/X$ et la topologie sur $(\mathrm{Sch})_{/X}$ que nous venons de construire induit bien la topologie analogue sur $(\mathrm{Sch})_{/Z}$. En particulier, on voit en prenant $X=\operatorname{Spec}(\mathbb{Z})$ que le site $(\mathrm{Sch},\mathrm{Zar})$ détermine les sites $(\mathrm{Sch}/Y,\mathrm{Zar})$, $Y\in(\mathrm{Sch})$.

\uline{Démonstration de la proposition 1.}-- Il suffit de montrer que les deux conditions suivantes sur $F\in\widehat{(\mathrm{Sch})_{/X}}$ sont équivalentes:

(i) Pour tout $Z/X\in(\mathrm{Sch})_{/X}$, $i_{Z\unsure{*|\bullet}}(F)\in\widetilde{\mathrm{Ouv}(Z)}$

(ii) Pour chaque $Z/X$ et pour chaque famille couvrante $\{Z_\alpha\longrightarrow Z\}$ de $Z/X$ la suite
\diagram{\begin{tikzcd}
(1)\quad F(Z)\arrow[r]&\displaystyle\prod_\alpha F(Z_\alpha)\arrow[r,shift left]\arrow[r,shift right]&\displaystyle\prod_{\alpha,\beta}F(Z_\alpha\mathop{\prod}\limits_Z Z_\beta)
\end{tikzcd}}
est exacte.

D'abord il est clair que (ii) $\Longrightarrow$ (i). Car si $U$ est un ouvert de l'espace topologique sous-jacent à $X$ et $\{U_\alpha\}$ un recouvrement de $U$ par des ouverts, il est clair que les $(\mathrm{Sch})_{/X}$-morphismes $i_Z(U_\alpha)\longrightarrow i_Z(U)$ sont des immersions ouvertes dont les images recouvrent $i_Z(U)$. De plus, nous avons un isomorphisme évident entre $i_Z(U_\alpha)\mathop{\prod}\limits_{i_Z(U)} i_Z(U_\beta)$ et $i_Z(U_\alpha\cap U_\beta)$. Comme $(i_{Z\unsure{*|\bullet}}F)(U)=F(i_Z(U))$, un $F$ qui satisfait à (ii) vérifie bien (i).

Soit d'autre part $F$ un préfaisceau avec la propriété (i) et démontrons (ii). Comme les $Z_\alpha\xrightarrow{j_\alpha}Z$ sont des immersions ouvertes on peut les factoriser : $Z_\alpha\longrightarrow j_\alpha(Z_\alpha)\hookrightarrow Z$ où le premier morphisme est un isomorphisme de préschémas et où $j_\alpha(Z_\alpha)$ est le préschéma induit sur un ouvert de $Z$. Il est facile de voir que la suite (1) est exacte si et seulement si la suite analogue pour la famille $\{j_\alpha(Z_\alpha)\longrightarrow Z\}$ l'est. Or ceci est
''',[
('text','upper right','4.'),('margin note','archival edge','158'),('text','top','les j_alpha sont des immersions ouvertes'),('text','upper middle','Remarque. Si Z to X'),('text','middle','Démonstration de la proposition 1'),('text','middle','(i) Pour tout Z/X'),('text','middle','(ii) Pour chaque Z/X'),('diagram','middle','(1) F(Z) to product F(Z_alpha), parallel arrows'),('text','middle','est exacte'),('text','lower middle',"D'abord il est clair"),('text','lower',"Soit d'autre part F")],sheet_kind='reused_typed',remarks='Original whole, upright whole, and both upright halves read. The handwritten fiber-product glyph is a product sign (not a cross) and is retained as prod_Z. The small mark on i_Z is indistinct between * and a dot; registered explicitly. The phrase says espace ... sous-jacent à X even though subsequent indices are Z.')
