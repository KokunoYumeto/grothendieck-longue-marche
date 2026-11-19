import sys
sys.path.insert(0,'out/scripts')
from work import crop,S,OUT,ROOT
from PIL import Image,ImageOps
for lab,box in [('alphabet',(530,22,1050,70)),('first_Gm',(38,257,111,321)),('frame_letter',(408,510,454,556)),('point_xi',(1427,270,1468,346)),('b_indices',(952,500,1035,785)),('c_labels',(1198,773,1394,828)),('square_w',(365,915,470,978)),('alpha1',(480,1215,540,1273)),('sont',(198,1572,265,1615)),('epsilon',(1025,1544,1045,1582)),('frob_accent',(1405,1620,1498,1681)),('pi1_field',(1177,1860,1256,1913)),('half_simple',(1454,1900,1522,1968)),('un_underline',(450,1980,525,2040)),('subgroup_underline',(495,1904,739,1952)),('ct_dot',(1584,2060,1650,2119))]:crop(13,37,lab,box,5)
im=Image.open(S/'J13-03_13_scan037.jpg')
for lab,box,ang in [('margin_upright',(18,1730,160,1850),30),('cancelled_principal_upright',(230,551,809,705),-3),('cancelled_9_upright',(238,1943,847,2020),0),('deleted_seul_upright',(702,1970,930,2034),0),('bottom_cancel_upright',(139,2080,961,2143),0),('six_upright',(950,2023,1655,2126),0)]:
 a=im.crop(box).resize(((box[2]-box[0])*3,(box[3]-box[1])*3)).rotate(ang,expand=True,fillcolor='white');p=ROOT/'work/crops'/f'J13-03_13_scan037_{lab}.png';a.save(p)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{p.name}\t{S}/J13-03_13_scan037.jpg\t{box}\t3\t{ang}\n')
a=ImageOps.grayscale(im).point(lambda p:max(0,min(255,(p-185)*255/65))).rotate(90,expand=True);p=ROOT/'work/crops/J13-03_13_scan037_watermark_upright_levels.png';a.save(p)
with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{p.name}\t{S}/J13-03_13_scan037.jpg\twhole\t1\t90; levels 185-250\n')
