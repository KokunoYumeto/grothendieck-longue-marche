# Prime-seven five-strand refinement: exact-map ledger

Date: 2026-11-13. New work after frozen checkpoint06; E50 certificates and
integrated sources remain unchanged. E51 is reserved by the parent. This note
records completed maps separately from the one target computation still
running at the time of writing.

## Completed finite maps

1. `bc_symplectic_five_p7_model.py` reconstructs the four transvections from
   the same integer chain alternating form. The actual B5 image has order
   276595200, hence is Sp4(F7), and its first B4 image has order115248.
   All Artin relations, the eight actual evaluation pairs, and both periodic
   powers are retained. Delta has order10 and epsilon has order8.
2. `bc_symplectic_five_p7_source.py` induces all eight evaluations through
   all six B/F cosets. All592 original orbits have saved exact intertwiners
   into ten retained B-sets. The faithful degree3570 source has order135531648.
3. `bc_symplectic_five_p7_subgroups.py` uses all97 N generators and the95
   primitive integral F-abelianization-kernel columns. Its exact orders are
   G135531648; F=H22588608; N=K6 5647152; C=F'=H'=gamma3(H)=K6 cap F'
   115248; L=N'=C'336. The actual x,y orders are14.
4. `bc_symplectic_five_p7_residual.py` decodes the third pentagon coordinate
   through the saved intertwiners. Its stable e2,e3 block, transposed to
   ordinary matrix multiplication, is a specified isomorphism
   theta:L -> SL2(F7). All336 matrix values are retained. Removing the unique
   L component from each original generator proves actual direct products
   N=L x (C7)^5 and C=L x (C7)^3. All generators commute as asserted, have
   order7 in the elementary factors, and the exact generated orders match.
   No enumeration of all16807 elementary-kernel permutations is needed.
5. The same residual program checks all672 B-conjugation edges. For the
   coordinate swap P and ordinary modular matrices
   s=[[0,1],[-1,0]], r=[[0,-1],[1,-1]], it proves
   theta(a^-1 l a)=(P q7(a) P)^-1 theta(l)(P q7(a) P).
   The literal x,y matrices are [[1,0],[2,1]], [[1,5],[0,1]]. Thus the action
   on the inner automorphism group is the specified projective q7 map.
6. The A14 map is the six-coset free exponent-sum map modulo14. Its order
   is1176, kernel in B is F'F^14, and the actual map from G has kernel C.
   Reduction modulo2 gives the actual A2 map of order24.
7. `bc_symplectic_five_p7_modular_probe.py` pairs the old G_A source with
   the literal projective q7 map on P1(F7). The exact joint index over G_A
   is168, proving the actual product. This is a statement about those
   specified maps, not the absence of every abstract PSL2(F7) quotient.
8. `bc_symplectic_five_p7_common.py` enumerates Q28=SL2(Z/28)/{+I,-I},
   order8064, with its actual s,r. Its map to A2 is reduction modulo4,
   verified on all24 values against the existing G_L dictionary. All8064
   elements and16128 edges agree with the induced signed48-point F map.
   The literal A14 x_A2 Q28 image has395136 elements, all generated, and
   its actual source kernel is Q7=(C7)^3.
9. `bc_symplectic_five_p7_target_perfect.py` enumerates all115248 elements
   of the B4 target and proves it perfect from the literal commutators
   [a,b], [b,c], a[a,b]a^-1. The generated orders are2744 then115248.
10. `bc_symplectic_five_p7_joint_symplectic.py` computes the actual paired
    prime-five/prime-seven maps. Their B4 joint is the full product of
    orders15000 and115248; their B5 joint is the full product of orders
    9360000 and276595200. The latter order is2588931072000000.

## Exact G_L comparison, including the signed lift

Let q7:B -> PSL2(F7) be the map in item7. The kernel of G_L -> G_A is an
elementary2 group. The image of ker(rho_A) under q7 is all PSL2(F7). The
quotient of that image by q7(ker(rho_L)) is a2 group, because it is a quotient
of ker(rho_A)/ker(rho_L). It is also a quotient of the perfect PSL2(F7),
and therefore trivial. Hence q7(ker(rho_L))=PSL2(F7).

The actual Q4=A2 map factors through G_L by E38. Thus the Q28 image of
ker(rho_L) lies in the displayed SL2(F7) kernel of Q28 -> Q4 and maps onto
PSL2(F7). If that image is J and Z is the centre of SL2(F7), then JZ=L.
Perfectness gives L=[L,L]=[JZ,JZ]=[J,J] subset J. Consequently J=L. This
proves the actual joint G_L x_A2 Q28 and retains the central sign.

The residual program also checks every normal closure in L. The identity
has closure order1, minus identity order2, and every other element order336.
Thus the only proper nontrivial quotient of L is PSL2(F7); L itself is
perfect. Every nontrivial quotient of C=L x (C7)^3 has order divisible by7.

## Full residual correction and maximum common quotient

Write R_nil=intersection_r gamma_r(Hhat), and let C_L be the perfect
residual of G_L from E43. Compactness of nested fibres and the exact finite
lower-central images give rho_L(R_nil)=C_L and rho7(R_nil)=C. The latter
uses [rho7(H),C]=C, certified directly. Both images are normal in the full
source images.

Their joint image is C_L x C. A nontrivial Goursat quotient would be
perfect. Its C-factor is then L or PSL2(F7): the central7 group is killed,
because the possible quotients of L have centre of order at most2. The
joint kernels are stable under B conjugation. The action of the G_L source
on this common quotient would therefore factor the specified inner-action
map q7 through G_L, contradicting the product proved above. This proves the
joint residual product and hence

    (R_nil cap ker rho_L) -> C is onto.

Intersect this group with the kernel of the actual D23 x G_sp5 source.
That finite image has order prime to7. Since C has no nontrivial quotient
of order prime to7, Goursat proves that the intersection still maps onto
all of C. This explicitly retains E50, including its new five-primary
source. R_nil already kills every finite nilpotent H-boundary image,
including every finite level of all retained pro-p H factors. Thus one
closed correcting subgroup preserves GL, D23, E50, and every boundary
factor simultaneously, and maps onto all of C.

For G_L alone the maximum common quotient with G7 is A2. The pure C
correction forces every common quotient through A14; A14 is solvable and
the maximal solvable quotient of G_L has order43200, prime to7. It therefore
kills the C7^2 kernel of A14 -> A2. A2 itself is a specified common quotient.

For the whole old E50/boundary source, restrict to cofinal finite levels
which retain P28=B/(gamma3(H) H^28). The actual map P28 -> A14 follows from
gamma3(H) subset F' and H^28 subset F^14. P28 is present through the
two-primary P4 factor and the retained full pro-seven H factor, with their
actual coprime H-image product. The pure C correction above proves that
the maximum common quotient is exactly A14, and the actual joint source
is G_old x_A14 G7.

## Same actual Galois word and corrected generation

Take any of the432 old multiplier-one points and any prescribed full E41
and E47 boundary correction-image values. E50 gives a single f0 and an
actual sigma with chi(sigma)=1, with its GL and prime-five source values
equal to those of f_sigma. Both f0 and f_sigma lie in Fhat', so their new
G7 values differ by an element of C. Lift that element through the closed
correcting subgroup just proved. The corrected f retains every old value
and agrees with this same f_sigma in G7. All48 induced evaluation values
then agree. The new pentagon, full braid and twist equations, periodic
conjugacies and individual target generation follow through the actual
Galois braid automorphism. No invariance of an arbitrary finite shadow
kernel is claimed.

For joint source generation, both the GL and the new G7 maps are the same
Galois precomposition. This automorphism preserves H and R_nil, so their
joint residual image remains C_L x C. Intersecting with the old D23 and
prime-five corrected kernels uses the same prime-to7 quotient argument.
The boundary factors vanish on R_nil. The corrected joint image therefore
contains the whole pure C. It projects onto the old source and agrees on
A14. Quotienting G_old x_A14 G7 by pure C gives G_old, proving the corrected
map onto the exact full fibre product. Compact nested fibres retain the
single word through every boundary level.

This use of a common actual Galois precomposition is essential to the
argument given here: the computed independence is the literal q7
independence, not an assertion about all abstract PSL2(F7) quotients.

## Earlier pending-target checkpoint, now superseded

`bc_symplectic_five_p7_target.py` is evaluating the full binary central
extension of the old Ferrari target together with the new B4 map. It uses
the complete lifted Schreier presentation and all57 ambient central
coordinates. No joint-target order from this pending run is asserted yet.

## Completion and authoritative scope

The pending computation completed successfully. Its actual permutation
base has order18202226446764195247073754517340160000000000000000000000000000000.
The complete lifted presentation recovers all55 old binary kernel
dimensions and independently replays every retained relator word. Its
joint target has order
655804321943684937290375047744340378894214239354880000000000000000000000000000000,
exactly the product of the old target and115248. The run took772.158s.
The old literal55-dimensional binary extension is fully retained.

The completed theorem is `sections/E_symplectic_five_p7_agent.tex`, E51.
Its source correction retains every432-point multiplier-one fibre and
every prescribed E41/E47 correction-image parameter. Actual word fibres
are kept separate: inside the chosen closed correcting subgroup K the
fibre is k(K cap ker rho7); among all Fhat' words with the fixed old and
new images it is f ker((rho_old,rho7)|Fhat').

The pair products TL x J7, J5 x J7 and TL x J5 give the full triple
product. To see the precise Goursat step, a common quotient of TL x J5
and J7 is perfect. Quotienting by either of its commuting factor images
would give a nontrivial common quotient in one of the checked pair
products. If both resulting quotients are trivial, both commuting images
are the whole group, which is then abelian and perfect, hence trivial.
The old T23-kernel is solvable, so passing to it cannot supply a new
nontrivial perfect common quotient. Finally A96 is simple and has a
factor11 in its order whereas all the other finite target orders do not.
This gives the full target stated in E51 and the same-Galois generation
comparison. The literal paired Sp4(F5)/Sp4(F7) computation supplies the
corresponding full B5 product before A96.

The independent peer proof audit by `profinite_images` passed the complete
source/residual/signed/Goursat argument. Parent review and independent
replay have been requested. All24 E50 code/output/array hashes in its
authoritative manifest were checked unchanged after this work.

In the same turn, D44 was independently read in full. Its residual pants
descent, specified cusp conjugator, actual abelianization map, supported
power gauge, primitive-boundary centralizer, full gentle cycles, S3 outer
comparison, positive torsion conjugacies, and central101 fibre-product
map all passed. No integrated file was modified in that audit.
