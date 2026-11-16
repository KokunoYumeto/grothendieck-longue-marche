# Review of three calculations after the transcription freeze

**Scope.** This review uses the frozen text of cote 23 scans 009–014, the context
README and `notes/RESULTS_STATE.md`, and the primary reference identified below.
No manuscript image was opened and no transcription was changed. The two
counterexample computations and the operator proof below are the reviewer's
calculations, with high confidence in the algebra. Their interpretation of a
manuscript passage is kept separate from the calculation.

## 1. The real function algebra on the cyclic group of order three

### What the concrete example establishes

Put (C_3=\{0,1,2\}), with addition modulo three, and

\[
U=\mathbb R^{C_3},\qquad
(fg)(i)=f(i)g(i),\qquad
\Delta f(i,j)=f(i+j),\qquad \epsilon(f)=f(0).
\]

The identifications (U\otimes U=\mathbb R^{C_3\times C_3}) and

\[
(\Delta\otimes1)\Delta f(i,j,\ell)
=f(i+j+\ell)=(1\otimes\Delta)\Delta f(i,j,\ell)
\]

verify the algebra-homomorphism and coassociativity requirements directly;
interchanging (i,j) verifies cocommutativity. Let (e_i) denote the indicator
of (i). Then (I=\ker\epsilon=\mathbb Re_1\oplus\mathbb Re_2), and the reduced
coproduct (\delta f=\Delta f-f\otimes1-1\otimes f), for (f\in I), has

\[
\begin{aligned}
\delta e_1&=-2e_1\otimes e_1-e_1\otimes e_2-e_2\otimes e_1+e_2\otimes e_2,\\
\delta e_2&=e_1\otimes e_1-e_1\otimes e_2-e_2\otimes e_1-2e_2\otimes e_2.
\end{aligned}
\]

Thus the constant family (U_i=I) verifies exactly the finite-dimensional
union and (\delta)-stability clauses in the margin of 23/013, lines 35–38.

A normalized multiplicative element is determined by (a=g(1)), with

\[
g(0)=1,\qquad g(2)=a^2,\qquad a^3=1.
\]

The only real solution is (a=1), so (\gamma(U)=\{1\}). A primitive element
is determined by (b=f(1)), with (f(2)=2b) and (0=f(0)=3b); hence

\[
\pi(U)=0,\qquad U(\pi(U))=\mathbb R.
\]

The canonical map from this enveloping algebra into (U) is the constant
function map (r\mapsto(i\mapsto r)). It has one-dimensional image and omits
(e_1), whereas (U) has dimension three. This proves the insufficiency of the
**displayed marginal checklist read on its own** for the displayed
reconstruction (U\simeq U(\pi(U))). The computation does not supply a full
definition of the source's additional designation “de Cartier” (23/013,
lines 50–53).

There is also a direct functor check in the manuscript's infinitesimal-parameter
setting. A relative multiplicative element has (g(1)=1+n), with (n) in the
nilpotent augmentation ideal of the parameter algebra. Its equation is

\[
0=(1+n)^3-1=n(3+3n+n^2).
\]

The second factor is invertible, by a finite geometric series, so (n=0).
The relative primitive equation is (3b=0), giving (b=0). Thus both relative
functors in this example have only their identity/zero element, just as for
(U=\mathbb R).

### Earlier augmentation-ideal condition and the discrete restart

Scan 23/010, lines 23–24, explicitly writes
“on suppose que (I(U)^n\longrightarrow0) pour (n\to\infty).” The present
example violates that condition in the discrete topology:

\[
I^2=I,\qquad I^n=I\ne0\quad(n\ge1).
\]

The precise completion morphism is

\[
U\longrightarrow\varprojlim_n U/I^n=\mathbb R,\qquad f\longmapsto f(0);
\]

it kills the nonzero two-dimensional ideal (I). The example therefore has
no claim to satisfy the preceding separated topological setup with that
augmentation-adic condition.

The live text then starts again at the circled 3 on 23/011, lines 24–32,
with a discrete (k)-algebra and an infinitesimal parameter algebra
(\Lambda). The nearby proposed sentence about (I(U)) not being nilpotent
is deleted and must remain identified as deleted. The decisive live formulas
are on 23/012: lines 10–14 put nilpotence on (U\otimes I(\Lambda)), and
lines 15–19 introduce an augmentation of (U) optionally. With the displayed
parameter relation (I(\Lambda)^n=0), multiplication gives

\[
(U\otimes I(\Lambda))^n\subset U\otimes I(\Lambda)^n=0.
\]

This argument uses no nilpotence of (I(U)). The passage then says
“Supposons maintenant que (U) soit une hyperalgèbre ordinaire” (23/012,
lines 21–22). These explicit transitions support describing the example as a
test of the later written checklist within the discrete/parameter construction.
Its violation of the earlier condition must be reported alongside the test;
the deleted wording must not be promoted into a live hypothesis.

### The missing filtration property is visible by computation

In the basis above, (\delta:I\to I\otimes I) is injective. In fact, for a
tensor with coefficients (a,b,c,d) in the ordered basis
((e_1\otimes e_1,e_1\otimes e_2,e_2\otimes e_1,e_2\otimes e_2)), the map

\[
L(a,b,c,d)=-\frac{a+b}{3}e_1+\frac{a-2b}{3}e_2
\]

satisfies (L\delta=1_I). Tensoring this explicit left inverse with identity
maps gives left inverses for every iterated reduced coproduct. Consequently

\[
\ker\bigl(\delta^{[r]}:I\to I^{\otimes(r+1)}\bigr)=0
\quad\text{for every }r\ge1.
\]

The connected reduced-coproduct filtration therefore stays at the scalar
subspace and does not exhaust (U). This is the exact property absent from
the four literal margin clauses in this example.

The base-extension map (U\to\mathbb C\otimes_{\mathbb R}U) makes the issue
equally explicit. With (\zeta=e^{2\pi i/3}), the function
(\chi(i)=\zeta^i) is a nontrivial group-like element. For (h=\chi-1),

\[
\delta h=h\otimes h,\qquad
\delta^{[r]}h=h^{\otimes(r+1)}\ne0.
\]

Moreover, the dual multiplication is given on the evaluation basis by
(\lambda_i\lambda_j=\lambda_{i+j}). Hence the explicit algebra map

\[
U^\vee\simeq\mathbb R[t]/(t^3-1)
\longrightarrow\mathbb R\times\mathbb C,
\qquad p(t)\longmapsto(p(1),p(\zeta))
\]

is an isomorphism: the factors (t-1) and (t^2+t+1) are comaximal and have
degrees one and two. The augmentation point is the first projection. This
exhibits precisely how the single real character coexists with a nonlocal
dual algebra and additional geometric characters.

**Primary comparison.** Cartier's original definition explicitly includes an
increasing algebra filtration in axiom (HA3): Cartier, *Hyperalgèbres et groupes
formels*, Exposé 2, §1, Définition 1, beginning at printed p. 2-01 and continuing
on 2-02. [Catalog](https://www.numdam.org/item/SSL_1955-1956__2__A4_0/);
[PDF](https://www.numdam.org/item/SSL_1955-1956__2__A4_0.pdf).
The retrieved text layer omits the displayed HA3 equations; the filtration
failure above is established directly rather than attributed to an unread
formula. The parent reviewer has the exact PDF locator for its own inspection.

## 2. Operator proof of the derivation/automorphism equivalence

**Verdict: correct in the manuscript's rational setting.** On 23/014 the given
endomorphism (\xi\in\operatorname{End}_k(M)) is nilpotent; choose its bound
(\xi^n=0). The inherited rational setting is explicit on 23/011, line 3,
and again on 23/014, lines 36–37. No finite-dimensionality or projectivity of
(M) is used in the following calculation.

On (W=\operatorname{Hom}_k(M\otimes_kM,M)), define

\[
L\mu=\xi\mu,\quad
R_1\mu=\mu(\xi\otimes1),\quad
R_2\mu=\mu(1\otimes\xi),\quad T=L-R_1-R_2.
\]

The three operators commute by composition and the tensor identities, and
(L^n=R_1^n=R_2^n=0). Every monomial of total degree (3n-2) contains an
(n)-th power of one of them. Thus (T^{3n-2}=0). All exponential expressions
below are finite polynomials. With (g=\exp\xi), commuting the three operators
gives the exact identity

\[
\exp(T)\mu
=\exp(L)\exp(-R_1)\exp(-R_2)\mu
=g\,\mu(g^{-1}\otimes g^{-1}).
\]

Put (N=3n-2) and

\[
q(T)=\sum_{j=0}^{N-1}\frac{T^j}{(j+1)!}.
\]

Then (\exp(T)-1=Tq(T)). The endomorphism (q(T)-1) is nilpotent, so its
finite geometric-series inverse proves (q(T)) invertible; it also commutes
with (T). Consequently the two kernels are equal:

\[
\ker T=\ker(\exp(T)-1).
\]

For the given bilinear product (\mu), the left kernel condition is exactly
the displayed Leibniz equality, and the right kernel condition, composed with
(g\otimes g), is exactly

\[
g\mu=\mu(g\otimes g).
\]

The inverse of (g) is (\exp(-\xi)), and (g-1=\xi q(\xi)) is nilpotent.
This supplies the missing proof for the two displayed conditions on 23/014,
lines 22–29. The calculation applies directly to the manuscript's arbitrary
bilinear multiplication; no associativity assumption has been added.

## 3. Literal product on the logarithm line

**Verdict: the proposed dual-number calculation is correct.** For the concrete
algebra (A=\mathbb Q[\varepsilon]/(\varepsilon^2)), put
(g=g'=1+\varepsilon). These elements commute, their logarithms are defined
by the manuscript's finite series, and

\[
\log(gg')=\log(1+2\varepsilon)=2\varepsilon\ne0,
\qquad
(\log g)(\log g')=\varepsilon^2=0.
\]

This tests exactly the juxtaposed product on frozen 23/009, line 27. It
establishes a discrepancy in that literal formula. It does not license a
post-freeze correction or establish what additional ink was intended.

## Context and register check

The context README and `notes/RESULTS_STATE.md` were read first. The register
has no matching settled, open, or intake entry for these exponential or
hyperalgebra calculations. Searches for `Cartier`, `hyperalg`, `Campbell`,
`Hausdorff`, `Poincaré`, `exponentielle`, `logarithme`, and `primitif` in the
supplied context returned only the Cartier-name occurrence in
`ega_fr/EGA_chap0_ega0-21.tex`, §21.7, whose displayed subject is the rank formula
for field-extension differentials and imperfection modules. The register's
planning entry **WG2 §2.1 #2** supplies planning provenance; it does not settle
any of the three calculations here. No claim from an earlier AI-generated
research note was used as a proved premise.
