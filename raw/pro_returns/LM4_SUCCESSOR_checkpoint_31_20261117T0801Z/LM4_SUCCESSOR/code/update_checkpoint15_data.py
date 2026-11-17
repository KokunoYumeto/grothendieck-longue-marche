"""Integrate reviewed A82-A84 and B82 without changing the open main decisions."""
from pathlib import Path
import csv

root=Path(__file__).resolve().parents[1]
path=root/'task_coverage.csv'
with path.open() as stream:
    reader=csv.DictReader(stream)
    fields,rows=reader.fieldnames,list(reader)
assert len(rows)==49
index={r['task']:r for r in rows}
formal={r['id']:r['status'] for r in csv.DictReader(
    (root/'LM4_SUCCESSOR_results.csv').open())}
assert all(formal[sid]=='Proved' for sid in ('A.82','A.83','A.84','B.82'))

def add(task,ids,paragraph):
    row=index[task]
    for sid in ids:
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids']+=';'+sid
    if paragraph not in row['state']:
        row['state']+=' '+paragraph

module_state=(
    'Actual module refinement: A82 proves arbitrary finite-coefficient '
    'H1 restriction surjectivity, compact augmentation projectivity at '
    'every prime, and actual full-head dyadic freeness of rank two '
    '(rank one for the regular pants action). A83 proves odd finite-head '
    'twisted duality in G0; A84 upgrades it at every modular odd head '
    'and to projective duality over the full completed group ring. '
    'The incidence cokernel remains exactly the reduced coset module '
    'of the selected generator subgroup. Thus target freeness and '
    'twisted duality do not prove marked generation or universal conjugacy.'
)
for task in ('A.3','A.7','A.8','A.5','A.6'):
    add(task,['A.82','A.83','A.84'],module_state)
add('C.2',['A.82'],
    'The actual regular-pants reflection augmentation module is now '
    'proved free of rank one over Z2[[E]]. The selected one-loop '
    'incidence map is onto exactly when its selected reflection and '
    'loop generate E; that full generation remains unproved.')
index['A.8']['obstruction']=(
    'The unrestricted finite-action nonrealization theorem excludes a '
    'constructed family, not every surviving action. Actual full-head '
    'dyadic module freeness and compact twisted projective duality now '
    'hold, but the selected incidence map is not proved onto. Odd '
    'nonselfdual multiplicity imbalances have neither been constructed '
    'nor excluded. No full marked recognition or universal conjugacy '
    'proof, cofinal negative involution construction, or global '
    'c-invariant Z4 lift of delta has been obtained.'
)
index['A.8']['next_step']=(
    'Resolve the full selected incidence/generation problem or an actual '
    'surviving finite-action full-order obstruction. Do not substitute '
    'module target freeness, a pro-two unit test, or a noncofinal tower '
    'for full marked generation.'
)

b_current=(
    'Faithful configuration and split Birman comparisons retain the '
    'actual residual centralizer. B78-B79 give complete marginal '
    'pencils; B80 refutes a general one-tangency shortcut, not the '
    'actual marginal. B81 gives the actual tangent-line bundle and '
    'whole filling-kernel intersections. B82 retains all eleven even '
    'base actions and four opposite-family inner actions for each '
    'actual partial source, a literal source-contained rank-eight '
    'free factor, and a complete partial-kernel intersection in the '
    'ordered rank-nine D-factor, also after completion. The latter '
    'does not show that D squared normalizes the entire partial '
    'source kernel. The correct remaining target is whole deletion-'
    'kernel normality, not normality of the source group H. The '
    'restricted D8 separator does not survive the full source action. '
    'The marginal and subsequent joint-source gates remain Open.'
)
b_obstruction=(
    'The proved free-factor intersections do not glue to whole partial-'
    'kernel normality, including normalization by D squared. The actual '
    'w-projection research gives a verified common marking and a '
    'source-adapted fiber basis with three retained product-one cluster '
    'directions. Their normalization of the whole partial kernel is '
    'unproved. The global local-cluster twist also acts on exterior '
    'punctures, and two exterior factors have no established whole-'
    'kernel invariance. The later joint interaction is separate.'
)
b_next=(
    'Use the actual transported w positive-triple and filled-negative-'
    'node relations to prove uniform normalization of the full partial '
    'source kernel by the three missing cluster directions, or obtain '
    'a genuine full-source obstruction. Seed membership and local '
    'factorizations alone do not suffice. Then address the joint '
    'kernel and B75 uniform finite-cover condition.'
)
for task in ('B.4','B.4.a','B.4.b','B.4.c','B.4.h'):
    add(task,['B.82'],'')
    index[task]['state']=b_current
    index[task]['obstruction']=b_obstruction
    index[task]['next_step']=b_next
index['B.4.c']['state']=(
    'The full product-closedness alternative and required profinite '
    'fixed-point complex remain Open. '+b_current)
assert all(index[t]['outcome']=='Open' for t in ('A.8','B.4','B.4.c','C.2'))
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields)
    writer.writeheader();writer.writerows(rows)

paper=root/'LM4_SUCCESSOR_paper.tex'
s=paper.read_text()
abstract=r'''We study involutions of the full profinite three-cusp group and
the icosahedral centralizer in the full profinite mapping class group.
Both main full decisions remain open.
For the involution problem, actual central compatibility and ordinary
full positive realization do not imply negative involutory realization.
An earlier finite action has compatible involutions at every iterated
actual source-central refinement but obstructs all literal-cusp full
negative lifts, with all factor frames allowed. At infinitely many
eligible fresh primes, a further actual family passes the first central
refinement and has ordinary full positive lifts, yet admits no full
negative involution with any cusp or frame choices. The two tower scopes
remain distinct. We also prove that the actual reflection augmentation
module is projective at every prime and free over the full dyadic group
ring, with rank two in the pure pants case and rank one in the regular
case. In the pure case we prove orientation-twisted projective duality
over every full completed coefficient group ring, including modular
finite heads. The selected incidence maps and nonselfdual blocks still
leave the full marked generation question unresolved.
For the icosahedral problem, faithful configuration comparisons and a
split Birman extension identify an exact completed nonabelian cocycle
condition. Complete marginal pencils and an actual tangent-line bundle
retain the based source. We prove whole filling-kernel intersections,
the exact partial-source operator description, a source-contained
rank-eight free factor, and a complete partial-kernel intersection in
an ordered rank-nine free factor, discretely and after completion.
These intersections do not establish normality of the entire source
deletion kernel; the subsequent joint-source condition also remains
open. A degree-eight cover refutes a general special-source shortcut
with one exceptional retained tangency, without refuting the actual
marginal. The paper retains the published-proof audits, rigid-kernel
and torus results, real-structure reductions, noncompact comparisons,
and corrected five-point census. Every assertion has an explicit proof
status. A gap in a published proof is not a counterexample to its theorem.
This work is incomplete; no priority is claimed.'''
a,b=s.index('\\begin{abstract}'),s.index('\\end{abstract}')
paper.write_text(s[:a]+'\\begin{abstract}\n'+abstract+'\n'+s[b:])
p=root/'LM4_SUCCESSOR_report.md'
s=p.read_text().replace('records/fourteenth_hour_research_report.md',
                        'records/fifteenth_hour_research_report.md',1)
p.write_text(s)
print('Updated49 task rows and abstract with A82-A84, B82; main decisions Open.')
