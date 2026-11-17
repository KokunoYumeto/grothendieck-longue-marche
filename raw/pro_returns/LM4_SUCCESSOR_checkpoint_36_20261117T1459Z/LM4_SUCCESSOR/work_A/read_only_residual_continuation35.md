# Residual continuation preserved after checkpoint34 release

This note records the complete mathematics developed while checkpoint34 writers were paused. It is first saved in checkpoint35. Prior34 sources, hashes and pause records remain unchanged. Conversation-level reviews are distinguished from saved-byte reviews. The formal normalized result is separately proposed as A118.

## 1. Exact normalized full lift and the canonical word

Use the actual original negative full-GT involution alpha, its norm word u in F', parameter phi, even k, d=1+2k, B=C2(s) coproduct C3(r), delta=sr, and the actual residual R=N intersect F' intersect O from the saved e34097f6 proof. That proof supplies a FULL peripheral automorphism Gamma inducing the SPECIFIED Psi_R on the whole B/R and sending delta literally to delta^d.

Its normalization is direct. Put f=s Gamma(s). Since the quotient map sends s to v=su, one has fR=uR. Thus f belongs to F' because u does and R is contained in F'. The involution relation gives iota(f)=f^-1. From x=delta^-2 and y=sxs, Gamma(x)=x^d and Gamma(y)=f^-1 y^d f. Gamma acts identically on the original S3 quotient, so its pure restriction commutes with the geometric S3 in Out(F). Its three peripheral powers are all d. The actual Harbater--Schneps identification in A1 therefore puts this normalized Gamma in GT0.

The exact A3 construction matters: reduce the multiplier by LEFT composition with an actual multiplier-d Galois automorphism's inverse; its original LM7_PUSH E65 covariance preserves R. Use R=[R,B] in the closed-normal criterion, and choose the final cusp correction inside R. Compose the Galois automorphism back. No later arbitrary inner normalization is inserted, so the entire B/R action is preserved. An unspecified peripheral lift alone would not establish fR=uR.

Let beta=Gamma^-1 alpha Gamma. The normalized group law gives

    phi_beta = Gamma^-1(f^-1 phi alpha(f)),
    U' = Gamma^-1(f^-1 u).

Then phi_beta beta(U')=U' by direct multiplication. Fixed-subgroup triviality transfers from alpha to beta, so norm uniqueness among ALL F' solutions identifies this U' with the actual canonical word. Gamma preserves R, hence U' lies in R, and phi_beta=U' beta(U')^-1 lies in R. On B/R, beta is c_B.

The actual dihedral normalization also gives d_beta=1. For any normalized peripheral gamma=(lambda,f_gamma), write q_D(f_gamma)=T^s in D=Zhat(T) semidirect C2(a), where s is even. Then gamma_D(T)=T^(1+2s). The third peripheral power condition makes 1+2s equal to one GLOBAL sign times lambda; because 1+2s is1 modulo4, the sign is chi4(lambda). Therefore D_gamma=chi4(lambda)lambda. For Gamma, d is1 modulo4, so q_D(f)=T^k=q_D(u), and q_D(U')=1. The original A45 definition then gives k_beta=0 and d_beta=1. In general u_(gamma alpha gamma^-1)=f_gamma gamma(u), and d_(gamma alpha gamma^-1)=D_gamma d; the direct norm proof needs no automorphy of a prospective canonical substitution.

## 2. The genuine transported pentagon

Write the five ORIGINAL marked P4 pairs, with braid generator f_br distinct from parameter f, as

    (a,ce), (bc,f_br), (c,f_br), (ab,ef_br), (a,c).

For these pairs (a_j,b_j), put

    f_j=f(a_j,b_j),
    U'_j=U'(a_j^d, f_j^-1 b_j^d f_j).

The exact F-word equality u=f Gamma(U') gives u(a_j,b_j)=f_j U'_j at each pair, without assuming an action of Gamma on P4. Thus the full original canonical pentagon is EXACTLY

    (f_1 U'_1)(f_2 U'_2)=(f_3 U'_3)(f_4 U'_4)(f_5 U'_5).

The factors and their order cannot be discarded. Gamma is proved GT0, not full GT, and beta is only thereby proved a negative GT0 involution. No ordinary pentagon for U' is obtained. The original GT0-conjugacy-invariant obstruction remains unchanged at its established scope, but its value is not selected.

## 3. Superseded longer normalization arguments

These earlier candidate arguments were audited algebraically, but are unnecessary after the direct fR=uR identity. They are preserved to explain the change of proof rather than silently erased.

(a) Choose the unique actual full pure s-frame g0 with su=g0 s g0^-1. Then u=iota(g0)g0^-1 and u_ab=0 make g0_ab diagonal. Prescribing its quotient frame through multiplier reduction and A3 would make the lifted s-frame have the same abelianization, since R is contained in F'. Consequently f=iota(g)g^-1 belongs to F'. This is a valid longer route conditional on that exact prescribed-frame output, but the direct whole-quotient argument does not need it.

(b) If two normalized words f and u give the same pure substitution on Q=F/R, their quotient c=f u^-1 centralizes y. The two-cycle relation also makes it centralize uxu^-1. These two elements generate Q, so c is in Z(Q) intersect Q'. In the actual product model this is the odd scalar-sign product, fixed by the cyclic action. Comparing the original f-hexagon with the already killed H_d for u gives c^3=c=1. This is an optional independent consistency check, not the normalization step used in A118.

## 4. Entire residual C3 cohomology

Let e=plus or minus1, epsilon=(1-e)/2, R_e=y^epsilon r, and rho_e=Ad(R_e). The source-bound A109 argument gives

    (F')^rho_e=1,    H1(C3,F';rho_e)={*}.

The minus branch follows from the actual s-conjugation and inversion of the cyclic generator. Since

    F'/R = P' × SL2(Z3)' × product_(p>=5) SL2(Zp),

the connecting map gives the ENTIRE pointed bijection

    T_e^R=(F'/R)^rho_e --> H1(C3,R;rho_e),
    t --> [g^-1 rho_e(g)],

where g is any actual F' lift. Surjectivity is exactly H1(C3,F')={*}; injectivity is exactly (F')^rho_e=1. For the topology, take the compact preimage of T_e^R in F' and its continuous defect map to the compact Hausdorff twisted-conjugacy quotient. It is constant on each fiber and therefore descends continuously. A continuous bijection from compact to Hausdorff is a homeomorphism. No continuous choice of lifts is needed, and no group structure on a general nonabelian H1 set is being presumed.

Its exact fixed-group coordinates are

    (P')^rho_e × C_SL2(Z3)'(J_e) × product_(p>=5) C_SL2(Zp)(J_e),

where J_e=diag(1,e) J diag(1,e)^-1 and J=[[0,-1],[1,-1]]. The dyadic coordinate here is the FULL free pro-two derived group P', not the earlier central quotient's derived group.

Retain the ORIGINAL full coherent frame

    J_e^alpha=s phi A_r  if e=1,
    J_e^alpha=A_r s     if e=-1.

It obeys alpha(J_e^alpha)J_e^alpha=1. Thus theta=Ad((J_e^alpha)^-1)alpha is an involution and reverses rho_e. On a cyclic cocycle z its induced reversal is

    z --> rho_e(theta(z)^-1).

For z=g^-1 rho_e(g), this is exactly (theta g)^-1 rho_e(theta g); hence the connecting homeomorphism carries it to the actual kappa=theta action on T_e^R. The odd torus factors and their inversion action are the previously proved actual ones, so

    H1(C2,T_e^R)=H1(C2,(P')^rho_e) × product_(p odd) C2.

No dyadic factor or actual coherent class has been evaluated. CE independently audited this whole argument during the pause; that was a conversation-level proof audit, not a saved-source binding. DE is formalizing the corresponding actual residual C3/C2 results separately as A117/A119.

## 5. The exact cubic gate before any H1 classification

Let eta=v delta^d and choose a full h in F lifting an actual quotient r-frame: eta R=h R_e h^-1 R. Set

    a=h^-1 eta h R_e^-1 in R.

Then the literal identity is

    a rho_e(a) rho_e^2(a)=h^-1 eta^3 h
      =h^-1 u^-1 H_d^-1 u h.

Thus H_d=1 is EXACTLY the assertion that this prescribed a is a cyclic cocycle. One cannot first apply the H1 classification to a and thereby assume the desired norm equation. This is a remaining nonlinear gate.

A compatible mixed identity can be printed without imposing that gate. Put

    w=(J_e^alpha)^-1 alpha(h)^-1 v h,
    theta=Ad((J_e^alpha)^-1)alpha.

Then theta(w)w=1, and direct multiplication using alpha(eta)=v eta^-1 v gives

    theta(a)=w rho_e^-1(a^-1) rho_e^-1(w)^-1.

Modulo R, w belongs to T_e^R. This is a mixed C2/C3 system, not a proof of its cubic norm vanishing. The last displayed mixed identity is a newly recorded direct algebraic derivation; independent saved-source review is requested before any use beyond this note.

## 6. Two existing route boundaries freshly checked

The complete saved A21 proof was reopened. An open free profinite subgroup of finite rank does NOT by itself give recognition as a finite graph of finite groups. Its explicit torsion-free Gamma_*=(product_(p odd)Zp) semidirect Z2 has open Zhat, and C2 coproduct Gamma_* has open rank-two free subgroup of index two, but abelianization C2×Z2 prevents the finite-graph conclusion. This does not refute the additional particular S3/V4 configuration in B semidirect alpha; it blocks only the generic recognition shortcut. A marked proper-amalgam/tree construction would still need proof.

The complete original LM7_PUSH E61 source was freshly reread. Its specified genus-one sewing projection is already trivial modulo twelve, including the extra CM branch. Its full sewing relation is imposed only on the stated Nakamura--Schneps subgroup; it cannot be imposed on all full GT from that source. The original A1 scope distinction remains: Collas's genus-one acting group is GR/I-Gamma, not automatically all GT. A new primary audit of Enriquez's profinite GT_ell construction has begun, but no section theorem or implication for the actual CM sign has yet been accepted. The attempted large PDF output was truncated and was not counted as a complete read.

## 7. Scope and preservation

The exact normalized reduction in sections1--2 was independently passed at conversation level by root and DE before release. The C3/reversal proof in section4 was independently passed by CE. These receipts describe mathematics observed in conversation; newly saved hashes must receive their own byte-bound reviews. All preceding34 sources remain unchanged. Neither full Main A nor the actual CM value has been solved by these reductions.
