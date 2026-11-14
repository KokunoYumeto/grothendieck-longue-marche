# Independent review: the cross-ratio locus in an elliptic fourth power

**Outcome: the geometric hypotheses of the proposed prime-to-p torsion-density application hold for every odd characteristic, including p=3.** The conclusion below uses the prime-to-p torsion-density theorem in the precise form opened in Yang, RIMS-1844, Proposition 2.3. The A-section owner is independently checking its original primary citation. This review does not modify `sections/A.tex`.

## Statement checked

Let Ω be an algebraically closed field of odd characteristic, E/Ω an elliptic curve, and π:E→P¹ the quotient by negation. Let c∈Ω\{0,1}. Put homogeneous coordinates (X_i:Z_i) on the four copies of P¹ and write [ij]=X_i Z_j−X_j Z_i. Define

\[
H_c=V([13][24]-c[14][23])\subset(\mathbf P^1)^4.
\]

Let H_c^dist denote its open subset where all four coordinates are distinct, and let Z be the scheme-theoretic inverse image of H_c under π⁴:E⁴→(P¹)⁴. Then:

1. H_c is an integral effective Cartier divisor of multidegree (1,1,1,1).
2. Z is integral, equals the closure of (π⁴)⁻¹(H_c^dist), and is an ample effective Cartier divisor of E⁴.
3. Z is not contained in a translate of any proper abelian subvariety of E⁴.
4. When Ω=Fbar_p, the cited density theorem therefore gives a Zariski-dense set of tuples in Z whose four entries have order prime to p. Such a tuple can be chosen with pairwise distinct π-images and with no entry in E[2]. Its four entries are killed by one common integer n prime to p.

No part of the geometric proof uses p≠3.

## 1. The base hypersurface is integral

Choose an ordered quadruple (t₁,t₂,t₃,t₄) of distinct points on P¹ with the displayed cross-ratio c. The map

\[
\operatorname{PGL}_2\longrightarrow H_c^{\rm dist},\qquad
M\longmapsto (M(t_1),M(t_2),M(t_3),M(t_4))
\]

is an isomorphism: the first three distinct images determine a unique projective linear transformation, and invariance and completeness of the cross-ratio force the fourth. Thus H_c^dist is a smooth integral threefold.

A point of H_c with any two equal coordinates has at least three equal coordinates. For example, setting x₁=x₂ in an affine chart gives (1−c)(x₁−x₃)(x₁−x₄)=0, and setting x₁=x₃ gives −c(x₁−x₄)(x₂−x₁)=0. The other four pairs follow by the same direct substitution, with coefficients in {1,c,1−c}. The same calculation in a chart where the common value is finite covers coincidences at infinity after a simultaneous projective change of coordinates. Hence the complement of H_c^dist is a union of the four triple-diagonal surfaces, of dimension two.

The defining nonzero section has multidegree (1,1,1,1). Its zero scheme is an effective Cartier divisor on the smooth fourfold (P¹)⁴, so all its irreducible components have dimension three. Every component therefore meets H_c^dist. Since the latter is integral, there is only one component. That component has multiplicity one, because H_c^dist is smooth. A Cartier divisor on a regular scheme has no embedded associated primes; equivalently, its local rings are hypersurface Cohen–Macaulay rings. Generic reducedness and the absence of embedded primes imply reducedness. Thus H_c is integral as a scheme.

An affine irreducibility certificate is also available. Write

\[
F=(x_1-x_3)(x_2-x_4)-c(x_1-x_4)(x_2-x_3)=A x_4+B,
\]

where A=c x₂−x₁+(1−c)x₃. Reducing B modulo A yields c(1−c)(x₂−x₃)², which is nonzero in every characteristic under c≠0,1. Thus A and B have no common factor, and the polynomial linear in x₄ is irreducible. The homogeneous boundary introduces no divisor component, as the preceding diagonal argument shows.

## 2. Independent square classes and the entire finite-flat pullback

Choose a coordinate on P¹ in which Ω(E)=Ω(x)(√f(x)); the divisor of f has odd valuation precisely at the four branch points of π. Let K=Ω(PGL₂), identified with Ω(H_c). The generic algebra of Z over H_c is

\[
K\bigl(\sqrt{f(M(t_1))},\ldots,\sqrt{f(M(t_4))}\bigr).
\]

For each i choose any branch point b of π, and consider the evaluation divisor

\[
D_{i,b}=\{M\in\operatorname{PGL}_2:M(t_i)=b\}.
\]

Evaluation PGL₂→P¹ is smooth and surjective, with fibres cosets of a smooth connected Borel subgroup. Thus D_{i,b} is an irreducible divisor, and the valuation of f(M(t_i)) at its generic point is odd. For j≠i, evaluation M(t_j) is nonconstant on D_{i,b}; indeed, after fixing M(t_i)=b, the remaining stabilizer is transitive on P¹\{b}. Consequently f(M(t_j)) has valuation zero at the generic point of D_{i,b}. The four square classes are independent: any nonempty product involving the ith class has odd valuation at D_{i,b} and cannot be a square. Since the characteristic is odd, Kummer theory gives a field extension of degree 16.

This establishes more than irreducibility of a chosen component. The morphism π⁴ is finite flat of degree 16, since each π is a finite morphism between smooth curves and therefore flat. Its base change Z→H_c is finite flat. On any nonempty affine open of the integral scheme H_c, its algebra is a torsion-free module over a domain and hence injects into its generic algebra, which was just shown to be a field. The algebra is therefore a domain. Thus the entire scheme Z is integral and is the closure of its nonempty inverse image of H_c^dist.

## 3. Ampleness and exclusion of a proper abelian translate

Flat pullback preserves the effective Cartier divisor, and

\[
\mathcal O_{E^4}(Z)
\simeq \bigotimes_{i=1}^4 \operatorname{pr}_i^*\pi^*\mathcal O_{\mathbf P^1}(1).
\]

Each factor π*O(1) has degree two on E. Their external tensor product is ample, for example by the product/Segre criterion. Hence Z is ample.

Suppose Z⊂a+B for a proper abelian subvariety B⊂E⁴. Since dim Z=3 and dim E⁴=4, dimension forces dim B=3 and equality Z=a+B of the integral reduced subvarieties. The quotient q:E⁴→E⁴/B is an elliptic quotient, and this divisor is the inverse image of the point q(a). Therefore O(Z)=q*O(q(a)), whose restriction to every positive-dimensional fibre is trivial. This contradicts ampleness. Thus no such translate exists.

## 4. Exact density input and permitted open conditions

Yang's *Abelian Coverings of Curves over Fbar_p which are not New Ordinary*, RIMS-1844 (February 2016), Proposition 2.3, printed page 5, was opened at <https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1844.pdf>. It states that an irreducible reduced subvariety of an abelian variety over Fbar_p whose prime-to-p torsion points are not Zariski dense is contained in a translate of a proper abelian subvariety. Yang attributes this to Anderson–Indik through Tamagawa, printed page 704. The original source verification is being handled by the A-section owner; no unchecked stronger theorem is required by this review.

Applying that statement to the integral Z and the noncontainment just proved gives the required density. The open subset where the four π-images are distinct and avoid the four branch values is nonempty: on PGL₂ it is obtained by excluding finitely many evaluation divisors. Its inverse image in Z is likewise a nonempty open. A dense set of prime-to-p torsion tuples meets it. The least common multiple of their orders is still prime to p and kills all four entries.

## 5. Downstream connectedness correction

The common exponent n need not be odd. Therefore connectedness of the pullback of a ramified quadratic map g:D→E along [n]:E→E should not be justified by coprime degrees. Instead, the quadratic function-field extension Ω(D)/Ω(E) is ramified, whereas the Galois extension furnished by [n] is unramified. Their intersection cannot be the ramified quadratic extension and is therefore Ω(E). The pullback is connected for every n prime to p, regardless of its parity.

This correction was communicated to the A-section owner, who confirmed that the ramified-versus-étale argument is retained. The further step using two branch origins can choose a prime ℓ different from both 2 and p; their difference then has order ℓ and cannot be killed by 2. Thus that step does not impose p≠3 either.
