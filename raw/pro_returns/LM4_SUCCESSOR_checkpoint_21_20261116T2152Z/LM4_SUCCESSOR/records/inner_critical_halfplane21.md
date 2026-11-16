# Proposed exact fixed-source theorem over the inner critical region

Twenty-first-hour proof under independent review. This concerns the
actual region, including its mixed critical fibers, and does not yet
transfer to the whole surface. We use the free quotient Q and its
based involution from free_swap_quotient21.md.

## 1. The separated half-planes

Let B={q:0<|q|<1}. Put z=1/t and Z=(1+z)/(1-z)=(t+1)/(t-1).
The retained punctures t=1,-1 become Z=infinity,0, so the fiber
coordinate belongs to C*. The involution is Z to 1/Z, with fixed
points Z=-1 (selected t=0) and Z=1 (other t=infinity).

For u in mu5 minus {1}, set alpha_u=u(2-u), beta_u=u^2/(2u-1).
Since beta_u=1/conjugate(alpha_u) and |alpha_u|>1, the inverse
Blaschke factor T_u has |T_u(q)|>1 on B, including its projective
poles. More explicitly, for h_u=1/T_u and d_u=u^2+(1-2u)q,

 |q-alpha_u|^2-|d_u|^2=(|alpha_u|^2-1)(1-|q|^2)>0.

Thus z=+-h_u(q) lies in the unit disk, and its Z coordinate lies
in the right half-plane. The retained branch punctures satisfy
z^2=q, so they also lie there. All actual removed points apart from
the retained0,infinity therefore lie in Re Z>0. There is no deleted
point in Re Z<0 or on the imaginary axis with0 removed. The map
Z to1/Z preserves each half-plane and exchanges the two imaginary
rays. No critical base value inside B has been removed.

## 2. An actual orbifold graph of spaces

We use the homotopy quotient by this literal C2 action; its fundamental
group at the fixed base point is pi1(Q_B) semidirect C2. The left
half-plane part of Q_B is exactly B times the left half-plane.
Its equivariant contraction to Z=-1 gives orbifold group
A=pi1(B) times C2. The right part retains every actual divisor and
critical fiber; let R denote its orbifold fundamental group with a
small collar of the imaginary boundary included.

Here is an open-cover justification. The two-component hypersurface
B times iR* is closed in the actual Q_B, since0 and infinity are
removed. It has a tubular collar avoiding the closed deleted
divisors. A C2-invariant metric and a positive invariant collar-width
function give an invariant collar; a constant width is not assumed
on this noncompact space. The half-plane parts enlarged slightly
across that collar form an invariant open cover. Each has the same
equivariant homotopy type as its half-plane with the boundary collar,
and the intersection contracts equivariantly to B times iR*.
In the homotopy quotient, the two boundary components are exchanged
freely and the intersection has the homotopy type of B.

Projection to q gives R to pi1(B), and the boundary section Z=i
in the quotient supplies an actual splitting. A fixed lift in EC2
defines the section in the homotopy quotient; its projection to B
is the identity. Consequently the edge inclusion pi1(B) to R is
injective and admits a retraction. Its inclusion into A is the
ordinary pi1(B) factor. Orbifold van Kampen therefore gives the
actual based group isomorphism

 E_B=(pi1(B) times C2) amalgam_(pi1(B)) R.

The chosen C2 is the involution at Z=-1. Whiskering to the boundary
at the fixed base q identifies the pi1(B) factor with the selected
fixed source Z=-1. No assertion about the unknown right-region
group is required beyond its displayed retraction.

## 3. A retracted-amalgam centralizer lemma

Let C be any discrete group, let j:C to R be an injective homomorphism
with retraction r:R to C, and form

 E=(C times <tau>) amalgam_C R, tau^2=1.

Then the discrete centralizer of tau is C times <tau>. For example,
the usual reduced-word normal form proves this: a reduced word
leaving the first vertex group cannot conjugate tau back into that
group, because tau does not belong to any edge subgroup conjugate
inside the first vertex group. The same argument is the unique
fixed-vertex argument in the ordinary amalgam tree.

The full profinite centralizer is the image of Chat times <tau>.
We give a finite-quotient proof instead of assuming an unverified
profinite tree realization. Identify r with its idempotent endomorphism
jr of R. For every finite-index normal N0 in R, put
N=N0 intersect r^-1(N0). It is finite-index normal, contained in N0,
and r(N) is contained in N. These r-stable N form a cofinal family,
closed under finite intersections. In the finite group Q_N=R/N,
the retraction has image D_N and kernel K_N, so Q_N=K_N semidirect D_N.
The corresponding quotient of the amalgam is

 E_N=(D_N times C2) amalgam_(D_N) Q_N
    =(C2 free-product K_N) semidirect D_N,

where D_N acts on K_N through the retraction splitting and fixes tau.
The free-product subgroup has finite index, hence its full completion
embeds as the corresponding open subgroup of E_Nhat. Its completion
is the full free profinite product C2 amalg K_N. The already verified
Herfort--Ribes1985 Theorem B' gives the centralizer of tau there as C2.
Consequently C_(E_Nhat)(tau)=C2 times D_N.

Every homomorphism from E to a finite group factors through some E_N:
choose N0 as the kernel of its restriction to R, and then refine to
the displayed r-stable N. The identifications of C in the two factors
ensure that the map from C times C2 factors through D_N times C2.
Therefore the maps Ehat to E_Nhat jointly separate elements of Ehat.
For a tau-centralizing element, its images are uniquely tau^epsilon
d_N. The epsilon are compatible, and the compatible d_N give an
element of Chat. To see the latter cofinality explicitly, for any
finite-index normal L of C take N=r^-1(L); then D_N=C/L. Thus the
finite D_N quotients induce the full profinite topology of C.
Subtracting the resulting tau^epsilon c makes every E_Nhat image
trivial, hence makes the original element trivial. The converse
centralizing inclusion is immediate.

This proof needs neither residual finiteness of R nor a claim that
an arbitrary infinite-index subgroup of R has its full topology.
The embeddings of Chat and Rhat into Ehat also follow from the
two explicit retractions, but the centralizer proof is already
given by the cofinal finite quotients above.

## 4. Exact local conclusion and the global boundary

Apply the lemma with C=pi1(B)=Z. Since E_B=pi1(Q_B) semidirect C2,
we obtain

 pi1(Q_B)^F=pi1(B),
 pi1(Q_B)^hat fixed by F = image of pi1(B)^hat,

with the right side the actual selected source at t=0. The notation
in the second line means the F-fixed subgroup of the full completion
of pi1(Q_B), not the completion of a previously computed fixed group.
The source is injective and has its full topology, by the q retraction.
The finite-index extension by C2 commutes with completion because its
kernel has finite index and therefore carries its full profinite topology.

Pulling back through the actual index-two free-swap cover gives the
same selected fixed-source equality for the based original region
Z_B. Over B, sqrt(1-q) is single-valued, so the inverse image of the
selected source has two components. We use the component containing
P. Its map to B is an isomorphism. Unlike the whole-base comparison,
the source monodromy of this restricted double cover is trivial;
we use only intersection with the open index-two subgroup, not the
surjective-source-monodromy converse from free_swap_quotient21.md.

The reciprocal-conjugate symmetry (q,t) to
(1/conjugate(q),1/conjugate(t)) gives the analogous outer-region
statement for the other fixed source t=infinity, with an appropriate
base point there. It does not turn that statement into one about the
selected source t=0 in the outer region.

The global surface includes both regions and the regular fibers near
the unit-circle arcs. Their fiber groups need not inject into regions
after critical fibers are inserted. Thus an amalgam along q-boundary
fibers cannot be asserted from these local splittings. Proving the
global compatible marking or controlling those two kernels remains
the exact main-problem gate.
