from pathlib import Path
import json,csv,re

root=Path('/workspace/scratch/f28c4f52d3ec'); page='148_scan069'
out=root/'proposed'
data=json.loads((out/f'{page}.json').read_text())
tex=(out/f'{page}.tex').read_text()
marks=list(csv.DictReader((root/'packets'/page/'MARKS.tsv').open(),delimiter='\t'))
assert [d['id'] for d in data['decisions']]==[m['id'] for m in marks]
assert len(data['doubts'])==len(data['decisions'])==tex.count(r'\unsure{')==4
assert all(d['decision']=='undecided' for d in data['decisions'])
assert not data['implicit_decisions']
assert len(data['changes'])==6
assert all(c['diff_c'] or c['diff_h'] for c in data['changes'])
assert all(c['viewed'] and c['main_reader_viewed'] for c in data['crops'])
assert len(data['crops'])==data['crop_files_saved']==data['crop_files_viewed']==9
assert sum('extends' not in c for c in data['crops'])==data['places_cropped']==7
for crop in data['crops']:
    assert (root/'result'/crop['crop']).is_file()
    assert Path(crop['view_path']).is_file()
    x0,y0,x1,y1=crop['box']
    assert 0<=x0<x1<=2358 and 0<=y0<y1<=1682
for entry in data['changes']+data['decisions']:
    assert any(entry['crop']==c['crop'] and entry['box']==c['box'] for c in data['crops'])
boxes=[tuple(b[k] for k in ['x0','y0','x1','y1']) for b in data['second_boxes']]
assert len(boxes)==len(set(boxes))==2
for x0,y0,x1,y1 in boxes: assert 0<=x0<x1<=2358 and 0<=y0<y1<=1682
assert data['second_boxes'][0]['reading']==tex[tex.index(r'\figure{'):tex.index('% crop-candidate:')].strip()
assert data['second_boxes'][1]['reading']==r'\mspage{68}'
for doubtful in [d['reading'] for d in data['doubts']]: assert doubtful in data['second_boxes'][0]['reading']

# Lexical checks only; no TeX engine is invoked.
balance=0
for token in re.findall(r'(?<!\\)[{}]',tex):
    balance+=1 if token=='{' else -1
    assert balance>=0
assert balance==0
assert tex.count(r'\begin{tikzpicture}')==tex.count(r'\end{tikzpicture}')==1
assert tex.count('$')==32
assert tex.count(r'\node[')==16
assert tex.count(r'\coordinate (')==16
assert tex.count(r'\draw[')==45
assert tex.count(r'\path[')==2
assert r"\'" not in (out/f'{page}.json').read_text()
assert data['workflow']['tex_compiled'] is False
check=json.loads((out/f'{page}_incidence_check.json').read_text())
assert (check['vertices'],check['finite_edges'],check['bounded_face_count'],check['exterior_rays'])==(16,35,20,10)

report=dict(page=page,status='passed',scope='Metadata, saved evidence, exact full-figure audit coverage, graph counts and lexical TeX structure; no compilation.',
    changes=6,decisions=4,doubts=4,unique_audit_boxes=2,places_cropped=7,crop_files_seen=9,
    vertices=16,finite_edges=35,exterior_rays=10,label_nodes=16,tex_compiled=False)
(out/f'{page}_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
