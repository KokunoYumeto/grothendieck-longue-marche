# Audit image-first helper verification

**PASS** — 2026-11-20 08:18:49 UTC

- Ten isolated synthetic protocol tests passed (zero failures/errors).
- No live receipt directory or audit session was created.
- Existing audit, freeze and package helpers were not changed.
- All 204 existing page/record files in the 102-page baseline remain byte-identical.
- Root finalized132 concurrently at 2026-11-20 08:13:39 UTC; the three generated reports and progress.log changed with that announced finalization. These are reported separately, not falsely described as unchanged.
- Helper SHA256: cd98f553a6153e0b060b7e53fbd39cb1877981d43f5e9d2e1de44df1e3da91ea.

The synthetic checks cover successful receipt creation and idempotent retries, exactly one started session, baseline/declaration/client-time rejection, immutable observations, missing first receipt and wrong page, strict timing, every completed audit and repeat audits, tampering/orphans, frozen/context write guards with read-only validation, symlinks and duplicate JSON fields. Fixtures contain no manuscript or image files and are removed afterward.

## Scope and limitations

Receipts record root declarations and actual helper-call UTC times, not proof of visual attention. Text-open marking records intent immediately before the actual text is opened. Completion timestamps in existing audit sessions have only second precision: an indistinguishable same-second completion is rejected by strict validation. This helper is not yet wired into existing audit/freeze/package commands.

Detailed artifact hashes, protected-input accounting and the exact test command are in the companion JSON.
