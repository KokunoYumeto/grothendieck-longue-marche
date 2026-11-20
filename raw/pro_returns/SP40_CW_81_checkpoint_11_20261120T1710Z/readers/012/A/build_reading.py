from pathlib import Path
import re,json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/012/A'
s=(root/'packets/012/C.tex').read_text()
paths=re.findall(r'\\path\[fill=black,even odd rule\]\s*.*?;',s,re.S)
assert len(paths)==68
scale='x=0.0076cm,y=-0.0076cm,line join=round,line cap=round'
right={25,32,33,38,39,41,52,54,55,56,60,61,62,64,67}
overlaid={34,36,40,42,43,44,45,46,47,48,49,50,51}
right_min=(809.5,348.6)
overlaid_min=(156.5,564)
labels=re.findall(r'\\node\[inner sep=0pt.*?;',s)
assert len(labels)==8
parts=[r'\scanpage{12}', '% crop-candidate: scan 12', '% Original full-scan coordinates are retained throughout this drawing.',r'\figure{\begin{tikzpicture}['+scale+']']

def annotated(indices):
 return '\n'.join('%% C path %02d, visually inspected in its local drawing.\n%s'%(i,paths[i-1]) for i in sorted(indices))

def uncertain_picture(x,y,baseline,body,comment):
 return '\n'.join([comment, r'\node[inner sep=0pt,outer sep=0pt,anchor=north west] at ('+str(x)+','+str(y)+r') {\unsure{\begin{tikzpicture}['+scale+',baseline={(0,'+str(baseline)+')}]',body,r'\end{tikzpicture}}};'])

for i,p in enumerate(paths,1):
 if i==25:
  parts.append(uncertain_picture(*right_min,700,annotated(right), '% A012-04: live drawing / cancellation of the right group remains unresolved.\n% The question qualifies state; all observed paths and arrow terminals remain visible.'))
 elif i==34:
  parts.append(uncertain_picture(*overlaid_min,700,annotated(overlaid), '% C-D3 / A012-03: overlaid zigzags; cancellation of the large oval remains an alternative.\n% The connected lower miniature is retained; this state doubt concerns the large oval overlays.'))
 elif i not in right and i not in overlaid:
  parts.append('%% C path %02d, visually inspected in its local drawing.\n%s'%(i,p))
parts.extend(labels)
# Pale continuations seen in the complete right-group crop. Their graph roles are left unassigned.
parts.extend([
 '% A012-08: pale left-rim continuation; geometry medium confidence; hand provisionally his.',
 r'\draw[black!35,line width=0.23pt] (882.6,629.5) .. controls (880.5,638) and (878.3,647) .. (877.3,655.5);',
 '% A012-09a: pale low return after the detached dark lower-rim pieces; no extra connection supplied.',
 r'\draw[black!35,line width=0.23pt] (978.5,817.6) .. controls (985,819.5) and (990.8,817.5) .. (994,814);',
 '% A012-09b: pale sloping return below the lower right side of the tall oval.',
 r'\draw[black!25,line width=0.20pt] (997,810.5) .. controls (1005,805) and (1011,797.5) .. (1016,792);',
 '% A012-10: pale terminal extension at the upper long descending curve; not assigned an arrow meaning.',
 r'\draw[black!30,line width=0.24pt] (1609,912) .. controls (1614,915) and (1618,919) .. (1621,922);',
 r'\draw[black!20,line width=0.20pt] (1605.5,912) .. controls (1610,916) and (1615,920) .. (1619,923);',
 '% A012-11: thin oblique trace beside the right vertical; hand and attachment undetermined.',
 '% A012-11 is drawn below in its own qualified local graphic.'
])
# Each newly transcribed detached shape is separately marked, with an unassigned role/hand.
def tiny_graph(id,x,y,body,w=3,h=3):
 parts.append(uncertain_picture(x,y,h/2,body,'% '+id+': detached visible shape; hand, role and surface origin undetermined.'))
# Source-coordinate positions; the inner graphic uses local coordinates.
tiny_graph('A012-11',1387,903.5,r'\draw[black!25,line width=0.20pt] (0,0) -- (10,6.5);',10,6.5)
tiny_graph('A012-12',384,1288,
 r'\draw[black!20,line width=0.20pt] (18,0) .. controls (25,5) and (28,15) .. (27,23) .. controls (25,30) and (17,34) .. (4,36);'+ '\n'+
 r'\draw[black!15,line width=0.20pt] (2,38) .. controls (7,36) and (12,36) .. (16,36);'+ '\n'+
 r'\draw[black!12,line width=0.18pt] (22,31) -- (29,35);',31,38)
tiny_graph('A012-13a',215.5,446.5,r'\fill[black] (0.8,0) .. controls (2,0) and (2,3.2) .. (1.3,4.1) .. controls (0,4.2) and (0,1) .. cycle;',2,4.1)
tiny_graph('A012-13b',270.8,481.8,r'\fill[black!48] (0,0) -- (2.9,1.1) -- (1.3,3.4) -- (0.1,2.5) -- cycle;',2.9,3.4)
tiny_graph('A012-14',451.9,498.6,r'\draw[black!27,line width=0.20pt] (0.8,0) -- (1.0,3.2);'+ '\n'+r'\fill[black] (0,3.6) -- (1.6,2.9) -- (3,4.5) -- (1.1,6.2) -- (0,5.8) -- cycle;',3,6.2)
tiny_graph('A012-15',787.3,1427.6,r'\fill[black] (0.8,0) -- (2.1,0.2) -- (3.3,2.8) -- (2.7,4.4) -- (0.5,4.2) -- (0,2.7) -- cycle;',3.3,4.4)
tiny_graph('A012-16a',1527.9,1704.6,r'\fill[black] (0.7,0) -- (1.9,0.2) -- (2.4,1.4) -- (1.7,2.9) -- (0,2.2) -- cycle;',2.4,2.9)
tiny_graph('A012-16b',1522.8,1711.3,r'\fill[black] (0.2,0) -- (2.7,0.3) -- (2.5,1.5) -- (1.1,2.6) -- (0,1.8) -- cycle;',2.7,2.6)
tiny_graph('A012-17',1587.3,395.5,r'\fill[black!60] (1.2,0) ellipse[x radius=1.2,y radius=1.1];',2.4,2.2)
tiny_graph('A012-18',1642,531.2,r'\fill[black] (1.2,0) -- (2.4,2.6) -- (0,2.5) -- cycle;',2.4,2.6)
tiny_graph('A012-19',906,502.3,r'\fill[black!45] (1.0,0) ellipse[x radius=1.0,y radius=0.7];',2,1.4)
tiny_graph('A012-20',429.5,900.9,r'\fill[black!24] (1.2,0) ellipse[x radius=1.2,y radius=1.0];',2.4,2)
# Graphic points established on supplied halves; no inferred characters.
points=[
 ('A012-21a',591.0,44.5,0.7,1.2,55),
 ('A012-21b',609.0,46.5,0.7,0.8,50),
 ('A012-21c',1659.4,55.3,0.6,0.9,70),
 ('A012-21d',780.0,396.0,1.1,1.1,20),
 ('A012-23a',657.0,1634.0,0.65,0.85,60),
 ('A012-23b',1077.5,1465.0,0.6,0.8,40),
 ('A012-23c',1454.5,1660.5,0.7,1.2,35),
 ('A012-23d',185.3,1796.0,0.65,0.65,45),
 ('A012-23e',1359.0,1932.0,1.0,1.2,32),
 ('A012-23f',487.3,2051.0,0.7,0.7,50),
 ('A012-23g',1418.0,2289.0,0.65,0.65,70),
 ('A012-23h',1658.0,2190.0,0.8,0.6,65),
 ('A012-23i',686.5,2333.5,0.6,1.2,45),
]
for id,x,y,rx,ry,tone in points:
 tiny_graph(id,x-rx,y-ry,r'\fill[black!'+str(tone)+'] ('+str(rx)+','+str(ry)+') ellipse[x radius='+str(rx)+',y radius='+str(ry)+'];',2*rx,2*ry)
tiny_graph('A012-22',1657,792.5,r'\draw[black,line width=0.40pt] (0,1.4) -- (13.5,0);',13.5,1.4)
parts.extend([r'\end{tikzpicture}}','% archive sheet number: 11',''])
(out/'reading.tex').write_text('\n'.join(parts))
(out/'new_half_points.json').write_text(json.dumps(points,indent=2)+'\n')
print('Wrote complete reading.tex, retaining all',len(paths),'source paths and',len(labels),'text labels.')
