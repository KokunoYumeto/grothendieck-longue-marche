# Mechanical syntax review through scan 133

Snapshot: 2026-11-17 22:51:11 UTC

## Scope and current gate

All 43 expected page fragments are present. The partial validator currently
reports 0 errors and 0 warnings.
It sees 33 audit records at this snapshot; the primary
reader's second visual audit is still in progress. Missing freeze and final
research deliverables remain informational in partial mode. This is not a final
completion or manuscript-accuracy certification.

The support agent read no scan images or research-context sources, performed no
mathematical checks, and edited no transcription files. Only the separately
requested inventory normalization and apparatus-locator additions were made.

## New syntax review: scans 124–133

The new fragments have balanced braces and environments. Examination of 240
TikZ draw/fill/node/coordinate commands found no missing terminating semicolon,
unbalanced coordinate parentheses, or unbalanced option brackets. Dollar and
display delimiter counts agree, and no unexpected ASCII control bytes were found.
The tikz-cd diagram on scan 129 has a consistent three-column row structure and
three syntactically formed arrow declarations. No visual direction or label
reading was checked.

The additional `pmatrix`, `underset`, `overset`, and fraction commands are already
covered by the harness's AMS declarations. The text environments and `tabular`
use standard LaTeX commands. No extra apparatus definitions or packages are
required by the new fragments. The harness input list now contains all 43 pages.
The two additional tikzpicture environments on scan 126 are inside existing
figure arguments, so the difference between its figure and picture counts is
explained by grouped drawings.

Full compilation remains unavailable because the TeX format and package/class
tree are absent; no new compile was attempted and no dependencies were installed.
Static checks cannot validate macro expansion, TikZ rendering, drawing fidelity,
or physical page layout.

## Inventory apparatus expansion

At the primary agent's instruction, 34 exact macro-body locator rows were added
only where a page/kind combination previously had zero corresponding rows.
The inventory increased from 911 to 945 rows. Every preexisting element ID and
field was retained, except the explicitly authorized replacement of cancel with
deleted in element 127.10's caption. The new rows continue the existing numeric
IDs, identify themselves as apparatus locator expansions, and record TeX line,
macro ordinal, and exact macro body. The event record is
`apparatus_locator_expansion.json`.

The latest report checks all 34 locator rows against current TeX and finds
0 locator changes. It finds no remaining caption
containing the obsolete cancel command. These statements refer to the recorded
snapshot; later visual-audit edits can change the locators.

## Remaining inventory review signals

The full per-page comparison is in `apparatus_inventory_counts.tsv` and
`apparatus_inventory_review.md`. There are currently
21 page/kind combinations with more macro
occurrences than corresponding inventory rows. These are review signals, not
proved omissions, because existing rows may describe groups or cancelled figures
under another category. No nonzero-category matching was guessed and no rows
were added for those combinations.

After the visual audit, refresh the reports with:

```sh
python records/review_apparatus_inventory.py
python records/validate_package.py --partial
```

The reconciliation script only reads TeX and inventory and writes reports. It
never edits the inventory or transcription. It identifies exact-body or line
changes in the added apparatus locators and can support the primary reader's
final reconciliation before freezing.
