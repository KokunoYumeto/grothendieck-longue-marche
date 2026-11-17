# Mechanical LaTeX findings before the visual audits finish

**Update, 2026-11-17 13:18:53 UTC:** Root authorized the exact technical fixes below; they were applied to scans 037, 056, 065, and 067 at 13:18:36 UTC. The corrected syntax checker subsequently compiled all 44 current page files successfully. Before/after hashes and operations are recorded in `technical_fixes_applied.json`; the current outcomes are in `latex_syntax_report.json`. The findings below document the earlier diagnosis.

This report concerns LaTeX syntax only. It does not certify manuscript readings, completeness, or visual fidelity. During the initial diagnosis no source-page files were changed; the subsequent edits were limited to the four expressly authorized technical repairs described below.

## Inventory and file coverage

- All 44 expected, nonempty page files exist; no extra `.tex` page files were found.
- The inventory has the required eight columns in the required order.
- Its 760 rows cover all 44 expected scans, use permitted sheet/element kinds, contain no duplicate cote/scan/element identifiers, and have `transcribed=yes` throughout.
- Coverage is a schema check only; it does not establish that every manuscript element has been inventoried.

## Harness correction

The first wrapper used a recursive input search that could resolve the shared basename `fragment.tex` to a sibling page. That invalidated the earlier reported 29-page success and the first attempted 44-page run. The corrected helper uses explicit absolute snapshot and wrapper filenames, prioritizes the current directory, and does not recursively search sibling snapshots for input files. The corrected run checked 44 distinct fragments and passed 38 before resolving two wrapper dependencies.

The neutral editorial wrappers no longer pre-tokenize their arguments. This permits the TikZ matrix environment to set ampersand catcodes before its cells are read.

## Wrapper dependency

Scans 058 and 060 use ellipse nodes. The temporary wrapper now includes `shapes.geometric` in `\usetikzlibrary`. Both fragments pass unchanged with this dependency added. The complete library list is:

```latex
\usetikzlibrary{arrows.meta,decorations.pathmorphing,patterns,calc,shapes.geometric}
```

## Proposed minimal page-code fixes

The line numbers below refer to the snapshots checked at 2026-11-17 13:16:01 UTC. All proposed fixes were tested successfully on temporary copies outside the deliverable tree before root authorized their application.

| Scan | Lines | Technical cause | Minimal code-only change |
|---|---|---|---|
| 037 | 21–33; error surfaces at 34 | A `tikzcd` occurs inside the argument of `\fbox`. Ordinary `&` tokens are captured before TikZ can change their catcode. | Add `ampersand replacement=\&` to this diagram's options and change its three cell separators from `&` to `\&`. |
| 056 | 48 | A diagram cell is already in math mode; the textual doubt contains `$m$` without a text-mode wrapper. | Replace `\quad\deleted{\unsure{pour tout $m$}}` with `\quad\deleted{\text{\unsure{pour tout $m$}}}`. |
| 065 | 16–17 | An arrow targets a trailing empty cell for which TikZ creates no node. | Change the terminal `&` on line 16 to `&{}`. |
| 065 | 29, 66, 68 | A literal `[` immediately after `\\` is parsed as an optional vertical-spacing argument instead of printed content. | At these three places, change `\\[\text` to `\\{}[\text`. The added empty group prints nothing. |
| 067 | 11–12 | An arrow targets a trailing empty cell for which TikZ creates no node. | Change the terminal `&` on line 11 to `&{}`. |

All six initially failing fragments passed with the wrapper dependency resolved and the proposed changes applied to temporary copies. The other 38 fragments passed the corrected per-page check. After the authorized fixes were applied to the actual page files, all 44 passed at 13:18:53 UTC. Later editorial changes made during the visual audit may warrant another syntax check.
