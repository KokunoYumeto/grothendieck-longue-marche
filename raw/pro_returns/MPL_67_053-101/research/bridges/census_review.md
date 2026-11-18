# Brief census audit

**UTC:** 2026-11-18T01:38:43Z  
**Reviewer:** GPT-6 Astra Pro; effort not exposed; `MPL_67_053-101/context_bridges` census-review subtask.

Read `research/censuses.md` and all 45 JSON records in `research/census_data.json`, then searched the frozen text for self-flags, question marks, headings, dates and page-number macros; read the relevant passages in full and compared the Hua page concordance. No images were inspected, and neither census file nor any frozen transcription was edited.

## Corrections

### CR01 — F05 attributes the doubt to the wrong textual state

**Required correction:** Change “67/060, replacement Lemme3(a)” to **“67/060, cancelled first Lemme3(a)”** and identify the item as **self-flagged in the cancelled draft**. In `pages/MPL_67_053-101_67_scan060.tex`, “ou plus régulier que ça ?” is inside the large `\deleted{...}` block beginning with the first Lemme3; the later live “Lemme3 Cas particuliers” starts after that block closes and does not contain this parenthesis. The present status sentence reverses the relationship by treating the quoted doubt as if it belonged to the replacement while mentioning the first formulation separately. The quote itself and Hua location §VII(3–4), p.59 = scan60 are correct; preserve the live replacement’s own hypotheses without carrying the cancelled question into them. The same clarification would help S11’s first sentence: explicitly call the quoted parenthesis a doubt in the cancelled formulation, while keeping its distinct claim that the replacement is a reformulation rather than a completed proof.

### CR02 — T02 omits the first numbered topic of the surgery sequence

**Suggested completion:** Add to T02, or insert a separate entry, **“Surface conforme à bord”** on frozen scan54, after “Chirurgie conforme.” Its circled label is retained as `\unsure{1|A}` followed by a closing parenthesis, so do not silently normalize it to an unequivocal 1. This is the first topical heading corresponding to Hua §VII(1), p.53 = scan54; the census already separately records topics2–6 on scans56,58,61,70,74. It is a heading completion, not another title sheet, date, or page count.

## No further correction indicated by this text-only check

The 47-file count, absent scans83 and90, and all fifteen live author numbers check exactly: scan54→1, 56→2, …, 82→15. The cancelled doubtful3 on60 and doubtful4 on61, the date ambiguity on54, dates12.1/13.1/9.2, December83, and the distinction between printed job dates and handwriting are represented correctly. All JSON IDs F01–F33/T01–T12 occur in the Markdown census, and the cited Hua page-to-scan offsets agree with p→p+1. No additional significant unresolved self-flag was found in the search; the “Il reste… à trouver” sentence on93 is immediately followed by its invariant quadratic-form parametrization, so it should not be promoted to another unresolved problem.
