# Independent audit of E.13, E.18, E.T6 and E.20

Auditor: levels_geometry. This records a separate mathematical review of the owner’s complete statements and proofs. It does not alter the owner’s TeX. All conclusions below concern the exact maps and hypotheses in those statements.

## E.13: the covering-and-filling transfer

The proof was read in full. Its high-degree Hurwitz construction gives the required surjective map on completed fundamental groups; it does not require a congruence-subgroup assertion.

For fixed `(C,P_1,...,P_n)` and reduced pole divisor `D` of degree `d`, the equations `df(P_i)=0` are independent linear equations in `H^0(C,O(D))`. The bound `d >= 2g+2n+5` gives the simultaneous jet surjections used in the proof: for a jet subscheme of length at most `2n+4`, the residual degree is greater than `2g-2`. The bad incidences have the claimed codimensions. A multiple moving critical point imposes two conditions with one moving parameter; two moving critical points with the same value impose three conditions with two parameters; coincidence with a prescribed critical value imposes two conditions with one parameter. Vanishing of a required second derivative, coincidence of two prescribed values, or vanishing of a pole coefficient gives a proper linear condition. The good locus is therefore a nonempty open subset of the irreducible vector bundle over the allowed open subset of `Sym^d C`.

Every simple branched cover admits a target coordinate with infinity an unramified value. This identifies its fibre over the pointed curve with the quotient of the just-described irreducible parameter space by the coordinate choices. The same jet calculation in families gives smoothness, and irreducibility gives geometrically connected fibres. A connected finite étale cover of the moduli stack consequently has connected pullback to the Hurwitz space. By the finite-cover characterization of the profinite fundamental group, the induced map on fundamental groups is surjective.

The subgroup reconstruction in E.22 is exact. Before imposing the filling equation, a target point-push that lifts to the selected covering has image in the normalizer of the covering subgroup. Its forgotten lift is the corresponding deck transformation, so the equation `ua=u` selects the covering subgroup itself, rather than its normalizer. The selected sheet makes that lift unique. This remains valid on completion because the subgroup has finite index and the deck quotient is finite. The resulting action is the stated surface-group homomorphism, up to the explicitly allowed inner conjugacy.

For the completion of morphism orbits, one can make the continuity check explicit. The finite left action on the finite set of right mapping-class orbits first gives an open orbit stabilizer. Inside one orbit `S_u\M`, each left action is right-equivariant and hence induces an action on every finite quotient `S_u\M/N`, for `N` normal and of finite index. These finite actions extend to the full completion and determine the continuous action on `S_u\widehat M`. Composition extends through the same finite quotients; density then proves the relations. This supplies the finite-quotient explanation behind the proof’s continuity sentence.

The normal-closure recognition of a retained cusp also checks: abelianization of the punctured target group distinguishes the individual cusp vectors, including the omitted vector given by the negative sum of the others. The unique index-two ramification over each labelled simple branch value then singles out the retained marked point. No unproved faithfulness of an unlabelled covering functor is used.

Verdict: the exact transfer statement is supported. The literal `woheadrightarrow` typo in E.25 and a duplicated sentence in E.14 were reported to the owner separately.

## E.18: the full discrete outer-automorphism table

Independently viewed the actual facsimile of Ivanov’s *Mapping Class Groups*, Theorem 8.5.A, printed page 103, including its full proof. The excluded surfaces are exactly spheres with at most four holes and tori with at most two holes. In the closed genus-two case the theorem gives the extra central-character factor. The proof recognizes powers of twists, reconstructs the curve-complex automorphism, and compares its action on every twist to leave precisely the curve-action kernel. Thus its use in E.18 has the correct range and correction.

For ordinary types, the map from the extended normalizer quotient to `S_n x C_2` is the actual permutation-and-orientation map. Its kernel is the pure orientation-preserving group. The centralizer of that group in the extended group is trivial, by twist conjugation and faithful curve action, so the quotient computes outer automorphisms.

For `(1,2)`, the identified group `B_4/Z(B_4)` is the inverse image of the point stabilizer `S_4` inside the full five-point sphere group. Finite-index rigidity on the five-point sphere applies; `S_4` is self-normalizing in `S_5`. Thus only the orientation class remains. This uses an explicit subgroup of the correct sphere group, rather than an abstract comparison of unrelated automorphism groups.

For `(2,0)`, the nontrivial mod-two character is zero on the central hyperelliptic involution, because the involution word has length ten. Its central transvection therefore squares to the identity and is non-inner: an inner representative would fix every squared twist and hence every curve, forcing a central conjugator. Orientation reversal commutes with that character modulo two. The two classes give `C_2 x C_2`.

For `SL_2(Z)=C_4 *_{C_2} C_6`, quotienting the centre gives `C_2*C_3`. The maximal finite factors and their adjacent vertices in the Bass–Serre tree give its outer group `C_2`. An automorphism inducing the identity on this quotient is precisely a central character twist. The two displayed automorphisms `(r,s)->(r^{-1},s)` and `(r,s)->(r^{-1},s^{-1})` respect the amalgam relation and give the two independent classes.

Also read Nielsen’s original Sections III–IV, especially printed pages 395–397, in the saved original full text. The reduction to the exponent-sum matrix and simultaneous conjugation supplies the exact map `Out(F_2) -> GL_2(Z)` used at `(0,4)`. The original proof’s preceding pair-reduction argument was also inspected.

Verdict: every row of E.34 is supported, with its stated comparison map.

## E.T6: the unpointed genus-one algebraic stack

Read the complete new TeX and the executed output of `code/e_unmarked_genus_one.py`. The torsor equivalence, connected-inertia descent, and all the group-cohomology maps were checked independently.

The Jacobian construction identifies a genus-one curve with a torsor under its degree-zero Picard group. Its translation subgroup is the connected identity component of inertia. Quotienting that subgroup gives the pointed elliptic stack, so every autoequivalence descends there. At `j=1728`, the exceptional base automorphism inverts the order-four inertia. A lift would give an isomorphism of the translation groups intertwining the tangent characters `i` and `-i`. An invertible one-dimensional scalar cannot do that over the ground field. Thus the descended class is the identity.

For an equivalence over the base, its value on the trivial torsor and its map on that object’s automorphism group recover exactly the torsor `Q` and band automorphism. Generic elliptic automorphisms give only `+1,-1`. The relative group is consequently `H^1(B,E) semidirect {+1,-1}`. Forgetting the chosen comparison with the identity base functor identifies the band inversion with the global base two-automorphism `[-1]`.

The claim that `H^1(B,E)` is torsion is justified as follows. Restrict to a finite étale fine-level curve. A generic section of an elliptic torsor extends across its discrete valuation rings by properness, so restriction to the function field is injective. Over that function field, a finite extension gives a point; transfer kills the class by the extension degree. The finite étale transfer back to the stack then kills the original class. The zero section group is indeed zero: inertia `[-1]` forces any section into two-torsion, and the standard `SL_2(F_2)` monodromy fixes no nonzero vector.

The amalgam cohomology computation gives, for `M=(Z/n)^2`,

`H^1(SL_2(Z),M) = M[2]/M^R`,

because the `C_6` invariant and first-cohomology terms vanish (`det(S-I)=1`) and the restriction `H^1(C_4,M)->H^1(C_2,M)` is injective through `1+R`. It is zero for odd `n` and `C_2` for even `n`. For every divisibility `n|m` with `n` even, the inclusion on modules sends `(n/2,0)` to `(m/2,0)`, hence preserves the nonzero class. Alternatively, the already proved torsion statement and these groups show directly that every class has order at most two, so the whole group equals its two-torsion and is `C_2`.

The explicit cocycle has `z(R)=0` and `z(S)=(1,1)` modulo two. The relation `R^2=S^3` gives zero on both sides. A coboundary would require an `R`-fixed vector equal to `(1,0)`, which is impossible. Its affine actions on four points have orders `2,3,4` for `R,S,RS` and generate `S_4`, as the executed certificate records. Thus the displayed finite torsor algebraizes and supplies the nontrivial twist. Base inversion acts trivially on its order-two class, so the absolute quotient is exactly `C_2`.

Verdict: E.T6 is supported. The simpler torsion-union argument was suggested to the owner as a small presentational tightening.

## E.20: real genus-three centralizers

Read the complete statement and proof. Independently reopened Boggi–Zalesskii, arXiv:2406.08639v2, Theorem A (page 3), Definitions 1.1–1.2, Lemma 4.4, and the order-prime proof in Section 4.2 (pages 10–11). Only the order-two case is used. Its hypotheses require cohomology comparison for discrete continuous modules and finite virtual cohomological type; the stated finite-type and filtered-union argument supplies that requirement here.

### Pointed comparison

The injection of completed fibre groups into completed total groups follows from their inner actions in the automorphism groups of the finitely generated profinite fibres. The automorphism groups are profinite and the completed fibres are centre-free. For the configuration group, first apply this argument to its free-fibre extension over the closed surface group; its centre then vanishes because both kernel and quotient are centre-free. This orders the checks without a circular exactness argument.

The HM configuration-group injection makes a closed congruence-kernel element act inner on the two-point configuration group. Adjusting its lift by that group makes it centralize the configuration group. Its projected inner adjustment in the closed surface group is trivial, since the original one-pointed element already acts trivially on the based closed group. Centralization of the distinguished free fibre therefore gives the punctured congruence kernel. Conversely, representatives fixing the actual cusp generator differ by its procyclic centralizer, which is killed on filling, giving the map to the based closed automorphism group. This proves exactly the pullback square E.43.

### Primitive oval recognition

The following intrinsic construction makes the incidence step completely explicit. For a real cusp inertia subgroup `I` of the punctured real surface extension, its normalizer is `I semidirect C_2`, with inversion action. The two `I`-conjugacy classes of sections are the two classes modulo `2I`, and therefore are its two real branches. Real cusps are the vertices of the incidence graph. These local section classes are its flags. The images of the flags in the global section classes specify the adjacent real intervals, which are its edges. The discrete identification follows by lifting the reflection to the universal cover, and the order-two theorem preserves exactly that identification after completion.

In a cover pulled back from the filled surface, deleting the inverse images of the marked point gives local inertia maps of degree one. Thus the resulting incidence maps are honest graph coverings of the selected one-vertex, one-edge oval graph. The selected component has cyclic deck group `<a_i>/(<a_i> intersect N)`. All these graph constructions commute with the deck actions because they use conjugation, normalizers, inclusions and quotient maps. The deck transformation obtained by lifting one circuit is therefore the image of `a_i`, not an unspecified generator of the cyclic group.

An automorphism of the base graph permutes its two flags and has sign `epsilon=+1` or `-1`. The same flag permutation is inherited in every cover, hence the sign is independent of the subgroup `N`. Deck equivariance forces the image of the oval generator modulo each `N` to be the target generator to that sign. The cofinal family of reflection-invariant normal subgroups then gives equality in the full procyclic group. Retaining flags is essential even for cycles with one or two vertices. These exact normalizer, degree-one and equivariance explanations were sent to the owner for inclusion.

### Cutting and the centralizer

The five cut types in E.45 have the stated Euler characteristics and all have punctures and genus at most two. Fixing each oval and its orientation fixes both sides as well, because ambient orientation is preserved. Thus the pure cutting quotient in E.44 is correctly typed.

Boggi2014 Theorem 4.5 supplies the injective full completed twist lattice and the procongruence cutting quotient; its complete proof was independently opened earlier. D.19 supplies full equals procongruence for each cut factor. Right exactness of completion, followed by the already injective twist map, proves the full completed stabilizer comparison. The finite orientation and permutation quotients are unchanged, giving E.47 and the embedding into the full mapping-class completion.

Goodness of the cut factors follows from the explicit free-group towers, virtual freeness in genus one, and a finite-index subgroup of the closed genus-two group embedded in the six-point sphere group, followed by punctured Birman sequences. The twist extension and finite extensions preserve the necessary comparison and finite virtual type. BZ’s order-two centralizer theorem can therefore be applied inside this particular completed stabilizer. The oval recognition puts the entire procongruence centralizer inside it. The final unique factorization into the kernel fixed subgroup and the injected discrete-centralizer closure proves the topological semidirect product.

Verdict: E.20 is supported with the explicit incidence construction just described. The proof does not establish vanishing of the fixed congruence kernel and does not need such a statement.

## E.T7: the unringed elliptic modular topos

The complete new proof was read, including its comparison to E.T1. The generic group `C2 x Gal(k(t))`, the characteristic central factor, the local fixed-point gluing functors and their normalizer ambiguities give exactly the stated group of generic automorphisms. The normalizer of a nonzero power of a primitive inertia group remains that inertia group: pass to the finite-index subgroup where the power is a free basis element, compute its centralizer, and use abelianization to rule out a nontrivial conjugation power. The compatible finite-puncture quotients then give the asserted generic normalizers.

The local kernels can be verified by actual étale charts, strengthening the originally displayed potential-good-reduction substitutions. At zero put `t=w^3`, twist the generic family by `w`, and scale `x=w^2 X`, `y=w^3 Y`. Its equation becomes

`Y^2=X^3 - 3w/(w^3-1) X - 2/(w^3-1)`.

The linear moduli parameter has nonzero derivative at `w=0`, so this is an étale uniformizing chart. Its punctured map is `c_w -> (1,c_0^3)`. At one put `t-1=v^2` and twist by `v`; the good equation is

`Y^2=X^3 - 3(1+v^2)X - 2v(1+v^2)`.

Its constant-term parameter is linear at zero, so it is the other étale chart, with `c_v -> (1,c_1^2)`. These give the precise local subgroups and residual groups `C6` and `C4`. The original `s^6` and `s^4` substitutions compute the same inertial monodromy but ramify twice in the stack parameter; the actual charts were sent to the parent and incorporated.

For a generic automorphism `(e,g)->(e+chi(g),beta(g))`, preservation of ordinary local kernels forces `chi(c_x)=0` there, and the index-three kernel forces the same at zero. The index-two kernel at one imposes no condition. Kummer theory therefore leaves precisely the square classes `1` and `t-1`. Since `beta` fixes the inertia class at one and acts on its generator by a unit, it fixes the nontrivial character. Conversely every stated `beta` with zero character preserves each local kernel: all units are odd, which is exactly the parity used by both special kernels. This proves the split direct product in both directions.

The normalizer quotient at each point is its closed cyclic inertia group and supplies exactly the natural-isomorphism ambiguity of that closed topos. It removes the possible local gluing kernel. The algebraic ghost maps to the character of `t-1`, because the displayed discriminant has that square class. The piecewise-affine homeomorphism is supported away from the special points, preserves the specified local data, and its relative isotopy makes the action on the orbifold fundamental group trivial. Its nontrivial point permutation still moves subterminal opens. All comparison directions therefore check.

## E.T8--E.T9: higher-dimensional full-group and topos reconstruction

Read `sections/E_higher_topos.tex` in full, and reopened Pop2018 Theorems1.1--1.2 including the definition of Kronecker dimension. The stated input for k=Qbar and transcendence degree at least3 matches Theorem1.2(4): dimension(k)=1 and td>dim(k)+1. This audit checks the new reduction; it does not purport to independently reread every specialization argument in Pop's paper.

The full-Galois reduction in E.T8 passes. For every open normal H, uniqueness in the scalar-quotient reconstruction makes the recovered finite field map equivariant under the quotient G/H. Hence it preserves the fixed base field. The image of H in the maximal pro-ell abelian quotient has finite index, and that quotient is torsion-free: Kummer duality identifies it with Hom(K*/k*,Z_ell), with K*/k* free abelian via the divisor embedding. Agreement up to one scalar on this finite-index image extends to the whole target. The uniqueness clause then identifies the restriction with the base field map. The same argument for nested normal subgroups gives compatible finite maps whose union intertwines the original full Galois isomorphism exactly. There is no unaccounted scalar after this union.

The variety argument E.T9 passes. Generic localization is intrinsic; for a codimension-one geometric point the generic direct-image stalk is the inertia-fixed-point functor. Pro-Yoneda recovers its inertia subgroup up to conjugacy. Distinct divisorial valuations have different abelianized inertia lines, by Kummer pairing and weak approximation. The field isomorphism therefore matches the prescribed DVRs. Normal intersection recovers the entire structure sheaf and local ring maps. The generating-site recognition is valid: an arbitrary sheaf has an etale algebraic-space espace etale (equality of sections is an open relation); coherent objects give qcqs spaces; complemented diagonal is separatedness; quasi-finite separated Zariski Main over the scheme base makes these objects schemes. Applying the already proved locally-ringed-space reconstruction on slices, and the finite-extension compatibility of E.T8, makes the maps natural on the generating site. This excludes an additional automorphism in the kernel of generic restriction.

For the proposed DM extension, trivial automorphism groups of the closed geometric-point functors detect trivial inertia, hence an algebraic space, but alone do not detect a scheme. A separated normal algebraic space need not be a scheme. This does not invalidate the variety proof, where Zariski Main has a known scheme target. It requires an additional step for the stack extension.

There is a sufficient step for the modular stacks actually under study. Choose a finite etale level scheme atlas U→M. A topos equivalence sends it to an intrinsic finite locally constant object V. Trivial closed-point inertia implies that V is an algebraic space. It is finite etale over M. The moduli stack has a scheme coarse space; its coarse morphism is proper and quasi-finite. Therefore V→M_coarse is proper and quasi-finite, hence finite, and a finite algebraic space over a scheme is a scheme. The resulting scheme atlas and its fibre products can be reconstructed by E.T9 and descended. This establishes the needed atlas step for those moduli stacks without asserting a nonexistent scheme-recognition criterion for all separated DM stacks.

## E.26--E.27: direct normalizers and strict marked operad

Read both proofs in full. E.26 passes independently of Boggi2014 Section5. The Cardano Tietze semidirect calculation, full-topology comparison diagrams and actual rank-two subgroup L are explicit. The retraction argument works because an element normalizing L has its conjugated L-elements in L before applying the retraction. The odd-coset argument gives incompatible C-coordinates -1 and0. The peripheral finite-cover proof retains two distinct unramified cusp cosets and refines a torus cover through compactified mod-two homology to obtain at least four cusps; independent peripheral homology lines then exclude the alleged normalizer. This also proves the primitive-generator cases and the quotient PSL2 argument. The difference between the B3 centre and the squared node subgroup is correctly retained.

E.27 passes for the stated strict marked-pants operad. Reopened Bonatto--Robertson Definition3.1 (ribbon graph objects) and Proposition6.9's exact calculation on printed pages54--55. A permutation of the two future sewing labels disappears on contraction of that unordered pair, so the required branch-swapping morphism contracts to an automorphism of the same graph object. The ordered cut quotient is precisely Kgeo under the displayed geometric branch character. The two nonscalar odd-coset matrices force the inner conjugator into both index-two kernels; the free-generator centralizer and commutator abelianization then force the extracted parameter f to be1. The injected B3 gluing removes the remaining inner ambiguity up to a^nu. The actual G2 source word gives X^-nu=1, and X is the named free generator in the independently proved kernel. No general multitwist-normalizer theorem is used. The later extraction from the whole exit tower is not proved by this calculation and is correctly retained as a separate explicit comparison obligation.
