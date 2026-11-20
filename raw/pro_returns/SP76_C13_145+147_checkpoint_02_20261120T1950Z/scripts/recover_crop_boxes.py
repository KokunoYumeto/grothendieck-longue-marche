"""Recover missing crop coordinates by numerical pixel registration only.

No OCR, character recognition, display, new reading crop, or transcription change.
Existing crop pixels are registered to the supplied original scan. Contrast and
resampling differences are handled by normalized image correlation.
"""
from pathlib import Path
from PIL import Image
import numpy as np
from scipy.signal import fftconvolve
import json

W=Path(__file__).resolve().parents[1]
S=W.parent/'source/SP76_C13_145+147_scans'

def ncc(im, tp):
    tp=tp-tp.mean()
    shape=tp.shape
    ones=np.ones(shape, dtype=np.float32)
    sums=fftconvolve(im,ones,mode='valid')
    sq=fftconvolve(im*im,ones,mode='valid')
    numerator=fftconvolve(im,tp[::-1,::-1],mode='valid')
    denominator=np.sqrt(np.maximum(sq-sums*sums/tp.size,1e-5)*np.sum(tp*tp))
    scores=numerator/denominator
    iy,ix=np.unravel_index(np.argmax(scores),scores.shape)
    return float(scores[iy,ix]),int(ix),int(iy)

def recover(name, hint=None):
    page=name[:11]
    src=Image.open(S/(page+'.jpg')).convert('L')
    target=Image.open(W/'crops'/name).convert('L')
    ratio=target.height/target.width
    small=np.asarray(src.resize((src.width//4,src.height//4),Image.Resampling.LANCZOS),dtype=np.float32)/255
    coarse=[]
    widths=range(160,min(src.width,1680),8) if hint is None else range(hint[2]-hint[0]-16,hint[2]-hint[0]+17,4)
    for width in widths:
        tw=max(8,round(width/4));th=max(3,round(width*ratio/4))
        tp=np.asarray(target.resize((tw,th),Image.Resampling.LANCZOS),dtype=np.float32)/255
        score,x,y=ncc(small,tp)
        coarse.append((score,width,x*4,y*4))
    score,bw,bx,by=max(coarse)
    candidates=[]
    # Native registration in a bounded neighborhood of the coarse alignment.
    left=max(0,bx-30);top=max(0,by-20)
    right=min(src.width,bx+bw+45);bottom=min(src.height,by+round(bw*ratio)+35)
    region=np.asarray(src,dtype=np.float32)[top:bottom,left:right]/255
    for width in range(max(10,bw-18),min(src.width,bw+19)):
        for height in {int(width*ratio),round(width*ratio),int(width*ratio)+1}:
            if width>region.shape[1] or height>region.shape[0]: continue
            tp=np.asarray(target.resize((width,height),Image.Resampling.LANCZOS),dtype=np.float32)/255
            sc,x,y=ncc(region,tp)
            candidates.append((sc,left+x,top+y,width,height))
    best=max(candidates)
    sc,x,y,width,height=best
    out={'crop':'crops/'+name,'box':[x,y,x+width,y+height],
         'normalized_pixel_correlation':sc,'coarse_best':[score,bw,bx,by],
         'method':'Numerical normalized cross-correlation of existing crop pixels against original scan; no text recognition or new reading.'}
    print(json.dumps(out),flush=True)
    return out

results=[recover('145_scan035_groupe_ens.png',[1192,1998,1551,2105]),
         recover('145_scan037_eq15.png'),recover('145_scan037_final_formula.png')]
(W/'reports/recovered_crop_boxes.json').write_text(json.dumps(results,indent=2)+'\n')
