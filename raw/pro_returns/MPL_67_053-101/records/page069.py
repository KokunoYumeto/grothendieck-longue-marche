import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{69}
% archive foliation: 71
des syst. admissibles de disques \inserted{conformes} autour
des $a_i$, vers l'ens des syst.
de disques \deleted{conformes}\inserted{\unsure{standards|euclidiens}} dans les $T_{X,a_i}$,
est bijective. \deleted{Au niveau des
esp.}

Au niveau des espaces
modulaires de type Teichmüller,
cela donnerait donc une \deleted{\unsure{à}} structure
de fibré principal de groupe
\deleted{\diagram{\begin{tikzcd}TB_{g,\unsure{I|\nu}}\arrow[r,"\sim"]&T_{g\nu}\end{tikzcd}}}
structural $(\mathbb R^{*+})^I$ : $TB_{g,I}$
sur $T_{g,I}$ $(\operatorname{card}I=\nu)$, \deleted{\unsure{--}}

Si \unsure{la relation} qui précédait
\deleted{(en passant aux log}
\deleted{longueurs} était vraie, cela signifierait
qu'on aurait une section canonique
de ce fibré, ce qui implique
aussi que pour un pt de $T\deleted{B}_{g,I}$,
i.e. une surface bd \inserted{ponctuée} ($\unsure{X_0}$-rigidifiée)
de type $(g,\nu)$, il y aurait un syst.
d'ombres can. dans les $T_{X,a_i}$, i.e. des
"""
save(69,tex,[('text','top','des syst. admissibles de disques'),('insertion','top','conformes'),('deletion','upper','conformes'),('insertion','upper','standards / euclidiens'),('deletion','upper','Au niveau des esp.'),('text','upper middle','Au niveau des espaces modulaires'),('deletion','middle','à'),('diagram','middle cancelled','TB_{g,I}→T_{gν}'),('deletion','middle','whole arrow diagram'),('text','middle lower','structural (R^{*+})^I'),('deletion','middle lower','dash'),('text','lower','Si la relation qui précédait'),('deletion','lower','en passant aux log'),('deletion','lower','longueurs'),('deletion','lower','B in TB'),('insertion','lower','ponctuée'),('text','bottom','de type (g,ν) il y aurait')],
 doubts=[('inserted description of discs','standards','euclidiens also possible; start overwritten','low'),('cancelled arrow','I / ν','index overwritten','low'),('paragraph initial noun','la relation','ink compressed; l’idée plus another word also possible','low'),('rigidification','X_0','possible stroke above X; compare fixed reference on scan 66','medium')],
 abbreviations=[('ens','ensemble'),('esp.','espaces'),('pt','point')],
 leads=['Conjecture concludes bijectivity of admissible discs→Euclidean/standard tangent discs.','Conditional principal (R^{*+})^I-bundle interpretation TB_{g,I} over T_{g,I}, and further claimed canonical section if the preceding relation were true.','Canonical section would induce canonical tangent shadow systems for a marked punctured surface; continuation on scan 70.'])
