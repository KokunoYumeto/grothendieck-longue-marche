# Modular boundary and congruence comparison

Research track: B. Author: GPT-6 Astra Pro; effort inherited, with no runtime effort value exposed. Date: 2026-11-17 (UTC).

This research began only after the parent recorded the transcription freeze at 23:29:03 UTC and opened context at 23:29:08 UTC. No manuscript image was consulted, and no frozen transcription or doubts file was changed.

## Question-level disposition

| Question | Disposition within the supplied fragment | Notes |
|---|---|---|
| Q1: Does this fragment carry out cote 149 scans 099–101's modular place-at-infinity test? | Partial analytic preparation is present; the arithmetic degeneration and residual-action test are not carried out in the passages examined. This is not a claim about the omitted portions of cote 64. | B01–B03 |
| Q2: Does this fragment advance bridge B5 to a new all-level congruence result? | It supplies explicit level-4 pinning work and the integral analytic framework; no new all-level GT₀ preservation theorem, arithmetic-image computation, or determination of the registered open kernels is established here. | B04–B07 |

The following note bodies contain at most four sentences each; the separate locator/status fields are metadata. Earlier context notes and result-register entries retain their supplied status as claims, except that independently checked elementary observations and precisely identified literature statements are explicitly distinguished below.

## B01 — The analytic punctured disk is present; the arithmetic cusp calculation is missing

- Kind: reading question.
- Current locus: scan 145, final displayed equation (8); comparison range 139–152, with a supplementary check of 153–157.
- Brief quote: “\(\mathbb C^*/\text{sous-groupe engendré par }[\kappa\mid k]=\exp(2i\pi\tau)\)”. The bracket records the frozen transcription's unresolved alternative; here and below, \(q\) is our comparison notation, not a resolution of that letter.
- Context / result IDs: `MPL_149_091-136_notes.md`, RN099-03 (cote 149 scan 099, manuscript p. 49, approximately lines 17–21, continued scan 100, lines 1–7); RN101-01 (scan 101, approximately lines 1–6); RN103-05 (scan 103, approximately lines 11–19). Also `LM_140-2_text.tex`, §37, scan 517, manuscript p. 264. Relation: **adds** analytic preparation; **differs** from the arithmetic test supplied by the earlier notes; no contradiction claimed.

The formula on scan 145 identifies the analytic family over \(0<|q|<1\), where \(q=e^{2\pi i\tau}\), and thus supplies a concrete analytic starting point for the modular cusp requested in RN099-03. The continuation through scan 152 does not extend the family across \(q=0\), construct a Tate curve over a local arithmetic base, specify inertia or a decomposition-group splitting, or calculate a residue-field action; scans 153–157 instead discuss normality of quadratic covers. The comparison therefore adds preparation to `LM_140-2_text.tex`, scan 517's elliptic modular family, without completing cote 149's place-at-infinity test: Tate's arithmetic construction and torsion sequence identify the additional mathematical ingredients required (Tate, 1995, manuscript pp. 19, 22–23). RN101-01's warning that bad reduction alone does not prove non-realizability, and RN103-05's specific Tate-cusp weight obstruction, remain carried context claims rather than results proved by these cote 64 pages.

## B02 — The symbol \(\tau_\infty\) is not a computed cusp inertia subgroup

- Kind: reading question.
- Current locus: scans 147–150; especially scan 148, equations (12)–(13).
- Brief quote: “\(\tau_\infty=\begin{pmatrix}-1&0\\0&+1\end{pmatrix}\)” and “échange de \(a\) et de \(d\)”.
- Context / result IDs: `LM_140-3_text.tex`, §39, scans 24–26, especially scan 25, equations (8)–(10); `LM_140-3_notes.md`, second pass for scans 21–30, first-pass notes 10–13 and own note E; `LM2_CONGRUENCE_ROWS.md`, LM2 C.r2. Relation: **differs** in the object denoted; **restates** the need to distinguish actual inertia data from outer-action conventions.

The explicitly defined \(\tau_\infty\) is a determinant-\(-1\) involution whose conjugation sends \(g^{-1}\) to \(\begin{psmallmatrix}d&b\\c&a\end{psmallmatrix}\), converting the natural right change of a Torelli basis into the customary left fractional-linear action. This differs from `LM_140-3_text.tex`, §39, scan 25's \(T_\infty(\overline{\mathbb Q}_0)\), which is an inertia source whose image is asserted to be a procyclic unipotent subgroup. Neither the common infinity subscript nor the convention change supplies a map from that arithmetic inertia source, and it does not repair the unique-multiplier assertion flagged in the carried claim LM2 C.r2.

## B03 — One elementary analytic monodromy check is available

- Kind: own idea.
- Current locus: scan 145, final equation (8), and scan 147, equation (14).
- Brief quote: “\(T_g\cdot(\tau,z)=(g\cdot\tau,z/(c\tau+d))\)”.
- Context / result IDs: `LM_140-3_text.tex`, §39, scan 25, equation (9); `LM_140-3_notes.md`, second pass for scans 21–30, first-pass note 10; `MPL_149_091-136_notes.md`, RN099-03 (scans 099–100). Relation: **adds** an elementary analytic witness; **restates** the unipotent shape of the cited context claim without supplying its arithmetic enhancement.
- Confidence: high for the analytic computation, because both the period transport and its matrix are explicit; no confidence claim about an unproved arithmetic comparison is intended.

For the positive loop \(q(t)=q_0e^{2\pi it}\), choose the lift \(\tau(t)=\tau_0+t\); the period cycles \((1,\tau(t))\) return as \((1,\tau_0+1)\), so on the column-coordinate convention the monodromy is \(T=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\). Its conjugate by \(S=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\) is \(STS^{-1}=\begin{psmallmatrix}1&0\\-1&1\end{psmallmatrix}\), giving the same procyclic unipotent image, after the appropriate change of generator, as the lower-triangular expression in `LM_140-3_text.tex`, scan 25. This adds a calculation from the current formulas to RN099-03's requested test and agrees with the analytic cusp chart described by Hain (2021, §4 opening, pp. 29–30). It proves only this analytic monodromy statement: identifying the completed geometric action with arithmetic inertia and specifying its cyclotomic and residual actions still requires the missing comparison and local arithmetic data.

## B04 — The level-4 calculation is a partial bridge, not an all-level theorem

- Kind: self-flagged.
- Current locus: scans 117–121, particularly scan 117's level specification, scan 118, equations (72)–(76), and scan 121 after equation (88).
- Brief quote: “épinglage de Jacobi relatif d'échelon \(4\)”; “la condition c) s'écrit Dieu sait comment — il faudra … y revenir”.
- Context / result IDs: `LM_140-2_text.tex`, §37, scans 527–528, equations (39)–(42); `LM_140-2_notes.md`, second-pass notes R24 (scan 527), R28–R29 (scan 528); `LM2_CONGRUENCE_ROWS.md`, LM2 C.d1 and C.r1–C.r3; `notes/RESULTS_STATE.md`, LM4_SUCCESSOR B.38 (B.5) and EXIT_TOWER E.24 (cote 143 §9, scans 29–33). Relation: **adds** explicit finite-level pinning work; **differs** in scope from the registered all-level and arithmetic-image claims; changes no registered open status.

Scans 117–118 seek a canonical, base-change-compatible Legendre pinning from points satisfying \(2x_i=\varepsilon_i\) and \(\sum_i x_i=0\), initially after choosing a primitive fourth root of unity, while scan 121 explicitly postpones condition c and the remaining independence calculation. This adds a concrete level-4 construction problem to the Legendre family and level-2 monodromy in `LM_140-2_text.tex`, scans 527–528, rather than completing the entire functorial comparison. The passage provides neither the family of projective kernels \(\Pi(2m)\) nor a proof that every actual GT₀ loop automorphism preserves them, so LM2 C.d1 and C.r1–C.r3 are carried claims, not newly verified consequences of this calculation. No arithmetic image with exact indices or determination of \(\mathcal K_5\), the level-seven kernel, or the level-eleven kernel follows here, leaving EXIT_TOWER E.24 and LM4_SUCCESSOR B.38 in their registered open state.

## B05 — Reduction of a Torelli frame gives the geometric entry to B5

- Kind: unpursued implication.
- Current locus: scans 144–147, especially scan 144, equation (4), and scan 145's lattice quotient.
- Brief quote: “Une structure de Torelli … est la donnée d'un isomorphisme” \(\mathbb Z^2\simeq\mathcal H\).
- Context / result IDs: `LM_140-3_text.tex`, §38, scan 20, and §39, scans 28–30, equations (14)–(20); `LM_140-3_notes.md`, second pass for scans 21–30, first-pass notes 23–27; `LM2_CONGRUENCE_ROWS.md`, LM2 C.d1. Relation: **restates** the integral period framework and **adds** the explicit finite-level reduction needed to connect it to the context; does not prove the GT₀ assertion.
- Editorial confidence: high for this limited reduction, because it is the kernel of a displayed integral matrix action on a free rank-two module; the manuscript does not itself execute the resulting arithmetic comparison.

Reducing the displayed Torelli frame modulo \(N\) gives the ordered basis \((1/N,\tau/N)\) of \(E_\tau[N]\), and a change of frame fixes it exactly when its matrix lies in \(\Gamma(N)=\ker(\mathrm{SL}_2(\mathbb Z)\to\mathrm{SL}_2(\mathbb Z/N\mathbb Z))\). This restates the lattice model in `LM_140-3_text.tex`, §38, scan 20, and supplies the elementary geometric input for that text's §39 reductions modulo \(2m\). To identify the latter projective kernels with this construction one must additionally specify the Legendre-family map and the treatment of the central \(\{\pm I\}\), rather than identifying every level structure merely from its numerical label. The current integral and analytic formulas therefore explain how to enter the congruence tower, but do not prove its preservation by the profinite GT₀ action registered as LM2 C.d1.

## B06 — The arithmetic action and its outer square class remain additional data

- Kind: reading question.
- Current locus: scans 146–150, especially scan 147, equation (14), and scan 150, Corollary 1.
- Brief quote: “\(g\in\mathrm{Sl}(2,\mathbb Z)\)” and “canoniquement isomorphe à \(\mathrm{Sl}(2,\mathbb Z)\)”.
- Context / result IDs: `LM_140-3_text.tex`, §39, scans 22–26, equations (1)–(12); `LM_140-3_notes.md`, second pass for scans 21–30, first-pass notes 4, 9, 12–14 and own notes C, E; `LM2_CONGRUENCE_ROWS.md`, LM2 C.r1–C.r3. Relation: **differs** in the kind of action constructed; **restates** the context's distinction between actual linear and outer arithmetic actions.

The matrices here specify a geometric \(\mathrm{SL}_2(\mathbb Z)\)-action, whereas `LM_140-3_text.tex`, §39, scan 22 explicitly introduces the additional arithmetic extension, its map to \(\mathrm{GL}_2(\widehat{\mathbb Z})\), and the cyclotomic determinant. That text's scans 23–26 and the carried return claims LM2 C.r1–C.r3 distinguish the determinant character of an actual linear action from the square-class information retained by the corresponding outer congruence action. Nothing in the current change-of-basis formulas constructs the arithmetic extension, selects a compatible cusp splitting, or restores a unique multiplier after passing to outer automorphisms, so those claims should not be promoted on the basis of this fragment.

## B07 — Two different congruence completions must remain distinct

- Kind: reading question.
- Current locus: scan 150, Corollary 3, compared with scan 140's earlier version.
- Brief quote: “\(\mathcal T\)” is the group of “autom. ext. à lacets de \(\Pi\) compatibles avec l'orientation”, with \(H=\Pi_{\mathrm{ab}}\).
- Context / result IDs: `LM_140-3_text.tex`, §39, scan 24, equation (7); `LM_140-2_notes.md`, second-pass own note D on scan 320; `notes/RESULTS_STATE.md`, EXIT_TOWER D.19 (prompt Part D(c), LM6 C.17 cutting factors); `LM2_CONGRUENCE_ROWS.md`, LM2 C.d1. Relation: **differs** between homological/classical and nonabelian/procongruence meanings; **adds** the literature verification requested by the scan-320 note; no contradiction of EXIT_TOWER D.19 is inferred.

The discrete isomorphism on scan 150 must not be read as the assertion that \(\widehat{\mathrm{SL}_2(\mathbb Z)}\to\mathrm{SL}_2(\widehat{\mathbb Z})\) is injective: this map uses only homological congruence quotients and has a nontrivial classical congruence kernel. By contrast, the procongruence mapping-class construction retains the action on the full nonabelian \(\widehat F_2\); Bux et al. (2011, §1, Main Theorem) prove that \(\widehat{\operatorname{Out}(F_2)}\to\operatorname{Out}(\widehat F_2)\) is injective and explicitly distinguish this theorem from failure of the usual linear congruence subgroup property. Restricting to the orientation-preserving finite-index subgroup gives the punctured-torus comparison relevant here and supplies the precise low-genus literature check left open in `LM_140-2_notes.md`, scan 320, own note D. The genus-at-most-two claim registered as EXIT_TOWER D.19 concerns this nonabelian procongruence usage, whereas bridge B5 uses classical modular congruence quotients, so neither statement settles the other by terminology alone.

## References and exact verification locators

Bux, K.-U., Ershov, M. V., & Rapinchuk, A. S. (2011). The congruence subgroup property for Aut \(F_2\): A group-theoretic proof of Asada's theorem. *Groups, Geometry, and Dynamics, 5*(2), 327–353. https://doi.org/10.4171/GGD/130

- Primary author PDF: https://m-ershov.github.io/Research/asada_final.pdf
- Checked locators: author-PDF pp. 1–3, §1, definition of congruence subgroups from finite quotients of a group, reformulation using completions, Main Theorem and Corollary on p. 2, and explicit contrast with usual \(\mathrm{GL}_2(\mathbb Z)\) congruence on p. 3. The author PDF has 24 pages and different pagination from the 27-page published article; the locators here use the author PDF.
- Publisher metadata checked: https://ems.press/journals/ggd/articles/4445 (authors, journal, volume, issue, pages, DOI, publication date March 6, 2011).

Hain, R. (2021, November 13). *Lectures on moduli spaces of elliptic curves* [Revised author lecture notes]. Duke University. https://sites.math.duke.edu/~hain/teaching/mth790/hain_final_rev_2021.pdf

- Checked locators: title page date; §4 opening, pp. 29–30, the \(q=e^{2\pi i\tau}\) punctured-disk chart and gluing a cusp with \(C_2\) stabilizer. This is the dated author document consulted, not a claim that the elementary monodromy calculation is a new result of these notes.

Tate, J. (1995). A review of non-Archimedean elliptic functions. In J. Coates & S.-T. Yau (Eds.), *Elliptic curves, modular forms, & Fermat's last theorem* (Series in Number Theory, Vol. 1, pp. 162–184). International Press. https://people.math.harvard.edu/~ctm/home/text/others/tate/tate-unif/tate-unif.pdf

- Checked locators in the author manuscript: p. 19, “Points of finite order”, \(0\to\mu_m\to E_t[m]\to\mathbb Z/m\mathbb Z\to0\) and its parameter class; pp. 22–23, “The modular point of view”, the model over \(\mathbb Z[[q]][1/q]\), generalized-elliptic extension, and use at modular cusps. Only the field case of the torsion discussion is needed here.
- The residual-weight obstruction in context RN103-05 is not independently proved or reliterature-audited in this return; its previous citation to Deligne (1980) remains part of that carried context claim.

## Material still missing for the research questions

For Q1, the missing chain is an identified local arithmetic base and generalized elliptic family at the cusp, the map from local inertia to the chosen global fundamental group, a precisely specified actual or outer residual action, and the comparison proving any proposed non-realizability. For Q2, the missing chain is a completed functorial finite-level pinning comparison, identification with the particular projective congruence kernels, arithmetic/profinite actions with compatible base points, and new evidence for the registered kernel or image questions.

The supplied context includes notes about cote 149, not that cote's manuscript images or a complete independently verified text; references to its wording and line locators therefore cite the supplied notes as such. The conclusions are confined to the supplied cote 64 fragment and the stated comparisons, not to unprovided earlier or later pages.
