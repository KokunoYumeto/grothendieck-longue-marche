# The canonical hexagon in every profinite involutory-generator quotient

## Status and hypotheses

This source-ready proof was developed and fully reviewed in the conversation during an execution-environment outage. Root, A, CE and DE independently checked the complete argument. No filesystem save, source hash, paper promotion, or workspace execution was claimed at that stage. Earlier external-dihedral and class-two constructions remain separate preserved arguments.

Let alpha=(-1,phi) be the actual full-GT involution, and let u∈Fhat(x,y)' be its fixed canonical word satisfying u=phi·alpha(u). Use the actual duality u(y,x)=u(x,y)^-1 and the full profinite canonical pentagon established in A37. In the original A45 dihedral marking x→a,y→aT, write u→T^k, where k∈2Zhat and d_alpha=2k+1. Put z=(xy)^-1 and retain the original ordered defect

H_d=u(x,y) x^k u(z,x) z^k u(y,z) y^k.

The conclusion is H_d(A,B)=1 for every profinite group L, every A∈L with A²=1, and every B∈L. Equivalently, in the ORIGINAL Fhat(x,y),

H_d ∈ clnorm(x²) ∩ clnorm(y²) ∩ clnorm(z²).

This is not a proof that H_d=1 in the unrestricted free profinite group or that this intersection is trivial. The full canonical pentagon is an essential hypothesis.

## 1. Original presentation and marking

The actual A96 sphere quotient G=P4/<Delta4²> has the original generators P,A,C,d,f and the six actions

D(P)=C^-1 P C,
D(A)=C^-1 P^-1 C P A,
D(C)=C,

F(P)=A^-1 P A,
F(A)=A,
F(C)=C P A^-1 P^-1 A,

where D and F denote conjugation by d and f. The original pure marking is

a=Af, c=Cd, b=a^-1 P^-1 c^-1, e=d^-1 P f^-1.

The actual canonical pentagon in this marking is

u(a,ce)u(bc,f)=u(c,f)u(ab,ef)u(a,c).

P is the unrestricted original generator. No cyclic root, relative completion, class-two approximation, or change of base marking is used below.

## 2. A genuine internal wreath target

For the moment let A,Y be elements of an arbitrary profinite group L with A²=1. Define

T=AYA,
B=TAT^-1=AYA Y^-1 A,
W=AY.

Thus A and B are involutions. Form the profinite wreath product

Q=(L×L)⋊C2,

where the nonidentity element f swaps the two factors. In H=L×L put

Ahat=(A,A),
P=(Y,T),
C=(A,B),

and define

d=(T^-1,T)f.

Because swapping (T^-1,T) gives its inverse, d²=f²=1. Conjugation by these two actual elements acts on H as

F(h1,h2)=(h2,h1),

D(h1,h2)=(T^-1 h2 T, T h1 T^-1).

These maps and the semidirect product are continuous.

## 3. All six original relations and all four squares

Direct multiplication, using only A²=1, gives

F(P)=(T,Y)=Ahat P Ahat,
F(Ahat)=Ahat,
F(C)=(B,A)=C P Ahat P^-1 Ahat,

D(P)=(T,T Y T^-1)=C P C,
D(C)=(A,B)=C,
D(Ahat)=(A Y^-1 A Y A,B)=C P^-1 C P Ahat.

For example T^-1BT=A, TAT^-1=B, and BTB=TYT^-1. Also

P Ahat P^-1=(YAY^-1,B),
P^-1 C P=(Y^-1AY,A).

These verify exactly the six original action rows, with Ahat^-1=Ahat and C^-1=C. The defining presentation therefore gives a genuine homomorphism G→Q, extending continuously to Ghat.

Define a=Ahat f and c=C d, using the same original marking. Since F fixes Ahat and D fixes C, one has

a²=c²=d²=f²=1.

This is a legitimate quotient evaluation of the original group. No relation is silently imposed on the original source itself, and P is neither deleted nor centralized.

## 4. Exact reduction of the full canonical pentagon

In any four-square quotient of the original marked group, put S=CP and r=cf. The six relations show:

f commutes with Ahat and S;
a commutes with Ahat and P;
c commutes with P and S;
P commutes with a and c.

The inverse substitutions reduce literally to

ce=Sf,
bc=P^-1a,
ab=P^-1c,
ef=Sc.

For a word in the closed commutator subgroup of Fhat(x,y), factors commuting with both substituted arguments contribute only its two zero abelian exponents and therefore cancel. This follows first for ordinary commutator words and then by continuity for the actual profinite u. Consequently

u(a,ce)=u(Ahat,S),

u(bc,f)=u(P^-1,Ahat)=u(Ahat,P^-1)^-1,

u(ab,ef)=u(P^-1,S).

The two remaining pairs consist of involutions. Their evaluations are therefore the SAME actual universal dihedral powers

u(c,f)=r^k,
u(a,c)=(ac)^k.

Finally ac=Ahat r^-1 in exactly that order. Thus the actual full pentagon gives the exact nonlinear identity

u(Ahat,S)u(Ahat,P^-1)^-1
=
r^k u(P^-1,S)(Ahat r^-1)^k.                 (1)

No abelianization, unknown Hall correction, first-layer substitution, or new dihedral parameter is used.

## 5. Every factor of the reduced identity is in H

In the explicit wreath target,

S=CP=(W,W),

r=cf=Cdf=C(T^-1,T)=(W^-1,W),

ac=Ahat r^-1=(Y,T^-1).

In particular every factor of (1), including its profinite powers, lies in the closed subgroup H=L×L. Therefore the ordinary first-factor projection H→L is a genuine continuous homomorphism on the entire identity. It gives

u(A,W)u(A,Y^-1)^-1
=
W^-k u(Y^-1,W)Y^k.                         (2)

No homomorphism on the reflection coset is asserted or needed. In this internal realization no auxiliary procyclic rotation, finite-order lifting, or norm approximation is required.

## 6. The original ordered hexagon

Since A²=1,

Z=(AW)^-1=Y^-1.

Actual duality rewrites (2) as

u(A,W)u(Z,A)
=
W^-k u(W,Z)^-1 Z^-k.

Right-multiply by Z^k u(W,Z)W^k. The adjacent powers cancel in the displayed order. Since the actual k is even, A^k=1. The resulting identity is precisely

u(A,W) A^k u(Z,A) Z^k u(W,Z) W^k
=
H_d(A,W)
=
1.

No noncommuting factors have been reordered.

For a desired pair (A,B) in any profinite group with A²=1, run the construction with Y=AB. Then W=AY=B. Hence H_d(A,B)=1 for every such pair. This does not require a Nielsen automorphism of an arbitrary profinite group with additional relations.

## 7. Exact closed normal kernels and cyclic transport

Take L=C2(A) amalg Zhat(B), the full free profinite product. The presentation map from the original Fhat(x,y) has kernel exactly clnorm(x²), so the original H_d belongs to that subgroup.

Let rho be the actual free-basis automorphism cycling x→y→z→x, where z=(xy)^-1. Write

B1=u(x,y)x^k,
B2=u(z,x)z^k,
B3=u(y,z)y^k.

Then H_d=B1B2B3 and

rho(H_d)=B3B1B2=B3 H_d B3^-1.

Applying rho to the first square-normal containment and using closed normality gives H_d∈clnorm(y²). Repeating gives H_d∈clnorm(z²). This proves membership of the SAME original word in all three closed normal subgroups. It does not exchange quotient images and intersections.

## 8. Scope and a preserved obstruction

This theorem strengthens the earlier peripheral-cover Frattini containments and subsumes vanishing in the involutory-core regular class-two models. It does not evaluate the unrestricted nonlinear H_d or Omega, prove a GT0 pentagon, determine actual CM parity, or resolve Main A or Main B.

The three square-normal kernels have a nontrivial common part. A separate, single prescribed word

v=[[x²,y²],z²],
w=[v,x v x^-1]

lies in all three by normality and belongs to F''. Its genuinely executed value in the fixed q3 representation X=(1,2;0,1), Y=(1,0;1,1) is -I. That computation and its exact producer are separately retained in the tool transcript and in-memory records pending filesystem recovery. The word is not claimed to arise as a canonical H_d.

All source and computation statements remain subject to exact saved-byte binding after execution access returns.
