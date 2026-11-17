# Independent audit of the honest binary affine lifting argument

The analytic argument is valid on the actual saturated integral affine
lattice. Its integral nature needs the precise quadratic calculation
below; a rank computation at a finite level alone would not establish
the analytic statement.

## 1. The exact source and affine lattice

The integral system in `check_integral_affine_system.py` uses the actual
100 free target coordinates, together with the two order-six coordinates
per expression. The binary conditions on the latter remain explicit.
The common coordinates are the integral J/K' lattice from A.4.60.
They are converted to modular K-Schreier coordinates by the exact
index-three matrix W, which is invertible over Z_2.

I read the complete integral lattice construction. It takes the row
Hermite transform of the transpose of the 598-by-291 free-equation
matrix. The last 96 rows of its unimodular transform are an actual
integral basis of the kernel. The particular solution is checked
against every original integer equation; its binary matching is
verified in the original coordinates. Consequently this is the
saturated rank-96 lattice of integral solutions, rather than the
larger rank-97 space of formal binary increments.

Write the corrected integral seed as z_0 and the kernel basis as
k_0,...,k_95. The family is

    z(u) = z_0 + 2 sum_i u_i k_i.

Its free equations hold identically. Its binary torsion conditions
remain those of z_0. The full coefficient-four cusp zero of the
corrected seed is verified by an actual integral Hermite witness.

## 2. The cusp word has zero integral power coordinates

Use the ordered modular Schreier-word section. Let beta=k(b)t and
A=k(a), where t is the fixed base-state-252 representative and k(v)
denotes the ordered word with exponent row v. The involution fixes
the base state, so c=t sigma(t)^(-1) belongs to K and is fixed as u
varies. The exact cusp word is

    d = beta sigma(beta^(-1) A rho(A^(-1)))
      = k(b) c sigma(k(b))^(-1) sigma(k(a)) sigma rho(k(a))^(-1).

Both positive frame relations and the two-cycle relation hold in the
actual quotient B_0/K'. They make d the identity in that quotient.
Thus d belongs to K', with exactly zero exponent vector in K^ab.
Its canonical obstruction has no remaining integral power coordinate.
It is the class of this word in the actual wedge coinvariant module W.

The binary finite record is constant in the family. Replacing lifts of
finite frames by central factors changes neither their cusp word nor
its canonical class, since each such factor occurs with its inverse.
The binary defect is therefore zero throughout the family. The actual
inclusion W/2W -> M_2 established by the uniform canonical calculation
implies d(u) lies in 2W. Since W = Z_2^8 plus C2^7, the restriction
2W -> W_free is injective and has image 2 W_free. In particular,
vanishing of the free class will imply vanishing of the entire class.

## 3. Exact quadratic term after the specified rational map

To compute the degree, send k_i to exp(X_i) in the class-two rational
Lie group and send [k_i,k_j] to [X_i,X_j], followed by the actual
wedge-coinvariant projection to W_free tensor Q_2. For a word in K'
the logarithm is exactly its central commutator class, so this map
computes precisely the required torsion-free obstruction.

The logarithm of the ordered section k(v) has a quadratic central
term. In d, the two section terms in b cancel after coinvariance,
as do the two section terms in a. The central correction in the
action on each X_i is linear in the exponent row. The fixed word c
contributes only constant and linear terms. Thus the homogeneous
quadratic part comes exactly from the Baker-Campbell-Hausdorff cross
term of the four rows

    b,  -bS,  aS,  -aRS.

Here S,R act on rows, and the homogeneous frame equations are

    f = bS-b = aR-a,          fS=-f.

The four rows sum to zero. Expanding their six exterior products,
with the factor one half from the class-two product, gives

    (1/2) <aS-b, f>.

Coinvariance under S gives 2<b,bS>=0 and
<aS,f>=<a,fS>=-<a,f>. The former class is zero in the torsion-free
quotient. The displayed quadratic term is therefore exactly

    -(1/2) <a,aR>.

In the actual family z_0+2uK, the homogeneous cubic coordinate is
2a(u), where a(u)=sum_i u_i a_i. Consequently the quadratic term
of the free cusp defect is

    -2 <a(u), a(u)R>.

This is the exact factor of two needed in the analytic argument.
It accounts for the potentially nonintegral binomial coordinates;
they have not been silently treated as integral polynomial terms.

## 4. Integrality and the full derivative

Let d_free(u) denote the free class and F(u)=d_free(u)/2. The preceding
calculation gives a polynomial of degree at most two over Q_2.
Its quadratic coefficients are integral. Its values at every integer
u are integral because d(u) lies in 2W. Hence its constant coefficient
is integral, and each linear coefficient is F(e_i)-F(0) minus the
already integral diagonal quadratic coefficient. Thus every
coefficient is in Z_2. Continuity of the ordered class-two coordinates
extends these integer identities to the actual completed source.

The full wedge quotient modulo four supplies the exact comparison

    W_free/2 W_free -> 2W/4W -> M_4.

The first arrow is an isomorphism and the second is injective. Tower's
program constructs that map from the actual integral canonical HNF.
Its 15 wedge coordinates have precisely the seven recorded even-row
directions as the kernel of doubling. Quotienting them therefore
gives the actual eight-dimensional free quotient, not a chosen
unrelated eight-dimensional vector space.

The program checks all 96 diagonal classes <a_i,a_i R> and all 4560
cross classes <a_i,a_j R>+<a_j,a_i R> in this free quotient modulo
two. Every class is zero. Thus every quadratic coefficient of F is
even, and its derivative modulo two is constant. The finite-difference
matrix minus the diagonal quadratic terms is exactly that derivative.
It has rank eight, with independent directions 0,1,2,3,4,5,9,11.

I independently reran the complete checker. Its saved output is
`work/ghost_mod4_review/review_integral_frame_jacobian.out`; all
quadratic checks and the rank-eight comparison passed. Centralizer
also recomputed all 96 differences directly at the newly corrected
honest seed, so the main proof can use that direct data rather than
rely on transporting a point from the larger formal finite family.

## 5. Explicit lifting and its scope

The corrected seed has F(0)=0 modulo two. Set the other 88 coordinates
to zero and use the specified invertible eight-by-eight derivative
minor. Starting with u_1=0, choose the eight binary coordinates delta_j
by

    D F(u_j) delta_j = -F(u_j)/2^j  (mod 2),
    u_(j+1) = u_j + 2^j delta_j.

The exact integral polynomial Taylor formula makes F(u_(j+1)) zero
modulo 2^(j+1): the quadratic error is divisible by 2^(2j), which is
sufficient for every j>=1. The sequence is Cauchy. Its limit lies
in (2 Z_2)^96, is supported on the eight specified indices, and has
F(u)=0. The affine record remains congruent to the corrected seed
modulo four. Its whole cusp class is zero because that class belongs
to 2W and its free image is zero.

This proves the simultaneous zero of the actual canonical obstructions
at every binary coefficient, with all affine source equations retained.
The subsequent proof must still use the actual finite automorphisms,
the natural primary maps for odd coefficient joins, and the complete
finite-certificate image theorem before claiming a normalized gentle
element. Centralizer is supplying those exact steps in A.4.61.

## 6. Final A.4.61 assembly audit

The complete self-contained proof in
`work/centralizer_all_coefficient_survivor.tex` passes the independent
semantic audit. The updated source-factorization paragraph is exact:
an ordinary lift of finite f lies in J contained in K, and the free
map x->x, y->f^(-1)yf is identity on F_0/K. It preserves K, K', K^m
and the abelian coefficient kernel F_0'F_0^(6m), hence preserves the
actual J_m intersection. The positive torsion frames extend that pure
map to B_0/J_m. At binary levels the kernel matrix reduces to the
verified mask-31 automorphism, giving an odd determinant and an actual
finite automorphism. This supplies the needed source morphism at
every level, rather than asserting preservation from dimensions.

For odd n divisible by three, the kernel E_n->E_3 is abelian of odd
order. With e=sigma(b)b^(-1), sigma(e)=-e. Replacing b by (e/2)b
therefore kills the defect with the stated sign. It preserves the
pure subgroup and the fixed ternary harmonic frame. The pair and
cubic frame are both identity on this odd factor, giving the
identity source action. Both coefficient actions and their frames
have the same base record and join under the actual CRT square.

The two canonical comparisons are the maps induced by the identity
of B_0. Their finite kernel orders are 3*n^97 and 2^(97a). Localized
integral homology therefore identifies the entire binary primary
kernel with the computed M_(2^a), and every odd primary kernel with
its counterpart on E_n. The binary defect is zero by the honest
analytic construction. The odd-factor cusp defect is the harmonic
commutator and is killed by two, so every odd primary component is
zero. Thus the defect is zero in the whole canonical central kernel.

The conjugated torsion generators define an endomorphism of the
full finite canonical cover. They factor because the relation kernel
maps into its center. The quotient automorphism and the stem
property give surjectivity of the entire cover. The existing full
finite-certificate image theorem consequently supplies a genuine
positive profinite automorphism preserving the pair and both frames.
The exact abelianization C_(6m)^2 and exact generator orders6m make
the normalization parameter a multiple of6m. Hence normalization
preserves the complete finite record literally.

Every finite family of target conditions is met by the construction
at a multiple of six times their common multiple. The actual
parameter and parity evaluations are continuous. The pure torsion
frames are unique because their centralizers intersect the pure
subgroup trivially, so their closed defining graph also makes the
finite frame conditions continuous. Compactness therefore supplies
one genuine normalized element with all coefficient pentagons zero
and the fixed parity-one frames. A.4.60 identifies the exact completed
target with the inverse limit. The character's proved vanishing on
full GT supplies the stated exclusion from that subgroup by its
actual restriction map. No mathematical defect was found.
