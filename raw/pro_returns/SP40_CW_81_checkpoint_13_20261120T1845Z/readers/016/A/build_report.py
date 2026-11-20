from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/016/A')
manifest=json.loads((root/'crop_manifest.json').read_text())
rows=[]
def row(id,location,C,H,reading,evidence,confidence,kind,diff_C,diff_H,status=None,crop=None,bbox=None,source_row=None,**extra):
 d=dict(id=id,location=location,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,diff_C=diff_C,diff_H=diff_H,C_doubt_status=status,readers_crop=crop,bbox=bbox)
 if source_row: d['C_doubt_source_row']=source_row
 d.update(extra);rows.append(d)
row('A016-D01','Opening union, second Sigma subscript',r'\Sigma_{\deleted{\unsure{2}}1}^+',r'\Sigma_1^+',r'\Sigma_{\deleted{\unsure{2}}1}^+','The live 1 has a heavy downstroke and foot. A dark hooked remnant lies behind its upper-left side; the predecessor remains only a 2 candidate.','low','omission',False,True,'retained','crop01_opening.png',[845,86,923,158],'D01')
row('A016-D02','Opening line, word cluster immediately before un ouvert',r'\deleted{\unsure{sera|sont}} est','serait',r'\deleted{\unsure{sera|sont}} est','A low initial curve, looped middle and dark tall final crossing form an overwritten cluster. The live est is readable; the surviving predecessor strokes do not settle sera against sont. H records the cluster as one live word.','low','deletion state (struck given live or live given struck)',False,True,'retained','crop01_opening.png',[974,97,1079,145],'D02',qualification='The cancelled predecessor remains qualified; the H difference is not a conclusively recovered old-word spelling.')
row('A016-D03','Far right of opening line',r'\unsure{connexe}','connexe','connexe','Initial open c and small o are followed by two low joined humps and the compact crossed/looped ending. The whole word is visible before the right edge.','medium','other',True,False,'resolved','crop02_right_top.png',[1456,113,1669,151],'D03')
row('A016-D04a','Raised de X/E2 insertion at right edge, separator',r'X\unsure{/|\setminus}E_{\unsure{2}}',r'X\setminus E_2',r'X\unsure{/|\setminus}E_{\unsure{2}}','The stroke after X is steep and slightly right-rising. Its short extent does not settle slash against setminus; slash remains first.','low','misread symbol or index',False,True,'retained','crop02_right_top.png',[1598,176,1641,220],'D04',qualification='H setminus survives as the explicit alternative; this is a qualified primary-candidate difference.')
row('A016-D04b','Same right insertion, E subscript',r'E_{\unsure{2}}',r'E_2',r'E_{\unsure{2}}','A low curved beginning of the subscript is visible, with its continuation meeting the page/image edge. The candidate 2 remains qualified.','low','other',False,False,'retained','crop02_right_top.png',[1640,184,1685,228],'D04',qualification='Same primary candidate as H; uncertainty alone supplies no H correction count.')
row('A016-D05','Opening third line, cancelled word after donc',r"\deleted{\unsure{c'est}}",r'\struck{\ill{}}',r"\deleted{\unsure{c'est}}",'A detached upright apostrophe, a small loop and the tall crossed t survive above the horizontal strike. The initial and central portions remain substantially covered.','low',r'readable ink left as \ill{}',False,True,'retained','crop03_line3.png',[420,281,585,327],'D05',qualification='The return supplies a qualified candidate, not an unqualified recovery of the whole cancelled word.')
row('A016-D06','Opening conclusion, separate fourth line',r'\unsure{cqfd|qfd}','cqfd','cqfd','Half a shows the small initial c curve to the left of the q stem and descender, followed by tall f and final d.','high','other',True,False,'resolved',None,[239,377,407,527],'D06',image_evidence='Half a, full-origin (0,0), bbox as given.')
row('A016-D07a','First partition, first Sigma',r'\deleted{\unsure{E}}\Sigma_1^+',r'\Sigma_1^+',r'\deleted{\unsure{E}}\Sigma_1^+','A thinner near-upright runs from the upper-left to the lower bar beneath the dark Sigma diagonals. A complete independent middle arm is not isolated.','low','omission',False,True,'retained','crop04_partition1.png',[645,607,704,666],'D07')
row('A016-D07b','Five-term partition, central Sigma12',r'\deleted{\unsure{E}}\Sigma_{12}',r'\Sigma_{12}',r'\deleted{E}\Sigma_{12}','The crop exposes a left upright and a short horizontal middle arm below the upper Sigma diagonal, together with the upper and lower arms. The predecessor E is recoverable here.','high','omission',True,True,'resolved','crop05_partition5.png',[1009,888,1076,940],'D07')
row('A016-D07c','Lower hypothesis, letter under first overbar',r'\overline{\deleted{\unsure{E}}\Sigma_{12}}',r'\overline{\Sigma_{12}}',r'\overline{\deleted{\unsure{E}}\Sigma_{12}}','The upper and lower horizontal runs are retraced, and a short crowded left remnant survives. The predecessor cannot be recovered independently as a complete E.','low','omission',False,True,'retained','crop07_lower_overwrites.png',[1032,2018,1156,2089],'D07')
row('A016-D07d','Lower hypothesis, predecessor beneath E1 after intersection',r'\deleted{\unsure{\Sigma}}E_1',r'E_1',r'\deleted{\unsure{\Sigma}}E_1','A thin upper diagonal survives inside the E. Its lower return is crowded into the live middle arm and left stem, leaving Sigma a qualified predecessor.','low','omission',False,True,'retained','crop07_lower_overwrites.png',[1226,2032,1296,2088],'D07')
row('A016-D08','Initial of Dans',r'\deleted{\unsure{O}}Dans','Dans',r'\deleted{\unsure{O}}Dans','Several closed or nearly closed loops occupy the initial D; a prior rounded O remains supported, but its contour is not separable throughout.','low','omission',False,True,'retained','crop06_dans.png',[276,1215,382,1300],'D08')
row('A016-D09','Raised replacement above cancelled alors, second word',r'\inserted{\unsure{en|on} \unsure{conclurait}}',r'\add{en considérant}',r'\inserted{en conclurait}','The word has an initial c/o group, a low connected middle, one tall looped l, and a final a/i/t-like run with a clear tall terminal t. The visible word is conclurait.','high','misread word',True,True,'resolved','crop08_conclurait.png',[462,2119,798,2168],'D09')
row('A016-D10a','Small sign immediately after égale',r'\unsure{à|:}','à',r'\unsure{:|à}','Two separate dark points are vertically aligned. No clear lower letter loop is isolated. Colon is placed first, with the contracted à candidate retained.','low','misread symbol or index',True,True,'retained','crop03_line3.png',[820,301,837,329],'D10',qualification='H à remains an explicit alternative; candidate order is changed without claiming a settled character.')
row('A016-D10b','Opening third line, connective before final inclusion',r"\unsure{donc|d'où}",'donc','donc','The initial looped d is followed by a continuous low on/c run. There is no isolated raised apostrophe in the gap.','medium','other',True,False,'resolved','crop03_line3.png',[1110,302,1237,342],'D10')
row('A016-D11','Raised replacement above alors, first word',r'\unsure{en|on}','en','en','The initial letter is an open low e-shaped trough, joined to a low n shoulder; no closed o loop is visible.','medium','other',True,False,'resolved','crop08_conclurait.png',[326,2142,398,2167],'D11')
row('A016-D12a','First crowded join under the final long overbar',r'\deleted{\unsure{\amalg}}\unsure{\cup|\amalg}',r'\sqcup',r'\unsure{\deleted{\amalg}\cup|\amalg}','Two upright strokes and an extended transverse lower rule coexist with a rounded bowl below it. The square-join strokes are clear; their overwritten state and the final cup/square-join reading remain unresolved.','low','deletion state (struck given live or live given struck)',True,True,'retained','crop09_lower_joins.png',[755,2254,805,2293],'D12',qualification='The combined alternative qualifies the chronology/state as well as the final operator. H square join survives as the live alternative.',glyph_status='Square-join component resolved; final form and predecessor state retained as doubtful.')
row('A016-D12b','Second crowded join under the final long overbar',r'\deleted{\unsure{\amalg}}\cup',r'\sqcup',r'\unsure{\deleted{\amalg}\cup|\amalg}','A thin extended transverse run intersects the two heavier uprights; a dark curved base and an extra short oblique descent also survive. These strokes do not determine which form is live.','low','deletion state (struck given live or live given struck)',True,True,'retained','crop09_lower_joins.png',[874,2250,917,2293],'D12',qualification='The actual doubtful-readings row includes both joins, while C.tex marks only the first final cup. The second local qualification is made explicit. H square join remains an alternative.',glyph_status='Square-join component resolved; final form and predecessor state retained as doubtful.')
row('A016-D13','Far right of final bracketed display',r'\unsure{\big]}','No closing bracket supplied',r'\unsure{\big]}','The high and low leftward return strokes reach the right boundary. Their joining upright is cut off or coincident with the dark edge.','low','omission',False,True,'retained','crop10_bottom_right.png',[1635,2216,1685,2334],'D13',qualification='The source-edge limitation remains; no second enlargement was made.')
row('A016-W20','Opening third line, word before the two-point sign','égale','égal','égale','The tall l is followed by an extended bent terminal run, retained as the final e. The full written form is preserved without grammatical adjustment.','medium','misread word',False,True,None,'crop03_line3.png',[637,282,778,363])
row('A016-W21','Endpoint of first partition row',r'\Sigma_1^-',r'\Sigma_1^-,',r'\Sigma_1^-','Half a shows the superscript minus and index 1 followed by blank paper; no comma is visible after the expression.','high','text not on the page',False,True,None,None,[940,597,1100,680],image_evidence='Half a, full-origin (0,0).')
row('A016-W22','Label above the definition equality',r'\text{def}',r'\mathrm{déf}',r'\text{def}','The raised d/e/f letters are visible on half a; no detached accent appears over the e.','high','misread word',False,True,None,None,[794,1025,864,1100],image_evidence='Half a, full-origin (0,0).')
row('A016-W23','Endpoint of definition display',r'\Sigma_2^-',r'\Sigma_2^- .',r'\Sigma_2^-','There is clear blank paper to the right of the terminal Sigma and index; no period is seen.','high','text not on the page',False,True,None,None,[1064,1048,1230,1148],image_evidence='Half a, full-origin (0,0).')
row('A016-W24','Right end of Dans cette partition line','ouverts','ouverts,','ouverts','The final word reaches the image/page boundary. No separate comma candidate is visible in the surviving endpoint area.','low','other',False,True,None,None,[1490,1210,1685,1313],image_evidence='Half b, local bbox [1490,109,1685,212], origin (0,1101).',qualification='The image edge prevents ruling on marks outside the surviving area. The return supplies only the visible endpoint.')
row('A016-G25','Below raised la comp. conn.','Insertion wording without an explicit guide path','Insertion wording without an explicit guide path','GUIDE01, attached to unchanged inserted la comp. conn.','A long bowed line runs below the inserted words from a raised left hook to a downward return immediately before the main Sigma2. Both ends survive.','high','insertion or placement',True,True,None,'crop02_right_top.png',[1162,172,1403,239],graphical_component='GUIDE01',state_change=False)
row('A016-G26','Below raised de X/E2 at right boundary','Insertion wording without an explicit guide path','Insertion wording without an explicit guide path','GUIDE02, attached to unchanged inserted de X/E2','The pale guide begins with a left upward bend, then follows a long shallow rightward curve to the edge. The lower detached hook is the already-transcribed comma, and is not drawn a second time.','medium','insertion or placement',True,True,None,'crop02_right_top.png',[1528,216,1685,250],graphical_component='GUIDE02',state_change=False)
row('A016-G27','Under the right part of connexe','No separate stroke','No separate stroke','Locally qualified STROKE01','A fine nearly horizontal run begins under the later letters and continues with a slight downward drift to the right edge. A small interruption is retained. Its role and hand remain undetermined.','medium','omission',True,True,None,'crop02_right_top.png',[1515,147,1670,161],graphical_component='STROKE01',shape_confidence='high',role_confidence='low',hand='undetermined hand',surface_origin='undetermined')
row('A016-G28','Small pale spot above/right of the central partition brace endpoint','No separate shape','No separate shape','Locally qualified SPOT01, small gray oval','The existing central-letter crop also shows one isolated pale oval-like spot. It has no readable character value; the source of the spot and its hand/role remain unsettled.','low','omission',True,True,None,'crop05_partition5.png',[1137,838,1145,847],graphical_component='SPOT01',shape_confidence='medium',role_confidence='low',hand='undetermined hand',surface_origin='undetermined')
row('A016-G29','Far right beside the third closure row','No separate shapes','No separate shapes','Locally qualified two-component SPOTS02a/b','Two separate dark spots lie on a short rising diagonal, the upper one rounded and the lower one wedge-like. They are retained graphically without assigning punctuation or another character.','medium','omission',True,True,None,'crop11_right_dots.png',[1618,1728,1629,1740],graphical_component='SPOTS02a/b',shape_confidence='high',role_confidence='low',hand='undetermined hand',surface_origin='undetermined')
row('A016-G30','Above the gap before E2 in the second nonempty-intersection condition','No separate shape','No separate shape','Locally qualified SPOT03','A detached short dark triangular/upright shape is visible above the condition. It has no demonstrated connection with the formula.','medium','omission',True,True,None,'crop12_detached_dot.png',[927,1892,932,1899],graphical_component='SPOT03',shape_confidence='high',role_confidence='low',hand='undetermined hand',surface_origin='undetermined')
row('A016-G31','Long cancellation through alors Sigma12 amalg E2 amalg Sigma2','Generic deleted wrapper','Generic struck wrapper','CANCEL01, one explicit observed curved strike with unchanged deletion scope','The stroke starts below alors, rises toward the first Sigma, passes across both joins and E2, and ends just before/below the live following expression. It is not a level horizontal rule.','high','drawing or diagram',True,True,None,'crop08_conclurait.png',[302,2178,1053,2213],graphical_component='CANCEL01',state_change=False)

inventory=[]
def inv(n,kind,position,first,hand='his hand',**extra):
 d=dict(sheet_kind='text',hand=hand,element=f'A016.{n:02d}',kind=kind,position=position,first_words_or_objects=first,transcribed='yes');d.update(extra);inventory.append(d)
inv(1,'text','opening four physical lines','et par suite ... cqfd')
inv(2,'deletion','opening union, second Sigma subscript',r'\unsure{2} beneath live 1')
inv(3,'deletion','opening line, before est',r'\unsure{sera|sont}')
inv(4,'insertion','above contenant, before Sigma2 minus','la comp. conn.')
inv(5,'drawing','below la comp. conn.','GUIDE01, bowed guide with two hooked ends')
inv(6,'insertion','right edge beside Sigma2 minus',r'de X\unsure{/|\setminus}E_{\unsure{2}}')
inv(7,'drawing','below de X/E2 insertion','GUIDE02, shallow curve ending at the page edge')
inv(8,'drawing','under the later part of connexe','STROKE01, interrupted fine horizontal run','undetermined hand',role='undetermined',surface_origin='undetermined')
inv(9,'deletion','opening third line after donc',r"\unsure{c'est}")
inv(10,'text','between opening argument and first partition','L’intersection des deux partitions')
inv(11,'display','first two partition rows',r'X=\Sigma_1^+\amalg E_1\amalg\Sigma_1^-; X=\Sigma_2^+\amalg E_2\amalg\Sigma_2^-')
inv(12,'deletion','first partition, first Sigma',r'\unsure{E} under Sigma')
inv(13,'text','below two partitions','de X est')
inv(14,'display','five-term partition',r'X=\Sigma_1^+\amalg E_1\amalg\deleted{E}\Sigma_{12}\amalg E_2\amalg\Sigma_2^+')
inv(15,'drawing','above and below five-term partition','BRACE01/BRACE02 with Sigma2 minus above and Sigma1 minus below',components=['BRACE01','BRACE02'])
inv(16,'deletion','central Sigma12 in five-term partition','E, resolved predecessor')
inv(17,'drawing','above/right of central upper brace end','SPOT01, qualified pale oval','undetermined hand',role='undetermined',surface_origin='undetermined')
inv(18,'text','left of definition','avec')
inv(19,'display','definition',r'\Sigma_{12}\overset{\text{def}}{=}\Sigma_1^-\cap\Sigma_2^-')
inv(20,'text','two lines beginning Dans cette partition','Dans cette partition ... sont fermés, et on a')
inv(21,'deletion','initial of Dans',r'\unsure{O}')
inv(22,'display','first closure row',r'\Sigma_1^+\subsetneq\overline{\Sigma_1^+}\subset\Sigma_1^+\cup E_1')
inv(23,'display','middle closure row',r'\overline{\Sigma_{12}}\subset\overline{\Sigma_1^-}\cap\overline{\Sigma_2^-}\subset(\Sigma_1^-\cup E_1)\cap(\Sigma_2^-\cup E_2)\subset\Sigma_{12}\cup E_1\cup E_2')
inv(24,'display','third closure row',r'\Sigma_2^+\subsetneq\overline{\Sigma_2^+}\subset\Sigma_2^+\cup E_2')
inv(25,'drawing','right of third closure row','SPOTS02a/b, two qualified separate spots','undetermined hand',components=['upper rounded spot','lower wedge-like spot'],role='undetermined',surface_origin='undetermined')
inv(26,'text','before lower intersection conditions','Notons aussi que')
inv(27,'display','two lower intersection conditions',r'\overline{\Sigma_{12}}\cap E_1\ne\varnothing, \overline{\Sigma_{12}}\cap E_2\ne\varnothing')
inv(28,'drawing','above second lower condition','SPOT03, qualified triangular/upright shape','undetermined hand',role='undetermined',surface_origin='undetermined')
inv(29,'text','last paragraph','Car si on avait p. ex. ... on ... ce qui n’est pas.')
inv(30,'deletion','first letter of last hypothesis under bar',r'\unsure{E} beneath Sigma12')
inv(31,'deletion','E1 in same hypothesis',r'\unsure{\Sigma} beneath E1')
inv(32,'deletion','line beginning alors',r'alors \Sigma_{12}\amalg E_2\amalg\Sigma_2')
inv(33,'drawing','crossing alors and its expression','CANCEL01, one explicit strike, unchanged deletion scope')
inv(34,'insertion','above cancelled alors expression','en conclurait')
inv(35,'display','following live equality',r'\overline{\Sigma_1^-}\cap E_1=\varnothing,')
inv(36,'display','last bracketed line',r'[car \overline{\Sigma_1^-}=...\subset\Sigma_1^-\cup\overline{\Sigma_{12}}\unsure{]}')
inv(37,'deletion','first join under final overbar',r'\unsure{\deleted{\amalg}\cup|\amalg}',state='overwritten square join followed by cup remains a qualified candidate; live square join remains an alternative')
inv(38,'deletion','second join under final overbar',r'\unsure{\deleted{\amalg}\cup|\amalg}',state='overwritten square join followed by cup remains a qualified candidate; live square join remains an alternative')
inv(39,'insertion','under brace below final closure Sigma2 plus',r'\subset\Sigma_2^+\cup E_2')
inv(40,'text','foot left','ce qui n’est pas.')
inv(41,'text','lower left archive numeral','15, recorded only in archive-number comment','undetermined hand')

doubts=[]
for d in rows:
 if d['C_doubt_status']=='retained' or d['id'] in ['A016-G27','A016-G28','A016-G29','A016-G30']:
  alternatives={
   'A016-D01':['2; no firmer numeral recovered'],
   'A016-D02':['sera','sont'],
   'A016-D04a':['/','setminus'],
   'A016-D04b':['2; boundary limits the form'],
   'A016-D05':["c’est; incomplete surviving word"],
   'A016-D07a':['E; incomplete surviving predecessor'],
   'A016-D07c':['E; incomplete surviving predecessor'],
   'A016-D07d':['Sigma; incomplete surviving predecessor'],
   'A016-D08':['O; overlapping loops remain'],
   'A016-D10a':[':', 'à'],
   'A016-D12a':['overwritten amalg followed by cup','live amalg'],
   'A016-D12b':['overwritten amalg followed by cup','live amalg'],
   'A016-D13':['closing bracket; joining upright not separately visible'],
   'A016-G27':['visible thin graphical run; role, hand and surface origin unresolved'],
   'A016-G28':['visible pale oval-like spot; role, hand and surface origin unresolved'],
   'A016-G29':['two visible spots; role, hand and surface origin unresolved'],
   'A016-G30':['visible triangular/upright spot; role, hand and surface origin unresolved']
  }[d['id']]
  doubts.append(dict(id=d['id'],location=d['location'],reading=d['reading'],alternatives=alternatives,confidence=d['confidence'],reason=d['evidence'],crop=d['readers_crop'],bbox=d['bbox'],C_doubt_source_row=d.get('C_doubt_source_row')))

notation=[
 {'location':'ordinary partition joins in both rows and five-term row; cancelled lower expression','sign':'Two uprights meeting an extended lower transverse rule','latex':r'\amalg','witness_mapping':'H uses sqcup at the corresponding occurrences. Each is mapped to this visible square-join form; typography conversion is not separately counted. The two crowded final joins have separate qualified rows D12a/b.'},
 {'location':'all Sigma forms, including opening second Sigma and final long overbar','sign':'Several Sigmas have a detached upper horizontal component above the angular lower body','latex':r'\Sigma','note':'These observed components are retained as the Sigma glyph; no extra overbar is assigned merely from its detached upper stroke.'},
 {'location':'definition above equality','sign':'def, without a detached acute over e','latex':r'\overset{\text{def}}{=}'},
 {'location':'first and third closure rows','sign':'inclusion with lower crossed stroke','latex':r'\subsetneq'},
 {'location':'middle closure row and final bracketed row','sign':'plain open inclusion curve without a separate lower equality bar','latex':r'\subset'},
 {'location':'closure expressions throughout lower half','sign':'flat upper rules distinct from Sigma upper strokes','latex':r'\overline{\Sigma_{12}},\overline{\Sigma_i^\pm}'},
 {'location':'two nonempty intersections and lower equalities','sign':'small loop crossed by a long diagonal slash','latex':r'\varnothing','witness_mapping':'H emptyset and proposal varnothing are aligned to these same observed slash/loop occurrences; no separate reading correction count.'},
 {'location':'raised first insertion','sign':'comp. conn. with two visible abbreviation points','latex':'comp. conn.','expansion_record_only':'composante connexe'},
 {'location':'opening conclusion','sign':'cqfd','latex':'cqfd','expansion_record_only':'ce qu’il fallait démontrer'},
 {'location':'lower argument','sign':'p. ex. with separated abbreviation points','latex':r'p.\,ex.','expansion_record_only':'par exemple'}
]

source_map=[]
for i in range(1,14):
 code=f'D{i:02d}';parts=[d for d in rows if d.get('C_doubt_source_row')==code]
 source_map.append({'source_row':code,'source_row_count':1,'local_parts':[{'id':d['id'],'location':d['location'],'status':d['C_doubt_status'],'reading':d['reading']} for d in parts]})

components=[
 {'id':'STROKE01','reading_tex_anchor':'% STROKE01:','observed_bbox':[1515,147,1670,161],'outer_origin':[225,65],'path_origin':[1515,147],'drawing_rectangle':[0,0,155,14],'units_cm_per_source_pixel':0.0085,'path_count':1,'visible_components':2,'qualification':'local unsure; undetermined role, hand, surface origin'},
 {'id':'GUIDE01','reading_tex_anchor':'% GUIDE01:','observed_bbox':[1162,172,1403,239],'outer_origin':[225,65],'scope_translation':[-225,-65],'path_coordinates':'full-scan coordinates','units_cm_per_source_pixel':0.0085,'path_count':1,'qualification':'unchanged insertion wording and attachment'},
 {'id':'GUIDE02','reading_tex_anchor':'% GUIDE02:','observed_bbox':[1528,216,1685,250],'outer_origin':[225,65],'scope_translation':[-225,-65],'path_coordinates':'full-scan coordinates','units_cm_per_source_pixel':0.0085,'path_count':1,'boundary':'right endpoint meets source edge; separate lower comma is not duplicated'},
 {'id':'BRACE01','reading_tex_anchor':'% BRACE01:','observed_bbox':[659,848,1066,883],'outer_origin':[500,795],'path_coordinates':'outer-local source pixels','units_cm_per_source_pixel':0.008,'path_count':1,'witness_state':'C overbrace and H apparatus already preserve the span and label; path construction supplies no independent lexical correction'},
 {'id':'BRACE02','reading_tex_anchor':'% BRACE02:','observed_bbox':[1085,955,1468,984],'outer_origin':[500,795],'path_coordinates':'outer-local source pixels','units_cm_per_source_pixel':0.008,'path_count':1,'witness_state':'C underbrace and H apparatus already preserve the span and label; physical left return is below the right portion of Sigma12'},
 {'id':'SPOT01','reading_tex_anchor':'% SPOT01:','observed_bbox':[1137,838,1145,847],'outer_origin':[500,795],'path_origin':[1137,838],'drawing_rectangle':[0,0,8,9],'units_cm_per_source_pixel':0.008,'path_count':1,'qualification':'local unsure; gray oval without a character or established role/hand/surface origin'},
 {'id':'SPOTS02a/b','reading_tex_anchor':'% SPOTS02a/b:','observed_bbox':[1618,1728,1629,1740],'outer_origin':[150,1430],'scope_translation':[-150,-1430],'path_origin':[1617,1727],'drawing_rectangle':[0,0,12,15],'units_cm_per_source_pixel':0.008,'path_count':2,'qualification':'one local unsure wrapper, two separate filled components; role/hand/surface origin unresolved'},
 {'id':'SPOT03','reading_tex_anchor':'% SPOT03:','observed_bbox':[927,1892,932,1899],'outer_origin':[320,1885],'scope_translation':[-320,-1885],'path_origin':[926,1891],'drawing_rectangle':[0,0,7,9],'units_cm_per_source_pixel':0.008,'path_count':1,'qualification':'local unsure; no character or established role/hand/surface origin'},
 {'id':'CANCEL01','reading_tex_anchor':'% CANCEL01:','observed_bbox':[302,2178,1053,2213],'outer_origin':[279,2104],'drawing_rectangle':[0,0,1185,123],'units_cm_per_source_pixel':0.007,'path_count':1,'qualification':'one actual strike drawn; six phantom deleted wrappers preserve deletion scope without drawing six additional rules'}
]

report=dict(scan=16,reader='A',start_utc='2026-11-20T16:05:19Z',end_utc='2026-11-20T16:26:08Z',full_image_viewed=True,halves_viewed=True,complete_visual_read=True,
 differences=rows,doubts=doubts,inventory=inventory,
 notes={
  'page_content':'The page continues an argument, records two partitions and their five-term intersection, defines Sigma12, then gives three closure rows and a lower argument ending “ce qui n’est pas.” These are attributed to the manuscript; no result is supplied or repaired here.',
  'author_uncertainty':'No explicit authorial question mark or verbal uncertainty was identified on this sheet. Editorial unsure marks are not attributed to the author.',
  'author_literal_conclusions':['cqfd',"ce qui n’est pas."],
  'title_date_page_counts':'No title or date is visible. The lower-left 15 is recorded only as an archive sheet number, with undetermined hand. Metadata maps our scan 16 to H page 15; no mspage number is supplied.',
  'mathematics_led_reading_decisions':'Bars, indices, plus/minus strokes and join shapes were inspected as visible writing. No algebraic or topological check was performed; check_events is empty. The two final join clusters retain the observed alternatives and state uncertainty.',
  'H_apparatus':'The brace-description note and the final underbrace note are editorial apparatus describing visible structure, and have been compared to that structure. They do not add manuscript prose. H sqcup/emptyset are locally mapped to the visible join and slash/loop forms in notation.',
  'scope':'Only scan016, its supplied packet, assigned images, brief, preamble, notation snapshot and crop helper were read. No other reader return, root decision, other page, external source, OCR, compilation or installation was used.',
  'source_C_notes':'C_notes.txt contains only a newline. No note from another page was used.',
  'boundary_limits':['The right inserted E subscript reaches the source edge.','The closing bracket upright at the foot reaches/coincides with the right edge.','The punctuation endpoint after ouverts is limited by the right boundary.','The lower label under the final brace approaches the bottom image/paper edge; the visible Sigma2 plus union E2 is retained.'],
  'layout_limits':'Graphical path bodies use declared source origins and fixed bounding rectangles. Typeset labels are transcription labels, with no claim of traced handwriting contours or compiled page-layout verification.'
 },
 notation=notation,check_events=[],crops=manifest['crops'],C_doubt_source_rows=source_map,graphical_components=components,
 viewing_log={
  'whole':{'path':'J81-02_81_scan016.jpg','delivered_views':1},
  'halves':[{'path':'J81-02_81_scan016_a.jpg','delivered_views':1,'origin_full':[0,0]},{'path':'J81-02_81_scan016_b.jpg','delivered_views':1,'origin_full':[0,1101]}],
  'half_coordinate_verification':manifest['halves'],
  'crop_delivery':[{'path':c['path'],'delivered_views':1} for c in manifest['crops']],
  'failed_or_unseen_image_deliveries':0,'recrops':0,
  'order':'UTC start; brief; packet/preamble/notation; whole once; half a once; half b once; twelve one-time crops, each delivered individually in numeric order.'
 },
 brief_feedback=[
  'For a tiny gray isolated spot, the distinction between writing and surface/scan origin remains unavailable. The return keeps a local qualified graphic with no character value or attribution.',
  'The final join shapes support both a round bowl and a transverse square-join component. The return qualifies final form and overwritten state together; the actual compound C source row is still counted once.',
  'Physical source-edge limits can prevent deciding endpoint punctuation without leaving a supported comma candidate. The report makes the limit explicit instead of supplying such a mark.'
 ])
report['source_structure_validation']='validation.json'
report['reading_tex_sha256']=__import__('hashlib').sha256((root/'reading.tex').read_bytes()).hexdigest()
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'difference_rows':len(rows),'actual_C_source_rows':len(source_map),'C_local_parts':sum(len(x['local_parts']) for x in source_map),'remaining_doubt_records':len(doubts),'inventory_items':len(inventory),'crops':len(manifest['crops'])}))
