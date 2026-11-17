# The actual pentagon hexagon vanishes in every signed congruence quotient

First saved on 17 November 2026 after the scheduled10:49:30 review and before the sole checkpoint32 capture. This is a new complete research proof, not a recovered historical file. It strengthens the finite-image conclusion of actual_affine_pentagon_signed_hexagon32_recovered.md (SHA256 9bcb84e25041c47d7b0b97be37a56db0c654251a7c74cc585c10e364c87ae48c). The611-page formal paper remains unchanged; this result is not yet promoted to a numbered statement.

## Exact theorem and hypotheses

Let F be the free profinite group on x,y. Let u lie in its closed commutator subgroup and satisfy full duality u(y,x)=u(x,y)^-1 and the original marked sphere pentagon

u(a,ce)u(bc,f)=u(c,f)u(ab,ef)u(a,c).

Define k by the actual universal dihedral evaluation u(s,sT)=T^k, with s^2=1 and sTs=T^-1. Since the derived subgroup of this profinite dihedral group is 2 Zhat, k belongs to 2 Zhat. Put d=1+2k and retain the original ordered word

H_d=u(x,y)x^k u(z,x)z^k u(y,z)y^k,  z=(xy)^-1.

For every positive integer m let q_m be the continuous homomorphism to SL2(Z/m) specified by the reductions of

X=[[1,2],[0,1]],  Y=[[1,0],[-2,1]].

Then q_m(H_d)=I for EVERY m, including even and nonreduced moduli. Equivalently H_d lies in the kernel of the continuous specified signed representation F -> SL2(Zhat). No norm equation is required in this theorem. Actual canonical words of full-GT negative involutions satisfy the required pentagon by A37. A general GT0 canonical word is not supplied with that additional hypothesis.

## 1. The exact uniform affine input

The complete preceding source checks the original A96 sphere presentation over every R=Z/m. Its six relations are reversibly equivalent to

[A,f0]=[C,d0]=[Af0,P]=[Cd0,P]=[PA,d0]=[CP,f0]=1,

with original a=Af0, c=Cd0, b=a^-1 P^-1 c^-1, e=d0^-1 P f0^-1. In R^2 semidirect SL2(R), with multiplication (t,M)(s,N)=(t+Ms,MN), put v=e1,w=e2 and assign

P=(0,-I), A=(-2v,I), C=(-2w,I),
f0=(2v,X), d0=(2w,Y).

All six relations hold: Xv=v, Yw=w, a=(0,X), c=(0,Y), and the last two commutations reduce to (I-Y)(2v)=4w and (I-X)(-2w)=4v. No division by2 occurs. The exact five pairs are

(a,ce): ((0,X),(2(v-w),-X^-1)),
(bc,f0): ((0,-X^-1),(2v,X)),
(c,f0): ((0,Y),(2v,X)),
(ab,ef0): ((0,-Y^-1),(-2w,-Y^-1)),
(a,c): ((0,X),(0,Y)).

For the first two pairs, the heads commute and preserve the direct summand Rv. On the quotient affine line by Rv, one argument is identity. Each commutator-word value is consequently a translation in Rv. This quotient is used only inside those pair subgroups, not as a quotient of the whole affine target.

Put U=u(X,Y). The third pair is the simultaneous translation(-w) conjugate of (Y,X), so its value is (-w+U^-1 w,U^-1), by duality. For the fourth pair remove the common genuinely commuting Y^-1 decoration. The remaining involutions are (0,-I),(-2w,-I), with ordered product (2w,I); the universal dihedral evaluation is therefore (2k w,I). The fifth pair has value (0,U). The ordered pentagon gives

(ell v,I)=(-w+(1+2k)U^-1 w,I).

The second coordinate of U^-1 w is U11 for every determinant-one2x2 matrix. Therefore

d U11=1 in EVERY Z/m.                                      (1)

The original integral S=[[0,-1],[1,0]] interchanges X and Y by conjugation. Duality gives SUS^-1=U^-1. The two determinant-one inverse formulas imply

U12=U21,                                                  (2)

without division. These are exactly the earlier proved uniform identities. In particular d is a full profinite unit and, in the inverse limit,

U=[[d^-1,b],[b,d(1+b^2)]]

for the actual entry b. The proof below needs only (1) and (2).

## 2. An integral cyclic conjugator

Introduce the integral matrix

J=[[0,-1],[1,-1]],  J^-1=J^2=[[-1,1],[-1,0]].

Direct multiplication over Z gives J^3=I and, with

Z=(XY)^-1=[[1,-2],[2,-3]],

the three identities

J X J^-1=Y,  J Y J^-1=-Z,  J(-Z)J^-1=X.                  (3)

These hold in every Z/m. This J reduces modulo3 to the earlier C0=XYX^-1, but J=XYX^-1 is NOT an integral identity and is not used. J need not lie in the image of q_m; conjugation in the displayed ambient matrix group is sufficient.

Let rho be the actual order-three free-group automorphism x->y, y->z, z->x. Put kappa=Ad(J) after reduction. On the two original generators, q_m rho differs from kappa q_m by the central character x->I,y->-I. Such a continuous character vanishes on F'. Since rho preserves F', we obtain

q_m(u(y,z))=kappa(U),
q_m(u(z,x))=kappa^2(U).                                   (4)

Also kappa(X)=Y and kappa^2(X)=-Z. The actual exponent k is even in Zhat, so (-Z)^k=Z^k. This is an identity of profinite powers in the finite group: the central factor -I has order dividing2. There is no choice of a single ordinary integer representative for k.

## 3. Preserve the actual ordered hexagon

Set V=U X^k. From (3)--(4) and even k,

q_m(H_d)=V kappa^2(V) kappa(V)
        =V (J^-1 V J)(J V J^-1)
        =V J^-1 V J^2 V J^-1
        =(V J^-1)^3,                                    (5)

using J^2=J^-1. This is equality in the original printed order, not merely equality up to conjugacy. No commutation between U and J is assumed.

## 4. Exact trace over an arbitrary modulus

The integer identity X^n=I+2n E12 extends continuously to the actual profinite k. Thus

X^k J^-1=[[-1-2k,1],[-1,0]]=[[-d,1],[-1,0]].

Write U=[[a,b],[b,c]], by (2). For g=U X^k J^-1,

g=[[-da-b,a],[-db-c,b]],
trace(g)=-da=-1,  det(g)=1,                              (6)

where (1) gives da=1. All calculations are exact in Z/m. Cayley--Hamilton over a commutative ring gives

g^2+g+I=0.

Multiply by g-I; there is no cancellation or division:

g^3-I=0.                                                (7)

Combining (5) and (7) proves q_m(H_d)=I for every m.

The compatible finite evaluations define the continuous map q:F->SL2(Zhat), with the same specified X,Y marking. Its kernel is the intersection of the kernels of all q_m. Therefore

H_d belongs to ker(q).                                  (8)

This proves vanishing in the full signed congruence image.

## 5. Precise remaining gates

Equation (8) strengthens the earlier original signed q3 and q12 conclusions. It does not assert ker(q)=1, and it therefore does not prove H_d=1 in the original free profinite group. It does not prove Omega_alpha=1, the actual involution conjugacy, or the comparison with either separately normalized E61/E65 CM character. The full-word/congruence-kernel distinction must be retained.

The affine proof and this integral conjugator are norm-free. Only the canonical full-GT specialization uses A37 to supply the pentagon for the actual canonical word. No conclusion is supplied for arbitrary GT0 canonical data without that hypothesis.

## 6. Independent symbolic audits and execution scope

Root derived the integral-conjugator strengthening while the single scheduled32 driver was waiting for the actual size estimate. CE and DE independently checked every integral matrix, the original cyclic order, the central-character restriction to F', continuous even powers, the trace formula, and Cayley--Hamilton over every modulus. Both complete conversation audits returned PASS. CE explicitly noted that the integral J is not XYX^-1, although they agree modulo3; this source retains that distinction. DE explicitly noted that J need not lie in the image of the free group.

Those audits used no tools, mathematical producer, target search, or filesystem operations. No new mathematical execution is claimed. This source is the first saved complete text of the strengthened theorem, with a fresh byte identity. The formal paper and its already reviewed PDF have not been modified.
