# Scan 012 — source-only wrapper and coordinate review

## Outcome and scope

The inspected assembly preserves the checked local coordinate placements and all 68 literal C fill-path blocks and eight original label nodes. The concrete remaining review points concern the enlarged complete figure box and nearby superscript question-mark insertion sites. No image, OCR, browser, external research, compiler, renderer, format builder, page writer, or record writer was used. This report supplies no ink judgment or rendered validation.

Inspected draft SHA-256: `aa6ff5636640762690c811e80491e547d31adc408bf8d5c4b10d9370eaad0f67`.

Inspected builder SHA-256: `9922f8be141785e765de17c7e799844f19150404f1c2d01df4fcea4910917486`.

Primary sources: `out/checks/build_scan012_final_draft.py`, `out/checks/scan012_final_draft.tex`, `packets/012/C.tex`, and `out/PREAMBLE.tex`. Installed PGF/LaTeX implementation text was also inspected to resolve the wrapper operations; it was never executed.

## 1. Literal preservation and wrapper syntax

- Each of the 68 complete original `\path[fill=black,even odd rule] ... ;` strings occurs exactly once in the draft. Each of the eight complete original label-node strings occurs exactly once.
- The draft has 50 graphic wrappers: two original-source state groups and 48 additions. There are 52 `\unsure` invocations, including the two retained lexical invocations.
- The right-group wrapper contains precisely source paths 25, 32, 33, 38, 39, 41, 52, 54, 55, 56, 60, 61, 62, 64, and 67. The doubt-3 wrapper contains precisely paths 34, 36, 40, 42–51. The other 40 source paths remain at outer-picture level. The two sets have no shared path number.
- The 51 `tikzpicture` openings match 51 closings; 50 overlay scopes match 50 scope closings. Comment-stripped brace counting ends at zero and never becomes negative. The generated closing sequence closes the inner picture, `\unsure` argument, and node argument before the semicolon.
- Source contour order has been permuted by collecting state groups. Every retained contour operation still uses its literal black even-odd fill; no white mask, opacity, clipping, or extra contour copy was introduced.

## 2. Coordinate placement: finite examples

Every wrapper has `inner sep=0pt,outer sep=0pt,anchor=base west`. Its outer node position equals the inner `baseline={(xmin,yref)}`. Outer and inner pictures both explicitly use `x=0.0076cm,y=-0.0076cm`. The installed PGF source resets the transformation when typesetting node text and entering the inner picture; the node-content placement supplies a translation. The rectangle's `base west` anchor uses its west edge and text baseline. The smallest supplied rectangle width and height are both 5 source pixels = 1.0812047 pt, above the installed rectangle minimum size of 1 pt.

The following additions give actual coordinates in centimetres relative to the outer coordinate origin. Positive source y maps downward. These are nominal unit arithmetic; TeX's finite dimension rounding was not measured.

| Checked source point | Outer anchor in cm | Inner offset from box-left/baseline in cm | Result in cm | Direct source coordinate in cm |
|---|---|---|---|---|
| Right group, path 25: `(1179.5,349)` | `(6.15220,-5.7988)` | `(2.81200,3.1464)` | `(8.96420,-2.6524)` | `(8.96420,-2.6524)` |
| Doubt 3, path 34: `(292.5,564)` | `(1.18940,-5.542300)` | `(1.03360,1.255900)` | `(2.22300,-4.286400)` | `(2.22300,-4.286400)` |
| Added A11 endpoint: `(1387,903.5)` | `(10.5260,-6.88940)` | `(0.0152,0.02280)` | `(10.5412,-6.86660)` | `(10.5412,-6.86660)` |
| Added R11 centre: `(672.6,2007.4)` | `(5.0920,-15.25700)` | `(0.01976,0.00076)` | `(5.11176,-15.25624)` | `(5.11176,-15.25624)` |

The eight original labels remain outer-picture nodes with their original coordinates and font options. For example, the retained fourth node is still at `(1490,71)`, giving centre `(11.324,-0.5396)` cm. Its original lexical `\unsure{OK|Ok}` is also unchanged.

The appended question mark increases the node text width to the right. The chosen west/baseline anchor leaves the checked graphic origins in place. No `scale`, `xscale`, `yscale`, `resizebox`, `scalebox`, `transform shape`, shift, rotation, or canvas-matrix operation appears in the assembled draft.

## 3. Bounding boxes, strokes, and clipping

The state rectangles exactly contain their original vertex extents:

| Wrapper | Declared box and actual original vertex extents |
|---|---|
| Right group | `[809.5,348.6,1648.4,1177.4]` |
| Doubt 3 | `[156.5,564,381.5,894.5]` |

The 85 primitive statements inside the wrappers comprise 28 original fills and 57 added draw/fill statements. Source inspection of their endpoints, control coordinates, ellipse radii, and declared stroke half-widths found all inside their supplied rectangles. The narrowest added margin was R1's 1.2 source pixels; the right-edge B016 stroke retained approximately 1.32886 pixels after its 0.42 pt stroke was included. No ellipse rotation appears.

The supplied rectangle uses only `use as bounding box`; it has no `draw`, `fill`, or `clip` action. In the installed PGF source this operation stops subsequent paths from enlarging the picture bounds. The separate `[overlay]` scope also disables bound accumulation. Neither command installs a clipping path. No `\clip` or clipping option appears in the draft. The supplied preamble's `\figure` macro adds a centre environment without a crop or resize operation.

## 4. Concrete page-layout and annotation risks

**The complete outer figure has larger bounds.** Original contour vertices span x = 24.6–1648.4 and y = 23–1177.4: 12.34088 cm by 8.77344 cm. The new supplied boxes extend through x = 1674 and y = 2341. The corresponding span from the original contour minima is already 12.53544 cm by 17.6168 cm, before superscript extents. `\figure` centres the complete outer box, so source-coordinate preservation does not establish an unchanged position relative to the physical document margin.

The horizontal span alone is 356.6678145 pt. The supplied 11 pt article setup uses a 360 pt text width in the installed class. This leaves only 3.3321855 pt for the extra right-edge superscript extent. The source has no shrink-to-fit operation. Precise complete-box width, page breaking, and final margin clearance remain unmeasured.

**Separate question marks have tightly spaced insertion sites.** `PREAMBLE.tex` appends a normal-font superscript `?` after every graphical argument. Its `\unsure` macro supplies no leader, collision avoidance, or annotation-only outer overlay.

| Wrapper pair | Superscript insertion sites in source-coordinate units | Separation |
|---|---|---|
| C_N25 / R11 | `(678,2001.5)` / `(675,2007.5)` | 3 pixels horizontally and 6 vertically; about 0.649 pt and 1.297 pt |
| C_N01 / C_N02 | `(594,45.5)` / `(612,47)` | 18 pixels horizontally and 1.5 vertically; about 3.892 pt and 0.324 pt |

These spacings are concrete annotation-clearance review points. This review does not certify visible glyph separation or exclusion of glyph/contour overprinting. The actual mark bodies retain the coordinates checked above. The original black fills and explicit `black!…` additions retain their specified fill/stroke colours inside the orange `\unsure` group.

## 5. Cancellation-rule audit

No `\deleted`, `\sout`, `\cancel`, drawn node border, or new generic strike/cancellation rule occurs in the assembled draft. `\deleted` and `\sout` occur only in the supplied preamble's unused macro definition. The cancellation alternatives in the state wrappers are comments. The original graphical paths remain present, and the new visible editorial symbols supplied by `\unsure` are superscript question marks.

## Implementation text inspected

- `/usr/share/texlive/texmf-dist/tex/generic/pgf/frontendlayer/tikz/tikz.code.tex`: baseline handling, `overlay`, picture entry/exit, node text boxing, and node transformation.
- `/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorescopes.code.tex`: picture transform reset, picture interruption, and baseline extraction.
- `/usr/share/texlive/texmf-dist/tex/generic/pgf/modules/pgfmoduleshapes.code.tex`: rectangle minimum size, southwest calculation, and `base west` anchor.
- `/usr/share/texlive/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathusage.code.tex`: distinct bounding-box, fill/stroke, and clipping actions.
- `/usr/share/texlive/texmf-dist/tex/generic/pgf/systemlayer/pgfsys.code.tex`: picture-box left-edge and baseline offsets.
- `/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo` and `latex.ltx`: article text width and `\textsuperscript` implementation.

## Root provenance follow-up

The A09b mapping was extended to cross-reference both B006 and C D_N12, whose source rows cover the two separate rim fragments. Rebuilding changed only mapping provenance: the draft SHA-256 remains `aa6ff5636640762690c811e80491e547d31adc408bf8d5c4b10d9370eaad0f67`. No image was reopened and no geometry was changed. Current builder SHA-256: `716a05bf75a5f0684ce46c738ec5833df23472dbb2453b38673f9f763907ee1a`.
