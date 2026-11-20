from PIL import Image, ImageOps, ImageFilter, ImageChops
from pathlib import Path
import json
root=Path('/workspace/scratch/811dda00717a/work/readers/scan039/R2')
source=Path('/workspace/scratch/811dda00717a/source/SP41_CW_81_scans/J81-05_81_scan039.jpg')
im=Image.open(source).convert('RGB')
plans=[
('01_rhs_annotation',[1245,75,1595,375],0,'First Pi case; cancelled mark after i.e.; underbrace attachment and lower annotation'),
('02_upper_margin',[25,195,540,620],-29,'Complete four-line upper slanted margin'),
('03_map',[480,565,1055,765],0,'Arrow letter, capital P form, target suffix'),
('04_quelles',[1150,765,1575,915],0,'Pour qu’elles: final hook'),
('05_panache',[225,1235,735,1350],0,'non panaché: word, ending and punctuation'),
('06_defined_term',[900,1365,1530,1510],0,'maquette and overwritten beginning of ordonnée'),
('07_decompositions',[245,1515,1020,1655],0,'Parenthesis: décompositions and n-aires'),
('08_fini',[1320,1445,1640,1585],0,'Deleted ordonné and inserted fini'),
('09_sigma_insertion',[1155,1575,1335,1705],0,'Sigma after involution and its placement'),
('10_property',[245,1825,885,1985],0,'Singular or plural endings of propriété suivante'),
('11_numbering',[290,1870,580,2295],0,'Cancelled a/b/et labels and live 28 label'),
('12_cancelled_trials',[465,1885,1645,2110],0,'Three cancelled draft lines and their formulas'),
('13_lower_margin',[25,1990,390,2355],-43,'Complete lower slanted NB note'),
('14_live_clauses',[480,2050,1670,2290],0,'Live a,b clauses, deletion, insertion and line attachment'),
('15_final_nb',[265,2250,1692,2360],0,'Final NB rewritten verb, abbreviation and source-edge ending')]
manifest=[]
for stem,bbox,angle,reason in plans:
    assert 0<=bbox[0]<bbox[2]<=im.width and 0<=bbox[1]<bbox[3]<=im.height
    tile=im.crop(bbox)
    trim=None
    if angle:
        tile=tile.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
        ink=tile.convert('L').point(lambda p:255 if p<125 else 0)
        bb=ink.getbbox()
        if bb:
            trim=[max(0,bb[0]-16),max(0,bb[1]-16),min(tile.width,bb[2]+16),min(tile.height,bb[3]+16)]
            tile=tile.crop(trim)
    tile=ImageOps.autocontrast(tile)
    tile=tile.resize((3000,round(tile.height*3000/tile.width)),Image.Resampling.LANCZOS)
    tile=tile.filter(ImageFilter.UnsharpMask(radius=1.5,percent=130,threshold=3))
    path=root/'crops'/(stem+'.png')
    tile.save(path)
    manifest.append({'path':str(path),'source':str(source),'bbox':bbox,'angle_degrees':angle,'rotated_trim':trim,'size':list(tile.size),'reason':reason,'viewed':False})
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
a=Image.open('/workspace/scratch/811dda00717a/source/SP41_CW_81_scans/J81-05_81_scan039_a.jpg').convert('RGB')
b=Image.open('/workspace/scratch/811dda00717a/source/SP41_CW_81_scans/J81-05_81_scan039_b.jpg').convert('RGB')
print(json.dumps({'original_dimensions':list(im.size),'half_a_dimensions':list(a.size),'half_b_dimensions':list(b.size),'half_b_assumed_y_origin':1100,'crops_created':len(manifest),'manifest':str(root/'crop_manifest.json')},indent=2))
