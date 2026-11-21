from pathlib import Path
import json,datetime,hashlib,re
D=Path('out/readers/024/C'); P=Path('packets/024')
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
start=D.joinpath('start_utc.txt').read_text().strip()
plans=[
('opening_math','a',[1005,82,1654,230],0,'R01 ring; R02 both alpha-prime indices'),
('initial_word','a',[282,73,592,212],0,'initial Considerons accent and complete word'),
('soit_point','a',[276,205,430,328],0,'extra point above soit'),
('cancelled_on','a',[700,305,1438,417],0,'R04 cancellation; following Considérons acute'),
('relation_insertion','a',[297,392,1132,564],0,'old lemma and raised Relation phrase'),
('definition_left','a',[612,510,1162,650],0,'R05 predecessor, R06 def, point, arrow'),
('tuple','a',[1220,645,1628,794],0,'R07 full tuple and all terminal runs'),
('left_rule','a',[235,755,443,1195],90,'full rule endpoints and detached trace'),
('ens_sommets','a',[312,890,978,1013],0,'R08 complete ens de(s) sommets'),
('aretes_cancel','a',[311,994,1063,1123],0,'R09 accent/punctuation; cancelled Cette relation'),
('le_graphe','a',[1080,942,1506,1108],0,'R16 whole Le/Ce and upper run'),
('le_quon','b',[426,99,1096,264],0,'R17 le; whole reduced qu on a; pale trace'),
('existe','b',[1121,204,1508,316],0,'R10 old word; Il; y a entry'),
('lens','b',[1100,439,1561,570],0,'l ens / l une and adjoining par/de'),
('soient_sigmas','b',[370,632,935,756],0,'R11; S01/S02 complete decorated glyphs'),
('connexes','b',[1095,625,1556,727],0,'R18 whole connexes/conn; comp. point'),
('exactement','b',[426,873,852,979],0,'R12 ending; live underlined un'),
('signed_containment','b',[929,850,1584,978],0,'R13, R14, contenu and all signs/endpoints'),
('barred_u','b',[631,970,981,1098],0,'later barred U sign and complete formula'),
('parenthetical_right','b',[999,939,1651,1188],0,'R15; de =; S04; p/bar gap; final RHS and endpoint'),
('definit','b',[340,1076,721,1195],0,'final definit accent, full f descender, un'),
('final_containment','b',[735,1051,1024,1185],0,'final U_s-minus subset S05 complete')]
crops=[]
for n,(stem,half,box,rot,purpose) in enumerate(plans,1):
 crops.append({'path':f'crop{n:02d}_{stem}.png','source':f'source/SP40_CW_81_scans/J81-03_81_scan024_{half}.jpg','bbox':box,'coordinate_origin':f'supplied half {half}, upper-left; native pixels','rotation':rot,'width':1800 if n==3 else 2300 if n==22 else 2600,'purpose':purpose,'views':1,'boundary_limitation':'none for the selected target; contextual fragments outside target may meet an edge'})
def locus(n):return {'source':crops[n-1]['source'],'coordinates':crops[n-1]['bbox'],'origin':crops[n-1]['coordinate_origin']}
diffs=[]
def diff(id,loc,C,H,reading,evidence,kind='other',dc=False,dh=False,status=None,crop=None,confidence='medium',**extra):
 d={'id':id,'location':loc,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dc,'diff_H':dh,'C_doubt_status':status,'readers_crop':crops[crop-1]['path'] if crop else None,'bbox':locus(crop) if crop else extra.pop('bbox',None),'marked_in_H':bool(H and ('\\ill' in H or '\\uncertain' in H))}
 d.update(extra);diffs.append(d);return d
# All original doubtful-reading row identities remain separate from physical-locus counts.
R={}
def rd(n,*args,**kw):
 ident=f'C024-R{n:02d}'; d=diff(ident,*args,source_row_id=ident,**kw);R.setdefault(ident,[]).append(d['id']);return d
rd(1,'opening Pi exponent',r'\Pi_I^{\unsure{\circ|0}}',r'\Pi_I^0',r'\Pi_I^{\unsure{\circ|0}}','Small closed high loop does not decide circle/zero.',kind='misread symbol or index',dh=True,status='retained',crop=1,alternatives=[r'\Pi_I^0'],physical_cluster='Pi-ring',qualification='H zero survives as the second candidate; primary difference is qualified.')
rd(2,'opening union index',r"\bigcup_{\unsure{\alpha'|i}\in I}",r'\bigcup_{i\in I}',r"\bigcup_{\alpha'\in I}",'Left loop and down-right terminal plus a separate raised prime are visible at this locus.',kind='misread symbol or index',dc=True,dh=True,status='resolved',crop=1,confidence='high',physical_cluster='opening-union-index',sublocus='a')
diff('C024-R02b','index immediately after opening E',r"E_{\alpha'} (table also qualifies this matching mark)",r'E_i',r"E_{\alpha'}",'Independent E-side low loop and high prime were read in the same complete crop.',kind='misread symbol or index',dc=True,dh=True,status='resolved',crop=1,confidence='high',source_row_id='C024-R02',sublocus='b',physical_cluster='opening-E-index');R['C024-R02'].append('C024-R02b')
rd(3,"opening after S l'",r"l'\unsure{ens|ens.}",r"l'ens.","l'ens",'The supplied half shows the complete ens ending followed by blank spacing before des; no detached point.',dc=True,dh=True,status='resolved',confidence='high',bbox={'source':'half a','coordinates':[576,222,832,309],'origin':'supplied half a upper-left'})
rd(4,'struck wording before second Considérons',r'\deleted{\unsure{On a}}',r'\struck{On}',r'\deleted{\unsure{On a|On}}','O is clear; lower fragments and the thick terminal are crossed. The final a has no isolated counter. Both complete cancelled word states remain.',kind='misread word',dh=True,status='retained',crop=4,confidence='low',alternatives=[r'\deleted{On}'],physical_cluster='cancelled-On',source_group='C024-G02',qualification='H On remains a complete alternative.')
rd(5,'overwritten glyph at live (s,i)',r'\deleted{\unsure{U|E}}(s,i)',r'(s,i)',r'\deleted{\unsure{U|E}}(s,i)','Two uprights, lower curved return and multiple diagonals obscure the predecessor. Live opening parenthesis and s are preserved in the same literal group.',kind='omission',dh=True,status='retained',crop=6,confidence='low',alternatives=[r'\deleted{E}(s,i)'],physical_cluster='definition-predecessor',source_group='C024-G04')
rd(6,'label over defining arrow',r'\unsure{def|déf}',r'déf','def','No detached accent appears above the e; f has a separate full descending endpoint.',dc=True,dh=True,status='resolved',crop=6,confidence='high',physical_cluster='definition-arrow',source_group='C024-G05')
rd(7,'complete revised tuple after fait de',r'(S,I\unsure{)\deleted{R})|\deleted{)}{,}R)}',r'(S,I,R)',r'\unsure{(S,I)\deleted{R})|(S,I\deleted{)},R)}','Tall first closer is clean. R carries crossing diagonals. A long lower return reaches the final hooked closer; no separate comma settles the correction.',kind='deletion state (struck given live or live given struck)',dh=True,status='retained',crop=7,confidence='low',alternatives=[r'(S,I\deleted{)},R)'],physical_cluster='tuple',source_group='C024-G06',qualification='Both full C state candidates retained, including each final closer; H live R overlaps the second state but lacks its cancelled predecessor.')
rd(8,'before sommets',r'\unsure{ens des|ens de}',r'ens.\ de',r'\unsure{ens de|ens des}','One low run reaches a d loop and reduced terminal. Extra s remains unresolved; no abbreviation point follows ens.',kind='misread word',dc=True,dh=True,status='retained',crop=9,confidence='low',alternatives=['ens des'],physical_cluster='ens-de-sommets',qualification='H de agrees with primary wording; its abbreviation point is absent.')
rd(9,'whole arêtes word and its accent',r'\unsure{arêtes|arètes|aretes}',r'arêtes',r'\unsure{aretes|arêtes|arètes}','No separate accent can be isolated from the tall t run. Every original whole-word candidate remains, with unaccented primary.',kind='misread word',dc=True,dh=True,status='retained',crop=10,confidence='low',alternatives=['arêtes','arètes'],physical_cluster='aretes',sublocus='word/accent',qualification='H accented word is retained as a qualified alternative.')
diff('C024-R09p','point and closing curve after arêtes',r'.)',r'.',r'.)','A dark baseline point and an independent closing curve with its low return are visible.',kind='omission',dh=True,status='resolved',crop=10,confidence='high',source_row_id='C024-R09',sublocus='endpoint punctuation',physical_cluster='aretes-endpoint');R['C024-R09'].append('C024-R09p')
rd(10,'cancelled word after live Il',r'Il \deleted{\unsure{existe|ex}} y a',r'\struck{il y a} il y a',r'Il \deleted{\unsure{existe|ex}} y a','Live Il is left of the low crossed word and live y a is right of it. Low remnants and a tall hooked terminal do not decide existe/ex.',kind='misread word',dh=True,status='retained',crop=13,confidence='low',alternatives=[r'Il \deleted{ex} y a'],physical_cluster='existe-cluster',source_group='C024-G11')
rd(11,'lower paragraph initial',r'\unsure{Soient|Soit}',r'Soient',r'\unsure{Soient|Soit}','Reduced ending contains a long low run and raised terminal; it does not separate the full nt from the shorter candidate.',status='retained',crop=15,alternatives=['Soit'],physical_cluster='Soient')
rd(12,'before underlined un',r'\unsure{exactement|exactemt}',r'exactement',r'\unsure{exactemt|exactement}','Short compressed middle/ending terminates in a crossed triangular t. The contracted candidate is primary.',kind='abbreviation expanded or spelling modernised',dc=True,dh=True,status='retained',crop=17,alternatives=['exactement'],physical_cluster='exactemt',qualification='H full form remains an alternative.')
rd(13,'first U, sign below s',r'U_{s_{\unsure{+|-}}}',r'U_{s_+}',r'\unsure{U_{s_+}|U_{s_-}}','Dense black lower block has two right lips and no isolated full cross; plus/minus remains open.',status='retained',crop=18,confidence='low',alternatives=[r'U_{s_-}'],physical_cluster='first-U-sign',source_group='C024-U01',contextual_recurrence='Later barred U inspected independently in crop19; separate local entry C024-D28.')
rd(14,'raised sign on Sigma after contenu dans',r'\Sigma_i^{\unsure{+|-}}',r'\Sigma_i^+',r'\unsure{\Sigma_i^-|\Sigma_i^+}','The raised mark is a wide solid horizontal block. Vertical extent is crowded; minus primary and plus alternative preserve the local ink.',kind='misread symbol or index',dc=True,dh=True,status='retained',crop=18,confidence='low',alternatives=[r'\Sigma_i^+'],physical_cluster='S03-raised-sign',source_group='C024-S03',qualification='H plus remains an alternative; no formula repair was made.')
rd(15,'right-edge word immediately before definit',r'\unsure{dé|qui}',r'\ill{}',r'\unsure{de|dé|qui}','Tall connected loop and low returning continuation support de; no detached acute is isolated. Original dé and qui remain as complete candidates.',kind=r'readable ink left as \ill{}',dc=True,dh=True,status='retained',crop=20,confidence='low',alternatives=['dé','qui'],physical_cluster='right-edge-word',H_count_scope='one ill placeholder, one physical word')
rd(16,'word before graphe est un arbre',r'\unsure{Le|Ce}',r'Ce',r'\unsure{Le|Ce}','Square upright body favors L; heavy detached upper zigzag keeps C possible. Whole-word and upper-mark scopes remain separate.',kind='misread word',dh=True,status='retained',crop=11,alternatives=['Ce'],physical_cluster='Le-Ce',source_group='C024-G08',qualification='H Ce is an alternative; upper-run hand is undetermined.')
rd(17,'word before fait',r'\unsure{le|Le}',r'Le',r'\unsure{le|Le}','Short upright and low e are clear; size/case is not fully settled by this local form.',kind='misread word',dh=True,status='retained',crop=12,alternatives=['Le'],physical_cluster='le-fait',qualification='H capital Le remains an alternative.')
rd(18,'after comp.',r'\unsure{connexes}',r'conn.',r'\unsure{connexes|conn}','Three reduced groups do not recover every middle letter; full and shortened candidates remain. comp. has its own point; no point follows the selected word.',kind='misread word',dh=True,status='retained',crop=16,confidence='low',alternatives=['conn'],physical_cluster='connexes',qualification='Shorter alternative has no manuscript point.')
# Additional textual readings and every visible/source-only graphical choice.
diff('C024-D01','first opening word',r'Considérons',r'Considérons',r'\unsure{Considerons|Considérons}','Reduced post-d run has no isolated acute; high upright remains connected. Full accented alternative retained.',kind='misread word',dc=True,dh=True,crop=2,alternatives=['Considérons'],physical_cluster='opening-Considerons')
diff('C024-D02','old underlined heading above definition',r'\deleted{\uline{Lemme} $\forall i\in I$,}',r'\struck{relation $R$ entre} \struck{$\forall i\in I$,}',r'\deleted{\uline{Lemme} $\forall i\in I$,}','Large L and reduced emme are underneath the rising crossing. Their independent lower underline survives.',kind='misread word',dh=True,crop=5,confidence='high',physical_cluster='old-Lemme',source_group='C024-G03')
diff('C024-D03','raised insertion scope and capital',r'\inserted{Relation $R$ entre $S$ et $I$}',r'\add{relation $R$ entre} $S$ et $I$',r'\inserted{Relation $R$ entre $S$ et $I$}','Capital R starts the raised word. S et I continues at the same raised level beyond the old line.',kind='insertion or placement',dh=True,crop=5,confidence='high',physical_cluster='Relation-insertion',source_group='C024-G03')
diff('C024-D04','old/raised lines: literal strike and underline',r'generic deleted/uline wrappers',r'generic struck/add wrappers',r'C024-G03','One rising long strike crosses old Lemme and forall; a separate curved underline lies below Lemme. The source draws each once.',kind='drawing or diagram',dc=True,crop=5,confidence='high',physical_cluster='old-Lemme',source_group='C024-G03',H_count_parent='C024-D02',source_only_choice=True)
diff('C024-D05','above initial soit',r'no separate point',r'no separate point',r'C024-M01','Small diamond-shaped point lies above the initial s, apart from the word i dot.',kind='omission',dc=True,dh=True,crop=3,confidence='high',physical_cluster='point-over-soit',source_group='C024-M01',role='undetermined',hand='undetermined hand',attachment='undetermined',surface_origin='undetermined')
diff('C024-D06','above definition predecessor',r'no separate point',r'no separate point',r'C024-M02','A discrete dark point sits above the overwritten predecessor, separate from its loops.',kind='omission',dc=True,dh=True,crop=6,confidence='high',physical_cluster='point-over-predecessor',source_group='C024-M02',role='undetermined',hand='undetermined hand',attachment='undetermined',surface_origin='undetermined')
diff('C024-D07','definition arrow hooked returns',r'\Longleftrightarrow',r'\Longleftrightarrow',r'C024-G05','Two shafts are joined by the left curved return; right terminal is hooked. Literal geometry is preserved beside the resolved def label.',kind='drawing or diagram',dc=True,dh=True,crop=6,confidence='high',physical_cluster='definition-arrow',source_group='C024-G05',source_only_choice=True)
diff('C024-D08','tuple crossing geometry',r'tuple alternatives typeset only',r'(S,I,R)',r'C024-G06','Crossing diagonals and the long return into the final closer are literal paths; no second generic crossing is added.',kind='drawing or diagram',dc=True,crop=7,physical_cluster='tuple',source_group='C024-G06',H_count_parent='C024-R07',source_only_choice=True)
diff('C024-D09','lemma left rule',r'one straight tabular rule',r'no rule',r'C024-G07 rule paths','Rule begins with a hooked retrace, bows slightly, and ends below the last lemma line. Both endpoints are in the crop.',kind='drawing or diagram',dc=True,dh=True,crop=8,confidence='high',physical_cluster='lemma-rule',source_group='C024-G07')
diff('C024-D10','detached mark left of lemma rule',r'absent',r'absent',r'C024-M03','One longer oblique run and one separated short pale terminal survive.',kind='omission',dc=True,dh=True,crop=8,physical_cluster='left-rule-trace',source_group='C024-M03',role='undetermined',hand='undetermined hand',attachment='undetermined',surface_origin='undetermined')
diff('C024-D11','upper run of Le/Ce',r'ordinary qualified word',r'Ce',r'C024-G08','Literal main body and detached zigzag are retained once inside the full Le/Ce qualification.',kind='drawing or diagram',dc=True,crop=11,physical_cluster='Le-Ce',source_group='C024-G08',H_count_parent='C024-R16',source_only_choice=True,role='C head / independent upper trace unresolved',hand='undetermined hand for upper run')
diff('C024-D12','after underlined arbre',r'no point',r'arbre.','arbre; no following manuscript point','Half a shows the full underline ending and blank area to the right.',kind='text not on the page',dh=True,confidence='high',bbox={'source':'half a','coordinates':[624,1097,888,1202],'origin':'supplied half a upper-left'},physical_cluster='arbre-endpoint')
diff('C024-D13','complete reduced phrase after le fait',r"qu'on a",r"c'est",r"\unsure{qu'on a}",'Long q descender and reduced low on run remain; final a candidate is a solid mark without a counter. Whole phrase and final a/unassigned-point scope stay open.',kind='misread word',dc=True,dh=True,crop=12,confidence='low',alternatives=["qu'on followed by an unassigned point"],physical_cluster='quon-a',source_group='C024-G10',hand='main phrase his hand; final mark attribution undetermined')
diff('C024-D14','below-left of fait',r'absent',r'absent',r'C024-M04 trace','Pale bent run has a visible lower turn and short left continuation, separate from the dark f.',kind='omission',dc=True,dh=True,crop=12,confidence='low',physical_cluster='fait-pale-trace',source_group='C024-M04',role='undetermined',hand='undetermined hand',attachment='undetermined',surface_origin='undetermined')
diff('C024-D15','live Il before cancellation',r'Il',r'il',r'Il','Initial I has a detached upper cap and lower body, followed by a separate looped l.',kind='misread word',dh=True,crop=13,confidence='high',physical_cluster='live-Il',source_group='C024-G11')
diff('C024-D16','cancelled existe/ex geometry',r'generic deleted word',r'generic struck il y a',r'C024-G11 old-word paths','Low word remnants, long horizontal crossing, lower spur and raised hooked terminal are preserved as one cancelled cluster.',kind='drawing or diagram',dc=True,crop=13,physical_cluster='existe-cluster',source_group='C024-G11',H_count_parent='C024-R10',source_only_choice=True)
diff('C024-D17','pale entry toward live a after y',r'plain y a',r'plain y a',r'C024-G11 pale entry and live a','A pale oblique segment leads toward the dark a beginning. It is drawn once with the adjoining a, with unresolved entry/correction role.',kind='drawing or diagram',dc=True,dh=True,crop=13,physical_cluster='y-a-entry',source_group='C024-G11',role='entry / other trace unresolved',hand='undetermined hand for pale stroke')
diff('C024-D18','after caractérisé par',r"l'ens",r"l'une",r"\unsure{l'ens|l'une}",'Low shoulders and long ending favor ens but do not isolate all letters. Both complete local words retained.',kind='misread word',dc=True,dh=True,crop=14,confidence='low',alternatives=["l'une"],physical_cluster='lens-lune',qualification='H survives as alternative.')
diff('C024-D19','after se précise',r'en :',r'ainsi :',r'en :','Two reduced groups form en before the two-point colon; the full half preserves the complete phrase.',kind='misread word',dh=True,confidence='high',bbox={'source':'half b','coordinates':[941,730,1290,844],'origin':'supplied half b upper-left'},physical_cluster='precise-en')
diff('C024-D20','live underlined un before first signed U',r'\uline{un}',r'\struck{une} une',r'\uline{un}','Single live un has one separate underline; no readable cancelled une lies at this locus.',kind='deletion state (struck given live or live given struck)',dh=True,crop=17,confidence='high',physical_cluster='underlined-un',local_details=['live un/une wording','H supplied cancelled une','single underline'])
diff('C024-D21','after first U_s sign',r'contenu',r'contenue',r'contenu','The full reduced word ends before dans without an added final e.',kind='misread word',dh=True,crop=18,confidence='high',physical_cluster='contenu')
diff('C024-D22','before first barred U',r'tel que',r'telle que',r'tel que','Short word ends in its tall l before que; no added le follows.',kind='misread word',dh=True,confidence='high',bbox={'source':'half b','coordinates':[335,988,572,1107],'origin':'supplied half b upper-left'},physical_cluster='first-tel')
diff('C024-D23','parenthetical de =',r'de $=$',r'de même',r'de $=$','Two separate horizontal strokes occupy the word position after de.',kind='abbreviation expanded or spelling modernised',dh=True,crop=20,confidence='high',physical_cluster='de-equals')
diff('C024-D24','final definit',r'définit',r'définit',r'definit','No separate acute occurs over the first e; raised marks align with the two i positions. Full f descender is within crop21.',kind='abbreviation expanded or spelling modernised',dc=True,dh=True,crop=21,confidence='high',physical_cluster='definit')
diff('C024-D25','un after definit',r'un',r'une',r'un','Low written un has no further e before the next U.',kind='misread word',dh=True,crop=21,confidence='high',physical_cluster='final-un')
diff('C024-D26','final tel que',r'tel que',r'telle que',r'tel que','The full final word has its t/e/l runs, ending before que without an additional le.',kind='misread word',dh=True,crop=20,confidence='high',physical_cluster='final-tel')
for sid,n,ev,dc,dh in [
 ('S01',15,'Detached bent head and interrupted pale upper-arm start; clear i dot and plus. Head/retrace or independent upper-run role stays qualified.',True,True),
 ('S02',15,'Detached upper head, separate thin upper arm, hooked foot, short dotless index and minus. Index i is locally uncertain.',True,True),
 ('S03',18,'Head joins the body; short dotless index remains locally recorded; solid raised sign has its own R14 alternatives.',False,False),
 ('S04',20,'Upper run visibly joins body; short dotless index retains its local i qualification; raised minus is firm.',False,False),
 ('S05',22,'Upper run visibly joins body; lower i has point and separate upright; raised minus is firm.',False,False)]:
 diff('C024-D27'+sid[-2:],'complete local glyph '+sid,r'ordinary \Sigma_i sign',r'ordinary \Sigma_i sign','C024-'+sid,ev,kind='drawing or diagram',dc=dc,dh=dh,crop=n,physical_cluster=sid,source_group='C024-'+sid,source_only_choice=True,recurring_print_rule='S01 first prints detached-head role; S02 first prints short-index uncertainty; all local records persist.')
diff('C024-D28','later sign under first barred U',r'\overline{U_{s_+}}',r'\overline{U_{s_+}}',r'\overline{U_{s_+}}; local alternative \overline{U_{s_-}}','Dense left block, two right lips and short low protrusion remain literal. Bar itself is firm. Later sign doubt is retained in source comment and report under first-occurrence convention.',kind='drawing or diagram',dc=True,dh=True,crop=19,confidence='low',alternatives=[r'\overline{U_{s_-}}'],physical_cluster='later-U-sign',source_group='C024-U02',source_row_context='C024-R13 contextual recurrence; not a second original doubt row',qualification='Same primary as H; H count concerns literal irregular geometry, not an editorial doubt marker alone.')
diff('C024-D29','tiny marks near first U low sign',r'absent',r'absent',r'C024-M06','One tiny pale tick and separate point are visible above-right of the low block, separate from the main s tip.',kind='omission',dc=True,dh=True,crop=18,confidence='low',physical_cluster='first-U-small-traces',source_group='C024-M06',role='undetermined',hand='undetermined hand',attachment='undetermined',surface_origin='undetermined')
diff('C024-D30','E_i in first signed nonemptiness formula',r'E_i',r'E_i',r'C024-E01','Detached upper arm and long middle/right return toward the dotted index are drawn literally. This source choice preserves the same E_i reading.',kind='other',crop=19,confidence='high',physical_cluster='signed-E-i',source_group='C024-E01',source_only_choice=True)
diff('C024-D31','archive numeral and source wrappers',r'\scanpage{24}; archive comment 23',r'\page{23}',r'\scanpage{24}; % archive sheet number: 23','Archive 23 is visible at the lower-left; supplied page-mapping metadata identifies H page 23. Administrative wrappers and comment carry no lexical correction count.',kind='other',confidence='high',bbox={'source':'half b','coordinates':[20,1203,92,1250],'origin':'supplied half b upper-left'},physical_cluster='archive-23',source_only_choice=True)
# Every source-only cancellation choice is separately disclosed, even when the qualified reading is unchanged.
diff('C024-D32','cancelled On a/On literal geometry',r'generic deleted word',r'generic struck On',r'C024-G02','Literal O, low remnants, long crossing, two lower ticks and swollen terminal preserve all selected components.',kind='drawing or diagram',dc=True,crop=4,physical_cluster='cancelled-On',source_group='C024-G02',H_count_parent='C024-R04',source_only_choice=True)
diff('C024-D33','definition predecessor literal geometry',r'generic deleted U/E followed by (s',r'(s',r'C024-G04','Two upper loop remnants, uprights, diagonals and the live opening parenthesis/s are retained in one group. Upper point is separately M02.',kind='drawing or diagram',dc=True,crop=6,physical_cluster='definition-predecessor',source_group='C024-G04',H_count_parent='C024-R05',source_only_choice=True)
diff('C024-D34','first U low-sign literal geometry',r'U_{s_{\unsure{+|-}}}',r'U_{s_+}',r'C024-U01','The irregular solid sign is preserved literally rather than only as a typographic plus/minus candidate. Its two tiny neighboring marks remain M06.',kind='drawing or diagram',dc=True,dh=True,crop=18,physical_cluster='first-U-sign',source_group='C024-U01',source_only_choice=True,qualification='H primary plus is retained; geometry, not editorial qualifier alone, is counted.')
# Complete public readings for every decorated Sigma and every independent component scope.
for d in diffs:
 if d['id'].startswith('C024-D27'):
  sid=d['source_group']; suffix=sid[-3:]
  full=r'\Sigma_i^+' if suffix=='S01' else r'\Sigma_i^-'
  d['reading']=full
  d['local_components']={'head':('detached; head/retrace or independent upper-run role unresolved' if suffix in ['S01','S02'] else 'joined to body, resolved'),'index':('dotted i, resolved' if suffix in ['S01','S05'] else 'short dotless hooked i, locally qualified'),'raised_sign':('plus, resolved' if suffix=='S01' else 'minus primary, plus retained' if suffix=='S03' else 'minus, resolved')}
  if suffix in ['S01','S02']:
   d['alternatives']=[full+' with detached upper run retained as head/retrace',full+' with detached upper run retained as an independent mark']
   d['hand_scope']={'body_and_index':'his hand','detached_upper_run':'undetermined hand'}
  elif suffix=='S03':d['alternatives']=[r'\Sigma_i^+']
  d['qualification']='Complete decorations remain with this glyph; local component qualifications are not transferred between loci.'

groupmeta=json.loads(D.joinpath('group_metadata.json').read_text())
for d in diffs:
 gid=d.get('source_group')
 if gid in groupmeta:
  g=groupmeta[gid]
  d['complete_group_reading']=g['reading']
  d['complete_group_alternatives']=g.get('alternatives',[])
  d['complete_group_states']=g.get('complete_states',[])
  d['group_owned_words_and_marks']=g['owns']
  d['group_qualification']=g['qualification']
  if d['reading'].startswith('C024-'):d['reading']=g['reading']

# Map original rows exactly, including compound and contextual scopes.
source_rows=[]; in_d=False
for ln,line in enumerate(P.joinpath('C_doubts.txt').read_text().splitlines(),1):
 if line.startswith('## Doubtful'):in_d=True
 if in_d and line.startswith('| 24 |'):
  idx=len(source_rows)+1;rid=f'C024-R{idx:02d}'
  source_rows.append({'id':rid,'source_path':'packets/024/C_doubts.txt','source_line':ln,'literal_source_row':line,'local_entries':R[rid],'overall_status':'resolved' if idx in [2,3,6] else 'retained','scope_note':('Both opening index loci remain one original row.' if idx==2 else 'Word/accent retained; separate endpoint punctuation resolved under same source row.' if idx==9 else 'Original first sign plus contextual later barred occurrence mapped to D28; source row counted once.' if idx==13 else 'Original row scope preserved.')})
# Inventory: whole regions and their components in page order.
inv=[]
def item(id,kind,pos,words,hand='his hand',**kw):
 d={'sheet_kind':'text','hand':hand,'element':id,'kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes'};d.update(kw);inv.append(d)
item('024.C.01','text','opening through notées U_s','Considerons/Considérons la partition … l\'ens des classes',source_groups=['C024-M01'])
item('024.C.02','drawing','above soit','one detached point',hand='undetermined hand',source_group='C024-M01',role='undetermined')
item('024.C.03','deletion','before second Considérons','cancelled On a / On',source_group='C024-G02')
item('024.C.04','text','after cancellation','Considérons la')
item('024.C.05','insertion','over old lemma line','Relation R entre S et I',source_group='C024-G03')
item('024.C.06','deletion','old line above defining relation','underlined Lemme, forall i in I comma',source_group='C024-G03')
item('024.C.07','drawing','old lemma line','rising cancellation and separate underline',source_group='C024-G03')
item('024.C.08','display','definition','cancelled U/E; (s,i) in R, def double arrow, barred U_s cap E_i nonempty',source_groups=['C024-G04','C024-G05'])
item('024.C.09','deletion','definition onset','U/E predecessor beside live opening parenthesis and s',source_group='C024-G04')
item('024.C.10','drawing','above definition predecessor','small detached point',hand='undetermined hand',source_group='C024-M02',role='undetermined')
item('024.C.11','text','arrow label','def',source_group='C024-G05')
item('024.C.12','text','lemma heading','underlined Lemme Cette relation fait de')
item('024.C.13','deletion','lemma tuple','complete old/live tuple states',source_group='C024-G06')
item('024.C.14','text','ruled lemma block','un graphe strict … ens de/des … aretes/arêtes/arètes.) … Le/Ce graphe est un arbre',source_group='C024-G07')
item('024.C.15','drawing','left of lemma block','hooked long rule',source_group='C024-G07')
item('024.C.16','drawing','left of rule','oblique run and separated pale terminal',hand='undetermined hand',source_group='C024-M03',role='undetermined')
item('024.C.17','deletion','before Le/Ce graphe','Cette relation',source_group='C024-G07')
item('024.C.18','text','word before graphe','complete Le/Ce glyph',source_group='C024-G08')
item('024.C.19','drawing','upper part of Le/Ce','detached upper zigzag',hand='undetermined hand',source_group='C024-G08',role='C-head / independent upper trace unresolved')
item('024.C.20','text','lemma end','underlining of arbre',source_group='C024-G07')
item('024.C.21','text','explanatory paragraph','le/Le fait qu\'on a … a) … b) …')
item('024.C.22','drawing','below-left of fait','pale bent trace',hand='undetermined hand',source_group='C024-M04',role='undetermined')
item('024.C.23','text','after le fait','complete reduced qu\'on a / qu\'on with unassigned point',source_group='C024-G10')
item('024.C.24','drawing','end of qu\'on a','solid point, a / independent mark',hand='undetermined hand',source_group='C024-G10',role='unresolved',component_of='024.C.23')
item('024.C.25','text','after forall i in I','live Il y a',source_group='C024-G11')
item('024.C.26','deletion','between Il and y a','existe / ex',source_group='C024-G11')
item('024.C.27','drawing','toward final a after y','pale oblique entry',hand='undetermined hand',source_group='C024-G11',role='entry / other trace unresolved')
item('024.C.28','text','b) wording','par l\'ens/l\'une de ces deux U_s')
item('024.C.29','text','last paragraph','Soient/Soit … comp. connexes/conn … se précise en')
item('024.C.30','text','initial signed Sigma pair','S01 complete Sigma_i-plus',source_group='C024-S01')
item('024.C.31','text','initial signed Sigma pair','S02 complete Sigma_i-minus',source_group='C024-S02')
item('024.C.32','text','before first U','exactemt/exactement; one live underlined un')
item('024.C.33','text','first U','U_s with complete plus/minus sign candidates',source_group='C024-U01')
item('024.C.34','drawing','near first U low sign','tiny tick and point',hand='undetermined hand',source_group='C024-M06',role='undetermined')
item('024.C.35','text','after contenu dans','S03 complete Sigma_i-minus/plus',source_group='C024-S03')
item('024.C.36','text','after first tel que','barred U_s-plus/minus cap E_i nonempty',source_groups=['C024-U02','C024-E01'])
item('024.C.37','text','parenthetical opening','et de = pour S04 comma',source_group='C024-S04')
item('024.C.38','text','right edge before final line','de/dé/qui')
item('024.C.39','text','final line initial','definit un')
item('024.C.40','text','final containment','U_s-minus subset S05 Sigma_i-minus',source_group='C024-S05')
item('024.C.41','text','final RHS through endpoint','tel que barred U_s-minus cap E_i nonempty, closing parenthesis and comma')
item('024.C.42','text','lower-left archive corner','23 recorded only in comment',hand='undetermined hand')
# Interleave independently attributed upper runs with their parent glyph regions.
for parent_id,new_id,group_id in [('024.C.30','024.C.30a','C024-S01'),('024.C.31','024.C.31a','C024-S02')]:
 at=next(i for i,x in enumerate(inv) if x['element']==parent_id)+1
 inv.insert(at,{'sheet_kind':'text','hand':'undetermined hand','element':new_id,'kind':'drawing','position':'detached upper run of '+group_id,'first_words_or_objects':'short head/retrace or independent upper run','transcribed':'yes','source_group':group_id,'role':'head/retrace or independent mark unresolved','component_of':parent_id})
coverage={'024.01':['024.C.01','024.C.04'],'024.02':['024.C.03'],'024.03':['024.C.06','024.C.07'],'024.04':['024.C.05'],'024.05':['024.C.08','024.C.11'],'024.06':['024.C.09','024.C.10'],'024.07':['024.C.12','024.C.14','024.C.15','024.C.16','024.C.18','024.C.19','024.C.20'],'024.08':['024.C.13'],'024.09':['024.C.17'],'024.10':['024.C.21','024.C.22','024.C.23','024.C.24','024.C.25','024.C.27','024.C.28'],'024.11':['024.C.26'],'024.12':['024.C.29','024.C.30','024.C.30a','024.C.31','024.C.31a','024.C.32','024.C.33','024.C.34','024.C.35','024.C.36','024.C.37','024.C.38','024.C.39','024.C.40','024.C.41']}
notation=[
 {'location':'opening','reading':r'\Pi_I^{\unsure{\circ|0}}','evidence':'high small loop; circle/zero unresolved'},
 {'location':'opening union and E','reading':r"\alpha' at both local indices",'evidence':'looped low alpha with high separate prime, crop01'},
 {'location':'opening and lemma','reading':'ens; later ens.','evidence':'initial no point; lemma final ens. has point; ens de/des remains qualified'},
 {'location':'definition','reading':'def','evidence':'no acute; cropped arrow label'},
 {'location':'definition and explanation','reading':r'\overline{U_s}\cap E_i\ne\varnothing','evidence':'bars, ordinary low s/i, intersection arch, crossed equals and slashed oval each read from the half'},
 {'location':'five Sigmas','reading':['C024-S01','C024-S02','C024-S03','C024-S04','C024-S05'],'evidence':'two detached heads, three locally joined heads; all index/raised signs individually recorded'},
 {'location':'S02/S03/S04 indices','reading':'short dotless hooked index, primary i','evidence':'local i uncertainty retained; S02 prints first qualifier, later reports retain scope'},
 {'location':'lower U signs','reading':[r'U_{s_+}|U_{s_-}',r'\overline{U_{s_+}}|\overline{U_{s_-}}'],'evidence':'separately drawn solid blocks; no transfer of plus certainty from another term'},
 {'location':'S03 raised sign','reading':[r'\Sigma_i^-',r'\Sigma_i^+'],'evidence':'horizontal solid block; minus primary, plus retained'},
 {'location':'parenthetical','reading':r'de $=$','evidence':'two literal horizontal runs; no verbal expansion'},
 {'location':'final line','reading':'definit; un; tel','evidence':'local absent first-e acute and masculine endings retained'},
 {'location':'abbreviations','reading':['ens','ens.','comp.','exactemt|exactement','connexes|conn'],'evidence':'local points and full alternatives retained; no expansion inside transcription'}]
doubts=[]
for d in diffs:
 if d.get('C_doubt_status')=='retained' or d.get('alternatives') or d['id'] in ['C024-D05','C024-D06','C024-D10','C024-D14','C024-D17','C024-D29','C024-D2701','C024-D2702','C024-D2703','C024-D2704']:
  doubts.append({'id':d['id'],'source_row_id':d.get('source_row_id'),'location':d['location'],'reading':d['reading'],'alternatives':d.get('alternatives',[]),'confidence':d['confidence'],'reason':d['evidence'],'crop':d['readers_crop'],'source_group':d.get('source_group'),'qualification':d.get('qualification'),'hand':d.get('hand'),'role':d.get('role')})
report={'scan':24,'reader':'C','start_utc':start,'end_utc':None,'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,'differences':diffs,'doubts':doubts,'inventory':inv,'C_inventory_coverage':coverage,'C_source_doubts':source_rows,'notes':{
 'page_content':"The sheet introduces the partition Pi_I with a circle/zero exponent, names classes U_s, and writes the relation involving the nonempty intersection of barred U_s and E_i. Its underlined Lemme calls the resulting graph an arbre. The author then writes that a) exactly two U_s meet E_i in the displayed sense and b) i is characterized by the l'ens/l'une reading of those two U_s. The final paragraph writes a signed-component claim using one U_s; the crowded sign after contenu dans retains minus/plus readings. These are attributed manuscript assertions, not proof checks.",
 'authors_own_uncertainty':'No explicit verbal qualification such as à vérifier and no manuscript question mark was read on this sheet. The retained question markers are editorial reading qualifications.',
 'title_date_page_counts':'Underlined Lemme is the local label. No date, title sheet, or written total page count is present. Archive numeral 23 is recorded only as a comment, with undetermined hand.',
 'mathematics_led_reading_decisions':'No mathematical inference was used to supply a glyph or repair a formula. Each sign, bar and index came from its own half/crop. No mathematical computation or proof check was performed.'},
 'notation':notation,'check_events':[],'crops':crops,'brief_feedback':[
 'The second U-sign occurrence is contextual in original R13 but visually needs its own local qualification; it is recorded separately without creating another original source row.',
 'Original R09 combines whole-word accent and punctuation; its word doubt is retained while endpoint point/closer presence is resolved under the same identity.',
 'Solid reduced marks require a complete word/formula group and a separate role/hand scope. Literal groups retain these without duplicating their adjoining words.',
 'Native supplied-half coordinates are used throughout. No full-scan offset, curve-extrema, image-difference, alignment, or metric computation was performed.'
 ],'provenance':{
 'brief_path':'out/briefs/brief_v22_scan024.md','brief_sha256':'5f3f3b2bb77e2a76700ae767a85d3c9152a1f8dc2448b1adf9648d300963e474',
 'packet_reading':'Recorded UTC first. Initial combined text output was truncated; every required document was subsequently read completely in bounded outputs. C_notes is empty. No other page image or reader material was read.',
 'viewing':'One whole, each half once, 22 distinct crops once. 25 successful image deliveries, zero failed/unseen deliveries, zero successful reopens. See view_audit.json for actual event times.',
 'pause':'Paused file writes after half b at root checkpoint request and resumed only after the raw snapshot completion message; first crop was still unviewed at pause.',
 'geometry':'All literal paths are manual visual approximations with declared local pt units, fixed origins, base-west nodes, and no metric or rendered validation. PIL cropping/enlargement/autocontrast/sharpening only; no OCR or image comparison.',
 'source_checks':'Structural-only checks of delimiters, commands, references and agreement are recorded by finalize.py. No compilation, rendering, installation, external research or internet use.',
 'independence':'No delegation, no other-reader files, no root decisions, no other-page images.',
 'editorial_separators':'Pipes in unsure candidates and invisible annotations are editorial alternatives. Their presence does not supply manuscript punctuation.',
 'source_only_choices':'All literal group bodies and complete candidate/word boundaries are in source_map.json. D04/D07/D08/D11/D16/D27*/D30/D31/D32/D33/D34 explicitly disclose source-level choices.'
 },'counts':{'original_C_doubt_rows':18,'original_C_rows_resolved':3,'original_C_rows_retained':15,'C_row09_local_punctuation_resolved_with_word_retained':True,'inventory_elements':len(inv),'differences_records':len(diffs),'raw_diff_C_true':sum(x['diff_C'] for x in diffs),'raw_diff_H_true':sum(x['diff_H'] for x in diffs),'images_success':25,'whole':1,'halves':2,'crops':22,'failed_unseen':0,'reopens':0}}
# Input hashes anchor the exact witnesses and conventions.
inputs=['out/briefs/brief_v22_scan024.md']+[str(P/x) for x in ['C.tex','H.tex','metadata.json','C_doubts.txt','C_notes.txt','notation.md','C_inventory.json']]+['source/SP40_CW_81_witnesses/codex/J81-03/PREAMBLE.tex','source/SP40_CW_81_witnesses/codex/J81-03/PROMPT.md']
report['provenance']['input_sha256']={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in inputs}
D.joinpath('report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Report written:',len(diffs),'difference/source-choice records;',len(inv),'inventory elements;',len(source_rows),'original C rows')
