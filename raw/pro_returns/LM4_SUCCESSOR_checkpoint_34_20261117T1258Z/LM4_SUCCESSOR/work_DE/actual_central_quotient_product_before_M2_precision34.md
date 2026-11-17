# Actual product structure of the first congruence-central quotient and its odd coherent obstruction

Checkpoint34 research proof. This is a structural evaluation of the ACTUAL quotient E1=F/N1. No finite target census, no new execution, and no assertion of the actual CM parity is involved.

## 1. Actual groups and coordinate projection

Retain A103--A108 and the exact original signed marking. Write

    P2=F^(2)/M21,        M21=closure([M2,F^(2)]),
    Aodd=product_(p odd) Z_p^2,
    Godd=product_(p odd) Gp,       Gp=SL2(Z_p).

The group P2 is pro-two and P2_ab=Z2^2, since M21 lies in the closed derived subgroup of F^(2). A106 embeds E1 in C x F_ab x P2. The C_(2) coordinate and the dyadic abelian coordinate are already determined by the P2 coordinate. Therefore projection gives an actual topological embedding

    E1 -> P2 x Aodd x Godd.                                  (1)

Both the P2 and Aodd coordinate projections of F are onto. Their joint projection is onto as well. To see this, its closed image is subdirect, and any common quotient from the profinite Goursat description is both pro-two and pro-odd, hence trivial. Equivalently every finite common quotient has order both a power of two and odd. Thus the image in (1) projects onto

    R=P2 x Aodd

and onto Godd separately.

For clarity, the profinite Goursat argument used here needs no finiteness or generation assertion: for a closed subdirect I<=R x G, the subgroups R0={r:(r,1) in I} and G0={g:(1,g) in I} are closed normal. Given (r,g) in I, matching their cosets defines a continuous isomorphism R/R0 -> G/G0. The subgroup I is exactly the inverse image of that graph. Compactness gives the quotient topology throughout.

## 2. The entire possible common quotient is only C3

The complete primary input already bound in A108 is

    (G3)_ab=C3,        (Gp)_ab=1 for p>=5.                   (2)

It implies that the MAXIMAL PRONILPOTENT quotient of Godd is exactly C3, via the actual reduction character chi:G3 -> C3.

Here is the full finite argument. A finite p-group with cyclic abelianization is cyclic: lift a generator to g; if <g> were proper, place it in a maximal subgroup M. Such a subgroup is normal of index p, so it contains the commutator subgroup; then <g>Q'=Q would contradict M being proper. A finite p-group with trivial abelianization is therefore trivial.

For a continuous homomorphism Godd -> a finite p-group, its restriction to every G_l with l>=5 is trivial by (2). The continuous homomorphism depends on only finitely many prime coordinates, so these restrictions make the entire product over l>=5 trivial. The remaining image of G3 is a finite p-group with abelianization a quotient of C3. It is trivial unless p=3, and in that case it is cyclic and a quotient of C3. Thus every finite p-group quotient factors through this same actual chi. The Sylow projections of a finite nilpotent quotient give the identical conclusion for every finite nilpotent quotient. Consequently any pronilpotent quotient of Godd is a quotient of C3. The actual chi is onto, proving the claim.

Now R=P2 x Aodd is pronilpotent. Therefore the common quotient Q in the Goursat description of the actual image I in (1) is a quotient of C3. In particular the index of I in R x Godd is at most three.

The actual markings give the relation

    chi(q3(g)) = exp_x(g)+exp_y(g) mod3                      (3)

for every g in F, since both original X and Y have chi-value one. Let ell:Aodd -> C3 be the sum of the two three-adic coordinates modulo three. The actual image I is contained in

    I0={ (p,a,c) : chi(c3)=ell(a) }.

This is an index-three closed subgroup of R x Godd. The index bound from Goursat therefore forces I=I0. It is not merely an inclusion or a proposed fiber product.

Rearranging coordinates proves the actual topological group isomorphism

    E1 = P2 x (G3 x_(C3) Z3^2)
            x product_(p>=5) (Gp x Z_p^2),                 (4)

where the fiber product uses chi on G3 and the sum-modulo-three map on Z3^2. The maps are exactly the original coordinate projections of A106.

## 3. Derived subgroup and the actual cyclic centralizer

The derived subgroup of the three-adic fiber product in (4) is exactly G3' x {0}. Indeed its projection to G3 is onto; lift each pair of G3 elements, and their commutator has exactly the desired first coordinate and zero abelian coordinate. Closure gives all of G3'. The reverse inclusion is immediate. Derived subgroups of the other displayed factors are equally explicit. For an infinite direct product, the closed derived subgroup contains every supported derived factor and hence their dense finite products, proving the full equality. Thus

    E1' = P2' x G3' x product_(p>=5) Gp.                    (5)

On this derived group the actual rho=Ad(r) acts componentwise. Its first component is the genuine action induced on P2'. On every odd factor it is Ad(J), where

    J=[[0,-1],[1,-1]].

The extra integral cyclic sign character vanishes on F'. The action on P2 is well-defined because the actual cyclic automorphism preserves M2 and M21, as proved using the modulo-four correction in A107. Consequently

    T=C_E1(r)=(E1')^rho
      =T2 x C_(G3')(J) x product_(p>=5) C_(Gp)(J),          (6)

with T2=(P2')^rho. The equality with C_E1(r) uses the zero fixed module of the original cyclic abelian matrix, as in A109--A111. This evaluates the entire T appearing in the separate homeomorphism H^1(C3,N1)~=T.

For either e=+1 or -1, put epsilon=(1-e)/2 and R_e=y^epsilon r. Conjugation on an odd derived factor is Ad(J_e), with

    J_e=diag(1,e) J diag(1,e)^(-1)=(-1)^epsilon Y^epsilon J.

The same argument gives

    T_e=C_E1(R_e)=T_(2,e) x T_(3,e) x product_(p>=5) T_(p,e),
    T_(3,e)=C_(G3')(J_e),        T_(p,e)=C_(Gp)(J_e).       (7)

The first factor is the actual fixed subgroup inside P2'; it is not replaced by a centralizer in all SL2(Z2).

## 4. Exact odd centralizers and their square quotients

Solving the four linear commutation equations with J_e shows that the centralizer algebra in M2(Z_p) is Z_p[J_e]. This can also be seen from its cyclic vector basis. Its determinant is the quadratic norm; hence C_(Gp)(J_e) is the norm-one unit group of that quadratic order. It is abelian.

For p>=5 the discriminant -3 is a unit. The algebra is either split or unramified quadratic according to the polynomial T^2+T+1 modulo p. The residue norm-one group is cyclic of order p-1 in the split case and p+1 in the irreducible case. Reduction of the integral norm-one group onto this residue group is onto: lift a residue element, then correct the determinant in 1+p Z_p by a scalar square root. The reduction kernel is abelian pro-p, and squaring on it is an automorphism. Thus

    T_(p,e)/T_(p,e)^2 ~= C2                 (p>=5).         (8)

At p=3, the full finite centralizer of J_e mod3 in SL2(F3) is the cyclic six-element group generated by J_e and -I. Its three-part is detected by the actual chi, because chi(J_e)=e is nonzero. Since G3' is exactly the kernel of this character, reduction of T_(3,e) has image precisely {I,-I}. Its kernel is abelian pro-three. The central element -I splits this reduction, giving

    T_(3,e) = {I,-I} x U_(3,e),
    U_(3,e) abelian pro-three,
    T_(3,e)/T_(3,e)^2 ~= {I,-I}.                            (9)

These are topological square quotients: the image of squaring on each compact abelian group is closed. The elementary six-element centralizer assertion is also the exact already-certified input of A105/A111; no new finite computation is being asserted here.

## 5. The actual coherent involution acts by inversion on every odd factor

Use the original full-group negative conjugator J_e^alpha and actual alpha from A111. Its coherent action on T_e is

    kappa_e(t)=(J_e^alpha)^(-1) alpha(t) J_e^alpha.

The decomposition (5) is respected by alpha, by iota=Ad(s), and by the relevant inner actions: the pro-two projection is natural, while each odd signed projection is acted on by its proved matrix conjugation. Thus kappa_e acts componentwise on (7).

At an odd prime let L_p be the actual matrix giving this conjugation on the derived factor. The ORIGINAL group relation

    alpha(R_e)=J_e^alpha R_e^(-1) (J_e^alpha)^(-1)

gives kappa_e rho_e kappa_e^(-1)=rho_e^(-1). Therefore conjugation by L_p J_e L_p^(-1) agrees with conjugation by J_e^(-1) on the relevant derived matrix group.

Its matrix centralizer consists only of scalars. For p>=5 this follows by commuting with the two elementary unipotents. At three one may use X^3=I+6E12 and Y^3=I-6E21, both in G3': since Z3 has no zero divisors, commuting with these likewise forces a scalar matrix. Thus

    L_p J_e L_p^(-1)=zeta_p J_e^(-1)

for a scalar unit zeta_p. Both cyclic matrices have trace -1; taking traces gives zeta_p=1. This removes a possible signed ambiguity rather than assuming it away. It follows that kappa_e sends J_e to J_e^(-1) exactly. On the quadratic algebra it is the usual conjugation, and on determinant-one units this is inversion. Therefore

    kappa_e(t_p)=t_p^(-1)        for every odd factor.       (10)

## 6. Complete odd part of the coherent obstruction space

For a compact abelian group A acted on by inversion, every element is a C2-cocycle and its coboundaries are the squares. Hence H^1(C2,A)=A/A^2 as a compact pointed group. Cocycles and equivalences for a product action are componentwise, and a product of correcting conjugators is an allowed correcting conjugator in the compact product. Thus (7)--(10) give a pointed homeomorphism

    H^1(C2,T_e)
      ~= H^1(C2,T_(2,e)) x product_(p odd) C2.              (11)

The statement about the first factor is only its actual cohomology space; it has not been computed. At the three-adic coordinate the identification in (9) is exactly the actual scalar reduction q3. Therefore A111's equality

    q3_*(omega_alpha)=epsilon_A (d mod3) I
                    =(-1)^Delta(alpha) I

is the three-adic coordinate of (11). The other odd square classes and the actual pro-two factor may supply additional obstructions to coherent framing. No value of those additional coordinates is inferred from the decomposition, and the original three-adic CM coordinate remains open.

## 7. Boundaries

The Goursat argument proves the actual quotient structure, not merely an available quotient or a faithful-looking finite image. The pure-frame choice ambiguity of A110 remains. Formula (11) is a target-space computation and does not assert that the actual class omega_alpha is trivial. It gives no splitting of the central pro-two extension used earlier, no full hexagon in F, and no conclusion about either main problem.
