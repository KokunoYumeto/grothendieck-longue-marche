"""Independent visual transcription of the fixed scan028 boxes.

Authoring only: no source lookup, OCR, comparison, or TeX compilation.
The coordinates below were written manually after successful crop viewing.
"""
import csv
import json
import os
from pathlib import Path

OUT = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/second')


def figure(width, height, ink):
    return (r'\figure{\begin{tikzpicture}[x=.014cm,y=-.014cm,'
            r'line cap=round,line join=round,>=stealth,font=\footnotesize]' + '\n'
            + rf'\clip (0,0) rectangle ({width},{height});' + '\n'
            + ink.strip() + '\n' + r'\end{tikzpicture}}')


rows = []

rows.append(('S28-top_polygon', figure(605, 385, r'''
\draw[line width=.55pt] (160,38) .. controls (123,64) and (84,123) .. (46,168);
\draw[line width=.65pt] (53,126) .. controls (46,150) and (47,155) .. (67,143);
\fill (128,57) -- (134,52) -- (138,58) -- (131,65) -- cycle;
\draw[line width=.65pt] (34,176) .. controls (62,163) and (93,232) .. (96,271);
\draw[line width=.4pt] (46,192) .. controls (54,231) and (64,279) .. (73,301);
\draw[line width=.8pt,->] (84,262) .. controls (91,275) and (95,276) .. (105,256);
\draw[line width=.75pt] (158,43) .. controls (135,110) and (142,209) .. (90,308);
\draw[line width=.9pt] (166,39) .. controls (193,40) and (230,54) .. (250,70)
 .. controls (276,92) and (298,101) .. (330,114);
\draw[line width=.55pt] (193,38) .. controls (181,39) and (183,55) .. (199,52);
\draw[line width=.45pt] (168,44) .. controls (180,85) and (208,111) .. (237,145);
\draw[line width=.35pt] (214,104) .. controls (227,117) and (228,136) .. (239,149);
\draw[line width=.2pt] (238,148) -- (256,179);
\draw[line width=.18pt] (260,187) -- (286,225);
\draw[line width=1.5pt] (322,116) .. controls (303,140) and (276,229) .. (312,264);
\draw[line width=.7pt] (326,117) .. controls (316,157) and (322,213) .. (315,260);
\draw[line width=.8pt] (319,124) .. controls (287,175) and (285,233) .. (312,260);
\draw[line width=.8pt] (332,133) .. controls (329,175) and (319,227) .. (315,260);
\draw[line width=.45pt] (359,137) .. controls (348,170) and (333,210) .. (319,239);
\draw[line width=.6pt,->] (302,133) -- (320,123);
\draw[line width=.9pt] (91,311) .. controls (165,283) and (228,255) .. (296,275);
\draw[line width=.65pt,->] (116,303) -- (156,289);
\draw[line width=1pt] (92,313) .. controls (126,337) and (158,357) .. (199,370);
\draw[line width=.6pt] (100,317) .. controls (128,333) and (157,334) .. (188,344);
\draw[line width=.8pt] (113,322) .. controls (141,348) and (183,375) .. (187,351);
\draw[line width=.6pt] (206,349) .. controls (234,328) and (270,302) .. (296,286);
\draw[line width=.8pt] (210,334) .. controls (237,314) and (270,304) .. (297,286);
\draw[line width=.5pt,->] (207,356) -- (296,283);
\draw[line width=.7pt] (195,356) -- (205,357);
\draw[line width=.65pt] (279,284) .. controls (290,278) and (295,283) .. (291,296);
\draw[line width=.6pt,->] (181,195) .. controls (174,198) and (182,219) .. (201,213)
 .. controls (219,210) and (225,185) .. (212,172);
\fill (159,26) .. controls (174,23) and (180,47) .. (165,51)
 .. controls (149,54) and (145,38) .. (159,26);
\fill (81,303) -- (96,302) -- (107,315) -- (90,321) -- (78,314) -- cycle;
\fill (309,254) -- (320,260) -- (319,272) -- (308,265) -- cycle;
\draw[line width=.65pt] (211,385) .. controls (299,286) and (383,267) .. (451,274)
 .. controls (532,278) and (593,317) .. (605,385);
\draw[line width=.8pt] (285,385) .. controls (316,344) and (372,329) .. (419,315)
 .. controls (454,300) and (501,317) .. (526,343) -- (564,385);
\draw[line width=.7pt] (446,294) .. controls (427,290) and (410,310) .. (416,331)
 .. controls (426,357) and (454,339) .. (476,324)
 .. controls (491,313) and (470,274) .. (454,289);
\fill (417,314) circle[radius=1.8pt];
\fill (448,309) circle[radius=1.5pt];
\fill (475,318) circle[radius=1.8pt];
\draw[line width=.5pt,dash pattern=on 8pt off 8pt] (370,385) .. controls (409,359) and (460,360) .. (487,377);
''')))

rows.append(('S28-top_cut_sphere', figure(308, 372, r'''
\draw[line width=.95pt] (24,246) .. controls (17,223) and (42,115) .. (117,101)
 .. controls (170,77) and (243,113) .. (263,147)
 .. controls (271,161) and (274,174) .. (274,193);
\draw[line width=.8pt] (274,190) .. controls (240,207) and (238,238) .. (270,244)
 -- (279,242) .. controls (283,285) and (275,312) .. (254,327)
 .. controls (213,359) and (129,350) .. (74,330);
\draw[line width=.8pt] (31,249) .. controls (64,249) and (83,279) .. (77,318);
\draw[line width=.65pt] (73,329) .. controls (151,356) and (241,351) .. (281,308);
\draw[line width=.8pt] (183,344) .. controls (213,337) and (248,319) .. (267,298);
\fill (181,341) -- (191,331) -- (197,334) -- (196,342) -- cycle;
\draw[line width=1.35pt] (115,99) .. controls (111,87) and (130,72) .. (138,82)
 .. controls (139,87) and (137,92) .. (134,95)
 .. controls (127,106) and (122,113) .. (116,104) -- cycle;
\draw[line width=.65pt] (125,91) -- (131,86);
\draw[line width=.2pt] (147,234) .. controls (169,267) and (193,286) .. (222,311);
\draw[line width=.55pt] (222,311) -- (291,372);
''')))

rows.append(('S28-numbered_cap', figure(381, 343, r'''
\draw[line width=1.7pt] (151,42) .. controls (110,52) and (74,103) .. (70,157)
 .. controls (65,178) and (72,193) .. (82,194);
\draw[line width=.7pt] (148,43) .. controls (102,70) and (73,119) .. (76,185);
\draw[line width=.65pt] (144,42) .. controls (113,66) and (83,104) .. (72,144);
\draw[line width=.65pt] (105,64) .. controls (116,72) and (138,67) .. (149,58);
\draw[line width=1.5pt] (151,43) .. controls (178,28) and (204,28) .. (222,41)
 .. controls (265,64) and (295,116) .. (309,144);
\draw[line width=.65pt] (168,34) .. controls (192,28) and (227,30) .. (229,42)
 .. controls (218,40) and (209,38) .. (199,37);
\draw[line width=.6pt] (193,35) .. controls (192,56) and (222,66) .. (233,62);
\draw[line width=.9pt] (217,44) .. controls (253,63) and (288,101) .. (295,130);
\draw[line width=1.9pt] (308,144) .. controls (303,171) and (299,191) .. (282,211);
\draw[line width=.75pt] (301,153) .. controls (281,176) and (279,201) .. (285,207);
\draw[line width=.75pt] (309,154) .. controls (322,180) and (312,199) .. (286,208);
\draw[line width=.6pt] (316,153) .. controls (325,188) and (310,205) .. (287,213);
\draw[line width=1.8pt] (282,211) .. controls (248,229) and (195,249) .. (145,254);
\draw[line width=.65pt] (281,207) .. controls (254,219) and (222,237) .. (152,240);
\draw[line width=1pt] (80,194) .. controls (106,193) and (138,218) .. (145,250);
\draw[line width=.75pt] (80,194) .. controls (93,206) and (123,195) .. (140,232);
\draw[line width=.55pt] (79,200) .. controls (76,228) and (107,260) .. (137,257);
\draw[line width=.55pt] (82,218) .. controls (81,235) and (102,247) .. (116,249);
\draw[line width=.55pt] (78,216) -- (92,220);
\draw[line width=.95pt] (157,48) .. controls (170,107) and (157,174) .. (150,244);
\draw[line width=1.15pt] (159,51) .. controls (189,116) and (235,174) .. (282,210);
\draw[line width=2pt] (147,253) .. controls (172,206) and (229,175) .. (306,145);
\draw[line width=.75pt] (164,64) .. controls (181,98) and (178,125) .. (185,148)
 .. controls (189,185) and (204,209) .. (215,236);
\draw[line width=.7pt] (170,103) .. controls (184,119) and (171,130) .. (180,135)
 .. controls (190,143) and (191,118) .. (198,122);
\draw[line width=.65pt,->] (166,139) .. controls (178,158) and (205,153) .. (198,126);
\draw[line width=.7pt] (181,141) .. controls (172,159) and (186,173) .. (196,154);
\draw[line width=.65pt,->] (178,163) .. controls (173,188) and (190,194) .. (198,179);
\draw[line width=.55pt,->] (119,222) -- (137,234);
\draw[line width=.55pt,->] (294,166) -- (290,192);
\draw[line width=.55pt,->] (235,58) -- (214,43);
\fill (153,42) circle[radius=3.5pt];
\fill (80,194) circle[radius=2.3pt];
\fill (146,254) circle[radius=3.4pt];
\fill (211,239) circle[radius=2.2pt];
\fill (282,211) circle[radius=2.8pt];
\fill (308,144) circle[radius=2.6pt];
\node at (103,91) {$5$};
\node at (237,78) {$4$};
\node at (133,169) {$6$};
\node at (265,130) {$3$};
\node at (235,206) {$2$};
\node at (174,229) {$\unsure{1}$};
\node at (40,98) {$4'$};
\node at (283,26) {$5'$};
\node at (335,139) {$6'$};
\node at (260,242) {$1'$};
\node at (174,275) {$2'$};
\node at (91,270) {$3'$};
\node at (302,311) {$6$};
''')))

rows.append(('S28-cross', figure(196, 182, r'''
\draw[line width=1.05pt] (27,73) .. controls (66,83) and (119,91) .. (174,102);
\draw[line width=1.1pt] (78,156) .. controls (94,116) and (101,78) .. (128,20);
\draw[line width=.55pt] (90,147) -- (91,134);
\draw[line width=.5pt] (113,47) -- (121,25);
''')))

rows.append(('S28-upper_handle', figure(473, 401, r'''
\draw[line width=.75pt] (25,302) .. controls (5,255) and (26,136) .. (84,88)
 .. controls (168,8) and (302,7) .. (359,42)
 .. controls (428,75) and (459,137) .. (449,212)
 .. controls (452,262) and (425,300) .. (400,325);
\draw[line width=.95pt] (77,244) .. controls (107,169) and (124,94) .. (187,78)
 .. controls (226,69) and (267,57) .. (291,61)
 .. controls (338,63) and (390,109) .. (409,164)
 .. controls (428,215) and (413,249) .. (378,289);
\draw[line width=.65pt] (123,255) .. controls (145,196) and (213,147) .. (269,145)
 .. controls (320,140) and (355,146) .. (369,180)
 .. controls (382,213) and (365,256) .. (339,283);
\draw[line width=.65pt] (25,302) .. controls (55,258) and (90,233) .. (123,251)
 .. controls (156,263) and (144,306) .. (109,323)
 .. controls (80,340) and (34,331) .. (25,302);
\draw[line width=.65pt] (337,283) .. controls (359,272) and (376,282) .. (396,317)
 .. controls (421,347) and (378,374) .. (344,382)
 .. controls (294,396) and (300,320) .. (317,302) -- (337,283);
\draw[line width=.7pt,dash pattern=on 7pt off 5pt] (104,247) .. controls (148,177) and (189,136) .. (242,119)
 .. controls (297,105) and (345,117) .. (368,153)
 .. controls (387,185) and (380,234) .. (365,279);
\draw[line width=.55pt,dash pattern=on 9pt off 7pt] (95,264) -- (79,323);
\draw[line width=.6pt,dash pattern=on 9pt off 7pt] (366,282) -- (337,381);
\draw[line width=.6pt,->] (80,316) -- (96,271);
\draw[line width=.55pt,->] (29,218) -- (29,190);
\draw[line width=.55pt,->] (444,245) -- (451,210);
\draw[line width=.55pt,->] (370,229) -- (378,186);
\draw[line width=.7pt] (285,44) .. controls (267,39) and (249,56) .. (256,77)
 .. controls (265,110) and (294,92) .. (315,75)
 .. controls (332,60) and (303,17) .. (293,41);
\fill (255,62) circle[radius=2pt];
\fill (286,59) circle[radius=1.5pt];
\fill (314,65) circle[radius=2.2pt];
\fill (77,244) circle[radius=1.8pt];
\draw[line width=.7pt] (0,32) .. controls (55,14) and (101,9) .. (137,24);
\draw[line width=.65pt,->] (46,100) -- (142,34);
\draw[line width=.7pt] (50,83) -- (127,39);
\draw[line width=.5pt] (45,91) -- (134,36);
\draw[line width=.65pt] (119,33) .. controls (133,27) and (140,35) .. (132,51);
\draw[line width=.8pt] (0,90) .. controls (18,93) and (33,102) .. (39,120);
\draw[line width=.7pt] (0,105) .. controls (25,124) and (38,120) .. (27,96);
\draw[line width=1.4pt] (136,0) -- (151,16) -- (157,2);
''')))

rows.append(('S28-middle_ring', figure(388, 344, r'''
\draw[line width=1.15pt] (241,24) .. controls (154,24) and (44,87) .. (29,159)
 .. controls (13,217) and (60,276) .. (147,304)
 .. controls (222,336) and (307,267) .. (348,207)
 .. controls (390,141) and (359,47) .. (304,30)
 .. controls (278,20) and (258,20) .. (241,24);
\draw[line width=.55pt] (33,153) .. controls (13,211) and (53,266) .. (126,296);
\draw[line width=.5pt] (235,22) .. controls (307,15) and (365,49) .. (369,124);
\draw[line width=1.8pt] (220,60) .. controls (175,57) and (119,84) .. (112,135)
 .. controls (101,184) and (119,216) .. (158,244)
 .. controls (199,248) and (269,228) .. (306,201)
 .. controls (337,178) and (332,118) .. (311,94)
 .. controls (282,60) and (252,58) .. (220,60);
\draw[line width=.8pt] (190,123) .. controls (164,121) and (120,155) .. (130,185)
 .. controls (142,211) and (198,204) .. (237,190)
 .. controls (265,176) and (272,144) .. (254,129)
 .. controls (231,114) and (211,117) .. (190,123);
\draw[line width=.6pt] (121,159) .. controls (164,117) and (213,109) .. (254,124);
\draw[line width=.65pt] (130,147) .. controls (172,109) and (220,98) .. (272,116)
 .. controls (304,135) and (290,176) .. (254,197);
\draw[line width=.5pt] (110,143) .. controls (139,119) and (166,101) .. (214,108);
\draw[line width=.6pt] (220,59) .. controls (216,45) and (229,23) .. (242,25)
 .. controls (255,27) and (254,47) .. (258,58);
\draw[line width=.75pt] (218,60) .. controls (203,76) and (211,105) .. (224,110)
 .. controls (238,103) and (251,86) .. (258,63);
\draw[line width=.55pt] (224,75) .. controls (231,91) and (247,83) .. (249,65);
\draw[line width=.6pt,dash pattern=on 5pt off 5pt] (251,28) -- (261,58);
\draw[line width=.8pt] (157,243) .. controls (146,263) and (149,291) .. (166,316)
 .. controls (184,323) and (207,307) .. (212,292);
\draw[line width=.75pt] (157,243) -- (194,198);
\draw[line width=.55pt] (195,199) .. controls (208,212) and (220,227) .. (213,246);
\draw[line width=.6pt,dash pattern=on 6pt off 4pt] (206,203) -- (214,244);
\draw[line width=.55pt,->] (211,290) -- (216,253);
\draw[line width=.55pt] (170,228) -- (187,229) -- (199,228);
\draw[line width=.7pt,dash pattern=on 8pt off 6pt] (141,112) .. controls (177,75) and (214,71) .. (269,83)
 .. controls (302,84) and (337,102) .. (337,139);
\draw[line width=.7pt,dash pattern=on 9pt off 6pt] (328,169) .. controls (313,234) and (268,266) .. (224,286)
 .. controls (195,302) and (137,287) .. (111,266);
\draw[line width=.75pt,dash pattern=on 8pt off 6pt] (98,145) .. controls (61,170) and (70,219) .. (98,245);
\draw[line width=.55pt,->] (84,252) -- (110,264);
\draw[line width=.5pt,->] (47,160) .. controls (43,145) and (51,143) .. (64,140);
\draw[line width=.6pt,->] (323,207) -- (316,224);
\fill (220,59) circle[radius=2.4pt];
\fill (239,79) circle[radius=2pt];
\fill (158,244) circle[radius=2.5pt];
\fill (195,199) circle[radius=2pt];
\fill (211,291) circle[radius=2pt];
\draw[line width=.85pt] (122,0) .. controls (177,46) and (260,101) .. (388,195);
\draw[line width=.65pt] (326,139) -- (335,160) -- (338,141);
\draw[line width=.75pt] (166,344) .. controls (236,282) and (300,264) .. (388,265);
\draw[line width=.65pt] (214,344) .. controls (265,295) and (331,275) .. (388,268);
\draw[line width=.65pt] (268,344) .. controls (314,326) and (347,324) .. (388,324);
\draw[line width=.5pt] (82,293) -- (81,344);
''')))

rows.append(('S28-labelled_triangle', figure(362, 412, r'''
\draw[line width=1.7pt] (179,90) .. controls (118,97) and (65,143) .. (54,239);
\draw[line width=.6pt] (175,87) .. controls (113,101) and (66,159) .. (58,221);
\draw[line width=2pt] (179,90) .. controls (218,78) and (272,111) .. (287,153)
 .. controls (296,188) and (295,209) .. (292,223);
\draw[line width=.65pt] (185,82) .. controls (232,77) and (273,109) .. (281,145);
\draw[line width=.6pt,->] (266,180) -- (258,125);
\draw[line width=1.15pt] (178,96) .. controls (182,158) and (144,246) .. (98,326);
\draw[line width=1.1pt] (180,103) .. controls (191,164) and (201,231) .. (219,279)
 .. controls (233,292) and (254,297) .. (278,295);
\draw[line width=.75pt,->] (197,185) -- (217,258);
\draw[line width=.7pt] (54,244) .. controls (84,244) and (128,269) .. (101,307);
\draw[line width=.7pt] (54,249) .. controls (52,276) and (74,312) .. (98,326);
\draw[line width=.4pt] (58,259) .. controls (61,289) and (80,317) .. (96,326);
\draw[line width=1.2pt] (291,223) .. controls (249,250) and (232,280) .. (276,295);
\draw[line width=.45pt] (290,237) .. controls (283,262) and (277,280) .. (276,295);
\draw[line width=.55pt] (281,255) -- (286,255);
\draw[line width=.95pt] (98,326) .. controls (155,328) and (237,307) .. (278,295);
\draw[line width=.8pt] (98,327) .. controls (141,372) and (237,384) .. (276,301);
\draw[line width=.4pt] (106,333) .. controls (168,373) and (236,363) .. (274,303);
\draw[line width=.6pt] (181,350) -- (183,361) -- (202,355);
\draw[line width=.45pt] (206,81) .. controls (225,57) and (223,23) .. (205,14)
 .. controls (194,8) and (182,8) .. (169,12);
\draw[line width=.45pt] (144,35) .. controls (128,61) and (104,91) .. (80,117);
\draw[line width=.75pt,->] (86,110) -- (64,133);
\fill (179,90) circle[radius=2.8pt];
\fill (98,326) circle[radius=1.8pt];
\fill (278,295) circle[radius=2.1pt];
\node at (183,60) {$a$};
\node at (25,252) {$b_a$};
\node at (95,355) {$\unsure{b_a|\beta_a}$};
\node at (322,223) {$c_a$};
\node at (314,307) {$c_b$};
\node at (196,378) {$\unsure{a'|a^1}$};
\node at (48,9) {$6$};
\draw[line width=.95pt] (0,268) .. controls (67,318) and (124,374) .. (158,412);
\draw[line width=.65pt] (0,297) -- (60,321);
\draw[line width=.6pt] (111,369) -- (124,412);
\draw[line width=.75pt] (0,385) -- (28,412);
''')))

rows.append(('S28-lower_left_torus', figure(331, 308, r'''
\draw[line width=.7pt] (36,190) .. controls (48,114) and (108,43) .. (173,34)
 .. controls (224,25) and (278,52) .. (291,75)
 .. controls (310,103) and (300,159) .. (285,194)
 .. controls (271,236) and (257,244) .. (222,259)
 .. controls (166,289) and (92,288) .. (50,270)
 .. controls (28,261) and (19,245) .. (34,228);
\draw[line width=.75pt] (121,151) .. controls (152,119) and (188,105) .. (214,120)
 .. controls (236,132) and (226,170) .. (195,189)
 .. controls (169,204) and (117,207) .. (109,187)
 .. controls (101,174) and (111,156) .. (116,151) -- (121,151);
\draw[line width=.65pt] (168,122) .. controls (158,98) and (161,44) .. (185,38)
 .. controls (197,34) and (203,42) .. (205,49);
\draw[line width=.45pt] (166,118) .. controls (168,86) and (180,57) .. (191,57);
\draw[line width=.6pt] (169,122) .. controls (183,118) and (197,111) .. (201,100);
\draw[line width=.6pt] (147,137) .. controls (171,137) and (198,145) .. (218,142);
\draw[line width=.75pt] (211,121) .. controls (225,124) and (233,142) .. (234,154);
\draw[line width=.65pt] (160,202) .. controls (143,213) and (128,212) .. (126,247)
 .. controls (121,276) and (145,293) .. (155,275);
\draw[line width=.6pt,dash pattern=on 8pt off 7pt] (168,204) .. controls (178,228) and (175,265) .. (157,278);
\draw[line width=.45pt,->] (144,215) -- (151,209);
\draw[line width=.5pt,->] (167,272) -- (156,278);
''')))

rows.append(('S28-lower_middle_ring', figure(451, 372, r'''
\draw[line width=.8pt] (248,34) .. controls (163,37) and (68,83) .. (39,169)
 .. controls (19,211) and (29,267) .. (63,301)
 .. controls (108,350) and (182,359) .. (232,348)
 .. controls (291,335) and (370,307) .. (405,260)
 .. controls (441,211) and (432,133) .. (410,109)
 .. controls (367,60) and (312,35) .. (277,32) -- (248,34);
\draw[line width=.6pt] (75,139) .. controls (115,88) and (176,57) .. (240,39);
\draw[line width=.8pt] (264,40) .. controls (226,29) and (172,66) .. (148,108)
 .. controls (113,162) and (111,194) .. (136,228)
 .. controls (161,263) and (185,269) .. (210,270);
\draw[line width=.65pt] (153,201) .. controls (154,174) and (190,146) .. (228,140)
 .. controls (263,131) and (293,135) .. (308,147)
 .. controls (329,165) and (310,205) .. (282,225)
 .. controls (257,247) and (217,246) .. (180,237)
 .. controls (156,232) and (147,216) .. (153,201);
\draw[line width=.9pt] (147,194) .. controls (172,157) and (213,136) .. (252,134);
\draw[line width=.7pt] (145,200) .. controls (170,169) and (206,152) .. (235,126);
\draw[line width=.75pt] (210,270) .. controls (270,279) and (315,238) .. (326,184)
 .. controls (337,143) and (316,104) .. (280,121) -- (245,135);
\draw[line width=.5pt] (307,144) .. controls (317,146) and (311,153) .. (309,155);
\draw[line width=.8pt] (211,269) -- (224,244);
\draw[line width=.8pt] (209,270) .. controls (199,310) and (208,348) .. (230,348);
\draw[line width=.6pt,dash pattern=on 7pt off 6pt] (237,257) .. controls (250,282) and (235,319) .. (237,341);
\draw[line width=.55pt,->] (231,341) -- (228,349);
\draw[line width=.65pt] (207,274) .. controls (203,289) and (211,309) .. (215,305) -- (213,279);
\draw[line width=.6pt,->] (199,282) -- (217,270);
\draw[line width=.6pt] (209,314) -- (226,317);
\draw[line width=.55pt] (237,323) .. controls (249,315) and (260,321) .. (270,316);
\draw[line width=.6pt,dash pattern=on 3pt off 6pt] (139,245) .. controls (140,268) and (159,292) .. (181,303);
\draw[line width=.55pt,dash pattern=on 5pt off 7pt] (344,140) -- (339,195);
\draw[line width=.6pt,dash pattern=on 10pt off 4pt] (338,220) .. controls (331,261) and (301,289) .. (276,313);
\draw[line width=.6pt,->] (281,34) .. controls (294,51) and (320,66) .. (331,73);
\draw[line width=.6pt] (330,78) .. controls (317,96) and (321,119) .. (339,114)
 .. controls (354,102) and (344,85) .. (330,78);
\fill (335,96) circle[radius=1.7pt];
\fill (331,80) circle[radius=1.4pt];
\fill (342,117) circle[radius=1.3pt];
\fill (209,270) circle[radius=2.3pt];
\draw[line width=.55pt,->] (280,29) -- (252,33);
\draw[line width=.65pt,->] (216,149) -- (197,153);
\node[rotate=25] at (370,38) {$2$};
\draw[line width=.7pt] (389,14) .. controls (399,49) and (401,53) .. (408,34)
 -- (420,45) -- (431,21) .. controls (443,32) and (445,19) .. (451,11);
''')))

rows.append(('S28-lower_handle', figure(587, 519, r'''
\draw[line width=.7pt] (199,481) .. controls (132,503) and (64,469) .. (37,422)
 .. controls (19,388) and (20,319) .. (35,270)
 .. controls (53,188) and (126,105) .. (205,58)
 .. controls (292,2) and (416,2) .. (497,67)
 .. controls (558,113) and (564,192) .. (551,279)
 .. controls (547,312) and (538,335) .. (526,353);
\draw[line width=.95pt] (191,422) .. controls (132,422) and (95,357) .. (85,292)
 .. controls (74,229) and (94,181) .. (131,144)
 .. controls (176,109) and (240,87) .. (285,84);
\draw[line width=.75pt] (286,95) .. controls (291,87) and (316,84) .. (339,84);
\draw[line width=.75pt] (347,83) .. controls (394,83) and (439,117) .. (461,161)
 .. controls (475,197) and (465,269) .. (444,300);
\draw[line width=.85pt] (234,372) .. controls (185,377) and (135,348) .. (115,318)
 .. controls (105,300) and (104,276) .. (108,255)
 .. controls (151,188) and (189,146) .. (237,125)
 .. controls (280,107) and (330,107) .. (359,117)
 .. controls (411,131) and (443,180) .. (436,231)
 .. controls (432,265) and (415,283) .. (389,291);
\draw[line width=.7pt] (190,422) .. controls (163,417) and (133,383) .. (118,324);
\draw[line width=.6pt,->] (127,146) .. controls (167,121) and (231,95) .. (290,87);
\draw[line width=.65pt,->] (223,132) .. controls (240,107) and (257,100) .. (276,98);
\draw[line width=.65pt,->] (183,157) .. controls (163,166) and (130,204) .. (108,260);
\draw[line width=.7pt] (234,372) .. controls (219,370) and (199,398) .. (190,434)
 .. controls (181,467) and (199,487) .. (226,490);
\draw[line width=.35pt] (234,372) .. controls (252,363) and (260,373) .. (264,397)
 .. controls (271,439) and (255,479) .. (226,490);
\draw[line width=.65pt,->] (191,398) -- (213,399);
\draw[line width=.7pt] (389,290) .. controls (425,296) and (484,305) .. (503,337)
 .. controls (515,360) and (505,387) .. (492,399)
 .. controls (474,412) and (445,411) .. (435,407)
 .. controls (412,389) and (384,358) .. (379,333)
 .. controls (375,318) and (383,307) .. (391,306);
\draw[line width=.7pt,->] (483,326) -- (504,339) -- (512,316);
\draw[line width=.55pt] (479,393) .. controls (492,393) and (500,386) .. (503,379);
\draw[line width=.55pt,dash pattern=on 6pt off 5pt] (468,325) .. controls (452,348) and (459,383) .. (438,402);
\draw[line width=.65pt,->] (445,397) -- (436,407);
\draw[line width=.55pt,dash pattern=on 5pt off 9pt] (390,36) .. controls (429,53) and (450,75) .. (466,104);
\draw[line width=.55pt,dash pattern=on 2pt off 7pt] (473,135) .. controls (491,194) and (493,249) .. (479,288);
\draw[line width=.55pt,dash pattern=on 5pt off 7pt] (477,289) -- (470,312);
\draw[line width=.55pt,dash pattern=on 5pt off 9pt] (72,276) .. controls (43,330) and (61,387) .. (97,417);
\draw[line width=.55pt,dash pattern=on 8pt off 8pt] (97,417) .. controls (113,432) and (142,443) .. (178,449);
\draw[line width=.6pt,dash pattern=on 3pt off 5pt] (218,460) -- (242,460) -- (250,469) -- (228,488);
\draw[line width=.6pt,->] (220,478) -- (226,490);
\draw[line width=.65pt,->] (61,231) .. controls (52,236) and (61,253) .. (72,247)
 .. controls (88,241) and (85,219) .. (67,210);
\draw[line width=.65pt] (64,209) -- (74,206);
\fill (234,372) circle[radius=1.8pt];
\fill (435,407) circle[radius=1.3pt];
\draw[line width=1.1pt] (25,0) .. controls (71,51) and (115,63) .. (161,69)
 .. controls (212,79) and (258,36) .. (280,0);
\draw[line width=.7pt] (122,0) .. controls (116,34) and (127,57) .. (151,69)
 .. controls (170,73) and (190,47) .. (192,24);
\draw[line width=.7pt,dash pattern=on 8pt off 5pt] (58,4) .. controls (105,50) and (160,43) .. (198,42)
 .. controls (236,36) and (257,13) .. (269,0);
\draw[line width=.6pt,->] (188,27) -- (192,0);
\draw[line width=.45pt] (54,44) -- (57,97) -- (61,136);
\draw[line width=.65pt] (166,71) .. controls (231,50) and (277,23) .. (331,27);
\draw[line width=.55pt,->] (331,27) -- (326,20);
\draw[line width=.9pt] (423,0) .. controls (481,39) and (529,103) .. (587,159);
\draw[line width=.8pt] (479,0) .. controls (489,21) and (501,44) .. (515,56);
\draw[line width=.85pt] (544,0) .. controls (535,17) and (530,43) .. (515,56)
 .. controls (548,88) and (568,91) .. (587,89);
\draw[line width=.75pt] (515,56) -- (587,51);
\node at (509,82) {$\unsure{b_a|\beta_a}$};
''')))

rows.append(('S28-arrow_end', figure(83, 80, r'''
\draw[line width=1.1pt] (12,0) .. controls (28,20) and (43,38) .. (52,51);
\draw[line width=.55pt] (52,51) .. controls (50,57) and (42,61) .. (33,65);
''')))

rows.append(('S28-counts', figure(296, 327, r'''
\node[rotate=25] at (129,91) {4 sommets};
\node[rotate=25] at (76,215) {6 arêtes};
\node[rotate=25] at (175,253) {2 \unsure{hexagones}};
\draw[line width=.65pt] (0,80) .. controls (9,52) and (21,14) .. (17,0);
\draw[line width=.5pt] (7,57) -- (21,7);
\draw[line width=.5pt,->] (6,17) -- (19,5);
\draw[line width=.95pt] (296,35) .. controls (263,67) and (247,99) .. (253,144)
 .. controls (256,174) and (274,189) .. (296,204);
\draw[line width=.45pt,->] (271,90) .. controls (266,77) and (279,69) .. (289,69);
\draw[line width=.8pt] (0,270) .. controls (29,275) and (75,294) .. (113,327);
\draw[line width=.7pt,->] (0,270) -- (46,307);
\draw[line width=.75pt] (47,319) -- (43,312) -- (42,324);
''')))

rows.append(('S28-number27', r'\margin{27}'))

rows.append(('S28-interior-one', figure(56, 52, r'''
\node at (36,34) {$\unsure{1}$};
\draw[line width=2.3pt] (0,49) -- (56,4);
\draw[line width=1pt] (16,0) -- (16,17) .. controls (22,13) and (25,24) .. (23,32);
\draw[line width=.9pt] (0,16) -- (6,28) -- (15,23);
\draw[line width=.7pt] (30,17) -- (34,7);
\draw[line width=.8pt] (38,15) -- (40,3);
\draw[line width=.75pt] (28,42) -- (56,40);
\draw[line width=1.4pt] (9,51) -- (56,46);
''')))

rows.append(('S28-lower-left-label', figure(64, 56, r'''
\node at (24,30) {$\unsure{b_a|\beta_a}$};
\draw[line width=1.3pt] (0,0) -- (61,56);
\draw[line width=.9pt] (28,0) -- (64,23);
\draw[line width=.4pt] (35,2) -- (64,18);
\draw[line width=.75pt] (37,42) -- (41,56);
''')))

rows.append(('S28-loop-arrow', figure(53, 72, r'''
\draw[line width=.9pt] (0,34) -- (17,0);
\draw[line width=.95pt] (39,72) .. controls (39,47) and (47,21) .. (53,5);
\draw[line width=.6pt] (15,38) .. controls (9,40) and (10,54) .. (18,57)
 .. controls (32,60) and (37,45) .. (34,32)
 .. controls (32,25) and (27,23) .. (21,22);
\draw[line width=.7pt] (30,14) -- (20,15) -- (21,22) -- (19,27);
''')))

rows.append(('S28-last-count', r'\rotatebox{25}{2 \unsure{hexagones}}'))

rows.append(('S28-unsupported-gray-sweep', figure(256, 298, r'''
\draw[line width=.4pt] (0,158) -- (9,136);
\draw[line width=.75pt] (0,281) .. controls (77,268) and (117,266) .. (179,284)
 .. controls (190,288) and (199,293) .. (207,298);
\draw[line width=.6pt] (83,298) .. controls (87,294) and (93,294) .. (98,294);
\draw[line width=.65pt] (104,294) .. controls (106,274) and (124,286) .. (129,298);
''')))

rows.append(('S28-unsupported-gray-ellipse', ''))


OBSERVATIONS = {
    'S28-top_polygon': 'Manual paths preserve the directed boundary strokes, repeated edges, black vertices, central loop arrow, and the lower adjoining handle fragments. A small loop attached to the upper edge is reproduced geometrically, without turning it into a letter. Faint diffuse gray show-through on the right is excluded.',
    'S28-top_cut_sphere': 'Open outline with two cut notches, thick upper mark, repeated lower arcs, and the beginning of a diagonal stroke. The diagonal darkens and continues to the crop boundary; it is represented as face ink rather than as a closed ellipse.',
    'S28-numbered_cap': 'Six outer primed labels, interior labels, and the separate lower 6 are retained. The small interior 1 is not securely distinguishable from the overlapping strokes and is marked unsure. Dense retracing is represented by parallel paths and heavy nodes; no inferred cancellation is imposed on it.',
    'S28-cross': 'Two crossed strokes with repeated portions near the ends; no definite arrowheads are present.',
    'S28-upper_handle': 'Open handle outline, two elliptical cut ends, central dashed trace, local direction marks, upper loop, and clipped adjacent drawing fragments are included. Incomplete neighboring text at the right boundary is not completed.',
    'S28-middle_ring': 'Multiple concentric skew outlines, upper and lower loops, solid and segmented paths, marked vertices, direction marks, the diagonal crossing stroke, and lower adjoining arcs are included. Dense intersections have been transcribed as visible geometry rather than normalized topological connections.',
    'S28-labelled_triangle': 'The labels a, b_a, c_a, and c_b are read directly. The crossed lower-left label is b_a or beta_a; the lower label is a prime or a raised 1. Both doubts remain local. The two side cut curves, lower arcs, upper outer curve, repeated edges, and diagonal crossing stroke are retained.',
    'S28-lower_left_torus': 'Outer contour has a real gap at the left; it is not closed in the transcription. The inner opening, upper return strokes, lower loop, and its segmented side are included.',
    'S28-lower_middle_ring': 'Outer contour, inner opening and folded inner curve, upper small eye-like loop, bottom loop, and segmented traces are retained. The clipped neighboring 2 and following visible stroke fragments appear at the upper-right; no complete word beyond the rectangle is supplied.',
    'S28-lower_handle': 'Large open handle with two cut ends, dotted paths, a local loop arrow, marked endpoints, upper adjacent drawing fragments, the crossed label and diagonal stroke. No closed torus is substituted for the open shape.',
    'S28-arrow_end': 'One hooked terminal of a diagonal stroke is visible. The missing second side of a conventional arrowhead is not invented.',
    'S28-counts': 'Clockwise 25-degree display rotation made the three slanted lines legible: 4 sommets, 6 arêtes, 2 hexagones. The last polygon word remains marked unsure because some central and terminal lettering is compressed/obscured. Original upward slant is retained in the TikZ text nodes.',
    'S28-number27': 'Margin number 27.',
    'S28-interior-one': 'Heavily overdrawn intersection. A possible small 1 is retained with an uncertainty mark; the visible intersecting paths are also represented.',
    'S28-lower-left-label': 'A descending stem and two loop-like forms are crossed by the diagonal stroke. Latin b with subscript a and Greek beta with subscript a remain alternatives; no substitution based on expected labeling is made.',
    'S28-loop-arrow': 'This is a curved direction arrow with an upper-left hook, not a word or a numeral. Both neighboring boundary segments are included.',
    'S28-last-count': 'The slanted count reads 2 followed by a tentative hexagones. A successful clockwise 25-degree view was used. Cropped remnants of the preceding word and the surrounding curves are not promoted into additional text.',
    'S28-unsupported-gray-sweep': 'Diffuse gray shapes are consistent with paper/show-through and have no independently secure face-ink contour. Only the black left-edge segment and bottom adjoining arcs inside the rectangle are transcribed.',
    'S28-unsupported-gray-ellipse': 'Only diffuse texture and show-through are visible. No independently readable face text or deliberate ellipse is established; reading is intentionally empty.',
}


def write_atomic(path, writer):
    temp = path.with_name(path.name + '.tmp')
    with temp.open('w', encoding='utf-8', newline='') as stream:
        writer(stream)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert len(rows) == 19
    assert len({name for name, _ in rows}) == 19

    def tsv_writer(stream):
        writer = csv.writer(stream, delimiter='\t')
        writer.writerow(['box', 'reading'])
        writer.writerows(rows)

    write_atomic(OUT / '148_scan028_second.tsv', tsv_writer)
    alternate = {'S28-numbered_cap', 'S28-top_polygon', 'S28-interior-one', 'S28-lower-left-label'}
    rotated = {'S28-counts', 'S28-last-count'}
    boxes = []
    for name, _ in rows:
        views = ['successful enhanced JPEG view']
        if name in alternate:
            views.append('successful nearest-neighbor contrast view')
        if name in rotated:
            views.append('successful clockwise 25-degree rotated view')
        boxes.append({'box': name, 'viewed': True, 'views': views,
                      'display_rotation_degrees': -25 if name in rotated else 0,
                      'observation': OBSERVATIONS[name]})
    journal = {
        'page': '148_scan028',
        'blind_inputs': [
            '/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan028/scan.jpg',
            '/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan028/boxes.tsv'],
        'boxes': boxes,
        'unresolved': [
            'Obscured interior numeral: possible 1.',
            'Crossed lower-left label: b_a or beta_a.',
            'Lower triangle label: a prime or raised 1.',
            'Last count word: tentative hexagones.',
            'Dense retraced path intersections retain geometric rather than inferred topological interpretation.'],
        'authoring_script': 'scripts/blind_authoring/148_scan028.py',
        'exclusions': 'Paper specks, diffuse show-through, and incomplete outside-rectangle text are not normalized into source content.'}

    def journal_writer(stream):
        json.dump(journal, stream, ensure_ascii=False, indent=2)
        stream.write('\n')

    write_atomic(OUT / '148_scan028_blind_journal.json', journal_writer)
    print('Atomically wrote 19 independent readings and the scan028 viewing journal.')


if __name__ == '__main__':
    main()
