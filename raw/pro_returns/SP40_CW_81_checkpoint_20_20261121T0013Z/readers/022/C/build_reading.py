from pathlib import Path
import json,re,hashlib

OUT=Path('/workspace/scratch/94548b74fbe0/out/readers/022/C')
S=[]
def sigma(i,box,base,head,body,index,sign,hat=None,bar=None,role='head/retrace or independent upper run unresolved',point=None,shared_bar=None):
    S.append(dict(id=f'C022-S{i:02}',observed_bbox=box,origin=base,head=head,body=body,index=index,sign=sign,hat=hat,bar=bar,role=role,point=point,shared_bar=shared_bar))

# Coordinates are manual observations in the original 1691 x 2362 scan.
# The two ordinary label positions in index/sign are typographical anchors.
sigma(1,[1211,155,1290,222],[1212,213],[(1217,184),(1254,186)],[(1216,190),(1249,199),(1217,212),(1255,213)],[1255,221,'\\alpha'],[1271,185,'+'],[(1235,168),(1257,155),(1274,168)])
sigma(2,[1447,163,1522,223],[1448,214],[(1451,185),(1484,187)],[(1450,192),(1482,201),(1450,212),(1488,213)],[1488,222,'\\alpha'],[1504,187,'+'],[(1469,173),(1484,164),(1498,174)])
sigma(3,[1164,308,1237,351],[1165,339],[(1168,314),(1199,313)],[(1168,316),(1189,323),(1167,338),(1202,338)],[1205,350,'\\alpha'],[1218,317,'-'],role='head joins the angled body at its left end')
sigma(4,[681,401,782,463],[682,449],[(686,409),(727,404)],[(684,416),(715,424),(688,446),(730,447)],[733,462,'\\alpha'],[758,406,'-'])
sigma(5,[1410,392,1490,447],[1412,432],[(1416,401),(1445,405)],[(1416,409),(1434,419),(1415,430),(1447,433)],[1449,443,'\\alpha'],[1472,402,'+'])
sigma(6,[907,643,1017,734],[909,718],[(916,668),(965,669)],[(915,669),(944,690),(913,715),(966,713)],[969,730,'\\alpha'],[997,676,'-'],bar=[(920,650),(992,648)],role='head and angled body meet at the left end; outer closure rule is separate')
sigma(7,[802,741,874,806],[803,788],[(807,766),(836,762)],[(808,770),(830,777),(807,790),(840,788)],[841,802,'\\alpha'],[857,768,'+'],[(817,756),(833,745),(848,755)])
sigma(8,[998,737,1080,795],[1000,786],[(1005,764),(1037,762)],[(1004,770),(1034,776),(1004,785),(1038,784)],[1042,792,'\\alpha'],[1062,767,'-'],shared_bar='C022-G04 connector horizontal, (1009,749) to (1068,749)')
sigma(9,[1119,726,1183,787],[1120,775],[(1127,746),(1151,741)],[(1127,751),(1143,759),(1127,774),(1154,775)],[1154,783,'\\alpha'],[1169,748,'+'],[(1138,738),(1152,730),(1167,738)])
sigma(10,[740,794,827,856],[741,844],[(745,812),(776,812)],[(745,815),(776,826),(746,843),(780,841)],[781,853,'\\alpha'],[812,803,'-'],role='upper head lies immediately below the crossing frame; exact joining is crowded')
sigma(11,[1400,766,1507,847],[1402,826],[(1407,793),(1443,791)],[(1407,798),(1442,810),(1406,823),(1465,824)],[1448,842,'\\alpha'],[1474,790,'-'],shared_bar='C022-G05 top frame, with dark local run (1410,774) to (1495,771)')
sigma(12,[567,1021,679,1101],[568,1086],[(576,1052),(620,1048)],[(576,1058),(619,1068),(578,1085),(632,1083)],[629,1098,'\\alpha'],[657,1055,'-'],bar=[(575,1031),(665,1028)],role='head and body meet at the upper left; closure rule is separate')
sigma(13,[591,1137,681,1213],[593,1194],[(602,1160),(638,1158)],[(601,1166),(630,1174),(598,1192),(644,1191)],[635,1207,'\\alpha'],[657,1159,'-'],bar=[(602,1145),(669,1142)])
sigma(14,[716,1542,832,1625],[718,1617],[(724,1583),(768,1581)],[(724,1587),(757,1598),(721,1616),(773,1613)],[780,1624,'\\alpha'],[811,1581,'-'],[(762,1558),(784,1546),(799,1557)])
sigma(15,[892,1577,985,1628],[895,1615],[(899,1582),(936,1581)],[(900,1588),(927,1598),(897,1615),(941,1614)],[944,1627,'\\alpha'],[967,1587,'-'])
sigma(16,[715,1949,814,2034],[717,2014],[(734,1982),(768,1980)],[(730,1988),(759,1997),(723,2015),(772,2015)],[773,2030,'\\alpha'],[788,1983,'+'],[(758,1964),(779,1953),(794,1963)])
sigma(17,[1193,1928,1303,2042],[1196,2002],[(1203,1963),(1244,1963)],[(1204,1972),(1231,1984),(1201,2000),(1254,2001)],[1255,2035,'\\beta'],[1282,1969,'+'],[(1242,1944),(1258,1931),(1274,1942)],point=[1210,1981])

def nfmt(v): return str(int(v)) if v==int(v) else str(v)
def xy(p,o): return '('+','.join(nfmt(p[j]-o[j]) for j in range(2))+')'
def path(ps,o): return ' -- '.join(xy(p,o) for p in ps)

def sig(g,qualified=False):
    o=g['origin']; bb=g['observed_bbox']; ident=g['id']
    lines=[f'% BEGIN {ident}',f'% full-scan origin/baseline {tuple(o)}; local x=X-{o[0]}, y=Y-{o[1]}; x=0.008cm, y=-0.008cm.',f'% Owns one Sigma body, its short head, index {g["index"][2]}, raised {g["sign"][2]}, and the listed roof/bar/point only.',f'% Upper-run role: {g["role"]}.']
    content=['\\begin{tikzpicture}[baseline={(0,0)},x=0.008cm,y=-0.008cm,line cap=round,line join=round]',f'\\path[use as bounding box] {xy(bb[:2],o)} rectangle {xy(bb[2:],o)};',f'\\draw[line width=.55pt] {path(g["head"],o)};',f'\\draw[line width=.55pt] {path(g["body"],o)};']
    if g['hat']: content.append(f'\\draw[line width=.55pt] {path(g["hat"],o)};')
    if g['bar']: content.append(f'\\draw[line width=.55pt] {path(g["bar"],o)};')
    if g['shared_bar']: content.append('% Shared visible rule owned once by '+g['shared_bar']+'.')
    ix,iy,it=g['index']; content.append(f'\\node[anchor=base west,inner sep=0,outer sep=0,font=\\scriptsize] at {xy([ix,iy],o)} {{$'+it+'$};')
    sx,sy,st=g['sign']; content.append(f'\\draw[line width=.55pt] {xy([sx-6,sy],o)} -- {xy([sx+6,sy],o)};')
    if st=='+':content.append(f'\\draw[line width=.55pt] {xy([sx,sy-6],o)} -- {xy([sx,sy+6],o)};')
    if g['point']:
        px,py=g['point']
        content.extend(['% BEGIN C022-M03',f'% Point-only local group; full-scan origin ({px},{py}); no letter is owned here.',f'\\node[anchor=base west,inner sep=0,outer sep=0] at {xy([px,py],o)} {{\\unsure{{\\mbox{{\\begin{{tikzpicture}}[baseline={{(0,0)}},x=0.008cm,y=-0.008cm]',r'\path[use as bounding box] (-2,-3) rectangle (3,2);',r'\fill (-2,-1) .. controls (-1,-4) and (2,-3) .. (3,0) .. controls (1,2) and (-1,2) .. cycle;',r'\end{tikzpicture}}}}};','% END C022-M03'])
    content.append('\\end{tikzpicture}')
    if qualified: lines.append('\\unsure{\\mbox{'+ '\n'.join(content) +'}}')
    else: lines.append('\\mbox{'+ '\n'.join(content) +'}')
    lines.append(f'% END {ident}\n')
    return '\n'.join(lines)

def sg(i,qualified=False):return sig(S[i-1],qualified)

def pic(id,box,origin,body,ownership):
    return f'% BEGIN {id}\n% observed full-scan bbox {tuple(box)}; origin/baseline {tuple(origin)}.\n% Local x=X-{origin[0]}, y=Y-{origin[1]}; x=0.008cm, y=-0.008cm.\n% Owns {ownership}.\n\\begin{{tikzpicture}}[baseline={{(0,0)}},x=0.008cm,y=-0.008cm,line cap=round,line join=round]\n\\path[use as bounding box] {xy(box[:2],origin)} rectangle {xy(box[2:],origin)};\n'+body+f'\n\\end{{tikzpicture}}\n% END {id}\n'

def node(pos,txt,origin,math=False,size='\\small',overlay=False):
    content='$'+txt+'$' if math else txt
    return '\\node[anchor=base west,inner sep=0,outer sep=0,font='+size+(',overlay' if overlay else '')+'] at '+xy(pos,origin)+' {'+content+'};\n'
def stroke(ps,o,width='.4pt',extra=''):return '\\draw[line width='+width+extra+'] '+path(ps,o)+';\n'
def curve(spec):return '\\draw[line width=.4pt] '+spec+';\n'
def dead(t):return r'\rlap{'+t+r'}\phantom{\deleted{'+t+'}}'

# Opening formula, bottom annotation and the flat bracket are one group.
o=[1010,216]
b=node([1010,216],r'V=',o,True,'\\large')+node([1087,216],r'X\setminus',o,True,'\\large')
b+=node([1158,214],r'\bigcup_{\alpha\in K}',o,True,'\\large')+node(S[0]['origin'],sg(1,True),o)
b+=stroke([[1081,255],[1080,269],[1084,273],[1257,272],[1264,268],[1262,260]],o)
b+=stroke([[1161,285],[1162,299]],o,'.55pt')+stroke([[1171,286],[1172,300]],o,'.55pt')
b+=node([1118,340],r'\bigcap_{\alpha\in K}',o,True,'\\large')+node(S[2]['origin'],sg(3),o)
b+=node([1118,340],r'\phantom{\inserted{\bigcap_{\alpha\in K}\Sigma_\alpha^-}}',o,True,overlay=True)
top=pic('C022-G01',[1007,150,1292,379],o,b,'V=X setminus the indexed union, S01, the flat bracket and two descending equality strokes, and the inserted indexed intersection with S03')

# A partial right-edge closing curve is preserved without completing its unseen end.
o=[1661,237]
edge=pic('C022-G02',[1658,207,1679,241],o,stroke([[1662,213],[1669,222],[1677,239]],o,'.35pt'),'the partial closing curve after K only; primary ) / blank interpretation remains qualified')

# First pair of conditions, with the exact looped brace and crossing arrow.
o=[390,340]
b=node([590,340],r'\overline V\cap E_\alpha\ne\varnothing',o,True,'\\large')
b+=node([590,455],r'V\cap',o,True,'\\large')+node(S[3]['origin'],sg(4),o)
# Cancelled relation/empty-set literal cluster, locally qualified as a whole.
co=[799,449]
cb=stroke([[803,426],[851,422]],co,'.6pt')+stroke([[802,439],[851,434]],co,'.6pt')
cb+=stroke([[829,421],[832,450],[839,449]],co,'.5pt')
cb+=stroke([[800,431],[855,421]],co,'.8pt')+stroke([[799,446],[855,435]],co,'.8pt')
cb+=curve('(94,-50) .. controls (72,-55) and (72,-3) .. (95,-12) .. controls (111,-23) and (105,-49) .. (94,-50)')
cb+=stroke([[876,471],[917,390]],co,'.55pt')+stroke([[876,391],[901,456]],co,'.6pt')+stroke([[885,390],[893,462]],co,'.5pt')
cb+=node([799,449],r'\phantom{\deleted{\unsure{\ne|=}\varnothing}}',co,True,overlay=True)
cluster=pic('C022-G03',[794,384,922,477],co,cb,'the old relation and old empty-set shape, their cancelling strokes, and invisible annotation deleted neq/equals + empty-set')
b+=node(co,'\\unsure{\\mbox{'+cluster+'}}',o)
b+=node([936,451],r'\ne\varnothing',o,True,'\\large')+node([1090,442],'alors que',o)
b+=node([1340,440],r'V\cap',o,True,'\\large')+node(S[4]['origin'],sg(5),o)+node([1498,440],r'=\varnothing',o,True,'\\large')
b+=curve('(158,-43) .. controls (167,-11) and (163,25) .. (156,43) .. controls (143,38) and (144,59) .. (153,50) .. controls (166,42) and (164,80) .. (165,114) .. controls (165,126) and (165,132) .. (169,137)')
b+=node([414,451],'trivial',o,'',size='\\scriptsize')
b+=stroke([[482,443],[581,434]],o,'.3pt')+stroke([[574,430],[582,434],[574,438]],o,'.4pt')
first=pic('C022-G04',[390,265,1615,485],o,b,'both conditions, S04 and S05, G03, the looped brace, trivial and its crossing arrow')

# Main equality and connected cancelled block. All outline runs are drawn once.
o=[245,630]
b=node([610,725],r'\overline V\cap E_\alpha=',o,True,'\\large')+node(S[5]['origin'],sg(6),o)+node([1038,722],r'\cap E_\alpha',o,True,'\\large')+node([1254,704],r'(qui est donc $\ne\varnothing$)',o)
b+=stroke([[687,751],[696,766]],o,'.55pt')+stroke([[699,753],[707,772]],o,'.55pt')
b+=node([727,798],r'\unsure{\overline V\cap '+sg(7)+'}',o,True,'\\small')
b+=node([727,798],r'\phantom{\unsure{\inserted{\overline V\cap\widehat\Sigma_\alpha^+}|\deleted{\inserted{\overline V\cap\widehat\Sigma_\alpha^+}}}}',o,True,overlay=True)
# Three ticks share one horizontal rule above S08. Their equality/strike/bar role is local.
qo=[1008,750]
qb=stroke([[1010,749],[1068,750]],qo,'.55pt')+stroke([[1017,752],[1025,744]],qo,'.45pt')+stroke([[1054,739],[1060,749]],qo,'.55pt')+stroke([[1064,739],[1068,750]],qo,'.55pt')
qb+=node(qo,r'\phantom{\unsure{\deleted{=}|=|\Rightarrow}}',qo,True,overlay=True)
connector=pic('C022-G06',[1007,734,1074,757],qo,qb,'one shared horizontal and three short oblique ticks; vertical deleted equals / equals / implication candidates, no second closure rule')
b+=node(qo,'\\unsure{\\mbox{'+connector+'}}',o)
b+=node(S[7]['origin'],'\\unsure{'+sg(8)+'}',o)+node([1089,784],r'\cap',o,True)+node(S[8]['origin'],sg(9),o)
b+=node([1000,786],r'\phantom{\unsure{\inserted{\overline{\Sigma_\alpha^-}\cap\widehat\Sigma_\alpha^+}|\deleted{\inserted{\overline{\Sigma_\alpha^-}\cap\widehat\Sigma_\alpha^+}}}}',o,True,overlay=True)

b+=node([260,846],dead('Comme'),o)+node([625,846],dead(r'$V\subset$'),o)+node(S[9]['origin'],sg(10),o)+node([875,848],dead(', on a'),o)
b+=node([1173,846],dead(r'$V\cap E_\alpha\subset$'),o)+node(S[10]['origin'],sg(11),o)+node([1520,844],dead(r'$\cap E_\alpha$,'),o)
b+=node([272,976],dead('prouvons'),o)+node([575,957],dead("l'inclusion inverse"),o)
b+=node(S[11]['origin'],sg(12),o)+node([677,1081],dead(r'$\cap E_\alpha\subset\overline V\cap E_\alpha$'),o)
b+=node([286,1208],dead('Soit'),o)+node([481,1204],dead(r'$x\in$'),o)+node(S[12]['origin'],sg(13),o)+node([672,1204],dead(r'$\cap E_\alpha$,'),o)
b+=node([867,1197],dead('prouvons'),o)+node([1170,1191],dead(r'$x\in\overline V\cap E_\alpha$ i.e.'),o)
b+=node([255,1309],dead(r'$x\in\overline V$,'),o)+node([499,1299],dead('soit'),o)+node([660,1292],dead(r'$W$ un voisinage de $x$,'),o)+node([1252,1281],dead("montrons qu'il"),o)
b+=node([271,1403],dead('rencontre'),o)
b+=node([701,1372],dead('Or'),o)+node([819,1374],dead(r'\unsure{on}'),o)+node([950,1371],dead('peut considérer cette'),o)
b+=node([278,1506],dead('formule'),o)+node([332,1464],dead(r'\inserted{égalité}'),o)+node([564,1485],dead('comme'),o)+node([884,1480],dead('égalité dans'),o)
b+=node([312,1595],dead("l'espace"),o)
vo=[576,1626]
vb=stroke([[587,1572],[616,1595],[634,1563]],vo,'.65pt')+stroke([[634,1563],[579,1631]],vo,'.7pt')+stroke([[583,1626],[616,1620]],vo,'.65pt')+stroke([[592,1618],[626,1574]],vo,'1.0pt')
vb+=node(vo,r'\phantom{\deleted{\unsure{Y|Z|X}}}',vo,True,overlay=True)
variable=pic('C022-G07',[572,1558,640,1636],vo,vb,'the old cancelled variable, all visible crossing/foot strokes; primary Y with Z and H X alternatives')
b+=node(vo,'\\unsure{\\mbox{'+variable+'}}',o)+node([640,1618],dead('$=$'),o)+node(S[13]['origin'],sg(14),o)+node([850,1617],dead('$=$'),o)+node(S[14]['origin'],sg(15),o)+node([999,1618],dead(r'$\cup E_\alpha$'),o)
b+=node([307,1730],dead('dans lequel on a deux parties fermées'),o)+node([306,1842],dead('disjointes'),o)
b+=node([718,1796],r'Or dans $X$ on a les deux',o)+node([309,1913],'parties',o)+node([580,1908],r'\uline{fermées}',o)+node([840,1906],r'\uline{disjointes}',o)
# Full outline + interior diagonals: their connected runs retain all observed bends.
b+='% BEGIN C022-G05-PATHS\n'
b+=curve('(1324,146) .. controls (1194,136) and (812,153) .. (476,170) .. controls (305,184) and (161,206) .. (29,205)')
b+=curve('(29,205) .. controls (45,278) and (54,417) .. (54,554) .. controls (69,616) and (64,686) .. (40,770)')
b+=curve('(40,770) .. controls (144,780) and (302,757) .. (394,751) .. controls (373,710) and (374,663) .. (418,658) .. controls (650,661) and (884,660) .. (1076,656)')
b+=curve('(40,770) .. controls (42,817) and (31,861) .. (47,876) .. controls (140,870) and (368,846) .. (664,840) .. controls (896,826) and (1085,857) .. (1189,824) .. controls (1260,803) and (1267,722) .. (1355,690)')
b+=curve('(68,875) .. controls (65,916) and (63,951) .. (68,972) .. controls (87,1011) and (236,981) .. (358,969) .. controls (537,947) and (741,985) .. (872,978) .. controls (958,974) and (1039,947) .. (1100,911)')
b+=curve('(63,1098) .. controls (294,1084) and (534,1063) .. (712,1074) .. controls (897,1087) and (1092,1075) .. (1272,1081)')
b+=curve('(63,1098) .. controls (58,1136) and (40,1185) .. (56,1202) .. controls (99,1229) and (201,1208) .. (298,1197) .. controls (354,1193) and (408,1184) .. (390,1132)')
b+=curve('(272,214) .. controls (315,288) and (352,355) .. (397,450) .. controls (448,562) and (509,643) .. (565,658)')
b+=curve('(737,263) .. controls (779,340) and (815,444) .. (856,529) .. controls (895,621) and (941,719) .. (998,779)')
b+=curve('(1147,218) .. controls (1192,296) and (1227,403) .. (1255,521)')
b+=curve('(571,700) .. controls (616,771) and (664,815) .. (707,842)')
b+=stroke([[1410,774],[1495,771]],o,'.7pt')
b+=stroke([[277,1499],[491,1492]],o,'.7pt')+stroke([[819,1363],[918,1365]],o,'.65pt')
b+='% END C022-G05-PATHS\n'

# Detached shapes have their own qualification, hand and ownership.
mo=[250,901]
mb=curve('(2,-9) .. controls (-1,-4) and (-1,0) .. (1,3)')
m2=pic('C022-M02',[247,887,257,908],mo,mb,'one small isolated upright/curved trace left of the cancellation frame; no adjoining word')
b+=node(mo,'\\unsure{\\mbox{'+m2+'}}',o)
mo=[1217,1840]
m1=pic('C022-M01',[1212,1832,1240,1858],mo,stroke([[1217,1837],[1234,1851]],mo,'.65pt'),'one detached falling oblique stroke; no adjoining word')
b+=node(mo,'\\unsure{\\mbox{'+m1+'}}',o)
main=pic('C022-G05',[245,630,1667,1935],o,b,'the main equality and its annotations, S06-S15, G06-G07, the cancelled proof and inserted égalité, all connected cancellation runs, the live Or sentence with both underlines, M01 and M02')

o=[635,2021]
b=node([635,2021],r'Y=',o,True,'\\large')+node(S[15]['origin'],sg(16),o)+node([825,2041],',',o)+node([902,2015],r'Z=',o,True,'\\large')+node([1040,2013],r'\bigcup_{\beta\in K\setminus\{\alpha\}}',o,True,'\\large')+node(S[16]['origin'],sg(17),o)
bottom=pic('C022-G08',[630,1928,1310,2085],o,b,'Y and Z equality labels, S16 and S17, one separating comma, the union with its full beta in K setminus alpha limit, and M03 inside S17')

reading=r'''\scanpage{22}
\deleted{\unsure{On|Un} \unsure{procède|procéde|procédé} par récurrence sur $\operatorname{card} K$,} \inserted{On note d'abord que} \deleted{pour prouver que} (si $\mbox{
'''+top+r'''}$, les $'''+sg(2)+r'''$ ($\alpha\in K$\unsure{\mbox{
'''+edge+r'''}} étant \unsure{disjoints|disjointes})
\[
\mbox{
'''+first+r'''}
\]

De façon précise, je dis que
\figure{
'''+main+r'''}

\[
\mbox{
'''+bottom+r'''}
\]
et on doit prouver
\[
\overline{(X\setminus(Y\cup Z))}\cap Y=\overline{(X\setminus Y)}\cap Y
\]
ce qui est immédiat
% archive sheet number: 21
'''
(OUT/'reading.tex').write_text(reading)
(OUT/'sigma_groups.json').write_text(json.dumps(S,ensure_ascii=False,indent=2)+'\n')

# Literal source boundaries are extracted from this submitted source, never inferred.
groups=[]
for m in re.finditer(r'^% BEGIN (C022-[A-Z0-9-]+)\n',reading,re.M):
    ident=m.group(1); endmark='% END '+ident+'\n'; end=reading.index(endmark,m.end())+len(endmark)
    excerpt=reading[m.start():end]
    groups.append(dict(id=ident,start_char=m.start(),end_char_exclusive=end,start_line=reading.count('\n',0,m.start())+1,end_line=reading.count('\n',0,end),source=excerpt,sha256=hashlib.sha256(excerpt.encode()).hexdigest(),path_command_count=len(re.findall(r'\\(?:draw|fill)\b',excerpt)),note='Counts for enclosing groups include their nested source groups; nested physical components are owned once.'))
(OUT/'source_groups.json').write_text(json.dumps(groups,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(reading_bytes=len(reading.encode()),source_groups=len(groups),sigma_groups=len(S))))
