from record import save
tex=r'''\scanpage{33}
\mspage{32}
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm]
\draw[dash pattern=on 32pt off 24pt] (310,265) ellipse (310 and 265);
\draw (130,170).. controls (160,215) and (235,265)..(300,295).. controls (385,334) and (440,323)..(530,320);
\draw (373,130)..controls (330,195) and (307,270)..(300,295)..controls (281,365) and (276,408)..(284,454);
\draw (300,295) circle (6);
\node at (270,250) {$P_1$};\node at (245,445) {$\gamma_1$};\node at (520,360) {$\gamma_2$};
\end{tikzpicture}}
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm]
\draw[dash pattern=on 32pt off 24pt] (325,270) ellipse (325 and 270);
\draw (285,70)..controls (255,99) and (208,205)..(200,290)..controls (187,339) and (198,361)..(202,385);
\draw (399,75)..controls (360,170) and (342,280)..(359,369);
\draw (285,70)..controls (314,88) and (365,82)..(399,75);
\draw (202,385)..controls (260,393) and (310,380)..(359,369);
\draw (260,105)..controls (299,130) and (347,132)..(383,118);
\draw (234,161)..controls (275,177) and (325,176)..(370,163);
\draw (208,220)..controls (241,240) and (296,233)..(355,202);
\draw (201,273)..controls (252,296) and (301,280)..(350,261);
\draw (202,344)..controls (247,355) and (302,334)..(350,322);
\draw (160,135)..controls (175,163) and (191,182)..(215,191);
\draw (292,229)..controls (348,270) and (408,269)..(525,262);
\draw (292,229) circle (4);\node at (488,300) {$\gamma_2$};
\end{tikzpicture}}
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm]
\draw[dash pattern=on 32pt off 24pt] (352,265) ellipse (352 and 265);
\draw (160,155)..controls (149,182) and (126,208)..(104,229)..controls (122,258) and (164,275)..(202,282);
\draw (160,155)..controls (174,170) and (200,180)..(220,185);
\draw (197,175)..controls (189,218) and (166,248)..(145,262);
\draw (260,98)..controls (222,155) and (190,263)..(196,361)..controls (196,388) and (198,410)..(205,437);
\draw (414,126)..controls (409,150) and (406,170)..(405,197);
\draw (399,292)..controls (395,353) and (399,379)..(413,404);
\draw (260,98)..controls (297,126) and (361,136)..(414,126);
\draw (205,437)..controls (249,450) and (344,423)..(413,404);
\draw (229,162)..controls (281,181) and (359,185)..(408,170);
\draw (211,230)..controls (250,248) and (292,250)..(325,244);
\draw (199,322)..controls (246,349) and (338,331)..(398,310);
\draw (198,389)..controls (250,405) and (352,387)..(402,367);
\draw (345,205)..controls (390,218) and (487,203)..(535,190)..controls (538,218) and (525,265)..(504,298)..controls (429,303) and (336,307)..(297,295)..controls (320,273) and (338,235)..(345,205);
\draw (376,211)..controls (375,242) and (360,273)..(344,302);
\draw (425,210)..controls (425,249) and (411,276)..(404,303);
\draw (495,201)..controls (493,238) and (478,280)..(461,302);
\draw (325,244) circle (4);
\draw[->] (-20,355)..controls (70,337) and (182,327)..(236,304)..controls (260,294) and (218,305)..(232,268)..controls (235,258) and (238,251)..(240,246);
\node at (-100,330) {$\ell_{11}$};\node at (775,250) {$V_1$};
\end{tikzpicture}}
\begin{center}\uline{Figure 7}\end{center}
'''
e=[('drawing','top','P1, gamma1, gamma2 within dashed boundary'),('drawing','middle','ruled vertical strip with gamma2'),('drawing','bottom','intersecting ruled strips, ell11, V1'),('text','bottom caption','Figure 7')]
d=[]
o=['Reused Figure7 belongs to Hironaka construction on scan029; three drawing stages reproduced; V1 label has no visible overbar.']
save(33,tex,e,d,o,sheet_kind='reused_typed')
