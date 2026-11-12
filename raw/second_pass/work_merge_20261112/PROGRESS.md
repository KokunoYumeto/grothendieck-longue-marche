# Merge of the 33 open fixes (second_pass/merge_fixes_open.md), 12 Nov 2026

- Started 10:47 UTC. Dated copy of the list: merge_fixes_open_20261112_before.md.
- open_dump.md: each fix's snippet, Pro's replacement and note, and what its scan page holds now (dump_open.py).
- check_in.py: 16 fixes are already in the current files verbatim (15 written by fuzzy_merge.py --go on 8 Nov after
  the list was made; 10-009 keeps the \illegible mark, so the text is already Pro's): 01-021, 01-022, 01-025, 01-026,
  01-030, 01-031, 02-007, 09-023, 02-010, 10-002, 02-013, 02-019, 10-009, 02-022, 03-002, 03-013.
- To decide against the scans: 01-013, 01-014, 09-008, 09-009, 02-003, 09-013, 09-021, 09-022, 02-012, 09-025,
  09-026, 10-007, 10-011, 10-013, 10-015, 10-017, 10-024.
- Tools: img.py (crops into img/); compile with answers/fixed/build/wrap.tex.

## Decisions so far
- 01-013 apply (one tikzcd row: I=S_0 ⊂ S(K̄) over ≀≃ S_0(K̄)∧_ΣΓ, so S(K̄) is not doubled, per Pro's note).
- 01-014 already in (the second pass reads «sinon pas de pb»); Pro's wider \inserted scope not taken (cas ν=1 is on the line).
- 09-008 reject (cancelled mark under hatching; left point, right loop, no ↔ head visible).
- 09-009 apply, letter read E (Pro: e).  02-003 reject (mark has no upward head; thickens at lower end).
- 09-013 apply with \unsure{\geq|2} (crossed glyph looks like a 2).  09-021 apply, plus U_{g,ν} -> U_{0,1} (ink, Pro's note).
- 09-022 apply.  02-012 apply.  09-025 apply.  09-026 apply.  10-007 already in (s_ν|g,ν alternatives kept).
- 10-011 apply.  10-013 reject (♮ visible after π; second pass's (π_0^♮) stays).  10-015 apply.
- 10-017 apply the hats; \mathcal T kept certain (clear on the scan).  10-024 apply.
- 02-010 already in but the (65) display above it is now doubled: remove the old display (Pro's scope note).

## Done (12 Nov, 11:05 UTC)
- Final: applied 12, rejected 3 (09-008, 02-003, 10-013), already in 18. 09-013 applied as Pro gives it (\unsure{\geq}2).
- Outcomes written on each line of second_pass/merge_fixes_open.md (record_outcomes.py; dated copy here).
- Edits: apply_merge.py; dated copies here as LM_PXXX_checked_fixed_before_20261112.tex.
- Changed and compiling in answers/fixed/build/wrap.tex (compile_changed.py, build/): P011 P013 P017 P019 P022 P024
  P025 P026 P032 P033 P034 P035. P013 failed before the merge too (raw & in seven tikz-cd diagrams inside \diagram);
  repaired with fix_tikzcd_in_macros.py (LaTeX only, content unchanged).
