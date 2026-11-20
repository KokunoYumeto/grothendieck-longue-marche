from pathlib import Path
import json
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[3]
crops=json.loads((BASE/'crop_plan.json').read_text())
by_crop={c['path']:c for c in crops}
for c in crops:
 c['coordinate_system']='original full scan, upper-left origin, pixels; right and lower bounds exclusive'
 c['viewed_once']=True
 if c['path']=='crop_04_middle_final_disk.png':
  c['boundary_note']='Target disk, detached blob, upper long trace and lower arches are complete. A neighboring portion of the long grouping brace meets the lower crop boundary; the complete brace was settled on the supplied halves.'
 elif c['path']=='crop_05_left_foot_trace.png':
  c['boundary_note']='The target foot trace and complete four-vertex graph are included; the bottom of the neighboring disk enters the upper margin as context.'
 elif c['path']=='crop_11_upper_variant_disk.png':
  c['boundary_note']='The complete target variant disk, descending trace and closing parenthesis are included. A small tail of the already-settled ou is visible at the left crop boundary.'

diffs=[]
def row(id,location,C,reading,evidence,confidence='medium',kind='drawing or diagram',diff_C=True,doubt=None,crop=None,bbox=None,**extra):
 d=dict(id=id,location=location,C=C,H=None,reading=reading,evidence=evidence,confidence=confidence,kind=kind,diff_C=diff_C,diff_H=False,C_doubt_status=doubt,readers_crop=crop,bbox=dict(image='J81-01_81_scan010.jpg',origin='upper left',xyxy=bbox) if bbox else None)
 d.update(extra);diffs.append(d)
row('A010-D01','First endpoint of the first lower-left segment',r'\unsure{\bullet|\circ}',r'\unsure{\circ|\bullet}','The left black triangular rim contains a distinct light triangular centre. The right endpoint has a larger enclosed white centre. The smaller left opening supports the open candidate first, while uneven filling remains supported.',kind='misread symbol or index',doubt='retained',crop='crop_01_lower_left_graph.png',bbox=[128,1028,149,1048],source_section='Doubtful readings',source_row=1)
row('A010-D02','Final middle disk and the two angular traces at the foot','faint strokes; alternative: marks from the other surface','Visible strokes and blob retained graphically; their origin remains unresolved.','The long upper trace above the final middle disk has dark and pale separated portions. The foot traces likewise have dark brown-black angular parts and pale continuations. Their visible outlines do not determine which surface produced them.',confidence='low',kind='other',diff_C=False,doubt='retained',crop='crop_04_middle_final_disk.png',bbox=[1264,309,1430,604],additional_crops=['crop_05_left_foot_trace.png','crop_06_right_foot_trace.png'],source_section='Doubtful readings',source_row=2,qualification='One source doubt row covers these separated physical places; counted once. Local additions are reported separately.')
row('A010-D03','Second disk of the bottom row','diagonal cancellation; alternative: hatching','Diagonal cancellation primary, hatching alternative retained.','Several long diagonal strokes return at the lower left and extend past parts of the outline. This supports the cancellation reading but leaves the hatching interpretation open. The underlying oval and three crossing strokes remain represented.',kind='other',diff_C=False,doubt='retained',crop='crop_03_overdrawn_disk.png',bbox=[444,703,652,933],source_section='Doubtful readings',source_row=3,qualification='The original C.tex has no unsure macro here; this remains an actual source-table doubt. The supplied deletion macro is retained invisibly while the physical diagonal strokes remain visible once.')
row('A010-D04','Middle vertex under upper disk 7',r'\unsure{\bullet|\circ}',r'\unsure{\bullet|\circ}','The centre consists of a thick black lower-left mass and a short arched return on its upper right, with a white pocket open to the right. The two line portions stop short around it. Its point-versus-open-circle reading remains unsettled.',kind='other',diff_C=False,doubt='retained',crop='crop_02_upper_path_vertex.png',bbox=[1148,243,1170,261],source_section='Doubtful readings',source_row=4)
row('A010-D05','Detached marks near the upper edge and to the right of the middle group','detached marks; alternative: transfer or surface flecks','Detached graphical marks retained; hand, intention and surface origin unresolved.','The upper pair contains a shallow curved stroke and an angular short stroke. The right middle group has a pale open curve, a smaller pale bent trace above it, and two separated dark flecks below. No character is supplied for these residual shapes.',confidence='low',kind='other',diff_C=False,doubt='retained',crop='crop_07_upper_detached_marks.png',bbox=[995,10,1065,57],additional_crops=['crop_08_pale_right_trace.png','crop_09_right_flecks.png'],source_section='Doubtful readings',source_row=5,qualification='One source doubt row covers these separated places; counted once. Changes to their explicit geometry have separate rows.')
row('A010-D06','Left endpoint of the three-vertex path below the lower-middle group',r'\bullet',r'\unsure{\circ|\bullet}','A small pale triangular centre sits within the dark left endpoint. The centre and right endpoint are visibly filled. The small left centre supports the open candidate while partial filling remains a supported reading.',kind='misread symbol or index',crop='crop_10_lower_middle_graph.png',bbox=[468,1018,491,1037])
row('A010-D07','Left endpoint of the four-vertex path below the final bottom disk',r'\bullet',r'\unsure{\circ|\bullet}','The left endpoint has a dark upper arch and lower returns surrounding a light lower pocket. Its outline remains open at the bottom. The other three vertices are heavy filled marks.',kind='misread symbol or index',crop='crop_05_left_foot_trace.png',bbox=[977,1022,1005,1044])
row('A010-D08','Inside final middle disk, between the detached blob and the outer lower arch','omitted','Small isolated dark spot drawn.','A separate compact black spot occurs above the left part of the outer lower arch, with paper visible between it and the neighboring strokes.',confidence='high',crop='crop_04_middle_final_disk.png',bbox=[1308,536,1324,552])
row('A010-D09','Upper variant disk, alongside the long downward stroke','Several small detached fragments omitted','Short dark fragments and two small dots drawn beside the descending stroke.','The crop retains short separate vertical pieces to the right below the central intersection, a small spot to the left farther down, and a small lower spot beside the long continuation. Their positions remain graphical; no symbol or function is assigned.',crop='crop_11_upper_variant_disk.png',bbox=[1578,170,1605,239])
row('A010-D10','Two marks at the upper page edge','Two short straight paths at (1018,28)--(1025,29) and (1037,27)--(1046,26)','First path made shallowly cup-shaped; second given angular raised ends.','The enlarged first trace curves down and back up. The second has a short horizontal body with raised or hooked ends. The stroke shapes are preserved without choosing letters.',crop='crop_07_upper_detached_marks.png',bbox=[1014,22,1052,34])
row('A010-D11','Above and right of the pale curve in the middle-right open space','omitted','Small pale bent trace drawn.','The crop shows a short descending bent gray trace above-right of the larger open curve. Its extremities are faint, and it supplies no stable character candidate.',confidence='low',crop='crop_08_pale_right_trace.png',bbox=[1563,345,1586,364])
row('A010-D12','Interior of the far-right angular foot group','omitted','Faint oblique residual trace drawn with approximate endpoints.','A pale oblique line rises toward the right from near the left portion of the dark lower angular line. It lies inside the larger visible group and fades at both extremities.',confidence='low',crop='crop_06_right_foot_trace.png',bbox=[1438,970,1510,1043])
row('A010-D13','Below the far-right angular foot group','omitted','Short detached slanted vertical stroke drawn.','A small gray-dark near-vertical mark sits below the left-middle part of the angular group; it is detached from its lower edge.',confidence='medium',crop='crop_06_right_foot_trace.png',bbox=[1430,1082,1444,1105])
row('A010-D14','Upper part of the right upright continuation of the far-right foot group','Only a uniformly faint path','A short darker upper piece and a separate spot retained along the faint continuation.','Near the upper-right extremity, a dark short upright piece and separated darker spot are visible amid the faint vertical trace.',crop='crop_06_right_foot_trace.png',bbox=[1562,901,1578,929])
row('A010-D15','Open space to the right of the two dots under top disk 2','omitted','Faint open curved residual trace drawn.','The single enlargement shows an upper descending curved run and a lower leftward return. The trace is pale and irregular; it supports a graphical contour without a letter reading.',confidence='low',crop='crop_13_upper_left_pale_curve.png',bbox=[398,238,428,280])
row('A010-D16','Open space between bottom disks 1 and 2','omitted','Faint diagonal trace and its darker fragments drawn.','A descending-right gray trace passes through several darker small segments and fades at its lower endpoint. No character candidate is supported.',confidence='low',crop='crop_14_lower_left_pale_diagonal.png',bbox=[365,739,419,791])
row('A010-D17','Far-right margin beside the bottom row','omitted','Small pale bounded patch drawn.','The crop shows an irregular bounded pale patch with a slightly darker contour and uneven corners. Its origin and intention remain undetermined; no letter or number is supplied.',confidence='low',crop='crop_15_far_right_pale_patch.png',bbox=[1627,784,1650,810])
row('A010-D18','Inside bottom disk 1, left of the right-hand intersection','Only the darker short trace at (276,827)--(293,828)','Faint horizontal continuation from approximately (249,826) to (276,827) retained.','The supplied left half shows a pale nearly horizontal extension leading into the darker short dash. Its path and endpoints were sufficiently visible on that half; no enlargement was made for this settled locus.',confidence='medium',bbox=[245,818,297,835],half_evidence=dict(image='J81-01_81_scan010_a.jpg',origin='upper left',xyxy=[245,818,297,835]))
row('A010-D19','Just below the lower-left circumference of bottom disk 2','omitted','Small dark hanging trace drawn.','The cancellation crop shows a narrow dark drop-like piece protruding just below the oval near its lower-left part. It is kept with the same graphical disk.',confidence='high',crop='crop_03_overdrawn_disk.png',bbox=[483,908,497,923])

inventory=json.loads((ROOT/'packets/010/C_inventory.json').read_text())
for item in inventory:
 item.pop('cote',None);item.pop('scan',None)
 item['hand']='his hand'
 if item['element'] in ('010.01','010.29','010.34','010.50','010.51'):
  item['hand']='undetermined hand'
 if item['element']=='010.40':
  item['first_words_or_objects']='two separate edges; first left endpoint open/filled uncertainty retained'
 if item['element']=='010.46':
  item['first_words_or_objects']='three-vertex path with uncertain open/filled left endpoint, plus isolated dot'
 if item['element']=='010.49':
  item['first_words_or_objects']='four-vertex path with uncertain open/filled left endpoint'
 if item['element']=='010.42':
  item['first_words_or_objects']='repeated diagonal strokes: cancellation primary, hatching alternative retained'
 if item['element']=='010.34':
  item['first_words_or_objects']='pale larger curl, added smaller bent trace above-right, and two small dark flecks'
extra_inventory=[
 ('010.52','text','lower-left page edge','9; archive sheet number preserved only in a TeX comment','another unnamed hand'),
 ('010.53','drawing','inside final middle disk above the lower arch','small detached dark spot','undetermined hand'),
 ('010.54','drawing','beside descending stroke inside/below top variant disk','short dark fragments and separate spots','undetermined hand'),
 ('010.55','drawing','inside far-right angular foot group','faint internal oblique trace','undetermined hand'),
 ('010.56','drawing','below far-right angular foot group','short detached slanted vertical stroke','undetermined hand'),
 ('010.57','drawing','upper-right continuation of far-right foot group','short dark upright fragment and separated spot','undetermined hand'),
 ('010.58','drawing','right of the two dots below top disk 2','faint open curved residual trace','undetermined hand'),
 ('010.59','drawing','between bottom disks 1 and 2','faint descending-right residual line','undetermined hand'),
 ('010.60','drawing','far-right margin alongside the bottom row','pale bounded irregular patch','undetermined hand'),
 ('010.61','drawing','inside bottom disk 1 left of right intersection','pale horizontal continuation into the darker dash','undetermined hand'),
 ('010.62','drawing','below lower-left circumference of bottom disk 2','small dark hanging trace','undetermined hand')
]
for element,kind,position,first,hand in extra_inventory:
 inventory.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))

report=dict(scan=10,reader='A',start_utc='2026-11-20 11:48:41 UTC',end_utc=None,full_image_viewed=True,halves_viewed=True,complete_visual_read=True,differences=diffs,doubts=[
 dict(location='first endpoint of first lower-left edge',reading=r'\circ',alternatives=[r'\bullet'],confidence='medium',reason='Distinct small light centre within heavy rim; irregular filling remains possible.',crop='crop_01_lower_left_graph.png'),
 dict(location='middle vertex below upper disk 7',reading=r'\bullet',alternatives=[r'\circ'],confidence='medium',reason='Black mass with upper hooked return and white pocket open on the right.',crop='crop_02_upper_path_vertex.png'),
 dict(location='bottom disk 2 state',reading='cancellation',alternatives=['hatching'],confidence='medium',reason='Repeated diagonal returns and overshoots remain compatible with both named states.',crop='crop_03_overdrawn_disk.png'),
 dict(location='final middle disk and angular foot traces',reading='visible strokes reproduced geometrically',alternatives=['marks from the other surface'],confidence='low',reason='The photographed surface and faint discontinuities do not establish the physical origin.',crop='crop_04_middle_final_disk.png'),
 dict(location='upper-edge marks and middle-right detached traces',reading='detached graphical marks',alternatives=['transfer or surface flecks'],confidence='low',reason='Their hand, intention and surface origin remain unestablished.',crop='crop_07_upper_detached_marks.png'),
 dict(location='left endpoint of lower-middle path',reading=r'\circ',alternatives=[r'\bullet'],confidence='medium',reason='Small gray triangular centre within dark rim.',crop='crop_10_lower_middle_graph.png'),
 dict(location='left endpoint of final lower path',reading=r'\circ',alternatives=[r'\bullet'],confidence='medium',reason='Hooked open lower pocket; filling interpretation remains uncertain.',crop='crop_05_left_foot_trace.png'),
 dict(location='new pale residual contours and bounded patch',reading='visible geometry only',alternatives=['transfer','surface mark'],confidence='low',reason='The crops support contours but do not establish a character, hand or intention.',crop='crop_13_upper_left_pale_curve.png',additional_crops=['crop_14_lower_left_pale_diagonal.png','crop_15_far_right_pale_patch.png'])
],inventory=inventory,notes={
 'page_content':'Three rows of outlined disks with straight or curved internal strokes, filled intersections or short heavy regions, grouping braces and small graphs. Five OK labels, one ou within drawn parentheses, one heavy question mark, and archive numeral 9.',
 'author_uncertainty_exact_words':['?'],
 'title_date_page_counts':'No title or date observed. One scanned sheet. The numeral 9 at the lower left is retained only as the archive-sheet comment; no mspage value supplied.',
 'mathematics_led_reading_decisions':[],
 'H_classification':'metadata hua_has=desc. H is an editorial description rather than full page text; every H field is null and diff_H is false. No H textual collation rows were invented.',
 'source_section_classification':{'Notation table':'Four rows concerning OK, graph marks, ?, and the parenthesized ou. They are notation entries, not C doubts.','Doubtful readings':'Five actual rows, mapped once each to A010-D01 through A010-D05. Rows 2, 3 and 5 remain actual doubts although C.tex has no unsure macro at all their places.','Abbreviations':'One row, OK; recorded as the literal label, without expansion.','Legibility':'One scan010 statement, treated as an editorial legibility note.','Steps marked as unverified':'The note reports five OK labels and one ?; it supplies no mathematical check.'},
 'cancellation_implementation':'Physical diagonal strokes remain visible once. The same drawing also occurs in a phantom deleted box to retain the supplied cancellation annotation without a generic added horizontal strike. This boxing-only change is not counted as a witness-reading difference.',
 'image_order':'UTC start recorded before packet reading; packet/conventions read, whole source viewed once, left half once, right half once, then each of 15 distinct crops viewed once. No full or half source was reopened.',
 'structural_validation':'Pending source-only validation. No TeX compiler, format builder, renderer, OCR, research or delegated reader was used.',
 'drawing_limit':'TikZ is an approximation of the visible geometry. The very pale internal foot trace has approximate endpoints; its crop records the source. Black/gray intensity differences are graphical observations, with no semantic role assigned.'
},notation=[
 dict(location='above top disks 3, 7, 8 and bottom disks 1, 5',visible_form='round O followed by two-armed K; no terminal punctuation',latex='OK',confidence='high'),
 dict(location='between large left parenthesis and top variant disk',visible_form='joined lowercase ou',latex='ou',confidence='high'),
 dict(location='above bottom disk 2',visible_form='heavy bent upper stroke and detached lower spot',latex='?',confidence='high',crop='crop_12_question_mark.png'),
 dict(location='under disks and disk groups',visible_form='filled dots, uncertain hollow centres, unheaded connectors',latex=r'\bullet, \circ, \unsure{\circ|\bullet}, dash edges in tikzcd',confidence='medium'),
 dict(location='beneath three grouped sets of disks and beneath upper disks 4–5',visible_form='long curved grouping braces with central cusp',latex='explicit TikZ paths',confidence='high'),
 dict(location='lower-left edge',visible_form='pencilled 9',latex='% archive sheet number: 9',confidence='high')
],check_events=[],crops=crops,brief_feedback=[
 'The available inventory sheet_kind choices do not include a dedicated drawing sheet; text is retained for this drawing-only sheet.',
 'A source doubtful-reading row can concern several disconnected places. It was counted once, with multiple crop references and independent local difference rows where needed.',
 'The brief permits undetermined hand for detached marks; this was used for pale residual contours, small flecks and uncertain-origin traces. Their graphical contours carry no supplied letter or semantic role.',
 'The cancellation-versus-hatching doubt is preserved in report and source comments while the primary deletion annotation remains in the TeX boxing. No new macro was defined.'
],image_dimensions={'full':[1680,1208],'a':[900,1208],'b':[900,1208],'b_full_scan_offset':[780,0]})
(BASE/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

lines=['# Scan 010 — independent reader A','',
'UTC start: 2026-11-20 11:48:41 UTC. This sheet has no running prose lines; the audit follows its rows and separately drawn objects. The whole image and each supplied half were viewed once. All boxes below use the original 1680 × 1208 scan with upper-left origin; half b starts at full-scan x = 780.','',
'## Reading audit','',
'| Locus | Visible reading / graphical audit | Remaining qualification |',
'| --- | --- | --- |',
'| Upper edge | Two detached short shapes: a shallow curved first stroke and angular-ended second stroke. Their explicit paths are revised. | Hand, intention and surface origin remain unresolved; crop 07. |',
'| Upper disk 1 and graph | One near-vertical internal cut, small upper-left retracing, and a single solid point below. | Readable on half a; C retained. |',
'| Upper disk 2 and graph | Two slanting cuts, upper-left short marks, and two separated solid points below. A faint open residual curve sits farther right. | Main drawing settled on half a; added pale curve in crop 13 has no character reading. |',
'| Upper disk 3 and graph | Two crossing lines, filled intersection, literal OK above, and a short unheaded horizontal line below. | Readable on half a; C retained. |',
'| Upper disks 4–5 and their group | Three near-vertical cuts in one disk and three curved peripheral cuts in the other. Shared brace above an oval containing three dots. | Group boundary and all three dots retained from halves. |',
'| Upper disk 6 and graph | Narrow oval, one black intersection, peripheral lower arc; encircling oval below with a line and separated dot. | Readable on half b; C retained. |',
'| Upper disk 7 and graph | Three crossing internal strokes with a heavy short middle piece; literal OK above. Below: two line portions and three vertices, central vertex strongly hooked. | Central vertex remains bullet/circle uncertainty; crop 02. |',
'| Upper disk 8 and graph | Three crossing strokes with a filled triangular interior region; literal OK above. Below: a triangle with three filled corners. | Readable on half b; C retained. |',
'| Upper variant disk | Literal ou between left parenthesis and small crossed oval; a closing parenthesis extends far down. Main black central point, several internal strokes, long dark continuation below, small side fragments and dots. | Added detached fragments from crop 11 have no assigned role. |',
'| Middle disk 1 | Four near-vertical cuts; small upper-left marking and pale continuation below one lower endpoint. | Main geometry settled on half a. |',
'| Middle disk 2 | Three slanting internal cuts, a small lower arch, and short retracings at top and bottom. | Settled on half a. |',
'| Middle disk 3 | Four peripheral arcs with a broad dark lower-right outline. | Settled on half a. |',
'| First middle group | Long brace below disks 1–3; four separated dots underneath. | All four dots and brace tips visible on half a. |',
'| Between middle groups | Two isolated flecks. | Geometric marks retained; hand undetermined. |',
'| Middle disk 4 | Broad oval, two crossing long strokes and black point; small top curve and two left-edge curved details. | Geometry checked on halves; no inferred combinatorial assertion. |',
'| Middle disk 5 | Narrow crossed oval with black point and two peripheral curves. | Settled on half b. |',
'| Middle disk 6 | Crossed oval with black point and two curves near upper left. | Settled on half b. |',
'| Middle disk 7 | Crossed oval, black intersection, detached inner blob, two lower arches, long broken upper trace and small detached spot above the outer lower arch. | Trace-origin C doubt retained; added spot shown by crop 04. |',
'| Right-middle open space | Large pale curl, smaller pale bent trace above-right, and two small black flecks lower down. | C origin doubt retained; crops 08–09. |',
'| Second middle group | Long brace and its retraced pieces; below: a short line and two detached dots. | Settled on half b. |',
'| Between middle and bottom rows | One heavy ? with a separate lower dot. | Glyph settled by crop 12; exact author uncertainty is “?”. |',
'| Bottom disk 1 and graph | Literal OK above. Two distinct black intersections, four crossing cuts, short interior residual dash with pale left extension. Below: two separate edges. | First endpoint of first edge has a light centre; open candidate first, filled retained (crop 01). Pale dash extension settled on half a. |',
'| Between bottom disks 1–2 | Pale descending-right trace with darker fragments. | Added from crop 14; no character or hand assigned. |',
'| Bottom disk 2 | Oval and original crossing strokes visible under repeated diagonal returns; one tiny dark hanging trace below its lower-left perimeter. | Cancellation primary, hatching alternative retained (crop 03). |',
'| Bottom disks 3–4 | Each has two near-vertical lines crossed by a horizontal line with a thick central segment; first has top loop, second right loop. | Geometry settled on half a. |',
'| Lower-middle group | Brace below disks 2–4. Under it: three-vertex path and isolated dot. | Left path endpoint has pale centre; open/filled uncertainty newly recorded (crop 10). |',
'| Final bottom disk | Literal OK above; upper heavy horizontal piece and descending heavy piece join within the oval, with the other fine strokes retained. | Geometry settled on half b. |',
'| Final lower graph and first angular trace | Four-vertex line; a broken angular trace crosses near its second vertex, bends at a dark lower corner and continues faintly toward the right. | First graph endpoint newly marked open/filled; trace origin remains unresolved (crop 05). |',
'| Far-right angular trace | Two pale uprights, dark bent lower run, pale rising right run, faint inner oblique trace, upper darker fragments and a detached short mark below. | Origin and very faint endpoints remain unresolved; crop 06. |',
'| Far-right pale patch | Small bounded irregular pale patch beside the bottom row. | Added graphical contour from crop 15; no character or intended function supplied. |',
'| Archive numeral | 9 in pencil at lower left. | Preserved only as `% archive sheet number: 9`; inventory 010.52. |','',
'## C source-section classification','',
'The Notation table has four rows and the Abbreviations table has one OK row. These are retained as notation, not counted as actual doubts. The Doubtful readings section has five actual rows. They map once each to A010-D01–D05, including rows without an unsure macro in C.tex. Every one remains qualified. D01 changes the primary candidate to an open endpoint; D02–D05 retain their prior qualified readings. D02 and D05 each cover several disconnected loci, listed under their single source row.','',
'H has status `desc`. Its drawing description supplies no full text for collation; every H field is null and every diff_H is false.','',
'## Local differences and evidence','',
'| ID | Location | Proposed reading / change | Confidence | Evidence |','| --- | --- | --- | --- | --- |']
for d in diffs:
 evidence=d['readers_crop'] or 'half a, full box '+str(d['bbox']['xyxy'])
 reading=d['reading'].replace('|',' / ').replace('\n',' ')
 lines.append(f"| {d['id']} | {d['location']} | {reading} | {d['confidence']} | {evidence} |")
lines += ['','## Inventory coverage','',f'All {len(inventory)} inventory entries in report.json are represented in reading.tex: the original 51 page objects checked visually, archive numeral 9 in its comment, and 10 additional residual-mark objects. The added smaller pale right trace is included within entry 010.34. No prose, display formula, title, date or manuscript page number is supplied.','',
'## Validation and limits','',
'Only structural source checks are performed: balanced braces and environments, supported macro names, source/report agreement, and existing relative crop paths. No TeX compiler, format builder or render validation is used. No mathematical computation, correspondence proof or theorem check was performed; check_events is empty. The drawings retain visible shapes without assigning an unstated graph-theoretic meaning.','',
'The question-mark crop settled its glyph without changing C. The additional pale-contour crops settled only which graphical fragments are visible; their origin and hand remain unresolved. Fifteen crops were made, one per target locus, and each was viewed once. Crop 04 clips a neighboring portion of the already-settled long brace; its target disk and upward trace are complete. Crop 05 includes only the bottom of the neighboring disk as context; its target graph and angular trace are complete. Crop 11 includes a small cropped tail of the already-settled ou at its left boundary; the target disk and closing parenthesis are complete.','']
(BASE/'reading.md').write_text('\n'.join(lines))
print(json.dumps({'differences':len(diffs),'changed_C':sum(d['diff_C'] for d in diffs),'C_doubt_rows':sum(d['C_doubt_status'] is not None for d in diffs),'inventory':len(inventory),'crops':len(crops)},indent=2))
