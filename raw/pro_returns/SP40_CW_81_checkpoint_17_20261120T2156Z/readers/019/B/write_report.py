from pathlib import Path
import json
b=Path('/workspace/scratch/94548b74fbe0/out/readers/019/B')
crops=json.loads((b/'crops/manifest.json').read_text())
cp={e['path'].split('/')[-1].split('_')[0]:e for e in crops}
d=[]
def add(i,location,C,H,reading,evidence,kind='other',dc=False,dh=False,status=None,crop=None,bbox=None,source=None,confidence='medium',**extra):
 e={'id':i,'location':location,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dc,'diff_H':dh,'C_doubt_status':status,'readers_crop':cp[crop]['path'] if crop else None,'bbox':cp[crop]['bbox'] if crop else bbox,'mathematical_consequence':None}
 if source: e['C_source_row']=source
 e.update(extra);d.append(e)
add('B00','page wrapper',r'\cotefile{81}','[no cotefile wrapper]','Omitted the repeated cote wrapper; scanpage{19} retained.','Brief v17 reserves cotefile{81} for scan002. This is a convention adjustment rather than an ink correction.','other',True,False,confidence='high',count_scope='convention only')
add('B01','opening abbreviation', 'Dém.', 'Dém.',r'D\unsure{é|è}m.','Detached accent is short and steep, with a downward-right lower part. Acute remains the first candidate; grave is also supported. The following abbreviation point is clear.',crop='01',confidence='low',count_scope='new qualification, unchanged primary')
add('B02','first-line right edge after 0,1','0,1 Le','0,1, le','0,1 Le','The comma between 0 and 1 is visible. The last numeral reaches the page edge; no additional post-1 comma is visible. No unseen continuation is supplied.','text not on the page',False,True,crop='02',confidence='medium',boundary_limit='The numeral 1 meets the physical right page edge; punctuation beyond that edge cannot be inspected.')
add('B03','second physical line, initial Le','Le','le','Le','A long tall initial stem and separate lower return form capital L.','misread word',False,True,bbox=[275,165,350,230],confidence='high')
add('B04','third line before card',r'\unsure{avec}','[no word] ',r'\unsure{avec}','Three detached compressed marks remain visible before card: a short stroke, a low run, and a curved run. They support avec but do not resolve all letter bodies.','omission',False,True,'retained','03',source='R09',confidence='low')
add('B05','fifth physical line before paired display',r'\unsure{ens.}','ens.','ens.','Half a shows the small connected e/n/s run with a separate terminal ink point.','other',True,False,'resolved',bbox=[270,510,390,545],source='R01',confidence='high')
add('B06','first U in paired display',r'\unsure{U|\deleted{=}U}_{J,i}',r'U_{J,i}','Complete graphical U G01 with entrance paths; cancelled-equals alternative retained.','The upper short arc enters the left U stem. A second arched run and a near-horizontal lower run extend left from that stem. Their shape is visible; flourish/cancelled-equals role remains unresolved. G01 draws the body and both extra runs once.','drawing or diagram',True,True,'retained','04',source='R10',confidence='medium',qualification='C primary U with entrance retained. One graphical cluster is counted; its cancellation-role uncertainty is not an additional physical count.',components=['G01a main upper entrance and U body','G01b left arched run','G01c left lower run'])
add('B07','below first display, l’une/l’un',r"\unsure{l'une|l'un}","l'un",r"\unsure{l'une|l'un}",'The low run after n bends downward and returns; it can support a final e but its separation from the terminal stroke is unresolved. H’s l’un survives as an alternative.','misread word',False,True,'retained','05',source='R11',confidence='medium',qualification='Qualified primary difference from H; no conclusive H error is claimed.')
add('B08','below the end of l’une/l’un','[no separately preserved marks]','[no separately preserved marks]','G02: darker round trace and fainter short lower trace, locally unsure.','A compact dark point lies just below the end of the word; a smaller faint upright trace lies farther left and lower. Their attachment to the word, writer and surface origin are not established.','drawing or diagram',True,True,crop='05',confidence='medium',observed_bbox=[1127,791,1165,813],components=[{'id':'G02a','shape':'dark compact point','shape_confidence':'high','source_position':[1160,795]},{'id':'G02b','shape':'faint short upright trace','shape_confidence':'low','source_position':[1130,810]}],interpretation_confidence='low')
add('B09','after Par hyp. de récurrence',r'\unsure{on a}','on a',r'\unsure{on a}','The three marks are a short dark dash, a paler low run with a terminal hook, and a dark point. The words remain heavily compressed.','other',False,False,'retained','06',source='R02',confidence='low')
add('B10','first large indexed join',r'\unsure{\coprod|\bigsqcup}',r'\coprod',r'\unsure{\coprod|\bigsqcup}','Two tall sides, an interior curved bowl and a projecting foot line are visible. The footed-coproduct reading remains primary, with the square-union alternative retained. No algebraic identification was used.','other',False,False,'retained','07',source='R03',confidence='medium')
add('B11','under first large join, predecessor at K0',r'\deleted{\unsure{J}}K_0',r'K_0',r'\deleted{\unsure{J}}K_0','A thin earlier loop and curved upper remnant survive under the heavy K strokes. J remains the supported candidate, but the overwrite does not settle its full body.','omission',False,True,'retained','07',source='R04',confidence='low')
add('B12','brace line 1, predecessor under K0',r'\deleted{\Sigma_{\unsure{\alpha|0}}}K_0',r'K_0',r'\deleted{\Sigma_{\unsure{\alpha|0}}}K_0','The older Sigma has distinct leftward horizontal runs and a diagonal return. Its small lower loop is crossed by the replacement K leg: alpha remains primary, zero retained.','omission',False,True,'retained','08',source='R12',confidence='medium')
add('B13','lead-in below the brace',r'\unsure{On a}',r'\struck{On}\uncertain{On a}',r'\unsure{On a|\deleted{O}On a|\deleted{On}On a}','There is one crowded initial capital group, one lower n run, and a separate a-like point before donc. The initial loops support an overwritten O reading as well as a retraced live capital. A separate fully recoverable predecessor n is not settled.','deletion state (struck given live or live given struck)',False,True,'retained','09',source='R05',confidence='low',qualification='Primary reading remains C’s On a. H’s cancellation reading is retained as a complete-state alternative; no writing chronology is inferred.')
add('B14','later large indexed join in U equality',r'\coprod',r'\coprod',r'\coprod; local \bigsqcup alternative retained in report','This occurrence independently shows tall sides, an extended foot and a curved lower retrace. The first-occurrence rule places the printed coprod/bigsqcup doubt at B10, while this local alternative remains recorded.',crop='10',confidence='medium',count_scope='independent recurrence audit, unchanged primary')
add('B15','far right of the penultimate display','[no mark]','[no mark]','G03: two detached dark points in a descending-left pair, locally unsure.','The crop shows two compact dark points, separated vertically and slightly horizontally, beyond the closing parenthesis. Their presence is clear; punctuation role, writer and surface origin remain unassigned.','drawing or diagram',True,True,crop='11',confidence='high',observed_bbox=[1620,1686,1632,1700],components=[{'id':'G03a','source_position':[1628,1690],'shape_confidence':'high'},{'id':'G03b','source_position':[1623,1697],'shape_confidence':'high'}],interpretation_confidence='low')
add('B16','after cancelled Soit, Au … equals','deuxième',r'\uncertain{dernier}',r'\unsure{deuxième|dernier}','The word begins with a small d loop, has extended low middle strokes, a separated high mark and a low humplike ending. Deuxième is the stronger reading, but the compressed middle leaves dernier supported. Au, cancelled Soit, the equals and following comma are readable.','misread word',False,True,crop='12',confidence='medium',qualification='H’s word remains an alternative; no conclusive H error is claimed.')
add('B17','cancelled word after dans la',r'\deleted{\unsure{somme|réunion}}',r'\struck{\ill{}}',r'\deleted{\unsure{somme|réunion}}','The horizontal strike overlaps nearly the whole low letter body. A first upward/returning stroke and several low humps support somme; réunion remains possible through the damaged middle.','readable ink left as \\ill{}',False,True,'retained','13',source='R06',confidence='low',qualification='One whole struck-word placeholder counted against H, with recovered word still qualified.')
add('B18','between borner and sommer','à',':',r'\unsure{:|à}','Two vertically separated small marks are visible: an upper point and a lower open, hooked mark. Colon is primary from the separated form; à remains supported by the lower hook.','misread symbol or index',True,False,crop='14',confidence='medium',qualification='Primary differs from C but C’s à is retained as an alternative. No grammatical repair was used.')
add('B19','word following the borner mark',r'\unsure{sommer}',r'\ill{}','sommer','The initial hooked s, separated low o run, humps, small e loop and terminal r hook are readable in the crop.','readable ink left as \\ill{}',True,True,'resolved','14',source='R07',confidence='high',qualification='One whole live-word placeholder counted against H.')
add('B20','after K1 before ens.',r'\unsure{cet}','cet','cet','Half b shows the opening c-like loop, low e and tall terminal t. The following ens. and comma are separate.','other',True,False,'resolved',bbox=[535,2195,630,2265],source='R08',confidence='high')
add('B21','last display at physical bottom edge',r'\bigcup_{\alpha\in K_1}\widehat{\Sigma}_\alpha^+\cup\widehat{\Sigma}_i^+',r'\bigcup_{\alpha\in K_1}\widehat{\Sigma}_\alpha^+\cup\widehat{\Sigma}_i^+','Current C/H reading retained.','The open round join, alpha, membership, K and lowered 1 are visible. The foot of the index reaches the physical page edge. The two roofs, plus signs and the right i point are visible.',crop='15',confidence='high',boundary_limit='The lower end of the final K1 index is physically cut by the page edge. No continuation is supplied.',count_scope='unchanged reading audit')

source_rows=[]
row_defs=[('R01','line 5, before paired display','ens.','B05','resolved'),('R02','after Par hyp. de récurrence','on a','B09','retained'),('R03','first large union sign',r'\coprod|\bigsqcup','B10','retained'),('R04','under large union, overwritten index','J','B11','retained'),('R05','lead-in above U = …','On a','B13','retained'),('R06','struck word after dans la','somme|réunion','B17','retained'),('R07','after se borner à','sommer','B19','resolved'),('R08','after K1','cet','B20','resolved'),('R09','line 3, before card','avec','B04','retained'),('R10','first U of paired formula','U entrance | cancelled equals U','B06','retained'),('R11','below first display','l’une|l’un','B07','retained'),('R12','brace line1 underneath K0','Sigma_alpha|Sigma_0','B12','retained')]
for n,loc,reading,decision,status in row_defs:
 source_rows.append({'source_row_id':n,'source_order':int(n[1:]),'source_location':loc,'source_reading':reading,'physical_locus_count':1,'decisions':[decision],'status':status})

doubts=[]
def doubt(id,loc,reading,alts,confidence,reason,crop,source=None,**extra):
 q={'id':id,'location':loc,'reading':reading,'alternatives':alts,'confidence':confidence,'reason':reason,'crop':cp[crop]['path'] if crop else None}
 if source:q['C_source_row']=source
 q.update(extra);doubts.append(q)
doubt('Q01','Dém. accent','é',['è'],'low','Short steep accent has unresolved direction.','01')
doubt('Q02','before card','avec',[],'low','Three compressed separated marks do not reveal each letter.','03','R09')
doubt('Q03','first U entrance','U with entrance flourish',['cancelled equals before U'],'medium','Attached runs are clear; their role is unsettled.','04','R10')
doubt('Q04','below first display',"l'une",["l'un"],'medium','The final low return may be a letter ending or a terminal flourish.','05','R11')
doubt('Q05','two traces under word ending','two graphical traces',[],'low','Their local shapes are retained, with unresolved attachment, hand and surface origin.','05',components=['G02a','G02b'])
doubt('Q06','after Par hyp. de récurrence','on a',[],'low','Only a dash, low run and point are clearly separable.','06','R02')
doubt('Q07','first large join',r'\coprod',[r'\bigsqcup'],'medium','Curved interior and extended foot coexist.','07','R03')
doubt('Q08','earlier index under K0','J',[],'low','Earlier loop and upper remnant are obscured by K.','07','R04')
doubt('Q09','brace first line, predecessor lower index',r'\alpha',['0'],'medium','Small earlier loop is crossed by the live K leg.','08','R12')
doubt('Q10','lead-in before U equality','On a',[r'\deleted{O}On a',r'\deleted{On}On a'],'low','Word and overwritten/live-state questions remain at one initial group.','09','R05')
doubt('Q11','later large join',r'\coprod',[r'\bigsqcup'],'medium','This local occurrence was independently inspected; later printed primary follows the recurring-sign convention.','10',printed_qualifier=False,first_qualifier='Q07')
doubt('Q12','far-right detached pair','two dark graphical points',[],'low','Shape confidence high; punctuation role, hand and surface origin unresolved.','11',components=['G03a','G03b'])
doubt('Q13','Au … equals','deuxième',['dernier'],'medium','Compressed middle and high mark do not settle every letter.','12')
doubt('Q14','struck word after dans la','somme',['réunion'],'low','Strike masks much of the letter body.','13','R06')
doubt('Q15','after borner',':',['à'],'medium','Separated upper point and lower hook support both readings.','14')

inventory=[]
def inv(n,kind,pos,words,hand='his hand',**extra):
 e={'sheet_kind':'text','hand':hand,'element':f'019.B.{n:02}','kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes'};e.update(extra);inventory.append(e)
inv(1,'text','top five physical lines','Dém. par récurrence … les ens.')
inv(2,'display','upper third','paired U intersections with Sigma_i plus and minus')
inv(3,'drawing','initial U in paired display','G01: full U and two extra left entrance runs',components=['G01a','G01b','G01c'])
inv(4,'deletion','initial U entrance, alternative state','possible cancelled equals; U-flourish primary',state='uncertain; alternative in reading.tex')
inv(5,'text','below paired display','ont la forme précédente … l’une/l’un des deux.')
inv(6,'drawing','under the ending of l’une/l’un','G02: dark compact point and fainter short lower trace','undetermined hand',components=['G02a','G02b'],role='unresolved',surface_origin='unresolved')
inv(7,'text','above first equality','Par hyp. de récurrence, on a')
inv(8,'display','middle first equality','U_J,i = X setminus footed join of hat Sigma_alpha plus')
inv(9,'deletion','index under first join','earlier J candidate beneath K0')
inv(10,'text','left of brace','où')
inv(11,'display','middle three-line brace','K0 subset J; Sigma membership; hat Sigma = Sigma union E')
inv(12,'deletion','brace first line beneath K0','earlier Sigma_alpha / Sigma_0')
inv(13,'text','below brace','On a donc, with uncertain initial state')
inv(14,'deletion','initial capital in On a donc','possible overwritten O/On; live On a primary',state='uncertain; complete alternatives in reading.tex')
inv(15,'display','lower equality before last prose paragraph','U = U_J,i cap Sigma_i minus = X setminus (…)')
inv(16,'drawing','far right of lower equality','G03: detached upper-right/lower-left pair of dark points','undetermined hand',components=['G03a','G03b'],role='unresolved',surface_origin='unresolved')
inv(17,'deletion','start of last prose paragraph','Soit')
inv(18,'text','lower prose paragraph','Au deuxième/dernier =, dans la … soit K1 cet ens., donc')
inv(19,'deletion','after dans la','somme / réunion')
inv(20,'deletion','after sur les','Sigma')
inv(21,'display','bottom edge','U = X setminus (round union indexed by alpha in K1 …)')
inv(22,'text','bottom-left archive numeral','18, preserved in archive-number comment','undetermined hand')

notation=[
 {'location':'top lines','visible':'Serif I; hooked J; lower-case card; sloped comparison lower rule.','latex':r'\operatorname{card} I, J, \geq'},
 {'location':'paired display and U recurrences','visible':'J with descending return and separate dotted i.','latex':r'U_{J,i}'},
 {'location':'paired display','visible':'Angular Sigma with short low i and high plus or minus.','latex':r'\Sigma_i^+,\Sigma_i^-'},
 {'location':'first and later large join','visible':'Tall sides, round interior, projecting foot; later lower retrace.','latex':r'\unsure{\coprod|\bigsqcup} first; later \coprod','local_decisions':['B10','B14']},
 {'location':'first equality; brace definition; lower equality; prose union; two hatted inequality terms; final two terms','visible':'Nine distinct roof-shaped accents over Sigma.','latex':r'\widehat{\Sigma}','S_row':'SA01-K81-06','S_assessment':'The broad S proposal supplies no locally matched omitted closure bar on this page. All nine observed roofs are already represented in current C and H.'},
 {'location':'brace line2','visible':'Two-legged pi, low zero, parentheses; ordinary upright-looking E and X.','latex':r'\pi_0(X\setminus E_\alpha)'},
 {'location':'brace first line and lower prose','visible':'Open curved inclusion and two independently crossed inclusions.','latex':r'\subset,\not\subset'},
 {'location':'prose union and last display','visible':'Round open join without the long projecting foot of the earlier two forms.','latex':r'\bigcup'},
 {'location':'abbreviations','visible':'Terminal points at Dém., hyp., both ens. occurrences and i.e.; card has no point.','latex':'Dém.; hyp.; ens.; i.e.; card'},
 {'location':'after borner','visible':'Upper point and separated lower hook.','latex':r'\unsure{:|à}'},
]

report={
 'scan':'019','reader':'B','start_utc':'2026-11-20 19:48:24 UTC','end_utc':'2026-11-20 20:01:09 UTC',
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'differences':d,'doubts':doubts,'inventory':inventory,
 'notes':{
  'page_content':'Continuation of a handwritten induction argument. It gives paired intersections, an indexed complement expression, three brace conditions, a second complement expression, restriction of indices to K1, and a final complement expression. The wording and formulas are transcribed as written, with qualified ink readings retained.',
  'authors_own_uncertainty_exact_words':[],
  'title_date_page_counts':'No title, date or manuscript page number observed. Archive numeral 18 at bottom left is recorded in a comment. H page18 corresponds to scan019.',
  'mathematics_led_reading_decisions':'Followed the displayed indices, roofs, plus/minus signs, unions, set differences and crossed inclusions locally. No algebraic repair, theorem reconstruction, conditional theorem or proof check was performed.',
  'H_apparatus':'The two H note macros are editorial explanations. They do not add manuscript words and create no collation rows. H editorial uncertain markers alone create no differences when the primary text is unchanged.',
  'S_row_scope':'SA01-K81-06 spans several scans and explicitly reports no scan viewing. Its proposed examples were not silently transferred. Nine local Sigma roofs were inspected as roofs; current C/H already preserve them. No unobserved closure bar was supplied.',
  'image_processing':'Full source dimensions 1692 by 2362; each half 1692 by 1261. Source crops use full-scan coordinates, x right/y down, without alignment or pixel-difference computation. PIL crop, autocontrast, Lanczos resize to width2800 and UnsharpMask(radius1.1,percent120,threshold3) were used. No rotations.',
  'image_ledger':'Whole once, half a once, half b once, 15 preplanned crops once each; all delivered successfully. No reopenings, retries, OCR, research, compilation, rendering, installs or other-page reads.',
  'graphical_sources':'G01 is a manual complete first-U approximation with three literal paths. G02 has two fills for two lower traces; G03 has two fills for the far-right point pair. Fixed source origins, units and baselines are given in reading.tex. Their source coordinates are not metric/render validation.',
  'boundary_limits':['Crop02 reaches the physical right edge at numeral1; unseen punctuation is not supplied.','Crop15 preserves the whole last display available on the sheet; the lower K1 end meets the physical bottom edge. Its top edge clips part of the previous prose line, which was already read in half b.'],
  'other_surface_observations':'Diffuse gray paper texture without a discrete supported character was not converted into text. G02/G03 retain discrete candidate paths while their surface origin remains unresolved.',
  'structural_verification':'Final structural source checks passed: braces, environments, five display pairs, no physical blank line within a display, allowed collation kinds, 12 source-row mappings, 15 crop references and count consistency. The checker initially had a Python quote error and then treated comment-only lines as blank paragraphs; its own source was corrected. Neither checker issue required a transcription change. No TeX compiler or renderer was invoked.'
 },
 'notation':notation,'check_events':[],'crops':crops,
 'original_C_doubt_rows':source_rows,
 'counts':{'original_C_doubt_rows':12,'original_C_doubt_rows_covered':12,'resolved_C_rows':3,'retained_C_rows':9,'new_and_original_unresolved_local_records':len(doubts),'difference_records':len(d),'diff_C_total':sum(e['diff_C'] for e in d),'diff_C_ink_and_doubt':sum(e['diff_C'] for e in d if e['id']!='B00'),'diff_C_convention_only':1,'diff_H_total':sum(e['diff_H'] for e in d),'source_images_viewed':3,'crops_viewed':15,'graphical_groups':3,'literal_graphical_components':7,'inventory_items':len(inventory)},
 'brief_feedback':['The first-U entrance role cannot be captured solely by an ordinary U or cancelled-equals label. An inline fixed-origin graphical U preserves its three visible runs while retaining the role alternatives.','Two newly isolated tiny-mark clusters retain unresolved attachment or surface origin. Their shape confidence is reported independently from interpretation.','The end of the top line and the index at the bottom display meet physical sheet edges. A further enlargement cannot recover off-sheet content.']
}
(b/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['counts'],ensure_ascii=False))
