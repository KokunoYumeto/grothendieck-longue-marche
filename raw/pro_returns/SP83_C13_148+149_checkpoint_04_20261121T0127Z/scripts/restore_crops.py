from pathlib import Path
from PIL import Image
import subprocess,hashlib,io,json,sys
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'CROP_COMPRESSION_MANIFEST.json').read_text())
selected=sys.argv[1:]
for r in m['crops']:
 if r['encoding']!='JPEG XL lossless':continue
 if selected and not any(s in r['original_path'] for s in selected):continue
 out=root/r['original_path']
 if out.exists():
  assert hashlib.sha256(out.read_bytes()).hexdigest()==r['original_sha256'],out
  continue
 src=root/r['archived_path'];assert hashlib.sha256(src.read_bytes()).hexdigest()==r['archived_sha256']
 raw=subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',str(src),'-f','rawvideo','-pix_fmt',r['pixel_format'],'pipe:1'],check=True,capture_output=True).stdout
 assert hashlib.sha256(raw).hexdigest()==r['pixel_sha256'],src
 im=Image.frombytes(r['mode'],tuple(r['size']),raw);b=io.BytesIO();im.save(b,format='PNG',**r['png_save_parameters'])
 assert hashlib.sha256(b.getvalue()).hexdigest()==r['original_sha256'],out
 out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(b.getvalue())
 print(out.relative_to(root))
print('All selected PNGs restored and verified byte for byte.')
