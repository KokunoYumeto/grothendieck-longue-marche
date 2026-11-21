from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '149_scan004'
OUT = ROOT / 'result/second'

READINGS = [
    ('B01', r'''i.e. un hom de schémas $\operatorname{Spec}K'\longrightarrow\operatorname{Spec}K$,
on a un morphisme de Topos
correspondant'''),
    ('B02', r'''(1) $B_{K'}\longrightarrow B_{K^{\unsure{\sharp|\natural}}}$'''),
    ('B03', r'''(\unsure{2}) $\Pi_{K'}\longrightarrow\Pi_{K^{\unsure{\sharp|\natural}}}$.'''),
    ('B04', r'''Ceci s'explicite en disant qu'\unsure{une|un} \deleted{\unsure{clôture}}
objet de $\Pi_{K'}$ (i.e. $p^t$. de $B_{K'}$, ou rev.
universel de $B_{K'}$, \deleted{)} une clôture \unsure{\deleted{alg.}\inserted{sép.}|sép.} \inserted{$\bar K'$} de $K'$)'''),
    ('B05', r'''on en fait un de $\Pi_{K^{\unsure{\sharp|\natural}}}$ (ainsi, on
prend $\bar K^{\unsure{\sharp|\natural}}$ = clôture \deleted{\unsure{sép|alg}}\inserted{alg} de $K$ dans $\bar K'$)'''),
    ('B06', r'''et pour deux $p^t$ correspondants, on a
un hom de groupes fondamentaux
correspondants, qui s'interpr\unsure{è|e}te p. ex.'''),
    ('B07', r'''comme
(\unsure{3|n}) $E_{\bar K'\mid K'}\longrightarrow E_{\bar K^{\unsure{\sharp|\natural}}\mid K^{\unsure{\sharp|\natural}}}$'''),
    ('B08', r'''et qui permet de réconstituer l'hom.
de topos comme une ``restriction des
scalaires''. '''.rstrip()),
    ('B09', r'''\margin{\unsure{1|$\vert$}\quad L'image de (3) est le sous-groupe fermé
de $E_{\bar K\mid K}$ qui correspond à la sous-\unsure{catégorie}}'''),
    ('B10', r'''\margin{3}'''),
]

NOTES = {
    'page': PAGE,
    'reader': 'reader_a',
    'phase': 'independent blind second reading',
    'authorized_inputs': [
        'source/SP83_C13_148+149_scans/149_scan004.jpg',
        'result/second/149_scan004_boxes.tsv',
        'Generic diplomatic macro conventions already provided',
    ],
    'independence': 'No witness, first.tsv, accepted page, first-reading crop, comparison, record, notes, notation or other reader\'s work consulted. All reading decisions precede comparison.',
    'original_view': {'viewed': True, 'count': 1, 'source_pixels': [1678, 2366]},
    'view_notes': [
        'All ten canonical exact-box crops were successfully displayed and directly viewed.',
        'All eighteen helper crops were successfully displayed and directly viewed. Helpers stay inside their parent prescribed rectangle.',
        'No image-output failure or discarded transport image occurred for this page. PNGs remained below the transport cap.',
        'The last-line B06 helper clips the upper part of some ascenders; the complete canonical B06 retains them and was used for the whole-line reading.',
    ],
    'boxes': {
        'B01': {
            'boundary': 'All three target lines and complete inline formula are inside the rectangle.',
            'reading_note': 'Retains hom without an added point, capital Topos, i.e. points, and final correspondant without an added colon. The inline shaft has a slight terminal head; transcribed as a rightward arrow.',
        },
        'B02': {
            'boundary': 'Complete formula label, arrow and both objects.',
            'reading_note': 'Label 1 is clear. The compact dark superscript after the target K has crossed/stepped strokes; sharp and natural remain alternatives. No superscript is supplied to the source K beyond its visible prime.',
        },
        'B03': {
            'boundary': 'Complete formula label, both objects, arrow and terminal point.',
            'reading_note': 'The label digit is strongly bent with a short lower stroke; 2 is the provisional reading, retained as doubtful rather than established from formula order. Target superscript remains sharp/natural. The short detached stroke at the arrow end is retained through rightward-arrow notation.',
        },
        'B04': {
            'boundary': 'All three target lines and visible revision layers fit inside the prescribed rectangle.',
            'reading_note': 'The article after qu\' is a run of low humps with an extended end; une/un remains open, without grammatical repair after the deleted feminine noun. The long strike crosses a word beginning clot- with the circumflex visible; cloture is proposed with doubt. The baseline abbreviations i.e., p^t., and rev. are retained. Punctuation after the first B_Kprime is a comma, not a semicolon. A separately crossed closing parenthesis follows the next B_Kprime and live comma. The overwritten abbreviation after cloture contains lighter tall-loop/loop-descender traces compatible with alg. and darker strokes compatible with sep.; whether these encode alg. replaced by sep., or only a retraced sep., remains explicit in the reading. A raised barred Kprime has a V-shaped insertion leader before de Kprime; it is retained as an insertion.',
        },
        'B05': {
            'boundary': 'Both target lines, complete formulas, replacement and closing parenthesis are inside the box.',
            'reading_note': 'Parenthetical word reads ainsi, followed by a comma and on. Raised alg has a looped l and descending g; no separate point is visible. The associated overwritten/crossed baseline abbreviation is uncertain between sep and alg and is retained under deletion with a reading doubt. The recurring superscripts remain sharp/natural. The upper-right arm of the later live K is retraced; no independent prime or extra symbol is securely visible there.',
        },
        'B06': {
            'boundary': 'All three complete target lines; no continuation supplied beyond p. ex.',
            'reading_note': 'The abbreviation is p^t, with no separately visible plural s or following point. Initial pour is retraced, not treated as a deletion. Correspondants and fondamentaux endings are retained. The accent on the e of interprete is uncertain and marked locally; the word itself and abbreviation p. ex. are legible.',
        },
        'B07': {
            'boundary': 'Comme, formula label, arrow and both complete indexed E objects are inside the rectangle. A neighboring-line fragment at the lower edge is excluded.',
            'reading_note': 'The label has an opening stroke joined to a hump-shaped character; 3/n remains a shape doubt. This is not silently resolved by the ordering of formulas. Source subscripts retain both primes and a near-vertical separator; target retains both compact sharp/natural signs and the bar only over its first K.',
        },
        'B08': {
            'boundary': 'Three target lines complete. The cut formula fragments at the top are context from B07.',
            'reading_note': 'The accent on reconstituer is visible. Retains l\'hom. abbreviation and the raised opening and closing double quotation marks around restriction des scalaires. Terminal point follows the closing quotation marks.',
        },
        'B09': {
            'boundary': 'The last pale stroke of the final word reaches the physical right paper/scan edge. Its ending is uncertain and potentially clipped by the source itself; no wording after it is supplied. Top-edge fragments of scalaires are context from B08.',
            'reading_note': 'Leading standalone vertical mark is retained as uncertain numeral 1/vertical stroke. Reference (3) has a separate visible upper and lower curve and is read 3. Formula contains E with bar K, near-vertical separator, K, and no additional visible superscripts. The final word is only provisionally read categorie, with an explicit doubt because the flat strokes and edge prevent secure final-letter separation.',
        },
        'B10': {
            'boundary': 'Pale folio 3 is complete; black lower scan edge excluded.',
            'reading_note': 'Hand: unnamed hand (folio annotation; attribution uncertain).',
        },
    },
    'clipped_or_uncertain_target_boundary_count': 1,
    'clipped_or_uncertain_target_boxes': ['B09'],
    'no_ocr_web_or_tex_compilation': True,
}

def main():
    target = OUT / (PAGE + '_second.tsv')
    if target.exists():
        raise RuntimeError('Refusing to overwrite a frozen independent reading.')
    with (OUT / (PAGE + '_boxes.tsv')).open(newline='') as f:
        boxes = list(csv.DictReader(f, delimiter='\t'))
    assert [r['box'] for r in boxes] == [b for b, _ in READINGS]
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
    counts = {}
    for suffix in ['crop_manifest', 'helper_manifest']:
        path = OUT / (PAGE + '_second_' + suffix + '.json')
        manifest = json.loads(path.read_text())
        for item in manifest:
            item['viewed'] = True
            item['view_method'] = 'Successful direct tools.view_image display with explicit image output'
        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
        counts[suffix] = len(manifest)
    assert counts == {'crop_manifest': 10, 'helper_manifest': 18}
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    NOTES['frozen_utc'] = datetime.now(timezone.utc).isoformat()
    NOTES['second_tsv_sha256'] = digest
    NOTES['box_count'] = len(READINGS)
    NOTES['canonical_crop_count'] = counts['crop_manifest']
    NOTES['helper_crop_count'] = counts['helper_manifest']
    NOTES['validation'] = 'Exact prescribed box order, ten nonempty rows, TSV round-trip and balanced macro braces checked; no TeX compilation.'
    (OUT / (PAGE + '_second_notes.json')).write_text(json.dumps(NOTES, ensure_ascii=False, indent=2) + '\n')
    (OUT / (PAGE + '_second.sha256')).write_text(digest + '  ' + target.name + '\n')
    target.chmod(0o444)
    print(json.dumps({'path': str(target), 'sha256': digest, 'box_count': len(READINGS),
                      'canonical_crops_viewed': counts['crop_manifest'],
                      'helpers_viewed': counts['helper_manifest'],
                      'boundary_issue_boxes': ['B09'], 'frozen': True}, indent=2))

if __name__ == '__main__':
    main()
