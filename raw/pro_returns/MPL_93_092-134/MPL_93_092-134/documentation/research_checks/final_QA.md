# Final independent QA

Date: 2026-11-18. Reviewer: GPT-6 Astra Pro; effort setting not exposed; `MPL_93_092-134/mechanical_validation`.

## Outcome

**PASS: the frozen transcription, current research-note source parts, and assembled main notes pass this review.** No remaining mathematical or required-metadata issue was identified in F09/F10 or in the checked parts. The root corrected the two introduction-register references reported during this pass: scan 123 now includes D10; scan 124 points to D07–D08.

The initial assembly-freshness issue is resolved: the main notes now equal the current source parts byte for byte, including the introduction references, F10/B4/crosswalk additions, and corrected E20 product convention. Fifteen actual review events are supplied in `final_review_events.tsv`; the final three cover the four last-added notes and are ready for the root's final ledger assembly.

## F09: exact Legendre comparison

I read `legendre_comparison.md` and the certificate source and independently reran `legendre_certificate.py`. Both exact rational residuals were zero:

\[
\left[z(1-z)\partial_z^2+(1-2z)\partial_z-\tfrac14\right](dx/y)
-d_x\left[\frac{y}{2(x-z)^2}\right]=0,
\]

and

\[
2P'+P^2-4Q=-\frac{z^2-z+1}{z^2(z-1)^2}.
\]

The period argument has the correct local meaning: differentiate along transported closed cycles avoiding the poles, then integrate the exact differential to zero. The scalar gauge used to remove the first derivative preserves solution ratios. Thus the projective coefficient comparison is valid in the stated characteristic-zero setting; the rational computation alone is not advertised as a formalized de Rham theorem.

I also reopened and read Harnad's [author preprint](https://arxiv.org/pdf/solv-int/9902013), §1, equations (1.9)–(1.12), printed pp. 2–3, and (1.18)–(1.19), p. 4. These supply the period and Schwarzian comparison and the constant-rescaling version of the same family. F09 correctly separates this external geometric realization from any claim that the manuscript explicitly names it.

## F10: hypotheses and nilpotence scope

The relevant morphism is the **projective** Weierstrass family over

\[
S=\operatorname{Spec}\mathbf Z[1/2,z,1/(z(1-z))],
\qquad T=\operatorname{Spec}\mathbf Z[1/2].
\]

Here S is smooth and connected over T. The cubic with its section at infinity is proper, and its unit discriminant gives smooth elliptic fibres. Its Hodge cohomology and de Rham cohomology are locally free. These are the hypotheses needed for the stated application, rather than properties of the affine equation alone.

The [original Katz paper](https://www.numdam.org/item/PMIHES_1970__39__175_0.pdf) was actually reopened: Introduction (0.5.2), printed p. 176, gives this projective Legendre model and thickening; §§9.0–9.1 define the arithmetic base and global nilpotence; Theorem 10.0, pp. 209–210, supplies the conclusion. Theorem 7.4/Corollary 7.5, p. 203, retain the stated base-change or flat-Frobenius alternatives when the conjugate filtration is used. No independent proof of Katz's paper is claimed.

The projective consequence is justified: projective p-curvature is induced by the image of linear p-curvature in the adjoint quotient, and a nilpotent endomorphism has nilpotent adjoint action. Equivalently, if N is nilpotent then sufficiently high iterated commutators with N vanish. The scalar gauge in F09 does not change the projective object. Neither step turns nilpotence into zero p-curvature.

F10's final wording correctly identifies a theorem-based consequence for this family, not an explicit p-curvature computation, not a zero-curvature claim, and not a conclusion for every uniformizing connection. Its revised use of “projective Legendre family” and the direct Katz model citation resolve the only useful precision suggestions from this pass.

## Read-only frozen-package checks

| Check | Result |
|---|---|
| Expected pages and scan markers | 42/42, scans 092–134 excluding 125; correct opening cote and scan marker |
| Combined transcription | Exact ordered byte concatenation of the 42 page files |
| Frozen SHA256 manifest | All 43 entries match: 42 pages plus combined fragment |
| Inventory | 1,191 rows; all 42 scans; all transcribed values `yes`; required columns, allowed kinds, required fields, per-page identifiers and sheet-kind consistency pass |
| Sheet kinds | All 42 recorded as `text` |
| Progress events | 42 ordered `done` and 42 ordered `audited` events |
| Doubts source and Markdown | 291 rows each, exact corresponding rendered rows, all 42 scans represented |
| Doubt confidence | 8 high, 88 medium, 195 low; no invalid value or missing required field |
| Annotation occurrences | 447 `unsure`; 1 `illegible` |
| Illegible-marker context | Scan 117, line 13, in prose outside math and diagrams |
| Commands and structure | Allowed annotation macros and inspected standard LaTeX/AMS/TikZ commands only; balanced braces, environments, and explicit math delimiters |
| Prohibited content checks | No external/image inclusion or preamble command, TODO/PLACEHOLDER marker, or forbidden placeholder ellipsis detected |
| Concurrent page changes | None detected during the snapshot check |

The delimiter lexer recognizes text containers. In particular, the inline math inside `textcircled` on scan 124 is a valid text-box construction, not a nested-math defect. No change to that frozen line was requested or made.

## Research metadata and earlier findings

The final checked assembly contains **87** distinct main notes, consecutive within each section: A15, B19, C09, D14, E20, F10. Every note has a location, kind, contextual relation, actual context-query pattern, and typed check outcome; every own-idea note has a confidence field. Bibliography labels B1–B13 resolve, including Harnad B13. The query register has **260** per-file records covering all **87** notes, and its patterns match the notes. The checked ledger snapshot has **211** well-formed events and covers every main note; accepted check types and nonempty date/identity/outcome fields pass. This snapshot precedes the last supplementary agent-event additions, which the root will consolidate. Agent identities expressed as `/root/...` are valid identities, not missing run metadata.

The source parts now incorporate the earlier A–D QA corrections: B07 states equivalent associated-bundle relations; C03 points to D11; B05 credits H-VIIa for the explicit oper interpretation; A07/A11 have the appropriate field/complex-curve scope; A14 uses the fixed-parameter wording; D14 uses A-module determinants. D14's odd-characteristic refinement was independently rechecked in the earlier pass and remains sound. Its proof does not establish determinant-one normalization or removal of the Picard hypothesis in characteristic 2.

The four final additions were also checked. A15 leaves the general functorial contact-element construction uncertified; B19 preserves the cancelled wording as a reading question. In E19, translational affine transport fixes the projective infinity section, which is algebraic and disjoint from the finite zero section in the stated models. In E20, `(x,w) -> (x+w,x)` has inverse `(y,x) -> (x,y-x)` and respects affine coordinate changes. The root corrected its factor order to agree with E10. These claims remain restricted to their explicit affine models and do not assert algebraicity of arbitrary analytic covering maps.

## Post-assembly verification

After the root's 01:50:49 assembly, the main notes are the exact byte concatenation prescribed by the assembler from all eight current source parts. The checked main-notes SHA256 is:

```text
12202d7f82724b79d9fe3d6d0765547494189fac7674ecb2ba58f63f4eb7f6ea
```

All 43 frozen transcription hashes were independently rechecked at this stage and still match. No source part changed during the snapshot check. The remaining release step is the root's announced ledger consolidation of the supplementary events and package creation; no unresolved source or assembled-note correction is left by this QA.

## Limits

This was a focused mathematical review of the new F09/F10 comparison, a follow-up on identified A–D issues, and static package validation. It was not a new visual reading, a transcription task, or a fresh proof audit of every research note. No images, OCR, or earlier P05 recalculation were used. No page file or combined transcription was modified. No LaTeX compilation was attempted; the previously recorded missing-format/package limitation remains, so compiler-level success is not claimed. Row coverage and lexical checks cannot establish palaeographic accuracy or completeness of the visual inventory.
