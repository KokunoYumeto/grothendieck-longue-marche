"""Main-reader decisions after actual visual inspection of scan 089 audit crops."""
from pathlib import Path
import csv,json,subprocess,sys
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];s='147_scan089'
items={x['box']:x for x in json.loads((R/'second'/f'{s}_comparison.json').read_text())['items']}
ds=[]
def add(b,groups):
 k=f'089-B{b:02d}'
 ds.append(dict(box=k,use_first=True,crop=f'crops/blind/{s}/{k}.png',changed=False,ink=' '.join(g[2] for g in groups),token_resolutions=[dict(operations=o,decision=d,ink=e) for o,d,e in groups]))
add(1,[([0],'Retain the equivalent mapsto encoding.','The raised connector has a left bar and a rightward head; the longer macro changes only typeset length.'),([1,2],'Keep only the cancelled M locally doubtful.','The crossing obscures the middle of the two-peaked capital. The lower G has a visible curved body and returning lower hook outside that obstruction.')])
add(3,[([0,2],'Retain the uncertain one-sided endpoints.','Each shaft ends in a short downward flick, without the separate two arms of a complete arrowhead.'),([1],'Retain soit.','The opening low s-like turn is followed by a rounded connecting body and a final tall crossed t; there is no initial e loop followed by the shorter st sequence.')])
add(4,[([0,1,2,3,4,5,6,7,8,9,16],'Retain edition display and label syntax.','The number is 125 and the four objects and arrows occupy the same square. Extra label braces, alignment characters and displayed-number wrappers do not change the ink reading.'),([10,11],'Retain C as the replacement at the same subscript position.','The clear round C retraces the angular old character at subscript height. It is not a separately raised addition; the old A candidate stays doubtful.'),([12,13,14,15],'Retain gamma-f and the possible overwritten S before a definite Pi.','The lower arrow label has two ascending arms and a narrow descending loop, the gamma shape, with a distinct lower f. The lower-right Pi has two uprights and a top bar. An additional S-like curved trace crosses its first upright and continues rightward; its old-letter status remains doubtful rather than disappearing.')])
add(5,[([0],'Retain i.e.','The neutral box clips the left beginning. Supplement crops/blind/147_scan089/089-B05-left-context.png, original bounds (200,1458,1050,1610), shows a separate dotted i before the looped e; this is not the single joined et proposed by the blind reading.'),([1,2,3,4,5,10,11],'Retain equivalent diagram grouping.','Both readings have the same three objects and the first complete rightward arrow labelled S Pi(f).'),([6,7,8,9],'Retain the second endpoint as uncertain.','The second horizontal shaft has a minute downward dark return and no distinct upper head arm, unlike the first arrow. The phi-G-prime label is plain.')])
add(6,[([0,1],'Retain the overwritten subscript without a raised-insertion wrapper.','The round live C and partly hidden angular A share the same subscript location beneath S.'),([2,3,4,5,6,7],'Retain doubled Z and the equivalent typeset lattice map.','All four Z occurrences have two parallel diagonal strokes. The lattice map has a rightward head, its A(G) and C exponents are visible, and a period follows the target.'),([8,9],'Retain automatique alors literally.','The first word ends after the q descender and compact ue, with no ment or raised abbreviation. The next word has a small initial a loop, tall l, and low ors sequence; it is neither dans nor donc.')])
subprocess.run([sys.executable,str(R/'scripts/write_audit.py')],input=json.dumps(dict(scan=89,second_reader='/root/blind_a',decisions=ds)),text=True,check=True)
t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (R/'root_visual_review.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for path in [f'crops/blind/{s}/089-B{i:02d}.png' for i in [1,3,4,5,6]]+[f'crops/blind/{s}/089-B05-left-context.png','crops/147_scan089_composite-chain.png']:
  w.writerow([89,path,'/root',t,'viewed and adjudicated'])
p=R/'adjudicated'/f'{s}.json';r=json.loads(p.read_text())
r['notes'].append('Blind audit retained all first box readings. The lower square label is gamma-f by its two arms and descending loop, and the doubled Z diagonals remain distinct. The neutral composite box clipped the start of i.e.; a supplementary left-context crop (200,1458,1050,1610) supplied the dotted i and e for that adjudication. No prior committed box or first reading was modified.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(R/'scripts/approve_audit.py'),'89'],check=True)
