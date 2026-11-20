from pathlib import Path
import json
ROOT=Path('/workspace/scratch/94548b74fbe0')
OUT=ROOT/'out/readers/010/B'
CROPS=json.loads((OUT/'crops.json').read_text())
CROP={x['path']:x for x in CROPS}
D=[]
def row(id,location,C,reading,evidence,confidence,kind,crop=None,bbox=None,diff=True,status=None,**extra):
 d={'id':id,'location':location,'C':C,'H':None,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':diff,'diff_H':False,'C_doubt_status':status,'readers_crop':crop,'bbox':{'source':'full','coordinates':bbox} if bbox else CROP[crop]['bbox'] if crop else None,'mathematical_consequence':None}
 d.update(extra)
 D.append(d)
row('B01','Lower left graph, left endpoint of first segment',r'\unsure{\bullet|\circ}; doubtful-readings row 1 has filled left point, with open also admitted',r'\unsure{\circ|\bullet}', 'The left endpoint encloses a small, sharply light centre. The outer black patch is triangular and broader below; the intended fill remains uncertain. The right endpoint of this first segment has the larger clear centre already represented by C.', 'medium','misread symbol or index','c02_lower_left_graph.png',[127,1026,146,1047],status='retained',C_doubt_source_section='Doubtful readings',C_doubt_source_row=1)
row('B02','Final middle disk and the two angular traces at the foot','Doubtful-readings row 2: faint strokes | marks from the other surface','Visible stem, blob and angular traces retained graphically; hand, origin and role remain undetermined.','The upper extension has dark and pale intervals; the separate blob and both angular shapes are visible. The page alone does not settle the source of these marks. Local drawing changes are recorded separately below.','low','other','c05_middle_final_disk.png',diff=False,status='retained',C_doubt_source_section='Doubtful readings',C_doubt_source_row=2,additional_crops=['c06_lower_graph_and_left_angular.png','c07_right_angular.png'])
row('B03','Bottom row, second disk','Doubtful-readings row 3: diagonal cancellation | hatching; C.tex wraps the picture in deleted','Diagonal cancellation | hatching, retained as an uncertain state around the graphically reproduced strokes.','Several long reversing diagonal paths cross internal strokes and run beyond parts of the outline. Their geometric presence is clear; the distinction between cancellation and hatching remains unresolved from the writing.','medium','other','c04_overdrawn_disk.png',diff=False,status='retained',C_doubt_source_section='Doubtful readings',C_doubt_source_row=3)
row('B04','Under seventh upper disk, middle vertex',r'\unsure{\bullet|\circ}',r'\unsure{\bullet|\circ}','A dark lower-left mass rises into a rightward hook, with an open white recess on the right. The hook does not settle the intended filled/open notation. The same primary and alternative are retained.','medium','other','c01_upper_middle_vertex.png',[1148,243,1168,260],diff=False,status='retained',C_doubt_source_section='Doubtful readings',C_doubt_source_row=4)
row('B05','Upper edge and open space right of middle group','Doubtful-readings row 5: detached marks | transfer or surface flecks','Detached marks drawn; possible transfer or surface flecks retained; no character or hand assigned.','Two bent dark marks, one pale curved trace, and two tiny black flecks are visible. Enlargements supply shape evidence but do not settle their purpose or origin. The higher pale slant and the two upper-edge shape revisions have their own rows.','low','other','c08_upper_edge_marks.png',diff=False,status='retained',C_doubt_source_section='Doubtful readings',C_doubt_source_row=5,additional_crops=['c09_right_pale_marks.png','c10_right_flecks.png'])
row('B06','Lower middle graph, first vertex',r'\bullet',r'\unsure{\bullet|\circ}','The left point has a gray triangular recess enclosed by darker sides. Its centre is less white than the first lower-left graph endpoint. Filled remains the first candidate; open remains a supported local alternative.','medium','other','c03_lower_middle_graph.png',[470,1017,490,1038])
row('B07','Last lower graph, first vertex',r'\bullet',r'\unsure{\bullet|\circ}','The left end has a broad black upper/left body and a light lower recess with a short hook to the right. The intended fill is unresolved. This is a separate local fill decision from the other graphs.','medium','other','c06_lower_graph_and_left_angular.png',[979,1025,1003,1043])
row('B08','Under seventh upper disk, projecting hook of middle vertex','The doubtful bullet/circle is represented without its separately projecting upper-right hook','Additional short curved path above/right of the middle vertex','The enlarged mark has an upper arch continuing down on the right beyond the main black mass. The added TikZ path preserves that visible projection; B04 retains the symbol qualification.','high','drawing or diagram','c01_upper_middle_vertex.png',[1149,244,1165,257])
row('B09','Final middle disk, above the outer lower arch','No detached point at this position','Small detached black spot near (1314,543)','A compact dark fleck sits in clear space between the diagonal chord and the outer lower arch, below the larger blob.','high','omission','c05_middle_final_disk.png',[1308,536,1321,551])
row('B10','Above final middle disk, long extension',r'One uniformly dark path from (1328,433) toward (1341,329)','Pale underlying trace with separately darker short segments','The upper enlargement shows separated dark patches and pale intervals along the extension, with a dark lower attachment. The geometry is retained with differing opacity. Origin and role remain as qualified in B02.','high','drawing or diagram','c05_middle_final_disk.png',[1323,323,1346,437])
row('B11','Bottom row second disk, lower-left boundary','No short downward tip at about x490','Short dark descending tip from the lower-left outline','A dark short stroke protrudes beneath the boundary, ending around (490,920). It is visible separately from the long final cancellation tail farther right.','high','omission','c04_overdrawn_disk.png',[484,906,497,925])
row('B12','Bottom row second disk, pale vertical trace above the lower-left tip','No pale vertical trace at about x490','Pale descending trace ending at the lower outline','A weak nearly vertical trace runs through the lower interior toward the short dark tip. Its exact origin and relation to the other strokes remain undetermined.','medium','omission','c04_overdrawn_disk.png',[484,854,499,918])
row('B13','Upper edge, left of the two detached marks',r'(1018,28)--(1025,29)','Shallow bowl-shaped trace with raised ends','The enlarged left mark descends toward the centre and rises at its right end. C uses a straight short line. No letter candidate is assigned.','medium','drawing or diagram','c08_upper_edge_marks.png',[1015,23,1028,33])
row('B14','Upper edge, right of the two detached marks',r'(1037,27)--(1046,26)','Short bar with a raised/bent left end and irregular raised right end','The enlarged mark has short upright returns at its ends surrounding a low connecting part. C uses a simple oblique bar. Its role remains unresolved in B05.','medium','drawing or diagram','c08_upper_edge_marks.png',[1033,22,1050,32])
row('B15','Right of middle group, above the existing pale curled trace','No higher slanted pale trace','Short pale curved/slanted trace around (1567,352)–(1580,362)','The enlargement shows a separate thin gray trace above and to the right of the larger pale hook. It has no supported letter reading.','medium','omission','c09_right_pale_marks.png',[1563,347,1585,367])
row('B16','Below and right of the graph under upper disk 2','No pale curve at this position','Thin pale hook/curve from about (416,241) down to (403,275)','The enlargement shows a bent gray line with a descending right part and a leftward lower return. It is reproduced as shape only; hand and purpose remain undetermined.','medium','omission','c11_pale_curve_below_top2.png',[399,239,428,279])
row('B17','Above upper disk 4','No pale descending trace at this position','Short broken pale descending trace with a darker small piece','The target enlargement shows the darker piece and a faint downward course. Very weak gray material reaches toward the lower crop edge; its continuation is not settled, and no second crop was taken. Only the supported short course is drawn.','low','omission','c13_pale_above_top4.png',[780,39,793,67],crop_boundary_note='Very faint gray material approaches the lower boundary at y=73; continuation and connection remain unresolved.')
row('B18','Between the first and second lower disks','No pale diagonal trace in this space','Short pale broken diagonal descending right','Several gray pieces align along the observed short slant. No character, operation, or relation to a neighboring disk is supplied.','medium','omission','c12_pale_slant_between_lower_disks.png',[365,739,397,780])
row('B19','Inside first lower disk, left of the right-hand black crossing',r'Pale horizontal trace begins at (276,827)','Faint left extension begins near (252,825), joining the darker right piece','Half a shows a faint nearly horizontal approach from farther left to the short darker mark already drawn in C. This extent was settled on the half, so no crop was made.','high','drawing or diagram',bbox=[247,815,302,841],evidence_surface='half a; coordinates equal full-scan coordinates')
row('B20','Inside the rightmost angular trace at the foot','No pale interior diagonal','Pale diagonal rising right through the interior of the angular shape','The enlargement shows a weak diagonal from the lower-left interior toward the upper-right area. Its precise relation to the darker angular outline remains undetermined.','medium','omission','c07_right_angular.png',[1426,886,1570,1051])
row('B21','Upper part of the rightmost angular trace',r'Continuous pale segment beginning (1568,905)','Darker short vertical piece over the pale trace','A distinct dark short stroke is visible near (1568,908)–(1570,917), above the right-hand slant. The pale path is retained and the darker local part added.','medium','drawing or diagram','c07_right_angular.png',[1563,903,1576,921])
row('B22','Beside the upper part of the rightmost angular trace','No independently drawn fleck at this position','Small detached spot near (1566,921)','The small dark spot lies left of the pale vertical continuation and below the short dark dash. No glyph or attachment is inferred.','medium','omission','c07_right_angular.png',[1561,917,1571,926])
row('B23','Above-left of the upper end of the rightmost angular trace','No detached gray spot at this position','Small gray spot near (1550,893)','A small detached gray patch is visible above-left of the upper vertical fragment. Shape is preserved without assigning hand or function.','low','omission','c07_right_angular.png',[1544,888,1556,899])
row('B24','Right of the upper end of the rightmost angular trace','No gray patch at this position','Small gray patch near (1603,930)','The enlargement shows a detached gray patch to the right of the angular trace. It supports no character reading; origin remains undetermined.','low','omission','c07_right_angular.png',[1597,924,1610,937])
row('B25','Below the rightmost angular trace','No separate short dash below the angular shape','Detached short downward/right gray dash near (1435,1084)–(1437,1093)','A short isolated gray stroke appears beneath the angular drawing. It is reproduced without connecting it to the shape above.','medium','omission','c07_right_angular.png',[1429,1079,1443,1098])

# The five source uncertainty-table rows remain five source loci; subordinate
# shape changes above do not invent extra C-doubt rows.
DOUBTS=[
 {'location':'Lower left graph, first left endpoint','reading':r'\circ','alternatives':[r'\bullet'],'confidence':'medium','reason':'Small bright centre surrounded by a triangular dark patch; intended fill remains uncertain.','crop':'c02_lower_left_graph.png'},
 {'location':'Under upper disk 7, middle vertex','reading':r'\bullet','alternatives':[r'\circ'],'confidence':'medium','reason':'Dark lower mass and rightward upper hook with a light recess.','crop':'c01_upper_middle_vertex.png'},
 {'location':'Lower middle graph, first vertex','reading':r'\bullet','alternatives':[r'\circ'],'confidence':'medium','reason':'The inner triangular recess is gray; black edges enclose it.','crop':'c03_lower_middle_graph.png'},
 {'location':'Last lower graph, first vertex','reading':r'\bullet','alternatives':[r'\circ'],'confidence':'medium','reason':'Black upper mass with a light lower notch/hook.','crop':'c06_lower_graph_and_left_angular.png'},
 {'location':'Bottom second disk, repeated overdrawn strokes','reading':'diagonal cancellation','alternatives':['hatching'],'confidence':'medium','reason':'Crossing and protruding paths are visible; the state remains unresolved.','crop':'c04_overdrawn_disk.png'},
 {'location':'Final middle disk extension/blob and angular foot traces','reading':'visible traces of undetermined origin and role','alternatives':['marks from the other surface'],'confidence':'low','reason':'Graphic shapes are visible but their source and hand cannot be established on this page.','crop':'c05_middle_final_disk.png','additional_crops':['c06_lower_graph_and_left_angular.png','c07_right_angular.png']},
 {'location':'Upper edge and right-middle detached marks','reading':'detached visible marks','alternatives':['transfer or surface flecks'],'confidence':'low','reason':'Shapes are preserved without a character or hand assignment.','crop':'c08_upper_edge_marks.png','additional_crops':['c09_right_pale_marks.png','c10_right_flecks.png']},
 {'location':'Additional pale curve below upper graph 2, trace above upper disk 4, and diagonal between lower disks 1 and 2','reading':'pale visible shape fragments','alternatives':['transfer or surface traces'],'confidence':'low','reason':'No supported word or mathematical-symbol reading; their hand and purpose remain unresolved. The very weak lower continuation in c13 is also unresolved.','crop':'c11_pale_curve_below_top2.png','additional_crops':['c12_pale_slant_between_lower_disks.png','c13_pale_above_top4.png']},
]
raw=json.loads((ROOT/'packets/010/C_inventory.json').read_text())
INV=[]
for i,o in enumerate(raw,1):
 q={k:o[k] for k in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']}
 q['hand']='his hand'
 if i in [1,29,34,50,51]: q['hand']='undetermined hand'
 if i==22: q['first_words_or_objects']='ou'
 if i==33: q['first_words_or_objects']='crossed disk with two lower arches; independent blob and extension listed separately'
 if i==40: q['first_words_or_objects']='two separate edges; first left endpoint open/filled qualification'
 if i==42: q['first_words_or_objects']='repeated diagonal strokes: cancellation/hatching state unresolved'
 if i==46: q['first_words_or_objects']='two joined-edge strokes and isolated dot; first point has local fill uncertainty'
 if i==49: q['first_words_or_objects']='line with four vertices; first point has local fill uncertainty'
 INV.append(q)
def inv(kind,position,objects,hand='undetermined hand'):
 INV.append({'sheet_kind':'text','hand':hand,'element':f'010.B.{len(INV)+1:02d}','kind':kind,'position':position,'first_words_or_objects':objects,'transcribed':'yes'})
inv('drawing','around upper-right variant','large drawn left and right parentheses','his hand')
inv('text','bottom left margin','archive numeral 9; transcribed as % archive sheet number: 9','another unnamed hand')
inv('drawing','final middle disk, left of its crossing','independent dark blob')
inv('drawing','above final middle disk','long broken pale/dark extension')
inv('drawing','final middle disk above its outer lower arch','small detached black spot')
inv('drawing','under upper disk 7 at middle vertex','short projecting upper-right hook','his hand')
inv('drawing','bottom second disk, lower-left boundary','short dark downward tip')
inv('drawing','bottom second disk, lower interior','pale nearly vertical descending trace')
inv('drawing','above upper disk 4','short pale descending trace with darker piece')
inv('drawing','below and right of graph under upper disk 2','pale hooked curve')
inv('drawing','between first and second lower disks','pale broken diagonal')
inv('drawing','above pale curled trace right of middle group','separate pale slanted curve')
inv('drawing','first lower disk interior','pale near-horizontal trace, including its farther-left continuation')
inv('drawing','rightmost angular trace interior','pale rising-right diagonal')
inv('drawing','upper endpoint area of rightmost angular trace','darker short vertical piece')
inv('drawing','left of upper vertical angular-trace fragment','small separate dark spot')
inv('drawing','above-left of right angular trace upper endpoint','small detached gray spot')
inv('drawing','right of right angular trace upper endpoint','small detached gray patch')
inv('drawing','below right angular trace','short detached gray downward dash')

NOTATION=[
 {'location':'above upper disks 3, 7, 8 and lower disks 1, 5','sign':'O followed by K; no punctuation','latex':'OK','confidence':'high'},
 {'location':'top-right parenthesized variant','sign':'rounded o followed by connected u','latex':'ou','confidence':'high'},
 {'location':'between middle group and lower second disk','sign':'heavy bent question shaft and separate lower dot','latex':'?','confidence':'high'},
 {'location':'all small graphs','sign':'unheaded edges, separate dots, and locally uncertain open/filled vertices','latex':r'\bullet, \circ, \unsure{\bullet|\circ}, \unsure{\circ|\bullet}; dash arrows in tikzcd','confidence':'medium'},
 {'location':'under upper disk 8','sign':'three solid corner spots joined on three sides','latex':'triangle with three bullet vertices and unheaded edges','confidence':'high'},
 {'location':'bottom-left margin','sign':'gray archival numeral 9','latex':'% archive sheet number: 9','confidence':'high'},
]
NOTES={
 'page_content':'Three horizontal bands contain 21 disk/oval figures (9 upper, 7 middle, 5 lower) and 12 small associated graphs, grouping braces, two enclosing graph ovals, a parenthesized upper-right variant, five OK labels, ou, and a question mark. No prose sentence or displayed formula is present.',
 'author_uncertainty_exact':['?'],
 'author_uncertainty_location':'The question mark lies below/right of the four-dot middle-left graph and above the overdrawn second lower disk. No accompanying assertion in words is supplied.',
 'title_date_page_counts':'No visible title, date, or manuscript page number. Archive numeral 9 is recorded in a comment and in the inventory. H page 9 corresponds to our scan 10.',
 'H_status':'metadata hua_has=desc. H supplies a descriptive drawing paragraph, including interpretations. It is apparatus for this task; no H text-collation rows or H differences are asserted.',
 'mathematics_led_reading_decisions':'No mathematical computation, proof check, graph-theoretic correspondence, or theorem reconstruction was used. All choices are from visible shapes and page arrangement.',
 'source_section_classification':{
   'Notation table':'Four notation rows, recorded in notation; these are not C doubts.',
   'Doubtful readings':'Five actual rows, mapped exactly once to B01–B05. B02 and B05 span several physical regions; their subordinate shape decisions have C_doubt_status=null.',
   'Abbreviations':'OK expansion/use is apparatus only. The transcription retains OK without expansion.',
   'Legibility':'C approximation remarks are apparatus, checked against the actual drawings.',
   'Steps marked as unverified':'The exact ? and five OK labels were visually checked. This did not produce a mathematical check event.'
 },
 'encoding_notes':'The visible repeated diagonal strokes in the lower second disk are retained. A standard rlap/phantom construction preserves the deleted annotation without drawing an extra generic strike; this encoding-only change is excluded from witness differences. An unsure wrapper records the source cancellation/hatching doubt. The hidden duplicate is a phantom used only for dimensions.',
 'crop_limitations':'No source image or supplied half was reopened or enlarged. Each of the 13 planned crops was made and viewed once. c13 leaves a very weak possible continuation near its lower edge unresolved; no recrop was made. c05 includes clipped context from the adjoining disk and a brace at the edge, while the target final disk and its upper extension are contained. c06 clips only adjoining lower-disk context above its target graph/trace.',
 'surface_marks':'Faint detached shapes are represented graphically, with undetermined hand and purpose. No letter, mathematical role, or writing chronology was assigned to them.',
 'source_checks':'Only direct structural checks are planned/performed. No TeX compiler, format builder, OCR, external source, or other-page image was used.'
}
for q in CROPS:
 q['viewed']=True
 if q['path']=='c13_pale_above_top4.png': q['boundary_note']='A very weak possible continuation approaches the lower edge; unresolved, no recrop.'
REPORT={
 'scan':10,'reader':'B','start_utc':(OUT/'start_utc.txt').read_text().strip(),'end_utc':None,
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'image_view_log':[
  {'source':'source/SP40_CW_81_scans/J81-01_81_scan010.jpg','views':1,'purpose':'layout'},
  {'source':'source/SP40_CW_81_scans/J81-01_81_scan010_a.jpg','views':1,'purpose':'complete left-half reading'},
  {'source':'source/SP40_CW_81_scans/J81-01_81_scan010_b.jpg','views':1,'purpose':'complete right-half reading'}],
 'image_dimensions':{'full':[1680,1208],'a':[900,1208],'b':[900,1208]},
 'half_mapping':'Full image width 1680 and half width 900 give right-half origin x=1680-900=780, y=0. Left-half origin is (0,0). The overlap is 120 pixels. All report boxes are full-image coordinates.',
 'differences':D,'doubts':DOUBTS,'inventory':INV,'notes':NOTES,'notation':NOTATION,'check_events':[], 'crops':CROPS,
 'brief_feedback':[
  'C uncertainty rows for faint marks combine several widely separated physical regions. This report preserves each source row as one C-doubt entry and gives separate local shape decisions with their own evidence.',
  'The conventions allow graphic preservation of faint marks without a glyph, but do not specify a macro for an unresolved hand/origin of a shape. Their geometry is drawn, with explicit qualification in comments, doubts, and inventory.',
  'Generic deleted wrapping of a picture adds a stroke beyond the source cancellation paths. The supplied rlap/phantom pattern preserves the annotation while retaining only the visible diagonal geometry.'
 ]
}
(OUT/'report.json').write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+'\n')
# Compact row-by-row audit of every original drawing group and the added marks.
AUDIT=[
 ('Upper margin','Two small marks above disk 6 are bent traces; shapes revised in B13–B14. Their purpose/hand stays unresolved. The extra pale trace above disk 4 is B17.'),
 ('Upper disk 1 and graph','Oval, one near-vertical dividing stroke, small upper-left doubled trace, and one separate solid point verified on half a.'),
 ('Upper disk 2 and graph','Two slanting inner strokes, small upper-left retracing, and two separated solid points verified. The pale curve farther below/right is added in B16.'),
 ('Upper disk 3 and graph','Two crossing chords, solid crossing, OK above, and short unheaded line below verified. No further letter or punctuation is supplied.'),
 ('Upper disks 4–5 and shared graph','Three near-vertical strokes in disk 4, three curved peripheral cuts in disk 5, shared brace, enclosing oval, and three dots verified across the halves.'),
 ('Upper disk 6 and graph','Narrow oval, crossing strokes, dark crossing, lower curved cut, small top retrace, enclosing graph oval, short line, and isolated dot verified.'),
 ('Upper disk 7 and graph','Three chord strokes, dark central segment, OK, and three-vertex line verified. Middle hooked vertex remains bullet/circle in B04; its projecting hook is preserved in B08.'),
 ('Upper disk 8 and graph','Three crossing directions, dark triangular region, reinforced top arc, OK, and the small triangle with three filled corners verified.'),
 ('Upper variant','ou between the left parenthesis and small crossed oval; both large parentheses, dark central point, outer faint arc, and descending dark extension verified. No graph is supplied below it.'),
 ('Middle disk 1','Four internal near-vertical cuts and pale downward extension from the lower boundary verified.'),
 ('Middle disk 2','Three oblique inner cuts, a short lower arch, lower reinforced marks, and top retrace verified.'),
 ('Middle disk 3','Four peripheral curved cuts and reinforced right/lower boundary verified.'),
 ('Middle left group','Grouping brace and four separate dots verified. Two tiny flecks between groups preserved. Heavy question mark with detached dot read as ?.'),
 ('Middle disk 4','Broad oval, two crossing strokes and dark intersection, two left peripheral bends, and small top-right bend verified.'),
 ('Middle disk 5','Narrow crossed oval, solid crossing, left peripheral curve and lower small arch verified.'),
 ('Middle disk 6','Crossed oval, solid crossing, larger left cut and smaller upper-left loop verified.'),
 ('Middle disk 7','Crossed oval and two lower arches verified. Independent blob and upward extension remain of undetermined role (B02); dark/pale intervals revised (B10). Tiny detached point above outer lower arch added (B09).'),
 ('Middle right group','Long grouping brace with returns/retracing, short unheaded line and two detached points verified. Existing pale curl and two tiny right-side flecks retained as uncertain-origin marks (B05); higher pale slant added (B15).'),
 ('Lower disk 1 and graph','OK, four strokes, two distinct solid crossings, and pale short interior mark verified. Its faint left extension is B19. Two separate graph edges verified: first left endpoint changes primary to open, with filled retained; first right is open; both ends of the second edge are dark. See B01.'),
 ('Lower disk 2','Outline and three discernible underlying strokes remain, with repeated reversing diagonal overdrawn paths. Cancellation/hatching stays unresolved (B03). Small lower dark tip and pale vertical trace added (B11–B12).'),
 ('Lower disks 3–4','Two small ovals with two near-vertical cuts and a bold horizontal central segment each verified; top loop of disk 3 and right loop of disk 4 retained.'),
 ('Lower middle group and graph','Shared grouping brace, first connected-edge sequence and isolated point verified. Left graph vertex has local bullet/circle doubt (B06). Faint slant between lower disks 1–2 added (B18).'),
 ('Lower disk 5 and graph','OK, oval boundary, four strokes and two bold angled segments verified. Four-vertex lower line preserved with first-vertex fill doubt (B07). First angular trace crosses the line and is preserved as a single positioned drawing.'),
 ('Angular traces at foot','Both angular traces retained with unresolved source/role (B02). Additional pale diagonal, dark fragment, detached spots and lower dash at right are B20–B25. No character or mathematical relation is assigned.'),
 ('Archive margin','Gray 9 at lower left is clearly visible on half a; retained only as % archive sheet number: 9 and added to the inventory. No manuscript page-number macro is introduced.')
]
md=['# Scan 010 — independent reader B','',f"Start UTC: {REPORT['start_utc']}",'End UTC: to be filled after structural verification.','',
 'The whole scan and each supplied half were viewed once. All thirteen tight crops were viewed once. This audit concerns only scan 010. H has status `desc`, so all recorded rows have `H=null` and `diff_H=false`.','',
 '## Reading audit','', '| Locus | Readable ink and unresolved qualifications |','| --- | --- |']
md += ['| '+a+' | '+b.replace('|',' / ')+' |' for a,b in AUDIT]
md += ['', '## Source C section classification','',
 '- **Notation table:** four notation rows; no C-doubt count is assigned to them.',
 '- **Doubtful readings:** five source rows, mapped once each to B01–B05. All remain qualified; B01 changes the primary candidate to open. B02 and B05 cover several separated regions and cite their additional crops.',
 '- **Abbreviations:** `OK` remains unexpanded in the transcription.',
 '- **Legibility / Steps marked as unverified:** apparatus checked against the page; the written `?` and five `OK` labels produce no proof-check claim.', '',
 '## Differences and evidence','', '| ID | Locus | Decision | C difference | Evidence |','| --- | --- | --- | --- | --- |']
for d in D:
 md.append('| '+d['id']+' | '+d['location']+' | '+d['reading'].replace('|',' / ')+' | '+str(d['diff_C']).lower()+' | '+(d['readers_crop'] or 'half a, full box '+str(d['bbox']['coordinates']))+' |')
md += ['', '## Inventory audit','', '| Element | Kind | Position | Recorded content | Hand |','| --- | --- | --- | --- | --- |']
for q in INV:
 md.append('| '+q['element']+' | '+q['kind']+' | '+q['position']+' | '+q['first_words_or_objects'].replace('|',' / ')+' | '+q['hand']+' |')
md += ['', '## Crops','', '| File | Full-scan box | Purpose |','| --- | --- | --- |']
for q in CROPS: md.append('| '+q['path']+' | '+str(q['bbox']['coordinates'])+' | '+q['purpose']+' |')
md += ['', '## Limits and checks','',
 'The faint-origin qualifications are retained. The very weak possible continuation toward the lower edge of c13 remains unresolved; no recrop was taken. c05 and c06 include clipped adjoining context, while their target disk/extension and graph/angular trace are retained within the planned boxes.',
 '', 'The source uses a standard `rlap` / `phantom` construction for the overdrawn lower disk so the actual diagonal paths remain the visible cancellation geometry. This encoding-only adjustment is excluded from the witness-difference count. It introduces no macro definition.',
 '', 'No mathematical computation, proof check, correspondence reconstruction, OCR, external source, or TeX compiler was used. `check_events` is empty. Only source structure, macro names, image references and transcription/report agreement are checked.', '']
(OUT/'reading.md').write_text('\n'.join(md))
print(f'Wrote report.json ({len(D)} rows, {len(INV)} inventory items) and reading.md.')
