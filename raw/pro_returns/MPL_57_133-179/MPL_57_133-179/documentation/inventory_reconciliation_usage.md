# Inventory reconciliation — prepared, not applied

`reconcile_inventory.py` reads only page-fragment text and the existing inventory. It does not access images or context and never changes the page fragments.

## Commands after the visual audit

Generate a fresh candidate and reports:

```bash
python /workspace/scratch/641dc45262b6/MPL_57_133-179/documentation/reconcile_inventory.py
```

After reviewing the candidate, explicitly regenerate and apply only its editorial-row reconciliation:

```bash
python /workspace/scratch/641dc45262b6/MPL_57_133-179/documentation/reconcile_inventory.py --apply
```

The apply operation checks that neither input inventory nor page bytes changed during the run, saves a timestamped inventory backup under documentation, and atomically replaces the inventory. It never applies display proposals.

## Outputs

- `inventory_reconciled_candidate.csv`: each separate deleted, inserted, and margin macro has its own row, including nested occurrences. New identifiers use `SCAN.edNNN`.
- `inventory_reconciliation_report.json`: source hashes, exact occurrence character offsets/lines, nesting, original-row matches and scores, unchanged-row anchors, and display review proposals.
- `inventory_display_proposals.csv`: proposed display splits or diagram/display kind corrections requiring review.

All non-editorial rows retain every field and their original relative order within each scan. Editorial rows use exact TeX line positions; a broad original position is inherited only when textual matching supports it. Relative interleaving with preserved rows uses textual anchors/interpolation and is bookkeeping, not verification against the image.

## Prepared candidate

The prepared candidate has 663 rows: 259 editorial occurrence rows (including 17 nested occurrences) and 404 unchanged non-editorial rows. It replaces 210 broad editorial rows, adding 49 rows overall. The original inventory was verified unchanged. Regenerate after further audit edits.

Two display review items were identified in the prepared snapshot:

- Scan 147, row `147.08`: recorded as diagram although its quotient expression remains inside an explicit display environment. Review changing this row back to display.
- Scan 147, row `147.23`: groups the two explicit displays currently starting at TeX lines 42 and 45. Split into separate display rows after review.

The parser was checked against nested macros, comments containing apparent macros, and escaped literal braces. Candidate counts agree with every parsed occurrence, all generated identifiers are unique, and preservation of all non-editorial fields/order was verified.
