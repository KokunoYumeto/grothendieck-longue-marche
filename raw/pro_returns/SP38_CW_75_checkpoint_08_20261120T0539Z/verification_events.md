# Verification events

- 2026-11-20 00:56:54 UTC: the initial structural checker reported display-delimiter imbalances on scans 003–005. Inspection of the text showed these were false positives from LaTeX row breaks followed by optional spacing, not transcription defects.
- 2026-11-20 00:57:16 UTC: `scripts/verify.py` now tokenizes control sequences before counting display delimiters. Rechecking the same five committed pages passed, including combined-file concatenation and inventory completeness. No page file was changed in this correction. No TeX compilation was performed.

- 2026-11-20 01:36:34 UTC: structural verification of the seven committed pages through scan008 passed (212 inventory elements, 98 unsure marks, 0 illegible, 52 deletions). This check specifically covers the newly changed adjacent brackets, composite marginal TikZ and left-tag group. No compilation; final freeze remains pending all 24 pages.

- 2026-11-20: final schema gate prepared for all 24 pages. Normalized only the collation category spelling readable ink left as \ill{} (removed literal Markdown/backslash escaping variants) in scan005.json. Raw reader reports and transcription files unchanged; counts unchanged. Future commits normalize the same known category.

- 2026-11-20 02:04:15 UTC: structural verification through scan009 (eight pages) passed; 248 inventory elements, 118 uncertainty marks, no illegible markers, 57 deletion spans. No TeX compilation. This is transcription/schema verification, not a mathematical proof event.

2026-11-20 02:42:08 UTC: scan010 structural verification passed. A preliminary naive display-delimiter assertion had counted the row-spacing token as an opening display; the corrected expression excluded doubled backslashes and passed. No transcription change resulted.
