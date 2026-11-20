from pathlib import Path
import json, datetime
R=Path('/workspace/scratch/94548b74fbe0/out/readers/013/A')
S=0.00635
lines=[r'\scanpage{13}',r'% Reader A; one-page independent reading. Coordinates in the figure use the full scan.',r'% No compiler or renderer used; graphical paths are direct approximations of inspected ink.',r'% Upper left marginal cluster; its internal positions follow the original pixels.',r'\margin{\begin{tikzpicture}[x=.00635cm,y=-.00635cm,line cap=round,line join=round]',r'\path[use as bounding box] (24,391) rectangle (145,861);',r'% M01: bar and upward shaft, with separately visible retracing.',r'\draw[line width=.42pt] (32,414)--(65,414);',r'\draw[black!65,line width=.25pt] (48,422)..controls (47,477) and (47,514)..(43,554)..controls (42,597) and (46,631)..(40,664);',r'\draw[line width=.43pt] (35,436)--(47,420)--(63,438) (47,420)--(62,423);',r'\draw[black!35,line width=.18pt] (47,426)--(38,448);',r'% M02: long brace, and pale independently visible parallel continuation.',r'\draw[line width=.31pt] (66,496)..controls (48,487) and (55,553)..(57,591)..controls (60,629) and (54,655)..(44,666)..controls (58,673) and (63,676)..(64,708)..controls (65,755) and (64,805)..(66,829)..controls (67,842) and (70,847)..(74,847);',r'\draw[black!35,line width=.22pt] (48,500)..controls (48,552) and (43,612)..(41,663)..controls (44,678) and (51,678)..(51,705)..controls (52,753) and (53,809)..(54,845);',r'\draw[line width=.18pt] (48,556)..controls (40,565) and (43,586)..(48,604);',r'% M03: question mark and opposed arrows, including the intervening curved stroke.',r'\node[font=\scriptsize] at (87,600) {?};',r'\draw[black!65,line width=.23pt] (120,555)--(119,578)..controls (119,588) and (117,592)..(111,596)..controls (118,600) and (120,610)..(122,638);',r'\draw[line width=.24pt] (114,568)--(119,578)--(124,571) (111,619)--(118,608)--(126,619);',r'\draw[black!32,line width=.17pt] (112,554)--(112,563) (109,559)--(112,563)--(115,559);',r'% M04: detached small grey mark above the bar; role and hand undetermined.',r'\fill[black!40] (47,404) ellipse[x radius=.9,y radius=1.8];',r'\end{tikzpicture}}',r'\figure{\begin{tikzpicture}[x=.00635cm,y=-.00635cm,line cap=round,line join=round]',r'\path[use as bounding box] (20,18) rectangle (2352,1670);',r'% R01--R12: visible horizontal rules; no extrapolated equal spacing.',r'\draw[black!50,line width=.14pt] (28,123)--(800,124)--(1570,127)--(2348,129);',r'\draw[black!50,line width=.14pt] (27,209)--(802,210)--(1572,211)--(2295,212);',r'\draw[black!12,line width=.12pt] (30,286)--(357,288) (1134,287)--(2340,292);',r'\draw[black!48,line width=.14pt] (24,555)--(783,553)--(1575,556)--(2343,562);',r'\draw[black!45,line width=.14pt] (27,638)--(788,640)--(1571,645)--(2346,648);',r'\draw[black!50,line width=.14pt] (26,752)--(790,754)--(1570,756)--(2340,762);',r'\draw[black!45,line width=.14pt] (23,842)--(788,840)--(1570,841)--(2307,847);',r'\draw[black!15,line width=.11pt] (23,932)--(395,934) (792,929)--(1190,931) (1568,928)--(2338,932);',r'\draw[line width=.18pt] (21,1090)--(790,1090)--(1570,1087)--(2348,1094);',r'\draw[black!48,line width=.14pt] (23,1204)--(788,1206)--(1570,1204)--(2342,1209);',r'\draw[black!48,line width=.14pt] (22,1298)--(791,1295)--(1570,1297)--(2341,1306);',r'\draw[black!45,line width=.14pt] (26,1564)--(789,1556)--(1570,1560)--(2340,1575);',r'% V01--V02: pale long vertical traces. Their surface origin and function remain undetermined.',r'\draw[black!12,line width=.12pt] (410,195)..controls (398,620) and (400,1210)..(391,1664);',r'\draw[black!12,line width=.12pt] (1565,23)..controls (1575,561) and (1570,1118)..(1572,1666);']
def node(x,y,w,txt,extra=''):
    opts='anchor=base west,inner sep=0pt,font=\\scriptsize'+(','+extra if extra else '')
    lines.append(r'\node['+opts+'] at ('+str(x)+','+str(y)+') {\\resizebox{'+f'{w*S:.5f}'+r'cm}{!}{'+txt+'}};')
def hidden_deleted(txt):
    return r'\rlap{'+txt+r'}\phantom{\deleted{'+txt+'}}'
def pale_state(txt):
    # The text is legible; a cancellation/live alternative is preserved without drawing an unsupported strike.
    return r'\unsure{\rlap{'+txt+r'}\phantom{\deleted{'+txt+'}}|'+txt+'}'
# All six Notes headings and identifiers, read individually.
for x,y,w,t in [(168,125,105,'Notes'),(547,124,110,'Notes'),(939,126,113,'Notes'),(1315,126,113,'Notes'),(1705,127,100,'Notes'),(2095,127,136,'Notes'),(217,208,25,'1'),(582,209,34,'5'),(978,231,23,'7'),(1343,208,49,'15'),(1737,209,53,'20'),(2140,209,47,'23')]: node(x,y,w,t)
# Cancelled first heading: text preserved, observed diagonal hatching drawn separately.
lines.append('% T01: readable cancelled heading and fourteen paths approximating the merged hatch strokes.')
node(84,293,241,hidden_deleted('A (1976/77)'))
for k,p in enumerate([
'(94,290)--(112,251)','(109,290)--(130,248)','(124,290)--(145,246)','(139,290)--(160,251)',
'(154,291)--(174,254)','(167,293)--(188,250)','(181,296)--(202,247)','(196,297)--(216,246)',
'(210,298)--(230,243)','(224,299)--(242,241)','(239,299)..controls (245,301) and (249,280)..(259,239)',
'(255,302)..controls (262,306) and (270,276)..(276,240)','(274,298)--(293,249)','(290,302)..controls (296,305) and (305,276)..(313,251)'],1):
    lines.append(f'% T01.H{k:02d}')
    lines.append(r'\draw[black!72,line width=.27pt] '+p+';')
# Main A: pale predecessor-like form and dark live form. State remains explicitly qualified.
lines.append('% A01: pale A, its lower position and exterior pale curves; no inferred writing chronology.')
node(187,579,42,pale_state('A'),'text=black!38')
lines += [r'\draw[black!28,line width=.18pt] (178,555)..controls (173,565) and (180,579)..(186,585);',r'\draw[black!28,line width=.18pt] (230,555)..controls (234,567) and (234,578)..(230,585);']
for x,y,w,t in [(181,556,47,'A'),(555,554,27,'B'),(964,548,27,'C'),(1316,552,31,'D'),(1716,553,28,'E'),(2109,558,37,'E')]: node(x,y,w,t)
for x,y,w,t in [(136,645,157,'(1976/77)'),(505,646,165,'(1978/79)'),(904,646,157,'(1979/80)'),(1277,646,118,'(1980)'),(1680,649,122,'(1981)'),(2075,652,112,'(1981)')]: node(x,y,w,t)
lines += [r'% A02: bent arrows and the repeated lower rule.',r'\draw[line width=.31pt] (254,667)--(319,667)--(318,644) (312,650)--(318,644)--(324,653);',r'\draw[line width=.34pt] (255,701)..controls (267,707) and (293,706)..(308,709)--(325,711)--(325,735) (318,728)--(325,736)--(332,731);',r'\draw[line width=.25pt] (254,713)--(277,713)--(306,710)--(317,710);',r'% A03: three residual components near the upper arrow; no assigned character or function.',r'\draw[black!38,line width=.18pt] (257,665)..controls (265,662) and (273,657)..(278,661);',r'\draw[black!63,line width=.21pt] (307,652)--(311,654);',r'\fill[black!58] (304,673) ellipse[x radius=.8,y radius=1.3];']
for x,y,w,t in [(113,751,202,'Découverte'),(166,787,70,'de la')]: node(x,y,w,t)
lines.append('% A04: visible pale residual vertical traces behind the first title; no second word supplied.')
lines += [r'\draw[black!18,line width=.18pt] (141,790)--(149,837) (164,792)--(168,823) (208,789)--(214,829) (243,795)--(248,834) (287,796)--(292,835);']
node(121,839,232,'Méditation')
node(518,752,138,'Réveil')
node(559,791,34,'en')
# The overlapping C-shaped start remains qualified. The old form is placed first in source order.
node(502,839,75,hidden_deleted(r'\unsure{C|Ca}'))
node(547,839,136,'Cascades')
lines.append(r'\draw[line width=.20pt] (497,833)..controls (495,841) and (507,843)..(514,839);')
lines += [r'% B01: detached/interrupting diagonal components adjoining R; their role and hand remain undetermined.',r'\fill (501,694)..controls (505,694) and (509,697)..(509,703)..controls (505,703) and (502,700)..(500,697)--cycle;',r'\draw[black!65,line width=.19pt] (513,706)--(517,710);',r'\draw[black!26,line width=.17pt] (518,711)--(529,721);',r'\fill[black!35] (533,728)--(537,730)--(541,729)--(539,734)--(536,734)--cycle;',r'\draw[black!55,line width=.18pt] (549,739)--(552,742) (554,744)--(558,749);']
for x,y,w,t in [(858,752,214,'Die Eltern'),(855,841,227,'(Les parents)'),(1245,751,202,'Das Kind'),(1238,846,222,"(L'enfant)"),(1617,753,276,'Der Baumeister'),(1619,841,269,'(Le Bâtisseur)'),(2008,759,279,'Le Bâtisseur')]: node(x,y,w,t)
# Crossed subdivisions: preserved candidates and local hatch strokes, not inferred from live row.
cross=[
('A',185,936,43,r'(\unsure{i})', ['(181,925)--(196,894)','(185,929)--(201,904)','(190,933)--(209,905)','(196,931)--(218,909)','(203,933)--(224,917)']),
('B',560,933,58,'(ii)', ['(557,930)--(585,897)','(565,929)--(600,899)','(576,931)--(607,906)','(580,933)--(615,916)']),
('C',950,929,45,r'(\unsure{i|ii})',['(949,921)--(973,898)','(954,922)--(984,903)','(962,925)--(991,911)']),
('D',1319,926,45,'(i)',['(1317,921)--(1336,904)','(1320,921)--(1343,907)','(1325,923)--(1351,911)','(1330,924)--(1362,916)']),
('E20',1722,927,47,r'(\unsure{i|ii})',['(1718,920)--(1735,903)','(1722,919)--(1743,905)','(1728,921)--(1756,906)','(1733,925)--(1766,916)']),
('E23',2131,929,67,r'(\unsure{iv|iii})',['(2128,921)--(2146,905)','(2134,919)--(2159,906)','(2143,922)--(2171,911)','(2153,923)--(2183,913)'])]
for name,x,y,w,t,paths in cross:
    lines.append('% X'+name+': local cancellation group.')
    node(x,y,w,hidden_deleted(t))
    for j,p in enumerate(paths,1):
        lines.append('% X'+name+'.H'+str(j))
        lines.append(r'\draw[line width=.30pt] '+p+';')
# Lower arrow/question and the B diagonal arrow.
node(122,977,16,'?','text=black!35')
lines += [r'% L01: lower first-column arrow, including its small upper hooked entry.',r'\draw[black!25,line width=.18pt] (176,921)..controls (160,910) and (158,918)..(159,936)--(157,1001) (149,992)--(157,1001)--(165,992);',r'% L02: faint diagonal arrow before the second live subdivision.',r'\draw[black!34,line width=.18pt] (523,1000)..controls (526,1027) and (529,1042)..(536,1052) (530,1048)--(536,1052)--(538,1047);']
# Pale former-looking lower forms before the dark row. The visible state is qualified locally.
node(168,1121,40,pale_state('(i)'),'text=black!25')
node(945,1080,39,pale_state(r'\unsure{(i)|(}'),'text=black!32')
node(1321,1071,45,pale_state('(i)'),'text=black!45')
for x,y,w,t in [(167,1092,37,'(i)'),(555,1088,53,'(ii)'),(944,1088,44,'(i)'),(1329,1089,42,'(i)'),(1722,1088,47,'(i)'),(2107,1091,75,'(iv)')]: node(x,y,w,t)
# Secondary titles and translations, each individually read.
for x,y,w,t in [(125,1204,119,'Envol'),(439,1206,308,'Vers un plus long Voyage'),(857,1205,299,'Bild und Wahrheit'),(820,1299,307,'(Image et Réalité)'),(1227,1205,230,'Der Wolf'),(1238,1298,225,'(Le Loup)'),(1616,1205,318,'Spiel- und Sucht'),(1590,1300,353,'(Jeu - et Fringale)'),(2029,1207,249,"Le ``Maître''")]: node(x,y,w,t)
# Detached mark below 'long'.
lines += [r'% G01: detached short dash below the left end of the g descender in long.',r'\fill (590,1240)..controls (592,1237) and (595,1238)..(596,1239)..controls (594,1242) and (591,1243)..(590,1240)--cycle;',r'% G02: interrupted short trace above the first foot; hand and surface origin undetermined.',r'\draw[black!60,line width=.19pt] (234,1409)--(233,1415);',r'\fill[black!75] (232,1420) ellipse[x radius=1.2,y radius=1.3];',r'\draw[black!28,line width=.18pt] (232,1427)--(230,1430) (229,1435)--(230,1438);',r'% G03: interrupted pale stroke below the first foot; hand and surface origin undetermined.',r'\fill[black!25] (340,1583) ellipse[x radius=1.6,y radius=1.2];',r'\fill[black!55] (338,1589) ellipse[x radius=1.2,y radius=1.1];',r'\draw[black!65,line width=.18pt] (337,1593)--(336,1596);',r'\draw[black!30,line width=.23pt] (335,1599)..controls (337,1605) and (336,1608)..(332,1609);',r'% G04--G07: separate lower-right dot, dash and local darkenings on rules.',r'\fill[black!35] (1933,1359)..controls (1939,1359) and (1939,1364)..(1934,1366)--(1931,1363)--cycle;',r'\draw[black!53,line width=.20pt] (2252,1343)--(2268,1344);',r'\fill (2221,1304)..controls (2226,1300) and (2231,1302)..(2235,1305)--cycle;',r'\fill (2308,1090)..controls (2314,1088) and (2319,1090)..(2321,1092)--(2311,1093)--cycle;']
for x,y,w,t in [(115,1560,173,r'M 1976 $\mathord{*}$'),(488,1560,171,'M 1979'),(860,1557,175,r'HS $\mathrm I$'),(1230,1557,166,r'Sch $\mathrm I$'),(1648,1563,192,r'Sch $\overline{\underline{\mathrm{VI}}}$'),(2047,1571,199,r'Sch $\overline{\underline{\mathrm{IX}}}$')]: node(x,y,w,t)
# The ten right-edge groups map one-for-one to C's ten original path entries.
edge=[
('E01','(2336,116)--(2349,129) (2334,128)--(2349,129)',100),
('E02','(2339,201)--(2349,208) (2332,206)..controls (2339,210) and (2344,207)..(2349,208)',100),
('E03','(2330,366)--(2348,375) (2330,373)--(2348,375)',100),
('E04','(2329,418)--(2349,426) (2329,427)..controls (2338,430) and (2344,427)..(2349,427)',100),
('E05','(2328,552)--(2342,562)--(2343,565) (2325,562)--(2339,562)',100),
('E06','(2331,639)--(2347,648) (2336,650)--(2347,648)',100),
('E07','(2338,965)--(2346,975) (2335,977)--(2345,977)--(2348,973)',45),
('E08','(2330,1081)--(2341,1092)',85),
('E09','(2335,1198)--(2343,1207)',90),
('E10','(2330,1564)--(2336,1570)--(2336,1575)',100)]
for eid,p,shade in edge:
    lines.append('% '+eid+': surviving local edge path.')
    lines.append(r'\draw[black!'+str(shade)+r',line width=.28pt] '+p+';')
lines += [r'\end{tikzpicture}}',r'% archive sheet number: 12',r'% The archive numeral is pencilled sideways at the lower right; comment-only by convention.',r'% crop-candidate: scan 13']
(R/'reading.tex').write_text('\n'.join(lines)+'\n')
# Mark the actual crop delivery order. All 24 returned images were viewed once.
crops=json.loads((R/'crops.json').read_text())
for i,c in enumerate(crops,1): c['viewed']=True; c['view_order_after_halves']=i; c['successful_view_count']=1
(R/'crops.json').write_text(json.dumps(crops,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex and synchronized 24 viewed crop records.')
