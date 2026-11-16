# Mechanical prefreeze report

## Scope

These checks were performed after the primary transcriber reported completion
of all 34 visual audits, while notation reconciliation was still in progress
and before freezing. No scans, crops, or context documents were read. No
transcription, inventory, combined fragment, or existing record was modified.
No freeze or SHA-256 manifest was created by this check.

## Concrete findings requiring metadata reconciliation

The following observations compare existing doubt metadata with the current
LaTeX strings only. They do not propose or adjudicate manuscript readings.

1. **Scan 017, manual doubt `bottom ne s'exprime plus`:** the reading field still
   contains `avec|uniqu.`, whereas the current transcription contains
   `\unsure{nec.|avec}`. A later manual entry, `last paragraph`, already records
   `nec.|avec`. The old entry should be updated, retired, or explicitly labelled
   as a superseded reading so that it does not contradict the current record.

2. **Scan 017, manual doubt `middle multiplicity notation`:** the reading field
   gives `e_1, e_-1`, with Greek epsilon described as the alternative. The current
   transcription consistently places `\varepsilon_1` and
   `\varepsilon_{-1}` first, with Latin `e` as the alternative. The metadata
   preference/order should match the audited transcription or explicitly state
   that it records the earlier preference.

3. **Scan 021, manual doubt `NB boundary L-expression`:** its reading field is
   `R j_*(E)|R_infty j_*(E)`, but the current source reads
   `\unsure{\mathbf R_\infty j_*(E)|\mathbf R j_*(E)}`. The same alternatives
   are retained in the opposite order. Reconcile the manual row's preferred
   reading with the source's first alternative.

4. **Scan 029, manual doubt `middle cancelled formula`:** the older row presents
   `L_E^∞(p^{n+ρ}t)` in its reading column. In the current source this is the
   second alternative; the first is the reciprocal-argument expression with
   exponent `-1`. The newer manual row `cancelled boundary factor, left of
   middle display` records the reciprocal reading. The older row should be
   labelled as an alternative/superseded preference or consolidated with the
   newer row.

5. **Scan 035, duplicate manual doubt entries:** `after ε definition` and
   `unfinished phrase at right of epsilon definition` both record
   `ceci avec les` at the same location. The latter updates the former's
   uncertainty status. These can be consolidated; the transcription itself
   contains one corresponding uncertainty token.

These are metadata-consistency findings. They require no change to the
transcription on mechanical grounds. Their resolution, if any, should be
recorded separately; this report describes the snapshot checked.

## Checks with no defect found

- All 34 page record `text` strings matched the corresponding page files
  byte-for-byte when UTF-8 encoded.
- The combined fragment matched the literal concatenation of the 34 ordered
  page files.
- No unexpected ASCII/C1 control characters were found in page text or in
  string fields of the page records. In particular, no tab remained in the
  scan 035 text.
- TeX grouping braces, environment nesting, inline dollar counts, display
  delimiters, and `\left`/`\right` counts passed the checks.
- All `tikzcd` environments had no remaining bare ampersand cell separators.
  Where escaped `\&` separators appeared, `ampersand replacement=\&` was
  present, including the affected environments on scans 013, 025, 026, and 035.
- All 545 inventory rows were valid, had `transcribed=yes`, and exactly matched
  the inventory projection of the page records.
- All 144 automatically generated uncertainty rows and all 85 manual doubt
  rows were present in the doubts file with their current record values.
  Thus the consistency issues above originate in manual record content, not
  in an out-of-date generated doubts file.

## Expected prefreeze state

The full structural validator's only error was the absent research-notes file,
`MPL_60_002-035_notes.md`. It warned that the frozen-hash manifest did not yet
exist. Both omissions are expected at this stage. No successful TeX document
compilation is claimed; the earlier compiler/package availability caveat in
`mechanical_preflight.md` remains applicable.

Root reconciliation: the five stale/duplicate manual doubt cases listed above were reconciled before freeze; no page text was changed by that metadata cleanup.
