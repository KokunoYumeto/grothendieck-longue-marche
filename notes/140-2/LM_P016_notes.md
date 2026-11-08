# LM_P016 — Notes accompanying the diplomatic transcription

## Scope, source, and numbering

The transcription is based on the ten supplied JPEGs, `LM_P016_scan151.jpg` through `LM_P016_scan160.jpg`. No external transcription, edition, OCR output, or mathematical reconstruction was used to supply words in the fragment. The research notes below are separate from the transcription; they are not a literature review, a statement of novelty, or a claim that any question remained unresolved beyond these pages.

Source identification, following the supplied task brief:

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished manuscript; Université de Montpellier archive, cote 140-2, “pages 1–292”; supplied scans 151–160, archive page counters 150–159]. Université de Montpellier.

The five upper handwritten numerals are represented by `\mspage{75}` through `\mspage{79}`. The lower-left handwritten counters are recorded separately as `\margin{150}` through `\margin{159}`: their authorship is not established by these images, so they have not been conflated with the upper folio numbers. The printed Montpellier footer and printed page counter are not manuscript text and are not transcribed.

| Scan | Upper handwritten folio | Lower-left handwritten counter |
|---|---:|---:|
| 151 | 75 | 150 |
| 152 | — | 151 |
| 153 | 76 | 152 |
| 154 | — | 153 |
| 155 | 77 | 154 |
| 156 | — | 155 |
| 157 | 78 | 156 |
| 158 | — | 157 |
| 159 | 79 | 158 |
| 160 | — | 159 |

The LaTeX file is a fragment, without a preamble or macro definitions. It uses the requested editorial macros and conventional mathematical LaTeX/TikZ-CD syntax. Diagram descriptions in square brackets are editorial descriptions authorized by the task, not words attributed to the manuscript. The prose is not translated. Apparent notational and grammatical difficulties have not been silently repaired.

## 1. Table of doubts

Line references are approximate handwritten main-text baselines, not line numbers in the `.tex` file. Marginal passages, displays, and insertions are located by description when a numerical line would be misleading. “High” means the specified reading or feature is visually relatively secure; “medium” and “low” describe decreasing confidence. Word counts in `\illegible{n}` are estimates. Repeated instances of the same alphabet uncertainty are covered by the first rows.

| Scan | Approximate line or location | Reading in the fragment | Alternatives or unresolved issue | Confidence |
|---|---|---|---|---|
| 151–160 | throughout | `E (looped extension-group letter)` | The ordinary/script alphabet of this letter is not secure. It is consistently marked with \unsure in the fragment; E is not a claim that a script form was absent. | medium |
| 152, 155–160 | orientation-module notation | `T` | The orientation letter may be a distinguished, double-stroked, or script T. Uncertain instances are marked; no identification with ℤ has been inserted unless written on the page. | medium |
| 151–160 | selected subscripts and exponents | `Γ, π, primes, subscripts 0/1/x, and the sign !` | The greatest symbol-level risks are overwritten primes and small indices. Local doubts are listed below; repeated notation elsewhere has not been used to silently repair an uncertain occurrence. | low |
| 151 | 1–2; upper insertion | `E; \Gamma'; \Gamma'_x` | Ordinary/script E; the subscript x on the initial Γ′ is not clearly present. | medium |
| 151 | 2–3; insertion at right | `un sous-groupe; soit \Gamma_1\supset\Gamma_x le s-g de \Gamma` | The inserted subscript and abbreviated wording are overwritten; attachment is to the introduction of Γ″. | low |
| 151 | 5 | `y\in U^{\Gamma_1}` | The exponent is heavily corrected; Γ″ with a star-like subscript is also possible. | low |
| 151 | 7–9 | `\Gamma_1; [deleted word]` | The subscript is overwritten; the deleted word before « fixe » cannot be recovered. | low |
| 151 | 10–11 | `cqfd.; L'injec; b)` | The first two are crossed out; b) is inserted over the second. | medium |
| 151 | 13 | `thm` | The abbreviation is compressed; no expansion has been supplied. | medium |
| 151 | 17–19 | `appliqué à l'action de \Gamma_0 sur U; [deleted fixe]` | Insertion wording and attachment; the deleted word has an uncertain final letter. | medium |
| 151 | 19 | `x\in U^{\Gamma'_0}; \Gamma'_0\subset\Gamma_x` | The apparent prime on Γ′₀ is retained; no prime has been added to Γx despite the resulting notational tension. | medium |
| 151 | 24–25 | `ce [deleted word] qui prouve b)` | The deleted material after « ce » is not recoverable. | low |
| 152 | 2 | `T-orientée` | The orientation letter may be blackboard/script T; its exact alphabet is not secure. | low |
| 152 | 3 | `anabélien \| anabélique` | The final letters are compressed; do not regularize by terminology. | medium |
| 152 | 3–4; insertion | `« ple »` | This appears to be an abbreviated insertion before « fidèle »; the letters and quotation marks are uncertain. | low |
| 152 | 6–9 | `se doit de convaincre; quand; suffit` | Compressed wording; the syntax has deliberately not been repaired. Two crossed-out words before « l'op. » are unreadable. | low |
| 152 | 11 | `isotopique` | This is a visual reading, not a reconstruction of the intended category. | medium |
| 152 | left margin | `pour la suite…` | Beginning of the marginal note is legible; its ending is less secure. | medium |
| 152 | 13–15 | `U^!; J (\simeq U^!)` | The first U is overwritten; a tilde in the inserted identification cannot be excluded. | low |
| 152 | 18–19 | `on a le; donné` | The words preceding and following « torseur » are overwritten and do not yield a secure syntactic reading. | low |
| 152 | 21–23 | `c'est un \pi/\pi^{\Gamma'}-torseur; le stabilisateur \| les stabilisateurs` | Crossed-out phrase and its supralinear replacement; quotient/exponent and singular/plural are uncertain. | low |
| 153 | 1 | `ttes; [deleted classes]` | The abbreviated quantifier and the crossed-out noun are uncertain. | medium |
| 153 | 1; upper numeral | `76` | The second digit is cursive; the folio sequence supports but does not replace its visual reading. | medium |
| 153 | 9 | `d'envisager la reconstitution \| d'essayer de reconstituer` | The verb and the last letters of the noun/verb are unclear; two phrase-level readings are retained. | low |
| 153 | 13 | `X′, S′` | The X is overwritten and an apparent prime is retained under a doubt mark. | low |
| 153 | 14–17 | `action; On espère trouver un; = … évident` | Crossed-out material; most of the second deleted sentence is not recoverable. | low |
| 153 | 20–22 | `J (\simeq U^!) \| J (\simeq \widetilde U^!)` | The mark over U may be a tilde or an overwrite; the supralinear phrase appears to say « comme Γ-ensemble ». | low |
| 153 | 22–24 | `deleted l'action; du; de Γ` | Three local cancellations complicate the final clause; their surviving letters are only partly clear. | medium |
| 154 | 3 | `\Gamma\to\operatorname{Autext}(\pi)` | The initial group symbol and arrow are overwritten; Γ→ is a tentative visual reading. | low |
| 154 | 6–8 | `ou un pro-légomène; U^!\longrightarrow U` | The phrase after Ũ\|U! is especially uncertain; the source of the displayed application is corrected. | low |
| 154 | first diagram | `B_J\to B_E \| B_J\to B_\pi; \rho \| ?` | Right subscript and arrow label are heavily overwritten; the left-to-right arrow is clear. | low |
| 154 | 11–13 | `morph; \rho^* \| ?^*; [deleted symbol]` | Crossed-out word before « foncteur », inverse-image label, and separate cancellation at the left of the second diagram are uncertain. | low |
| 154 | second diagram | `B_E \| B_\pi; vertical identifications` | The lower annotation visibly reads π-Ens and is not used to repair the ambiguous upper subscript. | low |
| 154 | 16 | `deleted qui` | A short word between « Ce » and « n'est » has been cancelled. | low |
| 155 | 1; cancelled addition | `avec op. fidèle de Γ` | The small line below « par π » is struck through; its first word is uncertain. | medium |
| 155 | 6–7 | `draconiennes; (Pour les formuler, on va supposer l'action de Γ fidèle)` | The compressed adjective is uncertain. The long insertion is read tentatively and placed at the end of the introductory phrase; its anchor is not explicit. | medium |
| 155 | 8–10 | `cyclique (si Γ′=Γ′⁰) ou; diédral (si Γ′≠Γ′⁰)` | The supralinear condition is partly overwritten; a short cancellation before « diédral » is unreadable. | medium |
| 155 | left margin, 8–13 | `bon \| donc` | A tiny oblique marginal word beside the double vertical emphasis rule is uncertain. | low |
| 155 | 14–16 | `[deleted two words]; marginal !` | A cancellation before « au moins » and a separate vertical marginal mark cannot be securely read. | low |
| 155 | 20–22; μ display | `\mu_E; T` | The subscript is overwritten. The target's orientation letter is rendered T with a doubt mark because its precise alphabet is unclear. | medium |
| 155 | 22–24 | `obtenue; d'où; labelled injection i` | The small connector before ℤ/nℤ is uncertain. The hook and rightward direction are visible; i is below the arrow. | medium |
| 155 | lower-left NB | `savoir; est; définir; five unreadable words` | The diagonal marginal note is compressed and partly meets the page edge. Only its recoverable fragments are transcribed; its reasoning is not completed. | low |
| 155 | last line | `d'où \| d'un sous-groupe` | The connector after ℤ/nℤ≃Γ′ is not secure. | low |
| 156 | 1 | `u; \overline{\mathrm m} ordre n` | The initial u is overwritten. The bar-over-m abbreviation is retained rather than expanded. | medium |
| 156 | 4–6 | `n.ième` | The ordinal ending and punctuation are compressed. | medium |
| 156 | 9–10 | `les \| des conditions` | The article before « conditions évidentes » is ambiguous. | medium |
| 156 | below the brace | `ordre μ(u) = ordre de u` | Written smaller below the two braced identities. It is retained as a separate unbraced line, not silently omitted or integrated into the brace. | high |
| 156 | 17 | `deleted de` | A short deletion precedes E, E′. | low |
| 156 | 21–22 | `qui ne soit compatible` | No « pas » is securely visible between « soit » and « compatible »; it has not been supplied. | medium |
| 157 | 1; upper insertion | `(card I=2); cancelled mark before it` | The cardinality condition is visible; a preceding overwritten item is not readable. | medium |
| 157 | 2–4 | `on doit avoir (pour avoir une action fidèle de Γ=Γ⁰)` | The inserted phrase runs across and around cancelled lines. The final equality is uncertain. | low |
| 157 | 4–6 | `E≃ℤ; sauf 1 \| e` | The excluded identity glyph is heavily inked. | medium |
| 157 | 7 | `et peut se reformuler` | Cancelled wording is partly obscured. | low |
| 157 | 8–9 | `deleted t.f.; inserted rg n` | The rank/finite-type correction is not fully legible. | low |
| 157 | first diagram | `X₀(π); Tore de dim n associé à π` | A short vertical stroke connects the object to the annotation; it has no visible arrowhead. | high |
| 157 | cohomology diagram | `classe d'extension \| classes d'extensions` | The singular/plural of the left annotation is unclear; the isomorphism itself points left. | medium |
| 157 | 20–22 | `Γ-X₀(π)-torseur; espace homogène` | The mark between Γ and X₀ is overwritten; « espace » is tentatively read. | low |
| 158 | 4–5 | `rendrait` | Part of the word rises above the line; whether it is a continuous word or an insertion is not secure. | medium |
| 158 | 8; cohomology annotation | `↓ \| ≃ above π∨` | The underbrace under H¹(π,ℤ) is clear; its small intervening identification/arrow mark is uncertain. | low |
| 158 | 10–11 | `deleted groupe; inserted groupe` | The repeated/corrected noun is heavily crossed. Both readings are tentative; no cleaner replacement has been inferred. | low |
| 158 | 12–14 | `θ; en; closing parenthesis after idπ` | The automorphism symbol is overwritten. A closing parenthesis is visible, but a corresponding opening parenthesis was not securely found and has not been added. | medium |
| 158 | 15 | `standard \| st. dont` | The compressed expression after « géométrique » may be the full word or an abbreviated form; neither expansion is silently imposed. | low |
| 158 | 17 | `i.e. 2; Pb` | The short expression before 2 is uncertain; Pb is retained as written. | medium |
| 158 | 19–20 | `T⊗ℤ/νℤ; où ν est d'ordre u` | The auxiliary letter is read as ν, not silently normalized to n. The order phrase is uncertain and has not been mathematically repaired. | low |
| 158 | 22–23 | `cancelled word before orienté; deux-` | The deletion is unreadable. The final stroke after « deux » may be a hyphen or the tail of the word. | low |
| 159 | 1–2 | `endom du vectoriel` | Abbreviation and following noun are compressed; no expansion of endom is supplied. | medium |
| 159 | 6–8 | `pro-algébrique; seult` | Both compressed readings are uncertain. The short underlined form is not expanded to « seulement ». | low |
| 159 | 8; insertion | `(ℤ̂-module libre de rg 2)` | The explanatory insertion is placed after π=π₁(X,0), where its leader appears to attach. | medium |
| 159 | 12; characteristic polynomial | `b=det u` | The determinant notation is overwritten; an accent or variant abbreviation cannot be excluded. | medium |
| 159 | middle-left margin | `pour Ω=ℂ … revient à … orientation(s) de …` | Only fragments of this oblique note are recoverable. The visible double vertical rule is described separately. | low |
| 159 | 17–18; insertion | `μ(u)∈μ_n^*(Ω); deleted dernière` | There appears to be a star above the subscript n; omitting it would be unsafe. The overwritten base noun is uncertain. | low |
| 159 | 20–22 | `ext.; deleted two words; d'` | The insertion is attached to autom; the cancellation and connector before « un tel groupe » are not fully legible. | low |
| 159 | lower-left margin | `oui, il le peut … sous-groupes … de E` | The beginning is clear, but the adjective/noun specifying the subgroups cannot be recovered confidently. | low |
| 159 | lower-left marginal diagram | `1\|0→T→E_i→Γ_i→1; Γ_i≃T/n_iT` | The sequence is oblique and crowded. Its subordinate identification and final words are not reliably readable; a description is used instead of a completed diagram. | low |
| 159 | last line | `groupes à` | The overwritten ending before the continuation « (1) lacets) » is uncertain. | low |
| 160 | 1–3 | `(1) lacets); deleted two words` | The page continues scan 159 mid-sentence. The cancellation between « seule » and « connaissance » is not recoverable. | low |
| 160 | 7–8 | `deleted words around inserted dans` | The placement of « dans » is visible; the superseded words are not securely legible. | low |
| 160 | μ display and annotation | `{}_∞E; ens des; élémts` | The infinity sign is below/left of E. The annotation is small and partly overlaps the oblique marginal note; its abbreviations are tentative. | medium |
| 160 | 12–15 | `Autext_ℓ(π); Aut \| tt entier` | The subscript appears to be a cursive ell. The compressed token before « entier » is uncertain and is not expanded. | low |
| 160 | left margin | `cela semble bien … Γ résoluble … réaliser géométriquement` | Only the marked fragments are recoverable. The missing words prevent a secure reading of the marginal argument. | low |
| 160 | section 16 heading | `toposiques` | The letter sequence favors this reading, but « topologiques » cannot be entirely excluded. The second heading has a wavy single underline. | medium |
| 160 | final diagram | `B_{J_*}\|B_{J^*}→B_U\|B_π` | The star's relation to J and the target subscript are uncertain; the arrow points right. | low |
| 160 | final NB | `reflète 2-fidlt; status of the NB` | The abbreviation and numeral are uncertain. The NB begins beside the diagram and continues below; it is represented as a marginal note rather than silently integrated into the main sentence. | low |

## 2. Abbreviations encountered

Expansions are interpretive and belong only to this list. An uncertain reading remains uncertain even when its likely expansion is familiar. Case and punctuation variants are retained separately where encountered; the absence of a period in the left column is intentional.

| Written or transcribed form | Possible expansion or meaning |
|---|---|
| `2-fidlt` | 2-fidèlement (possible expansion of uncertain writing) |
| `\overline{\mathrm m}` | même |
| `Alg` | algébrique |
| `alg` | algébriquement / algébrique (according to the expression) |
| `Aut` | automorphismes |
| `Autext` | automorphismes extérieurs |
| `autom` | automorphisme |
| `autom.` | automorphisme |
| `car.` | caractère (probable) |
| `card` | cardinal |
| `cf` | confer; compare |
| `cqfd.` | ce qu’il fallait démontrer (crossed out; reading uncertain) |
| `dim` | dimension |
| `endom` | endomorphisme (uncertain reading) |
| `Ens` | ensembles |
| `ens` | ensemble |
| `Ens.` | ensembles |
| `ext.` | extérieur |
| `géom` | géométrie |
| `géom.` | géométrique |
| `i.e.` | id est; that is |
| `Im` | image |
| `isom.` | isomorphisme |
| `morph` | morphisme (uncertain crossed-out reading) |
| `NB` | nota bene |
| `op.` | opération |
| `Pb` | problème |
| `ple` | pleine (possible expansion of an uncertain insertion) |
| `pt` | point |
| `resp.` | respectivement |
| `rg` | rang (uncertain inserted reading) |
| `s-g` | sous-groupe (uncertain reading in an insertion) |
| `seult` | seulement (uncertain reading) |
| `ss groupe` | sous-groupe |
| `ss-groupe` | sous-groupe |
| `ss-groupes` | sous-groupes |
| `st.` | standard (possible expansion; reading uncertain) |
| `t.f.` | de type fini (uncertain crossed-out reading) |
| `th.` | théorème (probable) |
| `thm` | théorème (uncertain abbreviated reading) |
| `Tr` | trace |
| `tt` | tout / tous, according to context |
| `tte` | toute |
| `ttes` | toutes (uncertain reading) |
| `élémts` | éléments (uncertain reading) |

## 3. Legibility and reliability

The main text is moderately legible, but several pages combine faint strokes, rapid abbreviations, overwritten mathematical symbols, and additions threaded between existing lines. The clearest portions are many of the uncorrected prose clauses, the two identities for μ on scan 156, the principal arrows in the cohomological calculation on scan 157, and much of the closing transition to section 16. Clear formulas do not make the surrounding hypotheses equally clear.

The least reliable portions are the corrected subgroup notation on scan 151; the abbreviated sentence and torsor wording on scan 152; the cancelled sentences on scan 153; the target subscripts and labels in the diagrams on scan 154; and the diagonal marginal notes on scans 155, 159, and 160. In particular, the subgroup description and subordinate identifications in the lower-left diagram on scan 159 have not been recovered fully. The final NB on scan 160 has an uncertain abbreviation and an uncertain status as a marginal addition rather than continuous main text.

Several choices are deliberately not normalized: the prime in the fixed-point notation on scan 151; the relation between J and U! or Ũ! on scan 153; the ambiguous B-subscript beside the visible annotation “π-Ens” on scan 154; the missing “pas” in the clause on scan 156; the order phrase involving ν and u on scan 158; and unmatched parentheses visible in the draft. Where the exact alphabet of E or T cannot be established, the uncertainty is marked rather than resolved by mathematical convention.

This is a conservative working transcription, not a certified critical edition. It contains unresolved words and symbols, approximate counts for illegible spans, and tentative readings of corrections. Doubt marking reduces but does not eliminate the possibility of unmarked errors. The marked passages should be checked against the original sheets or a better scan before being quoted as exact text.

## 4. Research notes — separate from the transcription

These notes concern only what is visible in this batch. “Conjecture” includes an explicit question, expectation, or proposed task, not necessarily a formally stated conjecture. “Unproved claim” means that a proof is absent or only invoked here; it does not mean that the claim is unproved elsewhere. Reading uncertainties are retained in the notes whenever they affect the mathematical interpretation. Cross-references use scan numbers, not the lower archive counters.

### R01. Scan 151, 1–10 — unproved claim

The proof invokes “le th. précédent” and “la section précédente” for a unique fixed point and its invariance when the acting subgroup is replaced by a smaller nontrivial subgroup. Those earlier hypotheses must be recovered before the maximality argument can be assessed; the corrected subgroup indices here are not a secure basis for reconstructing them.

### R02. Scan 151, 11–25 — unproved claim

The argument ends “D’autre part c) est clair.” The statement of c) is not present in this batch, so these pages do not support a reconstruction or verification of that assertion.

### R03. Scan 152, 1–11 — unproved claim

The text describes U through π with “structure à lacets” and proposes that an outer action also describes “l’objet (U, Γ)” in a category tentatively read as “isotopique.” Verification requires an exact specification of that category, the orientation data, and what equivalence of actions is intended; several words of this sentence remain uncertain.

### R04. Scan 152, left margin — conjecture

The marginal note begins “il faudrait revenir sur le cas général.” The surrounding main text restricts to orientation-preserving behavior, but the note’s last words are not secure; it records a return to the general case rather than supplying that treatment.

### R05. Scan 152, 13–23 — unproved claim

The construction identifies exceptional-point data with π-conjugacy classes of maximal nontrivial partial sections and invokes “π^{Γ′} = (1)” to obtain a π-torsor. A proof should make explicit the action by conjugation, its stabilizer, and the hypotheses that force that stabilizer to be trivial.

### R06. Scan 153, 1–7 — unproved claim

The maximal partial sections are said to form an E-set canonically identified with “Ũ|U! = Ũ!” and with free π-action. To verify canonicity, one would need the map from a lifted exceptional point to its stabilizer section, its independence from choices, and its equivariance.

### R07. Scan 153, 8–15 — conjecture

After setting “S′ = S ∪ U!” the text seeks to reconstruct the outer group with lacets associated with U′ and its outer Γ-action. This is a reconstruction problem stated here, not a construction completed on this page; the precise introductory verb remains uncertain.

### R08. Scan 153, 18–24 — conjecture

“Mais il faudrait d’abord s’assurer du caractère intrinsèque” explicitly leaves an intrinsicness check open. The required comparison is between data obtained from an extension and data depending only on the outer group π and the outer Γ-action.

### R09. Scan 154, 1–10 — conjecture

“On aimerait cependant aussi une description intrinsèque” introduces a topos-theoretic formulation of the exceptional-locus map. The proposed morphism is to carry Γ-action, but the subscripts and its name are overwritten; the precise target must be established before a categorical reconstruction is attempted.

### R10. Scan 154, 11–18 — unproved claim

The inverse-image functor is described as “le produit contracté sur π” with one of the maximal nontrivial partial sections. A proof would have to specify the relevant π-object and explain how the construction is independent, up to the intended equivalence, of the representative partial section.

### R11. Scan 154, diagrams — own idea

One possible check is to compare the functors obtained from two π-conjugate representatives of the same partial-section class and to track the resulting Γ-compatibility explicitly. This is a proposed consistency test, not a claim of canonicity or novelty.

Confidence: **medium**. Reason: The page itself links conjugacy classes, contracted products, and Γ-compatible inverse-image functors; the exact diagram labels are uncertain.

### R12. Scan 155, 7–13 — unproved claim

The page lists cyclic/dihedral behavior, finiteness of π-conjugacy classes, and containment of each nontrivial partial section in a unique maximal one. The corrected alternatives involving Γ′⁰ and the faithful-action insertion are part of the hypotheses to verify; this batch does not provide a full proof of all these assertions.

### R13. Scan 155, 14–16 — conjecture

The author qualifies the preceding result: “je pense que ça reste vrai tel quel, à vérifier…” after noting the established case Γ = Γ⁰. A check of the general case must include the orientation-reversing elements rather than silently extending the orientation-preserving argument.

### R14. Scan 155, 17–24 — unpursued implication

The underlined “structure supplémentaire” introduces μ on finite-order elements of E with values in T ⊗ ℚ/ℤ. This distinguishes the extension as a group from an extension supplied with local geometric data; whether the latter data are determined by the former becomes an explicit question on the next page.

### R15. Scan 155, lower-left NB — conjecture

The marginal NB singles out “u ∉ E⁰” and “d’ordre 2 exactement” while discussing the definition of μ(u). Its intervening words are not sufficiently legible to state a complete claim; the orientation-reversing case should therefore remain a separate verification item.

### R16. Scan 156, 1–9 — unproved claim

The finite-order element is assigned a local “multiplicateur,” described as a primitive root and then as an element of T ⊗ ℤ/nℤ. A proof should specify the local coordinate/orientation choices and their transformation law; these details matter for the assertion of an intrinsic target.

### R17. Scan 156, 10–14 — unproved claim

The “conditions évidentes” comprise π-conjugacy invariance, μ(uⁿ) = nμ(u), and equality of orders. The displayed first condition is restricted to α ∈ π, not to all of E; that restriction should be kept in any later use.

### R18. Scan 156, 15–23 — conjecture

“J’ignore si cette application μ … peut se définir intrinsèquement en termes de l’extension E” is the central open question on this page. The alternative proposed is two geometrically realized extensions with an isomorphism not compatible with their μ-functions; the construction of such an example is not supplied here.

### R19. Scan 156, 15–23 — own idea

A useful test would be to search, within one fixed geometrically realized extension, for an extension automorphism whose action on torsion elements fails to preserve μ. Such an automorphism could test the proposed intrinsicness without first constructing two different total groups; this is only a proposed route.

Confidence: **medium**. Reason: The manuscript itself formulates incompatibility with an isomorphism of extensions; specializing the source and target is a direct test of that formulation.

### R20. Scan 157, 1–7 — unproved claim

In the rank-one case the page concludes that E has no finite-order element other than the identity and that the question does not arise. The corrections involving Γ⁰ and faithful action must be resolved before treating this as a statement for every rank-one extension.

### R21. Scan 157, 8–19 — unproved claim

The displayed real-vector-space sequence is used with Hⁱ(Γ, π ⊗ℤ ℝ) = 0 for i > 0 to obtain H²(Γ, π) ← H¹(Γ, X₀(π)). A verification must recover the standing assumptions on Γ that justify the vanishing, and must identify the map and its sign convention rather than reversing the displayed arrow.

### R22. Scan 157, 20–26 — conjecture

The conditional “S’il était vrai … que tte opération” has “pour n = 2” inserted and continues onto the next scan. The proposed geometric reduction would identify the extension data with a torus torsor carrying Γ-action, but the claimed universality of standard torus actions is still conditional here.

### R23. Scan 157, 20–26 — own idea

A possible comparison is to hold the linear Γ-action on the lattice fixed while varying the torsor class appearing in H¹. Tracking fixed points and the μ-data in that comparison could separate dependence on the extension class from dependence on the local geometric realization.

Confidence: **medium**. Reason: The page explicitly introduces both the cohomological torsor class and the intrinsicness question for μ; no result of this comparison is asserted.

### R24. Scan 158, 1–4 — conjecture

The conditional from the previous scan concludes that standardness of the torus action would establish “le caractère intrinsèque de l’application μ dans ce cas.” These pages do not prove that every action under consideration is isomorphic to such a standard action.

### R25. Scan 158, 10–14 — conjecture

“La question revient à celle-ci” reduces the calculation to a split cyclic extension described by an automorphism θ with θⁿ = idπ, and asks for an element of T ⊗ ℚ/ℤ. Any solution must retain the generator and the orientation module as part of the input rather than identifying the target with ℚ/ℤ without a choice.

### R26. Scan 158, 15–20 — unproved claim

The proposed answer uses a standard torus with a fixed origin, separates orientation reversal, and lists rotation orders “2, 3, 4 ou 6.” The page does not prove this reduction or the completeness of the list; the phrase near the orientation-reversing order-two assertion remains uncertain.

### R27. Scan 158, 21–23 — unpursued implication

The local multiplier is identified with “une” of two eigenvalues after identifying the orientation module with ℤ. The continuation is needed to determine what selects one eigenvalue; the distinction should not be erased by treating the unordered pair as the multiplier itself.

### R28. Scan 159, 3–12 — unpursued implication

For an elliptic curve over an algebraically closed field Ω, the page distinguishes the profinite fundamental group with its u-action from choosing one of the two roots “dans Ω” of T² + aT + b = 0. Studying precisely how this choice is represented in the geometric category is a separate problem from recovering the characteristic polynomial.

### R29. Scan 159, 13–16 — unproved claim

“Il est clair que cette structure supplémentaire ne peut se déduire de la seule connaissance de l’action de u sur π” is asserted without a proof here. A verification should specify the permitted isomorphisms and exhibit the ambiguity they leave in the selected root; the adjacent orientation note is only partly legible.

### R30. Scan 159, 17–24 — conjecture

The text asks whether the multiplier can instead be recovered from the outer action on the group “avec 1 lacet.” The shift from the unpunctured group to this punctured-group datum is essential; no answer should be attributed to the unpunctured action merely from this question.

### R31. Scan 159, lower-left margin — unproved claim

A marginal response begins “oui, il le peut, grâce à la considération…” and sketches subgroup extensions. The subgroup description and parts of the diagram are unreadable, so the note records a proposed positive answer but does not support a complete reconstruction of its argument.

### R32. Scan 159, last lines, continuing on scan 160 — unpursued implication

“Cela impliquerait d’autre part que la construction…” begins a conditional consequence for reconstructing the group with a lacet and its action. The sentence continues on scan 160 and should be assessed as one conditional argument, not as an independent proved assertion.

### R33. Scan 160, 1–6 — conjecture

The carried-over argument leads to the problem of “forage de trous,” which the author says must finally be attacked. It concerns reconstruction together with the Γ-action, not merely the existence of a punctured surface or its abstract fundamental group.

### R34. Scan 160, 7–16 — conjecture

In the underlined “cas anabélien,” the text asks again whether μ is deducible from the action or is extra data required for geometric reconstruction, ending “la question reste entière.” The left marginal qualification is too incomplete to treat as a proof resolving that question.

### R35. Scan 160, 12–15 — conjecture

The bracketed passage asks whether μ might be definable on the entire indicated outer-automorphism group, once faithful action identifies E with a subgroup. The exact notation and scope of “entier” are uncertain; a rigorous formulation must first recover the group and domain intended.

### R36. Scan 160, left margin — unproved claim

The marginal note visibly mentions “Γ résoluble” and words tentatively read as “réaliser géométriquement.” Its intervening reasoning is not readable enough to attribute a precise realization theorem or restriction to the author.

### R37. Scan 160, section 16 and final NB — unproved claim

Section 16 opens with a morphism of multigaloisian topoi and a NB relating it to topological situations (X, S) or U, subject to excluding an S² component. The strength of the asserted correspondence is not secure because the key abbreviation is unclear, and the discussion continues beyond this batch.

### R38. Scan 160, section 16 — own idea

A source-based next step would be to compare the local subgroup extensions sketched in the preceding margin with the input morphism of topoi introduced here. This might clarify what data the forthcoming “bouchage” and “forage” constructions preserve, but the present pages do not supply the comparison.

Confidence: **low**. Reason: The juxtaposition suggests the connection, while the marginal subgroup labels and the final topos subscripts remain uncertain.

