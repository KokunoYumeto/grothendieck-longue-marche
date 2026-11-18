import sys
sys.path.insert(0,'MPL_67_002-052/records')
from save_page import save
save(44,r'''\mspage{18}
% archive foliation: 46
b') Cas $\mathcal X\simeq\mathbb P^1_{\mathbb C}$, $\sigma$ une inversion --- laquelle définit une structure de droite projective réelle --- on trouve \deleted{le disque} pour $X$ un \uline{disque}. Pour obtenir une métrique distinguée sur $\mathcal X$ invariante par $\sigma$, il faut se donner un pt du disque ouvert $X\setminus\partial X$

\figure{\begin{tikzpicture}\draw (0,0)--(5,.2);\end{tikzpicture}}

En résumé, tte surface conforme à bord 0-connexe admet une unique métrique Riemannienne distinguée, sauf dans les quatre cas suivants

a) a') Cas $X\simeq\mathbb C$, ou $X\simeq\unsure{\overline{\mathbb H}|\mathbb H}=\{z\in\mathbb C\mid\mathrm{Im}\,z\geq0\}$ [droite affine complexe, demi-plan à bord défini par une droite affine réelle], on a alors une classe de métriques mod constante, qui forment une orbite sous $\mathrm{Aut}\,X$.

b) b') $X\simeq\mathbb P^1_{\mathbb C}$ ou $X\simeq\text{disque}$ [droite projective complexe ou \deleted{\unsure{demidisque fermé}} défini par droite projective réelle] --- il y a alors un ens. de métriques distinguées dépendant de 3 paramètres réels resp. de 2 paramètres réels, également orbite sous $\mathrm{Aut}\,X$.
''',[
('text','top','b′) Cas 𝒳≃P¹_C, σ une inversion'),
('deletion','upper','le disque'),
('text','middle','Pour obtenir une métrique distinguée ... X\∂X'),
('drawing','middle separator','horizontal rising line'),
('text','middle lower','En résumé ... quatre cas suivants'),
('text','lower','a) a′) Cas X≃C ou X≃Hbar ...'),
('text','bottom','b) b′) X≃P¹_C ou X≃disque'),
('deletion','bottom','demidisque fermé')],leads='Recap four exceptional objects (plane/closed half-plane, sphere/closed disk) and distinguished metric parameter spaces dimensions1,3,2. Spherical metric on double of disk needs an interior point of quotient. Search context metrics, demi-plan, disque, normalization and R(X); distinguish author normalization precisely without inventing it.')
