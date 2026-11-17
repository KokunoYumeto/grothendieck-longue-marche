"""Integrate the reviewed actual one-neck comparison and mixed-neck obstruction."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
source = root/'work_DE/B109_middle_neck_obstruction.tex'
target = root/'sections/b_middle_neck_obstruction.tex'
assert source.exists() and not target.exists()
target.write_bytes(source.read_bytes())
(root/'records/B109_formal_source_copy22.json').write_text(json.dumps({
    'draft':str(source.relative_to(root)),
    'integrated':str(target.relative_to(root)),
    'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'comparison':'byte-identical full proof; no excerpt or silent revision'
},indent=2)+'\n')
p = root/'sections/part_B.tex'
s = p.read_text()
for rel in ('sections/b_neck_comparison.tex','sections/b_middle_neck_obstruction.tex'):
    line = '\\input{'+rel+'}'
    assert line not in s
    s += line+'\n'
p.write_text(s)
subprocess.run([sys.executable,str(root/'code/assemble_register.py')],check=True)
rows = list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 278
assert dict(Counter(r['status'] for r in rows)) == {'Known':6,'Proved':234,'Refuted':19,'Open':19}

p = root/'task_coverage.csv'
with p.open() as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    coverage = list(reader)
assert len(coverage) == 49
for row in coverage:
    if row['task'] not in ('B.4','B.4.a','B.4.b','B.4.c','B.4.h'):
        continue
    assert row['outcome'] == 'Open'
    for sid in ('B.108','B.109'):
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids'] += ';'+sid
    row['state'] += (' B108 proves the actual first-neck slit-model amalgam '
      'and its proper full profinite completion, using paired ordinary '
      'retractions and cofinal compatible finite edge quotients. Its cone '
      'centralizer reduces to one still-unknown bad vertex. B109 proves '
      'noninjection of the three natural middle-neck F5 maps on both sides '
      'and computes two distinct based relations at the first mixed neck; '
      'their precise two-relator quotient has an HNN/path presentation.')
    row['approaches'] += (' Actual common first-neck disk; paired ordinary '
      'one-family retractions; compatible finite amalgams and fully checked '
      'prime-order centralizer comparison; literal quadrant vanishing arcs '
      'and calibrated cut words.')
    row['obstruction'] += (' The first-neck vertex centralizer remains '
      'unevaluated. Natural mixed-neck edge maps have actual kernels, so '
      'a global amalgam cannot use them as free injective edges. The '
      'two-relator block is not the complete regional or shared-edge quotient.')
    row['next_step'] = ('Determine the complete actual bad-region relation '
      'presentation and cone centralizer, retaining six pair nodes, four '
      'cone contacts, the branch puncture and old q=0 operator. Compare '
      'the actual quotient-edge groups at every neck and restore all old '
      'base loops. Continue the full nonlinear, coefficient and final '
      'joint-source gates; do not infer a product from node incidence alone.')
with p.open('w',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerows(coverage)

p = root/'LM4_SUCCESSOR_paper.tex'
s = p.read_text()
old = '''The global transfer, deeper nonabelian lifting and subsequent
joint-source condition remain unresolved.'''
new = '''An actual one-neck slit model has a proper full profinite amalgam,
but its remaining vertex centralizer is unevaluated. The three natural
middle-neck maps are noninjective, and their first pair of based node
relations gives an explicit two-relator HNN block. The global transfer,
deeper nonabelian lifting and subsequent joint-source condition remain
unresolved.'''
assert old in s
p.write_text(s.replace(old,new,1))

p = root/'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert s.splitlines()[0] == 'INCOMPLETE'
marker = '## Twenty-second-hour research: actual completed neck comparison'
assert marker not in s
s += '''\n## Twenty-second-hour research: actual completed neck comparison

B108 proves a comparison on the actual simply connected slit inner and
outer regions joined by the first regular unit-circle neck. All eighteen
physical critical values remain. A common based disk selects the four
literal A punctures and one branch puncture. Ordinary one-family filling
maps the index-two subgroup of each bad vertex to the actual F7 bundle
fiber, and the disk free-factor projection gives a retraction to the
same K=F5. The projection also kills the entire cone-conjugate K: every
conjugated B peripheral is killed by filling, and the conjugated other
branch peripheral is killed by the projection. No whisker is discarded
and no equivariant one-family filling is asserted.

The paired retractions give actual maps to (K times K) semidirect C2,
with the involution swapping factors. Every finite edge kernel is
realized exactly in both vertices. This supplies compatible refinements
of arbitrary finite vertex quotients. Their finite-group amalgams are
virtually finite-rank free and residually finite, by an explicit regular
permutation action and the ordinary amalgam tree. These finite amalgams
factor every finite quotient of the actual one-neck group. Consequently
the vertex completions embed and the full profinite amalgam is proper;
no residual finiteness of the original unknown vertices is assumed.

The selected odd cone fixes just its vertex in every finite amalgam.
The full prime-order element theorem of Boggi--Zalesskii applies there:
the proof explicitly verifies goodness for arbitrary discrete continuous
modules and finite virtual cohomological TYPE, not only finite vcd.
A finite-index free subgroup and the two-row cohomology comparison
establish all these hypotheses. Root and A reopened the entire applicable
primary prime-order proof, including Lemma2.2. Its centralizer conclusion
in each finite amalgam, followed by cofinal finite-quotient separation,
reduces the completed cone centralizer to its bad vertex completion.
The latter is still unknown. No nonsolvable finite-subgroup centralizer
assertion, closure-intersection exchange, or infinite-index completion
is used. The other four necks and old base loops remain outside this
specific theorem.

B109 proves an obstruction to extending the same free-edge gluing.
For each of the three natural middle-neck semicircle markings, an
actual horizontal path reaches a transverse selected-pair node while
all five selected punctures stay in the same quadrant. The complete
critical table excludes earlier nodes and retains both simultaneous
middle nodes. Transport of the actual vanishing disk and its whiskers
gives a nontrivial free-group commutator killed in each bad vertex.
The outer reflected path gives its own killed word; the two words are
not silently identified. Thus these particular edge maps fail injection
on both sides. This does not refute the desired fixed-source equality
or every alternative compatible marking.

At the first mixed neck, the radial arcs pass on opposite sides of
A4,A3 and the retained branch. Exact radical bounds fix the physical
order A2,A4,A3,branch,B1. One explicit positive cut basis gives the
raw outer relation [x1,x5] and raw inner relation
[x1,(x1x2x3x4)x5(x1x2x3x4)^-1]. Conjugating the WHOLE latter relation
by x1^-1 yields [x1,Px5P^-1], P=x2x3x4. The primitive basis change
P=w identifies the quotient by precisely these two relations with
<a,b,w | [a,b],[a,wbw^-1]> free-product F2. The first factor is an
HNN extension of Z times F2; its stable-letter kernel has the exact
bi-infinite path commutation presentation. This quotient is not claimed
to be the complete actual shared edge or regional image.

The retained scripts contain the genuine exact collision, radical,
polygon and cut-word checks, their outputs, and failed initial attempts.
Complete independent reviews accompany the two formal proofs. Both main
decisions remain Open; 49 task/lead rows remain. The formal register has
278 statements:234 Proved,19 Refuted,19 Open and6 Known. Subsequent complete
regional-presentation research is retained separately at its actual
verification stage; it does not become a formal theorem by computation
or by counting pair nodes alone.
'''
p.write_text(s)
subprocess.run([sys.executable,str(root/'code/update_checkpoint_report.py')],check=True)
print('Integrated B108--B109:278 statements,49 task rows; both main decisions Open.')
