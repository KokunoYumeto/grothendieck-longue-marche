from pathlib import Path
import json

P=Path('/workspace/scratch/94548b74fbe0/out/readers/020/A')
rows=[]
def add(location,C,H,reading,evidence,confidence,kind,diff_C,diff_H,status=None,crop=None,bbox=None,source_row=None,**extra):
    item={'id':f'020A-{len(rows)+1:02d}','location':location,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':diff_C,'diff_H':diff_H,'C_doubt_status':status,'readers_crop':crop,'bbox':{'coordinates':bbox,'origin':'original full scan, upper left'} if bbox else None}
    if source_row: item['C_source_doubt_row']=source_row
    item.update(extra)
    rows.append(item)

add('Opening Pi_I superscript',r'\Pi_I^{\unsure{\circ|0}}',r'\Pi_I^0',r'\Pi_I^{\unsure{\circ|0}}','Small closed ring with a pale centre; both circle and zero remain supported. The primary circle is qualified against H; H zero survives as the alternative.','medium','misread symbol or index',False,True,'retained','01_first_ring.png',[1108,88,1227,165],'R01',recurrence='First of three; printed doubt here only.')
add('Opening Pi_J superscript',r'\Pi_J^\circ',r'\Pi_J^0',r'\Pi_J^\circ; local alternatives \circ|0','Separate small rounded closed outline above the hooked J. Local zero alternative remains even though the recurring primary alone is printed.','medium','misread symbol or index',False,True,'retained','02_second_ring.png',[670,194,783,280],'R01',recurrence='Second of three; source table scope includes this opening recurrence.')
add('Opening distinctes de U',r'\deleted{\Pi}U_{J,i}',r'U_{J,i}',r'\deleted{\Pi}U_{J,i}','Thin transverse cap and upright remnants survive beneath the much heavier U form. The overwritten predecessor is visible on half a.','high','omission',False,True,crop=None,bbox=[1310,164,1469,265])
add('Opening word before parmi',r'\unsure{clas.|deux}',r'deux',r'\unsure{clas.|deux.}','Tall loop over compressed low humps, followed by an isolated endpoint point. The compressed word supports clas. and deux.; the first candidate stays clas. The endpoint point is preserved with either candidate.','low','misread word',False,True,'retained','03_deux_clas.png',[889,289,1008,349],'R02',qualification='Qualified H primary difference, with H word retained as alternative. C primary and its point remain; the explicit point on the alternative adds no independent C count.')
add('First paired intersection, positive Sigma subscript',r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+',r'\Sigma_i^+',r'\Sigma_{\unsure{j|\deleted{J}i|i}}^+','A high point accompanies a long descended stem and low left-returning double stroke. A continuous j is the working primary; overwritten J followed by i and plain i remain complete alternatives.','medium','misread symbol or index',True,True,'retained','04_paired_intersections.png',[823,393,933,498],'R03',mathematical_consequence='The primary transcription prints j at this one intersection. Later i occurrences are recorded independently and supply no repair.')
add('Cancelled Sigma before U est un voisinage',r'\deleted{\unsure{\Sigma_i|\Sigma_j}}',r'\struck{\ill{}}',r'A020-G01: \deleted{\Sigma_{\unsure{j|i}}}, with two literal oblique cancellation runs','A Sigma body survives both crossings. The lowered right return gives j the primary position; i remains possible under the crossed strokes. Both cancellation runs are visible.','low','misread symbol or index',True,True,'retained','05_cancelled_sigma.png',[319,810,403,903],'R04',graphic_group='A020-G01',H_placeholder_parent='H-ILL-01',H_placeholder_count=1,change_components=['Changed C index candidate order','Recovered qualified glyph from H placeholder','Two distinct cancellation runs replace a generic visible strike'])
add('Below gap after voisinage',None,None,'A020-G02: locally qualified gray round point','The complete g descender closes to the left; a separate small gray rounded patch sits below the following gap. Shape is visible; its role, hand and surface origin remain undetermined.','medium','omission',True,True,crop='15_voisinage_detached_point.png',bbox=[1176,831,1185,839],graphic_group='A020-G02')
add('Index after voisinage de corrected E',r'E_{\unsure{i|j}}',r'E_i',r'E_{\unsure{i|j}}','Short lowered hooked stroke with a separate comma farther below/right. The index itself remains too compressed to settle i/j.','medium','other',False,False,'retained','06_voisinage_E.png',[1386,791,1405,818],'R05')
add('Overwritten predecessor at voisinage de E',r'\deleted{\Sigma}E_{\unsure{i|j}}',r'E_i',r'\deleted{\Sigma}E_{\unsure{i|j}}','Angular interior diagonals of Sigma remain inside the heavier upright and bars of E.','high','omission',False,True,crop='06_voisinage_E.png',bbox=[1331,770,1391,820])
add('Comma after voisinage de E index',r'E_{\unsure{i|j}}, et',r'E_i et',r'E_{\unsure{i|j}}, et','A separate low curved comma follows the small index; its upper and lower endpoints are within crop06.','high','omission',False,True,crop='06_voisinage_E.png',bbox=[1396,819,1411,836])
add('First non-emptiness formula, E predecessor',r'\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i',r'\overline{\Sigma_i^+}\cap E_i',r'\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i','A thin angular Sigma interior remains beneath the heavy E. The closure rule above the first Sigma is already present in both witnesses.','high','omission',False,True,crop='07_nonempty_formulas.png',bbox=[476,945,532,996])
add('Second non-emptiness formula, barred Sigma predecessor',r'\overline{\deleted{E}\Sigma_i^-}',r'\overline{\Sigma_i^-}',r'\overline{\deleted{E}\Sigma_i^-}','The old left upright and horizontal strokes remain beneath the heavier diagonal Sigma body. The separate upper closure rule is visible.','high','omission',False,True,crop='07_nonempty_formulas.png',bbox=[742,911,860,988])
add('Second non-emptiness formula, intersected E predecessor',r'\deleted{\Sigma}E_i',r'E_i',r'\deleted{\Sigma}E_i','A diagonal interior angular run survives inside the live E at the right intersection.','high','omission',False,True,crop='07_nonempty_formulas.png',bbox=[916,927,971,983])
add('On verb donc',r'\unsure{voit|sait}',r'voit','sait','The initial low returning stroke has an upper backward hook, followed by a small vowel loop, the marked i and tall terminal t. Working resolution is sait.','medium','misread word',True,True,'resolved','08_voit_sait.png',[1358,891,1482,955],'R10')
add('Live word before cancelled count word',r'est en \deleted{\unsure{tout|est}}',r'est \struck{\ill{}}',r'est en [cancelled tout/est]','The low open e followed by a linked n stands clear to the left of the cancelled word. Its strokes are live.','high','omission',False,True,crop='09_cancelled_count_word.png',bbox=[1325,1058,1405,1094],qualification='This live en lies outside the cancelled H-ILL-02 physical word.')
add('Cancelled word before count',r'\deleted{\unsure{tout|est}}',r'\struck{\ill{}}',r'A020-G03: \deleted{\unsure{tout|est}} with two drawn crossing runs','Initial tall loop and final upturn survive; the intermediate body is crossed. Tout/est remains unresolved. The left short crossing and right long descending crossing are retained as separate literal runs.','low','drawing or diagram',True,True,'retained','09_cancelled_count_word.png',[1454,1035,1592,1094],'R06',graphic_group='A020-G03',H_placeholder_parent='H-ILL-02',H_placeholder_count=1,lexical_diff_C=False,qualification='C count comes from the explicit crossing geometry; the lexical C doubt is retained.')
add('Adverb in parenthesis before la',r'\unsure{aussi|ainsi}',r'aussi',r'\unsure{aussi|ainsi}','The internal body is reduced to a long near-horizontal run, then a curved turn and a dotted final i. Internal letters remain unresolved.','low','other',False,False,'retained','11_aussi_ainsi.png',[300,1367,447,1416],'R11')
add('High point in gap after la',None,None,'A020-G04: locally qualified detached triangular point','A discrete dark triangular point lies above and to the right of la. It is preserved once as a shape; its role, hand and surface origin remain undetermined.','medium','omission',True,True,crop='11_aussi_ainsi.png',bbox=[566,1363,574,1374],graphic_group='A020-G04')
add('Abbreviation before par/p récurrence',r'\unsure{dém.|dem.}',r'dém.',r'\unsure{dém.|dem.}','The small raised stroke is crowded into the d/e group; its separation as an accent remains unresolved. The terminal abbreviation point is distinct. Both accented and unaccented forms are retained.','medium','other',False,False,'retained','12_dem_par_recurrence.png',[670,1335,832,1383],'R07')
add('Compressed word after dém./dem.',r'par',r'par',r'\unsure{par|p}','A long descending p-like stroke returns to an extended rightward head. The horizontal remainder supports compressed par; the single-letter abbreviation p remains a supported alternative. No endpoint point is supplied.','low','other',False,False,crop='12_dem_par_recurrence.png',bbox=[874,1338,956,1409],qualification='New local qualification with unchanged witness primary; not an actual C source doubt row.')
add('Lemma Pi_I superscript',r'\Pi_I^\circ',r'\Pi_I^0',r'\Pi_I^\circ; local alternatives \circ|0','Small rounded closed oval above/right of indexed Pi. Both circle and zero remain supported locally; only the primary is printed at this recurrence.','medium','misread symbol or index',False,True,'retained','13_lemma_formula_insertion.png',[1228,1558,1348,1645],'R01',recurrence='Third of three; source-row R01 counted once overall.')
add('Overwritten union limit under K',r'\deleted{\unsure{I}}K',r'K',r'\deleted{I}K','An old straight vertical and left-reaching top/foot survive through the K strokes. The predecessor I is recovered from these strokes.','medium','misread symbol or index',True,True,'resolved','13_lemma_formula_insertion.png',[1068,1738,1128,1806],'R08')
add('Brace over lemma union body',r'\overbrace{\Sigma_\alpha^+\cup E_\alpha}^{\inserted{\widehat{\Sigma}_\alpha^+}}',r'\note{au-dessus de ... il écrit \widehat{\Sigma}_\alpha^+}',r'A020-G05: complete body and hatted label with literal main brace run and closed left retrace','The left run has a closed oval/retrace before the central raised step; the right run curves to a short descending tip. Both the body and added hatted Sigma remain present once.','high','drawing or diagram',True,True,crop='13_lemma_formula_insertion.png',bbox=[1108,1619,1387,1748],graphic_group='A020-G05',qualification='H apparatus already supplies the hatted label; the H difference concerns the brace geometry, not a second omitted label.')
add('Cancelled inserted non vide and curved guide',r'\inserted{\deleted{non vide}}',r'\add{\uncertain{non vide}}',r'A020-G06: inserted, cancelled non vide, its crossing stroke and long curved guide; adjoining de I, occurs once','A dark oblique crossing passes through non vide. A distinct lower curved guide rises from the gap before de to the right of the inserted line. The complete word-bearing group also includes de I,; partie and et stay outside.','high','deletion state (struck given live or live given struck)',True,True,crop='13_lemma_formula_insertion.png',bbox=[1142,1767,1392,1858],graphic_group='A020-G06',lexical_diff_C=False,qualification='C already supplies the insertion and cancellation state. Its current change is the literal guide/crossing geometry. H has the insertion but leaves the words live.')
add('Cancelled on a before Sigma membership expression',r'\deleted{on a}',r'\struck{\ill{}}',r'\deleted{on a}','The initial round o/n body and separate a survive a single horizontal crossing.','high',r'readable ink left as \ill{}',False,True,crop='14_membership_correction.png',bbox=[608,1981,761,2011],H_placeholder_parent='H-ILL-03',H_placeholder_count=1)
add('Reworked membership/arrow group',r'\deleted{\unsure{\Rightarrow}}\in',r'\in',r'A020-G07; states \deleted{\Rightarrow}\in | \deleted{\to}\in | \in','Outer curved membership-like body, a heavy middle run and a small right-returning arrow-like component are all present. They support the recorded predecessor/live alternatives, while their exact relation and cancellation target remain unsettled.','low','drawing or diagram',True,True,'retained','14_membership_correction.png',[940,1938,1004,2000],'R09',graphic_group='A020-G07',qualification='Local unsure wraps the complete observed paths. Full-state alternatives are explicit in the TeX comment and invisible annotation; they do not print duplicate visible operators.')
add('E inside X setminus E_alpha in membership expression',r'E_\alpha',r'E_\alpha',r'{\unsure{E|\deleted{\Sigma}E}}_\alpha','Top rule, upright and middle arm support E. A slanted lower interior also supports an overwritten Sigma/E state; the source keeps E as primary and records that state alternative locally.','low','other',False,False,crop='14_membership_correction.png',bbox=[1188,1932,1268,1995],qualification='New state qualification with unchanged primary; independent of C source-row R09.')
add('Scan label and archive numeral',r'\scanpage{20}; % archive sheet number: 19',r'\page{19}',r'\scanpage{20}; % archive sheet number: 19','Source administration only: packet maps our scan20 to H page19. A visible lower-left archive 19 is recorded as a comment, with undetermined hand.','high','other',False,False,crop=None,bbox=[25,2304,80,2348],source_only=True)

doubts=[]
def doubt(location,reading,alternatives,confidence,reason,crop,row=None,**extra):
    d={'location':location,'reading':reading,'alternatives':alternatives,'confidence':confidence,'reason':reason,'crop':crop}
    if row: d['C_source_doubt_row']=row
    d.update(extra); doubts.append(d)
doubt('Opening Pi_I ring',r'\circ',['0'],'medium','Small closed ring does not settle the raised character interpretation.','01_first_ring.png','R01',printed='first occurrence qualified')
doubt('Opening Pi_J ring',r'\circ',['0'],'medium','Locally inspected closed ring retains zero alternative.','02_second_ring.png','R01',printed='primary only under recurring-sign rule')
doubt('Word before parmi','clas.',['deux.'],'low','Compressed low humps; separate endpoint point retained with both words.','03_deux_clas.png','R02')
doubt('Positive Sigma index in paired intersection','j',[r'\deleted{J}i','i'],'medium','Descended stem and doubled low return allow both glyph and overwritten-state readings.','04_paired_intersections.png','R03')
doubt('Cancelled Sigma before U','j',['i'],'low','Index crossed; full cancelled Sigma group kept.','05_cancelled_sigma.png','R04')
doubt('E index after voisinage','i',['j'],'medium','Short hooked lowered mark remains compressed.','06_voisinage_E.png','R05')
doubt('Gray point after voisinage','round graphical patch',['punctuation role','independent trace or surface mark'],'medium','Shape visible; hand, role and surface origin unresolved.','15_voisinage_detached_point.png',graphic_group='A020-G02')
doubt('Cancelled count word','tout',['est'],'low','Crossings cut internal letter bodies.','09_cancelled_count_word.png','R06')
doubt('Parenthetical adverb','aussi',['ainsi'],'low','Internal letters run together.','11_aussi_ainsi.png','R11')
doubt('High point after la','triangular graphical point',['independent trace or surface mark','unestablished written-mark role'],'medium','Shape visible; no character role or hand established.','11_aussi_ainsi.png',graphic_group='A020-G04')
doubt('Abbreviation before par/p','dém.',['dem.'],'medium','Small upper stroke merges with the letter group.','12_dem_par_recurrence.png','R07')
doubt('Word after dém./dem.','par',['p'],'low','Compressed rightward head allows the single-letter abbreviation.','12_dem_par_recurrence.png')
doubt('Lemma Pi_I ring',r'\circ',['0'],'medium','Locally inspected closed oval retains both interpretations.','13_lemma_formula_insertion.png','R01',printed='primary only under recurring-sign rule')
doubt('Membership/arrow group',r'\deleted{\Rightarrow}\in',[r'\deleted{\to}\in',r'\in'],'low','Glyph presence, arrow interpretation and cancellation target remain jointly open.','14_membership_correction.png','R09',graphic_group='A020-G07')
doubt('E inside X setminus E_alpha','E',[r'\deleted{\Sigma}E'],'low','Slanted lower interior allows an overwritten predecessor state.','14_membership_correction.png')

inventory=[]
def inv(kind,position,words,hand='his hand',**extra):
    d={'sheet_kind':'text','hand':hand,'element':f'020A.I{len(inventory)+1:02d}','kind':kind,'position':position,'first_words_or_objects':words,'transcribed':'yes'}
    d.update(extra); inventory.append(d)
inv('text','opening three lines','Ainsi les classes de Pi_I ... les clas./deux. parmi')
inv('deletion','opening distinctes de U','Pi overwritten by U')
inv('display','first paired intersection line','U_{J,i} cap Sigma_{j/deleted Ji/i}^+, U_{J,i} cap Sigma_i^-')
inv('deletion','positive Sigma subscript','Possible overwritten J before i, alternative to j or i',qualification='The deletion state is an explicit alternative, not an unqualified decision.')
inv('text','below paired display','qui sont non vides. Or les deux classes en question sont non vides, car')
inv('deletion','before U est un voisinage','Cancelled Sigma with j/i index',graphic_group='A020-G01')
inv('drawing','same cancelled Sigma group','Two slanted cancellation runs',graphic_group='A020-G01',components=['draw run 1','draw run 2'])
inv('text','voisinage line','U_{J,i} est un voisinage de corrected E_{i/j}, et')
inv('drawing','below gap after voisinage','Gray round point','undetermined hand',graphic_group='A020-G02',components=['one gray ellipse'],qualification='Role and surface origin unresolved.')
inv('deletion','voisinage de corrected E','Sigma under E')
inv('display','two non-emptiness formulas','Two overlined Sigma terms intersect corrected E_i and are unequal to empty')
inv('deletion','first non-emptiness E','Sigma under E')
inv('deletion','second overlined Sigma','E under Sigma')
inv('deletion','second non-emptiness E','Sigma under E')
inv('text','count lead-in and equation','On sait donc que le nb des classes est en ... (n-1)+2=n+1=card I+1')
inv('deletion','before count','tout/est cancelled',graphic_group='A020-G03')
inv('drawing','same cancelled count word','Short left crossing and long right crossing',graphic_group='A020-G03',components=['draw run 1','draw run 2'])
inv('text','parenthesis over three lines','ce qui achève aussi/ainsi la dém./dem. par/p récurrence sur le nb des classes')
inv('drawing','high gap after la','Dark triangular point','undetermined hand',graphic_group='A020-G04',components=['one closed fill path'],qualification='Role and surface origin unresolved.')
inv('text','lemma heading','Lemme, single underline; Toute classe de Pi_I est de la forme')
inv('display','lemma first formula','X setminus bigcup_{alpha in deleted I K}(Sigma_alpha^+ cup E_alpha)',graphic_group='A020-G05')
inv('deletion','union limit','I under K')
inv('insertion','above lemma union body','hat Sigma_alpha^+',graphic_group='A020-G05')
inv('drawing','above same parenthesized body','Main brace run and closed left oval/retrace',graphic_group='A020-G05',components=['main brace draw path','left retrace draw path'])
inv('text','lemma continuation','où K est une partie ... de I, et')
inv('insertion','between partie and de I','non vide, cancelled',graphic_group='A020-G06')
inv('deletion','same insertion','non vide',graphic_group='A020-G06')
inv('drawing','same insertion and adjoining de I','One cancellation run and long curved guide',graphic_group='A020-G06',components=['cancellation draw path','curved guide draw path'])
inv('margin note','lower left, slanted upward','K est neq empty / si I neq empty')
inv('text','first condition line','forall alpha in K, ... Sigma_alpha^+ [reworked sign] pi_0(X setminus E_alpha), tels que')
inv('deletion','after forall alpha in K','on a')
inv('drawing','before pi_0','Locally qualified membership/arrow group',graphic_group='A020-G07',components=['outer curved run','middle run','right arrow-like return'])
inv('deletion','same relation group','Possible cancelled Rightarrow or single arrow before membership',qualification='Full-state alternatives include live/retraced membership.',graphic_group='A020-G07')
inv('deletion','E inside X setminus E_alpha','Possible Sigma predecessor beneath E',qualification='E remains primary; predecessor state is locally qualified.')
inv('text','final condition lead-in','forall alpha,beta in K, alpha neq beta, on ait')
inv('display','final hatted intersection','hat Sigma_alpha^+ cap hat Sigma_beta^+ = empty')
inv('display','last parenthesis','Longleftrightarrow Sigma_alpha^+ cap Sigma_beta^+ = empty, closing parenthesis and point')
inv('text','bottom left','Archive numeral 19, preserved in comment','undetermined hand')

graphics=[
 {'id':'A020-G01','source_origin':[320,817],'baseline_source_y':875,'unit_map':'x=0.025em and y=-0.025em per manually selected source pixel','observed_bbox':[319,810,403,903],'fixed_drawing_rectangle':[-2,-5,82,85],'path_commands':2,'visible_text':r'\Sigma_{\unsure{j|i}}','invisible_annotation':r'\deleted{\Sigma_{\unsure{j|i}}}','boundaries':'Cancelled Sigma/index only; following U is outside.','qualification':'Index j/i retained; cancellation present.'},
 {'id':'A020-G02','source_origin':[1175,817],'baseline_source_y':817,'unit_map':'x=0.025em and y=-0.025em','observed_bbox':[1176,831,1185,839],'fixed_drawing_rectangle':[0,0,11,24],'path_commands':1,'visible_text':None,'boundaries':'One point only; voisinage and de are outside.','qualification':'Graphical shape under local unsure; hand, role, surface origin unresolved.'},
 {'id':'A020-G03','source_origin':[1457,1038],'baseline_source_y':1081,'unit_map':'x=0.025em and y=-0.025em','observed_bbox':[1454,1035,1592,1094],'fixed_drawing_rectangle':[-2,-3,130,53],'path_commands':2,'visible_text':r'\unsure{tout|est}','invisible_annotation':r'\deleted{\unsure{tout|est}}','boundaries':'Cancelled word only; en and following count are outside.'},
 {'id':'A020-G04','source_origin':[565,1395],'baseline_source_y':1395,'unit_map':'x=0.025em and y=-0.025em','observed_bbox':[566,1363,574,1374],'fixed_drawing_rectangle':[0,-33,12,0],'path_commands':1,'visible_text':None,'boundaries':'One point only; la and dém./dem. are outside.','qualification':'Graphical shape under local unsure; hand, role, surface origin unresolved.'},
 {'id':'A020-G05','source_origin':[1105,1660],'baseline_source_y':1735,'unit_map':'x=0.025em and y=-0.025em','observed_bbox':[897,1619,1387,1807],'fixed_drawing_rectangle':[-210,-50,275,145],'path_commands':2,'visible_text':r'X\setminus\bigcup_{\alpha\in\deleted{I}K}; (\Sigma_\alpha^+\cup E_\alpha); \inserted{\widehat{\Sigma}_\alpha^+}','boundaries':'Complete formula, parenthesized body and added hatted label; de la forme and où are outside.','qualification':'Manual brace geometry; label and body unchanged.'},
 {'id':'A020-G06','source_origin':[1148,1770],'baseline_source_y':1845,'unit_map':'x=0.025em and y=-0.025em','observed_bbox':[1142,1767,1392,1858],'fixed_drawing_rectangle':[-3,-5,255,94],'path_commands':2,'visible_text':r'\inserted{non vide}; de I,','invisible_annotation':r'\inserted{\deleted{non vide}}','boundaries':'Inserted cancelled non vide and adjoining de I, occur once; partie and et are outside.','qualification':'Cancellation and guide are separate observed paths.'},
 {'id':'A020-G07','source_origin':[945,1943],'baseline_source_y':1984,'unit_map':'x=0.025em and y=-0.025em','observed_bbox':[940,1938,1004,2000],'fixed_drawing_rectangle':[-2,-2,55,55],'path_commands':3,'visible_text':None,'invisible_annotation':r'\deleted{\Rightarrow}\in|\deleted{\to}\in|\in','boundaries':'Relation shape only; Sigma and pi_0 are outside.','qualification':'Whole graphic locally unsure; complete state alternatives explicit in comment and phantom, without duplicate visible operators.'}
]

source_map=[
 {'id':'R01','source_location':'opening and lemma','source_reading':'superscript circle','source_alternatives':['0'],'status':'retained','local_reports':['020A-01','020A-02','020A-21'],'physical_loci':3},
 {'id':'R02','source_location':'line 3','source_reading':'clas.','source_alternatives':['deux'],'status':'retained','local_reports':['020A-04'],'physical_loci':1},
 {'id':'R03','source_location':'first paired intersection','source_reading':'i written on J','source_alternatives':['j','i'],'status':'retained','local_reports':['020A-05'],'physical_loci':1},
 {'id':'R04','source_location':'before U est un voisinage','source_reading':'Sigma_i','source_alternatives':['Sigma_j'],'status':'retained','local_reports':['020A-06'],'physical_loci':1},
 {'id':'R05','source_location':'voisinage de E','source_reading':'i','source_alternatives':['j'],'status':'retained','local_reports':['020A-08'],'physical_loci':1},
 {'id':'R06','source_location':'word struck at right before count','source_reading':'tout','source_alternatives':['est'],'status':'retained','local_reports':['020A-16'],'physical_loci':1},
 {'id':'R07','source_location':'in the parenthesis','source_reading':'dém.','source_alternatives':['dem.'],'status':'retained','local_reports':['020A-19'],'physical_loci':1},
 {'id':'R08','source_location':'under K, union index','source_reading':'I','source_alternatives':[],'status':'resolved','local_reports':['020A-22'],'physical_loci':1},
 {'id':'R09','source_location':'beside membership sign before pi_0','source_reading':'Rightarrow','source_alternatives':[],'status':'retained','local_reports':['020A-26'],'physical_loci':1},
 {'id':'R10','source_location':'above the count','source_reading':'voit','source_alternatives':['sait'],'status':'resolved','local_reports':['020A-14'],'physical_loci':1},
 {'id':'R11','source_location':'in the parenthesis, before la','source_reading':'aussi','source_alternatives':['ainsi'],'status':'retained','local_reports':['020A-17'],'physical_loci':1}
]

notation=[
 {'location':'three Pi occurrences','sign':'small raised ring','proposed_LaTeX':r'first \Pi_I^{\unsure{\circ|0}}, then \Pi_J^\circ and \Pi_I^\circ','qualification':'All three local zero alternatives are in doubts and source-row R01.'},
 {'location':'opening U and both paired U terms, later voisinage U','sign':'hooked capital J, comma, dotted i','proposed_LaTeX':r'U_{J,i}'},
 {'location':'paired intersections','sign':'Sigma upper head strokes','proposed_LaTeX':r'\Sigma^+,\Sigma^-','qualification':'The supplied pair has one letter-head run per Sigma; the separate closure rules are in the later formulas.'},
 {'location':'two non-emptiness formulas','sign':'separate spanning upper rules','proposed_LaTeX':r'\overline{\Sigma_i^+},\overline{\deleted E\Sigma_i^-}','qualification':'Both existing C/H closure bars are locally confirmed.'},
 {'location':'small Sigma i indices in negative pair and barred formulas','sign':'point next to lower terminal hook','proposed_LaTeX':r'\Sigma_i','qualification':'Point and terminal hook transcribed together; no duplicate detached point supplied.'},
 {'location':'count and final parenthesis','sign':'nb','proposed_LaTeX':'nb','qualification':'Two occurrences, no expansion.'},
 {'location':'count','sign':'low linked card','proposed_LaTeX':r'\operatorname{card} I+1'},
 {'location':'ce qui achève','sign':'two short adjoining accent fragments','proposed_LaTeX':'achève','qualification':'Grave retained; this unchanged spelling is explicit in the audit.'},
 {'location':'récurrence','sign':'raised short acute stroke','proposed_LaTeX':'récurrence','qualification':'Acute retained independently of the unresolved dém./dem. accent.'},
 {'location':'Lemme heading','sign':'single underline','proposed_LaTeX':r'\uline{Lemme}'},
 {'location':'lemma formula annotation and final hatted pair','sign':'three roofs on Sigma','proposed_LaTeX':r'\widehat{\Sigma}_\alpha^+,\widehat{\Sigma}_\beta^+','qualification':'Three local hats total: one added label and two final hatted terms; the last parenthetical pair remains unhatted.'},
 {'location':'last parenthesis','sign':'two-ended, two-line arrow','proposed_LaTeX':r'\Longleftrightarrow'},
 {'location':'margin and all emptiness statements','sign':'slashed small oval','proposed_LaTeX':r'\varnothing'},
 {'location':'archive foot','sign':'19','proposed_LaTeX':'% archive sheet number: 19','qualification':'Undetermined hand; comment only.'}
]

audit=json.loads((P/'image_audit.json').read_text())
audit['checkpoint_status']='Root checkpoint hold respected; resumed in the same context after release. No subsequent image was opened.'
audit['next_work']='Complete source-only final checks and return.'
(P/'image_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')

report={
 'scan':20,'reader':'A','start_utc':'2026-11-20 20:45:40 UTC','end_utc':None,
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'differences':rows,'doubts':doubts,'inventory':inventory,
 'notes':{
   'page_content':'The author identifies the classes of Pi_I with the Pi_J classes distinct from U_{J,i}, together with the nonempty intersections, writes their count as (n-1)+2=n+1=card I+1, and states a lemma describing a class by X minus a union of Sigma_alpha^+ cup E_alpha. He writes pairwise disjointness of the hatted sets and the parenthetical equivalence with disjointness of the unhatted sets. These are attributed manuscript assertions; no proof check was performed.',
   'author_uncertainty':{'exact_words':[],'observation':'No explicit authorial uncertainty phrase was read. The editorial doubts above concern the ink. The inserted non vide is visibly cancelled.'},
   'title_date_page_counts':{'heading':'Lemme, single underline','date':None,'manuscript_page_number':None,'archive_number':'19','our_scan':20,'H_page':19,'pages_read':1},
   'mathematics_led_reading_decisions':'The malformed or reworked local signs were kept with their observed states. Later i indices did not resolve the positive Sigma index or cancelled Sigma. The written count and final parenthetical equivalence were transcribed without computation or proof validation.',
   'H_apparatus':'H notes about other pages and the location of the added hatted Sigma are apparatus. No other page was inspected. The three struck ill placeholders each receive one physical parent count.',
   'source_only_administration':'Scan20/H page19 mapping and the archive comment are administrative source choices with diff_C=false and diff_H=false. No manuscript page-number glyph is supplied.',
   'S_coverage':{'row_id':'SA01-K81-06','item':'SA01-29','recorded_where':'81/15-22','recorded_author':'Claude Opus 5.5 at effort max, reader R4 (no scan viewed)','stated_scope':'The row spans scans015–022 and supplies witness proposals only; each example must be matched locally.','local_observations':'Two closure bars on Sigma_i^+ and the corrected Sigma_i^- were visually confirmed. Both are already in current C and H. The exact Sigma_1 and U_s example strings are not on this page. No bar was inferred from the broad range.','diff_C':False,'diff_H':False,'ink_correction_count':0},
   'processing':'All requested packet files, brief v18 and PREAMBLE were read. Whole page once for layout, supplied a once line by line, b once line by line; 14 planned crops and one new complete attachment target. All 18 image deliveries succeeded; zero repeated views and zero failed unseen deliveries. The last crop supplied complete neighbouring context for a newly noticed gray point; its E-index neighbour was outside that crop. No OCR, web research, rendering, compilation, installation or optional mathematical computation occurred.',
   'manual_graphics':'Seven graphical groups use declared local origins, fixed rectangles, base-west text nodes and consistent local pixel units. These are manual approximations, with no rendered or metric validation. The G07 phantom annotation is excluded from bounds by overlay, while its actual paths retain the local qualifier.',
   'report_silent_source_choices':['clas. remains primary; the endpoint point is included with both word candidates','sait is printed unqualified after its local resolution','aussi remains primary with ainsi alternative','achève uses a grave; récurrence uses an acute','dém. retains dem. as an explicit alternative','par retains p without a point as an explicit alternative','later Pi rings print circle but retain local zero alternatives in report','inside X setminus E_alpha, E remains primary with a Sigma/E predecessor-state alternative','G07 prints the locally qualified observed graphic; complete state candidates are in its comment and invisible annotation','the final parenthetical Sigmas carry plus signs and no hats','the two detached small shapes remain graphical, with undetermined hands and roles']
 },
 'notation':notation,'check_events':[],'crops':json.loads((P/'crop_manifest.json').read_text()),
 'brief_feedback':['The exact count unit is clarified here as 11 actual C source rows and 13 local subloci, because R01 covers three rings.','A qualified relation graphic carries full-state alternatives in its source comment and invisible annotation so its observed strokes occur once; this representational choice is explicit for consolidation.','The new gray point required one complete neighbouring-word attachment target after discovery at crop06; no decided E-index target was reopened.'],
 'C_doubt_source_map':source_map,'graphics':graphics,'image_audit':audit,
 'counts':{'actual_C_doubt_source_rows':len(source_map),'C_doubt_local_subloci':sum(r['physical_loci'] for r in source_map),'C_doubt_rows_resolved':sum(r['status']=='resolved' for r in source_map),'C_doubt_rows_retained':sum(r['status']=='retained' for r in source_map),'difference_records':len(rows),'diff_C_true':sum(r['diff_C'] for r in rows),'diff_H_true':sum(r['diff_H'] for r in rows),'remaining_doubt_loci':len(doubts),'inventory_items':len(inventory),'graphic_groups':len(graphics),'literal_draw_or_fill_commands':sum(g['path_commands'] for g in graphics),'local_crops':15,'successful_image_deliveries':18,'failed_unseen_deliveries':0,'mathematical_check_events':0,'H_ill_placeholder_parents':3}
}
(P/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['counts'],indent=2))
