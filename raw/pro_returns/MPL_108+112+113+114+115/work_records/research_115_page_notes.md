# Cote 115: page-specific research notes and crossing-kernel comparison

Research-only notes on the frozen `deliverable/MPL_108+112+113+114+115_transcription.tex`; no image was read or transcription changed in producing these notes. Each numbered note has a one-to-four-sentence analysis, an exact kind field, a precise scan locator, a brief verbatim TeX cue checked by exact substring matching, a separately labelled analytical anchor that may use modernized notation, and supplied-context references. Mathematical counterexamples and proposed reconstructions are expressly marked as our own elementary checks; their confidence is conditional on the indicated literal interpretation and is not a claim of novelty.

The context README and full RESULTS_STATE were read before drafting, and Hua’s README before using his modernised reading. **Hua, modernised reading of cote115**, and his four named findings remain credited interpretations; his prose is never used to resolve frozen uncertainties. In particular his reflexivity finding attaches “sans doute pas” to the wrong question in this frozen layout, and his modernised Noyaux subsection repeats the unrestricted external-product full-faithfulness assertion.

All BISITE/STRATA/GALOIS statuses referenced here retain their source status: the selected dossier says its returns have not had full-effort review. The exact STRATA C.1 statement is not supplied, as detailed after the page notes. Kind labels classify the manuscript item or comparison, not the status of an explanatory counterexample in its body; cancelled blocks are marked “withdrawn in the same text”, and the unfinished additive line is a “reading question”. All 52 literal cues passed exact substring validation against the cited frozen page fragments; the detailed checks are in `research_115_page_notes.literal_quote_validation.json`.

## 115-R01 — 115 scan002 — title / scope

**Kind:** `reading question`.

**Literal cue (verbatim frozen TeX; cote 115, scan 002):**

```tex
``Correspondances'' fonctorielles
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan002.tex`.

**Analytical anchor (may use modernized notation):** “Correspondances” fonctorielles; Dualité des topos

The title frames a program of functorial correspondences and topos duality; the concrete material subsequently supplied is chiefly ordinary Set-valued presheaf kernels, Kan adjunctions, conjugacy and completion sketches. It does not by itself announce a stable six-functor theorem or a duality of arbitrary topoi with fixed coefficients.

**Context searched:** context/notes/RESULTS_STATE.md: MPL_105 — BISITE F.10 (unpursued lead); context/hua_project/115.modern.tex: Résumé.

## 115-R02 — 115 scan003 — explicit question / variance

**Kind:** `conjecture`.

**Literal cue (verbatim frozen TeX; cote 115, scan 003):**

```tex
\overset{?}{\simeq}
H_B\bigl(\Psi_*,f^\circ_!(\Phi^*)\bigr)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan003.tex`.

**Analytical anchor (may use modernized notation):** H_A(f*Ψ_*,Φ*) ≃? H_B(Ψ_*,fᵒ_!Φ*)

This first questioned display is not established on the page and must be distinguished from the coend pairing formulas on scan010. If H_A is read as the contravariant Hom-kernel pairing later defined on scan008, the formula fails already for f:e→[1] selecting 0, Ψ_*=y₁ and Φ*=1: its left side is a singleton and its right side is empty; the possible superscript on H_A in the frozen text keeps the intended reading open. This is an own conditional check of the literal Hom-kernel interpretation, with high confidence in the calculation and medium confidence in its applicability to the unsettled notation.

**Context searched:** context/hua_project/115.modern.tex: La dualité; context/notes/RESULTS_STATE.md: BISITE F.18 (related derived boundary; no exact question entry).

**Confidence:** High for the elementary calculation; medium for intended notation.

## 115-R03 — 115 scan003 — explicit question / adjunction direction

**Kind:** `conjecture`.

**Literal cue (verbatim frozen TeX; cote 115, scan 003):**

```tex
\overset{?}{\simeq}\operatorname{Hom}_{\widehat A}(\unsure{f^*b},a)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan003.tex`.

**Analytical anchor (may use modernized notation):** Hom_B(b,f(a)) = Hom_Bhat(b,f_!(a)) ≃? Hom_Ahat(f*b,a)

The first equality is the representable left-Kan extension formula, but the final questioned equality reverses the arguments needed for f_!⊣f*. For f:e→[1] selecting 0 and b=1, Hom_B(1,0) is empty while Hom_Set(f*y₁,1)=Hom_Set(1,1) is a singleton, so the literal final comparison is false. The valid ordinary adjunction instead reads Hom_Bhat(f_!F,G)≃Hom_Ahat(F,f*G); this is an own explanatory comparison, not a proposed emendation.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; La dualité; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE A.23–A.24,F.1,F.7.

**Confidence:** High: explicit finite-category computation.

## 115-R04 — 115 scan003 — unproved density calculation

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 003):**

```tex
f^*(b)=\varinjlim_{a'\text{ ds }A/b}a'^{\unsure{\circ}}
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan003.tex`.

**Analytical anchor (may use modernized notation):** f*(b)=varinjlim_{a′ ds A/b} a′^{…}

The expression resembles the ordinary presentation of a restricted representable as the colimit of representables indexed by its category of elements, followed by a limit formula for maps out of that colimit. The doubtful opposition on a′ and the ensuing Hom_A(a′,a) line prevent importing an unqualified identity with Hom_B(b,f(a)); even a correct density formula cannot reverse the adjunction from the preceding note. This is a reading-level comparison, with the frozen superscripts retained.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE E.3 (stronger enhanced recognition).

## 115-R05 — 115 scan003 — cancelled draft

**Kind:** `withdrawn in the same text`.

**Literal cue (verbatim frozen TeX; cote 115, scan 003):**

```tex
\deleted{\widehat B^\circ\unsure{\longrightarrow|{-}}\widehat A}
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan003.tex`.

**Analytical anchor (may use modernized notation):** Crossed-out four variance pairs and cancelled wheel

The cancelled arrays already organize the two choices Âᵒ/A∨ and B̂ᵒ/B∨, but their question marks, mixed ! indices and missing endings make them exploratory rather than a second independent theorem. They anticipate the more explicit wheel of scan006 without licensing repairs to either frozen diagram. Credit Hua’s wheel lead for the comparison, while using scan006 for the affirmative statement.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; context/notes/RESULTS_STATE.md: Hua 115-wheel-eleven-curryings.

## 115-R06 — 115 scan004 — ordinary definitions / claimed equivalences

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 004):**

```tex
formée des foncteurs commutant aux $\varinjlim$.
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan004.tex`.

**Analytical anchor (may use modernized notation):** Hom_! “commutant aux varinjlim”; Hom^! “commutant aux varprojlim”

The definitions fix the variance of the displayed categories: a kernel X∈PSh(A×B) is a functor Aᵒᵖ×Bᵒᵖ→Set, and the bare curryings are immediate ordinary equivalences. Extending along the indicated Yoneda embeddings gives the continuous or cocontinuous presentations, with preservation understood separately in each argument and in the chosen size universe. This is the substantive ordinary kernel formalism credited to Hua’s modernised reading; no weak-equivalence localization is imposed here.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; context/notes/RESULTS_STATE.md: Hua 115-wheel-eleven-curryings; MPL_105 — BISITE F.10.

## 115-R07 — 115 scan004 — ordinary internal-Hom identities

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 004):**

```tex
\underline{\operatorname{Hom}}_A(X,Y)&\overset{\mathrm{def}}=p_{B*}\underline{\operatorname{Hom}}_{A\times B}(X,Y)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan004.tex`.

**Analytical anchor (may use modernized notation):** Hom_A(X,Y)=p_{B*}Hom_{A×B}(X,Y)

The projection subscripts mean the forgotten factor: p_B:A×B→A and p_A:A×B→B, so the displayed relative internal-Hom objects have the asserted target presheaf categories. Applying global sections recovers ordinary Hom sets by the usual restriction/right-Kan adjunction. This is a direct formal precursor of BISITE F.7, but supplies no derived exchange map or arbitrary cartesian-square theorem.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE F.7.

## 115-R08 — 115 scan004 — kernel transforms / local notation conflict

**Kind:** `reading question`.

**Literal cue (verbatim frozen TeX; cote 115, scan 004):**

```tex
savoir $b\longmapsto{}^dX(b)=\underline{\operatorname{Hom}}_B(p_B^*(L),X)$
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan004.tex`.

**Analytical anchor (may use modernized notation):** X(L,M)=Hom(L⊠M,X)≃Hom(L,ᵈX(M))≃Hom(M,ˢX(L))

The two partial transforms and the common pairing are ordinary tensor–Hom adjunctions and explain the practical role of the kernel. In the prose curry b↦ᵈX(b), the parenthetical formula instead uses Hom_B(p_B*L,X), which elsewhere defines the other transform and leaves L unrelated to b; that local conflict must be recorded rather than repaired from the preceding formulas. Hua’s modernised account supports the intended two-transform construction but is not authority to replace the frozen line.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; context/notes/RESULTS_STATE.md: Hua 115-isbell-duality-derived-from-kernels.

## 115-R09 — 115 scan004 — canonical specialization

**Kind:** `unpursued implication`.

**Literal cue (verbatim frozen TeX; cote 115, scan 004):**

```tex
Cas $B=A^\circ$, d'où élément canonique
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan004.tex`.

**Analytical anchor (may use modernized notation):** “Cas B=Aᵒ … H=H_A”

The margin explicitly specializes the general kernel to the Hom bimodule with B=Aᵒ, which is the mathematical basis for the conjugate presheaf/copresheaf transforms developed on scan008. This directly supports Hua’s finding 115-isbell-duality-derived-from-kernels as an observation about the order of the construction. The folder does not name Isbell, and “derived from kernels” in that finding means obtained from the kernel construction, not derived-category functors.

**Context searched:** context/hua_project/115.modern.tex: La dualité; context/notes/RESULTS_STATE.md: Hua 115-isbell-duality-derived-from-kernels.

## 115-R10 — 115 scan004 — unproved assertion / own counterexample

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 004):**

```tex
est pleinement fidèle,
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan004.tex`.

**Analytical anchor (may use modernized notation):** (L,M)↦L⊠M “est pleinement fidèle”

As written for arbitrary presheaves this is false: for A=B=e it is the Cartesian product Set×Set→Set. It is not faithful because the distinct maps (id_∅,g):(∅,1)→(∅,{0,1}) have the same empty product map, and it is not full because the coordinate swap {0,1}²→{0,1}² is not f×g for separate one-variable functions. This own elementary check has high confidence and flags the assertion without changing it; Hua’s modernised “Noyaux” subsection repeats full faithfulness rather than repairing it.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux (same full-faithfulness assertion); context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE F.4–F.5 (different projection-formula scope).

**Confidence:** High: explicit finite sets and morphisms.

## 115-R11 — 115 scan004 — unproved Yoneda factorization

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 004):**

```tex
le composé est le foncteur canonique dit ``de Yoneda'' pour
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan004.tex`.

**Analytical anchor (may use modernized notation):** “le composé est le foncteur canonique dit ‘de Yoneda’”

The proposed identification with Yoneda cannot be used to prove the preceding full-faithfulness claim. For A=B=e, the product-category representable at (L,M) is (S,T)↦Hom(S,L)×Hom(T,M), which need not preserve limits on Setᵒᵖ separately: at S=∅ it gives Hom(T,M), although preserving the terminal object of Setᵒᵖ would require a singleton. Thus even the indicated factorization through the separately continuous subcategory fails without additional restrictions; this is an own direct check, not a restoration of an omitted hypothesis.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; context/notes/RESULTS_STATE.md: Hua 115-wheel-eleven-curryings.

**Confidence:** High: terminal-object preservation test.

## 115-R12 — 115 scan004 — unproved Hom factorization with doubtful superscripts

**Kind:** `reading question`.

**Literal cue (verbatim frozen TeX; cote 115, scan 004):**

```tex
\xleftarrow{\sim}
\operatorname{Hom}_{\widehat A}
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan004.tex`.

**Analytical anchor (may use modernized notation):** Hom(L′^{…}⊠M′^{…},L^{…}⊠M^{…}) ←~ Hom(L′^{…},L^{…})×Hom(M′^{…},M^{…})

The same product-map obstruction applies to the unqualified Hom factorization, and to a componentwise internal-Hom factorization if the symbols mean arbitrary objects of the two presheaf categories. However the frozen ξ/sharp superscripts are doubtful, so a possible intended restriction cannot be excluded or silently supplied. The safe research conclusion is a conditional mathematical objection to the unrestricted reading and a retained reading question about the special notation.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE F.7 (different derived exchange claim).

**Confidence:** High for unrestricted reading; intended restricted notation unresolved.

## 115-R13 — 115 scan004 — unproved exponent independence / own counterexample

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 004):**

```tex
on trouve donc $(p_B^*L)^M\simeq p_B^*L$
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan004.tex`.

**Analytical anchor (may use modernized notation):** “on trouve donc (p_B*L)^M≃p_B*L”

With A=B=e and L=M={0,1}, the displayed internal Hom has four elements whereas p_B*L has two, so the literal unrestricted conclusion fails. The preceding specialization Hom(p_A*M,p_B*L)←~p_B*L is the constant-function map and is likewise not generally an isomorphism. This is an own high-confidence cardinality check; the surrounding doubtful superscripts leave the intended scope unsettled and the frozen formula unchanged.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE F.5–F.7 (scope comparison only).

**Confidence:** High: 4 versus 2 elements.

## 115-R14 — 115 scan006 — affirmative wheel statement

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 006):**

```tex
Toutes les flèches du diagramme sont des équivalences de catégories
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan006.tex`.

**Analytical anchor (may use modernized notation):** “Toutes les flèches du diagramme sont des équivalences de catégories”

The page explicitly claims the wheel of ordinary kernel presentations, with six one-variable and four two-variable choices plus the central kernel category. Hua’s finding correctly counts eleven distinct presentations, while the frozen diagram has thirteen drawn occurrences because the two bare currying categories each occur twice. This is not a diagram of eleven higher or derived categories, and the mathematical claim requires the separately limit/colimit-preserving meanings fixed on scan004.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; context/notes/RESULTS_STATE.md: Hua 115-wheel-eleven-curryings.

## 115-R15 — 115 scan006 — finite multivariable claim / explicit precaution

**Kind:** `self-flagged`.

**Literal cue (verbatim frozen TeX; cote 115, scan 006):**

```tex
Je suppose $I,J$ finis pour ``play safe''.
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan006.tex`.

**Analytical anchor (may use modernized notation):** “Je suppose I,J finis pour ‘play safe’.”

The partition I=⨿I_j and sign partition J=J⁺⨿J⁻ extend the ordinary currying scheme to blocks of arguments, with preservation imposed separately in the chosen blocks. The explicit finiteness precaution and inconsistent I_{j⁺}/I_{j⁻} indexing remain part of the evidence; the page does not justify an infinite-variable extension. Nothing here supplies the coherent homotopy-colimit or multiderivator enhancement required by BISITE F.13/F.18.

**Context searched:** context/hua_project/115.modern.tex: Noyaux entre topos de préfaisceaux; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE F.13; context/notes/RESULTS_STATE.md: BISITE F.18.

## 115-R16 — 115 scan008 — ordinary contravariant adjunction

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 008):**

```tex
paires de foncteurs adjoints
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan008.tex`.

**Analytical anchor (may use modernized notation):** “paires de foncteurs adjoints”

The boxed pairing gives an ordinary contravariant adjunction between presheaves and copresheaves: writing y_a=A(-,a) and y^a=A(a,-), φ(P)(a)=Nat(P,y_a) and ψ(Q)(a)=Nat(Q,y^a). These formulas explain the evaluation pairings without implying that φ or ψ is an equivalence. Credit Hua’s modernised reading for identifying this with the Isbell construction; the formulas can be checked directly from Yoneda within the supplied material.

**Context searched:** context/hua_project/115.modern.tex: La dualité; context/notes/RESULTS_STATE.md: Hua 115-isbell-duality-derived-from-kernels; 115-isbell-reflexivity-left-open.

## 115-R17 — 115 scan008 — unproved uniqueness statements (a),(b),(c)

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 008):**

```tex
-- ce qui caractérise $\psi_A$ à iso unique près
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan008.tex`.

**Analytical anchor (may use modernized notation):** “caractérise … à iso unique près”

The asserted uniqueness of ψ, φᵒ and H_A is the ordinary density/cofree-completion statement: restriction to the representable generators, together with the stated separate limit or colimit preservation, determines their values on a presheaf presentation. For H_A the displayed value on representables is Hom_A(a,b), in this order. The page offers no derived or weak-equivalence version of that uniqueness, and the quantifier “commutes with limits” must be read in the relevant opposite categories.

**Context searched:** context/hua_project/115.modern.tex: La dualité; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE E.3,F.1 (stronger enhanced assertions).

**Confidence:** High for the ordinary statement: density determines a functor from its represented values under the indicated preservation hypotheses.

## 115-R18 — 115 scan008 — opposition identities

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 008):**

```tex
\varphi_{A^\circ}&=\psi_A
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan008.tex`.

**Analytical anchor (may use modernized notation):** φ_{Aᵒ}=ψ_A; ψ_{Aᵒ}=φ_A; H_{Aᵒ}(Ψ,Φ)=H_A(Φ,Ψ)

The margin directly exchanges the two conjugate constructions when the base category is opposed. This is a natural formal symmetry of ordinary diagram categories, not an equivalence between the two fine homotopy theories over one unchanged base. BISITE F.8 is the appropriate stronger comparison, because it explicitly separates base opposition from coefficient opposition.

**Context searched:** context/hua_project/115.modern.tex: La dualité; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE F.8,C.4.

## 115-R19 — 115 scan008 — units and representable fixed points

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 008):**

```tex
iso si $\Phi\in\mathrm{Ob}\,A$ ou $\Psi\in\mathrm{Ob}\,A$
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan008.tex`.

**Analytical anchor (may use modernized notation):** “iso si Φ∈Ob A ou Ψ∈Ob A”

The units α_P:P→ψφP and β_Q:Q→φψQ are ordinary evaluation maps, and Yoneda proves the stated isomorphisms for represented objects. This positive assertion does not imply the following converse question or any weak-equivalence property for arbitrary objects. Its proof needs no stable or derived enhancement.

**Context searched:** context/hua_project/115.modern.tex: La dualité; context/notes/RESULTS_STATE.md: Hua 115-isbell-reflexivity-left-open.

## 115-R20 — 115 scan008 — explicit representability question / own illustration

**Kind:** `conjecture`.

**Literal cue (verbatim frozen TeX; cote 115, scan 008):**

```tex
\alpha_\Phi,\beta_\Psi$ ? Iso (si et) seulement si $\Phi$ resp. $\Psi$ est représentable ?
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan008.tex`.

**Analytical anchor (may use modernized notation):** “Iso (si et) seulement si … représentable ?”

The converse fails in a simple example: let A be the discrete category on two objects and P=(∅,∅), so φP=(1,1), ψφP=(∅,∅), and the unit is an isomorphism although P is not representable. This P is not even a retract of either represented presheaf (1,∅) or (∅,1), because no map from either to P exists. This is an own checked illustration of the broader reflexivity point already credited to Hua’s finding, not a novelty claim; the phrase “sans doute pas” is not attached to this question in the frozen layout.

**Context searched:** context/hua_project/115.modern.tex: La dualité; L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-reflexivity-left-open.

**Confidence:** High: direct calculation of both conjugates.

## 115-R21 — 115 scan008 — explicit weak-equivalence question / own answer

**Kind:** `conjecture`.

**Literal cue (verbatim frozen TeX; cote 115, scan 008):**

```tex
tjrs une équivalence faible (sans doute pas).
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan008.tex`.

**Analytical anchor (may use modernized notation):** “Est-ce|Est-on tjrs une équivalence faible (sans doute pas).”

Here “sans doute pas” qualifies whether the units are always weak equivalences, correcting the attachment suggested by Hua’s finding and modernised narrative. Under the ordinary W∞ class detected by categories of elements, take A=e and P={0,1}: both conjugates are singletons, so α_P:2→1 changes the number of connected components and is not a weak equivalence. The symmetric copresheaf statement fails in the same way; this own example has high confidence under the explicitly stated W∞ interpretation.

**Context searched:** context/hua_project/115.modern.tex: La dualité (interpretive attachment checked against frozen layout); context/notes/RESULTS_STATE.md: Hua 115-isbell-reflexivity-left-open.

**Confidence:** High under W∞ via categories of elements.

## 115-R22 — 115 scan008 — explicit weak-map-to-isomorphism question / own answer

**Kind:** `conjecture`.

**Literal cue (verbatim frozen TeX; cote 115, scan 008):**

```tex
Les foncteurs $\varphi_A$ et $\psi_A$ transforment-ils équiv. faibles en isom ?
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan008.tex`.

**Analytical anchor (may use modernized notation):** “transforment-ils équiv. faibles en isom ?”

Again for W∞ detected by categories of elements, let A=[1] and use y₀→y₁: both element categories have terminal objects, so this map is a weak equivalence. Its φ-image is the reversed map A(1,-)→A(0,-), whose value at 0 is ∅→1, hence it is not an isomorphism; opposition gives the corresponding ψ failure. This own check answers the separate third question without asserting a conclusion for every possible unspecified weak class.

**Context searched:** context/hua_project/115.modern.tex: La dualité; context/notes/RESULTS_STATE.md: Hua 115-isbell-reflexivity-left-open.

**Confidence:** High under the explicit W∞ convention.

## 115-R23 — 115 scan008 — ordinary contraction / separate kernel

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 008):**

```tex
H^A(a,b)\overset{\inserted{\text{ou}}}{=}\mathrm{Hom}_A(b,a)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan008.tex`.

**Analytical anchor (may use modernized notation):** H^A(a,b)=Hom_A(b,a); Φ*a=Φ(a); a*Ψ=Ψ(a)

The contraction H^A(P,Q)=∫^a P(a)×Q(a) is separately cocontinuous and has the displayed Yoneda evaluation rules, so it is distinct from the contravariant Hom pairing H_A. On represented inputs its order is Hom_A(b,a), the reverse of H_A(a,b), and this order is essential for scan010’s pairing identities. This gives an ordinary coend precursor of BISITE G.2/G.4, not their covariant spectral dualizing weight or a Verdier duality.

**Context searched:** context/hua_project/115.modern.tex: La dualité; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE G.2,G.4; context/companion/chunks/DER_XIIb-a.tex, ms.68 (ordinary coend transport).

## 115-R24 — 115 scan009 — cancelled multivariable topoi draft

**Kind:** `withdrawn in the same text`.

**Literal cue (verbatim frozen TeX; cote 115, scan 009):**

```tex
X_1\otimes X_2\simeq\mathrm{Hom}(X_1^\vee,X_2^\vee;\underline1)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan009.tex`.

**Analytical anchor (may use modernized notation):** F(X₁×…×Xₙ), X₁⊗X₂, and mixed Hom^{!!}_{!!} displays

The extension from presheaf categories to general X_i is inside a cancelled working block, with incomplete expressions and disputed signs on the Hom symbols. It gestures toward a tensor/duality formalism for topoi but supplies neither a definition of the tensor in this generality nor a proof of the displayed equivalences. Credit Hua’s programmatic interpretation, while preserving the difference between the explicit ordinary kernel wheel and this abandoned generalization.

**Context searched:** context/hua_project/115.modern.tex: Résumé; Noyaux entre topos de préfaisceaux; context/notes/RESULTS_STATE.md: MPL_105 — BISITE F.10; BISITE F.18.

## 115-R25 — 115 scan009 — cancelled duality question and reversed two-cell

**Kind:** `withdrawn in the same text`.

**Literal cue (verbatim frozen TeX; cote 115, scan 009):**

```tex
\deleted{\unsure{A}}\quad\mathcal F(X^\vee)\ ?
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan009.tex`.

**Analytical anchor (may use modernized notation):** μ downward, μ∨ upward; “F(X∨) ?”

The two diagrams reverse the displayed natural-transformation direction while retaining the displayed direction of the object-level functors, and the adjacent question asks what F(X∨) should mean. This is evidence that a 2-categorical duality is being sought, not a completed definition of a dual topos or an involutive higher functor. BISITE F.18 and GALOIS E.11/G.6 remain open targets in RESULTS_STATE; the cancelled drawings do not settle them.

**Context searched:** context/hua_project/115.modern.tex: Résumé; context/notes/RESULTS_STATE.md: BISITE F.18; GALOIS E.11; GALOIS G.6.

## 115-R26 — 115 scan009 — cancelled point/presheaf comparison

**Kind:** `withdrawn in the same text`.

**Literal cue (verbatim frozen TeX; cote 115, scan 009):**

```tex
\mathrm{Top}(A)\arrow[r,"\varphi"]&X\arrow[r,no head,"\psi"]&\mathrm{Top}(B)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan009.tex`.

**Analytical anchor (may use modernized notation):** Top(A)→X→Top(B); A→Pt(X)

The point-category sketch and the partial expressions φ_*∨(F), ψ*(G) are unfinished pieces of the same cancelled block. They suggest a proposed passage between presentations of X and kernel data, but there is no stated comparison theorem or specified hypotheses on points. These are not enough to identify the ordinary presheaf construction with a general topos correspondence.

**Context searched:** context/hua_project/115.modern.tex: Résumé; context/notes/RESULTS_STATE.md: MPL_105 — BISITE F.10 (unpursued enhancement lead).

## 115-R27 — 115 scan010 — two affirmative ordinary pairing identities

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 010):**

```tex
\langle\Phi_*,f^{\circ *}(\Psi^*)\rangle_A&\simeq\langle f_!(\Phi_*),\Psi^*\rangle_B
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan010.tex`.

**Analytical anchor (may use modernized notation):** ⟨Φ_*,fᵒ*Ψ*⟩_A≃⟨f_!Φ_*,Ψ*⟩_B; ⟨f*Ψ_*,Φ*⟩_A≃⟨Ψ_*,fᵒ_!Φ*⟩

Both boxed identities are ordinary coend/Kan adjunction identities when the brackets denote the contraction pairing of scan008; the second display’s final base subscript is not supplied in the frozen text. They must not be conflated with scan003’s questioned formula for the different Hom-kernel pairing, or with a base-change theorem for a cartesian square. The cancelled marginal “si fᵒ iso” is a discarded qualification, not an established restriction on the correct ordinary formulas.

**Context searched:** context/hua_project/115.modern.tex: La dualité; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE F.1,F.4,F.7.

## 115-R28 — 115 scan011 — motivating definition with variance conflict

**Kind:** `reading question`.

**Literal cue (verbatim frozen TeX; cote 115, scan 011):**

```tex
H^x\in A^\vee\qquad H^x(\cdot)=\mathrm{Hom}_B(a,x)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan011.tex`.

**Analytical anchor (may use modernized notation):** H_x(a)=Hom_B(a,x); H^x(·)=Hom_B(a,x)

The frozen line for H^x repeats the order used for H_x, which is incompatible with declaring H^x covariant and with composing H_x(a)×H^x(b) into Hom_A(a,b). The contextual construction would use maps x→b in the second factor, but that is a research reading question, not permission to change the frozen transcription. Hua’s “L’enveloppe” uses the coherent two-sided version and must be credited as an interpretation.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual.

## 115-R29 — 115 scan011 — abstract triple-category construction

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 011):**

```tex
la catégorie des triples $(H_*,H^*,\alpha)$
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan011.tex`.

**Analytical anchor (may use modernized notation):** “catégorie des triples (H_*,H^*,α)”

Independently of the preceding motivating slip, the abstract data P∈Â, Q∈A∨ and α_{a,b}:P(a)×Q(b)→A(a,b) form a coherent ordinary category when a morphism is (u:P→P′,v:Q′→Q) satisfying α(p,vq′)=α′(up,q′). Identity and composition follow by substitution, giving a direct elementary check of the definition rather than a derived enhancement. This is the precise paired-object construction underlying Hua’s Isbell-envelope lead.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual.

**Confidence:** High: identity and composition satisfy compatibility by substitution.

## 115-R30 — 115 scan011 — compatibility notation conflict

**Kind:** `reading question`.

**Literal cue (verbatim frozen TeX; cote 115, scan 011):**

```tex
H'^*(b)\arrow[u,"\varphi'_*"']
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan011.tex`.

**Analytical anchor (may use modernized notation):** φ*:H′*→H*; later arrow and equation labelled φ′_*

The abstract morphism list specifies a contravariant second component φ*, but the compatibility diagram and equation label that second component φ′_*. Since the prime/subscript notation is not identified with φ* on the page, the research note must retain this internal notation conflict while recording the intended compatibility equation separately. It does not obstruct the abstract category once its two component directions are explicitly fixed.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual.

## 115-R31 — 115 scan011 — unproved functor from a fully faithful extension

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 011):**

```tex
Pour un foncteur pl. fid \(A\xrightarrow{\varphi}B\), on déduit un foncteur
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan011.tex`.

**Analytical anchor (may use modernized notation):** “Pour un foncteur pl. fid A→B, on déduit … B→Ã”

With the coherently typed incoming and outgoing Hom functors, full faithfulness of A→B identifies Hom_B(a,b) with Hom_A(a,b), so composition supplies the pairing and each arrow x→x′ supplies the two required component maps. This proves the ordinary comparison functor under that interpretation, but its formula in the frozen text still contains unresolved a|x arguments and the H^x issue. The functor need not be fully faithful without a separate generation/density condition, which is precisely the next page’s question.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual.

**Confidence:** High under the coherently typed Hom interpretation: composition defines the pairing and both component maps.

## 115-R32 — 115 scan012 — canonical self-duality assertion

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 012):**

```tex
$\widetilde{A^\circ}\simeq\widetilde A^\circ$ canonique
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan012.tex`.

**Analytical anchor (may use modernized notation):** “Ã^{op} ≃ (Aᵒ)~ canonique”

Swapping P,Q and transposing α identifies the abstract triple category for Aᵒᵖ with the opposite of the triple category for A, including reversal of the two components of a morphism. This is an elementary ordinary equivalence and supports Hua’s self-duality lead once the triple definition is fixed. It is a change of base to Aᵒᵖ, not a duality of the original presheaf category over unchanged A.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE F.8.

**Confidence:** High: swapping components and transposing the pairing gives inverse constructions.

## 115-R33 — 115 scan012 — full-faithfulness question and proposed sufficient condition

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 012):**

```tex
Il suffit que $f$ soit strict. génér. ou fon. cogénérateur.
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan012.tex`.

**Analytical anchor (may use modernized notation):** “Cas où φ♯ est pl. fidèle ? Il suffit que f soit strict. génér. ou fon. cogénérateur.”

The stated sufficient condition is not defined or proved on this page, so “strict. génér.” cannot silently be identified with a modern density condition. A safe own sufficient condition is that the incoming restricted Yoneda functor B→Â be fully faithful: its density then makes every pairing-compatible outgoing component the unique precomposition component of the same arrow; the dual codensity hypothesis works similarly. Confidence is high for this explicitly stronger condition, while its equivalence to the manuscript’s abbreviated terminology remains unresolved.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual.

**Confidence:** High for stated density criterion; terminology unresolved.

## 115-R34 — 115 scan012 — Yoneda special case / commutativity question

**Kind:** `conjecture`.

**Literal cue (verbatim frozen TeX; cote 115, scan 012):**

```tex
v=v'\circ\varphi_*\ ?
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan012.tex`.

**Analytical anchor (may use modernized notation):** “φ♯ fidèle”; “comm ?”; “v=v′∘φ_* ?”

For B=Â, the first component of the comparison is literally F, so faithfulness is immediate. Its fullness follows because the displayed equality vu=(v′φ_*)u for every u:y_a→F detects equality of the two maps F→y_b by Yoneda, forcing the second component to be the conjugate of the first. This supplies an own elementary completion of the page’s local question and validates the full embedding Â→Ã under the coherent triple definition; the copresheaf embedding follows by opposition.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual.

**Confidence:** High: representables detect equality of presheaf maps.

## 115-R35 — 115 scan012 — essential-image union and special triple forms

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 012):**

```tex
\unsure{la réunion} des \unsure{images} essentielles de
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan012.tex`.

**Analytical anchor (may use modernized notation):** “réunion des … images essentielles”; (F,G,α)≃(F,F♯,α_F) or ≃(G♭,G,α^G)

The rewritten lines single out the essential images of the two fully faithful embeddings, while the displayed special triple forms characterize membership in each image. Their full union is a subcategory of the full triple-envelope, but the page does not prove that every triple belongs to either image or identify their overlap. The overlap inside the triple-envelope involves mutually conjugate/reflexive data, so it must be distinguished from the different cocontinuous/representable overlap drawn on scan014.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual; 115-isbell-reflexivity-left-open.

## 115-R36 — 115 scan012 — functoriality diagrams with opposing directions

**Kind:** `reading question`.

**Literal cue (verbatim frozen TeX; cote 115, scan 012):**

```tex
B&\widetilde B\arrow[u,"\widetilde f"']&\widehat B\arrow[u,"f^*"']
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan012.tex`.

**Analytical anchor (may use modernized notation):** One diagram has B~→A~; the final oval has A~→B~

The frozen arrows do not determine a single functoriality theorem: restriction of a B-pairing gives values in Hom_B(fa,fa′), rather than Hom_A(a,a′), and only a fully faithful f supplies the inverse identification needed for a raw restriction to the A-envelope. As an own construction, every f:A→B instead gives a covariant envelope functor by left Kan extension of both components, with pairing [h:b→fa,p]×[q,k:fa′→b′]↦k f(α(p,q))h. The construction is coherent up to the canonical Kan-composition isomorphisms, but does not automatically commute with both graph embeddings of the presheaf and copresheaf categories; confidence is high for this explicit construction and medium as an explanation of the intended arrows.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual; MPL_105 — BISITE F.10.

**Confidence:** High for the explicit coend pairing; medium for intended manuscript interpretation.

## 115-R37 — 115 scan014 — Karoubi comparison / distinct ambient categories

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 014):**

```tex
(Kar(A^\circ))^\circ \simeq Kar(A)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan014.tex`.

**Analytical anchor (may use modernized notation):** Kar(Aᵒ)ᵒ≃Kar(A), with hooks to Â and A∨ᵒ inside Hom(A∨,Set)

The top diagram realizes presheaves as cocontinuous Set-valued functors on A∨ and opposite copresheaves as representable such functors; a functor in both classes represents a small-projective object, hence a retract of a corepresentable by the ordinary density presentation. This is the Karoubi/Cauchy comparison in that functor-category ambient, and it must not be identified with the full reflexive locus of the triple-envelope from scans011–012. The discrete-two-object initial-presheaf example in R20 shows why the latter reflexive locus can exceed Kar(A); credit Hua for the inclusion-versus-equality warning, while keeping the two constructions separate.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual; 115-isbell-reflexivity-left-open.

**Confidence:** High for the density/retract argument; exact drawn intermediate symbol remains doubtful.

## 115-R38 — 115 scan014 — E(A) embedding / intersection ambiguity

**Kind:** `reading question`.

**Literal cue (verbatim frozen TeX; cote 115, scan 014):**

```tex
A=\widehat A\unsure{\cap|,}A^{\vee\circ}
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan014.tex`.

**Analytical anchor (may use modernized notation):** “E(A)”→Hom(A^{vee|circ},Set) “pl. fid.”; “A=Â cap|, A∨ᵒ”

The diagram proposes an intermediate E(A) containing both displayed images, but the target superscript and cap/comma symbol remain doubtful and no definition of E(A) is supplied here. If the last line is read as a literal equality of the cocontinuous/representable intersection with A, idempotent completion is missing in general: that intersection corresponds to Kar(A), as the diagram immediately above suggests. This is a conditional reading-level caution, not a repair or a claim that the full triple-envelope embeds in that ordinary functor category.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/notes/RESULTS_STATE.md: Hua 115-isbell-envelope-self-dual.

**Confidence:** High for conditional Karoubi correction; literal notation unresolved.

## 115-R39 — 115 scan014 — unproved ordinary gluing assertion and caveat

**Kind:** `self-flagged`.

**Literal cue (verbatim frozen TeX; cote 115, scan 014):**

```tex
et $N'-N$ n'est pas tjrs une équivalence.
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan014.tex`.

**Analytical anchor (may use modernized notation):** “Σ′ … somme des sous-catégories pleines”; “ne sont pas néct. ss. pl.”; “N′–N n’est pas tjrs une équivalence”

The page first proposes a fully faithful Σ′→M and then records failures of fullness/intersection equivalence, so it supplies a cautionary gluing sketch rather than a proved universal amalgamation statement. An own elementary illustration is M=[1] with full pieces {0},{1} and empty intersection: their categorical pushout is two discrete objects, while their full union in M retains the crossing arrow 0→1. Consequently “somme” needs an explicit interpretation and crossing-Hom data; this is an ordinary issue, distinct from BISITE E.13’s loss of coherent gluing after taking homotopy categories.

**Context searched:** context/hua_project/115.modern.tex: L’enveloppe; context/companion/chunks/DER_XIIb-a.tex, ms.59–63 (crossing bimodule and collage); context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE E.13; context/notes/RESULTS_STATE.md: MPL_150_085-099+151_001-031 §106 (STRATA C.1 lead only).

**Confidence:** High: finite-category pushout versus full ambient union.

## 115-R40 — 115 scan015 — unqualified ordinary free cocompletion

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 015):**

```tex
\underline{\mathrm{Hom}}(A,M)\simeq
\underline{\mathrm{Hom}}_!(\widehat A,M)\simeq
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan015.tex`.

**Analytical anchor (may use modernized notation):** Hom(A,M)≃Hom_!(Â,M)

For small A and a cocomplete coefficient category M, the equivalence is the ordinary free cocompletion statement: extend a functor on A by colimits over categories of elements. The page does not state the cocompleteness or size hypotheses, and the incomplete following formulas do not add them. This is a precursor to BISITE E.3, whose enhanced slice-recognition premises are much stronger.

**Context searched:** context/hua_project/115.modern.tex: Coefficients; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE E.3; context/notes/RESULTS_STATE.md: GALOIS E.11; G.6.

## 115-R41 — 115 scan015 — unqualified additive extension / own counterexample

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 015):**

```tex
\mathrm{Hom}_!(\widehat A_{ab},M).
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan015.tex`.

**Analytical anchor (may use modernized notation):** Hom(A,M)≃Hom_!(Â_ab,M)

The additive equivalence needs a specified additive coefficient setting; as an unrestricted assertion about M it fails for A=e and M=Set. Any colimit-preserving functor Ab→Set sends the initial object 0 to ∅, and the arrows X→0 then force every value to be ∅, whereas Hom(e,Set) is equivalent to all of Set. This own high-confidence counterexample tests the literal unrestricted reading and does not deny a correctly hypothesized additive free-cocompletion theorem.

**Context searched:** context/hua_project/115.modern.tex: Coefficients; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE E.3; context/notes/RESULTS_STATE.md: GALOIS E.11; G.6.

**Confidence:** High: preservation of the initial object and maps to zero.

## 115-R42 — 115 scan015 — unfinished additive formula

**Kind:** `reading question`.

**Literal cue (verbatim frozen TeX; cote 115, scan 015):**

```tex
\mathrm{Hom}_!(\widehat A_{ab}
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan015.tex`.

**Analytical anchor (may use modernized notation):** “Ex M=Ab|…”; final “Hom_!(Â_ab” has no completed target

The Ab-valued example and the equivalence Hom(Bᵒ,Ab)≃B̂_ab indicate the intended linear direction, but the next Hom_! expression is unfinished. It cannot be completed from the neighbouring cotes or Hua’s exposition in the transcription, and it supplies no theorem that linearization yields an equivalent derived category. The relevant general higher-coefficient construction remains open under GALOIS E.11/G.6 in RESULTS_STATE.

**Context searched:** context/hua_project/115.modern.tex: Coefficients; context/notes/RESULTS_STATE.md: GALOIS E.11; GALOIS G.6.

## 115-R43 — 115 scan015 — cofaisceau/faisceau variance

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 015):**

```tex
\text{cofaisceaux sur }A,\ \text{à val. dans }M.
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan015.tex`.

**Analytical anchor (may use modernized notation):** A=Bᵒ; “cofaisceaux sur A” and “faisceaux sur B”

The two presentations identify functors A→M with opposite-base presheaf data, and then express them through cocontinuous or continuous extensions under the appropriate existence hypotheses. This is an ordinary variance dictionary, not a construction of geometric sheaf–cosheaf Verdier duality. In particular it provides no cosheaf pushforward or finite-poset hypothesis of BISITE G.12.

**Context searched:** context/hua_project/115.modern.tex: Coefficients; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE F.8,G.12; context/notes/RESULTS_STATE.md: BISITE D.13 (related geometric duality claim).

## 115-R44 — 115 scan015 — formal coefficient opposition

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 015):**

```tex
\mathcal F(\mathcal X,M)^\circ\simeq\mathcal F^\vee(\mathcal X,M^\circ)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan015.tex`.

**Analytical anchor (may use modernized notation):** F(X,M)ᵒ≃F∨(X,Mᵒ); “duals|duales l’une de l’autre”

Opposing a category of limit-preserving functors converts it into a category of colimit-preserving functors with both source and coefficient oppositions, as the last line Hom^!(Aᵒ,M)≃Hom_!(A,Mᵒ)ᵒ makes explicit. This is the precise formal content behind the duality language, and it supports the distinction made by BISITE F.8. It is not an involutive duality on arbitrary fixed coefficients M, nor does it supply the perfect-object dualities of BISITE G.6.

**Context searched:** context/hua_project/115.modern.tex: Coefficients; context/DOSSIER_STATEMENTS_WITH_STATUS.md: BISITE F.8,G.6.

## 115-R45 — 115 scan015 — unproved opposite-topos notation

**Kind:** `unproved claim`.

**Literal cue (verbatim frozen TeX; cote 115, scan 015):**

```tex
\mathcal F(\mathcal X,M)\simeq\mathcal F^\vee(\mathcal X^\circ,M)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan015.tex`.

**Analytical anchor (may use modernized notation):** F(X,M)≃F∨(Xᵒ,M)

This further display uses Xᵒ without a completed definition of an opposite topos on these pages, so its general topos-level meaning remains unresolved. It may encode the ordinary opposite indexing category already used for presheaf topoi, but cannot by itself prove the cancelled X∨ program of scan009. The rigorous formal functor-category opposition of R44 is the available evidence.

**Context searched:** context/hua_project/115.modern.tex: Coefficients; context/notes/RESULTS_STATE.md: BISITE F.18; MPL_105 — BISITE F.10.

## 115-R46 — 115 scans005,007,013 — ancillary surfaces / coverage boundary

**Kind:** `reading question` — ancillary scope note.

**Literal cue (verbatim frozen TeX; cote 115, scan 007):**

```tex
\node at (2,-.65){$B$};
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan007.tex`.

**Analytical anchor (may use modernized notation):** No additional legible mathematical proposition in the frozen text; scan007 has a small labelled diagram

The frozen files for these scans are principally reused printer material or a small drawing, and contain no further explicit mathematical question or theorem to compare. Their absence from the substantive list is therefore a content distinction, not an omitted rescan or a reinterpretation from Hua’s page numbering. All substantive claims above are anchored to the frozen text, with Hua’s page n corresponding to scan n+1.

**Context searched:** context/notes/RESULTS_STATE.md: Hua findings provenance and page-offset rule; context/hua_project/README.md.

## Crossing-kernel comparison with the unavailable STRATA C.1 statement

### 115-C01 — Exact-ID availability and status

**Kind:** `unpursued implication`.

**Literal cue (verbatim frozen TeX; cote 115, scan 002):**

```tex
``Correspondances'' fonctorielles
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan002.tex`.

**Analytical anchor (may use modernized notation):** 115 scan002, “Correspondances” fonctorielles; scan004, X∈PSh(A×B).

The exact STRATA C.1 statement and its status are **not supplied** in `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, and searching the supplied context finds only the README’s “perhaps the bimodule of crossing arrows of STRATA C.1” and the RESULTS_STATE reference to `MPL_150_085-099+151_001-031 §106`. Thus no full identification with C.1, nor verification of that result, can be claimed here. The comparison below is with the explicit supplied collage passage, which is enough to make the shape, variance and strength of the proposed connection precise.

**Context searched:** `context/README.md`, research instruction XVI; `context/notes/RESULTS_STATE.md`, `MPL_150_085-099+151_001-031 §106`; `context/companion/chunks/DER_XIIb-a.tex`, XII ms.59–63; `context/companion/chunks/DER_XIIapp.tex`, appendix ms.17–18.

### 115-C02 — Same ordinary bimodule shape after one opposition

**Kind:** `unpursued implication`.

**Literal cue (verbatim frozen TeX; cote 115, scan 006):**

```tex
=\underline{\mathrm{Hom}}(A^\circ,B^\circ;\mathrm{Ens})
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan006.tex`.

**Analytical anchor (may use modernized notation):** 115 scan004, X∈PSh(A×B); scan006, Hom(Aᵒ,Bᵒ;Ens).

A cote115 kernel is contravariant in both displayed small categories, X:Aᵒᵖ×Bᵒᵖ→Set. The companion’s crossing data for a full sieve U and complementary cosieve T is H:Uᵒᵖ×T→Set, H(u,t)=Hom_X(u,t), so the same set-valued input is obtained by setting **A=U and B=Tᵒᵖ**. This is an exact variance match of ordinary bimodule data, but cote115 does not itself choose an ambient category, a complementary cut, or forbid crossings in the reverse direction.

**Context searched:** `context/companion/chunks/DER_XIIb-a.tex`, XII ms.59–60, Proposition1 and commentary “An open–closed cut remembers a profunctor”; `context/notes/RESULTS_STATE.md`, STRATA0.1 and `MPL_150_085-099+151_001-031 §106` (lead only); `context/hua_project/115.modern.tex`, “Noyaux entre topos de préfaisceaux”.

| Feature | Frozen cote115 | Supplied crossing-collage passage | Result of comparison |
|---|---|---|---|
| Small inputs | A and B | U and T | Match by A=U, B=Tᵒᵖ. |
| Variance | Aᵒᵖ×Bᵒᵖ→Set | Uᵒᵖ×T→Set | Exactly matched after opposing the second input. |
| Meaning of values | An arbitrary presheaf kernel X(a,b) | Actual crossing arrows Hom_X(u,t) | Same type of data; extra interpretation belongs to the collage. |
| Reverse crossings | Not specified | Hom_X(t,u)=∅ because U is a sieve | This structural constraint is absent from cote115’s arbitrary-kernel setup. |
| Reconstruction | Currying and transforms of the kernel | Coll(H), with objects U⊔T, original internal Homs and crossing Homs H | The reconstruction is explicit only in the supplied companion. |
| Pairing/envelope | Triples (P,Q,α:P⊠Q→Hom_A) | One bimodule H between two fixed categories | These are different constructions; an envelope object is a factorization datum through the Hom kernel, not the crossing bimodule itself. |
| Homotopical strength | Ordinary Set-valued identities; weak-equivalence questions remain separate | Appendix adds a crossing-arrow bridge and a homotopy-pushout comparison | No general coherent-gluing/base-change result is stated by cote115’s wheel. |

### 115-C03 — What the collage adds

**Kind:** `unpursued implication`.

**Literal cue (verbatim frozen TeX; cote 115, scan 014):**

```tex
Alors on définit une catégorie $\Sigma'$
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan014.tex`.

**Analytical anchor (may use modernized notation):** 115 scan004’s general kernel; scan014’s “somme” of full subcategories.

The companion reconstructs Coll(H) from U,T,H by retaining the original Homs within U and T, inserting H(u,t) as the crossing Homs, and setting Homs from T to U empty; functoriality of H supplies the mixed compositions. Every composable string then crosses at most once, which makes associativity an ordinary direct check and explains the unrestricted reconstruction assertion of XII Proposition1. Cote115 supplies precisely the possible input kernel after the variance adjustment, but not this reconstruction statement or its full-sieve/cosieve hypotheses.

**Context searched:** `context/companion/chunks/DER_XIIb-a.tex`, XII ms.59–60, Proposition1 and its supplied commentary; `context/notes/RESULTS_STATE.md`, `MPL_150_085-099+151_001-031 §106` (unreviewed lead); exact STRATA C.1 remains unavailable.

### 115-C04 — Pairing triples are not the collage of a crossing kernel

**Kind:** `unpursued implication`.

**Literal cue (verbatim frozen TeX; cote 115, scan 011):**

```tex
H_x(a)=\mathrm{Hom}_B(a,x)
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan011.tex`.

**Analytical anchor (may use modernized notation):** 115 scan011, “catégorie des triples (H_*,H^*,α)”.

In the motivating fully faithful A→B construction, x∈B contributes incoming arrows B(-,x)|_A, outgoing arrows B(x,-)|_A and composition through x into A(-,-). This is an object of a category of factorizations/pairings around the Hom kernel of one category A, whereas the collage construction starts with two categories U,T and a single cross-Hom bimodule between them. The two constructions share profunctor language and can inform one another, but identifying the triple-envelope itself with “the crossing bimodule of STRATA C.1” would collapse distinct mathematical objects.

**Context searched:** `context/hua_project/115.modern.tex`, “L’enveloppe”; `context/companion/chunks/DER_XIIb-a.tex`, XII ms.59–60; `context/notes/RESULTS_STATE.md`, Hua 115-isbell-envelope-self-dual and `MPL_150_085-099+151_001-031 §106`.

### 115-C05 — The crossing-arrow category is further structure

**Kind:** `unpursued implication`.

**Literal cue (verbatim frozen TeX; cote 115, scan 006):**

```tex
Toutes les flèches du diagramme sont des équivalences de catégories
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan006.tex`.

**Analytical anchor (may use modernized notation):** 115 scan006 claims equivalences of ordinary functor categories; scan010 gives ordinary pairings.

The appendix defines E with objects crossing arrows a→b and morphisms ordinary commuting squares, with source projection p:E→U a split fibration and target projection q:E→T a split opfibration, together with ip⇒jq. This ordinary crossing-arrow category is **not a twisted-arrow category**, and its natural transformation is part of the data used in the companion’s homotopy-pushout discussion. Cote115 does not construct E, those two projections or the homotopy-pushout comparison, so its kernel equivalences are strictly weaker evidence than the later coherent gluing discussion.

**Context searched:** `context/companion/chunks/DER_XIIapp.tex`, appendix ms.17–18, commentary beginning “Write E=…”, and its subsequent homotopy-pushout discussion; `context/notes/RESULTS_STATE.md`, `MPL_150_085-099+151_001-031 §106`; `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.13,F.9,F.10.

### 115-C06 — Own useful reconstruction, with scope and confidence

**Kind:** `own idea`.

**Literal cue (verbatim frozen TeX; cote 115, scan 014):**

```tex
somme des sous-catégories pleines
```

**Literal-cue check:** PASS — exact substring in `deliverable/pages/MPL_108+112+113+114+115_115_scan014.tex`.

**Analytical anchor (may use modernized notation):** 115 scan014’s ordinary gluing caveat.

A productive way to make the connection concrete is to adjoin the explicit two-piece collage construction to a cote115 kernel with B=Tᵒᵖ, then compute its presheaves using the corresponding kernel transform; the companion’s U=T=e example gives H=S and the adjunction G↦G×S ⊣ F↦F^S. This supplies a finite test of variance and of the missing crossing data: S=∅ gives two independent Set factors, while S=1 gives the arrow-category relation. This is an **own synthesis of the supplied constructions**, with high confidence for the ordinary algebraic comparison and no claim to identify or prove the unavailable STRATA C.1, nor to obtain derived base change from it.

**Context searched:** `context/companion/chunks/DER_XIIb-a.tex`, XII ms.63, the Set-pair example and kernel adjunction; `context/notes/RESULTS_STATE.md`, STRATA0.1 and `MPL_150_085-099+151_001-031 §106`; `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.10,G.4.
