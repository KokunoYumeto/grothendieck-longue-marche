# Staged PDF delta target ceiling: 16 to 23

This proposal changes one recovery constant from 16 to 23 and updates two matching documentation phrases. It is not installed. The complete original helper bytes are retained under `before/`; `proposed/` contains the three replacements. `CHANGE.json` identifies every literal and its exact before/proposed hash.

The depth-one COPY/LITERAL format, 64 MiB input limits, named-book authority rules, primitive full-PDF bases, disjoint base/target sets, alias rules and exact target reconstruction checks remain unchanged. The native PNG and indexed-overview recipe contracts are unchanged.

## Executed controls

`CONTROLS.json` records 39 passing focused controls. The synthetic profile qualifies 23 distinct targets against five full bases and recovers all 52 logical files with Git absent from the recovery process PATH. The former nine- and sixteen-target profiles still qualify. Twenty-four targets are rejected at both builder and recovery-inventory boundaries. Negative cases retain exact source-checkpoint and named-book authority, size, primitive-base, overlap, chain and codec checks.

All synthetic PDFs, ZIPs, raw process output and restored fixture trees remain outside this stage. `STANDALONE_RESTORE.json` is an exact copy of the successful synthetic recovery report. The declared `external-runtime/` namespace records their identities without retaining fixture payloads or machine locations. No production checkpoint, current publication PDF or future revision878 plan was used.

## Reproducible focused execution

From the project root, use a new empty directory outside the project for `EXTERNAL_EMPTY_DIRECTORY`:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B work/records/checkpoint_pdf_delta_target23_staged_v1/check_controls.py --project-root PROJECT_ROOT --runtime-directory EXTERNAL_EMPTY_DIRECTORY
```

The result was already executed and is pinned by `PROVENANCE.json`; rerunning is not an installation prerequisite. Preserve the existing result if another execution is needed.

## Installation prerequisites

The parent workflow must verify the exact active before hashes, the independent review and the final handoff. Only then may it install the three proposed helper copies. This stage does not authorize a concrete PDF-delta plan. Once revision878 PDFs are stable, any plan must pass the unchanged exact book identity, archive privacy, whole-archive size, primitive reconstruction, PNG/RGB reproof and complete standalone recovery gates. No storage saving or future archive fit is claimed by the cardinality change.

All source, publication, snapshot and actual-review evidence remains unchanged.
