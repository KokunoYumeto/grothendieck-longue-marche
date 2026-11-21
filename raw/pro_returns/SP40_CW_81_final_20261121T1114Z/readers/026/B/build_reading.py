from pathlib import Path
import json, re, hashlib
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[3]
SCALE=.085
records=[]
fragments={}

def graphic(id,bbox,paths,nodes=(),reading='',candidates=(),crop=None,baseline=None,qual=False,role='',hand='his hand',components=None,extra=''):
    x0,y0,x1,y1=bbox
    base=(y1-3 if baseline is None else baseline)-y0
    lines=[f'% BEGIN {id}',f'% native origin full scan: ({x0},{y0}); x={SCALE}mm, y=-{SCALE}mm; baseline full y={y0+base}; fixed rectangle {x1-x0} by {y1-y0}.',f'% selected reading: {reading}']
    if candidates: lines.append('% complete candidates: '+' || '.join(candidates))
    lines.append(r'\begin{tikzpicture}[x=0.085mm,y=-0.085mm,baseline={(0,'+str(base)+r')},line cap=round,line join=round]')
    lines.append(r'\path[use as bounding box] (0,0) rectangle ('+str(x1-x0)+','+str(y1-y0)+');')
    for p in paths:
        lines.append(p)
    for node in nodes:
        x,y,tex,*opts=node
        opts=opts[0] if opts else ''
        lines.append(r'\node[anchor=base west,inner sep=0pt,outer sep=0pt'+(','+opts if opts else '')+'] at ('+str(x-x0)+','+str(y-y0)+') {'+tex+'};')
    if extra: lines.append(extra)
    lines += [r'\end{tikzpicture}',f'% END {id}']
    text='\n'.join(lines)+'\n'
    if qual: text='\\unsure{'+text+'}'
    fragments[id]=text
    records.append({'id':id,'bbox':list(bbox),'full_origin':[x0,y0],'native_units':'full-scan pixels; local (u,v)=(x-x0,y-y0)','coordinate_map':{'x_mm':SCALE,'y_mm':-SCALE,'baseline_full_y':y0+base,'fixed_rectangle':[x1-x0,y1-y0]},'reading':reading,'candidates':list(candidates),'role':role,'hand':hand,'crop':crop,'literal_source':text,'paths':paths,'nodes':nodes,'components':components or [],'qualifier_printed':qual,'drawing_status':'manual approximation from the once-displayed image; no rendering or metric validation'})
    return text

def path(points,width=.45,color='black',closed=False):
    # Points are explicit local pixel coordinates; conversion is not inferred from a template.
    s=' -- '.join(f'({x},{y})' for x,y in points)
    return r'\draw[line width='+str(width)+'pt'+(',draw='+color if color!='black' else '')+'] '+s+(' -- cycle;' if closed else ';')

def sigma(id,bbox,head,body,index='',upper='',crop='',joined=False,roof=None,old=None,ring=False,shared_index=False):
    x0,y0,x1,y1=bbox
    pp=[]
    if joined:
        pp.append(path(head+body,.45))
    else:
        pp.extend([path(head,.43),path(body,.46)])
    if roof: pp.append(path(roof,.5))
    label=r'\Sigma'+('_{'+index+'}' if index else '')+('^{'+upper+'}' if upper else '')
    if roof: label=r'\overline{'+label+'}'
    nodes=[]
    # Native node placements are explicitly fixed per local box, independent of text metrics.
    if index and not shared_index:
        if id in ['B026-S04','B026-S05','B026-S07']:
            w=x1-x0; h=y1-y0
            pp.append(path([(w-27,h-19),(w-18,h-22),(w-13,h-14),(w-24,h-10),(w-17,h-18),(w-9,h-9)],.9))
            nodes.append((x1-29,y1-1,'$\\phantom{\\scriptstyle '+index+'}$'))
            if id=='B026-S07':
                pp.append(r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (74,75) {$\unsure{\phantom{\alpha}}$};')
        else: nodes.append((x1-17,y1-1,'$\\scriptstyle '+index+'$'))
    if upper:
        if id=='B026-S05':
            pp.append(path([(17,15),(22,10),(26,16),(17,18),(26,19)],.9))
            nodes.append((x0+35,y0+29,'$\\scriptstyle \\alpha,\\unsure{\\circ|0|o}$'))
            nodes.append((x0+13,y0+17,'$\\phantom{\\deleted{\\unsure{\\alpha}}}$'))
        else: nodes.append((x1-25,y0+14,'$\\scriptstyle '+upper+'$'))
    cands=[label+' with '+('joined' if joined else 'detached')+' head/retrace']
    if not joined: cands.append(label+' with independent upper run')
    if old: cands=old
    return graphic(id,bbox,pp,nodes,reading=label,candidates=cands,crop=crop,baseline=y1-6,qual=(id in ['B026-S01','B026-S04','B026-S05','B026-S06','B026-S07']),role='glyph body and decorations; '+('locally joined head' if joined else 'upper-run role retained locally; first recurring qualifier on S01'),components=['head','body']+(['roof'] if roof else [])+(['index shared with foot'] if shared_index else []))

# Every head/body path below was selected independently from the prescribed half or the named one-time crop.
sigma('B026-S01',(600,288,677,346),[(7,16),(46,15)],[(8,23),(29,27),(39,31),(27,41),(7,46),(47,46)],r'\alpha',r'\alpha','01_family')
sigma('B026-S02',(762,823,871,884),[(8,15),(31,9),(58,7)],[(11,18),(45,23),(34,31),(8,46),(69,46),(84,51)],r'\alpha','','03_hemispheres')
sigma('B026-S03',(671,890,752,942),[(5,19),(43,16)],[(5,19),(30,23),(15,32),(5,43),(44,41)],r'\alpha',r'\alpha','04_interlinear',joined=True)
sigma('B026-S04',(823,881,890,939),[(7,20),(25,15)],[(4,25),(24,27),(10,38),(5,43),(35,43)],r'\deleted{\unsure{\alpha}}',r'\alpha','04_interlinear',old=[r'\Sigma_{\deleted{\alpha}}^{\alpha}; lower predecessor glyph qualified'])
sigma('B026-S05',(958,866,1040,932),[(8,27),(28,24)],[(7,33),(24,34),(11,43),(7,47),(35,47)],r'\deleted{\unsure{\alpha}}',r'\deleted{\unsure{\alpha}}\alpha,\unsure{\circ|0|o}','04_interlinear',old=[r'\Sigma_{\deleted{\alpha}}^{\deleted{\alpha}\alpha,\circ}',r'\Sigma_{\deleted{\alpha}}^{\deleted{\alpha}\alpha,0}',r'\Sigma_{\deleted{\alpha}}^{\deleted{\alpha}\alpha,o}'])
sigma('B026-S06',(1050,935,1122,991),[(4,9),(30,20),(37,15)],[(10,18),(31,26),(27,39),(5,41),(43,39)],r'\alpha','','04_interlinear',old=[r'\deleted{\Sigma_{\alpha}}',r'\deleted{les}'])
sigma('B026-S07',(782,1000,886,1075),[(8,38),(54,32)],[(8,38),(38,47),(9,61),(58,59)],r'\unsure{\deleted{\alpha}|\alpha}',r'\alpha','05_si_condition',joined=True,old=[r'\Sigma_{\deleted{\alpha}}^{\alpha}',r'\Sigma_{\alpha}^{\alpha}'])
sigma('B026-S08',(757,1095,886,1167),[(10,31),(57,24)],[(13,34),(45,41),(13,58),(69,56)],r'\alpha',r'\alpha,\circ','06_connexe_correction')
sigma('B026-S09',(475,1222,613,1303),[(8,28),(52,24)],[(10,32),(42,41),(12,61),(1,66),(59,63)],'',r'\alpha,\circ','08_barred_formulas',roof=[(17,15),(79,12),(124,7)])
sigma('B026-S10',(1095,1169,1248,1240),[(17,28),(59,24)],[(18,32),(47,38),(21,53),(9,61),(60,59)],'',r'\alpha,\circ','08_barred_formulas',roof=[(49,9),(96,7),(140,8)])
sigma('B026-S11',(1374,1152,1517,1223),[(13,33),(58,31)],[(14,37),(42,44),(16,60),(5,64),(65,62)],'',r'\alpha,\circ','08_barred_formulas',roof=[(12,13),(72,10),(134,10)])
sigma('B026-S12',(1532,1163,1641,1238),[(10,28),(48,26)],[(12,33),(39,42),(11,57),(8,60),(53,59)],'',r'\alpha,\circ','08_barred_formulas')
sigma('B026-S13',(406,1356,524,1421),[(11,27),(45,18)],[(9,32),(39,30),(43,35),(13,53),(8,58),(48,55)],'',r'\alpha,\circ','09_parenthesis_end')
sigma('B026-S14',(448,1467,575,1524),[(11,19),(48,16)],[(12,24),(34,26),(40,30),(16,45),(9,49),(50,44)],'',r'\unsure{-,\circ|\alpha,\circ|-\alpha,\circ}','09_parenthesis_end')
sigma('B026-S15',(115,1645,188,1718),[(9,20),(41,16)],[(9,20),(35,23),(14,31),(34,35),(13,58),(45,58)],'1','+','10_pairs_correction',joined=True)
sigma('B026-S16',(188,1645,255,1718),[(8,16),(29,18)],[(7,23),(27,29),(24,39),(10,56),(38,56)],'1','-','10_pairs_correction')
sigma('B026-S17',(329,1633,407,1700),[(10,14),(37,12)],[(9,25),(36,27),(24,44),(17,53),(43,51)],'2','+','10_pairs_correction')
sigma('B026-S18',(403,1632,470,1700),[(8,18),(34,18)],[(9,24),(34,27),(23,42),(14,52),(38,50)],'2','-','10_pairs_correction')
sigma('B026-S19',(925,1730,1022,1804),[(11,28),(52,25)],[(11,34),(48,40),(27,57),(10,63),(59,64)],'1','+','12_distinctes_insertion')
sigma('B026-S20',(1413,1710,1503,1780),[(10,23),(47,19)],[(13,29),(44,34),(30,44),(11,53),(59,56)],'2','+','half_b')
sigma('B026-S21',(646,1941,751,2010),[(11,24),(48,20)],[(14,29),(41,33),(17,49),(6,55),(50,53)],'1','+','13_first_display')
sigma('B026-S22',(804,1934,900,2003),[(7,24),(46,25)],[(6,31),(41,34),(24,50),(9,55),(48,54)],'2','+','13_first_display')
sigma('B026-S23',(651,2085,744,2158),[(9,29),(50,23)],[(10,35),(40,37),(35,45),(10,62),(63,56),(63,66)],'1','+','14_first_bottom_row',shared_index=True)
sigma('B026-S24',(792,2086,886,2153),[(8,21),(32,19)],[(7,27),(30,29),(23,40),(13,51),(39,50)],'2','-','14_first_bottom_row')
sigma('B026-S25',(1129,2061,1226,2133),[(12,26),(52,20)],[(11,33),(46,35),(40,42),(8,59),(57,59)],'1','+','14_first_bottom_row')
sigma('B026-S26',(1251,2058,1350,2126),[(10,26),(39,26)],[(7,32),(34,37),(20,48),(12,59),(47,59)],'2','-','14_first_bottom_row')
sigma('B026-S27',(1387,2058,1491,2125),[(14,26),(49,22)],[(14,29),(46,34),(27,47),(6,59),(57,54)],'1','+','14_first_bottom_row')
sigma('B026-S28',(641,2172,748,2246),[(10,22),(56,15)],[(11,28),(44,30),(46,35),(20,56),(7,64),(63,58)],'2','+','15_second_bottom_row')
sigma('B026-S29',(806,2170,899,2243),[(9,22),(42,14)],[(7,26),(39,30),(21,46),(7,58),(46,56)],'1','-','15_second_bottom_row')
sigma('B026-S30',(1136,2159,1236,2230),[(10,24),(49,16)],[(11,28),(44,33),(29,45),(8,57),(57,54)],'2','+','15_second_bottom_row')
sigma('B026-S31',(1265,2156,1363,2227),[(10,31),(42,27)],[(10,31),(41,34),(36,44),(15,56),(65,54),(70,67)],'1','-','15_second_bottom_row',joined=True,shared_index=True)
sigma('B026-S32',(1382,2155,1482,2226),[(10,26),(41,19)],[(10,31),(37,33),(28,41),(6,54),(43,50)],'2','+','15_second_bottom_row')
sigma('B026-S33',(528,2264,628,2334),[(7,21),(55,17)],[(17,24),(39,30),(34,37),(9,57),(61,53)],'12','','16_final_row',joined=True)
sigma('B026-S34',(652,2261,749,2325),[(10,14),(53,14)],[(8,20),(44,28),(35,35),(5,47),(56,45)],'1','-','16_final_row')
sigma('B026-S35',(783,2259,887,2322),[(9,12),(45,9)],[(10,19),(34,22),(38,27),(12,46),(42,43)],'2','-','16_final_row')
sigma('B026-S36',(1154,2255,1253,2322),[(10,12),(49,10)],[(10,12),(43,21),(41,27),(10,45),(7,50),(57,53)],'1','-','16_final_row',joined=True)
sigma('B026-S37',(1264,2256,1353,2321),[(8,13),(37,8),(41,10),(9,16)],[(9,20),(34,22),(20,40),(12,45),(36,46)],'2','-','16_final_row')

# Graphic groups for independently ambiguous marks and physical guides.
graphic('B026-EFAM',(744,319,781,348),[path([(21,7),(16,4),(10,6),(9,12),(16,14),(10,17),(8,27),(23,29),(33,23)],.6),path([(9,16),(15,24),(25,27)],.6)],reading=r'\mathcal E',candidates=[r'\mathcal E',r'\mathscr E',r'\varepsilon'],crop='01_family',qual=True,role='family-index glyph; alphabet unresolved')
graphic('B026-HSTART',(281,851,655,937),[path([(7,32),(43,31)],.5)],[(285,908,r'\rlap{hémisphères}\phantom{\deleted{hémisphères}}')],reading='live hémisphères primary, cancelled hémisphères alternative',candidates=['hémisphères',r'\deleted{hémisphères}'],crop='03_hemispheres',qual=True,role='short transverse run at initial h; cancellation scope unresolved')
graphic('B026-GDE',(1324,772,1595,904),[r'\draw[line width=.45pt] (97,82) .. controls (109,56) and (143,39) .. (177,25);'],[(1334,865,'(et'),(1425,798,r'\inserted{de}'),(1450,867,'plus,')],reading='(et inserted de plus, with curved guide',candidates=['de attached between et and plus'],crop='03_hemispheres',role='insertion guide',baseline=884)
graphic('B026-GEQ',(640,855,1415,1015),[r'\draw[line width=.45pt] (315,66) .. controls (318,88) and (233,94) .. (151,96) .. controls (102,97) and (94,113) .. (105,145);'],[(671,936,r'\inserted{$'+fragments['B026-S03']+r'\text{ et }'+fragments['B026-S04']+r'\setminus E='+fragments['B026-S05']+'$}'),(761,979,'connexes'),(1050,984,r'\rlap{'+fragments['B026-S06']+r'}\phantom{\deleted{\unsure{$\Sigma_\alpha$|les}}}'),(1168,966,'et où')],reading=r'inserted Sigma_alpha^alpha et Sigma_deleted-alpha^alpha setminus E = Sigma_deleted-alpha^(deleted-alpha alpha,circle); connexes; deleted Sigma_alpha/les; et où',candidates=[r'\deleted{\Sigma_\alpha} after connexes',r'\deleted{les} after connexes'],crop='04_interlinear',role='interlinear insertion, bent guide, cancelled trailing group and following et où',baseline=979,extra=r'\draw[line width=.5pt] (413,84)--(462,120);'+ '\n'+r'\draw[line width=.45pt] (418,124)--(452,90);')
graphic('B026-REL1',(1349,1003,1392,1050),[path([(25,5),(24,32)],.45),path([(8,19),(37,17)],.45),path([(29,8),(38,10)],.35)],reading=r'\ne',candidates=[r'\ne',r'+'],crop='05_si_condition',qual=True,role='complete relation with short upper-right run, long middle run and slanted upright')
graphic('B026-GCONN',(548,1057,1125,1194),[r'\draw[line width=.45pt] (89,110) .. controls (70,71) and (117,63) .. (252,40) .. controls (330,28) and (400,26) .. (418,17);',path([(90,110),(257,98),(420,81),(553,69)],.65)],[(559,1160,'si'),(600,1105,r'\inserted{X connexe, \deleted{et}}'),(647,1171,r'\rlap{les $'+fragments['B026-S08']+r'$ connexes}\phantom{\deleted{les $\Sigma_\alpha^{\alpha,\circ}$ connexes}}')],reading=r'si deleted les Sigma_alpha^(alpha,circle) connexes; inserted X connexe, deleted et',candidates=[r'si \deleted{les \Sigma_\alpha^{\alpha,\circ} connexes}, \inserted{X connexe, \deleted{et}}'],crop='06_connexe_correction',role='complete correction group with old clause and replacement; curved upper guide and lower crossing',baseline=1171)
graphic('B026-GAUSS',(1457,1062,1648,1125),[r'\draw[line width=.5pt] (9,46) .. controls (42,39) and (60,48) .. (86,42) .. controls (126,47) and (155,42) .. (181,49);'],[(1463,1113,r'\rlap{\unsure{aussitôt|aussitot}}\phantom{\deleted{\unsure{aussitôt|aussitot}}}')],reading=r'\deleted{\unsure{aussitôt|aussitot}}',candidates=[r'\deleted{aussitôt}',r'\deleted{aussitot}'],crop='06_connexe_correction',role='readable cancelled word, accent unresolved',baseline=1113)
graphic('B026-M02',(1169,1177,1192,1193),[path([(6,6),(12,8)],.3,'gray')],reading='short detached oblique trace below the first parenthetical closure rule',candidates=['trace attached to upper alpha','trace attached to closure rule','independent trace'],crop='08_barred_formulas',qual=True,role='attachment and surface origin unresolved',hand='undetermined hand')
graphic('B026-M03',(440,1270,475,1318),[r'\draw[gray,line width=.3pt] (13,6) .. controls (20,14) and (27,23) .. (27,29) .. controls (29,36) and (17,42) .. (8,41);',r'\draw[gray,line width=.2pt] (10,4)--(14,10);'],reading='pale right-bowing open arc with short upper entry',candidates=['pale graphical arc; character, role, hand and surface origin unestablished'],crop='17_pale_arc',qual=True,role='unattached pale shape, no character supplied',hand='undetermined hand')
graphic('B026-ATWO',(905,1349,930,1383),[r'\fill (12,10) ellipse (1.2 and 2);',r'\fill (10,24) ellipse (1.3 and 2);'],reading='à primary; colon alternative',candidates=['à',':'],crop='09_parenthesis_end',qual=True,role='two vertically separated marks before la; lexical/punctuation reading qualified')
graphic('B026-M04',(714,1403,732,1427),[r'\fill[gray] (4,5) ellipse (.7 and 1.1);',r'\fill[gray] (7,11) ellipse (.5 and 1);',r'\fill[gray] (10,17) ellipse (.7 and 1.2);'],reading='three small descending flecks below peut',candidates=['three graphical flecks; role, attachment, hand and surface origin unestablished'],crop='09_parenthesis_end',qual=True,role='unattached specks preserved without character interpretation',hand='undetermined hand')
graphic('B026-DELIM2',(314,1635,339,1693),[r'\draw[line width=.45pt] (20,5).. controls (4,1) and (5,17)..(5,36).. controls (4,55) and (11,55)..(18,51);'],reading='[ primary; ( alternative',candidates=['[','('],crop='10_pairs_correction',qual=True,role='complete second left delimiter; upper cap and rounded lower return')
graphic('B026-GPAIRS',(90,1625,773,1772),[r'\draw[line width=.45pt] (137,120).. controls (161,75) and (198,80)..(264,77).. controls (351,84) and (410,61)..(437,61).. controls (456,72) and (480,66)..(502,63);',path([(421,57),(460,30),(483,47),(515,23),(543,39),(584,17)],.55),path([(429,73),(603,37)],.45)],[(100,1712,r'$\{'+fragments['B026-S15']+','+fragments['B026-S16']+r'\},'+fragments['B026-DELIM2']+fragments['B026-S17']+','+fragments['B026-S18']+r'\}$'),(508,1679,r'\rlap{distinctes}\phantom{\deleted{distinctes}}'),(276,1740,r'\inserted{de $X$,}')],reading='both binary pairs, second left bracket qualified; deleted distinctes, inserted de X, and connecting guide',candidates=[r'\{\Sigma_1^+,\Sigma_1^-\},[\Sigma_2^+,\Sigma_2^-\} \deleted{distinctes} \inserted{de X,}',r'\{\Sigma_1^+,\Sigma_1^-\},(\Sigma_2^+,\Sigma_2^-\} \deleted{distinctes} \inserted{de X,}'],crop='10_pairs_correction',role='complete pair/correction group; guide and cancellation paths retain separate ownership',baseline=1712)
graphic('B026-GADJ',(1171,1617,1642,1711),[r'\draw[line width=.45pt] (60,67)--(453,51);',r'\draw[line width=.5pt] (159,26)..controls(163,44)and(164,74)..(172,79)..controls(182,73)and(196,57)..(205,39);',r'\draw[line width=.5pt] (159,27)..controls(180,15)and(210,18)..(208,30)..controls(205,40)and(176,35)..(161,28);',r'\fill (415,65) ellipse (1.3 and 1.3);',r'\fill (410,72) ellipse (1.3 and 1.3);'],[(1182,1666,'non'),(1382,1666,r'\unsure{anachées|enchées|arallèles|anachees|enchees|aralleles}')],reading='non panachées primary with complete lexical/accent alternatives, single underline, long p return and two detached points below right end',candidates=['non panachées','non penchées','non parallèles','non panachees','non penchees','non paralleles'],crop='11_adjective',role='complete underlined adjective; lower two points have unestablished role, hand and surface origin',baseline=1670,components=['word span','underline','p descending return','two detached lower points'])
graphic('B026-GDIST',(275,1685,1015,1886),[r'\draw[line width=.45pt] (96,170)..controls(82,132)and(143,119)..(253,104)..controls(393,98)and(568,66)..(653,54);',r'\draw[line width=.45pt] (289,85)--(470,54);'],[(286,1854,'si'),(372,1786,r'\inserted{elles sont \uline{distinctes}, et si}'),(390,1854,'on peut trouver'),(925,1800,'$'+fragments['B026-S19']+'$')],reading='base si, inserted elles sont distinctes, et si, on peut trouver Sigma1plus',candidates=['si inserted elles sont distinctes, et si on peut trouver Sigma_1^+'],crop='12_distinctes_insertion',role='complete raised insertion with curved guide; distinctes underline is separate',baseline=1854)
graphic('B026-GQDESC',(775,1666,904,1764),[r'\draw[line width=.35pt] (15,10)..controls(4,4)and(0,13)..(7,22)..controls(13,25)and(21,18)..(16,12);',r'\draw[line width=.35pt] (16,13)..controls(25,38)and(27,66)..(33,90);'],[(804,1697,"u'elles")],reading="qu'elles with long q descender",candidates=["qu'elles; descender belongs to q and touches insertion-guide neighbourhood"],crop='12_distinctes_insertion',role='word-bearing group owns qu’elles; q descender remains once, separate from guide',baseline=1697)
graphic('B026-CAP1',(760,1974,798,2004),[path([(5,23),(15,9),(28,20)],.5),r'\fill[gray] (33,23) ellipse (1 and 1.4);'],reading=r'\cap with angular arch and detached lower-right point',candidates=[r'\cap; point as terminal continuation',r'\cap; independent neighbouring point'],crop='13_first_display',qual=True,role='point attachment and hand unresolved',components=['pointed arch','detached point'])
graphic('B026-E1',(1318,1910,1389,1974),[path([(27,11),(34,8),(43,13)],.3),path([(15,20),(10,53),(37,52)],.4),path([(13,39),(40,31)],.4)],[(1373,1970,'$\\scriptstyle1$')],reading=r'E_1 with detached upper curve',candidates=[r'E_1 with detached top arm',r'E_1 with independent upper curve'],crop='13_first_display',qual=True,role='upper-curve role qualified; glyph and index his hand; independent-curve candidate undetermined hand for upper curve')
graphic('B026-E2',(1440,1897,1518,1965),[r'\draw[line width=.3pt] (19,15)..controls(30,5)and(41,7)..(46,15);',path([(12,16),(6,57),(35,56)],.4),path([(12,44),(40,39)],.4)],[(1491,1963,'$\\scriptstyle2$')],reading=r'E_2 with detached upper curve',candidates=[r'E_2 with detached top arm',r'E_2 with independent upper curve'],crop='13_first_display',role='later locally qualified upper curve, first printed qualifier at E1')
graphic('B026-ARED',(408,2098,429,2121),[r'\fill (7,8)--(13,6)--(16,9)--(11,12)--(7,11)--cycle;'],reading='a primary; detached point alternative',candidates=['a in complete on a alors','uninterpreted point in complete on [point] alors'],crop='14_first_bottom_row',qual=True,role='reduced lexical shape or independent point; latter hand/role/attachment unresolved')
graphic('B026-INCL1',(748,2099,792,2143),[r'\draw[line width=.7pt] (36,10)..controls(7,6)and(4,19)..(13,27)..controls(21,32)and(29,30)..(40,30);',path([(12,23),(7,34)],.35),path([(10,21),(24,30)],.4)],reading=r'\subset primary; deleted cap then subset alternative',candidates=[r'\subset',r'\deleted{\cap}\subset'],crop='14_first_bottom_row',qual=True,role='retraced inclusion/cancelled predecessor state remains unresolved')
graphic('B026-GNEDEL',(898,2081,988,2151),[path([(6,38),(52,26),(22,46),(57,38)],.9),path([(12,48),(62,16)],.5),r'\draw[line width=.5pt] (66,27)..controls(47,21)and(42,48)..(64,43)..controls(78,38)and(71,22)..(66,27);',path([(51,62),(86,5)],.65),path([(52,46),(80,23)],.55)],reading=r'\deleted{\ne\varnothing}',candidates=[r'\deleted{\ne\varnothing}'],crop='14_first_bottom_row',role='cancelled inequality and slashed oval, resolved glyphs; exact overmarks retained',baseline=2140)
graphic('B026-DEF',(607,2244,648,2290),[r'\draw[line width=.4pt] (3,28)..controls(9,9)and(19,4)..(18,17)..controls(14,27)and(2,34)..(1,29);',r'\draw[line width=.4pt] (13,28)..controls(19,23)and(21,24)..(20,28)..controls(19,35)and(29,31)..(33,24);',path([(34,4),(33,43)],.5),path([(28,31),(38,27)],.4),path([(24,16),(26,13)],.3)],reading='déf primary; def with separate upper trace alternative',candidates=['déf','def plus detached upper trace'],crop='16_final_row',qual=True,role='complete label, small upper mark accent/independent trace uncertain',baseline=2282)
graphic('B026-M06',(744,2310,765,2332),[path([(7,7),(9,11)],.25,'gray')],reading='small separate slant below first final-row intersection',candidates=['independent slant','detached continuation of intersection'],crop='16_final_row',qual=True,role='attachment, hand and surface origin unresolved',hand='undetermined hand')
graphic('B026-NEFINAL',(1344,2274,1394,2318),[path([(23,4),(13,39)],.5),path([(5,20),(38,13)],.4),path([(3,28),(37,26)],.5),r'\fill (43,26) ellipse (1 and 1);'],reading=r'\ne with separated dot at right of lower run',candidates=[r'\ne with detached endpoint',r'\ne with independent adjacent point'],crop='16_final_row',qual=True,role='complete relation; small endpoint attachment unresolved')

# Diagram is a genuine tikz-cd object. Its literal overlay uses a declared fixed local origin.
diag=r'''% BEGIN B026-DIAG
% Native overlay coordinates: pixels of the rotated native crop07, relative to its left endpoint.
% Original crop (38,950,265,1375), PIL rotation -52 degrees expanded; see crop_plan.json.
% Overlay x=.10mm, y=-.10mm; outer +52-degree rotation restores the observed page slant.
% Crossed label candidates: deleted E | deleted B | deleted Sigma.
% Lower E candidates: E_alpha | E with hooked lower-arm return; the shared stroke is drawn once.
% M01: the detached dot below the connector has undetermined hand, role, attachment and surface origin.
\reversemarginpar\margin{\diagram{\rotatebox{52}{\begin{tikzcd}[ampersand replacement=\&,column sep=14.2mm,execute at end picture={
\begin{scope}[shift={(bLeft.center)},x=.10mm,y=-.10mm,line cap=round,line join=round]
\draw[line width=.4pt] (0,0)..controls(42,3)and(91,4)..(142,1.6);
\fill (0,0) circle(4.8); \fill (142,1.6) ellipse(5.8 and 4.6);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at(40,-81){diagramme};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at(58,-15){\phantom{\deleted{\unsure{$E$|$B$|$\Sigma$}}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at(58,-15){\unsure{\begin{tikzpicture}[x=.10mm,y=-.10mm,baseline={(0,0)}]
\path[use as bounding box](0,-37)rectangle(45,0);
\draw[line width=.6pt](8,-32)--(40,-33)--(42,-25)--(30,-14)--(6,-7)--(32,-8);
\draw[line width=.6pt](10,-31)--(4,-2)--(19,-1)--(32,-28);
\draw[line width=.6pt](2,-11)--(36,-28);\draw[line width=.6pt](1,-5)--(34,-6);
\end{tikzpicture}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at(34,9){\unsure{\begin{tikzpicture}[x=.10mm,y=-.10mm,baseline={(0,0)}]\path[use as bounding box](0,0)rectangle(5,5);\fill(2,2)circle(1.1);\end{tikzpicture}}};
% Lower label is literal: each short head, body, relation and shared E/alpha return occurs once.
\draw[line width=.4pt](-55,23)--(-28,23);
\draw[line width=.4pt](-53,27)--(-35,30)--(-41,37)--(-63,48)--(-35,46);
\draw[line width=.4pt](-25,26)--(-14,27);
\draw[line width=.6pt](5,25)..controls(31,24)and(40,42)..(7,48);
\draw[line width=.6pt](5,44)--(30,45);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at(53,47){\unsure{\begin{tikzpicture}[x=.10mm,y=-.10mm,baseline={(0,29)}]
\path[use as bounding box](0,0)rectangle(45,35);
\draw[line width=.5pt](13,5)..controls(29,-1)and(40,0)..(40,4);
\draw[line width=.5pt](9,9)--(0,29)--(34,29)..controls(43,22)and(43,23)..(41,30)..controls(30,38)and(24,32)..(27,30)--(43,33);
\draw[line width=.5pt](9,21)--(33,17);
\end{tikzpicture}}};
\draw[line width=.6pt](125,20)..controls(105,24)and(101,38)..(112,39)--(130,39);
\draw[line width=.4pt](148,20)--(177,19);
\draw[line width=.45pt](149,24)--(166,27)--(159,34)--(142,47)--(174,46);
\draw[line width=.5pt](188,20)--(188,33);\draw[line width=.5pt](180,26)--(195,26);
\end{scope}
}]
|[alias=bLeft]|\phantom{\bullet}\&\phantom{\bullet}
\end{tikzcd}}}}\normalmarginpar%
% END B026-DIAG
'''
fragments['B026-DIAG']=diag
records.append({'id':'B026-DIAG','bbox':[38,950,265,1375],'native_units':'pixels of expanded rotated crop07 before resize','full_origin':[38,950],'coordinate_map':{'rotation_degrees':-52,'display_rotation_degrees':52,'overlay_origin':'left endpoint in rotated native crop','x_mm':.10,'y_mm':-.10},'reading':'diagramme; two filled endpoints and connector; deleted E/B/Sigma; Sigma^- superset E_alpha/E subset Sigma^+; detached point','candidates':[r'\deleted E',r'\deleted B',r'\deleted\Sigma',r'E_\alpha',r'E with hooked lower-arm return'],'crop':'07_margin_diagram','literal_source':diag,'paths':'literal execute-at-end overlay in source','nodes':'two phantom diagram cells; all visible points and labels owned by overlay','components':['word diagramme','two filled vertices','bowed connector','crossed upper label','lower label','M01 detached point'],'hand':'his hand for diagram; detached point undetermined','role':'marginal diagram; crossed-glyph and lower-tail readings retained locally; detached-point role unresolved','qualifier_printed':True,'drawing_status':'manual approximation, no metric/render validation'})

# Complete fixed-origin groups keep nearby marks at their observed vertical positions.
graphic('B026-GMAIN',(440,1222,613,1318),[],[(475,1297,'$'+fragments['B026-S09']+'$'),(440,1315,fragments['B026-M03'])],reading='main barred Sigma with the separate pale arc to its left',candidates=['barred Sigma and independent pale arc; arc character, role, hand and surface origin unresolved'],crop='08_barred_formulas',role='complete source-coordinate group; S09 and M03 occur once',baseline=1297)
graphic('B026-GROOF10',(1095,1169,1248,1240),[],[(1095,1234,'$'+fragments['B026-S10']+'$'),(1169,1190,fragments['B026-M02'])],reading='first parenthetical barred Sigma and small detached trace below its roof',candidates=['barred Sigma; trace attached to alpha','barred Sigma; trace attached to closure rule','barred Sigma; independent trace'],crop='08_barred_formulas',role='complete source-coordinate group; S10 and M02 occur once',baseline=1234)
graphic('B026-GPEUT',(655,1345,750,1438),[],[(660,1390,'peut'),(714,1424,fragments['B026-M04'])],reading='peut with three separate flecks below it',candidates=['peut; flecks with unestablished role, attachment, hand and surface origin'],crop='09_parenthesis_end',role='word-bearing group owns peut exactly once and positions M04 below it',baseline=1390)
graphic('B026-CAPFINAL',(744,2286,795,2334),[path([(19,20),(28,7),(42,18)],.45)],[(744,2329,fragments['B026-M06'])],reading='first final-row intersection arch and the separate low-left slant',candidates=['intersection arch with detached continuation','intersection arch with independent low-left slant'],crop='16_final_row',role='complete relation/mark group; M06 remains individually qualified and occurs once',baseline=2310)
F=lambda n:fragments['B026-'+n]
tex=r'''\scanpage{26}
Soit $X$ un ens. Une \uline{décomposition binaire} de $X$ est un ens de deux parties de $X$
\[
('''+F('S01')+r''')_{\alpha\in '''+F('EFAM')+r'''}\qquad(\text{les ``hémisphères''})
\]
dont la réunion est $X$, et dont \deleted{l'intersection} aucune n'est contenue dans l'autre -- on désigne par $E$ (``équateur'') l'intersection (on n'exclut pas qu'elle soit vide). Quand $X$ est un espace topologique, on s'intéresse au cas où les
'''+F('HSTART')+' $'+F('S02')+r'''$ sont fermés,
'''+F('GDE')+r''' le plus souvent,
'''+F('GEQ')+r''' $E\ne\varnothing$); si les $'''+F('S07')+r'''$ connexes et $E'''+F('REL1')+r'''\varnothing$, $X$ est connexe,
'''+F('GCONN')+r''', on conclut
'''+F('GAUSS')+r''' que
% B026-M03 is the independent pale arc immediately to the left of the following formula.
$'''+F('GMAIN')+r'''\cap E\ne\varnothing$
% margin note written sideways
'''+F('DIAG')+r'''(car $'''+F('GROOF10')+r'''\cap E='''+F('S11')+r'''\setminus '''+F('S12')+r'''$, et $'''+F('S13')+r'''$ ne '''+F('GPEUT')+r''' être '''+F('ATWO')+r''' la fois ouvert et fermé car $'''+F('S14')+r'''$, est un ouvert $\ne\varnothing$ et $\ne X$)

Considérons deux décompositions binaires
'''+F('GPAIRS')+r''' on dit '''+F('GQDESC')+r''' sont
'''+F('GADJ')+' '+F('GDIST')+r''' dans l'une, $'''+F('S20')+r'''$ dans l'autre, tels que
\[
'''+F('S21')+F('CAP1')+F('S22')+r'''=\varnothing\qquad(\text{d'où }'''+F('E1')+r'''\cap '''+F('E2')+r'''=\varnothing)
\]
on '''+F('ARED')+r''' alors
\[
\begin{aligned}
'''+F('S23')+'&'+F('INCL1')+F('S24')+' '+F('GNEDEL')+r'''\quad\text{i.e.}\quad'''+F('S25')+r'''\cap'''+F('S26')+'='+F('S27')+r'''\\
'''+F('S28')+r'''&\subset'''+F('S29')+r'''\qquad\text{\unsure{ie|i.e.|i.e}}\quad'''+F('S30')+r'''\cap'''+F('S31')+'='+F('S32')+r'''\\
'''+F('S33')+r'''&\overset{\text{'''+F('DEF')+r'''}}{=}'''+F('S34')+F('CAPFINAL')+F('S35')+r'''\supset E_1\cup E_2,\quad'''+F('S36')+r'''\cap'''+F('S37')+F('NEFINAL')+r'''\varnothing
\end{aligned}
\]
% archive sheet number: 25
'''
(ROOT/'reading.tex').write_text(tex)
(ROOT/'graphic_records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('reading.tex bytes',len(tex.encode()),'graphic records',len(records))
