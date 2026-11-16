import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\mspage{7})

qu'on compose encore comme précédemment. On a bien \deleted{\unsure{deux|un}} \unsure{foncteurs|foncteur}
\diagram{\begin{tikzcd}
\deleted{\unsure{C\longrightarrow}}&\widetilde C\arrow[r]&W^{-1}C
\end{tikzcd}}

\deleted{Le premier de ces deux foncteurs transforme bien les éléments de $W$ en flèches inversibles. \deleted{On a} Pour
\diagram{\begin{tikzcd}
x\arrow[r,"f","\sim"']&y
\end{tikzcd}}
\unsure{$f\in W$}, on considère
\[\text{soit }F=[f]\]
\diagram{\begin{tikzcd}
y\arrow[dr,"1_y"']&x\arrow[d,"f","\sim"']\\
&y
\end{tikzcd}}
\[\text{soit }G=[1_y,f].\]
\unsure{Et on trouve les composés} \unsure{et on a donc}
\[\uline{GF}=\unsure{[\,]^{x}}\]
}
\unsure{définissons le} $=$
\diagram{\begin{tikzcd}C\arrow[r]&\widetilde C\end{tikzcd}}
qui va être un peu plus délicat. Soit $f:x\longrightarrow y$. On choisit une factorisation
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
x\arrow[dr,"f_0"']&y\arrow[dr,bend left=30,dotted,"i"]\arrow[dr,dashed,"\beta","\sim"']&\\
&\bar y\arrow[u,"\unsure{\alpha}","\sim"']\arrow[r,dotted,"\unsure{g}","\sim"']&\bar y'
\end{tikzcd}}
\inserted{\unsure{donc $\bar y$ cof}}
et, avec le \unsure{w.k lifting lemma} (ici $y$ étant cofibrant) on peut compléter par des pointillés, où $\beta$ a une section $i$.

On considère alors $[g f_0,i]$, il faut montrer que ça ne dépend pas des choix faits. Pour un choix $[f',i']$
\diagram{\begin{tikzcd}
x\arrow[r,dashed,"f"]\arrow[dr,"f'"']&y\arrow[d,"i'","\sim"',shift right=1]\\
&y'\arrow[u,dashed,"\alpha","\sim"',shift right=1]
\end{tikzcd}}
tel qu'il existe \deleted{\unsure{un|une}} une rétraction $\alpha$ de $\widetilde y$ sur $y$, telle que
\[\alpha f'=f.\]

\margin{On s'est ramené aux factorisations $f=\unsure{\alpha}f_0$, $\unsure{f_0}\in\unsure{\operatorname{cof}}$ et $\unsure{\alpha}\in W$, telles que $\unsure{\alpha}$ ait une section.}

Considérons deux tels choix, il faut voir qu'ils sont dans une $=$ composante connexe de $\underline{\operatorname{Ch}}_0(x,y)$. Mais pour deux factorisations d'une flèche $f:x\longrightarrow y$ en $\alpha f_0$ et $\alpha'f'_0$, $f_0,f'_0\in\operatorname{Cof}$, $\alpha,\alpha'\in W$, \deleted{\unsure{$x\longrightarrow y$}} on peut les coiffer par une troisième \deleted{\unsure{$f''$}} $\alpha'',f''_0$ qui \deleted{\unsure{\diagram{\begin{tikzcd}x\arrow[r]&y''\end{tikzcd}}}} \deleted{\unsure{permet de}} \inserted{\unsure{reçoit|réduit}} les deux \unsure{comme on voit dans les diagrammes}

\margin{Ce foncteur est bijectif sur les objets, surjectif sur les flèches, \unsure{comme préc.}. On vérifie aisément [il suffit pour cela \unsure{dans un produit} de voir que pour tt $f\in W$, $f:x\longrightarrow y$, $[f]^{-1}$ provient de $\widetilde C$, on prend
\diagram{\begin{tikzcd}
x\arrow[r,"\unsure{f}"]\arrow[dr,"\sim"']&y\arrow[d,shift left=1,"\alpha"]\\
&\unsure{\bar y}\arrow[u,very thick,shift left=1,"\unsure{i}","\sim"']
\end{tikzcd}}
\unsure{(les deux flèches sont des isos)}]
\diagram{\begin{tikzcd}
y\arrow[dr,"\unsure{1_y}"']&\unsure{x}\arrow[d,"\unsure{f}","\sim"',shift right=1]\\
&y\arrow[u,"\unsure{\alpha}"',shift right=1]
\end{tikzcd}}
}

\mspage{13}
"""
elements=[('text','top left','7)'),('text','top first two lines',"qu'on compose encore comme précédemment"),('diagram','top centre','cancelled C arrow; tilde C to W inverse C'),('text','cancelled upper block first two lines','Le premier de ces deux foncteurs'),('diagram','cancelled block upper centre','x to y, f, sim'),('text','cancelled block','f in W, on considère'),('display','cancelled block upper right','soit F=[f]'),('diagram','cancelled block middle','y to y, x to y; 1y, f'),('display','cancelled block right','soit G=[1y,f]'),('text','cancelled block bottom','Et on trouve les composés'),('display','cancelled block bottom','GF=[1x]'),('text','middle above comparison','définissons le ='),('diagram','middle','C to tilde C'),('text','middle','qui va être un peu plus délicat'),('diagram','middle factorization','x, y, bar y, bar y prime; f0 alpha beta i g'),('text','below factorization','et avec le w.k lifting lemma'),('text','lower middle','On considère alors [g f0,i]'),('diagram','lower middle','x to y, x to y prime, i prime alpha'),('text','right of lower diagram',"tel qu'il existe une rétraction"),('display','right of lower diagram','alpha f prime=f'),('text','bottom paragraph','Considérons deux tels choix'),('diagram','within cancelled bottom line','x to y double prime'),('diagram','left margin upper sketch','x, y, bar y; f sim alpha beta'),('diagram','left margin lower sketch','y, x, y; opposing arrows'),('text','foot','13')]
notes='''This page attempts the revised two-arrow construction and a functor C to tilde C. A large earlier argument that the first functor in C→tilde C→W^{-1}C inverts W is cancelled. The surviving text says defining C→tilde C “va être un peu plus délicat” and requires independence of choices (“il faut montrer que ça ne dépend pas des choix faits”). It appeals to the weak lifting lemma with y cofibrant, then claims that two factorizations may be dominated by a third; the sentence continues on the next handwritten page. The diagonal margin claims bijectivity on objects and surjectivity on arrows for the comparison with W^{-1}C, with the reduction to inverses of weak equivalences. Heavy overwriting, compressed cursive and cancelled paragraphs make this page particularly uncertain. In the later audit, revisit the cancelled GF expression and the little marginal diagrams; no contextual source used.'''
if __name__=='__main__':save(106,14,tex,elements,notes=notes)
