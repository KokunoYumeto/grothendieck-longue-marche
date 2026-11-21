"""Visible-ink geometry for scan 072; no OCR or TeX compilation."""
from pathlib import Path
from collections import defaultdict
from PIL import Image
from scipy import ndimage
import numpy as np
import json

ROOT=Path('/workspace/scratch/f28c4f52d3ec'); PAGE='148_scan072'
scan=np.asarray(Image.open(ROOT/'source/SP83_C13_148+149_scans'/f'{PAGE}.jpg').convert('RGB')).astype(np.int16)

def clean(mask,minimum):
    labels,count=ndimage.label(mask)
    sizes=np.bincount(labels.ravel())
    keep=sizes>=minimum; keep[0]=False
    final=keep[labels]
    return final,dict(components=count,kept_components=int(keep.sum()),removed_pixels=int(mask.sum()-final.sum()))

def outlines(mask,offset):
    up=np.zeros_like(mask); up[1:]=mask[:-1]
    down=np.zeros_like(mask); down[:-1]=mask[1:]
    left=np.zeros_like(mask); left[:,1:]=mask[:,:-1]
    right=np.zeros_like(mask); right[:,:-1]=mask[:,1:]
    edges=set()
    for direction,edge_mask in enumerate((mask&~up,mask&~right,mask&~down,mask&~left)):
        ys,xs=np.nonzero(edge_mask)
        for x,y in zip(xs.tolist(),ys.tolist()):
            if direction==0: a,b=(x,y),(x+1,y)
            elif direction==1: a,b=(x+1,y),(x+1,y+1)
            elif direction==2: a,b=(x+1,y+1),(x,y+1)
            else: a,b=(x,y+1),(x,y)
            edges.add((a,b))
    outgoing=defaultdict(set)
    for a,b in edges: outgoing[a].add(b)
    directions={(1,0):0,(0,1):1,(-1,0):2,(0,-1):3}
    paths=[]
    while edges:
        first=min(edges); start,current=first
        edges.remove(first); outgoing[start].remove(current)
        points=[start,current]; previous=start
        while current!=start:
            opts=[q for q in outgoing[current] if (current,q) in edges]
            assert opts
            old=directions[(current[0]-previous[0],current[1]-previous[1])]
            def priority(q):
                new=directions[(q[0]-current[0],q[1]-current[1])]
                return {1:0,0:1,3:2,2:3}[(new-old)%4]
            nxt=min(opts,key=priority)
            edges.remove((current,nxt)); outgoing[current].remove(nxt)
            previous,current=current,nxt; points.append(current)
        pts=points[:-1]; simple=[]
        for i,b in enumerate(pts):
            a=pts[i-1]; c=pts[(i+1)%len(pts)]
            if (b[0]-a[0])*(c[1]-b[1])!=(b[1]-a[1])*(c[0]-b[0]):
                simple.append([b[0]+offset[0],b[1]+offset[1]])
        assert len(simple)>=4
        paths.append(simple)
    return paths

def rasterize(paths,box):
    x0,y0,x1,y1=box
    crossings=[[] for _ in range(y1-y0)]
    for loop in paths:
        for a,b in zip(loop,loop[1:]+loop[:1]):
            if a[0]==b[0]:
                for y in range(min(a[1],b[1]),max(a[1],b[1])): crossings[y-y0].append(a[0]-x0)
            else: assert a[1]==b[1]
    mask=np.zeros((y1-y0,x1-x0),dtype=bool)
    for y,xx in enumerate(crossings):
        xx.sort(); assert len(xx)%2==0
        for a,b in zip(xx[::2],xx[1::2]): mask[y,a:b]=True
    return mask

def export(paths,colour):
    result=[rf'\path[fill={colour},draw=none,even odd rule]']
    for loop in paths:
        points=[f'({x},{y})' for x,y in loop]
        for i in range(0,len(points),12): result.append(('' if i==0 else '--')+'--'.join(points[i:i+12]))
        result[-1]+='--cycle'
    result[-1]+=';'
    return '\n'.join(result)+'\n'

layers=[]
for name,box,colour,minimum in [
    ('red',[335,202,1315,1220],'red!55!black',3),
    ('ray_tip',[207,207,245,242],'black',3),
    ('right_ray',[1974,861,2110,885],'black',3)]:
    x0,y0,x1,y1=box; pix=scan[y0:y1,x0:x1]
    r,g,b=pix[:,:,0],pix[:,:,1],pix[:,:,2]
    if name=='red':
        mask=(r-g>5)&(r-b>8)&(r<245)
        threshold='R-G>5, R-B>8, R<245; includes the visibly paler brown outer curves'
    else:
        mask=(pix.max(axis=2)<190)&(np.abs(r-g)<20)&(np.abs(g-b)<25)
        threshold='max RGB<190, abs(R-G)<20, abs(G-B)<25'
    mask,stats=clean(mask,minimum)
    if name=='right_ray':
        # The box also clips the separate top bar of the numeral 5 below it.
        # That numeral is transcribed as a node; retain only the ray component.
        labels,count=ndimage.label(mask)
        sizes=np.bincount(labels.ravel()); sizes[0]=0
        keep=labels==int(sizes.argmax())
        stats['excluded_off_target_numeral_pixels']=int(mask.sum()-keep.sum())
        stats['retained_target_components']=1
        mask=keep
    paths=outlines(mask,(x0,y0))
    rebuilt=rasterize(paths,box)
    assert np.array_equal(mask,rebuilt)
    tex=export(paths,colour)
    (ROOT/'proposed'/f'{PAGE}_{name}_geometry.tex').write_text(tex)
    layers.append(dict(name=name,box=box,colour=colour,threshold=threshold,
        component_minimum=minimum,stats=stats,filled_pixels=int(mask.sum()),paths=paths,
        vector_export_identical_pixels=True,geometry_file=f'{PAGE}_{name}_geometry.tex'))
data=dict(page=PAGE,method='Visible ink outlined as filled grid-boundary polygons after manual reading; no OCR.',
    simplification='Collinear corners only; no smoothing, closing, dilation or hole filling.',layers=layers)
(ROOT/'proposed'/f'{PAGE}_vector_geometry.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
print(json.dumps([dict(name=x['name'],paths=len(x['paths']),vertices=sum(map(len,x['paths'])),stats=x['stats'],pixels_identical=True) for x in layers]))
