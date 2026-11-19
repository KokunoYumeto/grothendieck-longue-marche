# Context research memo — SP31 cote 156-3

Prepared by `/root/context_links`, GPT-6 Astra Pro, reasoning effort not exposed. The transcription was already frozen at 2026-11-19 21:46:48 UTC. This worker read only the supplied text files and the frozen transcription: no scan images, no witness C notes, no TeX edits, no outside literature. This memo supplies context comparisons for the primary reader; it is not the final page-by-page research apparatus.

## Source and status discipline

`SP31_CW_156-3_context/README.md` identifies one packet covering all current scans. `MPL_156-3/README.md` says that S14 and B10 are planning guesses made before these pages were read, and that the *Esquisse* transcription was not checked by eye. In the references below, **Esquisse** means `SP31_CW_156-3_context/Esquisse_cote119_copy1_API_transcription.tex`; `119/nn` is that file's exact `\scanpage` tag, not a converted PDF number.

`notes/RESULTS_STATE.md` describes its register statuses as claims of earlier runs unless explicitly refereed. The specifically refereed LM4/LM7 rows named in its introduction are not the results pertinent to these pages; the finite-poset, stratification and exit entries used below remain register claims here. No claim has been promoted to reviewed or established by this contextual comparison. Source files named in the register but not present in the packet were not consulted.

After joining line-end hyphenation, searches find no occurrence of réseau, tronçon, biordre or pro-objet in the supplied Esquisse; the one découpage hit is cellular cutting in 119/11. Therefore its connections to 156-3 are programmatic or structural, not an earlier definition of the current objects. The exact patterns and counts are in `context_search.tsv`.

## Precise context anchors

### CTX-A01 — Canonical reconstruction, with pieces and attachment data

**Esquisse §5, 119/27–30.** At 119/27 the goal is to reconstruct stratified structures from “pièces de construction”; 119/28 introduces the two-stratum pair and a tubular neighborhood; 119/29 gives the attachment map and the pushout expression for X from U and Y. The passage adds attachment data and discusses noncanonical choices, whereas 156-3/002–006 starts from moderate pairs, complement partitions and finite boundaries; these are related reconstruction aims, not identical definitions. **Register links:** `EXIT_ONE_TYPE P1d1`, `EXIT_ONE_TYPE P4e`, `MPL_121_049-073+153+155 R121-08`, all carried as leads/claims.

### CTX-A02 — Axioms are provisional, and a concrete test matters

**Esquisse §5, 119/32–34.** The text calls its approach “axiomatique,” contemplates multiple moderate theories, and at 119/34 calls its system “plausible provisoire,” without claiming the comparison theorem has been proved from it. This is a close methodological parallel to “Axiomes provisoires” in 156-3/004, the possibly provisional finiteness assumptions in /006, the request for intrinsic conditions in /017, and the failed topology experiment in /023–025. **Register links:** `MPL_150_044-084 Q9`, `WG2 B15 (§1.2)`; neither entry settles the new cut axioms.

### CTX-A03 — Flags index an enriched reconstruction system

**Esquisse §5, 119/36–37.** At 119/36 the system is indexed by Drap(I), the flags of the poset indexing the strata, but depends on additional local retractions and includes embeddings and proper fibrations; at 119/37 multiplicities require an essentially finite category of indices. This differs from 156-3/010–016, where Drap(L) denotes chains of lieux and the argument reconstructs an order up to reversal from binary/ternary data. **Register links:** `STRATA A.4`, `STRATA B.1`, `EXIT_ONE_TYPE P1d1`, `MPL_150_044-084 Q2`; the common flag vocabulary does not identify the constructions.

### CTX-A04 — Pair data may require genuine triple composition data

**Esquisse note (7), 119/58–59.** The supplied text says that deployed strata and pairwise tubes suffice in the space case, but in the multiplicity case requires triple junction spaces and a map to the long-edge tube; the NB at 119/58 expressly says that the latter map is not determined by the two adjoining tubes alone. At 119/59 the result is an ordered object or, for multiplicities, a category object whose composition is supplied by those triple maps. This is a useful contrast to 156-3/004 and /011–017: binary cut partitions reconstruct the special order data under the manuscript's hypotheses, but this does not prove a general binary-data reconstruction of stratified spaces. **Register links:** `EXIT_ONE_TYPE P4e`, `STRATA B.1`, `MPL_150_044-084 N18`.

### CTX-A05 — Topological and combinatorial components must be separated

**Esquisse §3, 119/12; §5, 119/28–29.** The early dessin passage explicitly uses components of the complements of an embedded complex as open cells; the later gluing passage retains boundary and fibration data. In 156-3/003 the partitions R_T are primitive data, while /007 and /011 call interval pieces components before the canonical topology is introduced; /019 therefore cannot be interpreted as a theorem about ordinary topological connected components merely from the terminology. **Register links:** `PATHS E.10`, `EXIT_ONE_TYPE P4e` offer warnings about information lost by component-only descriptions; those are background analogies, not proofs of a counterexample here.

### CTX-A06 — “Boundary” has several roles

**Esquisse §5, 119/28–29 and 119/35.** The boundary of a chosen tubular neighborhood is part of an attachment construction; at 119/35 the text explicitly discusses a “bord” even when there is no manifold-with-boundary structure. This is a useful comparison with the warning on relative versus absolute frontier in 156-3/018 and the crossed boundary definition on /025, but it does not identify the topological frontier with the finite endpoint set of an arbitrary tronçon. **Register links:** `EXIT_ONE_TYPE P1a1`, `MPL_150_001-043 Q1b`, carried only as leads.

### CTX-A07 — Comparison of theories is stronger than an object-level encoding

**Esquisse §5, 119/33; §6, 119/41.** The comparison goal concerns components, and then the full homotopy type, of isomorphism spaces; 119/41 distinguishes 0-isotopic categories from infinity-isotopic ones and stresses contractibility of choices. The cut-partition reconstruction in 156-3/012–016 is about recovering an order/biorder on a fixed set; it supplies no isomorphism-space or mapping-space comparison. **Register links:** `MPL_121_001-048 Q4.3`, `MPL_151_032-075 Q4-03`, `MPL_150_044-084 N37`; none should be silently imported as a consequence of these pages.

### CTX-A08 — Compact PL comparison is a different assertion

**Esquisse note (6), 119/57–58.** The note claims equality of isomorphism classes of compact moderate spaces with those of the piecewise linear theory, while §5, 119/33 distinguishes the stronger isotopy and homotopy-level expectations. The supplied context register has related claims `MPL_150_001-043 Q4b`, `MPL_150_085-099+151_001-031 K02`, `MPL_151_032-075 Q4-02`, and `MPL_150_044-084 T05`; their underlying literature was not checked in this run. Nothing in 156-3/002–025 proves a compact PL theorem or a passage from these cut data to finite-category homotopy types.

### CTX-A09 — Order and topology require an explicit variance convention

**Esquisse note (7), 119/59; 156-3/022–024.** The Esquisse describes an internal ordered object built from deployed strata and tubes, whereas /022–024 are investigating a topology on the set of lieux itself and the relation of singleton closures to inclusion. `STRATA 0.1`, `STRATA A.4`, `STRATA A.12`, and `WG2 B15 (§1.2)` concern downset topologies/minimum-vertex realizations with stated variance; they do not make the canonical interval topology here automatically Alexandrov. A useful note should specify the order and topology before applying any finite-poset dictionary.

### CTX-A10 — “Forms” names an intuition, not the proposed finite-cut definition

**Esquisse §5, 119/31–32.** The text speaks of the “propriétés topologiques” of “formes géométriques” and seeks a context able to express the “intuition topologique des formes.” These phrases motivate the foundational project; they do not define a form as a pro-object of cuts or finite categories. The packet README's S14 therefore remains a later planning guess to test against 156-3/002–025, rather than an explicit definition inherited from this Esquisse passage. **Register links:** S14 and `MPL_150_044-084 Q9`, retained as planning/background only.

## Context-search map covering every supplied scan

Each row is a candidate connection for the primary reader, not a substitute for the page's own mathematical notes.

| Current scan | Objects searched / strongest anchor | Relation to context; relevant register IDs |
|---|---|---|
| 002 | networks, moderate pairs, new axioms; Esquisse 119/27,32 | Adds a concrete pair-based axiom proposal to the broad reconstruction program; S14 from packet README, `WG2 B15 (§1.2)`. |
| 003 | moderate complement, partitions, components; 119/12,28–29 | Differs from actual topological component decompositions; `PATHS E.10`, `EXIT_ONE_TYPE P4e` as cautions. |
| 004 | recover boundary and all cuts from pair cuts; 119/58–59 | A special low-arity reconstruction expectation, contrasted with explicit triple composition data; `EXIT_ONE_TYPE P4e`, `STRATA B.1`. |
| 005 | discrete network, maximal finite cut; 119/34 | New concrete provisional axiom, not a consequence of general tame triangulability; `MPL_150_044-084 Q9`. |
| 006 | finiteness and cut refinement; 119/36–37 | Supplies finite component sets and containment transitions, but no complete reconstruction equivalence; S14, `STRATA A.4`, `WG2 B15 (§1.2)`. |
| 007 | ordered line, finite chain cuts, n+1 pieces; 119/12 | Provides an order-theoretic model, not a claim that every named component is topologically connected; `PATHS E.10`. |
| 008 | opposite order, interval pieces, finite union; 119/28–29 | Changes the kind of reconstruction data: finite endpoint sets versus tubular gluing maps; `EXIT_ONE_TYPE P4e`. |
| 009 | local/global directedness and density; 119/32–34 | A new specialized axiom system; no matching tronçon definition in Esquisse; `MPL_150_044-084 Q9`. |
| 010 | flags, boundary, order duality; 119/36 | Same flag terminology in a different indexing role; `STRATA A.4`, `WG2 B15 (§1.2)`. |
| 011 | biorder recovered from pair cuts; 119/58–59 | Directly bears on Hua findings `156-3-betweenness-from-cuts`; general gluing analogy is limited. |
| 012 | strict betweenness, comparability, divisibility; 119/36 and RESULTS_STATE findings | Directly bears on Hua findings `156-3-order-from-betweenness`; Esquisse supplies no proof of this order theorem. |
| 013 | oriented pair and order reconstruction; same context | Adds the actual orientation-and-comparison construction behind `156-3-order-from-betweenness`. |
| 014 | four-variable finite lemma and proof; same context | Supplies a local proof step and dependence on density/directedness; `156-3-order-from-betweenness`. |
| 015 | pair complement partitions recover ternary relation; 119/58–59 | Directly bears on `156-3-betweenness-from-cuts`; not a theorem about all stratified reconstruction data. |
| 016 | intersection test and divisibility; same context | Adds the middle-element criterion and explicit density use; `156-3-betweenness-from-cuts`. |
| 017 | intrinsic axiom task, maximal subcategory; 119/34,59 | Restates the need for axioms in a concrete order problem; `MPL_150_044-084 Q9`, S14. |
| 018 | relative/absolute frontier, intersections, topology; 119/35 | Distinguishes two boundary roles; `EXIT_ONE_TYPE P1a1` is a background contrast, not a proof here. |
| 019 | finite disjoint decomposition, uniqueness, components; 119/12,36 | Adds a uniqueness claim for finite order pieces; component interpretation needs checking; `PATHS E.10`, S14. |
| 020 | meets, moderate joins, failure of universal closure; 119/31–32 | Concrete test of stability under operations, analogous to Esquisse's concern but different in scope; `MPL_150_044-084 Q9`. |
| 021 | moderate difference, locally closed pieces; 119/28–30 | Formal analogue of cutting a closed piece from an ambient one; no tubular/fibration data supplied; `EXIT_ONE_TYPE P4e`. |
| 022 | canonical topology, singleton closure and inclusion; 119/59 | Potential order/topology comparison requires explicit variance; `STRATA 0.1`, `WG2 B15 (§1.2)`. |
| 023 | T0, sobriety, alternate closed-set topology; 119/33–34 | A new obstruction/question for a topology choice, not settled by tame comparison; `WG2 B15 (§1.2)`. |
| 024 | supremum topology and failed closure attempt; 119/34 | Provides a concrete failure to preserve the desired interval behavior; `MPL_150_044-084 Q9`. |
| 025 | revert to original topology, terminological closedness; 119/32–34 | A local choice of working context, with boundary draft withdrawn; S14 remains unproved. |

## S14 and B10: what this packet does and does not support

**S14 has partial motivation, not a theorem.** Scans 002–006 introduce cut sets, finite complement classes and boundary incidence, and /011–016 reconstruct order data from pair cuts. These are genuine ingredients for a finite-data encoding. They do not define a pro-object, prove that the index is cofiltered, construct a realization functor, or identify an original topological form with its reconstruction; /017 explicitly leaves intrinsic axioms open and /023–025 show topology is still under revision.

**B10 is not established by these scans.** The compact tame/PL statement appears as an earlier programmatic assertion in Esquisse note (6), 119/57–58, and as claims in the supplied register. Current pages contain neither a compactness hypothesis nor triangulations nor the comparison of isomorphism spaces required to make that bridge. A finite collection of cut components by itself also does not determine all higher attachment data: this is already the caution of Esquisse note (7), 119/58–59, and of register claim `EXIT_ONE_TYPE P4e`.

**Open-register scope.** No direct solution or concrete advance to the nine explicitly open entries listed at the start of RESULTS_STATE (LM4 C.12; RESIDUE E.6, C.8, F.6, I.7, J.2, J.3; EXIT_ONE_TYPE P3c-general; PATHS C.10) has been established by this context check. They should not be cited merely because they contain words such as poset, strata or category.

## Own-idea candidates, bounded and explicitly labeled

### CTX-OWN1 — The naive cut index is not automatically a pro-index

**Own idea / conditional obstruction; confidence high.** For the ordered model, finite moderate subsets are finite chains (156-3/007,010); if u and v are incomparable, the singleton cuts {u} and {v} admit no common upper bound in this inclusion poset, since a chain cannot contain both. Thus reversing the finite-chain refinement order does not automatically give the cofiltered category needed for the naive S14 pro-object, despite Dec1–Dec2's finite component sets and containment maps. This does not refute S14: a larger category of cuttings, a compatibility restriction, or another construction could resolve the obstruction. **Context:** packet README S14, Esquisse 119/36–37; **IDs:** `WG2 B15 (§1.2)`, `STRATA A.4` as background only.

**Reason/check:** This is a direct order-theoretic implication from the definition of chain, checked here; it does not rely on an outside theorem or a register result. No assertion is made that a pro-object must use exactly this index or that the broad S14 proposal is false.

### CTX-OWN2 — Separate a reconstruction theorem from an intrinsic realization theorem

**Own idea / research test; confidence medium.** The argument of 156-3/012–016 reconstructs order data when the given partitions already come from a tronçon; the task on /017 asks which abstract input relations and partitions arise this way. An explicit test family should therefore separate orientation reconstruction from the coherence conditions on overlapping pair cuts, with the four-point lemma of /014 as one local check rather than as a complete existence criterion. **Context:** Esquisse 119/58–59 distinguishes pair tubes from extra triple composition maps; **IDs:** Hua findings `156-3-order-from-betweenness`, `156-3-betweenness-from-cuts`, `EXIT_ONE_TYPE P4e`.

**Reason/limit:** The manuscript itself separates recovery from axiomatization, and the context shows why low-arity data can require compatibility beyond their individual pieces. No sufficiency or novelty is claimed for the proposed test; the Esquisse comparison is an analogy across different constructions.
