"""Primary reader's final prose and explicit check-event reconciliation."""
from pathlib import Path
import csv
from workflow import WORK, PREFIX, now, log
from report_helpers import rebuild_reports


def replace_observation(filename, marker, prose):
    path = WORK / filename
    text = path.read_text()
    start = f'<!-- BEGIN {marker} -->'
    end = f'<!-- END {marker} -->'
    assert text.count(start) == text.count(end) == 1
    a = text.index(start) + len(start)
    b = text.index(end)
    path.write_text(text[:a] + '\n' + prose.strip() + '\n' + text[b:])


replace_observation(f'{PREFIX}_doubts.md', 'FINAL LEGIBILITY OBSERVATIONS', r'''
The primary reader completed both visual readings of all 25 pages in the prescribed order. The live manuscript is mostly readable in the supplied full-resolution halves; the typed leaves and short covers are generally clearer. Confidence drops in densely overwritten indices, slanting marginal additions, and cancellation layers. The retained uncertainty concerns visible traces: the two blacked-out word groups on 16/010 and the short physically obscured word on 16/005 remain illegible; the crowded cancelled hypothesis on 16/006, the two-level cancelled sums on 16/012, old indices on 16/015, and the crossed margin and lower fragment on 16/016 remain among the least secure readings. The clipped induction crop on 16/008 and clipped cancelled alpha crop on 16/013 are explicitly limited in the notes; their readings retain doubt.

Every one of C's 288 uncertainty macros was reviewed: its 151 live marks are accounted for, in the supplied order, in `decisions.tsv`, and its 137 struck-text marks in `cancelled_doubt_review.tsv` and the table below. The final pages retain 114 uncertainty macros, represented by 111 place entries in `remaining_doubts.tsv`; a place may contain more than one marked fragment. The 59 entries in `certainty_only.tsv` record additional resolutions or adjustments to alternatives. These registers overlap in purpose and must not be added to obtain a count of distinct places.

C supplied a substantially more complete diplomatic starting text across these pages. Its remaining substantive differences include small words and abbreviations, the duplicated old expression and reused equality on 16/015, and many omitted graphic attachment strokes. H is available on 19 pages. Its 501 recorded differences include omitted readable cancelled text, expanded abbreviations, changed indices, and altered insertion or deletion states. The corresponding C count is 97 across 25 pages; 77 registered places affect both witnesses, yielding 521 places in the combined changes register. These are counts of recorded places with different coverage, not estimates of either witness's error rate. Certainty-only adjustments do not enter these totals. Agreement of C and H was checked against the image throughout and supplied no independent evidence for a reading.

The second visual reading especially recovered long or curved leaders connecting interlinear additions to the baseline. Their shapes and attachment positions are now represented in TikZ, with inventory and change rows. Mathematical discrepancies remain written in the transcription, including the minus in 16/004, the complement indices in 16/005, global-looking identities on 16/011–013, the integral claims on 16/014, the basis bound on 16/015, and the cancelled shift index on 16/016. The accompanying notes give the exact checks and concrete counterexamples used during reading. No external text, OCR, or TeX compilation was used.
''')

replace_observation(f'{PREFIX}_sheet_feedback.md', 'FINAL LEGIBILITY AND PATTERN OBSERVATIONS', r'''
The counts above use all ten requested error kinds and count a place once in the union even when both witnesses differ. H has a transcription for 19 of the 25 pages. Certainty-only resolutions and narrowed or reordered alternatives have their own register. The 97 substantive C changes comprise 38 drawing/diagram changes and 59 changes in the other nine categories; the graphical count chiefly records visible boundaries, leaders, and related strokes that the starting text omitted. Counting those omissions separately exposes a feature that a word-only comparison would miss.

### Additional recurring patterns to carry into the next run

| Pattern | Places and observed consequence |
|---|---|
| A surviving sign is reused by a later revision layer | On 16/015 the marginal equality survives the cancelled old left member and serves the replacement product above it. The crossed beta-minus-alpha belongs to the lower old L, although it sits directly beneath a newer condition. C duplicated these components. Track one physical occurrence through the revision layers before counting expressions. |
| A replaced noun leaves the older agreement intact | The changes from algèbre to anneau on 16/003, 16/004, and 16/015 leave feminine wording in the ink. Record both the replacement and the surviving ending; the revision history explains the resulting grammar. |
| Long attachment leaders cross unrelated live material | Examples recur on 15/183, 185, 187, 193 and 16/003–008, 010, 016. The leader's route and its attachment must be recorded as well as the inserted words. Several were absent from both witnesses even when they had the words. On 16/007 H also treats the live et supposons under the leader as deleted. |
| Reused leaves carry an independent pagination and orientation | The reused typed leaves 15/192 and 15/194 have their own page sequence; the intervening manuscript belongs to the folder's notes. Their physical scan order is retained, with each sheet's orientation and pagination recorded in the notes. |
| A component identity is copied with the total identity symbol | The written 1 in 16/011–013 requires attention to the stated domain. The notes give the restriction homomorphism to End(M^i), explicit counterexamples on the total module, and the projector factor in the checked refined identity. This is a prompt to inspect every written 1 and index, with the source symbol retained. |
| Old and new notations coexist within the same argument | On 16/014–016 the small zero attached to an outlined letter can be absent, clear, or obscured by its foot. On 16/016 both transferred Lambda primes are visible. Each occurrence keeps its own ink-supported reading and doubt, while the notation register records the correspondence of the surrounding formulas. |

The strongest residual uncertainty is concentrated in cancellation layers and compressed margins. Two blacked-out groups on 16/010 and the obscured word on 16/005 remain illegible. On 16/016 the crossing strokes through the slanted conditions leave their live/deleted status doubtful, so the text, strokes, and uncertainty are all retained. These limitations are carried into the in-place marks, remaining-doubts table, and hand log.
''')

hand = WORK / f'{PREFIX}_hand_log.md'
assert '## Cross-page audit after the second reading' not in hand.read_text()
with hand.open('a') as f:
    f.write(r'''

## Cross-page audit after the second reading

All 25 pages were visually audited after the last first-reading completion. This comparison consolidates the local observations above; its scope is the occurrences explicitly listed here.

| Recurrence | Cross-page result and scope |
|---|---|
| ζ on 15/183, 185, 187; ξ on 15/191, 193 and 16/014 | The upper turn and long descending return of the torsion label recur as ζ on 183–187. The fibre notation on 191/193 has the multi-turn ξ shape, and the exterior-form notation on 014 is read ξ in its local definitions. C and H both gave ξ for the ζ occurrences on 185. The named occurrences were compared; the mathematical objects and their definitions are separately stated on their pages. |
| Centre sign on 16/005–006 | The curled upper stroke and long lower foot recur through the six live occurrences on 006 and the occurrence on 005. The transcription consistently uses the large gothic-style Z there. H uses a small gothic z. The alphabet judgment remains medium-confidence where already recorded. |
| ν, i, j, α in 16/003–005 and 011–013 | The grading parameter, dotted i, descending j, and looped alpha were checked in their formulas. Clear written index changes and missing primes survive in the transcription, with the exact degree or operator calculation in the notes. Overtracing that still obscures a glyph retains its local doubt. |
| v, u, w on 16/006–008 | The rounded v and returning u stroke were checked in the paired maps and corner products. The first overwritten v on 006 still admits u; later clearer forms do not erase that local uncertainty. The two-dip w recurs in the inverse maps. |
| Λ and L feet, zero indices and primes on 16/010–016 | The component maps and the exterior construction supply the local notation, while the ink determines each exponent, zero and prime. The final L foot on 014 and first bold Lambda foot on 016 remain doubtful. Both raised Lambda primes in the transported identities on 016 are retained. |
| Abbreviations and attachment strokes | The page-specific gp and gpe forms, equality sign for même, raised endings, and full or abbreviated isom forms remain as written. Long leaders were traced to their attachments during the second reading, including those running across live text. Their local paths determine the graphical transcription and deletion state. |
''')

notes = WORK / f'{PREFIX}_notes.md'
text = notes.read_text().lstrip('\n')
assert not text.startswith('# Notes')
notes.write_text('# Notes on the 25 scanned pages\n\n'
    'These notes were made by the primary reader during the two visual readings. '
    'They record the page content, local reading evidence, and the explicit mathematical checks. '
    'Statement identifiers link to `CHECK_EVENTS.tsv`; computations use only the supplied pages '
    'and the concrete algebraic examples stated here. The transcription retains the written formulas.\n\n' + text)

events = WORK / 'CHECK_EVENTS.tsv'
with events.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
new = {
    'N16-013-R1': 'Rechecked the component maps of N16-013-P1: each output has input degree minus 2; on the displayed n=1 chain the only nonzero block is Hom(M^2,M^0). This verifies the stated degree -2 refinement.',
    'N16-013-R3': 'Rechecked the earlier written range i<=n-1 with alpha>=0: n-i+alpha-1>=0. At n=i=1, alpha=0 the later alpha-only range admits exponent -1. This is the exact range comparison in the note.',
    'N16-014-R2': 'Rechecked the specified rational chain (1,xi,v): C sends it to (0,2,xi), B to (0,1,xi/2), so C=2B on that span, including the bottom vector.',
    'N16-015-R2': 'Rechecked the specified chain projections: LP sends 1 to xi, Q retains xi, and C sends xi to 2. All other inputs are killed by P. Hence CQLP=2P, while BQLP=P.',
    'N16-016-R2': 'Rechecked on the stated rational chain C=2B, whence C^2L^2=4B^2L^2 and L^2C^2=4L^2B^2. Directly B^2L^2 pi_0=pi_0 and L^2B^2 pi_4=pi_4, as written in the refinement.',
}
assert not set(new) & {r['statement_id'] for r in rows}
for identifier, outcome in new.items():
    rows.append(dict(zip(fields, [identifier, now().split()[0], rows[0]['who'], 'targeted proof check', outcome])))
with events.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

rebuild_reports(WORK)
log(f'final observations completed {now()}: legibility, witness coverage, ten-kind counts, additional recurring patterns, cross-page hand/notation audit, and five explicit refined-statement check events reconciled; no page reading changed')
print('Final prose completed; five check-event records added; generated reports refreshed.')
