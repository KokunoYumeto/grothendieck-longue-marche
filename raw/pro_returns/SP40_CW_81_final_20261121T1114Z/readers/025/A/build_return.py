from pathlib import Path
import json,re,datetime,hashlib
B=Path('out/readers/025/A')
groups=[]
def group(gid,origin,rect,baseline,body,semantic='',qualified=False,ownership='',observed=None,candidates=None,hand='his hand',role=None):
    x,y=origin;w,h=rect
    s=f'% BEGIN {gid}\n% full-scan origin: ({x},{y}); x=.20pt, y=-.20pt; local baseline: (0,{baseline}); fixed drawing rectangle: (0,0)--({w},{h}).\n'
    if candidates:s+='% complete candidates: '+' ; '.join(candidates)+'\n'
    if role:s+='% local role/state qualification: '+role+'\n'
    if qualified:s+=r'\unsure{'
    s+=r'\begin{tikzpicture}[x=.20pt,y=-.20pt,baseline=(localbase),line cap=round,line join=round]'+'\n'
    s+=f'\\path[use as bounding box] (0,0) rectangle ({w},{h});\n\\coordinate (localbase) at (0,{baseline});\n'
    if semantic:s+=r'\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at (0,'+str(baseline)+r') {\phantom{$'+semantic+r'$}};'+'\n'
    s+=f'\\begin{{scope}}[shift={{(-{x},-{y})}}]\n'+body.rstrip()+'\n'+r'\end{scope}'+'\n'+r'\end{tikzpicture}'
    if qualified:s+='}'
    s+='\n% END '+gid+'\n'
    groups.append(dict(id=gid,origin_full_scan=[x,y],coordinate_unit_pt=.20,y_direction='down',local_baseline=[0,baseline],drawing_rectangle_local=[0,0,w,h],observed_locus_bbox_full_scan=observed or [x,y,x+w,y+h],observed_locus_bbox_status='Manual approximate observed locus box, not a computed path bound.',drawing_rectangle_status='Fixed origin and layout rectangle, recorded separately from observed locus; no curve-extrema computation.',ownership=ownership,complete_candidates=candidates or [semantic],semantic_annotation=semantic,qualified_here=qualified,hand=hand,role=role,geometric_validation='manual approximation from once-viewed image; source-only, no rendered or metric validation'))
    return s
G={}
G['strike_open']=group('A025-G00',(285,68),(410,114),61,r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (290,129) {\rlap{Soit en effet}\phantom{\deleted{Soit en effet}}};
\draw[line width=.55pt] (291,129) .. controls (374,115) and (548,111) .. (686,106);''',ownership='Complete deleted Soit en effet and its single long cancellation stroke; Si stays outside.',candidates=[r'\deleted{Soit en effet}'])
G['s1']=group('A025-S01',(830,122),(91,73),57,r'''\draw[line width=.85pt] (839,131) .. controls (853,128) and (864,133) .. (877,131);
\draw[line width=.58pt] (840,139) .. controls (852,142) and (866,149) .. (873,155) .. controls (865,165) and (851,173) .. (834,180) .. controls (859,179) and (879,180) .. (892,181) .. controls (897,183) and (896,188) .. (896,190);
\draw[line width=.48pt] (835,144) .. controls (833,148) and (833,150) .. (833,154);
\draw[line width=.64pt] (841,143) .. controls (844,153) and (843,164) .. (845,176) .. controls (849,184) and (837,184) .. (839,177);
\draw[line width=.48pt] (839,141) -- (872,153);
\draw[line width=.60pt] (895,130) -- (917,132);
\draw[line width=.66pt] (902,159) .. controls (902,163) and (904,166) .. (908,168);''',semantic=r'\deleted{\unsure{E|I}}\Sigma_{\unsure{i|\prime}}^-',qualified=True,ownership='Complete overwritten Sigma, its predecessor strokes, one short upper head, minus and undotted index. Preceding subset and following comma stay outside.',candidates=[r'\deleted{E}\Sigma_i^-',r'\deleted{I}\Sigma_i^-',r'\deleted{E}\Sigma_{\prime}^-',r'\deleted{I}\Sigma_{\prime}^-'],role='Predecessor E/I unresolved; upper run head/retrace versus independent run unresolved; index i/prime unresolved. Primary candidate uses deleted E, live Sigma_i^- and head/retrace. Independent upper-run candidate has undetermined hand.')
G['cap']=group('A025-G01',(1099,153),(47,36),27,r'''\draw[line width=.55pt] (1105,168) -- (1137,168);
\draw[line width=.50pt] (1104,175) -- (1130,176);
\draw[line width=.85pt] (1108,175) .. controls (1120,157) and (1127,153) .. (1135,164) .. controls (1140,172) and (1139,177) .. (1139,181);''',semantic=r'\deleted{=}\cap',ownership='Only overwritten equals and live cap; barred U and E group outside.',candidates=[r'\deleted{=}\cap'])
G['E']=group('A025-G02',(1159,132),(66,59),43,r'''\draw[line width=.50pt] (1167,141) -- (1167,169) .. controls (1168,173) and (1175,172) .. (1195,172);
\draw[line width=.43pt] (1173,141) .. controls (1180,137) and (1193,137) .. (1199,143);
\draw[line width=.47pt] (1169,161) -- (1188,161);
\fill (1218,157) .. controls (1221,156) and (1221,160) .. (1219,162) -- (1217,161) -- cycle;
\draw[line width=.52pt] (1211,174) .. controls (1214,180) and (1214,183) .. (1209,185);''',semantic=r'E_{\unsure{j|i}}',qualified=True,ownership='Complete E, detached upper arm, one high index point and one low index body. Nonemptiness relation outside.',candidates=[r'E_j',r'E_i'],role='Index j primary, i retained; point retained once as the common dotted-index component. No independent-point candidate is selected.')
G['etsi']=group('A025-G03',(1405,138),(136,60),39,r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1410,177) {\rlap{et si}\phantom{\deleted{et si}}};
\draw[line width=.56pt] (1421,164) .. controls (1451,174) and (1501,181) .. (1535,190);''',ownership='Complete deleted et si and descending cancellation stroke; alors outside.',candidates=[r'\deleted{et si}'])
G['ona']=group('A025-G04',(295,283),(143,22),15,r'''\fill (301,297) -- (303,293) -- (306,294) -- (304,297) -- cycle;
\draw[line width=.24pt] (325,296) .. controls (334,293) and (339,293) .. (343,292);
\draw[line width=.49pt] (343,292) -- (352,292) -- (357,296);
\draw[line width=.52pt] (422,295) .. controls (423,293) and (429,293) .. (432,295);''',semantic=r'\text{on a}',qualified=True,ownership='Entire reduced on a phrase, all three separated mark clusters; no ordinary duplicate on a.',candidates=['Reduced complete phrase on a','Three unassigned traces'],role='Lexical reading on a retained with low confidence; role/attachment and hand of unassigned-trace candidate undetermined.')
G['union']=group('A025-G05',(847,268),(84,79),68,r'''\draw[line width=.65pt] (865,275) .. controls (873,293) and (865,326) .. (880,337) .. controls (899,348) and (923,325) .. (919,285);
\draw[line width=.43pt] (853,287) .. controls (863,279) and (870,280) .. (876,291) .. controls (879,309) and (873,327) .. (883,336) .. controls (896,345) and (922,321) .. (917,282);
\draw[line width=.53pt] (857,291) .. controls (875,291) and (893,293) .. (903,290);
\draw[line width=.44pt] (912,290) -- (914,316);''',semantic=r'\unsure{\rlap{\raisebox{.65ex}{$\scriptstyle-$}}\bigcup|\deleted{\bigcap}\bigcup}',qualified=True,ownership='Complete main union/cross/retraces. Lower alpha-in-K limit stays outside exactly once.',candidates=[r'\rlap{\raisebox{.65ex}{$\scriptstyle-$}}\bigcup',r'\deleted{\bigcap}\bigcup'],role='Cross presence firm; complete cross-on-union versus earlier-intersection/live-union state remains unresolved. No disjointness operation inferred.')
G['s2']=group('A025-S02',(966,251),(98,98),81,r'''\draw[line width=.43pt] (995,270) -- (1012,260) .. controls (1018,265) and (1022,273) .. (1033,273);
\draw[line width=.54pt] (973,291) -- (1021,287);
\draw[line width=.43pt] (975,291) .. controls (988,296) and (1002,302) .. (1007,309) .. controls (1012,316) and (984,325) .. (970,330) .. controls (997,329) and (1019,327) .. (1028,332);
\draw[line width=.52pt] (1047,284) -- (1051,304);
\draw[line width=.50pt] (1039,294) -- (1060,294);
\draw[line width=.45pt] (1047,337) .. controls (1043,326) and (1030,321) .. (1030,333) .. controls (1030,349) and (1043,342) .. (1048,330) .. controls (1051,324) and (1052,319) .. (1053,314);
\draw[line width=.51pt] (1042,331) .. controls (1046,337) and (1050,341) .. (1057,339);
% BEGIN A025-M01
% nested full-scan origin (1041,306), local baseline (0,0), base-west zero-separation anchor; owns two upper-index traces only.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1041,306) {\unsure{\begin{tikzpicture}[x=.20pt,y=-.20pt,baseline=(markbase)]
\path[use as bounding box] (0,0) rectangle (10,15);\coordinate (markbase) at (0,0);
\draw[gray,line width=.21pt] (1,2) -- (3,3);
\fill (3,9) -- (6,8) -- (8,11) -- (5,14) -- cycle;
\end{tikzpicture}}};
% END A025-M01''',semantic=r'\widehat{\Sigma}_\alpha^+',ownership='Complete hatted Sigma, alpha, plus and nested two-mark group M01. No nearby union or limit owned.',candidates=[r'\widehat{\Sigma}_\alpha^+ with the two locally qualified upper-index traces'],role='Head/body pale junction observed joined. The two small upper-index traces retain attachment, role, hand and surface-origin uncertainty separately.')
G['ou']=group('A025-G06',(1220,295),(56,33),25,r'''\fill (1226,320) -- (1230,316) -- (1233,316) -- (1232,320) -- cycle;
\draw[line width=.29pt] (1241,320) -- (1256,318);
\draw[line width=.48pt] (1256,318) -- (1270,319);
\draw[line width=.43pt] (1261,302) -- (1264,309);''',semantic=r'\text{où}',qualified=True,ownership='Entire reduced où including its descending accent. Following i-in-K condition outside.',candidates=['Reduced complete word où','Three unassigned traces'],role='où primary; lexical attachment and alternative trace hand remain unresolved.')
G['s3']=group('A025-S03',(1244,359),(96,54),41,r'''\draw[line width=.48pt] (1251,369) -- (1304,365);
\draw[line width=.39pt] (1254,369) .. controls (1271,372) and (1294,378) .. (1295,382) .. controls (1283,389) and (1260,394) .. (1248,398) -- (1302,398);
\draw[line width=.47pt] (1320,363) -- (1324,376);
\draw[line width=.47pt] (1312,368) -- (1332,367);
\draw[line width=.48pt] (1326,396) .. controls (1319,405) and (1305,406) .. (1305,401) .. controls (1308,396) and (1317,401) .. (1321,400) -- (1330,404);''',semantic=r'\Sigma_\alpha^+',ownership='Only complete Sigma alpha plus before membership. Adjacent pi expression outside.',role='Joined upper arm and body; this local head carries no independent detached-run doubt.')
G['edge']=group('A025-G07',(1597,345),(71,52),37,r'''\draw[line width=.43pt] (1605,350) -- (1608,387) -- (1630,365) -- (1635,354);
\draw[line width=.43pt] (1602,369) -- (1635,353);
\draw[line width=.42pt] (1609,369) .. controls (1622,373) and (1624,375) .. (1632,374) .. controls (1642,373) and (1644,369) .. (1640,367);
\draw[line width=.39pt] (1654,367) -- (1646,381) -- (1646,386);
\draw[line width=.55pt] (1623,379) -- (1665,379);''',semantic=r'\deleted{\unsure{\text{les}|K|\text{tel}}}',qualified=True,ownership='Complete cancelled edge cluster and all crossing/rightward runs. No separate comma selected; closing parenthesis of pi expression stays outside.',candidates=[r'\deleted{\text{les}}',r'\deleted{K}',r'\deleted{\text{tel}}'],role='les primary, K/tel retained; deletion state firm. Final rightward run reaches physical edge; no independent terminal comma observed.')
G['oldU']=group('A025-G08',(1103,438),(56,74),57,r'''\draw[line width=.42pt] (1111,449) .. controls (1112,479) and (1112,495) .. (1130,499) .. controls (1144,501) and (1152,476) .. (1149,448);
\draw[line width=.44pt] (1119,460) -- (1149,450) -- (1131,476) -- (1148,476);
\draw[line width=.59pt] (1149,448) .. controls (1153,473) and (1147,494) .. (1138,501) .. controls (1139,510) and (1146,508) .. (1152,502);''',semantic=r'\unsure{\deleted{U\Sigma}|\deleted{\bigcup\Sigma}|\deleted{U}|U\Sigma}',qualified=True,ownership='Complete corrected/possibly live U-Sigma cluster before les, with one lower hook. Live les outside.',candidates=[r'\deleted{U\Sigma}',r'\deleted{\bigcup\Sigma}',r'\deleted{U}',r'U\Sigma'],role='Deleted U Sigma primary; alternative glyphs preserve original C row and newly retained live compound state. No chronology supplied.')
G['s4']=group('A025-S04',(1288,437),(70,48),38,r'''\draw[line width=.58pt] (1300,444) -- (1325,445);
\draw[line width=.50pt] (1294,453) .. controls (1306,456) and (1319,456) .. (1324,458) .. controls (1322,462) and (1302,470) .. (1292,473) -- (1325,474) -- (1333,472);
\draw[line width=.54pt] (1346,442) -- (1349,455);
\draw[line width=.47pt] (1338,447) -- (1356,446);
\draw[line width=.56pt] (1343,468) .. controls (1352,464) and (1344,475) .. (1335,479) .. controls (1326,481) and (1331,473) .. (1339,474) -- (1354,478);''',semantic=r'\Sigma_\alpha^+',ownership='Complete live Sigma alpha plus after les; shared foot/index contact retained once.',candidates=[r'\Sigma_\alpha^+ with head/retrace',r'\Sigma_\alpha^+ with independent upper run'],role='Detached head/body; head role locally unresolved. Recurring primary printed without second unsure. Independent-run candidate upper-hand undetermined.')
G['K']=group('A025-G09',(874,478),(194,162),139,r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (880,543) {$\inserted{K\setminus\{i\}}$};
\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at (952,615) {\phantom{$\deleted{K}$}};
\draw[line width=.45pt] (959,552) -- (973,621);
\draw[line width=.45pt] (963,590) -- (1000,564);
\draw[line width=.57pt] (969,597) -- (1000,613);
\draw[line width=.50pt] (979,548) .. controls (991,552) and (1003,540) .. (988,555) -- (962,573) .. controls (979,571) and (996,559) .. (1002,563) .. controls (1018,570) and (977,590) .. (986,600) .. controls (1011,593) and (992,619) .. (978,635);
% BEGIN A025-M02
% long guide/strike: full-scan origin (920,526), local baseline (0,0), base-west zero separation.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (920,526) {\unsure{\begin{tikzpicture}[x=.20pt,y=-.20pt,baseline=(guidebase)]
\path[use as bounding box] (0,0) rectangle (145,101);\coordinate (guidebase) at (0,0);
\draw[line width=.28pt] (5,97) .. controls (-2,78) and (19,48) .. (42,42) .. controls (74,32) and (111,20) .. (141,6) .. controls (144,4) and (140,2) .. (136,3);
\end{tikzpicture}}};
% END A025-M02''',ownership='Complete deleted K, raised inserted K setminus braced i, looped cancellation and locally qualified long guide/strike. et les stays outside.',candidates=[r'\deleted{K}\inserted{K\setminus\{i\}} with long run acting as guide',r'\deleted{K}\inserted{K\setminus\{i\}} with long run acting as strike'],role='Words/state firm; long-run role remains unresolved locally, with source-positioned curved geometry.')
G['s5']=group('A025-S05',(1236,552),(82,61),48,r'''\draw[line width=.48pt] (1244,560) -- (1283,560);
\draw[line width=.40pt] (1245,570) .. controls (1263,572) and (1279,575) .. (1278,581) .. controls (1275,585) and (1251,597) .. (1240,600) -- (1279,601);
\draw[line width=.50pt] (1303,560) -- (1306,572);
\draw[line width=.46pt] (1294,565) -- (1314,564);
\draw[line width=.44pt] (1294,599) .. controls (1285,607) and (1276,608) .. (1274,606) .. controls (1270,602) and (1286,602) .. (1290,603) -- (1301,608);''',semantic=r'\Sigma_\alpha^+',ownership='Prose Sigma alpha plus before parenthetical alpha in K setminus braced i.',candidates=[r'\Sigma_\alpha^+ with head/retrace',r'\Sigma_\alpha^+ with independent upper run'],role='Separate upper run; its head/retrace role remains unresolved at this independent occurrence. No extra index point.')
G['s6']=group('A025-S06',(291,819),(110,76),62,r'''\draw[line width=.41pt] (299,834) -- (357,825);
\draw[line width=.44pt] (310,840) .. controls (336,842) and (359,846) .. (355,855) .. controls (350,863) and (317,879) .. (298,886) .. controls (324,885) and (350,878) .. (368,875) .. controls (374,875) and (372,882) .. (372,884);
\draw[line width=.48pt] (383,826) -- (386,841);
\draw[line width=.47pt] (375,832) -- (396,832);
\draw[line width=.51pt] (372,855) -- (376,858);''',semantic=r'\Sigma_i^+',ownership='Complete positive prose Sigma, one short index and plus; i.e. stays outside.',candidates=[r'\Sigma_i^+ with head/retrace',r'\Sigma_{\prime}^+ with head/retrace',r'\Sigma_i^+ with independent upper run',r'\Sigma_{\prime}^+ with independent upper run'],role='Rising detached head; index i/prime locally retained. Recurring primaries printed after S01; independent-run candidate hand undetermined.')
G['s7']=group('A025-S07',(548,806),(101,69),59,r'''\draw[line width=.46pt] (555,822) -- (597,817);
\draw[line width=.41pt] (556,834) .. controls (574,836) and (589,833) .. (593,842) .. controls (595,847) and (575,856) .. (561,863) .. controls (583,857) and (609,856) .. (615,865);
\draw[line width=.58pt] (621,813) -- (642,814);
\draw[line width=.52pt] (615,851) -- (616,855);''',semantic=r'\Sigma_i^-',ownership='Complete negative prose Sigma and short index/minus; following full stop outside.',candidates=[r'\Sigma_i^- with head/retrace',r'\Sigma_{\prime}^- with head/retrace',r'\Sigma_i^- with independent upper run',r'\Sigma_{\prime}^- with independent upper run'],role='Detached nearly horizontal head; local i/prime alternative remains recorded; recurring primary printed.')
G['s8']=group('A025-S08',(1169,900),(103,65),55,r'''\draw[line width=.45pt] (1176,915) -- (1211,912);
\draw[line width=.43pt] (1178,915) .. controls (1183,921) and (1204,920) .. (1208,925) .. controls (1212,932) and (1184,945) .. (1173,952) -- (1214,952);
\draw[line width=.57pt] (1239,912) -- (1264,909);
\draw[line width=.51pt] (1253,936) .. controls (1249,948) and (1243,952) .. (1233,951) .. controls (1215,946) and (1220,962) .. (1238,956) -- (1265,957);
\draw[line width=.35pt] (1224,952) -- (1235,953);''',semantic=r'\Sigma_\alpha^-',ownership='Final Sigma alpha minus, with no closing brace or endpoint punctuation.',role='Faint joined head/body junction; alpha and minus firm. No correction to index.')
G['points']=group('A025-M03',(1591,1713),(16,18),15,r'''\fill (1600,1717) .. controls (1604,1714) and (1604,1719) .. (1600,1720) -- cycle;
\fill (1595,1724) .. controls (1598,1722) and (1599,1726) .. (1596,1728) -- cycle;''',qualified=True,ownership='Two lower-right detached dark lozenges only; no text or inferred punctuation.',candidates=['Two detached graphical marks with unestablished role, attachment, hand and surface origin'],hand='undetermined hand',role='Shape preserved; no character, writer or mathematical role supplied.')
tex='\\scanpage{25}\n'+G['strike_open']+'Si on a $U_s\\subset\n'+G['s1']+'$, $\\overline{U_s}\n'+G['cap']+G['E']+'\\ne\\varnothing$,\n'+G['etsi']+'alors\n'+G['ona']+'\n\\[\n\\begin{aligned}\nU_s=X\\setminus\\mathop{\n'+G['union']+'}\\limits_{\\alpha\\in K}\n'+G['s2']+'&\\qquad\\text{\n'+G['ou']+'}\\quad i\\in K\\subset I\\\\\n&\\forall\\alpha\\in K\\qquad\n'+G['s3']+'\\in\\pi_0(X\\setminus E_\\alpha)\\ \n'+G['edge']+'\\\\\n&\n'+G['oldU']+'\\ \\text{les }\n'+G['s4']+'\\ \\text{mut\\textsuperscript{t}. disjoints}\n\\end{aligned}\n\\]\nIl faut voir que $\n'+G['K']+'$ et les $\n'+G['s5']+'$ $(\\alpha\\in K\\setminus\\{i\\})$ sont determinés en termes de $i$ et de $\n'+G['s6']+'$ i.e. $\n'+G['s7']+'$. Je dis que\n\\[\nK\\setminus\\{i\\}=\\bigl\\{\\alpha\\in I\\mid E_\\alpha\\subset\n'+G['s8']+'\\]\n% Lower-right detached mark group, full-scan location retained in its source declaration.\n\\figure{\\hfill\n'+G['points']+'}\n% archive sheet number: 24\n'
(B/'reading.tex').write_text(tex)
# Literal source maps are rebuilt only after writing the exact complete source.
maps=[]
for g in groups:
    start=tex.index('% BEGIN '+g['id']+'\n');end=tex.index('% END '+g['id']+'\n',start)+len('% END '+g['id']+'\n')
    g.update(source_file='reading.tex',start_char=start,end_char_exclusive=end,start_utf8_byte=len(tex[:start].encode()),end_utf8_byte_exclusive=len(tex[:end].encode()),start_line=tex.count('\n',0,start)+1,end_line=tex.count('\n',0,end),literal_source=tex[start:end])
    maps.append(g)
for gid,parent,origin,rect,ownership,role in [('A025-M01','A025-S02',[1041,306],[10,15],'Two upper-index traces only. Parent owns whole Sigma and ordinary alpha strokes.','Dark point and gray fleck: attachment, hand, role, surface origin undetermined.'),('A025-M02','A025-G09',[920,526],[145,101],'Long curved guide/strike only; parent owns old/live K and looped cancellation.','Long-run guide/strike role unresolved; main writing his hand.')]:
    start=tex.index('% BEGIN '+gid+'\n');end=tex.index('% END '+gid+'\n',start)+len('% END '+gid+'\n')
    maps.append(dict(id=gid,parent=parent,origin_full_scan=origin,local_baseline=[0,0],drawing_rectangle_local=[0,0,*rect],coordinate_unit_pt=.20,y_direction='down',anchor='base west',inner_sep_pt=0,outer_sep_pt=0,ownership=ownership,role=role,source_file='reading.tex',start_char=start,end_char_exclusive=end,start_utf8_byte=len(tex[:start].encode()),end_utf8_byte_exclusive=len(tex[:end].encode()),start_line=tex.count('\n',0,start)+1,end_line=tex.count('\n',0,end),literal_source=tex[start:end]))
# Exact prose/notation anchors and literal path components, with nested ownership explicit.
text_spans=[]
for aid,needle in [('A025-T01',r'\scanpage{25}'),('A025-T02',r'Si on a $U_s\subset'),('A025-T03',r'\overline{U_s}'),('A025-T04',r'\ne\varnothing$,'),('A025-T05','alors\n'),('A025-T06',r'U_s=X\setminus'),('A025-T07',r'}\limits_{\alpha\in K}'),('A025-T08',r'}\quad i\in K\subset I'),('A025-T09',r'&\forall\alpha\in K\qquad'),('A025-T10',r'\in\pi_0(X\setminus E_\alpha)'),('A025-T11',r'\ \text{les }'),('A025-T12',r'\ \text{mut\textsuperscript{t}. disjoints}'),('A025-T13',r'Il faut voir que $'),('A025-T14',r'$ et les $'),('A025-T15',r'$ $(\alpha\in K\setminus\{i\})$ sont determinés en termes de $i$ et de $'),('A025-T16',r'$ i.e. $'),('A025-T17',r'$. Je dis que'),('A025-T18',r'K\setminus\{i\}=\bigl\{\alpha\in I\mid E_\alpha\subset'),('A025-T19','% archive sheet number: 24')]:
    start=tex.index(needle);end=start+len(needle)
    text_spans.append(dict(id=aid,start_char=start,end_char_exclusive=end,start_utf8_byte=len(tex[:start].encode()),end_utf8_byte_exclusive=len(tex[:end].encode()),literal_source=tex[start:end]))
for g in maps:
    components=[]
    for n,m in enumerate(re.finditer(r'\\(?:draw|fill)(?:\[[^\]]*\])?[^;]*;',g['literal_source']),1):
        start=g['start_char']+m.start();end=g['start_char']+m.end()
        owners=[q for q in maps if q['start_char']<=start and end<=q['end_char_exclusive']]
        owner=min(owners,key=lambda q:q['end_char_exclusive']-q['start_char'])['id']
        components.append(dict(id=g['id']+'-P'+str(n).zfill(2),owned_by=owner,start_char=start,end_char_exclusive=end,start_utf8_byte=len(tex[:start].encode()),end_utf8_byte_exclusive=len(tex[:end].encode()),literal_source=tex[start:end],scope='Literal path command; drawing rectangle is not a computed path bound.'))
    g['path_components']=components
(B/'source_map.json').write_text(json.dumps({'offset_convention':'zero-based Unicode character and UTF-8 byte offsets; end exclusive; line numbers one-based; every literal_source is exactly the complete reader A source span','group_coordinate_convention':'Local coordinates map to full scan by adding origin. Coordinates in group scope are supplied as full-scan coordinates and shifted by minus origin. x=.20pt and y=-.20pt. Nested marks use declared origin, baseline (0,0), base-west anchor and zero separations. Font extents are not geometric path bounds.','groups':maps,'text_spans':text_spans},ensure_ascii=False,indent=2)+'\n')
print('Wrote complete reading.tex and exact source_map.json; groups',len(maps))
