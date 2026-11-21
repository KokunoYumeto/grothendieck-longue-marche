from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '149_scan003'
OUT = ROOT / 'result/second'

READINGS = [
    ('B01', r'''1. \uline{Résultats de fidélité}
\margin{\unsure{1|$\lambda$}}'''),
    ('B02', r'''topos (pro\inserted{fini}) galoisien.'''),
    ('B03', r'''Si $\bar K$ est une telle clôture, son groupe
des \inserted{$K$-}automorphismes $\operatorname{Gal}(\bar K\mid K)$ ou $E_{\bar K\mid K}$
s'identifie au groupe des \deleted{$\unsure{K}$-}automorphismes'''),
    ('B04', r'''du $p^t$ \inserted{de $B_K$} associé à $\bar K\mid K$ (il vaut peut-être
mieux de dire : à l'opposé de ce
groupe --- \deleted{$\bar K$} la variance des clôtures alg.
de $K$ est comme celle des foncteurs
fibres, à l'opposé de celle des points...)'''),
    ('B05', r'''Bien entendu, $B_K$ se réconstitue à
partir de $\Pi_K$, comme le topos des'''),
    ('B06', r'''des Ensembles discrets à action continue
de $E_{\bar K\mid K}$.'''),
    ('B07', r'''\margin{2}'''),
]

NOTES = {
    'page': PAGE,
    'reader': 'reader_a',
    'phase': 'independent blind second reading',
    'authorized_inputs': [
        'source/SP83_C13_148+149_scans/149_scan003.jpg',
        'result/second/149_scan003_boxes.tsv',
        'result/scripts/second_reader_guide.md',
    ],
    'independence': 'No witness, first reading, accepted page, first crop, notation, notes, record or comparison consulted. All choices below precede any comparison.',
    'original_view': {'viewed': True, 'count': 1},
    'view_notes': [
        'All seven exact-box canonical PNGs were directly and successfully viewed. B01-B04 had been successfully viewed before the context handoff; B05-B07 were each viewed individually afterward.',
        'An attempted combined output for B05-B07 was truncated. That attempted output is not counted as a view; the later individual successful displays are the evidence.',
        'B02, B03 and B04 were revisited as their existing canonical crops to decide insertion placement and revision scope. The original was not reopened.',
        'All eight helpers were directly viewed. Each helper is contained entirely within its named prescribed box; none adds text outside the authorized rectangles.',
    ],
    'boxes': {
        'B01': {
            'boundary': 'Heading and small upper-right mark complete within the prescribed rectangle.',
            'reading_note': 'Heading numeral 1 with point; phrase underlined. The separate dark upper-right mark has a diagonal left entry and nearly vertical right leg. Identity remains uncertain between numeral 1 and a lambda-like sign; it is retained separately rather than omitted.',
        },
        'B02': {
            'boundary': 'Target phrase and insertion complete. Fragments of the preceding line at the top and the beginning of the next Le at the right are context only.',
            'reading_note': 'The curved insertion leader has its lower endpoint between the baseline o of pro and the closing parenthesis. The raised fini is therefore placed inside the parentheses. No hyphen is supplied between pro and fini.',
        },
        'B03': {
            'boundary': 'Three target lines complete. An upper-edge fragment of the preceding line is excluded. The lower-edge de B_K belongs to the next line and is read completely in B04.',
            'reading_note': 'Raised K- is inserted before the first automorphismes. The separate old K-like symbol and its short following hyphen before the second automorphismes are crossed; K identity remains doubtful. Both full formulas are retained. Their separators are near-vertical slightly curved strokes, transcribed as mid; no bar is supplied to the obscured deleted K.',
        },
        'B04': {
            'boundary': 'The raised de B_K, all five target lines, and closing parenthesis are complete. Prior-line fragments at the top and following-line fragments at the bottom are context only.',
            'reading_note': 'Raised de B_K is attached by a curved leader after p^t. The dash after groupe is retraced with converging strokes, rather than a secure equals sign. The following barred K is crossed. Final de has a dark retraced e, with no separately visible s; it is read de. Abbreviation alg., superscript t and three final dots are preserved.',
        },
        'B05': {
            'boundary': 'Two target lines complete. Tail fragments of the preceding parenthesis at the top and the top of a following-line symbol at the bottom are context only; continuation after des is outside this box.',
            'reading_note': 'The detached accent above the beginning of réconstitue is visible and retained. Pi has its top bar and both descending strokes; K is a subscript.',
        },
        'B06': {
            'boundary': 'Two target lines and terminal point complete; no continuation is supplied.',
            'reading_note': 'Ensembles begins with a tall looped capital-form E and a separated upper stroke, retained with capital E. Formula separator is near upright with a leftward bend at its foot. A small detached diagonal immediately left of the first K is treated as the visible continuation of that K\'s rising arm, not a securely independent minus sign.',
        },
        'B07': {
            'boundary': 'Pale lower-left folio 2 complete; the dark scan edge is not handwriting.',
            'reading_note': 'Hand: unnamed hand (folio annotation; attribution uncertain).',
        },
    },
    'clipped_target_count': 0,
    'unresolved_target_boundary_count': 0,
    'no_ocr_web_or_tex_compilation': True,
}

def main():
    target = OUT / (PAGE + '_second.tsv')
    if target.exists():
        raise RuntimeError('Refusing to overwrite an existing independent second reading.')
    with (OUT / (PAGE + '_boxes.tsv')).open(newline='') as f:
        boxes = list(csv.DictReader(f, delimiter='\t'))
    assert [b['box'] for b in boxes] == [b for b, _ in READINGS]
    for box, reading in READINGS:
        assert reading and '\t' not in reading
        depth = 0
        for char in reading:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
                assert depth >= 0, box
        assert depth == 0, box
    with target.open('w', newline='') as f:
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')
        writer.writerow(['box', 'reading'])
        writer.writerows(READINGS)
    with target.open(newline='') as f:
        roundtrip = list(csv.DictReader(f, delimiter='\t'))
    assert [(r['box'], r['reading']) for r in roundtrip] == READINGS
    for suffix in ['crop_manifest', 'helper_manifest']:
        path = OUT / (PAGE + '_second_' + suffix + '.json')
        manifest = json.loads(path.read_text())
        for item in manifest:
            item['viewed'] = True
            item['view_method'] = 'tools.view_image with explicit image output; successful direct view'
        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    NOTES['frozen_utc'] = datetime.now(timezone.utc).isoformat()
    NOTES['second_tsv_sha256'] = digest
    NOTES['box_count'] = len(READINGS)
    NOTES['canonical_crop_count'] = 7
    NOTES['helper_crop_count'] = 8
    NOTES['validation'] = 'Exact box order, seven rows, TSV round-trip, nonempty fields and balanced macro braces checked. No TeX compilation.'
    (OUT / (PAGE + '_second_notes.json')).write_text(json.dumps(NOTES, ensure_ascii=False, indent=2) + '\n')
    (OUT / (PAGE + '_second.sha256')).write_text(digest + '  ' + target.name + '\n')
    target.chmod(0o444)
    print(json.dumps({'path': str(target), 'sha256': digest, 'box_count': len(READINGS),
                      'canonical_crops_viewed': 7, 'helpers_viewed': 8,
                      'clipped_targets': 0, 'frozen': True}, indent=2))

if __name__ == '__main__':
    main()
