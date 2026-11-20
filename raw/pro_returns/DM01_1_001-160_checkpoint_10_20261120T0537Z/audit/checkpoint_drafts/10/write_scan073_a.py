import json
from pathlib import Path
rows=[
('M1448','first',r'v_n','Below Sup, an open curved v is followed by a distinct lower horizontal stroke with a hooked end; the extra subscript trace excludes bare v.',[1255,230,1360,330],'high'),
('M1449','undecided',r'\unsure{n|m}','The lowered index after alpha consists of a low trough, one small rise and a long flat exit. The compressed stroke does not securely distinguish n from m, including against nearby fuller indices.',[1380,230,1480,285],'low'),
('M1450','undecided',r'\unsure{En effet}','A tall initial loop and a short terminal upright survive, but dense zigzag cancellation merges the intervening letter bodies and word ending; neither full word can be independently recovered.',[310,365,650,450],'low'),
('M1451','undecided',r'\unsure{v_n}','Between Lambda and the right norm bars, a small loop and a lower short horizontal remnant remain. Broad cancellation crosses the baseline and index, so v and the n layer cannot both be securely isolated.',[900,550,1030,620],'low'),
('M1452','first','---','Inside the round parentheses are three separated short horizontal strokes; no letter body or numeral is visible between them.',[640,725,805,790],'high'),
('M1453','undecided',r'\unsure{uv}','Above the surviving argument, one rounded loop and a short raised horizontal remnant survive a thick horizontal deletion. The number and identities of the concealed baseline letters are not established by those remnants.',[435,1030,585,1110],'low'),
('M1454','undecided',r'\unsure{\alpha_m(|v|)}','A curved opening parenthesis survives in the deleted expression, but cancellation merges the alpha/index region and the argument/right boundary. The bars, letter, closing layers and complete concealed extent cannot be separately established.',[830,1040,1050,1125],'low'),
('M1455','alternative','w','The first rho argument has two deep adjoining bowls separated by a tall middle upstroke, supporting w rather than the single hooked v. A tiny detached raised speck follows the last bowl; it does not establish an additional prime.',[1190,1035,1350,1145],'medium'),
('M1456','undecided',r'\unsure{u|w}','The last rho argument has a tall left downstroke, a broad shallow bowl, a low middle rise and a second terminal dip. This can be u with a curled exit or a flattened w; the plain hooked v is not supported.',[1370,1060,1545,1145],'low'),
('M1457','undecided',r'\unsure{que}','A long descending loop consistent with q survives at the left, while the middle bodies and final upright/loop are crossed by thick zigzags. The u and e ending cannot be independently read.',[635,1150,815,1230],'low'),
]
views=[
('source/DM01_1_001-160_scans/1_scan073.jpg',[0,0,1768,2600],1,1,'Locate all assigned marks and page boundaries.'),
('work/scan073_a_top_formula.png',[1100,210,1640,360],3,1,'Sup subscript and final alpha index.'),
('work/scan073_a_en_effet.png',[310,365,650,450],3,1,'Deleted En effet bodies and ending.'),
('work/scan073_a_cross_norm.png',[780,530,1100,630],4,1,'Locate deleted variable inside norm.'),
('work/scan073_a_parenthetic.png',[330,700,850,800],3,1,'Count the parenthetical horizontal strokes.'),
('work/scan073_a_lemma.png',[330,1020,1600,1230],2,1,'Locate deleted letters, formula, rho arguments and que.'),
('work/scan073_a_top_indices.png',[580,220,1610,345],3,1,'Compare baseline v and compressed n/m indices.'),
('work/scan073_a_deleted_formula.png',[830,1040,1050,1125],5,1,'Inspect deleted formula components and boundaries.'),
('work/scan073_a_deleted_letters.png',[435,1030,585,1110],5,1,'Inspect cancelled baseline letter count.'),
('work/scan073_a_rho_args.png',[1190,1035,1545,1145],4,1,'Distinguish bowls and terminal strokes in both rho arguments.'),
('work/scan073_a_que.png',[635,1150,815,1230],5,1,'Inspect q descender and obscured ending.'),
('work/scan073_a_vu_context.png',[770,1145,1730,1285],2,1,'Compare local v hook and u bodies.'),
('work/scan073_a_vn_detail.png',[900,550,1030,620],6,1.5,'Separate variable remnant from index and cancellation.'),
('work/scan073_a_vu_comparison.png',[380,1225,1220,1290],3,1,'Compare same-line variable bowls and exit curls.'),
('work/scan073_a_alpha_argument.png',[610,1045,805,1120],4,1,'Compare adjacent alpha argument and compressed index.'),
('work/scan073_a_last_index.png',[1380,230,1480,285],8,1,'Resolve exact final index trough and flattened exit.'),
]
data={'scan':73,'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan073_a','started_utc':'2026-11-20T05:30:21.738969+00:00','finished_utc':'2026-11-20T05:32:22+00:00','rows':[{'id':i,'scan':73,'decision':d,'reading':r,'what the ink shows':e,'crop':b,'confidence':c,**({'candidates':[r'\alpha_m(|v|)']} if i=='M1454' else {})} for i,d,r,e,b,c in rows],'views':[{'path':p,'box':b,'scale':s,'contrast':c,'purpose':u} for p,b,s,c,u in views],'other_errors':[],'patterns':[],'notes':['Actual source dimensions are 1768 x 2600; all crop boxes use that unscaled source.','Only M1448–M1457 adjudicated. All listed marks on scan073 were read to establish boundaries; no outside-mark error is asserted.','Cancellation prevents recovery of several complete words, formula layers and counts; source candidate lengths are not evidence of concealed ink extent.','Peer review requested from coordinator for M1453 and M1455–M1456. Initial primary interval may include pauses; it is not a continuous active-reading claim.']}
Path('work/scan073_a.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('work/scan073_a.json')
from collections import Counter
print(dict(Counter(x['decision'] for x in data['rows'])))
