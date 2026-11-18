import sys
sys.path.insert(0,'MPL_67_002-052/records')
from save_page import save
save(45,r'''\mspage{\unsure{19}}
% archive foliation: 47
\uline{Corollaire 3} Soit $\underset{\text{ouvert}\atop\text{0-connexe}}{X\subset X'}$, $X'$ hol. 0-connexe. Alors $X$ est hyperbolique, sauf dans les cas suivants :

a) $X'$ est $\simeq\mathbb P^1_{\mathbb C}$ (resp. $\mathbb E^1_{\mathbb C}$, resp. $\mathbb G_{m\mathbb C}$), et $\operatorname{card}(X\setminus X')\leq2$ (resp. $\leq1$, resp. $=0$)

b) $X'$ est compacte de genre 1 et $X=X'$.

\uline{Remarque} Soit \deleted{\unsure{e}} $X$ une surface conforme 0-connexe (pas néc. orientable). On dit encore que $X$ est hyperbolique si $\widetilde X\simeq H$, ou ce qui revient au $=$, si tte application conforme $\mathbb C\longrightarrow X$ est constante.

\margin{ou encore si le rev. \deleted{\unsure{absolu}} \inserted{des} orientations (qui est une surf. holomorphe) est hyperbolique.}

Ainsi les surfaces conformes \inserted{ss. bord,} 0-connexes \uline{non} hyperboliques sont, en plus des quatre cas énumérés dans (i) ci-dessus, les quotients de telles surfaces par des anti-involutions sans pts fixes. On trouve donc de plus
''',[
('text','top','Corollaire 3 Soit X⊂X′; X′ hol. 0-connexe'),
('insertion','under inclusion','ouvert 0-connexe'),
('text','upper','Alors X est hyperbolique, sauf ...'),
('text','upper middle','a) X′≃P¹_C (resp E¹_C, G_mC); card(X\X′)'),
('text','middle','b) X′ compacte de genre1, X=X′'),
('text','middle to lower','Remarque Soit X une surface conforme ...'),
('deletion','middle','e'),
('margin note','left diagonal','ou encore si le rev. ... orientations'),
('deletion','left margin','absolu'),
('insertion','left margin','des'),
('text','lower','Ainsi les surfaces conformes ... On trouve donc de plus'),
('insertion','lower right','ss. bord')],leads='Corollary3 on hyperbolicity of open X⊂X′, exceptional P1,E1,Gm, genus1 compact; handwritten complement reads X\X′, potentially a reading/correction question (keep ink). Then nonorientable conformal surfaces via free anti-involutions; extends definition and list of exceptions. Page number appears19 but faint. Left margin orientation-cover criterion.')
