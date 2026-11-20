# Exact other-error alias proposal

**Prepared only; authoritative files have not been edited.** The current table
has 14 observation rows. The proposed table has 11 rows, removing exactly the
root-reviewed peer aliases for scans 042, 044, and 046. Each selected primary
row remains byte-for-byte the same after TSV serialization.

## Review files

- `OTHER_ERROR_ALIASES.json`: three explicit full-row pairs, their SHA-256
  hashes, and the source-report hashes. The scan042/044 canonicals are the
  existing first rows; scan046 uses the final primary-B row preserved in
  `deliverable/audit/parts/scan046_b.json`, with its peer report preserved at
  `deliverable/audit/scan046_peer.json`.
- `other_error_aliases.py`: small exact-match helper, with no similarity
  matching, normalization of text, alias chains, or reading inference.
- `reconcile.patch` and `reconcile.py`: proposed changes only. Both append
  paths normalize incoming rows through the registry before any output write.
  Existing noncanonical tables fail closed until an audited migration occurs.
- `proposal/before/` and `proposal/after/`: complete snapshots for the error
  table and reconcile script; the after side also includes the newly added
  registry and helper. Absence on the before side is explicitly recorded as a
  null hash, rather than a fabricated old file.
- `proposal/manifest.json`: SHA-256 hashes, installation order, row counts,
  removed alias IDs, and 476 protected existing audit/history/source-report
  text files. It also protects `decisions.tsv`, `CHECK_EVENTS.tsv`, and
  `progress.log`.
- `proposal/CORRECTION.md`: append-only correction of the false scan042/044
  historical claims and description of the scan046 pair. Historical notes
  and raw reports are untouched.
- `verification.json`: focused validation results and their limits.

## Apply after root review

From the workspace root, recheck the exact preconditions:

```bash
python work/error_alias_fix/apply_proposal.py
```

Apply the reviewed proposal:

```bash
python work/error_alias_fix/apply_proposal.py --apply
```

Then run the normal verifier:

```bash
python deliverable/scripts/reconcile.py verify
```

The apply command takes `work/reconcile.lock`, rechecks every before hash,
archives the complete proposal under
`deliverable/audit/other_error_normalizations/OE0001_exact_aliases_042_044_046/`,
and installs the helper, registry, table, and patched reconciler in that order.
`application.json` records prepared/completed status; the frozen proposal
manifest retains its original proposed status. All replacements are atomic
per file, and complete before snapshots exist before any replacement. This
is not a filesystem-wide atomic transaction; if interrupted, inspect the
application status and use the retained snapshots before retrying. The
script rejects an existing audit transaction and does not overwrite it.

If a subsequent page commit or audit update makes the proposal stale, it
fails before writing. Retain this proposal, update the proposal output path
in `prepare_transaction.py`, and prepare/review a fresh snapshot; do not
disable the preconditions.

## Verification scope

The existing verifier never read `other_errors.tsv` and never enforced an
exact union of report errors. The patch adds only an exact canonical/unique
table invariant. It cannot establish report-to-table completeness. No broad
union reconstruction is included.

The focused checks passed: 14 to 11 normalization; preservation of an
unregistered row sharing the same scan and reading; rejection of a changed
row with an old hash; actual patched commit/recommit and import/reimport
methods preserving 11 rows; unchanged raw primary/peer JSON; rejection of
unaudited aliases before any output write; and an actual transaction apply
in a disposable text-only copy, with all 476 protected hashes unchanged.
Mark/source/image validation was replaced by a minimal fixture for the
append-path checks. No images or later pages were inspected; the root should
run the ordinary full verifier after application.

## Future explicitly reviewed aliases

Add a new exact canonical/alias row pair and its hashes to the registry only
after root review. `row_sha256()` encodes the four string fields in fixed
order. Canonical text is never inferred. Archive the prior registry and any
table change in a new audit transaction. Both append paths will then suppress
that registered alias during later commits and reimports without modifying
the submitted reports. Unregistered wording variations remain distinct.
