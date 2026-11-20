from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'records/scan002/reader_{a}/report.json').read_text()) for a in 'ABC'}
I={a:{i['id']:i for i in R[a]['issues']} for a in 'ABC'}
# Main reader decisions made after viewing each discrepancy crop; no OCR.
mapping={'D01':('B01','D01'),'D02':('B02','D02'),'D03':('B02','D02'),'D04':('B03','D03'),'D05':('B04','D04'),'D06':('B05','D05'),'D07':('B06','D06'),'D08':('B07','D07'),'D09':('B08','D08'),'D10':('B10','D10'),'D11':('B11','D11'),'D12':('B12','D12'),'D13':('B13','D13'),'D14':('B14','D14'),'T01':('B15','T01'),'T02':('B16','T02'),'T03':('B17','T03'),'T04':('B18','T04'),'T05':('B19','T05'),'T06':('B20','T06'),'T07':('B21','T07'),'T08':('B28','T03'),'T09':('B22','T08'),'T10':('B23','T09'),'T11':('B24','T10'),'T12':('B25','T14'),'T13':('B26','T11'),'M01':('B27','M01')}
issues=[]
for a,(b,c) in mapping.items():
 x=copy.deepcopy(I['A'][a]);x['final']=x.pop('reading');x['readers']={k:I[k][v]['reading'] for k,v in [('A',a),('B',b),('C',c)]}
 x['marked_in_H']='no'
 if a.startswith('D') and a not in ['D10','D11']:x['crop']=f'crops/scan002_{a}.png'
 else:
  crop={'D10':'01_lens_scribble.png','D11':'01_lens_scribble.png','T01':'02_ss_sets_first_link.png','T02':'02_ss_sets_first_link.png','T04':'03_cat_left_arrow.png','T05':'03_cat_left_arrow.png','T06':'04_preord_overwrite.png','T07':'04_preord_overwrite.png','T09':'05_maquettes_triang.png','T10':'06_Fx_Fy.png','T11':'06_Fx_Fy.png'}.get(a)
  x['crop']=f'records/scan002/reader_C/{crop}' if crop else ''
 if a=='T12':x['crop']='crops/scan002_T12.png'
 if a=='T13':x['crop']='records/scan002/reader_C/06_Fx_Fy.png; crops/scan002_T12.png'
 if a=='M01':x['crop']='records/scan002/reader_A/crop07_lower_right_edge.png'
 issues.append(x)
D={x['id']:x for x in issues}
def update(k,**kw):D[k].update(kw)
update('D01',diff_C=True,final='Three, four and five marked positions; forked central tick of the longest segment and a small shaft gap just right of its second tick.',evidence=I['A']['D01']['evidence']+' Main crop also shows a narrow white interruption immediately right of the second tick, around source x=1045–1049. All three retained C’s continuous shaft here; the consolidated trace separates its two portions.')
update('D04',diff_C=True,final='Irregular two-cell upright strip, open upper-left corner, bowed bottom, detached lower-right dot, and crossbar beginning just short of the left side.',evidence=I['A']['D04']['evidence']+' Main crop additionally shows white between the left stem and the beginning of the internal crossbar. All three retained C’s joined crossbar; its start is moved right to preserve the visible gap.')
update('D06',diff_C=True,final='Two irregular hatched lenses with eight interior strokes, upper retrace, open far-right tip and a short inward return at the far-left tip.',evidence=I['A']['D06']['evidence']+' A short near-horizontal stroke turns inward from the far-left point. It is absent from the three returned C-based traces and is added from this crop.')
update('D10',final='Trace the visible dense loops and their two descending bends; retain an in-place comment that their status as cancelled lettering is unresolved, without asserting one unreadable word.',confidence='low',evidence=I['C']['D10']['evidence']+' The main reader confirms the two descending bends. Reader A’s empty uncertainty node is not retained; the visible ink is represented graphically and its unresolved status is stated at that location in a LaTeX comment.')
update('D11',crop='records/scan002/reader_C/01_lens_scribble.png; crops/scan002_middle_right_lenses.png',final='Five slanted marks in the first lens, three principal marks plus a short curved loop in the middle, four in the last; a gap before the middle lens and a touching second joint.',evidence=I['A']['D11']['evidence']+' The main crop of the middle and right lenses confirms the open left side of the middle lens and the short transverse loop crossing its two right hatch strokes. The first-to-second separation is also explicitly reported by B29 and reader C D11.')
# A distinct contour correction in the first lens, reported independently by B and C.
x=copy.deepcopy(I['C']['D09']);x['id']='D10a';x['final']=x.pop('reading');x['crop']='records/scan002/reader_C/01_lens_scribble.png';x['readers']={'A':'Retained C’s closed upper-left outline in reading.tex.','B':I['B']['B09']['reading'],'C':I['C']['D09']['reading']};x['marked_in_H']='no';x['evidence']+=' The main reader confirms this gap; no interpretation of its mathematical significance is imposed.';issues.insert(10,x)
update('D12',diff_C=True,final='Sloping three-cell strip with open upper-left, a second divider stopping below the top, and separate lower-right returns; preserve the small bent return on the lower edge.',evidence=I['A']['D12']['evidence']+' Main crop shows a short upward-and-downward return on the lower edge near its right end, followed by a short rightward tail; the right vertical ends separately above it. The earlier C trace and all three returns simplify these two terminals. Their separation and the lower return are traced here.')
update('D13',diff_C=True,final='Two unequal unhatched lobes with a rising through-line, open far-left top, a small gap below the central junction, and a short inward return at the outer right bend.',evidence=I['A']['D13']['evidence']+' The main crop also separates the lower central branches from the upper junction by a narrow white gap, and shows a short inward stub at the right bend. All three retained C’s joined upper/lower central contour and omitted that stub. The consolidated trace preserves both features.')
update('T02',consequential='The first relation is a hooked left-pointing arrow, not the primary superset reading of C or the unqualified superset of H.',evidence=I['C']['T02']['evidence']+' The main crop confirms an independent left head and right return; reader B’s residual superset alternative is resolved.')
update('T04',consequential='The live second relation has a right-hand hook as well as a left arrowhead; H’s straight arrow loses that decoration.')
update('T05',diff_C=True,final=r'\unsure{\hookleftarrow|\deleted{\supset}\hookleftarrow}',evidence=I['C']['T05']['evidence']+' The main reader adopts this ordering: secure live hooked arrow, uncertain previous-sign history. A separately cancelled superset is neither asserted nor silently ruled out.',confidence='low')
update('T09',final=r'\overset{\inserted{\text{Maquettes}}}{\deleted{\text{Triang}}}',evidence=I['C']['T08']['evidence']+' The vertical placement of Maquettes over Triang is retained in the final display.')
update('T11',consequential='The letters x and y are baseline arguments in Fx and Fy; H makes them subscripts.',evidence=I['C']['T10']['evidence'])
update('T12',evidence=I['C']['T14']['evidence']+' The main crop also confirms a separate lower bar in the relation and the long descending stroke of y; these are not a prime or an exclamation mark.')
update('M01',final='Six small nonlinguistic edge marks traced as a marginal graphic, with origin explicitly uncertain.',evidence=I['C']['M01']['evidence'])
# Explicit unchanged adjudications for the C contextual glyph questions.
for cid,readers in [('T12',{'A':'Right arrow retained in Fx to Fy.','B':'Right arrow retained in Fx to Fy.','C':I['C']['T12']['reading']}),('T13',{'A':'x <= y with curves retained.','B':I['B']['B25']['reading'],'C':I['C']['T13']['reading']})]:
 x=copy.deepcopy(I['C'][cid]);x['id']='unchanged_'+cid;x['final']=x.pop('reading');x['readers']=readers;x['crop']='records/scan002/reader_C/06_Fx_Fy.png' if cid=='T12' else 'crops/scan002_T12.png';x['marked_in_H']='no';issues.append(x)
text=(O/'records/scan002/reader_C/reading.tex').read_text()
text=text.replace('\\scanpage{2}\n\\cotefile{104}','\\cotefile{104}\n\\scanpage{2}')
text=text.replace('(922,132)--(1041,128)--(1144,126)','(922,132)--(1043,128) (1049,128)--(1144,126)')
text=text.replace('(154,262)--(184,258)','(159,262)--(184,258)')
text=text.replace('\\draw (637,216)--(624,211)','\\draw (504,255)..controls(508,258)and(513,258)..(520,258);\n\\draw (637,216)--(624,211)')
text=text.replace('(645,484)--(757,478)--(759,506)--(754,514)\n (651,488)--(647,517)--(745,514)', '(645,484)--(757,478)--(759,506)--(754,508)\n (651,488)--(647,517)--(743,513)--(746,508)--(747,516)--(756,513)')
text=text.replace('..controls(390,660)and(395,679)..(400,704)\n ..controls(391,756)', '..controls(390,660)and(395,679)..(400,701);\n\\draw (400,708) ..controls(391,756)')
text=text.replace('\\draw (228,704)--(400,698)--(551,688);','\\draw (228,704)--(400,698)--(551,688);\n\\draw (556,705)--(549,706);')
(O/'pages/H104-01_104_scan002.tex').write_text(text)
inv=copy.deepcopy(R['C']['inventory'])
for x in inv:
 x['sheet_kind']='text'
 if x['hand']=='main handwritten hand':x['hand']='his hand'
 if x['kind']=='margin':x['kind']='margin note'
 x['position']='full-image bbox '+','.join(map(str,x['position']['bbox']))
remaining=[
 {'location':'First lens, dense loops','reading':'Graphical trace; status uncertain','alternatives':'Cancelled lettering or nonlinguistic retracing','confidence':'low','reason':'No dependable letters or defensible word count survive; the source ink itself is traced.'},
 {'location':'Second connector, earlier stroke history','reading':r'\hookleftarrow','alternatives':r'\deleted{\supset}\hookleftarrow','confidence':'low','reason':'The live hooked arrow is secure; the older sign is not independently separable.'},
 {'location':'Under live Préord','reading':r'\deleted{\unsure{Ord}}','alternatives':'Underlying lettering not independently recoverable','confidence':'low','reason':'O-like oval and tall d-like stroke are compatible with Ord but overlaid.'},
 {'location':'Live third name','reading':'Préord','alternatives':'PréOrd','confidence':'medium','reason':'The case of the o/O is obscured by overlapping strokes; the acute is clear.'},
 {'location':'Lower-right edge','reading':'Six nonlinguistic marks','alternatives':'Writer’s ink, handling marks or reproduction marks','confidence':'low','reason':'Marks are visible but cannot be attributed from the supplied image.'}]
notes=[
 'A handwritten sheet of subdivided segments, strips, hatched curved figures and an unhatched double lobe. Below them are a corrected row of names, then Fx → Fy and x ≤ y on separate lines. There is no explanatory prose or explicit theorem on this page.',
 'The row reads (Ss sets), (Cat), an overwritten Préord/PréOrd, (Ord), and Maquettes inserted above struck Triang. The first two live connectors are hooked left arrows; the last two are open-left inclusion signs. The possible earlier sign beneath the second arrow and possible Ord beneath Préord remain uncertain.',
 'The ink, not a type or inclusion argument, settles the first arrow and the baseline placement of x and y. H’s subscripts change the formula’s written notation. No mathematical proof, calculation or background theorem was used to make these glyph decisions, so this scan adds no check events.',
 'The first lens contains dense retraced loops. They are drawn, including their descending bends, without claiming that one word is illegible. Whether they cancel lettering remains unresolved. The six dark marks at the lower-right edge are preserved with unattributed origin.',
 'H supplies an actual separate TikZ drawing as well as editorial prose. Its regularizations and omitted strokes are collated against that drawing. The prose’s early plural description of four-cell squares is not counted as an extra manuscript difference: H’s drawing and later description show one. Editorial headings and explanatory notes are not transcribed as manuscript text.',
 'No author-written “à vérifier”, “sauf erreur”, “je présume”, question, title, date or manuscript folio occurs. The lower-left 1 is an archive sheet number and is recorded only in a comment.'
]
decision={'scan':2,'folder':'H104-01','issues':issues,'remaining':remaining,'inventory':inv,'notes':notes,'checks':[],'crop_counts':{'A':7,'B':6,'C':7,'main':14},'main_adjudication_complete':True}
(O/'records/scan002/decision.json').write_text(json.dumps(decision,ensure_ascii=False,indent=2)+'\n')
(O/'records/scan002/main_read_log.md').write_text('''# Main adjudication: scan 002

Only the reader returns and decision crops were viewed; the main reader did not open a whole page or either half. Reader C crops 01–06 and reader A crop07 were viewed once. Fourteen new crops were generated for the remaining drawing and inequality differences; their source boxes are in crops/main_crop_manifest.jsonl. Six image outputs from one overlarge tool response were unavailable after truncation and were delivered again in batches of two before adjudication. No decided locus was re-cropped or re-read.

All three returns, C’s contextual doubts, the H page and H drawing were compared. Decisions and all three readings are in decision.json and the generated changes log. The main crop review supplied five additional contour refinements overlooked in all three returned traces: the longest segment’s shaft gap, the two-cell strip’s internal gap, the upper lens pair’s inward stub, the lower three-cell strip’s terminal return, and the lower double lobe’s central gap/right stub. These are visible drawing features, with no mathematical interpretation assigned.

All listed elements are present in the consolidated page. A visible scribble is preserved graphically with its unresolved status in a local comment, rather than an empty uncertainty macro or an invented word count. H’s general drawing-regularization notes do not count as in-place doubt marks in marked_in_H.
''')
print('scan002 adjudication written',len(issues),'issues',len(inv),'inventory')
