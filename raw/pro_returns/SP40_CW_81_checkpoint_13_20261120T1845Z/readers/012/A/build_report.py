from pathlib import Path
import json, datetime
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/012/A'
crops=json.loads((out/'crops_manifest.json').read_text())
cp={x['path'].split('/')[-1].split('.')[0]:x['path'] for x in crops}
report={
 'scan':12,'reader':'A','start_utc':'2026-11-20T12:54:24Z','end_utc':None,
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'image_view_order':['whole once','half a once','half b once','11 distinct enlargement crops, each once'],
 'image_dimensions':{'full':[1690,2361],'a':[1690,1260],'b':[1690,1261]},
 'coordinate_system':'All bboxes are on the original full scan, upper-left origin; crop right/bottom bounds are exclusive. Half a begins at y=0; half b begins at y=1100, derived as 2361-1261.',
 'H_status':'text; descriptive drawing and rereading note apply to scan012. The final unnumbered section and its note explicitly refer to feuillet13 and are excluded from this page.',
 'differences':[], 'doubts':[], 'inventory':[], 'notes':[], 'notation':[], 'check_events':[], 'crops':crops,
 'brief_feedback':[]}
D=report['differences']
def diff(id,location,C,H,reading,evidence,kind='drawing or diagram',dc=True,dh=True,confidence='high',crop=None,bbox=None,status=None,source=None,**kw):
 row=dict(id=id,location=location,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,diff_C=dc,diff_H=dh,C_doubt_status=status,readers_crop=crop,bbox=bbox)
 if source: row['source_C_doubt_row']=source
 row.update(kw);D.append(row)
 return row

def doubt(id,location,reading,alternatives,reason,crop,confidence='medium',source=None,**kw):
 row=dict(id=id,location=location,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason,crop=crop)
 if source: row['source_C_doubt_row']=source
 row.update(kw); report['doubts'].append(row)

diff('A012-01','label above fourth top oval',r'\unsure{OK|Ok}','four labels OK (ou ok) in rereading note',r'\unsure{OK|Ok}',
 'The O has a returning upper loop; the following long upright joins an upper diagonal and a short descending hooked branch. The height/branch shape leaves K/k open. The strongest C candidate is retained.',kind='other',dc=False,dh=False,confidence='medium',crop=cp['01_top_right_OK'],bbox=[1456,43,1521,97],status='retained',source='C-D1',tex_anchor=r'at (1490,71){\unsure{OK|Ok}}')
doubt('D-A012-01','label above fourth top oval',r'OK',['Ok'],'Case of final k/K remains unsettled after the one crop.',cp['01_top_right_OK'],source='C-D1',tex_anchor=r'\unsure{OK|Ok}')
diff('A012-02','between the two lower-left miniature ovals',r'\unsure{ou}','variants introduced by ou',r'\unsure{ou}',
 'A compact o-like initial is joined to a low valley and one compressed arch/descending terminal. The word ou remains strongest; the compressed second letter does not settle a fully certain lexical reading.',kind='other',dc=False,dh=False,confidence='medium',crop=cp['02_miniature_ou'],bbox=[176,846,215,867],status='retained',source='C-D2',tex_anchor=r'at (196,861){\unsure{ou}}')
doubt('D-A012-02','between miniature ovals','ou',['unresolved second-letter form'],'The initial bowl and long compressed continuation are visible, but the second letter remains compressed.',cp['02_miniature_ou'],source='C-D2',tex_anchor=r'\unsure{ou}')
diff('A012-03','large overlaid oval in lower-left register','overlaid zigzags; possible cancellation in C-D3, no local unsure in C.tex','disques, hachures, variantes; no local cancellation claim for this oval','overlaid zigzags, with cancellation of the large oval retained as an alternative',
 'The crop shows heavy oblique sweeps and low hooked returns traversing the chords, with ends above and to the right of the rim. The strokes remain graphic; their cancellation function remains open. The connected lower miniature is retained, and the local state marker is placed beside the large-oval height.',kind='other',dc=False,dh=False,confidence='low',crop=cp['03_overlaid_oval'],bbox=[155,562,385,829],status='retained',source='C-D3',tex_anchor='% C-D3 / A012-03',qualification='Same uncertainty as the source row; adding its local graphic unsure marker supplies no independent reading-change count.')
doubt('D-A012-03','overlaid large lower-left oval','overlaid zigzags',['cancellation of the large oval'],'Ink crossings and extensions are clear; their editorial function is unsettled.',cp['03_overlaid_oval'],confidence='low',source='C-D3',tex_anchor='% C-D3 / A012-03',shape_confidence='high')
diff('A012-04','entire lower-right drawing group','all paths drawn; no explicit live/cancelled qualification','Tout le coin inférieur droit, les deux axes en équerre et ce qu’ils renferment (...) est biffé','live drawing primary, cancellation retained as an alternative; every path and endpoint preserved',
 'Long curves carry repeated hook-like terminals and directed ends. The many crossing paths remain separately traceable. Their presence does not settle whether a cancellation also operates on the whole group. The source geometry is retained with local state doubt. H’s cancellation is preserved as an alternative, so this is a qualified disagreement.',kind='deletion state (struck given live or live given struck)',dc=False,dh=True,confidence='low',crop=cp['04_right_group'],bbox=[809,348,1650,1179],tex_anchor='% A012-04',qualification='C supplies graphic geometry without an explicit cancellation assertion; the wrapper alone is not counted against C.')
doubt('D-A012-04','right group and repeated corner lines','live drawing',['whole-group cancellation'],'Arrow-like terminals and crossing curves are legible; the global editorial state remains uncertain.',cp['04_right_group'],confidence='low',tex_anchor='% A012-04',shape_confidence='high')

diff('A012-05','between first dot and heavy tripod','C path 27: upright looping mark','omitted from the enumerated graph list','upright looping mark retained graphically',
 'A pointed upper diagonal, narrow left loop, right rounded loop and descending return are visible. No stable letter reading is supplied.',dc=False,dh=True,crop=cp['10_upper_looping_mark'],bbox=[529,414,556,510],tex_anchor='% C path 27')
diff('A012-06','between lower diagonal quadrilateral and spoked triangle','C path 66: upright zigzag','omitted from the enumerated graph list','three narrow return regions with upper/lower extensions retained graphically',
 'The upper light extension, two compact upper returns, larger diagonal lower return and bottom hook are visible. Their shape is retained without assigning a letter or a mathematical operation.',dc=False,dh=True,crop=cp['11_lower_zigzag'],bbox=[400,901,442,1019],tex_anchor='% C path 66')
diff('A012-07','around the lower-left miniature alternatives','C paths 53,57,58: two parentheses and detached left dash','variants mentioned without the surrounding parenthesis pair or left dash','opening and closing curved strokes and detached left dash retained',
 'Half a shows the opening arc from approximately (54,759) to (56,841), closing arc (387,802) to (379,919), and short dash (25,798) to (34,799).',dc=False,dh=True,crop=None,bbox=[24,757,407,921],tex_anchor='% C path 53',evidence_surface='half a; full-scan coordinates')

new_geometry=[
 ('A012-08','left rim of tall oval in right group',[875,627,885,658],'pale continuation between the darker upper and lower left-rim pieces','A narrow gray descending trace continues through the interval left blank between C paths 33 and 41.','medium'),
 ('A012-09a','bottom return of tall oval in right group',[976,811,996,822],'pale curved return after the small dark lower-rim pieces','A shallow gray return lies beyond the end of C path 61; its far end remains light.','medium'),
 ('A012-09b','lower-right return of tall oval in right group',[994,788,1019,813],'separate pale sloping trace below the dark right-side fragment','The crop retains a light oblique return below C path 55, with an interruption before the low curved piece. The interruption is preserved.','medium'),
 ('A012-10','terminal of upper long descending curve at far right',[1603,908,1623,926],'two pale terminal traces beyond the darker hooked end','The crop shows light terminal wisps beyond the black endpoint contour. Both short traces are drawn without assigning them a further arrow function.','medium'),
 ('A012-11','beside lower portion of right vertical line',[1385,901,1399,912],'thin gray oblique trace beside the vertical','A small gray crossing/oblique continuation projects to the right; its attachment and hand are undetermined.','low')]
for id,loc,box,rd,ev,co in new_geometry:
 diff(id,loc,'absent from C dark contours','tall oval / crossing curves described; fine trace unspecified',rd,ev,dc=True,dh=(id=='A012-11'),confidence=co,crop=cp['04_right_group'],bbox=box,tex_anchor='% '+id,shape_confidence=co,role='unassigned; nearby drawing relation left as seen',hand='undetermined hand' if id=='A012-11' else 'his hand',hand_qualification='provisional attribution for the attached pale contour')

diff('A012-12','pale detached trace below drawing field','absent','absent','pale hooked curve with low leftward foot and short faint neighbouring oblique piece, preserved as drawing',
 'The enlarged gray trace descends from an upper-right shoulder, turns left near its foot and leaves a low near-horizontal tail; a short light oblique piece sits near the turn. The crop establishes a trace but supplies no secure character. Hand, role and surface origin remain undetermined.',confidence='medium',crop=cp['05_lower_pale_trace'],bbox=[383,1286,416,1329],tex_anchor='% A012-12',shape_confidence='medium',hand='undetermined hand',role='unassigned')
doubt('D-A012-12','pale trace in lower blank field','hooked graphical trace',['unassigned surface trace'],'The curve survives enlargement, but no character, authorial role or hand is established.',cp['05_lower_pale_trace'],confidence='low',tex_anchor='% A012-12',shape_confidence='medium')

mark_specs=[
 ('A012-13a','just above first lower triangle',[214,445,220,452],'short detached upright point',cp['08_triangle_gap_marks'],'A narrow dark upright stands above, detached from the triangle tip.'),
 ('A012-13b','between first lower triangle and solid dot',[270,481,275,486],'small gray triangular point',cp['08_triangle_gap_marks'],'The gray compact point lies between the triangle and the already-transcribed larger black dot.'),
 ('A012-14','gap between first black dot and upright looping mark',[450,498,456,506],'small dark point with a faint short upper stem',cp['09_gap_point'],'The crop shows a black compact base and a short gray trace immediately above it. Neither a punctuation role nor a letter is established.'),
 ('A012-15','lower blank field, near horizontal centre',[786,1426,793,1434],'single dark irregular point',cp['06_lower_single_point'],'The shape is a compact dark fleck with a broad lower part. No text accompanies it.'),
 ('A012-16a','lower-right blank field, upper member of pair',[1526,1703,1532,1709],'upper dark point of oblique pair',cp['07_lower_paired_points'],'The upper point is physically separate and northeast of the other point; no colon or relation is supplied.'),
 ('A012-16b','lower-right blank field, lower member of pair',[1521,1710,1527,1716],'lower dark point of oblique pair',cp['07_lower_paired_points'],'The lower point has its own dark triangular/rounded outline and remains detached.'),
 ('A012-17','inside bottom of far-right small oval',[1586,394,1592,400],'small gray point near the inner lower rim',cp['04_right_group'],'The cropped context at the top right contains a distinct small point above the small oval’s lower rim.'),
 ('A012-18','far right below upper horizontal line',[1640,529,1646,536],'small dark point',cp['04_right_group'],'A detached compact point appears below the right horizontal terminal.'),
 ('A012-19','just above upper horizontal line, below and left of square',[904,500,910,507],'small gray point',cp['04_right_group'],'A small pale point stands above the upper horizontal line; it is detached from that line.'),
 ('A012-20','left of upper tip of lower zigzag',[428,899,433,905],'faint compact gray point',cp['11_lower_zigzag'],'The enlarged zigzag context shows a separate light gray point left of the upper tip.')]
for id,loc,box,rd,cr,ev in mark_specs:
 diff(id,loc,'absent','absent',rd,ev,confidence='medium' if id in {'A012-13b','A012-17','A012-19','A012-20'} else 'high',crop=cr,bbox=box,tex_anchor='% '+id,hand='undetermined hand',role='undetermined',surface_origin='undetermined')

points=json.loads((out/'new_half_points.json').read_text())
for id,x,y,rx,ry,tone in points:
 loc=('upper drawing field' if id.startswith('A012-21') else 'lower blank field')+f', point at ({x:g},{y:g})'
 box=[int(x-rx-2),int(y-ry-2),int(x+rx+3),int(y+ry+3)]
 diff(id,loc,'absent','absent','detached point reproduced graphically',
  'The supplied half shows a distinct compact dot/fleck at the stated coordinates. Its visible shape is retained; hand, meaning and surface origin are undetermined.',confidence='medium' if tone>=45 else 'low',crop=None,bbox=box,tex_anchor='% '+id,evidence_surface='half a' if y<1100 else 'half b (origin y=1100)',hand='undetermined hand',role='undetermined',surface_origin='undetermined')
diff('A012-22','far-right sheet edge at main horizontal crease','absent','absent','short oblique near-horizontal dark dash',
 'Half a shows a short dark dash meeting the right paper edge. Crop 04 includes only its left portion; the complete extent is taken from the supplied half. Hand and surface origin remain undetermined.',confidence='medium',crop=None,bbox=[1655,789,1673,798],tex_anchor='% A012-22',evidence_surface='half a; original full-scan coordinates',hand='undetermined hand',role='undetermined',crop_boundary_disclosure='Crop 04 stops at x=1661 and clips the right end of this non-target dash; it has not been recropped.')

# Trace each original doubtful-readings row exactly once, independently from differences or physical counting.
report['source_C_doubt_rows']=[
 {'source_row_id':'C-D1','source_section':'Doubtful readings','source_row_number':1,'source_place':'above upper right oval','source_first_reading':'OK','source_other_readings':['Ok'],'status':'retained','local_loci':[{'location':'fourth top label','difference_id':'A012-01','doubt_id':'D-A012-01','crop':cp['01_top_right_OK'],'bbox':[1456,43,1521,97]}]},
 {'source_row_id':'C-D2','source_section':'Doubtful readings','source_row_number':2,'source_place':'between miniature ovals','source_first_reading':'ou','source_other_readings':['—'],'status':'retained','local_loci':[{'location':'word between lower-left miniature ovals','difference_id':'A012-02','doubt_id':'D-A012-02','crop':cp['02_miniature_ou'],'bbox':[176,846,215,867]}]},
 {'source_row_id':'C-D3','source_section':'Doubtful readings','source_row_number':3,'source_place':'lower-left heavily marked oval','source_first_reading':'overlaid zigzags','source_other_readings':['possible cancellation of the underlying oval'],'status':'retained','local_loci':[{'location':'large oval and its overlaid strokes','difference_id':'A012-03','doubt_id':'D-A012-03','crop':cp['03_overlaid_oval'],'bbox':[155,562,385,829]}],'source_tex_state':'This source doubt occurs in the table despite no unsure marker at the physical locus in C.tex.'}
]
report['abbreviations']=[{'form':'OK','expansion':'okay','location':'three upper labels and one beside lower-left overlaid oval','transcription':'Unexpanded; final upper label remains OK|Ok.'}]

inventory=json.loads((root/'packets/012/C_inventory.json').read_text())
pathmap={1:[2],3:[1],5:[3],7:[4,6,7,8,9,10,11,12,14,15,16,17,19,20,21,22,24],9:[5,13,18],11:[23],12:[30,31],13:[27],14:[29],15:[28],16:[26],17:[35],18:[34,36,40,42,43,44,45,46,47,48,49,50,51],20:[53,57,58],22:[59,63],24:[34],25:[37],26:[68],27:[66],28:[65],29:[25,32],30:[33,41,55,60,61],31:[25,38,39,52,54,56,62,64,67],32:[25]}
for n,item in enumerate(inventory,1):
 item['hand']='his hand';item['sheet_kind']='text';item['transcribed']='yes'
 item['C_inventory_element']=item['element'];item['element']='A012.I%02d'%n
 if n in pathmap:item['source_paths']=pathmap[n]
 if n==18:item['first_words_or_objects']='oval with chords and overlaid zigzags; cancellation function uncertain; all paths retained'
 if n==20:item['first_words_or_objects']='opening and closing parenthesis strokes with detached short left dash'
 if n==24:item['first_words_or_objects']='right miniature oval with radial strokes; its outline is physically in the same contour cluster as the large oval above'
 if n==29:item['first_words_or_objects']='repeated upper horizontal and left descending boundary strokes; visible gap at the corner and retraced returns'
 if n in (29,30,31,32):item['state']='live/cancelled unresolved; qualified by A012-04'
 if n in (13,27):item['role']='unassigned graphic mark; no textual character supplied'
 if n==8:item['first_words_or_objects']='OK|Ok, final letter case uncertain'
 if n==23:item['first_words_or_objects']='ou, compressed second letter uncertain'
report['inventory']=inventory
report['inventory'].append({'sheet_kind':'text','hand':'undetermined hand','element':'A012.I33','kind':'text','position':'bottom left, full-scan bbox [27,2302,74,2333]','first_words_or_objects':'archive numeral 11','transcribed':'yes','representation':'% archive sheet number: 11'})
for j,row in enumerate([d for d in D if d['diff_C']],34):
 report['inventory'].append({'sheet_kind':'text','hand':row.get('hand','undetermined hand'),'element':'A012.I%02d'%j,'kind':'drawing','position':row['location'],'first_words_or_objects':row['reading'],'transcribed':'yes','difference_id':row['id'],'bbox':row['bbox'],'role':row.get('role','unassigned'), 'tex_anchor':row.get('tex_anchor')})

report['notation']=[
 {'location':'four short approval labels','written_form':'OK; final upper occurrence OK|Ok','latex':r'OK; \unsure{OK|Ok}','evidence':'Separate looped O and K-like upright/branches; four occurrences visually counted.','status':'last occurrence retains case doubt'},
 {'location':'four alternative labels','written_form':'ou','latex':r'ou; final lower occurrence \unsure{ou}','evidence':'Joined o and low u/terminal; the lowest inter-miniature occurrence is compressed.','status':'one local word doubt retained'},
 {'location':'middle narrow looping and lower zigzag marks','written_form':'graphic loops/returns','latex':'TikZ paths 27 and 66','evidence':'Complete strokes examined at crops 10 and 11; no secure letter assignment.','status':'graphic form retained'},
 {'location':'second top oval','written_form':'open rings at the upper/lower middle line; crossed right endpoints; filled outer crosspiece endpoints','latex':'C path 3 retained in TikZ','evidence':'Each local rim, filled end and crossing stroke checked on half a.','status':'graphic endpoint distinctions preserved'},
 {'location':'right-group boundary and curves','written_form':'repeated boundaries, hooks, detached arrow-like strokes and short dashes','latex':'TikZ paths 25,32,33,38,39,41,52,54,55,56,60,61,62,64,67 with pale additions','evidence':'Complete crop 04 includes endpoints, visible interruptions and local returns.','status':'geometry preserved, group cancellation uncertain'},
 {'location':'lower blank field near (400,1307)','written_form':'pale hooked trace','latex':'local unsure TikZ drawing A012-12','evidence':'The crop preserves the curve, foot and light oblique neighbour without supplying a numeral.','status':'hand, role and surface origin undetermined'}
]
report['notes']=[
 {'type':'page_content','text':'A sheet of drawings: four principal upper ovals with two small alternatives; lower triangle/dot, tripod, quadrilateral and triangle with stem; two left ovals plus parenthesized miniature variants; central divided oval; lower quadrilateral with diagonal and spoked triangle; right group of two oval outlines and extended crossing curves beside repeated boundary strokes.'},
 {'type':'text_audit','text':'There are four OK-family labels and four ou-family labels. Their actual spellings and local doubts are retained. H’s initial count three is explicitly corrected to four by its own rereading note; the integrated H reading therefore agrees with the visible count.'},
 {'type':'author_uncertainty','exact_words':[],'text':'No independent question mark or prose statement of uncertainty is visible. The unsure markers in reading.tex are editorial qualifications.'},
 {'type':'title_date_page','text':'The scan carries archive numeral 11 at bottom left. It has no title or date in the main drawing field. No manuscript-page macro is supplied for this archive numeral.'},
 {'type':'H_boundary','text':'H.tex has text status for this packet. Its drawing description and rereading note are collated. Its terminal unnumbered section Décompositions n-aires (et découpages) d’espaces topologiques and following note expressly locating that wording on feuillet13 remain contextual apparatus and are excluded from scan012.'},
 {'type':'graphic_state','text':'The original C-D3 table already qualifies the overlaid lower-left oval, although C.tex lacks a local unsure. The proposed local marker carries that same existing doubt. The right group is also locally qualified for live/cancelled state; H’s cancelled reading remains an explicit alternative.'},
 {'type':'mathematics_led_reading','text':'No expression, object assignment or morphism is supplied to identify these unlabeled drawings. The graph shapes, edge multiplicities, rims, fills and drawn directions are transcribed from their strokes. No mathematical computation or theorem check was performed.'},
 {'type':'faint_marks','text':'Distinct detached traces and points are represented graphically, with hand, role and surface origin left undetermined. Gray paper texture that supplies no stable stroke or character has not been converted into invented writing.'},
 {'type':'source_path_audit','text':'All 68 original C filled contour commands and all 8 original label nodes are retained. The two state-qualified contour clusters are boxed locally without a generic added cancellation stroke. Pale missing continuations and detached marks receive separate explicit paths.'},
 {'type':'crop_boundary','text':'Crop 03 retains the complete targeted large oval and its overlay extensions; adjacent lower miniature outlines continue beyond its lower boundary and are read from half a. Crop 04 retains the entire targeted right group; its right boundary clips only the separate edge dash, whose whole extent is documented from half a.'},
 {'type':'validation','text':'Validation is structural source inspection only: braces, environments, macro names, path retention, crop references and report/transcription anchors. No compiler or rendering was used.'}
]
report['brief_feedback']=[
 'H’s metadata status text accompanies a descriptive drawing and a tail belonging to a later sheet; the boundary is explicit in its own note and has been disclosed.',
 'Graphic cancellation function can remain unresolved while all paths are secure. The local unsure wrapper preserves the paths without supplying a generic horizontal strike.',
 'The brief does not give a numeric threshold for paper specks. Distinct stable traces/points are retained graphically with unknown origin; texture without a supported stroke receives no character.'
]
# The local graphic doubt apparatus also records every detached mark's open attribution/role.
doubt('D-A012-11','beside lower portion of right vertical line','thin gray oblique trace',['attachment, hand and surface origin unresolved'],'A small oblique trace is visible beside the vertical; its precise attachment is weak.',cp['04_right_group'],confidence='low',tex_anchor='% A012-11',bbox=[1385,901,1399,912])
for row in D:
 if row['id'].startswith(('A012-13','A012-14','A012-15','A012-16','A012-17','A012-18','A012-19','A012-20','A012-21','A012-22','A012-23')):
  doubt('D-'+row['id'],row['location'],row['reading'],['hand, role and surface origin unassigned'],row['evidence']+' Shape confidence and interpretation confidence are recorded separately.',row['readers_crop'],confidence='low',tex_anchor=row['tex_anchor'],shape_confidence=row['confidence'],bbox=row['bbox'],evidence_surface=row.get('evidence_surface','crop'))
report['summary_counts']={'original_C_doubt_rows':3,'original_C_doubt_rows_retained':3,'original_C_doubt_rows_resolved':0,'crops':len(crops),'C_original_paths_retained':68,'original_text_labels':8,'difference_rows':len(D),'rows_diff_C':sum(d['diff_C'] for d in D),'rows_diff_H':sum(d['diff_H'] for d in D)}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

# Compact audit follows the physical registers and gives an exhaustive original-path map.
audit=['# Independent reading audit — scan 012, reader A','',
 'Start UTC: 2026-11-20T12:54:24Z. The whole scan, half a and half b were each viewed once, in that order. Eleven distinct enlargement crops were then viewed once each. No further whole/half views or recrops were made.',
 '', '## Witness boundary','',
 'H has text status in metadata. Its descriptive drawing and rereading note apply here. Its final unnumbered section and note expressly locate their wording on feuillet13; that tail is contextual and excluded from the scan012 transcription and collation.',
 '', '## Reading by physical register','',
 '| Register / local item | Reading audit | Source geometry / evidence |',
 '| --- | --- | --- |',
 '| Upper left oval | Rim, three long straight divisions, hatched triangular region and lower curved cap retained. The nearby word is `ou`. | C path 2; half a. |',
 '| Small upper alternative | Small oval with central filled junction and separate spokes, including lower curled/open feature retained. | Path 1; half a. |',
 '| Second upper oval and label | `OK`; three upright strands, heavy crosspiece, filled outer ends, middle open-ring ends and crossed right ends retained at their local positions. | Path 3; half a. |',
 '| Third upper oval and label | `OK`; long slanted divisions and densely hatched quadrilateral retained, including detached small hatch pieces. | Paths 4, 6–12, 14–17, 19–22, 24; half a. |',
 '| Fourth upper oval and label | `OK|Ok` remains uncertain. Hatched triangle, heavy segment to right and narrow right strip retained. | Paths 5, 13, 18; crop 01 for label. |',
 '| Far-right small alternative | `ou`; divided small oval and heavy radial segment retained. A small inner lower point is added with unknown hand/role. | Path 23; half a and contextual upper right of crop 04. |',
 '| First lower triangle and dot | Triangle with tip extensions and distinct solid dot retained. Short upright point above tip and small gray intermediate point added. | Paths 30–31; crop 08. |',
 '| Gap before tripod | Upright looping mark remains graphic. A separate dark point with pale upper stem is added farther left. | Path 27; crops 09–10. |',
 '| Heavy tripod | All three arms and filled terminal ends retained. | Path 29; half a. |',
 '| Square and triangle with stem | Local gaps/retraces and thick stem retained. | Paths 28 and 26; half a, crop 04 context. |',
 '| Second-register far-left oval | Crossing divisions and two dark wedge regions retained. | Path 35; half a. |',
 '| Large overlaid lower-left oval | Underlying rim/chords and all overlaid zigzags retained. Cancellation remains an alternative; local graphic uncertainty is explicit. Adjacent `OK` retained. | Paths 34, 36, 40, 42–51; crop 03. |',
 '| Parenthesized miniature variants | Detached left dash, opening/closing curves, first `ou`, both ovals and spokes retained. Inter-miniature `ou` remains uncertain. | Paths 53, 57–59, 63 and lower miniature part of path 34; crop 02. |',
 '| Central divided oval | Rim, convergent divisions and triangular hatching retained. | Path 37; half a. |',
 '| Lower quadrilateral and diagonal | Both boundaries and rising diagonal retained. | Path 68; half a. |',
 '| Lower narrow zigzag | Pointed light upper extension, three return regions and final hook retained graphically. Tiny gray neighbour at top separately added. | Path 66; crop 11. |',
 '| Lower spoked triangle | Outer triangle, central junction and three internal arms, including lower-right overrun, retained. | Path 65; half a. |',
 '| Right boundary and extended curves | Repeated upper/left boundary strokes, open corner gap, all long curves, hooked terminals, detached short arrow and dashes retained. Live/cancelled state remains open. | Paths 25, 32, 38–39, 52, 54, 56, 62, 64, 67; crop 04. |',
 '| Right tall oval | Four crossing divisions and separate/dim rim parts retained. Pale left-rim and lower-right return fragments missing from C’s dark contours are added. | Paths 33, 41, 55, 60–61; crop 04. |',
 '| Right low oval | Outer low outline and curved chords/overruns retained together with the extended crossing line. | Path 25; crop 04. |',
 '| Lower blank field | Pale hooked trace and distinct isolated points retained graphically; their hand, role and surface origin remain undetermined. | Crops 05–07 and half b; every local point has a report bbox. |',
 '| Archive numeral | `11`, recorded solely as an archive comment. | Bottom left, half b. |',
 '', '## Original C doubt source rows','',
 '| Source row | Local locus | Decision | Crop |', '| --- | --- | --- | --- |',
 '| C-D1, row 1 | Fourth upper label | Retain `OK|Ok`. The short hooked final branch leaves case unsettled. | 01 |',
 '| C-D2, row 2 | Word between miniatures | Retain `ou` with doubt. The second continuation remains compressed. | 02 |',
 '| C-D3, row 3 | Large lower-left oval overlays | Retain overlaid zigzags / possible cancellation. The table row is mapped even though C.tex has no local unsure. | 03 |',
 '', 'The three notation-table rows and the abbreviation-table row are kept in their source categories. They are not additional C doubts. No compound source row is collapsed into a neighbouring locus.',
 '', '## Every reported difference','',
 '| ID | Local reading / qualification | C change | H change | Evidence |', '| --- | --- | --- | --- | --- |']
for row in D:
 reading=row['reading'].replace('|',' / ').replace('\n',' ')
 evidence=row['readers_crop'] or row.get('evidence_surface','supplied half')
 audit.append('| '+row['id']+' | '+row['location']+': '+reading+' | '+str(row['diff_C']).lower()+' | '+str(row['diff_H']).lower()+' | '+evidence+'; bbox '+str(row['bbox'])+' |')
audit.extend(['','## Remaining qualifications','',
 'The original three C doubts remain. The right group additionally retains a live/cancelled-state qualification. Detached specks and pale traces have explicit shape records but no established textual or mathematical role, hand or surface origin. Their local graphical unsure wrappers mark those open qualifications. The two larger narrow looping/zigzag marks are preserved as drawings without an invented character.',
 '', '## Source and validation audit','',
 'All 68 C contour commands were read and assigned to the physical groups above; the path index file preserves their exact source bounds and subpath counts. All are retained once in reading.tex. The eight label nodes are retained, with the original two lexical doubts. Additional pale paths and detached marks have their own source comments matching report IDs. No mathematical computation was performed; check_events is empty.',
 '', 'The source checks inspect balanced braces, matching environments, known macros, original-path retention, text-label retention, crop existence, all three source-row mappings and the current report/TeX anchors. There is no compilation or rendering claim.',
 '', 'Crop 03 includes the complete target overlay and rim; the adjacent miniature extends below its boundary and was read on half a. Crop 04 includes the complete right drawing group; a separate paper-edge dash extends past that crop’s right boundary and is recorded from half a. No crop was repeated.',
 ''])
(out/'reading.md').write_text('\n'.join(audit))
print('Report:',len(D),'difference/audit rows;',len(report['inventory']),'inventory items;',len(report['doubts']),'local doubt records.')
