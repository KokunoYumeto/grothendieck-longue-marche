# Original Bhat s-frame and the exact canonical signed phase

Complete conversation proof, fully audited by root, A and CE; DE fully audited the normalized Bhat-frame and basic consequences. Old original frame/matrix bytes remain to be rebound after outage. No execution or formal promotion. The even-diagonal frame result was already retained historically; no novelty claim is made for that portion.

## 1. Exact Bhat inputs and canonical reflection transporter

Use the original Bhat=profinite(C2(s)*C3(r)), its level-two normal free subgroup F with quotient S3, and iota=Ad(s)|F exchanging x,y. Let alpha be the actual negative involution and Sigma=alpha c, with c(s)=s. The retained original normalized frame is
alpha(s)=Sigma(s)=s phi=beta_frame s beta_frame^(-1),
where beta_frame belongs to F. Cancelling s gives the identity INSIDE F
phi=iota(beta_frame)beta_frame^(-1).

Canonical duality iota(u)=u^(-1) makes (s u)²=1; orientation/mod-S3 shows s u is nontrivial. Herfort–Ribes finite-factor torsion conjugacy gives s u=g s g^(-1) in Bhat. Its S3 image forces g modF into C_S3(s)=<s>. Multiplying g on the right by s if needed preserves the conjugate and gives gamma in F. The centralizer theorem C_Bhat(s)=<s> and F intersect <s>=1 give uniqueness of gamma. Hence
s u=gamma s gamma^(-1),
u=iota(gamma)gamma^(-1).

The original norm gives alpha(s u)=s phi alpha(u)=s u. Apply alpha to the transporter identity and use alpha(s)=beta_frame s beta_frame^(-1):
alpha(gamma)beta_frame s beta_frame^(-1)alpha(gamma)^(-1)
=gamma s gamma^(-1).
Both normalized conjugators belong to F. Uniqueness therefore yields
alpha(gamma)beta_frame=gamma,
beta_frame=alpha(gamma)^(-1)gamma.
No automorphism or surjectivity of psi_u is used.

## 2. Abelianization, full dihedral image, and original mod4 marking

Negative alpha acts by -I on Fab, so
(beta_frame)_ab=2 gamma_ab.
Since u lies in F', iota(gamma_ab)=gamma_ab, which means gamma_ab is diagonal. Thus beta_frame has even diagonal abelianization. If beta_frame^(-1)_ab=(rho,rho), rho belongs to 2 Zhat.

The actual full-dihedral result alpha_D=id also gives (beta_frame)_D=1 directly from beta_frame=alpha(gamma)^(-1)gamma.

A more general independent derivation applies to any multiplier-one GT0 pair (1,f): its original peripheral exponent gives f_D=1. If f=iota(beta)beta^(-1) for the normalized s-frame, beta_D is fixed by the dihedral swap. That swap sends T^r to T^(-r) and a T^r to a T^(1-r). The rotation fixed equation 2r=0 has only r=0 in Zhat; the reflection equation 2r=1 is impossible modulo2. Its full fixed subgroup is trivial. Thus beta_D=1 already for those multiplier-one frame data.

The retained ORIGINAL signed q12 generator matrices are
x -> (1,2;0,1), y -> (1,0;-2,1).
Modulo4, X4=I+2E12 and Y4=I-2E21 commute and square to I. Therefore q4 factors through exponent sums modulo2, proving
q4(beta_frame)=I.
This is a supplied historical marking, not a claim of a fresh file read.

## 3. Signed q3 calculation without extending s to S

Use the original signed X,Y, S=(0,2;1,0), J=diag(1,-1), j=Ad(J), C as in the signed quotient proof. Put
B=q3(beta_frame), Gamma=q3(gamma), Phi=q3(phi), U=q3(u),
beta_nu=Inn(X^nu)j.
Actual kernel stability gives
B=beta_nu(Gamma)^(-1)Gamma,
U=S Gamma S^(-1)Gamma^(-1).

IMPORTANT TYPING: S²=-I, so s->S is NOT asserted to extend Bhat into SL2(F3). Instead apply q3 to the already established F-identity phi=iota(beta_frame)beta_frame^(-1), using q3 iota=Ad(S)q3. It gives Phi=S B S^(-1)B^(-1), and multiplication using S²=-I yields
B S B^(-1)=S Phi.

The actual positive phase Phi=Y^nu X^(-nu) gives
S Phi=X^nu S X^(-nu).
Since C_SL2(F3)(S)=<S>, we get B=X^nu S^b for some b modulo4.

Let chi:SL2(F3)->C3 be abelianization, chi(X)=chi(Y)=1. The norm expression for B gives chi(B)=2 chi(Gamma), while B=X^nu S^b gives chi(B)=nu. Thus chi(Gamma)=-nu, and
Gamma=X^(-nu)H for H in Q8.
Substitution gives
X^(-nu)B=j(H)^(-1)H,
U=Y^(-nu)[S,H]X^nu.

## 4. The Q8 identity and exact frame square

Put R=U_2. Every H in Q8 has the form S^a R^b, b in {0,1}. The literal identities are
j(S)=S^(-1), j(R)=R S, R S R^(-1)=S^(-1), S²=R²=-I.
If b=0, j(H)^(-1)H=S^(2a).
If b=1, j(H)^(-1)H=S^(-2a-1).
Therefore in both cases
(j(H)^(-1)H)²=[S,H]=(-I)^b.

Since U=epsilon_u Y^(-nu)X^nu, comparison gives
epsilon_u I=(X^(-nu)B)².
The inverse has the same square because X^(-nu)B belongs to <S>, whose fourth powers are I. Hence the precise ORIGINAL-frame formula is
epsilon_u I=(q3(beta_frame)^(-1)X^nu)².

If beta_frame^(-1)_ab=(rho,rho), then chi(B)=-2rho=rho modulo3, so nu=rho modulo3.

This expresses the ACTUAL canonical phase through the retained ORIGINAL s-transporter. It does not identify this corrected finite element with the named E61 W until the exact cusp normalizer is rebound, nor identify the stated parity character epsilon2 or the CM character Delta. No r-frame sign or equality with d modulo3 is implied.
