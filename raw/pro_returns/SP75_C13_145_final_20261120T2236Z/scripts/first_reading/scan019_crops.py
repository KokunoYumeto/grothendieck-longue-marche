from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
source=root/'packets/145_scan019/page.jpg'
out=root/'edition'
boxes={
    'formula_eight':[340,30,835,300],
    'margin_covariance':[1030,70,1605,430],
    'square_verification':[290,415,1510,655],
    'nb_left_cancelled_ici':[215,670,1010,835],
    'nb_faudrait_revision':[1225,620,1655,745],
    'generators_prose':[215,855,1630,1030],
    'relation_block':[335,1040,1395,1300],
    'comme_produits':[345,1365,835,1455],
    'cancelled_product':[210,1420,550,1505],
    'product_derivation':[340,1560,1655,1735],
    'formula_nine':[305,1765,1030,1990],
    'eliminant_accent':[220,1970,550,2085],
    'definition_ending':[1030,2050,1655,2165],
    'manuscript_number_eighteen':[20,2265,115,2340],
}
im=Image.open(source).convert('RGB')
assert im.size==(1677,2360)
manifest=[]
for name,box in boxes.items():
    path=out/'crops'/('145_scan019_'+name+'.png')
    assert not path.exists(),path
    c=ImageOps.autocontrast(im.crop(box),cutoff=.5)
    c=c.resize((2800,round(c.height*2800/c.width)),Image.Resampling.LANCZOS)
    c=c.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
    c.save(path)
    manifest.append({'name':name,'crop':'crops/'+path.name,'box':box,'width':2800})
(out/'reader_reports/145_scan019_crop_boxes.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Saved '+str(len(manifest))+' crops and their original-coordinate manifest.')
