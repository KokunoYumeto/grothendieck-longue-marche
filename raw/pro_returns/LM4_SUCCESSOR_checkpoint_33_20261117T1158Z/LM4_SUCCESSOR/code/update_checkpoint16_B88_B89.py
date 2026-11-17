"""Integrate the exact zero-word refutation and symmetric compact comparison."""
from pathlib import Path
import csv
import shutil

root=Path(__file__).resolve().parents[1]
formal={r['id']:r['status'] for r in csv.DictReader(
    (root/'LM4_SUCCESSOR_results.csv').open())}
assert len(formal)==258
assert formal['B.88']=='Refuted' and formal['B.89']=='Proved'
path=root/'task_coverage.csv'
with path.open() as stream:
    reader=csv.DictReader(stream)
    fields,rows=reader.fieldnames,list(reader)
assert len(rows)==49
index={r['task']:r for r in rows}
addition=(
    'B88 refutes the specific normalized zero-word source membership, '
    'discretely and compactly, by an actual order64 paired Heisenberg '
    'quotient; that detector kills the ambient filling kernel and does '
    'not refute its desired source equality. B89 proves that the actual '
    'symmetric deletion-kernel intersection is the mutual commutator '
    'and that the same is true for the closed kernels. The compact '
    'comparison follows from an explicit finite-extension separation '
    'lemma and the full induced topology and density of the actual '
    'fiber product over the filled free-by-free group.'
)
for task in ('B.4','B.4.a','B.4.b','B.4.c','B.4.h'):
    row=index[task]
    assert row['outcome']=='Open'
    for sid in ('B.88','B.89'):
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids']+=';'+sid
    if addition not in row['state']:
        row['state']+=' '+addition
    row['obstruction']=(
        'The all-positive and coupled diagonal blocks do not establish '
        'whole source-kernel normalization under every retained '
        'direction. B88 proves the particular zero-word correction is '
        'outside the source, rather than leaving that finite-subgroup '
        'search as a conjectural membership. B89 now identifies the '
        'actual symmetric intersection and its compact topology; the '
        'remaining fixed-lift classes in nonabelian H1 of this mutual '
        'commutator are not proved neutral. The projected fixed-source '
        'comparison after the18 critical fillings is also unproved. '
        'B87 on the filled surface and the64 mixed transverse nodes '
        'do not supply either assertion. The later joint-source '
        'condition remains separate.'
    )
    row['next_step']=(
        'Resolve the actual nonabelian involution cocycles in the '
        'proved closed mutual-commutator kernel and the projected '
        'fixed-source comparison after critical filling. Retain the '
        'actual completion comparison of B89 and the negative '
        'zero-word constraint of B88. Alternatively prove the missing '
        'mixed-direction whole-kernel normalization directly, then '
        'address the joint-source and B75 uniform finite-cover gates.'
    )
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields)
    writer.writeheader();writer.writerows(rows)

paper=root/'LM4_SUCCESSOR_paper.tex'
s=paper.read_text()
old='''finite cone-class detector. These results do not supply the fixed-lift
comparison after symmetric deletion, whole source-kernel normality,
or the subsequent joint-source condition.'''
new='''finite cone-class detector. For the actual symmetric deletion we
identify the intersection of the two filling kernels with their mutual
commutator, including the closed kernels. An explicit finite-extension
argument proves the required full topology of the associated fiber
product. A separate actual order64 quotient excludes the specified
zero-direction source word. The remaining nonabelian fixed-lift
cocycles, projected fixed-source comparison, whole source-kernel
normality and subsequent joint-source condition remain unresolved.'''
assert old in s and new not in s
paper.write_text(s.replace(old,new,1))

p=root/'records/sixteenth_hour_research_report.md'
backup=root/'records/sixteenth_hour_research_report_initial_4_statements.md'
assert not backup.exists()
shutil.copyfile(p,backup)
s=p.read_text()
s=s.replace('The formal register presently has256 statements:215 Proved,16 Refuted,\n19 Open and6 Known, with102 bibliography entries.',
            'The first integrated build had256 statements:215 Proved,16 Refuted,\n19 Open and6 Known, with102 bibliography entries. The two subsequently\naccepted additions are recorded below; the frozen final counts are258\nstatements:216 Proved,17 Refuted,19 Open,6 Known, with104 references.')
s+='''
## Subsequent accepted additions in the same hour: B.88 and B.89

The specific zero-source membership discussed above is now refuted,
rather than left at the inconclusive169-word subgroup test. B.88 uses
the two actual maps v and v(w−1)/(1−v) into the three-punctured line.
They agree literally on the source and at the actual base point.
Their paired maps to UT3(F2) give an actual epimorphism onto the full
order64 direct product. The source maps exactly onto the diagonal.
The actual word a inverse b inverse z b a has two images differing by
the nonidentity central element, for all32 permitted central-coordinate
choices. Its exclusion holds equally for the actual compact source.
The maps factor through the both-family filling, so this finite
detector kills R and supplies no refutation of I=R. The formal B.86
scope paragraph now points to this exact negative conclusion; its
kernel proof is unchanged. The earlier proposed source and initial
combined PDF remain available as earlier states.

B.89 closes the actual completion comparison for the symmetric
deletion kernels. The two one-sided complements and the filled surface
are actual aspherical free-by-free bundles. Their union removes only
the finite mixed divisor intersection from the filled smooth four-real-
dimensional manifold, preserving pi1 and pi2. The precise Brown–Loday
Lemma4.1 applies to this open homotopy pushout without requiring the
symmetric intersection itself to be aspherical. Its kernel formula,
with Brown's explicit normal-subgroup crossed-commutator identification,
proves NA intersect NB=[NA,NB]. Both primary proofs were opened by
the root and independent reviewers at the exact steps used.

The compact conclusion is not obtained by interchanging an intersection
and a closure. We prove directly that every finite-kernel extension of
the actual finitely generated free-by-free group has a finite-index
subgroup avoiding that kernel. In the central case the discrepancy
between the lifted free-factor actions is killed on the characteristic
exponent-and-commutator subgroup of the free kernel. Centralizing a
general finite kernel reduces to its center over a finite-index
free-by-free quotient. This separates the kernel in a finite quotient.

For the actual fiber product, the two coordinate-kernel intersections
with an arbitrary finite-index normal subgroup are invariant under
the two ambient factors. Applying the finite-extension lemma to their
finite quotients, then taking a finite-index core in the common head,
proves the full induced topology. Intersection of finite-index cosets
in that head proves density in the actual compact fiber product.
Right exactness of completion and continuity of commutation then give
the actual closed intersection as the closed mutual commutator and as
the closure of the discrete intersection. No profinite homotopy
excision theorem is required.

This theorem identifies the group in which the fixed-lift obstruction
lives. It does not make every nonabelian involution cocycle neutral,
or identify the projected fixed subgroup with the source image. The
actual source injection on the filled surface also gives I=H intersect R;
thus the desired equality is equivalently that H is the preimage of
the filled source. The fixed fiber-product target has exactly that
description. Its fixed lifting and projected-source comparisons are
the remaining global requirements.

The original four-addition research record is preserved separately as
sixteenth_hour_research_report_initial_4_statements.md. Its once-open
zero-word membership and its not-yet-proved compact intersection are
superseded by B.88 and B.89, respectively. Both main full decisions
remain Open. All49 task and lead rows remain, with their individual
statuses and unresolved portions explicitly retained.
'''
p.write_text(s)
print('Integrated B88/B89 into coverage, abstract and research record;258 rows,104 references.')
