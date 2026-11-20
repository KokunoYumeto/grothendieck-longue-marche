"""Index supplied witness C TikZ paths by their literal coordinate bounds; no image processing."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1]
s=(R.parent/'packets/012/C.tex').read_text()
starts=list(re.finditer(r'\\path\[fill=black,even odd rule\]',s));rows=[]
for i,m in enumerate(starts):
 end=s.index(';',m.end())+1;piece=s[m.start():end]
 points=[tuple(map(float,p)) for p in re.findall(r'\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)',piece)]
 row={'path_index':i+1,'line_start':s.count('\n',0,m.start())+1,'line_end':s.count('\n',0,end)+1,'bounds_C_coordinates':[min(x for x,y in points),min(y for x,y in points),max(x for x,y in points),max(y for x,y in points)],'vertices':len(points),'note':'Literal source coordinates; no image-based classification.'};rows.append(row)
(R/'checks/scan012_C_path_map.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Indexed',len(rows),'literal source paths; no source modified.')
for r in rows:
 if r['vertices']>50:print(r['path_index'],r['line_start'],r['line_end'],r['bounds_C_coordinates'],r['vertices'])
