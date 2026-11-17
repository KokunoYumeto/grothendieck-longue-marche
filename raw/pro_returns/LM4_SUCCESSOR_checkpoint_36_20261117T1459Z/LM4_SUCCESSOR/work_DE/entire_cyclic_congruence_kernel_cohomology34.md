# Entire cyclic cohomology of the actual first congruence-central kernel

Checkpoint34 research proof. This is separate from the frozen proposed formal statements A109--A110. It retains the actual original marking throughout and does not decide the original full-GT CM parity.

## 1. Exact input and statement

Let B=C2(s) amalg C3(r) be the actual full profinite modular free product, F its marked S3 kernel, rho=Ad(r), and F' its closed derived subgroup. Use the actual signed congruence map q:F -> C, N=ker(q), and N1=closure([N,F]). The proved geometric stability makes N1 rho-invariant; N1 lies in F'. Put E1=F/N1 and E1'=F'/N1.

The complete A109 proof supplies BOTH

    (F')^rho=1,       H^1(C3,F')={*}.

Use continuous nonabelian cohomology with cocycles c rho(c) rho^2(c)=1 and equivalence c~n^(-1)c rho(n).

Put T=(E1')^rho. There is a canonical pointed homeomorphism

    boundary:T -> H^1(C3,N1),
    h |-> [w^(-1)rho(w)],       w in F' mapping to h.          (1)

Furthermore T equals the actual pure quotient centralizer C_E1(r). This is a homeomorphism of pointed compact spaces. No ordinary group structure on H^1 is assumed, and no completion of an infinite-index discrete kernel is identified with N1.

## 2. The boundary and both inverse assertions

For h fixed by rho, any lift w has defect c_w=w^(-1)rho(w) in N1. Its three-factor norm telescopes to w^(-1)rho^3(w)=1. Replacing w by wn, n in N1, gives

    c_(wn)=n^(-1)c_w rho(n),

so (1) is independent of the lift and sends the identity to the distinguished point.

For surjectivity take any N1-cocycle c. Viewed in F', it is a coboundary because H^1(C3,F') is trivial. Thus c=w^(-1)rho(w) for some w in F'. Its quotient h=wN1 is fixed, and (1) maps h to [c].

For injectivity suppose h_i have lifts w_i and

    c_(w2)=n^(-1)c_(w1)rho(n)

for n in N1. The lifts w1 n and w2 then have the same crossed defect. Direct multiplication gives

    rho(w1 n w2^(-1))=w1 n w2^(-1).

This element belongs to F', whose fixed subgroup is one. Hence w1 n=w2 and h1=h2. In particular a quotient fixed element has a rho-fixed lift in F' exactly when it is the identity.

For topology let

    L={w in F' : w^(-1)rho(w) in N1}.

It is compact and closed. Its quotient map onto T is surjective, and its continuous defect map into the compact cocycle space followed by the orbit quotient is constant on the N1 fibers. Therefore (1) is continuous, without choosing any continuous section. The cohomology space is Hausdorff: its cocycle space is closed in N1, and the compact N1 action has a compact, hence closed, orbit relation. A continuous bijection from compact T to this Hausdorff space is a homeomorphism.

Finally N1<=F' gives E1_ab=F_ab=Zhat^2. An element centralizing r is fixed by the original order-three matrix

    M = [[0,-1],[1,-1]].

The determinant of M-I is three; the adjugate and injectivity of multiplication by three on Zhat^2 show its fixed module is zero. Consequently C_E1(r)<=E1', proving T=C_E1(r).

## 3. Exact signed comparison and the central extension of T

A106 gives the actual compact central pro-two extension

    1 -> K=(N intersect F')/N1 -> E1' -> C' -> 1.             (2)

On C' the original rho is honest conjugation by the integral matrix

    J = [[0,-1],[1,-1]],

since the extra cyclic exponent-parity character kills F'. Thus there is an exact continuous sequence of compact groups

    1 -> K^rho -> T -> C_(C')(J) -> 1.                      (3)

To prove its right-hand surjectivity, lift a J-centralizing c in C' to g in E1'. The defect g^(-1)rho(g) is a K-cocycle. A109's full compact coprime-action lemma gives H^1(C3,K)={*}, because K is pro-two. Write that defect as k^(-1)rho(k). Then gk^(-1) is fixed and lifts c. The kernel is exactly K^rho. In particular (3) is a central extension with a pro-two kernel; no assertion that it splits is needed.

Write C3matrix=J mod3=XYX^(-1) mod3. This equality with the word XYX^(-1) is only a modulo-three equality. For the actual derived kernel

    K3'=ker(q3:F' -> Q8),

A109 identifies H^1(C3,K3') with Q8^rho={I,-I}. Because N1<=K3', the natural cohomology map fits the exact commutative comparison

    T ---------------------> H^1(C3,N1)
    | q3                          | inclusion-induced
    v                             v
    {I,-I} ----------------> H^1(C3,K3').                  (4)

Both horizontal maps are the proved pointed homeomorphisms. To check the marking, choose the SAME lift w in F' in both boundary constructions. The lower label is exactly q3(w)=q3(h), so no inverse or sign change occurs. The vertical map is surjective: the actual h constructed in A110 has q3(h)=-I, while the identity supplies I. Its fibers are therefore the two closed cosets of ker(q3|T), viewed through (1). This description does not select the actual CM sign.

## 4. Exact original quotient-frame interpretation

For the original multiplier-one automorphism Sigma=alpha c, let A_r in F' be its unique original full-group r-frame:

    Sigma(r)=A_r r A_r^(-1),       rho(A_r)=phi A_r.

The complete set of PURE quotient r-frames for this same action on B1 is

    { image(A_r) h : h in T }.                             (5)

Indeed two such conjugators differ on the right by C_E1(r)=T. Every element of this set has the same zero abelian vector because A_r and T lie in the actual derived groups.

Choose h in T and a lift w in F'. The full pure word t=A_r w lifts its quotient frame. Its actual transporter defect is

    t^(-1) phi^(-1) rho(t)
       = w^(-1) A_r^(-1) phi^(-1) rho(A_r) rho(w)
       = w^(-1)rho(w) in N1.                               (6)

Thus (1) parameterizes ALL obstruction classes to lifting the quotient r-frames in (5) to an exact full-group transporter. The distinguished class occurs precisely at h=1, in agreement with the original full-group uniqueness. Changing the lift of the quotient frame changes (6) only by an N1-coboundary.

Under the signed comparison (4), its label is q3(h). In particular the A110 fixed element with q3(h)=-I changes the original modulo-three frame sign while leaving the quotient automorphism, abelian normalization and modulo-four normalization unchanged. The theorem does not identify which original sign epsilon_A occurs. It explains why the arbitrary quotient-frame scalar recipe cannot resolve it, and why a coherent extra condition such as A111 has genuinely additional content.

## 5. Scope and complete dependencies

This proof uses the COMPLETE A109 torsion-normalization argument for both H^1(C3,F')={*} and (F')^rho=1, the actual A106 kernel criterion, A107 geometric stability, and A110's theoretically constructed fixed lift. It uses no new target computation, no generic completion/intersection exchange, no assertion that N1 is pro-two, and no assertion that the exact central extension (3) splits. In fact A110 already proves N1 is NOT pro-two, consistently with the nontrivial classes in (1).

The actual full-GT CM character and both main comparison problems remain open.
