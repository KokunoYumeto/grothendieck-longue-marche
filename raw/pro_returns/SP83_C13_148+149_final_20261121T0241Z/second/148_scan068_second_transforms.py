from pathlib import Path
from PIL import Image,ImageChops
import json
ROOT=Path('/workspace/scratch/f28c4f52d3ec/result')
PAGE='148_scan068'
p=ROOT/'second'/f'{PAGE}_second_crop_manifest.json'
manifest=json.loads(p.read_text())
for e in manifest:
    f=Path(e['path'])
    n=int(e['box'][1:])
    if 7<=n<=16:
        backup=f.with_name(f.stem+'_unrotated.png')
        if not backup.exists():f.rename(backup)
        im=Image.open(backup).convert('RGB')
        rot=im.transpose(Image.Transpose.ROTATE_180)
        rot.save(f)
        assert ImageChops.difference(rot.transpose(Image.Transpose.ROTATE_180),im).getbbox() is None
        e['display_rotation_degrees']=180
        e['retained_unrotated_path']=str(backup)
        e['retained_unrotated_viewed']=False
    e['bytes']=f.stat().st_size
    e['needs_transport']=e['bytes']>6290000
    if e['needs_transport']:
        d=ROOT/'crops'/'transport'
        d.mkdir(exist_ok=True)
        transport=d/(f.stem+'.webp')
        im=Image.open(f).convert('RGB')
        im.save(transport,format='WEBP',lossless=True,method=4)
        assert ImageChops.difference(im,Image.open(transport).convert('RGB')).getbbox() is None
        e['transport_path']=str(transport)
        e['transport_pixels_identical']=True
p.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([(e['box'],e['bytes'],e.get('transport_path')) for e in manifest]))
