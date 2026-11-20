import json
from datetime import datetime,timezone
from pathlib import Path
p=Path('work/scan026_b.json')
rows=[
 {'id':'M0509','scan':26,'decision':'first','reading':'non atomique','what the ink shows':'A separate low n-on group precedes atomique; the latter has a crossed tall t, an i dot, and the deep q downstroke before the terminal low letters.','crop':[600,820,1100,910],'confidence':'medium'},
 {'id':'M0510','scan':26,'decision':'undecided','reading':r'\unsure{par exemple}','what the ink shows':'The initial descending p and a later tall loop survive, but the long cancellation merges the central letter bodies. These remnants do not securely establish the full proposed phrase.','crop':[1090,820,1545,915],'confidence':'low'},
 {'id':'M0511','scan':26,'decision':'first','reading':'induit','what the ink shows':'The word begins with a dotted i, then a low n connection and a raised d; a second i dot appears before the short terminal t stroke.','crop':[300,1165,610,1245],'confidence':'medium'},
 {'id':'M0512','scan':26,'decision':'undecided','reading':r'\unsure{exactement}','what the ink shows':'Several raised loops and a final upward connection remain above the heavy horizontal cancellation. The middle bodies and crossings needed to establish exactement are merged into that line.','crop':[650,1165,1000,1245],'confidence':'low'},
 {'id':'M0513','scan':26,'decision':'first','reading':'applications','what the ink shows':'The compressed initial hooks lead into a tall l loop, a separately dotted i, and the raised t; low terminal strokes end in the hooked s before the comma.','crop':[1430,1260,1745,1360],'confidence':'medium'},
 {'id':'M0514','scan':26,'decision':'undecided','reading':r'\unsure{bornées}','what the ink shows':'The cancellation preserves an initial small upright, a middle arch and a high terminal looped stroke, while covering nearly all the connecting bodies. The terminal stroke is not securely separable from the cancellation, so bornées remains unconfirmed.','crop':[300,1370,600,1460],'confidence':'low'},
 {'id':'M0515','scan':26,'decision':'undecided','reading':r'\unsure{munie de}','what the ink shows':'A dot and a small late ascender survive above the deletion, with low humps at the beginning. The heavy bar joins the rest of the letters and obscures the proposed word division.','crop':[1190,1470,1500,1580],'confidence':'low'},
 {'id':'M0516','scan':26,'decision':'first','reading':'sur','what the ink shows':'After the opening parenthesis, the uncancelled word has a short initial s turn, connected low u strokes and an extended terminal r before a separate comma.','crop':[1520,1470,1700,1580],'confidence':'medium'},
 {'id':'M0517','scan':26,'decision':'first','reading':r'\mathfrak A_2','what the ink shows':'The capital has a pointed high apex, oblique left stroke and crossbar, with an open lower swash rather than two stacked B bowls. A separate small 2 sits below and to its right.','crop':[1230,2030,1485,2140],'confidence':'high'},
 {'id':'M0518','scan':26,'decision':'undecided','reading':r'd\unsure{ans}','what the ink shows':'The deleted word begins with a closed low bowl and tall d ascender. The following low bodies are joined by the cancellation, preventing a secure reading of ans.','crop':[1480,2030,1665,2140],'confidence':'low'},
 {'id':'M0519','scan':26,'decision':'first','reading':"dans l'adhérence",'what the ink shows':'The first word has the tall looped d and a separate terminal s; l and its apostrophe are distinct at the next word. The following a and adjacent d/h ascenders lead into the compressed accented middle and long final connection.','crop':[300,2110,1030,2240],'confidence':'medium'},
]
views=[{'path':'source/DM01_1_001-160_scans/1_scan026.jpg','box':[0,0,1761,2598],'scale':1,'contrast':1,'purpose':'Locate assigned marks on actual-size page.'}]
items=[
 ('scan026_b_0509_0510',(280,735,1745,915),2,'Non atomique and deleted par exemple.'),
 ('scan026_b_0511_0512',(280,1140,1745,1250),2,'Induit and deleted exactement.'),
 ('scan026_b_0513_0514',(280,1250,1745,1460),2,'Applications and deleted bornées.'),
 ('scan026_b_0515_0516',(280,1460,1745,1680),2,'Deleted munie de and parenthetic sur.'),
 ('scan026_b_0517_0519',(280,2020,1745,2240),2,'Formula and following cancelled and uncancelled words.'),
 ('scan026_b_0510_detail',(1090,820,1545,915),3,'Surviving strokes under par exemple cancellation.'),
 ('scan026_b_0511_0512_detail',(300,1165,1000,1245),3,'Dotted letters of induit and cancellation remnants.'),
 ('scan026_b_0513_detail',(1430,1260,1745,1360),3,'Applications ascenders, dot and ending.'),
 ('scan026_b_0514_detail',(300,1370,600,1460),3,'Cancelled bornées and terminal loop.'),
 ('scan026_b_0515_0516_detail',(1190,1470,1700,1580),3,'Deletion remnants and uncancelled sur.'),
 ('scan026_b_0517_0518_detail',(1220,2025,1665,2150),3,'A versus B, lowered 2 and cancelled dans.'),
 ('scan026_b_0519_detail',(300,2110,1030,2240),3,'Dans and l\u2019adhérence letter sequence.'),
]
views += [{'path':'work/views/'+name+'.png','box':list(box),'scale':scale,'contrast':1,'purpose':purpose} for name,box,scale,purpose in items]
report={'scan':26,'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan026_b','started_utc':'2026-11-20T00:35:46.831386+00:00','finished_utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'views':views,'other_errors':[],'patterns':[],'notes':['Assigned subset M0509–M0519 only; actual source dimensions 1761×2598.','Dense cancellation leaves M0510, M0512, M0514, M0515 and M0518 partly or wholly uncertain after enlarged inspection.','M0517 was referred for an independent A/B check; own primary reading is A with subscript 2.']}
p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
Path('work/scan026_b.initial.json').write_text(p.read_text())
print(p)
print(report['finished_utc'])
from collections import Counter
print(dict(Counter(r['decision'] for r in rows)))
