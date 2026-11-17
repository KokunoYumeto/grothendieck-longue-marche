# A uniform actual P4 affine-character boundary for the pentagon

Cycle30 late research, complete proof for independent review. This is not a finite-head or source-word census. It identifies what the full pentagon can detect after passing to a finite elementary-abelian two-kernel with odd abelian head. No conclusion about the full canonical parameter or its nonlinear cusp is inferred.

## 1. Actual source, words, and claim

Use the actual pure generators

    (a,b,c,d,e,f)=(A12,A13,A23,A14,A24,A34)

and the Fadell--Neuwirth decomposition P4=F(d,e,f) semidirect P3. The actual pure actions, in the retained conventions, are

    Ad(a^-1): d -> Ad(de)d, e -> Ad(d)e, f -> f;
    Ad(b^-1): d -> Ad(df)d, e -> Ad([d,f])e, f -> Ad(d)f;
    Ad(c^-1): d -> d, e -> Ad(ef)e, f -> Ad(e)f.            (1)

In P3, Z=abc is central and P3=F(a,c) times <Z>, with b=a^-1 Z c^-1. Composing the three displayed actions gives

    Ad(Z^-1)|F(d,e,f)=Ad(def).                            (2)

These are the same exact source and marking retained in the earlier A5 pentagon note; no finite classification from that note is used here. The short accompanying free-word checker verifies (2) on all three generators using (1), without any target enumeration.

Let k be any field and Aff1(k)=k semidirect k^times, with multiplication

    (v,t)(w,s)=(v+t w,t s).

CLAIM. Every homomorphism P4->Aff1(k) with nonabelian image factors through one of the following five ACTUAL free-two quotients, as specified by its six images:

    (i)   a=b=d=1, c e f=1;
    (ii)  a=c=e=1, b d f=1;
    (iii) b=c=f=1, a d e=1;
    (iv)  d=e=f=1, a b c=1;
    (v)   a=f, c=d, b=(df)^-1, e=(fd)^-1.                (3)

The first four forget a strand and remove the remaining central twist; the fifth is the marked sphere-infinity quotient. Each is also verified directly by substituting its two free generators in (1) and the P3 relations. Below is a complete algebraic proof of exhaustion, valid over every field.

## 2. Reduction to a nonabelian fiber

The centralizer of any nonidentity element of Aff1(k) is abelian: a nonzero translation has the translation subgroup as centralizer; an element of slope different from1 has a unique fixed point and its centralizer is the multiplicative group about that point. Consequently the centralizer of a nonabelian subgroup is trivial.

Write D,E,F for the three fiber images. If their subgroup is nontrivial abelian, every pure action in (1) fixes each image, because it preserves the abelianization of the fiber. Thus a,b,c centralize that nontrivial abelian subgroup. The whole image lies in the abelian centralizer of one of its nonidentity elements, contrary to the hypothesis. If the fiber image is trivial, the map factors through P3; its central Z must have trivial image in a nonabelian affine group. This is case(iv).

It remains to assume that <D,E,F> is nonabelian. Put P=DEF. By (2), the images of Z and P^-1 induce the same conjugation on this fiber. Their quotient centralizes a nonabelian subgroup, hence

    Z=P^-1.                                              (4)

In particular both a and c commute with P.

## 3. The two exact rank-one Artin matrices

Write

    D=(v1,t1), E=(v2,t2), F=(v3,t3),
    rho=t1 t2 t3, v=(v1,v2,v3)^T,
    p=(1-t1,1-t2,1-t3)^T.

The translation of P is

    L(v)=v1+t1 v2+t1 t2 v3, and L(p)=1-rho.               (5)

Evaluating the first and third actions of (1) on translation coordinates gives

    A=I+u_A ell_A,  u_A=(t1,-1,0)^T,
                      ell_A=(t2-1,1-t1,0);
    C=I+u_C ell_C,  u_C=(0,t2,-1)^T,
                      ell_C=(0,t3-1,1-t2).              (6)

Both ell_A and ell_C kill p; both u_A,u_C lie in ker L. These formulas follow directly from conjugation

    Ad(w,q)(v,t)=((1-t)w+q v,t).

If the affine image of a is (w_a,a0), relation(1) says

    A v=a0^-1 v-a0^-1 w_a p,                             (7)

and similarly for c. The inverse on the base generator is important.

Set q=t1t2 and r=t2t3. On u_A,u_C the two matrices have coefficients

    A: [[q, t2(1-t1)],[0,1]],
    C: [[1,0],[1-t3,r]].                                 (8)

Their two fixed-vector equations have determinant

    (q-1)(r-1)-t2(1-t1)(1-t3)
       =(t2-1)(rho-1).                                   (9)

No value of a root of unity or finite residue is chosen in these identities.

## 4. Boundary with slope rho different from1

Conjugate the entire affine image so that P=(0,rho), possible because rho differs from1. Its centralizer is the diagonal torus, so w_a=w_c=0. Equation(5) gives L(v)=0. Since rho differs from1, u_A,u_C form a basis of ker L: the only possible relation modulo the boundary vector would force rho=1, or equivalently their two independent columns span this two-dimensional plane. Write

    v=xi u_A+eta u_C.

It is nonzero, since otherwise the fiber image would be diagonal and abelian. Equations(7)--(8) say it is a simultaneous eigenvector of A,C.

If eta=0, then C u_A=u_A+(1-t3)u_C forces t3=1. Also v3=0, so F=1. If xi=0, the A equation forces t1=1 and v1=0, so D=1.

If both coefficients are nonzero, the second coordinate in the A equation and first in the C equation force both eigenvalues to be1. Equation(9) then gives t2=1. The two remaining equations give xi=eta: at least one of t1,t3 differs from1 since rho differs from1. Hence v2=-xi+t2 eta=0, and E=1.

Thus this entire case has one of D,E,F equal to1.

## 5. Boundary with slope rho=1

First suppose P is a nonzero translation. Its affine centralizer consists of translations, so a0=c0=1. Equations(6)--(7) become

    u_A ell_A(v) in k p, u_C ell_C(v) in k p.              (10)

Not all t_i are1, since that would make the whole fiber a translation group. If none is1, neither u_A nor u_C is proportional to p. Thus both ell_A(v) and ell_C(v) vanish. The two rows are independent (their first and last nonzero entries suffice), and their common kernel is k p. This would give L(v)=0 by rho=1, contradicting the nonzero boundary translation.

Some t_i is therefore1. If t3=1, then t1t2=1 and t1,t2 differ from1. The vector u_C is not proportional to p, so ell_C(v)=(1-t2)v3=0, giving F=1. If t1=1, the symmetric first-row argument gives D=1. If t2=1, then t1t3=1 with both different from1; u_A is not proportional to p, and ell_A(v)=(1-t1)v2=0 gives E=1. More than one t_i equal to1 would force all of them equal to1, already excluded.

Finally suppose P=1. Then E=(FD)^-1. The actions of a^-1 and c^-1 in (1) are respectively conjugation by F^-1 and D^-1 on the ENTIRE fiber. The nonabelian fiber has trivial centralizer, so a=F and c=D. Equations(4) and b=a^-1 Z c^-1 give b=(DF)^-1. This is case(v).

## 6. Finish the exhaustive factorization

If F=1, the c and b actions in (1) are the identity on the nonabelian fiber, so c=b=1; the a action is conjugation by DE, giving a=(DE)^-1. This is case(iii).

If D=1, the a and b actions are identity and c=(EF)^-1, giving case(i). If E=1, the a and c actions are identity and b=(DF)^-1, giving case(ii). Triviality of the fiber centralizer justifies each equality, not just equality of conjugation classes. Together with Sections2--5 this proves(3) completely.

## 7. The actual pentagon becomes duality in every affine character

Let u in the commutator subgroup of the full free profinite group satisfy the exact swap duality u(y,x)=u(x,y)^-1. For a finite affine target, the actual marked pentagon is

    u(a,ce) u(bc,f)
       =u(c,f) u(ab,ef) u(a,c).                           (11)

An abelian target makes every u-value1. For each of cases(i)--(iv), substituting(3) into(11) leaves the same single u-value on both sides, with all other values on cyclic pairs and hence1. Explicitly the surviving value is respectively u(c,f), u(b,f), u(a,e), u(a,c).

For case(v), the first two argument pairs are (f,f^-1) and (f^-1,f), and the middle right pair is (d^-1,d^-1). Those three values are1. The remaining equation is

    1=u(d,f)u(f,d),                                      (12)

which is exactly the given full duality. Thus every finite affine-character evaluation of the actual P4 pentagon is already satisfied by ANY such u. The conclusion is about these evaluations, not about the pentagon in the full P4.

## 8. Entire elementary-two module over every odd abelian head

Let Q be a finite abelian group of odd order and V a finite F_2[Q]-module. The result extends from one character to ANY continuous homomorphism

    P4-hat -> V semidirect Q.                             (13)

Choose a finite field containing all roots of unity of exponent(Q). Each Q operator has square-free minimal polynomial dividing X^N-1, since N is odd, and the operators commute. Successive eigenspace decompositions simultaneously diagonalize V after that scalar extension. Every scalar coordinate of every character space defines an affine homomorphism from V semidirect Q to Aff1(k). These coordinates separate V.

Each u-value in(11) has trivial Q head, since Q is abelian and u is a commutator word. Its pentagon discrepancy therefore lies in V. Section7 kills every separating affine coordinate, so the entire discrepancy is1 in(13). This retains every character, not merely selected roots or bounded heads. Finite extensions with elementary abelian two-kernel and odd abelian quotient also split: the same finite homogeneous-cochain averaging proved internally in B143 gives H^2(Q,V)=0 because multiplication by the odd index |Q| is invertible on V. Thus the same conclusion is independent of a chosen splitting.

## 9. Consequence and limits for the actual Main-A gate

This supplies a uniform boundary for the proposed full-character metabelian pentagon route. At the first elementary-two layer over ANY finite odd abelian head, the complete pentagon adds no condition to exact swap duality. The proof used the actual P4 source and complete pure actions; it did not replace the pentagon by a finite collection of tests or appeal to a prounipotent result at roots of unity.

Consequently the all-odd-head coefficient gate cannot be closed merely by imposing that first-layer pentagon after the three-module common-word/duality equations. Any successful use of the full pentagon must retain further nonlinear kernel information, a nonabelian head, or another actual marked compatibility not lost in this quotient. The global canonical involution equation can also carry information not visible in those linearizations.

Nothing here constructs a GT0 or GT counterexample, realizes arbitrary coefficients as canonical data, proves the missing a_reg=d, or annihilates Omega. Both main decisions remain Open. All30 frozen formal sources are unchanged. The only new execution is the three-generator free-word verification of (2); its producer, stdout, stderr and exact JSON are preserved.
