## Reader A

\scanpage{17}
\uline{Cas particuliers}

Supposons que $\forall i\in I$, \deleted{$E_i$ \unsure{est|soit} rare dans $X$.} \inserted{on ait} (si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)

\deleted{Alors on trouve que}
\[
\begin{aligned}
\overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\
\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i .
\end{aligned}
\]

Alors je dis qu'on a
\[
\overline{\Sigma_{12}}=\Sigma_{12}
% G01: retraced cup; full-scan origin (944,783), fixed local rectangle 36 by 36.
\mathbin{\vcenter{\hbox{\begin{tikzpicture}[x=0.007cm,y=-0.007cm,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (36,36);
\draw[line width=0.55pt,line cap=round,line join=round] (7,5) .. controls (7,13) and (7,21) .. (9,25) .. controls (18,33) and (32,30) .. (32,14) -- (30,7);
\draw[line width=0.4pt,line cap=round,line join=round] (25,7) .. controls (32,20) and (20,32) .. (8,25);
\end{tikzpicture}}}} E_1\cup E_2
\]

% G02: short curved separator with downturned right endpoint.
% Full-scan origin (300,887); fixed local rectangle 240 by 22.
\figure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (240,22);
\draw[line width=0.3pt,line cap=round] (2,14) .. controls (70,5) and (181,4) .. (232,8) .. controls (238,9) and (239,10) .. (238,14);
\end{tikzpicture}}

% slanted
\reversemarginpar
\margin{introduire la partition $\unsure{\Pi|\pi}_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$}
\normalmarginpar
\deleted{Supposons}

Soit $J\subset I$ tel que $I=J\amalg\{i\}$.

Considerons la partition
% G03: upper Pi_J insertion and curved guide. Source origin (1215,1100).
% Fixed rectangle 175 by 135; base-west anchors and zero node separations.
\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(pide.base)]
\path[use as bounding box] (0,0) rectangle (175,135);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (6,65) {\inserted{$\Pi_J$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (pide) at (105,124) {de};
\draw[line width=0.3pt,line cap=round] (68,120) .. controls (73,91) and (129,99) .. (153,84) -- (152,79);
\end{tikzpicture}
$X$ \deleted{definie} definie par les $\deleted{\Sigma}E_j$ $(j\in J)$, \deleted{et} \unsure{Intersection|intersection} des partitions
% G04: ternaires Pi_j insertion and its long bent caret. Source origin (970,1345).
\begin{tikzpicture}[x=0.0075cm,y=-0.0075cm,baseline=(terde.base)]
\path[use as bounding box] (0,0) rectangle (335,135);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,57) {\inserted{ternaires $\Pi_j$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (terde) at (270,118) {de};
\draw[line width=0.35pt,line cap=round,line join=round] (161,64) .. controls (177,65) and (206,70) .. (215,89) -- (218,105) .. controls (233,80) and (246,62) .. (260,48);
\end{tikzpicture}
$X$ $(j\in J)$ definies par les $E_j$ \deleted{$\unsure{\in|E}$} $(j\in J)$
\[
X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}\Sigma_j^{\unsure{\prime|\cdot}\alpha}
\]
% G05 is the small detached oblique mark immediately before upper alpha.
% It is represented once by the qualified prime/dot candidate above; no role is assigned.

% G11: two detached marks at far right between display and lower prose.
% Full-scan origin (1567,1735), fixed local rectangle 18 by 20.
% Shapes only: character, role, hand and surface origin remain unestablished.
\margin{\unsure{\begin{tikzpicture}[x=0.02cm,y=-0.02cm,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (18,20);
\fill (9,5) .. controls (11,4) and (13,6) .. (11,9) .. controls (8,10) and (8,7) .. cycle;
\fill (4,12) .. controls (7,11) and (8,14) .. (5,15) .. controls (3,16) and (2,13) .. cycle;
\end{tikzpicture}}}

-- c'est aussi la partition definie par celle de $\displaystyle\unsure{.}\,\bigcup_{j\in J}E_j$ en les $E_j$, et la partition
% G06 is the detached baseline point before the first indexed union, represented once above.
% G07: lower Pi_J insertion and curved guide. Source origin (770,1965).
\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=(lowde.base)]
\path[use as bounding box] (0,0) rectangle (145,100);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,54) {\inserted{$\Pi_J^{\unsure{\circ|0}}$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (lowde) at (69,85) {de};
\draw[line width=0.3pt,line cap=round] (39,89) .. controls (40,65) and (55,62) .. (76,56) .. controls (93,51) and (119,40) .. (122,34) -- (118,30);
\end{tikzpicture}
$\displaystyle X\setminus
% G08: union with visible transverse stroke; interpretation of stroke stays qualified.
% Full-scan origin (1115,1970), fixed local rectangle 80 by 75.
\mathop{\unsure{\vcenter{\hbox{\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (80,75);
\draw[line width=0.45pt,line cap=round] (18,9) .. controls (13,34) and (18,60) .. (38,63) .. controls (61,67) and (70,39) .. (63,10);
\draw[line width=0.4pt,line cap=round] (12,20) .. controls (26,20) and (39,17) .. (59,18);
\end{tikzpicture}}}}}\limits_{j\in J}E_j$
intersection des partitions binaires $\Pi_{J,j}^{\circ}$
% G09: inserted quantifier and guide over induites. Source origin (1230,2070).
% The recurring circle/zero doubt is marked at its first occurrence above.
\begin{tikzpicture}[x=0.0075cm,y=-0.0075cm,baseline=(induites.base)]
\path[use as bounding box] (0,0) rectangle (335,115);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (60,45) {\inserted{$(j\in J)$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (induites) at (52,91) {induites};
\draw[line width=0.3pt,line cap=round] (14,92) .. controls (0,72) and (30,57) .. (53,53) .. controls (99,66) and (189,54) .. (219,41) .. controls (224,39) and (216,32) .. (214,31);
\end{tikzpicture}
% G10: inserted U_J= and guide curling down to the right of sur.
% Full-scan origin (320,2155); fixed local rectangle 145 by 155.
\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(sur.base)]
\path[use as bounding box] (0,0) rectangle (145,155);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (43,61) {\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (sur) at (0,111) {sur};
\draw[line width=0.3pt,line cap=round] (56,72) .. controls (88,81) and (111,74) .. (124,99) .. controls (133,121) and (132,138) .. (136,148);
\end{tikzpicture}
$\displaystyle X\setminus\bigcup_{j\in J}E_j$ par les $\Pi_j$ $(\unsure{g|j}\in J)$. Pour
% archive sheet number: 16



{
  "differences": [
    {
      "id": "A017-D01",
      "location": "Deleted first supposition: subject",
      "C": "\\unsure{E_i|\\Sigma_i}",
      "H": "E_i",
      "reading": "E_i",
      "evidence": "A left vertical and three separate horizontal levels survive the crossing strokes; the lowered i is retained.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "01_upper_correction.png",
      "bbox": [
        1040,
        213,
        1146,
        282
      ],
      "C_source_row": "R01",
      "C_local_part": "subject E_i versus Sigma_i"
    },
    {
      "id": "A017-D02",
      "location": "Deleted first supposition: verb",
      "C": "\\unsure{est}",
      "H": "soit",
      "reading": "\\unsure{est|soit}",
      "evidence": "A short low run and final tall crossed stem support est first; the densely crossed middle does not settle the competing soit reading. H remains an explicit alternative, not a conclusively excluded reading.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "01_upper_correction.png",
      "bbox": [
        1112,
        226,
        1247,
        277
      ],
      "C_source_row": "R01",
      "C_local_part": "verb est"
    },
    {
      "id": "A017-D03",
      "location": "Deleted first supposition: adjective",
      "C": "\\unsure{rare|dense}",
      "H": "rare",
      "reading": "rare",
      "evidence": "Two short r-like shoulders with an intervening low rounded a and terminal e survive; no distinct initial tall d is visible in this word.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "01_upper_correction.png",
      "bbox": [
        1248,
        238,
        1400,
        280
      ],
      "C_source_row": "R01",
      "C_local_part": "adjective rare versus dense"
    },
    {
      "id": "A017-D04",
      "location": "Parenthesis following on ait",
      "C": "si",
      "H": "où",
      "reading": "si",
      "evidence": "The small s loop and separate i stroke are visible immediately after the opening parenthesis.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "01_upper_correction.png",
      "bbox": [
        1395,
        184,
        1477,
        242
      ]
    },
    {
      "id": "A017-D05",
      "location": "End of deleted first sentence",
      "C": "X.",
      "H": "X",
      "reading": "X.",
      "evidence": "A distinct dark point follows the crossed X.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "01_upper_correction.png",
      "bbox": [
        1530,
        236,
        1614,
        288
      ]
    },
    {
      "id": "A017-D06",
      "location": "Raised on ait",
      "C": "\\inserted{on ait}",
      "H": "on ait",
      "reading": "\\inserted{on ait}",
      "evidence": "The words sit above the cancelled clause, with a clear vertical displacement.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "01_upper_correction.png",
      "bbox": [
        1134,
        186,
        1343,
        236
      ]
    },
    {
      "id": "A017-D07",
      "location": "Cancelled sentence before two equalities",
      "C": "\\unsure{trouve}",
      "H": "trouve",
      "reading": "trouve",
      "evidence": "The tall initial t, short following shoulder, low round/return strokes and final e-like return remain visible beneath the long cancellation line.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "02_struck_sentence.png",
      "bbox": [
        553,
        328,
        732,
        381
      ],
      "C_source_row": "R02",
      "C_local_part": "trouve"
    },
    {
      "id": "A017-D08",
      "location": "First equality endpoint after E_i",
      "C": "no comma",
      "H": "E_i,",
      "reading": "no comma",
      "evidence": "The index has its dot and stem; the area immediately to its right contains no comma. The separate point beside the second equality is retained as that equality's endpoint.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "03_equation_endpoints.png",
      "bbox": [
        940,
        425,
        1080,
        495
      ]
    },
    {
      "id": "A017-D09",
      "location": "Sentence before third equality",
      "C": "Alors je dis qu'on a",
      "H": "Alors je dis que",
      "reading": "Alors je dis qu'on a",
      "evidence": "The half shows an apostrophe after qu, the low on run, and a separate small final a oval.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "image": "half a",
        "origin": "upper left",
        "box": [
          300,
          620,
          1000,
          776
        ]
      }
    },
    {
      "id": "A017-D10",
      "location": "First join of Sigma12 equality",
      "C": "\\unsure{\\cup|\\amalg}",
      "H": "\\cup",
      "reading": "cup form with doubled curved right return, drawn as G01",
      "evidence": "Both surviving bottoms curve upward into the right arms. Two distinct right returns are present. The cup reading is selected; the extra return is drawn without assigning a correction chronology.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "04_first_join.png",
      "bbox": [
        944,
        783,
        980,
        819
      ],
      "C_source_row": "R03",
      "C_local_part": "first join",
      "physical_cluster": "G01",
      "shape_confidence": "high",
      "role_of_retracing": "unestablished"
    },
    {
      "id": "A017-D11",
      "location": "Separator below third equality",
      "C": "\\rule{2.4cm}{0.3pt}",
      "H": "omitted",
      "reading": "G02: shallow curved rule with downturned right endpoint",
      "evidence": "The half shows a shallow rise across the rule and a small downward turn at the right end.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "image": "half a",
        "origin": "upper left",
        "box": [
          297,
          884,
          543,
          910
        ]
      },
      "physical_cluster": "G02"
    },
    {
      "id": "A017-D12",
      "location": "Opening of slanted margin note",
      "C": "introduire",
      "H": "introduisons",
      "reading": "introduire",
      "evidence": "After introdui the surviving short shoulder and low terminal return support re; the longer sons ending is not written.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "05_margin_note.png",
      "bbox": [
        39,
        943,
        260,
        1115
      ]
    },
    {
      "id": "A017-D13",
      "location": "Slanted margin partition name",
      "C": "\\unsure{\\Pi|\\pi}_j",
      "H": "\\Pi_j",
      "reading": "\\unsure{\\Pi|\\pi}_j",
      "evidence": "A connected top and two legs are visible. The local capital/lowercase scale remains insufficiently distinct.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "05_margin_note.png",
      "bbox": [
        31,
        1217,
        111,
        1321
      ],
      "C_source_row": "R04",
      "C_local_part": "Pi versus pi"
    },
    {
      "id": "A017-D14",
      "location": "Cancelled predecessor within marginal E_j",
      "C": "\\deleted{\\unsure{\\Sigma}}E_j",
      "H": "E_j ... \\ill{}",
      "reading": "\\deleted{\\unsure{\\Sigma}}E_j",
      "evidence": "Angular dark remnants are superimposed on E. Sigma remains the supported but uncertain predecessor. The inspected note ends at its closing brace; H's trailing ill is not assigned an invented extra word. This is the single H placeholder/cancellation cluster for this note.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "05_margin_note.png",
      "bbox": [
        132,
        1146,
        190,
        1206
      ],
      "C_source_row": "R04",
      "C_local_part": "crossed Sigma",
      "H_parent": "H-MARGIN-ILL"
    },
    {
      "id": "A017-D15",
      "location": "Start of main lower paragraph",
      "C": "Considérons",
      "H": "Considérons",
      "reading": "Considerons",
      "evidence": "The entire word and the area above its e are visible; no detached acute stroke is present.",
      "confidence": "high",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "17_considerons.png",
      "bbox": [
        315,
        1148,
        713,
        1222
      ]
    },
    {
      "id": "A017-D16",
      "location": "Upper Pi_J insertion over de",
      "C": "\\inserted{\\Pi_J} de",
      "H": "\\add{\\Pi_J} de",
      "reading": "same words with literal guide G03",
      "evidence": "The half shows a separate curved stroke rising from the gap before de toward an upturned right endpoint below the raised name. The insertion state itself agrees with both witnesses.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "image": "half a",
        "origin": "upper left",
        "box": [
          1215,
          1100,
          1390,
          1235
        ]
      },
      "physical_cluster": "G03"
    },
    {
      "id": "A017-D17",
      "location": "Cancelled word following de X",
      "C": "\\deleted{\\unsure{des parties|définie}}",
      "H": "\\struck{définie}",
      "reading": "\\deleted{definie}",
      "evidence": "The cancelled word begins d-e followed by one tall descending f and the short i/n/i/e continuation. There is no detached acute above e. The live following word has its own separate strokes.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "06_cancelled_definie.png",
      "bbox": [
        420,
        1263,
        650,
        1388
      ],
      "C_source_row": "R05",
      "C_local_part": "cancelled wording"
    },
    {
      "id": "A017-D18",
      "location": "Live word after cancelled definie",
      "C": "définie",
      "H": "définie",
      "reading": "definie",
      "evidence": "The low e between d and the tall f has blank space above it, with no separate acute.",
      "confidence": "high",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "06_cancelled_definie.png",
      "bbox": [
        682,
        1260,
        884,
        1370
      ]
    },
    {
      "id": "A017-D19",
      "location": "Predecessor beneath first E_j after les",
      "C": "\\deleted{\\Sigma}E_j",
      "H": "E_j",
      "reading": "\\deleted{\\Sigma}E_j",
      "evidence": "The diagonal middle and returning lower limb of Sigma remain beneath the E bars; a separate diagonal crosses this cluster. C's doubt-table row qualifies this locus although C.tex has no unsure macro here.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "07_first_E_predecessor.png",
      "bbox": [
        1283,
        1277,
        1366,
        1379
      ],
      "C_source_row": "R07",
      "C_local_part": "first predecessor Sigma"
    },
    {
      "id": "A017-D20",
      "location": "Cancelled opening before intersection",
      "C": "\\deleted{\\unsure{et}}",
      "H": "\\struck{intersection}\\add{intersection}",
      "reading": "\\deleted{et}",
      "evidence": "A small e followed by a tall t survives under the short low crossing. One following continuous word is visible. This H correction cluster is counted here once; its live word qualification is D21.",
      "confidence": "medium",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "08_intersection_start.png",
      "bbox": [
        327,
        1428,
        406,
        1484
      ],
      "C_source_row": "R06",
      "C_local_part": "et",
      "H_parent": "H-INTERSECTION-CLUSTER"
    },
    {
      "id": "A017-D21",
      "location": "Live word following cancelled et",
      "C": "\\unsure{intersection}",
      "H": "\\struck{intersection}\\add{intersection}",
      "reading": "\\unsure{Intersection|intersection}",
      "evidence": "The leading stroke rises well above the low bodies and has no separable initial i dot. The remainder supports intersection. Capital I is selected with lowercase retained; the opening remains crowded. H's duplication/insertion state is collated once in D20.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "08_intersection_start.png",
      "bbox": [
        400,
        1409,
        652,
        1487
      ],
      "C_source_row": "R06",
      "C_local_part": "intersection",
      "H_parent": "H-INTERSECTION-CLUSTER"
    },
    {
      "id": "A017-D22",
      "location": "Guide beneath inserted ternaires Pi_j",
      "C": "\\inserted{ternaires \\Pi_j}",
      "H": "\\add{ternaires \\Pi_j}",
      "reading": "same insertion plus G04 bent caret",
      "evidence": "The lower half shows a low curved left arm descending into a long pointed caret and a rising right arm. Both endpoints are visible.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "image": "half b",
        "origin": "upper left",
        "box": [
          970,
          244,
          1305,
          394
        ]
      },
      "physical_cluster": "G04"
    },
    {
      "id": "A017-D23",
      "location": "Plural defined word before second E_j",
      "C": "définies",
      "H": "définies",
      "reading": "definies",
      "evidence": "Both i dots and the ending are visible. The region above the e before f has no acute.",
      "confidence": "high",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "18_definies.png",
      "bbox": [
        550,
        1519,
        730,
        1616
      ]
    },
    {
      "id": "A017-D24",
      "location": "Cancelled isolated sign after later E_j",
      "C": "\\deleted{\\unsure{E|\\in}}",
      "H": "\\ill{}",
      "reading": "\\deleted{\\unsure{\\in|E}}",
      "evidence": "Two curved lobes with an open right side lie beneath a rising cancelling slash. Membership is the stronger candidate; E survives as an alternative.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "09_later_cancelled_sign.png",
      "bbox": [
        1181,
        1507,
        1217,
        1584
      ],
      "C_source_row": "R07",
      "C_local_part": "later isolated E/in",
      "H_parent": "H-LATER-SIGN-ILL"
    },
    {
      "id": "A017-D25",
      "location": "Small upper mark before alpha in partition display",
      "C": "omitted",
      "H": "omitted",
      "reading": "\\Sigma_j^{\\unsure{\\prime|\\cdot}\\alpha}",
      "evidence": "A short dark detached oblique dab lies between the Sigma head endpoint and alpha. Its shape supports prime/dot candidates; hand, origin and role are unestablished. It is represented once at its observed upper position.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "10_partition_display.png",
      "bbox": [
        1190,
        1624,
        1200,
        1636
      ],
      "physical_cluster": "G05",
      "shape_confidence": "high"
    },
    {
      "id": "A017-D26",
      "location": "Final defined word in c'est aussi paragraph",
      "C": "définie",
      "H": "définie",
      "reading": "definie",
      "evidence": "The enlarged word shows d-e-f and both i dots; there is no detached acute over e.",
      "confidence": "high",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "19_last_definie.png",
      "bbox": [
        1116,
        1745,
        1298,
        1826
      ]
    },
    {
      "id": "A017-D27",
      "location": "Detached baseline point before first large union",
      "C": "omitted",
      "H": "omitted",
      "reading": "\\unsure{.}\\,\\bigcup_{j\\in J}E_j",
      "evidence": "A compact dark horizontal point sits to the left of the cup near its lower baseline. No connection or mathematical role is supplied. Hand and surface origin remain undetermined.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "11_first_union_dot.png",
      "bbox": [
        734,
        1899,
        743,
        1907
      ],
      "physical_cluster": "G06",
      "shape_confidence": "high"
    },
    {
      "id": "A017-D28",
      "location": "Inserted Pi_J upper ring",
      "C": "\\Pi_J^{\\unsure{\\circ|0}}",
      "H": "\\Pi_J^0",
      "reading": "\\Pi_J^{\\unsure{\\circ|0}}",
      "evidence": "A small raised nearly round open-centred loop is visible. Its circular shape alone leaves circle/zero unresolved. H's zero is retained explicitly as the alternative.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "12_inserted_partition_ring.png",
      "bbox": [
        831,
        1974,
        854,
        1996
      ],
      "C_source_row": "R08",
      "C_local_part": "inserted Pi_J upper ring"
    },
    {
      "id": "A017-D29",
      "location": "Guide beneath inserted lower Pi_J",
      "C": "\\inserted{\\Pi_J^{\\circ|0}} de",
      "H": "\\add{\\Pi_J^0} de",
      "reading": "same wording and ring qualification with guide G07",
      "evidence": "A long independent curved stroke begins before de, rises beneath the inserted name and ends with a short upward hook at the right.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "12_inserted_partition_ring.png",
      "bbox": [
        805,
        1991,
        897,
        2059
      ],
      "physical_cluster": "G07"
    },
    {
      "id": "A017-D30",
      "location": "Middle large union after X complement",
      "C": "\\unsure{\\overline{\\bigcup}|\\bigcup}",
      "H": "\\bigcup",
      "reading": "G08: visible cup plus short transverse stroke; role locally qualified",
      "evidence": "The horizontal crosses the left stem below its top and ends before the right stem. Its presence is resolved. Its interpretation as an overbar or another stroke remains unestablished, so the literal two-path graphic is qualified locally.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "13_middle_union.png",
      "bbox": [
        1121,
        1974,
        1188,
        2040
      ],
      "C_source_row": "R11",
      "C_local_part": "bar presence",
      "physical_cluster": "G08",
      "interpretation_confidence": "low"
    },
    {
      "id": "A017-D31",
      "location": "Binary partition name upper ring",
      "C": "\\Pi_{J,j}^{\\circ}",
      "H": "\\Pi_{J,j}^0",
      "reading": "\\Pi_{J,j}^{\\circ} (circle/zero qualification inherited from first occurrence)",
      "evidence": "The separate small raised ring has an open centre. The same circle/zero uncertainty persists at this independently inspected occurrence. C's source R08 explicitly includes it despite no unsure macro here.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "14_binary_partition_guide.png",
      "bbox": [
        1185,
        2125,
        1209,
        2148
      ],
      "C_source_row": "R08",
      "C_local_part": "binary partition name ring"
    },
    {
      "id": "A017-D32",
      "location": "Inserted quantifier and apparent opening parenthesis at induites",
      "C": "\\inserted{(j\\in J)} induites",
      "H": "\\add{(j\\in J)} (induites",
      "reading": "inserted quantifier and induites with G09 guide; no prose opening parenthesis",
      "evidence": "The putative left parenthesis continues upward into one long curved rule under the added quantifier, terminating in a small upturned right hook. The complete path is preserved.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "14_binary_partition_guide.png",
      "bbox": [
        1233,
        2101,
        1461,
        2170
      ],
      "physical_cluster": "G09"
    },
    {
      "id": "A017-D33",
      "location": "U subscript: predecessor and replacement state",
      "C": "U_{\\deleted{\\unsure{J|j}}J}",
      "H": "U_J",
      "reading": "U_{\\unsure{\\deleted{J}J|\\deleted{j}J|J}}",
      "evidence": "Two displaced lower feet are visible with one heavier final right stem and upper bar. The predecessor supports J/j; the strokes also leave one retraced J as a complete-state alternative. No writing chronology is inferred. H's J remains an explicit complete-state alternative.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "15_U_subscript.png",
      "bbox": [
        390,
        2179,
        424,
        2233
      ],
      "C_source_row": "R12",
      "C_local_part": "predecessor J versus j and state",
      "physical_cluster": "U-SUBSCRIPT"
    },
    {
      "id": "A017-D34",
      "location": "U subscript: final capital J",
      "C": "J",
      "H": "J",
      "reading": "J in all selected complete-state alternatives",
      "evidence": "The final heavier stem has a horizontal top and left-returning foot. This confirmation is separate from the predecessor/state doubt and makes no additional witness change.",
      "confidence": "high",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "15_U_subscript.png",
      "bbox": [
        396,
        2184,
        425,
        2233
      ],
      "C_source_row": "R12",
      "C_local_part": "final J",
      "physical_cluster": "U-SUBSCRIPT"
    },
    {
      "id": "A017-D35",
      "location": "U_J equals insertion and guide around sur",
      "C": "\\inserted{U_J={}}",
      "H": "U_J=",
      "reading": "insertion retained, with literal G10 guide",
      "evidence": "The name and equality are raised above sur. A separate line runs below the name and curves down to the right of sur; its entire endpoint is included in the crop. H prints the name at the baseline.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "15_U_subscript.png",
      "bbox": [
        359,
        2159,
        460,
        2307
      ],
      "physical_cluster": "G10"
    },
    {
      "id": "A017-D36",
      "location": "Final quantified letter",
      "C": "\\unsure{g|j}",
      "H": "j",
      "reading": "\\unsure{g|j}",
      "evidence": "A small closed upper loop is followed by a long descending stem and leftward foot. The loop supports g first; j remains possible in the crowded joining strokes. H's j is expressly retained as an alternative.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "16_final_words.png",
      "bbox": [
        1251,
        2241,
        1289,
        2312
      ],
      "C_source_row": "R09",
      "C_local_part": "g versus j"
    },
    {
      "id": "A017-D37",
      "location": "Final parenthesis count",
      "C": "(g|j\\in J).",
      "H": "(j\\in J)).",
      "reading": "(\\unsure{g|j}\\in J).",
      "evidence": "One closing curve and a separate full stop follow J. There is no second closing curve. The guide misread as an opening parenthesis is recorded separately in D32.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "16_final_words.png",
      "bbox": [
        1378,
        2218,
        1461,
        2295
      ]
    },
    {
      "id": "A017-D38",
      "location": "Final word",
      "C": "\\unsure{Pour|Puis}",
      "H": "\\uncertain{Pour}",
      "reading": "Pour",
      "evidence": "The P is followed by a small round o reduced to a dark point and a low u/r run. There is no raised dot for an internal i. The decision uses this page alone; the witness's next-sheet argument is not used.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "16_final_words.png",
      "bbox": [
        1500,
        2214,
        1641,
        2293
      ],
      "C_source_row": "R10",
      "C_local_part": "Pour versus Puis"
    },
    {
      "id": "A017-D39",
      "location": "Far right between partition display and final paragraph",
      "C": "omitted",
      "H": "omitted",
      "reading": "G11: two separate dark point shapes under local unsure qualification",
      "evidence": "The final tight crop shows two compact dark patches on a rising diagonal, separated by white paper. Both shapes are retained graphically without assigning a character, hand, role or surface origin.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "20_right_detached_marks.png",
      "bbox": [
        1570,
        1739,
        1581,
        1751
      ],
      "physical_cluster": "G11",
      "components": [
        {
          "component": "upper patch",
          "shape_confidence": "high",
          "interpretation_confidence": "low"
        },
        {
          "component": "lower patch",
          "shape_confidence": "high",
          "interpretation_confidence": "low"
        }
      ]
    }
  ],
  "doubts": [
    {
      "location": "first cancelled verb",
      "reading": "est",
      "alternatives": [
        "soit"
      ],
      "confidence": "low",
      "reason": "crossing strokes conceal the short central letters",
      "crop": "01_upper_correction.png",
      "source_row": "R01",
      "difference": "A017-D02"
    },
    {
      "location": "marginal partition name",
      "reading": "Pi",
      "alternatives": [
        "pi"
      ],
      "confidence": "medium",
      "reason": "connected top and legs do not settle local case/size",
      "crop": "05_margin_note.png",
      "source_row": "R04",
      "difference": "A017-D13"
    },
    {
      "location": "marginal E predecessor",
      "reading": "cancelled Sigma",
      "alternatives": [],
      "confidence": "low",
      "reason": "surviving angular under-strokes are crowded",
      "crop": "05_margin_note.png",
      "source_row": "R04",
      "difference": "A017-D14"
    },
    {
      "location": "after cancelled et",
      "reading": "Intersection",
      "alternatives": [
        "intersection"
      ],
      "confidence": "low",
      "reason": "leading stroke tall and crowded; capital/lowercase unsettled",
      "crop": "08_intersection_start.png",
      "source_row": "R06",
      "difference": "A017-D21"
    },
    {
      "location": "sign after later E_j",
      "reading": "cancelled in",
      "alternatives": [
        "cancelled E"
      ],
      "confidence": "low",
      "reason": "lobes crossed by rising slash",
      "crop": "09_later_cancelled_sign.png",
      "source_row": "R07",
      "difference": "A017-D24"
    },
    {
      "location": "detached upper mark before alpha",
      "reading": "prime-shaped mark",
      "alternatives": [
        "dot-shaped mark"
      ],
      "confidence": "medium",
      "reason": "shape clear, character/role/hand/origin unestablished",
      "crop": "10_partition_display.png",
      "difference": "A017-D25"
    },
    {
      "location": "point before first union",
      "reading": "baseline point",
      "alternatives": [],
      "confidence": "medium",
      "reason": "character role, hand and surface origin unestablished",
      "crop": "11_first_union_dot.png",
      "difference": "A017-D27"
    },
    {
      "location": "inserted Pi_J superscript",
      "reading": "circle",
      "alternatives": [
        "zero"
      ],
      "confidence": "medium",
      "reason": "raised round open-centred loop supports both",
      "crop": "12_inserted_partition_ring.png",
      "source_row": "R08",
      "difference": "A017-D28"
    },
    {
      "location": "middle union transverse stroke",
      "reading": "literal cup with transverse stroke",
      "alternatives": [
        "overbar interpretation",
        "unassigned extra stroke interpretation"
      ],
      "confidence": "low",
      "reason": "presence clear; mathematical role unestablished",
      "crop": "13_middle_union.png",
      "source_row": "R11",
      "difference": "A017-D30"
    },
    {
      "location": "binary Pi_{J,j} superscript",
      "reading": "circle",
      "alternatives": [
        "zero"
      ],
      "confidence": "medium",
      "reason": "same local round-loop ambiguity; first occurrence carries the explicit TeX doubt",
      "crop": "14_binary_partition_guide.png",
      "source_row": "R08",
      "difference": "A017-D31"
    },
    {
      "location": "U subscript",
      "reading": "cancelled J followed by live J",
      "alternatives": [
        "cancelled j followed by live J",
        "one retraced J"
      ],
      "confidence": "low",
      "reason": "two displaced feet do not determine separate cancellation and replacement states",
      "crop": "15_U_subscript.png",
      "source_row": "R12",
      "difference": "A017-D33"
    },
    {
      "location": "final quantifier",
      "reading": "g",
      "alternatives": [
        "j"
      ],
      "confidence": "low",
      "reason": "closed loop and descending foot remain locally ambiguous",
      "crop": "16_final_words.png",
      "source_row": "R09",
      "difference": "A017-D36"
    },
    {
      "location": "far right between display and final prose",
      "reading": "two separate dark point shapes",
      "alternatives": [],
      "confidence": "medium",
      "reason": "visible shapes clear; character, role, hand and surface origin unestablished",
      "crop": "20_right_detached_marks.png",
      "difference": "A017-D39"
    }
  ],
  "notes": {
    "page_content": "Underlined Cas particuliers; an upper supposition and two recorded closure equalities; a further Sigma12 equality; a separator; a slanted partition note; and prose defining partitions for J, continuing through the final Pour. These are descriptions of the manuscript assertions, not proof endorsements.",
    "authors_own_uncertainty": {
      "exact_words": [],
      "comment": "No explicit authorial uncertainty formula was identified on this sheet; editorial reading doubts are recorded separately."
    },
    "title_date_page_counts": {
      "title": "Cas particuliers",
      "date": null,
      "author_page_number": null,
      "archive_number": "16",
      "H_page": "16",
      "comment": "H page16 is the metadata convention for our scan17. The visible pale16 is recorded only as the archive-number comment, not mspage."
    },
    "source_scope": "Only the assigned packet, brief, PREAMBLE, notation snapshot, and scan017 images were read. The note in C R10 about a following sheet was not used as ink evidence. No other reader or later page was inspected.",
    "workflow": "Brief read first; current UTC start was then recorded before packet/image reading. Whole scan opened once for layout, half a once, half b once. Sixteen initial distinct tight crops, three later previously uncropped accent loci, and one final previously uncropped detached-mark locus were each displayed once. The final mark crop followed the initial source-only structural check. No successfully viewed image or decided target was reopened. No crop retry occurred.",
    "coordinates": "Full scan is 1685x2363. Half a is 1685x1261 and starts at full y=0. Half b is 1685x1262; bottom alignment yields full y=half-b y+1101, using 2363-1262. Report full boxes use upper-left origin and [left,top,right,bottom]. Unrotated crop display coordinates use x_full=left+x_display*(right-left)/2600 and y_full=top+y_display*(bottom-top)/output_height. These maps locate hand-estimated graphical anchors. The rotated marginal crop was used for reading without a computed inverse rotation.",
    "graphics": "G01 and G08 each contain two literal draw paths. G02,G03,G04,G07,G09,G10 each contain one. G11 contains two separate fill paths. G05 is represented once by a qualified prime/dot candidate, and G06 once by a qualified baseline point. Every insertion-guide path appearing in reading.tex has its own difference and inventory item. Local drawing origins, rectangles, coordinate units, baselines and zero-separation base-west text anchors are declared in TeX; font extents are not asserted to coincide with source boxes.",
    "crop_bounds": "All intended target ascenders, descenders and guide endpoints are included. Some crops contain clipped unrelated adjacent-line context, including the neighboring mark at the margin-note crop boundary and preceding/following formula remnants; none is supplied as an extra manuscript word. No target was recropped.",
    "mathematics_led_reading_decisions": "No mathematical computation, morphism, theorem verification or algebraic correspondence was used. The written X minus Sigma_i is preserved. No mathematical repair was made. Bars, cup shapes, indices, circle/zero doubts and the literal transverse union stroke were selected from strokes only.",
    "C_source_row_map": [
      {
        "row": "R01",
        "source_place": "first line directly under on ait",
        "parts": {
          "subject": "A017-D01",
          "verb": "A017-D02",
          "adjective": "A017-D03"
        }
      },
      {
        "row": "R02",
        "source_place": "struck sentence above equalities",
        "parts": {
          "trouve": "A017-D07"
        }
      },
      {
        "row": "R03",
        "source_place": "third equality, first join",
        "parts": {
          "join": "A017-D10"
        }
      },
      {
        "row": "R04",
        "source_place": "left note",
        "parts": {
          "Pi/pi": "A017-D13",
          "crossed Sigma": "A017-D14"
        }
      },
      {
        "row": "R05",
        "source_place": "after de X",
        "parts": {
          "cancelled wording": "A017-D17"
        }
      },
      {
        "row": "R06",
        "source_place": "start of intersection",
        "parts": {
          "et": "A017-D20",
          "intersection": "A017-D21"
        }
      },
      {
        "row": "R07",
        "source_place": "under E_j and after later E_j",
        "parts": {
          "first Sigma": "A017-D19",
          "later E/in": "A017-D24"
        }
      },
      {
        "row": "R08",
        "source_place": "Pi_J above de, and binary partition name",
        "parts": {
          "inserted ring": "A017-D28",
          "binary ring": "A017-D31"
        }
      },
      {
        "row": "R09",
        "source_place": "last parenthesis",
        "parts": {
          "g/j": "A017-D36"
        }
      },
      {
        "row": "R10",
        "source_place": "last word at right edge",
        "parts": {
          "Pour/Puis": "A017-D38"
        }
      },
      {
        "row": "R11",
        "source_place": "first complement after inserted Pi_J",
        "parts": {
          "transverse bar presence": "A017-D30"
        }
      },
      {
        "row": "R12",
        "source_place": "above sur, U subscript",
        "parts": {
          "predecessor and complete state": "A017-D33",
          "final J": "A017-D34"
        }
      }
    ],
    "actual_computations": [
      {
        "operation": "image dimension reads",
        "inputs": [
          "J81-02_81_scan017.jpg",
          "J81-02_81_scan017_a.jpg",
          "J81-02_81_scan017_b.jpg"
        ],
        "result": [
          [
            1685,
            2363
          ],
          [
            1685,
            1261
          ],
          [
            1685,
            1262
          ]
        ],
        "scope": "PIL metadata size only, no image comparison"
      },
      {
        "operation": "half-b coordinate offset",
        "inputs": [
          2363,
          1262
        ],
        "mapping": "2363-1262",
        "result": 1101,
        "scope": "source-coordinate conversion only"
      },
      {
        "operation": "crop processing",
        "inputs": "twenty exact boxes in crop_manifest.json",
        "mapping": "crop; RGB autocontrast; only crop05 rotates -40 degrees with BICUBIC, expand and white fill; every crop becomes width2600 with height=round(pre_height*2600/pre_width), LANCZOS",
        "result": "twenty PNGs with recorded input/output dimensions in crop_manifest.json",
        "scope": "visual legibility only; no OCR, pixel-difference calculation, registration, numerical curve analysis or image comparison"
      },
      {
        "operation": "graphical anchor coordinate conversion",
        "inputs": "unrotated crop origins, original box dimensions, 2600 output width and recorded output heights",
        "mapping": "affine coordinate formula in notes.coordinates",
        "result": "hand-estimated full-scan path anchors declared for G01-G11 in reading.tex/report",
        "scope": "placement approximations only, no computed identity or geometric theorem"
      },
      {
        "operation": "initial source-only structural check",
        "inputs": [
          "reading.tex before G11 addition",
          "report.json before G11 addition",
          "crop_manifest.json before crop20"
        ],
        "result": {
          "reported_error": "empty line inside display",
          "source_rows": 12,
          "source_parts": 19,
          "difference_rows": 38,
          "draw_path_commands": 10,
          "crop_files": 19
        },
        "scope": "The empty-line report was caused by stripping a comment-only line into a blank line in the checker. The source had no empty physical line there. The checker is repaired to inspect physical display lines; no compiler or renderer was invoked."
      },
      {
        "operation": "final source-only structural check",
        "inputs": [
          "reading.tex including G11",
          "report.json including D39",
          "crop_manifest.json including crop20"
        ],
        "result": {
          "errors": [],
          "source_rows": 12,
          "source_parts": 19,
          "difference_rows": 39,
          "draw_path_commands": 10,
          "crop_files": 20
        },
        "scope": "delimiter and file/reference checks plus explicit counts, no compilation, rendering or mathematical verification; G11 has two separately documented fill paths"
      }
    ],
    "structural_verification": {
      "inputs": [
        "reading.tex",
        "report.json",
        "crop_manifest.json"
      ],
      "checks": "comment-aware brace balance; begin/end nesting; display delimiter counts and empty physical lines; crop existence and references; source-row ID references; macro inventory for manual review",
      "errors": [],
      "source_rows": 12,
      "source_parts": 19,
      "differences": 39,
      "draw_path_commands": 10,
      "crop_files": 20,
      "macros": [
        "Pi",
        "Sigma",
        "alpha",
        "amalg",
        "begin",
        "bigcup",
        "cdot",
        "circ",
        "coprod",
        "cup",
        "deleted",
        "displaystyle",
        "draw",
        "end",
        "figure",
        "fill",
        "forall",
        "hbox",
        "in",
        "inserted",
        "limits",
        "margin",
        "mathbin",
        "mathop",
        "node",
        "normalmarginpar",
        "overline",
        "path",
        "pi",
        "prime",
        "reversemarginpar",
        "scanpage",
        "setminus",
        "subset",
        "uline",
        "unsure",
        "vcenter"
      ],
      "compiler_or_renderer_used": false
    },
    "reading_report_pair_review": "Two full joint text-output attempts were truncated by output caps. The entire selected TeX was delivered. All fields of the final report are then read in four consecutive bounded text outputs against that TeX; no image is reopened."
  },
  "notation": [
    {
      "location": "title",
      "sign": "single underline",
      "latex": "\\uline{Cas particuliers}",
      "evidence": "one continuous line under both words"
    },
    {
      "location": "two upper equations and preceding parenthesis",
      "sign": "signed Sigma with lowered dotted i; separate closure rules",
      "latex": "\\Sigma_i^+,\\Sigma_i^-,\\overline{\\Sigma_i^+},\\overline{\\Sigma_i^-}",
      "evidence": "signed letters and upper rules inspected on half a; no mathematical inference"
    },
    {
      "location": "upper parenthesis",
      "sign": "comp. conn.",
      "latex": "comp. conn.",
      "evidence": "points after the two abbreviations retained; no expansion"
    },
    {
      "location": "third equality",
      "sign": "bar over Sigma12; retraced curved join",
      "latex": "\\overline{\\Sigma_{12}}; G01",
      "evidence": "separate upper rule and two curved right returns"
    },
    {
      "location": "Soit and lower display",
      "sign": "square join with extended foot",
      "latex": "\\amalg",
      "evidence": "uprights and horizontal extended base; H sqcup treated as same local reading, no macro-only row"
    },
    {
      "location": "partition display",
      "sign": "large coproduct, lowered alpha in pi_0(X minus E_j)",
      "latex": "\\coprod_{\\alpha\\in\\pi_0(X\\setminus E_j)}",
      "evidence": "wide squared bottom and upright legs; small pi and low round zero visible in crop10"
    },
    {
      "location": "named main partitions",
      "sign": "capital Pi and capital J index",
      "latex": "\\Pi_J,\\Pi_j,\\Pi_{J,j}",
      "evidence": "joined cap with two legs; J has upper bar and returning foot"
    },
    {
      "location": "two lower superscripts",
      "sign": "small upper ring",
      "latex": "\\Pi_J^{\\unsure{\\circ|0}};\\Pi_{J,j}^{\\circ}",
      "evidence": "two independently inspected open-centred loops; recurring-doubt convention"
    },
    {
      "location": "main lower prose",
      "sign": "locally absent acute strokes",
      "latex": "Considerons; definie (cancelled); definie; definies; definie",
      "evidence": "separate source crops retained; no spelling normalization"
    },
    {
      "location": "foot",
      "sign": "archive numeral",
      "latex": "% archive sheet number: 16",
      "evidence": "small pale 16 at lower-left page edge, half b"
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "A local upper mark before alpha and a baseline point before the first union have supported visible shapes but no established role. The brief permits qualified candidates; these are kept without mathematical interpretation.",
    "The middle union bar is visibly inside the tops of the stems. Literal paths preserve that placement while the role remains qualified; a conventional overline would move it.",
    "Inline insertion-guide graphics need to include their adjacent attachment word once. The selected TeX uses zero-separation base-west nodes and declared local origins rather than duplicating the words in a separate illustration."
  ]
}

## Reader B

\scanpage{17}
\uline{Cas particuliers}

Supposons que $\forall i\in I$, \deleted{$\unsure{E_i|\Sigma_i}$ \unsure{est|soit} \unsure{rare|dense} dans $X$.} \inserted{on ait} (si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)

\deleted{Alors on \unsure{trouve} que}
\[
\begin{aligned}
\overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\
\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i .
\end{aligned}
\]

Alors je dis qu'on a
\[
\overline{\Sigma_{12}}=\Sigma_{12}
% G01: two curved passes of the first cup; full-scan origin (946,783).
\mathbin{\vcenter{\hbox{\begin{tikzpicture}[x=0.014cm,y=-0.014cm]
\useasboundingbox (0,0) rectangle (36,32);
\begin{scope}[shift={(-946,-783)}]
\draw[line width=0.65pt] (950,787) .. controls (949,803) and (953,810) .. (960,810) .. controls (976,812) and (979,800) .. (974,789);
\draw[line width=0.50pt] (950,788) .. controls (950,802) and (951,807) .. (959,808) .. controls (971,807) and (971,798) .. (968,790);
\end{scope}
\end{tikzpicture}}}} E_1\cup E_2
\]

% G02: shallow separator and downturned right endpoint; full-scan origin (300,888).
\figure{\begin{tikzpicture}[x=0.012cm,y=-0.012cm]
\useasboundingbox (0,0) rectangle (242,25);
\begin{scope}[shift={(-300,-888)}]
\draw[line width=0.45pt] (303,900) .. controls (359,892) and (483,892) .. (519,893) .. controls (535,893) and (538,897) .. (538,901);
\end{scope}
\end{tikzpicture}}

% slanted
\reversemarginpar
\margin{introduire la partition $\Pi_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$
% G03: short dark wedge to the right of the closing brace in crop05.
% Its character, role, hand, and possible attachment to neighbouring text remain open.
\unsure{\begin{tikzpicture}[x=0.25mm,y=0.25mm,baseline=0pt]
\useasboundingbox (0,0) rectangle (3,4);
\fill (0,0) -- (0.4,3) -- (2.2,2) -- cycle;
\end{tikzpicture}}}
\normalmarginpar
\deleted{Supposons}

Soit $J\subset I$ tel que $I=J\amalg\{i\}$.

Consid\unsure{e|é}rons la partition
% G04: first Pi_J insertion and its curved guide. Fixed source origin (1218,1105).
\begin{tikzpicture}[x=0.010cm,y=-0.010cm,baseline=(live.base)]
\useasboundingbox (0,0) rectangle (180,130);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (0,58) {\inserted{$\Pi_J$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (70,115) {de};
\begin{scope}[shift={(-1218,-1105)}]
\draw[line width=0.40pt] (1282,1226) .. controls (1284,1204) and (1306,1196) .. (1338,1192) .. controls (1354,1189) and (1367,1188) .. (1370,1183);
\end{scope}
\end{tikzpicture}
$X$ \deleted{definie} definie par les $\deleted{\Sigma}E_j$ $(j\in J)$, \deleted{\unsure{et}} intersection des partitions
% G05: ternaires Pi_j and the long V-shaped guide; source origin (947,1345).
\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=(live.base)]
\useasboundingbox (0,0) rectangle (352,140);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (20,52) {\inserted{ternaires $\Pi_j$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (292,110) {de $X$};
\begin{scope}[shift={(-947,-1345)}]
\draw[line width=0.45pt] (1127,1407) .. controls (1161,1407) and (1180,1418) .. (1184,1451) .. controls (1193,1432) and (1214,1404) .. (1228,1390);
\end{scope}
\end{tikzpicture}
$(j\in J)$ definies par les $E_j$ $\unsure{\deleted{\in}|\deleted{E}|\notin}$ $(j\in J)$
\[
X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}\Sigma_j^\alpha
\]

-- c'est aussi la partition definie par celle de
% G06: detached baseline point before the first union, role and hand unresolved.
$\displaystyle \unsure{\mathord{\begin{tikzpicture}[x=0.025cm,y=-0.025cm,baseline=0pt]
\useasboundingbox (0,0) rectangle (9,7);
\begin{scope}[shift={(-734,-1902)}]
\fill (735,1903) -- (741,1902) -- (741,1907) -- (735,1907) -- cycle;
\end{scope}
\end{tikzpicture}}}\bigcup_{j\in J}E_j$ en les $E_j$, et la partition
% G07: raised Pi_J ring and bent guide; source origin (752,1973).
\begin{tikzpicture}[x=0.010cm,y=-0.010cm,baseline=(live.base)]
\useasboundingbox (0,0) rectangle (168,110);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (15,40) {\inserted{$\Pi_J^{\unsure{\circ|0}}$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (91,80) {de};
\begin{scope}[shift={(-752,-1973)}]
\draw[line width=0.40pt] (808,2055) .. controls (803,2038) and (826,2029) .. (852,2022) .. controls (870,2018) and (894,2005) .. (891,1997) -- (888,1994);
\end{scope}
\end{tikzpicture}
$\displaystyle X\setminus
% G08: literal cup and transverse upper stroke; source origin (1118,1976).
\mathop{\vcenter{\hbox{\begin{tikzpicture}[x=0.009cm,y=-0.009cm]
\useasboundingbox (0,0) rectangle (69,70);
\begin{scope}[shift={(-1118,-1976)}]
\draw[line width=0.45pt] (1130,1980) .. controls (1125,1999) and (1126,2020) .. (1137,2034) .. controls (1152,2045) and (1170,2034) .. (1176,2014) .. controls (1180,2003) and (1177,1986) .. (1172,1980);
\draw[line width=0.40pt] (1123,1990) .. controls (1141,1990) and (1156,1988) .. (1168,1988);
\end{scope}
\end{tikzpicture}}}}\limits_{j\in J}E_j$ intersection des partitions binaires $\Pi_{J,j}^{\circ}$
% The upper ring's local circle/zero doubt is recorded also at this second occurrence.
% G09: inserted (j in J), live induites, and one continuous hooked guide.
% Fixed source origin (1234,2070); the guide supplies no extra prose parenthesis.
\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=(live.base)]
\useasboundingbox (0,0) rectangle (320,110);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (45,35) {\inserted{$(j\in J)$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (50,84) {induites};
\begin{scope}[shift={(-1234,-2070)}]
\draw[line width=0.40pt] (1244,2162) .. controls (1237,2145) and (1263,2122) .. (1298,2117) .. controls (1350,2130) and (1433,2110) .. (1456,2105) .. controls (1461,2103) and (1456,2100) .. (1452,2098);
\end{scope}
\end{tikzpicture}
% G10: U-subscript correction states and its long guide into the sur/X gap.
% Fixed source origin (311,2140); glyph/state alternatives carry no chronology.
\begin{tikzpicture}[x=0.010cm,y=-0.010cm,baseline=(live.base)]
\useasboundingbox (0,0) rectangle (151,165);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (56,75) {\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (20,123) {sur};
\begin{scope}[shift={(-311,-2140)}]
\draw[line width=0.40pt] (375,2228) .. controls (392,2234) and (422,2234) .. (434,2245) .. controls (447,2259) and (448,2277) .. (451,2294);
\end{scope}
\end{tikzpicture}
$\displaystyle X\setminus\bigcup_{j\in J}E_j$ par les $\Pi_j$ $(\unsure{g|j}\in J)$. Pour
% archive sheet number: 16



{
  "differences": [
    {
      "id": "D01a",
      "location": "Opening cancelled subject",
      "C": "\\unsure{E_i|\\Sigma_i}",
      "H": "E_i",
      "reading": "\\unsure{E_i|\\Sigma_i}",
      "evidence": "Three heavy horizontal remnants and a left upright favour E; diagonals, a lower loop, and the index overlap the cancellation. The complete cancelled glyph is not settled. H shares the first candidate.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop01_top_correction.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1035,
          178,
          1665,
          336
        ]
      },
      "C_source_row": 1,
      "local_part": "subject"
    },
    {
      "id": "D01b",
      "location": "Opening cancelled short verb",
      "C": "\\unsure{est}",
      "H": "soit",
      "reading": "\\unsure{est|soit}",
      "evidence": "An elongated low loop, a short rounded middle, and a taller final upright favour est. The cancellation prevents a secure division of the intervening strokes; soit remains an explicit alternative. C uncertainty is retained, with its unspecified alternative made concrete.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop01_top_correction.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1035,
          178,
          1665,
          336
        ]
      },
      "C_source_row": 1,
      "local_part": "verb",
      "qualification": "H differs in primary candidate only; its reading is retained as an alternative."
    },
    {
      "id": "D01c",
      "location": "Opening cancelled adjective",
      "C": "\\unsure{rare|dense}",
      "H": "rare",
      "reading": "\\unsure{rare|dense}",
      "evidence": "The low r-like rises and terminal loop favour rare, but the central word is crossed and the high stroke can belong to the preceding word. The enlargement does not settle rare/dense.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop01_top_correction.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1035,
          178,
          1665,
          336
        ]
      },
      "C_source_row": 1,
      "local_part": "adjective"
    },
    {
      "id": "D02",
      "location": "Cancelled sentence above the equalities",
      "C": "\\unsure{trouve}",
      "H": "trouve",
      "reading": "\\unsure{trouve}",
      "evidence": "The tall opening t, several shallow lower returns, and the final low strokes survive the long cancellation. The intervening letter divisions remain uncertain. The target word and final que descender are present in the crop; the initial A of context is clipped at the top.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop02_trouve.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          270,
          319,
          950,
          442
        ]
      },
      "C_source_row": 2
    },
    {
      "id": "D03",
      "location": "First join of the Sigma_12 equality",
      "C": "\\unsure{\\cup|\\amalg}",
      "H": "\\cup",
      "reading": "\\cup, reproduced as two curved passes (G01)",
      "evidence": "The enlarged sign has one left upright, two closely spaced right returns, and curved lower bowls. The literal two paths are retained. The square-join candidate is removed on the inspected strokes.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crop04_join.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          700,
          738,
          1240,
          850
        ]
      },
      "C_source_row": 3,
      "graphic": "G01",
      "counting": "One physical join cluster per witness; C doubt resolution and the two-path geometry are recorded together."
    },
    {
      "id": "D04a",
      "location": "Slanted margin, partition name",
      "C": "\\unsure{\\Pi|\\pi}_j",
      "H": "\\Pi_j",
      "reading": "\\Pi_j",
      "evidence": "The upright rotated view shows the joined horizontal head and two substantial descending legs. The capital form is selected; the long subscript j is separate.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop05_margin.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          20,
          936,
          323,
          1318
        ]
      },
      "C_source_row": 4,
      "local_part": "partition letter"
    },
    {
      "id": "D04b",
      "location": "Slanted margin, predecessor under E_j",
      "C": "\\deleted{\\unsure{\\Sigma}}E_j",
      "H": "E_j",
      "reading": "\\deleted{\\unsure{\\Sigma}}E_j",
      "evidence": "An angular dark under-form and a crossing stroke remain within the first E. Sigma is a supported candidate but its original outline is partly hidden. H omits the local predecessor.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop05_margin.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          20,
          936,
          323,
          1318
        ]
      },
      "C_source_row": 4,
      "local_part": "cancelled predecessor"
    },
    {
      "id": "D05",
      "location": "Cancelled wording after de X",
      "C": "\\deleted{\\unsure{des parties|définie}}",
      "H": "\\struck{définie}",
      "reading": "\\deleted{definie}",
      "evidence": "One continuous word shows the looped d, low e, long f descender, two i positions and the ending. The surviving strokes support definie. No detached acute is visible over its e; the two-word first C candidate is removed.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crop06_cancelled_definie.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          411,
          1260,
          879,
          1395
        ]
      },
      "C_source_row": 5,
      "qualification": "The H difference here is the written accent; its lexical reading matches."
    },
    {
      "id": "D06a",
      "location": "Overwritten beginning of intersection",
      "C": "\\deleted{\\unsure{et}}",
      "H": "\\struck{intersection}\\add{intersection}",
      "reading": "\\deleted{\\unsure{et}} intersection",
      "evidence": "A short low e-like opening and crossed upright occur before the longer live word. The compact predecessor remains uncertain. Only one complete longer word is visible in this cluster; no separate raised replacement word is supplied.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop08_intersection.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          307,
          1404,
          813,
          1500
        ]
      },
      "C_source_row": 6,
      "local_part": "short predecessor",
      "counting": "H cancellation/insertion reading is counted once for this physical cluster; D06b is the independent C word doubt."
    },
    {
      "id": "D06b",
      "location": "Live longer word intersection",
      "C": "\\unsure{intersection}",
      "H": "\\add{intersection}",
      "reading": "intersection",
      "evidence": "The extended word has the surviving internal rises and the final crossed t, dot and low terminal run. The live lexical reading intersection is selected. Its state comparison with H is included in D06a.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop08_intersection.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          307,
          1404,
          813,
          1500
        ]
      },
      "C_source_row": 6,
      "local_part": "live longer word",
      "parent_difference": "D06a"
    },
    {
      "id": "D07a",
      "location": "Predecessor beneath E_j after par les",
      "C": "\\deleted{\\Sigma}E_j (source doubt table qualifies Sigma)",
      "H": "E_j",
      "reading": "\\deleted{\\Sigma}E_j",
      "evidence": "The top and bottom horizontal segments with the surviving diagonal give Sigma beneath the heavy E strokes. The crossing is retained. This is a source-table doubt even though C.tex prints no unsure macro at this occurrence.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crop07_corrected_E.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1258,
          1264,
          1598,
          1386
        ]
      },
      "C_source_row": 7,
      "local_part": "first corrected E_j"
    },
    {
      "id": "D07b",
      "location": "Isolated slashed form after later E_j",
      "C": "\\deleted{\\unsure{E|\\in}}",
      "H": "\\ill{}",
      "reading": "\\unsure{\\deleted{\\in}|\\deleted{E}|\\notin}",
      "evidence": "Two curved lower arms and an oblique upper crossing favour a membership-form candidate over E. The strokes do not settle a cancelled predecessor versus an integral slashed-membership sign. All complete selected states are explicit.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop10_isolated_sign.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1071,
          1507,
          1447,
          1616
        ]
      },
      "C_source_row": 7,
      "local_part": "later isolated form",
      "qualification": "C E remains an alternative; the cancellation interpretation itself is newly qualified.",
      "counting": "One H ill placeholder and one C physical glyph/state cluster."
    },
    {
      "id": "D08a",
      "location": "Raised partition name over lower de",
      "C": "\\Pi_J^{\\unsure{\\circ|0}}",
      "H": "\\Pi_J^0",
      "reading": "\\Pi_J^{\\unsure{\\circ|0}}",
      "evidence": "The small upper rounded, partly angular loop is visibly raised. Its strokes do not decide circle versus numeral zero. H zero remains the second candidate.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop12_inserted_Pi.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          552,
          1963,
          972,
          2096
        ]
      },
      "C_source_row": 8,
      "local_part": "first upper ring",
      "qualification": "Qualified primary-candidate difference from H."
    },
    {
      "id": "D08b",
      "location": "Binary partition name, repeated upper ring",
      "C": "\\Pi_{J,j}^{\\circ} (source table qualifies this ring too)",
      "H": "\\Pi_{J,j}^0",
      "reading": "\\Pi_{J,j}^{\\circ}, carrying the page-first circle/zero qualification",
      "evidence": "A separate tiny raised loop occurs beside this Pi. Circle/zero remains unresolved locally. The final TeX follows the recurring-symbol convention: the first occurrence carries unsure and this occurrence uses the same first candidate.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop14_binary_Pi.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1092,
          2062,
          1567,
          2220
        ]
      },
      "C_source_row": 8,
      "local_part": "binary-name upper ring",
      "qualification": "Qualified primary-candidate difference from H; source-row scope explicitly retained."
    },
    {
      "id": "D09",
      "location": "Last parenthesis, quantified letter",
      "C": "\\unsure{g|j}",
      "H": "j",
      "reading": "\\unsure{g|j}",
      "evidence": "The compact loop above the long downstroke favours g, while the extended leftward foot also supports j. The crop retains the complete foot; both readings remain.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop16_final_words.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1115,
          2209,
          1652,
          2340
        ]
      },
      "C_source_row": 9,
      "qualification": "H j is retained as an alternative, not rejected conclusively."
    },
    {
      "id": "D10",
      "location": "Last word at right edge",
      "C": "\\unsure{Pour|Puis}",
      "H": "\\uncertain{Pour}",
      "reading": "Pour",
      "evidence": "The capital P is followed by a compressed low o, a broad u and terminal r-like return. There is no separate high i dot at the relevant later position. The decision uses this crop only, without the following sheet.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop16_final_words.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1115,
          2209,
          1652,
          2340
        ]
      },
      "C_source_row": 10
    },
    {
      "id": "D11",
      "location": "First complement after inserted Pi_J ring",
      "C": "\\unsure{\\overline{\\bigcup}|\\bigcup}",
      "H": "\\bigcup",
      "reading": "\\overline{\\bigcup}, reproduced by the literal cup and transverse stroke G08",
      "evidence": "A separate transverse run starts just left of the left stem, crosses it near the top and stops short of the right stem. Its presence is clear. G08 preserves this attachment and span without assigning an additional mathematical interpretation.",
      "confidence": "high",
      "kind": "misread symbol or index",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crop13_middle_union.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1002,
          1955,
          1641,
          2112
        ]
      },
      "C_source_row": 11,
      "graphic": "G08",
      "counting": "One physical union/stroke cluster per witness, including the literal geometry."
    },
    {
      "id": "D12",
      "location": "Inserted U subscript above sur",
      "C": "U_{\\deleted{\\unsure{J|j}}J}",
      "H": "U_J",
      "reading": "U_{\\unsure{\\deleted{J}J|\\deleted{j}J|J}}",
      "evidence": "Two displaced lower returns share a crowded upright; the final upper horizontal favours capital J. The predecessor can be J or j, and the two returns do not establish cancellation/replacement rather than retracing. The plain final-J state is therefore retained as an explicit alternative.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop15_U_subscript.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          307,
          2140,
          581,
          2321
        ]
      },
      "C_source_row": 12,
      "qualification": "Glyph and state uncertainty are separate. H matches the plain-J alternative. No writing chronology is inferred."
    },
    {
      "id": "H01",
      "location": "Opening parenthesis",
      "C": "si",
      "H": "où",
      "reading": "si",
      "evidence": "A looped s and narrow following i stand after the opening parenthesis, before the two signed Sigmas.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop01_top_correction.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1035,
          178,
          1665,
          336
        ]
      }
    },
    {
      "id": "H02",
      "location": "End of opening cancellation",
      "C": "dans X.",
      "H": "dans X",
      "reading": "dans X.",
      "evidence": "A distinct dark baseline point follows the cancelled X.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop01_top_correction.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1530,
          235,
          1610,
          289
        ]
      }
    },
    {
      "id": "H03",
      "location": "Raised on ait",
      "C": "\\inserted{on ait}",
      "H": "on ait",
      "reading": "\\inserted{on ait}",
      "evidence": "The words are above the crossed sentence and supply its live continuation before the parenthesis.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop01_top_correction.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1135,
          183,
          1340,
          235
        ]
      }
    },
    {
      "id": "H04",
      "location": "First equality endpoint",
      "C": "E_i",
      "H": "E_i,",
      "reading": "E_i",
      "evidence": "The i dot and upright are present; the clear space after the first right-hand member has no comma. The point on the lower row remains the second equality endpoint.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop03_equation_endpoints.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          935,
          416,
          1070,
          499
        ]
      }
    },
    {
      "id": "H05",
      "location": "Prose introducing Sigma_12 equality",
      "C": "Alors je dis qu'on a",
      "H": "Alors je dis que",
      "reading": "Alors je dis qu'on a",
      "evidence": "Half a shows the long q descender, apostrophe, low on and final small a after dis. This locus was settled on half a and was not cropped.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          300,
          621,
          1004,
          774
        ]
      },
      "image_evidence": "supplied half a; same coordinates as full scan"
    },
    {
      "id": "N01",
      "location": "Divider below third equality",
      "C": "\\rule{2.4cm}{0.3pt}",
      "H": "[absent]",
      "reading": "G02 shallow curved rule with hooked right endpoint",
      "evidence": "Half a shows a gently rising left run, long shallow middle and a short downward right ending. The literal one-path separator replaces the straight rule.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          300,
          888,
          542,
          913
        ]
      },
      "graphic": "G02",
      "image_evidence": "supplied half a; no crop because settled there"
    },
    {
      "id": "H06",
      "location": "Slanted note opening",
      "C": "introduire",
      "H": "introduisons",
      "reading": "introduire",
      "evidence": "The upright rotated view ends in a short i-like upright and low re return. The selected ending is introduire.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop05_margin.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          20,
          936,
          323,
          1318
        ]
      }
    },
    {
      "id": "N02",
      "location": "Short dark shape to right of slanted-note brace",
      "C": "[absent]",
      "H": "\\ill{}",
      "reading": "\\unsure{G03 short wedge}",
      "evidence": "The rotated crop contains a short isolated dark wedge to the right of the closing brace. Its character, writer, role and possible attachment to neighbouring main text remain unresolved. The shape is retained locally; no word is supplied.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop05_margin.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          20,
          936,
          323,
          1318
        ]
      },
      "graphic": "G03",
      "counting": "The one final margin ill placeholder is collated once. The shape is not claimed to be the full content intended by H.",
      "qualification": "Possible neighbouring-text attachment remains open; root can adjudicate from this same crop.",
      "shape_confidence": "medium",
      "role_and_hand": "unresolved"
    },
    {
      "id": "N03",
      "location": "Considérons accent",
      "C": "Considérons",
      "H": "Considérons",
      "reading": "Consid\\unsure{e|é}rons",
      "evidence": "The e-area has no secure detached acute; a faint short upper-right trace prevents complete resolution. The unaccented candidate is first, with the source accent retained explicitly.",
      "confidence": "low",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop17_considérons.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          313,
          1138,
          745,
          1243
        ]
      },
      "qualification": "Qualified accent reading, not a claim about editorial intent."
    },
    {
      "id": "N04",
      "location": "Live definie immediately after cancellation",
      "C": "définie",
      "H": "définie",
      "reading": "definie",
      "evidence": "The low e between looped d and the long f has no detached acute in the enlarged word. Both i positions and the final ending are present.",
      "confidence": "medium",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop06_cancelled_definie.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          684,
          1264,
          877,
          1379
        ]
      }
    },
    {
      "id": "N05",
      "location": "definies after (j in J)",
      "C": "définies",
      "H": "définies",
      "reading": "definies",
      "evidence": "The first e is a low join before the tall f, without an upper acute. The later two detached marks belong to the two i positions, and the low final run carries the plural ending.",
      "confidence": "high",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop18_definies.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          536,
          1511,
          982,
          1619
        ]
      }
    },
    {
      "id": "N06",
      "location": "Lower partition definie",
      "C": "définie",
      "H": "définie",
      "reading": "definie",
      "evidence": "The e before f has no raised acute. The two later detached marks align with the i positions; they do not supply an accent over e.",
      "confidence": "high",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop19_lower_definie.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1080,
          1740,
          1452,
          1845
        ]
      }
    },
    {
      "id": "N07",
      "location": "Guide under first inserted Pi_J",
      "C": "\\inserted{\\Pi_J} without guide",
      "H": "\\add{\\Pi_J} without guide",
      "reading": "unchanged Pi_J insertion plus G04",
      "evidence": "Half a shows the curved stroke above de, turning upward toward its right endpoint. G04 keeps that observed run; the inserted wording is unchanged.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1218,
          1105,
          1395,
          1235
        ]
      },
      "graphic": "G04",
      "image_evidence": "supplied half a; guide settled there"
    },
    {
      "id": "N08",
      "location": "Guide for ternaires Pi_j",
      "C": "\\inserted{ternaires \\Pi_j} without guide",
      "H": "\\add{ternaires \\Pi_j} without guide",
      "reading": "unchanged insertion plus G05",
      "evidence": "A leftward upper run curves down to the low V point and rises in a long oblique right stroke. The full guide survives within the crop and is drawn once.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop09_ternaires.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          947,
          1345,
          1246,
          1478
        ]
      },
      "graphic": "G05"
    },
    {
      "id": "N09",
      "location": "Detached point before first lower union",
      "C": "[absent]",
      "H": "[absent]",
      "reading": "\\unsure{G06 baseline point}",
      "evidence": "The crop shows one discrete small dark quadrilateral left of the union at its lower level. It has no established role or hand; no operation is assigned.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop11_first_union.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          732,
          1900,
          744,
          1910
        ]
      },
      "graphic": "G06",
      "qualification": "Shape presence is high confidence; interpretation and hand remain unresolved.",
      "shape_confidence": "high",
      "role_and_hand": "unresolved"
    },
    {
      "id": "N10",
      "location": "Guide for lower inserted Pi_J ring",
      "C": "\\inserted{\\Pi_J^{\\unsure{\\circ|0}}} without guide",
      "H": "\\add{\\Pi_J^0} without guide",
      "reading": "unchanged qualified insertion plus G07",
      "evidence": "A long curve rises from the partition/de gap, runs beneath the inserted symbol and ends with a short upward hook on the right. The ring decision is logged separately under D08a.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop12_inserted_Pi.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          552,
          1963,
          972,
          2096
        ]
      },
      "graphic": "G07"
    },
    {
      "id": "N11",
      "location": "Guide above induites",
      "C": "\\inserted{(j\\in J)} induites, no drawn guide",
      "H": "\\add{(j\\in J)} (induites",
      "reading": "\\inserted{(j\\in J)} induites with G09",
      "evidence": "The left curved portion continues into the long run above induites and its hooked right endpoint. It is preserved as one connected guide. H renders the left portion as a prose opening parenthesis.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop14_binary_Pi.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1092,
          2062,
          1567,
          2220
        ]
      },
      "graphic": "G09"
    },
    {
      "id": "N12",
      "location": "Guide from inserted U expression into sur/X gap",
      "C": "\\inserted{U_J=} without guide",
      "H": "U_J= without insertion or guide",
      "reading": "qualified inserted U expression plus G10",
      "evidence": "A thin run below the double subscript feet curves right and then descends deeply between sur and X. The endpoint is inside the crop. G10 preserves this one connected path; D12 records the independent glyph/state alternatives.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop15_U_subscript.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          307,
          2140,
          581,
          2321
        ]
      },
      "graphic": "G10"
    },
    {
      "id": "H07",
      "location": "End of final quantified parenthesis",
      "C": "(\\unsure{g|j}\\in J).",
      "H": "(j\\in J)).",
      "reading": "(\\unsure{g|j}\\in J).",
      "evidence": "One closing parenthesis follows J, then one distinct point. No second closing parenthesis appears before Pour.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop16_final_words.png",
      "bbox": {
        "system": "full scan, upper-left origin",
        "coordinates": [
          1322,
          2218,
          1472,
          2310
        ]
      }
    }
  ],
  "doubts": [
    {
      "id": "D01a",
      "location": "Opening cancelled subject",
      "reading": "\\unsure{E_i|\\Sigma_i}",
      "alternatives": [
        "\\Sigma_i"
      ],
      "confidence": "low",
      "reason": "Dense cancellation hides the full subject and index.",
      "crop": "crop01_top_correction.png"
    },
    {
      "id": "D01b",
      "location": "Opening cancelled short verb",
      "reading": "\\unsure{est|soit}",
      "alternatives": [
        "soit"
      ],
      "confidence": "low",
      "reason": "The short word is crossed; letter divisions remain open.",
      "crop": "crop01_top_correction.png"
    },
    {
      "id": "D01c",
      "location": "Opening cancelled adjective",
      "reading": "\\unsure{rare|dense}",
      "alternatives": [
        "dense"
      ],
      "confidence": "low",
      "reason": "The central low run is crossed.",
      "crop": "crop01_top_correction.png"
    },
    {
      "id": "D02",
      "location": "Cancelled sentence above the equalities",
      "reading": "\\unsure{trouve}",
      "alternatives": [
        "unresolved internal letters"
      ],
      "confidence": "medium",
      "reason": "The long strike obscures the shallow middle letters.",
      "crop": "crop02_trouve.png"
    },
    {
      "id": "D04b",
      "location": "Slanted margin, predecessor under E_j",
      "reading": "\\deleted{\\unsure{\\Sigma}}E_j",
      "alternatives": [
        "unresolved predecessor"
      ],
      "confidence": "low",
      "reason": "The angular under-form is partly covered by E.",
      "crop": "crop05_margin.png"
    },
    {
      "id": "D06a",
      "location": "Overwritten beginning of intersection",
      "reading": "\\deleted{\\unsure{et}} intersection",
      "alternatives": [
        "unresolved short predecessor"
      ],
      "confidence": "low",
      "reason": "Only a compact crossed opening survives clearly.",
      "crop": "crop08_intersection.png"
    },
    {
      "id": "D07b",
      "location": "Isolated slashed form after later E_j",
      "reading": "\\unsure{\\deleted{\\in}|\\deleted{E}|\\notin}",
      "alternatives": [
        "\\deleted{E}",
        "\\notin"
      ],
      "confidence": "low",
      "reason": "Glyph and cancellation role remain independently open.",
      "crop": "crop10_isolated_sign.png"
    },
    {
      "id": "D08a",
      "location": "Raised partition name over lower de",
      "reading": "\\Pi_J^{\\unsure{\\circ|0}}",
      "alternatives": [
        "0"
      ],
      "confidence": "medium",
      "reason": "The small raised ring does not settle circle/zero.",
      "crop": "crop12_inserted_Pi.png"
    },
    {
      "id": "D08b",
      "location": "Binary partition name, repeated upper ring",
      "reading": "\\Pi_{J,j}^{\\circ}, carrying the page-first circle/zero qualification",
      "alternatives": [
        "0"
      ],
      "confidence": "medium",
      "reason": "This second physical ring remains locally unresolved.",
      "crop": "crop14_binary_Pi.png"
    },
    {
      "id": "D09",
      "location": "Last parenthesis, quantified letter",
      "reading": "\\unsure{g|j}",
      "alternatives": [
        "j"
      ],
      "confidence": "low",
      "reason": "The small loop and extended tail support both candidates.",
      "crop": "crop16_final_words.png"
    },
    {
      "id": "D12",
      "location": "Inserted U subscript above sur",
      "reading": "U_{\\unsure{\\deleted{J}J|\\deleted{j}J|J}}",
      "alternatives": [
        "U_{\\deleted{j}J}",
        "U_J"
      ],
      "confidence": "low",
      "reason": "Double feet do not establish predecessor case or replacement state.",
      "crop": "crop15_U_subscript.png"
    },
    {
      "id": "N02",
      "location": "Short dark shape to right of slanted-note brace",
      "reading": "\\unsure{G03 short wedge}",
      "alternatives": [
        "unassigned character or neighbouring-text attachment"
      ],
      "confidence": "low",
      "reason": "Retained shape has unresolved attachment, role and hand.",
      "crop": "crop05_margin.png"
    },
    {
      "id": "N03",
      "location": "Considérons accent",
      "reading": "Consid\\unsure{e|é}rons",
      "alternatives": [
        "Considérons"
      ],
      "confidence": "low",
      "reason": "The faint upper trace does not securely establish an acute.",
      "crop": "crop17_considérons.png"
    },
    {
      "id": "N09",
      "location": "Detached point before first lower union",
      "reading": "\\unsure{G06 baseline point}",
      "alternatives": [
        "unassigned dot-like mark"
      ],
      "confidence": "medium",
      "reason": "Visible point has unresolved role and hand.",
      "crop": "crop11_first_union.png"
    }
  ],
  "notes": {
    "page_content": "Underlined Cas particuliers. A corrected supposition and two closure equalities; a further Sigma_12 equality; a separator; a slanted partition note; a J subset I paragraph, partition display and lower partition prose ending Pour.",
    "author_own_uncertainty_exact_words": [],
    "author_own_uncertainty_note": "No explicit author doubt word or question mark was identified. Editorial unsure markings are reader uncertainty.",
    "title": "Cas particuliers",
    "date": "No written date observed",
    "page_counts": "Archive pencil 16 at lower left; no author page number is supplied. H page 16 is the witness page identifier, one below our scan.",
    "mathematics_led_reading_decisions": "No algebraic, topological or theorem check was performed. The written X setminus Sigma_i is retained. The dot-like mark and slashed form receive no inferred mathematical role. Formula expectations did not settle uncertain strokes.",
    "witness_apparatus": "H note about X setminus Sigma_i is editorial apparatus, not extra manuscript text. H emph matches the observed title underline. H sqcup and C amalg at the two inspected square joins convey the same selected glyph; that macro conversion creates no row. H page macro is pagination apparatus.",
    "graphic_placement": "All graphical paths are manual approximations of observed strokes. Literal full-scan coordinates are translated by the declared fixed local origins. Text nodes use base-west anchors and zero inner/outer separation; their font extents are not claimed to be original pixel bounds. G03 has only a local upright shape origin and the full source-locus box because its attachment remains unresolved.",
    "crop_limits": "Crop02 clips the top of the contextual initial A, but retains the trouve target and the complete que descender. Crop03 includes the continuation of that descender at its top. Crop09 clips unrelated upper/side context, with the ternaires target and full guide preserved. Crop18 clips part of the following les context, with definies complete. No target was recropped or reopened.",
    "final_joint_read": "Two combined TeX/report outputs were truncated by tool delivery. The complete TeX was visible; the complete report is read across smaller field groups, including the previously omitted middle. No image is reopened."
  },
  "notation": [
    {
      "location": "Top two equalities",
      "signs": "\\Sigma_i^+,\\Sigma_i^-,E_i,\\overline{\\Sigma_i^+},\\overline{\\Sigma_i^-}",
      "evidence": "Separate closure bars, signed superscripts, dotted short i forms and three-bar E forms."
    },
    {
      "location": "Third equality",
      "signs": "\\overline{\\Sigma_{12}},\\Sigma_{12},E_1,E_2,\\cup",
      "evidence": "Closure rule and lower 12; first cup has two curved passes, G01."
    },
    {
      "location": "Soit line and partition display",
      "signs": "J\\subset I,\\ I=J\\amalg\\{i\\},\\ X=E_j\\amalg\\coprod_{\\alpha\\in\\pi_0(X\\setminus E_j)}\\Sigma_j^\\alpha",
      "evidence": "Broad J, single subset curve, square joins, coproduct legs, two alpha positions, low ring on pi."
    },
    {
      "location": "Slanted note and inserted partition names",
      "signs": "\\Pi_j,\\Pi_J,\\Pi_{J,j}",
      "evidence": "Joined upper head with two descending legs; local subscript forms read individually."
    },
    {
      "location": "Two lower upper rings",
      "signs": "\\circ|0",
      "evidence": "Both tiny raised loops remain independently qualified under original C row8."
    },
    {
      "location": "Three lower indexed unions",
      "signs": "\\bigcup;\\ \\overline{\\bigcup};\\ \\bigcup",
      "evidence": "First and last open tops; a transverse attached upper stroke on the middle, preserved as G08."
    },
    {
      "location": "Top parenthetical prose",
      "signs": "comp. conn.",
      "evidence": "Both abbreviations and their separate terminal points are present; no expansion is introduced."
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The first-occurrence recurring-symbol rule and the instruction to preserve every separately named compound-row locality both apply to row8. The TeX marks the first ring and uses the same first candidate at the second; the report keeps both local doubts explicit.",
    "Small nonstandard mathematical glyphs and insertion guides need inline TikZ to keep their physical attachment in prose/math. The standalone separator uses figure; the local inline figures use fixed origins without redefining any macro.",
    "The short wedge at the slanted-note right edge has an uncertain relationship to neighbouring main text. Its supported shape is retained locally and qualified; no character or full missing word is supplied."
  ]
}

## Reader C

\scanpage{17}
\uline{Cas particuliers}

Supposons que $\forall i\in I$, \deleted{$E_i$ \unsure{est|soit} rare dans $X$.} \inserted{on ait} (si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)

\deleted{Alors on \unsure{trouve} que}
\[
\begin{aligned}
\overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\
\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i\hspace{1.5cm}
% M01: source origin (1172,557); observed triangular point, period interpretation retained as alternative.
\mathpunct{\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(monebase)]
\coordinate (monebase) at (0,6);
\path[use as bounding box] (0,0) rectangle (7,7);
\fill (1,5) -- (3,1) -- (5,0) -- (7,5) -- cycle;
\end{tikzpicture}|.}}
\end{aligned}
\]

Alors je dis qu'on a
\[
\overline{\Sigma_{12}}=\Sigma_{12}
% G01: source origin (947,783); primary literal retraced cup, alternative amalg.
\mathbin{\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(joinbase)]
\coordinate (joinbase) at (0,29);
\path[use as bounding box] (0,0) rectangle (33,32);
\draw[line width=0.8pt,line cap=round] (4,3) .. controls (2,10) and (4,17) .. (5,24);
\draw[line width=0.65pt,line cap=round] (5,24) .. controls (12,28) and (25,24) .. (25,17) -- (22,7);
\draw[line width=0.8pt,line cap=round] (1,25) .. controls (12,31) and (28,28) .. (30,20) -- (30,8);
\end{tikzpicture}|\amalg}}E_1\cup E_2
\]

% G02: dividing rule; source origin (300,887). The wide fixed rectangle retains its left placement.
\figure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm]
\path[use as bounding box] (0,0) rectangle (1300,25);
\draw[line width=0.3pt,line cap=round] (2,14) .. controls (40,6) and (105,11) .. (145,8) .. controls (183,6) and (222,4) .. (237,8) .. controls (239,9) and (237,12) .. (239,13);
\end{tikzpicture}}

% slanted
\reversemarginpar
\margin{\unsure{introduire|introduisons} la partition $\unsure{\Pi|\pi}_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$}
\normalmarginpar
\deleted{Supposons}

Soit $J\subset I$ tel que $I=J\amalg\{i\}$.

Consid\unsure{e|é}rons la partition
% G03: insertion of Pi_J and bent guide; source origin (1215,1100), fixed rectangle and base-west text anchors.
\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(pjbase)]
\coordinate (pjbase) at (0,120);
\path[use as bounding box] (0,0) rectangle (175,140);
\begin{scope}[overlay]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (10,60) {\inserted{$\Pi_J$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (100,120) {de};
\draw[line width=0.3pt,line cap=round] (65,111) .. controls (67,91) and (91,90) .. (119,85) .. controls (137,83) and (148,80) .. (151,73);
\end{scope}
\end{tikzpicture}
$X$ \deleted{définie} définie par les $\deleted{\unsure{\Sigma}}E_j$ $(j\in J)$, \unsure{\deleted{et}|et} intersection des partitions
% G04: ternaires Pi_j and its two-branch caret; source origin (950,1350).
\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(ternbase)]
\coordinate (ternbase) at (0,100);
\path[use as bounding box] (0,0) rectangle (300,110);
\begin{scope}[overlay]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (20,45) {\inserted{ternaires $\Pi_j$}};
\draw[line width=0.3pt,line cap=round] (180,45) .. controls (206,43) and (223,49) .. (234,100);
\draw[line width=0.6pt,line cap=round] (234,100) -- (277,37);
\end{scope}
\end{tikzpicture}
de $X$ $(j\in J)$ définies par les $E_j$ \deleted{$\unsure{E|\in}$} $(j\in J)$
\[
X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}
% M03: detached short mark near the Sigma head and alpha. Dotless j avoids drawing an additional dot.
% Outer source origin (1145,1624); inner origin is explicitly translated to (1192,1627).
\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(sigbase)]
\coordinate (sigbase) at (0,70);
\path[use as bounding box] (0,0) rectangle (110,88);
\begin{scope}[overlay]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,70) {$\Sigma_{\jmath}^{\alpha}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (47,3) {$\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(mthreebase)]
\coordinate (mthreebase) at (0,0);
\path[use as bounding box] (0,0) rectangle (7,7);
\fill (1,6) -- (0,4) -- (3,0) -- (5,1) -- (6,3) -- cycle;
\end{tikzpicture}}$};
\end{scope}
\end{tikzpicture}
\hspace{3cm}\raisebox{-0.45cm}{$\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(mtwobase)]
% M02a and M02b: source origin (1568,1738); two separate dark specks, with unestablished role and hand.
\coordinate (mtwobase) at (0,0);
\path[use as bounding box] (0,0) rectangle (13,17);
\fill (8,3) -- (10,0) -- (12,3) -- (11,5) -- (8,6) -- cycle;
\fill (1,11) -- (4,10) -- (6,12) -- (3,15) -- (1,14) -- cycle;
\end{tikzpicture}}$}
\]

-- c'est aussi la partition définie par celle de $\displaystyle\bigcup_{j\in J}E_j$ en les $E_j$, et la partition
% G05: raised Pi_J ring and its curved guide; source origin (770,1970).
\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(pjringbase)]
\coordinate (pjringbase) at (0,85);
\path[use as bounding box] (0,0) rectangle (165,110);
\begin{scope}[overlay]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,40) {\inserted{$\Pi_J^{\unsure{\circ|0}}$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (60,85) {de};
\draw[line width=0.3pt,line cap=round] (40,84) .. controls (37,64) and (60,58) .. (82,50) .. controls (110,40) and (128,30) .. (122,24);
\end{scope}
\end{tikzpicture}
$\displaystyle X\setminus\mathop{\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(unionbase)]
% G06: source origin (1115,1975); cup and visible transverse stroke; its mathematical role remains unassigned.
\coordinate (unionbase) at (0,58);
\path[use as bounding box] (0,0) rectangle (70,62);
\draw[line width=0.5pt,line cap=round] (14,4) .. controls (8,20) and (10,45) .. (26,54) .. controls (42,65) and (67,48) .. (65,22) .. controls (65,12) and (63,7) .. (61,4);
\draw[line width=0.5pt,line cap=round] (7,16) -- (56,14);
\end{tikzpicture}}}\limits_{j\in J}E_j$ intersection des partitions binaires $\Pi_{J,j}^{\circ}$
% G07: inserted condition and long hooked guide over induites; source origin (1235,2070).
\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(condbase)]
\coordinate (condbase) at (0,100);
\path[use as bounding box] (0,0) rectangle (320,120);
\begin{scope}[overlay]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (55,35) {\inserted{$(j\in J)$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (45,100) {induites};
\draw[line width=0.3pt,line cap=round] (5,97) .. controls (-4,81) and (17,55) .. (70,53) .. controls (126,59) and (188,58) .. (220,42) .. controls (224,40) and (221,36) .. (217,33);
\end{scope}
\end{tikzpicture}
% G08: inserted U subscript correction and guide; source origin (330,2160).
\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(ubase)]
\coordinate (ubase) at (0,100);
\path[use as bounding box] (0,0) rectangle (145,160);
\begin{scope}[overlay]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,100) {sur};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (35,55) {\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}};
\draw[line width=0.3pt,line cap=round] (42,63) .. controls (65,70) and (108,64) .. (119,104) .. controls (121,120) and (122,130) .. (123,134);
\end{scope}
\end{tikzpicture}
$\displaystyle X\setminus\bigcup_{j\in J}E_j$ par les $\Pi_j$ $(\unsure{g|j}\in J)$. Pour
% archive sheet number: 16



{
  "differences": [
    {
      "id": "D01",
      "location": "Opening cancelled clause: first indexed letter",
      "C": "\\unsure{E_i|\\Sigma_i}",
      "H": "E_i",
      "reading": "E_i",
      "evidence": "A left upright and three surviving horizontal arms support E; the indexed form is kept inside the cancellation.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop01_opening.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1040,
          215,
          1140,
          285
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 01",
      "C_source_local_part": "E_i / Sigma_i"
    },
    {
      "id": "D02",
      "location": "Opening cancelled clause: short verb",
      "C": "\\unsure{est}",
      "H": "soit",
      "reading": "\\unsure{est|soit}",
      "evidence": "Crossing strokes cover the middle letters; a short opening loop and tall terminal stroke support est, with soit still possible.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop01_opening.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1135,
          228,
          1265,
          278
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 01",
      "C_source_local_part": "est",
      "qualification": "H soit remains an explicit alternative; this is a qualified primary-candidate difference."
    },
    {
      "id": "D03",
      "location": "Opening cancelled clause: rare/dense",
      "C": "\\unsure{rare|dense}",
      "H": "rare",
      "reading": "rare",
      "evidence": "The low sequence has two short r-like shoulders and a rounded ending; rare is readable through the cancellation.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop01_opening.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1250,
          237,
          1380,
          276
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 01",
      "C_source_local_part": "rare / dense"
    },
    {
      "id": "D04",
      "location": "Full stop after cancelled X",
      "C": "X$.}",
      "H": "X$}",
      "reading": "X$.}",
      "evidence": "A separate dark point follows the crossed X before the lower parenthetical continuation.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop01_opening.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1535,
          237,
          1610,
          289
        ]
      }
    },
    {
      "id": "D05",
      "location": "Raised on ait above opening cancellation",
      "C": "\\inserted{on ait}",
      "H": "on ait",
      "reading": "\\inserted{on ait}",
      "evidence": "The two words sit on a distinct raised baseline above the crossed clause.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop01_opening.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1135,
          185,
          1350,
          233
        ]
      }
    },
    {
      "id": "D06",
      "location": "Opening of parenthetical after on ait",
      "C": "si",
      "H": "où",
      "reading": "si",
      "evidence": "After the opening curve, the small s-form is followed by a separate upright i; the reading si is retained.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop01_opening.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1390,
          180,
          1475,
          235
        ]
      }
    },
    {
      "id": "D07",
      "location": "Cancelled sentence above the two equalities",
      "C": "\\unsure{trouve}",
      "H": "trouve",
      "reading": "\\unsure{trouve}",
      "evidence": "The tall t and several low returns survive; the horizontal cancellation merges the remaining short letter strokes.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop02_cancelled_sentence.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          548,
          325,
          735,
          380
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 02",
      "C_source_local_part": "trouve"
    },
    {
      "id": "D08",
      "location": "End of first upper equality",
      "C": "E_i",
      "H": "E_i,",
      "reading": "E_i",
      "evidence": "The enlarged space after the dotted index is clear through the right context; no separate comma is recovered there.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop03_equalities.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          935,
          425,
          1090,
          500
        ]
      }
    },
    {
      "id": "D09",
      "location": "Detached point far right of second upper equality",
      "C": "E_i .",
      "H": "E_i .",
      "reading": "M01: locally qualified literal triangular point; period is retained as an interpretation alternative.",
      "evidence": "A compact triangular point lies well to the right of E_i on the lower equality level. Its shape is clear; its punctuation role remains open.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop03_equalities.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1168,
          554,
          1185,
          571
        ]
      },
      "graphic": "M01",
      "shape_confidence": "high",
      "role_confidence": "low",
      "qualification": "Both witnesses period readings remain supported alternatives. One physical point is represented once."
    },
    {
      "id": "D10",
      "location": "Prose before third equality",
      "C": "Alors je dis qu'on a",
      "H": "Alors je dis que",
      "reading": "Alors je dis qu'on a",
      "evidence": "The apostrophe and low on run follow qu; a small separate final a is visible at the right endpoint.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          300,
          620,
          1000,
          775
        ]
      },
      "half_evidence": "half a, same coordinates as the full scan"
    },
    {
      "id": "D11",
      "location": "Third equality: first join",
      "C": "\\unsure{\\cup|\\amalg}",
      "H": "\\cup",
      "reading": "G01: locally qualified retraced cup graphic, with amalg alternative.",
      "evidence": "One shared left upright and two closely spaced right returns form a heavy overdrawn cup-like sign. The right-hand join after E_1 has a separate simple curve.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop04_join.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          943,
          780,
          984,
          817
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 03",
      "C_source_local_part": "first join",
      "graphic": "G01",
      "qualification": "Original cup/amalg uncertainty is retained. The change records the visible retracing geometry, without assigning a writing sequence."
    },
    {
      "id": "D12",
      "location": "Dividing rule below third equality",
      "C": "\\rule{2.4cm}{0.3pt}",
      "H": "(no corresponding entry in H)",
      "reading": "G02: bowed single rule with a short hooked right end.",
      "evidence": "The rule rises gently and has a small downturned right endpoint; it occupies the left part of the writing area.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          298,
          884,
          545,
          913
        ]
      },
      "graphic": "G02",
      "half_evidence": "half a, same coordinates as the full scan",
      "H_absence": "No rule is transcribed in the supplied H body."
    },
    {
      "id": "D13",
      "location": "First word of angled margin note",
      "C": "introduire",
      "H": "introduisons",
      "reading": "\\unsure{introduire|introduisons}",
      "evidence": "The ending is compressed into a low connected run and hooked terminal; introduire is the stronger reading, with the longer H ending still supported.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop05_margin.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          45,
          945,
          255,
          1110
        ]
      },
      "qualification": "H introduisons survives as an explicit alternative."
    },
    {
      "id": "D14",
      "location": "Angled margin note: partition letter",
      "C": "\\unsure{\\Pi|\\pi}_j",
      "H": "\\Pi_j",
      "reading": "\\unsure{\\Pi|\\pi}_j",
      "evidence": "A joined top and two descending legs are visible. The compact size and curved right leg leave the case unresolved.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop05_margin.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          28,
          1220,
          108,
          1320
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 04",
      "C_source_local_part": "Pi_j / pi_j"
    },
    {
      "id": "D15",
      "location": "Angled margin note: under-form of E_j and H terminal ill",
      "C": "\\deleted{\\unsure{\\Sigma}}E_j",
      "H": "E_j ... \\ill{}",
      "reading": "\\deleted{\\unsure{\\Sigma}}E_j",
      "evidence": "Angular diagonal remnants are covered by the darker E strokes. The note ends at its closing brace; the edge fragments belong to adjacent main writing.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop05_margin.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          125,
          1155,
          191,
          1222
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 04",
      "C_source_local_part": "crossed Sigma",
      "H_physical_parent": "H.marginal.trailing_ill",
      "qualification": "The terminal H placeholder is collated once here with the locally recoverable qualified predecessor; no further word is supplied after the brace."
    },
    {
      "id": "D16",
      "location": "Beginning of main partition paragraph: accent",
      "C": "Considérons",
      "H": "Considérons",
      "reading": "Consid\\unsure{e|é}rons",
      "evidence": "The enlarged word supplies its complete connected letters; a separate acute over the relevant vowel is not securely isolated from the tall neighbouring return.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop14_considerons.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          315,
          1145,
          725,
          1220
        ]
      },
      "qualification": "The accented witness spelling remains an explicit alternative."
    },
    {
      "id": "D17",
      "location": "Raised Pi_J before de X: curved guide",
      "C": "\\inserted{\\Pi_J}",
      "H": "\\add{\\Pi_J}",
      "reading": "Inserted Pi_J plus G03 curved attachment guide.",
      "evidence": "A long bent curve runs below the raised partition name into the following de; it is preserved in addition to the insertion annotation.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1215,
          1100,
          1390,
          1240
        ]
      },
      "graphic": "G03",
      "half_evidence": "half a, same coordinates as the full scan"
    },
    {
      "id": "D18",
      "location": "Cancelled word after de X",
      "C": "\\deleted{\\unsure{des parties|définie}}",
      "H": "\\struck{définie}",
      "reading": "\\deleted{définie}",
      "evidence": "The small initial d loop, tall descending f and following short letter sequence are readable beneath the single horizontal strike.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          415,
          1265,
          657,
          1390
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 05",
      "C_source_local_part": "des parties / définie",
      "half_evidence": "half b, bbox [415,164,657,289], origin at full-scan y=1101"
    },
    {
      "id": "D19",
      "location": "Earlier E_j in par les E_j: overwritten predecessor",
      "C": "\\deleted{\\Sigma}E_j (source doubt table qualifies Sigma)",
      "H": "E_j",
      "reading": "\\deleted{\\unsure{\\Sigma}}E_j",
      "evidence": "The live E has three dark arms; diagonal remnants form an X-like crossing within it, leaving Sigma as a qualified predecessor.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop06_old_sigma.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1280,
          1275,
          1370,
          1380
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 07",
      "C_source_local_part": "under E_j",
      "qualification": "The C table already qualifies this physical under-form although C.tex prints it without unsure."
    },
    {
      "id": "D20",
      "location": "Opening of intersection: et and its cancellation state",
      "C": "\\deleted{\\unsure{et}}",
      "H": "\\struck{intersection}\\add{intersection}",
      "reading": "\\unsure{\\deleted{et}|et} intersection",
      "evidence": "A small loop and tall return precede the main word. Their low joining stroke merges with the apparent crossing, leaving the local cancellation target uncertain.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop07_intersection.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          325,
          1410,
          425,
          1480
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 06",
      "C_source_local_part": "et",
      "qualification": "The selected primary state is cancelled et; live et remains explicit. The H cancelled/added intersection sequence is collated once as this physical opening cluster."
    },
    {
      "id": "D21",
      "location": "The longer word intersection",
      "C": "\\unsure{intersection}",
      "H": "\\add{intersection}",
      "reading": "intersection",
      "evidence": "The longer sequence has the tall internal strokes, low joined middle and terminal tion run needed for intersection.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop07_intersection.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          400,
          1400,
          650,
          1480
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 06",
      "C_source_local_part": "intersection",
      "physical_parent": "D20",
      "qualification": "H state qualification is recorded under D20; the longer live word agrees."
    },
    {
      "id": "D22",
      "location": "Raised ternaires Pi_j and caret",
      "C": "\\inserted{ternaires \\Pi_j}",
      "H": "\\add{ternaires \\Pi_j}",
      "reading": "Inserted ternaires Pi_j plus G04 two-branch caret.",
      "evidence": "A shallow left branch descends to the insertion point; a stronger oblique right branch rises from the same point.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          950,
          1350,
          1250,
          1460
        ]
      },
      "graphic": "G04",
      "half_evidence": "half b bbox [950,249,1250,359], origin at full-scan y=1101"
    },
    {
      "id": "D23",
      "location": "Isolated crossed sign after later E_j",
      "C": "\\deleted{\\unsure{E|\\in}}",
      "H": "\\ill{}",
      "reading": "\\deleted{\\unsure{E|\\in}}",
      "evidence": "A narrow two-lobed form and an oblique crossing survive before the following parenthesis; E and membership remain plausible readings.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop08_late_cancel.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1175,
          1505,
          1225,
          1580
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 07",
      "C_source_local_part": "after later E_j",
      "H_physical_parent": "H.body.after_Ej.ill"
    },
    {
      "id": "D24",
      "location": "Lower display: small detached mark by Sigma head and alpha",
      "C": "\\Sigma_j^\\alpha",
      "H": "\\Sigma_j^\\alpha",
      "reading": "M03: local qualified short dark mark, with dotless j used in the text node to avoid a second printed dot.",
      "evidence": "The crop shows a short separate dark piece above the Sigma head, immediately left of alpha. Its possible attachment to the j remains open.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop09_display_marks.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1188,
          1623,
          1203,
          1640
        ]
      },
      "graphic": "M03",
      "shape_confidence": "high",
      "role_confidence": "low",
      "qualification": "This records the local placement and unresolved attachment, without assigning an extra mathematical operation."
    },
    {
      "id": "D25",
      "location": "Two detached specks at right of lower display",
      "C": null,
      "H": "(no corresponding entry in H)",
      "reading": "M02a and M02b: two separate qualified dark-speck paths.",
      "evidence": "Two compact dark pieces lie diagonally apart in the right blank area, below the formula level; neither yields a secure character candidate.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop09_display_marks.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1568,
          1738,
          1581,
          1755
        ]
      },
      "graphic": "M02a; M02b",
      "shape_confidence": "high",
      "role_confidence": "low",
      "hand": "undetermined hand",
      "surface_origin": "unestablished"
    },
    {
      "id": "D26",
      "location": "Inserted lower partition name: raised ring",
      "C": "\\Pi_J^{\\unsure{\\circ|0}}",
      "H": "\\Pi_J^0",
      "reading": "\\Pi_J^{\\unsure{\\circ|0}}",
      "evidence": "The raised closed ring has no decisive feature separating the circle and zero candidates at this scale.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop10_pi_union.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          775,
          1970,
          865,
          2030
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 08",
      "C_source_local_part": "Pi_J above de",
      "qualification": "H zero remains an explicit alternative."
    },
    {
      "id": "D27",
      "location": "Guide under inserted Pi_J with ring",
      "C": "\\inserted{\\Pi_J^{\\unsure{\\circ|0}}}",
      "H": "\\add{\\Pi_J^0}",
      "reading": "The same insertion with G05 curved guide into de.",
      "evidence": "A curved stroke begins low at the left of de, rises beneath the raised name and ends with a short turn.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop10_pi_union.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          805,
          1988,
          902,
          2060
        ]
      },
      "graphic": "G05"
    },
    {
      "id": "D28",
      "location": "First complement after inserted Pi_J: transverse union stroke",
      "C": "\\unsure{\\overline{\\bigcup}|\\bigcup}",
      "H": "\\bigcup",
      "reading": "G06: literal cup with short transverse stroke, locally qualified as to mathematical role.",
      "evidence": "The horizontal begins slightly left of the cup stem and ends before the right stem. Its presence is clear; the path preserves its height inside the cup mouth.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crop10_pi_union.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1115,
          1975,
          1185,
          2037
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 11",
      "C_source_local_part": "bar on union / plain union",
      "graphic": "G06",
      "role_confidence": "low",
      "qualification": "The source doubt about presence of a stroke is resolved. Its mathematical role remains separately qualified; the transcription uses the literal drawn form."
    },
    {
      "id": "D29",
      "location": "Binary partition name: second raised ring",
      "C": "\\Pi_{J,j}^{\\circ} (qualified by source row 8)",
      "H": "\\Pi_{J,j}^0",
      "reading": "\\Pi_{J,j}^{\\circ}, sharing the first ring qualification",
      "evidence": "The second raised small ring is visible above the two distinct indices J,j. Its circle/zero uncertainty is retained under the first-occurrence convention.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop11_binary.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1090,
          2115,
          1225,
          2205
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 08",
      "C_source_local_part": "binary partition name",
      "qualification": "The original C compound row covers this second occurrence even though C.tex has no second unsure macro; H zero remains a supported alternative."
    },
    {
      "id": "D30",
      "location": "Inserted condition and guide above induites",
      "C": "\\inserted{(j\\in J)}",
      "H": "\\add{(j\\in J)} (induites",
      "reading": "Inserted condition plus G07 long hooked guide.",
      "evidence": "The left curve continues across the top of induites and finishes with a small right hook; it is drawn as one connected guide.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop11_binary.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1235,
          2070,
          1560,
          2190
        ]
      },
      "graphic": "G07"
    },
    {
      "id": "D31",
      "location": "H opening parenthesis before induites",
      "C": "induites",
      "H": "(induites",
      "reading": "induites, with G07 above it",
      "evidence": "The curve read in H as an opening parenthesis is continuous with the long guide over the word.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crop11_binary.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1235,
          2105,
          1285,
          2178
        ]
      },
      "physical_parent": "D30",
      "qualification": "This local H punctuation interpretation is recorded without a second H change count for the same guide cluster."
    },
    {
      "id": "D32",
      "location": "Inserted U: repeated subscript forms",
      "C": "U_{\\deleted{\\unsure{J|j}}J}",
      "H": "U_J",
      "reading": "U_{\\unsure{\\deleted{J}J|\\deleted{j}J|J}}",
      "evidence": "Two displaced lower hooks are visible under the shared upper material. They support the old/live J/j readings and a single retraced J reading.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop12_U.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          365,
          2160,
          430,
          2235
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 12",
      "C_source_local_part": "U subscript under-form",
      "qualification": "The original J/j doubt remains. Complete-state alternatives preserve the additional uncertainty about a cancelled predecessor versus retracing."
    },
    {
      "id": "D33",
      "location": "Insertion state of U_J =",
      "C": "\\inserted{U_{...}={}}",
      "H": "U_J =",
      "reading": "\\inserted{U_{...}={}}",
      "evidence": "The U expression is raised above sur and connected to the gap before X by the descending guide.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop12_U.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          350,
          2155,
          460,
          2240
        ]
      }
    },
    {
      "id": "D34",
      "location": "Long guide beneath inserted U expression",
      "C": "\\inserted{U_{...}={}}",
      "H": "U_J =",
      "reading": "G08: bent guide descending beside sur to its full lower endpoint.",
      "evidence": "The thin stroke travels under the subscript area, bends right and descends beyond the prose baseline.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop12_U.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          368,
          2215,
          460,
          2302
        ]
      },
      "graphic": "G08"
    },
    {
      "id": "D35",
      "location": "Last quantified letter",
      "C": "\\unsure{g|j}",
      "H": "j",
      "reading": "\\unsure{g|j}",
      "evidence": "A compact upper loop sits on a long hooked descender. The local g-like top remains clearer than a simple dotted upright, with j retained.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop13_end.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1235,
          2235,
          1288,
          2317
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 09",
      "C_source_local_part": "g / j",
      "qualification": "H j remains an explicit alternative; no index is selected from the formula context."
    },
    {
      "id": "D36",
      "location": "Closing punctuation after final quantified condition",
      "C": "(g\\in J).",
      "H": "(j\\in J)).",
      "reading": "(\\unsure{g|j}\\in J).",
      "evidence": "One closing curve follows J, followed by a separated full stop.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop13_end.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1388,
          2215,
          1470,
          2300
        ]
      }
    },
    {
      "id": "D37",
      "location": "Final word at right edge",
      "C": "\\unsure{Pour|Puis}",
      "H": "\\uncertain{Pour}",
      "reading": "Pour",
      "evidence": "The capital P, small low o and connected ur ending are recoverable; the entire final hook remains inside the crop.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop13_end.png",
      "bbox": {
        "coordinate_system": "full scan, top-left origin",
        "xyxy": [
          1500,
          2210,
          1640,
          2285
        ]
      },
      "C_source_row": "C_doubts.txt / Doubtful readings / row 10",
      "C_source_local_part": "Pour / Puis",
      "qualification": "The next-sheet wording mentioned in the C table was not used as reading evidence."
    }
  ],
  "doubts": [
    {
      "location": "Opening cancelled verb",
      "reading": "est",
      "alternatives": [
        "soit"
      ],
      "confidence": "low",
      "reason": "Central strokes are merged by the crossing.",
      "crop": "crop01_opening.png",
      "difference": "D02"
    },
    {
      "location": "Cancelled sentence above equalities",
      "reading": "trouve",
      "alternatives": [],
      "confidence": "low",
      "reason": "Only some individual letter strokes survive below the cancellation.",
      "crop": "crop02_cancelled_sentence.png",
      "difference": "D07"
    },
    {
      "location": "Point after second equality",
      "reading": "literal triangular point",
      "alternatives": [
        "period interpretation"
      ],
      "confidence": "low",
      "reason": "Its shape is visible; role and hand are unestablished.",
      "crop": "crop03_equalities.png",
      "difference": "D09"
    },
    {
      "location": "First join in third equality",
      "reading": "retraced cup graphic",
      "alternatives": [
        "amalg"
      ],
      "confidence": "medium",
      "reason": "Overlapping curves and uprights remain under one local qualification.",
      "crop": "crop04_join.png",
      "difference": "D11"
    },
    {
      "location": "First marginal word",
      "reading": "introduire",
      "alternatives": [
        "introduisons"
      ],
      "confidence": "low",
      "reason": "The compressed terminal run does not settle every ending stroke.",
      "crop": "crop05_margin.png",
      "difference": "D13"
    },
    {
      "location": "Marginal partition letter",
      "reading": "Pi_j",
      "alternatives": [
        "pi_j"
      ],
      "confidence": "medium",
      "reason": "Case remains uncertain in the compact two-legged form.",
      "crop": "crop05_margin.png",
      "difference": "D14"
    },
    {
      "location": "Marginal E_j predecessor",
      "reading": "cancelled Sigma",
      "alternatives": [],
      "confidence": "low",
      "reason": "The dark live E covers much of the angled under-form.",
      "crop": "crop05_margin.png",
      "difference": "D15"
    },
    {
      "location": "Consid[e|é]rons",
      "reading": "e",
      "alternatives": [
        "é"
      ],
      "confidence": "low",
      "reason": "An independent acute is not securely isolated from the adjacent tall return.",
      "crop": "crop14_considerons.png",
      "difference": "D16"
    },
    {
      "location": "Earlier E_j predecessor in main text",
      "reading": "cancelled Sigma",
      "alternatives": [],
      "confidence": "low",
      "reason": "Crossing diagonals survive under the live E without fully separating the old letter.",
      "crop": "crop06_old_sigma.png",
      "difference": "D19"
    },
    {
      "location": "Opening before intersection",
      "reading": "cancelled et",
      "alternatives": [
        "live et"
      ],
      "confidence": "low",
      "reason": "Glyph and local cancellation target remain crowded together.",
      "crop": "crop07_intersection.png",
      "difference": "D20"
    },
    {
      "location": "Later isolated crossed sign",
      "reading": "cancelled E",
      "alternatives": [
        "cancelled membership sign"
      ],
      "confidence": "low",
      "reason": "A two-lobed shape and slash survive without resolving the letter/sign.",
      "crop": "crop08_late_cancel.png",
      "difference": "D23"
    },
    {
      "location": "Detached mark by lower Sigma/alpha",
      "reading": "literal short dark piece",
      "alternatives": [
        "attachment as j dot"
      ],
      "confidence": "low",
      "reason": "The physical piece is clear but its attachment and hand remain open.",
      "crop": "crop09_display_marks.png",
      "difference": "D24"
    },
    {
      "location": "Right of lower display",
      "reading": "two literal dark specks",
      "alternatives": [],
      "confidence": "low",
      "reason": "Role, hand and surface origin remain unestablished; no character is supplied.",
      "crop": "crop09_display_marks.png",
      "difference": "D25"
    },
    {
      "location": "First raised ring over Pi_J",
      "reading": "circle",
      "alternatives": [
        "zero"
      ],
      "confidence": "medium",
      "reason": "The small raised ring does not settle the character interpretation.",
      "crop": "crop10_pi_union.png",
      "difference": "D26"
    },
    {
      "location": "Transverse line at union mouth",
      "reading": "literal cup with transverse stroke",
      "alternatives": [
        "barred-union interpretation"
      ],
      "confidence": "low",
      "reason": "Stroke presence is resolved; mathematical role is separately unestablished.",
      "crop": "crop10_pi_union.png",
      "difference": "D28"
    },
    {
      "location": "Second raised ring over binary partition name",
      "reading": "circle",
      "alternatives": [
        "zero"
      ],
      "confidence": "medium",
      "reason": "The repeated ring retains the first-occurrence qualification.",
      "crop": "crop11_binary.png",
      "difference": "D29"
    },
    {
      "location": "U subscript sequence",
      "reading": "cancelled J followed by J",
      "alternatives": [
        "cancelled j followed by J",
        "single retraced J"
      ],
      "confidence": "low",
      "reason": "Two lower hooks share crowded upper strokes, leaving glyph and sequence states open.",
      "crop": "crop12_U.png",
      "difference": "D32"
    },
    {
      "location": "Last quantified letter",
      "reading": "g",
      "alternatives": [
        "j"
      ],
      "confidence": "low",
      "reason": "The small loop and long hooked descender remain compatible with both candidates.",
      "crop": "crop13_end.png",
      "difference": "D35"
    }
  ],
  "notes": {
    "page_content": "Underlined Cas particuliers; opening cancelled wording and raised on ait; two closure equalities; Alors je dis qu'on a and a third equality; a dividing rule; an angled partition note; cancelled Supposons; the main partition paragraph with several raised additions; lower partition display and paragraph ending Pour.",
    "author_own_uncertainty": "No separate verbal uncertainty or question mark is recovered. The exact manuscript assertion Alors je dis qu'on a is retained. The unsure annotations belong to this reading.",
    "title_date_page_counts": "Title Cas particuliers has one underline. No date or separate manuscript page number is recovered. Pencilled archive numeral 16 is recorded only as the prescribed comment, with hand undetermined.",
    "mathematics_led_reading_decisions": "The complement in the opening parenthesis is X setminus Sigma_i as visibly written. The lower transverse union stroke and all doubtful indices are preserved from their own strokes. No mathematical correspondence, proof, numerical geometry comparison, or algebraic repair was used to choose a reading.",
    "H_apparatus": "H page{16} is its page identifier. H note about X setminus Sigma_i and X setminus E_i is editorial apparatus. H emph on the heading conveys the same single emphasis span. H add/struck correspond to insertion/deletion conventions. H uncertain{Pour} adds no independent difference after the word is recovered.",
    "C_scope": "Only the actual Doubtful readings section provides the source doubt identities. Its row 7 qualifies the earlier Sigma even without a C.tex unsure macro; row 8 also covers the second raised ring. Each row and separately named local part is mapped above. The next-sheet words in row 10 were not used.",
    "image_workflow": "Whole scan viewed once for layout; half a once and half b once for full line-by-line reading; all fourteen created crop images viewed once each. No image was reopened after its decision. Crop 14 was added for unresolved accent presence, without remaking another crop.",
    "crop_boundaries": "All deciding target continuations are retained. Crop 05 includes a small edge trace from adjacent main writing near Soit; it supplies no extra marginal word. Crops 02, 09, 10, 11 and 12 contain clipped neighbouring context at their boundaries, while their stated target loci and target endpoints remain in view.",
    "graphic_coordinates": "All local TikZ paths use x=0.01cm and y=-0.01cm, a fixed source origin, and an explicitly declared drawing rectangle. Observed locus boxes are recorded separately from path control points, rectangles and font extents. Inline text uses base-west anchors with zero inner and outer separation. M03 uses the explicitly declared (47,3) translation from outer origin (1145,1624), with its own fixed inner baseline. Coordinate choices and paths are manual visual approximations; no curve-extrema, fitting or image-difference computations were performed.",
    "scope_of_validation": "The structural source check passed. The complete reading.tex and report.json contents were read together, including all local path declarations, words, punctuation, source-row parts, inventories and archive-number comment. Two oversized text outputs truncated the report; bounded text sections supplied every remaining field. No image was reopened. No compiler, renderer, OCR, external research, package installation or delegated reading was used."
  },
  "notation": [
    {
      "location": "Opening and two upper equalities",
      "written": "Signed Sigma with separate closure rules; dotted i indices",
      "latex": "\\Sigma_i^+,\\Sigma_i^-,E_i,\\overline{\\Sigma_i^+},\\overline{\\Sigma_i^-}"
    },
    {
      "location": "Opening abbreviation",
      "written": "comp. conn. with the two points",
      "latex": "comp. conn."
    },
    {
      "location": "Third equality",
      "written": "Separate upper rule over Sigma_12",
      "latex": "\\overline{\\Sigma_{12}}"
    },
    {
      "location": "Soit line and lower partition display",
      "written": "Squared joins with extended foot",
      "latex": "J\\amalg\\{i\\}; E_j\\amalg\\coprod"
    },
    {
      "location": "Main partition display",
      "written": "Product-shaped large sign, alpha lower limit, pi with lowered small ring",
      "latex": "\\coprod_{\\alpha\\in\\pi_0(X\\setminus E_j)}"
    },
    {
      "location": "Lower names",
      "written": "Capital J and smaller j as separate indices, small raised rings",
      "latex": "\\Pi_J^{\\unsure{\\circ|0}},\\Pi_{J,j}^{\\circ}"
    },
    {
      "location": "Three lower indexed unions",
      "written": "First and last open cups; middle cup has a short internal transverse stroke",
      "latex": "\\bigcup_{j\\in J}; G06_{j\\in J};\\bigcup_{j\\in J}"
    },
    {
      "location": "Archive lower left",
      "written": "Pencilled 16",
      "latex": "% archive sheet number: 16"
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The source doubt row for an actual transverse stroke can be resolved as to stroke presence while a local graphical qualification retains its unestablished mathematical role; the report records those two scopes separately.",
    "Small detached pieces can coincide with a dotted letter interpretation. M03 is drawn once with a dotless j node and an explicit local role qualification; no extra operation is supplied.",
    "H has a terminal marginal ill placeholder and an internal body ill placeholder. Each receives one physical-parent entry; the marginal predecessor and the absence of further marginal words are kept together."
  ]
}

--- A
+++ B
@@ -1,9 +1,9 @@
 \scanpage{17}
 \uline{Cas particuliers}
 
-Supposons que $\forall i\in I$, \deleted{$E_i$ \unsure{est|soit} rare dans $X$.} \inserted{on ait} (si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)
+Supposons que $\forall i\in I$, \deleted{$\unsure{E_i|\Sigma_i}$ \unsure{est|soit} \unsure{rare|dense} dans $X$.} \inserted{on ait} (si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)
 
-\deleted{Alors on trouve que}
+\deleted{Alors on \unsure{trouve} que}
 \[
 \begin{aligned}
 \overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\
@@ -14,95 +14,109 @@
 Alors je dis qu'on a
 \[
 \overline{\Sigma_{12}}=\Sigma_{12}
-% G01: retraced cup; full-scan origin (944,783), fixed local rectangle 36 by 36.
-\mathbin{\vcenter{\hbox{\begin{tikzpicture}[x=0.007cm,y=-0.007cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (36,36);
-\draw[line width=0.55pt,line cap=round,line join=round] (7,5) .. controls (7,13) and (7,21) .. (9,25) .. controls (18,33) and (32,30) .. (32,14) -- (30,7);
-\draw[line width=0.4pt,line cap=round,line join=round] (25,7) .. controls (32,20) and (20,32) .. (8,25);
+% G01: two curved passes of the first cup; full-scan origin (946,783).
+\mathbin{\vcenter{\hbox{\begin{tikzpicture}[x=0.014cm,y=-0.014cm]
+\useasboundingbox (0,0) rectangle (36,32);
+\begin{scope}[shift={(-946,-783)}]
+\draw[line width=0.65pt] (950,787) .. controls (949,803) and (953,810) .. (960,810) .. controls (976,812) and (979,800) .. (974,789);
+\draw[line width=0.50pt] (950,788) .. controls (950,802) and (951,807) .. (959,808) .. controls (971,807) and (971,798) .. (968,790);
+\end{scope}
 \end{tikzpicture}}}} E_1\cup E_2
 \]
 
-% G02: short curved separator with downturned right endpoint.
-% Full-scan origin (300,887); fixed local rectangle 240 by 22.
-\figure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (240,22);
-\draw[line width=0.3pt,line cap=round] (2,14) .. controls (70,5) and (181,4) .. (232,8) .. controls (238,9) and (239,10) .. (238,14);
+% G02: shallow separator and downturned right endpoint; full-scan origin (300,888).
+\figure{\begin{tikzpicture}[x=0.012cm,y=-0.012cm]
+\useasboundingbox (0,0) rectangle (242,25);
+\begin{scope}[shift={(-300,-888)}]
+\draw[line width=0.45pt] (303,900) .. controls (359,892) and (483,892) .. (519,893) .. controls (535,893) and (538,897) .. (538,901);
+\end{scope}
 \end{tikzpicture}}
 
 % slanted
 \reversemarginpar
-\margin{introduire la partition $\unsure{\Pi|\pi}_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$}
+\margin{introduire la partition $\Pi_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$
+% G03: short dark wedge to the right of the closing brace in crop05.
+% Its character, role, hand, and possible attachment to neighbouring text remain open.
+\unsure{\begin{tikzpicture}[x=0.25mm,y=0.25mm,baseline=0pt]
+\useasboundingbox (0,0) rectangle (3,4);
+\fill (0,0) -- (0.4,3) -- (2.2,2) -- cycle;
+\end{tikzpicture}}}
 \normalmarginpar
 \deleted{Supposons}
 
 Soit $J\subset I$ tel que $I=J\amalg\{i\}$.
 
-Considerons la partition
-% G03: upper Pi_J insertion and curved guide. Source origin (1215,1100).
-% Fixed rectangle 175 by 135; base-west anchors and zero node separations.
-\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(pide.base)]
-\path[use as bounding box] (0,0) rectangle (175,135);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (6,65) {\inserted{$\Pi_J$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (pide) at (105,124) {de};
-\draw[line width=0.3pt,line cap=round] (68,120) .. controls (73,91) and (129,99) .. (153,84) -- (152,79);
+Consid\unsure{e|é}rons la partition
+% G04: first Pi_J insertion and its curved guide. Fixed source origin (1218,1105).
+\begin{tikzpicture}[x=0.010cm,y=-0.010cm,baseline=(live.base)]
+\useasboundingbox (0,0) rectangle (180,130);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (0,58) {\inserted{$\Pi_J$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (70,115) {de};
+\begin{scope}[shift={(-1218,-1105)}]
+\draw[line width=0.40pt] (1282,1226) .. controls (1284,1204) and (1306,1196) .. (1338,1192) .. controls (1354,1189) and (1367,1188) .. (1370,1183);
+\end{scope}
 \end{tikzpicture}
-$X$ \deleted{definie} definie par les $\deleted{\Sigma}E_j$ $(j\in J)$, \deleted{et} \unsure{Intersection|intersection} des partitions
-% G04: ternaires Pi_j insertion and its long bent caret. Source origin (970,1345).
-\begin{tikzpicture}[x=0.0075cm,y=-0.0075cm,baseline=(terde.base)]
-\path[use as bounding box] (0,0) rectangle (335,135);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,57) {\inserted{ternaires $\Pi_j$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (terde) at (270,118) {de};
-\draw[line width=0.35pt,line cap=round,line join=round] (161,64) .. controls (177,65) and (206,70) .. (215,89) -- (218,105) .. controls (233,80) and (246,62) .. (260,48);
+$X$ \deleted{definie} definie par les $\deleted{\Sigma}E_j$ $(j\in J)$, \deleted{\unsure{et}} intersection des partitions
+% G05: ternaires Pi_j and the long V-shaped guide; source origin (947,1345).
+\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=(live.base)]
+\useasboundingbox (0,0) rectangle (352,140);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (20,52) {\inserted{ternaires $\Pi_j$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (292,110) {de $X$};
+\begin{scope}[shift={(-947,-1345)}]
+\draw[line width=0.45pt] (1127,1407) .. controls (1161,1407) and (1180,1418) .. (1184,1451) .. controls (1193,1432) and (1214,1404) .. (1228,1390);
+\end{scope}
 \end{tikzpicture}
-$X$ $(j\in J)$ definies par les $E_j$ \deleted{$\unsure{\in|E}$} $(j\in J)$
+$(j\in J)$ definies par les $E_j$ $\unsure{\deleted{\in}|\deleted{E}|\notin}$ $(j\in J)$
 \[
-X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}\Sigma_j^{\unsure{\prime|\cdot}\alpha}
+X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}\Sigma_j^\alpha
 \]
-% G05 is the small detached oblique mark immediately before upper alpha.
-% It is represented once by the qualified prime/dot candidate above; no role is assigned.
 
-% G11: two detached marks at far right between display and lower prose.
-% Full-scan origin (1567,1735), fixed local rectangle 18 by 20.
-% Shapes only: character, role, hand and surface origin remain unestablished.
-\margin{\unsure{\begin{tikzpicture}[x=0.02cm,y=-0.02cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (18,20);
-\fill (9,5) .. controls (11,4) and (13,6) .. (11,9) .. controls (8,10) and (8,7) .. cycle;
-\fill (4,12) .. controls (7,11) and (8,14) .. (5,15) .. controls (3,16) and (2,13) .. cycle;
-\end{tikzpicture}}}
-
--- c'est aussi la partition definie par celle de $\displaystyle\unsure{.}\,\bigcup_{j\in J}E_j$ en les $E_j$, et la partition
-% G06 is the detached baseline point before the first indexed union, represented once above.
-% G07: lower Pi_J insertion and curved guide. Source origin (770,1965).
-\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=(lowde.base)]
-\path[use as bounding box] (0,0) rectangle (145,100);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,54) {\inserted{$\Pi_J^{\unsure{\circ|0}}$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (lowde) at (69,85) {de};
-\draw[line width=0.3pt,line cap=round] (39,89) .. controls (40,65) and (55,62) .. (76,56) .. controls (93,51) and (119,40) .. (122,34) -- (118,30);
+-- c'est aussi la partition definie par celle de
+% G06: detached baseline point before the first union, role and hand unresolved.
+$\displaystyle \unsure{\mathord{\begin{tikzpicture}[x=0.025cm,y=-0.025cm,baseline=0pt]
+\useasboundingbox (0,0) rectangle (9,7);
+\begin{scope}[shift={(-734,-1902)}]
+\fill (735,1903) -- (741,1902) -- (741,1907) -- (735,1907) -- cycle;
+\end{scope}
+\end{tikzpicture}}}\bigcup_{j\in J}E_j$ en les $E_j$, et la partition
+% G07: raised Pi_J ring and bent guide; source origin (752,1973).
+\begin{tikzpicture}[x=0.010cm,y=-0.010cm,baseline=(live.base)]
+\useasboundingbox (0,0) rectangle (168,110);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (15,40) {\inserted{$\Pi_J^{\unsure{\circ|0}}$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (91,80) {de};
+\begin{scope}[shift={(-752,-1973)}]
+\draw[line width=0.40pt] (808,2055) .. controls (803,2038) and (826,2029) .. (852,2022) .. controls (870,2018) and (894,2005) .. (891,1997) -- (888,1994);
+\end{scope}
 \end{tikzpicture}
 $\displaystyle X\setminus
-% G08: union with visible transverse stroke; interpretation of stroke stays qualified.
-% Full-scan origin (1115,1970), fixed local rectangle 80 by 75.
-\mathop{\unsure{\vcenter{\hbox{\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (80,75);
-\draw[line width=0.45pt,line cap=round] (18,9) .. controls (13,34) and (18,60) .. (38,63) .. controls (61,67) and (70,39) .. (63,10);
-\draw[line width=0.4pt,line cap=round] (12,20) .. controls (26,20) and (39,17) .. (59,18);
-\end{tikzpicture}}}}}\limits_{j\in J}E_j$
-intersection des partitions binaires $\Pi_{J,j}^{\circ}$
-% G09: inserted quantifier and guide over induites. Source origin (1230,2070).
-% The recurring circle/zero doubt is marked at its first occurrence above.
-\begin{tikzpicture}[x=0.0075cm,y=-0.0075cm,baseline=(induites.base)]
-\path[use as bounding box] (0,0) rectangle (335,115);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (60,45) {\inserted{$(j\in J)$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (induites) at (52,91) {induites};
-\draw[line width=0.3pt,line cap=round] (14,92) .. controls (0,72) and (30,57) .. (53,53) .. controls (99,66) and (189,54) .. (219,41) .. controls (224,39) and (216,32) .. (214,31);
+% G08: literal cup and transverse upper stroke; source origin (1118,1976).
+\mathop{\vcenter{\hbox{\begin{tikzpicture}[x=0.009cm,y=-0.009cm]
+\useasboundingbox (0,0) rectangle (69,70);
+\begin{scope}[shift={(-1118,-1976)}]
+\draw[line width=0.45pt] (1130,1980) .. controls (1125,1999) and (1126,2020) .. (1137,2034) .. controls (1152,2045) and (1170,2034) .. (1176,2014) .. controls (1180,2003) and (1177,1986) .. (1172,1980);
+\draw[line width=0.40pt] (1123,1990) .. controls (1141,1990) and (1156,1988) .. (1168,1988);
+\end{scope}
+\end{tikzpicture}}}}\limits_{j\in J}E_j$ intersection des partitions binaires $\Pi_{J,j}^{\circ}$
+% The upper ring's local circle/zero doubt is recorded also at this second occurrence.
+% G09: inserted (j in J), live induites, and one continuous hooked guide.
+% Fixed source origin (1234,2070); the guide supplies no extra prose parenthesis.
+\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=(live.base)]
+\useasboundingbox (0,0) rectangle (320,110);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (45,35) {\inserted{$(j\in J)$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (50,84) {induites};
+\begin{scope}[shift={(-1234,-2070)}]
+\draw[line width=0.40pt] (1244,2162) .. controls (1237,2145) and (1263,2122) .. (1298,2117) .. controls (1350,2130) and (1433,2110) .. (1456,2105) .. controls (1461,2103) and (1456,2100) .. (1452,2098);
+\end{scope}
 \end{tikzpicture}
-% G10: inserted U_J= and guide curling down to the right of sur.
-% Full-scan origin (320,2155); fixed local rectangle 145 by 155.
-\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(sur.base)]
-\path[use as bounding box] (0,0) rectangle (145,155);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (43,61) {\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (sur) at (0,111) {sur};
-\draw[line width=0.3pt,line cap=round] (56,72) .. controls (88,81) and (111,74) .. (124,99) .. controls (133,121) and (132,138) .. (136,148);
+% G10: U-subscript correction states and its long guide into the sur/X gap.
+% Fixed source origin (311,2140); glyph/state alternatives carry no chronology.
+\begin{tikzpicture}[x=0.010cm,y=-0.010cm,baseline=(live.base)]
+\useasboundingbox (0,0) rectangle (151,165);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (56,75) {\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (20,123) {sur};
+\begin{scope}[shift={(-311,-2140)}]
+\draw[line width=0.40pt] (375,2228) .. controls (392,2234) and (422,2234) .. (434,2245) .. controls (447,2259) and (448,2277) .. (451,2294);
+\end{scope}
 \end{tikzpicture}
 $\displaystyle X\setminus\bigcup_{j\in J}E_j$ par les $\Pi_j$ $(\unsure{g|j}\in J)$. Pour
 % archive sheet number: 16

--- A
+++ C
@@ -3,106 +3,132 @@
 
 Supposons que $\forall i\in I$, \deleted{$E_i$ \unsure{est|soit} rare dans $X$.} \inserted{on ait} (si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)
 
-\deleted{Alors on trouve que}
+\deleted{Alors on \unsure{trouve} que}
 \[
 \begin{aligned}
 \overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\
-\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i .
+\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i\hspace{1.5cm}
+% M01: source origin (1172,557); observed triangular point, period interpretation retained as alternative.
+\mathpunct{\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(monebase)]
+\coordinate (monebase) at (0,6);
+\path[use as bounding box] (0,0) rectangle (7,7);
+\fill (1,5) -- (3,1) -- (5,0) -- (7,5) -- cycle;
+\end{tikzpicture}|.}}
 \end{aligned}
 \]
 
 Alors je dis qu'on a
 \[
 \overline{\Sigma_{12}}=\Sigma_{12}
-% G01: retraced cup; full-scan origin (944,783), fixed local rectangle 36 by 36.
-\mathbin{\vcenter{\hbox{\begin{tikzpicture}[x=0.007cm,y=-0.007cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (36,36);
-\draw[line width=0.55pt,line cap=round,line join=round] (7,5) .. controls (7,13) and (7,21) .. (9,25) .. controls (18,33) and (32,30) .. (32,14) -- (30,7);
-\draw[line width=0.4pt,line cap=round,line join=round] (25,7) .. controls (32,20) and (20,32) .. (8,25);
-\end{tikzpicture}}}} E_1\cup E_2
+% G01: source origin (947,783); primary literal retraced cup, alternative amalg.
+\mathbin{\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(joinbase)]
+\coordinate (joinbase) at (0,29);
+\path[use as bounding box] (0,0) rectangle (33,32);
+\draw[line width=0.8pt,line cap=round] (4,3) .. controls (2,10) and (4,17) .. (5,24);
+\draw[line width=0.65pt,line cap=round] (5,24) .. controls (12,28) and (25,24) .. (25,17) -- (22,7);
+\draw[line width=0.8pt,line cap=round] (1,25) .. controls (12,31) and (28,28) .. (30,20) -- (30,8);
+\end{tikzpicture}|\amalg}}E_1\cup E_2
 \]
 
-% G02: short curved separator with downturned right endpoint.
-% Full-scan origin (300,887); fixed local rectangle 240 by 22.
-\figure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (240,22);
-\draw[line width=0.3pt,line cap=round] (2,14) .. controls (70,5) and (181,4) .. (232,8) .. controls (238,9) and (239,10) .. (238,14);
+% G02: dividing rule; source origin (300,887). The wide fixed rectangle retains its left placement.
+\figure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm]
+\path[use as bounding box] (0,0) rectangle (1300,25);
+\draw[line width=0.3pt,line cap=round] (2,14) .. controls (40,6) and (105,11) .. (145,8) .. controls (183,6) and (222,4) .. (237,8) .. controls (239,9) and (237,12) .. (239,13);
 \end{tikzpicture}}
 
 % slanted
 \reversemarginpar
-\margin{introduire la partition $\unsure{\Pi|\pi}_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$}
+\margin{\unsure{introduire|introduisons} la partition $\unsure{\Pi|\pi}_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$}
 \normalmarginpar
 \deleted{Supposons}
 
 Soit $J\subset I$ tel que $I=J\amalg\{i\}$.
 
-Considerons la partition
-% G03: upper Pi_J insertion and curved guide. Source origin (1215,1100).
-% Fixed rectangle 175 by 135; base-west anchors and zero node separations.
-\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(pide.base)]
-\path[use as bounding box] (0,0) rectangle (175,135);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (6,65) {\inserted{$\Pi_J$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (pide) at (105,124) {de};
-\draw[line width=0.3pt,line cap=round] (68,120) .. controls (73,91) and (129,99) .. (153,84) -- (152,79);
+Consid\unsure{e|é}rons la partition
+% G03: insertion of Pi_J and bent guide; source origin (1215,1100), fixed rectangle and base-west text anchors.
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(pjbase)]
+\coordinate (pjbase) at (0,120);
+\path[use as bounding box] (0,0) rectangle (175,140);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (10,60) {\inserted{$\Pi_J$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (100,120) {de};
+\draw[line width=0.3pt,line cap=round] (65,111) .. controls (67,91) and (91,90) .. (119,85) .. controls (137,83) and (148,80) .. (151,73);
+\end{scope}
 \end{tikzpicture}
-$X$ \deleted{definie} definie par les $\deleted{\Sigma}E_j$ $(j\in J)$, \deleted{et} \unsure{Intersection|intersection} des partitions
-% G04: ternaires Pi_j insertion and its long bent caret. Source origin (970,1345).
-\begin{tikzpicture}[x=0.0075cm,y=-0.0075cm,baseline=(terde.base)]
-\path[use as bounding box] (0,0) rectangle (335,135);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,57) {\inserted{ternaires $\Pi_j$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (terde) at (270,118) {de};
-\draw[line width=0.35pt,line cap=round,line join=round] (161,64) .. controls (177,65) and (206,70) .. (215,89) -- (218,105) .. controls (233,80) and (246,62) .. (260,48);
+$X$ \deleted{définie} définie par les $\deleted{\unsure{\Sigma}}E_j$ $(j\in J)$, \unsure{\deleted{et}|et} intersection des partitions
+% G04: ternaires Pi_j and its two-branch caret; source origin (950,1350).
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(ternbase)]
+\coordinate (ternbase) at (0,100);
+\path[use as bounding box] (0,0) rectangle (300,110);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (20,45) {\inserted{ternaires $\Pi_j$}};
+\draw[line width=0.3pt,line cap=round] (180,45) .. controls (206,43) and (223,49) .. (234,100);
+\draw[line width=0.6pt,line cap=round] (234,100) -- (277,37);
+\end{scope}
 \end{tikzpicture}
-$X$ $(j\in J)$ definies par les $E_j$ \deleted{$\unsure{\in|E}$} $(j\in J)$
+de $X$ $(j\in J)$ définies par les $E_j$ \deleted{$\unsure{E|\in}$} $(j\in J)$
 \[
-X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}\Sigma_j^{\unsure{\prime|\cdot}\alpha}
+X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}
+% M03: detached short mark near the Sigma head and alpha. Dotless j avoids drawing an additional dot.
+% Outer source origin (1145,1624); inner origin is explicitly translated to (1192,1627).
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(sigbase)]
+\coordinate (sigbase) at (0,70);
+\path[use as bounding box] (0,0) rectangle (110,88);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,70) {$\Sigma_{\jmath}^{\alpha}$};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (47,3) {$\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(mthreebase)]
+\coordinate (mthreebase) at (0,0);
+\path[use as bounding box] (0,0) rectangle (7,7);
+\fill (1,6) -- (0,4) -- (3,0) -- (5,1) -- (6,3) -- cycle;
+\end{tikzpicture}}$};
+\end{scope}
+\end{tikzpicture}
+\hspace{3cm}\raisebox{-0.45cm}{$\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(mtwobase)]
+% M02a and M02b: source origin (1568,1738); two separate dark specks, with unestablished role and hand.
+\coordinate (mtwobase) at (0,0);
+\path[use as bounding box] (0,0) rectangle (13,17);
+\fill (8,3) -- (10,0) -- (12,3) -- (11,5) -- (8,6) -- cycle;
+\fill (1,11) -- (4,10) -- (6,12) -- (3,15) -- (1,14) -- cycle;
+\end{tikzpicture}}$}
 \]
-% G05 is the small detached oblique mark immediately before upper alpha.
-% It is represented once by the qualified prime/dot candidate above; no role is assigned.
 
-% G11: two detached marks at far right between display and lower prose.
-% Full-scan origin (1567,1735), fixed local rectangle 18 by 20.
-% Shapes only: character, role, hand and surface origin remain unestablished.
-\margin{\unsure{\begin{tikzpicture}[x=0.02cm,y=-0.02cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (18,20);
-\fill (9,5) .. controls (11,4) and (13,6) .. (11,9) .. controls (8,10) and (8,7) .. cycle;
-\fill (4,12) .. controls (7,11) and (8,14) .. (5,15) .. controls (3,16) and (2,13) .. cycle;
-\end{tikzpicture}}}
-
--- c'est aussi la partition definie par celle de $\displaystyle\unsure{.}\,\bigcup_{j\in J}E_j$ en les $E_j$, et la partition
-% G06 is the detached baseline point before the first indexed union, represented once above.
-% G07: lower Pi_J insertion and curved guide. Source origin (770,1965).
-\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=(lowde.base)]
-\path[use as bounding box] (0,0) rectangle (145,100);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,54) {\inserted{$\Pi_J^{\unsure{\circ|0}}$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (lowde) at (69,85) {de};
-\draw[line width=0.3pt,line cap=round] (39,89) .. controls (40,65) and (55,62) .. (76,56) .. controls (93,51) and (119,40) .. (122,34) -- (118,30);
+-- c'est aussi la partition définie par celle de $\displaystyle\bigcup_{j\in J}E_j$ en les $E_j$, et la partition
+% G05: raised Pi_J ring and its curved guide; source origin (770,1970).
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(pjringbase)]
+\coordinate (pjringbase) at (0,85);
+\path[use as bounding box] (0,0) rectangle (165,110);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,40) {\inserted{$\Pi_J^{\unsure{\circ|0}}$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (60,85) {de};
+\draw[line width=0.3pt,line cap=round] (40,84) .. controls (37,64) and (60,58) .. (82,50) .. controls (110,40) and (128,30) .. (122,24);
+\end{scope}
 \end{tikzpicture}
-$\displaystyle X\setminus
-% G08: union with visible transverse stroke; interpretation of stroke stays qualified.
-% Full-scan origin (1115,1970), fixed local rectangle 80 by 75.
-\mathop{\unsure{\vcenter{\hbox{\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (80,75);
-\draw[line width=0.45pt,line cap=round] (18,9) .. controls (13,34) and (18,60) .. (38,63) .. controls (61,67) and (70,39) .. (63,10);
-\draw[line width=0.4pt,line cap=round] (12,20) .. controls (26,20) and (39,17) .. (59,18);
-\end{tikzpicture}}}}}\limits_{j\in J}E_j$
-intersection des partitions binaires $\Pi_{J,j}^{\circ}$
-% G09: inserted quantifier and guide over induites. Source origin (1230,2070).
-% The recurring circle/zero doubt is marked at its first occurrence above.
-\begin{tikzpicture}[x=0.0075cm,y=-0.0075cm,baseline=(induites.base)]
-\path[use as bounding box] (0,0) rectangle (335,115);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (60,45) {\inserted{$(j\in J)$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (induites) at (52,91) {induites};
-\draw[line width=0.3pt,line cap=round] (14,92) .. controls (0,72) and (30,57) .. (53,53) .. controls (99,66) and (189,54) .. (219,41) .. controls (224,39) and (216,32) .. (214,31);
+$\displaystyle X\setminus\mathop{\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(unionbase)]
+% G06: source origin (1115,1975); cup and visible transverse stroke; its mathematical role remains unassigned.
+\coordinate (unionbase) at (0,58);
+\path[use as bounding box] (0,0) rectangle (70,62);
+\draw[line width=0.5pt,line cap=round] (14,4) .. controls (8,20) and (10,45) .. (26,54) .. controls (42,65) and (67,48) .. (65,22) .. controls (65,12) and (63,7) .. (61,4);
+\draw[line width=0.5pt,line cap=round] (7,16) -- (56,14);
+\end{tikzpicture}}}\limits_{j\in J}E_j$ intersection des partitions binaires $\Pi_{J,j}^{\circ}$
+% G07: inserted condition and long hooked guide over induites; source origin (1235,2070).
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(condbase)]
+\coordinate (condbase) at (0,100);
+\path[use as bounding box] (0,0) rectangle (320,120);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (55,35) {\inserted{$(j\in J)$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (45,100) {induites};
+\draw[line width=0.3pt,line cap=round] (5,97) .. controls (-4,81) and (17,55) .. (70,53) .. controls (126,59) and (188,58) .. (220,42) .. controls (224,40) and (221,36) .. (217,33);
+\end{scope}
 \end{tikzpicture}
-% G10: inserted U_J= and guide curling down to the right of sur.
-% Full-scan origin (320,2155); fixed local rectangle 145 by 155.
-\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(sur.base)]
-\path[use as bounding box] (0,0) rectangle (145,155);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (43,61) {\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (sur) at (0,111) {sur};
-\draw[line width=0.3pt,line cap=round] (56,72) .. controls (88,81) and (111,74) .. (124,99) .. controls (133,121) and (132,138) .. (136,148);
+% G08: inserted U subscript correction and guide; source origin (330,2160).
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(ubase)]
+\coordinate (ubase) at (0,100);
+\path[use as bounding box] (0,0) rectangle (145,160);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,100) {sur};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (35,55) {\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}};
+\draw[line width=0.3pt,line cap=round] (42,63) .. controls (65,70) and (108,64) .. (119,104) .. controls (121,120) and (122,130) .. (123,134);
+\end{scope}
 \end{tikzpicture}
 $\displaystyle X\setminus\bigcup_{j\in J}E_j$ par les $\Pi_j$ $(\unsure{g|j}\in J)$. Pour
 % archive sheet number: 16

--- B
+++ C
@@ -1,121 +1,133 @@
 \scanpage{17}
 \uline{Cas particuliers}
 
-Supposons que $\forall i\in I$, \deleted{$\unsure{E_i|\Sigma_i}$ \unsure{est|soit} \unsure{rare|dense} dans $X$.} \inserted{on ait} (si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)
+Supposons que $\forall i\in I$, \deleted{$E_i$ \unsure{est|soit} rare dans $X$.} \inserted{on ait} (si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)
 
 \deleted{Alors on \unsure{trouve} que}
 \[
 \begin{aligned}
 \overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\
-\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i .
+\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i\hspace{1.5cm}
+% M01: source origin (1172,557); observed triangular point, period interpretation retained as alternative.
+\mathpunct{\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(monebase)]
+\coordinate (monebase) at (0,6);
+\path[use as bounding box] (0,0) rectangle (7,7);
+\fill (1,5) -- (3,1) -- (5,0) -- (7,5) -- cycle;
+\end{tikzpicture}|.}}
 \end{aligned}
 \]
 
 Alors je dis qu'on a
 \[
 \overline{\Sigma_{12}}=\Sigma_{12}
-% G01: two curved passes of the first cup; full-scan origin (946,783).
-\mathbin{\vcenter{\hbox{\begin{tikzpicture}[x=0.014cm,y=-0.014cm]
-\useasboundingbox (0,0) rectangle (36,32);
-\begin{scope}[shift={(-946,-783)}]
-\draw[line width=0.65pt] (950,787) .. controls (949,803) and (953,810) .. (960,810) .. controls (976,812) and (979,800) .. (974,789);
-\draw[line width=0.50pt] (950,788) .. controls (950,802) and (951,807) .. (959,808) .. controls (971,807) and (971,798) .. (968,790);
-\end{scope}
-\end{tikzpicture}}}} E_1\cup E_2
+% G01: source origin (947,783); primary literal retraced cup, alternative amalg.
+\mathbin{\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(joinbase)]
+\coordinate (joinbase) at (0,29);
+\path[use as bounding box] (0,0) rectangle (33,32);
+\draw[line width=0.8pt,line cap=round] (4,3) .. controls (2,10) and (4,17) .. (5,24);
+\draw[line width=0.65pt,line cap=round] (5,24) .. controls (12,28) and (25,24) .. (25,17) -- (22,7);
+\draw[line width=0.8pt,line cap=round] (1,25) .. controls (12,31) and (28,28) .. (30,20) -- (30,8);
+\end{tikzpicture}|\amalg}}E_1\cup E_2
 \]
 
-% G02: shallow separator and downturned right endpoint; full-scan origin (300,888).
-\figure{\begin{tikzpicture}[x=0.012cm,y=-0.012cm]
-\useasboundingbox (0,0) rectangle (242,25);
-\begin{scope}[shift={(-300,-888)}]
-\draw[line width=0.45pt] (303,900) .. controls (359,892) and (483,892) .. (519,893) .. controls (535,893) and (538,897) .. (538,901);
-\end{scope}
+% G02: dividing rule; source origin (300,887). The wide fixed rectangle retains its left placement.
+\figure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm]
+\path[use as bounding box] (0,0) rectangle (1300,25);
+\draw[line width=0.3pt,line cap=round] (2,14) .. controls (40,6) and (105,11) .. (145,8) .. controls (183,6) and (222,4) .. (237,8) .. controls (239,9) and (237,12) .. (239,13);
 \end{tikzpicture}}
 
 % slanted
 \reversemarginpar
-\margin{introduire la partition $\Pi_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$
-% G03: short dark wedge to the right of the closing brace in crop05.
-% Its character, role, hand, and possible attachment to neighbouring text remain open.
-\unsure{\begin{tikzpicture}[x=0.25mm,y=0.25mm,baseline=0pt]
-\useasboundingbox (0,0) rectangle (3,4);
-\fill (0,0) -- (0.4,3) -- (2.2,2) -- cycle;
-\end{tikzpicture}}}
+\margin{\unsure{introduire|introduisons} la partition $\unsure{\Pi|\pi}_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$}
 \normalmarginpar
 \deleted{Supposons}
 
 Soit $J\subset I$ tel que $I=J\amalg\{i\}$.
 
 Consid\unsure{e|é}rons la partition
-% G04: first Pi_J insertion and its curved guide. Fixed source origin (1218,1105).
-\begin{tikzpicture}[x=0.010cm,y=-0.010cm,baseline=(live.base)]
-\useasboundingbox (0,0) rectangle (180,130);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (0,58) {\inserted{$\Pi_J$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (70,115) {de};
-\begin{scope}[shift={(-1218,-1105)}]
-\draw[line width=0.40pt] (1282,1226) .. controls (1284,1204) and (1306,1196) .. (1338,1192) .. controls (1354,1189) and (1367,1188) .. (1370,1183);
+% G03: insertion of Pi_J and bent guide; source origin (1215,1100), fixed rectangle and base-west text anchors.
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(pjbase)]
+\coordinate (pjbase) at (0,120);
+\path[use as bounding box] (0,0) rectangle (175,140);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (10,60) {\inserted{$\Pi_J$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (100,120) {de};
+\draw[line width=0.3pt,line cap=round] (65,111) .. controls (67,91) and (91,90) .. (119,85) .. controls (137,83) and (148,80) .. (151,73);
 \end{scope}
 \end{tikzpicture}
-$X$ \deleted{definie} definie par les $\deleted{\Sigma}E_j$ $(j\in J)$, \deleted{\unsure{et}} intersection des partitions
-% G05: ternaires Pi_j and the long V-shaped guide; source origin (947,1345).
-\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=(live.base)]
-\useasboundingbox (0,0) rectangle (352,140);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (20,52) {\inserted{ternaires $\Pi_j$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (292,110) {de $X$};
-\begin{scope}[shift={(-947,-1345)}]
-\draw[line width=0.45pt] (1127,1407) .. controls (1161,1407) and (1180,1418) .. (1184,1451) .. controls (1193,1432) and (1214,1404) .. (1228,1390);
+$X$ \deleted{définie} définie par les $\deleted{\unsure{\Sigma}}E_j$ $(j\in J)$, \unsure{\deleted{et}|et} intersection des partitions
+% G04: ternaires Pi_j and its two-branch caret; source origin (950,1350).
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(ternbase)]
+\coordinate (ternbase) at (0,100);
+\path[use as bounding box] (0,0) rectangle (300,110);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (20,45) {\inserted{ternaires $\Pi_j$}};
+\draw[line width=0.3pt,line cap=round] (180,45) .. controls (206,43) and (223,49) .. (234,100);
+\draw[line width=0.6pt,line cap=round] (234,100) -- (277,37);
 \end{scope}
 \end{tikzpicture}
-$(j\in J)$ definies par les $E_j$ $\unsure{\deleted{\in}|\deleted{E}|\notin}$ $(j\in J)$
+de $X$ $(j\in J)$ définies par les $E_j$ \deleted{$\unsure{E|\in}$} $(j\in J)$
 \[
-X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}\Sigma_j^\alpha
+X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}
+% M03: detached short mark near the Sigma head and alpha. Dotless j avoids drawing an additional dot.
+% Outer source origin (1145,1624); inner origin is explicitly translated to (1192,1627).
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(sigbase)]
+\coordinate (sigbase) at (0,70);
+\path[use as bounding box] (0,0) rectangle (110,88);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,70) {$\Sigma_{\jmath}^{\alpha}$};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (47,3) {$\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(mthreebase)]
+\coordinate (mthreebase) at (0,0);
+\path[use as bounding box] (0,0) rectangle (7,7);
+\fill (1,6) -- (0,4) -- (3,0) -- (5,1) -- (6,3) -- cycle;
+\end{tikzpicture}}$};
+\end{scope}
+\end{tikzpicture}
+\hspace{3cm}\raisebox{-0.45cm}{$\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(mtwobase)]
+% M02a and M02b: source origin (1568,1738); two separate dark specks, with unestablished role and hand.
+\coordinate (mtwobase) at (0,0);
+\path[use as bounding box] (0,0) rectangle (13,17);
+\fill (8,3) -- (10,0) -- (12,3) -- (11,5) -- (8,6) -- cycle;
+\fill (1,11) -- (4,10) -- (6,12) -- (3,15) -- (1,14) -- cycle;
+\end{tikzpicture}}$}
 \]
 
--- c'est aussi la partition definie par celle de
-% G06: detached baseline point before the first union, role and hand unresolved.
-$\displaystyle \unsure{\mathord{\begin{tikzpicture}[x=0.025cm,y=-0.025cm,baseline=0pt]
-\useasboundingbox (0,0) rectangle (9,7);
-\begin{scope}[shift={(-734,-1902)}]
-\fill (735,1903) -- (741,1902) -- (741,1907) -- (735,1907) -- cycle;
-\end{scope}
-\end{tikzpicture}}}\bigcup_{j\in J}E_j$ en les $E_j$, et la partition
-% G07: raised Pi_J ring and bent guide; source origin (752,1973).
-\begin{tikzpicture}[x=0.010cm,y=-0.010cm,baseline=(live.base)]
-\useasboundingbox (0,0) rectangle (168,110);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (15,40) {\inserted{$\Pi_J^{\unsure{\circ|0}}$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (91,80) {de};
-\begin{scope}[shift={(-752,-1973)}]
-\draw[line width=0.40pt] (808,2055) .. controls (803,2038) and (826,2029) .. (852,2022) .. controls (870,2018) and (894,2005) .. (891,1997) -- (888,1994);
+-- c'est aussi la partition définie par celle de $\displaystyle\bigcup_{j\in J}E_j$ en les $E_j$, et la partition
+% G05: raised Pi_J ring and its curved guide; source origin (770,1970).
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(pjringbase)]
+\coordinate (pjringbase) at (0,85);
+\path[use as bounding box] (0,0) rectangle (165,110);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,40) {\inserted{$\Pi_J^{\unsure{\circ|0}}$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (60,85) {de};
+\draw[line width=0.3pt,line cap=round] (40,84) .. controls (37,64) and (60,58) .. (82,50) .. controls (110,40) and (128,30) .. (122,24);
 \end{scope}
 \end{tikzpicture}
-$\displaystyle X\setminus
-% G08: literal cup and transverse upper stroke; source origin (1118,1976).
-\mathop{\vcenter{\hbox{\begin{tikzpicture}[x=0.009cm,y=-0.009cm]
-\useasboundingbox (0,0) rectangle (69,70);
-\begin{scope}[shift={(-1118,-1976)}]
-\draw[line width=0.45pt] (1130,1980) .. controls (1125,1999) and (1126,2020) .. (1137,2034) .. controls (1152,2045) and (1170,2034) .. (1176,2014) .. controls (1180,2003) and (1177,1986) .. (1172,1980);
-\draw[line width=0.40pt] (1123,1990) .. controls (1141,1990) and (1156,1988) .. (1168,1988);
-\end{scope}
-\end{tikzpicture}}}}\limits_{j\in J}E_j$ intersection des partitions binaires $\Pi_{J,j}^{\circ}$
-% The upper ring's local circle/zero doubt is recorded also at this second occurrence.
-% G09: inserted (j in J), live induites, and one continuous hooked guide.
-% Fixed source origin (1234,2070); the guide supplies no extra prose parenthesis.
-\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=(live.base)]
-\useasboundingbox (0,0) rectangle (320,110);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (45,35) {\inserted{$(j\in J)$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (50,84) {induites};
-\begin{scope}[shift={(-1234,-2070)}]
-\draw[line width=0.40pt] (1244,2162) .. controls (1237,2145) and (1263,2122) .. (1298,2117) .. controls (1350,2130) and (1433,2110) .. (1456,2105) .. controls (1461,2103) and (1456,2100) .. (1452,2098);
+$\displaystyle X\setminus\mathop{\unsure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(unionbase)]
+% G06: source origin (1115,1975); cup and visible transverse stroke; its mathematical role remains unassigned.
+\coordinate (unionbase) at (0,58);
+\path[use as bounding box] (0,0) rectangle (70,62);
+\draw[line width=0.5pt,line cap=round] (14,4) .. controls (8,20) and (10,45) .. (26,54) .. controls (42,65) and (67,48) .. (65,22) .. controls (65,12) and (63,7) .. (61,4);
+\draw[line width=0.5pt,line cap=round] (7,16) -- (56,14);
+\end{tikzpicture}}}\limits_{j\in J}E_j$ intersection des partitions binaires $\Pi_{J,j}^{\circ}$
+% G07: inserted condition and long hooked guide over induites; source origin (1235,2070).
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(condbase)]
+\coordinate (condbase) at (0,100);
+\path[use as bounding box] (0,0) rectangle (320,120);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (55,35) {\inserted{$(j\in J)$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (45,100) {induites};
+\draw[line width=0.3pt,line cap=round] (5,97) .. controls (-4,81) and (17,55) .. (70,53) .. controls (126,59) and (188,58) .. (220,42) .. controls (224,40) and (221,36) .. (217,33);
 \end{scope}
 \end{tikzpicture}
-% G10: U-subscript correction states and its long guide into the sur/X gap.
-% Fixed source origin (311,2140); glyph/state alternatives carry no chronology.
-\begin{tikzpicture}[x=0.010cm,y=-0.010cm,baseline=(live.base)]
-\useasboundingbox (0,0) rectangle (151,165);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (added) at (56,75) {\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (live) at (20,123) {sur};
-\begin{scope}[shift={(-311,-2140)}]
-\draw[line width=0.40pt] (375,2228) .. controls (392,2234) and (422,2234) .. (434,2245) .. controls (447,2259) and (448,2277) .. (451,2294);
+% G08: inserted U subscript correction and guide; source origin (330,2160).
+\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(ubase)]
+\coordinate (ubase) at (0,100);
+\path[use as bounding box] (0,0) rectangle (145,160);
+\begin{scope}[overlay]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,100) {sur};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (35,55) {\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}};
+\draw[line width=0.3pt,line cap=round] (42,63) .. controls (65,70) and (108,64) .. (119,104) .. controls (121,120) and (122,130) .. (123,134);
 \end{scope}
 \end{tikzpicture}
 $\displaystyle X\setminus\bigcup_{j\in J}E_j$ par les $\Pi_j$ $(\unsure{g|j}\in J)$. Pour
