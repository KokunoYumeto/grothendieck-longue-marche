from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
from datetime import datetime, timezone
root=Path('out/readings/scan011/R1')
source=Path('/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan011.jpg')
im=Image.open(source)
loci=[
 ('01_heading',[580,44,1193,140],'Compressed group abbreviation and reinforced group-letter alphabet; also context for à droite.',0),
 ('02_cancelled_attempt',[288,143,901,254],'Canceled Aut expression, two low added labels, and argument T/D remain obscured by cancellation.',0),
 ('03_splitting',[620,414,1158,522],'English word and its ending in un splitting, against H section; detached high point included as context.',0),
 ('04_verb',[327,815,1013,891],'Compressed verb following On: C avait/aurait/écrit against H aura.',0),
 ('05_composition',[684,1070,1371,1211],'Possible composition circle before second parenthesis, exact underbrace placement and equality beneath.',0),
 ('06_cancelled_gamma',[520,1246,1267,1323],'First gamma in the first canceled verification line is obscured by overinking.',0),
 ('07_proof_subscript',[947,1365,1518,1448],'Final q subscript in live proof, t versus b, with other q occurrence on same line.',0),
 ('08_nb',[1348,1622,1667,1747],'Compressed si after NB and two-line parenthesis punctuation.',0),
 ('09_cancelled_relation',[478,1701,652,1771],'Crossed Gamma and following relation, subset versus membership.',0),
 ('10_dihedral',[1146,1890,1610,2046],'Diédral/diédhral, D alphabet, and crowded condition in the same marginal note.',0),
 ('11_final_correction',[1236,2094,1657,2193],'Canceled d’ordre n. and raised replacement words, exact deletion and insertion bounds.',0)
]
rows=[]
for name,box,reason,rotation in loci:
    crop=im.crop(box)
    scale=2400/crop.width
    crop=crop.resize((2400,round(crop.height*scale)),Image.Resampling.LANCZOS)
    crop=ImageOps.autocontrast(crop,cutoff=0.35)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.3,percent=125,threshold=3))
    if rotation:
        crop=crop.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    filename=name+'.png'
    crop.save(root/filename)
    rows.append({'id':name,'source':str(source),'bbox':box,'rotation_degrees':rotation,'file':'readings/scan011/R1/'+filename,'reason':reason,'enhancement':'LANCZOS resize to 2400 px width; autocontrast cutoff 0.35%; UnsharpMask radius 1.3, percent 125, threshold 3','output_dimensions':list(crop.size),'viewed':False})
manifest={'scan':'011','reader':'R1','start_utc':'2026-11-20T02:43:03Z','original_dimensions':[1685,2361],'image_viewing':{'whole':'once, layout','half_a':'once, full line-by-line reading','half_b':'once, full line-by-line reading','half_b_original_offset':[0,1100]},'crop_count':len(rows),'crops':rows}
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(rows),'unique locus crops.')
