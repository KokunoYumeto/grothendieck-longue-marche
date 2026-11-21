"""Restore the exact original PNG bytes from the packaged lossless crops."""
from pathlib import Path
from PIL import Image
import hashlib,io,json
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'crop_storage_manifest.json').read_text())
restored=0
for row in manifest['crops']:
 source=root/row['stored_path'];target=root/row['original_path']
 webp=source.read_bytes();assert hashlib.sha256(webp).hexdigest()==row['stored_sha256'],source
 im=Image.open(io.BytesIO(webp));im.load()
 assert im.mode==row['mode'] and list(im.size)==[row['width'],row['height']],source
 assert hashlib.sha256(im.tobytes()).hexdigest()==row['pixel_sha256'],source
 out=io.BytesIO();im.save(out,format='PNG');png=out.getvalue()
 assert hashlib.sha256(png).hexdigest()==row['original_sha256'],target
 if target.exists():assert target.read_bytes()==png,target
 else:target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(png);restored+=1
print(json.dumps({'verified':len(manifest['crops']),'restored':restored}))
