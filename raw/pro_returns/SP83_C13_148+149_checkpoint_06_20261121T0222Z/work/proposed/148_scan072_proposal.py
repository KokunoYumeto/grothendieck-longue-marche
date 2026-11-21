from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,math,re as regex
import numpy as np

ROOT=Path('/workspace/scratch/f28c4f52d3ec'); PAGE='148_scan072'; OUT=ROOT/'proposed'
geometry=json.loads((OUT/f'{PAGE}_vector_geometry.json').read_text())
left_vertices=dict(a=[585,470],b=[1073,263],c=[913,480],d=[765,588],e=[574,812],
    f=[817,823],g=[1018,776],h=[1282,663],i=[708,991],j=[939,957],k=[1222,977])
left_edges=[]
def le(a,b,colour='gray',width=.60,controls=None): left_edges.append(dict(a=a,b=b,colour=colour,width=width,controls=controls))
le('a','b','gray',.65)
le('a','c','gray!70',.48)
le('a','d','black!85',.48)
le('a','e','gray!65',.28,[[560,570],[571,730]])
le('b','c','gray',.62)
le('b','h','gray',.60,[[1152,369],[1252,532]])
le('c','d','black!75',.55)
le('c','f','gray',.72,[[880,593],[836,722]])
le('c','g','black!75',.58)
le('c','h','gray',.52,[[1033,526],[1153,604]])
le('d','e','gray',.45)
le('d','f','black!75',.48)
le('e','f','gray!75',.40,[[655,815],[741,815]])
le('e','i','black!85',.47)
le('f','g','black!75',.58)
le('f','i','gray',.62)
le('f','j','black!90',.42)
le('g','h','black!75',.63)
le('g','j','gray',.78)
le('g','k','gray',.53)
le('h','k','gray',.73,[[1269,774],[1235,897]])
le('i','j','gray',.45)
le('j','k','gray',.43)
left_retrace=dict(a='c',b='f',colour='gray!55',width=.34,controls=[[876,602],[802,740]])
left_rays=[
 dict(a='a',end=[214,216],colour='black!90',width=.45,controls=[[443,452],[324,310]]),
 dict(a='b',end=[1230,86],colour='gray',width=.52,controls=[[1136,194],[1181,124]]),
 dict(a='e',end=[220,914],colour='gray',width=.60,controls=None),
 dict(a='i',end=[573,1284],colour='gray',width=.70,controls=[[669,1103],[619,1207]]),
 dict(a='j',end=[943,1343],colour='gray',width=.55,controls=[[941,1099],[938,1244]]),
 dict(a='k',end=[1447,1172],colour='black!85',width=.42,controls=None),
 dict(a='h',end=[1713,605],colour='gray',width=.58,controls=[[1429,633],[1572,599]])]
left_marks={
 'a':[6,5],'b':[8,9],'c':[8,7],'d':[5,6],'e':[6,5],'f':[6,8],
 'g':[8,7],'h':[7,8],'i':[8,6],'j':[5,5],'k':[5,6]}
# Specific continuous brown stretches read in the source crops. The colour mask
# alone loses desaturated pixels here. These do not close arbitrary components.
red_supplements=[
 dict(name='outer left crossing of the ray from e',width=.18,
      points=[[370,850],[370,860],[371,870],[371,880],[372,891]]),
 dict(name='seventh contour, inner left flank',width=.17,
      points=[[863,501],[855,520],[848,540],[842,560],[836,580],[828,600],[819,620],
              [810,640],[800,660],[792,680],[782,700],[773,720],[764,740],[756,760],
              [747,780],[742,800],[737,820],[732,840],[730,860]]),
 dict(name='eighth contour, left flank',width=.17,
      points=[[881,500],[875,520],[868,540],[860,560],[852,580],[844,600],[836,620],
              [830,640],[822,660],[814,680],[806,700],[800,720],[794,740],[788,760],
              [784,780],[779,800],[774,820],[774,840],[777,860]]),
 dict(name='eighth contour, right flank',width=.17,
      points=[[945,500],[936,520],[923,540],[915,560],[908,580],[902,600],[897,620],
              [892,640],[887,660],[882,680],[875,700],[869,720],[864,740],[859,760],
              [853,780],[848,800],[841,820],[834,840],[824,860]])]
right_vertices=dict(a=[1558,821],b=[1750,726],c=[1960,749],d=[1981,878],
    e=[1889,982],f=[1617,968],g=[1579,1037],h=[1979,1064])
right_edges=[]
def re(a,b,width=.47,controls=None): right_edges.append(dict(a=a,b=b,colour='black!80',width=width,controls=controls))
re('a','b',.53)
re('b','c',.55,[[1821,734],[1891,744]])
re('c','d',.50,[[1961,791],[1973,836]])
re('d','e',.43)
re('e','f',.27,[[1790,977],[1698,977]])
re('f','a',.35)
re('f','g',.49)
re('e','h',.48)
right_loop=dict(a='h',b='h',colour='black!75',width=.39,
    segments=[[[2040,1030],[2087,1013],[2120,1040]],[[2177,1083],[2082,1120],[1979,1064]]])
right_rays=[
 dict(a='a',end=[1485,809],colour='black!80',width=.45,controls=None),
 dict(a='b',end=[1738,655],colour='black!80',width=.50,controls=None),
 dict(a='c',end=[2017,650],colour='black!80',width=.55,controls=[[1990,709],[2012,673]]),
 dict(a='d',end=[2106,873],colour='black',width=.52,controls=None),
 dict(a='g',end=[1508,1089],colour='black!80',width=.38,controls=[[1548,1059],[1526,1073]]),
 dict(a='g',end=[1595,1115],colour='black!80',width=.43,controls=None)]
right_marks=dict(a=[8,5],b=[5,5],c=[5,5],d=[9,5],e=[7,5],f=[8,6],g=[6,5],h=[7,7])
labels=[]
def label(vertex,value,position,size=4.8,bold=False,circled=False):
    labels.append(dict(vertex=vertex,reading=str(value),position=position,size=size,bold=bold,circled=circled))
label('a',3,[1530,801]); label('a',6,[1570,796]); label('a',15,[1590,850],5.9,True)
label('b',9,[1730,693]); label('b',1,[1730,765],6.3,True); label('b',9,[1781,760],6.3,True)
label('c',3,[1931,772]); label('c',3,[1991,742]); label('c',7,[1980,789],5.1)
label('d',2,[1965,855]); label('d',1,[1970,906],5.7,True); label('d',5,[2017,893])
label('e',4,[1868,973],5.3,True); label('e',2,[1905,946],4.6,False,True); label('e',3,[1930,991],4.6,False,True)
label('f',1,[1615,930],4.5,False,True); label('f',5,[1661,959]); label('f',4,[1610,999])
label('g',4,[1546,1040]); label('g',2,[1603,1070])
label('h',17,[1950,1062],5.5); label('h',3,[2005,1040]); label('h',3,[2000,1095])
caption=r"découpage \unsure{pantalonnesque|pantalonesque}"
caption_second="d'une carte (triangulée)"

def point(p): return f'({p[0]},{p[1]})'
def edge_tex(edge,prefix):
    start=f"({prefix}{edge['a']})"
    end=point(edge['end']) if 'end' in edge else f"({prefix}{edge['b']})"
    if edge.get('controls'):
        path=start+' .. controls '+point(edge['controls'][0])+' and '+point(edge['controls'][1])+' .. '+end
    else: path=start+'--'+end
    return rf"\draw[{edge['colour']},line width={edge['width']:.2f}pt] {path};"
left_tex=['% Left graph: coordinate identifiers are editorial and are not printed.']
for name,p in left_vertices.items(): left_tex.append(rf'\coordinate (l{name}) at {point(p)};')
for edge in left_edges: left_tex.append(edge_tex(edge,'l'))
left_tex.append('% Separate visible pencil retracing of c--f; no additional incidence is asserted.')
left_tex.append(edge_tex(left_retrace,'l'))
for ray in left_rays: left_tex.append(edge_tex(ray,'l'))
for name,(rx,ry) in left_marks.items(): left_tex.append(rf'\fill[black!70] (l{name}) ellipse ({rx} and {ry});')
left_graph_tex='\n'.join(left_tex)
supplement_tex=[]
for item in red_supplements:
    supplement_tex.append(rf"\draw[red!55!black,line width={item['width']:.2f}pt] "+'--'.join(point(p) for p in item['points'])+';')
left_tex.append('% Specific source-visible continuous brown stretches supplement the colour outline.')
left_tex+=supplement_tex
left_tex.append((OUT/f'{PAGE}_red_geometry.tex').read_text().rstrip())
left_tex.append((OUT/f'{PAGE}_ray_tip_geometry.tex').read_text().rstrip())
left_tex.append(r'\node[font=\fontsize{4.8}{5}\selectfont,inner sep=0pt] at (925,601) {$\unsure{1}$};')
left_complete='\n'.join(left_tex)

right_tex=['% Right weighted graph: labels retain their individual positions.']
for name,p in right_vertices.items(): right_tex.append(rf'\coordinate (r{name}) at {point(p)};')
for edge in right_edges: right_tex.append(edge_tex(edge,'r'))
lp='(rh)'
for c1,c2,end in right_loop['segments']: lp+=' .. controls '+point(c1)+' and '+point(c2)+' .. '+point(end)
right_tex.append(rf"\draw[black!75,line width=.39pt] {lp};")
for ray in right_rays: right_tex.append(edge_tex(ray,'r'))
for name,(rx,ry) in right_marks.items(): right_tex.append(rf'\fill[black!85] (r{name}) ellipse ({rx} and {ry});')
right_tex.append((OUT/f'{PAGE}_right_ray_geometry.tex').read_text().rstrip())
enclosures=[
 r'\draw[black!65,line width=.23pt] (1604,949) .. controls (1590,942) and (1594,918) .. (1611,913) .. controls (1627,910) and (1635,933) .. (1625,942) .. controls (1618,949) and (1611,950) .. (1604,949);',
 r'\draw[black!65,line width=.23pt] (1913,961) .. controls (1882,961) and (1889,930) .. (1904,932) .. controls (1917,932) and (1929,954) .. (1913,961);',
 r'\draw[black!65,line width=.23pt] (1936,978) .. controls (1928,969) and (1912,981) .. (1914,995) .. controls (1917,1010) and (1938,1007) .. (1942,994) .. controls (1944,986) and (1940,983) .. (1938,982);']
right_tex+=enclosures
for item in labels:
    reading=rf"\boldsymbol{{{item['reading']}}}" if item['bold'] else item['reading']
    right_tex.append(rf"\node[font=\fontsize{{{item['size']}}}{{6}}\selectfont,inner sep=0pt] at {point(item['position'])} {{$"+reading+'$};')
right_complete='\n'.join(right_tex)
caption_tex=rf'\node[anchor=north west,align=left,font=\fontsize{{6}}{{8}}\selectfont,inner sep=0pt] at (1617,132) {{{caption}\\\hspace{{.30cm}}{caption_second}}};'
tex='\n'.join([r'\scanpage{72}',r'\figure{\begin{tikzpicture}[x=.0058cm,y=-.0058cm,line cap=round,line join=round]',
    caption_tex,left_complete,right_complete,r'\end{tikzpicture}}','% crop-candidate: scan 72',r'\mspage{71}'])+'\n'
(OUT/f'{PAGE}.tex').write_text(tex)

# Independent geometry preview, generated without invoking TeX.
viewbox=[190,75,2310,1360]
canvas=Image.new('RGB',(viewbox[2]-viewbox[0],viewbox[3]-viewbox[1]),'white')
draw=ImageDraw.Draw(canvas)
def cp(p): return (p[0]-viewbox[0],p[1]-viewbox[1])
def colour(value):
    if value=='gray': return (115,115,115)
    if value.startswith('gray!'): n=int(value.split('!')[1]); a=round(255*(1-n/100)+128*n/100); return (a,a,a)
    if value.startswith('black!'): a=round(255*(1-int(value.split('!')[1])/100)); return (a,a,a)
    return (5,5,5)
def bezier(a,c1,c2,b):
    return [[(1-t)**3*a[k]+3*(1-t)**2*t*c1[k]+3*(1-t)*t*t*c2[k]+t**3*b[k] for k in range(2)] for t in np.linspace(0,1,80)]
def paint(edge,vertices):
    a=vertices[edge['a']]; b=edge.get('end',vertices.get(edge.get('b')))
    points=bezier(a,*edge['controls'],b) if edge.get('controls') else [a,b]
    draw.line([cp(p) for p in points],fill=colour(edge['colour']),width=max(1,round(edge['width']/.1644)),joint='curve')
for edge in left_edges+[left_retrace]+left_rays: paint(edge,left_vertices)
for edge in right_edges+right_rays: paint(edge,right_vertices)
start=right_vertices['h']
for c1,c2,end in right_loop['segments']:
    draw.line([cp(p) for p in bezier(start,c1,c2,end)],fill=(55,55,55),width=2,joint='curve'); start=end
for vertices,marks in [(left_vertices,left_marks),(right_vertices,right_marks)]:
    for name,(rx,ry) in marks.items():
        x,y=cp(vertices[name]); draw.ellipse((x-rx,y-ry,x+rx,y+ry),fill=(45,45,45))
for item in red_supplements:
    draw.line([cp(p) for p in item['points']],fill=(140,0,0),width=max(1,round(item['width']/.1644)),joint='curve')
def rasterize(paths,box):
    x0,y0,x1,y1=box; crossings=[[] for _ in range(y1-y0)]
    for loop in paths:
        for a,b in zip(loop,loop[1:]+loop[:1]):
            if a[0]==b[0]:
                for y in range(min(a[1],b[1]),max(a[1],b[1])): crossings[y-y0].append(a[0]-x0)
    mask=np.zeros((y1-y0,x1-x0),dtype=bool)
    for y,xx in enumerate(crossings):
        xx.sort(); assert len(xx)%2==0
        for a,b in zip(xx[::2],xx[1::2]): mask[y,a:b]=True
    return mask
for layer in geometry['layers']:
    mask=rasterize(layer['paths'],layer['box']); assert int(mask.sum())==layer['filled_pixels']
    alpha=Image.fromarray((mask*255).astype('uint8'))
    rgb=(140,0,0) if layer['name']=='red' else (0,0,0)
    canvas.paste(Image.new('RGB',alpha.size,rgb),cp(layer['box'][:2]),alpha)
fontpath='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
boldpath='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
for enclosure in enclosures:
    coords=[[float(x),float(y)] for x,y in regex.findall(r'\(([\d.]+),([\d.]+)\)',enclosure)]
    start=coords[0]
    for n in range(1,len(coords),3):
        c1,c2,end=coords[n:n+3]
        draw.line([cp(p) for p in bezier(start,c1,c2,end)],fill=(110,110,110),width=1,joint='curve')
        start=end
for label in labels:
    font=ImageFont.truetype(boldpath if label['bold'] else fontpath,round(label['size']*4.3))
    draw.text(cp(label['position']),label['reading'],font=font,anchor='mm',fill=(25,25,25))
draw.text(cp([925,601]),'1?',font=ImageFont.truetype(fontpath,21),anchor='mm',fill=(190,100,0))
caption_font=ImageFont.truetype(fontpath,25)
draw.text(cp([1617,132]),'découpage ',font=caption_font,fill=(25,25,25))
caption_start=[1617+caption_font.getlength('découpage '),132]
draw.text(cp(caption_start),'pantalonnesque|pantalonesque?',font=caption_font,fill=(190,100,0))
draw.text(cp([1669,205]),caption_second,font=caption_font,fill=(25,25,25))
preview=OUT/f'{PAGE}_geometry_preview.png'; canvas.save(preview)
parts=dict(page=PAGE,left_vertices=left_vertices,left_edges=left_edges,left_retrace=left_retrace,
    left_rays=left_rays,left_marks=left_marks,left_graph_tex=left_graph_tex,left_complete_tex=left_complete,
    red_supplements=red_supplements,red_supplement_tex='\n'.join(supplement_tex),
    right_vertices=right_vertices,right_edges=right_edges,right_loop=right_loop,right_rays=right_rays,
    right_marks=right_marks,right_labels=labels,right_enclosures=enclosures,right_complete_tex=right_complete,
    caption=caption,caption_second=caption_second,caption_tex=caption_tex,
    doubtful_left_mark=r'\unsure{1}',preview=str(preview),tex_compiled=False)
(OUT/f'{PAGE}_parts.json').write_text(json.dumps(parts,ensure_ascii=False,indent=2)+'\n')
assert len(left_edges)==23 and len(left_rays)==7 and len(labels)==23
print(json.dumps(dict(tex_bytes=len(tex.encode()),left_joins=23,left_rays=7,right_vertices=8,
    right_finite_edges=len(right_edges)+1,right_rays=6,right_labels=23,preview_bytes=preview.stat().st_size)))
