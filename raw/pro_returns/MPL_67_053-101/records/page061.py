import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{61}
\deleted{\unsure{4}}
% archive foliation: 63
b) Recollement de $\overline H$ à lui-même suivant
un isom. rectifiable $[0,1]\xrightarrow{\sigma}[-1,0]$ \inserted{$(\sigma(0)=0)$},
regardé au voisinage du pt 0.

\margin{\uline{12.1}\quad\deleted{\unsure{a)}} c) Soit $C$ une
courbe rectifiable dans \deleted{\unsure{un voisinage de}}\inserted{un ouvert} $U$,
\deleted{\unsure{image de}} $\unsure{\mathbb C}$,
toute \deleted{\unsure{application}} fonction \inserted{complexe}
continue sur $U$ qui est
\unsure{analytique|continue} dans $U\setminus C$, \unsure{est en}
fait holomorphe dans $U$.}

\textcircled{4} \uline{Recollements \deleted{bord à bord}\inserted{des disques}}.
\margin{Le recollement ``bord à bord''}
Cela correspond,
dans le th. 4, au cas où $K$ est une
variété \inserted{(compacte)} de dim 1, $S=\varnothing$. \deleted{Il} Pour avoir
``des \unsure{esp.} de modules'', il est naturel
de dégager des conditions restrictives
naturelles sur l'involution $\sigma$ de
$\delta\widetilde X$.

Pour ceci, \deleted{\unsure{rapp}} on se rappelle que
pour une surface conforme à bord $X$
\inserted{(au lieu de $\widetilde X$)}, et une comp. connexe du bord, soit $C$,
il revient au même de se donner une
structure de droite projective \inserted{rectifiable} sur $C$,
ou un ``bouchage de trou'' en $C$
par un disque \inserted{de bord $C$}, les propriétés de régularité
(\unsure{p.r. à} la structure analytique réelle de $C$)
de la structure de droite projective, reflétant
"""
save(61,tex,[('deletion','top number','4'),('text','top b)','Recollement de H-bar à lui-même'),('insertion','top formula','σ(0)=0'),('margin note','upper left diagonal','12.1 c) Soit C une courbe rectifiable'),('deletion','within margin','a); un voisinage de; image de; application'),('insertion','within margin','un ouvert; complexe'),('text','heading','4 Recollements des disques'),('deletion','heading','bord à bord'),('insertion','heading','des disques'),('margin note','upper right bubble','Le recollement bord à bord'),('text','middle','Cela correspond dans le th. 4'),('insertion','middle','compacte'),('deletion','middle','Il'),('text','lower','Pour ceci on se rappelle'),('deletion','lower opening','rapp'),('insertion','lower','au lieu de X-tilde'),('insertion','lower','rectifiable'),('insertion','lower','de bord C')],
 doubts=[('marginal c)','un ouvert U; C; analytique / continue','dense superposed lines; word before dans U minus C uncertain','low'),('modules sentence','esp.','abbreviation rather than expanded word','medium'),('last parenthesis','p.r. à','abbreviation faint','medium')],
 abbreviations=[('esp.','espaces'),('dim','dimension'),('p.r. à','par rapport à')],
 leads=['Marginal addition dated 12.1 states a removability principle for a rectifiable curve and a continuous function holomorphic off it; one key handwritten word is uncertain, so any mathematical use requires that qualification.','Projective-line structures on a boundary component are related to capping it by a disc; regularity of the structure should reflect seam regularity.','Finite dimensional moduli motivate natural restrictive conditions on the boundary gluing involution.'])
