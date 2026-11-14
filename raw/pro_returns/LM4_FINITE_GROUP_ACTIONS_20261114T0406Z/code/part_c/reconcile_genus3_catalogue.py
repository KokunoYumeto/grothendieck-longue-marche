#!/usr/bin/env python3
"""Assemble the proved disjoint genus-three catalogue and identify every
B34 hyperelliptic overlap by an explicit monodromy isomorphism.
"""
from pathlib import Path
from collections import Counter
import json,csv,sys
HERE=Path(__file__).resolve().parent;WORK=HERE.parent
if not (WORK/'root'/'catalogue_higher_genus.py').exists():WORK=HERE.parents[1]
sys.path.insert(0,str(HERE));sys.path.insert(0,str(WORK/'root'))
from catalogue_genus3_reflection_quotients import Group,ordered
from catalogue_higher_genus import decoration_orbits

def csvrows(p):return list(csv.DictReader(p.open()))

def main():
 root=WORK/'root';b=WORK/'part_b'
 if (b/'code').is_dir():b=b/'code'
 positive_all=json.loads((root/'higher_genus_output/oriented_higher_genus_sections.json').read_text())
 positive=[r for r in positive_all if r['summary']['genus']==3 and r['summary']['punctures']==0]
 assert len(positive)==55
 lookup={}
 ds=json.loads((root/'research_data/actions-genus3.json').read_text())['actions']
 for ai,act in enumerate(ds,1):
  if act['gamma']!=0:continue
  G=Group([tuple(x-1 for x in p) for p in act['topreps'][0]])
  vs=[G.ids_of(v) for v in act['autgreps']]
  for oi,orb in enumerate(decoration_orbits(G,act,0,True),1):
   cid=f'G3N0-O{ai}-{oi}'
   for vi,removed,regular in orb:
    key=(tuple(act['bd']),G.tuple_key(vs[vi]));assert key not in lookup
    lookup[key]=cid
 hyp=json.loads((HERE/'type_3_0_hyperelliptic_sections.json').read_text())
 oldrows={r['class_id']:r for r in csvrows(HERE/'type_3_0_hyperelliptic_catalogue.csv')}
 posrows={r['summary']['id']:r['summary'] for r in positive}
 positive_overlap=[]
 for rec in hyp:
  if any(q['orientation']<0 for q in rec['group_elements']):continue
  els={q['id']:tuple(q['permutation']) for q in rec['group_elements']}
  cs=[els[j] for j in rec['cone_generators']]
  G=Group(cs);v=tuple(G.ids[q] for q in cs)
  ms=tuple(G.orders[q] for q in v);target=tuple(sorted(ms))
  v=ordered(G,v,ms,target);cid=lookup[target,G.tuple_key(v)]
  old=oldrows[rec['class_id']];new=posrows[cid]
  fields={'order':'order','full_splitting_classes':'full_sections',
   'nontrivial_partial_splitting_classes':'nontrivial_partial_sections',
   'maximal_partial_classes_Phi':'phi_points','Gamma_orbits_on_Phi':'phi_orbits'}
  assert all(int(old[k])==int(new[v]) for k,v in fields.items())
  positive_overlap.append({'hyperelliptic_class':rec['class_id'],'positive_class':cid})
 assert len(positive_overlap)==18 and len({r['positive_class'] for r in positive_overlap})==18
 rmap=json.loads((HERE/'genus3_hyperelliptic_reflection_crosscheck.json').read_text())['mapping']
 pmap=json.loads((HERE/'genus3_hyperelliptic_projective_crosscheck.json').read_text())['mapping']
 assert len(rmap)==57 and len(pmap)==4
 allhyp=[r['hyperelliptic_class'] for r in positive_overlap+rmap+pmap]
 assert len(allhyp)==79 and len(set(allhyp))==79
 records=[];rows=[]
 for p in positive:
  s=p['summary'];row={'class_id':s['id'],'type':'(3,0)','orientation':'positive','source_result':'B.33',
   'positive_source':s['source_pair'],'quotient_kind':'orientable genus '+str(s['quotient_genus']),
   'order':s['order'],'positive_order':s['order'],'full_splitting_classes':s['full_sections'],
   'nontrivial_partial_splitting_classes':s['nontrivial_partial_sections'],
   'maximal_partial_classes_Phi':s['phi_points'],'Gamma_orbits_on_Phi':s['phi_orbits'],
   'oval_section_classes':0,'line_section_classes':0}
  rows.append(row);records.append({'summary':row,'model':p})
 sources=[('B.37',HERE/'type_3_0_reflection_quotient_sections_catalogue.csv',HERE/'type_3_0_reflection_quotient_sections.json','disc'),
  ('B.39',HERE/'type_3_0_projective_quotient_catalogue.csv',HERE/'type_3_0_projective_quotient_sections.json','projective plane'),
  ('B.40',HERE/'type_3_0_torus_mirrors_sections_catalogue.csv',HERE/'type_3_0_torus_mirrors_sections.json',None),
  ('B.38',b/'type_3_0_free_positive_and_anti_catalogue.csv',b/'type_3_0_free_positive_and_anti_sections.json',None),
  ('B.41',b/'type_3_0_klein_quotient_catalogue.csv',b/'type_3_0_klein_quotient_sections.json','Klein bottle')]
 counts={}
 for result,table,detail,kind in sources:
  ss=csvrows(table);dd=json.loads(detail.read_text())
  if isinstance(dd,dict):dd=dd['catalogue']
  dd={r['class_id']:r for r in dd};counts[result]=len(ss)
  for s in ss:
   q=kind or s.get('quotient') or ('orientable' if s['quotient_orientable']=='True' else 'nonorientable')+' quotient, genus/crosscaps '+s['quotient_genus_or_crosscaps']+', boundaries '+s['mirror_boundary_components']
   row={'class_id':s['class_id'],'type':'(3,0)','orientation':'mixed','source_result':result,
    'positive_source':s.get('positive_action',s.get('positive_source','')),'quotient_kind':q}
   for key in ('order','positive_order','full_splitting_classes','nontrivial_partial_splitting_classes',
    'maximal_partial_classes_Phi','Gamma_orbits_on_Phi','oval_section_classes','line_section_classes'):
    row[key]=int(s[key])
   assert row['order']==2*row['positive_order']
   rows.append(row);records.append({'summary':row,'model':dd[s['class_id']]})
 assert counts=={'B.37':145,'B.39':11,'B.40':57,'B.38':18,'B.41':6}
 assert len(rows)==292 and len({r['class_id'] for r in rows})==292
 assert sum(r['orientation']=='mixed' for r in rows)==237
 assert all(r['line_section_classes']==0 for r in rows)
 with (HERE/'type_3_0_complete_catalogue.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (HERE/'type_3_0_complete_sections.json').write_text(json.dumps({'surface_type':'(3,0)',
  'classes':292,'positive_classes':55,'mixed_classes':237,
  'source_classification':counts,'catalogue':records},indent=2)+'\n')
 check={'classes':292,'positive_classes':55,'mixed_classes':237,'disjoint_mixed_sources':counts,
  'hyperelliptic_positive_overlap':positive_overlap,'hyperelliptic_mirror_overlap':rmap,
  'hyperelliptic_projective_overlap':pmap,'hyperelliptic_overlaps_total':79,
  'by_order':dict(sorted(Counter(r['order'] for r in rows).items())),
  'mixed_by_order':dict(sorted(Counter(r['order'] for r in rows if r['orientation']=='mixed').items()))}
 (HERE/'reconcile_genus3_catalogue_output.json').write_text(json.dumps(check,indent=2)+'\n')
 print(json.dumps({k:v for k,v in check.items() if not isinstance(v,list)},indent=2))
if __name__=='__main__':main()
