"""Integrate reviewed thirteenth-hour statements without dropping task rows."""
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
assert formal['A.79']==formal['B.79']=='Proved'
assert formal['B.80']=='Refuted'

def update(task,ids,state=None,obstruction=None,next_step=None):
    row=index[task]
    for sid in ids:
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids']+=';'+sid
    for key,value in [('state',state),('obstruction',obstruction),('next_step',next_step)]:
        if value is not None:
            row[key]=value

a_current=(
    'A75 gives a full positive peripheral realization of the selected integral '
    'tower, but its full negative order and cofinality remain open. A76-A77 '
    'obstruct the original prescribed finite action/frame; A78 changes that '
    'frame and passes its six-cup gate. A79 separately fixes the stored A64 '
    'finite ACTION and excludes every full normalized negative involutory '
    'lift, allowing all frames: every candidate has exact order four on the '
    'actual ordinary sixteen-cup quotient. All iterated actual source-central '
    'refinements nevertheless carry compatible involutory negative data and '
    'norm-one frames, realized by one full ordinary positive lift. The later '
    'reselected W=0 actions are not excluded.'
)
a_obstruction=(
    'No cofinal compatible full negative involution has been constructed, '
    'and no obstruction excludes all surviving finite actions. A79 fixes '
    'one finite ACTION and the literal cusp, although it allows every frame. '
    'Full marked reflection recognition and the global c-invariant Z4 lift '
    'of delta remain unresolved.'
)
a_next=(
    'Resolve a full-order or full-generation implication for the surviving '
    'actions, or prove the required marked profinite reflection recognition. '
    'Do not substitute further passing scalar or noncofinal towers.'
)
prefixes={
    'Lead 3':'The full parity-one involution remains undecided. ',
    'A.4':'The arbitrary dyadic and mixed-level classification remains open. ',
    'A.5':'The full pointed cohomology set and involution conjugacy classes remain undetermined. ',
    'A.6':'The parity of all full involutions in GT0 and GT remains undecided. ',
    'A.8':'The full involution-conjugacy decisions for P, GT0, and GT remain Open. '
}
for task,prefix in prefixes.items():
    update(task,['A.79'],prefix+a_current,a_obstruction,a_next)
update('Lead 2',['A.79'],
    'Ordinary positive central-quotient lifting remains valid. Unrestricted '
    'equivariant/order-preserving variants are false in the specified '
    'counterexamples. A79 now gives an actual finite ACTION whose every '
    'normalized full negative lift has order four on one actual finite '
    'quotient, independently of all frame choices. Every iterated '
    'source-central refinement still has compatible involutory negative '
    'data and norm-one frames. Changing the finite action remains possible; '
    'the universal involution problem is Open.', '',a_next)

b_current=(
    'The faithful configuration and split Birman comparisons retain the '
    'actual completed source and residual centralizer. B78 gives the full '
    'ratio-pencil presentation, including retained-base translates. B79 '
    'gives a second complete presentation of the SAME surface and source: '
    '23 fiber generators, all26 critical lassos, and82 local relation '
    'normal generators over the entire affine line. The actual source '
    'boundary is the five-point product, not the local central element. '
    'After one local elimination, equality of the actual compact deletion '
    'kernel images is equivalent to normalization by three retained '
    'directions. B80 refutes even the proposed general shortcut with only '
    'one exceptional retained tangency, by an actual D8 covering with '
    'source kernel imageC2 and ambient kernel imageV4. It does not refute '
    'the actual marginal, whose internal normal-generation property is '
    'stronger. The actual uniform normality and later joint-source gate '
    'remain Open.'
)
b_obstruction=(
    'The WHOLE actual source deletion kernel must be normalized in the '
    'complete group, not merely its peripheral generators. Internal normal '
    'generation and every nilpotent image already pass. Filling only '
    'vw=1 makes the source generic and proves equality in that enlarged '
    'surface, but the original interaction with that retained divisor '
    'is unresolved. The subsequent joint-source gate remains separate.'
)
b_next=(
    'Prove whole-kernel normality from all26 relations, or give an actual '
    'finite separator retaining the product-one meridian. Use the exact '
    'product-one two-kernel localization or a justified internal-normality '
    'argument; then address the joint interaction kernel and B75 uniform '
    'finite-cover condition. No further affine/metabelian F7 census.'
)
for task in ('B.4','B.4.a','B.4.b','B.4.c','B.4.h'):
    update(task,['B.79','B.80'],b_current,b_obstruction,b_next)
# The original task asks for full product closedness or an appropriate
# fixed-point complex.  Finite-target results do not decide that task.
index['B.4.c']['outcome']='Open'
index['B.4.c']['state']=(
    'The full product-closedness alternative and the required profinite '
    'fixed-point complex remain Open. The earlier Proved coverage label '
    'described proved finite-target reductions and was too broad. '
    +b_current)
assert index['A.8']['outcome']==index['B.4']['outcome']=='Open'
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields)
    writer.writeheader();writer.writerows(rows)

paper=root/'LM4_SUCCESSOR_paper.tex'
s=paper.read_text()
abstract=r'''We study involutions of the full profinite three-cusp group and
the icosahedral centralizer in the full profinite mapping class group.
Both main full decisions remain open.
For the involution problem, selected integral towers admit compatible
actions and frame norms and a full ordinary positive realization.
Their full negative order and cofinality remain unresolved.
We prove a stronger finite obstruction: for one specified finite action,
every full positive peripheral lift fixing the literal cusp has a
negative companion of exact order four on one actual finite quotient,
regardless of all factor-frame choices. All iterated actual source-central
refinements nevertheless admit compatible involutory negative data and
norm-one frames. This disproves the corresponding order-preserving
lifting principle while leaving other finite actions available.
The distinction from earlier prescribed-frame obstructions is explicit.
For the icosahedral problem, faithful configuration comparisons and a
split Birman extension give a nonabelian cocycle whose completed zero
set is the residual centralizer. Two complete based pencil presentations
now retain the actual marginal source. The sum pencil has twenty-three
fiber generators, all twenty-six critical lassos, and eighty-two local
relation normal generators, with no retained base loop omitted.
Its source is a special fiber; its actual boundary product differs from
the local central element. Uniform normality of the entire source
deletion kernel remains the precise unresolved marginal condition.
We refute a proposed general special-source shortcut even when the
source has only one exceptional retained tangency: an explicit
eight-sheeted cover separates its kernel images of orders two and four.
That example does not refute the actual marginal equality, which has
additional internal normal generation. The later joint-source condition
also remains open.
The paper retains the published-proof audits, rigid-kernel and torus
results, real-structure reductions, noncompact comparisons, and
corrected five-point census. Every assertion has an explicit proof
status. A gap in a published proof is not a counterexample to its
theorem. This work is incomplete; no priority is claimed.'''
a,b=s.index('\\begin{abstract}'),s.index('\\end{abstract}')
paper.write_text(s[:a]+'\\begin{abstract}\n'+abstract+'\n'+s[b:])

p=root/'LM4_SUCCESSOR_report.md'
s=p.read_text().replace('records/twelfth_hour_research_report.md',
                        'records/thirteenth_hour_research_report.md',1)
p.write_text(s)
print('Updated49 task rows and abstract with A79, B79, B80; main decisions Open.')
