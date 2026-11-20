# Final consistency review A: scans 019 and 020, with scan006 proof qualification

## Scope and outcome

This is a read-only review against the accepted audit decisions. No image was opened, no fresh ink choice was made, no mathematical certificate was rerun, and no TeX compilation was performed. Only this review file was written.

The final pages contain all six accepted scan019 page edits and all seventeen accepted scan020 page edits. All nine scan019 comparison finals and all twenty scan020 comparison finals agree exactly with their adjudication records; their adjudication and ink fields agree as well. The corresponding reviewed-report audit entries agree with those records. All report_replace fields currently match the reviewed reports.

The remaining discrepancies are principally stale descriptive metadata. The substantive examples are the scan019 three-versus-five uncertain-index count, the scan019 bracket description and certainty about produits, the scan020 definite-prime description, and the scan020 coverage claim that the whole of system (8) is cancelled. The current quoted readings themselves generally carry the accepted uncertainties correctly.

Scan006 needs an explicit assumption statement in its own proof documentation. Its computational inputs are fixed preferred readings, while the relevant scan005 indices remain uncertain. The successful reductions do not adjudicate those indices.

All JSON array indices below are zero-based. Stable IDs and coverage row numbers are supplied where available.

## Sources reviewed

The authority for accepted readings was:

- [Scan019 adjudication](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/second/145_scan019_adjudication.json), especially boxes B01, B03, B04, B07, B08 and B11.
- [Scan020 adjudication](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/second/145_scan020_adjudication.json), especially boxes B07, B09, B12 and B15–B21.

These were checked against:

- [Scan019 final page](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/pages/145_scan019.tex), [reviewed report](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/reader_reports/145_scan019_reviewed.json), and [comparison](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/second/145_scan019_comparison.tsv).
- [Scan020 final page](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/pages/145_scan020.tex), [reviewed report](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/reader_reports/145_scan020_reviewed.json), and [comparison](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/second/145_scan020_comparison.tsv).
- The Scan006, Scan019 and Scan020 sections of [the mathematical and reading notes](sandbox:/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/SP75_C13_145_notes.md), the corresponding reviewed-report notes and check events, and the relevant word-certificate documentation.

## 1. Scan019: proposed synchronization

### 1.1 Layout: later brackets are still called underbraces

**Field:** layout.

The phrase “a long derivation with two underbrace labels” contradicts accepted B08 and the current page, which use two flat brackets. The earlier square-verification annotation remains a genuine cusp-shaped underbrace.

**Exact replacement within the field:**

> a long derivation with two flat bracket labels

Replace only “a long derivation with two underbrace labels” with that text.

### 1.2 Hand summary: the uncertain-index count is obsolete

**Field:** hand[0].

It says “three live indices in (8)”; accepted B01 now qualifies five live indices, with another independent 1/0 doubt after the square-verification brace.

**Replace the entire field with:**

> Dark retracing can combine a straight index with earlier looped forms. Five live indices in (8) remain uncertain: the final l index in row 1 is 1/0; the first l and sigma indices in row 2 are each 1/infinity; the final l index in row 2 is infinity/0; and the final l index in row 3 is 0/infinity. The l index after the square-verification brace separately remains 1/0. The expected cyclic pattern does not resolve any of these readings.

This restates the accepted alternatives and introduces no new choice.

### 1.3 Hand summary: produits is asserted too strongly

**Field:** hand[3].

The present conclusion, “The forms support produits and relations against H’s singular readings,” conflates the still-clear plural relations with the reopened produits/produit/quotient locus.

**Replace the entire field with:**

> A terminal s can be a small hooked continuation after a tall t or a compressed word body. Relations retains its plural reading. After the inserted comme, the opening loop and terminal turn leave produits / produit / quotient unresolved; neither the word nor its singular/plural ending is certified by this handwriting observation.

Authority: accepted B07; current changes s019-13 and doubts[18].

### 1.4 Coverage row 18: obsolete count and location claim

**Field:** diff_coverage[row=18].explanation, currently array index 17.

The current text says “the three newly doubtful live subscripts are in doubts only.” There are now five, and their alternatives appear in the final page and in the complete current reading quoted by s019-01 as well as the doubt register.

**Replace the explanation with:**

> H’s note about heavy retracing is editorial and not transcribed. The five cancelled superscripts are recorded in s019-01. Five live-subscript uncertainties in (8) are explicitly retained in the final page and doubt register, with no separate ink resolution inferred from their expected cyclic order.

Keep its macro/editorial status: the row being classified is H’s editorial retracing note.

### 1.5 Location labels should not present preferred indices as settled

These do not change any exponent reading, decision status, confidence, crop, or coordinate. They make the identifying prose agree with accepted B01.

| Field | Current identifying text | Proposed identifying text |
|---|---|---|
| unlisted_decisions[id=U019-02].ink, opening phrase | At row 1, final l1, | At row 1, final l with subscript 1/0, |
| unlisted_decisions[id=U019-03].ink, opening phrase | At row 2, first l1, | At row 2, first l with subscript 1/infinity, |
| unlisted_decisions[id=U019-04].ink, opening phrase | At row 2, final l-infinity, | At row 2, final l with subscript infinity/0, |
| unlisted_decisions[id=U019-05].ink, opening phrase | At row 3, final l0, | At row 3, final l with subscript 0/infinity, |
| doubts[3].place | (8), row 2 final l-infinity exponent | (8), row 2 final l exponent, whose subscript remains infinity/0 |
| inventory[element=I18].position | (8), row 2 final l-infinity superscript | (8), row 2 final l superscript, with subscript infinity/0 |
| inventory[element=I26].position | comme before produits, above the cancelled short product | comme before the doubtful produits / produit / quotient, above the cancelled short product |

For the four unlisted decisions, retain the rest of the existing ink sentence unchanged. These are location-label synchronizations, not new certainty-only change rows.

### 1.6 Historical root-review description

**Field:** root_review.crops_viewed.

Its references to “three overwritten current indices” and “plural produits” describe the first-pass outcome. They should not be silently rewritten as if that first-pass review had already reached the audit’s later decisions. If this field is presented as part of the current final summary, add an explicit historical label and the following qualification:

> This describes the first-pass root review. The subsequent blind audit broadened five live indices in (8), reopened produits / produit / quotient, and distinguished the two later flat brackets from the earlier cusp-shaped underbrace.

The same distinction applies to the report’s sealed first readings. Their older readings are expected historical data.

### 1.7 Fields already synchronized

The six listed decisions, the expanded cancelled-phrase alternatives, the final définition/définit doubt, the final gén without stop, the current inventory quotations, and the two separate gén./gén abbreviation entries agree with the accepted audit. No further reading replacement is proposed in those fields. In particular, keep the readable later post-rho factors separate from the explicitly unrecoverable earlier layers.

## 2. Scan020: proposed synchronization

### 2.1 Notation still certifies the high sigma mark as a prime

**Field:** notation[1].

The opening sentence says “sigma bears a prime.” Accepted B17 retains prime/numeral 1, while excluding an inverse at that height.

**Replace the entire field with:**

> In the live introduction to (7), the high sigma mark remains prime/numeral 1; no minus is written at that height. The lower permutation index has dotted rho with exponent -1 and argument (i). Dotted rho also occurs in both relevant lines of (7). The earlier cancelled sigma formula retains its separate index doubt.

Authority: accepted B17; M0841; s020-22; doubts[20].

### 2.2 Hand summary repeats the definite-prime wording

**Field:** hand[3].

**Replace the entire field with:**

> A high mark can appear as a single upright dark tick. The sigma mark in the introduction to (7) has no minus and remains prime/numeral 1. It is distinct from the lower index’s explicit minus and 1; H’s interpretation of the high mark as an inverse is not retained.

**Related minor synchronization:** hand[1] uses “as in un des” as an unqualified example. Replace only that phrase with:

> as in the compressed donc un / un des locus

The broader handwriting observation and the p.v./p.r. doubt can remain unchanged.

### 2.3 Notes still print a definite k in the inserted tuple

**Field:** notes[2], and its matching paragraph in the Scan020 notes section.

Replace the sentence:

> The insertion physically reads (i,j,k) distincts), with an extra unmatched close.

with:

> The insertion physically reads (i,j,k/h) distincts), with the third letter uncertain and an extra unmatched close.

The accepted mathematical transcription remains \inserted{(i,j,\unsure{k|h})\text{ distincts})}. The extra closing parenthesis is authorial and must not be “repaired.”

### 2.4 Coverage row 53 contradicts the accepted cancellation scope

**Field:** diff_coverage[row=53], currently array index 52.

It currently says that “the entire display is cancelled in both witnesses and the manuscript” and treats outer strike placement as a macro choice. Accepted B21 explicitly rejects a blanket manuscript deletion and separates the local states.

**Proposed row:**

- row: 53
- status: substantive
- change_id: s020-40
- related_change_ids: s020-35, s020-36
- explanation:

> The aligned/cases wrappers are typesetting alternatives, but the blanket outer deletion is a substantive state difference. Both witnesses treat system (8) as wholly cancelled; the accepted audit instead preserves the crossed number, uncertain cancellation scope on the first two labels and the second row’s initial factor, the locally cancelled first-row exponent clusters, and the second-row replacement l1. The third row ends in bare l-infinity and is not enclosed in a blanket deletion. See s020-40, with s020-35 and s020-36 for the local readings.

This is the principal remaining coverage contradiction on scan020.

### 2.5 Two change-location labels retain the superseded description

The final readings and ink accounts in these rows are already updated. Only the place fields need synchronization:

| Stable row | Proposed place |
|---|---|
| changes[id=s020-35] | System (8), first row and local cancellation states |
| changes[id=s020-36] | System (8), third-row final bare l-infinity; apparent exponent reassigned to the second-row replacement |

This removes the obsolete “Cancelled relation (8)” and “final right exponent” descriptions without changing the accepted readings.

### 2.6 Fields already synchronized; historical fields to preserve

The current listed/unlisted decisions, doubts, inventory E38–E43, etc/chgts abbreviation entries, current correction readings, and the restored Noter que agree with the accepted audit. The right NB’s cancelled exponent is represented, and the second-row l1 replacement is distinct from the third row.

The following are historical witness or first-pass records and should not be overwritten with audited readings:

- unlisted_decisions[].source_mark;
- c_markup_audit.deleted_details[].source and inserted_details[].source;
- the counts of C’s original marked spans;
- sealed first/second readings and the report’s original second_boxes readings;
- comparison first and second columns.

In particular, the blanket deletion inside c_markup_audit’s source quotation records C’s markup. It is not the same problem as coverage row 53’s assertion about the manuscript.

The root_review.crops_viewed description may be explicitly labelled “first-pass root review” if rendered as a current summary. Its historical “prime against inverse” statement must not be taken to eliminate the subsequently accepted numeral-1 alternative.

## 3. Mathematical notes: conditional scope

### 3.1 Scan019: the audit supplies the required condition, but isolated proof paragraphs should carry it too

The current notes[14] already says that the free-word checks use the preferred cyclic indices conditionally and cannot select them from the ink. Accordingly, the complete note section does not resolve the new doubts by algebra.

For a self-contained proof account, qualify the earlier paragraphs and event summaries at their point of use:

- **notes[12]:** replace its opening “Main-reader targeted algebra check in the local convention linfinity l1 l0=1:” with:

  > Main-reader targeted algebra check conditional on the preferred cyclic indices in (8), the preferred post-brace index 1, and the local convention linfinity l1 l0=1:

- **notes[13]:** replace its opening “The included check_019_words.py separately verifies” with:

  > Under the same preferred cyclic-index assumptions, the included check_019_words.py separately verifies

- **check_events[statement_id=145-019-square-and-product-expansion].outcome:** prepend:

  > Conditional on the preferred cyclic indices in (8) and the preferred post-brace index 1.

- **check_events[statement_id=145-019-automorphism-images].outcome:** prepend:

  > Conditional on the preferred cyclic indices in (8).

Propagate the two note-paragraph qualifications to the matching Scan019 notes section. Keep the existing limitation to automorphism images and the warning about changed loop-product convention. These are scope clarifications of an existing computation, not new checks or new events.

The certificate’s present encoding and scope do not enumerate the uncertain-index assumptions themselves. The companion reviewed note should supply that qualification whenever the certificate is cited independently.

### 3.2 Scan020: existing conditional treatment is adequate

The current note explicitly compares both initial-rho exponent states in the marginal l-infinity formula, reports agreement for the cancelled-exponent interpretation and failure for the live inverse interpretation, and states that this does not authorize erasing the ink ambiguity.

The certificate separately labels the failing live-inverse comparison as a candidate comparison whose ink state must be decided from the manuscript. The C3 quotient argument is also limited to the sigma presentation; it does not claim the same obstruction for the later epsilon generators.

No mathematical-note reading correction is proposed for scan020. Keep both exponent states in the transcription and avoid using the word calculation to infer the scope of cancellation in (8).

### 3.3 Scan006: qualification is needed in the local proof account

**Files/fields:** reviewed report notes[6], notes[7], check_events[0].outcome; the matching Scan006 notes paragraphs; and the descriptive header of scripts/check_006_words.py.

The current notes[6] says “the generator images written on scans 005–006 give” the identities. The script header says it uses “exactly the generator images on scans 005–006.” Neither locally states that the preferred readings of the unresolved scan005 indices are assumptions. The certificate records the fixed input encoding and successful reductions, but has no assumption qualification. The separate Scan005 audit note already qualifies the later check; the Scan006 account should be equally explicit.

The script’s assumed maps, read without execution, are these. Put a=l0, b=l1, c=(ab)^-1. Then:

| Map | Image of a | Image of b |
|---|---|---|
| rho | b | c |
| sigma-infinity | b | a |
| sigma0 | b^-1 c^-1 | c |
| sigma1 | c | c^-1 a^-1 |

These are computational inputs, not further findings about uncertain ink.

**Proposed full replacement for notes[6]:**

> The main reader performed a conditional free-word check of the three displayed inner-conjugation identities, taking the preferred cyclic readings of the still-uncertain scan005 indices as assumptions. With a=l₀, b=l₁ and c=l∞=(ab)⁻¹, the code assumes rho(a)=b and rho(b)=c; sigma-infinity(a)=b and sigma-infinity(b)=a; sigma0(a)=b⁻¹c⁻¹ and sigma0(b)=c; and sigma1(a)=c and sigma1(b)=c⁻¹a⁻¹. Under these assumed maps, free reduction gives σ₀σ₁=int(b⁻¹)ρ, σ₁σ∞=int(c⁻¹)ρ, and σ∞σ₀=int(a⁻¹)ρ on both free generators. The calculation and reduced-word output are saved in scripts/check_006_words.py and reader_reports/145_scan006_word_check.json. This verifies the identities for the stated interpretation; it does not determine the uncertain scan005 indices, prove the exterior-action realization claim, or normalize the doubtful fixed-point expression.

**Within notes[7], replace:**

> This does not change the verified inner-conjugation identities;

with:

> This does not change the conditional inner-conjugation calculation under the assumed preferred cyclic generator maps and does not resolve the remaining scan005 indices;

Keep the rest of the audit-history paragraph intact.

**Proposed replacement for check_events[0].outcome:**

> Executed free-word substitution and adjacent inverse cancellation on l₀,l₁ for all three displayed cyclic identities, conditional on the preferred cyclic generator maps specified in the proof note. Left and right images agree in each case under those inputs. This does not adjudicate the uncertain scan005 indices. The original script and reduced-word output are included.

**Proposed descriptive script-header text, if its documentation is synchronized:**

> Local free-word calculation conditional on the preferred cyclic generator maps from scans 005–006. The remaining scan005 index doubts are not resolved by this calculation.

No computational code, reduced words, equality result, event identity, or event count needs alteration or rerunning.

## 4. Structural checks without compilation

The checks distinguish escaped literal braces from grouping braces and ignore comments. They test environment nesting, display delimiters, dollar parity, and left/right counts. They do not attempt TeX expansion or visual rendering.

| Final page | Grouping brace net | Unescaped dollar count | Display opens/closes | Left/right | Environments checked |
|---|---:|---:|---:|---:|---|
| Scan019 | 0 | 30, even | 7 / 7 | 4 / 4 | aligned ×3; gathered ×1; tikzpicture ×2 |
| Scan020 | 0 | 64, even | 9 / 9 | 2 / 2 | aligned ×5; tikzpicture ×6 |

No grouping, environment, or delimiter-parity error was found in either final page.

The same checks passed for 90 current reading/quotation fields on scan019 and 148 on scan020, comprising change finals, decision readings, doubt readings, inventory quotations, and adjudication finals.

Two scan020 page-edit entries are intentionally context-dependent replacement fragments:

- page_edits[3] replaces text ending with a closing dollar; both old and new fragments have one dollar.
- page_edits[6] replaces text ending with an opening display delimiter; both old and new fragments are incomplete displays in isolation.

These fragments are not standalone TeX passages. Their application is present in the balanced final page, so they require no “parity repair.” Likewise, the author’s extra close in the (7) tuple is accepted manuscript punctuation, not an unmatched TeX group.

## 5. Application boundaries

All proposed changes above are metadata synchronization or explicit qualification of computational assumptions. They do not alter an accepted ink decision.

If root applies them, fields already mirrored under adjudication.report_replace should be kept consistent with their reviewed-report counterparts, or explicitly recorded as a subsequent metadata correction. Layout and notation were not among the existing report_replace keys. Matching note paragraphs should then be refreshed in the aggregate notes.

Preserve all sealed first and second submissions, their crops and manifests, historical witness/source quotations, and the accepted comparison/adjudication final and ink fields. No fresh crop, new ink adjudication, proof rerun, compilation, or new mathematical check event is required by this review.
