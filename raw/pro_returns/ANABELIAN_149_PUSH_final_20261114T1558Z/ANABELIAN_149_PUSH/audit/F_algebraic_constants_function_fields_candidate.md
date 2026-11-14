# Candidate F.45: function fields over algebraic constants

Status: independently reviewed by root and degeneration; integrated as F.45 in
`sections/F_algebraic_constants_extension.tex`. This file is retained as the
complete pre-integration audit. The convention throughout is the actual CHW
closed-point-preserving relative convention. The literal incomplete R27
definition remains refuted by F.1 and F.17.

## 1. Proposed theorem and its boundary

Let \(L/\overline{\mathbf Q}\) be a finitely generated field extension of
positive transcendence degree. Then étale-topos reconstruction holds over
\(L\). More generally it holds over every subfield \(k_0\subset L\) with
\(\operatorname{trdeg}_{\mathbf Q}k_0>0\): for all finite-type
\(k_0\)-schemes \(X,Y\),
\[
 \operatorname{Hom}_{k_0}(X^{\mathrm{awn}},Y)
 \longrightarrow
 \pi_0\operatorname{Hom}^{\mathrm{cp}}_{BG_{k_0}}
       (X_{\mathrm{et}},Y_{\mathrm{et}})
\]
is bijective.

In particular this would give reconstruction over
\(\overline{\mathbf Q}(t)\), a sufficient class not covered by F.44.
The positive-transcendence-degree restriction is essential: the algebraic
subfield \(\overline{\mathbf Q}\) itself fails reconstruction by F.41.
No characterization of every characteristic-zero field is asserted.

The new argument replaces the arithmetic Gauss valuations in F.35/F.43
by geometric divisorial valuations. The latter remain unramified under
every algebraic extension of the constants. This removes, rather than
assumes, the earlier missing-number-field hypothesis.

## 2. Field predicates and exact Hilbert input

Every finite extension \(L'/L\) is again finitely generated of the same
positive transcendence degree over \(\overline{\mathbf Q}\). Its constants
algebraic over \(\overline{\mathbf Q}\) are just
\(\overline{\mathbf Q}\), since that field is algebraically closed. For
such a field,
\[
 D((L')^\times):=\bigcap_{n\ge1}((L')^\times)^n
       =\overline{\mathbf Q}^{\times}.                 \tag{Q1}
\]
Indeed use a normal proper model over \(\overline{\mathbf Q}\). An element
divisible by every positive integer has zero valuation at every prime
divisor. A rational function with zero divisor on a normal proper integral
variety is a global invertible function, hence a constant. Conversely every
nonzero algebraic constant has all its roots among the constants. The same
argument applies to every further finitely generated extension used below.

Such an \(L'\) is Hilbertian by Bary-Soroker–Paran, Theorem 1.2 and
Corollary 3.2, printed pp.2 and16 of the opened author PDF. The theorem
explicitly permits an arbitrary field of constants and a finitely
generated **transcendental** extension. It gives the stronger property of
full Hilbertianity; ordinary Hilbertianity is all that is needed here.

Consequently every prescribed finite quotient of the arithmetic
fundamental group of a smooth geometrically connected \(L'\)-curve is
detected by a closed-point decomposition group, and the detecting degrees
are unbounded. To prove this, let \(Y\to U\) be the corresponding connected
finite \(G\)-torsor. Choose a finite separable map from the smooth proper
completion of \(U\) to \(\mathbf P^1\), of arbitrarily large degree
\(n\), by Riemann–Roch. Remove the finite set of branch and omitted-point
images. The composite \(Y\to\mathbf P^1\) is then finite étale and
connected of degree \(n|G|\). Hilbert specialization making this entire
fibre one field produces a single closed point \(x\in U\) of degree
\(n\), and the residual \(G\)-torsor over \(x\) is connected. Its
decomposition image is all of \(G\). Finite sets to be avoided can be
included in the removed locus. The full-group specialization formulation
is Serre, Proposition 3.3.1; equivalently apply Hilbert irreducibility to
the primitive element of this composite function-field extension.

For a smooth geometrically connected quasiprojective variety, reduce a
given connected finite cover to a smooth curve on which it stays connected
by the cover-preserving Bertini construction already proved in F.29. This
retains the arithmetic constant field: every geometric component stays
irreducible, and the Galois action remains transitive on the components.
The curve result therefore detects arbitrary **arithmetic**, not merely
geometric, finite quotients on the variety. The point and value fields can
be made simultaneous by taking the joint finite quotient.

All finite data over \(L\) descend to a finitely generated
\(F/\mathbf Q\) with
\[
                    L=F\overline{\mathbf Q}.             \tag{Q2}
\]
Moreover \(L/F\) is algebraic Galois, because it is the compositum with
the normal algebraic extension \(\overline{\mathbf Q}/\mathbf Q\).
In a common separable closure this gives
\(G_L\triangleleft G_F\). A finite collection of elements of finite
extensions of \(L\), including actual point values, lies in
\(M\overline{\mathbf Q}\) for one finite extension \(M/F\), after
enlarging the finite descent field to contain the finitely many constants
occurring in their equations. No finite-generation assertion about
\(\overline{\mathbf Q}/\mathbf Q\) is being made.

## 3. The moved geometric divisor lemma

**Lemma.** Let \(M/\mathbf Q\) be finitely generated of positive
transcendence degree. Put \(C=M\cap\overline{\mathbf Q}\), a number
field, so that \(M/C\) is regular. Suppose
\(\sigma\in\operatorname{Aut}_C(M)\) is nonidentity and of finite order.
Given finitely many elements to be units, and an integer \(r\), after one
finite normal extension of the number-field constants there are discrete
geometric valuations \(v_1,\ldots,v_r\) such that:

1. the \(2r\) valuations \(v_i,\sigma^{-1}v_i\) are pairwise distinct;
2. all prescribed elements, and their required \(\sigma\)-translates,
   are units at these valuations;
3. each valuation is normalized with value group \(\mathbf Z\), has
   characteristic-zero infinite residue field, and is trivial on the
   constants;
4. each prolongation to \(M\overline{\mathbf Q}\) has the same value
   group \(\mathbf Z\).

Here the enlarged \(M\) and the extension of \(\sigma\), acting trivially
on the enlarged constants, are used in the conclusion.

**Proof.** Construct a \(\sigma\)-stable normal affine model of \(M/C\)
by adjoining the finite orbit of a finite set of generators and
normalizing; normalization is finite for a finite-type algebra over a
field. Intersect the translates of its smooth locus and remove the zeros
and poles of the prescribed elements and their translates. This is still
a nonempty \(\sigma\)-stable smooth quasiprojective model \(Z/C\).
Since \(\sigma\ne1\), its fixed locus is a proper closed subset.

Choose a \(\overline{\mathbf Q}\)-point \(z\) outside that fixed locus
and outside the finitely many excluded divisors. Thus
\(z\ne\sigma z\). Make these finitely many points rational over a finite
extension \(C'/C\). On an affine open containing them, choose a regular
function \(h\) with
\[
       h(z)=0,\qquad h(\sigma z)\ne0,\qquad dh(z)\ne0.    \tag{Q3}
\]
These are compatible conditions: the distinct maximal ideals are
comaximal, and \(\mathfrak m_z/\mathfrak m_z^2\ne0\) because
\(\dim Z>0\). The Chinese remainder theorem prescribes the value modulo
\(\mathfrak m_{\sigma z}\) and a nonzero first-order term modulo
\(\mathfrak m_z^2\). All chosen data are defined over a finite constant
extension.

The divisor \(h=0\) is smooth at \(z\), so has a unique prime component
\(D\) through \(z\), of multiplicity one. It is not
\(\sigma\)-stable: if it were, \(\sigma z\) would belong to
\(D\subset\{h=0\}\), contrary to (Q3). It is not one of the excluded
divisors because \(z\) is outside those divisors. Its valuation satisfies
\(v_D(h)=1\). For the next step remove the full finite
\(\sigma\)-orbits of \(D\) and of every previously selected divisor
before choosing \(z\). This gives the desired pairwise distinct pairs.
There are only finitely many choices, so their fields of definition lie
in one finite normal number-field extension. Replace \(M\) by its
compositum with this extension; regularity makes it a field and lets
\(\sigma\) extend by the identity on the constants. The selected prime
components and multiplicities can be followed at the chosen rational
smooth points. In particular they remain discrete divisorial valuations
with a uniformizer.

Finally, if \(C''/C'\) is finite, then
\(\mathcal O_v\otimes_{C'}C''\) is finite étale over the DVR
\(\mathcal O_v\). Its localizations at primes over the maximal ideal are
unramified DVRs; their ramification index is one. This identifies the
prolongations of \(v\) to the finite constant compositum. Taking a
compatible prolongation through all finite constants preserves the value
group \(\mathbf Z\). This proves (4), which is the feature unavailable
for the arithmetic Gauss valuations used previously. \(\square\)

For simultaneous approximation at the selected divisors, take the normal
affine coordinate ring of a common model and localize away from the union
of their finitely many height-one primes. This is a semilocal Dedekind
ring: its nonzero localizations are precisely the selected DVRs. Its
maximal ideals are pairwise comaximal. CRT is applied in this semilocal
ring, not to possibly non-comaximal height-one ideals in a
higher-dimensional affine coordinate ring.

## 4. Integral residues on a punctured rational line

Let
\[
 U=\operatorname{Spec}L[T,1/(P_1\cdots P_r)]
\]
with distinct monic irreducible \(P_j\), and suppose a compatible Kummer
class has an actual multiplicative value at every point over every finite
extension of \(L\). Choose \(x_0\in U(L)\) with actual value \(b_0\).
Since this coordinate ring is a localized PID, the class has the form
\[
 \kappa(b_0)+\sum_{j=1}^r\lambda_j
       \bigl([P_j(T)]-[P_j(x_0)]\bigr),
             \qquad\lambda_j\in\widehat{\mathbf Z}.       \tag{Q4}
\]
We prove \(\lambda_j\in\mathbf Z\).

Choose a descent field \(F\) as in (Q2) containing all coefficients and
normalizing data. The Hilbertian field \(L\) is not separably closed;
choose a nontrivial finite separable extension \(E/L\). Descend its
defining equation and, for a transcendence basis \(t_1,\ldots,t_d\) of
\(F/\mathbf Q\), take a finite Galois extension
\(M/\mathbf Q(t_1,\ldots,t_d)\) containing \(F\), all roots of the
\(P_j\), and the descended coefficients and roots defining \(E\).
Then \(M\overline{\mathbf Q}/L\) is finite Galois and nontrivial.
Choose a nonidentity
\(\sigma\in\operatorname{Gal}(M\overline{\mathbf Q}/L)\).
It fixes \(\overline{\mathbf Q}\), preserves \(M\) by normality, and
restricts nontrivially to \(M\). Thus it satisfies the preceding lemma
over \(C=M\cap\overline{\mathbf Q}\).

Use that lemma with all nonzero polynomial coefficients, differences of distinct
roots, derivatives at roots, and the nonzero normalizing factors among
the required good elements. After replacing \(M\) by the permitted
constant compositum it remains finite Galois over
\(\mathbf Q(t_1,\ldots,t_d)\), by choosing the added constant extension
normal over \(\mathbf Q\). The automorphism still fixes all the
\(P_j\)-coefficients, though it may permute their roots.

At \(v_i\) select a root \(r_i\) of \(P_i\) and a uniformizer
\(\pi_i\). At \(\sigma^{-1}v_i\) select a residue class \(c_i\)
avoiding all the reduced roots of the \(P_j\). The residue fields are
infinite. CRT in the stated semilocal Dedekind ring gives \(\alpha\in M\)
such that
\[
 \alpha\equiv r_i+\pi_i\pmod{\mathfrak p_{v_i}^2},
 \qquad
 \alpha\equiv c_i\pmod{\mathfrak p_{\sigma^{-1}v_i}}.
\]
Taylor expansion, unit derivatives and the good root differences give
\[
 v_i(P_j(\alpha))=\delta_{ij},\qquad
 v_i(P_j(\sigma\alpha))=0.                                \tag{Q5}
\]
The second identity uses that \(\sigma\) fixes the coefficients, not
that it fixes the chosen roots. These conditions also ensure
\(\alpha\in U(M\overline{\mathbf Q})\).

Write \(b_\alpha\in(M\overline{\mathbf Q})^\times\) for the actual
value. Put \(R_j=P_j(\sigma\alpha)/P_j(\alpha)\), and choose an integer
\(a_{j,n}\) representing \(\lambda_j\bmod n\). The evaluation of (Q4)
and its image under \(\sigma\) imply
\[
  \frac{\sigma b_\alpha}{b_\alpha}
        \prod_jR_j^{-a_{j,n}}
               \in\bigl((M\overline{\mathbf Q})^\times\bigr)^n.
                                                               \tag{Q6}
\]
Choose any prolongation \(\widetilde v_i\) of \(v_i\) to
\(M\overline{\mathbf Q}\). The lemma makes it integer valued, with no
ramification scaling. Apply it to (Q6) and use (Q5):
\[
 \lambda_i=-\widetilde v_i(\sigma b_\alpha/b_\alpha)
                    \in\mathbf Z
             \quad\text{inside }\widehat{\mathbf Z}.       \tag{Q7}
\]
Thus the class is represented by the actual unit
\[
 h(T)=b_0\prod_j\left(P_j(T)/P_j(x_0)\right)^{\lambda_j}.
\]
At every finite-extension point its actual value differs from \(h\) by
an element of \(\overline{\mathbf Q}^{\times}\), by (Q1).

This argument does not require the actual value to lie in one fixed
finite radical field and does not interchange radical levels. All levels
use the single valuation \(\widetilde v_i\) of the same field
\(M\overline{\mathbf Q}\). The unramified constant extension is the
precise justification for this simplification.

## 5. Removing the Picard–Tate contribution

Let \(X/L\) be smooth, geometrically connected, affine and pointed by
\(x_0\in X(L)\). Let \(\xi\) be a compatible Kummer class with actual
multiplicative values at every finite-extension point. After a finite
extension splitting the boundary components of a smooth projective
compactification, descend all geometric data and the generalized Albanese
\(A\) to a finitely generated \(F/\mathbf Q\) satisfying (Q2).

Spiess–Szamuely, Propositions 4.1 and4.3 and Corollary4.2, supplies the
integral identification
\[
 H^1(X_{\bar L},\mathbf Z_\ell(1))
       =\operatorname{Hom}(T_\ell A,\mathbf Z_\ell(1)).     \tag{Q8}
\]
The finite kernel of geometric abelian fundamental groups disappears
under Hom into the torsion-free target; this is an integral statement,
not a rational comparison with an unproved saturation assumption.

Put \(H=G_L\triangleleft G_F\) and \(W=(V_\ell A)_H\). Normalize the
class by its actual value \(b_0\) at \(x_0\). Since all roots of unity
lie in \(L\), its normalized geometric functional extends to a
homomorphism on the split arithmetic fundamental group, zero on the
section at \(x_0\). The projected Kummer homomorphisms of closed points
span \(W\): otherwise an annihilating nonzero integral functional,
reduced at a level where it is nonzero, would give a nontrivial finite
arithmetic quotient trivial on every point decomposition group. This
contradicts Section2.

Choose finitely many such point images spanning \(W\). Their coordinates,
actual values \(\beta_i\), and \(b_0\) lie in a finitely generated
\(M/\mathbf Q\), finite over a suitable enlarged descent field. On
\(G_{M\overline{\mathbf Q}}\), finite index in every chosen point group,
their rational spans are unchanged. For \(g\in G_M\) and
\(h\in G_{M\overline{\mathbf Q}}\), their Kummer cocycles satisfy
\[
 c_i(ghg^{-1})=g c_i(h),\qquad
 \kappa(\beta_i/b_0)(ghg^{-1})
      =\chi(g)\kappa(\beta_i/b_0)(h)                         \tag{Q9}
\]
in \(H\)-coinvariants. The usual coboundary correction in the first
identity vanishes in those coinvariants. Normality of \(H\) makes this
quotient stable under \(G_M\). Equality with the actual evaluations
therefore makes the geometric functional \(G_M\)-equivariant on a
spanning collection, hence on all of \(W\) and on \(T_\ell A\).

Apply Jannsen's integral Tate-Hom theorem for1-motives over the finitely
generated field \(M\), **original Theorem4.3(ii), printed p.676**, to
\([0\to A]\) and \([0\to\mathbf G_m]\). It identifies the functional
with an element of
\(\operatorname{Hom}_M(A,\mathbf G_m)\otimes\mathbf Z_\ell\).
The Albanese universal property identifies this group with the normalized
unit lattice tensored with \(\mathbf Z_\ell\). After the boundary
components are split, this one geometric unit lattice is already fixed
over the descent field: its divisor and value1 at \(x_0\) determine a
unit uniquely. Thus all coefficient primes use one integral unit basis,
and the original class is in its \(\widehat{\mathbf Z}\)-span plus the
actual constant value at \(x_0\). The Picard–Tate contribution of this
particular point-theoretic class vanishes. The entire Picard–Tate module
need not vanish.

For a curve, use the Riemann–Roch map of F.27 to a punctured rational
line, isolating a chosen rational boundary point in its zero fibre.
The norm of the class has actual point values. Section4 makes its
residue an ordinary integer. The norm weights residues by residue degree,
and the chosen boundary point has degree one. Repeating at each boundary
point makes every boundary residue integral. The injective divisor
matrix of a unit basis then makes the exponents ordinary integers.

For higher dimension choose a smooth transverse curve at a smooth point
of each boundary divisor away from all intersections. At finite Kummer
level, after étale localization the class is represented by \(u z^a\);
transversality takes \(z\) to a uniformizer and retains the same residue.
The curve calculation therefore makes every global residue integral,
and the same divisor matrix gives a regular unit \(h\). Normalize it by
\(h(x_0)=b_0\). The finite extensions used above introduce no descent
gap: a Galois conjugate divided by \(h\) has zero divisor and value1 at
\(x_0\), hence is1. At each finite Kummer level the residual class is
geometrically zero, hence constant by low-degree Hochschild–Serre;
evaluation at \(x_0\) kills it. Consequently
\[
                              \xi=\kappa(h).               \tag{Q10}
\]

Constant abelian varieties do not invalidate the spanning argument.
Section2 detects quotients by points over **finite extensions of the
function field**, whose morphisms to the constant abelian variety need
not be constant. Merely looking at its algebraic-constant points would
lose exactly the required span.

## 6. Recovering the actual point function

For a pinned relative map from a smooth affine curve to \(\mathbf G_m\),
Section5 and (Q1) give
\[
                 \phi(x)=c_xh(x),
          \qquad c_x\in\overline{\mathbf Q}^{\times}.      \tag{Q11}
\]
All statements hold after every finite extension of \(L\).

Suppose first that \(h\) is nonconstant. The unbounded-degree points
show that the point function cannot be constant: otherwise every
\(h(x)\) would belong to the base field, whereas a fibre of the finite
map defined by \(h\) has degree bounded by \(\deg h\). More explicitly,
if \(h(x)\in L\), then \([k(x):L]\le\deg h\); every closed point
of larger degree has \(h(x)\notin L\), hence
\(h(x)\notin\overline{\mathbf Q}\). Since the point function is
nonconstant, its inverse image of the complement of any prescribed
target value is a nonempty open. Each such open retains closed points
of arbitrarily large degrees by Section2. Pull back
\(T-1\) to that nonempty inverse-image open, and apply Section5 to get
an actual unit \(h_1\) there. At a closed point of degree exceeding the
combined pole degrees, the function
\(c_xh-d_xh_1-1\), with \(c_x,d_x\in\overline{\mathbf Q}^\times\),
vanishes; hence it vanishes identically. Therefore
\(h_1=Ah+B\) with nonzero algebraic constants \(A,B\). Where
\(h(x)\notin\overline{\mathbf Q}\), comparison of coefficients gives
\(c_x=-A/B=:c\). Such points automatically belong to the open, since
\(\phi(x)=1\) would make \(h(x)=1/c_x\) algebraic.

For every \(b\in\overline{\mathbf Q}^\times\), repeat on the
inverse-image open of \(T-b\ne0\). A sufficiently high-degree point,
where the preceding scalar has already been identified, gives
\(h_b=e_b(ch-b)\). If \(h(x)\) is algebraic, take
\(b=ch(x)\). Were \(\phi(x)\ne b\), the point would belong to that
open while its regular unit \(h_b\) vanished. Hence \(\phi=ch\) at
these points too. Normalizing at \(x_0\) fixes the scalar.

If \(h\) is constant, choose \(\beta\in L\) with
\(\beta/h\notin\overline{\mathbf Q}\), possible because the
transcendence degree is positive. Equation(Q11) shows that no closed
point maps to \(\beta\). Its inverse image is closed; every nonempty
closed subset of a noetherian curve has a closed point. Thus the map
factors through the complement of \(\beta\), and \(T-\beta\) gives
an actual unit \(h_\beta\) on the whole curve. Its values belong to
\(L\) by(Q11); unbounded-degree points force \(h_\beta\) to be
constant. Normalizing at \(x_0\) gives
\[
             (\phi(x)-\beta)/(h-\beta)
                         \in\overline{\mathbf Q}.
\]
Together with \(\phi(x)/h\in\overline{\mathbf Q}\) and
\(\beta/h\notin\overline{\mathbf Q}\), this forces \(\phi(x)=h\).
Here the separating \(\beta\) lies in \(L\) itself; no missing
number field is needed.

For a smooth affine variety, make an arbitrary geometric closed point
rational by a finite extension, and choose a smooth geometrically
connected curve through it and \(x_0\). The curve's point-function unit
and the restriction of \(h\) have the same Kummer class. Their quotient
has zero divisor on a proper completion and value1 at \(x_0\), so they
are equal. This proves the required point function on the whole variety.

We have now verified exactly CHW Theorem4.18(5): every pinned relative
map from a connected regular affine finite-type scheme with a rational
point to \(\mathbf G_m\) has an algebraic geometric-point function.
Characteristic zero makes the source smooth, and connectedness together
with the rational point makes it geometrically connected. Dimension zero
is the field-source statement. CHW's theorem then gives the all-scheme
Hom assertion, including the full étale-chart comparison and descent.
There is no extra amenability hypothesis in that theorem.

## 7. Precise subfield descent

Let \(k_0\subset L\) have positive transcendence degree over
\(\mathbf Q\), and put \(K=k_0\overline{\mathbf Q}\subset L\).
Then \(K/\overline{\mathbf Q}\) is finitely generated. Indeed choose a
finite transcendence basis \(B\) of this intermediate extension. The
relative algebraic closure of \(\overline{\mathbf Q}(B)\) in the
finitely generated extension \(L/\overline{\mathbf Q}(B)\) is finite
(Stacks, Lemma9.26.11, tag030D). Since \(K\) is algebraic over that
rational field, it is contained in this finite closure and is finite too.
Its transcendence degree is positive because adjoining algebraic
constants cannot remove a transcendental element over \(\mathbf Q\).

The core theorem applies to \(K\). The extension \(K/k_0\) is algebraic,
since it is obtained by adjoining elements algebraic over \(\mathbf Q\).
The algebraic-extension descent theorem F.32 therefore gives
reconstruction over \(k_0\). This explicitly excludes the zero-dimensional
constant case and makes no claim that reconstruction descends along an
arbitrary transcendental extension.

## 8. Strictness relative to F.44

The example \(\overline{\mathbf Q}(t)\) is outside F.44's sufficient
class. If it belonged to that class, F.44's equivalent description would
give a finitely generated subfield \(F_0\) over which it is algebraic,
and a normal closure \(N/F_0\) with a virtually pro-\(\mathcal C\)
Galois group for some proper hereditary extension-closed
\(\mathcal C\) containing cyclic groups. Put
\(C=F_0\cap\overline{\mathbf Q}\), a number field. Since \(F_0/C\)
is regular and \(N\) contains \(\overline{\mathbf Q}\), restriction
gives a quotient
\[
              \operatorname{Gal}(N/F_0)\twoheadrightarrow G_C.
\]
Thus \(G_C\) would have an open pro-\(\mathcal C\) subgroup. Every
open subgroup of \(G_C\) is the absolute Galois group of a number field
and has \(S_n\)-quotients for arbitrarily large \(n\), by the regular
Morse polynomial and Hilbert specialization used in F.44. But a proper
hereditary \(\mathcal C\) excludes all sufficiently large \(A_n\),
and hence those \(S_n\). This is a contradiction.

The new class would therefore add a genuinely different sufficient
mechanism. It would also show that reconstruction is not preserved under
arbitrary subfields: the positive field \(\overline{\mathbf Q}(t)\)
contains the negative field \(\overline{\mathbf Q}\). The intrinsic
classification in F.9 would remain unresolved.

## 9. Source access and the exact replacement audit

New primary source opened directly by the topos agent on
14 November2026:

- Bary-Soroker, L., & Paran, E. (2013). Fully Hilbertian fields.
  *Israel Journal of Mathematics, 194*(2), 507–538.
  https://doi.org/10.1007/s11856-012-0153-6.
  Opened https://arxiv.org/pdf/0907.0343, Theorem1.2, printed p.2;
  Theorem3.1, printed p.15; Corollary3.2, printed p.16. The PDF header
  identifies arXiv:0907.0343v1 while its internal date is16 September2021;
  this version distinction is retained rather than silently identifying
  the author text with the journal pagination. Retrievals turn804view0,
  turn805view0–1.

Previously opened sources used within their original hypotheses:

- Serre, *Topics in Galois Theory*, Proposition3.3.1 (full-degree Hilbert
  specialization); F.44's recorded regular symmetric-group families.
- Poonen–Slavov, Theorem1.5, for the cover-preserving Bertini step already
  proved in F.29; elementary finite-jet smooth curves as in F.7/F.30.
- Spiess–Szamuely, Propositions4.1 and4.3, Corollary4.2, integral Albanese
  comparison; generalized Albanese universal property in Section3.
- Jannsen, original Theorem4.3(ii), printed p.676, integral Tate-Hom for
  1-motives over finitely generated fields. It is applied over \(M\),
  never directly over \(\overline{\mathbf Q}\) or \(L\).
- CHW, Theorem4.18(5), the exact all-scheme reconstruction reduction;
  F.32's already audited coherent étale-base-change descent.
- Stacks, tag030D, finiteness of relative algebraic closure in a finitely
  generated field extension.

| Earlier predicate | Replacement here | Explicit restriction |
|---|---|---|
| Radical-closed scalar field and divisible kernel | Algebraically closed constants and(Q1) | Normal proper model; all finite extensions covered |
| Prosolvable/pro-formation residual Hilbert group | Hilbertianity of \(L\) itself | Positive transcendence degree is used |
| Missing number field moving Gauss places | Missing finite geometric extension and moved prime divisors | The automorphism fixes all algebraic constants |
| Fixed radical field and norm scaling | Integer-valued prolongation through unramified constant extensions | No arithmetic valuation is used |
| Normal subgroup for Albanese equivariance | \(G_L\triangleleft G_F\) from \(L=F\overline{\mathbf Q}\) | All Tate-Hom applications stay over finitely generated \(M\) |
| Scalar ambiguity in point functions | \(\overline{\mathbf Q}^\times\) | In the constant case choose \(\beta/h\) transcendental inside \(L\) |
| Descent to arbitrary subfields | \(k_0\overline{\mathbf Q}/k_0\) algebraic, with positive-dimensional compositum | Algebraic subfields are excluded |

### Targeted comparison completed on14 November2026

Both available search engines were queried with combinations of
“étale topos/topoi”, “reconstruction”, “algebraic closure/Qbar”, and
“function fields”. The comparison relied on the following directly
opened primary statements, not on search snippets or discussion boards.

1. Carlson–Haine–Wolf, author PDF
   https://math.berkeley.edu/~phaine/files/reconstruction_of_schemes_from_etale_topoi.pdf,
   Introduction Theorems0.1 and0.3, pp.1–2 (retrieval turn807view0),
   independently compared with the supplied arXiv source. The first
   concerns fields finitely generated over their prime field. The second
   assumes no nonidentity infinitely divisible torus points, which fails
   for the fields here because they contain
   \(\overline{\mathbf Q}^\times\). Its reduction Theorem4.18 is used,
   while its amenability theorem does not by itself give this candidate.
2. Carlson–Stix, arXiv:2410.22474v2, revised20 September2026, PDF internal
   date22 September2026, https://arxiv.org/pdf/2410.22474,
   Introduction TheoremsA–B and PropositionC, pp.1–2
   (retrieval turn807view1). The current field theorem remains for
   sub-\(p\)-adic fields; the new relative theorem keeps sub-\(p\)-adic
   function fields. PropositionC assumes Kummer-faithfulness. Neither
   statement covers \(\overline{\mathbf Q}(t)\): a finitely generated
   extension of \(\mathbf Q_p\) has only a finite relative algebraic
   extension of \(\mathbf Q_p\), which cannot contain all roots of
   unity; and the constants here are infinitely divisible.
3. Bary-Soroker–Paran is used only for its exact Hilbertian field theorem,
   not as an étale-topos reconstruction theorem. Its author/journal
   version distinction is recorded above.

No opened source in this targeted comparison stated the proposed
positive-transcendence-degree algebraic-constant theorem. This is a
limited comparison, not an exhaustive priority or novelty claim.
No finite numerical assertion is used in this proof.
