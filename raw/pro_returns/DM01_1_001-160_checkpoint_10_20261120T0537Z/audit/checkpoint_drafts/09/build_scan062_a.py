import json, os
from datetime import datetime,timezone
from pathlib import Path
rows=[
{'id':'M1208','scan':62,'decision':'first','reading':'(a)','what the ink shows':'Two curved parentheses enclose a small rounded a with a right descending exit stroke. The enclosed oval and exit are visible despite the pale folded paper.','crop':[40,95,125,160],'confidence':'medium'},
{'id':'M1209','scan':62,'decision':'undecided','reading':r'\illegible{2}','what the ink shows':'Between the two parenthesized labels the fold carries separated dark hooks, short slanting strokes and a few dot-like remnants on two levels. No continuous pair of word bodies or discriminating letter sequence survives the light and crease.','crop':[20,155,245,305],'confidence':'low'},
{'id':'M1210','scan':62,'decision':'undecided','reading':r'(\unsure{b|3})','what the ink shows':'The enclosing left and right curves are visible; the interior has two short right-facing rounded lobes. A tall b ascender cannot be separated securely from the pale surrounding strokes, leaving b versus 3 unresolved.','crop':[35,290,125,365],'confidence':'low'},
{'id':'M1211','scan':62,'decision':'undecided','reading':r'Prop\unsure{.}','what the ink shows':'The tall initial P loop, short r shoulder, low o body and deep final p descender can be followed through the cancellation. No distinct abbreviation point is secure after the p; the isolated dark fleck lies below and to its left.','crop':[265,275,345,365],'confidence':'low'},
{'id':'M1212','scan':62,'decision':'undecided','reading':r'\unsure{un}','what the ink shows':'After Soit, a thick horizontal deletion covers almost the whole short word. Its left upturn and right triangular peak remain, but the intervening u and n bodies cannot be individually distinguished.','crop':[655,300,785,360],'confidence':'low'},
{'id':'M1213','scan':62,'decision':'first','reading':'Si','what the ink shows':'Below the inserted Si, the cancelled form retains a tall bent S with a lower return and a separate short i stroke and dot. These two letter positions remain distinct above the cancellation, and the upper inserted S supplies a local shape comparison.','crop':[995,530,1165,610],'confidence':'medium'},
{'id':'M1214','scan':62,'decision':'undecided','reading':r'(\unsure{hilbert}','what the ink shows':'An opening parenthesis is distinct at the left of the cancelled fragment. Several tall stems and low turns follow beneath the horizontal crossing, but the rightmost bodies run into the page edge and do not separately establish all of hilbert.','crop':[1550,530,1707,607],'confidence':'low'},
{'id':'M1215','scan':62,'decision':'undecided','reading':r'\unsure{hilbert. Notons que}','what the ink shows':'The first group has tall h/l/b-like rises and a dot above the deletion; the next starts with a clear N and a short crossed ascender. The horizontal strike merges most low letter bodies, including the proposed endings and que, so the complete phrase remains uncertain.','crop':[280,620,1005,718],'confidence':'low'},
{'id':'M1216','scan':62,'decision':'undecided','reading':r'\illegible{2}','what the ink shows':'Immediately before the fixed parenthesized e_J, two small rises project above the crossing and broken low hooks remain below it. Their joins and word divisions are covered by the continuous strike, so no two-word reading is secured.','crop':[730,620,1110,718],'confidence':'low'}
]
views=[
{'path':'source/DM01_1_001-160_scans/1_scan062.jpg','box':[0,0,1707,2188],'scale':1,'contrast':1,'rotation':0,'purpose':'Locate the assigned folded labels and deleted theorem text.'},
{'path':'work/scan062_a_views/fold.png','box':[0,70,260,410],'scale':4,'contrast':1,'rotation':0,'purpose':'Inspect the three folded-corner marks.'},
{'path':'work/scan062_a_views/heading.png','box':[260,275,925,370],'scale':3,'contrast':1,'rotation':0,'purpose':'Inspect deleted Prop. and un with heading context.'},
{'path':'work/scan062_a_views/si_hilbert.png','box':[980,520,1707,625],'scale':3,'contrast':1,'rotation':0,'purpose':'Locate deleted Si and the right-edge hilbert fragment.'},
{'path':'work/scan062_a_views/erased_band.png','box':[275,620,1360,795],'scale':3,'contrast':1,'rotation':0,'purpose':'Separate the crossed theorem lines and locate M1215–M1216.'},
{'path':'work/scan062_a_views/fold_rot40.png','box':[0,70,260,410],'scale':4,'contrast':1.6,'rotation':40,'purpose':'Check faint folded letter remnants at a rotated angle.'},
{'path':'work/scan062_a_views/deleted_hilbert.png','box':[1430,530,1707,607],'scale':5,'contrast':1,'rotation':0,'purpose':'Resolve opening parenthesis and edge-limited deleted stems.'},
{'path':'work/scan062_a_views/si.png','box':[995,530,1165,610],'scale':5,'contrast':1.3,'rotation':0,'purpose':'Distinguish cancelled S and i from the inserted Si above.'},
{'path':'work/scan062_a_views/deleted_words.png','box':[280,630,1365,715],'scale':4,'contrast':1.1,'rotation':0,'purpose':'Inspect full cancelled phrase and neighboring e_J.'},
{'path':'work/scan062_a_views/midgap.png','box':[760,630,1185,705],'scale':5,'contrast':1.3,'rotation':0,'purpose':'Inspect surviving strokes before the fixed e_J.'},
{'path':'work/scan062_a_views/prop_un.png','box':[265,280,790,360],'scale':5,'contrast':1.25,'rotation':0,'purpose':'Check individual abbreviation letters and obscured un bodies.'},
{'path':'work/scan062_a_views/fold_labels.png','box':[20,85,220,365],'scale':5,'contrast':1.25,'rotation':20,'purpose':'Compare parenthesized a and ambiguous b/3 lobes.'},
{'path':'work/scan062_a_views/prop_detail.png','box':[265,275,345,365],'scale':8,'contrast':0.8,'rotation':0,'purpose':'Check final p and possible abbreviation point.'}
]
finished=datetime.now(timezone.utc).isoformat()
d={'scan':62,'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan062_a','started_utc':'2026-11-20T04:15:17.141137+00:00','finished_utc':finished,'rows':rows,'views':views,'other_errors':[],'patterns':[{'name':'Cancelled and inserted Si','marks':['M1213'],'description':'The cancelled and inserted forms at this occurrence both retain a tall bent initial S and a separately dotted i; this local comparison supports the two-letter reading.'}],'notes':['Assigned M1208–M1216 only; current source and every current-page MARKS.tsv boundary read. Actual image dimensions 1707 by 2188.','Folded paper, dense cancellation and the right page edge limit the unresolved readings after enlarged and contrast-adjusted inspection. No OCR or recognition tools used.','Potential b/3 competition in M1210 and obscured M1215–M1216 strokes sent to the coordinator before completion.']}
p=Path('work/scan062_a.json');p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
initial=Path('work/scan062_a.initial.json')
with initial.open('x') as f:f.write(p.read_text())
os.chmod(initial,0o444)
print(str(p));print(finished);print({key:sum(r['decision']==key for r in rows) for key in ['first','alternative','other','undecided']})
