from pathlib import Path
from PIL import Image
import ast,hashlib,io,json,zipfile
base=Path(__file__).resolve().parent;root=base.parents[1];source=root/'work/checkpoint07_source';cache=root/'work/jxl_best_evidence_cache';oldcache=root/'work/jxl_evidence_cache'
old=json.loads((root/'work/checkpoint06_jxl/stage/evidence_encoding.json').read_text());known={r['source_file']:r['rgba_sha256'] for r in old}
known.update({r['file']:r['rgba_sha256'] for r in json.loads((base/'new_crops_encoding.json').read_text())})
records=[];image_sizes={};baseline=0;gain=0
for p in source.rglob('*'):
 if p.suffix not in {'.png','.webp'}:continue
 rel=str(p.relative_to(source));h=known[rel];best=cache/(h+'.jxl');default=oldcache/(h+'.jxl');im=Image.open(p)
 size=best.stat().st_size;assert size<p.stat().st_size
 target=str(Path(rel).with_suffix('.jxl'));image_sizes[target]=size;baseline+=default.stat().st_size;gain+=default.stat().st_size-size
 records.append(dict(source_file=rel,archive_file=target,width=im.width,height=im.height,rgba_sha256=h,source_bytes=p.stat().st_size,archive_bytes=size,pixels_identical=True))
records.sort(key=lambda r:r['source_file']);mapping={Path(r['source_file']).name:Path(r['archive_file']).name for r in records}
texttypes={'.tex','.md','.tsv','.csv','.json','.py','.log','.txt'};files={};protected=[]
for p in source.rglob('*'):
 if not p.is_file() or p.suffix in {'.png','.webp'}:continue
 rel=str(p.relative_to(source));data=p.read_bytes()
 if p.suffix=='.jpg':image_sizes[rel]=len(data);continue
 preserve=p.suffix=='.tex' or p.name.endswith(('_first.tsv','_second.tsv','_comparison.tsv','_token_differences.tsv'))
 if preserve:protected.append(dict(file=rel,sha256=hashlib.sha256(data).hexdigest()))
 if p.suffix in texttypes and not preserve:
  text=data.decode()
  for a,b in mapping.items():text=text.replace(a,b)
  data=text.encode()
 files[rel]=data
accepted=[]
for r in records:
 m=base/'cache_tuned'/(r['rgba_sha256']+'.json');c=m.with_suffix('.jxl')
 if m.exists() and c.exists() and c.stat().st_size==r['archive_bytes']:
  d=json.loads(m.read_text());r['lossless_tuning']=d['tune'];accepted.append(dict(source_file=r['source_file'],archive_file=r['archive_file'],rgba_sha256=r['rgba_sha256'],pixels_identical=True,options=d['tune']))
files['evidence_encoding.json']=(json.dumps(records,indent=2)+'\n').encode();files['lossless_tuning_manifest.json']=(json.dumps(accepted,indent=2)+'\n').encode();files['checkpoint_protected_hashes.json']=(json.dumps(protected,indent=2)+'\n').encode()
script=(base/'reencode_snapshot_jxl_best.py').read_text();tree=ast.parse(script)
for node in ast.walk(tree):
 if isinstance(node,ast.For) and isinstance(node.target,ast.Name) and node.target.id=='name' and isinstance(node.iter,ast.List):
  for n in ast.literal_eval(node.iter):
   p=base/n
   if p.exists():files['scripts/compression/'+n]=p.read_bytes()
files['scripts/reencode_snapshot_jxl_best.py']=script.encode()
files['lossless_optimization.json']=(root/'work/checkpoint06_optimized/stage/lossless_optimization.json').read_bytes()
# This documentation estimate deliberately allows more than its actual length.
files['EVIDENCE_ENCODING.md']=(root/'work/checkpoint06_optimized/stage/EVIDENCE_ENCODING.md').read_bytes()+b'\nAdditional current cache documentation.\n'
b=io.BytesIO()
with zipfile.ZipFile(b,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for rel,data in sorted(files.items()):z.writestr(rel,data)
size=len(b.getvalue())+sum(size+76+2*len(name.encode()) for name,size in image_sizes.items())
r={'estimated_archive_bytes':size,'current_image_savings':gain,'text_zip_bytes':len(b.getvalue()),'images':len(image_sizes),'nonimage_files':len(files),'estimated_total_gain_needed':size+gain-536870912,'allowance_for_minor_documentation_differences':100000}
(base/'checkpoint07_size_estimate.json').write_text(json.dumps(r,indent=2)+'\n');print(r)
