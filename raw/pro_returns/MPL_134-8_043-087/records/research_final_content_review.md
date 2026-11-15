# Final content review: concrete issues

1. **`research_summary.md`, H4: a named resolution argument is described as an explicit resolution.** Scan075:52–53 writes “argument de résolution d’objets de `N^{\unsure{\flat|b}}` par des `\inserted{sommes d'}` objets de `N`”; it does not display the resolution itself there. Replace “including an explicit resolution by sums of objects of `N`” with “explicitly naming a resolution argument for objects of `N^{\unsure{\flat|b}}` by sums of objects of `N`”.

2. **`research_dossier_coverage.json`, BISITE E.3, `relation_note`: preserve the exact presentation criterion.** “Coherent compact-generator presentation” compresses the source row’s specified condition that each `Map(h_S(c),−)` preserve **all small colimits**, with the functors jointly detecting equivalences and `h_S` fully faithful (`DOSSIER_STATEMENTS_WITH_STATUS.md`:183). Replace that phrase with “a coherent presentation by the fully faithful `h_S`, whose mapping-space functors preserve all small colimits and jointly detect equivalences”; the existing bounded absence statement can then remain.

3. **Adjacent findings paragraph in `research_summary.md`: the statement that both witnesses “write” the same binomial equation silently renames a variable.** Scan074:117 writes `P(a+b)=P(a)+P(b)+ab`, while `ps6.tex`:2943 writes `P(a+a')=P(a)+P(a')+aa'`. Quote both forms, or say explicitly that PS uses `a'` where the handwriting uses `b`, before describing their correspondence.

## Applied corrections

- Items 1 and 3 were applied to `research_summary.md` during final integration; neither changes the frozen transcription.

- Item 2 was applied to `research_dossier_coverage.json` (BISITE E.3 `relation_note`) and `research_dossier_map_draft.md`: the fully faithful `h_S`, the mapping-space functors `\Map(h_S(c),-)`, preservation of **all small colimits**, and joint detection of equivalences are now explicit, with the bounded absence claim retained. All 255 source rows/status claims/current quotations and all 45 frozen-source hashes remain unchanged. The persisted integration generator reads these corrected records and contains no stale wording; no generator edit or unrelated draft regeneration was needed.

  Corrected input SHA-256 values:

  - `research_dossier_coverage.json`: `62d478341bb9fba0775095708c81b0f4ad80a90b9d0d64da668c169d83917608`
  - `research_dossier_map_draft.md`: `3fae0bfd98e73121371786fdcf1da3baf7624f7a74aa8f4562e9557f32c52d5a`
