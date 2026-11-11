# LM3_TEICHMULLER_TOWER — research and verification report

**AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.**  
**Research cutoff:** 11 November 2026.

## Deliverable and status register

This package develops Parts A–F of the attached prompt. The paper contains **110 numbered assertions: 57 Proved, 30 Known, 11 Refuted, and 12 Open**. The bibliography has **53 distinct entries**, each explicitly marked verified or unverified; in the present package every cited source was opened. The reading register contains **42 records** of mathematical or contextual evidence bearing on the manuscript. An opened source is not thereby an independently certified proof.

The paper's principal result is a distinction, followed through all the constructions: the arithmetic-image quotient introduced in §29 is identified with G_Q for every hyperbolic type, while the earlier normalizer quotient is a different group. Its genus-zero comparison leads to GT_0 at the isolated tripod and to GT at the subsequent levels. The conjecture G_Q=GT remains separate.

The categorical part constructs an actual pro-object of finite categories, proves cofinality of the transporter quotients, compares its finite representations with finite boundary-constructible sheaves with their stalks, and computes the decorated genus-zero tower automorphism group using the exact Harbater–Schneps theorem. The positive-genus construction retains stack isotropy. The remaining higher-completion and elliptic automorphism comparisons are stated explicitly, with the point where the argument stops.

## How to read the status labels

| Label | Meaning |
|---|---|
| Proved | The exact assertion is proved in this paper. If it is a conditional implication, its antecedent is stated explicitly and is not certified by that label. |
| Known | The exact imported theorem is supplied with an opened primary source, theorem number and checked scope. We do not claim to have reconstructed every historical proof. |
| Refuted | A complete counterexample is given. Computable finite components are checked by attached programs. An invalid proof alone is never labelled a refutation. |
| Open | Either an established open mathematical problem, a new unrefereed claim not fully certified in this audit, or an exact comparison left unresolved here. The statement and notes distinguish these meanings. |

The established open problems include the high-genus congruence question B.3 and the profinite arithmetic equality E.8. The audit-unresolved comparisons are B.7, B.14, C.8, D.23, E.14, F.16 and F.18. D.7, D.13 and E.26 record the three supplied 2026 claim families and the exact limits of their verification. None is removed from the register after proving a special case.

## Main corrections to the supplied leads

- **Lead1:** The Russian result is contextually Belyi's theorem, and it supplies faithfulness. But the revised arithmetic-image quotient has surjectivity by definition. The earlier normalizer problem is the GT-like realization problem; the two cannot be substituted for one another.
- **Lead2:** The relative Hom theorem has the stated sub-p-adic hypotheses and geometric-inner ambiguity. The literal maximal-open-normalizer criterion for cusp groups is false; the correct theorem includes the cyclotomic conjugation condition. The absolute open-Hom deduction is conditional only at the specified base-field reconstruction step.
- **Lead3:** Faithfulness holds for affine and proper hyperbolic curves over the specified fields. Hoshi–Mochizuki Corollary6.4 supplies the stronger faithfulness modulo the orientation-preserving geometric monodromy image, resolving the manuscript's “peut-être ... faux” question positively in that formulation.
- **Lead4:** CSP, normality of the geometric image, and properness of that image in all loop-preserving outer automorphisms are distinct assertions. The older attached genus-two paper does not prove the closed case; the later theorem does. The exceptional nonhyperbolic types are treated explicitly.
- **Lead5:** Both full and procongruence Birman sequences have exact positive forms. The arithmetic-image filling sequence is proved. The unrestricted ambient outer-automorphism row marked “??” is a stronger lifting statement, not automatically a corollary of those exact sequences or of configuration-space cuspidalization.
- **Full étale topos:** Killing peripheral inertia reconstructs a fundamental-group quotient and its covering theory, not the whole small étale topos. The correct reconstruction first uses arithmetic anabelian Isom to recover the open curve, then its proper model and an explicit basis for the full étale site.
- **Companion packages:** We retain the actual transitions and the distinction between natural isomorphisms and arbitrary natural transformations. We do not refute GALOIS F.4's qualified split-representation statement. We use Jansen and BGH directly for the categorical and geometric comparisons rather than treat the companion review as authority.

## The 2026 proof packs

The full main texts of families019 and031 and §§2–5 of008 were examined, with the external primary inputs used in our deductions checked individually. Conditional deductions are written out. The remaining new technical arguments are identified in the detailed audits below.

The supplied Lean comparator for008 ends with a placeholder and is not itself a checked proof. The current search also found Willwacher's subsequent October2026 proof treatment, which was opened. We report that development and its verification scope. We do not infer that an unrefereed statement is false, nor that a subsequently published preprint has been fully checked merely because its principal theorem agrees with the claim.

The rational implications distinguish GRT_1 from G_m⋉GRT_1, pro-l realizations from full profinite groups, and Zariski density from topological density. The all-weight rational bound would not establish exhaustion of every finite quotient of GT, which is the actual profinite requirement.

## Input and search record

Only the files supplied in this conversation and primary public mathematical sources were used. The original ZIP was extracted without modifying it. Primary paper PDFs were converted to text for search; scanned pages were rendered or inspected where extraction was insufficient. The individual reports specify their inspected scan numbers, exact theorem locations and version discrepancies.

Current searches covered the named authors and titles in the prompt, the full/procongruence distinction, genus-two congruence, normalizers and inertia, relative and absolute Hom, cuspidalization and sections, automorphisms at the five requested types, the recent tower papers and the October2026 Deligne–Drinfeld literature. We make no novelty claim based on a negative search.

## Reproducibility and build

The results and reading CSVs are generated from the audit fragments and checked against every numbered statement in the TeX sections. Citation aliases are normalized before the bibliography is built; the validation checks every cited key and every status. The finite programs were rerun successfully. Their limits are part of their output and the paper.

BUILD_RECORD

---

## Detailed audit: Parts A and F


