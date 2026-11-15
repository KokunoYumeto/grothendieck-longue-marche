from save_page import save
text=r'''\scanpage{108}
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=1.7pt] (241,345)--(760,324);
\draw[black!60,line width=.5pt] (244,320)--(737,310);
\draw[black!60,line width=.5pt,dashed] (244,368)--(746,359);
\draw[orange!80!brown,line width=1.4pt] (295,127)--(389,457) (361,119)--(279,449) (569,159)..controls(619,283)and(646,366)..(662,451) (603,168)--(548,448) (445,285)--(443,439) (488,286)--(490,440);
\draw[black,line width=2pt] (308,334)--(351,335) (297,367)--(365,369);
\fill[black] (351,163) circle (3);\fill[black] (342,194) circle (3);
\draw[black,->,line width=.6pt] (373,416)--(389,460) (443,414)--(443,444) (488,414)--(490,445) (545,431)--(548,451);
\node at (285,386) {$x_0$};\node at (386,385) {$x_1$};\node at (400,476) {$\lambda$};\node at (446,468) {$\alpha$};\node at (490,473) {$\beta$};\node at (546,478) {$\mu$};
\draw[gray,line width=.4pt] (239,318)--(325,204) (253,320)--(375,151) (266,314)--(407,163) (281,308)--(408,193) (313,304)--(425,199) (349,306)--(447,212) (377,306)--(493,220) (414,308)--(534,220) (461,309)--(576,214) (501,308)--(610,202) (545,306)--(646,192) (604,305)--(708,226);
\draw[yellow!70!olive,line width=1.7pt] (884,330)--(941,332)..controls(977,330)and(942,264)..(1003,233)..controls(1091,181)and(1110,273)..(1128,320)--(1465,325);
\draw[orange!80!brown,line width=1.4pt] (1027,162)--(1133,512) (1076,142)--(942,491) (1304,161)--(1404,481) (1357,172)--(1264,487) (1191,265)--(1191,471) (1233,265)--(1230,478);
\draw[black!65,dashed,line width=.5pt] (876,361)--(1453,369);
\draw[black,line width=2pt] (978,361)--(1099,366) (1040,198)--(1052,198);
\draw[black!65,line width=.5pt] (1034,254)--(1057,254);
\node at (960,367) {$x_0$};\node at (1123,374) {$x_1$};
\draw[gray,line width=.4pt] (833,499)--(903,364) (876,507)--(945,372) (897,514)--(974,374) (939,513)--(1013,376) (959,518)--(1047,379) (1006,528)--(1081,382) (1065,537)--(1137,390) (1154,529)--(1224,393) (1240,517)--(1318,396) (1279,521)--(1376,399) (1338,516)--(1438,391) (1420,484)--(1475,404);
\end{tikzpicture}}
\mspage{107}
'''
save({'scan':108,'text':text,'elements':[('drawing','upper left','two orange crossings; two vertical orange arrows; two black intervals; x0 x1 lambda alpha beta mu'),('drawing','upper middle','yellow raised arc; two orange crossings; two vertical orange lines; black intervals; x0 x1; pencil hatching'),('margin note','bottom left','107')]})
