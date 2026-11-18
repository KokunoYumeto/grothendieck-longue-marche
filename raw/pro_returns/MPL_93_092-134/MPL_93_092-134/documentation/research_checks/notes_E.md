## E. Uniformization, algebraicity, and formal projective data

### E01 — Mere homogeneity does not imply the three uniformization types

**File/location:** cote 93, scan 126, definition and Theorem 1(a),(b). **Kind:** own idea. **Confidence:** high, by a connected counterexample.

Under the written definition, \(D=\mathbb P^1-\{0,\infty\}=\mathbb C^*\) is homogeneous, since \(z\mapsto az\) acts transitively. It is neither simply connected nor projectively equivalent to any of the three listed domains, so the implication from mere homogeneity is false and adding connectedness is insufficient. The later construction uses universal covers, which are independently simply connected, and can use the intended uniformization models without this erroneous implication.

**Context:** Contradicts H-Xa, p. 125/scan 126, where Hua repeats the same unqualified three-domain assertion; S20 supplies no missing hypothesis.
**Context query:** homog|simplement connexe|uniformisation
**Check:** independent re-proof || Multiplication is transitive on C*, whose fundamental group is Z; scan126.homogeneous_classification refuted, refined statement E01.simply_connected_scope.

### E02 — The disk stabilizer is the positive real-projective component

**File/location:** cote 93, scan 126 corollary, continued on 127. **Kind:** unproved claim.

The full equality \(\mathrm{PGL}_2(\mathbb R)=\mathrm{SL}_2(\mathbb R)/\{\pm1\}\) is false on real points. Since \(\operatorname{Im}((az+b)/(cz+d))=(ad-bc)\operatorname{Im}(z)/|cz+d|^2\), the upper-half-plane stabilizer is the positive-determinant component, isomorphic to \(\mathrm{PSL}_2(\mathbb R)\); a negative determinant exchanges the two half-planes. Scalar multiplication changes the determinant by a positive square and does not eliminate this distinction.

**Context:** Rechecks and credits H-Xa's correction, pp. 125–126/scans 126–127; the frozen displayed equality is unchanged.
**Context query:** PGL|PSL|composantes|GL.*R
**Check:** targeted proof check || Direct imaginary-part calculation and the witness z→-z; refined statement E02.positive_component.

### E03 — A real form need not have a real boundary circle

**File/location:** cote 93, scan 127, correspondences \(\alpha\)–\(\delta\). **Kind:** own idea. **Confidence:** high, by an explicit fixed-point-free real structure.

The antiholomorphic involution \(z\mapsto-1/\bar z\) defines a real form of \(\mathbb P^1_\mathbb C\) with no real point, since a finite fixed point would have \(|z|^2=-1\). It therefore cannot produce the circle and complementary pair of disks used in the manuscript's correspondence. The intended comparison must restrict to split real forms, or equivalently here to real conics with a real point, rather than all real descents of the group or Lie algebra.

**Context:** Confirms the split qualification added by H-Xa, p. 126/scan 127; its wording about real structures should still retain the real-point condition.
**Context query:** forme réelle|descente|split|compact|cercle
**Check:** targeted proof check || The fixed-point equation has no solution; the conic x²+y²+z²=0 provides the corresponding algebraic model.

### E04 — “Invariant metric” needs its group specified

**File/location:** cote 93, scan 126, parenthesis in the third uniformization type. **Kind:** reading question.

The parenthesis about “métriques … invariantes” cannot mean a positive Riemannian metric on \(\mathbb P^1\) invariant under all of \(\mathrm{PGL}_2(\mathbb C)\). A dilation fixing 0 multiplies a nonzero tangent vector there by an arbitrary positive factor, contradicting invariance of its norm. A round metric invariant under a chosen compact rotation group, or the hyperbolic metric on a disk, is a different statement, so both the intended group and the written \(X/P\) notation need clarification.

**Context:** Adds a reading question not resolved by H-Xa, p. 125/scan 126; no contextual normalization of the sentence is imported.
**Context query:** métrique|riemann|invariant|disque
**Check:** targeted proof check || The isotropy dilation at 0 precludes a positive metric invariant under the full projective group.

### E05 — The “pour iso” restriction should be carried into the Scholie

**File/location:** cote 93, scan 126(c) and scan 127, Scholie. **Kind:** reading question.

Scan 126 inserts “pour iso” twice, providing the groupoids on which the projective completion functor in scan 127 is naturally read. This is a material qualification already present in the manuscript, not a new error to attribute to it. An extension to all holomorphic maps would fail, for example because \(\exp:\mathbb C\to\mathbb C\) does not extend to a morphism \(\mathbb P^1\to\mathbb P^1\).

**Context:** Clarifies the morphism category left implicit in H-Xa, pp. 125–126/scans 126–127; the universal-cover construction needs only isomorphisms.
**Context query:** foncteur|pour iso|simplement connexes
**Check:** used and rechecked in this run || Checked the two explicit category insertions and their use in the Scholie; the exponential witness refutes only the overbroad interpretation.

### E06 — A quotient model checks the canonical bundle construction

**File/location:** cote 93, scans 127–128, “fibré projectif canonique” and Theorem 2. **Kind:** unproved claim.

Writing \(X=D/\Gamma\) with \(D\) a simply connected uniformization model, set \(P_X=(\mathbb P^1\times D)/\Gamma\) and \(\widetilde X=(D\times D)/\Gamma\) for the diagonal deck action, extended by Möbius transformations on the \(\mathbb P^1\) factor. The section \([z,z]\), the map \(p([u,z])=(q(u),q(z))\), and the distribution with \(u\) constant give exactly the marked section, universal-cover fibers, and compatible flat connection. The section is transverse, and the uniqueness assertion includes these universal-cover conditions rather than asserting uniqueness among all projective connections on \(X\).

**Context:** Gives an explicit construction checking H-Xa, pp. 126–127/scans 127–128, and the germ explanation in the margin; classical uniformization itself is background.
**Context query:** groupoïde|système local|revêtement universel|marquée
**Check:** targeted proof check || Verified equivariance, descent, the universal-cover fibers, and transversality in the quotient model; the global uniformization theorem was not re-proved.

### E07 — The sphere case has no nontrivial unramified quotient

**File/location:** cote 93, scan 129, first case, “a un pt fixe au moins”. **Kind:** unproved claim.

The sphere case uses the fact that every nonidentity Möbius transformation has a fixed point over \(\mathbb C\), whereas deck transformations act freely. Therefore a Riemann surface whose universal cover is \(\mathbb P^1\) is itself \(\mathbb P^1\), and the displayed product construction follows. The freedom condition is essential: branched quotients by finite projective groups are not counterexamples.

**Context:** Rechecks H-Xa, p. 128/scan 129; no relation to the finite-group actions in the unrelated results-register headlines is inferred.
**Context query:** point.*fixe|sphère|sphere|revêtement
**Check:** targeted proof check || Solving the fixed-point quadratic for a Möbius map and using freeness of a deck action gives trivial deck group.

### E08 — The plane-covered list follows from translations

**File/location:** cote 93, scan 129, second case and margin, “sont des translations”. **Kind:** unproved claim.

An affine map \(z\mapsto az+b\) with \(a\ne1\) has a fixed point, so a deck group acting freely on \(\mathbb C\) consists of translations. Its discreteness makes it a lattice of rank 0, 1, or 2 in the real two-dimensional vector space \(\mathbb C\), giving \(\mathbb C\), \(\mathbb C^*\), or an elliptic curve. This verifies the listed cases and explains the torsor interpretation without choosing an origin on the original curve.

**Context:** Restates and checks H-Xa, p. 128/scan 129; the actual mathematical point is the affine deck action, not the doubtful wording beside the quotient labels.
**Context query:** translations|rang|elliptique|torseurs
**Check:** targeted proof check || Fixed-point calculation reduces to a discrete translation subgroup; the elementary lattice classification is used.

### E09 — The tangent-bundle connection is affine, not linear

**File/location:** cote 93, scans 129–130, “fibré en droites affines”. **Kind:** unpursued implication.

The zero section of the tangent-bundle model is the marked transverse section, so the horizontal distribution cannot preserve it as a linear connection would. The invariant equation \(dw+\eta=0\), with \(\eta\) a nonzero invariant differential and \(w=\eta(v)\), gives an algebraic affine connection and extends to the projective completion with infinity horizontal. Rescaling \(\eta\) and \(w\) together leaves the distribution unchanged, giving a coordinate-independent construction on the one-dimensional group torsors in scan 129.

**Context:** Adds an explicit model to H-Xa, pp. 128–129/scans 129–130, and verifies why the manuscript says the connection does not respect the vector-space structure.
**Context query:** affines|vectorielle|tangent|connexion
**Check:** independent re-proof || The algebraic distribution dw+eta=0 is invariant under the coordinate rescaling and has translational vertical part, which extends to P1.

### E10 — The unfinished multiplicative case can be written explicitly

**File/location:** cote 93, scan 130, final unfinished \(\mathbb C^*\) case. **Kind:** own idea. **Confidence:** high, by an explicit algebraic distribution and analytic covering map.

For \(X=\mathbb G_m\), put \(\eta=dx/x\) and \(w=v/x\) on its tangent bundle; the horizontal equation is \(dw+dx/x=0\). The analytic covering is \(p(x,w)=(x e^w,x)\), and \(d\log(xe^w)=dx/x+dw\) verifies compatibility with the product connection. Thus the bundle, connection, zero section, and infinity section are algebraic, while the covering map is transcendental; locally \(s=\log x\) gives \(G_x(s)=-1/x^2\).

**Context:** Extends H-Xa, p. 129/scan 130, which leaves this case at the same transition; answers the affine algebraicity question here, not the general nonproper question of scan 115.
**Context query:** algébrique|G.*m|mathbb.*C.*ast|affines
**Check:** computation or formal certificate || additional_checks.txt verifies G_x(log x)=-1/x²; direct differentiation verifies the covering-map horizontal equation.

### E11 — Algebraic formal data can have a transcendental realization

**File/location:** cote 93, scans 130–132, “prouver (ou l'infirmer !)” and the formal map. **Kind:** own idea. **Confidence:** high, by the multiplicative example.

The series \(x\exp(w)=x\sum w^n/n!\) has coefficients in \(\mathbb C[x,x^{-1}]\) and invertible linear coefficient, so it defines an isomorphism of the indicated formal completions over \(\mathbb G_m\). Its analytic covering map cannot be algebraic, since restricting it to a tangent fiber would give a nonconstant algebraic map \(\mathbb A^1\to\mathbb G_m\), whereas every invertible polynomial is constant. This explains why algebraicity of the connection and formal datum does not algebraize the whole covering map, and why scan 132 singles out \(\mathbb A^1\) for an algebraic \(p\).

**Context:** Adds a precise distinction to H-Xa/H-Xb, pp. 129–131/scans 130–132; the margin on scan 130 can refer to the connection without asserting algebraicity of the exponential.
**Context query:** formel|algébrique|prolonger|revêtement
**Check:** independent re-proof || Formal inverse exists by the unit linear term; units of C[w] are constants, ruling out an algebraic exponential covering.

### E12 — Deligne algebraizes the flat object, not the extra section automatically

**File/location:** cote 93, scan 131, items a), b), c) and the final insertion. **Kind:** self-flagged.

The insertion “mais pas l'algéb. de c !” refers to item c), the section \(\sigma\), while the connection is item b). Deligne [B2, II, Theorem 5.9] gives existence and uniqueness, up to the appropriate isomorphism, of the regular algebraic flat object corresponding to an analytic flat object; the projective version follows through its faithful tensor description. An arbitrary transverse marked section is extra nonhorizontal data, so its algebraicity remains the separate issue explicitly preserved by the manuscript.

**Context:** Refines H-Xb, p. 130/scan 131, whose compressed “uniqueness / not existence of \(\sigma\)” gloss does not fully reproduce the manuscript's distinction.
**Context query:** Deligne|algéb|section|régulière
**Check:** used and rechecked in this run || Read Deligne II5.9 and compared it with the actual a/b/c enumeration; no theorem about arbitrary nonhorizontal sections inferred.

### E13 — A transverse section need not be algebraic in the regular model

**File/location:** cote 93, scan 131, remaining question about the transverse section \(\sigma\). **Kind:** own idea. **Confidence:** high, by a countermodel to the automatic-algebraicity inference.

On the trivial algebraic \(\mathbb P^1\)-bundle over \(\mathbb A^1\) with trivial connection, the analytic section \(x\mapsto e^x\) is everywhere transverse but is not algebraic in that model. This shows why the regular flat-bundle theorem does not automatically algebraize a specified transverse section. It is not the canonical uniformizing section of \(\mathbb A^1\), and no p-curvature calculation from earlier P05 is repeated or used as a premise.

**Context:** Supports the qualification in H-Xb, p. 130/scan 131; the overlap with P05 is the test function only, not a new verification of that earlier note. The horizontal \(\sigma'\) on scan 132 is a distinct issue in E19.
**Context query:** Deligne|exp|section|P05|algébrique
**Check:** targeted proof check || The derivative of e^x never vanishes, but e^x is not a rational function; the underlying trivial connection is already regular and algebraic.

### E14 — Reconstructing the analytic domain requires analytic continuation

**File/location:** cote 93, scan 132, “comment reconstituer…” and the third case. **Kind:** self-flagged.

The question asks how algebraic \((P_X,c_X,\sigma)\) recover the analytic open \(\widetilde X\) and its covering map. In the hyperbolic case the page identifies fiber disks as maximal domains of continuation of the formal germ, a condition involving analytic continuation rather than just finite-order jets. The algebraic torsor constructed next classifies projective connections but does not by itself select the uniformizing one over every base field or family.

**Context:** Restates H-Xb, p. 131/scan 132, and connects it to H-VIIIb's family question on scan 115; S20's topology-independent interpretation remains an additional problem.
**Context query:** reconstituer|maximaux|disques|purement algébrique|famille
**Check:** used and rechecked in this run || Compared the reconstruction question and maximal-domain condition with the later algebraic torsor; no algebraic criterion for the uniformizing choice asserted.

### E15 — The displayed second-jet extension follows directly from the diagonal ideal

**File/location:** cote 93, scan 133, formula for \(E\). **Kind:** unproved claim.

For a smooth relative curve, \(\mathcal J/\mathcal J^2\simeq\omega\) and \(\mathcal J^2/\mathcal J^3\simeq\omega^2\). Tensoring their extension by \(\omega^{-1}\) gives exactly \(0\to\omega\to E\to\mathcal O_X\to0\) with \(E=(\mathcal J/\mathcal J^3)\otimes\omega^{-1}\). This checks the algebraic construction without choosing a square root of \(\omega\), and provides the concrete link requested on scan 095.

**Context:** Checks H-Xb, p. 132/scan 133, and connects to H-VIIa p. 94/scan 095; Deligne [B2, I, §§5.2–5.4] is a published characteristic-zero parallel.
**Context query:** augmentation|J|oscul|extension|jets
**Check:** targeted proof check || Used the two graded pieces of the diagonal ideal and tensor exactness for a line bundle.

### E16 — The third jet determines the allowed prolongation, not every formal series

**File/location:** cote 93, scans 133–134, “en correspondance biunivoque” and the restriction on formal isomorphisms. **Kind:** unproved claim.

For \(z+az^2+bz^3+\cdots\), the matching Möbius map \(z/(1-az)\) has third coefficient \(a^2\), leaving the defect \(b-a^2\). Two prolongations of a fixed second jet therefore differ intrinsically by \(\operatorname{Hom}(\omega,\omega^3)=\omega^2\), while characteristic-zero formal ODE recursion determines the allowed further coefficients. The restriction that the transported connection extend to the whole projective bundle is essential: \(z\) and \(z+z^4\) already show that arbitrary formal isomorphisms are not determined by a third jet.

**Context:** Checks H-Xb, pp. 132–133/scans 133–134, and the restriction already present in H-VIIIb; compare Deligne [B2, I, Proposition 5.8] without importing a positive-characteristic generalization.
**Context query:** ordre.*3|torseur|Hom|jets|Schwarz
**Check:** targeted proof check || Expanded the normalized Möbius map and identified the derivation space; formal recursion is used only in characteristic zero and with the global-connection restriction.

### E17 — The torsor's base needs clarification

**File/location:** cote 93, scan 134, “torseur canonique sur S”. **Kind:** reading question.

The literal phrase says “sur S,” but \(\omega_{X/S}^{\otimes2}\) and its displayed Hom sheaf live on \(X\). The immediate construction is the sheaf of local connections on \(X\); a relative functor on \(S\) requires taking sections after base change, and identifying its translations with a vector bundle on \(S\) requires further cohomology and base-change hypotheses. Likewise the set of global connections is a torsor under \(H^0(X,\omega^2)\) only when it is nonempty.

**Context:** Adds a base-of-torsor question to H-Xb, p. 133/scan 134, and a qualification to the family programme of H-VIIIb p. 114/scan 115.
**Context query:** torseur|base change|changement de base|sur.*S
**Check:** used and rechecked in this run || Checked where the displayed sheaves live and separated the local sheaf from its relative section functor; no representability theorem assumed.

### E18 — The final Lie-bundle formula fits the extension, with characteristic zero retained

**File/location:** cote 93, scan 134, last displays and unfinished final paragraph. **Kind:** unproved claim.

Since \(\det E\simeq\omega\), the characteristic-zero adjoint bundle is \(\operatorname{Sym}^2E\otimes\omega^{-1}\), with successive graded pieces \(\omega,\mathcal O_X,\omega^{-1}\). Tensoring by \(\omega\) gives the displayed target \(\operatorname{Sym}^2E\), consistent with the earlier filtered Lie-algebra construction. The supplied range ends in the middle of this discussion, so the next sheet's conclusions in Hua's modernization are context only and are not silently completed here.

**Context:** Checks H-Xb, p. 133/scan 134, against H-VIIa and H-VIIIb; Hua's continuation on p. 134 corresponds to unsupplied scan 135.
**Context query:** Sym|algèbre de Lie|omega|filtr
**Check:** targeted proof check || Computed determinant and graded symmetric-square pieces; the identification is used with the characteristic-zero assumption of scan 133.

### E19 — The omitted horizontal section is distinct from the marked transverse section

**File/location:** cote 93, scan 132, “description purement algébrique” of \(\sigma'\). **Kind:** self-flagged.

The question here concerns a horizontal section \(\sigma'\) disjoint from the already marked transverse section \(\sigma\), not the unresolved algebraization of \(\sigma\) on scan 131. In the plane-covered models of E09–E10, \(\sigma'\) is the section at infinity in the projective completion of the tangent affine-line bundle, hence is algebraic. Translation parallel transport fixes that section, which checks its horizontality and disjointness in these explicit models without asserting the same construction for arbitrary projective connections.

**Context:** Adds an explicit answer for H-Xb, p. 131/scan 132, using the affine construction of H-Xa, pp. 128–129/scans 129–130; keeps this question separate from Deligne's qualification and S20's general arithmetic programme.
**Context query:** sigma'|horizontale|disjointe|clôture.*projective|purement algébrique
**Check:** targeted proof check || In the affine model dw+eta=0, translation fixes the projective point at infinity; that algebraic section is disjoint from the finite zero section.

### E20 — In the affine-line case the covering map is algebraic

**File/location:** cote 93, scan 132, “Et de \(p_X\)” and “\(p_X\) est lui-même algébrique !”; scan 130, affine-line case. **Kind:** self-flagged.

For \(X=\mathbb A^1\), the map from the tangent affine-line bundle is explicitly \((x,w)\mapsto(x+w,x)\), an algebraic isomorphism onto \(X\times X\) over its second factor that takes the zero section to the diagonal. A change of affine coordinate \(x'=ax+b\), \(w'=aw\) preserves this formula, so it descends to an affine-line torsor without choosing an origin. This answers the specific \(p_X\) question in that case and remains distinct from the transcendental multiplicative covering \(x\exp(w)\) in E10–E11.

**Context:** Adds the explicit coordinate-free compatibility to H-Xa, p. 129/scan 130, and H-Xb, p. 131/scan 132; no claim that all analytic continuation maps in S20 are algebraic.
**Context query:** p_X|identité|simplement.*connexe|affine|purement algébrique
**Check:** targeted proof check || With the manuscript's second-factor base convention, the inverse is (y,x)→(x,y−x); affine coordinate changes give x'+w'=a(x+w)+b, so the construction is algebraic and equivariant.
