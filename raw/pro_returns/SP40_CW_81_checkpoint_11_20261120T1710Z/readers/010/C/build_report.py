from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
crops=json.loads((HERE/'crop_records.json').read_text())
diffs=[]
def row(id,location,C,reading,evidence,confidence,kind,diff_C,crop=None,bbox=None,doubt=None,source=None,anchor=None):
 d={'id':id,'location':location,'C':C,'H':None,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':diff_C,'diff_H':False,'C_doubt_status':doubt,'readers_crop':crop,'bbox':{'source':'original full scan','origin':'upper left','xyxy':bbox}}
 if source:d['C_doubt_source']={'section':'Doubtful readings','row':source}
 if anchor:d['C_anchor']=anchor
 diffs.append(d)
row('C010-D01','Lower-left graph, left endpoint of first edge',r'\unsure{\bullet|\circ}',r'\unsure{\circ|\bullet}','A small enclosed pale center is visible within the thick triangular left rim. The right endpoint has a larger fully enclosed white center and remains circ. The left primary candidate is reversed; its filled alternative remains supported by the heavy surrounding ink.','medium','misread symbol or index',True,'01_lower_left_graph.png',[119,1014,329,1059],'retained',1)
row('C010-D02a','Final middle disk, projecting upper trace and detached blob','Faint strokes; marks from the other surface retained as alternative','Projecting trace and blob retained graphically; trace has pale intervals and short darker sections; role and hand undetermined.','The long rising trace is visibly interrupted and alternates pale and dark sections. The detached blob has a tapered upper part and broad lower mass. The crop supplies their geometry without establishing a writing surface or function.','low','drawing or diagram',True,'04_middle_final_disk.png',[1270,314,1420,600],'retained',2,r'\draw (1328,433) .. controls (1330,406) and (1335,357) .. (1341,329);')
row('C010-D02b','Foot below and across final graph, left angular trace','Faint angular strokes; possible marks from the other surface','Visible left angular trace retained; role, hand and surface origin remain unresolved.','The descending stroke crosses the graph near its second spot, forms a heavy lower bend, then has a pale continuation and separated rising dark patches to the right. All of those portions remain drawn.','low','other',False,'05_left_angular_trace_and_graph.png',[971,960,1302,1105],'retained',2)
row('C010-D02c','Far lower right, second angular trace','Faint angular strokes; possible marks from the other surface','Visible right angular trace retained; role, hand and surface origin remain unresolved.','Two pale rising ends accompany a heavy shallow V-shaped lower portion. The visible trace permits no secure attribution of hand or surface. A separate internal pale line is recorded in C010-D14.','low','other',False,'06_right_angular_trace.png',[1330,885,1603,1080],'retained',2)
row('C010-D03','Lower row, second disk, state of repeated diagonal strokes','Diagonal cancellation; hatching alternative in C doubtful-readings table','Diagonal cancellation remains the primary state; hatching remains an explicit alternative. The full drawing is marked unsure.','Repeated oblique strokes make low returning turns and cross the disk outline at several points. Those crossings support the cancellation candidate but do not settle its purpose. The underlying outline and chords stay visible.','medium','other',False,'03_overdrawn_disk.png',[438,703,654,935],'retained',3)
row('C010-D03G','Lower row, second disk, generic horizontal strike produced by the deleted wrapper',r'\deleted{\hbox{<drawn disk>}}',r'\unsure{\rlap{<drawn disk>}\phantom{\deleted{<same drawn disk>}}}','The visible crossings run diagonally and follow the reproduced paths. The source deleted wrapper would add a horizontal strike across the boxed picture. The proposed boxing keeps its deletion annotation in an invisible copy and shows the actual drawn strokes once.','high','drawing or diagram',True,'03_overdrawn_disk.png',[438,703,654,935])
row('C010-D04','Graph below seventh upper disk, middle vertex',r'\unsure{\bullet|\circ}',r'\unsure{\bullet|\circ}','The middle spot is a thick body with an upper hook and a white opening at lower right; a gap precedes the right edge. The body supports bullet as primary while the open-looking form keeps circ available.','medium','other',False,'02_top_seventh_graph.png',[1080,228,1221,273],'retained',4)
row('C010-D05a','Upper edge, detached pair of traces','Detached marks; transfer or surface flecks alternative','Both detached traces remain; function and hand undetermined.','The left trace bends downward then up; the right trace is a short low bar with small raised ends. There is insufficient stroke structure to supply a character. Geometry is refined in C010-D06.','low','other',False,'07_upper_edge_traces.png',[1005,14,1057,43],'retained',5)
row('C010-D05b','Open space right of middle group, main pale curl','Detached pale curled trace; transfer or surface flecks alternative','Main pale curl retained graphically; function and hand undetermined.','A pale upper slant rounds into a return with a darker lower tip. No word or character is supplied. The separate upper-right trace is recorded in C010-D08.','low','other',False,'08_right_middle_pale_marks.png',[1500,337,1604,418],'retained',5)
row('C010-D05c','Open space right of middle group, lower tiny flecks','Two detached flecks; transfer or surface flecks alternative','The two tiny spots remain, without assigned character or function.','Two distinct compact dark spots lie diagonally, the upper one right of the lower one. Their visible positions are retained.','low','other',False,'09_right_middle_flecks.png',[1545,566,1582,602],'retained',5)
row('C010-D06','Upper edge, geometry of detached pair',r'(1018,28)--(1025,29) and (1037,27)--(1046,26)','Left shallow bent trace and right short bar with raised ends, drawn with curves and short segments.','Crop 07 exposes the left U-like bend and the right two small upward projections that the two straight C strokes omit. No literal U or other character is transcribed.','medium','drawing or diagram',True,'07_upper_edge_traces.png',[1005,14,1057,43])
row('C010-D07','Below and right of upper second disk','No corresponding path','Pale detached curved trace near (414,240)–(400,273).','A weak descending right curve turns left at its foot. The crop preserves the full visible arc; its role and hand remain unsettled.','low','omission',True,'10_upper_left_pale_arc.png',[395,224,439,285])
row('C010-D08','Above-right of main pale curl in right middle open space','No corresponding path','Separate pale short slant near (1567,351)–(1576,363).','The small upper trace has a slightly curved diagonal body separated by clear space from the lower curl. It is drawn without a character candidate.','low','omission',True,'08_right_middle_pale_marks.png',[1500,337,1604,418])
row('C010-D09','Gap above and right of lower first disk','No corresponding path','Pale diagonal trace near (368,743)–(398,777).','The crop shows a continuous directional run with several darker small points, descending to the right. Its origin and hand remain unresolved.','low','omission',True,'11_lower_left_pale_arc.png',[351,729,405,788])
row('C010-D10','Final middle disk, below-left of its crossing','No small spot at this position','Small detached spot near (1314,544).','The compact dark spot is visibly separated from the rising diagonal and from the outer lower arch. Its mathematical role remains unassigned.','medium','omission',True,'04_middle_final_disk.png',[1270,314,1420,600])
row('C010-D11','Lower second disk, lower-left outline','No small pendant stroke at this position','Short dark pendant stroke near (490,911)–(489,920).','A short narrow mark extends downward immediately below the lower-left part of the outline. The target remains completely inside the crop.','medium','omission',True,'03_overdrawn_disk.png',[438,703,654,935])
row('C010-D12','Lower middle graph, first vertex',r'\bullet',r'\unsure{\circ|\bullet}','The left spot surrounds a triangular pale center. Open circle is the stronger visible candidate, while the dark irregular body leaves the filled reading available. Other spots remain as C.','medium','misread symbol or index',True,'12_lower_middle_graph.png',[461,1008,660,1055])
row('C010-D13','Final lower graph, first vertex',r'\bullet',r'\unsure{\bullet|\circ}','The left end has a substantial black patch and a bent return around a lower pale opening. The opening reaches the lower boundary, so bullet remains primary; circ is kept as a supported alternative.','medium','other',True,'05_left_angular_trace_and_graph.png',[971,960,1302,1105])
row('C010-D14','Inside the right angular trace at the foot','No internal pale diagonal','Pale diagonal from about (1440,1036) toward (1490,985).','A weak slant rises from the inner side of the heavy lower edge into the white space. It has no clear label or attachment beyond its visible trace.','low','omission',True,'06_right_angular_trace.png',[1330,885,1603,1080])
row('C010-D15','Upper end of right angular trace','Only a uniformly pale upper return','Short dark upright near (1568,907), a spot near (1567,921), and a faint spot near (1550,894).','The crop shows the dark short upright and its lower separated spot, plus a faint detached upper-left spot. Their positions are drawn; no letters or role are supplied.','low','drawing or diagram',True,'06_right_angular_trace.png',[1330,885,1603,1080])
row('C010-D16','Inside lower first disk, left continuation of pale horizontal trace',r'\draw[opacity=.4] (276,827)--(293,828);','Add the faint left continuation from about (250,826) to (276,828), retaining the darker right part.','Half a shows a weak horizontal run extending left of the darker short segment toward x250. This was settled from the supplied half; no crop was made.','medium','omission',True,None,[245,818,299,838])
diffs[-1]['half_location']={'half':'a','origin':'upper left','xyxy':[245,818,299,838]}
row('C010-D17','Right margin level with lower row','No corresponding shape','Very pale irregular patch with a scalloped upper edge and rounded lower portion, drawn without a character.','The enlargement shows an irregular pale filled area and uneven darker rim. Its origin, role and hand remain undetermined; the rendering preserves only its visible shape.','low','omission',True,'13_right_margin_gray_patch.png',[1623,779,1655,816])
# Complete inventory, retaining C element identifiers for easy source location.
inv=[]
for src in json.loads((ROOT/'packets/010/C_inventory.json').read_text()):
 x={k:src[k] for k in ['sheet_kind','element','kind','position','first_words_or_objects','transcribed']}
 x['hand']='his hand'
 if src['element'] in ['010.01','010.29','010.34','010.50','010.51']:x['hand']='undetermined hand'
 if src['element']=='010.11':x['first_words_or_objects']='group brace under top disks 4 and 5'
 if src['element']=='010.22':x['first_words_or_objects']='ou'
 if src['element']=='010.33':x['first_words_or_objects']='crossed disk with two lower arches; detached superposed marks inventoried separately'
 if src['element']=='010.34':x['first_words_or_objects']='main pale curled trace'
 if src['element']=='010.42':x['first_words_or_objects']='repeated diagonal strokes: cancellation primary, hatching retained; unsure state'
 if src['element']=='010.47':x['first_words_or_objects']='disk with four strokes and two adjoining thickened segments'
 inv.append(x)
def item(element,kind,position,objects,hand='undetermined hand'):
 inv.append({'sheet_kind':'text','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':objects,'transcribed':'yes'})
item('010.11a','drawing','below upper disks 4 and 5','oval enclosing three dots','his hand')
item('010.22a','drawing','far upper right','two curved parentheses enclosing ou and the small variant disk','his hand')
item('010.33a','drawing','above seventh middle disk','projecting broken dark/pale stroke')
item('010.33b','drawing','left of crossing inside seventh middle disk','detached tapered dark blob')
item('010.33c','drawing','below-left of crossing inside seventh middle disk','small detached spot at about (1314,544)')
item('010.34a','drawing','right middle open space, below main curl','two tiny detached flecks')
item('010.34b','drawing','above-right of main pale curl','short separate pale slant')
item('010.52','drawing','below/right of second upper disk','pale detached curved trace')
item('010.53','drawing','gap above/right of first lower disk','pale diagonal trace')
item('010.54','drawing','below lower-left outline of second lower disk','small pendant stroke','his hand')
item('010.55','drawing','interior of right angular trace at foot','separate pale rising diagonal')
item('010.56','drawing','upper end of right angular trace','dark short upright and two separated flecks')
item('010.57','drawing','inside first lower disk','pale horizontal trace, including faint left continuation')
item('010.58','drawing','far right margin, level with lower disks','pale irregular patch, origin and role undetermined')
item('010.59','text','lower-left corner','archive numeral 9, recorded in % archive sheet number: 9','another unnamed hand')
# One record per unresolved local reading/role; C source rows may encompass several loci.
doubts=[]
for d in diffs:
 if d['C_doubt_status']=='retained' or d['id'] in ['C010-D07','C010-D08','C010-D09','C010-D12','C010-D13','C010-D14','C010-D15','C010-D17']:
  alts=[]
  if d['id'] in ['C010-D01','C010-D12']:alts=['filled point']
  elif d['id'] in ['C010-D04','C010-D13']:alts=['open-looking circle']
  elif d['id']=='C010-D03':alts=['hatching']
  else:alts=['transfer or surface trace; role and hand undetermined']
  doubts.append({'location':d['location'],'reading':d['reading'],'alternatives':alts,'confidence':d['confidence'],'reason':d['evidence'],'crop':d['readers_crop'],'difference_id':d['id']})
report={'scan':10,'reader':'C','start_utc':'2026-11-20 11:49:02 UTC','end_utc':'2026-11-20 12:02:43 UTC','full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,'differences':diffs,'doubts':doubts,'inventory':inv,
'notes':{
 'page_content':'One landscape sheet with three rows of disk drawings (nine, seven, five), twelve small graph groups, grouping braces and two encircling ovals. Five labels read OK; one reads ou; a heavy question mark is present. Archive numeral 9 is lower left.',
 'authors_own_uncertainty':{'exact_words_or_marks':['?'],'location':'above the overdrawn second disk of the lowest row','observation':'A heavy curved head and detached lower dark spot are visible on half a. No accompanying proposition is written.'},
 'title_date_page_counts':{'title':None,'date':None,'manuscript_page_number':None,'archive_sheet_number':'9','scans_read':1},
 'mathematics_led_reading_decisions':[],'mathematical_work':'Visual transcription and structural source checking only. No mathematical computation, correspondence, theorem reconstruction or proof check was performed.',
 'H_status':'metadata hua_has=desc. H page 9 is a drawing description. H fields are null and diff_H is false throughout; no H text-collation rows were created.',
 'source_section_classification':{'Notation table':'Four rows checked as notation; they do not create C-doubt records.','Doubtful readings':'Five actual source rows. Row 1 maps to C010-D01; row 2 to C010-D02a/b/c; row 3 to C010-D03; row 4 to C010-D04; row 5 to C010-D05a/b/c. Each source row is retained; compound rows are split only to record separate physical loci.','Abbreviations':'OK, possible expansion okay, retained as contextual apparatus only; the transcription keeps OK.','Legibility':'Contextual statement concerning approximate curves; no additional C doubt.','Steps marked as unverified':'Question mark and five OK labels checked against the page. This source note supplies no proof-check event.'},
 'inventory_refinements':'The archive numeral is explicitly inventoried. Paired parentheses, the upper grouping oval, uncertain superposed marks, and newly recorded faint traces have separate entries. The final lower disk visibly contains four strokes; C inventory wording had three, while C.tex itself already drew four.',
 'workflow':{'image_order':['full once for layout','half a once','half b once','13 tight crop enlargements, each viewed once'],'full_dimensions':[1680,1208],'half_dimensions':[900,1208],'half_offsets':{'a':[0,0],'b':[780,0]},'half_offset_basis':'full width minus half width: 1680-900=780 for b; a begins at full x=0','scope':'Only scan010 assigned images, assigned packet, brief, preamble, notation snapshot and crop helper read. No OCR, research, delegation, compiler, package installation, other readers or other page images.'},
 'crop_limits':'Target marks remain inside every crop. Crop 04 includes only the tip of the neighbouring lower grouping brace as context; that brace was already read in the supplied half. The angular-trace crop 05 includes the bottom rim of the neighbouring disk as context. No crop was repeated.',
 'geometry':'C drawing paths were reused after individual visual comparison. New pale marks have no supplied character or mathematical role. The overdrawn disk uses a visible graphic plus an invisible deleted copy to avoid a generic horizontal strike. Its unsure marker concerns cancellation versus hatching.',
 'source_validation':'Passed direct checks of balanced braces and environments, reviewed control sequences, existing crop references, complete C source-doubt mapping, archive inventory, and all reported changed readings. See validation.json. No compilation or render claimed.'},
'notation':[
 {'location':'above upper disks 3, 7, 8 and lower disks 1, 5','visible':'round O with raised/tall two-armed K; no terminal punctuation','latex':'OK'},
 {'location':'far upper right, before variant disk','visible':'connected lower-case ou inside drawn parentheses','latex':'ou; parentheses reproduced by TikZ curves'},
 {'location':'above lower second disk','visible':'heavy question-shaped head and separated dot','latex':'?'},
 {'location':'small graphs across all three rows','visible':'solid spots, open-looking endpoints, unheaded strokes, and a three-cornered closed graph','latex':r'\bullet, \circ, unheaded tikzcd edges; local \unsure markers retained'},
 {'location':'upper seventh graph, middle vertex','visible':'heavy body with an open right hook','latex':r'\unsure{\bullet|\circ}'},
 {'location':'lower left first endpoint and lower middle first endpoint','visible':'pale centers surrounded by dark rims','latex':r'\unsure{\circ|\bullet} at each independently read locus'},
 {'location':'first vertex of final lower graph','visible':'black patch with a lower opening and bent return','latex':r'\unsure{\bullet|\circ}'},
 {'location':'lower-left corner','visible':'pencilled 9','latex':'% archive sheet number: 9'}],
'check_events':[],'crops':crops,
'brief_feedback':['For a pure drawing, uncertainty about cancellation versus hatching concerns the same visible strokes. I used unsure around the complete graphic and recorded both state candidates in its source comment and report, with an invisible deleted copy preserving the primary annotation.','Faint physical patches support shapes while their role, hand and surface origin remain unsettled; these are reproduced graphically without a character candidate.','Compound C doubt-table rows 2 and 5 cover spatially separate marks. The report maps each of their local records back to the one source row, preserving a source-row count of five.']}
(HERE/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote report.json:',len(diffs),'decision rows;',sum(d['diff_C'] for d in diffs),'C differences;',len(inv),'inventory entries')
