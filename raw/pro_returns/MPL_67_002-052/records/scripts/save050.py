import sys
sys.path.insert(0,'MPL_67_002-052/records')
from save_page import save
save(50,r'''% archive foliation: 52
Générateurs et relations pour les groupoïdes et groupes de Teichmüller (spéciaux et ordinaires, évt. toriques\ldots)

Je m'attends à trouver trois types de présentations à propriétés complémentaires --- mais toutes à signification arithmétique :

a) Présentation par ``\uline{pantalons}'' ou ``\uline{triades}''. Elle revient à travailler sur les pts à l'infini ``les plus \unsure{cubiques|critiques}'' sur les multiplicités modulaires, et semble (d'après l'exemple de $\mathcal T_{0,4}^{+!}$) commode surtout pour exprimer des groupes du type $T_{g,\nu}^{+!}$ (ou $T_{g;I}^{+}$).

b) Présentation par ``boîte'' complète de pièces de Légo (\unsure{voire|voir} des boîtes encore plus complètes) à l'aide des \inserted{\uline{groupes d'}}\uline{automorphismes} \inserted{\uline{\unsure{stricts}}} de ces pièces, et certains ``chemins'' de déformation particuliers allant de certaines pièces à d'autres. Exemples frappants : $T_{0,4}^+$ (\unsure{connu!|connus!}), ou
\[
T_{1,1}^+\simeq\mathrm{SL}(2,\mathbb Z)\quad\text{engendré par }\rho,\sigma\quad\text{avec }\rho^{\unsure{3}}=\sigma^2,
\]
\[
\rho^6\ (=\sigma^4)=1.
\]

c) Présentations \uline{par involutions}, qui sont dans $\mathcal T_{g\nu}^{-}$. Exemple typique $T_{11}\simeq\mathrm{GL}(2,\mathbb Z)$ \deleted{\unsure{eng}} (\deleted{\unsure{Origine}} aux Groupes cartographiques triangulés) engendré par trois réflexions $r_1,r_2,r_3$ avec
\[
(r_1r_2)^2=(r_2r_3)^3,\quad(r_1r_2)^4\bigl(=(r_2r_3)^6\bigr)=1.
\]
''',[
('text','title','Générateurs et relations ... Teichmüller'),
('text','upper','Je m’attends à trouver trois types ...'),
('text','upper middle','a) Présentation par pantalons ou triades'),
('text','middle','b) Présentation par boîte complète de pièces de Légo'),
('insertion','middle','groupes d’'),
('insertion','middle','stricts'),
('display','lower middle','T₁,₁+≃SL(2,Z); ρ³=σ²'),
('display','lower','ρ⁶(=σ⁴)=1'),
('text','lower','c) Présentations par involutions; T₁₁≃GL(2,Z)'),
('deletion','lower','eng; Origine'),
('display','bottom','(r₁r₂)²=(r₂r₃)³; (r₁r₂)⁴(=(r₂r₃)⁶)=1')],leads='Own expectation Je m’attends: three complementary arithmetically meaningful presentations, pants/triads, Lego automorphism groups plus deformation paths, involutions/cartographic triangles. Need three notes plus relation to context Lego/Teichmüller tower/cells. Explicit SL2Z presentation and GL2Z reflection relations are possible concrete targeted computation checks; do not silently correct relations or superscripts +! (visible dot). No author number visible on page.')
