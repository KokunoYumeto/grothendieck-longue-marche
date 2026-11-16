# Proposed next result: nonzero s-torsion cohomology and its exact frame correction

**Status:** research proof under independent review during checkpoint05 freeze. It has not been inserted in the formal source or register. The exact scripts check_heisenberg7_head.py and check_heisenberg7_frame.py pass. The claim, if accepted, remains a specified quotient-image construction, not a full involution.

## The retained odd nilpotent head

Use symmetric Heisenberg coordinates over F7:

    (x,y,z,d)(u,v,w,e)
      =(x+3^d u, y+3^(-d)v,
        z+w+(x 3^(-d)v-y 3^d u)/2, d+e),

with d modulo6. Let H=Heis7 semidirect C6, order2058. The actual Pi quotient is

    s=(0,0,0,3), r=(1,1,2,2), tau=(6,6,2,5).

The exact head certificate enumerates all2058 generated elements, verifies s²=r³=1, and computes tau^6=(0,0,6,0). The s-centralizer is Z(Heis7) times C6, of order42. The head is characteristic: it is the quotient of Pi by gamma3(Pi') (Pi')^7, since Pi' is full free profinite of rank2 and its maximal class-two exponent-seven quotient is Heis7. The displayed quotient has the full required order.

Genuine c acts by

    c_H(x,y,z,d)=(4y,2x,-z,-d).

This is an involutory automorphism fixing s and sending r to s r^(-1)s. The head lies in the relative pro-seven tower over the congruence subgroup Pi', so the retained h_C is identity on H. The congruence-kernel image is all Heis7: C6 is congruence, and a solvable congruence quotient cannot retain a prime7 factor, as proved in A.49.

The retained s-frame beta has trivial Pi-abelianization. Indeed A.31's arithmetic sigma has complete Kummer character of2 equal zero, hence rho_sigma=0 in the verified frame formula; A.33 retains its congruence frame images, including the congruence C6 abelian quotient. Since h_C is identity on H, beta_H centralizes s. Therefore

    beta_H=z^j for some j in F7.

No particular value of j is assumed or selected. The correction below works for all seven possibilities.

## The Schrödinger module and the nonzero torsion class

Let k=F8 with primitive seventh root zeta. On k^7, with basis indexed by F7, define

    rho(x,y,z,d)e_j
      =zeta^(-z+xy/2+y 3^d j) e_(3^d j+x).

The action is verified exactly over F8. As an F2 module V+ has dimension21. Its nontrivial central character makes it irreducible; its commuting field is F8. Let V- be the c_H twist. The central characters are the two Frobenius orbits of nontrivial seventh roots, so these are distinct irreducible F2 modules. They pair by the nondegenerate symmetric Fourier matrix

    B(v,w)=sum_(i,j) v_i zeta^(-2ij) w_j.

One has B(rho(g)v,rho(c_H g)w)=B(v,w). The exact script checks this on the head generators and every basis pair. Thus V-=V+^vee and the pair has dimension42 overF2.

On V+, the order-two norm kernel has dimension4 overF8, while its image has dimension3; hence H1(<s>,V+) has dimension1. The order-three norm kernel also has dimension4. The coboundaries have dimension7 because there are no H-invariants. Hence H1(Pi,V+) has dimension1 overF8, and restriction to the s-factor is an isomorphism. This is the new feature relative to A.49: the s-torsion direction is not zero.

Choose the cocycle with d_+(s)=e0 and d_+(r)=0. Since tau^6 has a nontrivial central character, rho(tau)-1 is invertible. There is a unique coboundary adjustment making d_+(tau)=0. The exact adjustment is

    k=(6,5,0,6,3,5,5)

in the polynomial basis F8=F2[t]/(t³+t+1). Both normalized generator vectors are

    v_s=v_r=(1,0,5,5,5,5,0).

Define d_-(g)=d_+(c(g)). It has those same generator vectors, but the c-twisted action, and its cusp value is also zero. Write Vbar=V+ plus V-. The resulting joint affine quotient is Vbar semidirect H. Each nonzero cocycle class gives a full affine quotient: H1(H,V+)=0 by coprime cohomology of the normal odd Heis7, and the module is simple. All nonzero classes differ by F8 scalars and therefore give the same quotient kernel. The two kernels are c-exchanged and their modules are nonisomorphic, so the joint kernel is all Vbar.

For invariance under GT0, H is characteristic and the two21-dimensional central-character modules are permuted. OverF8 an extension of the Heisenberg representation to C6 is unique, since Hom(C6,F8^×)=1; equivalently any other twist by a cube root requires a larger field and has different F2 dimension. Thus the complete two-kernel affine family over this head is invariant.

The odd normal Heis7 acts without invariants. Hence H^j(C,Vbar)=H^j(C,Vbar^vee)=0 for every j by coprime Hochschild--Serre. The R-image in the affine quotient is Vbar: the nonzero Pi cocycles cannot inflate from C, and irreducibility gives each full summand.

## The forced frame correction already has trivial norm

At the level Vbar semidirect C, h_C is identity on the representation quotient H. The s-frame beta_H=z^j acts on V+,V- by inverse scalars. Its action on their nonzero H1(<s>) directions therefore forces precisely the correction

    A_j=(zeta^(-j), zeta^j).

This is conjugation by beta_H in the finite affine quotient. Because the actual cusp has zero vector coordinate and beta_H is central in H, the correction fixes the actual cusp. Since c_H invertsz and exchanges the modules,

    A_j c(A_j)=1.

Thus the nonzero torsion class introduces a definite linear correction but no norm obstruction in this particular head. This is an actual formula, valid for every retained frame value j, rather than an appeal to odd-order norm vanishing.

## The correct central cover includes a nonsplit head lift

Let P have elements(v,w,t), with v,w inF8^7 and t inF8, and product

    (v,w,t)(v',w',t')=(v+v',w+w',t+t'+B(v,w')).

It has order2^45, center F8, quotient Vbar, and commutator form B(v,w')+B(v',w). H acts honestly by its paired representations and fixes the center.

The actual s-vector has square B(v_s,v_s)=1. Thus P semidirect H is NOT the correct cover for an order-two s lift. Let

    Htilde=H x_(C6) C12,

and identify its central involution with1 in the additive centerF8 ofP. The resulting central product

    Ghat=(P semidirect Htilde)/<(1,central involution)>

is a central extension of Vbar semidirect H by F8. The two square contributions of the actual s lift now cancel. The r lift has its unique central correction making order3; the exact correction in the chosen coordinates is2 inF8. The normalized cusp still has zero Vbar coordinate.

In canonical d in{0,...,5}, the central multiplication has the additional carry floor((d+e)/6), interpreted as0 or1 inF8. The c automorphism is

    (v,w,t,h) -> (w,v,t+B(v,w)+[d(h)!=0],c_H(h)).

This is the flip on the hyperbolic group together with inversion on C12. Its two corrections make it fix the actual s; the exact script checks that it sends the actual r to s r^(-1)s and the cusp to its inverse. It has square one. The script also verifies all bilinear automorphism identities on the complete F2 generator set.

The specified odd-order lift beta_tilde of z^j in Htilde centralizes the actual cusp, and c(beta_tilde)=beta_tilde^(-1). Therefore

    (Inn(beta_tilde)c_Ghat)^2=1.

The finite script checks this for all seven j and the complete group-generator set. The phrase 'specified odd-order lift' means the canonical lift in the central extension Htilde, not uniqueness among all conjugate lifts in Ghat.

## Identifying the actual central refinement

Let W be the intersection of R with the kernel of the joint affine quotient. The same finite Pontryagin-dual argument as A.49 shows that the actual central kernel of Pi/[W,Pi] is the commutator of the R-preimage and is a quotient of(wedge²Vbar)_C.

This coinvariant space has dimension3 overF2. The two self-terms have no invariants because their Heisenberg central characters square nontrivially. The cross term is End_H(V+)=F8. The same dimension already holds for the odd subgroup J=Heis7 semidirect C3. The exact F2 calculation restricts the42-dimensional module, forms all861 exterior-square coordinates, and obtains relation rank858 using only X,Y,r. Thus the bound on the actual center is8.

The explicit map Pi -> Ghat realizes all8 central elements on R: its R-image projects onto Vbar, and commutators of pure summand lifts give every value of the nondegenerate F8 pairing. Hence the actual R-preimage is P, and

    Pi/[W,Pi] = Ghat x_H C.

As in A.49, this follows from the actual projections and the attained finite upper bound; the compensating C12 cover is not merely substituted for the actual refinement.

On this fiber product take the positive action(Inn(beta_tilde),h_C). For s its finite conjugator beta_tilde has exactly the retained H-frame. For r, the centralizer of the actual order-three lift projects onto C_H(r), by the coprime complement theorem for the normal2-group P. Multiplying beta_tilde by a suitable such centralizer element gives the finite conjugator matching the retained r-frame. The actual cusp is fixed. Thus the full framed A.3 input is obtained.

The negative action is(Inn(beta_tilde)c_Ghat,beta_C), of order two by the explicit norm formula. Scalar stabilization follows by the identical finite-duality argument of A.49: in the next refinement the central pairing A1 tensor Vbar -> A2 vanishes, the next center is a wedge quotient, and its odd J action is trivial on both central subquotients. The J-coinvariant dimension3 is already attained by the old centerF8, so the new center is zero. Only after that equality may A.3 be applied with the stabilized kernel to realize the entire specified central-refinement action by a full positive lift.

## Compatibility to check explicitly in final review

Perfect earlier heads are independent as before. The A.49 residual abelianization has the two6-dimensional AGL1(7) modules, on which the Heisenberg center acts trivially; the new21-dimensional modules have nontrivial center. Thus there is no common C-equivariant elementary-abelian quotient, and the earlier stabilized residual still surjects onto the new modules. The one-dimensional-overF8 Pi cohomology has a single nonzero kernel up to scalar, so the H1 vanishing persists for that enlarged base. This should retain all prior towers and their exact frames, but the final write-up must give that independence passage explicitly rather than silently assume it.

No cofinality, general representation-layer lifting theorem, or full order-two element has been obtained.
