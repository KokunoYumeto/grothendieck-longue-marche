# Documentation consistency findings — proposed, not applied

## Scope and status

This audit covers canonical records and final pages for scans **079–095**, together with their completed second-reading adjudications. It also checks the explanatory inputs used by `scripts/aggregate.py`: `review/feedback.md`, `review/legibility.md`, and the separate `review/notation_comparison.md` register, against the operative `upload/PROMPT(20261121-115654).md`.

No source image was reopened, no new reading or mathematical check was made, and no canonical JSON, page, frozen reading, comparison, adjudication, or generated global document was changed. The proposed script was assembled and statically parsed; it was **not executed or imported**, including in its default validation mode. The three Markdown files beside it are drafts only. Manuscript-wide totals and comparative accuracy claims are deliberately omitted.

## Main finding

Completed decisions are generally present in the final pages and current `unresolved` entries, but several earlier paragraphs still assert the superseded first-pass reading. The appended blind-adjudication paragraphs do not remove these contradictions. Because `aggregate.py` copies `notes`, `hand_observations`, `notation_additions` and `inventory` directly, the stale text would also enter the generated notes, hand log, notation list, doubts and inventory.

The proposed script makes exact, guarded changes only in those four explanatory fields. It retains first-pass method history and the recorded mathematical arguments. The frozen first readings and the adjudications retain the complete history of rejected readings. `aggregate.py` already explains that initial method statements describe the first-reading stage; such historical statements are not treated as current claims that no later cross-leaf review occurred.

## Concrete corrections proposed

In the table, a box citation means the corresponding row in `second/149_scanNNN_adjudications.tsv`. Inventory excerpts are descriptions of the final ink, not new transcriptions.

| Scan | Stale explanatory statement | Proposed alignment with the completed record | Authority |
|---|---|---|---|
| 079 | The final caution quotes certain **les**; the inventory fixes the formula’s letters; notes say the author’s caution is in `check_events`. | Carry **les/le**, the local kappa/k and eta/k doubts into descriptions; say that `check_events` contains the separately recorded 079-N1 check, while author cautions remain in notes. | B002, B015; canonical `check_events` |
| 080 | The hand log calls the first two links of (16) securely headed; inventory fixes all arrows and includes the stop inside cancelled **car.** | Distinguish the secure first link of (16), doubtful second link, doubtful first link of (13), and shaft-preferred first link of (17). Keep the live stop outside cancelled **car** and the restored stop after **schéma.** | B005, B009–B011 |
| 081 | Notes describe only the original set of doubtful struck words; inventory gives **groupe** and **schéma** without the restored doubts. | Describe the added uncertainty in those two cancelled words while retaining the historical first-pass crop account. | B002, B014 |
| 082 | Notes claim `check_events` is empty and that the cancelled (21) digits are distinguishable. | Identify the later recorded 082-N1 check; retain doubt in cancelled (21) and final cancelled G_m. Distinguish the doubtful first gamma/xi occurrence from the resolved later **Quand gamma_i=0**. | B004, B008, B015–B016, B021; canonical `check_events` |
| 083 | The old cancelled-phrase summary omits **ce/et** and **leur**; the inventory fixes **le** after N_x. | Use **ce/et qui donne/devra/leur** and live **le/E** uncertainty. The canonical equals-sign hand and notation entries are already current. | B011, B013 |
| 084 | Inventory describes the numerator x and final **donc** without their local alternatives. | Include numerator **x/dotted x** and **donc/sur** doubt in those element descriptions. | B006, B014 |
| 085 | Notes claim an empty check list and a certain display label; inventory omits the recovered cancelled relation after H¹. | Refer to the recorded 085-N1 check; describe **(22)/(21)** and the doubtful cancelled **equals/isomorphism** relation. | B003, B009; canonical `check_events` |
| 086 | Notes and inventory still say E_Ueta; inventory still calls the prose shorthand barred m; the opening relation is described as certain equals. | Use final **E_UK**, written **=**, and explicit **equals/colon** doubt. | B001, B008–B009 |
| 087 | Notes call the entire marginal note cancelled, retain **Comme** as the sole preferred fragment, reject enclosing curves around the old local symbol, and quote certain **et la E extension**. | Distinguish the final margin line’s doubtful cancellation state; use **Si on/Comme**, the admitted old-symbol alternatives and doubtful replacement tilde, and **la/le** plus cancelled **suite/seule/sous**. Replace the pending-audit wording for the retained vertical isomorphism. | B003, B007, B010, B014, B016 |
| 088 | Notes still support an arrow for the upper middle diagram link and certify the terminal s of **lacets**. | Describe the four final headless links and **lacets/lacet**. Avoid claiming that every prose map is headless: the separately written headed map remains. Clarify E_tildeK in insertion-location descriptions. | B002, B005, B011, B014–B017 |
| 089 | The hand log still says live 6 over old 5; notes prefer an arrow for the pi-to-E connector; verb endings are described as settled. | Use underlying **6/5**, live **5/6**, a shaft-preferred internal connector, and the retained **peut/par** and **s’identifier/s’identifie** doubts. | B002, B006, B016–B017 |
| 090 | Notes still prefer eta in the nested indices, call the last raised addition E_Ueta, and omit **alors** and **on** from later doubt descriptions. | Use the final K readings, cancelled **alors** with retained alternatives, and **ns/on/nous**. The canonical hand and notation entries already record the K comparison. | B008, B014, B018, B021 |
| 091 | Notes still certify **transcendance**, retain subgroup K/U alternatives, describe an editorial question-mark placeholder, and prefer cancelled **le** and capital N. Inventory retains the placeholder. | Use **tr.-scend/tr.-scendance**, resolved subgroup K, cancelled **de/d**, cancelled **leur/le/sur**, **réf/N**, and cancelled **peut/permet**. Keep the opening rounded U. | B003–B004, B006–B009, B012, B017 |
| 092 | Notes say the target in (29) cannot be divided into an earlier name and live E; another paragraph retains only a whole-term overdraw doubt. | Record tentative cancelled **Gal** beneath live replacement E with shared k(s); retain **de extension/d’extension** and **entre/dentre**. | B006, B011, B021 |
| 093 | Notes still retain the old illegibility extent, **Alors**, **réciproque**, eta/K, and the old accented ending. The notation table still prints E_U(eta/K). | Use tentative raised **ou** and lower **pas/non**, **Ainsi/Aussi**, resolved **inverse**, final nested K, and **prete/prète/préter**. Update the matching hand and notation explanations. | B003–B004, B007, B014–B015, B017 |
| 094 | Notes still certify **On**, **regardons**, **fixé** and capital S, retain à where the final text has colons, and do not explicitly retain the right-side field form. The hand log still certifies S. | Carry the final alternatives, raised replacement state, two literal colons and doubtful xi-like form/raised point. Say that the expanded second box was adjudicated and the circumflex remains unresolved; it is no longer awaiting that inspection. | B002–B006, B008, B011–B012, B014 |
| 095 | Notes still end at certain **n’est**, omit the point beside B and the two points before N, say r/vee without plus, and describe **en lesquels**. Inventory fixes **biais** and cancelled **moins**. | Use **vient/n’est**, **B./B_0**, **../colon**, **r/plus/vee**, **sur/en les quels**, the p-with-raised-r short form and expanded local alternatives, and cancelled **unique/moins**. Scope the visual-only check statement to the first reader. | B007, B013, B016–B019, B027, B030; canonical recorded check |

## Inventory hand labels and attribution questions

The proposal normalizes existing **main manuscript/main cursive/main mathematical hand** labels on 080, 087, 090, 093 and the added 095 element to **his hand**. This is a label cleanup of an existing main-hand attribution, not a new handwriting determination. It also normalizes 080’s explicitly identified finer foliation hand to **another unnamed hand**. Cancellation descriptions are retained in the element text and notes, rather than inside the hand field.

The following are intentionally **not** changed automatically:

- **079 upper 39:** the final page and B018 retain the manuscript-page wrapper, but the inventory says **another unnamed hand**. The adjudication establishes the digits and wrapper, not the hand. A wrapper is insufficient evidence to overwrite the existing attribution.
- **087 upper 43 and lower 86:** inventory uses attribution-undetermined numeral descriptions; B018–B019 establish placement and readings. The proposed script leaves these numeral-hand entries untouched.
- **090 lower 89 and 093 upper 46/lower 92:** numeral-hand descriptions are nonstandard or explicitly unattributed. They require the root’s existing source judgment before assigning a more specific hand label.

These are documentary provenance questions for root review. No new image examination was performed for this task.

## Unresolved entries and stable identifiers

The current `unresolved` arrays generally carry the final reading decisions, including the removed K/eta and K/U doubts where those were settled, the added cancelled forms, and the new local punctuation/word alternatives. This semantic agreement does not make every Reading cell a literal diplomatic excerpt: the separate static audit identified the three 090 formatting defects below. The proposal does not edit `unresolved`; root will apply any approved replacements separately.

Some stable location IDs retain old names, such as `corps_de_N`, `cancelled_Alors`, `regardons` and `cancelled-moins`. Their accompanying readings have been updated. These identifiers should not be renamed merely to match the current preferred word; they identify the location and may be used by other records. The script likewise preserves inventory element IDs while correcting their descriptive text.

### Separate root-only replacements for 090 Reading values

These are proposed exact replacements for `reading` only, copied from the final page and preserving the same uncertainty and cancellation. They are **not included in the cleanup script**. The source is `pages/149_scan090.tex`, with completed adjudications B004, B013 and B015. The physical line breaks in the last formula are compressed below for a single table cell; its TeX row break is retained.

**`090.kappa`** — replace `\kappa_i\text{ preferred, at both occurrences}` with:

```tex
\unsure{\kappa|k}_i
```

**`090.f_deleted_words`** — replace `désigne ... aussi` with:

```tex
\deleted{\unsure{désigne|désignons} \unsure{aussi}}
```

**`090.f_deleted_formula`** — replace `lower exists i tel que; upper i in I(k), simeq, colon` with:

```tex
\deleted{$\begin{array}[b]{@{}c@{\ }l@{}} &\inserted{\unsure{i\in I(k)}\,\unsure{\simeq|\sim}:}\\ \exists&i\ \text{\unsure{tel que}} \end{array}$}
```

The “both occurrences” scope for `090.kappa` belongs in explanatory metadata, not in the Reading cell. The ellipsis in the old `090.f_deleted_words` value is an editorial omission marker, not source ink. The existence formula must retain its lower i, its upper inserted condition, the doubtful relation and the cancellation of both levels.

## Global explanatory drafts

`review/feedback_proposed.md` replaces the obsolete claim that 083/086 contain a distinct barred-m short form, the old K/U preference on 091, and the broad statement that 092 has no tentative earlier target name. It treats the first consolidation’s errors separately from witness errors, uses the final audited examples, and does not claim a completed audit outside 079–095.

`review/legibility_proposed.md` replaces the pending-second-reading language with a scoped assessment of completed adjudications. It does not repeat the unquantified global claim that C is generally closer. It explains recoverable text, residual uncertainty, crop-boundary limitations, author versus editorial doubts, and the limits of comparing place counts.

The historical `review/notation_comparison.md` remains untouched. Its pending dispositions and early eta/barred-m comparisons need a final section from root: completed decisions on 083/086/091 select the written equals sign, and 086/088/090/091/093 use the adjudicated K forms at the specified locations. This does not remove the separate kappa/Latin-k doubts on 088/090 or the gamma/xi doubt at the first class occurrence on 082. Any statement about controls outside this audit scope is cited only as an already-recorded adjudication comparison; those leaves were not opened in this task.

## Applying after review

The unexecuted proposal is `scripts/propose_documentation_cleanup.py`. It defaults to validation only; `--apply` is explicit. Every exact old value or note substring must match before any write, and the script refuses a target outside scans 079–095 or outside the four permitted explanatory fields. It checks that all other canonical fields remain unchanged. Each JSON replacement is atomic after the batch preflight.

It does not run aggregation or alter the feedback/legibility source files. After root reviews the proposed edits, resolves any desired numeral-hand attribution, and finishes the remaining adjudications, root can apply approved changes, promote or revise the two Markdown drafts, finish the notation-comparison dispositions, and regenerate the global documents through the established workflow. No manuscript-wide count in these drafts needs to be treated as final.
