import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,179,r'''\scanpage{179}
\mspage{68}
\margin{178}

Let $\mathcal{S}_M$ be the algebra of $C^\infty$ functions on $S(M)$; then:

\uline{Theorem 4.5.2.} The map $\mathbf{S}_M:\mathcal{G}\longrightarrow\mathcal{S}_M$ is an epimorphism whose kernel is $\mathcal{F}$, the ideal of completely continuous operators.

Our problem now is to ``regularize'' the equation
\[
(4.5.3)\qquad J\rho=f
\]
that is to reduce it to an equation of Fredholm type. We wish to find an operator $K\in\mathcal{G}$ such that the equation $KJ\rho=Kf$ is of Fredholm type and has the same solutions as the original equation.

Now, if $KJ=Kf$ is of Fredholm type this means that $KJ=I+L$ where $L\in\mathcal{F}$ and then $\mathbb{S}_MKJ=1$. Hence a necessary condition for the existence of a reduction is $\mathbb{S}_MJ(b)\neq0$ for all $b\in S(M)$. This condition is also sufficient:

\uline{Theorem 4.5.4.} If $J\in\mathcal{G}$ then the equation $J\rho=f$ can be regularized if and only if $\mathbf{S}_MJ(u)\neq0$ for all $u\in S(M)$.

\uline{Proof:} We must find an operator $K\in\mathcal{G}$ such that $KL=Kf$ has the same solutions as (4.5.3) and is of Fredholm type. Let $K_1$ be any operator such that $\mathbf{S}_MK_1\cdot\mathbf{S}_MJ=1$; then clearly:
''',[
('text','top center','68'),('margin note','upper corner inverted','178'),('text','upper','Let S_M be the algebra'),('text','upper','Theorem 4.5.2. The map'),('text','middle','Our problem now is to regularize'),('display','middle','(4.5.3) J rho=f'),('text','middle','that is to reduce it'),('text','lower middle','Now, if KJ=Kf'),('text','lower','Theorem 4.5.4'),('text','bottom','Proof: We must find')],sheet_kind='reused_typed',remarks='Original whole, upright whole and both upright halves read. Internal p68 continues the singular-operator text p67 on scan177. Literal KJ=Kf in the middle paragraph and KL=Kf in the proof are retained; no rho or J has been supplied to repair those lines. Double quotation marks regularize use the required LaTeX convention. Script S_M differs from the bold/doubled symbol map S_M.')
