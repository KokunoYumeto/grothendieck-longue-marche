from pathlib import Path
import json,re
B=Path('/workspace/scratch/94548b74fbe0'); O=B/'out/readers/012/C'
marks=json.loads((O/'marks_manifest.json').read_text())
crops=json.loads((O/'crops/manifest.json').read_text())
path_audit=json.loads((O/'source_path_manifest.json').read_text())
H=(B/'packets/012/H.tex').read_text()
Hdraw=H[H.index('\\drawing'):H.index('\\note')].strip()
Hnote=H[H.index('\\note'):H.index('\\section')].strip()
def difference(id,location,C,H,reading,evidence,confidence,kind,diff_C,diff_H,status=None,crop=None,bbox=None,**extra):
 d=dict(id=id,location=location,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,diff_C=diff_C,diff_H=diff_H,C_doubt_status=status,readers_crop=crop,bbox=bbox)
 d.update(extra);return d
D=[]
D.append(difference('D001','upper-right label, final letter',r'\unsure{OK|Ok}','OK (ou ok)',r'\unsure{OK|Ok}','Closed first oval and tall second upright are visible. The second letter has an oblique upper arm and a short bent descending outer branch; its case remains unsettled. H retains OK as a candidate, so this is no established H reading error.','medium','other',False,False,'retained','crops/01_upper_right_label.png',[1457,42,1525,98],source_row_id='C.DR1',local_id='C.DR1.K'))
D.append(difference('D002','between the two lower-left miniature ovals',r'\unsure{ou}','des variantes introduites par ou',r'\unsure{ou}','The first compressed loop is followed by one low undulating continuation. The crop preserves ou as the strongest word reading but does not make the second letter fully distinct. No competing word was recovered.','medium','other',False,False,'retained','crops/02_between_miniatures.png',[176,844,216,866],source_row_id='C.DR2',local_id='C.DR2.word'))
D.append(difference('D003a','heavily marked lower-left oval: inner strokes and external loops','overlaid zigzags; C paths 34, 36, 40, 42–51','generic hatched disks description','Dense inner obliques, longer zigzags, and lower/right return loops retained in their observed positions.','The interior contains close slants. Longer strokes rise above the rim, return in rounded loops below the crosspiece, and extend beyond the lower-right rim. Source path 34 continues into the neighbouring miniature; that continuity is retained.','high','other',False,False,None,'crops/03_overdrawn_left_oval.png',[154,562,384,829],source_row_id='C.DR3',local_id='C.DR3.geometry',H_group_reference='D006'))
D.append(difference('D003b','heavily marked lower-left oval: cancellation target and function','C doubtful-readings row: overlaid zigzags / possible cancellation of the underlying oval','generic hatched disks description','Overlaid zigzags; cancellation of the large oval remains a supported unresolved state.','Long loops and slants pass beyond the oval, while the underlying rim and chords remain recoverable. The strokes establish overdrawn geometry but leave the editorial function and cancellation target open. A local unsure wrapper now carries this retained source-table doubt.','low','other',False,False,'retained','crops/03_overdrawn_left_oval.png',[154,562,384,829],source_row_id='C.DR3',local_id='C.DR3.state',qualification='The wrapper changes no observed stroke. The lower miniature included in source path 34 remains outside the proposed cancellation target.',H_group_reference='D006'))
D.append(difference('D004','entire lower-right ruled/curved group','Graphic paths without an explicit cancellation assertion','Tout le coin inférieur droit, les deux axes en équerre et ce qu’ils renferment (les courbes qui se croisent et les deux disques), est biffé','Observed rules and curves retained, with cancelled/live status unresolved.','The broad group has repeated nearvertical strokes at its left, a retraced upper rule with a hooked right return, a long oblique rising from the lower-left, and several crossing curves with hooked ends. These strokes and their crossings are visible. Their purpose as a whole-group cancellation is not settled by the crop. H’s biffé is therefore preserved as a supported state, with an explicit live alternative.','low','deletion state (struck given live or live given struck)',False,True,None,'crops/04_connected_right_group.png',[809,348,1650,1179],source_row_id=None,local_id='right_group.state',qualification='Qualified difference from H; no conclusive assertion of an H error. Source C did not explicitly assert either cancellation state.'))
D.append(difference('D005','eight short labels and their count','Four OK labels, four ou labels, two qualified','H drawing says trois OK; H rereading note corrects it to quatre','Four OK loci and four ou loci; case and one ou remain qualified as in D001/D002.','Half a shows labels near (436,58), (752,62), (1081,42), (1490,71), (1460,361), (435,632), (67,797), and (196,861). The rereading note supplies the corrected count four, so H is collated with that note, rather than counting the superseded trois separately.','high','other',False,False,None,None,[45,18,1528,868],source_row_id=None,half_evidence='a, full-scan origin (0,0)'))
D.append(difference('D006','complete principal drawing field','Detailed TikZ field; all 68 source fill-path blocks retained after direct visual reading',Hdraw,'Complete geometric transcription, including local retracings, interrupted pieces, open loops, dark points, parentheses, auxiliary looped marks, shared contacts, arrow hooks, and the triangle’s three interior spokes.','H supplies a verbal description of the drawing field. Its text names the principal shapes but leaves their detailed geometry, detached fragments, stroke placement, and several auxiliary marks unencoded. The full geometry is collated as this one descriptive-substitution locus. The separate explicit whole-group cancellation assertion is handled by D004.','high','drawing or diagram',False,True,None,None,[24,18,1673,1180],source_row_id=None,half_evidence='a, original full-scan origin (0,0)',sub_loci=[{'location':'top oval family','bbox':[146,23,1632,405],'details':'Actual chord ends, hatching, upper/lower rings, thick bars, lower arc, and miniature sectors.'},{'location':'middle auxiliary upright loop','bbox':[528,413,557,510],'details':'Four source contour subpaths retained; no letter assigned.'},{'location':'left parenthesised group','bbox':[24,757,406,920],'details':'Both parentheses, four local labels/miniature relations, and left-edge detached dash.'},{'location':'lower auxiliary zigzag','bbox':[399,900,443,1019],'details':'Angular/looped vertical mark retained graphically.'},{'location':'triangle below central oval','bbox':[574,891,671,1014],'details':'Three interior spokes, central junction, outer triangle, and the lower-right extension.'},{'location':'right group','bbox':[809,348,1650,1179],'details':'Repeated border strokes; open upper-left gap retained; hooked ends and detached oblique pieces retained.'}]))
D.append(difference('D007','left page edge, at fold height; source inventory coverage','C path 57 is present, but C_inventory.json has no separate item','not individually described','Short detached horizontal dash retained and inventoried separately.','The source path spans x24.6–34.2, y797–800.5 and corresponds to the dark dash left of the opening parenthesis on half a. This is an inventory correction, with no alteration of that C path.','high','other',False,False,None,None,[23,795,36,802],source_row_id=None,half_evidence='a, original full-scan origin (0,0)',H_group_reference='D006'))
D.append(difference('D008','bottom-left archive number','% archive sheet number: 11; absent from separate C inventory','\\page{11}','% archive sheet number: 11','Two pencil-like ascending numeral strokes at the foot read 11. The supplied convention places this archive number in a comment. It is now a separate inventory item.','high','other',False,False,None,None,[25,2302,76,2331],source_row_id=None,half_evidence='b, origin (0,1100); b coordinates [25,1202,76,1231]'))
for m in marks:
 lower=m['bbox'][1]>1200
 c_text='No corresponding path or node in C.'
 if m['id']=='N11': c_text='C path 33 contains the upper rim endpoint near y629; C path 41 resumes the lower-left rim at y656. The pale intervening trace is absent.'
 if m['id']=='N12': c_text='C paths 55, 60 and 61 preserve darker lower-rim fragments, with no path for the pale oblique fragment reported here.'
 if m['id']=='N14': c_text='C path 25 preserves the strong terminal shape through roughly (1611,915); its pale outer continuation is absent.'
 ev='The '+m['reading']+' is visible '+('in the indicated enlargement.' if m['crop'] else 'on supplied half '+('b, whose full-scan origin is (0,1100).' if lower else 'a, whose full-scan origin is (0,0).'))+' It is reproduced graphically. Hand, intentionality, role and surface origin remain undetermined.'
 D.append(difference('D_'+m['id'],m['location'],c_text,'No lower-field mark described.' if lower else 'Not specified individually in the drawing description.',m['reading'],ev,m['confidence'],'omission',True,lower,None,m['crop'],m['bbox'],source_row_id=None,local_id=m['id'],qualification='Confidence refers to visible shape; no character, mathematical meaning, handwriting attribution, or surface origin is established.',H_group_reference=None if lower else 'D006',tex_anchor='% '+m['id']+':'))
source_rows=[
 dict(source_row_id='C.DR1',source='C_doubts.txt / Doubtful readings / row 1',source_text='12 | above upper right oval | OK | Ok | medium | O closes on itself, k/K has an unusually short last branch.',status='retained',difference_ids=['D001'],local_subloci=[dict(id='C.DR1.K',bbox=[1457,42,1525,98],reading=r'\unsure{OK|Ok}',crop='crops/01_upper_right_label.png')]),
 dict(source_row_id='C.DR2',source='C_doubts.txt / Doubtful readings / row 2',source_text='12 | between miniature ovals | ou | — | medium | The second hump is compressed; compare ou beside the top oval.',status='retained',difference_ids=['D002'],local_subloci=[dict(id='C.DR2.word',bbox=[176,844,216,866],reading=r'\unsure{ou}',crop='crops/02_between_miniatures.png')]),
 dict(source_row_id='C.DR3',source='C_doubts.txt / Doubtful readings / row 3',source_text='12 | lower-left heavily marked oval | overlaid zigzags | possible cancellation of the underlying oval | low | Several strokes extend beyond the boundary. Both the oval with its chords and the overlying pen strokes are drawn in their actual positions. The ink alone does not settle their editorial function.',status='retained',difference_ids=['D003a','D003b'],local_subloci=[dict(id='C.DR3.geometry.inner',bbox=[184,625,348,746],reading='dense oblique inner strokes',crop='crops/03_overdrawn_left_oval.png'),dict(id='C.DR3.geometry.outer',bbox=[160,562,384,807],reading='long rising obliques and lower/right return loops',crop='crops/03_overdrawn_left_oval.png'),dict(id='C.DR3.state',bbox=[154,562,384,829],reading='overlaid zigzags; possible cancellation of the large oval, with live overdrawn state retained',crop='crops/03_overdrawn_left_oval.png')],qualification='One original source row, mapped through its local geometric and state subloci; counted once. It exists in the doubt table even though original C.tex had no unsure wrapper at this drawing.')
]
doubts=[
 dict(location='upper-right label',reading=r'\unsure{OK|Ok}',alternatives=['Ok'],confidence='medium',reason='Final branch shape does not settle K/k; the primary OK survives.',crop='crops/01_upper_right_label.png',bbox=[1457,42,1525,98],source_row_id='C.DR1',local_id='C.DR1.K'),
 dict(location='between lower-left miniatures',reading=r'\unsure{ou}',alternatives=[],confidence='medium',reason='Compressed second hump; no independently recovered alternative word.',crop='crops/02_between_miniatures.png',bbox=[176,844,216,866],source_row_id='C.DR2',local_id='C.DR2.word'),
 dict(location='heavy lower-left oval, state of the superposed strokes',reading='overlaid zigzags; cancellation status unresolved',alternatives=['cancellation of the underlying large oval','live overdrawn hatching/loops'],confidence='low',reason='External overshoots and return loops remain compatible with the two stated functions. The observed path geometry is preserved.',crop='crops/03_overdrawn_left_oval.png',bbox=[154,562,384,829],source_row_id='C.DR3',local_id='C.DR3.state'),
 dict(location='whole lower-right group, cancellation state',reading='curves and rules with unresolved cancelled/live state',alternatives=['whole-group cancellation as H states','live drawing with retraced rules and crossing curves'],confidence='low',reason='No recovered authorial word or unambiguous separate cancellation scope marker settles the role of the observed strokes.',crop='crops/04_connected_right_group.png',bbox=[809,348,1650,1179],source_row_id=None,local_id='right_group.state')
]
for m in marks:
 doubts.append(dict(location=m['location'],reading=m['reading'],alternatives=['intentional detached or continuing trace','trace of undetermined surface origin'],confidence=m['confidence'],reason='The visible graphical shape is retained; role, hand, and surface origin remain open. No character is supplied.',crop=m['crop'],bbox=m['bbox'],source_row_id=None,local_id=m['id'],shape_confidence=m['confidence'],role_confidence='undetermined',hand='undetermined hand'))
# Main inventory follows the actual page. The source inventory is a locating aid;
# the descriptions below have been checked and qualified from the scan.
inv=json.loads((B/'packets/012/C_inventory.json').read_text())
path_map={1:[2],2:[],3:[1],4:[],5:[3],6:[],7:[4,6,7,8,9,10,11,12,14,15,16,17,19,20,21,22,24],8:[],9:[5,13,18],10:[],11:[23],12:[30],13:[27],14:[29],15:[28],16:[26],17:[35],18:[34,36,40,42,43,44,45,46,47,48,49,50,51],19:[],20:[53,58],21:[],22:[59,63],23:[],24:[34],25:[37],26:[68],27:[66],28:[65],29:[25,32],30:[33,41,55,60,61],31:[25,38,39,52,54,56,62,64],32:[25,67]}
for i,item in enumerate(inv,1):
 item.pop('cote',None);item.pop('scan',None)
 item['hand']='his hand';item['element']=f'012.C.{i:02d}';item['source_inventory_element']=f'012.{i:02d}'
 item['C_source_paths']=path_map[i]
item_updates={
8:'OK/Ok, case qualified in the final letter',
12:'small triangle, with upward extension at apex; the separate point is inventoried independently',
13:'narrow upright looping mark; no letter assignment',
18:'large oval with chords, inner obliques, and long overlaid zigzags/loops; cancellation status unresolved',
23:'ou, second letter compressed and qualified',
24:'right miniature oval with radial/crossing strokes; source path shared with the large oval above',
27:'upright angular and looping mark; no letter assignment',
28:'triangle with three interior spokes meeting at a central junction, plus lower-right terminal extension',
29:'retraced upper horizontal rule with right hook; repeated nearvertical border strokes; top-left gap retained',
30:'upper oval with crossing chords, light rim gaps and darker separated fragments',
31:'extended crossing curves, slanted/upward and rightward/downward hooked ends, detached short obliques and repeated traces',
32:'low rounded outline with curved chords and passing long oblique; all recovered contours retained'}
for i,x in item_updates.items(): inv[i-1]['first_words_or_objects']=x
for item in inv: item['transcribed']='yes'
extras=[
 dict(sheet_kind='text',hand='his hand',element='012.C.33',kind='drawing',position='right of small triangle, below first oval',first_words_or_objects='separate dark point',transcribed='yes',C_source_paths=[31]),
 dict(sheet_kind='text',hand='undetermined hand',element='012.C.34',kind='drawing',position='left page edge, at fold height',first_words_or_objects='short detached horizontal dash',transcribed='yes',C_source_paths=[57]),
 dict(sheet_kind='text',hand='unnamed archival hand',element='012.C.35',kind='text',position='bottom-left foot',first_words_or_objects='archive numeral 11, represented by archive comment only',transcribed='yes',bbox=[25,2302,76,2331]),
 dict(sheet_kind='text',hand='his hand',element='012.C.36',kind='deletion',position='large heavily marked lower-left oval',first_words_or_objects='possible cancellation by the observed overlaid zigzags; live interpretation retained',transcribed='yes',source_row_id='C.DR3',qualification='Uncertain state, locally attached to the graphic; no generic cancellation stroke added.'),
 dict(sheet_kind='text',hand='his hand',element='012.C.37',kind='deletion',position='whole lower-right drawing group',first_words_or_objects='possible whole-group cancellation; live state retained',transcribed='yes',qualification='Uncertain state; H states biffé. Actual strokes remain the visible geometry, without a generic cancellation rule.')
]
inv+=extras
for m in marks:
 inv.append(dict(sheet_kind='text',hand='undetermined hand',element='012.C.'+m['id'],kind='drawing',position=m['location'],first_words_or_objects=m['reading'],transcribed='yes',bbox=m['bbox'],tex_anchor='% '+m['id']+':',qualification=m['role']))
# Per-path audit: every source block has a locating observation and is retained.
for p in path_audit:
 n=p['path']
 if n==1: obs='Small upper alternative oval: rim, crossing chords, dark central junction and lower curved division.'
 elif n==2: obs='Upper-left large oval: chord ends, hatched triangular region, lower arc, boundary retracings.'
 elif n==3: obs='Upper second oval: three upright strokes, central heavy bar, peripheral contacts, open small loops and crosslike end marks.'
 elif n in [4,6,7,8,9,10,11,12,14,15,16,17,19,20,21,22,24]: obs='Upper third oval: outline/chord system and individually retained hatch/rim fragments at this block’s coordinates.'
 elif n in [5,13,18]: obs='Upper fourth oval: hatched triangle, thick right-going portion, curved near-right upright and local small fragment.'
 elif n==23: obs='Far-right miniature: irregular rim, multiple radial/crossing strokes, thick central/right-going portion.'
 elif n==26: obs='Triangle with heavy upright stem above it.'
 elif n==27: obs='Narrow upright looped auxiliary mark, retained graphically.'
 elif n==28: obs='Small square, including the small bottom-left interruption.'
 elif n==29: obs='Heavy three-pronged drawing, with three rounded terminal thickenings.'
 elif n==30: obs='Left small triangle and the apex extension; detached higher tick added independently as N05.'
 elif n==31: obs='Separate dark point right of that triangle.'
 elif n==32: obs='Repeated nearvertical border strokes with separate upper starts and unequal lower extents.'
 elif n in [33,41,55,60,61]: obs='Upper oval in right group: strong outline/chord portions and separated darker lower-rim fragments; new faint segments N11/N12 kept separate.'
 elif n in [34,36,40,42,43,44,45,46,47,48,49,50,51]: obs='Heavily marked lower-left oval and shared lower miniature contour: close hatching, longer obliques, return loops and tiny separate components; function remains qualified.'
 elif n==35: obs='Middle far-left oval with two dark opposing wedge regions and extended chord ends.'
 elif n==37: obs='Central middle oval: hatched small sector, crossing curves, lower slanted ends and lower contact.'
 elif n in [53,58]: obs='One of the two parenthesis strokes around the lower-left alternative group.'
 elif n in [59,63]: obs='Left miniature within parentheses: light/strong rim portions and dark wedge/radial components.'
 elif n==57: obs='Detached left-edge horizontal dash, inventoried separately.'
 elif n==65: obs='Lower central triangle: three spokes, central junction, outer contour and rightward terminal extension.'
 elif n==66: obs='Lower narrow upright zigzag/looped auxiliary mark, retained graphically.'
 elif n==68: obs='Lower-left quadrilateral with diagonal and small uneven boundary details.'
 else: obs='Right-group long curves/rules and detached local pieces; exact source block retained at its observed coordinates.'
 p['observation']=obs;p['retained_exact_source_block']=True;p['evidence']='supplied half a; crop 03 or 04 for the corresponding enlarged locus'
notation=[
 dict(location='four label loci above or beside ovals',written='OK',latex='OK, with upper-right '+r'\unsure{OK|Ok}',evidence='Closed oval plus branched upright; upper-right branch case stays open.'),
 dict(location='upper miniature alternative, far-right alternative, and lower parenthesised alternatives',written='ou',latex='ou; middle lower occurrence '+r'\unsure{ou}',evidence='Small loop followed by low joined continuation.'),
 dict(location='upper second oval, middle upright endpoints',written='small open loops',latex='TikZ C source path 3',evidence='Light centres enclosed by dark rims at upper/lower middle contacts; no algebraic notation supplied.'),
 dict(location='between simpler lower graphs',written='upright loops/zigzags',latex='TikZ C source paths 27 and 66',evidence='Narrow looping and angular shapes retained as drawn; no letter recovered.'),
 dict(location='lower-left miniature pair',written='parenthesis strokes',latex='TikZ C source paths 53 and 58',evidence='Long opening curve on left and longer closing curve on right.'),
 dict(location='bottom-left archive foot',written='11',latex='% archive sheet number: 11',evidence='Two pencil-like numeral forms in half b.'),
 dict(location='repeated printed/handwritten label form in current packet',written='OK',latex='OK',expansion='okay',qualification='Possible expansion from source abbreviation table; never expanded in reading.tex.')
]
notes=dict(
 page_content='A drawing sheet. The principal field occupies the upper half: oval/chord constructions, eight short labels, a row of simpler graph-like drawings, two left miniature alternatives inside parentheses, and a large right-hand group of rules and crossing curves. Sparse detached traces remain in the lower field.',
 authors_own_uncertainty={'exact_words':['ou'], 'comment':'Four ou loci mark written alternatives, one reading remaining qualified. No prose statement of uncertainty is recovered. The upright looping/zigzag marks are preserved without assigning them a question mark or letter.'},
 title_date_page_counts={'title':None,'date':None,'author_page_number':None,'archive_sheet_number':'11','scan':'12','H_page':'11','comment':'Archive numbering is represented only in a TeX comment.'},
 mathematical_reading_decisions='The short labels, boundary contacts, hatching, three interior spokes of the lower triangle, open loops and arrow hooks were read from visible strokes. No map, theorem, topological equivalence, or algebraic repair was supplied. No mathematical computation was performed.',
 source_boundary='The final unnumbered section in packet H.tex and its note explicitly concern feuillet 13. That tail is contextual apparatus for another sheet and is excluded from scan012 transcription and collation. The H drawing description and rereading note before that boundary apply to scan012.',
 H_collation_policy='The descriptive replacement of the principal drawing field is one D006 locus. Individual missing fragments within it are fully identified without repeating diff_H=true. The explicit biffé assertion remains a separate qualified state difference D004. Sparse lower-field omissions outside the described drawing field have their own local rows.',
 abbreviation_source='The notation and abbreviation table rows in C_doubts.txt are kept in their own categories. The three actual doubtful-reading rows alone form C.DR1–C.DR3. The supplied C_notes.txt is empty.',
 handwriting='Principal dark drawing and labels: his hand, following the packet and visible consistency. Archive foot: unnamed archival hand. All newly retained small/pale detached traces: undetermined hand; authorial intention and surface origin are unresolved.',
 graphics='All 68 original C fill-path blocks are retained exactly after visual comparison. Two local unsure wrappers attach the open state questions to the respective drawing clusters. The first cluster includes a source path also extending into the lower miniature; the uncertainty target is explicitly restricted to the large oval. Thirty-one manually specified visible-mark entries supplement the source. No character is substituted for an unassigned shape.',
 image_views={'full':1,'half_a':1,'half_b':1,'crops_generated':17,'crops_visually_inspected':17,'comment':'A first tool return attempted to include crop 04 after crop 03 but discarded crop 04 at the output limit. The same existing crop 04 was then displayed alone; it was not recropped. The first tool return for crop 16 was truncated before its image was visible; the same existing file was displayed afterward. Five final crops inspected previously unresolved faint lower-field traces. No whole/half image was revisited and no decided locus was recropped.'},
 original_doubt_source_row_count=3,
 original_doubt_status={'resolved':0,'retained':3},
 scope='Only the assigned packet, brief, PREAMBLE, notation snapshot, original scan and supplied halves were read. No web, OCR, other page, other reader, compiler, rendering, package installation, or mathematical repair was used.'
)
report=dict(scan='012',reader='C',start_utc=(O/'start_utc.txt').read_text().strip(),end_utc=None,full_image_viewed=True,halves_viewed=True,complete_visual_read=True,bbox_coordinate_system='Original full scan: [left,top,right,bottom], pixels. Full 1690×2361; a 1690×1260 at (0,0); b 1690×1261 at (0,1100).',differences=D,doubts=doubts,inventory=inv,notes=notes,notation=notation,abbreviations=[dict(form='OK',expansion='okay',qualification='Possible expansion only; manuscript form retained.')],check_events=[],crops=crops,source_doubt_map=source_rows,source_path_audit=path_audit,brief_feedback=[
 'A single source filled contour (path 34) contains the doubtful large oval and its lower live miniature. The local unsure wrapper includes that shared contour, while the comments and records explicitly restrict the cancellation target to the large oval.',
 'H is classified text but gives a descriptive drawing replacement. D006 records the geometric substitution once; its local missing details remain explicit and are not double-counted against H.',
 'For tiny pale marks with no supported character identity, the transcript uses explicit small graphical paths. Hand, purpose and surface origin remain unresolved; paper mottling was not turned into supplied words.',
 'Structural source verification only. No TeX compilation or rendered validation is claimed.'
])
(O/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# Compact page-order reading audit, with explicit source-row and crop links.
md=['# Scan 012 — independent reader C','',f"Start UTC: {report['start_utc']}",'','## Scope and source boundary','',notes['source_boundary'],'',notes['scope'],'','The whole original and each supplied half were displayed once. Half a has origin (0,0); half b has origin (0,1100), derived from the actual 1690×2361 and 1690×1261 image dimensions. Seventeen enlarged crops were created. Crops 04 and 16 were first dropped by tool-output limits, then displayed from the same existing files. No decided locus was recropped.','', '## Page-order reading audit','', '| Location | Readable ink and geometry | Unresolved qualification |','|---|---|---|']
read_rows=[
 ('Upper-left large oval','Irregular outer oval; long crossing chord strokes; triangular hatching; lower internal arc and short boundary retracings. C path 2 retained.','No added mathematical relation.'),
 ('Above upper-left oval / small alternative','`ou`; small oval with central dark junction, chord spokes and lower curved compartment. Paths 1 and label retained.','Two nearby detached marks N01/N02 have undetermined role/hand.'),
 ('Upper second oval','`OK`; three long upright strokes, thick central crosspiece, ring-like central upper/lower contacts, dark outer contacts and small crossed terminal strokes. Path 3 retained.','No classification or map inferred from vertex appearance.'),
 ('Upper third oval','`OK`; crossed chord system and hatched quadrilateral; small detached hatch components and lower-right rim fragment all retained. Paths 4, 6–12, 14–17, 19–22, 24.','Pale/strong local stroke changes preserved by source paths.'),
 ('Upper fourth oval','`\\unsure{OK|Ok}`; hatched triangle, heavy right-going segment and near-right curved upright. Paths 5, 13, 18.','C.DR1 retained; crop 01 does not settle K/k.'),
 ('Far-right small alternative','`ou`; irregular small oval, central junction, radial/crossing strokes and heavy short branch. Path 23 retained.','No word expansion.'),
 ('First lower graph row, left','Small triangle with apex extension, separate dark point, then a narrow upright looped mark. Paths 30,31,27.','Detached higher tick N05 and gap spots N06–N08 have unassigned role/hand.'),
 ('First lower graph row, centre/right','Heavy three-pronged figure, small square with lower-left interruption, triangle with upright stem. Paths 29,28,26.','All strong boundaries retained; no completion of the square’s tiny gap.'),
 ('Second register, far left','Oval with two opposing black wedges and crossing chords. Path 35.','No uncertainty added.'),
 ('Second register, heavily marked oval','Underlying oval and chord layout, dense slants, long overlaid zigzags and return loops; `OK` at right. Paths 34,36,40,42–51.','C.DR3: geometry retained; cancellation/live role stays open. Crop 03. Source row counted once, with inner/outer geometry and state mapped separately.'),
 ('Lower-left parenthesised alternatives','Opening parenthesis, `ou`, two miniature ovals, middle `\\unsure{ou}`, closing parenthesis. Paths 53,58,59,63, plus shared lower portion of path34.','C.DR2 retained after crop02. The right miniature remains outside the possible large-oval cancellation target.'),
 ('Central second-register oval','Oval with crossing curves, small hatched sector and lower crossing endpoints. Path37.','No interpreted formula.'),
 ('Bottom of the principal left field','Quadrilateral with diagonal; upright angular/looped auxiliary mark; triangle with three interior spokes meeting at a central junction and a lower-right extension. Paths68,66,65.','Auxiliary mark remains graphical, with no letter assignment.'),
 ('Right-group border','Repeated upper horizontal rule with hooked return at the right; repeated nearvertical left strokes with unequal lower ends. The upper-left gap remains open. Paths25,32.','D004 whole-group cancellation/live state remains open after crop04; H’s biffé is a supported alternative.'),
 ('Right-group upper oval','Outer curve, crossing chord curves and separate darker rim fragments. Paths33,41,55,60,61.','Faint intervening and lower-right fragments N11/N12 added; their pale endpoints remain qualified.'),
 ('Right-group long crossing curves','Long rising oblique and broad descending curves, repeated upright runs, hooked rightward/downward terminals and detached short obliques. Paths25,38,39,52,54,56,62,64.','N14 retains a pale continuation outside a strong terminal; no further connection inferred.'),
 ('Right-group lower oval','Low rounded outline and curved chords, with long oblique passing across it; small source mark67 retained.','Same D004 open whole-group state.'),
 ('Fold-height edges and gaps','Left detached dash in original path57 retained; right dash N15 added. Small N03/N04/N09/N10/N13 spots retained at their exact reported loci.','Hands, purposes and surface origins unassigned.'),
 ('Lower blank field','Pale curve N16; isolated dark spot N17; subsequent sparse graphical spots/traces N18–N31.','No character or mathematical role assigned. Crops05/06/07/12–17 inspect unresolved local shapes; other tiny shapes were already visible on half b. N31 shares the already necessary crop16 with N24.'),
 ('Bottom-left foot','Archive `11`, comment only.','No author page number, date or title supplied.')
]
for a,b,c in read_rows: md.append('| '+a+' | '+b+' | '+c+' |')
md+=['','## Original C doubt-row map','', '| Source row | Physical/local subloci | Decision and report rows | Crop |','|---|---|---|---|',
 '| C.DR1 — above upper-right oval | Branched final letter in OK/Ok | Retained: D001 | 01_upper_right_label.png |',
 '| C.DR2 — between miniature ovals | Joined loop and compressed continuation | Retained: D002 | 02_between_miniatures.png |',
 '| C.DR3 — lower-left heavily marked oval | Inner slants; external zigzags/loops; their cancellation function | Geometry retained: D003a. State retained: D003b. One source row, three explicitly mapped local subloci. | 03_overdrawn_left_oval.png |','',
 'The notation and abbreviation table entries are not counted as doubtful-reading rows. All three actual rows are retained; none is silently dropped or merged into a neighbouring row.','',
 '## Every retained C source path','', '| Source path | Original full-scan bbox | Direct reading audit |','|---|---|---|']
for p in path_audit: md.append(f"| {p['path']:02d} | {p['bbox']} | {p['observation']} |")
md+=['','## New visible marks: local audit','', '| ID | Location / shape | Full-scan bbox | Evidence | Qualification |','|---|---|---|---|---|']
for m in marks:
 ev=m['crop'] or ('half b, origin (0,1100)' if m['bbox'][1]>1200 else 'half a, origin (0,0)')
 md.append(f"| {m['id']} | {m['location']}: {m['reading']} | {m['bbox']} | {ev} | Shape {m['confidence']}; hand, role, intention and surface origin undetermined. |")
md+=['','## H collation','',
 '- D006 records the detailed geometry replacing H’s prose description once. Its local figures and omitted details are listed explicitly in the report.',
 '- The original “trois” is read together with H’s rereading correction to “quatre”; the visible count is four OK loci.',
 '- The principal rightmost upper horizontal stroke has a hooked return, and the repeated nearvertical border has no corresponding arrowhead. The actual hooks and all shorter arrowlike ends within the group remain in the paths.',
 '- D004 qualifies H’s assertion that the entire lower-right group is biffé. The crop leaves cancelled/live state open.',
 '- The feuillet13 section tail is excluded as supplied contextual apparatus. No other page was read.','',
 '## Notes and checks','',notes['mathematical_reading_decisions'],'',
 'Possible abbreviation expansion: OK → okay, recorded here and in report.json only. The transcription retains OK.','',
 'The two local drawing-state questions use the supplied unsure macro around actual local graphics. No generic cancellation line has been added. The shared source path into the right lower miniature is retained; the possible cancellation target remains the large oval only.','',
 'Structural source checks are reported separately below after synchronization. No compilation, rendered validation, external theorem, or mathematical proof check is claimed.','']
(O/'reading.md').write_text('\n'.join(md))
print('Built report.json and reading.md:',len(D),'local difference/audit rows;',len(inv),'inventory items;',len(doubts),'doubt/role entries.')
