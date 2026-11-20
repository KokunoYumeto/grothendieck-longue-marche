from PIL import Image, ImageOps
from pathlib import Path
import json
root=Path('/workspace/scratch/7178efd1cfac/SP48_CW_104/records/scan005/reader_C')
src=Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans/H104-01_104_scan005.jpg')
im=Image.open(src)
items=[
('01_top_chain',[55,85,1118,228],3000),
('02_chain_end_mark',[1115,90,1260,185],2200),
('03_upper_trial',[150,403,1220,755],3200),
('04_F_array',[1405,180,1680,550],2200),
('05_small_arrows',[1400,470,1920,760],2600),
('06_Ci_opening',[1715,65,2340,355],3000),
('07_Ci_boundaries',[1918,350,2350,643],2600),
('08_Ci_equalities',[1950,625,2350,790],2600),
('09_Ci_ending',[1825,770,2350,1078],3000),
('10_E0_a',[30,805,1055,925],3000),
('11_pi0_surj',[1230,800,1605,955],2500),
('12_E1_arrow',[1370,1050,1670,1190],2300),
('13_E1_cancel',[945,1160,1110,1255],2200),
('14_c_opening',[170,1260,1085,1385],3000),
('15_c_target',[1655,1220,2350,1370],3000),
('16_cp_cancel',[1570,1430,1950,1635],2600),
('17_lower_drawing',[1090,1535,1215,1668],2200),
('18_final_pi',[1958,1350,2350,1525],2600)
]
manifest=[]
for name,box,width in items:
 out=root/'crops'/f'{name}.png'
 c=ImageOps.autocontrast(im.crop(box),cutoff=0)
 c=c.resize((width,round(c.height*width/c.width)),Image.Resampling.LANCZOS)
 c.save(out)
 manifest.append({'path':str(out),'source':str(src),'bbox':box,'rotation_degrees':0,'autocontrast':'Pillow ImageOps.autocontrast cutoff=0','resize':'LANCZOS','output_dimensions':list(c.size),'sharpening':'none','viewed':False})
(root/'crop_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(len(manifest),'crops saved')
