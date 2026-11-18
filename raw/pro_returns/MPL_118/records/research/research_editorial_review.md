# MPL 118 — Editorial review of research mappings and root notes

**Reviewer:** GPT-6 Astra Pro; effort inherited/not exposed. **Completed:** 2026-11-18T03:20:27+00:00.

## Scope and result

All 270 mapping note bodies were read, and their identifiers, statuses, evidence fragments, available context paths, and record structure were checked. The exact 255-row dossier set and all 12 numbered NEW_RESULTS entries plus its three Known-after-all statements are covered once, with no omissions or extra IDs. No manuscript images, OCR, transcription amendments, or new proof validation were used in this editorial review.

The 14 current root notes (H01–H03 and C01–C11) were read for concrete factual, logical, source-attribution, and note-ID problems. The substantive corrections found are listed below; root_notes.md is being expanded, so the review applies to the recorded snapshot rather than to later additions.

## Mechanical findings

| Mapping | Records | Partial | Analogue | Absent |
|---|---:|---:|---:|---:|
| strata_paths_mapping | 86 | 3 | 10 | 73 |
| bisite_mapping | 113 | 10 | 30 | 73 |
| residue_mapping | 56 | 5 | 9 | 42 |
| new_results_mapping | 15 | 0 | 1 | 14 |

- All 255 dossier statuses match the supplied status strings exactly. All 12 NEW_RESULTS numbered records preserve the source Checked-by field verbatim and its correct source line; the three remaining records correspond to the three Known-after-all statements.
- All 270 mapping note bodies satisfy the one-to-four-sentence constraint. Their labels, exact quotations, and source metadata are outside those note bodies.
- All 262 manuscript-evidence occurrences are literal substrings of the cited frozen page files. Every non-absent row has manuscript evidence. Every referenced context file exists.
- Every selected RESULTS_STATE ID in the four mapping JSON files occurs in RESULTS_STATE. Every one of the 270 mapping IDs has a corresponding event in the three supplied event TSVs.
- No absent row was found to infer a mathematical refutation or settlement merely from absence. The distinction between the product/diagonal and all-final-image meanings of totality, categorical opfibration versus intrinsic/model cofibration, and ordinary fraction calculus versus coherent rectification is consistently preserved.
- Root note IDs H01–H03 and C01–C11 are unique. Their bodies have at most four actual sentences; a naive punctuation count splits the abbreviation ms. in H01, H02, and C07, which is not a sentence-length violation.

## Concrete findings and corrections

### E01 — PATHS A.2 and A.3 needed the filtration-gap qualification

**Status: corrected in the owned STRATA/PATHS JSON and Markdown at the primary agent’s request.** A.2 formerly said that scans039–040 prove the special union theorem, and A.3 described the comma identification without qualification. The notes now call it the asserted argument, identify the lax-commutation gap, and point to the separate MPL118-C03 repair; their supplied statements, statuses, relations, and evidence are unchanged. The JSON metadata records an editorial revision timestamp; event scope remains textual comparison only.

The issue is concrete: the frozen hypotheses f(X_i)⊂Y_i give ψf≤φ, not automatically ψf=φ, so the printed identification with a triangle strictly over I cannot itself be treated as a completed proof. This observation was already isolated and repaired in the primary note C03; this editorial pass adds no new proof claim.

### E02 — C04 must name the ordinary weak-homotopy localizer

**Status: corrected by the primary agent and verified in the live root notes.** The action-groupoid argument giving W_BG = equivariant bijections is the W∞ argument; it is not true for arbitrary W. C04 now begins with the explicit W=W∞ qualification, followed by the existing argument. Its intended consequence for nontrivial BG is otherwise coherent, and this changes no frozen reading.

### E03 — Several valid contextual IDs were attributed to the wrong supplied file

**Status: corrected source attributions were verified in H01–H03, C03, C06, C08, and C11.** The following exact IDs do not occur in RESULTS_STATE.md. They remain legitimate contextual IDs where the dossier or NEW_RESULTS names them; the correction is to the source attribution, not to delete them.

| ID absent from RESULTS_STATE | Correct supplied route |
|---|---|
| TOTASPH A.13 | NEW_RESULTS.md, numbered result 8 (and the cited companion discussion) |
| TOTASPH C.5 | NEW_RESULTS.md, numbered result 11, which names C.5–C.10 |
| TOTASPH C.6 | NEW_RESULTS.md, numbered result 11, which names C.5–C.10 |
| TOTASPH C.7 | NEW_RESULTS.md, numbered result 11, which names C.5–C.10 |
| TOTASPH C.8 | NEW_RESULTS.md, numbered result 11, which names C.5–C.10 |
| TOTASPH C.9 | NEW_RESULTS.md, numbered result 11, which names C.5–C.10 |
| RESIDUE F.1 | DOSSIER_STATEMENTS_WITH_STATUS.md, line 272 |
| STRATA G.2 | DOSSIER_STATEMENTS_WITH_STATUS.md, line 24 |
| RESIDUE B.8 | DOSSIER_STATEMENTS_WITH_STATUS.md, line 242 |
| RESIDUE B.10 | DOSSIER_STATEMENTS_WITH_STATUS.md, line 244 |
| RESIDUE B.11 | DOSSIER_STATEMENTS_WITH_STATUS.md, line 245 |
| PATHS D.16 | DOSSIER_STATEMENTS_WITH_STATUS.md, line 82 |

The exact RESULTS_STATE entries GALOIS B.1/B.3, TOTASPH C.10, POLES B.2/H.5, and the named 118 Hua-summary entries do occur there. The source-ID correction affects the earlier wording of H01–H03, C03, C06, C08, and C11, as applicable; it does not alter their mathematical content.

### E04 — Optional source-line precision for Known-after-all entries

All three NR-K records currently anchor the Known-after-all block at line31 and identify their statement ordinal, which is unambiguous. For exact entry-line precision, NR-K2 could use line32 and NR-K3 line33; NR-K1 remains line31. This is a minor locator refinement, not a coverage or status error. H01 also repeats its NEW_RESULTS result 8 reference in the context metadata; one copy can be removed as a purely editorial cleanup.

## Root-note logic and terminology

No additional concrete logical error was found in the reviewed formulations after separating the intended W∞ scope of C04 from arbitrary-localizer statements. C01 restricts strict-base-change commutation to Grothendieck integrals and does not claim it for ordinary pushouts; C02 explicitly keeps the opfibration/cartesian and fibre hypotheses; C03 records the strict-versus-lax issue instead of silently identifying its triangle. C05 keeps the empty-category/nullary exception, C06 distinguishes strict products from products after localization, C07 stays at 1-equivalences, C08 chooses nonzero H1 rather than relying on nontrivial π1 alone, and C09 preserves the deletion and unfinished dependencies of the saturation proof.

This is an editorial consistency and limited logical-scope review, not a replacement for the separately identified mathematical peer checks or external-reference verification. Historical priority remains bounded to located supplied material.

## Snapshot and remaining integration

Root-notes snapshot SHA256:

```text
cf75841aefc86e1a2552c404e8a23e0eca377db15b49a73af530f4da65d1cdd6
```

At the snapshot there were 14 uniquely identified root notes. The primary agent is adding later sections and bibliography/check-record material; unresolved bibliography labels and references to records still being created are integration work, not treated here as completed deliverables.

The frozen transcription was not changed. Its SHA256 remains:

```text
63b5213a6f4b8790fefa6a9d7d8ce3fdc50723ef67fad682348b36a48845b149
```

## Addendum — Claims and authorial self-flags

**Reviewed:** 2026-11-18T03:30:16+00:00. **Scope:** all 29 M notes in root_claims.md and all 46 initial SF notes in root_self_flags.md, compared with the frozen TeX only. No scan images, OCR, or transcription edits were used; this remains textual editorial comparison rather than a new proof audit.

The two lists cover the explicit question marks, conditional qualifications, and abandoned proofs well overall. The following concrete corrections were reported to the primary agent; the reviewer has not rewritten either source file. Later integration may already have applied them.

### E05 — Two explicit authorial items need separate SF entries

**Scan015:** the `\uline{Question}` paragraph before the bracketed i→i′ question is a distinct item. It says that f having the uncertain property `\unsure{asphérique|cofibré}` need not force g to have it, and that f∈W may fail to force g∈W in the open/closed attaching-immersion pushout. SF15 currently records only the following i∈W⇒i′∈W doubt; the two directions should not be merged. The later scan023 double-cone example is the appropriate cross-reference for the former weak-equivalence implication.

Exact frozen excerpt:

```tex
\uline{Question} --- si $f$ \unsure{asphérique|cofibré}, il n'en résulte pas que $g$ le soit, et si $f\in\underline W$, il est possible qu'on n'ait pas $g\in\underline W$,
```

**Scan023:** the conjectural fundamental-groupoid rescue has no separate SF entry, although C07 discusses and answers it. The register explicitly includes questions answered later, so it should retain this question with a cross-reference to C07.

Exact frozen excerpt:

```tex
\margin{Il semble vrai pourtant que si $g$ induit une \deleted{iso} $1$-équiv.,
i.e. équiv. sur les groupoïdes fondamentaux, alors $f$ aussi. $[\ ]$ ?}
```

### E06 — Literal quotation corrections

| Note | Finding | Minimal correction |
|---|---|---|
| M13 | Its backtick formula silently replaces the frozen dash by an arrow and adds parentheses around Ens. | Use the exact formula below, or explicitly label the displayed formula as normalized notation. |
| SF12 | Its backtick fragment omits the dollar signs between the pair and the word adjoint, so it is not a literal TeX substring. | Use the complete frozen fragment below, or quote the prose separately. |
| M14 | “stable par produits” is not written on scan017. | Cite the actual “c) Product” heading or its displayed product formula. |
| SF31 / SF32 | The quoted French expands the manuscript’s = abbreviation to même. | Retain =, or explicitly label the phrase as an expanded paraphrase rather than literal wording. |
| SF43 | “Il y a des chances” spans the end of scan036 and start of scan037. | Give scans036–037 as the source of that quotation. |

M13 literal fragment:

```tex
H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}
```

SF12 literal fragment:

```tex
$(\lambda_f,\sigma_f)$ adjoint ?
```

M14 product formula:

```tex
H_{T\times X}((t,u),(t',y))\simeq\mathrm{Hom}_T(t,t')\times H_X(u,y)
```

SF31 / SF32 literal wordings:

```tex
Donc il y aura quand $=$ surjectivité!
Mais oui, par le $=$ argument
```

### E07 — SF11 identifies the section as a retraction

The frozen diagrams on scans011–012 draw the uncertain η_f/H_f map from X into Fib(f), while ρ_f goes from Fib(f) back to X. Thus the heading and body of SF11 should call η_f/H_f the section or comma inclusion, not the retraction functor. Its possible Serre nonmembership and the uncertainty of the letter remain unchanged.

### E08 — M28 must distinguish two Dwyer-related classes

The sentence about an open problem concerning “their composition” immediately follows a reference to Thomason’s Dwyer maps and can identify the two classes incorrectly. RESULTS_STATE TOTASPH F.27 explicitly asks about `W_\infty`-dwyérienne sieves in the later manuscript sense, while DOSSIER RESIDUE F.6 discusses total presheaves and that same specified composition assertion. Name this later class explicitly, so the question is not attributed without qualification to the Thomason class cited in the preceding sentence. This recommendation is source differentiation, not a new verdict on either theorem.

### E09 — M09 has one more source-file attribution error

BISITE A.1 does not occur as an entry in RESULTS_STATE.md. Its full statement is supplied in DOSSIER_STATEMENTS_WITH_STATUS.md, line115, so M09 should cite RESULTS_STATE for GALOIS B.1/B.3 and DOSSIER for BISITE A.1.

### E10 — Optional context and qualification refinements

M05 cites BISITE A.11, whose actual subject is enough intrinsic fibrations and the equality Fib_W∩W=W^u. For its opposite-category discussion, BISITE F.8 (DOSSIER line202) is the directly relevant row, alongside RESIDUE B.6.

Two explicit programme/qualification phrases could be added to the SF register if maximal granularity is desired: scan015 “mettons au net” for the fibration/cofibration constructions, and scan025’s margin making condition (iii) unnecessary in the presheaf case provided condition (ii) can be weakened in the stated way. Their themes are already covered by M09/M16 and SF22/SF24, so these are refinements rather than two further clear omissions.

## Addendum validation boundary

All 29 M identifiers and 46 initial SF identifiers are unique, and their note bodies remain within the one-to-four-sentence limit. The asserted backtick manuscript quotations were checked literally; the two nonmatches are M13 and SF12 above. No other concrete logical or source error was found in the reviewed claims beyond the distinctions recorded here, and no supplied mathematical proof status was changed.

## Final bounded textual QA — Reading questions, titles, and applied fixes

**Completed:** 2026-11-18T03:39:59+00:00. This pass read all 20 R notes and 8 T notes, the Hua-project README, and the specific Hua passages to which the comparisons refer. It checked the frozen TeX and the inventory for the corresponding quotations, headings, local page numbers, and sheet counts; it did not inspect images, repeat the 270-row audit, or undertake further proof checks.

### Earlier required editorial fixes: verified present

- E05: SF47 and SF48 separately retain the scan023 fundamental-groupoid conjecture and scan015 opposite-pushout-map question.
- E06: M13 and SF12 now use literal TeX fragments; M14 uses the actual Product/homotopy headings; SF31 retains the = abbreviation; SF32 uses a shorter literal quotation; SF43 cites scans036–037.
- E07: SF11 now identifies the section/comma inclusion rather than the retraction.
- E08: M28 explicitly separates Thomason Dwyer maps from the later W∞-dwyérienne sieve composition question.
- E09: M09 now attributes BISITE A.1 to DOSSIER rather than RESULTS_STATE.
- E10 was optional granularity/context refinement. M05 still cites BISITE A.11 rather than the more directly relevant F.8; this does not affect the preceding verified required corrections.

### Three narrow wording corrections from this pass

**E11 — R04 and the related SF06 should not invent a diplomatic uncertainty on WSE.** Frozen scan005 contains `$WSE$` without an uncertainty macro, whereas WCF occurs as `\unsure{WCF}`. Distinguish an explicitly doubtful WCF reading from the unmarked but anomalous/undefined WSE label. R04 can discuss the uncertain meaning of WSE without saying its letters were marked uncertain; SF06 should make the same distinction.

**E12 — R14 should attribute the alternate identity to the cylinder interpretation, not to typing alone.** In the frozen diagram i_j goes from bar(Y′_j) to Y′_j and r_j goes back, so the written r_j i_j=id_bar(Y′_j) is type-correct. Hua’s footnote at lines1004–1015 proposes the opposite retraction identity for the cylinder factorization; it is that interpretation which motivates the alternative. The phrase “even where the types suggest another formula” should therefore be replaced by wording about the proposed cylinder interpretation.

**E13 — R06 can identify the particular axiom Hua expands.** At Hua lines548–552, the footnote says Loc2 and Loc3 are not recalled on the sheet, then explains the relative-Theorem-A role of Loc3. It does not separately expand Loc2 there. Suggested precision: Hua expands the role of Loc3 as relative Theorem A, although its definition is not written on this page.

### New-section checks that passed

All 20 R identifiers and 8 T identifiers are unique. Their note bodies contain one to four sentences, and every backtick manuscript quotation in their evidence fields matches the frozen TeX. The substantive differences attributed to Hua were confirmed in the cited supplied passages: subtitle, 1985 notice date, normalized section/exponent letters, cocartesian-squares reading, histoire/axiome, cart/cocartesian interpretation, h^{-1}(Y′) correction claim, aspherical/coaspherical wording, allegedly missing cartesian hypothesis, equivalent/isomorphic/ W-aspherical distinctions, omissions of deleted material, elementary-interval repair, retraction identity, product target, Hot_A/Hot distinction, (iv)/(ii) sum claim, inserted Non, lax triangle, and strong-saturation interpretation.

The title notes agree with the frozen cover, part2 heading, gluing continuation, local authorial sequence including 2 bis, corollary numbers, and Passage à la limite heading. The inventory independently confirms 38 distinct supplied scans: 1 cover, 6 reused typed sheets (004,006,007,010,017,018), and 31 text sheets. The scan018 notice dates are exactly 28 April1983 and 13 May1983 in the frozen TeX.

The absence of a manuscript-wide count/range is supported by the frozen text. This pass does not independently re-audit the images or re-fetch the archive catalogue; the primary agent’s separately documented image reading and external catalogue citation retain their own scope.

**Final status:** the earlier required editorial corrections are integrated; the three small wording points E11–E13 have been reported for primary-agent correction. No additional concrete error was found in this bounded reading-question/title pass.


## Primary-reader closure of editorial corrections

Recorded 2026-11-18 03:47:16 UTC. E05–E13 have been applied in the primary note parts: the two missing self-flags are SF47/SF48; the quotation, section/retraction, WSE/WCF, retraction-typing, Loc3, and Dwyer-class distinctions are corrected. The optional opposition pointer uses BISITE F.8. NR-K2/K3 now point to exact source lines32/33, and the duplicate H01 source citation is removed. STRATA D.4 now leaves the uncertain preservation adjective unspecified. No supplied result status, relation judgment, manuscript quotation, frozen page, or combined transcription was changed.
