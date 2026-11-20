#!/usr/bin/env python3
"""Recover a crop rectangle by numerical pixel matching; no OCR or image viewing.

The exact crop.py transform is reconstructed in memory. A result is accepted
only if every decoded RGB output pixel equals the existing crop file. No image
is written. This script does not decide or transcribe manuscript content.
"""
from pathlib import Path
import argparse, hashlib, json
import numpy as np
from PIL import Image, ImageOps, ImageFilter
from scipy.signal import fftconvolve


def integral(a):
    return np.pad(a.astype(np.float64).cumsum(0).cumsum(1), ((1,0),(1,0)))


def sums(a,h,w):
    return a[h:,w:] - a[:-h,w:] - a[h:,:-w] + a[:-h,:-w]


def match(source, crop, width, height, scale):
    sw,sh=source.size
    s=np.asarray(source.resize((round(sw*scale),round(sh*scale)),Image.Resampling.LANCZOS).convert('L'),dtype=np.float32)
    tw,th=round(width*scale),round(height*scale)
    t=np.asarray(crop.resize((tw,th),Image.Resampling.LANCZOS).convert('L'),dtype=np.float32)
    t-=t.mean()
    energy=(t*t).sum()
    if not energy:return -1,0,0
    total=sums(integral(s),th,tw); total2=sums(integral(s*s),th,tw)
    denom=np.sqrt(np.maximum(total2-total*total/(tw*th),0)*energy)
    numerator=fftconvolve(s,t[::-1,::-1],mode='valid')
    scores=np.divide(numerator,denom,out=np.full(numerator.shape,-1.,dtype=np.float64),where=denom>1e-8)
    y,x=np.unravel_index(scores.argmax(),scores.shape)
    return float(scores[y,x]),int(x),int(y)


def exact_crop(source, box):
    im=ImageOps.autocontrast(source.crop(box))
    factor=min(2800/im.width,4000/im.height)
    return im.resize((round(im.width*factor),round(im.height*factor)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.4,percent=110,threshold=3))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path);parser.add_argument('crop',type=Path)
    parser.add_argument('--box',type=int,nargs=4,help='Verify a recovered rectangle without repeating search')
    args=parser.parse_args()
    source=Image.open(args.source).convert('RGB');crop=Image.open(args.crop).convert('RGB')
    reference=np.asarray(crop)
    if args.box:
        boxes=[tuple(args.box)]
    else:
        target_w,target_h=crop.size
        candidates=[]
        for w in range(50,source.width+1):
            h=round(w*target_h/target_w)
            if h<10 or h>source.height or round(2800*h/w)!=target_h:continue
            candidates.append((w,h))
        # Quarter-resolution search; shortlisted candidates get full-resolution correlation.
        coarse=[]
        for w,h in candidates:
            score,x,y=match(source,crop,w,h,.25)
            coarse.append((score,w,h,x,y))
        coarse.sort(reverse=True)
        print(json.dumps({'coarse_candidates':len(coarse),'best':coarse[:8]}),flush=True)
        full=[]
        for _,w,h,_,_ in coarse[:16]:
            score,x,y=match(source,crop,w,h,1.)
            full.append((score,x,y,x+w,y+h))
        full.sort(reverse=True)
        print(json.dumps({'full_best':full[:8]}),flush=True)
        boxes=[tuple(v[1:]) for v in full]
    for box in boxes:
        candidate=exact_crop(source,box)
        actual=np.asarray(candidate)
        if actual.shape==reference.shape and np.array_equal(actual,reference):
            print(json.dumps({'status':'exact_pixel_match','source':args.source.name,'crop':args.crop.name,
                              'box':box,'rotation_degrees':0,'output_size':crop.size,
                              'matched_rgb_bytes':int(reference.size),'rgb_sha256':hashlib.sha256(reference.tobytes()).hexdigest()}))
            return 0
    print(json.dumps({'status':'no_exact_match','tested_boxes':boxes}))
    return 1

if __name__=='__main__':raise SystemExit(main())
