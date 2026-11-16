import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{53}
\mspage{18}
\deleted{Version forte}\inserted{Corollaire de W7 bis} (\deleted{\unsure{W8}} forme plus forte en apparence)
\uline{W7 \unsure{ter|bis}} Soit $\mathcal X$ lisse sur $\Phi=\diagram{\begin{tikzcd}&a\arrow[dl]\\0\arrow[dr]&\\&b\end{tikzcd}}$, d'où diagramme (comm. dans $\mathrm{Hot}_W$)
\[\diagram{\begin{tikzcd}&X&\\X_a\arrow[ur,"i'_b"]&&X_b\arrow[ul,"i'_a"']\\&X_0\arrow[ul,"i_a"]\arrow[ur,"i_b"']&\end{tikzcd}}\]
Alors
\[i_a\in W\Longleftrightarrow\unsure{i'_a|i'_0}\in W\]
\[(\text{donc }i_b\in W\Longleftrightarrow i'_b\in W)\]
(NB Cela implique l'énoncé dual W7' ter, avec $X$ propre sur $\Psi=\diagram{\begin{tikzcd}&a\arrow[dl]\\0&\\&b\arrow[ul]\end{tikzcd}}$)

Corollaire de W8 bis (forme renforcée en apparence).
\uline{W8 \unsure{ter|bis}} Soient $\mathcal X,\mathcal X'$ lisses sur $\underline\Phi=\diagram{\begin{tikzcd}&a\arrow[dl]\\0&\\&b\arrow[ul]\end{tikzcd}}$, et $f:\mathcal X-\mathcal X'$ un $\underline\Phi$-morphisme. Soient $f_a,f_b,f_0$ induits sur les fibres, et les conditions
\[\begin{array}{ll}a)&f\in W\\b)&f_0\in W\\c)&f_a\text{ et }f_b\in W\end{array}\]
Alors deux de ces conditions impliquent la troisième.
\mspage{52}
'''
e=[('text','top','18'),('deletion','top','Version forte'),('insertion','top','Corollaire deW7bis'),('deletion','top','W8'),('text','top','forme plus forte'),('text','upper','W7ter'),('diagram','upper','Phi a to0 to b'),('text','upper','d’où diagramme'),('diagram','upper middle','X0 Xa Xb X'),('text','middle','Alors'),('display','middle','ia inW iff'),('display','middle','donc ib inW iff'),('text','middle lower','NB Cela implique'),('diagram','middle lower','Psi a b to0'),('text','lower','Corollaire deW8bis'),('text','lower','W8ter'),('diagram','lower','Phi a b to0'),('text','lower','et f'),('display','bottom','abc conditions'),('text','bottom','Alors deux'),('text','bottom','52')]
record_page(53,s,e,notes='Final page18 and folio52. W7ter/W8ter labels uncertain between ter and bis. Top shape has ink arrow0→b, preserved despite later bottom shape b→0. No proof on this page for strengthened W8 claim.')
build_doubts()
