# Independent review of the two-branch cubic construction

Date: 2026-11-14. Reviewer: degeneration agent. Source reviewed: audit/A_cubic_two_branch_candidate.md, including its general multiplication-pullback construction and its elementary abelian extension. The candidate and the shared A section were not edited in this review.

## Decision and exact scope

**The complete candidate passes independent adversarial review.** It proves geometrically prime-to-two point-section injectivity for every smooth proper curve of genus at least two admitting, geometrically, a cyclic cubic cover of an ordinary elliptic curve in characteristic two. The same argument with character quotients proves the result for elementary abelian exponent-three covers of an elliptic curve; the supersingular case is already covered by A.29. The extension to finitely generated base fields and hyperbolic open subcurves is valid with the spreading correction stated below.

The essential argument uses A.21 in its proved form: the map to a genus-one target need only be finite separable, and it must have one fibre in which every index is divisible by a fixed prime-to-characteristic integer greater than one. It need not be Galois. Each reflection quotient below supplies such a fibre with all indices equal to six.

The proof does not assert injectivity from the elliptic target alone, does not lift a collision through an even-degree cover, and does not assume that two quotient maps jointly embed the curve at ramified fibres. Each of these issues is handled explicitly.

## 1. Existence of every required two-branch auxiliary

Work initially over an algebraically closed field of characteristic two. For distinct A,B on the ordinary elliptic curve E and a∈{1,2}, choose a degree-zero divisor D₀ with

\[
3[D_0]=a[B-A]\quad\text{in }\operatorname{Pic}^0(E).
\]

Multiplication by three is surjective, so this is possible. Choose f with divisor a(A−B)+3D₀. Its cubic Kummer cover T/E is connected, since the valuation of f at A is nonzero modulo three, and is cyclic of degree three. Its only ramified points downstairs are A,B, each with index three. At all other points the valuation of f is divisible by three, and the local unit has a cube root in the completed local ring. Tame Riemann–Hurwitz therefore gives g(T)=3.

This construction allows arbitrary unramified Kummer twists. The reflection argument does not require a special choice among them.

## 2. The reflection really lifts as an involution

Set ρ(t)=A+B−t. It exchanges A and B and induces minus one on Pic⁰(E), since translation acts trivially there. Hence D₀+ρ*D₀ is principal. It follows that fρ*f has divisor three times a principal divisor. After extracting a constant cube root in the algebraically closed field, choose h with

\[
h^3=f\rho^*f.
\]

For z³=f, the map τ on T defined by τ|k(E)=ρ* and τ(z)=h/z is an automorphism. It conjugates the cubic deck generator δ to δ⁻¹. Moreover

\[
\tau^2(z)=\frac{\rho^*h}{h}z.
\]

The ratio is a cube root of unity and thus a constant. Applying ρ once again shows that its square is one. Since its order also divides three, it is one. Therefore τ has order two; no unresolved lifting obstruction remains.

The same conclusions apply to τ′=δτδ⁻¹. The two involutions are distinct.

## 3. Wild differents and the genus-one quotient

Ordinarity gives exactly two geometric solutions to 2t=A+B. Neither is A or B, because ρ exchanges those distinct points. Consequently T/E is étale over both fixed points of ρ. On each three-element deck torsor τ acts by inversion followed by a translation, so it fixes exactly one point. These are all fixed points of τ.

The quotient E/ρ has genus zero. Its two fixed points are wildly ramified for the quadratic map. Each different exponent is at least two, while Riemann–Hurwitz makes their sum four; hence each equals two. An independent local check is available: choose an ordinary Weierstrass model with a₁=1 and a₃=0. At the origin the uniformizer u=x/Y transforms under inversion as u/(1+u), giving valuation two to the difference of the two parameters. Translation to either fixed point conjugates the reflection to this local action.

At a τ-fixed point of T, the étale map T→E identifies completed local rings because the residue field is algebraically closed. The identification intertwines τ and ρ. Therefore the different exponent upstairs is still two, rather than an unspecified wild contribution.

For H=T/〈τ〉, with its smooth proper normalization, wild Riemann–Hurwitz gives

\[
2g(T)-2=4=2(2g(H)-2)+2+2,
\]

so g(H)=1. The same proof gives g(T/〈τ′〉)=1. The calculation depends on cubic degree and on E being ordinary; those hypotheses are retained.

## 4. Why the elliptic target has an entire suitable ramified fibre

Let V/E be a connected abelian cover of exponent three containing T. Suppose x is a fixed point of ρ, is different from A,B, and is ramified in V/E. The tame inertia in an exponent-three cover has order three, so every point of V above x has index three.

There is exactly one τ-fixed point Q of T above x. Put y equal to its image in H. The fibre of the degree-two map T→H over y is the single point Q with index two. This singleton-fibre fact is essential: the other two points of T above x are exchanged by τ and map to a different point of H.

Since T/E is unramified at x, every point of V above Q has index three in V→T. Thus every point over y under V→H has index

\[
e(V/H)=e(V/T)e(T/H)=3\cdot2=6.
\]

There are no additional points in that fibre. A.21 therefore applies to V→H with m=3. It also applies to the conjugate quotient H′, using its own unique τ′-fixed point above x. This remains valid although the composite maps to H and H′ need not be Galois.

If a point-section collision on V has equal E-images, write P_T,Q_T for its images in T. Equality in both elliptic quotients gives either P_T=Q_T, or

\[
Q_T=\tau P_T=\tau'P_T=\delta^2\tau P_T.
\]

The latter case makes Q_T fixed by δ. Both P_T and Q_T then lie at the totally ramified points over A,B. Their common E-image forces them to be the same point. Thus equality in the two quotients and in E implies equality in T on every fibre, including the ramified fibres. No global closed-immersion claim for the product of the two quotient maps is needed.

## 5. The original three-point family as a special case

For D={0,d,2d}, with d of exact order three, the residue vectors

\[
(1,-1,0)+(0,-1,1)=(1,1,1)\quad\text{in }\mathbf F_3^D
\]

give two such auxiliaries. For either pair A,B the omitted point x satisfies A+B=2x, because the sum of the three points is zero and 3x=0. Thus it is fixed by the relevant reflection, is not a branch point of that auxiliary, and is a branch point of the original cubic cover.

The common Kummer cover is étale over the original cover. Its two reflection quotients for each auxiliary force equality of the auxiliary images. The residual unramified character must also be included; its equality follows from A.21 as in Section7 below. This proves the whole exact-order-three family without any upper bound on the Prym packet's two-primary orders.

## 6. General cyclic cubic covers: all nine points of each multiplication orbit

Let C/E be any cyclic cubic cover with g(C)≥2. It is ramified, since an unramified cover of a genus-one curve again has genus one. Pull back along [3]:E→E. The pullback C′ is connected: its cubic function field is Galois of prime degree and ramified, whereas the degree-nine isogeny field is unramified. Any nontrivial intersection would contain that whole cubic field and would make it unramified, a contradiction. Thus C′→C is a connected étale E[3]-torsor of degree nine.

Every original branch point gives a coset G=t₀+E[3] of nine branch points on the new elliptic base. The pullback is étale on the base, so its nonzero branch coefficient a modulo three is constant on G. For each such coset,

\[
a\sum_{g\in E[3]}[t_0+g]
=\sum_{0\ne g\in E[3]}a([t_0+g]-[t_0])
\quad\text{in }\mathbf F_3[G].
\]

The coefficient at t₀ on the right is −8a=a modulo three, and the other coefficients are a. This proves the identity for every coset; it is not an empirical check on selected elliptic curves.

For each nonzero g, take A=t₀+g and B=t₀ and the corresponding two-branch auxiliary with residues a,−a. The point

\[
x=t_0-g
\]

is a third, distinct point in the same branch coset. Since 3g=0,

\[
2x=2t_0-2g=2t_0+g=A+B.
\]

Hence x supplies precisely the ambient ramified fixed point required in Section4. The argument treats all eight nonzero g, including every direction in the two-dimensional group E[3].

Let V be the common Kummer field of C′ and all these auxiliaries, over all branch cosets. It is connected by taking the field compositum, and its Galois group over E is elementary abelian of exponent three. There is no new branch point. At a branch point, all ramified completed cubic Kummer fields are the same tame extension of kbar((u)), since their indices are three and local units have cube roots. Thus the local index of V/E remains exactly three, not a higher power of three. The indices of V/E and C′/E agree everywhere, proving that V→C′ is étale.

The normal closure of V→C has odd order. Indeed C′→C is a Galois 3-group cover. Take all conjugates of V over C′ under that group. Their compositum over C′ is still an elementary abelian 3-extension, and is normal over C. Its Galois group is an extension of E[3] by an elementary abelian 3-group. Every constituent cover is étale, so this is a finite étale cover with 3-group geometric monodromy. Thus A.3 applies to lift any collision on C to V. No even-degree cover is used for the lifting.

## 7. Recovering the original character, including its unramified part

A.21 on V→E first gives equal E-images for the lifted pair, because V/E has full index three on its nonempty branch set. Section4 then applies to every auxiliary and gives equality of its images.

Write the equation of C′/E as w³=F and let f_g be all the auxiliary Kummer functions. The branch-vector identity shows that R=F/∏f_g has every valuation divisible by three. Its cube root therefore defines an unramified cyclic cover H₀/E, or the trivial cover if the Kummer class is zero. This field is contained in V. A connected nontrivial H₀ is a genus-one curve.

At any point of H₀ lying over a branch point of V/E, every point of V has local index three over H₀ because H₀/E is unramified. Hence A.21 on V→H₀ gives equality there as well. In the trivial case equality is already equality in E.

The images on C′ of distinct original C-points are still distinct. Their common E-image cannot be a branch point of C′, since its totally ramified cubic fibre would have only one geometric point. Thus the lifted pair lies over an unramified E-fibre of V, and has the form R_V,gR_V for a unique element g of Gal(V/E).

Equality in every auxiliary kills each auxiliary character on g; equality in H₀ kills the residual character. The exact Kummer identity is

\[
\chi_{C'}=\left(\prod_g\chi_{T_g}\right)\chi_{H_0}.
\]

It follows that the C′-character of g is trivial, forcing equality of the C′-images and contradicting their distinct original C-images. This formulation uses deck characters, so it does not require evaluating a chosen rational Kummer generator at a point where that generator could have a zero or pole of order divisible by three.

## 8. Elementary abelian exponent-three covers: stabilizers at branch fibres

Let C/E be Galois with G=(Z/3)^r and g(C)≥2. It is ramified. Since the residue characteristic is two and the group has exponent three, every nontrivial inertia group is cyclic of order three. A.21 gives equal E-images for a collision.

For every nontrivial character χ:G→Z/3, the quotient C_χ/E is cyclic cubic. If it is ramified, its genus is at least two and the cyclic theorem just proved gives equality of the quotient images. If it is unramified, C_χ has genus one; the map C→C_χ still has full ramification index three above any original branch point, because that inertia lies in kerχ. A.21 gives equality in this quotient as well.

Now fix P,Q in the same geometric E-fibre and write Q=gP. Let I=Stab_G(P). Equality in C_χ is exactly the condition g∈kerχ·I, since the quotient fibre is a kerχ-orbit. In particular, for all characters factoring through G/I the condition is χ(g)=0. Those characters separate elements of the elementary abelian group G/I. Therefore g∈I and Q=P. This works equally on unramified and ramified fibres and proves the claimed elementary abelian extension.

## 9. Finite fields, spreading, and the precise remaining scope

Over a finite field all chosen geometric data, covers, automorphisms, constants and lifts descend after a finite extension of constants. The constructions therefore legitimately use A.3 and A.21, which preserve equality after such extensions.

Over a field finitely generated over F₂, a geometrically given elliptic map and action may require a finite extension of the **base field**, not only a constant-field extension. Make that finite extension first; point-section equality is preserved by restriction and distinct points remain distinct. Then spread the smooth proper curves, the finite tame action, and the quotient map over a finite-type base, shrinking so that the quotient degree and faithfulness persist. Ordinarity of the genus-one target persists after shrinking because it is an open condition. A.8 specializes any collision to a finite-field fibre in this same class, where it has been ruled out. Open subcurves follow by the quotient map to the proper compactification.

The higher-degree limitation is real: for a two-branch cyclic cover of odd prime degree e, the same reflection computation gives quotient genus (e−1)/2. A.21 alone does not establish injectivity on that target when e>3. This proof also does not settle cyclic 3-power covers of exponent greater than three.

Finally, the earlier necessary condition involving a full D-coset inside a Prym two-primary packet remains a separate torsion-geometric question. The present construction bypasses it by using full point-section equality and additional odd covers. In the abandoned direct Abel-class reduction, one can prove only that simultaneous two-primary norm and displacement leave an odd part killed by three:

\[
3x=\pi^*\operatorname{Nm}(x)+(2+\delta)(1-\delta)x.
\]

The common kernel of the norm and 1−δ can have nontrivial three-torsion, so it would have been incorrect to assert that x itself must be two-primary. That limitation does not affect the new finite-cover proof.
