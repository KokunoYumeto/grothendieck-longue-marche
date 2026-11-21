from pathlib import Path
import json,difflib,re
p=Path('out/readers/021/C')
c=Path('packets/021/C.tex').read_text(); h=Path('packets/021/H.tex').read_text(); tex=(p/'reading.tex').read_text()
man=json.loads((p/'crop_manifest.json').read_text()); groups=json.loads((p/'graphical_groups.json').read_text())
crops={x['path']:x for x in man['crops']}
rows=[]
for ln,line in enumerate(Path('packets/021/C_doubts.txt').read_text().splitlines(),1):
 if line=='## Doubtful readings': active=True
 elif line.startswith('## '): active=False
 elif locals().get('active') and line.startswith('| 21 |'): rows.append((ln,line))
D=[]
def diff(i,loc,C,H,reading,evidence,confidence,kind,dc,dh,status=None,crop=None,bbox=None,**extra):
 d={'id':i,'location':loc,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dc,'diff_H':dh,'C_doubt_status':status,'readers_crop':crop,'bbox':bbox or (crops[crop]['bbox'] if crop else None),'coordinate_origin':'original full scan top-left'}
 d.update(extra); D.append(d); return d
R=[
('opening after je dis que',r'\unsure{l\'on a|on a}',r'\uncertain{on a}',"l'on a | on a",'Broad open loop and separate following run remain compatible with both local readings; endpoint a is a compact dark form.','medium','other',False,True,'retained','crop01_opening.png'),
('between first intersections',r'\text{\unsure{i.e|i.e.}}','i.e.','i.e','The e has a continuous rightward terminal curve; the following paper has no separate terminal point. The adjacent long upright belongs to que above.','high','other',True,True,'resolved','crop02_first_ie.png'),
('beginning of parenthetical line',r'\unsure{(ce|Ce}','(ce','(ce','Tall separate left parenthesis is followed by the small ce; its lower return is visible. No matching close is supplied.','high','other',True,False,'resolved','crop03_ce_statement.png'),
('cancelled line under K condition',r'\deleted{\unsure{\Sigma_\alpha}}',r'\struck{\ill{}}',r'\deleted{\Sigma_\alpha}','Angular head, diagonal/body and low alpha curl survive the oblique crossings. The literal crossings are included in G02.','medium',r'readable ink left as \ill{}',True,True,'resolved','crop04_upper_brace.png'),
('after Or',r'\unsure{comme}',r'\struck{\ill{}} \ill{} :','comme (qualified)','Initial joined loops are heavily retraced, followed by the shallow repeated humps and e run. The lexical qualification remains.','medium','other',False,False,'retained','crop05_or_comme.png'),
('marginal lead-in',r'\unsure{j.e.|i.e.}','i.e.','j.e. | i.e.; literal middle two-point cluster also preserves j:e./i:e. candidates','The first stem descends and hooks left; a high first-letter dot and two separate middle points are visible. The following small e/c-shaped stroke and final point are retained.','low','other',False,True,'retained','crop08_margin.png'),
('central sign between sideways labels',r'\unsure{\rotatebox{-90}{$!$}|\text{ou}|-}',None,'upright ! | sideways ou | sideways dash','A short nearly upright shaft and a separate lower point are visible. Their role along the sideways labels remains open; the actual two components are drawn under one local qualifier.','low','other',False,False,'retained','crop08_margin.png'),
('third upright marginal row',r'\unsure{\Sigma_{i\alpha}|\Sigma_{i,\alpha}}',r'\Sigma_\alpha',r'\Sigma_{i\alpha} | \Sigma_{i,\alpha}','One dot stands above the terminal hook before alpha; the hook is shared by the visible Sigma/index group. Both original comma alternatives remain, with no duplicated dot or stem.','medium','other',False,False,'retained','crop08_margin.png'),
('verb after alpha0 in K1',r'\unsure{signifi|signifie}','signifie','signifie','After the dotted i, a separate short slanted terminal stroke supplies the final e. The complete word and endpoint are within crop09.','medium','other',True,False,'resolved','crop09_signifi.png'),
('cancelled word after ce qui',r'\deleted{\unsure{impli|impl.}}',r'\struck{implique}',r'\deleted{impli} | \deleted{impl.}','The initial dot, compressed low run, tall loop and final short stroke remain under the crossing runs. The crop supports the short cancelled forms without a written que ending.','low','abbreviation expanded or spelling modernised',False,True,'retained','crop10_cancelled_impli.png'),
('live replacement after cancellation',r'\unsure{signifie}','signifie','signifie','The complete live word ends with a separate short e stroke beyond the dotted i.','medium','other',True,False,'resolved','crop10_cancelled_impli.png'),
('corollary Pi exponent',r'\Pi_I^{\unsure{\circ|0}}',r'\Pi_I^0',r'\Pi_I^{\unsure{\circ|0}}','Small closed raised loop with an entry curl; its circle/zero interpretation remains open. The primary circle differs from H while H zero remains an alternative.','medium','other',False,True,'retained','crop12_pi.png'),
('old V under final E_alpha',r'\deleted{\unsure{V}}E_\alpha',r'E_\alpha',r'\deleted{V}E_\alpha, overlaid','Two thin oblique arms meet below the live E crossbars, preserving the V predecessor. G09b keeps the overlap and one live E_alpha.','high','omission',True,True,'resolved','crop13_bottom_brace.png'),
('large union in E_i subset U display',r'\mathop{\unsure{\rlap{\raisebox{.65ex}{$\scriptstyle-$}}\bigcup|\bigcup}}',r'\bigcup','round union with high transverse run','The horizontal starts left of the left stalk, crosses it and ends inside the cup. Both the complete bowl and this separate run are preserved. Presence is resolved; no extra mathematical operation is assigned.','high','other',True,True,'resolved','crop06_central_union.png'),
('right index in second inclusion',r'\Sigma_{\unsure{\alpha_0|\alpha}}^-',r'\Sigma_{\alpha_0}^-',r'\Sigma_{\unsure{\alpha_0|\alpha}}^-','A dark low terminal enlargement follows the alpha loop; it supports a compact zero and also a continuous alpha tail. Both candidates remain.','medium','other',False,False,'retained','crop07_second_inclusion.png')
]
M=[]
for n,v in enumerate(R,1):
 loc,C,H,rd,ev,cf,k,dc,dh,st,cr=v
 rid=f'C021-R{n:02d}'
 if H is None: H='Diagram apparatus: no central sideways sign transcribed'
 d=diff(rid,loc,C,H,rd,ev,cf,k,dc,dh,st,cr,source_row_id=rid,raw_source_file='packets/021/C_doubts.txt',raw_source_line=rows[n-1][0],raw_source_row=rows[n-1][1],physical_count_key=rid)
 if n==5:d['H_parent_count']='C021-D02'
 if n in (7,8):d['H_parent_count']='C021-D04'
 M.append({'source_row_id':rid,'source_table':'Doubtful readings','original_row_order':n,'source_file':'packets/021/C_doubts.txt','source_line':rows[n-1][0],'raw_source_row':rows[n-1][1],'local_parts':[{'id':rid+'-a','location':loc,'status':st,'reading':rd,'crop':cr,'difference_id':rid}],'status':st,'diff_C':dc,'raw_C_table_retained':True})

diff('C021-D01','opening endpoint after a','no colon',':','no colon','The space after the compact terminal a contains no colon.','high','text not on the page',False,True,crop='crop01_opening.png')
diff('C021-D02','whole Or lead-in',r'Or \unsure{comme} on a',r'Or \struck{\ill{}} \ill{} :',r'Or \unsure{comme} on a','The entire short line is visible: Or, retraced comme, on and compact a. H whole placeholder passage receives one parent count.','medium',r'readable ink left as \ill{}',False,True,crop='crop05_or_comme.png',children=['C021-R05'],H_count_scope='one whole placeholder passage')
diff('C021-D03','marginal middle two-point cluster','j.e./i.e. with one middle point','i.e.',r'literal G05a; j.e.|i.e.|j:e.|i:e.','Two vertically separated middle points occur after the descending first stem. They remain drawn once with attachment/punctuation unresolved.','medium','drawing or diagram',True,False,crop='crop08_margin.png',H_parent_count='C021-R06',raw_component_diff_H=True,source_group='C021-G05a')
diff('C021-D04','complete marginal diagram',r'C tikz-cd five rows, two braces and sideways labels',r'H note: Sigma_i+ ou Sigma_i-, E_i, Sigma_alpha, E_alpha, Sigma_alpha0+ with one accolade','G05 complete diagram','The crop shows two nested braces with small closed turns, five upright rows, the third indexed i/alpha row, two sideways signed labels and their central sign. One H drawing-description parent covers all local diagram differences.','high','drawing or diagram',True,True,crop='crop08_margin.png',source_group='C021-G05',H_count_scope='one drawing-description replacement',children=['C021-R07','C021-R08','C021-M04'])
diff('C021-D05','actual cancelled Sigma crossing geometry','generic deleted annotation','struck ill placeholder','literal G02 cancellation','Two angular body/head runs and two oblique crossing runs plus the alpha curl are represented once; no generic extra strike is drawn.','medium','drawing or diagram',False,False,crop='crop04_upper_brace.png',C_parent_count='C021-R04',H_parent_count='C021-R04',raw_component_diff_C=True,raw_component_diff_H=True,source_group='C021-G02')
diff('C021-D06','upper large brace','standard left brace','vertical bar','two literal meeting brace runs','Upper near-vertical run turns to the pointed middle; lower run begins at its leftward point and descends separately.','high','drawing or diagram',True,True,crop='crop04_upper_brace.png',source_group='C021-G02')
diff('C021-D07','second K in K=K1 union {i}','firm K1','firm K1','K with head retrace | deleted I followed by live K, literal extra crossbar','A short transverse run crosses the upper upright of this K. The complete literal K is qualified; the alternative predecessor state stays explicit in source/report.','medium','drawing or diagram',True,True,crop='crop04_upper_brace.png',source_group='C021-G02a',new_qualifier_on_firm_C=True)
diff('C021-D08','achèvera accent','achèvera','achèvera',r'ach\unsure{è|é|e}vera','A small raised mark over the vowel is visible; its slope and accent attachment remain insufficiently distinct. All three local accent/presence candidates are printed.','low','other',True,False,crop='crop03_ce_statement.png',new_qualifier_on_firm_C=True)
diff('C021-D09','demonstration first vowel','démonstration','démonstration',r'\unsure{demonstration|démonstration}','No separated acute is securely recovered above the compressed first vowel. The unaccented primary and the witness accented alternative remain together.','medium','misread word',True,True,crop='crop03_ce_statement.png',new_qualifier_on_firm_C=True,qualified_H_overlap=True)
diff('C021-D10','lead-in to second inclusion','cela implique que','ce qui implique que','cela implique que','The first cluster has c, looped l and a terminal low vowel stroke, giving the single word cela; followed by implique que.','high','misread word',False,True,bbox=[292,1028,891,1140],half_reference={'file':'J81-03_81_scan021_a.jpg','origin_full_scan':[0,0],'bbox':[292,1028,891,1140]})
diff('C021-D11','cancelled impli crossing paths','generic deleted strike','struck implique','G07 two crossing runs','A long slightly rising crossing and a separate shorter lower run are retained over the cancelled short word.','high','drawing or diagram',True,False,crop='crop10_cancelled_impli.png',H_parent_count='C021-R10',raw_component_diff_H=True,source_group='C021-G07')
diff('C021-D12','précédent first accent','précédent','précédent',r'pr\unsure{é|ê}cédent','The raised stroke is short and bent; acute and circumflex-shaped readings remain supported locally. The second é is retained separately as written in the selected source.','medium','other',True,False,crop='crop17_corollary_words.png',new_qualifier_on_firm_C=True)
diff('C021-D13','bottom X setminus Sigma_alpha',r'X\setminus\Sigma_\alpha',r'X\setminus E_\alpha',r'X\setminus\Sigma_\alpha','The letter has an angular descending middle and lower return, with a separate short top run; it is preserved as Sigma.','high','misread symbol or index',False,True,crop='crop13_bottom_brace.png')
diff('C021-D14','corollary left rule','straight tabular rule','apparatus records vertical rule','literal curved continuous rule G09','The line starts beneath the heading, bends slightly through the body and reaches the lower margin. H already describes its presence.','high','drawing or diagram',True,False,crop='crop16_lower_trace.png',bbox=[250,1810,271,2340],source_group='C021-G09',half_reference={'file':'J81-03_81_scan021_b.jpg','origin_full_scan':[0,1101],'bbox':[250,709,271,1239]})
diff('C021-D15','bottom main brace','standard left brace','cases brace','literal looped brace ending at page edge','The visible middle closes into a small loop. The lower continuation reaches the physical edge, whose surviving endpoint is retained without a supplied lower arm.','high','drawing or diagram',True,True,crop='crop13_bottom_brace.png',source_group='C021-G09')
diff('C021-D16','corollary large union','ordinary bigcup','ordinary bigcup','G09a bowl and pale left retrace','The dark cup has a short pale returning run alongside its upper-left limb. Both paths are preserved.','high','drawing or diagram',True,True,crop='crop21_last_union_sigma.png',source_group='C021-G09a')
diff('C021-D17','overlap of old V and live E_alpha','deleted V before live E','E_alpha only','G09b actual overlaid predecessor/live group','The two thin V arms and live E crossbars occupy one physical cluster. The qualified C source is resolved under R13; this row exposes the geometric choice without another count.','high','drawing or diagram',False,False,crop='crop13_bottom_brace.png',C_parent_count='C021-R13',H_parent_count='C021-R13',raw_component_diff_C=True,raw_component_diff_H=True,source_group='C021-G09b')
# Each independently variable head is recorded at its own physical locus.
heads=[
('H01','first roofed Sigma alpha0',[565,150,695,260],'crop18_first_intersection.png','C021-G01a',True),
('H02','first display roofed Sigma_i+',[738,153,829,245],'crop18_first_intersection.png','C021-G01',True),
('H03','right first intersection Sigma_alpha0',[1238,177,1318,253],'crop19_second_intersection.png','C021-G01',True),
('H04','right intersection Sigma_i',[1342,178,1404,241],'crop19_second_intersection.png','C021-G01',True),
('H05','central roofed Sigma_alpha+',[1147,831,1236,930],'crop06_central_union.png','C021-G03',True),
('H06','second inclusion roofed Sigma_alpha0+',[912,1080,1030,1182],'crop07_second_inclusion.png','C021-G04',True),
('H07','second inclusion right Sigma_alpha0/alpha minus',[1130,1095,1270,1182],'crop07_second_inclusion.png','C021-G04',True),
('H08','exclusion left Sigma_alpha0+',[621,1316,749,1410],'crop11_exclusion.png','C021-G06',True),
('H09','exclusion right Sigma_i+',[855,1318,944,1393],'crop11_exclusion.png','C021-G06',True),
('H10','proof conclusion Sigma_i+',[303,1552,405,1628],'crop22_proof_conclusion.png','C021-G08',True),
('H11','proof conclusion Sigma_alpha+',[457,1555,542,1621],'crop22_proof_conclusion.png','C021-G08',True),
('H12','marginal upper Sigma_i+',[1507,962,1567,1013],'crop08_margin.png','C021-G05',False),
('H13','marginal upper Sigma_i-',[1603,967,1661,1015],'crop08_margin.png','C021-G05',False),
('H14','marginal third Sigma_i alpha',[1532,1090,1614,1137],'crop08_margin.png','C021-G05',False),
('H15','marginal bottom Sigma_alpha0+',[1525,1209,1630,1280],'crop08_margin.png','C021-G05',False),
('H16','bottom condition first Sigma_alpha+',[532,2293,628,2348],'crop13_bottom_brace.png','C021-G09',True),
('H17','bottom X setminus Sigma_alpha head',[1160,2300,1215,2345],'crop13_bottom_brace.png','C021-G09',False)
]
for suffix,loc,box,cr,g,dh in heads:
 dc=suffix not in ('H12','H13','H14','H15')
 d=diff('C021-'+suffix,loc,'ordinary Sigma macro at this locus','ordinary Sigma macro or diagram apparatus','complete literal head/body group; ordinary primary Sigma reading retained','The short upper run and the lower bent body are separately visible. The selected literal group includes the whole letter, its index and raised sign once; the upper-run role remains head/retrace | independent upper rule.','medium','drawing or diagram',dc,dh,crop=cr,bbox=box,source_group=g,role_alternatives=['Sigma head/retrace','independent upper rule'],printed_qualifier=(suffix=='H01'))
 if suffix in ('H12','H13','H14','H15'): d.update(C_parent_count='C021-D04',H_parent_count='C021-D04',raw_component_diff_C=True,raw_component_diff_H=True)
 if suffix=='H17': d.update(H_parent_count='C021-D13',raw_component_diff_H=True)
 if suffix=='H01':d['new_qualifier_on_firm_C']=True
for ident,loc,cr,bbox,sg,dc,dh,parent in [
('M01','two pale upper runs','crop14_upper_traces.png',[832,415,890,452],'C021-M01',True,True,None),
('M02','left detached slash','crop15_left_trace.png',[100,878,122,899],'C021-M02',True,True,None),
('M03','point beneath central roof','crop06_central_union.png',[1149,850,1162,862],'C021-M03',False,False,'C021-H05'),
('M04','pale terminal margin trace','crop08_margin.png',[1456,1237,1478,1267],'C021-M04',False,False,'C021-D04'),
('M05','short trace above V','crop12_pi.png',[319,1838,335,1855],'C021-M05',True,True,None),
('M06','point left of corollary rule','crop16_lower_trace.png',[187,2112,202,2130],'C021-M06',True,True,None)]:
 d=diff('C021-'+ident,loc,'absent separate component','absent separate component','local qualified literal shape '+sg,'A discrete local shape remains visible in the stated crop; shape is preserved without a character, operation, hand or surface-origin assignment.','medium','omission',dc,dh,crop=cr,bbox=bbox,source_group=sg,role='undetermined',hand='undetermined hand',surface_origin='undetermined')
 if parent:d.update(C_parent_count=parent,H_parent_count=parent,raw_component_diff_C=True,raw_component_diff_H=True)
# C source map retains the raw table identity even when a graphical child receives the count.
for row in M:
 rid=row['source_row_id']
 row['related_component_rows']=[d['id'] for d in D if d.get('C_parent_count')==rid or d.get('H_parent_count')==rid]

inventory=[]
def inv(el,kind,pos,words,hand='his hand',components=None):
 v={'sheet_kind':'text','hand':hand,'element':el,'kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes'}
 if components:v['components']=components
 inventory.append(v)
for a in [
('021.C.01','text','opening',"Soit alpha0 in K1, je dis que l'on a | on a"),
('021.C.02','display','first pair of equalities','roofed Sigma_alpha0 cap roofed Sigma_i+ = empty i.e Sigma_alpha0 cap Sigma_i = empty'),
('021.C.03','text','parenthetical prose','(ce qui achèvera/achévera/achevera la demonstration/démonstration, car on aura'),
('021.C.04','display','upper U formula and K condition','U=X setminus union roofed Sigma_alpha+; K=K1 union {i}'),
('021.C.05','deletion','under K condition','Sigma_alpha, crossed'),
('021.C.06','text','below first union','comme dans le lemme.'),
('021.C.07','text','next proof lead-in','Or comme on a'),
('021.C.08','display','central inclusion','E_i subset U_{J,i}=X setminus cup-with-cross-stroke roofed Sigma_alpha+'),
('021.C.09','text','second inclusion lead-in','cela implique que'),
('021.C.10','display','second inclusion','E_i subset X setminus roofed Sigma_alpha0+ = Sigma_alpha0/alpha-'),
('021.C.11','margin note','middle right','j.e./i.e. and its separate middle points'),
('021.C.12','diagram','middle right','five upright rows, two sideways signed labels, central !/ou/dash, two braces'),
('021.C.13','text','below inclusion',"d'autre part alpha0 in K1 signifie"),
('021.C.14','display','exclusion','Sigma_alpha0+ not subset Sigma_i+'),
('021.C.15','text','conclusion of proof','ce qui [cancelled impli/impl.] signifie aussi que Sigma_i+ cap Sigma_alpha+ = empty, cqfd.'),
('021.C.16','deletion','inside ce qui clause','impli | impl., two crossing runs'),
('021.C.17','text','corollary heading','Corollaire du lemme, underlined; Pour une classe'),
('021.C.18','text','first ruled line','V de Pi_I circle/zero, son expression'),
('021.C.19','display','corollary expression','V=X setminus union roofed Sigma_alpha+'),
('021.C.20','text','above bottom brace','du lemme précédent/prêcédent est unique [underlined] -- on a'),
('021.C.21','display','bottom brace','K={alpha in I | bar V cap E_alpha != empty i.e. corrected E_alpha cap dot V != empty}; Sigma_alpha+ est l’unique comp. de X setminus Sigma_alpha contenue dans X setminus V'),
('021.C.22','deletion','bottom corrected E_alpha','old V beneath live E_alpha'),
('021.C.23','drawing','upper condition brace','two meeting upper/lower runs'),
('021.C.24','drawing','corollary left rule','continuous slightly bent vertical rule'),
('021.C.25','drawing','bottom main brace','looped middle and lower continuation to sheet edge'),
('021.C.26','drawing','corollary union','bowl with pale upper-left retrace'),
('021.C.27','drawing','second K in K condition','K and transverse top run, qualified predecessor/retrace state')]:inv(*a)
for n,(suffix,loc,box,cr,g,dh) in enumerate(heads,28):inv('021.C.'+str(n),'drawing',loc,'complete Sigma head/body/index/raised-sign group',components=[g])
for ident in ('M01','M02','M03','M04','M05','M06'):
 d=next(x for x in D if x['id']=='C021-'+ident);inv('021.C.'+ident,'drawing',d['location'],d['reading'],'undetermined hand',[d['source_group']])
inv('021.C.archive','text','bottom left','archive sheet number 20; TeX comment only','undetermined hand')

doubts=[]
for d in D:
 if d.get('C_doubt_status')=='retained' or d.get('new_qualifier_on_firm_C') or d['id'].startswith('C021-H') or d['id'].startswith('C021-M') or d['id']=='C021-D03':
  doubts.append({'location':d['location'],'source_row_id':d.get('source_row_id'),'reading':d['reading'],'alternatives':d.get('role_alternatives',d['reading'].split('|')[1:] if '|' in d['reading'] else []),'confidence':d['confidence'],'reason':d['evidence'],'crop':d['readers_crop'],'difference_id':d['id'],'printed_qualifier':d.get('printed_qualifier',not d['id'].startswith('C021-H'))})

notation=[
{'location':'first equality','visible_sign':'two roofs, first without plus; doubly lowered zero','latex':r'\widehat{\Sigma}_{\alpha_0}\cap\widehat{\Sigma}_i^+','evidence':'crop18'},
{'location':'first equivalence','visible_sign':'i.e without final point','latex':'i.e','evidence':'crop02'},
{'location':'central U display','visible_sign':'crossed high left stalk on round union','latex':'literal C021-G03','evidence':'crop06'},
{'location':'marginal labels','visible_sign':'two sideways signed Sigmas, upright shaft/point between them','latex':'literal C021-G05','evidence':'crop08'},
{'location':'corollary exponent','visible_sign':'small raised loop','latex':r'\Pi_I^{\unsure{\circ|0}}','evidence':'crop12'},
{'location':'bottom set','visible_sign':'flat bar over first V, dot over second V','latex':r'\overline V;\dot V','evidence':'crop13'},
{'location':'end of proof and bottom condition','visible_sign':'cqfd. and comp. with terminal dots','latex':'cqfd.; comp.','evidence':'crops22,13'},
{'location':'all literal Sigma heads','visible_sign':'short upper runs and separately bent bodies','latex':'G01/G03/G04/G05/G06/G08/G09','evidence':'individual H01-H17 rows; first head-role qualifier at G01a'}]
notes={'page_content':"The author writes that alpha0 in K1 gives the two displayed empty intersections, then writes U=X setminus the union of the roofed Sigma_alpha+ with K=K1 union {i}. The proof ends with Sigma_i+ cap Sigma_alpha+ = empty and 'cqfd.'.",'corollary':r"The underlined 'Corollaire du lemme' calls the expression V=X\setminus\bigcup_{\alpha\in K}\widehat\Sigma_\alpha^+ unique, and gives K={alpha in I | bar V cap E_alpha != empty, i.e. E_alpha cap dot V != empty}. Its final written complement is X\setminus Sigma_alpha.",'author_own_uncertainty':[],'author_corrections':['cancelled Sigma_alpha under the upper K condition','cancelled impli/impl. before live signifie','V predecessor beneath the live E_alpha'],'title_date_page_counts':{'title':'Corollaire du lemme (underlined)','written_date':None,'manuscript_page_number':None,'archive_number':'20, comment only'},'mathematics_led_reading_decisions':'No expected mathematical expression supplied a missing stroke. The first roofed Sigma has no +; the final complement retains Sigma; the right alpha0/alpha remains qualified. No proof or mathematical check was performed.'}
S={'id':'SA01-K81-06','raw_source':json.loads(Path('packets/021/S_rows.json').read_text()),'scope':'broad scans015-022 proposal; its author viewed no scan','quoted_example_matches':[],'scan021_observations':[{'location':'bottom first V','reading':r'\overline V','ink':'separate horizontal upper run','crop':'crop13_bottom_brace.png','already_in_C':True,'already_in_H':True,'S_exact_example_match':False},{'locations':['first equality left','first equality right','upper U formula','central E_i formula','second inclusion','corollary V formula'],'reading':'six roofed Sigma occurrences','already_in_C':True,'already_in_H':True,'S_exact_example_match':False}],'decision':'No quoted S example matches a formula on this inspected page. The observed V bar and existing roofs are retained. Separately drawn Sigma head runs keep their local head/retrace-versus-rule uncertainty; S supplies no role or added closure bar.','current_witness_correction_claim':False}
report={'scan':'021','reader':'C','start_utc':(p/'start_utc.txt').read_text().strip(),'end_utc':None,'full_image_viewed':True,'halves_viewed':True,'halves_viewed_detail':['a','b'],'complete_visual_read':True,'differences':D,'actual_C_outcome_map':M,'actual_C_source_rows':15,'actual_C_local_parts':15,'actual_C_resolved_rows':7,'actual_C_retained_rows':8,'doubts':doubts,'inventory':inventory,'notes':notes,'notation':notation,'check_events':[],'crops':man['crops'],'S_coverage':S,'brief_feedback':['C slip table describes the middle index as alpha while current C.tex and actual doubtful row15 use alpha0|alpha; original categories and row identity retained separately.','Literal supported shapes can preserve the visible source while their glyph/head role remains open; graphical ownership and semantic candidates are given in the exact group catalog.'],'provenance':{'packet_files_read':['metadata.json','C.tex','H.tex','C_doubts.txt','C_notes.txt','C_inventory.json','S_rows.json','notation.md'],'C_notes_file_empty':True,'source_boundary':'Only scan021 packet/images; shared notation other-sheet entries are contextual only.','initial_text_output_truncation':'Initial combined cat output was truncated. Complete bounded rereads of all required files preceded the whole image.','image_delivery_failures':[],'successful_image_views':{'whole':1,'a':1,'b':1,'local_crops':22},'crop_count':22,'crop_retries':0,'same_target_recrops':0,'image_order':'whole, a, b; crops01-17; crops18-22','coordinate_processing':{'original_size':[1685,2362],'half_sizes':{'a':[1685,1261],'b':[1685,1261]},'lower_half_origin':[0,1101],'actual_task_necessary_mapping':'2362 - 1261 = 1101, used for the lower-half coordinate origin. Crop coordinates use original full-image units.','resizing':'Each crop enlarged to width2600 by PIL LANCZOS; proportional height rounded; autocontrast and UnsharpMask radius1.2 percent100 threshold3.','excluded_operations':'No pixel-difference, metric-fitting, alignment, curve-extrema, mathematical calculation, OCR, compilation, render, web, research or installation.'},'graphical_groups_file':'graphical_groups.json','count_policy':'Source-row outcome identities remain separate from physical correction counts. Child rows with parent_C/H_count retain raw component flags and receive zero additional count. New qualifiers on firm C are marked.','H_apparatus_classification':'H page20 is a source page label. Its right-diagram and corollary-border notes are apparatus and were read with the body; their prose is not invented manuscript wording. H note about the next lot and end-document command are excluded from manuscript collation.'}}
(p/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(p/'C_diff.patch').write_text(''.join(difflib.unified_diff(c.splitlines(True),tex.splitlines(True),fromfile='packets/021/C.tex',tofile='out/readers/021/C/reading.tex')))
(p/'H_diff.patch').write_text(''.join(difflib.unified_diff(h.splitlines(True),tex.splitlines(True),fromfile='packets/021/H.tex',tofile='out/readers/021/C/reading.tex')))
print('Complete report draft saved:',len(D),'local difference/audit rows;',len(inventory),'inventory entries; 15 source doubts mapped.')
