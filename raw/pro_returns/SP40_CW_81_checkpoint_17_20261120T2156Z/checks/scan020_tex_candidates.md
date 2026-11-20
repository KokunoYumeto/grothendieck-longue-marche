# Scan020 exact TeX candidates

Status: candidate extraction complete; every ink, uncertainty, count and final selection remains with root.

Zero-based half-open Unicode character offsets; UTF-8 byte offsets are additionally recorded. Literal spans include their original whitespace.

No image or graphical metric was inspected or calculated. All geometry below is literal source.

## Source risks

- No root ink choice, confidence, correction count, original C outcome, or approval is supplied by this extraction.
- Word-bearing group boundaries differ. Transplanting a selected group requires deleting its own overlapping prose exactly once, particularly B_G02 la and A/B/C non-vide groups.
- A and B cancelled-Sigma groups carry invisible deletion annotations with different qualifier scopes; C uses a generic deleted macro. Retaining generic cancellation beside selected literal crossing commands would duplicate the source treatment.
- A alone has a graphical cancelled tout/est group, a detached point after voisinage, a par|p qualifier, and a lower E/deleted-Sigma-E qualification.
- B's relation alternatives follow the graphic as visible qualifier content; A stores complete states in an overlay phantom; C supplies formal alternatives. Moving between these exact sources requires a root-selected qualifier/annotation strategy.
- The C union comment says an annotation identifies the operator, but the inspected complete source block has no such phantom/bigcup annotation command. This is a source-comment discrepancy, awaiting root handling.
- Source origins, baselines, scales, rectangles, translations and path coordinates are copied literally. No image correspondence, metric result or rendered validation is asserted.
- A/B source point groups at la must not be combined with a separately retained copy of la when the selected complete group already owns that word.
- Final source-map attachments must bind the exact final draft hash and use checks/scan020_final_draft.tex relative to out, with out/checks/scan020_final_draft.tex retained as the workspace-relative alias.

## Complete graphical candidate blocks

### A020-G01

Cancelled Sigma/index and both cancellation runs; following U is outside.

Source: `out/readers/020/A/reading.tex` characters `[330,965)`; lines 7–16. UTF-8 SHA-256: `49faca533233ce0910fea6c702138e68017378bcce069cbe96e0c2d45caab495`.

Draw/fill commands: 2. Phantom annotations: 1. Full node and literal path spans are individually indexed in the JSON.

```tex
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
```

### A020-G02

Point only; voisinage and de remain outside.

Source: `out/readers/020/A/reading.tex` characters `[993,1350)`; lines 18–23. UTF-8 SHA-256: `49faca533233ce0910fea6c702138e68017378bcce069cbe96e0c2d45caab495`.

Draw/fill commands: 1. Phantom annotations: 0. Full node and literal path spans are individually indexed in the JSON.

```tex
% A020-G02: gray detached round point, source origin (1175,817), baseline y=817.
% Shape candidate only; role, hand and surface origin unresolved. No word is in this group.
\unsure{\begin{tikzpicture}[baseline={(0,0)},x=0.025em,y=-0.025em]
\useasboundingbox (0,0) rectangle (11,24);
\fill[gray] (4,18) ellipse [x radius=2.2,y radius=2.5];
\end{tikzpicture}}
```

### A020-G03

Cancelled word and its two crossing runs; en and the class count remain outside.

Source: `out/readers/020/A/reading.tex` characters `[1577,2136)`; lines 30–38. UTF-8 SHA-256: `49faca533233ce0910fea6c702138e68017378bcce069cbe96e0c2d45caab495`.

Draw/fill commands: 2. Phantom annotations: 1. Full node and literal path spans are individually indexed in the JSON.

```tex
% A020-G03: cancelled tout/est; fixed source origin (1457,1038), baseline y=1081.
% The observed two crossing runs replace a generic visible cancellation rule.
\begin{tikzpicture}[baseline=(A020G03base.base),x=0.025em,y=-0.025em]
\useasboundingbox (-2,-3) rectangle (130,53);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G03base) at (0,43)
{\rlap{\unsure{tout|est}}\phantom{\deleted{\unsure{tout|est}}}};
\draw[line width=0.45pt] (0,27)--(30,44);
\draw[line width=0.35pt] (46,8)--(80,26)..controls (96,34) and (110,40)..(122,41);
\end{tikzpicture}
```

### A020-G04

Point only; la and the abbreviation remain outside.

Source: `out/readers/020/A/reading.tex` characters `[2214,2563)`; lines 40–45. UTF-8 SHA-256: `49faca533233ce0910fea6c702138e68017378bcce069cbe96e0c2d45caab495`.

Draw/fill commands: 1. Phantom annotations: 0. Full node and literal path spans are individually indexed in the JSON.

```tex
% A020-G04: detached high triangular point after la; source origin (565,1395).
% Shape candidate only; role, hand and surface origin unresolved. No word is in this group.
\unsure{\begin{tikzpicture}[baseline={(0,0)},x=0.025em,y=-0.025em]
\useasboundingbox (0,-33) rectangle (12,0);
\fill (4,-31)--(7,-26)--(7,-22)--(2,-24)--cycle;
\end{tikzpicture}}
```

### A020-G05

Complete X setminus generic bigcup formula, parenthesized body, hatted label, and two literal brace paths; de la forme and où remain outside.

Source: `out/readers/020/A/reading.tex` characters `[2694,3892)`; lines 49–68. UTF-8 SHA-256: `49faca533233ce0910fea6c702138e68017378bcce069cbe96e0c2d45caab495`.

Draw/fill commands: 2. Phantom annotations: 0. Full node and literal path spans are individually indexed in the JSON.

```tex
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
```

### A020-G06

Inserted/cancelled non vide plus adjoining de I,; partie and et remain outside.

Source: `out/readers/020/A/reading.tex` characters `[3915,4809)`; lines 70–82. UTF-8 SHA-256: `49faca533233ce0910fea6c702138e68017378bcce069cbe96e0c2d45caab495`.

Draw/fill commands: 2. Phantom annotations: 1. Full node and literal path spans are individually indexed in the JSON.

```tex
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
```

### A020-G07

Relation paths and overlay phantom complete-state annotation; Sigma and pi_0 remain outside.

Source: `out/readers/020/A/reading.tex` characters `[5023,5874)`; lines 87–99. UTF-8 SHA-256: `49faca533233ce0910fea6c702138e68017378bcce069cbe96e0c2d45caab495`.

Draw/fill commands: 3. Phantom annotations: 1. Full node and literal path spans are individually indexed in the JSON.

```tex
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
```

### B_G01

Cancelled Sigma/index and two cancellation runs; following U is outside.

Source: `out/readers/020/B/reading.tex` characters `[330,1082)`; lines 7–15. UTF-8 SHA-256: `ef3bc8a63fffea22241614526297de75551e0632d9b4947a37fab589055c2036`.

Draw/fill commands: 2. Phantom annotations: 1. Full node and literal path spans are individually indexed in the JSON.

```tex
% B_G01: cancelled Sigma and its two visible crossing runs. Observed locus (320,810,403,900).
% Source origin (315,803); x right, y down; 0.25 pt per source pixel. Baseline y=76.
% The visible node occurs once; its phantom carries the deletion state without a generic extra rule.
\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,76)}]
\path[use as bounding box] (0,0) rectangle (95,100);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,76) {\rlap{$\unsure{\Sigma_j|\Sigma_i}$}\phantom{\deleted{$\unsure{\Sigma_j|\Sigma_i}$}}};
\draw[line width=0.45pt,line cap=round] (10,73) .. controls (20,54) and (30,31) .. (40,12);
\draw[line width=0.45pt,line cap=round] (45,73) .. controls (43,80) and (49,82) .. (54,76) -- (69,35);
\end{tikzpicture}
```

### B_G02

la and qualified inner point group; adverb and abbreviation remain outside. Inner origin translation is literal (66,18).

Source: `out/readers/020/B/reading.tex` characters `[1438,2195)`; lines 22–32. UTF-8 SHA-256: `ef3bc8a63fffea22241614526297de75551e0632d9b4947a37fab589055c2036`.

Draw/fill commands: 1. Phantom annotations: 0. Full node and literal path spans are individually indexed in the JSON.

```tex
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
```

### B_G03

Transplant block includes $X\setminus\text{...}$; inner TikZ owns literal union, qualified index, parenthesized body, hatted label, and brace. X setminus is outside the inner TikZ but inside this full source block.

Source: `out/readers/020/B/reading.tex` characters `[2320,4199)`; lines 36–52. UTF-8 SHA-256: `ef3bc8a63fffea22241614526297de75551e0632d9b4947a37fab589055c2036`.

Draw/fill commands: 6. Phantom annotations: 0. Full node and literal path spans are individually indexed in the JSON.

```tex
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
```

### B_G04

partie, inserted/cancelled non vide, and de I, et; une remains outside.

Source: `out/readers/020/B/reading.tex` characters `[4215,5210)`; lines 54–64. UTF-8 SHA-256: `ef3bc8a63fffea22241614526297de75551e0632d9b4947a37fab589055c2036`.

Draw/fill commands: 2. Phantom annotations: 1. Full node and literal path spans are individually indexed in the JSON.

```tex
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
```

### B_G05

Relation paths followed by formal complete-state alternatives visibly inside the same unsure wrapper; Sigma and pi_0 remain outside.

Source: `out/readers/020/B/reading.tex` characters `[5543,6437)`; lines 68–76. UTF-8 SHA-256: `ef3bc8a63fffea22241614526297de75551e0632d9b4947a37fab589055c2036`.

Draw/fill commands: 3. Phantom annotations: 0. Full node and literal path spans are individually indexed in the JSON.

```tex
% B_G05 literal reworked relation, followed inside the qualifier by its supported complete-state interpretations.
% Origin (943,1947), 0.25 pt per source pixel, baseline y=43; observed locus (944,1949,999,2004).
% M01 curved body, M02 middle shaft, M03 thin right head. No additional unqualified membership or arrow is drawn.
\mathrel{\unsure{\text{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,43)}]
\path[use as bounding box] (0,0) rectangle (62,66);
\draw[line width=0.70pt,line cap=round] (45,11) .. controls (35,-1) and (16,17) .. (7,32) .. controls (1,43) and (5,51) .. (15,55) .. controls (23,58) and (32,56) .. (39,51);
\draw[line width=0.75pt,line cap=round] (4,40) -- (43,32);
\draw[line width=0.40pt,line cap=round] (35,24) .. controls (38,16) and (51,29) .. (54,36) .. controls (56,34) and (54,20) .. (48,19);
\end{tikzpicture}}|\deleted{\Rightarrow}\in|\deleted{\to}\in|\in}}
```

### B_MARGIN

Complete slanted margin note; the source supplies a TikZ node rotate=19 with base-west anchor, but no source origin, fixed rectangle or explicit baseline declaration.

Source: `out/readers/020/B/reading.tex` characters `[5211,5488)`; lines 65–66. UTF-8 SHA-256: `ef3bc8a63fffea22241614526297de75551e0632d9b4947a37fab589055c2036`.

Draw/fill commands: 0. Phantom annotations: 0. Full node and literal path spans are individually indexed in the JSON.

```tex
% slanted; the two written conditions have no punctuation between them.
\reversemarginpar\margin{\begin{tikzpicture}\node[rotate=19,anchor=base west,inner sep=0pt,outer sep=0pt] {\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}};\end{tikzpicture}}\normalmarginpar
```

### C_G01--G02

Complete X, setminus, literal union and qualified index, parenthesized body, hatted label, and brace; adjoining French words remain outside.

Source: `out/readers/020/C/reading.tex` characters `[828,2805)`; lines 14–47. UTF-8 SHA-256: `52fb15dd649722dc953a0ad84079dc85846b03305f8ac558f3afb0b57d9e0fbf`.

Draw/fill commands: 4. Phantom annotations: 0. Full node and literal path spans are individually indexed in the JSON.

```tex
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
```

### C_G03--G04

partie, de I, with its comma, and inserted/cancelled non vide; et remains outside.

Source: `out/readers/020/C/reading.tex` characters `[2821,4042)`; lines 49–68. UTF-8 SHA-256: `52fb15dd649722dc953a0ad84079dc85846b03305f8ac558f3afb0b57d9e0fbf`.

Draw/fill commands: 2. Phantom annotations: 1. Full node and literal path spans are individually indexed in the JSON.

```tex
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
```

## Textual and qualifier crosswalk

### TEX020-01 — Opening Pi_I superscript

Original C parts: `C020-R01-1`.

**A** — `out/readers/020/A/reading.tex` characters `[36,60)`.

```tex
\Pi_I^{\unsure{\circ|0}}
```

**B** — `out/readers/020/B/reading.tex` characters `[36,60)`.

```tex
\Pi_I^{\unsure{\circ|0}}
```

**C** — `out/readers/020/C/reading.tex` characters `[36,60)`.

```tex
\Pi_I^{\unsure{\circ|0}}
```

**C_packet** — `packets/020/C.tex` characters `[36,60)`.

```tex
\Pi_I^{\unsure{\circ|0}}
```

**H** — `packets/020/H.tex` characters `[32,39)`.

```tex
\Pi_I^0
```

### TEX020-02 — Opening Pi_J superscript

Original C parts: `C020-R01-2`.

All three readers print only the recurring primary; the reader reports retain their local circle/zero doubts.

**A** — `out/readers/020/A/reading.tex` characters `[83,94)`.

```tex
\Pi_J^\circ
```

**B** — `out/readers/020/B/reading.tex` characters `[83,94)`.

```tex
\Pi_J^\circ
```

**C** — `out/readers/020/C/reading.tex` characters `[83,94)`.

```tex
\Pi_J^\circ
```

**C_packet** — `packets/020/C.tex` characters `[83,94)`.

```tex
\Pi_J^\circ
```

**H** — `packets/020/H.tex` characters `[62,69)`.

```tex
\Pi_J^0
```

### TEX020-03 — Overwritten Pi/U after distinctes de

**A** — `out/readers/020/A/reading.tex` characters `[110,133)`.

```tex
$\deleted{\Pi}U_{J,i}$,
```

**B** — `out/readers/020/B/reading.tex` characters `[110,133)`.

```tex
$\deleted{\Pi}U_{J,i}$,
```

**C** — `out/readers/020/C/reading.tex` characters `[110,133)`.

```tex
$\deleted{\Pi}U_{J,i}$,
```

**C_packet** — `packets/020/C.tex` characters `[110,133)`.

```tex
$\deleted{\Pi}U_{J,i}$,
```

**H** — `packets/020/H.tex` characters `[85,95)`.

```tex
$U_{J,i}$,
```

### TEX020-04 — Word and terminal point before parmi

Original C parts: `C020-R02-1`.

A and B print clas.|deux. with the terminal point inside each candidate. C prints deux|clas with one terminal point outside the wrapper. C_packet includes the point only in clas.; H prints deux without a point.

**A** — `out/readers/020/A/reading.tex` characters `[134,175)`.

```tex
et de plus les \unsure{clas.|deux.} parmi
```

**B** — `out/readers/020/B/reading.tex` characters `[134,175)`.

```tex
et de plus les \unsure{clas.|deux.} parmi
```

**C** — `out/readers/020/C/reading.tex` characters `[134,174)`.

```tex
et de plus les \unsure{deux|clas}. parmi
```

**C_packet** — `packets/020/C.tex` characters `[134,174)`.

```tex
et de plus les \unsure{clas.|deux} parmi
```

**H** — `packets/020/H.tex` characters `[96,121)`.

```tex
et de plus les deux parmi
```

### TEX020-05 — Complete first paired display and first Sigma index order

Original C parts: `C020-R03-1`.

A orders j|deleted J i|i. B and C order deleted J i|j|i. Preserve the actual source spacing macros with whichever full source is chosen.

**A** — `out/readers/020/A/reading.tex` characters `[176,257)`.

```tex
\[
U_{J,i}\cap\Sigma_{\unsure{j|\deleted{J}i|i}}^+,\quad U_{J,i}\cap\Sigma_i^-
\]
```

**B** — `out/readers/020/B/reading.tex` characters `[176,257)`.

```tex
\[
U_{J,i}\cap\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\quad U_{J,i}\cap\Sigma_i^-
\]
```

**C** — `out/readers/020/C/reading.tex` characters `[175,252)`.

```tex
\[
U_{J,i}\cap\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\ U_{J,i}\cap\Sigma_i^-
\]
```

**C_packet** — `packets/020/C.tex` characters `[175,252)`.

```tex
\[
U_{J,i}\cap\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\ U_{J,i}\cap\Sigma_i^-
\]
```

**H** — `packets/020/H.tex` characters `[122,179)`.

```tex
\[
U_{J,i}\cap\Sigma_i^+, \qquad U_{J,i}\cap\Sigma_i^-
\]
```

### TEX020-06 — Cancelled Sigma/index and its cancellation source

Original C parts: `C020-R04-1`.

A qualifies the index inside Sigma; B qualifies complete Sigma_j/Sigma_i candidates. Both use a visible rlap payload, invisible deletion annotation and two literal crossing commands. C uses the generic deleted macro.

**A** — `out/readers/020/A/reading.tex` characters `[330,965)`.

```tex
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
```

**B** — `out/readers/020/B/reading.tex` characters `[330,1082)`.

```tex
% B_G01: cancelled Sigma and its two visible crossing runs. Observed locus (320,810,403,900).
% Source origin (315,803); x right, y down; 0.25 pt per source pixel. Baseline y=76.
% The visible node occurs once; its phantom carries the deletion state without a generic extra rule.
\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,76)}]
\path[use as bounding box] (0,0) rectangle (95,100);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,76) {\rlap{$\unsure{\Sigma_j|\Sigma_i}$}\phantom{\deleted{$\unsure{\Sigma_j|\Sigma_i}$}}};
\draw[line width=0.45pt,line cap=round] (10,73) .. controls (20,54) and (30,31) .. (40,12);
\draw[line width=0.45pt,line cap=round] (45,73) .. controls (43,80) and (49,82) .. (54,76) -- (69,35);
\end{tikzpicture}
```

**C** — `out/readers/020/C/reading.tex` characters `[325,358)`.

```tex
$\deleted{\Sigma_{\unsure{j|i}}}$
```

**C_packet** — `packets/020/C.tex` characters `[325,363)`.

```tex
\deleted{$\unsure{\Sigma_i|\Sigma_j}$}
```

**H** — `packets/020/H.tex` characters `[252,267)`.

```tex
\struck{\ill{}}
```

### TEX020-07 — voisinage through de E and et; small-point source scope

Original C parts: `C020-R05-1`.

A includes the separate qualified A020-G02 point. B and C contain no TikZ/draw/fill command within their exact supplied phrase scopes. A/B qualify i|j on E; C prints E_i. The three reader sources all retain deleted Sigma before E and the comma.

**A** — `out/readers/020/A/reading.tex` characters `[966,1392)`.

```tex
$U_{J,i}$ est un voisinage
% A020-G02: gray detached round point, source origin (1175,817), baseline y=817.
% Shape candidate only; role, hand and surface origin unresolved. No word is in this group.
\unsure{\begin{tikzpicture}[baseline={(0,0)},x=0.025em,y=-0.025em]
\useasboundingbox (0,0) rectangle (11,24);
\fill[gray] (4,18) ellipse [x radius=2.2,y radius=2.5];
\end{tikzpicture}}
de $\deleted{\Sigma}E_{\unsure{i|j}}$, et
```

**B** — `out/readers/020/B/reading.tex` characters `[1083,1151)`.

```tex
$U_{J,i}$ est un voisinage de $\deleted{\Sigma}E_{\unsure{i|j}}$, et
```

**C** — `out/readers/020/C/reading.tex` characters `[359,414)`.

```tex
$U_{J,i}$ est un voisinage de $\deleted{\Sigma}E_i$, et
```

**C_packet** — `packets/020/C.tex` characters `[364,432)`.

```tex
$U_{J,i}$ est un voisinage de $\deleted{\Sigma}E_{\unsure{i|j}}$, et
```

**H** — `packets/020/H.tex` characters `[268,306)`.

```tex
$U_{J,i}$ est un voisinage de $E_i$ et
```

### TEX020-08 — Complete two barred nonemptiness formulas

The two overline commands occur in all current C/H source scopes. This extraction supplies no visual confirmation or correction count.

**A** — `out/readers/020/A/reading.tex` characters `[1393,1534)`.

```tex
\[
\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
\]
```

**B** — `out/readers/020/B/reading.tex` characters `[1152,1293)`.

```tex
\[
\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
\]
```

**C** — `out/readers/020/C/reading.tex` characters `[415,556)`.

```tex
\[
\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
\]
```

**C_packet** — `packets/020/C.tex` characters `[433,574)`.

```tex
\[
\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
\]
```

**H** — `packets/020/H.tex` characters `[307,398)`.

```tex
$\overline{\Sigma_i^+}\cap E_i\neq\emptyset$,
$\overline{\Sigma_i^-}\cap E_i\neq\emptyset$.
```

### TEX020-09 — Verb after On and live en before cancelled word

Original C parts: `C020-R10-1`.

**A** — `out/readers/020/A/reading.tex` characters `[1535,1576)`.

```tex
On sait donc que le nb des classes est en
```

**B** — `out/readers/020/B/reading.tex` characters `[1294,1335)`.

```tex
On sait donc que le nb des classes est en
```

**C** — `out/readers/020/C/reading.tex` characters `[557,598)`.

```tex
On sait donc que le nb des classes est en
```

**C_packet** — `packets/020/C.tex` characters `[575,630)`.

```tex
On \unsure{voit|sait} donc que le nb des classes est en
```

**H** — `packets/020/H.tex` characters `[399,437)`.

```tex
On voit donc que le nb des
classes est
```

### TEX020-10 — Cancelled tout/est after en

Original C parts: `C020-R06-1`.

A uses a visible unsure word, phantom deletion annotation and two literal runs. B/C use the generic deleted macro.

**A** — `out/readers/020/A/reading.tex` characters `[1577,2136)`.

```tex
% A020-G03: cancelled tout/est; fixed source origin (1457,1038), baseline y=1081.
% The observed two crossing runs replace a generic visible cancellation rule.
\begin{tikzpicture}[baseline=(A020G03base.base),x=0.025em,y=-0.025em]
\useasboundingbox (-2,-3) rectangle (130,53);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (A020G03base) at (0,43)
{\rlap{\unsure{tout|est}}\phantom{\deleted{\unsure{tout|est}}}};
\draw[line width=0.45pt] (0,27)--(30,44);
\draw[line width=0.35pt] (46,8)--(80,26)..controls (96,34) and (110,40)..(122,41);
\end{tikzpicture}
```

**B** — `out/readers/020/B/reading.tex` characters `[1336,1363)`.

```tex
\deleted{\unsure{tout|est}}
```

**C** — `out/readers/020/C/reading.tex` characters `[599,626)`.

```tex
\deleted{\unsure{tout|est}}
```

**C_packet** — `packets/020/C.tex` characters `[631,658)`.

```tex
\deleted{\unsure{tout|est}}
```

**H** — `packets/020/H.tex` characters `[438,453)`.

```tex
\struck{\ill{}}
```

### TEX020-11 — Written class count

Exact written statement only; no arithmetic or mathematical verification.

**A** — `out/readers/020/A/reading.tex` characters `[2137,2174)`.

```tex
$(n-1)+2=n+1=\operatorname{card} I+1$
```

**B** — `out/readers/020/B/reading.tex` characters `[1364,1401)`.

```tex
$(n-1)+2=n+1=\operatorname{card} I+1$
```

**C** — `out/readers/020/C/reading.tex` characters `[627,664)`.

```tex
$(n-1)+2=n+1=\operatorname{card} I+1$
```

**C_packet** — `packets/020/C.tex` characters `[659,696)`.

```tex
$(n-1)+2=n+1=\operatorname{card} I+1$
```

**H** — `packets/020/H.tex` characters `[454,494)`.

```tex
$(n-1)+2 = n+1 = \operatorname{card}I+1$
```

### TEX020-12 — Parenthesis opening ce qui achève and adverb

Original C parts: `C020-R11-1`.

**A** — `out/readers/020/A/reading.tex` characters `[2175,2210)`.

```tex
(ce qui achève \unsure{aussi|ainsi}
```

**B** — `out/readers/020/B/reading.tex` characters `[1402,1437)`.

```tex
(ce qui achève \unsure{aussi|ainsi}
```

**C** — `out/readers/020/C/reading.tex` characters `[665,700)`.

```tex
(ce qui achève \unsure{aussi|ainsi}
```

**C_packet** — `packets/020/C.tex` characters `[697,732)`.

```tex
(ce qui achève \unsure{aussi|ainsi}
```

**H** — `packets/020/H.tex` characters `[495,515)`.

```tex
(ce qui achève aussi
```

### TEX020-13 — la and adjoining small-mark source scope

A's graphical group owns only the point; la remains outside. B's complete graphical group owns la and a translated nested point picture. C's exact inspected phrase contains la and no separate point command.

**A** — `out/readers/020/A/reading.tex` characters `[2190,2564)`.

```tex
\unsure{aussi|ainsi} la
% A020-G04: detached high triangular point after la; source origin (565,1395).
% Shape candidate only; role, hand and surface origin unresolved. No word is in this group.
\unsure{\begin{tikzpicture}[baseline={(0,0)},x=0.025em,y=-0.025em]
\useasboundingbox (0,-33) rectangle (12,0);
\fill (4,-31)--(7,-26)--(7,-22)--(2,-24)--cycle;
\end{tikzpicture}}

```

**B** — `out/readers/020/B/reading.tex` characters `[1438,2195)`.

```tex
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
```

**C** — `out/readers/020/C/reading.tex` characters `[680,727)`.

```tex
\unsure{aussi|ainsi} la \unsure{dèm.|dém.|dem.}
```

**C_packet** — `packets/020/C.tex` characters `[712,754)`.

```tex
\unsure{aussi|ainsi} la \unsure{dém.|dem.}
```

**H** — `packets/020/H.tex` characters `[510,528)`.

```tex
aussi la dém.\ par
```

### TEX020-14 — Abbreviation accent candidates and following par/p

Original C parts: `C020-R07-1`.

A retains acute/unaccented candidates and qualifies par|p with no point on p. B/C retain grave/acute/unaccented candidates and print par unqualified.

**A** — `out/readers/020/A/reading.tex` characters `[2564,2632)`.

```tex
\unsure{dém.|dem.} \unsure{par|p} récurrence sur le nb des classes).
```

**B** — `out/readers/020/B/reading.tex` characters `[2196,2258)`.

```tex
\unsure{dèm.|dém.|dem.} par récurrence sur le nb des classes).
```

**C** — `out/readers/020/C/reading.tex` characters `[704,766)`.

```tex
\unsure{dèm.|dém.|dem.} par récurrence sur le nb des classes).
```

**C_packet** — `packets/020/C.tex` characters `[736,793)`.

```tex
\unsure{dém.|dem.} par récurrence sur le nb des classes).
```

**H** — `packets/020/H.tex` characters `[519,563)`.

```tex
dém.\ par
récurrence sur le nb des classes).
```

### TEX020-15 — Lemma Pi_I superscript and adjoining heading

Original C parts: `C020-R01-3`.

**A** — `out/readers/020/A/reading.tex` characters `[2634,2693)`.

```tex
\uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
```

**B** — `out/readers/020/B/reading.tex` characters `[2260,2319)`.

```tex
\uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
```

**C** — `out/readers/020/C/reading.tex` characters `[768,827)`.

```tex
\uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
```

**C_packet** — `packets/020/C.tex` characters `[795,854)`.

```tex
\uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
```

**H** — `packets/020/H.tex` characters `[704,758)`.

```tex
\emph{Lemme} Toute classe de $\Pi_I^0$ est de la forme
```

### TEX020-16 — Complete union/brace/formula candidate blocks

Original C parts: `C020-R08-1`.

A uses a generic bigcup plus two literal brace paths; B has three union and three brace commands; C has two union and two brace commands. These counts describe source commands only.

B full transplant source includes X setminus outside its inner TikZ. C comment mentions an operator annotation, while the complete inspected group contains no phantom or bigcup annotation command.

**A** — `out/readers/020/A/reading.tex` characters `[2694,3892)`.

```tex
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
```

**B** — `out/readers/020/B/reading.tex` characters `[2320,4199)`.

```tex
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
```

**C** — `out/readers/020/C/reading.tex` characters `[828,2805)`.

```tex
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
```

**C_packet** — `packets/020/C.tex` characters `[855,988)`.

```tex
$X\setminus\bigcup_{\alpha\in\deleted{\unsure{I}}K}(\overbrace{\Sigma_\alpha^+\cup E_\alpha}^{\inserted{\widehat{\Sigma}_\alpha^+}})$
```

**H** — `packets/020/H.tex` characters `[759,826)`.

```tex
\[
X\setminus\bigcup_{\alpha\in K}(\Sigma_\alpha^+\cup E_\alpha)
\]
```

### TEX020-17 — Union index predecessor/state candidates

Original C parts: `C020-R08-1`.

**A** — `out/readers/020/A/reading.tex` characters `[3260,3281)`.

```tex
\alpha\in\deleted{I}K
```

**B** — `out/readers/020/B/reading.tex` characters `[3303,3335)`.

```tex
\alpha\in\unsure{\deleted{I}K|K}
```

**C** — `out/readers/020/C/reading.tex` characters `[1999,2031)`.

```tex
\alpha\in\unsure{\deleted{I}K|K}
```

**C_packet** — `packets/020/C.tex` characters `[875,905)`.

```tex
\alpha\in\deleted{\unsure{I}}K
```

**H** — `packets/020/H.tex` characters `[781,792)`.

```tex
\alpha\in K
```

### TEX020-18 — Cancelled non vide with guide and adjoining words

A owns non vide and de I, only. B owns partie, non vide and de I, et. C owns partie, non vide and de I, with et outside.

A's rlap includes inserted{non vide}; A's phantom includes inserted{deleted{non vide}}. B/C place inserted outside a visible rlap and a phantom{deleted{non vide}}. Preserve the exact selected wrapper.

**A** — `out/readers/020/A/reading.tex` characters `[3915,4809)`.

```tex
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
```

**B** — `out/readers/020/B/reading.tex` characters `[4215,5210)`.

```tex
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
```

**C** — `out/readers/020/C/reading.tex` characters `[2821,4042)`.

```tex
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
```

**C_packet** — `packets/020/C.tex` characters `[989,1051)`.

```tex
où $K$ est une partie \inserted{\deleted{non vide}} de $I$, et
```

**H** — `packets/020/H.tex` characters `[916,975)`.

```tex
où $K$ est une partie \add{\uncertain{non vide}} de $I$, et
```

### TEX020-19 — Slanted margin-note source construction

A uses rotatebox{19} inside a makebox; B uses a TikZ node rotate=19; C uses rotatebox{23} inside a makebox. These literal source constructions are preserved without geometric evaluation.

**A** — `out/readers/020/A/reading.tex` characters `[4823,4968)`.

```tex
\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{19}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}}}\normalmarginpar
```

**B** — `out/readers/020/B/reading.tex` characters `[5283,5488)`.

```tex
\reversemarginpar\margin{\begin{tikzpicture}\node[rotate=19,anchor=base west,inner sep=0pt,outer sep=0pt] {\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}};\end{tikzpicture}}\normalmarginpar
```

**C** — `out/readers/020/C/reading.tex` characters `[4100,4245)`.

```tex
\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{23}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}}}\normalmarginpar
```

**C_packet** — `packets/020/C.tex` characters `[1062,1207)`.

```tex
\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{19}{\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}}}}\normalmarginpar
```

**H** — `packets/020/H.tex` characters `[1260,1314)`.

```tex
\marginal{$K$ est $\neq\emptyset$ si $I\neq\emptyset$}
```

### TEX020-20 — Cancelled on a and preceding quantifier

**A** — `out/readers/020/A/reading.tex` characters `[4969,5005)`.

```tex
$\forall\alpha\in K$, \deleted{on a}
```

**B** — `out/readers/020/B/reading.tex` characters `[5489,5525)`.

```tex
$\forall\alpha\in K$, \deleted{on a}
```

**C** — `out/readers/020/C/reading.tex` characters `[4246,4282)`.

```tex
$\forall\alpha\in K$, \deleted{on a}
```

**C_packet** — `packets/020/C.tex` characters `[1208,1244)`.

```tex
$\forall\alpha\in K$, \deleted{on a}
```

**H** — `packets/020/H.tex` characters `[976,1013)`.

```tex
$\forall\alpha\in K$, \struck{\ill{}}
```

### TEX020-21 — Reworked relation before pi_0

Original C parts: `C020-R09-1`.

A's complete-state candidates appear in its comment and overlay phantom; only locally qualified paths occupy the graphic payload. B prints the drawing and pipe-separated formal candidates inside one unsure wrapper. C prints only three formal candidates, using rightarrow rather than the to macro in A/B. Exact macro identity is retained.

**A** — `out/readers/020/A/reading.tex` characters `[5023,5874)`.

```tex
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
```

**B** — `out/readers/020/B/reading.tex` characters `[5543,6437)`.

```tex
% B_G05 literal reworked relation, followed inside the qualifier by its supported complete-state interpretations.
% Origin (943,1947), 0.25 pt per source pixel, baseline y=43; observed locus (944,1949,999,2004).
% M01 curved body, M02 middle shaft, M03 thin right head. No additional unqualified membership or arrow is drawn.
\mathrel{\unsure{\text{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,43)}]
\path[use as bounding box] (0,0) rectangle (62,66);
\draw[line width=0.70pt,line cap=round] (45,11) .. controls (35,-1) and (16,17) .. (7,32) .. controls (1,43) and (5,51) .. (15,55) .. controls (23,58) and (32,56) .. (39,51);
\draw[line width=0.75pt,line cap=round] (4,40) -- (43,32);
\draw[line width=0.40pt,line cap=round] (35,24) .. controls (38,16) and (51,29) .. (54,36) .. controls (56,34) and (54,20) .. (48,19);
\end{tikzpicture}}|\deleted{\Rightarrow}\in|\deleted{\to}\in|\in}}
```

**C** — `out/readers/020/C/reading.tex` characters `[4299,4361)`.

```tex
\unsure{\deleted{\Rightarrow}\in|\deleted{\rightarrow}\in|\in}
```

**C_packet** — `packets/020/C.tex` characters `[1261,1294)`.

```tex
\deleted{\unsure{\Rightarrow}}\in
```

**H** — `packets/020/H.tex` characters `[1015,1038)`.

```tex
\Sigma_\alpha^+\in\pi_0
```

### TEX020-22 — Lower E_alpha predecessor/state inside pi_0 argument

A qualifies E versus deleted-Sigma-plus-E. The other four inspected exact scopes contain E_alpha and no deleted predecessor macro.

**A** — `out/readers/020/A/reading.tex` characters `[5875,5929)`.

```tex
\pi_0(X\setminus{\unsure{E|\deleted{\Sigma}E}}_\alpha)
```

**B** — `out/readers/020/B/reading.tex` characters `[6438,6464)`.

```tex
\pi_0(X\setminus E_\alpha)
```

**C** — `out/readers/020/C/reading.tex` characters `[4361,4387)`.

```tex
\pi_0(X\setminus E_\alpha)
```

**C_packet** — `packets/020/C.tex` characters `[1294,1320)`.

```tex
\pi_0(X\setminus E_\alpha)
```

**H** — `packets/020/H.tex` characters `[1033,1059)`.

```tex
\pi_0(X\setminus E_\alpha)
```

### TEX020-23 — Final quantified hatted condition and parenthetical relation

All final text and displayed relations remain author-attributed transcription; this extraction performs no proof check.

**A** — `out/readers/020/A/reading.tex` characters `[5932,6131)`.

```tex
tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
```

**B** — `out/readers/020/B/reading.tex` characters `[6467,6666)`.

```tex
tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
```

**C** — `out/readers/020/C/reading.tex` characters `[4390,4589)`.

```tex
tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
```

**C_packet** — `packets/020/C.tex` characters `[1323,1522)`.

```tex
tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
```

**H** — `packets/020/H.tex` characters `[1062,1259)`.

```tex
tels que
$\forall\alpha,\beta\in K$, $\alpha\neq\beta$, on ait
$\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\emptyset$
($\Longleftrightarrow \Sigma_\alpha^+\cap\Sigma_\beta^+=\emptyset$).
```

## Extraction audit

All 287 exact stored source spans resolve, with unchanged input hashes. No reader file was modified.

Original C catalog: 11 actual rows, 13 primary parts. Its original row/part IDs remain intact in the JSON.
