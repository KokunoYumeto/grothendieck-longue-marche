import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{64}
\mspage{6}
% archive foliation: 66
\[
D\longrightarrow o(D)\qquad (\text{``ombre de $D$''})
\]
qui associe à tt disque conforme \unsure{autour de}
$D$ son ombre dans $T_{X',a}$, n'a rien d'injec-
tif. Les \uline{disques ``concentriques''} à $D$
donnent les $\lambda o(D)$ $(0<\lambda\leq1)$, plus
précisément, $D\unsure{\longrightarrow|-}o(D)$ est compatible aux
homothéties de rapport \deleted{$\lambda>0$} $\lambda\in]0,1]$.

Je m'intéresse en fait au cas
où $X'$ est compacte, et munie d'une
\deleted{\unsure{famille}} partie finie de ``pts marqués'', soit
\deleted{$\unsure{I}$}\inserted{$(a_i)_{i\in I}$}, et où on prend une famille
de disques $D_i$ $(i\in I)$ \inserted{\uline{mutuellement disjoints}} autour des $a_i$,
donnant des ombres
\[
o(D_i)\subset T_{X',a_i}.
\]
On cherche des conditions particulières
\inserted{plausibles} sur le système des $D_i$, impliquant
(qui sait ?) qu'il est déterminé par
le système des ombres.
"""
save(64,tex,[('display','top','D→o(D) (ombre de D)'),('text','upper','qui associe à tt disque conforme'),('deletion','upper middle','λ>0'),('text','middle','Je m’intéresse en fait au cas'),('deletion','middle','famille'),('deletion','middle','I'),('insertion','middle','(a_i)_{i∈I}'),('insertion','middle lower','mutuellement disjoints'),('display','lower','o(D_i)⊂T_{X′,a_i}'),('text','bottom','On cherche des conditions particulières'),('insertion','bottom','plausibles')],
 doubts=[('opening after conforme','autour de','phrase runs into D; no missing a supplied','low'),('homothety sentence','D→o(D)','arrowhead weak, possibly plain dash','medium'),('middle deleted word','famille','letters mostly crossed','low')],
 notations=[('Shadow of a disc',r'o(D)','lowercase o, not zero; title says ombre')],
 abbreviations=[('tt','tout'),('pts','points')],
 leads=['Shadow map D→o(D) is said not to be injective and is claimed compatible with contractions of concentric discs.','Explicit question: plausible conditions on mutually disjoint discs about marked points of compact X′ that determine the system from its tangent shadows; manuscript says (qui sait ?).'])
