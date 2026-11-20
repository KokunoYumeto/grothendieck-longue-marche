from pathlib import Path
import argparse
import json

p = argparse.ArgumentParser()
p.add_argument('--utc', required=True)
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
x = json.loads((root / 'review/scan030_findings.json').read_text())
x['scan'] = 30
manifest = json.loads((root / 'review/scan030_crop_manifest.json').read_text())
t = (root / 'review/scan030_draft.tex').read_text()
(root / 'pages/J156-5-04_156-5_scan030.tex').write_text(t)
for c in x['changes']:
    c['crop'] = c.get('crop', '').removeprefix('deliverable/')
    c['main_decision'] = 'Accepted after main-reader inspection of the cited crop. Letter shapes and cancellation extents, not the expected proposition, decide the transcription.'
    i = int(c['id'].split('-')[1])
    if i in (13, 14, 32):
        c['certainty_only'] = False
    if i in (3, 9, 30, 37, 43):
        c['certainty_only'] = c['against_C'] = c['against_H'] = False
        c['review_only'] = True
    if i == 20:
        c['main_decision'] = 'A short heavy strike terminates at B, while the longer shallower strike continues through the following A,A′∈F′. Nested extents are reproduced; the order in which the two strokes were made is not claimed.'
    if i == 31:
        c['main_decision'] = 'The separate C-led terminal line and its stop are real ink. Its compressed joined ending does not securely distinguish Cor. from C6.; retain a marked reading pending the blind pass.'
    if i in (11, 19, 20, 22, 24, 41):
        c['consequential'] = True
    if i in (51, 52):
        c['locus_box'] = c['box']
        c['box'] = manifest['right_note']['box']
for z in x['inventory']:
    z['kind'] = {'page_number': 'text', 'text_block': 'text', 'heading': 'text', 'margin': 'margin note'}.get(z['kind'], z['kind'])
x['notes'] = [
    'The handwritten sheet number is 29. The proposition asserts that multiplication by G preserves refinement, subdivision and the subfigure relation. The starred formula describes F′.G by support containment. The proof undertakes c), using inclusion and closedness; its appeal to “la théorie de F.G” is a stated dependency, not an independently verified premise here.',
    'Part a) was checked conditionally from the stated Inf characterization: F′.G is below F′ and G; when F′≪F, it is therefore a lower bound of F and G, hence below their Inf F.G (030-check-01). This order argument does not establish existence of these figures or prove b), c), C6 or C7₀. It did not change any visible sign.',
    'The main line states “Cor. L’axiome C6 est valable.” The right note qualifies the argument with “Un peu vif” and “mais il faut vérifier encore l’unicité”, with unicité underlined. It then proposes the two displayed order statements, retaining the abandoned implication in b). The left note gives the inverse-image description of the induced G′ and ends with a doubtful short label omitted by both witnesses.',
    'The next main line reads “Vérifions quand même C7₀”, with a small open 0 beside the 7 and no independent final stop. The proposed F′=G′∪(F\\setminus G) is followed by three obligations: that it is a figure, that it subdivides F, and that it induces G′ on G. The word raffine is struck and subdivise is inserted above it. These checks are not completed on this sheet.',
    'The two visible occurrences of que in “Or on sait que (…) que” remain. The phrases le sens de, p.r. à and est le = retain their singular form and abbreviation. Four empty-set glyphs have the long phi stem, separately distinguished from the raised open circles. The live formula at the far right remains doubtful where the scan edge truncates G/L. Two nested cancellation strokes and both right-margin grouping boundaries are reproduced. No date or title sheet occurs.'
]
x['check_events'] = [{
    'statement_id': '030-check-01',
    'type': 'targeted proof check',
    'outcome': 'Conditional order-theoretic proof of a): assume the displayed products are greatest lower bounds for ≪. Then F′.G≪F′≪F and F′.G≪G, so F′.G≪F.G by the greatest-lower-bound property. Existence and the other asserted figure axioms were not checked.'
}]
x['adjudicator'] = 'GPT-6 Astra Pro, main reader, SP114 second pass; effort setting not exposed'
x['adjudicated_utc'] = a.utc
(root / 'review/scan030_adjudicated.json').write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
with (root / 'review/main_image_reviews.tsv').open('a') as f:
    for c in manifest.values():
        f.write('030\t' + c['path'].removeprefix('deliverable/') + '\tmain reader\tinspected before first adjudication\n')
rows = sum(c.get('certainty_only', False) or c.get('against_C') or c.get('against_H') for c in x['changes'])
with (root / 'progress.log').open('a') as f:
    f.write(f"scan 030 done {a.utc}: {x['line_count']} lines read, {len(manifest)} places cropped, {rows} rows\n")
print('Saved scan030, rows', rows)
