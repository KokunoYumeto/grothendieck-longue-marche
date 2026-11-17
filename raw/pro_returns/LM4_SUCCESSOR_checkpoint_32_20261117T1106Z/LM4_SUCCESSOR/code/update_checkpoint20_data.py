"""Integrate four fully reviewed main-B comparisons; retain all open tasks."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv, hashlib, json, subprocess, sys
root=Path(__file__).resolve().parents[1]
inputs=['work_CE/B101_all_diagonal_head_kernels.tex',
        'work_A/B102_nodal_cover_Smith_edge.tex',
        'sections/b_root_path_normal_form.tex',
        'work_DE/B104_boundary_models.tex']
p=root/'sections/part_B.tex';s=p.read_text()
for rel in inputs:
 assert (root/rel).exists(),rel
 line='\\input{'+rel+'}'
 assert line not in s,('Already integrated',rel)
 s+=line+'\n'
p.write_text(s)
subprocess.run([sys.executable,str(root/'code/assemble_register.py')],check=True)
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==273
assert dict(Counter(r['status'] for r in rows))=={'Known':6,'Proved':229,'Refuted':19,'Open':19}
for sid in ['B.101','B.102','B.103','B.104']:
 assert next(r for r in rows if r['id']==sid)['status']=='Proved'
p=root/'task_coverage.csv'
with p.open() as f:
 r=csv.DictReader(f);fields=r.fieldnames;coverage=list(r)
assert len(coverage)==49
addition=('B101 determines all eight actual augmented diagonal-row stabilizers. '
'B102 identifies the full actual E-cover and its Smith edge, retaining spherical '
'and nonspherical H2. B103 supplies exact integral root-path normal forms and '
'excludes every group-ring unit multiple for a complete actual stabilizer column. '
'B104 gives faithful21/16-row coordinates and a finite32/359-cell model retaining '
'every source translate and the genuine geometric involution.')
for row in coverage:
 if row['task'] not in ['B.4','B.4.a','B.4.b','B.4.c','B.4.h']:continue
 assert row['outcome']=='Open'
 for sid in ['B.101','B.102','B.103','B.104']:
  assert sid not in row['statement_ids'].split(';')
  row['statement_ids']+=';'+sid
 row['state']+=' '+addition
 row['obstruction']=('All eight row stabilizers and the actual complete E-cover comparison '
 'are now proved. The whole source orbit is encoded by a finite free complex '
 'over its actual enlarged coefficient group, but its equivariant H2 and Smith '
 'edge are not determined. Full-column unit monomiality fails on an actual '
 'head stabilizer; no whole-span conclusion follows. The residual image U/J_I, '
 'the nonlinear defect in [M,M], the actual compact coefficient comparison, '
 'projected fixed-source equality and the subsequent joint-source condition '
 'remain Open. Neither asphericity of Z nor vanishing of its H2 can be assumed.')
 row['next_step']=('Analyze the actual finite whole-orbit complex and its geometric '
 'involution to determine the Smith edge, including the nonspherical quotient '
 'H2(M). Investigate the actual graph-section filling kernels and the reflection '
 'pencil critical-filling map, with their required marked comparisons. Then '
 'resolve the separate nonlinear, compact and joint-source conditions. No '
 'finite-depth orbit list, rank localization, or isolated-column equality '
 'may replace the whole-kernel calculation.')
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(coverage)
p=root/'LM4_SUCCESSOR_paper.tex';s=p.read_text()
old='''An exact two-operator presentation determines one entire transported-row
stabilizer, while actual complete words refute a proposed passage from
equal augmented rows to full-column relations. The symmetric complement
has an explicit $\\mathbb Z^3$ retract and a nonzero torus attaching sphere,
so it is not aspherical. All additional Tate values still lie in the
cohomology of the kernel of the orbit-sum map. That overlap contribution,
deeper nonabelian lifting, projected fixed-source equality and the
subsequent joint-source condition remain unresolved.'''
new='''Exact two-operator presentations determine all eight transported-row
stabilizers, while complete integral root-path normal forms refute
full-column monomiality even for every unit of the coefficient ring.
The symmetric complement has an explicit $\\mathbb Z^3$ retract and a
nonzero torus attaching sphere, so it is not aspherical. An actual
relative nodal comparison identifies its full covering complex and the
Smith edge, retaining the separate nonspherical homology term. Faithful
Fox edge coordinates give a finite complex with 32 one-cells and 359
two-cells over the actual enlarged coefficient group; it retains the
entire source orbit and its genuine geometric involution. Its full
kernel and additional Tate values remain undetermined. That obstruction,
deeper nonabelian lifting, projected fixed-source equality and the
subsequent joint-source condition remain unresolved.'''
assert old in s;p.write_text(s.replace(old,new,1))
p=root/'LM4_SUCCESSOR_report.md';s=p.read_text()
assert s.splitlines()[0]=='INCOMPLETE'
marker='## Twentieth-hour research: full cover and finite whole-orbit model'
assert marker not in s
s+='''\n## Twentieth-hour research: full cover and finite whole-orbit model

B101 determines all eight augmented diagonal-row stabilizers inside the
actual old-base kernel. It retains the actual four section maps, three
straight bridges, both bridge inverses and the two literal signed
operators generating each normal closure. The constant/moving comparison
uses the actual coordinate swap. Its cone centralizer argument covers
both cone classes. The auxiliary six-generator lifts are not asserted
to be full geometric monodromy. Complete root and independent reviews
and a clean four-page component verify the entire statement.

B102 gives the actual relative nodal homotopy comparison, on both the
underlying space and fixed subspace, with its based transports. The
E-cover has H1=M_ab and H2=Z2. The bounded Tate complex identifies the
source-coset augmentation quotient with the reduced fixed-locus H0;
its edge is exactly the previous algebraic kappa. The local fixed-node
source loop is the actual product ab and is retained. Ordinary
Brown--Loday coinvariants do not retain the E-action. Half-turn sphere
classes have the stated endpoint-difference image, while the Hopf
sequence retains the separate nonspherical quotient H2(M). Neither
fixed-locus dimension nor a particular nonzero pi2 class proves kappa
zero or nonzero. Root reopened Brown--Loday's complete applicable proofs
on printed314--315,318--321. The six-page component has full visual QA.

B103 proves an exact free integral root-path basis for the entire
product-tree chain module, with a complete boundary integration and
actual coefficient action. The original124-letter node(8,0) relator is
printed literally; the actual four signed old operators yield its full
119780-letter image. Their unique normal forms have42 and33162 terms.
The bi-order proves every unit of Z[G] is a signed group element, and
each such monomial creates at most twice the input support. Hence the
actual geometric head stabilizer does not send that column to any
ring-unit multiple. This does not prove two-column independence or
whole-span nonmembership. Complete independent word/DAG/boundary replay
and two full formal-proof reviews verify the claim. The earlier huge
square-expansion attempt remains retained as interrupted.

B104 proves faithful21-row and16-row descriptions of the whole relation
module. The retained forest has a unique cycle completion; its collapse
is a chain/cycle comparison, not an equivariant homotopy equivalence
with unchanged stabilizers. Genuine semilinear Fox matrices retain all
mixed conjugators. The exact16-row Tate extractor recovers diagonal
coefficients and the actual right-defect normalization. All35 matrices,
735 columns,703187 literal letters and695738 terms have an independent
replay, including all462 source/involution commutations. Both sheets
supply128 complete node cycles. The actual even-base CW model has32
edges and359 faces:231 source cylinders and128 nodes. Its M-cover is
the same C_E with the larger deck group G semidirect F11. Every one of
the359 columns, with319438 terms, has an independently checked zero
next-boundary. Its two-cell involution is derived from actual equivariant
cylinders and nodes; an arbitrary algebraic lift is not substituted.
This finite free complex encodes the entire source orbit. Its kernel
is not proved finitely generated or Tate-acyclic. The five-page
component is clean and all pages have been visually checked.

These four complete statements passed root and independent full-proof
reviews. The integrated register has273 rows:229 Proved,19 Refuted,
19 Open and6 Known, with108 verified-status bibliography entries and
all49 task and lead rows. Both main full decisions remain Open.

A separate exact reflection chart sends the actual surface to the
complement of22 affine lines and four conics, with involution
(a,b)->(a,-b) and base point(199/200,0). The fixed source is the affine
line with19 specified punctures. A finite explicit discriminant gives
an actual equivariant28-puncture bundle whose fixed subgroup is the
section image, discretely and in completion. The source proof and exact
Q(zeta5) basepoint check are retained as research, not an added numbered
claim. Inserting its critical fibers still requires a genuine
fixed-lifting comparison. Source lassos at its punctures are not killed
as though the section extended across them.

For the complete checkpoint, PNG verification images from this hour
onward use a standard nested TAR with standard identical-content hard
links, inside the one hourly ZIP. This lossless storage encoding retains
every path and every byte without reducing image quality. The digest
manifest and independent verifier cover every logical image file and
all prior versions. All mathematical files, PDFs, code, full data and
reports remain direct ZIP entries. The exact restoration command and
container hash are supplied. Earlier checkpoints remain unchanged;
no prior content is omitted.
'''
p.write_text(s)
subprocess.run([sys.executable,str(root/'code/update_checkpoint_report.py')],check=True)
review=dict(recorded_at=datetime.now(timezone.utc).isoformat(),scope='Root complete proof reads plus independent reviews, B101--B104',
files={rel:hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in inputs},
reviews={'B101':'Root full read; A and DE full reads; canonical4-page QA',
'B102':'Root full read; CE and DE full reads; canonical6-page QA; primary Brown--Loday reopened',
'B103':'Root complete source/producer proof; A and CE formal full reads; separate DE data replay',
'B104':'Root complete proposal read; A and CE full formal reads; separate DE full data replays'},
status='PASS',main_A='Open',main_B='Open')
(root/'records/checkpoint20_root_formal_reviews.json').write_text(json.dumps(review,indent=2)+'\n')
print('Integrated B101--B104:273 statements,49 task rows; both main decisions Open.')
