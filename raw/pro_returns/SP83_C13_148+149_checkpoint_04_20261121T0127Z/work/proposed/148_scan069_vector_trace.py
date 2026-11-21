"""Geometry production for scan 069. Colour masks are not OCR.

The visible red ink is outlined as filled vector paths, preserving its pen gaps,
arrow marks and small circles. Labels and graph incidence are read manually.
No TeX engine is invoked. All coordinates are original scan pixels.
"""
from pathlib import Path
from collections import defaultdict
from PIL import Image
from scipy import ndimage
import numpy as np
import json

ROOT=Path('/workspace/scratch/f28c4f52d3ec'); PAGE='148_scan069'
im=np.asarray(Image.open(ROOT/'source/SP83_C13_148+149_scans/148_scan069.jpg').convert('RGB')).astype(np.int16)

def remove_small_components(mask, minimum=5):
    labels, count=ndimage.label(mask)
    sizes=np.bincount(labels.ravel())
    keep=sizes>=minimum; keep[0]=False
    return keep[labels], dict(components=count, kept_components=int(keep.sum()), removed_pixels=int(mask.sum()-keep[labels].sum()))

def outline_pixels(mask, offset=(0,0)):
    """Trace grid-cell boundaries with ink on the right of each directed edge."""
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
    loops=[]
    directions={(1,0):0,(0,1):1,(-1,0):2,(0,-1):3}
    while edges:
        first=min(edges)
        start,current=first
        edges.remove(first); outgoing[start].remove(current)
        points=[start,current]; previous=start
        while current!=start:
            opts=[q for q in outgoing[current] if (current,q) in edges]
            assert opts, (current,points[-5:])
            olddir=directions[(current[0]-previous[0],current[1]-previous[1])]
            def priority(q):
                newdir=directions[(q[0]-current[0],q[1]-current[1])]
                turn=(newdir-olddir)%4
                return {1:0,0:1,3:2,2:3}[turn]
            nxt=min(opts,key=priority)
            edges.remove((current,nxt)); outgoing[current].remove(nxt)
            previous,current=current,nxt; points.append(current)
        # Exact lossless removal of collinear intermediate corners only.
        p=points[:-1]
        simplified=[]
        for i,b in enumerate(p):
            a=p[i-1]; c=p[(i+1)%len(p)]
            if (b[0]-a[0])*(c[1]-b[1]) != (b[1]-a[1])*(c[0]-b[0]):
                simplified.append([b[0]+offset[0],b[1]+offset[1]])
        assert len(simplified)>=4
        loops.append(simplified)
    return loops

box=[430,275,1357,1057]
x0,y0,x1,y1=box
pix=im[y0:y1,x0:x1]
r,g,b=pix[:,:,0],pix[:,:,1],pix[:,:,2]
red=(r-g>18)&(r-b>12)&(r<220)
red,redstats=remove_small_components(red,5)
redloops=outline_pixels(red,(x0,y0))

# The six-turn black overdraw is confined to the crop already read by eye.
blackbox=[1249,438,1299,540]
x0,y0,x1,y1=blackbox
pix=im[y0:y1,x0:x1]
r,g,b=pix[:,:,0],pix[:,:,1],pix[:,:,2]
black=(pix.max(axis=2)<104)&(np.abs(r-g)<18)&(np.abs(g-b)<24)
black,blackstats=remove_small_components(black,4)
blackloops=outline_pixels(black,(x0,y0))

def tex_outlines(loops, colour):
    # Even-odd fill retains all holes; loops close stroke boundaries, not curves.
    lines=[rf'\path[fill={colour},draw=none,even odd rule]']
    for loop in loops:
        chunks=[]
        for p in loop: chunks.append(f'({p[0]},{p[1]})')
        for i in range(0,len(chunks),12):
            prefix='' if i==0 else '--'
            lines.append(prefix+'--'.join(chunks[i:i+12]))
        lines[-1]+='--cycle'
    lines[-1]+=';'
    return '\n'.join(lines)

redtex=tex_outlines(redloops,'red!55!black')
blacktex=tex_outlines(blackloops,'black')
(ROOT/'proposed'/f'{PAGE}_red_geometry.tex').write_text(redtex+'\n')
(ROOT/'proposed'/f'{PAGE}_black_geometry.tex').write_text(blacktex+'\n')
data=dict(page=PAGE, method='colour separation and exact grid-boundary vector outlines; no OCR',
    red_box=box,red_threshold='R-G>18, R-B>12, R<220; components under five pixels removed',
    red_stats=redstats,red_pixels=int(red.sum()),red_paths=redloops,
    black_box=blackbox,black_threshold='max RGB<104, abs(R-G)<18, abs(G-B)<24; components under four pixels removed',
    black_stats=blackstats,black_pixels=int(black.sum()),black_paths=blackloops,
    path_simplification='collinear corners only; no smoothing, dilation, closing or hole filling')
(ROOT/'proposed'/f'{PAGE}_vector_geometry.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n')
print(json.dumps(dict(red_loops=len(redloops),red_vertices=sum(map(len,redloops)),red_stats=redstats,
    black_loops=len(blackloops),black_vertices=sum(map(len,blackloops)),black_stats=blackstats)))
