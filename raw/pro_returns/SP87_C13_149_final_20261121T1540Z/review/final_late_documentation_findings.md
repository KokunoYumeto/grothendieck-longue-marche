# Final late-page documentation consistency findings

## Scope and result

Reviewed canonical metadata for **096–098, 100 and 102** against the current final page text and completed explicit blind adjudications. The inspected fields were notes, hand_observations, notation_additions, abbreviations, unresolved and inventory; check_events was read only to assess attribution and the stated scope of already recorded checks.

**Five substantive issue groups require metadata correction:** the clipped ending on096; the formula-prefix description on096; the obsolete empty-check-list statement on097; the newly uncertain cancelled ext|est on098; and the old certain meme notation entry on100. Exact guarded proposals appear below. The final TeX pages and adjudications already contain the updated readings.

Scan102 has no stale reading or mathematical-scope claim in the inspected fields. Reader C independently reviewed that leaf with the same result. Its “main authorial hand” labels are stylistic variants of an existing attribution; changing them is not needed for this consistency review. No new attribution is inferred for any foliation hand.

No images were opened, no mathematical checks were performed, and no canonical record, page, frozen TSV, adjudication or global document was edited. **This findings file is the only file written by this review.**

## Evidence map

| Leaf | Finding | Final authority |
|---|---|---|
| 096 | The old note and hand evidence claim the entire prefix distingu is verifiable, but the final low return remains u versus the exit of g. | Final \unsure{distingu\|disting}; B006. |
| 096 | The old prefix note and formula inventory omit preferred (f_K)_*; the note also omits the final g_i preference. | Final formula and B016; section label B004. |
| 097 | “The check_events list is therefore empty” is a current false statement. | The same canonical record contains the main reader’s 149097-section-conjugation-action event and matching notes. |
| 098 | Several descriptions and the abbreviation table still give cancelled ext without its final est alternative. | Final cancelled ext\|est with external stop; B028/B030 and unresolved 098-ext-est. |
| 100 | The notation table gives certain meme, although notes, hand observations, unresolved and the page prefer encore with meme retained. | Final encore\|meme; B001. |
| 102 | No stale reading found. | Final page and B005/B009/B010/B011/B017, including rat\|rt, 1\|n, si, the cancelled NB alternatives and ie. |

## How to apply the guards

The proposals below are **data, not an executed cleanup script**. All paths are relative to SP87_C13_149_work.

For replace_substring, select the named record field, require the exact old substring to occur once, and replace only that occurrence. For replace_fields, require a unique array object matching the selector, then require every listed old field value to equal its guard before replacing those fields together. In particular, replace the098 abbreviation’s form and expansion together, and replace all three100 notation fields together. Do not use fuzzy replacement or silently skip a failed guard.

Every guard was checked successfully against the saved records during this review. The source hashes at the end identify the reviewed snapshot. If a file has subsequently changed, recheck the relevant final page/adjudication and the exact field guards; do not apply the proposal merely because an old word still occurs somewhere.

## Required guarded metadata changes

These corrections preserve final decisions and existing uncertainty. They neither alter diplomatic text nor turn a previous visual or mathematical observation into a new check.

```json
[
  {
    "id": "R096-clip-notes",
    "file": "review/149_scan096_reviewed.json",
    "op": "replace_substring",
    "selector": {
      "top_level": true
    },
    "field": "notes",
    "expected_occurrences": 1,
    "old": "The first paragraph’s word at the right edge is transcribed only through the visible prefix distingu; neither the expected é nor H’s extra e is completed, and no illegibility marker is added for missing paper.",
    "new": "The first paragraph’s word at the right edge is transcribed as \\unsure{distingu|disting}: the final low return may begin u or belong to g. Neither an unseen é nor an additional e is supplied, and no illegibility marker is added for missing paper.",
    "authority": "Final page line containing the clipped word; blind adjudication B006."
  },
  {
    "id": "R096-clip-hand",
    "file": "review/149_scan096_reviewed.json",
    "op": "replace_fields",
    "selector": {
      "array": "hand_observations",
      "match": {
        "habit": "A source word meeting the page edge cannot be completed from grammatical agreement."
      }
    },
    "old": {
      "evidence": "Only distingu remains verifiable before the paper edge."
    },
    "new": {
      "evidence": "The visible prefix is retained as distingu|disting: the last low return may begin u or be the exit of g. No ending beyond the paper edge is supplied."
    },
    "authority": "Blind adjudication B006 retains the u itself as uncertain."
  },
  {
    "id": "R096-prefix-notes",
    "file": "review/149_scan096_reviewed.json",
    "op": "replace_substring",
    "selector": {
      "top_level": true
    },
    "field": "notes",
    "expected_occurrences": 1,
    "old": "The leading E f_K/f_K in (29), the small mark next to g, and tt/tte remain doubtful.",
    "new": "The prefix in (29) now favors (f_K)_* while retaining E f_K|f_K; the section label favors g_i while retaining g; tt|tte remains doubtful.",
    "authority": "Final page and blind adjudications B004/B016."
  },
  {
    "id": "R096-prefix-inventory",
    "file": "review/149_scan096_reviewed.json",
    "op": "replace_fields",
    "selector": {
      "array": "inventory",
      "match": {
        "element": "numbered_formula29"
      }
    },
    "old": {
      "first_words_or_objects": "(29) E f_K|f_K = ψ : E_K → E_{U_K}"
    },
    "new": {
      "first_words_or_objects": "(29) \\unsure{(f_K)_*|\\mathcal E f_K|f_K}=\\psi:\\mathcal E_K\\longrightarrow\\mathcal E_{U_K}"
    },
    "authority": "Blind B016 and the exact formula in the final page include the newly preferred prefix."
  },
  {
    "id": "R097-check-scope",
    "file": "review/149_scan097_reviewed.json",
    "op": "replace_substring",
    "selector": {
      "top_level": true
    },
    "field": "notes",
    "expected_occurrences": 1,
    "old": "Actual mathematical checks: This first reader performed no independent proof, computation, mathematical use or refutation. The check_events list is therefore empty; the reviews above are visual collation checks only.",
    "new": "Actual mathematical checks: The first reader performed no independent proof, computation, mathematical use or refutation; its first-pass check_events list was empty. The current record also contains the main reader’s separately attributed conditional section-conjugation-action check below. The preceding collation observations are visual checks, not additional mathematical proof events.",
    "authority": "Current check_events contains 149097-section-conjugation-action, attributed to the main reader; the following notes paragraph records the same conditional check."
  },
  {
    "id": "R098-cancelled-word-notes",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_substring",
    "selector": {
      "top_level": true
    },
    "field": "notes",
    "expected_occurrences": 1,
    "old": "The lower ext has crossed letters but a separate uncrossed stop beyond the strike, hence deleted ext followed by a live stop and the raised effective.",
    "new": "The lower cancelled word is retained as \\deleted{\\unsure{ext|est}}. The distinct following stop remains outside the strike, followed by the raised effective; ext is preferred but is not certain.",
    "authority": "Final page and blind adjudication B028/B030."
  },
  {
    "id": "R098-cancelled-word-main-review",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_substring",
    "selector": {
      "top_level": true
    },
    "field": "notes",
    "expected_occurrences": 1,
    "old": "The l’extension leader stays above the live word; the ext stop is visibly beyond the strike and is retained live.",
    "new": "The l’extension leader stays above the live word; the stop after the cancelled ext|est is visibly beyond the strike and remains live.",
    "authority": "Blind B028/B030 preserves ext|est and a separate uncancelled full stop."
  },
  {
    "id": "R098-cancelled-word-hand",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_fields",
    "selector": {
      "array": "hand_observations",
      "match": {
        "habit": "The stop of an abbreviation can survive outside the actual strike."
      }
    },
    "old": {
      "evidence": "A distinct round stop stands beyond the cancellation endpoint of ext, before the effective leader."
    },
    "new": {
      "evidence": "A distinct round stop stands beyond the cancellation endpoint of the doubtful ext|est, before the effective leader."
    },
    "authority": "Blind B028: middle x/s is unresolved; only the stop is securely outside the strike."
  },
  {
    "id": "R098-cancelled-word-abbreviation",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_fields",
    "selector": {
      "array": "abbreviations",
      "match": {
        "form": "ext."
      }
    },
    "old": {
      "form": "ext.",
      "expansion": "extérieure; letters cancelled, terminal stop uncrossed"
    },
    "new": {
      "form": "\\deleted{\\unsure{ext|est}}.",
      "expansion": "extérieure if the preferred ext reading is correct; est remains possible. Only the letters are cancelled; the terminal stop is live."
    },
    "authority": "Final page, unresolved entry 098-ext-est and blind B028/B030."
  },
  {
    "id": "R098-cancelled-word-inventory",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_fields",
    "selector": {
      "array": "inventory",
      "match": {
        "element": "effective-replacement"
      }
    },
    "old": {
      "position": "above ext, leader before sur"
    },
    "new": {
      "position": "above cancelled ext|est, leader before sur"
    },
    "authority": "The final cancelled form is ext|est; this does not rename the stable inventory element."
  },
  {
    "id": "R100-opening-notation",
    "file": "review/149_scan100_reviewed.json",
    "op": "replace_fields",
    "selector": {
      "array": "notation_additions",
      "match": {
        "written": "meme without an independent accent"
      }
    },
    "old": {
      "written": "meme without an independent accent",
      "transcription": "meme",
      "evidence": "149_scan100_meme crop: the area above the word is blank; retain the written absence of the circumflex. No general spelling replacement is inferred."
    },
    "new": {
      "written": "Three low joined groups without an independent circumflex; encore preferred, meme retained",
      "transcription": "\\unsure{encore|meme}",
      "evidence": "Blind B001 favors encore from an open e/n entry, c-like middle with a small oval, and final r/e return. The flattened joins also permit unaccented meme; absence of a circumflex does not make meme certain."
    },
    "authority": "Final page, unresolved opening_word, updated hand observation and blind adjudication B001."
  }
]
```

## Mathematical-note scope

This section assesses the wording and attribution of recorded material; it is not a re-proof.

| Leaf | Current distinction | Finding |
|---|---|---|
| 096 | Rational-point functoriality and composition of sections are recorded as conditional formal checks; section classification and existence claims remain background. Reader A and main-reader review are attributed. | Scope is clear. The optional “initial E” to “initial prefix” edit below updates a label without changing the check. |
| 097 | The source’s effectives does not certify faithfulness. The main reader’s conditional conjugation-action calculation is distinct from geometric existence. | Correct the obsolete empty-list sentence, keeping the first reader’s historical no-check statement and the root event both intact. |
| 098 | Specialization, first-kind sections, conjugacy classes and effective-operation statements are described as authorial claims; check_events is empty. | Consistent. No verification should be added. |
| 100 | The recorded proof concerns abstract outer-action descent and a choice of splitting. Geometric nontriviality, the good-reduction conjecture and the marginal VA/H1 claim remain unproved background; topology is expressly not separately checked. | Consistent. The later hook/callout is not used to rewrite the mathematical assertion. |
| 102 | Only the conditional innerness-to-trivial-abelianization implication is recorded as checked and rechecked. No converse, geometric criterion or separate H1 identification is asserted as proved. The p-case and “loufoque” condition retain the author’s qualifications. | Consistent. The statement that b) was outside the first reader’s packet is historical and does not assert that the final edition omits b). |

## Advisory precision changes

The following items do not reverse a decision. They prevent abbreviated inventory or prose descriptions from appearing more certain than the final text, or align a quoted word’s accent with its final spelling.

- On098, “target K” should clearly mean the **K subscript** of the inclusion/hooked-arrow targets. The separate earlier **main body** remains E|K.
- On100, the main-lower inventory excerpt can include the hook already separately inventoried; there is no missing-inventory-element claim.
- Historical crop counts, first-pass process descriptions and physical line counts are not recomputed by this text-only review.

```json
[
  {
    "id": "A096-check-prefix-name",
    "file": "review/149_scan096_reviewed.json",
    "op": "replace_substring",
    "selector": {
      "array": "check_events",
      "match": {
        "statement_id": "149096-rational-point-section"
      }
    },
    "field": "outcome",
    "expected_occurrences": 1,
    "old": "it does not resolve the crowded initial E by mathematical expectation.",
    "new": "it does not resolve the crowded initial prefix by mathematical expectation.",
    "authority": "The same conditional check remains unchanged; B016 now prefers (f_K)_* while retaining E f_K|f_K."
  },
  {
    "id": "A098-target-index-notes",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_substring",
    "selector": {
      "top_level": true
    },
    "field": "notes",
    "expected_occurrences": 1,
    "old": "Both disputed targets are literal capital K, supported by sharp branches and same-page contrasts with rounded lowercase k in k(s) and E_k. The lower target K is retraced over a rounded stroke, but a separate deleted k is not recoverable.",
    "new": "The subscripts of both the inclusion target and the hooked-arrow target are capital K, supported by sharp branches and same-page contrasts with rounded lowercase k in k(s) and E_k. The lower target’s K index is retraced over a rounded stroke, but a separate deleted k is not recoverable. This does not resolve the separate E|K uncertainty in the earlier target’s main body.",
    "authority": "Final formulas and blind B005/B017/B024: the earlier main body admits E|K, whereas the two later target indices retain K."
  },
  {
    "id": "A098-target-index-main-review",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_substring",
    "selector": {
      "top_level": true
    },
    "field": "notes",
    "expected_occurrences": 1,
    "old": "Both target capitals K are retained from their angular branches and lowercase controls.",
    "new": "Both target K subscripts are retained from their angular branches and lowercase controls.",
    "authority": "Same distinction as A098-target-index-notes."
  },
  {
    "id": "A098-target-index-hand",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_fields",
    "selector": {
      "array": "hand_observations",
      "match": {
        "habit": "Angular capital K and rounded lowercase k must be compared locally."
      }
    },
    "old": {
      "evidence": "The inclusion and hooked-arrow targets have sharp branches; k(s) and the parenthetical E_k have rounded shoulders."
    },
    "new": {
      "evidence": "The K subscripts on the inclusion and hooked-arrow targets have sharp branches; k(s) and the parenthetical E_k have rounded shoulders."
    },
    "authority": "Clarifies which part of the target is certain, without changing the hand observation."
  },
  {
    "id": "A098-target-body-inventory",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_fields",
    "selector": {
      "array": "inventory",
      "match": {
        "element": "overdrawn-subgroup-symbol"
      }
    },
    "old": {
      "position": "baseline 5, before dans E_K"
    },
    "new": {
      "position": "baseline 5, before dans and the retraced \\unsure{\\mathcal E|K}_K"
    },
    "authority": "Blind B005 and the final page retain E|K for that main body; its K index remains certain."
  },
  {
    "id": "A098-tantot-note-spelling",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_substring",
    "selector": {
      "top_level": true
    },
    "field": "notes",
    "expected_occurrences": 1,
    "old": "tantot is retained from its two t stems and circumflex.",
    "new": "tantôt is retained from its two t stems and circumflex.",
    "authority": "The final page and B015 print tantôt; this only removes accentless shorthand from an otherwise consistent note."
  },
  {
    "id": "A098-aussitot-note-spelling",
    "file": "review/149_scan098_reviewed.json",
    "op": "replace_substring",
    "selector": {
      "top_level": true
    },
    "field": "notes",
    "expected_occurrences": 1,
    "old": "aussitot, obtenue",
    "new": "aussitôt, obtenue",
    "authority": "The final page and B021 print aussitôt; this is a metadata spelling clarification only."
  },
  {
    "id": "A100-main-lower-inventory",
    "file": "review/149_scan100_reviewed.json",
    "op": "replace_fields",
    "selector": {
      "array": "inventory",
      "match": {
        "element": "main_lower"
      }
    },
    "old": {
      "first_words_or_objects": "Ici l’action extérieure de T sur pi n’est sûrement pas triviale"
    },
    "new": {
      "first_words_or_objects": "Ici l’action extérieure de T sur pi n’est \\inserted{\\unsure{?}} sûrement pas triviale"
    },
    "authority": "Final page and blind B011. The added hook already has its own inventory entry, so this is an excerpt clarification rather than a missing-element finding."
  }
]
```

## Fields inspected without another change proposal

- **096:** the K notation, tt|tte notation/abbreviations, all current unresolved rows and the insertion placement descriptions otherwise agree with the final page.
- **097:** hand observations, notation, abbreviations, unresolved rows, insertion/deletion inventory, numeral inventory and final relative 1 description agree.
- **098:** the expanded unresolved list already includes the raised xi state, retraced target, extension alternatives, de/dé, de/des and all newly doubtful cancellations. The insertion inventory includes both f occurrences and the live extension leader. Its empty check list is consistent.
- **100:** unresolved rows include the two points before1 in (31), the hook after n’est, the changed opening word and cancelled phrase, and the still ambiguous connectors. The display31 and raised-hook inventory entries are present.
- **102:** all requested reading metadata agrees with the final page and blind adjudications. No automatic hand-attribution or reading edit is proposed.

## Reviewed snapshot hashes

SHA-256 values are recorded for auditability. These hashes are not permission to overwrite a newer canonical record.

```json
{
  "review/149_scan096_reviewed.json": "6318c587892245fff359419569a356dff9408204e913bf0881c3cdf7a09ce1dd",
  "pages/149_scan096.tex": "be1822fb09d4c89e8f1f1efd96f2da358aa266ebeaacfa1f51dc5fba13a59dc9",
  "second/149_scan096_adjudications.tsv": "fc0f91528e20828551924d236eb07185336bacbb9b55c95e73ca5a5ec9a49c98",
  "review/149_scan097_reviewed.json": "3f6ea95402a8c7196024114cdc5d121efb5854967f620a8a422fb6a61040698c",
  "pages/149_scan097.tex": "cdf4e82d6e17b75ed3ccf06c60740deff25ad2614d81adc74cc17f2ae87b543e",
  "second/149_scan097_adjudications.tsv": "60acf51d0d38ed364a89297f333f876ef8605ac954399c46c61a39c9d611413a",
  "review/149_scan098_reviewed.json": "7058482d38bce3639dc610065f8c15a23843227d611b01f715ba627c30940589",
  "pages/149_scan098.tex": "c450842b4f8b5d80a1f6167c9da018ec1fe8501d15ddb47a23ad56ba115b0b31",
  "second/149_scan098_adjudications.tsv": "75e4cd5c368ce04f22b118a3a05d9e72b6ce956e9555d1664115ffe64495edf8",
  "review/149_scan100_reviewed.json": "f07feb1d747512a17754fde8f244e46e30d61d7dcfc087d7f840b853dc498d16",
  "pages/149_scan100.tex": "7a2295c28130d89056c0a6cfecb66a7d9ae752faca70193c10ca5ce74ec14963",
  "second/149_scan100_adjudications.tsv": "418e4f671cea61a404da4e5bdec4b11352259ae3f3f669319c24ef66013d280e",
  "review/149_scan102_reviewed.json": "264bc041fd79e4ef02b618ff13309d3d6e1028153bfdf3c8e887d686505ef21b",
  "pages/149_scan102.tex": "ea940b0e5369d46a4b0859a9adc530bc46f5fc43bb64fb7f21fa2d46333bff0f",
  "second/149_scan102_adjudications.tsv": "972310335c535f4488118e8a39cb1dab4b2dd1805ed964b2a23cfeaf50aa726a"
}
```
