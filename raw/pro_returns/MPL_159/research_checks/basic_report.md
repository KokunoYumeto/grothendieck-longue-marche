# Basic algebra checks, after the transcription freeze

Author: GPT-6 Astra Pro, root agent, MPL_159 run, 18 November 2026.
These are mathematical checks of explicitly stated models, not new readings
of the images. The frozen transcription is not edited by these checks.

## B1. The factor r+1 on scan 9

For a locally free module V of rank r let m(a)(v)=av in Sym²(V).
There is a canonical contraction C: V* ⊗ Sym²(V) → V sending
λ⊗vw to λ(v)w+λ(w)v. For a local basis e_i, the element m(a)
is Σ e_i*⊗ae_i, so C(m(a))=a+ra=(r+1)a.
Thus (r+1) invertible supplies a natural left inverse; rank one is
separately an isomorphism without inverting 2. This checks the stated
sufficient conditions, and does not settle the all-characteristic question
about canonical recovery from an infinite projective connection.

## B2. Isotropic splittings and characteristic two

For an alternating perfect pairing and an isotropic half-rank subbundle,
changing a local splitting by u changes its restricted alternating matrix
by u-uᵗ, up to the convention for the off-diagonal pairing. Every alternating
matrix has zero diagonal, so choosing a strict triangular part of u cancels
it, even in characteristic two. The kernel consists of symmetric matrices.
Local isotropic splittings therefore exist over an arbitrary base; their
torsor need not have a global section.

For a finite free V, the invariant tensors (V⊗V)^{S₂}, equivalently Γ²(V),
have basis e_i⊗e_i and e_i⊗e_j+e_j⊗e_i. Their map into the coinvariants
Sym²(V) has coefficient 1 on the first type and 2 on the second.
It is an isomorphism after inverting 2, but in characteristic two the
off-diagonal terms vanish. This explains why scan 13's displayed map from
Γ², rather than from Sym², requires a characteristic qualification; it
does not impose that qualification on the existence of isotropic splittings.
The script exhaustively checks the splitting linear map for ranks 2 and 3
over F₂, and rank 2 over F₃; the preceding argument proves the general case.

## B3. Two separate checks of the scan 20–21 calculation

First, the literal formulas on scan 20 give c_D(1)=1 and, on substituting
λ=ν=0 and μ=1 in the subsequent general formula, c_D(1)=-1.
They cannot both hold in characteristic different from two. This observation
does not choose a correction or a preferred convention.

Second, in the declared coordinate model ∂_x+(1+bt+ct²)∂_t, the change
z=t/(1+at) gives

    ∂_x + [1+(b-2a)z+(a²-ab+c-a')z²]∂_z.

Consequently a change of this form preserves a prescribed zero linear
coefficient only if 2a=0. This independently supports the kind of factor-two
obstruction on scan 21; it is not an assertion that every intermediate
sign or bracket on scan 20 is correct. It also shows why a differential
operator on a one-form must not be silently replaced by the exterior
derivative, which vanishes on two-forms on a curve for a different reason.

## B4. The dimension identity on scan 13

The identity g(g+1)/2-(3g-3)=(g-2)(g-3)/2 is exact. Interpreting it as
the dimension of a kernel still requires surjectivity of the relevant
multiplication map. The nonhyperelliptic and characteristic-not-two
qualifiers are actually present on scan 13; the arithmetic is not a
substitute for those hypotheses. Genus two is a separate hyperelliptic
case where the ordinary Sym² multiplication is still an isomorphism.

## B5. Trivial centralizer does not force a closed conjugacy orbit

For a genus-g surface group with g≥2, send all b_i to the identity,
a₁ to diag(2,1), a₂ to the upper unitriangular matrix with entry 1, and
the remaining a_i to the identity. The product-of-commutators relation
holds. The Zariski closure of the image is the upper-triangular Borel:
powers of diag(2,1) are dense in its torus and powers of the unipotent
matrix are dense in its unipotent radical. Its PGL₂ centralizer is trivial,
since commuting with the diagonal forces a diagonal matrix and commuting
with the unipotent then forces a scalar.

Conjugation by diag(s,1) keeps a₁ fixed and sends a₂'s upper entry to s.
At s=0 the tuple therefore has a diagonal limit, whose image is abelian
and hence cannot be conjugate to the original nonabelian image. The orbit
is not closed in the full affine representation variety despite its trivial
stabilizer. The diagonal limit has positive-dimensional stabilizer and leaves
the trivial-centralizer locus, so the example does not assert nonclosedness
inside that smaller locus. This does not disprove an
algebraic-space or stack quotient; it explains why the written orbit space
must not automatically be identified with a reductive GIT character variety.

## B6. The higher stratification detects the resonant coordinate change

Over F_p[x][[t]], take the full ordinary formal-diagonal translation
stratification Δx=x+ε and Δt=t+ε. Choose q=p^r≥4 and let h fix x
and send t to t+t^q; extend h to fix ε.
Then

    Δ(h(t)) = t+ε+(t+ε)^q = t+t^q+ε+ε^q,
    h(Δt)   = t+t^q+ε.

Their difference is ε^q, which is nonzero in the ordinary completed
principal-parts algebra. The first-order connection does not see it, but
the full stratification does. This checks only this explicit automorphism;
it does not prove global normal-form existence or uniqueness with arbitrary
higher stratification data, or any corresponding assertion for divided-power
stratifications. The script verifies the polynomial identity for four primes
with q≥4, and the displayed Frobenius identity proves it for all p-powers.
