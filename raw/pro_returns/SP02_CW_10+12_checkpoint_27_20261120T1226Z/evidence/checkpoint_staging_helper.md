# Reusable checkpoint staging helper

2026-11-20 02:49:19 UTC

New reusable mechanical checkpoint staging helper plus focused synthetic tests only; no live staging, image/witness/context inspection, reading decisions, audit/freeze, archive creation or upload.

## Behavior

- Default snapshot-only mode writes nothing and does not claim completed staging.
- Explicit expected count/last key and exact map-prefix page/record correspondence; stored page hash and record key agreement.
- Explicit provisional documentation paths are hashed only; no root observations generated.
- Existing refresher, assembler and lexical checker run only with --write.
- Protected page/record/report/event files, source-copy set, selected provisional files and page-map metadata are checked between stages and at completion.
- Evidence uses exclusive names; --label permits a distinct later snapshot at the same page count.
- No package, upload or scheduling interface; root coordinates provisional facts and the due time.

## Focused validation

Five temporary synthetic fixture tests passed in 0.028 seconds, exit code 0. No older broad suite was rerun.

- default snapshot check writes nothing
- successful staging preserves protected files and creates exact combined bytes
- concurrent protected change stops before assembly
- unrecorded page rejected before staging
- existing evidence preserved before refresh

## Files

| File | SHA-256 |
|---|---|
| `scripts/prepare_checkpoint.py` | `6e062886ab0c449af081163e5e888d2ffecb67e20c50f0a7da3cab24b52dd62f` |
| `scripts/tests/test_prepare_checkpoint.py` | `ba0c906aa5178ac53bf94b111d32dd9edaf2b9760c37fbff39595eb50653f830` |
| `scripts/README_tools.md` | `64f073bef67dae4e5fc3b64b09c56b91e42c52296dc76eeec081ab45f3ab1b74` |

No checkpoint15 staging or package created by this task. Await current root-provided provisional files/facts and due-time packaging authorization.
