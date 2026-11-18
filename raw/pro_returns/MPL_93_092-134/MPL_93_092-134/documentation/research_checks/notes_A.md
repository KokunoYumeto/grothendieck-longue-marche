### A01 — Transversality includes a rank-one hypothesis

**File/location:** cote 93, scan 092, opening definition and fixed isomorphism. **Kind:** unpursued implication.

“Nulle part stationnaire” first means that the derivative gives a local direct summand, whereas “transverses” is then used after \(\omega\) is assumed invertible, so that \(c_{2,3}:\Omega\to\omega\) is an isomorphism. Any extension to higher relative dimension must retain this distinction: a nowhere-zero derivative need not trivialize the full cotangent bundle. The fixed isomorphism \(i\) also explains why the subsequent family of connections is a torsor with a prescribed symbol, rather than all connections on the bundle.

**Context:** Adds a hypothesis check to H-VIIa, pp. 91–94/scans 092–095; S20 and P01 supply no higher-dimensional generalization.
**Context query:** transversal|stationnaire|cotangent|Gauss
**Check:** used and rechecked in this run || Compared the two definitions and their rank assumptions in frozen scan 092 and H-VIIa; no general higher-dimensional theorem asserted.

### A02 — The principal-symbol calculation and the role of 2

**File/location:** cote 93, scans 093–094, \(\gamma_0=?\) and the extension diagrams. **Kind:** self-flagged.

The question “\(\gamma_0=?\)” is answered by \(c(fw)-fc(w)=w\otimes df\), which makes the left end map the identity, while the right end map is \(-2i\). Consequently the middle map is an isomorphism when 2 is invertible, and this hypothesis is inserted explicitly before the proposition. The calculation resolves this particular question internally, but does not justify using the same extension identification in characteristic 2.

**Context:** Restates H-VIIa, pp. 92–93/scans 093–094, with the exact inserted hypothesis; bears on H-FIND only as a distinction from the later integral invariant.
**Context query:** gamma|symbole|2.*invers|caractéristique
**Check:** targeted proof check || The displayed Leibniz rule gives the principal symbol; a morphism of short exact sequences with invertible end maps has invertible middle map.

### A03 — A tensor-power ambiguity left frozen

**File/location:** cote 93, scan 095, last main paragraph before the large margin. **Kind:** reading question.

The frozen reading has the doubtful expression \(\Omega^2\otimes\omega\simeq\omega^{\otimes 2|3}\), although the subsequent torsor of projective connections is modeled on \(\omega^2\). H-VIIa also writes \(\Omega^2\otimes\omega\simeq\omega^2\), so the modernized reading does not resolve whether the exponent, the notation for a graded component, or the identification is intended here. A future image check should address the actual superscript and the conventions established before scan 092, not silently replace the line by the later answer.

**Context:** Differs from treating H-VIIa, p. 94/scan 095, as a corrected authoritative formula; P01 concerns a different quadratic differential.
**Context query:** Omega.*2|omega.*2|torseur|gradu
**Check:** used and rechecked in this run || Textual comparison identified the same unresolved power in the contextual reading; no post-freeze emendation made.

### A04 — The formal-neighborhood link is revisited, with conditions

**File/location:** cote 93, scan 095, margin and “Faire le lien”; scans 109 and 133–134. **Kind:** self-flagged.

“Faire le lien” asks for a comparison between the connection and formal data; the margin relates the restricted operator to order 2 and its extension to order 3. Scan 109 later adds that the transported connection must globalize to the projective bundle, and scans 133–134 return to jets and compatible projective isomorphisms. These later passages advance the programme without saying that an arbitrary formal coordinate change is induced by a projective transformation.

**Context:** Adds the sequence of qualifications to H-VIIa p. 94, H-VIIIb p. 108, and H-Xb pp. 132–133/scans 095, 109, 133–134; see also E15.
**Context query:** voisinage|formel|jets|globalise
**Check:** used and rechecked in this run || Compared the three stages of the formal-data proposal; arbitrary formal isomorphisms are not credited with the stated globalizability.

### A05 — A splitting produces one connection, not a global splitting

**File/location:** cote 93, scan 096, “Pour quelles connexions…” and proposition. **Kind:** unpursued implication.

The proposition assigns a unique admissible projective connection to a given splitting of \(\mathcal L\), equivalently to a section disjoint from \(\sigma\). It therefore answers a conditional question and does not establish that the extension admits a global splitting. The explicit “2 inv.!” is needed in the horizontal-component calculation and must not disappear when the result is compared with characteristic-p material.

**Context:** Restates H-VIIb, p. 95/scan 096, while separating its conditional statement from the later global uniformization construction in H-Xa; no settled results-register entry supplies a splitting.
**Context query:** splitting|scind|horizontale|2.*inv
**Check:** targeted proof check || Checked the implication structure and the factor 2 in the displayed component; existence of a global splitting remains an additional condition.

### A06 — The first Riccati equation is corrected later

**File/location:** cote 93, scans 097 and 103; corrections on 105–107 and 114. **Kind:** withdrawn in the same text.

The tentative formula \(\lambda'+\lambda^2=\varphi\) is introduced with “Sauf erreur” and “sauf erreur de calcul,” and scan 097 adds “facteur 2 !”; scan 103 carries a related doubtful margin. The later boxed equations consistently give \(2\lambda'+\lambda^2=\mu\), arising from \(c_{D+\eta}=c_D+2D\eta+\eta^2\). Thus the corrected normalization has explicit support in the same manuscript, while the earlier uncancelled formulas remain part of the diplomatic text.

**Context:** Adds the actual revision trail to H-VIIb and H-VIIIa, which present the corrected version; resembles the separate same-page correction in earlier P02 without identifying the two calculations.
**Context query:** Riccati|facteur|lambda|coefficient
**Check:** computation or formal certificate || RICCATI_TO_SCHWARZIAN and AFFINE_SHIFT_TRANSITIVITY in root_symbolic_checks.txt verify the later normalization in characteristic zero.

### A07 — The minimal image line requires a nonzero operator

**File/location:** cote 93, scan 098, “le plus petit” invertible submodule. **Kind:** own idea. **Confidence:** high, because the zero operator is a direct counterexample to an unqualified statement.

The image of the principal-parts map is an invertible subsheaf of \(L\) on a smooth integral curve over a field if the operator is nonzero, but \(D=0\) has image 0, which is not a line bundle. On a disconnected curve the nonzero condition is needed on every component on which this construction is claimed. The assertion about a canonical smallest invertible \(L'\) should therefore be read with that qualification, or restricted to the nondegenerate situation already under discussion.

**Context:** Refines H-VIIb, pp. 97–98/scans 098–099, which moves directly to epimorphic quotients; S20 and the results register do not settle this omitted edge case.
**Context query:** engendr|sous-module|inversible|opérateur
**Check:** targeted proof check || Over a DVR a nonzero ideal is principal and free of rank one; the zero-image case refutes the unqualified extension.

### A08 — Extension from the nondegenerate locus needs its hypotheses

**File/location:** cote 93, scans 099–100, density and regular extension criterion. **Kind:** unproved claim.

“Laquelle sera unique” uses the assumption that the nondegenerate locus is dense on each fiber and the ability to compare sections of the quadratic-differential torsor there. Over a smooth curve over a field, the difference of two extensions is a section of a line bundle vanishing on a dense open, so uniqueness follows; for general \(X/S\), one should formulate the corresponding schematic-density and flatness hypotheses. Existence is the separate assertion that the Riccati expression has no pole, not a consequence of uniqueness.

**Context:** Adds a relative-scope qualification to H-VIIb, pp. 98–99/scans 099–100; H-Xb's later algebraization problem is not a proof of this relative extension assertion.
**Context query:** dense|régulière|prolonge|famille
**Check:** targeted proof check || Verified uniqueness on smooth integral curves by the torsor difference; no unrestricted relative-base theorem claimed.

### A09 — The local operator is missing a multiplicative factor if read literally

**File/location:** cote 93, scan 100, first displayed formula. **Kind:** reading question.

The frozen line reads \(D(f\,dt)=a\,df/dt+b\), whereas H-VIIb supplies \(a f'+bf\). The literal formula sends 0 to \(b\), so it cannot define the stated linear differential operator unless \(b=0\); this makes a missing \(f\) mathematically plausible but does not establish that it is visible in the ink. The transcription remains unchanged, and the contextual alternative is recorded here for a future reading.

**Context:** Differs from H-VIIb, p. 99/scan 100, precisely at the added factor \(f\); the later \(\lambda=b/a\) explains the intended coefficient but is not visual evidence.
**Context query:** bf|lambda|opérateur.*diff|D.*dt
**Check:** targeted proof check || Evaluating the literal formula at f=0 detects failure of additivity; the proposed reading is not promoted to a visual correction.

### A10 — Residue 2 and the absent constant term

**File/location:** cote 93, scan 100 and scan 107, polar-part criterion. **Kind:** unproved claim.

The condition “\(\frac2t\) (+ pas de terme constant)” is exactly the characteristic-zero cancellation condition for a genuine pole of \(\lambda\) when \(2\lambda'+\lambda^2\) is regular. Writing \(\lambda=r/t+k+\cdots\) gives coefficients \(r(r-2)\) of \(t^{-2}\) and \(2rk\) of \(t^{-1}\), hence \(r=2\) and \(k=0\); a higher pole is impossible over a field because its square has strictly larger pole order than its derivative. The argument uses reduced field coefficients and invertibility of 2, and should not be transported unchanged to arbitrary nonreduced bases.

**Context:** Independently checks H-VIIb and H-VIIIa, pp. 99 and 106/scans 100 and 107, rather than deriving the criterion from the earlier erroneous Riccati normalization.
**Context query:** pôle|polaire|résidu|terme.*constant
**Check:** computation or formal certificate || LAURENT_DOUBLE_POLE and LAURENT_SIMPLE_POLE in root_symbolic_checks.txt, plus the pole-order comparison over a field.

### A11 — Automorphisms must specify the data they preserve

**File/location:** cote 93, scan 101, “Quels sont les autom… ??”. **Kind:** self-flagged.

The question about automorphisms sending \(c\) to \(c+\bar\omega_2\) is not the same as the automorphism group of the full triple \((P,\sigma,c)\). On a smooth complex curve, an automorphism preserving both the flat connection and the transverse section is locally a constant Möbius transformation fixing an open set of developing values, hence is the identity. That argument does not classify automorphisms allowed to move the marked section or alter the connection, which is the distinction the unfinished scan requires.

**Context:** Adds a preservation-of-data distinction to H-VIIb, p. 100/scan 101; [B1, §1.3] gives the corresponding adjoint-oper rigidity, with no implication for the unrelated GT rows in RESULTS_STATE.
**Context query:** automorph|moduli|opér|oper
**Check:** independent re-proof || In a local horizontal trivialization, the automorphism is constant and fixes the image of a local biholomorphism; a Möbius transformation with that property is the identity.

### A12 — The cancelled moduli diagram does not establish a tower claim

**File/location:** cote 93, scan 101, crossed-out diagram at the top. **Kind:** reading question.

The deleted diagram involving \(\mathcal M_g\) is a concrete lead toward varying connections in moduli, but several labels remain doubtful and the whole diagram is struck through. It does not state an action of GT, a Lego decomposition, or one of the finite-groupoid assertions in the supplied results register. Its useful connection is with the explicit family question on scan 115, not an identification with an unrelated current research result.

**Context:** Adds a restrained comparison with S20 and scan 115; searches found moduli vocabulary in RESULTS_STATE, but no statement-level bearing on EXIT_TOWER or LM4_SUCCESSOR is established.
**Context query:** moduli|modulaires|M_g|famille|paramètre
**Check:** used and rechecked in this run || Compared the cancelled diagram and the register's actual statements; no mathematical result is claimed from the overlap of words.

### A13 — A global disjoint horizontal section is obstructed on compact curves

**File/location:** cote 93, scans 096, 101, and 108. **Kind:** own idea. **Confidence:** high in characteristic zero, by the line-bundle degree argument.

A global section of \(P-\sigma\) would split the first-principal-parts sequence and hence give a holomorphic connection on \(\omega\), so on a smooth compact complex curve it is impossible when \(g\ne1\). Indeed, for a meromorphic section \(e\) of a line bundle with holomorphic connection, the meromorphic form \(\nabla e/e\) has residues \(\operatorname{ord}_x(e)\), whose sum is zero, forcing the line bundle's degree to vanish. Thus the canonical projective connection on \(\mathbb P^1\), explicitly noted on scan 108, cannot come from one globally defined connection on \(\Omega^1_{\mathbb P^1}\).

**Context:** Adds a global obstruction to H-VIIb/H-VIIIa, pp. 95–107/scans 096–108; it is compatible with their local section description and does not contradict analytic local existence.
**Context query:** degré|compact|splitting|connexion.*omega
**Check:** independent re-proof || Residue theorem proves degree zero for a holomorphic line-bundle connection; deg omega=2g-2 gives the obstruction.

### A14 — A moving pole over a nonreduced base

**File/location:** cote 93, scans 099–100 and 107, relative pole criterion. **Kind:** own idea. **Confidence:** high for the explicit calculation; medium for the best general relative formulation.

Over \(\mathbb Q[\epsilon]/(\epsilon^2)\), the expression \(\lambda=2/(t+\epsilon)=2/t-2\epsilon/t^2\) satisfies \(2\lambda'+\lambda^2=0\), although its expansion in the fixed parameter \(t\) contains a nilpotent double-pole coefficient. This does not refute the geometric simple-pole statement along the moving Cartier divisor \(t+\epsilon=0\); it shows why a coefficientwise pole-order argument on the fixed parameter divisor is insufficient in families. A relative formulation should refer to the intersection divisor and its jet, as scan 099 already suggests.

**Context:** Adds a nonreduced-base test to H-VIIb/H-VIIIa and to the family question on scan 115; no supplied context states this example.
**Context query:** nilpotent|famille|diviseur|polaire
**Check:** computation or formal certificate || Dual-number expansion and differentiation give zero modulo epsilon squared; recorded in additional_checks.txt.

### A15 — The contact-element construction is explicitly left to find

**File/location:** cote 93, scan 099, final paragraph and unfinished bracket continuing on 100. **Kind:** self-flagged.

The phrases “doit être déterminée !” and “élts de contact can. d'ordre 1 à trouver” distinguish the polar-part calculation from a proposed intrinsic contact-element construction for an arbitrary invertible \(\Omega\). The corrected residue calculation in A10 addresses the first point, while the later second-jet construction in E15 treats the specific cotangent case. A full answer to the broader bracket would need to construct the indicated contact element functorially under changes of local frame, rather than infer it from a chosen-coordinate Riccati formula.

**Context:** Adds an explicit outstanding step to H-VIIb, pp. 98–99/scans 099–100, and distinguishes it from H-Xb, p. 132/scan 133; no matching settled RESULTS_STATE entry supplies the arbitrary-line-bundle construction.
**Context query:** contact|canonique|Omega|ordre.*1|principal
**Check:** used and rechecked in this run || Compared the explicit pending words on frozen099 with the later special second-jet construction and the contextual discussion; the broader functorial claim is not certified.
