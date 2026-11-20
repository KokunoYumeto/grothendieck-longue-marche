from pathlib import Path
from PIL import Image,ImageOps,ImageFilter,ImageChops,ImageStat
import json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/016/A'
src=root/'source/SP40_CW_81_scans/J81-02_81_scan016.jpg'
im=Image.open(src)
halves={}
for suffix,y0 in [('a',0),('b',1101)]:
 half=Image.open(root/f'source/SP40_CW_81_scans/J81-02_81_scan016_{suffix}.jpg')
 delta=ImageChops.difference(im.crop((0,y0,1685,y0+1261)),half)
 halves[suffix]={'size':half.size,'full_origin':[0,y0],'mean_absolute_channel_difference':ImageStat.Stat(delta).mean}
crops=[
 ('crop01_opening', [780,60,1100,177], 'Overwritten union subscript and cancelled word before est'),
 ('crop02_right_top', [1120,94,1685,280], 'Connexe; raised insertions, boundary notation and guide paths'),
 ('crop03_line3', [398,263,1260,377], 'Cancelled c\u2019est, ending of \u00e9gale, following small sign and donc'),
 ('crop04_partition1', [605,588,795,686], 'Predecessor under first Sigma in first partition'),
 ('crop05_partition5', [927,833,1166,995], 'Predecessor under central Sigma12 and adjacent brace endpoints'),
 ('crop06_dans', [245,1190,452,1323], 'Overwritten initial of Dans'),
 ('crop07_lower_overwrites', [985,2005,1460,2119], 'Two overwritten letters in first lower hypothesis'),
 ('crop08_conclurait', [279,2104,1063,2227], 'Raised replacement en conclurait and cancelled alors expression'),
 ('crop09_lower_joins', [600,2219,1098,2315], 'Two crowded joins under long final overbar'),
 ('crop10_bottom_right', [1100,2200,1685,2362], 'Final underbrace, endpoint inclusion and cut right closing bracket'),
 ('crop11_right_dots', [1540,1670,1685,1785], 'Isolated small paired traces right of third closure row'),
 ('crop12_detached_dot', [780,1840,1010,1955], 'Detached small mark above second lower intersection condition')
]
report=[]
for stem,box,purpose in crops:
 crop=ImageOps.autocontrast(im.crop(box))
 width=2600 if box[2]-box[0]>250 else 1800
 crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 name=stem+'.png'
 crop.save(out/name)
 report.append({'path':name,'bbox':box,'rotation':0,'purpose':purpose,'pixels':crop.size})
(out/'crop_manifest.json').write_text(json.dumps({'source':str(src),'halves':halves,'crops':report},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'half_coordinate_verification':halves,'crops_created':len(report),'manifest':str(out/'crop_manifest.json')},ensure_ascii=False))
