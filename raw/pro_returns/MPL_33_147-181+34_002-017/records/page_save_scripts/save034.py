import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{34}
\mspage{13}
\margin{\uline{Factoriza-tion} \uline{Problem}}
\margin{$\unsure{\Phi_0}$ given, $\unsure{\Phi}$ variable. \deleted{NB we need only $\unsure{\Phi}$}}
$M$ a category, $\Phi_0\subset\mathrm{Fl}(M)$, $\Psi=(\Phi_0^{\deleted{*}})_*$, $\Phi_0\subset\Phi\subset\overline\Phi_0=\Psi^*$, we want to deduce conditions on $\Phi_0,\Phi$ insuring that the pair $(\Phi,\Psi)$ satisfies factorization condition, i.e.
\[
\forall f\in\mathrm{Fl}(M),\quad\exists\text{ factorization }f=pi,\quad i\in\Phi,\quad p\in\Psi.
\]
\margin{NB. we do not use $\Phi\subset\unsure{\overline\Phi_0|\Phi_0}$.}
The idea is to take \inserted{(for given $f$)} all diagrams
\diagram{\begin{tikzcd}
A\arrow[r,"v"]\arrow[d,"g"']&X\arrow[d,"f"]\\
B\arrow[r,"u"']&Y
\end{tikzcd}} $(D)$ with $g\in\Phi_0$
giving rise to
\diagram{\begin{tikzcd}
A\arrow[r,"v"]\arrow[d,"\unsure{a|g}"']\arrow[dr,phantom,"\mathrm{coc}"]&X\arrow[d,"\unsure{i_D|g_D}"]\arrow[dd,bend left=55,"f"]\\
B\arrow[r]&X_D=X\amalg_A B\arrow[d,"p_D"]\\
&Y
\end{tikzcd}}
and to define $\deleted{\unsure{\Sigma_1}(f)}\inserted{X_1(f)}=\deleted{\varinjlim}\coprod_{\text{all }D}(X)\,X_D$ (amalgamated sum under $X$)
so that we get factorization
\diagram{\begin{tikzcd}
X\arrow[r,"i_1(f)"]\arrow[d,"f"']&\deleted{\Sigma}X_1(f)\arrow[dl,"\Sigma_1(f)"]\\
Y&
\end{tikzcd}}
\deleted{with} (hopefully) $i_1(f)\in\Phi$.

For this first step, we need

$a)$ $\Phi_0$ is small (we'll see later how to relax this condition)

$b)$ Amalgamated sums indexed by $I$ with $\operatorname{card}I\leq\operatorname{card}\Phi_0$ exist in $M$, \deleted{and}
\inserted{rather, $\overbrace{\operatorname{card}\Phi_0\times c}^{\sigma}$, where $c$ is $\sup(\operatorname{card}\operatorname{Hom}(A,X)\times\operatorname{card}\operatorname{Hom}(B,Y))$ for $\unsure{u|g}:A\to B$ in $\Phi_0$}

$c)$ $\Phi_{\deleted{\unsure{0}}}$ stable by \inserted{\uline{Composition, and by}} cobase extensions, and \inserted{$(d_0)$} by filtering direct limits \inserted{all} indexed by a set $I$ of cardinality $\leq\operatorname{card}\Phi_0$ \inserted{\unsure{v. thus} $\leq\sigma$}.
\margin{do with \unsure{strengthened}}

We then are making a transfinite induction to define $X_\alpha(f)$ and
\diagram{\begin{tikzcd}
X\arrow[r,"i_\alpha(f)"]\arrow[d,"f"']&X_\alpha(f)\arrow[dl,"\Sigma_\alpha(f)"]\\
Y&
\end{tikzcd}}
$i_\alpha(f)\in\Phi$
with $\alpha$ any ordinal \deleted{$\unsure{\Phi}$} $<\alpha_0$ ($\alpha_0$ \deleted{first} ordinal \deleted{\unsure{of the cardinal}\illegible{2}} \inserted{number to be fixed} \deleted{\unsure{define later in terms of $\pi$}} \inserted{later}).
\[
\left\{\begin{aligned}
\Sigma_{\alpha+1}(f)&=\Sigma_1(\Sigma_\alpha(f)),\quad X_{\alpha+1}(f)=\text{source}\,\Sigma_{\alpha+1}(f),\quad i_{\alpha+1}(f)=\text{composition}\\[4em]
\Sigma_\alpha(f)&=\varinjlim_{\alpha'<\alpha}\Sigma_{\alpha'}(f)\quad\text{if $\alpha$ is a limiting ordinal.}
\end{aligned}\right.
\]
\diagram{\begin{tikzcd}
X\arrow[r,"i_\alpha(f)"]\arrow[d,"f"']&X_\alpha(f)\arrow[r,"i_1(\Sigma_\alpha(f))"]\arrow[dl,"\Sigma_\alpha(f)"]&X_{\alpha+1}(f)\arrow[dll,"\Sigma_{\alpha+1}(f)=\Sigma_1(\Sigma_\alpha(f))"]\\
Y&&
\end{tikzcd}}
\deleted{We} We assume that $\Phi$ is stable too by \inserted{the} filtering direct limits \deleted{of cardinality $\leq c$} which occur in the several transfinite induction steps.
Let $\pi$ be a cardinal such that \deleted{all objects of $\Phi_0$} \inserted{for any $g\in\Phi_0$, source and target of $g$} are $\pi$-\unsure{access. ob.}
--- i.e. $\operatorname{Hom}(A,-):M\to\mathrm{Sets}$ commutes to filtering direct limits which are \deleted{\unsure{great wr}} ``large with resp. to $\pi$''. We may take $\pi=\sup_{g\in\Phi_0}\pi_g$, where
\mspage{33}
'''
e=[('text','top','13'),('margin note','upper left','Factorization Problem'),('margin note','upper left diagonal','Phi0 given Phi variable'),('deletion','upper left','NB we need only'),('text','top','M a category'),('deletion','top formula','star above Phi0'),('display','upper','for all f exists factorization'),('margin note','top','NB we do not use'),('text','upper','The idea is to take'),('insertion','upper','for given f'),('diagram','upper left','A X B Y (D)'),('text','upper','with g in Phi0 giving rise to'),('diagram','upper right','A X B XD Y'),('text','upper middle','and to define'),('deletion','upper middle','Sigma1(f)'),('insertion','upper middle','X1(f)'),('deletion','upper middle','lim'),('display','upper middle','coproduct XD under X'),('text','middle','so that we get factorization'),('diagram','middle','X X1(f) Y'),('deletion','middle diagram','Sigma'),('deletion','middle','with'),('text','middle','hopefully i1(f) in Phi'),('text','middle','For this first step'),('text','middle a','Phi0 is small'),('text','middle b','Amalgamated sums'),('deletion','middle b','and'),('insertion','right margin','rather cardPhi0 times c sigma'),('text','middle c','Phi stable'),('deletion','middle c','subscript0'),('insertion','middle c','Composition and by'),('insertion','middle c','d0'),('insertion','middle c','all'),('insertion','middle c right','v. thus <=sigma'),('margin note','left middle','do with strengthened'),('text','lower middle','We then are making'),('diagram','lower middle','X Xalpha(f) Y'),('text','lower middle','with alpha any ordinal'),('deletion','lower middle','Phi'),('deletion','lower middle','first'),('deletion','lower middle','of the cardinal'),('insertion','lower middle','number to be fixed'),('deletion','lower middle','define later in terms'),('insertion','lower middle','later'),('display','lower','successor and limit Sigmaalpha'),('diagram','lower right','X Xalpha Xalpha+1 Y'),('deletion','bottom','We'),('text','bottom','We assume that Phi'),('insertion','bottom','the'),('deletion','bottom','of cardinality <=c'),('text','bottom','Let pi be a cardinal'),('deletion','bottom','all objects of Phi0'),('insertion','bottom','for any g source and target'),('text','bottom','i.e. Hom(A,-)'),('deletion','bottom','great wr'),('display','bottom','pi=sup pi_g'),('text','bottom left','33')]
record_page(34,s,e,'reused_typed',notes='Factorization construction with changing size bounds and explicit hopefully; Phi0 small condition is promised a later relaxation. Several cancelled ordinal/cardinal words and the cramped side notes remain uncertain. No context consulted.')
build_doubts()
