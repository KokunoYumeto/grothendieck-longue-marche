# Original r-frame and exact CRT normalization of the retained CM transporters

Complete conversation proof. Root and DE fully audited the r-frame, root/CE/DE fully audited the normalization, and the earlier original beta-frame proof was checked by all. The supplied original E61 frame formulas and covariance are retained inputs; historical source bytes remain to be rebound. No named parity-character definition is guessed, and no formal promotion is claimed.

## 1. The original r-transporter lies in F'

In Bhat=C2(s)*C3(r), retain x=(sr)^(-2), y=sxs, z=(xy)^(-1). The reduced words are
x=r² s r² s, y=s r² s r².
Conjugation by r sends x to y, y to r s r² s r=z, and z to x. Denote this ORIGINAL cyclic automorphism by rho_cyc.

For Sigma=alpha c, the retained normalized r-frame is
Sigma(r)=phi^(-1)r=A_r r A_r^(-1),
with A_r in F. Thus
phi=r A_r r^(-1)A_r^(-1)=rho_cyc(A_r)A_r^(-1).

Since phi lies in F', the abelianization satisfies
(rho_cyc-I)(A_r)_ab=0.
The matrix of rho_cyc on the x,y basis is (0,-1;1,-1), so det(rho_cyc-I)=3. Its adjugate and injectivity of multiplication by3 on Zhat show (A_r)_ab=0. This is a GLOBAL assertion before reduction modulo3; the matrix becomes singular mod3, so a mod3-only argument would be invalid.

Write A3=q3(A_r). Since A_r lies in F', the central character in q3 rho_cyc versus Ad(C)q3 vanishes on A_r. Therefore
Phi=C A3 C^(-1)A3^(-1).
Using Phi=Y^nu X^(-nu) and C X C^(-1)=Y gives
A3 C A3^(-1)=Phi^(-1)C=X^nu C X^(-nu).

The exact centralizer of C in SL2(F3) is <C,-I>, a cyclic group of order6. Hence A3=X^nu h with h there. Since A3 lies in Q8, abelianization forces
h=epsilon_A C^(-nu), epsilon_A in {+1,-1}.
Thus
A3=epsilon_A X^nu C^(-nu),
A3^(-1)X^nu=epsilon_A C^nu.
No equality between epsilon_A and d modulo3 has been proved.

One retained marking safeguard: the negative-alpha r-conjugator is J_r=s phi A_r=s rho_cyc(A_r), which lies in the s-coset. The order-two condition gives alpha(J_r)J_r=1. It does NOT give alpha(A_r)=A_r^(-1), and A_r must not replace J_r in that norm problem.

## 2. Exact E61 inputs and the canonical even-power lift

Retain the original q12:Bhat->SL2(Z/12)/{±I}, the original F generator lifts
X12=(1,2;0,1), Y12=(1,0;-2,1),
and the frame formulas
T=q12(A_r^(-1)) V,
W=q12(beta_s^(-1)) V,
V=U0^(8rho).
The original E61 covariance is q12 Sigma=Ad(V)q12, with beta_s^(-1)_ab=(rho,rho).

No matrix for U0 is chosen. Choose either signed SL2(Z/12) lift U0tilde, and DEFINE
Vtilde=U0tilde^(8rho).
This is independent of changing U0tilde to -U0tilde, since the exponent is even. It is the canonical even-power lift.

EXPLICIT PRECISION CORRECTION: Vtilde has cube I. The other signed lift -Vtilde of the same projective V has cube -I. The shorthand 'every signed lift of V has cube I' is false and is retained as superseded; only the canonical even-power lift is used below.

## 3. Exponents and positive signed covariance

The kernel of SL2(Z/4)->SL2(F2)=S3 consists of I+2M with trace(M)=0 modulo2, and has exponent2. According as a reduction has order1,2,3, the element has order dividing2,4,6. Thus the exponent divides12.

For g in SL2(F3), Cayley-Hamilton gives g²=-I at trace0, and g³=-tr(g)I at trace+1 or-1. Its exponent also divides12. Consequently the chosen even-power lift has
Vtilde³=U0tilde^(24rho)=I
in both CRT components.

The covariance initially lives in the quotient by DIAGONAL ±I. Compare signed lifts on each free generator x,y. Modulo3, both sides have order3: Sigma has multiplier1, so its actual signed images are X and a conjugate of Y. Negating an order3 matrix gives order6. Therefore the possible diagonal sign is PLUS for each generator. The signed covariance holds in BOTH CRT components, and hence on the whole free group.

## 4. Determine the two components without guessing U0

Modulo3, the actual signed Sigma action is Inn(X^nu). Since X,Y generate SL2(F3), V3 differs from X^nu by a scalar ±I. The canonical cube-one property excludes the negative sign, so
V3=X^nu.

Modulo4, q4(phi)=I because phi lies in F' and the original X4,Y4 commute. Hence Sigma fixes both mod4 generators. The positive covariance shows V4 centralizes
X4=I+2E12, Y4=I-2E21.
Reduction of these commutation equations modulo2 makes bar(V4) centralize BOTH E12 and E21. Their common invertible centralizer in M2(F2) consists only of I. Thus V4 lies in the exponent-two reduction kernel. Since it also has cube I, V4=I.

The exact canonical CRT lift is therefore
Vtilde=(I,X^nu).

## 5. Actual corrected component powers

Take the signed products determined by the original F lifts and this canonical Vtilde:
Wtilde=q12_signed(beta_s^(-1)) Vtilde,
Ttilde=q12_signed(A_r^(-1)) Vtilde.
The original beta-frame proof gave q4(beta_s)=I and
(q3(beta_s)^(-1)X^nu)²=epsilon_u I.
Since A_r belongs to F', q4(A_r)=I as well. Consequently
W4=T4=I,
W3=q3(beta_s)^(-1)X^nu,
W3²=epsilon_u I,
T3=epsilon_A C^nu,
T3³=epsilon_A I.

These are actual component powers under the retained E61 formulas, derived without a guessed U0 matrix or an invalid homomorphism s->S into SL2. The embedding with mod4 component I identifies the corrected s-frame subgroup with <S>=C4 and the corrected r-frame subgroup with <C,-I>=C6. Their intrinsic cyclic parities are encoded by the displayed square and cube, respectively.

The exact correspondence with the NAMED epsilon2,epsilon3 conventions in E61/E65 remains a source-binding step until those definitions are read. The computation does not determine epsilon_A or epsilon_u, prove d mod3=epsilon_A, or settle Delta or the canonical hexagon.
