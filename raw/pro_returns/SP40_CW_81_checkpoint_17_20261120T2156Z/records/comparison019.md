## Reader A

\scanpage{19}
Dém. par récurrence, c'est trivial si $\operatorname{card} I=0,1$ Le cas $\operatorname{card} I=2$ a été vu. Cas général \unsure{avec} $\operatorname{card} I\geqslant 3$, on choisit $J$ comme dessus. Il suffit de voir que les ens.
% G01: complete first U, including its three entrance/body paths.
% Shape candidates: U with entrance return | cancelled equality before U.
% Source origin (580,535); x right, y down; one local unit is one source pixel.
% The local rectangle is [0,0,120,70]; baseline y=60; scale 0.008 cm/unit.
\figure{\[
\mathord{\unsure{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(u-base),line cap=round,line join=round]
\coordinate (u-base) at (0,60);
\path[use as bounding box] (0,0) rectangle (120,70);
\draw[line width=.65pt] (36,14) .. controls (50,10) and (66,17) .. (63,28) .. controls (59,53) and (58,57) .. (68,53) .. controls (90,41) and (98,28) .. (101,17) .. controls (98,46) and (103,61) .. (114,61);
\draw[line width=.55pt] (6,26) .. controls (20,22) and (41,16) .. (60,22);
\draw[line width=.65pt] (5,26) -- (55,29);
\end{tikzpicture}}}_{J,i}\cap\Sigma_i^+,\ U_{J,i}\cap\Sigma_i^-
\]}
ont la forme précédente, il suffit de le voir pour \(\underset{\phantom{\text{l'un}}\unsure{\cdot}}{\text{\unsure{l'une|l'un}}}\) des deux.
% G02: one visible point below the terminal run of l'une/l'un; attachment unresolved.

Par hyp. de récurrence, \unsure{on a}
% G03: first footed union, with its rounded inner return and upright retraces.
% Glyph candidates coprod | bigsqcup remain unresolved (original C row R03).
% Source origin (895,965); local rectangle [0,0,125,90]; baseline y=80.
\figure{\[
U_{J,i}=X\setminus\mathop{\unsure{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(union-one-base),line cap=round,line join=round]
\coordinate (union-one-base) at (0,80);
\path[use as bounding box] (0,0) rectangle (125,90);
\draw[line width=.7pt] (13,13) .. controls (18,58) and (30,79) .. (65,75) .. controls (93,74) and (94,37) .. (96,12);
\draw[line width=.6pt] (4,80) -- (122,66);
\draw[line width=.45pt] (13,13) -- (32,78);
\draw[line width=.6pt] (96,12) -- (101,71);
\end{tikzpicture}}}\limits_{\alpha\in \deleted{\unsure{J|j}}K_0}\widehat{\Sigma}_\alpha^+
\]}
où
\[
\left\{\begin{aligned}
&\deleted{\Sigma_{\unsure{\alpha|0}}}K_0\subset J\\
&\Sigma_\alpha^+\in\pi_0(X\setminus E_\alpha)\qquad (\forall\,\alpha\in K_0)\\
&\widehat{\Sigma}_\alpha^+=\Sigma_\alpha^+\cup E_\alpha.
\end{aligned}\right.
\]
\unsure{On a|\deleted{On}On a} donc
% G04: second footed union, inspected independently in half b.
% Same glyph candidates as G03; the first-occurrence uncertainty is printed at G03.
% Source origin (820,1605); local rectangle [0,0,95,93]; baseline y=80.
\figure{\[
U=U_{J,i}\cap\Sigma_i^-=X\setminus\left(\mathop{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(union-two-base),line cap=round,line join=round]
\coordinate (union-two-base) at (0,80);
\path[use as bounding box] (0,0) rectangle (95,93);
\draw[line width=.65pt] (14,18) .. controls (17,65) and (20,78) .. (40,76) .. controls (61,79) and (62,49) .. (64,14);
\draw[line width=.6pt] (4,74) -- (71,72);
\draw[line width=.45pt] (14,18) -- (21,78);
\draw[line width=.65pt] (64,14) -- (65,80);
\end{tikzpicture}}\limits_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
\]}
\deleted{Soit} Au \unsure{dernier|deuxième} $=$, dans la \deleted{\unsure{somme|réunion}} réunion $\bigcup_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+$, il suffit de se borner \unsure{à|:} sommer sur les \deleted{$\Sigma$} $\alpha\in K_0$ tels que $\widehat{\Sigma}_\alpha^+\not\subset\widehat{\Sigma}_i^+$ i.e. $\Sigma_\alpha^+\not\subset\Sigma_i^+$ soit $K_1$ cet ens., donc
\[
U=X\setminus\left(\bigcup_{\alpha\in K_1}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
\]
% archive sheet number: 18



{
  "differences": [
    {
      "id": "A01",
      "location": "Top text, line 5, before paired display",
      "C": "\\unsure{ens.}",
      "H": "ens.",
      "reading": "ens.",
      "evidence": "Half a shows an initial small e return, joined low n/s run and a separate terminal point; the whole abbreviation can be read.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": null,
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          270,
          505,
          390,
          545
        ]
      },
      "C_source_row": "R01"
    },
    {
      "id": "A02",
      "location": "After Par hyp. de récurrence",
      "C": "\\unsure{on a}",
      "H": "on a",
      "reading": "\\unsure{on a}",
      "evidence": "Crop05 shows a short detached dark dash, a low longer returning stroke, then a point. These support the supplied compressed on a candidate without resolving its letters.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/05_ona_recurrence.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          1130,
          875,
          1260,
          925
        ]
      },
      "C_source_row": "R02"
    },
    {
      "id": "A03",
      "location": "First large union sign in the middle equality",
      "C": "\\mathop{\\unsure{\\coprod|\\bigsqcup}}",
      "H": "\\coprod",
      "reading": "G03: qualified literal footed rounded-U graphic; coprod primary, bigsqcup retained",
      "evidence": "Crop06 shows a rounded inner bowl, an extended sloping foot, a straight left supporting/retraced run and a straight right retrace. Four local paths preserve these components. The glyph-name uncertainty remains.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/06_first_union.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          897,
          975,
          1017,
          1048
        ]
      },
      "C_source_row": "R03",
      "qualification": "The witness glyph-name primary is retained; the difference is explicit preservation of the rounded return and retraced components.",
      "graphic": "G03"
    },
    {
      "id": "A04",
      "location": "Lower index of first large union, overwritten at K0",
      "C": "\\alpha\\in\\deleted{\\unsure{J}}K_0",
      "H": "\\alpha\\in K_0",
      "reading": "\\alpha\\in\\deleted{\\unsure{J|j}}K_0",
      "evidence": "Crop06 has a finer upright and loop under the heavy K; a small nearby point leaves a lowercase j reading possible. The current K0 is legible. The predecessor remains doubtful.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/06_first_union.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          974,
          1040,
          1057,
          1108
        ]
      },
      "C_source_row": "R04",
      "qualification": "C primary J and its uncertainty retained; j is an explicitly recorded supported alternative. H omits the whole predecessor."
    },
    {
      "id": "A05",
      "location": "Lead-in below the brace, before donc",
      "C": "\\unsure{On a}",
      "H": "\\struck{On} \\uncertain{On a}",
      "reading": "\\unsure{On a|\\deleted{On}On a}",
      "evidence": "Crop09 shows one overlapped capital cluster, one long low n-like continuation and a separate small lozenge before donc. The cluster supports On a; the overlapping capital also leaves H’s cancelled-On state possible. A second independent complete On cannot be isolated from these strokes.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/09_ona_donc.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          285,
          1510,
          430,
          1575
        ]
      },
      "C_source_row": "R05",
      "qualification": "H survives as the complete-state alternative; this is a qualified primary-state difference, not a conclusive rejection of H."
    },
    {
      "id": "A06",
      "location": "Struck word after dans la",
      "C": "\\deleted{\\unsure{somme|réunion}}",
      "H": "\\struck{\\ill{}}",
      "reading": "\\deleted{\\unsure{somme|réunion}}",
      "evidence": "Crop11 shows an initial small rising hook and a low sequence of humps under one long strike. The middle and ending are substantially crossed; somme remains the strongest candidate, réunion remains supported at low confidence.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/11_struck_word.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          1305,
          1785,
          1565,
          1845
        ]
      },
      "C_source_row": "R06",
      "qualification": "One H ill placeholder counted once; the replacement is still explicitly doubtful."
    },
    {
      "id": "A07",
      "location": "After se borner à / colon",
      "C": "\\unsure{sommer}",
      "H": "\\ill{}",
      "reading": "sommer",
      "evidence": "Crop12 exposes the initial curled s, low o, two linked m groups, small e return and final low r hook. All belong to the one word between the small preceding sign and sur les.",
      "confidence": "medium",
      "kind": "readable ink left as \\ill{}",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/12_borner_sommer.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          765,
          2020,
          1040,
          2085
        ]
      },
      "C_source_row": "R07"
    },
    {
      "id": "A08",
      "location": "After K1 in final prose",
      "C": "\\unsure{cet}",
      "H": "cet",
      "reading": "cet",
      "evidence": "Crop13 shows a small open/looped c-e entry and the tall final t with its right cross return; the following ens. is separate.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/13_cet.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          540,
          2210,
          640,
          2270
        ]
      },
      "C_source_row": "R08"
    },
    {
      "id": "A09",
      "location": "Line 3, before card",
      "C": "\\unsure{avec}",
      "H": "(omitted at this locus)",
      "reading": "\\unsure{avec}",
      "evidence": "Crop02 shows three separate low groups: short initial point/stroke, shallow bar, and a curved longer return. A compressed avec remains a candidate; the individual letters remain unsettled.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/02_avec.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          275,
          294,
          405,
          336
        ]
      },
      "C_source_row": "R09",
      "H_anchor": "Cas général $\\operatorname{card}I\\geq 3$"
    },
    {
      "id": "A10",
      "location": "First U of the paired display",
      "C": "\\unsure{U|\\deleted{=}U}",
      "H": "U",
      "reading": "G01: qualified full U graphic, with entrance-flourish primary and cancelled-equality alternative retained",
      "evidence": "Crop03 shows the U body and two additional near-horizontal entrance runs meeting its upper-left turn. The three selected paths reproduce those connected strokes once. Their character/old-sign attachment remains unresolved.",
      "confidence": "low",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/03_first_u.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          582,
          544,
          696,
          600
        ]
      },
      "C_source_row": "R10",
      "qualification": "The original C uncertainty is retained; the witness change is the literal entrance geometry. H shares the U primary.",
      "graphic": "G01"
    },
    {
      "id": "A11",
      "location": "Below the paired display, before des deux",
      "C": "\\unsure{l'une|l'un}",
      "H": "l'un",
      "reading": "\\unsure{l'une|l'un}",
      "evidence": "Crop04 shows l with a raised apostrophe, a low u/n run and a final extended return. That return supports a final e without settling it; the primary l’une and alternative l’un remain.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/04_lune.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          952,
          752,
          1170,
          811
        ]
      },
      "C_source_row": "R11",
      "qualification": "H’s l’un remains the explicit alternative. The point below the ending is separately recorded as A15 and is not counted as another word."
    },
    {
      "id": "A12",
      "location": "Brace first line, predecessor beneath K0",
      "C": "\\deleted{\\Sigma_{\\unsure{\\alpha|0}}}K_0",
      "H": "K_0",
      "reading": "\\deleted{\\Sigma_{\\unsure{\\alpha|0}}}K_0",
      "evidence": "Crop07 gives the angular upper, diagonal and lower Sigma strokes beneath the heavy K. The lower small overlapping loop remains compatible with alpha or zero; K0 is clear.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/07_brace_predecessor.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          690,
          1183,
          797,
          1268
        ]
      },
      "C_source_row": "R12"
    },
    {
      "id": "A13",
      "location": "After Au, before the written equality sign",
      "C": "deuxième",
      "H": "\\uncertain{dernier}",
      "reading": "\\unsure{dernier|deuxième}",
      "evidence": "Crop10 shows a small d, a long low middle run, a narrow upright/dotted group and two final low bends. I read dernier first; the compressed middle and raised marks leave deuxième possible. No expected ordinal from the formula was used to settle it.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crops/10_ordinal.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          595,
          1790,
          878,
          1847
        ]
      },
      "qualification": "H has the same primary with editorial doubt. C’s deuxième remains an explicit alternative."
    },
    {
      "id": "A14",
      "location": "Small sign between borner and sommer",
      "C": "à",
      "H": ":",
      "reading": "\\unsure{à|:}",
      "evidence": "Crop12 shows a small upper oblique dot and a lower open curved hook. The lower hook supports a compressed a with detached accent; the two-level form also supports a colon reading.",
      "confidence": "low",
      "kind": "other",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/12_borner_sommer.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          625,
          2032,
          661,
          2074
        ]
      },
      "qualification": "C’s primary à is retained with newly explicit doubt. H’s colon remains the alternative."
    },
    {
      "id": "A15",
      "location": "Small point under the terminal l’une/l’un run",
      "C": "(omitted at this locus)",
      "H": "(omitted at this locus)",
      "reading": "\\underset{\\phantom{\\text{l'un}}\\unsure{\\cdot}}{\\text{\\unsure{l'une|l'un}}}",
      "evidence": "Crop04 shows a distinct dark small point just below the right-hand terminal run. It is reproduced once below the word; attachment to the word, role and hand remain open. A still lower diffuse gray fleck supplies no additional character candidate.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/04_lune.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          1153,
          788,
          1168,
          803
        ]
      },
      "qualification": "Visible point shape has medium confidence; punctuation/letter-attachment and hand remain undetermined.",
      "graphic": "G02"
    },
    {
      "id": "A16",
      "location": "Footed union in U = U_J,i cap Sigma_i^- display",
      "C": "\\coprod",
      "H": "\\coprod",
      "reading": "G04: literal second footed rounded-U graphic, primary coprod with local bigsqcup alternative retained in report",
      "evidence": "Half b shows the second bowl, short extending foot and both straighter supporting/retraced uprights. Four selected paths reproduce this local form. Its glyph-name qualification is covered by the first-occurrence wrapper at G03.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          824,
          1615,
          891,
          1688
        ]
      },
      "qualification": "Independently inspected on half b, coordinates [824,514,891,587] in that half. No extra crop was required for this settled path geometry; glyph-name interpretation remains qualified.",
      "graphic": "G04"
    },
    {
      "id": "A17",
      "location": "Beginning of line 2",
      "C": "Le",
      "H": "le",
      "reading": "Le",
      "evidence": "Half a shows a tall upright initial L reaching well above the following cas; capital form retained.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          277,
          164,
          490,
          231
        ]
      }
    },
    {
      "id": "A18",
      "location": "End of line 1, after card I = 0,1",
      "C": "0,1$ Le",
      "H": "0,1$, le",
      "reading": "0,1$ Le",
      "evidence": "Crop01 reaches the physical right edge. The last numeral’s base reaches that edge; no further punctuation can be recovered. The transcription ends the visible group at 1 and starts the next line with Le.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/01_top_endpoint.png",
      "bbox": {
        "coordinates": "original full scan, upper-left origin, pixels",
        "xyxy": [
          1600,
          92,
          1692,
          165
        ]
      },
      "qualification": "Qualified selected-text difference only: the edge prevents a decisive statement about a comma beyond the surviving image."
    }
  ],
  "doubts": [
    {
      "location": "After Par hyp. de récurrence",
      "reading": "\\unsure{on a}",
      "alternatives": [],
      "confidence": "low",
      "reason": "Crop05 shows a short detached dark dash, a low longer returning stroke, then a point. These support the supplied compressed on a candidate without resolving its letters.",
      "crop": "crops/05_ona_recurrence.png",
      "decision_id": "A02",
      "C_source_row": "R02"
    },
    {
      "location": "First large union sign in the middle equality",
      "reading": "G03: qualified literal footed rounded-U graphic; coprod primary, bigsqcup retained",
      "alternatives": [
        "\\bigsqcup"
      ],
      "confidence": "medium",
      "reason": "Crop06 shows a rounded inner bowl, an extended sloping foot, a straight left supporting/retraced run and a straight right retrace. Four local paths preserve these components. The glyph-name uncertainty remains.",
      "crop": "crops/06_first_union.png",
      "decision_id": "A03",
      "C_source_row": "R03"
    },
    {
      "location": "Lower index of first large union, overwritten at K0",
      "reading": "\\alpha\\in\\deleted{\\unsure{J|j}}K_0",
      "alternatives": [
        "j"
      ],
      "confidence": "low",
      "reason": "Crop06 has a finer upright and loop under the heavy K; a small nearby point leaves a lowercase j reading possible. The current K0 is legible. The predecessor remains doubtful.",
      "crop": "crops/06_first_union.png",
      "decision_id": "A04",
      "C_source_row": "R04"
    },
    {
      "location": "Lead-in below the brace, before donc",
      "reading": "\\unsure{On a|\\deleted{On}On a}",
      "alternatives": [
        "\\deleted{On}On a"
      ],
      "confidence": "low",
      "reason": "Crop09 shows one overlapped capital cluster, one long low n-like continuation and a separate small lozenge before donc. The cluster supports On a; the overlapping capital also leaves H’s cancelled-On state possible. A second independent complete On cannot be isolated from these strokes.",
      "crop": "crops/09_ona_donc.png",
      "decision_id": "A05",
      "C_source_row": "R05"
    },
    {
      "location": "Struck word after dans la",
      "reading": "\\deleted{\\unsure{somme|réunion}}",
      "alternatives": [
        "réunion"
      ],
      "confidence": "low",
      "reason": "Crop11 shows an initial small rising hook and a low sequence of humps under one long strike. The middle and ending are substantially crossed; somme remains the strongest candidate, réunion remains supported at low confidence.",
      "crop": "crops/11_struck_word.png",
      "decision_id": "A06",
      "C_source_row": "R06"
    },
    {
      "location": "Line 3, before card",
      "reading": "\\unsure{avec}",
      "alternatives": [],
      "confidence": "low",
      "reason": "Crop02 shows three separate low groups: short initial point/stroke, shallow bar, and a curved longer return. A compressed avec remains a candidate; the individual letters remain unsettled.",
      "crop": "crops/02_avec.png",
      "decision_id": "A09",
      "C_source_row": "R09"
    },
    {
      "location": "First U of the paired display",
      "reading": "G01: qualified full U graphic, with entrance-flourish primary and cancelled-equality alternative retained",
      "alternatives": [
        "\\deleted{=}U"
      ],
      "confidence": "low",
      "reason": "Crop03 shows the U body and two additional near-horizontal entrance runs meeting its upper-left turn. The three selected paths reproduce those connected strokes once. Their character/old-sign attachment remains unresolved.",
      "crop": "crops/03_first_u.png",
      "decision_id": "A10",
      "C_source_row": "R10"
    },
    {
      "location": "Below the paired display, before des deux",
      "reading": "\\unsure{l'une|l'un}",
      "alternatives": [
        "l'un"
      ],
      "confidence": "medium",
      "reason": "Crop04 shows l with a raised apostrophe, a low u/n run and a final extended return. That return supports a final e without settling it; the primary l’une and alternative l’un remain.",
      "crop": "crops/04_lune.png",
      "decision_id": "A11",
      "C_source_row": "R11"
    },
    {
      "location": "Brace first line, predecessor beneath K0",
      "reading": "\\deleted{\\Sigma_{\\unsure{\\alpha|0}}}K_0",
      "alternatives": [
        "\\Sigma_0"
      ],
      "confidence": "medium",
      "reason": "Crop07 gives the angular upper, diagonal and lower Sigma strokes beneath the heavy K. The lower small overlapping loop remains compatible with alpha or zero; K0 is clear.",
      "crop": "crops/07_brace_predecessor.png",
      "decision_id": "A12",
      "C_source_row": "R12"
    },
    {
      "location": "After Au, before the written equality sign",
      "reading": "\\unsure{dernier|deuxième}",
      "alternatives": [
        "deuxième"
      ],
      "confidence": "low",
      "reason": "Crop10 shows a small d, a long low middle run, a narrow upright/dotted group and two final low bends. I read dernier first; the compressed middle and raised marks leave deuxième possible. No expected ordinal from the formula was used to settle it.",
      "crop": "crops/10_ordinal.png",
      "decision_id": "A13",
      "C_source_row": null
    },
    {
      "location": "Small sign between borner and sommer",
      "reading": "\\unsure{à|:}",
      "alternatives": [
        ":"
      ],
      "confidence": "low",
      "reason": "Crop12 shows a small upper oblique dot and a lower open curved hook. The lower hook supports a compressed a with detached accent; the two-level form also supports a colon reading.",
      "crop": "crops/12_borner_sommer.png",
      "decision_id": "A14",
      "C_source_row": null
    },
    {
      "location": "Small point under the terminal l’une/l’un run",
      "reading": "\\underset{\\phantom{\\text{l'un}}\\unsure{\\cdot}}{\\text{\\unsure{l'une|l'un}}}",
      "alternatives": [
        "point attached to the word ending",
        "independent trace"
      ],
      "confidence": "medium",
      "reason": "Crop04 shows a distinct dark small point just below the right-hand terminal run. It is reproduced once below the word; attachment to the word, role and hand remain open. A still lower diffuse gray fleck supplies no additional character candidate.",
      "crop": "crops/04_lune.png",
      "decision_id": "A15",
      "C_source_row": null
    },
    {
      "location": "Footed union in U = U_J,i cap Sigma_i^- display",
      "reading": "G04: literal second footed rounded-U graphic, primary coprod with local bigsqcup alternative retained in report",
      "alternatives": [
        "\\bigsqcup"
      ],
      "confidence": "medium",
      "reason": "Half b shows the second bowl, short extending foot and both straighter supporting/retraced uprights. Four selected paths reproduce this local form. Its glyph-name qualification is covered by the first-occurrence wrapper at G03.",
      "crop": null,
      "decision_id": "A16",
      "C_source_row": null
    },
    {
      "location": "End of line 1, after card I = 0,1",
      "reading": "0,1$ Le",
      "alternatives": [],
      "confidence": "low",
      "reason": "Crop01 reaches the physical right edge. The last numeral’s base reaches that edge; no further punctuation can be recovered. The transcription ends the visible group at 1 and starts the next line with Le.",
      "crop": "crops/01_top_endpoint.png",
      "decision_id": "A18",
      "C_source_row": null
    }
  ],
  "notes": {
    "page_content": "Handwritten continuation of a recurrence proof: paired intersections, a complement expression with indexed roofed Sigmas, a three-line brace, and restriction to K1 in the final expression.",
    "author_uncertainty": "No explicit author question mark or verbal statement of doubt was found on this sheet. Reader unsure wrappers are editorial.",
    "title_date_page_counts": "One handwritten text sheet; no title or date; pale archive numeral 18 at lower left. No author page number was added.",
    "H_apparatus": "H’s page number and two note macros are editorial apparatus. Notes about the lemma and continuation on another page are not additional manuscript text and create no collation rows.",
    "metadata_conventions": "C’s repeated cotefile{81} is removed under the current convention. scanpage{19} and the archive-number comment are retained. This metadata adjustment is excluded from physical ink difference counts.",
    "mathematics_led_reading": "Read all indices, signs, hats, joins and relations locally. The rightmost E index in the brace is alpha (crop08); the final lower union index reads alpha in K1 despite clipping at the sheet edge (crop14). No expression was repaired from an expected argument. No theorem or proof was checked.",
    "sigma_heads": "Crop03 and crop06 show the plain and roofed Sigma forms with a separated horizontal head and lower zigzag. Roofed occurrences retain widehat; plain occurrences retain Sigma. This page’s upper strokes were read as local handwriting components, without adding a closure operation.",
    "boundary_limits": "First-line numeral 1 reaches the physical right boundary; punctuation beyond it cannot be recovered. Final K1 lower index reaches the physical bottom boundary; its visible parts support K1. Crop13 includes part of the long descender belonging to que on the preceding line, retained through that existing word rather than duplicated as a new mark.",
    "graphical_accuracy": "G01/G03/G04 are manual local path approximations, with declared source origins, baselines and scales. No render, compiler, pixel alignment, extrema calculation or metric validation was run. Source loci and drawing rectangles are separately given.",
    "point_scope": "One clearly separated dark point under l’une/l’un is retained as G02. Its attachment, role and hand remain undetermined. A still lower diffuse gray fleck does not yield a further character candidate.",
    "structural_audit": "Final source-only audit passed. Its first blank-line assertion crossed separate display pairs and falsely failed; the audit was corrected to inspect each display independently, with no transcription change for that script correction.",
    "C_row_scope": "R01–R12 are assigned positional IDs for the twelve physical rows of C_doubts.txt under Doubtful readings, in their exact supplied order. The notation table is not counted as additional doubt rows."
  },
  "notation": [
    {
      "location": "top cardinality expressions",
      "sign": "I, J, card, sloped lower inequality stroke",
      "latex": "I, J, \\operatorname{card}, \\geqslant",
      "note": "geqslant records the visible oblique lower stroke; same inequality reading as witness geq, no separate macro-syntax count"
    },
    {
      "location": "paired and repeated displays",
      "sign": "U; hooked J and dotted i subscripts; cap; angular Sigma; raised plus/minus",
      "latex": "U_{J,i}, \\cap, \\Sigma_i^+, \\Sigma_i^-"
    },
    {
      "location": "first and second footed unions",
      "sign": "rounded bowl with extending foot and retraces",
      "latex": "G03 / G04, coprod primary; bigsqcup alternative",
      "note": "second occurrence locally inspected and recorded; first-occurrence printed qualifier retained"
    },
    {
      "location": "all roofed Sigmas",
      "sign": "separate angular roof over Sigma",
      "latex": "\\widehat{\\Sigma}"
    },
    {
      "location": "brace",
      "sign": "pi with two legs and small lower zero; alpha at E",
      "latex": "\\pi_0(X\\setminus E_\\alpha)",
      "note": "final E_alpha independently settled by crop08"
    },
    {
      "location": "lower two inclusion clauses",
      "sign": "open inclusion crossed by a separate oblique stroke",
      "latex": "\\not\\subset"
    },
    {
      "location": "last display",
      "sign": "ordinary curved union; alpha in K1 below it",
      "latex": "\\bigcup_{\\alpha\\in K_1}",
      "note": "crop14: K1 lower extremity meets the physical sheet boundary; no unseen continuation supplied"
    },
    {
      "location": "prose abbreviations",
      "sign": "Dém., hyp., ens., i.e.; card without point",
      "latex": "Dém., hyp., ens., i.e.; \\operatorname{card}",
      "note": "literal forms retained; no expansion in transcription"
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The first-line punctuation is bounded by the physical sheet edge. This return distinguishes a selected reading without an extra comma from a claim that no comma was originally written.",
    "For a named mathematical glyph with a distinctive rounded return and retraces, literal graphics preserve the observed form; the glyph-name candidates remain in comments and the report, with a local unsure wrapper on the first graphic."
  ]
}

## Reader B

\scanpage{19}
D\unsure{é|è}m. par récurrence, c'est trivial si $\operatorname{card} I=0,1$ Le cas $\operatorname{card} I=2$ a été vu. Cas général \unsure{avec} $\operatorname{card} I\geq 3$, on choisit $J$ comme dessus. Il suffit de voir que les ens.
\[
% G01: complete first U, with its three visible entrance/body paths.
% Source origin (580,540), positive x right and y down; unit .009 cm/pixel.
% Baseline at source y=594. Primary reading U with entrance flourish;
% alternative a cancelled equals before U. The role remains unresolved.
\mathord{\unsure{\begin{tikzpicture}[x=.009cm,y=-.009cm,baseline=(g01base.base)]
\path[use as bounding box] (0,0) rectangle (118,60);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (g01base) at (0,54) {};
\draw[line width=.65pt,line cap=round,line join=round] (35,9) .. controls (48,6) and (60,12) .. (61,27) .. controls (61,36) and (58,46) .. (64,48) .. controls (78,47) and (98,30) .. (99,12) .. controls (98,32) and (101,48) .. (112,53);
\draw[line width=.48pt,line cap=round] (5,23) .. controls (23,16) and (45,12) .. (61,23);
\draw[line width=.65pt,line cap=round] (5,23) .. controls (23,25) and (43,22) .. (55,25);
\end{tikzpicture}|\deleted{=}U}}_{J,i}\cap\Sigma_i^+,\ U_{J,i}\cap\Sigma_i^-
\]
ont la forme précédente, il suffit de le voir pour \unsure{l'une|l'un}%
% G02: two local lower traces; presence is separate from unresolved attachment,
% role, hand and surface origin. Source origin (1125,790), unit .006 cm/pixel.
% Fixed local baseline y=0; the zero-width placement keeps the group under the word ending.
\makebox[0pt][r]{\unsure{\begin{tikzpicture}[x=.006cm,y=-.006cm,baseline=(g02base.base)]
\path[use as bounding box] (0,0) rectangle (40,24);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (g02base) at (0,0) {};
\fill (35,5) ellipse (1.6 and 1.25);
\fill[black!65] (5,20) ellipse (.6 and 1.0);
\end{tikzpicture}}} des deux.

Par hyp. de récurrence, \unsure{on a}
\[
U_{J,i}=X\setminus\mathop{\unsure{\coprod|\bigsqcup}}\limits_{\alpha\in \deleted{\unsure{J}}K_0}\widehat{\Sigma}_\alpha^+
\]
où
\[
\left\{\begin{aligned}
&\deleted{\Sigma_{\unsure{\alpha|0}}}K_0\subset J\\
&\Sigma_\alpha^+\in\pi_0(X\setminus E_\alpha)\qquad (\forall\,\alpha\in K_0)\\
&\widehat{\Sigma}_\alpha^+=\Sigma_\alpha^+\cup E_\alpha.
\end{aligned}\right.
\]
\unsure{On a|\deleted{O}On a|\deleted{On}On a} donc
\[
% The later footed join was independently inspected. Its local coprod/bigsqcup
% alternative remains in the report; the first-occurrence qualification is above.
U=U_{J,i}\cap\Sigma_i^-=X\setminus\left(\coprod_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
\qquad
% G03: detached pair to the lower right of the display. No punctuation role assigned.
% Source origin (1616,1680), unit .012 cm/pixel, baseline y=0.
\mathord{\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g03base.base)]
\path[use as bounding box] (0,0) rectangle (18,22);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (g03base) at (0,0) {};
\fill (12,10) ellipse (1.8 and 1.4);
\fill (7,17) ellipse (1.7 and 1.25);
\end{tikzpicture}}}
\]
\deleted{Soit} Au \unsure{deuxième|dernier} $=$, dans la \deleted{\unsure{somme|réunion}} réunion $\bigcup_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+$, il suffit de se borner \unsure{:|à} sommer sur les \deleted{$\Sigma$} $\alpha\in K_0$ tels que $\widehat{\Sigma}_\alpha^+\not\subset\widehat{\Sigma}_i^+$ i.e. $\Sigma_\alpha^+\not\subset\Sigma_i^+$ soit $K_1$ cet ens., donc
\[
U=X\setminus\left(\bigcup_{\alpha\in K_1}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
\]
% archive sheet number: 18



{
  "differences": [
    {
      "id": "B00",
      "location": "page wrapper",
      "C": "\\cotefile{81}",
      "H": "[no cotefile wrapper]",
      "reading": "Omitted the repeated cote wrapper; scanpage{19} retained.",
      "evidence": "Brief v17 reserves cotefile{81} for scan002. This is a convention adjustment rather than an ink correction.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": null,
      "mathematical_consequence": null,
      "count_scope": "convention only"
    },
    {
      "id": "B01",
      "location": "opening abbreviation",
      "C": "Dém.",
      "H": "Dém.",
      "reading": "D\\unsure{é|è}m.",
      "evidence": "Detached accent is short and steep, with a downward-right lower part. Acute remains the first candidate; grave is also supported. The following abbreviation point is clear.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crops/01_opening.png",
      "bbox": [
        250,
        60,
        940,
        170
      ],
      "mathematical_consequence": null,
      "count_scope": "new qualification, unchanged primary"
    },
    {
      "id": "B02",
      "location": "first-line right edge after 0,1",
      "C": "0,1 Le",
      "H": "0,1, le",
      "reading": "0,1 Le",
      "evidence": "The comma between 0 and 1 is visible. The last numeral reaches the page edge; no additional post-1 comma is visible. No unseen continuation is supplied.",
      "confidence": "medium",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/02_top_edge.png",
      "bbox": [
        1350,
        55,
        1692,
        168
      ],
      "mathematical_consequence": null,
      "boundary_limit": "The numeral 1 meets the physical right page edge; punctuation beyond that edge cannot be inspected."
    },
    {
      "id": "B03",
      "location": "second physical line, initial Le",
      "C": "Le",
      "H": "le",
      "reading": "Le",
      "evidence": "A long tall initial stem and separate lower return form capital L.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": [
        275,
        165,
        350,
        230
      ],
      "mathematical_consequence": null
    },
    {
      "id": "B04",
      "location": "third line before card",
      "C": "\\unsure{avec}",
      "H": "[no word] ",
      "reading": "\\unsure{avec}",
      "evidence": "Three detached compressed marks remain visible before card: a short stroke, a low run, and a curved run. They support avec but do not resolve all letter bodies.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/03_avec.png",
      "bbox": [
        250,
        265,
        790,
        355
      ],
      "mathematical_consequence": null,
      "C_source_row": "R09"
    },
    {
      "id": "B05",
      "location": "fifth physical line before paired display",
      "C": "\\unsure{ens.}",
      "H": "ens.",
      "reading": "ens.",
      "evidence": "Half a shows the small connected e/n/s run with a separate terminal ink point.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": null,
      "bbox": [
        270,
        510,
        390,
        545
      ],
      "mathematical_consequence": null,
      "C_source_row": "R01"
    },
    {
      "id": "B06",
      "location": "first U in paired display",
      "C": "\\unsure{U|\\deleted{=}U}_{J,i}",
      "H": "U_{J,i}",
      "reading": "Complete graphical U G01 with entrance paths; cancelled-equals alternative retained.",
      "evidence": "The upper short arc enters the left U stem. A second arched run and a near-horizontal lower run extend left from that stem. Their shape is visible; flourish/cancelled-equals role remains unresolved. G01 draws the body and both extra runs once.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/04_first_U.png",
      "bbox": [
        550,
        505,
        1015,
        635
      ],
      "mathematical_consequence": null,
      "C_source_row": "R10",
      "qualification": "C primary U with entrance retained. One graphical cluster is counted; its cancellation-role uncertainty is not an additional physical count.",
      "components": [
        "G01a main upper entrance and U body",
        "G01b left arched run",
        "G01c left lower run"
      ]
    },
    {
      "id": "B07",
      "location": "below first display, l’une/l’un",
      "C": "\\unsure{l'une|l'un}",
      "H": "l'un",
      "reading": "\\unsure{l'une|l'un}",
      "evidence": "The low run after n bends downward and returns; it can support a final e but its separation from the terminal stroke is unresolved. H’s l’un survives as an alternative.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/05_lune.png",
      "bbox": [
        935,
        735,
        1555,
        840
      ],
      "mathematical_consequence": null,
      "C_source_row": "R11",
      "qualification": "Qualified primary difference from H; no conclusive H error is claimed."
    },
    {
      "id": "B08",
      "location": "below the end of l’une/l’un",
      "C": "[no separately preserved marks]",
      "H": "[no separately preserved marks]",
      "reading": "G02: darker round trace and fainter short lower trace, locally unsure.",
      "evidence": "A compact dark point lies just below the end of the word; a smaller faint upright trace lies farther left and lower. Their attachment to the word, writer and surface origin are not established.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/05_lune.png",
      "bbox": [
        935,
        735,
        1555,
        840
      ],
      "mathematical_consequence": null,
      "observed_bbox": [
        1127,
        791,
        1165,
        813
      ],
      "components": [
        {
          "id": "G02a",
          "shape": "dark compact point",
          "shape_confidence": "high",
          "source_position": [
            1160,
            795
          ]
        },
        {
          "id": "G02b",
          "shape": "faint short upright trace",
          "shape_confidence": "low",
          "source_position": [
            1130,
            810
          ]
        }
      ],
      "interpretation_confidence": "low"
    },
    {
      "id": "B09",
      "location": "after Par hyp. de récurrence",
      "C": "\\unsure{on a}",
      "H": "on a",
      "reading": "\\unsure{on a}",
      "evidence": "The three marks are a short dark dash, a paler low run with a terminal hook, and a dark point. The words remain heavily compressed.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/06_on_a.png",
      "bbox": [
        725,
        850,
        1285,
        950
      ],
      "mathematical_consequence": null,
      "C_source_row": "R02"
    },
    {
      "id": "B10",
      "location": "first large indexed join",
      "C": "\\unsure{\\coprod|\\bigsqcup}",
      "H": "\\coprod",
      "reading": "\\unsure{\\coprod|\\bigsqcup}",
      "evidence": "Two tall sides, an interior curved bowl and a projecting foot line are visible. The footed-coproduct reading remains primary, with the square-union alternative retained. No algebraic identification was used.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/07_first_union.png",
      "bbox": [
        500,
        945,
        1205,
        1120
      ],
      "mathematical_consequence": null,
      "C_source_row": "R03"
    },
    {
      "id": "B11",
      "location": "under first large join, predecessor at K0",
      "C": "\\deleted{\\unsure{J}}K_0",
      "H": "K_0",
      "reading": "\\deleted{\\unsure{J}}K_0",
      "evidence": "A thin earlier loop and curved upper remnant survive under the heavy K strokes. J remains the supported candidate, but the overwrite does not settle its full body.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/07_first_union.png",
      "bbox": [
        500,
        945,
        1205,
        1120
      ],
      "mathematical_consequence": null,
      "C_source_row": "R04"
    },
    {
      "id": "B12",
      "location": "brace line 1, predecessor under K0",
      "C": "\\deleted{\\Sigma_{\\unsure{\\alpha|0}}}K_0",
      "H": "K_0",
      "reading": "\\deleted{\\Sigma_{\\unsure{\\alpha|0}}}K_0",
      "evidence": "The older Sigma has distinct leftward horizontal runs and a diagonal return. Its small lower loop is crossed by the replacement K leg: alpha remains primary, zero retained.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/08_brace_predecessor.png",
      "bbox": [
        270,
        1160,
        975,
        1290
      ],
      "mathematical_consequence": null,
      "C_source_row": "R12"
    },
    {
      "id": "B13",
      "location": "lead-in below the brace",
      "C": "\\unsure{On a}",
      "H": "\\struck{On}\\uncertain{On a}",
      "reading": "\\unsure{On a|\\deleted{O}On a|\\deleted{On}On a}",
      "evidence": "There is one crowded initial capital group, one lower n run, and a separate a-like point before donc. The initial loops support an overwritten O reading as well as a retraced live capital. A separate fully recoverable predecessor n is not settled.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/09_on_a_donc.png",
      "bbox": [
        270,
        1490,
        670,
        1585
      ],
      "mathematical_consequence": null,
      "C_source_row": "R05",
      "qualification": "Primary reading remains C’s On a. H’s cancellation reading is retained as a complete-state alternative; no writing chronology is inferred."
    },
    {
      "id": "B14",
      "location": "later large indexed join in U equality",
      "C": "\\coprod",
      "H": "\\coprod",
      "reading": "\\coprod; local \\bigsqcup alternative retained in report",
      "evidence": "This occurrence independently shows tall sides, an extended foot and a curved lower retrace. The first-occurrence rule places the printed coprod/bigsqcup doubt at B10, while this local alternative remains recorded.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crops/10_second_union.png",
      "bbox": [
        785,
        1580,
        1070,
        1745
      ],
      "mathematical_consequence": null,
      "count_scope": "independent recurrence audit, unchanged primary"
    },
    {
      "id": "B15",
      "location": "far right of the penultimate display",
      "C": "[no mark]",
      "H": "[no mark]",
      "reading": "G03: two detached dark points in a descending-left pair, locally unsure.",
      "evidence": "The crop shows two compact dark points, separated vertically and slightly horizontally, beyond the closing parenthesis. Their presence is clear; punctuation role, writer and surface origin remain unassigned.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/11_display_endpoint.png",
      "bbox": [
        1410,
        1570,
        1665,
        1745
      ],
      "mathematical_consequence": null,
      "observed_bbox": [
        1620,
        1686,
        1632,
        1700
      ],
      "components": [
        {
          "id": "G03a",
          "source_position": [
            1628,
            1690
          ],
          "shape_confidence": "high"
        },
        {
          "id": "G03b",
          "source_position": [
            1623,
            1697
          ],
          "shape_confidence": "high"
        }
      ],
      "interpretation_confidence": "low"
    },
    {
      "id": "B16",
      "location": "after cancelled Soit, Au … equals",
      "C": "deuxième",
      "H": "\\uncertain{dernier}",
      "reading": "\\unsure{deuxième|dernier}",
      "evidence": "The word begins with a small d loop, has extended low middle strokes, a separated high mark and a low humplike ending. Deuxième is the stronger reading, but the compressed middle leaves dernier supported. Au, cancelled Soit, the equals and following comma are readable.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/12_deuxieme.png",
      "bbox": [
        260,
        1755,
        1020,
        1888
      ],
      "mathematical_consequence": null,
      "qualification": "H’s word remains an alternative; no conclusive H error is claimed."
    },
    {
      "id": "B17",
      "location": "cancelled word after dans la",
      "C": "\\deleted{\\unsure{somme|réunion}}",
      "H": "\\struck{\\ill{}}",
      "reading": "\\deleted{\\unsure{somme|réunion}}",
      "evidence": "The horizontal strike overlaps nearly the whole low letter body. A first upward/returning stroke and several low humps support somme; réunion remains possible through the damaged middle.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/13_struck_somme.png",
      "bbox": [
        1020,
        1755,
        1580,
        1870
      ],
      "mathematical_consequence": null,
      "C_source_row": "R06",
      "qualification": "One whole struck-word placeholder counted against H, with recovered word still qualified."
    },
    {
      "id": "B18",
      "location": "between borner and sommer",
      "C": "à",
      "H": ":",
      "reading": "\\unsure{:|à}",
      "evidence": "Two vertically separated small marks are visible: an upper point and a lower open, hooked mark. Colon is primary from the separated form; à remains supported by the lower hook.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crops/14_borner_mark.png",
      "bbox": [
        250,
        2015,
        1100,
        2110
      ],
      "mathematical_consequence": null,
      "qualification": "Primary differs from C but C’s à is retained as an alternative. No grammatical repair was used."
    },
    {
      "id": "B19",
      "location": "word following the borner mark",
      "C": "\\unsure{sommer}",
      "H": "\\ill{}",
      "reading": "sommer",
      "evidence": "The initial hooked s, separated low o run, humps, small e loop and terminal r hook are readable in the crop.",
      "confidence": "high",
      "kind": "readable ink left as \\ill{}",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/14_borner_mark.png",
      "bbox": [
        250,
        2015,
        1100,
        2110
      ],
      "mathematical_consequence": null,
      "C_source_row": "R07",
      "qualification": "One whole live-word placeholder counted against H."
    },
    {
      "id": "B20",
      "location": "after K1 before ens.",
      "C": "\\unsure{cet}",
      "H": "cet",
      "reading": "cet",
      "evidence": "Half b shows the opening c-like loop, low e and tall terminal t. The following ens. and comma are separate.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": null,
      "bbox": [
        535,
        2195,
        630,
        2265
      ],
      "mathematical_consequence": null,
      "C_source_row": "R08"
    },
    {
      "id": "B21",
      "location": "last display at physical bottom edge",
      "C": "\\bigcup_{\\alpha\\in K_1}\\widehat{\\Sigma}_\\alpha^+\\cup\\widehat{\\Sigma}_i^+",
      "H": "\\bigcup_{\\alpha\\in K_1}\\widehat{\\Sigma}_\\alpha^+\\cup\\widehat{\\Sigma}_i^+",
      "reading": "Current C/H reading retained.",
      "evidence": "The open round join, alpha, membership, K and lowered 1 are visible. The foot of the index reaches the physical page edge. The two roofs, plus signs and the right i point are visible.",
      "confidence": "high",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crops/15_last_formula.png",
      "bbox": [
        600,
        2240,
        1510,
        2362
      ],
      "mathematical_consequence": null,
      "boundary_limit": "The lower end of the final K1 index is physically cut by the page edge. No continuation is supplied.",
      "count_scope": "unchanged reading audit"
    }
  ],
  "doubts": [
    {
      "id": "Q01",
      "location": "Dém. accent",
      "reading": "é",
      "alternatives": [
        "è"
      ],
      "confidence": "low",
      "reason": "Short steep accent has unresolved direction.",
      "crop": "crops/01_opening.png"
    },
    {
      "id": "Q02",
      "location": "before card",
      "reading": "avec",
      "alternatives": [],
      "confidence": "low",
      "reason": "Three compressed separated marks do not reveal each letter.",
      "crop": "crops/03_avec.png",
      "C_source_row": "R09"
    },
    {
      "id": "Q03",
      "location": "first U entrance",
      "reading": "U with entrance flourish",
      "alternatives": [
        "cancelled equals before U"
      ],
      "confidence": "medium",
      "reason": "Attached runs are clear; their role is unsettled.",
      "crop": "crops/04_first_U.png",
      "C_source_row": "R10"
    },
    {
      "id": "Q04",
      "location": "below first display",
      "reading": "l'une",
      "alternatives": [
        "l'un"
      ],
      "confidence": "medium",
      "reason": "The final low return may be a letter ending or a terminal flourish.",
      "crop": "crops/05_lune.png",
      "C_source_row": "R11"
    },
    {
      "id": "Q05",
      "location": "two traces under word ending",
      "reading": "two graphical traces",
      "alternatives": [],
      "confidence": "low",
      "reason": "Their local shapes are retained, with unresolved attachment, hand and surface origin.",
      "crop": "crops/05_lune.png",
      "components": [
        "G02a",
        "G02b"
      ]
    },
    {
      "id": "Q06",
      "location": "after Par hyp. de récurrence",
      "reading": "on a",
      "alternatives": [],
      "confidence": "low",
      "reason": "Only a dash, low run and point are clearly separable.",
      "crop": "crops/06_on_a.png",
      "C_source_row": "R02"
    },
    {
      "id": "Q07",
      "location": "first large join",
      "reading": "\\coprod",
      "alternatives": [
        "\\bigsqcup"
      ],
      "confidence": "medium",
      "reason": "Curved interior and extended foot coexist.",
      "crop": "crops/07_first_union.png",
      "C_source_row": "R03"
    },
    {
      "id": "Q08",
      "location": "earlier index under K0",
      "reading": "J",
      "alternatives": [],
      "confidence": "low",
      "reason": "Earlier loop and upper remnant are obscured by K.",
      "crop": "crops/07_first_union.png",
      "C_source_row": "R04"
    },
    {
      "id": "Q09",
      "location": "brace first line, predecessor lower index",
      "reading": "\\alpha",
      "alternatives": [
        "0"
      ],
      "confidence": "medium",
      "reason": "Small earlier loop is crossed by the live K leg.",
      "crop": "crops/08_brace_predecessor.png",
      "C_source_row": "R12"
    },
    {
      "id": "Q10",
      "location": "lead-in before U equality",
      "reading": "On a",
      "alternatives": [
        "\\deleted{O}On a",
        "\\deleted{On}On a"
      ],
      "confidence": "low",
      "reason": "Word and overwritten/live-state questions remain at one initial group.",
      "crop": "crops/09_on_a_donc.png",
      "C_source_row": "R05"
    },
    {
      "id": "Q11",
      "location": "later large join",
      "reading": "\\coprod",
      "alternatives": [
        "\\bigsqcup"
      ],
      "confidence": "medium",
      "reason": "This local occurrence was independently inspected; later printed primary follows the recurring-sign convention.",
      "crop": "crops/10_second_union.png",
      "printed_qualifier": false,
      "first_qualifier": "Q07"
    },
    {
      "id": "Q12",
      "location": "far-right detached pair",
      "reading": "two dark graphical points",
      "alternatives": [],
      "confidence": "low",
      "reason": "Shape confidence high; punctuation role, hand and surface origin unresolved.",
      "crop": "crops/11_display_endpoint.png",
      "components": [
        "G03a",
        "G03b"
      ]
    },
    {
      "id": "Q13",
      "location": "Au … equals",
      "reading": "deuxième",
      "alternatives": [
        "dernier"
      ],
      "confidence": "medium",
      "reason": "Compressed middle and high mark do not settle every letter.",
      "crop": "crops/12_deuxieme.png"
    },
    {
      "id": "Q14",
      "location": "struck word after dans la",
      "reading": "somme",
      "alternatives": [
        "réunion"
      ],
      "confidence": "low",
      "reason": "Strike masks much of the letter body.",
      "crop": "crops/13_struck_somme.png",
      "C_source_row": "R06"
    },
    {
      "id": "Q15",
      "location": "after borner",
      "reading": ":",
      "alternatives": [
        "à"
      ],
      "confidence": "medium",
      "reason": "Separated upper point and lower hook support both readings.",
      "crop": "crops/14_borner_mark.png"
    }
  ],
  "notes": {
    "page_content": "Continuation of a handwritten induction argument. It gives paired intersections, an indexed complement expression, three brace conditions, a second complement expression, restriction of indices to K1, and a final complement expression. The wording and formulas are transcribed as written, with qualified ink readings retained.",
    "authors_own_uncertainty_exact_words": [],
    "title_date_page_counts": "No title, date or manuscript page number observed. Archive numeral 18 at bottom left is recorded in a comment. H page18 corresponds to scan019.",
    "mathematics_led_reading_decisions": "Followed the displayed indices, roofs, plus/minus signs, unions, set differences and crossed inclusions locally. No algebraic repair, theorem reconstruction, conditional theorem or proof check was performed.",
    "H_apparatus": "The two H note macros are editorial explanations. They do not add manuscript words and create no collation rows. H editorial uncertain markers alone create no differences when the primary text is unchanged.",
    "S_row_scope": "SA01-K81-06 spans several scans and explicitly reports no scan viewing. Its proposed examples were not silently transferred. Nine local Sigma roofs were inspected as roofs; current C/H already preserve them. No unobserved closure bar was supplied.",
    "image_processing": "Full source dimensions 1692 by 2362; each half 1692 by 1261. Source crops use full-scan coordinates, x right/y down, without alignment or pixel-difference computation. PIL crop, autocontrast, Lanczos resize to width2800 and UnsharpMask(radius1.1,percent120,threshold3) were used. No rotations.",
    "image_ledger": "Whole once, half a once, half b once, 15 preplanned crops once each; all delivered successfully. No reopenings, retries, OCR, research, compilation, rendering, installs or other-page reads.",
    "graphical_sources": "G01 is a manual complete first-U approximation with three literal paths. G02 has two fills for two lower traces; G03 has two fills for the far-right point pair. Fixed source origins, units and baselines are given in reading.tex. Their source coordinates are not metric/render validation.",
    "boundary_limits": [
      "Crop02 reaches the physical right edge at numeral1; unseen punctuation is not supplied.",
      "Crop15 preserves the whole last display available on the sheet; the lower K1 end meets the physical bottom edge. Its top edge clips part of the previous prose line, which was already read in half b."
    ],
    "other_surface_observations": "Diffuse gray paper texture without a discrete supported character was not converted into text. G02/G03 retain discrete candidate paths while their surface origin remains unresolved.",
    "structural_verification": "Final structural source checks passed: braces, environments, five display pairs, no physical blank line within a display, allowed collation kinds, 12 source-row mappings, 15 crop references and count consistency. The checker initially had a Python quote error and then treated comment-only lines as blank paragraphs; its own source was corrected. Neither checker issue required a transcription change. No TeX compiler or renderer was invoked."
  },
  "notation": [
    {
      "location": "top lines",
      "visible": "Serif I; hooked J; lower-case card; sloped comparison lower rule.",
      "latex": "\\operatorname{card} I, J, \\geq"
    },
    {
      "location": "paired display and U recurrences",
      "visible": "J with descending return and separate dotted i.",
      "latex": "U_{J,i}"
    },
    {
      "location": "paired display",
      "visible": "Angular Sigma with short low i and high plus or minus.",
      "latex": "\\Sigma_i^+,\\Sigma_i^-"
    },
    {
      "location": "first and later large join",
      "visible": "Tall sides, round interior, projecting foot; later lower retrace.",
      "latex": "\\unsure{\\coprod|\\bigsqcup} first; later \\coprod",
      "local_decisions": [
        "B10",
        "B14"
      ]
    },
    {
      "location": "first equality; brace definition; lower equality; prose union; two hatted inequality terms; final two terms",
      "visible": "Nine distinct roof-shaped accents over Sigma.",
      "latex": "\\widehat{\\Sigma}",
      "S_row": "SA01-K81-06",
      "S_assessment": "The broad S proposal supplies no locally matched omitted closure bar on this page. All nine observed roofs are already represented in current C and H."
    },
    {
      "location": "brace line2",
      "visible": "Two-legged pi, low zero, parentheses; ordinary upright-looking E and X.",
      "latex": "\\pi_0(X\\setminus E_\\alpha)"
    },
    {
      "location": "brace first line and lower prose",
      "visible": "Open curved inclusion and two independently crossed inclusions.",
      "latex": "\\subset,\\not\\subset"
    },
    {
      "location": "prose union and last display",
      "visible": "Round open join without the long projecting foot of the earlier two forms.",
      "latex": "\\bigcup"
    },
    {
      "location": "abbreviations",
      "visible": "Terminal points at Dém., hyp., both ens. occurrences and i.e.; card has no point.",
      "latex": "Dém.; hyp.; ens.; i.e.; card"
    },
    {
      "location": "after borner",
      "visible": "Upper point and separated lower hook.",
      "latex": "\\unsure{:|à}"
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The first-U entrance role cannot be captured solely by an ordinary U or cancelled-equals label. An inline fixed-origin graphical U preserves its three visible runs while retaining the role alternatives.",
    "Two newly isolated tiny-mark clusters retain unresolved attachment or surface origin. Their shape confidence is reported independently from interpretation.",
    "The end of the top line and the index at the bottom display meet physical sheet edges. A further enlargement cannot recover off-sheet content."
  ]
}

## Reader C

\scanpage{19}
Dém. par récurrence, c'est trivial si $\operatorname{card} I=0,1$ Le cas $\operatorname{card} I=2$ a été vu. Cas général \unsure{avec} $\operatorname{card} I\geq 3$, on choisit $J$ comme dessus. Il suffit de voir que les ens.
\[
\unsure{U|\deleted{=}U}_{J,i}\cap\Sigma_i^+,\ U_{J,i}\cap\Sigma_i^-
\]
ont la forme précédente, il suffit de le voir pour
\(\underset{\hspace{1.5em}\unsure{\vcenter{\hbox{%
% M01: drawing origin (1124,790) on the full scan; fixed local rectangle.
% The dark point and pale short lower-left trace have undetermined role/hand/origin.
\begin{tikzpicture}[baseline=(0,0),x=0.01cm,y=-0.01cm]
\path[use as bounding box] (0,0) rectangle (42,23);
\fill (35,7) circle[radius=0.02cm];
\draw[gray,line width=0.2pt] (6,18)--(6,20);
\end{tikzpicture}%
}}}}{\text{\unsure{l'une|l'un}}}\)
des deux.

Par hyp. de récurrence, \unsure{on a}
\[
U_{J,i}=X\setminus\mathop{\unsure{\coprod|\bigsqcup}}\limits_{\alpha\in \overset{\unsure{\cdot}}{\deleted{\unsure{J|\jmath}}}K_0}\widehat{\Sigma}_\alpha^+
\]
% M02: the point over the predecessor has full-scan centre about (989,1047).
% Its attachment is unresolved. The dotless j alternative prevents a second dot.
où
\[
\vcenter{\hbox{\unsure{%
% M03: pale trace left of brace; drawing origin (488,1276), pixel units.
% Its hand, character, role and surface origin remain undetermined.
\begin{tikzpicture}[baseline=(0,0),x=0.01cm,y=-0.01cm]
\path[use as bounding box] (0,0) rectangle (28,40);
\draw[gray!55,line width=0.18pt] (11,3)--(15,4);
\draw[gray!60,line width=0.23pt] (15,6).. controls (23,11) and (20,18)..(22,22)
  .. controls (22,28) and (13,32)..(8,36)--(1,36);
\end{tikzpicture}%
}}}\quad
\left\{\begin{aligned}
&\deleted{\Sigma_{\unsure{\alpha|0}}}K_0\subset J\\
&\Sigma_\alpha^+\in\pi_0(X\setminus E_\alpha)\qquad (\forall\,\alpha\in K_0)\\
&\widehat{\Sigma}_\alpha^+=\Sigma_\alpha^+\cup E_\alpha.
\end{aligned}\right.
\]
\unsure{On a|\deleted{On}On a} donc
\[
U=U_{J,i}\cap\Sigma_i^-=\unsure{\cdot}\,X\setminus\left(\coprod_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
\qquad\underset{\unsure{\vcenter{\hbox{%
% M04: paired dark points; origin (1618,1684) on the full scan.
% These are copied as shapes, without an asserted punctuation or algebraic role.
\begin{tikzpicture}[baseline=(0,0),x=0.01cm,y=-0.01cm]
\path[use as bounding box] (0,0) rectangle (16,19);
\fill (10,6) ellipse[x radius=0.016cm,y radius=0.011cm];
\fill (5,13) ellipse[x radius=0.015cm,y radius=0.011cm];
\end{tikzpicture}%
}}}}{\vphantom{\Sigma}}
\]
% M05: the qualified point preceding X has full-scan centre about (728,1661).
% The second large join retains the first join's qualified primary reading.
\deleted{Soit} Au \unsure{deuxième|deuxieme|dernier} $=$, dans la \deleted{\unsure{somme|réunion}} réunion $\bigcup_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+$, il suffit de se borner \unsure{à|:} sommer sur les \deleted{$\Sigma$} $\alpha\in K_0$ tels que $\widehat{\Sigma}_\alpha^+\not\subset\widehat{\Sigma}_i^+$ i.e. $\Sigma_\alpha^+\not\subset\Sigma_i^+$ soit $K_1$ cet ens., donc
\[
U=X\setminus\left(\bigcup_{\alpha\in K_1}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
\]
% The last lower limit touches the physical lower edge; no continuation is supplied.
% archive sheet number: 18



{
  "differences": [
    {
      "id": "D00",
      "location": "Source opening convention",
      "C": "\\cotefile{81}",
      "H": "omitted",
      "reading": "\\scanpage{19} only at the opening; archive 18 remains a comment",
      "evidence": "The page carries the proof continuation and the lower-left archival 18. The supplied brief reserves cotefile for scan002; no cote-title ink occurs on this sheet.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          20,
          20,
          1670,
          2345
        ]
      },
      "administrative": true
    },
    {
      "id": "D01",
      "location": "First physical line, right edge after card I=0,1",
      "C": "0,1",
      "H": "0,1,",
      "reading": "0,1",
      "evidence": "The surviving 1 reaches the physical right paper edge. No further comma survives inside that edge. This records the extant scan, with no assertion about any lost material beyond the edge.",
      "confidence": "medium",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/01_top_edge.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          1400,
          65,
          1692,
          164
        ]
      },
      "qualification": "Right-edge limit: absence outside the scanned paper is unassessed."
    },
    {
      "id": "D02",
      "location": "Second physical line, first word",
      "C": "Le",
      "H": "le",
      "reading": "Le",
      "evidence": "Half a shows a tall initial upright with a long returning foot, followed by the low continuation; initial L is capital height.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          276,
          166,
          342,
          233
        ]
      },
      "half_reference": {
        "half": "a",
        "box": [
          276,
          166,
          342,
          233
        ],
        "origin": "half a upper-left; full y=half y"
      }
    },
    {
      "id": "D03",
      "location": "Third physical line, before card I>=3",
      "C": "\\unsure{avec}",
      "H": "omitted",
      "reading": "\\unsure{avec}",
      "evidence": "Three separated short components survive: an oblique point, a low horizontal run, and a shallow curved run. They do not independently settle the compressed word; avec remains the marked candidate.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/02_avec.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          252,
          258,
          790,
          358
        ]
      },
      "source_C_doubt_row": "C019.R09"
    },
    {
      "id": "D04",
      "location": "Fifth physical line, before the paired display",
      "C": "\\unsure{ens.}",
      "H": "ens.",
      "reading": "ens.",
      "evidence": "The enlargement shows an initial small loop/entry, the joined low letter run, and a separate terminal ink point. I read ens. without a remaining word doubt.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/03_ens_first_U.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          270,
          506,
          390,
          549
        ]
      },
      "source_C_doubt_row": "C019.R01"
    },
    {
      "id": "D05",
      "location": "Paired display, first U entrance strokes",
      "C": "\\unsure{U|\\deleted{=}U}",
      "H": "U",
      "reading": "\\unsure{U|\\deleted{=}U}",
      "evidence": "Two near-horizontal entrance strokes and an upper curved return enter the first U stem. Their attachment is visible; a predecessor equality/cancellation remains unestablished. Both complete candidates are retained.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/03_ens_first_U.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          578,
          529,
          698,
          603
        ]
      },
      "source_C_doubt_row": "C019.R10"
    },
    {
      "id": "D06",
      "location": "Below the paired display, l’une/l’un",
      "C": "\\unsure{l'une|l'un}",
      "H": "l'un",
      "reading": "\\unsure{l'une|l'un}",
      "evidence": "The word has the looped l/apostrophe group, low joined humps, and a long final return. That return supports the final-e candidate without settling it. H’s l’un survives as the alternative.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/04_lune.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          962,
          750,
          1173,
          804
        ]
      },
      "source_C_doubt_row": "C019.R11",
      "qualification": "Different primary reading; H survives as an explicit alternative."
    },
    {
      "id": "D07",
      "location": "Immediately below the end of l’une/l’un",
      "C": "omitted",
      "H": "omitted",
      "reading": "M01: one dark point below the ending, with a much fainter short lower-left trace",
      "evidence": "A separate dark approximately round point is visible below the terminal return, near (1159,797). A short pale trace lies lower-left, near (1130,808). They are copied once as a locally qualified two-component graphic; their role, hand and surface origin remain unassigned.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/04_lune.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          1124,
          790,
          1166,
          813
        ]
      },
      "graphic": "M01",
      "component_confidence": {
        "dark_point": "high",
        "pale_short_trace": "low",
        "role_hand_surface_origin": "unresolved"
      }
    },
    {
      "id": "D08",
      "location": "After Par hyp. de récurrence,",
      "C": "\\unsure{on a}",
      "H": "on a",
      "reading": "\\unsure{on a}",
      "evidence": "After the comma are a small dark point, a light horizontal curved run with dark return, and another point. The small group does not settle complete letter bodies. The supplied on a candidate remains uncertain.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/05_ona1.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          1010,
          845,
          1290,
          947
        ]
      },
      "source_C_doubt_row": "C019.R02"
    },
    {
      "id": "D09",
      "location": "First single equality, large join",
      "C": "\\unsure{\\coprod|\\bigsqcup}",
      "H": "\\coprod",
      "reading": "\\unsure{\\coprod|\\bigsqcup}",
      "evidence": "The glyph has two upright sides, a separately extended foot bar, and a rounded interior return. Those visible components support the retained candidates; the surrounding mathematics has not been used to select one. The second occurrence is separately logged in notation and prints the first primary unmarked.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/06_union1_index.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          896,
          969,
          1020,
          1048
        ]
      },
      "source_C_doubt_row": "C019.R03"
    },
    {
      "id": "D10",
      "location": "First single equality, predecessor under the join",
      "C": "\\deleted{\\unsure{J}}K_0",
      "H": "K_0",
      "reading": "\\overset{\\unsure{\\cdot}}{\\deleted{\\unsure{J|\\jmath}}}K_0",
      "evidence": "Thin hooked/looped predecessor strokes survive below the live K, and a small separated high point appears near (989,1047). J remains uncertain. A dotless-j body is retained as a supported alternative under the separately copied point; this avoids drawing a second dot. The point’s attachment to that predecessor or another nearby stroke remains unresolved.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/06_union1_index.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          975,
          1040,
          1058,
          1109
        ]
      },
      "source_C_doubt_row": "C019.R04",
      "graphic": "M02",
      "qualification": "One physical predecessor/point cluster; the point qualification is not counted again."
    },
    {
      "id": "D11",
      "location": "Middle brace, first condition under live K0",
      "C": "\\deleted{\\Sigma_{\\unsure{\\alpha|0}}}K_0",
      "H": "K_0",
      "reading": "\\deleted{\\Sigma_{\\unsure{\\alpha|0}}}K_0",
      "evidence": "The thin predecessor has two left-pointed turns and a diagonal consistent with Sigma. Its small lower loop is crossed by the heavier live K strokes. Alpha and zero remain supported lower-index candidates; neither is supplied from the later lines.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/07_overwritten_K.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          690,
          1190,
          795,
          1269
        ]
      },
      "source_C_doubt_row": "C019.R12"
    },
    {
      "id": "D12",
      "location": "Left of the middle brace, near the first/second-condition gap",
      "C": "omitted",
      "H": "omitted",
      "reading": "M03: pale bowed trace with a short separated upper segment and lower-left return",
      "evidence": "The enlargement shows a faint near-upright curved trace bending down-left, plus a short separated upper segment. It yields no established character. The complete visible candidate is drawn under unsure; character, role, hand and surface origin remain unassigned.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/16_pale_trace_brace.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          488,
          1276,
          516,
          1316
        ]
      },
      "graphic": "M03",
      "qualification": "The crop fully contains the isolated trace but has no adjacent text line inside its bounds; its page position is documented."
    },
    {
      "id": "D13",
      "location": "Lead-in below the brace, before donc",
      "C": "\\unsure{On a}",
      "H": "\\struck{On} \\uncertain{On a}",
      "reading": "\\unsure{On a|\\deleted{On}On a}",
      "evidence": "One crowded tall looped group, a low following run, and a separate small oval point precede donc. Several crossing strokes remain inside the initial group. The crop does not settle a separate cancelled On versus retracing/overwriting within the visible On. The complete H state is retained as the alternative; no chronology is asserted.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/08_ona2.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          268,
          1485,
          670,
          1593
        ]
      },
      "source_C_doubt_row": "C019.R05",
      "qualification": "C’s primary words remain; the supported full-state alternative is added. H’s state is retained, not conclusively rejected."
    },
    {
      "id": "D14",
      "location": "Long U display, immediately before X",
      "C": "omitted",
      "H": "omitted",
      "reading": "\\unsure{\\cdot}",
      "evidence": "A small detached dark point is visible immediately left of X near (728,1661). It is preserved as a qualified point, without an asserted multiplication, punctuation, hand or surface origin.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/09_union2.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          723,
          1656,
          733,
          1667
        ]
      },
      "graphic": "M05"
    },
    {
      "id": "D15",
      "location": "Long U display, to the right and below the closing parenthesis",
      "C": "omitted",
      "H": "omitted",
      "reading": "M04: two small dark points, the lower one offset left",
      "evidence": "The complete-context enlargement shows two distinct dark points near (1628,1690) and (1623,1697), separated from the closing parenthesis. Their visible positions are copied literally. A punctuation role, writer and surface origin remain unresolved.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/14_lower_end_dots.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          1618,
          1684,
          1634,
          1703
        ]
      },
      "graphic": "M04",
      "component_confidence": {
        "two_shapes": "high",
        "punctuation_role_hand_surface_origin": "unresolved"
      }
    },
    {
      "id": "D16",
      "location": "Lower paragraph, after Au and before =",
      "C": "deuxième",
      "H": "\\uncertain{dernier}",
      "reading": "\\unsure{deuxième|deuxieme|dernier}",
      "evidence": "The long word has an initial looped/raised component, several separated low runs, a narrow upright with a raised mark, and a final run of humps. Deuxième remains my primary; the attachment of the raised mark leaves the accent unsettled, and dernier remains a supported word alternative. Au and the following equality/comma are readable.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/10_deuxieme.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          415,
          1765,
          1025,
          1885
        ]
      },
      "qualification": "C’s primary spelling is unchanged but newly qualified. H’s word remains an explicit alternative; this is not a conclusive H error."
    },
    {
      "id": "D17",
      "location": "Lower paragraph, struck word after dans la",
      "C": "\\deleted{\\unsure{somme|réunion}}",
      "H": "\\struck{\\ill{}}",
      "reading": "\\deleted{\\unsure{somme|réunion}}",
      "evidence": "A long cancellation covers almost the entire low letter body. A raised initial remnant, low humps, and a returning terminal stroke survive. Somme and réunion remain uncertain; the following live réunion has not been used to manufacture the predecessor.",
      "confidence": "low",
      "kind": "readable ink left as \\ill{}",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/11_struck_somme.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          1310,
          1788,
          1555,
          1830
        ]
      },
      "source_C_doubt_row": "C019.R06",
      "qualification": "Candidate recovery from surviving ink; neither word is claimed certain."
    },
    {
      "id": "D18",
      "location": "Lower paragraph, mark immediately after borner",
      "C": "à",
      "H": ":",
      "reading": "\\unsure{à|:}",
      "evidence": "The mark comprises a high short dark stroke and a lower open curved component. The lower component has a short return, which supports the à candidate; the separation also supports H’s colon reading. Both remain explicit.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/12_borner_sommer.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          631,
          2036,
          656,
          2070
        ]
      },
      "qualification": "C’s primary à remains; H’s colon remains an alternative. No grammar-based repair is made."
    },
    {
      "id": "D19",
      "location": "Lower paragraph, after the borner mark",
      "C": "\\unsure{sommer}",
      "H": "\\ill{}",
      "reading": "sommer",
      "evidence": "The enlarged word shows the initial bent s-like stroke, the connected low o/m runs, a small loop near the ending, and the returning r termination. I read sommer, retaining the written word without expansion.",
      "confidence": "medium",
      "kind": "readable ink left as \\ill{}",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/12_borner_sommer.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          772,
          2028,
          1029,
          2069
        ]
      },
      "source_C_doubt_row": "C019.R07"
    },
    {
      "id": "D20",
      "location": "Last prose line, after K1",
      "C": "\\unsure{cet}",
      "H": "cet",
      "reading": "cet",
      "evidence": "A low initial rounded entry and following join lead to a tall final t with a rightward cross/return. The enlarged group settles cet. The following ens. and separate comma are independently visible.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/13_cet.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          546,
          2214,
          633,
          2261
        ]
      },
      "source_C_doubt_row": "C019.R08"
    }
  ],
  "doubts": [
    {
      "id": "D03",
      "location": "Third physical line, before card I>=3",
      "reading": "\\unsure{avec}",
      "alternatives": [
        "avec"
      ],
      "confidence": "low",
      "reason": "Three shortened components do not settle full letters.",
      "crop": "crops/02_avec.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          252,
          258,
          790,
          358
        ]
      },
      "source_C_doubt_row": "C019.R09"
    },
    {
      "id": "D05",
      "location": "Paired display, first U entrance strokes",
      "reading": "\\unsure{U|\\deleted{=}U}",
      "alternatives": [
        "U with entrance return",
        "cancelled equality before U"
      ],
      "confidence": "low",
      "reason": "Attachment/cancellation of entrance strokes remains open.",
      "crop": "crops/03_ens_first_U.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          578,
          529,
          698,
          603
        ]
      },
      "source_C_doubt_row": "C019.R10"
    },
    {
      "id": "D06",
      "location": "Below the paired display, l’une/l’un",
      "reading": "\\unsure{l'une|l'un}",
      "alternatives": [
        "l’une",
        "l’un"
      ],
      "confidence": "medium",
      "reason": "The last low return may be the final e or a word-ending flourish.",
      "crop": "crops/04_lune.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          962,
          750,
          1173,
          804
        ]
      },
      "source_C_doubt_row": "C019.R11"
    },
    {
      "id": "D07",
      "location": "Immediately below the end of l’une/l’un",
      "reading": "M01: one dark point below the ending, with a much fainter short lower-left trace",
      "alternatives": [
        "dark point with pale lower-left trace"
      ],
      "confidence": "medium",
      "reason": "Shapes retained; role, hand and surface origin remain open.",
      "crop": "crops/04_lune.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          1124,
          790,
          1166,
          813
        ]
      },
      "source_C_doubt_row": null
    },
    {
      "id": "D08",
      "location": "After Par hyp. de récurrence,",
      "reading": "\\unsure{on a}",
      "alternatives": [
        "on a"
      ],
      "confidence": "low",
      "reason": "The tiny components do not settle complete letter bodies.",
      "crop": "crops/05_ona1.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          1010,
          845,
          1290,
          947
        ]
      },
      "source_C_doubt_row": "C019.R02"
    },
    {
      "id": "D09",
      "location": "First single equality, large join",
      "reading": "\\unsure{\\coprod|\\bigsqcup}",
      "alternatives": [
        "\\coprod",
        "\\bigsqcup"
      ],
      "confidence": "medium",
      "reason": "Foot bar and rounded return coexist in the visible glyph.",
      "crop": "crops/06_union1_index.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          896,
          969,
          1020,
          1048
        ]
      },
      "source_C_doubt_row": "C019.R03"
    },
    {
      "id": "D10",
      "location": "First single equality, predecessor under the join",
      "reading": "\\overset{\\unsure{\\cdot}}{\\deleted{\\unsure{J|\\jmath}}}K_0",
      "alternatives": [
        "cancelled J body with separate high point",
        "cancelled dotless-j body with separate high point"
      ],
      "confidence": "low",
      "reason": "Predecessor body and attachment of the high point remain open.",
      "crop": "crops/06_union1_index.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          975,
          1040,
          1058,
          1109
        ]
      },
      "source_C_doubt_row": "C019.R04"
    },
    {
      "id": "D11",
      "location": "Middle brace, first condition under live K0",
      "reading": "\\deleted{\\Sigma_{\\unsure{\\alpha|0}}}K_0",
      "alternatives": [
        "\\deleted{\\Sigma_\\alpha}",
        "\\deleted{\\Sigma_0}"
      ],
      "confidence": "medium",
      "reason": "Heavier live K obscures the predecessor’s lower loop.",
      "crop": "crops/07_overwritten_K.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          690,
          1190,
          795,
          1269
        ]
      },
      "source_C_doubt_row": "C019.R12"
    },
    {
      "id": "D12",
      "location": "Left of the middle brace, near the first/second-condition gap",
      "reading": "M03: pale bowed trace with a short separated upper segment and lower-left return",
      "alternatives": [
        "pale curved trace"
      ],
      "confidence": "low",
      "reason": "No character, hand, role or surface origin established.",
      "crop": "crops/16_pale_trace_brace.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          488,
          1276,
          516,
          1316
        ]
      },
      "source_C_doubt_row": null
    },
    {
      "id": "D13",
      "location": "Lead-in below the brace, before donc",
      "reading": "\\unsure{On a|\\deleted{On}On a}",
      "alternatives": [
        "On a",
        "cancelled On followed by On a"
      ],
      "confidence": "low",
      "reason": "Crossings do not settle full cancellation/overwriting state.",
      "crop": "crops/08_ona2.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          268,
          1485,
          670,
          1593
        ]
      },
      "source_C_doubt_row": "C019.R05"
    },
    {
      "id": "D14",
      "location": "Long U display, immediately before X",
      "reading": "\\unsure{\\cdot}",
      "alternatives": [
        "detached point"
      ],
      "confidence": "medium",
      "reason": "Point shape retained, with role, hand and surface origin open.",
      "crop": "crops/09_union2.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          723,
          1656,
          733,
          1667
        ]
      },
      "source_C_doubt_row": null
    },
    {
      "id": "D15",
      "location": "Long U display, to the right and below the closing parenthesis",
      "reading": "M04: two small dark points, the lower one offset left",
      "alternatives": [
        "paired points"
      ],
      "confidence": "high",
      "reason": "The two shapes are clear; punctuation role, hand and surface origin remain open.",
      "crop": "crops/14_lower_end_dots.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          1618,
          1684,
          1634,
          1703
        ]
      },
      "source_C_doubt_row": null
    },
    {
      "id": "D16",
      "location": "Lower paragraph, after Au and before =",
      "reading": "\\unsure{deuxième|deuxieme|dernier}",
      "alternatives": [
        "deuxième",
        "deuxieme",
        "dernier"
      ],
      "confidence": "medium",
      "reason": "Compressed word and raised mark attachment remain unsettled.",
      "crop": "crops/10_deuxieme.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          415,
          1765,
          1025,
          1885
        ]
      },
      "source_C_doubt_row": null
    },
    {
      "id": "D17",
      "location": "Lower paragraph, struck word after dans la",
      "reading": "\\deleted{\\unsure{somme|réunion}}",
      "alternatives": [
        "somme",
        "réunion"
      ],
      "confidence": "low",
      "reason": "Cancellation masks most letter bodies.",
      "crop": "crops/11_struck_somme.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          1310,
          1788,
          1555,
          1830
        ]
      },
      "source_C_doubt_row": "C019.R06"
    },
    {
      "id": "D18",
      "location": "Lower paragraph, mark immediately after borner",
      "reading": "\\unsure{à|:}",
      "alternatives": [
        "à",
        ":"
      ],
      "confidence": "low",
      "reason": "The high stroke and low open return support both candidates.",
      "crop": "crops/12_borner_sommer.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          631,
          2036,
          656,
          2070
        ]
      },
      "source_C_doubt_row": null
    },
    {
      "id": "N-JOIN2",
      "location": "Long U display, second large join",
      "reading": "\\coprod",
      "alternatives": [
        "\\coprod",
        "\\bigsqcup"
      ],
      "confidence": "medium",
      "reason": "The second glyph was independently enlarged. Its upright sides, foot stroke and rounded return leave the same local glyph interpretation open. Printed primary is unmarked by the recurring-glyph rule.",
      "crop": "crops/09_union2.png",
      "bbox": {
        "coordinate_system": "original full scan, upper-left origin, pixels",
        "box": [
          822,
          1606,
          893,
          1685
        ]
      },
      "source_C_doubt_row": null
    }
  ],
  "notes": {
    "page_content": "Continuation headed Dém. par récurrence. The text gives cardinality cases, the written U expressions and three braced conditions, then names K1 in the lower prose and ends with another complement-of-union expression. These statements are transcribed; no proof check is claimed.",
    "authors_own_uncertainty": [],
    "title_date_page_counts": {
      "title": null,
      "date": null,
      "manuscript_page_number": null,
      "archive_sheet_number": "18",
      "scan": 19,
      "H_page_label": 18
    },
    "paragraph_order": "Opening proof prose, paired display, following prose, recurrence lead-in and equality, où and brace, On a donc and display, lower paragraph and final display.",
    "mathematics_led_reading_decisions": "The mathematical expressions identified the local targets: large join glyphs, predecessor indices, hats, lower limits and noninclusion strokes. No expected identity, theorem, grammatical repair or mathematical correction was used to settle an unreadable mark.",
    "S_row_handling": {
      "id": "SA01-K81-06",
      "status": "locally inspected as a witness proposal only",
      "result": "The three quoted examples in the supplied broad-range row do not occur verbatim on this page. The visible raised signs at this page’s nine hatted Sigma occurrences are angular roofs already represented in current C/H. No new closure bar is inferred."
    },
    "H_apparatus": "H’s two note macros concerning neighboring sheets and its page label are apparatus. No prose is invented from them, and no H collation count is assigned merely for their omission.",
    "C_notes": "The supplied C_notes.txt was empty.",
    "image_order": "Whole once, a once, b once; then crop01 through crop16 once each. All deliveries succeeded. No image was reopened.",
    "image_processing": "PIL crop, autocontrast, LANCZOS resize to width 2800 and UnsharpMask only. No OCR or recognition, no source pixel matching, no image difference calculation, no optional geometry calculation.",
    "coordinate_maps": "Full scan 1692x2362; each half 1692x1261. a uses y_full=y_a; b uses y_full=y_b+1101, with 1101=2362-1261. Crop boxes all use the original full scan upper-left origin.",
    "graphical_representation": "M01, M03 and M04 use fixed local rectangles and literal paths/fills with their full-scan origins written in the TeX comments. M02 and M05 use qualified dot candidates. These preserve observed shapes without assigning a character role, mathematical operation, hand or surface origin. Font extents and surrounding TeX placement are manual approximations, not rendered or metrically validated.",
    "crop_boundaries": "Crop01 and crop15 include the physical right/bottom paper boundaries. Crop13 contains the entire target K1/cet/ens./donc group; its upper boundary cuts only the preceding line’s long descender. Crop16 contains the whole isolated pale trace but no adjacent text line. No repeat crop was made.",
    "validation": "Only structural source checks are authorized: braces, delimiters, environments, macro names, file references and reading/report consistency. No compilation, rendering or installation is performed.",
    "source_validation_history": "The first source-only pass treated comment-only lines as blank paragraphs. The validator was corrected to inspect actual physical blank lines in the unstripped source. The required repeated source-only pass returned no errors; the TeX source did not need a blank-line repair."
  },
  "notation": [
    {
      "location": "Top lines 1–3",
      "reading": "\\operatorname{card} I; J; \\geq",
      "evidence": "Serifed I, hooked J and two-part comparison sign inspected on half a."
    },
    {
      "location": "Paired display, both occurrences",
      "reading": "U_{J,i}\\cap\\Sigma_i^+, U_{J,i}\\cap\\Sigma_i^-",
      "evidence": "Both low J/i groups, both intersections and separate high plus/minus inspected; no hat is supplied to either Sigma."
    },
    {
      "location": "First large join",
      "reading": "\\unsure{\\coprod|\\bigsqcup}",
      "evidence": "Two upright sides, an extended foot bar and rounded return; crop06. Qualification retained as D09."
    },
    {
      "location": "Second large join",
      "reading": "\\coprod",
      "alternatives": [
        "\\coprod",
        "\\bigsqcup"
      ],
      "evidence": "Independent crop09 shows the short extended foot and lower curved return. Primary printed unmarked after first-occurrence qualification; local uncertainty remains in N-JOIN2."
    },
    {
      "location": "Plain joins in prose, middle definition and final display",
      "reading": "\\bigcup, \\cup",
      "evidence": "Open rounded bowls at their separately inspected positions; no foot bar supplied at these positions."
    },
    {
      "location": "Raised signs over nine Sigma occurrences across first equality, brace definition, lower display, prose union, hatted noninclusion pair and last display",
      "reading": "\\widehat{\\Sigma}",
      "evidence": "Each has an angular raised roof. Current C and H already supply these roofs. No closure bar is inferred from S’s broad page range."
    },
    {
      "location": "Middle brace, second condition",
      "reading": "\\pi_0(X\\setminus E_\\alpha)\\quad(\\forall\\alpha\\in K_0)",
      "evidence": "Pi has two uprights and a low oval; E, alpha and the parenthesized quantifier inspected on half b."
    },
    {
      "location": "Lower noninclusion line, both relations",
      "reading": "\\not\\subset",
      "evidence": "Each open inclusion has its own oblique crossing stroke, independently inspected on half b."
    },
    {
      "location": "Last lower limit at paper edge",
      "reading": "\\alpha\\in K_1",
      "evidence": "Crop15 preserves enough of the alpha, membership and K/1 strokes for the reading. Their bottom ends meet the physical edge; unseen continuation is not supplied."
    },
    {
      "location": "Contractions throughout",
      "reading": "Dém.; hyp.; ens.; i.e.; card",
      "evidence": "Stops retained at the individually read abbreviation positions; card has no added abbreviation point."
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The brief supplies no explicit layout rule for a tiny anonymous trace below a prose-word ending or beside a mathematical display. I use small standard-TikZ glyph fragments at the local attachment, with fixed origin/rectangle and locally marked uncertainty, so the adjacent word/formula occurs only once. They are not presented as mathematical operations.",
    "At the physical right and bottom sheet edges, report absence only within surviving paper; the lost continuation beyond the edge is unassessed."
  ]
}

--- A
+++ B
@@ -1,35 +1,33 @@
 \scanpage{19}
-Dém. par récurrence, c'est trivial si $\operatorname{card} I=0,1$ Le cas $\operatorname{card} I=2$ a été vu. Cas général \unsure{avec} $\operatorname{card} I\geqslant 3$, on choisit $J$ comme dessus. Il suffit de voir que les ens.
-% G01: complete first U, including its three entrance/body paths.
-% Shape candidates: U with entrance return | cancelled equality before U.
-% Source origin (580,535); x right, y down; one local unit is one source pixel.
-% The local rectangle is [0,0,120,70]; baseline y=60; scale 0.008 cm/unit.
-\figure{\[
-\mathord{\unsure{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(u-base),line cap=round,line join=round]
-\coordinate (u-base) at (0,60);
-\path[use as bounding box] (0,0) rectangle (120,70);
-\draw[line width=.65pt] (36,14) .. controls (50,10) and (66,17) .. (63,28) .. controls (59,53) and (58,57) .. (68,53) .. controls (90,41) and (98,28) .. (101,17) .. controls (98,46) and (103,61) .. (114,61);
-\draw[line width=.55pt] (6,26) .. controls (20,22) and (41,16) .. (60,22);
-\draw[line width=.65pt] (5,26) -- (55,29);
-\end{tikzpicture}}}_{J,i}\cap\Sigma_i^+,\ U_{J,i}\cap\Sigma_i^-
-\]}
-ont la forme précédente, il suffit de le voir pour \(\underset{\phantom{\text{l'un}}\unsure{\cdot}}{\text{\unsure{l'une|l'un}}}\) des deux.
-% G02: one visible point below the terminal run of l'une/l'un; attachment unresolved.
+D\unsure{é|è}m. par récurrence, c'est trivial si $\operatorname{card} I=0,1$ Le cas $\operatorname{card} I=2$ a été vu. Cas général \unsure{avec} $\operatorname{card} I\geq 3$, on choisit $J$ comme dessus. Il suffit de voir que les ens.
+\[
+% G01: complete first U, with its three visible entrance/body paths.
+% Source origin (580,540), positive x right and y down; unit .009 cm/pixel.
+% Baseline at source y=594. Primary reading U with entrance flourish;
+% alternative a cancelled equals before U. The role remains unresolved.
+\mathord{\unsure{\begin{tikzpicture}[x=.009cm,y=-.009cm,baseline=(g01base.base)]
+\path[use as bounding box] (0,0) rectangle (118,60);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (g01base) at (0,54) {};
+\draw[line width=.65pt,line cap=round,line join=round] (35,9) .. controls (48,6) and (60,12) .. (61,27) .. controls (61,36) and (58,46) .. (64,48) .. controls (78,47) and (98,30) .. (99,12) .. controls (98,32) and (101,48) .. (112,53);
+\draw[line width=.48pt,line cap=round] (5,23) .. controls (23,16) and (45,12) .. (61,23);
+\draw[line width=.65pt,line cap=round] (5,23) .. controls (23,25) and (43,22) .. (55,25);
+\end{tikzpicture}|\deleted{=}U}}_{J,i}\cap\Sigma_i^+,\ U_{J,i}\cap\Sigma_i^-
+\]
+ont la forme précédente, il suffit de le voir pour \unsure{l'une|l'un}%
+% G02: two local lower traces; presence is separate from unresolved attachment,
+% role, hand and surface origin. Source origin (1125,790), unit .006 cm/pixel.
+% Fixed local baseline y=0; the zero-width placement keeps the group under the word ending.
+\makebox[0pt][r]{\unsure{\begin{tikzpicture}[x=.006cm,y=-.006cm,baseline=(g02base.base)]
+\path[use as bounding box] (0,0) rectangle (40,24);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (g02base) at (0,0) {};
+\fill (35,5) ellipse (1.6 and 1.25);
+\fill[black!65] (5,20) ellipse (.6 and 1.0);
+\end{tikzpicture}}} des deux.
 
 Par hyp. de récurrence, \unsure{on a}
-% G03: first footed union, with its rounded inner return and upright retraces.
-% Glyph candidates coprod | bigsqcup remain unresolved (original C row R03).
-% Source origin (895,965); local rectangle [0,0,125,90]; baseline y=80.
-\figure{\[
-U_{J,i}=X\setminus\mathop{\unsure{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(union-one-base),line cap=round,line join=round]
-\coordinate (union-one-base) at (0,80);
-\path[use as bounding box] (0,0) rectangle (125,90);
-\draw[line width=.7pt] (13,13) .. controls (18,58) and (30,79) .. (65,75) .. controls (93,74) and (94,37) .. (96,12);
-\draw[line width=.6pt] (4,80) -- (122,66);
-\draw[line width=.45pt] (13,13) -- (32,78);
-\draw[line width=.6pt] (96,12) -- (101,71);
-\end{tikzpicture}}}\limits_{\alpha\in \deleted{\unsure{J|j}}K_0}\widehat{\Sigma}_\alpha^+
-\]}
+\[
+U_{J,i}=X\setminus\mathop{\unsure{\coprod|\bigsqcup}}\limits_{\alpha\in \deleted{\unsure{J}}K_0}\widehat{\Sigma}_\alpha^+
+\]
 où
 \[
 \left\{\begin{aligned}
@@ -38,21 +36,22 @@
 &\widehat{\Sigma}_\alpha^+=\Sigma_\alpha^+\cup E_\alpha.
 \end{aligned}\right.
 \]
-\unsure{On a|\deleted{On}On a} donc
-% G04: second footed union, inspected independently in half b.
-% Same glyph candidates as G03; the first-occurrence uncertainty is printed at G03.
-% Source origin (820,1605); local rectangle [0,0,95,93]; baseline y=80.
-\figure{\[
-U=U_{J,i}\cap\Sigma_i^-=X\setminus\left(\mathop{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(union-two-base),line cap=round,line join=round]
-\coordinate (union-two-base) at (0,80);
-\path[use as bounding box] (0,0) rectangle (95,93);
-\draw[line width=.65pt] (14,18) .. controls (17,65) and (20,78) .. (40,76) .. controls (61,79) and (62,49) .. (64,14);
-\draw[line width=.6pt] (4,74) -- (71,72);
-\draw[line width=.45pt] (14,18) -- (21,78);
-\draw[line width=.65pt] (64,14) -- (65,80);
-\end{tikzpicture}}\limits_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
-\]}
-\deleted{Soit} Au \unsure{dernier|deuxième} $=$, dans la \deleted{\unsure{somme|réunion}} réunion $\bigcup_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+$, il suffit de se borner \unsure{à|:} sommer sur les \deleted{$\Sigma$} $\alpha\in K_0$ tels que $\widehat{\Sigma}_\alpha^+\not\subset\widehat{\Sigma}_i^+$ i.e. $\Sigma_\alpha^+\not\subset\Sigma_i^+$ soit $K_1$ cet ens., donc
+\unsure{On a|\deleted{O}On a|\deleted{On}On a} donc
+\[
+% The later footed join was independently inspected. Its local coprod/bigsqcup
+% alternative remains in the report; the first-occurrence qualification is above.
+U=U_{J,i}\cap\Sigma_i^-=X\setminus\left(\coprod_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
+\qquad
+% G03: detached pair to the lower right of the display. No punctuation role assigned.
+% Source origin (1616,1680), unit .012 cm/pixel, baseline y=0.
+\mathord{\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g03base.base)]
+\path[use as bounding box] (0,0) rectangle (18,22);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] (g03base) at (0,0) {};
+\fill (12,10) ellipse (1.8 and 1.4);
+\fill (7,17) ellipse (1.7 and 1.25);
+\end{tikzpicture}}}
+\]
+\deleted{Soit} Au \unsure{deuxième|dernier} $=$, dans la \deleted{\unsure{somme|réunion}} réunion $\bigcup_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+$, il suffit de se borner \unsure{:|à} sommer sur les \deleted{$\Sigma$} $\alpha\in K_0$ tels que $\widehat{\Sigma}_\alpha^+\not\subset\widehat{\Sigma}_i^+$ i.e. $\Sigma_\alpha^+\not\subset\Sigma_i^+$ soit $K_1$ cet ens., donc
 \[
 U=X\setminus\left(\bigcup_{\alpha\in K_1}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
 \]

--- A
+++ C
@@ -1,37 +1,38 @@
 \scanpage{19}
-Dém. par récurrence, c'est trivial si $\operatorname{card} I=0,1$ Le cas $\operatorname{card} I=2$ a été vu. Cas général \unsure{avec} $\operatorname{card} I\geqslant 3$, on choisit $J$ comme dessus. Il suffit de voir que les ens.
-% G01: complete first U, including its three entrance/body paths.
-% Shape candidates: U with entrance return | cancelled equality before U.
-% Source origin (580,535); x right, y down; one local unit is one source pixel.
-% The local rectangle is [0,0,120,70]; baseline y=60; scale 0.008 cm/unit.
-\figure{\[
-\mathord{\unsure{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(u-base),line cap=round,line join=round]
-\coordinate (u-base) at (0,60);
-\path[use as bounding box] (0,0) rectangle (120,70);
-\draw[line width=.65pt] (36,14) .. controls (50,10) and (66,17) .. (63,28) .. controls (59,53) and (58,57) .. (68,53) .. controls (90,41) and (98,28) .. (101,17) .. controls (98,46) and (103,61) .. (114,61);
-\draw[line width=.55pt] (6,26) .. controls (20,22) and (41,16) .. (60,22);
-\draw[line width=.65pt] (5,26) -- (55,29);
-\end{tikzpicture}}}_{J,i}\cap\Sigma_i^+,\ U_{J,i}\cap\Sigma_i^-
-\]}
-ont la forme précédente, il suffit de le voir pour \(\underset{\phantom{\text{l'un}}\unsure{\cdot}}{\text{\unsure{l'une|l'un}}}\) des deux.
-% G02: one visible point below the terminal run of l'une/l'un; attachment unresolved.
+Dém. par récurrence, c'est trivial si $\operatorname{card} I=0,1$ Le cas $\operatorname{card} I=2$ a été vu. Cas général \unsure{avec} $\operatorname{card} I\geq 3$, on choisit $J$ comme dessus. Il suffit de voir que les ens.
+\[
+\unsure{U|\deleted{=}U}_{J,i}\cap\Sigma_i^+,\ U_{J,i}\cap\Sigma_i^-
+\]
+ont la forme précédente, il suffit de le voir pour
+\(\underset{\hspace{1.5em}\unsure{\vcenter{\hbox{%
+% M01: drawing origin (1124,790) on the full scan; fixed local rectangle.
+% The dark point and pale short lower-left trace have undetermined role/hand/origin.
+\begin{tikzpicture}[baseline=(0,0),x=0.01cm,y=-0.01cm]
+\path[use as bounding box] (0,0) rectangle (42,23);
+\fill (35,7) circle[radius=0.02cm];
+\draw[gray,line width=0.2pt] (6,18)--(6,20);
+\end{tikzpicture}%
+}}}}{\text{\unsure{l'une|l'un}}}\)
+des deux.
 
 Par hyp. de récurrence, \unsure{on a}
-% G03: first footed union, with its rounded inner return and upright retraces.
-% Glyph candidates coprod | bigsqcup remain unresolved (original C row R03).
-% Source origin (895,965); local rectangle [0,0,125,90]; baseline y=80.
-\figure{\[
-U_{J,i}=X\setminus\mathop{\unsure{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(union-one-base),line cap=round,line join=round]
-\coordinate (union-one-base) at (0,80);
-\path[use as bounding box] (0,0) rectangle (125,90);
-\draw[line width=.7pt] (13,13) .. controls (18,58) and (30,79) .. (65,75) .. controls (93,74) and (94,37) .. (96,12);
-\draw[line width=.6pt] (4,80) -- (122,66);
-\draw[line width=.45pt] (13,13) -- (32,78);
-\draw[line width=.6pt] (96,12) -- (101,71);
-\end{tikzpicture}}}\limits_{\alpha\in \deleted{\unsure{J|j}}K_0}\widehat{\Sigma}_\alpha^+
-\]}
+\[
+U_{J,i}=X\setminus\mathop{\unsure{\coprod|\bigsqcup}}\limits_{\alpha\in \overset{\unsure{\cdot}}{\deleted{\unsure{J|\jmath}}}K_0}\widehat{\Sigma}_\alpha^+
+\]
+% M02: the point over the predecessor has full-scan centre about (989,1047).
+% Its attachment is unresolved. The dotless j alternative prevents a second dot.
 où
 \[
+\vcenter{\hbox{\unsure{%
+% M03: pale trace left of brace; drawing origin (488,1276), pixel units.
+% Its hand, character, role and surface origin remain undetermined.
+\begin{tikzpicture}[baseline=(0,0),x=0.01cm,y=-0.01cm]
+\path[use as bounding box] (0,0) rectangle (28,40);
+\draw[gray!55,line width=0.18pt] (11,3)--(15,4);
+\draw[gray!60,line width=0.23pt] (15,6).. controls (23,11) and (20,18)..(22,22)
+  .. controls (22,28) and (13,32)..(8,36)--(1,36);
+\end{tikzpicture}%
+}}}\quad
 \left\{\begin{aligned}
 &\deleted{\Sigma_{\unsure{\alpha|0}}}K_0\subset J\\
 &\Sigma_\alpha^+\in\pi_0(X\setminus E_\alpha)\qquad (\forall\,\alpha\in K_0)\\
@@ -39,21 +40,23 @@
 \end{aligned}\right.
 \]
 \unsure{On a|\deleted{On}On a} donc
-% G04: second footed union, inspected independently in half b.
-% Same glyph candidates as G03; the first-occurrence uncertainty is printed at G03.
-% Source origin (820,1605); local rectangle [0,0,95,93]; baseline y=80.
-\figure{\[
-U=U_{J,i}\cap\Sigma_i^-=X\setminus\left(\mathop{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(union-two-base),line cap=round,line join=round]
-\coordinate (union-two-base) at (0,80);
-\path[use as bounding box] (0,0) rectangle (95,93);
-\draw[line width=.65pt] (14,18) .. controls (17,65) and (20,78) .. (40,76) .. controls (61,79) and (62,49) .. (64,14);
-\draw[line width=.6pt] (4,74) -- (71,72);
-\draw[line width=.45pt] (14,18) -- (21,78);
-\draw[line width=.65pt] (64,14) -- (65,80);
-\end{tikzpicture}}\limits_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
-\]}
-\deleted{Soit} Au \unsure{dernier|deuxième} $=$, dans la \deleted{\unsure{somme|réunion}} réunion $\bigcup_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+$, il suffit de se borner \unsure{à|:} sommer sur les \deleted{$\Sigma$} $\alpha\in K_0$ tels que $\widehat{\Sigma}_\alpha^+\not\subset\widehat{\Sigma}_i^+$ i.e. $\Sigma_\alpha^+\not\subset\Sigma_i^+$ soit $K_1$ cet ens., donc
+\[
+U=U_{J,i}\cap\Sigma_i^-=\unsure{\cdot}\,X\setminus\left(\coprod_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
+\qquad\underset{\unsure{\vcenter{\hbox{%
+% M04: paired dark points; origin (1618,1684) on the full scan.
+% These are copied as shapes, without an asserted punctuation or algebraic role.
+\begin{tikzpicture}[baseline=(0,0),x=0.01cm,y=-0.01cm]
+\path[use as bounding box] (0,0) rectangle (16,19);
+\fill (10,6) ellipse[x radius=0.016cm,y radius=0.011cm];
+\fill (5,13) ellipse[x radius=0.015cm,y radius=0.011cm];
+\end{tikzpicture}%
+}}}}{\vphantom{\Sigma}}
+\]
+% M05: the qualified point preceding X has full-scan centre about (728,1661).
+% The second large join retains the first join's qualified primary reading.
+\deleted{Soit} Au \unsure{deuxième|deuxieme|dernier} $=$, dans la \deleted{\unsure{somme|réunion}} réunion $\bigcup_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+$, il suffit de se borner \unsure{à|:} sommer sur les \deleted{$\Sigma$} $\alpha\in K_0$ tels que $\widehat{\Sigma}_\alpha^+\not\subset\widehat{\Sigma}_i^+$ i.e. $\Sigma_\alpha^+\not\subset\Sigma_i^+$ soit $K_1$ cet ens., donc
 \[
 U=X\setminus\left(\bigcup_{\alpha\in K_1}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
 \]
+% The last lower limit touches the physical lower edge; no continuation is supplied.
 % archive sheet number: 18

--- B
+++ C
@@ -1,58 +1,62 @@
 \scanpage{19}
-D\unsure{é|è}m. par récurrence, c'est trivial si $\operatorname{card} I=0,1$ Le cas $\operatorname{card} I=2$ a été vu. Cas général \unsure{avec} $\operatorname{card} I\geq 3$, on choisit $J$ comme dessus. Il suffit de voir que les ens.
+Dém. par récurrence, c'est trivial si $\operatorname{card} I=0,1$ Le cas $\operatorname{card} I=2$ a été vu. Cas général \unsure{avec} $\operatorname{card} I\geq 3$, on choisit $J$ comme dessus. Il suffit de voir que les ens.
 \[
-% G01: complete first U, with its three visible entrance/body paths.
-% Source origin (580,540), positive x right and y down; unit .009 cm/pixel.
-% Baseline at source y=594. Primary reading U with entrance flourish;
-% alternative a cancelled equals before U. The role remains unresolved.
-\mathord{\unsure{\begin{tikzpicture}[x=.009cm,y=-.009cm,baseline=(g01base.base)]
-\path[use as bounding box] (0,0) rectangle (118,60);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (g01base) at (0,54) {};
-\draw[line width=.65pt,line cap=round,line join=round] (35,9) .. controls (48,6) and (60,12) .. (61,27) .. controls (61,36) and (58,46) .. (64,48) .. controls (78,47) and (98,30) .. (99,12) .. controls (98,32) and (101,48) .. (112,53);
-\draw[line width=.48pt,line cap=round] (5,23) .. controls (23,16) and (45,12) .. (61,23);
-\draw[line width=.65pt,line cap=round] (5,23) .. controls (23,25) and (43,22) .. (55,25);
-\end{tikzpicture}|\deleted{=}U}}_{J,i}\cap\Sigma_i^+,\ U_{J,i}\cap\Sigma_i^-
+\unsure{U|\deleted{=}U}_{J,i}\cap\Sigma_i^+,\ U_{J,i}\cap\Sigma_i^-
 \]
-ont la forme précédente, il suffit de le voir pour \unsure{l'une|l'un}%
-% G02: two local lower traces; presence is separate from unresolved attachment,
-% role, hand and surface origin. Source origin (1125,790), unit .006 cm/pixel.
-% Fixed local baseline y=0; the zero-width placement keeps the group under the word ending.
-\makebox[0pt][r]{\unsure{\begin{tikzpicture}[x=.006cm,y=-.006cm,baseline=(g02base.base)]
-\path[use as bounding box] (0,0) rectangle (40,24);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (g02base) at (0,0) {};
-\fill (35,5) ellipse (1.6 and 1.25);
-\fill[black!65] (5,20) ellipse (.6 and 1.0);
-\end{tikzpicture}}} des deux.
+ont la forme précédente, il suffit de le voir pour
+\(\underset{\hspace{1.5em}\unsure{\vcenter{\hbox{%
+% M01: drawing origin (1124,790) on the full scan; fixed local rectangle.
+% The dark point and pale short lower-left trace have undetermined role/hand/origin.
+\begin{tikzpicture}[baseline=(0,0),x=0.01cm,y=-0.01cm]
+\path[use as bounding box] (0,0) rectangle (42,23);
+\fill (35,7) circle[radius=0.02cm];
+\draw[gray,line width=0.2pt] (6,18)--(6,20);
+\end{tikzpicture}%
+}}}}{\text{\unsure{l'une|l'un}}}\)
+des deux.
 
 Par hyp. de récurrence, \unsure{on a}
 \[
-U_{J,i}=X\setminus\mathop{\unsure{\coprod|\bigsqcup}}\limits_{\alpha\in \deleted{\unsure{J}}K_0}\widehat{\Sigma}_\alpha^+
+U_{J,i}=X\setminus\mathop{\unsure{\coprod|\bigsqcup}}\limits_{\alpha\in \overset{\unsure{\cdot}}{\deleted{\unsure{J|\jmath}}}K_0}\widehat{\Sigma}_\alpha^+
 \]
+% M02: the point over the predecessor has full-scan centre about (989,1047).
+% Its attachment is unresolved. The dotless j alternative prevents a second dot.
 où
 \[
+\vcenter{\hbox{\unsure{%
+% M03: pale trace left of brace; drawing origin (488,1276), pixel units.
+% Its hand, character, role and surface origin remain undetermined.
+\begin{tikzpicture}[baseline=(0,0),x=0.01cm,y=-0.01cm]
+\path[use as bounding box] (0,0) rectangle (28,40);
+\draw[gray!55,line width=0.18pt] (11,3)--(15,4);
+\draw[gray!60,line width=0.23pt] (15,6).. controls (23,11) and (20,18)..(22,22)
+  .. controls (22,28) and (13,32)..(8,36)--(1,36);
+\end{tikzpicture}%
+}}}\quad
 \left\{\begin{aligned}
 &\deleted{\Sigma_{\unsure{\alpha|0}}}K_0\subset J\\
 &\Sigma_\alpha^+\in\pi_0(X\setminus E_\alpha)\qquad (\forall\,\alpha\in K_0)\\
 &\widehat{\Sigma}_\alpha^+=\Sigma_\alpha^+\cup E_\alpha.
 \end{aligned}\right.
 \]
-\unsure{On a|\deleted{O}On a|\deleted{On}On a} donc
+\unsure{On a|\deleted{On}On a} donc
 \[
-% The later footed join was independently inspected. Its local coprod/bigsqcup
-% alternative remains in the report; the first-occurrence qualification is above.
-U=U_{J,i}\cap\Sigma_i^-=X\setminus\left(\coprod_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
-\qquad
-% G03: detached pair to the lower right of the display. No punctuation role assigned.
-% Source origin (1616,1680), unit .012 cm/pixel, baseline y=0.
-\mathord{\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g03base.base)]
-\path[use as bounding box] (0,0) rectangle (18,22);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] (g03base) at (0,0) {};
-\fill (12,10) ellipse (1.8 and 1.4);
-\fill (7,17) ellipse (1.7 and 1.25);
-\end{tikzpicture}}}
+U=U_{J,i}\cap\Sigma_i^-=\unsure{\cdot}\,X\setminus\left(\coprod_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
+\qquad\underset{\unsure{\vcenter{\hbox{%
+% M04: paired dark points; origin (1618,1684) on the full scan.
+% These are copied as shapes, without an asserted punctuation or algebraic role.
+\begin{tikzpicture}[baseline=(0,0),x=0.01cm,y=-0.01cm]
+\path[use as bounding box] (0,0) rectangle (16,19);
+\fill (10,6) ellipse[x radius=0.016cm,y radius=0.011cm];
+\fill (5,13) ellipse[x radius=0.015cm,y radius=0.011cm];
+\end{tikzpicture}%
+}}}}{\vphantom{\Sigma}}
 \]
-\deleted{Soit} Au \unsure{deuxième|dernier} $=$, dans la \deleted{\unsure{somme|réunion}} réunion $\bigcup_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+$, il suffit de se borner \unsure{:|à} sommer sur les \deleted{$\Sigma$} $\alpha\in K_0$ tels que $\widehat{\Sigma}_\alpha^+\not\subset\widehat{\Sigma}_i^+$ i.e. $\Sigma_\alpha^+\not\subset\Sigma_i^+$ soit $K_1$ cet ens., donc
+% M05: the qualified point preceding X has full-scan centre about (728,1661).
+% The second large join retains the first join's qualified primary reading.
+\deleted{Soit} Au \unsure{deuxième|deuxieme|dernier} $=$, dans la \deleted{\unsure{somme|réunion}} réunion $\bigcup_{\alpha\in K_0}\widehat{\Sigma}_\alpha^+$, il suffit de se borner \unsure{à|:} sommer sur les \deleted{$\Sigma$} $\alpha\in K_0$ tels que $\widehat{\Sigma}_\alpha^+\not\subset\widehat{\Sigma}_i^+$ i.e. $\Sigma_\alpha^+\not\subset\Sigma_i^+$ soit $K_1$ cet ens., donc
 \[
 U=X\setminus\left(\bigcup_{\alpha\in K_1}\widehat{\Sigma}_\alpha^+\ \cup\ \widehat{\Sigma}_i^+\right)
 \]
+% The last lower limit touches the physical lower edge; no continuation is supplied.
 % archive sheet number: 18
