# SP33_CW_156-5 — Research notes

## Scope, method, and principal findings

These notes concern **156-5, scans 002–025, manuscript pages 1–24**, and were written only after the transcription was frozen at **2026-11-19 21:25:11 UTC**. The frozen readings are evidence; every suggested mathematical repair is confined to these notes and the proof appendix. The root reader alone read the scans, compared the witnesses, performed both visual passes, and interpreted the manuscript and context; an ancillary worker implemented finite-set computations from explicitly supplied abstract definitions without access to scans, witnesses, context, or the sweep’s code.

The strongest findings are: the connectedness assertion and C4 fail for every ground set with at least two points; a finite component classification extends the sweep’s numerical counterexamples; the displayed product must be separated from an enlarged product allowing empty choices; and the refinement and maximal-full-support subdivision theorems have direct proofs once literal slips are kept distinct from the mathematical statements. Additional qualifications concern support versus ambient points, strong versus ordinary irreducibility, finite Boolean generation, and the change of order convention needed for comparison with the STRATA register. These are this run’s deductions and checks, **not claims of novelty or external peer review**.

### Source keys and citation convention

| Key | Supplied source and coverage actually used |
|---|---|
| **M156/NNN** | The frozen file in `pages/` for scanNNN, named in that scan’s section below; also in `SP33_CW_156-5_transcription.tex`. These24 pages alone received visual checking here. |
| **E119/NN** | `SP33_CW_156-5_context/Esquisse_cote119_copy1_API_transcription.tex`, at its own `\\scanpage{119/NN}` marker. The supplied API transcription is explicitly unchecked by eye; §§5–6, scans 119/27–41, and notes6–7, scans 119/57–59, were read for the comparisons. Its formulas and historical claims are context leads, not newly verified ink. |
| **RS** | `SP33_CW_156-5_context/notes/RESULTS_STATE.md`, read before writing notes. An entry’s stated status is the earlier run’s claim unless specifically reviewed; many displayed statements are ellipsized, and their full source proofs are not in this packet. Each relevant id is named below; no register status is changed. |
| **Plan** | `SP33_CW_156-5_context/MPL_156-5/README.md`, especially S14 and B10. These are planning guesses, not established findings. |
| **S5** | `SP33_CW_156-5_sweep3/readings/156-5.md`, with its associated `156-5_CORRECTIONS.tsv`, `156-5_CHECK_EVENTS.tsv`, `156-5_DEPENDS.tsv`, and `156-5_INTEGRATION.md`. The reading, integration, and relevant cross-cote comparisons in `STUDY.md` were used after freeze. |
| **STUDY** | `SP33_CW_156-5_sweep3/STUDY.md`, especially §2.5 and its comparisons of156-4/5/6/7. Claims about other cotes and scans outside002–025 are background leads, not visual checks by this run. |
| **C01/C02/C03** | The respective `J156-5-01_notes.md`, `J156-5-02_notes.md`, and `J156-5-03_notes.md` under `SP33_CW_156-5_witnesses/codex/`; the item-by-item review appears below. |
| **P00–P13** | `SP33_CW_156-5_mathematical_checks.md`, the written proofs and counterexamples of this run; independent enumeration is documented by two scripts and their JSON outputs under `scripts/` and `records/`. |

**A material provenance qualification:** S5 explicitly says, “No scan image was viewed for this part.” Its correction rows and mathematical summaries were therefore treated as leads, not independent visual confirmation, despite the task’s general description of witnessS. The actual visual decisions and S-row outcomes are in the changes log. S’s scan 026 and 049 rows are out of this task’s scope and receive no ink verdict here.

For every numbered note, `records/context_searches.json` and `.tsv` record this run’s searches for the note’s objects, words, and register ids. The source keys above expand every shortened citation to its exact supplied file; an E119 citation includes its scan marker. “Adds”, “restates”, “differs”, and “contradicts” describe the relationship to those supplied materials, not a claim about all literature. No external literature search was performed; the historical and modern-theorem references inside RS remain attributed leads.

### Mathematical convention used only for checks

Write $F\subseteq\mathcal P(L)$, $|F|=\bigcup F$, and $A^\circ=A\setminus\bigcup_{B\in F,\,B\subsetneq A}B$. The checked model uses points of the support, strict proper lower members for boundaries, and weak inclusion in union/intersection and incidence formulas; admissible means every support point has a least member and every member has nonempty open stratum. The empty family is admissible, while a family containing the empty set is not; these conventions do not replace any frozen symbol (P00).

A subfigure is a down-closed subfamily, written $F\le G$; compatibility means both are subfigures of one figure, equivalently of their union. Refinement $F\ll G$ and subdivision $F\preccurlyeq G$ are different orders, and subdivision additionally requires equal support. The proof appendix gives details, so each note below stays within one to four sentences of mathematical discussion.

## Page-by-page notes


### Scan 002 — manuscript page 1

Source: `pages/J156-5-01_156-5_scan002.tex`.


#### N002-1 — reading question

**Place:** Proposition 1, conditions 1 and beta.

The literal condition “Pour tout $x\in L$” is stronger than the support condition used by the proof, and beta literally has $x\in\mathscr L$, not $x\in|\mathscr L|$. Taking $L=\{a,b\}$ and $F=\{\{a\}\}$ refutes equivalence with condition 1 as written; P00–P01 prove the theorem on the support, without changing either frozen expression.

**Context relation:** Differs from the normalized proposition in S5 §1 / SA21-R5-01; E119/27–30 gives the stratification programme but no such support lemma.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P00; P01; see `CHECK_EVENTS.tsv`.


#### N002-2 — reading question

**Place:** boundary display and alpha / delta-prime.

The frozen boundary has plain $B\subset A$, as does the union in alpha, and no extra strictness stroke or inequality was adopted from S. The boundary must exclude $B=A$, while alpha at $A=B$ and the marginal delta-prime require weak inclusion, so one global strict interpretation cannot serve every occurrence. The mathematical convention in P00 is explicit and is not an emendation of the ink.

**Context relation:** Contradicts the proposed strict ink reading of SA21-K5-04 while retaining its mathematical warning; E119/31–34 has no corresponding formula.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P00; see `CHECK_EVENTS.tsv`.


#### N002-3 — unpursued implication

**Place:** margin referring to GF VIII, page 37.

“variante ‘indexée’ formellement plus forte” is an explicit forward lead: an indexed family could distinguish coincident subsets, whereas the present family is a set of subsets. That distinction should be tested before identifying these figures with categories carrying automorphisms or repeated strata; the cited GF VIII page is outside the supplied scans and is not checked here.

**Context relation:** Adds a precise indexing warning to E119/37, where the stratum index set is replaced by an essentially finite category, and to E119/59 on internal categories.

**RESULTS_STATE ids:** STRATA B.1


### Scan 003 — manuscript page 2

Source: `pages/J156-5-01_156-5_scan003.tex`.


#### N003-1 — unproved claim

**Place:** proof, minimal member becomes least.

The step “A minimal” implies “un plus petit élément” is justified by alpha, which produces a member through the point inside every intersection. P01 checks this implication directly: minimality forces that member to equal $A$, so no unjustified uniqueness-of-minimal-element argument is needed.

**Context relation:** Restates, with the needed hypothesis exposed, S5 §1 / SA21-R5-01; no matching proof occurs in E119/27–41.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P01; see `CHECK_EVENTS.tsv`.


#### N003-2 — reading question

**Place:** last paragraph, 3 implies 1.

The proof begins “On suppose gamma et delta” but ends “Par eta”, so eta is used despite its omission in the opening list. This is harmless for the intended three-condition proposition, but the two-condition statement alone is false in the infinite case of N004-3.

**Context relation:** Differs from the silently completed hypothesis list in S5 §1; E119/34 likewise discusses provisional axioms, without settling this set-theoretic implication.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P01; P02; see `CHECK_EVENTS.tsv`.


#### N003-3 — unpursued implication

**Place:** proof together with scan 002 marginal delta-prime.

The marginal replacement of “delta, eta” by delta-prime really works on the support: a decomposition of every closed member into the strata below it, together with uniqueness of the stratum through a point, gives the least-member property. P01 supplies the missing separate proof and makes the weak inclusion in that decomposition explicit.

**Context relation:** Adds an explicit proof to the margin and restates the normalized alternative checked by S5 §1; E119/36 supplies a more geometric decomposition problem rather than this lemma.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P01; see `CHECK_EVENTS.tsv`.


### Scan 004 — manuscript page 3

Source: `pages/J156-5-01_156-5_scan004.tex`.


#### N004-1 — unproved claim

**Place:** Remark 1, artinian families.

“beta … automatique” for an artinian family follows by choosing a minimal member through a point; the descending-chain counterexample with nonempty intersection shows why the hypothesis matters. P02 also proves the stronger useful fact that gamma alone implies eta for an artinian family, explaining the failure of the finite draft below.

**Context relation:** Restates S5 §1 / SA21-R5-02 and SA21-R5-03 with a written proof; E119/39 emphasizes finiteness of stratifications but contains no artinian version.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P02; see `CHECK_EVENTS.tsv`.


#### N004-2 — withdrawn in the same text

**Place:** cancelled examples and slanted correction; both on scan 004.

“Exemple idiot” explicitly withdraws the drawn finite counterexample and points instead to “I infini”, GF VIII pages 44–45. The claim that eta is not redundant is not withdrawn, but these finite drawings cannot establish it; the cited later example remains outside this return.

**Context relation:** Restates the withdrawal recorded by SA21-K5-05 and S5 §1, now with the independently read deletion state; E119/34 offers only a general comparison with tentative axioms.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P02; see `CHECK_EVENTS.tsv`.


#### N004-3 — own idea

**Place:** test of the nonredundancy claim.

Our explicit test-family takes $A=\{p,a\}$, $B_n=\{p\}\cup\{b_m:m\ge n\}$, and includes $A$, $\{a\}$, all $B_n$, and all $\{b_n\}$. Its nonempty strata are singletons, so gamma and delta hold, while $A^\circ=\{p\}\subset B_0$ and $A\not\subset B_0$ refute eta. P02 gives the calculation; no identity with Grothendieck’s unavailable GF VIII example, and no novelty, is claimed.

**Context relation:** Adds a concrete infinite witness to the lead in S5 §1; E119/27–41 and RS do not provide this example.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P02; see `CHECK_EVENTS.tsv`.


**Own-idea confidence:** High: every boundary and stratum is calculated explicitly; the descending chain is visible.


#### N004-4 — self-flagged

**Place:** cancelled marginal bracket ending in two question marks.

The cancelled condition ending “si A∈… ⇒ A≠∅ ??” is an explicit authorial question separate from the withdrawal of the finite example. Its leading Greek letter is frozen as delta/eta and the connecting words remain uncertain, so no exact proposed implication is reconstructed from the context.

**Context relation:** Adds a separate item for the question already noticed by C01; E119/34 offers a general parallel in tentative axiom-making, not evidence for the missing condition.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


### Scan 005 — manuscript page 4

Source: `pages/J156-5-01_156-5_scan005.tex`.


#### N005-1 — unpursued implication

**Place:** surjection to an ordered set and topology.

“Se donner … une famille admissible … revient” to a poset $I$, support $S$, and surjection $S\to I$ is the exact reconstruction $A_i=p^{-1}(\downarrow i)$ proved in P03. Here downsets are **closed**, whereas STRATA 0.1 uses downset **opens**, so comparison with that register must replace $I$ by $I^{op}$. The manuscript gives the elementary data model, not a new proof of the register’s exit or coefficient theorems.

**Context relation:** Adds an explicit set-theoretic presentation to E119/36–37 and differs in orientation from RS STRATA 0.1 / WG2 B15 (§1.2).

**RESULTS_STATE ids:** STRATA 0.1; WG2 B15 (§1.2)


**Check:** P03; see `CHECK_EVENTS.tsv`.


#### N005-2 — reading question

**Place:** upper margin, preadmissible families.

The uncertain “un ens. fini|fin.” of additional closed subsets cannot be a general finiteness requirement. All singletons of $\mathbb N$ together with all initial segments $\{0,\ldots,n\}$ for $n\ge1$ form a preadmissible family with infinitely many members having empty stratum; P03 describes the additions as arbitrary nonprincipal downsets.

**Context relation:** Adds a counter-test to the margin, not treated in S5’s summary; E119/39’s finite filtration does not impose finiteness on this abstract definition.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P03; see `CHECK_EVENTS.tsv`.


#### N005-3 — reading question

**Place:** margin, “parties fermées irréd.”.

The unqualified identification of the members with “parties fermées irréd.” needs complete join-irreducibility, or a finite poset. For the chain $\mathbb N$ with closed downsets, the whole space is irreducible in the ordinary finite-union sense but has no greatest point, so it is not a principal closed set. Scan012’s “au sens fort” supplies the distinction required by P03.

**Context relation:** Qualifies the unqualified assertion in S5 §1 and connects the two manuscript margins; E119/36 has ordered indices but no irreducibility theorem.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P03; see `CHECK_EVENTS.tsv`.


#### N005-4 — unpursued implication

**Place:** preorder margin and faithful indexing.

The margin “un préordre sur S” separates point-level equivalence from order on the quotient: the quotient is an actual poset because distinct members are distinct subsets. This is a concrete positive model for the intake’s quotient-preorder question, but does not establish that an arbitrary partition into locally closed pieces has the same property.

**Context relation:** Adds a sufficient construction to RS INTAKE 20261114 §13.4 (cote 150 scan 003) and differs from the extra geometric structures of E119/36.

**RESULTS_STATE ids:** INTAKE 20261114 §13.4


**Check:** P03; see `CHECK_EVENTS.tsv`.


### Scan 006 — manuscript page 5

Source: `pages/J156-5-01_156-5_scan006.tex`.


#### N006-1 — unproved claim

**Place:** locally closed sets and condition (*).

The criterion “i≤j≤k, i,k∈J ⇒ j∈J” is precisely order convexity. P04 proves both directions without a finiteness assumption using $J=(\uparrow J)\cap(\downarrow J)$; this identifies locally closed saturated subsets in the topology of scan 005.

**Context relation:** Adds an elementary order-theoretic criterion to E119/39’s locally closed strata and to the question in RS INTAKE 20261114 §13.4.

**RESULTS_STATE ids:** INTAKE 20261114 §13.4


**Check:** P04; see `CHECK_EVENTS.tsv`.


#### N006-2 — unpursued implication

**Place:** Boolean algebra NB and inserted finiteness.

The insertion “si … fini” is essential to the claim that the generated Boolean algebra consists of all saturated subsets. For the singleton figure on $\mathbb N$, the ordinary Boolean algebra generated using finite operations is finite–cofinite, whereas every subset is saturated. P04 therefore checks the finite claim, not its unrestricted extension.

**Context relation:** Restates S5 §1’s finite qualification and differs from any reading that imports arbitrary unions into Boolean generation; E119/39 uses finite families in its geometric dévissage.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P04; see `CHECK_EVENTS.tsv`.


#### N006-3 — unpursued implication

**Place:** “modérées ou … constructibles”.

The words “modérées ou … constructibles” here name saturation relative to a finite figure, without choosing a geometric tame category. They provide a finite Boolean vocabulary for the programme, but do not prove triangulability, tubular existence, or comparison of tame theories.

**Context relation:** Adds a combinatorial special case to E119/31–35 and differs in scope from RS MPL_150_044-084 Q9 and the planning bridge WG2 B15 (§1.2).

**RESULTS_STATE ids:** MPL_150_044-084 Q9; WG2 B15 (§1.2)


### Scan 007 — manuscript page 6

Source: `pages/J156-5-01_156-5_scan007.tex`.


#### N007-1 — unproved claim

**Place:** definition of admissible subfamily.

The definition “qui est fermé dans” the family means down-closed for inclusion, not merely a subfamily which happens to be admissible. P05 verifies that all proper lower members, hence each boundary and open stratum, remain unchanged; this is the invariant used repeatedly in later union and refinement arguments.

**Context relation:** Restates S5 §1 / SA21-R5-05 and gives the set-level closed-part analogue of E119/28–30’s closed-pair decomposition.

**RESULTS_STATE ids:** STRATA D.2


**Check:** P05; see `CHECK_EVENTS.tsv`.


#### N007-2 — unproved claim

**Place:** proposition, induced equivalence relation.

The converse uses the induced equivalence classes and the inserted saturation of the smaller support. P05 checks that the support is already saturated because the smaller family consists of ambient members, so the insertion makes an available fact explicit rather than adding an independent hypothesis; the remaining argument forces every ambient lower member into the subfamily.

**Context relation:** Restates the complete criterion in S5 §1 and adds precision to the order/partition comparison relevant to RS INTAKE 20261114 §13.4; E119/36 supplies only the broader stratification setting.

**RESULTS_STATE ids:** INTAKE 20261114 §13.4


**Check:** P05; see `CHECK_EVENTS.tsv`.


### Scan 008 — manuscript page 7

Source: `pages/J156-5-01_156-5_scan008.tex`.


#### N008-1 — reading question

**Place:** first proof, “Psi adm.”.

The parenthesis “Psi adm.” is not the hypothesis that gives $B^\circ\ne\varnothing$, since $B$ is initially a member of the ambient family. The intended proof uses admissibility of that ambient family; P05 explains why equality of the induced strata then identifies the closed members, without replacing the frozen parenthesis.

**Context relation:** Qualifies the clean proof summary of S5 §1 / SA21-R5-05; E119/27–41 has no corresponding parenthesis.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P05; see `CHECK_EVENTS.tsv`.


#### N008-2 — unproved claim

**Place:** compatibility proposition, a / a-prime / b / c.

“deux sous-familles adm. d’une famille adm.” is equivalent to the union being admissible with both families closed in it; agreement on the common support is a stronger condition than merely agreeing on its partition. P05 checks the least-member gluing argument, and the stratum-by-stratum version added on scan 012 gives a local recognition test.

**Context relation:** Restates S5 §2 / SA21-R5-06 and adds a set-theoretic compatibility test to E119/28–30’s gluing language; it does not replace E’s attachment maps.

**RESULTS_STATE ids:** STRATA C.8


**Check:** P05; see `CHECK_EVENTS.tsv`.


#### N008-3 — self-flagged

**Place:** end of proposition proof.

“Reste à prouver b⇒c, c⇒a” marks temporary proof obligations, not a standing conjecture. The first begins immediately and the continuation runs through scans 009–010; P05 records the completed mathematical argument.

**Context relation:** Restates C01’s standing item and S5 §2, while E119/35’s still-unclear tubular uniqueness is a genuinely different unresolved issue.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P05; see `CHECK_EVENTS.tsv`.


### Scan 009 — manuscript page 8

Source: `pages/J156-5-01_156-5_scan009.tex`.


#### N009-1 — self-flagged

**Place:** remaining union condition, continued on scan 010.

“Il reste à prouver que si …” concerns the lower-member condition needed for the union, and the page ends mid-sentence at “les B en”. Its continuation supplies the missing cases on scan 010, so the break is physical pagination rather than abandonment of the proof.

**Context relation:** Restates C01’s standing item and S5 §2 / SA21-R5-06; the context E119/28–30 does not give this particular compatibility proof.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P05; see `CHECK_EVENTS.tsv`.


#### N009-2 — unpursued implication

**Place:** compatibility proof and overlap.

The proof’s common-lower-member condition shows exactly what set-level “recollement” remembers: the same subsets with the same least members on the overlap. It supplies no maps from links or normal fibres, so it cannot by itself furnish the coherent gluing data in the earlier geometric programme.

**Context relation:** Differs in retained data from E119/36 and 119/58–59; bears on the scope of RS STRATA C.8 and EXIT_ONE_TYPE P1d1, whose full statements are carried as background.

**RESULTS_STATE ids:** STRATA C.8; EXIT_ONE_TYPE P1d1


### Scan 010 — manuscript page 9

Source: `pages/J156-5-02_156-5_scan010.tex`.


#### N010-1 — unpursued implication

**Place:** warning after Corollary 1.

“cette dernière condition ne suffit nullement” is demonstrated already by $F=\{\{a\},\{a,b\}\}$ and $G=\{\{a\},\{b\}\}$: the support and partition coincide, but the union has an empty top stratum. P05 checks the warning and identifies order information as the missing datum.

**Context relation:** Restates S5 §2 / SA21-R5-07 and provides an elementary analogy to RS PATHS E.10’s warning that marked components alone do not determine mapping spaces; E119/36 retains more than stratum labels.

**RESULTS_STATE ids:** PATHS E.10


**Check:** P05; see `CHECK_EVENTS.tsv`.


#### N010-2 — unproved claim

**Place:** Corollary 2.

For compatible figures, “même support” does force equality because the common-support formula identifies exactly the common members. Compatibility cannot be dropped, as N010-1 shows; this conditional rigidity is the key input to the maximal-subdivision proof on scan 024.

**Context relation:** Restates S5 §2 / SA21-R5-06 and adds the explicit dependency used later; E119/28–30’s geometric supports alone have no comparable uniqueness claim.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P05; see `CHECK_EVENTS.tsv`.


#### N010-3 — own idea

**Place:** comparison prompted by the partition counterexample.

Use the pair in N010-1 as the first unit test for any proposed functor that sends a figure only to its stratum partition: it must distinguish the two incidence orders or explicitly declare that information forgotten. This is a test of data loss, not a counterexample to the fully coherent exit or normal-link results in RS.

**Context relation:** Adds a minimal finite test beside E119/58–59 and the warning in RS EXIT_ONE_TYPE P4e; it does not re-prove that geometric result.

**RESULTS_STATE ids:** EXIT_ONE_TYPE P4e; EXIT_ONE_TYPE P1a1


**Check:** P05; see `CHECK_EVENTS.tsv`.


**Own-idea confidence:** High for the test: the two families and their distinct orders are explicit; no geometric realization claim is made.


### Scan 011 — manuscript page 10

Source: `pages/J156-5-02_156-5_scan011.tex`.


#### N011-1 — unproved claim

**Place:** C1, bounded sups.

“admet des Sup majorés” is correct: inside a common upper figure the subfigures are downsets, and their arbitrary union is again a downset. P05 also proves that any pairwise compatible collection has its union as a figure, so the finite-sup detour is unnecessary in this concrete model.

**Context relation:** Restates S5 §2 and STUDY §2.5’s C1 in its set model; E119/31–32’s stability under geometric gluing is a separate, stronger ambition.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P05; see `CHECK_EVENTS.tsv`.


#### N011-2 — self-flagged

**Place:** cancelled draft and adjacent margin.

The cancelled “un peu vif|cf.” and “il faut passer|préciser par des Sup finis”, together with “explicitons|expliciter … Prop ou Cor”, qualify the exposition locally. They must be retained as tentative or drafting language even though P05 checks C1; C02’s blanket “None explicitly marked” needs this qualification.

**Context relation:** Adds the marginal drafting instruction to C02’s own caveat and differs from treating S5 §2’s clean theorem summary as the entire manuscript state; E119/34 is a comparison in method, not a proof source.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P05; see `CHECK_EVENTS.tsv`.


#### N011-3 — unpursued implication

**Place:** empty-family discussion in the cancellation.

“cas du Sup … vide” correctly singles out the empty family as the least figure. It must be distinguished from the family containing the empty set, which is inadmissible because that member has empty stratum; P00 and the computation both enforce this distinction.

**Context relation:** Restates the distinction explicitly used in S5 §§1–3 and STUDY’s axioms; E119/27–41 contains no competing empty-family convention.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P00; P05; see `CHECK_EVENTS.tsv`.


### Scan 012 — manuscript page 11

Source: `pages/J156-5-02_156-5_scan012.tex`.


#### N012-1 — unproved claim

**Place:** irreducibles “au sens fort”.

“un ens fermé est irréductible (au sens fort) sss il a un plus grand élément” is correct for complete join-irreducibility. P03 proves it by expressing a downset as the union of its principal downsets, and this qualification repairs the mathematical scope of scan 005’s shorter wording.

**Context relation:** Restates S5 §2 with the strong sense made explicit and qualifies its §1 summary; E119/36’s ordered index set does not settle the distinction.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P03; see `CHECK_EVENTS.tsv`.


#### N012-2 — reading question

**Place:** C2, final indexing phrase.

The principal subfigures displayed are $F_X$, but the trailing phrase literally says “pour Y∈…” rather than indexing them by $X$. P05 checks the evident decomposition over $X\in F$; the mismatch is recorded as a reading question and left in the frozen text.

**Context relation:** Differs from the normalized C2 in S5 §2 and adds a literal indexing caution to STUDY §2.5; E119/36’s Drap(I) is a different indexing construction.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P05; see `CHECK_EVENTS.tsv`.


#### N012-3 — unproved claim

**Place:** C3 and “Remords à prop. pge7”.

C3 and the “Remords” make compatibility testable on principal multistrates and their intersections. The proof in P05 uses the unchanged lower sets from each compatible pair, so it remains valid for infinite families; this is a positive local criterion despite the later failure of C4.

**Context relation:** Restates S5 §2 / SA21-R5-06 and distinguishes C1–C3 from STUDY §2.5’s extra component axiom; E119/36–37 motivates richer local data without this criterion.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P05; see `CHECK_EVENTS.tsv`.


### Scan 013 — manuscript page 12

Source: `pages/J156-5-02_156-5_scan013.tex`.


#### N013-1 — reading question

**Place:** proposed three-member multistrate display.

The extra braces in the frozen display are not silently flattened into a family of subsets. Even its natural well-typed interpretation $\{A,\{x\},A\cup\{x\}\}$ fails admissibility, since the two lower members cover the top; the proposed comparability bridge therefore fails independently of the brace ambiguity.

**Context relation:** Confirms the substantive counterexample of SA21-K5-01 / S5 §3 while differing from its cleaned display; E119/40–41 gives no justification for this bridge.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P07; see `CHECK_EVENTS.tsv`.


#### N013-2 — own idea

**Place:** component containing the one-member family {L}.

For every nonempty ground set, the multistrate $\{L\}$ is isolated: a nonempty lower figure equals it, and any upper figure would violate down-closure unless it also equals it. For $|L|\ge2$ it is incompatible with the distinct node $\{\{x\}\}$, so both connectedness and cross-component compatibility fail even for infinite $L$. P06 gives the complete argument.

**Context relation:** Strengthens S5 §3’s finite computation to a uniform obstruction; differs from E119/40–41’s contractible-choice requirement rather than solving it.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P06; see `CHECK_EVENTS.tsv`.


**Own-idea confidence:** High: down-closure at the member L leaves no possible additional member.


#### N013-3 — own idea

**Place:** finite component classification.

For finite $n\ge3$, P06 predicts and proves exactly $n+2$ components: $\{L\}$ alone, the two nodes $\{A\}$ and $\{A,L\}$ for each $(n-1)$-subset $A$, and one component of everything else. The valid bridge $\{A,\{x\},A\cup\{x,y\}\}$ uses a second outside point $y$ to keep the top stratum nonempty. Independent exhaustive enumeration verifies the exact partition through $n=4$, not merely its component count.

**Context relation:** Adds a finite classification to S5 §3 and a precise repair of the failed bridge; E119/40–41 contains no such component calculation.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P06; see `CHECK_EVENTS.tsv`.


**Own-idea confidence:** High for finite n: written proof plus independent exhaustive checks; no extension of the classification to arbitrary infinite families is claimed.


### Scan 014 — manuscript page 13

Source: `pages/J156-5-02_156-5_scan014.tex`.


#### N014-1 — unproved claim

**Place:** finite connectedness proposition.

“M est connexe” for finite figures is false as soon as $|L|\ge2$: there are three components on two points and five on three points. P06 and the independent enumeration refute this statement; the manuscript does not withdraw it within scans 002–025.

**Context relation:** Confirms SA21-K5-01 / SA21-R5-08 and contradicts the manuscript claim, without promoting S to a visual witness; E119/40–41 asks for an even stronger form of choice-independence.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P06; see `CHECK_EVENTS.tsv`.


#### N014-2 — unproved claim

**Place:** “l’axiome C4 … est automatique”.

C4 is false in this model, not merely unsupported by the connectedness argument. On two points the figures $\{\{a\},\{a,b\}\}$ and $\{\{b\},\{a,b\}\}$ lie in different components and have inadmissible union; P06 also gives the universal isolated-node counterexample.

**Context relation:** Confirms S5 §3 and STUDY §2.5’s stated obstruction to the fourth system; the later absence of a component axiom in the sweep’s account of 156-6 does not establish why it was dropped.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P06; see `CHECK_EVENTS.tsv`.


#### N014-3 — unpursued implication

**Place:** connectedness versus choice-independence.

Even a repaired connectedness theorem would control only components, whereas the “choix anodins” principle in the context asks for contractible spaces of choices and retains higher homotopy. Thus this page’s proposed connectedness argument cannot alone justify an invariant construction up to coherent choice.

**Context relation:** Differs in strength from E119/40–41 and bears on the scope of RS EXIT_ONE_TYPE P1d1 and MPL_150_044-084 N35.

**RESULTS_STATE ids:** EXIT_ONE_TYPE P1d1; MPL_150_044-084 N35


#### N014-4 — reading question

**Place:** empty and singleton ground sets.

The claim “M=∅, et M est connexe” uses a convention allowing the empty space to be connected, while the singleton case is explicitly “0-connexe”. The finite counterexamples begin at two points and do not depend on this convention; nonemptiness would still have to be specified for any space-of-choices application.

**Context relation:** Adds a convention warning to S5 §3 and differs from the nonempty contractible choice spaces envisaged in E119/40–41.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


### Scan 015 — manuscript page 14

Source: `pages/J156-5-02_156-5_scan015.tex`.


#### N015-1 — reading question

**Place:** literal ranges in the boxtimes formula.

With the literal ranges $A\in F$, $B\in G$, the extra condition “pas tous deux ∅” is redundant because admissible families contain no empty-set member. For singleton factors the displayed product is $\{\{a,b\}\}$ and is admissible, but contains neither factor as a subfigure, contrary to the later claim; P07 separates these two assertions.

**Context relation:** Qualifies S5 §3’s blanket assertion of inadmissibility, while retaining its refutation of the bounding argument; E119/28–30’s geometric gluing does not fix the displayed ranges.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P07; see `CHECK_EVENTS.tsv`.


#### N015-2 — unproved claim

**Place:** intended inclusion of the disjoint union of factors.

If empty choices are adjoined to both factors so that the product contains $F\amalg G$, every mixed member $A\cup B$ has the proper lower members $A$ and $B$ covering it. Its open stratum is then empty, so this enlarged construction cannot be the asserted multistrate or rescue connectedness.

**Context relation:** Confirms the intended-construction objection in SA21-K5-01 / S5 §3, with the extra interpretation stated rather than inserted into the transcription; E119/36 requires genuine additional geometric pieces.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P07; see `CHECK_EVENTS.tsv`.


#### N015-3 — unproved claim

**Place:** boundary and stratum identities.

The printed boundary identity already fails for the literal singleton-factor product, whose actual boundary is empty. The stratum identity fails for $F=\{\{a\},\{a,a'\}\}$ and $G=\{\{b\}\}$: the product’s top stratum is $\{a'\}$, not $\{a',b\}$. P07 refutes the identities separately from the ambiguity about empty choices.

**Context relation:** Adds a literal-range counterexample to S5 §3 and explains why its argument and the ink need separate formulations; no corresponding identity is supplied by E119/27–41.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P07; see `CHECK_EVENTS.tsv`.


### Scan 016 — manuscript page 15

Source: `pages/J156-5-02_156-5_scan016.tex`.


#### N016-1 — unproved claim

**Place:** supports and cosupports.

“les supports correspondent aux parties quelconques” is correct in the full set-theoretic figure model. P08 proves orthogonality by disjoint supports and uses point figures to identify the double orthogonal with all figures supported on the union, yielding exactly $\mathcal P(L)$.

**Context relation:** Restates S5 §4 / SA21-R5-09 and the concrete model in STUDY §2.5; E119/28–30 supplies a geometric closed/complement pair but no abstract support-lattice theorem.

**RESULTS_STATE ids:** BISITE F.9; STRATA D.2


**Check:** P08; see `CHECK_EVENTS.tsv`.


#### N016-2 — unpursued implication

**Place:** scope of the Boolean support lattice.

The computation of $\mathcal P(L)$ proves Booleanity for this model only. It cannot be transferred to every abstract biorthogonal-support system in the sweep, where STUDY records non-distributive examples from 156-7; those outside scans are background here, not newly checked examples.

**Context relation:** Differs in generality from STUDY’s abstract systems and prevents treating S5 §4 as a universal theorem; E119/31–34 explicitly allows a range of tame settings.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


#### N016-3 — unpursued implication

**Place:** comparison with support formalism in RS.

The set complement behind “cosupports” supplies the simplest closed/open separation, but no coefficient category or adjunction has been constructed. Therefore this is an illustration alongside the registered recollement formalism, not an independent proof of it.

**Context relation:** Adds an elementary model beside E119/38 and RS BISITE F.9 / STRATA D.2; the registered derivator claims are carried as background only.

**RESULTS_STATE ids:** BISITE F.9; STRATA D.2


### Scan 017 — manuscript page 16

Source: `pages/J156-5-02_156-5_scan017.tex`.


#### N017-1 — unpursued implication

**Place:** Stone compactification and isolated points.

The parenthesis “L se récupère … points isolés” is mathematically significant: $L$ is already recovered as the atoms of $\mathcal P(L)$, and these correspond to isolated principal ultrafilters in its Stone space. P08 checks the atom identification; it does not claim that a passage to Stone space irretrievably loses the original point set.

**Context relation:** Restates the parenthetical correction in S5 §4 and adds the direct atom description; E119/33–34 discusses category comparison, not this Stone reconstruction.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P08; see `CHECK_EVENTS.tsv`.


#### N017-2 — conjecture

**Place:** “Ceci suggère de refaire …”.

“Ceci suggère de refaire” the theory on a compact discontinuous space is a proposed change of setting, not a completed equivalence of theories. Under explicit zero-dimensional Hausdorff hypotheses and clopen supports, P08 derives regular open sets as the biorthogonally closed supports, using $U^*=\operatorname{int}(X\setminus U)$ and $U^{**}=\operatorname{int}\overline U$.

**Context relation:** Adds a topological variant to S5 §4 and differs from E119/31–34’s broader comparison of moderate theories; it does not settle RS MPL_150_044-084 Q9.

**RESULTS_STATE ids:** MPL_150_044-084 Q9


**Check:** P08; see `CHECK_EVENTS.tsv`.


#### N017-3 — reading question

**Place:** final regular-open formulas.

The frozen final line has `\overline U\unsure{\geq|=}\operatorname{int}(\overline U)`, while the intended fixed-point relation suggested by the orthogonality calculation is $U=\operatorname{int}\overline U$. The preceding formula for $V$ also repeats a symbol read as “f U”; P08 states the coherent complementary pair $V=X\setminus\overline U$, $U=X\setminus\overline V$ without substituting it into the ink.

**Context relation:** Differs from S5 §4’s clean regular-open summary; E119/31–34 offers no deciding reading for these rewritten formulas.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P08; see `CHECK_EVENTS.tsv`.


#### N017-4 — unproved claim

**Place:** NB, figures as closed compatible sets of multistrates.

The NB reconstructs a figure from all its principal multistrates as a down-closed, pairwise compatible subset of $M$. P05’s arbitrary-compatible-union argument proves the converse: form the union, and every principal multistrate of that union already lies in the original down-closed set. Thus this reconstruction survives the failure of connectedness.

**Context relation:** Adds an explicit proof to the NB and restates the set-model interpretation in S5 §§2–4; E119/58–59’s internal-category reconstruction still retains additional geometric data.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P05; P08; see `CHECK_EVENTS.tsv`.


### Scan 018 — manuscript page 17

Source: `pages/J156-5-03_156-5_scan018.tex`.


#### N018-1 — unproved claim

**Place:** stratum and principal-multistrate conditions.

“Toute condition portant sur la nature des strates … ou … multistrates” is stable under subfigures and compatible unions because the member and its entire lower subfamily remain unchanged. P09 checks this local stability statement; a condition on the whole collection, such as local finiteness, needs the separate qualification on scan 019.

**Context relation:** Restates S5 §4 and adds the mechanism underlying the assertion; E119/31–32’s desired stability axioms are more geometric than this set-level argument.

**RESULTS_STATE ids:** MPL_150_044-084 Q9


**Check:** P09; see `CHECK_EVENTS.tsv`.


#### N018-2 — unproved claim

**Place:** density margin.

For closed members, “A=closure(A°)” is equivalent to the stated incidence condition $A\subseteq B\Rightarrow A^\circ\subseteq\overline{B^\circ}$: one direction uses $A^\circ\subset A\subset B$, and the other sums the lower strata of $B$. P09 spells out where closedness is needed; the assertion is not taken as a theorem for arbitrary subsets of an arbitrary topological space.

**Context relation:** Adds a hypothesis-aware proof to S5 §4’s list; E119/36–39 discusses stratified structures with extra data, not this bare density test.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P09; see `CHECK_EVENTS.tsv`.


#### N018-3 — self-flagged

**Place:** cancelled diagonal NB.

The cancelled “peut-être” and “saurait-il” introduce a tentative relaxation involving “préadmissibles”, but intervening words remain uncertain. The precise proposed axiom cannot responsibly be reconstructed from the mathematics or the context; this is a retained self-flagged fragment, not a newly formulated conjecture.

**Context relation:** Restates C03’s caution; E119/34’s provisional axioms and RS MPL_150_044-084 Q9 are thematic parallels only, not evidence for missing words.

**RESULTS_STATE ids:** MPL_150_044-084 Q9


#### N018-4 — unpursued implication

**Place:** connectivity and sphere-boundary examples.

Conditions such as “i-connexe” or boundaries being “sphères topologiques” restrict individual pieces, but do not by themselves specify the linking maps or meridian injections needed for an ordinary exit category. These pages therefore do not overturn the register’s warning that aspherical strata alone are insufficient.

**Context relation:** Differs in data from E119/35–36 and 119/58–59; bears on RS STRATA F.3, EXIT_ONE_TYPE P1a1 / P1b1, and MPL_150_044-084 N39.

**RESULTS_STATE ids:** STRATA F.3; EXIT_ONE_TYPE P1a1; EXIT_ONE_TYPE P1b1; MPL_150_044-084 N39


### Scan 019 — manuscript page 18

Source: `pages/J156-5-03_156-5_scan019.tex`.


#### N019-1 — unproved claim

**Place:** local finiteness and finite sups.

“pas … généralement par sup quelconque” is witnessed by the singleton figures at $1/n$ in $\mathbb R$: each is locally finite, but their compatible union is not locally finite at zero. Finite unions of locally finite collections remain locally finite, so P09 verifies both sides of the distinction.

**Context relation:** Restates S5 §4’s qualification and supplies an explicit example; E119/39’s finite stratifying filtrations do not justify arbitrary unions.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P09; see `CHECK_EVENTS.tsv`.


#### N019-2 — reading question

**Place:** finite / finite-type sentence.

“de t. f. et ses strates sont finies” must refer to finiteness of the principal multistrates if it is to characterize a finite figure. Cardinality of the subsets themselves cannot be intended mathematically: the one-member family $\{L\}$ is finite even when $L$ is infinite. P09 checks the principal-subfamily interpretation and leaves the literal wording intact.

**Context relation:** Adds a terminology qualification to S5 §4; E119/36 uses geometric strata rather than the principal-family finiteness meant here.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P09; see `CHECK_EVENTS.tsv`.


#### N019-3 — own idea

**Place:** triangulated realization by closed “cells”.

For a finite poset $I$, take $X=|NI|$ and $X_i=|N(\downarrow i)|$; the maximal vertex with positive barycentric coordinate identifies the nonempty strata and gives the required admissible family. P10 proves the closed-downset correspondence directly and records the order reversal needed before comparing it with the register’s minimum-vertex convention.

**Context relation:** Adds a specific construction to this page and E119/36; RS STRATA A.4, STRATA A.12, and BISITE G.10 remain background for the stronger exit statements.

**RESULTS_STATE ids:** STRATA A.4; STRATA A.12; BISITE G.10; STRATA 0.1


**Check:** P10; see `CHECK_EVENTS.tsv`.


**Own-idea confidence:** High for finite posets: the simplicial construction is explicit; no unrestricted geometric or exit theorem is inferred.


#### N019-4 — reading question

**Place:** quotation marks around “cellules”.

The construction in N019-3 does not make every closed piece a regular closed ball: three incomparable points below a greatest point give a tripod. Thus the written “cellules” must not silently be strengthened to regular CW cells, and the sphere-boundary restrictions from scan 018 remain additional requirements.

**Context relation:** Differs in strength from a regular-cell reading, and separates this page from E119/35’s tubular questions and the registered realization comparisons.

**RESULTS_STATE ids:** BISITE G.10


**Check:** P10; see `CHECK_EVENTS.tsv`.


### Scan 020 — manuscript page 19

Source: `pages/J156-5-03_156-5_scan020.tex`.


#### N020-1 — self-flagged

**Place:** “Dans une terminologie qui sera développée”.

“qui sera développée” explicitly postpones the subdivision terminology, then the same page begins its definition through refinement. The common cell covering provides a finer figure on the relevant support, but the word does not yet assert a geometric subdivision theorem up to isotopy.

**Context relation:** Adds an explicit algebraic refinement notion to E119/33–34’s triangulation programme; RS MPL_150_044-084 Q2 and Q9 remain unsolved by this terminology.

**RESULTS_STATE ids:** MPL_150_044-084 Q2; MPL_150_044-084 Q9


**Check:** P11; P12; see `CHECK_EVENTS.tsv`.


#### N020-2 — unproved claim

**Place:** refinement proposition, least containers.

“un plus petit élément phi(A)” is a least container in the second figure; its existence is stronger than choosing a minimal container. Together with closed intersections it is equivalent to a monotone map on stratum quotients, as P11 proves on scans 020–023.

**Context relation:** Restates S5 §5 / SA21-R5-10 and gives a concrete underlying map for the order language of E119/36–37 and RS WG2 B15 (§1.2).

**RESULTS_STATE ids:** WG2 B15 (§1.2)


**Check:** P11; see `CHECK_EVENTS.tsv`.


#### N020-3 — unpursued implication

**Place:** relation to planning question S14.

These pages provide finite figures, refinement, and subdivision, which are ingredients for the proposed S14 system of finite cuttings. They do not define a form, network, cutting, or workshop, construct a pro-object, prove cofilteredness of all chosen cuttings, or prove recovery of a tame space from such a system. The planning guess is therefore supported only at the level of vocabulary and elementary models, not confirmed as a theorem.

**Context relation:** Adds ingredients to MPL_156-5/README.md’s S14 and differs from its reconstruction expectation; E119/36 and 119/58–59 explicitly retain attachment data.

**RESULTS_STATE ids:** WG2 B15 (§1.2); EXIT_ONE_TYPE P4e


### Scan 021 — manuscript page 20

Source: `pages/J156-5-03_156-5_scan021.tex`.


#### N021-1 — reading question

**Place:** top line, intersection condition.

The literal top line has “A∩F” where the continuation repeatedly uses $A\cap B$. P11 checks the latter well-typed formulation, which is also what S5 summarizes; the frozen transcription is not silently repaired.

**Context relation:** Differs from S5 §5’s normalized condition a; E119/36’s index diagrams do not decide this local symbol.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P11; see `CHECK_EVENTS.tsv`.


#### N021-2 — unproved claim

**Place:** a implies b and marginal lemma.

The marginal lemma “A°⊂B alors A⊂B” under b is the key to both directions. P11 proves it by decomposing $A$ into lower strata and using monotonicity of their assigned containers, then verifies that the resulting container is least.

**Context relation:** Restates S5 §5 / SA21-R5-10 with the logical dependency isolated; E119/36 gives no substitute for this proof.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P11; see `CHECK_EVENTS.tsv`.


#### N021-3 — unpursued implication

**Place:** NB, continuity of the support inclusion.

The NB correctly identifies the closed-intersection condition, together with support inclusion, with continuity for the two preorder topologies. P11 checks that continuity forces every $F$-stratum into a unique $G$-stratum and makes the induced quotient map increasing, so no independent least-container choice is needed.

**Context relation:** Adds a concrete continuity criterion beside RS STRATA 0.1 and WG2 B15 (§1.2), with the opposite open/closed convention recorded; E119/36’s geometric retractions require more structure.

**RESULTS_STATE ids:** STRATA 0.1; WG2 B15 (§1.2)


**Check:** P11; see `CHECK_EVENTS.tsv`.


### Scan 022 — manuscript page 21

Source: `pages/J156-5-03_156-5_scan022.tex`.


#### N022-1 — self-flagged

**Place:** “Reste : prouver C⊂B”.

The author marks “Reste : prouver C⊂B” and immediately reorganizes the argument as a corollary. This is a temporary gap in exposition, completed by the marginal lemma and the continuation on scan 023; P11 checks the noncircular proof order.

**Context relation:** Restates C03’s standing item and S5 §5 / SA21-R5-10; E119/35’s deferred tubular uniqueness is not resolved by this local completion.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P11; see `CHECK_EVENTS.tsv`.


#### N022-2 — unpursued implication

**Place:** marginal b-double-prime.

“la relation de préordre … plus fine” gives an economical characterization: the identity on the included supports preserves the two preorders. P11 proves equivalence with the stratum map, so the relation remembers incidence as well as the partition and avoids the failure illustrated on scan 010.

**Context relation:** Adds an elementary quotient-map criterion to E119/36 and RS INTAKE 20261114 §13.4; the register’s more general stratification question remains separate.

**RESULTS_STATE ids:** INTAKE 20261114 §13.4; STRATA 0.1


**Check:** P11; see `CHECK_EVENTS.tsv`.


#### N022-3 — reading question

**Place:** “relation d’ordre de |G|” in b-double-prime.

The support $|G|$ generally carries a preorder, not an antisymmetric order, because two points may lie in the same stratum. The frozen wording “relation d’ordre de |G|” is interpreted mathematically through the quotient poset of scan 005; antisymmetry on the support would be an extra requirement.

**Context relation:** Differs from a literal order-on-points reading and adds a qualification to S5 §5; E119/36’s ordered index set corresponds to the quotient, not the whole underlying point set.

**RESULTS_STATE ids:** INTAKE 20261114 §13.4


**Check:** P03; P11; see `CHECK_EVENTS.tsv`.


### Scan 023 — manuscript page 22

Source: `pages/J156-5-03_156-5_scan023.tex`.


#### N023-1 — self-flagged

**Place:** “Reste : prouver b-prime⇒b”.

“Reste : prouver b′⇒b” is completed with “qed.” on this sheet. The nonempty intersection of the assigned stratum with the comparison member gives the required order relation, and P11 checks the implication without treating the erased intermediate calculations as live premises.

**Context relation:** Restates C03’s standing item and S5 §5 / SA21-R5-10; E119/27–41 has no parallel proof that would change this completion.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P11; see `CHECK_EVENTS.tsv`.


#### N023-2 — unproved claim

**Place:** “C’est une relation d’ordre”.

Refinement is reflexive and transitive by preorder preservation; two opposite refinements force equal supports and equal preorders, which reconstruct equal admissible families by P03. P11 proves antisymmetry and the independent finite computation checks the relation laws on all admissible families through three points.

**Context relation:** Restates S5 §5’s order claim without extending the check to later scans; differs from E119/36–37’s category-valued indices, which carry more than a partial order.

**RESULTS_STATE ids:** STRATA B.1


**Check:** P11; see `CHECK_EVENTS.tsv`.


#### N023-3 — reading question

**Place:** subdivision proposition, minimal|maximal.

The frozen first reading is “minimal|maximal”, but the preceding clause says that there is no proper extension among refinements containing $F$ as a subfigure. P12 proves **maximality**, and literal minimality is false already for the empty refinement of a nonempty figure; the mathematical evidence is recorded here rather than used to alter the ink.

**Context relation:** Differs from S5 §5 / SA21-R5-11’s normalized maximal statement; E119/39’s finer filtrations do not settle the lettering.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P12; see `CHECK_EVENTS.tsv`.


#### N023-4 — unproved claim

**Place:** NB, testing refinement on multistrates.

“tt multistrate de F raffine G” is equivalent to refinement of $F$ because the least-container and closed-intersection conditions are local on principal lower subfamilies. This localization justifies the compatible-union proof on scan 024 and is checked in P11–P12.

**Context relation:** Restates S5 §5 and adds its precise role in the next proof; E119/36’s local retractions are an analogy, not the same localization theorem.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P11; P12; see `CHECK_EVENTS.tsv`.


### Scan 024 — manuscript page 23

Source: `pages/J156-5-03_156-5_scan024.tex`.


#### N024-1 — unproved claim

**Place:** full support implies maximality and converse.

The missing-point construction “H={{x}}” proves the converse: if the support is smaller, this disjoint one-point figure refines $G$ and can be adjoined properly. Full support forces any compatible extension refining $G$ to have the same support and hence be equal; P12 proves both directions and the computation checks all 54 target figures through three points.

**Context relation:** Restates S5 §5 / SA21-R5-11 with the scope of this run’s check specified; E119/39’s finite refinements suggest the application but do not prove this criterion.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P12; see `CHECK_EVENTS.tsv`.


#### N024-2 — reading question

**Place:** opening b implies a paragraph.

The first sentence literally calls $F'$ a “sous figure de F”, but its next support chain and last clause require $F$ to be a subfigure of $F'$. P12 checks the latter direction as needed for maximality and retains the contradictory wording in the transcription.

**Context relation:** Differs from S5 §5’s normalized proof; E119/27–41 provides no ink evidence for a replacement.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P12; see `CHECK_EVENTS.tsv`.


#### N024-3 — unproved claim

**Place:** compatible-union corollary and arbitrary-sup insertion.

Replacing the cancelled “disjointes” by live “compatibles” is substantive, and the insertion “Sup quelc.” is valid in this model. The union preserves each principal multistrate, hence each refinement condition; P12 checks arbitrary pairwise compatible unions, not merely the two-figure case.

**Context relation:** Restates the set-model result in S5 §5 and adds emphasis to the insertion; E119/31–32’s geometric gluing stability and RS STRATA C.8 are stronger background questions.

**RESULTS_STATE ids:** STRATA C.8


**Check:** P12; see `CHECK_EVENTS.tsv`.


#### N024-4 — unproved claim

**Place:** margin conditions c and d.

Under refinement, “Toute strate de G est réunion de strates de F” is equivalent to full support, with “strate” here meaning the closed members of the figure. Without a prior refinement hypothesis, adding least containers as in d recovers closed intersections because intersections of $F$-members are unions of $F$-members. P12 records these hypotheses rather than reading c as an unconditional criterion.

**Context relation:** Adds the omitted hypothesis accounting to S5 §5’s subdivision summary; E119/39’s common refinements are a contextual comparison, not a substitute proof.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P12; see `CHECK_EVENTS.tsv`.


#### N024-5 — reading question

**Place:** lower slanted comment after the corollary.

The margin calls the union assertion a “propriété formelle … intéressante”, but the following contrast and its reference to moderate constructions remain too uncertain for a precise mathematical proposition. Neither the sweep nor the context is used to complete that fragment; it remains a specific place for renewed ink review.

**Context relation:** Differs from treating the corollary’s clean statement as the whole marginal discussion; E119/31–34 and RS MPL_150_044-084 Q9 provide thematic words only.

**RESULTS_STATE ids:** MPL_150_044-084 Q9


### Scan 025 — manuscript page 24

Source: `pages/J156-5-03_156-5_scan025.tex`.


#### N025-1 — unproved claim

**Place:** commutative square of supports and quotient posets.

The square with surjective $p,q$ and increasing $\varphi$ exactly describes the refinement data when $S\subseteq T$ and $qi=\varphi p$. P13 reconstructs both figures as inverse images of principal downsets and checks the converse; $\varphi$ need not be surjective when the support inclusion is proper.

**Context relation:** Restates S5 §5’s description and adds the explicit reconstruction; E119/36–37’s diagrams retain geometric spaces and maps beyond this quotient square.

**RESULTS_STATE ids:** WG2 B15 (§1.2); STRATA 0.1


**Check:** P13; see `CHECK_EVENTS.tsv`.


#### N025-2 — reading question

**Place:** NB, “un couple F subset G”.

Raw family inclusion $F\subset G$ is not implied by the displayed square: $F=\{\{a\},\{b\}\}$ refines $G=\{\{a,b\}\}$ but is not its subfamily. Thus the square classifies general refinements, and the extra written inclusion needs clarification; P13 gives the counterexample without altering the symbol.

**Context relation:** Differs from an unrestricted literal equivalence in this NB and qualifies S5 §5’s summary; E119/39’s refinement of filtrations likewise does not require this raw inclusion.

**RESULTS_STATE ids:** None directly settles this item; no unrelated open problem is assigned.


**Check:** P13; see `CHECK_EVENTS.tsv`.


#### N025-3 — reading question

**Place:** inverse image of a “G-modérée” subset.

The inverse-image claim follows from $qi=\varphi p$ if “modérée” means saturated, and also under the finite-figure convention of scan 006. If instead it means the ordinary Boolean algebra generated by a possibly infinite figure, it can fail: singleton strata on $\mathbb N$ refine the even/odd two-piece figure, but the inverse image of the even piece is not finite–cofinite. P13 therefore checks the stated meaning explicitly rather than extending scan 006’s finite assertion.

**Context relation:** Adds a finiteness caveat to S5 §5 and links back to E119/39’s finite-family setting; RS MPL_150_044-084 N37 concerns coefficient classification, not this elementary Boolean issue.

**RESULTS_STATE ids:** MPL_150_044-084 N37


**Check:** P04; P13; see `CHECK_EVENTS.tsv`.


#### N025-4 — own idea

**Place:** unfinished final direct-image sentence.

The sentence “L’image … dir. d’une partie fermée” is unfinished, so no direct-image theorem is attributed to it. A useful continuation test is the discrete figure on $\{a,b\}$ refining $\{\{a\},\{a,b\}\}$: the source-closed subset $\{b\}$ is not target-closed. P13 checks this counterexample to any unconditional closed-image claim, without pretending that the truncated text makes that claim.

**Context relation:** Adds a test beside E119/28–30’s gluing maps and RS BISITE D.9 / STRATA D.5; it does not re-prove their distinct categorical-properness counterexamples.

**RESULTS_STATE ids:** BISITE D.9; STRATA D.5


**Check:** P13; see `CHECK_EVENTS.tsv`.


**Own-idea confidence:** High: both finite closed-set lattices are explicit; the intended continuation is unknown.


#### N025-5 — unpursued implication

**Place:** possible next comparison with direct-image results.

The support inclusion is only a continuous map of preorder spaces; it is not automatically a map satisfying the categorical properness hypotheses in the register. Any later geometric direct-image comparison should therefore check those hypotheses separately, and should distinguish the elementary square here from a realized map $|N\varphi|$.

**Context relation:** Differs in hypotheses from RS BISITE D.11, RESIDUE H.1 and H.7, carried as background; E119/35–36 and 119/58–59 also require geometric attachment structure.

**RESULTS_STATE ids:** BISITE D.11; RESIDUE H.1; RESIDUE H.7


## Standing question 1 — what the manuscript itself marks as unverified

Temporary “prove…” steps are recorded separately from lasting doubts. A transcription doubt is the reader’s uncertainty about ink, not automatically the author’s uncertainty about mathematics. In particular the false connectedness/C4 claims on scans 013–015 are asserted positively, not marked as doubts by the author in these 24 pages.

| Scan | His words or mark | State in the manuscript and disposition | Note |
|---|---|---|---|
| 003 | “Prouvons …”; “il faut prouver…” | Sequential obligations inside the proof of Proposition1; completed on this sheet, with the omitted opening reference to eta recorded separately. These are proof-stage markers, not open conjectures. | N003-1–3 |
| 004 | “??” after the cancelled condition involving $A\ne\varnothing$ | Explicit uncertainty in a cancelled marginal proposal; the leading Greek letter remains uncertain. No precise replacement proposition is invented. | N004-4; doubts table |
| 004 | “Exemple idiot”; “contre… correct (avec I infini)” | The finite draft is expressly withdrawn on the same page; a correct later example is claimed and referenced, but the cited GF VIII pages were not supplied for checking. | N004-2–3 |
| 007–008 | “Conditions équivalentes”; “prouvons l’inverse” | The subfamily converse is proved on 008; the wrong admissibility parenthesis is a reading question, not an authorial doubt. | N007-2; N008-1 |
| 008 | “Reste à prouver b⇒c, c⇒a” | Both are temporary proof obligations pursued immediately through 009–010. | N008-3 |
| 009 | “Il reste à prouver que si …” | The union condition continues across the physical page break and is completed on 010. | N009-1 |
| 011 | Cancelled “un peu vif|cf.”; “il faut passer|préciser par des Sup finis” | A real qualification of the drafting argument, even though cancelled; the exact uncertain words remain as frozen. | N011-2 |
| 011 | “explicitons|expliciter … Prop ou Cor” | A marginal request to expand the exposition, omitted from C02’s short standing list. | N011-2 |
| 017 | “Ceci suggère de refaire|faire théorie…” | An explicit unpursued change of setting to compact spaces and clopen pieces; not a completed equivalence. | N017-2–3 |
| 018 | Cancelled “peut-être”; “saurait-il”; “préadmissibles” | Tentative cancelled relaxation of an axiom; the exact condition is too uncertain to reconstruct. | N018-3 |
| 020 | “Dans une terminologie qui sera développée” | Terminology is deferred locally and developed through 025; no global realization theorem follows. | N020-1 |
| 021 | “Prouvons …”; marginal “Lemme” | Local least-container and stratum-inclusion obligations; checked and completed through 023. | N021-2 |
| 022 | “Reste : prouver C⊂B” | Isolated as a remaining step, then reorganized via the corollary and completed on 023. | N022-1 |
| 023 | “Reste : prouver b′⇒b”; “qed.” | The remaining direction is completed on the same sheet. | N023-1 |
| 024 | “propriété formelle … intéressante” | A suggested significance of the compatible-union result; the subsequent slanted fragment is too uncertain to formulate as a conjecture. | N024-5 |
| 025 | “L’image … dir. d’une partie fermée” | An unfinished sentence at the end of the supplied interval, not an asserted theorem with a question mark. It is a continuation lead and receives a separate test, not a false attribution. | N025-4 |

No additional live explicit conjecture formula such as “je conjecture” was found in this interval. Definitions and unproved assertions are nevertheless recorded in the page notes; being confidently asserted is not the same as having been checked.

### Review of every standing-question item in witnessC’s notes

| Witness item | Keep / correct / drop | Reason against the frozen transcription |
|---|---|---|
| C01:004 cancelled condition and two question marks | Keep | Both question marks and cancellation remain; the Greek letter and some words are still uncertain. |
| C01:004 “Exemple idiot”, second word uncertain | Correct | The consolidated reading resolves “idiot”; the withdrawal and GF VIII44–45 reference remain. |
| C01:008 “Reste à prouver b⇒c, c⇒a” | Keep, clarify | Temporary obligations, completed in the continuation, not unresolved at the end of025. |
| C01:009 “Il reste à prouver que si …” | Keep, clarify | Continued on 010, not an abandoned proof. |
| C01:no explicit reservation on 002,003,005,006,007 | Keep narrowly; supplement | No persistent hedge was found there; ordinary proof-stage “Prouvons…” on 003 and 007 are added above, and reading slips are not converted into authorial reservations. |
| C02:“None explicitly marked” | Correct / qualify | Its own following sentence records cancelled caution on 011; the marginal request to expand a proposition/corollary and 017’s proposed new setting must also be listed. |
| C02:011 “un peu [vif]” | Keep | Cancelled and still uncertain; the alternative remains in the transcription. |
| C02:011 “il faut [passer] par des Sup finis” | Keep, correct alternatives | Frozen reading is passer/préciser; this is a drafting qualification, not proof that arbitrary bounded sups fail. |
| C03:018 cancelled “peut-être”, “saurait-il” | Keep | Tentative nature survives; exact condition remains unresolved. |
| C03:022 “Reste : prouver C⊂B” | Keep, clarify | Completed through the marginal lemma/corollary argument, with the proof order checked in P11. |
| C03:023 “Reste : prouver b′⇒b”, ending “qed.” | Keep | The completion is on the same sheet. |

Additions to C are011’s drafting instruction,017’s “Ceci suggère…”,020’s explicit postponement of terminology, and the distinction between temporary proof obligations and 025’s unfinished sentence. Nothing in the mathematical context was used to manufacture a self-flag on 013–015.

## Standing question 2 — titles, dates, manuscript numbering, and page counts

There is **no separate title sheet or cover and no written total page count** in scans 002–025. Every supplied page is a manuscript note sheet, and the written folios run1–24; these are local page numbers, not a statement that the entire cote ends at24. The two written dates in this interval are **(14.6.86)** on 002 and **15 juin** on 018; the latter does not repeat a year. A prior overwritten/cancelled mark on 018 is transcribed as uncertain14/4, not silently made into another secure date.

| Scan | Manuscript page | Written title, date, or notable internal heading | Review of C’s corresponding item |
|---|---:|---|---|
| 002 | 1 | “GF V”; “Algèbre des figures”; “Sorite ensembliste.”; “(14.6.86)” | Keep; correct C01’s uncertainty on “Sorite”, now resolved. The GF VIII37 margin is a cross-reference, not a total. |
| 003 | 2 | “Dém” | Keep C01’s folio; add internal proof heading. |
| 004 | 3 | “Remarque|Remarques”; “Définition”; GF VIII44,45 reference | Keep C01’s folio and reference interpretation;44,45 are not page counts of this packet. |
| 005 | 4 | Cancelled “Proposition2”; live reconstruction discussion | Keep C01’s folio; cancelled heading is not a new title sheet. |
| 006 | 5 | NB on Boolean/constructible subsets | Keep C01’s folio; no date or total. |
| 007 | 6 | “Sous-famille (ou sous-ens) admissible”; “Prop.” | Keep C01’s title and folio, retaining abbreviated wording. |
| 008 | 7 | “Scholie”; “Proposition”; reference to manuscript pge/pg11 | Correct C01’s expanded “page 11” to the frozen abbreviation with its uncertainty;11 is an internal reference. |
| 009 | 8 | Continuation ending “les B en” | Keep C01’s folio and page-break observation. |
| 010 | 9 | “Corollaire1”; “Corollaire2” | Keep C02’s folio; add headings, not title sheets. |
| 011 | 10 | “figures ensemblistes”; C1; marginal Cor3 | Keep C02’s folio; record terminology and internal numbering. |
| 012 | 11 | “multistrates ensemblistes”; C2; C3; “Remords…” | Keep C02’s folio; add internal headings and labels. |
| 013 | 12 | “Composantes connexes de M=ens des multistrates.” | Keep C02’s heading and folio. |
| 014 | 13 | “Prop” on connectedness | Keep C02’s folio; mathematical falsity does not alter the heading. |
| 015 | 14 | NB on the repeated product construction | Keep C02’s folio; no written date here. |
| 016 | 15 | “Supports et cosupports.” | Keep C02’s heading and folio. The faint sideways watermark is inventoried separately, not a title. |
| 017 | 16 | Continuation on Stone compactification | Keep C02’s folio and absence of date/total. |
| 018 | 17 | Underlined “15 juin”; earlier cancelled uncertain14/4 | Keep C03’s date and folio; specify cancellation/uncertainty instead of inferring a new secure date. |
| 019 | 18 | “Figure finie”; finite-type definition | Keep C03’s folio; add internal terminology. |
| 020 | 19 | “Proposition” on refinement | Keep C03’s folio and heading. |
| 021 | 20 | Marginal “Lemme” | Keep C03’s folio and heading. |
| 022 | 21 | “Corollaire” at foot | Keep C03’s folio and heading. |
| 023 | 22 | “Définition”; “Ex”; “Proposition” | Keep all C03 items. |
| 024 | 23 | “Corollaire”; “Définition” of subdivision | Keep all C03 items. |
| 025 | 24 | “NB”; subdivision notation and square | Keep C03’s folio and absence of date/title sheet/total. |

C01’s “eight sheets numbered1–8”, C02’s sequence9–16, and C03’s sequence17–24 are all retained. Their assertions of no separate title sheet or stated page total are retained for their respective ranges. S5’s later **18 Juin** on scan 037 is outside this task and is not added to the list of dates visually checked here.

## What these pages change in the surrounding research programme

| Context item | Status supplied in context | Contribution of scans 002–025; limit |
|---|---|---|
| **Plan S14** | Unchecked planning guess in `MPL_156-5/README.md` | Finite figures, refinement and subdivision are explicit ingredients (006,019–025). There is no definition here of a form/network/cutting/workshop, no pro-object construction, and no reconstruction theorem from all finite cuttings. Later scans mentioned by the sweep cannot silently supply missing proofs in this interval. |
| **Plan B10** | Planning bridge, with compact tame/PL comparison cited as a guess/background | The triangulated finite-poset model of019–020 is compatible with a combinatorial approach. It proves neither tame homeomorphism versus PL homeomorphism nor an equivalence of geometric theories; E119/33–34 and 119/57–58 and RS MPL_150_001-043 Q4b / MPL_151_032-075 Q4-02–03 are leads only. |
| **WG2 B15 (§1.2)** | Unchecked planning item | 005 and 020–025 provide quotient-poset and monotone-map data, with the opposite open/closed convention. No localization-of-spaces theorem, and no real-line extension, is proved. |
| **STRATA 0.1; A.4; A.12; BISITE G.10** | Earlier run’s “Proved” claims | The finite closed-piece realization and variance dictionary are identified. Their exit-category and constructible-coefficient conclusions are not re-derived or upgraded from the abbreviated register rows. |
| **INTAKE 20261114 §13.4** | Intake lead, not referee verdict | 005–006 and 022 give an explicit admissible-family setting where the quotient is a poset and locally closed subsets are convex. This is a sufficient model, not a characterization of arbitrary geometric partitions. |
| **STRATA C.8; EXIT_ONE_TYPE P1a1 / P1d1 / P4e** | Earlier run’s claims | Compatibility and refinement describe set-level incidence; the manuscript here supplies no normal-link, attachment, or inertia data. E119/36 and 119/58–59 explicitly show what must be retained for geometric reconstruction. |
| **STRATA F.3; EXIT_ONE_TYPE P1b1; MPL_150_044-084 N39** | Refuted claim / proved claim / first-pass lead, respectively | Local connectivity and sphere conditions on 018 do not establish ordinary exits; the registered meridian/link hypotheses remain separate. |
| **BISITE F.9; STRATA D.2** | Earlier run’s “Known” claims | The support complement in016 is an elementary illustration of support separation; no coefficient-level recollement theorem is asserted or checked here. |
| **BISITE D.9 / D.11; STRATA D.5; RESIDUE H.1 / H.7** | Earlier run’s refuted/proved claims | The square on 025 is continuous at preorder level; the unfinished direct-image sentence is not a properness theorem. Properness and realization hypotheses must be tested separately. |
| **MPL_150_044-084 Q2 / Q9 / N35 / N37; MPL_121_049-073+153+155 R121-08** | Research-note leads | These comparisons distinguish realization from incidence and coefficient classification from recovery of geometry. Only the selected summaries are supplied; their underlying proofs and external sources are not newly certified. |
| **WG2 §3.1 #2** | Unchecked planning summary | These pages bear on the elementary poset and stratification side of the plan, not on every listed STRATA problem. |

The nine explicitly open register items—**LM4 C.12; RESIDUE E.6; EXIT_ONE_TYPE P3c-general; PATHS C.10; RESIDUE C.8; RESIDUE F.6; RESIDUE I.7; RESIDUE J.2; RESIDUE J.3**—are not settled by these pages. None has a directly applicable proof or counterexample here; the repeated words “finite”, “category”, or “stratum” do not establish a substantive solution. Their statuses are carried without change, with this scope statement recorded in the check ledger.

## Check results, reproducibility, and limits

`CHECK_EVENTS.tsv` is an event ledger, not a claim that visual transcription constituted a mathematical check. Written proofs and counterexamples are in `SP33_CW_156-5_mathematical_checks.md`; actual computation times, script hashes, complete finite catalogues and relations are in `records/finite_figures_check.json` and `records/finite_figures_n4_components.json`. The finite tests use no source text or image recognition and do not replace the unrestricted proofs.

| Test | Actual scope and result |
|---|---|
| Family enumeration | All4,16,256 families on 1,2,3 points; respectively2,7,45 are admissible including the empty family. The focused4-point run examines all 65,536 families and finds500 admissible families. |
| Multistrate components | For1,2,3,4 points:1,5,28,231 multistrates and 1,3,5,6 components; component sizes are1;2,2,1;21,2,2,2,1;222,2,2,2,2,1. The4-point run checks the exact predicted partition in P06. |
| Cross-component compatibility | On2 and 3 points,14 of16 and 324 of330 ordered cross-component pairs are incompatible. No4-point compatibility-pair enumeration is claimed. |
| Refinement criteria | The two principal formulations agree on all 4+49+2025 admissible ordered pairs for1–3 points; there are respectively3,26,549 true pairs. |
| Relation laws | Reflexivity, antisymmetry and transitivity hold in the finite tests;4,70,3601 composable refinement chains are checked, in addition to the written proof. |
| Subdivision maximality | Full support equals maximality under the subfigure order for all 54 target figures on 1–3 points, with the proof in P12. |

The sweep’s SA21-R5-12 through SA21-R5-16 concern later scans and are not relabelled as checks by this run. Even where this run agrees with an earlier check, its own event records the actual proof or computation performed. The transcription hashes are verified separately at completion; all remaining ink uncertainties, including surprising or mathematically false literal readings, remain in the frozen files.
