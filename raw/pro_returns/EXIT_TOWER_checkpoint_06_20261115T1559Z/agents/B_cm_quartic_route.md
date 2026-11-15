# Three-division quartic: exact maps and remaining comparison

This is an incremental research record. It does not assert a value of the LM7 character on GT.

## 1. An actual algebraic map

For the smooth short Weierstrass curve E: y²=x³+ax+b put D=4a³+27b². Its three-division polynomial is

    psi3(x)=3x⁴+6ax²+12bx−a².

The four roots are the images of the eight nonzero three-torsion points under the elliptic involution. Their binary-quartic invariant I is zero, and J=-432D. Thus their double cover is equianharmonic.

Choose the normalized quartic C: t²=x⁴+2ax²+4bx−a²/3 and its positive point at infinity as origin. Set

    X=(t+x²+a)/2, Z=X−a/3, Y=Xx+b/2.

Then C maps birationally to

    E': Y²=Z³+D/108,

and the inverse is x=(Y−b/2)/(Z+a/3), t=2(Z+a/3)−x²−a. Both smooth projective curves have genus one, so the birational maps extend to inverse isomorphisms. The other point at infinity is P=(-a/3,-b/2). The quartic involution exchanges the two poles and is Q↦P−Q. Consequently its four branch points satisfy 2Q=P.

At b=0, P is a nonzero point of order two. The four original three-torsion images therefore become the four halves of this particular two-torsion point on E'. At a=0, P is nonzero three-torsion: its horizontal tangent has triple intersection at P. These are geometric point identifications, rather than an inference from the equality of two number fields.

The source scaling (x,a,b,t)↦(u²x,u⁴a,u⁶b,u⁴t) induces (Z,Y)↦(u⁴Z,u⁶Y). At the harmonic point u=i this is the elliptic involution of E'. At the equianharmonic point u=zeta6 it is the target automorphism zeta3². This last exponent must be retained when fixing the positive braid generators.

The two ordered poles are intrinsic to the monic construction: define p± by t/x²→±1. Under an affine coordinate change x'=cx+d fixing the original origin at infinity, the canonical map is t'=c²t, preserving both signs. Root relabelling preserves the polynomial and the ordered poles. Therefore the mixed four-root braid group lands in Gamma12 with both elliptic labels individually fixed. The determinant-minus-one H-level correction fixes infinity and only relabels these roots, so it supplies an inner element of this exact target, not merely its pole-exchanging extension. After rigidifying the original central involution, v=u² gives weights(a,b)=(2,3), weight(D)=6 and target weights(Z,Y)=(2,3); the D108 slice has the standard residual mu6 action.

`code/b_cm_quartic.py` verifies the direct and inverse equations, the invariants, the two torsion specializations, the weights, and the elementary braid-fold matrix identities. It does not prove profinite functoriality.

## 2. The translation normalizer on nine points

Let H=(Z/3)² act on an oriented torus by translations, and label one regular orbit by H, with the identity label called 0. The normalizer N of this actual H in the mapping class group of the nine-point torus has an exact quotient N/H≅SL2(Z). Its subgroup N0 fixing the identity label maps isomorphically to SL2(Z) by ordinary forgetting of the other eight points.

Here is a direct discrete proof. Remove the nine points and their one quotient point. The covering sequence is F10 normal in F2 with quotient H, given by abelianization modulo three. This kernel is characteristic. The center-free extension argument used in E.44 identifies the covering F2 with the exact inverse image of H in Aut(F10). A normalizing mapping class therefore descends to an oriented once-punctured torus mapping class. Conversely every such mapping class preserves the covering kernel and lifts. The deck kernel is H. Every normalizer element has a unique deck translate fixing label 0, so N0 is the required complement. On linear representatives both the downstairs quotient map and the upstairs forgetting map induce the same integral homology matrix; hence the latter is also the claimed isomorphism. Its full induced topology follows by pulling back every finite quotient along the actual ambient forgetting map.

One must recognize the translation action, rather than an arbitrary C3² action. A C3² action at a CM torus can contain rotations and have fixed points. For the translation action the preimage of H in the universal-curve extension is the torsion-free F2. A finite action with an unmarked fixed point has a torsion lift in this extension. Thus preservation of the actual universal-curve extension, together with the finite-subgroup theorem, distinguishes the free translation action. The remaining labelled free actions have the two orientation classes of an H-level basis. A determinant-minus-one relabelling interchanges them and fixes the retained origin. The effect of this relabelling on the later four-point comparison must be recorded explicitly; no pure-class uniqueness is being asserted.

## 3. The next required diagrams

Add the three nonzero two-torsion points using the torsion-lift classes of the central elliptic involution. The resulting label set is E[2] union E[3], with 12 points, not 13. Its involution quotient is a sphere with eight marked points: the four branch values and the four nonzero three-torsion images. Forget three branch values to retain the original origin and the four latter images; this is the five-point configuration defining the quartic above.

The outstanding profinite comparison is the actual hyperelliptic centralizer in the 12-point elliptic group, its full induced topology, and its quotient by the elliptic involution with the named eight-point sphere group. Forgetting three exchanged pairs then gives the exact five-point branch-order comparison already proved in E.44; this is the intended route to fixing the GT parameter of the eight-point quotient. D is independently checking this step.

The resulting source-to-target orbifold map should be identified by its actual fundamental-group generators and positive peripheral transports before using it for the CM character. The target is the preimage of the order-six CM group under Gamma12→Gamma11. On abstract orbifold types both source and target are C2*C3. In B4/Z, delta4²=(abc)² has order two and epsilon4=a²bc has order three; under a,c↦u, b↦w their images are -I and (uw)². The explicit scaling above sends the positive source zeta6 to target zeta3², so the geometric order-three image may be epsilon4 inverse. This orientation issue is recorded, not silently normalized away.

The following sections supply the named signed-frame calculation. Their integration, including the intrinsic diagram above, is submitted for independent audit before the final result is promoted.

## 4. Exact scalar-free pointpush covariance

Write G=Gamma12=B4/<omega4>, L=Gamma11=B3/<omega3²>, with the ordinary filling q(a,b,c)=(u,w,u). Its free rank-two kernel K has generators

    xi1=ca^-1, xi2=aba c^-1 b^-1 a^-1.

The actual B4 conjugation words are

    a:(xi1,xi2) -> (xi1,xi2 xi1),
    b:(xi1,xi2) -> (xi1 xi2^-1,xi2),
    c:(xi1,xi2) -> (xi1,xi1 xi2).

Thus the action on K_ab is Q(a)=Q(c)=U=[[1,1],[0,1]], Q(b)=L0=[[1,0],[-1,1]]. These words are checked through the faithful Artin action by b_cm_module.py. They also give the split free-kernel presentation of B4 over B3; the central quotient retains K because omega4 maps to the infinite-order omega3² before taking either quotient.

Let A_GT=(1,f) and use the genuine HS braid formula. Put e=f(ba²b,c²). Since ba²b=(ab)³ a^-2 and a commutes with both (ab)³ and c, the central-shift identity for f in the free commutator subgroup gives e=f((ab)³,c²). Hence [e,a]=1. Its filling is trivial because the two filled arguments commute, so e belongs to K. Now Phi(c)=e^-1 c e and Phi(a)=a. If N is the induced K_ab matrix, then (U-I)[e]=0 and

    N e1 = [Phi(ca^-1)] = e1+(U-I)[e] = e1.

Also N commutes with U. These two literal equations force N=[[1,t],[0,1]] over Zhat: no scalar, including a primewise sign, remains. Covariance with b gives

    N L0 N^-1 = q12(f)^-1 L0 q12(f).

LM7 E.65's independently checked signed covariance says that V=U^(8rho) satisfies the same equality modulo12 and commutes with U. The joint centralizer of U,L0 consists of scalar matrices; both N and V fix e1. Therefore N=V modulo12.

Let Rplus=UL0 (order six) in L. The canonical pure frame A of LM7 E.65 has a lift Atilde to L in <u²,w²>; the signed representation on this subgroup is q12. The relation Phi(Rplus)=Atilde Rplus Atilde^-1 holds: it holds modulo the central involution by the defining frame, and the other possible sign is excluded by abelianization L_ab=C12, on which the multiplier-one action is the identity. Lift Atilde further to G by the same word in a²,b². The corrected automorphism Ad(Atilde^-1)Phi preserves G3=q^-1(<Rplus>) and acts on K_ab modulo12 by exactly

    T=q12(A)^-1 V.

This fixes the normalization of T by a named pointpush generator, not just by conjugation covariance.

## 5. The equianharmonic subgroup and its actual comparison

The algebraic map in Section1 factors through the rigidification of M11 by its central involution, since it only uses the original x-coordinate. This source stack is

    [(a,b), 4a³+27b² != 0 / Gm with weights (2,3)].

The target is the locus j=0 in M12 with ordered points, represented as [E0\{0}/mu6], where E0:Y²=Z³+1 and the second point is P. The coordinate map gives an isomorphism of these stacks: the level set D=108 is the affine E0 via (Z,Y)=(-a/3,-b/2), and its residual scaling group is mu6. Conversely (Z,Y) on E0 gives a=-3Z,b=-2Y and D=108. Thus its map

    phi:B=C2(s)*C3(r) -> G3=q^-1(<Rplus>)

is an actual isomorphism. The kernel of B_ab:C2*C3->C6 is the fundamental group of E0\{0}, and phi identifies it with the pointpush kernel K. The induced quotient C6 map is an automorphism, so phi(tau) maps to Rplus^epsilon with epsilon=1 or -1. The explicit weight calculation in Section1 retains which order-three local action occurs; the sign proof below works with this actual epsilon and never replaces it by an unproved identification.

The intrinsic construction in Sections2–3 and D's audited centralizer comparison makes this exact phi compatible with the ordinary tower action with the same parameter A_GT. Namely recover the free C3² orbit, add the three nonzero fixed points of the central elliptic involution, descend through the actual eight-point quotient, forget three branch labels, and use E44's named five-point quartic cover. The two level-orientation classes differ by a relabelling fixing the original origin; it only permutes the four target branch labels. Such a permutation is a geometric braid in the mixed five-point target and supplies an inner comparison there. Thus this ambiguity does not change phi's outer naturality equation.

For completeness, adding a fixed point is an actual finite groupoid operation. Its objects are the conjugacy classes of order-two lifts of the central elliptic involution in the universal-curve extension. The preimage is the free product with one C2 factor for each unmarked fixed point and a free factor for the paired punctures. Finite-subgroup conjugacy and centralizer closure give the same classes after full completion. Each chosen lift centralizer has trivial intersection with the free surface kernel and maps isomorphically to the class stabilizer in N0. Its full topology follows by pulling back finite quotients along ordinary forgetting to N0. Repeating for the three remaining fixed points gives the ordered fixed-point groupoid and its finite permutation descent. Every map used is a restriction of the actual universal-curve projection. This is the simultaneous fixed-point construction, rather than three unrelated choices of lifts.

Accordingly, for some h in the completed target G,

    Ad(Atilde^-1) Phi phi = Ad(h) phi alpha_B.

Both sides induce the identity on the finite quotient <Rplus>. Therefore q(h) centralizes Rplus. Its centralizer in Lhat is exactly <Rplus>: modulo the central involution this is the finite C3-factor centralizer in C2 amalg C3, supplied by the p=3 finite-subgroup theorem. Hence h belongs to G3 and q(h)=Rplus^k for one k in Z/6. This is one global CM exponent, not separate signs at different primes.

Let C be the integral homology isomorphism induced by phi and M the K_ab matrix of alpha_B. Then

    T C = Rplus^k C M,
    C R C^-1 = Rplus^epsilon.

In particular, after changing the named homology basis by C, M differs from T by the indicated single CM power. The rest of the proof only uses its parity, which is independent of epsilon and of replacing k by -k.

## 6. The exact affine model of the modular commutator quotient

Put tau=sr and K0=B'. Then K0 is free of rank two. The quotient by [K0,K0] has the presentation

    B/[K0,K0] = Z² semidirect C6,
    R=[[0,-1],[1,1]], tau=(0,R),
    s=(p,R³)=(p,-I), r=(p,R⁴)=(p,-R), p=(1,0).

Here is a direct abelian Schreier check. Put p_i=tau^i(s tau^-3)tau^-i and t=tau^6 in K0_ab. The s² and r³ relations give p_i+p_(i+3)+t=0 and p_i+p_(i+4)+p_(i+8)+2t=0, with p_i periodic modulo6. The equations at i=0,1 force t=0 and p_2=p_1-p_0. All remaining equations then follow. The displayed semidirect model shows p_0,p_1 are independent, and conjugation by tau is exactly R. Finite-index completion gives the same model with Zhat².

Since alpha_B fixes tau literally, its matrix M commutes with R. Write the pure torsion frames in this quotient as beta=(b,R^j), A=(a,R^ell). Their exponents j,ell are even, because both frames lie in the kernel of B->S3. Conjugating s and r gives the two exact equations

    M p = 2b + R^j p,
    M p = (I-R⁴)a + R^ell p.

At three, R⁴=-R and R+I is a nonzero nilpotent of rank one. Its image equals its kernel L_minus. On the quotient by that line, R acts by -1, hence R^ell acts by +1. The second equation forces M to act by +1 on that quotient. Commutation with R+I then forces M to act by +1 on L_minus itself.

At two, the named projective map q3:B->PSL2(F3)=A4 is the affine action on F2² in this model. An explicit dictionary is

    infinity -> (0,0), 0 -> (1,0), -1 -> (0,1), 1 -> (1,1).

For q3(s)=S, q3(r)=R0=-UL0, and q3(tau)=U^-1, this dictionary sends tau to R, s to translation by p, and r to (p,R⁴). The exact identity j=4rho in C6 follows from beta_ab=(-rho,-rho) in the generators x=tau^-2 and y=sxs. Thus V3=U^(8rho) has affine image (0,R^j). Consequently the projective image of W=q3(beta)^-1 V3 is translation by -R^-j b. Since W is in <S>, that translation is epsilon2(W)*p. Therefore b=epsilon2(W) R^j p modulo2. The first exact frame equation now yields

    M = (-1)^epsilon2(W) R^j modulo4.

Indeed it first gives equality on p, and commutation with R gives equality on Rp; these form a basis. The exponent j is even. Hence the parity of the unique exponent of M modulo4 in <R> is exactly epsilon2(W).

`b_cm_module.py` verifies the named projective/affine dictionary, every mod-four beta-frame case, every mod-three A-frame case, and the six B4 pointpush word identities used in Section4.

## 7. The named CM parity comparison

The previous section proves that M acts by +1 on the (-1)-eigenline at3, and that its CM exponent modulo4 has parity epsilon2(W). Section5 compares M to T by a single CM exponent k. Since T is I modulo4, the latter exponent has parity k. Since T acts by (-1)^epsilon3(T) on the (-1)-eigenline at3, the former equality gives k=epsilon3(T) modulo2. Thus

    epsilon2(W)=epsilon3(T).

This is the exact delta=0 identity for multiplier-one GT elements. LM7 E.65's choice-independent Galois translation then gives Delta=0 on all of GT, since the Galois subgroup is contained in GT and Delta vanishes there. The designated E58 gentle element has Delta=1, so this comparison excludes it from GT. This conclusion is submitted as the result of the complete diagram and module calculation above, not inferred from field coincidence, finite enumeration alone, or the absence of a supplied pentagon certificate.
