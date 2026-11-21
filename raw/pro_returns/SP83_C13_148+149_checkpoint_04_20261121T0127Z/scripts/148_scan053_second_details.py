from pathlib import Path
from PIL import Image
base=Path('/workspace/scratch/f28c4f52d3ec/result/crops')
parts=[('B24','upper',(350,600,2480,1450)),('B24','middle',(0,1200,2400,2100)),('B25','lower',(0,600,2350,1850)),('B25','end',(0,1400,2300,2700))]
for box,name,rect in parts:
 im=Image.open(base/f'148_scan053_second_{box}.png').crop(rect)
 im=im.resize((round(im.width*1.5),round(im.height*1.5)),Image.Resampling.LANCZOS)
 im.save(base/f'148_scan053_second_detail_{name}.png')
