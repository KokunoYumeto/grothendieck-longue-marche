# MPL_131 — Research notes

**Archive:** Montpellier, cote 131, file `131.pdf`; 38 retained scans, 002–042 excluding 011, 019, and 022. **Research date:** 16 November 2026. **Transcription freeze:** 15:28:08 UTC; **context contents opened:** 15:28:13 UTC. The frozen page fragments and aggregate are the documentary witness for these notes; proposed mathematical reconstructions below do not alter them.

## Scope and how to read the notes

There are **90 individually located notes** below. Each has one of the requested kinds, a brief textual cue, one to four substantive sentences, an actual search of both supplied context documents, and an explicit statement of the relation to the relevant prior entry. Line references are **lines in the frozen per-page TeX file**, not invented line counts for the image; the accompanying physical description identifies the part of the scanned page. A word quoted without a doubt marker is taken from an unmarked portion of the frozen reading, while alternatives and uncertain text are identified as such. The complete uncertainty record remains `MPL_131_doubts.md`.

The supplied context contains only `README.md` and `notes/RESULTS_STATE.md`. The result CSVs, intake reports, earlier-package notes, war-game documents, and Hua findings register named there are **not supplied and were not inspected**. A context citation to one of those filenames is a citation to its **excerpt in RESULTS_STATE**, with the available scan metadata, not a claim to have read the original. Its “Proved,” “Refuted,” “Known,” and “Open” labels ordinarily remain previous AI-run claims; specifically reported referee reviews retain their stated limitations. None of the directly relevant cote-131 entries is treated as an independently established theorem.

The context search ledger, `records/context_searches.json`, records the exact terms, searched-file hashes, and matching file/line coordinates for every note. The full coverage ledger, `records/context_register_coverage.md`, accounts for all **48 primary context entries**, the four run summaries, and visible secondary IDs, including negative matches. No original source text from the supplied archives is duplicated as a separate source file in this deliverable.

## Principal results of the comparison

| Finding | Evidence and qualification | Notes |
|---|---|---|
| A close published comparison exists | Murre’s unramified and étale results and SGA 3’s auxiliary criteria provide concrete comparators; the complete locally quasi-finite variant is only announced in the inspected Murre passage, so the exact general draft is not certified wholesale | RN002–RN003, RN011, RN051, RN068 |
| A compressed lifting hypothesis needs attention | The earlier schematic-density insertion matters; an embedded-nilpotent example tests the later wording under ordinary topological irreducibility | RN019–RN020 |
| Uniqueness and existence must remain distinct | The revised comparison lemma uses two injections for an existing candidate, whereas constructing universal sections of the finite local models requires effectivity | RN046–RN054 |
| Globalization is not a purely formal last line | Constructibility, representability of the relation, finite-presentation control, shrinking, and actual open-chart coverage each have a role | RN012–RN014, RN057–RN069 |
| Announced applications have precise published scopes | Hom, Picard, universal flattening, component, and projectivity comparisons are stated with their hypotheses and representability categories | RN030–RN042 |
| The preliminary subject guesses need pruning | Descent and representability are central; heights, local symbols, and étale cohomology are not demonstrated handwritten themes, and reused algebra leaves do not prove such a link | RN001, RN071–RN085 |

These findings are a research audit of the draft and its context, **not a complete proof of the general criterion, an independent decipherment of the handwriting, or a novelty judgment**. The conditional embedded-prime check is set out explicitly so that the precise interpretation on which it depends can be assessed.

### Citation convention

Manuscript citations are the file/scan/line locations attached to each note (Grothendieck, n.d.). Published comparisons use author–date citations and exact theorem, exposition, or Stacks tag; full APA-style references and checked URLs are at the end. Stable Stacks tags are the primary locators because section numbering can change. The consulted SGA 3 text is a French retypesetting, and Raynaud’s original XI.1.4 is listed only as an indirectly identified dependency.

## 1. The criterion, its revisions, and the supplied findings

### RN001 — Planning placement: construction techniques confirmed

**Kind:** unpursued implication

**Location:** **131.pdf, scan 002**, first condition list; frozen page-file line 13; **131.pdf, scan 017**, application heading; frozen page-file line 25; **131.pdf, scan 033**, local-to-global proposition; frozen page-file line 11.

**Text:** “Pour que $F$ soit représentable”; “Applications en vue.”

The retained manuscript supports the README placement in Book I I.VI: it develops representability, completion descent, local-to-global construction, and Hom/Picard applications. The additional planning labels heights, local symbols, and étale cohomology are not demonstrated themes of the handwritten argument; the word étale concerns morphisms and functors, while the lattice and tensor passages occur on reused typed leaves. For S19, the useful residue is a comparative account of the actual axioms, deferred reductions, and printed counterparts, rather than a claim that this packet solves one of the arithmetic questions selected by broad keywords.

**Context search:** `RN001`; `S19`, `construction`, `descent`, `heights`, `local symbols`, `étale cohomology`, `Hom`.

**Context comparison:** `README.md`, Book I I.VI, rank 22 and **S19**, citing cote 131 scans 002–042; `notes/RESULTS_STATE.md` → **MPL_33_002-049 §2**, source `MPL_33_002-049_notes.md` (scan field truncated after “002…”, original unavailable); `notes/RESULTS_STATE.md` → **WG H9**, source `WARGAME_MATH_HUNCHES_20261112.md` (cote 44, Th. 4–5; no scan supplied; unchecked height/lattice hunch, original unavailable); **confirms the construction/descent/Hom placement; gives no supporting evidence for the height, local-symbol, or cohomological placement**.

### RN002 — Direct printed comparator for the main finding

**Kind:** unproved claim

**Location:** **131.pdf, scan 014**, theorem; frozen page-file line 4; **131.pdf, scan 004**, dimension induction; frozen page-file line 4.

**Text:** “localement quasi fini” and “séparé”; “Pour prouver la représentabilité”.

The draft gives a theorem-shaped criterion and a proof programme, with essential local and generic modularity clauses that the truncated Hua head does not expose in full. Murre (1966, Exposé 294, Theorem 1 and Corollary 2) publishes the unramified and étale criteria; its note on p. 247 announces a locally quasi-finite analogue without stating that full criterion. This is a direct literature match to investigate, but neither that announcement nor Hua’s unsuccessful reference search certifies the precise revised general statement or its novelty. A complete comparison should retain each version’s test category, finiteness, effectivity, separation, and modularity assumptions.

**Context search:** `RN002`; `131-locally`, `quasi-finite`, `representability`, `pro-represent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds the actual proof architecture and a verified printed comparator; qualifies the no-reference/candidate status without declaring the general draft settled**.

### RN003 — The two corollaries do not retain the same numbered conditions

**Kind:** withdrawn in the same text

**Location:** **131.pdf, scan 016**, first corollary and deletion; frozen page-file line 6; **131.pdf, scan 016**, second corollary and insertion; frozen page-file line 12; **131.pdf, scan 014**, main theorem condition 5; frozen page-file line 15.

**Text:** Deleted “1°) à 6°)”; inserted “1° 2° 3° 4° 6°”; “ainsi que 8°”.

On scan 016 the étale corollary removes condition 5 from its displayed list, whereas the unramified corollary keeps conditions 1–6, explicitly adds 8, and replaces 7 by (NR). Consequently a common summary “conditions 1–6 plus unramifiedness” loses a substantive insertion and the difference between the two results. The surviving margin requests also remain tasks in this document, regardless of the Hua register’s truncated literature verdict.

**Context search:** `RN003`; `131-unramified`, `conditions`, `étale`, `Nothing remains`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **corrects the scope of the shortened corollary summary by reporting the visible withdrawal and insertion, rather than contradicting an unavailable full Hua statement**.

### RN004 — A context-suggested reading of the topology abbreviation

**Kind:** reading question

**Location:** **131.pdf, scan 002**, condition 1; frozen page-file line 13; **131.pdf, scan 014**, condition 2; frozen page-file line 10.

**Text:** Frozen reading: “fppc|fpqc”.

The supplied Hua head describes fpqc descent, and the later manuscript explicitly speaks of faithfully flat quasi-compact descent, so fpqc is the contextually supported alternative to the first frozen reading. That evidence concerns intended mathematics, not the exact strokes of the abbreviation, and therefore does not resolve or change the frozen transcription. The same distinction matters when comparing an fppf theorem with the completion map, which need not be locally of finite presentation.

**Context search:** `RN004`; `fpqc`, `faithfully`, `completion`, `descent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **suggests the second already-recorded reading; adds a terminology question while preserving the page file and its first reading**.

### RN005 — Artinian exactness and the length-one insertion

**Kind:** unpursued implication

**Location:** **131.pdf, scan 002**, condition 4 and its insertions; frozen page-file line 25; **131.pdf, scan 012**, cancelled Artinian replacement; frozen page-file line 41.

**Text:** “ext. résiduelle triviale”; “$\operatorname{long}_A A'/A=1$”.

The insertion restricts an exactness test to a local Artinian situation with trivial residual extension and a length-one quotient, while scan 012 experiments with a stronger-looking bijectivity replacement and cancels it. A proof of equivalence with universal prorepresentability must explain how these elementary tests generate the required finite Artinian descent diagrams; it cannot simply identify the displayed equalizer with every pullback axiom of deformation theory. Schlessinger’s Theorem 2.11 distinguishes a hull from prorepresentability in a fixed-residue-field category, so it supplies a useful comparison but not an automatic replacement of this broader test category (Schlessinger, 1968).

**Context search:** `RN005`; `artin`, `pro-represent`, `exact`, `length`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the exact restricted test and its cancelled variant, which the broad prorepresentability head does not specify**.

### RN006 — Finite prorepresenting rings carry the zero-dimensional requirement

**Kind:** unpursued implication

**Location:** **131.pdf, scan 002**, condition 5; frozen page-file line 42; **131.pdf, scan 014**, revised Artinian-base condition; frozen page-file line 15.

**Text:** “l’anneau $B$ … est fini sur $K$”; “finis … $A$”.

The first list requires finiteness over an algebraically closed field at a point, while the later list phrases finiteness over Artinian base rings; translating between them is part of the proof, not merely a renumbering. Finiteness of the tangent space alone would allow a formal ring such as $k[[t]]$, whereas the manuscript asks for a finite-dimensional local algebra over a field. Thus a comparison with a hull or formal moduli criterion must retain this stronger geometric restriction and explain its propagation to the finite models over a complete local base.

**Context search:** `RN006`; `Artinian`, `finite`, `prorepresent`, `quasi-finite`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **sharpens the finiteness clause and distinguishes it from a tangent-space or hull criterion; no same-point settled row is supplied**.

### RN007 — Base-change stability and the meaning of absolute conditions

**Kind:** unproved claim

**Location:** **131.pdf, scan 004**, opening paragraph; frozen page-file line 2.

**Text:** “les conditions $1^\circ$ à $8^\circ$ sont stables par tte extension de la base”.

The assertion is used before the dimension induction, but the page does not check it separately for the revised complete-local and finite-residue-field tests. A faithful reconstruction must distinguish stability under changing the base scheme from the stronger claim that a condition is absolute on the underlying functor, and must use the numbering of scan 002 when interpreting the exceptions 2, 5, and 6. The later reordered list on scan 014 cannot be substituted into this sentence without a concordance.

**Context search:** `RN007`; `base change`, `conditions`, `quasi-finite`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a proof obligation and a numbering constraint absent from the abbreviated finding**.

### RN008 — The zero-dimensional case is referred to, not proved on the first sheet

**Kind:** unproved claim

**Location:** **131.pdf, scan 004**, case 1; frozen page-file line 6; **131.pdf, scan 029**, Artinian-base corollary; frozen page-file line 11.

**Text:** “cor $2$ à prop. $1$”; “On n’a eu besoin que de $1^\circ$ à $5^\circ$”.

The opening proof invokes a later auxiliary corollary to assemble a scheme over an Artinian base from the local prorepresenting algebras. Scans 029–031 supply the intended continuation, so this is an internal deferred proof rather than a claim whose justification is absent from the packet altogether. Once the prorepresenting rings have been shown Artinian as that corollary assumes, they themselves lie in the test category and their universal elements are already available; the distinct effectivity question for finite models over a positive-dimensional complete local base is discussed in RN053–RN054.

**Context search:** `RN008`; `artinian`, `representability`, `effectivity`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the packet-internal cross-reference and isolates the remaining effectivity check**.

### RN009 — Why the complete one-dimensional case can avoid condition 8

**Kind:** unproved claim

**Location:** **131.pdf, scan 004**, margin to case 2; frozen page-file line 9; **131.pdf, scan 005**, continuation of induction; frozen page-file line 2.

**Text:** “Si $\dim S=1$ … l’hypothèse $8^\circ$ est inutile”.

The claim is plausible within the displayed induction because the punctured spectrum of a one-dimensional local Noetherian scheme has dimension zero, leaving the special-to-generic extension controlled by the local condition. It does not say that condition 8 is dispensable in the subsequent arbitrary-base globalization, where constructibility or a generic-neighbourhood statement reappears. A reconstructed proof should separate these two uses of dimension one rather than treat the marginal sentence as a global redundancy theorem.

**Context search:** `RN009`; `dimension`, `quasi-finite`, `generic`, `condition`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the restricted inductive role of the claim; does not remove a hypothesis from the general finding**.

### RN010 — A lemma is explicitly requested at the modularity transition

**Kind:** self-flagged

**Location:** **131.pdf, scan 005**, top margin; frozen page-file line 3; **131.pdf, scan 014**, condition 7 bracket; frozen page-file line 19.

**Text:** “Dégager un lemme à cet effet”; “on verra que cel implique: pro-modulaire”.

The draft moves between modularity, promodularity, and being étale, and explicitly requests a lemma at the passage from a special-fibre model to the local condition. The first proof temporarily uses a revised version of 7, while the later theorem promises a comparison with promodularity; these are two obligations to be matched against the definition on scans 035–037. The margin should remain an author-marked unfinished step even if a modern formal criterion supplies part of the intended argument.

**Context search:** `RN010`; `modular`, `pro-represent`, `quasi-finite`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **MPL_33_098-146 §65**, source `MPL_33_098-146_notes.md` (no scan supplied; methodological first-pass lead, original unavailable); **adds an explicit author flag and a later internal comparison; no matching proof is contained in the supplied register excerpt**.

### RN011 — Completion descent needs an effective descent theorem for this class

**Kind:** unproved claim

**Location:** **131.pdf, scan 005**, case 3; frozen page-file line 6.

**Text:** “la donnée de descente … est effective”.

The argument needs representability to descend from the completed local base, not just the assertion that sections of $F$ satisfy a sheaf equalizer. Murre (1966, Exposé 294, Proposition 1) gives the relevant fpqc descent statement for separated locally quasi-finite schemes with locally Noetherian bases. In a modern verification, Stacks Tags 0AP9 and 0APK also supply a route through ind-quasi-affine morphisms, whereas Tag 02W8 alone states an fppf result and does not cover an arbitrary completion map. These are scoped justifications of this step, not a proof of every other condition in the manuscript.

**Context search:** `RN011`; `descent`, `completion`, `quasi-finite`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a precise effectivity reference and the fpqc/fppf scope distinction**.

### RN012 — The short local-to-global lemma has a constructibility dependency

**Kind:** unproved claim

**Location:** **131.pdf, scan 005**, last lemma; frozen page-file line 12; **131.pdf, scan 006**, sole paragraph; frozen page-file line 2; **131.pdf, scan 033**, expanded auxiliary proposition; frozen page-file line 11.

**Text:** “Alors $F$ est représentable”; “vérifier la condition de constructibilité”.

Read in isolation, the lemma on scan 005 appears to deduce global representability solely from representation over every local scheme. Its next sheet and the cited Proposition 3 make the extra work visible: constructibility of the locally modular locus, together with locality and filtered-limit compatibility, is used to spread and glue charts. The statement therefore must be read with “$F$ comme dessus” and the later hypotheses, not as an unrestricted local-base descent principle.

**Context search:** `RN012`; `representability`, `local`, `constructib`, `S19`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `README.md`, Book I I.VI, rank 22 and **S19**, citing cote 131 scans 002–042; `notes/RESULTS_STATE.md` → **MPL_33_002-049 §2**, source `MPL_33_002-049_notes.md` (scan field truncated after “002…”, original unavailable); **adds the omitted-in-summary constructibility dependency and resolves the internal cross-reference**.

## 2. Local and generic openness, lifting tests, and author-marked questions

### RN013 — The square-zero closed-immersion reduction is a substantive lemma

**Kind:** unproved claim

**Location:** **131.pdf, scan 009**, framed marginal lemma; frozen page-file line 20.

**Text:** “On peut supposer en A resp. B … imm. fermée”; “idéal de carré nul”.

The boxed reduction would turn the finite-model or local-modularity problem into a test on closed immersions and then square-zero thickenings. A proof must show that the necessary base changes and successive nilpotent reductions preserve the hypotheses and the conclusion under descent; the box itself supplies neither argument. The general formal étale characterization for an existing finitely presented morphism does not by itself prove this reduction for an arbitrary functor (Stacks Project Authors, 2026, Tag 02HM).

**Context search:** `RN013`; `unramified`, `artin`, `descent`, `nilpotent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the exact reduction to be proved rather than treating it as an already-established consequence of the corollary**.

### RN014 — Generization and generic neighbourhoods are separate inputs

**Kind:** unpursued implication

**Location:** **131.pdf, scan 009**, conditions C1 and C2; frozen page-file line 27; **131.pdf, scan 037**, proof of Proposition 3; frozen page-file line 14.

**Text:** “stable par générisation”; “$U\cap\bar x$ est un voisinage”.

The two clauses separate extension from special to generic points from neighbourhood control inside point closures. For Noetherian sober spaces, constructibility plus stability under generization implies openness, and a criterion in terms of nonempty open subsets of irreducible closed subsets gives the related topological mechanism (Stacks Project Authors, 2026, Tags 0542 and 053X). This explains the structure of the later proof but does not establish constructibility for the manuscript’s functor-defined locus; that is precisely the remaining geometric input.

**Context search:** `RN014`; `generic`, `representability`, `étale`, `constructib`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds a verified topological comparator and distinguishes it from the unsupplied geometric constructibility argument**.

### RN015 — The étale lifting condition is called automatic

**Kind:** unproved claim

**Location:** **131.pdf, scan 007**, NB after 7; frozen page-file line 7; **131.pdf, scan 009**, last NB; frozen page-file line 32; **131.pdf, scan 012**, margin to condition 9; frozen page-file line 32.

**Text:** “Cette condition est vide”; “automatique si $F\longrightarrow S$ est étale”.

These three remarks concern lifting across nilpotent thickenings or the associated generization condition. For a formally étale functor the unique lifting property supplies the intended local mechanism, but the precise category of tests still matters when the draft assumes étaleness only on Artinian arguments. Once a representing morphism is known and is locally of finite presentation, formal étaleness becomes étaleness by Stacks Tag 02HM; this does not independently construct the representing object.

**Context search:** `RN015`; `étale`, `Artinian`, `unramified`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds the repeated internal assertions and the distinction between formal lifting and existence**.

### RN016 — Replacing A and B by openness of the infinitesimal étale locus

**Kind:** unproved claim

**Location:** **131.pdf, scan 007**, general-case reformulation; frozen page-file line 18.

**Text:** “pas néc. non ram.”; “l’ens des pts … infᵗ étale est ouvert”.

The text explicitly returns to the general case and proposes an openness condition as a substitute for A and B. For a scheme morphism locally of finite presentation the formal étale and étale conditions agree, making the analogue natural, but before representability this pointwise locus needs a functorial definition and a proof that it yields the required charts. The cancelled diagonal qualifications below it show that the author was still adjusting the exact range of the condition.

**Context search:** `RN016`; `étale`, `quasi-finite`, `conditions`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds an alternate formulation and its unresolved range; the provided finding does not settle its equivalence**.

### RN017 — The cancelled diagonal discussion is later resumed

**Kind:** withdrawn in the same text

**Location:** **131.pdf, scan 007**, cancelled lower block; frozen page-file line 20; **131.pdf, scan 020**, live diagonal argument; frozen page-file line 2.

**Text:** Cancelled “Conditions analogues”; later “coïncide formellement avec la diagonale”.

The lower discussion on scan 007 cancels a proposed diagonal/base-change formulation rather than establishing it as a live hypothesis. Scan 020 resumes a related argument by representing the diagonal, using separation to make it closed, and comparing the formal self-fibre product with the actual diagonal. These passages document a revised proof route; the poor lower handwriting on scan 007 prevents a secure claim that every cancelled clause was replaced by a logically identical later one.

**Context search:** `RN017`; `diagonal`, `separated`, `unramified`, `quasi-finite`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds a withdrawal and later resumption, with both scans; no such revision history is visible in the context head**.

### RN018 — Generic nonextendability is requested as a replacement

**Kind:** self-flagged

**Location:** **131.pdf, scan 012**, top marginal reformulation and rotated passage; frozen page-file line 4; **131.pdf, scan 016**, lower margin; frozen page-file line 19.

**Text:** “Exprimer 8° ici par une impossibilité générique de prolonger”.

The later margin asks for a generic nonextension formulation, while scan 012 contains a longer, heavily revised attempt in that direction. The intended assertion should specify the order on intermediate closed subschemes, localization, and the open set on which maximality persists; the uncertain “plus-petit|grand” on scan 012 is mathematically consequential. The printed comparison in RN002 makes the programme recognizable, but the exact crossed-out and rotated formulation remains a reading question rather than a silently repaired theorem.

**Context search:** `RN018`; `generic`, `unramified`, `prolong`, `extension`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds the author’s requested reformulation and the unresolved order word; no exact statement is supplied by the truncated context**.

### RN019 — The later lifting criterion needs its density assumptions clarified

**Kind:** reading question

**Location:** **131.pdf, scan 007**, insertion in 7; frozen page-file line 4; **131.pdf, scan 016**, NR(b); frozen page-file line 16.

**Text:** “d’adhérence schématique $S'$”; later “irréductible” and “$I\mathfrak p=0$”.

The earlier condition explicitly requires the punctured open to be schematically dense, while the later corollary visibly says irreducible and imposes $I\mathfrak p=0$. Topological irreducibility alone does not exclude embedded associated primes, so it is not a formal substitute for that density hypothesis. Murre’s corresponding F7 uses a unique associated prime (Murre, 1966, pp. 245–246), making the intended meaning or retained background assumptions worth checking; RN020 gives a conditional diagnostic. The transcription remains unchanged, including the product $I\mathfrak p$ rather than the localization $I_{\mathfrak p}$.

**Context search:** `RN019`; `associated`, `irréduct`, `schematic`, `unramified`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds a hypothesis-level discrepancy not addressed by the literature-status head; it does not presume an error in the unavailable full Hua account**.

### RN020 — Own conditional test using an embedded nilpotent

**Kind:** own idea

**Location:** **131.pdf, scan 016**, NR(b); frozen page-file line 16; **131.pdf, scan 007**, earlier density insertion; frozen page-file line 4.

**Text:** “si … $\in\operatorname{Im}F(A_{\mathfrak p})$ alors … $\in\operatorname{Im}F(A)$”.

As an own countercheck under the ordinary topological meaning of irreducible, take $A=k[[t,\varepsilon]]/(\varepsilon^2,t\varepsilon)$, $I=\mathfrak p=(\varepsilon)$, $S=\operatorname{Spec}A$, and $F=h_{\operatorname{Spec}(A/I)}$ over $S$, represented by a finite, finitely presented closed immersion and hence unramified and separated. Here $A$ is complete local Noetherian of dimension one with irreducible spectrum and $I\mathfrak p=0$, and the generic restriction of the identity in $F(A/I)$ lifts over $A_{\mathfrak p}$ because inverting $t$ kills $\varepsilon$, but $F(A)$ is empty since an $A$-algebra map $A/I\to A$ would require the nonzero element $\varepsilon$ to vanish. The embedded associated prime $(t,\varepsilon)$ makes the punctured open fail schematic density, so scan 007 excludes the example and the test targets only the compressed reading of scan 016. **Confidence: high conditional on that interpretation**, because the algebra verifies each displayed hypothesis and failure; this is an unverified research diagnostic of intended scope, not a claim of novelty or an unconditional correction of the manuscript.

**Context search:** `RN020`; `associated`, `embedded`, `nilpotent`, `unramified`, `131-`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds a new-to-this-package conditional check; no corresponding example or settled result occurs in the supplied context**.

### RN021 — The independence question about 7 is explicitly answered only in shorthand

**Kind:** self-flagged

**Location:** **131.pdf, scan 014**, lower diagonal margin; frozen page-file line 26.

**Text:** “Est-ce que 7° est surabondant? Non”.

The question is followed by a negative answer tied to a change in condition 4 from Artinian adic limits to a Noetherian adic setting, but the connecting words are uncertain in the frozen reading. No example or argument on this margin verifies the claimed independence, and the question must be indexed even though the author writes an answer immediately. A precise comparison requires choosing the original and altered versions of 4 and 7 before attempting a counterexample.

**Context search:** `RN021`; `quasi-finite`, `adic`, `condition`, `conjecture`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the author’s explicit question, answer, and qualification; the supplied head contains no independence proof**.

### RN022 — The requested example showing that 8 is needed

**Kind:** conjecture

**Location:** **131.pdf, scan 014**, lower margin request; frozen page-file line 26.

**Text:** “Donner l’exemple-type … montrant que (8°) n’est pas surabondant”.

The author requests a one-dimensional example witnessing nonredundancy of condition 8 in the unramified setting. The retained pages do not specify that example, and the complete-local one-dimensional observation on scan 004 concerns a narrower inductive step rather than refuting this request. Any proposed example must be checked against the full chosen list of locality, limit, prorepresentability, separation, and local-lifting hypotheses, not only against infinitesimal unramifiedness.

**Context search:** `RN022`; `unramified`, `quasi-finite`, `condition`, `one-dimensional`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds an explicit unfulfilled example request and distinguishes it from the complete-local dimension-one remark**.

### RN023 — The promised removal of dimension and finiteness restrictions

**Kind:** unproved claim

**Location:** **131.pdf, scan 014**, marginal NB; frozen page-file line 24.

**Text:** “impliquent l’analogue de 7° sans hypo. de dim 1 ni …”.

The NB proposes deriving a more general version of local modularity from the earlier axioms and 7. The final restriction word is uncertain, so the note cannot be promoted to a precise theorem removing every finiteness assumption. Its proof would have to identify the finite approximations and one-dimensional tests sufficient to detect the larger locus, then show that the filtered-limit and descent hypotheses preserve the conclusion.

**Context search:** `RN023`; `finite`, `dimension`, `quasi-finite`, `modular`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a promised strengthening and its reading limit, rather than silently extending the stated criterion**.

### RN024 — The open-immersion case is left to be made explicit

**Kind:** self-flagged

**Location:** **131.pdf, scan 015**, short proposed special case; frozen page-file line 4; **131.pdf, scan 016**, upper margin; frozen page-file line 10.

**Text:** “Immersion ouverte”; “Expliciter aussi le cas d’une immersion ouverte”.

Scan 015 proposes conditions 1–4 together with an Artinian-test étale monomorphism, and scan 016 still asks for the case to be made explicit. For an existing morphism, an étale monomorphism is an open immersion (Stacks Project Authors, 2026, Tag 025G), but the draft still needs the representability and extension from the restricted test category. The note is therefore a genuine unfinished specialization of the programme even though its final scheme-theoretic implication is standard.

**Context search:** `RN024`; `open immersion`, `étale`, `unramified`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds the unfinished specialization and a scoped known endpoint; qualifies any blanket claim that the draft contains no remaining tasks**.

### RN025 — Generic representability and generic modularity are not the same hypothesis

**Kind:** unproved claim

**Location:** **131.pdf, scan 012**, top generic representability condition; frozen page-file line 3; **131.pdf, scan 017**, RG statement; frozen page-file line 2; **131.pdf, scan 016**, bottom continuation; frozen page-file line 21.

**Text:** “$F_U$ soit représentable”; “La condition 8°) est conséquence de la …”.

The RG sentence asks for representation over a nonempty open of every irreducible closed subscheme, while condition 8 concerns a neighbourhood of a generically modular map. A proof that the former supplies the latter must use the locally finite-type representing scheme and spread the pertinent local property; the bare existence of a point or a generic formal model is weaker. The bottom of Remarque 3 is too uncertain to decide from that line alone exactly which version of generic representability is asserted sufficient.

**Context search:** `RN025`; `generic`, `representab`, `quasi-finite`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds the two distinct formulations and a reading limit at the claimed implication**.

### RN026 — Restricting the testing rings remains a stated programme

**Kind:** conjecture

**Location:** **131.pdf, scan 017**, first remark; frozen page-file line 4.

**Text:** “[Limitation] des anneaux $A,B$ et schémas $S'$” (initial word uncertain).

The remark calls for a smaller family of rings and schemes in conditions 2, 4, 5, 7, and 8, but it does not state a final replacement family. The later essentially finite-type and finite-residue-field tests in Proposition 1 are a concrete internal lead, although they concern recognition of a proposed representing object and cannot automatically replace every test used to construct it. A useful continuation would state each restriction separately and cite the locality, approximation, or descent argument that permits it.

**Context search:** `RN026`; `finite`, `Artinian`, `local`, `representability`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds a test-category optimization question and an internal lead; no completed restriction theorem is supplied by the context**.

### RN027 — The isolated “Façon d’exprimer” is an unfinished textual lead

**Kind:** reading question

**Location:** **131.pdf, scan 018**, only textual line; frozen page-file line 2.

**Text:** “Façon d’exprimer”.

This sparse sheet does not identify which preceding condition was to be reformulated. It may belong to the nearby generic nonextendability discussion, but that attachment is an inference from order rather than an explicit continuation in the surviving words. No missing sentence should be supplied from a published formulation or from the context summary.

**Context search:** `RN027`; `generic`, `unramified`, `131-`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds an unresolved attachment question; neither supplied Hua head contains text that resolves it**.

### RN028 — Formal equality of the self-relation must imply actual equality

**Kind:** unproved claim

**Location:** **131.pdf, scan 020**, first paragraph; frozen page-file line 2.

**Text:** “coïncide formellement avec la diagonale … donc lui est identique”.

The conclusion uses more than agreement on the special fibre: it needs a finite relation and sufficiently strong equality on all infinitesimal neighbourhoods to kill its defining difference. In a Noetherian complete-local argument this calls for completion and faithful-flatness or a separated-intersection argument, with the relevant finite module or ideal explicitly identified. The final transition from an étale monomorphism to an open immersion has the standard endpoint in Stacks Tag 025G, whereas the preceding formal-to-actual equality remains the proof obligation specific to this passage.

**Context search:** `RN028`; `diagonal`, `separated`, `completion`, `unramified`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds the algebraic content hidden in “donc”; does not infer equality from a fibrewise set comparison**.

### RN029 — Own proposal: an axiom-dependency comparison table

**Kind:** own idea

**Location:** **131.pdf, scan 002**, first list; frozen page-file line 13; **131.pdf, scan 014**, reordered theorem list; frozen page-file line 6; **131.pdf, scan 016**, specializations; frozen page-file line 12; **131.pdf, scan 025**, weakened comparison tests; frozen page-file line 18.

**Text:** “conditions”; “injectif”; the several surviving numbered lists.

A useful continuation is a table whose rows are the distinct hypotheses and whose columns are construction of local rings, existence of universal elements, uniqueness, effective descent, openness, and globalization. It should keep the scan 002 and scan 014 numberings separate and mark scan 025 as a recognition statement for an already supplied candidate, then compare the unramified printed criterion without collapsing those roles. **Confidence: medium**, because the explicit proof references make such a table feasible but several overwritten labels and promodularity definitions still need mathematical reconstruction; this is an unverified organizational research idea, not a new theorem.

**Context search:** `RN029`; `conditions`, `effectivity`, `pro-represent`, `131-`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `README.md`, Book I I.VI, rank 22 and **S19**, citing cote 131 scans 002–042; `notes/RESULTS_STATE.md` → **MPL_33_002-049 §2**, source `MPL_33_002-049_notes.md` (scan field truncated after “002…”, original unavailable); **proposes a way to reconcile the two direct findings with the draft’s revisions; no such dependency table occurs in the supplied material**.

## 3. The applications listed on scan 017

### RN030 — The quotient example needs its sheaf and finiteness hypotheses

**Kind:** unproved claim

**Location:** **131.pdf, scan 017**, example a; frozen page-file line 8.

**Text:** “$G/H$, $H$ sous-groupe ouvert $+$ fermé, plat/$S$”.

The quotient is listed as an example without a specification of the quotient topology or the remaining assumptions on $G$ and $H$. A reconstruction should first define the quotient sheaf, verify that its diagonal and infinitesimal lifting behaviour have the required form, and then check the completion and generic conditions; the shorthand does not specify the quotient construction or verify the representability criterion. The flat-kernel application in Murre (1966, §3(A)) is a useful narrower comparator, not a justification for dropping its additional hypotheses or identifying the uncertain preceding word.

**Context search:** `RN030`; `quotient`, `subgroup`, `flat`, `131-unramified`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **LM1 D.11**, source `LM1_GROUP_SCHEMES_results.csv` (location printed “49; 608-609; 610; task D.c integral classification”; types of numbers not expanded; open run claim, original unavailable); **adds the missing scope questions; the arithmetic group-scheme descent row is a different problem and supplies no quotient theorem here**.

### RN031 — Two uncertain example labels must not be repaired from theory

**Kind:** reading question

**Location:** **131.pdf, scan 017**, first word of example a; frozen page-file line 8; **131.pdf, scan 017**, subscheme example; frozen page-file line 18.

**Text:** Frozen readings: “Mémo-finité|Mono-finité”; “distingués|disjoints”.

The first label and the adjective attached to subschemes remain low-confidence readings, even though the neighbouring quotient and group-theoretic examples make several mathematical expansions tempting. Neither supplied Hua excerpt contains these words, and the published subgroup results inspected do not establish what this ink says. In particular, this note makes no unrestricted claim about a moduli functor of all subgroup schemes and does not change either alternative in the transcription.

**Context search:** `RN031`; `subgroup`, `Hom`, `unramified`, `quotient`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds two unresolved readings; the context offers no textually supported replacement**.

### RN032 — Divisorial correspondences identify a specific rigidity programme

**Kind:** unpursued implication

**Location:** **131.pdf, scan 017**, example b; frozen page-file line 10; **131.pdf, scan 017**, application 1 bracket; frozen page-file line 28.

**Text:** “Classes de Correspondances divisorielles”; “sur $X\times_S X$”.

The example and the projectivity bracket single out classes of divisorial correspondences as the proposed parameter functor, rather than an arbitrary functor of all divisors. To use the representability criterion, one must specify the equivalence relation on divisors, its behaviour in families, and the rigidity that makes the resulting functor unramified. The nearby Picard application suggests the relevant line-bundle framework, but the page does not itself construct this correspondence scheme or prove the required rigidity.

**Context search:** `RN032`; `correspond`, `Picard`, `Murre`, `algebraic representative`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **WG2 §2.4 #4**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (cotes 47/44 named, no scan supplied; unchecked plan, original unavailable); `notes/RESULTS_STATE.md` → **WG2 §2.3 #13**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (no scan supplied; unchecked algebraic-representative/Murre-1985 lead, original unavailable); **adds the manuscript’s explicit mechanism; differs from the unchecked higher-codimension algebraic-representative programme**.

### RN033 — Pointed Hom is not automatically rigid for an arbitrary source

**Kind:** unproved claim

**Location:** **131.pdf, scan 017**, example c; frozen page-file line 12.

**Text:** “Hom [pointés] dans un groupe commutatif”.

The shorthand does not name the source scheme, its connectedness or properness assumptions, or the role of the chosen point. Those conditions matter: merely fixing a point does not make every mapping functor into a commutative group unramified, so a usable theorem must identify the rigidity argument that removes infinitesimal variation. The more specific abelian-source example in the next line has a verified comparator in RN034 and should not silently supply hypotheses for every earlier Hom notation.

**Context search:** `RN033`; `Hom`, `abelian`, `unramified`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds an explicit scope gap in the general pointed-Hom shorthand, beyond the context’s abelian-scheme example**.

### RN034 — Hom from an abelian scheme: unramified need not mean étale

**Kind:** unproved claim

**Location:** **131.pdf, scan 017**, abelian Hom example; frozen page-file line 14.

**Text:** “Hom de V.A. dans un groupe comm.”

SGA 3 XI §6.6 states representability and unramifiedness of $\operatorname{Hom}_{S\text{-gr}}(H,G)$ when $H$ is an abelian scheme over locally Noetherian $S$ and $G$ is a commutative group prescheme locally of finite type (Grothendieck, 1970). That passage also explains why special-fibre homomorphisms need not extend, so one cannot upgrade this example to an étale functor merely because the same page later mentions étale component functors. The manuscript records the application without its proof or full hypotheses, making the scoped published statement the appropriate comparison.

**Context search:** `RN034`; `Hom`, `abelian`, `étale`, `unramified`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **confirms a precise application theme while adding the important distinction between uniqueness and existence of infinitesimal extensions**.

### RN035 — Universal flattening is an application with real hypotheses

**Kind:** unpursued implication

**Location:** **131.pdf, scan 017**, insertion in example e; frozen page-file line 16.

**Text:** “Foncteurs platificateurs”.

The inserted example points to a subfunctor of the base whose values record flatness, but no hypotheses on a morphism or module are written here. For a proper finitely presented morphism and a module of finite presentation, a universal flattening exists and is a monomorphism of finite presentation (Stacks Project Authors, 2026, Tag 05UH). A universal flattening and a flattening stratification are distinct notions; Tag 052F gives a module that is not finitely presented whose pullbacks to all $k[x,y]/(x,y)^n$ are flat but whose pullback to $k[[x,y]]$ is not, showing that finite-level flatness alone does not guarantee effectivity. The application therefore warrants a full hypothesis check rather than an unrestricted existence assertion.

**Context search:** `RN035`; `flatten`, `flat`, `platifi`, `effectiv`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a scoped theorem and a relevant effectivity obstruction; no distinct flatificator result is supplied by the context**.

### RN036 — Connected and irreducible component functors require separate definitions

**Kind:** unproved claim

**Location:** **131.pdf, scan 017**, example f; frozen page-file line 21.

**Text:** “composantes connexes … composantes irred.”; “même étales”.

The passage does not define whether it parametrizes individual components, decompositions into components, or another finite factorization, and the properness word itself is marked uncertain. For comparison, the Stein factor of a proper flat finitely presented morphism with geometrically reduced fibres is finite étale (Stacks Project Authors, 2026, Tag 0E0D). That result supports a precise connected-component construction under its hypotheses, but it does not establish the unqualified irreducible-component assertion suggested by the parenthetical shorthand. The next step is to identify both functors and their behaviour when components split or meet in special fibres.

**Context search:** `RN036`; `component`, `composante`, `étale`, `unramified`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds missing definitions and hypotheses; the broad corollary finding contains no exact component-functor result**.

### RN037 — Factorizations of a finite morphism are only named

**Kind:** unpursued implication

**Location:** **131.pdf, scan 017**, line below example f; frozen page-file line 23.

**Text:** “Factorisations d’un morphisme fini … ouvert”.

The line proposes a further application but does not specify the middle object, the allowed morphisms in the factorization, or its equivalence relation. An étale parameter construction would require precise factorization data and base-change conditions; the reading “univ.” before “ouvert” remains uncertain. No such construction is supplied on the retained page, so this remains an application lead rather than a consequence already proved here.

**Context search:** `RN037`; `factor`, `finite`, `étale`, `component`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds an unpursued application with unresolved moduli data; no exact counterpart occurs in the supplied register**.

### RN038 — Projectivity of abelian schemes and extension of a polarization

**Kind:** unproved claim

**Location:** **131.pdf, scan 017**, application 1; frozen page-file line 27; **131.pdf, scan 017**, its bracketed method; frozen page-file line 28.

**Text:** “Un schéma abélien sur $S$ loc. noeth. normal est projectif sur $S$”.

The heading “Applications en vue” and the instruction to use divisorial correspondences mark a target and a proposed mechanism, with no proof on this sheet. Deligne (1985, §1.1(c)) states extension of a generic-fibre polarization and resulting projectivity over a normal integral base, under his quasi-compact and quasi-separated conventions, citing the Grothendieck–Murre/Raynaud argument. This supplies a precise published comparator covering the normal Noetherian integral case; extending the comparison to the manuscript’s full locally Noetherian wording requires an explicit treatment of components and the convention for relative projectivity. Raynaud XI.1.4 is an identified dependency, but its original theorem text was not directly inspected in this review.

**Context search:** `RN038`; `projecti`, `abelian`, `correspond`, `Picard`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **WG2 §2.4 #4**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (cotes 47/44 named, no scan supplied; unchecked plan, original unavailable); **adds a verified polarization-extension comparator; the context’s thematic plan alone did not verify the stated projectivity application**.

### RN039 — Picard existence over a field has a direct published theorem

**Kind:** unproved claim

**Location:** **131.pdf, scan 017**, application 2; frozen page-file line 30.

**Text:** “Existence du Picard d’un schéma propre sur un corps”.

Murre (1964, II.15, Theorem 2) proves representability of the Picard functor of a proper scheme over a field by a group scheme locally of finite type. That is a close comparator for the announced application, while the manuscript does not reproduce the necessary functor definition or proof. The Picard 1-motive in LM7 C.1 concerns a particular Fermat/Jacobian construction and is not an earlier proof of this representability theorem.

**Context search:** `RN039`; `Picard`, `proper`, `Murre`, `1-motive`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **LM7 C.1**, source `LM7_FERMAT_TOWER_results.csv` (§51.13–14, folios 719–724, scans 143–153; known-status run claim, original unavailable); **confirms a published theorem matching the application; distinguishes it from the different Picard object in the existing result register**.

### RN040 — The inserted historical names refer to different Picard statements

**Kind:** reading question

**Location:** **131.pdf, scan 017**, insertion in application 2; frozen page-file line 30.

**Text:** “[Chevalley–Seshadri–Grothendieck–Murre]”.

The name sequence does not provide bibliographic references or assert that the four authors proved identical statements. Grothendieck’s FGA V, Corollary and Remark 6.6, distinguishes the full projective Picard theorem from Chevalley’s and Seshadri’s reduced-parameter predecessors; Murre’s later theorem supplies the proper field case (Grothendieck, 1962; Murre, 1964). The context’s Murre-1985 algebraic-representative lead is chronologically and mathematically different, so the shared surname cannot serve as the reference intended on this page.

**Context search:** `RN040`; `Chevalley`, `Seshadri`, `Murre`, `Picard`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **WG2 §2.3 #13**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (no scan supplied; unchecked algebraic-representative/Murre-1985 lead, original unavailable); **adds exact historical comparators and rejects a misleading same-name identification with the unchecked later programme**.

### RN041 — The generic-base Picard application must specify the base

**Kind:** unproved claim

**Location:** **131.pdf, scan 017**, end of application 2; frozen page-file line 30.

**Text:** “sur une base $S$, existence au-dessus d’un ouvert non vide”.

The sentence leaves the base hypotheses implicit; Murre’s 1964 introduction reports Grothendieck’s generic existence result for a proper scheme over an integral Noetherian base. A modern comparator assumes that $f:X\to B$ is proper, flat, and finitely presented and that $\mathcal O_T\to f_{T,*}\mathcal O_{X_T}$ is an isomorphism for every scheme $T\to B$, and concludes that the relative Picard sheaf is an algebraic space (Stacks Project Authors, 2026, Tag 0D2C). That result must not be substituted verbatim for the draft’s generic scheme-existence statement, since both the hypotheses and the representability category differ. The raw assignment of absolute Picard groups on test schemes must also be distinguished from the appropriate relative sheaf.

**Context search:** `RN041`; `Picard`, `generic`, `representability`, `abelian`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **WG2 §2.4 #4**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (cotes 47/44 named, no scan supplied; unchecked plan, original unavailable); **adds a scoped historical statement and a distinct modern comparison; does not infer unrestricted existence over every base**.

### RN042 — Own comparison with the algebraic-representative programme

**Kind:** own idea

**Location:** **131.pdf, scan 017**, divisorial correspondence example; frozen page-file line 10; **131.pdf, scan 017**, Picard application; frozen page-file line 30.

**Text:** “Classes de Correspondances divisorielles”.

A useful comparison with WG2 §2.3 #13 is to ask whether a proposed higher-codimension algebraic representative controls a full family-valued functor, a quotient of such a functor, or only regular homomorphisms on algebraically trivial cycles. The divisorial/Picard case suggests examining descent and infinitesimal rigidity separately: the full Picard functor need not be quasi-finite or unramified, so any use of this criterion must first identify a functor satisfying its hypotheses. **Confidence: medium as a research direction**, because the manuscript supplies the codimension-one motivation but the context contains only a compressed, unchecked higher-codimension plan; no transfer theorem or novelty is claimed.

**Context search:** `RN042`; `algebraic representative`, `Murre`, `correspond`, `codimension`, `Picard`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.3 #13**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (no scan supplied; unchecked algebraic-representative/Murre-1985 lead, original unavailable); `notes/RESULTS_STATE.md` → **WG2 §2.4 #4**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (cotes 47/44 named, no scan supplied; unchecked plan, original unavailable); **proposes an unverified link between different parameter problems; neither restates nor rederives a settled result in the supplied context**.

## 4. The auxiliary recognition lemmas and finite complete models

### RN043 — Why finite-residue-field local tests can suffice

**Kind:** unproved claim

**Location:** **131.pdf, scan 023**, Proposition 1 hypothesis; frozen page-file line 8; **131.pdf, scan 025**, covering insertion; frozen page-file line 8.

**Text:** “à extension résiduelle finie”; “les $U_t$ recouvrent $T$”.

The local test class is restricted, although the opening proof subsequently writes “pour tout localisé” in a compressed way. For a finite-type affine test scheme, every point specializes within its fibre to a closed fibre point, and such closed points have finite residue-field extension over the base point (Stacks Project Authors, 2026, Tag 01TF). Open neighbourhoods of these test points therefore cover the scheme, which supplies the missing justification for the insertion without silently broadening the stated test class.

**Context search:** `RN043`; `local`, `Artinian`, `finite`, `representability`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the residual-field and covering argument, absent from the truncated direct finding**.

### RN044 — Spreading the morphism and spreading equality use two hypotheses

**Kind:** unpursued implication

**Location:** **131.pdf, scan 025**, opening proof continuation; frozen page-file line 2.

**Text:** “$X$ est loc de prés. finie”; “prenant $U$ assez petit”.

Local finite presentation of $X/S$ lets the local morphism $u_t$ spread to an open neighbourhood, while the filtered-ring-colimit condition on $F$ lets its section agree with the prescribed section after a further shrinking. These are different uses of limit preservation, followed by uniqueness on overlaps and Zariski locality to glue. Stacks Tag 01ZC gives the precise morphism-limit comparison for the first use and for spreading equalities of morphisms; it does not replace the separate hypothesis on the unrepresented functor.

**Context search:** `RN044`; `finite presentation`, `limits`, `local`, `representability`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a separation of the two approximation steps, rather than attributing both to one unspecified locality axiom**.

### RN045 — The section symbols in Proposition 1 and its descent conclusion

**Kind:** reading question

**Location:** **131.pdf, scan 023**, end of surjectivity paragraph; frozen page-file line 21; **131.pdf, scan 029**, display after descent; frozen page-file line 4.

**Text:** “induisant $\xi_t$”; later “$F(f')$”.

The first passage starts with a section read as $\eta$ but ends with $\xi_t$, and the descent conclusion writes $F(f')$ after defining $f$. The surrounding proof suggests section and morphism identifications, but it does not justify silently changing the letters in the diplomatic text. Any formal reconstruction should declare those identifications separately and check domains and codomains against the displayed diagram.

**Context search:** `RN045`; `completion`, `descent`, `prorepresent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds two local typing questions; no notation-level resolution appears in the supplied context**.

### RN046 — The deleted descent axiom is replaced by uniqueness tests

**Kind:** withdrawn in the same text

**Location:** **131.pdf, scan 025**, cancelled hypothesis; frozen page-file line 17; **131.pdf, scan 025**, first of two surviving comparison assumptions; frozen page-file line 18.

**Text:** Deleted “$F$ compatible avec desc. fid. plts”; surviving “injectif”.

The revised corollary requires injectivity of $F(B)\to F(\widehat B)$ and $F(\widehat B)\to\varprojlim F(B_n)$, which asserts uniqueness rather than existence of an effective formal section. Here an actual candidate $(X,\xi)$ has already been supplied, so formal maps may be realized inside that scheme and then compared in $F$. This weaker recognition lemma must not be restated as a full formal-effectivity criterion merely because the earlier global theorem uses stronger compatibility language.

**Context search:** `RN046`; `effectivity`, `completion`, `descent`, `prorepresent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **differs from the head’s broad effectivity description by identifying a later weakened recognition statement and its pre-existing candidate**.

### RN047 — An uncertain isomorphism sign coexists with “injectif”

**Kind:** reading question

**Location:** **131.pdf, scan 025**, completion-to-Artinian-limit display; frozen page-file line 22.

**Text:** Frozen LaTeX: `F(\widehat B)\xrightarrow{\unsure{\sim}}\varprojlim F(B_n)`; “injectif”.

The frozen display retains an uncertain isomorphism decoration together with the emphatic word injectif. The proof of this corollary can be read using injectivity, whereas later construction of universal sections would need more; mathematical usefulness therefore cannot decide whether the decoration is live, overwritten, or misread. The ambiguity is confined to the research discussion and does not authorize normalizing the arrow or the word.

**Context search:** `RN047`; `effectivity`, `Artinian`, `completion`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a consequential notation ambiguity for which the general context summary supplies no textual resolution**.

### RN048 — Compatible infinitesimal maps into an existing scheme are effective here

**Kind:** unproved claim

**Location:** **131.pdf, scan 027**, surjectivity construction; frozen page-file line 11.

**Text:** “uniques, donc compatibles, d’où … $u':T'\mathbin{-}X$”.

All Artinian sources have the same underlying closed point, so the compatible maps land in one affine open of $X$ containing its image, and the inverse limit of the ring maps constructs a map from $\operatorname{Spec}\widehat B$. This is a local-source effectivity statement for maps into an existing scheme, as in Stacks Tag 0AQG; it needs neither properness of $X$ nor a general Artin algebraization theorem. Equality with the prescribed $F$-section then uses injectivity of the completion-to-Artinian comparison, a separate step.

**Context search:** `RN048`; `effectivity`, `completion`, `Artinian`, `Greenberg`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **MPL_91_099-143 §68**, source `MPL_91_099-143_notes.md` (scans 124, 126, 128; first-pass Greenberg–Néron lead, original unavailable); **adds the elementary map-effectivity mechanism; the Greenberg–Néron excerpt is only a thematic comparison and is not needed as a theorem**.

### RN049 — The completion overlap requires global monicity first

**Kind:** unproved claim

**Location:** **131.pdf, scan 027**, overlap equality; frozen page-file line 17.

**Text:** “En vertu de $1^\circ)$”; “$T'\times_T T'$”.

The overlap need not be local or essentially of finite type over $S$, so the already-proved injectivity on restricted local tests cannot be applied there without a further reduction. The intended repair is to extend monicity from those tests to finite-type affine schemes and then arbitrary affine schemes, using local finite presentation of $X$, filtered-limit compatibility of $F$, and locality as in Proposition 1. With that global statement supplied, equality of the two $F$-sections yields equality of the two maps; this is an omitted-step diagnosis, not a counterexample to the corollary. The relevant morphism-limit theorem is Stacks Tag 01ZC.

**Context search:** `RN049`; `monomorph`, `completion`, `descent`, `representability`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a specific domain-of-application check and a proposed proof completion; no matching overlap argument is in the supplied head**.

### RN050 — Descending a morphism and identifying an F-section are distinct

**Kind:** unpursued implication

**Location:** **131.pdf, scan 029**, descent conclusion; frozen page-file line 2.

**Text:** “Donc il existe $u:T\to X$”; “$\eta=F(u)(\xi)$”.

The completion of a Noetherian local ring is faithfully flat, and representable functors satisfy fpqc descent, so the overlap equality descends $u'$ to a unique morphism $u$ (Stacks Project Authors, 2026, Tags 00MC and 023Q). The final equality of sections then follows from injectivity of $F(B)\to F(\widehat B)$ rather than from a further existence theorem for $F$. This explains why removal of the full sheaf axiom for $F$ in this recognition corollary is compatible with still using descent for the known scheme $X$.

**Context search:** `RN050`; `descent`, `completion`, `effectivity`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the two distinct objects to which descent or injectivity is applied; does not reintroduce the deleted axiom without justification**.

### RN051 — The relative natural-transformation formulation is explicitly preferred

**Kind:** unpursued implication

**Location:** **131.pdf, scan 023**, upper margin; frozen page-file line 11; **131.pdf, scan 029**, NB; frozen page-file line 9.

**Text:** “$F\to G$ … mono, imm. ouverte, isom.”; later “$G\to F$”.

The two remarks propose testing a natural transformation rather than only recognizing a scheme representing a single functor, with the direction of the letters changing between the passages. Murre’s §2 Lemma 1 is the direct printed comparison for Artinian tests of monomorphisms and isomorphisms (Murre, 1966). The open-immersion variant still needs its additional formal lifting and local finite-presentation hypotheses, so it is not supplied merely by replacing the word isomorphism in the lemma.

**Context search:** `RN051`; `Artinian`, `representability`, `Murre`, `monomorph`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds the preferred relative reformulation and distinguishes its three different conclusions**.

### RN052 — “Artinian, i.e. finite” uses a residue-field convention

**Kind:** reading question

**Location:** **131.pdf, scan 029**, Corollary 2 condition 1; frozen page-file line 13.

**Text:** “artiniens, i.e. finis sur … ceux de $S$”.

An Artinian ring is not automatically a finite algebra over an Artinian base: for example $k(t)$ is an Artinian ring but is not finite over $k$. The intended equivalence therefore depends on the finite residue-extension convention in the prorepresentability category, or on an additional finiteness assertion established elsewhere. The nearby test categories suggest that convention, but the phrase should be explained in a reconstruction rather than silently treated as a general algebraic equivalence.

**Context search:** `RN052`; `Artinian`, `finite`, `prorepresent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a necessary convention check to the abbreviated finiteness claim**.

### RN053 — Finite local algebras already give ordinary schemes

**Kind:** unpursued implication

**Location:** **131.pdf, scan 031**, Proposition 2 condition 2; frozen page-file line 14; **131.pdf, scan 031**, finite-model construction; frozen page-file line 21.

**Text:** “finis sur $A$”; “$\coprod_i\operatorname{Spec}B_i$”.

If each $B_i$ is genuinely finite over the complete Noetherian local ring $A$, its spectrum is already an ordinary finite $A$-scheme; no separate approximation theorem is needed merely to form that scheme. A finite algebra over such a base is a product of complete Noetherian local rings (Stacks Project Authors, 2026, Tag 0325). The substantive remaining issue is existence of the universal element of $F(B_i)$, which is logically different from existence of $\operatorname{Spec}B_i$.

**Context search:** `RN053`; `prorepresent`, `finite`, `effectivity`, `Greenberg`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **MPL_91_099-143 §68**, source `MPL_91_099-143_notes.md` (scans 124, 126, 128; first-pass Greenberg–Néron lead, original unavailable); **adds the finite-model/effective-section distinction; no approximation theorem from the earlier-package excerpt is required for the finite spectrum itself**.

### RN054 — Universal sections require effectivity, conditionally on the reused labels

**Kind:** unproved claim

**Location:** **131.pdf, scan 031**, construction after condition 3; frozen page-file line 19; **131.pdf, scan 025**, earlier weakened conditions; frozen page-file line 18.

**Text:** “On construit grâce à $2^\circ)$ … $\xi_1$”.

Compatible Artinian universal elements determine a formal system, but to obtain $\xi_i\in F(B_i)$ one needs existence in the comparison with the inverse limit, not just injectivity. Consequently this construction has an unfilled effectivity step if condition 3 reuses only the weakened injective maps on scan 025; there is no such objection if the altered labels refer back to the stronger compatibility hypotheses of scans 002 or 014. Because the subscripts, superscripts, and arrow directions of the $L$ labels are revised and partly uncertain, this remains a conditional proof audit rather than an unconditional declaration that Proposition 2 is false.

**Context search:** `RN054`; `effectivity`, `Artinian`, `completion`, `prorepresent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the precise existence-versus-uniqueness question left unresolved by the broad effectivity head**.

### RN055 — The punctured-base gluing hypothesis is explicitly assumed

**Kind:** unproved claim

**Location:** **131.pdf, scan 031**, open-immersion condition; frozen page-file line 25; **131.pdf, scan 033**, proof continuation; frozen page-file line 5.

**Text:** “$u$ est une immersion ouverte”; “on peut recoller”.

The auxiliary proposition assumes that the overlap map is an open immersion and then glues the finite models to the scheme over the punctured base. It therefore isolates rather than proves the crucial openness step used in the opening dimension induction. In reconstructing the main theorem, one must also retain the separation argument ensuring that images of distinct finite local pieces do not become wrongly identified on the punctured base.

**Context search:** `RN055`; `separated`, `quasi-finite`, `descent`, `open immersion`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the boundary between the auxiliary gluing proposition and the openness/separation work required in the main proof**.

### RN056 — Two requested simplifications of the gluing proposition

**Kind:** self-flagged

**Location:** **131.pdf, scan 031**, long margin; frozen page-file line 27; **131.pdf, scan 033**, upper margin; frozen page-file line 3.

**Text:** “Simplifier l’énoncé”; “Transformer $4^\circ)$ sous une forme plus facile à vérifier”.

The first margin proposes starting with a model on $U$ and a scheme $Z$ carrying an $F$-section, with an open overlap, promodularity at the special fibre, and a special-fibre isomorphism. The following margin separately asks for a convenient one-dimensional criterion for the open-immersion condition. Neither request should disappear into a polished restatement: the packet records the proposed data but leaves the equivalence and the reduced test to be justified.

**Context search:** `RN056`; `one-dimensional`, `finite`, `representability`, `modular`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **MPL_33_098-146 §65**, source `MPL_33_098-146_notes.md` (no scan supplied; methodological first-pass lead, original unavailable); **adds two explicit author tasks and their proposed hypotheses, with both manuscript locations**.

## 5. Local modularity and the final globalization argument

### RN057 — The field-of-definition condition is part of local modularity

**Kind:** unpursued implication

**Location:** **131.pdf, scan 035**, field square and condition 2; frozen page-file line 26; **131.pdf, scan 035**, final NB; frozen page-file line 38.

**Text:** “$L$ est un corps de définition pour $\beta$”.

The definition combines a local universal property with a field comparison: equality after embedding in a common overfield is required to force the specified inclusion and descent of the point. This is stronger information than an unlabelled tangent-space or completed-local-ring comparison and is used in identifying local models that represent the same geometric object. Any replacement of “modulaire local” by a modern term must account for both clauses, including the role of residue fields.

**Context search:** `RN057`; `modular`, `corps de définition`, `field`, `prorepresent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the actual two-part definition; the supplied context has no separate field-of-definition statement**.

### RN058 — Variance in the displayed Hom of fields

**Kind:** reading question

**Location:** **131.pdf, scan 035**, image condition in clause 1; frozen page-file line 10; **131.pdf, scan 035**, clause 2; frozen page-file line 29.

**Text:** “$\operatorname{Hom}_k(k(t'),k(t))$”; later “$\lambda:L\mathbin{-}L'$”.

If $\operatorname{Hom}_k$ denotes field homomorphisms, evaluating $\eta(t)\in F(k(t))$ on a $k(t')$-point normally uses a map $k(t)\to k(t')$, whereas the frozen display reverses those arguments. It may reflect a scheme convention or a draft variance slip; the later $L\to L'$ comparison supports the usual ring-map direction without determining the ink. The standard contravariance of affine schemes and rings is recorded in Stacks Tag 01I1, but it is not a warrant to repair this display.

**Context search:** `RN058`; `modular`, `field`, `prorepresent`, `Hom`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a convention question not answered by any supplied contextual formula**.

### RN059 — Actual local-ring isomorphisms are not merely formal agreement

**Kind:** unproved claim

**Location:** **131.pdf, scan 037**, first paragraph; frozen page-file line 2.

**Text:** “$\bar\eta$ est un isomorphisme”.

Under local representability, the text identifies local modularity with an isomorphism of actual local rings. An étale map with equal residue fields can induce an isomorphism on completions without inducing an isomorphism of the original local rings, so replacing this sentence by formal étaleness alone would change its content. To reach the later open charts, the proof must keep track of monicity and local finite presentation as well as the local condition; Stacks Tag 025G supplies the corresponding open-immersion endpoint.

**Context search:** `RN059`; `modular`, `completion`, `étale`, `local`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the distinction between the actual and completed local statements, not exposed by the context’s summary**.

### RN060 — Common field realizations are asserted to identify the local models

**Kind:** unproved claim

**Location:** **131.pdf, scan 037**, second paragraph; frozen page-file line 4.

**Text:** “il existe un $S$-isom $\varphi:T\mathbin{-}T'$”.

The NB claims that agreement after the field diagram characterizes isomorphism of two locally modular parameter schemes. The intended proof must first use the field-of-definition clause to identify the residue-field data, then use the two local universal properties to obtain mutually inverse maps. Leaving out either clause would turn the claim into a substantially weaker geometric-point comparison, insufficient on its own to identify local schemes.

**Context search:** `RN060`; `modular`, `field`, `isom`, `prorepresent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a proof obligation internal to the local-modularity definition; no same-object result is in the register**.

### RN061 — The constructible modularity locus is the hard input

**Kind:** unproved claim

**Location:** **131.pdf, scan 033**, Proposition 3 condition 2; frozen page-file line 15; **131.pdf, scan 037**, proof; frozen page-file line 14.

**Text:** “partie constructible”; “il est donc ouvert”.

Once stability under generization is established, the openness conclusion follows from a precise topological theorem. Stacks Tag 0903 proves the relevant implication on spectral spaces for a set open in the constructible topology, so the affine-scheme step need not acquire an unnecessary extra Noetherian assumption. The geometric content remains the manuscript’s constructibility assertion for $M(T,\eta)$ and the proof that local representability makes this locus stable under generization.

**Context search:** `RN061`; `constructib`, `modular`, `generic`, `representability`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `README.md`, Book I I.VI, rank 22 and **S19**, citing cote 131 scans 002–042; `notes/RESULTS_STATE.md` → **MPL_33_002-049 §2**, source `MPL_33_002-049_notes.md` (scan field truncated after “002…”, original unavailable); **adds a scoped topology reference while preserving the genuinely geometric hypothesis to be proved**.

### RN062 — The generic modularity reformulation is explicitly requested

**Kind:** self-flagged

**Location:** **131.pdf, scan 033**, margin beside constructibility; frozen page-file line 16.

**Text:** “Transformer en une condition de modularité ``générique''”.

The request aims to replace a global constructibility condition by a test around generic points. A valid replacement must quantify over the appropriate irreducible closed subsets or base changes and specify when the locus contains a nonempty open, rather than merely asserting the existence of one generic model. The earlier RG and nonextendability variants offer possible formulations, but the page does not prove that any particular one is equivalent to condition 2 of Proposition 3.

**Context search:** `RN062`; `generic`, `modular`, `representab`, `S19`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds the explicit unfinished equivalence problem and its internal candidate formulations**.

### RN063 — A direct gluing attempt is cancelled in favour of a relation lemma

**Kind:** withdrawn in the same text

**Location:** **131.pdf, scan 039**, cancelled top paragraph; frozen page-file line 5; **131.pdf, scan 039**, live replacement; frozen page-file line 7; **131.pdf, scan 041**, final continuation; frozen page-file line 2.

**Text:** Cancelled “les $X^{(a)}$ se recollent”; live “$h_Z\times_F h_Z$”.

The page abandons a direct construction of pairwise overlap sets and instead introduces representability of the self-fibre product and locally isomorphic projections. The final sheet uses triviality of this relation after a suitable shrinking before invoking another formal gluing proposition. This is a recorded change of proof strategy within scans 039–041, not evidence that the cancelled paragraph can be included as an additional completed argument.

**Context search:** `RN063`; `gluing`, `recol`, `descent`, `representability`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **MPL_33_098-146 §65**, source `MPL_33_098-146_notes.md` (no scan supplied; methodological first-pass lead, original unavailable); **adds the internal withdrawal and replacement, including the continuation scan**.

### RN064 — The relation lemma’s necessary assumptions are left for review

**Kind:** self-flagged

**Location:** **131.pdf, scan 039**, margin beside lemma; frozen page-file line 13.

**Text:** “Reprendre les conditions nécessaires sur $F$”.

The author explicitly asks which conditions on $F$ the lemma needs, with the following claim of weaker assumptions itself uncertain in the frozen reading. A precise version should state what makes the equality subfunctor representable, what ensures its projections are local isomorphisms, and where locality and limit preservation enter. These questions must be answered before using the lemma independently of the larger representability proof.

**Context search:** `RN064`; `modular`, `monomorph`, `representability`, `conditions`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **MPL_33_098-146 §65**, source `MPL_33_098-146_notes.md` (no scan supplied; methodological first-pass lead, original unavailable); **adds an author-marked hypothesis audit not settled by the register’s broad criterion statement**.

### RN065 — The argument of F in the relation lemma remains uncertain

**Kind:** reading question

**Location:** **131.pdf, scan 039**, lemma setup; frozen page-file line 7.

**Text:** Frozen alternatives: “$\eta\in F(S)$ | $\eta\in F(Z)$”.

A general natural transformation $h_Z\to F$ is specified by an element of $F(Z)$, whereas an element of $F(S)$ would first be pulled back and would describe a more special section. This type distinction makes $F(Z)$ a plausible mathematical alternative, but it does not decide between the frozen readings or justify replacing $S$ in the transcription. The supplied context contains no version of this lemma from which an independent textual reading could be obtained.

**Context search:** `RN065`; `modular`, `representability`, `functor`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a consequential type question; no underlying lemma text is available in the context**.

### RN066 — Triviality over a local base must spread to one neighbourhood

**Kind:** unproved claim

**Location:** **131.pdf, scan 039**, last line; frozen page-file line 20; **131.pdf, scan 041**, first sentence; frozen page-file line 2.

**Text:** “relation d’équivalence triviale”; “voisinage ouvert convenable de $a$”.

The proof needs one neighbourhood on which the whole self-relation becomes the diagonal, not separate pointwise neighbourhoods with no uniform control. A standard route applies Stacks Tag 081E to the diagonal $Z\to Z'$ over the directed system of affine neighbourhoods of $a$, after checking that the initial base, $Z$, and $Z'$ are quasi-compact and quasi-separated and that this diagonal morphism is locally of finite presentation. These requirements can be addressed in the Noetherian finite-chart setting, but the manuscript’s more general wording should not be extended without checking them.

**Context search:** `RN066`; `local`, `finite presentation`, `representability`, `gluing`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the uniform shrinking and finiteness obligations behind the compressed conclusion**.

### RN067 — “Quasi-modulaire” receives an explicitly requested clarification

**Kind:** self-flagged

**Location:** **131.pdf, scan 041**, middle bracket; frozen page-file line 2.

**Text:** “Préciser la signification de ce terme”; inserted “est une immersion ouverte”.

The bracket is an explicit author flag about terminology, and the insertion proposes an open-immersion meaning for the chart map. It should not be converted into a claim that an earlier definition of quasi-modularity was already complete. The substantive verification is that the preceding shrinking actually produces this representable open subfunctor, not merely local isomorphisms of stalks or points.

**Context search:** `RN067`; `modular`, `open immersion`, `representability`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **MPL_33_098-146 §65**, source `MPL_33_098-146_notes.md` (no scan supplied; methodological first-pass lead, original unavailable); **adds a surviving terminology task and its proposed interpretation**.

### RN068 — The final formal gluing proposition needs a covering condition

**Kind:** unproved claim

**Location:** **131.pdf, scan 041**, final sentence; frozen page-file line 2.

**Text:** “une autre proposition ``formelle'' nous permet de recoller”.

A Zariski sheaf covered by representable open subfunctors is representable by gluing, as stated in Stacks Tag 01JJ. The remaining coverage check is that for every $T/S$ and every $\eta\in F(T)$, the open subschemes representing $T\times_F X_i$ jointly cover $T$; the limit condition helps reduce this verification to the local and finite-type tests. SGA 3 XI Proposition 3.5 supplies a related printed open-chart criterion with differently organized descent and limit hypotheses (Grothendieck, 1970), but it does not erase the intervening chart-construction obligations.

**Context search:** `RN068`; `gluing`, `open immersion`, `representability`, `S19`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); `README.md`, Book I I.VI, rank 22 and **S19**, citing cote 131 scans 002–042; `notes/RESULTS_STATE.md` → **MPL_33_002-049 §2**, source `MPL_33_002-049_notes.md` (scan field truncated after “002…”, original unavailable); **adds a verified gluing endpoint and identifies the coverage check still needed in the draft**.

### RN069 — Own diagnostic: local-isomorphism projections alone do not force a scheme quotient

**Kind:** own idea

**Location:** **131.pdf, scan 039**, relation lemma; frozen page-file line 12; **131.pdf, scan 041**, shrinking instruction; frozen page-file line 2.

**Text:** “isomorphismes locaux”; “assez petit”.

As an own comparison, Stacks Example 03FN uses $U=\operatorname{Spec}k'[x]$ for a quadratic Galois extension and the relation $R=\Delta U\amalg\Delta'(U\setminus\{0\})$, whose projections are local isomorphisms but whose quotient is not a scheme. This explains why the manuscript’s further shrinking to trivial self-relations and open charts is substantive. **Confidence: high for this diagnostic**, because the published example is explicit; it is not a counterexample to the full manuscript criterion, since that example is nonseparated and does not satisfy all the local-model hypotheses. The proposed use of the comparison remains an unverified reconstruction aid, with no novelty claim.

**Context search:** `RN069`; `quotient`, `gluing`, `separated`, `representability`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a diagnostic countermodel to an overweak gluing shortcut, not a contradiction of a supplied settled result**.

### RN070 — Own limited link to the open integral group-scheme descent problem

**Kind:** own idea

**Location:** **131.pdf, scan 005**, completion descent; frozen page-file line 6; **131.pdf, scan 029**, relative comparison NB; frozen page-file line 9.

**Text:** “donnée de descente”; “un hom de foncteurs $G\to F$”.

The open LM1 D.11 item could potentially use the relative recognition lemma only after its integral group-scheme classification has been formulated as an explicit natural transformation with the required local and limit properties. The present packet does not supply that transformation, its test rings at 2, or the descent datum for the particular $\mu_2$-extension, so it gives no solution of LM1 D.11. **Confidence: low as a transfer proposal**, because the common descent language suggests a possible method but the source statement and proof files are unavailable; the idea is unverified and claims no new result.

**Context search:** `RN070`; `LM1 D.11`, `integral`, `descent`, `group`.

**Context comparison:** `notes/RESULTS_STATE.md` → **LM1 D.11**, source `LM1_GROUP_SCHEMES_results.csv` (location printed “49; 608-609; 610; task D.c integral classification”; types of numbers not expanded; open run claim, original unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **records a conditional method under the actual open-item ID and explicitly identifies the missing bridge**.

## 6. Reused typed leaves: mathematical and textual cautions

### RN071 — The typed leaves have separate source pagination

**Kind:** reading question

**Location:** **131.pdf, scan 008**, typed header; frozen page-file line 3; **131.pdf, scan 010**, typed header; frozen page-file line 3; **131.pdf, scan 013**, typed header; frozen page-file line 2; **131.pdf, scan 042**, typed header; frozen page-file line 2.

**Text:** “n° 392”; “n° 371”; typed page marks “4–27”, “4–26”, “–54–”, “–25–”.

The retained packet contains fourteen reused typed leaves with their own pagination, alongside the handwritten folio sequence. The number-371 leaves run through typed pages 34 down to 25 in reverse scan order, while typed page 54 is separate in that sequence and the number-392 leaves show 4–27, 4–26, and 4–24. This physical evidence does not identify an exact published edition or prove that the representability argument uses the printed subject matter, and it is not a reason to reorder the transcription.

**Context search:** `RN071`; `title`, `folio`, `page`, `S19`, `tensor`.

**Context comparison:** `notes/RESULTS_STATE.md` → **MPL_33_002-049 §93**, source `MPL_33_002-049_notes.md` (T01–T04, no scan mapping supplied; methodological first-pass lead, original unavailable); `README.md`, Book I I.VI, rank 22 and **S19**, citing cote 131 scans 002–042; `notes/RESULTS_STATE.md` → **MPL_33_002-049 §2**, source `MPL_33_002-049_notes.md` (scan field truncated after “002…”, original unavailable); **adds actual local pagination evidence; the earlier title-inventory entry is methodological only and supplies no source identification for these leaves**.

### RN072 — The divisor class convention includes a sign

**Kind:** unpursued implication

**Location:** **131.pdf, scan 008**, definition of c(M); frozen page-file line 8; **131.pdf, scan 008**, Proposition 16(iii); frozen page-file line 17; **131.pdf, scan 010**, determinant display; frozen page-file line 6.

**Text:** “sera noté $-c(M)$”; “$c(T)=-c(\chi(T))$”.

The typed source fixes a sign when passing from the divisor of a torsion quotient to the class attached to a module. Any comparison with a determinant-line or divisor-class convention must preserve that sign and the orientation of the quotient, rather than normalize them to a more familiar formula. The height/lattice hunch in the context concerns a different construction and supplies no evidence that this sign convention is used in the handwritten representability proof.

**Context search:** `RN072`; `lattice`, `height`, `divis`, `determinant`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG H9**, source `WARGAME_MATH_HUNCHES_20261112.md` (cote 44, Th. 4–5; no scan supplied; unchecked height/lattice hunch, original unavailable); **adds a local convention check; no supported transfer to the Mordell–Weil height programme**.

### RN073 — The relative lattice invariant depends on omitted earlier hypotheses

**Kind:** unpursued implication

**Location:** **131.pdf, scan 021**, section heading; frozen page-file line 7; **131.pdf, scan 021**, opening of section 6; frozen page-file line 9.

**Text:** “Les notations et hypothèses sont celles des n°s 2 à 5”.

The typed leaf defines $\chi(M,M')$ from determinant lattices and records antisymmetry and a cyclic-sum identity. Its references to local principal rings and fractional ideals depend on earlier assumptions not reproduced in the retained leaves, so one should not recast it as a theorem over arbitrary domains. Nor does the use of divisor language identify it with the line-bundle families or divisorial correspondence functor in scan 017.

**Context search:** `RN073`; `lattice`, `divis`, `correspond`, `height`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG H9**, source `WARGAME_MATH_HUNCHES_20261112.md` (cote 44, Th. 4–5; no scan supplied; unchecked height/lattice hunch, original unavailable); `notes/RESULTS_STATE.md` → **WG2 §2.4 #4**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (cotes 47/44 named, no scan supplied; unchecked plan, original unavailable); **adds a source-scope limit and distinguishes two meanings of divisor data; the context does not contain the omitted hypotheses**.

### RN074 — The graded tensor-product calculation already checks associativity

**Kind:** unpursued implication

**Location:** **131.pdf, scan 013**, formula 17 and associativity calculation; frozen page-file line 6.

**Text:** “tout revient donc à vérifier l’identité”.

The printed calculation reduces associativity to the displayed multiplicative identity for $\varepsilon$ and then derives it from its two multiplicativity relations. Thus this is not an unresolved associativity claim in the handwritten representability notes, and the general $\varepsilon_{ij}$ should not be silently specialized to the usual sign rule. The context’s graded Lefschetz-ring plan shares vocabulary but supplies no statement identifying its operators or grading with this typed construction.

**Context search:** `RN074`; `graded`, `tensor`, `Lefschetz`, `grading`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); **records a completed calculation in a separate typed source; no demonstrated link to the unchecked graded-correspondence programme**.

### RN075 — The left side of printed formula 18 lacks a visible tensor factor

**Kind:** reading question

**Location:** **131.pdf, scan 013**, last display; frozen page-file line 31.

**Text:** Frozen display: “$\bigotimes_{i\in I}=\prod_{i\in I}h_i(x_i)$”.

The transcription preserves the tensor operator and index without supplying the absent visible operand. The surrounding calculation suggests $x_i$ as the expected tensor factors, but that is a mathematical reconstruction, not a verified character on this leaf. No contextual excerpt supplies the same formula or an independently identified source edition, so the proposed completion belongs only in this reading question.

**Context search:** `RN075`; `tensor`, `graded`, `Lefschetz`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); **adds a specific unresolved formula question; no corroborating textual witness is present in the context**.

### RN076 — The tensor-product chapter changes its unit convention

**Kind:** reading question

**Location:** **131.pdf, scan 034**, section-opening convention; frozen page-file line 9; **131.pdf, scan 026**, continuation heading; frozen page-file line 5.

**Text:** “n’ayant pas nécessairement d’élément unité”; later “ayant un élément unité”.

The definition on typed page 29 allows nonunital associative algebras, whereas the later universal-property section explicitly resumes the unital convention. A consolidated mathematical exposition must mark that change rather than treat every canonical inclusion $u_i$ as already available in the nonunital setting. The scanned sequence reverses the typed pagination, which makes the scope boundary especially easy to overlook.

**Context search:** `RN076`; `tensor`, `algebra`, `graded`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); **adds a convention and ordering check; the related planning vocabulary does not supply these definitions**.

### RN077 — The universal property requires commuting images

**Kind:** unpursued implication

**Location:** **131.pdf, scan 026**, universal-property statement; frozen page-file line 7; **131.pdf, scan 024**, continuation and commutative case; frozen page-file line 14.

**Text:** “soient permutables”; “problème d’application universelle”.

The universal property for the tensor product of associative algebras requires the images of different factors to commute. The final paragraph explains why this restriction is automatic for a commutative target, but it is not automatic for an arbitrary associative target. This distinction prevents reading the construction as the unrestricted coproduct of noncommutative algebras, and no such coproduct identification should be imported from the representability terminology elsewhere in the packet.

**Context search:** `RN077`; `tensor`, `algebra`, `representab`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); `README.md`, Book I I.VI, rank 22 and **S19**, citing cote 131 scans 002–042; `notes/RESULTS_STATE.md` → **MPL_33_002-049 §2**, source `MPL_33_002-049_notes.md` (scan field truncated after “002…”, original unavailable); **adds the exact universal-property scope; no common theorem with the manuscript’s scheme-valued representability is established**.

### RN078 — The final letter in the universal-property proof is uncertain

**Kind:** reading question

**Location:** **131.pdf, scan 026**, last paragraph before continuation; frozen page-file line 17.

**Text:** Frozen alternatives: “$v$ | $w$ est un homomorphisme d’algèbres”.

The preceding sentence constructs $w$, so $w$ would fit the proof, while the visible letter was retained with $v$ as the first reading. The continuation on scan 024 evaluates $w$, which strengthens the mathematical expectation but is not a second visual witness to the uncertain letter. The word forms “Soient $F$ une” and “quels que soit” likewise remain as written rather than being regularized from a printed edition.

**Context search:** `RN078`; `tensor`, `algebra`, `graded`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); **adds a proof-sensitive reading question and preserves the original spelling; the context has no resolving witness**.

### RN079 — The endomorphism tensor example uses “or”, not two projectivity assumptions

**Kind:** unproved claim

**Location:** **131.pdf, scan 028**, endomorphism example; frozen page-file line 17.

**Text:** “Lorsque $M$ ou $N$ est un $A$-module projectif de type fini”.

The typed source asserts the endomorphism-tensor map is an isomorphism when either one of the modules is finitely generated projective, and cites an earlier chapter for the proof. A verification can reduce that factor to a finite free module and then a direct summand, keeping the other module arbitrary; one should not silently strengthen the source to require both factors projective. The contextual Lefschetz endomorphism-ring programme concerns additional graded and geometric structure, so this elementary identity alone does not address its relations.

**Context search:** `RN079`; `endomorphism`, `tensor`, `Lefschetz`, `ring`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); **adds a precise hypothesis check; gives no new verification of the separate graded-ring plan**.

### RN080 — Tensor quotients use images of ideals without an unstated flatness hypothesis

**Kind:** unpursued implication

**Location:** **131.pdf, scan 030**, quotient tensor product; frozen page-file line 5; **131.pdf, scan 032**, ideal-image paragraph; frozen page-file line 23.

**Text:** “$\operatorname{Im}(a\otimes F)+\operatorname{Im}(E\otimes b)$”.

The quotient formula uses images of tensor products of ideals, which avoids asserting that the maps from those tensor products are injective. This matters if the algebraic identities are reused in a descent calculation, since tensoring an inclusion need not preserve injectivity without an appropriate flatness assumption. The source supplies a tensor-quotient identity, not an exactness theorem for arbitrary tensor factors or for the functor $F$ in the handwritten pages.

**Context search:** `RN080`; `tensor`, `exact`, `flat`, `descent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds an exactness limitation and prevents a false bridge between the typed tensor calculation and the functorial descent axioms**.

### RN081 — Routine verifications and the finite-family extension are expressly delegated

**Kind:** unproved claim

**Location:** **131.pdf, scan 028**, opening continuation; frozen page-file line 9; **131.pdf, scan 032**, finite-family paragraph; frozen page-file line 21.

**Text:** “Les vérifications sont triviales”; “laissant au lecteur le soin de les étendre”.

These are explicit proof omissions in the reused typed algebra material, not author-expressed uncertainty about the quasi-finite representability theorem. The first asks for compatibility of scalar-change identifications with multiplication, and the second delegates extension of the two-factor statements to finite families. They are indexed here and in the standing proof-omission table so that the task’s request to retain unproved assertions includes the reused leaves without misclassifying them as new conjectures.

**Context search:** `RN081`; `tensor`, `graded`, `unverified`, `flagged`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); `notes/RESULTS_STATE.md` → **MPL_33_098-146 §65**, source `MPL_33_098-146_notes.md` (no scan supplied; methodological first-pass lead, original unavailable); **adds source-specific delegated checks; the prior-note flag index is methodological only**.

### RN082 — Finite factorization makes the large monoid convolution meaningful

**Kind:** unproved claim

**Location:** **131.pdf, scan 040**, finite-factorization condition; frozen page-file line 13; **131.pdf, scan 038**, continuation proving associativity; frozen page-file line 5.

**Text:** “un nombre fini de couples”; “elle est associative”.

Condition (D) makes each coefficient of the convolution on $A^S$ a finite sum, and it also makes the triple-factorization sums in the next leaf finite. The displayed regrouping on scan 038 then proves associativity, completing the sentence broken at the end of scan 040. This is a proof continued in reverse typed-page order within the scanned packet, not an unresolved infinite-summation argument.

**Context search:** `RN082`; `monoid`, `formal`, `algebra`, `ring`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); `README.md`, Book I I.VI, rank 22 and **S19**, citing cote 131 scans 002–042; `notes/RESULTS_STATE.md` → **MPL_33_002-049 §2**, source `MPL_33_002-049_notes.md` (scan field truncated after “002…”, original unavailable); **adds the internal continuation and finiteness mechanism; no corresponding theorem is supplied by the broad context matches**.

### RN083 — Formal-series notation does not itself define an analytic sum or topology

**Kind:** unpursued implication

**Location:** **131.pdf, scan 038**, strict/large algebra distinction; frozen page-file line 11; **131.pdf, scan 036**, short continuation; frozen page-file line 5.

**Text:** “ne représente aucune opération algébrique”; “séries formelles de Dirichlet”.

The source explicitly distinguishes finite-support monoid algebras from unrestricted coefficient families and warns that its infinite summation notation is symbolic. The additive and multiplicative monoids of natural numbers yield the stated formal power-series and formal Dirichlet-series examples, but no topology or analytic convergence is supplied by this notation alone. Their occurrence on reused leaves therefore does not establish an arithmetic or local-symbol theme for the handwritten packet.

**Context search:** `RN083`; `formal`, `number`, `local symbols`, `height`.

**Context comparison:** `README.md`, Book I I.VI, rank 22 and **S19**, citing cote 131 scans 002–042; `notes/RESULTS_STATE.md` → **MPL_33_002-049 §2**, source `MPL_33_002-049_notes.md` (scan field truncated after “002…”, original unavailable); `notes/RESULTS_STATE.md` → **WG H9**, source `WARGAME_MATH_HUNCHES_20261112.md` (cote 44, Th. 4–5; no scan supplied; unchecked height/lattice hunch, original unavailable); **adds a precise negative limit on the preliminary arithmetic placement; the shared words do not create a research link**.

### RN084 — Own obstruction to applying large-monoid convolution to an infinite group

**Kind:** own idea

**Location:** **131.pdf, scan 040**, finite-factorization condition; frozen page-file line 13; **131.pdf, scan 038**, large algebra; frozen page-file line 11.

**Text:** “Pour tout $s$ … nombre fini de couples $(t,u)$”.

As an own elementary check, an infinite group fails (D), since a fixed $s$ has one factorization $s=t(t^{-1}s)$ for every group element $t$. Thus the unrestricted coefficient construction cannot be transferred directly to a profinite group with infinitely many elements; a completed group-algebra comparison with the arithmetic register would first require specifying support, topology, and limiting data. **Confidence: high for the obstruction**, because it is an immediate count of factorizations, but the proposed comparison remains unverified and makes no claim about a particular LM4 or LM7 result.

**Context search:** `RN084`; `profinite`, `group`, `ring`, `algebra`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); `notes/RESULTS_STATE.md` → **LM4 F.7**, source `LM4_FINITE_GROUP_ACTIONS_results.csv` (§30, folios 194–196, scans 383–387), and **LM7 E.23**, source `LM7_FERMAT_TOWER_results.csv` (§51.16, folios 733v–736v, scans 172–178; both open run claims, statements truncated, originals unavailable); **adds a methodological obstruction to a tempting cross-context analogy; no arithmetic result is rederived or contradicted**.

### RN085 — Free-monoid operators and quotient rings encode different data

**Kind:** unpursued implication

**Location:** **131.pdf, scan 042**, operator construction; frozen page-file line 3; **131.pdf, scan 040**, continuation with quotient ring; frozen page-file line 3.

**Text:** “monoïde libre”; “le noyau … est contenu dans l’annulateur”.

The typed construction first extends a family of operators to words and then linearly to the monoid algebra over the integers. The continuation permits passage to a quotient ring only when the proposed relations act trivially, explicitly phrased as containment in the module annihilator. Nothing here imposes continuity of a profinite action, geometric descent data, or the particular relations of the arithmetic groups in the context, so the universal-algebra mechanism alone does not address those open problems.

**Context search:** `RN085`; `group`, `operators`, `ring`, `profinite`, `descent`.

**Context comparison:** `notes/RESULTS_STATE.md` → **WG2 §2.1 #2**, source `PROGRAM_WARGAME_ROUND2_20261112.md` (visible scan range 3–18, attribution compressed; unchecked Lefschetz-ring plan, original unavailable); `notes/RESULTS_STATE.md` → **LM4 F.7**, source `LM4_FINITE_GROUP_ACTIONS_results.csv` (§30, folios 194–196, scans 383–387), and **LM7 E.23**, source `LM7_FERMAT_TOWER_results.csv` (§51.16, folios 733v–736v, scans 172–178; both open run claims, statements truncated, originals unavailable); **adds a scope distinction between algebraic operator encoding and the unrelated arithmetic-descent questions**.

## 7. Additional author requests and consequential readings

### RN086 — The first special-case sheet asks to combine two conditions

**Kind:** self-flagged

**Location:** **131.pdf, scan 003**, entire paragraph; frozen page-file line 2; **131.pdf, scan 016**, later specialization; frozen page-file line 12.

**Text:** “remplacer $5^\circ$ par la non ramification”; “bloquer $4^\circ$ et $5^\circ$”.

The early sheet requests a simpler single characterization of prorepresentable unramified functors, with the Artinian qualification inserted. The later corollaries carry the programme forward, but their changed numbering and surviving separate conditions do not by themselves prove that this requested optimal simplification has been achieved. A comparison should state whether the combined condition is left exactness plus rigidity, universal prorepresentability, or an equivalent restricted lifting criterion, rather than infer a unique answer from the heading.

**Context search:** `RN086`; `unramified`, `Artinian`, `prorepresent`, `conditions`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds the explicit early simplification request and its later continuation; no exact combined characterization is visible in the context**.

### RN087 — The proposed residue-field reduction is too overwritten to certify

**Kind:** reading question

**Location:** **131.pdf, scan 031**, right margin to condition 2; frozen page-file line 15.

**Text:** “il suffit de la vérifier pour …”.

The margin proposes restricting the prorepresentability test, but the displayed quotient is frozen with alternatives involving $A$ or $B$ and a maximal-ideal quotient. A reduction to residue fields alone would need a separate lifting or deformation argument, whereas a reduction to particular local Artinian thickenings would be a different statement. The available ink and register excerpt do not decide that distinction, so this is not used as a proved simplification of Proposition 2.

**Context search:** `RN087`; `prorepresent`, `Artinian`, `finite`, `field`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds an author-proposed reduction with unresolved test category; no exact contextual formula resolves it**.

### RN088 — The inserted source in condition C is not silently changed

**Kind:** reading question

**Location:** **131.pdf, scan 009**, insertion in condition C; frozen page-file line 25.

**Text:** Inserted “$S'$ imm. fermée … sur $S'$”.

The frozen insertion repeats $S'$ where the adjacent map and later lifting formulations might suggest a closed subscheme such as $X$ or $S'_0$. The mathematical context makes those alternatives tempting but does not determine whether the writer omitted a subscript or intended a different attachment. This ambiguity affects how the square-zero test is quantified, and it must be carried into any reconstruction rather than repaired in the transcription.

**Context search:** `RN088`; `unramified`, `nilpotent`, `conditions`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds an insertion-attachment/type question; the context supplies no independent text of condition C**.

### RN089 — The rotated NB proposes a combination whose wording remains uncertain

**Kind:** reading question

**Location:** **131.pdf, scan 012**, rotated NB; frozen page-file line 39.

**Text:** “8° et 9° peuvent se remplacer par une condition unique”.

The beginning clearly announces a combined replacement, but the subsequent wording about representability, modularity or promodularity, and base extension is too uncertain to state a complete equivalent axiom. The condition numbers on this sheet are themselves revised, so they cannot be mapped automatically to the main theorem’s 8 and 9 or to the later corollaries. The context’s polished summary may suggest an intended formulation, but no such reading has been imported into the frozen text or used to certify an equivalence.

**Context search:** `RN089`; `unramified`, `conditions`, `base`, `representability`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); **adds a specific uncompleted equivalence and numbering question; the provided excerpt is insufficient to settle it**.

### RN090 — The finite-subextension condition is visibly withdrawn

**Kind:** withdrawn in the same text

**Location:** **131.pdf, scan 012**, cancelled condition 6; frozen page-file line 18; **131.pdf, scan 012**, nearby live condition; frozen page-file line 20; **131.pdf, scan 035**, later definition; frozen page-file line 38.

**Text:** Cancelled “provient d’une sous-extension finie”.

The sheet cancels a separate finite-field-of-definition condition while retaining universal prorepresentability and revising the unramified test. This records a withdrawal of an explicit listed hypothesis, not a proof that every finiteness-of-definition issue can be discarded throughout the packet. The later local-modularity definition again contains a field-of-definition clause, so a reconstructed criterion must distinguish that clause from the cancelled pointwise finite-subextension assertion.

**Context search:** `RN090`; `field`, `finite`, `prorepresent`, `unramified`.

**Context comparison:** `notes/RESULTS_STATE.md` → **Hua, findings register, 131-unramified-and-etale-corollaries** (reported `131.pdf`, scans 012, 016–017; truncated register excerpt, underlying register unavailable); `notes/RESULTS_STATE.md` → **Hua, findings register, 131-locally-quasi-finite-representability** (reported `131.pdf`, scans 002–006, 014, 016; truncated register excerpt, underlying register unavailable); **adds a same-sheet withdrawal and its distinction from the later definition; no corresponding revision is recorded in the context head**.

## 8. Standing question: what the manuscript itself leaves to verify or formulate

The table separates an explicit question, a deferred proof, a requested formulation, and an announced application. These are documentary flags, not interchangeable assertions that the mathematics is false. No occurrence of the literal phrases “sauf erreur,” “je présume,” “admis,” or “il faudrait vérifier” was read in the retained transcription; the substantial flags here are the wording listed below, especially the question on scan 014 and the clarification bracket on scan 041. This index is additional to the individual notes, which preserve the context comparison for each item.

| Flag | File / scan and physical position | His words, briefly | Nature and current assessment | Individual note |
|---|---|---|---|---|
| SF01 | 131.pdf / 003, only paragraph | “remplacer $5^\circ$”; “bloquer $4^\circ$ et $5^\circ$” | Requested simpler unramified characterization; later corollaries do not by themselves certify the optimal combined axiom | RN086 |
| SF02 | 131.pdf / 005, top margin | “Dégager un lemme à cet effet” | Explicit missing lemma at the modularity transition | RN010 |
| SF03 | 131.pdf / 006, only paragraph | “vérifier la condition de constructibilité” | Identified remaining task for the local-to-global argument | RN012 |
| SF04 | 131.pdf / 012, upper marginal oval | “peut se formuler de façon … plus faible” | Proposed weaker generic nonextension formulation; intervening words uncertain | RN018 |
| SF05 | 131.pdf / 012, rotated NB | “8° et 9° peuvent se remplacer par une condition unique” | Proposed equivalence; subsequent wording and numbering uncertain | RN089 |
| SF06 | 131.pdf / 014, bracket within 7 | “on verra que cel implique: pro-modulaire” | Deferred comparison of modularity notions | RN010 |
| SF07 | 131.pdf / 014, diagonal NB | “On [fera résulter\|peut vérifier] … impliquent l’analogue de 7°” | Promised strengthening; verb and final restriction uncertain | RN023 |
| SF08 | 131.pdf / 014, lower margin | “Donner l’exemple-type … montrant que (8°) n’est pas surabondant” | Requested example; no such example is specified in the retained pages | RN022 |
| SF09 | 131.pdf / 014, same margin | “Est-ce que 7° est surabondant? Non” | Explicit question answered in shorthand with an uncertain qualification, without a displayed proof | RN021 |
| SF10 | 131.pdf / 016, upper margin | “Expliciter aussi le cas d’une immersion ouverte” | Requested special-case formulation; short proposal on scan 015 | RN024 |
| SF11 | 131.pdf / 016, lower margin | “Exprimer 8° ici par une impossibilité générique de prolonger” | Requested generic reformulation | RN018 |
| SF12 | 131.pdf / 017, Remarque 4 | “[Limitation] des anneaux $A,B$ et schémas $S'$” | Proposed reduction of test objects; initial word uncertain | RN026 |
| SF13 | 131.pdf / 017, lower heading | “Applications en vue.” | Both following applications are announced targets rather than proved on this page | RN038–RN041 |
| SF14 | 131.pdf / 031, right margin | “il suffit de la vérifier pour …” | Asserted test reduction, not a literal expression of doubt; displayed quotient unresolved | RN087 |
| SF15 | 131.pdf / 031, long margin | “Simplifier l’énoncé” | Requested alternative gluing statement with three proposed conditions | RN056 |
| SF16 | 131.pdf / 033, upper margin | “Transformer $4^\circ)$ sous une forme plus facile à vérifier” | Requested one-dimensional test for the open-overlap hypothesis | RN056 |
| SF17 | 131.pdf / 033, margin to Proposition 3 | “Transformer en une condition de modularité ``générique''” | Requested equivalence replacing constructibility | RN062 |
| SF18 | 131.pdf / 039, lemma margin | “Reprendre les conditions nécessaires sur $F$” | Explicit hypothesis audit for the relation lemma | RN064 |
| SF19 | 131.pdf / 041, middle bracket | “Préciser la signification de ce terme” | Explicit terminology task; proposed open-immersion meaning inserted | RN067 |

### Deferred or abbreviated proofs, distinguished from expressions of doubt

| File / scan | Wording | What is left to supply or where it is continued |
|---|---|---|
| 131.pdf / 004 | “cf. notes jointes, cor 2 à prop. 1” | Internal continuation in scans 029–031, with the Artinian test-category and finite-residue convention checked in RN008 and RN052; the separate complete-base effectivity issue occurs in RN053–RN054 |
| 131.pdf / 005–006 | “On utilise la prop 3 des notes jointes” | Proposition 3 and its later argument on scans 033–041; RN012 |
| 131.pdf / 007 | “je dis que (A) et (B) peuvent se remplacer” | Equivalence of formulations, not proved by this sentence; RN016 |
| 131.pdf / 009 | “On peut supposer en A resp. B” | Boxed closed-immersion/square-zero reduction; RN013 |
| 131.pdf / 014 | “en fait, étale suffit” | Comparison of the local conditions, retained as a claim within the theorem’s revision; RN010, RN023 |
| 131.pdf / 016 | “qui implique 7°” | (NR) to local modularity, with the density caveat; RN019–RN020 |
| 131.pdf / 028, reused typed | “Les vérifications sont triviales” | Multiplicative compatibility of scalar-change maps; RN081 |
| 131.pdf / 032, reused typed | “laissant au lecteur le soin de les étendre” | Two factors to arbitrary finite families; RN081 |
| 131.pdf / 040 → 038, reused typed | “Il est immédiat que la multiplica-” | Continues as a displayed finite-sum associativity calculation; RN082 |
| 131.pdf / 041 | “une autre proposition ``formelle''” | Open-chart gluing and coverage; RN068 |
| 131.pdf / 042, reused typed | “On vérifie sans peine”; “il est immédiat” | Module axioms and compatibility of the operator-ring construction; RN085 |

The substantive cancellations are separately identified as withdrawals in RN003, RN017, RN046, RN063, and RN090; each provides the relevant scan or pair of scans. Cancellations preserved in the transcription are not automatically claims later refuted mathematically.

## 9. Standing question: title sheets, headings, and page counts

**No cover or standalone title sheet and no explicit total-page-count statement were present among the 38 retained scans.** The catalogue title and approximate date, “Foncteurs représentables par schéma quasi fini : notes manuscrites (s.d.)”, “[vers 1971][119]”, are supplied metadata, not a title or date newly read on one of these images. Similarity to publications from the 1960s does not establish the manuscript’s date.

The table records every retained scan’s visible manuscript folio, separate typed pagination where present, and its principal titles or structural headings. A dash in the typed-page column means no separate typed pagination, not an unread page. Section and proposition labels are headings; numbers such as 371 and 392 are source marks, not counts of pages. The complete element inventory, including all NB labels and local subdivisions, is in `MPL_131_inventory.csv`.

| File / scan | Manuscript folio | Separate typed pagination / source mark | Title or principal structural heading actually present |
|---|---:|---|---|
| 131.pdf / 002 | A; 1 | — | Numbered conditions 1–8; marginal labels on exactness, finiteness, separation, modularity |
| 131.pdf / 003 | 2 | — | Bracketed, partly uncertain “Caractérisation des foncteurs proreprésentables non ramifiés” |
| 131.pdf / 004 | 3 | — | Numbered dimension-induction cases; NB |
| 131.pdf / 005 | 4 | — | “Lemme”; continuation of numbered proof cases |
| 131.pdf / 006 | 5 | — | No title; one continuation paragraph |
| 131.pdf / 007 | 6 | — | Conditions 7, 8, and $(D_1)$; NB |
| 131.pdf / 008 | 7 | 4–27; n° 392 | “PROPOSITION 16” |
| 131.pdf / 009 | 8 | — | “Axiomes”; “Cas particuliers”; marginal “Lemme” |
| 131.pdf / 010 | 9 | 4–26; n° 392 | “Exemple”; “7. Classes de diviseurs attachéesaux modules de type fini”; “PROPOSITION 15” |
| 131.pdf / 012 | 11 | — | Revised circled condition numbers; NB; “A bis” |
| 131.pdf / 013 | 12 | –54–; n° 371 | No section title; graded tensor calculation, formulas 17–18 |
| 131.pdf / 014 | 13 | — | “Théorème” |
| 131.pdf / 015 | 14 | — | “Immersion ouverte” |
| 131.pdf / 016 | 15 | — | “Corollaire 1”; “Corollaire 2”; “Remarque 3” |
| 131.pdf / 017 | 16 | — | “RG”; “Remarque 4”; “Exemples de foncteurs non ramifiés”; “Applications en vue.” |
| 131.pdf / 018 | 17 | — | Unfinished “Façon d’exprimer” |
| 131.pdf / 020 | 19 | — | No title; diagonal argument beginning “En effet” |
| 131.pdf / 021 | 20 | 4–24; n° 392 | “6. Invariant relatif de deux réseaux.” |
| 131.pdf / 023 | 22 | — | Deleted “Lemme”, inserted “Proposition 1”; “Dém” |
| 131.pdf / 024 | 23 | –34–; n° 371 | “COROLLAIRE” in the universal-property continuation |
| 131.pdf / 025 | 24 | — | “Corollaire 1”; a separate cancelled marginal “Corollaire” |
| 131.pdf / 026 | 25 | –33–; n° 371 | “PROPOSITION 5” |
| 131.pdf / 027 | 26 | — | Numbered injectivity and surjectivity proof steps |
| 131.pdf / 028 | 27 | –32–; n° 371 | “Exemples de produits tensoriels d’algèbres”; “2. Caractérisation universelle des produits tensoriels d’algèbres.” |
| 131.pdf / 029 | 28 | — | “N.B.”; “Corollaire 2” |
| 131.pdf / 030 | 29 | –31–; n° 371 | “PROPOSITION 1”; “COROLLAIRE 1”, “2”, “3”; “PROPOSITION 2”, “3”, “4” |
| 131.pdf / 031 | 30 | — | Cancelled “Prop.” and “Corollaire 3”; live “Proposition 2” |
| 131.pdf / 032 | 31 | –30–; n° 371 | No new section title; continuation of tensor-product definition and properties |
| 131.pdf / 033 | 32 | — | “Prop. 3” |
| 131.pdf / 034 | 33 | –29–; n° 371 | “§ 2. Produits tensoriels d’algèbres”; “1. Produit tensoriel d’un nombre fini d’algèbres”; “DEFINITION 1” |
| 131.pdf / 035 | 34 | — | “N.B.”; definition of local modularity and final field-of-definition NB |
| 131.pdf / 036 | 35 | –28–; n° 371 | No title; end of formal-series paragraph and typographic separator |
| 131.pdf / 037 | 36 | — | “Re N.B.”; “Preuve prop. 3” |
| 131.pdf / 038 | 37 | –27–; n° 371 | No new heading; large-monoid-algebra definition and examples |
| 131.pdf / 039 | 38 | — | Cancelled preliminary gluing paragraph; live “Lemme” |
| 131.pdf / 040 | 39 | –26–; n° 371 | “12. Exemples d’algèbres : VI. Algèbre large d’un monoïde.” |
| 131.pdf / 041 | 40 | — | No title; final globalization paragraph with terminology bracket |
| 131.pdf / 042 | 41 | –25–; n° 371 | No new heading; free-monoid/operator construction |

The retained numbered folios run from 1 to 41 with 10, 18, and 21 absent from these images; the task identifies their corresponding scans 011, 019, and 022 as blank and omitted. The additional “A” on scan 002 is a visible mark, not an extra retained page. Inventory classifications are 23 `text`, 14 `reused_typed`, and one `cancelled_draft` (scan 039, which also contains live continuation text); none is `cover`.

**Context comparison for this standing inventory:** searches for `title`, `page`, `folio`, and `S19` in the two context documents lead to README’s supplied catalogue metadata and the methodological entries MPL_33_002-049 §93 and §2 in `RESULTS_STATE.md`; their underlying source `MPL_33_002-049_notes.md` is unavailable and gives no matching cote-131 foliation. The table above therefore adds new local evidence rather than repeating an earlier title inventory.

## 10. Explicit disposition of the planning questions and prior findings

| Context question / ID | Disposition for this package | Evidence |
|---|---|---|
| Book I I.VI, rank 22: descent and representable functors | **Confirmed** as the core handwritten subject | Scans 002–007, 014–016, 023–041; RN001–RN029, RN043–RN070 |
| Hom and related construction techniques | **Confirmed** as announced applications | Scan 017; RN030–RN042 |
| Hilbert in the chapter description | **Indirect relevance only** | The manuscript does not construct a Hilbert scheme; the checked Picard literature supplies a projective-method comparison, not evidence of such a construction on these sheets |
| Heights and local symbols | **No supporting handwritten treatment found** | The lattice/divisor leaves are reused typed material; RN071–RN073, RN083 |
| Étale cohomology | **No supporting cohomological treatment found** | Étale means a morphism/functor property here; no cohomology theory is developed in the retained argument; RN001 |
| S19, residue of Book I | **Addressed within the supplied specification** | Print/Stacks comparison, two standing inventories, explicit outstanding steps; the full planning document was not supplied |
| Hua, findings register, 131-locally-quasi-finite-representability | **Direct overlap confirmed; status qualified** | Main theorem and induction match the topic, but the exact general variant and revised hypotheses require further audit; RN002, RN009–RN012, RN046–RN054 |
| Hua, findings register, 131-unramified-and-etale-corollaries | **Direct overlap confirmed; blanket closure not certified** | Distinct corollary lists, retained condition 8, unfinished margin tasks, and conditional density issue; RN003, RN018–RN026, RN030–RN042 |
| LM1 D.11, open integral descent | **Possible method only; no solution claimed** | Conditional recognition-lemma transfer, with missing data explicitly listed; RN070 |
| WG2 §2.3 #13, algebraic representatives | **Possible comparison of different moduli problems** | RN032, RN040, RN042; no transfer theorem established |
| Other arithmetic section, GT, CM, good-reduction, Fourier, and Lefschetz items | **No demonstrated manuscript-specific implication in supplied excerpts** | Full ID-by-ID dispositions in `records/context_register_coverage.md`; thematic or same-word hits are not proofs |

No settled-status register entry has been re-proved here as though it were open, and no open item is declared solved on the basis of a vocabulary match. Context excerpts that are incomplete remain incomplete in this assessment; missing statements, scans, and review qualifications have not been reconstructed.

## 11. References and verification scope

### Manuscript and supplied context

Grothendieck, A. (n.d.). *[Notes on representability; Montpellier cote 131]* [Unpublished manuscript and reused typed leaves, catalogue filename 131.pdf]. User-supplied scans 002–042, excluding 011, 019, and 022. The bracketed title is descriptive, not a title transcribed from a cover; catalogue dating and ordering are not independently verified here.

*README.md*. (2026). [User-supplied task-context document, MPL_131_context.zip]. See the Book I I.VI, rank 22, and S19 placement. Author and full parent planning document are not supplied.

*RESULTS_STATE.md*. (2026, November 15). [User-supplied context register, MPL_131_context.zip/notes]. Citations to LM, Hua, WG, and prior-package identifiers above refer to the visible excerpts here. The underlying files and full statements are unavailable; the scope and status of each excerpt are recorded in `records/context_register_coverage.md`.

### Primary published comparisons

Deligne, P. (1985). Le lemme de Gabber. *Astérisque, 127*, 131–150. https://www.numdam.org/item/AST_1985__127__131_0.pdf

Grothendieck, A. (1962). Technique de descente et théorèmes d’existence en géométrie algébrique. V. Les schémas de Picard: Théorèmes d’existence. *Séminaire Bourbaki, 7*, Exposé 232, 143–161. https://www.numdam.org/article/SB_1961-1962__7__143_0.pdf

Grothendieck, A. (1970). Critères de représentabilité. Applications aux sous-groupes de type multiplicatif des schémas en groupes affines (Exposé XI). In M. Demazure & A. Grothendieck (Eds.), *Schémas en groupes I: Propriétés générales des schémas en groupes* (Lecture Notes in Mathematics, Vol. 153). Springer. https://wstein.org/sga/SGA3/Expo11.pdf

Murre, J. P. (1964). On contravariant functors from the category of preschemes over a field into the category of abelian groups (with an application to the Picard functor). *Publications Mathématiques de l’IHÉS, 23*, 5–43. https://www.numdam.org/item/PMIHES_1964__23__5_0.pdf

Murre, J. P. (1966). Representation of unramified functors. Applications. *Séminaire Bourbaki, 9*, Exposé 294, 243–261. https://www.numdam.org/article/SB_1964-1966__9__243_0.pdf

Schlessinger, M. (1968). Functors of Artin rings. *Transactions of the American Mathematical Society, 130*(2), 208–222. https://doi.org/10.1090/S0002-9947-1968-0217093-3 — consulted full text: https://math.uchicago.edu/~amathew/schlessingerdef.pdf

**Verification locators.** Deligne: §1.1(c), p. 131, with standing conventions on p. 132; FGA V: Corollary and Remark 6.6, pp. 159–160; SGA 3 XI: Proposition 3.5 and §6.6; Murre 1964: introduction and II.15, Theorem 2, pp. 42–43; Murre 1966: F7, Theorem 1, Corollary 2, §2 Lemma 1, Proposition 1, and the announcement on p. 247; Schlessinger: Theorem 2.11. The SGA 3 URL supplies the French retypesetting dated 5 December 2008, not an inspected first-edition scan. Murre’s Exposé 294 was delivered in May 1965 and credits unpublished results of Grothendieck; the cited collected-volume year is 1966. No manuscript date is inferred from that relationship.

### Stacks Project: individually checked stable locators

The Stacks Project Authors. (2026). *The Stacks Project*. Retrieved November 16, 2026, from the stable tag URLs below. The tag, rather than a mutable section number, identifies the result used in each note.

| Tag and direct URL | Consulted result or limited role | Notes |
|---|---|---|
| [00MC](https://stacks.math.columbia.edu/tag/00MC) | Faithful flatness of Noetherian completion with the stated Jacobson-radical hypothesis | RN050 |
| [01I1](https://stacks.math.columbia.edu/tag/01I1) | Contravariant correspondence between affine morphisms and ring homomorphisms | RN058 |
| [01JJ](https://stacks.math.columbia.edu/tag/01JJ) | Representability by gluing a sheaf covered by representable open subfunctors | RN068 |
| [01TF](https://stacks.math.columbia.edu/tag/01TF) | Closed fibre points and finite residue extensions for locally finite-type morphisms | RN043 |
| [01ZC](https://stacks.math.columbia.edu/tag/01ZC) | Local finite presentation and directed affine-limit compatibility | RN044, RN049 |
| [023Q](https://stacks.math.columbia.edu/tag/023Q) | Representable functors satisfy fpqc descent | RN050 |
| [024R](https://stacks.math.columbia.edu/tag/024R) | Formal and ordinary unramifiedness under the stated local finiteness hypotheses | Auxiliary source check; the notes do not apply it to an unrepresented functor |
| [025G](https://stacks.math.columbia.edu/tag/025G) | Open-immersion criteria, including étale monomorphisms | RN024, RN028, RN059 |
| [02HM](https://stacks.math.columbia.edu/tag/02HM) | Étale equals locally finitely presented and formally étale | RN013, RN015–RN016 |
| [02W8](https://stacks.math.columbia.edu/tag/02W8) | Effective **fppf** descent of separated locally quasi-finite schemes | RN011; not used alone for completion descent |
| [0325](https://stacks.math.columbia.edu/tag/0325) | Finite algebras over complete Noetherian local rings decompose into complete local factors | RN053 |
| [03FN](https://stacks.math.columbia.edu/tag/03FN) | A quotient with locally isomorphic projections that is not a scheme | RN069; diagnostic example, not a counterexample to all manuscript hypotheses |
| [052F](https://stacks.math.columbia.edu/tag/052F) | Flattening definitions and the formal-flatness counterexample | RN035 |
| [053X](https://stacks.math.columbia.edu/tag/053X) | Noetherian constructibility and generic-open-subset tests | RN014 |
| [0542](https://stacks.math.columbia.edu/tag/0542) | Constructibility plus generization stability implies openness in the stated setting | RN014 |
| [05UH](https://stacks.math.columbia.edu/tag/05UH) | Universal flattening for a proper finitely presented morphism and a finitely presented module | RN035 |
| [081E](https://stacks.math.columbia.edu/tag/081E), with [081D](https://stacks.math.columbia.edu/tag/081D) | Eventual isomorphism and the precise inverse-limit and finite-presentation hypotheses | RN066 |
| [0903](https://stacks.math.columbia.edu/tag/0903) | Openness from constructible-topology openness and generization stability in spectral spaces | RN061 |
| [0AP9](https://stacks.math.columbia.edu/tag/0AP9) | Separated locally quasi-finite morphisms are ind-quasi-affine | RN011 |
| [0APK](https://stacks.math.columbia.edu/tag/0APK) | Effective fpqc descent in the ind-quasi-affine class | RN011 |
| [0AQG](https://stacks.math.columbia.edu/tag/0AQG) | Comparison of maps from a complete-local spectrum and formal spectrum to an existing scheme | RN048 |
| [0D2C](https://stacks.math.columbia.edu/tag/0D2C) | Picard algebraic-space representability under properness, flatness, finite presentation, and universal structure-sheaf pushforward isomorphism | RN041 |
| [0E0D](https://stacks.math.columbia.edu/tag/0E0D) | Finite étale Stein factor under properness, flatness, finite presentation, and geometrically reduced fibres | RN036 |

### Indirectly identified dependency, not verified theorem text

Raynaud, M. (1970). *Faisceaux amples sur les schémas en groupes et les espaces homogènes* (Lecture Notes in Mathematics, Vol. 119). Springer. Chapter XI, Theorem 1.4 is the dependency identified through Deligne (1985); its original statement was not directly read and is not used here as independently checked evidence for the manuscript’s full projectivity wording.

### Limits of the literature audit

The references establish the particular comparisons stated in the notes. They do not establish completeness of the bibliography, priority, a new theorem, or a proof of all revised quasi-finite hypotheses. Where only a modern analogue, a narrower theorem, an indirect citation, or a possible research transfer is available, that distinction is stated at the relevant note. Source pages and supplied context documents themselves are not bundled in this ZIP.
