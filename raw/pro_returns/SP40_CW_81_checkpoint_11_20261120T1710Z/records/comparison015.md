## Reader A

\scanpage{15}
\begingroup
\makeatletter
\tagsleft@true
\makeatother
\uline{\deleted{\unsure{I|V}}Version I}

% MARK01: observed full-scan bbox (191,141,195,145); local origin (191,141).
\unsure{\begin{tikzpicture}[baseline=0pt,x=.013cm,y=-.013cm]
\path[use as bounding box] (0,0) rectangle (74,8);
\fill (0,0) .. controls (2,-1) and (4,2) .. (4,4) .. controls (2,5) and (0,3) .. cycle;
\end{tikzpicture}}
Soient $X$ un espace topologique, $(\deleted{\unsure{\Sigma|S}}E_i)_{i\in I}$ un ens. de parties
% GUIDE01: full-scan origin (372,177), approximate curve within (371,214,475,261).
\begin{tikzpicture}[baseline=(opening.base),x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (-48,0) rectangle (170,87);
\node[anchor=base west,inner sep=0] at (-47,29) {\inserted{\unsure{fermés|fermées}}};
\node[anchor=base west,inner sep=0] (opening) at (29,80) {de $X$};
\draw (1,83) .. controls (-8,48) and (21,43) .. (47,46)
 .. controls (72,50) and (91,48) .. (102,39);
\end{tikzpicture}
(noté indiciellement), telles que l'on ait
% slanted
\reversemarginpar
\margin{$\nearrow$ On suppose de plus que pour \unsure{tte|toute|tt} comp. conn. $\unsure{\Sigma_i|\Sigma}$ de $X\setminus E_i$, on ait $\overline{\Sigma}_i\cap E_i\ne\varnothing$ i.e. $\overline{\Sigma}_i\ne\Sigma_i$ i.e. $\Sigma_i$ non fermé dans $X$ (ce qui est le cas si $X$ est connexe)}
\normalmarginpar
\[
 \forall i\in I,\quad \operatorname{Card}\pi_0(X\setminus\deleted{\Sigma}E_i)=2
 \tag*{(a)}
\]
\margin{\uline{NB} les comp. conn. $\Sigma_i^+,\Sigma_i^{\unsure{+|-|\ast}}$ de $X\setminus\Sigma_i$ sont ouvertes dans $X$}
\[
 \begin{aligned}
 &\forall(i,j)\in I\times I,\ i\ne j,\quad \deleted{\Sigma}E_j\ \text{est contenu dans l'une}\\
 &\text{des deux composantes connexes de }X\setminus\deleted{\Sigma}E_i.
 \end{aligned}
 \tag*{(b)}
\]

NB Cette condition (b) est vérifiée automatiquement les $\deleted{\Sigma}E_i$ $(i\in I)$ sont connexes, dès lors que les $E_i$ sont supposés disjoints mutuellement

On se propose d'étudier le ``découpage'' de $X$ par la famille $(E_i)$.

% RULE01: full-scan origin (501,996); long wavy underline and separate short run under 2.
\begin{tikzpicture}[baseline=(case.base),x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (443,117);
\node[anchor=base west,inner sep=0] (case) at (13,70)
 {Cas $\operatorname{Card}\deleted{\unsure{(\mathrm{de})}}(I)\deleted{\unsure{\leq|=}}=2$};
\draw (63,92) .. controls (98,82) and (124,103) .. (166,91)
 .. controls (202,81) and (216,99) .. (262,85)
 .. controls (286,74) and (309,88) .. (342,81)
 .. controls (360,77) and (374,80) .. (378,82);
\draw (393,80) -- (426,80);
\end{tikzpicture}

Soit $\Sigma_i^+$ la comp. conn. de $X\setminus E_i$ qui ne contient pas $E_j$ $(j\ne i)$, alors on a (si $I=\{1,2\}$)
% Drawing coordinates retain C's local map: full-scan approximately (x+24,y+1069).
% The lower-right contour is interrupted at observed bbox (394,1278,413,1308).
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\path[use as bounding box] (-10,-20) rectangle (535,300);
\draw (182,89) .. controls (226,-13) and (337,-39) .. (379,72)
 .. controls (405,143) and (409,181) .. (384,212);
\draw (376,226) .. controls (359,258) and (333,277) .. (303,281)
 .. controls (217,298) and (139,247) .. (161,158)
 .. controls (157,176) and (155,135) .. (182,89);
\draw[line width=.8pt] (181,89) .. controls (256,91) and (313,77) .. (382,86)
 (174,218) .. controls (240,224) and (317,212) .. (380,212);
\draw (44,9) .. controls (46,57) and (63,106) .. (32,108)
 .. controls (52,132) and (38,151) .. (46,195) -- (55,228);
\draw (41,109) .. controls (72,143) and (35,144) .. (48,193)
 .. controls (47,224) and (57,241) .. (39,252) .. controls (55,242) and (43,259) .. (49,282);
\draw (428,86) .. controls (439,93) and (409,141) .. (434,149)
 .. controls (420,158) and (436,251) .. (417,254);
% CANCEL01: glyph retained once; observed oblique crossing strokes replace a generic horizontal strike.
\node at (166,20) {\rlap{$\unsure{\Sigma_1^+|\Sigma_2^+}$}\phantom{$\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}$}};
\draw[line width=.65pt] (135,37) -- (185,-10);
\draw[gray,line width=.45pt] (155,7) -- (177,-12) -- (170,9);
\node at (139,90) {$E_1$}; \node at (149,220) {$E_2$};
\node at (429,32) {$\Sigma_1^+$};
\node at (492,160) {$\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}$};
\node at (14,111) {$\Sigma_2^-$}; \node at (115,278) {$\Sigma_2^+$};
% MARK02: detached spot above the right label; full scan (528,1193,531,1197).
\node[inner sep=0] at (505,126) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
\path[use as bounding box] (0,0) rectangle (4,5);
\fill (0,0) .. controls (3,0) and (4,3) .. (2,4) .. controls (0,4) and (0,1) .. cycle;
\end{tikzpicture}}};
\end{tikzpicture}}
\[
 \Sigma_1^+\cap\Sigma_2^+=\varnothing
 \tag*{(1)}
\]
ce qui \deleted{résulte de}
\[
 \begin{aligned}
 &\begin{tikzpicture}[baseline=(inc.base),x=.013cm,y=-.013cm,line cap=round]
 \path[use as bounding box] (0,0) rectangle (329,79);
 \node[anchor=base west,inner sep=0] (inc) at (2,59)
 {\rlap{$\Sigma_1^-\supset\Sigma_2^+$}\phantom{$\deleted{\Sigma_1^-\supset\Sigma_2^+}$}};
 % CANCEL02: original full-scan origin (704,1388).
 \draw (2,54) .. controls (149,38) and (243,44) .. (325,37);
 % MARK03: two detached points above the relation, observed (859,1404,863,1411).
 \node[inner sep=0] at (157,19) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
 \path[use as bounding box] (0,0) rectangle (5,8);
 \fill (3,0) circle[radius=.8]; \fill (1,6) circle[radius=1];
 \end{tikzpicture}}};
 \end{tikzpicture}
 \qquad\text{équivaut à}\\
 &\deleted{\Sigma_2^-\supset\Sigma_1^+}\qquad \Sigma_1^+\subset\Sigma_2^-\cup E_2,\quad\text{et}
 \end{aligned}
\]
% CANCEL03: two distinct strokes, full-scan origin (202,1435).
\begin{tikzpicture}[baseline=(carsi.base),x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (231,83);
\node[anchor=base west,inner sep=0] (carsi) at (24,47)
 {\rlap{\unsure{car si|Car si}}\phantom{\deleted{\unsure{car si|Car si}}}};
\draw (43,39) .. controls (99,41) and (160,34) .. (204,37) -- (207,40);
\draw (44,45) .. controls (104,48) and (161,43) .. (183,46)
 .. controls (199,51) and (211,49) .. (220,49);
\end{tikzpicture}
\deleted{Si on avait} comme $\Sigma_1^+\cap E_2=\varnothing$, cela équivaut aussi à
\[
 \Sigma_1^+\subset\Sigma_2^-
 \tag*{(2)}
\]
% MARK04: independent right-side pair, full scan (1603,1778,1610,1786).
\margin{\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
\path[use as bounding box] (0,0) rectangle (9,10);
\fill (6,1) .. controls (8,0) and (9,2) .. (6,4) .. controls (4,4) and (4,2) .. cycle;
\fill (1,7) .. controls (3,6) and (5,7) .. (3,9) .. controls (1,9) and (0,8) .. cycle;
\end{tikzpicture}}}
\unsure{et} symétriquement, à
\[
 \Sigma_2^+\subset\Sigma_1^-
 \tag*{$(2')$}
\]

Comme
% MARK05: detached slant between the cancelled words and Sigma; source (510,2061,528,2076).
$\overset{\begin{smallmatrix}\text{\deleted{vois. ouvert}}\\
\text{\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
\path[use as bounding box] (0,0) rectangle (19,17);
\draw[line cap=round,line width=.7pt] (1,15) .. controls (8,6) and (12,3) .. (18,1);
\end{tikzpicture}}}
\end{smallmatrix}}{\Sigma_2^-}\supset E_1$,
\deleted{il contient les} \inserted{i.e. $\Sigma_2^-$ est un \uline{vois}. ouvert de $E_1$,} on \unsure{a}
% slanted; local note coordinates are full-scan coordinates minus (17,1962).
% GUIDE02 and GUIDE03 are separate observed curved strokes, without a supplied mathematical role.
\reversemarginpar
\margin{\figure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (445,383);
\node[rotate=40,inner sep=0] at (114,154) {$\overline{\Sigma_1^+}\cap E_1\ne\varnothing$};
\node[rotate=40,inner sep=0] at (264,56) {i.e.};
\node[rotate=40,inner sep=0] at (95,260) {$\overline{\Sigma_1^+}\ne\Sigma_1^+$};
\node[rotate=40,inner sep=0] at (331,85) {\unsure{à signaler|à sign.ler}};
\node[rotate=40,inner sep=0] at (94,326) {avant};
% Approximate paths: GUIDE02 observed near (233,2071)-(274,2131).
\draw (257,110) .. controls (224,103) and (211,125) .. (217,144)
 .. controls (222,149) and (233,150) .. (237,168);
\draw (237,168) -- (227,162) (237,168) -- (238,156);
% GUIDE03 observed near (187,2149)-(300,2200).
\draw (171,238) .. controls (155,210) and (204,200) .. (245,196)
 .. controls (265,193) and (276,193) .. (282,187);
\end{tikzpicture}}}
\normalmarginpar
\[
 \Sigma_2^-\cap\Sigma_1^+\ne\varnothing
\]
Car
% RULE02: hooked short underline, observed full bbox (896,2226,1038,2245).
\begin{tikzpicture}[baseline=(carformula.base),x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,-54) rectangle (222,30);
\node[anchor=base west,inner sep=0] (carformula) at (0,0) {$\overline{\Sigma_1^+}\cap E_1$};
\draw (44,15) -- (42,22) .. controls (75,23) and (119,14) .. (165,17)
 .. controls (175,18) and (181,17) .. (183,14) -- (179,10);
\end{tikzpicture}
$\ne\varnothing$ (sinon
% GUIDE04: full-scan origin (1455,2104), original guide around (1460,2151)-(1604,2200).
\begin{tikzpicture}[baseline=(sigmaopen.base),x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (170,127);
\node[anchor=base west,inner sep=0] at (-10,40) {\inserted{l'ouvert}};
\node[anchor=base west,inner sep=0] (sigmaopen) at (35,105) {$\Sigma_1^+$};
\draw (6,95) .. controls (15,64) and (35,52) .. (63,52)
 .. controls (91,56) and (117,54) .. (147,47);
\draw (147,47) -- (143,43) (147,47) -- (147,40);
\end{tikzpicture}
serait \inserted{un} fermé dans $X$, \unsure{donc|puis}
% CANCEL04: same recovered group as C, with explicit oblique crossings over the initial symbol.
\begin{tikzpicture}[baseline=(lastcancel.base),x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,-26) rectangle (160,50);
\node[anchor=base west,inner sep=0] (lastcancel) at (8,20)
 {\rlap{$\unsure{\Sigma_1^+\text{ serait}}$}\phantom{$\deleted{\unsure{\Sigma_1^+\text{ serait}}}$}};
\draw (10,12) -- (47,-10); \draw (25,22) -- (66,-5);
\draw (39,21) .. controls (84,20) and (126,14) .. (156,18);
\end{tikzpicture}
$X$ serait disconnexe),
\endgroup
% archive sheet number: 14



{
  "differences": [
    {
      "id": "D01a",
      "location": "heading: overwritten predecessor",
      "C": "deleted unsure I|V",
      "H": "struck V",
      "reading": "\\deleted{\\unsure{I|V}}",
      "evidence": "An internal near-upright survives between two transverse strokes; the adjoining V-shaped return overlaps it. The predecessor remains I primary with V retained. H overlaps the alternative, so this is a qualified primary-reading difference.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "01_heading.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          43,
          19,
          283,
          120
        ]
      },
      "C_source_row": 1,
      "source_part": "predecessor"
    },
    {
      "id": "D01b",
      "location": "heading: word Version",
      "C": "unsure Version",
      "H": "Version",
      "reading": "Version",
      "evidence": "After the crowded initial, the e-r run, raised s turn, i stem, and joined o-n ending are readable.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "01_heading.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          43,
          19,
          283,
          120
        ]
      },
      "C_source_row": 1,
      "source_part": "Version"
    },
    {
      "id": "D02",
      "location": "opening indexed family: overwritten letter",
      "C": "deleted unsure Sigma|S before E_i",
      "H": "E_i",
      "reading": "\\deleted{\\unsure{\\Sigma|S}}E_i",
      "evidence": "The E has a heavy upright and three bars; a thinner returning diagonal/curved middle remains inside it. Its curvature leaves Sigma/S open. H omits that predecessor.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "02_family.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1110,
          119,
          1675,
          225
        ]
      },
      "C_source_row": 2
    },
    {
      "id": "D03",
      "location": "upper-left note: between pour and comp.",
      "C": "tte|toute|tt",
      "H": "uncertain toute",
      "reading": "\\unsure{tte|toute|tt}",
      "evidence": "The small group has two tall, close strokes and a compressed termination. The joined strokes leave the full and contracted readings open. H toute remains an alternative.",
      "confidence": "low",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          57,
          526,
          132,
          618
        ]
      },
      "C_source_row": 3
    },
    {
      "id": "D04",
      "location": "upper-left note: before fermé",
      "C": "unsure non",
      "H": "uncertain n'est pas",
      "reading": "non",
      "evidence": "A short two-humped run is visible directly after Sigma_i and beside the intruding main NB; there are no separated apostrophe/tall-t/second-word strokes in this short run.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          270,
          583,
          324,
          636
        ]
      },
      "C_source_row": 4
    },
    {
      "id": "D05",
      "location": "upper-right NB: second Sigma exponent",
      "C": "+|-|*",
      "H": "-",
      "reading": "\\Sigma_i^{\\unsure{+|-|\\ast}}",
      "evidence": "The dark patch has a horizontal body and a downward protrusion; the covered centre leaves plus/minus/star candidates. Minus, H’s reading, remains explicitly retained.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "05_right_nb.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1408,
          377,
          1445,
          409
        ]
      },
      "C_source_row": 5
    },
    {
      "id": "D06",
      "location": "upper-right NB: complement after X",
      "C": "Sigma_i|E_i",
      "H": "E_i",
      "reading": "X\\setminus\\Sigma_i",
      "evidence": "The glyph has a top horizontal, a diagonal returning through the middle, and a lower horizontal; its left edge stays open. No upright E stem is visible at this locus.",
      "confidence": "high",
      "kind": "misread symbol or index",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "05_right_nb.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1519,
          379,
          1641,
          430
        ]
      },
      "C_source_row": 6
    },
    {
      "id": "D07",
      "location": "condition (b), final E: predecessor",
      "C": "deleted unsure Sigma",
      "H": "E_i",
      "reading": "X\\setminus\\deleted{\\Sigma}E_i.",
      "evidence": "Two thin diagonals meet at the right-middle under the heavy E bars, preserving the angular Sigma. The final full stop is also visible farther right.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "06_b_final_e.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1432,
          512,
          1665,
          607
        ]
      },
      "C_source_row": 7
    },
    {
      "id": "D08",
      "location": "main NB: automatiquement",
      "C": "unsure automatiquement",
      "H": "automatiquement",
      "reading": "automatiquement",
      "evidence": "The pale initial run leads into the crossed t, dotted i, descending q and connected -ment termination. The final t reaches the right scan edge; no extra word is supported after it.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "07_automatiquement.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          976,
          603,
          1683,
          719
        ]
      },
      "C_source_row": 8
    },
    {
      "id": "D09a",
      "location": "case heading: cancelled parenthetical",
      "C": "deleted unsure (de)",
      "H": "omitted",
      "reading": "\\deleted{\\unsure{(\\mathrm{de})}}",
      "evidence": "A small looped upright and low return survive under/at the left of the new (I); crowding prevents a secure complete predecessor.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "08_case.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          752,
          1010,
          817,
          1068
        ]
      },
      "C_source_row": 9,
      "source_part": "parenthetical"
    },
    {
      "id": "D09b",
      "location": "case heading: overwritten relation",
      "C": "deleted unsure <=|=",
      "H": "omitted",
      "reading": "\\deleted{\\unsure{\\leq|=}}=2",
      "evidence": "Two heavy horizontal strokes cover a shorter slanted return between them. The older <= or = cannot be separated securely.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "08_case.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          821,
          1027,
          887,
          1062
        ]
      },
      "C_source_row": 9,
      "source_part": "relation"
    },
    {
      "id": "D10",
      "location": "drawing: crossed upper-left label",
      "C": "deleted unsure Sigma_1^+|Sigma_2^+",
      "H": "omitted",
      "reading": "\\deleted{\\unsure{\\Sigma_1^+|\\Sigma_2^+}}",
      "evidence": "The angular base and raised cross are visible; diagonal cancellations cross the lower numeral and its descending return. Neither 1 nor 2 is secure. The actual crossing geometry is logged at G04.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "09_drawing_cancel.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          132,
          1037,
          247,
          1134
        ]
      },
      "C_source_row": 10
    },
    {
      "id": "D11",
      "location": "drawing: right label exponent",
      "C": "deleted unsure + followed by unsure -",
      "H": "Sigma_1^-",
      "reading": "\\Sigma_1^{\\deleted{\\unsure{+}}\\unsure{-}}",
      "evidence": "A heavy horizontal body overlies vertical and diagonal remnants in a rectangular blot. The live minus and overwritten plus remain qualified; H omits the covered predecessor.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "10_drawing_exponent.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          521,
          1203,
          562,
          1229
        ]
      },
      "C_source_row": 11
    },
    {
      "id": "D12",
      "location": "first equivalence wording after (1)",
      "C": "unsure équivaut",
      "H": "équivaut",
      "reading": "équivaut",
      "evidence": "The initial e, long descending q, dotted i, joined vau and terminal t-like extension are visible before the separate à.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "11_equivaut.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1095,
          1391,
          1328,
          1465
        ]
      },
      "C_source_row": 12
    },
    {
      "id": "D13",
      "location": "beneath drawing: cancelled car si",
      "C": "deleted unsure car si",
      "H": "omitted",
      "reading": "\\deleted{\\unsure{car si|Car si}}",
      "evidence": "The open initial c/C, a-like loop and final s plus dotted i survive two cancellation strokes; the intervening r and capitalization remain uncertain. Geometry is logged at G06.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "12_car_si.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          202,
          1435,
          433,
          1518
        ]
      },
      "C_source_row": 13
    },
    {
      "id": "D14",
      "location": "before symétriquement",
      "C": "unsure et",
      "H": "omitted",
      "reading": "\\unsure{et}",
      "evidence": "Only a small left mark and a low pale curved run remain in the word position. They support the tentative et without settling it.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "13_symetrique.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          230,
          1897,
          290,
          1923
        ]
      },
      "C_source_row": 14
    },
    {
      "id": "D15",
      "location": "above bottom inclusion: cancelled wording",
      "C": "deleted unsure vois. ouvert",
      "H": "struck vois. ouvert",
      "reading": "\\deleted{vois. ouvert}",
      "evidence": "The v/o loop, i dot, short s, abbreviation point, and ouvert ending with a tall crossed t remain visible through the single crossing line. Placement is logged at P07.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "14_vois_deleted.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          408,
          1993,
          643,
          2078
        ]
      },
      "C_source_row": 15
    },
    {
      "id": "D16",
      "location": "lower slanted note: à signaler / à sign.ler",
      "C": "à signaler|à sign.ler",
      "H": "ill{} after first formula",
      "reading": "\\unsure{à signaler|à sign.ler} avant",
      "evidence": "The accented à, initial si run, descending g and later tall l are visible. The crop reaches the rightmost ending; its continuation cannot be fully assessed from this enlargement. Retain both source readings. H’s whole tail placeholder is counted once at H17.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "15_lower_margin.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          258,
          1975,
          460,
          2104
        ]
      },
      "C_source_row": 16,
      "grouped_H_difference": "H17",
      "boundary_limit": "Crop ends at x=432; the rightmost continuation of the slanted ending extends toward x=460 in the half."
    },
    {
      "id": "D17",
      "location": "last line: insertion above fermé",
      "C": "inserted unsure un|une",
      "H": "omitted",
      "reading": "\\inserted{un}",
      "evidence": "The raised short u and following low n run end before the tall f; no additional terminal e loop is visible.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "16_bottom_words.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          384,
          2250,
          447,
          2281
        ]
      },
      "C_source_row": 17
    },
    {
      "id": "D18",
      "location": "last line: connector before crossed group",
      "C": "donc|puis",
      "H": "donc",
      "reading": "\\unsure{donc|puis}",
      "evidence": "The first loop has a long fine descender, followed by compressed low humps; the internal strokes do not settle donc/puis. H agrees with the primary candidate.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "16_bottom_words.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          833,
          2272,
          946,
          2341
        ]
      },
      "C_source_row": 18
    },
    {
      "id": "D19",
      "location": "last line: cancelled mathematical/verbal group",
      "C": "deleted unsure Sigma_1^+ serait",
      "H": "struck Sigma_1^+ != emptyset",
      "reading": "\\deleted{\\unsure{\\Sigma_1^+\\text{ serait}}}",
      "evidence": "A Sigma with lower 1 and raised cross precedes a low connected run ending in a tall crossed/hooked stroke. The run supports serait tentatively; the dense cancellations prevent a secure full recovery. The primary differs from H; this is not asserted as a conclusive H error.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "16_bottom_words.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          927,
          2238,
          1095,
          2295
        ]
      },
      "C_source_row": 19
    },
    {
      "id": "D20",
      "location": "opening insertion above de X",
      "C": "fermés|fermées",
      "H": "fermées",
      "reading": "\\inserted{\\unsure{fermés|fermées}}",
      "evidence": "The raised accent and terminal s are clear. The small vowel run before s is compressed and does not securely distinguish one e from two. H’s fermées remains the alternate.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "03_fermes.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          190,
          177,
          555,
          296
        ]
      },
      "C_source_row": 20
    },
    {
      "id": "D21a",
      "location": "upper-left note: component abbreviation",
      "C": "conn.|connex.",
      "H": "conn.",
      "reading": "conn.",
      "evidence": "The rotated line shows c-o followed by two low n runs and a separate terminal point; no distinct x stroke extends beyond them.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          27,
          599,
          127,
          692
        ]
      },
      "C_source_row": 21,
      "source_part": "component abbreviation"
    },
    {
      "id": "D21b",
      "location": "upper-left note: first Sigma index",
      "C": "unsure i; source alternative no index",
      "H": "Sigma_i",
      "reading": "\\unsure{\\Sigma_i|\\Sigma}",
      "evidence": "A dot lies at the right of the first Sigma, but a separate lowered stem cannot be recovered confidently. Later indexed occurrences have fuller dot-and-stem forms. Both local states remain supported.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          128,
          531,
          185,
          594
        ]
      },
      "C_source_row": 21,
      "source_part": "first Sigma index"
    },
    {
      "id": "H01",
      "location": "upper-left note: opening words",
      "C": "On suppose",
      "H": "Supposons",
      "reading": "On suppose",
      "evidence": "A separate open initial O/n group precedes a space and the descending double-p run of suppose.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          26,
          401,
          206,
          570
        ]
      }
    },
    {
      "id": "H02",
      "location": "condition (a): Card capitalization",
      "C": "Card",
      "H": "card",
      "reading": "Card",
      "evidence": "The first character has a tall open capital-sized loop before ard.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          621,
          373,
          732,
          423
        ]
      }
    },
    {
      "id": "H03",
      "location": "condition (a): covered Sigma",
      "C": "deleted Sigma before E_i",
      "H": "E_i",
      "reading": "\\deleted{\\Sigma}E_i",
      "evidence": "The half shows the angular return within the heavy E stem and bars.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          900,
          373,
          947,
          425
        ]
      }
    },
    {
      "id": "H04",
      "location": "upper-right note: NB underline",
      "C": "uline NB",
      "H": "NB",
      "reading": "\\uline{NB}",
      "evidence": "A separate straight horizontal rule lies directly below the two letters.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "05_right_nb.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1244,
          331,
          1315,
          385
        ]
      }
    },
    {
      "id": "H05",
      "location": "condition (b): first corrected E_j",
      "C": "deleted Sigma before E_j",
      "H": "E_j",
      "reading": "\\deleted{\\Sigma}E_j",
      "evidence": "The half shows two angular returns under the E bars, with the j descending independently to the right.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          816,
          455,
          895,
          531
        ]
      }
    },
    {
      "id": "H06",
      "location": "main NB: Cette capitalization",
      "C": "Cette",
      "H": "cette",
      "reading": "Cette",
      "evidence": "The initial C is tall and open, rising above the following low e/t run.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          332,
          632,
          443,
          695
        ]
      }
    },
    {
      "id": "H07",
      "location": "main NB: immediately after automatiquement",
      "C": "automatiquement les",
      "H": "automatiquement ill{} si les",
      "reading": "automatiquement les",
      "evidence": "The final t reaches the right edge; the next physical line begins les. The half and crop support no intervening si or separate unreadable word.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "07_automatiquement.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1190,
          619,
          1683,
          799
        ]
      }
    },
    {
      "id": "H08",
      "location": "main NB: corrected first E_i",
      "C": "deleted Sigma E_i",
      "H": "E_i",
      "reading": "\\deleted{\\Sigma}E_i",
      "evidence": "The large E has an internal angular predecessor crossing its central bar.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          441,
          745,
          515,
          805
        ]
      }
    },
    {
      "id": "H09",
      "location": "main NB: after mutuellement",
      "C": "mutuellement",
      "H": "mutuellement.",
      "reading": "mutuellement",
      "evidence": "The final tall t and its return end the line; no separate full stop follows in the open space.",
      "confidence": "medium",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1124,
          763,
          1469,
          824
        ]
      }
    },
    {
      "id": "H10",
      "location": "case heading: Card capitalization",
      "C": "Card",
      "H": "card",
      "reading": "Card",
      "evidence": "The large looped first letter rises above the a/r run and aligns with the tall final d.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "08_case.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          640,
          1022,
          734,
          1070
        ]
      }
    },
    {
      "id": "P01",
      "location": "below (1): first crossed inclusion and équivaut à",
      "C": "équivaut à before both crossed inclusions",
      "H": "first crossed inclusion before équivaut à",
      "reading": "First crossed inclusion on the left of équivaut à, then second crossed inclusion on the following line.",
      "evidence": "The crop shows the first crossed inclusion and équivaut à sharing one physical line, with the crossed inclusion left of the wording.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "11_equivaut.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          685,
          1371,
          1414,
          1466
        ]
      }
    },
    {
      "id": "H11",
      "location": "after first équivaut à",
      "C": "à",
      "H": "à :",
      "reading": "à",
      "evidence": "The last low a-like mark has a separate raised accent; no colon pair follows it.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "11_equivaut.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1345,
          1400,
          1414,
          1457
        ]
      }
    },
    {
      "id": "P02",
      "location": "Si on avait cancellation",
      "C": "before comme",
      "H": "after cela équivaut",
      "reading": "Deleted Si on avait at the left of the same line as comme.",
      "evidence": "The half shows a long crossed phrase at x236–642, with comme beginning farther right around x733.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          228,
          1578,
          960,
          1666
        ]
      }
    },
    {
      "id": "H12",
      "location": "continuation aussi à",
      "C": "aussi à",
      "H": "aussi à :",
      "reading": "aussi à",
      "evidence": "The crop shows the dotted i, then a separate low à with its accent; the right-hand space contains no colon.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "22_aussi.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          224,
          1673,
          497,
          1752
        ]
      }
    },
    {
      "id": "H13",
      "location": "after symétriquement, à",
      "C": "à",
      "H": "à :",
      "reading": "à",
      "evidence": "A comma precedes the separate à; the raised accent and low body account for the two marks at the end, without a following colon.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "13_symetrique.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          858,
          1866,
          977,
          1932
        ]
      }
    },
    {
      "id": "P07",
      "location": "cancelled vois. ouvert placement",
      "C": "above/before Sigma_2^-",
      "H": "after the inclusion",
      "reading": "Cancelled vois. ouvert above the first Sigma_2^- of the bottom paragraph.",
      "evidence": "The phrase lies over the first Sigma around x425–625; the inclusion continues below toward E_1 at x645.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "14_vois_deleted.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          408,
          1993,
          643,
          2078
        ]
      }
    },
    {
      "id": "P08",
      "location": "bottom replacement clause and cancelled il contient les",
      "C": "deleted il contient les followed by inserted i.e. clause",
      "H": "i.e. clause followed by struck il contient les",
      "reading": "Cancelled il contient les below the inserted i.e. clause, before the continuing on a.",
      "evidence": "The i.e. clause occupies the raised line; the crossed il contient les remains directly beneath it. H also leaves the raised clause without an insertion state.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "21_bottom_insertion.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          734,
          1984,
          1668,
          2138
        ]
      }
    },
    {
      "id": "H14",
      "location": "underline span under vois. in inserted clause",
      "C": "uline vois.",
      "H": "emph vois.",
      "reading": "\\uline{vois}.",
      "evidence": "The separate underline ends before the isolated abbreviation point; the point is outside the ruled span.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "21_bottom_insertion.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1192,
          2013,
          1287,
          2071
        ]
      }
    },
    {
      "id": "H15",
      "location": "bottom paragraph: on a ending",
      "C": "on a",
      "H": "on a :",
      "reading": "on \\unsure{a}",
      "evidence": "The separate final small mark supports a tentatively but has no recoverable full loop. No two-point colon follows it. The new qualification changes certainty, not the primary letter.",
      "confidence": "low",
      "kind": "other",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "21_bottom_insertion.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1264,
          2067,
          1403,
          2101
        ]
      },
      "qualification_change": "New local doubt on a; primary unchanged."
    },
    {
      "id": "H17",
      "location": "lower slanted note: tail after first formula",
      "C": "i.e. barred Sigma_1^+ != Sigma_1^+ à signaler|à sign.ler avant",
      "H": "ill{}",
      "reading": "i.e. $\\overline{\\Sigma_1^+}\\ne\\Sigma_1^+$ \\unsure{à signaler|à sign.ler} avant",
      "evidence": "The i.e., the second barred/unbarred pair and inequality, and avant are readable. The intermediate slanted word remains doubtful as recorded at D16. One placeholder is counted for this whole passage.",
      "confidence": "medium",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "15_lower_margin.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          25,
          1975,
          460,
          2316
        ]
      }
    },
    {
      "id": "H18",
      "location": "last argument: Car capitalization",
      "C": "Car",
      "H": "car",
      "reading": "Car",
      "evidence": "The large open C rises well above the joined a/r run.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "18_car_formula.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          699,
          2174,
          794,
          2225
        ]
      }
    },
    {
      "id": "P09",
      "location": "insertion before last Sigma_1^+ and guide",
      "C": "inserted l’ouvert before Sigma; no explicit guide",
      "H": "Sigma_1^+, inserted ouvert,",
      "reading": "inserted l'ouvert before Sigma_1^+, with the curved guide GUIDE04",
      "evidence": "A tall looped l and the following word sit above the symbol. A curve starts in the gap before Sigma, rises above it and ends in a hooked tip to the right. H changes the wording, moves the insertion and adds commas absent here.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "17_louvert.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1436,
          2102,
          1610,
          2229
        ]
      }
    },
    {
      "id": "G01",
      "location": "left of opening Soient",
      "C": "omitted",
      "H": "omitted",
      "reading": "MARK01: small detached tilted filled oval",
      "evidence": "A discrete dark tilted spot is visible around (191,141)-(195,145), separate from the opening S. Its role, character, hand and surface origin remain unsettled.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "19_detached_top.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          191,
          141,
          195,
          145
        ]
      },
      "interpretation_confidence": "low"
    },
    {
      "id": "G02",
      "location": "guide beneath opening insertion",
      "C": "insertion text only",
      "H": "insertion text only",
      "reading": "GUIDE01: rising curved guide with upturned right end",
      "evidence": "The line begins in the gap after parties, bends upward over de, then travels right below the added word and turns up at its endpoint.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "03_fermes.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          369,
          213,
          478,
          263
        ]
      }
    },
    {
      "id": "G03",
      "location": "case-heading underline",
      "C": "single continuous uline",
      "H": "single emph span",
      "reading": "RULE01: wavy long run, gap, short separate rule under 2",
      "evidence": "The underline runs beneath Cas through the crowded relation, stops before 2, and resumes as a short distinct segment under the numeral.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "08_case.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          558,
          1064,
          932,
          1095
        ]
      }
    },
    {
      "id": "G04",
      "location": "crossing geometry over upper-left drawing label",
      "C": "generic deleted strike",
      "H": "label omitted",
      "reading": "CANCEL01: oblique dark and pale crossing runs over retained label",
      "evidence": "Two diagonal runs extend across and beyond the labelled angular glyph; the upper pale return forms a pointed excursion. These are reproduced as explicit paths, without adding a generic horizontal strike. H’s omitted label/cluster is counted at D10.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "09_drawing_cancel.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          155,
          1055,
          220,
          1119
        ]
      },
      "grouped_H_difference": "D10"
    },
    {
      "id": "G05",
      "location": "right drawing label: detached dot",
      "C": "omitted",
      "H": "omitted",
      "reading": "MARK02: detached small filled spot above the exponent",
      "evidence": "The enlarged label shows a separate dark spot at (528,1193)-(531,1197), above and clear of the overwritten exponent. Its role and hand remain unresolved.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "10_drawing_exponent.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          528,
          1193,
          531,
          1197
        ]
      },
      "interpretation_confidence": "low"
    },
    {
      "id": "G06",
      "location": "car si cancellation geometry",
      "C": "single generic deleted strike",
      "H": "passage omitted",
      "reading": "CANCEL03: two distinct cancellation lines",
      "evidence": "The upper stroke runs nearly level through the letters; a second lower run remains visibly separate along the middle and turns out to the right. H’s whole omission is counted at D13.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "12_car_si.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          241,
          1468,
          425,
          1488
        ]
      },
      "grouped_H_difference": "D13"
    },
    {
      "id": "G07",
      "location": "above first crossed inclusion relation",
      "C": "omitted",
      "H": "omitted",
      "reading": "MARK03: two small detached points",
      "evidence": "Two separate dark points lie above the curved inclusion sign, at full-scan bbox (859,1404)-(863,1411). No punctuation or mathematical role is supplied.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "11_equivaut.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          859,
          1404,
          863,
          1411
        ]
      },
      "interpretation_confidence": "low"
    },
    {
      "id": "G08",
      "location": "far right of display (2)",
      "C": "omitted",
      "H": "omitted",
      "reading": "MARK04: detached rising pair of spots",
      "evidence": "The isolated two dark spots are diagonal relative to one another, at full bbox (1603,1778)-(1610,1786). Their character, role, hand and origin remain open.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "20_detached_lower.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          1603,
          1778,
          1610,
          1786
        ]
      },
      "interpretation_confidence": "low"
    },
    {
      "id": "G09",
      "location": "between crossed vois. ouvert and bottom Sigma",
      "C": "omitted",
      "H": "omitted",
      "reading": "MARK05: short detached rising slant",
      "evidence": "A discrete slant is visible below the cancellation and above the base symbol; it is retained graphically without naming a bar, accent or operation.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "14_vois_deleted.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          509,
          2059,
          529,
          2076
        ]
      },
      "interpretation_confidence": "low"
    },
    {
      "id": "G10",
      "location": "lower slanted note: two guide paths",
      "C": "text only",
      "H": "tail placeholder",
      "reading": "GUIDE02: short curved arrow; GUIDE03: separate longer bent curve",
      "evidence": "The rotated crop exposes a short curved arrow beside the slanted wording and a separate longer curved run above the left display. Their shapes are drawn with the note. H’s tail placeholder is counted once at H17.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "15_lower_margin.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          183,
          2067,
          305,
          2202
        ]
      },
      "grouped_H_difference": "H17"
    },
    {
      "id": "G11",
      "location": "underline in last Car formula",
      "C": "underline of full barred Sigma intersect E_1",
      "H": "no underline",
      "reading": "RULE02: short curved underline with both ends hooked upward",
      "evidence": "The rule begins beneath the right part of Sigma, spans the intersection and part of E, and ends before the lowered index. Both ends turn upward. It is shorter than C’s full-expression underline.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "18_car_formula.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          896,
          2226,
          1038,
          2245
        ]
      }
    },
    {
      "id": "G12",
      "location": "last cancelled group: crossing paths",
      "C": "generic deleted strike",
      "H": "different struck group",
      "reading": "CANCEL04: explicit oblique runs over initial Sigma and low cross-run",
      "evidence": "Oblique strokes cross the initial symbol and an additional low line crosses the following run. The selected qualified glyph/text is drawn once. H’s reading difference is counted at D19.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "16_bottom_words.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          927,
          2238,
          1095,
          2295
        ]
      },
      "grouped_H_difference": "D19"
    },
    {
      "id": "G13",
      "location": "drawing: lower-right contour",
      "C": "continuous oval contour",
      "H": "disk with no contour interruption described",
      "reading": "Visible short interruption in the lower-right outline",
      "evidence": "Half b shows a short pale/open interval in the oval below the lower chord, followed by the lower curved run. The proposed contour uses two paths at this locus.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          394,
          1278,
          413,
          1308
        ]
      }
    },
    {
      "id": "G14",
      "location": "first crossed inclusion: cancellation-line geometry",
      "C": "generic horizontal deleted strike",
      "H": "struck inclusion",
      "reading": "CANCEL02: slightly rising cancellation run",
      "evidence": "The crossing line begins near the lower left of Sigma and ends higher at the right of the second Sigma; explicit coordinates retain its slant.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "11_equivaut.png",
      "bbox": {
        "coordinate_system": "full scan; origin upper left",
        "xyxy": [
          704,
          1424,
          1033,
          1445
        ]
      }
    }
  ],
  "doubts": [
    {
      "location": "heading: overwritten predecessor",
      "reading": "\\deleted{\\unsure{I|V}}",
      "alternatives": [
        "V"
      ],
      "confidence": "low",
      "reason": "An internal near-upright survives between two transverse strokes; the adjoining V-shaped return overlaps it. The predecessor remains I primary with V retained. H overlaps the alternative, so this is a qualified primary-reading difference.",
      "crop": "01_heading.png",
      "C_source_row": 1,
      "difference_id": "D01a"
    },
    {
      "location": "opening indexed family: overwritten letter",
      "reading": "\\deleted{\\unsure{\\Sigma|S}}E_i",
      "alternatives": [
        "S"
      ],
      "confidence": "medium",
      "reason": "The E has a heavy upright and three bars; a thinner returning diagonal/curved middle remains inside it. Its curvature leaves Sigma/S open. H omits that predecessor.",
      "crop": "02_family.png",
      "C_source_row": 2,
      "difference_id": "D02"
    },
    {
      "location": "upper-left note: between pour and comp.",
      "reading": "\\unsure{tte|toute|tt}",
      "alternatives": [
        "toute",
        "tt"
      ],
      "confidence": "low",
      "reason": "The small group has two tall, close strokes and a compressed termination. The joined strokes leave the full and contracted readings open. H toute remains an alternative.",
      "crop": "04_upper_margin.png",
      "C_source_row": 3,
      "difference_id": "D03"
    },
    {
      "location": "upper-right NB: second Sigma exponent",
      "reading": "\\Sigma_i^{\\unsure{+|-|\\ast}}",
      "alternatives": [
        "-",
        "*"
      ],
      "confidence": "low",
      "reason": "The dark patch has a horizontal body and a downward protrusion; the covered centre leaves plus/minus/star candidates. Minus, H’s reading, remains explicitly retained.",
      "crop": "05_right_nb.png",
      "C_source_row": 5,
      "difference_id": "D05"
    },
    {
      "location": "case heading: cancelled parenthetical",
      "reading": "\\deleted{\\unsure{(\\mathrm{de})}}",
      "alternatives": [],
      "confidence": "low",
      "reason": "A small looped upright and low return survive under/at the left of the new (I); crowding prevents a secure complete predecessor.",
      "crop": "08_case.png",
      "C_source_row": 9,
      "difference_id": "D09a"
    },
    {
      "location": "case heading: overwritten relation",
      "reading": "\\deleted{\\unsure{\\leq|=}}=2",
      "alternatives": [
        "="
      ],
      "confidence": "low",
      "reason": "Two heavy horizontal strokes cover a shorter slanted return between them. The older <= or = cannot be separated securely.",
      "crop": "08_case.png",
      "C_source_row": 9,
      "difference_id": "D09b"
    },
    {
      "location": "drawing: crossed upper-left label",
      "reading": "\\deleted{\\unsure{\\Sigma_1^+|\\Sigma_2^+}}",
      "alternatives": [
        "Sigma_2^+"
      ],
      "confidence": "low",
      "reason": "The angular base and raised cross are visible; diagonal cancellations cross the lower numeral and its descending return. Neither 1 nor 2 is secure. The actual crossing geometry is logged at G04.",
      "crop": "09_drawing_cancel.png",
      "C_source_row": 10,
      "difference_id": "D10"
    },
    {
      "location": "drawing: right label exponent",
      "reading": "\\Sigma_1^{\\deleted{\\unsure{+}}\\unsure{-}}",
      "alternatives": [
        "covered + and live - both tentative"
      ],
      "confidence": "low",
      "reason": "A heavy horizontal body overlies vertical and diagonal remnants in a rectangular blot. The live minus and overwritten plus remain qualified; H omits the covered predecessor.",
      "crop": "10_drawing_exponent.png",
      "C_source_row": 11,
      "difference_id": "D11"
    },
    {
      "location": "beneath drawing: cancelled car si",
      "reading": "\\deleted{\\unsure{car si|Car si}}",
      "alternatives": [
        "Car si"
      ],
      "confidence": "low",
      "reason": "The open initial c/C, a-like loop and final s plus dotted i survive two cancellation strokes; the intervening r and capitalization remain uncertain. Geometry is logged at G06.",
      "crop": "12_car_si.png",
      "C_source_row": 13,
      "difference_id": "D13"
    },
    {
      "location": "before symétriquement",
      "reading": "\\unsure{et}",
      "alternatives": [],
      "confidence": "low",
      "reason": "Only a small left mark and a low pale curved run remain in the word position. They support the tentative et without settling it.",
      "crop": "13_symetrique.png",
      "C_source_row": 14,
      "difference_id": "D14"
    },
    {
      "location": "lower slanted note: à signaler / à sign.ler",
      "reading": "\\unsure{à signaler|à sign.ler} avant",
      "alternatives": [
        "à sign.ler"
      ],
      "confidence": "low",
      "reason": "The accented à, initial si run, descending g and later tall l are visible. The crop reaches the rightmost ending; its continuation cannot be fully assessed from this enlargement. Retain both source readings. H’s whole tail placeholder is counted once at H17.",
      "crop": "15_lower_margin.png",
      "C_source_row": 16,
      "difference_id": "D16"
    },
    {
      "location": "last line: connector before crossed group",
      "reading": "\\unsure{donc|puis}",
      "alternatives": [
        "puis"
      ],
      "confidence": "low",
      "reason": "The first loop has a long fine descender, followed by compressed low humps; the internal strokes do not settle donc/puis. H agrees with the primary candidate.",
      "crop": "16_bottom_words.png",
      "C_source_row": 18,
      "difference_id": "D18"
    },
    {
      "location": "last line: cancelled mathematical/verbal group",
      "reading": "\\deleted{\\unsure{\\Sigma_1^+\\text{ serait}}}",
      "alternatives": [],
      "confidence": "low",
      "reason": "A Sigma with lower 1 and raised cross precedes a low connected run ending in a tall crossed/hooked stroke. The run supports serait tentatively; the dense cancellations prevent a secure full recovery. The primary differs from H; this is not asserted as a conclusive H error.",
      "crop": "16_bottom_words.png",
      "C_source_row": 19,
      "difference_id": "D19"
    },
    {
      "location": "opening insertion above de X",
      "reading": "\\inserted{\\unsure{fermés|fermées}}",
      "alternatives": [
        "fermées"
      ],
      "confidence": "medium",
      "reason": "The raised accent and terminal s are clear. The small vowel run before s is compressed and does not securely distinguish one e from two. H’s fermées remains the alternate.",
      "crop": "03_fermes.png",
      "C_source_row": 20,
      "difference_id": "D20"
    },
    {
      "location": "upper-left note: first Sigma index",
      "reading": "\\unsure{\\Sigma_i|\\Sigma}",
      "alternatives": [
        "Sigma without index"
      ],
      "confidence": "low",
      "reason": "A dot lies at the right of the first Sigma, but a separate lowered stem cannot be recovered confidently. Later indexed occurrences have fuller dot-and-stem forms. Both local states remain supported.",
      "crop": "04_upper_margin.png",
      "C_source_row": 21,
      "difference_id": "D21b"
    },
    {
      "location": "bottom paragraph: on a",
      "reading": "a",
      "alternatives": [],
      "confidence": "low",
      "reason": "The final letter position contains a small separate dark mark without a complete recoverable loop.",
      "crop": "21_bottom_insertion.png",
      "difference_id": "H15"
    },
    {
      "location": "left of opening Soient",
      "reading": "MARK01: small detached tilted filled oval",
      "alternatives": [
        "character/role/hand/surface origin unresolved"
      ],
      "confidence": "low",
      "reason": "Shape preserved under a local unsure; the qualification concerns its interpretation.",
      "crop": "19_detached_top.png",
      "difference_id": "G01"
    },
    {
      "location": "right drawing label: detached dot",
      "reading": "MARK02: detached small filled spot above the exponent",
      "alternatives": [
        "character/role/hand/surface origin unresolved"
      ],
      "confidence": "low",
      "reason": "Shape preserved under a local unsure; the qualification concerns its interpretation.",
      "crop": "10_drawing_exponent.png",
      "difference_id": "G05"
    },
    {
      "location": "above first crossed inclusion relation",
      "reading": "MARK03: two small detached points",
      "alternatives": [
        "character/role/hand/surface origin unresolved"
      ],
      "confidence": "low",
      "reason": "Shape preserved under a local unsure; the qualification concerns its interpretation.",
      "crop": "11_equivaut.png",
      "difference_id": "G07"
    },
    {
      "location": "far right of display (2)",
      "reading": "MARK04: detached rising pair of spots",
      "alternatives": [
        "character/role/hand/surface origin unresolved"
      ],
      "confidence": "low",
      "reason": "Shape preserved under a local unsure; the qualification concerns its interpretation.",
      "crop": "20_detached_lower.png",
      "difference_id": "G08"
    },
    {
      "location": "between crossed vois. ouvert and bottom Sigma",
      "reading": "MARK05: short detached rising slant",
      "alternatives": [
        "character/role/hand/surface origin unresolved"
      ],
      "confidence": "low",
      "reason": "Shape preserved under a local unsure; the qualification concerns its interpretation.",
      "crop": "14_vois_deleted.png",
      "difference_id": "G09"
    }
  ],
  "notes": {
    "page_content": "A handwritten Version I page introduces X, the indexed family E_i, conditions (a) and (b), two marginal notes, the case Card(I)=2, a labelled oval drawing, and the written relations (1), (2), (2 prime). The final parenthesis continues to the page end with a comma.",
    "author_uncertainty": "No explicit verbal uncertainty phrase or question mark was identified on this sheet. Cancellations, overwritten glyphs and added wording are preserved; editorial unsure markers describe this reader’s unresolved ink.",
    "title_date_counts": "Heading Version I. No date or author page count read. The pencil 14 is recorded only as an archive-sheet comment; writer attribution is unresolved.",
    "mathematics_led_reading_decisions": "No mathematical result or expected formula selected a glyph. The repeated indexed symbols were tracked while reading, and the crossed signs, written complement Sigma_i, unbarred intersections, closure bars, and literal automatically les wording were kept from their local strokes.",
    "workflow": "UTC clock and initial packet-read calls were issued together at 2026-11-20 15:15:26 UTC. The first combined text output was truncated; the brief and every packet file were subsequently read in complete outputs before the image pass. Whole image opened once, a once, b once, then one enlargement per listed unresolved locus. All 22 crop PNGs were displayed successfully; none was reopened or recropped. Root’s shared source-row reminder was read after crop 22.",
    "coordinate_map": "Full scan is 1691x2360; both supplied halves are 1691x1260. Half a starts at full y=0; half b starts at full y=1100 (2360-1260), with 160-pixel overlap. Bboxes in the report use full-scan top-left origin.",
    "boundary_limit": "Crop 15 was planned too narrowly at the right end of the slanted à signaler/à sign.ler phrase (x=432 boundary; half shows continuation toward x=460). It is not recropped. That source doubt remains explicit. The drawn note guide paths are approximations and carry separate observed boxes and path-coordinate envelopes.",
    "witness_classification": "H has full text for its page 14, our scan 15. Its drawing description is apparatus; its emptyset macro and typographic quote/emphasis macro choices have no separate reading differences. Its single lower-note ill placeholder is collated once at H17; local doubts and graphic details there refer back to that row.",
    "verification_scope": "Source-only structural and reading/report checks. No OCR, external sources, compiler, TeX format builder, rendering, installation, or delegation.",
    "source_doubt_accounting": {
      "actual_source_rows": 21,
      "local_decisions": 24,
      "resolved_local_decisions": 9,
      "retained_local_decisions": 15,
      "compound_rows": {
        "1": [
          "D01a",
          "D01b"
        ],
        "9": [
          "D09a",
          "D09b"
        ],
        "21": [
          "D21a",
          "D21b"
        ]
      }
    },
    "drawing_component_map": [
      {
        "component": "GUIDE01",
        "origin_full": [
          372,
          177
        ],
        "units_cm": [
          0.013,
          -0.013
        ],
        "observed_bbox": [
          369,
          213,
          478,
          263
        ],
        "control_point_envelope_local": [
          -8,
          39,
          102,
          83
        ]
      },
      {
        "component": "RULE01",
        "origin_full": [
          501,
          996
        ],
        "units_cm": [
          0.013,
          -0.013
        ],
        "observed_bbox": [
          558,
          1064,
          932,
          1095
        ],
        "control_point_envelope_local": [
          63,
          74,
          426,
          103
        ]
      },
      {
        "component": "main oval",
        "origin_full_approx": [
          24,
          1069
        ],
        "units_cm": [
          0.013,
          -0.013
        ],
        "source_paths": "C upper contour plus revised right/lower split; C two-chord command; C two left-brace commands; C right-brace command. All six live labels and the crossed label individually compared with the halves."
      },
      {
        "component": "CANCEL01",
        "origin_full_approx": [
          24,
          1069
        ],
        "units_cm": [
          0.013,
          -0.013
        ],
        "observed_bbox": [
          155,
          1055,
          220,
          1119
        ],
        "path_envelope_local": [
          135,
          -12,
          185,
          37
        ]
      },
      {
        "component": "CANCEL02",
        "origin_full": [
          704,
          1388
        ],
        "units_cm": [
          0.013,
          -0.013
        ],
        "observed_bbox": [
          704,
          1424,
          1033,
          1445
        ],
        "control_point_envelope_local": [
          2,
          37,
          325,
          54
        ]
      },
      {
        "component": "CANCEL03",
        "origin_full": [
          202,
          1435
        ],
        "units_cm": [
          0.013,
          -0.013
        ],
        "observed_bbox": [
          241,
          1468,
          425,
          1488
        ],
        "control_point_envelope_local": [
          43,
          34,
          220,
          51
        ]
      },
      {
        "component": "GUIDE02",
        "origin_full": [
          17,
          1962
        ],
        "units_cm": [
          0.009,
          -0.009
        ],
        "observed_bbox": [
          233,
          2067,
          277,
          2133
        ],
        "control_point_envelope_local": [
          211,
          103,
          257,
          168
        ]
      },
      {
        "component": "GUIDE03",
        "origin_full": [
          17,
          1962
        ],
        "units_cm": [
          0.009,
          -0.009
        ],
        "observed_bbox": [
          183,
          2149,
          305,
          2202
        ],
        "control_point_envelope_local": [
          155,
          187,
          282,
          238
        ]
      },
      {
        "component": "RULE02",
        "formula_local_origin_full_approx": [
          854,
          2217
        ],
        "units_cm": [
          0.013,
          -0.013
        ],
        "observed_bbox": [
          896,
          2226,
          1038,
          2245
        ],
        "control_point_envelope_local": [
          42,
          10,
          183,
          23
        ]
      },
      {
        "component": "GUIDE04",
        "origin_full": [
          1455,
          2104
        ],
        "units_cm": [
          0.013,
          -0.013
        ],
        "observed_bbox": [
          1460,
          2151,
          1605,
          2200
        ],
        "control_point_envelope_local": [
          6,
          40,
          147,
          95
        ]
      },
      {
        "component": "CANCEL04",
        "origin_full_approx": [
          927,
          2250
        ],
        "units_cm": [
          0.013,
          -0.013
        ],
        "observed_bbox": [
          927,
          2238,
          1095,
          2295
        ],
        "control_point_envelope_local": [
          10,
          -10,
          156,
          22
        ]
      }
    ]
  },
  "notation": [
    {
      "location": "opening family and conditions (a),(b)",
      "sign": "E and covered Sigma",
      "latex": "\\deleted{\\Sigma}E_i, \\deleted{\\Sigma}E_j",
      "evidence": "Heavy upright/three bars over angular internal returns; first predecessor separately qualified Sigma/S."
    },
    {
      "location": "condition (a)",
      "sign": "Card and pi_0",
      "latex": "\\operatorname{Card}\\pi_0",
      "evidence": "Capital-height open C; topped pi and a low small oval index."
    },
    {
      "location": "upper-right NB",
      "sign": "complement glyph",
      "latex": "X\\setminus\\Sigma_i",
      "evidence": "Open left edge and diagonal central return of Sigma."
    },
    {
      "location": "formulas (1),(2),(2 prime)",
      "sign": "plus/minus, inclusion/intersection/union",
      "latex": "\\Sigma_1^+,\\Sigma_2^-,\\subset,\\supset,\\cap,\\cup",
      "evidence": "Each plus shows a cross; each minus a horizontal; inclusion sides are curved without lower bars; intersections open down and union opens up."
    },
    {
      "location": "two slanted notes and final Car formula",
      "sign": "closure bars",
      "latex": "\\overline{\\Sigma}_i; \\overline{\\Sigma_1^+}",
      "evidence": "Separate horizontal strokes above the Sigma groups, distinct from their top arms."
    },
    {
      "location": "purpose paragraph",
      "sign": "double quotation ticks",
      "latex": "``découpage''",
      "evidence": "Paired ticks at each side of the word."
    },
    {
      "location": "opening prose and notes",
      "sign": "abbreviations",
      "latex": "ens.; comp. conn.; NB; i.e.; vois.",
      "evidence": "Punctuation read locally, including the point after ens. and the point outside the vois underline."
    },
    {
      "location": "formula label (2 prime)",
      "sign": "prime",
      "latex": "(2')",
      "evidence": "One short raised stroke after the numeral inside the closing parenthesis."
    },
    {
      "location": "pale continuation before (2)",
      "sign": "aussi à",
      "latex": "aussi à",
      "evidence": "Enlargement shows the final i dot and separate accented à. No remaining reading doubt or C change at this crop target."
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The actual C doubtful-reading row mapping is preserved separately from local decisions and graphic component changes; this avoids conflating the three compound rows.",
    "Graphical shape confidence and unresolved role/hand are reported separately for the five detached-mark clusters.",
    "The too-narrow crop-15 ending is disclosed and stays doubtful; no second crop was made.",
    "Path coordinates are approximate reconstructions; observed locus boxes, local origins, and control-point envelopes are listed separately. No rendered layout verification is claimed."
  ]
}

## Reader B

\scanpage{15}
\begingroup
\makeatletter
\tagsleft@true
\makeatother
\uline{\deleted{\unsure{I|V}}Version I}

% G01: detached short dot at full-scan (190,140)--(196,147); hand, role and surface origin undetermined.
\reversemarginpar
\margin{\unsure{$\cdot$}}
\normalmarginpar
Soient $X$ un espace topologique, $(\deleted{\unsure{\Sigma|S}}E_i)_{i\in I}$ un ens. de
% Opening local group; coordinates are full scan minus (195,169).
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (363,116);
\node[anchor=base west,inner sep=0] at (12,85) {parties};
\node[anchor=base west,inner sep=0] at (134,34) {\inserted{\unsure{fermés|fermées}}};
\node[anchor=base west,inner sep=0] at (202,83) {de $X$};
% GUIDE01: the curved insertion guide, (379,256) to (477,215) on the full scan.
\draw (184,87) .. controls (168,47) and (232,51) .. (249,54)
 .. controls (269,55) and (280,50) .. (282,46);
\end{tikzpicture}}
(noté indiciellement), telles que l'on ait
% slanted
\reversemarginpar
\margin{$\nearrow$ On suppose de plus que pour \unsure{tte|toute|tt} comp. conn. $\Sigma_i$ de $X\setminus E_i$, on ait $\overline{\Sigma}_i\cap E_i\ne\varnothing$ i.e. $\overline{\Sigma}_i\ne\Sigma_i$ i.e. $\Sigma_i$ non fermé dans $X$ (ce qui est le cas si $X$ est connexe)}
\normalmarginpar
\[
 \forall i\in I,\quad \operatorname{Card}\pi_0(X\setminus\deleted{\Sigma}E_i)=2
 \tag*{(a)}
\]
% G02: separate upper horizontal stroke over the first Sigma in this NB.
% The overset rule preserves the stroke; its role remains undetermined.
\margin{\uline{NB} les comp. conn. $\overset{\unsure{\rule{.8em}{.35pt}}}{\Sigma}_i^+,\Sigma_i^{\unsure{+|-|\ast}}$ de $X\setminus\Sigma_i$ sont ouvertes dans $X$}
\[
 \begin{aligned}
 &\forall(i,j)\in I\times I,\ i\ne j,\quad \deleted{\Sigma}E_j\ \text{est contenu dans l'une}\\
 &\text{des deux composantes connexes de }X\setminus\deleted{\Sigma}E_i.
 \end{aligned}
 \tag*{(b)}
\]

NB Cette condition (b) est vérifiée automatiquement les $\deleted{\Sigma}E_i$ $(i\in I)$ sont connexes, dès lors que les $E_i$ sont supposés disjoints mutuellement

On se propose d'étudier le ``découpage'' de $X$ par la famille $(E_i)$.

% The heading underline has a separate short run beneath 2.
\uline{Cas $\operatorname{Card}\deleted{\unsure{(\mathrm{de})}}(I)\deleted{\unsure{\leq|=}}=$}\ \uline{$2$}

Soit $\Sigma_i^+$ la comp. conn. de $X\setminus E_i$ qui ne contient pas $E_j$ $(j\ne i)$, alors on a (si $I=\{1,2\}$)
% Drawing coordinate map: full-scan (x,y) = local (x+22,y+1069).
% The pale lower-right rim is drawn in separate supported runs; its exact continuity remains uncertain.
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\path[use as bounding box] (0,-40) rectangle (535,300);
\draw (182,89) .. controls (226,-13) and (337,-39) .. (379,72)
 .. controls (407,148) and (405,201) .. (388,217);
\node[anchor=north west,inner sep=0] at (354,222) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (34,44);
\draw[gray,line width=.28pt] (29,3) .. controls (24,17) and (15,29) .. (5,39);
\end{tikzpicture}}};
\draw (355,266) .. controls (341,275) and (321,280) .. (303,281)
 .. controls (217,298) and (139,247) .. (161,158)
 .. controls (157,176) and (155,135) .. (182,89);
\draw[line width=.8pt] (181,89) .. controls (256,91) and (313,77) .. (382,86)
 (174,218) .. controls (240,224) and (317,212) .. (380,212);
\draw (44,9) .. controls (46,57) and (63,106) .. (32,108)
 .. controls (52,132) and (38,151) .. (46,195) -- (55,228);
\draw (41,109) .. controls (72,143) and (35,144) .. (48,193)
 .. controls (47,224) and (57,241) .. (39,252) .. controls (55,242) and (43,259) .. (49,282);
\draw (428,86) .. controls (439,93) and (409,141) .. (434,149)
 .. controls (420,158) and (436,251) .. (417,254);
\node[inner sep=0] at (166,20) {\rlap{$\unsure{\Sigma_1^+|\Sigma_2^+}$}\phantom{$\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}$}};
% CANCEL01: the two diagonal crossing runs of the upper-left deleted label.
\draw[line width=.7pt] (135,39) -- (187,-8);
\draw[line width=.45pt] (141,32) .. controls (158,13) and (164,2) .. (177,-13);
\node at (139,90) {$E_1$}; \node at (149,220) {$E_2$};
\node at (429,32) {$\Sigma_1^+$};
\node at (492,160) {$\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}$};
% G03: detached dot above the crowded right-hand exponent; role and hand undetermined.
\node[inner sep=0] at (507,125) {\unsure{$\cdot$}};
\node at (14,111) {$\Sigma_2^-$}; \node at (115,278) {$\Sigma_2^+$};
\end{tikzpicture}}
\[
 \Sigma_1^+\cap\Sigma_2^+=\varnothing
 \tag*{(1)}
\]
ce qui \deleted{résulte de} équivaut à
\[
 \begin{aligned}
 &\deleted{\Sigma_1^-\supset\Sigma_2^+}\\
 &\deleted{\Sigma_2^-\supset\Sigma_1^+}\qquad \Sigma_1^+\subset\Sigma_2^-\cup E_2,\quad\text{et}
 \end{aligned}
\]
% Local cancelled words, origin (211,1427); both horizontal crossing runs retained.
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (220,86);
\node[anchor=base west,inner sep=0] at (15,57) {\rlap{\unsure{Car si|car si}}\phantom{\deleted{\unsure{Car si|car si}}}};
\draw (37,48) .. controls (90,46) and (138,45) .. (182,47);
\draw (45,54) .. controls (108,55) and (156,58) .. (201,58);
\end{tikzpicture}}
\deleted{Si on avait} comme $\Sigma_1^+\cap E_2=\varnothing$, cela équivaut aussi à
\[
 \Sigma_1^+\subset\Sigma_2^-
 \tag*{(2)}
\]
% G04: two detached small marks at full-scan (1602,1779)--(1612,1791); hand and role undetermined.
\margin{\unsure{\begin{tikzpicture}[x=.02cm,y=-.02cm]
\path[use as bounding box] (0,0) rectangle (10,12);
\fill (6,1) ellipse (1 and .7);
\fill (1,8) ellipse (1 and .6);
\end{tikzpicture}}}
\unsure{et} symétriquement, à
\[
 \Sigma_2^+\subset\Sigma_1^-
 \tag*{$(2')$}
\]

% Lower correction group: full-scan (x,y) = local (x+219,y+2009).
\figure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (1448,145);
\node[anchor=base west,inner sep=0] at (19,122) {Comme};
\node[anchor=base west,inner sep=0] at (207,43) {\rlap{\unsure{vois. ouvert}}\phantom{\deleted{\unsure{vois. ouvert}}}};
\draw (209,37) .. controls (270,33) and (334,38) .. (410,36);
\node[anchor=base west,inner sep=0] at (265,122) {$\Sigma_2^-\supset E_1,$};
% G05: detached slant below the struck words, visible (510,2076)--(526,2063).
\node[inner sep=0] at (299,61) {\unsure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (16,13);
\draw (0,13) .. controls (5,6) and (10,1) .. (16,0);
\end{tikzpicture}}};
\node[anchor=base west,inner sep=0] at (556,97) {\rlap{il contient les}\phantom{\deleted{il contient les}}};
\draw (557,91) .. controls (705,95) and (858,86) .. (997,82);
\node[anchor=base west,inner sep=0] at (557,49) {\inserted{i.e. $\Sigma_2^-$ est un \uline{vois.} ouvert de $E_1$,}};
\node[anchor=base west,inner sep=0] at (1048,93) {on a};
\end{tikzpicture}}
% slanted
\reversemarginpar
\margin{$\overline{\Sigma_1^+}\cap E_1\ne\varnothing$ i.e. $\overline{\Sigma_1^+}\ne\Sigma_1^+$ \unsure{à signaler|à sign.ler} avant
% G06: curved detached guide; full-scan origin (180,2145), role of the curve undetermined.
\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (124,78);
\node[inner sep=0] at (62,39) {\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (124,78);
\draw (9,69) .. controls (-1,38) and (49,35) .. (75,23)
 .. controls (102,16) and (119,12) .. (119,6);
\end{tikzpicture}}};
\end{tikzpicture}}}
\normalmarginpar
\[
 \Sigma_2^-\cap\Sigma_1^+\ne\varnothing
\]
Car $\underline{\overline{\Sigma_1^+}\cap E_1}\ne\varnothing$
% Final local insertion: coordinates are full scan minus (1278,2080).
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (362,164);
\node[anchor=base west,inner sep=0] at (19,127) {(sinon};
\node[anchor=base west,inner sep=0] at (170,62) {\inserted{l'ouvert}};
\node[anchor=base west,inner sep=0] at (213,131) {$\Sigma_1^+$};
% GUIDE02: bent attachment guide from before Sigma to the right of the inserted word.
\draw (183,117) .. controls (207,63) and (230,75) .. (262,78)
 .. controls (285,81) and (311,79) .. (326,74) -- (326,70) -- (322,70);
\end{tikzpicture}}
serait \inserted{\unsure{un|une}} fermé dans $X$, donc
% Final deleted group: origin (928,2238). The detached upper remnants have no assigned character.
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (165,67);
\node[anchor=base west,inner sep=0] at (21,49) {\rlap{\unsure{$\Sigma_1^+$ serait}}\phantom{\deleted{\unsure{$\Sigma_1^+$ serait}}}};
\draw (11,28) -- (51,5);
\draw (20,35) -- (70,13);
% G07: upper remnant cluster, shape retained locally under doubt; hand, role and surface origin undetermined.
\node[inner sep=0] at (28,14) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (37,24);
\draw (3,18) .. controls (11,8) and (8,7) .. (10,3) -- (15,18) -- (33,9);
\draw (24,6) -- (26,16);
\end{tikzpicture}}};
\end{tikzpicture}}
$X$ serait disconnexe),
\endgroup
% archive sheet number: 14



{
  "differences": [
    {
      "id": "D01a",
      "location": "underlined title, overwritten initial",
      "C": "deleted unsure I|V",
      "H": "struck V",
      "reading": "\\uline{\\deleted{\\unsure{I|V}}Version I}",
      "evidence": "A central upright survives between transverse top and bottom strokes; the superposed oblique V strokes prevent separating the predecessor completely. I remains primary and V remains supported. The underline runs beneath the whole title, including the initial cluster. H puts its struck V outside the marked title span.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "01_heading.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          50,
          23,
          106,
          84
        ]
      },
      "C_source_doubt_row": 1,
      "qualification": "Qualified H difference: H V remains an alternative."
    },
    {
      "id": "D01b",
      "location": "title word",
      "C": "unsure Version",
      "H": "Version",
      "reading": "Version",
      "evidence": "The large V is followed by a rounded e, r shoulder, s turn, narrow looped i, o bowl and final n. The word can be read through the heavier initial overdraw.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "01_heading.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          51,
          24,
          184,
          82
        ]
      },
      "C_source_doubt_row": 1
    },
    {
      "id": "D02",
      "location": "first indexed family, predecessor under E",
      "C": "deleted unsure Sigma|S",
      "H": "E_i without predecessor",
      "reading": "\\deleted{\\unsure{\\Sigma|S}}E_i",
      "evidence": "Inside the live upright E, a returning diagonal and rounded waist remain. The overlap prevents a secure separation of angular Sigma from S.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "02_first_family.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1162,
          140,
          1222,
          191
        ]
      },
      "C_source_doubt_row": 2
    },
    {
      "id": "D03",
      "location": "upper slanted note, after pour",
      "C": "unsure tte|toute|tt",
      "H": "uncertain toute",
      "reading": "\\unsure{tte|toute|tt}",
      "evidence": "Two tall linked strokes and a short ending favour the abbreviated tte. The compressed intervening trace does not settle the longer spelling or the final e.",
      "confidence": "low",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "04_upper_left_note.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          83,
          467,
          166,
          558
        ]
      },
      "C_source_doubt_row": 3,
      "qualification": "H toute is retained as an alternative; this is not an established exclusion of that reading."
    },
    {
      "id": "D04",
      "location": "upper slanted note, before fermé",
      "C": "unsure non",
      "H": "uncertain n'est pas",
      "reading": "non",
      "evidence": "A short three-part wave above the upright main-text NB has two n shoulders around a small round middle trace. There is no separate apostrophe or the several letter groups required by n'est pas.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "04_upper_left_note.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          267,
          588,
          316,
          632
        ]
      },
      "C_source_doubt_row": 4
    },
    {
      "id": "D05",
      "location": "right NB, second raised sign",
      "C": "unsure +|-|*",
      "H": "- ",
      "reading": "\\Sigma_i^{\\unsure{+|-|\\ast}}",
      "evidence": "The small raised patch has a broad horizontal body with short projections above and below it. Overlap obscures whether those projections belong to a plus, an overwritten minus, or a star-like form.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "05_right_nb.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1410,
          380,
          1445,
          402
        ]
      },
      "C_source_doubt_row": 5,
      "qualification": "H minus remains an alternative."
    },
    {
      "id": "D06",
      "location": "right NB, after X setminus",
      "C": "unsure Sigma|E",
      "H": "E_i",
      "reading": "X\\setminus\\Sigma_i",
      "evidence": "The upper arm returns diagonally to the lower left and then across the foot. The left side remains open; the shape has no independent full-height upright. The following lowered i is visible.",
      "confidence": "high",
      "kind": "misread symbol or index",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "05_right_nb.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1570,
          383,
          1634,
          429
        ]
      },
      "C_source_doubt_row": 6
    },
    {
      "id": "D07",
      "location": "condition (b), final corrected E",
      "C": "deleted unsure Sigma",
      "H": "E_i without predecessor",
      "reading": "\\deleted{\\Sigma}E_i.",
      "evidence": "A slant descends from the top-left to the middle-right, then returns toward the bottom-left inside the live E. Its angular three-part path is visible. The distant dot after the dotted subscript is a full stop.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "06_b_final.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1549,
          541,
          1659,
          590
        ]
      },
      "C_source_doubt_row": 7
    },
    {
      "id": "D08",
      "location": "NB after (b), pale adverb",
      "C": "unsure automatiquement",
      "H": "automatiquement",
      "reading": "automatiquement",
      "evidence": "Despite the pale first joining strokes, the raised t, following compressed m/a/t/i strokes, q descender, and final ment are visible in one word. Its final t crossbar reaches the crop's right boundary; the supplied half shows the page-edge continuation.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "07_automatiquement.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1202,
          620,
          1675,
          715
        ]
      },
      "C_source_doubt_row": 8,
      "boundary_limit": "The final t crossbar reaches x=1670 in this crop; no second crop was made."
    },
    {
      "id": "D09a",
      "location": "case heading, predecessor inside parentheses",
      "C": "deleted unsure (de)",
      "H": "no predecessor",
      "reading": "\\deleted{\\unsure{(\\mathrm{de})}}(I)",
      "evidence": "Below and left of the live I there is a small loop, a tall return and a low joining loop. The overwritten strokes support (de), with the complete earlier lettering still uncertain.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "08_case_heading.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          753,
          1010,
          832,
          1069
        ]
      },
      "C_source_doubt_row": 9
    },
    {
      "id": "D09b",
      "location": "case heading, overwritten relation",
      "C": "deleted unsure <=|= followed by =",
      "H": "=",
      "reading": "\\deleted{\\unsure{\\leq|=}}=",
      "evidence": "Two thick horizontal runs enclose oblique, partly triangular traces. These traces do not isolate the older relation securely. The live two-stroke equality is preserved.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "08_case_heading.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          826,
          1033,
          891,
          1058
        ]
      },
      "C_source_doubt_row": 9
    },
    {
      "id": "D10",
      "location": "drawing, cancelled upper-left label",
      "C": "deleted unsure Sigma_1^+|Sigma_2^+",
      "H": "no cancelled label",
      "reading": "\\deleted{\\unsure{\\Sigma_1^+|\\Sigma_2^+}}",
      "evidence": "An angular Sigma and raised cross remain beneath multiple diagonal crossings. The lowered right-hand form is crowded by a descending cancellation return, leaving 1 and 2 unresolved. CANCEL01 reproduces the two crossing runs visible above the ordinary glyph.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "09_cancelled_drawing_label.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          155,
          1055,
          224,
          1124
        ]
      },
      "C_source_doubt_row": 10,
      "related_graphics": [
        "CANCEL01"
      ]
    },
    {
      "id": "D11",
      "location": "drawing, right-hand raised correction",
      "C": "deleted unsure + and live unsure -",
      "H": "Sigma_1^-",
      "reading": "\\Sigma_1^{\\deleted{\\unsure{+}}\\unsure{-}}",
      "evidence": "The raised area is a dense rectangular patch with several horizontal runs and short vertical connections. A central minus and crossed plus are supported but cannot be cleanly isolated. The independent dot above the patch is recorded separately as G03.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "10_drawing_exponent.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          524,
          1202,
          561,
          1225
        ]
      },
      "C_source_doubt_row": 11
    },
    {
      "id": "D12",
      "location": "after (1), live équivaut",
      "C": "unsure équivaut",
      "H": "équivaut",
      "reading": "équivaut",
      "evidence": "The initial small accented e, a q loop with long descender, the joined middle shoulders, dotted i and extended final t can be followed. The following à is a low a-like turn with a separate accent.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "11_equivaut.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1101,
          1401,
          1321,
          1470
        ]
      },
      "C_source_doubt_row": 12
    },
    {
      "id": "D13",
      "location": "cancelled phrase under the oval",
      "C": "deleted unsure car si",
      "H": "omitted",
      "reading": "\\deleted{\\unsure{Car si|car si}}",
      "evidence": "The initial open curve is substantially taller than the following low letters, favouring capital C. A rounded next loop, compressed joining trace, final curved s and i dot remain between two long horizontal cancellations. Lower-case car si remains an alternative because the cancellation obscures the first group.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "12_car_si.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          223,
          1452,
          415,
          1490
        ]
      },
      "C_source_doubt_row": 13
    },
    {
      "id": "D14",
      "location": "before symétriquement",
      "C": "unsure et",
      "H": "omitted",
      "reading": "\\unsure{et}",
      "evidence": "Only a pale small oblique trace and a separate shallow arch remain at the start of this line. They support the supplied et candidate without revealing a complete t stem.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "14_et_symetrique.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          231,
          1903,
          292,
          1922
        ]
      },
      "C_source_doubt_row": 14
    },
    {
      "id": "D15",
      "location": "crossed wording above lower Sigma_2^-",
      "C": "deleted unsure vois. ouvert",
      "H": "struck vois. ouvert",
      "reading": "\\deleted{\\unsure{vois. ouvert}}",
      "evidence": "The v bowl, o loop, i dot and s curve, followed by the open middle letters and tall terminal t of ouvert, are readable. The crossing line covers the place of the abbreviation point, so the qualified phrase is retained.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "15_vois_ouvert.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          424,
          2022,
          631,
          2058
        ]
      },
      "C_source_doubt_row": 15
    },
    {
      "id": "D16",
      "location": "lower slanted note, phrase before avant",
      "C": "unsure à signaler|à sign.ler",
      "H": "ill placeholder for remainder",
      "reading": "\\unsure{à signaler|à sign.ler} avant",
      "evidence": "The accented à, s/i group and long g descender are visible. The compressed continuation and small point-like interruption do not settle signaler versus sign.ler. The far-right ending approaches the planned crop boundary, and no repeat crop was made. Avant is readable on the next slanted line.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "17_lower_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          273,
          2006,
          433,
          2110
        ]
      },
      "C_source_doubt_row": 16,
      "H_coverage": "H04 below accounts for the entire remainder represented by H ill; no second H count here.",
      "boundary_limit": "Far-right continuation approaches x=427, the crop boundary; complete endpoint lettering is not claimed."
    },
    {
      "id": "D17",
      "location": "final sentence, insertion above fermé",
      "C": "inserted unsure un|une",
      "H": "no article insertion",
      "reading": "\\inserted{\\unsure{un|une}}",
      "evidence": "A short linked wave sits above the gap before fermé. Its terminal hump runs toward the high beginning of f; a separate final e cannot be isolated.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "19_un_ferme.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          386,
          2256,
          441,
          2276
        ]
      },
      "C_source_doubt_row": 17
    },
    {
      "id": "D18",
      "location": "final sentence, before cancelled group",
      "C": "unsure donc|puis",
      "H": "donc",
      "reading": "donc",
      "evidence": "After the first looped stem there is a closed round o, then linked n shoulders and a low terminal c. These local forms support donc. The first stem has a long lower extension, which is retained by the reading rather than used to replace the word.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "20_donc_cancelled.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          838,
          2283,
          941,
          2342
        ]
      },
      "C_source_doubt_row": 18
    },
    {
      "id": "D19",
      "location": "final cancelled phrase",
      "C": "deleted unsure Sigma_1^+ serait",
      "H": "struck Sigma_1^+ neq emptyset",
      "reading": "\\deleted{\\unsure{$\\Sigma_1^+$ serait}}",
      "evidence": "The Sigma, lowered 1 and raised cross remain readable. To their right a compressed connected run ends in a tall looped/crossed t-like form. This favours the supplied serait reading; the intermediate letters remain obscured. The additional upper traces are reproduced separately as G07, without supplying a word for them.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "20_donc_cancelled.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          932,
          2239,
          1086,
          2291
        ]
      },
      "C_source_doubt_row": 19,
      "qualification": "The primary reading differs from H; the crowded ink leaves the phrase qualified.",
      "related_graphics": [
        "G07"
      ]
    },
    {
      "id": "D20",
      "location": "opening insertion above de X",
      "C": "inserted unsure fermés|fermées",
      "H": "added fermées",
      "reading": "\\inserted{\\unsure{fermés|fermées}}",
      "evidence": "The f stem, compressed middle joins, detached acute and terminal s hook are visible. The small vowel immediately before s remains too compressed to settle one versus two e strokes. Fermés remains the primary visual candidate.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "03_fermes.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          328,
          178,
          451,
          229
        ]
      },
      "C_source_doubt_row": 20,
      "qualification": "H fermées remains a supported alternative; no grammatical agreement was used to select the reading."
    },
    {
      "id": "D21a",
      "location": "upper slanted note, component abbreviation",
      "C": "unsure conn.|connex.",
      "H": "conn.",
      "reading": "conn.",
      "evidence": "The rounded c/o beginning is followed by two low n shoulders and a terminal dot. No additional x trace is visible before that dot.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "04_upper_left_note.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          30,
          601,
          114,
          691
        ]
      },
      "C_source_doubt_row": 21
    },
    {
      "id": "D21b",
      "location": "upper slanted note, first Sigma index",
      "C": "Sigma with unsure i",
      "H": "Sigma_i",
      "reading": "\\Sigma_i",
      "evidence": "Beside the first Sigma there is a small separated dot and a short lower stroke. The two parts give the written i index.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "04_upper_left_note.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          124,
          542,
          172,
          596
        ]
      },
      "C_source_doubt_row": 21
    },
    {
      "id": "H01",
      "location": "upper slanted note, opening",
      "C": "On suppose de plus",
      "H": "Supposons de plus",
      "reading": "On suppose de plus",
      "evidence": "The first line has a separate On before suppose. The last letters of suppose end before the next slanted line de plus; the added ns of Supposons has no corresponding group.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "04_upper_left_note.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          26,
          403,
          206,
          574
        ]
      }
    },
    {
      "id": "H02",
      "location": "NB after (b), line break after automatiquement",
      "C": "automatiquement les",
      "H": "automatiquement ill{} si les",
      "reading": "automatiquement les",
      "evidence": "The adverb ends at the right edge of its line; the following line begins with les at x310. The intervening start-of-line space contains no separate si group. H's extra placeholder and si have no additional word to map to.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "07_automatiquement.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          291,
          616,
          1675,
          800
        ]
      }
    },
    {
      "id": "H03",
      "location": "NB after (b), initial word",
      "C": "Cette",
      "H": "cette",
      "reading": "Cette",
      "evidence": "The word begins with a large open C at x343, distinctly above the following low letters.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          337,
          643,
          450,
          699
        ]
      }
    },
    {
      "id": "H04",
      "location": "lower slanted marginal note, after first inequality",
      "C": "i.e. closure inequality; unsure à signaler|à sign.ler avant",
      "H": "ill{} after first inequality",
      "reading": "i.e. $\\overline{\\Sigma_1^+}\\ne\\Sigma_1^+$ \\unsure{à signaler|à sign.ler} avant",
      "evidence": "After the first inequality, dotted i.e. is visible; the next line has a barred Sigma with raised plus and lower 1, a crossed equality, and an unbarred Sigma_1^+. The final two slanted prose groups include the qualified phrase and readable avant.",
      "confidence": "medium",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "17_lower_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          26,
          1996,
          433,
          2328
        ]
      },
      "covered_local_rows": [
        "D16"
      ]
    },
    {
      "id": "H05",
      "location": "condition (a), corrected set symbol",
      "C": "deleted Sigma E_i",
      "H": "E_i",
      "reading": "\\deleted{\\Sigma}E_i",
      "evidence": "The live E has an upright left stem; an older angular down-and-return line survives inside it. The precursor is visibly overdrawn.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          898,
          374,
          947,
          422
        ]
      }
    },
    {
      "id": "H06",
      "location": "condition (b), first corrected set symbol",
      "C": "deleted Sigma E_j",
      "H": "E_j",
      "reading": "\\deleted{\\Sigma}E_j",
      "evidence": "The capital has a surviving inner slant returning toward the lower left beneath the heavier upright and horizontal E strokes.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          811,
          455,
          889,
          531
        ]
      }
    },
    {
      "id": "H07",
      "location": "NB after (b), first set symbol",
      "C": "deleted Sigma E_i",
      "H": "E_i",
      "reading": "\\deleted{\\Sigma}E_i",
      "evidence": "An angular inner diagonal is visible beneath the E at the beginning of the second NB line; the later E_i in the same paragraph is uncorrected.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          440,
          746,
          501,
          798
        ]
      }
    },
    {
      "id": "H08",
      "location": "condition (a), cardinality operator",
      "C": "Card",
      "H": "card",
      "reading": "Card",
      "evidence": "The operator begins with a large open C whose height exceeds that of a/r, followed by the tall d.",
      "confidence": "high",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          619,
          370,
          731,
          420
        ]
      }
    },
    {
      "id": "H09",
      "location": "case heading, cardinality operator",
      "C": "Card",
      "H": "card",
      "reading": "Card",
      "evidence": "The initial C is a large open loop before the short a/r joins and tall d.",
      "confidence": "high",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "08_case_heading.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          643,
          1028,
          732,
          1065
        ]
      }
    },
    {
      "id": "H10",
      "location": "right NB, NB underline",
      "C": "uline NB",
      "H": "NB without emphasis",
      "reading": "\\uline{NB}",
      "evidence": "A separate dark near-horizontal line lies immediately beneath NB and above the Sigma row.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "05_right_nb.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1258,
          370,
          1316,
          380
        ]
      }
    },
    {
      "id": "H11",
      "location": "NB after (b), paragraph endpoint",
      "C": "mutuellement without point",
      "H": "mutuellement.",
      "reading": "mutuellement",
      "evidence": "The final t finishes the low rightward stroke; the following blank area has no distinct full stop.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          992,
          771,
          1442,
          832
        ]
      }
    },
    {
      "id": "H12",
      "location": "upper slanted note, punctuation before second i.e.",
      "C": "Sigma_i i.e.",
      "H": "Sigma_i, i.e.",
      "reading": "Sigma_i i.e.",
      "evidence": "The first i.e. has its own two dots. After the unbarred Sigma_i in the next equality, the next marks belong to i.e.; there is no separate comma at the transition.",
      "confidence": "medium",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "04_upper_left_note.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          24,
          685,
          263,
          954
        ]
      }
    },
    {
      "id": "H13",
      "location": "after (1), placement of crossed first inclusion",
      "C": "two crossed inclusions below (1)",
      "H": "first crossed inclusion between résulte de and équivaut à",
      "reading": "crossed inclusions on their own successive lines",
      "evidence": "The first crossed Sigma_1^- superset Sigma_2^+ lies below the equality and left of live équivaut à; it does not sit in the word sequence ce qui résulte de.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          694,
          1388,
          1398,
          1555
        ]
      }
    },
    {
      "id": "H14",
      "location": "after first équivaut à",
      "C": "à without colon",
      "H": "à :",
      "reading": "à",
      "evidence": "A small a-like lower mark and detached accent form à. The following right-side space is blank.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "11_equivaut.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1355,
          1410,
          1412,
          1450
        ]
      }
    },
    {
      "id": "H15",
      "location": "after aussi à",
      "C": "à without colon",
      "H": "à :",
      "reading": "à",
      "evidence": "The endpoint has one shallow a-like lower curve and an upper accent. No third or fourth punctuation mark follows it.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "13_aussi_a.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          435,
          1690,
          490,
          1738
        ]
      }
    },
    {
      "id": "H16",
      "location": "after symétriquement, à",
      "C": "à without colon",
      "H": "à :",
      "reading": "à",
      "evidence": "The comma after symétriquement is visible. The final low a-like stroke and detached accent give à; nothing follows before the blank right margin.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "14_et_symetrique.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          865,
          1863,
          972,
          1931
        ]
      }
    },
    {
      "id": "H17",
      "location": "crossed Si on avait",
      "C": "deleted Si on avait before comme",
      "H": "struck Si on avait after cela équivaut",
      "reading": "deleted Si on avait before comme",
      "evidence": "The cancelled words occupy the left of the same horizontal line on which comme begins at x734. Aussi à continues on the next line.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          234,
          1581,
          964,
          1657
        ]
      }
    },
    {
      "id": "H18",
      "location": "lower paragraph, placement of crossed vois. ouvert",
      "C": "before/above Sigma_2^- superset E_1",
      "H": "after that inclusion",
      "reading": "above Sigma_2^-",
      "evidence": "The cancelled words sit above the first Sigma of the lower paragraph; the later crossed il contient les is a separate group farther right.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "15_vois_ouvert.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          418,
          2016,
          710,
          2144
        ]
      }
    },
    {
      "id": "H19",
      "location": "lower paragraph, inserted i.e. clause and cancelled il contient les",
      "C": "deleted il contient les with inserted i.e. clause",
      "H": "i.e. clause live, then struck il contient les",
      "reading": "inserted i.e. clause above deleted il contient les",
      "evidence": "The i.e. clause lies on the raised line directly above the struck baseline wording. The word vois. has its own underline. The raised clause ends with the comma near E_1.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "16_lower_insertion.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          767,
          2019,
          1666,
          2126
        ]
      }
    },
    {
      "id": "H20",
      "location": "lower paragraph, on a endpoint",
      "C": "on a",
      "H": "on a :",
      "reading": "on a",
      "evidence": "The low on group is followed by a very small a; the blank space to its right contains no paired colon points.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "16_lower_insertion.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1261,
          2066,
          1439,
          2116
        ]
      }
    },
    {
      "id": "H21",
      "location": "last argument, initial Car",
      "C": "Car",
      "H": "car",
      "reading": "Car",
      "evidence": "The initial C is tall and open, extending above the following a/r join.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          696,
          2157,
          798,
          2207
        ]
      }
    },
    {
      "id": "H22",
      "location": "last argument, underlined expression",
      "C": "underline closure Sigma_1^+ cap E_1",
      "H": "no emphasis",
      "reading": "\\underline{\\overline{\\Sigma_1^+}\\cap E_1}",
      "evidence": "A low horizontal bracket-like stroke runs beneath the Sigma/intersection/E expression; the unequal sign and empty set lie outside this underline.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          889,
          2223,
          1053,
          2250
        ]
      }
    },
    {
      "id": "H23",
      "location": "last parenthesis, l'ouvert insertion",
      "C": "inserted l'ouvert before Sigma_1^+",
      "H": "Sigma_1^+, added ouvert,",
      "reading": "(sinon inserted l'ouvert Sigma_1^+ serait",
      "evidence": "The added group has a tall l, apostrophe and joined ouvert above the Sigma. The long bent guide attaches in the gap before Sigma. There are no commas surrounding the inserted group in the manuscript.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "18_louvert.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1294,
          2101,
          1612,
          2229
        ]
      },
      "related_graphics": [
        "GUIDE02"
      ]
    },
    {
      "id": "G01",
      "location": "left of opening Soient",
      "C": "omitted",
      "H": "omitted",
      "reading": "qualified detached dot",
      "evidence": "A short dark diagonal dot is visible alone near (192,143). Its shape is retained as a local dot candidate; no character function, hand or surface origin is assigned.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          188,
          137,
          198,
          150
        ]
      }
    },
    {
      "id": "GUIDE01",
      "location": "opening insertion, curved guide",
      "C": "insertion macro alone",
      "H": "added fermées without guide",
      "reading": "curved guide beneath fermés/fermées",
      "evidence": "The line rises from the gap after parties, bends right beneath the inserted word, then ends with a short upturn. The explicit TikZ path follows its observed endpoints; insertion wording and state remain as in D20.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "03_fermes.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          369,
          209,
          480,
          265
        ]
      },
      "path_component": "reading.tex GUIDE01",
      "coordinate_map": "local coordinates = full scan minus (195,169); x=.013cm, y=-.013cm"
    },
    {
      "id": "G02",
      "location": "right NB, upper stroke above first Sigma",
      "C": "no separate stroke",
      "H": "no separate stroke",
      "reading": "qualified separate horizontal rule above first Sigma",
      "evidence": "Above the first Sigma top arm there is another near-horizontal stroke, separated by a narrow white interval. NB has its own higher underline. The extra stroke is preserved as a rule with its role left undetermined.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "05_right_nb.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1267,
          385,
          1307,
          395
        ]
      },
      "path_component": "overset rule; no closure operation assigned"
    },
    {
      "id": "G03",
      "location": "drawing, detached dot above right exponent",
      "C": "omitted",
      "H": "omitted",
      "reading": "qualified detached dot",
      "evidence": "A small vertically elongated dark spot is separated from the dense exponent by a clear paper gap. It does not touch the subscript or Sigma.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "10_drawing_exponent.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          525,
          1190,
          536,
          1200
        ]
      },
      "path_component": "node (507,125) in main drawing",
      "coordinate_map": "full = local + (22,1069); role, hand and surface origin undetermined"
    },
    {
      "id": "G04",
      "location": "blank right of display (2)",
      "C": "omitted",
      "H": "omitted",
      "reading": "two qualified detached small marks",
      "evidence": "Two isolated small dark marks lie in the right-side blank area, one slightly above and to the right of the other. Their shapes are reproduced without a textual value or assigned surface origin.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1602,
          1779,
          1612,
          1791
        ]
      },
      "path_component": "G04 two fill ellipses"
    },
    {
      "id": "G05",
      "location": "below crossed vois. ouvert",
      "C": "omitted",
      "H": "omitted",
      "reading": "qualified detached rising stroke",
      "evidence": "The short dark oblique stroke sits below the cancelled words and above the Sigma expression, with a full paper gap at both ends. No attachment or meaning is assigned.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "15_vois_ouvert.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          508,
          2060,
          529,
          2081
        ]
      },
      "path_component": "G05 local draw (0,13) ... (16,0)",
      "coordinate_map": "body origin (219,2009); local component centred at (299,61)"
    },
    {
      "id": "G06",
      "location": "lower-left, curved stroke beside main lower display",
      "C": "omitted",
      "H": "omitted",
      "reading": "qualified curved guide",
      "evidence": "A pale curved line starts near (189,2214), bends upward and right above the main Sigma_2^- expression, and ends near (299,2151). Its path is preserved; the attachment and role are undetermined.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "17_lower_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          180,
          2145,
          304,
          2223
        ]
      },
      "path_component": "G06 local draw (9,69) ... (119,6)",
      "coordinate_map": "full = local + (180,2145)"
    },
    {
      "id": "G07",
      "location": "above final cancelled Sigma phrase",
      "C": "no separate upper cluster",
      "H": "no separate upper cluster",
      "reading": "qualified upper remnant paths",
      "evidence": "Above the readable Sigma there is a small angular/looped cluster and a short upright with their own endpoints. The crop supports paths, but not a secure extra word. They are drawn locally under doubt without duplicating the selected Sigma glyph.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "20_donc_cancelled.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          932,
          2239,
          972,
          2265
        ]
      },
      "H_coverage": "The shared final cancelled cluster is counted against H once in D19.",
      "path_component": "G07 two draw commands",
      "coordinate_map": "body origin (928,2238), local component centred at (28,14)"
    },
    {
      "id": "G08",
      "location": "drawing, lower-right oval rim",
      "C": "single continuous contour",
      "H": "described disk boundary",
      "reading": "separate pale lower-right run with locally qualified continuity",
      "evidence": "The right rim loses density below the lower transverse line. A pale short descending run and a further lower arc are separated by very narrow weak/blank intervals. The proposed path records these supported runs and leaves their exact continuity under local doubt.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          374,
          1278,
          413,
          1338
        ]
      },
      "path_component": "main drawing upper rim; qualified pale run; lower arc",
      "coordinate_map": "full = local + (22,1069)"
    },
    {
      "id": "G09",
      "location": "drawing, crossed upper-left label geometry",
      "C": "generic deleted line",
      "H": "cancelled label omitted",
      "reading": "two observed diagonal crossing runs",
      "evidence": "The label has two diagonal crossing runs; a generic added horizontal strike does not reproduce those runs. The proposed graphic uses an invisible deleted dimensional copy and draws the observed diagonals. The underlying text/state is D10.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "09_cancelled_drawing_label.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          155,
          1055,
          224,
          1124
        ]
      },
      "H_coverage": "H omission counted once in D10.",
      "path_component": "CANCEL01 two draw commands"
    },
    {
      "id": "G10",
      "location": "cancelled Car si, cancellation geometry",
      "C": "generic deleted line",
      "H": "phrase omitted",
      "reading": "two parallel crossing runs",
      "evidence": "The crop shows two distinct nearly horizontal cancellation runs with a small interval between them. Both are reproduced around the qualified word reading in D13.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "12_car_si.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          244,
          1469,
          416,
          1490
        ]
      },
      "H_coverage": "H omission counted once in D13.",
      "path_component": "Car-si figure, two draw commands"
    },
    {
      "id": "G11",
      "location": "case-heading underline before numeral 2",
      "C": "one continuous uline group",
      "H": "one emphasized group",
      "reading": "underline ending before 2, plus a short separate underline under 2",
      "evidence": "The wavy main underline stops below the equality; a separate short horizontal run lies beneath 2, with a visible gap. The proposed TeX uses two underline groups for these runs.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "08_case_heading.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          551,
          1064,
          932,
          1098
        ]
      }
    },
    {
      "id": "G12",
      "location": "final l'ouvert insertion guide",
      "C": "insertion macro alone",
      "H": "no guide",
      "reading": "long bent guide before Sigma_1^+",
      "evidence": "The guide rises from before Sigma, turns along the underside of l'ouvert and ends with a small right hook. GUIDE02 explicitly draws the line; the words and insertion attachment are recorded in H23.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "18_louvert.png",
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          1457,
          2148,
          1608,
          2201
        ]
      },
      "H_coverage": "H insertion cluster counted once in H23.",
      "path_component": "GUIDE02",
      "coordinate_map": "full = local + (1278,2080)"
    },
    {
      "id": "H24",
      "location": "drawing, left brace and contour details",
      "C": "two left-brace paths, right brace, two transverse lines",
      "H": "drawing description gives two braces and two chords",
      "reading": "all checked C paths retained apart from qualified rim revision",
      "evidence": "The left side contains two overlapping brace-like runs with forked/retraced lower ends, while the right brace is a separate thin run. H's verbal drawing description provides the broad arrangement but omits these local retracings; it is treated as apparatus, not manuscript prose.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; top-left origin; 1691×2360",
        "xyxy": [
          24,
          1074,
          466,
          1360
        ]
      }
    }
  ],
  "doubts": [
    {
      "location": "underlined title, overwritten initial",
      "reading": "\\uline{\\deleted{\\unsure{I|V}}Version I}",
      "alternatives": [
        "V"
      ],
      "confidence": "medium",
      "reason": "A central upright survives between transverse top and bottom strokes; the superposed oblique V strokes prevent separating the predecessor completely. I remains primary and V remains supported. The underline runs beneath the whole title, including the initial cluster. H puts its struck V outside the marked title span.",
      "crop": "01_heading.png",
      "difference_id": "D01a",
      "C_source_doubt_row": 1
    },
    {
      "location": "first indexed family, predecessor under E",
      "reading": "\\deleted{\\unsure{\\Sigma|S}}E_i",
      "alternatives": [
        "S"
      ],
      "confidence": "medium",
      "reason": "Inside the live upright E, a returning diagonal and rounded waist remain. The overlap prevents a secure separation of angular Sigma from S.",
      "crop": "02_first_family.png",
      "difference_id": "D02",
      "C_source_doubt_row": 2
    },
    {
      "location": "upper slanted note, after pour",
      "reading": "\\unsure{tte|toute|tt}",
      "alternatives": [
        "toute",
        "tt"
      ],
      "confidence": "low",
      "reason": "Two tall linked strokes and a short ending favour the abbreviated tte. The compressed intervening trace does not settle the longer spelling or the final e.",
      "crop": "04_upper_left_note.png",
      "difference_id": "D03",
      "C_source_doubt_row": 3
    },
    {
      "location": "right NB, second raised sign",
      "reading": "\\Sigma_i^{\\unsure{+|-|\\ast}}",
      "alternatives": [
        "-",
        "*"
      ],
      "confidence": "low",
      "reason": "The small raised patch has a broad horizontal body with short projections above and below it. Overlap obscures whether those projections belong to a plus, an overwritten minus, or a star-like form.",
      "crop": "05_right_nb.png",
      "difference_id": "D05",
      "C_source_doubt_row": 5
    },
    {
      "location": "case heading, predecessor inside parentheses",
      "reading": "\\deleted{\\unsure{(\\mathrm{de})}}(I)",
      "alternatives": [],
      "confidence": "low",
      "reason": "Below and left of the live I there is a small loop, a tall return and a low joining loop. The overwritten strokes support (de), with the complete earlier lettering still uncertain.",
      "crop": "08_case_heading.png",
      "difference_id": "D09a",
      "C_source_doubt_row": 9
    },
    {
      "location": "case heading, overwritten relation",
      "reading": "\\deleted{\\unsure{\\leq|=}}=",
      "alternatives": [
        "="
      ],
      "confidence": "low",
      "reason": "Two thick horizontal runs enclose oblique, partly triangular traces. These traces do not isolate the older relation securely. The live two-stroke equality is preserved.",
      "crop": "08_case_heading.png",
      "difference_id": "D09b",
      "C_source_doubt_row": 9
    },
    {
      "location": "drawing, cancelled upper-left label",
      "reading": "\\deleted{\\unsure{\\Sigma_1^+|\\Sigma_2^+}}",
      "alternatives": [
        "Sigma_2^+"
      ],
      "confidence": "low",
      "reason": "An angular Sigma and raised cross remain beneath multiple diagonal crossings. The lowered right-hand form is crowded by a descending cancellation return, leaving 1 and 2 unresolved. CANCEL01 reproduces the two crossing runs visible above the ordinary glyph.",
      "crop": "09_cancelled_drawing_label.png",
      "difference_id": "D10",
      "C_source_doubt_row": 10
    },
    {
      "location": "drawing, right-hand raised correction",
      "reading": "\\Sigma_1^{\\deleted{\\unsure{+}}\\unsure{-}}",
      "alternatives": [
        "exponent strokes unresolved"
      ],
      "confidence": "low",
      "reason": "The raised area is a dense rectangular patch with several horizontal runs and short vertical connections. A central minus and crossed plus are supported but cannot be cleanly isolated. The independent dot above the patch is recorded separately as G03.",
      "crop": "10_drawing_exponent.png",
      "difference_id": "D11",
      "C_source_doubt_row": 11
    },
    {
      "location": "cancelled phrase under the oval",
      "reading": "\\deleted{\\unsure{Car si|car si}}",
      "alternatives": [
        "car si"
      ],
      "confidence": "low",
      "reason": "The initial open curve is substantially taller than the following low letters, favouring capital C. A rounded next loop, compressed joining trace, final curved s and i dot remain between two long horizontal cancellations. Lower-case car si remains an alternative because the cancellation obscures the first group.",
      "crop": "12_car_si.png",
      "difference_id": "D13",
      "C_source_doubt_row": 13
    },
    {
      "location": "before symétriquement",
      "reading": "\\unsure{et}",
      "alternatives": [],
      "confidence": "low",
      "reason": "Only a pale small oblique trace and a separate shallow arch remain at the start of this line. They support the supplied et candidate without revealing a complete t stem.",
      "crop": "14_et_symetrique.png",
      "difference_id": "D14",
      "C_source_doubt_row": 14
    },
    {
      "location": "crossed wording above lower Sigma_2^-",
      "reading": "\\deleted{\\unsure{vois. ouvert}}",
      "alternatives": [
        "abbreviation point obscured"
      ],
      "confidence": "medium",
      "reason": "The v bowl, o loop, i dot and s curve, followed by the open middle letters and tall terminal t of ouvert, are readable. The crossing line covers the place of the abbreviation point, so the qualified phrase is retained.",
      "crop": "15_vois_ouvert.png",
      "difference_id": "D15",
      "C_source_doubt_row": 15
    },
    {
      "location": "lower slanted note, phrase before avant",
      "reading": "\\unsure{à signaler|à sign.ler} avant",
      "alternatives": [
        "à sign.ler"
      ],
      "confidence": "low",
      "reason": "The accented à, s/i group and long g descender are visible. The compressed continuation and small point-like interruption do not settle signaler versus sign.ler. The far-right ending approaches the planned crop boundary, and no repeat crop was made. Avant is readable on the next slanted line.",
      "crop": "17_lower_margin.png",
      "difference_id": "D16",
      "C_source_doubt_row": 16
    },
    {
      "location": "final sentence, insertion above fermé",
      "reading": "\\inserted{\\unsure{un|une}}",
      "alternatives": [
        "une"
      ],
      "confidence": "low",
      "reason": "A short linked wave sits above the gap before fermé. Its terminal hump runs toward the high beginning of f; a separate final e cannot be isolated.",
      "crop": "19_un_ferme.png",
      "difference_id": "D17",
      "C_source_doubt_row": 17
    },
    {
      "location": "final cancelled phrase",
      "reading": "\\deleted{\\unsure{$\\Sigma_1^+$ serait}}",
      "alternatives": [],
      "confidence": "low",
      "reason": "The Sigma, lowered 1 and raised cross remain readable. To their right a compressed connected run ends in a tall looped/crossed t-like form. This favours the supplied serait reading; the intermediate letters remain obscured. The additional upper traces are reproduced separately as G07, without supplying a word for them.",
      "crop": "20_donc_cancelled.png",
      "difference_id": "D19",
      "C_source_doubt_row": 19
    },
    {
      "location": "opening insertion above de X",
      "reading": "\\inserted{\\unsure{fermés|fermées}}",
      "alternatives": [
        "fermées"
      ],
      "confidence": "medium",
      "reason": "The f stem, compressed middle joins, detached acute and terminal s hook are visible. The small vowel immediately before s remains too compressed to settle one versus two e strokes. Fermés remains the primary visual candidate.",
      "crop": "03_fermes.png",
      "difference_id": "D20",
      "C_source_doubt_row": 20
    },
    {
      "location": "left of opening Soient",
      "reading": "qualified detached dot",
      "alternatives": [],
      "confidence": "medium",
      "reason": "A short dark diagonal dot is visible alone near (192,143). Its shape is retained as a local dot candidate; no character function, hand or surface origin is assigned.",
      "crop": null,
      "difference_id": "G01",
      "qualification": "Visible shape retained; character, role, hand or surface origin remains undetermined as stated. G08 concerns rim continuity."
    },
    {
      "location": "right NB, upper stroke above first Sigma",
      "reading": "qualified separate horizontal rule above first Sigma",
      "alternatives": [],
      "confidence": "medium",
      "reason": "Above the first Sigma top arm there is another near-horizontal stroke, separated by a narrow white interval. NB has its own higher underline. The extra stroke is preserved as a rule with its role left undetermined.",
      "crop": "05_right_nb.png",
      "difference_id": "G02",
      "qualification": "Visible shape retained; character, role, hand or surface origin remains undetermined as stated. G08 concerns rim continuity."
    },
    {
      "location": "drawing, detached dot above right exponent",
      "reading": "qualified detached dot",
      "alternatives": [],
      "confidence": "high",
      "reason": "A small vertically elongated dark spot is separated from the dense exponent by a clear paper gap. It does not touch the subscript or Sigma.",
      "crop": "10_drawing_exponent.png",
      "difference_id": "G03",
      "qualification": "Visible shape retained; character, role, hand or surface origin remains undetermined as stated. G08 concerns rim continuity."
    },
    {
      "location": "blank right of display (2)",
      "reading": "two qualified detached small marks",
      "alternatives": [],
      "confidence": "medium",
      "reason": "Two isolated small dark marks lie in the right-side blank area, one slightly above and to the right of the other. Their shapes are reproduced without a textual value or assigned surface origin.",
      "crop": null,
      "difference_id": "G04",
      "qualification": "Visible shape retained; character, role, hand or surface origin remains undetermined as stated. G08 concerns rim continuity."
    },
    {
      "location": "below crossed vois. ouvert",
      "reading": "qualified detached rising stroke",
      "alternatives": [],
      "confidence": "high",
      "reason": "The short dark oblique stroke sits below the cancelled words and above the Sigma expression, with a full paper gap at both ends. No attachment or meaning is assigned.",
      "crop": "15_vois_ouvert.png",
      "difference_id": "G05",
      "qualification": "Visible shape retained; character, role, hand or surface origin remains undetermined as stated. G08 concerns rim continuity."
    },
    {
      "location": "lower-left, curved stroke beside main lower display",
      "reading": "qualified curved guide",
      "alternatives": [],
      "confidence": "medium",
      "reason": "A pale curved line starts near (189,2214), bends upward and right above the main Sigma_2^- expression, and ends near (299,2151). Its path is preserved; the attachment and role are undetermined.",
      "crop": "17_lower_margin.png",
      "difference_id": "G06",
      "qualification": "Visible shape retained; character, role, hand or surface origin remains undetermined as stated. G08 concerns rim continuity."
    },
    {
      "location": "above final cancelled Sigma phrase",
      "reading": "qualified upper remnant paths",
      "alternatives": [],
      "confidence": "medium",
      "reason": "Above the readable Sigma there is a small angular/looped cluster and a short upright with their own endpoints. The crop supports paths, but not a secure extra word. They are drawn locally under doubt without duplicating the selected Sigma glyph.",
      "crop": "20_donc_cancelled.png",
      "difference_id": "G07",
      "qualification": "Visible shape retained; character, role, hand or surface origin remains undetermined as stated. G08 concerns rim continuity."
    },
    {
      "location": "drawing, lower-right oval rim",
      "reading": "separate pale lower-right run with locally qualified continuity",
      "alternatives": [],
      "confidence": "medium",
      "reason": "The right rim loses density below the lower transverse line. A pale short descending run and a further lower arc are separated by very narrow weak/blank intervals. The proposed path records these supported runs and leaves their exact continuity under local doubt.",
      "crop": null,
      "difference_id": "G08",
      "qualification": "Visible shape retained; character, role, hand or surface origin remains undetermined as stated. G08 concerns rim continuity."
    }
  ],
  "notes": {
    "page_content": "Handwritten topological separation discussion headed Version I. Conditions (a) and (b), two marginal notes, a right NB, the case Card(I)=2, an oval split by two transverse lines, relations (1),(2),(2′), and a final argument continuing after disconnexe), are all transcribed.",
    "author_uncertainty_or_instruction": "The lower slanted note ends with the qualified words à signaler|à sign.ler followed by readable avant. No written mathematical question mark was identified; transcription doubt marks are editorial.",
    "title_date_page_counts": "Underlined Version I; no date or author page number identified. Archive 14 is recorded only in a comment and attributed to an undetermined hand. H page{14} is metadata, not additional manuscript text.",
    "mathematics_led_reading_decisions": "No formula was changed from mathematical expectation. The written NB automatically les wording and the right-note Sigma reading remain as observed. No proof, theorem, example or mathematical computation was performed.",
    "source_doubt_mapping": "The 21 actual rows in C Doubtful readings map to D01a/D01b, D02 through D08, D09a/D09b, D10 through D20, and D21a/D21b. The seven notation rows, three Slips retained rows and seven abbreviation rows were treated as their supplied source categories, not additional source doubts.",
    "source_apparatus": "H drawing orientation and explanatory description are treated as apparatus. H uncertainty markers alone do not create a difference. One H ill remainder is counted once in H04; local D16 is covered by it. Shared physical clusters are cross-referenced where a graphical detail has no additional H count.",
    "drawing_path_map": "The main drawing uses the individually checked C contour, two transverse paths, two left-brace paths and one right brace. Its mapping is full scan = local + (22,1069). G08 splits the weak lower-right rim into supported runs. Upper cancelled label crossings use CANCEL01. Other fixed origins are stated next to their commands and in the graphical rows.",
    "crop_limits": "No settled locus was cropped again. Crop 07 reaches the final t crossbar at its right edge; half a supplied that endpoint. Crop 14 cuts part of the descender from the neighbouring word but retains its actual targets. Crop 17 leaves the lower-note far-right ending at the edge; the uncertainty is retained. No new crop was made for these limits.",
    "validation": "One final source/report synchronization pass completed: brace balance, environment nesting, math delimiters, required report fields, permitted kind values, all 20 crop references, all 21 source rows/24 local decisions, exact TeX strings for every source-doubt reading, qualified graphical additions and archive comment were checked. No compiler or rendering was used."
  },
  "notation": [
    {
      "location": "(a) and case heading",
      "sign": "Card with capital C",
      "proposed_LaTeX": "\\operatorname{Card}",
      "evidence": "large open initial C above low a/r; tall final d"
    },
    {
      "location": "(a)",
      "sign": "pi with lower 0",
      "proposed_LaTeX": "\\pi_0",
      "evidence": "top horizontal arch and small lowered round trace"
    },
    {
      "location": "corrected E family/(a)/(b)/NB",
      "sign": "E over angular Sigma predecessor",
      "proposed_LaTeX": "\\deleted{\\Sigma}E_i",
      "evidence": "upright and three arms cross an older angular inner path; first occurrence retains S alternative"
    },
    {
      "location": "upper-left note",
      "sign": "conn. and dotted lower i",
      "proposed_LaTeX": "conn. $\\Sigma_i$",
      "evidence": "two n shoulders plus point; separate small dot and short low stroke beside Sigma"
    },
    {
      "location": "margin closures and last argument",
      "sign": "separate cap over Sigma",
      "proposed_LaTeX": "\\overline{\\Sigma}_i,\\overline{\\Sigma_1^+}",
      "evidence": "detached near-horizontal cap; scope follows each local stroke"
    },
    {
      "location": "right NB",
      "sign": "setminus followed by open angular Sigma",
      "proposed_LaTeX": "X\\setminus\\Sigma_i",
      "evidence": "two turning diagonal legs and lower arm; open left side"
    },
    {
      "location": "lower formulas",
      "sign": "subset/superset without lower bars",
      "proposed_LaTeX": "\\subset,\\supset",
      "evidence": "single curved-sided relation stroke; no parallel lower equality bar"
    },
    {
      "location": "purpose paragraph",
      "sign": "paired quotation ticks",
      "proposed_LaTeX": "``découpage''",
      "evidence": "two short ticks on each side"
    },
    {
      "location": "display labels",
      "sign": "(a),(b),(1),(2),(2′)",
      "proposed_LaTeX": "\\tag*{(a)} ... \\tag*{$(2\\prime)$}",
      "evidence": "parentheses at left; raised prime after final 2"
    },
    {
      "location": "three lower à endpoints",
      "sign": "small a plus separate accent, without colon",
      "proposed_LaTeX": "à",
      "evidence": "low a-like mark and one separate upper accent; no extra punctuation pair"
    },
    {
      "location": "bottom left",
      "sign": "archive 14",
      "proposed_LaTeX": "% archive sheet number: 14",
      "evidence": "pale 1 followed by open 4; hand undetermined"
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The source-row reminder was read and followed: three compound source rows have separate local decisions while keeping their original row identity.",
    "The strict single-crop limit leaves the lower-note final lettering qualified after its far-right continuation approached the planned boundary.",
    "Detached shapes and the extra upper rule are represented under local doubt; their visible shapes do not establish a mathematical role."
  ]
}

## Reader C

\scanpage{15}
\begingroup
\makeatletter
\tagsleft@true
\makeatother
\uline{\deleted{\unsure{I|V}}Version I}

Soient $X$ un espace topologique, $(\deleted{\unsure{\Sigma|S}}E_i)_{i\in I}$ un ens. de % GUIDE01: full-scan origin (190,169), local coordinates in source pixels.
\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(p.base),line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (385,113);
\node[anchor=base west,inner sep=0pt] (p) at (19,89) {parties};
\node[anchor=base west,inner sep=0pt] at (210,89) {de $X$};
\node[anchor=base west,inner sep=0pt] at (136,38) {\inserted{\unsure{fermés|fermées}}};
\draw (185,87) .. controls (180,63) and (188,54) .. (214,52)
 .. controls (240,47) and (265,61) .. (286,44);
\end{tikzpicture} (noté indiciellement), telles que l'on ait
% slanted
\reversemarginpar
\margin{$\nearrow$ On suppose de plus que pour \unsure{tte|toute|tt} comp. conn. $\unsure{\Sigma_i|\Sigma}$ de $X\setminus E_i$, on ait $\overline{\Sigma}_i\cap E_i\ne\varnothing$ i.e. $\overline{\Sigma}_i\ne\Sigma_i$ i.e. $\Sigma_i$ non fermé dans $X$ (ce qui est le cas si $X$ est connexe)}
\normalmarginpar
\[
 \forall i\in I,\quad \operatorname{Card}\pi_0(X\setminus\deleted{\Sigma}E_i)=2
 \tag*{(a)}
\]
\margin{\uline{NB} les comp. conn. $\Sigma_i^+,\Sigma_i^{\unsure{+|-|\ast}}$ de $X\setminus\Sigma_i$ sont ouvertes dans $X$}
\[
 \begin{aligned}
 &\forall(i,j)\in I\times I,\ i\ne j,\quad \deleted{\Sigma}E_j\ \text{est contenu dans l'une}\\
 &\text{des deux composantes connexes de }X\setminus\deleted{\Sigma}E_i.
 \end{aligned}
 \tag*{(b)}
\]

NB Cette condition (b) est vérifiée automatiquement les $\deleted{\Sigma}E_i$ $(i\in I)$ sont connexes, dès lors que les $E_i$ sont supposés disjoints mutuellement

On se propose d'étudier le ``découpage'' de $X$ par la famille $(E_i)$.

% RULE01/RULE02: full-scan origin (500,994); the underline has two visible runs.
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (458,106);
\node[anchor=base west,inner sep=0pt] at (15,75) {Cas};
\node[anchor=base west,inner sep=0pt] at (142,75) {$\operatorname{Card}$};
\node[anchor=base west,inner sep=0pt] at (252,66) {$\deleted{\unsure{(\mathrm{de})}}(I)$};
\node[anchor=base west,inner sep=0pt] at (331,66) {$\deleted{\unsure{\leq|=}}=$};
\node[anchor=base west,inner sep=0pt] at (395,66) {$2$};
\draw (31,94) .. controls (80,80) and (111,104) .. (169,87)
 .. controls (206,75) and (218,94) .. (259,82)
 .. controls (300,72) and (312,91) .. (353,80)
 .. controls (364,79) and (375,77) .. (378,82);
\draw (395,80) -- (428,80);
\end{tikzpicture}}

Soit $\Sigma_i^+$ la comp. conn. de $X\setminus E_i$ qui ne contient pas $E_j$ $(j\ne i)$, alors on a (si $I=\{1,2\}$)
% DRAW01: full-scan origin (19,1038), fixed local source-pixel rectangle.
% C's two left-brace paths and right-brace path are retained after checking,
% with local translation (5,33), i.e. full-scan origin (24,1071) for those paths.
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (553,336);
% Oval: visible strong runs, pale runs and short gaps are distinct paths.
\draw (186,122) .. controls (210,76) and (262,35) .. (290,38)
 .. controls (342,35) and (380,88) .. (402,160);
\draw (403,168) .. controls (405,185) and (403,206) .. (401,216);
\draw[black!45] (401,217) .. controls (401,226) and (398,235) .. (394,243);
\draw (391,249) .. controls (387,257) and (382,263) .. (378,267);
\draw (374,273) .. controls (369,282) and (365,287) .. (361,291);
\draw (358,295) .. controls (334,319) and (294,320) .. (269,315)
 .. controls (219,309) and (178,276) .. (169,220)
 .. controls (166,206) and (168,197) .. (168,193);
\draw (168,193) .. controls (163,196) and (163,190) .. (166,181);
\draw (168,193) -- (173,185);
\draw[black!45] (168,179) .. controls (174,160) and (179,139) .. (186,122);
% Chords, separately checked at both rim contacts.
\draw[line width=.8pt] (186,122) .. controls (247,125) and (324,109) .. (392,119)
 (176,250) .. controls (242,253) and (328,246) .. (391,239);
\begin{scope}[shift={(5,33)}]
\draw (44,9) .. controls (46,57) and (63,106) .. (32,108)
 .. controls (52,132) and (38,151) .. (46,195) -- (55,228);
\draw (41,109) .. controls (72,143) and (35,144) .. (48,193)
 .. controls (47,224) and (57,241) .. (39,252) .. controls (55,242) and (43,259) .. (49,282);
\draw (428,86) .. controls (439,93) and (409,141) .. (434,149)
 .. controls (420,158) and (436,251) .. (417,254);
\end{scope}
% Cancelled label: one visible text copy, actual crossing paths, invisible deletion annotation.
\node[inner sep=0pt] at (167,48) {\rlap{$\unsure{\Sigma_1^+|\Sigma_2^+}$}\phantom{$\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}$}};
\draw (138,60) -- (198,27);
\draw (151,42) .. controls (161,20) and (181,12) .. (177,24) -- (149,52);
\node at (139,116) {$E_1$}; \node at (150,247) {$E_2$};
\node at (430,68) {$\Sigma_1^+$};
\node at (501,193) {$\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}$};
\node at (23,135) {$\Sigma_2^-$}; \node at (131,308) {$\Sigma_2^+$};
% MARK01: detached short dot above the right overwritten superscript;
% full-scan observed bbox approximately (525,1189,531,1198), role/hand unresolved.
\node[inner sep=0pt] at (509,156) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
\path[use as bounding box] (0,0) rectangle (4,6);
\fill (1,0) .. controls (4,1) and (4,4) .. (2,6) .. controls (0,5) and (0,2) .. (1,0);
\end{tikzpicture}}};
\end{tikzpicture}}

\[
 \Sigma_1^+\cap\Sigma_2^+=\varnothing
 \tag*{(1)}
\]
ce qui \deleted{résulte de}
\[
 \begin{aligned}
 &\deleted{\Sigma_1^-\supset\Sigma_2^+}\qquad\text{\unsure{équivaut|èquivaut} à}\\
 &\deleted{\Sigma_2^-\supset\Sigma_1^+}\qquad \Sigma_1^+\subset\Sigma_2^-\cup E_2,\quad\text{et}
 \end{aligned}
\]
% CANCEL01/CANCEL02: full-scan origin (206,1437); two cancellation runs.
\figure{\begin{tikzpicture}[x=.018cm,y=-.018cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (232,73);
\node[anchor=base west,inner sep=0pt] at (16,47) {\rlap{\unsure{car si|Car si}}\phantom{\deleted{\unsure{car si|Car si}}}};
\draw (42,37) .. controls (100,40) and (155,34) .. (201,37);
\draw (43,47) .. controls (95,47) and (153,53) .. (215,47);
\end{tikzpicture}}
\deleted{Si on avait} comme $\Sigma_1^+\cap E_2=\varnothing$, cela équivaut aussi à
\[
 \Sigma_1^+\subset\Sigma_2^-
 \tag*{(2)}
\]
\unsure{et} \unsure{symètriquement|symétriquement}, à
\[
 \Sigma_2^+\subset\Sigma_1^-
 \tag*{$(2')$}
\]

Comme
% MARK02 and raised cancelled words: full-scan origin (409,2008).
\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(inc.base),line cap=round]
\path[use as bounding box] (0,0) rectangle (319,136);
\node[anchor=base west,inner sep=0pt] at (16,42) {\deleted{\unsure{vois. ouvert}}};
\node[anchor=base west,inner sep=0pt] (inc) at (75,113) {$\Sigma_2^-\supset E_1$,};
\node[inner sep=0pt] at (111,61) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (19,16);
\draw[line width=.6pt] (1,15) .. controls (8,7) and (13,3) .. (18,2);
\end{tikzpicture}}};
\end{tikzpicture} \deleted{il contient les} \inserted{i.e. $\Sigma_2^-$ est un \uline{vois.} ouvert de $E_1$,} on a
% slanted
\reversemarginpar
\margin{$\overline{\Sigma_1^+}\cap E_1\ne\varnothing$ i.e. $\overline{\Sigma_1^+}\ne\Sigma_1^+$ \unsure{à sign.ler|à signaler} avant}
\normalmarginpar
% GUIDE02: observed curved stroke above the first Sigma of the next display.
% Fixed full-scan origin (180,2158); no character or mathematical role assigned.
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (125,67);
\node[inner sep=0pt] at (62,33) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
\path[use as bounding box] (0,0) rectangle (125,67);
\draw[black!65] (7,59) .. controls (0,34) and (22,28) .. (60,21)
 .. controls (87,18) and (105,13) .. (118,7);
\end{tikzpicture}}};
\end{tikzpicture}}
\[
 \Sigma_2^-\cap\Sigma_1^+\ne\varnothing
\]
Car $\underline{\overline{\Sigma_1^+}\cap E_1}\ne\varnothing$ % GUIDE03: full-scan origin (1274,2097); hooked insertion guide retained.
\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(sin.base),line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (386,173);
\node[anchor=base west,inner sep=0pt] (sin) at (20,102) {(sinon};
\node[anchor=base west,inner sep=0pt] at (220,102) {$\Sigma_1^+$};
\node[anchor=base west,inner sep=0pt] at (171,49) {\inserted{\unsure{l'ouvert|louvert}}};
\draw (188,100) .. controls (202,61) and (226,56) .. (258,60)
 .. controls (292,63) and (317,61) .. (331,55) -- (329,51);
\end{tikzpicture} serait \inserted{un} fermé dans $X$, \unsure{donc|puis} % CANCEL03: full-scan origin (920,2238), one text copy and visible overstrikes.
\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(del.base),line cap=round,line join=round]
\path[use as bounding box] (0,0) rectangle (177,67);
\node[anchor=base west,inner sep=0pt] (del) at (16,49) {\rlap{$\unsure{\Sigma_1^+\text{ serait}|\Sigma_1^+\ne\varnothing}$}\phantom{$\deleted{\unsure{\Sigma_1^+\text{ serait}|\Sigma_1^+\ne\varnothing}}$}};
\draw (14,31) -- (53,9);
\draw (8,25) -- (18,5) -- (24,29) -- (39,23);
\draw (24,32) .. controls (60,23) and (105,29) .. (164,39);
\end{tikzpicture} $X$ serait disconnexe),
\endgroup
% archive sheet number: 14



{
  "differences": [
    {
      "id": "D01a",
      "location": "Heading, overwritten initial",
      "C": "deleted I|V",
      "H": "deleted V",
      "reading": "deleted I|V",
      "evidence": "A tall interior upright and upper/lower transverse strokes survive inside the heavy V-shaped strokes. Their overlap does not settle the predecessor; H V survives as the second candidate.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "01_heading.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          40,
          18,
          285,
          118
        ]
      },
      "C_source_doubt_row": 1
    },
    {
      "id": "D01b",
      "location": "Heading, live word",
      "C": "unsure Version",
      "H": "Version",
      "reading": "Version",
      "evidence": "The sequence after the large initial has an e loop, r shoulder, s rise, narrow i stroke, o and final n. The final separate serifed I is clear.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "01_heading.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          40,
          18,
          285,
          118
        ]
      },
      "C_source_doubt_row": 1
    },
    {
      "id": "D02",
      "location": "Opening indexed family, predecessor under E",
      "C": "deleted Sigma|S",
      "H": "E_i only",
      "reading": "deleted Sigma|S followed by E_i",
      "evidence": "Two curved oblique returns remain between the three E bars. The overdrawn middle prevents a decisive angular/rounded predecessor reading. H omits the surviving predecessor.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "02_family.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          1118,
          114,
          1355,
          224
        ]
      },
      "C_source_doubt_row": 2
    },
    {
      "id": "D03",
      "location": "Upper slanted note, between pour and comp.",
      "C": "tte|toute|tt",
      "H": "toute",
      "reading": "tte|toute|tt",
      "evidence": "The small group has two tall connected strokes and a compressed low ending. The abbreviated primary survives; the enlargement does not separate the last e from the joins. H toute survives as an alternative.",
      "confidence": "low",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          25,
          510,
          193,
          661
        ]
      },
      "C_source_doubt_row": 3
    },
    {
      "id": "D04",
      "location": "Upper slanted note, before fermé",
      "C": "unsure non",
      "H": "n'est pas",
      "reading": "non",
      "evidence": "A short n-shaped hump, rounded middle and second low hump are visible above the intrusive main-line NB; there is no separate est or pas sequence.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          252,
          573,
          330,
          631
        ]
      },
      "C_source_doubt_row": 4
    },
    {
      "id": "D05",
      "location": "Right NB, second superscript",
      "C": "+|-|*",
      "H": "-",
      "reading": "+|-|*",
      "evidence": "The compact dark overdraw has a horizontal arm and lower projecting stroke. The black overlap leaves +, - and star candidates open. H minus survives as an alternative.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "06_right_NB.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          1412,
          379,
          1443,
          405
        ]
      },
      "C_source_doubt_row": 5
    },
    {
      "id": "D06",
      "location": "Right NB, glyph after X minus",
      "C": "Sigma|E",
      "H": "E",
      "reading": "Sigma",
      "evidence": "The glyph has an open left edge, upper oblique return and lower horizontal return. It carries no connecting left upright of the E forms visible in (a) and (b).",
      "confidence": "high",
      "kind": "misread symbol or index",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "06_right_NB.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          1573,
          379,
          1623,
          429
        ]
      },
      "C_source_doubt_row": 6
    },
    {
      "id": "D07",
      "location": "Display (b), last overwritten E",
      "C": "deleted unsure Sigma then E_i",
      "H": "E_i",
      "reading": "deleted Sigma then E_i",
      "evidence": "The surviving upper and lower diagonals meet at the right point inside the E. The lowered i and final full stop are separate and clear.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "08_b_Ei.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          1397,
          515,
          1667,
          610
        ]
      },
      "C_source_doubt_row": 7
    },
    {
      "id": "D08",
      "location": "NB prose, end of first line",
      "C": "unsure automatiquement",
      "H": "automatiquement",
      "reading": "automatiquement",
      "evidence": "Pale initial a/u strokes continue into the tall t and connected omatiquement ending. The full letter run is recoverable despite uneven ink.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "09_automatiquement.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          965,
          606,
          1682,
          720
        ]
      },
      "C_source_doubt_row": 8
    },
    {
      "id": "D09a",
      "location": "Case heading, old parenthetical under (I)",
      "C": "deleted unsure (de)",
      "H": "omitted",
      "reading": "deleted unsure (de)",
      "evidence": "A small loop and adjoining e-like return survive under the large current I and parenthesis. The overlapping strokes do not isolate the complete old parenthetical.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "10_case.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          753,
          1017,
          823,
          1069
        ]
      },
      "C_source_doubt_row": 9
    },
    {
      "id": "D09b",
      "location": "Case heading, overwritten relation",
      "C": "deleted <=|= then =",
      "H": "=",
      "reading": "deleted <=|= then =",
      "evidence": "A short angular lower turn remains between and below the heavy horizontal bars. The earlier relation remains <= or =.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "10_case.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          830,
          1028,
          887,
          1066
        ]
      },
      "C_source_doubt_row": 9
    },
    {
      "id": "D10",
      "location": "Drawing, crossed upper-left label",
      "C": "deleted Sigma_1^+|Sigma_2^+",
      "H": "omitted",
      "reading": "deleted Sigma_1^+|Sigma_2^+",
      "evidence": "The capital Sigma and raised cross remain readable; the lower-right digit is entangled with oblique cancellation strokes. No digit is selected from the nearby live labels.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "11_drawing.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          153,
          1054,
          226,
          1125
        ]
      },
      "C_source_doubt_row": 10
    },
    {
      "id": "D11",
      "location": "Drawing, right brace superscript",
      "C": "deleted unsure + followed by unsure -",
      "H": "live -",
      "reading": "deleted unsure + followed by unsure -",
      "evidence": "A compact rectangular dark overdraw contains intersecting horizontal and upright pieces with light openings. The predecessor and live sign remain qualified; H gives only the live minus.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "11_drawing.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          520,
          1200,
          561,
          1226
        ]
      },
      "C_source_doubt_row": 11
    },
    {
      "id": "D12",
      "location": "Right of first cancelled inclusion",
      "C": "unsure équivaut",
      "H": "équivaut",
      "reading": "équivaut|èquivaut",
      "evidence": "The initial e, q bowl and descending stem, compressed ui/v run and long final stroke support the word. The tiny detached accent does not confidently settle its direction. Crop 12 clips only the lowest q-tail endpoint; half b shows the full descender.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "12_equivaut.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          1095,
          1400,
          1389,
          1490
        ]
      },
      "C_source_doubt_row": 12
    },
    {
      "id": "D13",
      "location": "Under drawing, cancelled short phrase",
      "C": "deleted unsure car si",
      "H": "omitted",
      "reading": "deleted car si|Car si",
      "evidence": "An open initial curve, low rounded run, final s-like stem and separate i dot survive between two cancellation lines. The initial case remains open.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "13_car_si.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          206,
          1437,
          438,
          1510
        ]
      },
      "C_source_doubt_row": 13,
      "physical_cluster": "car_si"
    },
    {
      "id": "D14",
      "location": "Before symétriquement",
      "C": "unsure et",
      "H": "omitted",
      "reading": "unsure et",
      "evidence": "Only two pale separated strokes remain at the start of the line; they support the source candidate without resolving it.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "15_symetriquement.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          230,
          1899,
          291,
          1923
        ]
      },
      "C_source_doubt_row": 14
    },
    {
      "id": "D15",
      "location": "Above bottom inclusion, cancelled words",
      "C": "deleted unsure vois. ouvert",
      "H": "deleted vois. ouvert",
      "reading": "deleted unsure vois. ouvert",
      "evidence": "The v/o loops, dotted i, and open ou run ending in a tall t are visible through the cancellation. The abbreviation point is crowded against the crossing rule; the phrase retains its qualification.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "16_vois.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          421,
          2023,
          636,
          2065
        ]
      },
      "C_source_doubt_row": 15
    },
    {
      "id": "D16",
      "location": "Lower slanted note, after second inequality",
      "C": "à signaler|à sign.ler",
      "H": "covered by the lower marginal ill placeholder",
      "reading": "à sign.ler|à signaler",
      "evidence": "After sig/n there is a small detached low point before the tall l and final er. The point makes the abbreviated spelling the stronger visible candidate; a compressed a remains possible. The source row is retained with reversed candidate priority.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "17_lower_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          267,
          1970,
          453,
          2105
        ]
      },
      "C_source_doubt_row": 16,
      "H_omission_cross_reference": "H26"
    },
    {
      "id": "D17",
      "location": "Bottom line, raised word before fermé",
      "C": "un|une",
      "H": "omitted",
      "reading": "inserted un",
      "evidence": "Two short raised humps form un. The following horizontal segment connects to the tall loop/stem of f below, rather than supplying a separate e.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "19_un.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          387,
          2250,
          448,
          2276
        ]
      },
      "C_source_doubt_row": 17
    },
    {
      "id": "D18",
      "location": "Bottom line, connector before deleted group",
      "C": "donc|puis",
      "H": "donc",
      "reading": "donc|puis",
      "evidence": "The first loop has a long descending stroke; the following rounded middle and low humps do not securely separate all letters. Primary donc and alternative puis remain.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "20_donc.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          831,
          2275,
          946,
          2340
        ]
      },
      "C_source_doubt_row": 18
    },
    {
      "id": "D19",
      "location": "Bottom, cancelled mathematical/prose group",
      "C": "deleted unsure Sigma_1^+ serait",
      "H": "deleted Sigma_1^+ neq emptyset",
      "reading": "deleted Sigma_1^+ serait | Sigma_1^+ neq emptyset",
      "evidence": "Sigma, lower 1 and raised + survive. The compressed following run and final tall loop remain crowded by oblique and near-horizontal overstrikes. H’s crossed formula survives as a supported alternative, not a conclusively rejected reading.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "20_donc.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          926,
          2241,
          1090,
          2303
        ]
      },
      "C_source_doubt_row": 19,
      "physical_cluster": "final_cancelled"
    },
    {
      "id": "D20",
      "location": "Opening raised insertion",
      "C": "fermés|fermées",
      "H": "fermées",
      "reading": "inserted fermés|fermées",
      "evidence": "The insertion has a tall f, compressed erm run, separate accented vowel stroke and final s. A second e cannot be isolated securely. H’s fermées is retained as an alternative.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "03_fermes.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          325,
          180,
          455,
          222
        ]
      },
      "C_source_doubt_row": 20
    },
    {
      "id": "D21a",
      "location": "Upper slanted note, component abbreviation",
      "C": "conn.|connex.",
      "H": "conn.",
      "reading": "conn.",
      "evidence": "The c opening is followed by two low n humps and a separate terminal point; no additional ex strokes intervene.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          29,
          586,
          143,
          701
        ]
      },
      "C_source_doubt_row": 21
    },
    {
      "id": "D21b",
      "location": "Upper slanted note, first Sigma index",
      "C": "Sigma with unsure i",
      "H": "Sigma_i",
      "reading": "Sigma_i|Sigma",
      "evidence": "A small low dot lies to the right of the first Sigma, but an independent descending index shaft is not securely isolated. The full indexed and unindexed candidates are retained.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          121,
          540,
          204,
          598
        ]
      },
      "C_source_doubt_row": 21
    },
    {
      "id": "H01",
      "location": "Heading underline span",
      "C": "underline includes cancelled initial and Version I",
      "H": "emphasis begins at Version",
      "reading": "underline includes whole heading",
      "evidence": "The single rising rule begins under the cancelled initial and continues beneath the final I.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "01_heading.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          40,
          18,
          285,
          118
        ]
      }
    },
    {
      "id": "H02",
      "location": "Upper slanted note opening",
      "C": "On suppose",
      "H": "Supposons",
      "reading": "On suppose",
      "evidence": "A separate capital O/n group precedes suppose. The final word ends without the ns of Supposons.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          28,
          397,
          208,
          578
        ]
      }
    },
    {
      "id": "H03",
      "location": "Upper note attachment",
      "C": "nearrow",
      "H": "omitted",
      "reading": "nearrow",
      "evidence": "A slanting shaft rises right from the note to a small arrowhead immediately before (a).",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          207,
          395,
          270,
          433
        ]
      }
    },
    {
      "id": "H04",
      "location": "Upper note, after bar Sigma_i neq Sigma_i",
      "C": "no comma",
      "H": ", before i.e.",
      "reading": "no comma",
      "evidence": "The following i.e. begins directly after the indexed Sigma; no additional baseline comma appears in the intervening gap.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "04_upper_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          30,
          680,
          225,
          941
        ]
      }
    },
    {
      "id": "H05",
      "location": "Display (a), operator initial",
      "C": "Card",
      "H": "card",
      "reading": "Card",
      "evidence": "The first letter is a large open capital curve extending above the following lowercase letters.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "05_display_a.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          620,
          371,
          736,
          420
        ]
      }
    },
    {
      "id": "H06",
      "location": "Display (a), overwritten E",
      "C": "deleted Sigma then E_i",
      "H": "E_i",
      "reading": "deleted Sigma then E_i",
      "evidence": "Two oblique Sigma remnants are visible inside the upright-and-three-bar E.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "05_display_a.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          901,
          375,
          952,
          427
        ]
      }
    },
    {
      "id": "H07",
      "location": "Display (b), first overwritten E",
      "C": "deleted Sigma then E_j",
      "H": "E_j",
      "reading": "deleted Sigma then E_j",
      "evidence": "The two diagonals converge at the right inside the E; the long hooked j descends separately.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "07_b_Ej.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          815,
          455,
          896,
          535
        ]
      }
    },
    {
      "id": "H08",
      "location": "Upper right marginal NB",
      "C": "underlined NB",
      "H": "plain NB",
      "reading": "underlined NB",
      "evidence": "A separate straight rule runs beneath NB and above the first Sigma line.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "06_right_NB.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          1248,
          332,
          1320,
          383
        ]
      }
    },
    {
      "id": "H09",
      "location": "Main NB, opening word",
      "C": "Cette",
      "H": "cette",
      "reading": "Cette",
      "evidence": "The initial C is visibly taller than the following ette sequence.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          325,
          630,
          445,
          694
        ]
      }
    },
    {
      "id": "H10",
      "location": "Main NB, transition after automatiquement",
      "C": "automatiquement les",
      "H": "automatiquement ill si les",
      "reading": "automatiquement les",
      "evidence": "The terminal t reaches the right edge of its line; the next line begins les. No si group occurs before les in the visible gap. The H ill placeholder has no separate ink locus here.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          268,
          623,
          1681,
          810
        ]
      }
    },
    {
      "id": "H11",
      "location": "Main NB, first indexed E",
      "C": "deleted Sigma then E_i",
      "H": "E_i",
      "reading": "deleted Sigma then E_i",
      "evidence": "The angular interior strokes remain beneath the heavy E at the start of the second line.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          438,
          746,
          505,
          804
        ]
      }
    },
    {
      "id": "H12",
      "location": "Main NB, end of mutuellement",
      "C": "no stop",
      "H": "mutuellement.",
      "reading": "mutuellement without terminal stop",
      "evidence": "The word ends with its tall final t; the space after it contains no distinct full stop.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          982,
          768,
          1424,
          831
        ]
      }
    },
    {
      "id": "H13",
      "location": "Case heading operator",
      "C": "Card",
      "H": "card",
      "reading": "Card",
      "evidence": "The initial loop is capital-sized and separately precedes the small ard run.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "10_case.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          637,
          1027,
          750,
          1074
        ]
      }
    },
    {
      "id": "H14",
      "location": "First equivalence endpoint",
      "C": "à",
      "H": "à :",
      "reading": "à",
      "evidence": "The endpoint has a small baseline a-shaped arch and its raised accent, with no additional pair of colon points.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "12_equivaut.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          1354,
          1407,
          1410,
          1454
        ]
      }
    },
    {
      "id": "H15",
      "location": "Cancelled Si on avait",
      "C": "before comme",
      "H": "after cela équivaut",
      "reading": "cancelled Si on avait before comme",
      "evidence": "The crossed words occupy the left of the same physical line whose right part begins comme; aussi à is the next lower line.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          232,
          1578,
          1647,
          1740
        ]
      }
    },
    {
      "id": "H16",
      "location": "Second equivalence endpoint",
      "C": "aussi à",
      "H": "aussi à :",
      "reading": "aussi à",
      "evidence": "A low a arch with its raised accent ends the line; the following blank space carries no colon.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "14_aussi.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          223,
          1673,
          492,
          1755
        ]
      }
    },
    {
      "id": "H17",
      "location": "Symmetry phrase endpoint",
      "C": "à",
      "H": "à :",
      "reading": "à",
      "evidence": "After the comma, the tiny a and raised accent are the complete visible endpoint; no second punctuation group follows.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "15_symetriquement.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          872,
          1858,
          969,
          1919
        ]
      }
    },
    {
      "id": "H18",
      "location": "Raised cancelled vois. ouvert placement",
      "C": "before/above Sigma_2^- superset E_1",
      "H": "after inclusion",
      "reading": "above first Sigma_2^-",
      "evidence": "The cancelled words are physically above the first Sigma, ahead of the inclusion’s E_1.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "16_vois.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          409,
          2008,
          728,
          2144
        ]
      }
    },
    {
      "id": "H19",
      "location": "Added i.e. clause",
      "C": "inserted i.e. Sigma_2^- est un underlined vois. ouvert de E_1,",
      "H": "unmarked live i.e. clause before cancelled il contient les",
      "reading": "raised insertion over the cancelled il contient les clause",
      "evidence": "The i.e. line sits above the baseline cancellation, with its word vois. separately underlined.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          765,
          2019,
          1659,
          2137
        ]
      }
    },
    {
      "id": "H20",
      "location": "End of on a",
      "C": "on a",
      "H": "on a :",
      "reading": "on a",
      "evidence": "The low on stroke is followed by the small isolated a; no following colon pair is visible.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          1250,
          2065,
          1418,
          2111
        ]
      }
    },
    {
      "id": "H21",
      "location": "Bottom justification initial",
      "C": "Car",
      "H": "car",
      "reading": "Car",
      "evidence": "The open C rises substantially above ar at the start of the justification.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          704,
          2164,
          791,
          2231
        ]
      }
    },
    {
      "id": "H22",
      "location": "Bottom closure-intersection emphasis",
      "C": "underline overline Sigma_1^+ cap E_1",
      "H": "no underline",
      "reading": "underline overline Sigma_1^+ cap E_1",
      "evidence": "A long lower rule with short upturned ends runs under the expression through E_1, in addition to the separate upper closure bar.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          843,
          2137,
          1081,
          2250
        ]
      }
    },
    {
      "id": "H23",
      "location": "Inserted word before parenthetical Sigma_1^+ and commas",
      "C": "inserted l'ouvert before Sigma_1^+",
      "H": "Sigma_1^+, inserted ouvert,",
      "reading": "inserted l'ouvert|louvert before Sigma_1^+; no commas",
      "evidence": "The raised word begins with a tall looped l, then the ouvert run. Its small apostrophe is not separately secure. The curved guide starts in the gap before Sigma and extends above it; no comma strokes flank the insertion.",
      "confidence": "medium",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "18_louvert.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          1274,
          2097,
          1660,
          2270
        ]
      }
    },
    {
      "id": "H26",
      "location": "Lower marginal note after first inequality",
      "C": "i.e. bar Sigma_1^+ neq Sigma_1^+ à signaler|à sign.ler avant",
      "H": "ill placeholder",
      "reading": "i.e. bar Sigma_1^+ neq Sigma_1^+ à sign.ler|à signaler avant, with local curved guide",
      "evidence": "The rotated crop shows i.e., a second barred Sigma expression, the compressed instruction and the separate word avant. One H placeholder covers this whole continuation; local source doubt D16 is counted only against C.",
      "confidence": "medium",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "17_lower_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          16,
          1943,
          466,
          2339
        ]
      }
    },
    {
      "id": "G01",
      "location": "Opening insertion guide",
      "C": "insertion macro only",
      "H": "addition macro only",
      "reading": "curved guide under inserted fermés/fermées",
      "evidence": "A long curved line starts in the gap after parties, turns upward, runs right beneath the raised word and ends in an upturned hook. GUIDE01 draws this path.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "03_fermes.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          370,
          210,
          480,
          263
        ]
      },
      "source_component": "GUIDE01"
    },
    {
      "id": "G02",
      "location": "Case heading underline geometry",
      "C": "one continuous underline",
      "H": "emphasis of heading",
      "reading": "wavy long run followed by a separate short run under 2",
      "evidence": "The long rule stops before the 2; a clear blank gap separates its endpoint from the short rule under the numeral. RULE01 and RULE02 preserve the two runs.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "10_case.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          528,
          1067,
          931,
          1097
        ]
      },
      "source_component": "RULE01/RULE02"
    },
    {
      "id": "G03",
      "location": "Main oval boundary and left brace",
      "C": "single closed oval path; two left-brace paths",
      "H": "disk with two chords and one brace on each side",
      "reading": "oval with pale/broken right and left runs, checked two chords and retraced left brace",
      "evidence": "The upper-right rim has a small gap before the lower run; the lower-right rim has short gaps and pale stretches. The left rim has a short hooked return. Two long overlapping left-brace runs remain visible. DRAW01 preserves these local components.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "11_drawing.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          19,
          1038,
          572,
          1374
        ]
      },
      "source_component": "DRAW01 oval paths, chords, and three retained brace commands"
    },
    {
      "id": "G04",
      "location": "Crossed upper-left drawing label",
      "C": "generic deletion rule",
      "H": "omitted crossed label",
      "reading": "local cancellation diagonals and loop over qualified label",
      "evidence": "The cancellation includes a long rising diagonal and a returning upper loop, rather than only a single horizontal crossing. The deleted label text appears once via invisible boxing.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "11_drawing.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          153,
          1054,
          226,
          1125
        ]
      },
      "source_component": "DRAW01 cancellation paths",
      "H_omission_cross_reference": "D10"
    },
    {
      "id": "G05",
      "location": "Detached point above right drawing superscript",
      "C": "omitted",
      "H": "omitted",
      "reading": "qualified graphical short dot",
      "evidence": "A separate dark short upright/rounded mark stands above the rectangular superscript overdraw, with white space between. Its path is retained as MARK01; character, role, hand and surface origin remain unresolved.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "11_drawing.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          525,
          1189,
          531,
          1198
        ]
      },
      "source_component": "MARK01"
    },
    {
      "id": "G06",
      "location": "Paired cancellation of car si",
      "C": "one generic deletion line",
      "H": "omitted phrase",
      "reading": "two explicit cancellation runs",
      "evidence": "Two long independent horizontal/curved runs cross the short word group at different levels and extend to separate right endpoints.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "13_car_si.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          206,
          1437,
          438,
          1510
        ]
      },
      "source_component": "CANCEL01/CANCEL02",
      "H_omission_cross_reference": "D13",
      "physical_cluster": "car_si"
    },
    {
      "id": "G07",
      "location": "First cancelled inclusion beside équivaut",
      "C": "equivaut before both cancelled displays",
      "H": "first cancelled inclusion before équivaut",
      "reading": "first cancelled inclusion aligned left of équivaut à",
      "evidence": "The first crossed inclusion and équivaut occupy one baseline, the formula on the left; the second crossed inclusion occupies the next line with the live inclusion to its right.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          698,
          1391,
          1448,
          1558
        ]
      }
    },
    {
      "id": "G08",
      "location": "Accent in symmetry phrase",
      "C": "symétriquement",
      "H": "symétriquement",
      "reading": "symètriquement|symétriquement",
      "evidence": "The detached accent over the e position slopes downward to the right in the enlargement. At its small source size a pen-thickness reading of the acute remains possible; both are preserved.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "15_symetriquement.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          511,
          1866,
          536,
          1891
        ]
      }
    },
    {
      "id": "G09",
      "location": "Detached short curve below cancelled vois. ouvert",
      "C": "omitted",
      "H": "omitted",
      "reading": "qualified short ascending curved path",
      "evidence": "A dark short curved stroke sits in white space below the cancelled wording and above the first Sigma. It has neither a settled character nor a settled attachment. MARK02 reproduces it locally.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "16_vois.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          510,
          2062,
          529,
          2077
        ]
      },
      "source_component": "MARK02"
    },
    {
      "id": "G10",
      "location": "Curved stroke above lower Sigma_2^- display",
      "C": "omitted",
      "H": "covered by lower marginal omission",
      "reading": "qualified curved stroke with hooked left turn",
      "evidence": "A pale continuous curve rises from the left of the main Sigma to an extended right end under the slanted note. GUIDE02 preserves the visible curve; its attachment/function remains unresolved.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "17_lower_margin.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          183,
          2162,
          301,
          2223
        ]
      },
      "source_component": "GUIDE02",
      "H_omission_cross_reference": "H26"
    },
    {
      "id": "G11",
      "location": "Guide for inserted l’ouvert",
      "C": "insertion macro only",
      "H": "addition macro only",
      "reading": "long curved guide with right hook",
      "evidence": "The guide bends upward from the gap after sinon, then runs right over Sigma and ends in a short hook. GUIDE03 draws the whole observed path.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "18_louvert.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          1456,
          2147,
          1610,
          2201
        ]
      },
      "source_component": "GUIDE03"
    },
    {
      "id": "G12",
      "location": "Final cancelled group geometry",
      "C": "one generic deletion rule",
      "H": "one generic deletion rule",
      "reading": "oblique, angular and near-horizontal overstrikes",
      "evidence": "Above and across the qualified group there is a rising diagonal, a small angular up/down crossing, and a longer slanted crossing run. CANCEL03 reproduces those visible paths without a generic extra horizontal line.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "20_donc.png",
      "bbox": {
        "coordinate_system": "original full scan; origin upper left",
        "xyxy": [
          926,
          2241,
          1090,
          2303
        ]
      },
      "source_component": "CANCEL03",
      "physical_cluster": "final_cancelled"
    }
  ],
  "doubts": [
    {
      "location": "Heading, overwritten initial",
      "reading": "deleted I|V",
      "alternatives": [
        "V"
      ],
      "confidence": "low",
      "reason": "A tall interior upright and upper/lower transverse strokes survive inside the heavy V-shaped strokes. Their overlap does not settle the predecessor; H V survives as the second candidate.",
      "crop": "01_heading.png",
      "source_difference": "D01a",
      "C_source_doubt_row": 1
    },
    {
      "location": "Opening indexed family, predecessor under E",
      "reading": "deleted Sigma|S followed by E_i",
      "alternatives": [
        "S followed by E_i"
      ],
      "confidence": "medium",
      "reason": "Two curved oblique returns remain between the three E bars. The overdrawn middle prevents a decisive angular/rounded predecessor reading. H omits the surviving predecessor.",
      "crop": "02_family.png",
      "source_difference": "D02",
      "C_source_doubt_row": 2
    },
    {
      "location": "Upper slanted note, between pour and comp.",
      "reading": "tte|toute|tt",
      "alternatives": [
        "toute",
        "tt"
      ],
      "confidence": "low",
      "reason": "The small group has two tall connected strokes and a compressed low ending. The abbreviated primary survives; the enlargement does not separate the last e from the joins. H toute survives as an alternative.",
      "crop": "04_upper_margin.png",
      "source_difference": "D03",
      "C_source_doubt_row": 3
    },
    {
      "location": "Right NB, second superscript",
      "reading": "+|-|*",
      "alternatives": [
        "-",
        "*"
      ],
      "confidence": "low",
      "reason": "The compact dark overdraw has a horizontal arm and lower projecting stroke. The black overlap leaves +, - and star candidates open. H minus survives as an alternative.",
      "crop": "06_right_NB.png",
      "source_difference": "D05",
      "C_source_doubt_row": 5
    },
    {
      "location": "Case heading, old parenthetical under (I)",
      "reading": "deleted unsure (de)",
      "alternatives": [],
      "confidence": "low",
      "reason": "A small loop and adjoining e-like return survive under the large current I and parenthesis. The overlapping strokes do not isolate the complete old parenthetical.",
      "crop": "10_case.png",
      "source_difference": "D09a",
      "C_source_doubt_row": 9
    },
    {
      "location": "Case heading, overwritten relation",
      "reading": "deleted <=|= then =",
      "alternatives": [
        "= then ="
      ],
      "confidence": "low",
      "reason": "A short angular lower turn remains between and below the heavy horizontal bars. The earlier relation remains <= or =.",
      "crop": "10_case.png",
      "source_difference": "D09b",
      "C_source_doubt_row": 9
    },
    {
      "location": "Drawing, crossed upper-left label",
      "reading": "deleted Sigma_1^+|Sigma_2^+",
      "alternatives": [
        "Sigma_2^+"
      ],
      "confidence": "low",
      "reason": "The capital Sigma and raised cross remain readable; the lower-right digit is entangled with oblique cancellation strokes. No digit is selected from the nearby live labels.",
      "crop": "11_drawing.png",
      "source_difference": "D10",
      "C_source_doubt_row": 10
    },
    {
      "location": "Drawing, right brace superscript",
      "reading": "deleted unsure + followed by unsure -",
      "alternatives": [],
      "confidence": "low",
      "reason": "A compact rectangular dark overdraw contains intersecting horizontal and upright pieces with light openings. The predecessor and live sign remain qualified; H gives only the live minus.",
      "crop": "11_drawing.png",
      "source_difference": "D11",
      "C_source_doubt_row": 11
    },
    {
      "location": "Right of first cancelled inclusion",
      "reading": "équivaut|èquivaut",
      "alternatives": [
        "èquivaut"
      ],
      "confidence": "medium",
      "reason": "The initial e, q bowl and descending stem, compressed ui/v run and long final stroke support the word. The tiny detached accent does not confidently settle its direction. Crop 12 clips only the lowest q-tail endpoint; half b shows the full descender.",
      "crop": "12_equivaut.png",
      "source_difference": "D12",
      "C_source_doubt_row": 12
    },
    {
      "location": "Under drawing, cancelled short phrase",
      "reading": "deleted car si|Car si",
      "alternatives": [
        "Car si"
      ],
      "confidence": "low",
      "reason": "An open initial curve, low rounded run, final s-like stem and separate i dot survive between two cancellation lines. The initial case remains open.",
      "crop": "13_car_si.png",
      "source_difference": "D13",
      "C_source_doubt_row": 13
    },
    {
      "location": "Before symétriquement",
      "reading": "unsure et",
      "alternatives": [],
      "confidence": "low",
      "reason": "Only two pale separated strokes remain at the start of the line; they support the source candidate without resolving it.",
      "crop": "15_symetriquement.png",
      "source_difference": "D14",
      "C_source_doubt_row": 14
    },
    {
      "location": "Above bottom inclusion, cancelled words",
      "reading": "deleted unsure vois. ouvert",
      "alternatives": [],
      "confidence": "medium",
      "reason": "The v/o loops, dotted i, and open ou run ending in a tall t are visible through the cancellation. The abbreviation point is crowded against the crossing rule; the phrase retains its qualification.",
      "crop": "16_vois.png",
      "source_difference": "D15",
      "C_source_doubt_row": 15
    },
    {
      "location": "Lower slanted note, after second inequality",
      "reading": "à sign.ler|à signaler",
      "alternatives": [
        "à signaler"
      ],
      "confidence": "medium",
      "reason": "After sig/n there is a small detached low point before the tall l and final er. The point makes the abbreviated spelling the stronger visible candidate; a compressed a remains possible. The source row is retained with reversed candidate priority.",
      "crop": "17_lower_margin.png",
      "source_difference": "D16",
      "C_source_doubt_row": 16
    },
    {
      "location": "Bottom line, connector before deleted group",
      "reading": "donc|puis",
      "alternatives": [
        "puis"
      ],
      "confidence": "low",
      "reason": "The first loop has a long descending stroke; the following rounded middle and low humps do not securely separate all letters. Primary donc and alternative puis remain.",
      "crop": "20_donc.png",
      "source_difference": "D18",
      "C_source_doubt_row": 18
    },
    {
      "location": "Bottom, cancelled mathematical/prose group",
      "reading": "deleted Sigma_1^+ serait | Sigma_1^+ neq emptyset",
      "alternatives": [
        " Sigma_1^+ neq emptyset"
      ],
      "confidence": "low",
      "reason": "Sigma, lower 1 and raised + survive. The compressed following run and final tall loop remain crowded by oblique and near-horizontal overstrikes. H’s crossed formula survives as a supported alternative, not a conclusively rejected reading.",
      "crop": "20_donc.png",
      "source_difference": "D19",
      "C_source_doubt_row": 19
    },
    {
      "location": "Opening raised insertion",
      "reading": "inserted fermés|fermées",
      "alternatives": [
        "fermées"
      ],
      "confidence": "medium",
      "reason": "The insertion has a tall f, compressed erm run, separate accented vowel stroke and final s. A second e cannot be isolated securely. H’s fermées is retained as an alternative.",
      "crop": "03_fermes.png",
      "source_difference": "D20",
      "C_source_doubt_row": 20
    },
    {
      "location": "Upper slanted note, first Sigma index",
      "reading": "Sigma_i|Sigma",
      "alternatives": [
        "Sigma"
      ],
      "confidence": "low",
      "reason": "A small low dot lies to the right of the first Sigma, but an independent descending index shaft is not securely isolated. The full indexed and unindexed candidates are retained.",
      "crop": "04_upper_margin.png",
      "source_difference": "D21b",
      "C_source_doubt_row": 21
    },
    {
      "location": "Inserted word before parenthetical Sigma_1^+ and commas",
      "reading": "inserted l'ouvert|louvert before Sigma_1^+; no commas",
      "alternatives": [
        "louvert before Sigma_1^+; no commas"
      ],
      "confidence": "medium",
      "reason": "The raised word begins with a tall looped l, then the ouvert run. Its small apostrophe is not separately secure. The curved guide starts in the gap before Sigma and extends above it; no comma strokes flank the insertion.",
      "crop": "18_louvert.png",
      "source_difference": "H23",
      "C_source_doubt_row": null
    },
    {
      "location": "Detached point above right drawing superscript",
      "reading": "qualified graphical short dot",
      "alternatives": [],
      "confidence": "medium",
      "reason": "A separate dark short upright/rounded mark stands above the rectangular superscript overdraw, with white space between. Its path is retained as MARK01; character, role, hand and surface origin remain unresolved.",
      "crop": "11_drawing.png",
      "source_difference": "G05",
      "C_source_doubt_row": null
    },
    {
      "location": "Accent in symmetry phrase",
      "reading": "symètriquement|symétriquement",
      "alternatives": [
        "symétriquement"
      ],
      "confidence": "medium",
      "reason": "The detached accent over the e position slopes downward to the right in the enlargement. At its small source size a pen-thickness reading of the acute remains possible; both are preserved.",
      "crop": "15_symetriquement.png",
      "source_difference": "G08",
      "C_source_doubt_row": null
    },
    {
      "location": "Detached short curve below cancelled vois. ouvert",
      "reading": "qualified short ascending curved path",
      "alternatives": [],
      "confidence": "medium",
      "reason": "A dark short curved stroke sits in white space below the cancelled wording and above the first Sigma. It has neither a settled character nor a settled attachment. MARK02 reproduces it locally.",
      "crop": "16_vois.png",
      "source_difference": "G09",
      "C_source_doubt_row": null
    },
    {
      "location": "Curved stroke above lower Sigma_2^- display",
      "reading": "qualified curved stroke with hooked left turn",
      "alternatives": [],
      "confidence": "medium",
      "reason": "A pale continuous curve rises from the left of the main Sigma to an extended right end under the slanted note. GUIDE02 preserves the visible curve; its attachment/function remains unresolved.",
      "crop": "17_lower_margin.png",
      "source_difference": "G10",
      "C_source_doubt_row": null
    }
  ],
  "notes": {
    "page_content": "Handwritten Version I: a topological-space/family statement with conditions (a),(b), two marginal notes, a two-member case, an oval cut by two chords, equations (1),(2),(2′), cancellations and a bottom closure argument.",
    "author_own_uncertainty": "No independent explicit authorial question or uncertainty sentence was recovered on this sheet. Editorial candidate qualifications remain separate from the author’s readable wording.",
    "title_date_page_counts": "Live heading Version I; no date or manuscript page count. Archive numeral 14 is recorded only in a comment; its hand is undetermined.",
    "actual_workflow": "UTC clock read alongside the initial parallel text reads. Whole source viewed once for layout, half a once and half b once for full line reading, then 20 tight crops each created once and viewed once. The lower-half offset is 2360-1260=1100 pixels; all report bboxes use full-scan coordinates.",
    "mathematics_led_reading_decisions": "No mathematical computation or proof was performed. Bases, indices, bars, superscripts and inclusion directions were compared directly with ink; no expected implication selected a glyph.",
    "source_doubt_identity": "Exactly 21 actual source rows, with separate decisions for row1 predecessor/Version, row9 parenthetical/relation, and row21 abbreviation/first index. Notation and slips-retained rows were not counted as source doubts.",
    "C_source_row_map": {
      "1": [
        "D01a",
        "D01b"
      ],
      "2": [
        "D02"
      ],
      "3": [
        "D03"
      ],
      "4": [
        "D04"
      ],
      "5": [
        "D05"
      ],
      "6": [
        "D06"
      ],
      "7": [
        "D07"
      ],
      "8": [
        "D08"
      ],
      "9": [
        "D09a",
        "D09b"
      ],
      "10": [
        "D10"
      ],
      "11": [
        "D11"
      ],
      "12": [
        "D12"
      ],
      "13": [
        "D13"
      ],
      "14": [
        "D14"
      ],
      "15": [
        "D15"
      ],
      "16": [
        "D16"
      ],
      "17": [
        "D17"
      ],
      "18": [
        "D18"
      ],
      "19": [
        "D19"
      ],
      "20": [
        "D20"
      ],
      "21": [
        "D21a",
        "D21b"
      ]
    },
    "crop_boundary_limitations": [
      "12_equivaut.png clips the lowest q-tail endpoint; its complete descender was visible in half b.",
      "15_symetriquement.png clips lower endpoints of the long y/q descenders; these were visible in half b. The small upper-right stroke in 17_lower_margin.png belongs to neighbouring main-line writing near the crop boundary and is not supplied a second time."
    ],
    "graphics_maps": "GUIDE01 origin (190,169); RULE01/02 origin (500,994); DRAW01 origin (19,1038), C brace paths translated locally by (5,33); CANCEL01/02 origin (206,1437); MARK02 cluster origin (409,2008); GUIDE02 origin (180,2158); GUIDE03 origin (1274,2097); CANCEL03 origin (920,2238). All are fixed local rectangles with positive source y drawn downward. Approximate Bézier bounds differ from observed target bboxes; the literal paths are in reading.tex.",
    "H_apparatus": "H page14 identifies scan15. Its drawing description is apparatus; it was collated for the features it reports. H emphasis equals manuscript underlining only where the marked span agrees. Its ill placeholder in the lower marginal continuation is counted once (H26).",
    "validation": "Structural source checks only; no compiler, renderer, OCR, external search, installation or delegation."
  },
  "notation": [
    {
      "location": "Displays (a), (b), main NB",
      "sign": "Sigma overwritten by E",
      "latex": "\\deleted{\\Sigma}E_i; \\deleted{\\Sigma}E_j",
      "evidence": "E upright and three bars over surviving oblique diagonals; first occurrence retains Sigma/S doubt."
    },
    {
      "location": "(a) and case heading",
      "sign": "Capital Card",
      "latex": "\\operatorname{Card}",
      "evidence": "Capital open initial followed by lowercase ard."
    },
    {
      "location": "Right NB",
      "sign": "Complement glyph Sigma_i",
      "latex": "X\\setminus\\Sigma_i",
      "evidence": "Open-left zigzag with no E upright."
    },
    {
      "location": "Upper slanted margin",
      "sign": "conn.; i.e.",
      "latex": "conn.; i.e.",
      "evidence": "Low nn run and explicit punctuation; first Sigma index remains doubtful."
    },
    {
      "location": "All main inclusions",
      "sign": "Unbarred inclusion signs",
      "latex": "\\subset,\\supset",
      "evidence": "Curved inclusion sides; no lower equality bars."
    },
    {
      "location": "Lower formulas and margin",
      "sign": "Closure bars and separate emphasis rule",
      "latex": "\\overline{\\Sigma_1^+}; \\underline{\\overline{\\Sigma_1^+}\\cap E_1}",
      "evidence": "Short upper bars and distinct long lower underline recovered locally."
    },
    {
      "location": "Bottom display label",
      "sign": "Prime",
      "latex": "(2')",
      "evidence": "Separate raised short stroke after 2 within parentheses."
    },
    {
      "location": "Bottom insertion",
      "sign": "un",
      "latex": "\\inserted{un}",
      "evidence": "Two raised humps stop before the connected f stem."
    },
    {
      "location": "Lower note",
      "sign": "Compressed instruction",
      "latex": "\\unsure{à sign.ler|à signaler}",
      "evidence": "Detached low point before tall l; alternative retained."
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The two planned prose crops retained all deciding letter bodies but clipped long descender endpoints; these limits are disclosed, and the crops were not repeated.",
    "The candidate reading adds inline TikZ annotation clusters to retain guides without duplicating their prose; these are local graphical annotations with fixed source-coordinate maps."
  ]
}

--- A
+++ B
@@ -5,30 +5,33 @@
 \makeatother
 \uline{\deleted{\unsure{I|V}}Version I}
 
-% MARK01: observed full-scan bbox (191,141,195,145); local origin (191,141).
-\unsure{\begin{tikzpicture}[baseline=0pt,x=.013cm,y=-.013cm]
-\path[use as bounding box] (0,0) rectangle (74,8);
-\fill (0,0) .. controls (2,-1) and (4,2) .. (4,4) .. controls (2,5) and (0,3) .. cycle;
+% G01: detached short dot at full-scan (190,140)--(196,147); hand, role and surface origin undetermined.
+\reversemarginpar
+\margin{\unsure{$\cdot$}}
+\normalmarginpar
+Soient $X$ un espace topologique, $(\deleted{\unsure{\Sigma|S}}E_i)_{i\in I}$ un ens. de
+% Opening local group; coordinates are full scan minus (195,169).
+\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (363,116);
+\node[anchor=base west,inner sep=0] at (12,85) {parties};
+\node[anchor=base west,inner sep=0] at (134,34) {\inserted{\unsure{fermés|fermées}}};
+\node[anchor=base west,inner sep=0] at (202,83) {de $X$};
+% GUIDE01: the curved insertion guide, (379,256) to (477,215) on the full scan.
+\draw (184,87) .. controls (168,47) and (232,51) .. (249,54)
+ .. controls (269,55) and (280,50) .. (282,46);
 \end{tikzpicture}}
-Soient $X$ un espace topologique, $(\deleted{\unsure{\Sigma|S}}E_i)_{i\in I}$ un ens. de parties
-% GUIDE01: full-scan origin (372,177), approximate curve within (371,214,475,261).
-\begin{tikzpicture}[baseline=(opening.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (-48,0) rectangle (170,87);
-\node[anchor=base west,inner sep=0] at (-47,29) {\inserted{\unsure{fermés|fermées}}};
-\node[anchor=base west,inner sep=0] (opening) at (29,80) {de $X$};
-\draw (1,83) .. controls (-8,48) and (21,43) .. (47,46)
- .. controls (72,50) and (91,48) .. (102,39);
-\end{tikzpicture}
 (noté indiciellement), telles que l'on ait
 % slanted
 \reversemarginpar
-\margin{$\nearrow$ On suppose de plus que pour \unsure{tte|toute|tt} comp. conn. $\unsure{\Sigma_i|\Sigma}$ de $X\setminus E_i$, on ait $\overline{\Sigma}_i\cap E_i\ne\varnothing$ i.e. $\overline{\Sigma}_i\ne\Sigma_i$ i.e. $\Sigma_i$ non fermé dans $X$ (ce qui est le cas si $X$ est connexe)}
+\margin{$\nearrow$ On suppose de plus que pour \unsure{tte|toute|tt} comp. conn. $\Sigma_i$ de $X\setminus E_i$, on ait $\overline{\Sigma}_i\cap E_i\ne\varnothing$ i.e. $\overline{\Sigma}_i\ne\Sigma_i$ i.e. $\Sigma_i$ non fermé dans $X$ (ce qui est le cas si $X$ est connexe)}
 \normalmarginpar
 \[
  \forall i\in I,\quad \operatorname{Card}\pi_0(X\setminus\deleted{\Sigma}E_i)=2
  \tag*{(a)}
 \]
-\margin{\uline{NB} les comp. conn. $\Sigma_i^+,\Sigma_i^{\unsure{+|-|\ast}}$ de $X\setminus\Sigma_i$ sont ouvertes dans $X$}
+% G02: separate upper horizontal stroke over the first Sigma in this NB.
+% The overset rule preserves the stroke; its role remains undetermined.
+\margin{\uline{NB} les comp. conn. $\overset{\unsure{\rule{.8em}{.35pt}}}{\Sigma}_i^+,\Sigma_i^{\unsure{+|-|\ast}}$ de $X\setminus\Sigma_i$ sont ouvertes dans $X$}
 \[
  \begin{aligned}
  &\forall(i,j)\in I\times I,\ i\ne j,\quad \deleted{\Sigma}E_j\ \text{est contenu dans l'une}\\
@@ -41,26 +44,21 @@
 
 On se propose d'étudier le ``découpage'' de $X$ par la famille $(E_i)$.
 
-% RULE01: full-scan origin (501,996); long wavy underline and separate short run under 2.
-\begin{tikzpicture}[baseline=(case.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (443,117);
-\node[anchor=base west,inner sep=0] (case) at (13,70)
- {Cas $\operatorname{Card}\deleted{\unsure{(\mathrm{de})}}(I)\deleted{\unsure{\leq|=}}=2$};
-\draw (63,92) .. controls (98,82) and (124,103) .. (166,91)
- .. controls (202,81) and (216,99) .. (262,85)
- .. controls (286,74) and (309,88) .. (342,81)
- .. controls (360,77) and (374,80) .. (378,82);
-\draw (393,80) -- (426,80);
-\end{tikzpicture}
+% The heading underline has a separate short run beneath 2.
+\uline{Cas $\operatorname{Card}\deleted{\unsure{(\mathrm{de})}}(I)\deleted{\unsure{\leq|=}}=$}\ \uline{$2$}
 
 Soit $\Sigma_i^+$ la comp. conn. de $X\setminus E_i$ qui ne contient pas $E_j$ $(j\ne i)$, alors on a (si $I=\{1,2\}$)
-% Drawing coordinates retain C's local map: full-scan approximately (x+24,y+1069).
-% The lower-right contour is interrupted at observed bbox (394,1278,413,1308).
+% Drawing coordinate map: full-scan (x,y) = local (x+22,y+1069).
+% The pale lower-right rim is drawn in separate supported runs; its exact continuity remains uncertain.
 \figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
-\path[use as bounding box] (-10,-20) rectangle (535,300);
+\path[use as bounding box] (0,-40) rectangle (535,300);
 \draw (182,89) .. controls (226,-13) and (337,-39) .. (379,72)
- .. controls (405,143) and (409,181) .. (384,212);
-\draw (376,226) .. controls (359,258) and (333,277) .. (303,281)
+ .. controls (407,148) and (405,201) .. (388,217);
+\node[anchor=north west,inner sep=0] at (354,222) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (34,44);
+\draw[gray,line width=.28pt] (29,3) .. controls (24,17) and (15,29) .. (5,39);
+\end{tikzpicture}}};
+\draw (355,266) .. controls (341,275) and (321,280) .. (303,281)
  .. controls (217,298) and (139,247) .. (161,158)
  .. controls (157,176) and (155,135) .. (182,89);
 \draw[line width=.8pt] (181,89) .. controls (256,91) and (313,77) .. (382,86)
@@ -71,62 +69,45 @@
  .. controls (47,224) and (57,241) .. (39,252) .. controls (55,242) and (43,259) .. (49,282);
 \draw (428,86) .. controls (439,93) and (409,141) .. (434,149)
  .. controls (420,158) and (436,251) .. (417,254);
-% CANCEL01: glyph retained once; observed oblique crossing strokes replace a generic horizontal strike.
-\node at (166,20) {\rlap{$\unsure{\Sigma_1^+|\Sigma_2^+}$}\phantom{$\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}$}};
-\draw[line width=.65pt] (135,37) -- (185,-10);
-\draw[gray,line width=.45pt] (155,7) -- (177,-12) -- (170,9);
+\node[inner sep=0] at (166,20) {\rlap{$\unsure{\Sigma_1^+|\Sigma_2^+}$}\phantom{$\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}$}};
+% CANCEL01: the two diagonal crossing runs of the upper-left deleted label.
+\draw[line width=.7pt] (135,39) -- (187,-8);
+\draw[line width=.45pt] (141,32) .. controls (158,13) and (164,2) .. (177,-13);
 \node at (139,90) {$E_1$}; \node at (149,220) {$E_2$};
 \node at (429,32) {$\Sigma_1^+$};
 \node at (492,160) {$\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}$};
+% G03: detached dot above the crowded right-hand exponent; role and hand undetermined.
+\node[inner sep=0] at (507,125) {\unsure{$\cdot$}};
 \node at (14,111) {$\Sigma_2^-$}; \node at (115,278) {$\Sigma_2^+$};
-% MARK02: detached spot above the right label; full scan (528,1193,531,1197).
-\node[inner sep=0] at (505,126) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
-\path[use as bounding box] (0,0) rectangle (4,5);
-\fill (0,0) .. controls (3,0) and (4,3) .. (2,4) .. controls (0,4) and (0,1) .. cycle;
-\end{tikzpicture}}};
 \end{tikzpicture}}
 \[
  \Sigma_1^+\cap\Sigma_2^+=\varnothing
  \tag*{(1)}
 \]
-ce qui \deleted{résulte de}
+ce qui \deleted{résulte de} équivaut à
 \[
  \begin{aligned}
- &\begin{tikzpicture}[baseline=(inc.base),x=.013cm,y=-.013cm,line cap=round]
- \path[use as bounding box] (0,0) rectangle (329,79);
- \node[anchor=base west,inner sep=0] (inc) at (2,59)
- {\rlap{$\Sigma_1^-\supset\Sigma_2^+$}\phantom{$\deleted{\Sigma_1^-\supset\Sigma_2^+}$}};
- % CANCEL02: original full-scan origin (704,1388).
- \draw (2,54) .. controls (149,38) and (243,44) .. (325,37);
- % MARK03: two detached points above the relation, observed (859,1404,863,1411).
- \node[inner sep=0] at (157,19) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
- \path[use as bounding box] (0,0) rectangle (5,8);
- \fill (3,0) circle[radius=.8]; \fill (1,6) circle[radius=1];
- \end{tikzpicture}}};
- \end{tikzpicture}
- \qquad\text{équivaut à}\\
+ &\deleted{\Sigma_1^-\supset\Sigma_2^+}\\
  &\deleted{\Sigma_2^-\supset\Sigma_1^+}\qquad \Sigma_1^+\subset\Sigma_2^-\cup E_2,\quad\text{et}
  \end{aligned}
 \]
-% CANCEL03: two distinct strokes, full-scan origin (202,1435).
-\begin{tikzpicture}[baseline=(carsi.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (231,83);
-\node[anchor=base west,inner sep=0] (carsi) at (24,47)
- {\rlap{\unsure{car si|Car si}}\phantom{\deleted{\unsure{car si|Car si}}}};
-\draw (43,39) .. controls (99,41) and (160,34) .. (204,37) -- (207,40);
-\draw (44,45) .. controls (104,48) and (161,43) .. (183,46)
- .. controls (199,51) and (211,49) .. (220,49);
-\end{tikzpicture}
+% Local cancelled words, origin (211,1427); both horizontal crossing runs retained.
+\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (220,86);
+\node[anchor=base west,inner sep=0] at (15,57) {\rlap{\unsure{Car si|car si}}\phantom{\deleted{\unsure{Car si|car si}}}};
+\draw (37,48) .. controls (90,46) and (138,45) .. (182,47);
+\draw (45,54) .. controls (108,55) and (156,58) .. (201,58);
+\end{tikzpicture}}
 \deleted{Si on avait} comme $\Sigma_1^+\cap E_2=\varnothing$, cela équivaut aussi à
 \[
  \Sigma_1^+\subset\Sigma_2^-
  \tag*{(2)}
 \]
-% MARK04: independent right-side pair, full scan (1603,1778,1610,1786).
-\margin{\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
-\path[use as bounding box] (0,0) rectangle (9,10);
-\fill (6,1) .. controls (8,0) and (9,2) .. (6,4) .. controls (4,4) and (4,2) .. cycle;
-\fill (1,7) .. controls (3,6) and (5,7) .. (3,9) .. controls (1,9) and (0,8) .. cycle;
+% G04: two detached small marks at full-scan (1602,1779)--(1612,1791); hand and role undetermined.
+\margin{\unsure{\begin{tikzpicture}[x=.02cm,y=-.02cm]
+\path[use as bounding box] (0,0) rectangle (10,12);
+\fill (6,1) ellipse (1 and .7);
+\fill (1,8) ellipse (1 and .6);
 \end{tikzpicture}}}
 \unsure{et} symétriquement, à
 \[
@@ -134,64 +115,64 @@
  \tag*{$(2')$}
 \]
 
-Comme
-% MARK05: detached slant between the cancelled words and Sigma; source (510,2061,528,2076).
-$\overset{\begin{smallmatrix}\text{\deleted{vois. ouvert}}\\
-\text{\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
-\path[use as bounding box] (0,0) rectangle (19,17);
-\draw[line cap=round,line width=.7pt] (1,15) .. controls (8,6) and (12,3) .. (18,1);
-\end{tikzpicture}}}
-\end{smallmatrix}}{\Sigma_2^-}\supset E_1$,
-\deleted{il contient les} \inserted{i.e. $\Sigma_2^-$ est un \uline{vois}. ouvert de $E_1$,} on \unsure{a}
-% slanted; local note coordinates are full-scan coordinates minus (17,1962).
-% GUIDE02 and GUIDE03 are separate observed curved strokes, without a supplied mathematical role.
+% Lower correction group: full-scan (x,y) = local (x+219,y+2009).
+\figure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (1448,145);
+\node[anchor=base west,inner sep=0] at (19,122) {Comme};
+\node[anchor=base west,inner sep=0] at (207,43) {\rlap{\unsure{vois. ouvert}}\phantom{\deleted{\unsure{vois. ouvert}}}};
+\draw (209,37) .. controls (270,33) and (334,38) .. (410,36);
+\node[anchor=base west,inner sep=0] at (265,122) {$\Sigma_2^-\supset E_1,$};
+% G05: detached slant below the struck words, visible (510,2076)--(526,2063).
+\node[inner sep=0] at (299,61) {\unsure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (16,13);
+\draw (0,13) .. controls (5,6) and (10,1) .. (16,0);
+\end{tikzpicture}}};
+\node[anchor=base west,inner sep=0] at (556,97) {\rlap{il contient les}\phantom{\deleted{il contient les}}};
+\draw (557,91) .. controls (705,95) and (858,86) .. (997,82);
+\node[anchor=base west,inner sep=0] at (557,49) {\inserted{i.e. $\Sigma_2^-$ est un \uline{vois.} ouvert de $E_1$,}};
+\node[anchor=base west,inner sep=0] at (1048,93) {on a};
+\end{tikzpicture}}
+% slanted
 \reversemarginpar
-\margin{\figure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (445,383);
-\node[rotate=40,inner sep=0] at (114,154) {$\overline{\Sigma_1^+}\cap E_1\ne\varnothing$};
-\node[rotate=40,inner sep=0] at (264,56) {i.e.};
-\node[rotate=40,inner sep=0] at (95,260) {$\overline{\Sigma_1^+}\ne\Sigma_1^+$};
-\node[rotate=40,inner sep=0] at (331,85) {\unsure{à signaler|à sign.ler}};
-\node[rotate=40,inner sep=0] at (94,326) {avant};
-% Approximate paths: GUIDE02 observed near (233,2071)-(274,2131).
-\draw (257,110) .. controls (224,103) and (211,125) .. (217,144)
- .. controls (222,149) and (233,150) .. (237,168);
-\draw (237,168) -- (227,162) (237,168) -- (238,156);
-% GUIDE03 observed near (187,2149)-(300,2200).
-\draw (171,238) .. controls (155,210) and (204,200) .. (245,196)
- .. controls (265,193) and (276,193) .. (282,187);
+\margin{$\overline{\Sigma_1^+}\cap E_1\ne\varnothing$ i.e. $\overline{\Sigma_1^+}\ne\Sigma_1^+$ \unsure{à signaler|à sign.ler} avant
+% G06: curved detached guide; full-scan origin (180,2145), role of the curve undetermined.
+\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (124,78);
+\node[inner sep=0] at (62,39) {\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (124,78);
+\draw (9,69) .. controls (-1,38) and (49,35) .. (75,23)
+ .. controls (102,16) and (119,12) .. (119,6);
+\end{tikzpicture}}};
 \end{tikzpicture}}}
 \normalmarginpar
 \[
  \Sigma_2^-\cap\Sigma_1^+\ne\varnothing
 \]
-Car
-% RULE02: hooked short underline, observed full bbox (896,2226,1038,2245).
-\begin{tikzpicture}[baseline=(carformula.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,-54) rectangle (222,30);
-\node[anchor=base west,inner sep=0] (carformula) at (0,0) {$\overline{\Sigma_1^+}\cap E_1$};
-\draw (44,15) -- (42,22) .. controls (75,23) and (119,14) .. (165,17)
- .. controls (175,18) and (181,17) .. (183,14) -- (179,10);
-\end{tikzpicture}
-$\ne\varnothing$ (sinon
-% GUIDE04: full-scan origin (1455,2104), original guide around (1460,2151)-(1604,2200).
-\begin{tikzpicture}[baseline=(sigmaopen.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (170,127);
-\node[anchor=base west,inner sep=0] at (-10,40) {\inserted{l'ouvert}};
-\node[anchor=base west,inner sep=0] (sigmaopen) at (35,105) {$\Sigma_1^+$};
-\draw (6,95) .. controls (15,64) and (35,52) .. (63,52)
- .. controls (91,56) and (117,54) .. (147,47);
-\draw (147,47) -- (143,43) (147,47) -- (147,40);
-\end{tikzpicture}
-serait \inserted{un} fermé dans $X$, \unsure{donc|puis}
-% CANCEL04: same recovered group as C, with explicit oblique crossings over the initial symbol.
-\begin{tikzpicture}[baseline=(lastcancel.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,-26) rectangle (160,50);
-\node[anchor=base west,inner sep=0] (lastcancel) at (8,20)
- {\rlap{$\unsure{\Sigma_1^+\text{ serait}}$}\phantom{$\deleted{\unsure{\Sigma_1^+\text{ serait}}}$}};
-\draw (10,12) -- (47,-10); \draw (25,22) -- (66,-5);
-\draw (39,21) .. controls (84,20) and (126,14) .. (156,18);
-\end{tikzpicture}
+Car $\underline{\overline{\Sigma_1^+}\cap E_1}\ne\varnothing$
+% Final local insertion: coordinates are full scan minus (1278,2080).
+\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (362,164);
+\node[anchor=base west,inner sep=0] at (19,127) {(sinon};
+\node[anchor=base west,inner sep=0] at (170,62) {\inserted{l'ouvert}};
+\node[anchor=base west,inner sep=0] at (213,131) {$\Sigma_1^+$};
+% GUIDE02: bent attachment guide from before Sigma to the right of the inserted word.
+\draw (183,117) .. controls (207,63) and (230,75) .. (262,78)
+ .. controls (285,81) and (311,79) .. (326,74) -- (326,70) -- (322,70);
+\end{tikzpicture}}
+serait \inserted{\unsure{un|une}} fermé dans $X$, donc
+% Final deleted group: origin (928,2238). The detached upper remnants have no assigned character.
+\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (165,67);
+\node[anchor=base west,inner sep=0] at (21,49) {\rlap{\unsure{$\Sigma_1^+$ serait}}\phantom{\deleted{\unsure{$\Sigma_1^+$ serait}}}};
+\draw (11,28) -- (51,5);
+\draw (20,35) -- (70,13);
+% G07: upper remnant cluster, shape retained locally under doubt; hand, role and surface origin undetermined.
+\node[inner sep=0] at (28,14) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (37,24);
+\draw (3,18) .. controls (11,8) and (8,7) .. (10,3) -- (15,18) -- (33,9);
+\draw (24,6) -- (26,16);
+\end{tikzpicture}}};
+\end{tikzpicture}}
 $X$ serait disconnexe),
 \endgroup
 % archive sheet number: 14

--- A
+++ C
@@ -5,21 +5,15 @@
 \makeatother
 \uline{\deleted{\unsure{I|V}}Version I}
 
-% MARK01: observed full-scan bbox (191,141,195,145); local origin (191,141).
-\unsure{\begin{tikzpicture}[baseline=0pt,x=.013cm,y=-.013cm]
-\path[use as bounding box] (0,0) rectangle (74,8);
-\fill (0,0) .. controls (2,-1) and (4,2) .. (4,4) .. controls (2,5) and (0,3) .. cycle;
-\end{tikzpicture}}
-Soient $X$ un espace topologique, $(\deleted{\unsure{\Sigma|S}}E_i)_{i\in I}$ un ens. de parties
-% GUIDE01: full-scan origin (372,177), approximate curve within (371,214,475,261).
-\begin{tikzpicture}[baseline=(opening.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (-48,0) rectangle (170,87);
-\node[anchor=base west,inner sep=0] at (-47,29) {\inserted{\unsure{fermés|fermées}}};
-\node[anchor=base west,inner sep=0] (opening) at (29,80) {de $X$};
-\draw (1,83) .. controls (-8,48) and (21,43) .. (47,46)
- .. controls (72,50) and (91,48) .. (102,39);
-\end{tikzpicture}
-(noté indiciellement), telles que l'on ait
+Soient $X$ un espace topologique, $(\deleted{\unsure{\Sigma|S}}E_i)_{i\in I}$ un ens. de % GUIDE01: full-scan origin (190,169), local coordinates in source pixels.
+\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(p.base),line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (385,113);
+\node[anchor=base west,inner sep=0pt] (p) at (19,89) {parties};
+\node[anchor=base west,inner sep=0pt] at (210,89) {de $X$};
+\node[anchor=base west,inner sep=0pt] at (136,38) {\inserted{\unsure{fermés|fermées}}};
+\draw (185,87) .. controls (180,63) and (188,54) .. (214,52)
+ .. controls (240,47) and (265,61) .. (286,44);
+\end{tikzpicture} (noté indiciellement), telles que l'on ait
 % slanted
 \reversemarginpar
 \margin{$\nearrow$ On suppose de plus que pour \unsure{tte|toute|tt} comp. conn. $\unsure{\Sigma_i|\Sigma}$ de $X\setminus E_i$, on ait $\overline{\Sigma}_i\cap E_i\ne\varnothing$ i.e. $\overline{\Sigma}_i\ne\Sigma_i$ i.e. $\Sigma_i$ non fermé dans $X$ (ce qui est le cas si $X$ est connexe)}
@@ -41,50 +35,67 @@
 
 On se propose d'étudier le ``découpage'' de $X$ par la famille $(E_i)$.
 
-% RULE01: full-scan origin (501,996); long wavy underline and separate short run under 2.
-\begin{tikzpicture}[baseline=(case.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (443,117);
-\node[anchor=base west,inner sep=0] (case) at (13,70)
- {Cas $\operatorname{Card}\deleted{\unsure{(\mathrm{de})}}(I)\deleted{\unsure{\leq|=}}=2$};
-\draw (63,92) .. controls (98,82) and (124,103) .. (166,91)
- .. controls (202,81) and (216,99) .. (262,85)
- .. controls (286,74) and (309,88) .. (342,81)
- .. controls (360,77) and (374,80) .. (378,82);
-\draw (393,80) -- (426,80);
-\end{tikzpicture}
+% RULE01/RULE02: full-scan origin (500,994); the underline has two visible runs.
+\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (458,106);
+\node[anchor=base west,inner sep=0pt] at (15,75) {Cas};
+\node[anchor=base west,inner sep=0pt] at (142,75) {$\operatorname{Card}$};
+\node[anchor=base west,inner sep=0pt] at (252,66) {$\deleted{\unsure{(\mathrm{de})}}(I)$};
+\node[anchor=base west,inner sep=0pt] at (331,66) {$\deleted{\unsure{\leq|=}}=$};
+\node[anchor=base west,inner sep=0pt] at (395,66) {$2$};
+\draw (31,94) .. controls (80,80) and (111,104) .. (169,87)
+ .. controls (206,75) and (218,94) .. (259,82)
+ .. controls (300,72) and (312,91) .. (353,80)
+ .. controls (364,79) and (375,77) .. (378,82);
+\draw (395,80) -- (428,80);
+\end{tikzpicture}}
 
 Soit $\Sigma_i^+$ la comp. conn. de $X\setminus E_i$ qui ne contient pas $E_j$ $(j\ne i)$, alors on a (si $I=\{1,2\}$)
-% Drawing coordinates retain C's local map: full-scan approximately (x+24,y+1069).
-% The lower-right contour is interrupted at observed bbox (394,1278,413,1308).
+% DRAW01: full-scan origin (19,1038), fixed local source-pixel rectangle.
+% C's two left-brace paths and right-brace path are retained after checking,
+% with local translation (5,33), i.e. full-scan origin (24,1071) for those paths.
 \figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
-\path[use as bounding box] (-10,-20) rectangle (535,300);
-\draw (182,89) .. controls (226,-13) and (337,-39) .. (379,72)
- .. controls (405,143) and (409,181) .. (384,212);
-\draw (376,226) .. controls (359,258) and (333,277) .. (303,281)
- .. controls (217,298) and (139,247) .. (161,158)
- .. controls (157,176) and (155,135) .. (182,89);
-\draw[line width=.8pt] (181,89) .. controls (256,91) and (313,77) .. (382,86)
- (174,218) .. controls (240,224) and (317,212) .. (380,212);
+\path[use as bounding box] (0,0) rectangle (553,336);
+% Oval: visible strong runs, pale runs and short gaps are distinct paths.
+\draw (186,122) .. controls (210,76) and (262,35) .. (290,38)
+ .. controls (342,35) and (380,88) .. (402,160);
+\draw (403,168) .. controls (405,185) and (403,206) .. (401,216);
+\draw[black!45] (401,217) .. controls (401,226) and (398,235) .. (394,243);
+\draw (391,249) .. controls (387,257) and (382,263) .. (378,267);
+\draw (374,273) .. controls (369,282) and (365,287) .. (361,291);
+\draw (358,295) .. controls (334,319) and (294,320) .. (269,315)
+ .. controls (219,309) and (178,276) .. (169,220)
+ .. controls (166,206) and (168,197) .. (168,193);
+\draw (168,193) .. controls (163,196) and (163,190) .. (166,181);
+\draw (168,193) -- (173,185);
+\draw[black!45] (168,179) .. controls (174,160) and (179,139) .. (186,122);
+% Chords, separately checked at both rim contacts.
+\draw[line width=.8pt] (186,122) .. controls (247,125) and (324,109) .. (392,119)
+ (176,250) .. controls (242,253) and (328,246) .. (391,239);
+\begin{scope}[shift={(5,33)}]
 \draw (44,9) .. controls (46,57) and (63,106) .. (32,108)
  .. controls (52,132) and (38,151) .. (46,195) -- (55,228);
 \draw (41,109) .. controls (72,143) and (35,144) .. (48,193)
  .. controls (47,224) and (57,241) .. (39,252) .. controls (55,242) and (43,259) .. (49,282);
 \draw (428,86) .. controls (439,93) and (409,141) .. (434,149)
  .. controls (420,158) and (436,251) .. (417,254);
-% CANCEL01: glyph retained once; observed oblique crossing strokes replace a generic horizontal strike.
-\node at (166,20) {\rlap{$\unsure{\Sigma_1^+|\Sigma_2^+}$}\phantom{$\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}$}};
-\draw[line width=.65pt] (135,37) -- (185,-10);
-\draw[gray,line width=.45pt] (155,7) -- (177,-12) -- (170,9);
-\node at (139,90) {$E_1$}; \node at (149,220) {$E_2$};
-\node at (429,32) {$\Sigma_1^+$};
-\node at (492,160) {$\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}$};
-\node at (14,111) {$\Sigma_2^-$}; \node at (115,278) {$\Sigma_2^+$};
-% MARK02: detached spot above the right label; full scan (528,1193,531,1197).
-\node[inner sep=0] at (505,126) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
-\path[use as bounding box] (0,0) rectangle (4,5);
-\fill (0,0) .. controls (3,0) and (4,3) .. (2,4) .. controls (0,4) and (0,1) .. cycle;
+\end{scope}
+% Cancelled label: one visible text copy, actual crossing paths, invisible deletion annotation.
+\node[inner sep=0pt] at (167,48) {\rlap{$\unsure{\Sigma_1^+|\Sigma_2^+}$}\phantom{$\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}$}};
+\draw (138,60) -- (198,27);
+\draw (151,42) .. controls (161,20) and (181,12) .. (177,24) -- (149,52);
+\node at (139,116) {$E_1$}; \node at (150,247) {$E_2$};
+\node at (430,68) {$\Sigma_1^+$};
+\node at (501,193) {$\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}$};
+\node at (23,135) {$\Sigma_2^-$}; \node at (131,308) {$\Sigma_2^+$};
+% MARK01: detached short dot above the right overwritten superscript;
+% full-scan observed bbox approximately (525,1189,531,1198), role/hand unresolved.
+\node[inner sep=0pt] at (509,156) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
+\path[use as bounding box] (0,0) rectangle (4,6);
+\fill (1,0) .. controls (4,1) and (4,4) .. (2,6) .. controls (0,5) and (0,2) .. (1,0);
 \end{tikzpicture}}};
 \end{tikzpicture}}
+
 \[
  \Sigma_1^+\cap\Sigma_2^+=\varnothing
  \tag*{(1)}
@@ -92,106 +103,71 @@
 ce qui \deleted{résulte de}
 \[
  \begin{aligned}
- &\begin{tikzpicture}[baseline=(inc.base),x=.013cm,y=-.013cm,line cap=round]
- \path[use as bounding box] (0,0) rectangle (329,79);
- \node[anchor=base west,inner sep=0] (inc) at (2,59)
- {\rlap{$\Sigma_1^-\supset\Sigma_2^+$}\phantom{$\deleted{\Sigma_1^-\supset\Sigma_2^+}$}};
- % CANCEL02: original full-scan origin (704,1388).
- \draw (2,54) .. controls (149,38) and (243,44) .. (325,37);
- % MARK03: two detached points above the relation, observed (859,1404,863,1411).
- \node[inner sep=0] at (157,19) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
- \path[use as bounding box] (0,0) rectangle (5,8);
- \fill (3,0) circle[radius=.8]; \fill (1,6) circle[radius=1];
- \end{tikzpicture}}};
- \end{tikzpicture}
- \qquad\text{équivaut à}\\
+ &\deleted{\Sigma_1^-\supset\Sigma_2^+}\qquad\text{\unsure{équivaut|èquivaut} à}\\
  &\deleted{\Sigma_2^-\supset\Sigma_1^+}\qquad \Sigma_1^+\subset\Sigma_2^-\cup E_2,\quad\text{et}
  \end{aligned}
 \]
-% CANCEL03: two distinct strokes, full-scan origin (202,1435).
-\begin{tikzpicture}[baseline=(carsi.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (231,83);
-\node[anchor=base west,inner sep=0] (carsi) at (24,47)
- {\rlap{\unsure{car si|Car si}}\phantom{\deleted{\unsure{car si|Car si}}}};
-\draw (43,39) .. controls (99,41) and (160,34) .. (204,37) -- (207,40);
-\draw (44,45) .. controls (104,48) and (161,43) .. (183,46)
- .. controls (199,51) and (211,49) .. (220,49);
-\end{tikzpicture}
+% CANCEL01/CANCEL02: full-scan origin (206,1437); two cancellation runs.
+\figure{\begin{tikzpicture}[x=.018cm,y=-.018cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (232,73);
+\node[anchor=base west,inner sep=0pt] at (16,47) {\rlap{\unsure{car si|Car si}}\phantom{\deleted{\unsure{car si|Car si}}}};
+\draw (42,37) .. controls (100,40) and (155,34) .. (201,37);
+\draw (43,47) .. controls (95,47) and (153,53) .. (215,47);
+\end{tikzpicture}}
 \deleted{Si on avait} comme $\Sigma_1^+\cap E_2=\varnothing$, cela équivaut aussi à
 \[
  \Sigma_1^+\subset\Sigma_2^-
  \tag*{(2)}
 \]
-% MARK04: independent right-side pair, full scan (1603,1778,1610,1786).
-\margin{\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
-\path[use as bounding box] (0,0) rectangle (9,10);
-\fill (6,1) .. controls (8,0) and (9,2) .. (6,4) .. controls (4,4) and (4,2) .. cycle;
-\fill (1,7) .. controls (3,6) and (5,7) .. (3,9) .. controls (1,9) and (0,8) .. cycle;
-\end{tikzpicture}}}
-\unsure{et} symétriquement, à
+\unsure{et} \unsure{symètriquement|symétriquement}, à
 \[
  \Sigma_2^+\subset\Sigma_1^-
  \tag*{$(2')$}
 \]
 
 Comme
-% MARK05: detached slant between the cancelled words and Sigma; source (510,2061,528,2076).
-$\overset{\begin{smallmatrix}\text{\deleted{vois. ouvert}}\\
-\text{\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
-\path[use as bounding box] (0,0) rectangle (19,17);
-\draw[line cap=round,line width=.7pt] (1,15) .. controls (8,6) and (12,3) .. (18,1);
-\end{tikzpicture}}}
-\end{smallmatrix}}{\Sigma_2^-}\supset E_1$,
-\deleted{il contient les} \inserted{i.e. $\Sigma_2^-$ est un \uline{vois}. ouvert de $E_1$,} on \unsure{a}
-% slanted; local note coordinates are full-scan coordinates minus (17,1962).
-% GUIDE02 and GUIDE03 are separate observed curved strokes, without a supplied mathematical role.
+% MARK02 and raised cancelled words: full-scan origin (409,2008).
+\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(inc.base),line cap=round]
+\path[use as bounding box] (0,0) rectangle (319,136);
+\node[anchor=base west,inner sep=0pt] at (16,42) {\deleted{\unsure{vois. ouvert}}};
+\node[anchor=base west,inner sep=0pt] (inc) at (75,113) {$\Sigma_2^-\supset E_1$,};
+\node[inner sep=0pt] at (111,61) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (19,16);
+\draw[line width=.6pt] (1,15) .. controls (8,7) and (13,3) .. (18,2);
+\end{tikzpicture}}};
+\end{tikzpicture} \deleted{il contient les} \inserted{i.e. $\Sigma_2^-$ est un \uline{vois.} ouvert de $E_1$,} on a
+% slanted
 \reversemarginpar
-\margin{\figure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (445,383);
-\node[rotate=40,inner sep=0] at (114,154) {$\overline{\Sigma_1^+}\cap E_1\ne\varnothing$};
-\node[rotate=40,inner sep=0] at (264,56) {i.e.};
-\node[rotate=40,inner sep=0] at (95,260) {$\overline{\Sigma_1^+}\ne\Sigma_1^+$};
-\node[rotate=40,inner sep=0] at (331,85) {\unsure{à signaler|à sign.ler}};
-\node[rotate=40,inner sep=0] at (94,326) {avant};
-% Approximate paths: GUIDE02 observed near (233,2071)-(274,2131).
-\draw (257,110) .. controls (224,103) and (211,125) .. (217,144)
- .. controls (222,149) and (233,150) .. (237,168);
-\draw (237,168) -- (227,162) (237,168) -- (238,156);
-% GUIDE03 observed near (187,2149)-(300,2200).
-\draw (171,238) .. controls (155,210) and (204,200) .. (245,196)
- .. controls (265,193) and (276,193) .. (282,187);
-\end{tikzpicture}}}
+\margin{$\overline{\Sigma_1^+}\cap E_1\ne\varnothing$ i.e. $\overline{\Sigma_1^+}\ne\Sigma_1^+$ \unsure{à sign.ler|à signaler} avant}
 \normalmarginpar
+% GUIDE02: observed curved stroke above the first Sigma of the next display.
+% Fixed full-scan origin (180,2158); no character or mathematical role assigned.
+\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (125,67);
+\node[inner sep=0pt] at (62,33) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (125,67);
+\draw[black!65] (7,59) .. controls (0,34) and (22,28) .. (60,21)
+ .. controls (87,18) and (105,13) .. (118,7);
+\end{tikzpicture}}};
+\end{tikzpicture}}
 \[
  \Sigma_2^-\cap\Sigma_1^+\ne\varnothing
 \]
-Car
-% RULE02: hooked short underline, observed full bbox (896,2226,1038,2245).
-\begin{tikzpicture}[baseline=(carformula.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,-54) rectangle (222,30);
-\node[anchor=base west,inner sep=0] (carformula) at (0,0) {$\overline{\Sigma_1^+}\cap E_1$};
-\draw (44,15) -- (42,22) .. controls (75,23) and (119,14) .. (165,17)
- .. controls (175,18) and (181,17) .. (183,14) -- (179,10);
-\end{tikzpicture}
-$\ne\varnothing$ (sinon
-% GUIDE04: full-scan origin (1455,2104), original guide around (1460,2151)-(1604,2200).
-\begin{tikzpicture}[baseline=(sigmaopen.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (170,127);
-\node[anchor=base west,inner sep=0] at (-10,40) {\inserted{l'ouvert}};
-\node[anchor=base west,inner sep=0] (sigmaopen) at (35,105) {$\Sigma_1^+$};
-\draw (6,95) .. controls (15,64) and (35,52) .. (63,52)
- .. controls (91,56) and (117,54) .. (147,47);
-\draw (147,47) -- (143,43) (147,47) -- (147,40);
-\end{tikzpicture}
-serait \inserted{un} fermé dans $X$, \unsure{donc|puis}
-% CANCEL04: same recovered group as C, with explicit oblique crossings over the initial symbol.
-\begin{tikzpicture}[baseline=(lastcancel.base),x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,-26) rectangle (160,50);
-\node[anchor=base west,inner sep=0] (lastcancel) at (8,20)
- {\rlap{$\unsure{\Sigma_1^+\text{ serait}}$}\phantom{$\deleted{\unsure{\Sigma_1^+\text{ serait}}}$}};
-\draw (10,12) -- (47,-10); \draw (25,22) -- (66,-5);
-\draw (39,21) .. controls (84,20) and (126,14) .. (156,18);
-\end{tikzpicture}
-$X$ serait disconnexe),
+Car $\underline{\overline{\Sigma_1^+}\cap E_1}\ne\varnothing$ % GUIDE03: full-scan origin (1274,2097); hooked insertion guide retained.
+\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(sin.base),line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (386,173);
+\node[anchor=base west,inner sep=0pt] (sin) at (20,102) {(sinon};
+\node[anchor=base west,inner sep=0pt] at (220,102) {$\Sigma_1^+$};
+\node[anchor=base west,inner sep=0pt] at (171,49) {\inserted{\unsure{l'ouvert|louvert}}};
+\draw (188,100) .. controls (202,61) and (226,56) .. (258,60)
+ .. controls (292,63) and (317,61) .. (331,55) -- (329,51);
+\end{tikzpicture} serait \inserted{un} fermé dans $X$, \unsure{donc|puis} % CANCEL03: full-scan origin (920,2238), one text copy and visible overstrikes.
+\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(del.base),line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (177,67);
+\node[anchor=base west,inner sep=0pt] (del) at (16,49) {\rlap{$\unsure{\Sigma_1^+\text{ serait}|\Sigma_1^+\ne\varnothing}$}\phantom{$\deleted{\unsure{\Sigma_1^+\text{ serait}|\Sigma_1^+\ne\varnothing}}$}};
+\draw (14,31) -- (53,9);
+\draw (8,25) -- (18,5) -- (24,29) -- (39,23);
+\draw (24,32) .. controls (60,23) and (105,29) .. (164,39);
+\end{tikzpicture} $X$ serait disconnexe),
 \endgroup
 % archive sheet number: 14

--- B
+++ C
@@ -5,33 +5,24 @@
 \makeatother
 \uline{\deleted{\unsure{I|V}}Version I}
 
-% G01: detached short dot at full-scan (190,140)--(196,147); hand, role and surface origin undetermined.
-\reversemarginpar
-\margin{\unsure{$\cdot$}}
-\normalmarginpar
-Soient $X$ un espace topologique, $(\deleted{\unsure{\Sigma|S}}E_i)_{i\in I}$ un ens. de
-% Opening local group; coordinates are full scan minus (195,169).
-\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
-\path[use as bounding box] (0,0) rectangle (363,116);
-\node[anchor=base west,inner sep=0] at (12,85) {parties};
-\node[anchor=base west,inner sep=0] at (134,34) {\inserted{\unsure{fermés|fermées}}};
-\node[anchor=base west,inner sep=0] at (202,83) {de $X$};
-% GUIDE01: the curved insertion guide, (379,256) to (477,215) on the full scan.
-\draw (184,87) .. controls (168,47) and (232,51) .. (249,54)
- .. controls (269,55) and (280,50) .. (282,46);
-\end{tikzpicture}}
-(noté indiciellement), telles que l'on ait
+Soient $X$ un espace topologique, $(\deleted{\unsure{\Sigma|S}}E_i)_{i\in I}$ un ens. de % GUIDE01: full-scan origin (190,169), local coordinates in source pixels.
+\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(p.base),line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (385,113);
+\node[anchor=base west,inner sep=0pt] (p) at (19,89) {parties};
+\node[anchor=base west,inner sep=0pt] at (210,89) {de $X$};
+\node[anchor=base west,inner sep=0pt] at (136,38) {\inserted{\unsure{fermés|fermées}}};
+\draw (185,87) .. controls (180,63) and (188,54) .. (214,52)
+ .. controls (240,47) and (265,61) .. (286,44);
+\end{tikzpicture} (noté indiciellement), telles que l'on ait
 % slanted
 \reversemarginpar
-\margin{$\nearrow$ On suppose de plus que pour \unsure{tte|toute|tt} comp. conn. $\Sigma_i$ de $X\setminus E_i$, on ait $\overline{\Sigma}_i\cap E_i\ne\varnothing$ i.e. $\overline{\Sigma}_i\ne\Sigma_i$ i.e. $\Sigma_i$ non fermé dans $X$ (ce qui est le cas si $X$ est connexe)}
+\margin{$\nearrow$ On suppose de plus que pour \unsure{tte|toute|tt} comp. conn. $\unsure{\Sigma_i|\Sigma}$ de $X\setminus E_i$, on ait $\overline{\Sigma}_i\cap E_i\ne\varnothing$ i.e. $\overline{\Sigma}_i\ne\Sigma_i$ i.e. $\Sigma_i$ non fermé dans $X$ (ce qui est le cas si $X$ est connexe)}
 \normalmarginpar
 \[
  \forall i\in I,\quad \operatorname{Card}\pi_0(X\setminus\deleted{\Sigma}E_i)=2
  \tag*{(a)}
 \]
-% G02: separate upper horizontal stroke over the first Sigma in this NB.
-% The overset rule preserves the stroke; its role remains undetermined.
-\margin{\uline{NB} les comp. conn. $\overset{\unsure{\rule{.8em}{.35pt}}}{\Sigma}_i^+,\Sigma_i^{\unsure{+|-|\ast}}$ de $X\setminus\Sigma_i$ sont ouvertes dans $X$}
+\margin{\uline{NB} les comp. conn. $\Sigma_i^+,\Sigma_i^{\unsure{+|-|\ast}}$ de $X\setminus\Sigma_i$ sont ouvertes dans $X$}
 \[
  \begin{aligned}
  &\forall(i,j)\in I\times I,\ i\ne j,\quad \deleted{\Sigma}E_j\ \text{est contenu dans l'une}\\
@@ -44,135 +35,139 @@
 
 On se propose d'étudier le ``découpage'' de $X$ par la famille $(E_i)$.
 
-% The heading underline has a separate short run beneath 2.
-\uline{Cas $\operatorname{Card}\deleted{\unsure{(\mathrm{de})}}(I)\deleted{\unsure{\leq|=}}=$}\ \uline{$2$}
+% RULE01/RULE02: full-scan origin (500,994); the underline has two visible runs.
+\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (458,106);
+\node[anchor=base west,inner sep=0pt] at (15,75) {Cas};
+\node[anchor=base west,inner sep=0pt] at (142,75) {$\operatorname{Card}$};
+\node[anchor=base west,inner sep=0pt] at (252,66) {$\deleted{\unsure{(\mathrm{de})}}(I)$};
+\node[anchor=base west,inner sep=0pt] at (331,66) {$\deleted{\unsure{\leq|=}}=$};
+\node[anchor=base west,inner sep=0pt] at (395,66) {$2$};
+\draw (31,94) .. controls (80,80) and (111,104) .. (169,87)
+ .. controls (206,75) and (218,94) .. (259,82)
+ .. controls (300,72) and (312,91) .. (353,80)
+ .. controls (364,79) and (375,77) .. (378,82);
+\draw (395,80) -- (428,80);
+\end{tikzpicture}}
 
 Soit $\Sigma_i^+$ la comp. conn. de $X\setminus E_i$ qui ne contient pas $E_j$ $(j\ne i)$, alors on a (si $I=\{1,2\}$)
-% Drawing coordinate map: full-scan (x,y) = local (x+22,y+1069).
-% The pale lower-right rim is drawn in separate supported runs; its exact continuity remains uncertain.
+% DRAW01: full-scan origin (19,1038), fixed local source-pixel rectangle.
+% C's two left-brace paths and right-brace path are retained after checking,
+% with local translation (5,33), i.e. full-scan origin (24,1071) for those paths.
 \figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
-\path[use as bounding box] (0,-40) rectangle (535,300);
-\draw (182,89) .. controls (226,-13) and (337,-39) .. (379,72)
- .. controls (407,148) and (405,201) .. (388,217);
-\node[anchor=north west,inner sep=0] at (354,222) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (34,44);
-\draw[gray,line width=.28pt] (29,3) .. controls (24,17) and (15,29) .. (5,39);
-\end{tikzpicture}}};
-\draw (355,266) .. controls (341,275) and (321,280) .. (303,281)
- .. controls (217,298) and (139,247) .. (161,158)
- .. controls (157,176) and (155,135) .. (182,89);
-\draw[line width=.8pt] (181,89) .. controls (256,91) and (313,77) .. (382,86)
- (174,218) .. controls (240,224) and (317,212) .. (380,212);
+\path[use as bounding box] (0,0) rectangle (553,336);
+% Oval: visible strong runs, pale runs and short gaps are distinct paths.
+\draw (186,122) .. controls (210,76) and (262,35) .. (290,38)
+ .. controls (342,35) and (380,88) .. (402,160);
+\draw (403,168) .. controls (405,185) and (403,206) .. (401,216);
+\draw[black!45] (401,217) .. controls (401,226) and (398,235) .. (394,243);
+\draw (391,249) .. controls (387,257) and (382,263) .. (378,267);
+\draw (374,273) .. controls (369,282) and (365,287) .. (361,291);
+\draw (358,295) .. controls (334,319) and (294,320) .. (269,315)
+ .. controls (219,309) and (178,276) .. (169,220)
+ .. controls (166,206) and (168,197) .. (168,193);
+\draw (168,193) .. controls (163,196) and (163,190) .. (166,181);
+\draw (168,193) -- (173,185);
+\draw[black!45] (168,179) .. controls (174,160) and (179,139) .. (186,122);
+% Chords, separately checked at both rim contacts.
+\draw[line width=.8pt] (186,122) .. controls (247,125) and (324,109) .. (392,119)
+ (176,250) .. controls (242,253) and (328,246) .. (391,239);
+\begin{scope}[shift={(5,33)}]
 \draw (44,9) .. controls (46,57) and (63,106) .. (32,108)
  .. controls (52,132) and (38,151) .. (46,195) -- (55,228);
 \draw (41,109) .. controls (72,143) and (35,144) .. (48,193)
  .. controls (47,224) and (57,241) .. (39,252) .. controls (55,242) and (43,259) .. (49,282);
 \draw (428,86) .. controls (439,93) and (409,141) .. (434,149)
  .. controls (420,158) and (436,251) .. (417,254);
-\node[inner sep=0] at (166,20) {\rlap{$\unsure{\Sigma_1^+|\Sigma_2^+}$}\phantom{$\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}$}};
-% CANCEL01: the two diagonal crossing runs of the upper-left deleted label.
-\draw[line width=.7pt] (135,39) -- (187,-8);
-\draw[line width=.45pt] (141,32) .. controls (158,13) and (164,2) .. (177,-13);
-\node at (139,90) {$E_1$}; \node at (149,220) {$E_2$};
-\node at (429,32) {$\Sigma_1^+$};
-\node at (492,160) {$\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}$};
-% G03: detached dot above the crowded right-hand exponent; role and hand undetermined.
-\node[inner sep=0] at (507,125) {\unsure{$\cdot$}};
-\node at (14,111) {$\Sigma_2^-$}; \node at (115,278) {$\Sigma_2^+$};
+\end{scope}
+% Cancelled label: one visible text copy, actual crossing paths, invisible deletion annotation.
+\node[inner sep=0pt] at (167,48) {\rlap{$\unsure{\Sigma_1^+|\Sigma_2^+}$}\phantom{$\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}$}};
+\draw (138,60) -- (198,27);
+\draw (151,42) .. controls (161,20) and (181,12) .. (177,24) -- (149,52);
+\node at (139,116) {$E_1$}; \node at (150,247) {$E_2$};
+\node at (430,68) {$\Sigma_1^+$};
+\node at (501,193) {$\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}$};
+\node at (23,135) {$\Sigma_2^-$}; \node at (131,308) {$\Sigma_2^+$};
+% MARK01: detached short dot above the right overwritten superscript;
+% full-scan observed bbox approximately (525,1189,531,1198), role/hand unresolved.
+\node[inner sep=0pt] at (509,156) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]
+\path[use as bounding box] (0,0) rectangle (4,6);
+\fill (1,0) .. controls (4,1) and (4,4) .. (2,6) .. controls (0,5) and (0,2) .. (1,0);
+\end{tikzpicture}}};
 \end{tikzpicture}}
+
 \[
  \Sigma_1^+\cap\Sigma_2^+=\varnothing
  \tag*{(1)}
 \]
-ce qui \deleted{résulte de} équivaut à
+ce qui \deleted{résulte de}
 \[
  \begin{aligned}
- &\deleted{\Sigma_1^-\supset\Sigma_2^+}\\
+ &\deleted{\Sigma_1^-\supset\Sigma_2^+}\qquad\text{\unsure{équivaut|èquivaut} à}\\
  &\deleted{\Sigma_2^-\supset\Sigma_1^+}\qquad \Sigma_1^+\subset\Sigma_2^-\cup E_2,\quad\text{et}
  \end{aligned}
 \]
-% Local cancelled words, origin (211,1427); both horizontal crossing runs retained.
-\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (220,86);
-\node[anchor=base west,inner sep=0] at (15,57) {\rlap{\unsure{Car si|car si}}\phantom{\deleted{\unsure{Car si|car si}}}};
-\draw (37,48) .. controls (90,46) and (138,45) .. (182,47);
-\draw (45,54) .. controls (108,55) and (156,58) .. (201,58);
+% CANCEL01/CANCEL02: full-scan origin (206,1437); two cancellation runs.
+\figure{\begin{tikzpicture}[x=.018cm,y=-.018cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (232,73);
+\node[anchor=base west,inner sep=0pt] at (16,47) {\rlap{\unsure{car si|Car si}}\phantom{\deleted{\unsure{car si|Car si}}}};
+\draw (42,37) .. controls (100,40) and (155,34) .. (201,37);
+\draw (43,47) .. controls (95,47) and (153,53) .. (215,47);
 \end{tikzpicture}}
 \deleted{Si on avait} comme $\Sigma_1^+\cap E_2=\varnothing$, cela équivaut aussi à
 \[
  \Sigma_1^+\subset\Sigma_2^-
  \tag*{(2)}
 \]
-% G04: two detached small marks at full-scan (1602,1779)--(1612,1791); hand and role undetermined.
-\margin{\unsure{\begin{tikzpicture}[x=.02cm,y=-.02cm]
-\path[use as bounding box] (0,0) rectangle (10,12);
-\fill (6,1) ellipse (1 and .7);
-\fill (1,8) ellipse (1 and .6);
-\end{tikzpicture}}}
-\unsure{et} symétriquement, à
+\unsure{et} \unsure{symètriquement|symétriquement}, à
 \[
  \Sigma_2^+\subset\Sigma_1^-
  \tag*{$(2')$}
 \]
 
-% Lower correction group: full-scan (x,y) = local (x+219,y+2009).
-\figure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round,line join=round]
-\path[use as bounding box] (0,0) rectangle (1448,145);
-\node[anchor=base west,inner sep=0] at (19,122) {Comme};
-\node[anchor=base west,inner sep=0] at (207,43) {\rlap{\unsure{vois. ouvert}}\phantom{\deleted{\unsure{vois. ouvert}}}};
-\draw (209,37) .. controls (270,33) and (334,38) .. (410,36);
-\node[anchor=base west,inner sep=0] at (265,122) {$\Sigma_2^-\supset E_1,$};
-% G05: detached slant below the struck words, visible (510,2076)--(526,2063).
-\node[inner sep=0] at (299,61) {\unsure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (16,13);
-\draw (0,13) .. controls (5,6) and (10,1) .. (16,0);
+Comme
+% MARK02 and raised cancelled words: full-scan origin (409,2008).
+\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(inc.base),line cap=round]
+\path[use as bounding box] (0,0) rectangle (319,136);
+\node[anchor=base west,inner sep=0pt] at (16,42) {\deleted{\unsure{vois. ouvert}}};
+\node[anchor=base west,inner sep=0pt] (inc) at (75,113) {$\Sigma_2^-\supset E_1$,};
+\node[inner sep=0pt] at (111,61) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (19,16);
+\draw[line width=.6pt] (1,15) .. controls (8,7) and (13,3) .. (18,2);
 \end{tikzpicture}}};
-\node[anchor=base west,inner sep=0] at (556,97) {\rlap{il contient les}\phantom{\deleted{il contient les}}};
-\draw (557,91) .. controls (705,95) and (858,86) .. (997,82);
-\node[anchor=base west,inner sep=0] at (557,49) {\inserted{i.e. $\Sigma_2^-$ est un \uline{vois.} ouvert de $E_1$,}};
-\node[anchor=base west,inner sep=0] at (1048,93) {on a};
-\end{tikzpicture}}
+\end{tikzpicture} \deleted{il contient les} \inserted{i.e. $\Sigma_2^-$ est un \uline{vois.} ouvert de $E_1$,} on a
 % slanted
 \reversemarginpar
-\margin{$\overline{\Sigma_1^+}\cap E_1\ne\varnothing$ i.e. $\overline{\Sigma_1^+}\ne\Sigma_1^+$ \unsure{à signaler|à sign.ler} avant
-% G06: curved detached guide; full-scan origin (180,2145), role of the curve undetermined.
-\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (124,78);
-\node[inner sep=0] at (62,39) {\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (124,78);
-\draw (9,69) .. controls (-1,38) and (49,35) .. (75,23)
- .. controls (102,16) and (119,12) .. (119,6);
+\margin{$\overline{\Sigma_1^+}\cap E_1\ne\varnothing$ i.e. $\overline{\Sigma_1^+}\ne\Sigma_1^+$ \unsure{à sign.ler|à signaler} avant}
+\normalmarginpar
+% GUIDE02: observed curved stroke above the first Sigma of the next display.
+% Fixed full-scan origin (180,2158); no character or mathematical role assigned.
+\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (125,67);
+\node[inner sep=0pt] at (62,33) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
+\path[use as bounding box] (0,0) rectangle (125,67);
+\draw[black!65] (7,59) .. controls (0,34) and (22,28) .. (60,21)
+ .. controls (87,18) and (105,13) .. (118,7);
 \end{tikzpicture}}};
-\end{tikzpicture}}}
-\normalmarginpar
+\end{tikzpicture}}
 \[
  \Sigma_2^-\cap\Sigma_1^+\ne\varnothing
 \]
-Car $\underline{\overline{\Sigma_1^+}\cap E_1}\ne\varnothing$
-% Final local insertion: coordinates are full scan minus (1278,2080).
-\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
-\path[use as bounding box] (0,0) rectangle (362,164);
-\node[anchor=base west,inner sep=0] at (19,127) {(sinon};
-\node[anchor=base west,inner sep=0] at (170,62) {\inserted{l'ouvert}};
-\node[anchor=base west,inner sep=0] at (213,131) {$\Sigma_1^+$};
-% GUIDE02: bent attachment guide from before Sigma to the right of the inserted word.
-\draw (183,117) .. controls (207,63) and (230,75) .. (262,78)
- .. controls (285,81) and (311,79) .. (326,74) -- (326,70) -- (322,70);
-\end{tikzpicture}}
-serait \inserted{\unsure{un|une}} fermé dans $X$, donc
-% Final deleted group: origin (928,2238). The detached upper remnants have no assigned character.
-\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
-\path[use as bounding box] (0,0) rectangle (165,67);
-\node[anchor=base west,inner sep=0] at (21,49) {\rlap{\unsure{$\Sigma_1^+$ serait}}\phantom{\deleted{\unsure{$\Sigma_1^+$ serait}}}};
-\draw (11,28) -- (51,5);
-\draw (20,35) -- (70,13);
-% G07: upper remnant cluster, shape retained locally under doubt; hand, role and surface origin undetermined.
-\node[inner sep=0] at (28,14) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round]
-\path[use as bounding box] (0,0) rectangle (37,24);
-\draw (3,18) .. controls (11,8) and (8,7) .. (10,3) -- (15,18) -- (33,9);
-\draw (24,6) -- (26,16);
-\end{tikzpicture}}};
-\end{tikzpicture}}
-$X$ serait disconnexe),
+Car $\underline{\overline{\Sigma_1^+}\cap E_1}\ne\varnothing$ % GUIDE03: full-scan origin (1274,2097); hooked insertion guide retained.
+\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(sin.base),line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (386,173);
+\node[anchor=base west,inner sep=0pt] (sin) at (20,102) {(sinon};
+\node[anchor=base west,inner sep=0pt] at (220,102) {$\Sigma_1^+$};
+\node[anchor=base west,inner sep=0pt] at (171,49) {\inserted{\unsure{l'ouvert|louvert}}};
+\draw (188,100) .. controls (202,61) and (226,56) .. (258,60)
+ .. controls (292,63) and (317,61) .. (331,55) -- (329,51);
+\end{tikzpicture} serait \inserted{un} fermé dans $X$, \unsure{donc|puis} % CANCEL03: full-scan origin (920,2238), one text copy and visible overstrikes.
+\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=(del.base),line cap=round,line join=round]
+\path[use as bounding box] (0,0) rectangle (177,67);
+\node[anchor=base west,inner sep=0pt] (del) at (16,49) {\rlap{$\unsure{\Sigma_1^+\text{ serait}|\Sigma_1^+\ne\varnothing}$}\phantom{$\deleted{\unsure{\Sigma_1^+\text{ serait}|\Sigma_1^+\ne\varnothing}}$}};
+\draw (14,31) -- (53,9);
+\draw (8,25) -- (18,5) -- (24,29) -- (39,23);
+\draw (24,32) .. controls (60,23) and (105,29) .. (164,39);
+\end{tikzpicture} $X$ serait disconnexe),
 \endgroup
 % archive sheet number: 14
