from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
source=Image.open(root/'packets/145_scan014/page.jpg').convert('RGB')
boxes={
'ce_qui_redonne':[260,350,742,490],
'struck_par':[1490,350,1620,455],
'sigma_definition_end':[665,720,1030,825],
'retrouve_comme':[235,1275,1170,1410],
'cancelled_rho_chain':[310,1465,940,1670],
'inserted_relation':[695,1385,1010,1500],
'marginal_derivation':[1060,1365,1630,1680],
'cyclic_rho_display':[310,1675,850,1970],
'marginal_comment':[860,1675,1575,1950],
'final_abbreviation':[990,2250,1655,2350],
'manuscript_number_thirteen':[20,2250,110,2345]
}
for name,box in boxes.items():
 im=ImageOps.autocontrast(source.crop(box),cutoff=.5)
 w=2800
 im=im.resize((w,round(im.height*w/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 im.save(root/'edition/crops'/f'145_scan014_{name}.png')
(root/'edition/reader_reports/145_scan014_crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print('Saved eleven first-reading crops and their original-pixel boxes.')
