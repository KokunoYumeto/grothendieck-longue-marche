import json
from pathlib import Path
from datetime import datetime,timezone
base=Path('work/scan058_a_views')
views=[{'path':'source/DM01_1_001-160_scans/1_scan058.jpg','box':[0,0,1676,2159],'scale':1,'contrast':1,'rotation':0,'purpose':'Locate assigned marks on measured full page.'}]
for name,box,scale,c,rot,purpose in [
('top',[210,45,1645,195],2,1,0,'Locate op. and cancelled two-factor expression.'),
('immediate',[260,535,1020,625],3,1,0,'Inspect the word after résulte in line context.'),
('delete_E1',[1330,695,1610,785],3,1,0,'Inspect first cancelled parenthetical E.'),
('delete_E2',[1130,835,1380,935],3,1,0,'Inspect second cancelled parenthetical E.'),
('sur',[900,990,1530,1105],3,1,0,'Separate cancelled parenthetical and lower inserted sur.'),
('formula',[790,1185,1110,1290],3,1,0,'Inspect all ink of cancelled mapping expression.'),
('punct',[940,1350,1165,1450],3,1,0,'Separate overwritten cluster after u=u0 from following comma.'),
('margin',[35,245,185,850],3,1,90,'Initial rotation check for sideways margin note; upside down.'),
('op',[1035,55,1140,125],6,1,0,'Distinguish the o bowl, p descent and abbreviation dot.'),
('uv',[525,115,620,175],6,1,0,'Count the two cancelled baseline factors.'),
('immediate_detail',[680,535,1015,625],5,1,0,'Inspect initial i/m strokes, middle d/i and final tall t.'),
('formula_detail',[790,1185,1110,1290],5,1.25,0,'Examine cancelled initial layers, arrow and right residue.'),
('margin_upright',[35,245,185,850],3,1,270,'Read two-line margin note upright.'),
('margin_full',[20,190,205,915],3,1.3,270,'Ensure complete margin phrase and line context.'),
('sur_detail',[1170,1005,1320,1095],6,1.3,0,'Inspect surviving parentheses and obscured internal letters.'),
('punct_detail',[1055,1370,1145,1440],6,1,0,'Inspect height and branching of dark punctuation cluster.'),
('margin_line1',[50,245,130,855],4,1.5,270,'Inspect first-line word bodies and paired tall t strokes.'),
('margin_line2',[105,300,180,850],4,1.5,270,'Inspect simple/application descenders and tall l strokes.'),
('uv_compare',[515,110,715,180],5,1,0,'Compare cancelled factors with immediately following vu.')]:
 views.append({'path':str(base/(name+'.png')),'box':box,'scale':scale,'contrast':c,'rotation':rot,'purpose':purpose})
rows=[
{'id':'M1145','scan':58,'decision':'first','reading':'op.','what the ink shows':'A closed initial oval is followed by a separate p stem descending below its small right shoulder, then a detached round dot. The o is overinked but retains its white upper counter.','crop':[1035,55,1140,125],'confidence':'high'},
{'id':'M1146','scan':58,'decision':'first','reading':'uv','what the ink shows':'Two baseline bodies survive the horizontal deletion: the left has two uprights joined by a deep u trough, and the right rises into a compact hooked v body. The immediately following uncancelled vu supplies the local hooked v and open u comparison; no superscript appears.','crop':[515,110,715,180],'confidence':'medium'},
{'id':'M1147','scan':58,'decision':'first','reading':'immédiatement','what the ink shows':'The word begins with a short i stroke and two low extended m runs; the middle retains a looped d and a detached i dot, followed by a tall t and compressed connected ending. It forms one run without the opening a/ss bodies or separate initial d required by aussi directement.','crop':[680,535,1015,625],'confidence':'medium'},
{'id':'M1148','scan':58,'decision':'first','reading':'(E)','what the ink shows':'After the uncancelled L¹(E), the deleted group retains a left curved parenthesis, the upright and right-going bars of E, and a distinct closing hook at the right. Crossing strokes thicken the upper and middle bars without hiding the complete parenthetical extent.','crop':[1330,695,1610,785],'confidence':'medium'},
{'id':'M1149','scan':58,'decision':'first','reading':'(E)','what the ink shows':'The second deleted group has a separate curved left edge, an E with three rightward horizontal arms, and a closing parenthesis turning left at its foot. The cancellation follows the bars, but their joins and the two outside curves remain visible.','crop':[1130,835,1380,935],'confidence':'medium'},
{'id':'M1150','scan':58,'decision':'undecided','reading':r'(\unsure{sur})','what the ink shows':'The deleted upper layer has visible opening and closing curved parentheses. Two heavy diagonal/horizontal strokes obscure the internal low letter bodies; the clearly readable lower inserted sur is a separate layer and does not establish all three deleted letters.','crop':[1170,1005,1320,1095],'confidence':'low'},
{'id':'M1151','scan':58,'decision':'undecided','reading':r'\unsure{$\bar w\to(u,$}','what the ink shows':'The initial barred body is crossed by several diagonal and vertical strokes, followed by a rightward shaft with a dark head. At the right a u-shaped body, small low loop, downward terminal hook and separate oblique dash survive; cancellation prevents secure separation of the proposed opening parenthesis, possible low index and punctuation, so the entire source fragment remains uncertain.','crop':[790,1185,1110,1290],'confidence':'low'},
{'id':'M1152','scan':58,'decision':'undecided','reading':r'\unsure{.}','what the ink shows':'Between u=u₀ and the separate following comma is a tall, thick vertical cluster with an upper slant and a rightward spur. It is not a clean round dot; overinking prevents identifying the underlying punctuation or cancelled sign.','crop':[940,1350,1165,1450],'confidence':'low'},
{'id':'M1153','scan':58,'decision':'first','reading':'supprimer ou mettre comme simple application','what the ink shows':'Upright, supprimer has an initial s/u run, paired long p descenders and dotted i; ou has a small oval and low exit, mettre a faint m/e run and paired tall t strokes, and comme an open c, oval o and low m arches. Below, simple has s/i, shallow m, p descent and tall l; application has the initial a, paired p descenders, tall l, dotted i and the extended tion ending, supporting the two-word ending rather than remarque.','crop':[20,190,205,915],'confidence':'medium'}]
report={'scan':58,'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan058_a','started_utc':'2026-11-20T03:52:34.058470+00:00','finished_utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'views':views,'other_errors':[],'patterns':[{'name':'Cancelled repeated parenthetical E','marks':['M1148','M1149'],'description':'Both occurrences retain separate outside parenthesis curves and an E with rightward bars despite thick cancellation; each occurrence was inspected separately.'}],'notes':['Assigned M1145–M1153 only. Actual image size 1676×2159. Start timestamp was taken before the first own-ink view; text/instruction preparation preceded it.','M1150 keeps internal deleted letters uncertain independently of the readable lower insertion. M1151 and M1152 were sent to the coordinator for independent review.','M1153 has a complete rotated source-box view plus separate enlarged line views; wording is medium confidence because pencil-like strokes are faint.','No OCR, recognition service or ImageGen used. All listed views were actually inspected; initial incorrect-direction margin rotation is retained in the view log.']}
path=Path('work/scan058_a.json');path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
initial=Path('work/scan058_a.initial.json')
if initial.exists(): raise SystemExit('Initial already exists; refusing overwrite')
initial.write_bytes(path.read_bytes())
print(path,report['finished_utc'],len(rows),len(views))
