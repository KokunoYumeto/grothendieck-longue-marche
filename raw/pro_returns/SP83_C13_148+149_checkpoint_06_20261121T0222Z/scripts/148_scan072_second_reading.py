from pathlib import Path
import csv,json,hashlib,os
root=Path('/workspace/scratch/f28c4f52d3ec');page='148_scan072'
a=[r'\figure{\begin{tikzpicture}[x=.007cm,y=-.007cm,line cap=round,line join=round,every node/.style={inner sep=.5pt,font=\tiny}]']
def path(s,style='gray!80,line width=.35pt'):a.append(r'\draw['+style+'] '+s+';')
def dot(x,y,r=3,style='black'):a.append(r'\fill['+style+'] ('+str(x)+','+str(y)+') circle[radius='+str(r)+'];')
def node(x,y,s,style=''):a.append(r'\node['+style+'] at ('+str(x)+','+str(y)+') {'+s+'};')
node(1615,135,r"découpage pantalonesque\\d'une carte (triangulée)",'anchor=north west,align=left,font=\\scriptsize')
# Large gray/black triangulated drawing. Named coordinates are internal, not source labels.
vertices={'A':(1073,263),'B':(583,469),'C':(915,480),'D':(767,590),'E':(1284,660),'F':(573,811),'G':(819,825),'H':(1018,779),'I':(706,992),'J':(939,953),'K':(1221,977)}
for name,(x,y) in vertices.items():a.append(r'\coordinate ('+name+') at ('+str(x)+','+str(y)+');')
for s in ['(A)--(B)','(A)--(C)','(A) .. controls (1160,385) and (1265,540) .. (E)','(B)--(C)','(B)--(D)','(B) .. controls (560,615) and (558,715) .. (F)','(C)--(D)','(C) .. controls (880,596) and (837,725) .. (G)','(C)--(H)','(C)--(E)','(D)--(F)','(D)--(G)','(F)--(G)','(F)--(I)','(G)--(H)','(G)--(I)','(G)--(J)','(H)--(E)','(H)--(J)','(H)--(K)','(I)--(J)','(J)--(K)','(K)--(E)']:
 path(s)
# Independent parallel retracing of the C--G run is visible.
path('(910,493) .. controls (870,602) and (815,734) .. (810,801)','gray!65,line width=.24pt')
# Source-darkened portions and external runs are uneven rather than uniform arrows.
for s in ['(B)--(D)','(D)--(G)','(F)--(I)','(C)--(H)','(G)--(J)']:path(s,'black,line width=.36pt')
path('(B) .. controls (445,445) and (337,319) .. (212,217)','black,line width=.4pt')
path('(212,217)--(224,219) (212,217)--(222,225)','black,line width=.28pt')
path('(A) .. controls (1125,200) and (1184,122) .. (1233,83)')
path('(1228,86)--(1233,83)--(1231,89)','gray!85,line width=.28pt')
path('(F) .. controls (450,859) and (330,892) .. (220,913)')
path('(I) .. controls (674,1115) and (621,1217) .. (570,1286)')
path('(570,1286)--(570,1277)','gray!80,line width=.28pt')
path('(J) .. controls (938,1104) and (938,1265) .. (947,1347)')
path('(K)--(1447,1175)','black,line width=.34pt')
path('(E) .. controls (1425,623) and (1600,601) .. (1712,608)')
for name,(x,y) in vertices.items():dot(x,y,3.5,'black' if name in ['C','D','G','H'] else 'gray!80')
# Irregular red circles at the eleven visible junctions.
rings=[
'(1053,247) .. controls (1070,231) and (1088,241) .. (1094,261) .. controls (1095,281) and (1073,293) .. (1059,278) .. controls (1049,267) and (1046,256) .. (1053,247)',
'(563,458) .. controls (573,443) and (600,448) .. (609,461) .. controls (612,478) and (600,491) .. (582,488) .. controls (567,486) and (559,470) .. (563,458)',
'(900,461) .. controls (916,453) and (928,461) .. (931,482) .. controls (931,497) and (916,506) .. (903,495) .. controls (895,487) and (895,470) .. (900,461)',
'(751,576) .. controls (763,565) and (780,568) .. (782,582) .. controls (779,588) and (787,594) .. (780,602) .. controls (766,616) and (751,609) .. (750,598) .. controls (747,590) and (746,583) .. (751,576)',
'(1264,638) .. controls (1278,620) and (1300,625) .. (1308,649) .. controls (1313,671) and (1297,694) .. (1279,692) .. controls (1269,690) and (1255,660) .. (1264,638) (1275,690)--(1286,698)',
'(555,798) .. controls (569,780) and (588,787) .. (592,806) .. controls (599,826) and (586,839) .. (568,834) .. controls (548,829) and (549,813) .. (555,798)',
'(804,807) .. controls (817,789) and (832,802) .. (834,823) .. controls (834,846) and (816,857) .. (803,839) .. controls (797,826) and (798,815) .. (804,807)',
'(1001,765) .. controls (1015,750) and (1035,761) .. (1035,779) .. controls (1035,799) and (1017,808) .. (1003,797) .. controls (996,789) and (994,775) .. (1001,765)',
'(689,980) .. controls (698,967) and (715,972) .. (723,984) .. controls (728,996) and (713,1004) .. (700,1003) .. controls (683,1000) and (681,991) .. (689,980) (696,1000) .. controls (712,1014) and (729,1004) .. (724,997)',
'(922,942) .. controls (936,931) and (953,938) .. (959,952) .. controls (962,968) and (940,976) .. (923,965) .. controls (915,960) and (913,949) .. (922,942)',
'(1203,957) .. controls (1215,941) and (1235,948) .. (1244,969) .. controls (1250,992) and (1233,1008) .. (1213,1001) .. controls (1196,995) and (1192,970) .. (1203,957)']
for s in rings:path(s,'red!35!black,line width=.38pt')
# Eight long contour runs, individually traced. The outer run has the visible gap near (950,1165).
contours=[
'(957,1158) .. controls (1035,1109) and (1112,1035) .. (1171,933) .. controls (1220,862) and (1245,751) .. (1242,640) .. controls (1245,565) and (1253,481) .. (1245,430) .. controls (1238,345) and (1170,249) .. (1118,218) .. controls (1090,210) and (1050,222) .. (1015,219) .. controls (985,221) and (974,211) .. (950,212) --(778,213) .. controls (614,213) and (492,302) .. (417,403) .. controls (357,491) and (340,549) .. (345,640) .. controls (344,704) and (366,741) .. (366,800) .. controls (371,859) and (376,909) .. (372,940) .. controls (362,968) and (362,1000) .. (373,1030) .. controls (412,1114) and (541,1160) .. (690,1205) .. controls (785,1224) and (881,1198) .. (943,1168)',
'(845,282) .. controls (944,276) and (1033,282) .. (1070,296) .. controls (1120,308) and (1148,372) .. (1171,425) .. controls (1195,492) and (1207,550) .. (1210,600) .. controls (1217,681) and (1232,722) .. (1224,774) .. controls (1218,850) and (1183,907) .. (1167,938) .. controls (1124,974) and (1020,995) .. (943,1018) .. controls (839,1090) and (775,1118) .. (717,1110) .. controls (632,1111) and (524,1054) .. (465,1010) .. controls (423,979) and (416,943) .. (413,886) .. controls (408,812) and (416,745) .. (417,640) .. controls (420,536) and (430,453) .. (453,411) .. controls (466,389) and (476,375) .. (486,369) .. controls (568,322) and (701,286) .. (845,282)',
'(990,309) .. controls (1042,304) and (1090,327) .. (1124,372) .. controls (1156,425) and (1179,516) .. (1183,600) .. controls (1184,688) and (1195,748) .. (1180,811) .. controls (1169,869) and (1154,897) .. (1121,915) .. controls (1074,931) and (1010,920) .. (950,930) .. controls (871,943) and (827,999) .. (735,1040) .. controls (677,1052) and (627,1014) .. (570,966) .. controls (533,942) and (496,929) .. (475,887) .. controls (461,836) and (472,753) .. (474,684) .. controls (478,609) and (472,540) .. (476,475) .. controls (477,438) and (491,413) .. (509,402) .. controls (549,365) and (599,358) .. (650,355) .. controls (769,353) and (865,322) .. (990,309)',
'(965,339) .. controls (1020,338) and (1049,351) .. (1068,396) .. controls (1094,448) and (1126,522) .. (1140,600) .. controls (1148,669) and (1147,744) .. (1131,802) .. controls (1118,859) and (1086,883) .. (1035,892) .. controls (930,915) and (812,954) .. (725,974) .. controls (685,983) and (666,933) .. (651,904) .. controls (634,882) and (605,886) .. (572,890) .. controls (543,893) and (519,874) .. (510,842) .. controls (501,796) and (520,732) .. (521,666) .. controls (524,613) and (504,553) .. (501,503) .. controls (498,462) and (530,430) .. (563,412) .. controls (599,392) and (694,396) .. (750,387) .. controls (831,376) and (904,337) .. (965,339)',
'(924,359) .. controls (967,356) and (1003,407) .. (1024,455) .. controls (1065,527) and (1090,623) .. (1105,703) .. controls (1117,751) and (1127,802) .. (1103,832) .. controls (1078,865) and (1007,881) .. (930,905) .. controls (850,929) and (782,961) .. (731,960) .. controls (694,960) and (685,928) .. (682,886) .. controls (681,791) and (681,710) .. (666,643) .. controls (654,592) and (643,558) .. (622,550) .. controls (610,539) and (596,538) .. (583,536) .. controls (554,516) and (536,494) .. (539,469) .. controls (541,452) and (556,438) .. (576,433) .. controls (640,419) and (720,432) .. (765,428) .. controls (809,421) and (849,396) .. (879,380) .. controls (897,369) and (911,361) .. (924,359)',
'(914,386) .. controls (946,379) and (974,418) .. (989,450) .. controls (1023,497) and (1056,567) .. (1068,600) .. controls (1086,669) and (1092,741) .. (1089,785) .. controls (1094,823) and (1070,842) .. (1045,850) .. controls (958,881) and (859,916) .. (785,931) .. controls (755,941) and (730,939) .. (717,921) .. controls (705,900) and (706,876) .. (709,843) .. controls (714,742) and (727,672) .. (734,600) .. controls (738,571) and (739,550) .. (750,537) .. controls (791,498) and (834,448) .. (885,403) .. controls (897,391) and (905,387) .. (914,386)',
'(914,423) .. controls (924,421) and (934,426) .. (944,430) .. controls (963,448) and (974,476) .. (985,511) .. controls (1001,566) and (1026,683) .. (1037,767) .. controls (1038,778) and (1047,786) .. (1050,798) .. controls (1049,810) and (1025,810) .. (1004,815) .. controls (958,836) and (906,853) .. (858,871) .. controls (817,890) and (790,909) .. (765,912) .. controls (738,911) and (731,889) .. (734,861) .. controls (740,808) and (772,727) .. (793,677) .. controls (825,606) and (848,540) .. (860,506) .. controls (866,493) and (870,482) .. (875,477) .. controls (883,448) and (886,428) .. (914,423)',
'(914,448) .. controls (929,445) and (941,464) .. (947,482) .. controls (955,508) and (939,532) .. (930,557) .. controls (903,633) and (872,735) .. (849,809) .. controls (843,840) and (833,867) .. (817,875) .. controls (800,884) and (779,874) .. (777,850) .. controls (770,822) and (785,779) .. (795,749) .. controls (823,666) and (856,574) .. (881,501) .. controls (890,476) and (891,450) .. (914,448)'
]
for s in contours:path(s,'red!35!black,line width=.34pt')
# Short red barbs and thickened marks are drawn individually, without imposing uniform orientation.
for s in ['(950,1165)--(957,1158)','(1010,218)--(1017,222)--(1021,218)','(368,946)--(373,934)','(482,372)--(486,369)--(491,373)','(838,283)--(845,281)--(847,284)','(506,406)--(511,400)--(514,405)','(558,415)--(563,411)--(565,416)','(572,434)--(578,430)--(581,436)','(874,384)--(879,380)--(881,385)','(1065,393)--(1069,400)--(1070,393)','(745,542)--(750,536)--(751,543)','(886,448)--(889,439)--(894,440)','(1035,894)--(1041,892)--(1044,896)','(1145,911)--(1151,907)--(1155,910)','(692,952)--(697,955)','(734,957)--(740,960)']:
 path(s,'red!35!black,line width=.55pt')
for x,y in [(1118,218),(1015,219),(944,430),(875,477),(860,506),(985,511),(793,677),(1037,767),(1042,800),(1004,815),(858,871),(1234,669),(1237,744)]:dot(x,y,2.9,'red!35!black')
# Small unlabelled hooked trace inside the large drawing; it is not assigned a numeral.
path('(924,597) .. controls (923,606) and (920,611) .. (917,612)','gray!80,line width=.23pt')
# Smaller weighted graph, at its source position. Eight junctions, unequal legs and an asymmetric loop.
small={'L':(1560,822),'T':(1750,724),'U':(1960,750),'R':(1980,879),'D':(1890,980),'V':(1615,968),'Q':(1576,1038),'W':(1978,1067)}
for name,(x,y) in small.items():a.append(r'\coordinate (m'+name+') at ('+str(x)+','+str(y)+');')
for s in ['(mL)--(mT)','(mT) .. controls (1825,735) and (1895,738) .. (mU)','(mU) .. controls (1961,790) and (1980,849) .. (mR)','(mR)--(mD)','(mD)--(mV)','(mV)--(mL)','(mV)--(mQ)','(mD)--(mW)']:
 path(s,'black,line width=.34pt')
path('(mL)--(1490,805) (mT)--(1740,652) (mU) .. controls (1984,710) and (2005,682) .. (2015,648) (mR) .. controls (2025,874) and (2070,870) .. (2100,872) (mQ)--(1504,1088) (mQ)--(1592,1112)','black,line width=.4pt')
path('(mW) .. controls (2036,1034) and (2101,1005) .. (2131,1041) .. controls (2167,1081) and (2115,1093) .. (2078,1093) .. controls (2044,1091) and (2000,1074) .. (mW)','gray!90,line width=.32pt')
for x,y in small.values():dot(x,y,4)
dot(2080,872,3.4)
# Short loose marks visible beside the weighted graph.
path('(1490,805)--(1494,810) (1559,813)--(1564,816) (1857,992)--(1856,997)','gray!85,line width=.25pt')
weights=[
(1529,800,'3'),(1564,790,'6'),(1595,848,r'\unsure{25|15}'),
(1728,694,'9'),(1726,762,r'\unsure{1|2}'),(1792,757,'9'),
(1984,741,'3'),(1927,768,'3'),(1980,782,'7'),
(1959,857,'2'),(1968,908,'1'),(2015,898,'5'),
(1863,970,'4'),(1909,946,'2'),(1927,992,'3'),
(1614,930,'1'),(1660,959,'5'),(1612,996,'4'),
(1536,1045,'4'),(1603,1065,'2'),
(1944,1065,'17'),(2002,1037,'3'),(2000,1098,'3')]
assert len(weights)==23
for x,y,t in weights:node(x,y,'$'+t+'$')
# Uneven pencil circles around the source 1,2,3 labels are not converted into a new notation.
path('(1604,915) .. controls (1617,902) and (1636,915) .. (1628,936) .. controls (1622,946) and (1608,945) .. (1601,937) .. controls (1597,929) and (1599,921) .. (1604,915)','gray!80,line width=.24pt')
path('(1896,936) .. controls (1906,924) and (1925,932) .. (1923,946) .. controls (1922,958) and (1909,963) .. (1898,953) .. controls (1890,947) and (1891,942) .. (1896,936)','gray!80,line width=.24pt')
path('(1918,980) .. controls (1927,972) and (1945,982) .. (1941,994) .. controls (1938,1007) and (1923,1009) .. (1915,1001) .. controls (1910,991) and (1912,985) .. (1918,980)','gray!80,line width=.24pt')
# Local retracing, without assigning a deleted earlier digit.
path('(1781,750) .. controls (1785,741) and (1799,744) .. (1800,752) .. controls (1795,758) and (1783,758) .. (1781,750)','gray!80,line width=.22pt')
a.append(r'\end{tikzpicture}}')
readings={'B01':'\n'.join(a),'B02':r'\margin{71}'}
# Ensure only the standard single-backslash font command occurs in the generated TikZ option.
readings['B01']=readings['B01'].replace('font=\\\\scriptsize','font=\\scriptsize')
expected=['B01','B02'];assert list(readings)==expected
out=root/'result/second'/f'{page}_second.tsv'
if out.exists():raise RuntimeError('Refusing to overwrite an existing independent TSV')
# Static structure checks, without TeX compilation.
for box,text in readings.items():
 depth=0
 for i,ch in enumerate(text):
  if ch not in '{}':continue
  n=0;j=i-1
  while j>=0 and text[j]=='\\':n+=1;j-=1
  if n%2:continue
  depth+=1 if ch=='{' else -1
  assert depth>=0,(box,'negative brace balance')
 assert depth==0,(box,'brace balance')
 assert text.count('$')%2==0,(box,'math dollar balance')
 assert text.count(r'\begin{tikzpicture}')==text.count(r'\end{tikzpicture}')
with out.open('w',encoding='utf-8',newline='') as h:
 w=csv.writer(h,delimiter='\t',lineterminator='\n');w.writerow(['box','reading'])
 for box in expected:w.writerow([box,readings[box]])
back=list(csv.DictReader(out.open(encoding='utf-8',newline=''),delimiter='\t'))
assert [r['box'] for r in back]==expected
assert all(r['reading']==readings[r['box']] for r in back)
sha=hashlib.sha256(out.read_bytes()).hexdigest()
(root/'result/second'/f'{page}_second.sha256').write_text(sha+'  '+out.name+'\n')
manifest_path=root/'result/second'/f'{page}_second_crop_manifest.json';manifest=json.loads(manifest_path.read_text())
for c in manifest['crops']:
 c['viewed']=True;c['view_method']='verified pixel-identical lossless WebP transport' if c['box']=='B01' else 'canonical PNG'
for h in manifest['helpers']:h['viewed']=True
manifest['complete_independent_reading_frozen_sha256']=sha
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
notes={
 'page':page,'reader':'reader_c','phase':'blind independent second reading',
 'allowed_inputs_only':True,'comparison_seen':False,'first_reading_seen':False,
 'source':'source/SP83_C13_148+149_scans/148_scan072.jpg',
 'original_directly_viewed_once':True,'box_count':2,
 'canonical_crop_paths':[f'result/crops/{page}_second_B01.png',f'result/crops/{page}_second_B02.png'],
 'all_prescribed_fields_directly_viewed':True,
 'transport':'B01 canonical PNG was 6202855 bytes. A lossless WebP of identical dimensions and verified decoded pixel equality was directly viewed. The canonical PNG is retained.',
 'helper_paths':[h['path'] for h in manifest['helpers']],
 'boundaries':{
  'B01':'Entire target caption, large drawing, numerical graph and all external line ends are within the prescribed box. Top and bottom branch ends have narrow but sufficient padding. No target is clipped. The two contour helpers intentionally cover overlapping parts; the canonical full-field view supplied the complete drawing.',
  'B02':'Complete folio 71 with no clipped digit. Hand: unnamed hand (folio annotation; attribution uncertain).'
 },
 'independent_observations':{
  'caption':"découpage pantalonesque / d'une carte (triangulée), with the two lines at the upper right; no deletion or insertion identified.",
  'large_drawing':'Eleven gray/black junctions carry irregular red circles. All visible internal and external gray/black runs are drawn; the doubled C--G-like central run is preserved as retracing, with internal coordinate names not printed. Eight long red contour runs are separately traced. The outermost run has a visible gap near its lower-right junction with the vertical branch, retained with its detached short stroke. Red barbs, thicker points, and the small unlabelled interior hook are retained without mathematical labels.',
  'small_drawing':'Eight junctions, six-sided central circuit, lower-left branching leg, lower-right asymmetric loop, and all external legs are drawn. Twenty-three numerical labels are recorded in source positions, including separately pencilled circles around 1,2,3. The nearby doubled head of the upper 9 is retained as retracing; no deletion chronology is inferred.',
  'unresolved_numbers':[
   {'position':'near left circuit vertex, beside its descending edge','reading':'25|15','reason':'First digit is heavily retraced; an angled upper stroke and low base favor 2, but 1 remains plausible.'},
   {'position':'below-left of the upper circuit vertex','reading':'1|2','reason':'Dark upright and lower horizontal base favor 1, but the enlarged retraced head does not exclude 2.'}
  ],
  'numeric_inventory':[{'x':x,'y':y,'reading':t} for x,y,t in weights],
  'ink_state':'No text cancellation is asserted. Local overwritten numerals and graphic retracing are preserved without inventing earlier text.'
 },
 'diagram_method':'Manual source-only TikZ tracing with approximate pixel coordinates. No topology or weight-consistency argument was used to alter the ink reading.',
 'no_ocr':True,'no_web':True,'no_tex_compilation':True,
 'verification':'Exact row order, CSV/TSV roundtrip, brace/dollar/environment balance; no comparison with a first reading.',
 'frozen_sha256':sha,'frozen_before_any_comparison':True
}
(root/'result/second'/f'{page}_second_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
os.chmod(out,0o444)
print(json.dumps({'path':str(out),'rows':len(back),'sha256':sha,'bytes':out.stat().st_size,'canonical_crops':2,'helpers':4},indent=2))
