from PIL import Image, ImageOps
from pathlib import Path
import json
root=Path('/workspace/scratch/17347c1714f0/out/readers/scan006/R3')
sources=Path('/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans')
specs=[
('opening','a',(255,74,1550,178),0,3000,'Opening script letter and words aussi / somme amalgamée'),
('first_de','a',(266,203,394,266),0,2600,'First de ending and cancellation'),
('second_de','a',(680,203,782,262),0,2600,'Second de ending and cancellation'),
('sur','a',(970,174,1104,283),0,2600,'Word introducing the span diagram'),
('cancelled_heading','a',(816,328,1515,426),0,3000,'Cancelled L’application naturelle'),
('cancelled_map','a',(827,443,1407,531),0,3000,'Cancelled cluster preceding script X and cancelled map'),
('drawing_centre','a',(300,550,531,753),0,2800,'All centre labels and transverse ticks on three branches'),
('drawing_cusp','a',(302,825,378,904),0,2600,'Small return edge where the lower lobes meet'),
('main_operator','a',(836,524,1445,698),0,3000,'Amalgamation display and overwritten operator'),
('coproduct_suffix','a',(985,700,1240,818),0,2800,'Letter in parentheses at the coproduct index'),
('side_display','a',(1356,678,1652,917),0,3000,'Right display suffix, vertical strokes and arrowed gloss'),
('imm','a',(443,1125,638,1199),0,2800,'Compressed word before fermée'),
('interlinear_stars','b',(935,332,1245,427),0,2800,'Two raised angular marks in inserted primed U formula'),
('slanted_note','b',(24,394,266,711),-47,3000,'Slanted three-line verification note'),
('replaced_condition','b',(287,494,841,668),0,3000,'Inserted and cancelled K conditions including dotted and primed marks'),
('cancelled_parenthesis','b',(863,508,1140,618),0,2800,'Cancelled complement and final raised short sign'),
('sufficiency','b',(1196,643,1588,744),0,3000,'Cancelled K-like group and following word before K prime')]
log=[]
for name,half,box,rotation,width,place in specs:
 source=sources/f'J71-01_71_scan006_{half}.jpg'
 im=Image.open(source).convert('L').crop(box)
 im=ImageOps.autocontrast(im)
 if rotation:
  im=im.rotate(rotation, resample=Image.Resampling.BICUBIC,expand=True,fillcolor=255)
 before=im.size
 scale=width/im.width
 im=im.resize((width,round(im.height*scale)),Image.Resampling.LANCZOS)
 file=root/f'{name}.jpg'
 im.save(file,'JPEG',quality=97,subsampling=0)
 log.append({'file':str(file),'source':str(source),'box':list(box),'rotation':rotation,'output_width':width,'scale':scale,'pre_scale_size':list(before),'processing':'grayscale; autocontrast; '+('rotate BICUBIC; ' if rotation else '')+'resize LANCZOS; JPEG quality 97','place':place,'observed':None})
(root/'crops.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
print('Saved',len(log),'crops and exact processing log.')
