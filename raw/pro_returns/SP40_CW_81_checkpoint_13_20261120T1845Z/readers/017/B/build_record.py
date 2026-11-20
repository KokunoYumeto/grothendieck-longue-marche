from pathlib import Path
import json

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/readers/017/B'
manifest = json.loads((OUT / 'crop_manifest.json').read_text(encoding='utf-8'))
crop_by_name = {r['path']: r for r in manifest['crops']}
differences = []

def add(id, location, C, H, reading, evidence, confidence, kind, diff_C, diff_H,
        C_doubt_status=None, crop=None, bbox=None, row=None, **extra):
    if bbox is None and crop:
        bbox = crop_by_name[crop]['bbox']
    d = dict(id=id, location=location, C=C, H=H, reading=reading,
             evidence=evidence, confidence=confidence, kind=kind,
             diff_C=diff_C, diff_H=diff_H, C_doubt_status=C_doubt_status,
             readers_crop=crop, bbox={'system':'full scan, upper-left origin','coordinates':bbox})
    if row is not None:
        d['C_source_row'] = row
    d.update(extra)
    differences.append(d)

add('D01a','Opening cancelled subject',r'\unsure{E_i|\Sigma_i}',r'E_i',r'\unsure{E_i|\Sigma_i}',
    'Three heavy horizontal remnants and a left upright favour E; diagonals, a lower loop, and the index overlap the cancellation. The complete cancelled glyph is not settled. H shares the first candidate.',
    'low','other',False,False,'retained','crop01_top_correction.png',row=1,local_part='subject')
add('D01b','Opening cancelled short verb',r'\unsure{est}','soit',r'\unsure{est|soit}',
    'An elongated low loop, a short rounded middle, and a taller final upright favour est. The cancellation prevents a secure division of the intervening strokes; soit remains an explicit alternative. C uncertainty is retained, with its unspecified alternative made concrete.',
    'low','misread word',False,True,'retained','crop01_top_correction.png',row=1,local_part='verb',qualification='H differs in primary candidate only; its reading is retained as an alternative.')
add('D01c','Opening cancelled adjective',r'\unsure{rare|dense}','rare',r'\unsure{rare|dense}',
    'The low r-like rises and terminal loop favour rare, but the central word is crossed and the high stroke can belong to the preceding word. The enlargement does not settle rare/dense.',
    'low','other',False,False,'retained','crop01_top_correction.png',row=1,local_part='adjective')
add('D02','Cancelled sentence above the equalities',r'\unsure{trouve}','trouve',r'\unsure{trouve}',
    'The tall opening t, several shallow lower returns, and the final low strokes survive the long cancellation. The intervening letter divisions remain uncertain. The target word and final que descender are present in the crop; the initial A of context is clipped at the top.',
    'medium','other',False,False,'retained','crop02_trouve.png',row=2)
add('D03','First join of the Sigma_12 equality',r'\unsure{\cup|\amalg}',r'\cup',r'\cup, reproduced as two curved passes (G01)',
    'The enlarged sign has one left upright, two closely spaced right returns, and curved lower bowls. The literal two paths are retained. The square-join candidate is removed on the inspected strokes.',
    'high','drawing or diagram',True,True,'resolved','crop04_join.png',row=3,graphic='G01',counting='One physical join cluster per witness; C doubt resolution and the two-path geometry are recorded together.')
add('D04a','Slanted margin, partition name',r'\unsure{\Pi|\pi}_j',r'\Pi_j',r'\Pi_j',
    'The upright rotated view shows the joined horizontal head and two substantial descending legs. The capital form is selected; the long subscript j is separate.',
    'medium','other',True,False,'resolved','crop05_margin.png',row=4,local_part='partition letter')
add('D04b','Slanted margin, predecessor under E_j',r'\deleted{\unsure{\Sigma}}E_j',r'E_j',r'\deleted{\unsure{\Sigma}}E_j',
    'An angular dark under-form and a crossing stroke remain within the first E. Sigma is a supported candidate but its original outline is partly hidden. H omits the local predecessor.',
    'low','omission',False,True,'retained','crop05_margin.png',row=4,local_part='cancelled predecessor')
add('D05','Cancelled wording after de X',r'\deleted{\unsure{des parties|définie}}',r'\struck{définie}',r'\deleted{definie}',
    'One continuous word shows the looped d, low e, long f descender, two i positions and the ending. The surviving strokes support definie. No detached acute is visible over its e; the two-word first C candidate is removed.',
    'high','misread word',True,True,'resolved','crop06_cancelled_definie.png',row=5,qualification='The H difference here is the written accent; its lexical reading matches.')
add('D06a','Overwritten beginning of intersection',r'\deleted{\unsure{et}}',r'\struck{intersection}\add{intersection}',r'\deleted{\unsure{et}} intersection',
    'A short low e-like opening and crossed upright occur before the longer live word. The compact predecessor remains uncertain. Only one complete longer word is visible in this cluster; no separate raised replacement word is supplied.',
    'low','deletion state (struck given live or live given struck)',False,True,'retained','crop08_intersection.png',row=6,local_part='short predecessor',counting='H cancellation/insertion reading is counted once for this physical cluster; D06b is the independent C word doubt.')
add('D06b','Live longer word intersection',r'\unsure{intersection}',r'\add{intersection}','intersection',
    'The extended word has the surviving internal rises and the final crossed t, dot and low terminal run. The live lexical reading intersection is selected. Its state comparison with H is included in D06a.',
    'medium','other',True,False,'resolved','crop08_intersection.png',row=6,local_part='live longer word',parent_difference='D06a')
add('D07a','Predecessor beneath E_j after par les',r'\deleted{\Sigma}E_j (source doubt table qualifies Sigma)',r'E_j',r'\deleted{\Sigma}E_j',
    'The top and bottom horizontal segments with the surviving diagonal give Sigma beneath the heavy E strokes. The crossing is retained. This is a source-table doubt even though C.tex prints no unsure macro at this occurrence.',
    'medium','omission',True,True,'resolved','crop07_corrected_E.png',row=7,local_part='first corrected E_j')
add('D07b','Isolated slashed form after later E_j',r'\deleted{\unsure{E|\in}}',r'\ill{}',r'\unsure{\deleted{\in}|\deleted{E}|\notin}',
    'Two curved lower arms and an oblique upper crossing favour a membership-form candidate over E. The strokes do not settle a cancelled predecessor versus an integral slashed-membership sign. All complete selected states are explicit.',
    'low',r'readable ink left as \ill{}',True,True,'retained','crop10_isolated_sign.png',row=7,local_part='later isolated form',qualification='C E remains an alternative; the cancellation interpretation itself is newly qualified.',counting='One H ill placeholder and one C physical glyph/state cluster.')
add('D08a','Raised partition name over lower de',r'\Pi_J^{\unsure{\circ|0}}',r'\Pi_J^0',r'\Pi_J^{\unsure{\circ|0}}',
    'The small upper rounded, partly angular loop is visibly raised. Its strokes do not decide circle versus numeral zero. H zero remains the second candidate.',
    'medium','misread symbol or index',False,True,'retained','crop12_inserted_Pi.png',row=8,local_part='first upper ring',qualification='Qualified primary-candidate difference from H.')
add('D08b','Binary partition name, repeated upper ring',r'\Pi_{J,j}^{\circ} (source table qualifies this ring too)',r'\Pi_{J,j}^0',r'\Pi_{J,j}^{\circ}, carrying the page-first circle/zero qualification',
    'A separate tiny raised loop occurs beside this Pi. Circle/zero remains unresolved locally. The final TeX follows the recurring-symbol convention: the first occurrence carries unsure and this occurrence uses the same first candidate.',
    'medium','misread symbol or index',False,True,'retained','crop14_binary_Pi.png',row=8,local_part='binary-name upper ring',qualification='Qualified primary-candidate difference from H; source-row scope explicitly retained.')
add('D09','Last parenthesis, quantified letter',r'\unsure{g|j}',r'j',r'\unsure{g|j}',
    'The compact loop above the long downstroke favours g, while the extended leftward foot also supports j. The crop retains the complete foot; both readings remain.',
    'low','misread symbol or index',False,True,'retained','crop16_final_words.png',row=9,qualification='H j is retained as an alternative, not rejected conclusively.')
add('D10','Last word at right edge',r'\unsure{Pour|Puis}',r'\uncertain{Pour}','Pour',
    'The capital P is followed by a compressed low o, a broad u and terminal r-like return. There is no separate high i dot at the relevant later position. The decision uses this crop only, without the following sheet.',
    'medium','other',True,False,'resolved','crop16_final_words.png',row=10)
add('D11','First complement after inserted Pi_J ring',r'\unsure{\overline{\bigcup}|\bigcup}',r'\bigcup',r'\overline{\bigcup}, reproduced by the literal cup and transverse stroke G08',
    'A separate transverse run starts just left of the left stem, crosses it near the top and stops short of the right stem. Its presence is clear. G08 preserves this attachment and span without assigning an additional mathematical interpretation.',
    'high','misread symbol or index',True,True,'resolved','crop13_middle_union.png',row=11,graphic='G08',counting='One physical union/stroke cluster per witness, including the literal geometry.')
add('D12','Inserted U subscript above sur',r'U_{\deleted{\unsure{J|j}}J}',r'U_J',r'U_{\unsure{\deleted{J}J|\deleted{j}J|J}}',
    'Two displaced lower returns share a crowded upright; the final upper horizontal favours capital J. The predecessor can be J or j, and the two returns do not establish cancellation/replacement rather than retracing. The plain final-J state is therefore retained as an explicit alternative.',
    'low','deletion state (struck given live or live given struck)',True,True,'retained','crop15_U_subscript.png',row=12,qualification='Glyph and state uncertainty are separate. H matches the plain-J alternative. No writing chronology is inferred.')

add('H01','Opening parenthesis','si','où','si',
    'A looped s and narrow following i stand after the opening parenthesis, before the two signed Sigmas.',
    'high','misread word',False,True,crop='crop01_top_correction.png')
add('H02','End of opening cancellation','dans X.','dans X','dans X.',
    'A distinct dark baseline point follows the cancelled X.',
    'high','omission',False,True,crop='crop01_top_correction.png',bbox=[1530,235,1610,289])
add('H03','Raised on ait',r'\inserted{on ait}','on ait',r'\inserted{on ait}',
    'The words are above the crossed sentence and supply its live continuation before the parenthesis.',
    'high','insertion or placement',False,True,crop='crop01_top_correction.png',bbox=[1135,183,1340,235])
add('H04','First equality endpoint',r'E_i',r'E_i,',r'E_i',
    'The i dot and upright are present; the clear space after the first right-hand member has no comma. The point on the lower row remains the second equality endpoint.',
    'high','text not on the page',False,True,crop='crop03_equation_endpoints.png',bbox=[935,416,1070,499])
add('H05','Prose introducing Sigma_12 equality',"Alors je dis qu'on a",'Alors je dis que',"Alors je dis qu'on a",
    'Half a shows the long q descender, apostrophe, low on and final small a after dis. This locus was settled on half a and was not cropped.',
    'high','misread word',False,True,bbox=[300,621,1004,774],image_evidence='supplied half a; same coordinates as full scan')
add('N01','Divider below third equality',r'\rule{2.4cm}{0.3pt}','[absent]',r'G02 shallow curved rule with hooked right endpoint',
    'Half a shows a gently rising left run, long shallow middle and a short downward right ending. The literal one-path separator replaces the straight rule.',
    'high','drawing or diagram',True,True,bbox=[300,888,542,913],graphic='G02',image_evidence='supplied half a; no crop because settled there')
add('H06','Slanted note opening','introduire','introduisons','introduire',
    'The upright rotated view ends in a short i-like upright and low re return. The selected ending is introduire.',
    'medium','misread word',False,True,crop='crop05_margin.png')
add('N02','Short dark shape to right of slanted-note brace','[absent]',r'\ill{}',r'\unsure{G03 short wedge}',
    'The rotated crop contains a short isolated dark wedge to the right of the closing brace. Its character, writer, role and possible attachment to neighbouring main text remain unresolved. The shape is retained locally; no word is supplied.',
    'low',r'readable ink left as \ill{}',True,True,crop='crop05_margin.png',graphic='G03',counting='The one final margin ill placeholder is collated once. The shape is not claimed to be the full content intended by H.',qualification='Possible neighbouring-text attachment remains open; root can adjudicate from this same crop.')
add('N03','Considérons accent','Considérons','Considérons',r'Consid\unsure{e|é}rons',
    'The e-area has no secure detached acute; a faint short upper-right trace prevents complete resolution. The unaccented candidate is first, with the source accent retained explicitly.',
    'low','abbreviation expanded or spelling modernised',True,True,crop='crop17_considérons.png',qualification='Qualified accent reading, not a claim about editorial intent.')
add('N04','Live definie immediately after cancellation','définie','définie','definie',
    'The low e between looped d and the long f has no detached acute in the enlarged word. Both i positions and the final ending are present.',
    'medium','abbreviation expanded or spelling modernised',True,True,crop='crop06_cancelled_definie.png',bbox=[684,1264,877,1379])
add('N05','definies after (j in J)','définies','définies','definies',
    'The first e is a low join before the tall f, without an upper acute. The later two detached marks belong to the two i positions, and the low final run carries the plural ending.',
    'high','abbreviation expanded or spelling modernised',True,True,crop='crop18_definies.png')
add('N06','Lower partition definie','définie','définie','definie',
    'The e before f has no raised acute. The two later detached marks align with the i positions; they do not supply an accent over e.',
    'high','abbreviation expanded or spelling modernised',True,True,crop='crop19_lower_definie.png')
add('N07','Guide under first inserted Pi_J',r'\inserted{\Pi_J} without guide',r'\add{\Pi_J} without guide',r'unchanged Pi_J insertion plus G04',
    'Half a shows the curved stroke above de, turning upward toward its right endpoint. G04 keeps that observed run; the inserted wording is unchanged.',
    'medium','drawing or diagram',True,True,bbox=[1218,1105,1395,1235],graphic='G04',image_evidence='supplied half a; guide settled there')
add('N08','Guide for ternaires Pi_j',r'\inserted{ternaires \Pi_j} without guide',r'\add{ternaires \Pi_j} without guide',r'unchanged insertion plus G05',
    'A leftward upper run curves down to the low V point and rises in a long oblique right stroke. The full guide survives within the crop and is drawn once.',
    'high','drawing or diagram',True,True,crop='crop09_ternaires.png',graphic='G05')
add('N09','Detached point before first lower union','[absent]','[absent]',r'\unsure{G06 baseline point}',
    'The crop shows one discrete small dark quadrilateral left of the union at its lower level. It has no established role or hand; no operation is assigned.',
    'medium','drawing or diagram',True,True,crop='crop11_first_union.png',bbox=[732,1900,744,1910],graphic='G06',qualification='Shape presence is high confidence; interpretation and hand remain unresolved.')
add('N10','Guide for lower inserted Pi_J ring',r'\inserted{\Pi_J^{\unsure{\circ|0}}} without guide',r'\add{\Pi_J^0} without guide',r'unchanged qualified insertion plus G07',
    'A long curve rises from the partition/de gap, runs beneath the inserted symbol and ends with a short upward hook on the right. The ring decision is logged separately under D08a.',
    'high','drawing or diagram',True,True,crop='crop12_inserted_Pi.png',graphic='G07')
add('N11','Guide above induites',r'\inserted{(j\in J)} induites, no drawn guide',r'\add{(j\in J)} (induites',r'\inserted{(j\in J)} induites with G09',
    'The left curved portion continues into the long run above induites and its hooked right endpoint. It is preserved as one connected guide. H renders the left portion as a prose opening parenthesis.',
    'high','drawing or diagram',True,True,crop='crop14_binary_Pi.png',graphic='G09')
add('N12','Guide from inserted U expression into sur/X gap',r'\inserted{U_J=} without guide',r'U_J= without insertion or guide',r'qualified inserted U expression plus G10',
    'A thin run below the double subscript feet curves right and then descends deeply between sur and X. The endpoint is inside the crop. G10 preserves this one connected path; D12 records the independent glyph/state alternatives.',
    'high','drawing or diagram',True,True,crop='crop15_U_subscript.png',graphic='G10')
add('H07','End of final quantified parenthesis',r'(\unsure{g|j}\in J).',r'(j\in J)).',r'(\unsure{g|j}\in J).',
    'One closing parenthesis follows J, then one distinct point. No second closing parenthesis appears before Pour.',
    'high','text not on the page',False,True,crop='crop16_final_words.png',bbox=[1322,2218,1472,2310])

doubts = []
for id, alts, reason in [
    ('D01a',[r'\Sigma_i'],'Dense cancellation hides the full subject and index.'),
    ('D01b',['soit'],'The short word is crossed; letter divisions remain open.'),
    ('D01c',['dense'],'The central low run is crossed.'),
    ('D02',['unresolved internal letters'],'The long strike obscures the shallow middle letters.'),
    ('D04b',['unresolved predecessor'],'The angular under-form is partly covered by E.'),
    ('D06a',['unresolved short predecessor'],'Only a compact crossed opening survives clearly.'),
    ('D07b',[r'\deleted{E}',r'\notin'],'Glyph and cancellation role remain independently open.'),
    ('D08a',['0'],'The small raised ring does not settle circle/zero.'),
    ('D08b',['0'],'This second physical ring remains locally unresolved.'),
    ('D09',['j'],'The small loop and extended tail support both candidates.'),
    ('D12',[r'U_{\deleted{j}J}',r'U_J'],'Double feet do not establish predecessor case or replacement state.'),
    ('N02',['unassigned character or neighbouring-text attachment'],'Retained shape has unresolved attachment, role and hand.'),
    ('N03',['Considérons'],'The faint upper trace does not securely establish an acute.'),
    ('N09',['unassigned dot-like mark'],'Visible point has unresolved role and hand.'),
]:
    d = next(x for x in differences if x['id'] == id)
    doubts.append(dict(id=id,location=d['location'],reading=d['reading'],alternatives=alts,
                       confidence=d['confidence'],reason=reason,crop=d['readers_crop']))

inventory = json.loads((BASE / 'packets/017/C_inventory.json').read_text(encoding='utf-8'))
for item in inventory:
    item['hand'] = 'his hand'
    item['provenance'] = 'Original C inventory identity retained; locally checked against this page.'
updates = {
    '017.03':r'Cancelled unsure E_i/Sigma_i, est/soit, rare/dense, dans X.',
    '017.09':r'introduire la partition Pi_j, with qualified cancelled Sigma beneath E_j',
    '017.13':r'Consid[e/é]rons la partition; definie; intersection; definies',
    '017.15':'Cancelled definie, without a visible acute',
    '017.17':'Qualified short cancelled et before the one live intersection',
    '017.19':r'Qualified states: deleted membership, deleted E, or slashed membership',
    '017.21':r'-- c’est aussi la partition definie, through Pour',
    '017.22':r'Inserted Pi_J, upper circle/zero qualified at first occurrence',
    '017.25':r'J/j predecessor and cancellation/retracing alternatives within U subscript',
}
for item in inventory:
    if item['element'] in updates:
        item['first_words_or_objects'] = updates[item['element']]

graphics = [
    dict(id='G01',element='017.B26',position='Third equality, first join',objects='Two curved passes of one cup',bbox=[946,783,982,815],origin=[946,783],units='x=0.014cm, y=-0.014cm',paths=2,source='crop04_join.png',hand='his hand',kind='drawing'),
    dict(id='G02',element='017.B27',position='Separator below third equality',objects='Shallow line and downturned right endpoint',bbox=[300,888,542,913],origin=[300,888],units='x=0.012cm, y=-0.012cm',paths=1,source='supplied half a',hand='his hand',kind='drawing'),
    dict(id='G03',element='017.B28',position='Right of slanted-note closing brace in rotated crop',objects='Locally qualified short dark wedge',bbox=[20,936,323,1318],origin='local upright wedge coordinates; whole source locus retained',units='x=y=0.25mm',paths=1,source='crop05_margin.png',hand='undetermined hand',kind='drawing'),
    dict(id='G04',element='017.B29',position='First inserted Pi_J above de X',objects='Curved guide beneath Pi_J',bbox=[1218,1105,1395,1235],origin=[1218,1105],units='x=0.010cm, y=-0.010cm',paths=1,source='supplied half a',hand='his hand',kind='drawing'),
    dict(id='G05',element='017.B30',position='Raised ternaires Pi_j and gap before de X',objects='Long bent V-shaped guide',bbox=[947,1345,1246,1478],origin=[947,1345],units='x=0.009cm, y=-0.009cm',paths=1,source='crop09_ternaires.png',hand='his hand',kind='drawing'),
    dict(id='G06',element='017.B31',position='Baseline point before first lower union',objects='Qualified small dark quadrilateral',bbox=[732,1900,744,1910],origin=[734,1902],units='x=0.025cm, y=-0.025cm',paths=1,source='crop11_first_union.png',hand='undetermined hand',kind='drawing'),
    dict(id='G07',element='017.B32',position='Raised lower Pi_J ring before de',objects='Long bent insertion guide with right hook',bbox=[752,1973,920,2083],origin=[752,1973],units='x=0.010cm, y=-0.010cm',paths=1,source='crop12_inserted_Pi.png',hand='his hand',kind='drawing'),
    dict(id='G08',element='017.B33',position='Middle lower union',objects='Cup outline and transverse upper run',bbox=[1118,1976,1187,2046],origin=[1118,1976],units='x=0.009cm, y=-0.009cm',paths=2,source='crop13_middle_union.png',hand='his hand',kind='drawing'),
    dict(id='G09',element='017.B34',position='Inserted (j in J) above induites',objects='Connected arched guide with right hook',bbox=[1234,2070,1470,2180],origin=[1234,2070],units='x=0.009cm, y=-0.009cm',paths=1,source='crop14_binary_Pi.png',hand='his hand',kind='drawing'),
    dict(id='G10',element='017.B35',position='From inserted U expression into sur/X gap',objects='Long descending curved guide',bbox=[311,2140,462,2305],origin=[311,2140],units='x=0.010cm, y=-0.010cm',paths=1,source='crop15_U_subscript.png',hand='his hand',kind='drawing'),
]
for g in graphics:
    inventory.append(dict(sheet_kind='text',hand=g['hand'],element=g['element'],kind=g['kind'],
                          position=g['position'],first_words_or_objects=g['objects'],transcribed='yes',graphic=g['id']))
inventory.append(dict(sheet_kind='text',hand='undetermined hand',element='017.B36',kind='text',
                      position='Lower-left archive numeral',first_words_or_objects='16; comment only',transcribed='yes'))

source_rows = [
    (1,'first line directly under on ait',[('subject','D01a','retained'),('est','D01b','retained'),('rare/dense','D01c','retained')]),
    (2,'struck sentence above equalities',[('trouve','D02','retained')]),
    (3,'third equality, first join',[('join','D03','resolved')]),
    (4,'left note',[('Pi/pi','D04a','resolved'),('crossed Sigma','D04b','retained')]),
    (5,'after de X',[('cancelled wording','D05','resolved')]),
    (6,'start of intersection',[('short et','D06a','retained'),('intersection','D06b','resolved')]),
    (7,'under E_j and after later E_j',[('first under-form','D07a','resolved'),('later isolated form','D07b','retained')]),
    (8,'Pi_J above de, and binary partition name',[('first upper ring','D08a','retained'),('binary-name upper ring','D08b','retained')]),
    (9,'last parenthesis',[('g/j','D09','retained')]),
    (10,'last word at right edge',[('Pour/Puis','D10','resolved')]),
    (11,'first complement after inserted Pi_J',[('bar on union','D11','resolved')]),
    (12,'above sur, U subscript',[('predecessor J/j','D12','retained'),('cancelled/live complete state','D12','new qualification')]),
]

report = dict(
    scan=17,reader='B',start_utc='2026-11-20 17:09:06 UTC',end_utc=None,
    model='GPT-6 Astra Pro',effort='not separately exposed',
    full_image_viewed=True,halves_viewed=True,complete_visual_read=True,
    image_views={'whole':1,'half_a':1,'half_b':1,'crop_views':{r['path']:1 for r in manifest['crops']},'failed_or_dropped_views':[]},
    differences=differences,doubts=doubts,inventory=inventory,
    notes={
        'page_content':'Underlined Cas particuliers. A corrected supposition and two closure equalities; a further Sigma_12 equality; a separator; a slanted partition note; a J subset I paragraph, partition display and lower partition prose ending Pour.',
        'author_own_uncertainty_exact_words':[],'author_own_uncertainty_note':'No explicit author doubt word or question mark was identified. Editorial unsure markings are reader uncertainty.',
        'title':'Cas particuliers','date':'No written date observed','page_counts':'Archive pencil 16 at lower left; no author page number is supplied. H page 16 is the witness page identifier, one below our scan.',
        'mathematics_led_reading_decisions':'No algebraic, topological or theorem check was performed. The written X setminus Sigma_i is retained. The dot-like mark and slashed form receive no inferred mathematical role. Formula expectations did not settle uncertain strokes.',
        'witness_apparatus':'H note about X setminus Sigma_i is editorial apparatus, not extra manuscript text. H emph matches the observed title underline. H sqcup and C amalg at the two inspected square joins convey the same selected glyph; that macro conversion creates no row. H page macro is pagination apparatus.',
        'graphic_placement':'All graphical paths are manual approximations of observed strokes. Literal full-scan coordinates are translated by the declared fixed local origins. Text nodes use base-west anchors and zero inner/outer separation; their font extents are not claimed to be original pixel bounds. G03 has only a local upright shape origin and the full source-locus box because its attachment remains unresolved.',
        'crop_limits':'Crop02 clips the top of the contextual initial A, but retains the trouve target and the complete que descender. Crop03 includes the continuation of that descender at its top. Crop09 clips unrelated upper/side context, with the ternaires target and full guide preserved. Crop18 clips part of the following les context, with definies complete. No target was recropped or reopened.',
    },
    notation=[
        {'location':'Top two equalities','signs':r'\Sigma_i^+,\Sigma_i^-,E_i,\overline{\Sigma_i^+},\overline{\Sigma_i^-}','evidence':'Separate closure bars, signed superscripts, dotted short i forms and three-bar E forms.'},
        {'location':'Third equality','signs':r'\overline{\Sigma_{12}},\Sigma_{12},E_1,E_2,\cup','evidence':'Closure rule and lower 12; first cup has two curved passes, G01.'},
        {'location':'Soit line and partition display','signs':r'J\subset I,\ I=J\amalg\{i\},\ X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}\Sigma_j^\alpha','evidence':'Broad J, single subset curve, square joins, coproduct legs, two alpha positions, low ring on pi.'},
        {'location':'Slanted note and inserted partition names','signs':r'\Pi_j,\Pi_J,\Pi_{J,j}','evidence':'Joined upper head with two descending legs; local subscript forms read individually.'},
        {'location':'Two lower upper rings','signs':r'\circ|0','evidence':'Both tiny raised loops remain independently qualified under original C row8.'},
        {'location':'Three lower indexed unions','signs':r'\bigcup;\ \overline{\bigcup};\ \bigcup','evidence':'First and last open tops; a transverse attached upper stroke on the middle, preserved as G08.'},
        {'location':'Top parenthetical prose','signs':'comp. conn.','evidence':'Both abbreviations and their separate terminal points are present; no expansion is introduced.'},
    ],
    check_events=[],crops=manifest['crops'],graphics=graphics,
    C_source_row_map=[{'row':n,'original_place':p,'parts':[{'local_part':part,'difference_id':id,'status':status} for part,id,status in parts]} for n,p,parts in source_rows],
    processing_events=[
        {'id':'P01','type':'image metadata and required half-coordinate offset','inputs':{'full':[1685,2363],'a':[1685,1261],'b':[1685,1262]},'mapping':'b full-scan y = b y + (2363 - 1262)','result':'Offset 1101 pixels. No pixel alignment or image-difference computation.','scope':'Coordinate bookkeeping only.'},
        {'id':'P02','type':'crop image processing','inputs':'The exact 19 source boxes and scales in crops / crop_manifest.json.','mapping':'PIL crop; RGB conversion; autocontrast; crop05 only BICUBIC rotation -42 degrees on expanded white canvas; integer-size LANCZOS resize.','result':'Nineteen saved PNGs, each viewed exactly once. Sixteen created by make_crops.py, three new accent loci by add_accent_crops.py. Existing crops were not regenerated.','scope':'Visual enlargement only; no OCR or image comparison.'},
        {'id':'P03','type':'manual coordinate bookkeeping for guide G05','inputs':{'crop_origin':[947,1345],'scale':8,'approximate_preview_points':[[1435,500],[1752,550],[1910,837],[2251,345]]},'mapping':'x = 947 + u/8; y = 1345 + v/8','result':[[1126.375,1407.5],[1166,1413.75],[1185.75,1449.625],[1228.375,1388.125]],'scope':'Approximate source-coordinate placement for the required stroke drawing. The final manually chosen Bézier path is separately explicit in reading.tex. This does not establish alignment, identity, topology or a theorem.'},
        {'id':'P04','type':'TeX graphics coordinate declarations','inputs':'The full-scan literal paths, origins and units in graphics / reading.tex.','mapping':'A fixed scope translation subtracts each declared origin; then the stated x/y units place the local path. G03 uses only local upright shape coordinates.','result':'Manual graphical approximations with fixed origins and base-west text anchors. No curve-extrema, fitting, numerical area, distance or image-difference calculation was performed.','scope':'Diplomatic graphical representation only.'},
    ],
    brief_feedback=[
        'The first-occurrence recurring-symbol rule and the instruction to preserve every separately named compound-row locality both apply to row8. The TeX marks the first ring and uses the same first candidate at the second; the report keeps both local doubts explicit.',
        'Small nonstandard mathematical glyphs and insertion guides need inline TikZ to keep their physical attachment in prose/math. The standalone separator uses figure; the local inline figures use fixed origins without redefining any macro.',
        'The short wedge at the slanted-note right edge has an uncertain relationship to neighbouring main text. Its supported shape is retained locally and qualified; no character or full missing word is supplied.',
    ]
)
(OUT / 'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')

audit = r'''# Scan 017 — independent reader B

Start: **2026-11-20 17:09:06 UTC**. Model exposed: **GPT-6 Astra Pro**; effort **not separately exposed**.

## Viewing record

I read the brief, assigned packet, notation snapshot and preamble. I viewed the whole scan once for layout, then half a once and half b once for the complete comparison. I made and viewed one enlargement for each of 19 unresolved local groups. No successfully viewed image or decided locus was reopened. The three late crops concern separate local accent loci, not replacements for earlier crops. No other page, reader, root decision, OCR, external source, compiler, renderer or package installer was used.

The original is 1685 × 2363 pixels. Half a is 1685 × 1261; half b is 1685 × 1262. The required bottom-half offset is `2363 - 1262 = 1101`; report boxes use full-scan coordinates. Every crop and transformation is in `crop_manifest.json` and `report.json`.

## Line-by-line audit

| Position | Readable ink and state | Qualification or comparison |
|---|---|---|
| Title | Cas particuliers, single underline | C underline and H emphasis agree. |
| Opening main line | Supposons que ∀i∈I, followed by cancelled Eᵢ/Σᵢ, est/soit, rare/dense, dans X. | The three parts of original C row1 remain separate doubts. The final point is visible. |
| Raised correction | on ait | The words are raised above the cancelled clause; H does not encode insertion. |
| Opening parenthesis | si Σᵢ⁺ Σᵢ⁻ | si is visible; H reads où. No separator comma is supplied between the signed letters. |
| Next line | sont les deux comp. conn. de X∖Σᵢ) | Abbreviation points and the written Sigma complement are retained. H's sic note is apparatus. |
| Cancelled line | Alors on trouve que | trouve remains qualified. The crop clips the initial A context at the top; target word and final descender remain present. |
| First equality | barred Σᵢ⁺ = Σᵢ⁺ ∪ Eᵢ | No comma after Eᵢ; H supplies one. |
| Second equality | barred Σᵢ⁻ = Σᵢ⁻ ∪ Eᵢ . | The distant baseline point belongs to this endpoint; it is retained once. |
| Prose above third equality | Alors je dis qu'on a | Settled on half a; H has Alors je dis que. |
| Third equality | barred Σ₁₂ = Σ₁₂ ∪ E₁ ∪ E₂ | First cup resolved from the curved strokes and drawn as two passes in G01. No algebraic inference used. |
| Divider | Long shallow curve with downturned right end | G02 replaces the straight C rule and fills H's omission. Settled on half a. |
| Slanted note | introduire la partition Πⱼ = {cancelled unsure Σ, live Eⱼ, Σⱼ⁺, Σⱼ⁻} | Π selected; precursor remains unsure. H introduisons differs. A small wedge to the right of the brace remains graphical and locally qualified; its possible neighbouring-text attachment is open. |
| New paragraph opening | Cancelled Supposons; Soit J⊂I tel que I=J⨿{i}. | Entire cancelled word, singleton and final point retained. |
| Considérons line | Consid[e/é]rons la partition, raised Π_J, de X | Accent remains local doubt. G04 preserves the curved insertion guide; no new lexical reading for Π_J. |
| Following line | Cancelled definie, live definie, par les corrected Σ/Eⱼ, (j∈J), | The cancelled word is resolved from its own strokes. The acute is not observed in either local definie. The Sigma under-form of Eⱼ is resolved. |
| intersection line | Cancelled unsure et, one live intersection, des partitions, raised ternaires Πⱼ, de X | Original C row6 has retained short predecessor and resolved longer word. H's state/scope difference is counted once. G05 preserves the long V guide. |
| Next line | (j∈J) definies par les Eⱼ, slashed isolated form, (j∈J) | No acute over the e of definies. The isolated form retains complete states: deleted membership, deleted E, or integral slashed membership. H's ill is counted once. |
| Partition display | X=Eⱼ ⨿ coproduct over α∈π₀(X∖Eⱼ) of Σⱼ^α | Read from half b; both alpha positions, index and coproduct retained. No result verified. |
| Lower prose first line | -- c'est aussi la partition definie par | No acute observed over the e of this definie. |
| Lower second line | celle de [qualified detached point] union over j∈J Eⱼ en les Eⱼ, | G06 preserves the discrete point; no mathematical role or hand assigned. |
| Lower third line | et la partition, raised Π_J with upper ring, de X∖union Eⱼ, intersection | Circle/zero remains qualified. G07 preserves the curved guide. G08 preserves the middle union's visible transverse upper stroke. |
| Lower fourth line | des partitions binaires Π_{J,j} with upper ring; raised (j∈J); induites | Original row8's second ring remains a separate local doubt. G09 preserves the connected guide; H reads its left portion as a prose parenthesis. |
| Last line | sur, raised U with crowded subscript and =, X∖union Eⱼ par les Πⱼ (g/j∈J). Pour | U retains predecessor and complete-state alternatives; G10 draws its guide. Last g/j remains doubtful. Only one final closing parenthesis is visible. Pour resolved locally, without another page. |
| Lower left | Archive numeral 16 | Comment only; writer undetermined. |

## Original C source-row map

| Original row | Local parts retained separately | Outcome |
|---|---|---|
| 1 | subject; short verb; adjective | All retained: D01a–c. |
| 2 | trouve | Retained: D02. |
| 3 | first join | Resolved to the curved cup; both passes drawn: D03/G01. |
| 4 | Π/π; cancelled Σ under E | Π resolved; predecessor retained: D04a–b. |
| 5 | cancelled wording after de X | Resolved definie: D05. |
| 6 | short et; longer intersection | First retained, second resolved: D06a–b. |
| 7 | first under-form; later isolated form | Sigma resolved; later sign and state retained: D07a–b. |
| 8 | first upper ring; binary-name upper ring | Both retained: D08a–b. First occurrence carries the TeX qualification. |
| 9 | final g/j | Retained: D09. |
| 10 | Pour/Puis | Pour resolved: D10. |
| 11 | middle union transverse stroke | Stroke present, literal geometry retained: D11/G08. |
| 12 | earlier J/j; complete corrected/retraced state | Retained and explicitly qualified: D12. |

The twelve original source rows keep their identities. Notation-table entries were not counted as extra doubts. A compound row with mixed outcomes remains one original row with its own local parts.

## Graphics and source coordinates

G01 has two literal curved paths. G02 is the one separator path. G03 is the qualified wedge. G04, G05, G07, G09 and G10 are the five insertion guides. G06 is the qualified point. G08 contains the cup outline and its upper transverse run. Each has a dedicated inventory item, report mapping and comment in the TeX.

The paths are manual approximations. Their full-scan coordinates use fixed scope translations, with the local origins and x/y units in the report; text uses base-west anchors with zero inner and outer separation. G03 has local upright coordinates only because attachment remains open. The source locus boxes, chosen drawing rectangles and font extents are not asserted to coincide. No path bounds or geometric identities were numerically proved.

## Computation and verification disclosure

No mathematical check was performed, so `check_events` is empty. Reading a manuscript assertion was not treated as a proof event.

Actual processing is disclosed separately in `processing_events`: image dimensions and the required half offset; the exact crop/rotation/autocontrast/LANCZOS operations; a manual linear coordinate conversion for approximate G05 preview points; fixed coordinate translations for the TeX shapes; and the structural source checks appended at completion. The preview conversion uses `(x,y)=(947+u/8,1345+v/8)` and its fixed inputs and numerical outputs are in P03. It only helped place the required stroke drawing and supplies no image alignment or mathematical result.

No renderer or compiler was invoked. The selected complete `reading.tex` and `report.json` are read together before return. Remaining uncertain glyphs, words, states and mark roles are explicit in both.
'''
(OUT / 'reading.md').write_text(audit,encoding='utf-8')
print(json.dumps({'differences':len(differences),'doubts':len(doubts),'inventory_items':len(inventory),'original_C_rows':len(source_rows),'crops':len(manifest['crops'])},ensure_ascii=False))
