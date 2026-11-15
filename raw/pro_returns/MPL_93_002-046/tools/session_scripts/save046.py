import sys
sys.path.insert(0,'MPL_93_002-046_work/tools')
from save_page import save_page
save_page(46,r"""
\scanpage{46}
schémas abéliens, \inserted{permettant de définir un foncteur qu.inverse du foncteur du théorème.} Pour ceci, on considère pour tout schéma abélien $A$ sur $S$ son extension vectorielle universelle, qui est une extension
\[
0\longrightarrow\underline t_{A^*}^{\vee}\;-\;E(A)\;-\;A\longrightarrow0.
\]
Il se trouve qu'on peut trouver un cristal en groupes lisses canonique sur $S$, soit $\underline E(\unsure{A})$, tel que l'on ait
\[
E(A)\unsure{\simeq|\cong}\underline E(A)_S.
\]
La définition est telle que \deleted{pour tout le foncteur}\inserted{$A$} $\underline E(A)$ définisse un foncteur
\[
\text{Schémab}(S)\longrightarrow\text{Cris Groupes lisses}_{\mathrm{nilp}}(S)
\]
compatible aux changements de base, l'isomorphisme précédent étant également fonctoriel et compatible aux changements de base. Il s'ensuit donc que l'on peut définir $\underline E(A)_{\deleted S}$ comme $S'\mapsto\underline E(A)_{S'}$, avec
\[
\underline E(A)_{S'}=E(A'),
\]
$A'$ désignant un schéma abélien qui prolonge $A$ sur $S'$, \deleted{\unsure{à}} à charge de définir \deleted{un}\inserted{un système transitif d'} isomorphismes canoniques entre les groupes obtenus pour des prolongements différents. Dans le cas où $S$ est de \unsure{caractééristique|caractéristique} nulle (donc plus question de puissances divisées !) cela est particulièrement simple; on prouve qu'il existe à isomorphisme \uline{unique} près un seul schéma en groupes lisses $E'$ sur l'épaississement $S'$ de $S$ qui prolonge $E$ (NB il suffirait même d'un nilépaississement, comme on voit par passage à la limite à partir du cas noethérien): c'est le résultat déjà signalé dans ma vieille lettre à Tate. Dans le cas général, c'est plus délicat, et peut se faire par ``la méthode de l'exponentielle'', qui sera exposée dans le contexte analogue des groupes de BT dans la suite du séminaire. On peut aussi définir $\underline E(A^*)$ par
\[
\underline E(A^*)=R^1f_{A\mathrm{cris}*}(\underline G_{m\,A_{\mathrm{cris}}}),
\]
où $A_{\mathrm{cris}}$ désigne le topos cristallin \deleted{\unsure{abso}} nilpotent absolu (relativement à $\underline Z$ ): cette méthode peut également s'adapter au cas des groupes de BT.

Quoi qu'il en soit de la méthode utilisée pour définir $\underline E(A)$, on
\margin{45}
""",'typed',[
('insertion','top, attached after schémas abéliens','permettant de définir un foncteur qu.inverse'),
('text','top','schémas abéliens, Pour ceci'),
('display','upper','0 to t_Astar dual - E(A) - A to 0'),
('text','upper','Il se trouve qu’on peut trouver'),
('display','upper middle','E(A) isomorphic underline E(A)_S'),
('text','upper middle','La définition est telle que'),
('deletion','upper middle','pour tout le foncteur'),
('insertion','above canceled phrase','A'),
('display','upper middle','Schémab(S) to Cris Groupes lisses_nilp(S)'),
('text','middle','compatible aux changements de base'),
('deletion','middle, E(A) subscript','S'),
('display','middle','E(A)_Sprime = E(Aprime)'),
('text','middle and lower','Aprime désignant un schéma abélien'),
('deletion','before à charge','à'),
('deletion','after définir','un'),
('insertion','after définir','un système transitif d’'),
('display','lower','E(Astar) = R1 f_Acris*(G_mAcris)'),
('text','lower','où A_cris désigne le topos cristallin'),
('deletion','before nilpotent','abso'),
('text','bottom','Quoi qu’il en soit de la méthode'),
('margin note','bottom left','45')
],[
('extension display, middle connectors','plain dashes','arrows with faded heads','medium','The first and final connectors have arrowheads; the two middle connectors have no visible heads.'),
('first prose E(A), argument','A','','medium','The argument is overtyped.'),
('identification E(A) with crystal evaluation',r'\simeq',r'\cong','low','The handwritten/retraced equivalence sign has several overlapping strokes.'),
('insertion A above canceled phrase','A','','medium','A remains above the end of the canceled phrase; its precise intended replacement span is unclear.'),
('after prolonge A sur Sprime','à','et','low','The short canceled mark is densely blackened; a lower curve survives.'),
('characteristic-zero paragraph','caractééristique','caractéristique','low','Two adjacent overtyped accented forms are visible; no silent spelling correction made.'),
('last canceled word before nilpotent','abso','absolu','medium','The visible canceled run begins abs and appears to stop after the fourth position.')
])
