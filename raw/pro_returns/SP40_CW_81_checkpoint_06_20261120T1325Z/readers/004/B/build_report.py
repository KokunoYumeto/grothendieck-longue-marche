from pathlib import Path
import json
from datetime import datetime, timezone
base=Path('/workspace/scratch/94548b74fbe0/out/readers/004/B')
D=[]
def add(id,loc,C,H,reading,evidence,kind='other',dc=False,dh=False,status=None,crop=None,bbox=None,confidence='high',consequence=None):
 row={'id':id,'location':loc,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dc,'diff_H':dh,'C_doubt_status':status,'readers_crop':crop,'bbox':bbox}
 if consequence: row['mathematical_consequence']=consequence
 D.append(row)
add('B004.01','left top, first Greek character in parenthesis',r'\unsure{\eta|\gamma}_{d-1}',r'\eta_{d-1}',r'\unsure{\eta|\gamma}_{d-1}','Short initial downstroke rises into a hump; the right leg descends and turns left. Eta remains the stronger candidate, but the cursive outline leaves gamma supported.',status='retained',crop='01_top_eta_brace.png',bbox=[690,205,997,348],confidence='medium')
add('B004.02','left top, between d-1 index and following equals',r'\unsure{\}|\,}','',r'\unsure{\}|\,}','A tall doubly looped mark is visible independently of the index and equals. Its crossing prevents a secure assignment as a brace or retracing.',kind='omission',dh=True,status='retained',crop='01_top_eta_brace.png',bbox=[820,228,854,323],confidence='low')
add('B004.03','below left box, relation after xf1',r'\unsure{=|\equiv}','=',r'=','Two dark horizontal strokes are visible. The additional pale strokes descend diagonally; no independent third horizontal is seen.',dc=True,status='resolved',crop='02_xf_relation.png',bbox=[260,974,307,1041],confidence='high')
add('B004.04','left, locally cancelled fragment beneath xf1 line',r'\deleted{\unsure{xf_1}}','',r'\deleted{xf_1}','The initial crossed x, tall looped f, and separate lowered 1 survive the parallel local strike strokes.',kind='omission',dc=True,dh=True,status='resolved',crop='03_struck_xf.png',bbox=[174,1072,262,1174],confidence='medium')
add('B004.05','left expansion, first factor, first index',r'f_i',r'f_1',r'f_i','A short lower stem and detached dot follow the first f, unlike the separate undotted 1 in the second factor.',kind='misread symbol or index',dh=True,crop='04_expansion_factors.png',bbox=[395,1120,457,1215])
add('B004.06','left expansion, first factor, index after lambda e',r'e_i',r'e_1',r'e_{\unsure{i|1}}','The e continues into a deep short stem with an upward terminal; the putative dot is joined or absent. The i reading is stronger, but the crop does not securely exclude 1.',kind='misread symbol or index',dc=True,dh=True,crop='04_expansion_factors.png',bbox=[538,1143,585,1210],confidence='low')
add('B004.07','left expansion, first term of second line',r'f_i f_1',r'f_1 f_1',r'f_i f_1','The first f has a small lowered stroke and detached dot; the second f has the single terminal index stroke.',kind='misread symbol or index',dh=True,crop='05_expansion_annotations.png',bbox=[501,1241,605,1361])
add('B004.08','left expansion, first term local cancellation',r'\deleted{f_i f_1}',r'f_1 f_1',r'\deleted{f_i f_1}','A separate rising diagonal traverses the product, distinct from the long page cancellation.',kind='deletion state (struck given live or live given struck)',dh=True,crop='05_expansion_annotations.png',bbox=[501,1241,612,1367])
add('B004.09','left expansion, below first struck product',r'\inserted{f_{i+1}}','',r'\inserted{f_{i+1}}','A tall f followed by lowered i, plus, and 1 is placed directly below the cancelled product.',kind='omission',dh=True,crop='05_expansion_annotations.png',bbox=[531,1361,614,1438])
add('B004.10','left expansion, product after lambda squared',r'e_i e_1',r'e_1 e_1',r'e_i e_1','The first e is followed by a dotted lower i; the second e has an undotted 1.',kind='misread symbol or index',dh=True,crop='05_expansion_annotations.png',bbox=[705,1263,815,1357])
add('B004.11','left expansion, local cancellation after lambda squared',r'\deleted{e_i e_1}',r'e_1 e_1',r'\deleted{e_i e_1}','A thin rising local diagonal crosses both e factors.',kind='deletion state (struck given live or live given struck)',dh=True,crop='05_expansion_annotations.png',bbox=[705,1263,815,1357])
add('B004.12','left expansion, first cross term',r'f_i e_1',r'f_1 e_1',r'f_i e_1','The index following f has a visible upper dot and short lower stem.',kind='misread symbol or index',dh=True,crop='05_expansion_annotations.png',bbox=[967,1238,1060,1361])
add('B004.13','left expansion, annotation under first cross term',r'\inserted{e_{i+1}}','',r'\inserted{e_{i+1}}','A short U-shaped guide lies below the product; e with i+1 is written below it.',kind='omission',dh=True,crop='05_expansion_annotations.png',bbox=[978,1337,1065,1411])
add('B004.14','left expansion, second cross term',r'e_i f_1',r'e_1 f_1',r'e_i f_1','The e has a short lowered stroke and detached dot before the tall f.',kind='misread symbol or index',dh=True,crop='05_expansion_annotations.png',bbox=[1107,1237,1214,1367])
add('B004.15','left expansion, local cancellation of second cross term',r'\deleted{e_i f_1}',r'e_1 f_1',r'\deleted{e_i f_1}','Crossing strokes traverse the second cross term and extend to its lower annotation.',kind='deletion state (struck given live or live given struck)',dh=True,crop='05_expansion_annotations.png',bbox=[1107,1237,1223,1405])
add('B004.16','left expansion, annotation below second cross term',r'\inserted{\deleted{\unsure{-}e_{i+1}}}','',r'\inserted{\deleted{\unsure{-e_{i+1}|e_{i+1}}}}','The lower e and i+1 survive; the horizontal strike passes through the left of the annotation, so an independent initial minus is unresolved.',kind='omission',dh=True,status='retained',crop='05_expansion_annotations.png',bbox=[1097,1352,1226,1432],confidence='low')
add('B004.17','upside-down note, first line',r'\deleted{e_1f_d}','',r'\deleted{e_1f_d}','After rotation, e with lowered 1 and tall f with rounded lower d are readable across a single horizontal local strike.',kind='omission',dh=True,crop='06_upside_down_note.png',bbox=[942,1606,1086,1720])
add('B004.18','upside-down note, second line and range',r'e_i e_1=0\qquad1\leq i\leq d-2','',r'e_i e_1=0\qquad1\leq i\leq d-2','After rotation, both e factors, equals zero, and the entire separate range to their right are clear.',kind='omission',dh=True,crop='06_upside_down_note.png',bbox=[488,1493,1079,1588])
add('B004.19','upside-down note, third line',r'f_i f_1=','',r'f_i f_1=','The two tall looped f characters, dotted i, undotted 1, and equals are visible after rotation; no continuation is written.',kind='omission',dh=True,crop='06_upside_down_note.png',bbox=[935,1415,1080,1496])
add('B004.20','bottom left, first delta formula',r'\deleted{\delta(e_i e_j)=\unsure{0}}','',r'\deleted{\delta(e_i e_j)=\unsure{0}}','The indices i and hooked j are readable. The small terminal loop is crossed by the horizontal cancellation and its retraced end; 0 remains tentative.',kind='omission',dh=True,status='retained',crop='07_struck_delta_end.png',bbox=[67,1579,376,1728],confidence='low')
add('B004.21','bottom left, second delta formula',r'\delta(e_i e_j)=','',r'\delta(e_i e_j)=','The second delta, round delimiters, dotted i, long hooked j, and two equals strokes are visible; the space after equals is blank.',kind='omission',dh=True,bbox={'image':'a','origin':'top-left','xyxy':[420,1593,680,1730]})
add('B004.22','upper right, first case after ei f1, local cancelled coefficient',r'\deleted{\unsure{a|0}}','',r'\deleted{\unsure{a|0}}','A small dark oval with an extended lower/right stroke lies under the minus, before the descended Greek letter. The overwriting leaves a and 0 unresolved.',kind='omission',dh=True,status='retained',crop='08_upper_cancelled_coefficient.png',bbox=[1637,462,1683,503],confidence='low')
add('B004.23','right, underlined equation, cancelled factor after f1e1',r'\deleted{\unsure{f_1}}','',r'\deleted{f_1}','The tall narrow loop and lowered terminal 1 survive several local crossing loops.',kind='omission',dc=True,dh=True,status='resolved',crop='10_underlined_struck_factor.png',bbox=[1465,677,1518,800],confidence='medium')
add('B004.24','right, equation above the long horizontal rule',r'\underline{f_1e_1\cdots}','no underline',r'\uline{$f_1e_1\deleted{f_1}=-e_1f_1=\eta_2=\alpha e_2+\beta f_2$}','A long slightly rising rule extends beneath the complete equation, from the left edge through the final f2.',kind='omission',dh=True,bbox={'image':'b','origin':'top-left','xyxy':[137,680,1110,824]})
add('B004.25','right, below rule, cancelled lead before lower brace',r'\deleted{\unsure{-e_i}}','',r'\deleted{\unsure{-e_i}}','A short minus and looped e-like form survive under a wavy strike; the terminal subscript merges into the brace.',kind='omission',dh=True,status='retained',crop='11_lower_cancelled_lead.png',bbox=[1640,895,1728,947],confidence='low')
add('B004.26','right lower brace, second case, eta subscript',r'\eta_{i\unsure{-|+}1}',r'\eta_{i+1}',r'\eta_{i\unsure{-|+}1}','The subscript contains a short pale bar with a small central rise. A separate vertical cross-stroke cannot be securely traced; minus is retained first and plus remains supported.',kind='misread symbol or index',dh=True,status='retained',crop='12_lower_second_case.png',bbox=[1740,935,1830,1006],confidence='low',consequence='The two retained index readings differ by two index steps; the ink does not authorize replacing the first candidate by the expected adjacent-index pattern.')
add('B004.27','right lower brace, second case, factor after eta',r'\unsure{e|a}_1',r'e_1',r'\unsure{e|a}_1','The initial loop is doubled, with a slanting upper stroke; the lower loop and terminal 1 favor e1, while a1 remains supported.',status='retained',crop='12_lower_second_case.png',bbox=[1827,938,1875,988],confidence='low')
add('B004.28','right lower brace, second case, added e product',r'\deleted{e_{i+1}e_1}',r'e_{i+1}e_1',r'\deleted{e_{i+1}e_1}','A local X is drawn across the two e factors; it is separate from the page-wide diagonals.',kind='deletion state (struck given live or live given struck)',dh=True,crop='12_lower_second_case.png',bbox=[1912,924,2032,1007])
add('B004.29','right, first line of descending equality chain, struck tail',r'\deleted{=e_i\eta_2=e_i(\alpha e_2+\beta f_2)}','',r'\deleted{=e_i\eta_2=e_i(\alpha e_2+\beta\unsure{\bar f_2|\vec f_2|f_2})}','A single horizontal cancellation runs from the equals through the closing parenthesis. The underlying e_i eta_2 and e_i(alpha e_2 + beta ... ) are legible.',kind='omission',dh=True,crop='13_lower_struck_tail.png',bbox=[1608,1036,2168,1153])
add('B004.30','right, end of struck tail, detached short stroke above f2',r'f_2','',r'\unsure{\bar f_2|\vec f_2|f_2}','A short detached nearly horizontal stroke with a hooked right tip lies above the f stem. The image leaves its status as a bar, arrow, or detached upper f stroke unsettled.',kind='omission',dc=True,dh=True,crop='13_lower_struck_tail.png',bbox=[2077,1040,2134,1134],confidence='low')
add('B004.31','right lower brace, first parity label',r'i\text{ imp}',r'i\text{ impair}',r'i\text{ imp}','The label ends after the descending p; no a, i, or r follows before the paper edge.',kind='abbreviation expanded or spelling modernised',dh=True,bbox={'image':'b','origin':'top-left','xyxy':[1187,836,1276,903]})
add('B004.32','lower right, initials after signed delta result',r'\unsure{Q\Phi S|QDS|QPS|QFS}','',r'\unsure{Q\Phi S|QDS|QPS|QFS}','Three compact connected characters remain: a large initial loop, a crossed and looped middle character, and a final S-like sweep. Q Phi S has the strongest outline; all C alternatives remain unresolved.',kind='omission',dh=True,status='retained',crop='14_bottom_initials.png',bbox=[2212,1472,2316,1547],confidence='low')
add('B004.33','whole written area, cancellation state',r'\deleted{...} throughout',r'formulas live; introductory \note says feuillet barred',r'\deleted{...} throughout, with local deletions nested','Two long diagonals cross the writing area, intersecting near the central fold. They span both columns; their page-wide state is encoded on every underlying block.',kind='deletion state (struck given live or live given struck)',dh=True,bbox=[164,168,2190,1554])
add('B004.34','left box, lower boundary',r'\boxed{...}',r'Encadré; no second lower rule',r'\text{\uline{$\boxed{...}$}}','Two distinct lower lines run nearly the full width. They separate near the left, cross locally near the middle, and remain distinct at the right end.',kind='drawing or diagram',dc=True,dh=True,crop='16_box_lower_rules.png',bbox=[105,860,1193,958])
add('B004.35','left box, two detached tiny marks at lower right','','',r'\unsure{\text{\'\'}}','Two dark small tick/dot forms with faint tails sit independently inside the box to the right of the lower cases. Their function is unsettled; the proposed text represents paired ticks without expanding them.',kind='omission',dc=True,dh=True,crop='15_box_detached_ticks.png',bbox=[1057,790,1094,821],confidence='low')
add('B004.36','upper-right f_i f1 case, label after zero',r'\text{si }i\text{ impair}',r'i\text{ impair}',r'\text{si }i\text{ impair}','A compact s-i pair precedes the separately dotted i and impair.',kind='omission',dh=True,bbox={'image':'b','origin':'top-left','xyxy':[501,171,840,235]})
add('B004.37','upper-right f_i f1 case, label after f_i+1',r'\text{si }i\text{ pair}',r'i\text{ pair}',r'\text{si }i\text{ pair}','A small connected s-i pair is written before the separate i and pair.',kind='omission',dh=True,bbox={'image':'b','origin':'top-left','xyxy':[593,234,839,294]})
add('B004.38','left box, range delimiters',r'(1\leq i\leq d-2)',r'pour 1\leq i\leq d-2',r'(1\leq i\leq d-2)','A curved opening and closing parenthesis surround the range above the braced system.',kind='omission',dh=True,bbox={'image':'a','origin':'top-left','xyxy':[333,463,604,550]})
add('B004.39','right, circled beta conclusion',r'\tikz ... circle ... \beta=0',r'\beta=0',r'\beta=0\text{ surrounded by a circle}','A large nearly closed oval surrounds beta equals zero; the alpha equation is outside it to the right.',kind='drawing or diagram',dh=True,bbox={'image':'b','origin':'top-left','xyxy':[881,1276,1105,1441]})
add('B004.40','left, below-box formulas, order and spacing',r'xf_1=f_1x=0 ... \eta=e_{d-1} ... \delta(e_{d-1})=e_{d-2}',r'\eta=e_{d-1}, \delta(e_{d-1})=e_{d-2}; xf_1=f_1x=0 ...',r'xf_1=f_1x=0 ... \eta=e_{d-1} ... \delta(e_{d-1})=e_{d-2}','The xf relation begins at the left beneath the box. The eta and delta pair are separately placed to its upper right; the proposed output follows the left-column reading and records this horizontal pairing.',kind='insertion or placement',dh=True,bbox=[156,902,1321,1062],confidence='medium')
# H supplies a condensed text. Its explicit note and orientation captions are editorial;
# printed punctuation adjoining formula tokens is nevertheless collated separately.
punct=[
('41','left box after e_i e1=0',r'e_i e_1=0',r'e_i e_1=0,',[150,582,361,646]),
('42','left box after f_i f1 cases',r'\end{cases}',r'\end{cases},',[659,614,1110,678]),
('43','left box after f_i e1=e_i+1',r'f_i e_1=e_{i+1}',r'f_i e_1=e_{i+1},',[165,658,435,746]),
('44','below box after eta=e_d-1',r'\eta=e_{d-1}',r'\eta=e_{d-1},',[813,915,1030,983]),
('45','below box after delta(e_d-1)=e_d-2',r'\delta(e_{d-1})=e_{d-2}',r'\delta(e_{d-1})=e_{d-2};',[1073,902,1325,996]),
('46','left xf relation after pair',r'\text{pair}',r'\text{pair};',[688,964,799,1045]),
('47','left expansion after closing parenthesis',r'\lambda(f_i e_1+e_i f_1)',r'\lambda(f_1e_1+e_1f_1),',[1095,1217,1255,1393]),
('48','lower far-left after e2 equation',r'e_2=f_1e_1',r'e_2=f_1e_1,',[47,1274,296,1387]),
('49','lower far-left after e3 equation',r'e_3=f_2e_1',r'e_3=f_2e_1.',[36,1362,308,1454]),
('50','upper-right after e_i e1=0',r'e_i e_1=0',r'e_i e_1=0,',[1407,109,1630,168]),
('51','upper-right after f_i f1 cases',r'\end{cases}',r'\end{cases},',[1760,227,2044,294]),
('52','upper-right after f_i e1 expansion',r'\beta f_{i+1}',r'\beta f_{i+1},',[1902,307,2108,425]),
('53','right underlined equation after beta f2',r'\beta f_2',r'\beta f_2;',[1991,670,2284,812]),
('54','right conclusion after beta=0',r'\beta=0',r'\beta=0,',[2053,1278,2282,1440]),
('55','right conclusion after alpha=plus/minus1',r'\alpha=\pm1',r'\alpha=\pm1,',[2290,1318,2440,1395]),
('56','right signed delta result before bottom eta equation',r'\delta\eta=\pm e_{d-2}',r'\delta\eta=\pm e_{d-2};',[1843,1452,2315,1588]),
('57','right foot after eta=f_d-2 e1',r'\eta=f_{d-2}e_1',r'\eta=f_{d-2}e_1,',[1593,1596,1896,1705])
]
for n,loc,c,h,box in punct:
 add('B004.'+n,loc,c,h,c,'The corresponding formula and its ending are visible; no separate manuscript punctuation mark occupies the following gap.',kind='text not on the page',dh=True,bbox=box)
# Additional visible spatial feature in H: it is acknowledged in H's note, so no false omission row.
inv_src=json.loads(Path('/workspace/scratch/94548b74fbe0/packets/004/C_inventory.json').read_text())
inventory=[]
for i in inv_src:
 inventory.append({k:i[k] for k in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']})
for i in inventory:
 i['hand']='his hand'
 if i['element']=='004.13' or i['element']=='004.14': i['first_words_or_objects']='uncertain minus before e(i+1), locally struck annotation'
 if i['element']=='004.28': i['first_words_or_objects']='=e_i eta_2=e_i(alpha e_2+beta [bar/arrow/plain f_2 uncertain]), locally struck'
extras=[
('004.B32','text','below right-column equation f1e1=-e1f1=eta2','underlining of the whole equation'),
('004.B33','drawing','lower-right conclusion','oval surrounding beta=0'),
('004.B34','drawing','left system box','rectangular enclosure with a second lower rule'),
('004.B35','text','inside lower-right edge of left box','two detached tiny ticks, function uncertain'),
('004.B36','text','above final f2 in locally cancelled right expansion','detached short bar/arrow/letter-top stroke, uncertain'),
('004.B37','margin note','upper far-left paper edge','archive pencil sheet number 3, comment only')
]
for eid,kind,pos,words in extras:
 inventory.append({'sheet_kind':'cancelled_draft','hand':'another unnamed hand' if eid=='004.B37' else 'his hand','element':eid,'kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes'})
doubts=[
('left top Greek letter',r'\eta',[r'\gamma'],'medium','Entry stroke and hump favor eta, but the cursive descending form remains ambiguous.','01_top_eta_brace.png'),
('left top after d-1 index',r'\}', ['retrace/no independently assigned character'],'low','Doubly looped vertical mark cannot be securely assigned.','01_top_eta_brace.png'),
('first expansion factor, e index','i',['1'],'low','Lower stem has a turned-up terminal with no clearly detached dot.','04_expansion_factors.png'),
('lower annotation under second cross term',r'-e_{i+1}',[r'e_{i+1}'],'low','Cancellation supplies a horizontal stroke where a minus would stand.','05_expansion_annotations.png'),
('bottom-left cancelled delta formula terminal','0',[],'low','Terminal loop is overwritten by the strike and its endpoint.','07_struck_delta_end.png'),
('upper-right cancelled coefficient','a',['0'],'low','Dark overwriting leaves a small oval and right extension.','08_upper_cancelled_coefficient.png'),
('lower-right cancelled lead',r'-e_i',[],'low','Terminal index merges with the brace.','11_lower_cancelled_lead.png'),
('lower-right second-case eta index','i-1',['i+1'],'low','The pale horizontal index stroke has only a small central rise.','12_lower_second_case.png'),
('lower-right second-case following factor',r'e_1',[r'a_1'],'low','Overlapping loops prevent confident separation of e and a.','12_lower_second_case.png'),
('right cancelled tail, final f2',r'\bar f_2',[r'\vec f_2',r'f_2'],'low','Detached nearly horizontal hooked stroke above the f has unsettled status.','13_lower_struck_tail.png'),
('lower-right three initials',r'Q\Phi S',['QDS','QPS','QFS'],'low','Connected central loops and cross-stroke do not fix the middle letter.','14_bottom_initials.png'),
('left box detached paired marks',"''",['two pen dots/ticks with no assigned punctuation function'],'low','Two small dark ovals with faint tails are visible, but their function is unclear.','15_box_detached_ticks.png')
]
report={
 'scan':4,'reader':'B','start_utc':'2026-11-20 09:33:59 UTC','end_utc':'2026-11-20 09:47:16 UTC',
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'differences':D,
 'doubts':[{'location':loc,'reading':reading,'alternatives':alts,'confidence':conf,'reason':reason,'crop':crop} for loc,reading,alts,conf,reason,crop in doubts],
 'inventory':inventory,
 'notes':{
  'page_content':'Two-column handwritten cancelled algebra calculation involving indexed e and f symbols, a descended Greek letter read primarily as eta, delta, lambda, alpha and beta; left boxed system and expansion, rotated note, right braced system and descending equality calculation.',
  'author_own_uncertainty_exact_words':[],
  'author_own_uncertainty_comment':'No verbal statement of authorial uncertainty is visible. C and this reader’s uncertainty markers are editorial.',
  'title_date_page_counts':'One scan, no title or date and no independently identifiable authorial page number; archive pencil 3 appears near the upper-left paper edge. H page 3 corresponds to scan 4 under the brief.',
  'mathematics_led_reading_decisions':[
   'The repeated i+1 notation prompted inspection of the lower second-case subscript; the crop preserves i-1|i+1 rather than forcing the neighboring pattern.',
   'The coefficient (1-alpha) was inspected because its joined 1/minus outline initially resembled a plus; the crop shows a horizontal minus attached to the end of the 1. It agrees with both witnesses.',
   'The repeated first-factor i indices prompted inspection of the expansion: f_i is visually secure; e_i remains qualified by the 1 alternative.',
   'The detached stroke above f_2 in the cancelled tail is kept despite the surrounding expansion using plain f symbols. No mathematical repair or proof check was performed.'
  ],
  'collation_scope':'All twelve C doubt loci have explicit report rows. H editorial notes and orientation captions Encadré/pour and À droite/pour are treated as apparatus, while printed punctuation immediately attached to formula readings is collated. H explicitly acknowledges the descending arrangement in a note, so its linear typesetting alone is not reported as an omission.',
  'diff_flag_usage':'diff_C is true for changed C readings or newly introduced/removed doubt qualifications; a retained C doubt has diff_C=false. Rewrapping the same alternatives or substituting uline for math underline is not counted as a change. H=null is never used because H has full text for this page.',
  'visual_method':'Whole image viewed once; half a viewed once; half b viewed once. Sixteen local crops made once each and viewed once each, with PIL LANCZOS enlargement and autocontrast; rotated note crop is turned 180 degrees. No OCR, other pages, other readers, external sources, or proof validation used.',
  'unchanged_ink_checks':'The full initial pair, every term of the left boxed system, eta=e_(d-1) and delta pair, e2/e3 equations, rotated note, right top range and all four relations, lower range, three vertical equals, beta/alpha conclusions, and both foot equations were read against the halves. Signs, index strokes, punctuation, and local cancellation boundaries were checked visually.'
 },
 'notation':[
  {'location':'first Greek letter left top; recurring both columns','sign':'eta/gamma-like descended letter','latex':r'\unsure{\eta|\gamma}', 'evidence':'Short entry stem, hump, long descending right leg; first occurrence qualified.'},
  {'location':'throughout indexed products','sign':'e, f, i, j, 1','latex':r'e_i, f_i, e_1, f_1, e_j','evidence':'e has low open loop; f has tall loop and descender; i ordinarily dotted, j has long hooked tail, 1 is a short undotted stroke.'},
  {'location':'left top and page foot','sign':'delta','latex':r'\delta','evidence':'Tall open upper turn and lower loop with descending stroke.'},
  {'location':'left expansion','sign':'lambda','latex':r'\lambda','evidence':'Long slant joins a short right leg; raised 2 is separately written in the second line.'},
  {'location':'right systems','sign':'alpha, beta','latex':r'\alpha,\beta','evidence':'Alpha has a small loop and extended leg; beta is tall with two curved portions.'},
  {'location':'right lower descending chain','sign':'vertical equals','latex':r'\rotatebox{90}{$=$}','evidence':'Three pairs of approximately vertical short strokes appear between successive horizontal lines.'},
  {'location':'below left box','sign':'deg','latex':r'\deg','evidence':'d-e-g with long lower g, no written expansion to degré.'},
  {'location':'right lower brace first parity label','sign':'imp','latex':r'\text{imp}','evidence':'The visible label ends at p, unlike the longer impair labels elsewhere.'},
  {'location':'right upper second case coefficient','sign':'one minus alpha','latex':r'(1-\alpha)','evidence':'Horizontal minus joins the terminal stroke of the 1; no independent plus vertical is seen in crop 09.'},
  {'location':'right cancelled expansion final factor','sign':'uncertain detached mark above f2','latex':r'\unsure{\bar f_2|\vec f_2|f_2}','evidence':'Short isolated upper stroke with hooked right tip in crop 13.'}
 ],
 'check_events':[],
 'crops':json.loads((base/'crop_manifest.json').read_text()),
 'brief_feedback':[
  'The brief has no dedicated convention for two detached pen ticks whose punctuation function is uncertain. They are preserved as unsure paired quote ticks, with an exact crop and position.',
  'The brief has no dedicated notation for a detached upper stroke that may belong to a handwritten f. The proposed math marks bar, arrow, and plain-f alternatives explicitly.',
  'H presents condensed formulas with editorial linking punctuation outside note macros. Those local commas and semicolons are reported separately; explicit orientation captions and notes are treated as apparatus.',
  'The page-wide cancellation is represented by nested deleted macros, as directed, rather than recreating page geometry; the two lower box rules and the beta oval receive explicit inventory entries.'
 ]
}
for row in report['differences']:
 if row['id']=='B004.35': row['reading']="\\unsure{\\text{''}}"
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote report with',len(D),'collation rows,',len(inventory),'inventory items,',len(doubts),'unresolved loci.')
