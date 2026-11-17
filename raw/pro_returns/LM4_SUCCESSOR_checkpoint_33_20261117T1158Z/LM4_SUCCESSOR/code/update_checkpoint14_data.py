"""Integrate reviewed fourteenth-hour statements and retain all49 task rows."""
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
assert all(formal[sid]=='Proved' for sid in ('A.80','A.81','B.81'))

def update(task,ids,state=None,obstruction=None,next_step=None):
    row=index[task]
    for sid in ids:
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids']+=';'+sid
    for key,value in [('state',state),('obstruction',obstruction),('next_step',next_step)]:
        if value is not None:
            row[key]=value

a_current=(
    'A75 realizes the selected integral tower by a full ordinary positive '
    'action; its full negative order and cofinality remain open. A76-A78 '
    'distinguish prescribed-frame obstructions from successful frame '
    'reselection. A79 fixes one finite ACTION and excludes every literal-cusp '
    'full negative involution with all frames allowed, despite compatible '
    'involutions at all iterated actual source-central refinements and a '
    'full ordinary positive realization. A80 uses the actual odd relation '
    'module to remove the full cusp-normalization restriction. A81 constructs '
    'such actions at infinitely many eligible fresh primes which pass the '
    'actual FIRST central refinement and admit an ordinary full positive '
    'lift, yet no full negative involution induces them with ANY cusp or '
    'frame choices. No all-iterated claim is made for A81. The later W=0 '
    'finite actions and universal involution decisions remain open.'
)
a_obstruction=(
    'The new unrestricted nonrealization theorem excludes a constructed '
    'family, not every surviving finite action. No cofinal compatible full '
    'negative involution, universal conjugacy proof, or full marked '
    'reflection-recognition theorem has been obtained. The full global '
    'c-invariant Z4 lift of delta remains unresolved.'
)
a_next=(
    'Resolve full order or full generation for the surviving actions, or '
    'prove the missing marked full-profinite reflection recognition. '
    'Do not infer existence from further passing central or noncofinal '
    'towers, and do not assume an odd quotient kernel gives an odd '
    'automorphism kernel.'
)
prefixes={
    'Lead 3':'The full parity-one involution remains undecided. ',
    'A.4':'The arbitrary dyadic and mixed-level classification remains open. ',
    'A.5':'The full pointed cohomology set and conjugacy classes remain undetermined. ',
    'A.6':'The parity of all full involutions in GT0 and GT remains undecided. ',
    'A.8':'The full involution-conjugacy decisions for P, GT0, and GT remain Open. '
}
for task,prefix in prefixes.items():
    update(task,['A.80','A.81'],prefix+a_current,a_obstruction,a_next)
update('Lead 2',['A.80','A.81'],
    'Ordinary positive central-quotient lifting is valid. The corresponding '
    'unrestricted order-preserving lifting assertion is false: A81 gives '
    'actual finite actions with an involution on their actual first '
    'source-central refinement and an ordinary full positive realization, '
    'but no full negative involutory realization even with arbitrary cusp '
    'and frame choices. A79 separately retains its all-iterated central '
    'compatibility for the earlier finite action. These scoped '
    'counterexamples do not decide the universal involution problem.',
    '',a_next)

b_current=(
    'The faithful configuration and split Birman comparisons retain the '
    'actual completed source and residual centralizer. B78-B79 give two '
    'complete pencil presentations of the same marginal; B80 refutes a '
    'general one-tangency shortcut, not that marginal. B81 gives an actual '
    'double-cover comparison to the smaller tangent-line bundle '
    'F7 semidirect F6, with all six based automorphisms and four source '
    'words. It proves exact full filling-kernel intersections in two '
    'rank-five free factors and two tangency rank-two factors, discretely '
    'and after completion. The whole source image is not yet proved '
    'normal. A restricted moving-family orbit subgroup has a verified '
    'D8 obstruction, but the actual omitted even-source action destroys '
    'that separator. The full marginal and later joint-source gates '
    'remain Open.'
)
b_obstruction=(
    'Normality is required for the WHOLE actual source deletion-kernel '
    'image, not only its seed meridians or its proved free-factor '
    'intersections. Ordered moving-family analysis must include eleven '
    'even base generators and four actual opposite-family source inner '
    'actions. The smaller restricted-orbit obstruction does not separate '
    'the full source. The subsequent joint interaction remains separate.'
)
b_next=(
    'Analyze the full actual ordered-family orbit subgroup including all '
    'even base actions and opposite-family source conjugations; prove '
    'whole-kernel normality or find a genuine full-source separator. '
    'Retain the product-one meridian, whose filling already gives '
    'equality. Then address the joint kernel and B75 uniform finite-cover '
    'condition. No further affine/metabelian F7 census.'
)
for task in ('B.4','B.4.a','B.4.b','B.4.c','B.4.h'):
    update(task,['B.81'],b_current,b_obstruction,b_next)
index['B.4.c']['state']=(
    'The full product-closedness alternative and required profinite '
    'fixed-point complex remain Open; the earlier correction from a '
    'too-broad coverage label is retained. '+b_current)
assert all(index[t]['outcome']=='Open' for t in ('A.8','B.4','B.4.c'))
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields)
    writer.writeheader();writer.writerows(rows)

paper=root/'LM4_SUCCESSOR_paper.tex'
s=paper.read_text()
abstract=r'''We study involutions of the full profinite three-cusp group and
the icosahedral centralizer in the full profinite mapping class group.
Both main full decisions remain open.
For the involution problem, we prove that actual central compatibility
and ordinary full positive realization do not imply an involutory
negative realization. An earlier specified finite action has compatible
involutions at every iterated actual source-central refinement but
obstructs every full negative lift fixing the literal cusp, with all
factor frames allowed. We now use actual odd relation modules and
anti-symplectic compact-surface homology to construct, at infinitely
many eligible fresh primes, finite actions which pass the first actual
central refinement and have ordinary full positive lifts, but admit no
full negative involution even with arbitrary cusp and frame choices.
We do not assert all-iterated compatibility for this new family or
exclude the other surviving finite actions. No particular fresh prime
or enormous coefficient matrix is claimed to have been computed.
For the icosahedral problem, faithful configuration comparisons and a
split Birman extension identify the residual centralizer with an exact
completed nonabelian cocycle zero set. Two complete pencil presentations
retain the actual marginal source. A further actual covering comparison
reduces it to a tangent-line bundle with group $F_7\rtimes F_6$ and
fully based source words. We prove full filling-kernel intersections
in two rank-five free factors and two tangency rank-two factors, both
discretely and after completion. Normality of the entire source
deletion-kernel image remains unresolved. An explicit degree-eight
cover refutes a proposed general special-source shortcut with one
exceptional retained tangency, but does not refute this actual marginal.
The subsequent joint-source condition also remains open.
The paper retains the published-proof audits, rigid-kernel and torus
results, real-structure reductions, noncompact comparisons, and
corrected five-point census. Every assertion has an explicit proof
status. A gap in a published proof is not a counterexample to its
theorem. This work is incomplete; no priority is claimed.'''
a,b=s.index('\\begin{abstract}'),s.index('\\end{abstract}')
paper.write_text(s[:a]+'\\begin{abstract}\n'+abstract+'\n'+s[b:])
p=root/'LM4_SUCCESSOR_report.md'
s=p.read_text().replace('records/thirteenth_hour_research_report.md',
                        'records/fourteenth_hour_research_report.md',1)
p.write_text(s)
print('Updated49 task rows and abstract with A80, A81, B81; main decisions Open.')
