# The two context planning questions: evidence from frozen cote 62

**Research date:** 16 November 2026. **Status:** a text-only evidence comparison for the primary reader; no transcription change, manuscript audit, independent literature verification, or register-status update.

## Findings

1. **The supplied cote 62 selection does not provide an identified second witness of cote 47 with the compatibility check completed.** The outstanding step is identifiable precisely in the supplied cote 47 transcription, scan 8, first paragraph: whether the *particular canonical comparison map* constructed on scan 7 becomes an isomorphism at the unit fibre. Cote 62 supplies elementary elliptic-curve geometry, a Lie line, and inversion, but no Fourier kernel calculation or verification of that map. This is a negative finding for the present selection, not for the archive as a whole. [CTX-T, cote 47, scans 7–8; T62, scans 004–017; STATE, WG2 §2.4 #4.]

2. **No earlier form of cote 44, Theorems 1–7, is identified in the supplied cote 62 selection.** The numbered programme concerns cycle quotients, Albanese varieties, intermediate Jacobians, complementary duality, positivity, a height/intersection formula, Lefschetz behavior, and numerical versus tau equivalence. None of those programme statements appears in the frozen cote 62 text. The dated Serre letter already present in cote 44, scans 8–9, is a useful companion to the programme, but the available dating does not establish that it precedes the undated programme or that cote 62 precedes it. [CTX-T, cote 44, scans 2, 4, 6, 8–9; T62, all selected scans; STATE, WG2 §2.4 #4, WG2 §2.3 #12.]

There is one concrete additional subject overlap: the **cancelled completion draft in cote 44, scan 3**, has connections to the algebra/completion text preserved among the cote 62 sheets. It is separate from Theorems 1–7. The genus-zero trisection material in cote 62 is also a positive match to the subject of the separately registered **62-triples-rigidified-moduli** lead. Neither connection closes the two planning questions.

## Sources, scope, and status discipline

The primary reader reported the transcription frozen at **18:57:54 UTC**, before the context was opened. The combined frozen source read for this comparison has SHA-256:

`9d5b838824b3bf4663823f19a80d2c98330181407538c2af34143a0b6f2c6869`.

The text comparison covered **all 46 selected cote 62 page files**: scan 002, scans 004–017, scans 019–026, and scans 028–050. It included the full supplied cote 47 and cote 44 transcription fragments and the relevant associated notes. Both `README.md` and `notes/RESULTS_STATE.md` were read in full. No scan image, crop, Oda PDF, or external publication was opened for this comparison. Nothing outside this evidence file was changed.

The terms “the manuscript says” and “the letter says” below refer to what the **supplied transcription records**. They do not announce a second visual reading. Earlier editorial uncertainty markers remain consequential, especially cote 44's cycle-equivalence subscript, complementary index, and the undefined meaning of tau equivalence.

| Key | Exact source | Locator convention |
|---|---|---|
| README | `/workspace/scratch/a578466e229b/MPL_62_002-050_context/README.md` | Section heading |
| STATE | `/workspace/scratch/a578466e229b/MPL_62_002-050_context/notes/RESULTS_STATE.md` | Exact register/planning ID |
| CTX-T | `/workspace/scratch/a578466e229b/MPL_62_002-050_context/MPL_16+47+54+44_transcription.tex` | Cote, `\scanpage` number, and local statement |
| CTX-N | `/workspace/scratch/a578466e229b/MPL_62_002-050_context/MPL_16+47+54+44_notes.md` | Exact note heading/ID |
| T62 | `/workspace/scratch/a578466e229b/MPL_62_002-050_work/pages/MPL_62_002-050_62_scanNNN.tex` | Replace NNN by the three-digit scan number |
| T62 combined | `/workspace/scratch/a578466e229b/MPL_62_002-050_work/MPL_62_002-050_transcription.tex` | `\cotefile{62}` and `\scanpage` number |

README, “What is in this zip,” calls the previous `MPL_16+47+54+44_*` return **“not yet second-passed; claims”** and says its own-run material is not established unless a review is explicitly recorded. STATE's opening “Status” paragraph similarly distinguishes the returns' own claims, intake opinions, and explicit referee checks. The direct planning entries below are marked **unchecked**. No supplied review marker upgrades the cote 47/cote 44 return merely because its later notes contain literature citations or high editorial-confidence labels.

README also contains general material about cote 43, cote 149, and cote 142. Those paragraphs are planning context; they are not evidence that the present cote 62 selection contains those dossiers or their arguments.

## Question 1: a second witness of cote 47 with the compatibility check done?

### What exactly is unfinished in the supplied witness

The relevant sequence is unusually well localized:

| Cote 47 location in CTX-T | Recorded argument | Evidential consequence |
|---|---|---|
| Scan 3, opening proposition and universal reduction | An integral transform from an abelian scheme is defined by pullback, tensor with a normalized algebraically trivial line bundle, and derived pushforward; convolution is to become tensor product. The universal situation uses the dual abelian scheme and the Weil line bundle. | This identifies the mathematical object sought in a second witness. A general elliptic-curve or line-bundle calculation is not sufficient evidence of the same argument. |
| Scan 4, inversion theorem; scan 5, corrected derived composite | The composite is revised to include inversion, a dimension shift, and the line factor denoted tau. | The convention-dependent data include the map, sign, shift, and base line; an unadorned abstract equivalence would not automatically fill the written gap. |
| Scan 6, Lemma 1 and anti-diagonal argument | The direct image of the universal line bundle is asserted to be a zero-section pushforward, shifted by minus the relative dimension and twisted by the determinant of the tangent/Lie bundle. In the composition calculation the kernel locus is the anti-diagonal. The page ends “modulo dém. du Lemme 1.” | The inversion calculation depends on the still-unproved direct-image lemma. |
| Scan 7, admitted Lemma 2 | The cohomology of a nontrivial algebraically trivial invertible sheaf over an algebraically closed field is declared to vanish; the text explicitly says “Nous allons ici admettre le lemme 2.” | In this witness the vanishing result is an admitted input. It handles the complement of the unit section. |
| Scan 7, lower half | A **canonical comparison map** is constructed using top-degree base change and the identity on the determinant of the tangent bundle. | The issue is the behavior of this chosen map, not just the existence of some isomorphism of objects. |
| Scan 8, first paragraph | The comparison is tested after derived pullback to points. Away from the unit, Lemma 2 applies. At a point of the form e(s), the reduction to an algebraically closed field ends “à faire une vérification de compatibilité.....” | This is the exact unfinished step. |
| Scans 8–11, remaining remarks/calculations | Translations, line sheaves, determinant/Picard components, Chern expressions, Riemann–Roch, and duality/automorphism remarks follow. | No later completion of the unit-fibre check was identified in this supplied cote 47 fragment. |

In explanatory notation, the map at issue is

\[
\alpha:Rp_*W\longrightarrow e_*\mathcal O_S\otimes\tau_{B^*}[-n].
\]

Here the supplied text uses (p:B^*\times_S B\to B^*), the unit section (e:S\to B^*), and the line (\tau_{B^*}=\bigwedge^n t_{B^*}). At the bottom of scan 7 it constructs the top-degree map through

\[
R^nq_*\mathcal O_B\simeq\bigwedge^n R^1q_*\mathcal O_B
 \simeq\bigwedge^n t_{B^*},
\]

then takes the identity to (\tau_{B^*}). The omitted scan-8 comparison concerns the derived restriction of this construction to the unit. Matching dimensions, or exhibiting an abstract exterior-power pattern on the two sides, does not by itself verify the action of (\alpha). [CTX-T, cote 47, scan 7, canonical homomorphism and final displayed formula; scan 8, first paragraph.]

This reading is independently *recorded within the earlier return*, without being a second-pass endorsement of that return:

- **CTX-N 47:8:1** explicitly labels the ending an “unproved claim.”
- **CTX-N 47:8:2** distinguishes the derived pointwise criterion from the missing zero-section fibre map.
- **CTX-N F7** is an **editorial proof plan**, isolating the cone/perfect-complex criterion and saying that the particular unit-fibre map still needs verification.
- **CTX-N F8** gives an **editorial Tor/Koszul calculation** and expressly says it does not complete the compatibility of the actual comparison map.

Thus F7/F8 are useful directions for a future proof; they are not evidence that the compatibility check was already completed, either in a second manuscript or by the previous return.

### What cote 62 contributes and does not contribute

Cote 62, scan 004, explicitly identifies the **Lie line** (\mathcal L_{C/S}=s^*T_{C/S}), with the margin “faisceau de Lie.” Scans 005–008 study cohomological flatness of powers of the invertible sheaf attached to the zero divisor and their filtered direct images. Scan 014 normalizes coordinates using a trivialization of the Lie line and its powers; scan 015 discusses the discriminant and its twelfth-power normalization. Scan 017 records the canonical symmetry of the abelian scheme and its sign on the Lie line. These are direct textual connections to the basic dimension-one objects that occur in cote 47. [T62, scans 004, 005–008, 014–017.]

**Conceptual inference, limited to a test setting:** in relative dimension one, the determinant of the Lie bundle is the Lie line itself. The cote 62 material could therefore help set up a one-dimensional check of cote 47's determinant-line and inversion conventions. It does not construct the universal Poincaré/Weil kernel on (C\times C^\vee), identify its derived direct image, or evaluate the canonical comparison map at the unit. The later (\mathfrak S_3)-quotient calculations are maps between genus-zero objects and do not supply those missing constructions. [T62, scans 004, 014–017, 028–040; CTX-T, cote 47, scans 5–8.]

**Answer to WG2 §2.4 #4, first question:** *No completed second witness is identified in this packet's frozen cote 62 text.* The archive-wide search question remains open. This result does not establish that no such witness exists elsewhere, in excluded scans, in an unprovided continuation, or in another dossier.

## Question 2: earlier forms of cote 44, Theorems 1–7?

### Exact target statements and locations

The following table summarizes the programme as a programme; it does not certify the mathematical assertions.

| Target | Exact CTX-T locator | What the supplied text proposes | Relevant CTX-N headings |
|---|---|---|---|
| Th. 1 | Cote 44, scan 2, first theorem under “Programme de travail” | Identify (N(\xi)\subset\operatorname{Alb}(S)), “en substance,” with the kernel of the natural map to a cycle quotient. The equivalence-relation subscript remains uncertain in the supplied transcription. | 44:2:1; 44:2:5 |
| Th. 2 | Cote 44, scan 2, following paragraph | Bound the dimension of (\operatorname{Alb}(S)/N(\xi)=P_\xi) solely in terms of X, with the sharpened bound (\frac12b^{2i-1}(X)). | 44:2:2; D09 |
| Th. 3 | Cote 44, scan 2, after “Ces deux th. impliquent” | Give the algebraically trivial cycle quotient a natural abelian-variety structure, and assert complementary canonical duality. The complementary index on this page is explicitly uncertain between (n-i) and (n+1-i). | 44:2:3; D08 |
| Th. 4 | Cote 44, scan 2, final theorem and “Hodge” margin | For (n=2m-1), make the middle canonical self-duality arise from a polarization. | 44:2:4; 44:8:6; 44:9:1–4; D13 |
| Th. 5 | Cote 44, scan 4, “Néron” theorem | Relate the Néron–Tate pairing of restrictions to a generic hyperplane-pencil fibre, under algebraic-triviality hypotheses, to ((-1)^m Z\cdot Z'). The page revises the sign qualification and proposes a more general fibration statement and local variant. | 44:4:1–3; 44:4:5–6; D12 |
| Th. 6 | Cote 44, scan 4, corrected “Cor.” to “Th. 6,” with “Lefschetz” margin | Below the middle range, restriction is an isomorphism; in the middle, the fixed part is the image; above it, restriction is surjective. Cancelled finite-kernel formulations are separate draft layers. | 44:4:4 |
| Th. 7 | Cote 44, scan 6, sole theorem, “Matsusaka” margin | Assert numerical equivalence equals tau equivalence for algebraic cycles on smooth projective X. The meaning of tau is not defined there, and no codimension restriction is written. | 44:6:1–3; D14 |

Cote 62 does have numbered propositions and a “Théorème 1” on scan 020. That theorem concerns induced **adic topologies on a finite module and its submodule**, followed by Artin–Rees. Its number is not evidence of a version of cote 44, Th. 1. Likewise, “équivalentes” on cote 62, scan 031, concerns valuations, and the word `cycle` in some TeX lines is a TikZ path command; neither supplies cycle-equivalence content. [T62, scans 020, 031, and the drawing code on scans 019/020/026.]

### The dated letter is a companion, with a chronology limit

The supplied cote 44 transcription has a letter beginning **“Bures le 12.8.1964” / “Mon cher Serre”** on scan 8 and continuing on scan 9. It proposes (J^i(X)), gives the endpoints (J^1=\operatorname{Pic}^0), (J^n=\operatorname{Alb}^0), complementary duality with index (n+1-i), and the half-Betti dimension bound. Its Tate-module expectation and tangent/Hodge realization have their own qualifications. The text says it has not proved much and is full of conjectures; it does not establish the numbered programme by assertion. [CTX-T, cote 44, scan 8, opening paragraphs and margins; CTX-N 44:8:1–7.]

On scan 9 the letter constructs a divisor correspondence from a pointed family of middle-codimension cycles, passes through the Albanese and a quotient by a kernel, and asks explicitly **“A prouver que cette dernière est positive!”** This is a substantive companion to the positivity problem, not a proof that symmetry plus nondegeneracy gives a polarization. [CTX-T, cote 44, scan 9; CTX-N 44:9:1–5, D13.]

The letter was already in the supplied context. It is not a newly found cote 62 witness. Moreover, neither the undated programme nor the present cote 62 text supplies a secure chronological order relative to this letter. README's catalogue description “[à partir de 1963]” and “vieille rédaction” is not an exact date for the present handwritten argument. A claim of an *earlier* formulation would require additional dating or an explicit textual dependency.

### Actual overlap: the separate completion sheet

Cote 44, scan 3, contains a **cancelled graded-completion draft**, with (\widehat A=\prod A_i), a comparison of tensor-product completion with the product of homogeneous components for graded modules, and a final assertion that completion is exact and faithful under the unresolved “TF” qualification. It is not one of Theorems 1–7. [CTX-T, cote 44, scan 3; CTX-N 44:3:1–5, D07.]

The closest cote 62 comparison is the algebra material:

- **Scan 020**, printed page 20 / no. 276: induced adic topologies and Artin–Rees.
- **Scans 022, 024, 026**, printed pages 9–11 / no. 276: complete filtered modules, formal power series, and a filtered-map surjectivity criterion.
- **Scan 041**, printed page 18 / no. 276: completion of filtered modules, quotient comparison, and invariance of the associated graded ring.
- **Scan 043**, printed page 17 / no. 276: an exactness lemma for completion of metrizable topological abelian groups with the stated topological-homomorphism hypotheses.
- **Scan 045**, printed page 16 / no. 276: completion maps and comparison of the completion of a quotient with a quotient of completions.
- **Scans 047, 049**, printed pages 15 and 13 / no. 276: noetherianity and finite-generation consequences for complete filtered objects.

These give a **subject and proof-tool connection** to the cancelled cote 44 completion draft. They do not identify the unexplained “TF” condition, establish the graded category in which the final faithfulness assertion is meant, or prove that the two sheets are chronologically related. In particular, the exactness statement at cote 62, scan 043, cannot simply be substituted for every categorical qualification in cote 44, scan 3. [CTX-N 44:3:3–5 and D07 explicitly flag those distinctions.]

**Answer to WG2 §2.4 #4, second question:** *No earlier form of Th. 1–7 is identified in the present cote 62 selection.* There is a distinct completion connection and an already supplied dated letter, with the limits just stated.

## Coverage of the frozen cote 62 selection

This topic map supports the bounded negative result. It was made from the existing TeX text, not a new image reading.

| Cote 62 scan IDs | Content relevant to the search |
|---|---|
| 002 | “Courbes elliptiques” title |
| 004–017 | Zero divisor, Lie line, cohomological flatness, filtered direct images, cubic equations, change-of-coordinate groups, normalization, canonical symmetry, and the genus-zero quotient |
| 019, 021, 023, 025 | Discriminant/invariant calculations, Kummer-style notes, cross-ratios and marked points |
| 020, 022, 024, 026 | Adic/filtered rings and modules, Artin–Rees, completeness and formal series |
| 028, 030, 032, 034, 036, 038, 040 | The (\mathfrak S_3) action on (\mathbb P^1), ramification and quotient maps, cyclotomic quadratic extension, explicit invariant |
| 029, 031, 033, 035, 037, 039 | Valuations, places, extension, approximation, and integral closure |
| 041, 043, 045, 047, 049 | Further filtered-completion and noetherianity material, with handwritten annotations: scan 047 has the marginal triples \((0,1,\infty)\), \((2,1/2,-1)\), and \((x',x'')\), directly echoing the trisection calculation |
| 042, 044, 046, 048, 050 | Genus-zero objects with a trisection and an extra disjoint section; torsors, invariant, reconstruction questions, special invariant values, and equivariant parameter t |

A lexical search for Fourier/Poincaré/Pontryagin/convolution/compatibility terms did not locate the target argument in cote 62. The full text comparison, rather than that search alone, is the basis for the negative findings: notation can differ, and absence of a name is not absence of a proof. The primary reader's uncertainty markers were preserved, and no claim is made about omitted scans 003, 018, 027, any later pages, or unprovided archival material.

## Register implications and the positive trisection lead

| STATE ID | Supplied status | What this packet adds; what it does not add |
|---|---|---|
| **WG2 §2.4 #4** | Planning question, round 2, unchecked | Both questions receive a bounded negative answer for the selected cote 62 text. The archive-wide search remains open. |
| **WG2 §2.3 #12** | Planning description of the mathematics, unchecked | Exact cote 44 locators are supplied above. Cote 62 does not prove or refute the cycle-representability, duality, or positivity programme. |
| **WG H9** | Hunch, “Believe,” unchecked | No new height/intersection calculation in cote 62 supports the proposed identification of Th. 5 with a Mordell–Weil lattice formula or the claimed reduction of Th. 4. The sign, base field, pencil/fibre hypotheses, and positivity requirements remain substantive. CTX-N 44:4:1–6 and D12–D13 are useful leads, not a completed verification. |
| **WG2 §1.1 #3** | Planning description, unchecked | Explains the packaging of cotes 16, 44, 47, 54 as the earlier Book II return. It does not make cote 62 a missing continuation of those arguments. |
| **62-triples-rigidified-moduli** | AI-produced candidate conjecture; intake says “new to us,” package waiting | The subject is positively supported by cote 62, scans 042, 044, 046, 048, 050, and the handwritten margin on scan 047. The consecutive range interleaves reused typescript and handwritten material. The full proposed equivalence/novelty claim is not established by this source comparison. |
| **LM7 E.30** | “Proved” as the earlier return's own claim; no referee marker on this row | The common geometric object is the three-punctured projective line with its (\mathfrak S_3) action, explicit in cote 62, scans 028–040 and 050. Cote 62 does not supply the arithmetic relative-completion statement or verify that register result. This is an optional conceptual connection only. |

For **Hua, findings register, 62-triples-rigidified-moduli**, the concrete support and limits are:

- **Scan 042** describes a Brauer–Severi object with a trisection and invokes (H^1(S,\mathfrak S_3)), with a descended involution and associated sections. Some literal source wording and notation remain uncertain.
- **Scan 044** adds a disjoint section s, defines the invariant, and considers the locus where the invariant and its difference from 1 are invertible.
- **Scan 046** describes reconstruction in a normal/integral situation but explicitly asks **“quels i conviennent ??”**. It leaves the unramified-extension and rational-map-extension conditions as questions to express.
- **Scan 047**, although dominated by reused typed algebra text, contains a handwritten marginal diagram with \( (0,1,\infty) \), \( (2,1/2,-1) \), and \( (x',x'') \). It is positive evidence of the associated-trisection discussion and must not be excluded merely because the principal page text is algebra.
- **Scan 048** treats the special invariant values 0 and 1 through reductions to order-2 and order-3 subgroups and gives a quadratic quotient description in another case.
- **Scan 050** starts **“Ceci ne nous a pas donné de façon très explicite de classifier…”**, then writes a torsor/equivariant-coordinate formulation and a complete-local example. This is direct evidence against describing every part of the preceding draft as an already explicit finished classification.

**Intake recommendation from this limited task:** the *topic identification* is confirmed by the frozen text; a fully proved three-way equivalence, precise hypotheses, canonicity, and novelty remain to be checked. The registered span mentions their pp. 41–53, while the present package stops at our scan 050; this report does not claim to have inspected a further continuation. No update to the findings register was made.

## Earlier-context claims that remain unreviewed here

The following should remain attributed to the previous return unless separately checked:

1. **Fourier literature identifications.** CTX-N F1–F4 and F6 cite Stacks results, Mukai, Laumon, and Mumford to compare the manuscript with later theory. This report verifies their *presence and stated scope in the supplied notes*, not the cited publications, their hypotheses, or the identification of the later isomorphisms with the specific map on cote 47, scan 7.
2. **Editorial Fourier calculations.** F5's relative (K)-theory line-factor correction, F7's cone argument, and F8's Tor/exterior-power comparison remain editorial calculations/proposals from the earlier return. F7 and F8 expressly leave the unit-map compatibility open. Likewise, scan 9's Chern-formula discussion contains a “mod torsion” question, not a general integral theorem.
3. **Intermediate-Jacobian identifications.** CTX-N D08–D11 distinguish algebraic representatives, Abel–Jacobi images, and hypothesis-dependent Tate-module comparisons. The named later publications and their precise comparisons were not reopened. In particular, no supplied text identifies the provisional Albanese equivalence in all codimensions merely by choosing a modern name.
4. **Height and positivity comparisons.** D12 is explicitly a comparison in another setting, not a proof of Th. 5 as written; D13 is explicitly an obstruction test, not a proof of positivity of the particular constructed correspondence.
5. **Tau equivalence and Matsusaka.** CTX-N 44:6:1–3 and D14 make the definition of tau essential. The old notes' divisor comparison and proposed contrary evidence under one unrestricted interpretation were not independently verified here. Neither the marginal name nor a modern interpretation licenses changing the programme's words.
6. **Completion faithfulness.** CTX-N 44:3:1–5 and D07 preserve the cancelled status, grading, topology, and unresolved TF qualification. The current cote 62 algebra pages do not remove all of those qualifications.
7. **Other-project and planning claims.** The Hua candidate and WG H9 retain the unchecked status recorded in STATE. A statement tagged “Proved” elsewhere in STATE is still only the return's claim unless an explicit intake/referee qualification says more; unrelated reviewed GT results do not review this Fourier/Jacobian dossier.

## Suggested wording for the final research notes

> The selected cote 62 pages do not supply either a second witness completing cote 47's Fourier compatibility check or an earlier formulation of cote 44, Theorems 1–7. The precise Fourier gap remains the unit-fibre verification of the canonical map in cote 47, scans 7–8; the prior notes F7–F8 explicitly retain it. Cote 62's Lie line and inversion supply a possible dimension-one testing setting, and its completion sheets connect to the separate cancelled draft at cote 44, scan 3. Its positive contribution is instead the explicit elliptic/genus-zero moduli and trisection material. These are findings about the supplied selection, not an archive-wide absence claim. [STATE, WG2 §2.4 #4; CTX-T, cote 47, scans 7–8; cote 44, scans 2–4, 6, 8–9; T62, scans 004, 014–017, 020, 041–050.]


# Appendix A. Literal title and page-count evidence from the frozen TeX

This appendix was requested after the main comparison. It is an independent **literal-text extraction**, not an image audit. Counts concern files and explicit markers, not an inferred number of original physical sheets or a complete archive dossier. The page-number sequence and printed headers are distinct layers.

- Exactly **46 page TeX files**, with scan IDs **002, 004–017, 019–026, 028–050**.
- The inclusive numerical interval 002–050 contains 49 numbers; **003, 018, 027 are excluded**, giving 46 selected files. No content has been inferred for those excluded IDs.
- Exactly one `\scanpage{...}` marker and one `\mspage{...}` marker occur in each selected page file. The encoded `\mspage` value is the scan number minus one throughout this selection; the values present are **1, 3–16, 18–25, 27–49**. This is a property of the current frozen text, not a fresh verification of the image numbers.
- The only overall title in scan 002 is **“Courbes elliptiques”**; scan 004 begins **“Modules des courbes elliptiques”**. The catalogue phrase “généralités - vieille rédaction” and a catalogue total/date in README are contextual metadata, not title words copied from scan 002.

## Exact heading strings

**Scan 002.**

```tex
Courbes elliptiques
```

**Scan 004.**

```tex
\uline{Modules des courbes elliptiques}
```

**Scan 020.**

```tex
\S2. -- \uline{Anneaux} $\mathrm m$-\uline{adiques noethériens}.
1. -- \uline{Restriction de la topologie} $\mathrm m$-\uline{adique à un sous-module}.
```

**Scan 022.**

```tex
4. -- \uline{Modules filtrés complets}.
```

**Scan 026.**

```tex
5. -- \uline{Modules de type fini sur un anneau filtré complet}.
```

**Scan 029.**

```tex
2. \uline{Valuations indépendantes}.
```

**Scan 033.**

```tex
\unsure{3$^\circ$|3} - \uline{Prolongements d'une valuation à une extension algébrique}.
```

**Scan 035.**

```tex
2. - \uline{Application} : \uline{prolongement d'une place à valeurs dans un corps algébriquement clos}.
```

**Scan 045.**

```tex
7. - \uline{Complété d'un module filtré}.
```

## Page-number layers

| Scan | Encoded `mspage` | Literal centred printed header, if present |
|---|---:|---|
| 002 | 1 | — |
| 004 | 3 | — |
| 005 | 4 | — |
| 006 | 5 | — |
| 007 | 6 | — |
| 008 | 7 | — |
| 009 | 8 | — |
| 010 | 9 | — |
| 011 | 10 | — |
| 012 | 11 | — |
| 013 | 12 | — |
| 014 | 13 | — |
| 015 | 14 | — |
| 016 | 15 | — |
| 017 | 16 | — |
| 019 | 18 | — |
| 020 | 19 | `$-\ 20\ -$` |
| 021 | 20 | — |
| 022 | 21 | `$-\ 9\ -$` |
| 023 | 22 | — |
| 024 | 23 | `$-\ 10\ -$` |
| 025 | 24 | — |
| 026 | 25 | `$-\ 11\ -$` |
| 028 | 27 | — |
| 029 | 28 | `$-39-$` |
| 030 | 29 | — |
| 031 | 30 | `$-\ 47\ -$` |
| 032 | 31 | — |
| 033 | 32 | `- 46 -` |
| 034 | 33 | — |
| 035 | 34 | `- 45 -` |
| 036 | 35 | — |
| 037 | 36 | `- 44 -` |
| 038 | 37 | — |
| 039 | 38 | `- 43 -` |
| 040 | 39 | — |
| 041 | 40 | `- 18 -` |
| 042 | 41 | — |
| 043 | 42 | `- 17 -` |
| 044 | 43 | — |
| 045 | 44 | `- 16 -` |
| 046 | 45 | — |
| 047 | 46 | `- 15 -` |
| 048 | 47 | — |
| 049 | 48 | `- 13 -` |
| 050 | 49 | — |


# Appendix B. Literal inventory of self-flagged steps and authorial questions

**Meaning of the labels.** “Deferred/open in this wording” reports the author's visible request; it is not a proof of mathematical incompleteness. “Answered/continued in selected text” reports a textual continuation, not validation of its reasoning. “Exposition” identifies a request about organization or explanation. “Routine proof goal” prevents a normal proof transition being misreported as an unresolved research question. Every quotation below is copied literally from the frozen TeX, including `\unsure`, `\deleted`, and `\inserted` encodings; uncertain readings are not resolved here.

The source list deliberately includes closed questions, cancelled draft goals, bare question marks, and invocations of known arguments. Editorial `\unsure{...}` by itself is **not** counted as an author's question. All locations below are cote 62 and use the page-filename template in the source table.

## F01. Scan 005: Known inputs and a compressed argument

Invoked rather than expanded; the text declares the first assertion proved for nonzero n and known otherwise.

```tex
La formule de RR, où $g=1$, d'où $2g-2=0$, nous montre que \uline{tout faisceau} \deleted{loc. libre} inversible sur $C$, de degré \inserted{relatif} $d\neq0$, est coh. plat, et que sa dimension est \deleted{\unsure{donc}} nulle si $d<0$, et $d\deleted{\unsure{-(g-1)}}$ si $d\geq1$. Donc la première assertion est démontrée pour $n\neq0$, et pour $n=0$ elle est connue par ailleurs, car $\underline L^{\otimes0}=\underline O_C$.
\margin{prop. préliminaire sur un faisceau inversible \unsure{quelconque}}
\inserted{On sait aussi qu'un faisceau inv. sur $C$ de degré relatif $d$ est ample ssi $d>0$, donc $\underline L^{\otimes n}$ est ample ssi $n\geq1$. \deleted{\unsure{Et puisque}}}
```

```tex
Mais \deleted{alors} comme $3>(2g-2)+2=\uline{2g}=2$, un raisonnement connu n'utilisant que RR donne le résultat.
```

## F02. Scan 006: Product-map proof target

Routine proof goal; the alternative direct argument is on scan 007, in the paragraph beginning “Mais on a plutôt intérêt”.

```tex
Notons que $\mathcal E=\varinjlim\mathcal E_n=f_*(\varinjlim\underline L^{\otimes n})$ est une $\underline O_S$-\uline{Algèbre}, dont la connaissance d'ailleurs implique la connaissance de $\underline\Gamma_*^{\unsure{\mathcal E}}(f,\underline L)=\coprod\mathcal E_n$, car $\mathcal E_m\times\mathcal E_n\unsure{\longrightarrow|-}\mathcal E_{m+n}$ est précisément induit par la multiplication de $\mathcal E$. On a, en passant au \unsure{gr. ann.} associé à la filtration croissante donnée, une Algèbre $\coprod_{n\geq0}\underline{\mathcal L}_n$, où les $\underline{\mathcal L}_n\simeq\mathcal E_n/\mathcal E_{n-1}$ pour $n\geq0$, en modifiant pour $n=0$ par $\underline O_S$. Il faut prouver que
\[
\underline{\mathcal L}_n\otimes\underline{\mathcal L}_m\unsure{\longrightarrow|-}\underline{\mathcal L}_{n+m},\qquad n,m\begin{cases}>0\\\neq1\end{cases},\quad\deleted{n,m}
\]
est bien isom., ou encore surjectif, \deleted{\unsure{et pour}} Si $n$ ou $m=0$, \deleted{\unsure{ramenons nous} \illegible{3} \unsure{au voisinage}} c'est trivial, sinon on a $n,m\geq2$, et on voit.
```

## F03. Scan 007: Operations of the tangent sheaf

Deferred definition, explicitly bracketed.

```tex
Considérons les opérations de $\underline T$ sur les germes de fonctions rationnelles sur $C$ [reste à définir], on constate que \deleted{\unsure{$\underline T$}} ces opérations induisent des hom
\[
\underline{\mathcal L}\otimes\underline{\mathcal L}_n\longrightarrow\underline{\mathcal L}_{n+1}\qquad n\geq2
\]
```

## F04. Scan 007: Local verification

Routine proof target continued by the pole-order statement at the top of scan 008; do not list it as an isolated open question.

```tex
On est ramené au cas où $S=\operatorname{Spec}k$, alors c'est une vérification locale : si $D$ est une \deleted{\unsure{diff}} dérivation inv. non nulle en un \inserted{pt $x\in C$} et si $f\neq0$ sur $C$ a en $x$ un pôle d'ordre $n$,
```

## F05. Scan 008: Continuation of that local verification

Textual answer to the preceding target.

```tex
\deleted{non divisible par $p$} alors \deleted{$Df$} $Df$ a en $x$ un pôle d'ordre au plus $n+1$, et égal à $n+1$ ssi $p\nmid n$.
```

## F06. Scan 008: Order of exposition

Relocation note; first word remains uncertain.

```tex
\margin{\unsure{intervertir} avec la prop. 2}
```

## F07. Scan 009: Cancelled rigidification opening

Cancelled draft goal, distinct from a surviving request for a proof.

```tex
\deleted{\uline{Supposons} que l'on se soit donné une rigidification}
```

## F08. Scan 010: Equation defining the embedded curve

The margin requests precision at the unit-multiple argument; the preceding margin gives a primitivity observation.

```tex
on \uline{constate alors} que $\Phi$ est la forme de degré $3$ qui définit \deleted{\unsure{notre}} $C$ dans $P(\mathcal E_3)\simeq P_S^3$. En effet si $\Phi'$ est la forme qui définit $C$, alors $\Phi$ est \uline{un multiple de $\Phi'$}, et \deleted{\unsure{d'une}} c'est un multiple par quelque chose qui est inversible, puisque $\Phi$ est ``non nulle'' en tt pt de $S$ --- un de ses coefficients est $1$ ---.
\margin{\unsure{d'ailleurs, est essentiellement primitive}}
\margin{préciser ce pt cf. intersections complètes}
```

## F09. Scan 011: Smoothness and explicit discriminant

The smoothness criterion is stated immediately; the requested explicit discriminant is left after a dash on this page. Later calculations have their own qualifications.

```tex
Réciproquement, partons d'une équation comme dessus, où les \deleted{$a$}\inserted{coeff. $a,b\ldots$} sont des sections de $\underline O_S$. On sait qu'\deleted{$a$}\inserted{une telle équation} définit un diviseur relatif \inserted{positif} de $P_S^2/S$, soit $C$. Il reste à écrire que c'est là une \uline{courbe simple} sur $S$. On sait qu'il faut pour cela que le discriminant de la forme
\[
\delta(a,b,c,d,e,f)
\]
soit une \uline{unité} partout. Ici le discriminant s'explicite : ---
```

## F10. Scan 012: Alternative account of the group action

Exposition suggestion, not by itself an unsolved theorem.

```tex
[on peut aussi dire --- \unsure{ce sera plus clair}, que $G$ opère sur le \unsure{vecteur} $E_3$, donc dans $\Phi_3(E_3)$, et qu'il laisse invariant le sous-\deleted{module}\inserted{\unsure{schéma}} de \deleted{\unsure{dimension}}\unsure{rang} $6$ des formes qui sont de la forme dite, d'où les opérations de $G$ sur $M$.
```

## F11. Scan 013: Alternative general moduli argument

Comparison with another route; no proof of the general-genus alternative is written here.

```tex
Ainsi, avec une terminologie générale, le foncteur $F$ : ``classes à isom près de courbes elliptiques sur $S$'' est \deleted{\unsure{pro}}-$\mathcal D$-représentable, où $\mathcal D$ désigne la catégorie des morphismes simples surjectifs. Si ce n'était que pour \unsure{obtenir cet énoncé}, on n'aurait pas à se donner tant de mal, \uline{car} on a un raisonnement général qui le donne pour les courbes de genre $g$ \unsure{quelc} (de façon \unsure{triangulaire} \unsure{quotient} par un groupe projectif---).
```

## F12. Scan 015: Limits and next normalizations

Tentative claim about fewer parameters; forward plan for characteristic restrictions.

```tex
Il ne semble pas qu'on puisse obtenir des normalisations locales sans \deleted{\unsure{type}} restriction de car. qui ferait intervenir moins de paramètres, [si on veut qu'elle soit subordonnée à la descente \deleted{\unsure{de}} par morphismes plats, ou \unsure{à|m.} simples]. Si on admet des ext. de base finies et plates, on peut pousser la normalisation plus loin en exigeant que $\delta(b,c,d,e,f)=1$ i.e. \inserted{(intrinsèquement)} se donner des trivialisations de $\unsure{\mathcal L|L}$ \deleted{compatibles} définies par des sections $\unsure{\lambda|D}$ dont la puissance $12$.ième (\unsure{ou même} $24$.ième) est \inserted{$\delta^{-1}$, où $\delta$ est} le discriminant. On va \deleted{\unsure{en ce}} donner des \deleted{\unsure{les}} normalisations plus poussées en car $\neq2$, puis en car. $\neq3$, puis on verra.
```

## F13. Scan 017: Which normalized equation?

The scan asks a question whose algebraic answer is present on scan 016 (“Transformons…” through the boxed equation). The scan order and argument order must not be conflated.

```tex
Quelle est la normalisation correspondante de l'équation de $C$ ?
```

## F14. Scan 016: Recorded answer associated with the normalization question

Textual calculation available in the selected file; no mathematical correction is made.

```tex
Transformons l'équation
\[
x^2=y^3+\unsure{\dot a|a}xy+by^2+cx+dy+e
\]
par $s$, et en rappelant que $sx=-x$, $sy=y$, on trouve
\[
x^2=y^3\unsure{-|+}axy+by^2-cx+dy+e
\]
et en comparant on trouve $a=c=0$, donc l'équation ici se met sous la forme
\[
\boxed{x^{\unsure{2|3}}=y^{\unsure{3|2}}+ay^2+by+c}
\]
avec comme condition $\delta(a,b,c)\neq0$, qui ici ne fait qu'exprimer que les solutions de $P(y)=y^3+ay^2+by+c$ sont distinctes en tt pt de $S$.
```

## F15. Scan 019: Geometric check

Explicit verification request next to invariant/Kummer notes.

```tex
\margin{\uline{à vérifier} \uline{\unsure{géométriquement}}}
```

## F16. Scan 020: Artin–Rees proof reduction

Routine goal in the reused typed text, followed on this selected page by the graded-algebra setup; the page ends mid-proof.

```tex
Le théorème 1 sera une conséquence du résultat plus précis que voici :

\uline{Lemme d'Artin-Rees} \unsure{--} \uline{Soient} $A$ \uline{un anneau commutatif noethérien}, $\mathrm m$ \uline{un idéal de} $A$, $E$ \uline{un} $A$-\uline{module de type fini et} $F$ \uline{un sous-module de} $E$. \uline{Pour tout entier} $k$ \uline{suffisamment grand on a}
\[
\mathrm m^pE\cap F=\mathrm m^{p-k}(\mathrm m^kE\cap F)\qquad\uline{\text{pour tout}}\ p\geq k.
\]
Il suffit évidemment de prouver l'inclusion\qquad --
\[
\mathrm m^pE\cap F\subset\mathrm m^{p-k}(\mathrm m^kE\cap F),
\]
puisque l'inclusion opposée est triviale.

Pour cela considérons dans l'anneau de polynômes $A[X]$ le sous-anneau $A'$ formé des polynômes $\sum a_pX^p$ tels que $a_p\in\mathrm m^p$ pour tout $p$. Il est clair qu'en tant qu'algèbre sur $A$, $A'$ est engendré par les $a_iX$ où $a_i$ est un système de générateurs de $\mathrm m$ ; par suite $A'$ est un anneau noethérien, par ailleurs gradué.
```

## F17. Scan 021: Discriminant question mark

Explicit question mark after a boxed draft formula; retain the cancelled/uncertain coefficient.

```tex
\boxed{\Delta=\deleted{\unsure{9|4}}b^3-27c^2}\quad ?
```

## F18. Scan 022: General-topology margin

Marginal qualification; the wording itself is uncertain.

```tex
\margin{\unsure{fait général} pour les top\unsure{.} métrisables\quad !\quad\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0.2,0.9) .. controls (-0.1,0.5) and (-0.1,-0.5) .. (0.15,-0.9);\end{tikzpicture}}}
```

## F19. Scan 024: Coefficientwise topology

Exposition note; words remain under uncertainty macros.

```tex
\margin{\unsure{Dire que la} \unsure{top. est} \unsure{celle de} la \unsure{conv. simple} des coefficients.}
```

## F20. Scan 026: Formal-series proof conclusion

Closed proof wording: the text explicitly says this proves the proposition.

```tex
Considérant alors la série formelle $y=\sum a_nX^n$, la relation précédente montre que l'on a
\[
y-\sum_{i=0}^{i=i_p}y_i\in\mathrm n^p
\]
ce qui prouve que la série $\sum y_i$ converge vers $y$, d'où la proposition.

\uline{Corollaire} -- \uline{Soit} $A$ \uline{un anneau commutatif}. \uline{L'anneau de séries formelles} $A[[X_1,\ldots,X_r]]$ \uline{filtré par les puissances de l'idéal} $(X_1,\ldots X_r)$, \uline{est séparé et complet}.
```

## F21. Scan 028: Renaming generators

Marginal organizational proposal with literal question marks.

```tex
\margin{\unsure{renommer}\quad
\[\left\{\begin{array}{l}\lambda t=1-\unsure{t}\\\mu t=\dfrac t{\unsure{t-1}}\\\nu t=\unsure{1/t}\\?\ ?\end{array}\right.\]}
```

## F22. Scan 029: Stronger valuation observation

Explicit editorial aside; not an unfinished research problem.

```tex
[En fait, on a $A=B_{\underline{\mathrm p}}$ en vertu de la prop.1, mais on s'en fout.]
```

## F23. Scan 030: Normalizer claim

Explicit “Prouver” margin. The literal statement includes an uncertain alphabet symbol.

```tex
\margin{Prouver : le normalisateur de $\mathfrak S_3$ dans $\operatorname{Aut}P^1_S$ est $\mathfrak S_3\times(\unsure{\mathbb Z}/2)$}
```

## F24. Scan 031: Valuation proof targets

Routine goals. The first paragraph ends in contradiction; the next cardinality argument is still in progress at the selected page end.

```tex
Montrons d'abord que l'on ne peut pas avoir $A_i\supset A_j$ si $i\ne j$. En effet, d'après ce que l'on a vu au \S4, le groupe $\Gamma_i$ s'identifierait à un groupe quotient $\Gamma_j/H$, où $H$ est un sous-groupe isolé de $\Gamma_j$ ; puisque l'application canonique $\Gamma\longrightarrow\Gamma_j\longrightarrow\Gamma_j/H=\Gamma_i$ est une injection, on a $\Gamma\cap H=\{0\}$ dans $\Gamma_j$, ce qui montre que $H$ est isomorphe à un sous-groupe de $\Gamma_j/\Gamma$ ; comme ce dernier groupe est fini (prop.1), on a $H=0$, et les valuations $v_i$ et $v_j$ sont équivalentes, d'où $A_i=A_j$ contrairement à l'hypothèse $i\ne j$.

Montrons maintenant que le nombre des $A_i$ est \unsure{'} $\leqslant n$. Supposons donc qu'il existe $s$ anneaux $A_i$ distincts, avec $s>n$. D'après le cor. 2 à la prop.2 du \S6, (qui est applicable, en vertu de ce que l'on vient de voir), il existe des éléments $x_i\in L$, $1\leqslant i\leqslant s$, tels que $v_i(x_i)=0$ et $v_j(x_i)>0$ pour $i\ne j$. Montrons que les $x_i$ sont linéairement indépendants sur $K$, ce qui fournira la contradiction cherchée. Supposons que l'on ait une relation linéaire non triviale :
\[
\sum a_ix_i=0,\text{ avec }a_i\in K.
\]
Soit $a_j$ celui des $a_i$ dont la valuation est minimum ; quitte à multiplier les $a_i$ par $a_j^{-1}$ on peut supposer que $a_j=1$. On a alors une relation :
```

## F25. Scan 032: Three quotient sections

Explicit “à expliciter” flag. Scans 036–040 subsequently give the quotient diagram and formulas; the request should not be detached from that continuation.

```tex
On suppose tjrs qu'il n'y a pas de pt $s$ de car. 2 ou 3 dans $S$. Alors \deleted{$\unsure{\mathfrak S_3}$ opère} $\mathfrak S_3\times \unsure{Z|\mathbb Z}_2$ opère ``tamely'' sur $P^1_S$ [en fait, il est compatible avec la fibration $P^1_S\to S$, et opère ``tamely'' sur les fibres\ldots] Le quotient \inserted{par un groupe ou un ss-groupe} \deleted{\unsure{il est|qui est}} \inserted{\unsure{est isomorphe}} encore à $P^1_S$ [car il est \uline{lisse} sur $S$, et rationnel sur $S$ d'après Lüroth]. Les schémas de pts fixes $(0,1,\infty)$ $(2,-1,\tfrac12)$ $(\bar S=x',x'')$ --- qui sont disjoints, et chacun stable sous $\mathfrak S_3$, qui \deleted{\unsure{y}} \inserted{lui-même} opère de façon \deleted{\unsure{simplement}} transitive sur chaque fibre, donnent dans $P^1_S/\mathfrak S_3$ trois \uline{sections} distinctes [à expliciter\ldots] qu'on peut utiliser pour identifier $P^1_S/\mathfrak S_3$ à $P^1_S$ avec les sections $\infty,0,1$. De même, \deleted{\unsure{le schéma du revt}} $P^1_S/(\mathbb Z/3)$ est muni d'abord de deux sections qui correspondent à $(0,1,\infty)$ et $(2,-1,\tfrac12)$, et qui
```

## F26. Scan 033: Valuation lemma conclusion

Closed wording for the maximal-place argument continued from scan 035; it ends “la place cherchée”.

```tex
l'application identique $k\longrightarrow k$, on a $\Omega\ne\unsure{\varnothing}$. Soit $(F,\psi)$ un élément maximal de $\Omega$. Montrons d'abord que $L$ est \uline{algébrique} sur $F$ ; sinon, en effet, il existerait $X\in L$ transcendant sur $F$, et $L$ contiendrait $F'=F(X)$ ; en composant la place $\lambda:F(X)\longrightarrow F$ donné par $f\longrightarrow f(0)$ avec la place $\psi:F\longrightarrow k$, on obtiendrait une place de $F'$ qui serait l'identité sur $k$, contrairement au caractère maximal de $(F,\psi)$. Donc $L/F$ est algébrique. Soit Alors $\psi'$ une place de $L$ à valeurs dans une extension $k'$ de $k$ qui prolonge $\psi$ ; une telle extension existe d'après la prop.4 du \S\ 2 ; en vertu de la prop.3, ci-dessus, $\psi'(L)$ est algébrique sur $\psi(F)=k$, donc $\psi'(L)=k$, \unsure{pui sque} $k$ est algébriquement clos, et la place $\psi'$ est la place cherchée.
```

## F27. Scan 033: Placement and retention of a proposition

Explicit editorial question about rearrangement and whether to keep a remnant of earlier drafts; names Samuel.

```tex
[Ce n$^\circ$ pourrait remonter bien plus tôt à condition de donner une démonstration directe de la prop.3, ce qui n'est pas bien difficile. Est-ce que cela en vaut la peine ? La prop.4 est un résidu des rédactions antérieures (où elle était démontrée en même temps que le th. d'extension des valuations) ; le rédacteur ne pense pas qu'elle ait jamais servi à quoi que ce soit, et ne l'a gardée que sur les instances de Samuel ; il laisse à son Maître le soin de décider son sort (de la proposition, pas de Samuel)]
```

## F28. Scan 035: Placement of a corollary

Alternative proof/placement comment.

```tex
[On pourrait aussi déduire ce corollaire directement de la prop.1, mais il me paraît plus naturel de le laisser en compagnie des cor.2 et 3].
```

## F29. Scan 035: Existence of a place

Routine reduction to the following lemma; the maximality proof continues in the selected scan 033.

```tex
D'après la prop.3 du \S\ 2, il existe une place $\varphi$ de $K$ à valeurs dans une extension $L$ de \inserted{$k$} qui prolonge $g$. Si $\psi$ est une place de $L$ à valeurs dans $k$, qui est l'identité sur $k$, la place composée $\theta=\psi\circ\varphi$ répond évidemment à la question. Tout revient donc à démontrer l'existence de $\psi$, autrement \unsure{doit|dit} à prouver le lemme suivant :

\uline{Lemme} 1 - \uline{Pour toute extension} $L$ \uline{d'un corps algébriquement clos} $k$, \uline{il existe une place} $\psi$ \uline{de} $L$ \uline{à valeurs dans} $k$ \uline{qui est l'identité sur} $k$.

Soit $\Omega$ l'ensemble des couples $(F,\psi)$, où $F$ est une sous-extension de $L$, et $\psi$ est une place de $F$ à valeurs dans $k$ qui est l'identité sur $k$. Si l'on ordonne \inserted{$\Omega$} par la relation de prolongement, on voit tout de suite que $\Omega$ est inductif ; comme $\Omega$ contient le couple formé de $k$ et de
```

## F30. Scan 036: Determining f and g; extending the formula

The calculation supplies g, but the underlined extension sentence explicitly asks for a meaning and justification on all of P1.

```tex
Pour déterminer explicitement $f$ et $g$, on procède ainsi. [On \deleted{\unsure{se}} peut supposer que \deleted{$S=\operatorname{Spec}(\unsure{\mathbb Z_m}[2^{-1},3^{-1}])$} \inserted{$S=\operatorname{Spec}(A)$, $A=\mathbb Z[2^{-1},3^{-1}]$} \deleted{\unsure{\{}} puisque toute la situation provient par image inverse d'une situation sur $\operatorname{Spec}(A)$]. La restriction de $g$ à $P^1_S-(\infty)-(0)$ est alors un \inserted{$S$-}morphisme de $G_m$ dans lui-même, donc est de la forme $t\to\lambda t^n$, où $n\in\mathbb Z$, et $\lambda\in H^0(S,\underline O_S^*)$. Comme $g(\infty)=\infty$, on a $n>0$, et comme $g$ est \inserted{un rev.} d'ordre 2, on a $n=2$. D'autre part \deleted{$\lambda$} \inserted{$g(1)=1$, d'où $\lambda=1$} \deleted{\unsure{$\in A$, donc de la forme $2^\alpha3^\beta$}.}
\[
(9)\qquad r=g(s)=s^2
\]
\uline{Cette formule est valable sur tout $P^1$} [lui donner un sens, et justifier cette assertion\ldots]
```

## F31. Scan 037: Ordered-group argument

The bijection proof explicitly closes before the following organizational question.

```tex
Posons pour simplifier les notations, $G=\Gamma_v$, $G'=\Gamma_{v'}$, et soit $S$ (resp. $S'$) l'ensemble des sous-groupes isolés de $G$ (resp. $G'$). Nous allons montrer que l'application $H'\longrightarrow H'\cap G$ est une bijection de $S'$ sur $S$, ce qui établira évidemment que $v$ et $v'$ ont même rang. Tout d'abord, il est clair que $H'\in S'\Longrightarrow H'\cap G\in S$ ; si de plus $H'_1\subset H'_2$ sont deux sous-groupes isolés de $G'$ tels que $H'_1\cap G=H'_2\cap G$, le groupe quotient $H'_2/H'_1$ est isomorphe à un sous-groupe de $G'/G$ ; comme le premier groupe est un groupe totalement ordonné et que le \unsure{sedond|second} est un groupe de torsion d'après la prop.2, il s'ensuit que $H'_2/H'_1=0$, et l'application considérée est injective. Enfin, si $H$ est un sous-groupe isolé de $G$, soit $H'\subset G'$ l'ensemble des $x\in G'$ tels qu'il existe $h\in H$ avec $-h\leqslant x\leqslant h$ ; on vérifie immédiatement que $H'$ est un sous-groupe isolé de $G'$ tel que $H'\cap G=H$, ce qui achève la démonstration.

[Est-il nécessaire de dégager \unsure{lo|le} ou les lemmes sur les groupes ordonnés que l'on vient \unsure{en'fait|en fait} de démontrer ?]
```

## F32. Scan 039: Linear-independence proof conclusion

Closed wording at the end of the displayed contradiction argument.

```tex
Comme $b_\beta=1$, ceci contredit l'hypothèse faite sur les $y_\alpha$, et achève la démonstration.
```

## F33. Scan 040: Action on the quotients

Explicit question answered by the recorded formula on the same page, with a final statement that a further proof would be easy; retain both layers.

```tex
Comment opère $\sigma$ dans les quotients ?
\margin{\diagram{\begin{tikzcd}[row sep=large]
\sigma\quad P^1\arrow[d,"f"]\\
\sigma'\quad P^1\arrow[d,"g"]\\
\sigma''\quad P^1
\end{tikzcd}}}
On voit que $\sigma'(\infty)=0$, $\sigma'(0)=\infty$, $\sigma'(1)=1$, d'où mêmes formules pour $\sigma''$, d'où
\[
\deleted{\sigma'(t)=1/t}
\]
\deleted{et d'autre part}
\[
(11)\qquad\sigma'(t)=\sigma''(t)=1/t
\]
et il \unsure{serait} facile de \unsure{prouver} ces équations \unsure{pour $\sigma$ dans ce dernier cas} (p.ex.).
```

## F34. Scan 042: Associated trisection and descent

Explicit “à préciser” and “par descente” ellipses; these qualify reconstruction/descent in the literal wording.

```tex
Soit $S$ un schéma de base, et soit $X$ un schéma de Br. Severi sur $S$ muni d'une \uline{\unsure{trisection}} non ramifiée $X'$, i.e. un ss-schéma \inserted{fermé} de $X$ qui est non ramifié sur $X$, d'ordre 3 sur $X$. Un tel truc peut être considéré comme un objet à \unsure{schém.} structural $\mathfrak S_3$, opérant sur $P^1_S$ comme il a été dit. La classification de tels objets est donc la même que la classification dans un $H^1(S,\mathfrak S_3)$ des revêtts \inserted{gal.} \uline{non ramifiés} de groupe $\mathfrak S_3$ de $S$. De plus, $\sigma$ définit dans $X$ un $S$-automorphisme \inserted{involutif} \unsure{intr.} $\unsure{\sigma_S|\sigma}$ qui transforme $X'$ en un $X''$, dit \uline{associé} à $X'$. Évidt, si on partait de $(X,X'')$, on aurait le même $\sigma$, et \unsure{on restitue} $X'$ [à préciser\ldots]. De plus, on obtient [par descente\ldots] une \uline{bisection}, non ramifiée \deleted{\unsure{[en ses points}} en les pts de $S$ de car. $\ne2,3$]..... On peut passer au quotient, \deleted{\unsure{f}} par $\mathfrak S_3$, \deleted{\unsure{puis}} on trouve \unsure{par} :
```

## F35. Scan 043: Topological qualification

Uncertain marginal word whose alternative contains a question mark; this is not secure evidence of a standalone authorial question.

```tex
\margin{\figure{\begin{tikzpicture}\node[rotate=20] at (0,0) {\unsure{topologt|topol.?}};\draw[->] (.65,.3)--(1,.6)--(1.25,.65);\end{tikzpicture}}}
```

## F36. Scan 044: Categorical derivation

Bracketed request continues at the top of scan 046.

```tex
Supposons que l'invariant $\unsure{j|i}$ ne prenne nulle part les valeurs $0,1$ i.e. soit inversible, ainsi que $\unsure{j|i}-1$. Alors son image inverse dans $P^1_S$ \deleted{\unsure{x}} de $p:S\to P^1_S$ définit un \deleted{section} \inserted{revêtement} \uline{galoisien} \uline{de} $S$, \uline{non ramifié}, \uline{de groupe} $\mathfrak S_3$, \deleted{\unsure{et}} \uline{et c'est celui qui définit} $X$. [\unsure{À déduire des formalismes|À déduire les formules}
```

## F37. Scan 046: Continuation of categorical request

Closes the bracket begun on scan 044, before the reconstruction assertion.

```tex
catégoriques généraux \ldots\ ].

Donc en ce cas, l'invariant suffit à réconstituer \deleted{\unsure{toute}} la situation $(X,X',s)$.
```

## F38. Scan 046: Which invariants occur?

Explicit unresolved admissibility question followed by two conditions still to express.

```tex
Donc ici encore, \uline{$i$ permet de tt reconstituer}. Ici cependant, \unsure{se pose la} question : quels $i$ conviennent ??

Il faut exprimer (i) qu'une certaine extension de corps -- de degré $3$ -- du corps des fonctions de $X$ est non ramifié sur $X$ (ii) Qu'une certaine application rationnelle de $X$ qui s'en déduit est partout définie \ldots
```

## F39. Scan 047: Comparison of proofs and marginal question mark

The proof-comparison comment and bare question mark are separate flags; neither identifies a new theorem without its local context.

```tex
(La démonstration précédente ne semble pas présenter d'avantage très décisif par rapport à la démonstration classique \ldots)
```

```tex
\margin{?}
\uline{Corollaire} 2 -- \uline{Soit} $A$ \figure{\begin{tikzpicture}[baseline=(n.base)]\node[draw,ellipse,inner sep=2pt] (n) {\uline{un anneau commutatif noethérien}};\end{tikzpicture}}. \uline{L'anneau de séries formelles} $A[[X]]$ \uline{est noethérien}.
```

## F40. Scan 049: Associated-graded surjectivity

Routine proof goal followed immediately by its explanation; do not promote it to an open research question.

```tex
de la proposition précédente il suffit pour cela de faire voir que l'homomorphisme associé $G(u)$ est surjectif, autrement dit que pour tout $x\in E_n$ il existe des $a_i\in A_{n-p_i}$ tels que l'on ait $x\equiv a_ix_i\pmod{E_{n+1}}$ ; mais cela signifie précisément que les $\tilde x_i$ engendrent le $G(A)$-module $G(E)$ : en effet, si $\tilde x\in G_n(E)$, on peut trouver des $\tilde a_i\in G(A)$ tels que $\tilde x=\sum\tilde a_i\tilde x_i$, et cette relation subsiste si l'on remplace $\tilde a_i$ par sa composante de degré $n-p_i$.

\uline{Corollaire} 1 -- \uline{Soit} $E$ \uline{un module filtré séparé sur un anneau filtré complet} $A$; \uline{Si} $G(E)$ \uline{est} \inserted{un} $G(A)$-\uline{module de type fini} (resp. \uline{noethérien}) \uline{alors} $E$ \uline{est un} $A$-\uline{module de type fini} (resp. \uline{noethérien}).

Soit en effet $F$ un sous-module de $E$, et munissons le de la filtration induite ; $G(F)$ est alors un sous-module homogène du $G(A)$-module gradué $G(E)$ ; si $G(F)$ est de type fini, on peut l'engendrer à l'aide d'éléments homogènes en nombre fini -- il suffit pour le voir de prendre les composantes homogènes d'un système fini de générateurs de $G(F)$ ; en considérant des;éléments de $F$ dont ces générateurs sont les formes initiales on voit, à l'aide de la Proposition 7, que $F$ est lui-même un module de type fini, d'où immédiatement le corollaire.
```

## F41. Scan 050: Explicitness of classification

Author explicitly says the preceding work has not supplied a very explicit classification.

```tex
Ceci ne nous a pas donné de façon très explicite de classifier les ``courbes \inserted{\unsure{simples}} de genre $0$'' sur $S$, munies d'une section et d'une trisection non ramifiée, disjointes
```

## F42. Scan 050: Functoriality label

Literal positive marginal label, to be distinguished from the later negative label.

```tex
\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node[rotate=35] at (-.8,0) {fonctoriel};\draw (0,2.5) .. controls (0.15,1.2) and (.15,-.8) .. (0,-1.5);\end{tikzpicture}}}
```

## F43. Scan 050: Nonfunctoriality and the complete-local example

Negative marginal label and noncanonical qualification in the example. Their exact attachment is for the primary reader to inspect; this extraction does not infer it from layout.

```tex
\margin{\uuline{non} \uline{fonctoriel}}
\uline{Exemple} $S=\operatorname{Spec}(O)$, $O$ anneau local \uline{complet} à corps résiduel $\mathrm{alg.}^{\mathrm t}$ clos \deleted{\unsure{(car. $\ne2,3$)}} \inserted{(de car. $\ne2,3$)}.

Alors \deleted{$\unsure{X\simeq P^1_S}$} $\pi_1(S)=0$, donc la situation équivaut, \inserted{[\unsure{Donn. non canoniq.|Donn. non canonique} \unsure{par} \unsure{quoi}]} à la donnée d'un $t\in O^*$ tel que \deleted{$\unsure{t(t-1)\in\mathbb Z}$} $t(t-1)\in O^*$, étant entendu que $t,t'$ donnent des \unsure{représ.} isomorphes \deleted{\unsure{si et}} s. s. s. $t'$ est de la forme \inserted{$\bar\sigma(t)\quad\sigma\in\mathfrak S_3$.}
```


## F44. Scan 005: Preliminary proposition

Explicit expository instruction in the margin; the qualifier remains uncertain.

```tex
\margin{prop. préliminaire sur un faisceau inversible \unsure{quelconque}}
```

## F45. Scan 017: Characteristic-free action on E2

The surviving text says “on le verra.” This is distinct from the closed normalization question later on the same page.

```tex
Notons qu'il y a dans $C$ un $S$-automorphisme canonique de symétrie, car $C$ est un schéma abélien sur $S$. Cet automorphisme \inserted{est d'ordre $2$, il} opère sur les $\mathcal E_i$ [de façon compatible avec les structures, multiplications \inserted{et les opérations de $\mathcal L$ sur $\mathcal E_\infty$}] et induit sur $\mathcal L$ le chgt de signe.
$s$ opère trivialement dans $\mathcal E_2$ [c'est ainsi \unsure{sans|sous} la condition qu'on vient de faire, on le verra], et il existe un supplémentaire unique \inserted{$L_3$} de $\mathcal E_2$ dans $\mathcal E_3$ où $s$ opère par symétrie, \deleted{\unsure{le}} qui est aussi égal à $\mathcal L\cdot \mathcal E_2$, on le note $L_3$.
\margin{N.B. la \unsure{considération} de $C\longrightarrow P(\mathcal E_2)$ et de la \unsure{différentielle} de ce morphisme nous donne (sans restriction de car) un morphisme
\diagram{\begin{tikzcd}\unsure{\mathcal L|L}^{\otimes3}\arrow[r,"\unsure{\partial|\vartheta}"]&\mathcal E_3\end{tikzcd}}
\unsure{compatible avec tt changement de base $S$}.}
```

## F46. Scan 030: Bad-characteristic exceptions

Marginal wording is uncertain; do not reconstruct a more precise question from the extraction.

```tex
\margin{\unsure{les except\textsuperscript{ns} qu'il y a pour car. $2$ ou $3$ de $S$}\quad\figure{\begin{tikzpicture}\draw (0,0)--(0,1.6);\end{tikzpicture}}}
```

# Appendix C. Complete literal cancellation inventory

This appendix extracts **every outermost `\deleted{...}` block** in the selected frozen page files, preserving nested cancellations inside their containing block. It therefore includes small word/formula edits as well as cancelled mathematical drafts. It is a completeness aid for the primary reader, not a claim that every deletion was a self-identified gap. In particular, the cancelled Proposition 1 on scan 004, the long cancelled corollary discussion on scan 008, the cancelled equation construction on scan 009, and the cancelled symmetry/complement assertions on scan 017 must not be silently promoted to final assertions. Surviving replacements are in the surrounding source file and in some of the quotations above.

## Scan 004: 5 outermost cancellations

**D004.01**

```tex
\deleted{fibré}
```

**D004.02**

```tex
\deleted{fonctions}
```

**D004.03**

```tex
\deleted{$s^*(\underline L)\simeq$}
```

**D004.04**

```tex
\deleted{\uline{Proposition 1} les $L^n$ $(n\in\mathbb Z)$ sont \unsure{cohomolgt|cohomologt} plats en \unsure{ttes|toute} dimension.}
```

**D004.05**

```tex
\deleted{\unsure{un}}
```

## Scan 005: 11 outermost cancellations

**D005.01**

```tex
\deleted{\unsure{+1}}
```

**D005.02**

```tex
\deleted{\unsure{Le}}
```

**D005.03**

```tex
\deleted{\unsure{très}}
```

**D005.04**

```tex
\deleted{pour}
```

**D005.05**

```tex
\deleted{loc. libre}
```

**D005.06**

```tex
\deleted{\unsure{donc}}
```

**D005.07**

```tex
\deleted{\unsure{-(g-1)}}
```

**D005.08**

```tex
\deleted{\unsure{Et puisque}}
```

**D005.09**

```tex
\deleted{Comme $\underline L$ est de degré relatif $1>0$, il est ample, \unsure{par suite} \unsure{les} $\underline L^{\otimes n}$ est très ample pour $n\unsure{\gg|>}0$.}
```

**D005.10**

```tex
\deleted{Mais alors D'ailleurs, comme $\underline L$ est engendré loc. par ses sections}
```

**D005.11**

```tex
\deleted{alors}
```

## Scan 006: 10 outermost cancellations

**D006.01**

```tex
\deleted{\unsure{hom}}
```

**D006.02**

```tex
\deleted{\unsure{locale}}
```

**D006.03**

```tex
\deleted{Le faisceau}
```

**D006.04**

```tex
\deleted{\unsure{$\mathcal L_0=\underline O_S$}}
```

**D006.05**

```tex
\deleted{est isomorphe à $\mathcal L^{\otimes\unsure{k}}$, et $\mathcal E_{n+1}/\mathcal E_n$ est isomorphe à $\mathcal L^{\otimes n}$.}
```

**D006.06**

```tex
\deleted{\unsure{faisant de}}
```

**D006.07**

```tex
\deleted{\unsure{une}}
```

**D006.08**

```tex
\deleted{n,m}
```

**D006.09**

```tex
\deleted{\unsure{et pour}}
```

**D006.10**

```tex
\deleted{\unsure{ramenons nous} \illegible{3} \unsure{au voisinage}}
```

## Scan 007: 3 outermost cancellations

**D007.01**

```tex
\deleted{\unsure{$\underline T$}}
```

**D007.02**

```tex
\deleted{\unsure{est}}
```

**D007.03**

```tex
\deleted{\unsure{diff}}
```

## Scan 008: 4 outermost cancellations

**D008.01**

```tex
\deleted{non divisible par $p$}
```

**D008.02**

```tex
\deleted{$Df$}
```

**D008.03**

```tex
\deleted{\uline{Corollaire 1} Si $k(s)$ est de car. nulle, alors
\[
\underline{\mathcal L}\otimes\underline{\mathcal L}_n\simeq\underline{\mathcal L}_{n+1}\quad\text{pour tt }n\geq2,
\]
donc
\deleted{$\underline{\mathcal L}_3\otimes\mathcal L\otimes\underline{\mathcal L}_2,\ \mathcal L_4$}
\inserted{$\mathcal L_4\simeq\mathcal L_2\otimes\mathcal L^2$}
\[
\mathcal L_n\simeq\mathcal L^{n-2}\otimes\mathcal L_2,
\]
\deleted{donc} pour $n\geq2$, \deleted{donc \unsure{on a} $\mathcal L_2\simeq$}

\uline{Corollaire 2} Si $k(s)$ est de car $p\neq2$, alors
\[
\deleted{\unsure{\underline{\mathcal L}_3\simeq\mathcal L_2\otimes\mathcal L}},\quad\underline{\mathcal L}_4\simeq\underline{\mathcal L}_3\otimes\mathcal L,\quad\mathcal L_6\simeq\underline{\mathcal L}_5\otimes\underline{\mathcal L}\quad\text{etc}
\]
[$\underline{\mathcal L}_{2n}=\underline{\mathcal L}_{2n-1}\otimes\mathcal L$ si $n\geq\unsure{2}$] enfin
\[
\mathcal L_2^{\unsure{2}}\simeq\mathcal L^{\otimes2}
\]}
```

**D008.04**

```tex
\deleted{Puisque}
```

## Scan 009: 7 outermost cancellations

**D009.01**

```tex
\deleted{diviseur}
```

**D009.02**

```tex
\deleted{De plus, comme}
```

**D009.03**

```tex
\deleted{\uline{Supposons} que l'on se soit donné une rigidification}
```

**D009.04**

```tex
\deleted{``droite \unsure{des points de} \unsure{l'infini}''}
```

**D009.05**

```tex
\deleted{trivialisation}
```

**D009.06**

```tex
\deleted{par des coordonnées $z,y,x$}
```

**D009.07**

```tex
\deleted{Alors la forme $\varphi$ (définie à \unsure{unité} \deleted{\unsure{homothétie}} \inserted{multiplication près par \unsure{u}}) prend la forme [où on remplace $z$ par $1$]
\[
ax^{\unsure{2|3}}+by^3+cxy+dy^2+ex+fy+g=0
\]
\margin{$x^3\quad y^2$}
\inserted{où $y$ définit un \unsure{suppl.} de $\mathcal E_1$ dans $\mathcal E_2$ et $x$ de $\mathcal E_2$ dans $\mathcal E_3$}}
```

## Scan 010: 8 outermost cancellations

**D010.01**

```tex
\deleted{qui est aussi la relation (unique, \inserted{à \uline{unité près}}, \unsure{que vérifie aussi bien à priori}) \unsure{vérifiée par}}
```

**D010.02**

```tex
\deleted{\unsure{de même $\mathcal E_3$, $y^3$}}
```

**D010.03**

```tex
\deleted{\unsure{$\mathcal E_3$}}
```

**D010.04**

```tex
\deleted{Cette équation}
```

**D010.05**

```tex
\deleted{\unsure{la}}
```

**D010.06**

```tex
\deleted{\unsure{z}}
```

**D010.07**

```tex
\deleted{\unsure{notre}}
```

**D010.08**

```tex
\deleted{\unsure{d'une}}
```

## Scan 011: 6 outermost cancellations

**D011.01**

```tex
\deleted{$a$}
```

**D011.02**

```tex
\deleted{$a$}
```

**D011.03**

```tex
\deleted{\unsure{avec}}
```

**D011.04**

```tex
\deleted{``base adaptée''}
```

**D011.05**

```tex
\deleted{``unité''}
```

**D011.06**

```tex
\deleted{Faisons opérer \unsure{dessus|dans}}
```

## Scan 012: 4 outermost cancellations

**D012.01**

```tex
\deleted{\unsure{puis schéma en groupes} $G$, de type fini sur $\mathbb Z$, qui \deleted{\unsure{repr.}} est représenté matriciellement par}
```

**D012.02**

```tex
\deleted{\unsure{X^2}+AXY^2}
```

**D012.03**

```tex
\deleted{module}
```

**D012.04**

```tex
\deleted{\unsure{dimension}}
```

## Scan 013: 4 outermost cancellations

**D013.01**

```tex
\deleted{\unsure{donc}}
```

**D013.02**

```tex
\deleted{fid. plat}
```

**D013.03**

```tex
\deleted{sur}
```

**D013.04**

```tex
\deleted{\unsure{pro}}
```

## Scan 014: 8 outermost cancellations

**D014.01**

```tex
\deleted{Cela}
```

**D014.02**

```tex
\deleted{[}
```

**D014.03**

```tex
\deleted{\unsure{formé}}
```

**D014.04**

```tex
\deleted{\unsure{triplets}}
```

**D014.05**

```tex
\deleted{La fixation de la structure ainsi \unsure{conduit à une équation}}
```

**D014.06**

```tex
\deleted{i.e.}
```

**D014.07**

```tex
\deleted{\unsure{précédent}}
```

**D014.08**

```tex
\deleted{prend alors la forme}
```

## Scan 015: 5 outermost cancellations

**D015.01**

```tex
\deleted{\unsure{type}}
```

**D015.02**

```tex
\deleted{\unsure{de}}
```

**D015.03**

```tex
\deleted{compatibles}
```

**D015.04**

```tex
\deleted{\unsure{en ce}}
```

**D015.05**

```tex
\deleted{\unsure{les}}
```

## Scan 016: 10 outermost cancellations

**D016.01**

```tex
\deleted{\unsure{le schéma}}
```

**D016.02**

```tex
\deleted{s'identifie}
```

**D016.03**

```tex
\deleted{est}
```

**D016.04**

```tex
\deleted{isomorphe}
```

**D016.05**

```tex
\deleted{\unsure{faisceau inverse}}
```

**D016.06**

```tex
\deleted{fibré \unsure{qui est} loc. libre}
```

**D016.07**

```tex
\deleted{\unsure{de rang un}}
```

**D016.08**

```tex
\deleted{et}
```

**D016.09**

```tex
\deleted{\unsure{dans les fibres}}
```

**D016.10**

```tex
\deleted{\unsure{$E$}}
```

## Scan 017: 7 outermost cancellations

**D017.01**

```tex
\deleted{Supposons \unsure{que tous les corps résiduels de}}
```

**D017.02**

```tex
\deleted{\unsure{Il en résulte aussitôt qu'il opère trivialement dans $\mathcal E_2$ [car il y opère trivialement]}}
```

**D017.03**

```tex
\deleted{Si les caractéristiques résiduelles de $S$ sont $\neq2$, on en conclut}
```

**D017.04**

```tex
\deleted{Il existe un supplémentaire unique de $\mathcal E_1$ dans $\mathcal E_2$ \unsure{stable qui sera le lieu $s$ opère}}
```

**D017.05**

```tex
\deleted{\unsure{le}}
```

**D017.06**

```tex
\deleted{Alors $L_3^{\otimes2}$ est un supplémentaire de $\mathcal E_5$ dans $\mathcal E_6$, soit $L_6$. A condition}
```

**D017.07**

```tex
\deleted{\unsure{\lambda}}
```

## Scan 019: 5 outermost cancellations

**D019.01**

```tex
\deleted{\unsure{a}}
```

**D019.02**

```tex
\deleted{\unsure{j}}
```

**D019.03**

```tex
\deleted{\unsure{t}}
```

**D019.04**

```tex
\deleted{\unsure{3}}
```

**D019.05**

```tex
\deleted{\unsure{Hom}($\unsure{\widetilde E}$,)}
```

## Scan 021: 6 outermost cancellations

**D021.01**

```tex
\deleted{$(x_1-x_2)(x_3$}
```

**D021.02**

```tex
\deleted{=27c^{\unsure{3|2}}+9b(b^2-2\sum x_1^2x_2x_3}
```

**D021.03**

```tex
\deleted{\unsure{9|4}}
```

**D021.04**

```tex
\deleted{(\sum\unsure{x^2})^2}
```

**D021.05**

```tex
\deleted{\unsure{x_1x_2}}
```

**D021.06**

```tex
\deleted{x_1x_2}
```

## Scan 023: 6 outermost cancellations

**D023.01**

```tex
\deleted{$\unsure{x_1x_2x_3}$}
```

**D023.02**

```tex
\deleted{\frac{27}{-\Delta}\bigl[(a/3+x_1)(a/3+x_2)(a/3+x_3)\bigr]^2}
```

**D023.03**

```tex
\deleted{\unsure{(a/3)}}
```

**D023.04**

```tex
\deleted{\unsure{a}}
```

**D023.05**

```tex
\deleted{\unsure{a}}
```

**D023.06**

```tex
\deleted{\prod(x_1^2+x_2^2-2x_1x_2)\unsure{=}}
```

## Scan 025: 2 outermost cancellations

**D025.01**

```tex
\deleted{y^2=\unsure{a}x^3+bx^{\unsure{2}}+cx+d}
```

**D025.02**

```tex
\deleted{$\unsure{x_3}$}
```

## Scan 028: 2 outermost cancellations

**D028.01**

```tex
\deleted{\unsure{\psi^2=\varphi|\varphi^2=\psi}}
```

**D028.02**

```tex
\deleted{\unsure{de}}
```

## Scan 030: 2 outermost cancellations

**D030.01**

```tex
\deleted{\unsure{Le}}
```

**D030.02**

```tex
\deleted{\unsure{distinct de $\sigma$}}
```

## Scan 032: 5 outermost cancellations

**D032.01**

```tex
\deleted{$\unsure{\mathfrak S_3}$ opère}
```

**D032.02**

```tex
\deleted{\unsure{il est|qui est}}
```

**D032.03**

```tex
\deleted{\unsure{y}}
```

**D032.04**

```tex
\deleted{\unsure{simplement}}
```

**D032.05**

```tex
\deleted{\unsure{le schéma du revt}}
```

## Scan 034: 3 outermost cancellations

**D034.01**

```tex
\deleted{\unsure{un domaine de}}
```

**D034.02**

```tex
\deleted{\unsure{descente}}
```

**D034.03**

```tex
\deleted{la}
```

## Scan 036: 12 outermost cancellations

**D036.01**

```tex
\deleted{\unsure{section}}
```

**D036.02**

```tex
\deleted{\unsure{P^1_{\infty}}\ \unsure{G_m}}
```

**D036.03**

```tex
\deleted{\unsure{P^1_m}}
```

**D036.04**

```tex
\deleted{\unsure{x}}
```

**D036.05**

```tex
\deleted{\unsure{x'}}
```

**D036.06**

```tex
\deleted{\unsure{\sim}}
```

**D036.07**

```tex
\deleted{\unsure{\sim}}
```

**D036.08**

```tex
\deleted{\unsure{se}}
```

**D036.09**

```tex
\deleted{$S=\operatorname{Spec}(\unsure{\mathbb Z_m}[2^{-1},3^{-1}])$}
```

**D036.10**

```tex
\deleted{\unsure{\{}}
```

**D036.11**

```tex
\deleted{$\lambda$}
```

**D036.12**

```tex
\deleted{\unsure{$\in A$, donc de la forme $2^\alpha3^\beta$}.}
```

## Scan 038: 11 outermost cancellations

**D038.01**

```tex
\deleted{\unsure{défini}}
```

**D038.02**

```tex
\deleted{\unsure{\lambda}}
```

**D038.03**

```tex
\deleted{\unsure{\lambda}}
```

**D038.04**

```tex
\deleted{\unsure{\lambda}}
```

**D038.05**

```tex
\deleted{\unsure{\lambda}}
```

**D038.06**

```tex
\deleted{\unsure{x}}
```

**D038.07**

```tex
\deleted{\unsure{2}}
```

**D038.08**

```tex
\deleted{\unsure{2}}
```

**D038.09**

```tex
\deleted{\unsure{2}}
```

**D038.10**

```tex
\deleted{\unsure{x''^3-x'^3}}
```

**D038.11**

```tex
\deleted{\unsure{=(x''-x')(x''^2+x'x''+x'^2)=0}}
```

## Scan 040: 3 outermost cancellations

**D040.01**

```tex
\deleted{$\unsure{(G_a)_S}$}
```

**D040.02**

```tex
\deleted{\sigma'(t)=1/t}
```

**D040.03**

```tex
\deleted{et d'autre part}
```

## Scan 042: 3 outermost cancellations

**D042.01**

```tex
\deleted{\unsure{[en ses points}}
```

**D042.02**

```tex
\deleted{\unsure{f}}
```

**D042.03**

```tex
\deleted{\unsure{puis}}
```

## Scan 044: 9 outermost cancellations

**D044.01**

```tex
\deleted{$\unsure{\infty}$}
```

**D044.02**

```tex
\deleted{\unsure{et}}
```

**D044.03**

```tex
\deleted{\unsure{est}}
```

**D044.04**

```tex
\deleted{\unsure{_S}}
```

**D044.05**

```tex
\deleted{\unsure{j}}
```

**D044.06**

```tex
\deleted{\unsure{j}}
```

**D044.07**

```tex
\deleted{\unsure{x}}
```

**D044.08**

```tex
\deleted{section}
```

**D044.09**

```tex
\deleted{\unsure{et}}
```

## Scan 046: 1 outermost cancellations

**D046.01**

```tex
\deleted{\unsure{toute}}
```

## Scan 048: 5 outermost cancellations

**D048.01**

```tex
\deleted{\unsure{Supposons} $i$ \unsure{est égal à} $\unsure{0}$}
```

**D048.02**

```tex
\deleted{\unsure{Supposons}}
```

**D048.03**

```tex
\deleted{\unsure{Donc}}
```

**D048.04**

```tex
\deleted{\unsure{ce dernier}}
```

**D048.05**

```tex
\deleted{\unsure{deux}}
```

## Scan 050: 10 outermost cancellations

**D050.01**

```tex
\deleted{\unsure{Autre façon}}
```

**D050.02**

```tex
\deleted{$\unsure{X}$}
```

**D050.03**

```tex
\deleted{de}
```

**D050.04**

```tex
\deleted{\unsure{X\simeq P^1_S\times_{(S,\mathfrak S_3)}}}
```

**D050.05**

```tex
\deleted{une section}
```

**D050.06**

```tex
\deleted{\unsure{\varphi}}
```

**D050.07**

```tex
\deleted{\unsure{(car. $\ne2,3$)}}
```

**D050.08**

```tex
\deleted{$\unsure{X\simeq P^1_S}$}
```

**D050.09**

```tex
\deleted{$\unsure{t(t-1)\in\mathbb Z}$}
```

**D050.10**

```tex
\deleted{\unsure{si et}}
```

**Extraction totals:** 177 outermost cancellation blocks; 183 total `\deleted{` occurrences including nesting.


# Appendix D. Review of the primary reader's draft Q01/Q02 and Sections 6–8

The draft reviewed was `MPL_62_002-050_work/MPL_62_002-050_notes.md`. No change was made to it. These comments concern source fidelity and indexing, not an independent mathematical review of all research notes.

- The bounded negative conclusions in Q01/Q02, distinction between the particular map and abstract isomorphism, chronology caveat, three pagination layers, scan 047 annotation qualification, and corrected LM4 E.20 status agree with the sources examined here.
- Q01/Q02's source field should explicitly use **002, 004–017, 019–026, 028–050**, rather than a range 019–050 that includes the excluded scan 027.
- Q01 can quote the literal ending as **“compatibilité.....”**, preserving the five ordinary periods of the supplied transcription.
- In Q02, **“abelian-variety structures on cycle quotients”** follows the programme more closely than “abelian representatives,” which can suggest the stronger modern universal-property identification discussed, but not settled, in CTX-N D08.
- The Section 6 index could add the scan 022 margin about a general fact for metrizable topologies (uncertain wording; main notes D02–D03) and the scan 043 “topologt|topol.?” margin (main notes D08). The latter alternative must not be promoted to a certain authorial question mark.
- If the index includes closed proof requests, add scan 006's “Il faut prouver que” with the direct argument on scan 007; scan 007's “vérification locale” with the opening of scan 008; and scan 011's “Il reste à écrire” immediately answered by the discriminant-unit criterion, distinct from the following blank formula request.
- The Section 8 status for LM7 E.30 may be made exact: **“Proved (the return's claim)”**, with no additional referee status implied. The supplied CYCLOTOMIC_KERNEL C1 row also says “Proved (the return's claim),” while the later run-level summary separately says reviewed with zero wrong; those are distinct levels of qualification.

The updated literal-flag inventory contains **46 entries F01–F46**. The cancellation extraction remains **177 outermost / 183 total including nested occurrences**. The enumeration is a source-text aid for integration by the primary reader and makes no full-archive absence claim.
