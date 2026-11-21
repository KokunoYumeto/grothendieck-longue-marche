"""Root adjudication of scan103 after direct inspection of all differing boxes."""
from pathlib import Path
import csv,json,subprocess,sys
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];s='147_scan103';it={x['box']:x for x in json.loads((R/'second'/f'{s}_comparison.json').read_text())['items']};ds=[]
f=lambda b:it[f'103-B{b:02d}']['first']
def add(b,g,final=None):
 k=f'103-B{b:02d}';ds.append(dict(box=k,final=f(b) if final is None else final,changed=final is not None and final!=f(b),crop=f'crops/blind/{s}/{k}.png',ink=' '.join(x[2] for x in g),token_resolutions=[dict(operations=o,decision=d,ink=e) for o,d,e in g]))
add(2,[([0,1,2],'Retain the local opening-parenthesis doubt and the clear pas with point.','The opening curve is not fully separable from the p onset. The p/a/s bodies and isolated dark point after s are exposed, so doubt applies to the opener rather than to the whole pas word.'),([3],'Retain comm.','The group ends in low m returns before the next parenthesis; there is no additional u body or tall crossed t.'),([4],'Retain iso.','The final rounded o is followed by blank space before de. No further m arches are exposed.')])
oldright=r"\prod_{\alpha'\in S'}\deleted{\unsure{1}}M"
newright=r"\prod_{\alpha'\in S'}\raisebox{-0.7ex}{\scriptsize$\deleted{\unsure{1}}$}M"
new3=f(3).replace(oldright,newright).replace(r'\unsure{*}',r'\unsure{*|1}')
add(3,[([0,1,2,5,10,11,12,13,14,15,20,21,22,34],'Retain the equivalent diagram, spacing and annotation-layout conventions.','The number146 lies beside the upper row. The same five objects, two vertical equivalences, middle horizontal connector and two diagonals occupy three rows. Spaces separating Pi-index1 from M and ampersand encodings do not alter these readings; the annotation has three visible baselines.'),([3,4,9],'Retain the actual top shaft and its uncertain short lower-left return.','The right head is complete. At the left end only a short lower return is exposed; no upper wing certifies the full left arrowhead supplied by the blind leftrightarrow convention. The first drawing preserves this stroke and its doubt.'),([6,7,8],'Retain the cancelled old G-prime candidate above the live G.','The upper group is heavily crossed and its raised detail is obscured. The clear live G is lower. Stacking these readings preserves their positions without asserting an independently certain old prime or a new insertion state for the lower G.'),([16,17],'Retain S-prime in the annotation.','The enlarged annotation shows a separate curved stroke above/right of the capital S. It is distinct from the S body and from the diagonal shaft; the prime is exposed.'),([18,19],'Retain the word à between the genus symbols.','A short upright accent stands above a compact rounded lower a body. This matches the small à at the beginning of the preceding annotation line. No two parallel equality bars occur; the upper and lower forms are not two similar punctuation dots.'),([23,24,25],'Retain the right product and lower the cancelled small1 candidate beside it.','The product has a small crossed descending mark at its lower-right, above the alpha-prime-in-S-prime baseline. Both readers retain the same cancelled candidate; the final encoding makes its small lowered position explicit without adding a live Pi to the factor.'),([26,27],'Retain the alpha-prime/alpha doubt at the physical right edge.','The lower alpha body reaches the edge of the sheet. A following prime is not fully exposed, so the blind unqualified alpha-prime is not certified.'),([28,29,30,31,32,33],'Keep the lower cancelled glyph independently lowered, admitting star or1.','The dense small cluster is above/right of S-prime, at the lower-right of the product. Its underlying stem and crossing strokes do not distinguish star from1. Position is retained without fixing its attachment inside the product index or asserting a shared revision history with the right product.')],new3)
add(4,[([0],'Retain equivalent three-point ellipsis encoding.','Three separate dark points follow elles-mêmes in the diagonal margin note.')])
add(6,[([0,1,2,3,4],'Retain equivalent index order and the cancelled raised-prime candidate.','The small crossed group is above/right of the target g while alpha is below/right. Writing the superscript before or after the subscript and using apostrophe or prime does not change these positions. The cancellation is clear but the underlying prime remains uncertain.')])
add(7,[([0],'Retain généraux.','The raised word has low terminal u/x strokes after the g-é-n-é-r-a sequence. There is no internal tall l or t supporting the longer blind alternatives; the separated tall stroke after the word belongs to the insertion leader.'),([1,2],'Retain réduit without an added e.','The last tall crossed t has a short horizontal exit followed by blank space before à. No separate final e loop is exposed.'),([3,4,5,6,7,8,9],'Retain the first geometrical rendering of148.','One continuous shaft carries two right chevrons; the second overlaps the right upright of the target Pi. Both Pi objects have visible index1, and the condition ends with a comma. A generic twoheadrightarrow captures two heads but loses the observed overlap, which the retained drawing records.')])
subprocess.run([sys.executable,str(R/'scripts/write_audit.py')],input=json.dumps(dict(scan=103,second_reader='/root/blind_a',decisions=ds,notes=['The main reader additionally inspected the saved enlargement103-B03_annotation_view.png from original box[705,1210,1085,1430]. It confirms the separate S-prime stroke and the small à form without consulting mathematical expectations.'])),text=True,check=True)
with (R/'root_visual_review.tsv').open('a',newline='') as out:
 w=csv.writer(out,delimiter='\t');t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 for d in ds:w.writerow([103,d['crop'],'/root',t,'viewed and adjudicated'])
 w.writerow([103,f'crops/blind/{s}/103-B03_annotation_view.png','/root',t,'viewed annotation enlargement'])
p=R/'adjudicated'/f'{s}.json';r=json.loads(p.read_text());cs={x['id']:x for x in r['changes']}
updates=[]
for k in ['C09','C10','C17']:
 final=cs[k]['final'].replace(oldright,newright).replace(r'\unsure{*}',r'\unsure{*|1}')
 if k=='C10':final=r'\raisebox{-0.7ex}{\scriptsize$\deleted{\unsure{1}}$}'
 fields=dict(final=final)
 if k=='C17':fields['ink']=cs[k]['ink'].replace('underlying star candidate','underlying star/1 candidates')
 updates.append(dict(id=k,fields=fields))
payload=dict(scan=103,page_replacements=[dict(old=oldright,new=newright,count=1),dict(old=r'\unsure{*}',new=r'\unsure{*|1}',count=1)],changes_updates=updates,notes_add=['Blind review confirms the short comm and iso forms, the separate S-prime in the diagonal annotation, the word à between genus symbols, the final généraux and réduit, and the geometry of146/148. The cancelled right-product candidate is now explicitly small and lowered; the lower cancelled cluster admits star or1. These are placement/uncertainty refinements, not newly counted witness errors.'])
subprocess.run([sys.executable,str(R/'scripts/apply_audit_edits.py')],input=json.dumps(payload),text=True,check=True)
r=json.loads(p.read_text())
for d in r['doubts']:
 if d['place']=='Cancelled group after the right-hand product':d['reading']=r'\raisebox{-0.7ex}{\scriptsize$\deleted{\unsure{1}}$}'
 if d['place']=="Lower product's cancelled group and its attachment":
  d['reading']=d['reading'].replace(r'\unsure{*}',r'\unsure{*|1}');d['alternatives']=['star candidate','1 candidate','unrecoverable small cancelled glyph; exact attachment unresolved']
for e in r['inventory']:
 if e['element']=='E06':e['position']='middle-right product, small lowered group between product sign and M'
 if e['element']=='E08':e['first_words_or_objects']=r'\unsure{*|1}'
r['notes']=[n.replace('lower cancelled star-candidate','lower cancelled star/1 candidate') for n in r['notes']]
for h in r['hand_log']:
 if h['habit']=='Tiny cancelled glyphs cannot be resolved from their expected mathematical role.':h['holds']=h['holds'].replace('star candidate','star/1 candidates')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(R/'scripts/approve_audit.py'),'103'],check=True)
