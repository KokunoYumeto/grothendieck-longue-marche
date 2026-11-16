import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{38}
\mspage{15}
\uline{Corollary} Assume \deleted{$\Phi_0$ is \unsure{sm}}

$a)$ $\Phi_0$ is small, source and target of any $g\in\Phi_0$ are accessible

$b)$ $M$ stable by filtering direct limits, \deleted{and by \illegible{3}}

\textcircled{$c$} \deleted{\unsure{any amalgamated}} \inserted{For any} diagram
\diagram{\begin{tikzcd}
A\arrow[r,"v"]\arrow[d,"\alpha"']&X\\B&
\end{tikzcd}}
with $\alpha\in\Phi_{\deleted{\unsure{0}}}$, the amalgamated sum exists
\diagram{\begin{tikzcd}
A\arrow[r,"v"]\arrow[d,"\alpha"']&X\arrow[d,"\alpha'"]\\
B\arrow[r,"u'"']&X'
\end{tikzcd}}
and $\alpha'\in\Phi$.
\margin{NB $c')$ $\Phi$ stable under composition}

\textcircled{$d$} $\Phi$ ``stable by \inserted{filtering} direct limits''
\margin{! It is enough to know it wrt. ordered sets $I$ where Sup of any two elements exists.}

Then $(\Phi,\Psi)$ satisfy the factorization condition, and \deleted{\unsure{more}} even, there exists a functor $\overline\Sigma$:
\deleted{Ex}
\diagram{\begin{tikzcd}
\underline{\mathrm{Fl}}(M)\arrow[rr,no head,"\overline\Sigma"]\arrow[dr,"t"']&&\underline{\mathrm{Fl}}(M)\arrow[dl,"t"]\\
&M&
\end{tikzcd}};
and a functorial morphism $\unsure{\xi}$ in $[\underline{\mathrm{Cat}}]/M$
\margin{possibly ``large'' categories over $M$}
\[
\deleted{\unsure{f\longrightarrow}}\quad\mathrm{id}_{\underline{\mathrm{Fl}}(M)}\longrightarrow\overline\Sigma.
\]
with $i(f)\in\Phi$, $p(f)\in\Psi$
\diagram{\begin{tikzcd}
X\arrow[r,"i(f)"]\arrow[d]&\overline X(f)\arrow[dl,"\unsure{p}(f)"]\\Y&
\end{tikzcd}}

\uline{Example} Assume that $M$ is stable by amalgamated sums.
Take $\Phi=\overline\Phi_0=\Psi^*$. Then $c)$ \deleted{and $d)$} is trivially satisfied.
What about $d)$? To get \deleted{extensions of} \inserted{the dotted $\varphi$}, we make a Zorn induction on pairs $(\unsure{J\subset I|J\in I},u_J:\overbrace{\varinjlim_{i\in J}A_i}^{A_J}\to X)$ \inserted{(filtering \unsure{subset})} such as to the diagram
\margin{\unsure{for compact limits}}
\diagram{\begin{tikzcd}
\underset{\unsure{g}}{A_{i_0}}\arrow[r]\arrow[d,"u_0"']&A_i\arrow[r]&\underline B=\varinjlim A_i\arrow[d,"v"]\arrow[dll,dashed,"\varphi"']\\
X\arrow[rr,"f","\in\Psi"']&&Y
\end{tikzcd}}
\diagram{\begin{tikzcd}
A_{i_0}\arrow[r]\arrow[rr,bend left=20]\arrow[d,"u_0"']&A_J\arrow[r]\arrow[dl,"u_J"]&\underline B\arrow[d]\\
X\arrow[rr,"f"']&&Y
\end{tikzcd}}
commute, with obvious order relation, \deleted{This is clearly}
\margin{induction}
\[
\operatorname{Hom}(B,X)\unsure{\longrightarrow|\text{---}}\begin{gathered}\operatorname{Hom}(g,f)\\\Vert\\\varprojlim\operatorname{Hom}(g_i,f)\end{gathered}\quad\text{surjective}
\]
\mspage{37}
'''
e=[('text','top','15'),('text','top','Corollary Assume'),('deletion','top','Phi0 is sm'),('text','upper a','Phi0 is small'),('text','upper b','M stable by filtering direct limits'),('deletion','upper b','and by'),('text','upper c','diagram'),('deletion','upper c','any amalgamated'),('insertion','upper c','For any'),('diagram','upper right','A X B'),('text','upper middle','with alpha in Phi'),('deletion','upper middle','subscript0'),('diagram','upper middle','A X B Xprime'),('display','middle','alpha prime in Phi'),('margin note','middle right','NB cprime Phi stable under composition'),('text','middle d','Phi stable by direct limits'),('insertion','middle d','filtering'),('margin note','middle right','It is enough to know'),('text','middle','Then Phi Psi satisfy'),('deletion','middle','more'),('deletion','middle left','Ex'),('diagram','middle','Fl(M) Fl(M) M'),('text','middle lower','and a functorial morphism'),('margin note','right','possibly large categories over M'),('display','middle lower','id Fl(M) to Sigma bar'),('deletion','middle lower','f to'),('display','middle lower','i(f) in Phi p(f) in Psi'),('diagram','left','X Xbar(f) Y'),('text','lower','Example Assume M'),('display','lower','Phi=barPhi0=Psi star'),('deletion','lower','and d'),('text','lower','What about d'),('deletion','lower','extensions of'),('insertion','lower','the dotted phi'),('text','lower','we make a Zorn induction'),('display','lower','pairs J subset I uJ'),('insertion','lower','filtering subset'),('margin note','lower diagonal','for compact limits'),('diagram','lower left','Ai0 Ai B X Y'),('diagram','lower right','Ai0 AJ B X Y'),('text','lower right','commute with obvious order relation'),('deletion','lower right','This is clearly'),('margin note','bottom left','induction'),('display','bottom','Hom(B,X) Hom(g,f) inverse limit'),('text','bottom left','37')]
record_page(38,s,e,'reused_typed',notes='Corollary summarizes factorization and functoriality; example Phi=barPhi0 asks What about d)? and starts a Zorn argument for stability by filtering limits. Underlined marginal phrase above the left lower diagram is difficult (tentatively for compact limits). Plain top horizontal functor stroke retained without an inferred arrowhead.')
build_doubts()
