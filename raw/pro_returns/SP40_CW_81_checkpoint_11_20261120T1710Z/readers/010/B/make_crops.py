from pathlib import Path
import json
import subprocess
ROOT = Path('/workspace/scratch/94548b74fbe0')
OUT = ROOT / 'out/readers/010/B'
SOURCE = ROOT / 'source/SP40_CW_81_scans/J81-01_81_scan010.jpg'
ITEMS = [
 ('c01_upper_middle_vertex.png', [1080,230,1221,274], 'Under upper disk 7: central hooked vertex and adjacent edge endpoints; C doubt 4.'),
 ('c02_lower_left_graph.png', [113,1005,334,1057], 'Lower left graph: separate decisions for the four endpoints; C doubt 1.'),
 ('c03_lower_middle_graph.png', [458,1004,664,1052], 'Lower middle graph: left endpoint white interior, middle gap, and isolated dot.'),
 ('c04_overdrawn_disk.png', [440,704,650,935], 'Lower disk 2: full repeated diagonal strokes and outline endpoints; C doubt 3.'),
 ('c05_middle_final_disk.png', [1267,310,1425,600], 'Final middle disk: upper detached/connected stroke, dark blob, and lower arches; part of C doubt 2.'),
 ('c06_lower_graph_and_left_angular.png', [967,966,1309,1105], 'Last graph together with the angular trace crossing it, preserving all trace endpoints; part of C doubt 2.'),
 ('c07_right_angular.png', [1310,875,1615,1105], 'Right angular trace and pale adjoining marks, preserving endpoints; part of C doubt 2.'),
 ('c08_upper_edge_marks.png', [1004,17,1057,44], 'Pair of detached dark marks at the upper paper edge; part of C doubt 5.'),
 ('c09_right_pale_marks.png', [1505,335,1600,416], 'Pale curved trace and higher pale slanted trace to the right of the middle row; part of C doubt 5.'),
 ('c10_right_flecks.png', [1538,560,1586,604], 'Two tiny detached dark flecks at right; part of C doubt 5.'),
 ('c11_pale_curve_below_top2.png', [391,237,438,291], 'Faint curved mark below and right of the graph under upper disk 2, absent from C.'),
 ('c12_pale_slant_between_lower_disks.png', [355,732,404,783], 'Faint short slanted trace between the first and second lower disks, absent from C.'),
 ('c13_pale_above_top4.png', [768,29,805,73], 'Faint descending trace above upper disk 4, absent from C.'),
]
records=[]
for name,bbox,purpose in ITEMS:
 subprocess.run(['python3',str(ROOT/'out/scripts/crop.py'),str(SOURCE),str(OUT/name),*map(str,bbox),'--rotate','0','--width','2800'],check=True)
 records.append({'path':name,'bbox':{'source':'full','coordinates':bbox},'rotation':0,'purpose':purpose})
(OUT/'crops.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(f'Created {len(records)} single-locus crops.')
