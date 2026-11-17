# The exact square-filled class-two fiber, its center, and the marked regular-cusp embedding

Source-ready proof developed and independently reviewed in the conversation during the execution-environment outage. No filesystem write, producer execution, or formal promotion was claimed at that stage.

## Statement

Fix an odd integer n>1. In A102, N_n=ker(F(P,A,C)→C_n) is the free retained fiber, whereas K_n=N_n⋊B_n is the entire kernel of G→C_n×D_(2n). Let U_n be the quotient of the actual G_(n,rel) by the COMPLETE closed normal family Γ3(N_n^(2)), a²,c²,d²,f². Let I_n be the image of N_n^(2), not the image of all K_n. Put R_n=F2[C_n], M=R_n A⊕R_n C and V=F2 p⊕M. Let H be the universal class-two pro-two group on p and the involutions A_i,C_i (0≤i<n). Let Q=C_n×D_(2n) act on V by fixing p, shifting M by T, and by D(a,c)=(a,c+(1+T^-1)a), F(a,c)=(a+(1+T)c,c). Define J to be the FULL F2[Q]-span in Λ²M of

r_d,i=C_(i-1)∧A_i+C_(i-1)∧C_i+A_i∧C_i,

r_f,i=A_i∧C_i+A_i∧A_(i+1)+C_i∧A_(i+1).

Then I_n is isomorphic, as an actual compact pro-two group, to Hbar=H/J. Its derived group is elementary abelian of rank n²+n+1; Z(Hbar)=Φ(Hbar)=<p²>×[Hbar,Hbar]; and Hbar/<p⁴> has order 2^(n²+3n+3).

For the ACTUAL regular pair A,S=CP, the elements q=S^n and x_i=S^i A S^-i embed the universal class-two pro-two group on q and n involutions x_i into I_n. This is an intrinsic pro-two topology/actual compact embedding statement, not a full-profinite-topology claim about an underlying discrete group. The original full-GT alpha acts on U_n. Its center values and the canonical H_d remain unevaluated.

## 1. Universal normal form

H has exact Hall forms p^z times the ordered core bits times independent central basic-commutator bits, z∈Z2 and all other coordinates in F2. An explicit associative multiplication adds the coordinates and the bilinear inversion-count terms; the p exponent is reduced modulo two only inside those bilinear terms. This proves independence, not merely generation. Thus [H,H]=Λ²V=(p∧M)⊕Λ²M, all these commutators have order two, and p is primitive with p² central.

## 2. The complete wrap

Define σ to fix p and shift each core, with σ(A_(n-1))=p A_0 p^-1 and the analogous C formula. The backward shift with the inverse p correction is its inverse, and σ^n=Inn(p). On the center σ is the simultaneous cyclic shift, hence preserves J. Since n is odd, σ'=Inn(p^(-1/n))σ has order dividing n. Set Nstar=Hbar⋊C_n(t), Ad(t)=σ', P=p^(1/n)t. Then P^n=p and Ad(P)=σ, so every integer identity A_(i+n)=p A_i p^-1 and C_(i+n)=p C_i p^-1 is retained.

## 3. Actual automorphisms, including offsets

Define

D(P)=C_0 P C_0, D(A_0)=C_0 C_-1 A_0, D(C_0)=C_0;

F(P)=A_0 P A_0, F(A_0)=A_0, F(C_0)=C_0 A_1 A_0.

Their full integer rows are D(p)=C_0 p C_0, D(A_i)=C_0 C_(i-1) A_i C_i C_0, D(C_i)=C_0 C_i C_0; F(p)=A_0 p A_0, F(A_i)=A_0 A_i A_0, F(C_i)=A_0 A_i C_i A_(i+1) A_0. The square defects are EXACTLY r_d,i and r_f,i: outer conjugation can be removed, and every wrap contributes a central order-two commutator whose contribution to a square is zero. On central commutators the induced map is the exterior-square H1 action, so the whole J is preserved. This does not discard the offsets in the generator words. P compatibility follows by conjugating the image of A_0/C_0 by D(P)^i/F(P)^i, including i+n; the nth-power equation gives D(p)/F(p). The odd powers of p are conjugated likewise, so D(t)=C_0 t C_0 and F(t)=A_0 t A_0. D fixes C_0 and PA_0 and conjugates P by C_0; hence D²=1. F fixes A_0 and C_0P, hence F²=1. These are the six original marked actions, and all four actual squares hold.

## 4. A genuine target and the inverse map

Gamma=<D,F> is finite, faithfully detected on Nstar/<p⁴>. Indeed D/F fix p²; any composite sends p to p times a central order-two word, each core to a finite p-exponent-zero word, and t to h t with h of p exponent zero. The latter finite subgroup embeds modulo p⁴, so identity on that finite quotient forces identity on every actual generator. The action on V has exact dihedral image D_(2n): over the square-free R_n, FD has roots ρ,ρ^-1 on every ρ≠1 factor and is I at ρ=1; a primitive nth root gives order exactly n. F is a nontrivial involution, so it is outside the odd-order rotation subgroup. Gamma→D_(2n) has two-group kernel by the finite Frattini automorphism kernel on Hbar/<p⁴>, followed by the restriction kernel Der(C_n,Z(Hbar/<p⁴>)).

Therefore Gstar=Nstar⋊Gamma is a genuine quotient of the original marked G over its actual C_n×D_(2n) head, with pro-two kernel Hbar⋊ker(Gamma→D_(2n)). It factors G_(n,rel), the full square family and Γ3. Conversely I_n is compact class two with involutory cores, so H→I_n is onto. Its actual d/f/P translates kill all J, giving Hbar→I_n onto. The Gstar target gives I_n→Hbar and fixes every p,A_i,C_i. The two maps are inverse continuous maps. This proves the precise fiber equality; it does not identify the entire finite-head kernel with Hbar or erase (fd)^n.

## 5. Exact dimension, without enumeration

The universal quadratic map q0 on M, with q0(e_i)=0 on the original core basis, satisfies q0(gv)=Λ²g q0(v)+Σ v_i q0(g e_i). Hence the full orbit span J is exactly the span of all core-orbit defects. Its annihilator consists of quadratic forms q with polar B that vanish on every core orbit.

Write M=F2α⊕F2γ⊕X⊕Y, α=Σ A_i, γ=Σ C_i. On the augmentation part use x=a+c, y=a+T c; T+1 is invertible there. F swaps x,y and D(x,y)=(T^-1 y,T x). The global shift and FD independently shift X and Y because n is odd. Thus the two COMPLETE core orbits are α+u_i+v_j and γ+u_i+v_j; Σ u_i=Σ v_j=0 are their sole linear relations.

Rectangle differences force B(X,Y)=0, since the differences u_i+u_i' span X and likewise Y. Set ℓ_X=B(α,-)|X and ℓ_Y analogously. Vanishing on α+u_i+v_j forces q(u_i)=ℓ_X(u_i)+Ω_X, q(v_j)=ℓ_Y(v_j)+Ω_Y, where Ω_X=Σ_(i<j)B_XX(u_i,u_j), similarly Ω_Y; the sole simplex relation and odd n force exactly these constants. Comparing the γ orbit gives B(α+γ,X⊕Y)=0 and q(α)=q(γ)=Ω_X+Ω_Y. B(α,γ) is free. Conversely arbitrary B_XX,B_YY,ℓ_X,ℓ_Y,B(α,γ) with these formulas define a unique quadratic form and kill every orbit vector. Therefore dim(Λ²M/J)=2*C(n-1,2)+2(n-1)+1=n²-n+1, dim J=n²-1, and the full derived rank is 2n+n²-n+1=n²+n+1.

The radical of the commutator pairing on V is zero: pairing p with a nonzero M component detects its independent p∧M coordinate, and a remaining nonzero p component pairs nontrivially with a core. Thus Z=Φ=<p²>×derived. The Hall form gives |Hbar/<p⁴>|=4·2^(2n)·2^(n²+n+1)=2^(n²+3n+3).

## 6. The whole marked regular fiber

Restriction of those dual forms to Aspace=F2α⊕I_A is onto the full alternating-form space: its linear part is arbitrary ℓ_X+ℓ_Y, and its augmentation alternating part is arbitrary B_XX+B_YY. Consequently Λ²Aspace→Λ²M/J is injective. For S=CP, q=S^n has H1 vector p+γ and primitive p exponent one; x_i=S^i A S^-i has vector A_i. Their wedge map is injective: x_i∧x_j remain independent, while q∧x_i=p∧A_i+γ∧A_i have distinct independent p components. In a possible Hall kernel, the p exponent first forces the q exponent zero, the independent A_i H1 coordinates force every core bit zero, and the injected wedge coordinates force every central bit zero. This proves the continuous compact embedding of the universal regular class-two pro-two fiber.

## 7. Original action and limit

A102 preserves N_n^(2) under the original alpha, and Γ3 is characteristic. The actual full-GT peripheral property sends each standard pair twist a,c,d,f to a conjugate of its inverse, so their COMPLETE square normal closure is alpha invariant. Thus alpha acts on U_n and its exact fiber, with full h0 retained. This does not specify its action on the central module, evaluate the actual canonical H_d, or identify a CM frame. No finite census, orbit cutoff, private build, formal promotion or saved-artifact claim accompanies the original in-context proof.
