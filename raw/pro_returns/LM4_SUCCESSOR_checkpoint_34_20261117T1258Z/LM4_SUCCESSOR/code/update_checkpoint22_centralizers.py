"""Integrate the completely reviewed slit centralizer and annular obstruction."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
draft = root/'work_CE/B111_q0_diagonal_proposed.tex'
target = root/'sections/b_annular_diagonal_obstruction.tex'
assert draft.exists() and not target.exists()
target.write_bytes(draft.read_bytes())
(root/'records/B111_formal_source_copy22.json').write_text(json.dumps({
    'draft':str(draft.relative_to(root)),
    'integrated':str(target.relative_to(root)),
    'sha256':hashlib.sha256(draft.read_bytes()).hexdigest(),
    'comparison':'Byte-identical complete reviewed proof.'
},indent=2)+'\n')
p = root/'sections/part_B.tex'
s = p.read_text()
for name in ('b_slit_bad_centralizer.tex','b_annular_diagonal_obstruction.tex'):
    line = '\\input{sections/'+name+'}'
    assert line not in s
    s += line+'\n'
p.write_text(s)
subprocess.run([sys.executable,str(root/'code/assemble_register.py')],check=True)
rows = list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 280
assert dict(Counter(r['status'] for r in rows)) == {
    'Known':6,'Proved':236,'Refuted':19,'Open':19}

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
    for sid in ('B.110','B.111'):
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids'] += ';'+sid
    row['state'] = row['state'].replace(
        'Its cone centralizer reduces to one still-unknown bad vertex.',
        'Its cone centralizer reduces to a bad vertex, now computed on the slit by B110.')
    row['state'] += (
        ' B110 identifies the actual slit bad vertex as a marked HNN extension '
        'of a twelve-vertex RAAG by C2, proves its proper full profinite HNN '
        'comparison, and identifies the cone centralizer with the actual '
        'four-contact source F4 times C2. Combined with B108 it proves the '
        'selected fixed-source equality on the actual one-neck slit model, '
        'including its selected original-cover component and full completion. '
        'B111 proves that restoring the actual q=0 loop kills the nontrivial '
        'diagonal [p,bar p], even after full completion.')
    row['approaches'] += (
        ' Exact six-strand regional van Kampen with rational-to-cyclotomic '
        'configuration isotopy; same-sheet inverse Nielsen transformations; '
        'finite RAAG/HNN normal form; all-module goodness and prime-order '
        'centralizer comparison through cofinal finite heads; actual even '
        'Borel source conjugators; literal annular kernel witness.')
    row['obstruction'] = row['obstruction'].replace(
        'The first-neck vertex centralizer remains unevaluated.',
        'The first-neck vertex centralizer is computed on the simply connected slit; '
        'its annular analogue remains unevaluated.')
    row['obstruction'] += (
        ' The slit-to-annular map has a proved nontrivial kernel, so the '
        'annular group is not obtained by assuming stability of the ten '
        'slit relations. Neither the full annular saturation nor the '
        'other-neck quotient-edge comparisons have been determined.')
    row['next_step'] = (
        'Determine the actual annular presentation and selected cone '
        'centralizer after restoring q=0, using the explicit new diagonal '
        'and complete retained operator. Compare actual quotient-edge '
        'groups at the other four necks. Retain the separate global '
        'selected-source, nonlinear, coefficient and final joint-source gates.')
with p.open('w',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerows(coverage)

p = root/'LM4_SUCCESSOR_paper.tex'
s = p.read_text()
old = '''An actual one-neck slit model has a proper full profinite amalgam,
but its remaining vertex centralizer is unevaluated. The three natural
middle-neck maps are noninjective, and their first pair of based node
relations gives an explicit two-relator HNN block. The global transfer,
deeper nonabelian lifting and subsequent joint-source condition remain
unresolved.'''
new = '''An actual one-neck slit model has a proper full profinite amalgam.
Its bad vertex is a specified HNN extension of a finite graph group by
an involution; its cone centralizer is exactly the actual free-four
fixed source, discretely and in full completion. This proves the selected
source equality on that model, including the selected original-cover
component. The three natural middle-neck maps are noninjective, and
restoring the old zero loop kills an explicit nontrivial slit diagonal.
The annular comparison, remaining necks, global transfer, deeper
nonabelian lifting and subsequent joint-source condition remain unresolved.'''
assert old in s
p.write_text(s.replace(old,new,1))

p = root/'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert s.splitlines()[0] == 'INCOMPLETE'
marker = '### Completed actual slit centralizer and annular kernel witness'
assert marker not in s
s += '''\n'''+marker+'''

The later completed work resolves the slit bad-vertex centralizer left
unevaluated at the preceding stage. B110 gives its exact marked HNN
presentation with twelve ordinary graph vertices and eighteen edges.
The two associated groups are literal rank-two abelian cliques. The
branch replacement and all ten regional relations have reversible
Tietze transformations, checked independently with different word
normal forms. The coefficient deformation from rational inputs to
the actual fifth roots is uniformly certified on all fifty paths.
Both distinct nodes at the simultaneous value and the retained branch
are present. No numerical picture or incidence-only relation is used.

The graph involution fixes exactly the free group generated by the
four commuting paired products a*bar(a),b*bar(b),d*bar(d),e*bar(e).
A reduced dependence-word argument proves this directly. The full
profinite comparison verifies residual finiteness, finite virtual
cohomological TYPE and goodness for arbitrary discrete continuous
modules. Lorensen's full primary HNN goodness proof and the applicable
Boggi--Zalesskii prime-order proof were reopened. Compatible finite
clique kernels and cofinal virtually free HNN heads prove properness
and the completed centralizer equality; no unproved completion of an
infinite-index group is substituted.

The four generators are the ACTUAL fixed-source loops. In the generic
orbifold fiber, each positive contact transport has a unique even
conjugator of the cone. Borel transport determines the multiplication
order, and the extending far section identifies that exact conjugator
with the source after filling. In the same-sheet basis the four loops
are the four diagonal products in physical order a,d,e,b. An independent
ordinary detector checks all twenty Reidemeister--Schreier relators and
retracts onto this source. Thus its full induced topology is proved.

With mirror-paired slits, B108 now gives the actual selected fixed-source
equality over the whole one-neck slit model, retaining all eighteen
critical base values. Its selected source is free of rank four. The
original source double cover has TWO components on this simply connected
base, because sqrt(1-q) exists before its four contact points are removed.
The selected component maps isomorphically to the quotient source.
Intersection with the actual open index-two surface-cover subgroup
gives the same ordinary and profinite equality upstairs. The connected
source-cover hypothesis of the global two-coset argument is not used.

B111 proves the next gate is substantive. For the actual retained q=0
operator, the inverse image of the beta33 contact relator is exactly
(a b^-1 w p)[p,bar(p)](a b^-1 w p)^-1. The graph has no p--bar(p)
edge, so its coordinate retraction onto free F(p,bar(p)) proves that
commutator nontrivial. The proper base completion proves it survives
in the full slit completion as well. Restoring the actual zero loop
kills it. Consequently both the discrete and completed slit-to-annular
maps are noninjective. This is an explicit kernel witness, not a failure
of a bounded membership search, and it does not decide the annular
centralizer or the global fixed-source equality.

The complete new formal baseline is 280 statements:236 Proved,19 Refuted,
19 Open and6 Known, with109 bibliography entries and49 task/lead rows.
Both main full decisions remain Open. The annular saturation and its
centralizer, the other-neck quotient comparisons, the global selected
source and the final joint-source condition remain separate obligations.
Main A's bounded V4--Heisenberg attempt is retained as a failed coefficient
coupling method, not as a new formal theorem or a counterexample to GT.
The actual Fox unit and third-cusp decisions remain Open.
'''
p.write_text(s)
subprocess.run([sys.executable,str(root/'code/update_checkpoint_report.py')],check=True)
print('Integrated B110--B111:280 statements,109 bibliography records,49 task rows; both main decisions Open.')
