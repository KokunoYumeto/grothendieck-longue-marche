from pathlib import Path
import json

OUT=Path('/workspace/scratch/94548b74fbe0/out/readers/014/A')
spots=[
 dict(id='G01',origin=[1538,52],extent=[8,8],bbox=[1540,54,1544,58],position='above and to the right of the insertion',crop='01_first_line.png',fill='black!75',shape='small oblique filled patch',path=r'\fill[black!75] (2,2) .. controls (4,2) and (6,3) .. (5,5) .. controls (4,6) and (2,5) .. (2,2) -- cycle;',confidence='medium'),
 dict(id='G02',origin=[1311,162],extent=[9,10],bbox=[1313,164,1318,169],position='below the n of n-aires',crop='01_first_line.png',fill='black!45',shape='pale short oblique spot',path=r'\fill[black!45] (3,3) .. controls (5,2) and (7,3) .. (6,5) .. controls (5,7) and (3,7) .. (2,6) .. controls (2,5) and (3,4) .. (3,3) -- cycle;',confidence='medium'),
 dict(id='G03',origin=[940,221],extent=[9,9],bbox=[943,224,947,228],position="immediately to the left of d'",crop='02_second_line.png',fill='black!50',shape='small detached dark spot',path=r'\fill[black!50] (3,3) .. controls (5,2) and (7,4) .. (6,6) .. controls (5,7) and (3,6) .. (3,3) -- cycle;',confidence='medium'),
 dict(id='G04',origin=[983,213],extent=[8,8],bbox=[985,215,989,218],position="small pale point just right of the d stem in d'",crop='02_second_line.png',fill='black!25',shape='pale small oval spot',path=r'\fill[black!25] (2,3) .. controls (2,1) and (5,1) .. (6,3) .. controls (6,5) and (3,5) .. (2,3) -- cycle;',confidence='low'),
 dict(id='G05',origin=[1425,727],extent=[8,8],bbox=[1427,728,1430,733],position='upper blank field, right of centre',crop='03_mid_right_trace.png',fill='black!85',shape='small nearly upright dark oval',path=r'\fill[black!85] (2,2) .. controls (3,0) and (5,1) .. (5,3) .. controls (5,6) and (2,6) .. (2,2) -- cycle;',confidence='medium'),
 dict(id='G06',origin=[1073,912],extent=[9,8],bbox=[1075,913,1079,917],position='blank field beneath the title',crop='04_mid_trace.png',fill='black!80',shape='small right-rising dark oval',path=r'\fill[black!80] (2,3) .. controls (3,1) and (6,0) .. (6,3) .. controls (5,5) and (2,6) .. (2,3) -- cycle;',confidence='medium'),
 dict(id='G07',origin=[240,1384],extent=[10,8],bbox=[241,1386,247,1390],position='left field below the page midpoint',crop='05_lower_left_trace.png',fill='black!80',shape='short horizontal dark oval or dash',path=r'\fill[black!80] (1,4) .. controls (2,2) and (6,1) .. (7,3) .. controls (8,5) and (3,6) .. (1,4) -- cycle;',confidence='medium'),
 dict(id='G08',origin=[1568,1791],extent=[15,17],bbox=[1570,1793,1580,1805],position='lower-right field, separated diagonal pair',crop='06_lower_right_pair.png',fill='black!90',shape='two separated dark spots, upper spot slightly angular and lower spot rounder',path=r'\fill[black!90] (7,2) .. controls (10,1) and (12,3) .. (11,5) .. controls (11,7) and (8,8) .. (7,7) -- (8,4) -- cycle;'+'\n'+r'\fill[black!90] (2,10) .. controls (3,8) and (6,9) .. (6,12) .. controls (6,15) and (2,15) .. (2,10) -- cycle;',confidence='medium'),
 dict(id='G09',origin=[231,1889],extent=[8,10],bbox=[233,1890,236,1896],position='faint mark in the lower-left field',crop='07_lower_left_faint.png',fill='black!25',shape='pale upright oval trace',path=r'\fill[black!25] (2,3) .. controls (2,1) and (4,0) .. (5,3) .. controls (5,7) and (2,8) .. (2,3) -- cycle;',confidence='low'),
 dict(id='G10',origin=[1705,2276],extent=[10,8],bbox=[1707,2278,1712,2281],position='near the lower-right edge',crop='08_bottom_right_trace.png',fill='black!50',shape='tiny horizontal oval trace',path=r'\fill[black!50] (2,3) .. controls (3,1) and (6,2) .. (7,3) .. controls (7,5) and (2,5) .. (2,3) -- cycle;',confidence='medium'),
 dict(id='G11',origin=[735,2423],extent=[11,13],bbox=[736,2425,742,2433],position='near the foot, left of the page centre',crop='09_bottom_middle_trace.png',fill='black!35',shape='pale oblique spot with a short lower-right taper',path=r'\fill[black!35] (2,2) .. controls (4,1) and (5,4) .. (5,6) -- (7,10) .. controls (5,9) and (3,7) .. (2,6) .. controls (0,4) and (1,2) .. (2,2) -- cycle;',confidence='low'),
]
guide=r'\draw[black!70,line width=0.3pt,line cap=round] (1279,162) .. controls (1268,146) and (1273,128) .. (1292,119) .. controls (1325,103) and (1371,100) .. (1421,101) .. controls (1452,102) and (1483,104) .. (1493,98) .. controls (1499,94) and (1497,85) .. (1495,81);'
tex=[r'\scanpage{14}',r'% Reader A: complete proposed page; source origin is full-scan top left.',r'% Coordinate map: X = 0.006 cm * x; Y = -0.006 cm * y.',r'% The text remains one title; its two physical lines are placed as nodes.',r'% Every small trace is qualified locally; hand, intention and surface origin are unresolved.',r'\figure{\begin{tikzpicture}[x=0.006cm,y=-0.006cm]',r'\path[use as bounding box] (0,0) rectangle (1760,2470);',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{9}{10}\selectfont] (A014T1) at (880,157) {\unsure{décompositions}};',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{9}{10}\selectfont] (A014I1) at (1163,82) {\inserted{et découpages}};',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{9}{10}\selectfont] (A014T2) at (1305,150) {$n$-aires};',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{9}{10}\selectfont] (A014T3) at (961,237) {d\textquotesingle\unsure{espaces} topologiques};',r'% GUIDE01: continuous lead-in; unchanged insertion attachment, explicit observed curve.',guide]
# Use the literal apostrophe, avoiding a macro outside the supplied preamble.
tex[-3]=tex[-3].replace(r'\textquotesingle',"'")
for s in spots:
    x,y=s['origin']; w,h=s['extent']
    tex += [f"% {s['id']}: {s['position']}; {s['shape']}; source box {s['bbox']}.",rf'\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{{5}}{{5}}\selectfont] at ({x},{y}) {{\unsure{{\begin{{tikzpicture}}[x=0.006cm,y=-0.006cm,baseline={{(0,0)}}]',rf'\path[use as bounding box] (0,0) rectangle ({w},{h});',s['path'],r'\end{tikzpicture}}};']
tex += [r'\end{tikzpicture}}',r'% archive sheet number: 13',r'% Archive comment corresponds to the lower-left numeral at full-scan box (80,2411,125,2447).','']
(OUT/'reading.tex').write_text('\n'.join(tex),encoding='utf-8')

crops=[
 ('01_first_line.png',[860,30,1560,192],'first main word, insertion, n-aires and nearby detached marks'),
 ('02_second_line.png',[930,182,1570,306],"d'espaces, topologiques, endpoint and nearby detached marks"),
 ('03_mid_right_trace.png',[1400,700,1455,760],'isolated dark trace in upper blank field'),
 ('04_mid_trace.png',[1045,885,1110,945],'isolated dark trace below title'),
 ('05_lower_left_trace.png',[210,1355,275,1420],'isolated short dark trace in lower-left field'),
 ('06_lower_right_pair.png',[1535,1760,1610,1835],'two separated dark spots in lower-right field'),
 ('07_lower_left_faint.png',[205,1865,265,1925],'faint isolated upright mark in lower-left field'),
 ('08_bottom_right_trace.png',[1675,2250,1730,2308],'isolated mark near lower-right edge'),
 ('09_bottom_middle_trace.png',[710,2395,770,2445],'isolated faint mark near foot'),
]
diffs=[
 dict(id='A014-D01',location='first main word',C=r'\unsure{décompositions}',H=None,reading=r'\unsure{décompositions}',evidence='Initial looped d, raised curved accent, c/o run, long descending p and tall later stroke are visible. The nearly level central run and crowded ending remain insufficiently separated to remove the source doubt.',confidence='medium',kind='other',diff_C=False,diff_H=False,C_doubt_status='retained',readers_crop='01_first_line.png',bbox={'source':'full','coordinates':[879,93,1269,188]},C_source_row='C_doubts.txt / Doubtful readings / first main word'),
 dict(id='A014-D02',location="word after d'",C=r'\unsure{espaces}',H=None,reading=r'\unsure{espaces}',evidence='Short initial hook/wave, deep p descender, small open curve and compressed finishing waves support espaces as the primary reading; the internal joins remain crowded after the one enlargement.',confidence='medium',kind='other',diff_C=False,diff_H=False,C_doubt_status='retained',readers_crop='02_second_line.png',bbox={'source':'full','coordinates':[1004,210,1166,276]},C_source_row="C_doubts.txt / Doubtful readings / after d'"),
 dict(id='A014-D03',location='insertion lead-in beneath et découpages',C=r'\inserted{et découpages}',H=None,reading='The same insertion is retained; GUIDE01 reproduces its continuous left downward bend, long rightward run and upturned right endpoint.',evidence='A continuous grey/dark guide descends at the gap before n and runs beneath the inserted words to a hooked right endpoint. This is a graphic-detail addition; the textual insertion and its attachment agree with C.',confidence='high',kind='drawing or diagram',diff_C=True,diff_H=False,C_doubt_status=None,readers_crop='01_first_line.png',bbox={'source':'full','coordinates':[1270,79,1500,164]},component_ids=['GUIDE01']),
]
for i,s in enumerate(spots,4):
 diffs.append(dict(id=f'A014-D{i:02d}',location=s['position'],C='not represented',H=None,reading=s['shape']+'; locally qualified graphic only',evidence='The crop shows '+s['shape']+'. No character, connection, purpose or hand is assigned. Surface origin remains unresolved.',confidence=s['confidence'],kind='drawing or diagram',diff_C=True,diff_H=False,C_doubt_status=None,readers_crop=s['crop'],bbox={'source':'full','coordinates':s['bbox']},component_ids=[s['id']]))

def inv(element,kind,position,words,hand='his hand',**extra):
 return dict(sheet_kind='cover',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=words,transcribed='yes',**extra)
items=[
 (44,inv('014.02','insertion','above the main first line','et découpages',provenance='C inventory 014.02; text node A014I1')),
 (79,inv('014.A.GUIDE01','drawing','beneath the insertion, descending before n','continuous bent insertion lead-in',components=['GUIDE01'],provenance='C records insertion semantics and describes its lead-in; explicit path supplied here')),
 (93,inv('014.01a','text','main first line at upper right','doubtful décompositions; n-aires',provenance='first part of C inventory 014.01; nodes A014T1 and A014T2')),
 (188,inv('014.01b','text','second title line at upper right',"d'espaces topologiques; espaces remains doubtful",provenance='second part of C inventory 014.01; node A014T3')),
 (2411,inv('014.A.archive','text','lower left','archive sheet number 13 (comment only)','another unnamed hand',provenance='present in C.tex archive comment; omitted from C inventory')),
]
for s in spots:
 items.append((s['bbox'][1],inv('014.A.'+s['id'],'drawing',s['position'],s['shape']+'; qualified; role and surface origin unresolved','undetermined hand',components=[s['id']],provenance='new reader-A graphical proposal')))
inventory=[v for _,v in sorted(items,key=lambda p:p[0])]
mapdata=[dict(id='GUIDE01',source_file='reading.tex',source_command=guide,full_scan_bbox=[1270,79,1500,164],map='direct full-scan coordinates; x=0.006cm, y=-0.006cm',path_command_count=1,visible_component_count=1)]
for s in spots:
 mapdata.append(dict(id=s['id'],source_file='reading.tex',source_command=s['path'],full_scan_bbox=s['bbox'],fixed_origin=s['origin'],local_bounding_box=[0,0]+s['extent'],map=f"full_scan(x,y)=({s['origin'][0]}+u,{s['origin'][1]}+v); both pictures use x=0.006cm,y=-0.006cm; base-west node and local baseline (0,0)",path_command_count=s['path'].count('\\fill'),visible_component_count=2 if s['id']=='G08' else 1,qualification='local unsure wrapper',shape_confidence=s['confidence'],interpretation='hand, intention and surface origin unresolved'))
report=dict(scan=14,reader='A',start_utc='2026-11-20 14:55:15 UTC',end_utc='2026-11-20 15:05:18 UTC',full_image_viewed=True,halves_viewed=True,complete_visual_read=True,differences=diffs,doubts=[
 dict(location='first main word',reading='décompositions',alternatives=[],confidence='medium',reason='compressed internal strokes; original C doubt retained',crop='01_first_line.png'),
 dict(location="after d'",reading='espaces',alternatives=[],confidence='medium',reason='crowded internal joins; original C doubt retained',crop='02_second_line.png'),
]+[dict(location=s['position'],reading=s['shape'],alternatives=[],confidence=s['confidence'],reason='visible shape retained, with unresolved hand, role and surface origin; no character supplied',crop=s['crop']) for s in spots],inventory=inventory,notes=dict(
 page_content="A cover title: décompositions, with et découpages inserted before n-aires, followed by d'espaces topologiques. The remainder is mostly blank; an archive 13 is at lower left.",
 author_uncertainty='No explicit authorial uncertainty wording occurs. All unsure markers in this return are editorial.',
 title_date_page_counts='No date, authorial page numeral or page count is visible. Archive numeral 13 is retained only as the required comment.',
 mathematics_led_decisions='None. No mathematical repair, theorem, correspondence or proof check was used.',
 source_doubt_map={'first main word':'A014-D01, retained','after d\u0027':'A014-D02, retained'},
 witness_status='H.tex supplies no text (metadata hua_has=nothing); every H field is null and every diff_H is false.',
 source_paths='C.tex contains no TikZ source paths. Its title words, insertion state and archive comment have all been checked against the images and retained. New graphic commands are listed in the final component map.',
 final_source_component_map=mapdata,
 text_node_map={'A014T1':'décompositions, original doubt retained','A014I1':'et découpages, inserted at the gap before n','A014T2':'n-aires','A014T3':"d'espaces topologiques, original espaces doubt retained"},
 workflow='The first clock value was recorded after the initial packet-read command, before any image was opened. The initial combined output truncated the middle of the brief; lines 110 onward were read separately to complete it. Whole image was viewed once, then half a once and half b once. Each of the nine crops was viewed once. No compiler, renderer, OCR, external source, installation or other page/reader was used.',
 image_coordinates='Full scan 1760x2470; both supplied halves 1760x1315. Half a has origin (0,0); half b has origin (0,1155), from 2470-1315.',
 crop_limits='Crop 01 includes small pieces of the second-line ascenders at its bottom border; crop 02 includes the tail of the first-line p at its top border. These belong to the already transcribed adjacent words. All target textual loci and isolated traces are within their crop bounds.',
 texture='Diffuse pink/grey show-through and paper texture were inspected on the whole and halves. They provide no supported character candidate. The eleven specifically isolated trace clusters are the qualified graphical proposals listed above.',
 graphic_geometry='One fixed full-page coordinate picture holds the title nodes, explicit insertion guide and qualified traces. Twelve filled trace components occur in eleven clusters; G08 contains two fill commands and two visible components. The guide is one further path. All invisible bounding rectangles are layout commands, not manuscript marks. Grayscale and contours are approximate; coordinates identify the observed loci.'
),notation=[
 dict(location='first title line',sign='n followed by a short hyphen',latex='$n$-aires',evidence='single rounded hump followed by separate horizontal dash'),
 dict(location='above first line and gap before n',sign='inserted et découpages with curved lead-in',latex=r'\inserted{et découpages}',evidence='separate upper wording and continuous guide into the first-line gap'),
 dict(location='second title line',sign='apostrophe after d',latex="d'",evidence='separate short descending upper stroke to the right of d'),
 dict(location='title endpoint',sign='no terminal punctuation represented',latex='topologiques',evidence='the s ends in a short terminal stroke; no separate following full stop is visible'),
],check_events=[],crops=[dict(path=n,bbox={'source':'full','coordinates':b},rotation=0,purpose=p,processing='PIL autocontrast and LANCZOS enlargement; 2800 px for the two title crops, 2000 px for isolated traces',viewed=True) for n,b,p in crops],brief_feedback=['The mandatory preservation of detached marks also reaches small isolated spots with unresolved surface origin. Their shape is retained graphically, and the report keeps this qualification separate from the title reading.'])
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

md='''# Scan 014 — reader A

## Visual reading audit

- **Layout:** whole image viewed once. Cover with a small title in the upper right, one inserted phrase above it, broad blank field, and archive **13** at lower left.
- **Upper insertion:** `et découpages` is readable. The long guide bends down at the gap before `n`; it has a hooked right endpoint. The words and attachment agree with C. Proposed path **GUIDE01** makes the observed guide explicit; crop **01**, full-scan box **1270,79,1500,164**.
- **Main line:** `\\unsure{décompositions}` retained. The initial looped d, accent, c/o, descending p and tall later stroke are visible, but the central near-level run and ending remain compressed. This retains original C doubtful-readings row **first main word**; crop **01**, locus **879,93,1269,188**.
- **Main-line ending:** `$n$-aires` read directly; the n and short lexical hyphen are visible. No word or symbol change proposed.
- **Second line:** `d'\\unsure{espaces} topologiques`. Apostrophe and topologiques are readable. The spaces candidate keeps its original doubt because the internal joins stay crowded. Original C row **after d'** maps to crop **02**, locus **1004,210,1166,276**. The title ends without a separate visible full stop.
- **Title-adjacent traces:** four local qualified shapes **G01–G04** are newly represented: upper-right spot, spot below n, spot left of d', and pale point beside the d stem. Crops **01–02**. No character, purpose, hand or surface origin is supplied.
- **Blank fields:** the eleven total isolated clusters below are retained only as locally qualified graphics. Diffuse coloured/grey show-through supplies no supported word or glyph. No additional text, deletion, marginal note, display or diagram was recovered.
- **Foot:** archive `13` was read on half b, full-scan **80,2411,125,2447**. It remains a comment and is now included in the inventory. No authorial date or page count is visible.

## Detached-component map

All coordinates are full-scan pixels. `reading.tex` has a fixed top-left origin and map **X = 0.006 cm × x**, **Y = −0.006 cm × y**. Each trace's local origin is fixed by a base-west node, baseline `(0,0)` and an invisible local bounding rectangle. The exact fill commands and local extents are in `report.json → notes → final_source_component_map`. Each trace carries a local `\\unsure` qualification; its unknown origin is not converted into punctuation.

| Component | Source origin | Locus box | Crop | Shape |
|---|---|---|---|---|
'''
for s in spots:
 md+='| '+s['id']+' | '+','.join(map(str,s['origin']))+' | '+','.join(map(str,s['bbox']))+' | '+s['crop']+' | '+s['shape']+' |\n'
md+='''
There are **12 filled components in 11 trace clusters**. G08 has two fill commands and two disconnected visible spots. GUIDE01 is one additional drawn path. C contains no pre-existing path commands. Its complete text, insertion state and archive comment are retained in the four title nodes and archive comment; no text occurs twice.

## Qualification and verification

Both original C doubts remain; no new alternative word is supplied. H has `nothing`, so H collation fields remain null/false. No mathematical check was performed (`check_events: []`). Source/report checks are structural only; no compiler or renderer was invoked.

The first recorded UTC value, **2026-11-20 14:55:15 UTC**, follows the initial packet-read command and precedes image viewing. The initial combined read truncated part of the brief; the remaining portion was then read separately. The full image, half a, half b and each of nine crops were each displayed once. Crop 01's bottom edge and crop 02's top edge include partial adjacent-line strokes; their target loci are complete. No recrop was made.
'''
(OUT/'reading.md').write_text(md,encoding='utf-8')
print('Wrote reading.tex, report.json and reading.md.')
