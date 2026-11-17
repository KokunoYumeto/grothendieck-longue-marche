"""Integrate the three completely reviewed actual regional comparisons."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import json
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
backup=root/'records/pdf_qa/checkpoint24_before_integration'
backup.mkdir(parents=True,exist_ok=False)
for name in ['LM4_SUCCESSOR_paper.pdf','LM4_SUCCESSOR_paper.tex','LM4_SUCCESSOR_paper.log','LM4_SUCCESSOR_paper.bbl']:
    source=root/name
    target=backup/(name+'.retained.txt' if source.suffix=='.bbl' else name)
    target.write_bytes(source.read_bytes())

copies=[
 ('work_CE/B115_prefix_section_obstruction_proposed.tex','sections/b_prefix_section_obstruction.tex'),
 ('records/proposed_B116_intrinsic_centralizers24.tex','sections/b_intrinsic_regional_centralizers.tex'),
 ('work_CE/B117_neck_base_subgroup_proposed.tex','sections/b_neck_base_subgroup.tex'),
]
for number,source in [(115,copies[0][0]),(117,copies[2][0])]:
    review=json.loads((root/f'work_DE/next_marginal_source/review_B{number}_frozen_source24.json').read_text())
    assert review['status']=='PASS_COMPLETE_FROZEN_SOURCE'
    assert review['source_sha256']==hashlib.sha256((root/source).read_bytes()).hexdigest()
assert 'PASS' in (root/'work_A/review_B116_intrinsic_centralizers24.md').read_text()
records=[]
for source,target in copies:
    src,dst=root/source,root/target
    assert src.exists() and not dst.exists()
    dst.write_bytes(src.read_bytes())
    records.append({'source':source,'integrated':target,'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'comparison':'Byte-identical fully reviewed source.'})
(root/'records/checkpoint24_formal_source_copies.json').write_text(json.dumps({'integrated_at':datetime.now(timezone.utc).isoformat(),'copies':records},indent=2)+'\n')

part=root/'sections/part_B.tex'
text=part.read_text()
for _,target in copies:
    line='\\input{'+target+'}'
    assert line not in text
    text+=line+'\n'
part.write_text(text)

p=root/'LM4_SUCCESSOR_paper.tex'
text=p.read_text()
old='''Its source image, the remaining necks,
global transfer, deeper nonabelian lifting and subsequent joint-source
condition remain unresolved.'''
new='''An explicit finite quotient excludes the proposed prefix extension
across every ordinary regional base section, also in full completion.
Exact discrete centralizers exclude any regional automorphism extending
that prefix change. The actual neck together with its base loop is an
ordinary regional retract with a marked index-two tree graph presentation;
the embedded branch word is retained. The source image after the two
cross relations, the remaining necks, global transfer, deeper nonabelian
lifting and subsequent joint-source condition remain unresolved.'''
assert old in text
p.write_text(text.replace(old,new,1))

p=root/'task_coverage.csv'
with p.open() as stream:
    reader=csv.DictReader(stream);fields=reader.fieldnames;coverage=list(reader)
assert len(coverage)==49
for row in coverage:
    if row['task'] not in {'B.4','B.4.a','B.4.b','B.4.c','B.4.h'}:
        continue
    assert row['outcome']=='Open'
    for sid in ['B.115','B.116','B.117']:
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids']+=';'+sid
    row['state']+=' B115 proves a uniform obstruction to extending the literal prefix automorphism across any ordinary regional element of odd base winding, also in full completion, using one actual finite quotient. B116 computes two intrinsic discrete regional centralizers and excludes every regional automorphism extending that prefix change. B117 identifies the actual neck-plus-base subgroup as an ordinary regional retract, with an eleven-vertex tree RAAG in index two and the exact embedded free-nine neck word f^2=k1^-1 t k0^-1. These are pre-cross results; the actual post-cross centralizer remains Open.'
    row['approaches']+=' Exact whole-presentation module quotient and geometric parity; full infinite-graph links and HNN-axis centralizers; invariant color retraction and complete Reidemeister-Schreier rewriting with actual branch marking.'
    row['obstruction']+=' The literal prefix automorphism cannot be extended while preserving an ordinary base section, and cannot extend to any discrete regional automorphism. A basis substitution with transformed relators remains valid. The finite-index tree presentation does not make the actual common neck coordinate.'
    row['next_step']='Retain the transformed regional and mirror relations, use the actual neck-plus-base subgroup and full-boundary corner to determine the source image and centralizer after both cross relations. Prove any required corner/vertex injection explicitly. Then compare the other four necks and global source, retaining the separate final joint-source and nonlinear gates.'
with p.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(coverage)

subprocess.run([sys.executable,str(root/'code/assemble_register.py')],check=True)
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==286
assert dict(Counter(row['status'] for row in rows))=={'Known':6,'Proved':242,'Refuted':19,'Open':19}

p=root/'LM4_SUCCESSOR_report.md'
text=p.read_text()
assert text.splitlines()[0]=='INCOMPLETE'
marker='### Uniform prefix obstruction and the actual neck-plus-base subgroup'
assert marker not in text
text+='\n'+marker+'''

B115 proves a uniform statement in the actual B112 region before the
two B114 cross relations. The physical prefix automorphism sends a to
aB. One explicit surjective quotient onto (F2)^12 semidirect S3 satisfies
all seventeen regional defining relations. The image of aB has two
lamps in different named families and positions; its centralizer in
the finite target is exactly the lamp subgroup. The permutation sign
is the sum of the actual ordinary-cover character and geometric base
winding modulo two. Consequently no ordinary odd-winding element can
centralize aB. The existing relation [k,a]=1 therefore prevents every
regional extension of the prefix automorphism whose base-generator
image is ordinary of odd winding. This includes arbitrary ordinary
degree+1 or degree-1 section choices, not only whisker changes. The
same one finite quotient proves the full profinite statement.

The actual K has its full topology by the ordinary retraction and
finite-index core comparison. The proof therefore types the completed
restriction precisely. Two independent implementations check the whole
actual relation set, the literal meridian/prefix substitutions and
the geometric parity. The first fixed-k detector and the subsequent
transposition-only version are preserved with their genuine outputs.
No broader finite-group census was run, and no regional obstruction
was transferred through the actual cross quotient.

B116 gives a separate intrinsic discrete obstruction. An exact
presentation isomorphism writes R as A(Omega) semidirect(D times Z),
where D=C2*Z and every coset/height translate of all ten node types is
retained. The complete links of a and B have common link precisely
{b,CaC}, while the entire link of a is discrete. A direct HNN-axis
argument proves the required one- and two-letter centralizer formulas
for an arbitrary infinite graph. The coarse abelianization then gives
C_R(a)=Z times(Z^2*F3) and C_R(aB)=Z times F2. Their abelianizations
have ranks six and three. Thus no discrete regional automorphism
sends a to aB, independently of its action on the base loop. No
completed centralizer formula for these infinite-order elements is
asserted. The needed special case is proved directly; the unsuccessful
attempt to access Servatius's original full proof is recorded and is
not used as a dependency.

B117 supplies a simpler actual marked subgroup for the continuing
quotient work. The group L=<K,k> is the image of an H-equivariant
color-deletion retraction of the whole ordinary region. Both color
classes in the full graph are edgeless. The retained class consists
of four complete H/<k> orbits, giving
L=H amalgam_<k>(<k> times F4), H=<h,k | [h^2,k]=1>.
Its auxiliary index-two subgroup is the graph group of an eleven-vertex,
ten-edge tree. The actual index-two neck is free of rank nine on the
eight leaf generators and F=f^2=k1^-1 t k0^-1. Replacing F by the
coordinate t would change the embedded neck. Explicit retractions
give all full-topology comparisons; no completion of the infinite
graph kernel is assumed. The complete ten Schreier rewrites and all
marked inverse identities have been executed and preserved.

All three results have complete root and independent source reviews.
They bring the formal register to286 statements:242 Proved,19 Refuted,
19 Open and6 Known. All49 task/lead rows remain. The two main full
decisions remain Open. The next actual task is the post-cross source
centralizer, retaining the transformed mirror relations and the full
boundary corner. New auxiliary-corner models must prove their maps
into that quotient; an isolated normal form does not supply injection.
'''
p.write_text(text)
print('Integrated B115--B117:286 statements; both main full decisions Open.')
