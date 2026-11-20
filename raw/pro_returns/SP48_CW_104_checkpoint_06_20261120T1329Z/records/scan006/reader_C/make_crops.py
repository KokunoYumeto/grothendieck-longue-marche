from pathlib import Path
from PIL import Image, ImageOps
import json
p=Path(__file__).resolve().parent
source=Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans/H104-01_104_scan006.jpg')
im=Image.open(source)
records=[]
for name,box,angle,width,reason in json.loads((p/'crop_plan.json').read_text()):
    crop=im.crop(box)
    if angle:
        crop=crop.rotate(angle,expand=True)
    crop=ImageOps.autocontrast(crop,cutoff=0)
    size=(width,round(crop.height*width/crop.width))
    crop=crop.resize(size,Image.Resampling.LANCZOS)
    destination=p/'crops'/(name+'.png')
    destination.parent.mkdir(exist_ok=True)
    crop.save(destination)
    records.append({'file':str(destination),'source':str(source),'bbox':box,'rotation_degrees_counterclockwise':angle,'autocontrast_cutoff':0,'resample':'LANCZOS','output_dimensions':size,'sharpening':'none','reason':reason})
(p/'crop_processing_log.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
print('Created',len(records),'unique decision crops; none viewed by this script.')
