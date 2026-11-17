"""Integrate seven completely reviewed statements; preserve every prior authored file."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, hashlib, json, re, shutil, subprocess, sys

root = Path(__file__).resolve().parents[1]
read = lambda rel: (root / rel).read_text()
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
specs = [
 ('A.103','work_A/A103_uniform_affine_congruence_proposed.tex','sections/a_uniform_affine_congruence.tex','1e598be72dd7e9166bb8e9fa9d12b4673e8f4220f442bf0d65afe4adc12c24a6'),
 ('A.104','work_A/A104_actual_congruence_automorphism_proposed.tex','sections/a_actual_congruence_automorphism.tex','e31670a92ac55b14d0f8d66a223f41600edf0319392625f8097ff68bb5125a50'),
 ('A.105','work_DE/A105_original_CM_parity_proposed.tex','sections/a_original_CM_parity.tex','acd5911db9ecdea7bdc7c1f109efc70e802834aeff00ba5c81989b76ab031950'),
 ('B.161','work_CE/B161_unfilled_source_double_proposed.tex','sections/b_unfilled_source_double.tex','ba428758794974325241d3c1c2d312f8a7a3d1ac668d0b9f4a34ef955fe88487'),
 ('B.162','work_CE/B162_unfilled_double_full_topology_proposed.tex','sections/b_unfilled_double_full_topology.tex','706f4c92dc874c7b2aa545065e976879b82e0d6428f6721bc91abaad2c2abb79'),
 ('B.163','work_CE/B163_actual_coset_cohomology_proposed.tex','sections/b_actual_coset_cohomology.tex','f837cc3bf622c2c1456fa8c96c063e7d08aac97c33ac8eebf079a607d0fb0d77'),
 ('B.164','work_CE/B164_remaining_contact_cohomology_proposed.tex','sections/b_remaining_contact_cohomology.tex','5c6d51d085df882a2a24927742274ab40f83da254c7f194884b46631c9fb7c5a'),
]
copies = [dict(statement=s, source=p, target=t, sha256=h) for s,p,t,h in specs]
for row in copies:
    data = (root/row['source']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == row['sha256']
    assert not any(c < 32 and c not in (9,10) for c in data)
    assert not (root/row['target']).exists()
review_paths = [
 'work_DE/review_A103_A104_full_source33.md',
 'work_DE/review_A103_A104_full_source33.json',
 'work_CE/review_A103_A104_A105_formal33.txt',
 'work_CE/review_A103_A104_A105_formal33.json',
 'work_A/review_A105_full_source33.md',
 'work_A/review_A105_full_source33.json',
 'work_DE/review_B161_B164_full_source33.md',
 'work_DE/review_B161_B164_full_source33.json',
 'work_A/review_B161_B163_full_source33.md',
 'work_A/review_B161_B163_full_source33.json',
 'work_A/review_B163_final_category_diff33.md',
 'work_A/review_B163_final_category_diff33.json',
]
reviews = {p:sha(root/p) for p in review_paths}
review = dict(status='PASS_COMPLETE_SOURCE_REVIEW',
    recorded_at=datetime.now(timezone.utc).isoformat(), reviewer='/root',
    scope='All seven complete mathematical sources read; final source changes checked by complete preserved diffs. Independent complete reviews bind the exact final sources. This is mathematical source review, not PDF visual approval.',
    copies=copies, independent_reviews=reviews,
    remaining_open=['Main A','Main B','Actual CM parity epsilon_A = d mod 3'])
review_path = root/'records/checkpoint33_root_formal_reviews.json'
assert not review_path.exists()

paper=read('LM4_SUCCESSOR_paper.tex')
anchor=r'\input{sections/a_odd_boundary_relative_two.tex}'
assert paper.count(anchor)==1
paper=paper.replace(anchor,anchor+'\n'+'\n'.join(r'\input{'+r['target']+'}' for r in copies[:3]))
anchor='before any further square or nilpotent filling.'
assert paper.count(anchor)==1
paper=paper.replace(anchor,anchor+'\n'
    'A uniform affine sphere-pentagon calculation over every finite ring\n'
    'proves that the original hexagon word vanishes in the entire signed\n'
    'congruence image. The prescribed endomorphism is an automorphism\n'
    'there, and its full surjectivity is exactly surjectivity on the actual\n'
    'congruence kernel. The original involution descends and is conjugate\n'
    'to complex conjugation on that image. In the original CM frames,\n'
    'the parity is the product of two specified signs; for actual full-GT\n'
    'data one sign is determined by the unit modulo three. Equality with\n'
    'the other frame sign, and hence the actual parity, remains open.')
anchor='The fixed-source equality, remaining necks, global transfer and final\njoint-source condition remain unresolved.'
assert paper.count(anchor)==1
paper=paper.replace(anchor,
    'The actual unfilled source double has its full induced topology; its\n'
    'fold-kernel closure is a continuous pointed free profinite group on\n'
    'the completed source coset space. The discrete fold kernel itself\n'
    'does not inherit its full topology. Continuous nonabelian cohomology\n'
    'identifies the remaining fixed-source question with equality of an\n'
    'exact filling-cohomology kernel and the closed image of all three\n'
    'whole contact orbits. Its ordered cocycle action and cofinal\n'
    'finite-neighborhood criterion retain the actual nodes and connectors.\n'+anchor)
part_b=read('sections/part_B.tex')
for row in copies[3:]:part_b+=r'\input{'+row['target']+'}\n'
with (root/'task_coverage.csv').open(newline='') as stream:
    reader=csv.DictReader(stream);fields=reader.fieldnames;tasks=list(reader)
assert len(tasks)==49
old_outcomes=[(r['task'],r['outcome']) for r in tasks]
for row in tasks:
    selected=[]
    if row['task'] in {'A.4','A.5','A.7','A.8'}:
        selected=['A.103','A.104']
        row['state']+=' Cycle33: A103 proves actual full-GT hexagon vanishing in every signed congruence image; A104 proves the prescribed actual congruence automorphism, original involution descent, and exact remaining kernel-surjectivity criterion.'
        row['approaches']+=' Uniform finite-ring affine sphere pentagon; actual finite congruence images and compactness; direct peripheral-matrix descent.'
        row['obstruction']='Full congruence conjugacy and surjectivity are established for the stated actual full-GT data. Full free-profinite kernel surjectivity, the full nonlinear word, and canonical realization remain open. The full-GT pentagon is not supplied for arbitrary GT0 data.'
        row['next_step']='Analyze the actual congruence kernel and its relative central quotients, retaining the prescribed map and all original cusp frames.'
    if row['task'] in {'A.6','A.7','A.8'}:
        selected+=['A.105']
        row['state']+=' A105 identifies the original LM7_PUSH E65 parity as epsilon_A epsilon_u; for actual full-GT data epsilon_u=d modulo3. The remaining equality epsilon_A=d modulo3 is Open.'
        row['obstruction']+=' The positive order-three frame A is distinct from the negative conjugator s phi A; its sign is not settled by the negative norm equation.'
    if row['task'] in {'B.4','B.4.a','B.4.b','B.4.c','B.4.h'}:
        selected=['B.161','B.162','B.163','B.164']
        row['state']+=' Cycle33: B161-B164 prove the embedded unfilled source double, its full topology, the continuous coset-kernel model and H1 embedding, and the exact remaining contact-image equality with its ordered action and cofinal actual finite-neighborhood criterion.'
        row['approaches']+=' Pre-node deleted-family comparison; arbitrary finite-target extension; proper profinite amalgams; finite-factor torsion theorem; compact compatible conjugators and lift sets; full ordered contact orbits.'
        row['obstruction']='The actual cohomology kernel is not yet proved equal to the closed whole contact image. A known contact already refutes injectivity of the whole H1 map as a shortcut. Other necks, global transfer, and the original uniform source-neighborhood condition remain open.'
        row['next_step']='Compute the actual whole family-kernel H1 and the filling fiber; compare its entire zero fiber with all three continuous contact orbits while retaining every node and connector.'
    for sid in selected:
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids']+=';'+sid
assert [(r['task'],r['outcome']) for r in tasks]==old_outcomes
assert all(next(r for r in tasks if r['task']==t)['outcome']=='Open' for t in ('A.8','B.4'))
report=read('LM4_SUCCESSOR_report.md')
assert report.splitlines()[0]=='INCOMPLETE'
lines=report.splitlines(True)
start=next(i for i,line in enumerate(lines) if line.startswith('| Task or lead |'))
end=start
while end<len(lines) and lines[end].startswith('|'):end+=1
cell=lambda s:s.replace('|',r'\|').replace('\n',' ')
lines[start:end]=['| Task or lead | Statements | Outcome and exact state |\n','|---|---|---|\n']+[
 '| '+cell(r['task'])+' | '+cell(r['statement_ids'])+' | **'+cell(r['outcome'])+'** — '+cell(r['state'])+' |\n' for r in tasks]
report=''.join(lines)+'\n\n'+read('records/thirty_third_hour_research_report.md')

backup=root/'records/pdf_qa/checkpoint33_before_integration'
assert not backup.exists()
paths=['LM4_SUCCESSOR_paper.'+e for e in ('pdf','tex','log','aux','bbl','blg','toc','out')]
paths+=['LM4_SUCCESSOR_results.csv','LM4_SUCCESSOR_references.bib','LM4_SUCCESSOR_report.md','task_coverage.csv','sections/part_B.tex','sections/b_sources.bib','code/assemble_register.py']
paths+=[str(p.relative_to(root)) for p in (root/'records').glob('build_*.log')]
for rel in paths:
    src=root/rel
    if src.is_file():
        suffix='.retained.txt' if src.suffix in {'.aux','.bbl','.blg','.toc'} else ''
        dst=backup/(rel+suffix);dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
review_path.write_text(json.dumps(review,indent=2)+'\n')
for row in copies:(root/row['target']).write_bytes((root/row['source']).read_bytes())
(root/'LM4_SUCCESSOR_paper.tex').write_text(paper)
(root/'sections/part_B.tex').write_text(part_b)
(root/'LM4_SUCCESSOR_report.md').write_text(report)
with (root/'task_coverage.csv').open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(tasks)
register_source=read('code/assemble_register.py')
old="else 'A.7;A.8'),notes="
new="else ('A.6;A.7;A.8' if int(m[2])==105 else 'A.7;A.8')),notes="
assert register_source.count(old)==1
(root/'code/assemble_register.py').write_text(register_source.replace(old,new))
(root/'records/checkpoint33_formal_source_copies.json').write_text(json.dumps(dict(
    integrated_at=datetime.now(timezone.utc).isoformat(),copies=copies,
    comparison='All seven integrated sources are byte-identical to their final reviewed sources.'),indent=2)+'\n')
subprocess.run([sys.executable,str(root/'code/assemble_register.py')],check=True)
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==354 and dict(Counter(r['status'] for r in rows))=={'Known':6,'Proved':310,'Refuted':19,'Open':19}
assert len(re.findall(r'^@',read('LM4_SUCCESSOR_references.bib'),re.M))==115
print('Integrated7 reviewed statements:354 claims,310Proved,19Refuted,19Open,6Known;115references,49tasks. Both mains and actual CM parity remain Open.',flush=True)
