"""Integrate the fully reviewed annular and actual-neck comparisons."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
copies = [
    ('work_A/B112_annular_centralizer.tex', 'sections/b_annular_centralizer.tex'),
    ('work_A/B114_annular_neck_comparison.tex', 'sections/b_annular_neck_comparison.tex'),
]
records = []
for source, target in copies:
    src, dst = root/source, root/target
    assert src.exists() and not dst.exists(), (source, target)
    dst.write_bytes(src.read_bytes())
    records.append({'source': source, 'integrated': target,
                    'sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
                    'comparison': 'Byte-identical complete reviewed component.'})
(root/'records/checkpoint23_formal_source_copies.json').write_text(
    json.dumps({'integrated_at': datetime.now(timezone.utc).isoformat(), 'copies': records}, indent=2)+'\n')

p = root/'sections/part_B.tex'
s = p.read_text()
for name in ('b_annular_centralizer.tex', 'b_whole_annular_regions.tex',
             'b_annular_neck_comparison.tex'):
    line = '\\input{sections/'+name+'}'
    assert line not in s
    s += line+'\n'
p.write_text(s)
subprocess.run([sys.executable, str(root/'code/assemble_register.py')], check=True)
rows = list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 283
assert dict(Counter(r['status'] for r in rows)) == {
    'Known': 6, 'Proved': 239, 'Refuted': 19, 'Open': 19}

p = root/'task_coverage.csv'
with p.open() as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    coverage = list(reader)
assert len(coverage) == 49
for row in coverage:
    if row['task'] not in ('B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'):
        continue
    assert row['outcome'] == 'Open'
    for sid in ('B.112', 'B.113', 'B.114'):
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids'] += ';'+sid
    row['state'] += (
        ' B112 determines the complete actual annular bad-vertex presentation '
        'and its discrete and full profinite cone centralizer as the actual '
        'free-five source times C2. Its exact even-period graph quotients are '
        'cofinal for arbitrary finite targets. B113 transfers both cone '
        'comparisons to the whole inner and outer regions and proves the '
        'selected original outer source equality with its connected free-nine '
        'source cover. B114 proves actual ordinary annular neck retractions '
        'and proper full completion of the abstract bad-vertex amalgam. The '
        'actual annular one-neck group is its quotient by two independent '
        'based cross commutators, each detected by a prescribed S3 quotient '
        'killing the other. The actual source is abstractly free-six and its '
        'connected original cover free-eleven; no source injection or '
        'centralizer equality for this final quotient is asserted.')
    row['approaches'] += (
        ' Complete simultaneous annular relation reduction; exact infinite '
        'and finite even-period graph presentations; actual triangular source '
        'basis and whole ordinary detector; cofinal all-module prime-order '
        'centralizer comparisons; fully invariant edge kernels; categorical '
        'two-annulus pushout with corrected lifted collar paths; two explicit '
        'independent S3 cross-relator detectors.')
    row['obstruction'] = row['obstruction'].replace(
        'The two regional results isolate different cone classes.',
        'Both cone classes in each complete region are now determined by B113.')
    row['obstruction'] = row['obstruction'].replace(
        'The first-neck vertex centralizer is computed on the simply connected slit; '
        'its annular analogue remains unevaluated.',
        'Both slit and complete annular bad-vertex centralizers are computed; '
        'the actual two-relator annular neck quotient remains unevaluated.')
    row['obstruction'] = row['obstruction'].replace(
        'Neither the full annular saturation nor the other-neck quotient-edge '
        'comparisons have been determined.',
        'The full annular saturation is determined by B112. The effect of both '
        'actual cross commutators on the one-neck centralizer, and the '
        'other-neck quotient-edge comparisons, remain undetermined.')
    row['next_step'] = (
        'Determine the centralizer/source IMAGE in the actual two-cross-relator '
        'annular neck quotient, using the corrected selected cone and the '
        'literal mirror automorphism. Test an exact signed-graph unfolding '
        'or mirror-fold presentation, allowing relations in the abstract '
        'source image. Then compare the other four necks and the global '
        'selected source. Retain the separate nonlinear, coefficient and '
        'final joint-source gates.')
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(coverage)

p = root/'LM4_SUCCESSOR_paper.tex'
s = p.read_text()
old = '''The annular comparison, remaining necks, global transfer, deeper
nonabelian lifting and subsequent joint-source condition remain unresolved.'''
new = '''Restoring that loop gives an exact annular graph presentation whose
cone centralizer is the actual free-five source, also in full completion.
Exact finite even-period quotients supply the cofinal comparison. Both
fixed sources in each whole annular region are thereby determined; the
selected original outer cover has free-nine fixed source. The complete
annular one-neck group is a quotient of a proper bad-vertex amalgam by
two independent nontrivial cross commutators, with actual base loops
and lifted connectors retained. Its source image, the remaining necks,
global transfer, deeper nonabelian lifting and subsequent joint-source
condition remain unresolved.'''
assert old in s
p.write_text(s.replace(old, new, 1))

p = root/'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert s.splitlines()[0] == 'INCOMPLETE'
marker = '### Complete annular centralizers and the actual two-relation neck quotient'
assert marker not in s
s += '\n'+marker+'''

B112 completes the annular bad-region calculation left open in the
preceding checkpoint. It retains the actual zero loop and all ten
simultaneous critical relations. An exact change of the six-meridian
basis identifies the geometric source lift h and the far-section lift
k=f^-1 h. Reversible transformations give a fourteen-vertex,
thirty-two-edge graph-group HNN presentation. Its cone-bearing edge
groups are handled by an exact infinite graph unfolding; no unproved
profinite HNN properness statement is used.

The cone-fixed graph subgroup is freely generated by four diagonal
products at every integer level. Its shift extension is free on the
four level-zero products and h. The five ACTUAL geometric source loops
are a printed triangular free basis of this group. They were independently
reconstructed from the positive Artin actions, and a second direct
infinite-graph evaluator checks the complete literal source identities.
The ordinary detector satisfies all twenty node relations and all ten
mapping equations in both directions. It retracts onto the source and
proves its full induced topology.

For each even period m>=4, the exact quotient by h^m is a finite graph
group extended by C_m times C2. Every finite quotient of the actual
annular group factors through one such head. The graph groups need not
be bipartite; their finite classifying spaces, residual finiteness,
finite virtual cohomological TYPE and all-discrete-module goodness are
verified with the actual hypotheses. The checked prime-order element
centralizer theorem gives each completed head centralizer. Compact
separation over these cofinal heads proves the actual full completed
centralizer is the source completion times C2.

B113 transfers this result through the actual retracted whole-region
amalgam. It proves the fixed-source comparison for both cones in both
complete regions: ranks1 and5 in the inner region, ranks5 and1 in the
outer region. The comparison uses finite amalgam heads with even edge
groups and retained odd cones; it does not assume residual finiteness
of the original bad region. For the selected outer source, the original
cover adjoins sqrt(1-q). Its monodromy along the q-circle of radius4
is nontrivial. The selected source cover is connected of rank9, and
intersection with the actual open index-two ambient subgroup proves
the ordinary and full profinite source equalities in the required
direction. The point (1+i sqrt3,1-i sqrt3) fixes the original based lift.

B114 identifies the correct annular neck comparison. The literal disk
subgroup has the free basis (a,bar b,d,e,f), detected by the complete
ordinary annular retraction. The opposite-cone retraction is nonzero
on the branch generator. Cofinal FULLY INVARIANT finite-index kernels
nevertheless give compatible exact edge kernels in both vertices.
Thus the abstract bad-vertex amalgam has its proper full completion
and its vertex cone-centralizer reduction.

The actual two-annulus group adds two relations: the opposite cone
commutes with the corresponding retained boundary-section loop.
Categorical elimination gives the precise quotient by both based
cross commutators, with closed normal closure after completion. Each
relator is nontrivial even modulo the other: two explicitly checked
maps to S3 send the selected relator to a3-cycle and kill the other.
They arise from the actual base-winding and orientation characters,
not an enumeration. Thus the two genuine kernel witnesses survive
in the full prequotient completion. A projection to the free-two base
also separates the inner source loop from the entire outer vertex
image, discretely and compactly. No centralizer formula for the final
quotient follows merely from the proper prequotient amalgam.

The source over this one-neck base is abstractly F6 and its connected
original cover is F11. These are source topology counts. We expressly
retain the possibility of a kernel in the source's ambient image
after gluing; neither equal ranks nor a proposed free normal form is
substituted for that comparison.

A genuine connector correction was made during independent review.
The first lower y-arc cone calculation had a correct cut word, but
its principal square-root lift ends at t=+i rather than the selected
gap t=-i. The failed selected-lift comparison is preserved. The
corrected upper collar crosses the positive ray at radius less than1,
avoids retained y=1, and ends at z=+i,t=-i. Its exact cone word is
x1 x2 x1^-1=a C a^-1. The full bad-fiber boundary preserves the actual
far loop, so the consistently transported section remains g0. Both
the old valid alternative-gauge calculation and the corrected complete
comparison remain available with their genuine certificates and reviews.

The fresh literature check considered orbit-configuration results of
Maassarani(2021), DOI10.1016/j.topol.2021.107847, and Roushon(2026),
DOI10.1007/s40879-026-00912-6. Their primary action hypotheses were
opened, not assumed. The direct coordinate identification fails:
two actual forbidden Mobius maps u/v and1-u+u/v compose to the
nonidentity translation v+1-u. The exact point (10,11-u) lies in
the actual surface but on that composed orbit graph. The retained
cyclotomic calculation checks every excluded factor. No theorem from
those papers is applied to this surface, and no arbitrary alternative
model is ruled out. The reading scope is in records/primary_readings23.md.

The formal baseline is283 statements:239 Proved,19 Refuted,19 Open
and6 Known, with111 verified-status bibliography entries and49 task/lead
rows. Both main full decisions remain Open. The next actual gate is
the source image and cone centralizer after both annular cross
commutators, followed by the other four necks, the global selected
source and the separate final joint-source comparison. Main A's full
involution conjugacy and its actual Fox-unit/third-cusp gates remain
Open; the bounded V4--Heisenberg coefficient attempt is not restarted.
'''
p.write_text(s)
subprocess.run([sys.executable, str(root/'code/update_checkpoint_report.py')], check=True)
print('Integrated B112--B114:283 statements,111 bibliography records,49 task rows; both main decisions Open.')
