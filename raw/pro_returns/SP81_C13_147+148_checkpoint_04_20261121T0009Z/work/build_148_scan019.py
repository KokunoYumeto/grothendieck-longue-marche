from pathlib import Path
import json
import re

ROOT = Path('/workspace/scratch/15c7af26487b/edition')
PAGE = '148_scan019'
packet = (ROOT / 'packets' / f'{PAGE}.md').read_text()
c = re.search(r'## Witness C\s+```tex\n(.*?)\n```', packet, re.S).group(1).strip()
h = re.search(r'## Witness H\s+```tex\n(.*?)\n```', packet, re.S).group(1).strip()
cfigs = re.findall(r'\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}', c, re.S)
hfigs = re.findall(r'\\drawing\{[^{}]*\}', h, re.S)

coords = {
    'upper_sphere': [735,166,1169,655],
    'upper_caption': [1202,143,1461,338],
    'passage_words': [1185,406,1503,520],
    'deleted_qualifier': [1113,554,1512,681],
    'special_cases': [177,697,822,824],
    'contained_quotes': [152,866,1007,998],
    'listing': [1254,1008,1517,1114],
    'middle_tetrahedron': [254,1008,718,1412],
    'lower_insertion': [738,1111,1476,1248],
    'lower_cases': [737,1231,1488,1368],
    'lower_sphere': [350,1467,822,2081],
    'lower_numeral': [97,2112,179,2195],
    'upper_isolated_mark': [489,126,544,183],
    'upper_edge_marks': [1246,37,1476,82],
    'lower_edge_marks': [1251,2149,1482,2192],
}

# Coordinates in each graphic follow the source crop, with y increasing downwards.
# Names assigned to coordinates are internal drawing aids; no labels are added.
upper = r'''\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round,line join=round]
\draw[gray!55,line width=.35pt] (245,19)..controls(118,7)and(16,128)..(5,247)..controls(1,364)and(75,468)..(211,475);
\draw[gray!55,line width=.35pt] (245,19)..controls(353,27)and(424,130)..(425,246)..controls(427,368)and(348,460)..(211,475);
\draw[gray!35,line width=.25pt] (240,21)..controls(143,30)and(63,180)..(69,299)..controls(74,384)and(145,476)..(213,474);
\draw[gray!35,line width=.25pt] (244,20)..controls(286,111)and(287,315)..(269,399)..controls(252,467)and(236,476)..(211,475);
\draw[gray!40,line width=.25pt] (246,19)..controls(178,15)and(142,134)..(145,207)..controls(139,351)and(153,447)..(211,475);
\draw[gray!40,line width=.25pt] (246,19)..controls(357,45)and(367,158)..(363,210)..controls(361,351)and(340,444)..(211,475);
\draw[red!28!black,line width=1pt] (245,19)..controls(142,3)and(72,165)..(75,295);
\draw[red!28!black,line width=.9pt,dash pattern=on 2.1pt off 3.7pt] (246,19)..controls(334,26)and(361,120)..(363,210);
\draw[red!28!black,line width=1pt] (147,207)..controls(142,224)and(143,271)..(143,301);
\draw[red!28!black,line width=.9pt,dash pattern=on 2.8pt off 4.8pt] (145,320)..controls(144,390)and(160,461)..(211,475);
\draw[red!28!black,line width=1.05pt] (275,304)..controls(268,349)and(262,426)..(247,455)..controls(236,473)and(222,475)..(211,475);
\draw[green!32!black,line width=1.75pt] (245,19)..controls(283,1)and(285,84)..(285,145)..controls(284,197)and(280,263)..(275,304);
\draw[green!32!black,line width=1.6pt,dash pattern=on 2.2pt off 7.3pt] (244,19)..controls(185,18)and(145,104)..(147,207);
\draw[green!32!black,line width=1.7pt] (75,295)..controls(67,360)and(122,456)..(181,472)..controls(194,477)and(204,476)..(211,475);
\draw[green!32!black,line width=1.65pt,dash pattern=on 2.3pt off 7.1pt] (363,210)..controls(361,320)and(340,433)..(285,464)..controls(256,479)and(235,477)..(211,475);
% The eight colored heads are traced as exposed strokes, without ideal arrow tips.
\draw[red!28!black,line width=1.25pt] (65,252)..controls(70,247)and(71,241)..(74,234)..controls(76,238)and(77,243)..(79,245);
\fill[red!28!black] (74,235) ellipse[x radius=.052cm,y radius=.06cm];
\draw[red!28!black,line width=1.1pt] (350,181)..controls(353,175)and(357,171)..(359,169)..controls(362,172)and(365,173)..(367,170);
\fill[red!28!black] (357,160) ellipse[x radius=.048cm,y radius=.06cm];
\node[anchor=west,inner sep=0pt] at (371,171) {\unsure{}};
\draw[red!28!black,line width=1.2pt] (132,241)..controls(137,249)and(140,251)..(142,256)..controls(147,248)and(151,247)..(155,246);
\fill[red!28!black] (141,264) ellipse[x radius=.05cm,y radius=.057cm];
\draw[red!28!black,line width=1.1pt] (251,348)..controls(256,352)and(259,356)..(261,360)..controls(266,352)and(272,350)..(276,349);
\fill[red!28!black] (261,367) ellipse[x radius=.048cm,y radius=.055cm];
\fill[green!32!black] (156,145)..controls(151,148)and(149,154)..(145,161)..controls(151,161)and(153,159)..(156,156)..controls(160,161)and(164,162)..(168,161)..controls(164,155)and(161,147)..(156,145)--cycle;
\draw[green!32!black,line width=1.65pt] (273,253)..controls(278,246)and(282,239)..(283,231)..controls(285,240)and(289,245)..(292,249);
\draw[green!32!black,line width=1.75pt] (73,351)..controls(77,359)and(80,364)..(85,367)..controls(88,360)and(92,354)..(96,350);
\draw[green!32!black,line width=1.8pt] (344,251)..controls(346,263)and(350,269)..(356,273)..controls(362,266)and(368,258)..(376,254);
\draw[black,line width=.9pt,dash pattern=on 1.8pt off 4.5pt] (20,253)..controls(52,215)and(109,206)..(147,207)..controls(222,205)and(305,193)..(363,210)..controls(398,220)and(419,234)..(422,248);
\draw[black,line width=1.25pt] (20,253)..controls(5,285)and(58,303)..(142,307)..controls(242,318)and(366,303)..(406,280)..controls(420,272)and(426,256)..(422,248);
\fill[black] (75,295) ellipse[x radius=.072cm,y radius=.077cm];
\fill[black] (275,304) ellipse[x radius=.073cm,y radius=.076cm];
\fill[black] (147,207) ellipse[x radius=.068cm,y radius=.076cm];
\fill[black] (363,210) ellipse[x radius=.074cm,y radius=.08cm];
\end{tikzpicture}}'''

middle = r'''\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round,line join=round]
\coordinate (A) at (22,383); \coordinate (B) at (175,19);
\coordinate (C) at (340,351); \coordinate (D) at (441,159);
\coordinate (O) at (190,235); \coordinate (Q) at (259,178);
\coordinate (P) at (338,167); \coordinate (J) at (338,108);
\draw[red!28!black,line width=.65pt] (A)--(104,183)--(B)--(Q)--(C)--(D)--(J)--(B);
\draw[red!28!black,line width=.65pt] (A)..controls(107,378)and(249,360)..(C);
\draw[red!28!black,line width=.7pt,dash pattern=on 3pt off 10pt] (A)--(D);
\draw[red!28!black,line width=.75pt] (18,369)..controls(25,357)and(34,343)..(43,331);
\draw[green!32!black,line width=1.55pt] (B)..controls(184,70)and(188,170)..(O)--(190,370);
\draw[green!32!black,line width=1.65pt] (A)..controls(77,340)and(147,281)..(O)--(Q);
\draw[green!32!black,line width=1.5pt] (104,183)--(O)..controls(236,271)and(293,319)..(C);
\draw[green!32!black,line width=1.6pt] (B)--(P)--(397,228);
\draw[green!32!black,line width=1.55pt] (Q)..controls(299,174)and(382,173)..(D);
\draw[green!32!black,line width=1.45pt] (J)--(P)..controls(338,228)and(338,297)..(C);
\draw[black!90,line width=2pt] (338,108)..controls(334,117)and(337,124)..(334,131)..controls(339,139)and(335,153)..(338,167);
\draw[black!80,line width=.65pt] (23,379)..controls(67,342)and(138,285)..(188,237);
\draw[black!85,line width=.65pt] (191,237)..controls(201,248)and(222,262)..(238,272);
% Red dots and broken strokes retain the unevenly drawn route.
\foreach \p in {(123,182),(132,184),(147,185),(160,185),(170,184),(198,184)} {\fill[red!70!black] \p circle[radius=.015cm];}
\draw[red!60!black,line width=.8pt,dash pattern=on 2.1pt off 3.6pt] (105,188)--(180,224)--(259,178)--(338,167)--(397,228);
\foreach \p in {(221,190),(231,221),(233,230),(239,239),(242,247),(249,256),(256,271),(265,275),(275,276),(302,292),(312,270),(325,267),(339,258),(353,253),(369,247),(380,243),(389,241)} {\fill[red!70!black] \p circle[radius=.016cm];}
\fill[red!70!black] (104,183) ellipse[x radius=.043cm,y radius=.047cm];
\fill[red!70!black] (216,180) ellipse[x radius=.065cm,y radius=.07cm];
\fill[red!70!black] (185,218) ellipse[x radius=.071cm,y radius=.065cm];
\fill[red!70!black] (259,178) ellipse[x radius=.04cm,y radius=.044cm];
\fill[red!50!black] (338,167) ellipse[x radius=.069cm,y radius=.063cm];
\fill[red!65!black] (397,228) ellipse[x radius=.042cm,y radius=.044cm];
\fill[red!70!black] (291,278) ellipse[x radius=.066cm,y radius=.072cm];
\draw[red!35!black,line width=.75pt] (269,258)..controls(263,262)and(254,263)..(247,266);
\fill[red!65!black] (246,255)--(250,260)--(254,268)--(245,269)--(246,255);
\foreach \p in {A,B,C,D} {\fill[black] (\p) ellipse[x radius=.076cm,y radius=.085cm];}
\end{tikzpicture}}'''

lower = r'''\figure{\begin{tikzpicture}[x=.0115cm,y=-.0115cm,line cap=round,line join=round]
% Pencil contours are traced separately, including their gaps and repeated passes.
\draw[gray!70,line width=.45pt] (87,198)..controls(132,153)and(191,129)..(235,120)..controls(311,112)and(386,167)..(421,213);
\draw[gray!45,line width=.3pt] (59,236)..controls(104,159)and(175,110)..(245,112)..controls(322,108)and(402,161)..(427,222);
\draw[gray!55,line width=.35pt] (64,228)..controls(119,184)and(175,145)..(231,128)..controls(297,123)and(372,169)..(416,211);
\draw[gray!70,line width=.45pt] (87,198)..controls(34,234)and(9,309)..(17,386)..controls(18,467)and(51,526)..(110,558)..controls(142,577)and(183,589)..(213,590);
\draw[gray!50,line width=.35pt] (62,236)..controls(38,271)and(14,343)..(20,412)..controls(23,489)and(71,544)..(110,558)..controls(148,578)and(191,586)..(215,589);
\draw[gray!70,line width=.5pt] (421,213)..controls(442,248)and(445,300)..(442,345)..controls(449,414)and(430,487)..(385,520)..controls(329,565)and(269,591)..(213,590);
\draw[gray!50,line width=.35pt] (430,238)..controls(444,292)and(446,368)..(439,419)..controls(431,466)and(414,493)..(406,511);
\draw[gray!65,line width=.45pt] (385,520)..controls(344,561)and(277,588)..(218,591)..controls(168,591)and(119,572)..(77,550);
\draw[gray!45,line width=.35pt] (61,516)..controls(126,563)and(238,589)..(314,568);
\draw[gray!65,line width=.45pt] (17,350)..controls(80,299)and(249,299)..(440,336)..controls(450,343)and(448,356)..(442,367)..controls(330,416)and(117,422)..(20,374)..controls(15,367)and(16,356)..(17,350);
\draw[gray!50,line width=.35pt] (22,341)..controls(119,298)and(309,306)..(439,327);
\draw[gray!55,line width=.4pt] (17,354)..controls(94,398)and(243,414)..(423,387);
\draw[gray!55,line width=.4pt] (17,366)..controls(66,389)and(131,400)..(187,401)..controls(274,405)and(353,389)..(438,369);
\draw[gray!45,line width=.35pt] (20,357)..controls(101,395)and(226,412)..(338,366);
\draw[gray!75,line width=.5pt] (235,120)..controls(216,130)and(200,220)..(195,289)..controls(191,331)and(193,366)..(196,400);
\draw[gray!45,line width=.35pt] (196,400)..controls(188,469)and(193,547)..(200,581);
\draw[gray!50,line width=.35pt] (234,125)..controls(224,203)and(211,286)..(207,351)..controls(203,388)and(207,411)..(215,423);
\draw[gray!40,line width=.3pt] (208,429)..controls(202,489)and(201,555)..(213,590);
\draw[gray!65,line width=.4pt] (235,120)..controls(270,141)and(260,211)..(260,309);
\draw[gray!40,line width=.3pt] (260,310)..controls(260,365)and(257,438)..(254,466);
\draw[gray!45,line width=.35pt] (253,483)..controls(251,543)and(239,576)..(213,590);
\draw[gray!70,line width=.45pt] (109,558)..controls(170,568)and(242,573)..(311,555);
% Four peripheral rings retain their uneven dark interiors.
\draw[black!90,line width=1.15pt] (79,197)..controls(78,186)and(93,183)..(97,194)..controls(101,204)and(84,212)..(80,202)--cycle;
\draw[gray!80,line width=.5pt] (83,192)--(92,203) (89,189)--(84,204);
\draw[black!90,line width=1.1pt] (413,212)..controls(412,203)and(424,199)..(430,208)..controls(431,215)and(417,226)..(414,218)--cycle;
\draw[black!90,line width=1.1pt] (103,557)..controls(101,548)and(116,548)..(117,557)..controls(116,563)and(117,570)..(107,565)--cycle;
\draw[gray!85,line width=.6pt] (108,550)--(110,564);
\draw[black!90,line width=1.15pt] (377,519)..controls(374,509)and(390,507)..(394,515)..controls(396,524)and(381,534)..(378,525)--cycle;
% Short exposed interior strokes are retained without added labels.
\draw[black!85,line width=1.2pt] (189,382)..controls(190,386)and(189,391)..(187,394);
\draw[black!75,line width=.8pt] (309,404)..controls(312,410)and(315,408)..(316,405);
\draw[gray!85,line width=.7pt] (322,400)--(323,405);
\draw[red!15!black,line width=.65pt] (279,339)..controls(280,334)and(284,334)..(284,338);
\draw[gray!70,line width=.4pt] (210,139)..controls(207,137)and(208,134)..(212,132);
\draw[gray!65,line width=.45pt] (422,241)..controls(427,241)and(430,240)..(432,238);
% This extended broken trace has uncertain material status; no role is assigned.
\draw[gray!45,line width=.75pt,dash pattern=on 2pt off 2.4pt] (196,8)..controls(155,29)and(145,78)..(153,113)..controls(164,168)and(194,241)..(211,299)..controls(217,322)and(222,338)..(226,349);
\draw[red!18!black,line width=.7pt] (154,79)..controls(151,83)and(151,91)..(152,98);
\draw[gray!80,line width=.65pt] (151,109)--(159,105) (157,130)--(159,139) (165,156)--(166,161);
\draw[red!18!black,line width=.7pt] (211,299)..controls(215,314)and(218,327)..(222,334);
\fill[red!12!black] (222,334)..controls(231,336)and(233,346)..(226,352)..controls(221,349)and(220,340)..(222,334)--cycle;
\node[anchor=east,inner sep=0pt] at (147,49) {\unsure{}};
\end{tikzpicture}}'''

edge_top = r'''\begin{tikzpicture}[x=.45cm,y=.45cm]
\foreach \x in {0,1,2,3} {\fill (\x,0) circle[radius=.013cm];\fill (\x+.13,0) circle[radius=.013cm];\fill (\x+.065,-.12) circle[radius=.014cm];}
\end{tikzpicture}'''
edge_bottom = r'''\begin{tikzpicture}[x=.45cm,y=.45cm]
\foreach \x in {0,1,2,3} {\fill (\x,0) circle[radius=.014cm];\fill (\x+.13,0) circle[radius=.013cm];\fill (\x+.065,-.12) circle[radius=.014cm];}
\end{tikzpicture}'''
caption = r'''passage\\
du carré\\
aux deux\\
tétraèdres'''
cancelled = r'la \deleted{\unsure{double}}\unsure{sub}division'
insertion_word = r'\inserted{\unsure{nouveau|commune}}'
interline = r'''\begin{tikzpicture}[baseline=(tetra.base),line cap=round,line join=round]
\node[anchor=base west,inner sep=0pt] at (0,.72) {cette carte (subdivision bar. du};
\node[anchor=base west,inner sep=0pt] (tetra) at (0,0) {tétraèdre};
\node[anchor=base west,inner sep=0pt] at ([xshift=.27cm]tetra.base east) {contient également les};
\node[anchor=base west,inner sep=0pt,font=\scriptsize] at ([xshift=.42cm,yshift=.34cm]tetra.base west) {\inserted{\unsure{nouveau|commune}}};
\draw[line width=.4pt] ([xshift=.06cm,yshift=.52cm]tetra.base east)..controls([xshift=.28cm,yshift=.29cm]tetra.base east)and([xshift=.24cm,yshift=.05cm]tetra.base east)..([xshift=.08cm,yshift=-.08cm]tetra.base east);
\draw[line width=.4pt] ([xshift=.62cm,yshift=.27cm]tetra.base west)..controls([xshift=.94cm,yshift=.15cm]tetra.base west)and([xshift=.06cm,yshift=.26cm]tetra.base east)..([xshift=.22cm,yshift=.32cm]tetra.base east);
\end{tikzpicture}'''
listing = r'''\begin{tikzpicture}
\node[rotate=180,inner sep=0pt] {\shortstack[l]{\texttt{NS 001 072}\\\texttt{L ===> PAGE}\\\texttt{************}}};
\end{tikzpicture}'''
noun = r'\unsure{coins|cas|cartes}'
ending = r'\unsure{associés|associées}'
upper_prose = 'Pour avoir\\\\\nle passage aux\\\\\naux structures\\\\\npantaloniques,\\\\\nil faut introduire\\\\\n' + cancelled + '\\\\\nbarycentrique complète\\\\\nde la carte carrée.'
left_prose = r'''dans les deux cas \inserted{``spéciaux''} non digons\\
(carré, tétraèdre) les positions\\
adjacentes sont toutes ``contenues\\
dans la subdivision barycentrique'''
lower_rest = 'subdivisions barycentriques\\\\\ndes trois ' + noun + " ``carrés'' " + ending + ',\\\\\n(dont l\'une est marquée en\\\\\npointillés rouges)'

tex = '\\cotefile{148}\n\\scanpage{19}\n\n'
tex += '\\begin{flushright}\n' + edge_top + '\n\\end{flushright}\n\n'
tex += '\\noindent\\hfill\\begin{minipage}[t]{.50\\textwidth}\\vspace{0pt}\n' + upper + '\n\\end{minipage}\\hfill\n'
tex += '\\begin{minipage}[t]{.34\\textwidth}\\vspace{0pt}\n' + caption + '\n\\par\\medskip\n' + upper_prose + '\n\\end{minipage}\n\n'
tex += '\\par\\medskip\\noindent\n' + left_prose + '\n\n'
tex += '\\begin{flushright}\n' + listing + '\n\\end{flushright}\n\n'
tex += '\\noindent\\begin{minipage}[t]{.43\\textwidth}\\vspace{0pt}\n' + middle + '\n\\end{minipage}\\hfill\n'
tex += '\\begin{minipage}[t]{.54\\textwidth}\\vspace{.55cm}\n' + interline + '\n\\par\\noindent\n' + lower_rest + '\n\\end{minipage}\n\n'
tex += lower + '\n\n\\margin{18}\n\n\\begin{flushright}\n' + edge_bottom + '\n\\end{flushright}\n'

changes = []
def change(place, C, H, final, evidence, crop, confidence, kind, error_kind, dc, dh, marked=False, consequential=False):
    ident = f'{PAGE}-{len(changes)+1:02d}'
    changes.append({'id':ident,'place':place,'C':C,'H':H,'final':final,
      'evidence':f'{evidence} Crop {PAGE}_{crop}.png, original box {coords[crop]}.',
      'crop':f'{PAGE}_{crop}.png','box':coords[crop],'confidence':confidence,
      'kind':kind,'error_sheet_kind':error_kind,'differs_C':dc,'differs_H':dh,
      'marked_in_H':marked,'consequential':consequential})
    return ident

ch_top = change('upper right paper edge', '[omitted]', '[omitted]', edge_top,
    'Four evenly spaced groups are visible, each with two upper black dots and one lower dot. The direct graphic preserves their keyed appearance without assigning a character or mathematical meaning.',
    'upper_edge_marks','high','omission','Omissions',True,True)
ch_upper = change('upper colored sphere', cfigs[0], hfigs[0], upper,
    'The crop exposes four large black equatorial points, a solid front and broken rear equatorial line, green solid/broken routes, brown solid/dashed routes, and eight colored head-like marks. C omits the brown mark on the upper left. The upper-right brown mark has a rounded upper part and an oblique lower return; C\'s ideal downward arrow is not securely exposed. All eight heads are traced directly, and the upper-right ambiguity is marked locally. The faint outer and underlying pencil passes are retained. H records the broad objects but gives no exact contours or individual heads.',
    'upper_sphere','medium','drawing or diagram','Drawings and diagrams',True,True,consequential=True)
ch_aux = change('upper paragraph, consecutive second and third baselines',
    r'le passage \unsure{aux|à} \unsure{aux|deux|autres} structures',
    'le passage aux deux structures','le passage aux\naux structures',
    'Each of the two successive short words has a low a/u body and an exposed terminal crossed x. The second lacks the tall looped d visible in deux in this page\'s caption. The repetition aux aux is retained exactly; no grammatical correction is made.',
    'passage_words','high','misread word','Words',False,True,consequential=True)
ch_cancel = change('upper paragraph, cancelled qualifier and merged following prefix',
    r'la \deleted{\unsure{double}}subdivision',r'la \struck{\ill{}} subdivision',cancelled,
    'The cancellation crosses low dou-like loops and taller strokes, leaving double a candidate rather than a secure full reading. The beginning of the following live word is merged with the dark cancelled area: division is exposed, while sub is not separately recoverable. The cancellation is not extended over the exposed division. C\'s candidate is retained, and a separate local uncertainty is added to the live prefix.',
    'deleted_qualifier','low',r'readable ink left as \ill{}','Readable ink left as illegible',False,True,marked=True)
ch_quotes = change('left paragraph, before contenues',r'toutes ``contenues','toutes contenues',r'toutes ``contenues',
    'Two small opening quotation strokes stand between toutes and contenues. No closing partner is exposed before the paragraph ends. H omits these opening marks.',
    'contained_quotes','high','omission','Omissions',False,True)
clisting = re.search(r'\\begin\{flushright\}.*?\\end\{flushright\}', c, re.S).group(0)
ch_print = change('middle right surviving printed listing',clisting,'[omitted]',listing,
    'After the prescribed crop rotation, the three printed rows read NS 001 072, L ===> PAGE, and twelve asterisks. There are three equals signs before the greater-than sign. In the original page all three rows are upside-down relative to the manuscript, so the block is rotated as a whole. C gives the characters upright; H mentions a listing in an editorial note but omits this surviving text.',
    'listing','high','other','Other',True,True)
ch_middle = change('middle colored tetrahedral drawing',cfigs[1],hfigs[1],middle,
    'Four black vertices, six green median strokes across the two drawn faces, seven red points, the uneven red broken/dotted route, the brown broken diagonal, and a thick dark segment from the upper edge to the right interior junction are visible. The dark upper segment and the green median that continues through it are absent from C\'s schematic. The red triangular/curved marker is reproduced from its actual strokes. Small dashes crossing green lines remain part of the visible brown broken diagonal. H notes a dark path and red points without their complete arrangement.',
    'middle_tetrahedron','medium','drawing or diagram','Drawings and diagrams',True,True,consequential=True)
ch_interline = change('lower paragraph, interlinear word and crossing curved attachment',
    r'cette carte \inserted{\unsure{commune|nouveau}} (subdivision bar. du tétraèdre) contient également les',
    r'cette carte (subdivision bar.\ du \add{\uncertain{nouveau}}\note{en interligne, au-dessus de « tétraèdre »} tétraèdre) contient également les',
    interline,
    'The compressed raised word lies above the latter part of tétraèdre and below the preceding carte line. Its initial down-up movement and detached shallow final strokes slightly favor nouveau, but commune remains open. A curved stroke beneath it merges with the tall closing parenthesis; the exact semantic attachment is not securely exposed. The two baselines, word, parenthesis and curve are placed directly, without assigning the insertion a prose position after carte or before tétraèdre.',
    'lower_insertion','low','insertion or placement','Insertions put in the wrong place',True,True,marked=True,consequential=True)
ch_noun = change('lower paragraph, noun after des trois',r'\unsure{cas|cartes|coins}','cartes',noun,
    'A clear co opening is followed by compact low strokes, including a compressed partly stained i/n region. No independent tall t is exposed as in cartes. Coins is favored, with cas and cartes retained locally because the small medial strokes remain compressed.',
    'lower_cases','medium','misread word','Words',True,True,consequential=True)
ch_ending = change('lower paragraph, ending after the quoted adjective','associés','associées',ending,
    'The ending has a compressed accented region and final hook. The exposed run favors associés; a separate second e before the hook is not securely present. Both endings remain in a local uncertainty rather than being decided from agreement.',
    'lower_cases','medium','misread word','Words',False,True)
ch_lower = change('lower pencil sphere and extended trace',cfigs[2],hfigs[2],lower,
    'The pencil figure has repeated, uneven and partly open outer/equatorial contours, uneven meridian passes, four dark peripheral rings with different interiors, and short interior dark strokes. These are retained separately instead of filling gaps with a regular ellipse. The broken gray/brown trace starts far above the sphere and crosses its pencil lines; its material origin and role are unsettled, so it is reproduced separately with a local question marker and no assigned drawing function. C gives one short regular oblique stroke within the sphere; H supplies only a broad description.',
    'lower_sphere','medium','drawing or diagram','Drawings and diagrams',True,True)
ch_num = change('lower left margin',r'\margin{18}','[omitted]',r'\margin{18}',
    'The lighter numeral has a long first downstroke and the two loops of the following 8. It reads 18. H does not transcribe it.',
    'lower_numeral','high','omission','Omissions',False,True)
ch_bottom = change('lower right paper edge','[omitted]','[omitted]',edge_bottom,
    'Four repeated groups are visible, each containing two upper black dots and one lower black dot, matching the keyed form at the top edge. They are reproduced graphically without assigning an alphabetic or mathematical value.',
    'lower_edge_marks','high','omission','Omissions',True,True)

def evidence_crop(name):
    return f'{PAGE}_{name}.png {coords[name]}'

decisions = [
 {'id':'M0134','decision':'first','reading':'aux','evidence':'The first short word after passage has a low a/u body and a separate terminal crossed x. The full word is exposed.','crop':evidence_crop('passage_words'),'confidence':'high'},
 {'id':'M0135','decision':'first','reading':'aux','evidence':'The next baseline begins with a low closed a, shallow u, and terminal crossed x. No tall d like the one in this page\'s caption deux is present. The repeated aux aux is source wording.','crop':evidence_crop('passage_words'),'confidence':'high'},
 {'id':'M0136','decision':'first','reading':'digons','evidence':'The tall opening d, dotted i, descending g, and connected low ons can be followed. No alternate letter reading is required by this crop.','crop':evidence_crop('special_cases'),'confidence':'high'},
 {'id':'M0137','decision':'undecided','reading':insertion_word,'evidence':'The raised initial down-up and detached shallow final strokes slightly favor nouveau, but the compressed central strokes keep commune open. The word is placed above tétraèdre. Its curved lower stroke merges with the closing parenthesis, leaving semantic attachment unresolved.','crop':evidence_crop('lower_insertion'),'confidence':'low'},
 {'id':'M0138','decision':'undecided','reading':noun,'evidence':'The co beginning and low terminal strokes favor coins; the medial i/n region is compressed and stained. No tall t is separately exposed. The alternatives are retained.','crop':evidence_crop('lower_cases'),'confidence':'medium'},
]

unnumbered = [{'place':'cancelled qualifier before subdivision','decision':'undecided',
 'reading':r'\deleted{\unsure{double}}','evidence':'Low dou-like loops and tall strokes survive the cancellation, but not every letter is independently exposed. The original C unnumbered doubt remains.',
 'crop':evidence_crop('deleted_qualifier'),'confidence':'low'}]

inventory = []
def element(kind, position, first, hand='his hand', sheet='text'):
    inventory.append({'sheet_kind':sheet,'hand':hand,'element':f'E{len(inventory)+1:02d}',
      'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
element('drawing','upper right paper edge','four groups of three black dots','machine printing','printed marks')
element('drawing','upper centre-right','colored sphere with four black equatorial points and eight head-like marks')
element('margin note','right of upper sphere, four baselines','passage / du carré / aux deux / tétraèdres')
element('text','upper right below caption, eight principal baselines','Pour avoir le passage aux aux structures pantaloniques')
element('deletion','upper paragraph, sixth baseline','cancelled double candidate, merging with live doubtful sub')
element('text','left below upper figure, four principal baselines','dans les deux cas … non digons')
element('insertion','above first baseline of left paragraph','quoted spéciaux; curved leader reaches gap after cas')
element('text','middle right, upside-down to handwriting','NS 001 072 / L ===> PAGE / twelve asterisks','machine printing','printed listing')
element('drawing','middle left','four black vertices, green subdivisions, seven red points, broken red route, dark upper segment')
element('text','middle right below printing, six principal baselines','cette carte (subdivision bar. du tétraèdre) contient également les')
element('insertion','between the first two baselines of lower paragraph','nouveau|commune with crossing curved stroke and parenthesis')
element('drawing','lower left-centre','pencil sphere with repeated contours and four peripheral rings')
element('drawing','extended above and into lower graphic area','broken gray/brown trace; material status and role unresolved','undetermined; possible transfer','material trace')
element('margin note','lower left margin','18','lighter marginal hand')
element('drawing','lower right paper edge','four groups of three black dots','machine printing','printed marks')

doubts = [
 {'place':'cancelled qualifier','reading':r'\deleted{\unsure{double}}','alternatives':'double; exact full cancelled word unresolved','confidence':'low','reason':'The cancellation crosses low dou-like loops and tall strokes; not all letters can be independently exposed. No grammatical restoration is used.'},
 {'place':'live prefix adjoining cancellation','reading':r'\unsure{sub}division','alternatives':'sub is the witness reading, but its separate live strokes remain obscured','confidence':'low','reason':'Only division to the right is fully exposed. The preceding dark strokes merge with the cancelled word, so the prefix retains its own local doubt.'},
 {'place':'lower interlinear word and attachment','reading':interline,'alternatives':'nouveau favored slightly; commune open; attachment to the surrounding prose remains uncertain','confidence':'low','reason':'The short word lies above tétraèdre. Its lower curved stroke crosses or merges with the tall closing parenthesis. Direct spatial placement preserves the evidence without supplying a semantic insertion point.'},
 {'place':'noun after des trois','reading':noun,'alternatives':'coins favored; cas; cartes','confidence':'medium','reason':'The co opening and low strokes are visible, while the small i/n region is compressed. No independent tall t is exposed.'},
 {'place':'ending after quoted carrés','reading':ending,'alternatives':'associés favored; associées','confidence':'medium','reason':'The final run is compressed and no separate second e is securely exposed; the reading is not settled by agreement.'},
 {'place':'upper sphere, brown upper-right head','reading':upper,'alternatives':'observed rounded upper part and lower oblique returns; ideal arrow orientation unresolved','confidence':'medium','reason':'A rounded upper component and a lower diagonal return are exposed. The graph reproduces those strokes and marks the locus locally rather than imposing C\'s downward arrowhead.'},
 {'place':'lower sphere area, extended broken trace','reading':lower,'alternatives':'possible transfer/material trace; intentional source stroke remains possible; no alphabetic, arrow, or mathematical role is assigned','confidence':'low','reason':'The gray/brown broken streak extends well above the pencil sphere and crosses the pencil work. Its different, diffuse texture leaves material origin unsettled. A direct trace and local question marker retain it without assigning a function.'},
]

boxes = []
def box(kind, name, reading, override=None):
    x0,y0,x1,y1 = override or coords[name]
    boxes.append({'box':f'B{len(boxes)+1:02d}','kind':kind,'x0':x0,'y0':y0,'x1':x1,'y1':y1,'reading':reading})
box('upper edge printed graphic only','upper_edge_marks',edge_top)
box('complete upper colored drawing; adjacent upright handwriting fragments are context only','upper_sphere',upper)
box('complete handwritten caption beside upper drawing','upper_caption',caption)
box('two consecutive full prose baselines; preceding descender is context only','passage_words','le passage aux\naux structures')
box('two full prose baselines and cancellation; preceding descender is context only','deleted_qualifier','il faut introduire\n'+cancelled)
box('full prose baseline and its raised insertion with leader','special_cases',r'dans les deux cas \inserted{``spéciaux\'\'} non digons'.replace("spéciaux\\'\\'", "spéciaux''"))
box('two full prose baselines and punctuation; preceding descenders are context only','contained_quotes',r'adjacentes sont toutes ``contenues'+'\n'+'dans la subdivision barycentrique',[152,866,1007,1014])
box('complete surviving printed block in original orientation','listing',listing)
box('complete middle colored drawing','middle_tetrahedron',middle)
box('first two prose baselines, interlinear insertion and crossing curves only; following baseline fragments are context','lower_insertion',interline)
box('two full central prose baselines only; neighboring descenders and following baseline fragments are context','lower_cases','subdivisions barycentriques\ndes trois '+noun+" ``carrés'' "+ending+',')
box('complete lower graphic area with extended and short isolated traces; surrounding prose fragments are context only','lower_sphere',lower)
box('complete lower marginal numeral','lower_numeral',r'\margin{18}')
box('lower edge printed graphic only','lower_edge_marks',edge_bottom)

diff_coverage = [
 {'row':594,'disposition':f'{ch_upper}; caption words agree, with source spatial placement retained. H\'s verso/cross-page statements are editorial notes, not source ink verified on this page.'},
 {'row':595,'disposition':f'{ch_upper}; long alignment is chiefly C drawing code versus H prose description. Individual visible paths/heads are assessed from the crop.'},
 {'row':596,'disposition':f'{ch_aux}; M0134 and M0135 resolved from the exposed x strokes; the source repeats aux aux.'},
 {'row':597,'disposition':f'{ch_aux}; continuation of M0135 alternatives, resolved aux.'},
 {'row':598,'disposition':f'{ch_cancel}; cancelled double remains a candidate; uncertainty of the merged live prefix is separately retained.'},
 {'row':599,'disposition':'Same source word and insertion in C/H; quoted spéciaux is raised and its curved leader reaches the gap after cas. H\'s interline wording is editorial. M0136 digons is also resolved in this crop.'},
 {'row':600,'disposition':f'{ch_quotes}; source has opening quotes only before contenues.'},
 {'row':601,'disposition':f'{ch_print}; the surviving printed rows are retained in their upside-down orientation. H\'s subsequent figure note is editorial.'},
 {'row':602,'disposition':f'{ch_middle}; source geometry and colors assessed directly, not from the tokenized coordinate alignment.'},
 {'row':603,'disposition':f'{ch_middle}; dark upper segment, red points and broken route included in complete drawing.'},
 {'row':604,'disposition':f'{ch_middle}; remaining drawing code. Lower prose begins in its own source position.'},
 {'row':605,'disposition':f'{ch_interline}; M0137 candidates and exact attachment remain doubtful; direct spatial rendering used.'},
 {'row':606,'disposition':f'{ch_interline}; same physical interlinear locus. H\'s placement note is editorial evidence, not additional manuscript words.'},
 {'row':607,'disposition':f'{ch_noun}; M0138 retains coins first with the other candidates locally.'},
 {'row':608,'disposition':f'{ch_noun}; continuation of noun alternatives. {ch_ending} retains the ending doubt with associés first. Quotation notation otherwise represents the same visible marks.'},
 {'row':609,'disposition':f'{ch_lower}; H\'s location note is editorial; complete lower graphic retained.'},
 {'row':610,'disposition':f'{ch_lower}; repeated contours, four rings, short interior strokes and uncertain extended trace assessed directly.'},
 {'row':611,'disposition':f'{ch_lower}; remainder of lower drawing code. {ch_num} records the lower manuscript numeral omitted by H.'},
]

report = {
 'page':PAGE,'reader':'reader_b','line_count':30,
 'layout':'Upper and lower right paper edges each have a row of four printed dot triplets. The upper colored sphere occupies the upper centre-right, with a four-baseline caption to its right and an eight-baseline paragraph beneath that caption. A four-baseline paragraph begins farther left below the upper figure, with one interlinear insertion. An upside-down three-row printed listing survives at middle right. A colored tetrahedral drawing sits middle left, beside a six-baseline paragraph with a second interlinear insertion. A pencil sphere and a long broken trace occupy the lower left-centre; the lighter numeral 18 is at the lower left. The line count is 22 principal handwritten prose/caption baselines, two raised-word baselines, three listing rows, two edge-mark rows, and one marginal numeral baseline; drawing paths are not counted as text lines.',
 'changes':changes,'decisions':decisions,'unnumbered_decisions':unnumbered,'inventory':inventory,'doubts':doubts,
 'notation':[
   {'form':'green, brown, red and black graphic strokes','meaning':'The page uses these colors to distinguish visible paths and points; the lower paragraph explicitly calls one marking pointillés rouges. No further mathematical interpretation is supplied by this transcription.','evidence':'Upper and middle drawing crops; lower paragraph final two baselines.','scope':'All three drawings on this page checked; no other pages used.'},
   {'form':'four dot triplets at each right edge','meaning':'Repeated keyed graphic form; no alphabetic or mathematical value assigned.','evidence':'Upper and lower edge crops each show four groups with two upper dots and one lower dot.','scope':'The two edge rows on this sheet only.'},
 ],
 'abbreviations':[{'form':'bar.','expansion':'barycentrique (tentative expansion only; the source abbreviation bar. is retained)'}],
 'hand':[
   {'habit':'The low a/u body and crossed x of aux remain distinguishable from the tall looped d of deux.','places':'Upper caption and consecutive second/third baselines of upper paragraph.','scope':'These page-specific occurrences only.','witness_errors':'H reads the second aux as deux; C already offers aux first.'},
   {'habit':'Raised words may have long curved lower strokes that merge with surrounding letter or parenthesis strokes.','places':'spéciaux insertion after cas; lower raised nouveau|commune locus.','scope':'Two interlinear insertions on this page.','witness_errors':'The first attachment is exposed; the second does not support a secure linear prose placement.'},
   {'habit':'Low compressed medial/final letter strokes require local alternatives even where the surrounding phrase is clear.','places':'coins|cas|cartes and associés|associées.','scope':'The lower paragraph only.','witness_errors':'C first offers cas and H cartes; H has associées. The image favors coins and associés while retaining doubts.'},
 ],
 'legibility':'The main ink handwriting is mostly dark and readable, though several compressed words and the cancellation remain locally difficult. The successive aux words expose their terminal x strokes; the page\'s caption supplies a visible same-page deux comparison. The cancelled qualifier is crossed heavily and merges with the following live prefix, so double and sub remain uncertain separately. Both interlinear insertions can be located, but the lower word\'s curved stroke crosses the closing parenthesis and does not securely settle attachment. The lower noun and agreement ending remain compressed. Colors and major paths in the two ink drawings are clear; the upper-right brown head exposes an irregular rounded/oblique form rather than a secure ideal orientation. Pencil in the bottom figure is pale and repeatedly retraced, while its four dark rings and small interior strokes remain visible. The extended gray/brown streak and the diffuse isolated upper patch have unsettled material origin. The printed listing, both edge-dot rows, and marginal 18 are clear.',
 'notes':'Page-specific source account: the upper caption reads passage du carré aux deux tétraèdres. The adjoining paragraph says Pour avoir le passage aux aux structures pantaloniques, il faut introduire la, then has a crossed doubtful double candidate and an obscured sub prefix before division, followed by barycentrique complète de la carte carrée. This is a transcription of the source\'s repeated aux aux, not a corrected statement. The left paragraph refers to deux cas, inserts quoted spéciaux before non digons, and says the adjacent positions are all opening-quoted contenues dans la subdivision barycentrique, without an exposed closing quotation. The lower paragraph begins cette carte (subdivision bar. du tétraèdre), with an interlinear nouveau|commune candidate and uncertain attachment, and states that it also contains subdivisions of three coins|cas|cartes quoted carrés associés|associées, one marked in red dotted strokes. These are the page\'s assertions; no mathematical claim was proved or independently re-proved during this reading. The drawings are recorded as strokes and colored points rather than inferred diagrams. Witness comparison: C is closer on the repeated aux and retains useful local doubts; H\'s deux is contradicted by the exposed terminal x, H drops the opening quotes and the surviving printing/marginal numeral, and H\'s broad drawing descriptions omit exact stroke arrangements. C\'s drawings omit the brown upper-left head and the middle drawing\'s dark upper segment and regularize lower pencil contours. The two witness placements of the lower inserted word are replaced by its physical interlinear position because the crossing attachment is unresolved. H\'s verso and cross-page references are editorial notes and were not independently checked through another page. Material note: the two repeated edge rows are keyed/printed-looking dots; the isolated upper diffuse gray/red patch has no recoverable numeral contour and receives no manuscript page number. The extended lower gray/brown trace may be transferred material, but provenance is unsettled; its actual path is preserved with a local uncertainty and no assigned drawing role. Inspection method: whole scan and both prepared full-resolution halves were viewed once each, followed by all 15 unique saved crops. The listing crop was viewed after its logged 180-degree rotation. The upper-sphere PNG display exceeded the tool output limit and was not counted as inspected at that attempt. Existing upper-sphere, middle-tetrahedron and lower-sphere PNGs were converted to same-dimension RGB JPEG display copies at quality 96 with subsampling 0, without resizing or recropping; each JPEG then actually displayed and was inspected. Original PNGs remain. No OCR, outside research, other page reading, or TeX compilation was performed. Second-reading targets are localized and neutral, with explicit target/context scope and full transcribed target ink; they have not been cropped or read blind.',
 'check_events':[],
 'second_boxes':boxes,'diff_coverage':diff_coverage,
 'deletion_insertion_check':'The single cancellation lies between la and the exposed division. Its double candidate remains under deleted+unsure; the live prefix sub is separately uncertain because cancellation strokes merge with it. The deletion is not extended over the exposed division. The raised quoted spéciaux has a leader to the gap after cas and before non, and that attachment is retained. The lower raised nouveau|commune candidate is placed above tétraèdre between the first two prose baselines; its curved lower stroke and the tall closing parenthesis are reproduced together, leaving semantic attachment open. No other secure cancellation or insertion was found. The long connection in toutes and neighboring descenders are retained as ordinary exposed handwriting, with no invented strike. The lower extended gray/brown trace has uncertain material status and is not interpreted as a textual edit.',
}

(ROOT/'work'/f'{PAGE}.tex').write_text(tex)
(ROOT/'work'/f'{PAGE}_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':PAGE,'changes':len(changes),'decisions':len(decisions),'unnumbered_decisions':len(unnumbered),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(boxes),'diff_rows':len(diff_coverage),'line_count':report['line_count']},ensure_ascii=False))
