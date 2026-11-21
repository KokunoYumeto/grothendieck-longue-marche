from pathlib import Path
import json, re, hashlib

ROOT=Path(__file__).resolve().parent
groups={}
def block(ident,body,**meta):
    groups[ident]=dict(id=ident,**meta)
    return '% BEGIN '+ident+'\n'+body+'\n% END '+ident+'\n'

def picture(body,bbox,baseline=None,qualified=False,unit='0.025em'):
    x0,y0,x1,y1=bbox
    if baseline is None: baseline=y1-4
    t=(r'\begin{tikzpicture}[x='+unit+',y=-'+unit+r',baseline=(base),line cap=round,line join=round]'+'\n'
       +r'\coordinate (base) at (0,'+str(baseline-y0)+');\n'
       +r'\path[use as bounding box] (0,0) rectangle ('+str(x1-x0)+','+str(y1-y0)+');\n'
       +r'\begin{scope}[shift={('+str(-x0)+','+str(-y0)+')}]\n'
       +body+'\n'+r'\end{scope}'+'\n'+r'\end{tikzpicture}')
    return r'\unsure{'+t+'}' if qualified else t

def node(x,y,text,math=False,size=''):
    return r'\node[anchor=base west,inner sep=0pt,outer sep=0pt'+(',font='+size if size else '')+'] at ('+str(x)+','+str(y)+') {'+('$'+text+'$' if math else text)+'};'

def draw(path,width='0.45pt',gray=None):
    return r'\draw[line width='+width+(',black!'+str(gray) if gray else '')+'] '+path+';'

S={}
# Each body rectangle and head connection was read at its own half/crop locus.
# Paths are manual approximations in original-scan pixel units, not extracted contours.
specs=[
('S01',[602,290,686,346],[606,305,648,333],r'\alpha',r'\alpha','detached','02_family',True),
('S02',[765,824,866,886],[771,834,837,872],r'\alpha',None,'detached','04_inserted_formula',False),
('S03',[672,892,752,942],[678,909,720,933],r'\alpha',r'\alpha','joined','04_inserted_formula',False),
('S04',[824,886,890,939],[831,902,856,925],None,r'\alpha','detached','04_inserted_formula',True),
('S05',[959,874,1041,930],[963,896,988,920],None,r'\alpha,\unsure{0|\circ|o}','detached','04_inserted_formula',True),
('S06',[1048,936,1117,991],[1058,948,1090,979],r'\alpha',None,'joined','04_inserted_formula',False),
('S07',[785,1001,886,1072],[792,1035,836,1061],None,r'\alpha','joined','05_following_si',True),
('S08',[767,1106,879,1166],[776,1125,822,1152],r'\alpha',r'\alpha,0','joined','06_corrected_connexe',False),
('S09',[472,1227,610,1296],[484,1249,526,1288],None,r'\alpha,0','detached','half_b',False),
('S10',[1097,1173,1242,1239],[1110,1193,1156,1228],None,r'\alpha,0','detached','half_b',False),
('S11',[1373,1158,1514,1220],[1387,1178,1432,1211],None,r'\alpha,0','detached','half_b',False),
('S12',[1535,1171,1644,1224],[1543,1183,1588,1214],None,r'\alpha,0','joined','half_b',False),
('S13',[408,1367,528,1423],[418,1380,458,1412],None,r'\alpha,0','detached','09_parenthetic_prose',False),
('S14',[451,1471,580,1527],[460,1488,501,1514],None,r'\unsure{-,0|\alpha,0|-\alpha,0}','detached','10_parenthetic_end',False),
('S17',[115,1651,180,1715],[122,1667,159,1704],'1','+','joined','12_pairs_and_guides',False),
('S18',[190,1648,253,1710],[200,1665,233,1700],'1','-','detached','12_pairs_and_guides',False),
('S19',[330,1636,401,1694],[338,1650,374,1681],'2','+','detached','12_pairs_and_guides',False),
('S20',[407,1634,468,1689],[415,1649,450,1678],'2','-','detached','12_pairs_and_guides',False),
('S21',[927,1744,1016,1806],[937,1761,981,1795],'1','+','detached','half_b',False),
('S22',[1412,1720,1510,1780],[1425,1736,1471,1768],'2','+','detached','half_b',False),
('S23',[648,1947,745,2011],[658,1967,698,1999],'1','+','detached','half_b',False),
('S24',[804,1947,906,2007],[814,1967,855,1994],'2','+','detached','half_b',False),
('S25',[648,2097,743,2160],[658,2117,710,2148],'1','+','detached','14_first_lower_relation',False),
('S26',[790,2089,884,2145],[801,2106,841,2134],'2','-','detached','14_first_lower_relation',False),
('S27',[1132,2074,1230,2139],[1142,2090,1188,2127],'1','+','detached','half_b',False),
('S28',[1252,2076,1348,2133],[1264,2090,1306,2120],'2','-','detached','half_b',False),
('S29',[1395,2067,1490,2127],[1405,2084,1451,2115],'1','+','detached','half_b',False),
('S30',[644,2177,750,2245],[654,2198,705,2232],'2','+','detached','half_b',False),
('S31',[805,2178,896,2241],[815,2195,855,2225],'1','-','detached','half_b',False),
('S32',[1135,2165,1238,2235],[1147,2183,1196,2222],'2','+','detached','15_second_ie',False),
('S33',[1268,2169,1355,2235],[1279,2188,1322,2218],'1','-','detached','half_b',False),
('S34',[1374,2164,1477,2229],[1386,2182,1430,2215],'2','+','detached','half_b',False),
('S35',[529,2270,625,2332],[538,2283,583,2318],'12',None,'joined','16_def',False),
('S36',[653,2265,748,2330],[665,2276,709,2320],'1','-','detached','16_def',False),
('S37',[783,2266,878,2329],[795,2281,836,2318],'2','-','detached','half_b',False),
('S38',[1167,2257,1248,2319],[1177,2275,1220,2309],'1','-','detached','half_b',False),
('S39',[1265,2256,1351,2317],[1278,2270,1320,2305],'2','-','detached','half_b',False),
]

low_blots={
 'S04':[(859,922),(868,916),(875,921),(879,919),(880,929),(884,932),(881,937),(873,929),(866,929)],
 'S05':[(986,914),(997,909),(1005,913),(1010,912),(1008,921),(1014,925),(1005,927),(999,923),(991,924)],
 'S07':[(849,1056),(862,1051),(870,1054),(871,1062),(877,1067),(872,1070),(866,1063),(856,1062)]
}
def poly(points):return ' -- '.join('('+str(x)+','+str(y)+')' for x,y in points)+' -- cycle'

for sid,bbox,b,low,high,connection,view,qual in specs:
    x0,y0,x1,y1=b; w=x1-x0; h=y1-y0
    top=draw(f'({x0},{y0}) .. controls ({x0+w*.32:.1f},{y0-2}) and ({x1-7},{y0-2}) .. ({x1},{y0-2})')
    start=(x0+4,y0+5) if connection=='detached' else (x0,y0)
    body=draw(f'({start[0]},{start[1]}) .. controls ({x0+12},{y0+6}) and ({x1-3},{y0+9}) .. ({x1-4},{y0+13}) .. controls ({x1-6},{y0+18}) and ({x0+7},{y1-5}) .. ({x0},{y1}) .. controls ({x0+w*.4:.1f},{y1-1}) and ({x1-9},{y1-1}) .. ({x1},{y1-1})')
    parts=[top,body]
    if sid=='S02':parts.append(draw('(837,871) -- (846,872)','0.35pt',60))
    if sid in ['S25','S30']:parts.append(draw(f'({x1},{y1-1}) -- ({x1+1},{y1+5})'))
    if sid=='S17':parts.append(draw('(124,1674) -- (146,1679) -- (128,1683)','0.35pt'))
    if low is not None:parts.append(node(x1+4,y1+4,low,True,r'\scriptsize'))
    if high is not None:parts.append(node(x1+4,y0-2,high,True,r'\scriptsize'))
    if sid in low_blots:
        parts.append(r'\fill '+poly(low_blots[sid])+';')
    if sid=='S05':
        parts.append(r'\fill (969,883) -- (976,877) -- (982,883) -- (984,887) -- (974,889) -- (969,887) -- cycle;')
    if sid=='S06':
        parts.extend([draw('(1053,941) -- (1090,964)','0.55pt'),draw('(1062,938) -- (1082,962)','0.4pt')])
    if sid=='S09':parts.append(draw('(490,1239) -- (601,1230)','0.5pt'))
    if sid=='S10':parts.append(draw('(1143,1178) -- (1239,1178)','0.5pt'))
    if sid=='S11':parts.append(draw('(1383,1167) -- (1510,1162)','0.5pt'))
    tex_plain=r'\Sigma'+('_{'+low+'}' if low else '')+('^{'+high+'}' if high else '')
    states=[]
    if sid=='S04':
        tex_plain=r'\Sigma_{\deleted{\alpha}}^{\alpha}'
        readings=[r'\Sigma_{\deleted{\alpha}}^{\alpha}',r'\Sigma_{\alpha}^{\alpha}']
    elif sid=='S05':
        tex_plain=r'\Sigma_{\deleted{\alpha}}^{\deleted{\alpha}\alpha,0}'
        readings=[tex_plain,r'\Sigma_{\alpha}^{\deleted{\alpha}\alpha,0}',r'\Sigma_{\deleted{\alpha}}^{\alpha,0} with independent upper dark trace',r'\Sigma_{\alpha}^{\alpha,0} with independent upper dark trace']
    elif sid=='S07':
        tex_plain=r'\Sigma_{\deleted{\alpha}}^{\alpha}'
        readings=[tex_plain,r'\Sigma_{\alpha}^{\alpha}']
    elif sid=='S06':
        tex_plain=r'\deleted{\Sigma_{\alpha}}';readings=[tex_plain]
    else:readings=[tex_plain]
    for rr in readings:
        states.append({'complete_reading':rr,'hand':'his hand; independent upper trace has undetermined hand' if 'independent upper' in rr else 'his hand','role':'literal complete glyph and local written correction state','attachment':'indices/signs at the individually specified native positions'})
    if connection=='detached':
        states += [{'complete_reading':rr+' with short upper head/retrace','hand':'his hand','role':'upper run allocated to the glyph','attachment':'detached short run above the body'} for rr in readings]
        states += [{'complete_reading':rr+' with independent short upper run','hand':'his hand for glyph; undetermined hand for independent run','role':'independent upper-run role and surface origin undetermined','attachment':'same visible run, no inferred algebraic operation'} for rr in readings]
    # The concrete literal drawing occurs once. Invisible annotation preserves its textual identity.
    annotation=r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ('+str(bbox[0])+','+str(y1)+') {'+r'\phantom{$'+tex_plain.replace(r'\unsure{0|\circ|o}','0')+'$}};'
    actual=picture('\n'.join(parts+[annotation]),bbox,baseline=y1,qualified=qual)
    S[sid]=block('C026-'+sid,actual,kind='literal mathematical glyph',observed_bbox=bbox,drawing_rectangle=bbox,
                  source_coordinate_system='original full-scan pixels; manually approximated paths',native_units={'x':'0.025em per source pixel','y':'-0.025em per source pixel'},
                  baseline=[bbox[0],y1],ownership=tex_plain,head_connection=connection,evidence_view=view,
                  candidate_states=states,confidence='medium' if qual else 'high',first_recurring_head_qualifier=(sid=='S01'),
                  components=[{'component':i+1,'literal_source':p} for i,p in enumerate(parts)])

# Generic text with local shape information is used only where the halves settle the reading.
# Every additional drawn guide/mark has a dedicated group and ownership boundary.

title=r'\uline{\unsure{décomposition|dècomposition|decomposition|disposition} binaire}'
familyE=r'\unsure{\mathcal E|\mathscr E|\varepsilon}'

# Initial crossed/retraced h: its actual cross is shown once, and the entire word alternatives remain explicit.
hbody='\n'.join([
draw('(302,864) .. controls (320,865) and (317,883) .. (302,887) .. controls (294,896) and (300,908) .. (308,910) .. controls (315,909) and (316,900) .. (323,900) -- (333,905)'),
draw('(287,883) -- (331,883)','0.55pt'),
draw('(287,883) -- (312,895)','0.45pt'),
node(333,906,'émisphères'),
node(282,906,r'\phantom{\unsure{hémisphères|\deleted{h}émisphères}}')])
G01=block('C026-G01',picture(hbody,[281,857,655,931],906,True),kind='word with local crossing run',observed_bbox=[281,857,655,931],drawing_rectangle=[281,857,655,931],native_units={'x':'0.025em','y':'-0.025em'},baseline=[281,906],ownership='hémisphères, complete word; no adjoining les or Sigma',evidence_view='17_hemispheres',candidate_states=[{'complete_reading':'hémisphères with initial h retrace/cross-run','hand':'his hand','role':'live word; cross allocation unresolved','attachment':'initial h only'},{'complete_reading':r'\deleted{h}émisphères','hand':'his hand','role':'cross may cancel the initial h','attachment':'initial h only; following émisphères remains live'}])

de_body='\n'.join([node(1335,857,'(et'),node(1427,793,r'\inserted{de}'),node(1450,856,'plus,'),draw('(1421,855) .. controls (1434,820) and (1484,808) .. (1504,795)','0.45pt')])
G02=block('C026-G02',picture(de_body,[1328,776,1596,895],856),kind='insertion and guide',observed_bbox=[1328,776,1596,895],drawing_rectangle=[1328,776,1596,895],native_units={'x':'0.025em','y':'-0.025em'},baseline=[1328,856],ownership='(et, inserted de, plus, and its comma; no following le plus souvent',evidence_view='18_de_plus',candidate_states=[{'complete_reading':r'(et \inserted{de} plus,','hand':'his hand','role':'raised insertion','attachment':'between et and plus'}])

# The interlinear formula is represented with its native placements and bent guide.
# S03--S05 supply all indices, predecessor blobs and the first recurring ring qualification.
formula=(r'\inserted{$'+S['S03']+r'\ et\ '+S['S04']+r'\setminus E='+S['S05']+'$}')
ins_body='\n'.join([node(670,928,formula),node(758,984,'connexes'),node(1050,984,r'$'+S['S06']+'$'),draw('(755,999) .. controls (737,969) and (747,950) .. (780,948) .. controls (846,948) and (922,949) .. (949,930) .. controls (954,926) and (956,922) .. (955,918)','0.4pt')])
G03=block('C026-G03',picture(ins_body,[666,875,1120,1004],984),kind='inserted equation with guide and cancelled following glyph',observed_bbox=[666,875,1120,1004],drawing_rectangle=[666,875,1120,1004],native_units={'x':'0.025em','y':'-0.025em'},baseline=[666,984],ownership='entire inserted three-Sigma formula, live connexes and cancelled Sigma_alpha after connexes; preceding comma and following et où remain outside',evidence_view='04_inserted_formula',candidate_states=[{'complete_reading':'inserted formula as separately qualified in S03/S04/S05; connexes; deleted Sigma_alpha','hand':'his hand, except the independent upper-trace candidate in S05','role':'insertion before connexes; following glyph cancelled','attachment':'bent guide turns to the gap immediately before connexes'}])

neq_body='\n'.join([draw('(1361,1018) -- (1385,1017)'),draw('(1374,1010) .. controls (1382,1009) and (1386,1010) .. (1387,1012)','0.35pt'),draw('(1379,1005) -- (1371,1031)'),node(1360,1027,r'\phantom{$\unsure{\ne|+}$}')])
G04=block('C026-G04',picture(neq_body,[1355,1000,1394,1036],1027,True),kind='qualified relation',observed_bbox=[1355,1000,1394,1036],drawing_rectangle=[1355,1000,1394,1036],native_units={'x':'0.025em','y':'-0.025em'},baseline=[1355,1027],ownership=r'\ne|+ only; adjoining E and varnothing outside',evidence_view='05_following_si',candidate_states=[{'complete_reading':r'\ne','hand':'his hand','role':'primary relation reading','attachment':'between E and varnothing'},{'complete_reading':'+','hand':'his hand','role':'alternative relation reading','attachment':'same physical sign'}])

correct_body='\n'.join([
node(605,1101,r'\inserted{$X$ connexe,}'),node(867,1084,r'\rlap{et}\phantom{\inserted{\deleted{et}}}'),
draw('(865,1080) -- (910,1080)','0.55pt'),
node(650,1157,'les'),node(770,1157,'$'+S['S08']+'$'),node(907,1140,'connexes'),node(1116,1141,','),
draw('(643,1164) .. controls (784,1153) and (995,1132) .. (1106,1128)','0.6pt'),
draw('(643,1168) .. controls (628,1120) and (642,1120) .. (681,1114) .. controls (814,1087) and (929,1081) .. (965,1075) .. controls (974,1073) and (975,1078) .. (968,1080)','0.35pt',65),
node(648,1157,r'\phantom{\deleted{les $\Sigma_{\alpha}^{\alpha,0}$ connexes}}')])
G05=block('C026-G05',picture(correct_body,[600,1068,1140,1174],1157),kind='replacement clause and cancellation',observed_bbox=[600,1068,1140,1174],drawing_rectangle=[600,1068,1140,1174],native_units={'x':'0.025em','y':'-0.025em'},baseline=[600,1157],ownership='inserted X connexe, deleted et, deleted les Sigma_alpha^(alpha,0) connexes, terminal comma, upper bent guide and lower cancellation; preceding si outside',evidence_view='06_corrected_connexe',candidate_states=[{'complete_reading':r'\deleted{les $\Sigma_\alpha^{\alpha,0}$ connexes}, \inserted{$X$ connexe, \deleted{et}}','hand':'his hand','role':'deleted clause with raised live replacement and crossed et','attachment':'replacement over the deleted clause; no inferred chronology beyond written states'}])

# Margin diagram: native local axes are upright before the final 50-degree placement.
# The diagram itself uses tikz-cd; all additions are end-picture overlays.
diag=r'''\diagram{\rotatebox{50}{\begin{tikzcd}[ampersand replacement=\&,column sep=2.8em,execute at end picture={
\begin{scope}[x=1mm,y=1mm,shift={(scLeft.center)}]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (-2,8) {diagramme};
% The cancelled upper character has B primary, E and Sigma alternatives; paths occur once.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,2) {\unsure{\begin{tikzpicture}[x=0.12em,y=-0.12em,baseline=(base),line cap=round,line join=round]
\coordinate (base) at (0,7);\path[use as bounding box] (0,0) rectangle (8,8);
\draw[line width=0.5pt] (1,7) -- (1,1) -- (5,1) .. controls (8,1) and (8,3) .. (4,4) .. controls (9,4) and (8,7) .. (1,7);
\draw[line width=0.5pt] (0,2) -- (7,0) (0,6) -- (8,2) (0,8) -- (7,4);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,7) {\phantom{$\deleted{B|E|\Sigma}$}};
\end{tikzpicture}}};
% One small point below the segment; no punctuation or algebraic role assigned.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (3,-1.3) {\unsure{\begin{tikzpicture}[x=1mm,y=1mm,baseline=(base)]\coordinate (base) at (0,0);\path[use as bounding box] (0,0) rectangle (.7,.7);\fill (.3,.3) circle (.13);\end{tikzpicture}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (-4,-6) {$\begin{tikzpicture}[x=0.12em,y=-0.12em,baseline=(base),line cap=round,line join=round]
\coordinate (base) at (0,7);\path[use as bounding box] (0,0) rectangle (9,8);
\draw (0,0) -- (5,0);\draw (0,1) .. controls (4,1) and (5,2) .. (4,3) -- (0,7) -- (5,7);
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\scriptsize] at (5,-.4) {$-$};
\end{tikzpicture}\supset E_{\alpha}\subset\begin{tikzpicture}[x=0.12em,y=-0.12em,baseline=(base),line cap=round,line join=round]
\coordinate (base) at (0,7);\path[use as bounding box] (0,0) rectangle (10,8);
\draw (0,0) -- (5,0);\draw (0,1) .. controls (4,1) and (5,2) .. (4,3) -- (0,7) -- (5,7);
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\scriptsize] at (5,-.4) {$+$};
\end{tikzpicture}$};
\end{scope}
}]
|[alias=scLeft]|\bullet\arrow[r,dash]\&\bullet
\end{tikzcd}}}'''
# Source-only markers expose both native diagram glyphs and its small point separately.
left_start=r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (-4,-6) {$\begin{tikzpicture}'
diag=diag.replace(left_start,r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (-4,-6) {$% BEGIN C026-S15'+'\n'+r'\begin{tikzpicture}',1)
diag=diag.replace(r'\end{tikzpicture}\supset E_{\alpha}\subset\begin{tikzpicture}',r'\end{tikzpicture}'+'\n% END C026-S15\n'+r'\supset E_{\alpha}\subset'+'% BEGIN C026-S16\n'+r'\begin{tikzpicture}',1)
diag=diag.replace(r'\end{tikzpicture}$};',r'\end{tikzpicture}'+'\n% END C026-S16\n'+r'$};',1)
for sid,label,bb in [('S15',r'\Sigma^-',[76,1285,125,1364]),('S16',r'\Sigma^+',[197,1124,248,1197])]:
    groups['C026-'+sid]={'id':'C026-'+sid,'kind':'literal mathematical glyph within diagram','observed_bbox':bb,'drawing_rectangle':[0,0,9 if sid=='S15' else 10,8],'source_coordinate_system':'local upright diagram glyph; parent scLeft.center overlay, rotatebox 50 degrees','native_units':{'x':'0.12em','y':'-0.12em'},'baseline':[0,7],'ownership':label,'head_connection':'detached','evidence_view':'08_oblique_diagram','candidate_states':[{'complete_reading':label+' with short head/retrace','hand':'his hand','role':'upper run allocated to glyph','attachment':'short detached head above body'},{'complete_reading':label+' with independent short upper run','hand':'his hand for glyph; undetermined hand for upper run','role':'independent run role/surface origin unestablished','attachment':'same supported upper path; no assigned operation'}]}
e_body=r'''\unsure{\begin{tikzpicture}[x=0.12em,y=-0.12em,baseline=(base),line cap=round,line join=round]
\coordinate (base) at (0,7);\path[use as bounding box] (0,0) rectangle (10,10);
\draw (1,0) .. controls (3,-.5) and (5,-.5) .. (6,0);
\draw (1,1.4) -- (0,7) -- (6,7);
\draw (.5,4) -- (4.5,3.6);
\draw (5.3,7) .. controls (5.4,9) and (8.3,9) .. (7.7,6.7) .. controls (7.2,6.6) and (7.3,8.3) .. (9.2,9);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,7) {\phantom{$E_\alpha$}};
\end{tikzpicture}}'''
e_fragment=block('C026-E01',e_body,kind='literal mathematical glyph within diagram',observed_bbox=[143,1208,193,1260],drawing_rectangle=[0,0,10,10],source_coordinate_system='local upright diagram glyph; parent scLeft.center overlay, rotatebox 50 degrees',native_units={'x':'0.12em','y':'-0.12em'},baseline=[0,7],ownership=r'E_\alpha, with shared foot/alpha loop; alpha attachment resolved independently from top-arm role',head_connection='detached',evidence_view='08_oblique_diagram',candidate_states=[{'complete_reading':r'E_\alpha with detached top arm','hand':'his hand','role':'top run allocated to E; low alpha selected','attachment':'top run over E; alpha loop shares the lower right foot'},{'complete_reading':r'E_\alpha with independent upper run','hand':'his hand for E/alpha; undetermined hand for independent upper run','role':'upper-run role and surface origin unestablished; low alpha selected','attachment':'same preserved upper run and shared foot/alpha loop'}])
diag=diag.replace(r'\supset E_{\alpha}\subset',r'\supset '+e_fragment+r'\subset',1)
G06=block('C026-G06',diag,kind='oblique diagram',observed_bbox=[45,956,248,1365],drawing_rectangle={'diagram_local_units':'mm; glyph subpictures use 0.12em','origin':'scLeft.center; fixed local overlay origin','rotation_degrees':50},baseline='tikz-cd baseline',ownership='diagramme; both filled endpoints; plain segment; cancelled B/E/Sigma; one detached point; full Sigma^- superset E_alpha subset Sigma^+ legend',evidence_view='08_oblique_diagram',candidate_states=[{'complete_reading':r'diagramme; segment with filled endpoints; \deleted{B}; \Sigma^-\supset E_\alpha\subset\Sigma^+; independent point','hand':'his hand for writing/diagram; point undetermined hand','role':'upper glyph cancelled; point role/surface origin unestablished','attachment':'glyph over segment; point just below segment; E alpha attached at low right'},{'complete_reading':r'same complete diagram with \deleted{E} in place of \deleted{B}','hand':'his hand, point undetermined','role':'same cancellation and point qualifications','attachment':'same placement'},{'complete_reading':r'same complete diagram with \deleted{\Sigma} in place of \deleted{B}','hand':'his hand, point undetermined','role':'same cancellation and point qualifications','attachment':'same placement'}])

# Paired dots below the underlined adjective are independent from that word.
adjective=r'non \unsure{panachées|penchées|parallèles}'
adj_body='\n'.join([node(1188,1658,adjective),draw('(1228,1685) -- (1622,1668)','0.45pt'),node(1188,1658,r'\phantom{\uline{non panachées}}'),
node(1581,1694,r'\unsure{\begin{tikzpicture}[x=0.025em,y=-0.025em,baseline=(base)]\coordinate (base) at (0,10);\path[use as bounding box] (0,0) rectangle (12,16);\fill (7,4) circle (1.15);\fill (3,11) circle (1.05);\end{tikzpicture}}')])
G07=block('C026-G07',picture(adj_body,[1180,1620,1633,1704],1658),kind='underlined word group with independent marks',observed_bbox=[1180,1620,1633,1704],drawing_rectangle=[1180,1620,1633,1704],native_units={'x':'0.025em','y':'-0.025em'},baseline=[1180,1658],ownership='non panachées/penchées/parallèles, underline, two detached lower points; preceding sont outside',evidence_view='13_non_adjective',candidate_states=[{'complete_reading':'non '+w+' with single underline and two lower points','hand':'his hand for term/underline; undetermined hand for points','role':'term qualified; points role and surface origin unestablished','attachment':'points below right end, not assigned to punctuation'} for w in ['panachées','penchées','parallèles']])

pairtext=r'$\{'+S['S17']+','+S['S18']+r'\},\unsure{[|(}'+S['S19']+','+S['S20']+r'\}$'
pairs_body='\n'.join([node(107,1699,pairtext),node(518,1669,r'\rlap{distinctes}\phantom{\deleted{distinctes}}'),
draw('(512,1681) -- (561,1644) -- (540,1679) -- (604,1640) -- (584,1671) -- (648,1635)','0.45pt'),draw('(518,1680) -- (698,1657)','0.45pt'),
node(272,1730,r'\inserted{de $X$,}'),draw('(229,1744) .. controls (240,1700) and (328,1709) .. (401,1708) .. controls (466,1702) and (523,1692) .. (545,1688) .. controls (562,1696) and (584,1692) .. (594,1690)','0.4pt')])
G08=block('C026-G08',picture(pairs_body,[100,1630,710,1752],1699),kind='binary pairs with deleted word and insertion',observed_bbox=[100,1630,710,1752],drawing_rectangle=[100,1630,710,1752],native_units={'x':'0.025em','y':'-0.025em'},baseline=[100,1699],ownership='both pairs and separating comma, deleted distinctes, inserted de X comma, its bent guide; following on dit outside',evidence_view='12_pairs_and_guides',candidate_states=[{'complete_reading':r'\{\Sigma_1^+,\Sigma_1^-\},[\Sigma_2^+,\Sigma_2^-\}\deleted{distinctes}\inserted{de X,}','hand':'his hand','role':'second opener [ primary; deletion and raised insertion firm','attachment':'de X after the pairs/deleted distinctes'},{'complete_reading':r'\{\Sigma_1^+,\Sigma_1^-\},(\Sigma_2^+,\Sigma_2^-\}\deleted{distinctes}\inserted{de X,}','hand':'his hand','role':'second opener ( alternative; same complete correction','attachment':'same placement'}])

on_body='\n'.join([draw('(389,1835) -- (391,1831)','0.4pt'),draw('(402,1834) .. controls (413,1832) and (424,1830) .. (433,1831)','0.35pt',55),draw('(445,1831) .. controls (450,1830) and (453,1832) .. (455,1833)','0.35pt',60),node(386,1836,r'\phantom{\unsure{on}}')])
on_group=block('C026-G09a',picture(on_body,[384,1824,460,1844],1837,True),kind='reduced word/traces',observed_bbox=[384,1824,460,1844],drawing_rectangle=[384,1824,460,1844],native_units={'x':'0.025em','y':'-0.025em'},baseline=[384,1837],ownership='on only; preceding si/insertion and following peut outside',evidence_view='12_pairs_and_guides',candidate_states=[{'complete_reading':'on','hand':'his hand','role':'primary lexical reading','attachment':'before peut trouver'},{'complete_reading':'three reduced separate traces without established lexical reading','hand':'undetermined hand','role':'nonlexical shape candidate, surface origin unestablished','attachment':'same group before peut trouver'}])
si_body='\n'.join([node(286,1852,'si'),node(370,1774,r'\inserted{elles sont \uline{distinctes}, et si}'),node(386,1837,on_group),node(510,1816,'peut trouver'),draw('(373,1850) .. controls (361,1817) and (378,1804) .. (415,1800) .. controls (563,1777) and (766,1759) .. (925,1737) .. controls (932,1736) and (932,1731) .. (928,1728)','0.4pt')])
G09=block('C026-G09',picture(si_body,[280,1716,939,1858],1837),kind='qualification insertion and guide',observed_bbox=[280,1716,939,1858],drawing_rectangle=[280,1716,939,1858],native_units={'x':'0.025em','y':'-0.025em'},baseline=[280,1837],ownership='baseline si, inserted elles sont distinctes, et si, reduced on, peut trouver and long bent guide; following Sigma1+ outside',evidence_view='12_pairs_and_guides',candidate_states=[{'complete_reading':r'si \inserted{elles sont \uline{distinctes}, et si} on peut trouver','hand':'his hand; reduced-on alternative keeps its separate undetermined hand scope','role':'insertion before on; distinctes singly underlined','attachment':'guide left turn immediately before on, upper endpoint after et si'}])

relation_body='\n'.join([draw('(786,2108) .. controls (770,2103) and (758,2114) .. (761,2127) .. controls (765,2138) and (780,2135) .. (790,2135)','0.55pt'),draw('(755,2141) .. controls (757,2129) and (764,2120) .. (769,2123) -- (779,2135)','0.4pt'),node(753,2135,r'\phantom{$\unsure{\deleted{\cap}\subset|\subset|\in}$}')])
G10=block('C026-G10',picture(relation_body,[748,2100,797,2146],2137,True),kind='overdrawn relation',observed_bbox=[748,2100,797,2146],drawing_rectangle=[748,2100,797,2146],native_units={'x':'0.025em','y':'-0.025em'},baseline=[748,2137],ownership='one relation between Sigma1+ and Sigma2-; both adjoining terms outside',evidence_view='14_first_lower_relation',candidate_states=[{'complete_reading':r'\deleted{\cap}\subset','hand':'his hand','role':'primary prior-cap/live-subset state, qualified','attachment':'one shared overdrawn sign; no asserted chronology proof'},{'complete_reading':r'\subset','hand':'his hand','role':'subset with retraced lower left','attachment':'same paths'},{'complete_reading':r'\in','hand':'his hand','role':'membership-shaped alternative','attachment':'same paths'}])

cancel_body='\n'.join([node(906,2133,r'\rlap{$\ne\varnothing$}\phantom{\deleted{$\ne\varnothing$}}'),draw('(903,2117) -- (947,2114) (904,2128) -- (959,2112) (911,2137) -- (952,2104) (948,2147) -- (981,2098)','0.65pt')])
G11=block('C026-G11',picture(cancel_body,[899,2093,987,2150],2133),kind='cancelled expression',observed_bbox=[899,2093,987,2150],drawing_rectangle=[899,2093,987,2150],native_units={'x':'0.025em','y':'-0.025em'},baseline=[899,2133],ownership=r'deleted \ne\varnothing only; neighbouring Sigma2- and i.e. outside',evidence_view='14_first_lower_relation',candidate_states=[{'complete_reading':r'\deleted{\ne\varnothing}','hand':'his hand','role':'readable cancelled pair of signs','attachment':'after Sigma2- in first lower inclusion'}])

def_body='\n'.join([node(613,2280,r'\mathrm{def}',True,r'\scriptsize'),r'\fill (634,2260) ellipse (0.8 and 1.2);',node(620,2307,'=',True),node(613,2280,r'\phantom{$\overset{\unsure{\text{déf}|\text{def}}}{=}$}')])
G12=block('C026-G12',picture(def_body,[610,2250,653,2312],2307,True),kind='definition label with raised mark',observed_bbox=[610,2250,653,2312],drawing_rectangle=[610,2250,653,2312],native_units={'x':'0.025em','y':'-0.025em'},baseline=[610,2307],ownership='complete def/déf label, one raised mark and equals; both Sigma terms outside',evidence_view='16_def',candidate_states=[{'complete_reading':r'\overset{\mathrm{déf}}{=}','hand':'his hand','role':'raised mark read as acute on e','attachment':'above e in the defining label'},{'complete_reading':r'\overset{\mathrm{def}}{=} with independent raised point','hand':'his hand for def and equals; undetermined hand for point','role':'raised point role and surface origin unestablished','attachment':'same observed point above e; not omitted'}])

def mark(ident,bbox,paths,ownership,view):
    return block(ident,picture('\n'.join(paths),bbox,qualified=True),kind='detached graphical traces',observed_bbox=bbox,drawing_rectangle=bbox,native_units={'x':'0.025em','y':'-0.025em'},baseline=[bbox[0],bbox[3]-4],ownership=ownership,evidence_view=view,candidate_states=[{'complete_reading':ownership,'hand':'undetermined hand','role':'shape retained; character, role and surface origin unestablished','attachment':'no mathematical or lexical attachment assigned'}])
M02=mark('C026-M02',[731,1520,755,1537],[draw('(734,1523) -- (737,1526)','0.35pt'),r'\fill[black!60] (742,1528) circle (.65);',r'\fill[black!45] (747,1530) circle (.6);',r'\fill[black!35] (752,1532) circle (.5);'],'one short slash and three faint points below un','10_parenthetic_end')
M04=mark('C026-M04',[749,2314,761,2330],[draw('(754,2318) -- (756,2324)','0.35pt',60)],'short gray slash below the first final intersection sign','16_def')

text=(r'\scanpage{26}'+'\n'
      +'Soit $X$ un ens. Une '+title+' de $X$ est un ens de deux parties de $X$\n'
      +r'\['+'\n'+r'('+S['S01']+r')_{\alpha\in'+familyE+r'}\qquad(\text{les ``hémisphères''})'+'\n'+r'\]'+'\n'
      +r"dont la réunion est $X$, et dont \deleted{l'intersection} aucune n'est contenue dans l'autre -- on désigne par $E$ (``équateur'') l'intersection (on n'exclut pas qu'elle soit vide). Quand $X$ est un espace topologique, on \unsure{s'intéresse|s'intèresse|s'interesse} au cas où les "+G01+' $'+S['S02']+'$ sont fermés, '+G02+' le plus souvent, '+G03+r' et où $E\ne\varnothing$); si les $'+S['S07']+'$ connexes et $E'+G04+r'\varnothing$, $X$ est connexe, si '+G05+r' on conclut \deleted{\unsure{aussitôt|aussitot}} que $'+S['S09']+r'\cap E\ne\varnothing$'+'\n'
      +'% margin note written sideways\n'+r'\reversemarginpar\margin{'+G06+r'}\normalmarginpar%'+'\n'
      +'(car $'+S['S10']+r'\cap E='+S['S11']+r'\setminus'+S['S12']+'$, et $'+S['S13']+r'$ ne peut \unsure{être|etre} \unsure{à|:} la fois ouvert et fermé car $'+S['S14']+r'$, est un '+r'\underset{\text{'+M02+r'}}{\text{un}}'+' ouvert '+r'$\ne\varnothing$ et $\ne X$)'+'\n\n'
      +'Considérons deux décompositions binaires '+G08+" on dit qu'elles sont "+G07+' '+G09+' $'+S['S21']+"$ dans l'une, $"+S['S22']+r"$ dans l'autre, tels que"+'\n'
      +r'\['+'\n'+S['S23']+r'\cap'+S['S24']+r'=\varnothing\qquad(\text{d’où }E_1\cap E_2=\varnothing)'+'\n'+r'\]'+'\n'
      +'on a alors\n'+r'\['+'\n'+r'\begin{aligned}'+'\n'
      +S['S25']+'&'+G10+S['S26']+r'\ '+G11+r'\quad\text{i.e.}\quad'+S['S27']+r'\cap'+S['S28']+'='+S['S29']+r'\\'+'\n'
      +S['S30']+r'&\subset'+S['S31']+r'\qquad\qquad\text{\unsure{i.e|i.e.|ie}}\quad'+S['S32']+r'\cap'+S['S33']+'='+S['S34']+r'\\'+'\n'
      +S['S35']+'&'+G12+S['S36']+r'\underset{\text{'+M04+r'}}{\cap}'+S['S37']+r'\supset E_1\cup E_2,\quad'+S['S38']+r'\cap'+S['S39']+r'\ne\varnothing'+'\n'+r'\end{aligned}'+'\n'+r'\]'+'\n'
      +'% archive sheet number: 25\n')
# Source repair only: mark-bearing un owns that word once.
text=text.replace(r'$, est un \underset',r'$, est $\underset').replace(r'{\text{un}} ouvert',r'{\text{un}}$ ouvert')
ROOT.joinpath('reading.tex').write_text(text)

source_map={'scan':26,'reader':'C','coordinate_policy':'Observed boxes are hand-read locations in the original 1694 x 2370 scan. Drawing paths are manual approximations; no tracing extraction, contour alignment, compilation, rendering or metric validation is claimed. All native units, local origins, baselines and qualifier scopes are retained.','groups':[]}
for ident,g in groups.items():
    begin='% BEGIN '+ident+'\n';end='% END '+ident+'\n'
    start=text.index(begin);stop=text.index(end,start)+len(end)
    excerpt=text[start:stop]
    source_map['groups'].append(dict(g,source_span={'start_utf8_byte':len(text[:start].encode()),'end_utf8_byte_exclusive':len(text[:stop].encode()),'start_character':start,'end_character_exclusive':stop,'start_line':text[:start].count('\n')+1,'end_line':text[:stop].count('\n')},source_exact=excerpt,source_sha256=hashlib.sha256(excerpt.encode()).hexdigest()))
ROOT.joinpath('source_map.json').write_text(json.dumps(source_map,ensure_ascii=False,indent=2)+'\n')
ROOT.joinpath('source_map_base.json').write_text(json.dumps(source_map,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex and source_map.json with',len(groups),'individually owned source groups.')
