# Class-three continuation: exact finite corrections and the constructive route

## 1. Completed finite correction calculation

`work/sections/split_auxiliary_agent.tex` is A.55. For a finite Galois field K containing μ_N, and T the primes completely split in K, it proves the exact image of central correction with ramification allowed in S∪T. The image is the annihilator of the actual inflated dual group H¹(Gal(K/Q),Z/N(−1)), under the sum of local cup-product Brauer invariants. Its proof uses finite Poitou–Tate duality (Milne, ADT I.4.10(b)), finiteness of H¹(G_{Q,S},−), and Chebotarev to identify the stabilized dual kernel.

The explicit order-sixteen dual cocycle is

    ζ_N = (N/16) κ_N(2v^24) + (N/2) binom(L,2),
    χ mod16 = (−1)^e 5^L,  L ∈ Z/4.

It gives a concrete failed correction problem with c=2·73^24 and S={2,73,∞}: an unramified Frobenius value one only at73 pairs to1/2. This is an actual correction counterexample. It has not been identified with the central discrepancy of any of the constructed ghosts.

The finite certificate and output are `work/code/split_auxiliary_certificate.py` and `work/code/split_auxiliary_certificate_output.txt`.

## 2. The exact comparison with finite defining-system flexibility

For fixed integral abelian cocycles a,b and an integral class-two coordinate h, changing its reduction modulo ℓ^r by a finite cocycle z is the actual central action on the set of finite class-two lifts. The coefficient exact sequence supplies

    0 → H¹_cts(G_Q,Z_ell(2))/ell^r
      → H¹(G_Q,Z/ell^r(2))
      --∂→ H²_cts(G_Q,Z_ell(2))[ell^r] → 0.

Thus the finite defining system h+z comes from an integral class-two lift precisely when ∂z=0. A.55 computes this condition explicitly: z must be unramified outside ell, and at ell=2 must have zero real restriction. A.40 makes its image zero for ell≥5, cyclic of order3 at ell=3, and a reduction of Z/8 at ell=2. The two cross-prime normalizations eliminate the remaining integral choices.

Primary source opened: Christian Maire, Ján Mináč, Ravi Ramakrishna and Nguyễn Duy Tân, *On the strong Massey vanishing property for number fields*, Mathematische Annalen 395, article102 (2026), published7 July2026, DOI10.1007/s00208-026-03518-1, <https://link.springer.com/article/10.1007/s00208-026-03518-1>. Theorem1.1 treats strong n-fold Massey vanishing for trivial F_p coefficients when μ_p is not in the base field. Definition1.1 explicitly distinguishes the chosen defining-system map Γ→Ubar from the existence of some lift of the abelian tuple. Theorem1.2 concerns finite matrix lifts with specified mod-p reduction.

The comparison map relevant here is reduction from integral class-two defining systems to finite defining systems, whose image is precisely the kernel of ∂ above. Varying a finite defining system in the larger H¹ group does not by itself put it in that image. In addition, our abelian Kummer coefficients have action χ; for odd p, no equivariant identification with the trivial coefficient module exists, since complex conjugation acts as−1 on F_p(1) and as1 on F_p. Restricting to G_{Q(μ_p)} makes that action trivial, but the base field then contains μ_p, so the stated hypothesis of Theorem1.1 changes. These are explicit comparison maps and coefficient actions; no claim is made that other Massey results cannot supply further information.

## 3. The full integral valuation criterion

`work/sections/weight3_divisibility_agent.tex` is A.58. At a support prime q>3, valuation patterns

    (24e(q²−1),0), (0,24e(q²−1)),
    (−24e(q²−1),−24e(q²−1))

make both actual strict third-layer residues divided by q²−1 lie in e Z_ell, at every coefficient ell≠q. For the negative pattern, the exact substitution is

    n=m,  α=β+(q−1)(u+1/2),  t=binom(m,2)−mu.

Both residues then factor as m(C+(q²−1)R), with C integral and24R integral. This proves the continuous primitive bound, including the inverse-limit part, whenever e_q→0. Fixed valuations (0,1) at2 and(1,0) at3 are handled by the unique cross-normalized class-two lift s_*.

The exact symbolic certificate and output are `work/code/valuation_divisibility_certificate.py` and `work/code/valuation_divisibility_certificate_output.txt`.

## 4. Three-prime construction: completed in A.59

A.59 and its coefficient-prime analytic lemma have been completed and independently audited by root and all three agents. Both are integrated in the 128-page manuscript. The following records the induction specification; the full proof is in sections/class3_ghost_construction.tex and sections/class3_coefficient_prime_lemma.tex.

Set n_j=(j+4)!, M_j=24n_j, D_j=48n_j², B(D)=(D+1)^4. Maintain pairwise coprime integer coefficients

    a_j=3u_j^24, b_j=−2v_j^24, c_j=w_j^24,

with u_j,v_j,w_j positive, prime to6 and with disjoint supports. Maintain unit-coordinate local points on a_jX^{D_j}+b_jY^{D_j}=c_jZ^{D_j} at every prime, and high a_j+b_j−c_j precision at p≤B(D_j). Start with(3,−2,1).

At stage j, process all primes up to a cutoff P containing B(D_{j+1}) and all old coefficient support. Prescribe residues of three prospective primes in increasing order of p. Prior choices then fix each exponent E_j(z)=24n_j(z²−1) modulo p−1. At p|n_j impose v_p(z−1)=v_p(n_j); at other processed p impose z modp≠0,±1. These imply v_p(E_j(z))=v_p(D_j), so each exponent has exactly the D_j-power image in every residue field encountered later.

At small/high-error places choose a common value of the three local analytic functions F_i(z)=z^{E_j(z)} and perturb one variable. At p|n_j the common starting variable is1+p^{v_p(n_j)}; the exact image lemma of the Legendre agent supplies the required precision. At p∤n_j, Teichmüller coordinates give a simple-root local inverse. At large places use the existing D_j-unit point (at coefficient places) or the Weil bound (at unit-coefficient places), and scale all three coordinates to avoid D_j-th power value1. Preimages under the fixed residue exponents then avoid±1, so the same inverse applies.

Chebotarev realizes the three resulting CRT classes with complete splitting in the radical fields for b_j/c_j, a_j/c_j and−a_j/b_j, all with root exponent n_j. Their maximal abelian subfields are Q(μ_{n_j}); the third ratio is (3/2) times a24th power and requires the corresponding pure-quartic check. Update the three coefficients by fresh primes q_j,r_j,s_j to exponents E_j(q_j),E_j(r_j),E_j(s_j). The fresh-prime congruences imply gcd(D_{j+1},q_j−1)|n_j, and likewise for r_j,s_j. Their appropriate split ratios are therefore D_{j+1}-powers locally, and all other updates are n_j-th powers. The new coefficient places have unit D_{j+1}-points. At old places impose the high next sum-error; elsewhere use the Weil bound.

Completed limits of A=a/c and B=b/c have support patterns exactly those of A.58, with e_q=n_j at each fresh prime. Factorial divisibility gives convergence in the global power completion and in every Q_p; the additive precision gives A_p+B_p=1. The complete local/CRT/field induction is proved in A.59; its conclusion is an actual full integral class-three lift of one ordinary infinite-support pair. The later fixed-depth result below proves higher lifting for pairs chosen at each depth; it does not supply a compatible full lift of this particular A.59 pair.

## 5. Class four and exact old-place matching

A.60 (sections/weight3_matching_agent.tex) proves the actual surjection from global integral weight-three H¹ to the four local groups at (q,ell)=(2,7),(3,13),(3,2), and (infinity,2). Cyclotomic unit eigenclasses supply the first two generators; the integral lifts of the finite Kummer classes of -1 and 2 supply an invertible two-by-two restriction matrix for the last two. Exact finite-field products are retained in code/weight3_local_generators.py and its output.

A.61 (sections/class4_lift_agent.tex) proves the full actual class-four lift for valuations E_q=24e_q(q²−1)(q³−1). It uses primitive integral Hall/Magnus coordinate maps, the exact strict residue q^(-1) times the lifted tame relator, and the actual unramified Galois action. The fresh divided fourth-layer residues belong to e_q Z_ell, literally in the c0 module. The global remaining obstruction is zero by K6(Z)=0; its two-primary real restriction is handled explicitly. Root's independent code/class4_magnus_certificate.py verifies the primitive degree-three/four extraction matrices and the denominator ideals.

A.62 (sections/cubic_exponent_ghost.tex) supplies these ordinary infinite-support pairs, for arbitrary constants divisible by24. Both statements were fully independently audited by root and the agents.

## 6. Every fixed nilpotent depth

A.65 (sections/fixed_depth_lift_agent.tex) and A.66 (sections/general_exponent_ghost.tex) prove the following precise new conclusion: for every fixed nilpotency class R and every prescribed finite Magnus congruence N, there is an ordinary infinite-support unit-equation pair with an actual integral class-R section agreeing with the rational point3 in that finite Magnus quotient.

The actual canonical Hall lift is controlled by D=(R!)^(h_R+1), with h_R the number of Hall generators through degreeR. No assertion identifies the kernel of the naive finite Magnus projection with the ordinary highest Lie layer: restricted-power terms at small coefficient primes are bypassed by the stronger lower congruence. The highest central coordinate remains the exact integral module Zhat(r) to the appropriate free-Lie rank.

The unramified obstruction group at weight r is annihilated by B_r=2|K_(2r−2)(Z)|. This follows from Weibel VI.8.2, VI.9.11, and the finiteness of the positive even K-groups. At two and r divisible by4, the extra factor2 accounts for the real restriction; no uncomputed K-group is assumed zero.

The central correction is an explicit cochain diagram. Arrange the canonical defect c to be divisible by B_r M_r and its divided strict residues to have a literal c0 primitive. Then beta=[c/(B_r M_r)] is unramified and B_r beta=0, so c has a continuous integral primitive -h. The cocycle h mod B_r M_r has Bockstein -beta. Its reduction mod M_r has Bockstein -B_r beta=0, hence lifts to an integral cocycle. Subtract that cocycle, with an explicit lifted finite coboundary if needed, to make h pointwise divisible by M_r. Thus the actual finite congruence to point3 is preserved at the next layer. Equivalently, B_r beta=0 says directly that c/M_r has an integral primitive, which can be multiplied by M_r.

Fresh inertia is bounded by repeated actual tame equations, losing only a fixed Hall denominator and the factors q^i−1. The ordinary cup identity supplies the initial E/2 bound at weight2; omitting that input would leave an unjustified q−1 division. Relative to point3, the canonical fresh inertia agrees with the tangential Hall lift because point3 has trivial inertia there in every fixed nilpotent quotient.

A.66 provides the required exponents C n_j product_(i=2)^(R−1)(q^i−1), with C arbitrarily divisible and n_j factorial. Dividing the exponents by C gives convergent products, proving actual compatible Cth roots of A/3 and B/(-2), which is the precise starting abelian congruence.

The pair is allowed to depend on R and N. This work has not constructed one ordinary ghost with a compatible sequence of all nilpotent lifts, or a section of the full geometric fundamental group. In particular, these fixed-depth existence statements alone cannot be passed to an inverse limit while retaining a fixed nonzero fresh valuation.
