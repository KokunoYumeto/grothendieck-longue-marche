#!/usr/bin/env python3
"""Verify lossless PDF-based encoding of QA PNGs through a checkpoint.

Usage: python code/encode_qa_pngs.py NN
Historical PDFs come only from the corresponding immutable saved checkpoint.
"""
from pathlib import Path
import argparse,hashlib,json,re,zipfile
import fitz
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('checkpoint',type=int)
args=parser.parse_args()
saved_paths=json.loads((ROOT/'notes/checkpoint_saved_paths.json').read_text())
pdfdir=ROOT/'qa/source_pdfs';pdfdir.mkdir(exist_ok=True)
images={};fallback=[];original_bytes=0;pdf_bytes=0
for serial in range(6,args.checkpoint+1):
 directory=ROOT/f'qa/checkpoint{serial:02d}'
 if serial==args.checkpoint:
  pdf_path=ROOT/'LM8_PUSH_paper.pdf'
 else:
  selected=saved_paths.get(f'{serial:02d}')
  source=Path(selected['path']) if selected else ROOT.parent/f'LM8_PUSH_checkpoint_{serial:02d}.zip'
  with zipfile.ZipFile(source) as z:data=z.read('LM8_PUSH_paper.pdf')
  pdf_path=pdfdir/f'checkpoint{serial:02d}_paper.pdf'
  if pdf_path.exists():assert pdf_path.read_bytes()==data
  else:pdf_path.write_bytes(data)
  pdf_bytes+=len(data)
 pdf_hash=hashlib.sha256(pdf_path.read_bytes()).hexdigest()
 with fitz.open(pdf_path) as doc:
  for png in sorted(directory.glob('page_*.png')):
   page=int(re.search(r'page_(\d+)',png.name)[1]);original=png.read_bytes()
   generated=doc[page-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25)).tobytes('png')
   rel=png.relative_to(ROOT).as_posix()
   if generated!=original:
    fallback.append(rel);continue
   images[rel]={'pdf_path':pdf_path.relative_to(ROOT).as_posix(),'pdf_sha256':pdf_hash,
                'page':page,'scale':1.25,'bytes':len(original),
                'sha256':hashlib.sha256(original).hexdigest()}
   original_bytes+=len(original)
# Preserve any superseded rendering exactly against its retained original PDF.
# This is separate from the final-review directories and does not count as QA.
superseded_path=ROOT/'qa/superseded_renderings.json'
if superseded_path.exists():
 for rendering in json.loads(superseded_path.read_text())['superseded_renderings']:
  directory=ROOT/rendering['directory'];pdf_path=ROOT/rendering['pdf_path']
  assert pdf_path.is_file() and directory.is_dir()
  pdf_hash=hashlib.sha256(pdf_path.read_bytes()).hexdigest()
  assert pdf_hash==rendering['pdf_sha256']
  pdf_bytes+=pdf_path.stat().st_size
  with fitz.open(pdf_path) as doc:
   for png in sorted(directory.glob('page_*.png')):
    page=int(re.search(r'page_(\d+)',png.name)[1]);original=png.read_bytes()
    generated=doc[page-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25)).tobytes('png')
    rel=png.relative_to(ROOT).as_posix()
    assert rel not in images
    if generated!=original:
     fallback.append(rel);continue
    images[rel]={'pdf_path':pdf_path.relative_to(ROOT).as_posix(),'pdf_sha256':pdf_hash,
                'page':page,'scale':1.25,'bytes':len(original),
                'sha256':hashlib.sha256(original).hexdigest()}
    original_bytes+=len(original)
manifest={'codec':'PNG_FROM_PDF01','pymupdf_version':fitz.VersionBind,'images':images,
          'exact_byte_comparison_for_every_image':True,'unmatched_pngs_retained_verbatim':fallback}
path=ROOT/'qa/reconstruction_manifest.json';path.write_text(json.dumps(manifest,indent=2)+'\n')
stored_hash=hashlib.sha256(path.read_bytes()).hexdigest()
transforms=[]
for rel,row in images.items():
 transforms.append({'original_path':rel,'original_sha256':row['sha256'],'original_bytes':row['bytes'],
                    'decoded_sha256':row['sha256'],'decoded_bytes':row['bytes'],
                    'kind':'raw_bytes','codec':'PNG_FROM_PDF01','stored_path':'qa/reconstruction_manifest.json',
                    'stored_sha256':stored_hash,'local_encoded_file':str(path),
                    'entire_decoded_byte_hash_verified':True,
                    'restore_command':['{python}','{archive}/code/restore_qa_png.py',
                                       '{archive}/qa/reconstruction_manifest.json',rel,'{target}']})
out={'status':'PASS','transforms':transforms,'encoded_images':len(images),'original_png_bytes':original_bytes,
     'required_old_pdf_bytes':pdf_bytes,'approximate_net_saved_bytes':original_bytes-pdf_bytes,
     'unmatched_pngs_retained_verbatim':fallback,
     'scope':'Every included PNG was regenerated and compared byte-for-byte. The exact source PDFs are included; no visual work record is discarded.'}
(ROOT/f'notes/checkpoint{args.checkpoint:02d}_qa_encoding.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='transforms'},indent=2))
