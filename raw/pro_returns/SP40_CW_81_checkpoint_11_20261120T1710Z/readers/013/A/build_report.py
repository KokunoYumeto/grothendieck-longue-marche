from pathlib import Path
import json,datetime
R=Path('/workspace/scratch/94548b74fbe0/out/readers/013/A')
P=Path('/workspace/scratch/94548b74fbe0/packets/013')
crops=json.loads((R/'crops.json').read_text())
cm={c['path']:c for c in crops}
diffs=[]
def add(id,loc,C,reading,evidence,confidence='high',kind='other',status=None,crop=None,bbox=None,source=None,changed=True,**extra):
    if bbox is None and crop: bbox=cm[crop]['bbox']
    d={'id':id,'location':loc,'C':C,'H':None,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':changed,'diff_H':False,'C_doubt_status':status,'readers_crop':crop,'bbox':{'coordinate_system':'original full scan, top-left origin, pixels','xyxy':bbox},'mathematical_consequence':None}
    if source:d['C_doubt_source_row']=source
    d.update(extra); diffs.append(d)
# Fourteen local decisions map the thirteen source doubtful-readings rows.
add('A-D01','A heading; pale form below the dark A',r'\deleted{\unsure{\mathrm A}}\mathrm A',r'pale \unsure{\deleted{A}|A} below the dark A; exterior pale curves retained',
'Two sloping legs, crossbar and lower feet support A independently of the dark letter. The pale form extends below the horizontal rule. Its crossed/overwritten state is not settled by an independent crossing stroke; the source cancellation is retained as the first state candidate. Two exterior pale curves are separately drawn.', 'medium','deletion state (struck given live or live given struck)','resolved','01_A_overwrite.png',source='C-Doubtful-01',change_group='A-heading',original_glyph_doubt_resolved=True,new_state_doubt=True,components=['pale A glyph','left pale curve (178,555) to (186,585)','right pale curve (230,555) to (230,585)'])
add('A-D02','First main title, final word',r'\unsure{Méditation|Méditations}','Méditation',
'The terminal arch returns to the baseline in a short right tail. The visible final group supports the singular ending; the accent over é rises rightward.', 'medium','other','resolved','02_meditation.png',source='C-Doubtful-02',change_group='meditation-ending')
add('A-D03','Second main title, beginning of Cascades',r'\deleted{\unsure{C|Ca}}Cascades',r'\deleted{\unsure{C|Ca}} overlapping Cascades; short hooked entry preserved',
'Two C-shaped curves occupy the opening. The narrower upper curve overlaps the following low oval; the strokes leave C/Ca unresolved. The proposed source retains that qualification and restores overlap and the short lower-left hook.', 'low','insertion or placement','retained','03_cascades.png',source='C-Doubtful-03',change_group='cascades-overlap',doubt_reading_changed=False,change_reason='Spatial overlap and hooked entry; retention of the original C/Ca doubt contributes no separate change count.')
for id,source,loc,C,reading,evidence,crop,status,conf,group in [
('A-D04','C-Doubtful-04','A, hatched subdivision',r'\deleted{(\unsure{\mathrm i})}',r'\deleted{(\unsure{i})}', 'The surrounding parentheses and one low inner hooked segment survive. Diagonal strokes cover the upper inner shape; i stays qualified. Five drawn hatch paths approximate the merged visible diagonals.','04_cross_A.png','retained','low','cross-A'),
('A-D05','C-Doubtful-05','B, hatched subdivision',r'\deleted{(\unsure{\mathrm{ii}|\mathrm i})}',r'\deleted{(ii)}','Two separate inner downstrokes with lower turns survive between the parentheses; the right-hand dot is distinct, and the left inner upright remains visible below the slash. These local strokes support ii. Four hatch paths preserve the visible cancellation geometry.','05_cross_B.png','resolved','medium','cross-B'),
('A-D06','C-Doubtful-06','C, hatched subdivision',r'\deleted{(\unsure{\mathrm i|\mathrm{ii}})}',r'\deleted{(\unsure{i|ii})}','The lower inner hook survives, while the upper interior merges with three broad oblique hatch bands. The source i/ii alternatives remain supported.','06_cross_C.png','retained','low','cross-C'),
('A-D07','C-Doubtful-07','D, hatched subdivision',r'\deleted{(\unsure{\mathrm i})}',r'\deleted{(i)}','A detached round dot and the short lower inner stem/turn survive before the right parenthesis. These support a single i locally. Four oblique paths reproduce the visible hatch.','07_cross_D.png','resolved','medium','cross-D'),
('A-D08','C-Doubtful-08','E (Notes 20), hatched subdivision',r'\deleted{(\unsure{\mathrm i|\mathrm{ii}})}',r'\deleted{(\unsure{i|ii})}','One lower upright is exposed, but the left interior and upper marks remain covered. The source i/ii qualification is retained. Four local diagonal paths reproduce the hatch.','08_cross_E20.png','retained','low','cross-E20'),
('A-D09','C-Doubtful-09','E (Notes 23), hatched subdivision',r'\deleted{(\unsure{\mathrm{iv}|\mathrm{iii}})}',r'\deleted{(\unsure{iv|iii})}','The left inner upright and the following low bowl/turn remain visible. Hatch intersections obscure the other inner boundaries; iv/iii stays unresolved. Four local hatch paths are retained.','09_cross_E23.png','retained','low','cross-E23')]:
    add(id,loc,C,reading,evidence,conf,'drawing or diagram',status,crop,source=source,change_group=group,doubt_reading_changed=(status=='resolved'),change_reason='Local candidate decision and explicit diagonal cancellation paths; no reading was inferred from the live row.')
add('A-D10','First column, pale question mark below the hatched row',r'\unsure{?}','?',
'Half a shows the curved upper question stroke and a separated low point at the left of the descending arrow. The question-mark glyph is readable; its intended referent remains unstated.', 'medium','other','resolved',bbox=[119,939,143,982],source='C-Doubtful-10',change_group='lower-question',half_evidence={'image':'J81-02_81_scan013_a.jpg','origin':[0,0],'bbox':[119,939,143,982]})
add('A-D11','D, pale form at the live subdivision',r'\deleted{\unsure{(\mathrm i)}}(\mathrm i)',r'pale \unsure{\deleted{(i)}|(i)} above/left of the dark (i)',
'The upper-left opening parenthesis, raised dot, short interior stem and upper closing curve can all be followed separately from the lower dark row. The glyphs resolve to (i); the visible overlap leaves cancellation/live state qualified. The pale form is above and left of the darker form in the inspected image.', 'medium','insertion or placement','resolved','10_live_D.png',source='C-Doubtful-11',change_group='live-D-overlap',original_glyph_doubt_resolved=True,new_state_doubt=True)
add('A-D12','B, secondary title',r'Vers un \unsure{plus} long Voyage','Vers un plus long Voyage',
'The descending p loop, tall l loop, low u cup and final s-shaped turn are visible in sequence. The neighboring words and capital V of Voyage were separately read.', 'high','other','resolved','11_plus.png',source='C-Doubtful-12',change_group='plus')
add('A-D13a','A, pale form below the live subdivision',r'\deleted{\unsure{(\mathrm i)}}(\mathrm i)',r'pale \unsure{\deleted{(i)}|(i)} below the dark (i)',
'The lower opening parenthesis, short inner stem and closing parenthesis are visible in pale ink. The glyphs support (i) without using the dark row as their reading. The pale state remains qualified because no independent strike through this lower form is isolated.', 'medium','deletion state (struck given live or live given struck)','resolved','12_live_A.png',source='C-Doubtful-13',change_group='live-A-overlap',source_sublocus='13a: under first live subdivision',original_glyph_doubt_resolved=True,new_state_doubt=True)
add('A-D13b','C, pale traces at the third live subdivision',r'\deleted{\unsure{(}}(\mathrm i)',r'pale \unsure{\deleted{\unsure{(i)|(}}|\unsure{(i)|(}} before the dark (i)',
'The pale opening curve is definite. A separate high pale dot, a pale inner vertical segment and the upper/right gray curve support a fuller (i) candidate, but their overlap with the dark strokes leaves the partial-opening candidate viable. The pale cancellation/live state also stays qualified.', 'low','misread symbol or index','retained','13_live_C.png',source='C-Doubtful-13',change_group='live-C-overlap',source_sublocus='13b: at third live subdivision',new_state_doubt=True)
# Other actual graphical changes, each with a local location and component map.
add('A-G01','Six-column layout and visible ruling',r'\begin{array}{@{}c|c|c|c|c|c@{}} with uniform array rules','Text nodes at six observed column positions; twelve horizontal-rule paths plus two pale vertical traces',
'The halves show individual horizontal rules with uneven vertical spacing and interrupted pale portions. The long pale traces occur near x=400 and x=1570; their surface origin remains undetermined. The proposed paths preserve the observed visible components and their positions instead of the five uniform vertical separators in C.', 'medium','drawing or diagram',bbox=[20,18,2352,1670],change_group='layout-rules',half_evidence={'a':'full half a, origin (0,0)','b':'full half b, origin (1122,0)'},components=['R01--R12 in reading.tex: horizontal rules','V01 near x=400','V02 near x=1570'])
add('A-G02','Cancelled A (1976/77) below Notes 1',r'\deleted{A (1976/77)}','A (1976/77), with explicit diagonal hatch paths',
'All characters and parentheses remain readable. The cancellation consists of many oblique strokes with merged crossings and several low curved returns. Fourteen approximation paths T01.H01--T01.H14 preserve that geometry; this is an approximation-path count, not a claim to reconstruct fourteen original pen movements.', 'high','drawing or diagram',crop='16_top_cancellation.png',change_group='cancelled-top-heading')
add('A-G03','Upper-left margin, main bar/arrow/brace/opposed-arrow cluster',r'\bar{\uparrow}\ \Bigg\{\quad ?\,\begin{smallmatrix}\downarrow\\\uparrow\end{smallmatrix}','M01--M03: bar, long upward shaft, brace, pale parallel strokes, ?, opposed arrows and curved connection',
'The crop exposes a short second shoulder at the upper arrow, a pale parallel shaft and brace continuation, a short internal curve beside the brace, the question mark, and a curved run between the two small arrowheads. These components are individually preserved as paths; arrow/brace meanings are not supplied.', 'high','drawing or diagram',crop='14_margin_arrows.png',change_group='upper-margin-cluster',components=[{'id':'M01','shape_confidence':'high','description':'bar, long shaft, upper arrowhead and short extra shoulder'},{'id':'M02','shape_confidence':'high','description':'dark brace, pale parallel continuation and interior small curve'},{'id':'M03','shape_confidence':'medium','description':'?, two opposed heads and their curved intervening run; tiny pale parallel head at x112'}])
add('A-G04','Immediately above the upper-left bar',None,'M04: small detached gray mark',
'A small vertical gray oval-like mark is visible above the bar at approximately (47,404). Its character value, hand and surface origin remain undetermined.', 'medium','omission',crop='14_margin_arrows.png',bbox=[43,398,51,410],change_group='margin-detached-mark')
add('A-G05','Between first date and Découverte',r'\begin{smallmatrix}\rule[.15ex]{1.4em}{.35pt}\hspace{-.4em}\uparrow\\\rule[.15ex]{1.4em}{.35pt}\hspace{-.4em}\downarrow\end{smallmatrix}','A02: two bent arrows; lower arrow has an additional converging horizontal rule',
'The upper rule turns vertically upward at its right end. The lower right-turning path has a second distinct lower rule beginning near x254 and converging near x317. Both bends and both arrowheads are retained, with the extra lower rule drawn explicitly.', 'high','drawing or diagram',crop='15_bent_arrows.png',change_group='bent-arrows')
add('A-G06','Near the upper bent arrow in the first column',None,'A03: pale crescent above its left start, short detached slash near the upper head, and small dot below the rule',
'Three discrete components are visible: the shallow pale curve from about (257,665) to (278,661), the short darker slash near (307,652), and the small gray dot near (304,673). Their hand, surface origin and function remain undetermined.', 'medium','omission',crop='15_bent_arrows.png',bbox=[250,644,315,678],change_group='bent-arrow-residuals',components=[{'id':'A03a','shape_confidence':'medium','bbox':[255,657,280,667]},{'id':'A03b','shape_confidence':'high','bbox':[305,650,313,656]},{'id':'A03c','shape_confidence':'medium','bbox':[301,670,307,676]}])
add('A-G07','Pale traces behind the first title',None,'A04: pale vertical and baseline fragments behind Méditation',
'The title crop exposes several gray vertical residual strokes and short baseline continuations around the dark letters. The proposed graphic preserves representative supported paths without supplying another word. Some gray continuations reach the top of the tight word crop; their character value and surface origin remain unresolved.', 'low','omission',crop='02_meditation.png',bbox=[121,789,350,845],change_group='meditation-residuals',boundary_limit='Some upper pale continuations meet y=789, the crop boundary. No repeat crop was made.')
add('A-G08','Initial R of Réveil and its immediate diagonal surroundings',None,'B01: interrupted upper-left diagonal marks, pale inner wedge and lower-right fragments',
'The crop shows a detached broad upper-left mark, a second short slash separated by white gaps, a pale diagonal continuation at R, a gray interior wedge and two short lower-right traces. Their visible shapes are retained separately. No extra letter or punctuation is assigned.', 'medium','omission',crop='17_reveil_initial.png',change_group='reveil-residuals',components=['broad mark (500,694)--(509,703)','short slash (513,706)--(517,710)','pale continuation (518,711)--(529,721)','inner wedge (533,728)--(541,734)','lower-right fragments (549,739)--(558,749)'])
add('A-G09','Below the g descender of long in the B secondary title',None,'G01: short detached dark dash',
'The enlargement shows a detached short dark mark below and left of the end of the g descender, near (593,1240). The gap is retained. Its role and hand remain undetermined.', 'high','omission',crop='11_plus.png',bbox=[587,1235,599,1245],change_group='long-detached-dash')
add('A-G10','Blank area above the first footer',None,'G02: interrupted descending trace',
'The crop shows a dark upper short segment, separated dark spot and two paler lower pieces running from about (234,1409) to (229,1438). They are preserved as one local graphic cluster with no character assigned.', 'medium','omission',crop='18_low_left_trace.png',change_group='above-footer-trace')
add('A-G11','Below and to the right of the first footer',None,'G03: separated spots and pale curved segment',
'The crop exposes a pale upper spot, a darker spot and small dark segment, followed by a pale hooked lower run near x332--340, y1583--1609. The visible gaps are retained; role, hand and surface origin remain undetermined.', 'medium','omission',crop='19_low_left_pale.png',change_group='below-footer-trace')
add('A-G12','Below Fringale, at approximately x1934,y1362',None,'G04: small gray irregular dot',
'The small gray patch is separated from the translation and the rule. The irregular outline is preserved graphically; role, hand and surface origin remain undetermined.', 'medium','omission',crop='20_lower_right_marks.png',bbox=[1928,1355,1942,1370],change_group='lower-gray-dot')
add('A-G13','Below the last translation-level rule, near x2252--2268,y1344',None,'G05: short gray horizontal dash',
'The short dash is visible below the rule, with a slight downward rightward run. Its role and hand remain undetermined.', 'high','omission',crop='20_lower_right_marks.png',bbox=[2247,1338,2273,1349],change_group='lower-right-dash')
add('A-G14','On the translation-level rule in the last column',None,'G06: local dark wedge on the rule',
'The dark wedge near x2221--2235,y1304 sits on the existing rule. The graphic uses a single local filled component adjoining that rule rather than a second independent rule.', 'high','omission',crop='20_lower_right_marks.png',bbox=[2217,1298,2239,1309],change_group='lower-rule-darkening')
add('A-G15','On the live-subdivision rule near the right edge',None,'G07: local darkening on the rule near x2308--2321',
'The crop shows a local dark wedge left of the diagonal edge stroke. Its connection to the horizontal rule is preserved; no separate character is assigned.', 'high','omission',crop='23_edge_lower.png',bbox=[2308,1086,2324,1096],change_group='subdivision-rule-darkening',boundary_limit='The leftward rule continues through the crop boundary; the local wedge and its right endpoint are present, and the rule itself was read on half b.')
edge_components=[
('E01','(.25,.031)--(1.0,.038)--(.32,.038)',[2333,113,2351,132],'21_edge_top.png','high','two oblique/horizontal branches at the top rule'),
('E02','(.42,.083)--(1.0,.088)--(.40,.088)',[2329,197,2351,212],'21_edge_top.png','high','oblique branch and lower hooked run'),
('E03','(.12,.192)--(1.0,.200)--(.20,.200)',[2327,362,2351,379],'21_edge_top.png','high','two converging branches'),
('E04','(.12,.230)--(1.0,.234)--(.18,.233)',[2326,414,2351,432],'21_edge_top.png','high','oblique upper branch and curved lower branch'),
('E05','(.30,.318)--(.95,.324)--(.12,.324)',[2322,548,2347,568],'22_edge_middle.png','high','diagonal branch, horizontal branch and short downturned terminal before the paper edge'),
('E06','(.37,.375)--(.96,.382)--(.36,.380)',[2328,635,2350,654],'22_edge_middle.png','high','two converging branches with visible white space before the boundary'),
('E07','(.47,.592)--(.96,.600)--(.36,.600)',[2332,962,2351,981],'23_edge_lower.png','medium','pale interrupted upper diagonal and lower hooked branch'),
('E08','(.37,.675)--(.95,.682)',[2327,1078,2345,1096],'23_edge_lower.png','high','diagonal reaching the live-subdivision rule'),
('E09','(.58,.752)--(.96,.758)',[2331,1195,2347,1211],'23_edge_lower.png','high','short broad diagonal above the lower-title rule'),
('E10','(.38,.976)--(.77,.982)',[2327,1560,2340,1579],'24_edge_foot.png','high','short diagonal with a dark downturned terminal')]
add('A-G16','Ten surviving groups along the right edge',"C's ten explicit right-edge draw subpaths",'E01--E10, individually mapped to the original ten components',
'The ten original source path entries were compared with the corresponding local strokes. Their differing branch angles, curved returns, interruptions, terminal downstrokes and distances from the paper edge are preserved. No eleventh edge group is inferred from G07, which is the separately recorded darkening on the horizontal rule.', 'high','drawing or diagram',crop='21_edge_top.png',bbox=[2322,113,2351,1579],change_group='right-edge-paths',components=[{'id':eid,'C_source_path':c,'bbox':b,'crop':crop,'shape_confidence':conf,'description':desc,'role':'undetermined','hand':'undetermined hand'} for eid,c,b,crop,conf,desc in edge_components],additional_crops=['22_edge_middle.png','23_edge_lower.png','24_edge_foot.png'])
add('A-G17','Lower first-column arrow and B descending arrow',r'\downarrow ; \searrow','L01--L02: observed shafts, head legs and upper hook in their local positions',
'Half a shows the first faint arrow beginning with a small curved entry beside the hatched row, then descending to an open head. The second arrow has a shallow curved shaft ending down-right just above (ii). Their physical positions and shapes are preserved.', 'medium','drawing or diagram',bbox=[148,909,543,1056],change_group='lower-arrow-geometry',half_evidence={'image':'J81-02_81_scan013_a.jpg','origin':[0,0],'first_arrow_bbox':[148,909,178,1005],'second_arrow_bbox':[519,994,543,1056]})
# Source-doubt identity map: source row 13 has two independently reported subloci.
rowmap=[]
for n in range(1,14):
    ds=[d for d in diffs if d.get('C_doubt_source_row')==f'C-Doubtful-{n:02d}']
    rowmap.append({'source_section':'Doubtful readings','source_row_id':f'C-Doubtful-{n:02d}','source_row_count':1,'local_decisions':[{'difference_id':d['id'],'sublocus':d.get('source_sublocus',d['location']),'status':d['C_doubt_status'],'crop':d['readers_crop'],'bbox':d['bbox']} for d in ds]})
# Remaining local uncertainties: ink candidates and state candidates, plus unassigned graphic roles.
doubts=[]
def doubt(loc,reading,alts,conf,reason,crop,id,bbox=None):
    doubts.append({'id':id,'location':loc,'reading':reading,'alternatives':alts,'confidence':conf,'reason':reason,'crop':crop,'bbox':{'coordinate_system':'original full scan, top-left origin, pixels','xyxy':bbox or cm[crop]['bbox']}})
doubt('Pale A below dark A','A with cancelled/overwritten state first',['live pale A'],'medium','A glyph resolves; a separate cancelling stroke is not isolated.','01_A_overwrite.png','U01')
doubt('Opening overlap in Cascades','cancelled C',['cancelled Ca'],'low','Intertwined C-shaped curves and lower oval leave the predecessor extent unresolved.','03_cascades.png','U02')
doubt('A crossed subdivision','(i)',['unrecovered interior beyond the supported i candidate'],'low','Hatch covers most interior strokes.','04_cross_A.png','U03')
doubt('C crossed subdivision','(i)',['(ii)'],'low','Inner upper strokes are merged with oblique hatch.','06_cross_C.png','U04')
doubt('E (Notes 20) crossed subdivision','(i)',['(ii)'],'low','The exposed lower upright does not settle the obscured left interior.','08_cross_E20.png','U05')
doubt('E (Notes 23) crossed subdivision','(iv)',['(iii)'],'low','Hatch intersections obscure boundaries between the surviving inner components.','09_cross_E23.png','U06')
doubt('Pale upper form beside D live subdivision','(i), cancelled/overwritten state first',['live (i)'],'medium','Glyphs resolve; the physical overlap leaves the cancellation state open.','10_live_D.png','U07')
doubt('Pale lower form beneath A live subdivision','(i), cancelled/overwritten state first',['live (i)'],'medium','Readable pale parentheses and inner stem; no isolated cancelling stroke.','12_live_A.png','U08')
doubt('Pale form beside C live subdivision','(i), cancelled/overwritten state first',['opening parenthesis only','live state for the same visible pale components'],'low','Pale dot, inner vertical and right curve support fuller (i), while overlap leaves the shorter recovered extent viable.','13_live_C.png','U09')
for did in ['A-G01','A-G04','A-G06','A-G07','A-G08','A-G09','A-G10','A-G11','A-G12','A-G13','A-G14','A-G15']:
    d=next(x for x in diffs if x['id']==did)
    doubts.append({'id':'U-role-'+did,'location':d['location'],'reading':d['reading'],'alternatives':[],'confidence':d['confidence'],'reason':'Visible graphical component(s) preserved; character value, role, hand and/or surface origin remain undetermined. No semantic alternate is invented.','crop':d['readers_crop'],'bbox':d['bbox']})
# Inventory: all original items covered and each new path cluster explicitly mapped.
inv=json.loads((P/'C_inventory.json').read_text())
for it in inv:
    it['sheet_kind']='list';it['hand']='his hand';it['transcribed']='yes'
    it.pop('cote',None);it.pop('scan',None)
inv[0]['kind']='drawing';inv[0]['first_words_or_objects']='Six-column list with text nodes and visible ruling'
inv[1]['first_words_or_objects']='Ten right-edge groups E01--E10, mapped individually in report'
for e,text in [('013.11','Pale A, glyph resolved; cancelled/live state qualified; exterior curves separately retained'),('013.19','Découverte de la Méditation; final singular resolved'),('013.27','(ii), locally resolved beneath hatch'),('013.29','(i), locally resolved beneath hatch'),('013.32','Readable pale ? and descending arrow with small hooked entry'),('013.34','Pale (i) below live form; glyph resolved, cancelled/live state qualified'),('013.35','Pale (i) or opening parenthesis at live form; extent and state qualified'),('013.36','Pale (i) above/left of dark (i); glyph resolved, state qualified'),('013.38','(ii) Vers un plus long Voyage; plus resolved')]:
    next(i for i in inv if i['element']==e)['first_words_or_objects']=text
for e in ['013.11','013.34','013.35','013.36']:
    next(i for i in inv if i['element']==e)['state']='cancelled/overwritten first candidate; live alternative retained'
extra_inv=[
('013.49','text','lower right, sideways','Archive pencil numeral 12, recorded in the TeX comment','undetermined hand',None),
('013.50','drawing','whole sheet','R01--R12: twelve horizontal-rule approximation paths','undetermined hand',['R01','R02','R03','R04','R05','R06','R07','R08','R09','R10','R11','R12']),
('013.51','drawing','near x400 and x1570','V01--V02: two pale long vertical traces','undetermined hand',['V01','V02']),
('013.52','drawing','around pale A below dark A','A01: pale exterior left and right curves','undetermined hand',['left curve','right curve']),
('013.53','drawing','behind Méditation','A04: pale vertical and baseline residuals','undetermined hand',['five vertical approximations','two baseline fragments']),
('013.54','drawing','above upper-left bar','M04: detached gray oval-like mark','undetermined hand',['M04']),
('013.55','drawing','upper-left arrow and brace','M01--M03: pale parallel/retraced and intervening curved components','undetermined hand',['M01 parallel shaft','M02 pale brace','M02 small inner curve','M03 pale small head','M03 curved connector']),
('013.56','drawing','near upper bent arrow','A03a--c: crescent, slash and dot','undetermined hand',['A03a','A03b','A03c']),
('013.57','drawing','around initial R of Réveil','B01: five local groups of interrupted diagonal/pale components','undetermined hand',['broad upper mark','detached slash','pale continuation','inner wedge','two lower-right fragments']),
('013.58','drawing','below long','G01: detached dark dash','undetermined hand',['G01']),
('013.59','drawing','above first footer','G02: interrupted descending trace','undetermined hand',['upper segment','dark spot','two lower pale pieces']),
('013.60','drawing','below first footer','G03: separated spots and pale hooked segment','undetermined hand',['upper pale spot','dark spot','dark short segment','pale lower run']),
('013.61','drawing','below Fringale','G04: small gray irregular dot','undetermined hand',['G04']),
('013.62','drawing','below last column rule','G05: short gray dash','undetermined hand',['G05']),
('013.63','drawing','on rule near x2227,y1304','G06: local dark wedge connected to rule','undetermined hand',['G06']),
('013.64','drawing','on rule near x2314,y1091','G07: local darkening connected to rule','undetermined hand',['G07'])]
for eid,kind,pos,first,hand,components in extra_inv:
    it={'sheet_kind':'list','hand':hand,'element':eid,'kind':kind,'position':pos,'first_words_or_objects':first,'transcribed':'yes'}
    if components:it['components']=components
    inv.append(it)
# Add exact path-component annotations to original deletion/drawing entries.
for eid,prefix,count in [('013.09','T01.H',14),('013.26','XA.H',5),('013.27','XB.H',4),('013.28','XC.H',3),('013.29','XD.H',4),('013.30','XE20.H',4),('013.31','XE23.H',4)]:
    next(i for i in inv if i['element']==eid)['graphical_components']={'prefix':prefix,'approximation_path_count':count,'count_type':'explicit paths in reading.tex; merged pen strokes prevent a claim about original writing movements'}
next(i for i in inv if i['element']=='013.02')['components']=[{'id':a,'C_source_path':b,'bbox':c} for a,b,c,*_ in edge_components]
next(i for i in inv if i['element']=='013.18')['components']=['upper bent arrow','lower bent arrow','additional converging lower rule']
notation=[
{'location':'six main letters','visible_form':'A B C D E E','latex':'A, B, C, D, E, E','evidence':'Separate plain capital stems and horizontal bars, inspected in both halves.'},
{'location':'live subdivision row, six columns','visible_form':'(i), (ii), (i), (i), (i), (iv)','latex':r'(i), (ii), (i), (i), (i), (iv)','evidence':'Local dotted small strokes and parentheses, with the last v-shaped inner form.'},
{'location':'first two Roman-number footer entries','visible_form':'HS I; Sch I','latex':r'HS $\mathrm I$; Sch $\mathrm I$','evidence':'Single vertical shafts with upper/lower serif bars.'},
{'location':'last two footer entries','visible_form':'Sch VI; Sch IX, shared top and bottom bars','latex':r'Sch $\overline{\underline{\mathrm{VI}}}$; Sch $\overline{\underline{\mathrm{IX}}}$','evidence':'Each two-letter numeral has common extended upper and lower rules.'},
{'location':'first footer','visible_form':'M 1976 *','latex':r'M 1976 $\mathord{*}$','evidence':'Small multi-ray star beside the year at baseline height.'},
{'location':'last secondary title','visible_form':'Le paired-double-tick Maître paired-double-tick','latex':"Le ``Maître''",'evidence':'Paired short strokes flank Maître; circumflex over î.'},
{'location':'footer abbreviations','visible_form':'M; HS; Sch','latex':'M; HS; Sch','evidence':'No expansion is written on this sheet.'},
{'location':'titles and translations','visible_form':'Découverte; Méditation; Réveil; Bâtisseur; Réalité; Maître','latex':'Découverte; Méditation; Réveil; Bâtisseur; Réalité; Maître','evidence':'Local accent strokes preserved; no spelling modernization.'}]
report={'scan':13,'reader':'A','start_utc':'2026-11-20 13:58:10 UTC','end_utc':None,'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
'viewing_record':{'full_image':{'path':'J81-02_81_scan013.jpg','dimensions':[2365,1688],'successful_view_count':1,'purpose':'layout'},'halves':[{'path':'J81-02_81_scan013_a.jpg','dimensions':[1242,1688],'full_scan_origin':[0,0],'successful_view_count':1},{'path':'J81-02_81_scan013_b.jpg','dimensions':[1243,1688],'full_scan_origin':[1122,0],'successful_view_count':1}],'order':'UTC start and brief/preamble/notation read; assigned packet read; whole image once; half a once; half b once; crops 01--24 once each; source/report synchronization.','crop_count':24,'failed_unseen_image_attempts':0,'recrops':0},
'witness_status':{'C':'full text, doubtful-readings, notes and inventory supplied','H':'nothing; H.tex empty','H_collation_rows':0},
'differences':diffs,'C_doubt_source_map':rowmap,'C_doubt_accounting':{'source_rows':13,'local_subloci':14,'resolved_original_glyph_or_word_doubts':8,'retained_original_doubts':6,'count_note':'Row 13 is one source row with local subloci 13a and 13b. A retained qualification itself contributes no change; some such rows have diff_C=true solely for a separately described overlap/path change. Each change_group is counted once.'},
'doubts':doubts,'inventory':inv,'notes':{
'page_content':'Six-column handwritten list headed Notes 1, 5, 7, 15, 20, 23, with main letters A B C D E E, years, titles, crossed and live subdivision markers, translations, footer abbreviations, arrows and edge traces.',
'authors_own_uncertainty':'Two question-mark glyphs are written at the left: a dark ? beside the upper opposed-arrow cluster and a pale ? beneath the first crossed subdivision. No verbal expression of authorial uncertainty occurs in the supplied page text.',
'page_numbering':'Archive numeral 12 is pencilled sideways at the lower right and appears only in a TeX comment. No manuscript page-number macro is added.',
'dates':['cancelled A (1976/77)','A (1976/77)','B (1978/79)','C (1979/80)','D (1980)','E (1981)','E (1981)','M 1976 *','M 1979'],
'page_counts':'The written numeric headings are transcribed as Notes 1, 5, 7, 15, 20, 23; no page-count label is supplied.',
'mathematics_led_decisions':'There is no mathematical computation in this reading. Numeral/alphabet decisions use their local strokes. No theorem, reconstruction or repair is supplied.',
'crossed_predecessor_method':'Each crossed interior was judged on its own crop; no glyph was recovered from the live subdivision beneath it.',
'graphical_scope':'All paths are direct approximations of inspected visible components. Black/gray values distinguish relative darkness. Role, hand and surface origin remain unassigned for detached and pale components. Additional annotation text occurs only in comments/report, not as manuscript prose.',
'crop_boundary_limits':['Crop 04 shows the adjoining pale upper hook entering its left edge; that hook was read in half a and is preserved in L01.','Crop 02 meets a few upper gray continuations at its top edge; no second word is supplied from them.','Crop 23 includes the darkening G07 and its right endpoint; the long rule continues through the left crop boundary and was read in half b.'],
'context_boundary':'The assigned notes contain no later-sheet tail to include. The notation snapshot was contextual and each sign on this page was read afresh.',
'validation':'Structural source checks only. No OCR, text recognition, PDF text layer, external source, browser, compiler, renderer, installation or delegation was used.'},
'notation':notation,'check_events':[],'crops':crops,
'brief_feedback':['The supplied kind vocabulary has no dedicated table value. I used drawing for the six-column layout with text nodes and rule paths, retaining each textual inventory item.','For pale doubled forms with readable glyphs but no isolated strike, I qualified cancelled/live state locally and kept the source deletion annotation in an invisible dimensional box, with no extra visible horizontal strike.','Uniform C array rules obscure the uneven line positions and the uncertainty of long pale vertical traces. The return gives explicit graphical paths and states their unassigned surface origin.'],
'structural_validation':{}}
(R/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote report.json:',len(diffs),'decision/change rows;',len(inv),'inventory items;',len(doubts),'local unresolved-reading/role entries.')
# Keep unchanged doubt qualification separate from its graphical change.
report=json.loads((R/'report.json').read_text())
for old,new in [('A-D03','A-G18'),('A-D04','A-G19'),('A-D06','A-G20'),('A-D08','A-G21'),('A-D09','A-G22')]:
    d=next(v for v in report['differences'] if v['id']==old)
    graphic=dict(d)
    graphic.update({'id':new,'C_doubt_status':None,'diff_C':True,'C_doubt_source_row_reference':d['C_doubt_source_row'],'count_note':'This row counts the graphical/placement difference once for the shared physical group. The associated retained-doubt row has diff_C=false.'})
    graphic.pop('C_doubt_source_row',None)
    d.update({'diff_C':False,'kind':'other','change_reason':'The original uncertainty and its first candidate are retained. The independent graphical/placement change is recorded in '+new+'.','graphical_change_row':new})
    if old=='A-D03':
        d['reading']=r'\deleted{\unsure{C|Ca}}Cascades'
    report['differences'].append(graphic)
# The line beneath Méditation is already one of the continuous sheet rules.
g=next(d for d in report['differences'] if d['id']=='A-G07')
g['reading']='A04: pale vertical residual fragments behind Méditation'
g['evidence']='The title crop exposes several gray vertical residual strokes around the dark letters. The proposed graphic preserves supported paths without supplying another word. The horizontal line beneath the word belongs to R07 and is not duplicated. Some gray upper continuations meet the tight crop boundary; their character value and surface origin remain unresolved.'
for i in report['inventory']:
    if i['element']=='013.53':
        i['first_words_or_objects']='A04: five pale vertical residual paths; underlying horizontal rule included once as R07'
        i['components']=['five vertical approximations']
for u in report['doubts']:
    if u['id']=='U-role-A-G07': u['reading']=g['reading']
for c in report['crops']:
    from PIL import Image
    c['output_dimensions']=list(Image.open(R/c['path']).size)
    c['transform']={'autocontrast':True,'resize':'PIL LANCZOS; scale=min(8,2600/width,3200/height)','unsharp_mask':{'radius':1.1,'percent':110,'threshold':3}}
report['C_doubt_accounting']['count_note']='Row 13 is one source row with local subloci 13a and 13b. Five exactly retained qualifications have diff_C=false and separate graphical/placement rows. At 13b the fuller primary candidate differs while uncertainty remains. Each change_group contributes at most one actual C correction.'
report['doubts'].append({'id':'U-role-A-G16','location':'Ten right-edge groups E01--E10','reading':'Local path shapes retained individually','alternatives':[],'confidence':'medium','reason':'Physical components have high shape confidence except pale E07 (medium); character value, hand and role remain undetermined. Individual component boxes/crops are in A-G16.','crop':'21_edge_top.png','bbox':{'coordinate_system':'original full scan, top-left origin, pixels','xyxy':[2322,113,2351,1579]}})
(R/'crops.json').write_text(json.dumps(report['crops'],ensure_ascii=False,indent=2)+'\n')
(R/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Separated unchanged doubt qualifiers from geometry; complete decision rows:',len(report['differences']))
