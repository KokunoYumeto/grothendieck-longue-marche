# Post-freeze mathematical checks

These checks concern editorial examples only. The transcription, images and notation were not delegated; the independent checker received the abstract definitions and examples after the transcription freeze and did not inspect source files. The primary reader reviewed the returned arguments before incorporating them in the notes. No novelty is claimed.

## Common-partition obstruction (N097-02–03)

For k=Q and distinct a_m, define f_n on A1 by the finite partition into the first n rational points and their complement, with coordinate m the indicator of a_m. The field-valued maps are natural under field extensions. A stratum containing the generic point of the integral affine line is a nonempty open, hence contains all but finitely many a_m. Every coordinate of a scheme morphism on that stratum vanishes in the function field, and therefore vanishes on the stratum. This contradicts the required indicator value at any a_m in it.

The example tests the canonical limit cone in the category of finite piecewise maps; it does not refute commutation of underlying field-valued functors with limits, nor prove that no other object could be a categorical limit. The infinite-dimensional affine limit is allowed by the manuscript's quasi-compact quasi-separated object condition.

If one finite partition works for all stage maps, ordinary scheme limits on the reduced pieces supply the desired map. Compatibility on atomic points implies compatibility of the scheme morphisms from those reduced pieces.

## Square-zero test (N093-02)

For R=k⊕M, M²=0, maps to fields kill M. A finite set of algebra generators spans only a finite-dimensional subspace of M, since multiplication of two elements of M vanishes. If M is infinite-dimensional, R is neither a finite-type k-algebra nor noetherian; its spectrum is nevertheless one point and hence topologically noetherian.

## Reduced object test (N093-03)

Let C=k[x,y], B=k+xC, J=xC. Then B is a subring of a domain and is reduced. The ideal J is maximal, B/J=k, and J²=x²C is contained in xB=kx+x²C; hence rad(xB)=J. Localizing at x gives B[1/x]=C[1/x], since y=(xy)/x.

The two reduced strata are Spec C[1/x] and Spec k. Their disjoint union is an affine noetherian finite-type k-scheme, constructibly isomorphic to Spec B. But J/J² is the k-vector space spanned by x,xy,xy²,..., so it is infinite-dimensional. A finitely generated ideal J would give a finite-dimensional J/J²; thus B is nonnoetherian.

## Reduced morphism test (N093-05)

Let A=k+x²C⊂B=k+xC. Put J_A=x²C and J_B=xC. We have A/J_A=B/J_B=k, J_A²=x⁴C⊂(x²)_A, and J_B³=x³C⊂(x²)_B=kx²+x³C. Therefore the radicals of the principal ideals (x²) are respectively J_A and J_B. Both localizations at x² equal C[1/x]: in A[1/x²], x=x³/x², y=x²y/x², and then 1/x=x/x².

The induced map Spec B→Spec A is an isomorphism on the open strata and the closed reduced point strata. The extended ideal J_AB equals x²C, and B/J_AB=k⊕xk[y] with square-zero infinite-dimensional second summand. Finite type of B over A would survive this quotient and make that square-zero algebra finite type over k, contradicting the preceding elementary calculation.

The closed supports are principal constructible closed sets; their reduced defining ideals are not finitely generated. These examples therefore apply to the stated reduced-stratum convention, but not automatically to a modified convention requiring the reduced immersions themselves to be finitely presented. The reduced morphism example has a nonnoetherian target and does not decide a noetherian-target version.

## Split-base open-cover test (N077-03)

For S'=S⊔S, the restriction of X_1⊔X_2 with X_i over the corresponding component is X_1×_S X_2. Restricting a single open component gives the empty scheme, since a map from T⊔T over S' cannot map the nonempty second component into the empty fibre. For X_i=A1_S and S nonempty, the images of the two-component cover therefore do not cover the product.

The failure concerns the covering family. Applying restriction to the isomorphism ⨿U_i→X still gives an isomorphism; it is not the same operation as taking ⨿Res(U_i).

## Printed tensor-reciprocity test (N090-01)

Over Q, H=diag(1,0), E=E12 satisfy HE−EH=E, defining a representation of [h,e]=e. Its first basis vector gives the weight-one character as a submodule. The dual representation has H*=-H^t and E*=-E^t; tensoring with the weight-one character gives diag(0,1) and -E21. Their common kernel is zero, so the trivial module does not embed.

Tensor–dual adjunction identifies Hom(M1,M2⊗N) with Hom(M1⊗N*,M2). Simplicity converts nonzero maps in the first group to injections and in the second to surjections; it does not convert the latter surjections to injections without further hypotheses.

## Other direct tests

N088-01 uses π(0)=0. N088-02 uses a one-dimensional trivial representation, β(e,e)=1 and f(e)=1: the orthonormal condition β(x',x')=1 allows x'=e independently of whether the chosen original basis is e or 2e, producing e and 2e from the printed expression.

N077-02 distinguishes the ordinary topological product from a fibre product over S. For the two-point identity map X=S, singleton opens cover X×_S X but do not contain the two-point subset. The stronger finite-subfamily statement can instead be proved using quasi-compactness of the finite ordinary topological product.

