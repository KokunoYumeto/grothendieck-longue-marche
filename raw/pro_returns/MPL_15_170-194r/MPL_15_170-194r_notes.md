# MPL_15_170-194r — Research notes

## Status, witnesses and method

These notes concern **cote 15, scans 170–171 and 179–194**, in that order: eighteen selected scans, not a claim about the extent of the underlying texts. The diplomatic transcription was frozen on **17 November 2026 at 12:44:19 UTC**; the context was opened at **12:44:30 UTC**. All comparisons below were made after that barrier and leave the frozen text unchanged.

The current manuscript was read and audited visually in a single transcription stream. Research comparisons used the supplied context, the complete RESULTS_STATE register, and primary literature identified at the end; research assistance did not divide the transcription. Earlier archive transcriptions and research returns are **first-pass claims unless their own entry explicitly reports review**; Hua's modernised reading is his project's credited interpretation, not a diplomatic witness or a result established by this return. No open register item is declared settled merely by a contextual citation.

Each numbered note has an allowed kind, a current scan and short quotation or a stated absence, a contextual locator and the relation to it, and relevant register IDs. A note's explanatory body has one to four sentences; metadata and comparison tables are separate. The new algebraic tests are labelled **own idea**, with confidence and limitations; several other calculations are explicitly credited to the earlier returns rather than rederived.

### Source key

| Short name | Exact supplied file / meaning |
|---|---|
| **Current**, or **15/NNN** without another source label | `MPL_15_170-194r_transcription.tex` and the corresponding `pages/MPL_15_170-194r_15_scanNNN.tex`; NNN is the PDF scan number. |
| **CT** | `context/MPL_16+47+54+44_transcription.tex`; CT16/047 means cote 16, scan 47, in that contextual transcription. |
| **CN** | `context/MPL_16+47+54+44_notes.md`. |
| **N87** | `context/same_cote_15/MPL_15_087-138_notes.md`; contextual note IDs such as T14, L03 or FR02 belong to that file. |
| **N195** | `context/same_cote_15/MPL_15_195-228+18_002-017_notes.md`; its cote 18 locators refer to the reported neighboring witness, not scans supplied here. |
| **RS / RESULTS_STATE** | `context/notes/RESULTS_STATE.md`; identifiers retain the status assigned there. |
| **Hua / Hua15** | Michel Hua's project, modernised reading of cote 15, `context/hua_project/15.modern.tex`, supplied with its own README and attribution to `github.com/Commutator-IO/grothendieck-project`. |
| **Oda69** | Supplied `context/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf`; printed and PDF page numbers are distinguished below. |

The context paths name the supplied input archive, which is intentionally not duplicated inside this deliverable. In current-page citations, L means a line in the frozen per-page TeX fragment, not a reconstructed original manuscript line; line references within N87/N195 retain those returns' own convention. The dots in short quotations indicate excerpts in these research notes; no such editorial abbreviation substitutes for text in the diplomatic transcription.

### Hua's section titles and the current scan boundary

Hua's “pages” are his source-page labels, not the current PDF scan numbers. These are the relevant section names behind the abbreviated citations below.

| Hua locator | Section or subsection title | Relation to the current selection |
|---|---|---|
| §I | “Groupe de Galois motivique commutatif. Cas d'un corps de base fini”; subsections “Les foncteurs fibres, et le groupe G” and “La classe de la gerbe, place par place”. | Earlier source pages 1–13; comparisons only, without those scans here. |
| §V, final subsection | “Foncteurs fibres réels et polarisations (pages 116 à 124)”. | Earlier real-fibre and cocharacter comparison; also discussed in N87. |
| §VII | “Groupes de Galois motiviques commutatifs (pages 134 à 138)”. | Earlier Artin–Tate quotient; no new arithmetic exact sequence on the current leaves. |
| §§IX–X | “Corps de classes commutatif et motifs métabéliens”; “« Unités », et un plan (pages 167 et 169)”. | Current 170 corresponds to the agenda labelled page 169; the surrounding class-field pages are absent. |
| §XI | “Cohomologie absolue des motifs de Tate Z(n)”; subsection “La dualité d'Artin–Verdier recalculée, et le groupe de Brauer”. | Current 179 is the cancelled/live Brauer-related leaf; 180 is a title. Other calculations summarized by Hua are absent. |
| §XII | “La distribution des Frobenius dans les groupes de Galois motiviques (pages 181 à 186)”. | Current title 182 and mathematical leaves 183,185,187. |
| §XIII | “Foncteurs fibres motiviques et groupe fondamental motivique”; subsection “En caractéristique p : les points canoniques (pages 190 et 192)”. | Current covers 189–190 and mathematical leaves 191,193. Later subsections extend into N195's selection. |
| §XIV | “Le groupe fondamental motivique discret”; subsections “Deux places archimédiennes” and “Foncteur fibre et structure de Hodge”. | Later comparison programme, reported in N195, not a new current witness. |

## Answers to the planning questions

| Question | Finding from the selected scans and supplied context | Detailed notes |
|---|---|---|
| Linear/non-linear comparison | The four pairs are distinct reconstruction problems with distinct hypotheses; the table below records the exact limits of the analogy. | BG02, BG04–BG05; F03–F10; PD10–PD12. |
| Category built from cote 16's Lefschetzien rings? | Not constructed here: 183 assumes a category. Cotes 12–13 are not supplied in full, so their construction remains a source question. | LC01. |
| Cote 16's sl₂ inside the motivic group, with its grading the weight cocharacter? | The prescribed action fails the already recorded projective-line/unit test; the weight grading differs from the Cartan cocharacter by a scalar factor in that example. No new embedding appears here. | LC02–LC03, credited to N87 L03–L05/Proof B. |
| Manuscript A–D versus printed letters? | Secure operational matches A→printed A and C→printed B; B→printed D and D→printed C are supported but lack standalone definitions in the supplied cote 16 witness. | LC04 and its qualified dictionary. |
| Cote 14 continuation of 16/047's singular-hypersurface programme? | Not decided: 16/047 explicitly asks for it, current 170 gives a related positivity agenda, and the full cote 14 witness is absent. | A02, LC05. |
| His arithmetic exact sequence over Q? | Current 183 gives a restricted Tate kernel. N87 reports the component and Artin–Tate quotients on 15/135,137; identifying the full arithmetic quotient and geometric kernel needs additional comparison and descent. | G01–G03, with a separately sourced modern Nori sequence. |
| A written period conjecture? | None on the eighteen current scans. N195 reports a live strong conjecture on 18/011, a cancelled formulation on 18/012, and a live elliptic dimension prediction on 18/013. | PG01–PG02; neighboring raw scans were not supplied for this task. |
| Which parts are theorems for Nori/Ayoub, and which remain additional claims? | The characteristic-zero Betti group comparison and the rational pure/André comparison have precise theorem statements. They do not establish the manuscript's algebraic-cycle identifications, effectivity criterion, or integral characteristic-p fibre structures. | LC07–LC10; PD04–PD08. |

## Linear statement, non-linear statement

These columns specify different problems, not asserted equivalences. External theorem keys refer to the primary bibliography; examples and descent calculations already in the supplied returns remain credited there.

| Pair | Linear statement | Non-linear statement | Current contribution and limit |
|---|---|---|---|
| **Tate and anabelian Hom** | For abelian varieties A,B over a finite field k and ℓ different from its characteristic, \(\operatorname{Hom}_k(A,B)\otimes_{\mathbf Z}\mathbf Z_\ell\to\operatorname{Hom}_{G_k}(T_\ell A,T_\ell B)\) is an isomorphism [Tate66, p.134]. | Over a sub-p-adic field, dominant maps between hyperbolic curves correspond to open continuous arithmetic fundamental-group maps over the fixed absolute Galois group, modulo geometric inner conjugation [Mochizuki99, Theorem A]. | 185–187 invoke Tate conjectures for **effectivity**; 193 distinguishes ℓ-adic monodromy and p-adic coefficient action. Neither states a Hom theorem; compare N87 FR21/§3 (15/088,090), N195 B01 (15/213,215,227), RS MPL_15_195-228+18_002-017 B01. |
| **Semisimplicity and trivial centres** | A semisimple representation category splits subobjects; N87's example Rep(G_m) still has tensor group with nontrivial centre. | Injectivity of \(P\to\operatorname{Aut}(P)\), \(g\mapsto\operatorname{Ad}_g\), is the separate requirement Z(P)=1. | The Lie statements on 192/194 belong to reused editorial sheets. Compare N87 L13–L14/§3 (15/090,135), N195 B02/R01; RS WG2 §2.3 #7 and MPL_15_195-228+18_002-017 R01. |
| **Polarizations and real structures** | Polarization adds positivity; 185 requires equality with the transported polarization on a fixed real twist. | In \(1\to\Pi\to E\to\operatorname{Gal}(\mathbf C/\mathbf R)\to1\), a lift s gives τ=Ad_s and c=s² with τ²=Ad_c; a section requires \(a\tau(a)c=1\), as calculated in N87 T27. | 183–185 use H¹ and impose compatibility at fixed twist class, while finiteness remains “? à vérifier”. Compare N87 T01–T09/T27 (15/117–123), N195 B03 (15/203,215,217); RS MPL_15_195-228+18_002-017 B03 and WG2 §2.3 #12. |
| **Weights and cyclotomic normalizers** | The non-Tate condition is \(\operatorname{Hom}_{G_k}(\mathbf Z_\ell(1),T_\ell A)=0\) for all abelian varieties A/k; number fields satisfy it [Stix12, Definition 26]. | For a characteristic-zero hyperbolic curve under that condition, a nontrivial closed geometric pro-ℓ subgroup lies in cusp inertia exactly when it is Z_ℓ and has a normalizing subgroup with **open arithmetic image and cyclotomic conjugation action** [Stix12, Definition 29/Theorem 30]. | The Tate kernel on 183 and effective weight-zero normalization on 191 provide neither normalizer nor character premise. Compare N87 FR22 (15/090,100,102), N195 B04–B05 (15/195,205,227); RS LM6 A.22, LM6 A.50 and MPL_15_195-228+18_002-017 B04. |

## 1. Agenda on scan 170

### A01 — Odd-weight motives and Weil-type abelian varieties remain an agenda

**Kind:** conjecture. **Witness:** 15/170 item0, “VA”, “motifs purs de poids impair”; **context/register:** CT44/002 Th.2–4 and44/008–009, CN44:8:2–6, Hua §X (source page169); RS WG2 §2.3 #12 and WG H9.

The agenda asks for abelian varieties associated with odd-weight pure motives under Hodge–Riemann conditions, without constructing them here. It restates more broadly the earlier J^i/P^i programme, where representability, cohomological realization and positivity have distinct unproved steps. The entry supplies no way to bypass those qualifications or extend the cycle construction to every odd-weight motive.

### A02 — Divisors, blow-ups and pencils are proposed routes to positivity

**Kind:** self-flagged. **Witness:** 15/170 lower addition, “diviseurs”, doubtful “éclatement” and “pinceaux”, ending “??”; **context/register:** CT44/004,008–009, CN44:8:6–7 and44:9:1–2; RS WG H9 and WG2 §2.3 #12.

This links the agenda with the earlier reduction of positivity to a divisor correspondence and a generic member of a pencil, although the exact blow-up/pencil wording is weakly legible. It adds an agenda locator, not the missing positivity proof or correction terms for singular fibres. Hua §X paraphrases the last line as a reduction “par récurrence”; that paraphrase cannot replace the uncertain frozen words.

### A03 — Lattice comparison continues into place-dependent torsors

**Kind:** unpursued implication. **Witness:** 15/170 item4, “comparaison des réseaux canoniques”, and item5's inserted “de 4)”; **context/register:** N195 A28–A38 (15/219–225), Hua §§X,XIV; RS claims #964 and MPL_18_018-062 P10 (register excerpt only).

The table distinguishes transcendental lattices at different places, a transcendental lattice against a Hodge lattice, and l-adic comparisons. The insertion ties the old-notes reference specifically to this comparison problem; the later package adds questions and retractions about the resulting torsors. This supports a programme link without recovering a place from a bare lattice or settling the later Hodge-enriched reconstruction question.

### A04 — Class fields, L-functions and the Riemann hypothesis are headings

**Kind:** reading question. **Witness:** 15/170 items2,6,8,9, “Relations avec le corps de classes”, “équation fonctionnelle”, “Topologie à mettre sur Z”, “Hyp. de Riemann ??”; **context/register:** Hua §§IX–X (source pages156–169), RS MPL_60_036-070 §2/LF09 and WG2 §Summary #2.

These entries state intended connections but give no class-field construction, functional equation, topology or proof of a Riemann hypothesis on the selected leaf. Hua's neighboring CM/class-field account concerns pages absent here; the cote60 register entries are leads to other work, not supplied proofs. The agenda's “OK” marks record a manuscript status, not a proof certificate.

### A05 — The weakest agenda phrase cannot support a precise extension

**Kind:** reading question. **Witness:** 15/170 item1, doubtful “groupes définis par des présentiques|présentations”; **context/register:** Hua §X (source page169), N87 T19–T22 (15/135–137); RS MPL_15_087-138 §124 and WG2 §2.4 #3.

Hua paraphrases this as an extension defined by motivic points, which fits the programme but does not establish the difficult noun from the ink. Comparing the marked word with repeated point-motivique vocabulary is a future reading task. The exact arithmetic sequence must be sourced from a clearer witness, not reconstructed from this uncertain line.

## 2. The cancelled divisor calculation on scan 179

### PD15 — The cancelled Leray argument and the live boundary map must remain separate

**Kind:** unproved claim. **Witness:** cote 15, scan 179, upper crossed block and live (1.1.). **Words:** “est un groupe de torsion pour p>0”; “bijectif modulo torsion”. **Context search:** `R_X|Div|torsion|Brauer|Kummer` → CT16/021, (8.3)–(8.7); CN R8; Hua §XI, subsection “La dualité d’Artin–Verdier recalculée, et le groupe de Brauer”, paragraph on pages 178 and 175. **Relation:** adds a generic-point/divisor route beside the contextual Kummer/Brauer calculation; supports Hua’s identification of a cancelled supporting argument, not its restoration as live proof. **RESULTS_STATE:** WG2 §1.1 #3 and WG2 §Summary #2 [unchecked plans]; no dedicated divisor-cohomology result in the ledger.

The live connecting map \(H^i(X,\underline{\operatorname{Div}}_X)\to H^{i+1}(X,G_{mX})\) is asserted bijective modulo torsion for \(i\ge1\), while the displayed Leray justification for torsion of \(H^p(X,R_X^*)\) is inside a cancelled block. A proof of the live assertion can be organized by showing that the adjacent rational-function cohomology groups are torsion under the actual hypotheses and then applying the long exact sequence; the cancellation neither provides a live proof nor declares the assertion false. CT16/021 instead makes finiteness and divisibility hypotheses explicit in a Kummer-limit comparison, so its calculation cannot simply replace the missing justification here.

### PD16 — Hua completes the unfinished factoriality sentence and renumbers its formula

**Kind:** reading question. **Witness:** cote 15, scan 179, formula number and last line. **Words:** “(1.1.)”; “un isomorphisme de faisceaux étales :”. **Context search:** `factoriels|Div|5.1|1.1` → Hua §XI, subsection “La dualité d’Artin–Verdier recalculée, et le groupe de Brauer”, pages 178 and 175; CT16/019–023, reused Brauer typescript. **Relation:** differs in numbering and supplies mathematical continuation absent from the current leaf. **RESULTS_STATE:** WG2 §1.1 #3 and WG2 §Summary #2 [unchecked plans].

Hua calls the displayed divisor sequence (5.1), whereas the frozen current page has (1.1.), and its factoriality sentence stops at a colon before any isomorphism is written. Hua then supplies the codimension-one direct-sum description and its consequences while identifying further Brauer propositions on the other page, which is not among the selected scans. Those are useful source-identification leads, but neither their formula numbering nor their completion belongs in the frozen transcription.

## 3. Frobenius, real forms, polarizations and effectivity

### F01 — Restriction to even degrees is qualified

**Kind:** withdrawn in the same text. **Witness:** cote 15/183, opening paragraph, “certaines” inserted over deleted “la plupart des”; **context/register:** Hua, modernised reading of cote 15, §XII (source pages 181–186), and MPL_15_087-138_notes.md T01–T02 (15/117–119), bearing on RS MPL_15_087-138 L01 and WG2 §2.4 #3.

The current page narrows the scope of replacing the category by its even-degree part to certain questions of Frobenius distribution. Hua's unqualified summary that one passes to the even part does not retain this revision, while the earlier package reports a real-fibre corollary with its own compatibility conditions. This adds an explicit limitation, not a proof that every distribution question survives the replacement.

### F02 — The finite-order restriction is weaker than a cocharacter

**Kind:** own idea. **Witness:** 15/185, restriction to μ₂, and 15/187, “rayons définis par les v(s′)”; **context/register:** MPL_15_087-138_notes.md T08, T13–T14 (15/119–123), Hua §XII, RS MPL_15_087-138 L01 and WG2 §2.4 #3. **Confidence:** high because restriction to μ₂ records a cocharacter exponent only modulo two; tentative for its application to the compressed manuscript.

For the one-dimensional torus, the cocharacters t↦t and t↦t⁻¹ have the same restriction to μ₂ but opposite rays in the cocharacter space. Thus the order-two restriction alone cannot define the signed rays needed by an effectivity cone; the full i(s′), or sufficient additional data specifying a cocharacter lift, must be retained in any precise formulation. This adds an information-loss test to the earlier finite-index-versus-parity caveat T13 and distinguishes the manuscript's displayed v(s′) from the cocharacters used in T14, without claiming that both test cocharacters satisfy the manuscript's preferred-type conditions.

### F03 — A real form is chosen before distribution is compared

**Kind:** unproved claim. **Witness:** 15/183, “choisissons un pt R-motivique” and “démultiplier”; **context/register:** N87 T01–T02 (15/117–119), T09 (15/121–123), Hua §XII; RS WG2 §2.4 #3 and MPL_15_195-228+18_002-017 B03.

The construction assumes a real motivic point, replaces a closed point by a pair containing a preferred-type map, and obtains a class in H¹ of the kernel of the Tate character restricted to the neutral component, together with a homomorphism into a twisted real group. This adds a family over closed points of a finite-type base to the earlier real-fibre and preferred-polarization discussion; it does not prove existence of the real point or uniqueness of the preferred map. The even-degree qualification and the earlier real-fibre compatibility hypotheses must accompany the construction.

### F04 — Conjugacy does not give a preferred representative

**Kind:** unpursued implication. **Witness:** 15/183, “déterminé en fait mod”, with “automorphisme intérieur” deleted and “conjugaison” inserted; **context/register:** Hua §XII (source page182), N87 T07,T09 (15/119–123); RS MPL_15_195-228+18_002-017 B03 and WG2 §2.4 #3.

The final wording determines u(s′) up to conjugation by a real point of the displayed kernel, subject to compatibility with ε and the second structural map. This restates the torsorial ambiguity in a form useful for distribution questions: on each fixed twisted real form, conjugacy-invariant functions can be evaluated without choosing representatives. It gives no canonical trivialization of the twisting class and no identification of all twisted groups with one real form.

### F05 — The order-two restriction must match the transported polarization

**Kind:** unproved claim. **Witness:** 15/185, “doivent être identiques” and “condition non tautologique”; **context/register:** N87 T07–T09 (15/119–123), N195 B03 (15/203,215,217), Hua §XII; RS MPL_15_195-228+18_002-017 B03 and claims #964.

For a fixed twisting class, the restrictions to μ₂ must define the same transported polarization, so admissible u(s′) satisfy an extra compatibility condition. This adds a fibrewise test to the earlier polarization correspondence and resembles the later Riemann–Hodge warning for torsors arising from places. It does not establish claims #964, which concerns archimedean places and integral comparison torsors, rather than this family of closed-point real forms.

### F06 — Finiteness is explicitly unfinished

**Kind:** self-flagged. **Witness:** 15/185, “fini”, “[si G est commutatif en tous cas !]”, “? à vérifier”, and deleted “classes de”; **context/register:** N87 T09,T13 (15/121–123), Hua §XII; RS WG2 §2.4 #3 and MPL_15_195-228+18_002-017 B03.

The sheet doubts finiteness of the polarizations described by homomorphisms from the later, unsubscripted μ_C and retains a commutative qualification, whereas the principal maps use μ₂. This adds unresolved questions about the domain and about sets versus orbits to the earlier preferred-polarization packet; Hua's shorter account omits the bracket and does not settle it. The deletion of “classes de” makes the distinction between the actual set and its conjugacy classes material; it does not license silently substituting the latter.

### F07 — Two elementary tests separate set and orbit finiteness

**Kind:** own idea. **Witness:** 15/185, finiteness bracket, “fini”; **context/register:** N87 T08–T09,T13 (15/119–123), Hua §XII; RS WG2 §2.4 #3. **Confidence:** high because Hom(μ₂,T)=T[2] and the displayed matrices are conjugate to diag(1,−1), limited for identifying the manuscript's admissible polarizations.

For algebraic-group homomorphisms over the complex numbers and a torus T of rank r, Hom(μ₂,T) has 2ʳ elements, so the commutative order-two version has a direct finite test. Conversely, the distinct matrices \(A_t=\begin{pmatrix}1&-2t\\0&-1\end{pmatrix}\), \(t\in\mathbf C\), are conjugate involutions in \(\operatorname{GL}_2(\mathbf C)\), giving infinitely many actual homomorphisms from μ₂ in one conjugacy class. These calculations neither assert that every map is a polarization nor interpret the unsubscripted μ_C; they show why those qualifications matter before proving the page's assertion.

### F08 — Recovery of effectivity is an additional Tate-dependent claim

**Kind:** unproved claim. **Witness:** 15/185–187, “conjectures de Tate” with doubtful “magnifiées”, “retrouver la structure d'effectivité”, “engendré”; **context/register:** N87 T14 (15/121–123), Hua §XII; RS MPL_15_087-138 L01 and MPL_15_195-228+18_002-017 B01/M08.

The text proposes recovering effectivity from the u(s′), describes a cone through rays associated to v(s′), and relates this to integrality of Frobenius eigenvalues. This extends the earlier single-cocharacter assertion to a family of fibres and exceeds a bare morphism-fullness statement. A proof must identify the cone's ambient space, retain enough cocharacter information, and specify the representations covered by the integrality criterion.

### F09 — Integrality in every representation forces algebraic units

**Kind:** own idea. **Witness:** 15/187, “dans tte représentation”, “entiers algébriques”; **context/register:** N87 FR02 (15/090), T14 (15/121–123), Hua §XII and §I “Les foncteurs fibres, et le groupe G”; RS MPL_15_087-138 §3 and MPL_15_195-228+18_002-017 B01/M08. **Confidence:** high for the conditional implication because contragredient eigenvalues are reciprocal; the intended manuscript quantifier remains open.

If the phrase ranges over a representation category closed under duals, an eigenvalue λ and its inverse must both be algebraic integers, so λ is an algebraic unit. If a character takes the value \(q^n\), with \(q\in\mathbf Z_{>1}\) and \(n\in\mathbf Z\setminus\{0\}\), integrality cannot hold for that character and its dual. Under that additional Tate-value hypothesis, the unrestricted dual-closed quantifier is impossible, so the intended range of representations needs clarification. N87 FR02 already gives the eigenvalue-2/dual-1/2 example, and Hua §I already separates the effective monoid from its group completion; the addition here is their application to the actual “dans tte représentation” wording on 15/187.

### F10 — The dual cone gives a concrete torus test

**Kind:** own idea. **Witness:** 15/183, i(s′), and 15/187, the cone “engendré”; **context/register:** N87 T10–T14 (15/121–123), Hua “Foncteurs fibres réels et polarisations (pages116 à124)” and §XII; RS WG2 §2.4 #3. **Confidence:** medium, since the lattice construction is exact but its identification with motivic effectivity is unproved here.

For a fixed complex torus T, let \(M=X^*(T)\), \(N=\operatorname{Hom}(M,\mathbf Z)\), \(\nu_s\in N\), and \(C=\operatorname{cone}_{\mathbf R_{\ge0}}\{\nu_s\}\); then the candidate monoid \(P=M\cap C^\vee\) consists exactly of characters satisfying \(\langle\chi,\nu_s\rangle\ge0\) for all s, without a finite-generation assertion. Placing the manuscript's maps, with their different source groups and twisted targets, in this common torus and lattice is an additional modelling assumption. This separates cocharacters from representation weights and supplies a test for the proposed effectivity criterion. The earlier denominator warning T10–T11 must be resolved before treating the \(\nu_s\) as actual maps from \(\mathbf G_m\), and restriction to μ₂ loses the inequalities.

### F11 — Distribution has constraints here, but no measure

**Kind:** unpursued implication. **Witness:** 15/182 title and 15/185–187, “distribution”, “condition non tautologique”, “condition arithmétique”; **context/register:** Hua §XII's expressly editorial Sato–Tate comparison, N87 T09,T14 (15/121–123); RS MPL_15_195-228+18_002-017 B03 and WG2 §2.4 #3.

These leaves impose twisting, polarization and integrality constraints, but define no probability measure, ordering of closed points, density or equidistribution assertion. Hua's Sato–Tate comparison is a research direction credited to his project, not a theorem written here. A precise next step would stratify pairs s′ by twisting class and specify the conjugacy-invariant functions to be averaged.

### F12 — Weakly read symbols remain reading questions

**Kind:** reading question. **Witness:** 15/183, initial adjective, doubled-loop superscript and second compatibility symbol; **context/register:** Hua §XII (source page182), N87 T01,T08 (15/117–123); RS MPL_15_087-138 L01 and WG2 §2.4 #3.

The frozen readings are uncertain “géomologiques|géométriques”, G^{00}, and J_R|j_R, whereas Hua writes géométriques, G^{0u} with an explicit doubt, and compatibility with ε and i. His footnote also reports different letters for the pair and then changes them for exposition. These comparisons are questions for a future visual review, not grounds for changing a frozen reading.

### HG03 — The even-degree restriction limits an apparent conflict with Hua's real obstruction

**Kind:** unpursued implication. **Witness:** 15/183, opening; 15/185, polarization maps. **Quote:** “supposons que les degrés … soient pairs”; correction to “certaines” questions. **Context relation:** qualifies the comparison with Hua §I “Les foncteurs fibres, et le groupe G” and “La classe de la gerbe, place par place” (his pages 4,6–10), and N87 T01–T08 (15/117–123); RS's **Orientation for this package** attributes the real-obstruction/quaternion bridge to Hua, and relevant indexed leads are **MPL_15_087-138 §3** and **WG2 §2.4 #3**.

Hua connects the absence of a real fibre functor for the full finite-field category with a $\mu_2$ obstruction and a quaternion class, crediting that connection to his project. Current 183 has already restricted to even degrees before choosing a real motivic point, so the two statements cannot be compared without retaining that categorical restriction. The deletion of “la plupart des” in favor of “certaines” also makes the permitted reduction narrower than Hua §XII's general-sounding passage to the even part. These pages provide a specific scope qualification, not a proof that all remaining real obstructions vanish.

## 4. Characteristic-p fibre objects and comparison questions

### PD01 — The fundamental object is not made neutral by listing realizations

**Kind:** unproved claim. **Witness:** cote 15, scan 191, opening and items (i)–(iii). **Words:** “il n'y a pas en général de sections”; “pro-torseur fondamental”. **Context search:** `pro-torseur|gerbe|foncteur|torseur` → Hua, modernised reading of cote 15, §XIII opening and “En caractéristique p : les points canoniques”; N195 A13–A14, 15/207 and 209; N87 T15–T18, 15/123–137. **Relation:** adds an explicit non-neutrality warning to the same-cote gerbe discussion. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked plan]; MPL_15_087-138 §124 [first-pass lead].

Scan 191 gives local realizations while expressly denying general sections of its \(T_\alpha\), so the existence of each listed realization must not be restated as a global fibre functor over the initial coefficient ring. The same-cote leads distinguish the category of fibre functors from individual torsors of tensor isomorphisms; the present wording leaves the precise groupoid or gerbe model implicit. Hua’s introductory description as an “ensemble” and “un torseur” should therefore be read as an explanatory model requiring this distinction, rather than a definition supplied on the sheet.

### PD02 — Henselian origins remain proposed lifts

**Kind:** self-flagged. **Witness:** cote 15, scan 191, items (i) and (ii), side labels. **Words:** “provenant sans doute”; “hensélisé”; “hensélisé strict.” **Context search:** `hensél|Witt|provenant|caractéristique` → Hua §XIII, “En caractéristique p”; N195 A01, 15/195:L9–19. **Relation:** adds proposed descent to smaller coefficient rings before the neighboring mixed-characteristic comparison. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 §133 [first-pass lead].

The two “sans doute” phrases qualify origins in henselian rings, not merely the existence of the completed or Witt-valued objects already displayed. Hua rewrites the ℓ-adic henselian source in standard notation and omits the corresponding tentative p-adic origin, while the frozen tilde notation, the Z/Q alternative in (i), and a small subscript in (ii) remain uncertain. A proof would have to construct descent of the realization together with its tensor and integral structure, and N195’s later comparison over \(W(k)\) does not supply that descent.

### PD03 — Reduction to de Rham–Hodge is a question with a derived qualification

**Kind:** self-flagged. **Witness:** cote 15, scan 191, item (iii), diagonal arrow, left margin. **Words:** “?”; “réduit”; “travailler dans la catégorie dérivée”; “structure filtrée”. **Context search:** `Hodge|filtr|dérivée|réduit` → CT54/003–007; CN D01–D05; N195 A02, 15/195:L21–23, and P01, 18/005:L2–16. **Relation:** adds a derived and filtered requirement to the abelian degree-one context. **RESULTS_STATE:** MPL_15_195-228+18_002-017 P01 [first-pass lead]; WG2 §2.4 #3 [unchecked plan].

The arrow from the Witt-valued object to the \(k\)-valued object is labelled “DeRham-Hodge”, but its lower item carries a question mark and the side note calls for a derived category and a filtration. CT54’s Hodge exact sequence and Oda’s precise comparison in PD04 supply a restricted example, not a proof of this general reduction. The deletion of “sans doute” in the margin strengthens the instruction to use a derived category without itself constructing the required derived realization.

### PD04 — What Oda verifies, with the filtration retained

**Kind:** unpursued implication. **Witness:** cote 15, scans 191 and 193, p-adic margins and the “DeRham-Hodge” arrow. **Words:** “opérations F et V”; “FV=p”. **Context search:** `Frobenius|Verschiebung|Dieudonné|p^A|Hodge` → CT54/005,007; CN D03–D05; N195 P04, 18/005:L18–26 and 18/011:L5–7. **Relation:** supports the restricted degree-one comparison already identified by CN D05, while adding a general motivic setting whose extension is unproved. **RESULTS_STATE:** MPL_15_195-228+18_002-017 P01 and S15: [first-pass leads]; WG2 §2.4 #3 [unchecked plan].

Oda’s Definition 3.1 (printed p. 80, PDF p. 19) specifies \(W(k)[F,V]\) with \(FV=VF=p\), \(F\lambda=\lambda^\sigma F\), and \(\lambda V=V\lambda^\sigma\), for \(k\) perfect of characteristic \(p\). For an abelian scheme \(A\) over \(k\), Corollary 5.11 (printed p. 131, PDF p. 70) canonically identifies \(M(A[p])\) with \(H^1_{\mathrm{dR}}(A)\) as left modules and carries \(VM(A[p])\) to \(H^0(A,\Omega^1_A)\), matching the stated exact sequence with the Hodge sequence. This directly checks CN D05’s restricted comparison, but it does not construct the manuscript’s pro-system of fibre objects for arbitrary motives, its mixed-characteristic comparison, or its integral tensor essential image.

### PD05 — A tensor test for a uniform FV=p rule

**Kind:** own idea. **Witness:** cote 15, scan 193, upper side addition; scan 191, “Structure supplémentaire”. **Words:** “FV=p”. **Context search:** `F,V|Dieudonné|cristall|tensor` → Oda, Definition 3.1; N195 A16, 15/211:L3–15,33–36, and P03–P04, 18/005. **Relation:** adds an elementary scope test to the existing warning that the degree-one theorem does not classify all motives. **RESULTS_STATE:** MPL_15_195-228+18_002-017 P01 and S15: [first-pass leads]; WG2 §2.4 #3 [unchecked plan]. **Confidence:** high for the calculation; medium for its relevance to the manuscript’s unstated intended category.

Over \(W(\mathbf F_p)=\mathbf Z_p\), the rank-one module with \(F=p\) and \(V=1\) satisfies Oda’s relations, but ordinary tensoring of these two operators gives \(FV=p^2\) on its tensor square. If the tensor-square Frobenius remains \(p^2\), forcing a relation \(FV=p\) requires \(V=p^{-1}\), which is not integral. Thus interpreting the marginal relation as a tensor-compatible integral rule on every motivic object needs an explicit degree restriction, weight-dependent normalization, or modified target category; this tests a possible reading of the marginal relation, whose full intended scope is unstated.

### PD06 — Lang explains a conditional uniqueness claim, not the missing hypotheses

**Kind:** self-flagged. **Witness:** cote 15, scan 191, lower paragraph. **Words:** “sans doute uniques à isom près”; “th. de Lang”; “k fini”. **Context search:** `Lang|uniques|torseur|hensél` → Hua §XIII, “En caractéristique p”, footnote on Lang and Hensel; N195 A13–A14, 15/207–209. **Relation:** restates Hua’s proposed sufficient hypotheses and independently checks the finite-field theorem against Lang’s primary paper. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 §133 [first-pass lead].

Lang’s theorem gives rational points on homogeneous spaces of connected algebraic groups over finite fields, hence triviality of the corresponding torsors; the primary statement is Lang (1956), Theorem 2, pp. 557–558. For a smooth finite-type group over a henselian local ring with connected special fibre and finite residue field, applying Lang to the special-fibre torsor and lifting its point gives the expected triviality (Stacks Project, Tags 07M7 and 04GE, Lemma 10.153.3). Scan 191 does not establish those smoothness, connectedness, or representability hypotheses for its integral tensor-isomorphism objects, and the “sans doute” must therefore remain a real qualification.

### PD07 — The perfect-field dimension-one extension is separately qualified

**Kind:** self-flagged. **Witness:** cote 15, scan 191, lower paragraph after the Lang parenthesis. **Words:** “plus gén.”; “k parfait de dim ch 1 (?)” (ch doubtful). **Context search:** `Lang|parfait|dim|Manin` → Hua §XIII, “En caractéristique p”; Oda §3 and Corollary 5.11; N195 P04, 18/005. **Relation:** adds a qualification omitted from Hua’s short summary; no supplied source proves this integral claim for all such fields. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 §133 [first-pass lead].

The inserted extension beyond finite \(k\) carries its own question mark and an uncertain abbreviation, so it should not be bundled into the already named Lang theorem. Reading “ch” as cohomological suggests a field-theoretic torsor vanishing question, but that interpretation neither settles the ink nor supplies the needed integral group-scheme hypotheses. Oda’s perfect-field hypothesis concerns his Dieudonné comparison and does not by itself imply uniqueness of the manuscript’s fibre functors.

### PD08 — A limit with one isomorphism class is a new expectation

**Kind:** conjecture. **Witness:** cote 15, scan 191, final main paragraph. **Words:** “il est possible”; “n'a qu'un élém. à isom près”. **Context search:** `limite|foncteur|isom|transition` → N195 A28–A31, 15/219:L5–10 and 15/221:L3–19; Hua §XIII, “En caractéristique p”. **Relation:** adds a positive-characteristic limit-uniqueness expectation to the neighboring distinction between finite-subcategory and global comparisons. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 §137 [first-pass lead].

The manuscript allows several isomorphism classes at individual \(T_\alpha(k)\) while suggesting that \(T_\infty(k)=\varprojlim T_\alpha(k)\) might have just the de Rham–Hodge class. The later same-cote notes record a separate countability and transition-surjectivity argument for comparisons of places, so that lead does not prove the present assertion. A precise investigation must distinguish inverse limits of groupoids from inverse limits of their isomorphism-class sets and specify which finite-stage objects admit compatible extensions.

### PD09 — Inspect the isomorphism tower before asserting a global comparison

**Kind:** own idea. **Witness:** cote 15, scan 191, displayed inverse limit. **Words:** “il est possible”. **Context search:** `limite|isom|surjectifs` → N195 A28–A31, 15/219–221; N87 R14, reused 15/138. **Relation:** adds a proposed test; the reused Lusin-space inverse-limit argument concerns a different category. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 §137 [first-pass lead]. **Confidence:** high for the conditional test, because it is the definition of a compatible isomorphism family.

For two proposed systems \(\omega,\eta\), form \(I_\alpha=\operatorname{Isom}^{\otimes}(\omega_\alpha,\eta_\alpha)\) and study the transition maps before passing to \(\varprojlim I_\alpha\). Nonemptiness of every \(I_\alpha(k)\) alone does not exhibit compatible isomorphisms, whereas a countable cofinal sequence with surjective maps allows successive choices. This would isolate exactly the compatibility obligation behind the present expectation and the later 15/219–221 sketch without asserting that its hypotheses hold here.

### PD10 — Nonunique isomorphism is explicit, and differs from Hua

**Kind:** reading question. **Witness:** cote 15, scan 193, first paragraph and notation (i). **Words:** “à isom non unique près”; “non uniq.”. **Context search:** `unique|pi_1|point géométrique` → Hua §XIII, “En caractéristique p”, paragraph beginning “Page 192”; N195 A03 and A27, 15/197,201,217. **Relation:** contradicts the word “unique” in Hua’s modernised summary, while supporting its fundamental-group action. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 B01 [first-pass lead].

Hua says the ℓ-adic realizations are independent “à isomorphisme unique près”, but the current frozen text twice retains nonuniqueness and explicitly associates it with \(\pi_1(X)\). This difference matters for a comparison with pointed or unpointed reconstruction, where path choices lead to inner-conjugacy ambiguity. It does not contradict scan 191’s proposed uniqueness of the isomorphism class: uniqueness of a class and uniqueness of an isomorphism are distinct statements.

### PD11 — Coefficient-field conjugacy and fundamental-group transport are different

**Kind:** unproved claim. **Witness:** cote 15, scan 193, main paragraph and lateral addition. **Words:** “\(\pi_1(X)\) n'opère pas”; “autom de k sur k(x)”; “1/2 linéaire”. **Context search:** `semiliné|autom|descente|pi_1` → N195 A03, 15/197:L2 and 15/201:L16; Hua §XIII, “En caractéristique p”, final paragraph. **Relation:** supplies an earlier explicit version of the distinction in N195; supports Hua’s basic comparison, with the qualification below. **RESULTS_STATE:** MPL_15_195-228+18_002-017 B01 and P01 [first-pass leads]; WG2 §2.4 #3 [unchecked plan].

The manuscript separates automorphisms fixing \(k(x)\), which act semilinearly on one fibre, from an automorphism not \(k(x)\)-linear, which generally changes the fibre to a conjugate, non-isomorphic one. Hua’s summary compresses those clauses and can be read as assigning both effects to automorphisms “au-dessus de k(x)”; retaining the distinction makes its claim precise. The sheet separately asserts that \(\pi_1(X)\) “n'opère pas”; comparison with the semilinear action requires specifying the coefficient ring and the relation between \(\operatorname{Aut}(k/k(x))\) and \(\pi_1(X)\), rather than inferring an absolute absence of Galois action.

### PD12 — Different p-adic points need not have the same fibre

**Kind:** self-flagged. **Witness:** cote 15, scan 193, second paragraph. **Words:** “il ne semble pas”; “partie continue”. **Context search:** `isom|points|partie continue|Witt` → N195 A01,A03,A05, 15/195–199; Hua §XIII, “En caractéristique p”. **Relation:** adds the explicit expectation of non-isomorphism for varying perfect-field-valued points before the mixed-characteristic and archimedean discussions. **RESULTS_STATE:** MPL_15_195-228+18_002-017 P01 [first-pass lead]; claims #964 [open, only a comparison of reconstruction problems].

The text doubts that the p-adic objects attached to different \(k\)-valued points are isomorphic and attributes the difficulty to a “partie continue” of a preceding cohomology group whose degree is doubtful. The ensuing assertion about conjugacy when the points lie over one \(x\) and \(k\) is algebraically closed is not a proof that fibres at arbitrary distinct points are isomorphic. This supplies a positive-characteristic counterpart to the place-reconstruction problem in claims #964, not an answer to its archimedean injectivity or essential-image questions.

### PD13 — Keep the obstruction degree and comparison degree distinct

**Kind:** reading question. **Witness:** cote 15, scan 191, \(H^{2|1}(\mathbf Q,G)\); scan 193, \(H^{1|2}\) in the “partie continue” sentence. **Words:** “obstructions non triviales” (both words doubtful). **Context search:** `H^2|H^1|gerbe|obstruction` → N87 T15–T18, 15/123–137; N195 A04, 15/197:L4–6; Hua §XIII, “En caractéristique p”, reference to his pages 6–10. **Relation:** restates the gerbe-versus-isomorphism-torsor issue, with two current exponent doubts. **RESULTS_STATE:** MPL_15_087-138 §124 [first-pass lead]; WG2 §2.4 #3 [unchecked plan].

Hua chooses \(H^2(\mathbf Q,G)\) and identifies it with a class from his pages 6–10, while the frozen scan 191 retains \(2|1\) and scan 193 retains a separate \(1|2\) alternative. The contextual distinction between a neutralization obstruction and forms or comparisons after choosing a fibre functor gives reasons to inspect both degrees in a future edition; it does not authorize deciding either by mathematical expectation. The early pages invoked by Hua are outside the supplied manuscript scans, so their identification is his project’s lead, not a newly verified equality.

### PD14 — Hua’s canonical-points heading suppresses visible qualifications

**Kind:** reading question. **Witness:** cote 15, scan 191, opening and item (iii). **Words:** deleted “de façon canonique”; live “?”. **Context search:** `canoniquement|réduction|points canoniques` → Hua §XIII, “En caractéristique p : les points canoniques”; N195 §133, qualifications on 15/195–197. **Relation:** differs from Hua’s unqualified prose, independently of the exponent choices. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §133 [first-pass lead]; WG2 §2.4 #3 [unchecked plan].

Hua’s prose says the listed objects are available “canoniquement” and presents their reduction as item (iii) without the manuscript question mark. The current page instead cancels the phrase “de façon canonique” and marks the reduced object as uncertain. Its chosen realizations may still admit canonical constructions in a suitably fixed setting, but that is an additional theorem or interpretation, not the live state of this sentence.

## 5. Reconstruction comparisons, arithmetic quotient and periods

### BG02 — Reused Lie semisimplicity does not prove a centre-free motivic statement

**Kind:** reading question. **Witness:** 15/192, final paragraph; 15/194, propositions 2–3. **Quote:** “tout idéal commutatif … est nul”; “V réductive”. **Context relation:** restates the source-separation warning of N195 R01 (15/196,200,206) and preserves the distinction in N87 L13–L14/§3 (15/090,135) and N195 B02; RS **MPL_15_195-228+18_002-017 R01**, **MPL_15_087-138 §3**, **WG2 §2.3 #7**.

These are editorial instructions within the separately headed Lie-algebra text, so their semisimplicity statements cannot be transferred to the motivic writing on other faces. The earlier notes already exhibit the decisive comparison $Z(\mathbf G_m)=\mathbf G_m$ while $\operatorname{Rep}(\mathbf G_m)$ splits into characters. The current packet adds no centre-free assertion for its motivic group, and supplies no update to the centre/centralizer problems in the research register.

### BG04 — The written weight restriction does not identify a cyclotomic normalizer

**Kind:** unpursued implication. **Witness:** 15/183, definition of $G^{00}$; 15/191, lower paragraph. **Quote:** “le noyau de”; “motifs effectifs de poids 0”. **Context relation:** adds a normalization of fibre functors to CT16/021's Tate-sheaf setting and N87 FR22 (15/090,100,102), while remaining distinct from N195 B04–B05 (15/195,205,227); RS **MPL_15_195-228+18_002-017 B04**, **LM7 C.1**, **LM7 C.8**.

Current 183 uses the Tate character to select a kernel, and 191 requires agreement with a fixed fibre functor on the effective weight-zero part. Neither page introduces the geometric procyclic subgroup, its arithmetic normalizer, or its conjugation character from the non-linear comparison. The neighboring weight/normalizer argument therefore remains an external bridge with its own hypotheses, not a theorem extracted from the notation $G^{00}$.

### BG05 — Open arithmetic image still does not supply the character premise

**Kind:** unpursued implication. **Witness:** 15/191 and 15/193, $\ell$-adic and $p$-adic action paragraphs. **Quote:** “$\pi_1(X)$ opère”; “n'opère pas”. **Context relation:** preserves N195 B05 (15/227)'s check on **LM6 A.22** and **LM6 A.50**, and N87's relation-to-open-items paragraph; searches found no normalizer assertion in the current sheets.

Stix's criterion requires both open image in the arithmetic Galois group and cyclotomic action on the candidate subgroup [Stix12, Definition 29/Theorem 30]. The supplied RS summary of **LM6 A.22** remains an open problem, and its truncated **LM6 A.50** entry cannot be used here to fill an unstated character step. Current 193 adds a concrete warning that the relevant actions differ with the realization, but supplies no construction of the subgroup required by A.22 and no solution of **LM7 E.23** or **FLAGGED_149 B9**.

### G01 — The current page specifies a restricted Tate kernel

**Kind:** reading question. **Witness:** 15/170, item 1; 15/183, displayed kernel. **Quote:** “Extension des” (continuation doubtful); “où $G^{00}$ est le noyau de”. **Context relation:** adds a real-twist use of the restricted kernel to N87 T19–T22/T28 (15/135,137); differs from the arithmetic-quotient question in RS **MPL_15_087-138 §2**, **MPL_15_195-228+18_002-017 §2**, and **WG2 §2.4 #3**.

The current text supplies $G^{00}=\ker(\varepsilon:G^0_{\mathbf R}\to\mathbf G_m)$, with the exponent itself doubtful, but no sequence with quotient $\Gamma_{\mathbf Q}$. N87 reports $1\to G^\circ\to G\to G'\to1$ at 15/135 and the Artin–Tate quotient $G\to G'\times\mathbf G_m$ at 15/137, whose kernel is $\ker\varepsilon\cap G^\circ$. Identifying $G'$ with the full proconstant absolute Galois group requires the Artin comparison described in N87 T28, while identifying the kernel with a geometric motivic group also needs a base-change/descent argument; neither is supplied in the current fragment. Hua §VII modernizes this subcategory as the Artin category, so its cleaner formula must not be mistaken for fresh proof on 183.

### G02 — The arithmetic sequence and a chosen global fibre functor are separate issues

**Kind:** unpursued implication. **Witness:** 15/183, choice of real motivic point; 15/191, opening and obstruction paragraph. **Quote:** “choisissons un pt … motivique”; “il n'y a pas en général de sections”. **Context relation:** adds the current non-neutrality warning to N87 T18–T25 (15/135,137), N195 M06 (18/006 versus the arithmetic sequence), and Hua §I “La classe de la gerbe, place par place”; RS **MPL_15_087-138 S15:**, **MPL_15_195-228+18_002-017 S15:**, **WG2 §2.4 #3**.

Any notation for an automorphism group of a fibre functor must distinguish the chosen real realization of 183 from the possibly unneutralized rational object of 191. In particular, neither the neighboring arithmetic quotient nor the modern Nori sequence summarized by N87 T25 supplies a canonical section of the current pro-torsor. The $H^{2\,|\,1}(\mathbf Q,G)$ reading on 191 remains uncertain, and the present note does not turn it into a proved $H^2$ classification.

### G03 — A precise modern exact sequence over Q is available for Nori motives

**Kind:** unpursued implication. **Witness:** current 15/183, restricted kernel, and 15/191, rational torsor. **Quote:** “le noyau de”; “il n'y a pas en général de sections”. **Context relation:** restates the modern comparison in N87 T25 (15/135,137) after an independent source check; the displayed arithmetic sequence is not attested in the current scans; RS **MPL_15_087-138 S15:** and **WG2 §2.4 #3**.

For rational Nori motives, choose $\overline{\mathbf Q}\subset\mathbf C$ and the compatible Betti fibre functors; Kahn's Theorem 5.10 with §10 gives an exact sequence of affine $\mathbf Q$-group schemes
$$
1\longrightarrow G_N(\overline{\mathbf Q})
\longrightarrow G_N(\mathbf Q)
\longrightarrow \underline{\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)}_{\mathbf Q}
\longrightarrow1,
$$
where the right-hand term is the proconstant group scheme and the arrows come from base change and the Artin subcategory [Kahn25]. The proof uses rational Galois descent, without assuming the standard conjectures or semisimplicity. This verifies the modern comparison already recorded in N87 T25, but does not identify the manuscript's unspecified category with Nori motives or provide a canonical splitting.

### PG01 — No period conjecture is stated in these eighteen scans

**Kind:** reading question. **Witness:** 15/170, comparison table; 15/183 and 15/191, fibre-functor discussions. **Quote:** “réseau transcendant et réseau de Hodge”; “foncteurs fibres”. **Context relation:** restates N87 T26's limited negative finding for 15/087–138, but differs from the positive neighboring witness in N195 P15–P26 at cote 18/011–013; RS **MPL_15_087-138 §124**, **MPL_15_195-228+18_002-017 §2**, **WG2 §2.4 #3**.

The present pages compare realizations and propose torsor structures, but contain no equality for the transcendence degree of a period field, no genericity statement for a period point, and no algebraic-independence claim for periods. The word “transcendant” in the lattice comparison on 170 does not state such a conjecture. This is a negative finding for the selected eighteen scans only; it must not erase the positive cote 18 evidence reported by the supplied later-package notes.

### PG02 — The supplied context already reports a written period witness elsewhere

**Kind:** conjecture. **Witness:** current 15/170, item 4, as the local comparison-programme anchor; contextual cote 18/011–013. **Quote:** current “comparaison des réseaux canoniques”; contextual quotations reported in N195: “Conj. de transcendance forte” and “degré de transcendance égal à $\dim G$ (4 ou 2) ?”. **Context relation:** N195 P15, P18 and P22 add a positive answer beyond current 170 and N87 T26; RS **MPL_15_195-228+18_002-017 §2**, **WG2 §2.4 #3**.

For $k\subset\overline{\mathbf Q}$, N195 P15 reports the live strong conjecture $\operatorname{trdeg}_k k(\alpha,\beta)=g+u$ on 18/011, where $g=\dim G$ and $u=\dim U'$, involving both period comparison and a Hodge-splitting comparison. Its P18 separately records a cancelled normalized formulation on 18/012, and P22 reports the live elliptic prediction for curves over $\overline{\mathbf Q}$, of degree 4 in the non-CM case and degree 2 in the CM case on 18/013. These are precise first-pass locators for the planning question, not readings independently checked from cote 18 scans in the present task. The correct conclusion is therefore “no new period statement in this packet; a written witness is already reported in the supplied neighboring context,” with the three textual states kept distinct.

## 6. Lefschetz rings, standard conjectures and modern comparisons

### LC01 — The current page assumes the motivic category

**Kind:** reading question. **Witness:** 15/183, “Soit … une catégorie de motifs”, with “de type fini” inserted. **Context and relation:** adds a category-first witness to N87 L01 (15/135,137); compare CT16/015–018, especially “anneau de correspondances Lefschetzien” on 16/018. **RESULTS_STATE:** WG2 §2.4 #3; MPL_15_087-138 §123; MPL_14_002-044 §107.

The current page starts from a category and does not construct it from cote 16's correspondence rings. The supplied neighboring notes already distinguish the conjectural cycle construction, the associated tensor category and its fibre functor. Neither this page nor the register excerpt for cote 14 decides the construction question for cotes 12–13, whose full witnesses are absent.

### LC02 — The prescribed Lefschetz action is not a tensor-group action

**Kind:** unpursued implication. **Witness:** 15/183, chosen real motivic point and maps u(s′), with no Lefschetz action displayed. **Context and relation:** restates N87 L03 and “Proof B — Projective-line correspondences, sl₂, and the Tate group” (15/135,137), compared with CT16/009–018,048. **RESULTS_STATE:** MPL_15_087-138 L03 and §111; WG2 §2.3 #2; WG2 §2.4 #3.

N87 already records the decisive projective-line test: the prescribed raising operator on \(h(\mathbf P^1)=\mathbf1\oplus\mathbb L\) sends the unit to a nonzero class, while tensor automorphisms fix the unit summand. That supplied calculation rules out this specified action as the action of a subgroup of the tensor-automorphism group; it does not exclude every abstract \(\operatorname{SL}_2\) subgroup from every motivic group. Current 183 adds no embedding or correction of that action, so no new proof or stronger impossibility is claimed.

### LC03 — The weight and Cartan cocharacters remain distinct

**Kind:** reading question. **Witness:** 15/183, compatibility with ε and the doubtful J_R|j_R; 15/185, restriction of i(s′) to μ₂. **Context and relation:** restates N87 L04–L05 and Proof B (15/090,094,135,137), with CT16/009–018,048. **RESULTS_STATE:** MPL_15_087-138 §111 and L03; WG2 §2.4 #3.

The supplied projective-line comparison is \(j(s)=\operatorname{diag}(1,s^2)=s\,\mathrm{id}\,\operatorname{diag}(s^{-1},s)\), which separates the weight grading from the Lefschetz Cartan cocharacter by a scalar factor. Motive maps also retain their Tate twists, as the earlier return stresses. The present polarization and Frobenius compatibilities do not identify those cocharacters or erase the twists.

### LC04 — A partial A–D dictionary, with two missing definitions

**Kind:** reading question. **Witness:** 15/170, “Positivité à la Hodge” and “diviseurs”; no A–D definitions occur in the current packet. **Context and relation:** restates the operational dictionary of N87 L09–L10 and its lettering table, and N195 M04, compared with CT16/040–049. **RESULTS_STATE:** WG2 §2.4 #3; MPL_15_087-138 §123; MPL_14_002-044 §107.

The contextual displays securely match manuscript A with the algebraic-class clause of printed A, and manuscript C with the inverse-Lefschetz content of printed B. The proposed B→D and D→C matches remain supported identifications by use, because the cited cote 16 witness does not give their standalone definitions. On CT16/044, C(X) also denotes the cycle-class space, so that occurrence cannot be treated as condition C.

| Manuscript letter and contextual witness | Operational content | Printed comparison | Confidence and limit |
|---|---|---|---|
| **A**, CT16/044–047 | Lefschetz maps on algebraic classes; critical-degree variants A⁰. | Grothendieck69 §3, p.196: **A**, including its algebraic-class clause. | Secure content match; printed A also includes the cohomological Lefschetz isomorphism. |
| **C**, CT16/040,042,045–049 | Algebraicity of inverse/complementary-degree Lefschetz maps, including the Λ formula and a Cayley–Hamilton inverse. | Grothendieck69 §3, p.196: **B**; Kleiman68 §2.3, p.370. | Secure operational match, without silently standardizing the source's notation. |
| **B**, CT16/044–045 | “A + index” implies B, and the index theorem identifies A and B. | Kleiman68 §3.6, p.379: **D**, homological = numerical equivalence; §3.9, p.380, gives the index comparison. | Strong parallel; the standalone manuscript B definition is missing. |
| **D**, CT16/040,046,048 | Projector algebraicity nearby; rational characteristic polynomials used alongside complementary-degree isomorphisms. | Printed **C**, algebraic Künneth projectors; Kleiman68 §§2.4,2.6–2.9, pp.370–371. | Supported parallel; the characteristic-polynomial criterion alone does not define manuscript D. |

### LC05 — Cote 16's singular-hypersurface programme remains unresolved for cote 14

**Kind:** reading question. **Witness:** 15/170, positivity/divisor agenda with question marks. **Context and relation:** differs from the explicit programme on CT16/047; restates the source boundary of N87 L11–L12 and N195 M05. **RESULTS_STATE:** WG2 §2.4 #3 and §Summary #2; MPL_14_002-044 §107; MPL_15_087-138 §123.

CT16/047 withdraws the proposed reduction to smooth hypersurfaces after Serre's simply-connectedness objection and asks to reformulate the standard conjectures for singular varieties. Current 170 gives a related positivity and reduction agenda, without the missing reformulation. No full raw cote 14 witness is supplied, so neither the current packet nor its register excerpt decides whether cote 14 carries the programme forward.

### LC07 — S15: the Nori–Ayoub group comparison has a fixed setting

**Kind:** unpursued implication. **Witness:** 15/183, finite-type base over Z; 15/191, “car p>0”. **Context and relation:** restates N87 T23/S15 (15/135,137) and N195 M07/S15, while adding a current boundary to their application. **RESULTS_STATE:** MPL_15_087-138 S15:; MPL_15_195-228+18_002-017 S15: and M07.

For a subfield of the complex numbers with chosen Betti data, Choudhury–Gallauer17, Theorem 9.1, proves inverse Hopf-algebra comparison maps, hence an isomorphism of the classical motivic groups, with principal-ideal-domain coefficients. This verifies the comparison already cited by the supplied returns, in particular over the rationals. It does not identify the manuscript's unspecified category, its algebraic-cycle morphisms, or the integral and positive-characteristic structures displayed here.

### LC08 — S15: motivated cycles and algebraic cycles are separate comparisons

**Kind:** unpursued implication. **Witness:** 15/170, pure motives and Hodge–Riemann agenda. **Context and relation:** restates N87 T24–T25 (15/135,137) and N195 M07–M08/S15; current 170 adds no cycle-surjectivity proof. **RESULTS_STATE:** MPL_15_195-228+18_002-017 M07 and M08; both S15 entries.

Arapura13, Theorem 6.3.3 and Corollary 6.3.4, give semisimplicity and a proreductive dual for the pure rational Nori subcategory; Theorem 6.4.1 compares it with André's motivated category. The further identification of motivated and algebraic-cycle morphisms requires additional input, such as the relevant standard conjectures. Neither these comparison theorems nor current 170 prove a general fullness or essential-image theorem for Hodge realization.

### LC09 — S15: effectivity is an additional, expressly conjectural condition

**Kind:** unproved claim. **Witness:** 15/185, “conjectures de Tate”; 15/187, cone “engendré” and algebraic-integral eigenvalues. **Context and relation:** adds a current condition to N87 T23–T25/S15 and N195 M07/S15; compare F08–F10. **RESULTS_STATE:** MPL_15_195-228+18_002-017 M07; both S15 entries.

The current effectivity-recovery assertion is framed through Tate conjectures and needs its own ambient cone and representation range. Neither Choudhury–Gallauer17, Theorem 9.1, nor Arapura13, Theorem 6.4.1, asserts this Frobenius criterion. Their established comparisons therefore leave this manuscript claim open.

### LC10 — S15: Witt vectors, F and V require further structure

**Kind:** unpursued implication. **Witness:** 15/191, Witt-valued object, “F et V”, filtration and derived-category margin. **Context and relation:** adds a characteristic-p and integral boundary to N87 T23–T25/S15 and N195 M07/S15; compare PD02–PD08. **RESULTS_STATE:** MPL_15_195-228+18_002-017 M07; both S15 entries.

The characteristic-zero Betti comparison does not assert the listed Witt-vector fibre objects, their uniqueness, or their F,V compatibility. Oda69 supplies the restricted degree-one result in PD04, while PD05 identifies a tensor-scope issue for the marginal FV=p relation. These are limits of the cited comparisons, not a claim that no other theory treats the structures in question.

## 7. Reused and incidental texts

The selected scans include seven leaves carrying distinct reused or incidental texts: root-system exercises on 171, a typed listing on 181, coherent-cohomology fragments on 184/186/188, and Lie-algebra editorial instructions on 192/194. Their headings, source pagination and equations support the contextual continuities below, without making them part of the handwritten motivic argument. The inventory also marks the handwritten faces 183,185,187,193 as reused_typed because they use reused typed sheets, as recorded during the visual reading; that physical classification does not turn their live motivic text into a reused mathematical source.

### RS01 — The cohomology leaves precede the neighboring equation (19)

**Kind:** reading question. **Current scans / quote:** 15/188, source folio 70, “there exists such $n'$”; 15/186, source folio 72, “Consider an exact sequence”; 15/184, source folio 73, “from (15), (18)”. **Context / delta:** adds preceding fragments to context/same_cote_15/MPL_15_087-138_notes.md, R09 at 15/126, equation (19), with source folio 74 recorded in its page-label table; differs in local scope from its R10 at 15/111,113,115, equations (21)–(23). **RESULTS_STATE:** WG2 §Summary #2; WG2 §2.4 #3; MPL_15_087-138 §123.

In source order the current fragments run 70 → [71 not supplied] → 72 → 73, although their scan order is reversed. Folio 72 supplies equality (15) and the restriction sequence (16), while folio 73 supplies its twist (17), cohomology sequence (18), and the threshold used in the base-point argument reported on neighboring folio 74. This adds an identifiable precursor to N87 R09, rather than re-proving its restriction-surjectivity argument or confusing it with the later calculation R10. The missing folio 71 and the context-only status of the 15/126 witness prevent describing the supplied selection as a complete continuous proof.

### RS02 — The projectivity-source identification remains provisional

**Kind:** reading question. **Current scans / quote:** 15/184, “condition of non-degeneracy”; 15/186, reference “p. 208”; 15/188, “$H^i(V,K[nE])=0$”. **Context / delta:** adds matching notation and earlier source pagination to context/same_cote_15/MPL_15_087-138_notes.md, R08 and P02 at 15/101,105–126; restates its provenance limitation, rather than confirming an attribution. **RESULTS_STATE:** WG2 §Summary #2; WG2 §2.3 #12; MPL_15_087-138 §123.

The divisorial notation, English exposition and restriction argument connect these fragments plausibly with the projectivity text headed on contextual scan 15/101, and the current “p. 208” reference matches one reported on 15/111. N87 R08's Moishezon/English-translation identification remains a lead from that first-pass return: the present fragments supply no title page, author or translator, and no external identification was checked in this follow-up. Coherent-sheaf vanishing and ampleness vocabulary are not evidence that this reused proof establishes the neighboring motivic or Lefschetz claims.

### RS03 — The Lie running labels extend the neighboring sequence

**Kind:** reading question. **Current scans / quote:** 15/192, “ALGÈBRES de LIE SEMI-SIMPLES (9)”; 15/194, the same heading with “(8)”; both “Tribu n° 59”. **Context / delta:** adds labels (9), (8) before the (7), (6), (5), (4), (3) sequence reported at 15/196,198,200,202,204 in context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, “Standing question II: title sheets and page counts”; restates its pagination-versus-extent distinction. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136; MPL_15_195-228+18_002-017 R01.

The matching running title and decreasing leaf labels support continuity between the current editorial leaves and the neighboring reused Lie-algebra series. The numbers (9) through (3) are source leaf labels, and Tribu n° 59 is an editorial identifier; neither gives a total extent or dates the motivic writing. The contextual 57|59 uncertainty on 15/200 remains that earlier return's reading question and is not corrected by the matching current headers.

### RS04 — The requested Lie revisions retain their separate editorial status

**Kind:** unproved claim. **Current scans / quote:** 15/192, “On en laissera tomber une” and “Donner la démonstration”; 15/194, “Donner ici les relations” and “le dire”. **Context / delta:** restates the source separation in context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, R01 at 15/196,200,206, and adds further editorial tasks alongside its R12 at 15/196; differs from the graded Lefschetz correspondence discussion in context/MPL_16+47+54+44_transcription.tex, 16/018. **RESULTS_STATE:** MPL_15_195-228+18_002-017 R01; MPL_15_195-228+18_002-017 R12; WG2 §2.3 #7; WG2 §2.4 #3.

These leaves ask a redactor to remove a duplicate construction, supply proofs and references, and revise root-space and module statements. They do not answer the separate generalization request recorded in N195 R12, whose referenced propositions are still absent from the supplied comparison. In particular, their semisimple Lie algebra and Weyl-module language supplies no identification of a Lefschetz action inside a motivic Galois group.

### RS05 — The root-system leaf is a separately titled reused text

**Kind:** reading question. **Current scan / quote:** 15/171, “SYSTÈMES de RACINES (20)”, “Tribu n° 59”, and “Groupe de Weyl $W$ de $E_7$”. **Context / delta:** adds a further running-title witness to context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, “Standing question II”, at 15/208,210,212; parallels, without identifying the same source, the reused chamber text at 54/008 and Tribu comments at 44/007 in context/MPL_16+47+54+44_transcription.tex. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136; MPL_15_195-228+18_002-017 R01; WG2 §Summary #2.

The exercise instructions and title identify a root-system source distinct from the motivic agenda on 170 and from the Lie-algebra running title on 192/194. Its label (20) can be compared with the neighboring root-system labels (3), (2), and unnumbered introduction, but does not establish that all intervening source leaves survive or that twenty is a total page count. The contextual chamber and Tribu texts show a related reuse pattern, not proof of identical provenance or a mathematical dependency.

### RS06 — “[name redacted] [name redacted]” closes a typed listing, not a mathematical text

**Kind:** reading question. **Current scan / quote:** 15/181, “[name redacted] [name redacted]”. **Context / delta:** adds an unmatched nonmathematical listing to the source-scope distinctions in context/same_cote_15/MPL_15_195-228+18_002-017_notes.md, “Standing question II”, especially its separate reused-source identifiers at 15/214,216,218; searches found no matching listing in that file, context/same_cote_15/MPL_15_087-138_notes.md, or context/MPL_16+47+54+44_transcription.tex and its notes. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136; WG2 §Summary #2.

Scan 181 contains numbered rows and personal-name/code columns ending with “[name redacted] [name redacted]”, with no mathematical statement to integrate into the motivic argument. The fragment does not identify its institution, purpose or date, and its row numbers and the separate marginal 180 do not determine the extent of the motivic dossier. It is retained as an incidental source witness without reproducing the personal entries in these research notes.

## Standing question I: author-self-flagged unverified steps

An author's explicit question mark, “sans doute”, requested verification, or conjectural dependency is distinguished below from the editor's **unsure** macro; the latter alone is not evidence of authorial doubt. This applies the distinction already made in N195's “Standing question I”, especially its motivic table (§133), without importing its later conclusions into these sheets.

| ID / kind | Current cote/scan and short quotation | Qualification, context comparison, and RESULTS_STATE |
| --- | --- | --- |
| U01 — self-flagged | **15/170:L6,17–19,45–47:** “À examiner”; “\(\mathbb R\) ???”; “Hyp. de Riemann ??”; marginal “diviseurs … ??” | The agenda explicitly leaves the finite-field real-valued-point problem, Riemann hypothesis, and proposed reduction of Hodge positivity to divisors open, while “OK” marks on some items do not supply proofs. **Adds** the exact qualifications to Hua §X, internal p. 169, whose final “par récurrence” summary does not preserve the frozen margin's doubtful alternatives involving blowups/pencils; compare N195 A12, **15/207:L8–10**, on real-valued points in characteristic \(p\). **RESULTS_STATE:** WG2 §2.4 #3 [unchecked]; MPL_15_195-228+18_002-017 §133 [first-pass lead]. |
| U02 — withdrawn in the same text | **15/183:L3:** deleted “la plupart des”, replaced by “certaines” | The reduction to even-degree motives is promised only for **certain** Frobenius-distribution questions; this is an authorial narrowing, although it is not an explicit question mark or a retraction of every such reduction. **Differs** from Hua §XII, internal pp. 181–186, which says simply that one passes to the even part; compare N195 §133's attention to weakened or cancelled assertions. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked]; MPL_15_195-228+18_002-017 §133 [first-pass lead]. |
| U03 — self-flagged | **15/185:L13–15:** “fini”; “[si \(G\) est commutatif en tous cas !]”; “? à vérifier” | The margin marks the nearby finiteness discussion for checking, and the commutative parenthesis is a stated qualification, not a proof of the general claim. **Adds** a live verification flag and restricted case absent from Hua §XII's account of the polarization condition, internal pp. 184–186; it follows the same recording distinction as N195 §133, **15/203:L13–24**, where two later identities explicitly carry “à vérifier”. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked]; MPL_15_195-228+18_002-017 §133 [first-pass lead]. |
| U04 — conjecture | **15/185:L17;15/187:L2–10:** “conformément aux conjectures de Tate”; “Le cône … engendré” | The recovery of effectivity from the \(u(s')\), continued on 187, is explicitly placed under Tate conjectures; the cone and Frobenius-integrality wording is subsequently asserted, rather than marked by a new author's question mark. **Supports** Hua §XII's conditional presentation, internal pp. 184–186, and **adds** the exact continuation and its status; compare N195 §133, **15/213:L29–37**, for a different explicitly conjecture-dependent assertion. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked]; MPL_15_195-228+18_002-017 §133 [first-pass lead]. |
| U05 — self-flagged | **15/191:L12–13,31–36,41–43:** twice “provenant sans doute”; “? … réduit”; deleted “sans doute” before “catégorie dérivée” | The two henselian origins and the reduction item remain tentative, whereas the margin's “sans doute” concerning the derived category is **deleted** and must not be counted as a live hesitation. **Differs** from Hua §XIII, “En caractéristique \(p\)”, internal p. 190, which renders the reduction as an unqualified item, and **anticipates** N195 A01–A05, **15/195–197**, on qualified mixed-characteristic comparison. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §133 [first-pass lead]; WG2 §2.4 #3 [unchecked]. |
| U06 — self-flagged | **15/191:L50–55:** “sans doute uniques … à isom près”; “th. de Lang”; “\(k\) parfait de dim [ch] \(1\) (?)” | Uniqueness of an isomorphism class is proposed under the weight-zero normalization, and the inserted extension beyond finite \(k\) carries a separate authorial “(?)”; the reading of “ch” remains editorially uncertain. **Supports** Hua §XIII's caution about unverified smoothness/connectedness hypotheses for the Lang/Hensel argument but **adds** the omitted perfect-field extension; compare N195 §133's qualification register for **15/195–197**. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §133 [first-pass lead]; WG2 §2.4 #3 [unchecked]. |
| U07 — conjecture | **15/191:L55–60:** “il faut s'attendre”; “il est possible”; “\(T_\infty(k)=\varprojlim T_\alpha(k)\)” | Several finite-stage isomorphism classes are expected, while one limiting de Rham–Hodge class is only suggested. **Restates** the qualification retained by Hua §XIII, internal p. 190, and **adds** an earlier instance of the finite-stage/global-comparison distinction recorded in N195 A28–A31, **15/219:L5–10;15/221:L3–19**, without importing that later argument as a proof. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §133 and §137 [first-pass leads]; WG2 §2.4 #3 [unchecked]. |
| U08 — self-flagged | **15/191:L62–63:** “relation … galoisien ??”; “Il doit être …, cf Manin” | The double question mark is authorial in the frozen text, but most surrounding words and the predicate “épuisant\|équivalent” are editorial alternatives, so the precise proposed relation is not established. **Differs** in placement and certainty from Hua §XIII's attachment of “cf. Manin” to its limit-uniqueness paragraph: its suggested identification with Manin's Dieudonné work is an interpretive lead, not a verified reading of this margin. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked]; MPL_15_195-228+18_002-017 §133 [first-pass lead]. |
| U09 — self-flagged | **15/193:L7–20,31–36:** “il ne semble pas”; “partie continue”; “en général … n'est plus isom” | The absence of isomorphisms between fibres at different \(k\)-valued points is explicitly tentative; the later conjugacy and semilinear-action clauses are assertions with stated field conditions, rather than additional author-marked questions. **Adds** this hesitation to Hua §XIII, internal p. 192, and **anticipates** N195 A01,A03,A05, **15/195–199**; the doubtful \(H^1\!\mid H^2\) exponent is editorial uncertainty and supplies no extra author's question. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §133 [first-pass lead]; claims #964 [open, only a related comparison problem]. |
| U10 — withdrawn in the same text | **15/179:L3–15,31–33:** cancelled Leray/torsion block; live “bijectif modulo torsion”; final colon | The cancellation withdraws the displayed supporting argument from the live text, while the boundary-map assertion remains live and the factoriality sentence is unfinished; no separate authorial question mark is supplied here. **Supports** Hua §XI's identification of the crossed supporting passage, internal pp. 178/175, but **differs** from reading his completed factoriality argument as present on this leaf. **RESULTS_STATE:** WG2 §1.1 #3 and WG2 §Summary #2 [unchecked]. |
| U11 — unproved claim | **15/171:L7–30;15/192:L6–14;15/194:L25–28,35:** “Montrer”; “Donner une seconde démonstration”; “dire pourquoi”; “donner les références”; “le dire” | These are explicit requested proofs, explanations, or references in reused root/Lie-theory sheets, not evidence of unresolved motivic conjectures or necessarily of mathematical doubt. **Extends** the corresponding classification in N195's “Reused typescripts: mathematical tasks and deferred proofs”, especially **15/196:L16–18;15/202:L12**, and its R01 provenance distinction. **RESULTS_STATE:** MPL_15_195-228+18_002-017 R01 [first-pass lead]; WG2 §1.1 #3 [unchecked]. |

**Exclusions across the full selection.** The title-only sheets **180,182,189,190**, administrative list **181**, and reused cohomological proof fragments **184,186,188** contain no additional author-self-flagged mathematical uncertainty in their frozen text; the last group's ordinary proof continuations and the phrases “It is evident” / “Let us show” are not doubts. This **restates** N195's standing-register distinction between ordinary proof continuation and an author's verification request (**15/214:L15–17,24–34** for a genuinely deferred task), with **RESULTS_STATE** MPL_15_195-228+18_002-017 R01 and §133 [first-pass leads]; editorial uncertainty on any of these leaves remains in the frozen transcription.

## Standing question II: title sheets and page counts

**No explicit total page count is stated on any of the selected title sheets or covers.** Square brackets in the short title quotations encode editorial uncertainty and are not authorial brackets. Eighteen is the number of scans selected for this package, not a manuscript's announced extent; the following titles, running labels, source folios, marginal numbers, and cross-references do not determine such an extent.

| ID / kind | Current cote/scan and short quotation or number | Context comparison, interpretation, and RESULTS_STATE |
| --- | --- | --- |
| T01 — reading question | **15/170:L4–6,49:** “Foncteurs fibres motiviques, et [gpes] [fondamentaux] motiviques”; “À examiner”; bottom **169** | **Supports** Hua §X, internal p. 169, as a programme heading with ten items numbered 0–9; neither those item numbers nor 169 states a total page count. The bracketed title words here summarize frozen editorial uncertainty, not authorial brackets. **RESULTS_STATE:** WG2 §2.4 #3 [unchecked]; MPL_15_195-228+18_002-017 §136 [first-pass lead]. |
| T02 — reading question | **15/180:L3–10:** “[Calcul\|Calculs] de [cohomol.] absolue / du motif de Tate / \(\mathbb Z([n\|u])\)”; bottom **179** | **Supports** the repeated-title identification in Hua §XI, internal p. 179, while preserving the current title's unresolved singular/plural and argument; Hua's separate cover at internal p. 171 is outside this selection. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136 [first-pass lead]; WG2 §Summary #2 [unchecked]. |
| T03 — reading question | **15/182:L3–8:** “Généralités [fonctoriello-catégoriques] sur la distribution des frobenius dans les [gpes] de Galois motiviques”; bottom **181** | **Supports** Hua §XII's identification of the distribution heading at internal p. 181, but does not import his normalized “fonctorielles-catégoriques” into the frozen title. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136 [first-pass lead]; WG2 §2.4 #3 [unchecked]. |
| T04 — reading question | **15/189:L2–6:** “Théorie de Galois des Motifs / Généralités”, bottom **188**; **15/190:L2–6:** “Foncteurs fibres motiviques / et [gpe\|gpes] [fondamental\|fondamentaux] / [motivique\|motiviques]”, bottom **189** | **Supports** Hua §XIII's two-cover identification at internal pp. 188–189, while retaining the unresolved number of “groupe(s)” in the second heading. No total or relationship of total extents is stated. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136 [first-pass lead]; WG2 §2.4 #3 [unchecked]. |
| T05 — reading question | **15/171:L3,15,32:** “SYSTÈMES de RACINES (20)”; “Tribu n°59”; “F) Groupe de Weyl \(W\) de \(E_7\)”; bottom **170** | **Adds** another source leaf to the same reused title family recorded by N195 §136 at **15/208,210,212**, with labels (3),(2) and a separate introduction. Here (20), “F)”, and 59 are source/section identifiers, not evidence for a twenty-page motivic dossier. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136 and R01 [first-pass leads]. |
| T06 — reading question | **15/192:L2,16,40;15/194:L2,37:** “ALGÈBRES de LIE SEMI-SIMPLES (9)” / “(8)”; “Tribu n°59”; “§4 — Théorèmes d'existence, (nouveau titre)”; bottoms **191,193** | **Extends** N195 §136's ensuing labels (7),(6),(5),(4),(3) at **15/196,198,200,202,204** and preserves the instruction that “Théorèmes d'existence” is a proposed internal heading of the reused source. These labels and its references to pp. 46–57, Jacobson pp. 123–124, propositions, and sections are not title-sheet totals. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136 and R01 [first-pass leads]. |
| T07 — reading question | **15/184:L2,22,29:** **73**, “See p. 202”, bottom **183**; **15/186:L2,16,29:** **72**, “p. 208”, bottom **185**; **15/188:L2,36:** **70**, bottom **187** | These untitled proof continuations carry source folios **73,72,70 in scan order**; neither the skipped 71 nor a complete source extent is reconstructed. **Restates** N195 §136's separation of reused pagination and manuscript numbering, concretely comparable with **15/220–228**, source pp. 12,9,7,6,5. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136 [first-pass lead]; WG2 §1.1 #3 [unchecked]. |
| T08 — reading question | **15/181:L6–19,22–24:** row codes **0170–0183**; “[name redacted] [name redacted]”; bottom **180** | The numerical row codes belong to the reused administrative list and its ending; they do not give manuscript pagination or a document total. **Adds** a distinct source-identifier case to N195 §136's pagination distinction, whose reused bibliography at **18/003** likewise has source numbers separate from the motivic sequence. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136 [first-pass lead]; WG2 §1.1 #3 [unchecked]. |
| T09 — reading question | **15/185:L3,12,19:** inserted “\(\pi\)”; later “\(\pi^{\xi(s')}\)”; bottom **184** | The frozen text uses the polarization symbol \(\pi\), not a heading “II”, and **supports** Hua §XII's “\(\pi\)-structure” interpretation at internal pp. 184–186. It supplies no page count or additional titled section. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136 [first-pass lead]; WG2 §2.4 #3 [unchecked]. |
| T10 — reading question | **15/179,183,187,191,193:** bottoms **178,182,186,190,192**; **15/191:L4,11,26,35** “1°)”, “(i)–(iii)”; **15/193:L38** “Notations” | These five remaining leaves have content/subsection labels rather than additional title-sheet totals; across **all eighteen selected scans**, each bottom marginal number is the current scan number minus one. **Restates** N195 §136's separation of pagination systems and **supports** Hua's use of internal pp. 178,182,186,190,192 for these materials, without treating either numbering system as the extent of a manuscript. **RESULTS_STATE:** MPL_15_195-228+18_002-017 §136 [first-pass lead]; WG2 §1.1 #3 [unchecked]. |

No missing title leaf, intervening source page, sheet total, or total manuscript length is inferred from these registers.

## 8. Further register questions and scope

### Q01 — The class-field agenda does not identify a CM or Taniyama group

**Kind:** reading question. **Witness:** 15/170, “Relations avec le corps de classes”; 15/183, choice of a real motivic point. **Context and relation:** adds a bounded negative finding for the current selection; differs in corpus from N87 §125's negative searches in CT/CN and from the earlier CM/class-field material in Hua §§VI–IX (source pages 127–164). **RESULTS_STATE:** LM6 A.22; MPL_15_087-138 §125; WG2 §2.4 #3.

The selected pages contain no identification of a Taniyama or Shimura group, no construction or exclusion of a nontrivial closed procyclic C in the register's R whose arithmetic normalizer has open image in \(G_{\mathbf Q(i)}\), and no completion of the class-field agenda. Hua's earlier chapters treat the maximal real/CM extension and commutative motivic groups, but those manuscript pages are outside this selection. The present real-twist and parity data give scope conditions for a future comparison, not a resolution of the precise subgroup problem LM6 A.22.

### Q02 — No supersingular-correspondence assertion occurs in this packet

**Kind:** reading question. **Witness:** 15/183, “degrés … pairs” and chosen real point; 15/191–193, characteristic-p fibre objects. **Context and relation:** differs in subject from Hua §§II–III, “Catégories de Deuring” and the Brandt/Picard construction (source pages 15–77), while the real-obstruction link is compared in HG03. **RESULTS_STATE:** ANABELIAN_SUCCESSOR A.57; LM7 E.23; FLAGGED_149 B9; RS “Orientation for this package”.

The current characteristic-p discussion does not state a universal assertion about supersingular correspondences, quaternion orders or Brandt groupoids. Hua's interpretation of those earlier pages remains credited to his project, and its real-obstruction bridge cannot be transported across the even-degree restriction without checking the category. Thus these scans supply neither proof nor counterexample for the named open programme items.

### Effect on the supplied results register

This is a report of what the current evidence adds, not an edit of RESULTS_STATE or a change of its statuses.

| Register entry | Current anchor and addition | Status after this packet |
|---|---|---|
| **claims #964** | 170's lattice-comparison agenda; 185's transported-polarization compatibility; 193's tentative non-isomorphism across p-adic points. A03, F05 and PD12 distinguish these from the later archimedean place/torsor problem. | Open: no proof of injectivity, characterization of torsors arising from places, or Hodge-enriched recovery. |
| **LM6 A.22, LM6 A.50; MPL_15_195-228+18_002-017 B04** | 183's Tate kernel and 191's weight-zero normalization do not supply a cyclotomic normalizer; 193 distinguishes actions. BG04–BG05 preserve the missing character premise. | A.22 remains Open; A.50 retains Proved, the return's claim. Its truncated excerpt is not expanded into an unstated theorem. |
| **ANABELIAN_SUCCESSOR A.57; LM7 E.23; FLAGGED_149 B9** | Q02 and HG03 record the restricted relation to Hua's earlier supersingular/real-obstruction discussion. | No direct current witness of the proposed universal-correspondence assertion, and no status change. |
| **WG2 §2.4 #3; MPL_15_087-138 L03/§111/§123/§124** | Category assumed on 183; exact current qualifications on 185,191,193; partial lettering and source boundaries in LC01–LC05. | Existing projective-line and cocharacter calculations remain credited; missing constructions and missing cote 14 evidence remain missing. |
| **Both same-cote S15 entries; MPL_15_195-228+18_002-017 M07–M08** | G03 and LC07–LC10 specify the modern comparison theorems and the current effectivity/integral limits. | Primary theorem statements checked in their stated settings; no identification of the entire manuscript programme with those categories. |
| **MPL_15_195-228+18_002-017 §2; MPL_15_087-138 §124** | PG01–PG02 distinguish absence of a current period conjecture from positive reported cote 18 witnesses. | A precise contextual lead, pending independent visual verification of the neighboring scans. |
| **WG H9; WG2 §2.3 #12** | 170's odd-weight/Hodge–Riemann and divisor/pencil agenda, compared with CT44/002–009. | Sign that the programme was being pursued; no missing positivity proof supplied here. |
| **MPL_15_195-228+18_002-017 R01/R12/§136** | RS01–RS06 and the title register identify reused-text continuities and editorial tasks. | Source separation strengthened; no reused theorem is transferred to the motivic argument. |

## 9. Primary references and what was checked

The keys below cite primary papers or official documentation, not secondary summaries. Access was checked on 17 November 2026; a searchable primary-paper passage is distinguished from a full direct PDF reading, and no entire proof audit is claimed.

| Key | Bibliographic source | Checked locus and retrieval limit |
|---|---|---|
| **Tate66** | John Tate, “Endomorphisms of Abelian Varieties over Finite Fields”, *Inventiones mathematicae* **2** (1966), 134–144. [Published paper](https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf). | p.134, displayed Hom map (1) and finite-field bijectivity; direct primary PDF text. |
| **Mochizuki99** | Shinichi Mochizuki, “The Local Pro-p Anabelian Geometry of Curves”, *Inventiones mathematicae* **138** (1999), 319–423. [Author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf). | Introduction, Theorem A, PDF p.3, with the preceding notation; both profinite and geometrically pro-p versions are stated. The table uses ordinary hyperbolic curves, within its scope. |
| **Stix12** | Jakob Stix, “On cuspidal sections of algebraic fundamental groups”, *Advanced Studies in Pure Mathematics* **63** (2012), 519–563. [Author version](https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXcuspsec20120802homepage.pdf). | Definitions 26 and 29 and Theorem 30, author-version pp.10–11; direct text checked, including both premises of essential cyclotomic normalization. |
| **Kahn25** | Bruno Kahn, *Galois descent for motivic theories*, arXiv:2312.01825v4, 29 May 2025. [Author preprint](https://arxiv.org/pdf/2312.01825). | §5.8 and Theorem 5.10, printed p.19; §10, printed pp.24–25, especially Proposition 10.1, Theorem 10.2 and Remark 10.3. The retrieved PDF identifies itself as v4. |
| **Grothendieck69** | Alexander Grothendieck, “Standard conjectures on algebraic cycles” (1969), pp.193–199. [Primary text](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf). | §3, p.196, printed A/B: searchable primary-page passage checked. Direct PDF extraction supplied no readable lines; no full visual recheck of this paper is claimed. |
| **Kleiman68** | Steven L. Kleiman, “Algebraic cycles and the Weil conjectures”, *Dix exposés sur la cohomologie des schémas* (1968), 359–386. [University-hosted primary text](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf). | §§2.3–2.9 and §§3.6,3.9; the inverse-operator, Künneth, characteristic-polynomial and index comparisons were checked in the primary text. The earlier archive mirror returned 404; the university copy supplied the text. |
| **Choudhury–Gallauer17** | Utsav Choudhury and Martin Gallauer Alves de Souza, “An isomorphism of motivic Galois groups”, *Advances in Mathematics* **313** (2017), 470–536. [DOI](https://doi.org/10.1016/j.aim.2017.04.006); [accepted manuscript](https://ora.ox.ac.uk/objects/uuid%3Ab86c4da7-d7ad-4b63-abc2-c78853bf050a/files/md8343c1db0d1a4927ecb71bb3205cbc0). | Theorem 9.1, accepted-manuscript p.41, including the PID hypothesis, and publisher introductory field/Betti setting. Direct PDF retrieval was blocked; indexed primary-paper passages were checked. |
| **Arapura13** | Donu Arapura, “An abelian category of motivic sheaves”, *Advances in Mathematics* **233** (2013), 135–195. [Primary-paper repository](https://pure.mpg.de/pubman/item/item_3121497_1/component/file_3121498/Arapura_an%2Babelian_oa_2013.pdf); [paper mirror](https://files01.core.ac.uk/download/pdf/223016697.pdf). | Theorem 6.3.3, Corollary 6.3.4 and Theorem 6.4.1 (author version p.60 for the last); indexed primary-paper statements checked, direct repository PDF retrieval blocked. |
| **Oda69** | Tadao Oda, “The first de Rham cohomology group and Dieudonné modules”, *Annales scientifiques de l'École Normale Supérieure*, fourth series **2** (1969), 63–135. [DOI](https://doi.org/10.24033/asens.1175). | Supplied PDF: Definition 3.1, printed p.80/PDF p.19, and Corollary 5.11, printed p.131/PDF p.70, rendered and visually checked for the research comparison. |
| **Lang56** | Serge Lang, “Algebraic Groups Over Finite Fields”, *American Journal of Mathematics* **78** (1956), 555–563. [Published paper](https://wstein.org/papers/bib/Lang-Algebraic_Groups_Over_Finite_Fields.pdf). | Theorem 2, pp.557–558, with connected algebraic-group setting; searchable primary passage checked. The application to the current integral isomorphism objects remains conditional on the hypotheses in PD06. |
| **Stacks** | The Stacks Project: [Tag 07M7](https://stacks.math.columbia.edu/tag/07M7), Lemma 15.9.14; [Tag 04GE](https://stacks.math.columbia.edu/tag/04GE), Lemma 10.153.3(7). | Smooth lifting after an étale extension and the henselian retraction criterion, read directly; their combination gives the lifting step used in PD06. |

## 10. Reading limits and follow-up priorities

The highest-priority future visual checks are 170's compressed item 1 and lower positivity addition; 183's adjective, kernel superscript and compatibility letter; 185's distinction between μ₂ and later μ_C; and 191/193's obstruction exponents and short marginal clauses. These remain explicit doubts or research reading questions, including when Hua suggests a mathematically clearer alternative. The provenance and neighboring-page claims remain limited to the supplied contextual transcriptions and notes; no absent cote 12–14 or 18 scan has been silently treated as inspected.

The immediate mathematical tasks are to specify the full cocharacter and common ambient cone in F02/F10, delimit the representation range in F09, prove or delimit the flagged finiteness statement in F06, and state the integral tensor target and comparison hypotheses in PD05–PD09. These are research directions, not repairs to the frozen manuscript. The 19 frozen-file hashes are checked again at delivery, with the outcome in `progress.log`; the doubts file and inventory remain separate from these interpretive notes.
