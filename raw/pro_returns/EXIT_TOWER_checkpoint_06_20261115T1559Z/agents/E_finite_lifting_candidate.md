# E.46 candidate for independent audit

This file contains an independently reconstructed proof of the finite counting lemma missing from the attached D.50 source, followed by its compactness consequence and the application to the designated LM7 E.58 element. It is a candidate under review, not yet an asserted result in the compiled register. Its proposed conclusion concerns **GT₀ only**. It does not claim that the element satisfies the pentagon or belongs to GT.

## 1. Exact finite lifting lemma

Let Λ be either the abstract free group on x₁,x₂, or the abstract free product C₂(s)*C₃(r). In both cases put x₃=(x₁x₂)⁻¹, with x₁=s,x₂=r in the second case. Fix an epimorphism q₀:Λ→E to a finite group, a normal subgroup A of E, D=E/A, and χ₀:Λ→D. Put Xᵢ=q₀(xᵢ) and Tᵢ={aXᵢa⁻¹:a∈A}.

There is a finite central extension p:D†→D and an epimorphism q₀†:Λ→D† with p q₀†=χ₀ having the following property. Given an epimorphism q₁†:Λ→D† and elements hᵢ†∈D† such that

q₁†(xᵢ)=hᵢ† q₀†(xᵢ)(hᵢ†)⁻¹  (i=1,2,3),

choose Hᵢ∈E with image p(hᵢ†), and set Tᵢ¹=HᵢTᵢHᵢ⁻¹. Then the numbers of epimorphisms qⱼ:Λ→E with qⱼ(xᵢ)∈Tᵢʲ (j=0,1; Tᵢ⁰=Tᵢ) are equal. In particular the second number is positive. Every such q₁ has conjugators cᵢ=Hᵢaᵢ, aᵢ∈A, so their D-coordinates are the prescribed p(hᵢ†).

No hypothesis [E,A]=A is required for this lemma.

### 1.1 The finite implementer extensions

For each J≤E which maps onto D and has Tᵢ∩J nonempty for all i, put M=J∩A and e=exp(J). For every irreducible complex representation ρ:M→GL(V) whose isomorphism class is invariant under conjugation by J, put d=dim(V) and define

J̃ρ={(g,T)∈J×GL(V): Tρ(m)T⁻¹=ρ(gmg⁻¹) for all m∈M, and (det T)^e=1}.

This is a group. For each g the implementer condition has a solution by invariance of ρ, and all its solutions are scalar multiples by Schur's lemma. The determinant condition leaves exactly de solutions, since it is c^(de)=a nonzero constant. Thus J̃ρ is finite, maps onto J, and has central kernel μ_de.

The map m↦(m,ρ(m)) embeds M as a normal subgroup of J̃ρ. It lies in J̃ρ because ρ(m)^e=I, and normality follows from the implementer identity. Its intersection with the scalar kernel is trivial, since its first coordinate would have to be 1. Define

Qρ=J̃ρ/{(m,ρ(m)):m∈M}.

Then 1→μ_de→Qρ→D→1 is exact and central. The map

J̃ρ→J×_D Qρ,  (g,T)↦(g,[(g,T)])

is an isomorphism. Indeed it is injective, and both finite groups have cardinality |J|de; equivalently one can multiply an arbitrary representative in Qρ by the graph of M to prescribe its J-coordinate. It gives an actual representation

Ψρ:J×_D Qρ→GL(V)

which restricts to ρ on M×{1}.

### 1.2 Auxiliary maps from the actual source

For a free source choose any lifts in Qρ of χ₀(x₁),χ₀(x₂), giving a homomorphism Rρ⁰:Λ→Qρ.

For the modular source choose a_s∈T₁∩J and a_r∈T₂∩J. Their orders divide 2 and 3 respectively. An implementer T_s has square scalar when a_s has order 2; rescale it to satisfy T_s²=I. Its determinant has order dividing 2 and hence e, so (a_s,T_s) lies in J̃ρ. If a_s=1 choose T_s=I. Similarly choose T_r³=I. The images of these pairs in Qρ satisfy the actual source relations s²=r³=1, and therefore define Rρ⁰:C₂*C₃→Qρ. In either source the third value is the inverse product of the first two; no independent choice for x₃ is made.

Take the joint image

D†=im(Λ→D×∏_(J,ρ) Qρ),

where the coordinates are χ₀ and all Rρ⁰. The first projection is onto D. Its kernel embeds in the finite product of scalar kernels and is central. The map to this actual joint image is q₀† and is onto by definition. This completes the construction with no abstract splitting of a central extension.

### 1.3 The exact pants count

Fix j=0 or 1 and a subgroup J≤E onto D. Write Cᵢʲ=Tᵢʲ∩J and Bᵢʲ=∑_(a∈Cᵢʲ) a in C[J]. Each Cᵢʲ is invariant under conjugation by M=J∩A, so Bᵢʲ commutes with C[M]. Each Cᵢʲ lies in the single quotient coset χⱼ(xᵢ), where χⱼ=pqⱼ†. Hence B₁ʲB₂ʲB₃ʲ belongs to C[M]. Its coefficient at 1 is precisely the number Hⱼ(J) of homomorphisms Λ→J with the indicated peripheral conditions. The torsion relations in the modular case are automatic because all members of C₁ʲ,C₂ʲ are E-conjugate to X₁,X₂.

Let eρ be a central primitive idempotent of C[M]. Every a∈Cᵢʲ has the same action on the irreducible classes of M. If this action moves [ρ], then Bᵢʲeρ=eρBᵢʲ and a eρ=e_(aρ) a imply eρBᵢʲ=0. Since χⱼ(x₁),χⱼ(x₂) generate D, a representation contributes to the product only if its class is invariant under all J. Thus precisely the representations used in 1.1 suffice for both j.

For such ρ let Rρʲ be the Qρ-coordinate of qⱼ† and define

Lᵢʲ=∑_(a∈Cᵢʲ) Ψρ(a,Rρʲ(xᵢ)).

This matrix commutes with ρ(M): conjugating a summand by ρ(m) replaces a by mam⁻¹ and leaves the Qρ-coordinate unchanged. By irreducibility it is scalar. Also

ρ(B₁ʲB₂ʲB₃ʲ)=L₁ʲL₂ʲL₃ʲ,

because the product of the Qρ-coordinates is Rρʲ(x₁x₂x₃)=1. Regular-character extraction of the coefficient of 1 therefore gives the exact identity

Hⱼ(J)=(1/|M|) ∑_(ρ invariant under J) (tr L₁ʲ)(tr L₂ʲ)(tr L₃ʲ)/dimρ.   (C1)

Indeed a scalar Lᵢʲ has scalar value tr(Lᵢʲ)/d; the contribution d·tr(L₁ʲL₂ʲL₃ʲ) to the regular character is their three traces divided by d. This verifies the factor 1/d directly.

### 1.4 Transport and epimorphisms

For each i choose jᵢ∈J over p(hᵢ†). Since jᵢ⁻¹Hᵢ∈A and Tᵢ is A-invariant,

Cᵢ¹=jᵢ Cᵢ⁰ jᵢ⁻¹.   (C2)

In particular emptiness matches, so omitted J contribute zero to both counts. Let hᵢρ be the Qρ-coordinate of hᵢ†. The pair (jᵢ,hᵢρ) belongs to J×_D Qρ, and the specified conjugator equality gives

Lᵢ¹=Ψρ(jᵢ,hᵢρ) Lᵢ⁰ Ψρ(jᵢ,hᵢρ)⁻¹.   (C3)

All three traces are unchanged. Equation (C1) proves H₀(J)=H₁(J). Subgroups J not mapping onto D have Hⱼ(J)=0, since χⱼ is onto. Thus equality holds for every subgroup J≤E.

Let Pⱼ(K) count the homomorphisms with exact image K. Then Hⱼ(J)=∑_(K≤J)Pⱼ(K). Finite-poset Möbius inversion proves P₀(E)=P₁(E). The reference q₀ is counted by P₀(E), so P₁(E)>0. Finally membership in HᵢTᵢHᵢ⁻¹ gives the conjugator Hᵢaᵢ with the specified D-value, as asserted.

## 2. Relative profinite lifting

Let Γ be the full profinite completion of either source above, let U be open normal, and let R be its closed nilpotent residual, the intersection of the kernels of all finite nilpotent quotients of U. Since R is characteristic in U it is normal in Γ. Put Γ_rel=Γ/R.

Suppose α is an automorphism of Γ_rel with specified positive peripheral conjugators b₁,b₂,b₃ there:

α(x̄ᵢ)=bᵢ x̄ᵢ bᵢ⁻¹.

Then there exists an automorphism Φ of Γ, with actual conjugators cᵢ lifting bᵢ, such that q_rel Φ=α q_rel. Here positive means the indicated generator itself, with exponent one; no claim with unprescribed powers is needed.

Work in the compact space Γ³ of conjugator triples. Impose (a) the peripheral product relation in every finite quotient, (b) generation of every finite quotient by the first two conjugated generators, and (c) the prescribed images of each cᵢ in every finite quotient of Γ_rel. These are closed conditions. A finite collection of them is contained in a single finite actual image q₀:Γ→E₀ which also retains Γ/U. Put U₀=q₀(U), A₀=γ_∞(U₀), D₀=E₀/A₀. Every old relative-coordinate quotient kills A₀, since its image of U is nilpotent.

Apply the finite lemma to E₀,A₀. In the resulting central extension D†→D₀, the image of U is a finite central extension of the nilpotent group U₀/A₀, hence is nilpotent. Thus its actual source map q₀† factors through Γ_rel. Precompose this factorization by α. The resulting q₁† is onto and has literal peripheral conjugators equal to the images of the specified bᵢ. The finite lemma supplies an epimorphism Γ→E₀ whose three conjugators have exactly those D₀-coordinates. Lifting these three conjugators to Γ meets the entire chosen finite collection.

Compactness gives one triple meeting all conditions. The source relations and peripheral product now hold in Γ, giving an endomorphism Φ. Its compact image surjects onto every finite quotient, so equals Γ. A finitely generated profinite group is Hopfian: preimage under a surjection acts injectively on the finite set of open subgroups of any fixed index, hence permutes it; every such subgroup consequently contains the kernel. Residual finiteness forces the kernel to be trivial. Thus Φ is an automorphism.

The coordinate equations on all finite quotients give q_rel Φ=α q_rel exactly. If b_k=1, then c_k∈R; conjugating Φ by c_k⁻¹ fixes that peripheral literally and leaves every retained relative conjugator coordinate unchanged.

This proof does not assume α fixes the chosen finite quotient Γ/U. The original auxiliary map factors through Γ_rel; precomposition is allowed to change its D₀-map, which is why the finite count was proved for both χ₀ and χ₁.

## 3. Exact relative local product

For every prime p let O^p(U) be the kernel of U→U^(p). The actual map

U/R→∏_p U^(p)

is an isomorphism. Its kernel is R by finite nilpotent Sylow decomposition. Every finite selection of prime-power quotient coordinates is jointly onto: Goursat's common quotient between groups of coprime orders is trivial. Compactness then proves surjectivity onto the infinite product. Consequently, for D=Γ/U,

Γ/R ≅ ∏_(p,D) Γ/O^p(U).   (C4)

To prove surjectivity explicitly, lift the common D-coordinate by one element of Γ; the discrepancy is a tuple in ∏U^(p), which the preceding isomorphism supplies. No extension splitting is used.

## 4. Application to the designated E.58 witness

Put Γ=B̂=C₂(s) amalg C₃(r), τ=sr, F=ker(Γ→S₃), x=τ⁻², y=sxs, and H=F′F³, with all subgroups closed. The six epimorphisms C₂*C₃→S₃ have one kernel (Aut(S₃) acts transitively), so F and H are characteristic. F is free profinite of rank two on x,y, and [Γ:H]=6·3²=54.

Use the actual projective quotient q:Γ→Q=SL₂(Z/12)/{±I} with

s↦[[0,1],[-1,0]],  r↦[[0,-1],[1,-1]].

The signed F-image is V₄×SL₂(F₃), of order 96, where V₄ is generated modulo four by U² and L². These two unipotents generate SL₂(F₃); its abelianization has order three, so it has no nontrivial common quotient with V₄. Goursat therefore gives the full product. The derived group of SL₂(F₃) is Q₈, as is checked from two quaternion generators and the index-three quotient. Hence

q(H)=V₄×Q₈,  |q(H)|=32.

The literal matrix word gives z₀=q([x,y]²)=[5I], a central element of order two. The joint source image

J=im(Γ→Q×Γ/H)=Q×_(Q/q(H))(Γ/H)

has order 32·54=1728. The element [x,y]²∈H gives (z₀,1)∈C_J(r). All these maps factor through Γ₂=Γ/O²(H), and ker(Γ₂→J) is pro-two.

If a finite-order element a has order prime to p, centralizers lift across a surjection with pro-p kernel K. Given a target centralizer element, choose a lift g; the subgroups generated by a and gag⁻¹ are complements to K in the inverse image of the common cyclic group. Finite Schur–Zassenhaus and compactness give u∈K with ugag⁻¹u⁻¹=a. The matching generator follows from their identical image. Thus ug is the prescribed centralizer lift.

Apply this with p=2,a=r to obtain c∈C_(Γ₂)(r)∩H^(2) mapping to (z₀,1). In (C4), take the identity automorphism of Γ/R_nil(H) and peripheral conjugators

b_s=1, b_τ=1, b_r=(c at p=2, 1 at all other primes).

The common Γ/H-coordinate is one and b_r centralizes r. Section 2 therefore supplies a full automorphism Φ of Γ retaining those conjugators. Normalize by its τ-conjugator in R_nil(H) so that Φ(τ)=τ literally. Its actual frames satisfy

Φ(s)=βsβ⁻¹, Φ(r)=ArA⁻¹, β∈R_nil(H), A∈H,
q(β)=1, q(A)=[5I], qΦ=q.   (C5)

Put f=sΦ(s). Since the relative action is the identity, f∈R_nil(H)⊂H′⊂F′. The actual free-product identities give

Φ(s)=sf, Φ(r)=f⁻¹r, Φ(x)=x, Φ(y)=f⁻¹yf.

Indeed conjugation by s interchanges x,y, and conjugation by r cyclically sends x→y→z→x, where z=(xy)⁻¹. Thus Φ(s)²=1 and Φ(r)³=1 give exactly

f(y,x)f(x,y)=1,
f(z,x)f(y,z)f(x,y)=1.

The characteristic subgroup F is preserved and its restriction is an automorphism. Hence (1,f) is an actual full GT₀ element.

The pure frames are unique: the discrete factor centralizers in C₂*C₃ are C₂ and C₃, and Boggi–Zalesskii Theorem A, applied to this virtually free group at p=2 and p=3, identifies their completed centralizers with the same finite factors. Both meet F trivially. Thus (C5) specifies actual full frames, not merely possible finite centralizer values.

Because β∈R_nil(H)⊂F′, its abelian frame coordinate ρ is zero. The normalized frames of E.24/E.65 are therefore T=q(A)⁻¹=[5I] and W=q(β)⁻¹=1, without a nonzero shear. In the signed lift T=5I is I modulo four and −I modulo three. Its sign on ker(R₀−I)=F₃(1,−1) is one, and W has order-two frame parity zero. Thus the designated element has the exact CM parity (1,0) and is rejected by the arithmetic CM test proved in E.24.

The conclusion is existence of the specified full gentle element and its genuine frames. The pentagon is not verified by this argument, and membership in GT is not claimed.

## 5. Audit requests

The points to check independently are: the finite implementer quotient and determinant restriction; the source maps retaining s²=r³=1; the factor 1/d in (C1); transport (C3) for arbitrary subgroup J; Möbius inversion; and the actual nilpotent factorization in the compactness argument. The finite matrix data already independently checked in E_CM_checks.py are supplemented by the elementary V₄×SL₂(F₃) and V₄×Q₈ derivations above.
