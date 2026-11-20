from pathlib import Path
import json,re
BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/readers/012/C'
s=(BASE/'packets/012/C.tex').read_text()
paths={i:m.group(0) for i,m in enumerate(re.finditer(r'\\path\[fill=black,even odd rule\]\s*.*?;',s,re.S),1)}
heavy={34,36,40,42,43,44,45,46,47,48,49,50,51}
right={25,32,33,38,39,41,52,54,55,56,60,61,62,64,67}
# These manual additions transcribe supported visible traces, without assigning
# letters, chronology, semantic role, authorial intention, or surface origin.
marks=[
('N01',[587,41,594,50],'crops/10_upper_pair.png','upper field, right of first miniature, left mark','small pale oblique spot',r'\path[fill=black!38] (590.1,43.3) -- (592.0,44.4) -- (591.0,47.5) -- (589.3,48.1) -- (589.5,45.6) -- cycle;','medium'),
('N02',[606,43,612,51],'crops/10_upper_pair.png','upper field, right of first miniature, right mark','short pointed dark spot',r'\path[fill=black!70] (609.0,45.4) -- (610.0,48.1) -- (608.0,48.4) -- cycle;','high'),
('N03',[1656,52,1663,61],None,'far upper-right blank margin','tiny detached point',r'\path[fill=black] (1659.1,55.5) ellipse [x radius=0.65,y radius=1.0];','medium'),
('N04',[777,392,786,401],None,'gap below upper second oval, above right group','small gray speck',r'\path[fill=black!34] (780.4,396.3) ellipse [x radius=1.2,y radius=0.8];','medium'),
('N05',[213,442,220,453],'crops/08_triangle_upper_tick.png','detached immediately above left triangle apex','short upright tick separated from triangle',r'\draw[black,line width=0.28pt] (216.4,446.5) -- (216.4,450.1);','high'),
('N06',[270,479,278,488],None,'between left triangle and separate large point, above their baseline','very small detached gray dot',r'\path[fill=black!45] (273.4,484.0) ellipse [x radius=0.65,y radius=0.85];','medium'),
('N07',[437,479,448,490],'crops/09_gap_mark.png','gap before vertical loop, upper-left pale spot','diffuse small gray oval',r'\path[fill=black!16] (442.1,484.1) ellipse [x radius=1.7,y radius=2.5];','low'),
('N08',[449,496,458,508],'crops/09_gap_mark.png','gap before vertical loop, lower dark spot','dark droplet with a very short pale upright above',r'\draw[black!26,line width=0.22pt] (453.0,499.0) -- (453.1,501.0);'+'\n'+r'\path[fill=black] (453.0,501.1) -- (454.4,503.1) -- (453.7,505.0) -- (452.2,504.4) -- (452.0,503.2) -- cycle;','high'),
('N09',[903,499,912,507],'crops/04_connected_right_group.png','just above left portion of long upper horizontal rule','small pale slanted trace',r'\draw[black!30,line width=0.25pt] (906.4,503.1) -- (908.4,501.8);','medium'),
('N10',[1639,528,1648,537],'crops/04_connected_right_group.png','under far-right end of long horizontal rules','isolated dark pointed spot',r'\path[fill=black] (1644.0,530.7) -- (1645.2,533.3) -- (1642.9,533.9) -- (1642.8,532.4) -- cycle;','medium'),
('N11',[872,625,887,660],'crops/04_connected_right_group.png','right group, upper oval, pale left-rim interval','pale curved continuation between strong rim portions',r'\draw[black!32,line width=0.25pt] (882.8,628.8) .. controls (879.6,637.0) and (876.7,646.3) .. (876.5,656.6);','medium'),
('N12',[979,792,1018,818],'crops/04_connected_right_group.png','right group, upper oval, pale lower-right oblique rim','faint oblique rim fragment, with pale interruption at its lower end',r'\draw[black!24,line width=0.23pt] (985.3,811.9) .. controls (996.8,805.3) and (1005.5,798.5) .. (1014.6,793.6);','medium'),
('N13',[1028,818,1039,829],'crops/04_connected_right_group.png','right group, immediately below upper oval','small gray detached dot',r'\path[fill=black!46] (1033.6,823.1) ellipse [x radius=1.15,y radius=1.35];','medium'),
('N14',[1608,911,1625,927],'crops/04_connected_right_group.png','right group, upper descending curve, beyond strong lower-right terminal','pale slanted terminal continuation',r'\draw[black!28,line width=0.38pt] (1610.6,915.1) .. controls (1613.2,917.0) and (1616.0,919.2) .. (1619.0,921.2);','medium'),
('N15',[1653,787,1674,800],'crops/11_right_edge_dash.png','right page edge, at horizontal fold height','short heavy horizontal dash reaching toward paper edge',r'\draw[black,line width=0.55pt] (1657.0,793.2) .. controls (1661.0,792.9) and (1665.2,794.3) .. (1670.2,794.1);','high'),
('N16',[381,1285,416,1332],'crops/05_faint_lower_curve.png','lower field, left of centre, below drawing field','pale curved trace with left-turning lower foot',r'\draw[black!20,line width=0.21pt] (401.8,1288.6) .. controls (407.2,1294.6) and (411.0,1299.8) .. (411.0,1310.6) .. controls (410.3,1317.7) and (398.6,1323.8) .. (385.3,1324.1);','medium'),
('N17',[784,1425,794,1436],'crops/06_lower_dark_dot.png','lower field, roughly central','isolated dark compact droplet',r'\path[fill=black] (788.5,1427.3) .. controls (789.7,1427.3) and (790.2,1429.1) .. (790.8,1430.9) .. controls (790.4,1432.2) and (787.8,1432.0) .. (787.4,1430.7) -- cycle;','high'),
('N18',[652,1629,661,1638],None,'lower field, left of centre, above second large fold','tiny dark point',r'\path[fill=black!60] (656.7,1634.4) ellipse [x radius=0.55,y radius=0.75];','medium'),
('N19',[1448,1655,1459,1667],'crops/13_lower_gray_spot.png','lower-right field, above paired dots','small gray spot',r'\path[fill=black!25] (1454.4,1660.8) ellipse [x radius=1.0,y radius=1.45];','medium'),
('N20',[1525,1702,1534,1712],'crops/07_lower_paired_dots.png','lower-right field, upper of two neighbouring dark spots','upper pointed spot',r'\path[fill=black] (1529.1,1704.6) -- (1530.5,1707.0) -- (1528.4,1708.2) -- (1527.8,1706.6) -- cycle;','high'),
('N21',[1519,1709,1528,1719],'crops/07_lower_paired_dots.png','lower-right field, lower of two neighbouring dark spots','lower compact triangular spot',r'\path[fill=black] (1522.8,1712.0) -- (1525.0,1712.4) -- (1523.5,1714.6) -- (1522.4,1713.9) -- cycle;','high'),
('N22',[181,1789,190,1801],'crops/14_lower_left_speck.png','lower-left blank field','small point with dark core and gray perimeter',r'\path[fill=black!34] (185.5,1794.5) ellipse [x radius=0.9,y radius=1.4];','high'),
('N23',[694,1846,705,1860],'crops/15_lower_oblique.png','lower field, left of centre','faint short oblique gray trace',r'\draw[black!18,line width=0.55pt] (698.0,1855.3) -- (701.0,1850.2);','medium'),
('N24',[1355,1920,1367,1939],'crops/16_lower_fold_spot.png','lower-right field, just above fold','irregular compact spot with a separate smaller gray spot above',r'\path[fill=black!35] (1358.7,1928.1) -- (1360.3,1930.3) -- (1363.8,1931.8) -- (1361.0,1934.0) -- (1359.3,1935.6) -- cycle;'+'\n'+r'\path[fill=black!20] (1359.5,1923.9) ellipse [x radius=0.95,y radius=1.35];','medium'),
('N25',[667,1996,678,2007],'crops/17_lower_central_point.png','lower field, near centre-left below fold','small dark-cored oval point with gray perimeter',r'\path[fill=black!35] (672.7,2002.6) ellipse [x radius=0.85,y radius=1.2];','high'),
('N26',[482,2046,492,2057],None,'lower field, left of centre','tiny dark point',r'\path[fill=black!52] (487.3,2051.1) ellipse [x radius=0.65,y radius=0.65];','medium'),
('N27',[1441,2089,1453,2114],'crops/12_faint_low_vertical.png','lower-right field, pale upright trace','irregular pale upright with central darkening and a separate small upper spot',r'\draw[black!17,line width=0.25pt] (1446.2,2100.0) .. controls (1447.0,2103.5) and (1446.8,2107.3) .. (1448.0,2110.4);'+'\n'+r'\path[fill=black!22] (1445.0,2099.7) -- (1447.0,2100.1) -- (1448.2,2103.6) -- (1446.6,2105.0) -- (1444.9,2103.3) -- cycle;'+'\n'+r'\path[fill=black!17] (1447.0,2096.2) ellipse [x radius=0.6,y radius=1.2];','low'),
('N28',[1654,2184,1664,2196],None,'lower-right page edge','tiny diagonal dark tick',r'\draw[black!66,line width=0.20pt] (1657.3,2190.8) -- (1659.3,2189.2);','medium'),
('N29',[1413,2285,1423,2296],None,'near bottom, right of centre','tiny detached dark point',r'\path[fill=black!68] (1418.0,2290.5) ellipse [x radius=0.65,y radius=0.7];','medium'),
('N30',[681,2330,691,2341],None,'near bottom paper edge, left of centre','small dark short slant',r'\draw[black!55,line width=0.24pt] (685.6,2334.5) -- (687.2,2337.0);','medium'),
('N31',[1347,1948,1357,1959],'crops/16_lower_fold_spot.png','lower-right field, below-left of N24','small detached gray spot',r'\path[fill=black!18] (1351.7,1952.9) ellipse [x radius=1.0,y radius=1.3];','medium')
]
mark_records=[dict(id=i,bbox=b,crop=c,location=l,reading=r,tex=t,confidence=q,hand='undetermined hand',role='undetermined; no letter, punctuation, mathematical role, or surface origin assigned') for i,b,c,l,r,t,q in marks]
(OUT/'marks_manifest.json').write_text(json.dumps(mark_records,ensure_ascii=False,indent=2)+'\n')
scale=r'[x=0.0076cm,y=-0.0076cm,line join=round,line cap=round]'
lines=[r'\scanpage{12}',r'% Independent reader C. All coordinates refer to the original full scan.',r'% crop-candidate: scan 12',r'\figure{\begin{tikzpicture}'+scale]
for i,p in paths.items():
 if i not in heavy|right:
  lines += [f'% C source path {i:02d}; checked against the supplied page.',p]
# Genuine local unsure wrappers apply to the graphic, while all observed paths
# retain their coordinates. The shared lower miniature in path 34 remains live;
# uncertainty concerns the overlay on the large oval only.
lines += [r'% C.DR3: overlaid strokes on the large oval; cancellation/live function unresolved.',r'% Path 34 also includes the lower miniature; that miniature is not a proposed cancellation target.',r'\node[inner sep=0pt,anchor=north west] at (156.5,564) {\unsure{\begin{tikzpicture}'+scale,r'\path[use as bounding box] (156.5,564) rectangle (381.5,894.5);']
for i in sorted(heavy): lines += [f'% C source path {i:02d}; local graphic qualification only.',paths[i]]
lines += [r'\end{tikzpicture}}};',r'% Right group: visible curves/rules retained; cancelled/live status remains open.',r'% H states the whole corner is biff\'e; the local unsure wrapper preserves that open state.',r'\node[inner sep=0pt,anchor=north west] at (809.5,348.6) {\unsure{\begin{tikzpicture}'+scale,r'\path[use as bounding box] (809.5,348.6) rectangle (1648.4,1177.4);']
for i in sorted(right): lines += [f'% C source path {i:02d}; local graphic qualification only.',paths[i]]
lines += [r'\end{tikzpicture}}};']
for m in mark_records:
 lines += [f"% {m['id']}: {m['location']}; {m['reading']}.",'% Undetermined hand, role and surface origin; graphical shape only.',m['tex']]
labels=re.findall(r'\\node\[inner sep=0pt[^\n]*;',s)
lines += ['% Short labels: all retained after direct reading, with source doubts kept.']+labels+[r'\end{tikzpicture}}','% archive sheet number: 11','']
(OUT/'reading.tex').write_text('\n'.join(lines))
print('Built reading.tex:',len(paths),'source paths,',len(mark_records),'new visible-mark entries,',len(labels),'label nodes.')
