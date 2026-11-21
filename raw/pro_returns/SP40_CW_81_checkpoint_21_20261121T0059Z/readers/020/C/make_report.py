from pathlib import Path
import json
from datetime import datetime, timezone

base = Path('/workspace/scratch/94548b74fbe0')
out = base / 'out/readers/020/C'
plan = json.loads((out / 'crop_plan.json').read_text())
crop_by_id = {x['id']: x for x in plan}
differences = []

def add(id, location, C, H, reading, evidence, confidence, kind, diff_C, diff_H,
        crop, source_row=None, status=None, sublocus=None, bbox=None, **extra):
    c = crop_by_id[crop] if crop else None
    row = dict(id=id, location=location, C=C, H=H, reading=reading,
               evidence=evidence, confidence=confidence, kind=kind,
               diff_C=diff_C, diff_H=diff_H, C_doubt_status=status,
               readers_crop=c['path'] if c else None,
               bbox={'coordinate_system':'original full scan, top-left origin',
                     'xyxy':bbox or (c['bbox'] if c else None)},
               C_source_doubt_row=source_row, local_sublocus=sublocus)
    row.update(extra)
    differences.append(row)

add('020C-D01','Opening line, superscript of Pi_I',
    r'\Pi_I^{\unsure{\circ|0}}',r'\Pi_I^0',r'\Pi_I^{\unsure{\circ|0}}',
    'Small closed, almost circular outline above the I. Its shape supports circle and a small zero; neither reading is removed.',
    'medium','misread symbol or index',False,True,'01','C-R01','retained','opening Pi_I',
    qualification='H zero remains an explicit alternative; this is a qualified primary-reading difference.')
add('020C-D02','Second line, superscript of Pi_J',
    r'\Pi_J^\circ',r'\Pi_J^0',r'\Pi_J^\circ',
    'Small closed angular-rounded ring above the hooked J. Local circle/zero doubt remains; the first-occurrence convention prints circle here without a second wrapper.',
    'medium','misread symbol or index',False,True,'02','C-R01','retained','opening Pi_J',
    local_alternatives=[r'\circ','0'],qualification='H zero remains a local alternative.')
add('020C-D03','Second line, distinctes de U_{J,i}',
    r'\deleted{\Pi}U_{J,i}',r'U_{J,i}',r'\deleted{\Pi}U_{J,i}',
    'A horizontal Pi head and two inner upright strokes survive within the larger curved U strokes. The hooked J, comma, dotted i and following comma are visible.',
    'high','omission',False,True,'03')
add('020C-D04','Third prose line, word between les and parmi',
    r'\unsure{clas.|deux}',r'deux',r'\unsure{deux|clas}.',
    'Initial low loop with a tall returning stem and a low undulating continuation supports deux first; the same compressed group still permits clas. The terminal point is treated separately in D05.',
    'medium','misread word',True,False,'04','C-R02','retained',
    qualification='C first candidate clas survives as the alternative; H deux is the selected primary word.')
add('020C-D05','Terminal point after deux/clas before parmi',
    r'clas.',r'deux parmi',r'\unsure{deux|clas}. parmi',
    'A separate compact dark point follows the end of the disputed word before the large gap leading to parmi. The point is outside the uncertainty wrapper and applies to both word readings.',
    'high','omission',False,True,'04',bbox=[980,305,1030,350])
add('020C-D06','First paired intersection, positive Sigma subscript',
    r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+',r'\Sigma_i^+',
    r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+',
    'A long low left-returning stem lies under a shorter upward hook and a detached high point. An overwritten J with i is the first complete state; single j and i remain supported alternatives.',
    'low','misread symbol or index',False,True,'05','C-R03','retained',
    qualification='H i remains an explicit alternative; no correction chronology is asserted.')
add('020C-D07','Cancelled Sigma immediately before U est un voisinage',
    r'\deleted{\unsure{\Sigma_i|\Sigma_j}}',r'\struck{\ill{}}',
    r'\deleted{\Sigma_{\unsure{j|i}}}',
    'The Sigma head, diagonal body and lower arm remain readable under crossing strokes. The lowered sign has a returning descender, favouring j, while the crossing strokes leave i supported.',
    'low',r'readable ink left as \ill{}',True,True,'06','C-R04','retained',
    qualification='The cancelled Sigma is recovered; its index remains qualified. The single H ill placeholder is counted once.')
add('020C-D08','Index of E after voisinage de',
    r'E_{\unsure{i|j}}',r'E_i',r'E_i',
    'A short downward-curving lowered stroke is followed by a spatially separate lower comma. There is no continuing j descender in the complete local target.',
    'medium','other',True,False,'07','C-R05','resolved',bbox=[1375,785,1425,840])
add('020C-D09','Overwritten letter at voisinage de E_i',
    r'\deleted{\Sigma}E_i',r'E_i',r'\deleted{\Sigma}E_i',
    'Thin oblique Sigma strokes run inside the heavier upright and three E arms. The predecessor is preserved separately from the index decision D08.',
    'high','omission',False,True,'07',bbox=[1325,765,1395,830])
add('020C-D10','Comma after voisinage de E_i before et',
    r'E_i,\ et',r'E_i\ et',r'E_i, et',
    'The lower curved comma is detached below and right of the short index; both marks fit completely in the crop.',
    'high','omission',False,True,'07',bbox=[1385,805,1430,845])
add('020C-D11','First nonemptiness formula, Sigma predecessor beneath E_i',
    r'\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i',
    r'\overline{\Sigma_i^+}\cap E_i',
    r'\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i',
    'Diagonal upper and lower strokes remain between the darker E upright and horizontal arms. The long closure rule over the preceding Sigma and plus is separately confirmed and already in C/H.',
    'high','omission',False,True,'08',bbox=[470,940,540,1010])
add('020C-D12','Second nonemptiness formula, E predecessor beneath barred Sigma_i^-',
    r'\overline{\deleted{E}\Sigma_i^-}',r'\overline{\Sigma_i^-}',
    r'\overline{\deleted{E}\Sigma_i^-}',
    'A lighter upright and inner arm remain under the stronger oblique Sigma body; the minus and separate long rule above the complete group are visible.',
    'high','omission',False,True,'09',bbox=[745,915,860,990])
add('020C-D13','Second nonemptiness formula, Sigma predecessor beneath E_i',
    r'\cap\deleted{\Sigma}E_i',r'\cap E_i',r'\cap\deleted{\Sigma}E_i',
    'Oblique remnants lie between the three E arms, as a complete separate local overwrite. The endpoint is a period.',
    'high','omission',False,True,'09',bbox=[905,925,985,995])
add('020C-D14','On ... donc following nonemptiness formulas',
    r'On \unsure{voit|sait} donc',r'On voit donc',r'On sait donc',
    'The first low stroke turns back on itself in an s-shaped return; an oval a and the high i mark precede the tall final t. The enlarged full verb supports sait.',
    'medium','misread word',True,True,'10','C-R10','resolved')
add('020C-D15','Between est and the cancelled word before the count',
    r'est en \deleted{\unsure{tout|est}}',r'est \struck{\ill{}}',
    r'est en \deleted{\unsure{tout|est}}',
    'A separate low loop and long n continuation form the live word en; the following cancellation begins farther right.',
    'high','omission',False,True,'11',bbox=[1315,1045,1420,1110])
add('020C-D16','Cancelled word at right before count',
    r'\deleted{\unsure{tout|est}}',r'\struck{\ill{}}',
    r'\deleted{\unsure{tout|est}}',
    'A tall left loop, flattened middle run and raised right termination survive the long crossing strokes. Tout remains the strongest word; est remains supported under the crossing.',
    'low',r'readable ink left as \ill{}',False,True,'11','C-R06','retained',
    qualification='One H cancelled ill placeholder is replaced by one explicitly qualified word.')
add('020C-D17','Parenthesis, adverb before la',
    r'\unsure{aussi|ainsi}',r'aussi',r'\unsure{aussi|ainsi}',
    'A compressed low initial group, a distinct turning s-like stroke and a final dotted i support aussi; the nearly level early run still permits ainsi.',
    'medium','other',False,False,'13','C-R11','retained',
    qualification='Same primary as H; its different editorial qualification produces no H count.')
add('020C-D18','Parenthesis, abbreviation before par récurrence',
    r'\unsure{dém.|dem.}',r'dém.',r'\unsure{dèm.|dém.|dem.}',
    'A very short raised stroke beside the d/e group tilts down toward the right. Grave is selected first; the nearly upright/rejoined mark also supports acute or no independently assigned accent. The endpoint point is clear.',
    'low','misread word',True,True,'13','C-R07','retained',
    qualification='H dém. and both original C accent-presence candidates remain explicit alternatives.')
add('020C-D19','Lemma heading sentence, superscript of Pi_I',
    r'\Pi_I^\circ',r'\Pi_I^0',r'\Pi_I^\circ',
    'The raised closed ring has a slight left protrusion and an oval hollow. Circle and zero remain locally supported; the printed recurrence is circle after the first page qualifier.',
    'medium','misread symbol or index',False,True,'14','C-R01','retained','lemma Pi_I',
    local_alternatives=[r'\circ','0'],qualification='H zero remains a local alternative.')
add('020C-D20','Lemma union index, form under the K',
    r'\alpha\in\deleted{\unsure{I}}K',r'\alpha\in K',
    r'\alpha\in\unsure{\deleted{I}K|K}',
    'Top and bottom horizontal serif-like strokes and a shared upright remain at the K. A cancelled I beneath K is supported, but those strokes can belong to the single K form; complete states are retained.',
    'medium','misread symbol or index',False,True,'14','C-R08','retained',
    qualification='The original blank alternative is made explicit as K alone. H K remains a complete-state alternative.')
add('020C-D21','Lemma, large U-shaped indexed union operator',
    r'\bigcup',r'\bigcup','G01.1 and G01.2 literal union bowl',
    'The rounded bowl has a small closed returning loop at the upper right and a thin lower-left retrace. The two local paths preserve those inspected components; no generic visible bigcup is drawn over them.',
    'high','drawing or diagram',True,True,'14',bbox=[1015,1675,1090,1755],
    graphic_group='G01',shape_confidence='high',geometric_precision='manual approximation, not rendered or metric-validated')
add('020C-D22','Lemma, upper brace beneath inserted hatted Sigma',
    r'\overbrace{\Sigma_\alpha^+\cup E_\alpha}^{\inserted{\widehat{\Sigma}_\alpha^+}}',
    r'\note{au-dessus de ... il écrit \widehat{\Sigma}_\alpha^+}',
    'G02.1 complete brace plus G02.2 left loop/return; inserted label retained once',
    'The left brace span contains a closed loop and a heavy returning run; the middle rises in a short angular step; the right span ends in a downturned hook. The upper hatted Sigma label is unchanged.',
    'high','drawing or diagram',True,True,'14',bbox=[1105,1650,1365,1690],
    graphic_group='G02',shape_confidence='high',geometric_precision='manual approximation, not rendered or metric-validated',
    H_apparatus='The note supplies the same upper label at the same physical locus; no duplicate manuscript formula or invented prose is counted.')
add('020C-D23','Inserted non vide above partie de I',
    r'\inserted{\deleted{non vide}}',r'\add{\uncertain{non vide}}',
    r'\inserted{\rlap{non vide}\phantom{\deleted{non vide}}} with G03 cancellation path',
    'The words non vide survive an oblique crossing rule with a hooked right return. The literal cancellation replaces a generic additional strike; words, insertion state and deleted annotation each occur once.',
    'high','deletion state (struck given live or live given struck)',True,True,'15',
    bbox=[1140,1760,1340,1815],graphic_group='G03',
    C_count_basis='C already marks deletion; the C change is the explicit slanted/hooked cancellation geometry.',
    H_count_basis='One physical non vide cluster: cancellation state and geometry counted together.')
add('020C-D24','Long curved guide from after partie above de I',
    r'\inserted{\deleted{non vide}} without literal guide',
    r'\add{\uncertain{non vide}} without literal guide',
    'G04 complete curved guide; adjoining partie and de I, retained exactly once',
    'A separate curve starts after partie, rises across the top of de I and runs toward a small downturned right endpoint. It remains distinct from the upper cancellation rule.',
    'high','drawing or diagram',True,True,'15',bbox=[1170,1780,1365,1860],
    graphic_group='G04',shape_confidence='high',geometric_precision='manual approximation, not rendered or metric-validated')
add('020C-D25','After first universal alpha in K, cancelled prose',
    r'\deleted{on a}',r'\struck{\ill{}}',r'\deleted{on a}',
    'The small opening oval, n hump and a loop remain visible along the cancelling horizontal stroke.',
    'high',r'readable ink left as \ill{}',False,True,'17',bbox=[600,1970,775,2020])
add('020C-D26','Membership sign immediately before pi_0 in lemma',
    r'\deleted{\unsure{\Rightarrow}}\in',r'\in',
    r'\unsure{\deleted{\Rightarrow}\in|\deleted{\rightarrow}\in|\in}',
    'The live membership-shaped outer curve and central stroke are accompanied by an angular right-returning head. A cancelled double arrow is retained first; the single-shaft arrow candidate and a single reworked membership form remain explicit complete alternatives.',
    'low','omission',False,True,'17','C-R09','retained',bbox=[935,1928,1005,1995],
    qualification='Original arrow/blank scope is retained and made a complete-state choice. H membership alone survives as an alternative; no writing chronology is asserted.')

source_lines=(base/'packets/020/C_doubts.txt').read_text().splitlines()
in_doubts=False
source_rows=[]
for line in source_lines:
    if line=='## Doubtful readings':
        in_doubts=True
        continue
    if in_doubts and line.startswith('## '):
        break
    if in_doubts and line.startswith('| 20 |'):
        cells=[c.strip() for c in line.split('|')[1:-1]]
        source_rows.append({'id':f'C-R{len(source_rows)+1:02d}',
                            'raw_row':line,'location':cells[1],
                            'reading':cells[2],'other_readings':cells[3],
                            'confidence':cells[4],'source_evidence':cells[5],
                            'contextual_preference':cells[6]})
assert len(source_rows)==11
for s in source_rows:
    locals_=[d for d in differences if d['C_source_doubt_row']==s['id']]
    s['local_decisions']=[{'difference_id':d['id'],'sublocus':d['local_sublocus'] or d['location'],
                         'status':d['C_doubt_status'],'reading':d['reading'],
                         'crop':d['readers_crop']} for d in locals_]
    s['source_row_status']='resolved' if all(d['C_doubt_status']=='resolved' for d in locals_) else 'retained'
    assert locals_

doubts=[]
def doubt(source,loc,reading,alts,conf,reason,crop,printed=None):
    d={'source_row':source,'location':loc,'reading':reading,'alternatives':alts,
       'confidence':conf,'reason':reason,'crop':crop_by_id[crop]['path']}
    if printed is not None:d['printed_at_this_occurrence']=printed
    doubts.append(d)
doubt('C-R01','First opening Pi_I superscript',r'\circ',['0'],'medium','Closed tiny ring permits both readings.','01',r'\unsure{\circ|0}')
doubt('C-R01','Second opening Pi_J superscript',r'\circ',['0'],'medium','Angular-rounded hollow ring permits a small zero.','02',r'\circ')
doubt('C-R01','Lemma Pi_I superscript',r'\circ',['0'],'medium','Small oval ring with protruding start permits a small zero.','14',r'\circ')
doubt('C-R02','Word before parmi','deux',['clas'],'medium','Initial returning stem and low continuation support both word forms; the terminal point is definite.','04',r'\unsure{deux|clas}.')
doubt('C-R03','First positive Sigma index',r'\deleted{J}i',['j','i'],'low','Long hooked stem, short upper hook and high point leave glyph and overwrite state open.','05')
doubt('C-R04','Cancelled Sigma index before U est un voisinage','j',['i'],'low','Descender favours j; cancellation can contribute part of that return.','06',r'\deleted{\Sigma_{\unsure{j|i}}}')
doubt('C-R06','Cancelled word after en','tout',['est'],'low','Crossing strokes cut initial and terminal rises.','11',r'\deleted{\unsure{tout|est}}')
doubt('C-R07','Abbreviation in parenthesis','dèm.',['dém.','dem.'],'low','Short near-upright/down-right raised mark has unsettled direction and independence.','13')
doubt('C-R08','Union index below the large cup',r'\deleted{I}K',['K'],'medium','Serif-like top, foot and upright support an I predecessor and also a single K form.','14')
doubt('C-R09','Reworked membership before pi_0',r'\deleted{\Rightarrow}\in',[r'\deleted{\rightarrow}\in',r'\in'],'low','Right angular head and shaft are readable; predecessor identity and cancellation attachment remain open.','17')
doubt('C-R11','Adverb before la','aussi',['ainsi'],'medium','Flat early run and final dotted i do not settle the intermediate letters.','13')

inventory=[]
def inv(element,kind,position,objects,hand='his hand',**extra):
    item={'sheet_kind':'text','hand':hand,'element':element,'kind':kind,
          'position':position,'first_words_or_objects':objects,'transcribed':'yes'}
    item.update(extra);inventory.append(item)
inv('020C-I01','text','Top three prose lines','Ainsi les classes ... les deux|clas. parmi')
inv('020C-I02','deletion','Second line within U','Pi predecessor before U_{J,i}')
inv('020C-I03','display','Upper paired intersections','U_{J,i} cap Sigma_{deleted J i|j|i}^+, U_{J,i} cap Sigma_i^-')
inv('020C-I04','deletion','First positive Sigma index','Qualified J predecessor beneath i; j and i complete alternatives')
inv('020C-I05','text','Beneath paired display through voisinage line','qui sont non vides. Or les deux classes ... et')
inv('020C-I06','deletion','Before U est un voisinage','Cancelled Sigma_{j|i}')
inv('020C-I07','deletion','voisinage de E_i','Sigma predecessor under E')
inv('020C-I08','display','Nonemptiness line','Two long-barred Sigma expressions intersect corrected E_i; comma then period')
inv('020C-I09','deletion','First nonemptiness E_i','Sigma predecessor')
inv('020C-I10','deletion','Second nonemptiness barred Sigma_i^-','E predecessor')
inv('020C-I11','deletion','Second nonemptiness E_i','Sigma predecessor')
inv('020C-I12','text','Middle count paragraph','On sait donc ... (ce qui achève aussi|ainsi la dèm.|dém.|dem. par récurrence ...).')
inv('020C-I13','deletion','After est en','tout|est')
inv('020C-I14','text','Lemma heading','Single underline under Lemme',emphasis='one underline, exact word span')
inv('020C-I15','text','Lower lemma sentence outside the formula and guide group','Toute classe ... de la forme; où K est une; et ... tels que ... on ait')
inv('020C-I16','display','Lemma central expression','X setminus indexed large cup (Sigma_alpha^+ cup E_alpha)',source_group='G01--G02 complete figure')
inv('020C-I17','drawing','Large indexed union','Rounded bowl with upper-right loop and lower-left retrace',
    components=['G01.1 main bowl and closed right return','G01.2 short lower-left retrace'])
inv('020C-I18','deletion','Index below union','Qualified I predecessor beneath K; K-only state retained')
inv('020C-I19','insertion','Above brace','Hatted Sigma_alpha^+',source_group='one node in G01--G02; no duplicate label')
inv('020C-I20','drawing','Brace over parenthesized union','Main curved/stepped brace and left closed loop',
    components=['G02.1 complete brace including right endpoint','G02.2 closed left loop and dark returning run'])
inv('020C-I21','text','Guide-bearing group in lemma','partie de I,',source_group='G03--G04 contains these words and comma exactly once; et is outside')
inv('020C-I22','insertion','Above partie de I','non vide',state='inserted wording is visibly cancelled')
inv('020C-I23','deletion','Same raised non vide','non vide with literal oblique cancellation',
    components=['G03 slanted crossing with hooked right return'],
    annotation='visible words in rlap; deleted state only in invisible phantom copy; no generic extra visible strike')
inv('020C-I24','drawing','From after partie across de I','Long curved insertion guide',components=['G04 complete curve and downturned right endpoint'])
inv('020C-I25','margin note','Lower left, rising to right','K est ne empty / si I ne empty',orientation='slanted; approximate typesetting angle +23 degrees')
inv('020C-I26','deletion','After first universal alpha in K','on a')
inv('020C-I27','deletion','Immediately before pi_0','Qualified arrow predecessor / reworked membership states')
inv('020C-I28','display','Penultimate body line','hat Sigma_alpha^+ cap hat Sigma_beta^+ = empty')
inv('020C-I29','display','Final body line','Parenthesized double implication with unbarred Sigma_alpha^+ cap Sigma_beta^+ = empty, followed by period')
inv('020C-I30','text','Bottom left archive numeral','19','undetermined hand',source_representation='% archive sheet number: 19')

notation=[
 {'location':'Three Pi superscripts','sign':'small closed ring','latex':r'\unsure{\circ|0}; later \circ','status':'Three local circle/zero doubts recorded independently under C-R01.'},
 {'location':'Opening U and three subsequent U occurrences','sign':'U with hooked J, comma and dotted i','latex':r'U_{J,i}','status':'Each local occurrence visually inspected; the first has the Pi predecessor.'},
 {'location':'Upper paired intersections','sign':'Short Sigma head strokes and raised plus/minus','latex':r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\ \Sigma_i^-','status':'Source selects ordinary Sigma head forms here; no additional closure rule is supplied.'},
 {'location':'Two nonemptiness formulas','sign':'Separate long upper rules spanning the raised signs','latex':r'\overline{\Sigma_i^+};\ \overline{\deleted{E}\Sigma_i^-}','status':'Both observed long rules confirmed; both are already represented in current C/H.'},
 {'location':'Nonemptiness formulas, margin note and two final equalities','sign':'Slashed small oval','latex':r'\varnothing','status':'Six local empty-set signs read; H emptyset syntax conveys the same selected reading and receives no macro-only difference.'},
 {'location':'Count prose, end of parenthesis, count formula','sign':'nb; low linked card','latex':r'nb;\ \operatorname{card} I','status':'Both nb occurrences and lowercase card retained; no abbreviation expansion in the transcription.'},
 {'location':'Parenthesis opening','sign':'Two small down-right marks above the middle e of achève','latex':'achève','status':'Grave accent retained after crop12; complete qui descender remains attached to qui once.'},
 {'location':'Parenthesis abbreviation','sign':'Near-upright/down-right tiny raised mark; terminal point','latex':r'\unsure{dèm.|dém.|dem.}','status':'Every supported accent/no-accent alternative remains local.'},
 {'location':'Parenthesis after abbreviation','sign':'Compressed par, then acute on récurrence','latex':'par récurrence','status':'Source selects full par and accented récurrence; the compressed run and local acute were inspected, not normalized from another page.'},
 {'location':'Lemma start and final equalities','sign':'Roof-shaped marks above Sigma','latex':r'\widehat{\Sigma}_\alpha^+;\ \widehat{\Sigma}_\beta^+','status':'One inserted upper label and two final hatted objects; the final parenthesized pair has ordinary Sigma forms.'},
 {'location':'Final parenthesis','sign':'Two shafts with heads at both ends','latex':r'\Longleftrightarrow','status':'Same author-written relation retained without an equivalence proof check.'},
 {'location':'Lower-left note','sign':'K est ne empty / si I ne empty','latex':r'K\text{ est }\ne\varnothing;\ \text{si }I\ne\varnothing','status':'Complete slanted note read; no source difference.'}
]

graphic_groups=[
 {'group':'G01--G02','observed_bbox':[900,1620,1380,1805],
  'local_origin_full_scan':[900,1600],'local_axes':'x right, y down; 1 local unit = 1 source pixel',
  'drawing_rectangle':[0,0,510,210],'display_units':'x=0.018cm, y=-0.018cm','baseline_local_y':145,
  'node_anchor':'base west; inner sep=0pt; outer sep=0pt',
  'text_boundaries':'Only X, setminus, union index alpha in qualified I/K, (Sigma_alpha^+ cup E_alpha), and inserted hatted Sigma label. No adjoining French words or punctuation are included.',
  'paths':['G01.1','G01.2','G02.1','G02.2'],
  'duplication_control':'Literal bowl is the only visible large union. Literal brace is the only visible brace. No generic bigcup or overbrace is superimposed.',
  'precision':'Manually approximated from the one complete crop; no rendering or metric comparison.'},
 {'group':'G03--G04','observed_bbox':[990,1760,1410,1900],
  'local_origin_full_scan':[990,1755],'local_axes':'x right, y down; 1 local unit = 1 source pixel',
  'drawing_rectangle':[0,0,420,150],'display_units':'x=0.018cm, y=-0.018cm','baseline_local_y':110,
  'node_anchor':'base west; inner sep=0pt; outer sep=0pt',
  'text_boundaries':'Exactly partie, de I, and non vide. The comma after I is inside the de I node. The following et remains outside this group.',
  'paths':['G03','G04'],
  'phantom_annotation':'The inserted node contains visible rlap{non vide} and an invisible phantom{deleted{non vide}}; only G03 supplies the visible cancellation rule.',
  'precision':'Manually approximated from the one complete crop; no rendering or metric comparison.'}
]

audit=json.loads((out/'image_audit.json').read_text())
counts={
 'difference_rows':len(differences),'diff_C_true':sum(d['diff_C'] for d in differences),
 'diff_H_true':sum(d['diff_H'] for d in differences),
 'actual_C_doubt_source_rows':len(source_rows),
 'C_doubt_source_rows_resolved':sum(s['source_row_status']=='resolved' for s in source_rows),
 'C_doubt_source_rows_retained':sum(s['source_row_status']=='retained' for s in source_rows),
 'C_doubt_local_decisions':sum(d['C_source_doubt_row'] is not None for d in differences),
 'C_doubt_local_decisions_resolved':sum(d['C_doubt_status']=='resolved' for d in differences),
 'C_doubt_local_decisions_retained':sum(d['C_doubt_status']=='retained' for d in differences),
 'remaining_local_doubts':len(doubts),'inventory_items':len(inventory),
 'crop_files':len(plan),'successful_image_views':20,'failed_unseen_deliveries':0,
 'literal_path_commands':6,'mathematical_check_events':0
}

report={
 'scan':20,'reader':'C','start_utc':(out/'start_utc.txt').read_text().strip(),
 'end_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'differences':differences,'doubts':doubts,'inventory':inventory,
 'notes':{
  'page_content':'The author continues the class-count argument: the opening identifies the classes of Pi_I using classes of Pi_J and the two written intersections. He writes that the two classes are nonempty, citing a neighbourhood of corrected E_i and the two barred nonemptiness expressions. He then writes the count (n-1)+2=n+1=card I+1 and describes this as completing the induction on the number of classes. The underlined Lemme states a representation by X minus an indexed union of Sigma_alpha^+ cup E_alpha, with the added hatted-Sigma label over that group; the body gives the written membership and pairwise-disjointness clauses. The final parentheses expressly relate the hatted and ordinary pairwise-intersection expressions by a double implication. These are attributed manuscript assertions, not results checked by this reading.',
  'authors_own_uncertainty':'No explicit question mark or verbal uncertainty phrase was found. The exact raised words non vide are cancelled. All unsure alternatives in reading.tex are editorial ink uncertainties.',
  'title_date_page_counts':'One sheet. Underlined heading Lemme; no date and no separate manuscript page-number label. The lower-left archive numeral 19 is recorded only in the required comment, with undetermined hand. H page 19 maps to our scan 20.',
  'mathematics_led_reading_decisions':'No formula was repaired from expected mathematics. Long upper rules were inspected locally. The first paired Sigma index, the cancelled Sigma index, the union-index state and the reworked membership retain explicit alternatives. No calculation, proof check, geometric-extrema check or pixel comparison was performed.',
  'source_administration':'No cotefile command is added on scan 20. The H editorial note about adjacent pages was read as apparatus; those other pages were not opened or collated. H emphasis and our single underline agree on the word Lemme. Ordinary line-wrap/display placement and the approximate margin rotation do not create correction counts.',
  'source_silent_choices':'The complete source selects achève with a grave, par in full, récurrence with an acute, où with a grave, both occurrences of nb without a following point, and lowercase card. It retains the upper-display plus/minus signs, the first-intersection comma, the comma after voisinage de E_i, comma/period endpoints of the nonemptiness pair, both final hats, and the final parenthesis and period. The latter two Pi superscripts print circle while their zero alternatives remain explicit in the report. The tiny final component of la is represented through that word once, not as a second free point. The source contains no extra detached-mark path beyond the six declared guide/operator/brace/cancellation paths.',
  'S_coverage':{
    'row_id':'SA01-K81-06','source_item':'SA01-29','stated_range':'81/15-22',
    'stated_author_scope':'Recorded author: Claude Opus 5.5 at effort max, reader R4 (no scan viewed). The row supplies witness proposals only.',
    'local_confirmations':[
      {'location':'First nonemptiness Sigma_i^+','crop':'crop08_first_barred_formula.png','reading':r'\overline{\Sigma_i^+}','current_C_has_bar':True,'current_H_has_bar':True,'witness_correction_count':0},
      {'location':'Second nonemptiness Sigma_i^-','crop':'crop09_second_barred_formula.png','reading':r'\overline{\deleted{E}\Sigma_i^-}','current_C_has_bar':True,'current_H_has_bar':True,'witness_correction_count':0}],
    'example_matching':'The exact quoted index-1/i.e. example, the strict-inclusion chain, and the U_s example are absent from this sheet. The local positive nonemptiness expression uses i and already has its bar in C/H. The sheet has no literal i.e. phrase. The parenthesized final double implication is recorded as its own author-written relation, not substituted for an S example.',
    'source_flags':'No S proposal is promoted to an unobserved bar or a present-witness omission.'},
  'processing_note':audit['text_reading_note']+' A root checkpoint hold began after the complete visual phase and saved reading.tex/image_audit.json/progress.md; work resumed in the same context with no image reopen. The final report and audit were completed after release.',
  'C_source_doubt_map':source_rows,
  'graphic_groups':graphic_groups
 },
 'notation':notation,'check_events':[],
 'crops':[dict(path=x['path'],bbox={'coordinate_system':'original full scan, top-left origin','xyxy':x['bbox']},rotation=x['rotation'],purpose=x['purpose']) for x in plan],
 'brief_feedback':[
  'The source row for the superscript ring is one compound source doubt covering three inspected local occurrences; their later unwrapped circle forms must remain visible in the audit.',
  'For the I/K and arrow/membership loci, the supplied blank alternative was rendered as an explicit complete state. The first candidate is retained; no independent C correction count is assigned to this qualification-only expansion.',
  'The graphic approximations have fixed declared local origins and text boundaries; these declarations provide source bookkeeping, not rendered geometric validation.'
 ],
 'counts':counts,'image_audit':audit,
 'structural_audit':{'status':'pending final source-only check','compilation_performed':False,'rendering_performed':False}
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,indent=2))
