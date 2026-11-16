# Middle cusp range: an exact literal boundary computation

Notes only, 2026-11-16. This is a boundary-module calculation, not a classification of the entire arithmetic restriction kernel.

Let R_n=Z_5[C_(5^n)], q_n=t^(5^n)-1 and J_(r,N)=ker(R_N→R_r). Assume 0≤r<m<N and put h=m-r, d=N-m. The action of Γ=Z_5^× is the actual permutation action t^a↦t^(χa). Then

    (J_(r,N)/q_m J_(r,N))_Γ
      ≅ Z_5^h ⊕ ⊕_(k=1)^r Z/5^(h+min(d,k)).

The splitting of the free quotient is noncanonical. Each torsion factor displayed is a single cyclic factor; the two layers must not be split separately. In particular (r,m,N)=(1,2,3) gives Z_5⊕Z/25.

## Actual affine action and the exact homology sequence

Let A=C_(5^d) act on R_N by t^a↦t^(a+5^m), and let Γ act by multiplication. This gives the compact semidirect group Q=A⋊Γ. Its action on R_r has A trivial. The required quotient is exactly (J_(r,N))_Q. The exact sequence of continuous compact group homology for 0→J→R_N→R_r→0 gives

    H_1(Q,R_N) → H_1(Q,R_r) → J_Q
      → (R_N)_Q → (R_r)_Q → 0.

All permutation modules have finitely many points. Shapiro identifies their H_1 groups with the direct sums of the abelianizations of their actual stabilizers. For the equivariant map of finite Q-sets, the induced H_1 maps are the stabilizer inclusions, not transfers.

The Q-orbits on C_(5^N) are the valuation shells j=0,...,m-1 and the ball 5^m C_(5^N). There are m+1 of them. On C_(5^r), they are the r nonzero valuation shells and zero. The map on free orbit coinvariants is onto, with kernel Z_5^(m-r).

## Each nonzero lower orbit

Fix its representative 5^j with 0≤j<r, and write k=r-j. Its lower stabilizer is

    Q_j=A⋊(1+5^k Z_5).

Because χ-1 generates 5^k Z_5 on the translation group, its compact abelianization is

    Q_j^ab ≅ C_(5^min(d,k)) ⊕ Z_5.

There is exactly one upper orbit above this lower orbit. Its stabilizer consists of pairs (b,χ) with χ∈1+5^(k+h)Z_5 and

    b=(1-χ)/5^(k+h) mod 5^d.

Projection to χ identifies this stabilizer with 1+5^(k+h)Z_5. Choose the lower Γ generator 1+5^k, and the upper generator χ=(1+5^k)^(5^h). The latter maps to

    (b, 5^h) ∈ C_(5^min(d,k)) ⊕ Z_5,

where b is a 5-adic unit by the binomial valuation. Quotienting by this relation yields a SINGLE cyclic group of order 5^(h+min(d,k)). This is the extension responsible for C25 in the smallest r>0 example.

## The zero lower orbit

Its stabilizer is Q. The tame unit 2 acts on A by multiplication by 2, so A has zero coinvariants in Q^ab; the pro-five part of Q^ab is just the pro-five part of Γ. The upper zero/ball orbit has stabilizer Γ, whose inclusion surjects on that abelianization. Thus this lower orbit contributes no torsion cokernel. Upper shells j≥r impose only further relations in this already-zero cokernel.

The exact sequence now gives a finite torsion kernel of the displayed type and free quotient Z_5^h. The free quotient splits continuously, proving the boundary formula.

## Natural maps retained, and the remaining gate

The natural reduction J_(r,N)/q_mJ_(r,N)→J_(r,m) maps the kth cyclic torsion group of exponent h+min(d,k) onto the kth cyclic group of exponent h. Its kernel on that factor has exponent min(d,k); this follows from the same stabilizer presentation by killing A. It is the identity on the free orbit-kernel quotient. The further inclusion into (R_m)_Γ kills the torsion and identifies the free quotient with ker((R_m)_Γ→(R_r)_Γ).

These statements concern the literal unweighted permutation boundary. The actual arithmetic comparison may transport the source through multiplication by u and a half-gauge, and has a weighted target. Its exact natural map must still be identified before this calculation can be used to classify the entire restriction kernel. No conclusion from equal coranks or abstract module types is being made.

## Conditional arithmetic interpretation to be audited

On the first boundary, the retained source generator gives the Cartier-untwisted action S_chi(t) S_chi(t^(5^r)) sigma, while the target has S_chi(t) sigma. Multiplication by u q_r and u respectively should transport the natural map to the literal reduction J_(r,N)/q_mJ_(r,N)→R_m; the augmentation kernels and diagonal half-gauge still require exact comparison. If that comparison and the full E-injection/zero-snake gate hold, the boundary kernel would be the torsion factors computed above. The actual restriction-corestriction exponent 5^(N-r) would then allow the same bounded cyclic-lift splitting as D90, suggesting S=product C_(5^(N-r)) times two copies of C_(5^(m-r+k)) for 1≤k≤min(r,N-m-1). This paragraph is conditional and is NOT a registered or proved arithmetic classification.
