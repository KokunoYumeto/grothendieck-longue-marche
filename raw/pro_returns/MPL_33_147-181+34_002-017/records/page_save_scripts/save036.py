import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{36}
\mspage{14}
$\pi_g$ is the smallest cardinal s.th. source and target of $g$ are $\pi$-accessible.

\uline{Example} If the objects occurring as sources and targets of $g$'s in $\Phi_0$ are ``of finite presentation'', i.e. $\operatorname{Hom}(A,-)$ commutes with any filtering direct limits, we get $\pi=0$. In this case we stop the induction with $\alpha_0=$ first infinite ordinal \deleted{the first}. In case the objects $A,B$ are not of finite presentation, (\unsure{still|but} they are accessible
--- we take the smallest cardinal such that $\operatorname{Hom}(A,?)$ commutes with direct limits indexed by \deleted{\unsure{ordi}} directed sets \deleted{great} \inserted{large} w.r. $\pi$.
Let \inserted{then} $\alpha_0$ be the first ordinal s.th. the set
\[
I_{\alpha_0}=\{\text{all ordinals }\alpha\text{ with }\alpha<\alpha_0\}
\]
be \deleted{great} large wrt $\pi$. We take the factorization
\diagram{\begin{tikzcd}
X\arrow[r,"i_{\alpha_0}(f)=i(f)"]\arrow[d]&X_{\alpha_0}(f)=\deleted{\Sigma}\unsure{\overline X}(f)\arrow[dl,"\Sigma_{\alpha_0}(f)=p(f)"]\\
Y&
\end{tikzcd}}
and we get $i(f)\in\Phi$, $p(f)\in\Psi$, provided we make the following assumptions;

$d)$ The \deleted{\unsure{elem}} source and target objects of the arrows of $\Phi_0$ are \uline{accessible}
(ok if $M$ a topos etc ---) and, if $\pi_0$ is the cardinality of the smallest ordinal number \inserted{$\alpha_0$} s.th. for any such $A$, $\operatorname{Hom}(A,-)$ commutes to the direct limits of type $I_{\alpha_0}$, \deleted{\unsure{we}} and \deleted{$\pi=\sup(\unsure{\pi}$}
$\pi=\sup(\pi_0,\operatorname{card}\Phi_0)$ \inserted{rather, $\sigma$}, we assume that for any filtering direct system with an indexing set $I$ of cardinality $\leq\pi$, and transition maps in $\Phi$, the direct limit exists and \deleted{$\unsure{X_n}$} $Z_i\to Z$ are equally in $\Phi$.

Then we get, not only factorization $f=pi$, with $i\in\Phi$, $p\in\Psi$, but even factorization $\uline{\overline X}(f)$ \uline{functorial} with respect to variable $f$.
\mspage{35}
'''
e=[('text','top','14'),('text','top','pi_g is the smallest cardinal'),('text','upper','Example If the objects'),('deletion','upper','the first'),('text','upper middle','In case the objects A B'),('deletion','upper middle','ordi'),('deletion','upper middle','great'),('insertion','upper middle','large'),('text','upper middle','Let alpha0'),('insertion','upper middle','then'),('display','middle','Ialpha0 all ordinals'),('deletion','middle','great'),('text','middle','large wrt pi We take'),('diagram','middle','X Xalpha0(f) Y'),('deletion','middle diagram','Sigma'),('text','middle','and we get'),('text','lower','d The source and target objects'),('deletion','lower','elem'),('insertion','lower','alpha0'),('deletion','lower','we'),('deletion','lower','pi=sup(pi'),('display','lower','pi=sup(pi0 cardPhi0)'),('insertion','lower','rather sigma'),('text','lower','we assume that for any'),('deletion','lower','X_n'),('display','lower','Z_i to Z'),('text','bottom','Then we get not only'),('text','bottom left','35')]
record_page(36,s,e,'reused_typed',notes='Continuation of scan034: finitely presented case pi=0 and first infinite ordinal; accessible-object and cardinal conditions; final explicit claim of a functorial factorization. No new proof of the accessibility hypotheses is supplied here; the text has several revised bounds.')
build_doubts()
