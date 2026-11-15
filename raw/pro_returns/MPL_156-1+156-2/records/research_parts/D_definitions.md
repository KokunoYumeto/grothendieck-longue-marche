# Research notes: Montpellier 156-1 and 156-2

## Scope, evidence, and answer to the proposed interpretation

These notes concern the 27 supplied scans of cote 156-1 followed by the 19 supplied scans of cote 156-2; a source written 156-1/023 means scan 23 of that cote, not either of its manuscript foliation sequences. All source quotations refer to the frozen diplomatic transcription; an uncertain reading remains uncertain here, and mathematical objections or proposed repairs have not been put back into the transcription. Individual notes have one to four substantive sentences, followed by separate source, classification, confidence where applicable, and context-search metadata.

**The proposed definition is not confirmed by these pages.** The manuscript starts a recursive geometry of forms, explicitly defines a zero-dimensional form, develops an evolving one-dimensional segment structure called a network, and studies spaces with marked ends that can be cut and reglued. It does not define a general form as a pro-object, give a category of finite refinements, prove those refinements cofiltered, or prove that finite incidence data determine a tame space. Its finite decompositions retain actual topological pieces and endpoint homeomorphisms; the genuinely profinite construction available from the later Boolean algebra of rives is a local invariant of a closed subset, with a substantially different meaning.

The supplied context consists of README.md and notes/RESULTS_STATE.md. The earlier manuscripts, research returns, intake files, and planning documents named in that register were not supplied, so comparisons below are comparisons with their recorded summaries, not independent verifications of those earlier proofs or readings. “Proved,” “Refuted,” and “Known” below describe the register's own status; unless expressly stated otherwise they are claims of earlier model runs, first-pass manuscript notes are leads, intake readings are not referee verdicts, and war-game entries are unchecked plans. The README explicitly says its proposed interpretation was guessed from the titles before the pages were read.

The search phrases printed after each numbered note were searched against both supplied context files; the exact queries and returned lines are preserved in records/research_context_searches.json. A missing direct match means absence from this small supplied context, not absence from the whole archive or literature. Modern comparisons are separately identified and cited in the APA bibliography; none establishes historical dependence or novelty.

## D. Definitions and their limits

### D01 — “Form” has a complete definition here only in dimension zero

**Source:** 156-1/002, opening paragraphs and margin. **Kind:** unpursued implication. **Quote:** “construction récurrente”; “forme de dim 0”; “La forme du modèle est l'ens quotient” (the linking word is uncertain in the transcription).

A zero-dimensional form is a discrete set whose elements are its lieux, while a model of such a form is a set L with an equivalence relation called “non disjoints,” and the associated form is the quotient set. The opening proposal is recursive in the dimension, but these scans do not complete the higher-dimensional recursion or define a category of arbitrary forms. Consequently the distinction between a form and its model is explicit at dimension zero and should not be erased when interpreting the later one-dimensional models.

**Context:** search: forme|dimension|quotient|B15; bears on WG2 B15 (§1.2) and WG2 §3.1 #2, unchecked planning entries with no source scan for this definition: these pages add an actual definition and restrict the title-based guess rather than prove its pro-object interpretation.

### D02 — The basic data of a one-dimensional model

**Source:** 156-1/004 and 006; earlier cancelled proposal at 002–003. **Kind:** unpursued implication. **Quote:** “ensemble des lieux”; “ensemble des segments”; “lieux intérieurs au segment.”

The revised data are sets L and S, a support map I↦Ĩ from S to the subsets of L, and an endpoint map δ assigning a two-element subset δI⊂Ĩ to each segment. Its interior is Ĩ°=Ĩ∖δI, regular lieux form Lr=⋃I Ĩ°, and the complementary lieux Ls are singular, critical, or branching. These are set-theoretic data with axioms below, not a topology on L, and the early additional relations and privileged subset L0 belong to cancelled drafts.

**Context:** search: réseau|segment|incidence|R121-08; no direct definition is registered; MPL_121_049-073+153+155 R121-08 is a first-pass lead at 121/050–052, compared there with 147/179–180 and 185–190: the present data add a different interval-based incidence system, without identifying it with that stratified reconstruction.

### D03 — F1: endpoint subdivision

**Source:** 156-1/006, F1. **Kind:** unpursued implication. **Quote:** “axiome de décomposition”; “Cette application est bijection.”

For a segment I with endpoints x,y and every z∈Ĩ∖{x}, there is exactly one segment I{x,z} supported inside Ĩ with endpoint set {x,z}; the same assertion applies from the other endpoint. In particular I{x,y}=I{y,x}=I, so the statement controls subsegments incident to an original endpoint. It does not assert that every pair of internal lieux determines a subsegment.

**Context:** search: subdivision|décomposition|segments|incidence; no direct F1 entry occurs; MPL_121_049-073+153+155 R121-08, first-pass lead at 121/050–052, is related only by its incidence vocabulary, and this axiom adds a more specific uniqueness requirement.

### D04 — F2: separation, with divisibility subsequently removed

**Source:** 156-1/006, F2 and margin; 024–025. **Kind:** withdrawn in the same text. **Quote:** “condition de divisibilité”; “on fait sauter” (uncertain reading); “réduit.”

Initially F2 requires Ĩ°≠∅ and, for z∈Ĩ°, requires Ĩ{x,z}∩Ĩ{y,z}={z}, together with the condition that any subsegment of I having z as an endpoint lies on one of those two sides. The doubtful later marginal instruction appears to request removal of nonempty interior from the general axioms, while scan 024 reserves “divisible” for networks satisfying it while admitting reduced networks with every segment a two-element set. Thus statements deduced from divisibility earlier in the draft must be read with that hypothesis, rather than transferred unchanged to all later networks.

**Context:** search: divisible|réduit|finite poset|finite category; no direct F2 revision is registered; STRATA A.4 and BISITE G.10 are “Proved” in their returns for finite-poset realizations, but this manuscript's reduced-graph case is a different construction and neither confirms nor contradicts those claims.

### D05 — F3: branches, and the additional local filtering clause

**Source:** 156-1/007; strengthening at 013 and references in its margins. **Kind:** reading question. **Quote:** “Axiome des branches”; doubtful “Il manque”; “compléter F3” with the verb marked uncertain.

For two segments with endpoint x, F3 says that sufficiently short initial subsegments either agree or meet only in x; common initial subsegments are intended to define an equivalence relation Rx on the segments incident to x, whose quotient Bx is the set of branches and whose cardinal is the order at x. A formula for that relation has an unresolved I/J or x/y reading on scan 007, so this semantic description follows the clear dichotomy and its later repetition at 023 rather than silently repairing that formula. The added clause requires common initial interiors inside a fixed segment, equivalently the local filtering needed for the later order description, and is not the same assertion as the global common-extension axiom F6.

**Context:** search: branches|filtrant|filtrante|réseau; no direct F3 entry occurs; the poset-realization statements STRATA A.4 and A.12 (the latter for every small poset), recorded “Proved,” concern exit realizations rather than this branch equivalence, so the present strengthening adds a separate proof obligation.

### D06 — F4: gluing at a regular joint

**Source:** 156-1/008, F4. **Kind:** unpursued implication. **Quote:** “Axiome de recollement”; “on n'affirme pas égalité!”

If I′ and I″ meet exactly at their common endpoint z and z is regular, with remaining endpoints x,y, F4 requires a unique segment I with endpoints {x,y} and support containing Ĩ′∪Ĩ″. The source explicitly does not assert equality of that support with the union, although F1 identifies the two given segments with I{x,z} and I{y,z}. This extra space in a glued support is central to the failed arbitrary-subset restriction claim examined below.

**Context:** search: recollement|attachment|N18|R121-08; MPL_150_044-084 N18 is a first-pass lead at 150/077 and 081–084 about retaining attachment data: F4 adds an abstract interval gluing law but does not restate that topological reconstruction.

### D07 — F5: regular lieux have exactly two branches

**Source:** 156-1/009. **Kind:** unproved claim. **Quote:** “L'ordre d'un lieu régulier ... est égal à deux”; “Équivalent à.”

F5 requires |Bx|=2 for every regular lieu x, and the manuscript presents an equivalent F5′ saying that interiors of segments containing x form a filter base. The first formulation controls local branch multiplicity, whereas the second requires a common smaller segment interior inside any two such interiors. The equivalence needs the preceding subdivision and branch axioms, and neither formulation imposes a finite number of lieux or segments.

**Context:** search: branches|filtre|finite|F5; no direct F5 entry is present; WG2 B15 (§1.2), an unchecked planning entry, is only a proposed bridge to finite-poset methods, and this infinitary local condition does not itself supply that bridge.

### D08 — F6 has two nonidentical formulations on its defining page

**Source:** 156-1/023. **Kind:** reading question. **Quote:** “On n'exige pas que les autres extrémités ... soient dans K”; “Ou encore.”

The first F6 says that segments I,J with a common endpoint x and the same branch there have a common extension K with x∈δK and I°∪J°⊂K°, explicitly excluding any requirement to retain their other singular endpoints. A subsequent purported reformulation instead demands I∪J⊂K, which is stronger in the presence of such endpoints. They must therefore be retained as distinct written versions, with the singular-end counterexample and the regular-end repair treated in the A notes rather than inserted into the transcription.

**Context:** search: filtrant|cofiltrant|branches|B15; no direct F6 entry occurs; WG2 B15 (§1.2) and WG2 §3.1 #2 remain unchecked plans, and the present distinction is an obstruction to inferring a refinement category from an unqualified filtering slogan.

### D09 — A network, and its divisible and reduced cases

**Source:** 156-1/024–025. **Kind:** unpursued implication. **Quote:** “est appelé un réseau”; “noeuds”; “lignes”; “graphe réduit.”

On 7 June the manuscript names a model satisfying F1–F6 a réseau, after identifying each segment with its support, and calls its singular lieux nodes, with regular connected components called lines. A network is divisible when every segment has nonempty interior and reduced when every segment equals its two-element endpoint set, equivalently Lr is empty under that revised definition. The reduced case is presented as a simple undirected graph S⊂P2(L), with no finiteness condition, so “network” does not mean “finite poset” here.

**Context:** search: réseau|graph|finite poset|B15; no direct network definition occurs in the context; STRATA A.4 and BISITE G.10, return-level “Proved” finite-poset dictionaries, supply possible later comparison tools, not an identification of this graph with their poset.

### D10 — A segment model is described by a pair of opposite partial orders

**Source:** 156-1/011–014. **Kind:** unproved claim. **Quote:** “biordre (paire d'ordres opposés)”; “loc. bifiltr.”

A segment model has L=Ĩ for one segment I, and choosing an endpoint x0 defines x≤y by [x0,x]⊂[x0,y], equivalently x∈[x0,y]. The manuscript claims equivalence with a biorder {≤,≥} having distinct least and greatest elements, divisibility, and local filtering in both directions, with segments the intervals [x,y] for x<y. These orders are partial, not asserted total, and the local filtering qualification is precisely the addition to F3 noted on scan 013.

**Context:** search: ordre|biordre|poset|STRATA; no direct biorder result is registered; STRATA 0.1, recorded “Proved” with source I ms.1–9 and XII ms.59–63, fixes a separate variance convention for finite-poset sheaves, so its ordering should not be imposed on this chosen orientation.

### D11 — “Regular immersion” means a conical neighborhood after contraction

**Source:** 156-2/002–003. **Kind:** unpursued implication. **Quote:** “régulièrement immergé”; “voisinage fermé”; “espace topologique compact” (the base letter is B or S in the uncertain reading).

For a closed nonempty A⊂X, contract A to a point a in X/A; regular immersion means that a has a closed neighborhood V homeomorphic to a cone on a compact space B, with a as vertex and V∖B open. Radial dilations provide a neighborhood basis, and the source treats the empty base as the isolated-vertex case. This is not by definition a smooth, algebraic, or pointwise locally flat embedding of A in X.

**Context:** search: conique|Q1b|Tubulure|ombre; MPL_150_001-043 Q1b is a first-pass lead at 150/012–015 and 022–023, compared with 147/140–142; INTAKE 20261114 §13.2 is an intake reading, not a referee verdict, locating uncertain “tubulure/ombre” at 149/133: this definition adds a precise contraction-and-cone condition without proving those notions identical.

### D12 — A ficelle can have nontrivial and even disconnected ends

**Source:** 156-2/003–004 and 009. **Kind:** unpursued implication. **Quote:** “ficelle topologique”; “fermés, non-ouverts” (hyphenation uncertain); “connexes.”

A ficelle is (X,{A,B}) with disjoint closed nonopen ends A,B, each regularly immersed, such that (X∖A)/B and (X∖B)/A are connected. It is reduced when A and B are single points, and orientation chooses one end as the origin. Neither connectedness of the two ends nor connectedness of X is an explicit axiom of the unreduced definition, a distinction essential to the later compact-triangulable claim.

**Context:** search: ficelle|compact|Q4b|Q4-02; no direct ficelle entry occurs; MPL_150_001-043 Q4b and MPL_151_032-075 Q4-02 are first-pass comparison leads at 150/037–039 and 151/044–045,059–061, respectively: their compact-object comparisons do not impose connected endpoint decorations here.

### D13 — A cutting is made along a separating lieu, with compatibility conditions

**Source:** 156-2/005–010. **Kind:** unpursued implication. **Quote:** “Découpage d'une ficelle”; “mutuellement disjoints”; “homeo. de raccordement.”

A lieu is an end or a closed internal C for which X∖C splits as a topological sum of two sides containing A and B, with the corresponding end-contracted sides connected, and C regularly immersed in X∖(A∪B). Cutting gives the two closed pieces X{A,C}=closure(U{A,C})∪C and X{B,C}=closure(U{B,C})∪C, each marked by its inherited end and C. Multiple internal lieux must be disjoint in the manuscript's stronger sense—each belongs to a component ficelle after cutting along the other—and n mutually compatible lieux form a chain whose reconstruction data are n+1 oriented ficelles and n gluing homeomorphisms.

**Context:** search: découpage|raccordement|R29|N18; MPL_148_029-072 R29 is a first-pass lead at 148/058:4–11,059:4–6,061:36–44, and MPL_150_044-084 N18 a first-pass lead at 150/077,081–084: these scans add an explicit one-dimensional cutting-and-regluing system while preserving the attachment-data issue.

### D14 — Rives are germs of clopen subsets, not a set of connected components

**Source:** 156-2/015–016. **Kind:** unpursued implication. **Quote:** “Comp(Z)=Hom cont(Z,{0,1})”; “algèbre ... idempotente.”

The definition is Comp(Z)=C(Z,{0,1})=Γ(Z,F2,Z), equivalently the Boolean algebra of clopen subsets, and Riv(A,X)=colimV⊃A Comp(V∖A) with restriction maps as neighborhoods shrink. This is a commutative unital Boolean F2-algebra of neighborhood germs, and under the stated conical hypothesis the manuscript identifies it with Comp of the boundary of a conical neighborhood. Neither Comp nor Riv means π0, and the later Spec notation requires a relative sheaf interpretation if it is to remember positions along A.

**Context:** search: composantes|link|N39|P4e; MPL_150_044-084 N39 is a first-pass lead at 150/072,077 compared with 147/180 and 149/134; EXIT_ONE_TYPE P4e is return-level “Proved” at 149/133: these pages add a Boolean local invariant that is weaker than full normal-link data.

### D15 — A birive and a maille require different amounts of structure

**Source:** 156-2/016–019. **Kind:** unpursued implication. **Quote:** “ρ+ρ′=1”; “maille”; “ssi ... est une ficelle top.”

A birive is an unordered complementary pair β={ρ,ρ′} in Riv(A,X), called trivial when it is {0,1}, and a nontrivial birive defines the author's whole-set germ notion that A “disconnects X locally.” The proposed partial cutting Decβ(A,X) has two marked copies Aρ,Aρ′ of A and unchanged complement X∖A, obtained by pushing the two spectral boundary parts onto those copies. A maille requires the additional regularity and ficelle conditions, and its orientation chooses one element of β; a merely nontrivial birive does not by itself guarantee those conditions.

**Context:** search: boucle|découpage|R29|R34; MPL_148_029-072 R29 and R34 are first-pass leads at 148/058–061 and 148/055:8,061:31–34,064:3: the present construction adds birive data to a loop-like cut, without identifying it with those earlier cutting or erasure operations.

### D16 — No definition of a workshop occurs in the supplied pages

**Source:** complete 156-1/001–027 and 156-2/001–019; especially 156-2/017–018. **Kind:** reading question. **Quote:** “maille”; “Réalisations topologiques des réseaux.”

Neither “atelier” nor an English “workshop” is defined in these 46 scans. The nearby explicit word is maille, a node-and-birive construction with a ficelle criterion, and translating it as a workshop would manufacture the requested definition. The absence is limited to the supplied pages; the final argument of cote 156-1 and the final symmetry claim of cote 156-2 are incomplete or unproved here, so later continuation elsewhere remains possible.

**Context:** search: atelier|workshop|maille|network; the README asks prospectively for a workshop, but RESULTS_STATE supplies no matching definition; this is a negative finding against the unchecked planning expectation in WG2 B15 (§1.2), not a claim about the entire archive.
