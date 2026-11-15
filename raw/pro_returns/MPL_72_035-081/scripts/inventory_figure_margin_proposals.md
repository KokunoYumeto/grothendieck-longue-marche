# Figure, margin, and insertion inventory proposals

## Scope

This is a mechanical comparison of the saved TeX fragments with `records/scanNNN.json` for scans 039, 040, 047, 049, 058, 059, 066, 071, 073, 078, 079, and 080. No image, attachment archive, supplied context, or external mathematical source was consulted. No page, record, inventory, progress entry, or doubt was changed.

Element IDs below refer to the record order before this reconciliation: `049.24` means the twenty-fourth element in `records/scan049.json`. TeX line references describe the inspected source and may shift after edits. Proposed child rows expose graphic or annotation elements already present in TeX and named within a larger existing row; they do not supply additional manuscript content.

## Summary of proposed actions

| Scan | Count cue | Existing coverage and proposal |
|---|---|---|
| 039 | 1 margin call / 0 margin-note rows | The wrapper contains the vertical stroke already inventoried as drawing **039.14**. Keep that row; its position records the margin location. |
| 040 | 1 inserted call / 2 insertion rows | **040.13** matches the inserted `f`. **040.15** groups two underbrace labels. Separate those two labels in the inventory; their insertion status also needs reconciliation with the source markup, which currently uses ordinary underbraces. |
| 047 | 3 figure calls / 2 drawing rows | **047.19** already names the circled inserted exponent. Retain the insertion row and add a drawing child for its ellipse. |
| 049 | 6 margin calls / 5 margin-note rows | Split **049.24** into its two separately encoded marginal notes. Update the stale content prefix in **049.41** to the current TeX wording. |
| 058 | 2 figure calls / 1 drawing row | **058.19** includes the circled `et` in a larger marginal block. Add a drawing child for that ellipse. |
| 059 | 3 margin calls / 2 margin-note rows | The extra wrapper contains diagram **059.07**, which already records the upper-right location. Keep the existing mapping. |
| 066 | 0 figure calls / 1 drawing row | Source lines 4, 16, and 46 contain three separator runs. **066.08** groups the latter two; the header run is within the larger header area. Give the three runs individual inventory entries. |
| 071 | 3 figure calls / 0 drawing rows | Displays **071.17**, **071.18**, and **071.35** explicitly name the partial boxes. Retain the displays and add one drawing child for each box path. |
| 073 | 0 figure calls / 1 drawing row | **073.25** matches inline `\tikz` at line 40. Keep the drawing row. The zero count comes from use of `\tikz` without a `\figure` wrapper. |
| 078 | 1 figure call / 0 drawing rows | The bracketed formula is already included in marginal block **078.15**. Add a drawing child for the bracket path. |
| 079 | 1 margin call / 0 margin-note rows | Reclassify **079.01** from `text` to `margin note`; preserve its words and position. |
| 080 | 4 margin calls / 3 margin-note rows | The extra wrapper contains the cancelled `a_i` already inventoried as deletion **080.02** in the top-right margin. Keep that mapping. |

## Detailed mapping

### Scan 039: a graphic in a margin wrapper

At TeX line 39, the entire margin argument is a figure containing one path:

```latex
\margin{\figure{\begin{tikzpicture}\draw (0,0)--(0,-1.7);\end{tikzpicture}}}
```

Existing **039.14** is `drawing`, positioned “left of bottom paragraph,” with content “vertical emphasis stroke.” The source has one graphic element within a location wrapper, and that graphic already has an inventory row. Keep **039.14**; adding another row merely for the outer wrapper would list the same stroke twice.

### Scan 040: one marked insertion and two underbrace annotations

| TeX location | Source content | Existing row | Proposal |
|---|---|---|---|
| Line 21 | `\inserted{f}` | **040.13**, insertion, “overwritten first factor,” `f` | Keep. |
| Line 26 | `\underbrace{f(\Pi)}_{-\widetilde\sigma\widetilde\rho}` | First item of **040.15**, insertion, “below second bottom equation” | Give the annotation `-\widetilde\sigma\widetilde\rho` its own row. |
| Line 27 | `\underbrace{\Psi(\Pi)}_{-\sigma\Pi'}` | Second item of **040.15** | Give the annotation `-\sigma\Pi'` its own row. |

The two lower labels are present in the TeX. Their existing record calls them insertions, while their source encoding does not use `\inserted`. The primary transcriber must reconcile that state from the completed audit. Deleting the existing inventory entry to force a count match would discard its recorded annotation status. Splitting the two labels makes their coverage explicit while leaving that state question visible.

### Scan 047: circled exponent already included in an insertion row

| Figure call | Source identifier | Existing row | Proposal |
|---|---|---|---|
| Line 22 | Line with labels `i-2`, `i-1`, `i` and two curved links | **047.07**, drawing; related label note **047.06** | Keep. |
| Line 71 | Ellipse containing `\scriptstyle n-2p`, nested inside `\inserted` and the exponent of `2` | **047.19**, insertion, “circled n-2p” | Retain the insertion row for the exponent; add a drawing child for the enclosing ellipse, pointing to this same insertion. |
| Line 80 | Points and paired segments labelled `c_1`, `c_2`, `c_3`, …, `c_n`, and isolated `c` | **047.20**, drawing | Keep. |

The missing separate drawing row concerns the ellipse at lines 71–73; the existing insertion row already names both the exponent and its circle. No formula or graphic needs to be supplied from a new reading for this inventory split.

### Scan 049: two marginal notes grouped together, plus stale inventory wording

| Margin call | Current TeX argument or prefix | Existing row | Proposal |
|---|---|---|---|
| Line 70 | Aligned formulas beginning `\Delta'_n[C_0,\mathbin{-},C_{n-1}]` and `\delta'_n[B_0,\mathbin{-},B_{n-1}]` | **049.14**, factorizations | Keep the existing block. |
| Line 112 | `\unsure{chgt} notation` | First part of **049.24** | Make a distinct margin-note row. |
| Line 113 | `non, grâce au \unsure{régime} des paires` | Second part of **049.24** | Make a distinct margin-note row. |
| Line 118 | `\uline{NB} Il n'y a pas de cancellation de termes.` | **049.26** | Keep. |
| Line 157 | Figure containing `Attention $p=0$!`, an oval, and a connector | **049.35**, margin note, and **049.36**, drawing | Keep both existing child descriptions. |
| Line 183 | `Attention, $n-1$ et non $n$!` | **049.41**, currently “Attention aux dénom.!” | Replace that inventory content prefix with the current TeX wording; retain its bottom-margin position and kind. |

The line 183 discrepancy is between two saved artifacts. This report adopts no new handwriting reading and makes no change to the TeX. The split of **049.24** accounts for the margin-count difference without adding another physical note.

### Scan 058: circled word in a larger marginal block

The figure at line 2 maps directly to drawing **058.01**, the labelled lines `H_0`, `H_1`, `h_0`, and `h_1`. The second figure is at line 38:

```latex
\margin{\figure{\begin{tikzpicture}\node[draw,ellipse] {et};\end{tikzpicture}}
```

It continues with the bracketed `2\beta_1` passage and the material involving `Z\subset H_1`. Existing **058.19** names this combined marginal block (“et; 2 beta_1; Z subset H_1”), and **058.20–058.21** separately record its cancellations. Retain these rows and add a drawing child for the ellipse around `et`. Its label stays connected to **058.19** rather than being treated as another word elsewhere on the page.

### Scan 059: margin wrappers already mapped to diagram and note rows

| Margin call | Contents | Existing coverage | Proposal |
|---|---|---|---|
| Line 4 | The pairing-index equality, whose first uncertainty macro starts with `\rho_{ij}` | **059.03**, top-right margin note | Keep. |
| Line 35 | The `b_0,b_1,b_n,b_{n+1}` diagram with its primed row and lower brace | **059.07**, diagram, upper right | Keep the diagram row and its position. No independent prose occurs in this wrapper. |
| Line 42 | The two inclusions followed by the `\mathcal O_S` arrow diagram | **059.08**, marginal inclusions, and **059.09**, diagram below them | Keep both rows. |

Thus the three margin wrappers already map to four existing inventory elements of appropriate content kinds. The count difference alone supplies no unlisted physical element here.

### Scan 066: separator runs encoded as characters

The source has these distinct runs:

| TeX line | Encoded run | Existing coverage |
|---|---|---|
| 4 | `-{}-{}-{}-{}-` | Immediately follows the university header described in **066.01**; the current separator row does not name this position. |
| 16 | `---` | First part of **066.08**, “below title and below list.” |
| 46 | `\begin{center}---\end{center}` | Second part of **066.08**. |

All three runs are already present in the transcription. The recommended granular inventory keeps the header row and provides three separator rows, with their separate positions and exact character prefixes. This replaces the combined **066.08** description and makes the upper run explicit. Their use of character runs explains the zero `\figure` count; the report proposes no extra strokes or replacements in the transcription.

### Scan 071: formula displays include the box descriptions

| Figure call | Formula prefix and graphic path | Existing display row | Proposed drawing child |
|---|---|---|---|
| Line 40 | `-\rho\widetilde s_0=...`; path across part of the top, down the left, and along part of the bottom | **071.17**, “partial box -rho s0 tilde” | Partial box surrounding this display. |
| Line 47 | Aligned `-\rho\widetilde u` and `-2\rho\widetilde u`; another partial box path | **071.18**, “partial box -rho u tilde; -2rho u tilde” | Partial box surrounding this aligned display. |
| Line 103 | `-\dfrac{\rho\beta}{\sigma}\widetilde t_{n+1}=...`; three-sided path | **071.35**, “three-sided box -rho beta/sigma t_n+1 tilde” | Three-sided box surrounding this display. |

Retain the three display rows, including the two aligned formulas within **071.18**, and add three drawing children for the already named paths. The current rows have combined a formula and its drawn enclosure under the `display` kind; they have not omitted those formula blocks.

### Scan 073: inline TikZ explains the drawing without a figure macro

At TeX line 40:

```latex
\tikz[baseline=(s.base)]{\node[draw,circle,inner sep=2pt](s){$*$};}
```

Existing drawing **073.25**, “circled star,” directly matches this code. Keep it. The macro-count difference arises from inline `\tikz` rather than `\figure`; no additional inventory row is needed. The primary transcriber can review that wrapper choice as an encoding-consistency matter before freeze.

### Scan 078: drawn bracket within an existing marginal formula block

The `\margin` at line 73 contains the figure beginning at line 74. Its aligned pairings start with `\langle\widetilde s_0,a_i^\vee\rangle`; line 83 draws the bracket along the left and lower edge. Existing **078.15** is a margin note described as “bracketed pairings with a_i vee and a_i'.” Retain that row for the marginal formula block and add a drawing child for the bracket path. Both the formula and the bracket are already encoded and named in the existing combined entry.

### Scan 079: a title classified as ordinary text

At line 3, `\margin{Sous-espaces invariants}` maps exactly to **079.01**, currently `text`, positioned “top right,” with the same words. Reclassify that existing row to `margin note`; preserve its content and position. There is no need for a second row repeating the title.

### Scan 080: cancelled word in a margin wrapper

| Margin call | Source content | Existing row |
|---|---|---|
| Line 5 | `\deleted{$\unsure{a_i}$}` | **080.02**, deletion, top right, `a_i` |
| Line 17 | `NB` followed by the `\beta_i=0` equivalence and codimension annotation | **080.09**, margin note |
| Line 19 | `\unsure{b}` | **080.10**, margin note |
| Line 57 | `NB Si c\notin C ...` | **080.29**, margin note |

The extra wrapper localizes the cancelled word already covered by **080.02**. Keep that deletion row and its top-right position. The four wrappers do not require four additional note rows because one contains only the already inventoried deleted element.

## Handoff

The parent mechanical reviewer handles deletion-group reconciliation separately. The primary transcriber owns all decisions and edits to the records, inventory, and manuscript fragments. After accepted changes, regenerate the inventory through the established record workflow and rerun the coverage report; some wrapper-versus-kind count differences remain fully explained by the mappings above.
