import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
text=r'''\scanpage{45}

\diagram{\begin{tikzcd}[column sep=large]
0\arrow[r]&G_k^0\arrow[r]&G_k\arrow[r]&\unsure{P_k|\mathfrak P_k}\arrow[r]&0
\end{tikzcd}}
\margin{extension abélienne maximale}
\margin{extension non ramifiée maximale}

\deleted{
\diagram{\begin{tikzcd}[column sep=large]
0\arrow[r]&Z_2^{r_1}\arrow[r]&G_k^0\arrow[r]&U_k^0/\operatorname{Im}E\arrow[r]&0
\end{tikzcd}}
\margin{ou un quotient ???}
\margin{idèles unités finis}
\margin{idèles unités finis principaux}
\figure{\begin{tikzpicture}\draw[gray] (0,0).. controls (-.2,-.2) and (.4,-.25)..(.8,-.15);\draw (2,0)..controls (2,-.2) and (2.4,-.2)..(2.6,0);\draw (3,0)..controls (3,-.2) and (3.6,-.2)..(3.8,0);\end{tikzpicture}}

N. B. $G_k/Z_2^{r_1}$ (qui est ce que dans la définition on fait par \unsure{restriction} d'\unsure{idèles} à l'infini) est le groupe de Galois de l'extension abélienne non ramifiée à l'infini maximale (i.e. qui est \unsure{complexe|complète} au dessus de \unsure{ttes} places réelles de $k$) -- Soit de façon générale, $S$ un ensemble \inserted{\unsure{fini}} de places finies ou infinies réelles, alors le groupe de Galois top. de l'extension \inserted{abélienne} non ramifiée en $\unsure{\complement S|C S}$ maximale, est $G_k^S$, où
\diagram{\begin{tikzcd}[column sep=large]
0\arrow[r]&G_k^{\unsure{0S}}\arrow[r]&G_k^S\arrow[r]&\unsure{P_k|\mathfrak P_k}\arrow[r]&0
\end{tikzcd}}
\diagram{\begin{tikzcd}[column sep=large]
0\arrow[r]&Z_2^{\unsure{S^\infty}}/\bigcap_k\operatorname{Im}\bigl(E^{\unsure{(\underline S^0)k}}\bigr)\arrow[r]&G_k^{0S}\arrow[r]&U_k^{S^0}/\operatorname{Im}E\arrow[r]&0
\end{tikzcd}}
\margin{ceci est-il \unsure{identique} à $Z_2^{S^\infty}$ ???}
\figure{\begin{tikzpicture}\draw (0,0)--(-.1,-.2)--(2.1,-.1)--(2.2,0);\end{tikzpicture}}
}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,0)--(2,-5.4);\draw (-.7,-4)..controls (1,-2.9) and (2.8,-1.2)..(3.7,-.3);\end{tikzpicture}}

Ceci résulte du \uline{lemme}. Pour qu'une \deleted{\unsure{normale}} \inserted{extension} $L$ d'un corps local \deleted{\unsure{abs.}} \unsure{quel} $K$ soit non ramifiée, il faut et il suffit que
\[
N_{L/k}U_L=U_L\unsure{\cap|\parallel}N_{L/k}L^*\supset U_k
\]

\mspage{44}'''
elements=[('diagram','top','0 → Gk0 → Gk → Pk → 0'),('margin note','under Gk','extension abélienne maximale'),('margin note','under Pk','extension non ramifiée maximale'),('deletion','central draft','two diagonal cancellation strokes over sequences and N.B.'),('diagram','upper middle','0 → Z2^r1 → Gk0 → Uk0/Im E → 0'),('margin note','under Z2','ou un quotient ???'),('margin note','under Uk0','idèles unités finis'),('margin note','under Im E','idèles unités finis principaux'),('drawing','under second sequence','three annotation brackets'),('text','middle','N. B. Gk/Z2^r1'),('insertion','above ensemble','fini'),('insertion','above non ramifiée','abélienne'),('diagram','lower','0 → Gk0S → GkS → Pk → 0'),('diagram','lower','0 → Z2^S∞ / intersection Im(E) → Gk0S'),('margin note','under lower quotient','ceci est-il identique à Z2^S∞ ???'),('drawing','under lower quotient','bracket'),('drawing','central','two long crossing cancellation strokes'),('text','foot','Ceci résulte du lemme'),('deletion','foot line 1','normale'),('insertion','foot line 1','extension'),('deletion','foot line 2','abs.'),('display','foot','N(L/k)UL=UL cap N(L/k)L* superset Uk'),('text','bottom left','44')]
save(45,text,elements,sheet_kind='cancelled_draft',observations='Whole and both halves read with enlarged sentence, labels, exact sequences and bottom lemma. Two diagonal strokes cross the central draft, from the second sequence through the lower sequences; this span is encoded as deleted, with both strokes reproduced. The first sequence and final lemma are outside that span. The questioned quotient exponents, short wording around the local field K, and the operation in the final formula remain explicitly uncertain. The U_L written on both sides of the last equality was retained.')
