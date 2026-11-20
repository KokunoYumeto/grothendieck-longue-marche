## Reader A

\scanpage{20}
Ainsi les classes de $\Pi_I^{\unsure{\circ|0}}$ sont les classes de $\Pi_J^\circ$ distinctes de $\deleted{\Pi}U_{J,i}$, et de plus les \unsure{clas.|deux.} parmi
\[
U_{J,i}\cap\Sigma_{\unsure{j|\deleted{J}i|i}}^+,\quad U_{J,i}\cap\Sigma_i^-
\]
qui sont non vides. Or les deux classes en question sont non vides, car
% A020-G01: cancelled Sigma with j/i index; glyph and complete cancellation state retained.
% Fixed source origin (320,817); local pixels right/down; baseline at source y=875.
% The two slanted cancellation runs are drawn once; the deleted annotation is invisible.
\begin{tikzpicture}[baseline=(A020G01base.base),x=0.025em,y=-0.025em]
\useasboundingbox (-2,-5) rectangle (82,85);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G01base) at (1,58)
{\rlap{$\Sigma_{\unsure{j|i}}$}\phantom{$\deleted{\Sigma_{\unsure{j|i}}}$}};
\draw[line width=0.35pt] (2,58)--(33,-1);
\draw[line width=0.35pt] (23,60)--(62,18);
\end{tikzpicture}
$U_{J,i}$ est un voisinage
% A020-G02: gray detached round point, source origin (1175,817), baseline y=817.
% Shape candidate only; role, hand and surface origin unresolved. No word is in this group.
\unsure{\begin{tikzpicture}[baseline={(0,0)},x=0.025em,y=-0.025em]
\useasboundingbox (0,0) rectangle (11,24);
\fill[gray] (4,18) ellipse [x radius=2.2,y radius=2.5];
\end{tikzpicture}}
de $\deleted{\Sigma}E_{\unsure{i|j}}$, et
\[
\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
\]
On sait donc que le nb des classes est en
% A020-G03: cancelled tout/est; fixed source origin (1457,1038), baseline y=1081.
% The observed two crossing runs replace a generic visible cancellation rule.
\begin{tikzpicture}[baseline=(A020G03base.base),x=0.025em,y=-0.025em]
\useasboundingbox (-2,-3) rectangle (130,53);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G03base) at (0,43)
{\rlap{\unsure{tout|est}}\phantom{\deleted{\unsure{tout|est}}}};
\draw[line width=0.45pt] (0,27)--(30,44);
\draw[line width=0.35pt] (46,8)--(80,26)..controls (96,34) and (110,40)..(122,41);
\end{tikzpicture}
$(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève \unsure{aussi|ainsi} la
% A020-G04: detached high triangular point after la; source origin (565,1395).
% Shape candidate only; role, hand and surface origin unresolved. No word is in this group.
\unsure{\begin{tikzpicture}[baseline={(0,0)},x=0.025em,y=-0.025em]
\useasboundingbox (0,-33) rectangle (12,0);
\fill (4,-31)--(7,-26)--(7,-22)--(2,-24)--cycle;
\end{tikzpicture}}
\unsure{dém.|dem.} \unsure{par|p} récurrence sur le nb des classes).

\uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
% A020-G05: complete formula and its added hatted label; no other words are in this group.
% Fixed source origin (1105,1660); local pixels right/down; formula baseline y=1735.
% The ordinary union operator, index, body, two parentheses and label occur once.
% The retraced left oval is drawn as the second path, beside the main brace run.
\figure{\begin{tikzpicture}[baseline=(A020G05body.base),x=0.025em,y=-0.025em]
\useasboundingbox (-210,-50) rectangle (275,145);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (-205,75)
{$X\setminus\displaystyle\bigcup_{\alpha\in\deleted{I}K}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G05body) at (0,75)
{$(\Sigma_\alpha^+\cup E_\alpha)$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (88,-6)
{$\inserted{\widehat{\Sigma}_\alpha^+}$};
\draw[line width=0.45pt] (12,20)..controls (42,18) and (60,13)..(82,16)
..controls (102,18) and (116,17)..(123,15)--(123,6)
..controls (145,16) and (168,13)..(184,10)
..controls (211,6) and (240,4)..(247,8)--(250,13);
\draw[line width=0.45pt] (22,22)..controls (33,13) and (50,10)..(64,16)
..controls (70,22) and (56,25)..(45,22)
..controls (36,19) and (29,19)..(22,22);
\end{tikzpicture}}
où $K$ est une partie
% A020-G06: complete cancelled insertion and curved guide with adjoining de I,.
% Fixed source origin (1148,1770); local pixels right/down; de I baseline y=1845.
% Exact word boundary: non vide (inserted and cancelled), de I,; partie and et remain outside.
% The phantom carries both editorial states without an extra visible generic strike.
\begin{tikzpicture}[baseline=(A020G06base.base),x=0.025em,y=-0.025em]
\useasboundingbox (-3,-5) rectangle (255,94);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,31)
{\rlap{\inserted{non vide}}\phantom{\inserted{\deleted{non vide}}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G06base) at (48,75) {de $I$,};
\draw[line width=0.45pt] (0,33)..controls (59,23) and (119,11)..(181,2);
\draw[line width=0.35pt] (31,74)..controls (25,52) and (55,37)..(105,27)
..controls (143,19) and (183,13)..(203,15)--(207,19);
\end{tikzpicture}
et
% slanted
\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{19}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}}}\normalmarginpar
$\forall\alpha\in K$, \deleted{on a} $\Sigma_\alpha^+
% A020-G07: complete observed reworked membership/arrow shape, source origin (945,1943).
% Full-state candidates: \deleted{\Rightarrow}\in | \deleted{\to}\in | \in.
% The primary is the first candidate; the third retains a live/retraced membership state.
% The phantom records the complete candidates; the local unsure qualifies the actual paths.
\mathrel{\unsure{\begin{tikzpicture}[baseline={(0,41)},x=0.025em,y=-0.025em]
\useasboundingbox (-2,-2) rectangle (55,55);
\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at (0,41)
{\phantom{$\deleted{\Rightarrow}\in|\deleted{\to}\in|\in$}};
\draw[line width=0.45pt] (38,4)..controls (24,1) and (1,25)..(1,33)
..controls (1,48) and (19,51)..(28,47);
\draw[line width=0.45pt] (2,33)--(41,28);
\draw[line width=0.35pt] (26,20)--(42,31)..controls (48,32) and (44,18)..(40,16);
\end{tikzpicture}}}
\pi_0(X\setminus{\unsure{E|\deleted{\Sigma}E}}_\alpha)$, tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
% archive sheet number: 19



{
  "differences": [
    {
      "id": "020A-01",
      "location": "Opening Pi_I superscript",
      "C": "\\Pi_I^{\\unsure{\\circ|0}}",
      "H": "\\Pi_I^0",
      "reading": "\\Pi_I^{\\unsure{\\circ|0}}",
      "evidence": "Small closed ring with a pale centre; both circle and zero remain supported. The primary circle is qualified against H; H zero survives as the alternative.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "01_first_ring.png",
      "bbox": {
        "coordinates": [
          1108,
          88,
          1227,
          165
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R01",
      "recurrence": "First of three; printed doubt here only."
    },
    {
      "id": "020A-02",
      "location": "Opening Pi_J superscript",
      "C": "\\Pi_J^\\circ",
      "H": "\\Pi_J^0",
      "reading": "\\Pi_J^\\circ; local alternatives \\circ|0",
      "evidence": "Separate small rounded closed outline above the hooked J. Local zero alternative remains even though the recurring primary alone is printed.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "02_second_ring.png",
      "bbox": {
        "coordinates": [
          670,
          194,
          783,
          280
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R01",
      "recurrence": "Second of three; source table scope includes this opening recurrence."
    },
    {
      "id": "020A-03",
      "location": "Opening distinctes de U",
      "C": "\\deleted{\\Pi}U_{J,i}",
      "H": "U_{J,i}",
      "reading": "\\deleted{\\Pi}U_{J,i}",
      "evidence": "Thin transverse cap and upright remnants survive beneath the much heavier U form. The overwritten predecessor is visible on half a.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinates": [
          1310,
          164,
          1469,
          265
        ],
        "origin": "original full scan, upper left"
      }
    },
    {
      "id": "020A-04",
      "location": "Opening word before parmi",
      "C": "\\unsure{clas.|deux}",
      "H": "deux",
      "reading": "\\unsure{clas.|deux.}",
      "evidence": "Tall loop over compressed low humps, followed by an isolated endpoint point. The compressed word supports clas. and deux.; the first candidate stays clas. The endpoint point is preserved with either candidate.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "03_deux_clas.png",
      "bbox": {
        "coordinates": [
          889,
          289,
          1008,
          349
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R02",
      "qualification": "Qualified H primary difference, with H word retained as alternative. C primary and its point remain; the explicit point on the alternative adds no independent C count."
    },
    {
      "id": "020A-05",
      "location": "First paired intersection, positive Sigma subscript",
      "C": "\\Sigma_{\\unsure{\\deleted{J}i|j|i}}^+",
      "H": "\\Sigma_i^+",
      "reading": "\\Sigma_{\\unsure{j|\\deleted{J}i|i}}^+",
      "evidence": "A high point accompanies a long descended stem and low left-returning double stroke. A continuous j is the working primary; overwritten J followed by i and plain i remain complete alternatives.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "04_paired_intersections.png",
      "bbox": {
        "coordinates": [
          823,
          393,
          933,
          498
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R03",
      "mathematical_consequence": "The primary transcription prints j at this one intersection. Later i occurrences are recorded independently and supply no repair."
    },
    {
      "id": "020A-06",
      "location": "Cancelled Sigma before U est un voisinage",
      "C": "\\deleted{\\unsure{\\Sigma_i|\\Sigma_j}}",
      "H": "\\struck{\\ill{}}",
      "reading": "A020-G01: \\deleted{\\Sigma_{\\unsure{j|i}}}, with two literal oblique cancellation runs",
      "evidence": "A Sigma body survives both crossings. The lowered right return gives j the primary position; i remains possible under the crossed strokes. Both cancellation runs are visible.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "05_cancelled_sigma.png",
      "bbox": {
        "coordinates": [
          319,
          810,
          403,
          903
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R04",
      "graphic_group": "A020-G01",
      "H_placeholder_parent": "H-ILL-01",
      "H_placeholder_count": 1,
      "change_components": [
        "Changed C index candidate order",
        "Recovered qualified glyph from H placeholder",
        "Two distinct cancellation runs replace a generic visible strike"
      ]
    },
    {
      "id": "020A-07",
      "location": "Below gap after voisinage",
      "C": null,
      "H": null,
      "reading": "A020-G02: locally qualified gray round point",
      "evidence": "The complete g descender closes to the left; a separate small gray rounded patch sits below the following gap. Shape is visible; its role, hand and surface origin remain undetermined.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "15_voisinage_detached_point.png",
      "bbox": {
        "coordinates": [
          1176,
          831,
          1185,
          839
        ],
        "origin": "original full scan, upper left"
      },
      "graphic_group": "A020-G02"
    },
    {
      "id": "020A-08",
      "location": "Index after voisinage de corrected E",
      "C": "E_{\\unsure{i|j}}",
      "H": "E_i",
      "reading": "E_{\\unsure{i|j}}",
      "evidence": "Short lowered hooked stroke with a separate comma farther below/right. The index itself remains too compressed to settle i/j.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "06_voisinage_E.png",
      "bbox": {
        "coordinates": [
          1386,
          791,
          1405,
          818
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R05"
    },
    {
      "id": "020A-09",
      "location": "Overwritten predecessor at voisinage de E",
      "C": "\\deleted{\\Sigma}E_{\\unsure{i|j}}",
      "H": "E_i",
      "reading": "\\deleted{\\Sigma}E_{\\unsure{i|j}}",
      "evidence": "Angular interior diagonals of Sigma remain inside the heavier upright and bars of E.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "06_voisinage_E.png",
      "bbox": {
        "coordinates": [
          1331,
          770,
          1391,
          820
        ],
        "origin": "original full scan, upper left"
      }
    },
    {
      "id": "020A-10",
      "location": "Comma after voisinage de E index",
      "C": "E_{\\unsure{i|j}}, et",
      "H": "E_i et",
      "reading": "E_{\\unsure{i|j}}, et",
      "evidence": "A separate low curved comma follows the small index; its upper and lower endpoints are within crop06.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "06_voisinage_E.png",
      "bbox": {
        "coordinates": [
          1396,
          819,
          1411,
          836
        ],
        "origin": "original full scan, upper left"
      }
    },
    {
      "id": "020A-11",
      "location": "First non-emptiness formula, E predecessor",
      "C": "\\overline{\\Sigma_i^+}\\cap\\deleted{\\Sigma}E_i",
      "H": "\\overline{\\Sigma_i^+}\\cap E_i",
      "reading": "\\overline{\\Sigma_i^+}\\cap\\deleted{\\Sigma}E_i",
      "evidence": "A thin angular Sigma interior remains beneath the heavy E. The closure rule above the first Sigma is already present in both witnesses.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "07_nonempty_formulas.png",
      "bbox": {
        "coordinates": [
          476,
          945,
          532,
          996
        ],
        "origin": "original full scan, upper left"
      }
    },
    {
      "id": "020A-12",
      "location": "Second non-emptiness formula, barred Sigma predecessor",
      "C": "\\overline{\\deleted{E}\\Sigma_i^-}",
      "H": "\\overline{\\Sigma_i^-}",
      "reading": "\\overline{\\deleted{E}\\Sigma_i^-}",
      "evidence": "The old left upright and horizontal strokes remain beneath the heavier diagonal Sigma body. The separate upper closure rule is visible.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "07_nonempty_formulas.png",
      "bbox": {
        "coordinates": [
          742,
          911,
          860,
          988
        ],
        "origin": "original full scan, upper left"
      }
    },
    {
      "id": "020A-13",
      "location": "Second non-emptiness formula, intersected E predecessor",
      "C": "\\deleted{\\Sigma}E_i",
      "H": "E_i",
      "reading": "\\deleted{\\Sigma}E_i",
      "evidence": "A diagonal interior angular run survives inside the live E at the right intersection.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "07_nonempty_formulas.png",
      "bbox": {
        "coordinates": [
          916,
          927,
          971,
          983
        ],
        "origin": "original full scan, upper left"
      }
    },
    {
      "id": "020A-14",
      "location": "On verb donc",
      "C": "\\unsure{voit|sait}",
      "H": "voit",
      "reading": "sait",
      "evidence": "The initial low returning stroke has an upper backward hook, followed by a small vowel loop, the marked i and tall terminal t. Working resolution is sait.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "08_voit_sait.png",
      "bbox": {
        "coordinates": [
          1358,
          891,
          1482,
          955
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R10"
    },
    {
      "id": "020A-15",
      "location": "Live word before cancelled count word",
      "C": "est en \\deleted{\\unsure{tout|est}}",
      "H": "est \\struck{\\ill{}}",
      "reading": "est en [cancelled tout/est]",
      "evidence": "The low open e followed by a linked n stands clear to the left of the cancelled word. Its strokes are live.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "09_cancelled_count_word.png",
      "bbox": {
        "coordinates": [
          1325,
          1058,
          1405,
          1094
        ],
        "origin": "original full scan, upper left"
      },
      "qualification": "This live en lies outside the cancelled H-ILL-02 physical word."
    },
    {
      "id": "020A-16",
      "location": "Cancelled word before count",
      "C": "\\deleted{\\unsure{tout|est}}",
      "H": "\\struck{\\ill{}}",
      "reading": "A020-G03: \\deleted{\\unsure{tout|est}} with two drawn crossing runs",
      "evidence": "Initial tall loop and final upturn survive; the intermediate body is crossed. Tout/est remains unresolved. The left short crossing and right long descending crossing are retained as separate literal runs.",
      "confidence": "low",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "09_cancelled_count_word.png",
      "bbox": {
        "coordinates": [
          1454,
          1035,
          1592,
          1094
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R06",
      "graphic_group": "A020-G03",
      "H_placeholder_parent": "H-ILL-02",
      "H_placeholder_count": 1,
      "lexical_diff_C": false,
      "qualification": "C count comes from the explicit crossing geometry; the lexical C doubt is retained."
    },
    {
      "id": "020A-17",
      "location": "Adverb in parenthesis before la",
      "C": "\\unsure{aussi|ainsi}",
      "H": "aussi",
      "reading": "\\unsure{aussi|ainsi}",
      "evidence": "The internal body is reduced to a long near-horizontal run, then a curved turn and a dotted final i. Internal letters remain unresolved.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "11_aussi_ainsi.png",
      "bbox": {
        "coordinates": [
          300,
          1367,
          447,
          1416
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R11"
    },
    {
      "id": "020A-18",
      "location": "High point in gap after la",
      "C": null,
      "H": null,
      "reading": "A020-G04: locally qualified detached triangular point",
      "evidence": "A discrete dark triangular point lies above and to the right of la. It is preserved once as a shape; its role, hand and surface origin remain undetermined.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "11_aussi_ainsi.png",
      "bbox": {
        "coordinates": [
          566,
          1363,
          574,
          1374
        ],
        "origin": "original full scan, upper left"
      },
      "graphic_group": "A020-G04"
    },
    {
      "id": "020A-19",
      "location": "Abbreviation before par/p récurrence",
      "C": "\\unsure{dém.|dem.}",
      "H": "dém.",
      "reading": "\\unsure{dém.|dem.}",
      "evidence": "The small raised stroke is crowded into the d/e group; its separation as an accent remains unresolved. The terminal abbreviation point is distinct. Both accented and unaccented forms are retained.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "12_dem_par_recurrence.png",
      "bbox": {
        "coordinates": [
          670,
          1335,
          832,
          1383
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R07"
    },
    {
      "id": "020A-20",
      "location": "Compressed word after dém./dem.",
      "C": "par",
      "H": "par",
      "reading": "\\unsure{par|p}",
      "evidence": "A long descending p-like stroke returns to an extended rightward head. The horizontal remainder supports compressed par; the single-letter abbreviation p remains a supported alternative. No endpoint point is supplied.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "12_dem_par_recurrence.png",
      "bbox": {
        "coordinates": [
          874,
          1338,
          956,
          1409
        ],
        "origin": "original full scan, upper left"
      },
      "qualification": "New local qualification with unchanged witness primary; not an actual C source doubt row."
    },
    {
      "id": "020A-21",
      "location": "Lemma Pi_I superscript",
      "C": "\\Pi_I^\\circ",
      "H": "\\Pi_I^0",
      "reading": "\\Pi_I^\\circ; local alternatives \\circ|0",
      "evidence": "Small rounded closed oval above/right of indexed Pi. Both circle and zero remain supported locally; only the primary is printed at this recurrence.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "13_lemma_formula_insertion.png",
      "bbox": {
        "coordinates": [
          1228,
          1558,
          1348,
          1645
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R01",
      "recurrence": "Third of three; source-row R01 counted once overall."
    },
    {
      "id": "020A-22",
      "location": "Overwritten union limit under K",
      "C": "\\deleted{\\unsure{I}}K",
      "H": "K",
      "reading": "\\deleted{I}K",
      "evidence": "An old straight vertical and left-reaching top/foot survive through the K strokes. The predecessor I is recovered from these strokes.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "13_lemma_formula_insertion.png",
      "bbox": {
        "coordinates": [
          1068,
          1738,
          1128,
          1806
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R08"
    },
    {
      "id": "020A-23",
      "location": "Brace over lemma union body",
      "C": "\\overbrace{\\Sigma_\\alpha^+\\cup E_\\alpha}^{\\inserted{\\widehat{\\Sigma}_\\alpha^+}}",
      "H": "\\note{au-dessus de ... il écrit \\widehat{\\Sigma}_\\alpha^+}",
      "reading": "A020-G05: complete body and hatted label with literal main brace run and closed left retrace",
      "evidence": "The left run has a closed oval/retrace before the central raised step; the right run curves to a short descending tip. Both the body and added hatted Sigma remain present once.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "13_lemma_formula_insertion.png",
      "bbox": {
        "coordinates": [
          1108,
          1619,
          1387,
          1748
        ],
        "origin": "original full scan, upper left"
      },
      "graphic_group": "A020-G05",
      "qualification": "H apparatus already supplies the hatted label; the H difference concerns the brace geometry, not a second omitted label."
    },
    {
      "id": "020A-24",
      "location": "Cancelled inserted non vide and curved guide",
      "C": "\\inserted{\\deleted{non vide}}",
      "H": "\\add{\\uncertain{non vide}}",
      "reading": "A020-G06: inserted, cancelled non vide, its crossing stroke and long curved guide; adjoining de I, occurs once",
      "evidence": "A dark oblique crossing passes through non vide. A distinct lower curved guide rises from the gap before de to the right of the inserted line. The complete word-bearing group also includes de I,; partie and et stay outside.",
      "confidence": "high",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "13_lemma_formula_insertion.png",
      "bbox": {
        "coordinates": [
          1142,
          1767,
          1392,
          1858
        ],
        "origin": "original full scan, upper left"
      },
      "graphic_group": "A020-G06",
      "lexical_diff_C": false,
      "qualification": "C already supplies the insertion and cancellation state. Its current change is the literal guide/crossing geometry. H has the insertion but leaves the words live."
    },
    {
      "id": "020A-25",
      "location": "Cancelled on a before Sigma membership expression",
      "C": "\\deleted{on a}",
      "H": "\\struck{\\ill{}}",
      "reading": "\\deleted{on a}",
      "evidence": "The initial round o/n body and separate a survive a single horizontal crossing.",
      "confidence": "high",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "14_membership_correction.png",
      "bbox": {
        "coordinates": [
          608,
          1981,
          761,
          2011
        ],
        "origin": "original full scan, upper left"
      },
      "H_placeholder_parent": "H-ILL-03",
      "H_placeholder_count": 1
    },
    {
      "id": "020A-26",
      "location": "Reworked membership/arrow group",
      "C": "\\deleted{\\unsure{\\Rightarrow}}\\in",
      "H": "\\in",
      "reading": "A020-G07; states \\deleted{\\Rightarrow}\\in | \\deleted{\\to}\\in | \\in",
      "evidence": "Outer curved membership-like body, a heavy middle run and a small right-returning arrow-like component are all present. They support the recorded predecessor/live alternatives, while their exact relation and cancellation target remain unsettled.",
      "confidence": "low",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "14_membership_correction.png",
      "bbox": {
        "coordinates": [
          940,
          1938,
          1004,
          2000
        ],
        "origin": "original full scan, upper left"
      },
      "C_source_doubt_row": "R09",
      "graphic_group": "A020-G07",
      "qualification": "Local unsure wraps the complete observed paths. Full-state alternatives are explicit in the TeX comment and invisible annotation; they do not print duplicate visible operators."
    },
    {
      "id": "020A-27",
      "location": "E inside X setminus E_alpha in membership expression",
      "C": "E_\\alpha",
      "H": "E_\\alpha",
      "reading": "{\\unsure{E|\\deleted{\\Sigma}E}}_\\alpha",
      "evidence": "Top rule, upright and middle arm support E. A slanted lower interior also supports an overwritten Sigma/E state; the source keeps E as primary and records that state alternative locally.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "14_membership_correction.png",
      "bbox": {
        "coordinates": [
          1188,
          1932,
          1268,
          1995
        ],
        "origin": "original full scan, upper left"
      },
      "qualification": "New state qualification with unchanged primary; independent of C source-row R09."
    },
    {
      "id": "020A-28",
      "location": "Scan label and archive numeral",
      "C": "\\scanpage{20}; % archive sheet number: 19",
      "H": "\\page{19}",
      "reading": "\\scanpage{20}; % archive sheet number: 19",
      "evidence": "Source administration only: packet maps our scan20 to H page19. A visible lower-left archive 19 is recorded as a comment, with undetermined hand.",
      "confidence": "high",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinates": [
          25,
          2304,
          80,
          2348
        ],
        "origin": "original full scan, upper left"
      },
      "source_only": true
    }
  ],
  "doubts": [
    {
      "location": "Opening Pi_I ring",
      "reading": "\\circ",
      "alternatives": [
        "0"
      ],
      "confidence": "medium",
      "reason": "Small closed ring does not settle the raised character interpretation.",
      "crop": "01_first_ring.png",
      "C_source_doubt_row": "R01",
      "printed": "first occurrence qualified"
    },
    {
      "location": "Opening Pi_J ring",
      "reading": "\\circ",
      "alternatives": [
        "0"
      ],
      "confidence": "medium",
      "reason": "Locally inspected closed ring retains zero alternative.",
      "crop": "02_second_ring.png",
      "C_source_doubt_row": "R01",
      "printed": "primary only under recurring-sign rule"
    },
    {
      "location": "Word before parmi",
      "reading": "clas.",
      "alternatives": [
        "deux."
      ],
      "confidence": "low",
      "reason": "Compressed low humps; separate endpoint point retained with both words.",
      "crop": "03_deux_clas.png",
      "C_source_doubt_row": "R02"
    },
    {
      "location": "Positive Sigma index in paired intersection",
      "reading": "j",
      "alternatives": [
        "\\deleted{J}i",
        "i"
      ],
      "confidence": "medium",
      "reason": "Descended stem and doubled low return allow both glyph and overwritten-state readings.",
      "crop": "04_paired_intersections.png",
      "C_source_doubt_row": "R03"
    },
    {
      "location": "Cancelled Sigma before U",
      "reading": "j",
      "alternatives": [
        "i"
      ],
      "confidence": "low",
      "reason": "Index crossed; full cancelled Sigma group kept.",
      "crop": "05_cancelled_sigma.png",
      "C_source_doubt_row": "R04"
    },
    {
      "location": "E index after voisinage",
      "reading": "i",
      "alternatives": [
        "j"
      ],
      "confidence": "medium",
      "reason": "Short hooked lowered mark remains compressed.",
      "crop": "06_voisinage_E.png",
      "C_source_doubt_row": "R05"
    },
    {
      "location": "Gray point after voisinage",
      "reading": "round graphical patch",
      "alternatives": [
        "punctuation role",
        "independent trace or surface mark"
      ],
      "confidence": "medium",
      "reason": "Shape visible; hand, role and surface origin unresolved.",
      "crop": "15_voisinage_detached_point.png",
      "graphic_group": "A020-G02"
    },
    {
      "location": "Cancelled count word",
      "reading": "tout",
      "alternatives": [
        "est"
      ],
      "confidence": "low",
      "reason": "Crossings cut internal letter bodies.",
      "crop": "09_cancelled_count_word.png",
      "C_source_doubt_row": "R06"
    },
    {
      "location": "Parenthetical adverb",
      "reading": "aussi",
      "alternatives": [
        "ainsi"
      ],
      "confidence": "low",
      "reason": "Internal letters run together.",
      "crop": "11_aussi_ainsi.png",
      "C_source_doubt_row": "R11"
    },
    {
      "location": "High point after la",
      "reading": "triangular graphical point",
      "alternatives": [
        "independent trace or surface mark",
        "unestablished written-mark role"
      ],
      "confidence": "medium",
      "reason": "Shape visible; no character role or hand established.",
      "crop": "11_aussi_ainsi.png",
      "graphic_group": "A020-G04"
    },
    {
      "location": "Abbreviation before par/p",
      "reading": "dém.",
      "alternatives": [
        "dem."
      ],
      "confidence": "medium",
      "reason": "Small upper stroke merges with the letter group.",
      "crop": "12_dem_par_recurrence.png",
      "C_source_doubt_row": "R07"
    },
    {
      "location": "Word after dém./dem.",
      "reading": "par",
      "alternatives": [
        "p"
      ],
      "confidence": "low",
      "reason": "Compressed rightward head allows the single-letter abbreviation.",
      "crop": "12_dem_par_recurrence.png"
    },
    {
      "location": "Lemma Pi_I ring",
      "reading": "\\circ",
      "alternatives": [
        "0"
      ],
      "confidence": "medium",
      "reason": "Locally inspected closed oval retains both interpretations.",
      "crop": "13_lemma_formula_insertion.png",
      "C_source_doubt_row": "R01",
      "printed": "primary only under recurring-sign rule"
    },
    {
      "location": "Membership/arrow group",
      "reading": "\\deleted{\\Rightarrow}\\in",
      "alternatives": [
        "\\deleted{\\to}\\in",
        "\\in"
      ],
      "confidence": "low",
      "reason": "Glyph presence, arrow interpretation and cancellation target remain jointly open.",
      "crop": "14_membership_correction.png",
      "C_source_doubt_row": "R09",
      "graphic_group": "A020-G07"
    },
    {
      "location": "E inside X setminus E_alpha",
      "reading": "E",
      "alternatives": [
        "\\deleted{\\Sigma}E"
      ],
      "confidence": "low",
      "reason": "Slanted lower interior allows an overwritten predecessor state.",
      "crop": "14_membership_correction.png"
    }
  ],
  "notes": {
    "page_content": "The author identifies the classes of Pi_I with the Pi_J classes distinct from U_{J,i}, together with the nonempty intersections, writes their count as (n-1)+2=n+1=card I+1, and states a lemma describing a class by X minus a union of Sigma_alpha^+ cup E_alpha. He writes pairwise disjointness of the hatted sets and the parenthetical equivalence with disjointness of the unhatted sets. These are attributed manuscript assertions; no proof check was performed.",
    "author_uncertainty": {
      "exact_words": [],
      "observation": "No explicit authorial uncertainty phrase was read. The editorial doubts above concern the ink. The inserted non vide is visibly cancelled."
    },
    "title_date_page_counts": {
      "heading": "Lemme, single underline",
      "date": null,
      "manuscript_page_number": null,
      "archive_number": "19",
      "our_scan": 20,
      "H_page": 19,
      "pages_read": 1
    },
    "mathematics_led_reading_decisions": "The malformed or reworked local signs were kept with their observed states. Later i indices did not resolve the positive Sigma index or cancelled Sigma. The written count and final parenthetical equivalence were transcribed without computation or proof validation.",
    "H_apparatus": "H notes about other pages and the location of the added hatted Sigma are apparatus. No other page was inspected. The three struck ill placeholders each receive one physical parent count.",
    "source_only_administration": "Scan20/H page19 mapping and the archive comment are administrative source choices with diff_C=false and diff_H=false. No manuscript page-number glyph is supplied.",
    "S_coverage": {
      "row_id": "SA01-K81-06",
      "item": "SA01-29",
      "recorded_where": "81/15-22",
      "recorded_author": "Claude Opus 5.5 at effort max, reader R4 (no scan viewed)",
      "stated_scope": "The row spans scans015–022 and supplies witness proposals only; each example must be matched locally.",
      "local_observations": "Two closure bars on Sigma_i^+ and the corrected Sigma_i^- were visually confirmed. Both are already in current C and H. The exact Sigma_1 and U_s example strings are not on this page. No bar was inferred from the broad range.",
      "diff_C": false,
      "diff_H": false,
      "ink_correction_count": 0
    },
    "processing": "All requested packet files, brief v18 and PREAMBLE were read. Whole page once for layout, supplied a once line by line, b once line by line; 14 planned crops and one new complete attachment target. All 18 image deliveries succeeded; zero repeated views and zero failed unseen deliveries. The last crop supplied complete neighbouring context for a newly noticed gray point; its E-index neighbour was outside that crop. No OCR, web research, rendering, compilation, installation or optional mathematical computation occurred.",
    "manual_graphics": "Seven graphical groups use declared local origins, fixed rectangles, base-west text nodes and consistent local pixel units. These are manual approximations, with no rendered or metric validation. The G07 phantom annotation is excluded from bounds by overlay, while its actual paths retain the local qualifier.",
    "report_silent_source_choices": [
      "clas. remains primary; the endpoint point is included with both word candidates",
      "sait is printed unqualified after its local resolution",
      "aussi remains primary with ainsi alternative",
      "achève uses a grave; récurrence uses an acute",
      "dém. retains dem. as an explicit alternative",
      "par retains p without a point as an explicit alternative",
      "later Pi rings print circle but retain local zero alternatives in report",
      "inside X setminus E_alpha, E remains primary with a Sigma/E predecessor-state alternative",
      "G07 prints the locally qualified observed graphic; complete state candidates are in its comment and invisible annotation",
      "the final parenthetical Sigmas carry plus signs and no hats",
      "the two detached small shapes remain graphical, with undetermined hands and roles"
    ]
  },
  "notation": [
    {
      "location": "three Pi occurrences",
      "sign": "small raised ring",
      "proposed_LaTeX": "first \\Pi_I^{\\unsure{\\circ|0}}, then \\Pi_J^\\circ and \\Pi_I^\\circ",
      "qualification": "All three local zero alternatives are in doubts and source-row R01."
    },
    {
      "location": "opening U and both paired U terms, later voisinage U",
      "sign": "hooked capital J, comma, dotted i",
      "proposed_LaTeX": "U_{J,i}"
    },
    {
      "location": "paired intersections",
      "sign": "Sigma upper head strokes",
      "proposed_LaTeX": "\\Sigma^+,\\Sigma^-",
      "qualification": "The supplied pair has one letter-head run per Sigma; the separate closure rules are in the later formulas."
    },
    {
      "location": "two non-emptiness formulas",
      "sign": "separate spanning upper rules",
      "proposed_LaTeX": "\\overline{\\Sigma_i^+},\\overline{\\deleted E\\Sigma_i^-}",
      "qualification": "Both existing C/H closure bars are locally confirmed."
    },
    {
      "location": "small Sigma i indices in negative pair and barred formulas",
      "sign": "point next to lower terminal hook",
      "proposed_LaTeX": "\\Sigma_i",
      "qualification": "Point and terminal hook transcribed together; no duplicate detached point supplied."
    },
    {
      "location": "count and final parenthesis",
      "sign": "nb",
      "proposed_LaTeX": "nb",
      "qualification": "Two occurrences, no expansion."
    },
    {
      "location": "count",
      "sign": "low linked card",
      "proposed_LaTeX": "\\operatorname{card} I+1"
    },
    {
      "location": "ce qui achève",
      "sign": "two short adjoining accent fragments",
      "proposed_LaTeX": "achève",
      "qualification": "Grave retained; this unchanged spelling is explicit in the audit."
    },
    {
      "location": "récurrence",
      "sign": "raised short acute stroke",
      "proposed_LaTeX": "récurrence",
      "qualification": "Acute retained independently of the unresolved dém./dem. accent."
    },
    {
      "location": "Lemme heading",
      "sign": "single underline",
      "proposed_LaTeX": "\\uline{Lemme}"
    },
    {
      "location": "lemma formula annotation and final hatted pair",
      "sign": "three roofs on Sigma",
      "proposed_LaTeX": "\\widehat{\\Sigma}_\\alpha^+,\\widehat{\\Sigma}_\\beta^+",
      "qualification": "Three local hats total: one added label and two final hatted terms; the last parenthetical pair remains unhatted."
    },
    {
      "location": "last parenthesis",
      "sign": "two-ended, two-line arrow",
      "proposed_LaTeX": "\\Longleftrightarrow"
    },
    {
      "location": "margin and all emptiness statements",
      "sign": "slashed small oval",
      "proposed_LaTeX": "\\varnothing"
    },
    {
      "location": "archive foot",
      "sign": "19",
      "proposed_LaTeX": "% archive sheet number: 19",
      "qualification": "Undetermined hand; comment only."
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The exact count unit is clarified here as 11 actual C source rows and 13 local subloci, because R01 covers three rings.",
    "A qualified relation graphic carries full-state alternatives in its source comment and invisible annotation so its observed strokes occur once; this representational choice is explicit for consolidation.",
    "The new gray point required one complete neighbouring-word attachment target after discovery at crop06; no decided E-index target was reopened."
  ]
}

## Reader B

\scanpage{20}
Ainsi les classes de $\Pi_I^{\unsure{\circ|0}}$ sont les classes de $\Pi_J^\circ$ distinctes de $\deleted{\Pi}U_{J,i}$, et de plus les \unsure{clas.|deux.} parmi
\[
U_{J,i}\cap\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\quad U_{J,i}\cap\Sigma_i^-
\]
qui sont non vides. Or les deux classes en question sont non vides, car
% B_G01: cancelled Sigma and its two visible crossing runs. Observed locus (320,810,403,900).
% Source origin (315,803); x right, y down; 0.25 pt per source pixel. Baseline y=76.
% The visible node occurs once; its phantom carries the deletion state without a generic extra rule.
\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,76)}]
\path[use as bounding box] (0,0) rectangle (95,100);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,76) {\rlap{$\unsure{\Sigma_j|\Sigma_i}$}\phantom{\deleted{$\unsure{\Sigma_j|\Sigma_i}$}}};
\draw[line width=0.45pt,line cap=round] (10,73) .. controls (20,54) and (30,31) .. (40,12);
\draw[line width=0.45pt,line cap=round] (45,73) .. controls (43,80) and (49,82) .. (54,76) -- (69,35);
\end{tikzpicture}
$U_{J,i}$ est un voisinage de $\deleted{\Sigma}E_{\unsure{i|j}}$, et
\[
\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
\]
On sait donc que le nb des classes est en \deleted{\unsure{tout|est}} $(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève \unsure{aussi|ainsi}
% B_G02: complete word-bearing group la and one qualified detached point above/right.
% Origin (500,1347), 0.25 pt per source pixel, baseline y=49. Observed point locus (566,1363,575,1373).
% Inner graphic origin is explicitly translated by (66,18); base-west anchor and baseline (0,0) fix its placement.
\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline=(Bla.base)]
\path[use as bounding box] (0,0) rectangle (88,62);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (Bla) at (0,49) {la};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (66,18) {\unsure{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,0)}]
\path[use as bounding box] (0,0) rectangle (7,8);
\fill (2,0) -- (5,4) -- (4,7) -- (1,6) -- cycle;
\end{tikzpicture}}};
\end{tikzpicture}
\unsure{dèm.|dém.|dem.} par récurrence sur le nb des classes).

\uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
% B_G03: union, complete parenthesized expression, overwritten limit, raised hatted Sigma, and literal brace.
% Origin (1010,1600), 0.25 pt per source pixel, baseline y=140; fixed drawing rectangle (0,15)-(390,200).
% Pi above and X setminus to the left are outside this group. No generic bigcup or overbrace is also drawn.
$X\setminus\text{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,140)}]
\path[use as bounding box] (0,15) rectangle (390,200);
% U01 body; U02 upper-right loop; U03 pale lower retrace.
\draw[line width=0.95pt,line cap=round] (17,90) .. controls (17,122) and (24,140) .. (45,142) .. controls (63,142) and (72,133) .. (71,115) -- (68,87);
\draw[line width=0.55pt,line cap=round] (68,87) .. controls (66,77) and (63,81) .. (64,89) .. controls (65,96) and (68,99) .. (68,104);
\draw[black!55,line width=0.45pt,line cap=round] (19,114) .. controls (23,140) and (51,150) .. (65,133);
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small] at (0,190) {$\alpha\in\unsure{\deleted{I}K|K}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small] at (91,140) {$(\Sigma_\alpha^+\cup E_\alpha)$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\scriptsize] at (184,58) {$\inserted{\widehat{\Sigma}_\alpha^+}$};
% BR01 main run and central turn; BR02 closed left loop; BR03 left retrace.
\draw[line width=0.65pt,line cap=round] (108,79) .. controls (132,75) and (151,71) .. (180,74) .. controls (193,75) and (204,70) .. (217,72) -- (220,62) .. controls (234,70) and (256,68) .. (287,64) .. controls (307,60) and (326,59) .. (339,62) .. controls (344,63) and (345,66) .. (345,69);
\draw[line width=0.55pt,line cap=round] (132,76) .. controls (141,68) and (160,69) .. (164,74) .. controls (153,81) and (142,82) .. (132,76);
\draw[line width=0.85pt,line cap=round] (120,80) .. controls (145,74) and (178,73) .. (210,74);
\end{tikzpicture}}$
où $K$ est une
% B_G04 contains exactly partie, the inserted/deleted non vide, and de I, et.
% Source origin (997,1750), 0.25 pt per source pixel, baseline y=110. Fixed rectangle (0,0)-(530,160).
% NV01 is the rising cancellation run with its right return. NV02 is the separate curved insertion guide.
\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,110)}]
\path[use as bounding box] (0,0) rectangle (530,160);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,115) {partie};
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small,rotate=8] at (157,45) {\inserted{\rlap{non vide}\phantom{\deleted{non vide}}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (200,89) {de $I$, et};
\draw[line width=0.55pt,line cap=round] (154,53) .. controls (203,44) and (282,30) .. (331,24) .. controls (331,31) and (325,37) .. (315,43);
\draw[line width=0.45pt,line cap=round] (182,94) .. controls (172,61) and (272,47) .. (339,40) .. controls (346,39) and (351,39) .. (355,43);
\end{tikzpicture}
% slanted; the two written conditions have no punctuation between them.
\reversemarginpar\margin{\begin{tikzpicture}\node[rotate=19,anchor=base west,inner sep=0pt,outer sep=0pt] {\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}};\end{tikzpicture}}\normalmarginpar
$\forall\alpha\in K$, \deleted{on a} $\Sigma_\alpha^+
% B_G05 literal reworked relation, followed inside the qualifier by its supported complete-state interpretations.
% Origin (943,1947), 0.25 pt per source pixel, baseline y=43; observed locus (944,1949,999,2004).
% M01 curved body, M02 middle shaft, M03 thin right head. No additional unqualified membership or arrow is drawn.
\mathrel{\unsure{\text{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,43)}]
\path[use as bounding box] (0,0) rectangle (62,66);
\draw[line width=0.70pt,line cap=round] (45,11) .. controls (35,-1) and (16,17) .. (7,32) .. controls (1,43) and (5,51) .. (15,55) .. controls (23,58) and (32,56) .. (39,51);
\draw[line width=0.75pt,line cap=round] (4,40) -- (43,32);
\draw[line width=0.40pt,line cap=round] (35,24) .. controls (38,16) and (51,29) .. (54,36) .. controls (56,34) and (54,20) .. (48,19);
\end{tikzpicture}}|\deleted{\Rightarrow}\in|\deleted{\to}\in|\in}}
\pi_0(X\setminus E_\alpha)$, tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
% archive sheet number: 19



{
  "differences": [
    {
      "id": "B020-D01",
      "location": "Opening line, Pi-I superscript",
      "C": "\\Pi_I^{\\unsure{\\circ|0}}",
      "H": "\\Pi_I^0",
      "reading": "\\Pi_I^{\\unsure{\\circ|0}}",
      "evidence": "Small closed rounded loop above the separately footed I; its strokes retain both a circle and a small zero. H zero survives as an alternative.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "01_opening_ring.png",
      "bbox": [
        1065,
        65,
        1260,
        180
      ],
      "C_source_row": "R01",
      "sublocus": "R01a",
      "qualification": "Qualified primary difference from H, not a conclusive exclusion of H zero."
    },
    {
      "id": "B020-D02",
      "location": "Second line, Pi-J superscript",
      "C": "\\Pi_J^\\circ",
      "H": "\\Pi_J^0",
      "reading": "\\Pi_J^\\circ; local alternatives \\circ|0",
      "evidence": "Closed small upper loop, locally inspected separately. First-occurrence convention prints the circle primary here without a second qualifier.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "02_second_ring.png",
      "bbox": [
        630,
        165,
        815,
        285
      ],
      "C_source_row": "R01",
      "sublocus": "R01b",
      "qualification": "Zero remains supported here despite the unmarked recurring primary in reading.tex."
    },
    {
      "id": "B020-D03",
      "location": "Second line, U after distinctes de",
      "C": "\\deleted{\\Pi}U_{J,i}",
      "H": "U_{J,i}",
      "reading": "\\deleted{\\Pi}U_{J,i}",
      "evidence": "Horizontal Pi head and two shorter upright remnants remain beneath the taller curved U; both lowered J and dotted i and their separator are visible.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "03_opening_overwritten_U.png",
      "bbox": [
        1270,
        145,
        1545,
        300
      ]
    },
    {
      "id": "B020-D04",
      "location": "Third line, word after les",
      "C": "\\unsure{clas.|deux}",
      "H": "deux",
      "reading": "\\unsure{clas.|deux.}",
      "evidence": "Small open first curl followed by a tall loop and flattened low continuation; clas. remains first but the joined strokes retain deux. Endpoint point is separately recorded in D05.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "04_les_word_parmi.png",
      "bbox": [
        735,
        275,
        1270,
        382
      ],
      "C_source_row": "R02",
      "qualification": "H deux survives as a lexical alternative; the terminal point is present for either candidate."
    },
    {
      "id": "B020-D05",
      "location": "Third line, point after doubtful word",
      "C": "clas. (point in first candidate); deux (no point in alternative)",
      "H": "deux (no point)",
      "reading": ".",
      "evidence": "A discrete dark point stands after the final downward turn and before the large gap preceding parmi. Both complete candidates in reading.tex include it.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "04_les_word_parmi.png",
      "bbox": [
        735,
        275,
        1270,
        382
      ],
      "physical_scope": "The endpoint point only; D04 counts only the word reading."
    },
    {
      "id": "B020-D06",
      "location": "First positive paired intersection, Sigma index",
      "C": "\\Sigma_{\\unsure{\\deleted{J}i|j|i}}^+",
      "H": "\\Sigma_i^+",
      "reading": "\\Sigma_{\\unsure{\\deleted{J}i|j|i}}^+",
      "evidence": "A short dotted right return lies beside a much deeper descending stem and left-returning foot. The shared junction does not settle overwritten J+i, j, or i as complete states.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "05_first_intersection_index.png",
      "bbox": [
        575,
        365,
        990,
        520
      ],
      "C_source_row": "R03",
      "qualification": "H simple i survives as an alternative; no chronology is inferred."
    },
    {
      "id": "B020-D07",
      "location": "Cancelled Sigma group before U est un voisinage",
      "C": "\\deleted{\\unsure{\\Sigma_i|\\Sigma_j}}",
      "H": "\\struck{\\ill{}}",
      "reading": "\\deleted{\\unsure{\\Sigma_j|\\Sigma_i}}; literal B_G01 crossing paths",
      "evidence": "The cancelled Sigma is recoverable; the small index has a substantial descending return, favoring j, but crossing strokes leave i supported. Two separately visible sloping cancellation runs are preserved by G01, with a small hooked return in the second path.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "06_cancelled_sigma_before_U.png",
      "bbox": [
        280,
        757,
        615,
        915
      ],
      "C_source_row": "R04",
      "physical_scope": "One cancelled glyph/index/state cluster and one H ill placeholder; geometry is included in this parent count.",
      "shape_confidence": "high for the two crossing runs; low for index identification",
      "components": [
        "G01.C01",
        "G01.C02"
      ]
    },
    {
      "id": "B020-D08",
      "location": "Index of E after voisinage de",
      "C": "E_{\\unsure{i|j}}",
      "H": "E_i",
      "reading": "E_{\\unsure{i|j}}",
      "evidence": "The short index is a hooked undotted stroke. Its limited downward extent favors i, while j remains possible. The separate lower comma is not used as its dot or tail.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "07_voisinage_E.png",
      "bbox": [
        1190,
        740,
        1555,
        890
      ],
      "C_source_row": "R05"
    },
    {
      "id": "B020-D09",
      "location": "Base E after voisinage de",
      "C": "\\deleted{\\Sigma}E",
      "H": "E",
      "reading": "\\deleted{\\Sigma}E",
      "evidence": "Thin diagonal Sigma returns remain inside the heavier vertical and horizontal E strokes.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "07_voisinage_E.png",
      "bbox": [
        1190,
        740,
        1555,
        890
      ]
    },
    {
      "id": "B020-D10",
      "location": "After E index before et",
      "C": "E_{\\unsure{i|j}}, et",
      "H": "E_i et",
      "reading": "E_{\\unsure{i|j}}, et",
      "evidence": "A distinct curved mark falls below the index and turns left at its lower end.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "07_voisinage_E.png",
      "bbox": [
        1190,
        740,
        1555,
        890
      ]
    },
    {
      "id": "B020-D11",
      "location": "First non-emptiness intersection, E base",
      "C": "\\deleted{\\Sigma}E_i",
      "H": "E_i",
      "reading": "\\deleted{\\Sigma}E_i",
      "evidence": "Angular thinner return survives between the thick E bars. The lowered hook and point are retained as the written i.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "08_barred_intersections.png",
      "bbox": [
        470,
        944,
        533,
        1004
      ]
    },
    {
      "id": "B020-D12",
      "location": "Second non-emptiness intersection, barred Sigma base",
      "C": "\\overline{\\deleted{E}\\Sigma_i^-}",
      "H": "\\overline{\\Sigma_i^-}",
      "reading": "\\overline{\\deleted{E}\\Sigma_i^-}",
      "evidence": "A left upright and short middle-bar remnant occur beneath the diagonal Sigma strokes. The independent upper closure rule and minus are already present in C and H.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "08_barred_intersections.png",
      "bbox": [
        744,
        908,
        861,
        996
      ]
    },
    {
      "id": "B020-D13",
      "location": "Second non-emptiness intersection, E base",
      "C": "\\deleted{\\Sigma}E_i",
      "H": "E_i",
      "reading": "\\deleted{\\Sigma}E_i",
      "evidence": "The small E retains an interior diagonal return of Sigma beneath its three heavier arms.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "08_barred_intersections.png",
      "bbox": [
        911,
        922,
        978,
        989
      ]
    },
    {
      "id": "B020-D14",
      "location": "On ... donc above count",
      "C": "\\unsure{voit|sait}",
      "H": "voit",
      "reading": "sait",
      "evidence": "The first stroke curls back into a low s; it is followed by a small a bowl, the raised point, and the tall terminal t. The crop supports sait.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "09_On_verb_donc.png",
      "bbox": [
        1190,
        875,
        1650,
        995
      ],
      "C_source_row": "R10"
    },
    {
      "id": "B020-D15",
      "location": "Live word between est and cancelled word before count",
      "C": "est en",
      "H": "est \\struck{\\ill{}}",
      "reading": "est en",
      "evidence": "The low open e/u-shaped entry and following n run are visibly separated from the cancelled word at the right; the live en has no crossing stroke.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "10_en_cancelled_word.png",
      "bbox": [
        1317,
        1034,
        1427,
        1100
      ],
      "physical_scope": "Live en only; the following one H ill placeholder is counted in D16."
    },
    {
      "id": "B020-D16",
      "location": "Cancelled word at right before count",
      "C": "\\deleted{\\unsure{tout|est}}",
      "H": "\\struck{\\ill{}}",
      "reading": "\\deleted{\\unsure{tout|est}}",
      "evidence": "A tall first rise and reduced low middle remain under the long diagonal. The crossing masks the letter sequence enough to retain both tout and est.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "10_en_cancelled_word.png",
      "bbox": [
        945,
        1010,
        1635,
        1140
      ],
      "C_source_row": "R06",
      "physical_scope": "One recovered qualified cancelled word, one H ill placeholder."
    },
    {
      "id": "B020-D17",
      "location": "Parenthesis, adverb before la",
      "C": "\\unsure{aussi|ainsi}",
      "H": "aussi",
      "reading": "\\unsure{aussi|ainsi}",
      "evidence": "The initial point/low run and joined middle reduce the u/n/s distinctions; the terminal i has a separate point. Both adverbs remain supported.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "12_aussi_dem.png",
      "bbox": [
        270,
        1290,
        975,
        1445
      ],
      "C_source_row": "R11"
    },
    {
      "id": "B020-D18",
      "location": "Above/right of la, in parenthesis",
      "C": "No separate component",
      "H": "No separate component",
      "reading": "One locally qualified tapered point in B_G02",
      "evidence": "A small discrete dark tapered mark lies around full-scan (570,1367), above and to the right of the la body. It is preserved once graphically. Its attachment to the adjoining word, character, role, hand and surface origin remain unsettled.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "12_aussi_dem.png",
      "bbox": [
        566,
        1363,
        575,
        1373
      ],
      "shape_confidence": "high for presence and small tapered outline",
      "role_confidence": "undetermined",
      "component": "G02.P01",
      "source_boundaries": "B_G02 contains la once and the qualified point once; no punctuation value is supplied."
    },
    {
      "id": "B020-D19",
      "location": "Parenthesis, abbreviated proof word",
      "C": "\\unsure{dém.|dem.}",
      "H": "dém.",
      "reading": "\\unsure{dèm.|dém.|dem.}",
      "evidence": "The detached short upper stroke leans down-right, favoring a grave accent. Its near-upright shape and very close approach to the small body do not settle direction/presence completely; acute and unaccented candidates remain explicit. The endpoint point is clear.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "12_aussi_dem.png",
      "bbox": [
        270,
        1290,
        975,
        1445
      ],
      "C_source_row": "R07",
      "qualification": "H dém. survives as an alternative; this is a qualified primary accent change."
    },
    {
      "id": "B020-D20",
      "location": "Lemma opening, Pi-I superscript",
      "C": "\\Pi_I^\\circ",
      "H": "\\Pi_I^0",
      "reading": "\\Pi_I^\\circ; local alternatives \\circ|0",
      "evidence": "Small closed oval with a short entry at upper left. This third local occurrence retains circle/zero uncertainty; only the first occurrence has a printed qualifier.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "13_lemma_formula_insert.png",
      "bbox": [
        1222,
        1558,
        1363,
        1642
      ],
      "C_source_row": "R01",
      "sublocus": "R01c",
      "qualification": "H zero survives locally as an alternative."
    },
    {
      "id": "B020-D21",
      "location": "Lemma, large indexed union sign",
      "C": "\\bigcup",
      "H": "\\bigcup",
      "reading": "Literal B_G03 U01/U02/U03",
      "evidence": "The large curved body has a narrow loop at its upper-right entrance and a paler lower retracing curve. All three runs are represented literally; the interpretation as the indexed union is retained.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "13_lemma_formula_insert.png",
      "bbox": [
        1017,
        1675,
        1092,
        1752
      ],
      "components": [
        "G03.U01",
        "G03.U02",
        "G03.U03"
      ],
      "source_boundaries": "Only the union sign paths; X setminus is outside G03, and the formula/limit nodes are separately identified."
    },
    {
      "id": "B020-D22",
      "location": "Lemma, overwritten union limit",
      "C": "\\alpha\\in\\deleted{\\unsure{I}}K",
      "H": "\\alpha\\in K",
      "reading": "\\alpha\\in\\unsure{\\deleted{I}K|K}",
      "evidence": "An I-like vertical with top and foot is visible within the heavier K. Its relation to the K body remains open: overwritten I+K and one elaborately drawn K are explicit complete states.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "13_lemma_formula_insert.png",
      "bbox": [
        1004,
        1747,
        1125,
        1805
      ],
      "C_source_row": "R08",
      "qualification": "C implicit absence alternative is made explicit; this wrapper/state clarification alone creates no C count. H K survives as an alternative."
    },
    {
      "id": "B020-D23",
      "location": "Lemma, brace above parenthesized union term",
      "C": "\\overbrace{\\Sigma_\\alpha^+\\cup E_\\alpha}^{\\inserted{\\widehat{\\Sigma}_\\alpha^+}}",
      "H": "\\note{au-dessus de ... il écrit \\widehat{\\Sigma}_\\alpha^+}",
      "reading": "B_G03 BR01/BR02/BR03 beside unchanged formula and inserted hatted Sigma",
      "evidence": "The brace has a main run with a sharp central upturn, a closed narrow loop within the left arm, and a thicker retraced left run. The raised hat/Sigma label is already present in C and H apparatus.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "13_lemma_formula_insert.png",
      "bbox": [
        1110,
        1654,
        1362,
        1691
      ],
      "components": [
        "G03.BR01",
        "G03.BR02",
        "G03.BR03"
      ],
      "source_boundaries": "G03 contains one body term and one raised hatted label; no generic overbrace is also drawn."
    },
    {
      "id": "B020-D24",
      "location": "Inserted non vide above de I",
      "C": "\\inserted{\\deleted{non vide}}",
      "H": "\\add{\\uncertain{non vide}}",
      "reading": "Readable inserted non vide, cancelled; literal B_G04 NV01",
      "evidence": "A rising long stroke crosses the inserted words and turns back at the right. The words themselves remain readable. H carries insertion but prints them live. C already has their cancellation state; the explicit rising run and right return replace its generic strike geometry.",
      "confidence": "high",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "13_lemma_formula_insert.png",
      "bbox": [
        1145,
        1767,
        1335,
        1813
      ],
      "components": [
        "G04.NV01"
      ],
      "C_change_scope": "Geometry only: wording, insertion and cancellation state retained.",
      "H_change_scope": "One physical inserted/deleted phrase cluster, including its cancellation geometry."
    },
    {
      "id": "B020-D25",
      "location": "Curved guide from gap before de I to inserted phrase",
      "C": "Insertion macro only; no guide path",
      "H": "Insertion macro only; no guide path",
      "reading": "Literal B_G04 NV02",
      "evidence": "The separate long curve starts low beside the gap after partie, rises rightward under the inserted phrase, and ends with a short downward return.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "13_lemma_formula_insert.png",
      "bbox": [
        1171,
        1784,
        1362,
        1854
      ],
      "components": [
        "G04.NV02"
      ],
      "source_boundaries": "B_G04 contains partie, inserted/deleted non vide, and de I, et exactly once; une remains outside."
    },
    {
      "id": "B020-D26",
      "location": "After forall alpha in K, cancelled prose",
      "C": "\\deleted{on a}",
      "H": "\\struck{\\ill{}}",
      "reading": "\\deleted{on a}",
      "evidence": "An o loop and joined n remain at the left of the crossing rule; a small separate a loop occurs farther right.",
      "confidence": "high",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "14_membership_correction.png",
      "bbox": [
        606,
        1975,
        766,
        2010
      ],
      "physical_scope": "One H ill placeholder, one cancelled phrase."
    },
    {
      "id": "B020-D27",
      "location": "Between positive Sigma and pi_0 in lemma",
      "C": "\\deleted{\\unsure{\\Rightarrow}}\\in",
      "H": "\\in",
      "reading": "Qualified literal B_G05; supported complete states deleted Rightarrow+in / deleted to+in / in with retracing",
      "evidence": "The curved left body and a dark middle shaft coexist with a thinner right-pointing head. One recovered shaft is visible; the full predecessor glyph and cancellation target remain open. The graphic is preserved with all three state interpretations inside the local qualifier.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "14_membership_correction.png",
      "bbox": [
        944,
        1949,
        999,
        2004
      ],
      "C_source_row": "R09",
      "components": [
        "G05.M01",
        "G05.M02",
        "G05.M03"
      ],
      "shape_confidence": "high for the three literal runs",
      "qualification": "C original Rightarrow candidate and H in candidate both remain supported. No chronology or mathematical repair is asserted.",
      "source_boundaries": "G05 owns the whole local relation; no unqualified second arrow or membership sign appears beside it."
    }
  ],
  "doubts": [
    {
      "id": "B020-D01",
      "location": "Opening line, Pi-I superscript",
      "reading": "\\Pi_I^{\\unsure{\\circ|0}}",
      "alternatives": [
        "\\circ",
        "0"
      ],
      "confidence": "medium",
      "reason": "Small closed rounded loop above the separately footed I; its strokes retain both a circle and a small zero. H zero survives as an alternative.",
      "crop": "01_opening_ring.png",
      "source_row": "R01",
      "printed_qualifier": true
    },
    {
      "id": "B020-D02",
      "location": "Second line, Pi-J superscript",
      "reading": "\\Pi_J^\\circ; local alternatives \\circ|0",
      "alternatives": [
        "\\circ",
        "0"
      ],
      "confidence": "medium",
      "reason": "Closed small upper loop, locally inspected separately. First-occurrence convention prints the circle primary here without a second qualifier.",
      "crop": "02_second_ring.png",
      "source_row": "R01",
      "printed_qualifier": false
    },
    {
      "id": "B020-D04",
      "location": "Third line, word after les",
      "reading": "\\unsure{clas.|deux.}",
      "alternatives": [
        "clas.",
        "deux."
      ],
      "confidence": "medium",
      "reason": "Small open first curl followed by a tall loop and flattened low continuation; clas. remains first but the joined strokes retain deux. Endpoint point is separately recorded in D05.",
      "crop": "04_les_word_parmi.png",
      "source_row": "R02",
      "printed_qualifier": true
    },
    {
      "id": "B020-D06",
      "location": "First positive paired intersection, Sigma index",
      "reading": "\\Sigma_{\\unsure{\\deleted{J}i|j|i}}^+",
      "alternatives": [
        "\\deleted{J}i",
        "j",
        "i"
      ],
      "confidence": "low",
      "reason": "A short dotted right return lies beside a much deeper descending stem and left-returning foot. The shared junction does not settle overwritten J+i, j, or i as complete states.",
      "crop": "05_first_intersection_index.png",
      "source_row": "R03",
      "printed_qualifier": true
    },
    {
      "id": "B020-D07",
      "location": "Cancelled Sigma group before U est un voisinage",
      "reading": "\\deleted{\\unsure{\\Sigma_j|\\Sigma_i}}; literal B_G01 crossing paths",
      "alternatives": [
        "\\Sigma_j",
        "\\Sigma_i"
      ],
      "confidence": "low",
      "reason": "The cancelled Sigma is recoverable; the small index has a substantial descending return, favoring j, but crossing strokes leave i supported. Two separately visible sloping cancellation runs are preserved by G01, with a small hooked return in the second path.",
      "crop": "06_cancelled_sigma_before_U.png",
      "source_row": "R04",
      "printed_qualifier": true
    },
    {
      "id": "B020-D08",
      "location": "Index of E after voisinage de",
      "reading": "E_{\\unsure{i|j}}",
      "alternatives": [
        "i",
        "j"
      ],
      "confidence": "medium",
      "reason": "The short index is a hooked undotted stroke. Its limited downward extent favors i, while j remains possible. The separate lower comma is not used as its dot or tail.",
      "crop": "07_voisinage_E.png",
      "source_row": "R05",
      "printed_qualifier": true
    },
    {
      "id": "B020-D16",
      "location": "Cancelled word at right before count",
      "reading": "\\deleted{\\unsure{tout|est}}",
      "alternatives": [
        "tout",
        "est"
      ],
      "confidence": "low",
      "reason": "A tall first rise and reduced low middle remain under the long diagonal. The crossing masks the letter sequence enough to retain both tout and est.",
      "crop": "10_en_cancelled_word.png",
      "source_row": "R06",
      "printed_qualifier": true
    },
    {
      "id": "B020-D17",
      "location": "Parenthesis, adverb before la",
      "reading": "\\unsure{aussi|ainsi}",
      "alternatives": [
        "aussi",
        "ainsi"
      ],
      "confidence": "medium",
      "reason": "The initial point/low run and joined middle reduce the u/n/s distinctions; the terminal i has a separate point. Both adverbs remain supported.",
      "crop": "12_aussi_dem.png",
      "source_row": "R11",
      "printed_qualifier": true
    },
    {
      "id": "B020-D18",
      "location": "Above/right of la, in parenthesis",
      "reading": "One locally qualified tapered point in B_G02",
      "alternatives": [
        "Tapered dark point; attachment to la or detached mark unresolved; no character assigned"
      ],
      "confidence": "medium",
      "reason": "A small discrete dark tapered mark lies around full-scan (570,1367), above and to the right of the la body. It is preserved once graphically. Its attachment to the adjoining word, character, role, hand and surface origin remain unsettled.",
      "crop": "12_aussi_dem.png",
      "source_row": null,
      "printed_qualifier": true
    },
    {
      "id": "B020-D19",
      "location": "Parenthesis, abbreviated proof word",
      "reading": "\\unsure{dèm.|dém.|dem.}",
      "alternatives": [
        "dèm.",
        "dém.",
        "dem."
      ],
      "confidence": "medium",
      "reason": "The detached short upper stroke leans down-right, favoring a grave accent. Its near-upright shape and very close approach to the small body do not settle direction/presence completely; acute and unaccented candidates remain explicit. The endpoint point is clear.",
      "crop": "12_aussi_dem.png",
      "source_row": "R07",
      "printed_qualifier": true
    },
    {
      "id": "B020-D20",
      "location": "Lemma opening, Pi-I superscript",
      "reading": "\\Pi_I^\\circ; local alternatives \\circ|0",
      "alternatives": [
        "\\circ",
        "0"
      ],
      "confidence": "medium",
      "reason": "Small closed oval with a short entry at upper left. This third local occurrence retains circle/zero uncertainty; only the first occurrence has a printed qualifier.",
      "crop": "13_lemma_formula_insert.png",
      "source_row": "R01",
      "printed_qualifier": false
    },
    {
      "id": "B020-D22",
      "location": "Lemma, overwritten union limit",
      "reading": "\\alpha\\in\\unsure{\\deleted{I}K|K}",
      "alternatives": [
        "\\deleted{I}K",
        "K"
      ],
      "confidence": "medium",
      "reason": "An I-like vertical with top and foot is visible within the heavier K. Its relation to the K body remains open: overwritten I+K and one elaborately drawn K are explicit complete states.",
      "crop": "13_lemma_formula_insert.png",
      "source_row": "R08",
      "printed_qualifier": true
    },
    {
      "id": "B020-D27",
      "location": "Between positive Sigma and pi_0 in lemma",
      "reading": "Qualified literal B_G05; supported complete states deleted Rightarrow+in / deleted to+in / in with retracing",
      "alternatives": [
        "\\deleted{\\Rightarrow}\\in",
        "\\deleted{\\to}\\in",
        "\\in (with retracing)"
      ],
      "confidence": "low",
      "reason": "The curved left body and a dark middle shaft coexist with a thinner right-pointing head. One recovered shaft is visible; the full predecessor glyph and cancellation target remain open. The graphic is preserved with all three state interpretations inside the local qualifier.",
      "crop": "14_membership_correction.png",
      "source_row": "R09",
      "printed_qualifier": true
    }
  ],
  "notes": {
    "page_content": "The author continues a class-count argument, then writes an underlined Lemme giving a form for classes of Pi_I with the upper round mark. The author writes the count (n-1)+2=n+1=card I+1 and the parenthetical statement that this also completes the induction on the number of classes. The lemma names complements of indexed unions of Sigma_alpha-plus cup E_alpha, the membership condition in pi_0(X setminus E_alpha), and pairwise disjointness of the hatted sets. The final written double arrow relates the hatted and un-hatted disjointness expressions. These are attributed manuscript assertions; this reading establishes no proof of them.",
    "author_uncertainty": {
      "exact_words": [],
      "note": "No explicit authorial question or uncertainty wording was recovered. The manuscript has corrections and a crossed inserted non vide; editorial doubtful readings are kept separately."
    },
    "title_date_page_counts": {
      "heading": "Lemme, single underline",
      "date": null,
      "own_page_number": null,
      "archive_number": "19",
      "scan_number": 20,
      "H_page_number": 19
    },
    "mathematics_led_reading_decisions": "The repeated indexing and formulas were followed to locate small signs and correction clusters. No expected identity or theorem was used to replace a visible sign. No mathematical calculation, proof check, OCR or external research was performed.",
    "processing_note": "Start UTC was recorded before packet reading. All requested text files were read. A truncated initial combined text delivery affected notation.md; its complete standalone text was then read successfully. Whole image, each supplied half, and each of fourteen crops were delivered successfully once. There were no failed unseen image deliveries or repeated image views. A root checkpoint hold was observed after the completed visual phase; this same context resumed without reopening an image. The first source-audit attempt stopped on an exact-comment-marker assumption in its excerpt extractor; the extractor was corrected and source-only checks then passed. No image was reopened for this administrative fix.",
    "image_audit_file": "image_audit.json",
    "source_choices": [
      {
        "location": "Start/foot",
        "selected": "\\scanpage{20}; % archive sheet number: 19",
        "evidence": "Packet scan020/H page19 mapping plus visible lower-left archive19. No manuscript page marker or cotefile is supplied.",
        "source_only": true,
        "diff_C": false,
        "diff_H": false
      },
      {
        "location": "Opening/paired line",
        "selected": "Ainsi; classes; distinctes; et de plus les; parmi; separate comma between the two intersections; second Sigma_i-minus",
        "evidence": "Complete half-a reading; no inferred closure bar on either first pair member."
      },
      {
        "location": "Upper prose",
        "selected": "qui sont non vides. Or les deux classes en question sont non vides, car",
        "evidence": "Half a, lines beneath the pair; full stop after first vides and comma after second vides retained."
      },
      {
        "location": "Non-emptiness display",
        "selected": "First comma and second full stop; both ne signs; slashed empty-set shapes",
        "evidence": "Half a and complete crop08. No additional separate mark is supplied for the letter-index joins."
      },
      {
        "location": "Count",
        "selected": "(n-1)+2=n+1=\\operatorname{card} I+1",
        "evidence": "Half b, upper count line. Transcribed without arithmetic check or proof inference."
      },
      {
        "location": "Parenthesis",
        "selected": "ce qui achève",
        "evidence": "Crop11: detached short downward-right upper accent group over the e; full q descender included. Unchanged C/H spelling is an explicit selection."
      },
      {
        "location": "Parenthesis",
        "selected": "par récurrence sur le nb des classes).",
        "evidence": "Half b and crop12 context: compact par group, acute at récurrence, nb, closing parenthesis and point. No abbreviation expansion is inferred beyond the selected visible compact par reading."
      },
      {
        "location": "Lemma prose",
        "selected": "Lemme (single underline), Toute classe, de la forme, où K est une partie de I, et, tels que, on ait",
        "evidence": "Half b and crop13. où carries the separately visible upper slant; all these words occur once in the complete source, including words held inside G04."
      },
      {
        "location": "Final two lines",
        "selected": "\\forall\\alpha,\\beta\\in K,\\quad\\alpha\\ne\\beta,\\quad\\widehat{\\Sigma}_\\alpha^+\\cap\\widehat{\\Sigma}_\\beta^+=\\varnothing;\\quad(\\Longleftrightarrow\\Sigma_\\alpha^+\\cap\\Sigma_\\beta^+=\\varnothing).",
        "evidence": "Half b, each local alpha/beta, two hats, plus signs, equalities, arrowheads, parentheses and endpoint point read independently; the semicolon in this audit is an item separator, not supplied manuscript punctuation."
      },
      {
        "location": "Guide/graphic groups",
        "selected": "G01 cancelled Sigma; G02 la+point; G03 union+limit+parenthesized term+hat+brace; G04 partie+non vide+de I, et; G05 whole relation",
        "evidence": "Exact source boundaries are stated in comments and graphic_groups; no adjoining word is duplicated and the G05 formula continues directly with pi_0."
      }
    ],
    "S_coverage": {
      "row_id": "SA01-K81-06",
      "item": "SA01-29",
      "stated_where": "81/15-22",
      "stated_reader": "Claude Opus 5.5 at effort max, reader R4 (no scan viewed)",
      "scope": "Witness proposals over scans015–022; no visual authority is inferred from that broad span.",
      "local_result": "The two closure bars on this sheet were confirmed on half a and already occur in both current C and H. None of the exact quoted example expressions is written verbatim here; the same closure-bar concern was considered only at the two local barred Sigma intersections. No bar is inferred on an unbarred U or the initial paired intersections.",
      "diff_C": false,
      "diff_H": false,
      "source_only_scope_choice": true
    },
    "H_collation": "H has text. Its editorial note about neighboring pages supplies no manuscript words on this sheet. Its note describing the raised hatted Sigma is collated with the body as one existing label, not an omitted second formula. H emphasis and our underline carry the same single-underline span. Each of its three ill placeholders is counted once (D07, D16, D26)."
  },
  "notation": [
    {
      "location": "Three Pi occurrences",
      "visible_form": "Small upper closed loops, lower I/J distinct",
      "latex": "\\Pi_I^{\\unsure{\\circ|0}}, \\Pi_J^\\circ, \\Pi_I^\\circ",
      "qualification": "Local circle/zero alternatives remain at all three physical occurrences."
    },
    {
      "location": "Opening U and each subsequent U",
      "visible_form": "Large curved U, lowered hooked J and dotted i separated by comma",
      "latex": "U_{J,i}"
    },
    {
      "location": "Two non-emptiness intersections",
      "visible_form": "Separate long horizontal closure rules above Sigma and its raised sign",
      "latex": "\\overline{\\Sigma_i^+}, \\overline{\\Sigma_i^-}",
      "status": "Already in C and H; S concern confirmed locally without current-witness bar correction."
    },
    {
      "location": "Count and parenthetical conclusion",
      "visible_form": "nb without a terminal abbreviation point; lower card lettering; point after proof abbreviation",
      "latex": "nb, \\operatorname{card} I, \\unsure{dèm.|dém.|dem.}"
    },
    {
      "location": "Lemma raised label and hatted disjointness pair",
      "visible_form": "Three separate roof accents over Sigma",
      "latex": "\\widehat{\\Sigma}_\\alpha^+; \\widehat{\\Sigma}_\\alpha^+\\cap\\widehat{\\Sigma}_\\beta^+"
    },
    {
      "location": "Last parenthesized expression",
      "visible_form": "Un-hatted Sigma heads, two-ended double-line arrow, equality and slashed empty-set form",
      "latex": "(\\Longleftrightarrow\\Sigma_\\alpha^+\\cap\\Sigma_\\beta^+=\\varnothing)."
    },
    {
      "location": "Lower-left margin",
      "visible_form": "Slanted two-line K est neq empty / si I neq empty",
      "latex": "K\\text{ est }\\ne\\varnothing;\\quad\\text{si }I\\ne\\varnothing",
      "qualification": "Semicolon here describes two lines only; reading.tex adds no punctuation between the conditions."
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "A nearly vertical accent in dém./dem. admits a grave-primary reading; the exact source row is retained while the additional supported accent candidate is exposed.",
    "The membership correction is most faithfully retained as literal geometry plus complete state interpretations. G05 makes its three runs and the unresolved old-arrow/live-membership states explicit.",
    "A detached point above/right of la can have unresolved attachment as well as role/hand. G02 keeps the word and shape together without assigning a punctuation value.",
    "No missing convention blocked completion. The prescribed first-occurrence rule is followed for the three Pi rings, while every local alternative remains in the report."
  ]
}

## Reader C

\scanpage{20}
Ainsi les classes de $\Pi_I^{\unsure{\circ|0}}$ sont les classes de $\Pi_J^\circ$ distinctes de $\deleted{\Pi}U_{J,i}$, et de plus les \unsure{deux|clas}. parmi
\[
U_{J,i}\cap\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\ U_{J,i}\cap\Sigma_i^-
\]
qui sont non vides. Or les deux classes en question sont non vides, car $\deleted{\Sigma_{\unsure{j|i}}}$ $U_{J,i}$ est un voisinage de $\deleted{\Sigma}E_i$, et
\[
\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
\]
On sait donc que le nb des classes est en \deleted{\unsure{tout|est}} $(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève \unsure{aussi|ainsi} la \unsure{dèm.|dém.|dem.} par récurrence sur le nb des classes).

\uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
% G01--G02: complete word-free union/brace group. Local origin is full-scan
% (900,1600); x increases right and y down; one local unit is one source pixel.
% Fixed local rectangle (0,0)--(510,210); baseline is local y=145.
% The literal U-shaped operator replaces the visible bigcup, which is not
% drawn a second time. Its annotation identifies that same operator only.
\figure{\begin{tikzpicture}[x=0.018cm,y=-0.018cm,baseline={(0,145)},every node/.style={anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{18}{20}\selectfont}]
\path[use as bounding box] (0,0) rectangle (510,210);
\node at (5,145) {$X$};
\node at (62,139) {$\setminus$};
% G01.1: main union bowl and the small closed return at its upper right.
\draw[line width=1.55pt,line cap=round,line join=round]
 (126,94) .. controls (128,124) and (136,145) .. (154,146)
 .. controls (178,150) and (185,130) .. (180,104)
 .. controls (179,93) and (178,84) .. (174,84)
 .. controls (169,83) and (170,94) .. (177,100);
% G01.2: the short visible lower-left retrace of that same bowl.
\draw[line width=0.45pt,line cap=round]
 (130,111) .. controls (133,132) and (143,148) .. (157,148);
\node at (111,191) {$\alpha\in\unsure{\deleted{I}K|K}$};
\node at (199,145) {$(\Sigma_\alpha^+\cup E_\alpha)$};
\node at (291,61) {$\inserted{\widehat{\Sigma}_\alpha^+}$};
% G02.1: complete upper brace, including its central upward step and right hook.
\draw[line width=0.7pt,line cap=round,line join=round]
 (217,78) .. controls (241,75) and (269,73) .. (298,74)
 -- (327,73) -- (328,63)
 .. controls (346,71) and (367,69) .. (393,64)
 .. controls (420,59) and (443,59) .. (451,62)
 .. controls (455,63) and (456,65) .. (457,68);
% G02.2: the left closed loop and returning dark run are one component.
\draw[line width=0.9pt,line cap=round,line join=round]
 (228,80) .. controls (241,70) and (252,69) .. (266,73)
 .. controls (256,80) and (243,82) .. (239,76)
 .. controls (261,75) and (288,72) .. (307,74);
\end{tikzpicture}}
où $K$ est une
% G03--G04: complete insertion/cancellation/guide group with the adjoining
% words partie and de I, including the comma exactly once. No et is in it.
% Local origin full-scan (990,1755), one unit = one source pixel, y down.
% Fixed rectangle (0,0)--(420,150); baseline local y=110; base-west anchors.
\figure{\begin{tikzpicture}[x=0.018cm,y=-0.018cm,baseline={(0,110)},every node/.style={anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{15}{17}\selectfont}]
\path[use as bounding box] (0,0) rectangle (420,150);
\node at (11,112) {partie};
\node at (212,90) {de $I$,};
\node[rotate=10] at (161,47) {\inserted{\rlap{non vide}\phantom{\deleted{non vide}}}};
% G03: the observed oblique cancellation and its hooked right return.
\draw[line width=0.85pt,line cap=round,line join=round]
 (160,48) .. controls (204,41) and (278,23) .. (338,15)
 -- (334,11) -- (341,17)
 .. controls (337,25) and (330,31) .. (320,37);
% G04: the long curved insertion guide begins after partie and spans de I.
\draw[line width=0.7pt,line cap=round,line join=round]
 (188,99) .. controls (183,77) and (211,65) .. (253,52)
 .. controls (287,42) and (325,36) .. (355,32)
 .. controls (360,32) and (362,33) .. (362,37);
\end{tikzpicture}}
et
% slanted; the complete marginal note is in his hand.
\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{23}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}}}\normalmarginpar
$\forall\alpha\in K$, \deleted{on a} $\Sigma_\alpha^+\unsure{\deleted{\Rightarrow}\in|\deleted{\rightarrow}\in|\in}\pi_0(X\setminus E_\alpha)$, tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
% archive sheet number: 19



{
  "differences": [
    {
      "id": "020C-D01",
      "location": "Opening line, superscript of Pi_I",
      "C": "\\Pi_I^{\\unsure{\\circ|0}}",
      "H": "\\Pi_I^0",
      "reading": "\\Pi_I^{\\unsure{\\circ|0}}",
      "evidence": "Small closed, almost circular outline above the I. Its shape supports circle and a small zero; neither reading is removed.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop01_first_ring.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1000,
          65,
          1390,
          175
        ]
      },
      "C_source_doubt_row": "C-R01",
      "local_sublocus": "opening Pi_I",
      "qualification": "H zero remains an explicit alternative; this is a qualified primary-reading difference."
    },
    {
      "id": "020C-D02",
      "location": "Second line, superscript of Pi_J",
      "C": "\\Pi_J^\\circ",
      "H": "\\Pi_J^0",
      "reading": "\\Pi_J^\\circ",
      "evidence": "Small closed angular-rounded ring above the hooked J. Local circle/zero doubt remains; the first-occurrence convention prints circle here without a second wrapper.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop02_second_ring.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          625,
          175,
          870,
          295
        ]
      },
      "C_source_doubt_row": "C-R01",
      "local_sublocus": "opening Pi_J",
      "local_alternatives": [
        "\\circ",
        "0"
      ],
      "qualification": "H zero remains a local alternative."
    },
    {
      "id": "020C-D03",
      "location": "Second line, distinctes de U_{J,i}",
      "C": "\\deleted{\\Pi}U_{J,i}",
      "H": "U_{J,i}",
      "reading": "\\deleted{\\Pi}U_{J,i}",
      "evidence": "A horizontal Pi head and two inner upright strokes survive within the larger curved U strokes. The hooked J, comma, dotted i and following comma are visible.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop03_overwritten_pi_u.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1250,
          145,
          1550,
          295
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null
    },
    {
      "id": "020C-D04",
      "location": "Third prose line, word between les and parmi",
      "C": "\\unsure{clas.|deux}",
      "H": "deux",
      "reading": "\\unsure{deux|clas}.",
      "evidence": "Initial low loop with a tall returning stem and a low undulating continuation supports deux first; the same compressed group still permits clas. The terminal point is treated separately in D05.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop04_deux_clas.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          735,
          275,
          1250,
          380
        ]
      },
      "C_source_doubt_row": "C-R02",
      "local_sublocus": null,
      "qualification": "C first candidate clas survives as the alternative; H deux is the selected primary word."
    },
    {
      "id": "020C-D05",
      "location": "Terminal point after deux/clas before parmi",
      "C": "clas.",
      "H": "deux parmi",
      "reading": "\\unsure{deux|clas}. parmi",
      "evidence": "A separate compact dark point follows the end of the disputed word before the large gap leading to parmi. The point is outside the uncertainty wrapper and applies to both word readings.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop04_deux_clas.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          980,
          305,
          1030,
          350
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null
    },
    {
      "id": "020C-D06",
      "location": "First paired intersection, positive Sigma subscript",
      "C": "\\Sigma_{\\unsure{\\deleted{J}i|j|i}}^+",
      "H": "\\Sigma_i^+",
      "reading": "\\Sigma_{\\unsure{\\deleted{J}i|j|i}}^+",
      "evidence": "A long low left-returning stem lies under a shorter upward hook and a detached high point. An overwritten J with i is the first complete state; single j and i remain supported alternatives.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop05_first_intersection.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          580,
          370,
          990,
          525
        ]
      },
      "C_source_doubt_row": "C-R03",
      "local_sublocus": null,
      "qualification": "H i remains an explicit alternative; no correction chronology is asserted."
    },
    {
      "id": "020C-D07",
      "location": "Cancelled Sigma immediately before U est un voisinage",
      "C": "\\deleted{\\unsure{\\Sigma_i|\\Sigma_j}}",
      "H": "\\struck{\\ill{}}",
      "reading": "\\deleted{\\Sigma_{\\unsure{j|i}}}",
      "evidence": "The Sigma head, diagonal body and lower arm remain readable under crossing strokes. The lowered sign has a returning descender, favouring j, while the crossing strokes leave i supported.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop06_cancelled_sigma.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          280,
          770,
          640,
          915
        ]
      },
      "C_source_doubt_row": "C-R04",
      "local_sublocus": null,
      "qualification": "The cancelled Sigma is recovered; its index remains qualified. The single H ill placeholder is counted once."
    },
    {
      "id": "020C-D08",
      "location": "Index of E after voisinage de",
      "C": "E_{\\unsure{i|j}}",
      "H": "E_i",
      "reading": "E_i",
      "evidence": "A short downward-curving lowered stroke is followed by a spatially separate lower comma. There is no continuing j descender in the complete local target.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop07_voisinage_e.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1375,
          785,
          1425,
          840
        ]
      },
      "C_source_doubt_row": "C-R05",
      "local_sublocus": null
    },
    {
      "id": "020C-D09",
      "location": "Overwritten letter at voisinage de E_i",
      "C": "\\deleted{\\Sigma}E_i",
      "H": "E_i",
      "reading": "\\deleted{\\Sigma}E_i",
      "evidence": "Thin oblique Sigma strokes run inside the heavier upright and three E arms. The predecessor is preserved separately from the index decision D08.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop07_voisinage_e.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1325,
          765,
          1395,
          830
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null
    },
    {
      "id": "020C-D10",
      "location": "Comma after voisinage de E_i before et",
      "C": "E_i,\\ et",
      "H": "E_i\\ et",
      "reading": "E_i, et",
      "evidence": "The lower curved comma is detached below and right of the short index; both marks fit completely in the crop.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop07_voisinage_e.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1385,
          805,
          1430,
          845
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null
    },
    {
      "id": "020C-D11",
      "location": "First nonemptiness formula, Sigma predecessor beneath E_i",
      "C": "\\overline{\\Sigma_i^+}\\cap\\deleted{\\Sigma}E_i",
      "H": "\\overline{\\Sigma_i^+}\\cap E_i",
      "reading": "\\overline{\\Sigma_i^+}\\cap\\deleted{\\Sigma}E_i",
      "evidence": "Diagonal upper and lower strokes remain between the darker E upright and horizontal arms. The long closure rule over the preceding Sigma and plus is separately confirmed and already in C/H.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop08_first_barred_formula.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          470,
          940,
          540,
          1010
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null
    },
    {
      "id": "020C-D12",
      "location": "Second nonemptiness formula, E predecessor beneath barred Sigma_i^-",
      "C": "\\overline{\\deleted{E}\\Sigma_i^-}",
      "H": "\\overline{\\Sigma_i^-}",
      "reading": "\\overline{\\deleted{E}\\Sigma_i^-}",
      "evidence": "A lighter upright and inner arm remain under the stronger oblique Sigma body; the minus and separate long rule above the complete group are visible.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop09_second_barred_formula.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          745,
          915,
          860,
          990
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null
    },
    {
      "id": "020C-D13",
      "location": "Second nonemptiness formula, Sigma predecessor beneath E_i",
      "C": "\\cap\\deleted{\\Sigma}E_i",
      "H": "\\cap E_i",
      "reading": "\\cap\\deleted{\\Sigma}E_i",
      "evidence": "Oblique remnants lie between the three E arms, as a complete separate local overwrite. The endpoint is a period.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop09_second_barred_formula.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          905,
          925,
          985,
          995
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null
    },
    {
      "id": "020C-D14",
      "location": "On ... donc following nonemptiness formulas",
      "C": "On \\unsure{voit|sait} donc",
      "H": "On voit donc",
      "reading": "On sait donc",
      "evidence": "The first low stroke turns back on itself in an s-shaped return; an oval a and the high i mark precede the tall final t. The enlarged full verb supports sait.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crop10_on_voit_sait.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1180,
          875,
          1655,
          1000
        ]
      },
      "C_source_doubt_row": "C-R10",
      "local_sublocus": null
    },
    {
      "id": "020C-D15",
      "location": "Between est and the cancelled word before the count",
      "C": "est en \\deleted{\\unsure{tout|est}}",
      "H": "est \\struck{\\ill{}}",
      "reading": "est en \\deleted{\\unsure{tout|est}}",
      "evidence": "A separate low loop and long n continuation form the live word en; the following cancellation begins farther right.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop11_en_cancelled_word.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1315,
          1045,
          1420,
          1110
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null
    },
    {
      "id": "020C-D16",
      "location": "Cancelled word at right before count",
      "C": "\\deleted{\\unsure{tout|est}}",
      "H": "\\struck{\\ill{}}",
      "reading": "\\deleted{\\unsure{tout|est}}",
      "evidence": "A tall left loop, flattened middle run and raised right termination survive the long crossing strokes. Tout remains the strongest word; est remains supported under the crossing.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop11_en_cancelled_word.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1190,
          1010,
          1630,
          1155
        ]
      },
      "C_source_doubt_row": "C-R06",
      "local_sublocus": null,
      "qualification": "One H cancelled ill placeholder is replaced by one explicitly qualified word."
    },
    {
      "id": "020C-D17",
      "location": "Parenthesis, adverb before la",
      "C": "\\unsure{aussi|ainsi}",
      "H": "aussi",
      "reading": "\\unsure{aussi|ainsi}",
      "evidence": "A compressed low initial group, a distinct turning s-like stroke and a final dotted i support aussi; the nearly level early run still permits ainsi.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop13_aussi_dem_par.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          270,
          1285,
          985,
          1435
        ]
      },
      "C_source_doubt_row": "C-R11",
      "local_sublocus": null,
      "qualification": "Same primary as H; its different editorial qualification produces no H count."
    },
    {
      "id": "020C-D18",
      "location": "Parenthesis, abbreviation before par récurrence",
      "C": "\\unsure{dém.|dem.}",
      "H": "dém.",
      "reading": "\\unsure{dèm.|dém.|dem.}",
      "evidence": "A very short raised stroke beside the d/e group tilts down toward the right. Grave is selected first; the nearly upright/rejoined mark also supports acute or no independently assigned accent. The endpoint point is clear.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop13_aussi_dem_par.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          270,
          1285,
          985,
          1435
        ]
      },
      "C_source_doubt_row": "C-R07",
      "local_sublocus": null,
      "qualification": "H dém. and both original C accent-presence candidates remain explicit alternatives."
    },
    {
      "id": "020C-D19",
      "location": "Lemma heading sentence, superscript of Pi_I",
      "C": "\\Pi_I^\\circ",
      "H": "\\Pi_I^0",
      "reading": "\\Pi_I^\\circ",
      "evidence": "The raised closed ring has a slight left protrusion and an oval hollow. Circle and zero remain locally supported; the printed recurrence is circle after the first page qualifier.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop14_lemma_union_group.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          880,
          1520,
          1475,
          1820
        ]
      },
      "C_source_doubt_row": "C-R01",
      "local_sublocus": "lemma Pi_I",
      "local_alternatives": [
        "\\circ",
        "0"
      ],
      "qualification": "H zero remains a local alternative."
    },
    {
      "id": "020C-D20",
      "location": "Lemma union index, form under the K",
      "C": "\\alpha\\in\\deleted{\\unsure{I}}K",
      "H": "\\alpha\\in K",
      "reading": "\\alpha\\in\\unsure{\\deleted{I}K|K}",
      "evidence": "Top and bottom horizontal serif-like strokes and a shared upright remain at the K. A cancelled I beneath K is supported, but those strokes can belong to the single K form; complete states are retained.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop14_lemma_union_group.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          880,
          1520,
          1475,
          1820
        ]
      },
      "C_source_doubt_row": "C-R08",
      "local_sublocus": null,
      "qualification": "The original blank alternative is made explicit as K alone. H K remains a complete-state alternative."
    },
    {
      "id": "020C-D21",
      "location": "Lemma, large U-shaped indexed union operator",
      "C": "\\bigcup",
      "H": "\\bigcup",
      "reading": "G01.1 and G01.2 literal union bowl",
      "evidence": "The rounded bowl has a small closed returning loop at the upper right and a thin lower-left retrace. The two local paths preserve those inspected components; no generic visible bigcup is drawn over them.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop14_lemma_union_group.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1015,
          1675,
          1090,
          1755
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null,
      "graphic_group": "G01",
      "shape_confidence": "high",
      "geometric_precision": "manual approximation, not rendered or metric-validated"
    },
    {
      "id": "020C-D22",
      "location": "Lemma, upper brace beneath inserted hatted Sigma",
      "C": "\\overbrace{\\Sigma_\\alpha^+\\cup E_\\alpha}^{\\inserted{\\widehat{\\Sigma}_\\alpha^+}}",
      "H": "\\note{au-dessus de ... il écrit \\widehat{\\Sigma}_\\alpha^+}",
      "reading": "G02.1 complete brace plus G02.2 left loop/return; inserted label retained once",
      "evidence": "The left brace span contains a closed loop and a heavy returning run; the middle rises in a short angular step; the right span ends in a downturned hook. The upper hatted Sigma label is unchanged.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop14_lemma_union_group.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1105,
          1650,
          1365,
          1690
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null,
      "graphic_group": "G02",
      "shape_confidence": "high",
      "geometric_precision": "manual approximation, not rendered or metric-validated",
      "H_apparatus": "The note supplies the same upper label at the same physical locus; no duplicate manuscript formula or invented prose is counted."
    },
    {
      "id": "020C-D23",
      "location": "Inserted non vide above partie de I",
      "C": "\\inserted{\\deleted{non vide}}",
      "H": "\\add{\\uncertain{non vide}}",
      "reading": "\\inserted{\\rlap{non vide}\\phantom{\\deleted{non vide}}} with G03 cancellation path",
      "evidence": "The words non vide survive an oblique crossing rule with a hooked right return. The literal cancellation replaces a generic additional strike; words, insertion state and deleted annotation each occur once.",
      "confidence": "high",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop15_non_vide_guide.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1140,
          1760,
          1340,
          1815
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null,
      "graphic_group": "G03",
      "C_count_basis": "C already marks deletion; the C change is the explicit slanted/hooked cancellation geometry.",
      "H_count_basis": "One physical non vide cluster: cancellation state and geometry counted together."
    },
    {
      "id": "020C-D24",
      "location": "Long curved guide from after partie above de I",
      "C": "\\inserted{\\deleted{non vide}} without literal guide",
      "H": "\\add{\\uncertain{non vide}} without literal guide",
      "reading": "G04 complete curved guide; adjoining partie and de I, retained exactly once",
      "evidence": "A separate curve starts after partie, rises across the top of de I and runs toward a small downturned right endpoint. It remains distinct from the upper cancellation rule.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop15_non_vide_guide.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          1170,
          1780,
          1365,
          1860
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null,
      "graphic_group": "G04",
      "shape_confidence": "high",
      "geometric_precision": "manual approximation, not rendered or metric-validated"
    },
    {
      "id": "020C-D25",
      "location": "After first universal alpha in K, cancelled prose",
      "C": "\\deleted{on a}",
      "H": "\\struck{\\ill{}}",
      "reading": "\\deleted{on a}",
      "evidence": "The small opening oval, n hump and a loop remain visible along the cancelling horizontal stroke.",
      "confidence": "high",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop17_cancelled_on_a_membership.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          600,
          1970,
          775,
          2020
        ]
      },
      "C_source_doubt_row": null,
      "local_sublocus": null
    },
    {
      "id": "020C-D26",
      "location": "Membership sign immediately before pi_0 in lemma",
      "C": "\\deleted{\\unsure{\\Rightarrow}}\\in",
      "H": "\\in",
      "reading": "\\unsure{\\deleted{\\Rightarrow}\\in|\\deleted{\\rightarrow}\\in|\\in}",
      "evidence": "The live membership-shaped outer curve and central stroke are accompanied by an angular right-returning head. A cancelled double arrow is retained first; the single-shaft arrow candidate and a single reworked membership form remain explicit complete alternatives.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop17_cancelled_on_a_membership.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          935,
          1928,
          1005,
          1995
        ]
      },
      "C_source_doubt_row": "C-R09",
      "local_sublocus": null,
      "qualification": "Original arrow/blank scope is retained and made a complete-state choice. H membership alone survives as an alternative; no writing chronology is asserted."
    }
  ],
  "doubts": [
    {
      "source_row": "C-R01",
      "location": "First opening Pi_I superscript",
      "reading": "\\circ",
      "alternatives": [
        "0"
      ],
      "confidence": "medium",
      "reason": "Closed tiny ring permits both readings.",
      "crop": "crop01_first_ring.png",
      "printed_at_this_occurrence": "\\unsure{\\circ|0}"
    },
    {
      "source_row": "C-R01",
      "location": "Second opening Pi_J superscript",
      "reading": "\\circ",
      "alternatives": [
        "0"
      ],
      "confidence": "medium",
      "reason": "Angular-rounded hollow ring permits a small zero.",
      "crop": "crop02_second_ring.png",
      "printed_at_this_occurrence": "\\circ"
    },
    {
      "source_row": "C-R01",
      "location": "Lemma Pi_I superscript",
      "reading": "\\circ",
      "alternatives": [
        "0"
      ],
      "confidence": "medium",
      "reason": "Small oval ring with protruding start permits a small zero.",
      "crop": "crop14_lemma_union_group.png",
      "printed_at_this_occurrence": "\\circ"
    },
    {
      "source_row": "C-R02",
      "location": "Word before parmi",
      "reading": "deux",
      "alternatives": [
        "clas"
      ],
      "confidence": "medium",
      "reason": "Initial returning stem and low continuation support both word forms; the terminal point is definite.",
      "crop": "crop04_deux_clas.png",
      "printed_at_this_occurrence": "\\unsure{deux|clas}."
    },
    {
      "source_row": "C-R03",
      "location": "First positive Sigma index",
      "reading": "\\deleted{J}i",
      "alternatives": [
        "j",
        "i"
      ],
      "confidence": "low",
      "reason": "Long hooked stem, short upper hook and high point leave glyph and overwrite state open.",
      "crop": "crop05_first_intersection.png"
    },
    {
      "source_row": "C-R04",
      "location": "Cancelled Sigma index before U est un voisinage",
      "reading": "j",
      "alternatives": [
        "i"
      ],
      "confidence": "low",
      "reason": "Descender favours j; cancellation can contribute part of that return.",
      "crop": "crop06_cancelled_sigma.png",
      "printed_at_this_occurrence": "\\deleted{\\Sigma_{\\unsure{j|i}}}"
    },
    {
      "source_row": "C-R06",
      "location": "Cancelled word after en",
      "reading": "tout",
      "alternatives": [
        "est"
      ],
      "confidence": "low",
      "reason": "Crossing strokes cut initial and terminal rises.",
      "crop": "crop11_en_cancelled_word.png",
      "printed_at_this_occurrence": "\\deleted{\\unsure{tout|est}}"
    },
    {
      "source_row": "C-R07",
      "location": "Abbreviation in parenthesis",
      "reading": "dèm.",
      "alternatives": [
        "dém.",
        "dem."
      ],
      "confidence": "low",
      "reason": "Short near-upright/down-right raised mark has unsettled direction and independence.",
      "crop": "crop13_aussi_dem_par.png"
    },
    {
      "source_row": "C-R08",
      "location": "Union index below the large cup",
      "reading": "\\deleted{I}K",
      "alternatives": [
        "K"
      ],
      "confidence": "medium",
      "reason": "Serif-like top, foot and upright support an I predecessor and also a single K form.",
      "crop": "crop14_lemma_union_group.png"
    },
    {
      "source_row": "C-R09",
      "location": "Reworked membership before pi_0",
      "reading": "\\deleted{\\Rightarrow}\\in",
      "alternatives": [
        "\\deleted{\\rightarrow}\\in",
        "\\in"
      ],
      "confidence": "low",
      "reason": "Right angular head and shaft are readable; predecessor identity and cancellation attachment remain open.",
      "crop": "crop17_cancelled_on_a_membership.png"
    },
    {
      "source_row": "C-R11",
      "location": "Adverb before la",
      "reading": "aussi",
      "alternatives": [
        "ainsi"
      ],
      "confidence": "medium",
      "reason": "Flat early run and final dotted i do not settle the intermediate letters.",
      "crop": "crop13_aussi_dem_par.png"
    }
  ],
  "notes": {
    "page_content": "The author continues the class-count argument: the opening identifies the classes of Pi_I using classes of Pi_J and the two written intersections. He writes that the two classes are nonempty, citing a neighbourhood of corrected E_i and the two barred nonemptiness expressions. He then writes the count (n-1)+2=n+1=card I+1 and describes this as completing the induction on the number of classes. The underlined Lemme states a representation by X minus an indexed union of Sigma_alpha^+ cup E_alpha, with the added hatted-Sigma label over that group; the body gives the written membership and pairwise-disjointness clauses. The final parentheses expressly relate the hatted and ordinary pairwise-intersection expressions by a double implication. These are attributed manuscript assertions, not results checked by this reading.",
    "authors_own_uncertainty": "No explicit question mark or verbal uncertainty phrase was found. The exact raised words non vide are cancelled. All unsure alternatives in reading.tex are editorial ink uncertainties.",
    "title_date_page_counts": "One sheet. Underlined heading Lemme; no date and no separate manuscript page-number label. The lower-left archive numeral 19 is recorded only in the required comment, with undetermined hand. H page 19 maps to our scan 20.",
    "mathematics_led_reading_decisions": "No formula was repaired from expected mathematics. Long upper rules were inspected locally. The first paired Sigma index, the cancelled Sigma index, the union-index state and the reworked membership retain explicit alternatives. No calculation, proof check, geometric-extrema check or pixel comparison was performed.",
    "source_administration": "No cotefile command is added on scan 20. The H editorial note about adjacent pages was read as apparatus; those other pages were not opened or collated. H emphasis and our single underline agree on the word Lemme. Ordinary line-wrap/display placement and the approximate margin rotation do not create correction counts.",
    "source_silent_choices": "The complete source selects achève with a grave, par in full, récurrence with an acute, où with a grave, both occurrences of nb without a following point, and lowercase card. It retains the upper-display plus/minus signs, the first-intersection comma, the comma after voisinage de E_i, comma/period endpoints of the nonemptiness pair, both final hats, and the final parenthesis and period. The latter two Pi superscripts print circle while their zero alternatives remain explicit in the report. The tiny final component of la is represented through that word once, not as a second free point. The source contains no extra detached-mark path beyond the six declared guide/operator/brace/cancellation paths.",
    "S_coverage": {
      "row_id": "SA01-K81-06",
      "source_item": "SA01-29",
      "stated_range": "81/15-22",
      "stated_author_scope": "Recorded author: Claude Opus 5.5 at effort max, reader R4 (no scan viewed). The row supplies witness proposals only.",
      "local_confirmations": [
        {
          "location": "First nonemptiness Sigma_i^+",
          "crop": "crop08_first_barred_formula.png",
          "reading": "\\overline{\\Sigma_i^+}",
          "current_C_has_bar": true,
          "current_H_has_bar": true,
          "witness_correction_count": 0
        },
        {
          "location": "Second nonemptiness Sigma_i^-",
          "crop": "crop09_second_barred_formula.png",
          "reading": "\\overline{\\deleted{E}\\Sigma_i^-}",
          "current_C_has_bar": true,
          "current_H_has_bar": true,
          "witness_correction_count": 0
        }
      ],
      "example_matching": "The exact quoted index-1/i.e. example, the strict-inclusion chain, and the U_s example are absent from this sheet. The local positive nonemptiness expression uses i and already has its bar in C/H. The sheet has no literal i.e. phrase. The parenthesized final double implication is recorded as its own author-written relation, not substituted for an S example.",
      "source_flags": "No S proposal is promoted to an unobserved bar or a present-witness omission."
    },
    "processing_note": "The first combined packet output was truncated. The entire brief and all listed packet files, preamble and notation snapshot were subsequently delivered in bounded calls and read. No image delivery failed; no successful view was reopened. A root checkpoint hold began after the complete visual phase and saved reading.tex/image_audit.json/progress.md; work resumed in the same context with no image reopen. The final report and audit were completed after release.",
    "C_source_doubt_map": [
      {
        "id": "C-R01",
        "raw_row": "| 20 | opening and lemma | superscript circle | 0 | medium | The circle is much smaller than the indexed I; its outline also permits a small zero. | The surrounding text does not settle this reading. |",
        "location": "opening and lemma",
        "reading": "superscript circle",
        "other_readings": "0",
        "confidence": "medium",
        "source_evidence": "The circle is much smaller than the indexed I; its outline also permits a small zero.",
        "contextual_preference": "The surrounding text does not settle this reading.",
        "local_decisions": [
          {
            "difference_id": "020C-D01",
            "sublocus": "opening Pi_I",
            "status": "retained",
            "reading": "\\Pi_I^{\\unsure{\\circ|0}}",
            "crop": "crop01_first_ring.png"
          },
          {
            "difference_id": "020C-D02",
            "sublocus": "opening Pi_J",
            "status": "retained",
            "reading": "\\Pi_J^\\circ",
            "crop": "crop02_second_ring.png"
          },
          {
            "difference_id": "020C-D19",
            "sublocus": "lemma Pi_I",
            "status": "retained",
            "reading": "\\Pi_I^\\circ",
            "crop": "crop14_lemma_union_group.png"
          }
        ],
        "source_row_status": "retained"
      },
      {
        "id": "C-R02",
        "raw_row": "| 20 | line 3 | clas. | deux | medium | A tall loop above two low humps with a distinct terminal point. The later phrase reads les deux classes. | Either classes or deux is suggested by les deux classes below. |",
        "location": "line 3",
        "reading": "clas.",
        "other_readings": "deux",
        "confidence": "medium",
        "source_evidence": "A tall loop above two low humps with a distinct terminal point. The later phrase reads les deux classes.",
        "contextual_preference": "Either classes or deux is suggested by les deux classes below.",
        "local_decisions": [
          {
            "difference_id": "020C-D04",
            "sublocus": "Third prose line, word between les and parmi",
            "status": "retained",
            "reading": "\\unsure{deux|clas}.",
            "crop": "crop04_deux_clas.png"
          }
        ],
        "source_row_status": "retained"
      },
      {
        "id": "C-R03",
        "raw_row": "| 20 | first paired intersection | i written on J | j / i | low | The dotted short hook is on top of a much longer left-returning stroke; separate letters and a descending j are both possible. | The next negative intersection and the subsequent barred formulas use i. |",
        "location": "first paired intersection",
        "reading": "i written on J",
        "other_readings": "j / i",
        "confidence": "low",
        "source_evidence": "The dotted short hook is on top of a much longer left-returning stroke; separate letters and a descending j are both possible.",
        "contextual_preference": "The next negative intersection and the subsequent barred formulas use i.",
        "local_decisions": [
          {
            "difference_id": "020C-D06",
            "sublocus": "First paired intersection, positive Sigma subscript",
            "status": "retained",
            "reading": "\\Sigma_{\\unsure{\\deleted{J}i|j|i}}^+",
            "crop": "crop05_first_intersection.png"
          }
        ],
        "source_row_status": "retained"
      },
      {
        "id": "C-R04",
        "raw_row": "| 20 | before U est un voisinage | Σ_i | Σ_j | low | Crossed through at the base; only a short return and dot remain from the index. | The neighbouring U and the barred sigmas repeat i. |",
        "location": "before U est un voisinage",
        "reading": "Σ_i",
        "other_readings": "Σ_j",
        "confidence": "low",
        "source_evidence": "Crossed through at the base; only a short return and dot remain from the index.",
        "contextual_preference": "The neighbouring U and the barred sigmas repeat i.",
        "local_decisions": [
          {
            "difference_id": "020C-D07",
            "sublocus": "Cancelled Sigma immediately before U est un voisinage",
            "status": "retained",
            "reading": "\\deleted{\\Sigma_{\\unsure{j|i}}}",
            "crop": "crop06_cancelled_sigma.png"
          }
        ],
        "source_row_status": "retained"
      },
      {
        "id": "C-R05",
        "raw_row": "| 20 | voisinage de E | i | j | medium | The mark turns down and slightly left. Subsequent intersections show i. | The barred intersections that follow use i. |",
        "location": "voisinage de E",
        "reading": "i",
        "other_readings": "j",
        "confidence": "medium",
        "source_evidence": "The mark turns down and slightly left. Subsequent intersections show i.",
        "contextual_preference": "The barred intersections that follow use i.",
        "local_decisions": [
          {
            "difference_id": "020C-D08",
            "sublocus": "Index of E after voisinage de",
            "status": "resolved",
            "reading": "E_i",
            "crop": "crop07_voisinage_e.png"
          }
        ],
        "source_row_status": "resolved"
      },
      {
        "id": "C-R06",
        "raw_row": "| 20 | word struck at right before count | tout | est | low | A long crossing diagonal cuts both the initial stroke and the last rise. The preceding word resembles en. | tout completes the words est en before the count. |",
        "location": "word struck at right before count",
        "reading": "tout",
        "other_readings": "est",
        "confidence": "low",
        "source_evidence": "A long crossing diagonal cuts both the initial stroke and the last rise. The preceding word resembles en.",
        "contextual_preference": "tout completes the words est en before the count.",
        "local_decisions": [
          {
            "difference_id": "020C-D16",
            "sublocus": "Cancelled word at right before count",
            "status": "retained",
            "reading": "\\deleted{\\unsure{tout|est}}",
            "crop": "crop11_en_cancelled_word.png"
          }
        ],
        "source_row_status": "retained"
      },
      {
        "id": "C-R07",
        "raw_row": "| 20 | in the parenthesis | dém. | dem. | medium | The upper stroke is very short and merges into the d. | dém. recurs beside récurrence. |",
        "location": "in the parenthesis",
        "reading": "dém.",
        "other_readings": "dem.",
        "confidence": "medium",
        "source_evidence": "The upper stroke is very short and merges into the d.",
        "contextual_preference": "dém. recurs beside récurrence.",
        "local_decisions": [
          {
            "difference_id": "020C-D18",
            "sublocus": "Parenthesis, abbreviation before par récurrence",
            "status": "retained",
            "reading": "\\unsure{dèm.|dém.|dem.}",
            "crop": "crop13_aussi_dem_par.png"
          }
        ],
        "source_row_status": "retained"
      },
      {
        "id": "C-R08",
        "raw_row": "| 20 | under K, union index | I | — | medium | A straight top and foot can be seen through K. | The same sentence calls K a part of I. |",
        "location": "under K, union index",
        "reading": "I",
        "other_readings": "—",
        "confidence": "medium",
        "source_evidence": "A straight top and foot can be seen through K.",
        "contextual_preference": "The same sentence calls K a part of I.",
        "local_decisions": [
          {
            "difference_id": "020C-D20",
            "sublocus": "Lemma union index, form under the K",
            "status": "retained",
            "reading": "\\alpha\\in\\unsure{\\deleted{I}K|K}",
            "crop": "crop14_lemma_union_group.png"
          }
        ],
        "source_row_status": "retained"
      },
      {
        "id": "C-R09",
        "raw_row": "| 20 | beside membership sign before π₀ | ⇒ | — | low | The right end looks arrow-shaped in the reworked sign. | The surrounding text does not settle this reading. |",
        "location": "beside membership sign before π₀",
        "reading": "⇒",
        "other_readings": "—",
        "confidence": "low",
        "source_evidence": "The right end looks arrow-shaped in the reworked sign.",
        "contextual_preference": "The surrounding text does not settle this reading.",
        "local_decisions": [
          {
            "difference_id": "020C-D26",
            "sublocus": "Membership sign immediately before pi_0 in lemma",
            "status": "retained",
            "reading": "\\unsure{\\deleted{\\Rightarrow}\\in|\\deleted{\\rightarrow}\\in|\\in}",
            "crop": "crop17_cancelled_on_a_membership.png"
          }
        ],
        "source_row_status": "retained"
      },
      {
        "id": "C-R10",
        "raw_row": "| 20 | above the count | voit | sait | medium | A low returning first stroke precedes a short vowel group and a high t. The sentence admits either verb. | The surrounding text does not settle this reading. |",
        "location": "above the count",
        "reading": "voit",
        "other_readings": "sait",
        "confidence": "medium",
        "source_evidence": "A low returning first stroke precedes a short vowel group and a high t. The sentence admits either verb.",
        "contextual_preference": "The surrounding text does not settle this reading.",
        "local_decisions": [
          {
            "difference_id": "020C-D14",
            "sublocus": "On ... donc following nonemptiness formulas",
            "status": "resolved",
            "reading": "On sait donc",
            "crop": "crop10_on_voit_sait.png"
          }
        ],
        "source_row_status": "resolved"
      },
      {
        "id": "C-R11",
        "raw_row": "| 20 | in the parenthesis, before la | aussi | ainsi | medium | The body is reduced to a nearly straight line, followed by a distinct turn and a dotted i. | Both adverbs can link the count to the conclusion. |",
        "location": "in the parenthesis, before la",
        "reading": "aussi",
        "other_readings": "ainsi",
        "confidence": "medium",
        "source_evidence": "The body is reduced to a nearly straight line, followed by a distinct turn and a dotted i.",
        "contextual_preference": "Both adverbs can link the count to the conclusion.",
        "local_decisions": [
          {
            "difference_id": "020C-D17",
            "sublocus": "Parenthesis, adverb before la",
            "status": "retained",
            "reading": "\\unsure{aussi|ainsi}",
            "crop": "crop13_aussi_dem_par.png"
          }
        ],
        "source_row_status": "retained"
      }
    ],
    "graphic_groups": [
      {
        "group": "G01--G02",
        "observed_bbox": [
          900,
          1620,
          1380,
          1805
        ],
        "local_origin_full_scan": [
          900,
          1600
        ],
        "local_axes": "x right, y down; 1 local unit = 1 source pixel",
        "drawing_rectangle": [
          0,
          0,
          510,
          210
        ],
        "display_units": "x=0.018cm, y=-0.018cm",
        "baseline_local_y": 145,
        "node_anchor": "base west; inner sep=0pt; outer sep=0pt",
        "text_boundaries": "Only X, setminus, union index alpha in qualified I/K, (Sigma_alpha^+ cup E_alpha), and inserted hatted Sigma label. No adjoining French words or punctuation are included.",
        "paths": [
          "G01.1",
          "G01.2",
          "G02.1",
          "G02.2"
        ],
        "duplication_control": "Literal bowl is the only visible large union. Literal brace is the only visible brace. No generic bigcup or overbrace is superimposed.",
        "precision": "Manually approximated from the one complete crop; no rendering or metric comparison."
      },
      {
        "group": "G03--G04",
        "observed_bbox": [
          990,
          1760,
          1410,
          1900
        ],
        "local_origin_full_scan": [
          990,
          1755
        ],
        "local_axes": "x right, y down; 1 local unit = 1 source pixel",
        "drawing_rectangle": [
          0,
          0,
          420,
          150
        ],
        "display_units": "x=0.018cm, y=-0.018cm",
        "baseline_local_y": 110,
        "node_anchor": "base west; inner sep=0pt; outer sep=0pt",
        "text_boundaries": "Exactly partie, de I, and non vide. The comma after I is inside the de I node. The following et remains outside this group.",
        "paths": [
          "G03",
          "G04"
        ],
        "phantom_annotation": "The inserted node contains visible rlap{non vide} and an invisible phantom{deleted{non vide}}; only G03 supplies the visible cancellation rule.",
        "precision": "Manually approximated from the one complete crop; no rendering or metric comparison."
      }
    ]
  },
  "notation": [
    {
      "location": "Three Pi superscripts",
      "sign": "small closed ring",
      "latex": "\\unsure{\\circ|0}; later \\circ",
      "status": "Three local circle/zero doubts recorded independently under C-R01."
    },
    {
      "location": "Opening U and three subsequent U occurrences",
      "sign": "U with hooked J, comma and dotted i",
      "latex": "U_{J,i}",
      "status": "Each local occurrence visually inspected; the first has the Pi predecessor."
    },
    {
      "location": "Upper paired intersections",
      "sign": "Short Sigma head strokes and raised plus/minus",
      "latex": "\\Sigma_{\\unsure{\\deleted{J}i|j|i}}^+,\\ \\Sigma_i^-",
      "status": "Source selects ordinary Sigma head forms here; no additional closure rule is supplied."
    },
    {
      "location": "Two nonemptiness formulas",
      "sign": "Separate long upper rules spanning the raised signs",
      "latex": "\\overline{\\Sigma_i^+};\\ \\overline{\\deleted{E}\\Sigma_i^-}",
      "status": "Both observed long rules confirmed; both are already represented in current C/H."
    },
    {
      "location": "Nonemptiness formulas, margin note and two final equalities",
      "sign": "Slashed small oval",
      "latex": "\\varnothing",
      "status": "Six local empty-set signs read; H emptyset syntax conveys the same selected reading and receives no macro-only difference."
    },
    {
      "location": "Count prose, end of parenthesis, count formula",
      "sign": "nb; low linked card",
      "latex": "nb;\\ \\operatorname{card} I",
      "status": "Both nb occurrences and lowercase card retained; no abbreviation expansion in the transcription."
    },
    {
      "location": "Parenthesis opening",
      "sign": "Two small down-right marks above the middle e of achève",
      "latex": "achève",
      "status": "Grave accent retained after crop12; complete qui descender remains attached to qui once."
    },
    {
      "location": "Parenthesis abbreviation",
      "sign": "Near-upright/down-right tiny raised mark; terminal point",
      "latex": "\\unsure{dèm.|dém.|dem.}",
      "status": "Every supported accent/no-accent alternative remains local."
    },
    {
      "location": "Parenthesis after abbreviation",
      "sign": "Compressed par, then acute on récurrence",
      "latex": "par récurrence",
      "status": "Source selects full par and accented récurrence; the compressed run and local acute were inspected, not normalized from another page."
    },
    {
      "location": "Lemma start and final equalities",
      "sign": "Roof-shaped marks above Sigma",
      "latex": "\\widehat{\\Sigma}_\\alpha^+;\\ \\widehat{\\Sigma}_\\beta^+",
      "status": "One inserted upper label and two final hatted objects; the final parenthesized pair has ordinary Sigma forms."
    },
    {
      "location": "Final parenthesis",
      "sign": "Two shafts with heads at both ends",
      "latex": "\\Longleftrightarrow",
      "status": "Same author-written relation retained without an equivalence proof check."
    },
    {
      "location": "Lower-left note",
      "sign": "K est ne empty / si I ne empty",
      "latex": "K\\text{ est }\\ne\\varnothing;\\ \\text{si }I\\ne\\varnothing",
      "status": "Complete slanted note read; no source difference."
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The source row for the superscript ring is one compound source doubt covering three inspected local occurrences; their later unwrapped circle forms must remain visible in the audit.",
    "For the I/K and arrow/membership loci, the supplied blank alternative was rendered as an explicit complete state. The first candidate is retained; no independent C correction count is assigned to this qualification-only expansion.",
    "The graphic approximations have fixed declared local origins and text boundaries; these declarations provide source bookkeeping, not rendered geometric validation."
  ]
}

--- A
+++ B
@@ -1,101 +1,78 @@
 \scanpage{20}
 Ainsi les classes de $\Pi_I^{\unsure{\circ|0}}$ sont les classes de $\Pi_J^\circ$ distinctes de $\deleted{\Pi}U_{J,i}$, et de plus les \unsure{clas.|deux.} parmi
 \[
-U_{J,i}\cap\Sigma_{\unsure{j|\deleted{J}i|i}}^+,\quad U_{J,i}\cap\Sigma_i^-
+U_{J,i}\cap\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\quad U_{J,i}\cap\Sigma_i^-
 \]
 qui sont non vides. Or les deux classes en question sont non vides, car
-% A020-G01: cancelled Sigma with j/i index; glyph and complete cancellation state retained.
-% Fixed source origin (320,817); local pixels right/down; baseline at source y=875.
-% The two slanted cancellation runs are drawn once; the deleted annotation is invisible.
-\begin{tikzpicture}[baseline=(A020G01base.base),x=0.025em,y=-0.025em]
-\useasboundingbox (-2,-5) rectangle (82,85);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G01base) at (1,58)
-{\rlap{$\Sigma_{\unsure{j|i}}$}\phantom{$\deleted{\Sigma_{\unsure{j|i}}}$}};
-\draw[line width=0.35pt] (2,58)--(33,-1);
-\draw[line width=0.35pt] (23,60)--(62,18);
+% B_G01: cancelled Sigma and its two visible crossing runs. Observed locus (320,810,403,900).
+% Source origin (315,803); x right, y down; 0.25 pt per source pixel. Baseline y=76.
+% The visible node occurs once; its phantom carries the deletion state without a generic extra rule.
+\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,76)}]
+\path[use as bounding box] (0,0) rectangle (95,100);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,76) {\rlap{$\unsure{\Sigma_j|\Sigma_i}$}\phantom{\deleted{$\unsure{\Sigma_j|\Sigma_i}$}}};
+\draw[line width=0.45pt,line cap=round] (10,73) .. controls (20,54) and (30,31) .. (40,12);
+\draw[line width=0.45pt,line cap=round] (45,73) .. controls (43,80) and (49,82) .. (54,76) -- (69,35);
 \end{tikzpicture}
-$U_{J,i}$ est un voisinage
-% A020-G02: gray detached round point, source origin (1175,817), baseline y=817.
-% Shape candidate only; role, hand and surface origin unresolved. No word is in this group.
-\unsure{\begin{tikzpicture}[baseline={(0,0)},x=0.025em,y=-0.025em]
-\useasboundingbox (0,0) rectangle (11,24);
-\fill[gray] (4,18) ellipse [x radius=2.2,y radius=2.5];
-\end{tikzpicture}}
-de $\deleted{\Sigma}E_{\unsure{i|j}}$, et
+$U_{J,i}$ est un voisinage de $\deleted{\Sigma}E_{\unsure{i|j}}$, et
 \[
 \overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
 \overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
 \]
-On sait donc que le nb des classes est en
-% A020-G03: cancelled tout/est; fixed source origin (1457,1038), baseline y=1081.
-% The observed two crossing runs replace a generic visible cancellation rule.
-\begin{tikzpicture}[baseline=(A020G03base.base),x=0.025em,y=-0.025em]
-\useasboundingbox (-2,-3) rectangle (130,53);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G03base) at (0,43)
-{\rlap{\unsure{tout|est}}\phantom{\deleted{\unsure{tout|est}}}};
-\draw[line width=0.45pt] (0,27)--(30,44);
-\draw[line width=0.35pt] (46,8)--(80,26)..controls (96,34) and (110,40)..(122,41);
+On sait donc que le nb des classes est en \deleted{\unsure{tout|est}} $(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève \unsure{aussi|ainsi}
+% B_G02: complete word-bearing group la and one qualified detached point above/right.
+% Origin (500,1347), 0.25 pt per source pixel, baseline y=49. Observed point locus (566,1363,575,1373).
+% Inner graphic origin is explicitly translated by (66,18); base-west anchor and baseline (0,0) fix its placement.
+\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline=(Bla.base)]
+\path[use as bounding box] (0,0) rectangle (88,62);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (Bla) at (0,49) {la};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (66,18) {\unsure{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,0)}]
+\path[use as bounding box] (0,0) rectangle (7,8);
+\fill (2,0) -- (5,4) -- (4,7) -- (1,6) -- cycle;
+\end{tikzpicture}}};
 \end{tikzpicture}
-$(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève \unsure{aussi|ainsi} la
-% A020-G04: detached high triangular point after la; source origin (565,1395).
-% Shape candidate only; role, hand and surface origin unresolved. No word is in this group.
-\unsure{\begin{tikzpicture}[baseline={(0,0)},x=0.025em,y=-0.025em]
-\useasboundingbox (0,-33) rectangle (12,0);
-\fill (4,-31)--(7,-26)--(7,-22)--(2,-24)--cycle;
-\end{tikzpicture}}
-\unsure{dém.|dem.} \unsure{par|p} récurrence sur le nb des classes).
+\unsure{dèm.|dém.|dem.} par récurrence sur le nb des classes).
 
 \uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
-% A020-G05: complete formula and its added hatted label; no other words are in this group.
-% Fixed source origin (1105,1660); local pixels right/down; formula baseline y=1735.
-% The ordinary union operator, index, body, two parentheses and label occur once.
-% The retraced left oval is drawn as the second path, beside the main brace run.
-\figure{\begin{tikzpicture}[baseline=(A020G05body.base),x=0.025em,y=-0.025em]
-\useasboundingbox (-210,-50) rectangle (275,145);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (-205,75)
-{$X\setminus\displaystyle\bigcup_{\alpha\in\deleted{I}K}$};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G05body) at (0,75)
-{$(\Sigma_\alpha^+\cup E_\alpha)$};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (88,-6)
-{$\inserted{\widehat{\Sigma}_\alpha^+}$};
-\draw[line width=0.45pt] (12,20)..controls (42,18) and (60,13)..(82,16)
-..controls (102,18) and (116,17)..(123,15)--(123,6)
-..controls (145,16) and (168,13)..(184,10)
-..controls (211,6) and (240,4)..(247,8)--(250,13);
-\draw[line width=0.45pt] (22,22)..controls (33,13) and (50,10)..(64,16)
-..controls (70,22) and (56,25)..(45,22)
-..controls (36,19) and (29,19)..(22,22);
-\end{tikzpicture}}
-où $K$ est une partie
-% A020-G06: complete cancelled insertion and curved guide with adjoining de I,.
-% Fixed source origin (1148,1770); local pixels right/down; de I baseline y=1845.
-% Exact word boundary: non vide (inserted and cancelled), de I,; partie and et remain outside.
-% The phantom carries both editorial states without an extra visible generic strike.
-\begin{tikzpicture}[baseline=(A020G06base.base),x=0.025em,y=-0.025em]
-\useasboundingbox (-3,-5) rectangle (255,94);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,31)
-{\rlap{\inserted{non vide}}\phantom{\inserted{\deleted{non vide}}}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G06base) at (48,75) {de $I$,};
-\draw[line width=0.45pt] (0,33)..controls (59,23) and (119,11)..(181,2);
-\draw[line width=0.35pt] (31,74)..controls (25,52) and (55,37)..(105,27)
-..controls (143,19) and (183,13)..(203,15)--(207,19);
+% B_G03: union, complete parenthesized expression, overwritten limit, raised hatted Sigma, and literal brace.
+% Origin (1010,1600), 0.25 pt per source pixel, baseline y=140; fixed drawing rectangle (0,15)-(390,200).
+% Pi above and X setminus to the left are outside this group. No generic bigcup or overbrace is also drawn.
+$X\setminus\text{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,140)}]
+\path[use as bounding box] (0,15) rectangle (390,200);
+% U01 body; U02 upper-right loop; U03 pale lower retrace.
+\draw[line width=0.95pt,line cap=round] (17,90) .. controls (17,122) and (24,140) .. (45,142) .. controls (63,142) and (72,133) .. (71,115) -- (68,87);
+\draw[line width=0.55pt,line cap=round] (68,87) .. controls (66,77) and (63,81) .. (64,89) .. controls (65,96) and (68,99) .. (68,104);
+\draw[black!55,line width=0.45pt,line cap=round] (19,114) .. controls (23,140) and (51,150) .. (65,133);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small] at (0,190) {$\alpha\in\unsure{\deleted{I}K|K}$};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small] at (91,140) {$(\Sigma_\alpha^+\cup E_\alpha)$};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\scriptsize] at (184,58) {$\inserted{\widehat{\Sigma}_\alpha^+}$};
+% BR01 main run and central turn; BR02 closed left loop; BR03 left retrace.
+\draw[line width=0.65pt,line cap=round] (108,79) .. controls (132,75) and (151,71) .. (180,74) .. controls (193,75) and (204,70) .. (217,72) -- (220,62) .. controls (234,70) and (256,68) .. (287,64) .. controls (307,60) and (326,59) .. (339,62) .. controls (344,63) and (345,66) .. (345,69);
+\draw[line width=0.55pt,line cap=round] (132,76) .. controls (141,68) and (160,69) .. (164,74) .. controls (153,81) and (142,82) .. (132,76);
+\draw[line width=0.85pt,line cap=round] (120,80) .. controls (145,74) and (178,73) .. (210,74);
+\end{tikzpicture}}$
+où $K$ est une
+% B_G04 contains exactly partie, the inserted/deleted non vide, and de I, et.
+% Source origin (997,1750), 0.25 pt per source pixel, baseline y=110. Fixed rectangle (0,0)-(530,160).
+% NV01 is the rising cancellation run with its right return. NV02 is the separate curved insertion guide.
+\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,110)}]
+\path[use as bounding box] (0,0) rectangle (530,160);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,115) {partie};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small,rotate=8] at (157,45) {\inserted{\rlap{non vide}\phantom{\deleted{non vide}}}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (200,89) {de $I$, et};
+\draw[line width=0.55pt,line cap=round] (154,53) .. controls (203,44) and (282,30) .. (331,24) .. controls (331,31) and (325,37) .. (315,43);
+\draw[line width=0.45pt,line cap=round] (182,94) .. controls (172,61) and (272,47) .. (339,40) .. controls (346,39) and (351,39) .. (355,43);
 \end{tikzpicture}
-et
-% slanted
-\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{19}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}}}\normalmarginpar
+% slanted; the two written conditions have no punctuation between them.
+\reversemarginpar\margin{\begin{tikzpicture}\node[rotate=19,anchor=base west,inner sep=0pt,outer sep=0pt] {\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}};\end{tikzpicture}}\normalmarginpar
 $\forall\alpha\in K$, \deleted{on a} $\Sigma_\alpha^+
-% A020-G07: complete observed reworked membership/arrow shape, source origin (945,1943).
-% Full-state candidates: \deleted{\Rightarrow}\in | \deleted{\to}\in | \in.
-% The primary is the first candidate; the third retains a live/retraced membership state.
-% The phantom records the complete candidates; the local unsure qualifies the actual paths.
-\mathrel{\unsure{\begin{tikzpicture}[baseline={(0,41)},x=0.025em,y=-0.025em]
-\useasboundingbox (-2,-2) rectangle (55,55);
-\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at (0,41)
-{\phantom{$\deleted{\Rightarrow}\in|\deleted{\to}\in|\in$}};
-\draw[line width=0.45pt] (38,4)..controls (24,1) and (1,25)..(1,33)
-..controls (1,48) and (19,51)..(28,47);
-\draw[line width=0.45pt] (2,33)--(41,28);
-\draw[line width=0.35pt] (26,20)--(42,31)..controls (48,32) and (44,18)..(40,16);
-\end{tikzpicture}}}
-\pi_0(X\setminus{\unsure{E|\deleted{\Sigma}E}}_\alpha)$, tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
+% B_G05 literal reworked relation, followed inside the qualifier by its supported complete-state interpretations.
+% Origin (943,1947), 0.25 pt per source pixel, baseline y=43; observed locus (944,1949,999,2004).
+% M01 curved body, M02 middle shaft, M03 thin right head. No additional unqualified membership or arrow is drawn.
+\mathrel{\unsure{\text{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,43)}]
+\path[use as bounding box] (0,0) rectangle (62,66);
+\draw[line width=0.70pt,line cap=round] (45,11) .. controls (35,-1) and (16,17) .. (7,32) .. controls (1,43) and (5,51) .. (15,55) .. controls (23,58) and (32,56) .. (39,51);
+\draw[line width=0.75pt,line cap=round] (4,40) -- (43,32);
+\draw[line width=0.40pt,line cap=round] (35,24) .. controls (38,16) and (51,29) .. (54,36) .. controls (56,34) and (54,20) .. (48,19);
+\end{tikzpicture}}|\deleted{\Rightarrow}\in|\deleted{\to}\in|\in}}
+\pi_0(X\setminus E_\alpha)$, tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
 % archive sheet number: 19

--- A
+++ C
@@ -1,101 +1,73 @@
 \scanpage{20}
-Ainsi les classes de $\Pi_I^{\unsure{\circ|0}}$ sont les classes de $\Pi_J^\circ$ distinctes de $\deleted{\Pi}U_{J,i}$, et de plus les \unsure{clas.|deux.} parmi
+Ainsi les classes de $\Pi_I^{\unsure{\circ|0}}$ sont les classes de $\Pi_J^\circ$ distinctes de $\deleted{\Pi}U_{J,i}$, et de plus les \unsure{deux|clas}. parmi
 \[
-U_{J,i}\cap\Sigma_{\unsure{j|\deleted{J}i|i}}^+,\quad U_{J,i}\cap\Sigma_i^-
+U_{J,i}\cap\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\ U_{J,i}\cap\Sigma_i^-
 \]
-qui sont non vides. Or les deux classes en question sont non vides, car
-% A020-G01: cancelled Sigma with j/i index; glyph and complete cancellation state retained.
-% Fixed source origin (320,817); local pixels right/down; baseline at source y=875.
-% The two slanted cancellation runs are drawn once; the deleted annotation is invisible.
-\begin{tikzpicture}[baseline=(A020G01base.base),x=0.025em,y=-0.025em]
-\useasboundingbox (-2,-5) rectangle (82,85);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G01base) at (1,58)
-{\rlap{$\Sigma_{\unsure{j|i}}$}\phantom{$\deleted{\Sigma_{\unsure{j|i}}}$}};
-\draw[line width=0.35pt] (2,58)--(33,-1);
-\draw[line width=0.35pt] (23,60)--(62,18);
-\end{tikzpicture}
-$U_{J,i}$ est un voisinage
-% A020-G02: gray detached round point, source origin (1175,817), baseline y=817.
-% Shape candidate only; role, hand and surface origin unresolved. No word is in this group.
-\unsure{\begin{tikzpicture}[baseline={(0,0)},x=0.025em,y=-0.025em]
-\useasboundingbox (0,0) rectangle (11,24);
-\fill[gray] (4,18) ellipse [x radius=2.2,y radius=2.5];
-\end{tikzpicture}}
-de $\deleted{\Sigma}E_{\unsure{i|j}}$, et
+qui sont non vides. Or les deux classes en question sont non vides, car $\deleted{\Sigma_{\unsure{j|i}}}$ $U_{J,i}$ est un voisinage de $\deleted{\Sigma}E_i$, et
 \[
 \overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
 \overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
 \]
-On sait donc que le nb des classes est en
-% A020-G03: cancelled tout/est; fixed source origin (1457,1038), baseline y=1081.
-% The observed two crossing runs replace a generic visible cancellation rule.
-\begin{tikzpicture}[baseline=(A020G03base.base),x=0.025em,y=-0.025em]
-\useasboundingbox (-2,-3) rectangle (130,53);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G03base) at (0,43)
-{\rlap{\unsure{tout|est}}\phantom{\deleted{\unsure{tout|est}}}};
-\draw[line width=0.45pt] (0,27)--(30,44);
-\draw[line width=0.35pt] (46,8)--(80,26)..controls (96,34) and (110,40)..(122,41);
-\end{tikzpicture}
-$(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève \unsure{aussi|ainsi} la
-% A020-G04: detached high triangular point after la; source origin (565,1395).
-% Shape candidate only; role, hand and surface origin unresolved. No word is in this group.
-\unsure{\begin{tikzpicture}[baseline={(0,0)},x=0.025em,y=-0.025em]
-\useasboundingbox (0,-33) rectangle (12,0);
-\fill (4,-31)--(7,-26)--(7,-22)--(2,-24)--cycle;
-\end{tikzpicture}}
-\unsure{dém.|dem.} \unsure{par|p} récurrence sur le nb des classes).
+On sait donc que le nb des classes est en \deleted{\unsure{tout|est}} $(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève \unsure{aussi|ainsi} la \unsure{dèm.|dém.|dem.} par récurrence sur le nb des classes).
 
 \uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
-% A020-G05: complete formula and its added hatted label; no other words are in this group.
-% Fixed source origin (1105,1660); local pixels right/down; formula baseline y=1735.
-% The ordinary union operator, index, body, two parentheses and label occur once.
-% The retraced left oval is drawn as the second path, beside the main brace run.
-\figure{\begin{tikzpicture}[baseline=(A020G05body.base),x=0.025em,y=-0.025em]
-\useasboundingbox (-210,-50) rectangle (275,145);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (-205,75)
-{$X\setminus\displaystyle\bigcup_{\alpha\in\deleted{I}K}$};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G05body) at (0,75)
-{$(\Sigma_\alpha^+\cup E_\alpha)$};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (88,-6)
-{$\inserted{\widehat{\Sigma}_\alpha^+}$};
-\draw[line width=0.45pt] (12,20)..controls (42,18) and (60,13)..(82,16)
-..controls (102,18) and (116,17)..(123,15)--(123,6)
-..controls (145,16) and (168,13)..(184,10)
-..controls (211,6) and (240,4)..(247,8)--(250,13);
-\draw[line width=0.45pt] (22,22)..controls (33,13) and (50,10)..(64,16)
-..controls (70,22) and (56,25)..(45,22)
-..controls (36,19) and (29,19)..(22,22);
+% G01--G02: complete word-free union/brace group. Local origin is full-scan
+% (900,1600); x increases right and y down; one local unit is one source pixel.
+% Fixed local rectangle (0,0)--(510,210); baseline is local y=145.
+% The literal U-shaped operator replaces the visible bigcup, which is not
+% drawn a second time. Its annotation identifies that same operator only.
+\figure{\begin{tikzpicture}[x=0.018cm,y=-0.018cm,baseline={(0,145)},every node/.style={anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{18}{20}\selectfont}]
+\path[use as bounding box] (0,0) rectangle (510,210);
+\node at (5,145) {$X$};
+\node at (62,139) {$\setminus$};
+% G01.1: main union bowl and the small closed return at its upper right.
+\draw[line width=1.55pt,line cap=round,line join=round]
+ (126,94) .. controls (128,124) and (136,145) .. (154,146)
+ .. controls (178,150) and (185,130) .. (180,104)
+ .. controls (179,93) and (178,84) .. (174,84)
+ .. controls (169,83) and (170,94) .. (177,100);
+% G01.2: the short visible lower-left retrace of that same bowl.
+\draw[line width=0.45pt,line cap=round]
+ (130,111) .. controls (133,132) and (143,148) .. (157,148);
+\node at (111,191) {$\alpha\in\unsure{\deleted{I}K|K}$};
+\node at (199,145) {$(\Sigma_\alpha^+\cup E_\alpha)$};
+\node at (291,61) {$\inserted{\widehat{\Sigma}_\alpha^+}$};
+% G02.1: complete upper brace, including its central upward step and right hook.
+\draw[line width=0.7pt,line cap=round,line join=round]
+ (217,78) .. controls (241,75) and (269,73) .. (298,74)
+ -- (327,73) -- (328,63)
+ .. controls (346,71) and (367,69) .. (393,64)
+ .. controls (420,59) and (443,59) .. (451,62)
+ .. controls (455,63) and (456,65) .. (457,68);
+% G02.2: the left closed loop and returning dark run are one component.
+\draw[line width=0.9pt,line cap=round,line join=round]
+ (228,80) .. controls (241,70) and (252,69) .. (266,73)
+ .. controls (256,80) and (243,82) .. (239,76)
+ .. controls (261,75) and (288,72) .. (307,74);
 \end{tikzpicture}}
-où $K$ est une partie
-% A020-G06: complete cancelled insertion and curved guide with adjoining de I,.
-% Fixed source origin (1148,1770); local pixels right/down; de I baseline y=1845.
-% Exact word boundary: non vide (inserted and cancelled), de I,; partie and et remain outside.
-% The phantom carries both editorial states without an extra visible generic strike.
-\begin{tikzpicture}[baseline=(A020G06base.base),x=0.025em,y=-0.025em]
-\useasboundingbox (-3,-5) rectangle (255,94);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,31)
-{\rlap{\inserted{non vide}}\phantom{\inserted{\deleted{non vide}}}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G06base) at (48,75) {de $I$,};
-\draw[line width=0.45pt] (0,33)..controls (59,23) and (119,11)..(181,2);
-\draw[line width=0.35pt] (31,74)..controls (25,52) and (55,37)..(105,27)
-..controls (143,19) and (183,13)..(203,15)--(207,19);
-\end{tikzpicture}
+où $K$ est une
+% G03--G04: complete insertion/cancellation/guide group with the adjoining
+% words partie and de I, including the comma exactly once. No et is in it.
+% Local origin full-scan (990,1755), one unit = one source pixel, y down.
+% Fixed rectangle (0,0)--(420,150); baseline local y=110; base-west anchors.
+\figure{\begin{tikzpicture}[x=0.018cm,y=-0.018cm,baseline={(0,110)},every node/.style={anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{15}{17}\selectfont}]
+\path[use as bounding box] (0,0) rectangle (420,150);
+\node at (11,112) {partie};
+\node at (212,90) {de $I$,};
+\node[rotate=10] at (161,47) {\inserted{\rlap{non vide}\phantom{\deleted{non vide}}}};
+% G03: the observed oblique cancellation and its hooked right return.
+\draw[line width=0.85pt,line cap=round,line join=round]
+ (160,48) .. controls (204,41) and (278,23) .. (338,15)
+ -- (334,11) -- (341,17)
+ .. controls (337,25) and (330,31) .. (320,37);
+% G04: the long curved insertion guide begins after partie and spans de I.
+\draw[line width=0.7pt,line cap=round,line join=round]
+ (188,99) .. controls (183,77) and (211,65) .. (253,52)
+ .. controls (287,42) and (325,36) .. (355,32)
+ .. controls (360,32) and (362,33) .. (362,37);
+\end{tikzpicture}}
 et
-% slanted
-\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{19}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}}}\normalmarginpar
-$\forall\alpha\in K$, \deleted{on a} $\Sigma_\alpha^+
-% A020-G07: complete observed reworked membership/arrow shape, source origin (945,1943).
-% Full-state candidates: \deleted{\Rightarrow}\in | \deleted{\to}\in | \in.
-% The primary is the first candidate; the third retains a live/retraced membership state.
-% The phantom records the complete candidates; the local unsure qualifies the actual paths.
-\mathrel{\unsure{\begin{tikzpicture}[baseline={(0,41)},x=0.025em,y=-0.025em]
-\useasboundingbox (-2,-2) rectangle (55,55);
-\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at (0,41)
-{\phantom{$\deleted{\Rightarrow}\in|\deleted{\to}\in|\in$}};
-\draw[line width=0.45pt] (38,4)..controls (24,1) and (1,25)..(1,33)
-..controls (1,48) and (19,51)..(28,47);
-\draw[line width=0.45pt] (2,33)--(41,28);
-\draw[line width=0.35pt] (26,20)--(42,31)..controls (48,32) and (44,18)..(40,16);
-\end{tikzpicture}}}
-\pi_0(X\setminus{\unsure{E|\deleted{\Sigma}E}}_\alpha)$, tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
+% slanted; the complete marginal note is in his hand.
+\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{23}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}}}\normalmarginpar
+$\forall\alpha\in K$, \deleted{on a} $\Sigma_\alpha^+\unsure{\deleted{\Rightarrow}\in|\deleted{\rightarrow}\in|\in}\pi_0(X\setminus E_\alpha)$, tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
 % archive sheet number: 19

--- B
+++ C
@@ -1,78 +1,73 @@
 \scanpage{20}
-Ainsi les classes de $\Pi_I^{\unsure{\circ|0}}$ sont les classes de $\Pi_J^\circ$ distinctes de $\deleted{\Pi}U_{J,i}$, et de plus les \unsure{clas.|deux.} parmi
+Ainsi les classes de $\Pi_I^{\unsure{\circ|0}}$ sont les classes de $\Pi_J^\circ$ distinctes de $\deleted{\Pi}U_{J,i}$, et de plus les \unsure{deux|clas}. parmi
 \[
-U_{J,i}\cap\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\quad U_{J,i}\cap\Sigma_i^-
+U_{J,i}\cap\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\ U_{J,i}\cap\Sigma_i^-
 \]
-qui sont non vides. Or les deux classes en question sont non vides, car
-% B_G01: cancelled Sigma and its two visible crossing runs. Observed locus (320,810,403,900).
-% Source origin (315,803); x right, y down; 0.25 pt per source pixel. Baseline y=76.
-% The visible node occurs once; its phantom carries the deletion state without a generic extra rule.
-\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,76)}]
-\path[use as bounding box] (0,0) rectangle (95,100);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,76) {\rlap{$\unsure{\Sigma_j|\Sigma_i}$}\phantom{\deleted{$\unsure{\Sigma_j|\Sigma_i}$}}};
-\draw[line width=0.45pt,line cap=round] (10,73) .. controls (20,54) and (30,31) .. (40,12);
-\draw[line width=0.45pt,line cap=round] (45,73) .. controls (43,80) and (49,82) .. (54,76) -- (69,35);
-\end{tikzpicture}
-$U_{J,i}$ est un voisinage de $\deleted{\Sigma}E_{\unsure{i|j}}$, et
+qui sont non vides. Or les deux classes en question sont non vides, car $\deleted{\Sigma_{\unsure{j|i}}}$ $U_{J,i}$ est un voisinage de $\deleted{\Sigma}E_i$, et
 \[
 \overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
 \overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
 \]
-On sait donc que le nb des classes est en \deleted{\unsure{tout|est}} $(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève \unsure{aussi|ainsi}
-% B_G02: complete word-bearing group la and one qualified detached point above/right.
-% Origin (500,1347), 0.25 pt per source pixel, baseline y=49. Observed point locus (566,1363,575,1373).
-% Inner graphic origin is explicitly translated by (66,18); base-west anchor and baseline (0,0) fix its placement.
-\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline=(Bla.base)]
-\path[use as bounding box] (0,0) rectangle (88,62);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (Bla) at (0,49) {la};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (66,18) {\unsure{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,0)}]
-\path[use as bounding box] (0,0) rectangle (7,8);
-\fill (2,0) -- (5,4) -- (4,7) -- (1,6) -- cycle;
-\end{tikzpicture}}};
-\end{tikzpicture}
-\unsure{dèm.|dém.|dem.} par récurrence sur le nb des classes).
+On sait donc que le nb des classes est en \deleted{\unsure{tout|est}} $(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève \unsure{aussi|ainsi} la \unsure{dèm.|dém.|dem.} par récurrence sur le nb des classes).
 
 \uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
-% B_G03: union, complete parenthesized expression, overwritten limit, raised hatted Sigma, and literal brace.
-% Origin (1010,1600), 0.25 pt per source pixel, baseline y=140; fixed drawing rectangle (0,15)-(390,200).
-% Pi above and X setminus to the left are outside this group. No generic bigcup or overbrace is also drawn.
-$X\setminus\text{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,140)}]
-\path[use as bounding box] (0,15) rectangle (390,200);
-% U01 body; U02 upper-right loop; U03 pale lower retrace.
-\draw[line width=0.95pt,line cap=round] (17,90) .. controls (17,122) and (24,140) .. (45,142) .. controls (63,142) and (72,133) .. (71,115) -- (68,87);
-\draw[line width=0.55pt,line cap=round] (68,87) .. controls (66,77) and (63,81) .. (64,89) .. controls (65,96) and (68,99) .. (68,104);
-\draw[black!55,line width=0.45pt,line cap=round] (19,114) .. controls (23,140) and (51,150) .. (65,133);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small] at (0,190) {$\alpha\in\unsure{\deleted{I}K|K}$};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small] at (91,140) {$(\Sigma_\alpha^+\cup E_\alpha)$};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\scriptsize] at (184,58) {$\inserted{\widehat{\Sigma}_\alpha^+}$};
-% BR01 main run and central turn; BR02 closed left loop; BR03 left retrace.
-\draw[line width=0.65pt,line cap=round] (108,79) .. controls (132,75) and (151,71) .. (180,74) .. controls (193,75) and (204,70) .. (217,72) -- (220,62) .. controls (234,70) and (256,68) .. (287,64) .. controls (307,60) and (326,59) .. (339,62) .. controls (344,63) and (345,66) .. (345,69);
-\draw[line width=0.55pt,line cap=round] (132,76) .. controls (141,68) and (160,69) .. (164,74) .. controls (153,81) and (142,82) .. (132,76);
-\draw[line width=0.85pt,line cap=round] (120,80) .. controls (145,74) and (178,73) .. (210,74);
-\end{tikzpicture}}$
+% G01--G02: complete word-free union/brace group. Local origin is full-scan
+% (900,1600); x increases right and y down; one local unit is one source pixel.
+% Fixed local rectangle (0,0)--(510,210); baseline is local y=145.
+% The literal U-shaped operator replaces the visible bigcup, which is not
+% drawn a second time. Its annotation identifies that same operator only.
+\figure{\begin{tikzpicture}[x=0.018cm,y=-0.018cm,baseline={(0,145)},every node/.style={anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{18}{20}\selectfont}]
+\path[use as bounding box] (0,0) rectangle (510,210);
+\node at (5,145) {$X$};
+\node at (62,139) {$\setminus$};
+% G01.1: main union bowl and the small closed return at its upper right.
+\draw[line width=1.55pt,line cap=round,line join=round]
+ (126,94) .. controls (128,124) and (136,145) .. (154,146)
+ .. controls (178,150) and (185,130) .. (180,104)
+ .. controls (179,93) and (178,84) .. (174,84)
+ .. controls (169,83) and (170,94) .. (177,100);
+% G01.2: the short visible lower-left retrace of that same bowl.
+\draw[line width=0.45pt,line cap=round]
+ (130,111) .. controls (133,132) and (143,148) .. (157,148);
+\node at (111,191) {$\alpha\in\unsure{\deleted{I}K|K}$};
+\node at (199,145) {$(\Sigma_\alpha^+\cup E_\alpha)$};
+\node at (291,61) {$\inserted{\widehat{\Sigma}_\alpha^+}$};
+% G02.1: complete upper brace, including its central upward step and right hook.
+\draw[line width=0.7pt,line cap=round,line join=round]
+ (217,78) .. controls (241,75) and (269,73) .. (298,74)
+ -- (327,73) -- (328,63)
+ .. controls (346,71) and (367,69) .. (393,64)
+ .. controls (420,59) and (443,59) .. (451,62)
+ .. controls (455,63) and (456,65) .. (457,68);
+% G02.2: the left closed loop and returning dark run are one component.
+\draw[line width=0.9pt,line cap=round,line join=round]
+ (228,80) .. controls (241,70) and (252,69) .. (266,73)
+ .. controls (256,80) and (243,82) .. (239,76)
+ .. controls (261,75) and (288,72) .. (307,74);
+\end{tikzpicture}}
 où $K$ est une
-% B_G04 contains exactly partie, the inserted/deleted non vide, and de I, et.
-% Source origin (997,1750), 0.25 pt per source pixel, baseline y=110. Fixed rectangle (0,0)-(530,160).
-% NV01 is the rising cancellation run with its right return. NV02 is the separate curved insertion guide.
-\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,110)}]
-\path[use as bounding box] (0,0) rectangle (530,160);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,115) {partie};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small,rotate=8] at (157,45) {\inserted{\rlap{non vide}\phantom{\deleted{non vide}}}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (200,89) {de $I$, et};
-\draw[line width=0.55pt,line cap=round] (154,53) .. controls (203,44) and (282,30) .. (331,24) .. controls (331,31) and (325,37) .. (315,43);
-\draw[line width=0.45pt,line cap=round] (182,94) .. controls (172,61) and (272,47) .. (339,40) .. controls (346,39) and (351,39) .. (355,43);
-\end{tikzpicture}
-% slanted; the two written conditions have no punctuation between them.
-\reversemarginpar\margin{\begin{tikzpicture}\node[rotate=19,anchor=base west,inner sep=0pt,outer sep=0pt] {\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}};\end{tikzpicture}}\normalmarginpar
-$\forall\alpha\in K$, \deleted{on a} $\Sigma_\alpha^+
-% B_G05 literal reworked relation, followed inside the qualifier by its supported complete-state interpretations.
-% Origin (943,1947), 0.25 pt per source pixel, baseline y=43; observed locus (944,1949,999,2004).
-% M01 curved body, M02 middle shaft, M03 thin right head. No additional unqualified membership or arrow is drawn.
-\mathrel{\unsure{\text{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,43)}]
-\path[use as bounding box] (0,0) rectangle (62,66);
-\draw[line width=0.70pt,line cap=round] (45,11) .. controls (35,-1) and (16,17) .. (7,32) .. controls (1,43) and (5,51) .. (15,55) .. controls (23,58) and (32,56) .. (39,51);
-\draw[line width=0.75pt,line cap=round] (4,40) -- (43,32);
-\draw[line width=0.40pt,line cap=round] (35,24) .. controls (38,16) and (51,29) .. (54,36) .. controls (56,34) and (54,20) .. (48,19);
-\end{tikzpicture}}|\deleted{\Rightarrow}\in|\deleted{\to}\in|\in}}
-\pi_0(X\setminus E_\alpha)$, tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
+% G03--G04: complete insertion/cancellation/guide group with the adjoining
+% words partie and de I, including the comma exactly once. No et is in it.
+% Local origin full-scan (990,1755), one unit = one source pixel, y down.
+% Fixed rectangle (0,0)--(420,150); baseline local y=110; base-west anchors.
+\figure{\begin{tikzpicture}[x=0.018cm,y=-0.018cm,baseline={(0,110)},every node/.style={anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{15}{17}\selectfont}]
+\path[use as bounding box] (0,0) rectangle (420,150);
+\node at (11,112) {partie};
+\node at (212,90) {de $I$,};
+\node[rotate=10] at (161,47) {\inserted{\rlap{non vide}\phantom{\deleted{non vide}}}};
+% G03: the observed oblique cancellation and its hooked right return.
+\draw[line width=0.85pt,line cap=round,line join=round]
+ (160,48) .. controls (204,41) and (278,23) .. (338,15)
+ -- (334,11) -- (341,17)
+ .. controls (337,25) and (330,31) .. (320,37);
+% G04: the long curved insertion guide begins after partie and spans de I.
+\draw[line width=0.7pt,line cap=round,line join=round]
+ (188,99) .. controls (183,77) and (211,65) .. (253,52)
+ .. controls (287,42) and (325,36) .. (355,32)
+ .. controls (360,32) and (362,33) .. (362,37);
+\end{tikzpicture}}
+et
+% slanted; the complete marginal note is in his hand.
+\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{23}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}}}\normalmarginpar
+$\forall\alpha\in K$, \deleted{on a} $\Sigma_\alpha^+\unsure{\deleted{\Rightarrow}\in|\deleted{\rightarrow}\in|\in}\pi_0(X\setminus E_\alpha)$, tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
 % archive sheet number: 19
