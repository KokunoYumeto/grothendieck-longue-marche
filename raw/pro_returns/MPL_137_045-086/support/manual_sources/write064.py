import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{64}
% archive foliation: 63
contient pas \uline{assez} de \inserted{$\Sigma$-}projectifs: il faut y rajouter $\Psi^0$\ldots) \deleted{Il est vrai que} Ces assertions sont d'ailleurs vraies aussi dans la plus gde catégorie $P$ [détermination des \inserted{$\Sigma$-}proj et des $\Sigma$-inj, et le fait qu'il y en a assez].

Les $\operatorname{Ext}^i$ calculés par les résolutions injectives \inserted{à droite} ou projectives \inserted{à g.} \deleted{\unsure{sont} (à gauche} \unsure{ou les} deux simultanément, sont les \unsure{mêmes} pour $i\geq1$, ce sont les hyperext habituels de \inserted{$L_\bullet$ et de $M_\bullet$}, (pour $i=0$ on doit prendre les $L^i$.

Si $F:\ Q=P_1\subset P\ \unsure{\longrightarrow|{-}}\ B$ (\unsure{$k$-addit.}) \deleted{est un} foncteur, on peut construire les foncteurs dérivés \inserted{à droite et à g.} (en utilisant des résolutions injectives ou projectives.

Nous sommes intéressés notamment aux $R^iF(\Psi^0)$, qu'on note aussi $\unsure{\mathcal H^i(F)|H^i(F)}$ [on doit pouvoir montrer que ce sont les dérivés \inserted{droits} de $F\mapsto F(\Psi^0)=\Gamma(F)$, quand $F$ varie dans la cat. des \deleted{foncteurs} \inserted{$k$-add.} $P\unsure{\longrightarrow|{-}}B$ \inserted{$\Sigma$-}exacts à gauche; (Si on se restreint à de tels $F$); \unsure{qu’elle|en effet} cette catégorie est équivalente à \deleted{\unsure{celle}} \deleted{$\unsure{B}$} $\unsure{B^\bullet|B'}$, $F\mapsto F(\Psi^0)$ s'identifie \deleted{alors} au foncteur $C^\bullet\mapsto Z^0(C^\bullet)$\inserted{$=H^0(C^\bullet)$} sur $\unsure{B^\bullet|B'}$, dont les dérivés sauf erreur sont les $H^i(C^\bullet)$ pour $i\geq1$. On a aussi $RF(\Psi^0)\simeq F(C^\bullet)$'''
e=[('text','top','contient pas assez de projectifs'),('insertion','top','Σ-'),('deletion','top line 2','Il est vrai que'),('text','upper','Ces assertions sont d’ailleurs vraies'),('insertion','upper','Σ- proj'),('text','upper middle','Les Ext^i calculés'),('insertion','upper middle','à droite'),('insertion','upper middle','à g.'),('deletion','upper middle','sont (à gauche'),('insertion','middle','Lbullet et de Mbullet'),('text','middle','Si F: Q=P1⊂P→B'),('deletion','middle','est un'),('insertion','middle','à droite et à g.'),('text','lower half','Nous sommes intéressés notamment'),('insertion','lower half','droits'),('deletion','lower third','foncteurs'),('insertion','lower third','k-add.'),('insertion','lower third','Σ-'),('deletion','lower third','celle'),('deletion','lower third','B'),('deletion','bottom','alors'),('insertion','bottom','=H0(Cbullet)'),('text','bottom','dont les dérivés sauf erreur')]
save(64,text,e)
