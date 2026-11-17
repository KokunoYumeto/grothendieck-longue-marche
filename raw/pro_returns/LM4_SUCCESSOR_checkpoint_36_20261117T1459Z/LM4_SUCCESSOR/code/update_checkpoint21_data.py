"""Integrate the actual free quotient and critical-region fixed-source proof."""
from pathlib import Path
from collections import Counter
import csv, subprocess, sys

root=Path(__file__).resolve().parents[1]
rel='sections/b_free_swap_quotient.tex'
p=root/'sections/part_B.tex';s=p.read_text();line='\\input{'+rel+'}'
assert line not in s
p.write_text(s+line+'\n')
subprocess.run([sys.executable,str(root/'code/assemble_register.py')],check=True)
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==276
assert dict(Counter(r['status'] for r in rows))=={'Known':6,'Proved':232,'Refuted':19,'Open':19}
for sid in ['B.106','B.107']:
    assert next(r for r in rows if r['id']==sid)['status']=='Proved'

p=root/'task_coverage.csv'
with p.open() as f:
    reader=csv.DictReader(f);fields=reader.fieldnames;coverage=list(reader)
assert len(coverage)==49
for row in coverage:
    if row['task'] not in ['B.4','B.4.a','B.4.b','B.4.c','B.4.h']:continue
    assert row['outcome']=='Open'
    for sid in ['B.106','B.107']:
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids']+=';'+sid
    row['state']+=(' B106 gives an actual free double quotient and an equivalence '
      'of the selected fixed-source question, discretely and in full completion. '
      'B107 proves that equality across every actual critical fiber over the '
      'punctured unit disk, by an explicit retracted orbifold amalgam and '
      'cofinal finite-quotient centralizer proof. The global comparison remains Open.')
    row['approaches']+=(' Actual free-swap quotient; exact inverse-Blaschke '
      'separation; invariant two-arc collar; retracted amalgam centralizers '
      'through cofinal finite heads, including all inner critical fibers.')
    row['obstruction']+=(' The two regional results isolate different cone '
      'classes. A common boundary marking must retain the shared free subgroup '
      'and its actual images after both fillings; boundary-fiber injections '
      'and global fixed lifting are not implied by the regional splittings.')
    row['next_step']=('Construct and verify the common inner/outer boundary '
      'marking and both full filling comparisons, retaining the branch pair '
      'and old base. Determine whether the shared free subgroup is detected '
      'by the actual one-family quotient. In parallel, use the finite full '
      'nodal complex and crossed nonlinear action to resolve the Smith edge, '
      'nonlinear defect, compact coefficient comparison and final joint-source '
      'condition. Do not substitute boundary injections or a noncofinal census.')
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(coverage)

p=root/'LM4_SUCCESSOR_paper.tex';s=p.read_text()
old='''full kernel and its additional Tate values remain undetermined. That obstruction,
deeper nonabelian lifting, projected fixed-source equality and the
subsequent joint-source condition remain unresolved.'''
new='''full kernel and its additional Tate values remain undetermined. An actual
free double quotient preserves the selected fixed-source question.
An explicit retracted amalgam proves that equality across all critical
fibers over the punctured unit disk, discretely and in full completion.
The global transfer, deeper nonabelian lifting and subsequent
joint-source condition remain unresolved.'''
assert old in s;p.write_text(s.replace(old,new,1))

p=root/'LM4_SUCCESSOR_report.md';s=p.read_text()
assert s.splitlines()[0]=='INCOMPLETE'
marker='## Twenty-first-hour research: actual quotient and critical-region theorem'
assert marker not in s
s+='''\n## Twenty-first-hour research: actual quotient and critical-region theorem

B106 identifies the actual free coordinate-swap quotient, with no extra
deleted fibers. In invariant coordinates q=vw,s=v+w and projective
t=(s-2)/(s-2q), the selected involution is t to -t. The exact divisor is
t=+-1, qt^2=1 and the eight projective graphs +-T_u(q), including their
poles. The two fixed sources each have ten punctures. The selected one
has the actual nineteen-punctured source as its connected unramified
double cover. A two-coset argument proves equivalence of the selected
fixed-source equality on the original and quotient surfaces, both
discretely and in full profinite completion. The proof requires no
source injection and uses only verified finite-index full topology.

The mixed collision equation factors completely: q=u+r-ur or
q=ur/(u+r-1). All same-sign and branch incidences lie over already
deleted fifth roots. Exact arithmetic in Q(zeta5) independently locates
eighteen physical critical values, nine inside and nine outside the
unit circle, with sixteen quotient nodes in each region. The two
reciprocal pair coincidences are retained, not counted twice. This
is a complete physical-divisor calculation, not a new finite-group
census. The original surface has twice the quotient physical nodes.

B107 proves an actual critical-filling result. The inverse-Blaschke
norm identity places every moving puncture outside |t|=1 when
0<|q|<1. We cut along the unit circle minus the two retained punctures,
using an explicit variable collar that also shrinks at those punctures.
The involution exchanges the two boundary arcs. Orbifold van Kampen
gives (C2 times Z) amalgam_Z R, with an actual boundary section and a
retraction R to Z. Thus its edge maps are proved injective. A cofinal
family of retraction-stable finite normal subgroups reduces every
finite quotient to (C2*K_N) semidirect D_N. Herfort--Ribes' verified
full free-product centralizer theorem then gives the exact completed
centralizer. Neither asphericity nor residual finiteness of R is
assumed. The selected fixed-source equality holds over this whole
inner region, including all its critical fibers, and transfers to
the selected component in the original double cover. Here that source
cover splits into two components, so only the correct intersection
direction is used. The outer mirror isolates the other cone and its
F-sigma lift; it does not decide the selected F-source globally.

Both formal proofs passed complete independent mathematical review.
The retracted-amalgam completion argument also has a separate full
review by A. Root reopened and read the entire applicable primary
Herfort--Ribes B-prime/Lemma3 proof on printed159--160 at this use.
Exact sources, failed initial symbolic attempts, successful programs
and outputs, reviews and proof notes are retained. The register has
276 statements:232 Proved,19 Refuted,19 Open and6 Known; all49 task
and lead rows remain tracked. Both main full decisions remain Open.

The global target is now a common marking for the two regional filling
kernels. The corresponding cone-plus-free factors share a free subgroup;
they are not complementary merely because they isolate different cones.
An actual detector in the one-family quotient might prove the required
injections, but neither that detector nor the global amalgam is yet
established. The finite full nodal complex, Smith edge, nonlinear crossed
action and final joint-source condition remain in the proof ledger.

A separate elementary proof establishes that every square-CW subcomplex
of a product of two countable trees has free fundamental group and is
homotopy equivalent to a graph. Relative leaf-strip collapses give
free-factor inclusions through finite rectangles, so the countable
union argument does not confuse local freeness with freeness. The
actual nodal complex cannot be directly homotopy equivalent to such
a subcomplex because B105 proves its nonzero spherical H2. An actual
group-level comparison would have to account for redundant relations.
This criterion remains a research note, not an extra formal result.

Main A continues at the canonical full completed-group-ring Fox-unit
gate. Abstract realization, pro-p generation and unmarked section-class
counts are not substituted for the actual marked generation statement.
The full current research record is records/twenty_first_hour_research_report.md.
'''
p.write_text(s)
subprocess.run([sys.executable,str(root/'code/update_checkpoint_report.py')],check=True)
print('Integrated B106--B107:276 statements,49 task rows; both main decisions Open.')
