# Independent audit of the nonproper analytic stack obstruction

## Verdict

The proposed correction is necessary. Two distinct assertions must be separated: descent at a fixed actual neighbourhood stage, and passage from termwise neighbourhood germs on an étale atlas to the intrinsic system of actual open neighbourhoods of the quotient stack. Fixed-stage sheaf descent remains valid. The latter interchange fails for nonproper étale analytic groupoids. It can fail for full sheaves even when invariant radial tubes exist; it can also fail for covering germs themselves when no small invariant neighbourhoods exist.

This audit checks the examples and the replacement argument independently. It does not identify a nonproper étale groupoid stack with a proper finite-stabilizer orbifold. The word “multiplicité” in the supplied transvection example encompasses the former: its displayed stabilizer is infinite.

## 1. The rotating roots-of-unity example

Let the discrete group Gamma = mu_infinity act on the unit disc by rotations, and let the closed substack be B Gamma at the origin. In simplicial degree q, its atlas is Gamma^q times the disc. A neighbourhood of Gamma^q times the origin can choose a different radius for each tuple. This is the crucial distinction from a pullback of one invariant neighbourhood downstairs.

Choose pairwise disjoint annuli A_n = {2^(-n-1) < |z| < 2^(-n)} and continuous radial bumps b_n supported strictly inside A_n, nonzero somewhere, with sup |b_n| <= 2^(-n). Define f(0)=0 and f(r exp(i theta)) = b_n(r) cos(n! theta) on A_n, and zero elsewhere. This is continuous, including at the origin. For an element of order m, all annuli with n >= m are invariant for this function because m divides n!. Thus f(gz)=f(z) as a neighbourhood germ for every fixed g. The same holds simultaneously for each fixed finite tuple of elements and its products. It gives the full atlas-germ descent datum.

The target Sh(R) makes the argument particularly strict. Geometric morphisms to this localic topos are determined by the inverse image on its open subterminals, hence by continuous functions. Since R is Hausdorff, transformations between the corresponding maps are unique when they exist and force equality. All cocycle identities are therefore automatic once the functions agree as germs.

A geometric morphism from the actual quotient-neighbourhood to Sh(R) is a Gamma-invariant continuous function on that neighbourhood. Dense rotations force every such function to be radial. Every actual invariant neighbourhood contains an invariant disc. The function f is nonradial on every disc, so its object-level germ cannot agree with the pullback of any actual quotient-neighbourhood map. The induced functor from intrinsic-germ maps to atlas-germ descent data is not essentially surjective.

Finite stabilizers alone are not a sufficient repair. Let Gamma act freely by rotations on the first coordinate of C* times the disc, with divisor C* times {0}, and define f(z,w)=b_n(|w|) cos(n! arg(z)) on the corresponding w-annuli. The same argument applies. Any neighbourhood of the divisor contains a uniform w-disc over the compact circle |z|=1, while actual invariant functions are radial in z. This version has trivial isotropy at every point and still fails because the groupoid is not proper.

These rotating examples do not, by themselves, refute covering-germ descent. In the point example, equivariant radial retractions give a uniform covering model. Its rotation-lift group is Q, in the extension 0 -> Z -> Q -> Q/Z -> 0. Thus the intrinsic covering germ has classifying topos BQ. Arbitrary continuous functions are the detector for the failure just proved.

## 2. The parabolic example also detects covering germs

Let Gamma=Z act on P1 by g(z)=z/(1+z), fixing 0. The identity

    g^n(z)=z/(1+n z)

holds for every integer n, and the derivative at 0 is 1.

Every orbit of a point other than 0 accumulates at 0. If an invariant open neighbourhood V of 0 were proper, its nonempty closed invariant complement would contain such an orbit and hence 0, a contradiction. Therefore the only actual open neighbourhood of the closed substack [0/Z] is the whole quotient stack [P1/Z].

After deleting the closed substack, w=1/z identifies the open quotient with [C/Z], where Z acts by w -> w+1. This action is free and properly discontinuous, and the exponential map identifies its quotient with C*. Its covering fundamental group is Z.

The punctured normal stack is C* times BZ, because the derivative action on the normal line is trivial. Its fundamental group is Z^2. A positive normal circle maps to a large circle in C_w, which contracts in C_w before taking the quotient; the operator generator maps to the deck generator. Therefore the tangential map is exactly

    Z^2 -> Z, (normal, operator) -> operator.

Its kernel is the normal Z, and the finite-covering version is the identical projection Zhat^2 -> Zhat with kernel Zhat. Hence the intrinsic covering-germ and tangential equivalence itself fails in this nonproper multiplicité. A formal étale normal germ can still carry the Z^2 model, but it must not be called the intrinsic system of actual open neighbourhoods.

The transvection example of F.20 is a separate nonproper example, and remains valid in that stated scope. It is not a counterexample to the existence of an invariant smooth tubular neighbourhood for a proper finite-group action. In its specific deleted quotient, putting w=x/y gives (C/Z) times C*; uniform invariant tubes |y|<epsilon exist and its covering group is Z^2. Thus the parabolic example, rather than the transvection itself, supplies the needed covering-germ counterexample.

## 3. Correct proper étale replacement

For a proper étale analytic groupoid with paracompact coarse space, work with a locally finite relatively compact orbifold-chart cover of the coarse space. Each chart has a finite stabilizer group. Properness makes the arrow space between compact chart pieces compact; étaleness covers that compact set by finitely many local bisections. The same applies to the compact restrictions of composable pairs, which carry the cocycle equations. Thus each compact chart member has only finitely many actual local constraints. Shrink on those finite charts, use finite-group invariant normal metrics, and choose a positive continuous minorant on the coarse space. Fixed-stage descent then glues the data on an actual neighbourhood stack. Arbitrary transformations and equality of transformations are handled by the same finite chart-pair/triple argument.

One must not assert that every neighbourhood in every chosen atlas contains an invariant neighbourhood. Even the proper Z-translation action on R_x times R_y, with closed invariant line y=0, has the neighbourhood |y|<exp(-x^2), which contains no invariant neighbourhood. The correct proof chooses a finite local chart family on the quotient, descends there, and compares with the original atlas data on termwise common refinements. Properness supports this proof; it does not justify a false global lower bound along a noncompact atlas orbit.

## 4. Required scope propagation

F.13 needs the proper/synchronizable intrinsic-stack qualification and the nonproper refutation. The final stack sentence in F.18, the intrinsic stack statement and descent paragraph in F.19, and the final intrinsic-germ stack comparison in F.27 must use the same scope. Any stack reading of F.26/F.28 must inherit it. F.20 remains in the explicitly broader nonproper category. F.23 uses a finite mu6 quotient and is unaffected. The Mbar0,4 and Mbar0,5 tests, the algebraic tame constructions, and the compactification calculations are unaffected.

F.34 was stated for a locally compact paracompact Hausdorff space. Its branch-identification sentence has now been clarified to mean the Čech groupoid of its locally finite Hausdorff chart cover, not an arbitrary nonproper quotient atlas. No change to its space-level theorem is needed.
