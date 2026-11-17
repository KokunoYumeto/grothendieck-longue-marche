# Actual signed mod-three quotient: stability, positive norm phase, and the remaining sign

This is source-ready conversation work during the execution-environment outage. Root, A and CE independently checked the complete symbolic argument. No workspace save, source hash, or new finite producer is claimed.

## Marked inputs

Fix the original q:Fhat(x,y)→G=SL2(F3), with

X=(1,2;0,1), Y=(1,0;1,1), Z=(XY)^-1=(1,1;2,0).

Let alpha be the actual full-GT negative involution, with alpha(x)=x^-1 and alpha(y)=phi^-1 y^-1 phi. Its original peripheral relation sends z to a conjugate of z^-1. This is an established relation for the ORIGINAL phi, not the desired canonical-u hexagon.

Let u∈Fhat' be the actual canonical word, with u=phi alpha(u) and u(y,x)=u(x,y)^-1. Write Phi=q(phi), U=q(u); both belong to G'=Q8. The accepted full-GT inputs give the actual k∈2Zhat and d=2k+1=a_reg∈Zhat^×. Retain

H_d=u(x,y)x^k u(z,x)z^k u(y,z)y^k.

## 1. Exact projective descent

The closed cube-normal quotient of Fhat is the full completion of

Delta=<x,y,z | xyz=1, x³=y³=z³=1>.

Put r=x and t_i=r^i(yx^-1)r^-i for i modulo3. Then y=t0r and z=t2^-1r. The y³ and z³ equations are respectively t0t1t2=1 and t1t0t2=1. Thus [t0,t1]=1 and t2=(t0t1)^-1. Conversely these equations recover the full original presentation. Hence

Delta=Z²⋊C3,

with r:t0→t1→(t0t1)^-1. The explicit finite quotients by nZ² are cofinal on the translation lattice: every finite image of Z² has a finite exponent. Therefore the full induced topology is proved and Deltahat=Zhat²⋊C3.

The cone character chi sends x,y,z to1∈C3. Original peripheral inversion gives chi alpha=-chi. Consequently Lambdahat=ker chi is alpha-stable, and 2Lambdahat is characteristic in that subgroup.

In the ORIGINAL projective q, t0 is represented by YX^-1=(1,1;1,2), and t1 by X t0 X^-1=(0,2;1,0). These are distinct commuting involutions modulo±I and generate V4; x has order3 and cycles its nonidentity elements. Thus Deltahat/(2Lambdahat) is exactly the actual A4 projective quotient, with the actual kernel. It follows that

qbar alpha=betabar qbar

for an involutory automorphism betabar of A4. No CM transporter has been chosen.

## 2. Exact signed descent

Conjugation embeds PGL2(F3), of order24, into Aut(SL2(F3)): a GL2 matrix commuting with the displayed X and Y is scalar. The natural map Aut(G)→Aut(A4) is injective. Indeed an automorphism inducing identity modulo the center differs from identity by a C2 character of G, and G_ab=C3.

Also |Aut(A4)|≤24: a chosen generating pair consisting of an order3 element and a nonidentity V4 element has at most8·3 possible images. The injections and the order24 group therefore give a unique lift beta∈Aut(G) of betabar.

The maps q alpha and beta q have the same projective images. Their difference is a continuous central C2 character of Fhat. This character is trivial on x and y: qalpha(x)=X^-1 and qalpha(y)=Phi^-1Y^-1Phi both have order3, whereas the two signed lifts of a projective order3 element have orders3 and6. Hence

q alpha=beta q

exactly. In particular beta²=1. This proves actual signed q-kernel stability; it is not inferred from arbitrarily compatible target matrices.

## 3. The actual positive Phi phase

Put J=diag(1,-1), j=AdJ, and S=(0,2;1,0). Then j inverts X,Y, AdS exchanges X,Y, and S²=-I.

Since beta(X)=X^-1, beta=Inn(X^nu)j for a unique nu∈Z/3. Composing with j fixes X; its PGL representative must commute with X, and those commuting matrices are scalar multiples of the three powers of X.

Comparing beta(Y)=Phi^-1Y^-1Phi gives

Phi X^nu ∈ C_G(Y)=<Y,-I>.

Because Phi∈Q8 and X,Y have the same generator in G_ab=C3, this yields

Phi=epsilon Y^nu X^-nu,  epsilon∈{±I}.

The actual norm equation gives beta(U)=Phi^-1U. Canonical duality gives SUS^-1=U^-1. Therefore V=U^-1S has V²=-I. Since j(S)=-S and S X^-nu=Y^-nu S,

beta(V)
=U^-1 Phi(-X^nu S X^-nu)
=-epsilon V.

But Q8^beta={±I}. To see this, choose 2s=nu modulo3, so beta is conjugate to j by X^s; a J-fixed matrix in Q8 is diagonal and hence ±I. If epsilon=-I, V would be fixed despite its order4. This is impossible. The ACTUAL constraint is thus

Phi=Y^nu X^-nu.

If U1,U2∈Q8 solve U=Phi beta(U), then U1^-1U2 is beta-fixed, hence ±I. The finite solution set has exactly two elements once actual existence is used. This does not assert two globally canonical profinite solutions.

## 4. Exact cube formula in the original q marking

Let C=XYX^-1=(0,2;1,2), so C³=I, and let kappa=AdC. Direct multiplication gives

kappa(X)=Y, kappa(Y)=-Z, kappa(-Z)=X.

Let rho:x→y→z→x. The homomorphisms q rho and kappa q differ by the central character x↦+I,y↦-I. That character vanishes on Fhat', including rho(Fhat'). Thus

q(u(y,z))=kappa(U), q(u(z,x))=kappa²(U).

Actual even k gives Z^k=(-Z)^k. Writing V0=U X^k, the ORIGINAL ordered defect satisfies

q(H_d)=V0 kappa²(V0) kappa(V0)=(V0 C^-1)^3.

For chi:G→C3 with chi(X)=chi(Y)=chi(C)=1,

chi(V0 C^-1)=k-1=-d mod3.

The accepted full-GT unit theorem for d implies that this is nonzero. Therefore g=U X^k C^-1 lies outside Q8. If its trace were zero, Cayley-Hamilton would give g²=-I, forcing its order to be a power of2 and placing it in Q8. Thus t=tr(g)=±1. Cayley-Hamilton now gives

g³=(t²-1)g-tI=-tI.

Consequently q(H_d)=-tr(U X^k C^-1)I is a precise central sign, not an evaluated sign.

## 5. The explicit remaining bit

Define U_nu=Y^-nu X^nu. This belongs to Q8 and satisfies both norm and duality:

beta_nu(U_nu)=X^nu Y^nu X^nu,

Phi beta_nu(U_nu)=Y^(2nu)X^nu=Y^-nu X^nu=U_nu,

S U_nu S^-1=X^-nuY^nu=U_nu^-1.

The two-solution classification therefore writes the ACTUAL U uniquely as

U=epsilon_u Y^-nu X^nu, epsilon_u∈{±1}.

Over F3, with nu and k reduced modulo3,

U_nu=(1,-nu;-nu,1+nu²),
X^k=(1,-k;0,1),
C^-1=(2,1;2,0).

Their product has trace 2-3nu-2k=k-1. Hence

q(H_d)=epsilon_u (d mod3) I.

Since the top-left entry of U_nu is1, epsilon_u is exactly the top-left entry of the ACTUAL U. The remaining condition is

q(H_d)=I  if and only if  epsilon_u=d mod3.

Both finite signs satisfy the preceding norm and duality equations. Neither is selected by these calculations.

## 6. Exact remaining kernel-cocycle gate

This paragraph additionally uses the previously established uniqueness of the actual norm solution in Fhat', equivalently the relevant trivial actual alpha-fixed subgroup. It is not inferred from the finite equations.

Let K0=ker(q)∩Fhat'. With h=[x,y], choose b_nu=1,[x,y],[x²,y²] for nu=0,1,2 respectively. Their original q-images are U_nu, and q(h²)=-I. Put delta=d mod3∈{±1}, choose e∈{0,1} with (-1)^e=delta, and set

b=(h²)^e b_nu.

Then q(b)=delta U_nu is exactly the finite norm solution for which q(H_d) would equalI. The actual word

c_b=b^-1 phi alpha(b)

lies in K0 and satisfies c_b alpha(c_b)=1. The remaining sign equality is equivalent to

c_b=t alpha(t)^-1 for some t∈K0.

Indeed b t then solves the original norm equation and equals the actual u by the stated uniqueness; conversely t=b^-1u gives the required coboundary. Every phi and alpha in this criterion is the actual original one.

The separately prescribed word w with q(w)=-I also gives an actual nontrivial obstruction: c_w=w^-1 alpha(w) lies in K0 and is a cocycle. If it were a K0 coboundary b^-1alpha(b), then w b^-1 would be alpha-fixed with q=-I, contradicting the same fixed-subgroup theorem. This shows why the finite central fixed point need not have a fixed lift. It does not compute the class of the separate candidate c_b.

## 7. Scope

The proof establishes actual signed kernel stability, excludes the negative Phi phase, gives the exact original-q cube and scalar criteria, and states a precisely typed remaining kernel-lifting problem. It does not identify the scalar with either E61/E65 signed transporter bit. Their original defining displays must be read before any comparison. It proves neither actual CM parity, Delta=0, nor H_d=1 in the original free profinite group.

The square-normal word witness is an obstruction to deductions from quotient containments, not a realization as a canonical defect. No finite target search, unobserved computation, or saved artifact is part of this original conversation proof.
