#!/usr/bin/env python3
from pathlib import Path
import json,csv,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from catalogue_genus3_torus_mirrors import Group
from genus3_multiboundary_sections import MultiBoundaryOrbifold

def main():
 records=json.loads((HERE/'type_3_0_torus_mirrors_certificates.json').read_text())
 rows=[];details=[]
 for rec in records:
  G=Group([tuple(p) for p in rec['group_elements']]);assert G.el==[tuple(p) for p in rec['group_elements']]
  x=rec['interior_cone_generators'];es=rec['boundary_elements']
  if rec['kind']=='annulus':assert G.prod(x+es)==G.one
  else:
   d=rec['crosscap_generator'];assert G.prod(x+es+[d,d])==G.one
  cycles=list(zip(rec['reflection_cycles'],rec['corner_lists'],es))
  model=MultiBoundaryOrbifold(rec['class_id'],G,rec['orientation'],x,cycles,rec['generator_vector'])
  pattern=((0,)*len(model.cones),(0,)*len(model.corner_orders),(0,)*len(model.refs),0)
  row,data=model.analyse(pattern,rec['class_id'],0);row['type']='(3,0)'
  row['positive_action']='O3.'+str(rec['positive_action']);row['quotient']=rec['kind']
  data['type']='(3,0)';data['crosscap_generator']=rec['crosscap_generator'];data['quotient_kind']=rec['kind']
  rows.append(row);details.append(data)
  print(rec['class_id'],rec['kind'],'order',G.n,'sections',len(data['sections']),flush=True)
 with (HERE/'type_3_0_torus_mirrors_sections_catalogue.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (HERE/'type_3_0_torus_mirrors_sections.json').write_text(json.dumps(details,indent=2)+'\n')
 print('FINAL',len(rows),'complete section catalogues passed.',flush=True)
if __name__=='__main__':main()
