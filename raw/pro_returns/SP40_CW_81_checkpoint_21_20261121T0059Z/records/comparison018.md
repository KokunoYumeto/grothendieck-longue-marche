## Reader A

\scanpage{18}
cette dernière, si $\operatorname{card}J=\operatorname{card}I-1=n-1$, on verra (par \unsure{récurrence}) que le cardinal de l'ens des classes est $(n-1)+1=n$.

Ceci posé, on voit d'abord que $E_i$ est dans
% G01: manual source origin (805,390), full-scan pixels; x right, y down.
% Words l'une, (unique), des/de, ces n occur only in this group.
\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,178)}]
\path[use as bounding box] (0,75) rectangle (710,205);
\node[anchor=base west,inner sep=0,outer sep=0] at (24,178) {l'une};
\node[anchor=base west,inner sep=0,outer sep=0] at (220,108) {\inserted{(unique)}};
\node[anchor=base west,inner sep=0,outer sep=0] at (286,178) {\unsure{des|de}};
\node[anchor=base west,inner sep=0,outer sep=0] at (452,178) {ces $n$};
% G01.P1: bent insertion guide, including its raised right endpoint.
\draw[line width=.35pt] (283,170) .. controls (270,120) and (321,128) .. (384,124) .. controls (426,124) and (462,114) .. (470,109) -- (470,104);
\end{tikzpicture}
classes, qui sont des ouverts. Soit $U_{J,i}$ la classe (ou ``composante'') qui contient $E_i$, et considérons les deux composantes $\Sigma_i^+,\Sigma_i^-$ de $X\setminus E_i$.

% G02: source origin (225,1145). The two manual rules replace a full-height tabular rule.
\figure{\begin{tikzpicture}[x=.008cm,y=-.008cm]
\path[use as bounding box] (0,0) rectangle (1420,265);
\node[anchor=base west,inner sep=0,outer sep=0] at (80,108) {\rlap{Lemme}\phantom{\uline{Lemme}}};
\node[anchor=base west,inner sep=0,outer sep=0] at (415,88) {Toute classe de $\Pi_{J\deleted{\unsure{i|j|,}}}^{\unsure{\circ|0}}$, distincte};
\node[anchor=base west,inner sep=0,outer sep=0] at (50,229) {de $U_{J,i}$, est contenue dans $\Sigma_i^+$ ou $\Sigma_i^-$};
% G02.P1: single slightly rising underline beneath Lemme.
\draw[line width=.5pt] (84,132) .. controls (174,123) and (248,122) .. (323,115);
% G02.P2: separate left rule starts below the first row and ends beside the second.
\draw[line width=.4pt] (31,104) .. controls (31,151) and (30,207) .. (35,238);
\end{tikzpicture}}

C'est presque une tautologie : Dire
% G03: source origin (220,1475). The following ordinary words classe donnée are outside this group once.
\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,99)}]
\path[use as bounding box] (0,20) rectangle (215,125);
\node[anchor=base west,inner sep=0,outer sep=0] at (83,99) {\rlap{la}\phantom{\deleted{la}}};
\node[anchor=base west,inner sep=0,outer sep=0] at (20,48) {\inserted{qu'une}};
% G03.P1: complete bent guide, with short right return.
\draw[line width=.35pt] (49,109) .. controls (76,77) and (110,67) .. (158,62) .. controls (176,59) and (195,47) .. (204,40) .. controls (206,36) and (202,35) .. (197,37);
% G03.P2: cancellation through la; no additional generic visible strike.
\draw[line width=.7pt] (85,95) -- (147,83);
\end{tikzpicture}
classe donnée
% G04: source origin (710,1445). U_alpha, de Pi_J, and baseline ne each occur once.
% The hook represented by G04.P2 is C's comma candidate; its punctuation/guide role stays unresolved.
\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,118)}]
\path[use as bounding box] (0,10) rectangle (330,140);
\node[anchor=base west,inner sep=0,outer sep=0] at (26,68) {\inserted{$U_{\unsure{\alpha|x}}$}};
\node[anchor=base west,inner sep=0,outer sep=0] at (112,53) {\inserted{de $\Pi_J^\circ$}};
\node[anchor=base west,inner sep=0,outer sep=0] at (89,118) {ne};
% G04.P1: rising left guide, bowed middle, and right return.
\draw[line width=.35pt] (49,110) .. controls (49,99) and (79,81) .. (105,68) .. controls (134,59) and (158,89) .. (211,79) .. controls (260,68) and (293,55) .. (301,43) -- (298,40);
% G04.P2: one qualified hook at fixed local origin (98,52), base-west anchored.
\node[anchor=base west,inner sep=0,outer sep=0] at (98,52) {\unsure{\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (16,20);
\draw[line width=.45pt] (1,3) .. controls (9,0) and (14,7) .. (7,16);
\end{tikzpicture}}};
\end{tikzpicture}
contient pas $\deleted{\Sigma}\overline{E_i}$ i.e. est $\ne U_{J,i}$, signifie que il existe un $j\in J$ tel que le $\Sigma_j^+\in\pi_0(X\setminus\deleted{\Sigma}E_{\unsure{j|J}})$
% G05: source origin (1405,1720); uncertain word, single literal cancellation, two detached points.
\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline={(0,50)}]
\path[use as bounding box] (0,0) rectangle (190,80);
\node[anchor=base west,inner sep=0,outer sep=0] at (0,50) {\rlap{\unsure{choisi|choisie}}\phantom{\deleted{\unsure{choisi|choisie}}}};
% G05.P1: cancellation run through the word.
\draw[line width=.65pt] (7,39) .. controls (55,40) and (109,41) .. (160,43);
% G05.P2-P3: detached points at fixed local origin (165,32); no character or role supplied.
\node[anchor=base west,inner sep=0,outer sep=0] at (165,32) {\unsure{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0pt]
\path[use as bounding box] (0,-8) rectangle (13,8);
\fill (2,2) ellipse [x radius=1,y radius=1.4];
\fill (8,-5) ellipse [x radius=.9,y radius=1.2];
\end{tikzpicture}}};
\end{tikzpicture}
``composant'' de cette classe \deleted{est} est l'élément du $\pi_0$ qui ne contient pas $E_i$; il est donc contenu dans l'un des
% G06: source origin (240,2080). Complete elements/insert/de group; following pi expression occurs outside once.
\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,176)}]
\path[use as bounding box] (0,90) rectangle (430,195);
\node[anchor=base west,inner sep=0,outer sep=0] at (30,180) {éléments};
\node[anchor=base west,inner sep=0,outer sep=0] at (155,133) {\inserted{(soit $\Sigma_i^-$)}};
\node[anchor=base west,inner sep=0,outer sep=0] at (351,168) {de};
% G06.P1: insertion guide with small raised right return.
\draw[line width=.35pt] (319,165) .. controls (320,141) and (359,143) .. (405,127) -- (409,124) -- (405,120);
\end{tikzpicture}
$\pi_0(X\setminus\Sigma_i)$, d'après l'étude du cas
% G07: source origin (245,2240); deleted word, raised replacement and comma occur once.
\begin{tikzpicture}[x=.008cm,y=-.008cm,baseline={(0,85)}]
\path[use as bounding box] (135,15) rectangle (335,110);
\node[anchor=base west,inner sep=0,outer sep=0] at (153,85) {\rlap{\unsure{deux}}\phantom{\deleted{\unsure{deux}}}};
\node[anchor=base west,inner sep=0,outer sep=0] at (145,49) {\inserted{$\operatorname{card}I=2$}};
\node[anchor=base west,inner sep=0,outer sep=0] at (300,95) {,};
% G07.P1: long slightly rising cancellation beneath the inserted formula.
\draw[line width=.65pt] (152,86) .. controls (193,79) and (252,84) .. (303,78);
\end{tikzpicture}
\deleted{\unsure{cela|OK}} \unsure{â|à} fortiori $U_\alpha\subset\Sigma_i^-$,
% G08: source origin (1440,2250). OK's rising stroke has unresolved joining/cancellation state.
\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline={(0,55)}]
\path[use as bounding box] (0,0) rectangle (210,95);
\node[anchor=base west,inner sep=0,outer sep=0] at (11,55) {\unsure{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0pt]
\path[use as bounding box] (0,-45) rectangle (85,8);
\node[anchor=base west,inner sep=0,outer sep=0] at (0,0) {\rlap{OK}\phantom{\deleted{OK}}};
% G08.P1: the visible rising crossing/joining stroke, drawn only here.
\draw[line width=.35pt] (0,-15) .. controls (24,-21) and (51,-32) .. (73,-40);
\end{tikzpicture}}};
\node[anchor=base west,inner sep=0,outer sep=0] at (127,61) {.};
% G08.P2: faint detached spot; shape, hand, surface origin and role remain qualified.
\node[anchor=base west,inner sep=0,outer sep=0] at (192,42) {\unsure{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (6,6);
\fill[gray] (2,2) ellipse [x radius=1.1,y radius=1.6];
\end{tikzpicture}}};
\end{tikzpicture}
% archive sheet number: 17



{
  "differences": [
    {
      "id": "A01",
      "location": "Opening word after cette",
      "C": "\\unsure{dernière}",
      "H": "dernière",
      "reading": "dernière",
      "evidence": "Looped d, low joined middle, separate i point and short grave; compressed final re remains readable.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "01_opening.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          415,
          80,
          650,
          150
        ]
      },
      "C_source_doubt_row": "C18-D01"
    },
    {
      "id": "A02",
      "location": "Opening parenthesis",
      "C": "\\unsure{récurrence}",
      "H": "récurrence",
      "reading": "\\unsure{récurrence}",
      "evidence": "Low shoulders and nearly point-like accent remain compressed after the one enlargement. Primary word retained without inventing another word.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "02_recurrence.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          595,
          185,
          1000,
          245
        ]
      },
      "C_source_doubt_row": "C18-D02"
    },
    {
      "id": "A03",
      "location": "l’ens des classes",
      "C": "l'\\unsure{ens}",
      "H": "l'ens.",
      "reading": "l'ens",
      "evidence": "Three joined low letters; the open gap to des has no visible abbreviation point.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "03_ens.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          390,
          292,
          660,
          350
        ]
      },
      "C_source_doubt_row": "C18-D03"
    },
    {
      "id": "A04",
      "location": "Following inserted (unique)",
      "C": "\\unsure{de|des}",
      "H": "des",
      "reading": "\\unsure{des|de}",
      "evidence": "Looped d followed by a separate small shoulder and long downturned tail. The tail supports des slightly more strongly, while de remains supported. H shares the selected primary.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "04_unique.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1080,
          530,
          1210,
          585
        ]
      },
      "C_source_doubt_row": "C18-D04"
    },
    {
      "id": "A05",
      "location": "After the disputed de/des",
      "C": "ces n",
      "H": "omitted",
      "reading": "ces $n$",
      "evidence": "Separate ces group beneath the descending q of the preceding line, then a separate n.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "04_unique.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1245,
          532,
          1480,
          582
        ]
      }
    },
    {
      "id": "A06",
      "location": "(unique) insertion guide",
      "C": "Insertion macro; no drawn guide",
      "H": "Insertion macro; no drawn guide",
      "reading": "G01.P1, same inserted wording",
      "evidence": "Long bowed rule below (unique), bending down at its left attachment and up at its right end. Adjacent l’une, des/de, ces n appear once in G01.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "04_unique.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1075,
          490,
          1285,
          565
        ]
      }
    },
    {
      "id": "A07",
      "location": "Before les deux composantes",
      "C": "\\unsure{considérons}",
      "H": "considérons",
      "reading": "considérons",
      "evidence": "c/o opening, tall d, separate rising accent, and compressed rons ending are visible.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "05_considerons.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          945,
          900,
          1240,
          965
        ]
      },
      "C_source_doubt_row": "C18-D05"
    },
    {
      "id": "A08",
      "location": "Lemma Pi upper ring",
      "C": "\\Pi^{\\unsure{\\circ|0}}",
      "H": "Pi^0",
      "reading": "\\Pi^{\\unsure{\\circ|0}}",
      "evidence": "Small closed round ring with a light centre. Its drawn form supports the circle first; zero remains supported. H’s zero survives as the explicit alternative.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "06_lemma.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1190,
          1160,
          1310,
          1230
        ]
      },
      "C_source_doubt_row": "C18-D06.b"
    },
    {
      "id": "A09",
      "location": "Lemma cancelled sign after subscript J",
      "C": "\\deleted{\\unsure{i|j|,}}",
      "H": "omitted",
      "reading": "\\deleted{\\unsure{i|j|,}}",
      "evidence": "Dark interrupted hooked descender follows J; dot/counter and exact predecessor do not settle. Cancellation and presence are clearer than its glyph.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "06_lemma.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1295,
          1220,
          1335,
          1265
        ]
      },
      "C_source_doubt_row": "C18-D06.a"
    },
    {
      "id": "A10",
      "location": "Lemma left rule and heading underline",
      "C": "Full-height tabular left rule; underlined Lemme",
      "H": "Underlined Lemme; no left rule",
      "reading": "G02.P1 underline; G02.P2 short lower left rule",
      "evidence": "Underline is single and rises slightly to the right. Separate vertical rule starts below the first text row, ending beside the second. C’s full-height tabular rule gives a longer upper span. Underline macro conversion itself carries no correction.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "06_lemma.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          250,
          1190,
          560,
          1390
        ]
      }
    },
    {
      "id": "A11",
      "location": "End of lemma after Sigma_i^-",
      "C": "No stop",
      "H": "Full stop",
      "reading": "No terminal stop",
      "evidence": "Visible endpoint space after the final index has no independent punctuation point. The index point remains part of i.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "06_lemma.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1530,
          1265,
          1645,
          1385
        ]
      }
    },
    {
      "id": "A12",
      "location": "After tautologie colon",
      "C": "\\unsure{Dire}",
      "H": "Dire",
      "reading": "Dire",
      "evidence": "Tall D has worked lower loops; the separate i strokes and low re continuation remain readable. No separate predecessor character is supplied from the retracing.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "07_dire.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1400,
          1385,
          1525,
          1465
        ]
      },
      "C_source_doubt_row": "C18-D07"
    },
    {
      "id": "A13",
      "location": "qu’une / cancelled la correction",
      "C": "Inserted qu’une; deleted la; no literal paths",
      "H": "Same correction state; no literal paths",
      "reading": "G03.P1 complete guide and G03.P2 literal cancellation",
      "evidence": "The guide bends from the left baseline up under the inserted word and ends with a short right return; la has one strongly rising cancellation run. No second visible generic deletion rule is added.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "08_quune.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          240,
          1500,
          435,
          1590
        ]
      }
    },
    {
      "id": "A14",
      "location": "Raised U subscript after donnée",
      "C": "U_{\\unsure{\\alpha|x}}",
      "H": "U_alpha",
      "reading": "U_{\\unsure{\\alpha|x}}",
      "evidence": "Small closed/crossed form attached to U; alpha remains stronger but x remains supported by the crossed right strokes. H shares the primary.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "09_insert_u.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          735,
          1465,
          800,
          1525
        ]
      },
      "C_source_doubt_row": "C18-D08"
    },
    {
      "id": "A15",
      "location": "Raised Pi ring in the same insertion",
      "C": "Pi_J^circ",
      "H": "Pi_J^0",
      "reading": "Pi_J^circ, recurring circle/zero uncertainty recorded",
      "evidence": "The second raised ring is small, rounded and hooked at its upper-left. This occurrence was inspected independently. Recurrence rule prints the first candidate unmarked; H’s zero remains supported as an alternative.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "09_insert_u.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          885,
          1458,
          965,
          1525
        ]
      }
    },
    {
      "id": "A16",
      "location": "U_alpha / de Pi_J insertion and baseline ne",
      "C": "Inserted wording; no literal guide",
      "H": "Inserted wording; no literal guide",
      "reading": "G04.P1 and G04.P2, with ne once",
      "evidence": "Main guide rises from before ne, bows below the raised formula, and returns upward at its right endpoint. Complete words are included once; no extra un is produced.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "09_insert_u.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          735,
          1460,
          1020,
          1570
        ]
      }
    },
    {
      "id": "A17",
      "location": "Hook after raised U_alpha",
      "C": "Printed comma",
      "H": "No comma",
      "reading": "Qualified literal hook G04.P2; punctuation/guide attachment unresolved",
      "evidence": "The short comma-like hook joins the long guide near its left upper turn. The actual hook is preserved once, rather than a comma plus a duplicate path. No established punctuation role is assigned.",
      "confidence": "low",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "09_insert_u.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          805,
          1495,
          825,
          1520
        ]
      },
      "physical_parent": "A16"
    },
    {
      "id": "A18",
      "location": "Before baseline ne contient",
      "C": "No extra cancelled un",
      "H": "\\struck{un} ne",
      "reading": "ne only",
      "evidence": "The baseline has one small joined ne group. No separate written un or cancellation at that locus is isolated; the rising line belongs to the insertion guide above it.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "09_insert_u.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          780,
          1520,
          900,
          1570
        ]
      }
    },
    {
      "id": "A19",
      "location": "Predecessor within first corrected E_i",
      "C": "\\deleted{\\unsure{\\Sigma}}",
      "H": "Omitted predecessor",
      "reading": "\\deleted{\\Sigma}",
      "evidence": "Two surviving internal oblique runs and the lower return form the angular predecessor; heavier left stem and three horizontal E strokes overlay it.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "10_bar_e.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1300,
          1495,
          1375,
          1565
        ]
      },
      "C_source_doubt_row": "C18-D09.a"
    },
    {
      "id": "A20",
      "location": "Upper rule over first corrected E_i",
      "C": "\\unsure{\\overline{E_i}|E_i}",
      "H": "E_i",
      "reading": "\\overline{E_i}",
      "evidence": "A separate upper horizontal has white space below it; the lower horizontal is attached to the E stem. The visible upper rule is retained as an overbar. This resolves bar presence, without assigning a closure operation or writing chronology.",
      "confidence": "high",
      "kind": "misread symbol or index",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "10_bar_e.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1300,
          1485,
          1380,
          1565
        ]
      },
      "C_source_doubt_row": "C18-D14"
    },
    {
      "id": "A21",
      "location": "After signifie",
      "C": "que il",
      "H": "qu'il",
      "reading": "que il",
      "evidence": "The low que group and subsequent separate il are both visible with a gap.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1030,
          1600,
          1195,
          1680
        ]
      }
    },
    {
      "id": "A22",
      "location": "Before Sigma_j^+",
      "C": "le",
      "H": "la",
      "reading": "le",
      "evidence": "Tall looped l ends in a low rightward e run; no separate a bowl is visible.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "11_formula.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          820,
          1735,
          890,
          1805
        ]
      }
    },
    {
      "id": "A23",
      "location": "Predecessor within corrected E_j",
      "C": "\\deleted{\\unsure{\\Sigma}}",
      "H": "Omitted predecessor",
      "reading": "\\deleted{\\Sigma}",
      "evidence": "Upper and lower internal slanting returns survive beneath the heavier E; no separate extra overbar appears above this corrected letter.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "11_formula.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1270,
          1725,
          1325,
          1788
        ]
      },
      "C_source_doubt_row": "C18-D09.b"
    },
    {
      "id": "A24",
      "location": "Second corrected E subscript",
      "C": "E_{\\unsure{j|J}}",
      "H": "E_j",
      "reading": "E_{\\unsure{j|J}}",
      "evidence": "Long nearly vertical downstroke with a short leftward bottom hook; no isolated dot settles j against J. H shares the primary j.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "11_formula.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1302,
          1750,
          1335,
          1815
        ]
      },
      "C_source_doubt_row": "C18-D09.c"
    },
    {
      "id": "A25",
      "location": "Cancelled word after formula",
      "C": "\\deleted{\\unsure{choisi}}",
      "H": "\\struck{choisie}",
      "reading": "\\deleted{\\unsure{choisi|choisie}}",
      "evidence": "c/h opening and dotted short strokes survive. The heavy crossing line obscures the ending; choisi is stronger, with choisie explicitly retained. H’s reading is an alternative, not a conclusively excluded word.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "11_formula.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1405,
          1715,
          1585,
          1785
        ]
      },
      "C_source_doubt_row": "C18-D10"
    },
    {
      "id": "A26",
      "location": "Cancellation run and two points after chosen word",
      "C": "Generic deletion; no separate points",
      "H": "Generic deletion; no separate points",
      "reading": "G05.P1 and locally qualified G05.P2–P3",
      "evidence": "One long cancellation run extends through the word; two small detached points lie beyond it on a rising alignment. Their character, hand, role and surface origin remain unsettled. Word i dots are not drawn a second time.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "11_formula.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1405,
          1715,
          1590,
          1785
        ]
      },
      "physical_parent": "A25"
    },
    {
      "id": "A27",
      "location": "Quoted proof word",
      "C": "\\unsure{composant|composante}",
      "H": "composante",
      "reading": "composant",
      "evidence": "The terminal t cross runs rightward and ends before the closing pair of quotation strokes; no further e body is visible.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "12_quoted.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          235,
          1880,
          590,
          1980
        ]
      },
      "C_source_doubt_row": "C18-D11"
    },
    {
      "id": "A28",
      "location": "Live word after cancelled est",
      "C": "\\deleted{est} est",
      "H": "\\struck{est} soit",
      "reading": "\\deleted{est} est",
      "evidence": "Right-hand word begins with a small e loop followed by s and tall crossed t; no dotted i is isolated. Left est is separately crossed.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "13_double_est.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1200,
          1845,
          1480,
          1920
        ]
      }
    },
    {
      "id": "A29",
      "location": "Before pi_0 in l’élément phrase",
      "C": "du",
      "H": "de",
      "reading": "du",
      "evidence": "Low joined u ending follows d; read on supplied half b in the full phrase.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          520,
          2005,
          630,
          2060
        ]
      }
    },
    {
      "id": "A30",
      "location": "(soit Sigma_i^-) insertion",
      "C": "Insertion macro, no literal guide",
      "H": "Insertion macro, no literal guide",
      "reading": "G06.P1; éléments, insertion and de once",
      "evidence": "Bent guide rises from the gap following éléments, runs under the inserted parenthesis and ends in a small upward return. de remains present below/right.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "14_soit.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          390,
          2150,
          660,
          2265
        ]
      }
    },
    {
      "id": "A31",
      "location": "Cancelled word after bottom cas",
      "C": "\\deleted{\\unsure{deux}}",
      "H": "Omitted deleted word",
      "reading": "\\deleted{\\unsure{deux}}",
      "evidence": "A low loop/ascender and several small rises survive beneath the long crossing stroke. The candidate deux remains uncertain. H’s raised replacement is read with this one physical correction cluster.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "15_card.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          390,
          2290,
          555,
          2345
        ]
      },
      "C_source_doubt_row": "C18-D12"
    },
    {
      "id": "A32",
      "location": "Raised card I=2 and long lower cancellation",
      "C": "Inserted card I=2; ordinary deletion",
      "H": "Baseline card I=2",
      "reading": "G07 with formula raised and literal cancellation G07.P1; comma once",
      "evidence": "card I=2 sits above the crossed baseline word; the crossing run extends almost to the following comma. H insertion/placement difference is grouped with A31.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "15_card.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          380,
          2260,
          570,
          2348
        ]
      },
      "physical_parent": "A31"
    },
    {
      "id": "A33",
      "location": "Cancelled bottom word before fortiori",
      "C": "\\deleted{\\unsure{OK|cela}}",
      "H": "\\struck{et}",
      "reading": "\\deleted{\\unsure{cela|OK}}",
      "evidence": "Low left loops, a tall looping middle stroke and a final triangular/looped body favour cela; crossed strokes leave OK supported. H’s short et has no secure matching full body here.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "16_bottom.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          650,
          2265,
          805,
          2330
        ]
      },
      "C_source_doubt_row": "C18-D13.a"
    },
    {
      "id": "A34",
      "location": "Accent on a before fortiori",
      "C": "\\unsure{â|à}",
      "H": "à",
      "reading": "\\unsure{â|à}",
      "evidence": "Tiny raised roof-like dark shape over a; a bent grave remains supported. H’s à survives as the alternative, and the new reading is qualified.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "16_bottom.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          830,
          2278,
          890,
          2330
        ]
      },
      "C_source_doubt_row": "C18-D13.b"
    },
    {
      "id": "A35",
      "location": "Final OK state",
      "C": "Live OK",
      "H": "Live OK",
      "reading": "Locally qualified G08: joining flourish/live primary; cancellation alternative",
      "evidence": "A rising stroke crosses/connects the O and K. Its shape is visible; its writing-state role remains unresolved. Same primary live reading plus editorial qualification alone creates no H count.",
      "confidence": "low",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "17_final_u.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1445,
          2257,
          1540,
          2325
        ]
      }
    },
    {
      "id": "A36",
      "location": "Final OK rising stroke",
      "C": "No literal rising path",
      "H": "No literal rising path",
      "reading": "G08.P1 once, hidden deletion annotation only",
      "evidence": "Observed rising run is drawn through the one label; no second generic cancellation rule is added. This geometry and A35 refer to one physical cluster.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "17_final_u.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1445,
          2257,
          1540,
          2325
        ]
      },
      "physical_parent": "A35"
    },
    {
      "id": "A37",
      "location": "Faint point near lower-right blank edge",
      "C": "Omitted",
      "H": "Omitted",
      "reading": "Locally qualified gray spot G08.P2",
      "evidence": "A compact faint gray point is visible above/right of the final period, distinct in position from that dark period. Its character, hand, role and surface origin remain unestablished.",
      "confidence": "low",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "17_final_u.png",
      "bbox": {
        "coordinate_system": "original full scan; origin top-left, x right, y down",
        "coordinates": [
          1628,
          2286,
          1642,
          2303
        ]
      }
    }
  ],
  "doubts": [
    {
      "location": "Opening parenthesis",
      "reading": "\\unsure{récurrence}",
      "alternatives": [],
      "confidence": "medium",
      "reason": "Low shoulders and nearly point-like accent remain compressed after the one enlargement. Primary word retained without inventing another word.",
      "crop": "02_recurrence.png"
    },
    {
      "location": "Following inserted (unique)",
      "reading": "\\unsure{des|de}",
      "alternatives": [
        "de"
      ],
      "confidence": "low",
      "reason": "Looped d followed by a separate small shoulder and long downturned tail. The tail supports des slightly more strongly, while de remains supported. H shares the selected primary.",
      "crop": "04_unique.png"
    },
    {
      "location": "Lemma Pi upper ring",
      "reading": "\\Pi^{\\unsure{\\circ|0}}",
      "alternatives": [
        "0"
      ],
      "confidence": "low",
      "reason": "Small closed round ring with a light centre. Its drawn form supports the circle first; zero remains supported. H’s zero survives as the explicit alternative.",
      "crop": "06_lemma.png"
    },
    {
      "location": "Lemma cancelled sign after subscript J",
      "reading": "\\deleted{\\unsure{i|j|,}}",
      "alternatives": [
        "j",
        ","
      ],
      "confidence": "low",
      "reason": "Dark interrupted hooked descender follows J; dot/counter and exact predecessor do not settle. Cancellation and presence are clearer than its glyph.",
      "crop": "06_lemma.png"
    },
    {
      "location": "Raised U subscript after donnée",
      "reading": "U_{\\unsure{\\alpha|x}}",
      "alternatives": [
        "x"
      ],
      "confidence": "medium",
      "reason": "Small closed/crossed form attached to U; alpha remains stronger but x remains supported by the crossed right strokes. H shares the primary.",
      "crop": "09_insert_u.png"
    },
    {
      "location": "Raised Pi ring in the same insertion",
      "reading": "Pi_J^circ, recurring circle/zero uncertainty recorded",
      "alternatives": [
        "0"
      ],
      "confidence": "low",
      "reason": "The second raised ring is small, rounded and hooked at its upper-left. This occurrence was inspected independently. Recurrence rule prints the first candidate unmarked; H’s zero remains supported as an alternative.",
      "crop": "09_insert_u.png"
    },
    {
      "location": "Hook after raised U_alpha",
      "reading": "Qualified literal hook G04.P2; punctuation/guide attachment unresolved",
      "alternatives": [
        "comma",
        "guide curl"
      ],
      "confidence": "low",
      "reason": "The short comma-like hook joins the long guide near its left upper turn. The actual hook is preserved once, rather than a comma plus a duplicate path. No established punctuation role is assigned.",
      "crop": "09_insert_u.png"
    },
    {
      "location": "Second corrected E subscript",
      "reading": "E_{\\unsure{j|J}}",
      "alternatives": [
        "J"
      ],
      "confidence": "low",
      "reason": "Long nearly vertical downstroke with a short leftward bottom hook; no isolated dot settles j against J. H shares the primary j.",
      "crop": "11_formula.png"
    },
    {
      "location": "Cancelled word after formula",
      "reading": "\\deleted{\\unsure{choisi|choisie}}",
      "alternatives": [
        "choisie"
      ],
      "confidence": "low",
      "reason": "c/h opening and dotted short strokes survive. The heavy crossing line obscures the ending; choisi is stronger, with choisie explicitly retained. H’s reading is an alternative, not a conclusively excluded word.",
      "crop": "11_formula.png"
    },
    {
      "location": "Cancelled word after bottom cas",
      "reading": "\\deleted{\\unsure{deux}}",
      "alternatives": [],
      "confidence": "low",
      "reason": "A low loop/ascender and several small rises survive beneath the long crossing stroke. The candidate deux remains uncertain. H’s raised replacement is read with this one physical correction cluster.",
      "crop": "15_card.png"
    },
    {
      "location": "Cancelled bottom word before fortiori",
      "reading": "\\deleted{\\unsure{cela|OK}}",
      "alternatives": [
        "OK"
      ],
      "confidence": "low",
      "reason": "Low left loops, a tall looping middle stroke and a final triangular/looped body favour cela; crossed strokes leave OK supported. H’s short et has no secure matching full body here.",
      "crop": "16_bottom.png"
    },
    {
      "location": "Accent on a before fortiori",
      "reading": "\\unsure{â|à}",
      "alternatives": [
        "à"
      ],
      "confidence": "low",
      "reason": "Tiny raised roof-like dark shape over a; a bent grave remains supported. H’s à survives as the alternative, and the new reading is qualified.",
      "crop": "16_bottom.png"
    },
    {
      "location": "Final OK state",
      "reading": "Locally qualified G08: joining flourish/live primary; cancellation alternative",
      "alternatives": [
        "cancellation"
      ],
      "confidence": "low",
      "reason": "A rising stroke crosses/connects the O and K. Its shape is visible; its writing-state role remains unresolved. Same primary live reading plus editorial qualification alone creates no H count.",
      "crop": "17_final_u.png"
    },
    {
      "location": "Faint point near lower-right blank edge",
      "reading": "Locally qualified gray spot G08.P2",
      "alternatives": [
        "surface-origin point rather than handwriting"
      ],
      "confidence": "low",
      "reason": "A compact faint gray point is visible above/right of the final period, distinct in position from that dark period. Its character, hand, role and surface origin remain unestablished.",
      "crop": "17_final_u.png"
    },
    {
      "location": "Detached pair after cancelled choisi/choisie",
      "reading": "two literal points",
      "alternatives": [],
      "confidence": "low",
      "reason": "Shape retained; character, hand, role, and surface origin unresolved.",
      "crop": "11_formula.png"
    }
  ],
  "notes": {
    "page_content": "Continuation concerning a partition, cardinalities, E_i and two signed Sigma components; an underlined Lemme and a prose argument with several corrections and raised additions.",
    "author_words": [
      "on verra (par récurrence)",
      "C’est presque une tautologie",
      "OK"
    ],
    "author_uncertainty": "No explicit question mark or verbal admission of doubt was identified. The quoted phrases are transcribed wording; none is treated as an independently checked result.",
    "title_date_page_counts": "Underlined Lemme is a local heading. No written date or manuscript page number was identified. Lower-left archive numeral 17 appears only in the archive comment. H page 17 is packet indexing apparatus, not an added second physical page number.",
    "mathematics_led_reading_decisions": "No computation or theorem check was performed. X\\setminus\\Sigma_i, que il, le, and du are retained from visible ink. No grammatical or mathematical repair is supplied.",
    "H_apparatus": "H’s note proposing X\\setminus E_i is editorial apparatus; the transcribed X\\setminus\\Sigma_i is one physical occurrence. H emph Lemme corresponds to the same emphasis reading as the single drawn underline.",
    "graphic_state": "Final OK is read as a live label first, with cancellation retained as a state alternative because the rising crossing/joining stroke is not settled. The visible shape is drawn once. The deleted bottom word and final OK are separate physical loci.",
    "boundary_limits": [
      "Crop06 cuts the low end of the lemma U_J,i subscript at its lower edge; that full index was already read on the successfully delivered supplied half b. The rule endpoints and target ring/suffix remain within crop06. No recrop was made.",
      "The bottom f descender meets the physical paper edge; crop16 includes the edge and all available ink. No continuation below the paper is supplied."
    ],
    "source_choices_without_lexical_difference": [
      "Physical line wraps are joined except the two-line lemma drawing.",
      "All guide-adjoining text occurs once: G01 l’une/(unique)/des-de/ces n; G03 qu’une/la then outside classe donnée; G04 raised U/de/Pi and baseline ne; G06 éléments/(soit Sigma)/de followed by one pi expression; G07 deleted word/raised card/comma.",
      "The C comma candidate at the left of the raised U guide is represented as the actual qualified hook once, with no duplicate comma node.",
      "G02 underline is a literal path over a hidden uline dimensional annotation; generic macro conversion is not counted separately.",
      "Hidden deleted copies in G03/G05/G07/G08 supply annotation/dimensions; only the selected visible paths draw those cancellation/crossing runs.",
      "The final gray spot is retained as a qualified shape, not a supplied character."
    ],
    "notation_table_status": "Packet notation rows and slips/abbreviations were read as such, not counted as extra C doubts. Fourteen actual doubtful-reading source rows are mapped below."
  },
  "notation": [
    {
      "location": "opening",
      "reading": "\\operatorname{card}J=\\operatorname{card}I-1=n-1",
      "evidence": "small c; capital J and serifed I; straight middle hyphens"
    },
    {
      "location": "opening abbreviation",
      "reading": "ens",
      "evidence": "three joined letters with no visible stop; expansion ensemble is not transcribed"
    },
    {
      "location": "definitions and lemma",
      "reading": "U_{J,i}",
      "evidence": "separate subscript comma and i point; the lemma crop’s clipped low J is covered by half b"
    },
    {
      "location": "two Pi occurrences",
      "reading": "\\unsure{\\circ|0} first, \\circ later",
      "evidence": "both small closed raised rings independently inspected; role/glyph alternative retained at first occurrence"
    },
    {
      "location": "raised U then final U",
      "reading": "U_{\\unsure{\\alpha|x}}; U_\\alpha",
      "evidence": "first crossed loop retains x alternative; final subscript has a low loop and right return, locally read alpha; same primary printed unmarked under recurrence convention"
    },
    {
      "location": "both E corrections",
      "reading": "\\deleted{\\Sigma}E",
      "evidence": "surviving internal diagonal returns under heavier E strokes at each separate locus"
    },
    {
      "location": "first corrected E",
      "reading": "\\overline{E_i}",
      "evidence": "distinct upper horizontal above the stem-attached E head; mathematical role not assigned"
    },
    {
      "location": "bottom before fortiori",
      "reading": "\\unsure{â|à}",
      "evidence": "small roof-like raised mark; bent-grave alternative retained"
    },
    {
      "location": "proof endpoint",
      "reading": "\\subset",
      "evidence": "open left-facing curved wedge with no lower equality rule"
    },
    {
      "location": "top quoted parenthesis / lower quoted word",
      "reading": "``composante'' / ``composant''",
      "evidence": "each pair of opening/closing quote strokes checked; lower t ends without a further e body"
    },
    {
      "location": "proof abbreviation and bottom label",
      "reading": "i.e.; OK",
      "evidence": "both abbreviated points visible in i.e.; final label glyphs OK clear, state separately qualified"
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "No missing convention blocked the reading. The distinction between a comma-like hook and its connected insertion-guide curl remains an ink-role doubt; this return preserves the whole shape once.",
    "The manuscript S row supplies no matching explicit Sigma/U closure example on this page. The E_i upper rule is decided under its independent C18-D14 source doubt."
  ]
}

## Reader B

\scanpage{18}
cette dernière, si $\operatorname{card}J=\operatorname{card}I-1=n-1$, on verra (par \unsure{rècurrence|récurrence}) que le cardinal de l'ens des classes est $(n-1)+1=n$.

Ceci posé, on voit d'abord que $E_i$ est dans
% G01: full-scan origin (820,465), x right/y down; manual geometry.
\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g01base)]
\path[use as bounding box] (0,0) rectangle (670,145);
\coordinate (g01base) at (0,115);
\begin{scope}[shift={(-820,-465)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (830,574) {l'une};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1024,505) {\inserted{(unique)}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1100,574) {\unsure{des|de} ces $n$};
\draw[line width=.35pt] (1089,559) .. controls (1075,521) and (1137,517) .. (1202,516) .. controls (1240,511) and (1271,507) .. (1278,498);
\end{scope}
\end{tikzpicture}
classes, qui sont des ouverts. Soit $U_{J,i}$ la classe (ou ``\unsure{composante|composant}'') qui contient $E_i$, et considérons les deux composantes $\Sigma_i^+,\Sigma_i^-$ de $X\setminus E_i$.

% G02: complete lemma group. Full-scan origin (244,1145).
% The underline and the left rule each occur once. The left rule begins
% below the first textual line; its observed endpoints are preserved.
\figure{\begin{tikzpicture}[x=.085mm,y=-.085mm,baseline=(g02base)]
\path[use as bounding box] (0,0) rectangle (1400,255);
\coordinate (g02base) at (0,238);
\begin{scope}[shift={(-244,-1145)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (305,1248) {\rlap{Lemme}\phantom{\uline{Lemme}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (645,1238) {Toute classe de $\Pi_{J\unsure{\deleted{j}|\deleted{i}|\deleted{,}|j}}^{\unsure{\circ|0}}$, distincte};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (275,1382) {de $U_{J,i}$, est contenue dans $\Sigma_i^+$ ou $\Sigma_i^-$};
\draw[line width=.45pt] (308,1275) .. controls (390,1270) and (471,1264) .. (550,1258);
\draw[line width=.35pt] (255,1247) .. controls (256,1290) and (257,1340) .. (259,1385);
\end{scope}
\end{tikzpicture}}

C'est presque une tautologie : Dire
% G03: whole adjoining correction group, origin (225,1465).
% The short hook after U_alpha belongs to G03b, with no separate comma.
\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g03base)]
\path[use as bounding box] (0,-28) rectangle (925,140);
\coordinate (g03base) at (0,111);
\begin{scope}[shift={(-225,-1465)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (301,1576) {\deleted{la}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (244,1523) {\inserted{qu'une}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (390,1576) {classe donnée};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (738,1510) {\inserted{$U_{\unsure{\alpha|x}}$ de $\Pi_J^\circ$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (801,1553) {ne contient};
% G03a: qu'une guide, one connected run with a hooked upper endpoint.
\draw[line width=.35pt] (271,1580) .. controls (279,1551) and (307,1541) .. (343,1538) .. controls (376,1535) and (414,1527) .. (423,1517) .. controls (426,1512) and (418,1510) .. (414,1513);
% G03b: second guide and its connected small hook, two path commands.
\draw[line width=.35pt] (760,1553) .. controls (759,1538) and (794,1517) .. (813,1510) .. controls (838,1511) and (861,1528) .. (891,1525) .. controls (938,1521) and (992,1501) .. (1011,1488);
\draw[line width=.35pt] (813,1510) .. controls (823,1501) and (817,1498) .. (811,1501);
\end{scope}
\end{tikzpicture}
pas $\deleted{\Sigma}$\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g04base)]
% G04: corrected E_i and the separate upper stroke. Outer origin
% (1308,1480); inner overmark origin (1324,1492), baseline y=12.
% Closure-bar/remnant role is unresolved; the visible stroke is retained
% once, including its short returning right end, under local unsure.
\path[use as bounding box] (0,0) rectangle (85,85);
\coordinate (g04base) at (0,67);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,67) {$E_i$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (16,24) {\unsure{\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g04markbase)]
\path[use as bounding box] (0,0) rectangle (55,12);
\coordinate (g04markbase) at (0,12);
\draw[line width=.45pt] (0,6) .. controls (17,5) and (34,6) .. (47,6) -- (31,10) -- (43,6);
\end{tikzpicture}}};
\end{tikzpicture}
i.e. est $\ne U_{J,i}$, signifie que il existe un $j\in J$ tel que le $\Sigma_j^+\in\pi_0(X\setminus\deleted{\Sigma}E_{\unsure{j|J}})$
% G05: crossed word plus the two additional upper/right points.
% Outer origin (1408,1712); dots' fixed local origin (1569,1737).
\begin{tikzpicture}[x=.07mm,y=-.07mm,baseline=(g05base)]
\path[use as bounding box] (0,0) rectangle (190,100);
\coordinate (g05base) at (0,70);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,70) {\deleted{\unsure{choisi|choisie}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (161,47) {\unsure{\begin{tikzpicture}[x=.07mm,y=-.07mm,baseline=(g05markbase)]
\path[use as bounding box] (0,0) rectangle (20,22);
\coordinate (g05markbase) at (0,22);
\fill (5,16) circle[radius=1.2];
\fill (10,6) circle[radius=1.2];
\end{tikzpicture}}};
\end{tikzpicture}
``\unsure{composant|composante}'' de cette classe \deleted{est} est l'\unsure{élêment|élément} du $\pi_0$ qui ne contient pas $E_i$; il est donc contenu dans l'un des
% G06: whole éléments / (soit Sigma_i^-) / de group, origin (251,2160).
\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g06base)]
\path[use as bounding box] (0,0) rectangle (470,126);
\coordinate (g06base) at (0,95);
\begin{scope}[shift={(-251,-2160)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (265,2255) {éléments};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (399,2201) {\inserted{(soit $\Sigma_i^-$)}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (595,2248) {de};
\draw[line width=.35pt] (560,2251) .. controls (563,2228) and (599,2215) .. (646,2205) .. controls (655,2202) and (653,2199) .. (647,2197);
\end{scope}
\end{tikzpicture}
$\pi_0(X\setminus\Sigma_i)$, d'après l'étude du cas
% G07: lower correction, origin (382,2265). Actual cancellation drawn
% once; the invisible deleted copy supplies annotation/dimensions only.
\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g07base)]
\path[use as bounding box] (0,0) rectangle (190,80);
\coordinate (g07base) at (0,59);
\begin{scope}[shift={(-382,-2265)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (395,2323) {\rlap{\unsure{deux}}\phantom{\deleted{\unsure{deux}}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (389,2297) {\inserted{$\operatorname{card}I=2$}};
\draw[line width=.55pt] (395,2325) .. controls (443,2318) and (509,2322) .. (556,2318);
\end{scope}
\end{tikzpicture},
\deleted{\unsure{OK|cela|et}} \unsure{â|à} fortiori $U_\alpha\subset\Sigma_i^-$,
% G08: final OK and its rising transverse stroke, origin (1450,2255).
% Whole-state candidates: live OK; deleted OK. The local unsure retains
% this unresolved state; no extra generic cancellation line is drawn.
\unsure{\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g08base)]
\path[use as bounding box] (0,0) rectangle (95,85);
\coordinate (g08base) at (0,70);
\begin{scope}[shift={(-1450,-2255)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1455,2323) {\rlap{OK}\phantom{\deleted{OK}}};
\draw[line width=.3pt] (1452,2293) .. controls (1470,2287) and (1497,2279) .. (1534,2264);
\end{scope}
\end{tikzpicture}}.
% archive sheet number: 17



{
  "differences": [
    {
      "id": "B01",
      "location": "opening dernière",
      "C": "\\unsure{dernière}",
      "H": "dernière",
      "reading": "dernière",
      "evidence": "Looped d, low r/n joins, separate i dot and descending-right grave, followed by the comma; reading resolved locally.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop01_opening.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          224,
          58,
          793,
          165
        ]
      },
      "C_source_doubt_row": "C18-R01"
    },
    {
      "id": "B02",
      "location": "parenthesis after verra",
      "C": "\\unsure{récurrence}",
      "H": "récurrence",
      "reading": "\\unsure{rècurrence|récurrence}",
      "evidence": "The word remains compressed. The small detached accent has a descending-right hook; grave is the selected visible candidate, acute remains supported. No spelling repair is made.",
      "confidence": "medium",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop02_recurrence.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          440,
          165,
          1060,
          285
        ]
      },
      "C_source_doubt_row": "C18-R02",
      "qualification": "H survives as the second candidate; this is a qualified reading difference."
    },
    {
      "id": "B03",
      "location": "l’ens des classes",
      "C": "l'\\unsure{ens}",
      "H": "l'ens.\\ des classes",
      "reading": "l’ens",
      "evidence": "Three joined letters and a long hooked final stroke are followed by clean intervening space; no abbreviation point appears.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crop03_ens.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          373,
          280,
          810,
          373
        ]
      },
      "C_source_doubt_row": "C18-R03"
    },
    {
      "id": "B04",
      "location": "word following raised (unique)",
      "C": "\\unsure{de|des}",
      "H": "des",
      "reading": "\\unsure{des|de}",
      "evidence": "The low run has a final hooked continuation resembling s; the endpoint also permits de. Primary order reversed from C without resolving the doubt.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop04_unique.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1080,
          530,
          1195,
          590
        ]
      },
      "C_source_doubt_row": "C18-R04"
    },
    {
      "id": "B05",
      "location": "between de/des and classes",
      "C": "ces $n$",
      "H": "[omitted]",
      "reading": "ces $n$",
      "evidence": "A distinct ces group appears under the long descender from que, followed by a separate n before the next physical line classes.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop04_unique.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1260,
          527,
          1480,
          591
        ]
      }
    },
    {
      "id": "B06",
      "location": "raised (unique), guide G01",
      "C": "l'une \\inserted{(unique)}",
      "H": "l'une \\add{(unique)}",
      "reading": "Same insertion, with the full bent guide",
      "evidence": "The guide begins below/left of de/des, bends upward beneath (unique), and ends with an upturned right end. Current witnesses encode the insertion but omit this independent path.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop04_unique.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1080,
          490,
          1284,
          565
        ]
      },
      "physical_parent": "unique-insertion"
    },
    {
      "id": "B07",
      "location": "upper quoted word",
      "C": "``composante''",
      "H": "“composante”",
      "reading": "``\\unsure{composante|composant}''",
      "evidence": "The long terminal curved return supports composante; attachment of that return to t leaves composant available. Both opening and closing quote pairs were seen.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crop05_upper_quote.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          976,
          754,
          1324,
          832
        ]
      },
      "qualification": "Same primary as H; a changed editorial uncertainty qualification alone supplies no H collation count."
    },
    {
      "id": "B08",
      "location": "before les deux composantes",
      "C": "\\unsure{considérons}",
      "H": "considérons",
      "reading": "considérons",
      "evidence": "The separate acute, looped d, and the final low ons run with its hook are recoverable.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop06_considerons.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          942,
          906,
          1229,
          975
        ]
      },
      "C_source_doubt_row": "C18-R05"
    },
    {
      "id": "B09",
      "location": "lemma, mark after subscript J",
      "C": "\\deleted{\\unsure{i|j|,}}",
      "H": "[omitted]",
      "reading": "\\unsure{\\deleted{j}|\\deleted{i}|\\deleted{,}|j}",
      "evidence": "The small dark form has a descending shaft, leftward lower return and crowded transverse upper stroke. Cancelled j is selected; cancelled i/comma and a live j remain possible. Glyph and state remain separate uncertainties.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop07_lemma_pi.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1298,
          1220,
          1328,
          1261
        ]
      },
      "C_source_doubt_row": "C18-R06a",
      "physical_parent": "lemma-Pi"
    },
    {
      "id": "B10",
      "location": "lemma raised ring",
      "C": "\\unsure{\\circ|0}",
      "H": "0",
      "reading": "\\unsure{\\circ|0}",
      "evidence": "Small closed raised ring with a white centre. Circle is the primary shape candidate and zero is retained.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop07_lemma_pi.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1268,
          1169,
          1295,
          1202
        ]
      },
      "C_source_doubt_row": "C18-R06b",
      "physical_parent": "lemma-Pi",
      "qualification": "H zero remains an explicit alternative; no conclusive error is claimed."
    },
    {
      "id": "B11",
      "location": "lemma underline and left rule, G02",
      "C": "\\uline{Lemme}; tabular left rule",
      "H": "\\emph{Lemme}; no left rule",
      "reading": "One underline and a left rule starting below the first textual line",
      "evidence": "Underline extends from approximately (308,1275) to (550,1258). The separate left line runs from approximately (255,1247) to (259,1385), beginning beside the underline region rather than above Lemme. The full lemma is represented once.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          244,
          1190,
          562,
          1395
        ]
      },
      "source_location": "half b, bbox [244,89,562,294]; y_full=y_b+1101",
      "qualification": "H emph and the single underline agree; the H difference is the left rule. C difference is the observed placement/endpoints of the generic table rule."
    },
    {
      "id": "B12",
      "location": "lemma endpoint",
      "C": "no full stop",
      "H": "full stop",
      "reading": "no full stop",
      "evidence": "Space after the final Sigma_i^- on the supplied lower half contains no detached sentence point.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1524,
          1268,
          1654,
          1387
        ]
      },
      "source_location": "half b, bbox [1524,167,1654,286]"
    },
    {
      "id": "B13",
      "location": "proof opening Dire",
      "C": "\\unsure{Dire}",
      "H": "Dire",
      "reading": "Dire",
      "evidence": "Large worked-over D, separate i stroke/dot, and the low re termination are legible. Lower loops belong to the worked-over D; no independent predecessor character is recovered.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crop08_dire.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1408,
          1383,
          1528,
          1461
        ]
      },
      "C_source_doubt_row": "C18-R07"
    },
    {
      "id": "B14",
      "location": "qu’une/la correction, guide G03a",
      "C": "\\deleted{la}\\inserted{qu’une}",
      "H": "\\add{qu’une}\\struck{la}",
      "reading": "Same words and states, full connected hooked guide",
      "evidence": "The guide touches the lower-left insertion point, rises across the l ascender region and continues beneath qu’une to a hooked right endpoint.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop09_insertions.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          242,
          1494,
          430,
          1585
        ]
      },
      "physical_parent": "proof-insertions"
    },
    {
      "id": "B15",
      "location": "inserted U subscript",
      "C": "U_{\\unsure{\\alpha|x}}",
      "H": "U_\\alpha",
      "reading": "U_{\\unsure{\\alpha|x}}",
      "evidence": "A small lower loop with a crossing rightward stroke supports alpha; the crossing alone permits x.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop09_insertions.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          730,
          1474,
          799,
          1522
        ]
      },
      "C_source_doubt_row": "C18-R08a",
      "physical_parent": "proof-insertions"
    },
    {
      "id": "B16",
      "location": "raised Pi in proof insertion",
      "C": "\\Pi_J^\\circ",
      "H": "\\Pi_J^0",
      "reading": "\\Pi_J^\\circ",
      "evidence": "The second raised ring was separately inspected. Its loop is small and crowded at upper left. Circle/zero uncertainty remains in the record; the first occurrence bears the printed qualifier.",
      "confidence": "medium",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop09_insertions.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          893,
          1456,
          962,
          1511
        ]
      },
      "physical_parent": "proof-insertions",
      "qualification": "H zero is retained as an alternative; repeated-glyph printing follows the brief."
    },
    {
      "id": "B17",
      "location": "apparent comma after inserted U_alpha",
      "C": "U_\\alpha, de",
      "H": "U_\\alpha de",
      "reading": "U_\\alpha de",
      "evidence": "The small hooked form at this position continues directly into the long guide G03b; it supplies no separate punctuation locus. It is drawn once as part of that guide.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crop09_insertions.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          802,
          1495,
          827,
          1522
        ]
      },
      "physical_parent": "proof-insertions"
    },
    {
      "id": "B18",
      "location": "guide beneath U_alpha de Pi, G03b",
      "C": "no guide path",
      "H": "no guide path",
      "reading": "One connected guide with its small upper-left hook",
      "evidence": "Lower-left end begins before ne, rises to the hook beside de, then curves downward and rises to the upper-right endpoint beyond Pi. Two source path commands meet at the same hook/guide point.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop09_insertions.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          753,
          1482,
          1017,
          1559
        ]
      },
      "physical_parent": "proof-insertions"
    },
    {
      "id": "B19",
      "location": "H struck un after the raised name",
      "C": "no additional struck word",
      "H": "\\struck{un}",
      "reading": "no additional struck un",
      "evidence": "Only the live ne group occurs below the raised label. The stroke above/beside it is the connected insertion guide; no second crossed word is supported.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop09_insertions.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          754,
          1492,
          871,
          1564
        ]
      },
      "physical_parent": "proof-insertions"
    },
    {
      "id": "B20",
      "location": "older form within corrected E_i",
      "C": "\\deleted{\\unsure{\\Sigma}}",
      "H": "[omitted]",
      "reading": "\\deleted{\\Sigma}",
      "evidence": "The surviving internal upper and lower obliques form the angular predecessor beneath the heavy E upright and lower arm. Sigma is resolved locally.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crop10_corrected_Ei.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1303,
          1503,
          1367,
          1557
        ]
      },
      "C_source_doubt_row": "C18-R09a",
      "physical_parent": "corrected-Ei"
    },
    {
      "id": "B21",
      "location": "separate rule above corrected E_i, G04",
      "C": "\\unsure{\\overline{E_i}|E_i}",
      "H": "E_i",
      "reading": "E_i with a locally qualified literal upper stroke",
      "evidence": "Two separated upper horizontal runs are visible: the lower belongs to the corrected capital head; the upper has a small retraced/returning right end. Upper-stroke presence is clear. Its closure-bar or overwritten-remnant role and exact hand remain unresolved; the stroke is kept once regardless of interpretation.",
      "confidence": "low",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop10_corrected_Ei.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1316,
          1490,
          1380,
          1514
        ]
      },
      "C_source_doubt_row": "C18-R14",
      "physical_parent": "corrected-Ei",
      "shape_confidence": "high",
      "qualification": "This is the independent actual C bar doubt, not an instantiated example from S. The source renders a qualified graphical overmark rather than selecting an algebraic closure operation."
    },
    {
      "id": "B22",
      "location": "before il existe",
      "C": "que il",
      "H": "qu'il",
      "reading": "que il",
      "evidence": "The e-ending of que remains written before the separate i/l strokes. No elision is supplied.",
      "confidence": "high",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1025,
          1598,
          1391,
          1747
        ]
      },
      "source_location": "half b, bbox [1025,497,1391,646]"
    },
    {
      "id": "B23",
      "location": "after tel que",
      "C": "le",
      "H": "la",
      "reading": "le",
      "evidence": "Looped l is followed by a short low e-form, without a separate a bowl.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          815,
          1734,
          893,
          1822
        ]
      },
      "source_location": "half b, bbox [815,633,893,721]"
    },
    {
      "id": "B24",
      "location": "older form within corrected E_j",
      "C": "\\deleted{\\unsure{\\Sigma}}",
      "H": "[omitted]",
      "reading": "\\deleted{\\Sigma}",
      "evidence": "Thin angular interior strokes survive inside the heavier corrected E. Sigma is independently recovered at this second locus.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crop11_formula_choisi.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1275,
          1730,
          1326,
          1779
        ]
      },
      "C_source_doubt_row": "C18-R09b",
      "physical_parent": "corrected-Ej"
    },
    {
      "id": "B25",
      "location": "subscript of corrected E_j",
      "C": "E_{\\unsure{j|J}}",
      "H": "E_j",
      "reading": "E_{\\unsure{j|J}}",
      "evidence": "The index is a nearly straight descending stroke with a small lower left hook and no securely detached dot or top bar. Lowercase j remains primary; J remains possible. No neighbouring formula supplies the reading.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop11_formula_choisi.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1308,
          1757,
          1333,
          1811
        ]
      },
      "C_source_doubt_row": "C18-R09c",
      "physical_parent": "corrected-Ej"
    },
    {
      "id": "B26",
      "location": "crossed word after right parenthesis",
      "C": "\\deleted{\\unsure{choisi}}",
      "H": "\\struck{choisie}",
      "reading": "\\deleted{\\unsure{choisi|choisie}}",
      "evidence": "Tall h, low o/s shapes and dotted strokes survive the horizontal cancellation. No separate final e is secure, but cancellation leaves choisie possible.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop11_formula_choisi.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1406,
          1712,
          1576,
          1793
        ]
      },
      "C_source_doubt_row": "C18-R10",
      "physical_parent": "choisi-points",
      "qualification": "H survives as an alternative; C primary and unresolved status are retained."
    },
    {
      "id": "B27",
      "location": "two additional right/upper points beside crossed choisi, G05",
      "C": "[omitted]",
      "H": "[omitted]",
      "reading": "Two locally qualified graphical points",
      "evidence": "Beyond the final dotted-letter group, two small distinct dark points rise diagonally to the right. The selected source draws only this additional pair, once. Their role, attachment, hand and surface origin remain unassigned.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop11_formula_choisi.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1567,
          1735,
          1591,
          1762
        ]
      },
      "physical_parent": "choisi-points",
      "shape_confidence": "medium"
    },
    {
      "id": "B28",
      "location": "quoted word in proof",
      "C": "\\unsure{composant|composante}",
      "H": "composante",
      "reading": "\\unsure{composant|composante}",
      "evidence": "The t has a short rightward crossing/return and no separately secure final e. The crossing can conceal an ending; the original alternatives remain.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop12_lower_quote.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          237,
          1892,
          584,
          1979
        ]
      },
      "C_source_doubt_row": "C18-R11",
      "qualification": "Qualified primary difference; H survives as the alternative."
    },
    {
      "id": "B29",
      "location": "verb after crossed est",
      "C": "\\deleted{est} est",
      "H": "\\struck{est} soit",
      "reading": "\\deleted{est} est",
      "evidence": "The live form has a small initial loop followed by s/t strokes; there is no separate oi group. The preceding est has a distinct horizontal cancellation.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop13_live_est.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1204,
          1849,
          1479,
          1922
        ]
      }
    },
    {
      "id": "B30",
      "location": "accent within l’élément",
      "C": "élément",
      "H": "élément",
      "reading": "\\unsure{élêment|élément}",
      "evidence": "The second detached accent is angular, with two apparent arms. Circumflex is selected, while a hooked acute remains possible. The first accented e is retained from its faint short raised stroke.",
      "confidence": "medium",
      "kind": "abbreviation expanded or spelling modernised",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop14_element_du.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          262,
          2003,
          493,
          2083
        ]
      },
      "qualification": "The familiar spelling survives as an explicit alternative; this is a local paleographic doubt."
    },
    {
      "id": "B31",
      "location": "article before the next pi_zero",
      "C": "du",
      "H": "de",
      "reading": "du",
      "evidence": "After the looped d, the remaining run has the low u trough and rising termination.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop14_element_du.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          528,
          2008,
          620,
          2067
        ]
      }
    },
    {
      "id": "B32",
      "location": "raised (soit Sigma_i^-), guide G06",
      "C": "\\inserted{(soit $\\Sigma_i^-$)}",
      "H": "\\add{(soit $\\Sigma_i^-$)}",
      "reading": "Same insertion and full bent/hooked guide",
      "evidence": "The guide rises from the gap between éléments and de, sweeps over the d ascender and ends in a small right hook. The adjoining éléments and de occur once in the selected source.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop15_soit_guide.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          555,
          2192,
          657,
          2258
        ]
      },
      "physical_parent": "soit-insertion"
    },
    {
      "id": "B33",
      "location": "crossed word below card I=2",
      "C": "\\deleted{\\unsure{deux}}",
      "H": "[omitted]",
      "reading": "\\deleted{\\unsure{deux}}",
      "evidence": "A low initial loop/ascender and small rises remain under the strong line. The full word cannot be recovered with confidence; deux stays qualified. The physical page edge is inside the crop.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop16_bottom_corrections.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          390,
          2299,
          560,
          2337
        ]
      },
      "C_source_doubt_row": "C18-R12",
      "physical_parent": "cas-correction"
    },
    {
      "id": "B34",
      "location": "raised card I=2",
      "C": "\\inserted{\\operatorname{card}I=2}",
      "H": "\\operatorname{card}I=2",
      "reading": "\\inserted{\\operatorname{card}I=2}",
      "evidence": "The expression is physically above the crossed word. The selected G07 keeps that placement, and retains the cancellation rule once.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop16_bottom_corrections.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          382,
          2268,
          565,
          2337
        ]
      },
      "physical_parent": "cas-correction"
    },
    {
      "id": "B35",
      "location": "cancelled form before fortiori",
      "C": "\\deleted{\\unsure{OK|cela}}",
      "H": "\\struck{et}",
      "reading": "\\deleted{\\unsure{OK|cela|et}}",
      "evidence": "A dark loop and tall angled strokes remain under crossing strokes. OK is the selected visible candidate; cela and et remain possible because cancellation obscures the joins.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop16_bottom_corrections.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          652,
          2269,
          804,
          2340
        ]
      },
      "C_source_doubt_row": "C18-R13a",
      "qualification": "H et survives as a supported alternative, not a conclusively rejected reading."
    },
    {
      "id": "B36",
      "location": "accent before fortiori",
      "C": "\\unsure{â|à}",
      "H": "à",
      "reading": "\\unsure{â|à}",
      "evidence": "The detached upper mark is roof-like; a short bent grave remains possible. The long return immediately below belongs to the a form and is not supplied as a second detached mark.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crop16_bottom_corrections.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          827,
          2280,
          884,
          2337
        ]
      },
      "C_source_doubt_row": "C18-R13b",
      "qualification": "H à survives as the alternative."
    },
    {
      "id": "B37",
      "location": "final U subscript",
      "C": "U_\\alpha",
      "H": "U_\\alpha",
      "reading": "U_\\alpha",
      "evidence": "Separately viewed low hook/crossing form supports alpha with x still possible. The original compound row explicitly relates this repetition to the inserted form. First-occurrence printing puts the qualifier at B15; this local uncertainty remains in the record.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crop17_final.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1213,
          2300,
          1248,
          2335
        ]
      },
      "C_source_doubt_row": "C18-R08b"
    },
    {
      "id": "B38",
      "location": "final OK and rising transverse stroke, G08",
      "C": "live OK",
      "H": "live OK",
      "reading": "Qualified whole OK graphic; live/cancelled state unresolved",
      "evidence": "A thin rising diagonal traverses the upper O/K region and reaches above the right side. It may belong to the letter construction or cancel the word. The glyphs and period remain clear. The literal diagonal is drawn once, with a local uncertainty wrapper and invisible deletion annotation.",
      "confidence": "low",
      "kind": "deletion state (struck given live or live given struck)",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crop17_final.png",
      "bbox": {
        "space": "original full scan; top-left origin",
        "xyxy": [
          1444,
          2258,
          1575,
          2341
        ]
      },
      "shape_confidence": "high",
      "qualification": "Live OK is primary and the cancelled state is an alternative; no cancellation chronology or mathematical endorsement is inferred."
    }
  ],
  "doubts": [
    {
      "difference_ids": [
        "B02"
      ],
      "location": "first parenthesis",
      "reading": "rècurrence",
      "alternatives": [
        "récurrence"
      ],
      "confidence": "medium",
      "reason": "Compressed body; short accent hook does not settle its intended direction.",
      "crop": "crop02_recurrence.png"
    },
    {
      "difference_ids": [
        "B04"
      ],
      "location": "after (unique)",
      "reading": "des",
      "alternatives": [
        "de"
      ],
      "confidence": "medium",
      "reason": "Long final hook can belong to either ending.",
      "crop": "crop04_unique.png"
    },
    {
      "difference_ids": [
        "B07"
      ],
      "location": "upper quoted word",
      "reading": "composante",
      "alternatives": [
        "composant"
      ],
      "confidence": "medium",
      "reason": "Terminal curved return can belong to t or to an e ending.",
      "crop": "crop05_upper_quote.png"
    },
    {
      "difference_ids": [
        "B09"
      ],
      "location": "mark after lemma J",
      "reading": "cancelled j",
      "alternatives": [
        "cancelled i",
        "cancelled comma",
        "live j"
      ],
      "confidence": "low",
      "reason": "Crowded crossing and lower hook leave both glyph and state open.",
      "crop": "crop07_lemma_pi.png"
    },
    {
      "difference_ids": [
        "B10"
      ],
      "location": "lemma raised ring",
      "reading": "circle",
      "alternatives": [
        "zero"
      ],
      "confidence": "medium",
      "reason": "Small closed ring supplies no stronger character determination.",
      "crop": "crop07_lemma_pi.png"
    },
    {
      "difference_ids": [
        "B15"
      ],
      "location": "inserted U index",
      "reading": "alpha",
      "alternatives": [
        "x"
      ],
      "confidence": "medium",
      "reason": "Loop/crossing remains ambiguous.",
      "crop": "crop09_insertions.png"
    },
    {
      "difference_ids": [
        "B16"
      ],
      "location": "inserted raised Pi ring",
      "reading": "circle",
      "alternatives": [
        "zero"
      ],
      "confidence": "medium",
      "reason": "Second loop separately seen; first occurrence carries printed doubt.",
      "crop": "crop09_insertions.png"
    },
    {
      "difference_ids": [
        "B21"
      ],
      "location": "upper stroke over corrected E_i",
      "reading": "closure-like upper rule",
      "alternatives": [
        "surviving overwritten pen stroke"
      ],
      "confidence": "low",
      "reason": "Stroke is visible; role and hand are unsettled.",
      "crop": "crop10_corrected_Ei.png"
    },
    {
      "difference_ids": [
        "B25"
      ],
      "location": "corrected E index",
      "reading": "j",
      "alternatives": [
        "J"
      ],
      "confidence": "low",
      "reason": "Undotted descending stem with small hook.",
      "crop": "crop11_formula_choisi.png"
    },
    {
      "difference_ids": [
        "B26"
      ],
      "location": "crossed word",
      "reading": "choisi",
      "alternatives": [
        "choisie"
      ],
      "confidence": "medium",
      "reason": "Cancellation conceals the final join.",
      "crop": "crop11_formula_choisi.png"
    },
    {
      "difference_ids": [
        "B27"
      ],
      "location": "extra point pair",
      "reading": "two graphical points",
      "alternatives": [
        "unestablished letter/mark attachment"
      ],
      "confidence": "low",
      "reason": "Shape is retained, but role, hand and surface origin are unassigned.",
      "crop": "crop11_formula_choisi.png"
    },
    {
      "difference_ids": [
        "B28"
      ],
      "location": "lower quoted word",
      "reading": "composant",
      "alternatives": [
        "composante"
      ],
      "confidence": "medium",
      "reason": "Short t return does not securely settle a final e.",
      "crop": "crop12_lower_quote.png"
    },
    {
      "difference_ids": [
        "B30"
      ],
      "location": "l’élément accent",
      "reading": "élêment",
      "alternatives": [
        "élément"
      ],
      "confidence": "medium",
      "reason": "Angular second accent can also be a hooked acute.",
      "crop": "crop14_element_du.png"
    },
    {
      "difference_ids": [
        "B33"
      ],
      "location": "crossed bottom word",
      "reading": "deux",
      "alternatives": [],
      "confidence": "low",
      "reason": "The long cancellation covers most of the low letters.",
      "crop": "crop16_bottom_corrections.png"
    },
    {
      "difference_ids": [
        "B35"
      ],
      "location": "cancelled form before fortiori",
      "reading": "OK",
      "alternatives": [
        "cela",
        "et"
      ],
      "confidence": "low",
      "reason": "Overlapping loops and diagonals conceal the word skeleton.",
      "crop": "crop16_bottom_corrections.png"
    },
    {
      "difference_ids": [
        "B36"
      ],
      "location": "accent before fortiori",
      "reading": "â",
      "alternatives": [
        "à"
      ],
      "confidence": "low",
      "reason": "Roof-like short mark can also be a bent grave.",
      "crop": "crop16_bottom_corrections.png"
    },
    {
      "difference_ids": [
        "B37"
      ],
      "location": "final U index",
      "reading": "alpha",
      "alternatives": [
        "x"
      ],
      "confidence": "medium",
      "reason": "Independently inspected recurrence, printed with the first candidate under the recurring-glyph rule.",
      "crop": "crop17_final.png"
    },
    {
      "difference_ids": [
        "B38"
      ],
      "location": "final OK state",
      "reading": "live OK",
      "alternatives": [
        "cancelled OK"
      ],
      "confidence": "low",
      "reason": "The rising diagonal may be part of the letters or a cancellation.",
      "crop": "crop17_final.png"
    }
  ],
  "notes": [
    {
      "topic": "page content",
      "text": "Opening continuation, a Ceci posé paragraph, an underlined Lemme with a separate left rule, and its densely corrected proof. No independent diagram or mathematical display; formulas are within prose."
    },
    {
      "topic": "author uncertainty",
      "text": "No lexical assertion of uncertainty such as peut-être is supplied on this page. The author writes OK at the conclusion; its transverse stroke has an unresolved state. The cancelled form earlier in the line remains uncertain. Reading the written OK is not a proof check."
    },
    {
      "topic": "title/date/page counts",
      "text": "Lemme is underlined. No date or independent manuscript page-number heading was seen. Archive 17 appears at lower left and is a comment only. H page{17} is treated as its editorial page marker."
    },
    {
      "topic": "mathematics-led decisions",
      "text": "No formula was repaired, proved, recomputed or used to determine an unclear glyph. The written X setminus Sigma_i and que il remain. H’s note proposing E_i for Sigma_i is apparatus; it adds no manuscript occurrence."
    },
    {
      "topic": "compound C rows",
      "text": "Fourteen original doubtful-reading rows retain their source identities. R06, R08, R09 and R13 are split into independently reported local parts. R14 remains independent of R09 even though the crop is shared. Notation, Slips retained and Abbreviations tables are not counted as extra doubt rows."
    },
    {
      "topic": "abbreviations",
      "text": "card, ens, i.e. and OK remain unexpanded. The period after ens supplied by H is absent; the two points of i.e. are seen."
    },
    {
      "topic": "source representation",
      "text": "All free graphic groups use fixed local origins, baseline coordinates, base-west text nodes and zero inner/outer node separation. Paths are manual approximations of viewed ink. Font extents and rendered fit were not measured or validated."
    },
    {
      "topic": "visible duplication safeguards",
      "text": "The comma-like hook after inserted U belongs to G03b; no comma is separately printed. The guide does not supply H’s additional struck un. éléments and de are included in G06 once. The point pair G05 is additional to the dotted-letter group. Final OK and bottom deux use visible rlap text with invisible deletion-dimensional copies; no generic additional cancellation is drawn there."
    },
    {
      "topic": "crop bounds",
      "text": "Every planned target’s guide endpoints and deciding ink were included. Neighbouring non-target text can meet crop boundaries. Bottom crops include the physical paper edge; the fortiori f descender reaches that physical edge. No unseen extension is supplied, and no target was reopened or recropped."
    }
  ],
  "notation": [
    {
      "location": "opening cardinality formula",
      "latex": "\\operatorname{card}J=\\operatorname{card}I-1=n-1",
      "evidence": "Small c in card, capitals J/I, separate equals and midline minuses."
    },
    {
      "location": "repeated U_J,i",
      "latex": "U_{J,i}",
      "evidence": "Capital J, comma and separate lowered i; checked at definition, lemma and unequal expression."
    },
    {
      "location": "lemma and insertion",
      "latex": "\\Pi_J^{\\unsure{\\circ|0}}",
      "evidence": "Two hanging strokes below a head; small raised ring. Only first printed occurrence bears doubt."
    },
    {
      "location": "inserted and final U",
      "latex": "U_{\\unsure{\\alpha|x}}",
      "evidence": "Crossed/looped small form, separately inspected at both places; first occurrence qualified."
    },
    {
      "location": "corrected E_i and E_j",
      "latex": "\\deleted{\\Sigma}E_i; \\deleted{\\Sigma}E_{\\unsure{j|J}}",
      "evidence": "Angular internal remnants survive the heavy E forms; second index stays uncertain."
    },
    {
      "location": "proof and conclusion",
      "latex": "\\ne;\\in;\\subset",
      "evidence": "Crossed paired equal strokes, open membership form, and a single open inclusion bowl; no extra equality line supplied."
    },
    {
      "location": "lower argument",
      "latex": "\\pi_0(X\\setminus\\Sigma_i)",
      "evidence": "Two pi legs with low zero, backslash, angular Sigma and low i; retained as written."
    },
    {
      "location": "quoted prose",
      "latex": "``...''",
      "evidence": "Paired ticks, sometimes joined, at both physical quotations."
    },
    {
      "location": "upper E_i rule",
      "latex": "G04 literal locally qualified stroke",
      "evidence": "Separate upper horizontal with short retrace; shape retained without assigning closure semantics."
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "A visibly separate rule over a corrected capital can have a secure shape while its closure/remnant role remains unresolved. The selected source uses a local qualified graphical overmark to preserve the line once, with both interpretations retained in the record.",
    "The small hook adjacent to inserted U_alpha is connected to the guide; a punctuation transcription would duplicate that physical mark.",
    "The final OK permits live/cancelled state alternatives. The whole graphic is locally qualified; actual diagonal geometry is retained without an additional generic strike."
  ]
}

## Reader C

\scanpage{18}
cette dernière, si $\operatorname{card}J=\operatorname{card}I-1=n-1$, on verra (par r\unsure{è|é}currence) que le cardinal de l'ens des classes est $(n-1)+1=n$.

Ceci posé, on voit d'abord que $E_i$ est dans
% G01: original full-scan origin (820,455); x=0.010cm, y=-0.010cm.
% Fixed drawing rectangle 670 by 160 source-coordinate units. The words occur here once.
\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g01base)]
\path[use as bounding box] (0,0) rectangle (670,160);
\coordinate (g01base) at (0,113);
\begin{scope}[shift={(-820,-455)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (833,568) {l'une};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1100,568) {\unsure{de|des}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1269,568) {ces $n$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1028,500) {\inserted{(unique)}};
% G01a: complete long insertion guide, with bent left end and upturned right end.
\draw[line width=.45pt] (1089,559) .. controls (1078,530) and (1100,519) .. (1154,517) .. controls (1208,517) and (1258,513) .. (1277,499);
\end{scope}
\end{tikzpicture}
classes, qui sont des ouverts. Soit $U_{J,i}$ la classe (ou ``composante'') qui contient $E_i$, et considérons les deux composantes $\Sigma_i^+,\Sigma_i^-$ de $X\setminus E_i$.

% G02: complete two-line lemma group; full-scan origin (230,1135).
% x=0.010cm, y=-0.010cm; fixed 1410 by 270 source-coordinate rectangle.
\figure{\begin{tikzpicture}[x=.010cm,y=-.010cm]
\path[use as bounding box] (0,0) rectangle (1410,270);
\begin{scope}[shift={(-230,-1135)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (300,1250) {\rlap{Lemme}\phantom{\uline{Lemme}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (640,1238) {Toute classe de $\Pi_{J\deleted{\unsure{i|j|,}}}^{\unsure{\circ|0}}$, distincte};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (275,1376) {de $U_{J,i}$, est contenue dans $\Sigma_i^+$ ou $\Sigma_i^-$};
% G02a: heading underline; G02b: separate, short left rule.
\draw[line width=.5pt] (307,1275) .. controls (382,1268) and (467,1262) .. (550,1258);
\draw[line width=.5pt] (254,1248) .. controls (255,1299) and (257,1351) .. (259,1383);
\end{scope}
\end{tikzpicture}}

C'est presque une tautologie : Dire
% G03: qu'une/la/classe group, full-scan origin (235,1480), fixed 310 by 125 rectangle.
\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g03base)]
\path[use as bounding box] (0,0) rectangle (310,125);
\coordinate (g03base) at (0,91);
\begin{scope}[shift={(-235,-1480)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (244,1522) {\inserted{qu'une}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (306,1568) {\rlap{la}\phantom{\deleted{la}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (390,1575) {classe};
% G03a/b: observed interrupted insertion guide; the q descender belongs to qu'une.
\draw[line width=.4pt] (270,1578) .. controls (276,1566) and (288,1558) .. (301,1554);
\draw[line width=.4pt] (308,1549) .. controls (331,1541) and (352,1538) .. (369,1535) .. controls (389,1529) and (414,1519) .. (420,1514) .. controls (423,1511) and (417,1510) .. (412,1511);
% G03c: the actual lower cancellation stroke, without an additional generic rule.
\draw[line width=.65pt] (306,1568) .. controls (328,1569) and (348,1563) .. (367,1558);
\end{scope}
\end{tikzpicture}
% G04: donnée / inserted name / ne group. Full-scan origin (530,1445), fixed 525 by 160.
\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g04base)]
\path[use as bounding box] (0,0) rectangle (525,160);
\coordinate (g04base) at (0,111);
\begin{scope}[shift={(-530,-1445)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (560,1556) {donnée};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (797,1548) {ne};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (737,1507) {\inserted{$U_{\unsure{\alpha|x}}$\quad de $\Pi_J^\circ$}};
% G04a: complete guide; no separate cancelled un is supplied.
\draw[line width=.4pt] (761,1554) .. controls (762,1540) and (791,1528) .. (811,1516) .. controls (853,1528) and (876,1534) .. (908,1521) .. controls (957,1511) and (1006,1500) .. (1012,1487);
% G04b: one locally qualified comma-like hook at the guide junction.
% Nested local origin (806,1504), baseline (0,0), base-west placement and zero separation.
% Its role as comma or guide return is unsettled; no second printed comma is added.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (806,1504) {\unsure{\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g04hookbase)]
\path[use as bounding box] (0,0) rectangle (15,17);
\coordinate (g04hookbase) at (0,0);
\draw[line width=.45pt] (0,4) .. controls (9,0) and (15,6) .. (6,13);
\end{tikzpicture}}};
\end{scope}
\end{tikzpicture}
contient pas $\deleted{\Sigma}\overline{E_i}$ i.e. est $\ne U_{J,i}$, signifie que il existe un $j\in J$ tel que le $\Sigma_j^+\in\pi_0(X\setminus\deleted{\Sigma}E_j)$
% G05: cancelled word and two detached endpoint points, origin (1400,1715), fixed 200 by 90.
\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g05base)]
\path[use as bounding box] (0,0) rectangle (200,90);
\coordinate (g05base) at (0,49);
\begin{scope}[shift={(-1400,-1715)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1410,1764) {\rlap{\unsure{choisi|choisie}}\phantom{\deleted{\unsure{choisi|choisie}}}};
% G05a: single cancellation stroke.
\draw[line width=.6pt] (1410,1757) .. controls (1468,1756) and (1524,1757) .. (1566,1758);
% G05b/c: both extra endpoint points occur once; the two i dots stay within the word.
% Nested origin (1567,1745), baseline (0,0), base-west anchor and zero separation.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1567,1745) {\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g05pointsbase)]
\path[use as bounding box] (0,0) rectangle (12,12);
\coordinate (g05pointsbase) at (0,0);
\fill (2,8) circle[radius=1.1];
\fill (9,2) circle[radius=1.0];
\end{tikzpicture}}};
\end{scope}
\end{tikzpicture}
``composant'' de cette classe \deleted{est} est l'\unsure{é|e}l\unsure{é|ê}ment du $\pi_0$ qui ne contient pas $E_i$; il est donc contenu dans l'un des
% G06: whole éléments / (soit Sigma) / de / pi_0 group, origin (245,2135), fixed 795 by 155.
\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g06base)]
\path[use as bounding box] (0,0) rectangle (795,155);
\coordinate (g06base) at (0,125);
\begin{scope}[shift={(-245,-2135)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (270,2260) {\unsure{é|e}léments};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (396,2213) {\inserted{(soit $\Sigma_i^-$)}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (595,2245) {de};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (719,2244) {$\pi_0(X\setminus\Sigma_i)$};
% G06a: guide crossing the ascender of de, with its full right hook.
\draw[line width=.4pt] (558,2247) .. controls (562,2228) and (580,2225) .. (612,2221) .. controls (632,2218) and (646,2213) .. (650,2208) .. controls (647,2204) and (645,2202) .. (642,2204);
\end{scope}
\end{tikzpicture}, d'après l'étude du
% G07: cas / cancelled deux / raised card I=2, origin (245,2240), fixed 370 by 123.
\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g07base)]
\path[use as bounding box] (0,0) rectangle (370,123);
\coordinate (g07base) at (0,85);
\begin{scope}[shift={(-245,-2240)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (275,2325) {cas};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (400,2321) {\rlap{\unsure{deux}}\phantom{\deleted{\unsure{deux}}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (386,2302) {\inserted{$\operatorname{card}I=2$}};
% G07a: complete long cancellation rule, kept once.
\draw[line width=.65pt] (399,2320) .. controls (438,2313) and (483,2317) .. (515,2314) .. controls (531,2312) and (546,2311) .. (555,2312);
% G07b: supported lower hook below the I/= region; its guide/letter role remains unsettled.
% Nested origin (510,2290), baseline (0,0), base-west placement and zero separation.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (510,2290) {\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g07hookbase)]
\path[use as bounding box] (0,0) rectangle (12,27);
\coordinate (g07hookbase) at (0,0);
\draw[line width=.5pt] (4,4) .. controls (10,10) and (8,18) .. (1,24);
\end{tikzpicture}}};
\end{scope}
\end{tikzpicture}, \deleted{\unsure{OK|cela}} \unsure{â|à} fortiori $U_\alpha\subset\Sigma_i^-$, OK.
% archive sheet number: 17



{
  "differences": [
    {
      "id": "D01",
      "location": "L01, cette dernière",
      "C": "\\unsure{dernière}",
      "H": "dernière",
      "reading": "dernière",
      "evidence": "The d loop, joined middle, dotted i and separate descending-right accent are visible. The comma is distinct.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/01_opening.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          416,
          82,
          644,
          153
        ]
      },
      "source_C_doubt_row": "C018-D01"
    },
    {
      "id": "D02",
      "location": "L02, first parenthesis",
      "C": "\\unsure{récurrence}",
      "H": "récurrence",
      "reading": "r\\unsure{è|é}currence",
      "evidence": "The word is recoverable, but the compact accent is a dark wedge with a short downward-right end. Grave is the primary visible candidate; acute remains supported by the compact stroke. This is a qualified change, not a conclusive H error.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/02_recurrence.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          600,
          190,
          986,
          240
        ]
      },
      "source_C_doubt_row": "C018-D02"
    },
    {
      "id": "D03",
      "location": "L03, l’ens des classes",
      "C": "\\unsure{ens}",
      "H": "ens.",
      "reading": "ens",
      "evidence": "Three joined letters after the apostrophe are visible. The gap before des contains no abbreviation point.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": null,
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          390,
          294,
          670,
          351
        ]
      },
      "source_C_doubt_row": "C018-D03",
      "half_location": "a, same coordinates; full upper half origin (0,0)"
    },
    {
      "id": "P01",
      "location": "L03, endpoint of ens",
      "C": "ens",
      "H": "ens.",
      "reading": "ens without a point",
      "evidence": "The clear gap after the s has no discrete point.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          471,
          307,
          666,
          351
        ]
      }
    },
    {
      "id": "D04",
      "location": "L05, after raised (unique)",
      "C": "\\unsure{de|des}",
      "H": "des",
      "reading": "\\unsure{de|des}",
      "evidence": "The d and e are visible; the long turning terminal stroke leaves a supported s alternative. H’s des remains explicitly retained.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/03_unique_de.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1095,
          532,
          1191,
          579
        ]
      },
      "source_C_doubt_row": "C018-D04"
    },
    {
      "id": "P02",
      "location": "L05, immediately before classes",
      "C": "de ces n classes",
      "H": "des classes",
      "reading": "de/des ces n classes",
      "evidence": "After the disputed de/des, a separate ces and a short n occur before the next physical line classes. The long descender from que above crosses ces.",
      "confidence": "high",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/03_unique_de.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1260,
          529,
          1482,
          583
        ]
      }
    },
    {
      "id": "G01",
      "location": "L05, (unique) insertion group",
      "C": "\\inserted{(unique)} without guide",
      "H": "\\add{(unique)} without guide",
      "reading": "G01a long bent guide with l’une, de/des, ces n and inserted (unique) each once",
      "evidence": "A thin line bends downward at the left attachment, passes below unique and turns upward at its right endpoint. The long adjacent upright belongs to que in L04 and is not added as a separate guide.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/03_unique_de.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1020,
          467,
          1284,
          566
        ]
      },
      "physical_cluster": "G01"
    },
    {
      "id": "D05",
      "location": "L08, et considérons",
      "C": "\\unsure{considérons}",
      "H": "considérons",
      "reading": "considérons",
      "evidence": "The middle dotted form, looped d, short rising-right acute, and final joined run are readable.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/04_considerons.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          940,
          907,
          1233,
          965
        ]
      },
      "source_C_doubt_row": "C018-D05"
    },
    {
      "id": "D06a",
      "location": "L10, small cancelled sign following the lemma J",
      "C": "\\deleted{\\unsure{i|j|,}}",
      "H": "no cancelled sign",
      "reading": "\\deleted{\\unsure{i|j|,}}",
      "evidence": "A dark short descending mark with a lower left hook is crossed/overworked. The surviving contour does not settle i, j or comma.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/05_lemma.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1296,
          1219,
          1331,
          1262
        ]
      },
      "source_C_doubt_row": "C018-D06",
      "physical_cluster": "lemma cancelled subscript"
    },
    {
      "id": "D06b",
      "location": "L10, upper ring on lemma Pi",
      "C": "\\unsure{\\circ|0}",
      "H": "0",
      "reading": "\\unsure{\\circ|0}",
      "evidence": "A small closed raised ring is visible; its use as circle or numeral remains unsettled. H’s 0 remains an alternative.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/05_lemma.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1267,
          1169,
          1293,
          1199
        ]
      },
      "source_C_doubt_row": "C018-D06",
      "physical_cluster": "lemma upper ring"
    },
    {
      "id": "G02",
      "location": "L10–11, lemma underline and left rule",
      "C": "single underline; full-height tabular left rule",
      "H": "emphasis on Lemme; no left rule",
      "reading": "G02a rising underline; separate G02b short left rule",
      "evidence": "The underline rises slightly to the right. The separate left rule begins around the heading underline level and ends beside the second line; it does not start at the top of the first text line.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/05_lemma.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          247,
          1239,
          558,
          1388
        ]
      },
      "physical_cluster": "G02",
      "counting_note": "One complete lemma graphic group; the underline’s emphasis reading already agrees with H."
    },
    {
      "id": "P03",
      "location": "L11, end of lemma",
      "C": "no final point",
      "H": "final point after Sigma_i^-",
      "reading": "no final point",
      "evidence": "The final Sigma index and raised minus are followed by clear paper; no full stop is visible on the supplied lower half or the complete lemma crop.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/05_lemma.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1525,
          1265,
          1666,
          1388
        ]
      }
    },
    {
      "id": "D07",
      "location": "L12, Dire",
      "C": "\\unsure{Dire}",
      "H": "Dire",
      "reading": "Dire",
      "evidence": "The large looped D is retraced. Its vertical, bowl, following i and low re are readable; no separate predecessor word is established.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/06_dire.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1400,
          1385,
          1527,
          1459
        ]
      },
      "source_C_doubt_row": "C018-D07"
    },
    {
      "id": "G03",
      "location": "L13, qu’une / cancelled la / classe",
      "C": "insertion and deletion macros only",
      "H": "insertion and deletion macros only",
      "reading": "G03a/b guide and G03c cancellation; words occur once",
      "evidence": "The q has its own descender. Beside it, the guide has a pale left run and a longer upper run with a right hook; the lower strike traverses la. The gap between the two visible guide runs is retained.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/07_quune.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          242,
          1506,
          517,
          1588
        ]
      },
      "physical_cluster": "G03"
    },
    {
      "id": "D08a",
      "location": "L13, subscript of inserted U",
      "C": "\\unsure{\\alpha|x}",
      "H": "alpha",
      "reading": "\\unsure{\\alpha|x}",
      "evidence": "A low loop/cross shape follows U. The closed-looking left part supports alpha, and the crossing alternative remains visible.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/08_ualpha.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          765,
          1486,
          795,
          1520
        ]
      },
      "source_C_doubt_row": "C018-D08",
      "physical_cluster": "inserted U subscript"
    },
    {
      "id": "D08b",
      "location": "L20, subscript of final U",
      "C": "alpha (unmarked recurrence, covered by C doubt table)",
      "H": "alpha",
      "reading": "alpha",
      "evidence": "The final subscript has a low left loop and raised returning right limb. Its local stroke supports alpha; the first occurrence’s x alternative is not carried as a separate printed doubt here.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/17_final.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1214,
          2296,
          1240,
          2321
        ]
      },
      "source_C_doubt_row": "C018-D08",
      "physical_cluster": "final U subscript"
    },
    {
      "id": "G04",
      "location": "L13, donnée / inserted U name / ne",
      "C": "insertion without literal guide",
      "H": "insertion without literal guide",
      "reading": "G04a guide; adjoining donnée and ne are kept once",
      "evidence": "A curved guide begins after donnée, rises beneath the inserted U name, dips under de Pi and ends with a small upturn at the right.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/08_ualpha.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          556,
          1463,
          1021,
          1568
        ]
      },
      "physical_cluster": "G04"
    },
    {
      "id": "M01",
      "location": "L13, after inserted U, at guide junction",
      "C": "comma after U",
      "H": "no comma",
      "reading": "one qualified comma-like hook G04b; comma/guide-return role unsettled",
      "evidence": "A short upper hook joins the long guide at the cusp. Its visible shape is preserved once; no additional typographic comma is printed.",
      "confidence": "low",
      "kind": "other",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/08_ualpha.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          803,
          1503,
          823,
          1523
        ]
      },
      "physical_cluster": "G04",
      "counting_note": "Component of G04; do not count the same guide junction again as an independent whole graphic."
    },
    {
      "id": "R01",
      "location": "L13, after donnée",
      "C": "ne contient, no struck un",
      "H": "\\struck{un} ne contient",
      "reading": "ne contient, no separate struck un",
      "evidence": "There is one short baseline word ne below the guide, followed by contient. No second word or separate cancellation for un is visible in the whole local group.",
      "confidence": "high",
      "kind": "text not on the page",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/08_ualpha.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          744,
          1518,
          1125,
          1566
        ]
      }
    },
    {
      "id": "N01",
      "location": "L13, raised Pi ring in the insertion",
      "C": "Pi_J^circ",
      "H": "Pi_J^0",
      "reading": "Pi_J^circ, recurring first candidate",
      "evidence": "The raised small loop has a short tilted return. Circle/0 remains the same recurring ambiguity first printed at the lemma. This local occurrence is separately recorded; H’s 0 remains supported.",
      "confidence": "low",
      "kind": "misread symbol or index",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/08_ualpha.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          889,
          1456,
          968,
          1510
        ]
      },
      "recurring_doubt": "D06b; uncertainty printed only at the first occurrence"
    },
    {
      "id": "D09a",
      "location": "L13, overwritten first E_i",
      "C": "\\deleted{\\unsure{Sigma}}",
      "H": "no predecessor",
      "reading": "\\deleted{Sigma} immediately before live barred E_i",
      "evidence": "The thin sloping upper and descending return survive inside the heavier E. The predecessor’s Sigma form is readable.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/09_first_E.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1307,
          1503,
          1369,
          1557
        ]
      },
      "source_C_doubt_row": "C018-D09",
      "physical_cluster": "first corrected E_i",
      "counting_note": "The H omission at this shared corrected-capital cluster also includes D14’s upper rule; count the cluster once against H."
    },
    {
      "id": "D14",
      "location": "L13, upper rule over corrected E_i",
      "C": "\\unsure{overline E_i|E_i}",
      "H": "plain E_i",
      "reading": "\\overline{E_i}",
      "evidence": "A separate near-horizontal upper rule sits above the E head, with visible white separation. Its presence is resolved. This is a graphic bar reading; no closure operation or chronology is inferred.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/09_first_E.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1317,
          1489,
          1378,
          1510
        ]
      },
      "source_C_doubt_row": "C018-D14",
      "physical_cluster": "first corrected E_i",
      "H_parent": "D09a",
      "S_relation": "Independent C doubt; S’s explicit examples are Sigma/U expressions and do not identify this E locus."
    },
    {
      "id": "R02",
      "location": "L14, before il existe",
      "C": "que il",
      "H": "qu’il",
      "reading": "que il",
      "evidence": "A complete que with its descending q is followed by a separately written il.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1030,
          1597,
          1211,
          1738
        ]
      },
      "half_location": "b, x=1030..1211, y=496..637; full y=half y+1101"
    },
    {
      "id": "R03",
      "location": "L15, before Sigma_j^+",
      "C": "le",
      "H": "la",
      "reading": "le",
      "evidence": "The tall looped l is followed by a low open e-like return.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          817,
          1731,
          897,
          1799
        ]
      },
      "half_location": "b, x=817..897, y=630..698; full y=half y+1101"
    },
    {
      "id": "D09b",
      "location": "L15, overwritten E in pi_0 argument",
      "C": "\\deleted{\\unsure{Sigma}}E",
      "H": "E alone",
      "reading": "\\deleted{Sigma}E",
      "evidence": "A thin upper diagonal and return are present within the heavy E; they preserve the Sigma predecessor.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/10_second_E_choisi.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1274,
          1738,
          1313,
          1782
        ]
      },
      "source_C_doubt_row": "C018-D09",
      "physical_cluster": "second corrected E_j"
    },
    {
      "id": "D09c",
      "location": "L15, second E subscript",
      "C": "\\unsure{j|J}",
      "H": "j",
      "reading": "j",
      "evidence": "A narrow lowered vertical ends in a bottom hook, without a capital J top bar. The local lowercase j reading is retained without a doubt marker.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/10_second_E_choisi.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1307,
          1751,
          1330,
          1810
        ]
      },
      "source_C_doubt_row": "C018-D09",
      "physical_cluster": "second corrected E_j"
    },
    {
      "id": "D10",
      "location": "L15, cancelled word after right parenthesis",
      "C": "\\deleted{\\unsure{choisi}}",
      "H": "\\struck{choisie}",
      "reading": "\\deleted{\\unsure{choisi|choisie}}",
      "evidence": "The h ascender and dotted strokes survive. The final horizontal is heavily overwritten; an independent final e cannot be settled. H’s choisie remains an explicit alternative.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/10_second_E_choisi.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1402,
          1714,
          1586,
          1783
        ]
      },
      "source_C_doubt_row": "C018-D10",
      "physical_cluster": "cancelled choisi"
    },
    {
      "id": "M02",
      "location": "L15, extra points after cancelled choisi",
      "C": "not recorded",
      "H": "not recorded",
      "reading": "qualified two-point cluster G05b/c, together with the cancelled word",
      "evidence": "Two small detached points lie to the right of the cancellation endpoint, in addition to the word’s i dots. The lower-left point is pale. Their role, hand and surface origin remain unsettled.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/10_second_E_choisi.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1565,
          1741,
          1583,
          1763
        ]
      },
      "physical_cluster": "G05",
      "path_confidence": {
        "G05b": "medium",
        "G05c": "medium"
      },
      "counting_note": "Two components of one endpoint cluster; both are drawn once."
    },
    {
      "id": "G05",
      "location": "L15, cancelled choisi group",
      "C": "generic deletion macro",
      "H": "generic struck macro",
      "reading": "word plus literal G05a cancellation and M02 points",
      "evidence": "The near-horizontal cancellation is preserved in the complete group. Its state was already in both witnesses; the new endpoint points carry the substantive omission.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crops/10_second_E_choisi.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1402,
          1714,
          1586,
          1783
        ]
      },
      "physical_cluster": "G05",
      "report_silent_source_choice": "G05a is an explicit geometric representation of the already agreed cancellation, not a second state difference."
    },
    {
      "id": "D11",
      "location": "L16, quoted composant(e)",
      "C": "\\unsure{composant|composante}",
      "H": "composante",
      "reading": "``composant’’",
      "evidence": "The final tall crossed t has its own returning foot. No further e body is visible before the closing quotation strokes. The opening and closing marks each support the supplied double-quote convention.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": "resolved",
      "readers_crop": "crops/11_composant.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          235,
          1899,
          589,
          1980
        ]
      },
      "source_C_doubt_row": "C018-D11"
    },
    {
      "id": "R04",
      "location": "L16, live word after cancelled est",
      "C": "\\deleted{est} est",
      "H": "\\struck{est} soit",
      "reading": "\\deleted{est} est",
      "evidence": "The cancelled est has a separate traversing rule. The live word has an initial e loop, low s and tall t, with no dotted i.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/12_est.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1208,
          1845,
          1471,
          1909
        ]
      }
    },
    {
      "id": "A01",
      "location": "L17, first accent in l’élément",
      "C": "é",
      "H": "é",
      "reading": "\\unsure{é|e}",
      "evidence": "Only a pale short mark occurs above the first e; its ink status and accent direction remain unsettled. The primary spelling is retained with an explicit blank-accent alternative.",
      "confidence": "low",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crops/13_du.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          332,
          2029,
          353,
          2067
        ]
      },
      "physical_cluster": "l’élément first accent",
      "H_qualification": "Same primary candidate as H; uncertainty alone is not an H collation count."
    },
    {
      "id": "A02",
      "location": "L17, second accent in l’élément",
      "C": "é",
      "H": "é",
      "reading": "\\unsure{é|ê}",
      "evidence": "The upper short stroke is angled with a possible lower-left companion; acute/circumflex remains unresolved locally.",
      "confidence": "low",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crops/13_du.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          391,
          2028,
          413,
          2068
        ]
      },
      "physical_cluster": "l’élément second accent",
      "H_qualification": "Same primary candidate as H; uncertainty alone is not an H collation count."
    },
    {
      "id": "R05",
      "location": "L17, after l’élément",
      "C": "du",
      "H": "de",
      "reading": "du",
      "evidence": "The d loop is followed by a low turning u-shaped run, not a separate e loop.",
      "confidence": "medium",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/13_du.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          531,
          2018,
          626,
          2055
        ]
      }
    },
    {
      "id": "A03",
      "location": "L19, first accent of éléments",
      "C": "é",
      "H": "é",
      "reading": "\\unsure{é|e}léments",
      "evidence": "The short pale horizontal above the initial e does not establish an acute direction; presence/absence of an accent remains qualified. The rest of the word is readable.",
      "confidence": "low",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crops/14_soit.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          266,
          2232,
          287,
          2268
        ]
      },
      "physical_cluster": "éléments first accent",
      "H_qualification": "Same primary candidate as H; uncertainty alone is not an H collation count."
    },
    {
      "id": "G06",
      "location": "L19, raised (soit Sigma_i^-)",
      "C": "insertion macro only",
      "H": "insertion macro only",
      "reading": "G06a complete hooked guide, elements/de/formula each once",
      "evidence": "The guide bends up from the gap after éléments, crosses the d ascender of de and terminates in a small return below the right parenthesis. No extra copy of de or the formula is supplied.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": true,
      "C_doubt_status": null,
      "readers_crop": "crops/14_soit.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          394,
          2159,
          660,
          2254
        ]
      },
      "physical_cluster": "G06"
    },
    {
      "id": "D12",
      "location": "L20, after cas",
      "C": "\\deleted{\\unsure{deux}} with raised card I=2",
      "H": "card I=2, no predecessor or raised state",
      "reading": "\\deleted{\\unsure{deux}} with raised card I=2",
      "evidence": "The first looped ascender and a few low rises survive in the crossed baseline word. They do not settle all letters. The raised cardinality formula is fully legible above it.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/15_deux.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          385,
          2264,
          566,
          2335
        ]
      },
      "source_C_doubt_row": "C018-D12",
      "physical_cluster": "G07",
      "counting_note": "One H omission/correction group, including raised placement of card I=2 and the crossed baseline word."
    },
    {
      "id": "G07",
      "location": "L20, cancellation and lower hook under card I=2",
      "C": "state macros without literal paths",
      "H": "no predecessor; plain card I=2",
      "reading": "G07a long cancellation; locally qualified G07b lower hook",
      "evidence": "The long rule crosses the baseline word. A distinct curved descent lies under the I/= region and joins the rule. Its character/guide role and chronology are unresolved; no extra algebraic sign is assigned.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "crops/15_deux.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          397,
          2290,
          559,
          2325
        ]
      },
      "physical_cluster": "G07",
      "H_parent": "D12",
      "path_confidence": {
        "G07a": "high",
        "G07b": "medium"
      },
      "interpretation_confidence": "low"
    },
    {
      "id": "D13a",
      "location": "L20, cancelled word before accented a",
      "C": "\\deleted{\\unsure{OK|cela}}",
      "H": "\\struck{et}",
      "reading": "\\deleted{\\unsure{OK|cela}}",
      "evidence": "Several overlapping loops and tall crossed strokes survive. OK is the primary candidate and cela remains supported; the recovered word is low confidence despite a clear cancellation state.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/16_OK_accent.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          654,
          2269,
          804,
          2330
        ]
      },
      "source_C_doubt_row": "C018-D13",
      "physical_cluster": "bottom cancelled word"
    },
    {
      "id": "D13b",
      "location": "L20, accent over a before fortiori",
      "C": "\\unsure{â|à}",
      "H": "à",
      "reading": "\\unsure{â|à}",
      "evidence": "A small detached roof-like wedge lies above a. A bent grave remains supported; H’s à is retained as the alternative.",
      "confidence": "low",
      "kind": "misread word",
      "diff_C": false,
      "diff_H": true,
      "C_doubt_status": "retained",
      "readers_crop": "crops/16_OK_accent.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          830,
          2281,
          887,
          2327
        ]
      },
      "source_C_doubt_row": "C018-D13",
      "physical_cluster": "bottom a accent"
    }
  ],
  "doubts": [
    {
      "id": "D02",
      "location": "L02, first parenthesis",
      "reading": "rècurrence",
      "alternatives": [
        "récurrence"
      ],
      "confidence": "low",
      "reason": "compact accent direction",
      "crop": "crops/02_recurrence.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          600,
          190,
          986,
          240
        ]
      }
    },
    {
      "id": "D04",
      "location": "L05, after raised (unique)",
      "reading": "de",
      "alternatives": [
        "des"
      ],
      "confidence": "low",
      "reason": "long terminal return",
      "crop": "crops/03_unique_de.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1095,
          532,
          1191,
          579
        ]
      }
    },
    {
      "id": "D06a",
      "location": "L10, small cancelled sign following the lemma J",
      "reading": "cancelled i",
      "alternatives": [
        "cancelled j",
        "cancelled comma"
      ],
      "confidence": "low",
      "reason": "overworked subscript",
      "crop": "crops/05_lemma.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1296,
          1219,
          1331,
          1262
        ]
      }
    },
    {
      "id": "D06b",
      "location": "L10, upper ring on lemma Pi",
      "reading": "upper circle",
      "alternatives": [
        "upper zero"
      ],
      "confidence": "low",
      "reason": "same visible ring supports both",
      "crop": "crops/05_lemma.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1267,
          1169,
          1293,
          1199
        ]
      }
    },
    {
      "id": "D08a",
      "location": "L13, subscript of inserted U",
      "reading": "alpha",
      "alternatives": [
        "x"
      ],
      "confidence": "medium",
      "reason": "loop/cross topology",
      "crop": "crops/08_ualpha.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          765,
          1486,
          795,
          1520
        ]
      }
    },
    {
      "id": "M01",
      "location": "L13, after inserted U, at guide junction",
      "reading": "comma-like hook",
      "alternatives": [
        "guide return"
      ],
      "confidence": "low",
      "reason": "hook shares guide junction",
      "crop": "crops/08_ualpha.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          803,
          1503,
          823,
          1523
        ]
      }
    },
    {
      "id": "N01",
      "location": "L13, raised Pi ring in the insertion",
      "reading": "upper circle",
      "alternatives": [
        "upper zero"
      ],
      "confidence": "low",
      "reason": "recurrence, printed primary without repeated unsure",
      "crop": "crops/08_ualpha.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          889,
          1456,
          968,
          1510
        ]
      }
    },
    {
      "id": "D10",
      "location": "L15, cancelled word after right parenthesis",
      "reading": "choisi",
      "alternatives": [
        "choisie"
      ],
      "confidence": "low",
      "reason": "obscured ending",
      "crop": "crops/10_second_E_choisi.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1402,
          1714,
          1586,
          1783
        ]
      }
    },
    {
      "id": "M02",
      "location": "L15, extra points after cancelled choisi",
      "reading": "two small detached points",
      "alternatives": [
        "letter/cancellation endpoints",
        "unassigned surface marks"
      ],
      "confidence": "low",
      "reason": "role/hand/origin unresolved",
      "crop": "crops/10_second_E_choisi.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          1565,
          1741,
          1583,
          1763
        ]
      }
    },
    {
      "id": "A01",
      "location": "L17, first accent in l’élément",
      "reading": "é",
      "alternatives": [
        "e"
      ],
      "confidence": "low",
      "reason": "pale first accent",
      "crop": "crops/13_du.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          332,
          2029,
          353,
          2067
        ]
      }
    },
    {
      "id": "A02",
      "location": "L17, second accent in l’élément",
      "reading": "é",
      "alternatives": [
        "ê"
      ],
      "confidence": "low",
      "reason": "compact angular accent",
      "crop": "crops/13_du.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          391,
          2028,
          413,
          2068
        ]
      }
    },
    {
      "id": "A03",
      "location": "L19, first accent of éléments",
      "reading": "éléments",
      "alternatives": [
        "eléments"
      ],
      "confidence": "low",
      "reason": "pale first accent",
      "crop": "crops/14_soit.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          266,
          2232,
          287,
          2268
        ]
      }
    },
    {
      "id": "D12",
      "location": "L20, after cas",
      "reading": "deux",
      "alternatives": [],
      "confidence": "low",
      "reason": "heavy deletion hides the full sequence",
      "crop": "crops/15_deux.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          385,
          2264,
          566,
          2335
        ]
      }
    },
    {
      "id": "G07",
      "location": "L20, cancellation and lower hook under card I=2",
      "reading": "lower hooked stroke",
      "alternatives": [
        "guide-related stroke",
        "unassigned stroke in formula/cancellation group"
      ],
      "confidence": "medium",
      "reason": "path supported, role unresolved",
      "crop": "crops/15_deux.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          397,
          2290,
          559,
          2325
        ]
      }
    },
    {
      "id": "D13a",
      "location": "L20, cancelled word before accented a",
      "reading": "OK",
      "alternatives": [
        "cela"
      ],
      "confidence": "low",
      "reason": "overlapping cancelled letters",
      "crop": "crops/16_OK_accent.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          654,
          2269,
          804,
          2330
        ]
      }
    },
    {
      "id": "D13b",
      "location": "L20, accent over a before fortiori",
      "reading": "â",
      "alternatives": [
        "à"
      ],
      "confidence": "low",
      "reason": "short roof-like accent",
      "crop": "crops/16_OK_accent.png",
      "bbox": {
        "system": "original full scan, upper-left origin",
        "xyxy": [
          830,
          2281,
          887,
          2327
        ]
      }
    }
  ],
  "notes": {
    "page_content": "Continued cardinality paragraph; definition of U_J,i; an underlined lemma and its proof with several cancellations and insertions.",
    "author_uncertainty": "No explicit question or authorial uncertainty formula is present. The final OK is transcribed as ink, not treated as a verified proof.",
    "titles_dates_page_counts": "Underlined Lemme; no date or authorial manuscript-page heading found. Archive numeral 17 appears at the lower-left edge and is kept only in a comment. H page{17} is its witness page wrapper under the brief.",
    "mathematics_led_decisions": "No mathematical computation, theorem check, reconstruction or correspondence was used. The final pi_0(X setminus Sigma_i) is retained from its angular Sigma strokes. H’s sic note is editorial apparatus, not additional manuscript wording.",
    "spelling": "que il retained; accents are local readings. New uncertainty on three lower accent positions is recorded separately. The recurrence word’s accent is retained as grave/acute uncertainty.",
    "boundary": "The fortiori f reaches the physical bottom paper edge. No unseen continuation is supplied.",
    "agreement_audit": "The line-by-line reading.md records agreed text and signs as visually read, rather than treating witness agreement as evidence."
  },
  "notation": [
    {
      "location": "L01",
      "form": "card J=card I-1=n-1",
      "latex": "\\operatorname{card}J=\\operatorname{card}I-1=n-1",
      "evidence": "small initial c; capital J and barred-serif I; two subtraction strokes and paired equals"
    },
    {
      "location": "L03",
      "form": "ens",
      "latex": "ens",
      "evidence": "joined e/n/s, no terminal point"
    },
    {
      "location": "L07, L11, L14",
      "form": "U_J,i",
      "latex": "U_{J,i}",
      "evidence": "lower J, separate comma and dotted i each inspected"
    },
    {
      "location": "L09/L11/L15/L19/L20",
      "form": "signed Sigma forms",
      "latex": "\\Sigma_i^+,\\Sigma_i^-,\\Sigma_j^+",
      "evidence": "local plus/minus retained; head strokes separately audited in S_bar_checks"
    },
    {
      "location": "L10 and L13",
      "form": "raised Pi ring",
      "latex": "first \\unsure{\\circ|0}, subsequent \\circ",
      "evidence": "both raised loops independently inspected; recurrence convention stated"
    },
    {
      "location": "L13/L20",
      "form": "alpha-like U subscript",
      "latex": "first \\unsure{\\alpha|x}; final \\alpha",
      "evidence": "first crossing loop remains qualified, final local loop resolved"
    },
    {
      "location": "L13/L15",
      "form": "overwritten Sigma beneath E",
      "latex": "\\deleted{\\Sigma}E",
      "evidence": "each predecessor decided independently from surviving diagonals"
    },
    {
      "location": "L13",
      "form": "separate upper rule over E_i",
      "latex": "\\overline{E_i}",
      "evidence": "independent upper rule above the E head; operation unassigned"
    },
    {
      "location": "L13",
      "form": "i.e.",
      "latex": "i.e.",
      "evidence": "both abbreviation points visible"
    },
    {
      "location": "L14/L20",
      "form": "unequal sign and open inclusion",
      "latex": "\\ne; \\subset",
      "evidence": "paired rules with crossing stroke; final small open wedge without lower equality rule"
    },
    {
      "location": "L19",
      "form": "pi_0(X setminus Sigma_i)",
      "latex": "\\pi_0(X\\setminus\\Sigma_i)",
      "evidence": "angular Sigma retained, with no inferred replacement by E"
    },
    {
      "location": "L20",
      "form": "card I=2",
      "latex": "\\operatorname{card}I=2",
      "evidence": "raised live formula; adjacent lower hook is drawn separately without an algebraic role"
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The brief’s recurring-glyph convention and original compound-row scope require separate local records even where the later occurrence is printed unmarked; D08b and N01 retain that mapping.",
    "A comma-like hook joins the insertion guide at one cusp; its character/guide role is left explicit and it is drawn once rather than supplying a second punctuation mark.",
    "The lower accented e marks retain local uncertainty; no page-wide accent normalization was used.",
    "The S witness supplies no scanned evidence or matching quoted expression here; the visibly separate E_i upper rule remains an independent C doubt decision."
  ]
}

--- A
+++ B
@@ -1,108 +1,116 @@
 \scanpage{18}
-cette dernière, si $\operatorname{card}J=\operatorname{card}I-1=n-1$, on verra (par \unsure{récurrence}) que le cardinal de l'ens des classes est $(n-1)+1=n$.
+cette dernière, si $\operatorname{card}J=\operatorname{card}I-1=n-1$, on verra (par \unsure{rècurrence|récurrence}) que le cardinal de l'ens des classes est $(n-1)+1=n$.
 
 Ceci posé, on voit d'abord que $E_i$ est dans
-% G01: manual source origin (805,390), full-scan pixels; x right, y down.
-% Words l'une, (unique), des/de, ces n occur only in this group.
-\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,178)}]
-\path[use as bounding box] (0,75) rectangle (710,205);
-\node[anchor=base west,inner sep=0,outer sep=0] at (24,178) {l'une};
-\node[anchor=base west,inner sep=0,outer sep=0] at (220,108) {\inserted{(unique)}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (286,178) {\unsure{des|de}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (452,178) {ces $n$};
-% G01.P1: bent insertion guide, including its raised right endpoint.
-\draw[line width=.35pt] (283,170) .. controls (270,120) and (321,128) .. (384,124) .. controls (426,124) and (462,114) .. (470,109) -- (470,104);
+% G01: full-scan origin (820,465), x right/y down; manual geometry.
+\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g01base)]
+\path[use as bounding box] (0,0) rectangle (670,145);
+\coordinate (g01base) at (0,115);
+\begin{scope}[shift={(-820,-465)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (830,574) {l'une};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1024,505) {\inserted{(unique)}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1100,574) {\unsure{des|de} ces $n$};
+\draw[line width=.35pt] (1089,559) .. controls (1075,521) and (1137,517) .. (1202,516) .. controls (1240,511) and (1271,507) .. (1278,498);
+\end{scope}
 \end{tikzpicture}
-classes, qui sont des ouverts. Soit $U_{J,i}$ la classe (ou ``composante'') qui contient $E_i$, et considérons les deux composantes $\Sigma_i^+,\Sigma_i^-$ de $X\setminus E_i$.
+classes, qui sont des ouverts. Soit $U_{J,i}$ la classe (ou ``\unsure{composante|composant}'') qui contient $E_i$, et considérons les deux composantes $\Sigma_i^+,\Sigma_i^-$ de $X\setminus E_i$.
 
-% G02: source origin (225,1145). The two manual rules replace a full-height tabular rule.
-\figure{\begin{tikzpicture}[x=.008cm,y=-.008cm]
-\path[use as bounding box] (0,0) rectangle (1420,265);
-\node[anchor=base west,inner sep=0,outer sep=0] at (80,108) {\rlap{Lemme}\phantom{\uline{Lemme}}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (415,88) {Toute classe de $\Pi_{J\deleted{\unsure{i|j|,}}}^{\unsure{\circ|0}}$, distincte};
-\node[anchor=base west,inner sep=0,outer sep=0] at (50,229) {de $U_{J,i}$, est contenue dans $\Sigma_i^+$ ou $\Sigma_i^-$};
-% G02.P1: single slightly rising underline beneath Lemme.
-\draw[line width=.5pt] (84,132) .. controls (174,123) and (248,122) .. (323,115);
-% G02.P2: separate left rule starts below the first row and ends beside the second.
-\draw[line width=.4pt] (31,104) .. controls (31,151) and (30,207) .. (35,238);
+% G02: complete lemma group. Full-scan origin (244,1145).
+% The underline and the left rule each occur once. The left rule begins
+% below the first textual line; its observed endpoints are preserved.
+\figure{\begin{tikzpicture}[x=.085mm,y=-.085mm,baseline=(g02base)]
+\path[use as bounding box] (0,0) rectangle (1400,255);
+\coordinate (g02base) at (0,238);
+\begin{scope}[shift={(-244,-1145)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (305,1248) {\rlap{Lemme}\phantom{\uline{Lemme}}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (645,1238) {Toute classe de $\Pi_{J\unsure{\deleted{j}|\deleted{i}|\deleted{,}|j}}^{\unsure{\circ|0}}$, distincte};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (275,1382) {de $U_{J,i}$, est contenue dans $\Sigma_i^+$ ou $\Sigma_i^-$};
+\draw[line width=.45pt] (308,1275) .. controls (390,1270) and (471,1264) .. (550,1258);
+\draw[line width=.35pt] (255,1247) .. controls (256,1290) and (257,1340) .. (259,1385);
+\end{scope}
 \end{tikzpicture}}
 
 C'est presque une tautologie : Dire
-% G03: source origin (220,1475). The following ordinary words classe donnée are outside this group once.
-\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,99)}]
-\path[use as bounding box] (0,20) rectangle (215,125);
-\node[anchor=base west,inner sep=0,outer sep=0] at (83,99) {\rlap{la}\phantom{\deleted{la}}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (20,48) {\inserted{qu'une}};
-% G03.P1: complete bent guide, with short right return.
-\draw[line width=.35pt] (49,109) .. controls (76,77) and (110,67) .. (158,62) .. controls (176,59) and (195,47) .. (204,40) .. controls (206,36) and (202,35) .. (197,37);
-% G03.P2: cancellation through la; no additional generic visible strike.
-\draw[line width=.7pt] (85,95) -- (147,83);
+% G03: whole adjoining correction group, origin (225,1465).
+% The short hook after U_alpha belongs to G03b, with no separate comma.
+\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g03base)]
+\path[use as bounding box] (0,-28) rectangle (925,140);
+\coordinate (g03base) at (0,111);
+\begin{scope}[shift={(-225,-1465)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (301,1576) {\deleted{la}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (244,1523) {\inserted{qu'une}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (390,1576) {classe donnée};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (738,1510) {\inserted{$U_{\unsure{\alpha|x}}$ de $\Pi_J^\circ$}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (801,1553) {ne contient};
+% G03a: qu'une guide, one connected run with a hooked upper endpoint.
+\draw[line width=.35pt] (271,1580) .. controls (279,1551) and (307,1541) .. (343,1538) .. controls (376,1535) and (414,1527) .. (423,1517) .. controls (426,1512) and (418,1510) .. (414,1513);
+% G03b: second guide and its connected small hook, two path commands.
+\draw[line width=.35pt] (760,1553) .. controls (759,1538) and (794,1517) .. (813,1510) .. controls (838,1511) and (861,1528) .. (891,1525) .. controls (938,1521) and (992,1501) .. (1011,1488);
+\draw[line width=.35pt] (813,1510) .. controls (823,1501) and (817,1498) .. (811,1501);
+\end{scope}
 \end{tikzpicture}
-classe donnée
-% G04: source origin (710,1445). U_alpha, de Pi_J, and baseline ne each occur once.
-% The hook represented by G04.P2 is C's comma candidate; its punctuation/guide role stays unresolved.
-\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,118)}]
-\path[use as bounding box] (0,10) rectangle (330,140);
-\node[anchor=base west,inner sep=0,outer sep=0] at (26,68) {\inserted{$U_{\unsure{\alpha|x}}$}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (112,53) {\inserted{de $\Pi_J^\circ$}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (89,118) {ne};
-% G04.P1: rising left guide, bowed middle, and right return.
-\draw[line width=.35pt] (49,110) .. controls (49,99) and (79,81) .. (105,68) .. controls (134,59) and (158,89) .. (211,79) .. controls (260,68) and (293,55) .. (301,43) -- (298,40);
-% G04.P2: one qualified hook at fixed local origin (98,52), base-west anchored.
-\node[anchor=base west,inner sep=0,outer sep=0] at (98,52) {\unsure{\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (16,20);
-\draw[line width=.45pt] (1,3) .. controls (9,0) and (14,7) .. (7,16);
+pas $\deleted{\Sigma}$\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g04base)]
+% G04: corrected E_i and the separate upper stroke. Outer origin
+% (1308,1480); inner overmark origin (1324,1492), baseline y=12.
+% Closure-bar/remnant role is unresolved; the visible stroke is retained
+% once, including its short returning right end, under local unsure.
+\path[use as bounding box] (0,0) rectangle (85,85);
+\coordinate (g04base) at (0,67);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,67) {$E_i$};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (16,24) {\unsure{\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g04markbase)]
+\path[use as bounding box] (0,0) rectangle (55,12);
+\coordinate (g04markbase) at (0,12);
+\draw[line width=.45pt] (0,6) .. controls (17,5) and (34,6) .. (47,6) -- (31,10) -- (43,6);
 \end{tikzpicture}}};
 \end{tikzpicture}
-contient pas $\deleted{\Sigma}\overline{E_i}$ i.e. est $\ne U_{J,i}$, signifie que il existe un $j\in J$ tel que le $\Sigma_j^+\in\pi_0(X\setminus\deleted{\Sigma}E_{\unsure{j|J}})$
-% G05: source origin (1405,1720); uncertain word, single literal cancellation, two detached points.
-\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline={(0,50)}]
-\path[use as bounding box] (0,0) rectangle (190,80);
-\node[anchor=base west,inner sep=0,outer sep=0] at (0,50) {\rlap{\unsure{choisi|choisie}}\phantom{\deleted{\unsure{choisi|choisie}}}};
-% G05.P1: cancellation run through the word.
-\draw[line width=.65pt] (7,39) .. controls (55,40) and (109,41) .. (160,43);
-% G05.P2-P3: detached points at fixed local origin (165,32); no character or role supplied.
-\node[anchor=base west,inner sep=0,outer sep=0] at (165,32) {\unsure{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0pt]
-\path[use as bounding box] (0,-8) rectangle (13,8);
-\fill (2,2) ellipse [x radius=1,y radius=1.4];
-\fill (8,-5) ellipse [x radius=.9,y radius=1.2];
+i.e. est $\ne U_{J,i}$, signifie que il existe un $j\in J$ tel que le $\Sigma_j^+\in\pi_0(X\setminus\deleted{\Sigma}E_{\unsure{j|J}})$
+% G05: crossed word plus the two additional upper/right points.
+% Outer origin (1408,1712); dots' fixed local origin (1569,1737).
+\begin{tikzpicture}[x=.07mm,y=-.07mm,baseline=(g05base)]
+\path[use as bounding box] (0,0) rectangle (190,100);
+\coordinate (g05base) at (0,70);
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,70) {\deleted{\unsure{choisi|choisie}}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (161,47) {\unsure{\begin{tikzpicture}[x=.07mm,y=-.07mm,baseline=(g05markbase)]
+\path[use as bounding box] (0,0) rectangle (20,22);
+\coordinate (g05markbase) at (0,22);
+\fill (5,16) circle[radius=1.2];
+\fill (10,6) circle[radius=1.2];
 \end{tikzpicture}}};
 \end{tikzpicture}
-``composant'' de cette classe \deleted{est} est l'élément du $\pi_0$ qui ne contient pas $E_i$; il est donc contenu dans l'un des
-% G06: source origin (240,2080). Complete elements/insert/de group; following pi expression occurs outside once.
-\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,176)}]
-\path[use as bounding box] (0,90) rectangle (430,195);
-\node[anchor=base west,inner sep=0,outer sep=0] at (30,180) {éléments};
-\node[anchor=base west,inner sep=0,outer sep=0] at (155,133) {\inserted{(soit $\Sigma_i^-$)}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (351,168) {de};
-% G06.P1: insertion guide with small raised right return.
-\draw[line width=.35pt] (319,165) .. controls (320,141) and (359,143) .. (405,127) -- (409,124) -- (405,120);
+``\unsure{composant|composante}'' de cette classe \deleted{est} est l'\unsure{élêment|élément} du $\pi_0$ qui ne contient pas $E_i$; il est donc contenu dans l'un des
+% G06: whole éléments / (soit Sigma_i^-) / de group, origin (251,2160).
+\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g06base)]
+\path[use as bounding box] (0,0) rectangle (470,126);
+\coordinate (g06base) at (0,95);
+\begin{scope}[shift={(-251,-2160)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (265,2255) {éléments};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (399,2201) {\inserted{(soit $\Sigma_i^-$)}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (595,2248) {de};
+\draw[line width=.35pt] (560,2251) .. controls (563,2228) and (599,2215) .. (646,2205) .. controls (655,2202) and (653,2199) .. (647,2197);
+\end{scope}
 \end{tikzpicture}
 $\pi_0(X\setminus\Sigma_i)$, d'après l'étude du cas
-% G07: source origin (245,2240); deleted word, raised replacement and comma occur once.
-\begin{tikzpicture}[x=.008cm,y=-.008cm,baseline={(0,85)}]
-\path[use as bounding box] (135,15) rectangle (335,110);
-\node[anchor=base west,inner sep=0,outer sep=0] at (153,85) {\rlap{\unsure{deux}}\phantom{\deleted{\unsure{deux}}}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (145,49) {\inserted{$\operatorname{card}I=2$}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (300,95) {,};
-% G07.P1: long slightly rising cancellation beneath the inserted formula.
-\draw[line width=.65pt] (152,86) .. controls (193,79) and (252,84) .. (303,78);
-\end{tikzpicture}
-\deleted{\unsure{cela|OK}} \unsure{â|à} fortiori $U_\alpha\subset\Sigma_i^-$,
-% G08: source origin (1440,2250). OK's rising stroke has unresolved joining/cancellation state.
-\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline={(0,55)}]
-\path[use as bounding box] (0,0) rectangle (210,95);
-\node[anchor=base west,inner sep=0,outer sep=0] at (11,55) {\unsure{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0pt]
-\path[use as bounding box] (0,-45) rectangle (85,8);
-\node[anchor=base west,inner sep=0,outer sep=0] at (0,0) {\rlap{OK}\phantom{\deleted{OK}}};
-% G08.P1: the visible rising crossing/joining stroke, drawn only here.
-\draw[line width=.35pt] (0,-15) .. controls (24,-21) and (51,-32) .. (73,-40);
-\end{tikzpicture}}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (127,61) {.};
-% G08.P2: faint detached spot; shape, hand, surface origin and role remain qualified.
-\node[anchor=base west,inner sep=0,outer sep=0] at (192,42) {\unsure{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (6,6);
-\fill[gray] (2,2) ellipse [x radius=1.1,y radius=1.6];
-\end{tikzpicture}}};
-\end{tikzpicture}
+% G07: lower correction, origin (382,2265). Actual cancellation drawn
+% once; the invisible deleted copy supplies annotation/dimensions only.
+\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g07base)]
+\path[use as bounding box] (0,0) rectangle (190,80);
+\coordinate (g07base) at (0,59);
+\begin{scope}[shift={(-382,-2265)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (395,2323) {\rlap{\unsure{deux}}\phantom{\deleted{\unsure{deux}}}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (389,2297) {\inserted{$\operatorname{card}I=2$}};
+\draw[line width=.55pt] (395,2325) .. controls (443,2318) and (509,2322) .. (556,2318);
+\end{scope}
+\end{tikzpicture},
+\deleted{\unsure{OK|cela|et}} \unsure{â|à} fortiori $U_\alpha\subset\Sigma_i^-$,
+% G08: final OK and its rising transverse stroke, origin (1450,2255).
+% Whole-state candidates: live OK; deleted OK. The local unsure retains
+% this unresolved state; no extra generic cancellation line is drawn.
+\unsure{\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g08base)]
+\path[use as bounding box] (0,0) rectangle (95,85);
+\coordinate (g08base) at (0,70);
+\begin{scope}[shift={(-1450,-2255)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1455,2323) {\rlap{OK}\phantom{\deleted{OK}}};
+\draw[line width=.3pt] (1452,2293) .. controls (1470,2287) and (1497,2279) .. (1534,2264);
+\end{scope}
+\end{tikzpicture}}.
 % archive sheet number: 17

--- A
+++ C
@@ -1,108 +1,123 @@
 \scanpage{18}
-cette dernière, si $\operatorname{card}J=\operatorname{card}I-1=n-1$, on verra (par \unsure{récurrence}) que le cardinal de l'ens des classes est $(n-1)+1=n$.
+cette dernière, si $\operatorname{card}J=\operatorname{card}I-1=n-1$, on verra (par r\unsure{è|é}currence) que le cardinal de l'ens des classes est $(n-1)+1=n$.
 
 Ceci posé, on voit d'abord que $E_i$ est dans
-% G01: manual source origin (805,390), full-scan pixels; x right, y down.
-% Words l'une, (unique), des/de, ces n occur only in this group.
-\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,178)}]
-\path[use as bounding box] (0,75) rectangle (710,205);
-\node[anchor=base west,inner sep=0,outer sep=0] at (24,178) {l'une};
-\node[anchor=base west,inner sep=0,outer sep=0] at (220,108) {\inserted{(unique)}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (286,178) {\unsure{des|de}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (452,178) {ces $n$};
-% G01.P1: bent insertion guide, including its raised right endpoint.
-\draw[line width=.35pt] (283,170) .. controls (270,120) and (321,128) .. (384,124) .. controls (426,124) and (462,114) .. (470,109) -- (470,104);
+% G01: original full-scan origin (820,455); x=0.010cm, y=-0.010cm.
+% Fixed drawing rectangle 670 by 160 source-coordinate units. The words occur here once.
+\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g01base)]
+\path[use as bounding box] (0,0) rectangle (670,160);
+\coordinate (g01base) at (0,113);
+\begin{scope}[shift={(-820,-455)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (833,568) {l'une};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1100,568) {\unsure{de|des}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1269,568) {ces $n$};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1028,500) {\inserted{(unique)}};
+% G01a: complete long insertion guide, with bent left end and upturned right end.
+\draw[line width=.45pt] (1089,559) .. controls (1078,530) and (1100,519) .. (1154,517) .. controls (1208,517) and (1258,513) .. (1277,499);
+\end{scope}
 \end{tikzpicture}
 classes, qui sont des ouverts. Soit $U_{J,i}$ la classe (ou ``composante'') qui contient $E_i$, et considérons les deux composantes $\Sigma_i^+,\Sigma_i^-$ de $X\setminus E_i$.
 
-% G02: source origin (225,1145). The two manual rules replace a full-height tabular rule.
-\figure{\begin{tikzpicture}[x=.008cm,y=-.008cm]
-\path[use as bounding box] (0,0) rectangle (1420,265);
-\node[anchor=base west,inner sep=0,outer sep=0] at (80,108) {\rlap{Lemme}\phantom{\uline{Lemme}}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (415,88) {Toute classe de $\Pi_{J\deleted{\unsure{i|j|,}}}^{\unsure{\circ|0}}$, distincte};
-\node[anchor=base west,inner sep=0,outer sep=0] at (50,229) {de $U_{J,i}$, est contenue dans $\Sigma_i^+$ ou $\Sigma_i^-$};
-% G02.P1: single slightly rising underline beneath Lemme.
-\draw[line width=.5pt] (84,132) .. controls (174,123) and (248,122) .. (323,115);
-% G02.P2: separate left rule starts below the first row and ends beside the second.
-\draw[line width=.4pt] (31,104) .. controls (31,151) and (30,207) .. (35,238);
+% G02: complete two-line lemma group; full-scan origin (230,1135).
+% x=0.010cm, y=-0.010cm; fixed 1410 by 270 source-coordinate rectangle.
+\figure{\begin{tikzpicture}[x=.010cm,y=-.010cm]
+\path[use as bounding box] (0,0) rectangle (1410,270);
+\begin{scope}[shift={(-230,-1135)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (300,1250) {\rlap{Lemme}\phantom{\uline{Lemme}}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (640,1238) {Toute classe de $\Pi_{J\deleted{\unsure{i|j|,}}}^{\unsure{\circ|0}}$, distincte};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (275,1376) {de $U_{J,i}$, est contenue dans $\Sigma_i^+$ ou $\Sigma_i^-$};
+% G02a: heading underline; G02b: separate, short left rule.
+\draw[line width=.5pt] (307,1275) .. controls (382,1268) and (467,1262) .. (550,1258);
+\draw[line width=.5pt] (254,1248) .. controls (255,1299) and (257,1351) .. (259,1383);
+\end{scope}
 \end{tikzpicture}}
 
 C'est presque une tautologie : Dire
-% G03: source origin (220,1475). The following ordinary words classe donnée are outside this group once.
-\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,99)}]
-\path[use as bounding box] (0,20) rectangle (215,125);
-\node[anchor=base west,inner sep=0,outer sep=0] at (83,99) {\rlap{la}\phantom{\deleted{la}}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (20,48) {\inserted{qu'une}};
-% G03.P1: complete bent guide, with short right return.
-\draw[line width=.35pt] (49,109) .. controls (76,77) and (110,67) .. (158,62) .. controls (176,59) and (195,47) .. (204,40) .. controls (206,36) and (202,35) .. (197,37);
-% G03.P2: cancellation through la; no additional generic visible strike.
-\draw[line width=.7pt] (85,95) -- (147,83);
+% G03: qu'une/la/classe group, full-scan origin (235,1480), fixed 310 by 125 rectangle.
+\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g03base)]
+\path[use as bounding box] (0,0) rectangle (310,125);
+\coordinate (g03base) at (0,91);
+\begin{scope}[shift={(-235,-1480)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (244,1522) {\inserted{qu'une}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (306,1568) {\rlap{la}\phantom{\deleted{la}}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (390,1575) {classe};
+% G03a/b: observed interrupted insertion guide; the q descender belongs to qu'une.
+\draw[line width=.4pt] (270,1578) .. controls (276,1566) and (288,1558) .. (301,1554);
+\draw[line width=.4pt] (308,1549) .. controls (331,1541) and (352,1538) .. (369,1535) .. controls (389,1529) and (414,1519) .. (420,1514) .. controls (423,1511) and (417,1510) .. (412,1511);
+% G03c: the actual lower cancellation stroke, without an additional generic rule.
+\draw[line width=.65pt] (306,1568) .. controls (328,1569) and (348,1563) .. (367,1558);
+\end{scope}
 \end{tikzpicture}
-classe donnée
-% G04: source origin (710,1445). U_alpha, de Pi_J, and baseline ne each occur once.
-% The hook represented by G04.P2 is C's comma candidate; its punctuation/guide role stays unresolved.
-\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,118)}]
-\path[use as bounding box] (0,10) rectangle (330,140);
-\node[anchor=base west,inner sep=0,outer sep=0] at (26,68) {\inserted{$U_{\unsure{\alpha|x}}$}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (112,53) {\inserted{de $\Pi_J^\circ$}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (89,118) {ne};
-% G04.P1: rising left guide, bowed middle, and right return.
-\draw[line width=.35pt] (49,110) .. controls (49,99) and (79,81) .. (105,68) .. controls (134,59) and (158,89) .. (211,79) .. controls (260,68) and (293,55) .. (301,43) -- (298,40);
-% G04.P2: one qualified hook at fixed local origin (98,52), base-west anchored.
-\node[anchor=base west,inner sep=0,outer sep=0] at (98,52) {\unsure{\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (16,20);
-\draw[line width=.45pt] (1,3) .. controls (9,0) and (14,7) .. (7,16);
+% G04: donnée / inserted name / ne group. Full-scan origin (530,1445), fixed 525 by 160.
+\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g04base)]
+\path[use as bounding box] (0,0) rectangle (525,160);
+\coordinate (g04base) at (0,111);
+\begin{scope}[shift={(-530,-1445)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (560,1556) {donnée};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (797,1548) {ne};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (737,1507) {\inserted{$U_{\unsure{\alpha|x}}$\quad de $\Pi_J^\circ$}};
+% G04a: complete guide; no separate cancelled un is supplied.
+\draw[line width=.4pt] (761,1554) .. controls (762,1540) and (791,1528) .. (811,1516) .. controls (853,1528) and (876,1534) .. (908,1521) .. controls (957,1511) and (1006,1500) .. (1012,1487);
+% G04b: one locally qualified comma-like hook at the guide junction.
+% Nested local origin (806,1504), baseline (0,0), base-west placement and zero separation.
+% Its role as comma or guide return is unsettled; no second printed comma is added.
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (806,1504) {\unsure{\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g04hookbase)]
+\path[use as bounding box] (0,0) rectangle (15,17);
+\coordinate (g04hookbase) at (0,0);
+\draw[line width=.45pt] (0,4) .. controls (9,0) and (15,6) .. (6,13);
 \end{tikzpicture}}};
+\end{scope}
 \end{tikzpicture}
-contient pas $\deleted{\Sigma}\overline{E_i}$ i.e. est $\ne U_{J,i}$, signifie que il existe un $j\in J$ tel que le $\Sigma_j^+\in\pi_0(X\setminus\deleted{\Sigma}E_{\unsure{j|J}})$
-% G05: source origin (1405,1720); uncertain word, single literal cancellation, two detached points.
-\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline={(0,50)}]
-\path[use as bounding box] (0,0) rectangle (190,80);
-\node[anchor=base west,inner sep=0,outer sep=0] at (0,50) {\rlap{\unsure{choisi|choisie}}\phantom{\deleted{\unsure{choisi|choisie}}}};
-% G05.P1: cancellation run through the word.
-\draw[line width=.65pt] (7,39) .. controls (55,40) and (109,41) .. (160,43);
-% G05.P2-P3: detached points at fixed local origin (165,32); no character or role supplied.
-\node[anchor=base west,inner sep=0,outer sep=0] at (165,32) {\unsure{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0pt]
-\path[use as bounding box] (0,-8) rectangle (13,8);
-\fill (2,2) ellipse [x radius=1,y radius=1.4];
-\fill (8,-5) ellipse [x radius=.9,y radius=1.2];
+contient pas $\deleted{\Sigma}\overline{E_i}$ i.e. est $\ne U_{J,i}$, signifie que il existe un $j\in J$ tel que le $\Sigma_j^+\in\pi_0(X\setminus\deleted{\Sigma}E_j)$
+% G05: cancelled word and two detached endpoint points, origin (1400,1715), fixed 200 by 90.
+\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g05base)]
+\path[use as bounding box] (0,0) rectangle (200,90);
+\coordinate (g05base) at (0,49);
+\begin{scope}[shift={(-1400,-1715)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1410,1764) {\rlap{\unsure{choisi|choisie}}\phantom{\deleted{\unsure{choisi|choisie}}}};
+% G05a: single cancellation stroke.
+\draw[line width=.6pt] (1410,1757) .. controls (1468,1756) and (1524,1757) .. (1566,1758);
+% G05b/c: both extra endpoint points occur once; the two i dots stay within the word.
+% Nested origin (1567,1745), baseline (0,0), base-west anchor and zero separation.
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1567,1745) {\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g05pointsbase)]
+\path[use as bounding box] (0,0) rectangle (12,12);
+\coordinate (g05pointsbase) at (0,0);
+\fill (2,8) circle[radius=1.1];
+\fill (9,2) circle[radius=1.0];
 \end{tikzpicture}}};
+\end{scope}
 \end{tikzpicture}
-``composant'' de cette classe \deleted{est} est l'élément du $\pi_0$ qui ne contient pas $E_i$; il est donc contenu dans l'un des
-% G06: source origin (240,2080). Complete elements/insert/de group; following pi expression occurs outside once.
-\begin{tikzpicture}[x=.007cm,y=-.007cm,baseline={(0,176)}]
-\path[use as bounding box] (0,90) rectangle (430,195);
-\node[anchor=base west,inner sep=0,outer sep=0] at (30,180) {éléments};
-\node[anchor=base west,inner sep=0,outer sep=0] at (155,133) {\inserted{(soit $\Sigma_i^-$)}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (351,168) {de};
-% G06.P1: insertion guide with small raised right return.
-\draw[line width=.35pt] (319,165) .. controls (320,141) and (359,143) .. (405,127) -- (409,124) -- (405,120);
-\end{tikzpicture}
-$\pi_0(X\setminus\Sigma_i)$, d'après l'étude du cas
-% G07: source origin (245,2240); deleted word, raised replacement and comma occur once.
-\begin{tikzpicture}[x=.008cm,y=-.008cm,baseline={(0,85)}]
-\path[use as bounding box] (135,15) rectangle (335,110);
-\node[anchor=base west,inner sep=0,outer sep=0] at (153,85) {\rlap{\unsure{deux}}\phantom{\deleted{\unsure{deux}}}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (145,49) {\inserted{$\operatorname{card}I=2$}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (300,95) {,};
-% G07.P1: long slightly rising cancellation beneath the inserted formula.
-\draw[line width=.65pt] (152,86) .. controls (193,79) and (252,84) .. (303,78);
-\end{tikzpicture}
-\deleted{\unsure{cela|OK}} \unsure{â|à} fortiori $U_\alpha\subset\Sigma_i^-$,
-% G08: source origin (1440,2250). OK's rising stroke has unresolved joining/cancellation state.
-\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline={(0,55)}]
-\path[use as bounding box] (0,0) rectangle (210,95);
-\node[anchor=base west,inner sep=0,outer sep=0] at (11,55) {\unsure{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0pt]
-\path[use as bounding box] (0,-45) rectangle (85,8);
-\node[anchor=base west,inner sep=0,outer sep=0] at (0,0) {\rlap{OK}\phantom{\deleted{OK}}};
-% G08.P1: the visible rising crossing/joining stroke, drawn only here.
-\draw[line width=.35pt] (0,-15) .. controls (24,-21) and (51,-32) .. (73,-40);
+``composant'' de cette classe \deleted{est} est l'\unsure{é|e}l\unsure{é|ê}ment du $\pi_0$ qui ne contient pas $E_i$; il est donc contenu dans l'un des
+% G06: whole éléments / (soit Sigma) / de / pi_0 group, origin (245,2135), fixed 795 by 155.
+\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g06base)]
+\path[use as bounding box] (0,0) rectangle (795,155);
+\coordinate (g06base) at (0,125);
+\begin{scope}[shift={(-245,-2135)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (270,2260) {\unsure{é|e}léments};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (396,2213) {\inserted{(soit $\Sigma_i^-$)}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (595,2245) {de};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (719,2244) {$\pi_0(X\setminus\Sigma_i)$};
+% G06a: guide crossing the ascender of de, with its full right hook.
+\draw[line width=.4pt] (558,2247) .. controls (562,2228) and (580,2225) .. (612,2221) .. controls (632,2218) and (646,2213) .. (650,2208) .. controls (647,2204) and (645,2202) .. (642,2204);
+\end{scope}
+\end{tikzpicture}, d'après l'étude du
+% G07: cas / cancelled deux / raised card I=2, origin (245,2240), fixed 370 by 123.
+\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g07base)]
+\path[use as bounding box] (0,0) rectangle (370,123);
+\coordinate (g07base) at (0,85);
+\begin{scope}[shift={(-245,-2240)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (275,2325) {cas};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (400,2321) {\rlap{\unsure{deux}}\phantom{\deleted{\unsure{deux}}}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (386,2302) {\inserted{$\operatorname{card}I=2$}};
+% G07a: complete long cancellation rule, kept once.
+\draw[line width=.65pt] (399,2320) .. controls (438,2313) and (483,2317) .. (515,2314) .. controls (531,2312) and (546,2311) .. (555,2312);
+% G07b: supported lower hook below the I/= region; its guide/letter role remains unsettled.
+% Nested origin (510,2290), baseline (0,0), base-west placement and zero separation.
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (510,2290) {\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g07hookbase)]
+\path[use as bounding box] (0,0) rectangle (12,27);
+\coordinate (g07hookbase) at (0,0);
+\draw[line width=.5pt] (4,4) .. controls (10,10) and (8,18) .. (1,24);
 \end{tikzpicture}}};
-\node[anchor=base west,inner sep=0,outer sep=0] at (127,61) {.};
-% G08.P2: faint detached spot; shape, hand, surface origin and role remain qualified.
-\node[anchor=base west,inner sep=0,outer sep=0] at (192,42) {\unsure{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0pt]
-\path[use as bounding box] (0,0) rectangle (6,6);
-\fill[gray] (2,2) ellipse [x radius=1.1,y radius=1.6];
-\end{tikzpicture}}};
-\end{tikzpicture}
+\end{scope}
+\end{tikzpicture}, \deleted{\unsure{OK|cela}} \unsure{â|à} fortiori $U_\alpha\subset\Sigma_i^-$, OK.
 % archive sheet number: 17

--- B
+++ C
@@ -1,116 +1,123 @@
 \scanpage{18}
-cette dernière, si $\operatorname{card}J=\operatorname{card}I-1=n-1$, on verra (par \unsure{rècurrence|récurrence}) que le cardinal de l'ens des classes est $(n-1)+1=n$.
+cette dernière, si $\operatorname{card}J=\operatorname{card}I-1=n-1$, on verra (par r\unsure{è|é}currence) que le cardinal de l'ens des classes est $(n-1)+1=n$.
 
 Ceci posé, on voit d'abord que $E_i$ est dans
-% G01: full-scan origin (820,465), x right/y down; manual geometry.
-\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g01base)]
-\path[use as bounding box] (0,0) rectangle (670,145);
-\coordinate (g01base) at (0,115);
-\begin{scope}[shift={(-820,-465)}]
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (830,574) {l'une};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1024,505) {\inserted{(unique)}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1100,574) {\unsure{des|de} ces $n$};
-\draw[line width=.35pt] (1089,559) .. controls (1075,521) and (1137,517) .. (1202,516) .. controls (1240,511) and (1271,507) .. (1278,498);
+% G01: original full-scan origin (820,455); x=0.010cm, y=-0.010cm.
+% Fixed drawing rectangle 670 by 160 source-coordinate units. The words occur here once.
+\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g01base)]
+\path[use as bounding box] (0,0) rectangle (670,160);
+\coordinate (g01base) at (0,113);
+\begin{scope}[shift={(-820,-455)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (833,568) {l'une};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1100,568) {\unsure{de|des}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1269,568) {ces $n$};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1028,500) {\inserted{(unique)}};
+% G01a: complete long insertion guide, with bent left end and upturned right end.
+\draw[line width=.45pt] (1089,559) .. controls (1078,530) and (1100,519) .. (1154,517) .. controls (1208,517) and (1258,513) .. (1277,499);
 \end{scope}
 \end{tikzpicture}
-classes, qui sont des ouverts. Soit $U_{J,i}$ la classe (ou ``\unsure{composante|composant}'') qui contient $E_i$, et considérons les deux composantes $\Sigma_i^+,\Sigma_i^-$ de $X\setminus E_i$.
+classes, qui sont des ouverts. Soit $U_{J,i}$ la classe (ou ``composante'') qui contient $E_i$, et considérons les deux composantes $\Sigma_i^+,\Sigma_i^-$ de $X\setminus E_i$.
 
-% G02: complete lemma group. Full-scan origin (244,1145).
-% The underline and the left rule each occur once. The left rule begins
-% below the first textual line; its observed endpoints are preserved.
-\figure{\begin{tikzpicture}[x=.085mm,y=-.085mm,baseline=(g02base)]
-\path[use as bounding box] (0,0) rectangle (1400,255);
-\coordinate (g02base) at (0,238);
-\begin{scope}[shift={(-244,-1145)}]
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (305,1248) {\rlap{Lemme}\phantom{\uline{Lemme}}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (645,1238) {Toute classe de $\Pi_{J\unsure{\deleted{j}|\deleted{i}|\deleted{,}|j}}^{\unsure{\circ|0}}$, distincte};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (275,1382) {de $U_{J,i}$, est contenue dans $\Sigma_i^+$ ou $\Sigma_i^-$};
-\draw[line width=.45pt] (308,1275) .. controls (390,1270) and (471,1264) .. (550,1258);
-\draw[line width=.35pt] (255,1247) .. controls (256,1290) and (257,1340) .. (259,1385);
+% G02: complete two-line lemma group; full-scan origin (230,1135).
+% x=0.010cm, y=-0.010cm; fixed 1410 by 270 source-coordinate rectangle.
+\figure{\begin{tikzpicture}[x=.010cm,y=-.010cm]
+\path[use as bounding box] (0,0) rectangle (1410,270);
+\begin{scope}[shift={(-230,-1135)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (300,1250) {\rlap{Lemme}\phantom{\uline{Lemme}}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (640,1238) {Toute classe de $\Pi_{J\deleted{\unsure{i|j|,}}}^{\unsure{\circ|0}}$, distincte};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (275,1376) {de $U_{J,i}$, est contenue dans $\Sigma_i^+$ ou $\Sigma_i^-$};
+% G02a: heading underline; G02b: separate, short left rule.
+\draw[line width=.5pt] (307,1275) .. controls (382,1268) and (467,1262) .. (550,1258);
+\draw[line width=.5pt] (254,1248) .. controls (255,1299) and (257,1351) .. (259,1383);
 \end{scope}
 \end{tikzpicture}}
 
 C'est presque une tautologie : Dire
-% G03: whole adjoining correction group, origin (225,1465).
-% The short hook after U_alpha belongs to G03b, with no separate comma.
-\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g03base)]
-\path[use as bounding box] (0,-28) rectangle (925,140);
-\coordinate (g03base) at (0,111);
-\begin{scope}[shift={(-225,-1465)}]
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (301,1576) {\deleted{la}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (244,1523) {\inserted{qu'une}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (390,1576) {classe donnée};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (738,1510) {\inserted{$U_{\unsure{\alpha|x}}$ de $\Pi_J^\circ$}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (801,1553) {ne contient};
-% G03a: qu'une guide, one connected run with a hooked upper endpoint.
-\draw[line width=.35pt] (271,1580) .. controls (279,1551) and (307,1541) .. (343,1538) .. controls (376,1535) and (414,1527) .. (423,1517) .. controls (426,1512) and (418,1510) .. (414,1513);
-% G03b: second guide and its connected small hook, two path commands.
-\draw[line width=.35pt] (760,1553) .. controls (759,1538) and (794,1517) .. (813,1510) .. controls (838,1511) and (861,1528) .. (891,1525) .. controls (938,1521) and (992,1501) .. (1011,1488);
-\draw[line width=.35pt] (813,1510) .. controls (823,1501) and (817,1498) .. (811,1501);
+% G03: qu'une/la/classe group, full-scan origin (235,1480), fixed 310 by 125 rectangle.
+\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g03base)]
+\path[use as bounding box] (0,0) rectangle (310,125);
+\coordinate (g03base) at (0,91);
+\begin{scope}[shift={(-235,-1480)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (244,1522) {\inserted{qu'une}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (306,1568) {\rlap{la}\phantom{\deleted{la}}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (390,1575) {classe};
+% G03a/b: observed interrupted insertion guide; the q descender belongs to qu'une.
+\draw[line width=.4pt] (270,1578) .. controls (276,1566) and (288,1558) .. (301,1554);
+\draw[line width=.4pt] (308,1549) .. controls (331,1541) and (352,1538) .. (369,1535) .. controls (389,1529) and (414,1519) .. (420,1514) .. controls (423,1511) and (417,1510) .. (412,1511);
+% G03c: the actual lower cancellation stroke, without an additional generic rule.
+\draw[line width=.65pt] (306,1568) .. controls (328,1569) and (348,1563) .. (367,1558);
 \end{scope}
 \end{tikzpicture}
-pas $\deleted{\Sigma}$\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g04base)]
-% G04: corrected E_i and the separate upper stroke. Outer origin
-% (1308,1480); inner overmark origin (1324,1492), baseline y=12.
-% Closure-bar/remnant role is unresolved; the visible stroke is retained
-% once, including its short returning right end, under local unsure.
-\path[use as bounding box] (0,0) rectangle (85,85);
-\coordinate (g04base) at (0,67);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,67) {$E_i$};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (16,24) {\unsure{\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g04markbase)]
-\path[use as bounding box] (0,0) rectangle (55,12);
-\coordinate (g04markbase) at (0,12);
-\draw[line width=.45pt] (0,6) .. controls (17,5) and (34,6) .. (47,6) -- (31,10) -- (43,6);
+% G04: donnée / inserted name / ne group. Full-scan origin (530,1445), fixed 525 by 160.
+\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g04base)]
+\path[use as bounding box] (0,0) rectangle (525,160);
+\coordinate (g04base) at (0,111);
+\begin{scope}[shift={(-530,-1445)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (560,1556) {donnée};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (797,1548) {ne};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (737,1507) {\inserted{$U_{\unsure{\alpha|x}}$\quad de $\Pi_J^\circ$}};
+% G04a: complete guide; no separate cancelled un is supplied.
+\draw[line width=.4pt] (761,1554) .. controls (762,1540) and (791,1528) .. (811,1516) .. controls (853,1528) and (876,1534) .. (908,1521) .. controls (957,1511) and (1006,1500) .. (1012,1487);
+% G04b: one locally qualified comma-like hook at the guide junction.
+% Nested local origin (806,1504), baseline (0,0), base-west placement and zero separation.
+% Its role as comma or guide return is unsettled; no second printed comma is added.
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (806,1504) {\unsure{\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g04hookbase)]
+\path[use as bounding box] (0,0) rectangle (15,17);
+\coordinate (g04hookbase) at (0,0);
+\draw[line width=.45pt] (0,4) .. controls (9,0) and (15,6) .. (6,13);
 \end{tikzpicture}}};
-\end{tikzpicture}
-i.e. est $\ne U_{J,i}$, signifie que il existe un $j\in J$ tel que le $\Sigma_j^+\in\pi_0(X\setminus\deleted{\Sigma}E_{\unsure{j|J}})$
-% G05: crossed word plus the two additional upper/right points.
-% Outer origin (1408,1712); dots' fixed local origin (1569,1737).
-\begin{tikzpicture}[x=.07mm,y=-.07mm,baseline=(g05base)]
-\path[use as bounding box] (0,0) rectangle (190,100);
-\coordinate (g05base) at (0,70);
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,70) {\deleted{\unsure{choisi|choisie}}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (161,47) {\unsure{\begin{tikzpicture}[x=.07mm,y=-.07mm,baseline=(g05markbase)]
-\path[use as bounding box] (0,0) rectangle (20,22);
-\coordinate (g05markbase) at (0,22);
-\fill (5,16) circle[radius=1.2];
-\fill (10,6) circle[radius=1.2];
-\end{tikzpicture}}};
-\end{tikzpicture}
-``\unsure{composant|composante}'' de cette classe \deleted{est} est l'\unsure{élêment|élément} du $\pi_0$ qui ne contient pas $E_i$; il est donc contenu dans l'un des
-% G06: whole éléments / (soit Sigma_i^-) / de group, origin (251,2160).
-\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g06base)]
-\path[use as bounding box] (0,0) rectangle (470,126);
-\coordinate (g06base) at (0,95);
-\begin{scope}[shift={(-251,-2160)}]
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (265,2255) {éléments};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (399,2201) {\inserted{(soit $\Sigma_i^-$)}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (595,2248) {de};
-\draw[line width=.35pt] (560,2251) .. controls (563,2228) and (599,2215) .. (646,2205) .. controls (655,2202) and (653,2199) .. (647,2197);
 \end{scope}
 \end{tikzpicture}
-$\pi_0(X\setminus\Sigma_i)$, d'après l'étude du cas
-% G07: lower correction, origin (382,2265). Actual cancellation drawn
-% once; the invisible deleted copy supplies annotation/dimensions only.
-\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g07base)]
-\path[use as bounding box] (0,0) rectangle (190,80);
-\coordinate (g07base) at (0,59);
-\begin{scope}[shift={(-382,-2265)}]
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (395,2323) {\rlap{\unsure{deux}}\phantom{\deleted{\unsure{deux}}}};
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (389,2297) {\inserted{$\operatorname{card}I=2$}};
-\draw[line width=.55pt] (395,2325) .. controls (443,2318) and (509,2322) .. (556,2318);
+contient pas $\deleted{\Sigma}\overline{E_i}$ i.e. est $\ne U_{J,i}$, signifie que il existe un $j\in J$ tel que le $\Sigma_j^+\in\pi_0(X\setminus\deleted{\Sigma}E_j)$
+% G05: cancelled word and two detached endpoint points, origin (1400,1715), fixed 200 by 90.
+\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g05base)]
+\path[use as bounding box] (0,0) rectangle (200,90);
+\coordinate (g05base) at (0,49);
+\begin{scope}[shift={(-1400,-1715)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1410,1764) {\rlap{\unsure{choisi|choisie}}\phantom{\deleted{\unsure{choisi|choisie}}}};
+% G05a: single cancellation stroke.
+\draw[line width=.6pt] (1410,1757) .. controls (1468,1756) and (1524,1757) .. (1566,1758);
+% G05b/c: both extra endpoint points occur once; the two i dots stay within the word.
+% Nested origin (1567,1745), baseline (0,0), base-west anchor and zero separation.
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1567,1745) {\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g05pointsbase)]
+\path[use as bounding box] (0,0) rectangle (12,12);
+\coordinate (g05pointsbase) at (0,0);
+\fill (2,8) circle[radius=1.1];
+\fill (9,2) circle[radius=1.0];
+\end{tikzpicture}}};
 \end{scope}
-\end{tikzpicture},
-\deleted{\unsure{OK|cela|et}} \unsure{â|à} fortiori $U_\alpha\subset\Sigma_i^-$,
-% G08: final OK and its rising transverse stroke, origin (1450,2255).
-% Whole-state candidates: live OK; deleted OK. The local unsure retains
-% this unresolved state; no extra generic cancellation line is drawn.
-\unsure{\begin{tikzpicture}[x=.08mm,y=-.08mm,baseline=(g08base)]
-\path[use as bounding box] (0,0) rectangle (95,85);
-\coordinate (g08base) at (0,70);
-\begin{scope}[shift={(-1450,-2255)}]
-\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1455,2323) {\rlap{OK}\phantom{\deleted{OK}}};
-\draw[line width=.3pt] (1452,2293) .. controls (1470,2287) and (1497,2279) .. (1534,2264);
+\end{tikzpicture}
+``composant'' de cette classe \deleted{est} est l'\unsure{é|e}l\unsure{é|ê}ment du $\pi_0$ qui ne contient pas $E_i$; il est donc contenu dans l'un des
+% G06: whole éléments / (soit Sigma) / de / pi_0 group, origin (245,2135), fixed 795 by 155.
+\begin{tikzpicture}[x=.010cm,y=-.010cm,baseline=(g06base)]
+\path[use as bounding box] (0,0) rectangle (795,155);
+\coordinate (g06base) at (0,125);
+\begin{scope}[shift={(-245,-2135)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (270,2260) {\unsure{é|e}léments};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (396,2213) {\inserted{(soit $\Sigma_i^-$)}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (595,2245) {de};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (719,2244) {$\pi_0(X\setminus\Sigma_i)$};
+% G06a: guide crossing the ascender of de, with its full right hook.
+\draw[line width=.4pt] (558,2247) .. controls (562,2228) and (580,2225) .. (612,2221) .. controls (632,2218) and (646,2213) .. (650,2208) .. controls (647,2204) and (645,2202) .. (642,2204);
 \end{scope}
-\end{tikzpicture}}.
+\end{tikzpicture}, d'après l'étude du
+% G07: cas / cancelled deux / raised card I=2, origin (245,2240), fixed 370 by 123.
+\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g07base)]
+\path[use as bounding box] (0,0) rectangle (370,123);
+\coordinate (g07base) at (0,85);
+\begin{scope}[shift={(-245,-2240)}]
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (275,2325) {cas};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (400,2321) {\rlap{\unsure{deux}}\phantom{\deleted{\unsure{deux}}}};
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (386,2302) {\inserted{$\operatorname{card}I=2$}};
+% G07a: complete long cancellation rule, kept once.
+\draw[line width=.65pt] (399,2320) .. controls (438,2313) and (483,2317) .. (515,2314) .. controls (531,2312) and (546,2311) .. (555,2312);
+% G07b: supported lower hook below the I/= region; its guide/letter role remains unsettled.
+% Nested origin (510,2290), baseline (0,0), base-west placement and zero separation.
+\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (510,2290) {\unsure{\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=(g07hookbase)]
+\path[use as bounding box] (0,0) rectangle (12,27);
+\coordinate (g07hookbase) at (0,0);
+\draw[line width=.5pt] (4,4) .. controls (10,10) and (8,18) .. (1,24);
+\end{tikzpicture}}};
+\end{scope}
+\end{tikzpicture}, \deleted{\unsure{OK|cela}} \unsure{â|à} fortiori $U_\alpha\subset\Sigma_i^-$, OK.
 % archive sheet number: 17
