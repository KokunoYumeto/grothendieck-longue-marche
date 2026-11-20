"""Restore the original PNG bytes from reversible crop payloads in this archive.

Run after extracting the ZIP: python3 RESTORE_CROPS.py
The manifest records the Pillow/zlib versions used for the verified encoding.
No OCR, resampling, image enhancement, or transcription operation is performed.
"""
from pathlib import Path
import hashlib,io,json,sys
from PIL import Image

def main():
 root=Path(__file__).resolve().parent
 manifest=root/'CROP_STORAGE.json'
 if not manifest.exists():raise SystemExit('Extract the archive and run its top-level RESTORE_CROPS.py.')
 d=json.loads(manifest.read_text());count=0
 for row in d['encoded_crops']:
  target=root/row['original_path']
  if target.exists():
   if hashlib.sha256(target.read_bytes()).hexdigest()!=row['original_sha256']:
    raise SystemExit('Refusing to replace a different existing file: '+row['original_path'])
   continue
  data=(root/row['stored_path']).read_bytes()
  if hashlib.sha256(data).hexdigest()!=row['stored_sha256']:raise SystemExit('Encoded crop hash mismatch: '+row['stored_path'])
  im=Image.open(io.BytesIO(data));im.load();im=im.convert(row['mode'])
  output=io.BytesIO();im.save(output,format='PNG',**row['png_options']);original=output.getvalue()
  if hashlib.sha256(original).hexdigest()!=row['original_sha256']:
   raise SystemExit('PNG reconstruction differs. Use the codec versions recorded in CROP_STORAGE.json. Nothing was written for '+row['original_path'])
  target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(original);count+=1
 print(f'Restored {count} original PNG files; every restored byte sequence matched its recorded SHA-256.')

if __name__=='__main__':main()
