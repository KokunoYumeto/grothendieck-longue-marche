from pathlib import Path
from PIL import Image, ImageOps
import json
root=Path('/workspace/scratch/7178efd1cfac/SP48_CW_104/records/scan006/reader_B')
source=Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans/H104-01_104_scan006.jpg')
items=[
 ('01_typed_strip',[105,65,452,1455],-90,3000,'Read sideways type and character spacing; 0/O, missing membership.'),
 ('02_top_symbols',[630,35,1230,215],0,2700,'Initial D alphabet, N alphabet, struck superseded letter.'),
 ('03_qualifiers',[1230,255,1680,540],0,2700,'Struck N, I alphabet, croissante, image qualifier and struck subscript.'),
 ('04_text_lines',[605,710,1555,905],0,3200,'ens/un; famille/échelle; accents and ordonnés.'),
 ('05_map_label',[560,895,835,1018],0,2400,'Full overwritten map label and live letter.'),
 ('06_struck_opening',[855,1045,1310,1155],0,2500,'Canceled Soit/Sinon l\'ens K.'),
 ('07_subset_definition',[1435,1028,1970,1280],0,2850,'Subset capital, index and defining map label.'),
 ('08_struck_soit',[650,1235,1105,1330],0,2400,'Canceled Soit x membership and capital/index.'),
 ('09_considérons',[585,1298,1570,1425],0,3200,'Considérons, canceled D and final large B.'),
 ('10_xy_array',[1685,682,2140,1045],0,2700,'Canceled connector/equality and D; vertical links and curved strokes.'),
 ('11_sideways_note',[2085,235,2345,1218],90,3200,'All margin objects, labels, vertical memberships, cancellation and unfinished equality.'),
 ('12_loop',[780,1530,960,1645],0,2300,'Loop endpoint, point label and gap; compare actual H drawing.'),
 ('13_lower_sketch',[1860,1230,2090,1430],0,2300,'Arrow endpoint knots, separate point and low segment return.'),
 ('14_footer',[1030,1500,2110,1645],0,3500,'F index, abbreviations and words in pi_0 definition.')
]
im=Image.open(source)
log=[]
for name,bbox,rotation,width,purpose in items:
 out=im.crop(tuple(bbox))
 if rotation: out=out.rotate(rotation,expand=True)
 out=ImageOps.autocontrast(out,cutoff=0)
 out=out.resize((width,round(out.height*width/out.width)),Image.Resampling.LANCZOS)
 path=root/'crops'/(name+'.png')
 out.save(path)
 log.append({'path':str(path),'bbox':bbox,'rotation_degrees_counterclockwise':rotation,'autocontrast_cutoff':0,'resize_filter':'LANCZOS','output_dimensions':list(out.size),'sharpening':'none','purpose':purpose})
(root/'processing_log.json').write_text(json.dumps({'source':str(source),'source_dimensions':list(im.size),'processing':log},ensure_ascii=False,indent=2)+'\n')
print('Created',len(log),'decision crops; no recognition, OCR, rendering or compilation used.')
