# Scan017 source union and root choices

All three independent returns are preserved. Root sections01–23 and the source-only corrections supply the selected readings. Main record approval/commit remains with root; no image bytes were read by the clerk.

## Current counts

```json
{
  "status": "All root local ink/count choices applied; final record approval pending.",
  "C": 22,
  "H": 33,
  "by_witness_confidence": {
    "C": {
      "high": 0,
      "medium": 14,
      "low": 8
    },
    "H": {
      "high": 6,
      "medium": 15,
      "low": 12
    }
  },
  "remaining_doubt_loci": 18,
  "inventory_elements": 39
}
```

## Complete decision crosswalk

| ID | Location | A | B | C-reader | Root selected | C count | H count | Original doubt status | Root section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 017-D01a | Opening cancelled subject E_i / Sigma_i | ["E_i"] | ["\\unsure{E_i\|\\Sigma_i}"] | ["E_i"] | \unsure{E_i\|\Sigma_i} | False | False | retained | 1 |
| 017-D01b | Opening cancelled short verb est / soit | ["\\unsure{est\|soit}"] | ["\\unsure{est\|soit}"] | ["\\unsure{est\|soit}"] | \unsure{est\|soit} | False | True | retained | 1 |
| 017-D01c | Opening cancelled adjective rare / dense | ["rare"] | ["\\unsure{rare\|dense}"] | ["rare"] | rare | True | False | resolved | 1 |
| 017-H01 | Opening parenthesis: si / où | ["si"] | ["si"] | ["si"] | si | False | True | pending root | 1 |
| 017-H02 | Opening cancelled sentence: terminal point | ["X."] | ["dans X."] | ["X$.}"] | dans $X$. | False | True | pending root | 1 |
| 017-H03 | Raised on ait insertion state | ["\\inserted{on ait}"] | ["\\inserted{on ait}"] | ["\\inserted{on ait}"] | \inserted{on ait} | False | True | pending root | 1 |
| 017-D02 | Cancelled trouve above the equalities | ["trouve"] | ["\\unsure{trouve}"] | ["\\unsure{trouve}"] | \deleted{Alors on \unsure{trouve} que} | False | False | retained | 2 |
| 017-H04 | First displayed equality: endpoint comma | ["no comma"] | ["E_i"] | ["E_i"] | No comma after first displayed E_i | False | True | pending root | 3 |
| 017-S01 | First displayed Sigma_i-plus closure bar | ["TeX: \\overline{\\Sigma_i^+}"] | ["TeX: \\overline{\\Sigma_i^+}"] | ["TeX: \\overline{\\Sigma_i^+}"] | \overline{\Sigma_i^+} | False | False | pending root | 3 |
| 017-S02 | Second displayed Sigma_i-minus closure bar | ["TeX: \\overline{\\Sigma_i^-}"] | ["TeX: \\overline{\\Sigma_i^-}"] | ["TeX: \\overline{\\Sigma_i^-}"] | \overline{\Sigma_i^-} | False | False | pending root | 3 |
| 017-G13 | Second equality endpoint: literal point and period-role choice | ["TeX: \\Sigma_i^-\\cup E_i ."] | ["TeX: \\Sigma_i^-\\cup E_i ."] | ["M01: locally qualified literal triangular point; period is retained as an interpretation alternative."] | C M01: exact locally qualified triangular fill with period alternative, represented once | True | True | pending root | 3 |
| 017-P01 | Two upper equalities: successive rows versus H horizontal layout | ["TeX: \\begin{aligned}\n\\overline{\\Sigma_i^+} &= \\Sigma_i^+\\cup E_i\\\\\n\\overline{\\Sigma_i^-} &= \\Sigma_i^-\\cup E_i .\n\\end{aligned}"] | ["TeX: \\begin{aligned}\n\\overline{\\Sigma_i^+} &= \\Sigma_i^+\\cup E_i\\\\\n\\overline{\\Sigma_i^-} &= \\Sigma_i^-\\cup E_i .\n\\end{aligned}"] | ["TeX: \\begin{aligned}\n\\overline{\\Sigma_i^+} &= \\Sigma_i^+\\cup E_i\\\\\n\\overline{\\Sigma_i^-} &= \\Sigma_i^-\\cup E_i\\hspace{1.5cm}\n% M01: source origin (1172,557); observed triangular point, period interpretation retained as alternative.\n\\mathpunct{\\unsure{\\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(monebase)]\n\\coordinate (monebase) at (0,6);\n\\path[use as bounding box] (0,0) rectangle (7,7);\n\\fill (1,5) -- (3,1) -- (5,0) -- (7,5) -- cycle;\n\\end{tikzpicture}\|.}}\n\\end{aligned}"] | Two successive equality rows in aligned; H horizontal source order preserved | False | False | pending root | 3 |
| 017-H05 | Prose before third equality: qu'on a / que | ["Alors je dis qu'on a"] | ["Alors je dis qu'on a"] | ["Alors je dis qu'on a"] | Alors je dis qu'on a | False | True | pending root | 4 |
| 017-S03 | Third displayed Sigma12 closure bar | ["TeX: \\overline{\\Sigma_{12}}"] | ["TeX: \\overline{\\Sigma_{12}}"] | ["TeX: \\overline{\\Sigma_{12}}"] | \overline{\Sigma_{12}} | False | False | pending root | 5 |
| 017-D03 | Third equality: first join physical cluster | ["cup form with doubled curved right return, drawn as G01"] | ["\\cup, reproduced as two curved passes (G01)"] | ["G01: locally qualified retraced cup graphic, with amalg alternative."] | Retraced cup: C G01 exact three-path graphic, outer unsure/amalg alternative removed | True | True | resolved | 5 |
| 017-D03-shape | Third equality: individual curved return paths | ["cup form with doubled curved right return, drawn as G01"] | ["\\cup, reproduced as two curved passes (G01)"] | ["G01: locally qualified retraced cup graphic, with amalg alternative."] | C G01 shared left stem, inner return and outer return; all three exact draw commands | False | False | pending root | 5 |
| 017-G02 | Separator below third equality | ["G02: shallow curved rule with downturned right endpoint"] | ["G02 shallow curved rule with hooked right endpoint"] | ["G02: bowed single rule with a short hooked right end."] | C G02 complete bowed separator figure and wide fixed rectangle | True | True | pending root | 6 |
| 017-H06 | Slanted note opening: introduire / introduisons | ["introduire"] | ["introduire"] | ["\\unsure{introduire\|introduisons}"] | introduire | False | True | pending root | 7 |
| 017-D04a | Slanted-note partition letter Pi / pi | ["\\unsure{\\Pi\|\\pi}_j"] | ["\\Pi_j"] | ["\\unsure{\\Pi\|\\pi}_j"] | \unsure{\Pi\|\pi}_j | False | False | retained | 7 |
| 017-D04b | Slanted-note E_j predecessor | ["\\deleted{\\unsure{\\Sigma}}E_j"] | ["\\deleted{\\unsure{\\Sigma}}E_j"] | ["\\deleted{\\unsure{\\Sigma}}E_j"] | \deleted{\unsure{\Sigma}}E_j | False | False | retained | 7 |
| 017-G12 | Shape reported beside the slanted-note closing brace | ["TeX: \\margin{introduire la partition $\\unsure{\\Pi\|\\pi}_j=\\{\\deleted{\\unsure{\\Sigma}}E_j,\\Sigma_j^+,\\Sigma_j^-\\}$}\n\\normalmarginpar"] | ["\\unsure{G03 short wedge}"] | ["TeX: \\margin{\\unsure{introduire\|introduisons} la partition $\\unsure{\\Pi\|\\pi}_j=\\{\\deleted{\\unsure{\\Sigma}}E_j,\\Sigma_j^+,\\Sigma_j^-\\}$}\n\\normalmarginpar"] | B-reported wedge is the existing lower-left S return in Soit; no separate marginal glyph | False | False | pending root | 7 |
| 017-H-MARGIN-ILL | H trailing marginal ill placeholder: one parent | ["\\deleted{\\unsure{\\Sigma}}E_j"] | ["\\unsure{G03 short wedge}"] | ["\\deleted{\\unsure{\\Sigma}}E_j"] | One H marginal parent: qualified crossed predecessor plus unspecified trailing ill; no further word supplied | False | True | pending root | 7 |
| 017-N03 | Considerons / Considérons: local accent | ["Considerons"] | ["Consid\\unsure{e\|é}rons"] | ["Consid\\unsure{e\|é}rons"] | Considerons | True | True | pending root | 8 |
| 017-G03 | Upper inserted Pi_J: guide path | ["same words with literal guide G03"] | ["unchanged Pi_J insertion plus G04"] | ["Inserted Pi_J plus G03 curved attachment guide."] | A G03 complete upper Pi_J insertion, one live de node, fixed origin and hooked guide | True | True | pending root | 9 |
| 017-D05 | Cancelled wording after de X | ["\\deleted{definie}"] | ["\\deleted{definie}"] | ["\\deleted{définie}"] | \deleted{definie} | True | True | resolved | 10 |
| 017-N04 | First live definie after cancelled wording: accent | ["definie"] | ["definie"] | ["TeX: définie par les"] | definie | True | True | pending root | 10 |
| 017-D07a | First main-text E_j predecessor | ["\\deleted{\\Sigma}E_j"] | ["\\deleted{\\Sigma}E_j"] | ["\\deleted{\\unsure{\\Sigma}}E_j"] | \deleted{\unsure{\Sigma}}E_j | False | True | retained | 11 |
| 017-D06a | Cancelled short opening before intersection | ["\\deleted{et}"] | ["\\deleted{\\unsure{et}} intersection"] | ["\\unsure{\\deleted{et}\|et} intersection"] | \unsure{\deleted{et}\|et} | True | True | mixed | 12 |
| 017-D06b | Live intersection: word, capital and state | ["\\unsure{Intersection\|intersection}"] | ["intersection"] | ["intersection"] | \unsure{intersection\|Intersection} | False | False | retained | 12 |
| 017-G04 | Inserted ternaires Pi_j: guide path | ["same insertion plus G04 bent caret"] | ["unchanged insertion plus G05"] | ["Inserted ternaires Pi_j plus G04 two-branch caret."] | A G04 complete ternaires Pi_j insertion, one de node and bent guide; X follows outside | True | True | pending root | 13 |
| 017-N05 | Plural definies before later E_j: accent | ["definies"] | ["definies"] | ["TeX: définies par les"] | definies | True | True | pending root | 14 |
| 017-D07b | Later isolated E/membership glyph and state cluster | ["\\deleted{\\unsure{\\in\|E}}"] | ["\\unsure{\\deleted{\\in}\|\\deleted{E}\|\\notin}"] | ["\\deleted{\\unsure{E\|\\in}}"] | \unsure{\deleted{\in}\|\deleted{E}\|\notin} | True | False | retained | 15 |
| 017-H-LATER-ILL | H later isolated-sign ill placeholder: one parent | ["\\deleted{\\unsure{\\in\|E}}"] | ["\\unsure{\\deleted{\\in}\|\\deleted{E}\|\\notin}"] | ["\\deleted{\\unsure{E\|\\in}}"] | \unsure{\deleted{\in}\|\deleted{E}\|\notin} | False | True | pending root | 15 |
| 017-G05 | Small upper mark before alpha in coproduct display | ["\\Sigma_j^{\\unsure{\\prime\|\\cdot}\\alpha}"] | ["TeX: \\Sigma_j^\\alpha"] | ["M03: local qualified short dark mark, with dotless j used in the text node to avoid a second printed dot."] | C complete M03 cluster: Sigma with dotless j, alpha, translated qualified point node and exact fill | True | True | pending root | 16 |
| 017-G05-index | C-reader dotless j node and upper-mark attachment component | ["TeX: \\Sigma_j^{\\unsure{\\prime\|\\cdot}\\alpha}"] | ["TeX: \\Sigma_j^\\alpha"] | ["M03: local qualified short dark mark, with dotless j used in the text node to avoid a second printed dot."] | \Sigma_{\jmath}^{\alpha} with the single translated M03 point | False | False | pending root | 16 |
| 017-G11 | Far-right pair of detached shapes | ["G11: two separate dark point shapes under local unsure qualification"] | ["TeX: \\Sigma_j^\\alpha\n\\]\n\n-- c'est aussi la partition definie par celle de"] | ["M02a and M02b: two separate qualified dark-speck paths."] | C M02a/M02b exact two-fill group with original hspace/raisebox placement and local qualification | True | True | pending root | 16 |
| 017-G11-upper | Far-right pair: upper shape component | ["G11: two separate dark point shapes under local unsure qualification"] | ["TeX: \\Sigma_j^\\alpha\n\\]\n\n-- c'est aussi la partition definie par celle de"] | ["M02a and M02b: two separate qualified dark-speck paths."] | C M02a exact upper-right fill | False | False | pending root | 16 |
| 017-G11-lower | Far-right pair: lower shape component | ["G11: two separate dark point shapes under local unsure qualification"] | ["TeX: \\Sigma_j^\\alpha\n\\]\n\n-- c'est aussi la partition definie par celle de"] | ["M02a and M02b: two separate qualified dark-speck paths."] | C M02b exact lower-left fill | False | False | pending root | 16 |
| 017-N06 | Final-paragraph definie: accent | ["definie"] | ["definie"] | ["TeX: c'est aussi la partition définie"] | definie | True | True | pending root | 17 |
| 017-G06 | Detached baseline point before first indexed union | ["\\unsure{.}\\,\\bigcup_{j\\in J}E_j"] | ["\\unsure{G06 baseline point}"] | ["TeX: celle de $\\displaystyle\\bigcup_{j\\in J}E_j$"] | B G06 exact locally qualified quadrilateral fill/mathord group before first bigcup | True | True | pending root | 18 |
| 017-D08a | Inserted lower Pi_J: upper ring | ["\\Pi_J^{\\unsure{\\circ\|0}}"] | ["\\Pi_J^{\\unsure{\\circ\|0}}"] | ["\\Pi_J^{\\unsure{\\circ\|0}}"] | \Pi_J^{\unsure{\circ\|0}} | False | True | retained | 19 |
| 017-G07 | Inserted lower Pi_J: guide path | ["same wording and ring qualification with guide G07"] | ["unchanged qualified insertion plus G07"] | ["The same insertion with G05 curved guide into de."] | B G07 complete inserted lower Pi_J ring, one de node and exact guide | True | True | pending root | 19 |
| 017-D11 | Middle indexed bigcup: cup and transverse-mark cluster | ["G08: visible cup plus short transverse stroke; role locally qualified"] | ["\\overline{\\bigcup}, reproduced by the literal cup and transverse stroke G08"] | ["G06: literal cup with short transverse stroke, locally qualified as to mathematical role."] | C G06 complete cup/transverse-stroke graphic with local unsure, limits and E_j | True | True | resolved | 19 |
| 017-D11-shape | Middle indexed bigcup: individual literal paths | ["G08: visible cup plus short transverse stroke; role locally qualified"] | ["\\overline{\\bigcup}, reproduced by the literal cup and transverse stroke G08"] | ["G06: literal cup with short transverse stroke, locally qualified as to mathematical role."] | C G06 exact cup contour and separate transverse draw command | False | False | pending root | 19 |
| 017-D11-role | Middle indexed bigcup: local qualification of stroke role | ["G08: visible cup plus short transverse stroke; role locally qualified"] | ["\\overline{\\bigcup}, reproduced by the literal cup and transverse stroke G08"] | ["G06: literal cup with short transverse stroke, locally qualified as to mathematical role."] | Local unsure on the literal middle-union graphic; function unassigned | False | False | pending root | 19 |
| 017-D08b | Binary partition Pi_J,j: upper ring | ["\\Pi_{J,j}^{\\circ} (circle/zero qualification inherited from first occurrence)"] | ["\\Pi_{J,j}^{\\circ}, carrying the page-first circle/zero qualification"] | ["\\Pi_{J,j}^{\\circ}, sharing the first ring qualification"] | \Pi_{J,j}^{\circ} (local circle/zero doubt retained through first-occurrence convention) | False | True | retained | 20 |
| 017-G09 | Inserted quantifier and induites: continuous guide/opening parenthesis | ["inserted quantifier and induites with G09 guide; no prose opening parenthesis"] | ["\\inserted{(j\\in J)} induites with G09"] | ["Inserted condition plus G07 long hooked guide."] | B G09 complete inserted condition, one induites node and continuous hooked guide | True | True | pending root | 20 |
| 017-G09-open | Induites guide: local opening-parenthesis interpretation component | ["inserted quantifier and induites with G09 guide; no prose opening parenthesis"] | ["\\inserted{(j\\in J)} induites with G09"] | ["induites, with G07 above it"] | H opening-parenthesis reading belongs to the selected continuous induites guide | False | False | pending root | 20 |
| 017-D12 | U subscript: predecessor and complete-state cluster | ["U_{\\unsure{\\deleted{J}J\|\\deleted{j}J\|J}}"] | ["U_{\\unsure{\\deleted{J}J\|\\deleted{j}J\|J}}"] | ["U_{\\unsure{\\deleted{J}J\|\\deleted{j}J\|J}}"] | U_{\unsure{\deleted{J}J\|\deleted{j}J\|J}} | True | True | retained | 21 |
| 017-D12-final | U subscript: separately named final J component | ["J in all selected complete-state alternatives"] | ["TeX: U_{\\unsure{\\deleted{J}J\|\\deleted{j}J\|J}}"] | ["TeX: U_{\\unsure{\\deleted{J}J\|\\deleted{j}J\|J}}"] | Final capital J in every retained complete-state alternative | False | False | pending root | 21 |
| 017-G10 | Raised U expression and guide to sur/X gap | ["insertion retained, with literal G10 guide"] | ["qualified inserted U expression plus G10"] | ["G08: bent guide descending beside sur to its full lower endpoint."] | B G10 complete raised U expression, one sur node and descending full guide | True | True | pending root | 21 |
| 017-G10-state | Raised U expression: insertion-state component | ["insertion retained, with literal G10 guide"] | ["qualified inserted U expression plus G10"] | ["\\inserted{U_{...}={}}"] | Raised U expression insertion state within selected B G10 parent | False | False | pending root | 21 |
| 017-D09 | Final quantified g / j | ["\\unsure{g\|j}"] | ["\\unsure{g\|j}"] | ["\\unsure{g\|j}"] | \unsure{g\|j} | False | True | retained | 22 |
| 017-H07 | Final extra closing parenthesis in H | ["(\\unsure{g\|j}\\in J)."] | ["(\\unsure{g\|j}\\in J)."] | ["(\\unsure{g\|j}\\in J)."] | $(\unsure{g\|j}\in J)$. | False | True | pending root | 22 |
| 017-D10 | Final Pour / Puis | ["Pour"] | ["Pour"] | ["Pour"] | Pour | True | False | resolved | 22 |
| 017-ARCHIVE | Archive numeral 16 comment and inventory coverage | ["TeX: % archive sheet number: 16"] | ["TeX: % archive sheet number: 16"] | ["TeX: % archive sheet number: 16"] | % archive sheet number: 16 | False | False | pending root | 23 |

## Original C rows and local states

| Original row | Primary loci | Local states | Component statuses |
| --- | --- | --- | --- |
| 1 | ["017-D01a", "017-D01b", "017-D01c"] | {"017-D01a": "retained", "017-D01b": "retained", "017-D01c": "resolved"} | {"017-D01a": [], "017-D01b": [], "017-D01c": []} |
| 2 | ["017-D02"] | {"017-D02": "retained"} | {"017-D02": []} |
| 3 | ["017-D03"] | {"017-D03": "resolved"} | {"017-D03": []} |
| 4 | ["017-D04a", "017-D04b"] | {"017-D04a": "retained", "017-D04b": "retained"} | {"017-D04a": [], "017-D04b": []} |
| 5 | ["017-D05"] | {"017-D05": "resolved"} | {"017-D05": []} |
| 6 | ["017-D06a", "017-D06b"] | {"017-D06a": "mixed", "017-D06b": "retained"} | {"017-D06a": [{"component": "et letters", "status": "resolved", "original_C_scope": true}, {"component": "cancellation target", "status": "retained", "new_qualification": true}], "017-D06b": [{"component": "word identity", "status": "supported"}, {"component": "initial case", "status": "retained"}]} |
| 7 | ["017-D07a", "017-D07b"] | {"017-D07a": "retained", "017-D07b": "retained"} | {"017-D07a": [], "017-D07b": []} |
| 8 | ["017-D08a", "017-D08b"] | {"017-D08a": "retained", "017-D08b": "retained"} | {"017-D08a": [], "017-D08b": []} |
| 9 | ["017-D09"] | {"017-D09": "retained"} | {"017-D09": []} |
| 10 | ["017-D10"] | {"017-D10": "resolved"} | {"017-D10": []} |
| 11 | ["017-D11"] | {"017-D11": "resolved"} | {"017-D11": [{"component": "transverse stroke presence", "status": "resolved", "confidence": "high"}, {"component": "mathematical role", "status": "retained", "confidence": "low"}]} |
| 12 | ["017-D12"] | {"017-D12": "retained", "017-D12-final": null} | {"017-D12": []} |

## Physical-parent count policy

| Parent | Witness | Children | Selected treatment |
| --- | --- | --- | --- |
| 017-H-MARGIN-ILL | H | ["017-D04b", "017-G12"] | Root section07: predecessor and unspecified placeholder grouped once without claiming exact positional identity. |
| 017-H-LATER-ILL | H | ["017-D07b"] | pending root |
| 017-D06a | H | ["017-D06b"] | pending root |
| 017-G10 | H | ["017-G10-state"] | Root section21 combines C-reader D33 insertion and D34 guide flags into one placement/guide count. |
| ["017-D03", "017-D11", "017-D12", "017-G11", "017-G05"] | C/H | [] | One count per physical cluster per witness; exact path/index/state children are noncount log rows. |

## Source completeness and prior computation

The draft retains113 raw differences,45 raw reader doubts and136 raw inventory rows, with their original identities and verbatim JSON spans. Forty literal drawing commands and all reader TeX characters have source mappings. Report-silent word choices and mark/qualifier representations have exact supplemental spans. The original twelve doubtful-reading rows contain eighteen primary loci; A names one extra noncount final-J component and B separately describes two aspects of its one D12. One existing B P03 coordinate event is preserved with exact source linkages and restricted placement scope; no calculation was rerun. All selected final-source attachments use the dedicated assembler current draft and map.

## Current selected-source attachments

Selected draft SHA256: `fe88173436631d1c0257cd4cc5857613fcce5bd8aef1de48a4ae3a5a485aaa7f`. Selected map SHA256: `e1f1c00e67bcc9d3234f3d24c1e580ddbfa1a89857804b5fe17d0c2ea3316ca8`. All56 decision entries,39 inventory entries and18 retained-doubt clusters are attached; overlapping inventory scopes retain their separate exact spans. Root final approval remains pending.

## Final source review

The single targeted source pass completed with no unresolved defect. It matched 763 distinct exact source spans, 117 final attachment entries and all 51 textual fingerprints. The review is recorded in scan017_source_audit.md. Root approval and commit remain pending.
