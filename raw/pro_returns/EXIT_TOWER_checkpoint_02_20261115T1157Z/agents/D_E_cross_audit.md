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
