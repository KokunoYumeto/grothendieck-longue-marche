"""Integrate the fully checked actual torus-sphere image and its strict scope."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,json,hashlib,subprocess,sys
root=Path(__file__).resolve().parents[1]
rel='work_DE/B105_torus_spherical_block.tex'
assert (root/rel).exists()
p=root/'sections/part_B.tex';s=p.read_text();line='\\input{'+rel+'}'
assert line not in s;p.write_text(s+line+'\n')
old=root/'records/pdf_qa/checkpoint20_before_spherical'
old.mkdir(parents=True,exist_ok=True)
(old/'paper.pdf').write_bytes((root/'LM4_SUCCESSOR_paper.pdf').read_bytes())
(old/'metrics.json').write_bytes((root/'records/checkpoint20_metrics.json').read_bytes())
subprocess.run([sys.executable,str(root/'code/assemble_register.py')],check=True)
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==274
assert dict(Counter(r['status'] for r in rows))=={'Known':6,'Proved':230,'Refuted':19,'Open':19}
p=root/'task_coverage.csv'
with p.open() as f:
 r=csv.DictReader(f);fields=r.fieldnames;coverage=list(r)
for row in coverage:
 if row['task'] not in ['B.4','B.4.a','B.4.b','B.4.c','B.4.h']:continue
 assert row['outcome']=='Open' and 'B.105' not in row['statement_ids'].split(';')
 row['statement_ids']+=';B.105'
 row['state']+=' B105 proves that the actual torus sphere survives in Z2 and that its two involution-related deck orbits form a free rank2 spherical block with zero Tate cohomology.'
 row['obstruction']+=' The B100 sphere now has a proved nonzero Z2 image, but its induced two-orbit block is Tate-acyclic and does not determine the whole residual obstruction.'
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(coverage)
p=root/'LM4_SUCCESSOR_paper.tex';s=p.read_text()
old='''entire source orbit and its genuine geometric involution. Its full
kernel and additional Tate values remain undetermined. That obstruction,'''
new='''entire source orbit and its genuine geometric involution. The explicit
torus sphere survives in that cover and generates, with its involution
mate, a free rank-two spherical block with zero Tate cohomology. The
full kernel and its additional Tate values remain undetermined. That obstruction,'''
assert old in s;p.write_text(s.replace(old,new,1))
p=root/'LM4_SUCCESSOR_report.md';s=p.read_text()
s+='''\n### B105: the actual sphere survives, with an induced involution block

The previously undecided image of the B100 torus sphere in the actual
mixed-kernel cover is now determined. The old0 far lift has empty
source correction, so it is literally a fixed-source generator t.
With u=t inverse, a=p2 and b=p12 p13 p12 inverse, we use the actual
node(6,3) disk and the two nullhomotopies supplied by the prefilled
graph cylinders. Their pasted product-cube sphere has the complete
chain z=(u-1)n-(a-1)C_b+(b-1)c_2, with
C_b=(1-b)c_12+p12 c_13. Its sole node coefficient is u-1.
Since u has infinite order in the actual larger deck group, finite
support proves right multiplication by u-1 injective in its integral
group ring. Thus z is nonzero in the actual Z2, and its deck orbit is
free of rank1. This proves a genuine spherical-image comparison, not
merely a cycle in an unrelated presentation complex.

The actual F mate is the distinct node(6,7), with raw sign+1 and
conjugator p12 p14 inverse p12 inverse. Its private node row gives a
second independent deck orbit. These two orbits form a free rank2
module over the full larger coefficient ring. F exchanges its two
basis vectors semilinearly, making the underlying abelian C2-module
induced. All its Tate cohomology vanishes. This is a conclusion about
that particular block; neither the whole spherical image nor the
nonspherical quotient H2(M) nor kappa is determined by it.

Both actual ten-term sphere chains, their complete next-boundaries,
the physical-mate coefficient and F squared have two exact independent
checks, one using full normal-form/DAG data and one using tuple group
words. Root, A and CE read the entire formal proof. The private
three-page component is clean and all pages are visually inspected.
The resulting combined register has274 rows:230 Proved,19 Refuted,
19 Open and6 Known. Both main full decisions remain Open.
'''
p.write_text(s)
subprocess.run([sys.executable,str(root/'code/update_checkpoint_report.py')],check=True)
record={'recorded_at':datetime.now(timezone.utc).isoformat(),'canonical':rel,'sha256':hashlib.sha256((root/rel).read_bytes()).hexdigest(),'root_full_proof':'PASS','independent_formal_reads':['A','CE'],'complete_data_replays':['work_DE/next_marginal_source/check_actual_cube_sphere20.py','work_CE/code/check_B100_sphere_finite_matrix.py'],'scope':'Actual free rank2 spherical submodule only; full Z2 and kappa remain Open.'}
(root/'records/B105_root_review20.json').write_text(json.dumps(record,indent=2)+'\n')
print('Integrated B105;274 statements, both main full decisions Open.')
