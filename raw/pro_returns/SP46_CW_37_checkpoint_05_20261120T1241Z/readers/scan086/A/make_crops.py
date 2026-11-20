from PIL import Image, ImageOps
from pathlib import Path
import json
root=Path('/workspace/scratch/006c0e32b2af/out/readers/scan086/A')
source=Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan086.jpg')
loci=[
 ('A086_01_section4_point.jpg',[1125,318,1285,378],'§4: small detached mark below/right of the period; punctuation or surface mark'),
 ('A086_02_de_underprint.jpg',[592,966,704,1020],'5.3: identity and state of the rounded underprint beneath live d'),
 ('A086_03_valuatifs_underprint.jpg',[612,1118,829,1171],'5.5: older character under live f'),
 ('A086_04_schematique_underprint.jpg',[553,1854,788,1912],'6.10: older character under live i'),
 ('A086_05_schema_punctuation.jpg',[977,1857,1098,1911],'6.10: comma or period after schéma'),
 ('A086_06_detached_pair.jpg',[1358,1478,1455,1548],'Blank area at right of 6.3: two small dark detached traces'),
 ('A086_07_vertical_trace.jpg',[749,385,867,492],'Between §4 and 4.1 leaders: fine vertical trace, possible paper or reproduction artifact'),
]
im=Image.open(source)
records=[]
for file,bbox,reason in loci:
    crop=im.crop(tuple(bbox)).convert('L')
    crop=ImageOps.autocontrast(crop,cutoff=0.3)
    newsize=(2600,round(crop.height*2600/crop.width))
    crop=crop.resize(newsize,Image.Resampling.LANCZOS)
    crop.save(root/file,quality=97,subsampling=0)
    records.append(dict(file=str(root/file),bbox=bbox,rotation=0,reason=reason,source=str(source),processing={'color':'grayscale','autocontrast_cutoff_percent':0.3,'resample':'LANCZOS','output_size':list(newsize),'sharpen':'none','jpeg_quality':97},visual_views=0))
(root/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'file':r['file'],'bbox':r['bbox'],'output_size':r['processing']['output_size']} for r in records],ensure_ascii=False,indent=2))
