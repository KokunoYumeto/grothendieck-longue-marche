import sys
sys.path.insert(0,'out/scripts');from work import crop
for label,box,scale in [('top',(270,238,1664,579),2),('hom_category',(267,603,1661,739),3),('localisable',(263,929,1658,1118),3),('condition',(270,1109,1658,1219),3),('parta',(269,1240,1657,1516),3),('functor',(269,1530,1658,1709),3),('handnote',(262,1670,1657,1750),4),('partb',(270,1747,1662,2087),3),('deleted_ring',(799,475,1034,517),7),('hom_tensor',(1125,612,1184,657),9),('category_delete',(644,687,826,722),7),('en_delete',(997,661,1083,719),8),('category_A',(1036,688,1092,723),9),('pour_correction',(1044,828,1094,866),10),('after_champ',(1094,1042,1569,1082),5),('condition_s',(742,1116,795,1148),10),('On_n',(1060,1115,1113,1161),9),('soit_correction',(374,1255,462,1293),8),('deleted_E',(468,1253,505,1287),10),('op_R',(725,1325,768,1363),10),('R_index',(1190,1388,1251,1445),9),('b_R',(467,1813,512,1854),10),('b_P',(466,1960,512,2001),10),('lastP',(1365,1971,1406,2009),10),('marginC',(101,642,160,711),8)]:crop(15,81,label,box,scale)
for label,box,scale in [('note_est',(1576,1670,1669,1721),9),('note_formee',(266,1703,455,1755),7),('note_Xprime',(509,1702,630,1754),7),('affine_anchor',(617,922,859,1007),6),('body1',(270,749,1672,929),3)]:crop(15,81,label,box,scale)
from pathlib import Path
from PIL import Image
for label,box,angle in [('note_line1_upright',(1127,1668,1669,1718),1),('note_line2_upright',(262,1703,1527,1756),0.3)]:
 im=Image.open('source/SP14_CW_13+15+26+35+48+66+97+123+162_scans/B15-01_15_scan081.jpg').crop(box);im=im.resize((im.width*4,im.height*4)).rotate(angle,expand=True,fillcolor='white');p=Path('work/crops')/('B15-01_15_scan081_'+label+'.png');im.save(p)
 with Path('out/crop_manifest.tsv').open('a') as f:f.write('\t'.join([p.name,'B15-01_15_scan081.jpg',','.join(map(str,box)),'4',str(angle)])+'\n')
for label,box,scale in [('grossiere_end',(273,896,324,936),10),('SpecS',(926,757,975,796),10),('hand_a_letter',(607,1066,651,1110),10)]:crop(15,81,label,box,scale)
for label,box,scale in [('droite_type',(274,1394,407,1434),8),('qui_type',(854,1895,940,1943),8)]:crop(15,81,label,box,scale)
crop(15,81,'qui_correct',(601,1895,673,1941),9)
