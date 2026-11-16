# Audit of the exact quadratic pullbacks of the two flex pencils

Date:2026-11-16. Inspected and replayed `work/b_quadratic_pencil_maps.py`, its output and matrices. Verdict: the geometric quotient/marking bridge passes, with the genuine quotient constructions below supplying the reason that the linear systems describe the actual maps.

## The degree-two pencil

The divisor of poles of f1 is2A0, so its deck involution on the elliptic curve is

\[
h(Q)=2A_0-Q.
\]

Its cusp permutation is `O↔B0`, `A1↔A2`, `B1↔C2`, `B2↔C1`, with A0 fixed. The quotient U/h is a projective line with five removed images of cusps. The map to the tripod fills the two images O/B0 and B2/C1. Three of the four fixed points of h lie in U and give interior order-two branch points in the orbifold quotient.

The actual relative pro-three orbifold extension has kernel N and quotient C2. An order-two stabilizer at one of these interior branch points is killed by the map to the pro-three tripod; hence its induced based involution satisfies `φh=φ`. Any other complement is N-conjugate by coprime Schur–Zassenhaus. Precomposing a homomorphism with a source inner automorphism changes it by a target inner automorphism. This justifies using the computed order-two representative when determining φ up to its allowed target conjugation.

The parent word calculation is stronger than an arbitrary order-two matrix assertion. The chronological word h has square `Int(k)` and fixes k. After chronological-to-fibre reversal, the actual square is `Int(M_k^−1)`. Multiplication by `Int(M_k^{1/2})` gives a literal order-two lift, because two is invertible in the pro-three group and h fixes k. The checked quadratic square identity is the class-two image of this group identity.

Killing the B0 and B2 peripherals, together with invariance under h, kills both filled pairs. The remaining A1 and B1 peripherals have degree-one images x and y, with ramification index one. A single target inner conjugation can normalize their degree-two parts simultaneously to zero: every IA automorphism of the free rank-two class-two pro-three group is inner. This fixes exactly the gauge used in the calculation.

## The degree-three pencil

The map f2 is invariant under `σ:(X,Y,Z)->(X,Y,ζZ)`. Its three fixed points are C0,C1,C2, all removed from U. Hence U→U/σ is a genuine étale cyclic cubic cover. The quotient again has five punctures; the target tripod fills the images of C0 and C2, while the image of C1 is infinity.

The small positive loop around the quotient image of C0 lifts to the positive one-third tangent path at C0 and has cube the C0 peripheral loop. That quotient point is filled in the tripod. Therefore the corresponding exact based automorphism obeys `φσ=φ`, not merely an outer equality.

The actual tangent lift and the parent σ-word have the same homology matrix, preserve the same peripheral δ, and have cube `Int(δ)` in chronological convention. Nielsen's rank-two outer identification makes their difference inner. Preservation of δ forces that inner element into its cyclic centralizer, and the equal cube forces its exponent to be zero. This pins the word used by the code. The same argument pins the half-tangent word for the preceding involution.

After killing C0 and C2, the A0 and B0 images can be normalized to x,y by the same rank-two IA-inner argument. Thus the equations used in the script are necessary for the actual geometric map in a completely specified marking.

## The exact solutions and their meaning

The script uses the original V basis with its *pure class-two BCH lifts* expressed in the known Schreier basis. This is legitimate over Z3 because only division by two occurs. The actual peripheral elements retain their computed quadratic terms; they are not silently replaced by the corresponding abelian basis vectors.

In intrinsic fibre-functor Hall coordinates, the two unique quadratic rows are

\[
q_1=(3/2,0,3,0,-1,0,-1,0,0,-1),
\]

\[
q_2=(0,1/2,0,0,0,0,1/2,-1/2,0,0).
\]

Each defining linear system has rank ten, and direct substitution verifies the symmetry equation, both filled peripheral equations and both normalization equations. The replay is `work/c_B43_quadratic_replay.out`. Every denominator is a three-adic unit.

The uniqueness here is conditional on the displayed geometric marking and target gauge, which the quotient argument supplies. It is not a claim that arbitrary choices of lifts of V have the same quadratic row. These actual pullbacks remove the previously unspecified quadratic geometric map in the two pencil comparisons. Determining an arithmetic homogeneous parameter still requires subtracting a reference origin with its actual cocycle; raw nonabelian Frobenius values remain affine data, as explained in B.43.
