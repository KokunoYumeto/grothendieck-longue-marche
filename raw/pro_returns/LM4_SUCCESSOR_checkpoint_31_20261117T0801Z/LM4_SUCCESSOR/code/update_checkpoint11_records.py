"""Record the accepted eleventh-hour results and their exact limitations."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
p = root / 'work_A/A_results.csv'
with p.open() as stream:
    reader = csv.DictReader(stream)
    fields, rows = reader.fieldnames, list(reader)
for row in rows:
    if row['id'] == 'A.56':
        row['notes'] = (
            'Full positive lift realizes this scalar-stable quotient and '
            'retained literal frames. A76 excludes a full involution for '
            'the original stored finite action and s-frame; later '
            'reselected tuples and cofinality remain Open. Reconstructed '
            'after environment replacement from the reviewed seventh-hour source.'
        )
with p.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

p = root / 'records/root_review_A70_A73_B75.md'
s = p.read_text()
marker = '## A.76: full order obstruction for the original prescribed frame'
text = '''## A.76: full order obstruction for the original prescribed frame

We read the complete formal and working proofs, the original actual
six-cup norm certificate, and CE's independent review and fresh rerun.
The formal proof uses the explicit finite head D0 itself, whose kernel
is already stable under both actions; no characteristic-core replacement
is required. Its order is 2^972 times72 times7^13. Relative perfection
of the A56 source kernel makes the actual central refinement a quotient
of the old tower. Transfer proves that refinement finite: a central
finite-index subgroup of index m has exponent dividing6m, and is
topologically finitely generated. Thus this is an actual finite test.

The H1 inflation isomorphism and injective transgression force every
candidate full positive action retaining the finite datum to preserve
the actual six-cup quotient, with the specified coefficient action.
The complete44-dimensional cocycle space and the joint boundary
restriction reduce all possible positive action changes to cusp-fixed
inner changes. They do not alter the norm. The remaining frame changes
are exhausted by the norm image from the s-fixed coefficient module.
Evaluation at weight23 annihilates that image; the six stored values
are(0,0,5,0,5,5). The cup03 value therefore cannot vanish.

For a full involution hc fixing the literal cusp, the square of the
normalized s-reflection lies in <s>. Its trivial S3 image forces that
square to be one, contradicting the forced finite norm invariant.
The ordinary full positive framed lift nevertheless exists. This is
an actual failure of prescribed-frame global-negative order preservation,
not only an intertwining obstruction or a failed search. Literal tau
normalization and the original finite action/frame remain explicit.
No arbitrary outer normalization is invoked. Later reselected A64/A66/A75
tuples are outside the conclusion; the main conjugacy problem stays Open.

The A56 statement and register notes now point forward to this result.
Historical checkpoint versions retain the earlier unresolved wording.
The current all-frame research is separate: at each of four Tate weights,
29 of4096 local frame values pass, but their compatibility with the full
old class and norm equations has not been inferred from that count.
'''
if marker not in s:
    p.write_text(s + '\n' + text)

p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '## Work since the tenth checkpoint'
text = '''## Work since the tenth checkpoint

Both main full decisions remain Open. The complete register now has236
numbered statements:197 Proved,14 Refuted,19 Open,6 Known, with91
bibliography entries and all49 task/lead rows. A70-A76 and B75 are the
new formal statements; all eight have complete proofs in the paper.

For the involution construction, A72 adds all32 actual mixed ordinary
cups, including a repair of the nonzero initial negative square in one
half. A73 determines576 new scalar directions,704 in total, and proves
that the next scalar refinement is relatively perfect, with the entire
integral tower retained. A75 solves the actual action and frame equations
by a2631-variable rank890 system. The failed restricted system is saved.
The original704 law, independent full20 law and earlier all-free128 law
verify the selected witness and its projections. Six exact constraints
preserve the forced integral halves. A full positive peripheral lift
realizes these data; its full negative square and cofinality are Open.

A76 now excludes the ORIGINAL stored A56 finite action and s-frame from
every full normalized negative involution. The actual finite source-central
refinement and both quotient normalizer norms nevertheless pass. Natural
transgression forces every candidate to descend to the actual six-cup
quotient, where the complete norm calculation has a nonzero invariant.
The obstruction concerns the globally negative multiplier, retaining the
specified frame and literal cusp normalization. It does not exclude
reselected frames or decide either full conjugacy question. A56's current
statement and register have been updated; earlier versions are preserved.

A70 gives a complete13824-element actual source-central counterexample
to unrestricted equivariant peripheral lifting with mixed multipliers.
A74 gives a separate binary-icosahedral prescribed-frame counterexample
on the entire orientation-central quotient, with multiplier one and norm
one. Neither is promoted to a freely framed negative-cocycle obstruction.
A71 supplies the classical three-trace argument on every finite local
coefficient ring with absolutely irreducible residue, and proves the
compatible inverse-limit conclusion. Its relevant primary source was
opened at the theorem; the original Macbeath article was not read.

For the icosahedral problem, B75 identifies the exact completed zero set
of a split four-moving-point Birman cocycle with the residual centralizer.
The actual index-five source, kernel topology, section, deck comparison,
and both directions of the identification are proved. Its remaining
condition is uniform characteristic finite-cover separation. Discrete
injectivity does not establish it. The text credits the prior abstract
interaction-cocycle solution in attached LM4 F14-F15.

The positive marginal braid source has been reconstructed directly:
19 lassos,95 path segments,872 exact crossings,8 fiber words and11
invertible actions. These are actual source words. The retained F3
action is outer for three base generators, contrary to an initial
all-inner assumption; the failed assumption and exact correction are
preserved. The current geometric approach uses a ratio pencil on the
ordered double cover. Its special tangent fiber and the other double
and triple collisions are kept explicit; generic-fiber surjectivity
and source normality have not been assumed. Bounded finite-cover tests
and partial Stallings computations are research evidence only.

The attached LM4 comparison now extends through F33. In particular its
full affine character-locus calculations are prior work, and no new
affine test is presented as deciding the completed source intersection.
A separate Leary-Nucinkis/Bestvina-Brady route was closed positively for
standard admissible graph actions: prime-power centralizers are standard
RAAG parabolics, and their commuting retractions give the finite-group
centralizer equality. Those examples do not refute the published claim.

All new proof reviews, failed attempts, executable programs, genuine
outputs, source-reading records and earlier checkpoint versions are
retained. The final PDF metrics and visual inspection are recorded
separately below and in records/checkpoint11_typesetting.txt.
'''
if marker not in s:
    p.write_text(s + '\n' + text)
print('Recorded A76 review, corrected A56 register note, and post-checkpoint10 work.')
