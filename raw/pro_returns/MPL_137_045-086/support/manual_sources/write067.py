import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{67}
% archive foliation: 66
NB $F(\mathbf1_{B'})$ devient donc un ``objet-\deleted{$(k)$}anneau'' de $B$ (``$k$-Algèbre'' quand il y a un $k$)

$F$ transforme ``anneaux'' de $B'$ en ``anneaux'' de $B$, en respectant les propr$^{\unsure{s}}$ d'unité, associativité et commutativité.

Les $F$ en question forment une catégorie. Si on a $B'',B',B$, ils se composent, d'où $2$-catégorie des $\otimes$-catégories $k$-additives.

\uline{Supposons maintenant que} $B'=\unsure{K_*|K}$ (catégorie dans laquelle se trouvent \unsure{ttes} nos résolutions injectives).

Un foncteur $k$-lin.
\[
K\xrightarrow{F}B
\]
s'identifie alors à un $C\in B^\bullet$. Donc on sait ce qu'il faut entendre par ``structure multiplicative sur le complexe de cochaînes $C^\bullet$'' de $B$ (on dira: str. mul. demi-simpliciale'' pour ne pas prêter à confusion).'''
e=[('text','top','NB F(1B′) devient donc un objet-anneau'),('deletion','top','(k)'),('text','upper third','F transforme anneaux de B′'),('text','middle','Les F en question forment une catégorie'),('text','lower middle','Supposons maintenant que B′=K*'),('text','lower','Un foncteur k-lin.'),('display','lower','K→B, F'),('text','bottom','s’identifie alors à un C∈Bbullet')]
save(67,text,e)
