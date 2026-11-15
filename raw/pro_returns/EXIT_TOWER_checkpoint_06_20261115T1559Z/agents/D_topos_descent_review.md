# Independent review: descent from finite level scheme atlases

This note proves the precise extension needed for the connected stable moduli stacks over `k=Qbar` in modular dimension at least three, using the checked variety reconstruction E.T8--E.T9. It does not assert that trivial inertia recognizes a scheme for every separated algebraic stack.

## 1. Choice of atlas and its intrinsic image

Let `M` be one of the indicated connected smooth separated Deligne--Mumford stacks. Choose a finite etale scheme level atlas `p:U→M`; a sufficiently high full level structure supplies one. A connected component of U is still finite etale and surjective, since its image is nonempty, open and closed in connected M. Thus one may take U connected. Its dimension is the modular dimension and it is smooth, normal and separated.

For an equivalence `F:X_et→Y_et` between two such stacks, use `F*` on sheaves. A finite etale representable morphism is precisely a finite locally constant object of the small etale topos. Therefore `V=F*(U)` is a finite etale representable object over X. The representable finite etale object is a Deligne--Mumford stack over X, initially without any claim that its source is a scheme. The slice equivalence is

`V_et ≅ X_et/F*(U) ≅ Y_et/U ≅ U_et`.

At a closed geometric point over Qbar, the automorphism group of its point functor is the geometric stabilizer. One can see this on an etale atlas by strict localization: the scheme strict-local point has no automorphisms, and its descent automorphisms are exactly the arrows of the atlas groupoid fixing that point. Equivalently, its residual gerbe is `B I_x`, whose stalk functor has automorphism group `I_x`. No residual absolute Galois group remains because the closed residue field is Qbar.

The equivalence of slices preserves these point-functor automorphisms and the closed-point condition (closedness is recovered from the open-set lattice). All closed-point stabilizers of V are consequently trivial, since those of U are trivial. If inertia had a nonidentity geometric point anywhere, its nonidentity finite-type locus would contain a closed point; the identity section is open and closed in finite unramified inertia. Thus inertia is trivial everywhere. A Deligne--Mumford stack with trivial inertia is an algebraic space, so V is an algebraic space.

## 2. Why V is a scheme in the modular application

The coarse space `X_coarse` is a scheme. For these separated finite-inertia stacks, the coarse morphism `X→X_coarse` is proper and quasi-finite. Since `V→X` is finite, the composite `V→X_coarse` is proper and quasi-finite. It is a morphism of algebraic spaces and is therefore finite. An algebraic space finite over a scheme is a scheme. This proves that V is a scheme; it does not use a false general identification of algebraic spaces with schemes.

Moreover V is finite etale over smooth X, hence smooth and normal. Its finite map to the separated coarse scheme makes it separated. It has dimension at least three. Consequently E.T9 applies to the slice equivalence and gives an isomorphism of schemes

`f_U: V → U`.

Its generic field map is precisely the map recovered from the generic slice equivalence by E.T8.

## 3. Recovering the groupoid and every structure map

Set `R=U×_Y U` and `S=V×_X V`. The first is a scheme: `R→U` is finite etale representable. The second is a scheme for the same reason, now that V is a scheme. Since `F*` preserves finite limits, `F*(R)=S` as objects over X. Applying the slice reconstruction E.T9 component by component gives an isomorphism

`f_R: S → R`.

All projections, unit, inverse and multiplication in these two groupoids are etale morphisms. For example, the unit of an etale groupoid is an open immersion; multiplication is the base change of a source/target map followed by the groupoid isomorphism identifying composable arrows, and is etale. The triple fibre products are again finite etale schemes over U or V.

The recovered maps commute with each groupoid structure map. The exact reason is finite-extension functoriality, not an unspecified choice of generic basepoints. On a connected component of a dominant etale morphism, the inclusion of function fields is finite separable, and the generic etale topos morphism is restriction to the associated open subgroup of the absolute Galois group. The square of slice equivalences commutes before reconstruction. E.T8's compatibility on open subgroups therefore makes the recovered generic field maps commute with these finite field embeddings. The corresponding scheme maps agree on the dense generic open, and their targets are separated; hence they agree everywhere. Apply this reasoning to both projections, the unit, inverse, and multiplication. It proves that `(f_R,f_U)` is an isomorphism of groupoids, with all identities and compositions preserved.

Descent gives an isomorphism of stacks

`f: X=[S⇒V] → [R⇒U]=Y`.

The descended topos equivalence agrees with F, not merely with its generic restriction. On the atlas slice this is E.T9; on the double-overlap slice it is the same statement, and the natural isomorphisms agree on the triple overlaps by the just-proved functoriality. Effective descent for sheaves along the epimorphism U therefore identifies the resulting inverse-image functor with F* on the whole topos. The same argument makes the construction independent of a replacement atlas: use their common finite etale refinement and the two projections.

## 4. One automorphism of the constant field

With a connected U, the recovered generic field isomorphism has one restriction `sigma:k→k`. Every connected component of R has projections finite etale and surjective onto U, so generic finite-extension compatibility forces its recovered map to have the same restriction sigma. The groupoid isomorphism and its descended stack isomorphism are therefore sigma-semilinear.

The same conclusion holds without first making U connected. Every nonempty connected component U_i of a finite etale atlas surjects onto connected Y. Hence `U_i×_Y U_j` is nonempty for every pair i,j. A connected component of this fibre product gives finite separable generic extensions of both `k(U_i)` and `k(U_j)`. Its recovered field map restricts to each component field map, so the restrictions to k coincide. Thus all sigma_i are one sigma. There is no independent constant-field action on different atlas components.

## 5. Uniqueness

The field reconstruction makes the map on each atlas component unique. Normality and the codimension-one valuation reconstruction make the scheme maps unique, and the generic compatibility makes the groupoid maps unique. Descent then makes the stack isomorphism unique up to 2-isomorphism. Conversely, any stack isomorphism gives the original unringed etale topos equivalence. Thus the claimed comparison is a bijection on isomorphism classes for these modular stacks, assuming exactly the E.T8--E.T9 reconstruction already checked.

## Verdict and scope

The finite-level-atlas descent is valid with the coarse-scheme argument explicitly included. It covers the requested stable modular stacks of dimension at least three. The dimension-two cases require an additional birational reconstruction input and are not established by this note.

## E.T12: connected-band Cartesian sheaves

Read the entire E.T12 statement, convention and proof. The result is valid for the explicitly defined category CartEt of Cartesian set-valued sheaves on the presentation's simplicial etale sites. Here is a direct all-sheaves justification of the full-faithfulness step. Represent an etale sheaf F over a scheme S by its etale algebraic space E→S. A section of p*F over H is a map H→E over S. Its restriction to a geometrically connected fibre of p is constant, since an etale geometric fibre of E is discrete. Therefore its two pullbacks to H×S H agree; the equality locus is open, and it contains every geometric point. Effective fpqc descent for maps to an algebraic space yields a unique S-section. Apply this after every etale base change U→S to obtain F=p_*p*F, hence full faithfulness of p*. The group descent isomorphism is p*beta; its cocycle at the identity section gives beta=beta², so the invertible beta is the identity. Morphisms obey the same argument.

These constructions are the literal pullback along B_SH→S and restriction along the trivial torsor. They commute with base change, so descent on a smooth atlas and its relation spaces gives the general base-stack version. A common smooth refinement identifies the categories from two presentations. For DM stacks an etale atlas gives the ordinary small-etale sheaf descent equivalence; thus this convention agrees with the preceding stable results.

The PGL2, Aff1 and Gm cases consequently give Set, and the elliptic torsor case gives the small etale topos of M11. The nontrivial M10 algebraic automorphism tensors by an E-torsor while inducing the identity on the Jacobian base, so its CartEt action is the identity under the displayed pullback equivalence. The map for BGm likewise lands in Aut(Set)=1. The convention is essential: no identification of the entire ambient lisse-etale topos is proved or asserted by this argument.
