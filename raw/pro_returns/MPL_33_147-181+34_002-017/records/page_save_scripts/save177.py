import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,177,r'''\scanpage{177}
\mspage{67}
\margin{176}

Note that $C_n^{\unsure{v|\nu}}$ is an even function for $n$ even and an odd function for $n$ odd, hence we have
\[
\gamma_n=\begin{cases}
\displaystyle\frac{w_p}{C_n^{1/2\,p}(1)}\,i\pi\int_0^1 C^{1/2\,p}(x)(1-x^2)^{1/2\,p-1/2}\,dx&n\text{ odd}\\[1.5ex]
\displaystyle-\frac{2w_p}{C_n^{1/2\,p}(1)}\int_0^1\log x\ C_n^{1/2\,p}(x)(1-x^2)^{1/2\,p-1/2}\,dx&n\text{ even}
\end{cases}
\]
the result is then proved by evaluating these integrals (see [18a]).

\uline{4.5 Reduction of a singular equation to the Fredholm case}.

We now return to the algebra $\mathcal{G}$ of singular operators on $M$. For each $J\in\mathcal{G}$ and each $x\in M$ we shall define the symbol of $J$ at $x$; this will be a function on $S_x$. Let $\mathbb{H}_xJ$ be the homogeneous part of $J$ at $x$; we define $\mathbb{S}_xJ=\mathbf{S}\mathbf{H}_xJ$, thus $\mathbf{S}_x$ is the composition of the homomorphism $\mathbb{H}_x$ and the isomorphism $\mathbb{S}$.

\uline{Definition 4.5.1.} If $J\in\mathcal{G}$ then the \uline{global symbol} of $J$ is a function on the tangent sphere bundle $S(M)$ defined by
\[
\mathbb{S}_MJ(b)=\mathbf{S}_{\pi(b)}J(b).
\]
Note that $\mathbf{S}_MJ=0$ implies that $\mathbb{H}_xJ=0$ for all $x\in M$ and $J\in\bigcap_{x\in M}\mathcal{F}_x=\mathcal{F}$, so $J$ is completely continuous.
''',[
('text','top center','67'),('margin note','upper corner inverted','176'),('text','upper','Note that C_n^v'),('display','upper middle','gamma_n two-case integral formula'),('text','middle','the result is then proved'),('text','heading','4.5 Reduction of a singular equation to the Fredholm case'),('text','middle lower','We now return to the algebra G'),('text','lower','Definition 4.5.1. If J in G'),('display','lower','S_M J(b) = S_pi(b) J(b)'),('text','bottom','Note that S_M J=0')],sheet_kind='reused_typed',remarks='Original whole, rotated upright whole and both upright halves read. Reused English text on singular operators, internal p67. The first integral contains C with no visible n subscript, unlike its denominator and the second integral; retained. The parameter glyph in C_n^v could be Latin v or Greek nu and is marked. Outlined double-struck H/S and solid bold H/S vary in the typewritten symbols and are distinguished literally in LaTeX; they may be impressions of the same overtyped letter rather than different mathematical alphabets. Handfilled gamma, script G and F, integrals and pi are transcribed as the original typescript notation, not editorial insertions.')
