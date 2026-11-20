import json
from datetime import datetime,timezone
from pathlib import Path
rows=[
('M0520','first','alors','The inserted word has a low onset rising to a tall angular l, followed by a compressed low ors run; it sits above the insertion curve.',[785,2110,980,2175],'medium'),
('M0521','first',r'\mathfrak H_A','The main glyph has two upright shoulders joined across a dark center and a long left descending stroke, supporting a fraktur H rather than a rounded mu. The small lower-right A has a sloping left leg, bowed right leg and crossbar.',[1000,2210,1115,2320],'medium'),
('M0522','undecided',r'la \unsure{même} finie','After la there is a short doubled horizontal glyph, too compressed to resolve the proposed même confidently. The last word has a tall crossed f, a separate i dot and a low terminal run, unlike the proposed pour.',[1280,2190,1725,2320],'low'),
('M0523','first','Considérons','The initial open C is followed by a long low run with an i dot, then a looped d and an accented low continuation ending in short ons strokes.',[300,2315,620,2400],'medium'),
('M0524','alternative','A','The character is pointed and triangular, with a crossbar and a hooked lower-left foot; it has the angular outline of A rather than a rounded theta.',[690,2310,755,2400],'high'),
('M0525','first','une rétraction','A short low une precedes a separate r onset and extended low run. The latter has a prominent crossed t, a following i dot and a small lifted terminal on stroke.',[780,2320,1245,2410],'medium'),
('M0526','undecided',r'\unsure{formes}','A hooked f with a long descender survives, together with small rises at the right end. Two heavy deletion strokes cover the central letters, so formes remains plausible but not securely distinguishable.',[1080,2440,1405,2530],'low'),
('M0527','other','en question','The first word has a looped e and n hump with no q descender. The next has a descending initial q, a medial crossed t and following i dot, supporting en question rather than que continuons.',[960,2375,1340,2465],'high'),
('M0528','first','finies','The word begins with a tall f whose cross-stroke extends rightward, followed by a separate i dot and a compressed low nies run.',[300,2510,465,2585],'medium'),
('M0529','undecided',r'tout \unsure{un théorème} encore sur','The initial tout has upright strokes at each end, and the final sequence shows the separate e/n, open c and low ore, then short sur strokes. The middle has a short low word and a tall stem followed by almost straight bars, insufficient to settle un théorème.',[480,2490,1280,2590],'low'),
('M0530','first','analogue','The beginning is a sequence of low a/n/a strokes before a tall l. The trailing rounded and descending strokes continue to the page corner and support ogue.',[1470,2500,1745,2598],'medium')]
views=[
('source/DM01_1_001-160_scans/1_scan026.jpg',[0,0,1761,2598],1,1,'Locate assigned lower-page marks'),
('work/scan026_c_views/midbottom.png',[250,2015,1740,2340],1.7,1,'Insertion and symbol context for M0520–M0522'),
('work/scan026_c_views/lastlines.png',[240,2300,1740,2598],1.8,1,'Read M0523–M0530 in line context'),
('work/scan026_c_views/m520.png',[720,2080,1100,2245],3,1,'Inspect inserted alors strokes'),
('work/scan026_c_views/m521_522.png',[975,2190,1740,2335],3,1,'Inspect fraktur symbol and la … finie'),
('work/scan026_c_views/m523_525.png',[260,2290,1300,2420],3,1,'Inspect Considérons, triangular A and rétraction'),
('work/scan026_c_views/m527.png',[880,2360,1370,2480],3,1,'Distinguish en question from first candidate'),
('work/scan026_c_views/m528_530.png',[275,2485,1750,2598],3,1,'Inspect final line and page-edge analogue'),
('work/scan026_c_views/m529_left.png',[475,2500,970,2590],4,1,'Inspect tout and unresolved middle words'),
('work/scan026_c_views/m529_right.png',[945,2495,1330,2595],4,1,'Inspect encore sur strokes'),
('work/scan026_c_views/m526.png',[1040,2435,1415,2535],4,1.3,'Inspect formes under heavy deletion'),
('work/scan026_c_views/m521.png',[1000,2210,1115,2320],6,1,'Inspect fraktur head and lower-right index')]
report={'scan':26,'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan026_c','started_utc':'2026-11-20T00:35:53.126509+00:00','finished_utc':datetime.now(timezone.utc).isoformat(),'rows':[dict(id=i,scan=26,decision=d,reading=r,**{'what the ink shows':e},crop=b,confidence=c) for i,d,r,e,b,c in rows],'views':[dict(path=p,box=b,scale=s,contrast=c,purpose=u) for p,b,s,c,u in views],'other_errors':[],'patterns':[{'name':'Compressed finie(s)','marks':['M0522','M0528'],'description':'Both occurrences show a tall crossed f, a distinct i dot, then a low compressed terminal run.'}],'notes':['Initial own-ink review of assigned M0520–M0530 only; actual image dimensions 1761×2598. No OCR or Hua comparison used.','Independent checks requested through coordinator for M0522, M0527 and M0529; complete initial report saved before waiting.','M0526 remains unresolved because central letters are hidden by deletion; M0529 retains uncertainty over its compressed middle words.']}
p=Path('work/scan026_c.json');p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');Path('work/scan026_c_initial.json').write_text(p.read_text())
print(report['finished_utc']);print(p);from collections import Counter;print(dict(Counter(r['decision'] for r in report['rows'])))
