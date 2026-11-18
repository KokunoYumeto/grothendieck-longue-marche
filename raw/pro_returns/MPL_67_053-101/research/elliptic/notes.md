## Real elliptic curves, involution modules, and torsors (scans 91–101)

Hua citations below are to **Michel Hua’s project, modernised reading of cote 67**, supplied in `hua_project/67.modern.tex`; his page number is one less than this package’s scan number. Its section XII and the findings-register entry are prior-project claims, with the precise checks performed here identified in `proofs.md` and `checks.tsv`. The reported Lean verification was not rerun.

For the real-elliptic items without a separate precise RESULTS_STATE id, the relevant register entry is its supplied Hua modernised-reading block; the module specialization bears specifically on **Hua, findings register, 67-involution-modules-triples**. The profinite open entries are cited only where a comparison actually bears on them.

### E01 — 67/91, proposition and construction; 92, working sheet

**Kind:** unproved claim.

“Le foncteur précédent … est une équivalence de catégories” is mathematically supported by the explicit inverse-image construction: take the preimage of \(m\) in \(P\oplus Q\), with action \((p,q)\mapsto(p,-q)\), and use multiplication by two to identify the recovered eigenspaces. The targeted check in P1 verifies the equivalence for arbitrary rings and 2-regular modules, including the graph description, and credits **Hua, findings register, 67-involution-modules-triples** for the supplied finding. It does not verify Hua’s reported Lean code, which is absent from this context.

**Context:** `hua_project/67.modern.tex: XII, “Modules munis d’une involution (pages 90, 91 et 99)” (source scans 91–92,100); notes/RESULTS_STATE.md, “Findings of another project”`. **Relation:** restates the supplied finding and adds an explicit in-run proof check.
**Results state:** Hua, findings register, 67-involution-modules-triples.

### E02 — 67/91, last proposition

**Kind:** own idea.

For “équivalence de catégories,” take a morphism of triples to be a pair \((f,g)\) whose reductions carry \(m\) into the target gluing submodule. This is the same missing convention explicitly supplied by Hua’s project, and P1 checks its naturality rather than treating object classification alone as categorical equivalence. Confidence is high because the inverse-image construction restricts \(f\oplus g\) functorially and the two multiplication-by-two identifications commute with every such map.

**Context:** `hua_project/67.modern.tex: XII, “Modules munis d’une involution (pages 90, 91 et 99)” (source scans 91–92,100), first proposition’s Lean footnote`. **Relation:** restates Hua’s supplied morphism convention and verifies its role.
**Results state:** Hua, findings register, 67-involution-modules-triples.

### E03 — 67/91, heavily revised bottom corollary

**Kind:** own idea.

The uncertain retained assertion “\(P,Q\) inv. de rg \(1\)” does not follow from only commutativity, 2-regularity, rank-two projectivity and the global condition \(\sigma\ne\pm1\). With \(k=\mathbf Q\times\mathbf Q\), \(M=k^2\), and \(\sigma=(\operatorname{diag}(1,-1),1)\), the eigenspace ranks are \((1,2)\) and \((1,0)\), so they are not invertible; P2 gives the check. Confidence is high for this conditional literal reading, but the cancelled/obscured earlier hypotheses prevent treating it as a refutation of a definite fully legible final theorem.

**Context:** `hua_project/67.modern.tex: XII, “Modules munis d’une involution (pages 90, 91 et 99)” (source scans 91–92,100), corollary on their page 99; notes/RESULTS_STATE.md, Hua finding`. **Relation:** differs from the broader uncertain scan91 wording; Hua’s principal-ring specialization avoids this particular counterexample.
**Results state:** Hua, findings register, 67-involution-modules-triples (scope of its corollaries).

### E04 — 67/100, first two corollaries and cancelled unit-map proviso

**Kind:** own idea.

The cancelled phrase “\(k^\times\to k_0^\times\) … surjectif” is mathematically substantive: over a PID with \(k_0=k/2k\) a field, nonsplit rank-two conjugacy classes are parametrized by \(k_0^\times/\operatorname{im}(k^\times)\), in addition to the split class. Changing generators of the two eigenspaces changes the nonzero graph slope by the ratio of their reduced units, proving this refinement in P3. Confidence is high; Hua’s modernised reading retains surjectivity and therefore states a conditional two-class conclusion, whereas the frozen scan records its deletion.

**Context:** `hua_project/67.modern.tex: XII, “Modules munis d’une involution (pages 90, 91 et 99)” (source scans 91–92,100), corollary on their page 99`. **Relation:** supports Hua’s qualified conclusion and identifies what the cancelled proviso controls.
**Results state:** Hua, findings register, 67-involution-modules-triples (rank-two specialization).

### E05 — 67/100, possible unconditional two-class reading

**Kind:** own idea.

A concrete test of “puis une” is \(k=\mathbf Z[(1+\sqrt{-11})/2]\): it is a norm-Euclidean PID, has residue field \(\mathbf F_4\) at 2, and its only units \(\pm1\) both reduce to 1. Thus E04 gives three nonsplit classes and one split class, so the two-class count requires the qualification. Confidence is high because P3 proves the Euclidean bound \(15/16<1\), identifies the unit and residue groups, and supplies exact involution matrices; the arithmetic script checks those matrices without claiming that a finite search proves conjugacy classification.

**Context:** `hua_project/67.modern.tex: XII, “Modules munis d’une involution (pages 90, 91 et 99)” (source scans 91–92,100), conditional rank-two corollary`. **Relation:** adds an explicit counterexample to dropping Hua’s unit-surjectivity hypothesis.
**Results state:** Hua, findings register, 67-involution-modules-triples (limits of corollaries).

### E06 — 67/91, opening ring hypothesis

**Kind:** reading question.

The frozen opening reads “pas néc comm.”, while Hua quotes “par exemple commut.” with doubt. Both permit the noncommutative generality used in E01, but the lexical difference must remain a reading question rather than a context-driven change to the transcription.

**Context:** `hua_project/67.modern.tex: XII, “Modules munis d’une involution (pages 90, 91 et 99)” (source scans 91–92,100), opening footnote`. **Relation:** differs in the reported wording, with no change to the valid mathematical scope.
**Results state:** Hua, findings register, 67-involution-modules-triples.

### E07 — 67/93, first paragraph and “isogènes”

**Kind:** unpursued implication.

The parenthetical “elles sont d’ailleurs isogènes” has an explicit degree-two model for matched \(a\): include \(\mathbf Z e_+\oplus\mathbf Z e_-\) in \(\mathbf Z e_++\mathbf Z(e_++e_-)/2\). The index-two inclusion is compatible with the same conformal structure and reflection, so it induces a real isogeny from the split to the nonsplit torus. This supplies a concrete instance of the manuscript’s aside and of Hua’s corresponding assertion, without identifying the two real isomorphism types.

**Context:** `hua_project/67.modern.tex: XII, “Deux familles (page 92)” (source scan 93); XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), displayed periods`. **Relation:** restates the isogeny claim and adds its explicit lattice map.
**Results state:** Hua, findings register, 67-involution-modules-triples (integral lattice specialization).

### E08 — 67/93–95, category and automorphism conventions

**Kind:** unproved claim.

“avec morphismes pas néc des iso” and the subsequent lattice automorphism calculation require origin-preserving morphisms of elliptic curves. Arbitrary maps of the underlying genus-one curves also include translations, so their automorphism group is larger than the stated finite group. The distinction is confirmed by scan101’s separate extension to torsors and matches the explicit “avec une origine fixée” in the Longue Marche context.

**Context:** `hua_project/67.modern.tex: XII, “Deux familles (page 92)” (source scan 93) and XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101); LM_140-2_text.tex, scan 517, paragraph defining M_{1,1} (locate by quoted phrase in search ledger)`. **Relation:** adds an explicit scope condition already indicated in the neighbouring context.

### E09 — 67/93, last paragraph

**Kind:** unproved claim.

The conclusion “l’autom. universel … \(-\operatorname{id}\)” holds for origin-preserving real automorphisms. An orientation-preserving lattice isometry commuting with a reflection preserves its invariant axis, sends its primitive generator to its positive or negative, and is consequently \(\pm1\). This checks the local argument already explained by Hua, even for square and hexagonal complex lattices with extra complex automorphisms.

**Context:** `hua_project/67.modern.tex: XII, “Deux familles (page 92)” (source scan 93), final paragraph and footnote`. **Relation:** restates and rechecks Hua’s explanation.

### E10 — 67/94, paragraph after the exact sequence

**Kind:** reading question.

The text explicitly says “celles dont l’invariant modulaire est réel.” Hua’s modernised footnote says that the page does not state the criterion in that form, which conflicts with the frozen reading here. The mathematical real-invariant criterion is present as a manuscript claim, rather than solely a modern interpolation.

**Context:** `hua_project/67.modern.tex: XII, “Les structures réelles d’une courbe complexe donnée (pages 93 à 97)” (source scans 94–98), first footnote`. **Relation:** contradicts the footnote’s statement about what the source says.

### E11 — 67/94–95, dihedral group and two orbits

**Kind:** unproved claim.

For “il y a deux orbites,” write the reflections of \(D_n\) as \(r^j\sigma\); rotation conjugacy changes \(j\) by an even number. Since \(n=2,4,6\), this gives exactly two classes, while the translation action of the rotation group on all reflections is free. P4 verifies the distinction between these two actions that the manuscript emphasizes and Hua restates.

**Context:** `hua_project/67.modern.tex: XII, “Les structures réelles d’une courbe complexe donnée (pages 93 à 97)” (source scans 94–98), opening classification`. **Relation:** restates and checks the two-orbit calculation.

### E12 — 67/95, final presumption → 97–98, case analysis

**Kind:** withdrawn in the same text.

“Je présume” proposes one \(E_a\) orbit and one \(E'_a\) orbit with a common parameter, but scans97–98 replace this by reciprocal parameters within a single lattice type outside the square case. The replacement follows because \(\sigma\mapsto-\sigma\) exchanges the eigenlines without changing whether they generate the lattice. Hua already records this retraction; the present package confirms its two-stage textual history rather than presenting the corrected statement as the original claim.

**Context:** `hua_project/67.modern.tex: XII, “Les structures réelles d’une courbe complexe donnée (pages 93 à 97)” (source scans 94–98), paragraph beginning “La page 94 présume” and concluding summary`. **Relation:** restates Hua’s identification of an internal retraction.

### E13 — 67/97–98, square exception

**Kind:** own idea.

“le cas carré est le seul où \(-\sigma\) … soit … conjugué à \(\sigma\)” also tests Hua’s footnote that the two real forms are always quadratic twists by \(-1\). In the square case a quarter turn conjugates \(\sigma\) to \(-\sigma\), so that twist is the same real form, and the second class is represented by a diagonal-versus-side reflection instead. Confidence is high because the calculation \(r\sigma r^{-1}=-\sigma\) is explicit in P4 and the matrix script; the two-form count itself is unaffected.

**Context:** `hua_project/67.modern.tex: XII, “Les structures réelles d’une courbe complexe donnée (pages 93 à 97)” (source scans 94–98), proposition footnote “tordue quadratique par -1”`. **Relation:** contradicts that universal twist identification while preserving the two-form proposition.

### E14 — 67/98, square-lattice paragraph

**Kind:** unpursued implication.

The square gives both \(E_1\) and \(E'_1\) because the axis eigenvectors generate the lattice, whereas the diagonal eigenvectors \(e_0+e_1,e_0-e_1\) span an index-two sublattice. Thus the two real forms have different real-locus topology despite one underlying square complex torus. This makes concrete the point where scan95’s anticipated split/nonsplit dichotomy does hold, as Hua’s case distinction explains.

**Context:** `hua_project/67.modern.tex: XII, “Les structures réelles d’une courbe complexe donnée (pages 93 à 97)” (source scans 94–98), square case; XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), real points`. **Relation:** restates the exceptional case and links it to the later topology.

### E15 — 67/98, hexagonal quadratic ratio; compare 99

**Kind:** own idea.

The literal \(Q(2v-u)/Q(u)=\sqrt3\) conflicts with \(Q\) being quadratic: for unit vectors meeting at 60 degrees the ratio is \(4-4(1/2)+1=3\). **Hua’s modernised reading of cote 67** already flags exactly this correction and checks it against the period formula; P5 independently recalculates the displayed expression while leaving the frozen radical intact. Confidence is high because the discrepancy is between squared length and length, and the exact-arithmetic check returns 3.

**Context:** `hua_project/67.modern.tex: XII, “Les structures réelles d’une courbe complexe donnée (pages 93 à 97)” (source scans 94–98), hexagonal case and its footnote; XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), periods`. **Relation:** restates and rechecks Hua’s correction, not a new discovery.

### E16 — 67/97, opening modular-invariant question

**Kind:** own idea.

The speculative “serait-ce \(j=\cdots\log a\) ?” is incompatible with the reciprocal relation already established on the same page if \(j\) means the modular invariant of the underlying complex curve. The two conjugations \(\sigma\) and \(-\sigma\) leave that complex curve fixed, so \(j(a)=j(1/a)\), whereas any nonzero constant multiple of \(\log a\) changes sign. Confidence is high for rejecting the suggested formula under that interpretation; Hua points instead to \(j(\tau)\), and the exact handwritten coefficient remains a separate doubt (E23).

**Context:** `hua_project/67.modern.tex: XII, “Les structures réelles d’une courbe complexe donnée (pages 93 à 97)” (source scans 94–98), final paragraph; XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), periods`. **Relation:** adds a short obstruction to the tentative logarithmic formula.

### E17 — 67/99, two boxed periods

**Kind:** unpursued implication.

The boxes \(\tau=i\sqrt a\) and \(\tau=(1+i\sqrt a)/2\) follow from identifying the orthonormal basis \((e_0,e_1/\sqrt a)\) with \((1,i)\). The second formula retains the half-lattice generator \(v=(e_0+e_1)/2\), so replacing \(a\) by a length ratio would change it. P5 checks these formulas and supports Hua’s identical normalization.

**Context:** `hua_project/67.modern.tex: XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), first displayed periods; LM_140-3_text.tex, scans19–20, lattice normalization`. **Relation:** restates Hua’s formula and adds comparison with the older general period construction.

### E18 — 67/99 and 101, real fixed-point calculations

**Kind:** unpursued implication.

“deux composantes connexes” for \(E_a\) and “connexe” for \(E'_a\) follow respectively from \(2y\in\mathbf Z\) and \(y\in\mathbf Z\) in the displayed lattice bases. The calculation is insensitive to the sign slip/doubt in scan99’s difference, but it distinguishes the two integral involution types. P6 checks it and agrees with Hua’s section on real points. Hua further identifies the conformal quotients as an annulus and a Möbius strip, connecting this integral distinction with the surgery setting.

**Context:** `hua_project/67.modern.tex: XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), real-point paragraphs`. **Relation:** restates and checks the fixed-locus calculation.

### E19 — 67/101, cohomology display and two cases

**Kind:** unproved claim.

The formula “\(H^1(\gamma,E(\mathbf C))\simeq\pi_+/(1+\sigma)\pi\)” follows from the exact sequence with \(V\) and the vanishing of positive-degree cohomology of a real vector space under a group of order two. In the split lattice the norm image is \(2\pi_+\), while in the nonsplit lattice \((1+\sigma)v=u\) fills \(\pi_+\), giving \(\mathbf Z/2\) and 0. P6 checks precisely the computation that Hua already explains; it is an abelian lattice calculation, not the unresolved nonabelian computation in the results register.

**Context:** `hua_project/67.modern.tex: XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), cohomology paragraphs; notes/RESULTS_STATE.md, LM4_SUCCESSOR E.10`. **Relation:** restates and checks Hua’s computation; differs in scope from the open congruence-kernel problem.
**Results state:** LM4_SUCCESSOR E.10 (comparison only; remains open).

### E20 — 67/101, “les torseurs non triviaux”

**Kind:** own idea.

An explicit representative of \(E_a^!\) is the torus \(\mathbf C/(\mathbf Z+i\sqrt a\,\mathbf Z)\) with descent map \(z\mapsto\bar z+1/2\). Its square is a period translation and it has no fixed points, while its action on differences is the conjugation of \(E_a\), so it realizes the nonzero torsor class computed on the page. Confidence is high because these properties are direct calculations in P6; the construction adds a concrete model to Hua’s cohomological description without claiming novelty.

**Context:** `hua_project/67.modern.tex: XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), nontrivial torsor paragraphs`. **Relation:** adds an explicit affine descent model.

### E21 — 67/101, sentence with cancelled “sans”

**Kind:** reading question.

The frozen text records “surfaces conformes [cancelled: sans] bord non orientables,” while Hua’s geometric exposition says without boundary and notes that “sans” appears crossed through. The geometry of a nontrivial torsor does give a free antiholomorphic involution and hence a boundaryless Klein-bottle quotient (P6), but it does not undo the visible cancellation. This is a reading-state question kept separate from the mathematical correction.

**Context:** `hua_project/67.modern.tex: XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), final footnote`. **Relation:** agrees about the apparent cancellation and distinguishes it from Hua’s corrected exposition.

### E22 — 67/101, two occurrences of the descriptive adjective

**Kind:** reading question.

The frozen reading is `\unsure{intrinsèques}`, whereas Hua writes “inhomogènes.” Both passages identify the objects as torsors under the real elliptic group schemes, so the mathematical referent does not settle the word. This context-suggested alternative belongs only in the notes.

**Context:** `hua_project/67.modern.tex: XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), paragraph beginning “Reste” and final classification`. **Relation:** differs in the adjective, not in the explicit torsor definition.

### E23 — 67/97, tentative logarithmic coefficient

**Kind:** reading question.

The frozen formula has `\unsure{\tfrac14|4}\log a`, whereas Hua quotes \(\tfrac12\log a\). The mismatch is retained as a reading question; none of these coefficients repairs the invariance objection in E16.

**Context:** `hua_project/67.modern.tex: XII, “Les structures réelles d’une courbe complexe donnée (pages 93 à 97)” (source scans 94–98), final paragraph`. **Relation:** differs in the reported coefficient.

### E24 — 67/99, difference of conjugation and identity

**Kind:** reading question.

The frozen display reads \((0,2y)\), while Hua uses \((0,-2y)\) and marks the manuscript sign uncertain. The latter is the algebraic difference for the preceding map \((x,y)\mapsto(x,-y)\), but both give the same lattice-membership condition. The sign stays unchanged in the diplomatic file.

**Context:** `hua_project/67.modern.tex: XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), real-point calculation and sign footnote`. **Relation:** differs in the literal sign while agreeing on the consequence.

### E25 — 67/93–99, lattice reflections and periods

**Kind:** unpursued implication.

The determinant-minus-one condition “renversant l’orientation” specializes the Longue Marche’s \(\mathrm{GL}_2(\mathbf Z)\) action on the upper half-plane to fixed real structures, and the square/hexagonal cases reproduce its two exceptional lattice orbits. These pages add the integral split/nonsplit distinction and its real-locus consequences to that older analytic description. They supply low-genus examples for comparison, but no proof of the unresolved higher-genus profinite involution classification or the nonabelian congruence-kernel cohomology.

**Context:** `LM_140-3_text.tex, scans19–21, (26)–(29); LM_140-3_notes.md, LM_P060 R30–R34; notes/RESULTS_STATE.md, LM6 C.12 and LM4_SUCCESSOR E.10`. **Relation:** adds a real integral refinement to the analytic lattice model.
**Results state:** LM6 C.12; LM4_SUCCESSOR E.10 (both remain open).

### E26 — 67/93–101, pointed real curves versus real torsors

**Kind:** unpursued implication.

The finite automorphism groups, two reflection orbits and nontrivial torsors show why a real coarse \(j\)-value does not specify a real elliptic object. This supplies concrete data for the deferred “conjugaison” description recorded in the neighbouring package’s scan72, while leaving its compactification and stack descent unfinished. Keeping the central \(\pm1\) is essential, as in the Longue Marche’s exceptional elliptic stabilizers.

**Context:** `MPL_147_048-137_notes.md, R072-01/R072-02 (scan72); LM_140-2_text.tex, scans542–543; hua_project/67.modern.tex, XII, real forms and torsors`. **Relation:** adds explicit real fibres and torsor data to a deferred moduli description.

### E27 — 67/96, unlabelled colored drawings

**Kind:** own idea.

Hua calls this a sheet of spheres cut by great-circle arcs, which is a plausible interpretation of the unlabelled figures. The drawings by themselves do not identify elliptic parameters, quotient maps, or a claim about the preceding real-form classification. Confidence is medium for the spherical interpretation and low for any more specific mathematical connection, because no written labels supply one.

**Context:** `hua_project/67.modern.tex: XII, “Les structures réelles d’une courbe complexe donnée (pages 93 à 97)” (source scans 94–98), final sentence on their page95`. **Relation:** agrees with a tentative visual interpretation but limits what can be inferred.

### E28 — 67/91, kernel defining Q and quotient-intersection calculation

**Kind:** reading question.

The frozen kernel for \(Q\) preserves `\unsure{-|+}`, and the later intersection line preserves the uncertain \(2Q\) on its right. Hua writes the coherent definitions \(Q=\ker(1+\sigma)\) and \(M'\cap Q=2Q\) without reproducing the problematic enlarged-intersection equality. P1 verifies that interpretation mathematically, but neither the proof nor the modernised text resolves the image reading after freeze.

**Context:** `hua_project/67.modern.tex: XII, “Modules munis d’une involution (pages 90, 91 et 99)” (source scans 91–92,100), displayed kernel and paragraph on intersections`. **Relation:** differs by making the intended algebra explicit rather than preserving the literal doubtful display.
**Results state:** Hua, findings register, 67-involution-modules-triples.

### E29 — 67/92, first handwritten display on reused printout

**Kind:** reading question.

The rough sheet writes “\(\sigma(x,y)=x-y\),” while Hua explicitly replaces it by \((x,-y)\). The latter is the action used in E01’s reconstruction, but the missing pair notation is retained in the frozen text as a draft feature. The printed August1982 job dates belong to the reused sheet, not to the December1983 mathematical heading on scan91.

**Context:** `hua_project/67.modern.tex: XII, “Modules munis d’une involution (pages 90, 91 et 99)” (source scans 91–92,100), second proposition footnote; XII opening date`. **Relation:** agrees with Hua’s report of the literal rough formula and separates it from his correction.
**Results state:** Hua, findings register, 67-involution-modules-triples.

### E30 — 67/101, “Pour bien faire il faudrait aussi classifier”

**Kind:** self-flagged.

The request “il faudrait aussi classifier” is substantially answered immediately by the calculation of \(H^1(\mathbf R,E)\) and the definition of \(E_a^!\). What is achieved is the classification of torsors under each fixed elliptic group scheme; interpreting them as unpointed genus-one curves additionally uses their Jacobian and the automorphism action, which fixes the unique nonzero class here. Hua treats this as the completion of the genus-one conformal table, and P6 supplies a direct representative and the absence-of-real-points check.

**Context:** `hua_project/67.modern.tex: XII, “Période, points réels, torseurs (pages 98 à 100)” (source scans 99–101), last three paragraphs`. **Relation:** restates Hua’s interpretation and isolates the scope of the same-page answer.
