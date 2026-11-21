# Administrative audit corrections

This pass synchronizes canonical metadata with the already accepted independent-reading adjudications. It makes no new manuscript-reading decisions.

The initial pass described below wrote the seven reviewed JSON files listed in its sections and this log. The follow-up pass is recorded separately at the end. Page TeX and its readings are unchanged. Frozen first readings, box lists and second readings, root choices/adjudications, first-pass reports, source files and crops are unchanged. No assembly or other global writer was run; consolidated deliverables remain for the root to rebuild.

## Scan 108 — `147_scan108_reviewed.json`

- Changed `sheet_kind` from `manuscript` to `text` in all 28 inventory entries.
- Changed inventory `E08.first_words_or_objects` from `\unsure{points|couples}` to `\deleted{\illegible{1}}`, following audit B13.
- Replaced the unresolved summary naming points/couples with a statement that the word remains illegible and those earlier candidates were withdrawn in B13.
- Changed inventory `E13.first_words_or_objects` from `\unsure{var.}` to `\deleted{\unsure{var.|ens}}`, following audit B23.
- Annotated nested decisions `C108-N02` and `C108-N04` with explicit superseded-by-audit status, references to B13 and B23 respectively, current readings `\deleted{\illegible{1}}` and `\deleted{\unsure{var.|ens}}`, and current confidence `low`. Their original reading, decision, evidence and confidence fields remain intact as historical records.

## Scan 111 — `147_scan111_reviewed.json`

- Replaced the unresolved lower-route-label summary naming only can./iso. with par fonct. / can. / iso., explicitly identifying par fonct. as the leading tentative reading accepted in B04.

## Scan 114 — `147_scan114_reviewed.json`

- Updated inventory `E08.first_words_or_objects`: `dans la cat des` now reads `dans la \unsure{cat\textsuperscript{ie}|cat} des`, matching B07/B08 and the canonical page, row and doubt.

## Scan 115 — `147_scan115_reviewed.json`

- Replaced the unresolved statement that ens is the only candidate with the accepted ens/en uncertainty, ens leading, from B02.
- Annotated the nested decision at `opening canceled ens` with explicit superseded-by-audit status and a B02 reference, current reading `\deleted{\unsure{ens|en}}`, and current confidence `low`. All its original fields remain intact as historical records.

## Scan 116 — `147_scan116_reviewed.json`

- Replaced the unresolved cancelled-coproduct-index summary naming only d-prime with the accepted tentative p≤d-leading reading and d′ alternative from B04.

## Scan 117 — `147_scan117_reviewed.json`

- Removed the unresolved item concerning a single/double prime on the base under the acting group in the live triple definition. B15 already resolves that base to `D_{d,d'}`; its resolution remains recorded in the existing adjudication and canonical metadata.

## Scan 119 — `147_scan119_reviewed.json`

- Kept inventory identifier `E03`, changed its unsupported kind `deletion and insertion` to `deletion`, and restricted its recorded content to `\deleted{\unsure{ordinaire}}`.
- Appended unique inventory entry `E22`, kind `insertion`, for the raised `\inserted{analytiques}` above that cancelled word. Existing inventory identifiers were not renumbered.
- In the row `canceled word below analytiques`, changed `against_H` from `false` to `true`, so the accepted tentative recovery of ordinaire from H's illegible span will enter H collation on rebuild. `marked_in_H` remains `true`; the reading and confidence are unchanged.

## Initial-pass counts and verification

- 7 canonical reviewed JSON files updated; 1 correction log created.
- 30 existing inventory records updated; 1 new inventory record appended.
- 3 nested historical decisions explicitly marked superseded, with current readings and audit references added.
- 4 unresolved summaries rewritten; 1 resolved item removed from the unresolved list.
- 1 witness-collation flag changed; its existing marked-in-H flag retained.

Before writing, field-level assertions verified the expected prior values, the authorized edit scope, preservation of the original nested fields, unchanged second-box/audit/decision/doubt arrays, and uniqueness of inventory identifiers. The resulting JSON files were parsed again after writing. No page or frozen-reading files were opened for writing.


## Follow-up metadata reconciliation — 2026-11-21

This follow-up changes canonical metadata only. It applies already accepted audit readings, regenerates current unresolved summaries, and corrects two event metadata fields. It makes no new manuscript-reading decision.

### Exact targeted corrections

- Scan 116, rows[5].H (first crowded insertion, pondéré): replaced the English-prefixed shorthand with the literal associated H passage:
```tex
\drawing{petit schéma : un point d'où partent deux flèches, la seconde se factorisant par la première au moyen d'une flèche en pointillé ; annoté « prédicat \uncertain{par} $d'$ »}
```

  The existing marked_in_H flag remains true.
- Scan 115, notes[5] (N115-06): replaced the current undulating-stroke description with the short dash and separate dot after (174), preserving the separate down-right pointer; labeled the earlier description superseded by B21.
- Scan 116, notes[1] (N116-02): describes the forked grouping stroke and labels the earlier normalized-brace description superseded by B03; retains the separate uncertain opening arc.
- Scan 117, notes[4] (N117-05): retains the unresolved high d clusters but states that B15 resolved the lower group base to D_{d,d'} with one prime.
- Scan 117, notes[6] (N117-07): leads with that current single-prime reading and preserves the complete original discussion under an explicit historical, superseded-by-B15 label.
- Scan 117, notation[4]: changes the form to the wedge with group base D_{d,d'} and records the B15 single-prime resolution in meaning_or_form; its place is unchanged.
- Scan 114, abbreviations[0].form: changes bare cat to the accepted uncertain raised-ie/bare-cat form, matching B07/B08. Its expansion is unchanged.
- Scan 119, notes[6] (N119-07): qualifies the cancelled abbreviation as codimens.|codim after B03 and labels the earlier unqualified codimens. reading superseded.
- Scan 119, abbreviations[1]: changes the form to codimens.|codim under the uncertainty wrapper, and makes the codimension expansion conditional on that unresolved reading.
- Scan 120, abbreviations[6].form: changes diff. to diff, following B06's separate comma; its expansion is unchanged.
- Scan 120, notation[5]: retains the clear bottom-chain s_i and canonical-map i_d while separately recording final-line s_i|s under the uncertainty wrapper, following B21; its places are unchanged.
- Scan 126, check_events entry with statement_id AUD126; N126-10: adds the explicit date 2026-11-21.
- Scan 129, check_events entry with statement_id R129-continuation-shapes; N129-13: changes only who to:

> GPT-6 Astra Pro; effort not separately exposed; SP80_C13_147 first-pass continuation review; reader_c; root confirmed the distinctions on existing crops before authorizing this patch


### Regenerated unresolved summaries

For each supplied scan from 108 through 126 (118 is absent), replaced the unresolved array with one summary per current doubts entry, in its existing order. The rule is: place, literal current reading, then the current alternatives text. Source doubts were not modified. In scan 109's live-verb summary only, the inherited phrase “acute-looking stroke requires root review” becomes “acute-looking stroke remains uncertain”, removing completed-work boilerplate without changing the doubt.

| Scan | Previous summaries | Current summaries from doubts |
| --- | ---: | ---: |
| 108 | 8 | 9 |
| 109 | 7 | 15 |
| 110 | 7 | 10 |
| 111 | 8 | 13 |
| 112 | 8 | 10 |
| 113 | 3 | 4 |
| 114 | 6 | 7 |
| 115 | 6 | 9 |
| 116 | 9 | 14 |
| 117 | 8 | 14 |
| 119 | 9 | 15 |
| 120 | 14 | 15 |
| 121 | 7 | 5 |
| 122 | 5 | 7 |
| 123 | 9 | 10 |
| 124 | 4 | 10 |
| 125 | 7 | 7 |
| 126 | 11 | 11 |


### Follow-up counts and verification

- 19 canonical JSON files updated: all 18 supplied scans in 108–126, plus the one authorized event field in scan 129.
- 18 unresolved arrays rebuilt: 136 previous summary entries replaced by 185 current doubt-derived entries.
- 16 explicitly targeted JSON leaf fields changed outside those arrays, affecting one witness row, five notes, two notation records, three abbreviation records, and two check events.
- The complete former scan 117 lower-base discussion remains available as explicitly superseded historical text.
- No fields in scans 127, 128, 130 or 131 were changed; no other scan 129 field was changed.
- Field-level assertions checked the expected prior values and authorized change paths, unchanged source doubts, second_boxes and audit_changes, and the retained scan 117 historical discussion. JSON files were parsed again after writing.
- Page TeX, frozen first/box/second files, root choices/adjudications, first-pass reports, source witnesses, crops, and generated globals were not written. No assembly or other global writer was run.


## Post-audit corrections for scans 123–129 — 2026-11-21

This pass applies the authorized read-only consistency findings. It changes five canonical reviewed JSON files, the single Scan126 bullet in the shared notation source, and this log. It makes no new reading decisions.

### Witness quotations

- Scan123 rows[0].C/H and rows[1].C/H now quote the respective contiguous first-display (190) source passages, rather than lists assembled with editorial commas.
- Scan123 rows[3].H now quotes the contiguous span from H's underbrace through its marginal action note, including the intervening display boundary.
- Scan123 rows[10].H now preserves the math delimiters inside H's struck D_d; rows[14].H uses H's literal braced superscript form P^{*}_d; rows[16].H preserves H's three separately delimited decorated terms.
- Scan126 rows[6].C now quotes Prenant de $=$ literally.
- Scan129 rows[5].C now quotes the complete source tikzcd environment, including its source options and line breaks.
- All ten replacements were verified as exact contiguous substrings of the relevant packet C.tex or H.tex. Witness flags and audit counts are unchanged.

### Current metadata

- Scan124 inventory[14] / E15 now ends the final identity with the accepted point/comma uncertainty from B16.
- Scan129 inventory[8] / E09 now includes the comma after Groupes from B06.
- Scan126 notes[4] and hand_log[4].places now distinguish three headed long arcs, five downward-terminal shafts, and one adjacent T connector with a transverse cap.
- Scan126 notation[1].notation now gives the middle replacement index as q-prime/d-prime under uncertainty, and hand_log[2].misreadings uses that same primary order.
- The exact Scan126 bullet in edition/notation.md now records the q-prime-leading uncertainty and the three-arcs/five-turns/one-cap distinction; no other shared notation line changed.
- Scan128 notes[3] now refers to the interpreted indexed range from d_0 through d_r instead of calling an ellipsis-normalized expression the written tuple. Its arity-check scope is unchanged.
- Scan129 notes[3] now describes the literal asymmetric annotation line without a central brace cusp and explicitly supersedes the former overbrace representation.
- Scan129 notation[1].meaning_or_form retains torseur/fibré/fibrés, torseur leading, and the brace beneath the annotation above P_{d_0}.
- Scan129 notation[6].meaning_or_form records the bound's point–dash–dash and defining-map source's point–dash–point encodings from B01.
- Scan129 notes[12] is preserved in full as a historical pre-blind account. An appended status explains that B01 supersedes its cdots/ldots encoding while retaining its stroke observations.

### Verification and protected material

- Exactly 21 canonical leaf fields changed across scans123,124,126,128,129, plus one shared notation line.
- Field-level assertions checked the permitted paths, exact source quotation membership, unchanged decisions/doubts/unresolved arrays, unchanged audit_changes/audit_counts and second_boxes, and preservation of the complete original historical note129[12].
- JSON readback and notation-line checks passed. No page TeX, first-pass report, frozen reading/box file, root choice/adjudication, source witness, crop, or generated global was written.
- No assembly was run. Scan130 was reserved for a separate read-only check and was not edited.


## Scan130 metadata reconciliation — 2026-11-21

This pass synchronizes canonical scan130 metadata with the committed final text and root audits B02, B05, B07/B25, B12/B25 and B18/B26. It makes no new reading decision and required no further visual judgment.

### Current inventory and summaries

- Inventory[1] / E02 now begins with the accepted fibres|flèches uncertainty, with fibres first.
- Notes[0], notes[3], notes[6] and notes[12] retain their complete original first-pass text. Each now has an appended Historical status paragraph identifying the superseding root audit and the current result: the opening noun, the paired live-tuple strokes, the two separate annotation attachments, and the localized middle-digit uncertainty respectively.
- Hand_log[0].places excludes the live summation tuple from its single-stroke examples and explicitly identifies that tuple as the two-stroke case after B18/B26.
- Deletion_insertion_checks[0].finding retains its original first-pass finding and appends the superseding two-attachment result from B07/B25. Its literal witness span is unchanged.
- Nested_decisions[3] retains every original field, including its old whole-number reading, ink description, decision and confidence. Added explicit superseded-by-audit status, references to B12/B25, current reading 2 with uncertain middle 1|6|0 and final 0, current medium confidence, and the root's B12 evidence.

### Optional line reconciliation

The 32 line identifiers and their order are unchanged. Six entries were synchronized:

- L02 / index1: fibres|flèches in the opening, with current C/H status.
- L06 / index5: pose|posera, with current C/H status; the separate later On posera bien sûr remains unchanged.
- L10 / index9: the full accepted TeX for the two separately attached annotations, copied from current rows[7].final, with current C/H status.
- L11 / index10: de|du in the first image-inverse definition, with current C/H status.
- L12 / index11: number uncertainty localized to the middle digit, keeping outer 2 and 0.
- L24 / index23: two distinct continuation strokes in the live tuple, with corresponding C/H status.

### Verification and protected material

- Exactly 14 records were affected: one inventory entry, four historical notes, one handwriting entry, one historical nested decision, one historical insertion-check finding, and six current line-reconciliation entries.
- The exact accepted opening, pose|posera, de|du, two-attachment TeX, number tag and paired-stroke tuple were checked textually against the committed page before writing.
- Scope assertions verified all changed paths, unchanged current rows/decisions/doubts/unresolved arrays, unchanged audit_changes/audit_counts/second_boxes/check_events, preservation of every original nested-decision field, and intact prefixes for the historical notes and insertion finding.
- Canonical JSON readback passed. The page TeX was checked again and is unchanged.
- Only review/147_scan130_reviewed.json and this administrative log were written. Reports, frozen readings and boxes, root adjudications/choices, source witnesses, crops, shared notation, and generated globals were not written. No assembly was run.


## Exact C/H source quotation corrections — scans 108–122, 130–131

Completed 2026-11-21 00:19:51 UTC. This administrative pass changes witness quotation fields only; it makes no manuscript-reading decision. The assigned source sweep covers scans108–117,119–122,130–131 (118 is absent). Scans111,113,121,130,131 required no correction.

### Accounting and scope

- Exactly 31 C/H leaf fields changed in 26 rows across 11 canonical reviewed JSON files: scans108,109,110,112,114,115,116,117,119,120,122. Eight fields are C quotations; 23 are H quotations.
- Eleven corrections restore literal source spans, source insertion/uncertainty/note markup, or complete source macro boundaries in place of synthetic joins or abbreviated wrappers. Twenty corrections preserve the same quoted words and symbols while restoring literal TeX bracing, delimiters, spacing commands or layout syntax.
- The scan112 row0 H field now quotes H's actual explanatory note about the vertical signs, rather than an invented English description. Source notes and source illegibility/uncertainty placeholders are preserved exactly where quoted.
- All empty C/H omission fields were preserved. No reading choices, final fields, evidence, confidence, flags, counts, decisions, doubts, inventories, notes, audit records or second boxes were changed.

### Verification

Before writing, row-place guards checked every selector, all 31 replacement spans were verified as contiguous source substrings after whitespace normalization, and recursive field-level assertions established that only the authorized C/H leaves differed. Existing JSON formatting was preserved. Readback rechecked the same field-level scope and all 31 source-membership assertions. No page TeX, frozen reading, adjudication, source witness, crop, generated global or shared notation file was written. No assembly, image inspection, compilation or freeze was run. No unresolved semantic source issue was identified in this correction set.

### Exact before/after record

The selectors are zero-based and refer to each scan's `review/147_scanNNN_reviewed.json`.

```json
[
  {
    "scan": 108,
    "selector": "rows[1].C",
    "place": "upper left marginal note and upper (152)",
    "before": "(152)\\qquad D_{\\unsure{q|d}}\\longrightarrow X; \\margin{On introduit aussi $D_0=X$, et $D_0\\longrightarrow X$ l'identité}",
    "after": "\\[\n(152)\\qquad D_{\\unsure{q|d}}\\longrightarrow X\n\\]\n\\margin{On introduit aussi $D_0=X$, et $D_0\\longrightarrow X$ l'identité}"
  },
  {
    "scan": 108,
    "selector": "rows[21].H",
    "place": "second paragraph, muni insertion",
    "before": "ordonné muni d'une fonction codim., comme ci-dessus,",
    "after": "\\add{ordonné} muni d'une fonction codim., comme ci-dessus,"
  },
  {
    "scan": 108,
    "selector": "rows[26].H",
    "place": "second paragraph, D/X overwrite",
    "before": "x\\in D; « X » corrigé en « D »",
    "after": "$x \\in D$ \\note{« $X$ » corrigé en « $D$ ».}"
  },
  {
    "scan": 108,
    "selector": "rows[27].C",
    "place": "second paragraph, codimension insertion and et",
    "before": "x\\in\\deleted{D}\\inserted{X} \\inserted{de codim $d=d(J)$,} et",
    "after": "$x\\in\\deleted{D}\\inserted{X}$ \\inserted{de codim $d=d(J)$,} et"
  },
  {
    "scan": 108,
    "selector": "rows[27].H",
    "place": "second paragraph, codimension insertion and et",
    "before": "points, de codim.\\ $d = d(J)$, \\add{et} sont les couples",
    "after": "\\uncertain{points}, de codim.\\ $d = d(J)$, \\add{et} sont les couples"
  },
  {
    "scan": 109,
    "selector": "rows[15].H",
    "place": "line 19, cancelled mark above D!d",
    "before": "$D^!_d$",
    "after": "$D^{!}_d$"
  },
  {
    "scan": 109,
    "selector": "rows[21].H",
    "place": "oblique margin, opening formulas",
    "before": "Mais l'expression de $D_{I(d)}$ en termes de $D_d$ \\ill{} \\ill{} $D^!_d$",
    "after": "Mais l'expression de $D_{I(d)}$ en termes de $D_d$ \\ill{} \\ill{} $D^{!}_d$"
  },
  {
    "scan": 109,
    "selector": "rows[22].H",
    "place": "oblique margin, ne met pas en évidence",
    "before": "\\ill{} \\ill{} $\\mathfrak S_d$",
    "after": "\\ill{} \\ill{} $\\mathfrak{S}_d$"
  },
  {
    "scan": 110,
    "selector": "rows[2].H",
    "place": "line 6, end of definition (154)",
    "before": "\\mathbb{N}) ;",
    "after": "\\mathbb{N}$) ;"
  },
  {
    "scan": 110,
    "selector": "rows[3].H",
    "place": "line 9, balancing group in (155)",
    "before": "\\overset{(\\mathfrak S_d)_{D_d}}{\\wedge}",
    "after": "\\overset{(\\mathfrak{S}_d)_{D_d}}{\\wedge}"
  },
  {
    "scan": 112,
    "selector": "rows[0].H",
    "place": "diagram (162), both vertical identifications",
    "before": "\\wr with no-head vertical strokes; note: les deux $\\simeq$ sont écrits verticalement, sans flèche",
    "after": "\\note{ce diagramme porte le numéro (162) ; les deux $\\simeq$ sont écrits verticalement, sans flèche.}"
  },
  {
    "scan": 112,
    "selector": "rows[5].H",
    "place": "two additions in paragraph after (162)",
    "before": "\\add{et de $x\\in J$.} On \\add{a « un $J$- de $D_J$ »} d'autre part, par « fonctorialité »",
    "after": "\\add{et de $x \\in J$.} On \\add{a « un $J$- de $D_J$ »} \\note{lecture incertaine de cet ajout.} d'autre part, par « fonctorialité »"
  },
  {
    "scan": 112,
    "selector": "rows[8].C",
    "place": "prose below (163), two horizontal connectors",
    "before": "D_J-D_{d,\\delta} et D_{d,\\delta}-D_\\delta",
    "after": "$D_J-D_{d,\\delta}$ et $D_{d,\\delta}-D_\\delta$"
  },
  {
    "scan": 112,
    "selector": "rows[8].H",
    "place": "prose below (163), two horizontal connectors",
    "before": "D_J\\to D_{d,\\delta} et D_{d,\\delta}\\to D_\\delta",
    "after": "$D_J \\to D_{d,\\delta}$ et $D_{d,\\delta} \\to D_\\delta$"
  },
  {
    "scan": 114,
    "selector": "rows[14].H",
    "place": "end of identity description",
    "before": "morphisme « identité » ;",
    "after": "\\text{morphisme « identité »} ;"
  },
  {
    "scan": 114,
    "selector": "rows[15].H",
    "place": "composition domain: source label",
    "before": "(D_{**},b)\\times_{D_*}(D_{**},s)\\longrightarrow D_{**}",
    "after": "(D_{**}, b) \\times_{D_{*}} (D_{**}, s) \\longrightarrow D_{**}"
  },
  {
    "scan": 114,
    "selector": "rows[16].C",
    "place": "composition formula: punctuation and next line",
    "before": "D_{**}\\quad (u,v)\\longmapsto v\\circ u",
    "after": "\\multicolumn{2}{l}{(D_{**},b)\\times_{D_*}(D_{**},\\sigma)\\longrightarrow D_{**}}\\\\[5pt]\n\\multicolumn{2}{c}{(u,v)\\longmapsto v\\circ u}"
  },
  {
    "scan": 115,
    "selector": "rows[16].C",
    "place": "(174a) codim abbreviation punctuation",
    "before": "(le but est de codim $\\leq$ la codim de la source)",
    "after": "\\text{(le but est de codim}\\\\\n\\hfill\\leq\\text{ la codim de la source)}"
  },
  {
    "scan": 115,
    "selector": "rows[16].H",
    "place": "(174a) codim abbreviation punctuation",
    "before": "(le but est de codim. $\\leq$ la codim. de la source) ;",
    "after": "(le but est de codim.\\ $\\leq$ la codim.\\ de la source) ;"
  },
  {
    "scan": 116,
    "selector": "rows[0].C",
    "place": "head diagram, source-map symbols",
    "before": "\\sigma_d;\\ \\sigma^{-1}(D_d)",
    "after": "D_{d,*} \\arrow[r,\"\\sigma_d\"] \\arrow[d,equal,\"\\mathrm{def}\"'] \\& D_d \\\\\n\\displaystyle\\coprod_{\\substack{\\deleted{\\unsure{d'}}\\\\d'\\in\\mathbb N}}D_{d,d'}=\\sigma^{-1}(D_d)"
  },
  {
    "scan": 116,
    "selector": "rows[0].H",
    "place": "head diagram, source-map symbols",
    "before": "s_d;\\ s^{-1}(D_d)",
    "after": "D_{d,*} \\overset{s_d}{\\longrightarrow} D_d, \\qquad\nD_{d,*} \\overset{\\text{déf}}{=} \\coprod_{d'\\in\\mathbb{N}} D_{d,d'} = s^{-1}(D_d)"
  },
  {
    "scan": 116,
    "selector": "rows[6].H",
    "place": "after source donnée)",
    "before": "est loc. isomorphe",
    "after": "est loc.\\ isomorphe"
  },
  {
    "scan": 116,
    "selector": "rows[9].C",
    "place": "second crowded insertion, cardinal",
    "before": "\\inserted{avec sa relation d'ordre et la fonction ``cardinal''}",
    "after": "\\inserted{``pondéré'' par $d'$, avec sa relation d'ordre et la fonction ``cardinal''}"
  },
  {
    "scan": 116,
    "selector": "rows[11].H",
    "place": "final power-set superscript in the first block",
    "before": "\\mathfrak P(I_d)^\\circ",
    "after": "\\mathfrak{P}(I_d)^{\\circ}"
  },
  {
    "scan": 117,
    "selector": "rows[17].H",
    "place": "first associated-cover formula: position of acting group",
    "before": "\\overset{(\\mathfrak S_d)_{D_d}}{\\wedge}",
    "after": "\\overset{(\\mathfrak{S}_d)_{D_d}}{\\wedge}"
  },
  {
    "scan": 117,
    "selector": "rows[22].H",
    "place": "live triple-index definition: position of acting group",
    "before": "\\overset{(\\mathfrak S_{d'})_{D_{d,d'}}}{\\wedge}",
    "after": "\\overset{(\\mathfrak{S}_{d'})_{D_{d,d'}}}{\\wedge}"
  },
  {
    "scan": 119,
    "selector": "rows[7].H",
    "place": "second occurrence of the maps to D0",
    "before": "\\struck{($D_{d,0}\\simeq D_d$, $D_{d',0}\\simeq D_{d'}$)}",
    "after": "\\struck{($D_{d,0} \\simeq D_d$, $D_{d',0} \\simeq D_{d'}$) le soient, comme on voit en considérant}"
  },
  {
    "scan": 120,
    "selector": "rows[9].H",
    "place": "Cancelled first start before on a aussi",
    "before": "\\struck{\\ill{}}",
    "after": "\\struck{\\ill{} considérons les}"
  },
  {
    "scan": 120,
    "selector": "rows[21].H",
    "place": "Last line, D_1 and final section labels",
    "before": "$D_1$, pr. les $i$",
    "after": "$D_1$, pr.\\ les $i$"
  },
  {
    "scan": 122,
    "selector": "rows[21].C",
    "place": "Point after the outer parenthesis ending the first sentence",
    "before": "$D_d$).",
    "after": "D_d$)."
  },
  {
    "scan": 122,
    "selector": "rows[21].H",
    "place": "Point after the outer parenthesis ending the first sentence",
    "before": "$D_d$).",
    "after": "D_d$)."
  }
]
```

## Final controlled-vocabulary reconciliation — 2026-11-21 00:20:43 UTC

No reading, evidence, witness quotation, confidence, decision or audit count changed. Descriptive category detail is retained in `error_detail`; the required ten-category totals now include these rows. The continuation event already identified its model, effort and review; its provenance now explicitly names that review as a run.

- 147_scan122_reviewed.json rows[21].kind: punctuation -> misread symbol or index
- 147_scan122_reviewed.json rows[21].error_category: supplied punctuation -> Text that is not on the page
- 147_scan122_reviewed.json rows[22].kind: number -> misread symbol or index
- 147_scan122_reviewed.json rows[22].error_category: ambiguous numeral -> Symbols and indices
- 147_scan122_reviewed.json rows[23].kind: letter -> misread symbol or index
- 147_scan122_reviewed.json rows[23].error_category: ambiguous overtrace -> Symbols and indices
- 147_scan123_reviewed.json rows[23].kind: diagram -> drawing or diagram
- 147_scan123_reviewed.json rows[23].error_category: brace extent -> Drawings and diagrams
- 147_scan123_reviewed.json rows[24].kind: symbol -> misread symbol or index
- 147_scan123_reviewed.json rows[24].error_category: cancellation obscures lower bar -> Struck text
- 147_scan124_reviewed.json rows[24].kind: index -> misread symbol or index
- 147_scan124_reviewed.json rows[24].error_category: prime overlaps parenthesis -> Symbols and indices
- 147_scan124_reviewed.json rows[25].kind: punctuation -> misread symbol or index
- 147_scan124_reviewed.json rows[25].error_category: point versus comma -> Symbols and indices
- 147_scan125_reviewed.json rows[11].kind: punctuation -> misread symbol or index
- 147_scan125_reviewed.json rows[11].error_category: comma substituted for literal point -> Symbols and indices
- 147_scan126_reviewed.json rows[16].kind: diagram -> drawing or diagram
- 147_scan126_reviewed.json rows[16].error_category: full head supplied for terminal cap -> Drawings and diagrams
- 147_scan126_reviewed.json rows[17].kind: word -> misread word
- 147_scan126_reviewed.json rows[17].error_category: terminal letter not separable -> Words
- 147_scan127_reviewed.json rows[22].kind: word -> misread word
- 147_scan127_reviewed.json rows[22].error_category: compressed ending -> Words
- 147_scan128_reviewed.json rows[21].kind: symbol -> misread symbol or index
- 147_scan128_reviewed.json rows[21].error_category: normalized continuation and supplied comma -> Symbols and indices
- 147_scan128_reviewed.json rows[22].kind: symbol -> misread symbol or index
- 147_scan128_reviewed.json rows[22].error_category: continuation shape and punctuation -> Symbols and indices
- 147_scan128_reviewed.json rows[23].kind: punctuation -> misread symbol or index
- 147_scan128_reviewed.json rows[23].error_category: two detached marks -> Symbols and indices
- 147_scan128_reviewed.json rows[24].kind: symbol -> misread symbol or index
- 147_scan128_reviewed.json rows[24].error_category: normalized continuation and supplied comma -> Symbols and indices
- 147_scan129_reviewed.json rows[36].kind: symbol -> misread symbol or index
- 147_scan129_reviewed.json rows[36].error_category: alphabet -> Symbols and indices
- 147_scan129_reviewed.json rows[37].kind: symbol -> misread symbol or index
- 147_scan129_reviewed.json rows[37].error_category: continuation shapes -> Symbols and indices
- 147_scan129_reviewed.json rows[38].kind: punctuation -> misread symbol or index
- 147_scan129_reviewed.json rows[38].error_category: omitted comma -> Omissions
- 147_scan129_reviewed.json rows[39].kind: punctuation -> misread symbol or index
- 147_scan129_reviewed.json rows[39].error_category: elongated terminal mark -> Symbols and indices
- 147_scan129_reviewed.json continuation event provenance: explicitly label the already identified run
- 147_scan130_reviewed.json rows[32].kind: word -> misread word
- 147_scan130_reviewed.json rows[32].error_category: letter sequence -> Words
- 147_scan130_reviewed.json rows[33].kind: word -> misread word
- 147_scan130_reviewed.json rows[33].error_category: compressed short word -> Words
- 147_scan130_reviewed.json rows[34].kind: number -> misread symbol or index
- 147_scan130_reviewed.json rows[34].error_category: retraced digit -> Symbols and indices

## Final witness-count reconciliation — 2026-11-21 00:26:12 UTC

Excluded ten certainty-only/duplicate-locus rows from the witness-change tables, retaining their complete snapshots in `excluded_witness_rows`, their doubts, and all blind audit changes. Excluded one additional brace-scope row because H explicitly described that scope correctly. Five witness-specific flags were corrected here, plus the earlier131 agreement flag. No manuscript reading, mark decision or blind-audit count changed. Original pre-removal indices and complete evidence are in `review/witness_count_reconciliation.json`.

## Final literal reading field — 2026-11-21 00:27:10 UTC

Scan112 rows[0].final now quotes the actual rotated-simeq phantom connector code, which occurs twice in the final page, instead of the English description “rotated90 degrees, without arrows”. No reading, witness flag, confidence or count changed.
