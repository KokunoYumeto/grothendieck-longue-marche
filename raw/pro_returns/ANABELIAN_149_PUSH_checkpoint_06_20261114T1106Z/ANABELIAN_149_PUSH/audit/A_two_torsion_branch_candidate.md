# Point separation from opposite two-torsion branch pairs

Status: root-reviewed, accepted, and integrated as A.29k. The historical candidate filename is retained. The argument uses A.29j and gives a positive class that is separate from the odd-order branch-difference obstruction. No general conclusion for ordinary elliptic quotients is claimed.

## Proposed statement

Work over a finite field of characteristic two, allowing finite constant extensions to define the following geometric data. Let E be ordinary, and let T₂ be its unique nonzero geometric two-torsion point.

1. Let C/E be a connected cyclic cover of odd degree n, with C of genus at least two. For a Kummer presentation zⁿ=F, write a(t)=ord_t(F) modulo n. Suppose

   a(t+T₂)=−a(t) for every geometric point t of E.

   Then A1 holds for C over every finite extension. This includes every cyclic odd-degree cover fully ramified at exactly two points whose difference is T₂, for every choice of its unramified/Picard-root component. Partial ramification and composite n are included in the skew-residue statement.

2. More generally, the same conclusion holds for an abelian odd-order cover C/E such that the residue function of every cyclic character quotient satisfies that two-torsion skew condition. The condition is deliberately stated character by character, avoiding a choice-dependent identification of local inertia generators.

3. A second positive class is a two-point fully ramified cyclic cover of prime degree ell for which <2,−1>=(Z/ell)* and the difference of the branch points has even order d≤ell−1. Every Picard-root choice is covered. For ell=5 this includes branch differences of order two or four.

All three assertions spread to fields finitely generated over F₂ by A.8, after a finite extension of the base field to define the action, the relevant points, and all maps. Hyperbolic open subcurves are included as in the earlier A-results.

## 1. A selected auxiliary for every odd degree

Translate a branch point to O. For n>1 odd set A=P=T₂ in A.29j. The relation nP=−A is satisfied. The selected cover C₀/E has

div(f₀)=(n+1)(T₂)−(n+1)(O),

and genus n. Let X have divisor2(T₂)−2(O). Up to a constant, f₀=X^((n+1)/2). Since gcd((n+1)/2,n)=1, the function field is Kummer-equivalent to wⁿ=X.

The Cartier criterion in A.29j says that an even index j is killed exactly when j/2 is odd. Every multiplication-by-two orbit on the nonzero residues modulo n contains such an index. Indeed let j₀ be its smallest positive representative. If j₀ were even, j₀/2 would lie in the orbit and be smaller. Thus j₀ is odd. If j₀>n/2, then 2j₀−n would be a smaller positive representative in the same orbit. Therefore j₀<n/2, and 2j₀ is an even representative with (2j₀)/2 odd. All nontrivial character orbits consequently have nilpotent Cartier action. The stable Cartier image on C₀ is exactly the invariant line kω_E, so f(C₀)=1.

The reflection ρ(t)=T₂−t lifts as proved in A.29j. Write τ for a lift and H=C₀/〈τ〉. Then g(H)=(n−1)/2 and C₀→H has two fixed points, each of different exponent two. Cartier on H is nilpotent. To see this without invoking Deuring–Shafarevich, the separable pullback of H⁰(H,Ω¹) is a Cartier-stable subspace of H⁰(C₀,Ω¹). Its elements vanish to order at least two at a fixed point, by the different formula. The pulled-back elliptic differential ω_E is nonzero there, because C₀/E is étale at that point. Therefore this subspace has zero intersection with the stable Cartier image kω_E. Its own sufficiently high Cartier image is zero. By the opened stable-rank criterion, f(H)=0.

One can also see the target explicitly. Put E in Artin–Schreier form

v²+v=X+a+c/X, with c≠0.

Starting from Y²+XY=X³+a₂X²+a₆, use v=Y/X+sqrt(a₆)/X, a=a₂, c=sqrt(a₆). The auxiliary becomes

v²+v=wⁿ+a+c/wⁿ.

Choose b with bⁿ=c. The reflection τ(w,v)=(b/w,v) has quotient coordinate s=w+b/w. The Dickson recurrence D₀=0, D₁=s, D_r=sD_{r−1}+bD_{r−2} gives D_n(s,b)=wⁿ+(b/w)ⁿ. Thus the quotient is

v²+v=D_n(s,b)+a.

The polynomial has odd degree n and leading coefficient one, hence exactly one reduced Artin–Schreier pole of odd order n. The one-pole Cartier calculation already proved in A.21 gives p-rank zero. At w²=b there are exactly two fixed points (the two roots of the Artin–Schreier equation); w=0 and infinity are exchanged. This agrees with the norm construction and fixed-point count above.

## 2. Point separation on the selected auxiliary

Let δ be a generator of the cyclic deck group, and set τ′=δτδ⁻¹. Both reflection quotients have p-rank zero and positive genus. A.1 and the Abel map therefore separate their point sections. A.21 applied to C₀/E also forces equal elliptic images for a putative section collision.

Suppose R,S on C₀ have the same images in E and in both reflection quotients. If R≠S, then S=τR=τ′R. The product of the two reflections is δ² or δ⁻². Since n is odd, it generates the entire deck group. Hence R is fixed by the deck group. Full ramification means that R lies over O or T₂; τ sends it to the point over the other branch value. This contradicts the equality of the E-images. Thus R=S and A1 holds for C₀, over every finite extension.

This also clarifies why the reflection pair alone is insufficient at the two branch points; their common E-image is an essential part of the argument.

## 3. Arbitrary Picard roots with the same two branch points

Normalize the full branch residues of a cyclic n-cover C/E to1 and−1, as in A.29j. Let F be its Kummer function and f₀ the selected function above. Then div(F/f₀) is divisible by n. The connected cover U/E generated by an n-th root of F/f₀ is unramified, of degree d dividing n; if trivial, take U=E. Thus U is genus one.

The fully ramified extension C₀/E is linearly disjoint from U/E: every nontrivial subextension of C₀/E is ramified at the two branch points, while U/E is unramified. The compositum V=C₀U contains C, with its original root given by the product of the roots defining C₀ and U. At both branch points the ramification index of V/E is n, equal to that of C/E; elsewhere both are unramified. Hence V/C is étale of odd degree d and has odd Galois closure. Over a finite constant extension all these covers are Galois as asserted.

A collision on C lifts to V by A.3. Its C₀-images agree by Section2. Its U-images agree by A.21, since V/U is ramified with the same nontrivial odd index n over the fibres above a branch point. At a base point outside the branch pair the C₀ and U characters recover the C character, so its C-images agree. At either branch value the C-fibre is a singleton, so equality is automatic. Thus C has A1.

## 4. Composite-degree skew residue functions and partial inertia

Now assume a(t+T₂)=−a(t) for the cyclic degree-n cover C/E, without full inertia. Its nonzero residues occur in disjoint two-point pairs {A_i,B_i}, where A_i=B_i+T₂. Choose an orientation and integer representative a_i=ord_{A_i}(F) modulo n, with 0<a_i<n. Put

d_i=gcd(n,a_i), e_i=n/d_i, b_i=a_i/d_i.

Then e_i>1 is odd and gcd(b_i,e_i)=1. Over E with origin B_i, choose the Section1 auxiliary B_i^aux/E of degree e_i and function f_i with residues1,−1 at A_i,B_i. It has A1 by Section2. In its field choose u_i with u_i^{e_i}=f_i and put w_i=u_i^{b_i}. Then

w_iⁿ=f_i^{a_i}.

The latter Kummer character has order e_i and its n-residue vector is precisely a_i((A_i)−(B_i)). In the explicit function f_i=X_i^((e_i+1)/2), the corresponding valuation a_i(e_i+1) is congruent to a_i modulo n because a_i e_i is divisible by n. This checks the generator normalization even for composite n and partial coefficients.

Let V/E be the compositum of C and all these auxiliaries. It is an abelian odd-order cover. At a point in the i-th pair, the original cover and its only ramified auxiliary have the same tame index e_i; all other auxiliaries are unramified. Over an algebraically closed residue field a local tame extension of a prescribed index is unique, so the compositum index remains e_i. Hence V/C is étale and has odd Galois closure.

The quotient

R=F / product_i f_i^{a_i}

has divisor divisible by n. Its n-th root w_U=z/product_i w_i belongs to k(V). The connected residual cover U/E is therefore unramified and has genus one, or is E itself. There is at least one branch pair because C has genus at least two and a cyclic unramified elliptic cover has genus one. At any such pair, V/U still has ramification index e_i at every point of a fibre over U. A.21 applies, including when U=E.

Lift a collision to V. Its images on every B_i^aux agree by Section2, and those on U agree by A.21. In particular its E-images agree. Choose g in Gal(V/E) carrying one lifted point to the other. Let χ₀,χ_i,χ_U be the characters of z,w_i,w_U in μ_n. They satisfy χ₀=χ_U product_iχ_i.

At an unramified common E-point, equality in every auxiliary and U kills all these characters, hence χ₀(g)=1. At a point in the i-th branch pair, equality in the other auxiliaries and U again kills their characters; equality in B_i^aux only requires χ_i(g) to lie in its inertia group μ_{e_i}. This is exactly the inertia subgroup of the original cyclic n-cover at that point. Therefore χ₀(g) lies in the original inertia group, which means the two original C-images coincide. This treats ramified fibres without asserting that the coordinate maps jointly separate all points of V there.

## 5. Abelian covers

Let C/E be abelian of odd order G and genus at least two, and assume the skew-residue condition for every cyclic character quotient C_χ/E. Every ramified such quotient has genus at least two and is separated by Section4. An unramified quotient has genus one, and the Galois map C→C_χ is ramified by Riemann–Hurwitz; A.21 therefore forces equality of its images. A.21 applied to C/E gives a common E-image.

For a putative collision write Q=gP, with I=Stab_G(P). Equality in every cyclic character quotient says g belongs to I kerχ for everyχ. Characters of the finite abelian group G/I separate its elements, so the intersection of these subgroups is I. Hence g∈I and Q=P. This is valid at every branch fibre.

## 6. Low even-order branch differences for certain prime degrees

Let n=ell be prime, <2,−1>=(Z/ell)*, and let A have even order d≤ell−1. There is a unique P in the cyclic group generated by A satisfying ell P=−A, and it too has order d. In A.29j at least one nontrivial character arrow is zero. The set of zero indices is invariant under j↦ell−j, by its explicit even/odd formulas. The hypothesis on <2,−1> implies that all multiplication-by-two orbits on the nonzero residues are either one orbit or two interchanged by negation. Thus every orbit contains a zero arrow. The stable Cartier image is kω_E and the reflection quotient has p-rank zero by the same differential-vanishing argument as Section1.

Section2 proves A1 for this selected auxiliary. The residual-unramified-character construction of Section3 proves it for every other Picard-root choice with the same branch pair. No assertion is made that arbitrary branch differences can be brought into this class by an odd isogeny: their two-primary and odd-order components prevent that inference.

## 7. Descent and exact scope

All curves, roots, cyclic actions, and maps used are defined over finite extensions of the finite ground field. A.3 permits those extensions and the odd étale covers. To pass to a finitely generated field, first make a finite extension of that base field to define the action and the relevant maps, then spread and shrink so smoothness, ordinary E, the two-torsion section, branch opposition, and the tame cover data persist; A.8 applies. Open subcurves follow from the previously established proper-to-open reduction.

These results do not settle arbitrary characteristic-two ordinary elliptic quotients or arbitrary hyperelliptic curves. In particular, the odd-torsion branch cosets in A.29h do not become T₂-opposite pairs under an odd isogeny. A.29j's all-Picard-root ordinariness obstruction for those pairs remains intact. The new class uses a different ramification configuration.

## Exact supporting certificate

The standard-library program code/A_two_torsion_branch_certificate.py and its adjacent JSON output check127 odd degrees through255,724 doubling-orbit witnesses,16,256 partial branch coefficients,479 low-even-order prime cases, and127 odd Dickson polynomials. The residue calculation verifies both a_i(e_i+1)≡a_i modulo n and equality of the embedded auxiliary inertia with the original inertia. The Dickson identity is checked independently as a polynomial recurrence and its Laurent substitution. These finite checks support the universal proofs above; they are not used to extrapolate an unproved range.
