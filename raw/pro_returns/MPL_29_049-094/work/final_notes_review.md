# Final assembled-notes review — Picard research agent

Review time: 2026-11-18 04:27:40 UTC

## Scope

Read the assembled `MPL_29_049-094_notes.md` (77 note items) and `CHECK_EVENTS.tsv` (96 events), compared the research records and relevant full-context headings/passages, and reopened selected primary sources to verify source locators and hypothesis scope. The standing-sections placeholder was excluded as instructed. No scan image was inspected and no frozen transcription or assembled deliverable was edited.

## Two minor integration fixes — resolved

1. **CHECK_EVENTS: `scan076:rank-equality-with-unrestricted-ell`.** The outcome starts with E/F3 and then says “pro-3 rank zero” without specifying the geometric group. Replace that clause with “after base change to the algebraic closure of F3, the geometric fundamental group has pro-3 rank zero.” P12 in the notes already has the correct geometric qualification; this change makes the event accurate when read independently.
2. **N-RQ-03, final sentence.** Replace “the formal notes below” with “the preceding formal notes” or “FORMAL-01–FORMAL-17”: those notes precede N-RQ-03 after integration.

The root subsequently confirmed that both fixes were applied in the generator/source and the main files regenerated. The root also reviewed the newly integrated standing sections; those sections remain outside this agent's review scope.

## Scoped approval

All bracketed BR-S, P-S and F-S source keys have link definitions. All named refinement IDs in the event log resolve to existing assembled notes, including the former P17 reference now correctly pointing to FORMAL-17. No note body exceeds four sentences: question marks inside quotations and the abbreviation “n.r.” caused false positives in the punctuation check and were manually excluded. The context sections and page mapping checked against `29.modern.tex` exist; no invented context match was found. The abstract-versus-geometric scope qualifications for P04, P05, P11, BR12 and BR15 are preserved, and FORMAL-10–FORMAL-17 distinguish root existence, uniqueness, formal effectivity and the external-source discrepancy.

The reviewed mathematical material is approved within its stated proof/background scopes with the two minor fixes above reported applied by the root. This is an integration review, not a new full audit of every external theorem, the image transcription, or the still-drafted standing sections.

## Primary-source spot checks

The Stacks locators 0AY6, 0BX7, 0BX5, 0BN6, 0BQJ, 0B87, 0BSE, 0G4C, 03SI, 02G3, 0GJ2, 0C6Q and 0C6S were reopened and their attached descriptions were consistent with the notes. Primary abstracts/theorem statements for arXiv:1509.08160, 2303.11161 and 2102.13424v2 support the stated categorical and finite-presentation claims. Conrad, *Picard functors for curves*, Proposition 3.1 explicitly explains the extension of its tangent-space proof beyond its displayed projective hypotheses; Kleiman, *The Picard scheme*, Theorem 5.11 and Corollary 5.13 provide the general representable-Picard statement as an additional exact locus if desired.
