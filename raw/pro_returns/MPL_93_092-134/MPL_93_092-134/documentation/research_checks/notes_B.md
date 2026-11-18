## B. Coordinate changes, differential equations, and the torsor dictionary

### B01 — Affine connections are not invariant under every homography

**File/location:** cote 93, scan 102, \(D_{u_M(t)}=D_t\). **Kind:** reading question.

The literal equality \(D_{u_M(t)}=D_t\) is false for inversion: if \(s=1/t\), then \(D_s-D_t=2\,dt/t\). The adjacent boxed equality concerns \(c_{D_s}=c_{D_t}\), which is true because the Schwarzian of inversion vanishes. The natural contextual repair is therefore a missing \(c\), but it remains a proposed reading rather than a change to the frozen line.

**Context:** Differs from H-VIIIa, p. 101/scan 102, which states projective invariance; refines the distinction already needed by P01 and P03.
**Context query:** homograph|inversion|D_s|D_t
**Check:** computation or formal certificate || INVERSION_AFFINE_CONNECTION_DIFFERENCE and POSTCOMPOSITION_HOMOGRAPHY in root_symbolic_checks.txt; literal affine equality refuted, refined statement B01.projective.

### B02 — Changing the reference connection also carries a factor 2

**File/location:** cote 93, scan 107, paragraph after “ni linéaire, ni ‘schématique’”. **Kind:** reading question.

After the corrected expression \(F_D(\eta)=2D\eta+\eta^2\), replacing \(D\) by \(D+\bar\eta\) changes \(F_D(\eta)\) by \(2\eta\bar\eta\). The frozen next sentence gives the change without a visible factor 2. This appears to be a remaining normalization slip, not a reason to reinterpret the repeated boxed formula.

**Context:** Adds a local discrepancy to H-VIIIa, p. 106/scan 107, whose consolidated formula uses the corrected normalization; links to A06.
**Context query:** référence|2D|omega_1|normalisation
**Check:** targeted proof check || Direct expansion of 2(D+bar_eta)eta+eta squared gives cross term 2 eta bar_eta.

### B03 — The “OK” check validates the final shift law

**File/location:** cote 93, scan 105, successive shifts and “OK”. **Kind:** self-flagged.

The final line of the verification is consistent because \(2D\eta+\eta^2+2(D+\eta)\theta+\theta^2=2D(\eta+\theta)+(\eta+\theta)^2\). Some intermediate annotations retain doubtful or missing 2s, which the final “OK” does not retrospectively erase from the page. The check supports the finished identity, not every intermediate written expression.

**Context:** Independently checks H-VIIIa, p. 104/scan 105, and clarifies the revision tracked in A06; P02 is a separate earlier normalization issue.
**Context query:** vérif|calcul|2D|transformation
**Check:** computation or formal certificate || AFFINE_SHIFT_TRANSITIVITY in root_symbolic_checks.txt has exact residual zero.

### B04 — The logarithmic integration has intermediate inconsistencies

**File/location:** cote 93, scan 102, lines between \(3s''^2=2s's'''\) and \(s''^2=C s'^3\). **Kind:** reading question.

On a chart with \(s's''\ne0\), the differential equation gives \(2s'''/s''=3s''/s'\), hence \(2\log s''=3\log s'+C\) locally after choosing logarithms. The frozen intermediate coefficients include a doubtful \(3/2\) where these two consistent versions require different normalizations. The endpoint and the direct inversion test support the Möbius conclusion, but do not settle the ink in the intervening lines.

**Context:** Adds a reading caution to H-VIIIa, p. 101/scan 102; H-IX later supplies a cleaner argument, and P01 does not determine the written coefficient.
**Context query:** logarith|homograph|3/2|Schwarz
**Check:** targeted proof check || Dividing the equation by s prime times s double-prime gives the stated logarithmic identity only on the indicated nonvanishing chart.

### B05 — The operator dictionary is a projective, or adjoint, oper dictionary

**File/location:** cote 93, scan 109, items (a), (b), and (b′). **Kind:** unpursued implication.

The triple consisting of a projective-line bundle, a connection, and an everywhere transverse section is naturally compared with an adjoint rank-two oper. The distinction matters because the projective object can be canonical while an \(\mathrm{SL}_2\) lift involves a square root and central twisting. [B1, §§1.1–1.4, 3.3] supplies that modern comparison, but the word “oper” and its additional terminology are not inserted into the manuscript.

**Context:** Credits H-VIIa, p. 94/scan 095, for explicitly naming the modern oper comparison, and connects it to the dictionary in H-VIIIb, p. 108/scan 109; the adjoint/simply connected distinction refines S20's rank-two strand.
**Context query:** oper|SL|PGL|racine.*carr
**Check:** used and rechecked in this run || Compared the transverse-section data with the definitions and lifting discussion in Beilinson–Drinfeld, Opers, §§1.1–1.4 and 3.3.

### B06 — A third jet is the first free projective datum

**File/location:** cote 93, scans 095, 109(c), and 133–134, “prolongements” “à l'ordre 3”. **Kind:** unpursued implication.

A Möbius transformation fixing a marked point is determined by its first two Taylor coefficients, whereas the next coefficient of a general local isomorphism supplies a projective-connection parameter. This explains why a canonical order-2 identification can be prolonged to order 3 in a torsor under quadratic differentials. It does not mean that every higher formal coefficient is independent once a projective connection and its horizontal development have been fixed.

**Context:** Restates and connects H-VIIa p. 94, H-VIIIb p. 108, and H-Xb pp. 132–133/scans 095, 109, 133–134; [B1, §3.3] also describes the canonical Borel torsor by second-order neighborhoods.
**Context query:** ordre.*2|ordre.*3|jets|voisinages
**Check:** targeted proof check || Expanding az/(1+cz) shows that its linear and quadratic coefficients determine a and c when the linear coefficient is a unit.

### B07 — The two associated-bundle relations are equivalent presentations

**File/location:** cote 93, scan 110, crossed-out equivalence relation and surviving simultaneous action. **Kind:** reading question.

The cancelled \((gf,y)\sim(f,g^{-1}y)\) and the surviving \((f,y)\sim(gf,g(y))\) are equivalent: replacing \(y\) by \(gy\) in the first gives the second. Thus the cancellation changes the presentation and should not be interpreted as correcting a mathematically different relation. In the simultaneous-action form, \((f,f(x))\) transforms to \((gf,gf(x))\), which verifies that the marked section is well defined.

**Context:** Restates H-VIIIb, p. 109/scan 110, and supplies a check of the diagonal section; adds concrete descent data to earlier P03's equivariance requirement.
**Context query:** torseur.*gauche|droite|équiv|f\\(x\\)
**Check:** targeted proof check || Substitution y→gy proves equivalence of the two written relations; the pair defining the marked section transforms equivariantly.

### B08 — Local horizontal sections and global monodromy are different

**File/location:** cote 93, scans 110–111, construction of \(\mathcal U\) and \(\mathcal T/B\). **Kind:** unpursued implication.

“Sections horizontales locales” are parametrized by points of a fiber after a local horizontal trivialization, but a global horizontal section requires a fixed point of the projective monodromy representation. Thus local ODE existence does not imply a global section of \(P\), still less one disjoint from \(\sigma\). The quotient description in the manuscript is a sheaf description and should be read locally unless a monodromy condition is supplied.

**Context:** Adds the global condition to H-VIIIb, pp. 109–110/scans 110–111, and to P03's developing-map discussion; no supplied results-register theorem supplies that fixed point.
**Context query:** monodrom|horizontale|locales|revêtement
**Check:** independent re-proof || In the universal-cover trivialization, a constant fiber point descends exactly when every monodromy element fixes it.

### B09 — The square-root expression comes from the determinant sequence

**File/location:** cote 93, scan 112, marginal \(L^2\simeq\omega^3\). **Kind:** unproved claim.

For the quotient \(P^1(\omega)\twoheadrightarrow L\) with kernel \(N\), the principal-parts sequence gives \(\det P^1(\omega)\simeq\omega^3\), hence \(N\otimes L^{-1}\simeq\omega^3L^{-2}\). A trivialization therefore gives \(L^2\simeq\omega^3\), exactly the margin's “racine carrée”. This is a trivialization over the chosen section of the projective bundle, and should not be confused with an automatic global square root on every base.

**Context:** Independently checks H-VIIIb, p. 111/scan 112; relates to B05's lifting distinction, but neither proves nor assumes a universal theta characteristic.
**Context query:** racine.*carr|det|L.*2|omega.*3
**Check:** targeted proof check || Took determinants of 0→omega squared→P1(omega)→omega→0 and of the quotient sequence.

### B10 — Horizontal one-forms describe an intermediate quotient

**File/location:** cote 93, scans 112–114, “Condition d'horizontalité ?” and the isolated margin “?”. **Kind:** self-flagged.

For \(D=D_t+\lambda\,dt\) and a nowhere-zero form \(\varphi=\alpha\,dt\), the condition is \(D\varphi=0\), or \(\alpha'+\lambda\alpha=0\). The nowhere-zero condition is essential for the multiplicative torsor \(\mathcal T/B_u\to\mathcal T/B\); allowing the zero solution would add a point outside that torsor. The local solution \(\varphi=ds\) also requires a local primitive and does not assert that every global horizontal one-form is globally exact.

**Context:** Restates H-VIIIb, pp. 111–113/scans 112–114, with the local/global qualification; the precise attachment of scan 113's isolated question mark remains uncertain.
**Context query:** horizontal|varphi|alpha|primitive
**Check:** targeted proof check || Expanded the connection on alpha dt and checked that nonvanishing is needed for a frame; global exactness was not assumed.

### B11 — The sign in the exponential changes within one calculation

**File/location:** cote 93, scan 113, first three formulas. **Kind:** reading question.

The page writes \(\log s'=-\Lambda+C\), then \(s'=C\exp\Lambda\), then an integral of \(\exp(-\Lambda)\). The first and third expressions agree and require the middle exponent to have a minus sign; scan 114 independently uses the negative exponent for \(\alpha\). H-VIIIb adopts that corrected integration, but the uncancelled plus sign stays in the diplomatic transcription.

**Context:** Differs at one sign from H-VIIIb, p. 112/scan 113, and is internally clarified by p. 113/scan 114; no earlier P-note settles the reading.
**Context query:** exp|Lambda|primitive|alpha
**Check:** targeted proof check || Differentiation of log s prime gives s double-prime/s prime=-lambda, selecting the negative exponent mathematically.

### B12 — The three differential equations form a consistent local system

**File/location:** cote 93, scan 114, equations (1)–(4). **Kind:** unproved claim.

The relations \(2\lambda'+\lambda^2=\mu\), \(\alpha'+\lambda\alpha=0\), and \(s'=\alpha\) give \(\lambda=-s''/s'\) and hence \(G_t(s)=\mu\). This checks the actual passage from a horizontal point to a horizontal frame and then to a developing coordinate, with \(s'\ne0\). It also pinpoints which signs and factors in the earlier exploratory calculations are required by the final dictionary.

**Context:** Independently checks H-VIIIb, p. 113/scan 114; adds an explicit derivation to P01 and agrees with P04's rank-two interpretation.
**Context query:** lambda|alpha|Schwarz|Riccati
**Check:** computation or formal certificate || RICCATI_TO_SCHWARZIAN in root_symbolic_checks.txt verifies exact residual zero.

### B13 — Linearization gives a specific second-order equation

**File/location:** cote 93, scan 114, Riccati equation. **Kind:** own idea. **Confidence:** high locally in characteristic zero, by direct substitution.

Putting \(\lambda=2u'/u\) on a chart with \(u\ne0\) turns \(2\lambda'+\lambda^2=\mu\) into \(u''=(\mu/4)u\). A ratio of two independent solutions has the manuscript's Schwarzian \(\mu\), with the order of the ratio immaterial up to a Möbius transformation. This identifies a differential equation but supplies no geometric family whose periods realize it.

**Context:** Adds the manuscript's corrected normalization to earlier P04 and carries its warning about the missing Picard–Fuchs realization; H-VIIIb gives the Riccati side.
**Context query:** Picard|Sturm|second.*ordre|mu/4
**Check:** computation or formal certificate || RICCATI_LINEARIZATION in root_symbolic_checks.txt verifies 2lambda prime+lambda squared=4u double-prime/u; P04's period-realization caveat is retained.

### B14 — The coordinate-change formula needs an inhomogeneous term

**File/location:** cote 93, scan 114, last NB before “Pb”. **Kind:** own idea. **Confidence:** high, by the chain rule and an explicit counterexample.

The displayed pure-weight formula for \(G_{\widetilde t}(s)\) fails for a general change of source coordinate: the correct relation is \(G_{\widetilde t}(s)\,d\widetilde t^2=(G_t(s)-G_t(\widetilde t))\,dt^2\). For \(s=t\) and \(\widetilde t=t^2\) on a local chart with \(t\ne0\), the left coefficient is \(-3/(4t^4)\), whereas the manuscript's right side predicts zero. Differences of two projective connections transform as quadratic differentials; an individual coefficient relative to the coordinate connection does not.

**Context:** Agrees with the correction explicitly credited to H-VIIIb, p. 113/scan 114, and independently checks the same issue already anticipated by earlier P03.
**Context query:** changement|cocycle|quadratique|transformation
**Check:** computation or formal certificate || CHAIN_RULE and BAD_WEIGHT_COUNTEREXAMPLE_t_to_t2_s_t in root_symbolic_checks.txt; literal formula refuted, refined statement B14.chain.

### B15 — Compactness gives algebraicity of the entire marked object

**File/location:** cote 93, scans 110 and 114–115, inserted compactness and “Pb”. **Kind:** unproved claim.

For a fixed smooth complete complex algebraic curve, analytic uniformization determines a projective connection, and GAGA algebraizes the bundle, the marked section, and the connection. This establishes the existence of the requested regular coefficient \(\mu\) on an algebraic coordinate chart; uniqueness here means the coefficient attached to the uniformizing projective structure, not uniqueness among all projective connections. The analogous assertion on an open curve cannot be obtained by applying proper GAGA to that open curve.

**Context:** Restates H-VIIIb, pp. 109 and 113–114/scans 110 and 114–115, with the meaning of uniqueness made explicit; strengthens S20's uniformization strand without settling its arithmetic strand.
**Context query:** GAGA|Gaga|compact|complète|algébrique
**Check:** carried as background without fault found || Classical uniformization and proper GAGA are used with their proper complex-curve hypotheses; no new proof of either theorem is claimed.

### B16 — Fiberwise algebraicity alone does not settle the family question

**File/location:** cote 93, scan 115, “Sont-elles algébriques ?”. **Kind:** own idea. **Confidence:** high for the counterexample to the inference; it is not a counterexample about the canonical uniformizing choice.

Fix a smooth projective complex curve \(C\) of genus at least 2, an algebraic projective connection \(c_0\), and \(0\ne q\in H^0(C,\omega_C^2)\); on \(C\times\mathbb A^1\), the analytic relative connections \(c_0+e^s q\) are algebraic on each fiber but not jointly algebraic. If they were jointly algebraic, taking a linear functional on the finite-dimensional space of quadratic differentials that is nonzero on \(q\) would make \(e^s\) a regular function on \(\mathbb A^1\), which it is not. This isolates the logical gap in passing from fiberwise GAGA to a family, while the separate regularity of the canonical uniformizing section is addressed in F06.

**Context:** Adds a counterexample to the inference underlying S20 and H-VIIIb, p. 114/scan 115; earlier P09 already asks for an actual comparison across a family.
**Context query:** famille|fibres|paramètre|algébriques|uniformisation
**Check:** independent re-proof || The explicit analytic family is fiberwise algebraic; evaluation in H0(C,omega squared) reduces joint algebraicity to polynomiality of e to the s.

### B17 — The fixed finite-type complex curve has an algebraic uniformizing connection

**File/location:** cote 93, scan 115, “Est-elle algébrique ?”; scan 131, the section qualification. **Kind:** own idea. **Confidence:** high, using classical cusp uniformization and proper GAGA with their stated scope.

For a fixed smooth finite-type curve over \(\mathbb C\), the answer is yes over \(\mathbb C\): in the hyperbolic case, a cusp parameter gives the uniformizing coefficient \(-1/t^2+O(1/t)\) in the manuscript's normalization [B12, §§2.1–2.2]. Relative to a holomorphic projective connection on the compactification \(\bar X\), the difference extends to a section of \(\omega_{\bar X}^2(2D)\), where \(D=\bar X-X\), and is algebraic by GAGA [B3]. The sphere, affine-line, multiplicative, and compact elliptic cases are covered by the earlier constructions; this also gives a regular-singular algebraic flat projective object with its algebraic marked section. The conclusion neither gives an algebraic formula for accessory parameters nor establishes descent to a smaller field or algebraic variation in families.

**Context:** Answers the fixed-curve question in H-VIIIb, p. 114/scan 115, and supplies an argument beyond H-Xb's Deligne qualification; Hua's discussion of accessory parameters concerns a stronger expression/variation issue that must not be conflated with algebraicity over \(\mathbb C\).
**Context query:** non.*propre|complète|accessoires|algébrique|Deligne
**Check:** targeted proof check || Cusp asymptotic checked in Takhtajan; compactification and GAGA argument, including a logarithmic-system verification of regular singularity, written in fixed_curve_algebraicity.md.

### B18 — The three-puncture connection is not the restricted zero connection

**File/location:** cote 93, scan 115, first classical example; comparison with Hua's later continuation. **Kind:** own idea. **Confidence:** high, by the cusp conditions and a rational calculation.

On \(X=\mathbb P^1-\{0,1,\infty\}\), the uniformizing coefficient is
\(\mu(z)=-(z^2-z+1)/(z^2(z-1)^2)\), with leading coefficient \(-1\) at each puncture. It is unique with those fixed cuspidal leading coefficients, because the difference of two choices lies in \(H^0(\mathbb P^1,\omega^2(0+1+\infty))=0\). Consequently it is not the projective connection obtained by simply restricting the standard one on \(\mathbb P^1\), whose coefficient is zero; that distinction also follows from their different projective monodromy.

**Context:** Corrects the literal later claim in H-Xb, pp. 136–137/scans 137–138, which are context only and not supplied images; adds an explicit answer to the example actually asked on scan 115.
**Context query:** trois points|trois trous|régulière|accessoires|droite projective
**Check:** computation or formal certificate || additional_checks.txt verifies all three leading pole coefficients; uniqueness uses degree -1 for omega²(D), and the source claim is refined to fixed cuspidal leading coefficients.

### B19 — A cancelled question remains too uncertain to assign a mathematical claim

**File/location:** cote 93, scan 110, deleted line immediately after item (e). **Kind:** reading question.

The cancelled line begins with a low-confidence “Quid” and ends with words read as “connexion projective sur X/S”. Its intervening wording is too uncertain to identify a definite conjecture or to treat it as a retraction of the surrounding equivalence. H-VIIIb supplies a coherent dictionary but does not settle those strokes, so the deleted line remains a reading question separate from the checked relations in B07.

**Context:** Records an unresolved reading beside H-VIIIb, p. 109/scan 110; no point from P01–P04 is used to fill the cancelled words.
**Context query:** Quid|dictionnaire|connexion.*projective|torseur
**Check:** used and rechecked in this run || Compared the frozen deleted wording with the contextual dictionary; uncertainty retained and no mathematical claim inferred from the cancellation.
