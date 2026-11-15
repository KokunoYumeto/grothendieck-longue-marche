## B. Cote 156-2: conic neighborhoods, ficelles, ordered cutting, and mailles

These notes use the frozen transcription of cote 156-2. References to earlier packages identify only the excerpted entries supplied in `RESULTS_STATE.md`; their underlying manuscripts and full research returns were not supplied, and a register status remains the cited run's claim unless explicitly reviewed there.

### B01 — Restricting the contraction quotient

**Source:** 156-2, scan 002, opening paragraph. **Kind:** unproved claim. **Quote:** “identifie ... à un sous-espace top.”

The argument asserts that $X'/A\to X/A$ is a topological embedding whenever $A\subset X'\subset X$, and sketches the closed-set proof rather than merely a set-theoretic bijection. An ambient closed set with a prescribed relatively closed trace in $X'$ automatically contains all of $A$ or avoids $A$ when that trace is saturated, because $A\subset X'$; this supplies the sketched argument without an additional normality hypothesis. The final written target “de $X$” is retained in the transcription; the immediately preceding map makes $X/A$ the natural target of this explanatory claim, which is a reading question rather than an emendation.

**Context:** search: `quotient|conique|voisinage`; **MPL_150_001-043 Q1b**, first-pass lead in `MPL_150_001-043_notes.md`, locates conic-neighborhood constructions at 150/012–015, 022–023 and 147/140–142; these pages **add** an elementary quotient-subspace argument, with no same claim identified in the supplied excerpt.

### B02 — Compact cone base and cofinal radial neighborhoods

**Source:** 156-2, scans 002–003. **Kind:** unpursued implication. **Quote:** “espace topologique compact”; “un système fond. de voisinages”.

His regular immersion is a condition on the collapsed point in $X/A$: a closed cone neighborhood has compact base and its base-complement is open. Compactness explains why uniformly smaller radial cones form a neighborhood basis, by a finite-subcover argument on the cone base; the preimages then form a neighborhood basis of the entire closed subset $A$. The construction does not supply a normal vector bundle or a product neighborhood of each individual point of $A$.

**Context:** search: `conique|tubulaire|normal`; **MPL_150_001-043 Q1b** (first-pass lead; 150/012–015, 022–023; 147/140–142) supplies the nearest terminology, while **EXIT_ONE_TYPE P1a1** in `EXIT_ONE_TYPE_results.csv` (Proved, return claim; MPL147/177–180) concerns normal-link homotopy fibers; 156-2 **adds a concrete quotient-cone definition** and **differs** from the latter's stronger reconstruction statement.

### B03 — The locality and tame-polyhedral assertions require their own checks

**Source:** 156-2, scan 003, NB 1 and NB 3. **Kind:** unproved claim. **Quote:** “L'hyp. ... est locale”; “Vraie pour ... modéré compact”.

He asserts invariance after replacing $X$ by any neighborhood of $A$, and validity for compact tame subspaces, with a compact polyhedral example. The first claim is naturally checked by shrinking the conic neighborhood, whereas the second needs a specified tame category and a regular-neighborhood construction for the pair; the word “modéré” alone does not state those hypotheses. These statements concern an entire subset collapsed to a point, so a theorem about conical neighborhoods at individual strata does not automatically settle them.

**Context:** search: `modérée|compact|polyhedral|conique`; **MPL_150_044-084 Q9**, first-pass lead in `MPL_150_044-084_notes.md` at 150/073–076, already flags the unspecified tame context, and **MPL_150_001-043 Q4b** (first-pass lead, 150/037–039) concerns compact Hauptvermutung; the present assertion **adds** a regular-neighborhood requirement rather than restating the latter theorem.

### B04 — A type mismatch in the exterior-neighborhood formula

**Source:** 156-2, scan 003, display defining $W'_t$. **Kind:** reading question. **Quote:** “$W'_t=X-V_t$”.

The page has just defined $V_t\subset X/A$ and its inverse image $W_t\subset X$, so the displayed subtraction mixes the ambient spaces unless the author is identifying the off-$A$ portions implicitly. Replacing $V_t$ by $W_t$ would make the following interior/exterior decomposition type-correct, but that is an explanatory possibility only and the frozen formula remains untouched. A later use of $W'_t$ should state which identification is intended.

**Context:** search: `voisinage|conique|tubulaire`; **MPL_150_001-043 Q1b**, first-pass lead (150/012–015, 022–023; 147/140–142), provides related neighborhood notation; this is an **additional local reading question**, with no matching formula in the supplied context.

### B05 — Connectivity versus the component-closure criterion

**Source:** 156-2, scan 004, conditions c and c′. **Kind:** unproved claim. **Quote:** “$c'\Longrightarrow c$”; “l'inverse ... fini de composantes connexes”.

He distinguishes connectedness after collapsing an endpoint from the assertion that the closure of every component of the complement meets both endpoints, and explicitly restricts the converse to finitely many components. This finiteness clause matters because infinitely many components can accumulate and cannot generally be separated by taking arbitrary unions of closed components. Any later use of c′ in the unrestricted topological setting should preserve the one-way implication actually asserted here.

**Context:** search: `comp. connexes|finite|connexes`; **MPL_150_044-084 N39**, first-pass lead in `MPL_150_044-084_notes.md` at 150/072, 077 (there compared with 147/180 and 149/134), discusses components versus fuller link information; the present finite-component qualification **adds** a distinct elementary connectivity issue and does not settle its homotopy-truncation question.

### B06 — Contraction stability is used as a structural tool

**Source:** 156-2, scan 004, two marginal notes and last assertion. **Kind:** unproved claim. **Quote:** “alors ... est une ficelle”; “est une ficelle ssi”.

The page asserts both stability under contraction of a closed subset of the interior and equivalence of the ficelle conditions before and after separately contracting the two endpoints. Connectivity passes through quotient maps, while the conic conditions require the quotient to leave suitable endpoint neighborhoods unaffected; these are the checks behind the repeated reductions to points on later pages. None of these assertions says that the original uncontracted space must itself be connected.

**Context:** search: `contraction|quotient|recollement`; no direct contraction-stability result occurs in the supplied excerpts; **MPL_150_044-084 N18**, first-pass lead (150/077, 081–084), concerns retaining attachment data under geometric changes, so this page **adds** a particular quotient operation rather than rederiving that lead.

### B07 — “Reduced ficelle is connected” has a narrower scope

**Source:** 156-2, scans 004–005; compare scan 011. **Kind:** unpursued implication. **Quote:** “Ficelle réduite est connexe”; “mais pas néc. ... \(\{a,b\}\)”.

For point endpoints, the two connected punctured spaces cover $X$ with nonempty intersection, so connectedness follows; removing both endpoints may still disconnect the space, as the circle drawing emphasizes. This does not justify the unrestricted connectedness claim later made on scan 011, because collapsing a disconnected endpoint can create connectivity that the original space lacked. The distinction is essential in B23 and B25.

**Context:** search: `connexe|quotient|comp. connexes`; no same reduced/unreduced distinction appears in the supplied register; this **adds** a qualification relevant to the reconstruction scope in **WG2 B15 (§1.2)**, an unchecked planning item in `PROGRAM_WARGAME_ROUND2_20261112.md` with no manuscript scan specified there.

### B08 — Open sides and closed sub-ficelles are not the same symbols

**Source:** 156-2, scans 005–006. **Kind:** reading question. **Quote:** “décomposition de $X\setminus C$”; “$X_{A,C}=\overline{U_{A,C}}\cup C$”.

Scan 005 uses heavily overwritten $U/X$ initials for the two sides of the complement, while scan 006 writes $X_{A,C}$ for their closure with the cutting locus adjoined. A proof of the cutting claims must distinguish the open side $U_{A,C}\subset X\setminus C$ from the closed piece $X_{A,C}$ containing $C$, even where the handwriting revises their notation. The frozen uncertainty alternatives record the overwritten initials and do not manufacture a consistent correction sequence.

**Context:** search: `recollement|pièces|closed`; **MPL_147_138-190 §69** (first-pass own-idea lead, 147/161–163) and **MPL_150_044-084 N18** (first-pass lead, 150/077, 081–084) discuss building pieces and attachments; this **adds** a local open-side/closed-piece distinction, with no exact notation match in their supplied excerpts.

### B09 — Uniqueness of sides is a statement in the reduced quotient

**Source:** 156-2, scan 005, bracket and marginal NB. **Kind:** unpursued implication. **Quote:** “de façon unique”; “Quand $A,B$ connexes”.

The side decomposition is identified through the two components of $X'\setminus C$ after contracting $A$ and $B$. He separately notes that the original sides are connected when the endpoints are connected, which would be redundant if that were already assumed in the definition. This explicit qualification is evidence against silently importing connected endpoints into Fic a–d.

**Context:** search: `connexes|quotient|strata`; no same uniqueness claim occurs in the supplied excerpts; the point **adds** a precise quotient-versus-original-space distinction to the coarse-data caution in **EXIT_ONE_TYPE P4e** (Proved, return claim in `EXIT_ONE_TYPE_results.csv`; MPL149/133).

### B10 — The proof of the first three ficelle conditions has a terminal mismatch

**Source:** 156-2, scan 006, proof of b. **Kind:** reading question. **Quote:** “ouverte ... dans $X\setminus\{a\}$”; “$X\setminus\{c\}$ ne serait pas connexe”.

The constructed clopen subset is asserted to lie in $X\setminus\{a\}$, but the last contradiction names $X\setminus\{c\}$, whose disconnection is precisely what a cutting locus is expected to produce. The evident proof target is the stipulated connectedness after removing the endpoint $a$, yet the text's final $c$ remains frozen. The intended argument can therefore be described without claiming that the displayed final contradiction is correct as written.

**Context:** search: `connexe|proof|quotient`; no same proof occurs in the supplied context; this is an **additional reading question**, relevant to the unchecked realization program **WG2 B15 (§1.2)** but not a resolution of it.

### B11 — Regular immersion is expressly the missing step

**Source:** 156-2, scan 006, last sentence; scan 007, Li c. **Kind:** self-flagged. **Quote:** “il manque encore ... d) d'immersion locale”.

After proving only a), b), and c), he explicitly withholds the conclusion that the two pieces are ficelles until the regular-immersion condition is supplied. Scan 007 proposes regular immersion of $C$ in the open complement as the missing hypothesis, relying on its cone-gluing lemma. The existence of the missing condition is therefore acknowledged, while the adequacy of the lemma still requires the qualification in B12.

**Context:** search: `conique|immersion|voisinage`; **MPL_150_001-043 Q1b** (first-pass lead; 150/012–015, 022–023; 147/140–142) supplies related conic constructions; the present explicit gap **adds** a source-local proof obligation rather than restating an established contextual result.

### B12 — The cone-gluing lemma lacks an explicit covering hypothesis

**Source:** 156-2, scan 007, opening lemma. **Kind:** unproved claim. **Quote:** “$Z'\cap Z''=\{c\}$”; “il f. et s.”

The lemma gives only two closed subsets meeting at $c$, without explicitly requiring $Z=Z'\cup Z''$ or a neighborhood version of that equality. With arbitrary extra pieces of $Z$ near $c$, conic neighborhoods in the two selected closed pieces cannot control the ambient germ; the application to complementary pieces has more structure than the literal statement. A valid restricted lemma should state that the pieces cover a neighborhood and check that their cone bases glue in the required way.

**Context:** search: `conique|recollement|gluing`; **MPL_150_044-084 N18** (first-pass lead, 150/077, 081–084) and **INTAKE 20261114 §13.6** (intake reading, not referee verdict, describing cote 150 without a narrower scan in this entry) already stress attachment data; this **adds** a missing ambient-cover hypothesis, not a contradiction of those broader claims.

### B13 — A literal countertest for the uncovered ambient space

**Source:** 156-2, scan 007, same lemma. **Kind:** own idea. **Quote:** “deux parties fermées”.

Take $Z=\mathbb Q$, $c=0$, $Z'=\{0,1\}$, and $Z''=\{0,-1\}$: the pieces are closed and $c$ has a one-point cone neighborhood in each, using the empty compact cone base allowed on scan 003. The rational line has no compact neighborhood of $0$, hence no closed neighborhood homeomorphic to a cone on a compact base. **Confidence: high**, because any rational interval contains sequences converging to an irrational number and therefore cannot lie in a compact subset of $\mathbb Q$; the example tests the literal lemma and does not refute its intended covered-space application.

**Context:** search: `conique|compact|gluing`; no direct example occurs in the supplied excerpts; this **adds a countertest** to the local proof gap in B12 and bears on the related conic-neighborhood lead **MPL_150_001-043 Q1b** (150/012–015, 022–023; 147/140–142), without changing its status.

### B14 — Tubular boundaries and contraction away from the cut

**Source:** 156-2, scan 007, example and lower marginal note. **Kind:** unproved claim. **Quote:** “Pour $t$ assez petit”; “$C$ est ... encore un lieu”.

He claims sufficiently small endpoint-neighborhood boundaries are lieux, and that contraction of a closed subset wholly on one side preserves the other cutting locus. The latter restriction is substantial: a contraction crossing both sides can erase the separation that defines a lieu. These assertions supply the collar-shrinking mechanism needed for the density and local filtering claims on scan 010, but the relevant neighborhoods and preservation of regular immersion should be tracked in a proof.

**Context:** search: `voisinage|conique|recollement`; **MPL_150_001-043 Q1b** (first-pass lead; 150/012–015, 022–023; 147/140–142) gives related neighborhood constructions, and **MPL_150_044-084 N18** (first-pass lead; 150/077, 081–084) concerns attachment retention; this **adds** concrete stability claims to compare with those leads.

### B15 — Disjointness of lieux is compatibility, not merely empty intersection

**Source:** 156-2, scans 007–009. **Kind:** unpursued implication. **Quote:** “(D) est un lieu de $F_{A,C}$ ou de $F_{B,C}$”.

For internal lieux, the definition requires one to remain a cutting locus in one of the two pieces produced by the other; empty set-theoretic intersection alone is not the definition. The exchange lemma is what makes this relation symmetric, and scan 010 identifies it with strict comparability in the chosen orientation. Consequently a finite family of admissible simultaneous cuts must be checked for this stronger compatibility before it is treated as a chain.

**Context:** search: `découpage|cutting|refinement`; **MPL_148_029-072 R29** (first-pass self-flagged/unproved lead at 148/058, 059, 061) concerns a different marked-circle cutting and erasure problem; the present definition **adds** a precise compatibility relation, while **WG2 B15 (§1.2)** remains an unchecked planning comparison rather than a ready-made refinement theorem.

### B16 — One cut corresponds to two pieces with a specified gluing homeomorphism

**Source:** 156-2, scan 008, marginal equivalence. **Kind:** unproved claim. **Quote:** “Pour mémoire”; “Équiv. de Catégories”.

The announced equivalence retains two actual ficelles and a homeomorphism of the ends to be identified, which is richer than the incidence pattern of two abstract vertices and one edge. A categorical proof must specify the morphisms on both sides and verify that cutting and gluing are quasi-inverse with those morphisms; the pages do not state this level of functorial detail. This is a concrete gluing program, not yet a claim that forgetting the pieces and gluing map preserves the space.

**Context:** search: `recollement|gluing|attachment`; **MPL_150_044-084 N18** (first-pass lead, 150/077, 081–084) and **STRATA C.8** in `STRATA_results.csv` (Proved, return claim; GALOIS A.8/B.3/B.5 comparison, no additional manuscript scan supplied) retain gluing data; 156-2 **adds** a specific homeomorphism-gluing category and **differs** from the latter's enhanced-coefficient pullback theorem.

### B17 — The exchange lemma rests on associativity of the geometric gluing

**Source:** 156-2, scan 008, lemma and proof. **Kind:** unpursued implication. **Quote:** “Il suffit de prouver”; “OPS ... réduits à des points”.

The displayed proof rewrites a three-piece decomposition by changing parentheses, thereby explaining why (D) lies beyond $C$ exactly when $C$ lies before (D). The argument uses both associativity of the pushout and preservation of the ficelle/lieu conditions after contracting the marked closed sets; its geometric content is not supplied by an equality of sets alone. Scan 013 contains a cancelled rehearsal of essentially this exchange statement, rather than an explicit refutation of the live proof on 008.

**Context:** search: `recollement|gluing|pièces`; **MPL_150_044-084 N18** (first-pass lead, 150/077, 081–084) and **MPL_147_138-190 §69** (first-pass own-idea lead, 147/161–163) are related building-piece discussions; this **adds** a precise associativity test for cuts without rederiving their broader reconstruction proposals.

### B18 — Two ordered cuts retain five pieces of data

**Source:** 156-2, scan 009. **Kind:** unpursued implication. **Quote:** “quintuplets”; “$h_{21}$”; “$h_{32}$”.

The three ficelles and two endpoint homeomorphisms are counted explicitly as a quintuple, so the announced equivalence again carries geometric labels and attachment maps. The repeated $F_1$ in the written tuple is doubtful in the transcription, while the following prose separately names $F_1,F_2,F_3$; the research explanation can identify the intended data without changing that reading. This is the first nontrivial finite-cut pattern in which coherence of successive gluing can be tested.

**Context:** search: `gluing|recollement|finite`; **MPL_150_044-084 N18** (first-pass lead; 150/077, 081–084) and **STRATA C.8** (Proved, return claim; GALOIS A.8/B.3/B.5 comparison, no additional scan specified) provide related retention of gluing data; these pages **add** a finite geometric instance rather than identify it with an unlabeled finite category.

### B19 — The order uses families of lieux, not inclusion of underlying regions

**Source:** 156-2, scans 009–010, definition and upper-left warning. **Kind:** unpursued implication. **Quote:** “$C\le D$ ssi $F_C\subset F_D$”; “n'implique ... pas”.

He defines the order through the collection of lieux of the initial sub-ficelle and asserts the equivalent membership criterion $C\in F_D$. The following marginal warning explicitly rejects replacing this with inclusion, or even equality, of the underlying regions $X_{A,C}$ and $X_{A,D}$. An order-theoretic reconstruction must therefore retain the cutting structure of those regions, and the heavily revised warning should not be strengthened beyond its secure negative point.

**Context:** search: `poset|relation d'ordre|incidence`; **MPL_121_049-073+153+155 R121-08**, first-pass lead in that package's notes at 121/050–052 (compared there with 147/179–180, 185–190), already says incidence alone is only part of reconstruction; 156-2 **adds** a specific order-versus-subset distinction, while **STRATA A.4** (Proved, return claim; finite minimum-vertex realization) starts from a given poset and does not settle this extraction problem.

### B20 — Local filtering and density remain geometric claims

**Source:** 156-2, scan 010, a), b), b′), c). **Kind:** unproved claim. **Quote:** “filtrant décroissant”; “filtrant croissant”; “divisibilité”.

The ordered set is asserted to have distinct endpoint elements, downward-filtered strict upper cones, upward-filtered strict lower cones, and an intermediate lieu between any strictly comparable pair. A proof should construct simultaneous sufficiently small collar cuts inside the relevant sub-ficelle, using B14, rather than infer these properties from the bare definition of a partially ordered set. No finiteness of the full set of lieux follows from these axioms; indeed strict density is normally incompatible with finiteness once distinct comparable endpoints exist.

**Context:** search: `poset|finite|refinement`; **WG2 B15 (§1.2)** is an unchecked planning item without a source scan in its register entry, and **STRATA A.4** is a return claim for finite posets; the manuscript **differs in scope** by introducing a generally infinite ordered family, while leaving the desired connection to finite models unproved.

### B21 — The general finite chain is an iterated geometric decomposition

**Source:** 156-2, scan 010, final paragraph. **Kind:** unproved claim. **Quote:** “$n$ lieux intermédiaires, mutuellement disjoints”; “$n+1$ ficelles”.

The equivalence with $n+1$ oriented pieces and $n$ gluing homeomorphisms is stated for a totally ordered family of pairwise compatible internal lieux. Induction using the exchange lemma is a plausible route, but a category of refinements and transition maps between different chains is not defined on this page. The statement supplies finite decompositions with geometric data, not a completed inverse system whose limit is asserted to be a form.

**Context:** search: `finite|refinement|recollement`; this **adds finite decomposition data** relevant to the context README conjecture and **WG2 B15 (§1.2)** (unchecked plan), while **MPL_150_044-084 N18** (first-pass lead, 150/077, 081–084) cautions that the attachment maps retained here cannot simply be discarded.

### B22 — Existence, connectedness, and uniqueness are separate assertions

**Source:** 156-2, scan 011, opening NB. **Kind:** unproved claim. **Quote:** “il f. et s. qu'il soit connexe”; “C'est gros!”; “C'est le seul cas d'exception!”.

The NB bundles a necessity claim, a sufficiency claim for compact triangulable spaces, existence of a reduced structure, and a uniqueness exception for a segment. The disconnected example in B23 refutes necessity for the literal, possibly nonreduced definition; it does not refute existence on connected nontrivial polyhedra or uniqueness of the reduced structure on an interval. The finite-polyhedron sufficiency and reduced uniqueness assertions are established by the separate arguments in B52–B53, rather than inheriting the fate of the bundled equivalence.

**Context:** search: `compact|triangulable|polyhedra`; **MPL_151_032-075 Q4-02**, first-pass lead at 151/044–045, 059–061, concerns compact polyhedral object comparisons, and **MPL_150_001-043 Q4b** (150/037–039) concerns Hauptvermutung; 156-2 **adds** a different existence/classification claim that neither supplied excerpt settles.

### B23 — A disconnected space satisfying the literal ficelle axioms

**Source:** 156-2, scan 011, compared with Fic a–d on 004. **Kind:** own idea. **Quote:** “qu'il soit connexe”.

Let $X=[0,1]\times\{-1,+1\}$, $A=\{0\}\times\{-1,+1\}$, and $B=\{1\}\times\{-1,+1\}$: the two intervals are disconnected, but contracting either endpoint set joins the two corresponding arms, so both quotients in Fic c are connected. The maps $(t,\varepsilon)\mapsto\varepsilon t$ and $(t,\varepsilon)\mapsto\varepsilon(1-t)$ identify $X/A$ and $X/B$ with intervals having conic neighborhoods at the contracted points, and a), b), d) therefore hold as well. **Confidence: high**, by these explicit quotient maps; requiring both endpoints to be connected repairs this necessity direction, but that requirement is only proposed later in the margin and is absent from Fic a–d.

**Context:** search: `connexe|quotient|compact`; no direct example occurs in the supplied register; this **adds a counterexample** to the present manuscript's unrestricted statement and bears on the scope of **WG2 B15 (§1.2)** (unchecked plan), without changing any existing return status.

### B24 — The interval classification also needs the connected-end restriction

**Source:** 156-2, scan 011, upper marginal classification. **Kind:** unproved claim. **Quote:** “les seules ... ficelles sur ([0,1])”.

The displayed endpoint intervals $A=[0,\alpha]$, $B=[\beta,1]$ describe the connected-end case, up to exchanging the unordered ends. They do not exhaust literal ficelles with disconnected endpoints, as B25 demonstrates. The small uncertainty about a prime on \(\beta\) is a separate reading issue and has no bearing on this structural omission.

**Context:** search: `compact|connexes|interval`; no same classification appears in the supplied excerpts; this **adds a hypothesis correction** relevant to **WG2 B15 (§1.2)** (unchecked plan) rather than a consequence of the finite-poset realization claims **STRATA A.4/A.12**.

### B25 — A nonstandard ficelle on the ordinary interval

**Source:** 156-2, scan 011, compared with 002 and 004. **Kind:** own idea. **Quote:** “$A=[0,\alpha]$, $B=[\beta,1]$”.

Take $X=[0,1]$, $A=\{0,1\}$, and $B=\{1/2\}$: $X/A$ is a circle with a conic neighborhood at the identified endpoints, $X/B=X$, and both quotients in Fic c are connected open intervals. Thus Fic a–d hold although $A$ is disconnected and not an endpoint interval. **Confidence: high**, by the explicit quotient descriptions, independently checked in `records/ficelle_interval_counterexample.md`; this does not contradict uniqueness of the *reduced* interval ficelle and prevents claiming an unrestricted classification into exactly two oriented equivalence classes.

**Context:** search: `connexes|quotient|interval`; no direct match occurs in the supplied context; this **adds a literal counterexample** to the present classification and qualifies the scope of **WG2 B15 (§1.2)** (unchecked plan), with no claimed progress on a listed open theorem.

### B26 — Endpoint enlargement is expressly withdrawn

**Source:** 156-2, scan 011, cancelled NB and adjacent margin. **Kind:** withdrawn in the same text. **Quote:** “$A\subset A'$, $B\subset B'$”; “Faux \(\longrightarrow\) idiot!”.

The cancelled statement says that enlarging both ends to disjoint closed regularly immersed subsets preserves a ficelle, and the margin retracts it at the same scan. It must not be used to prove the following proposed equivalence of structures, or silently revived under the later suggestion that ends be connected or contractible. B27 gives an explicit failure even with connected contractible enlarged ends.

**Context:** search: `recollement|connexes|contractile`; no same enlargement lemma appears in the supplied excerpts; this **adds an author-withdrawn claim** beside the attachment-data caution **MPL_150_044-084 N18** (first-pass lead, 150/077, 081–084), not a contradiction of that lead.

### B27 — A tripod explains the connectivity obstruction to enlargement

**Source:** 156-2, scan 011, the retracted enlargement statement. **Kind:** own idea. **Quote:** marginal “(Connexité)”.

Let $X$ be a three-armed finite tree, with $A$ and $B$ two distinct leaf points; this is a reduced ficelle because removing either chosen leaf leaves a connected space and each endpoint is conical. Enlarge $A$ to its entire closed arm including the central vertex, keeping $B$ fixed: the enlarged set is connected, contractible, and regularly immersed, but its removal leaves the other two arms disconnected, which contraction of the single point $B$ cannot repair. **Confidence: high**, by this finite-graph calculation; connected or contractible endpoints therefore do not by themselves rescue the discarded enlargement rule.

**Context:** search: `connexes|contractile|gluing`; no same example is supplied; this **adds a concrete witness** to the author's own retraction, related only in scope to **MPL_150_044-084 N18** (first-pass lead, 150/077, 081–084).

### B28 — Universal equivalence of oriented structures is also withdrawn

**Source:** 156-2, scan 011, last body sentence and margin. **Kind:** withdrawn in the same text. **Quote:** “soupçonne”; “Faux déjà dans le cas du segment!”.

He tentatively proposes that all oriented ficelle structures on a triangulable $X$ are equivalent under the relation generated by coordinatewise endpoint inclusion, then explicitly rejects it on the interval. Within the connected-end interval subfamily, the two orientations cannot be joined by these inclusions and each orientation has a common minimal endpoint pair, giving exactly two classes there. The extra disconnected-end structures in B25 mean that this last exact count must not be asserted for the unrestricted family.

**Context:** search: `isotopy|équivalence|compact`; **MPL_151_032-075 Q4-03**, first-pass lead at 151/044–045, 059–061, concerns homeomorphism isotopies, which is a **different equivalence problem**; the present author-retracted endpoint-inclusion conjecture **adds** no proof of that lead or of a register classification.

### B29 — Restricting loci by a property also restricts their links

**Source:** 156-2, scan 012. **Kind:** conjecture. **Quote:** “il est bon de ... supposer”; “restriction correspondante”.

He proposes imposing a property $P$ on endpoints and internal lieux, but also on the boundaries of their conic neighborhoods on each side, to retain the preceding order properties. The phrasing is a proposed sufficient mechanism, not a demonstrated closure theorem for every intrinsic property $P$. A proof must identify which operations on these links preserve $P$ when constructing intermediate or common-refinement cuts.

**Context:** search: `normal|link|conique`; **EXIT_ONE_TYPE P1a1** (Proved, return claim; MPL147/177–180) and **MPL_150_044-084 N39** (first-pass lead; 150/072, 077; comparisons 147/180, 149/134) emphasize link information; 156-2 **adds** the explicit two-sided (P)-condition and does not rederive their different homotopy statements.

### B30 — The point condition is a restricted cutting theory, not an automatic classification of $X$

**Source:** 156-2, scan 012, example 1. **Kind:** unpursued implication. **Quote:** “être ... réduit à un pt”; “théorie des segments top.”

The example identifies a point-valued special case of the allowed ends, loci, and their side links, while the final abbreviation remains uncertain between `ord.` and `ind.`. It should not be expanded into the stronger assertion that every ambient space carrying such a restricted family of cuts is itself an interval: the uncut regions may retain additional topology. The point example is best tested at the level of its resulting ordered cutting structure and its declared admissible loci.

**Context:** search: `incidence|link|poset`; **MPL_121_049-073+153+155 R121-08** (first-pass lead; 121/050–052, compared with 147/179–180, 185–190) and **EXIT_ONE_TYPE P4e** (Proved, return claim; MPL149/133) both warn about information lost by coarse descriptions; this example **adds** a case where the intended level of classification needs to be specified.

### B31 — A cancelled duplicate is not a second mathematical refutation

**Source:** 156-2, scan 013, cancelled lemma; compare live scan 008. **Kind:** reading question. **Quote:** “Alors $C$ est un lieu de $F_{A,D}$”.

The cancelled block rehearses the exchange of two internal cutting loci already stated and argued on scan 008, with unfinished wording and uncertain overwritten letters. Unlike the explicit “Faux” annotations on scan 011, this cancellation supplies no reason to infer that the underlying exchange lemma was abandoned as false. It records a discarded draft of an argument whose live occurrence must be assessed separately.

**Context:** search: `cancelled|withdrawn|recollement`; **MPL_148_029-072 R39**, a first-pass withdrawn/unpursued lead at 148/067, likewise preserves a cancelled gluing proposal; the present block **adds** a separate documentary case and does not establish the same mathematical claim.

### B32 — Ball and sphere examples specify admissible loci, not all embeddings

**Source:** 156-2, scans 013–014. **Kind:** unpursued implication. **Quote:** “homéom. à $B^n$”; “décompositions par des $S^n$”.

The examples propose decompositions of products or spheres by loci of prescribed ball or sphere homeomorphism type. Homeomorphism type alone is insufficient to certify a lieu: the separation and regular-immersion conditions of the definition remain in force, so the drawings cannot justify including every embedding of such a ball or sphere. The geometric pieces and side-neighborhood data remain part of the proposed theory.

**Context:** search: `sphere|polyhedra|normal|link`; **RESIDUE A.7** (Proved, return claim in `RESIDUE_results.csv`; finite-fiber sphere obstruction, no manuscript scan supplied in that entry) and **EXIT_ONE_TYPE P4e** (Proved, return claim; MPL149/133) concern losses in coarser descriptions; these examples **add geometric test objects** without resolving either comparison by finite incidence data.

### B33 — The bicollar is an additional condition

**Source:** 156-2, scan 014, last paragraph. **Kind:** unpursued implication. **Quote:** “On peut aussi exiger”; “$C\times]-1,1[$”.

He explicitly offers a product neighborhood with the two half-products lying in the corresponding pieces as a further requirement. This is stronger than regular immersion defined only after collapsing the whole closed set: a cone on three points already has a regularly immersed vertex, but its neighborhood is not an interval. The example illustrates the difference between the two definitions, not a claim that a three-armed vertex is an internal lieu of a reduced ficelle.

**Context:** search: `collar|conique|tubulaire`; **INTAKE 20261114 §13.6** (intake reading, not referee verdict; account of cote 150) and **MPL_150_001-043 Q1b** (first-pass lead; 150/012–015, 022–023; 147/140–142) provide related collars and conic germs; the new optional product condition **adds a stronger local model** rather than restating the quotient-cone condition.

### B34 — `Comp` is a Boolean algebra of clopens

**Source:** 156-2, scans 015–016. **Kind:** unpursued implication. **Quote:** “\(\operatorname{Hom}_{\mathrm{cont}}(Z,\{0,1\})\)”; “$E^2=E$”.

The written formula identifies `Comp(Z)` with all clopen subsets of $Z$, with symmetric difference as addition, intersection as multiplication, and complement $E\mapsto1+E$. It is not the set $\pi_0(Z)$, and “un composant” on scan 016 may therefore mean a union of connected components according to the author's own definition. The distinction is necessary before comparing this invariant with any link homotopy or component-set construction.

**Context:** search: `Comp|clopen|Boolean|rives|comp. connexes`; no same Boolean definition appears in the supplied context; it **adds** a side invariant beside **EXIT_ONE_TYPE P1a1** (Proved, return claim; MPL147/177–180) and **MPL_150_044-084 N39** (first-pass lead; 150/072, 077), without replacing their fuller link data.

### B35 — Rives are germs of clopen choices on punctured neighborhoods

**Source:** 156-2, scan 015, first display. **Kind:** unpursued implication. **Quote:** “\(\lim_{\longrightarrow}\operatorname{Comp}(V\setminus A)\)”.

The direct limit identifies two clopen choices when they agree after shrinking to a smaller neighborhood of the entire closed set $A$. It therefore differs from recording only the global components of $X\setminus A$, and it retains no metric scale or preferred choice of tubular boundary. This is a local-germ construction at $A$, even though $A$ itself may be extended or disconnected.

**Context:** search: `germes|voisinage|proespaces|normal`; **MPL_150_001-043 Q1b** (first-pass lead; 150/012–015, 022–023; 147/140–142) supplies neighboring germ terminology, while **MPL_150_044-084 N39** (first-pass lead; 150/072, 077) concerns homotopy prospaces; 156-2 **adds a Boolean germ invariant** and **differs in retained information** from the latter.

### B36 — The link identification is plausible for the stated compact conic model

**Source:** 156-2, scan 015, NB 1; compare 002–003. **Kind:** unproved claim. **Quote:** “\(\operatorname{Riv}(A,X)\simeq\operatorname{Comp}(S_{A,X})\)”.

For a chosen conic neighborhood, punctured smaller neighborhoods have the form of the compact base times a connected radial interval, so their clopens are exactly those of the base. Cofinality of these neighborhoods, established by the compact-base condition, supplies the proposed direct-limit identification. The invariant algebra is intrinsic, while its particular presentation using $S_{A,X}$ follows the chosen conic structure; no unique homeomorphism type of all possible cone bases is established here.

**Context:** search: `normal|link|conique`; **EXIT_ONE_TYPE P1a1** (Proved, return claim; MPL147/177–180) and **MPL_150_001-043 Q1b** (first-pass lead; 150/012–015, 022–023) provide related link and conic constructions; this **adds a zero-dimensional Boolean comparison**, not the full normal-link homotopy comparison in the register.

### B37 — The paracompact comparison matches a standard sheaf theorem

**Source:** 156-2, scan 015, NB 2; scan 016, first assertion. **Kind:** unproved claim. **Quote:** “pour tt faisceau”; “injective, et bijective si $X$ paracompact”.

Because $A$ is already closed, the neighborhood-section formula agrees with Schapira (2023, Proposition 10.1.2(iii), printed p. 176), with the standard Hausdorff convention included in paracompactness. Injectivity follows without paracompactness because sections with equal germs along $A$ agree on the union of suitable neighborhoods, while surjectivity uses a locally finite shrinking to extend and glue local representatives near $A$. The cited statement for sheaves of modules suffices for the \(\mathbb F_2\)-algebra used here.

**Context:** search: `paracompact|neighborhood|colim|rives`; no same theorem is present in the supplied excerpts; the page **adds a precise sheaf step** alongside **INTAKE 20261114 §13.6** (intake reading, not referee verdict, on cote 150's reconstruction), rather than requiring a new proof of any listed settled entry.

### B38 — The sheaf spectrum leaves its base convention implicit

**Source:** 156-2, scan 015, last paragraph. **Kind:** reading question. **Quote:** “\(\widetilde A=\operatorname{Spec}(i_*(\mathbb F_{2\,U}))\)”.

The frozen formula contains neither an explicit restriction to $A$ nor a definition of `Spec` for this sheaf. One consistent modern interpretation is $\widetilde X=\operatorname{Spec}_X(i_*\mathbb F_{2,U})$ and $\widetilde A=\widetilde X\times_X A$, using the relative stalk-prime construction described by Gillam (2011, §2.2 and §3.3); this is a proposed formalization, not a corrected transcription. Its mathematical suitability is high because it retains the base point and leaves $U$ unchanged, but the historical identification remains provisional because the page omits the convention.

**Context:** search: `Spec|rives|normal|attachment`; no same spectrum definition occurs in the supplied context; this **adds a base-retention question** beside **EXIT_ONE_TYPE P4e** (Proved, return claim; MPL149/133) and **MPL_150_044-084 N18** (first-pass lead; 150/077, 081–084), without rederiving their information-loss claims.

### B39 — Relative Stone space, étalé space, and global spectrum differ

**Source:** 156-2, scans 015–017. **Kind:** own idea. **Quote:** “\(\widetilde A_i\longrightarrow A\)”.

For $X=S^1\times[-1,1]$ and $A=S^1\times\{0\}$, the Boolean sheaf along $A$ is locally constant with ring $\mathbb F_2^2$: its relative Stone spectrum is two circles, its étalé space of ring elements is four circles, and the ordinary spectrum of its global algebra is two points. The maps to $A$ in the later pushout require the first kind of object, or equivalent base-preserving data, rather than either of the other two constructions. **Confidence: high**, by the explicit product calculation; this is a diagnostic example for B38, not a claim that the manuscript spells out all three alternatives.

**Context:** search: `coarse maquette|link|attachment`; this **adds a concrete base-loss test** to **EXIT_ONE_TYPE P4e** (Proved, return claim; MPL149/133) and **MPL_150_044-084 N18** (first-pass lead; 150/077, 081–084), whose different settings and supplied statuses remain unchanged.

### B40 — The zero algebra and complementary pairs can be checked directly

**Source:** 156-2, scan 016. **Kind:** unpursued implication. **Quote:** “nulle ssi $A$ est ouvert”; “\(\rho+\rho'=1\)”.

The equality $0=1$ in the filtered colimit holds exactly when some neighborhood $V$ has $V\setminus A=\varnothing$, which is equivalent to openness of the already closed $A$. In a nonzero Boolean algebra a birive is an unordered complementary pair, and its decomposition of a Stone spectrum is the idempotent–clopen correspondence (The Stacks Project Authors, n.d.-c, Lemmas 10.21.1 and 10.21.3, Tag 04PN). A nontrivial pair is a global decomposition of the germ algebra; it does not yet imply the ficelle conditions later imposed for a maille. The doubtful cancelled words “Ceci doit être” record tentative local wording beside the distinctness observation, without specifying a separate conjecture.

**Context:** search: `birive|Boolean|clopen|rives`; no same construction appears in the supplied excerpts; this **adds** the algebra behind the new cutting operation, bearing on the README's finite-cutting guess without settling **WG2 B15 (§1.2)**, which remains an unchecked plan.

### B41 — Nontrivial birives need not separate at every point of the node

**Source:** 156-2, scan 016, definition of local disconnection. **Kind:** own idea. **Quote:** “$A$ disconnect $X$ loc.\(^{t}\)”.

For two distinct points $A=\{p,q\}\subset\mathbb R^2$, small disjoint punctured disks give $\operatorname{Riv}(A,X)\cong\mathbb F_2^2$, hence a nontrivial birive, although neither punctured disk is disconnected. **Confidence: high**, from this explicit neighborhood computation: the definition concerns a germ around the whole set $A$, and one of the two rive sections may vanish in the stalk at a particular point. This example is not asserted to define a maille, whose additional conditions appear on scans 017–018.

**Context:** search: `normal|link|comp. connexes`; the example **differs in scope** from pointwise or stratal normal-link comparisons in **EXIT_ONE_TYPE P1a1** (Proved, return claim; MPL147/177–180) and **MPL_150_044-084 N39** (first-pass lead; 150/072, 077), and **adds** a warning against conflating them.

### B42 — Compactness alone does not make the side algebra finite

**Source:** 156-2, scans 002 and 015–016. **Kind:** own idea. **Quote:** “espace topologique compact”; “algèbre ... idempotente”.

The cone on a Cantor space satisfies the compact-base conic condition at its vertex, but its rive algebra is the infinite Boolean algebra of Cantor clopens. **Confidence: high**, because the radial computation in B36 applies directly and the Cantor set has arbitrarily fine finite clopen partitions. Any assertion that there are only finitely many sides therefore needs additional tame or finiteness hypotheses; the general Boolean definition does not provide them.

**Context:** search: `compact|finite|modérée|refinement`; this **qualifies** the context README conjecture and **WG2 B15 (§1.2)** (unchecked plan), while **MPL_151_032-075 Q4-02** (first-pass lead; 151/044–045, 059–061) concerns a separately specified compact tame setting and is not contradicted by the Cantor example.

### B43 — Equal rive algebras can conceal different links

**Source:** 156-2, scan 015, NB 1. **Kind:** own idea. **Quote:** “\(\operatorname{Comp}(S_{A,X})\)”.

The vertex inclusions in cones on $S^1$ and $S^2$ both give the two-element rive algebra because each link is connected, although their link dimensions and homotopy groups differ. **Confidence: high**, by the connectedness calculation; the example rules out recovery from the Boolean side algebra alone, not recovery from all enriched cuttings retaining their actual pieces and gluing maps. It therefore provides a bounded test of the finite-data conjecture rather than a general negative reconstruction theorem.

**Context:** search: `normal|link|coarse maquette|proespaces`; this **adds a local information-loss test** to **EXIT_ONE_TYPE P4e** (Proved, return claim; MPL149/133), **EXIT_ONE_TYPE P1a1** (Proved, return claim; MPL147/177–180), and **MPL_150_044-084 N39** (first-pass lead; 150/072, 077), without rederiving those entries.

### B44 — `Maille` replaces `boucle` and has additional admissibility conditions

**Source:** 156-2, scans 015 and 017. **Kind:** unpursued implication. **Quote:** cancelled “boucle topologique”; live “maille”.

The later terminology replaces the earlier section heading, while the definition requires regular immersion of $A$ and the ficelle conditions a), b), c) for the fully cut space with its two distinguished boundary pieces. A chosen nontrivial birive alone does not establish these requirements, and the disconnected-node example B41 must not be promoted into a maille example. The construction is a one-node cyclic counterpart to a ficelle, with admissibility carrying substantive geometric content.

**Context:** search: `boucle|maille|cutting|circles`; **MPL_148_029-072 R29** and **R34** (first-pass leads at 148/058–059, 061 and 148/055, 061, 064) concern marked-circle cutting and erasure; these pages **add a distinct node-and-birive definition**, without identifying it with those earlier operations.

### B45 — Regular immersion of the cut boundary and the converse remain unproved

**Source:** 156-2, scan 017, first paragraph and margin. **Kind:** self-flagged. **Quote:** “alors ... régulièrement immergé”; doubtful “réciproq.”.

The parenthesis transfers regular immersion from $A\subset X$ to the full cut boundary and its two clopen pieces, and the marginal abbreviation appears to ask for or assert a converse. Neither direction is proved on this page, and the marginal reading is itself uncertain. A formal spectrum model must first be fixed, then its relation to the original conic neighborhoods checked, before this transfer can be treated as a theorem.

**Context:** search: `conique|normal|voisinage`; **MPL_150_001-043 Q1b** (first-pass lead; 150/012–015, 022–023; 147/140–142) supplies related models; the present parenthesis **adds a specific unverified transfer** and does not follow directly from **EXIT_ONE_TYPE P1a1** (return claim; MPL147/177–180).

### B46 — The partial cut retains two whole copies of the node

**Source:** 156-2, scan 017, pushout and following maps. **Kind:** unpursued implication. **Quote:** “\(\operatorname{Dec}_{\beta}(A,X)\)”; “$A\times\beta$”.

The displayed pushout replaces each spectral side separately by a copy of $A$, giving a map to $X$ that is asserted to be an isomorphism off $A$ and to have the stated two copies over the node. This records more than an ordinary quotient collapsing both sides together: the selected complementary-pair labels remain distinct. In a rigorous implementation the closed embeddings and pushout topology must be checked, and this construction still does not certify that the resulting pair is a ficelle for every birive.

**Context:** search: `recollement|gluing|attachment`; **MPL_150_044-084 N18** (first-pass lead; 150/077, 081–084) and **INTAKE 20261114 §13.6** (intake reading, not referee verdict, on cote 150) retain attachment maps; 156-2 **adds a specified two-sided pushout**, differing from the coherent-coefficient pullback in **STRATA C.8** (Proved, return claim).

### B47 — The partial-cut criterion is an asserted equivalence, not a formal consequence of terminology

**Source:** 156-2, scan 018, first paragraph. **Kind:** unproved claim. **Quote:** “on voit”; “ssi ... est une ficelle top.”

The author identifies a maille with the condition that its partial cut, equipped with the two copies of $A$, is a ficelle. This relies on transferring the regular-immersion and connectivity conditions between the full and partial cuts, precisely where scan 017 leaves proof obligations. Choosing an orientation then means choosing one of the two rive labels, once the maille conditions have been met.

**Context:** search: `recollement|gluing|conique`; no same equivalence is supplied; it **adds a concrete criterion** beside the reconstruction discussion **MPL_150_044-084 Q2** (first-pass lead; 150/073–084, especially 074, 076–077, 084), without establishing the broader realization comparison discussed there.

### B48 — Reduction to point nodes is proposed but its scope is uncertain

**Source:** 156-2, scan 018, rotated marginal NB. **Kind:** self-flagged. **Quote:** doubtful “Dans tout ce qui précède”; “se réduire au cas”.

The margin proposes reducing $A_1,A_2$ to points, but its exact opening and attachment are doubtful, so it cannot license an unrestricted retroactive reduction of every preceding construction. In particular, contracting a disconnected node can change connectivity of the ambient space and of a side containing another contracted node; deleting the contracted node itself leaves its complement homeomorphic to the original complement. A proof should specify which conditions survive the reduction before using it in the symmetry assertion on scan 019.

**Context:** search: `quotient|comp. connexes|normal`; this **adds a scope question** to the coarse-data distinction in **EXIT_ONE_TYPE P4e** (Proved, return claim; MPL149/133) and the component/link lead **MPL_150_044-084 N39** (150/072, 077), without treating either as a proof of the reduction.

### B49 — Two mailles require a common decomposition, not just disjoint nodes

**Source:** 156-2, scans 018–019, conditions a), b), c). **Kind:** unpursued implication. **Quote:** “$A_1\cap A_2=\varnothing$”; “définit à la fois ... $\beta_1$, et $\beta_2$”.

The relation requires the second node to be a lieu after cutting at the first and requires the resulting two sides to induce both specified birives. These conditions are stronger than disjointness of the node subsets, and the repeatedly revised word “comparables/compatibles” remains a lexical uncertainty rather than a settled equivalence relation. For nonconnected nodes, the asserted “deux composantes connexes” deserves particular care: the earlier ficelle axioms guarantee connectedness of certain quotients, not automatically of every uncontracted side.

**Context:** search: `cutting|recollement|comp. connexes`; **MPL_148_029-072 R29** (first-pass lead; 148/058–059, 061) concerns an earlier cutting-scope issue, while **MPL_150_044-084 N18** (150/077, 081–084) retains gluing data; the present conditions **add a two-node compatibility test** rather than a general common-refinement theorem.

### B50 — Symmetry is announced at the stopping point

**Source:** 156-2, scan 019, final sentence. **Kind:** unproved claim. **Quote:** “Je dis que cette condition est en fait symétrique”.

The manuscript ends by asserting symmetry under exchange of the two node-and-birive pairs, without giving the proof in the supplied continuation. A natural proof target is an order-independent simultaneous cutting whose two complementary regions induce both birives, but its construction and the requisite connectedness/regular-immersion checks have not been supplied here. The stopping point therefore records an open proof obligation within this package, not a demonstrated symmetric category of all cuttings.

**Context:** search: `recollement|gluing|cutting|refinement`; this **adds a specific unfinished symmetry problem** relevant to **WG2 B15 (§1.2)** (unchecked planning item) and the attachment-data lead **MPL_150_044-084 N18** (150/077, 081–084), without resolving any listed open register theorem.

### B51 — A positive profinite consequence of the Boolean algebra

**Source:** 156-2, scans 015–016. **Kind:** own idea. **Quote:** “algèbre ... idempotente”.

Every prime quotient of the Boolean ring $R=\operatorname{Riv}(A,X)$ is $\mathbb F_2$, so its spectrum is a compact Hausdorff totally disconnected space, hence a cofiltered inverse limit of finite discrete spaces (The Stacks Project Authors, n.d.-b, Lemma 10.26.5; n.d.-d, Lemma 5.22.2). More concretely, the subalgebra generated by $n$ elements has at most $2^n$ nonzero atoms and is finite, so the finite Boolean subalgebras of $R$ give the finite spectral quotients and their refinement maps. **Confidence: high**, by the Boolean identities and the cited spectrum criteria: this is a positive reconstruction statement for the side algebra's Stone spectrum, and not for the relative cut space over $A$ or the ambient form. The two-circle calculation in B39 shows why that distinction is substantive.

**Context:** search: `finite|pro|refinement|form`; this **partially supports and sharply limits** the context README guess and **WG2 B15 (§1.2)** (unchecked plan), while **EXIT_ONE_TYPE P4e** (Proved, return claim; MPL149/133) concerns fuller link information that the side algebra does not retain.

### B52 — Existence of a reduced ficelle on every connected nontrivial finite polyhedron

**Source:** 156-2, scan 011, sufficiency portion of the opening NB. **Kind:** own idea. **Quote:** “Il y a alors ... une structure de ficelle réduite”.

Let $X=|K|$ for a connected nontrivial finite simplicial complex, choose a spanning tree in its one-skeleton, and take two distinct leaf vertices $u,v$ of that tree. Removing either leaf leaves a connected spanning tree on the remaining vertices, and every punctured simplex joins its remaining vertices, so both $X\setminus\{u\}$ and $X\setminus\{v\}$ are connected; small closed truncated stars are cones on compact links with open interiors, giving regular immersion and nonisolated endpoints. Thus $(X,\{u,v\})$ is a reduced ficelle under the literal definition. **Confidence: high**, by this explicit construction; the stated scope is finite polyhedra, without importing a convention about arbitrary infinite triangulations.

**Context:** search: `compact|polyhedra|triangulable`; this **adds a proof of the finite-polyhedron sufficiency assertion** to the present package, while **MPL_151_032-075 Q4-02** (first-pass lead; 151/044–045, 059–061) and **MPL_150_001-043 Q4b** (first-pass lead; 150/037–039) concern different compact-tame comparison results and are not rederived.

### B53 — The reduced uniqueness exception is exactly the arc for finite polyhedra

**Source:** 156-2, scan 011, uniqueness portion of the opening NB. **Kind:** own idea. **Quote:** “Si $X$ est un segment cette str. est unique”.

For a connected finite polyhedron of dimension at least two, infinitely many interior points of a maximal simplex of dimension at least two are conical non-cut points, giving many possible pairs of reduced ends; for a finite graph with a cycle, the same holds for interior points of a cycle edge. A finite tree has precisely its leaves as non-cut points, so its unordered reduced endpoint pair is unique exactly when the tree has two leaves, equivalently when its realization is a closed interval. **Confidence: high**, by these elementary simplex and finite-graph checks; this proves the reduced uniqueness assertion in the finite-polyhedron setting and leaves the false classification of all nonreduced interval structures in B24–B25 separate.

**Context:** search: `compact|polyhedra|connexe`; no same uniqueness theorem appears in the supplied excerpts; this **adds a bounded positive proof** beside the compact-object comparison lead **MPL_151_032-075 Q4-02** (151/044–045, 059–061), without asserting that the existing register settled this endpoint problem.

