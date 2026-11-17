# Uniform obstruction to extending the actual prefix basis across an ordinary regional section

DE, checkpoint24. Complete independent proof and literal finite check: PASS. The group is the actual B112 regional annular bad vertex BEFORE the two cross relations. This result does not identify the actual annular quotient's centralizer.

## 1. The exact region and prefix change

Use C for the adapted cone, U=(a,b,d,e), B=CbC, h for the actual fixed-source base lift and k=f^{-1}h for the actual far/base lift. The complete regional presentation consists of C²=1, six generic relations

  [h,C]=1,  h k h^{-1}=C k C,  [k,U]=1 (four U),

and the ten actual node relations

  [U,CUC]=1 (four U),
  [a,b]=[CaC,d]=[CaC,e]=[d,CeC]=1,
  [b,h d h^{-1}]=[b,h e h^{-1}]=1.

All sixteen plus the cone square are checked directly from the stable actual annular_neck_presentation23.json, not from a simplified subset. The assignments b=CBC and h=fk are retained literally.

The actual common neck is K=F(a,B,d,e,f), with ordinary-cut basis

  O1=aBa^{-1}, O2=a, O3=fde d^{-1}f^{-1}, O4=d, O5=d^{-1}fd.

Define theta on this free group by theta(O_i)=P_i=O1...Oi. This is an automorphism: the inverse in the O marking sends O1 to O1 and O_i to O_(i-1)^{-1}O_i for i>1. The actual O/K inverse substitutions and both directions of all five theta images are independently verified. In particular,

                    theta(a)=theta(O2)=O1 O2=aB.

This is theta, the triangular PREFIX automorphism; it is distinct from the actual reflection eta.

## 2. One actual finite quotient of the whole region

Let V be the twelve-dimensional vector space over F_2 with basis e_(U,j), U=a,b,d,e and j=1,2,3. Let S3 act only on j, separately within each named family, and put Q=V semidirect S3. Use the multiplication

 (v,p)(w,q)=(v+p.w,pq).

Define

  U -> e_(U,3),   k -> (12),   C -> (23),
  h -> (23),     f -> (23)(12),     z=C h ->1.

Thus B=CbC maps to e_(b,2). These assignments satisfy the entire regional presentation. The six generic relations hold because (12) fixes position3, h=C and C²=1. Every one of the ten node relations is a commutator between two vectors in the abelian V, including the h-translated ones. The separate exact evaluator confirms all seventeen original words. The map is surjective: C,k generate S3 and their action moves each of the four U lamps through all three positions. Its order is 2^12*6, but no enumeration of that group is used.

The image v of theta(a) is e_(a,3)+e_(b,2). For every vector m and every p in S3,

 (m,p)(v,1)(m,p)^{-1}=(p.v,1).

The vector m cancels identically. As the two nonzero lamps have different family names, p.v=v forces p to fix position3 and position2 separately. Hence p=1. Consequently the target centralizer of v is EXACTLY V.

It follows at once that no conjugate of the image of k centralizes v. More generally no element with any nonidentity permutation component does, irrespective of its lamp-vector correction.

## 3. The geometric parity identity excludes every ordinary section

Let epsilon:R->C2 be the actual orientation character of the ordinary double cover, and let beta:R->Z be the actual q0 base winding. In the common K,C,k generators, epsilon(C)=1 and epsilon is zero on K,k; beta(k)=1 and beta is zero on K,C. In particular f is an ordinary fiber word, h=fk is an ordinary base lift, and z=C h has both characters odd.

The permutation SIGN of the finite quotient is precisely

                  sign rho = epsilon + beta modulo2.

This is checked on every actual generator and respects every original regional relator. Therefore an ordinary element of odd base winding has an odd permutation, necessarily a transposition. It cannot centralize theta(a).

Suppose a homomorphism Phi:R->R restricts on K to the literal theta and sends k to any ordinary element of odd q0 winding. The existing relation [k,a]=1 would force [Phi(k),theta(a)]=1, contradicting the finite quotient. Thus NO such extension exists. In particular theta cannot be extended by any genuine alternative ordinary degree+1 or degree-1 base section. This excludes arbitrary retained-fiber corrections as well as graph-kernel corrections; it is stronger than excluding changes of whisker or conjugates of k.

The identical contradiction applies to continuous homomorphisms of the full profinite completion: the one finite quotient, orientation character and base winding modulo2 all extend continuously. An ordinary image with odd base winding still has a transposition head.

## 4. Exact scope and the surviving geometric task

The prefix change remains a valid free-basis change of K and a valid substitution in a presentation. This theorem does not say that the regional graph presentation cannot be rewritten in prefix variables with its relations transformed. It rules out the specific stronger requirement that this prefix automorphism extend to the original regional group while its far base generator remains an ordinary odd-degree base lift.

Thus the signed-permutation prefix edge basis does not by itself produce a simultaneous regional graph-coordinate change preserving the actual section. Any successful fine-kernel comparison must retain transformed regional relations and both actual cross cells, or use another structural argument. The finite quotient is a quotient of the regional group; no extension to the full cross quotient has been assumed and no post-cross-quotient centralizer or source nonmembership is deduced.

## 5. Independent evidence

The independent producer check_prefix_base_obstruction24.py imports no CE producer or group library. Its genuine stdout/stderr and prefix_base_obstruction_independent24.json retain all seventeen literal words, all finite images, the five exact theta images and inverse images, and the three possible transposition support differences. The all-vector and all-ordinary-section conclusions are the symbolic identities in Sections2–3, not an inference from those three printed cases.

A independently checked the actual character typing and the all-section conclusion. CE independently constructed the same whole regional quotient and also checked the raw transported node data. MainA and MainB remain Open.
