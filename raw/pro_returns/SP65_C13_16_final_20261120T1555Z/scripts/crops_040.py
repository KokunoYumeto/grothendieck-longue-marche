from PIL import Image,ImageOps
from pathlib import Path
im=Image.open('source/SP65_C13_16_scans/16_scan040.jpg')
boxes={'upper_bound':(620,395,795,455),'cancel_sum':(548,442,615,495),'p_exp':(1125,425,1220,490),'equivaut':(1215,1065,1470,1170),'insert':(380,1540,535,1685),'inequality':(1080,1535,1260,1605),'cancel_word':(1400,1505,1530,1570),'quantifier':(682,1760,790,1830),'last_words':(245,1855,820,1945),'last_bound':(1180,1825,1360,1910)}
for name,box in boxes.items():
 out=Path('views')/('040_'+name+'.png');assert not out.exists()
 c=ImageOps.autocontrast(im.crop(box));w=2600 if c.width>500 else 1400;c.resize((w,round(c.height*w/c.width)),Image.Resampling.LANCZOS).save(out)
print(boxes)
