# LM1_GROUP_SCHEMES: the group schemes M_{ρ,σ} over Z and the schematic envelopes of discrete groups (§§48–50)

DRAFT, provisional (11 November 2026). Development prompt for Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981). File prefix for your deliverables: `LM1_GROUP_SCHEMES`.

## What is to be settled

From §48 on (cote 140-3, folios 428–650; cote 140-4, folios 650–664) Grothendieck replaces the profinite calculation of §§38–47 by an algebraic one. Instead of solving the equation of loops in `SL(2, Ẑ)`, he constructs a group scheme over `Z` whose `Ẑ`-points contain the solutions, and studies it as a scheme: "Construction d'un schéma en groupes" (§48, twelve subsections), "Les groupes M_{ρ,σ} généraux" (§49, six subsections, about 100 folios), "Enveloppes schématiques de groupes discrets: cas métabélien" (§50). The objects: for a group scheme `G` (first `SL_2`, `GL_2`) with elements `ρ` of order 3 and `σ` of order 2 (the images of the standard generators of `SL(2, Z)`), the morphism `α ↦ αρ(α^{-1}) = [α, ρ]`; the equations `ζ = η ε_1(μ−1)` and `αρ(α)^{-1} = βσ(β)^{-1} ε_1(μ−1)`; the groups `B_0`, `B_{ρ,σ}`, `G_{ρ,σ}`, `G^*_{ρ,σ}`, `SG^*_{ρ,σ}`; a canonical "épinglage" attached to `ρ, σ`; the characterization of the "modular" triple `(ε, σ, ρ)`; the groups `M_{ρ,σ}`, `SM_{ρ,σ}` and their structure; the general `M_{ρ,σ}` "sans signes" and with the signs `ε_2, ε_3`; the passage from `M̃_{0,3}` to `Ñ_{1,1}` and from `GL(2, Ẑ)/{±1}` to `GL(2, Ẑ)`.

What he asks or marks (cote 140-3 scans unless noted):
1. The scheme of solutions and its relative dimension (151); uniqueness of the lifts (358) and its failure "sans quelques restrictions sur S" (323: sections `τ` with `2τ = 0`, `τ² = 0`); surjectivity of the parametrizations (370); smoothness of the parameter scheme away from residue characteristics 2 and 3 (140-4 scan 41).
2. "Il est plausible … vaudrait bien la peine de tirer cette question au clair" (336): group sheaves over `Spec Z` presented by finite cyclic maps and `G_a`, for `SL_2` and `GL_2` with the orders 4 and 6.
3. "une construction systématique de représentations motiviques" from geometric or discrete representations (489); adelic points of a group scheme over `Z` (546).
4. Central extensions by `μ_2`, their non-triviality, normality of complements (596–605); the Brauer class `c` as a cup product (610–611), "ne peut guère être que Z/4Z" (631); lifts with full image as "un exercice plaisant et délectable" of class field theory (634); the remark that `ρ, σ, τ` generate `G⁺` perhaps only modulo a finite group (652).
5. §50 (140-4 scans 1–41): is a fibrewise unipotent section given by a homomorphism `G_a → G` (6); the "lemme dubitatif" (10–16): does integrality of signed combinations of divided powers or exponentials force integrality in residue characteristics 2, 3, 5, "un contre-exemple … ou un théorème !", with the "Théorème (!)" of folio 652'; the schematic envelope of a metabelian group and its universal property (§50.3–5).

## Leads (unverified; prove or refute each)

- **Lead 1.** `SL(2, Z) = Z/4 *_{Z/2} Z/6` (Serre). Item 2 asks whether the analogous presentation holds for the group scheme, as an fppf sheaf of groups over `Spec Z`: is `SL_2` the amalgam, in group sheaves, of `μ_4`-type and `μ_6`-type finite flat subgroup schemes together with `G_a`. This should be decidable: true over `Z[1/6]`, with a definite correction at 2 and 3.
- **Lead 2.** `M_{ρ,σ}` is the scheme of pairs `(α, β)` solving a twisted-conjugacy equation; it is a torsor-like object over the product of the twisted centralizers of `ρ` and `σ` (the tori `T_ρ`, `T_σ`, which are norm-one tori of `Z[ζ_3]` and `Z[i]`, not tori over `Spec Z` in the strict sense, as he notes at scan 259). Its structure, dimension 6 in one normalization (scan 393), smoothness and fibres at 2 and 3 can be computed outright.
- **Lead 3.** The schematic envelope of §50 is the pro-algebraic (Hochschild–Mostow) or Malcev-type hull of a discrete metabelian group over `Z`, and its unipotent part is the integral form given by divided powers (Lazard; the Kostant `Z`-form). The "lemme dubitatif" is a statement about integer-valued polynomials and divided-power exponentials and can be settled by a direct computation at 2, 3, 5.
- **Lead 4.** Item 4: the `μ_2`-extensions are those of `SL_2` and of the metaplectic type over the adeles; the Brauer class should be the quaternion symbol attached to `(−1, −3)` or to the two quadratic characters `ε_2, ε_3`, which is the cup product he writes.

## Parts

**A. Definitions and dictionary.** All groups and schemes of §§48–49 with his symbols, scans and the corrected formulas (the second-pass corrections for C3-264-282 to C3-682-696 are attached and change many of them: `η = βσ(β)^{-1}`, the definition (13)–(14) of `M_{ρ,σ}` by `det f = det y = ε' det x`, the generators `ε_0, ε_1`, and so on). One table.

**B. The scheme `M_{ρ,σ}` for `SL_2`, `GL_2`.** Its functor of points, representability, equations, relative dimension, smoothness, fibres in characteristics 2 and 3, group structure, the épinglage, the subgroups `M(0)`, `M[0]`, `M(q)`, the exact sequences of §48.IX–XI and §49.V–VI, each stated and proved, with every slip of the manuscript corrected and named. Item 1 completely. Verify the key identities by computer algebra and attach the code.

**C. Presentations over `Z` (item 2, Lead 1).** State the question precisely in fppf group sheaves, and settle it for `SL_2`, `PGL_2`, `GL_2`.

**D. Points and extensions (items 3, 4).** `M_{ρ,σ}(Ẑ)`, `M_{ρ,σ}(A_f)`, `M_{ρ,σ}(Z)`; the comparison with the profinite groups of §§38–47 (which solutions of the profinite equation of loops are `Ẑ`-points, and what the scheme adds); the `μ_2`-extensions, the Brauer class, its order, the class-field-theory exercise carried out. Say what "représentations motiviques" should mean at scan 489 and prove what can be proved.

**E. §50.** Unipotent and quasi-unipotent sections; the "lemme dubitatif" decided (theorem or counterexample, with the computation); the "Théorème (!)" of folio 652' proved or corrected; the schematic envelope of a metabelian group constructed, its universal property proved, and compared with the existing notions of hull. Worked example: the envelope of `SL(2, Z)/[Π_0, Π_0]` used in §51 (his `𝔖`), which package LM7_FERMAT_TOWER needs.

---

THE TEXT YOU ARE GIVEN
- Grothendieck wrote *La Longue Marche à travers la théorie de Galois* by hand between January and June 1981. It was never prepared for print. What is attached is a transcription of the manuscript made by AI from scans (first pass: GPT-6 Astra, ChatGPT Pro mode; second pass, line by line against the scans: Claude, Anthropic), by package. The manuscript is in four archive files: cote 140-2 (folios 1–292, §§1–37), cote 140-3 (folios 293–650, §§38–49), cote 140-4 (folios 650bis–787, §§50–53) and cote 140-1 (a draft of 37 scans). `\scanpage{n}` marks the scan, `\mspage{n}` his folio number.
- Marks in the transcription: `\unsure{a|b}` a doubtful reading with its alternatives; `\illegible{n}` unread words; `\deleted{…}` struck by the author; `\inserted{…}` added by him; `\margin{…}` a marginal note. A reading is never final. Where your mathematics depends on a doubtful or unread place, say so at that place, work with each alternative that makes sense, and report which one the mathematics supports as evidence for the editors, with the scan number. Do not silently choose, and do not call any reading settled. The scans of the pages that matter are attached: look at them.
- His notation changes as he goes, sometimes within a section ("Notations définitives (?)", §46). Fix yours on the first page with a table giving, for each symbol you use, his symbol and the scan where he introduces it.
- He marks his own doubts ("un peu faux", "ultra-faux", "sauf erreur", "peut-être est-ce tout à fait faux ?", "Théorème (!)"). These are part of the text: a statement he doubts is treated as a question, one he withdraws as withdrawn.

WHAT IS ATTACHED
A zip with: the transcription packages listed in the manifest (the current text of each), the scans of the pages named in this prompt, his table of contents, the checked research notes of those packages (notes by the transcribing models on his conjectures, unproved claims and unpursued implications; drafts, not authority), the background papers, and `OVERVIEW.md` (a reading of the whole manuscript by Claude, from which the leads below come).

RULES OF PROOF (they bind every statement you deliver)
1. State the actual claim with all its data: which group (discrete, profinite, pro-ℓ), which field, which type `(g, ν)`, outer or genuine actions, base points and the choices they involve, which topology, which of his numbered conditions in which version. Do not replace it by a convenient special case; if you prove a special case, name it as one and keep the general statement on your list as open.
2. Type every map: source, target, the category in which it is a morphism, and each property you use (continuous, open, compatible with which outer action, defined up to which inner automorphisms).
3. Every reduction ("we may assume", "pass to an open subgroup", "fill the holes", "replace by a covering") comes with its comparison map and a proof that the exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: a homomorphism and its class modulo inner automorphisms; an isomorphism and a canonical isomorphism; injective, with open image, bijective; a discrete group and its profinite completion (and say when the completion map is injective); a statement over `Q` and over a finite extension.
5. Check the cases he sets aside or forgets: types `(0,0)`, `(0,1)`, `(0,2)`, `(1,0)`; `(0,3)` and `(1,1)` against the general anabelian type; residue characteristics 2 and 3; non-orientable and real cases; trivial and non-trivial centres.
6. A counterexample is given completely and, when finite or computable, checked by a program whose code and output you attach. One verified counterexample refutes the statement: say "false", and then find the strongest true statement in its place. An invalid proof alone shows a gap, not falsity.
7. No authority. His assertions, the notes of the transcribing models, and the leads marked "Lead" below (inferences by Claude from one reading, checked by no one) are all to be proved or refuted. If a lead is wrong, say so plainly.
8. Later work (Belyi, Drinfeld, Ihara, Nakamura, Matsumoto, Tamagawa, Mochizuki, Pop, Hoshi, Boggi and others) is to be used, with exact theorem numbers, wherever it proves or refutes what he asks. The task is to do the mathematics he set out, with everything now available, and to carry it to where it stops; it is not a survey. Never invent a reference; mark each bibliography entry `verified` (you opened it) or `unverified`. Before calling anything new, say what you searched.
9. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the smallest undecided instance.

WHAT TO DELIVER
One ZIP containing:
- `<ID>_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the parts, every statement numbered and labelled Proved / Refuted / Known (with citation) / Open, with complete proofs; each statement that answers a passage of the manuscript cites it by section, folio and scan. English, first person plural, the register of a careful research paper; quote Grothendieck in French where his wording matters, and never write in his voice. This text is meant for a book that reproduces his text and builds it out; how it will be placed there is not decided, so make it readable on its own.
- `<ID>_results.csv`: one row per numbered statement: `id, statement, status, where_proved, depends_on, manuscript_passages (section; folio; scan), depends_on_doubtful_reading (scan, alternatives), notes`.
- `<ID>_readings.csv`: every place where the mathematics bears on a doubtful reading: `package, scan, the \unsure or \illegible place, what the mathematics supports, how strongly`.
- `<ID>_references.bib`, `<ID>_report.md` (what you read, what you computed, corrections to the leads and to the notes, what remains open), and `code/`.
The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and claim no priority.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go.
