from pathlib import Path
import json,csv,re

ROOT=Path('/workspace/scratch/f28c4f52d3ec'); PAGE='148_scan072'; OUT=ROOT/'proposed'
data=json.loads((OUT/f'{PAGE}.json').read_text()); tex=(OUT/f'{PAGE}.tex').read_text()
marks=list(csv.DictReader((ROOT/'packets'/PAGE/'MARKS.tsv').open(),delimiter='\t'))
assert [d['id'] for d in data['decisions']]==[m['id'] for m in marks]==['M0950']
assert data['decisions'][0]['decision']=='undecided'
assert tex.count(r'\unsure{')==len(data['doubts'])==2
assert not data['implicit_decisions']
assert len(data['changes'])==8 and all(c['diff_c'] or c['diff_h'] for c in data['changes'])
assert len(data['crops'])==data['crop_files_saved']==data['crop_files_viewed']==data['places_cropped']==7
assert all(c['viewed'] and c['main_reader_viewed'] for c in data['crops'])
for crop in data['crops']:
    assert (ROOT/'result'/crop['crop']).is_file() and Path(crop['view_path']).is_file()
    x0,y0,x1,y1=crop['box']; assert 0<=x0<x1<=2359 and 0<=y0<y1<=1682
for row in data['changes']+data['decisions']:
    assert any(row['crop']==c['crop'] and row['box']==c['box'] for c in data['crops'])
boxes=[tuple(b[k] for k in ['x0','y0','x1','y1']) for b in data['second_boxes']]
assert len(boxes)==len(set(boxes))==2
for x0,y0,x1,y1 in boxes: assert 0<=x0<x1<=2359 and 0<=y0<y1<=1682
assert data['second_boxes'][0]['reading']==tex[tex.index(r'\figure{'):tex.index('% crop-candidate:')].strip()
assert data['second_boxes'][1]['reading']==r'\mspage{71}'
for doubt in data['doubts']: assert doubt['reading'] in data['second_boxes'][0]['reading']
balance=0
for token in re.findall(r'(?<!\\)[{}]',tex):
    balance+=1 if token=='{' else -1
    assert balance>=0
assert balance==0
assert tex.count(r'\begin{tikzpicture}')==tex.count(r'\end{tikzpicture}')==1
assert tex.count(r'\coordinate (')==19
assert tex.count(r'\node[')==25
assert tex.count('$')==48
assert tex.count(r'\draw[')==53
assert tex.count(r'\fill[')==19
assert tex.count(r'\path[')==3
assert r"\'" not in (OUT/f'{PAGE}.json').read_text()
check=json.loads((OUT/f'{PAGE}_incidence_check.json').read_text())
assert check['left']['distinct_finite_endpoint_joins']==23 and check['left']['bounded_face_count']==13
assert all(d==3 for d in check['right']['total_incidence_degrees'].values())
assert check['right']['visible_numeric_annotations']==23
assert len(data['geometry_production']['manual_red_supplements'])==4
assert all(layer['filtered_mask_export_identical'] for layer in data['geometry_production']['layers'])
assert data['workflow']['tex_compiled'] is False
report=dict(page=PAGE,status='passed',scope='Saved evidence, MARKS coverage, exact complete audit target, graph checks and lexical TeX structure; no compilation.',
    changes=8,decisions=1,doubts=2,crop_files=7,unique_audit_boxes=2,
    left_vertices=11,left_distinct_joins=23,left_rays=7,right_vertices=8,right_finite_edges=9,
    right_rays=6,right_numeric_annotations=23,manual_red_support_paths=4,tex_compiled=False)
(OUT/f'{PAGE}_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
