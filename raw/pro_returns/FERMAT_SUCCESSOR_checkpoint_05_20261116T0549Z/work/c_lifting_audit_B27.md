# Independent audit of B.27

**Auditor:** Part C subagent.  **Date:** 2026-11-16.

**Text inspected:** the full B.27 at the end of `deliverable/sections/B_main.tex`, as saved at approximately 02:52 UTC, and A.54 in `deliverable/sections/A_quintic.tex`. No B files were modified.

## Verdict

The theorem's proof is valid with its stated hypotheses, conditional on the explicitly identified rank-zero/finiteness and exact CM-conductor inputs in Part A. It applies to **every actual section whose entire geometric cocycle is unramified outside the coefficient prime**, for every closed normal G_Q-stable J contained in N_n′. It is not confined to the particular lift families of earlier returns. Choosing a rational unit tangent is a coordinate choice for the split extension, not a restriction to a subfamily of sections.

The theorem does **not** classify every lift of an abelian class that happens to be unramified: a lift's higher nonabelian coordinates can ramify at other primes. Nor does the argument extend merely by replacing the geometric pro-ell group by the full profinite group. The pro-ell image of the actual arithmetic action is essential.

I found no counterexample to the stated theorem. The two suggested textual refinements are minor: make X/Z=-s explicit in the Puiseux formula, and say that the **actual compact arithmetic subgroup** of IA Aut(F_2), rather than every IA automorphism, descends to N_n/J. Arbitrary IA automorphisms need not preserve J; G_Q-stability supplies preservation for the subgroup actually used.

## 1. The arithmetic quotient and local surjectivity are correctly typed

Let G=G_{Q,S}, S={ell,infinity}, K=Q(zeta_ell), and H=G_{K,{lambda}}. Here H is the actual open normal subgroup of G: taking the Galois closure over Q of an extension of K unramified outside lambda creates no ramification outside ell, because K/Q itself ramifies only there. Put P=H^(ell), R=ker(H->P), Gamma=G/R. The maximal-pro-ell kernel R is characteristic in H and hence normal in G. Thus

    1 -> P -> Gamma -> Gal(K/Q) -> 1

is an actual quotient sequence, not a formally assembled product. No splitting of this sequence is required.

Let D be the image of G_{K_lambda} in P. This image is compact and therefore closed. If D is proper, there is a finite ell-group quotient of P in which its image is proper. In that finite ell-group choose a maximal subgroup containing the image. Such a subgroup is normal of index ell. The resulting cyclic degree-ell extension of K is unramified outside lambda and lambda splits completely. It is therefore everywhere unramified. Since K is totally imaginary and has class number one, global class field theory excludes it. Hence D=P.

The image of G_{Q_ell} in Gamma also maps onto Gal(K/Q), because the prime ell is totally ramified in K/Q. Its intersection with P contains the image just shown to be all of P. Therefore G_{Q_ell}->Gamma is surjective.

This argument proves surjectivity onto **Gamma**, not onto the whole group G_{Q,S}. Class number one alone would not justify that stronger assertion. B.27 uses precisely the correct quotient.

## 2. The actual geometric action over K has pro-ell image

For n=ell^r, the Fermat cover of the tripod has geometric deck group (Z/n)^2. After geometric pro-ell completion its group is the characteristic open subgroup

    N_n = ker(F_2^(ell) -> (Z/n)^2).

The induced pro-ell topology is the full one on this subgroup: a finite ell-cover of this open subgroup has ell-group normal closure over the ambient free pro-ell group. Thus this identification is with the actual geometric pro-ell fundamental group, not only a quotient of it.

At the chosen rational cusp the power cover has compatible rational Puiseux leading constants. For the plus Fermat equation, one can take X/Z=-s, t=s^n, and Y/Z=-(1-s^n)^(1/n). This makes the based arithmetic action the restriction of the genuine tripod action. At any prime different from ell the smooth pair and the integral unit tangent give a trivial inertia action on its geometric pro-ell group. Hence the genuine action factors through G_{Q,S}.

The action of G_K on F_2/Phi(F_2) is the mod-ell cyclotomic scalar, hence is identity. The kernel of Aut(F_2^(ell))->GL_2(F_ell) is pro-ell. An elementary proof uses the finite characteristic lower exponent-ell central quotients: an automorphism acting trivially on the first quotient acts trivially on the generated associated graded, and the successive kernels of its action embed in finite F_ell Hom groups. Passing to the inverse limit gives a pro-ell group. This is a statement about the free **pro-ell** group itself; it makes no false faithfulness assumption concerning all maximal-pro-prime quotients of a full profinite group.

The compact arithmetic image of H lies in this IA group. Restrict that image to N_n. Its image is still pro-ell. The hypothesis that J is G_Q-stable then lets this actual arithmetic image act on Q=N_n/J; its image on Q remains pro-ell. Full invariance of J under every automorphism of F_2 is neither assumed nor needed.

## 3. Graph factorization applies to arbitrary cocycles

Let z:G_{Q,S}->Q be any continuous 1-cocycle for the given action rho. The map

    h |-> (z(h), rho(h))

from H to Q semidirect rho(H) is a genuine continuous homomorphism. Both Q and rho(H) are pro-ell, so the target is pro-ell. By the defining universal property of H^(ell), this homomorphism kills R. Its two components therefore factor through Gamma. The same conclusion holds for rho on all of G, and for z as a function on all of G, because R is normal and the full graph homomorphism kills it.

There is an important type distinction, correctly reflected in the written display: a section G_Q->Q semidirect G_Q cannot itself factor through Gamma, because its arithmetic projection is the identity on G_Q. It is the **cocycle and action**, or equivalently the graph in Q semidirect Aut(Q), that factor. I suggested adjusting the proof subheading to make that distinction explicit.

This argument makes no use of how z was constructed, of its abelian leading term, or of a chosen central family. It proves the required factorization for the entire unramified section space.

It also proves injectivity of localization on these nonabelian section classes. If two cocycles are conjugate on G_{Q_ell} by u in Q, the same constant u conjugates them globally: their values and action depend only on Gamma, and every element of Gamma is the image of a local element. No nonabelian restriction/corestriction argument is involved.

## 4. The compact class reaches the full single-coefficient Selmer group

The condition J contained in N_n′ guarantees that the quotient retains all of N_n^ab. In particular the map induced by U_n->U_ell, followed by compactification and the Abel--Jacobi map, descends to a map to T_ell A_ell, where A_ell=Jac(X_ell).

The resulting compact class is unramified at every p different from ell. At such a prime A_ell has good reduction. Its unramified T_ell-cohomology is the local Kummer image: reduction identifies the ell-adic completion of A_ell(Q_p) with the ell-primary part of A_ell(F_p), and the finite-field Kummer sequence gives the same quotient T_ell A_ell/(Frob_p-1). At ell, assumed local point/cusp geometry gives a local compact Kummer class. At the real place the odd-primary positive-degree cohomology vanishes. Thus the global compact class lies in the ordinary ell-primary Tate Selmer group.

Rank zero and finite Sha for A_ell imply that this Tate Selmer group is A_ell(Q)^wedge_ell. The passage to continuous Tate-module cohomology introduces no omitted lim^1 term in degree one: the finite invariant groups form a Mittag--Leffler system. Only the rank-zero/finiteness results for the base exponents ell=3 or5 are used, not results for the potentially higher-rank Jacobian of X_{ell^r}.

## 5. A.54 is exactly the needed five-adic strengthening

Full profinite local Kummer injectivity is insufficient for this step; a single-coefficient Kummer map can kill prime-to-ell torsion. A.54 removes precisely that problem at five.

I checked the internal logic of A.54. Given its stated exact local CM conductor lambda^2, every conjugate CM character is nontrivial on U_1/U_2=C_5. A wild inertia lift of a generator therefore has only primitive fifth-root eigenvalues on V_q A_5, for every coefficient prime q different from5. The identity Phi_5(tau)=0 passes to every stable integral Tate lattice. The displayed Bezout identity makes tau-1 invertible on that lattice because5 is a unit in Z_q. This excludes every prime-to-five rational torsion point. The argument passes across the rational isogeny to Jac(X_5) on rational Tate modules and then on its own lattice; it does not incorrectly assume an isogeny degree prime to q.

A compact abelian p-adic Lie group with an open Z_5^g subgroup and no prime-to-five torsion is pro-five. Its finitely generated Z_5-module structure, including finite five-primary torsion, gives intersection_m 5^m A_5(Q_5)=0. Hence the required T_5 Kummer map is injective. This audit does not independently reprove the external exact CM-conductor theorem used in A.50/A.54; that remains its stated, separately verified Part A input.

At three, I independently reran `b_unramified_selmer.gp` using the locally built PARI/GP2.19.1. My separate output is `deliverable/code/c_B27_local_replay.out`. It gives

    elllocalred(ellinit([0,0,1,0,-7]),3)
      = [3,-4,[1,0,0,0],3].

I opened the official PARI documentation for elllocalred: the entries mean conductor exponent3, Kodaira IV*, already minimal model, and Tamagawa number3. The nonsingular reduction contains exactly three points (two affine nonsingular points and infinity), while the formal group is pro-three. Thus the complete local elliptic group is pro-three, and its T_3 Kummer map is injective too.

Official source: The PARI Group. (2026). *PARI/GP: Elliptic curves*, elllocalred. https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html . The document was opened and the precise return-value convention inspected. The numerical call was independently rerun rather than copied from a database.

The same replay independently certifies class number1 and unique coefficient-prime ramification for Q(zeta_3) and Q(zeta_5), using bnfcertify. The paper also supplies elementary class-number arguments.

## 6. Descent of the local cusp to Q is valid and uses special geometry

Let a in A_ell(Q)^wedge_ell be the compact global class. Since A_ell(Q) is finite and embeds into the pro-ell local group, it is already ell-primary. Thus a is an actual rational point of A_ell.

If P_ell is the local compact point furnished by local geometry, local Kummer injectivity gives [P_ell-O]=a as actual local points of A_ell. The Abel--Jacobi map X_ell->A_ell is a closed embedding because X_ell has positive genus. Its fibre above the rational point a has a Q_ell point and hence is its unique rational point. Equivalently, a closed subscheme of Spec(Q) with a Q_ell point is Spec(Q). Thus P_ell is a Q-rational point of X_ell. The Part A point computations place it at a coordinate cusp.

An interior point of U_n cannot map to such a cusp under the coordinate-power map: all three coordinates of an interior point are nonzero. Hence the originally supplied local geometric section must be the image of a local cusp section.

Finally a Q_ell-rational cusp of X_{ell^r} has nonzero coordinate ratio -zeta with zeta an ell-power root of unity. Q_ell has no nontrivial ell-power root of unity for odd ell=3,5. Therefore it is one of the three globally rational cusps. This is not an invalid general inference that a local algebraic branch is globally rational; it uses the exact cyclotomic description of this boundary.

## 7. Rebasing and the local-to-global image argument preserve the hypotheses

Let the new rational unit tangent at the identified cusp c have cocycle a(g) relative to the original tangent. It is unramified outside ell. In the original splitting, the new action and cocycle are explicitly

    rho_c(g) = Int(a(g)) rho(g),
    z_c(g)   = z(g) a(g)^(-1).

Normality of J and its original Galois stability imply stability under the new action. The preceding graph theorem applies to the tangent cocycle a itself, so a, rho_c, and z_c all factor through Gamma.

A local aligning conjugator u in Q is an element of the same geometric quotient used globally. Replace z_c by

    z_c^u(g) = u^(-1) z_c(g) rho_c(g)(u).

This still factors through Gamma. It also remains unramified outside ell: on each excluded inertia group rho_c is identity and z_c is1. By local cusp geometry one can choose u so that z_c^u(G_{Q_ell}) lies in I_c.

The image I_c is genuinely isomorphic to Z_ell(1). Its peripheral generator is primitive in N_n^ab, so I_c intersects N_n′ trivially, and therefore also intersects J trivially. It is stable for the cusp-based action, with cyclotomic action.

Now every gamma in Gamma is represented by a local element. Since z_c^u is a function of gamma, every global cocycle value is a local cocycle value. Hence all its values lie in I_c. This establishes a global cusp section directly. It needs neither a cusp-normalizer theorem nor an averaging or descent argument for nonabelian cohomology.

## 8. The three packets and their parameters are correct

For an odd coefficient ell,

    H^1(G_{Q,S},Z_ell(1)) = Z_ell kappa_ell(ell).

Kummer theory identifies the finite levels with S-unit classes; the units of Z[1/ell] are ±ell^Z and the odd-primary completion of ±1 is zero. Equivalently in the completed valuation description, unramifiedness kills every prime coordinate except ell. No degree-two phantom or convergence issue enters this degree-one calculation.

Every such ell-component can be placed in a full profinite cusp cocycle by taking zero at all other coefficient primes. Its resulting full cusp section localizes to cusp sections at every place, proving the asserted Selmer implication in the quotient sense.

Within a given packet, the map from inertia cohomology to V_n=N_n^ab cohomology is injective because H^0(G_Q,V_n/I_c)=0. The paper's good-Frobenius weight proof is valid. Alternatively, the compact Tate invariants vanish, and after passing to a finite field splitting the cusps the remaining toric quotient is a sum of Z_ell(1), which also has no invariants. Since Q retains V_n, distinct inertia parameters cannot become geometrically conjugate in Q.

Different centres have distinct images under the compact Kummer map on X_ell: the three cusp points have distinct Abel--Jacobi classes, and these classes lie in the ell-primary rational group. Thus the union is disjoint. The packet coordinate is an affine Z_ell coordinate relative to the specified unit tangent; changing an unramified tangent translates this coordinate without changing the packet classification.

## 9. Exact scope and useful cautions

The theorem includes J=1, J=N_n′, J=N_n″, and the positive intrinsic lower-central or derived quotients whose kernel lies in N_n′. It does not require J to be characteristic under every abstract automorphism; closed normal G_Q-stability is enough.

The assumption J contained in N_n′ is materially used three times: to retain the compact Tate projection; to keep cusp inertia injective; and to distinguish packet classes through abelianization. If it is removed, even J=N_n collapses the quotient to one section class and destroys the asserted three disjoint packets.

The unramifiedness hypothesis is on the whole cocycle, not only its compact or full abelian class. The new theorem applies to arbitrary sections satisfying that hypothesis. The attribution to LM6 E.16/LM7 E.34 is justified for the actual lifts built through their unramified graph quotient; it should not be silently expanded to every possible lift of their abelian inputs.

The local surjectivity theorem uses class number1 and the unique coefficient prime over ell. Neither an arbitrary number field nor arbitrary coefficient primes are covered. The graph factorization uses the actual geometric action coming from the free pro-ell tripod group; it is not a theorem for an arbitrary action on an arbitrary pro-ell group.

## Final audit conclusion

B.27 is a substantive theorem on the complete unramified section space, and the final text supports its stated generality. The coefficient-prime local condition alone forces the global cusp packet under these hypotheses. The main potential pitfalls requested by root—wrong arithmetic factorization target, improper use of local decomposition surjectivity, unsupported cusp descent, failure to retain inertia under J, and accidental restriction to a preconstructed tangent family—are all avoided in the written argument. The remaining deep dependencies are precisely the Part A rank-zero/Sha and exact local CM-conductor inputs already named in the manuscript.
