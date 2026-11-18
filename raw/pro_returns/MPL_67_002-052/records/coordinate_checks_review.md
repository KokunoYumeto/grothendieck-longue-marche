# Independent review of the explicit coordinate checks

**Reviewer:** /root/research_arithmetic.

**Review recorded:** 2026-11-18 01:23:55 UTC.

**Actual timestamps:** first review read at 2026-11-18 01:19:27 UTC; independent symbolic/exact calculation output at 2026-11-18 01:22:02 UTC; source hash read at 2026-11-18 01:22:24 UTC.

**Reviewed file:** records/research_checks.md, SHA-256 4918fdfdc401f9ef8caa3728d0de4a5afd2bcf3b21849015edcdbd6aa116054d.

**Requested scope:** C01, C02a–d, C05, C06, C07, C08. The verdict concerns their displayed maps, identities, normalizations, and source-to-source matrix dictionary. C03 and C04 are outside this review. No group-presentation proof or results-register theorem was rederived. No frozen file was edited.

## Verdict

All requested displayed calculations pass. No substantive correction is required. Twenty independent symbolic/exact checks returned True; the remaining orbit, covering-area, and quotient-map statements were checked by the explicit arguments below.

Two small clarifications improve precision without changing any formula:

- In C02b the zero expression involving A_p is the Hermitian cross-pairing of the lines of p and conjugate(p). It is not the positive quadratic value q_A(conjugate(p)). The expression printed in the file is correct.
- The coordinate changes and inverses in C02c and C06 use nonzero a,b. Writing a,b∈C× makes that domain explicit. In C08, “restriction to the holomorphic affine centralizer” means restriction of the descent homomorphism to that source subgroup; the negative-slope map descends through the quotient rather than preserving the upper half-plane upstairs.

## C01 — Reflection assignment and source dictionary: passed

Independent integer-matrix multiplication checked every involution square and determinant, r₁r₂=S, r₂r₃=R, S²=R³=−I, S⁴=R⁶=I, and

S⁻¹R = [[1,1],[0,1]].

The context was reread at context/LM_140-4_text.tex, §53, scan236, equations29–30. Its matrices are

A=[[-1,0],[0,1]], B=[[0,1],[1,0]], C=[[-1,1],[0,1]].

They give, by direct multiplication,

r₁=A, r₂=B, r₃=−ACA, C=−Ar₃A.

The minus sign in that conversion is necessary and is correctly retained. Equation30 also gives the useful more explicit comparison

σ_LM=AB=S, ρ_LM=BC=[[0,1],[-1,1]], R=Aρ_LM A.

Thus the ρ symbol in the cote67 assignment is mapped to R, while the source LM generator is related to it by the displayed conjugation. This is a complete matrix dictionary for the particular convention being checked; it does not certify a presentation.

The supplied checked note LM_P052 S01 already records the S,R calculation and presentation claim, as the reviewed file acknowledges.

## C02a — Global metric, normalization, and pullback: passed

Write A=[[a,u+iv],[u−iv,d]], with a,d,u,v real and A positive definite. The independently expanded polynomial is

q_A(x+iy)=a(x²+y²)+2ux+2vy+d.

This verifies the sign of the imaginary off-diagonal coefficient used by the later formulas. Scaling A by c>0 multiplies both det(A) and q_A² by c². Determinant-one normalization therefore gives the claimed unique matrix representative of a metric: the positive square root of the metric coefficient recovers q_A, and the displayed polynomial recovers the entries.

For the infinity chart z=1/w, with J=[[0,1],[1,0]], the exact identity is

q_A(1/w)=|w|⁻² q_{J*AJ}(w).

The factor |w|⁻⁴ in the denominator cancels the factor in |dz|². Since J*AJ remains positive definite, the expression in the w chart is smooth and positive at w=0.

For a nonsingular complex matrix M, let v=(z,1)ᵗ and d_M(z)=M₂₁z+M₂₂. The homogeneous identity

(f_M(z),1)ᵗ=Mv/d_M(z)

gives q_A(f_M(z))=q_{M*AM}(z)/|d_M(z)|². Together with f'_M=det(M)/d_M² and

det(M*AM)=|det M|² det A,

this proves f_M* g_A=g_{M*AM} exactly. The determinant transformation was also checked symbolically with four independent complex matrix entries.

For conjugation c(z)=conjugate(z), direct expansion gives

q_D(conjugate(z))=q_conjugate(D)(z)

for the Hermitian matrix D=M*AM. Since z↦f_M(conjugate(z)) is f_M∘c, its pullback is therefore g_conjugate(M*AM), as written. The order of the conjugation and matrix product in C02a is correct.

The factorization A=B*B gives the stated map g_A=f_B* g_I. Polar integration was checked independently:

Area(g_I)=2∫₀^∞ r/(1+r²)² dr=1.

The symbolic curvature calculation returned 4π from −Δ(log w)/(2w), with w=1/[π(1+x²+y²)²]. The hyperboloid matrix also has the asserted determinant t²−x²−y²−z². Its eigenvalues are t±sqrt(x²+y²+z²), so the displayed determinant-one equation with t>0 indeed lies in the positive cone.

## C02b — Fixed forms and A_p opposite poles: passed

### Rotation case

Conjugation of A by diag(−1,1) changes the signs of both off-diagonal entries. Its fixed forms are exactly the diagonal positive matrices. An arbitrary rotation matrix diag(e^{iθ},1) also fixes precisely those diagonal forms jointly over all θ.

For A=diag(a,d), the map f_B(z)=sqrt(a/d)z, with B=diag(sqrt(a),sqrt(d)), sends the metric to the standard round coordinate. The inverse image of its unit equator is |z|=sqrt(d/a), and its poles remain 0,∞. The stated positive-ray parameter is consequently correct.

### Conjugation case

The pullback by z↦conjugate(z) sends A to conjugate(A), so the fixed positive forms have v=0. With s real and t>0, the displayed matrix is

A_p=t⁻¹[[1,−s],[−s,s²+t²]], p=s+it.

Independent calculations give det(A_p)=1 and

B_p=t⁻¹/²[[1,−s],[0,t]], B_p*B_p=A_p.

The associated Möbius map is explicitly f_{B_p}(z)=(z−s)/t. It sends p to i and conjugate(p) to −i. Under the standard round stereographic map, those points have sphere coordinates (0,1,0) and (0,−1,0), hence are opposite poles. This supplies an actual map verifying the geometric assertion.

The printed pairing is also correct:

(conjugate(p),1) A_p (conjugate(p),1)ᵗ
= t⁻¹[(conjugate(p)−s)²+t²]=0.

Here the row is v_p* and the column is v_conjugate(p). Positivity of q_A is fully compatible with this cross-pairing.

Conversely, a determinant-one real-positive A supplies t=1/A₁₁>0 and s=−A₁₂/A₁₁. Substitution recovers all four entries; the lower-right entry follows from det A=1. The parameterization and inverse are therefore exact.

### Antipodal case

For h(z)=−1/conjugate(z), take M=S. Independent matrix multiplication gives

conjugate(S*AS)=[[d,−u−iv],[−u+iv,a]].

The fixed form equations are a=d and u=v=0. A fixed metric ray gives the same equations: this pullback preserves determinant, so a positive proportionality factor for a fixed ray has square one and is one. Thus there is exactly the one positive ray, with the one area-normalized metric, asserted in the reviewed calculation.

## C02c — Antiholomorphic compositions: passed

For a,b∈C×, the inverse maps are

s_a⁻¹(z)=conjugate(z)/conjugate(a),
t_b⁻¹(z)=conjugate(b)/conjugate(z).

Substitution gives s_a²(z)=|a|²z and t_b²(z)=(b/conjugate(b))z. Substitution of u_θ(z)=θz, |θ|=1, into the conjugation expressions yields θ⁻¹z for s_a and θz for t_b. The pole-fixing and pole-exchanging actions in C02c therefore have the stated order and signs.

## C02d — Cylinder, covering area, and scalar obstruction: passed

For z=e^{2πiw}, differentiation gives dz=2πiz dw. Consequently the descended flat metric is |dz|²/(4π²|z|²). On z=e^{iθ}, the length integral is ∫₀^{2π}dθ/(2π)=1.

The degree-two quotient is checked using area densities on evenly covered coordinate patches. Each downstairs patch has two isometric lifts under p* g_X=g_tildeX, hence the two integrals differ by the factor two. This argument also applies to an orientation-reversing deck involution because area is a positive density. The upstairs area-one normalization gives downstairs area one-half.

Integration of the asserted relation f* g=c_f g over the compact sphere forces c_f=1. For f(z)=2z, the pullback at the fixed point 0 is 4g(0), which conflicts with the required equality and positivity. This checks the stated concrete obstruction.

## C05 — Peripheral-marking example: passed

The free-word substitutions were checked independently, with cancellation:

φ(a)=ab, φ(b)=b; ψ(a)=ab⁻¹, ψ(b)=b.

Both ψφ and φψ fix a and b. For a chosen pants spine with inclusion j and deformation retraction r, the actual self-map is jφr; jψr is its homotopy inverse, by rj=id and jr homotopic to the identity.

The third peripheral word (ab)⁻¹ maps to (ab²)⁻¹. The independent word output was b⁻¹b⁻¹a⁻¹, with exponent sums (−1,−2). Those sums differ from every listed vector ±(1,0), ±(0,1), ±(1,1). Conjugation preserves exponent sums, so the claimed peripheral obstruction is verified by this explicit map.

## C06 — Normal tensor and polar product: passed

Multiplication of x=r_xζ_x and y=r_yζ_y directly gives

xy=(r_xr_y)(ζ_xζ_y).

This verifies the written map on the product of polar-coordinate spaces, including its extended nonnegative radial variables. The retrieved Nakayama–Ogus example was already checked at publisher pp2189–2190 in records/context_arithmetic.md.

For fixed a,b∈C×, the coordinate changes x'=ax and y'=by give t'=ab t and tangent coordinate bases ∂_{x'}=a⁻¹∂_x, ∂_{y'}=b⁻¹∂_y. The factors cancel exactly in

t'∂_{x'}⊗∂_{y'}=t∂_x⊗∂_y.

The verdict certifies this local coordinate comparison only. The reviewed text correctly leaves the global arithmetic construction and Galois comparison outside that calculation.

## C07 — Borel stabilizer and reduction: passed

For g=[[a,b],[c,d]]∈SL₂(Z), its first column represents g[1:0]. Stabilizing [1:0] requires c=0, and ad=1 in the integers gives a=d=1 or a=d=−1. The resulting matrices are exactly ±[[1,n],[0,1]].

A rational line admits a primitive integral column (p,q)ᵗ. The displayed Bézout equation ps−qr=1 gives a matrix [[p,r],[q,s]] of determinant one, establishing surjectivity of the orbit map. Two such matrices with the same rational line differ on the right by the computed stabilizer, proving that its fibres are the stated right cosets.

Two primitive integral columns for one rational line differ by sign. Their reductions modulo two are equal and nonzero. Thus the map to P¹(F₂) is well defined, including the sign choice. This directly verifies the quotient and reduction asserted in C07.

## C08 — Half-plane quotient and the two sources: passed

The fibres of q(x+iy)=x+i|y| are exactly conjugation orbits. For an affine holomorphic map h(z)=az+b, the equality h∘c=c∘h compares a with conjugate(a) and b with conjugate(b), forcing a,b real, a≠0. The same coefficient comparison applies to h(z)=a conjugate(z)+b.

For either of these two actual maps, direct computation gives

q∘h=F_{a,b}∘q,
F_{a,b}(x+iy)=ax+b+i|a|y, y≥0.

At a>0 this is az+b on the upper half-plane. At a<0 it is a conjugate(z)+b there. The group law is

F_{a,b}∘F_{a',b'}=F_{aa',ab'+b}.

The identity element is F_{1,0}; its inverse formula is F_{a⁻¹,−b/a}. The identity fibre of the full source therefore consists exactly of the two lifts z and conjugate(z). The holomorphic source has only the first lift, and already maps onto every F_{a,b}. This explicitly verifies the isomorphism from the holomorphic centralizer and the same isomorphism from the quotient of the full centralizer by {1,c}.

The frozen scan043 was read only, to confirm its specified closed half-plane and “groupe affine réel” wording. The review establishes the concrete descent maps written in C08; it does not add a classification theorem about larger automorphism categories.

## Independent execution summary

The 20 symbolic/exact assertions returned True:

1. Reflection involution squares.
2. Reflection determinants.
3. The two reflection products.
4. The central powers and finite orders displayed.
5. The central-sign conversion and its inverse.
6. The LM-to-cote67 modular-generator dictionary.
7. S⁻¹R.
8. The real-coordinate polynomial q_A.
9. Antiholomorphic conjugation of a Hermitian form.
10. The antipodal pullback matrix.
11. Curvature 4π.
12. Area 1.
13. det(A_p)=1.
14. B_p*B_p=A_p.
15. The opposite-line cross-pairing.
16. The images p↦i and conjugate(p)↦−i.
17. The Lorentz determinant.
18. The general determinant transformation under M*AM.
19. The graph-map inverse substitutions.
20. The peripheral exponent-sum obstruction.

The covering-area, tensor, orbit-stabilizer, and half-plane descent arguments were verified directly above. No false assertion or omitted central sign was found within the requested scope.
