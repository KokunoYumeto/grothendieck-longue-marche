# Independent proof audit for E.74

Auditor: `/root/a_structure`. Outcome: **PASS for the stated source, cohomology, and fiber mechanism**, with the precise constructions below. This note audits the mathematical argument supplied by root; numerical matrix certificates are recorded separately by their executor.

## 1. Actual local source and splitting

Put k=Q3(zeta3), D=Gal(k(3)/k), and G=Gal(k(3)/Q3). Thus G is the actual relative pro-three-by-C2 quotient of the local absolute group. Its finite-order complement is asserted in this quotient, with its explicit map from the absolute group.

The actual localization map D -> P=G_{K,{3}}^(3), K=Q(zeta3), is onto. Otherwise its closed image lies in the inverse image of a maximal subgroup of a finite three-group quotient of P, hence in a subgroup of index three. The resulting cyclic cubic global extension is unramified outside three and has trivial local decomposition group at three. It is therefore unramified everywhere, contradicting Cl(K)=1. The local relative group consequently surjects onto Gamma=P semidirect C2.

Choose a lift of the specified involution c in the preimage of <c>. Coprime complement conjugacy supplies an actual order-two lift. Choose any lift of tau in D and put its conjugate lift at tau'=c tau c. The free property of P on tau,tau' gives a continuous section on P, equivariant for c. It extends to the actual splitting j:Gamma -> G. In particular, this argument does not assert an involution in the full absolute Galois group of Q3.

Let R=ker(G -> Gamma). It is pro-three, lies in D, and acts trivially on every geometric graded lattice A, since the given based geometric action factors through Gamma. With the chosen j, every element of G has the unique form r*j(g).

## 2. Full absolute versus maximal-pro-three cohomology

This comparison is required for H2, even though the coefficient action already factors through the relative quotient.

Let N be the kernel of G_k -> D. An invariant nonzero homomorphism N -> F3 would have normal kernel in G_k and would produce a further pro-three quotient of G_k, with central kernel F3 over D. Maximality excludes it. The five-term sequence therefore makes inflation H2(D,F3) -> H2(G_k,F3) injective. The actual Demushkin theorem gives dimension one on the left, and local Tate duality gives dimension one on the right because mu3 is contained in k. Thus this inflation is an isomorphism. H1 is the actual Kummer isomorphism, and both groups have vanishing cohomology in degrees greater than two.

Every finite three-primary module whose action factors through D has a finite composition series with trivial F3 factors: its finite acting quotient is a three-group. The long exact sequences and induction therefore give the comparison in every degree for every such finite module. Taking the exact C2-invariant functor gives the analogous comparison over Q3 and G, because two is a three-adic unit.

For the compact lattice A, the finite-coefficient cohomology groups are finite. Their inverse systems are Mittag--Leffler, so the derived-limit terms in passing from A/3^m to A vanish. This proves the integral continuous H1 and H2 comparisons used in E74, including their topologies. The argument does not infer H2 comparison merely from factorization of the representation.

## 3. Exact cocycle splitting and the local groups

Because R acts trivially on A, restriction of an A-valued cocycle to R is a continuous homomorphism theta:R-ab -> A, equivariant for Gamma. Conversely, for such theta and a Gamma-cocycle u, the formula

`a(r*j(g)) = theta(r) + u(g)`

is an actual continuous cocycle. Coboundaries restrict to zero on R and change precisely the Gamma component. Thus the chosen splitting j induces the exact integral topological direct sum

`H1(G,A) = H1(Gamma,A) direct-sum Hom_Gamma(R-ab,A)`.

E41 evaluates the first summand as `A/(T-1)A^c`, where T is the actual tau action and J is the c action. The second summand is torsion-free and finitely generated. A direct finite evaluation embedding proving this assertion is given below.

Local Tate duality identifies H2(G,A) with the compact coinvariants of A(-1). The actual cyclotomic character factors through Gamma. Since tau and c generate Gamma, these coinvariants are exactly

`coker [ T-7I | J+I ]`.

The image is compact and closed. The factors seven and minus one come from the actual cyclotomic values of those two generators; no residue-three Frobenius is being substituted for tau.

Write n=rank(A), c_plus=rank(A^c), and b=dim_Q3(A_Q3^*(1))^G. The known positive weights of the actual global Frobenius tau give H0(G,A_Q3)=0. Local Euler characteristic over Q3 then gives rank H1(G,A)=n+b. The Gamma summand has rank n-c_plus, so the extra summand has rank c_plus+b. All torsion is precisely the E41 torsion.

For degree one, b=5: the toric character module has two rational factors and three conjugate pairs, and the compact elliptic summand has no invariant Tate vectors. For degree two, the sole weight-two Tate factor is wedge2(T3E)=Z3(1), so b=1. In degrees at least three, the lowest occurring finite-field weight is greater than two; hence b=0. These arguments apply to the actual retained integral graded quotients, since their rational weight components are inherited by the exact quotient maps.

Every twisted stabilizer in a lower geometric quotient is zero. Its first nonzero graded coordinate would be fixed by the actual T matrix, because inner twisting acts trivially there. T has no eigenvalue one. Thus each nonempty central lifting fiber is the stated H1 group, with no further stabilizer quotient. This computes the fibers after existence; it does not assert that every lower class has zero obstruction.

## 4. A concrete local Kummer basis

Put lambda=1-zeta3, O=Z3[zeta3], and U_i=1+lambda^i O. The decomposition of the local multiplicative group gives

`k* = lambda^Z times mu2 times mu3 times U2`.

Indeed U1/U2 has order three and zeta3 is outside U2, so U1=mu3 times U2 with trivial intersection. The convergent logarithm and exponential identify U2 with lambda2 O. Cubing corresponds to multiplication by three, and `3*lambda2 O=lambda4 O` up to a unit.

For `u2=1+lambda2` and `u3=1+lambda3`, the logarithmic series give

`log(u2)=lambda2 mod lambda4`,

`log(u3)=lambda3 mod lambda4`.

All subsequent terms have the indicated higher valuation, including the denominator-three term. Thus lambda, zeta3, u2, u3 give an actual basis of `k*/k*3`. The first two are exactly the restrictions of the two global S-unit Kummer classes defining H1(P,F3).

It follows that the restrictions of kappa_u2 and kappa_u3 form a basis of

`H1(R,F3)^P = H1(D,F3)/H1(P,F3)`.

The equality follows from the split five-term sequence and H2(P,F3)=0. Choose actual elements r1,r2 of R dual to these two restricted characters. Equivalently they have the prescribed actions on the two cubic unit roots, while they lie in the actual kernel of D -> P.

These two elements normally generate R in D. Otherwise their closed normal closure has a nontrivial normal quotient. A nontrivial finite three-group image of that quotient has a nonzero invariant F3 character, by nilpotence of the augmentation ideal. This contradicts their spanning of the relative Frattini quotient. The choice is therefore a concrete pair of normal generators, specified by finite Kummer data inside the actual kernel. No Demushkin relator word has been assigned or evaluated by this choice.

## 5. Saturated evaluation coordinates for the extra factor

The chosen normal generators give the actual continuous surjection of compact modules

`Z3[[P]]^2 -> R-ab`,

with the two basis vectors sent to r1 and r2. Therefore evaluation gives an injective map

`E: Hom_Gamma(R-ab,A) -> A^2`,

`E(theta)=(theta(r1),theta(r2))`.

Its image is closed. Assigning arbitrary two values defines a continuous P-module map from the free compact module to A. The condition that it kill the actual relation submodule is a collection of closed integral linear equations. The additional c-equivariance condition is another collection of closed integral linear equations, using the actual c-action on R-ab. Their intersection is exactly the evaluation image.

The image is saturated over Z3. If three times a pair satisfies all these equations, the pair itself satisfies them because A is torsion-free. Hence it defines the required actual equivariant homomorphism. Repeating proves saturation for every power of three. Since A^2 is a finite free Z3-module, the closed saturated submodule is a direct summand and is free of the rank c_plus+b already proved.

Choose a unimodular Z3-coordinate map S on A^2 carrying this **actual saturated submodule** to the first d=c_plus+b coordinates. The extra coordinates of a cohomology class are then the first d entries of

`S(a(r1),a(r2))`.

Given these d entries, apply S inverse with zeros in the remaining coordinates. The resulting pair lies in the evaluation image and determines the unique equivariant homomorphism theta. The displayed cocycle formula reconstructs its class together with the independently chosen Gamma component. These are actual inverse maps.

This choice of S is a choice of coordinates for the actual closed submodule. It is **not a numerical computation of the unknown Demushkin quotient relation or of its Fox derivatives**. Computing S as a numerical matrix requires those additional actual relation-module data. The rank, torsion, direct-sum type, two-evaluation coordinate map, and its inverse are proved without pretending those data have been evaluated.

## Scope retained

The argument supplies the exact wild local central cohomology and all nonempty central fibers. The obstruction value for a specified nonabelian lower section still requires the actual central defect or the actual relation-module evaluation. The global coupled problem E23 is not declared solved by this local fiber computation.
