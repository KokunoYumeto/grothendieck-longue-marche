## C. The Schwarzian cocycle and the algebraic sheaf

### C01 — The cocycle identities are identities of quadratic differentials

**File/location:** cote 93, scans 116–117, assertions (1), (2), and (4). **Kind:** unproved claim.

“On vérifie facilement” covers postcomposition invariance and the chain law; these give \(G(t,s)+G(s,r)=G(t,r)\) when each term includes its own differential square. In particular, source Möbius invariance is valid for the differential-valued \(G(t,s)\), even though an arbitrary source-coordinate change does not leave the scalar coefficient unchanged. This distinction reconciles the clean cocycle statement here with the failure of scan 114's pure-weight formula.

**Context:** Independently checks H-IX, pp. 115–116/scans 116–117, and carries forward the normalization in earlier P01 and the caution in P03.
**Context query:** cocycle|invariant|quadratique|Schwarz
**Check:** computation or formal certificate || CHAIN_RULE and POSTCOMPOSITION_HOMOGRAPHY in root_symbolic_checks.txt have residual zero; the differential factors were included.

### C02 — Analytic surjectivity is local, and the kernel is Möbius

**File/location:** cote 93, scans 117–118, “aisément une réciproque” and III(a),(b). **Kind:** unproved claim.

The analytic ODE \(G_t(s)=\mu\) has a local solution for prescribed initial data with \(s'\ne0\), so the asserted surjectivity is surjectivity of sheaves, not necessarily on sections over an arbitrary open set. If \(G_t(s)=0\), then \(y=s''/s'\) satisfies \(2y'=y^2\); its solutions integrate to Möbius functions, and uniqueness makes the local Möbius element constant across a connected domain. Global developing functions may nevertheless be multivalued, as the subsequent torsor construction accommodates.

**Context:** Restates H-IX, pp. 116–117/scans 117–118, and adds the precise local/global distinction needed in earlier P03 and P04.
**Context query:** surject|connexe|réciproque|équations.*diff
**Check:** targeted proof check || Reduced the zero equation to 2y prime=y squared and used local analytic ODE existence with nonzero first derivative; no global surjectivity claimed.

### C03 — “Mod. matrices diagonales” is too large a quotient

**File/location:** cote 93, scan 117, displayed description of \(H\). **Kind:** reading question.

The frozen text says “mod. matrices diagonales,” while the Möbius group over \(\mathbb C\) is the quotient of invertible matrices by nonzero scalar matrices. For example, \(\operatorname{diag}(2,1)\) acts by \(t\mapsto2t\), so it cannot be identified with the identity matrix. “Scalaires” or a more restricted meaning of “diagonales” would fit the mathematics, but the written word remains unchanged.

**Context:** Differs from H-IX, p. 116/scan 117, which uses \(\mathrm{PGL}_2\); relates to the scalar ambiguity in H-FIND and D11, rather than supplying a new theorem.
**Context query:** diagon|scalaire|PGL|matrice
**Check:** targeted proof check || The diagonal matrix diag(2,1) is an explicit nonidentity projective transformation over C.

### C04 — A unique global connection does not make the local sheaf final

**File/location:** cote 93, scan 119, first sentence. **Kind:** own idea. **Confidence:** high, by an explicit local counterexample.

The phrase “le faisceau final” for \(H\backslash\mathcal P_{\mathbb P^1}\) is false as a statement about the sheaf: on \(\mathbb G_m\), both \(t\) and \(t^2\) are étale coordinates locally, and \(G_t(t^2)=3/t^2\ne0\). The following conclusion about the unique global projective connection on \(\mathbb P^1\) is correct, because its torsor has a global base point and \(H^0(\mathbb P^1,\mathcal O(-4))=0\). Thus the corrected statement is about global sections, not all local sections.

**Context:** Adds a counterexample to a literal claim omitted in H-IX, p. 118/scan 119, while confirming that reading's unique-global-connection statement.
**Context query:** final|unique.*connexion|P.*1|degré
**Check:** computation or formal certificate || FINAL_SHEAF_COUNTEREXAMPLE in root_symbolic_checks.txt; scan119.final_sheaf refuted, refined statement C04.global.

### C05 — The algebraic identities and analytic solvability are separate

**File/location:** cote 93, scan 119, “Extension à la géom. alg.” and margin about order 3. **Kind:** unpursued implication.

The identities defining \(G\) are rational differential identities with integer coefficients once first derivatives are invertible, so their validity does not require analytic integration. By contrast, the analytic proof that every local quadratic differential has a developing coordinate uses an ODE existence theorem and does not transfer to algebraic étale neighborhoods. The order-3 principal-parts condition in the margin is therefore relevant to defining the invariant, without providing algebraic solvability.

**Context:** Adds a scope separation to H-IX, pp. 118–120/scans 119–121, and to P04's distinction between an equation and its geometric realization.
**Context query:** algéb|ordre.*3|surject|principal
**Check:** used and rechecked in this run || Compared the algebraic identity construction with the explicit loss of surjectivity on scan 121; no analytic existence theorem transported to the algebraic site.

### C06 — The canonical connection on a relative projective line is relative

**File/location:** cote 93, scan 120, final paragraph and “que le lecteur (bis) énoncera”. **Kind:** unproved claim.

For a projective-line bundle \(X_0\to S\), the canonical relative projective connection on a trivialization is invariant under relative projective automorphisms and hence descends. Uniqueness follows locally from the vanishing of the relative pushforward of \(\omega_{X_0/S}^2\simeq\mathcal O(-4)\). This is a projective connection along the fibers of \(X_0/S\), not an absolute flat connection on the bundle in directions on \(S\).

**Context:** Checks the formulation left to the reader in H-IX, p. 119/scan 120; H-Xa's flat bundle on a complex curve is a different use of the word connection.
**Context query:** relatif|fibré.*project|unique.*connexion|base
**Check:** targeted proof check || Invariance permits descent from local projective-line trivializations; H0(P1_A,O(-4))=0 gives local uniqueness over the base.

### C07 — The characteristic-zero relative kernel is explicitly left to check

**File/location:** cote 93, scan 121, first paragraph and margin “à vérifier !”. **Kind:** self-flagged.

The proposed implication \(G(t,s)=0\Rightarrow s=g\circ t\) is accompanied by “lisse/S ??” and “à vérifier !”, so its relative hypotheses are genuinely unsettled on this page. Over a characteristic-zero field with geometrically connected smooth curve, the differential constants are the ground field, and the local Möbius calculation gives the expected result after descent. Over a general base, one still has to state the smoothness, constant-sheaf, and descent assertions that produce \(g\) over \(S\), rather than only locally on \(X\).

**Context:** Restates the qualification in H-IX, p. 120/scan 121; the later H-FIND statement concerns different positive-characteristic constants and does not prove this relative assertion.
**Context query:** vérifier|géom.*connex|constantes|car.*0
**Check:** targeted proof check || Checked the field-case mechanism and identified the extra relative descent obligation; the unrestricted relative statement remains unproved in these notes.

### C08 — Algebraic integrability is stronger than having algebraic coefficients

**File/location:** cote 93, scan 121, loss of surjectivity and “intégrable par fonctions algébriques”. **Kind:** unpursued implication.

The manuscript explicitly distinguishes a projective connection from one lying in the image of algebraic étale developing maps. This supplies a useful test for S20: an equation may have algebraic coefficients while its uniformizing solutions are transcendental, so neither property identifies it as a Picard–Fuchs equation. The phrase “intégrable par fonctions algébriques” thus describes an extra property to establish, rather than a synonym for an algebraic projective connection.

**Context:** Adds the manuscript's own distinction to P04 and P09; H-IX, p. 120/scan 121, agrees that the algebraic map is not generally surjective.
**Context query:** intégrable|fonctions.*algéb|monodrom|Picard
**Check:** used and rechecked in this run || Compared the explicit loss of surjectivity and the definition of algebraic integrability with H-IX and P04/P09; no general classification of algebraic solutions asserted.

### C09 — The torsor construction is formal once the cocycle is fixed

**File/location:** cote 93, scans 118 and 120, “formelle à partir de (II)”. **Kind:** unproved claim.

Choose local coordinates \(t_i\), take local copies of \(\omega^2\), and glue by translation by \(G(t_i,t_j)\); the cocycle identity is exactly the compatibility on triple overlaps. The coordinate \(t_i\) supplies the local zero, and the sign convention is fixed by \(G(t,s)=c_s-c_t\). The resulting torsor is canonical up to unique isomorphism with this structure, even though it need not have a canonical global section on a general curve.

**Context:** Independently checks the formal construction of H-IX, pp. 117–119/scans 118–120, and explains the distinction needed by C04 and B15.
**Context query:** torseur|cocycle|unique.*isom|translation
**Check:** independent re-proof || Glued local affine torsors using the verified cocycle and checked independence of the chosen coordinate cover.
