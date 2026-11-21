"""Losslessly re-encode one immutable checkpoint snapshot for a transfer retry.

Reads every deliverable from the original ZIP, not from mutable working files.
PNG images are replaced by pixel-identical lossless WebP; explicit image names
in textual records follow the encoding change. No image recognition is used.
"""
from pathlib import Path
from PIL import Image
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,sys,zipfile

source,target,cache=map(Path,sys.argv[1:4])
assert source.exists() and not target.exists()
text_ext={'.tex','.md','.tsv','.csv','.json','.py','.log','.txt'}
with zipfile.ZipFile(source) as z:
    payload={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
names=[n for n in payload if n.lower().endswith('.png')]
def encode(n):
    old=Image.open(BytesIO(payload[n]));rgba=old.convert('RGBA').tobytes()
    name=str(Path(n).with_suffix('.webp'));cached=cache/name
    if cached.exists():data=cached.read_bytes()
    else:
        buffer=BytesIO();old.save(buffer,format='WEBP',lossless=True,quality=100,method=6)
        data=buffer.getvalue();cached.parent.mkdir(parents=True,exist_ok=True);cached.write_bytes(data)
    new=Image.open(BytesIO(data))
    assert old.size==new.size and rgba==new.convert('RGBA').tobytes(),n
    return n,name,data,{'working_file':n,'archive_file':name,'width':old.width,'height':old.height,'rgba_sha256':hashlib.sha256(rgba).hexdigest(),'working_bytes':len(payload[n]),'archive_bytes':len(data),'pixels_identical':True}
with ThreadPoolExecutor(max_workers=4) as pool:encoded=list(pool.map(encode,names))
mapping={Path(n).name:Path(m).name for n,m,_,_ in encoded}
result={m:data for _,m,data,_ in encoded}
for name,data in payload.items():
    if name in names:continue
    if Path(name).suffix.lower() in text_ext:
        value=data.decode('utf-8')
        for old,new in mapping.items():value=value.replace(old,new)
        data=value.encode('utf-8')
    result[name]=data
result['evidence_encoding.json']=(json.dumps([r for _,_,_,r in encoded],ensure_ascii=False,indent=2)+'\n').encode()
result['EVIDENCE_ENCODING.md']=('# Evidence encoding for checkpoint transfer retry\n\nThis archive preserves the complete immutable contents of the original checkpoint02 snapshot. Its '+str(len(names))+' PNG evidence images are encoded as lossless WebP. Every decoded RGBA pixel and dimension was compared with the original snapshot and found identical. No crop was resized, enhanced, or recognized in this conversion. Explicit evidence filenames in text records have matching suffixes. The source archive and earlier checkpoint are unchanged. The additional packaging record identifies the retry.\n').encode()
result['checkpoint_retry.json']=(json.dumps({'original_archive':source.name,'original_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'original_entries':len(payload),'retry_reason':'Two prepare_uploads calls failed before returning an upload session or file id. The transfer is retried with lossless image encoding. The first live-tree staging attempt was rejected for inconsistent snapshot timing and was never uploaded.','pixel_comparisons_passed':len(encoded)},indent=2)+'\n').encode()
result['scripts/reencode_checkpoint.py']=Path(__file__).read_bytes()
target.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name in sorted(result):z.writestr(name,result[name])
with zipfile.ZipFile(target) as z:
    pages=[n for n in z.namelist() if n.startswith('pages/') and n.endswith('.tex')]
    reviews=[n for n in z.namelist() if n.startswith('reviews/') and n.endswith('.json') and json.loads(z.read(n)).get('approved')]
    assert len(pages)==len(reviews)==13,(len(pages),len(reviews))
print(json.dumps({'archive':str(target),'bytes':target.stat().st_size,'entries':len(result),'pages':len(pages),'images':len(names),'pixels_identical':True}),flush=True)
