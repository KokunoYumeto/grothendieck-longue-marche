import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{62}
\mspage{5}
% archive foliation: 64
les propriétés de régularité de $C$ en tant que
cercle \inserted{``intérieur''} dans la surface \deleted{sans bord}\inserted{conforme} $X'$ déduite
par bouchage du trou. D'autre part,
le choix d'un point de $D\setminus C$ équivaut
à celui d'une structure torique
sur $C$ compatible avec la structure de
droite projective réelle (i.e. une réduction
du groupe structural \inserted{$(\unsure{\operatorname{GP}(1,\mathbb R)}\simeq)$}
$\operatorname{GL}(2,\mathbb R)/\mathbb R^*$
au sous-groupe cpt maximal $\operatorname O(2)/\pm1$)
--- et cela équivaut aussi à la donnée
d'une structure \unsure{torique|conique} de $D$ sur \inserted{le bord}
$\delta D=C$. Notons que l'on aura alors une
inclusion canonique
\[
D\subset\overline T_{X',a}
\]
où $a$ est le centre choisi de $D$. On
va expliciter \deleted{ainsi} ces diverses
relations ainsi

\uline{Prop.} Équivalence entre \deleted{la cat. des
surfaces conf.}
"""
save(62,tex,[('text','opening','les propriétés de régularité de C'),('insertion','line 2','intérieur'),('deletion','line 2','sans bord'),('insertion','line 2','conforme'),('text','upper middle','D’autre part le choix d’un point'),('insertion','structural group','GP(1,R)≃'),('text','middle','et cela équivaut aussi'),('insertion','middle','le bord'),('text','middle lower','Notons que l’on aura alors'),('display','lower middle','D⊂T-bar_{X′,a}'),('text','lower','où a est le centre choisi'),('deletion','lower','ainsi'),('text','bottom','Prop. Équivalence entre'),('deletion','bottom two lines','la cat. des surfaces conf.')],
 doubts=[('structural group insertion','GP(1,R)','do not silently replace by PGL(2,R)','medium'),('disc structure','torique','conique possible; initial overwritten','medium')],
 notations=[('Projective group of the real line',r'\unsure{\operatorname{GP}(1,\mathbb R)}','Scan 62; equated to GL(2,R)/R*'),('Tangent-line expression',r'\overline T_{X\prime,a}','Scan 62; horizontal bar retained')],
 abbreviations=[('conf.','conformes')],
 leads=['Choice of centre in a capping disc corresponds to reducing projective boundary data to a toric structure, with maximal compact subgroup O(2)/±1.','Canonical inclusion of the centred disc into the displayed barred tangent line; normalization and real/complex conventions need examination.'])
