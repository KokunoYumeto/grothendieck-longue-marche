"""Restore crop pixels from a portable archive without rereading or recropping."""
from pathlib import Path
from PIL import Image
import csv,hashlib
W=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((W/'CROP_ENCODING.tsv').open(),delimiter='\t'))
mapping={}
for r in rows:
    p=W/r['stored'];im=Image.open(p).convert(r['mode'])
    assert im.size==(int(r['width']),int(r['height']))
    assert hashlib.sha256(im.tobytes()).hexdigest()==r['pixel_sha256']
    target=W/r['original']
    if not target.exists():im.save(target,format='PNG')
    test=Image.open(target).convert(r['mode'])
    assert hashlib.sha256(test.tobytes()).hexdigest()==r['pixel_sha256']
    mapping[Path(r['stored']).name]=Path(r['original']).name
frozen={'first_reading_hashes.tsv','TRANSCRIPTION_SHA256.tsv','CROP_ENCODING.tsv','CROP_ENCODING.md'}
for p in W.rglob('*'):
    if not p.is_file() or p.name in frozen or p.suffix not in {'.json','.md','.tsv','.csv','.log','.txt','.py','.tex'}:continue
    if p.parent.name=='pages' or p.name.endswith('_transcription.tex') or p.name.endswith('_first.tsv') or p.name.endswith('_boxes.tsv'):continue
    old=p.read_text();new=old
    for a,b in mapping.items():new=new.replace(a,b)
    if old!=new:p.write_text(new)
print(f'Restored and verified {len(rows)} original crop pixel arrays; no readings changed.')
