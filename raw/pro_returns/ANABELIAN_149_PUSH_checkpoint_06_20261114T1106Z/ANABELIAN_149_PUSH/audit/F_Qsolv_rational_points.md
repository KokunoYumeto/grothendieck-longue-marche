# Qsolv: punctured-line Kummer integrality and reconstruction of point functions

Status: independently reviewed by root and promoted as F.18–F.19 (Proved). It does **not** claim equality of full-topos morphisms in the nonconstant case.

Put k=Qsolv. Use F.16's proved D(E*)=k* for every finite E/k and its fixed-number-field radical descent calculation.

## 1. Unbounded finite degrees, without a circular Kummer-line claim

There is a proper finite extension of k: the splitting field of T^5−6T+3 retains its A5 Galois group after compositing with k. If E/k is any proper finite extension, choose a∈E\k. Since D(E*)=k*, some n-th root of a does not belong to E. Adjoining that root gives a proper finite extension E'/E. Repeating gives degrees at least doubling. This can start above any prescribed finite L/k; if L=k first take the displayed A5 extension. The primitive-element theorem gives algebraic points of arbitrarily large degree over L. In particular every finite L/k admits a proper finite extension.

## 2. Integral Kummer classes on punctured rational lines over every finite L/k

Let L/k be finite and U⊂Gm,L a nonempty open. Write

    O(U)* = L* × ∏_{j=0}^r P_j(t)^Z,

where P_0=t and P_1,…,P_r are distinct monic irreducible polynomials for the removed closed points. They are squarefree and pairwise coprime. Let ξ∈lim_n H1(U,μ_n), and assume every evaluation at every point over every finite E/L is the compatible Kummer class of an actual b_x∈E*. Then ξ is represented by an actual unit h∈O(U)*, and b_x/h(x)∈k* at every such point.

Proof. Pic(U)=0. Choose x0∈U(L), with evaluation b0∈L*. For λ_j∈Zhat, write the class as

    ξ = κ_L(b0) + ∑_j λ_j([P_j(t)]−[P_j(x0)]).

Choose a proper finite extension L'/L as in §1, and a finite Galois number field M/Q containing generators of L and L' over k, all coefficients and roots of the P_j, and x0,b0. Then L'⊂Mk, so choose a nonidentity σ∈Gal(Mk/L). It restricts to an automorphism of M, fixes every coefficient P_j and x0,b0, and need not fix their roots.

Choose distinct good rational primes p_i, one per polynomial, splitting completely in M. Exclude coefficient denominators, all discriminants/resultants, and primes at most ∑deg(P_j). There are infinitely many such primes. One may use the elementary split-prime argument: for a primitive integral element of the finite Galois field M, infinitely many primes divide values of its nonconstant minimal polynomial (Schur's argument); outside finitely many index/discriminant primes, a degree-one prime in a Galois extension forces total splitting. Schur's argument itself is elementary: if only p_1,…,p_s divided nonzero polynomial values, choose f(a)≠0 and evaluate f(a+f(a)p_1⋯p_s T)/f(a), a nonconstant integer polynomial congruent to 1 modulo every p_i, at an integer with absolute value greater than 1.

For each i choose a place v_i|p_i of M and a root r_i∈M of P_i. Since p_i splits completely and σ is nonidentity, v_i and σ⁻¹v_i are distinct. Across different i the rational primes differ. In O_M with the finitely many coefficient denominators inverted, CRT supplies α satisfying

    α ≡ r_i+p_i mod v_i²,
    α ≡ c_i mod σ⁻¹v_i,

where c_i∈F_{p_i} avoids the roots of every P_j. Taylor expansion at the simple root gives

    v_i(P_j(α))=δ_ij,
    v_i(P_j(σα))=v_{σ⁻¹v_i}(P_j(α))=0.

The second equality uses that σ fixes the coefficients, not the roots. Thus r'_j=P_j(σα)/P_j(α) satisfies v_i(r'_j)=−δ_ij, and α∈U(Mk).

Let b_α∈Mk realize the evaluation. Put it in one fixed number field F=MS, where S⊂k is finite and contains B=M∩k. For integer representatives a_{j,n} of λ_j modulo n, the Kummer evaluation gives a root z_n∈Mk of

    (b_α/b0) ∏_j(P_j(α)/P_j(x0))^(−a_{j,n}) = z_n^n.

Apply the F.16 radical descent with σ. Since σ fixes b0 and P_j(x0), it gives

    (σb_α/b_α) ∏_j(r'_j)^(−a_{j,n}) ∈ (F*)^n.

The integer-valued characters h_i=v_i∘Norm_{F/M} satisfy h_i(r'_j)=−[F:M]δ_ij. Therefore

    [F:M] λ_i = −h_i(σb_α/b_α) ∈ Z.

A rational element of Zhat is an integer, so every λ_i is integral. The initial expression for ξ is now the Kummer class of

    h(t)=b0 ∏_j(P_j(t)/P_j(x0))^λ_j ∈ O(U)*.

At every finite-extension point the quotient of the actual value by h(x) has zero Kummer class; F.16 makes that quotient lie in k*. This proves the lemma.

## 3. Nonconstant pinned Gm endomorphisms have nonzero integer exponent

Let φ:(Gm,k)_et→(Gm,k)_et be closed-point preserving and relative, and let f denote its Qbar-point function. F.16 gives φ*[t]=m[t], m∈Z, and f(α)=c_α α^m with c_α∈k*.

If m=0, all point values lie in k. Choose β∉k and put L=kβ. After base change, the inverse image of the closed point β is a closed subset with no closed point. Every nonempty closed subset of Gm_L has a closed point, so this inverse image is empty (the generic point cannot be an isolated exception), and φ_L factors through Gm,L minus {β}. Pull back the unit t−β. Apply §2 on all Gm,L to get a unit h_β(t)=a t^r, a∈L*, r∈Z, satisfying

    f(α)−β = d_α a α^r,   d_α∈k*.

The left side belongs to L for every α. If r≠0, choose α with [L(α):L]>|r| using §1. The displayed equality would put α^r in L, a contradiction. Thus r=0. Comparing α with 1 gives

    (f(α)−β)/(f(1)−β) ∈ k*.

Since f(α),f(1)∈k and β∉k, this forces f(α)=f(1). All closed points have the same image. The generic point cannot have a different image: otherwise the inverse image of the target open complement of that closed image would be the singleton generic point, which is not open in Gm. Hence the entire point map is constant. By the closed-subtopos factorization, φ factors through that rational point; relativity over BG_k makes it the usual algebraic constant map.

This proves that a nonconstant pinned endomorphism has m≠0, without assuming a section-conjecture statement.

## 4. The entire point function is an algebraic monomial

Assume m≠0. For each b∈k*, the inverse image of the target point b is a proper closed subset of Gm, hence finite. Call its complement U_b. Pull back t−b and apply §2 to obtain h_b∈O(U_b)* and

    f(α)−b=d_{α,b}h_b(α),   d_{α,b}∈k*,  α∈U_b(Qbar).

For b=1, combine this with f(α)=c_α α^m. After clearing denominators, the rational function

    c_α t^m−d_{α,1}h_1(t)−1

has numerator degree bounded independently of α. Choose α outside the finite exceptional fibre and of degree over k exceeding this bound. Its vanishing at α forces an identity of rational functions. Thus h_1(t)=A t^m+B, with A,B∈k*.

For every α∉k, radical closure gives α^m∉k; moreover such α cannot lie in the fibre f(α)=1. Comparing coefficients of 1 and α^m gives

    c_α=−A/B=:c,    f(α)=c α^m.

Now apply the same bounded-degree argument to an arbitrary b∈k*: at sufficiently high-degree α the already known formula f(α)=cα^m implies

    h_b(t)=e_b(c t^m−b),   e_b∈k*.

This rational function is a regular unit on U_b. Therefore every zero of c t^m−b in Gm lies in the removed fibre f⁻¹(b). For x∈k*, choose b=cx^m. Its zero at x forces f(x)=b. Consequently

    f(α)=cα^m  for every α∈Qbar*.

## 5. Scope of the point calculation and subsequent completion

The argument above proves the base point function of every pinned Gm endomorphism is an algebraic monomial and proves the full morphism is the algebraic constant map when m=0. This calculation alone does not identify a nonconstant φ with the geometric morphism induced by c t^m. CHW's reconstruction-from-points proposition requires algebraic point realizations after every separated quasicompact étale target chart. Such pullback charts include curves of arbitrary genus, whereas the calculation above uses Pic(U)=0 on rational U.

That obstacle is subsequently overcome by the independent arguments now integrated as F.20–F.23. F.20 detects all finite arithmetic quotients by closed-point decomposition groups using the common-constant wreath construction and Hilbert specialization over a number field. F.21 applies it to the joint image of the two pullback maps and uses compactness of geometric conjugators to identify their generic functors. F.22 then identifies the full small-topos morphisms by finite normalizations, maximal étale loci, and their sliced open subobjects; it explicitly handles partly ramified charts. F.23 therefore proves the full corrected Qsolv Gm endomorphism theorem. The precise proofs and independent review are in sections/F.tex and audit/F_full_topos_independent_review.md. No all-scheme field classification follows from this rational-source argument.
