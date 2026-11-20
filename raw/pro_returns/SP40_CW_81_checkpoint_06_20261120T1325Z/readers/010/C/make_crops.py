from pathlib import Path
import json, subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'source/SP40_CW_81_scans/J81-01_81_scan010.jpg'
SPECS=[
 ('01_lower_left_graph.png',[119,1014,329,1059],'First lower graph: separately inspect both endpoints of first edge and retain neighbouring edge.'),
 ('02_top_seventh_graph.png',[1080,228,1221,273],'Middle vertex and both adjoining edge endpoints beneath upper seventh disk.'),
 ('03_overdrawn_disk.png',[438,703,654,935],'Whole lower second disk, complete hatching/cancellation ends and underlying strokes.'),
 ('04_middle_final_disk.png',[1270,314,1420,600],'Final middle disk, projecting upper stroke, detached dark blob and lower arches.'),
 ('05_left_angular_trace_and_graph.png',[971,960,1302,1105],'Left lower angular trace and crossed four-vertex graph, including all endpoint spots.'),
 ('06_right_angular_trace.png',[1330,885,1603,1080],'Right lower angular trace with both pale upper endpoints and complete heavy bend.'),
 ('07_upper_edge_traces.png',[1005,14,1057,43],'Paired detached bars near upper edge.'),
 ('08_right_middle_pale_marks.png',[1500,337,1604,418],'Pale curled trace and neighbouring upper faint mark in right middle open space.'),
 ('09_right_middle_flecks.png',[1545,566,1582,602],'Two tiny detached flecks at right middle.'),
 ('10_upper_left_pale_arc.png',[395,224,439,285],'Faint arc beneath the upper second disk and right of its two-dot graph.'),
 ('11_lower_left_pale_arc.png',[351,729,405,788],'Faint diagonal trace in gap above and right of lower first disk.'),
 ('12_lower_middle_graph.png',[461,1008,660,1055],'Lower middle three-vertex path and detached dot, including hollow-looking first vertex.'),
 ('13_right_margin_gray_patch.png',[1623,779,1655,816],'Detached pale irregular patch at right margin; inspect shape without supplying a character.')
]
records=[]
for name,bbox,purpose in SPECS:
 dest=HERE/name
 subprocess.run(['python3',str(ROOT/'out/scripts/crop.py'),str(SOURCE),str(dest),*[str(x) for x in bbox],'--rotate','0','--width','2800'],check=True)
 records.append({'path':name,'source':str(SOURCE.relative_to(ROOT)),'bbox':bbox,'coordinate_system':'original full scan; origin upper left','rotation':0,'width':2800,'purpose':purpose})
(HERE/'crop_records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
