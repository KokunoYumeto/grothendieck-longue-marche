# Mechanical source inventory and parsing anomalies

These observations concern the supplied files and their syntax. They are not readings of the manuscript and do not count as ink checks.

The balanced-macro inventory finds 2,684 listed uncertainty macros on 142 pages. Source files use CRLF line endings. `scripts/reconcile.py` reads their bytes without newline translation and substitutes only the complete balanced spans of listed marks. Text outside those spans, including line endings, remains byte-for-byte identical.

## Escaped braces and normalized whitespace

| Mark | Scan | MARKS.tsv representation | Actual source macro / difference |
| --- | --- | --- | --- |
| M1340 | 067 | `\unsure{\}` | `\unsure{\}}`; the first closing brace is escaped and belongs to the candidate. |
| M2152 | 102 | `\unsure{\}` | `\unsure{\}\|§\|?}` with unescaped pipes in the source; candidates are the literal closing brace `\}`, `§`, and `?`. The pipes are escaped only in this table for Markdown. |
| M2285 | 117 | `\unsure{\}` | `\unsure{\}}`; the first closing brace is escaped and belongs to the candidate. |
| M2534 | 136 | One line with a space after `\leq` | The actual macro has a CRLF at that location. Candidate equality permits this whitespace normalization, while the replacement boundary follows the full source macro. |

The original IDs remain authoritative. Each anomalous ID is mapped to the corresponding full balanced source span, without inventing additional IDs.

## Nested listed marks

| Outer mark | Inner mark | Scan | Consequence |
| --- | --- | --- | --- |
| M0771 | M0772 | 038 | `\unsure{\illegible{1}}` contains a separately listed illegible mark. |
| M0779 | M0780 | 038 | The same nested form occurs again. |
| M2170 | M2171 | 103 | An outer wording choice contains an inner `\unsure{\rho\|f}` choice in its first candidate. |

Every outer and inner ID requires its own decision and ink observation. The outer replacement controls the final text; a child replacement must never overwrite it at stale source offsets. For first/alternative choices the script applies child decisions when comparing the chosen candidate. An outer output that explicitly retains the original inner macro is reconciled with the child row. A removed inner span still has its own decision and check event in the audit tables.

## Literal pipes versus choice separators

Source text uses unescaped `|` both for alternatives and for absolute-value notation. For example `\unsure{|K|}` (M0272) and `\unsure{1+|A|}` (M0544) have literal mathematical bars. There are also genuine choices with more than two candidates, such as M1093.

The mechanical validator splits unescaped pipes only at brace depth zero, and accepts the exact whole body as a first reading when its pipes are literal notation. Where literal bars and alternatives are mixed, readers may supply an explicit `candidates` string list in the row; the full submission and this override are retained in the audit JSON. This is a syntactic reconciliation aid, not evidence for any reading. The ink observation remains required for every row.

## Pixel coordinates

Crop bounds are checked against each image's actual encoded dimensions, not the generic dimensions quoted in the prompt. Coordinates use original source-image pixels and the order `x0,y0,x1,y1`, with right and bottom excluded. No rescaled-display coordinates are substituted.

For the two outer `\unsure{\illegible{1}}` records, a recovered actual symbol is classified `other`, since the supplied body contains no proposed reading. If unreadable, both levels remain `undecided`. Removing the outer wrapper does not itself constitute settling its ink.

## Supplied PREAMBLE.tex contents

Mechanical text comparison found that supplied `PREAMBLE.tex` equals `pages/1_scan003.tex` after newline normalization. It contains page003 transcription text and no `\newcommand` or `\def` definitions, rather than the macro preamble described in the prompt. The source is left untouched. This does not prevent the requested mark-only page reconciliation, and compilation is not claimed.
