# The frozen-support gate after E.132–E.134

## What has been proved

E.132 gives matched class-four continuations of exactly the consistent finite E.125 prefixes, and therefore matched class five and global class six. E.133 gives a class-four matching failure after every legal prefix. E.134 shows that the E.123 compact elliptic gate is already necessary for class-four matching. None of these statements produces one pair which survives every depth.

For a **fixed pair**, B.26 and A.20–A.21 already provide the correct compactness theorem: nonempty matching fibres at every class have a compatible inverse-limit point. The remaining construction problem is nonemptiness for that one fixed pair, once its first support primes and their nonzero integer valuations have been frozen. Compactness over varying pairs is unavailable.

## The precise limit of the fixed rational reference

Let q be a fresh support prime away from the fixed rational reference point's bad primes, and let m be the nonzero ordinary valuation on one peripheral axis. The reference section has zero inertia at q. The candidate ghost has abelian inertia m times that axis. Therefore their reductions already differ in the abelian quotient modulo 3^(v3(m)+1). Geometric conjugacy cannot remove this discrepancy in an abelian quotient.

E.130 avoids this discrepancy only in a **fixed finite quotient** which kills every fresh inertia exponent. Increasing that quotient cofinally while retaining the same rational reference would force m to be divisible by all powers of three, contrary to m being a nonzero ordinary integer. For E.125's first exponent 11!, v3(11!)=4, so comparison with the point 5/16 already fails at abelian modulus 3^5. This is a failure of that proposed normalization mechanism, not an obstruction to a section whose reference is allowed to change.

## A genuinely smaller finite-field question

Fix a finite field F_q with q≠3 and q≡−1 modulo3, an interior point t in P1(F_q)−{0,1,∞}, and a specified rational tangent at one cusp. Can their full geometrically pro-three section classes coincide?

This is a question about a **Frobenius complement**, not equality of the full decomposition groups. A cusp decomposition group has a nonzero inertia subgroup. Its procyclic Frobenius complement could, a priori, coincide with the decomposition group of an interior point without the two full decomposition groups being equal or commensurate.

There is an exact rational-path reformulation. At nilpotent class r, embed the torsion-free integral pro-three free nilpotent group N_r into its rational unipotent completion U_r(Q_3). Relative to the cusp section, let F be the arithmetic Frobenius automorphism and let z_t be the point cocycle value. The equation

    z_t = g^(-1) F(g)

has a unique solution in U_r(Q_3). Indeed, in weight i the correction equation has linear coefficient q^i−1, which is nonzero in Q_3; induction through the central series gives existence and uniqueness. The solutions are compatible as r varies. The two section classes coincide integrally if and only if every solution lies in N_r: one direction is immediate, and the other follows from compactness of the nonempty integral solution sets in the free pro-three group. Equivalently, one must decide integrality of the unique rational-unipotent Frobenius-invariant path. Showing that some coordinate fails integrality for every interior t is the exact separation statement still not proved here.

Even a proof of this finite-field separation would only rule out imposing the **same rational-base cusp Frobenius** at a frozen new support through all finite quotients. An actual ghost has nonzero inertia at that support and may change its higher global section data; no implication to the main finite-support conjecture has been established.

## Opened primary sources and exact limitations

1. Saïdi and Tamagawa (2009), *A prime-to-p version of Grothendieck's anabelian conjecture for hyperbolic curves over finite fields of characteristic p>0*, Publ. RIMS45,135–186. Opened the full primary PDF at https://empslocal.ex.ac.uk/people/staff/ms220/Site/Publications_files/publRIMS.pdf. Checked Lemma1.7, Proposition1.8, Corollary1.11, Proposition1.21, Corollary1.22 and Proposition1.23, printed pp144–157. Proposition1.8(ii) and Corollary1.11(ii) separate full cusp decomposition groups from the exceptional decomposition-group collisions. They do not prove the Frobenius-complement assertion above. The finiteness theorem for the exceptional set also requires a cofinite prime set, which a single coefficient prime does not satisfy.

2. Wakabayashi (2012), *On the cuspidalization problem for hyperbolic curves over finite fields*, RIMS1750, primary PDF https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1750.pdf. Opened and checked TheoremsA–C and their exact scope. These reconstruct cuspidalizations/configuration-space groups from specified Frobenius-preserving isomorphisms. The hypotheses do not directly give point-versus-cusp Frobenius-complement separation.

Searches used both available engines with combinations of “pro-l fundamental group finite field decomposition groups distinct rational points cuspidal sections”, “pro-l finite field decomposition groups injective”, and “finite fields cuspidal sections pro”. No exact theorem establishing the smaller assertion was located in the opened material. This records a search boundary, not a claim that no such theorem exists.

## Current unresolved implication

One must either construct a fixed infinitely supported ordinary pair whose successive pinned even-layer matching systems are all nonempty, or prove that some frozen support eventually makes such a system inconsistent. The controlling finite sets of support primes in E.69 depend on both the weight and the predecessor section. No uniform controlling set and no compatible extension theorem for all higher weights has been proved.

## 2026-11-18 05:40 UTC: the exact all-prime class-two gate

The necessary local hypothesis furnished by A.31 is **point matching at support primes q in coefficient components ell different from q**. It does not furnish matching at the equal coefficient prime or at a zero-valuation place. The stronger phrase “everywhere point-matched” must not be substituted for this statement.

E.137 makes this earlier gate exact. Fix any of the 24 global integral class-two classes above an ordinary pair. At a support prime q the difference from the actual local point, over all off-diagonal coefficient components, is a finite cyclic coordinate D_q in Z/(q²−1). Only coefficient primes dividing q²−1 matter. For q≥5 the global twist generator eta restricts to (q²−1)/24 and embeds Z/24 as the order-24 subgroup. Thus each such place either excludes all 24 candidates or pins exactly one. A ghost passing every place has a unique matching class; if no class passes, at most two support places witness the failure. Passing the gate yields a global integral class-three section by B.25 and the weight-three fixed-ramification H² vanishing. It does not preserve matching at class three or solve any subsequent layer.

No construction in the checked sources presently establishes an infinite-support ordinary pair passing this **all-coefficient** gate. E.123/E.125/E.132 impose matching in coefficient three and must not be promoted to all coefficients. The selected failures E.121 show actual support-place defects; E.83's zero-support failure is a distinct stronger local condition and does not itself exclude the off-diagonal support gate.

The current constructive difficulty is concrete. At a newly selected support q, the complete class-two test involves every prime divisor of q²−1. A finite Chebotarev prescription can control a preassigned finite set of coefficient moduli, but those remaining divisors are not known before q is chosen. E.127's simultaneous geometric image helps with any fixed finite collection of actions; it does not by itself solve this varying-modulus requirement. This is a limitation of the attempted argument, not a proof of nonexistence. Scheduling later corrections may alter the abelian pair and the canonical central class, but no simultaneous extension lemma preserving all earlier ordinary local conditions has been proved.

The available metabelian/Alexander constructions E.98–E.100 have zero intrinsic abelian coordinates relative to a rational tangent and fail tripod ordinarity at Q2, as independently reported by the literature audit. Their existence therefore does not settle this gate. Fixed-S unipotent or finite-descent theorems additionally require a fixed finite ramification set and/or full local geometric conditions. Infinite-support ordinary pairs are outside that fixed-S hypothesis, even though every finite coefficient reduction has finite ramification.

Fermat/Jacobian descent also cannot simply be read off from a class-two section. Abelianizing an open subgroup of the geometric fundamental group is not the same operation as taking the class-two quotient of the original group: deck conjugation on that subgroup's abelianization generally remains nontrivial. The actual triangle calculation E.134 illustrates the obstruction quantitatively: its H3 quotient is class two, but the compact E-prime[3] kernel first occurs in the class-four quotient of order243. Even that specific finite compact torsor was not supplied by an arbitrary class-two lift. Thus a theorem about full metabelian or abelian-by-finite descent needs an additional quotient/lifting argument before it can constrain the exact E.137 set.

## 2026-11-18 07:58 UTC: the class-two gate is now nonempty

The earlier 05:40 nonexistence-of-a-construction statement is superseded by E.171–174 in `sections/part_E_all_prime_class_two.tex`. Their complete proof has passed full independent reads by root and cohomology. Starting from (23/64,41/64), one treats each coefficient ell>=5 once by the relative approximation theorem E153, preserving the local diagonal-curve arithmetic invariant. All later support primes are nonexceptional at that coefficient. The two small coefficients use fixed actual finite point sections, and E171 proves that one global C24 twist matches them simultaneously. The final pair has infinite support, frozen ordinary integer valuations, actual ordinary local limits, all-prime off-diagonal class-two support matching, and a global class-three lift. No full pronilpotent section or next-layer matching has been constructed.

The method's finite-weight limitation is exact. A residue q modulo ell can avoid q²=1, but it cannot avoid q^w=1 for every weight: its multiplicative order divides ell−1. Thus a new support prime can be made permanently irrelevant to the class-two local fibre, but cannot be made permanently irrelevant to the entire tower merely by a finite nonexceptional congruence. This identifies the point at which the once-per-coefficient proof ceases to apply; it is not a nonexistence theorem for another construction.

### Harmonic torsor route: a precise failed inference

For odd ell, the point1/2 and a suitable infinity tangent have the same abelian pair, since the ell-primary Kummer class of−1 is zero. At q≡−1mod ell, odd-weight local H1 vanishes. Neither observation proves equality of the full local sections.

Root supplied a direct finite countermodel to the proposed inference from odd generators. In the exponent-ell Heisenberg group with symmetric coordinates, let Frobenius act as F(a,b,z)=(-a,-b,z). The generators have odd weight, but their central commutator has even weight. Every central value (0,0,z) defines a distinct twisted-conjugacy class with zero abelianization: a conjugator preserving zero abelianization must satisfy−2a=−2b=0, hence a=b=0, and such a central conjugator cannot change z. Consequently even an integral free presentation on odd-weight generators does not make the nonabelian Lang map surjective. An actual arithmetic identity killing the even central torsor coordinates would be required; none has been proved.

The harmonic swap X↔Y likewise has fixed Lie classes in degrees1 and3; the degree3 class [X−Y,[X,Y]] is fixed. Their bracket supplies a fixed degree4 class. The coprime involution centralizer therefore cannot be reduced to a rank-one cusp inertia group merely from its first graded piece.

A rank-zero elliptic shortcut also fails without another hypothesis. The expected pointed harmonic H3 compactification is the j=0 curve y²=x³+1, with translated base P0=(-1,0) of order2. Even if its rank and 3-Selmer are calculated, E112's identification of absolute continuous H1(T3E) with the rational completion used density of rational points in E(Q3)^completion3. A rank-zero curve lacks that density and may leave a Weil–Châtelet Tate-module direction supported at the coefficient prime. No harmonic-fibre exclusion has been deduced from rank0.

### The exceptional coefficient-three relative module

Modulo3, V_b has determinant chi³=chi, so its alternating determinant pairing identifies it with its Tate dual. At an auxiliary q≡−1mod3 where b is locally zero, the ordinary A condition is the ramified first-coordinate line; its local Tate annihilator is another ramified line under the self-duality. Thus the free-auxiliary-prime descent used in E153 no longer applies: dual classes may acquire new permitted ramification. Cohomology identified the exceptional universal dual cocycle z_b=(b²/2,b) and proved its pairing with actual point targets vanishes by the third-obstruction/eta reciprocity identity. This handles that specific class, not every ramified dual class.

For genuinely Lagrangian old local conditions, a Ramakrishna-style replacement of an unramified condition by a transverse ordinary line might remove detected Selmer classes. The frozen ordinary-point problem instead fixes exact old targets, hence uses zero homogeneous local condition there. The balanced self-dual argument does not automatically apply. No ordinary auxiliary-prime theorem, no automatic plus-gate consistency, and no infinite branch have been proved from this observation.

## Exact harmonic finite-field test and the field F5

This is a proved necessary test and a small-field separation result, not a universal separation theorem or an all-depth ghost obstruction. Its executed certificate is `code/ghost_audit_harmonic_finite_field.py`, with saved `.out`.

Let q be an odd prime power with q≡−1mod3 and characteristic different from3. Consider the degree-nine geometric three-cover of the tripod

    C: u³+v³=2w³,       t=u³/(2w³).

The point t=1/2 has the unique F_q-point lift P=(1,1,1), since cubing is bijective on F_q. The infinity cusp has the unique F_q-boundary lift R=(1,−1,0). If the full geometrically pro-three point section and infinity tangential section coincide, their lifts to this actual cover coincide; after compactification or after any Kummer cover of its punctured locus they still coincide. The same applies after extending constants to F_q².

Let r³=2 in F_q and let ζ be a primitive cube root in F_q². The lines

    L_r=u+v−rw,       L_rζ=u+v−rζw

each cut the cubic at three distinct boundary points: its u=0 point, its v=0 point, and R. This follows by substituting u+v=rw into the cubic, which yields3ruvw=0. Their ratio f=L_r/L_rζ is therefore an invertible function on the punctured cubic and defines actual Kummer three-covers there. At R both lines vanish simply, with leading terms−rw and−rζw, so f(R)=ζ⁻¹, independently of the tangential parameter. At P,

    f(P)/f(R)=((1+rζ)/(1+r))².

For the identity, use (1+r)³=3/(r−1), hence2−r=3r/(1+r)², and apply the same identity to rζ. Therefore a full point/infinity collision forces1+rζ to have trivial three-primary component in F_q²×; the denominator1+r lies in F_q× and has prime-to-three order. This requirement comes from the full Kummer tower of f. Merely being a cube is equivalent to it when v3(q²−1)=1, but not in general.

At q=5 one has r=3 and

    (1+3ζ)^8=ζ²≠1.

Thus infinity is separated. The compact cubic C has exactly six F5-points. With P as elliptic origin, swapping u and v is the nontrivial involution fixing P, hence inversion. Its only rational fixed points are P and R, so C(F5)[2]={P,R}. The finite cusps Qu=(0,3,1) and Qv=(3,0,1) are outside that subgroup and consequently have nonzero three-primary Abel–Jacobi difference from P. The multiplication-by-three cover detects this difference. Its restriction to the punctured curve, and the Galois closure over the original tripod, have geometric three-power degree. This excludes collisions with both finite cusps. The S3 symmetry of the tripod is transitive on its three F5-interior points, proving that no interior point of U(F5) has the same full geometrically pro-three class as any cusp.

The single unit test passes at q=47 and83; this is not evidence of a full collision. Higher covers and additional units remain untested there. The proof above only refutes the proposed universal harmonic collision for all q≡−1mod3.

### A higher Fermat necessary family, not yet a separation proof

For n>=1, the cover u^(3^n)+v^(3^n)=2w^(3^n) again has unique F_q lifts P=(1,1,1) and R=(1,−1,0). Let r_n be the unique3^n-th root of2 in F_q, and let ζ_n be a primitive3^n-th root over a finite extension. The tangent-line ratio

    (v−r_n w)/(v−r_n ζ_n w)

has divisor supported at boundary points, and has value1 at R. A collision forces its value at P, (1−r_n)/(1−r_n ζ_n), to be trivial in the three-primary multiplicative completion of that constant extension. This is a genuine infinite sequence of necessary tests, but no proof that one fails for every q has been obtained. Norms down the constant-field tower alone lose higher three-primary digits, so vanishing of their norms is insufficient.


## 2026-11-18 09:09 UTC: finite-field point/cusp separation is proved

The earlier finite-field separation question is now resolved by E.192--194 in `sections/part_E_finite_field_detector.tex`. The preceding failed shortcuts and finite computations are retained as a dated record, not as the current status. Over every finite field of characteristic different from3, the family y²+3xy+ty=x³ has a rational exact3-torsion section, so its actual geometric3-adic Tate monodromy is pro3. At zero it is split multiplicative, and every cusp Frobenius has trace q+1, independently of its tangent/inertia. An interior fibre has trace q+1−#E(Fq), with1≤#E(Fq)≤2q+1. This gives a finite detector whenever3^N>2q+1. Tripod automorphisms treat every cusp. The split Legendre family y²=x(x+1)(x+t) proves the coefficient-two counterpart in characteristic different from2.

In E.135, the first nonintegral rational Frobenius-path coordinate consequently occurs by weight3N−2; for q≡−1mod3 its weight is even. The bound follows because the detecting geometric matrix image is a three-group of order at most3^(3N−2), hence has nilpotency class at most3N−2. Full independent source/proof reads by root and cohomology are positive. The finite certificate verifies the algebra and examples but is not the universal proof.

E.193 gives the exact constructive limitation: once a support prime q is frozen, an ordinary boundary point there cannot retain the Frobenius class of a fixed reference point with good interior reduction in every cofinal finite three-group quotient. It must fail by the explicit detector. Finite prescriptions before q is selected remain valid, and changing higher global section data afterward is not excluded. For any actual full ordinary section, the relevant cusp-specific elliptic representation must have Tate local form and trace q+1 at its off-diagonal support places. This alone does not force finite ramification of that global linear representation and does not settle the main all-depth ghost question.


### Global scope after the elliptic detector

The induced global3-adic representation is not automatically finitely ramified. At an A-support prime the original family is split multiplicative; at a B-support prime its node is nonsplit when q≡−1mod3. For the latter, translating the t=1 node to the origin gives tangent polynomialY²+3XY+3X², which splits precisely when the residue field containsμ3. Thus the A/B Frobenius traces are q+1 and−(q+1), respectively, in that residue class.

For the23/64,41/64 support pattern, these two local conditions force the representation to be absolutely irreducible. Indeed, a reducible constituent whose residual character is1 would take values1 at23 and−41 at41. By Kronecker--Weber and continuity, the logarithm of any continuous3-adic one-dimensional global character is a scalar multiple oflog⟨χ3⟩: all other local unit factors have dense torsion and hence zero additive logarithm. The value1 at23 forces that scalar to vanish, leaving a finite-image character, which cannot take value−41. This is a necessary property, not a new infinite-support contradiction: the same argument already applies to the genuine rational reference pair5/16,11/16.

A cusp-specific detector is potentially good of order3 at one cusp and multiplicative at the other two. Large3-divisible valuations at the first cusp can kill its inertia, but no single choice kills the two remaining directions. If an ordinary pair had support in only one direction outside a finite set, one of A, B or A/B would have finite support, and E101 would force the entire pair to be rational. Thus an infinite ordinary pair does not acquire finite ramification of one such representation merely by concentrating the eventual support in a single cusp direction. Killing bounded3-power inertia at all three cusps instead returns to the compact triangle/Fermat quotients already considered. No Fontaine--Mazur or finite-ramification conclusion is justified here.

## 2026-11-18 09:30 UTC: the coefficient-three Hodge premise remains missing

E.200 now proves the precise global detector statement: for any ordinary infinite-support pair admitting a full geometrically pro-three section, all three cusp-specific elliptic representations are infinitely ramified and at least two are absolutely irreducible. The proof was fully reviewed by root and cohomology_audit. This is a conditional necessary test, not an existence or nonexistence theorem.

Neither A.31 nor E.68 identifies the coefficient-three restriction with the local ordinary point section. A.31 is off diagonal. E.68 describes successive central Tate-layer discrepancies, whereas the two-dimensional elliptic detector has non-unipotent geometric image and need not factor through any fixed integral nilpotent class. No passage from those separate finite rational unipotent comparisons to a de Rham or Hodge–Tate comparison for this detector has been proved. The cohomology reviewer independently confirmed this exact limitation; we do not assert that the desired local Hodge property is false.

Primary source checked: Mochizuki, S. (1999), *The local pro-p anabelian geometry of curves*, author PDF [https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf). Definition 3.4, Proposition 3.5 and the following remark are on author p.27; they concern the action defined by a geometric point and its weight-zero/Malcev comparison. Definition 4.3 and Proposition 4.4, author pp.31–32, express an additional splitting/J-geometricity condition. Proposition 5.4, author p.34, transports a geometric section through an **open** homomorphism. These statements do not supply that condition for an arbitrary section of the original projection. The paper’s Theorem C, author p.5, proves injectivity of the point-to-section map, not its surjectivity.

Even a local Hodge conclusion would not by itself establish finite ramification. As a scope check, Ramakrishna, R. (2000), *Infinitely ramified Galois representations*, *Annals of Mathematics, 151*, 793–815, [published primary PDF](https://emis.de/ft/50658), Theorems 1–2 on p.794, constructs surjective infinitely ramified representations for a density-one set of coefficient primes at least five; under GRH, Theorem 2 also makes them crystalline at the coefficient prime. These results are not coefficient-three examples with our residual or peripheral conditions, and are not being used as counterexamples to the present section problem. They explain why a generic implication from a local crystalline condition to finite global ramification is unavailable.

At zero-support places, ordinarity alone also does not identify the full local section with the ordinary point. Hence the detector is not known to have the trace of a good elliptic fibre there. No global compatible system, purity statement, or finite conductor has been obtained. A.33’s support-density-zero theorem uses only ordinarity and supplies none of those missing premises.

## 2026-11-18 10:06 UTC: the original coefficient-five c0 gate has a conditional finite reduction

E.205 proves that, for any fixed legal minimal-five-shell first pair, consistency of E.202's two-by-two finite affine system is equivalent to existence of an unchanged original-factorial continuation passing the entire continuous coefficient-five third obstruction. One-stage delayed root-of-unity corrections force D_j into5^{v5(n_j)} and make the divided residues tend to zero. This supersedes the earlier statement that the later coefficient-five c0 condition was an additional unhandled requirement after first-system consistency. It does not solve the first system, the other coefficient primes, or higher depths.

E.208 isolates a sufficient first-prime condition: one fully legal q0 with ell_q(3U_q)=0 permits the original r0 selection to make both off-diagonals nonzero in independent weight-two/weight-three fixed fields, forcing an invertible first matrix. Primary quintic reciprocity rewrites that first diagonal as ell_q(3)+2ell_q(sigma2 pi_q) for a primary pi_q. No distribution theorem or legal prime with that value has been proved. The full exact status, original CRT restrictions, source locators and exploratory-computation limits are in notes/ghost_audit_first_five_gate.md.

## 2026-11-18, 10:31 UTC: unconditional original coefficient-five gate

E.213 removes the first-pair premise from E.211 by a two-candidate-prime Chebotarev construction, retaining every original CRT/radical condition. The original factorial family therefore has ordinary infinite-support pairs with full integral pro-five class-two matching at all support primes and a global pro-five class-three lift. This resolves the original coefficient-five first-system and later class-three convergence gates together. It does not establish another coefficient, matching at class three, or a full pro-five/pronilpotent section. The quintic spin distribution question is no longer needed for this result.
