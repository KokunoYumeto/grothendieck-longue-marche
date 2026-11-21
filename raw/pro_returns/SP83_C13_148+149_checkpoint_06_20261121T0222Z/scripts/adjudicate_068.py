from pathlib import Path
import csv,json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan068'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest()=='16ad7c72c0d9e43ff2bd375bec671847e2635b6ebc2702ddec9ced1bb01b842e'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B01':'Two pale closed loops meet at the one heavy vertex; their further crossing is unmarked. Both readings preserve this incidence. Different curve control points and filled-vertex contours alone do not establish another material difference.',
'B02':'Five pairs of dark endpoints are visible. The first three have joining strokes; in the fourth, short faint upper and lower stubs survive but the middle is not joined. The fifth pair has no connecting line. The upper endpoint of the first pair has a small pale center. The second tracing captures these visible details without completing the fourth connector.',
'B03':'Six heavy points, overlapping outer traces, and the long left-to-right inner chord are visible. A further faint run curves down from the upper-right vertex inside the right contour and bends left toward the lowest vertex. The first drawing lacked part of this run. Its visible portions are added, with breaks where the hatching obscures continuity; the whole figure retains its existing uncertainty about faint incidence. The second reader also recognized the curved run. Lower retraced arcs are retained without interpreting every crossing as a vertex.',
'B04':'The heavy two-point edge, two small endpoint enclosures, broad surrounding curve, left continuation and three rays from the right point are visible. The broad enclosure and right small enclosure have gaps. The first tracing preserves them; the second closes the broad outline. No arrows or labels are supplied.',
'B05':'The broad oval and left small endpoint enclosure have visible upper/side gaps. The central heavy connection has a closely retraced pale band. The first approximation retains the gaps and retracing, while the second regularizes the enclosing paths as closed. No extra independent graph edge is inferred from the broad band.',
'B06':'Both complete canonical crop (through pixel-identical lossless WebP) and the existing neutral-weight helper were viewed. Two inner holes and an outer retraced oval are visible. Between the holes the left pale connector bends toward the upper-left side of the lower hole, rather than ending near its upper-right side as first drawn; the right run wanders near the right side. These paths are adjusted. The outer upper pen gap, broken upper-right radial run and isolated faint fragment above-left of the lower hole are retained from the first tracing. Printed hatching prevents secure complete incidence, so the figure remains doubtful and no symmetric missing radial edge is added.',
'B07':'All six upright listing lines were read on the rotated canonical crop: ****A END JOB 653 PREDONTA ROOM 11.24.04 AM 02 JUN 82 R6.PR1 SYS JES2 JOB 653 END A****. The last character of PR1 is the same printer digit 1 seen in the time. The two readings agree on every character. The second uses explicit positions for the large printer gaps; this layout refinement is not counted as a new witness error.',
'B08':'The P field has twelve rows: eleven P, twelve P, three rows with PP at each side, twelve P, eleven P, then five rows of left PP. The two readings have the same characters and occupied cells; array versus individually positioned nodes is only formatting.',
'B09':'The twelve R rows have eleven and twelve letters at the top, three open rows, two full middle rows, and five descending right-leg pairs with gaps increasing from four to eight spaces. The first and second character grids agree.',
'B10':'Twelve E rows are visible: two full twelve-letter rows; three EE rows; two eight-letter rows; three EE rows; two full twelve-letter rows. The two representations agree on these cells.',
'B11':'The D field has nine and ten letters in its first two rows, a seven-cell inner gap in row three, eight-cell gaps in rows four through nine, a seven-cell gap in row ten, then ten and nine letters. The source and both grids agree.',
'B12':'The O field has two full twelve-letter top rows, eight rows of OO at both sides with eight empty cells between, and two full twelve-letter bottom rows. The two readings agree.',
'B13':'The diagonal N run and both stems were read row by row. The last row really has only one right-hand N, one cell farther right than the pair in the preceding row. Both readings retain this printer irregularity; it is not regularized.',
'B14':'There are two rows of twelve T, followed by ten rows with the central TT after five empty cells. Both grids agree.',
'B15':'The A grid has ten letters after one blank in row one, twelve in row two, three open AA rows, two full twelve-letter middle rows and five open AA rows. The two readings agree.',
'B16':'The whole twelve-row four-zero block, top strip, groups 1 and 2, and existing column-ruler detail were viewed. The first row starts two printer cells to the right of row two, hence eleven blank cells from the base, not ten. This offset is also visible in the other two groups in the complete top strip. The remaining row positions and character runs agree. Eight zeros remain the leading count in each top row, but the hatching masks some individual contours; the second reader certainty does not remove those four count doubts.',
'B17':'The pale folio has a looped 6 and a crossed descending 7: 67. The extra margin wrapper in the second reading is only placement markup.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
V={}
V['B02']=C['B02']['second']
V['B03']=C['B03']['first'].replace('\\foreach \\x/\\y in {2515/287',r'''% Faint curved upper-right to lowest-vertex run: visible sections only.
\draw[gray!60] (2758,202) .. controls (2784,235) and (2795,272) .. (2789,307);
\draw[gray!60] (2787,314) .. controls (2788,351) and (2760,386) .. (2724,412);
\draw[gray!60] (2711,422) .. controls (2679,445) and (2640,478) .. (2600,497);
\draw[gray!60] (2591,503)--(2577,511);
\foreach \x/\y in {2515/287''')
V['B06']=C['B06']['first'].replace(r'\draw[gray] (2631,752) .. controls (2625,779) and (2619,801) .. (2610,814);',r'\draw[gray] (2631,752) .. controls (2616,782) and (2584,809) .. (2567,830);').replace(r'\draw[gray] (2656,758) .. controls (2651,779) and (2646,800) .. (2638,820);',r'\draw[gray] (2640,758) .. controls (2650,782) and (2635,803) .. (2638,820);')
V['B07']=C['B07']['second']
old=r'\unsure{\texttt{'+r'\ '*10+'00000000}}'
new=r'\unsure{\texttt{'+r'\ '*11+'00000000}}'
assert C['B16']['first'].count(old)==4
V['B16']=C['B16']['first'].replace(old,new)
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,v in V.items():
 assert C[b]['first'] in s,b
 s=s.replace(C[b]['first'],v)
 D[b].update(choice='reading',reading=v)
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
for x in r['changes']:
 n=int(x['id'].rsplit('-',1)[1]);b=f'B{n:02}'
 x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b])
 if b in V:x['final']=V[b]
 if n==2:x.update(diff_c=True,confidence='medium')
for x in r['doubts']:
 for b in ['B03','B06']:
  if x['reading']==C[b]['first']:x.update(reading=V[b],reason=E[b])
 if x['reading']==old:x.update(reading=new,reason=E['B16'])
for x in r['decisions']:
 if x['id'] in ['M0896','M0897','M0898','M0899']:
  x.update(reading=new,evidence=E['B16'],crop=f'crops/{p}_second_B16.png',box=boxes['B16'])
r['notes'].append(dict(id=p+'-N-audit',text='The independent reading was frozen before comparison. All 17 unequal boxes were inspected by the main reader. Printed PREDONTA grids and all six job records agree in wording; the spatial setting of the latter is refined. Four first zero rows move one fixed-pitch cell right, while their counts remain doubtful. Drawing changes add fourth-pair stubs and a visible faint interior arc, and adjust the inter-hole connector trajectory. These are optical readings, not a topological proof.'))
extra=[f'crops/{p}_second_{z}.png' for z in ['B03_neutral','B06_neutral','B16_grid_upper','B16_group1','B16_group2','B16_strip1']]+[f'crops/transport/{p}_second_B06.webp']
r['second_main_review']=dict(viewed_boxes=list(E),reviewed_at=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),decisions=f'second/{p}_main_decisions.json',additional_existing_crops_viewed=extra)
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
