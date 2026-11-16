import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""\mspage{4)}
Cette composition est associative à iso can. près, et elle a des identités bilatères (\deleted{\unsure{par}} un iso can. !) savoir
\diagram{\begin{tikzcd}
x \arrow[dr,"1"'] & x \arrow[d,"1","\sim"'] \\
& x
\end{tikzcd}} noté $\uline{1}_x$.

On a d'autre part des \deleted{\unsure{appl.}} foncteurs
\[\operatorname{Hom}_C(x,y)_{\text{discret}}\longrightarrow\uline{\mathrm{Ch}}_0(x,y)\]
\deleted{\unsure{compatibles à}}
\[f\longmapsto(f,\operatorname{Id}_{\unsure{x|y}})\]
compatibles aux compositions. Ceci posé soit
\[\pi_0(x,y)\overset{\mathrm{def}}=\pi_0\uline{\mathrm{Ch}}_0(x,y);\]
alors la composition des $\uline{\mathrm{Ch}}_0$ définit une composition des $\pi_0(x,y)$, qui est associative (str. !) et admet les classes des $\uline{1}_x$ comme unités bilatères. D'où une catégorie, que je note $\widetilde C^{\unsure{2|?}}$, et un foncteur
\[C\longrightarrow\widetilde C.\]

Pour l'instant, on n'a utilisé rien sur $(C,W)$, [\deleted{\unsure{ni}} \unsure{ni} la donnée des $\mathrm{cof}\subset\mathrm{Fl}\,C$; \unsure{en se contentant} de prendre les flèches $i$ dans (\deleted{$\mathrm{cof}\cap W$}\inserted{$\unsure{\mathrm{Couniv.}W}$}) --- mais \deleted{\unsure{si}} on peut garder la construction, avec $\mathrm{cof}$ \inserted{\unsure{pas néc.}\ $=\mathrm{cof}_W$,} tel que $\mathrm{cof}\cap W\subset\deleted{\unsure{W}}\unsure{\mathrm{Couniv.}W}$]. \deleted{On} \inserted{Mais,} on veut prouver que ce foncteur transforme $f\in W$ en iso.
\diagram{\begin{tikzcd}
x \arrow[r,"f","\sim"'] & y \arrow[dr,"g?"'] & x \arrow[d,"i?","\sim"'] \\
&&\bar x
\end{tikzcd}}
on cherche $g,i$ tels que $(gf,i)\in\text{comp. conn. de }\uline{1}_x$ dans $\pi_0(\uline{\mathrm{Ch}}_0(x,x))$ et $(\bar f g,j)\in\text{comp. conn. de }\uline{1}_y$.
\diagram{\begin{tikzcd}
& x \arrow[r,"f","\sim"'] \arrow[d,"i","\sim"'] & y \arrow[d,"j"',"\sim"] \\
y \arrow[r,"g"'] & \bar x \arrow[r,"{\bar f\quad\sim}"',"\sim"] \arrow[ur,phantom,"(\text{cocart})" description] & \bar y
\end{tikzcd}}
\mspage{7}
"""
elements=[('text','upper left','4)'),('text','top paragraph','Cette composition est associative'),('diagram','upper quarter','x, x, x; 1, 1'),('text','right of first diagram','noté 1_x'),('text','upper middle','On a d’autre part des foncteurs'),('display','upper middle','Hom_C(x,y)_discret → Ch_0(x,y)'),('display','upper middle','f ↦ (f,Id_x)'),('text','middle','compatibles aux compositions. Ceci posé soit'),('display','middle','pi_0(x,y) = pi_0 Ch_0(x,y)'),('text','middle','alors la composition des Ch_0 définit'),('display','below middle','C → tilde C'),('text','lower middle','Pour l’instant, on n’a utilisé rien'),('diagram','lower left upper','x → y → bar x ← x; g?,i?'),('text','lower right','on cherche g,i tels que'),('diagram','bottom left','y → bar x → bar y; cocart'),('text','bottom left margin','7')]
notes='''The page passes from composition associative up to canonical isomorphism on Ch_0 to strictly associative composition on pi_0, claiming a category and functor C→tilde C. Associativity/coherence and the identity assertion receive no detailed verification here. It explicitly says “on veut prouver que ce foncteur transforme f∈W en iso” and seeks g,i with the two composites in identity components. The question marks are on g? and i? in the first lower diagram. The bracketed discussion about cof and couniversal weak equivalences has deletions and difficult compressed handwriting; do not regularize its criterion from the expected mathematics. The superscript attached to the first tilde C resembles 2 or a question mark, retained as doubtful.'''
if __name__=='__main__':save(106,8,tex,elements,notes=notes)
