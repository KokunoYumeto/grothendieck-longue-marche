from pathlib import Path
import json
R=Path('/workspace/scratch/94548b74fbe0/out/readers/013/C')
P=Path('/workspace/scratch/94548b74fbe0/packets/013')
manifest=json.loads((R/'crops_manifest.json').read_text())
for i,c in enumerate(manifest,1):
 c['viewed']=True; c['view_order']=i
manifest[9]['display_note']='The first display call aborted before dispatch; the same existing file was then successfully displayed once. No duplicate crop was made.'
(R/'crops_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
M={c['path'].split('_')[0]:c for c in manifest}
tex=[r'\scanpage{13}',r'% Six-column ruled list. All coordinates below follow this sheet only.',r'% archive sheet number: 12',r'% The archive number is sideways at the lower right and is recorded only in this comment.',r'\figure{\resizebox{\linewidth}{!}{%',r'\begin{tikzpicture}[x=1pt,y=-1pt,line cap=round,line join=round]',r'\path[use as bounding box] (20,65) rectangle (2353,1666);',r'% Table ruling; pale broken/interrupted runs are retained as graphical approximations.',r'\begin{scope}[draw=black!38,line width=1pt]',r'\draw (28,124)--(747,125)--(1520,125)--(2349,130);',r'\draw (27,210)--(747,210)--(1530,210)--(2287,212);',r'\draw[draw=black!12] (28,285)--(2347,293);',r'\draw (22,554)--(402,553)--(1146,554)--(1925,556)--(2343,562);',r'\draw (24,640)--(405,638) (407,638)--(1569,643)--(2346,647);',r'\draw (24,753)--(777,752)--(1559,755)--(2343,762);',r'\draw (24,842)--(787,841)--(1573,840)--(2345,846);',r'\draw[draw=black!17] (23,932)--(333,931);',r'\draw[draw=black!70,line width=1.4pt] (20,1089)--(398,1091)--(1171,1088)--(1960,1088)--(2347,1094);',r'\draw (24,1205)--(788,1204)--(1568,1201)--(2342,1207);',r'\draw (22,1298)--(786,1296)--(1570,1295)--(2344,1304);',r'\draw (24,1565)--(799,1557)--(1578,1559)--(2341,1574);',r'\draw[draw=black!12] (406,213)--(400,1664) (797,213)--(800,1664) (1190,214)--(1192,1658) (1568,214)--(1576,1665) (1963,216)--(1968,1664);',r'\end{scope}']
def node(x,y,w,s,label,math=False,color=None):
 tex.append('% '+label)
 if math:s=r'\('+s+r'\)'
 if color:s=r'{\color{'+color+'}'+s+'}'
 tex.append(r'\node[anchor=south west,inner sep=0pt] at ('+str(x)+','+str(y)+r') {\resizebox{'+str(w)+r'pt}{!}{'+s+r'}};')
def shape(identifier,x,y,body,purpose):
 tex.append('% '+identifier+': '+purpose+'; role/hand/surface origin unresolved.')
 tex.append(r'\node[anchor=north west,inner sep=0pt,font=\fontsize{14}{14}\selectfont] at ('+str(x)+','+str(y)+r') {\unsure{\begin{tikzpicture}[x=1pt,y=-1pt,line cap=round,line join=round]')
 tex.extend(body)
 tex.append(r'\end{tikzpicture}}};')
# Faint residual strokes are drawn before the overlying title text.
shape('G02',140,765,[r'\draw[draw=black!22,line width=1.4pt] (3,1)..controls(2,17)and(4,30)..(7,43) (23,21)..controls(28,29)and(27,43)..(30,55) (67,15)..controls(67,35)and(74,48)..(75,66) (99,35)..controls(103,47)and(101,63)..(103,73);'],'four pale residual stroke runs behind the first title, no recovered letters')
for x,w in [(170,102),(548,112),(936,120),(1314,112),(1703,108),(2095,136)]:node(x,130,w,'Notes','heading Notes')
for x,w,n in [(217,25,'1'),(578,38,'5'),(973,29,'7'),(1340,52,'15'),(1735,54,'20'),(2139,56,'23')]:node(x,211,w,n,'heading number '+n)
node(83,301,240,r'\deleted{A (1976/77)}','cancelled early A/date entry')
node(178,579,66,r'\deleted{\unsure{\mathrm A}}\mathrm A','C doubt row 1: pale overwritten A candidate followed by the dark A',True)
for x,y,w,l in [(554,559,29,'B'),(966,553,30,'C'),(1316,556,34,'D'),(1715,557,31,'E'),(2110,559,37,'E')]:node(x,y,w,r'\mathrm '+l,'large heading '+l,True)
for x,w,d in [(133,158,'(1976/77)'),(504,166,'(1978/79)'),(904,160,'(1979/80)'),(1275,125,'(1980)'),(1680,126,'(1981)'),(2074,114,'(1981)')]:node(x,652,w,d,'date '+d)
# Left marginal connected graphic; the observed placement is part of this page figure.
tex += [r'% G15: left marginal brace, upward arrow, retracings, question and opposed arrows.',r'\begin{scope}[line width=2.3pt]',r'\draw (33,414)--(65,414);',r'\draw (34,438)--(48,419)--(63,438) (48,420)..controls(48,490)and(46,557)..(43,625)..controls(42,647)and(39,663)..(42,669);',r'\draw (48,419)--(62,423);',r'\draw (65,494)..controls(54,500)and(54,532)..(55,577)..controls(56,618)and(55,657)..(42,668)..controls(56,674)and(62,681)..(63,718)..controls(68,782)and(62,836)..(73,847);',r'\draw (52,555)..controls(45,564)and(47,590)..(56,609);',r'\draw[draw=black!35,line width=1.5pt] (39,447)--(47,432) (47,433)..controls(51,491)and(44,542)..(39,586)..controls(38,627)and(39,655)..(39,667);',r'\draw[draw=black!35,line width=1.5pt] (39,672)..controls(52,681)and(47,738)..(51,790)..controls(53,817)and(50,838)..(55,846);',r'\draw (120,554)..controls(120,569)and(123,581)..(117,594)..controls(115,598)and(111,599)..(110,600);',r'\draw (113,568)--(121,579)--(126,570);',r'\draw (110,600)..controls(119,602)and(121,613)..(121,628)..controls(121,634)and(122,636)..(125,640);',r'\draw (113,621)--(120,611)--(128,619);',r'\end{scope}']
node(78,624,20,'?','upper marginal question mark')
shape('G15a',45,402,[r'\fill[black!35] (2,0) ellipse (1.2pt and 2.7pt);'],'detached pale point above the top arrow bar')
# Two bent arrows, including the repeated lower horizontal run.
tex += [r'% G16: bent arrows and separate local components.',r'\draw[line width=2.4pt] (254,667)--(318,668)--(318,643) (312,648)--(318,642)--(325,652);',r'\draw[line width=2.4pt] (257,702)..controls(267,707)and(287,708)..(305,708)--(326,710)--(326,738) (319,730)--(327,739)--(334,733);',r'\draw[line width=1.5pt] (254,713)..controls(271,713)and(291,712)..(305,709);']
shape('G16b',260,658,[r'\draw[black!35,line width=1.4pt] (0,7)..controls(7,3)and(11,-1)..(17,4);'],'short pale arch above the left of the upper arrow')
shape('G16c',307,651,[r'\draw[black!80,line width=2pt] (0,1)--(5,3);'],'detached oblique stroke to the left of the upward head')
shape('G16d',302,671,[r'\fill[black!50] (1,1) ellipse (1.1pt and 1.5pt);'],'small detached point below upper horizontal shaft')
node(111,755,209,'Découverte','first title line 1, acute accent retained')
node(162,789,77,'de la','first title line 2')
node(119,844,235,'Méditation','C doubt row 2 resolved singular ending')
node(502,756,155,'Réveil','second main title line 1')
node(557,794,37,'en','second main title line 2')
node(495,844,187,r'\deleted{\unsure{C|Ca}}Cascades','C doubt row 3: predecessor retained')
for x,y,w,t in [(856,756,218,'Die Eltern'),(855,853,229,'(Les parents)'),(1241,759,214,'Das Kind'),(1233,858,231,"(L'enfant)"),(1612,760,282,'Der Baumeister'),(1613,851,277,'(Le Bâtisseur)'),(2002,763,285,'Le Bâtisseur')]:node(x,y,w,t,'main-title cell')
# Cancelled subdivisions: qualifications refer only to surviving predecessor ink.
for x,w,s,ref in [(182,51,r'(\unsure{\mathrm i})','4'),(556,64,r'(\mathrm{ii})','5'),(946,64,r'(\unsure{\mathrm i|\mathrm{ii}})','6'),(1317,49,r'(\mathrm i)','7'),(1715,66,r'(\unsure{\mathrm i|\mathrm{ii}})','8'),(2125,83,r'(\unsure{\mathrm{iv}|\mathrm{iii}})','9')]:node(x,939,w,r'\deleted{'+s+'}','crossed subdivision; C doubt row '+ref,True)
# Pale questions/arrows between the two subdivision levels.
node(122,980,17,'?','C doubt row 10 resolved')
tex += [r'% G10: pale curved-top downward arrow beside the lower question mark.',r'\draw[draw=black!40,line width=1.6pt] (174,920)..controls(162,913)and(157,922)..(158,942)..controls(160,963)and(158,988)..(159,1000) (148,991)--(159,1001)--(167,991);',r'% G30: pale descending arrow before the second live subdivision.',r'\draw[draw=black!25,line width=1.4pt] (526,984)..controls(526,1008)and(526,1023)..(533,1042)--(538,1051);',r'\draw[draw=black!60,line width=1.4pt] (529,1047)..controls(533,1051)and(536,1050)..(538,1050)--(542,1055);']
# Overwritten/displaced labels occur immediately before their live replacements in source order.
node(166,1126,78,r'\unsure{\deleted{(\mathrm i)}|(\mathrm i)}','C doubt row 13a: pale lower (i), glyph and state both qualified',True,'black!40')
node(167,1096,39,r'(\mathrm i)','first live subdivision',True)
node(554,1094,55,r'(\mathrm{ii})','second live subdivision',True)
node(939,1087,36,r'\unsure{\deleted{(}|(}','C doubt row 13b: extra opening curve, state qualified',True,'black!45')
node(947,1092,44,r'(\mathrm i)','third live subdivision',True)
node(1317,1073,111,r'\unsure{\deleted{(\mathrm i)}|(\mathrm i)}','C doubt row 11: upper displaced (i), recovered glyph and qualified state',True,'black!55')
node(1329,1092,42,r'(\mathrm i)','fourth live subdivision',True)
node(1722,1091,48,r'(\mathrm i)','fifth live subdivision',True)
node(2106,1095,79,r'(\mathrm{iv})','sixth live subdivision',True)
for x,y,w,t in [(122,1210,128,'Envol'),(438,1213,312,'Vers un plus long Voyage'),(852,1207,304,'Bild und Wahrheit'),(818,1322,312,'(Image et Réalité)'),(1224,1216,244,'Der Wolf'),(1235,1320,234,'(Le Loup)'),(1613,1221,324,'Spiel- und Sucht'),(1588,1326,358,'(Jeu - et Fringale)'),(2028,1213,254,"Le ``Maître''")]:node(x,y,w,t,'lower title')
for x,y,w,t in [(111,1580,180,r'M 1976\(\mathord{*}\)'),(484,1580,172,'M 1979'),(858,1562,181,r'HS \(\mathrm I\)'),(1228,1568,173,r'Sch \(\mathrm I\)'),(1642,1573,204,r'Sch \(\overline{\underline{\mathrm{VI}}}\)'),(2040,1580,210,r'Sch \(\overline{\underline{\mathrm{IX}}}\)')]:node(x,y,w,t,'foot reference')
# Ten right-edge components, checked individually against their crops.
tex += [r'% Gedge1--Gedge10: surviving short right-edge pieces; no unseen continuation supplied.',r'\draw[line width=2.2pt] (2337,116)--(2350,129)--(2336,128);',r'\draw[line width=2.2pt] (2341,201)--(2347,207)..controls(2341,208)and(2336,210)..(2332,205);',r'\draw[line width=2.2pt] (2330,364)--(2348,375)--(2331,374);',r'\draw[line width=2.2pt] (2329,419)--(2348,426)..controls(2341,430)and(2334,428)..(2330,428);',r'\draw[line width=2.2pt] (2329,552)--(2341,562)--(2327,562) (2341,562)--(2343,565);',r'\draw[line width=2.2pt] (2331,639)--(2346,648)--(2335,650);',r'\draw[draw=black!55,line width=2.2pt] (2338,965)--(2346,976)..controls(2342,980)and(2339,976)..(2335,979);',r'\draw[line width=2.2pt] (2330,1083)--(2340,1093);',r'\draw[line width=2.2pt] (2335,1198)--(2341,1205);',r'\draw[line width=2.2pt] (2330,1564)--(2336,1570)..controls(2338,1572)and(2337,1574)..(2337,1576);']
# Other visually supported detached shapes, with no supplied character value.
shape('G12',590,1237,[r'\fill[black] (2,3) ellipse (2.3pt and 1.3pt);'],'detached dark dot beneath the left end of the g descender in long')
shape('G23',227,1405,[r'\draw[draw=black!65,line width=2pt] (8,3)--(7,7)--(6,10);',r'\fill[black!75] (5,15) ellipse (1.5pt and 1.4pt);',r'\draw[draw=black!25,line width=1.4pt] (5,20)--(3,23) (4,25)--(1,27) (3,30)--(0,32) (2,34)--(0,35);'],'dark upper fragments with intermittent pale continuation in first lower blank cell')
shape('G24',332,1581,[r'\draw[draw=black!25,line width=1.5pt] (8,0)--(7,3) (6,5)--(5,7);',r'\fill[black!70] (4,13) ellipse (1.1pt and 1.5pt);',r'\draw[draw=black!35,line width=1.4pt] (3,17)--(3,19) (3,22)--(2,24) (2,26)--(0,27);'],'interrupted slanted vertical trace below M 1976')
shape('G25',369,1015,[r'\draw[draw=black!20,line width=1.3pt] (0,1)--(7,8);',r'\draw[draw=black!55,line width=2pt] (7,8)--(8,12);',r'\fill[black!65] (11,15) ellipse (1.6pt and 1.1pt);',r'\draw[draw=black!30,line width=1.6pt] (12,18)--(15,20) (16,21)--(20,24);',r'\fill[black!25] (12,4) circle (1.6pt);',r'\fill[black!20] (16,5) circle (1.1pt);'],'small oblique interrupted cluster to the right of the first pale arrow')
shape('G26',405,617,[r'\draw[draw=black!40,line width=1.4pt] (7,1)..controls(8,8)and(6,13)..(3,17);',r'\draw[draw=black!20,line width=1pt] (3,17)--(3,21);'],'curved short upright at the first/second date boundary')
shape('G27',1930,1358,[r'\fill[black!45] (1,1)--(5,0)--(8,3)--(6,7)--(2,6)--cycle;',r'\draw[draw=black!25,line width=1.3pt] (3,6)--(0,8);'],'small irregular spot beneath Fringale')
shape('G28a',1792,701,[r'\fill[black!40] (1,1) ellipse (1.4pt and 1.6pt);'],'pale upper point above Baumeister')
shape('G28b',1854,699,[r'\fill[black!90] (1,6)..controls(0,4)and(3,1)..(5,1)..controls(8,1)and(7,4)..(6,6)--cycle;',r'\draw[draw=black!25,line width=1pt] (6,1)--(9,0);'],'dark upper point with short pale tip above Baumeister')
shape('G28c',1690,731,[r'\fill[black!35] (2,2) ellipse (1.2pt and 1.6pt);'],'small pale point immediately left of the Baumeister B stem')
shape('G29',240,751,[r'\fill[black!40] (1,2) ellipse (1.3pt and 1.8pt);'],'small detached pale point beneath Découverte')
shape('GhalfB',2249,1342,[r'\draw[draw=black!55,line width=1.3pt] (0,1)--(18,1.4);'],'isolated horizontal stroke below last title, settled on half b')
tex += [r'\end{tikzpicture}}}',r'% crop-candidate: scan 13']
(R/'reading.tex').write_text('\n'.join(tex)+'\n')
# Structured report.
diffs=[]
def add(id,loc,C,read,evidence,conf,kind='other',changed=False,status=None,crop=None,bbox=None,row=None,sublocus=None,components=None):
 d=dict(id=id,location=loc,C=C,H=None,reading=read,evidence=evidence,confidence=conf,kind=kind,diff_C=changed,diff_H=False,C_doubt_status=status,readers_crop=M[crop]['path'] if crop else None,bbox={'image':'original full scan','origin':'upper left','xyxy':bbox or (M[crop]['bbox'] if crop else [])},mathematical_consequence=None)
 if row:d['source_doubt_row']=row
 if sublocus:d['local_sublocus']=sublocus
 if components:d['components']=components
 diffs.append(d)
add('C013.d01','First heading A, pale offset predecessor',r'\deleted{\unsure{\mathrm A}}\mathrm A',r'\deleted{\unsure{\mathrm A}}\mathrm A','Pale lowered angled feet and a cross-run remain under the dark A; the upper predecessor is masked. A remains a supported candidate, with no further recovered glyph.','low',status='retained',crop='c01',row=1)
add('C013.d02','First main title, final word',r'\unsure{Méditation|Méditations}','Méditation','The ending finishes with the arch and downstroke of n and its short exit. No further s-shaped turn is visible. The acute over é is present.','high',changed=True,status='resolved',crop='c02',row=2)
add('C013.d03','Second main title, overlapping beginning of Cascades',r'\deleted{\unsure{C|Ca}}Cascades',r'\deleted{\unsure{C|Ca}}Cascades','Two large open C-curves overlap with the following low bowl. The overdrawn baseline does not establish whether the predecessor included the following a.','low',status='retained',crop='c03',row=3)
add('C013.d04','A crossed subdivision',r'\deleted{(\unsure{\mathrm i})}',r'\deleted{(\unsure{\mathrm i})}','The two parentheses and a low central hooked upright survive between diagonal cancellation strokes. The dot/internal extent remains covered. No recovery is based on the live label below.','low',status='retained',crop='c04',row=4)
add('C013.d05','B crossed subdivision',r'\deleted{(\unsure{\mathrm{ii}|\mathrm i})}',r'\deleted{(\mathrm{ii})}','Two separated lower upright-and-foot forms survive inside the parentheses; a free upper dot is visible over the right one and the left upper mark meets a crossing stroke. The pair is read from this predecessor itself.','medium',changed=True,status='resolved',crop='c05',row=5)
add('C013.d06','C crossed subdivision',r'\deleted{(\unsure{\mathrm i|\mathrm{ii}})}',r'\deleted{(\unsure{\mathrm i|\mathrm{ii}})}','One central downstroke with a hooked foot is visible; nearby dark continuations coincide with the diagonal hatch and can still hide another i.','low',status='retained',crop='c06',row=6)
add('C013.d07','D crossed subdivision',r'\deleted{(\unsure{\mathrm i})}',r'\deleted{(\mathrm i)}','A detached round dot survives over one short central upright and its low rightward foot, between the parentheses; the crossing diagonals pass alongside the upper dot.','medium',changed=True,status='resolved',crop='c07',row=7)
add('C013.d08','E Notes20 crossed subdivision',r'\deleted{(\unsure{\mathrm i|\mathrm{ii}})}',r'\deleted{(\unsure{\mathrm i|\mathrm{ii}})}','A short central upright and its lower turn survive; the left internal area is crossed and the second-stem possibility cannot be settled from this crop.','low',status='retained',crop='c08',row=8)
add('C013.d09','E Notes23 crossed subdivision',r'\deleted{(\unsure{\mathrm{iv}|\mathrm{iii}})}',r'\deleted{(\unsure{\mathrm{iv}|\mathrm{iii}})}','One left upright survives and the right internal stroke forms a rounded low turn; intersecting long cancellation strokes still mask the internal junction needed to settle v/ii.','low',status='retained',crop='c09',row=9)
add('C013.d10','Pale question beside the first downward arrow',r'\unsure{?}','?','The enlarged mark has a distinct upper left hook curving downward, an interrupted lower shaft, and a detached dark point beneath it.','high',changed=True,status='resolved',crop='c10',row=10)
add('C013.d11','D live-subdivision cluster, displaced upper label',r'\deleted{\unsure{(\mathrm i)}}(\mathrm i)',r'\unsure{\deleted{(\mathrm i)}|(\mathrm i)}\quad (\mathrm i)','Two parenthesized labels are visible at separate vertical levels. The upper one has its own dot and short central upright; its glyph is recovered as (i). No separate cancelling stroke crosses that upper label, so deleted/live alternatives are now explicit. Its position is above the lower dark label.','medium',kind='deletion state (struck given live or live given struck)',changed=True,status='resolved',crop='c11',row=11,components=[{'component':'upper displaced glyph','reading':'(i)','confidence':'high'},{'component':'upper label state','reading':'overwritten/deleted or live displaced writing','confidence':'low'},{'component':'vertical relation','reading':'upper group above lower dark (i)','confidence':'high'}])
add('C013.d12','B lower title, word before long',r'\unsure{plus}','plus','The word has a descending p loop, a tall narrow l, a joined low u and a final compact s; all are visible independently of the adjacent long.','high',changed=True,status='resolved',crop='c12',row=12)
add('C013.d13a','Pale label below first live subdivision',r'\deleted{\unsure{(\mathrm i)}}',r'\unsure{\deleted{(\mathrm i)}|(\mathrm i)}','Pale left/right parentheses and a short inner downstroke with a foot remain below the dark label. The dot is not securely separable. The original (i) glyph doubt is retained; its state is separately qualified in C013.d15.','low',status='retained',crop='c13',row=13,sublocus='13a: beneath first live subdivision')
add('C013.d13b','Third live subdivision, extra opening curve',r'\deleted{\unsure{(}}',r'\unsure{\deleted{(}|(}','A complete pale opening curve is separately visible just left of the dark opening parenthesis. The opening-parenthesis glyph is recovered. Its overwritten/deleted status versus a live/retraced curve remains unresolved and is explicit in the reading.','medium',kind='deletion state (struck given live or live given struck)',changed=True,status='resolved',crop='c14',row=13,sublocus='13b: third live subdivision')
add('C013.d15','Pale label below first live subdivision: state qualification',r'\deleted{\unsure{(\mathrm i)}}',r'\unsure{\deleted{(\mathrm i)}|(\mathrm i)}','The lower pale group is displaced below the dark group and shows no distinct through-stroke. A deleted/overwritten reading is retained as first candidate, and live displaced writing is now also preserved. The glyph doubt is the same source locus as C013.d13a.','low',kind='deletion state (struck given live or live given struck)',changed=True,crop='c13',components=[{'component':'glyph','source_doubt_row':13,'local_sublocus':'13a','cross_reference':'C013.d13a'},{'component':'state','reading':'deleted/overwritten | live displaced writing','confidence':'low'}])
add('C013.g15','Left margin from arrow bar through lower brace',r'\bar{\uparrow}\ \Bigg\{\quad ?\,\begin{smallmatrix}\downarrow\\[-.5ex]\uparrow\end{smallmatrix}','G15 connected paths and G15a detached point','The long upward shaft shares the upper brace area; a small interior loop and pale parallel retracings remain. The opposed arrows have a curved middle join. A small pale point stands above the top bar. These local paths and relative placements are drawn explicitly.','high',kind='drawing or diagram',changed=True,crop='c15',components=[{'component':'long arrow and brace','tex':'G15','confidence':'high'},{'component':'interior loop and pale parallel runs','tex':'G15','confidence':'medium'},{'component':'opposed arrow middle join','tex':'G15','confidence':'high'},{'component':'detached point','tex':'G15a','bbox':[45,402,51,409],'confidence':'medium','role_hand_origin':'unresolved'}])
add('C013.g16','Two bent arrows between first date and title',r'\begin{smallmatrix}\rule[.15ex]{1.4em}{.35pt}\hspace{-.4em}\uparrow\\[-.5ex]\rule[.15ex]{1.4em}{.35pt}\hspace{-.4em}\downarrow\end{smallmatrix}','G16 two bent arrows, repeated lower rule, and G16b/G16c/G16d detached components','The lower arrow has two distinct nearly horizontal runs that converge toward its bend. Above the left part of the upper rule is a pale short arch. A separate short oblique mark lies left of its upward head, and a small point lies below its horizontal shaft.','high',kind='drawing or diagram',changed=True,crop='c16',components=[{'component':'lower repeated rule','tex':'G16','bbox':[253,701,328,716],'confidence':'high'},{'component':'pale arch','tex':'G16b','bbox':[259,658,279,667],'confidence':'medium'},{'component':'short oblique mark','tex':'G16c','bbox':[306,651,314,656],'confidence':'high'},{'component':'small point','tex':'G16d','bbox':[302,671,306,676],'confidence':'medium'}])
add('C013.g02','Behind the first main title',None,'G02 pale graphical residual strokes, no letter supplied','Several pale near-vertical runs continue above and behind the darker title. Their shapes are retained without assigning predecessor words, hand, or surface origin.','low',kind='omission',changed=True,crop='c02',components=[{'component':'left run','bbox':[141,766,148,809],'confidence':'medium'},{'component':'second run','bbox':[163,786,171,820],'confidence':'low'},{'component':'third run','bbox':[207,780,216,832],'confidence':'low'},{'component':'fourth run','bbox':[239,800,245,840],'confidence':'low'}])
add('C013.g12','B lower title, beneath long',None,'G12 detached dark dot','The point lies separately just below and left of the end of the g descender in long. It has a compact dark oval shape; no punctuation role is assigned.','high',kind='omission',changed=True,crop='c12',bbox=[589,1236,597,1245])
add('C013.edge5','Right edge beside the large final E',r'(.30,.318)--(.95,.324)--(.12,.324)','Gedge5 includes the short downturned terminal','The diagonal meets the short horizontal run and continues a little downward at their right junction; that turn remains inside the sheet edge. C gives only the two straight arms.','high',kind='drawing or diagram',changed=True,crop='c19',bbox=[2325,548,2347,568])
add('C013.edge10','Right edge beside final foot reference',r'(.38,.976)--(.77,.982)','Gedge10 short diagonal with a thicker downward end','The short slant bends into a nearly vertical dark terminal before the paper edge. C gives a single straight segment.','high',kind='drawing or diagram',changed=True,crop='c22',bbox=[2327,1561,2342,1580])
for id,loc,crop,read,evidence,confidence,bbox in [
 ('C013.g23','Blank lower first column','c23','G23 interrupted narrow mark','A dark upper fragment and lower dark point are followed by separated pale short pieces along a slant. No character is recovered.','medium',[227,1405,239,1441]),
 ('C013.g24','Below the first foot reference','c24','G24 interrupted slanted vertical trace','Several short pale pieces and one darker point lie along a narrow descending-left line. No character or function is assigned.','medium',[331,1581,342,1610]),
 ('C013.g25','Between first pale arrow and first vertical column boundary','c25','G25 oblique interrupted cluster','A short descending-right sequence of pale and dark fragments remains with two small upper spots. Its surface origin and hand are unsettled.','low',[368,1014,391,1041]),
 ('C013.g26','At first/second date boundary','c26','G26 curved upright with pale continuation to rule','A light curved upright ends toward the horizontal rule. It is retained as a path without a numeral or punctuation value.','medium',[404,616,416,642]),
 ('C013.g27','Beneath Fringale','c27','G27 small irregular spot','A compact irregular grey/dark spot has a tiny pale lower-left turn. No textual role is established.','medium',[1928,1356,1941,1369]),
 ('C013.g29','Immediately beneath Découverte','c29','G29 small pale point','A small compact grey point is separate below the word near its v/e region. It is not attached to a recovered letter stroke.','medium',[239,750,245,758])]:
 add(id,loc,None,read,evidence,confidence,kind='omission',changed=True,crop=crop,bbox=bbox)
for id,loc,read,evidence,confidence,bbox in [
 ('C013.g28a','Above Baumeister, left upper point','G28a pale point','A small detached grey point is visible well above the body of the word. Its attachment and origin remain unsettled.','medium',[1791,700,1797,706]),
 ('C013.g28b','Above Baumeister, right upper point','G28b dark point and pale short tip','The compact dark oblique spot has a small pale upper-right extension. Both are separately positioned above the final part of the word; no diacritic role is assigned.','high',[1853,698,1865,707]),
 ('C013.g28c','Immediately left of the B in Baumeister','G28c small pale point','A small grey oval is visible just left of the B stem. Its role and hand remain unresolved.','medium',[1689,730,1695,737])]:
 add(id,loc,None,read,evidence,confidence,kind='omission',changed=True,crop='c28',bbox=bbox)
add('C013.gHalfB','Blank last column beneath lower title',None,'GhalfB isolated short horizontal stroke','The supplied half b shows a separate thin horizontal dash below the title area; no word or role is attached to it. Its shape was settled on half b, so no crop was made.','high',kind='omission',changed=True,bbox=[2248,1338,2275,1350])
# Doubts include all retained source loci and all new local state/shape qualifications.
doubts=[]
for did,loc,read,alts,reason,crop,row,sub in [
 ('C013.d01','Pale predecessor beneath first A',r'\mathrm A',[], 'Upper glyph masked by dark A; lower feet and cross-run alone survive.','c01',1,None),
 ('C013.d03','Predecessor at Cascades','C',['Ca'],'Low bowl is merged with replacement strokes.','c03',3,None),
 ('C013.d04','A crossed subdivision','(i)',[],'Internal dot/extent masked by diagonal hatch.','c04',4,None),
 ('C013.d06','C crossed subdivision','(i)',['(ii)'],'Second internal upright cannot be separated from the cancellation.','c06',6,None),
 ('C013.d08','E Notes20 crossed subdivision','(i)',['(ii)'],'Crossed internal area leaves one-versus-two uprights open.','c08',8,None),
 ('C013.d09','E Notes23 crossed subdivision','(iv)',['(iii)'],'Internal junctions are masked.','c09',9,None),
 ('C013.d11','D displaced upper subdivision','deleted/overwritten (i)',['live displaced (i)'],'Glyph is readable; no separate cancelling through-stroke settles its state.','c11',11,None),
 ('C013.d13a','Pale lower first subdivision','(i)',[],'Inner stroke and brackets are pale; the dot is unestablished.','c13',13,'13a'),
 ('C013.d15','Pale lower first subdivision state','deleted/overwritten (i)',['live displaced (i)'],'No separate cancellation stroke is distinguished.','c13',13,'13a'),
 ('C013.d13b','Third live subdivision extra opening curve','deleted/overwritten (',['live/retraced ('],'The curved glyph is clear; its state remains open.','c14',13,'13b')]:
 doubts.append(dict(id=did,location=loc,reading=read,alternatives=alts,confidence='low',reason=reason,crop=M[crop]['path'],source_doubt_row=row,local_sublocus=sub))
for d in diffs:
 if d['id'].startswith('C013.g'):
  # Graphical uncertainty concerns interpretation/hand/origin; path confidence is separate.
  doubts.append(dict(id=d['id']+'-role',location=d['location'],reading=d['reading'],alternatives=[],confidence=d['confidence'],reason='The supported shape is drawn. The role, hand, or surface origin of detached/faint components remains unresolved; no character value is supplied.',crop=d['readers_crop'],bbox=d['bbox'],qualification='graphical role/hand/origin; not a recovered-word alternative'))
# Inventory: every source inventory element was checked, with local new components appended.
inv=json.loads((P/'C_inventory.json').read_text())
for i in inv:
 i['sheet_kind']='list'; i['hand']='his hand'; i['source_inventory_element']=i['element']; i['transcribed']='yes'
 if i['element']=='013.01':i['kind']='drawing';i['first_words_or_objects']='six-column ruled list with six Notes headings';i['representation']='one full-page TikZ figure with positioned text and paths'
 if i['element']=='013.02':i['first_words_or_objects']='ten right-edge short stroke components';i['components']=[{'id':'Gedge'+str(n),'transcribed':'yes'} for n in range(1,11)]
 if i['element']=='013.10':i['components']=[{'id':'G15','description':'barred upward arrow, brace, interior loop and parallel pale runs; question; opposed arrows with middle join','transcribed':'yes'}]
 if i['element']=='013.18':i['components']=[{'id':'G16','description':'upper bent arrow and lower bent arrow with two horizontal runs','transcribed':'yes'}]
 if i['element']=='013.32':i['first_words_or_objects']='? and pale curved-top downward arrow';i['components']=[{'id':'G10','transcribed':'yes'}]
 if i['element']=='013.33':i['components']=[{'id':'G30','description':'pale curved descending shaft and lower arrowhead','transcribed':'yes'}]
 if i['element']=='013.34':i['first_words_or_objects']='qualified pale (i), deleted/overwritten or live displaced writing'
 if i['element']=='013.35':i['first_words_or_objects']='readable extra opening parenthesis; deleted/overwritten or live/retraced state'
 if i['element']=='013.36':i['position']='D subdivision, upper displaced label above lower dark (i)';i['first_words_or_objects']='readable (i), deleted/overwritten or live displaced state'
extra=[
 ('013.49','text','another unnamed hand','lower right, sideways','archive number 12, recorded in comment','archive'),
 ('013.50','drawing','undetermined hand','behind first title','four pale residual stroke runs','G02'),
 ('013.51','drawing','undetermined hand','above left marginal arrow bar','small pale detached point','G15a'),
 ('013.52','drawing','undetermined hand','above left of upper bent arrow','pale arch','G16b'),
 ('013.53','drawing','undetermined hand','left of upper bent arrow head','short detached oblique stroke','G16c'),
 ('013.54','drawing','undetermined hand','below upper bent arrow shaft','small detached point','G16d'),
 ('013.55','drawing','undetermined hand','beneath long in B lower title','dark detached dot','G12'),
 ('013.56','drawing','undetermined hand','first lower blank cell','interrupted narrow mark','G23'),
 ('013.57','drawing','undetermined hand','below first foot reference','interrupted slanted vertical trace','G24'),
 ('013.58','drawing','undetermined hand','right of first pale downward arrow','oblique fragment cluster','G25'),
 ('013.59','drawing','undetermined hand','first/second date boundary','curved upright with faint continuation','G26'),
 ('013.60','drawing','undetermined hand','beneath Fringale','irregular small spot','G27'),
 ('013.61','drawing','undetermined hand','above Baumeister, left point','pale point','G28a'),
 ('013.62','drawing','undetermined hand','above Baumeister, right point','dark spot with pale upper-right tip','G28b'),
 ('013.63','drawing','undetermined hand','just left of B in Baumeister','small pale point','G28c'),
 ('013.64','drawing','undetermined hand','beneath Découverte','small pale point','G29'),
 ('013.65','drawing','undetermined hand','below final lower title','isolated short horizontal stroke','GhalfB')]
for el,kind,hand,pos,first,code in extra:inv.append(dict(sheet_kind='list',hand=hand,element=el,kind=kind,position=pos,first_words_or_objects=first,transcribed='yes',tex_component=code))
# All distinct non-character components have explicit path maps.
component_map={
 'G02':['four draw subpaths in the G02 node'], 'G15a':['single ellipse'],
 'G16b':['single curved arch'], 'G16c':['single oblique segment'], 'G16d':['single ellipse'],
 'G12':['single filled ellipse'], 'G23':['upper draw path','dark ellipse','four separate pale lower segments'],
 'G24':['two upper pale segments','dark ellipse','three lower pale segments'],
 'G25':['pale upper slant','dark short upright','dark ellipse','two lower slants','two pale upper circles'],
 'G26':['main curved path','short pale continuation'], 'G27':['filled irregular polygon','short lower-left continuation'],
 'G28a':['single pale ellipse'],'G28b':['filled dark spot','short pale tip'],'G28c':['single pale ellipse'],'G29':['single pale ellipse'],'GhalfB':['single horizontal segment']}
for i in inv:
 if i.get('tex_component') in component_map:i['components']=[{'path':p,'transcribed':'yes'} for p in component_map[i['tex_component']]]
source_rows=[]
for n in range(1,14):
 local=[d for d in diffs if d.get('source_doubt_row')==n]
 source_rows.append(dict(row=n,source_section='C_doubts.txt / Doubtful readings',decisions=[d['id'] for d in local],local_locus_count=len(local),status='mixed' if n==13 else local[0]['C_doubt_status']))
report=dict(scan=13,reader='C',start_utc='2026-11-20 13:58:25 UTC',end_utc=None,full_image_viewed=True,halves_viewed=True,complete_visual_read=True,differences=diffs,doubts=doubts,inventory=inv,
 notes={'page_content':'Six-column ruled title/reference list, headings Notes 1, 5, 7, 15, 20, 23; live capital labels A B C D E E. Dates, bilingual titles, crossed subdivisions, live subdivisions and bottom references are all transcribed.',
 'authors_own_uncertainty':['? beside opposed arrows at left of first date','? beside pale downward arrow below the first cancelled subdivision'],
 'title_date_page_counts':'No page count is identified as such. Dates as written: (1976/77), (1978/79), (1979/80), (1980), (1981), (1981); the first date also appears in the cancelled early A entry. Archive number 12 is recorded only as a comment. No separate manuscript page numeral was found.',
 'mathematics_led_reading_decisions':'No mathematical computation, map, correspondence, or proof check was used. Subdivision decisions follow the surviving local strokes only.',
 'H_collation':'metadata.json gives hua_has=nothing and H.tex is empty. Every H field is null and every diff_H is false; no H collation rows were invented.',
 'source_row_accounting':'13 source doubtful-readings rows, 14 local loci. Row 13 is split into 13a (first live subdivision) and 13b (third live subdivision). The notation and abbreviation rows were not counted as doubts.',
 'inspection_order':'Clock read at 13:58:25 while loading brief/preamble/notation; packet files then read. Whole scan once, half a once, half b once, followed by 30 distinct crops. No successfully viewed image was reopened. c10 initial call aborted before dispatch and the same file was then displayed once.',
 'dimensions':{'full':[2365,1688],'half_a':[1242,1688],'half_b':[1243,1688],'half_a_origin':[0,0],'half_b_origin':[1122,0]},
 'crop_limits':'c16 retains complete arrows but clips adjacent date/title context; c29 retains complete Découverte and overlaps part of already-settled lower-arrow context without re-adjudicating that arrow. Right-edge crops preserve the available endpoints; no continuation outside the photographed sheet is supplied.',
 'graphical_qualifications':'Detached points, residual strokes and small marks are drawn with local unsure wrappers. Confidence in a supported path is recorded separately from unsettled role, hand or surface origin. Ordinary paper texture was not converted into supplied words.',
 'inventory_changes':'The archive numeral is now explicitly inventoried. The six-column list is represented by one TikZ figure with positioned text. Existing C inventory labels for pale displaced subdivisions have been updated to match explicit state uncertainty.',
 'structural_validation':'Pending final structural checks; no compiler or renderer used.'},
 notation=[
 {'location':'six large capitals','written_form':'A B C D E E','latex':r'\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E,\mathrm E','evidence':'Both final capitals show three horizontal E arms on their own local ink.'},
 {'location':'live subdivision row','written_form':'(i), (ii), (i), (i), (i), (iv)','latex':r'(\mathrm i),(\mathrm{ii}),(\mathrm i),(\mathrm i),(\mathrm i),(\mathrm{iv})','evidence':'Parentheses and local short dotted uprights/terminal v read on the halves; displaced traces separately enlarged.'},
 {'location':'foot references','written_form':'M 1976 *, M 1979, HS I, Sch I, Sch VI, Sch IX','latex':r'M 1976\mathord{*};\ M 1979;\ HS\ \mathrm I;\ Sch\ \mathrm I;\ Sch\ \overline{\underline{\mathrm{VI}}};\ Sch\ \overline{\underline{\mathrm{IX}}}','evidence':'First I numerals have clear serifs. VI and IX have common top and bottom bars. Star sits beside 1976 at the baseline.'},
 {'location':'last lower title','written_form':'Le “Maître”','latex':"Le ``Maître''",'evidence':'Paired short quote strokes occur on each side; circumflex retained.'},
 {'location':'first title','written_form':'Découverte; Méditation','latex':'Découverte; Méditation','evidence':'Acute strokes inspected in c29 and c02; singular final n settled in c02.'},
 {'location':'left below hatching','written_form':'? and curved-top downward arrow','latex':'?; G10 paths','evidence':'Separate question dot and hooked upper stroke; arrow has a distinct curved top and downward head.'},
 {'location':'before B live subdivision','written_form':'pale descending arrow','latex':'G30 paths','evidence':'Long pale curved shaft descends to short darker arrowhead; no new textual value supplied.'}],
 check_events=[],crops=manifest,brief_feedback=['The packet uses a diagram wrapper around a table and free TikZ. This return uses the prescribed figure wrapper for the page-wide graphical layout, with the left marginal cluster at its observed location.','The required inventory kind list has no dedicated table kind; drawing is used for the ruled list geometry and text for its entries.','For three displaced/overwritten subdivision loci, the glyph and its deletion state need independent qualifications. Their source-row identities and local state decisions are mapped explicitly.'],
 source_doubt_rows=source_rows,physical_cluster_map={'C013.d13a':['C013.d13a','C013.d15'],'C013.d11':['C013.d11'],'C013.d13b':['C013.d13b']})
(R/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex and report.json:',len(diffs),'decision/difference rows,',len(inv),'inventory items,',len(source_rows),'source doubt rows')
