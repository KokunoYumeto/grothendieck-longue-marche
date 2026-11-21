# scan019 source-only TeX candidates

A/B/C are released. Root owns every ink selection and count. Exact complete groups, containing blocks, literal commands and UTF-8 offsets are in scan019_tex_candidates.json.

| Group | Exact source lines | Literal components | Declared origin / baseline | Attachment |
| --- | --- | --- | --- | --- |
| A_G01 | out/readers/019/A/reading.tex:8–14 | draw, draw, draw | [580, 535] / 60 | The group ends before _{J,i}; the container also contains both paired terms. |
| A_G02 | out/readers/019/A/reading.tex:16–16 | cdot | standard TeX placement / not declared | The inline formula includes the complete word l'une/l'un, the phantom l'un and one qualified cdot. Surrounding prose is outside the inline formula. |
| A_G03 | out/readers/019/A/reading.tex:24–31 | draw, draw, draw, draw | [895, 965] / 80 | The group ends before limits; the container includes the J|j predecessor and the complete equality. |
| A_G04 | out/readers/019/A/reading.tex:46–53 | draw, draw, draw, draw | [820, 1605] / 80 | The group ends before limits; the containing display includes the complete lower equality. |
| B_G01 | out/readers/019/B/reading.tex:8–14 | draw, draw, draw | [580, 540] / 54 | The group ends before _{J,i}; its unsure argument includes the literal alternate deleted-equality-plus-U. |
| B_G02 | out/readers/019/B/reading.tex:20–25 | fill, fill | [1125, 790] / 0 | A terminal percent follows the word's unsure group. The zero-width right-aligned makebox attaches immediately to it; des deux follows the box. |
| B_G03 | out/readers/019/B/reading.tex:47–52 | fill, fill | [1616, 1680] / 0 | A qquad precedes the complete qualified pair inside the lower equality display. The full source container already contains that equality. |
| C_M01 | out/readers/019/C/reading.tex:7–15 | fill, draw | [1124, 790] / (0,0) | The full inline underset includes hspace{1.5em}, vcenter/hbox, both literal components, and the single complete l'une/l'un word group. |
| C_M02 | out/readers/019/C/reading.tex:20–20 | cdot | standard TeX placement / not declared | The overset contains one qualified dot and the whole deleted J|jmath body; live K_0 follows outside this complete group. |
| C_M03 | out/readers/019/C/reading.tex:26–35 | draw, draw | [488, 1276] / (0,0) | The vcenter/hbox/unsure group is followed by quad and then the complete left brace. Its second draw command occupies two physical lines. |
| C_M04 | out/readers/019/C/reading.tex:45–53 | fill, fill | [1618, 1684] / (0,0) | The complete underset contains both literal ellipses, vcenter/hbox and the vphantom{Sigma} second argument; qquad precedes it inside the full lower display. |
| C_M05 | out/readers/019/C/reading.tex:44–44 | cdot | standard TeX placement / not declared | The exact qualified dot follows the equality and precedes the thin-space command and X; its containing display also holds M04. |

## Report-silent or adjacent source choices

- L01 — opening abbreviation: Preserve the selected local acute/grave qualification; a reader's absent difference row supplies no alternate reading.
- L02 — cardinality inequality: A's exact macro choice requires an explicit selected-source decision; no ink or count conclusion is assigned here.
- L03 — Au before ordinal: Exact excerpts preserve Soit state as context and the firm/qualified Au source states; counts remain root-owned.
- L04 — first overwritten union index: This adjacent index lies in A G03's complete equality container but outside its literal graphical group.
- L05 — complete On a state before donc: Keep all selected complete-state alternatives within one group; do not append another On.
- L06 — ordinal after Au: Candidate order differs in the exact sources.
- L07 — sign between borner and sommer: The preceding sign and the sommer word occupy separate loci; each source excerpt preserves their adjacency.

## Overlap attention

- A G02's inline group already includes l'une/l'un; B G02's makebox follows its separately qualified word. A selected word/group attachment must preserve the word once.
- A G04 and B G03 have containing displays for the same complete lower equality. B G03's exact placement span begins with qquad and contains only its point group/comments; copying both full display containers would repeat the equality.
- A G03's complete equality includes J|j, while B's complete equality has J. The graphical group ends before limits, allowing the selected adjacent predecessor to be tracked as its own literal replacement.
- A G01's printed unsure group has a drawing primary only; B G01's printed unsure group additionally contains |deleted{=}U. Preserve the root-selected complete group.
- C M01 already includes the complete l'une/l'un word. Its hspace/underset/vcenter/hbox and the chosen word must travel together.
- C M02 contains the whole predecessor plus one point; selecting M02 together with another complete predecessor would duplicate that body and may duplicate the j dot.
- C M03's second draw command spans two source lines; its quad and following brace placement are separately captured.
- C M04 and M05 share one containing lower display. Each has its own exact local group; M04's placement includes qquad and vphantom{Sigma}.

The map preserves every literal draw/fill and the separate bounding-box, node or coordinate source commands. Declared coordinates and scales are copied from source. No rendered or metric validation is claimed.

Current preamble is recorded by hash and remains unchanged. No final draft has been assembled.
