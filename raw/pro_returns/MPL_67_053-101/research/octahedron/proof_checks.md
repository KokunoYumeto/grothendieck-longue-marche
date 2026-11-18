# Limited mathematical checks for O01–O13

These checks were made after the diplomatic text was frozen. They are checks by this run, not external referee verdicts; no claim of novelty is made. The exact finite computations use only the Python standard library. Their scope is explicitly limited below.

## 1. Extending the Klein group of four points (O01)

Normalize the four distinct points to ∞,0,1,λ with λ≠0,1. The three transformations

\[
 z\longmapsto\frac{\lambda}{z},\qquad
 z\longmapsto\frac{z-\lambda}{z-1},\qquad
 z\longmapsto\frac{\lambda(z-1)}{z-\lambda}
\]

induce the three double transpositions. Their squares are the identity and their compositions reproduce the permutation group of the four points: equality follows from agreement on three points. Uniqueness of a projective transformation with three specified distinct images proves uniqueness of each extension. This supplies the elementary check of the claim on scan84, but says nothing about a profinite realization problem.

## 2. Normalizer and complements (O02, O05, O06)

Assume char(k)≠2 and every element of k has a square root. An involution has two k-rational fixed points, which can be put at 0 and ∞; it then acts by z↦−z. A commuting independent involution must interchange these points and has form z↦a/z; a coordinate rescaling using √a makes it z↦1/z. Thus every faithful Klein group has the displayed standard model V.

A projective transformation commuting with z↦−z preserves {0,∞}, hence is cz or c/z. Commuting also with z↦1/z forces c²=1, giving exactly V. The conjugation map N(V)→Aut(V)=S₃ therefore has kernel V and image of size at most6. Choose i²=−1; the maps iz and (z+1)/(z−1) preserve V and induce two different transpositions on the three pairs {0,∞}, {1,−1}, {i,−i}. Hence the image is all S₃ and |N(V)|=24.

The induced permutation action on the six vertices is independent of the field: all six elements are distinct, and substituting i²=−1 computes the same permutations. This is the usual orientation-preserving octahedron subgroup; its action on the four antipodal face-pairs is faithful and hence identifies it with S₄. The finite script explicitly checks this faithful order24 action over F₅ and F₉; the same six-vertex permutations establish the general statement. A face stabilizer has order3 because the group is transitive on eight faces; a face-pair stabilizer has order6 because it is transitive on four such pairs, and the Klein group acts freely on those pairs. Thus only the latter is a complement to V, as Hua §XI already points out.

For the cohomological addition explicitly credited to Hua §XI, `complements_check.py` enumerates every map GL₂(F₂)→F₂² (4⁶=4096 cochains). It tests f(gh)=f(g)+g f(h) for all pairs and finds four cocycles. The four functions g↦g v−v are distinct and exhaust them, so H¹(S₃,V)=0. Equivalently, the complements are simply transitively conjugate under V. This computation validates the finite cohomology claim, not any of the register's infinite-group comparisons.

## 3. Characteristic5 counterexample and the refined datum (O03, O04, O09)

Work over k=algebraic closure of F₅ and put i=2. Then

\[
 S=\{0,\infty,\pm1,\pm i\}=\mathbf P^1(\mathbf F_5).
\]

The translation t(z)=z+1 preserves S. It conjugates −z to 2−z, which does not lie in V={z,−z,1/z,−1/z}; therefore V′=tVt⁻¹ differs from V. Nevertheless its fixed-point union is tS=S. This is already a complete explicit refutation of the asserted injectivity V↦S on scans84 and86.

The script enumerates the 120 invertible 2×2 F₅ matrices up to nonzero scalar, finds N(V) of order24, and finds five conjugates of V with that same fixed set. Moreover every projective transformation over the algebraic closure preserving S is defined over F₅: its values on any three distinct F₅ points lie in F₅, and the unique projective transformation with those three values has F₅ coefficients. Thus Aut(P¹,S)=PGL₂(F₅) has order120 even over the algebraic closure, whereas Aut(P¹,V)=N(V) has order24. The claimed equivalence using bare pairs (X,S) therefore fails by automorphism groups, independently of any choices of representatives.

A partition of S into three antipodal pairs supplies the missing data. Define the three nonidentity permutations that fix one pair pointwise and exchange the two points in each of the other pairs. Together with the identity they form a canonical V. Conversely, if the fixed-point condition on scan87 holds, the three fixed pairs are disjoint and every nontrivial element exchanges the other two pairs, so this construction recovers the given subgroup. A projective transformation preserving the pairing normalizes this recovered subgroup; one normalizing it preserves its fixed pairs. Consequently retaining the pairing, rather than just S, restores the normalizer as automorphism group in characteristic5. This refinement is a sufficient repair of the lost finite data, not a claim to have completed the manuscript's arithmetic descent construction.

## 4. The quotient coordinate (O12)

For char(k)≠2, set q(z)=z²+z⁻². It is invariant under both generators of V, and the rational map (z⁴+1)/z² has degree4. The invariant function-field extension therefore has degree exactly |V|=4, so q is a quotient coordinate. Away from 0 and ∞,

\[
 q'(z)=2(z^4-1)/z^3.
\]

Its four zeros ±1,±i are distinct and give ramification index2; 0 and ∞ also have local degree2. The three branch values are 2,−2,∞, distinct because char(k)≠2. This rechecks the earlier coordinate claim in `MPL_142_094-122_notes.md` B01 (scan108) rather than treating it as an established prior result. It does not identify an arithmetic level-four family without the additional descent and level-structure data.

## 5. Characteristic3 geometric fixed points (O08)

The script works in F₉=F₃[i]/(i²+1), enumerates all 720 projective matrices, extracts the normalizer of standard V, and acts on P¹(F₉). It finds all its nonidentity fixed points in orbits of sizes6 and4, with stabilizers of orders4 and6 respectively. For every nonidentity matrix (a b; c d), the fixed-point equation has discriminant (a−d)²+4bc; the script checks that the F₉ fixed-point count is1 when this discriminant vanishes and2 otherwise. Thus every geometric fixed point over the algebraic closure is already counted; the computation is not merely a rational-point sample.

Order-three projective transformations in characteristic3 are unipotent and have one fixed point rather than two, explaining the collision of the usual complex face-centre picture. The six-vertex octahedral permutation model and the normalizer S₄ remain intact; the separate point configuration of twelve edge midpoints and eight face centres asserted in Hua §XI cannot be transported unchanged to this characteristic. The manuscript's NB names those geometric constructions without explicitly writing their counts, so the note qualifies its interpretation rather than claiming to refute a numeric statement absent from the ink.

## 6. The conditional twisting identity (O11)

Fix a reference V-line X₀, and define X(T)=T×^V X₀ for a V-torsor T. The successive quotients of T×T′×X₀ by the two commuting V-actions give a canonical isomorphism

\[
 X(T\wedge T')\simeq X(T)\wedge_V T'.
\]

This is associativity of the contracted product with the specified actions. It checks the identity conditional on that definition; it does not manufacture a canonical X₀ from the nearly cancelled passage on scan87. The distinction agrees with Hua §XI's explicit decision to use a chosen reference line in its modernised interpretation.

## 7. Generic isotropy of the two groupoids (O13)

For fixed distinct labels, three ordered points determine a unique normalizing projective transformation, and the fourth has coordinate λ; consequently the fully labelled object has trivial automorphism group. If permutations of the four-element label set are allowed, its generic automorphisms are the four double transpositions, because the six anharmonic transforms of λ are generically distinct. On the target of scan89, the permutation action on the three partitions factors S₄ through S₃, with the same V kernel; hence generic isotropy also has order4.

This verifies the generic automorphism warning stated in Hua §XI and the distinction already present at LM scans549–552. It is not a proof of an equivalence over arbitrary schemes, of compatibility with degeneration, or of the register's completed tower constructions.
