from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage
import numpy as np
import json, math

ROOT=Path('/workspace/scratch/f28c4f52d3ec'); PAGE='148_scan069'
geometry=json.loads((ROOT/'proposed'/f'{PAGE}_vector_geometry.json').read_text())
vertices={
 'a':[878,350],'b':[996,337],'c':[1262,390],'d':[724,481],
 'e':[989,500],'f':[915,568],'g':[1019,553],'h':[1148,486],
 'i':[1072,626],'j':[1230,627],'k':[726,714],'l':[931,829],
 'm':[1135,757],'n':[1274,724],'o':[1227,837],'p':[1133,982]}
# Finite edges: graphite/grey and dark retraced strokes are distinguished.
edges=[]
def edge(a,b,colour='gray',width=.75,controls=None):
    edges.append(dict(a=a,b=b,colour=colour,width=width,controls=controls))
edge('f','a','black',.50)
edge('f','b','gray',.90)
edge('f','d','black',.50)
edge('f','e','gray',.72)
edge('f','g','gray',.90)
edge('f','i','black',.50)
edge('f','k','gray!65',.65)
edge('f','l','gray',.70,[[917,682],[916,756]])
edge('b','e','gray',.78)
edge('e','h','gray',.78)
edge('e','g','gray',.75)
edge('g','i','gray',.90)
edge('g','h','gray',.90)
edge('b','h','black',.48)
edge('c','h','gray',.95)
edge('h','i','black',.50)
edge('h','j','black',.50)
edge('i','j','black',.50)
edge('i','m','gray',.90)
edge('i','l','black',.50)
edge('j','m','gray',.90)
edge('j','n','black',.50)
edge('d','k','black',.50)
edge('k','l','gray',.62)
edge('l','m','gray',.95)
edge('l','p','black',.52)
edge('m','n','gray',.90)
edge('m','o','black',.52)
edge('m','p','black',.90,[[1129,835],[1128,917]])
edge('o','p','gray',.90)
edge('a','d','gray!65',.60,[[780,364],[754,414]])
edge('a','b','gray!65',.60)
edge('b','c','gray',.85,[[1083,307],[1190,354]])
edge('c','j','gray',.85,[[1308,492],[1291,543]])
edge('n','o','gray',.85,[[1264,765],[1249,802]])

rays=[
 dict(a='a',end=[835,135],colour='gray',width=.65),
 dict(a='b',end=[1138,87],colour='gray',width=1.00),
 dict(a='c',end=[1394,279],colour='gray',width=.95),
 dict(a='d',end=[431,393],colour='gray',width=.65),
 dict(a='j',end=[1458,607],colour='gray',width=.90),
 dict(a='k',end=[395,922],colour='gray',width=.90),
 dict(a='l',end=[780,1092],colour='gray',width=.90),
 dict(a='n',end=[1539,793],colour='gray',width=.90),
 dict(a='o',end=[1525,983],colour='gray',width=.90),
 dict(a='p',end=[1223,1238],colour='black',width=.45)]

labels=[
 dict(vertex='a',reading=r'\unsure{\infty}',plain='∞?',position=[859,349],rotation=90,mark='M0944'),
 dict(vertex='b',reading=r'\unsure{\infty}',plain='∞?',position=[989,335],rotation=58,mark='M0945'),
 dict(vertex='c',reading='1',plain='1',position=[1274,400],rotation=0),
 dict(vertex='d',reading=r'\unsure{\infty}',plain='∞?',position=[714,490],rotation=-25,mark='M0946'),
 dict(vertex='e',reading=r'\unsure{1}',plain='1?',position=[980,501],rotation=35,mark='M0947'),
 dict(vertex='f',reading='0',plain='0',position=[899,596],rotation=0),
 dict(vertex='g',reading=r'\infty',plain='∞',position=[1017,577],rotation=-10),
 dict(vertex='h',reading='0',plain='0',position=[1148,520],rotation=0),
 dict(vertex='i',reading='1',plain='1',position=[1047,636],rotation=0),
 dict(vertex='j',reading=r'\infty',plain='∞',position=[1194,647],rotation=12),
 dict(vertex='k',reading='1',plain='1',position=[728,735],rotation=0),
 dict(vertex='l',reading=r'\infty',plain='∞',position=[911,831],rotation=0),
 dict(vertex='m',reading='0',plain='0',position=[1117,777],rotation=8),
 dict(vertex='n',reading='1',plain='1',position=[1285,731],rotation=0),
 dict(vertex='o',reading=r'\infty',plain='∞',position=[1240,844],rotation=-8),
 dict(vertex='p',reading='1',plain='1',position=[1124,1001],rotation=0)]

def point(p): return f'({p[0]},{p[1]})'
lines=[r'\scanpage{69}',r'\figure{\begin{tikzpicture}[x=.008cm,y=-.008cm,line cap=round,line join=round]',
 '% Vertex identifiers are editorial coordinates only; they are not printed.']
for name,p in vertices.items(): lines.append(rf'\coordinate ({name}) at {point(p)};')
for e in edges:
    if e['controls']:
        path=f"({e['a']}) .. controls {point(e['controls'][0])} and {point(e['controls'][1])} .. ({e['b']})"
    else: path=f"({e['a']})--({e['b']})"
    lines.append(rf"\draw[{e['colour']},line width={e['width']:.2f}pt] {path};")
for r in rays:
    lines.append(rf"\draw[{r['colour']},line width={r['width']:.2f}pt] ({r['a']})--{point(r['end'])};")
lines.append('% Red curve and circle outlines preserve visible pen gaps and local arrow marks.')
lines.append((ROOT/'proposed'/f'{PAGE}_red_geometry.tex').read_text().rstrip())
lines.append('% The black six-turn overdraw is reproduced as a visible shape, not three invented shafts.')
lines.append((ROOT/'proposed'/f'{PAGE}_black_geometry.tex').read_text().rstrip())
for label in labels:
    lines.append(rf"\node[font=\fontsize{{5}}{{5}}\selectfont,inner sep=0pt,rotate={label['rotation']}] at {point(label['position'])} {{$"+label['reading']+r'$};')
lines += [r'\end{tikzpicture}}','% crop-candidate: scan 69',r'\mspage{68}']
text='\n'.join(lines)+'\n'
(ROOT/'proposed'/f'{PAGE}.tex').write_text(text)

# Reconstruct the filled vector paths at pixel centres to certify export fidelity.
def rasterize_grid_paths(paths,box):
    x0,y0,x1,y1=box
    crossings=[[] for _ in range(y1-y0)]
    for loop in paths:
        for a,b in zip(loop,loop[1:]+loop[:1]):
            if a[0]==b[0]:
                for y in range(min(a[1],b[1]),max(a[1],b[1])):
                    crossings[y-y0].append(a[0]-x0)
            else:
                assert a[1]==b[1]
    result=np.zeros((y1-y0,x1-x0),dtype=bool)
    for y,xx in enumerate(crossings):
        xx.sort(); assert len(xx)%2==0
        for a,b in zip(xx[::2],xx[1::2]): result[y,a:b]=True
    return result

red_mask=rasterize_grid_paths(geometry['red_paths'],geometry['red_box'])
black_mask=rasterize_grid_paths(geometry['black_paths'],geometry['black_box'])
assert int(red_mask.sum())==geometry['red_pixels']
assert int(black_mask.sum())==geometry['black_pixels']

# Preview is made from the vector-coordinate model, without invoking TeX.
viewbox=[380,75,1560,1250]; scale=2
canvas=Image.new('RGB',((viewbox[2]-viewbox[0])*scale,(viewbox[3]-viewbox[1])*scale),'white')
draw=ImageDraw.Draw(canvas)
def cp(p): return ((p[0]-viewbox[0])*scale,(p[1]-viewbox[1])*scale)
def bezier(a,c,d,b):
    pts=[]
    for t in np.linspace(0,1,100):
        pts.append([(1-t)**3*a[k]+3*(1-t)**2*t*c[k]+3*(1-t)*t*t*d[k]+t**3*b[k] for k in range(2)])
    return pts
def paint_edge(a,b,col,w,controls=None):
    rgb={'black':(15,15,15),'gray':(114,114,114),'gray!65':(159,159,159)}[col]
    pts=bezier(a,*controls,b) if controls else [a,b]
    draw.line([cp(p) for p in pts],fill=rgb,width=max(1,round(w*4.4*scale)),joint='curve')
for e in edges: paint_edge(vertices[e['a']],vertices[e['b']],e['colour'],e['width'],e['controls'])
for r in rays: paint_edge(vertices[r['a']],r['end'],r['colour'],r['width'])
for mask,box,colour in [(red_mask,geometry['red_box'],(140,0,0)),(black_mask,geometry['black_box'],(0,0,0))]:
    alpha=Image.fromarray((mask*255).astype('uint8')).resize((mask.shape[1]*scale,mask.shape[0]*scale),Image.Resampling.NEAREST)
    layer=Image.new('RGB',alpha.size,colour)
    canvas.paste(layer,(int((box[0]-viewbox[0])*scale),int((box[1]-viewbox[1])*scale)),alpha)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15*scale)
for label in labels:
    layer=Image.new('RGBA',(80*scale,60*scale),(255,255,255,0))
    ld=ImageDraw.Draw(layer)
    fill=(190,100,0,255) if 'mark' in label else (10,10,10,255)
    ld.text((40*scale,30*scale),label['plain'],font=font,anchor='mm',fill=fill)
    layer=layer.rotate(label['rotation'],resample=Image.Resampling.BICUBIC,expand=False)
    pos=cp(label['position']); canvas.paste(layer,(round(pos[0]-40*scale),round(pos[1]-30*scale)),layer)
preview=ROOT/'proposed'/f'{PAGE}_geometry_preview.png'; canvas.save(preview)

assert len(vertices)==16 and len(edges)==35 and len(rays)==10 and len(labels)==16
assert len({tuple(sorted((e['a'],e['b']))) for e in edges})==35
parts=dict(page=PAGE,vertices=vertices,edges=edges,rays=rays,labels=labels,
    boundary=['a','b','c','j','n','o','p','l','k','d'],
    red_geometry_file=f'{PAGE}_red_geometry.tex',black_geometry_file=f'{PAGE}_black_geometry.tex',
    red_vector_fill_pixels=int(red_mask.sum()),black_vector_fill_pixels=int(black_mask.sum()),
    vector_grid_export_area_matches=True,tex_compiled=False,preview=str(preview))
(ROOT/'proposed'/f'{PAGE}_parts.json').write_text(json.dumps(parts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(tex_bytes=len(text.encode()),vertices=16,finite_edges=35,rays=10,
    labels=16,red_paths=len(geometry['red_paths']),preview_bytes=preview.stat().st_size)))
