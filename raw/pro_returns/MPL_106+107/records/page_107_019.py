import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
Filtering $\varinjlim$ exist in $(\mathrm{Hot})$?
\mspage{\textcircled{a}}

We would like moreover that the canonical functors
\[
(\mathrm{Cat})\longrightarrow\mathrm{Hot}(\underline W),\qquad\widehat A\longrightarrow\mathrm{Hot}_A\simeq\mathrm{Hot}(\underline W)
\]
\margin{($A$ a test category)}
should commute with such limits. The first case is reduced to the second with $A=\Delta$, using the standard test-functor $\Delta\xrightarrow{i_{\unsure{\Delta|a}}}(\mathrm{Cat})$, giving rise to the nerve-functor $i^*:(\mathrm{Cat})\longrightarrow\widehat\Delta$, as the latter commutes with filtering direct limits (due to the fact that $i(a)$ is ``of f.p.'' for any $a\in\Delta$.

Take first the case of a countable direct system, we may assume it is indexed by $\unsure{-|\omega}$
\diagram{\begin{tikzcd}X_0\arrow[r,no head,"f_0"]&X_1\arrow[r,"f_1"]&X_2\cdots-\end{tikzcd}}
Using factorisation of any morphism as $pi$, with $i$ mono and $p$ a homotopism, we get a diagram
\diagram{\begin{tikzcd}
X'_0\arrow[r,hook,"f'_0"]\arrow[d,"u_0"',"="]&X'_1\arrow[r,hook,"f'_1"]\arrow[d,"u_1"]&X'_2\arrow[r,hook,"f'_2"]\arrow[d,"u_2"]&\cdots\\
X_0\arrow[r,no head,"f_0"']&X_1\arrow[r,no head,"f_1"']&X_2\arrow[r,"f_2"']&\cdots-
\end{tikzcd}}
\margin{\diagram{\begin{tikzcd}X'_\infty\arrow[d,no head,"u_\infty"]\\X_\infty\end{tikzcd}}}
where the $f'_i$ are mono, and the vertical arrows are homotopy equivalences. Let $X'_\infty,X_\infty$ be the limits, hence $u_\infty:X'_\infty\longrightarrow X_\infty$. We're to check

(i) $X'_\infty$ \unsure{is} a direct limit of the $X'_i$'s in $(\mathrm{Hot}_A)$

(ii) $X'_\infty\longrightarrow X_\infty$ is an iso in $(\mathrm{Hot})_A$, i.e. is $\deleted{\unsure{\in}}W$.

Point i) is enough \inserted{(and equivalent, in fact)} to ensure that $(\mathrm{Hot}_A)$ is stable under countable \inserted{filtering} direct limits, and that $\widehat A\longrightarrow(\mathrm{Hot}_A)$ com-\deleted{\unsure{mut}}mutes to such limits, when the transition morphisms are mono. \deleted{\unsure{As}} As for (ii), granting (i), it \deleted{\unsure{is equivalent}}\inserted{is equivalent} with the desired result of commutation of $\widehat A\longrightarrow(\mathrm{Hot}_A)$ to countable filtering direct limits.

To check the limiting property
\[
(*)\qquad\operatorname{Hom}_{\mathrm{Hot}}(X_\infty,\unsure{Y})\xrightarrow{\sim}\varprojlim_i\operatorname{Hom}_{\mathrm{Hot}}(X_i,Y),
\]
\mspage{18}
"""
elements=[('text','title','Filtering lim exist in (Hot)?'),('text','top circled','a'),('text','opening','We would like moreover'),('display','upper','(Cat) -> Hot(W); Ahat -> Hot_A'),('margin note','below right display','A a test category'),('text','upper paragraph','should commute with such limits'),('text','next paragraph','Take first the case'),('diagram','upper middle','X_0 f_0 X_1 f_1 X_2'),('text','middle','Using factorisation'),('diagram','middle','Xprime_i -> Xi'),('margin note','right of diagram','Xprime_infty -> X_infty'),('text','below diagram','where the fprime_i are mono'),('text','item i','Xprime_infty is a direct limit'),('text','item ii','Xprime_infty -> X_infty is an iso'),('text','lower paragraph','Point i) is enough'),('text','last paragraph','To check the limiting property'),('display','foot','(*) Hom_Hot(X_infty,Y)'),('text','foot left','18')]
if __name__=='__main__':save(107,19,tex,elements,notes='New English argument on filtering colimits in Hot. Countable reduction replaces arrows by monos and homotopy equivalences; marks two checks (i) universal property and (ii) colimit comparison in W, and asserts equivalence of (ii), given (i), with full preservation. Heading has question mark. The indexing mark after by is only a dash-shaped stroke (not silently converted to omega). Several headless arrows retained. Last display has unprimed X_infty and Xi despite preceding primed system. Research note needed on the strength of an ordinary categorical colimit claim and later corrections.')
