# R1 final documentation audit — scans 002–008

## Scope and method

This was a read-only documentary audit of the gated records for scans002–008 and their assembled deliverables. It examined the classification and event coverage of mathematical claims, consistency between the records and assembled notes/tables, and required delivery content. Scan009 was still under main adjudication and its unfinished main outputs were excluded. No consolidated record or page was edited. No compilation, rendering, OCR, external research, or new image inspection was performed.

The findings below preserve the observations as originally reported to main. The subsequent addendum records fixes reported by main; it does not claim that R1 independently re-audited those fixes.

## Mathematical claims and check-event coverage

No missing CHECK_EVENTS coverage or overstated proof classification was found in the scoped notes themselves. All **25 numbered statements** had event coverage. All **43 scoped events** and all record-note paragraphs matched the assembled ledger and notes. The notes explicitly separated broad manuscript reconstruction assertions from the small targeted checks, and retained the conditional limits on the uncertain AtM4 adjective and on the compatibility component of the reverse implication.

The scoped collation had **306 rows**, matching the sum of the records’ `diff_H` decisions. The inventory had **227 rows**, matching the scoped record inventories, with `transcribed=yes` throughout. Required TSV/CSV columns were present and their cells were populated. The seven gated page fragments occurred exactly in the assembled transcription, in scan order, without a document preamble. These are documentary checks, not mathematical proof events.

## Original concrete findings

### 1. Consequential summary overstated the uncertain letter in 005-22

In `records/scan005.json`, decision **005-22** retained:

```tex
F,\unsure{C|G}
```

Its `math_consequence`, also reproduced near the top of the assembled changes log, nevertheless said:

> The initial pair is F,C, but the following equivalence uses G. Retain the literal mismatch.

That asserted C and a definite mismatch more strongly than the adjudicated reading permitted. The suggested replacement was:

> The initial pair retains C|G, with C preferred; if C is the written letter, it differs from G in the following equivalence. The ink uncertainty is preserved.

The notes for **005-N3** already distinguished the checked F/G equivalence from the unresolved preceding glyph correctly.

### 2. Five decision-level doubt statuses contradicted their evidence and audit entries

The following rows had `C_doubt_status: "resolved"`, although their final readings retained the original uncertainty, their evidence explicitly said the doubt remained, and their corresponding `C_doubt_audit` entries correctly said **retained**.

| Decision | Retained final reading | Suggested documentary adjustment |
|---|---|---|
| 004-16 | `\unsure{déf|def}` | Set decision-level status to `retained`. |
| 005-09 | `\deleted{\unsure{$\mathscr F$}}` | Set decision-level status to `retained`. |
| 005-22 | `F,\unsure{C|G}` | Set decision-level status to `retained`. |
| 008-05 | `\unsure{des'|des|d'}` | Set decision-level status to `retained`. |
| 008-23 | `\unsure{\exists}` | Set decision-level status to `retained`. |

All five already had `diff_C: false`. Their reading, evidence, and C-doubt audit needed no alteration for this correction.

### 3. Scan004 abbreviation wording contradicted the retained accent doubt

The abbreviation entry in `records/scan004.json`, reproduced at line169 of the then-current `SP35_CW_156-7_doubts.md`, said:

> Form: `def`  
> Location: “004, both equivalence labels, unaccented”

This conflicted with **004-16**, the remaining-doubts table, and the page fragment, which retained **déf|def** for the first label. **004-17** resolved only the second label as unaccented `def`.

The suggested wording was:

> Form: `déf / def`  
> Meaning: définition  
> Location: “004, first equivalence label retains the accent doubt déf|def; second label is unaccented def.”

### 4. Three encountered abbreviation groups were absent from the assembled list

| Missing entry | Documentary occurrence within audited pages | Proposed expansion |
|---|---|---|
| NB / NB. | Scan004 margins; scan008 NB paragraphs | *nota bene* |
| Sup / sup | Scan005 At1/At2; scan004 supremum margin; scan008 cancelled intersection formulas | supremum |
| Cor | Scan008 cancelled corollary heading and reference | corollaire |

These entries could be added without changing any transcription.

### 5. Required legibility and witness-comparison section remained a placeholder

Under `## Legibility and witness comparison`, the then-current doubts file contained only:

> Assessment pending the complete collation.

The governing deliverable requires a short assessment of legibility, the least trusted portions, and the comparison between witnesses. Main acknowledged that this section would be completed during finalization after scan009.

### 6. Package-validation row count was stale

The then-current `records/package_validation.json` reported `collation_rows: 312`, while the current scoped collation TSV and the sum of scoped record decisions gave **306**. Main acknowledged that the package validator would be rerun after scan009. This was a stale validation summary, not a mismatch between the current collation and its gated records.

## Addendum — fixes reported by main

In the assignment requesting preservation of this report, main stated that it had applied:

- The five decision-level status corrections listed in finding2.
- The conditional qualification of **005-22** listed in finding1.
- The scan004 abbreviation wording correction listed in finding3.
- The **NB**, **Sup**, and **Cor** abbreviation entries listed in finding4.

Main also reported that legibility and counts were being finalized. R1 was explicitly instructed that no new audit was needed. This addendum therefore records main’s report of the changes; R1 has not independently rechecked the revised files as part of this save operation.
