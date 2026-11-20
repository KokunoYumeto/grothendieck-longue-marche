#!/usr/bin/env python3
"""Verify crop-coordinate associations numerically, without displaying images.

Reconstruct the recorded crop.py transform in memory. Exact RGB equality is
required. No image files are generated and no OCR/text interpretation occurs.
The certificate records only successful coordinate/image associations.
"""
from pathlib import Path
import argparse,csv,hashlib,json
import numpy as np
from PIL import Image,ImageOps,ImageFilter

FIELDS=['crop_file','source_scan','x0','y0','x1','y1','rotation_degrees','status','output_width','output_height','matched_rgb_bytes','rgb_sha256','method','source_documentation']


def reconstruct(source,box,angle,width_limit=2800,height_limit=4000):
    im=source.crop(box)
    if angle:im=im.rotate(angle,expand=True,fillcolor='white',resample=Image.Resampling.BICUBIC)
    im=ImageOps.autocontrast(im)
    factor=min(width_limit/im.width,height_limit/im.height)
    return im.resize((round(im.width*factor),round(im.height*factor)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.4,percent=110,threshold=3))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work',type=Path,default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--views',type=Path);parser.add_argument('--source',type=Path)
    parser.add_argument('--only',nargs='*');parser.add_argument('--width-limit',type=int,default=2800);parser.add_argument('--height-limit',type=int,default=4000)
    args=parser.parse_args();work=args.work.resolve();views=args.views or work.parent/'views';source_dir=args.source or work.parent/'source/SP70_C13_142_scans'
    with (work/'CROPS.tsv').open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
    certificate=work/'CROP_PIXEL_RECOVERY.tsv';records={}
    if certificate.exists():
        with certificate.open(newline='') as f:records={r['crop_file']:r for r in csv.DictReader(f,delimiter='\t')}
    images={};issues=[];matched=[];skipped=[]
    for row in rows:
        name=row['crop_file'];scan=int(row['scan'])
        if args.only is not None and name not in args.only:continue
        if row['coordinate_status']=='unknown':skipped.append(name);continue
        box=tuple(int(row[k]) for k in ('x0','y0','x1','y1'));angle=float(row['rotation_degrees'] or '0')
        if scan not in images:images[scan]=Image.open(source_dir/f'142_scan{scan:03d}.jpg').convert('RGB')
        expected=np.asarray(reconstruct(images[scan],box,angle,args.width_limit,args.height_limit));actual=np.asarray(Image.open(views/name).convert('RGB'))
        if expected.shape!=actual.shape or not np.array_equal(expected,actual):
            issues.append({'crop_file':name,'attempted_box':box,'attempted_rotation':angle,'existing_dimensions':list(actual.shape[:2][::-1]),'reconstructed_dimensions':list(expected.shape[:2][::-1])})
            continue
        records[name]=dict(crop_file=name,source_scan=f'142_scan{scan:03d}.jpg',x0=box[0],y0=box[1],x1=box[2],y1=box[3],rotation_degrees=f'{angle:g}',status='exact_pixel_match',output_width=actual.shape[1],output_height=actual.shape[0],matched_rgb_bytes=int(actual.size),rgb_sha256=hashlib.sha256(actual.tobytes()).hexdigest(),method=f'exact reconstructed crop.py RGB equality; width_limit={args.width_limit}; height_limit={args.height_limit}',source_documentation=row['source_documentation'])
        matched.append(name)
    with certificate.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t');writer.writeheader();writer.writerows(records[k] for k in sorted(records))
    print(json.dumps({'exact_matches':len(matched),'skipped_unknown':skipped,'mismatches':issues},indent=2))
    return bool(issues)

if __name__=='__main__':raise SystemExit(main())
