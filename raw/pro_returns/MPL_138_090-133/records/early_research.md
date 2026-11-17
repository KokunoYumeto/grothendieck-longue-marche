# Early arithmetic pages: bounded research pass

Run: `MPL_138_090-133`; author: GPT-6 Astra Pro, support agent `/root/mechanical_validator`; effort setting not separately exposed. Prepared after the transcription freeze of 2026-11-17 23:02:39 UTC.

## Scope, locators, and status discipline

This pass concerns frozen scans **90, 91, 93–96**, followed by the requested title/count audit of **97, 98, 106, 110, 113, 121, 133**. It reads the saved TeX and the supplied context, not the scan images. It changes no transcription, reading apparatus, or inventory. A local locator such as `096:18–22` means lines of `pages/MPL_138_090-133_138_scan096.tex`; it is not an estimate of manuscript lineation. The short source quotations below preserve the frozen wording, including uncertainty macros where relevant.

`context/README.md` and `context/notes/RESULTS_STATE.md` were read before the comparisons. The LM transcriptions advertise a second pass, whereas the supplied Esquisse transcription explicitly says it has not yet been checked by eye; neither is used to overwrite this packet. A status quoted from RESULTS_STATE remains that register's status and attribution, and no status is advanced by this report. No Hua modernization, scan, external article, or source from a different conversation was consulted.

Two notation cautions govern the comparison. On scan 90 the sphere has **ν+1** named peripheral generators, whereas the later LM type `(g,n)` uses the number of punctures itself; thus this page's **ν=2 corresponds to type (0,3)**. Moreover, `Γ_ν` on scan 90 is a quotient of an automorphism group; `Γ=Aut(Q̄)` on scan 94 is the field Galois group, and their equality is not supplied by the shared letter. The later LM also distinguishes orientation and permission to permute peripheral labels; a conceptual parallel below is not a literal identification before those conventions are matched.

### Context reference key

All paths in this table are relative to `context/`. The TeX line numbers are file-local, and the scan numbers come from the context's own `scanpage` markers.

| Key | Exact context file and locus | Material used |
|---|---|---|
| C1 | `LM_140-2_text.tex`, scans 71–72, end of §8 / start of §9, lines 2075–2104 | Peripheral maps from the Tate module as outer maps; conjugacy and tangential data. |
| C2 | `LM_140-2_text.tex`, scans 84–85, condition c), lines 2398–2437 | For every puncture, compatibility of `κ_i:T→π` with the same cyclotomic character, expressed up to inner conjugacy. |
| C3 | `LM_140-2_text.tex`, scans 89–92, topological comparison, lines 2580–2685 | Orientation module, exterior peripheral maps, product relation, and exceptions to injectivity. |
| C4 | `LM_140-2_text.tex`, scans 99–100, lines 2888–2947; scans 110–111, lines 3305–3357 | Outer actions, peripheral structure, and common sign/cyclotomic character. |
| C5 | `LM_140-2_text.tex`, scans 257–259, Teichmüller-space discussion, lines 8260–8325 | Low-puncture sphere cases and the distinction between spaces, groups, and rigidifications. |
| C6 | `LM_140-2_text.tex`, §26 “Groupes de Teichmüller profinis,” scans 318–320, lines 9473–9540 | Centrelessness assumption; extended loop automorphism group; discrete completion versus its image. |
| C7 | `LM_140-2_text.tex`, §26, scans 322–327, lines 9594–9775 | Retraction of a self-normalizer guess; normality question; normalizer of the geometric strict subgroup; arithmetic extension. |
| C8 | `LM_140-2_text.tex`, scans 368–370, lines 10946–10994 | Marking/discretification dependence; normalizers; caution about the full profinite group. |
| C9 | `LM_140-2_text.tex`, scans 331, 374–377, lines 9863–9883, 11121–11159 | Embeddings into C versus isomorphisms of algebraic closures; commutant as a torsor twist. |
| C10 | `LM_140-2_text.tex`, scans 540–541, equations (11)–(12), lines 15650–15665 | Primitive-root torsor and the maximal cyclotomic subextension. |
| C11 | `LM_140-4_text.tex`, scans 185–187, lines 9099–9144; scans 193–195, lines 9222–9255 | Finite-order presentation in an L-group example; a conditional finite-cover description of a one-dimensional multiplicity. |
| C12 | `LM_140-4_text.tex`, scan 96, equations (217)–(219), lines 5613–5644 | Cyclotomic character as one component of a richer arithmetic map; surjectivity is stated. |
| E1 | `Esquisse_cote119_copy1_API_transcription.tex`, §2, scan 119/6, typescript p.4, lines 218–248 | Tower action and the problem of recognizing the arithmetic image. |
| E2 | Same Esquisse file, §2, scan 119/7, typescript p.5, lines 263–294 | Genus-zero braid language and the need for a symmetry-compatible package of basepoints. |
| E3 | Same Esquisse file, scan 119/57, typescript p.55, note (5), lines 2531–2541 | Cyclotomic action on congruence maps; the preceding inertia sentence concerns inertia inside the field Galois group. |

The searches used the exact concepts and notation families `cyclotom`, `inertie`, `torseur`, `commutant`, `Teichm`, `tresses`, `Isom`, `μ_n^*`, and the completion/normalizer passages. These comparisons identify continuities and differences; they are not a full review of the cited LM claims.

## Research items

### ER01 — Sign map and oriented quotient

**Source:** 090:11–24; short quote: `B_\nu\xrightarrow{\chi_\nu^\circ}\mathbb Z^*=\{\pm1\}\quad\text{surjectif}`.  
**Kind:** unproved claim.  
**Context:** C3, C4; E2.  
**RESULTS_STATE:** EXIT_TOWER E.24 and LM1 D.7 are **Open (the return's claim)**; neither is a proof of this discrete identification.

The sign character, its surjectivity, and the interpretation of the quotient as the nonoriented sphere Teichmüller group are asserted here without a proof. The later LM supplies the common orientation module and compatibility with the sign character, while Esquisse retains the genus-zero braid description. This page therefore gives a concrete early peripheral presentation of that language; it does not identify its profinite enlargement with the arithmetic image.

### ER02 — Range needed for the inner-automorphism hook

**Source:** 090:18–20; short quote: `L_\nu\hookrightarrow\operatorname{Ker}(\chi_\nu^\circ)` with `g\longmapsto(\operatorname{int}(g),\operatorname{id}_{\mathbb Z})`.  
**Kind:** unproved claim / hypothesis issue.  
**Context:** C6, scan 318, equations (1)–(2).  
**RESULTS_STATE:** no register entry settles this local missing-hypothesis issue; LM4 D.32 is **Proved, refereed 14 Nov 2026 as claimed**, but concerns the three-cusp rank test and finite pure loop groups, not an unrestricted parameter range here.

Interpreting this hook literally requires control of the centre of `L_ν`; the fragment does not state a lower bound on ν before using it. The analogous LM sequence first assumes the anabelian case and explicitly admits centrelessness. The early page should consequently be cited with its intended puncture range still to be specified, rather than as a uniform faithful inner-action statement for every ν.

### ER03 — Pure sphere group, braid quotient, and the three-puncture case

**Source:** 090:24–30; short quotes: `On sait que $\mathcal T_2^\circ=1$` and `groupe des tresses sphériques coloriées`.  
**Kind:** unproved claim / reading issue.  
**Context:** C3, C5; E2.  
**RESULTS_STATE:** LM4 D.32 has the reviewed status stated in ER02, but its finite-subgroup assertion must not be substituted for equality of whole automorphism groups.

The assertion of triviality is about the discrete oriented object with three named punctures, using the parameter shift recorded above. The later LM discusses the low-puncture sphere spaces, and Esquisse describes genus-zero Teichmüller groups through braids, but neither quoted passage resolves the precise quotient intended by the uncertain `/\mathbb Z_2` here. Whether “trous” means marked punctures or boundary circles with a specified boundary convention must remain explicit before one cites an exact mapping-class/braid isomorphism.

### ER04 — Completion versus closure is an extra comparison

**Source:** 090:33–38; short quote: `\overline B_\nu/\widehat L_\nu=\widehat{\mathcal T}_\nu`.  
**Kind:** unproved claim.  
**Context:** C6, especially scan 320 immediately before equation (8).  
**RESULTS_STATE:** LM1 D.7 remains **Open (the return's claim)**; LM4_SUCCESSOR B.38 is **Open (the return's claim)** for particular congruence kernels, not a supplied proof of this comparison.

The display treats the relevant discrete completions as embedded in the profinite automorphism setting and identifies a closure quotient with a full profinite completion. The later LM distinguishes the completion from its image and says explicitly that injectivity is being admitted. This is therefore a comparison hypothesis to track separately from the definitions, without importing a conclusion about all congruence kernels.

### ER05 — Normality of the full completed discrete subgroup

**Source:** 090:44; short quote: `$\widehat{\mathcal T}_\nu$ invariant dans $\Gamma_\nu$?`.  
**Kind:** question.  
**Context:** C7, C8; E1.  
**RESULTS_STATE:** EXIT_TOWER E.24 and LM1 D.7 are **Open (the return's claim)**.

This is an explicit normality question about a geometric/discrete-origin subgroup inside an ambient profinite group, not a stated result. At LM scan 322 a margin rejects a self-normalizer guess and replaces it by the question whether the geometric subgroup is invariant; later passages introduce normalizers and smaller arithmetic subgroups. The early question is thus a direct precursor of that distinction, but supplies no answer to the register's arithmetic-image problem.

### ER06 — The oriented normality question is separately recorded

**Source:** 090:44; short quote: `$\widehat{\mathcal T}_\nu^\circ$ \unsure{dist. ds} $\Gamma_\nu^\circ$?`.  
**Kind:** question / reading issue.  
**Context:** C7, especially the normalizer of the geometric strict subgroup; C8.  
**RESULTS_STATE:** EXIT_TOWER E.24 is **Open (the return's claim)**.

The second question restricts to the oriented kernels, so it should not be collapsed into ER05. The later normalizer formulation is a close conceptual comparison, although the exact meaning of the abbreviated `dist. ds` remains a frozen reading uncertainty. No normality theorem is inferred merely from the compatible character diagram above it.

### ER07 — The author withdraws the equality at ν=2

**Source:** 090:46–48; short quote: `\inserted{c'est \uline{faux} pour $\nu=2$}`.  
**Kind:** question with the author's negative answer / self-retraction of a proposed equality.  
**Context:** C6–C8; E1–E2.  
**RESULTS_STATE:** LM4 D.12, EXIT_TOWER E.24, and LM1 D.7 are **Open (the return's claim)**; LM4 D.32 has the limited reviewed status recorded above.

The inserted sentence directly qualifies the immediately preceding equality `\widehat{\mathcal T}_\nu^\circ=\Gamma_\nu^\circ`; it is not a construction of a group-theoretic retraction. Read alongside `\mathcal T_2^\circ=1`, it records that the full profinite oriented object was already being distinguished from the completed discrete one in the three-puncture case. The page gives no witness or proof of the negative answer, and its ambient group must not silently become GT, GT₀, or the Galois image.

### ER08 — Weighted peripheral presentation and the infinity convention

**Source:** 091:3–7; short quotes: `\inserted{$[1,\infty]$}` and `\lambda_0^{\varepsilon_0}=\lambda_1^{\varepsilon_1}=\cdots=\lambda_\nu^{\varepsilon_\nu}=1`.  
**Kind:** implication not pursued / reading-convention issue.  
**Context:** C11, finite-order presentation at scans 186–187 and conditional multiplicity discussion at scans 193–195.  
**RESULTS_STATE:** LM4_SUCCESSOR B.12 is **Open (the return's claim)** and explicitly has the corrected weighted-orbifold target `Out_∂(C₃ ⨿ C₃)`.

The variant adds finite orders to the same named peripheral presentation and is naturally compared with weighted/orbifold peripheral data. The printed formula does not say how an exponent ∞ is to be interpreted; omission of the corresponding power relation is a convention to investigate, not a correction licensed by the ink. Later LM distinguishes L-group examples and makes a finite-cover description of multiplicities conditional, so this short presentation proves neither geometric uniformization nor that every weight system has a faithful finite surface cover.

### ER09 — Commutants and twisting the entire torsor system

**Source:** 093:4–8,20–25 and 094:17–20; short quotes: `\unsure{\text{commutants}|\text{commutatifs}}` and `commutant de $\pi$ ds $T_i$`.  
**Kind:** unproved construction / reading question.  
**Context:** C9, scan 374, equation (27) and the preceding commutant sentence.  
**RESULTS_STATE:** LM6 F.35 is **Proved (the return's claim)** for actual forgetful maps and identifications; that return has not been rechecked here.

The two-column scheme transports the group, torsors, commutant groups, and inertia subgroups together by the same right Γ-torsor. The explicit definition on scan 94 supports “commutants” as a contextual candidate for scan 93, and the later LM again describes a commutant as a group twisted by a torsor. This is evidence for a reading question, not permission to replace the frozen alternative or a proof of every displayed contracted-product identification.

### ER10 — The inverse-twist expression needs its actions specified

**Source:** 093:27; short quote: `I_i=\unsure{\check C\wedge_\Gamma\widetilde I_i\wedge_\Gamma C}`.  
**Kind:** reading question / uncompleted construction.  
**Context:** C9, scan 374, and C1's exterior-map formulation.  
**RESULTS_STATE:** no directly settling entry; LM6 F.35 remains background with its **Proved (the return's claim)** status.

The forward twist is explicitly written on lines 23–25, whereas the proposed inverse has two torsor factors and unspelled actions. The later commutant formulation makes transport by a torsor intelligible but does not resolve these exact factors or their order. A careful reconstruction would first state the left/right and opposite-torsor conventions; this report leaves that reconstruction open.

### ER11 — Isomorphisms of algebraic closures versus embeddings into C

**Source:** 094:3–4; short quote: `\inserted{$(=\operatorname{Isom}(\overline{\mathbb Q},\unsure{\mathbb C}))$}`.  
**Kind:** reading question.  
**Context:** C9, scans 331 and 377.  
**RESULTS_STATE:** EXIT_TOWER E.24 is **Open (the return's claim)**; no status entry resolves the target glyph or the meaning of `Isom`.

Later LM explicitly distinguishes an isomorphism with a fixed algebraic closure inside C from a field embedding into C. That comparison provides a concrete reason to revisit the uncertain codomain or a possible abbreviated meaning of `Isom`, while retaining the current first reading. It supplies no authority to replace C by a chosen algebraic subfield in the transcription.

### ER12 — A literal Γ-action uses more marking data than an outer action

**Source:** 094:6–14 and 096:4–10; short quotes: `$\Gamma$-groupe` and `\text{pas compatible}\\\text{avec }\Gamma`.  
**Kind:** unproved construction / marking issue.  
**Context:** C1, C4; E2, especially lines 284–293.  
**RESULTS_STATE:** LM6 F.35 is **Proved (the return's claim)**; EXIT_TOWER E.24 is **Open (the return's claim)**.

The early notation uses actual group actions and maps between chosen fibre-functor torsors, then explicitly acknowledges that the comparison α is not Γ-compatible. Later LM places the intrinsic datum at the level of exterior groups and peripheral maps, while Esquisse emphasizes symmetry-compatible families of basepoints. This page records a concrete choice-dependent calculation whose passage to a canonical outer or groupoid statement still requires its marking conventions to be stated.

### ER13 — Common cyclotomic inertia and the puncture hypotheses

**Source:** 093:30–32, 094:23–28, and 095:31; short quotes: `\varprojlim_n\mu_n(\overline{\mathbb Q})` and `\text{indépendant de $i$}`.  
**Kind:** unproved claim.  
**Context:** C1–C4; C12; E3.  
**RESULTS_STATE:** LM6 B.27 is **Open (the return's claim)**; WG H1 is an **unchecked war-game hunch**. Neither centralizer problem is settled by identifying this character.

The intended source of a common character is the Γ-equivariant identification of the puncture groups with one Tate module, not merely the fact that each abstract group is procyclic. LM condition c) says this explicitly for every peripheral map, so the early page restates that mechanism in torsor notation. The hook into the geometric fundamental group also needs the puncture-range hypotheses that later LM discusses, and the inertia of the field Galois group mentioned before Esquisse note (5) must not be confused with these geometric puncture groups.

### ER14 — “Independent of i” versus “independent of ν”

**Source:** 093:32; short quote: `\uline{\unsure{Indép. de $i$|Indép. de $\nu$}}`.  
**Kind:** reading question.  
**Context:** C2 and C4, especially LM scan 111.  
**RESULTS_STATE:** no register result settles the glyph; LM6 B.27 remains **Open (the return's claim)**.

The unambiguous phrase “indépendant de i” on scan 95 and the later common-Tate-module formulation make the puncture-index reading a strong contextual candidate. The alternative ν-reading would ask for comparison across different puncture configurations, for which these lines do not specify the necessary transition data. The uncertainty is retained; contextual agreement is not visual verification.

### ER15 — The product-one relation still carries simultaneous marking data

**Source:** 095:9–24; short quotes: `\gamma_\pi^{-1}(l_1^\gamma),\ldots,\gamma_\pi^{-1}(l_n^\gamma)` and `l_1l_2\cdots l_n=1`.  
**Kind:** implication not pursued / incomplete argument.  
**Context:** C3, scan 91's choice of an order and conjugates; C2's exterior compatibility.  
**RESULTS_STATE:** LM1 D.7 is **Open (the return's claim)**.

The juxtaposed formulas suggest comparing Galois transport with a peripheral system satisfying the sphere relation, but the fragment contains no completed argument connecting every displayed tuple to that relation. The later LM explicitly chooses an ordering and conjugates of the peripheral images before writing its defining relation. One should therefore retain those simultaneous choices when reconstructing the argument, rather than infer a product identity for arbitrarily chosen individual representatives or powers.

### ER16 — Domain of χ and the σ/γ variables

**Source:** 095:28–37; short quotes: `\unsure{\pi|\Gamma}\xrightarrow{\chi}\widehat{\mathbb Z}^{*}` and `\chi(\unsure{\sigma|\gamma})`.  
**Kind:** reading question.  
**Context:** C2, C4, C12.  
**RESULTS_STATE:** EXIT_TOWER E.24 and LM1 D.7 are **Open (the return's claim)**.

The surrounding right-Γ-torsor law and the later LM character `χ:Γ→Ẑ*` point toward Γ and the same acting variable as natural contextual candidates. The frozen alternatives nevertheless distinguish a possible change of notation from a possible reading problem. Using the expected cyclotomic formula to normalize those symbols would conceal that unresolved issue.

### ER17 — Bounded check: the cancellation gives independence of φ for fixed i

**Source:** 096:7–22, with Γ-stability of `I_i` stated at 093:8; short quote from 096:19: `=\alpha'_i(\varphi)\gamma_{\pi_i}.`.  
**Kind:** targeted proof check of a conditional implication.  
**Context:** C1–C2 and E2 supply the comparison with exterior peripheral maps and basepoint packages, not hypotheses beyond the frozen formulas.  
**RESULTS_STATE:** no existing register claim is reproved or advanced; LM6 F.35 remains background, **Proved (the return's claim)**.  
**Confidence:** high for this conditional calculation, because it uses only substitution, cancellation, stability of a subgroup, and transitivity of a torsor; it is not a confidence rating for the handwritten glyph.

Substituting the displayed laws for α and β gives `α′_i(φγ)=β(φ)γ_πγ_π^{-1}α_i(φ)γ_{π_i}=α′_i(φ)γ_{π_i}`, exactly as written. Since `γ_{π_i}(I_i)=I_i`, its image in the fixed target is unchanged, and transitivity of the right Γ-torsor makes this image independent of φ for fixed i. No step compares two different puncture indices, so the calculation supports the φ alternative in `\unsure{i|\varphi}` conditionally and leaves the source reading unchanged. It proves neither the geometric existence of the input data nor equality of the subgroups belonging to distinct punctures.

### ER18 — The π/Γ subscript and the common kernel require a declared action

**Source:** 096:24–29; short quotes: `\widetilde I_i=C\wedge_\pi I_i` and `(indépendt de $i$)`.  
**Kind:** reading question / unproved claim.  
**Context:** C2, C4, C9; compare the earlier `C\wedge_\Gamma I_i` at 093:25.  
**RESULTS_STATE:** LM6 B.27 is **Open (the return's claim)**; no assertion about its cyclotomic centralizers is established here.

This paragraph changes the contracted-product subscript from Γ to π and introduces a quotient by a kernel without explicitly declaring a new right π-action on C. If the intended operator is the same arithmetic group and the action on every `I_i` is through the same χ, a common kernel is the natural comparison, but that conditional reconstruction does not resolve the symbols. The current text should be flagged as a possible change of notation or an omitted action, not silently rewritten to the later standard convention.

### ER19 — Identifying the quotient with all of Aut(I_i) needs surjectivity

**Source:** 096:27,32; short quote: `\pi'\simeq\operatorname{Aut}(I_i)\simeq\widehat{\mathbb Z}^{*}`.  
**Kind:** unproved claim.  
**Context:** C12, scan 96, where cyclotomic surjectivity is explicitly stated; C4.  
**RESULTS_STATE:** LM1 D.7 and EXIT_TOWER E.24 are **Open (the return's claim)** for richer image questions.

Quotienting an acting group by its action kernel identifies the quotient with the image of that action; reaching the whole displayed automorphism group is an additional surjectivity statement. Later LM states cyclotomic surjectivity in an arithmetic setting, but the acting group in this early paragraph is still affected by the π/Γ issue of ER18. Even under the intended arithmetic interpretation, surjectivity of this single character must not be promoted to surjectivity of the full arithmetic representation.

### ER20 — Primitive roots suggest a quotient of the comparison torsor

**Source:** 096:35, compared with 093:4 and 094:3–4; short quote: `C\simeq\varprojlim\mu_n(\overline{\mathbb Q})^{*}`.  
**Kind:** own interpretive idea / reading question.  
**Context:** C9, scan 377; C10, scans 540–541; E3.  
**RESULTS_STATE:** LM6 B.27 and EXIT_TOWER E.24 are **Open (the return's claim)**; this observation supplies no section or arithmetic-image result.  
**Confidence:** medium as a proposed reconstruction, because the preceding paragraph introduces an action kernel and quotient but never explicitly replaces C by its quotient.

The earlier C is a torsor under the full field automorphism group, whereas the later LM identifies the primitive-root object with a torsor for cyclotomic units and locates its inverse limit over the maximal cyclotomic subextension. A plausible reconstruction to investigate is that the final line concerns the induced cyclotomic torsor, or the quotient of the earlier C by the kernel of χ, rather than the original full comparison torsor. This would explain the adjacent quotient discussion, but the missing quotient or change of notation remains an editorial hypothesis and has not been inserted into the source.

## Standing title, date, and count audit

This is a text-evidence audit of the frozen fragments, not a material examination of the sheets. The archive foliation is expressly marked as such in each page's TeX comment and is not promoted to an authorial manuscript page number. The comparison source for catalog placement is `context/README.md`, “This package in our plan,” and `context/notes/RESULTS_STATE.md`, “Orientation for this package” (a curated, unrefereed lead); neither is a mathematical result ID.

| Audit ID | Scan / exact local TeX locus | Frozen title or other evidence | Count/date classification and standing conclusion |
|---|---|---|---|
| TA01 | 097:2–5 | Archive foliation **96**; `\unsure{précartes} et cartes \unsure{tot$^t$\|de $h^+$}` with uncertain “épinglées,” “par/pour,” then `précartes\ldots`. | A possible section/cover heading with unresolved words. No total page count or date is stated; do not manufacture a full title from scan 98. |
| TA02 | 098:2–6 | Archive foliation **97**; `Cartes \inserted{\uline{totalement}} épinglées. etc.`; an editorial comment says the faint upper-right mark resembles 1 but is not secure. | “I)” begins a definition, not a page count. The faint mark is not an authenticated manuscript page 1. The inserted word “totalement” is part of the recorded title state. |
| TA03 | 113:2–3 | Archive foliation **112**; `Cartes sphériques en bas degrés`. | A mathematical section heading, with no explicit date or extent. “Bas degrés” is mathematical content, not a number of sheets. |
| TA04 | 121:2–3 | Archive foliation **120**; `“Opérations” sphériques / sur les cartes / (axiomatique provisoire)` (line breaks encoded by `\\`). | A heading explicitly marked provisional. No page count, date, or assertion that the later axioms are finalized is supplied. |
| TA05 | 106:2–8 | Archive foliation **105**; `Montpellier \unsure{le\|be} 11.1.1977`; cancelled letter beginning “Monsieur le Ministre” and recommending Kwang Taek Jeong. | The date belongs to the letter layer recorded as cancelled. It is not automatically the composition date of the mathematical calculations or of the entire cote; no page count is given. |
| TA06 | 110:2,11,13,15–22,28,30 | Archive foliation **109**; notice **N°7119**, dated **12 Décembre 1977**; thesis notice for Michel Combe, title *Ressources en Eau du Maroc avec application à la méthodologie de la représentation des systèmes aquifères et de leur fonctionnement.*; defence **21 DECEMBRE 1977, 15h30**, room **6**. | “Trois volumes,” “Un quatrième volume,” **1200 pages**, **508 figures**, **46 bassins**, series **n°231**, **1967–1977**, scale **1/1.000.000**, and **15 ans** all describe the thesis or its research, not this mathematical manuscript's extent. The frozen record's reuse may motivate a local dating investigation, but this text-only pass does not establish the physical order of writing. |
| TA07 | 133:2,10–20,23,25,28–29 | Archive foliation **132**; film title `LE RECIF DE CORAIL`; originally announced for **14 décembre 1977**, rescheduled to **21 DECEMBRE 1977**, **11 heures**, amphitheatre **5**; J. COUDRAY; addressee Grothendieck, Mathématiques **5**. | **65 minutes** is film duration, not pages; the terminal **5** is recorded in the address/routing area, not authenticated as manuscript pagination. This notice supplies administrative dates and no mathematical title or page total. |

The packet has 43 supplied page fragments, numbered 90, 91, 93–133: an inclusive range label alone must not be converted into 44 surviving sheets, because scan 92 is absent from the specified set. This modern deliverable count is distinct from every historical number in TA01–TA07. The local dates are compatible with the context's approximate “vers 1976–1978” catalog placement, but do not establish a single composition date, date each mathematical layer, or prove a chronological priority claim.

## Check-event accounting

`records/early_check_events.tsv` records **one targeted proof check**, ER17, with its exact conditional scope. The searches, historical comparisons, status-register readings, and title/count classification are not logged as proof checks. No independent re-proof of an LM or RESULTS_STATE claim, external-literature verification, or mathematical certification of the remaining fragment claims was performed.
