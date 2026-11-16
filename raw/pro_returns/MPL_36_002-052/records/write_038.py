from save_page import save
tex=r'''
\scanpage{38}

\begin{center}-- 98 --\end{center}
\margin{n\textsuperscript{o} 316}

un automorphisme de $E$.

Si en outre $E$ est une algèbre (non nécessairement associative), et si $u$ est une dérivation (nilpotente) de $E$, alors $e^u$ est un automorphisme de \uline{l'algèbre} $E$. En effet, si $x,y\in E$, on a
\[
u^p(xy)=\sum_{r+s=p}\binom{p}{r}u^r(x)u^s(y)
\]
pour tout entier $p\geq0$ (formule de Leibniz). Il en résulte que :
\[
\begin{aligned}
e^u(xy)&=\sum_{p\geq0}\frac{1}{p!}u^p(xy)=\sum_{p\geq0}\sum_{r+s=p}\frac{u^r(x)}{r!}\frac{u^s(y)}{s!}\\
&=\sum_{r,s=0}^\infty\frac{u^r(x)}{r!}\frac{u^s(y)}{s!}=e^u(x)e^u(y)
\end{aligned}
\]
d'où notre assertion.

Soit maintenant $\mathfrak g$ une algèbre de Lie. Si $x$ appartient au radical nilpotent de $\mathfrak g$, la dérivation $\operatorname{ad}_{\mathfrak g}x$ de $\mathfrak g$ est nilpotente. On peut donc poser la définition suivante :

\uline{Définition} 5 -- \uline{On appelle automorphisme spécial de} $\mathfrak g$ \uline{un automorphisme de} $\mathfrak g$ \uline{de la forme} $e^{\operatorname{ad}x}$, \uline{où} $x$ \uline{est dans le radical nilpotent de} $\mathfrak g$.

Il est clair qu'un automorphisme spécial laisse stable tout idéal de $\mathfrak g$.

\uline{Définition} 6 -- \uline{Soient} $\mathfrak g$ \uline{une algèbre de Lie}, $\unsure{\mathfrak r|r}$ \uline{son radical}. \uline{On appelle sous-algèbre de Levi de} $\mathfrak g$ \uline{toute sous-algèbre supplémentaire de} $\mathfrak r$ \uline{dans} $\mathfrak g$.

Une sous-algèbre de Levi est isomorphe à $\mathfrak g/\mathfrak r$, donc semi-simple. Comme une sous-algèbre semi-simple n'a que $0$ en commun avec $\mathfrak r$, toute sous-algèbre semi-simple $\unsure{\mathfrak h|h}$ telle que $\mathfrak g=\mathfrak r+\mathfrak h$ est une sous-algèbre de Levi ; par conséquent, l'image d'une sous-algèbre de Levi par un homomorphisme surjectif est une sous-algèbre de Levi.
\margin{37}
'''
e=[('text','readable top centre','- 98 -'),('margin note','readable top right','n°316'),('text','first line','un automorphisme de E'),('text','upper paragraph','Si en outre E est une algèbre ...'),('display','upper middle','u^p(xy)=sum binomial(p,r) u^r(x)u^s(y)'),('text','between displays','pour tout entier p>=0 (formule de Leibniz)'),('display','middle two-line chain','e^u(xy)=sum 1/p! u^p(xy)=...=e^u(x)e^u(y)'),('text','below chain','d’où notre assertion'),('text','middle Lie paragraph','Soit maintenant g une algèbre de Lie'),('text','Définition 5','On appelle automorphisme spécial ... e^(ad x)'),('text','following definition','Il est clair qu’un automorphisme spécial laisse stable tout idéal'),('text','Définition 6','Soient g une algèbre de Lie, r son radical'),('text','bottom paragraph','Une sous-algèbre de Levi ... homomorphisme surjectif'),('margin note','original bottom left','37')]
d=[{'line':'Définition 6 radical symbol','reading':'fraktur r','alternatives':'italic r; faded small type','confidence':'medium'},{'line':'bottom semisimple subalgebra symbol','reading':'fraktur h','alternatives':'italic h; small type','confidence':'medium'}]
save(38,tex,e,d,'Reused blue typescript, upside down; rotated whole and both halves read. Printed page “- 98 -”, “n°316”, pencil 37. It is a Lie-algebra text: exponential of nilpotent derivations, special automorphisms, Levi subalgebras, and their surjective images. Do not attribute these reused textbook claims to an original conjecture of the handwritten Picard notes. The field/base hypotheses lie outside the supplied excerpt. Retain explicit “Il est clair” as an unproved assertion in the supplied page, with this provenance qualification.',sheet_kind='reused_typed')
