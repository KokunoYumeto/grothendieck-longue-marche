# Scope and exact cohomology addenda to the signed mod-three proof

Conversation-only complete proof. Root, A, CE and DE reviewed the GT0 scope and the trace-zero case; root, A and CE reviewed the precise two-class kernel comparison. No saved-byte rebind, formal promotion, or CM-frame identification is asserted.

## GT0 scope and canonical duality

Retain the original normalized negative involution alpha and phi in Fhat', with alpha(x)=x^(-1), alpha(y)=phi^(-1)y^(-1)phi. The accepted original GT0 outer S3 relation gives the original third peripheral inversion. Thus the marked triangle quotient, characteristic translation subgroup, exact signed lift, and the positive-Phi calculation in the parent proof require no canonical-u pentagon.

For completeness the accepted canonical duality follows from original GT0 identities and norm uniqueness. Let iota exchange x,y. The original relations are iota(phi)=phi^(-1) and iota alpha iota=Inn(phi) alpha, with Inn(phi)(v)=phi v phi^(-1). Apply iota to u=phi alpha(u):
iota(u)=phi^(-1) iota alpha(u)
       =phi^(-1) [phi alpha(iota(u)) phi^(-1)]
       =alpha(iota(u)) phi^(-1).
Hence alpha(iota(u))=iota(u) phi. Taking inverses gives
alpha(iota(u)^(-1))=phi^(-1)iota(u)^(-1).
Therefore iota(u)^(-1)=phi alpha(iota(u)^(-1)), and this word is in Fhat'. Uniqueness among all Fhat' norm solutions implies iota(u)^(-1)=u, proving iota(u)=u^(-1).

Consequently the signed descent q alpha=beta_nu q, positive Phi=Y^nu X^(-nu), and classification U=epsilon_u U_nu, U_nu=Y^(-nu)X^nu, hold at that original GT0 scope. They do not require that d=1+2k be a unit.

## Complete trace formula, including the nonunit branch

For every actual k in 2 Zhat, let
C=XYX^(-1)=(0,2;1,2),
g_nu=U_nu X^k C^(-1),
t=tr(g_nu)=k-1 in F3.
The exact ORIGINAL ordered identity gives
q(H_d)=(U X^k C^(-1))^3=epsilon_u g_nu^3.
Cayley-Hamilton for determinant-one g_nu gives the uniform equation
q(H_d)=epsilon_u ((t^2-1)g_nu-t I).

Since t=-d modulo3, if d modulo3 is nonzero then t^2=1 and
q(H_d)=epsilon_u (d mod3) I.
If d=0 modulo3 then t=0, g_nu^2=-I, and
q(H_d)=-epsilon_u g_nu.
This has exact order4: its square is -I and it is not a scalar in SL2(F3). Hence the COMPLETE actual GT0 criterion is
q(H_d)=I iff d mod3 is nonzero and epsilon_u=d mod3.

This neither constructs an actual GT0 involution with d=0 modulo3 nor excludes one. Full GT supplies d=a_reg in Zhat^times by accepted A.100 and A.88; that input is needed only to guarantee the unit branch. The later full-dihedral correction forces original phi_D=1 but leaves canonical even k unrestricted by the projected norm, so does not settle this separate canonical branch.

## Exact two-class description of the particular kernel obstruction

Assume d mod3=delta in {+1,-1}. Let K0=ker(q) intersect Fhat', let h=[x,y], and let
b_0=1, b_1=[x,y], b_2=[x^2,y^2],
so q(b_nu)=U_nu and q(h^2)=-I. Choose e in {0,1} with (-1)^e=delta and set b=(h^2)^e b_nu.
Then q(b)=delta U_nu is the finite norm solution with the desired scalar sign.

The actual cocycle c_b=b^(-1)phi alpha(b) lies in K0. With lambda=b^(-1)u we have
c_b=lambda alpha(lambda)^(-1),
q(lambda)=(delta U_nu)^(-1)(epsilon_u U_nu)
          =delta epsilon_u I=q(H_d).
Thus q(H_d)=I iff c_b=t alpha(t)^(-1) for some t in K0, by uniqueness of the actual norm solution in Fhat'. The family t alpha(t)^(-1) is the same coboundary set as t^(-1)alpha(t).

Fix the prescribed actual word w=[v,xvx^(-1)] with v=[[x^2,y^2],z^2], whose genuine direct matrix evaluation gave q(w)=-I. It belongs to Fhat''. The word c_w=w^(-1)alpha(w) lies in K0 because beta fixes -I; it is a cocycle. It is NOT a K0 coboundary: if c_w=k^(-1)alpha(k), then
alpha(w k^(-1))=w k^(-1),
where w k^(-1) belongs to Fhat' and has q-image -I. This contradicts the accepted trivial alpha-fixed subgroup.

If q(H_d)=-I, then q(lambda^(-1))=-I, so lambda^(-1)=w k for k in K0. It follows exactly that
c_b=k^(-1) c_w alpha(k).
If q(H_d)=I, then lambda belongs to K0 and c_b is a coboundary.

Therefore this PARTICULAR actual class [c_b] is precisely either 1 or [c_w], with its selection equivalent to the remaining signed defect. This describes the relevant kernel classes of H^1(C2,K0) -> H^1(C2,Fhat'); it does NOT assert that all of H^1(C2,K0) consists of two elements. No E61/E65 transporter bit is identified.
