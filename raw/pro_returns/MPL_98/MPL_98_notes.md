# MPL_98 — Research notes

## Evidence and limits of the comparison

These notes concern **98.pdf, scans 002–044**, the complete 43-page supplied range. The diplomatic transcription was frozen at **2026-11-18 01:36:35 UTC**, after one sequential reading of every whole scan and both halves, a second visual audit of every page, and a reconciliation of recurring notation. No OCR was used on the supplied manuscript images. The 43 individual fragments and combined fragment are covered by 44 SHA-256 hashes; the final verification is recorded in progress.log.

The root performed all manuscript reading. Research collaborators worked only after the freeze, on the supplied context, published literature, and mathematical arguments; they did not inspect the scans or independently transcribe pages. Mechanical validation establishes that all 43 fragments are present, the 694 inventory rows are marked transcribed, the combined fragment matches them, and the syntax harness compiles; it does not certify every reading or the mathematics. The doubt register records the remaining uncertainty, especially in the pencil and crowded marginal passages.

**Context keys.** “Hua98” means Michel Hua’s project’s AI-produced modernized reading in the supplied **hua_project/98.modern.tex**, accompanied by **hua_project/README.md**. Its page n is our scan n+1. “RS” means the supplied **notes/RESULTS_STATE.md**, and “README” means the context package’s README.md, not the deliverable README. All four supplied context members were read after the freeze. The source packages are not copied into this return.

Hua98 is credited whenever a note uses its reconstruction, added proof, or proposed link. It is neither a diplomatic witness nor an established-result source. In particular, a mathematically convenient reading cannot replace a frozen letter, subscript, deletion, or incomplete sentence. The reading questions at the end of the numbered notes record those differences without changing the transcription.

Each note identifier keys an actual context search in **research/context_searches.jsonl** and **research/note_plan.json**, recording the query, time, and matching file/line locators; relevant matches and their manuscript scan correspondence are identified in each note. A search hit is not a proof, and an absent substantive match is stated rather than filled with an invented connection. The note bodies contain one to four sentences; longer proofs and counterexamples are in the research memoranda and **research/root_proof_checks.md**.

### Register-status key

| Key or entry | Status supplied by the context | Treatment in this run |
|---|---|---|
| **RS–Ø** | RS Orientation expressly says that no own established result directly matches these norm, cohomology, or bounded-family subjects | No settled result is silently assumed; source comparison, independent proof, or an explicitly limited background use is recorded as appropriate |
| **H98 = Hua, findings register, 98-axiomatic-norms-can-section** | **conjecture (unsearched); Lean card: partly proved; intake: new to us** | Finite locally free scheme and finite-fibre G-set models checked; degree/empty-target refinement identified; the Lean files and certificates were not supplied or run |
| **LM7 E.23; FLAGGED_149 B9; LM1 D.11; LM4 D.12; LM4 F.7** | **Open**, originating returns’ claims | No solution or refutation is claimed; G11 and the disposition table below explain the limited bearing |
| **LM7 C.1; LM7 C.5** | **Known / Proved**, originating returns’ claims | Related Picard/Jacobian background only; the original result files and arithmetic claims were not checked |
| **WG H9; WG H2; WG2 entries** | Unchecked planning guesses or questions | Not promoted to mathematical evidence |
| Other returned-package notes, including **MPL_131 RN001 / §2 / 10** | First-pass leads | Compared only to the supplied summaries; their underlying manuscripts and return files are absent |

RS separately lists a reviewed chain in the GT programme, but none of the checks here relies on that chain. The absence of a direct application is consistent with RS’s own package orientation. No result status in the user’s register has been edited.

### Principal findings and their scope

| Finding | Notes | Qualification |
|---|---|---|
| The top alternating-image construction works integrally | N01–N02 | The full sign-eigenspace is a different object and can be too large in characteristic two |
| A single numerical degree conflicts with arbitrary empty-target base change | N10–N11 | The source’s degree-predicate wording and Hua’s reported hasDeg formalization suggest the refinement; no formal code was checked |
| The finite-orbit G-set site needs an enlarged setting for some Čech nerves | G01–G07 | This concerns abstract groups; continuous profinite actions require their own category |
| The \(G_m\) sequence has a precise conditional reconstruction | G08, G13 | The field setting can satisfy Picard vanishing; the conic counterexample concerns one fixed non-field cover |
| Bounded cycle degree does not bound even pure fixed-quotient sheaves | B02, B31 | \(\mathcal O(n)\) on \(\mathbf P^1\) is explicit; attribution to the faint tentative statement remains conditional |
| Relative field embeddings cannot be ignored | B05–B11 | An arbitrary compositum is not interchangeable with a suitable witness |
| The Tor proof uses the wrong resolution ring in one step | B18, B20 | A polynomial-algebra resolution repairs the proof under stated finiteness hypotheses |
| Input flatness is actually present in the frozen Tor lemma | B19, R09 | The counterexample proves its necessity; it does not expose an omission in that lemma |
| “En tt degré” is defensible for the truncated Hom complex | B22–B24 | Only the subsequent identification with Ext is restricted to \(p\le N\) |
| The reused typescript has a full-rank homogeneous-system error | T06–T07 | The preceding-prefix repair is confined to the notes |

The boundedness arguments below use finite type schemes over noetherian bases and coherent sheaves unless a note explicitly changes that scope. Properness, finite presentation, input flatness, finite degree ranges, and the choice of coefficient ring are kept separate. The counterexamples are checks made in this run, not claims of novelty.


## Numbered notes

There are **89 notes** below. The file is 98.pdf throughout; scan numbers are the supplied PDF scan numbers, not archival foliation or reused printed pagination. Each note has its own recorded context search and one to four sentences of analysis.


### Scope and chronology


#### MPL98.P01 — Scope and planning disposition


**File / scan:** 98.pdf, 002–044.  
**Kind:** unpursued implication / planning comparison.  
**Brief source quotation:** “Normes”; “Familles limitées”.  
**Context:** README.md, “This package in our plan”; RS, Orientation, lines 13–22; Hua98, “Les stations,” pp. 1–43, corresponding to scans 002–044.  
**Register:** RS–Ø; S19 and Book I I.VI are planning leads, not established theorems.


The two covers and the handwritten arguments support the construction-techniques placement: norm operations, group cohomology, and bounded families are the actual mathematical strands. The ten reused typescript faces supply additional topology and abelian-variety material which Michel Hua’s project deliberately omits, so the present record adds evidence to that modernized account. The planning suggestions concerning Néron models, Greenberg transforms, residues, and intersection formulas are not developed into results in these scans; the proposed connection with moduli construction is a method-level connection, not a representability proof.


#### MPL98.P02 — Chronology and the two covers


**File / scan:** 98.pdf, 002,026.  
**Kind:** reading question / unpursued implication.  
**Brief source quotation:** “Cf aussi SGA 4 XVII”; “cf SGA 6 XIII”.  
**Context:** README.md, cote 98 description; RS, Orientation; Hua98, cover discussion at pp. 1 and 25 (scans 002 and 026).  
**Register:** RS–Ø; S19 comparison against print.


The supplied catalogue places the material from 1966–1967 onward, but the internal covers do not themselves establish the date of each sheet or of the reused typescripts. Grothendieck’s 1961 Exposé 221 and Deligne’s published SGA 4 XVII §6.3 are close mathematical comparators, so correspondence with them cannot establish priority or the direction of dependence (Grothendieck, 1961b, 1962; Deligne, 1973). This note qualifies the contextual chronology while retaining its usefulness as a catalogue lead; the XVII/XVIII reading disagreement is isolated in R01.


### Norms, symmetric powers, and axioms


#### MPL98.N01 — Integral alternating tensor line


**File / scan:** 98.pdf, 003.  
**Kind:** own idea / targeted proof check.  
**Brief source quotation:** “Ils opèrent en particulier dans la partie … Λⁿ_A M”.  
**Context:** Hua98, “Le déterminant comme loi multiplicative,” p. 2 (scan 003), especially its factorial/anti-invariant footnote.  
**Register:** H98; its determinant mechanism is checked here, not its reported Lean certificate.


For a free rank-\(n\) module, the image of \(\operatorname{Alt}=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\sigma\) is the free line generated by the alternating basis tensor, which has a coefficient \(1\), so \(\Lambda^nM\) embeds in \(M^{\otimes n}\) without inverting \(n!\). Every tensor endomorphism commuting with the permutations preserves that image, and localization gives the finite-projective version; the full proof is NORM01 in the norm memorandum. This differs from identifying the exterior power with the whole sign-eigenspace, which has dimension \(3\), rather than \(1\), for \(M=\mathbf F_2^2\). Thus Hua’s warning about the full eigenspace is correct, but its claimed need to abandon the integral image construction is too strong; Deligne (1973, XVII §6.3.1) is the published comparator.


**Confidence and reason:** High: an integral basis proof and a separate characteristic-two counterexample distinguish the two assertions.


#### MPL98.N02 — Canonical norm section


**File / scan:** 98.pdf, 003–005.  
**Kind:** unproved claim / unpursued implication.  
**Brief source quotation:** “Normes”; “N … Γ(G_T/T)”.  
**Context:** Hua98, §§I, “Le déterminant…” and “La norme…,” pp. 2–4 (scans 003–005).  
**Register:** H98; finite locally free scheme model checked.


For \(X=\operatorname{Spec}B\to Y=\operatorname{Spec}A\) finite locally free of rank \(r\), the determinant of multiplication is a multiplicative homogeneous polynomial law and defines \((B^{\otimes r})^{S_r}\to A\), hence \(Y\to\operatorname{Sym}^r_Y(X)\). This supplies a precise construction for the canonical-section interpretation in Michel Hua’s project and restates its finite locally free model with the needed algebra spelled out. Naturality of the determinant and the orbit-sum description give arbitrary base-change compatibility; compare Ferrand (1998, §§2.5.1, 3.1.1–3.1.2) and Deligne (1973, XVII §6.3.4).


#### MPL98.N03 — Nonreduced finite flat fibres


**File / scan:** 98.pdf, 005,013.  
**Kind:** own idea / boundary example.  
**Brief source quotation:** “fini et plat”; “loc. libre … rang r”.  
**Context:** Hua98, finite locally free conventions and “Trois exemples,” pp. 4 and 12 (scans 005 and 013).  
**Register:** H98; adds a boundary check, not a new norm theorem.


The construction includes nonreduced finite locally free fibres: for \(B=A[\epsilon]/(\epsilon^2)\), multiplication by \(a+b\epsilon\) has norm \(a^2\). Constant geometric-fibre length alone is insufficient: \(X=\operatorname{Spec}k\to Y=\operatorname{Spec}(k[\eta]/\eta^2)\) has fibre length \(1\), but every positive relative symmetric power is \(X\), which has no \(Y\)-section. This adds an explicit boundary to Hua’s description and does not suggest replacing the local-freeness wording actually present in scan 013.


**Confidence and reason:** High: both assertions follow from explicit multiplication matrices or the impossible splitting of the dual-number quotient.


#### MPL98.N04 — Trace from the norm


**File / scan:** 98.pdf, 005.  
**Kind:** own idea / unpursued implication.  
**Brief source quotation:** “N … Γ(G_T/T)”.  
**Context:** Hua98, “La norme relative à une opération symétrique,” p. 4 (scan 005); RS entries on arithmetic norms.  
**Register:** H98; LM7 E.124 and SECTIONS_OVER_Q A.179/A.184 remain originating-run claims, not checked arithmetic applications.


Applying the symmetric operation “addition” gives trace, while “multiplication” gives norm; infinitesimally \(N(1+\epsilon b)=1+\epsilon\operatorname{Tr}(b)\) over \(A[\epsilon]/(\epsilon^2)\). This adds a concrete link between the two operations to the diagrams and agrees with Hua’s unifying interpretation (Deligne, 1973, XVII §6.3.18). The generic mechanism does not verify the arithmetic unit-norm images or residue computations listed under LM7 E.124 and SECTIONS_OVER_Q A.179/A.184, whose underlying result files were not supplied.


**Confidence and reason:** High for the determinant expansion; no confidence claim is made about the uninspected arithmetic results.


#### MPL98.N05 — Symmetric target and functoriality


**File / scan:** 98.pdf, 005,007.  
**Kind:** unproved claim.  
**Brief source quotation:** “Fonctorialité en X,Y,S”; “symm”.  
**Context:** Hua98, pp. 4–8 (scans 005–009), symmetric-operation construction and compatibility diagrams.  
**Register:** H98; quotient-descent condition checked.


A symmetric map \(G^r\to G'\), composed with an \(r\)-tuple induced from \(T\to G\), produces an operation by descending through \(\operatorname{Sym}^r(T/S)\) and composing with the canonical section. The quotient must have the relevant universal property for the chosen target; arbitrary sheaf-valued operations cannot be treated as descending automatically. This refines Hua’s broad norm/trace description: Deligne (1973, XVII §§6.3.13–6.3.15) explicitly states the sheaf-descent hypothesis and its representable and quasi-coherent cases.


#### MPL98.N06 — Disjoint sums and multiplicativity


**File / scan:** 98.pdf, 007,012.  
**Kind:** unproved claim.  
**Brief source quotation:** “Cas où r=0, r=1”; “Additivité en M”.  
**Context:** Hua98, normalization/additivity, pp. 6 and 11 (scans 007 and 012).  
**Register:** H98; sum compatibility independently checked.


For \(B=B_1\times B_2\), block-diagonal multiplication gives \(N_{B/A}(b_1,b_2)=N_{B_1/A}(b_1)N_{B_2/A}(b_2)\), and the section lies in the \((r_1,r_2)\) component of the symmetric power of the disjoint union. The rank-one identity is immediate, while degree zero gives the empty symmetric product and the chosen nullary value, which is the identity in the additive or multiplicative unital cases. This verifies, rather than merely repeats, the additivity diagram used by Hua; the separate problem with a single numerical degree on the empty target is N10 (Deligne, 1973, XVII §6.3.5).


#### MPL98.N07 — Norm transitivity left unproved


**File / scan:** 98.pdf, 005,007,009,012.  
**Kind:** unproved claim.  
**Brief source quotation:** “Transitivité”; “Je dis qu’on a”.  
**Context:** Hua98, “La transitivité,” pp. 4–8 and axiom (ii ter), p. 11 (scans 005–009,012).  
**Register:** H98; transitivity independently re-proved.


For finite locally free \(A\to B\to C\), the required identity is \(N_{C/A}=N_{B/A}\circ N_{C/B}\), with the corresponding flattening of symmetric powers. The norm memorandum proves it integrally by a block-determinant identity, using a monic-polynomial localization and then descent back to the original ring. Because the proof works after every scalar extension, it establishes equality of polynomial laws and of the sections, a stronger check than agreement on geometric fibres alone. This supplies the proof behind the manuscript’s final assertion and Hua’s reconstruction; the exact published comparator is Deligne (1973, XVII Lemma 6.3.3 and §6.3.15(v)).


#### MPL98.N08 — Axioms and quotient closure


**File / scan:** 98.pdf, 011.  
**Kind:** unproved claim / axiomatic clarification.  
**Brief source quotation:** “où les sommes finies existent”; conditions (i)–(v).  
**Context:** Hua98, “Les axiomes,” p. 10 (scan 011); RS, H98 finding.  
**Register:** H98: conjecture (unsearched), Lean card partly proved; additional structure identified.


The page specifies a class of arrows, the existence and stability of certain fibre products and finite quotients, a degree assignment, and compatible sections. These are additional axioms, not consequences of the existence of finite coproducts in an arbitrary category. This qualifies the phrase “in any category with finite sums” in Hua’s findings register while supporting its interpretation as an axiomatic package with concrete models; the uncertain margin mark “!|?” remains a reading question, not a confidently attributed objection.


#### MPL98.N09 — Orbit-sum degree computation


**File / scan:** 98.pdf, 011–013.  
**Kind:** unproved claim / targeted proof check.  
**Brief source quotation:** “card(Eⁿ/G)”; “très facilement”.  
**Context:** Hua98, “Trois exemples,” pp. 10–12 (scans 011–013), including its added permutation-basis proof.  
**Register:** H98; Hua’s added proof credited and independently checked.


If \(B\) is free with basis indexed by \(E\), then \(B^{\otimes n}\) has a permutation basis indexed by \(E^n\), and the \(H\)-invariants have the orbit sums as a basis. Consequently their rank is \(\#(E^n/H)\), and this particular invariant module commutes with every base change, without inverting \(|H|\). This rechecks Hua’s explicitly added argument and supplies the missing detail behind the manuscript’s ease assertion. It must not be extended to arbitrary group actions: the involution \(\epsilon\mapsto-\epsilon\) on \(\mathbf Z[\epsilon]/\epsilon^2\) gains extra invariants modulo \(2\).


#### MPL98.N10 — Empty-target degree convention


**File / scan:** 98.pdf, 011–013.  
**Kind:** own idea / axiomatic boundary.  
**Brief source quotation:** “Soit deg une fonction”; “deg(id_X)=1”.  
**Context:** Hua98, degree axioms and Lean footnote, pp. 10–12 (scans 011–013).  
**Register:** H98; literal single-function formulation refuted, degree-predicate refinement checked; no Lean execution.


With arbitrary pullback in schemes or G-sets, pulling a degree-\(r\) arrow back to the empty target gives the empty identity, so a single base-change-invariant numerical degree with identity degree one would force \(r=1\). Additivity applied to two identities then forces \(2=1\), showing that the literal single-function formulation needs refinement. The source’s own later wording “dit de degré r” and Hua’s reported Lean predicate hasDeg suggest a suitable repair: treat degree as indexed data or a fibrewise predicate, which is vacuously true for every \(r\) over the empty target. This differs from refuting the canonical-section construction or the uninspected Lean development.


**Confidence and reason:** High: the contradiction is formal, while the predicate formulation directly removes it.


#### MPL98.N11 — Finite G-set multiset model


**File / scan:** 98.pdf, 012–013.  
**Kind:** unproved claim / targeted proof check.  
**Brief source quotation:** “un élément privilégié”; “on vérifie aussitôt”.  
**Context:** Hua98, “Exemple I,” pp. 11–12 (scans 012–013).  
**Register:** H98; finite-fibre G-set model checked independently.


For an equivariant map whose fibres all have the same finite cardinality, assign to a point of the target the multiset containing each point of its fibre once. Equivariance and base change follow from bijections of fibres, disjoint sums concatenate the multisets, and composition flattens the multiset of fibre-multisets. This verifies the source’s “aussitôt” assertion and agrees with Hua’s interpretation after the empty-target degree refinement in N10; it is an ordinary proof, not a rerun of Hua’s claimed formalization.


#### MPL98.N12 — Finite flat versus finite locally free


**File / scan:** 98.pdf, 013.  
**Kind:** reading question / unproved claim.  
**Brief source quotation:** “fini et plat … loc. libre … rang r”.  
**Context:** Hua98, conventions and scheme example, p. 12 (scan 013).  
**Register:** H98; finite locally free scope checked.


The source’s definition of degree explicitly includes local freeness of rank \(r\), so its scheme example should not be weakened to arbitrary finite flat morphisms over unrestricted bases. Finite locally free is equivalent to finite, flat, and locally of finite presentation; finite flat alone suffices over a locally noetherian base (The Stacks Project Authors, n.d., Tag 02K9). This agrees with the usable scope of Hua’s example and explains the function of the words already on the page, rather than supplying an absent hypothesis.


#### MPL98.N13 — Contracted product and covering hypotheses


**File / scan:** 98.pdf, 014.  
**Kind:** self-flagged: a step marked for development.  
**Brief source quotation:** “à développer” [doubt-marked]; “X×_(Γ)E … existe”.  
**Context:** Hua98, contracted-product discussion, p. 13 (scan 014).  
**Register:** H98; only the principal-covering model is checked.


The proposed transport from G-sets to objects of a category needs existence of the contracted products and compatibility with the products and quotients used in the norm diagrams. For a genuine locally trivial principal covering, these assertions can be checked on trivializing opens and glued, giving the topological model described by Hua. The scan stops at an unfinished “compos…” phrase, so it does not contain a completed verification for arbitrary topological or analytic categories.


#### MPL98.N14 — Hilbert–Chow link


**File / scan:** 98.pdf, 002–009,026–044.  
**Kind:** unpursued implication.  
**Brief source quotation:** “Normes”; “Familles limitées”.  
**Context:** Hua98, “Les stations,” lines 216–222, linking the norm block (scans 002–009) to the boundedness block (026–044).  
**Register:** H98 and RS–Ø; the proposed bridge is credited to Michel Hua’s project.


A finite locally free family of length-\(r\) subschemes \(Z\subset X_T\) has a norm section, yielding a Hilbert–Chow map \(\operatorname{Hilb}^r(X/S)\to\operatorname{Sym}^r(X/S)\). This supports Hua’s proposed link between the two blocks, which the manuscript does not explicitly make. Ambient flatness of \(X/S\) is unnecessary for this first map in the separated algebraic-space setting; the flat family is \(Z/T\), while divided powers provide the comparison target with unrestricted base-change compatibility (Rydh, 2008b, §4.3 and Proposition 4.1.1). The link does not establish a date or a new priority claim.


#### MPL98.N15 — The explicit request to relate the examples


**File / scan:** 98.pdf, 013–014.  
**Kind:** self-flagged: question and request for explanation.  
**Brief source quotation:** “Expliquer la relation de cet exemple avec le cas général, peut-on …”.  
**Context:** Hua98, transition from G-sets to schemes and coverings, pp. 12–13 (scans 013–014); the exact tail of the margin is not securely read.  
**Register:** H98; adds the author’s explicit question to the finding’s status.


The margin asks for an explanation connecting the G-set example to the general case, but its words after “peut-on” remain doubtful in the frozen reading. Transport through a principal covering explains the unramified cases; it cannot by itself establish every ramified finite locally free example, such as the dual-number algebra in N03. This records an actual open step on the sheet and qualifies any impression that the three examples have all been deduced from one completed Galois argument.


### Group actions, descent, and cohomology


#### MPL98.G01 — Finite-orbit site and missing fibre products


**File / scan:** 98.pdf, 016,018.  
**Kind:** unproved claim / own idea.  
**Brief source quotation:** “E/G soit fini”; “à développer”.  
**Context:** Hua98, “Les G-ensembles comme faisceaux,” p. 15 and the Čech construction, p. 17 (scans 016,018).  
**Register:** RS–Ø; H98 is adjacent norm material, not a settled cohomology result.


Here G is an abstract group, equivalently a discrete group: its finite-orbit G-sets form a generating site with the jointly surjective sieve topology, so the associated topos is the topos of all G-sets. For infinite \(G\), however, \(G\times G\) under diagonal left translation has \(|G|\) orbits and is outside that small category, although \(G\) itself is inside it. Thus the subsequent Čech nerve must be interpreted in the enlarged G-set topos or an adequate larger site; this makes explicit a limitation noted but not fully resolved in Hua’s account (The Stacks Project Authors, n.d., Tag 079Z).


**Confidence and reason:** High for the orbit count and the necessary enlargement; the site comparison is made using covering sieves, not unavailable fibre products.


#### MPL98.G02 — Recovering the group action


**File / scan:** 98.pdf, 016.  
**Kind:** self-flagged: a step marked for development.  
**Brief source quotation:** “A=Φ(G_g)”; “à développer”.  
**Context:** Hua98, p. 15 (scan 016), equivalence between G-sets and sheaves.  
**Register:** RS–Ø; no directly matching established entry.


Evaluation on the left regular G-set recovers the underlying set, while contravariance applied to right translations supplies its left G-action. The mutually inverse description uses \(X\mapsto\operatorname{Hom}_G(X,A)\) and the descent condition, with the action convention fixed throughout. This supplies the mechanism behind the source’s “On sait” and agrees with Hua’s reconstruction; the source’s literal second argument \(E\) in one Hom expression is retained as reading question R11.


#### MPL98.G03 — Cohomology presheaf versus sheaf


**File / scan:** 98.pdf, 018,020.  
**Kind:** unproved claim / conceptual clarification.  
**Brief source quotation:** “prépré…faisceau”; “foncteur dérivé qième”.  
**Context:** Hua98, pp. 17–19 (scans 018,020), cohomology presheaf and its derived evaluation.  
**Register:** RS–Ø.


For a G-module \(A\), the value at a G-set \(S\) is naturally \(\operatorname{Ext}^q_{\mathbf Z[G]}(\mathbf Z[S],A)\), and on \(G/F\) this is \(H^q(F,A)\). The presheaf is retained on the Čech nerve; replacing it by its sheafification would discard the data used by the spectral sequence. This restates Hua’s explanation with an explicit derived-functor model and gives mathematical significance to the source’s insistence on “pré” (The Stacks Project Authors, n.d., Tag 03AZ).


#### MPL98.G04 — Čech spectral sequence and coinduced contraction


**File / scan:** 98.pdf, 018.  
**Kind:** unproved claim / targeted proof check.  
**Brief source quotation:** “utiliser essentiellement les faits suivants”; “Hom_Z(Z(G),M)=M^G”.  
**Context:** Hua98, “La suite spectrale A,” p. 17 (scan 018).  
**Register:** RS–Ø; ordinary independent proof, no formal certificate.


For nonempty \(T\), the augmented complex \(\mathbf Z[T^{p+1}]\to\mathbf Z\) is exact after choosing a point of \(T\), and the bicomplex \(\operatorname{Hom}_G(\mathbf Z[T^{p+1}],I^q)\) gives the displayed Čech-to-group-cohomology spectral sequence. The notation \(M^G\) here denotes the coinduced function module explicitly identified by the preceding Hom expression, not invariants. An injective G-module is a retract of a coinduced module, and insertion of a chosen point contracts the resulting ordinary function-valued Čech complex; an arbitrary coinduced module need not itself be injective. This supplies the details behind the source’s sketch and makes Hua’s shorthand explicit; see COH02–COH03 and Hochschild and Serre (1953, I §3).


#### MPL98.G05 — Shapiro and orbit conventions


**File / scan:** 98.pdf, 018,020.  
**Kind:** reading question / unpursued implication.  
**Brief source quotation:** “S=F\G”; “H^q(F,A)”.  
**Context:** Hua98, p. 17 (scan 018), footnote on right/left cosets; relative case p. 19 (scan 020).  
**Register:** RS–Ø.


The later left-action convention usually writes the transitive object \(G/F\), but \(F\backslash G\) can carry the left action \(g\cdot Fx=Fxg^{-1}\), with inversion giving an equivariant identification with \(G/F\). Thus the bare coset notation is not by itself a contradiction; the action must be specified before changing it. This qualifies Hua’s proposed correction and preserves the source’s visible notation while recovering the same Shapiro identification (Hochschild & Serre, 1953, I §3).


#### MPL98.G06 — Relative sequence and Hochschild–Serre


**File / scan:** 98.pdf, 020.  
**Kind:** unproved claim / targeted proof check.  
**Brief source quotation:** “La suite spectrale B n’est donc pas essentiellement plus générale que A”.  
**Context:** Hua98, “La suite spectrale B,” p. 19 (scan 020).  
**Register:** RS–Ø.


For \(T\to S\) surjective, the relative nerve gives an abutment \(\operatorname{Ext}^{p+q}_{\mathbf Z[G]}(\mathbf Z[S],A)\), the cohomology of the slice topos. For subgroups \(F'\subseteq F\subseteq G\), when \(S=G/F\) and \(T=G/F'\), the slice is the category of F-sets and the fibre is \(F/F'\), which proves the asserted reduction. Only when \(F'\triangleleft F\) does this become \(H^p(F/F',H^q(F',A))\Rightarrow H^{p+q}(F,A)\); without normality the stabilizers in the nerve must remain visible. This checks Hua’s comparison with Hochschild–Serre under its actual group-quotient hypothesis (Hochschild & Serre, 1953, II §4).


#### MPL98.G07 — Requested generalisation to arbitrary sheaves


**File / scan:** 98.pdf, 020.  
**Kind:** self-flagged: requested generalization.  
**Brief source quotation:** “Tout ceci est à généraliser aux hyperfaisceaux quelconques”.  
**Context:** Hua98, end of p. 19 (scan 020), its stated topos generalization.  
**Register:** RS–Ø; a general method, not an arithmetic-section result.


For an epimorphism \(T\to S\) in a Grothendieck topos and an abelian sheaf, the corresponding Čech-to-derived-cohomology spectral sequence supplies the requested ordinary-cover generalization (The Stacks Project Authors, n.d., Tags 03AZ and 079Z). This verifies the direction of Hua’s proposed generalization while leaving the manuscript’s explicit request visible. The historical word “hyperfaisceaux” alone does not establish a separate theorem about arbitrary modern hypercovers or hypercomplete higher topoi.


#### MPL98.G08 — The conditional Picard–Brauer edge sequence and the field setting


**File / scan:** 98.pdf, 022.  
**Kind:** unproved claim / conditional reconstruction.  
**Brief source quotation:** “H²(T/S,G_m)”; initial “•|0”; the field square below.  
**Context:** Hua98, “Le cas de G_m,” p. 21 (scan 022), including editorial additions of an initial zero and a meaning for H³′.  
**Register:** RS–Ø; fixed-cover edge sequence checked with qualifications.


The conditional reconstruction of the extended sequence follows under \(E_2^{p,1}=0\), with \(H^{3\prime}=\ker(H^3\to E_2^{0,3})\); this does not certify every uncertain source symbol. Its endpoint is \(E_4^{4,0}\), not generally \(H^4\), since a later \(d_4:E_4^{0,3}\to E_4^{4,0}\) may remain. For the initial injection alone the exact condition is that \(d_2:E_2^{0,1}\to E_2^{2,0}\) vanish, with \(\operatorname{Pic}(T)=0\) sufficient; COH06 and its Appendix C give the filtration proof. For a finite field extension admitted as a cover in the chosen topology, the nerve rings are Artinian with zero Picard group, so the field setting drawn on the page can meet the stronger condition, including inseparable extensions in the fppf topology; G13 treats the general-scheme boundary.


#### MPL98.G09 — Local coefficient systems


**File / scan:** 98.pdf, 024.  
**Kind:** withdrawn in the same text / targeted proof check.  
**Brief source quotation:** “système local” with “trivial” deleted and “défini” inserted.  
**Context:** Hua98, “Quatre fibrations,” p. 23 (scan 024).  
**Register:** RS–Ø; the source correction is rechecked.


The page itself replaces a claim of triviality by a local system determined by the group action, and the later braces should be read in that light. The Klein-bottle fibration over the circle illustrates the correction: reflection acts by \(-1\) on the fibre’s integral \(H^1\), giving \(H^1(K,\mathbf Z)=\mathbf Z\) and \(H^2(K,\mathbf Z)=\mathbf Z/2\). Ignoring monodromy would give the torus answer instead; this supports Hua’s local-coefficient reading and Serre’s original formulation (Serre, 1951, II §8, Proposition 6).


#### MPL98.G10 — Group–subgroup and quotient fibrations


**File / scan:** 98.pdf, 024.  
**Kind:** unproved claim / comparison of special cases.  
**Brief source quotation:** “Shapiro”; “Hochschild–Serre”; “ss-groupe distingué”.  
**Context:** Hua98, p. 23 (scan 024), four fibrations.  
**Register:** RS–Ø.


The principal-bundle, subgroup, and normal-subgroup constructions recover the familiar classifying-space and group-cohomology spectral sequences when the indicated homotopy fibrations exist. For discrete groups the subgroup case with discrete fibre gives Shapiro, and the normal-subgroup case gives Hochschild–Serre, agreeing with Hua’s comparison (Hochschild & Serre, 1953, I §3 and II §4). For general topological groups, bundle/classifying-space hypotheses remain necessary; the page’s compressed diagrams do not supply a verification for every topological group or quotient.


#### MPL98.G11 — No finite-homotopy or section result follows


**File / scan:** 98.pdf, 016–024.  
**Kind:** unpursued implication / register disposition.  
**Brief source quotation:** “suite spectrale de Leray - Čech”.  
**Context:** RS, headline programmes and selected open rows, lines 347–351; Hua98, §§III, pp. 15–23 (scans 016–024).  
**Register:** LM7 E.23; FLAGGED_149 B9; LM1 D.11; LM4 D.12; LM4 F.7 — all Open in originating returns.


The spectral-sequence constructions provide a method for organizing group actions and descent, but these pages do not determine the section-map fibres, prime-to-\(p\) point comparison, integral \(\mu_2\) extension, GT torsion classification, or \(A_5\) completion centralizer asked for by the five selected open entries. This agrees with RS’s own package orientation and adds no proof or counterexample to those entries. The broad EXIT_TOWER, GT, FINMON, and SECTIONS programme headings therefore remain background rather than outcomes of this cote.


#### MPL98.G12 — Cohomology action is not only component permutation


**File / scan:** 98.pdf, 024.  
**Kind:** own idea / conditional counterexample.  
**Brief source quotation:** “via celles de … π₀(X) sur π₀(X/F)” [connecting words uncertain].  
**Context:** Hua98, p. 23 (scan 024), subgroup-fibration local system.  
**Register:** RS–Ø; adds a limitation to a possible reading.


Take \(X=O(2)\) and \(F=\{I,\operatorname{diag}(1,-1)\}\), so \(X/F\simeq S^1\). The quotient is connected, but the nonidentity component of \(O(2)\) acts by reflection and hence by \(-1\) on \(H^1(S^1,\mathbf Z)\). Therefore the cohomological action is not determined solely by permutation of the fibre’s connected components. This refutes only that interpretation of the uncertain “via” phrase, while preserving and supporting the explicit local-system correction in G09.


**Confidence and reason:** High for the explicit homogeneous-space computation; the application to the manuscript is conditional on the doubtful connecting phrase.


#### MPL98.G13 — The real conic tests an unrestricted fixed-cover injection


**File / scan:** 98.pdf, 022.  
**Kind:** own idea / boundary counterexample.  
**Brief source quotation:** “H²(T/S,G_m)” with initial “•|0”.  
**Context:** Hua98, “Le cas de G_m,” p. 21 (scan 022), conditional low-degree sequence; related to G08.  
**Register:** RS–Ø; only an unrestricted fixed-cover extension to schemes is refuted.


For the nonsplit real conic \(S:x^2+y^2+z^2=0\) and \(T=S_{\mathbf C}\simeq\mathbf P^1_{\mathbf C}\), the lift of the real involution to the tautological line squares to \(-1\). Rescaling changes that square by \(c\bar c>0\), so \(d_2[\mathcal O(1)]=[-1]\ne0\) in \(\mathbf R^\times/N(\mathbf C^\times)\), and the fixed-cover Čech \(H^2\) edge has nonzero kernel. COH07 and its Appendix D give the explicit calculation, independently peer-checked; Badr et al. (2018, Theorem 4.1) recall the related general obstruction theorem and credit Lichtenbaum. This adds a counterexample beyond Hua’s field-oriented setting, without refuting the field diagrams, resolving the uncertain initial mark, or contradicting the Čech comparison after the colimit over all cover refinements.


**Confidence and reason:** High: explicit semilinear descent calculation and spectral-sequence filtration; its application to an unrestricted scheme formulation is separate from the source’s intended scope.


### Bounded families, field extensions, Tor, and Ext


#### MPL98.B01 — Fixed quotient and Hilbert polynomial boundedness


**File / scan:** 98.pdf, 027–028.  
**Kind:** unproved claim / own illustrative counterexample.  
**Brief source quotation:** “quotients d’un faisceau donné”; “les P_F … en nb finis”.  
**Context:** Hua98, “Les quotients d’un faisceau fixe,” pp. 26–27 (scans 027–028); RS, Orientation, bounded-family question.  
**Register:** RS–Ø; S19 primary-literature comparison.


For a projective scheme over a noetherian base, quotients of a fixed coherent sheaf with Hilbert polynomial in a fixed finite set are bounded, as realized by the corresponding finite union of Quot schemes. This agrees with Hua’s stated target theorem and with Grothendieck (1961b, Theorem 2.1), whose 1962 erratum explicitly restores sufficiency to the printed statement; the full Quot construction is not re-proved here. A fixed Hilbert polynomial without a fixed-quotient bound is insufficient: \(\mathcal O(n)\oplus\mathcal O(-n)\) on \(\mathbf P^1\) has polynomial \(2m+2\) and unbounded \(h^0\). The counterexample distinguishes the role of the two conditions rather than disputing the source’s combined criterion (The Stacks Project Authors, n.d., Tags 0DPB and 0DPC).


**Confidence and reason:** High for the elementary constant-polynomial counterexample; the positive boundedness theorem is a checked literature result, not independently reconstructed in full.


#### MPL98.B02 — Fixed quotient and cycle degree do not bound even pure sheaves


**File / scan:** 98.pdf, 027–028.  
**Kind:** own idea / conditional counterexample.  
**Brief source quotation:** “Chow raffiné”; “cycles associés … de degré borné”.  
**Context:** Hua98, p. 26 (scan 027), pale-pencil variant in the fixed-quotient footnote; p. 27 (scan 028), induction.  
**Register:** RS–Ø; refutes a possible bounded-cycle formulation, not the fixed-Hilbert-polynomial theorem.


On \(\mathbf P^1_k\), the maps \(\mathcal O^2\to\mathcal O(n)\) given by \(X^n,Y^n\) are surjective for every \(n\ge1\). Each quotient is pure of dimension one with the same associated cycle \([\mathbf P^1]\), yet its Hilbert polynomial is \(m+n+1\), so this family is unbounded. This defeats the literal fixed-quotient/bounded-cycle-degree formulation even with purity, strengthening the simpler lower-dimensional-torsion example recorded in BR01. It contradicts that mathematical interpretation of the tentative variant described by Hua, while the faint wording and any intended extra hypothesis remain separate reading questions.


**Confidence and reason:** High for the explicit pure-sheaf counterexample; conditional about the scope intended by the difficult pencil text.


#### MPL98.B03 — Induction requires bounded kernels


**File / scan:** 98.pdf, 028.  
**Kind:** unproved claim / comparison with context.  
**Brief source quotation:** “les noyaux de tous les F′_i sont limités”.  
**Context:** Hua98, pp. 26–27 (scans 027–028), footnote and added kernel argument.  
**Register:** RS–Ø.


The induction needs a uniform quotient sheaf for the lower-dimensional \(F''_i\), obtained from kernels of maps from the fixed sheaf to the already bounded \(F'_i\). Parameterizing those maps and stratifying so that kernels commute with fibres supplies the missing justification in the projective setting. The frozen scan 028 already names the kernels, whereas Hua’s footnote treats the passage through them as its own reconstruction; its proof detail can be useful without replacing that source reading. Neither the mere inclusion \(F''_i\subset F_i\) nor boundedness of the \(F_i\) alone makes arbitrary subsheaves bounded.


#### MPL98.B04 — Properness for variable morphisms and extensions


**File / scan:** 98.pdf, 028,034.  
**Kind:** own idea / boundary counterexample.  
**Brief source quotation:** “noyaux … conoyaux des hom de F en G”; “extensions de F par G”.  
**Context:** Hua98, operation examples p. 33 (scan 034), compared with the projective argument pp. 26–27 (scans 027–028).  
**Register:** RS–Ø; properness qualification checked.


On \(\mathbf A^1_k\), the singleton input families \(\{\mathcal O\}\) are bounded, but the maps \(\mathcal O\xrightarrow{x^n}\mathcal O\) have cokernels \(k[x]/(x^n)\) of unbounded length. Thus boundedness of the internal Hom sheaf does not by itself bound the family of all global maps or their cokernels. The projective setting of the earlier induction provides the needed properness, and Grothendieck’s permanence statement for kernels, images, cokernels, and extensions explicitly assumes it (1961b, Proposition 1.2). This adds a boundary to an unrestricted reading of Hua’s operation list; BR11 gives the finite-presentation argument for unboundedness on the affine line.


**Confidence and reason:** High: explicit cokernels and a uniform presentation-degree bound rule out a finite type parameter family.


#### MPL98.B05 — Field amalgamation over the middle field


**File / scan:** 98.pdf, 029.  
**Kind:** unproved claim / targeted proof check.  
**Brief source quotation:** “On vérifie facilement que c’est là une relation d’équivalence”.  
**Context:** Hua98, “Faisceaux sur des extensions du corps de base,” p. 28 (scan 029), transitivity footnote.  
**Register:** RS–Ø.


Transitivity must amalgamate the two witnessing overfields over the specified middle field, with its embeddings, rather than merely over the original ground field. If the witnesses are \(L,L'\) over \(K_2\), the nonzero tensor product \(L\otimes_{K_2}L'\) has a residue field into which both fields embed, and the two sheaf isomorphisms then compose. This verifies the source’s ease assertion and independently rechecks the repair credited to Hua’s project.


#### MPL98.B06 — Finite-type descent of sheaves and isomorphisms


**File / scan:** 98.pdf, 029–030.  
**Kind:** unproved claim / targeted proof check.  
**Brief source quotation:** “Si X est de type fini sur k”; “K′ … de type fini”.  
**Context:** Hua98, pp. 28–29 (scans 029–030), finite-presentation descent.  
**Register:** RS–Ø; no underlying result file is assumed.


Finite presentation allows a coherent sheaf on a finite type \(X_K\) to descend to a finitely generated coefficient field, and finitely many more coefficients descend an isomorphism, its inverse, and the two identities. The inserted finite type hypothesis on \(X\) matters: it gives the quasi-compact, quasi-separated setting in which this finite-data descent is valid. This agrees with Hua’s reconstruction and supplies the precise role of the condition already present in the source (The Stacks Project Authors, n.d., Tag 01ZR).


#### MPL98.B07 — Arbitrary compositum counterexample


**File / scan:** 98.pdf, 030,033.  
**Kind:** own idea / answer to a written question.  
**Brief source quotation:** “peut-on prendre … n’importe quelle extension composée|commune ?”.  
**Context:** Hua98, p. 29 (scan 030), reads “universelle”; its all-composita discussion p. 32 (scan 033) is the related later passage.  
**Register:** RS–Ø; conditional answer to the frozen question.


Let \(X=\mathbf A^1_k\), take two abstract copies \(K_i=k(t)\), and put \(F_i=K_i[x]/(x-t)\). Aligned embeddings into \(k(t)\) identify the sheaves, while independent embeddings into \(k(t_1,t_2)\) give distinct supports \(x=t_1\) and \(x=t_2\), which remain distinct after every further field extension. Thus an arbitrary prescribed compositum cannot replace a suitable witnessing compositum. This answers the composed/common-extension reading negatively and explains the source’s later instruction to use all relative positions; Hua’s different word remains reading question R04.


**Confidence and reason:** High for the annihilator/support argument; conditional on the doubtful word in the question.


#### MPL98.B08 — Withdrawn base-field invariance


**File / scan:** 98.pdf, 030.  
**Kind:** withdrawn in the same text.  
**Brief source quotation:** deleted “cet ens ne change pas par extension du corps de base”; following “Cependant…”.  
**Context:** Hua98, p. 29 (scan 030), explicitly cancelled base-field-invariance assertion; compare scan 033.  
**Register:** RS–Ø.


The deleted assertion that the class set does not change under ground-field extension should remain withdrawn rather than be reported as a theorem. The point example of B07 shows the difficulty: after choosing \(k'=k(t)\), a geometric class over \(k\) can acquire the \(k'\)-rational representative \(x=t\) or an independent transcendental representative, depending on the amalgamation. This adds an explicit explanation for the source’s cancellation and agrees with Hua’s warning about single-valued base-field change; the surviving sentence on scan 030 is itself unfinished.


#### MPL98.B09 — Universal algebraically closed field and automorphism orbits


**File / scan:** 98.pdf, 031.  
**Kind:** unproved claim / independent re-proof.  
**Brief source quotation:** “de degré de transcendance infini”; “Aut(𝑘̃/k)”.  
**Context:** Hua98, “Un corps universel,” p. 30 (scan 031), modernized corollary numbered 5.  
**Register:** RS–Ø.


For coherent sheaves on finite type \(X/k\), an algebraically closed \(\Omega/k\) of infinite transcendence degree realizes every equivalence class, and equivalence of representatives on \(X_\Omega\) is exactly the \(\operatorname{Aut}(\Omega/k)\)-orbit relation. The proof first descends both objects and a witnessing isomorphism to finitely generated coefficient fields over the ground field, then extends their embeddings to automorphisms of \(\Omega\) using transcendence bases and algebraic closures. This verifies Hua’s interpretation and the source’s substantive assertion; BR04 records the finite-data argument, while R04 records the different corollary number.


#### MPL98.B10 — Set size and finite-presentation qualification


**File / scan:** 98.pdf, 030–031.  
**Kind:** unpursued implication / own boundary example.  
**Brief source quotation:** “un ensemble dans le … univers”; “transcendance infini”.  
**Context:** Hua98, pp. 29–30 (scans 030–031), conventions on universes and a universal field.  
**Register:** RS–Ø.


The field \(\Omega\) is universal for these finite-presentation objects, not a set-sized field containing every field extension of \(k\). Finite transcendence degree is insufficient uniformly: a cyclic sheaf on the affine line defined by a monic degree-\(n\) polynomial with \(n\) algebraically independent coefficients retains those coefficients in its annihilator and cannot be represented over a field of smaller transcendence degree. This adds the size qualification underlying Hua’s explanation and separates the source’s set-of-classes assertion from an unrestricted universal-field claim.


**Confidence and reason:** High: finite-presentation descent and the annihilator of a cyclic module retain the specified algebraically independent coefficients.


#### MPL98.B11 — Multivalued operations and relative positions


**File / scan:** 98.pdf, 032–033.  
**Kind:** self-flagged: requested generalization / own illustrative example.  
**Brief source quotation:** “à généraliser”; “de toutes les façons possibles une extension composée”.  
**Context:** Hua98, “Opérations sur les classes,” pp. 31–32 (scans 032–033).  
**Register:** RS–Ø.


The operation on geometric classes is set-valued because separate inputs do not determine their relative embeddings in one overfield. For the two moving point sheaves of B07, tensor product gives the point sheaf when the supports are aligned and zero when they are distinct, so choosing only one compositum loses valid outputs. This supplies an explicit example for the source’s all-composita instruction and agrees with Hua’s interpretation; independence of the chosen sufficiently large algebraically closed field follows from the finite-data argument in B09.


**Confidence and reason:** High: the tensor product of the two point modules is computed by the sum of their annihilator ideals, which depends on their relative embeddings.


#### MPL98.B12 — Reduced support and inseparability


**File / scan:** 98.pdf, 034.  
**Kind:** own idea / boundary counterexample.  
**Brief source quotation:** “O_(Supp F)_réd”; “K alg. clos”.  
**Context:** Hua98, p. 33 (scan 034), reduced support among the operation examples.  
**Register:** RS–Ø.


Over an imperfect field \(k\) of characteristic \(p\), the reduced algebra \(k[x]/(x^p-a)\), for \(a\notin k^p\), becomes nonreduced after adjoining \(a^{1/p}\). Consequently reduction of support cannot be assumed to commute with arbitrary field extension without a geometric-reducedness condition. The source’s algebraically closed-field restriction addresses this obstacle for finite type schemes, so the example explains rather than removes that restriction and qualifies a broader version of Hua’s operation list.


**Confidence and reason:** High: the polynomial becomes a (p)-th power after the stated extension.


#### MPL98.B13 — Primary components and noncanonical choices


**File / scan:** 98.pdf, 034.  
**Kind:** unproved claim / own illustrative counterexample.  
**Brief source quotation:** “filtration primaire”; “composantes primaires … composantes de son support”.  
**Context:** Hua98, p. 33 (scan 034), primary-filtration and component operations.  
**Register:** RS–Ø.


Canonical support filtrations and primary components attached to isolated support components should be distinguished from arbitrary choices of embedded primary components. For example, \((x^2,xy)=(x)\cap(x^2,y-a x)\) for every \(a\in k\), so an embedded primary component is not unique. The source’s set-valued formulation and its reference to support components leave room for that distinction; this adds a caution to Hua’s list rather than claiming that the manuscript asserts uniqueness of every primary decomposition.


**Confidence and reason:** High: the displayed ideal intersections agree, while their embedded primary factors vary.


#### MPL98.B14 — Tensor boundedness through product of parameter spaces


**File / scan:** 98.pdf, 035.  
**Kind:** unproved claim / targeted proof check.  
**Brief source quotation:** “S‴=S′×_S S″”; “la conclusion pour ⊗ s’ensuit”.  
**Context:** Hua98, “Stabilité des familles limitées,” p. 34 (scan 035).  
**Register:** RS–Ø.


Taking the product of the two finite type parameter spaces and tensoring the pulled-back coherent sheaves gives a finite type family containing all tensor outputs. Different relative field embeddings are represented by different points of that product, so this argument respects the set-valued operations of scans 032–033. This independently checks Hua’s explanation and the source’s construction; unlike Hom, ordinary tensor product already commutes with base change.


#### MPL98.B15 — Hom base change and generic flattening


**File / scan:** 98.pdf, 035–036.  
**Kind:** self-flagged: lemma requested / unproved claim.  
**Brief source quotation:** “Rédiger sous forme de lemme”; “localement sur X”.  
**Context:** Hua98, pp. 34–35 (scans 035–036), Hom base change and the request for a local lemma.  
**Register:** RS–Ø.


After restricting the inputs to a stratum, a finite local presentation of the first sheaf expresses Hom as a kernel between finite sums of the second, and generic flatness of the coefficient module and cokernel makes that kernel commute with further base change. A finite affine cover and common refinement of the parameter strata supply the global boundedness conclusion. This agrees with Hua’s reconstruction and explains why the source asks for a local lemma; it does not silently replace the literal second arguments \(F\) in the displayed Hom kernel by the mathematically intended \(G\). This computes Hom afresh on each stratum; it does not assert that the original global Hom module already commutes with the restriction to that stratum.


#### MPL98.B16 — Finite stratification of complex cohomology


**File / scan:** 98.pdf, 036–037.  
**Kind:** unproved claim / independent re-proof.  
**Brief source quotation:** “décomposition … loc fermés disjoints”; “récurrence noethérienne”.  
**Context:** Hua98, finite-range complex lemma, pp. 35–36 (scans 036–037).  
**Register:** RS–Ø.


For a fixed finite cohomological range, only finitely many terms, cycles, boundaries, and cokernels are needed, and generic flatness on reduced integral strata followed by noetherian induction gives a finite stratification with the desired fibrewise base-change property. The exact sequences defining cycles and boundaries then remain exact after arbitrary base change on each stratum. This verifies Hua’s interpretation using the source’s fixed \(N\), but the result concerns the complex restricted to a stratum and does not identify its cohomology with pullback of the original cohomology across an arbitrary nonflat stratum inclusion (The Stacks Project Authors, n.d., Tag 052A).


#### MPL98.B17 — One finite degree range at a time


**File / scan:** 98.pdf, 036–037,044.  
**Kind:** own idea / boundary counterexample.  
**Brief source quotation:** “pour |q|≤N”; “à degrés … bornés”.  
**Context:** Hua98, pp. 35–36 and chapter plan p. 43 (scans 036–037,044).  
**Register:** RS–Ø.


Over \(k[t]\) with \(k\) infinite, put the two-term blocks \(k[t]\xrightarrow{t-a_n}k[t]\), for distinct \(a_n\), in degrees \(2n,2n+1\). Every dense open contains a point \(t=a_n\) where ordinary cohomology fails base change in that block’s even degree, so no finite stratification works in every degree at once. This adds a sharp reason to retain the finite-range qualification in both the source and Hua’s reconstruction.


**Confidence and reason:** High: the special fibre changes a nonzero multiplication differential to zero.


#### MPL98.B18 — Wrong-ring free resolution in Tor proof


**File / scan:** 98.pdf, 039–040.  
**Kind:** own idea / refutation of a proof step.  
**Brief source quotation:** “résolution libre … comme B_i-module”; “⊗_B L^(i)”.  
**Context:** Hua98, Tor proof p. 39 (scan 040), which repeats the same resolution-ring choice; coefficient-ring doubts on scan 039 remain separate.  
**Register:** RS–Ø; proof step refuted, intended base-change theorem not thereby refuted.


Take \(A=k\), \(B=k[x]\), \(B_1=B_2=k=B/(x)\), and \(M_1=M_2=k\). The \(B_i\)-free resolutions concentrated in degree zero give no positive homology when tensored over \(B\), whereas the resolution \(B\xrightarrow{x}B\) gives \(\operatorname{Tor}_1^B(k,k)=k\). Thus freeness over \(B_i\) does not justify the claimed computation of Tor over \(B\), even when all base-\(A\) flatness conditions hold. This contradicts that proof step in the frozen reading and Hua’s account; B20 gives a repair with genuinely \(B\)-flat resolutions.


**Confidence and reason:** High: two explicit complexes give different degree-one groups.


#### MPL98.B19 — Input flatness is necessary and is present in the lemma


**File / scan:** 98.pdf, 039–040.  
**Kind:** own idea / necessity check.  
**Brief source quotation:** “que les F_α soient plats sur S”; “comme M_i est plat sur A”.  
**Context:** Hua98, Tor-lemma editorial flatness footnote, pp. 38–39 (scans 039–040); see reading disagreement R09.  
**Register:** RS–Ø; only the weakened statement omitting input flatness is refuted.


Set \(A=k[t]\), \(B=A[x]\), \(M_1=B/(tx)\), and \(M_2=B/(x)=A\). The two-term resolution gives \(\operatorname{Tor}_0^B(M_1,M_2)=\operatorname{Tor}_1^B(M_1,M_2)=A\) and higher Tor zero, but after \(t=0\) the modules become \(k[x]\) and \(k\), whose first Tor is zero. Thus flatness of every output Tor group does not replace flatness of the input modules. The frozen lemma explicitly contains input flatness, so this validates the need for its assumption and differs from Hua’s claim that the hypothesis had to be supplied.


**Confidence and reason:** High: the specialization calculation is explicit and independently checked; the source attribution has been corrected in the research record.


#### MPL98.B20 — Corrected Tor base-change mechanism


**File / scan:** 98.pdf, 040–041.  
**Kind:** own idea / refined proof.  
**Brief source quotation:** “la cohomologie de K′ … Tor”; “suite spectrale homologique”.  
**Context:** Hua98, pp. 39–40 (scans 040–041), tensor-resolution proof.  
**Register:** RS–Ø; refinement of the proof step refuted in B18.


Let \(A\) be noetherian, \(B\) finite type over \(A\), and \(B_i\) finitely many finite type \(B\)-algebras with finite \(B_i\)-modules \(M_i\); choose polynomial \(B\)-algebras \(C_i\twoheadrightarrow B_i\) and finite-rank \(C_i\)-free resolutions of the \(M_i\), which are \(B\)-flat resolutions. Their total tensor complex has finite terms over \(C=\bigotimes_B C_i\), and the kernel ideals act null-homotopically, so its finite homology is a module over \(\bigotimes_B B_i\), giving coherence on the intended fibre product. With \(B\) and the \(M_i\) flat over \(A\), the resolutions survive arbitrary \(A\)-base change, and the first-quadrant hyper-Tor spectral sequence gives the requested range when the output Tor groups in that range are \(A\)-flat. This adds a concrete correction to Hua’s repeated proof step without changing the manuscript; BR08R gives the complete argument and Stacks Tag 0620 supplies the two-module comparator.


**Confidence and reason:** High under the stated noetherian, finite type, and flatness hypotheses; this is a proof repair, not a claim of novelty.


#### MPL98.B21 — Dense open and noetherian stratification


**File / scan:** 98.pdf, 039,041.  
**Kind:** self-flagged: question about strengthening / unproved claim.  
**Brief source quotation:** “Peut-on faire plus ?” [uncertain]; “décomposition cellulaire”.  
**Context:** Hua98, pp. 38–40 (scans 039–041), generic-open proposition and corollary.  
**Register:** RS–Ø.


The generic-open assertion can be iterated on reduced closed complements to obtain finitely many locally closed strata for a fixed degree range, after making the finite list of required modules flat. This explains the relation between the proposition and its later corollary and agrees with Hua’s generic-flatness reconstruction once the resolution issue in B18 is repaired. The margin’s possible request for a stronger statement is preserved as uncertain; B17 rules out the unrestricted all-degrees strengthening for arbitrary unbounded complexes.


#### MPL98.B22 — Finite free truncation versus no finiteness


**File / scan:** 98.pdf, 042.  
**Kind:** unproved claim / own idea.  
**Brief source quotation:** “sans conditions de finitude”; later “libres de type fini en tous degrés”.  
**Context:** Hua98, Ext lemma p. 41 (scan 042), finite free truncation and margin.  
**Register:** RS–Ø; finite-generation scope independently checked.


The later finite-rank free terms are substantive because they make termwise Hom commute with arbitrary scalar extension, even though the lemma opens by relaxing finiteness assumptions. For \(A=B=\mathbf Z\), \(M=\bigoplus_{n\ge1}\mathbf Z\), \(N=\mathbf Z\), and \(A'=\mathbf Q\), all positive Ext groups vanish and Hom is the flat module \(\prod\mathbf Z\), but \((\prod\mathbf Z)\otimes\mathbf Q\to\prod\mathbf Q\) misses \((1/n!)_{n\ge1}\). This adds a counterexample to deleting the local finite-presentation condition and supports Hua’s retention of a finite free truncation. The scope check does not say finite rank is necessary for every particular module and base-change pair.


**Confidence and reason:** High: localization gives exactly the rational sequences with one common denominator.


#### MPL98.B23 — Terminal cokernel flatness is essential


**File / scan:** 98.pdf, 042–043.  
**Kind:** own idea / necessity check.  
**Brief source quotation:** “le conoyau de K^N−K^(N+1) est A-plat”.  
**Context:** Hua98, Ext proof pp. 41–42 (scans 042–043), terminal-cokernel discussion.  
**Register:** RS–Ø.


Let \(A=k[t]\), \(B=A[x]\), \(M=B/(x)\), and \(N=B/(x-t)\). The Hom complex of the free resolution of \(M\) is \(A\xrightarrow{t}A\), so its degree-zero cohomology is the flat zero module, but at \(t=0\) the new degree-zero cohomology is \(k\). The terminal cokernel \(A/(t)\) is the obstruction, showing that flatness of the lower Ext groups alone does not suffice. This confirms the mathematical function of the manuscript’s terminal-cokernel condition and agrees with that part of Hua’s explanation.


**Confidence and reason:** High: a two-term complex computes both sides and isolates the failed hypothesis.


#### MPL98.B24 — All degrees of K versus the Ext range


**File / scan:** 98.pdf, 043.  
**Kind:** own idea / correction to contextual interpretation.  
**Brief source quotation:** “est un isom en tt degré”; “en particulier pour p≤N”.  
**Context:** Hua98, final footnote of the Ext proof, p. 42 (scan 043); truncation stated on scan 042.  
**Register:** RS–Ø; source’s all-degree complex assertion independently checked.


The source first compares the cohomology of a complex concentrated in degrees \(0,\ldots,N+1\), with flat terms, flat lower cohomology, and flat terminal cokernel. Descending through the two short exact sequences defining cycles and boundaries proves base change for that complex in every degree. Only the identification of its cohomology with Ext is restricted to \(p\le N\), which the source states separately. Thus Hua’s footnote overcorrects the phrase “en tt degré” on this reading; BR10 proves the distinction without changing the frozen formulas or their coefficient-ring doubts.


**Confidence and reason:** High under the explicitly stated truncation and flatness assumptions; the argument concerns K before its Ext interpretation.


#### MPL98.B25 — Canonical comparison maps must glue


**File / scan:** 98.pdf, 042.  
**Kind:** self-flagged: verification left to the reader.  
**Brief source quotation:** “on laisse au lecteur le soin de vérifier … ‘se recollent’”.  
**Context:** Hua98, p. 41 (scan 042), passage from affine calculation to sheaves.  
**Register:** RS–Ø.


The affine comparison maps must be independent of a chosen resolution and compatible with restriction, not merely abstract isomorphisms of the correct modules. Comparison maps between full projective resolutions are unique up to homotopy, and the canonical tensor–Hom map commutes with restriction; restricting the calculation to \(p\le N\) therefore supplies the required gluing in the finite free local setting. This fills the specific verification left to the reader and agrees with the intended global assertion in Hua’s reconstruction.


#### MPL98.B26 — Tor in fixed degree versus all degrees


**File / scan:** 98.pdf, 037,044.  
**Kind:** own idea / boundary counterexample.  
**Brief source quotation:** “les Tor_i … sont limités”; “Tors locaux”.  
**Context:** Hua98, stability statements pp. 34–36 and chapter plan p. 43 (scans 035–037,044).  
**Register:** RS–Ø.


For \(B=k[x,y]/(x,y)^2\), a minimal free resolution of \(k\) has ranks \(2^i\), so \(\dim_k\operatorname{Tor}_i^B(k,k)=2^i\). The two singleton input families are bounded, but the union of their Tor outputs over all degrees is not. This adds an explicit distinction between each fixed-degree assertion in the source/Hua discussion and a uniform statement across all degrees.


**Confidence and reason:** High: successive syzygies are sums of copies of the two-dimensional square-zero maximal ideal.


#### MPL98.B27 — Proper direct images and coherence


**File / scan:** 98.pdf, 034,044.  
**Kind:** unproved claim / scope clarification.  
**Brief source quotation:** “f:X→Y propre”; “Images directes et R^p f_*”.  
**Context:** Hua98, p. 33 operation list and p. 43 chapter plan (scans 034,044).  
**Register:** RS–Ø.


Properness is needed even to keep a direct image coherent: for \(\mathbf A^1_k\to\operatorname{Spec}k\), the image of \(\mathcal O\) is the infinite-dimensional module \(k[x]\). After stratifying the parameter base so that the coefficient family is flat, a bounded alternating Čech complex on affine target charts computes the proper direct images; further flatness stratification of its coherent cohomology gives the required fibrewise base-change comparison. This agrees with Hua’s qualified interpretation and preserves the properness visible in the source; derived and individual underived base-change assertions remain distinct (The Stacks Project Authors, n.d., Tags 02O5, 052A, and 061Z), with Tag 07VK a comparator when the proper target is the affine parameter base itself.


#### MPL98.B28 — Relative Ext and the qualification quand ça marche


**File / scan:** 98.pdf, 044.  
**Kind:** self-flagged: explicit qualification / unproved claim.  
**Brief source quotation:** “quand ça marche”; “Ext¹ … en tous cas”.  
**Context:** Hua98, “Le plan d’un chapitre,” p. 43 (scan 044).  
**Register:** RS–Ø; no unconditional relative-Ext theorem certified.


The plan explicitly qualifies the relative-Ext proposition and then singles out degree one, but it supplies no complete hypotheses or proof for that final “en tous cas”. For a finitely presented morphism, a clean sufficient modern setting uses a perfect first argument and a bounded complex of finitely presented base-flat sheaves with proper support, so relative derived Hom has the required finiteness and base-change properties (The Stacks Project Authors, n.d., Tag 0A1J). This adds a usable scope to Hua’s interpretation while leaving the manuscript’s broader degree-one expectation an unproved programme item.


#### MPL98.B29 — Base-change detection needs a finiteness scope


**File / scan:** 98.pdf, 044.  
**Kind:** unproved claim / independent re-proof.  
**Brief source quotation:** “Réciproque si Im(S′−S) contient tous les points …”.  
**Context:** Hua98, chapter plan p. 43 (scan 044), base-change detection of boundedness.  
**Register:** RS–Ø.


With both the original and new bases noetherian, a bound after \(T\to S\) can descend without assuming that map finite type: a finite affine cover of its finite type parameter scheme and finite-presentation descent produce finitely many parameter schemes of finite type over \(S\). The image condition lets every relevant fibre class be lifted and then recovered over the original residue field up to the stated equivalence (The Stacks Project Authors, n.d., Tag 01ZR). This supports Hua’s and the source’s reciprocal assertion in that scope. It should not be enlarged to non-quasi-compact bases: a disjoint union of closed points can carry arbitrarily large ranks in one locally coherent family, while no finite type parameter family over \(\mathbf A^1\) bounds those ranks.


#### MPL98.B30 — Finite union and chapter programme


**File / scan:** 98.pdf, 044.  
**Kind:** unproved claim / programme comparison.  
**Brief source quotation:** “Réunion finie de familles limitées est limitée”; “Prop. 1”–“Prop 7”.  
**Context:** Hua98, chapter plan p. 43 (scan 044).  
**Register:** RS–Ø; MPL_131 RN001 and §2 are first-pass representability leads, not theorems used here.


A finite disjoint union of parameter schemes proves closure under finite unions directly. The final sheet assembles seven proposed propositions and five corollary entries into a chapter plan, including operations on bounded complexes; it is not a completed proof of every item. This agrees with Hua’s structural reading and adds a precise account of the still-qualified relative-Ext item; the nearby MPL_131 representability leads concern a further construction step not carried out here.


#### MPL98.B31 — Generic length one does not give a global embedding


**File / scan:** 98.pdf, 027.  
**Kind:** own idea / refutation of an intermediate step.  
**Brief source quotation:** “Si l=1, F_i⊂O_(Z_i)”.  
**Context:** Hua98, p. 26 (scan 027), generic-length-one case in the pale-pencil footnote.  
**Register:** RS–Ø; local generic information does not provide the asserted global inclusion.


Generic length one does not imply that a sheaf embeds globally in the structure sheaf of its support. The quotients \(F_n=\mathcal O_{\mathbf P^1}(n)\) of \(\mathcal O^2\) from B02 have generic length one, but \(\operatorname{Hom}(\mathcal O(n),\mathcal O)=H^0(\mathcal O(-n))=0\) for \(n>0\). This identifies a concrete obstruction in the proposed initial induction step and strengthens the warning about the tentative variant in Hua’s account. It does not decide whether an additional twist or a different condition was intended in the faint text.


**Confidence and reason:** High for the vanishing calculation; conditional as a diagnosis of the intended pale-pencil argument.


#### MPL98.B32 — The explicit question about when Tor base change is an isomorphism


**File / scan:** 98.pdf, 038–040.  
**Kind:** self-flagged: explicit question.  
**Brief source quotation:** “À quelles conditions est-ce un isomorphisme ?”.  
**Context:** Hua98, transition to the Tor base-change problem, p. 37 and later lemma pp. 38–39 (scans 038–040).  
**Register:** RS–Ø.


The question receives a sufficient answer in the following lemma: flatness of the relative scheme and the input modules over the base, together with flatness of the relevant output Tor groups, makes the edge comparisons isomorphisms in the stated range. The input-module assumption is present in the frozen later lemma, and B19 shows why output flatness alone cannot replace it. This links the question to the subsequent development while distinguishing the valid criterion from the resolution-ring defect in its written proof; the coefficient-ring ambiguity in the first formulation remains R07.


### The reused topology and abelian-variety typescripts


#### MPL98.T01 — Reused topology sheets are distinct evidence


**File / scan:** 98.pdf, 004,006,008,010.  
**Kind:** unpursued implication / evidence classification.  
**Brief source quotation:** printed “n° 329”; pages 39,35,37,36.  
**Context:** Hua98, introductory scope and editorial conventions, which omit reused typescripts; scans 004,006,008,010 have no substantive counterpart in its body.  
**Register:** RS–Ø; adds evidence omitted by Hua’s project.


The four topology faces form a distinct reused typescript sequence, identifiable by their printed number and nonconsecutive page order. Their graph, quotient, product, and gluing arguments must not be assimilated to the surrounding handwritten norm argument merely because they share this cote. This adds fully transcribed source material to Hua’s deliberately selective account, without identifying the typescript’s author or edition from resemblance alone.


#### MPL98.T02 — Subspace quotient criterion and literal trace typo


**File / scan:** 98.pdf, 006.  
**Kind:** reading question / targeted proof check.  
**Brief source quotation:** “f(B) est la trace sur f(B) de f(D)”.  
**Context:** Hua98 omits this reused face; its scope statement is the only contextual match for scan 006, printed p. 35.  
**Register:** RS–Ø.


The quoted phrase is self-referential, whereas the quotient-subspace criterion requires that every relatively saturated subset \(B\subseteq A\) open in \(A\) have \(f(B)\) open in \(f(A)\), equivalently the trace on \(f(A)\) of an open subset of the quotient. There is an equivalent formulation with closed subsets; the criterion is an additional requirement, not a property enjoyed by every restriction of a quotient map. Taking inverse images proves this equivalence and identifies the natural proposed correction of the second \(f(B)\) to \(f(A)\). This adds an omitted typescript issue to the context while preserving the literal phrase in the transcription.


#### MPL98.T03 — The product topology and regrouping


**File / scan:** 98.pdf, 004,008.  
**Kind:** unproved claim / targeted proof check.  
**Brief source quotation:** “Produit d’espaces topologiques”.  
**Context:** Hua98 omits reused scans 004 and 008, printed pp. 39 and 37; its scope statement is the relevant contextual match.  
**Register:** RS–Ø.


The finite-support basis for an arbitrary product gives the coordinatewise continuity criterion. Applying that criterion to the canonical regrouping maps in both directions proves the asserted product homeomorphisms and their agreement with the initial-topology formulation. This checks the mechanism of the reused text and adds background omitted by Hua, without importing it as another norm axiom.


#### MPL98.T04 — Theorem of the square and additive Picard pullback


**File / scan:** 98.pdf, 015.  
**Kind:** unpursued implication / targeted source comparison.  
**Brief source quotation:** “(α+β)⁻¹(ξ)=α⁻¹(ξ)+β⁻¹(ξ)”; “(nδ)⁻¹(ξ)=nξ”.  
**Context:** Hua98 omits scan 015, printed p. 99; RS LM7 C.1 and C.5 supply nearby Picard/Jacobian leads.  
**Register:** LM7 C.1 [Known] and LM7 C.5 [Proved] are originating-run claims; their proofs were not supplied.


The modern Picard-group comparator is \(m^*L\simeq p_1^*L\otimes p_2^*L\) for \(L\in\operatorname{Pic}^0(A)\), which immediately gives the additive pullback and \([n]^*L\simeq L^{\otimes n}\) formulas (Milne, 1986/2022, Proposition 9.2 and following paragraph). This supports the typescript’s stated mechanism and adds material omitted by Hua. It is background relevant to the Picard and generalized-Jacobian language of LM7 C.1/C.5, not a check of the Fermat extension class, its exact order, or its splitting claim.


#### MPL98.T05 — Kernel of the Picard homomorphism


**File / scan:** 98.pdf, 017.  
**Kind:** unproved claim / postponed proof.  
**Brief source quotation:** “Nous démontrerons au cours du chapitre”; “le noyau de φ_X est fini”.  
**Context:** Hua98 omits scan 017, printed p. 94; RS LM7 C.1/C.5 and WG H9 contain only thematic matches.  
**Register:** LM7 C.1/C.5 as above; WG H9 is an unchecked planning hunch.


The face announces existence of nondegenerate divisors, surjectivity of their Picard homomorphisms, and a uniform integer controlling the kernel criterion, but those announced proofs are not contained in the supplied face. In the modern abelian-variety formulation, \(\phi_L:A\to A^\vee\) with finite kernel is an isogeny, while \(\phi_L=0\) is equivalent to \([L]\in\operatorname{Pic}^0(A)\); these are different conditions (Milne, 1986/2022, Propositions 8.1 and 9.2). This adds a postponed-proof item absent from Hua’s account; it does not establish the Néron–Tate/intersection formula guessed under WG H9.


#### MPL98.T06 — Jet flags and the last nonzero linear subsystem


**File / scan:** 98.pdf, 019,021,023.  
**Kind:** unproved claim / independent re-proof.  
**Brief source quotation:** “la dimension baisse au plus d’une unité”; “un diviseur X et un seul”.  
**Context:** Hua98 omits the substantive reused argument on scans 019,021,023, printed pp. 90,89,87.  
**Register:** RS–Ø.


For a nonzero finite-dimensional space with an injective local-expansion map, imposing successive coefficient-vanishing conditions drops the dimension by at most one and has zero intersection. The final nonzero kernel is therefore one-dimensional, and it has a \(K\)-rational generator if the space and coefficient functionals are defined over \(K\). The rationality conclusion uses that \(K\)-structure on the ambient space, not merely coefficients in \(K\) in an unrelated chosen basis. This checks the intended flag mechanism in the omitted typescript; the separate indexing defect is treated in T07.


#### MPL98.T07 — Full-rank homogeneous equations do not give a divisor


**File / scan:** 98.pdf, 019.  
**Kind:** own idea / refutation of the written linear-algebra step.  
**Brief source quotation:** “rang n+1”; “μ=0,…,s”; “à un facteur d’homogénéité près”.  
**Context:** Hua98 omits scan 019, printed p. 90; the source’s preceding flag statement is on scan 021.  
**Register:** RS–Ø; literal homogeneous-system claim refuted.


A homogeneous system whose coefficient matrix has full rank \(n+1\) on \(n+1\) unknowns has only the zero solution, so the displayed equations cannot determine a nonzero function up to scale. The elementary basis \(1,t\) already gives the identity matrix and forces both coefficients to vanish. Taking the prefix ending at \(s-1\), immediately before the first full-rank prefix, would instead leave a one-dimensional solution space in the fixed coefficient variables, which is the mechanism of T06. This is a proposed mathematical repair in the notes only and adds an error not discussed by Hua’s selective reading.


**Confidence and reason:** High: direct rank-nullity, with an explicit two-dimensional example.


#### MPL98.T08 — Power-series lower limit is a reading issue


**File / scan:** 98.pdf, 023.  
**Kind:** reading question / unpursued implication.  
**Brief source quotation:** “f=Σ_(j=∞)^∞ c_j M_j(t)”.  
**Context:** Hua98 omits scan 023, printed p. 87; no substantive contextual match beyond its omission statement.  
**Register:** RS–Ø.


The frozen lower limit is \(\infty\), although the preceding enumeration starts at \(j=0\) and the following vanishing conditions use \(c_0,c_1,\ldots\). Replacing that lower limit by zero is a mathematically natural proposed correction, but the transcription retains the printed anomaly. The degree-compatible enumeration itself does make the remaining-coefficient condition an ideal, because multiplying a surviving monomial by a positive-degree monomial raises its degree; this adds a check rather than a modernization of the typescript.


#### MPL98.T09 — Projectivity and historical ampleness terminology


**File / scan:** 98.pdf, 025.  
**Kind:** unproved claim / terminology comparison.  
**Brief source quotation:** “birationnelle et biholomorphe”; “il existe un entier m>0”.  
**Context:** Hua98 omits scan 025, printed p. 95; RS’s abelian-variety planning entries supply thematic rather than textual parallels.  
**Register:** RS–Ø; WG2 Book II entries remain unchecked planning context.


The typescript’s “ample” is defined through the map of the complete linear system, so it should be compared carefully with modern ampleness and very ampleness rather than silently renamed. For an effective nondegenerate line bundle on an abelian variety, the modern criterion gives ampleness, and a suitable tensor power gives a projective embedding (Milne, 1986/2022, Proposition 9.1 and Remark 7.3); Theorem 7.1 separately proves projectivity of every abelian variety. Point separation alone does not supply the full closed-immersion criterion without the corresponding tangent-direction condition (Milne, 2008, I, Proposition 6.3). This adds a precise modern comparator to material omitted by Hua while leaving the historical wording intact.


#### MPL98.T10 — Pencil marks and attribution limit


**File / scan:** 98.pdf, 019.  
**Kind:** reading question / possible marginal query.  
**Brief source quotation:** “utile au cas non singulier?”; “Nouveau!|Revoir!” [both uncertain].  
**Context:** Hua98, note attached to p. 17, mentions the reused p. 18 face (our scan 019) and reads a pencil mark as “Prouver!”.  
**Register:** RS–Ø; no secure attribution of the pencil hand.


The frozen reading does not securely give “Prouver!”, so that contextual word cannot be promoted to a confidently recorded authorial demand for proof. The partially legible note about the nonsingular case may indicate a question about the theorem immediately below, but its exact wording and the second pencil annotation remain doubtful. This differs from Hua’s reading and prevents both an unwarranted correction and a confident attribution of the reused typescript or pencil hand.


#### MPL98.T11 — The omitted index-zero term in the typescript expansion


**File / scan:** 98.pdf, 019.  
**Kind:** reading question.  
**Brief source quotation:** “Σ_(i=1)^n λ_i c_(iμ)” after “f_0,…,f_n”.  
**Context:** Hua98 omits scan 019, printed p. 90; no substantive matching formula is present in the supplied context.  
**Register:** RS–Ø.


The coefficient expansion starts its inner sum at \(i=1\), although the stated basis and the earlier expression for \(f_\lambda\) run from \(i=0\) to \(n\). Including the index-zero term is the natural algebraic repair, independent of the later rank error in T07. This records an additional literal anomaly absent from Hua’s reading and leaves the written lower limit unchanged.


#### MPL98.T12 — Function versus divisor in the typed equality


**File / scan:** 98.pdf, 021.  
**Kind:** reading question.  
**Brief source quotation:** “(f+cf′)g=X_c−Y”.  
**Context:** Hua98 omits scan 021, printed p. 89; only its general scope statement matches the reused face.  
**Register:** RS–Ø.


The displayed left side is a function while the right side is a divisor; the preceding argument uses divisor notation for the corresponding products. An outer divisor operator on the product would make the statement well typed, but it is not supplied in the frozen transcription. This adds a distinct formula-level issue from the omitted typescript and does not affect the independent finite-dimensional flag proof in T06.


#### MPL98.T13 — Compatible overlap homeomorphisms need not embed the pieces


**File / scan:** 98.pdf, 010.  
**Kind:** unproved exercise / own counterexample.  
**Brief source quotation:** “n’est pas suffisante … (exerc.)”.  
**Context:** Hua98 omits scan 010, printed p. 36; its omission statement is the relevant contextual match.  
**Register:** RS–Ø.


Take \(X_1=\{a,b\}\) discrete, \(X_2=\{a,c\}\) with the upper-set topology of \(a<c\), and \(X_3=\{c,b\}\) with that of \(c<b\), identifying equal labels on the singleton overlaps. Every overlap map is a homeomorphism and the compatibility conditions hold, but the quotient has opens \(\varnothing,\{b\},\{b,c\},\{a,b,c\}\). The induced topology on \(X_1\) omits the open singleton \(\{a\}\), so its canonical map is not an embedding. This supplies a checked example for the exercise absent from Hua’s account; it does not weaken the uniform open-overlap or closed-overlap hypotheses of T14.


**Confidence and reason:** High: all eight subsets of the three-point quotient were checked directly; a research collaborator independently checked the same finite topology.


#### MPL98.T14 — The sufficient gluing hypotheses and the interval quotient


**File / scan:** 98.pdf, 010.  
**Kind:** unproved claim / targeted proof check.  
**Brief source quotation:** “recollement”; “ouverts … fermés”.  
**Context:** Hua98 omits scan 010, printed p. 36; its scope statement is the relevant contextual match.  
**Register:** RS–Ø.


For compatible gluing, the positive result applies when all overlaps are open in both participating pieces, or when all are closed in both pieces. Saturating an open or respectively closed subset of one piece gives the same kind of trace on every other piece and proves that the original pieces embed. The interval-to-circle example similarly uses the locally finite family of closed integral translates to verify the quotient topology. These checks fill the topological mechanism omitted by Hua; T13 separately supplies the exercise’s counterexample when the overlap conditions are removed.


### Reading questions raised by the supplied context


#### MPL98.R01 — XVII versus XVIII on the cover


**File / scan:** 98.pdf, 002.  
**Kind:** reading question.  
**Brief source quotation:** cover “SGA 4 XVII”.  
**Context:** Hua98, p. 1 (scan 002), cover footnote reads XVIII and proposes comparison with XVII §6.3; RS Orientation names XVII §6.3.  
**Register:** H98; reading comparison, not a theorem check.


The frozen cover reads XVII, whereas Hua’s project records XVIII and comments on the discrepancy with the norm exposé. The published norm construction is in XVII §6.3, but mathematical fit cannot decide whether an extra stroke is present on the cover. This is a direct reading disagreement between the two witnesses and leaves the frozen cover unchanged.


#### MPL98.R02 — Cor/Cn versus Hua Can


**File / scan:** 98.pdf, 007,011–013.  
**Kind:** reading question.  
**Brief source quotation:** “Cor|Cn” in the norm-section labels.  
**Context:** Hua98, notation convention and pp. 6,10–12 (scans 007,011–013), normalizes the label to Can and discusses Cm-like handwriting.  
**Register:** H98; notation itself remains uncertain.


The repeated label is frozen as the doubtful reading Cor|Cn, while Hua’s project uses Can for the canonical section. The mathematical construction supports interpreting the symbol as the designated norm section, but does not settle its individual letters. This records the contextual alternative without replacing the cross-page notation table or any label in the transcription.


#### MPL98.R03 — Phi/Cl versus Hua gothic F


**File / scan:** 98.pdf, 030–033.  
**Kind:** reading question.  
**Brief source quotation:** “Φ|Cl(X/k)”.  
**Context:** Hua98, conventions and pp. 29–32 (scans 030–033), uses a Gothic F for the set of geometric classes.  
**Register:** RS–Ø.


The frozen readings retain the competing Φ/Cl forms, while Hua’s project consistently chooses a Gothic letter. Both accounts assign the expression the same role as the class set, but that semantic agreement does not establish the alphabet in the ink. This is an unresolved palaeographic question, not a new definition introduced into the transcription.


#### MPL98.R04 — Composed or common extension versus universal extension


**File / scan:** 98.pdf, 030.  
**Kind:** reading question.  
**Brief source quotation:** “extension composée|commune”.  
**Context:** Hua98, p. 29 (scan 030), reads “extension universelle”.  
**Register:** RS–Ø.


The three candidate words lead to different mathematical questions, so the contextual “universelle” cannot be substituted merely because the next page discusses a universal field. The counterexample in B07 is conditional on the composed/common-extension reading and does not resolve the handwriting. This records a consequential disagreement with Hua’s reading while preserving the source’s doubt mark.


#### MPL98.R05 — The unfinished final contracted-product assertion


**File / scan:** 98.pdf, 014.  
**Kind:** reading question.  
**Brief source quotation:** “conserve les compos…”.  
**Context:** Hua98, end of p. 13 (scan 014), expands the unfinished contracted-product discussion.  
**Register:** H98; completion distinguished from source text.


The source ends in an unfinished word after the assertion that the functor preserves something, rather than giving a complete list of preserved operations. Hua’s developed formulation is a possible mathematical reconstruction and belongs with the unproved compatibility question in N13. The transcription retains the visible interruption and does not adopt the completion.


#### MPL98.R06 — Example labels and the deleted final item


**File / scan:** 98.pdf, 034.  
**Kind:** reading question.  
**Brief source quotation:** labels a), b), c), circled d–h, and deleted i).  
**Context:** Hua98, “Exemples,” p. 33 (scan 034), reorganizes or renames examples and omits the final cancelled item.  
**Register:** RS–Ø.


The source’s interleaved lettered and circled labels, insertion arrows, and cancelled final item are part of the working organization of the page. Hua’s reordered list is useful as exposition but is not evidence for changing those labels or dropping the cancellation. The frozen transcription therefore differs deliberately in structure and preserves the unreadable cancelled words with doubt macros.


#### MPL98.R07 — Coefficient rings in the base-change formulas


**File / scan:** 98.pdf, 039,041–043.  
**Kind:** reading question.  
**Brief source quotation:** Tor/Ext coefficient subscripts O_S, O_Y, O_X; Hom_(A|B).  
**Context:** Hua98, base-change sections pp. 38–42 (scans 039,041–043), regularizes the coefficient rings.  
**Register:** RS–Ø.


The frozen formulas include literal base-ring subscripts and explicit S/Y or A/B doubts, while the algebraic proof and Hua’s reconstruction generally require the relative scheme ring. The mathematical checks B18–B24 state their rings explicitly and do not turn a proposed correction of a subscript into a fact about the ink. This differs from the contextual normalization and is particularly material where changing the ring changes the Tor or Ext group itself.


#### MPL98.R08 — The adjective after familles


**File / scan:** 98.pdf, 044.  
**Kind:** reading question.  
**Brief source quotation:** “familles virtuelles” [uncertain].  
**Context:** Hua98, “Le plan d’un chapitre,” p. 43 (scan 044), reads “familles universelles”.  
**Register:** RS–Ø.


The frozen adjective is the doubtful reading “virtuelles”, whereas Hua’s project chooses “universelles”. The boundedness argument only needs a parameter family containing the classes, so mathematical context alone cannot justify replacing the word by a stronger universal-family claim. This keeps the disagreement open and avoids importing representability into the final chapter plan.


#### MPL98.R09 — Input flatness is present in the frozen lemma


**File / scan:** 98.pdf, 039–040.  
**Kind:** reading question / contextual claim contradicted.  
**Brief source quotation:** “que les F_α soient plats sur S”.  
**Context:** Hua98, Tor-lemma footnote p. 38 (scan 039), says the input-sheaf flatness hypothesis was added because the proof uses it.  
**Register:** RS–Ø; source comparison contradicts that particular editorial claim.


The frozen lemma explicitly includes flatness of the \(F_\alpha\) over \(S\), and scan 040 repeats the assumption for the \(M_i\). Thus Hua’s claim to have supplied a missing hypothesis differs from the frozen reading; B19 tests the necessity of an assumption already present. An earlier research draft in this run followed the contextual omission claim, and this source comparison corrected the note and event disposition without altering the frozen transcription.


#### MPL98.R10 — Corollary 3 versus the modernized Corollary 5


**File / scan:** 98.pdf, 031.  
**Kind:** reading question.  
**Brief source quotation:** “Corollaire 3”.  
**Context:** Hua98, “Un corps universel,” p. 30 (scan 031), prints “Corollaire 5”.  
**Register:** RS–Ø.


The corollary heading is frozen as 3, while Hua’s project labels the same universal-field assertion 5. Neither the surrounding modern numbering nor the mathematical dependence settles the manuscript numeral. The source number is therefore retained, with the contextual number recorded here for cross-reference.


#### MPL98.R11 — The second argument of the sheaf Hom formula


**File / scan:** 98.pdf, 016.  
**Kind:** reading question.  
**Brief source quotation:** “Φ_A(X)=Hom_G(X,E)”.  
**Context:** Hua98, p. 15 (scan 016), repairs the second argument to A.  
**Register:** RS–Ø.


The frozen Hom expression has \(E\), although the surrounding construction fixes \(A\) and the intended represented sheaf uses \(\operatorname{Hom}_G(X,A)\). Hua’s \(A\) is the natural mathematical reconstruction, as explained in G02, but it does not change the literal expression. This separates a source-letter question from the verified equivalence of categories.


#### MPL98.R12 — A-flat versus A-free in the Hom complex


**File / scan:** 98.pdf, 043.  
**Kind:** reading question.  
**Brief source quotation:** “dont les termes sont A-plats”.  
**Context:** Hua98, Ext proof footnote p. 42 (scan 043), attributes A-free to the source and then corrects it to A-flat in its modernized proof.  
**Register:** RS–Ø.


The frozen wording is “A-plats”, not “A-libres”. Finite sums of the coefficient module \(N\) are \(A\)-flat under the stated hypothesis, but need not be \(A\)-free, so the distinction is mathematically consequential. This differs from Hua’s report of the source wording while agreeing with its corrected proof and the mechanism used in B23–B24; no frozen coefficient symbol is changed.


#### MPL98.R13 — The conclusion about extensions is already in the frozen text


**File / scan:** 98.pdf, 028.  
**Kind:** reading question / contextual reconstruction qualified.  
**Brief source quotation:** “Donc les extensions F_i de F′_i par F″_i sont limités”.  
**Context:** Hua98, fixed-quotient footnote p. 27 (scan 028), says its reading gave the opposite implication and that it rewrote it.  
**Register:** RS–Ø.


The frozen concluding line already states boundedness of the extensions \(F_i\) from the bounded \(F'_i,F''_i\), the direction required by the induction. Hua’s claimed reversal therefore reflects a different reading, not a correction that should be imported into this transcription. This complements the kernel comparison in B03 and illustrates why a mathematically improved contextual text cannot serve as the diplomatic witness.


## Standing question 1: steps explicitly left unverified or undeveloped

The following are words on the supplied faces, rather than doubts inferred merely from a missing proof. Bracketed uncertainty follows the frozen transcription. A request to develop an explanation is not automatically a conjecture that the assertion is true; a marginal mark on an unidentified typescript is not automatically in its author’s hand. The numbered notes provide the mathematical and contextual dispositions.

| File | Scan | Words or mark | What is left open, and where it is treated |
|---|---:|---|---|
| 98.pdf | 013 | “Expliquer la relation de cet exemple avec le cas général, peut-on …” | The tail remains doubtful; the relation between the G-set example and the general construction is explicitly requested. N15 distinguishes covering descent from ramified finite locally free cases. |
| 98.pdf | 014 | “à développer” [uncertain, double underlining]; unfinished “compos…” | The transport-of-structure discussion is incomplete. N13 and R05 do not complete the source’s sentence. |
| 98.pdf | 016 | “à développer” | The sheaf/group-action framework needs development. G01–G04 supply the stated site and injective/coinduced qualifications. |
| 98.pdf | 020 | “[identités] à développer” | The marginal first word is uncertain; the relative/slice identifications are checked in G05–G06. |
| 98.pdf | 020 | “Tout ceci est à généraliser aux hyperfaisceaux quelconques” | This is an explicit requested generalization. G07 distinguishes an ordinary-cover theorem from a separate hypercover theorem and its hypotheses. |
| 98.pdf | 027 | “Il y a deux choses à prouver” | The fixed-quotient criterion has two directions to establish. B01 compares the published theorem; B02 and B31 test the faint tentative cycle variant and its initial step. |
| 98.pdf | 030 | “Question : peut-on prendre … n’importe quelle extension [composée\|commune] ?” | The source asks whether any compositum may be used. B07 answers the mathematical question with relative embeddings made explicit; R04 records the reading difference from Hua. |
| 98.pdf | 030 | Struck assertion that the set “ne change pas par extension du corps de base” | This is withdrawn on the same face, not a live theorem. B08 distinguishes a base-relative equivalence relation from the deleted unrestricted statement. |
| 98.pdf | 032 | “à [généraliser]” [uncertain]; request to introduce the proposition and definition | The operation framework remains in draft form. B11 illustrates why all compatible relative positions matter. |
| 98.pdf | 036 | “Rédiger sous forme de [lemme]”; “localement sur X” | The source explicitly asks for a local lemma and observes that the chosen local presentations are only local. B15 gives the kernel/base-change mechanism. |
| 98.pdf | 038 | “À quelles conditions est-ce un isomorphisme ?” | The Tor comparison is posed as a question before the following lemma. B32 relates it to B18–B20 and does not treat the question as already settled at its first occurrence. |
| 98.pdf | 039 | “[Peut-on faire plus ?]” [whole margin uncertain] | An apparent question about extending the lemma. B21 preserves the uncertainty and does not substitute Hua’s different reading as a secure demand. |
| 98.pdf | 040 | Margin proposing, instead of the spectral sequence, a result on cohomology of a complex | A proposed alternative proof method, not a new mathematical hypothesis. B20 gives the repair; the source margin itself is not silently expanded. |
| 98.pdf | 042 | “on laisse au lecteur le soin de vérifier … ‘se recollent’” | The affine comparison maps must glue. B25 checks independence of resolutions and restriction compatibility in the asserted range. |
| 98.pdf | 044 | “quand ça marche”; “en tous cas” | Relative Ext is qualified, with a stronger expectation for degree one. B28 records the unresolved generality rather than treating the chapter plan as a proved theorem. |

Three other cases require separate classification. On **scan 011**, the frozen margin retains an uncertain exclamation/question mark; N08 discusses the nearby quotient/base-change issue without calling that punctuation a definite doubt. On reused **scan 019**, “utile au cas non singulier?” and “Nouveau!|Revoir!” are uncertain pencil readings; T10 records them as possible marginal queries, with no secure attribution of the hand. On reused **scan 017**, “Nous démontrerons au cours du chapitre” expressly postpones the announced abelian-variety results, while reused **scan 010** labels the insufficiency of overlap homeomorphisms an exercise; T05 and T13 treat those as statements of the unidentified typescript, not automatically as Grothendieck’s own conjectures.

There are also claims made with ease-language rather than an explicit doubt: scan 009, “Je dis qu’on a” (N07); scans 012–013, “trivialement,” “on vérifie aussitôt,” and “très facilement” (N09, N11–N12); scan 029, “On vérifie facilement” (B05); scan 032, “On voit facilement” (B09, B11); scan 035, the appeal to a general lemma (B15); and reused scan 021, “c’est clair” (T06). They are included among the unproved-claim notes but are not counted as authorial declarations of uncertainty.

## Standing question 2: title sheets, headings, and page counts

| File | Scan | Title or heading carried by the face | Status |
|---|---:|---|---|
| 98.pdf | 002 | “[Formalisation\|Formulation] des Normes”; “Cf aussi SGA 4 XVII” | Cover/title sheet. The first word remains uncertain; the marginal “P” is also uncertain. R01 records Hua’s different Roman-numeral reading. |
| 98.pdf | 003 | “Normes” | Heading of the handwritten construction. |
| 98.pdf | 011 | “Théorie axiomatique des morphismes [normés\|normants]” | Internal heading, with the frozen alternative retained. |
| 98.pdf | 026 | “Familles limitées”; “cf. SGA 6 XIII” | Second cover/title sheet. |
| 98.pdf | 044 | “Familles limitées de faisceaux cohérents” | Chapter-plan heading. |
| 98.pdf | 044 | “Familles limitées de complexes de faisceaux cohérents” | Companion heading; the insertion changes “finis” to “bornés” for the degrees, with punctuation and the final parenthesis left as written and marked where unreadable. |
| 98.pdf | 008 | “§ 4. Produit d’espaces topologiques” | Reused typescript heading, printed p. 37. |
| 98.pdf | 017 | “4 - Applications du théorème du carré aux variétés abéliennes” | Reused typescript heading, printed p. 94. |
| 98.pdf | 023 | “3-5 - Le Noyau du théorème du Carré” | Reused typescript heading, printed p. 87. |

The ten reused typescript faces carry the following printed pagination. These numbers belong to the reused text; they are not represented as the manuscript author’s handwritten page numbers.

| Supplied scan | Printed page | Repeated typescript identifier | Subject |
|---:|---:|---|---|
| 004 | 39 | n° 329 | Graph/initial-topology and product material |
| 006 | 35 | n° 329 | Restriction of quotient topologies |
| 008 | 37 | n° 329 | Products of topological spaces |
| 010 | 36 | n° 329 | Gluing and the interval quotient |
| 015 | 99 | n° 268 | Picard-zero pullback formulas |
| 017 | 94 | n° 268 | Applications of the theorem of the square |
| 019 | 90 | n° 268 | Coefficient matrices and a further theorem |
| 021 | 89 | n° 268 | Successive coefficient conditions |
| 023 | 87 | n° 268 | Kernel of the theorem of the square |
| 025 | 95 | n° 268 | Projectivity and linear systems |

**Page-count answer.** There is no confidently read authored statement of a total page count such as “19 pages” or a range such as “Pages 1–67.” The supplied range contains **43 scans: 2 covers, 10 reused typescript faces, and 31 text faces**, as recorded in the inventory. No whole face is classified as a cancelled draft, although many individual passages are deleted. The archival foliation runs 1–43 and is recorded only in TeX comments; no confidently identified authorial handwritten page/sheet number warranted a \(\backslash\mathrm{mspage}\) entry. The seven propositions and five corollary entries on scan 044 count planned results, not pages.

Neither the typescript’s author nor its edition has been established in this run. The catalogue’s “from 1966–1967” placement is not a date proved for each face, and the cover references alone do not date the reused material.

## Disposition of the supplied results register

This table supplements the per-note register fields. It reports the bearing of the supplied pages on the entries, not a new assessment of their unsupplied proofs.

| Register ID / lead | Supplied status and locator | Bearing and disposition in this package |
|---|---|---|
| **98-axiomatic-norms-can-section** (H98) | Hua finding; conjecture (unsearched), Lean card partly proved; RS line 460, with orientation at lines 18–20 | N01–N15 supply concrete models, proofs of selected compatibilities, and the empty-base degree refinement. No Lean source or certificate was supplied or executed. |
| **LM7 E.23** | Open; RS line 347, originating locator §51.16, folios 733v–736v, scans 172–178 | G11: group-cohomology methods do not determine the remaining section-map fibres. No status change. |
| **FLAGGED_149 B9** | Open; RS line 348, cote 149, scans 35–36 | G11: no solution of the prime-to-\(p\) point question appears in these scans. |
| **LM1 D.11** | Open; RS line 349, folios 608–610, integral classification | G11: the integral \(\mu_2\)-extension problem remains outside the proved content here. |
| **LM4 D.12** | Open; RS line 350, cited low-type/profinite torsion passages | G11: the spectral-sequence method does not classify torsion in the full profinite groups. |
| **LM4 F.7** | Open; RS line 351, §30, scans 383–387 | G11: no completion-centralizer comparison for the stated \(A_5\) problem is proved. |
| **LM7 C.1 / LM7 C.5** | Known / Proved, originating claims; the Picard/generalized-Jacobian rows of RS, including line 374 for C.5 | T04–T05 provide relevant Picard-zero background, not a check of the Fermat extension class, its exact order, splitting, or degree. |
| **LM7 E.124** | Proved, originating claim; RS line 378 | N04 supplies a general trace/norm mechanism, not a verification of the stated unit-norm or class-group calculation. |
| **SECTIONS_OVER_Q A.179 / A.184** | Proved, originating claims; RS lines 387 and 363 | N04 does not re-derive the arithmetic tower and residue results. |
| **WG H9** | Unchecked hunch; RS line 447 | T05 does not establish the proposed Néron–Tate/intersection identification. |
| **WG H2** | Unchecked hunch; RS line 454 | G09–G12 discuss monodromy but do not settle the stated arithmetic vanishing-cycle hunch. |
| **WG2 §1.1 #3 / §Summary #2** | Unchecked planning questions; RS lines 448 and 453 | The reused abelian-variety text is additional material relevant to inventory, without identifying a new Book II theorem. |
| **MPL_131 RN001 / §2 / 10** | First-pass leads; RS lines 430–431 and 409 | B30 separates boundedness inputs from a further representability construction; the underlying cote 131 manuscript and return were not supplied. |
| **S19; Book I I.VI** | Planning prompts; context README lines 9 and 15–17 | P01–P02 and the primary-source ledger provide the requested comparison with print; no inferred priority, dependence, or representability theorem is asserted. |

All register entries above retain their supplied status. The exact background uses and the narrower checks performed here appear in CHECK_EVENTS.tsv.

## Proof documentation and verification limits

The extended arguments are in [norm_research.md](research/norm_research.md), [cohomology_research.md](research/cohomology_research.md), [boundedness_research.md](research/boundedness_research.md), and [root_proof_checks.md](research/root_proof_checks.md). The cohomology peer review and the Ext-finiteness memo add independent checks of the main boundary examples. Finite computations are distinguished from theorem-prover certificates; no Lean result is claimed. The primary-source ledger identifies every inspected electronic witness and separates statements read, selected proof passages checked, metadata-only records, and unread leads.

The main ledger contains mathematical checks and research-stage source comparisons. Ordinary reading of the manuscript during transcription is not relabelled as a proof check. Its “used and rechecked” source-comparison rows identify textual disagreements only; its “carried as background” rows do not certify the underlying result. Existing collaborators’ event records remain in research/ so that consolidation does not conceal their original claim identifiers or limitations.

## References

The bracketed keys are stable identifiers for integration into the final notes. Year suffixes in this consolidated list follow alphabetical title order: **Grothendieck 1961a = EGA III_1; 1961b = FGA IV. Rydh 2008a = Families of zero cycles II; 2008b = Hilbert and Chow schemes.** The norm memo and final notes use these same suffixes; older event wording has been normalized by title.

**[BBL18]** Badr, E., Bars, F., & Lorenzo García, E. (2018). The Picard group of Brauer–Severi varieties. *Open Mathematics, 16*, 1196–1203. [https://doi.org/10.1515/math-2018-0101](https://doi.org/10.1515/math-2018-0101). [Author-hosted paper](https://mat.uab.cat/~francesc/Brauer.pdf).

**[SGA6]** Berthelot, P., Grothendieck, A., & Illusie, L. (Eds.). (1971). *Théorie des intersections et théorème de Riemann–Roch: Séminaire de Géométrie Algébrique du Bois Marie 1966–1967 (SGA 6)* (Lecture Notes in Mathematics, Vol. 225). Springer. [https://doi.org/10.1007/BFb0066283](https://doi.org/10.1007/BFb0066283). [Original publisher front matter](https://link.springer.com/content/pdf/bfm:978-3-540-36936-3/1).

**[SGA4-XVII]** Deligne, P. (1973). Cohomologie à supports propres (Exposé XVII). In M. Artin, A. Grothendieck, & J.-L. Verdier (Dirs.), *Théorie des topos et cohomologie étale des schémas: Tome 3 (SGA 4)* (Lecture Notes in Mathematics, Vol. 305, pp. 250–480). Springer. [https://doi.org/10.1007/BFb0070723](https://doi.org/10.1007/BFb0070723). [Retypeset mathematical text actually used](https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf). [Author's IAS bibliography](https://publications.ias.edu/deligne/paper/350).

**[FERR98]** Ferrand, D. (1998). Un foncteur norme. *Bulletin de la Société Mathématique de France, 126*(1), 1–49. [https://doi.org/10.24033/bsmf.2319](https://doi.org/10.24033/bsmf.2319). [Original-paper PDF](https://www.numdam.org/article/BSMF_1998__126_1_1_0.pdf).

**[EGA-III1]** Grothendieck, A. (1961a). Éléments de géométrie algébrique: III. Étude cohomologique des faisceaux cohérents, première partie. *Publications Mathématiques de l'IHÉS, 11*, 5–167. [https://doi.org/10.1007/BF02684273](https://doi.org/10.1007/BF02684273). Written with the collaboration of J. Dieudonné. [NUMDAM record](https://www.numdam.org/item/PMIHES_1961__11__5_0/); [primary PDF mirror](https://wstein.org/sga/circle/EGAIII.1.pdf).

**[FGA-IV]** Grothendieck, A. (1961b). Techniques de construction et théorèmes d'existence en géométrie algébrique IV: Les schémas de Hilbert. In *Séminaire Bourbaki: Années 1960/61, exposés 205–222* (Vol. 6, Exposé 221, pp. 249–276). Société mathématique de France. [Original-paper PDF](https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf).

**[FGA-IV-ERR]** Grothendieck, A. (1962). Erratum à l'exposé n°221. In *Séminaire Bourbaki: Année 1961/62, exposés 223–240* (Vol. 7, p. 302). Société mathématique de France. [Original erratum](https://www.numdam.org/item/SB_1961-1962__7__302_1.pdf).

**[EGA-IV2]** Grothendieck, A. (1965). Éléments de géométrie algébrique: IV. Étude locale des schémas et des morphismes de schémas, seconde partie. *Publications Mathématiques de l'IHÉS, 24*, 5–231. [https://doi.org/10.1007/BF02684322](https://doi.org/10.1007/BF02684322). Written with the collaboration of J. Dieudonné. [NUMDAM record](https://www.numdam.org/item/PMIHES_1965__24__5_0/); [primary PDF mirror](https://wstein.org/sga/circle/EGAIV.2.pdf).

**[HS53]** Hochschild, G., & Serre, J.-P. (1953). Cohomology of group extensions. *Transactions of the American Mathematical Society, 74*(1), 110–134. [https://doi.org/10.1090/S0002-9947-1953-0052438-8](https://doi.org/10.1090/S0002-9947-1953-0052438-8). [Original-paper PDF](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/hochschild-serre.pdf).

**[SGA6-XIII]** Kleiman, S. (1971). Les théorèmes de finitude pour le foncteur de Picard (Exposé XIII). In P. Berthelot, A. Grothendieck, & L. Illusie (Eds.), *Théorie des intersections et théorème de Riemann–Roch (SGA 6)* (Lecture Notes in Mathematics, Vol. 225, pp. 616–666). Springer. [https://doi.org/10.1007/BFb0066296](https://doi.org/10.1007/BFb0066296). **Metadata-only inspection in this run; no internal theorem certified from the primary chapter.**

**[MILNE-AVS22]** Milne, J. S. (2022, January 2). *Abelian varieties* [Corrected author version]. [Author's PDF](https://www.jmilne.org/math/xnotes/AVs.pdf). Original work published as “Abelian varieties,” in G. Cornell & J. H. Silverman (Eds.), *Arithmetic geometry* (pp. 103–150), Springer, 1986. For an original/revised author–date citation, use **Milne (1986/2022)** and retain the section numbers of this corrected version.

**[MILNE-AV08]** Milne, J. S. (2008). *Abelian varieties* (Version 2.0) [Course notes]. [Author's PDF](https://www.jmilne.org/math/CourseNotes/AV.pdf). This is a separate, longer work from the corrected 1986 chapter above.

**[ROBY63]** Roby, N. (1963). Lois polynomes et lois formelles en théorie des modules. *Annales scientifiques de l'École normale supérieure, 3e série, 80*(3), 213–348. [https://doi.org/10.24033/asens.1124](https://doi.org/10.24033/asens.1124). [Official publication record](https://www.numdam.org/articles/10.24033/asens.1124/). **Metadata checked; full paper not inspected in this run.**

**[RYDH-ZC08]** Rydh, D. (2008a, April 11). *Families of zero cycles and divided powers: II. The universal family* [Preprint]. [Author's PDF](https://davidrydh.se/papers/famzerocyclesII-20080411.pdf).

**[RYDH-HC08]** Rydh, D. (2008b). *Hilbert and Chow schemes of points, symmetric products and divided powers* [Thesis paper III, KTH]. [Author-hosted thesis paper](https://people.kth.se/~dary/thesis/thesis-paperIII.pdf). This entry identifies the inspected thesis paper, not an asserted journal publication.

**[SERRE51]** Serre, J.-P. (1951). Homologie singulière des espaces fibrés. Applications. *Annals of Mathematics, 54*(3), 425–505. [Original-paper PDF](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/serre.pdf).

**[STACKS]** The Stacks Project Authors. (n.d.). *The Stacks Project*. Retrieved November 18, 2026, from [https://stacks.math.columbia.edu](https://stacks.math.columbia.edu). The individual stable tag URLs and precise statements used are listed in §3. In the notes, cite the corporate author and tag, rather than an inferred publication year for a continuously maintained page.


Exact passage locators, electronic-witness qualifications, and individual Stacks tags are recorded in [primary_sources.md](research/primary_sources.md). Metadata-only entries are included as identified leads, not as inspected mathematical proofs.
