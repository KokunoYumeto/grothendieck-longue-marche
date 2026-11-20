# Audit/freeze helper hardening

> Parser alignment follow-up 2026-11-19 21:12:23 UTC: malformed completion/audit-looking lines and duplicate identity fields are now rejected. Three focused synthetic checks passed. The original 28-test full run below is retained; the broader suite was not rerun for this narrow change.

Initial hardening completed: 2026-11-19 21:01:02 UTC.

**All five findings from the readiness review are fixed. All 28 isolated synthetic tests pass** (17 audit, 11 freeze). All changed Python files also pass AST parsing.

## Changes

1. **Equal preview/final validation.** Both paths validate complete record metadata and stage the same report projections before returning or publishing. Baseline/projection metadata and the full completion trail are checked again afterward. Preview publishes no live files/events and assigns no completion timestamp.

2. **Immutable inventory identity and allowed fields.** Every resolved inventory row must use its page's scan identity and the exact supported field set. Audit patches/additions reject another scan or unknown fields. An idempotent patch repeating the correct identity remains compatible.

3. **Complete audit gates.** Begin, finalization, and recovery validate the 106-page map, exact recursive page/record sets, page hashes, inventory confirmation, complete first-pass done-event order, and matching prior audit record/session/log evidence. Invalid timestamps, missing/overlapping/mismatched events and fabricated prior audit entries are refused. Recovery explicitly accepts only the selected unfinished session's coherent before/after states.

4. **Honest freeze write state.** Errors retain observed `written`, `write_attempted`, `prepared`, `committed`, `manifest_created`, `manifest_reused`, and `hash_block_appended` state. A partial preparation no longer reports that nothing was written. `written` is null only when an attempted write cannot be read back. A valid observed commit marker is distinguished even if a later flush raises.

5. **Pinned retry evidence.** New manifests retain `state_fingerprint_version=1` and `state_fingerprint`, including file/history/session bytes and recognized completion/audit event lines. Both preview and writing retries require the same evidence. Prepended/appended freeze hash blocks do not change the evidence pin.

An independent code review found an additional recovery corner case: a prepared session still marked started could be interrupted again after its completion log append. Recovery now saves commit_pending and the immutable completion timestamp before publishing. A dedicated two-interruption test passes.

## Compatibility

CLI flags are unchanged. Recovery now honors `--witness-root`, so its page-map metadata must be available. The existing two positional arguments of `resume_audit` remain valid; the new witnesses argument is optional.

Committed legacy schema-1 freezes remain verifiable. An uncommitted legacy manifest without a fingerprint is preserved and refused for explicit reconciliation. No unsafe replacement baseline is inferred.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s SP02_CW_10+12/scripts/tests -p 'test_*hardening.py' -v
```

The tests cover rejected inventory identities/fields, preview/final validation parity, missing/reordered first-pass events, recursive extra records, fake/unlogged prior audits, interrupted starts, mixed before/after commits, repeated recovery interruptions, freeze errors at several publication phases, changed history/event pins, unchanged retries, and legacy committed verification.

All fixtures contain 106 invented pages and invented metadata under temporary `work/helper_hardening_fixtures/` directories. Every helper call supplies explicit temporary output/map paths. Fixtures were cleaned up; no entries remain. Full output is in `helper_hardening_tests.txt`.

## Changed-file identities (current revision)

| File | SHA256 |
| --- | --- |
| `scripts/record_page.py` | `4169a107c15439e7e04c0947bbf363c151929d12f83e1c2ffa43102c0bee87c2` |
| `scripts/record_audit.py` | `7e3dc0cfa292c0aca4b9314a4ed42b4a794417c3e3b5d71c5efac510aeef4fa5` |
| `scripts/freeze_transcription.py` | `8fa9d75703cd037f6464898079027188049008e20f9b8dd121541531c83c2ba3` |
| `scripts/README_tools.md` | `5e08b08ade036ec31561e9c6d09e0765d435514818cfbf722e223f632d824f89` |
| `scripts/tests/test_audit_hardening.py` | `66599efe33538b7723a36d1555d4003d407222957cf1661e12a494ec6177b3a4` |
| `scripts/tests/test_freeze_hardening.py` | `a33e806c7bdcbd2390926533451fbc9a362acbfc690ef711fc5fcb4f1f4aeb11` |

Only helper code, documentation, tests and evidence were written. No live audit/freeze command, completion event, page record, transcription, witness prose, image, context, package, or upload was touched. The separate bounded scan083 check reads only its authorized metadata, root-authored inputs, page bytes and lexical structure.


## Parser alignment follow-up — FREEZE-PARSER-1

2026-11-19 21:12:23 UTC. Freeze parsing rejects malformed completion/audit-looking lines and duplicate identity fields before readiness/fingerprinting, matching the audit parser. The two new regression cases reject direct readiness and writing retries without changing the synthetic manifest/log. The focused unchanged-retry test passes and verifies all 107 synthetic files. CLI flags and live state are unchanged. See `helper_hardening_parser_tests.txt` for the three-test output. No broader review/test cycle was run.
