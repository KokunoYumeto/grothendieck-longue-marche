from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
x = json.loads((root / 'review/scan029_findings.json').read_text())
t = (root / 'review/scan029_draft.tex').read_text()
(root / 'pages/J156-5-04_156-5_scan029.tex').write_text(t)
for c in x['changes']:
    c['crop'] = c.get('crop', '').removeprefix('deliverable/')
    c['main_decision'] = 'Accepted after main-reader inspection of the cited crop; obscured letters remain marked rather than supplied from the sense.'
    i = int(c['id'].split('-')[1])
    if i in (12, 22):
        c['certainty_only'] = False
    if i == 27:
        c['against_C'] = c['against_H'] = c['certainty_only'] = False
        c['macro_only'] = True
        c['main_decision'] = 'H explicitly describes the whole proposition as crossed out in its editorial note. Encoding that same physical state by deleted is not counted as a substantive discrepancy.'
    if i == 28:
        c['main_decision'] = 'The first subdivision sign has a tall retraced loop above its upper arm and the normal bowed lower bar. No independently bounded earlier glyph can be separated from that retracing; do not invent a deleted item.'
    if i == 32:
        c['main_decision'] = 'The first letter is the short bent s also seen in the preceding sur; its apparent long descender is continuous with the oblique page cancellation. The following u shoulder and low r are visible.'
    if i == 10:
        c['main_decision'] = 'Initial dotted i, a medial tall t-like stroke and the short terminal r with a dark stop favour inter. The strike prevents certainty; intersection remains an alternative.'
    if i in (9, 14, 15, 22, 28):
        c['consequential'] = True
for z in x['inventory']:
    z['kind'] = {'page_number': 'text', 'text_block': 'text', 'heading': 'text', 'margin': 'margin note'}.get(z['kind'], z['kind'])
x['notes'] = [
    'The handwritten sheet number is 28. The page names the constructed Inf for the refinement relation the “figure intersection” F.G. It distinguishes that construction from the set intersection F∩G in general, says they coincide for compatible figures, and asserts an arbitrary-family version with support equal to the intersection of supports. These assertions are transcribed, not independently proved here.',
    'The underlined word after “propriété de” is modération: the initial m, o, looped d, accented following letter and terminal -tion are visible. H’s demi-treillis is not supported by those letters. The preceding s’/l’apparente and the cancelled phrase remain doubtful. No mathematical expectation was used to settle either.',
    'The cancelled footer states that F′≼F entails F′.G≼F.G and adds “(Immédiat sur supports) : Subdivision induite sur un raffinement.” Its assertion of immediacy is the author’s, not a completed check in this run. The entire footer and its smaller nested cancellation are preserved. H already describes the broad cancellation in an editorial note, so conversion of that description into the edition’s deleted macro is excluded from substantive counts.',
    'The compatibility sentence visibly omits sont; none is supplied. The insertion en général has a curved guide above the live la figure, not a strike through those words. The first footer relation has retracing but no separately recoverable cancelled sign. No title, date, explicit question or verbal reservation occurs on this sheet.'
]
x['check_events'] = []
x['adjudicator'] = 'GPT-6 Astra Pro, main reader, SP114 second pass; effort setting not exposed'
x['adjudicated_utc'] = '2026-11-20 18:50:00 UTC'
(root / 'review/scan029_adjudicated.json').write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
with (root / 'review/main_image_reviews.tsv').open('a') as f:
    for c in x['crop_manifest']:
        f.write('029\t' + c['path'].removeprefix('deliverable/') + '\tmain reader\tinspected before first adjudication\n')
rows = sum(c.get('certainty_only', False) or c.get('against_C') or c.get('against_H') for c in x['changes'])
with (root / 'progress.log').open('a') as f:
    f.write(f"scan 029 done 2026-11-20 18:50:00 UTC: {x['line_count']} lines read, 19 places cropped, {rows} rows\n")
print('Saved scan029, rows', rows)
