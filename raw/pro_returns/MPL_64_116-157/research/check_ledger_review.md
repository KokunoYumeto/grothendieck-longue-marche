# Check-ledger consolidation review

Author: GPT-6 Astra Pro; effort inherited, runtime effort value not exposed; run `MPL_64_116-157/modular_context`. Date: 2026-11-18 UTC.

## Initial consolidation

The initial merge included five source ledgers: `analytic_review_events.tsv`, `arithmetic_events.tsv`, `connections_events.tsv`, `modular_events.tsv`, and `root_events.tsv`. It produced **198 unique events**, with **direct event coverage for all 71 main-note IDs**, no missing IDs, no malformed rows, no invalid dates, no unrecognized types, and no exact duplicate rows. Additional source ledgers are incorporated by rerunning the same script; the timestamped `check_ledger_coverage.json` and `check_ledger_coverage.md` report the current merge rather than this historical initial count.

The first merge normalized 84 rows: 45 date spellings, 29 explicit run-label additions, 10 type aliases, and 10 statement-ID aliases, with some rows having more than one change. No documentary row required reclassification in that initial merge. Each original and normalized field, source-file hash, and source row number is retained in the coverage JSON.

The subsequent strict merge incorporated the ten events in `connections_review_events.tsv`, giving **208 unique events from six source ledgers**, still with **71/71 direct note coverage**, zero exact duplicates, and no validation errors or warnings. That ledger's targeted checks, computation, and carried Katz-theorem background retain their stated types; its ten UTC timestamp spellings bring the number of normalized rows to 94. The `--require-complete` gate passed after inclusion of this independent review.

**Final principal-researcher rerun, 2026-11-18:** the additional `INTEGRATION.final_scope` event records adoption of the review's parameter-base specialization wording and the finished S06 target clarification. The final ledger therefore contains **209 unique events**, with the same six sources, **71/71 direct note coverage**, and zero errors, warnings, or duplicates. The coverage JSON records the final assembled notes hash.

## Reproduction

Run from the package root:

```sh
python scripts/merge_check_events.py --require-complete
```

The script discovers every `research/*events.tsv` source ledger afresh, writes the derived `CHECK_EVENTS.tsv`, and regenerates the Markdown and JSON coverage reports. It does not read or write the frozen transcription, page files, or doubts. Source ledgers remain unchanged, so additions or corrections belong in the applicable source ledger rather than in the derived master.

## Normalization policy

- The five exact fixed types are `targeted proof check`, `independent re-proof`, `computation or formal certificate`, `used and rechecked in this run`, and `carried as background without fault found`.
- Refutations retain the **actual refinement ID** in the type, validated against `^refuted, with refined statement \S+$`; for example, `refuted, with refined statement A03.R`. A generic literal `id` is not accepted unless an actual refinement ID can be recovered from an explicitly labelled outcome and restored to the type.
- The legacy spelling `used and rechecked` becomes `used and rechecked in this run`; this changes no verification level. No independent review is upgraded from a statement lookup or targeted check to an independent re-proof.
- Only obvious register/context namespace aliases are normalized, such as `LM2.C.d1` to `LM2 C.d1`, `EXIT_TOWER.E.24` to `EXIT_TOWER E.24`, and `MPL_149_091-136.RN099-03` to `MPL_149_091-136 RN099-03`. Local proof, appendix, and literature IDs are preserved.
- Explicit UTC timestamps become ISO 8601 UTC timestamps. A day-only date remains day-only; no event time is invented.
- The modular ledger and the independent analytic-review ledger receive the explicit run label `MPL_64_116-157/modular_context`, reflecting their actual authoring track. Existing model and inherited-effort wording is retained.
- C/R/U inventory notes are documentary and are classified as carried background, not mathematical proofs; any such change is disclosed in the normalization record. Supporting mathematical checks remain separately logged under their actual proof or computation IDs.

## Validation and coverage meaning

Each input must have the exact five-column header, five nonempty fields per event, a valid date, and an allowed type. Embedded tabs or newlines in fields are rejected so the output also has five physical columns. The script validates the written master and removes only duplicates of the entire normalized five-field row, retaining every duplicate's source provenance.

Direct main-note coverage comes from an exact note ID, a qualified sub-ID such as `A01.DVR` or `S03-C1-PF`, or a refutation's explicit refinement ID. Proof appendices expressly cited by a note, such as AC05, are recorded as supporting coverage but do not silently fill the direct-ID requirement. A carried-background event counts as a recorded use, not as a proof of the note's claim; coverage totals must not be read as proof totals.

Validation errors prevent replacement of the master and are written to the coverage report. `--require-complete` additionally returns a nonzero exit code when any main note lacks direct coverage; without that flag, a valid partial consolidation can be inspected while additional ledgers are still being prepared. Inputs are read as byte snapshots, and the recorded hashes correspond to the bytes actually parsed.

## Review boundary

This work checks and consolidates the event records; it does not independently certify the truth of every logged theorem or counterexample. The source outcomes' limitations, prior-claim status, and distinctions among proof checks, computations, source uses, and documentary comparisons remain intact.
