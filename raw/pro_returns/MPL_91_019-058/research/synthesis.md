# Research notes — MPL 91, scans 019–058

## Scope, source order, and status

These notes concern the **38 retained scans** of cote 91, scans 019–058 excluding the supplied blank omissions 030 and 033. The transcription was frozen at **2026-11-17 23:04:59 UTC**, after the single-reader transcription and second visual audit of all 38 pages; the context was opened at **23:05:09 UTC**. The final integrity record in progress.log verifies the 38 page files and the exact combined fragment against their pre-context SHA-256 hashes. Reading questions raised by the context appear only in these notes.

Source quotations refer to the frozen diplomatic text, including its uncertain words and deleted or inserted states. In particular, a mathematical inconsistency is not by itself evidence that an uncertain word should be changed. Editorial examples and proposed repairs are labelled **own idea**, with confidence and a reason; they are not claims of historical priority, novelty, or a completed external referee review.

The separate A, B and C identifiers keep the research searchable by scan. Every item has an executed query across all six supplied context files, recorded in research/searches_019-032.tsv, research/context_searches_034-049.tsv, and research/root_context_searches.jsonl, with corresponding human-readable records or query plans. The supplementary research/etale_criterion_review.md gives the full finite locally free equivalence proof and detailed checks behind C01–C26. The source/context passages actually used are named beside each note; a broad keyword match is not treated as a mathematical identification.

### Source key and limitations

| Source | Exact supplied location | Status used here |
|---|---|---|
| Planning context | README.md, “This package in our plan” and “What our planning document asks” | Unchecked Book I I.VI placement, rank 20, and wider K-theory/Néron/residue/duality/intersection expectations; the later addenda supersede the early “Only this README” description. |
| Results register | notes/RESULTS_STATE.md, built 17 November 2026, 03:25 UTC | Run claims unless an explicit referee qualification is supplied; some source statements are truncated in the register itself, and their underlying returns were not provided. |
| Earlier same-cote notes | same_cote_91/MPL_90+91_002-018_notes.md | First pass, not yet checked; earlier cote 91 scans 002–018 and separately identified cote 90 material. |
| Later same-cote notes | same_cote_91/MPL_91_099-143_notes.md | First pass, not yet checked; references to scans 099–143 below come from these notes, not a new visual inspection. |
| Hua's modernised account | hua_project/91.modern.tex, with hua_project/README.md | Michel Hua's project's interpretation, credited on every use; supplied in full and read for research only. Its manuscript page \(p\) corresponds here to scan \(p+1\). |
| Hua findings H-H, H-R, H-E | RESULTS_STATE entries 91-hom-unramified-rigidification, 91-res-representable-by-scheme, 91-weil-restriction-finite-etale-criterion | Candidates with the project's “no reference found” search status and a statement-level intake “new to us”; neither proof validation nor novelty follows from those labels. |
| Primary literature | Exact URLs and theorem locators in the notes and research reference logs | Checked only to the extent stated; metadata or an abstract is not described as a checked proof. |

The important additions are the separation of the two obstruction compatibilities on 020–021, hypothesis and scheme-versus-algebraic-space audits on 025–032, the sheaf-intersection distinction on 039, the scope of projectivity and surjectivity on 044–045, and the explicit tests of the numerical and categorical assertions on 051–058. The finite locally free four-condition criterion survives a complete modern proof; the unrestricted degree and left-exact-endofunctor formulations do not survive the examples given below.

## P01 — Disposition of the three Hua findings

**Kind:** unpursued implication / comparison audit. **Sources:** cote 91, scans 019–029, 031–032, 054–058. **Search record:** P01. **Context:** the three exact findings IDs in notes/RESULTS_STATE.md and the corresponding sections II–IV and VI of Hua's modernised reading.

| Finding, with attribution | What the retained pages support | What this package adds or limits |
|---|---|---|
| **Hua, findings register, 91-hom-unramified-rigidification** | The obstruction continuation on 019–021 and the letter's explicit unramified, separated, locally finite-presentation conclusion on 031. | Two compatibility steps must be established, the frozen verbs are less certain than Hua's “two admissions” narrative, and the alternative module argument needs its own representability and compatibility checks. |
| **Hua, findings register, 91-res-representable-by-scheme** | Announced scheme-representability conditions on 026, corollaries and questions on 025–029, and the scheme-valued cover/descent distinction in the letter on 031–032. | The source distinguishes extra separation/quasi-separation and quasi-projectivity hypotheses; the letter explicitly says ordinary Hom need not be scheme-representable over the original field, so a broad unconditional scheme theorem would be false to its content. |
| **Hua, findings register, 91-weil-restriction-finite-etale-criterion** | Four equivalent conditions and an arrow cycle on 054, with item (iv) questioned, followed by “homogène” and the component-object programme on 055–058. | A complete finite locally free proof is supplied in research/etale_criterion_review.md, EC04–EC05; the source's broader deleted-hypothesis formulations and the asserted classification of all left-exact endofunctors require separate repairs. |

The finding IDs retain their supplied candidate/intake status. “Verified” here refers only to the specifically stated modern finite locally free argument and the explicit examples, not to novelty or to every manuscript generalization.

## P02 — Results-register links and unchanged open items

**Kind:** unpursued implication / bounded register comparison. **Sources:** cote 91, scans 031–032, 034–058, particularly 054–058. **Search record:** P02. **Context:** notes/RESULTS_STATE.md, “Open items”, “Settled in our registers”, and the headline run summaries.

| Exact ID and supplied status | Concrete bearing of these pages | Disposition |
|---|---|---|
| **LM1 D.11 — Open**, return's claim; cote 49 scans 608–610, task D.c | C12 gives the finite free \(\mu_2/\mathbf Z_2\) example: geometric component count jumps, and the binary restriction has two integral and two generic-only components; EC08 writes its idempotent equations. | A method-level warning for integral finite-group constructions, not an arithmetic descent datum or integral extension classification; remains Open. |
| **LM7 E.23 — Open**, return's claim; §51.16, scans 172–178, formulas (369)–(379) | The word “sections” here means sections of morphisms used in restriction, not the requested continuous arithmetic fundamental-group section classes; no comparison map to E.16 or its fibres is provided. | No status change. |
| **FLAGGED_149 B9 — Open**, return's claim; cote 149 scans 35–36 | Finite étale functors and group actions supply general language, but no hyperbolic-curve point pair, prime-to-\(p\) tower, or equality criterion occurs on these leaves. | No status change. |
| **LM4 D.12 — Open**, return's claim; cotes 25 bis/30, cited low-type torsion pages | The use of \(\pi_1(S,a)\) on 056–058 is a Galois-category framework and does not construct or classify torsion in profinite \(GT_0\). | No status change. |
| **LM4 F.7 — Open**, return's claim; §30, scans 383–387 | No mapping-class centralizer, nonsolvable finite subgroup, or comparison between discrete and profinite centralizers is identified here. | No status change. |
| **SECTIONS_OVER_Q A.185 — Proved**, return's claim | C23 identifies the product/group formalism relevant to stating Weil-restriction isogenies; its specific Prym curves, fields, maps and rank contribution are absent here. | Retain the supplied status; do not re-derive or claim verification of the arithmetic result. |
| **MPL_31_002-051 N070 — first-pass self-flagged lead** | The noetherian/local-noetherian and finite-presentation changes in 026, 044 and 050 merit the same hypothesis audit; C01–C02 and the early/middle notes locate them. | Adds exact local checks, not a theorem imported from the previous note. |
| **MPL_131 RN001/§2 and §10 — first-pass leads** | The supplied register points to representability criteria and I.VI construction techniques, giving a comparison target for the Murre-based argument in the letter. | Underlying cote 131 sources were not supplied here; no identification of full theorem hypotheses beyond the excerpt is asserted. |

The headline programmes EXIT_TOWER, SECTIONS_OVER_Q, LM4_SUCCESSOR, FINMON, and the later anabelian/Fermat updates concern specified towers, arithmetic sections, group centralizers or finite homotopy models that these leaves do not identify. Their shared words “functor”, “group”, “descent” and “section” are insufficient to assert a proof, contradiction, anticipation, or status change. The same limitation applies to the register's referee-qualified GT chain: this package neither rechecks nor extends those conclusions.

## P03 — Response to the planning questions

**Kind:** unpursued implication / bounded programme comparison. **Sources:** cote 91, scans 019–058, especially 026, 031–032, 034, 037 and 040–058. **Search record:** P03, supplemented by C24. **Context:** README.md; earlier package NPLAN-01; later package RN118-01, RN126-01, RN128-01 and RN131-01–RN132-02; Hua, VII and IX.

| Planning theme | Evidence in this interval | Assessment |
|---|---|---|
| Book I I.VI: descent and representable functors | Rigidified Hom, the letter, restriction, affine construction, gluing, Grassmannian models and permanence properties. | Directly confirmed as the central subject. |
| Hom by nonprojective methods | Proper sources, finite or infinitesimal test pieces, normal-flatness hypotheses, and the letter's comparison with Matsumura. | Directly confirmed, with unresolved proof steps and important scheme-valued descent qualifications. |
| Greenberg | Scan 034 names generalizations and Greenberg complements; scan 037 names Greenberg in equal characteristic. | A programme and construction-method bridge here; Hua's later VII develops the local-functor adjoint, and the later supplied notes place actual thick-point/rational-map claims on 126, 128 and 131–132. |
| Néron | The word is not present in the frozen retained text; later supplied notes locate “Espaces de Néron” on 118 and the “Greenberg / Néron” title on 124. | The catalogue title is broader than these particular leaves; no Néron model is constructed here. |
| \(K_G(X)\), residue-duality theory, numerical intersections | None of these constructions is carried out on the retained leaves; the intersection question on 039 concerns subsheaves, not an intersection pairing of cycles. | No direct confirmation of those wider topics from this interval. |
| S19: the remaining Book I material is small | The interval contains substantial representability work and several explicit open tasks, but does not measure the unpublished remainder of the archive. | This bounded sample cannot validate or refute the proposed global size estimate. |

Archive order and the one dated letter do not date every surrounding draft or prove that the two outlines belong to one continuously paginated text.
