"""Geometry-only recovery of early 053 margin crop provenance.

Reads the existing source/crops; never writes or replaces evidence images.
The initial registration searches scale using normalized pixel correlation.
No OCR, textual reading, or witness comparison is involved.
"""
from pathlib import Path
import json, hashlib, math
import numpy as np
from PIL import Image
from scipy.signal import fftconvolve
from scipy.ndimage import uniform_filter, map_coordinates
from scipy.optimize import minimize

BASE = Path(__file__).resolve().parents[2]
SOURCE = BASE / 'source/SP83_C13_148+149_scans/148_scan053.jpg'

def ncc(image, template):
    temp = template.astype(np.float64)
    temp -= temp.mean()
    h,w = temp.shape
    raw = fftconvolve(image, temp[::-1,::-1], mode='valid')
    s = np.pad(image.cumsum(0).cumsum(1), ((1,0),(1,0)))
    sq = np.pad((image*image).cumsum(0).cumsum(1), ((1,0),(1,0)))
    sm = s[h:,w:] - s[:-h,w:] - s[h:,:-w] + s[:-h,:-w]
    sm2 = sq[h:,w:] - sq[:-h,w:] - sq[h:,:-w] + sq[:-h,:-w]
    denom = np.sqrt(np.maximum(sm2-sm*sm/(w*h),1e-6) * (temp*temp).sum())
    out = raw / denom
    iy,ix = np.unravel_index(out.argmax(),out.shape)
    return float(out[iy,ix]), int(ix), int(iy)

def approximate(name,angle):
    source = Image.open(SOURCE).convert('L')
    source_half = np.array(source.resize((source.width//2,source.height//2),Image.Resampling.LANCZOS),dtype=np.float64)
    image = Image.open(BASE/'result/crops'/name).convert('L')
    straight = image.rotate(angle,Image.Resampling.BICUBIC,expand=True,fillcolor=255)
    cx,cy=straight.width//2,straight.height//2
    patch=straight.crop((cx-180,cy-160,cx+180,cy+160))
    best=[]
    for scale in np.arange(2.0,5.01,.1):
        size=(round(patch.width/(scale*2)),round(patch.height/(scale*2)))
        templ=np.array(patch.resize(size,Image.Resampling.LANCZOS),dtype=np.float64)
        score,x,y=ncc(source_half,templ)
        best.append((score,float(scale),2*(x+size[0]/2),2*(y+size[1]/2)))
    best.sort(reverse=True)
    print(name,'coarse',best[:3],flush=True)
    score,scale,cx,cy=best[0]
    source_arr=np.array(source,dtype=np.float64)
    obs=np.array(image,dtype=np.float64)
    # Samples cover several different strokes while avoiding white outside fill.
    yy,xx=np.mgrid[500:image.height-500:14,500:image.width-500:14]
    good=obs[yy,xx] < 245
    xx=xx[good].astype(float); yy=yy[good].astype(float)
    values=obs[yy.astype(int),xx.astype(int)]
    values=(values-values.mean())/values.std()
    cosa,sina=math.cos(math.radians(angle)),math.sin(math.radians(angle))
    qx=xx-(image.width-1)/2; qy=yy-(image.height-1)/2
    ux=cosa*qx+sina*qy; uy=-sina*qx+cosa*qy
    def loss(params):
        sc,ox,oy=params
        z=map_coordinates(source_arr,[uy/sc+oy,ux/sc+ox],order=1,mode='constant',cval=255)
        z=(z-z.mean())/max(z.std(),1e-8)
        return float(np.mean((z-values)**2))
    opt=minimize(loss,[scale,cx,cy],method='Nelder-Mead',options={'maxiter':1500,'xatol':1e-7,'fatol':1e-10})
    print(name,'refined',opt.x.tolist(),'loss',opt.fun,'success',opt.success,flush=True)
    return {'name':name,'angle_clockwise':angle,'initial':best[:3], 'refined_scale_center':opt.x.tolist(),'normalized_loss':opt.fun}

if __name__=='__main__':
    rows=[approximate('148_scan053_margin3.png',52),approximate('148_scan053_margin4.png',54)]
    (BASE/'result/qa/early_margin_crop_registration.json').write_text(json.dumps(rows,indent=2)+'\n')
