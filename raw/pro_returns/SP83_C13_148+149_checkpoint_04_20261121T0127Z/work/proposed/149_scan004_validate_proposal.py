from pathlib import Path
import csv
import json
import re

BASE = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '149_scan004'
record = json.loads((BASE/'proposed'/f'{PAGE}.json').read_text())
tex = (BASE/'proposed'/f'{PAGE}.tex').read_text()
with (BASE/'packets'/PAGE/'MARKS.tsv').open() as fh:
    supplied = [row['id'] for row in csv.DictReader(fh, delimiter='\t')]
checks = []
def check(name, value):
    checks.append({'check': name, 'passed': bool(value)})
    if not value:
        raise AssertionError(name)

def escaped(s, i):
    n = 0
    j = i-1
    while j >= 0 and s[j] == '\\':
        n += 1
        j -= 1
    return n % 2 == 1

def balanced(s):
    level = 0
    for i, char in enumerate(s):
        if char in '{}' and not escaped(s, i):
            level += 1 if char == '{' else -1
            if level < 0:
                return False
    return level == 0

check('Only the five supplied MARKS IDs, in source order', [d['id'] for d in record['decisions']] == supplied)
check('Whole TEX has parity-aware balanced braces', balanced(tex))
check('All ten second readings have balanced braces', all(balanced(b['reading']) for b in record['second_boxes']))
check('Whole TEX has an even number of unescaped math dollars', sum(c == '$' and not escaped(tex,i) for i,c in enumerate(tex)) % 2 == 0)
check('Three opening and three closing display delimiters', tex.count(r'\[') == tex.count(r'\]') == 3)
check('Every second reading is a verbatim proposed TEX substring', all(b['reading'] in tex for b in record['second_boxes']))
check('All second boxes are unique IDs and valid original coordinates', len({b['box'] for b in record['second_boxes']}) == len(record['second_boxes']) and all(0 <= b['x0'] < b['x1'] <= 1678 and 0 <= b['y0'] < b['y1'] <= 2366 for b in record['second_boxes']))
for field, id_key in [('changes','id'),('inventory','element'),('notes','id'),('implicit_decisions','id')]:
    check(f'{field} IDs are unique', len({row[id_key] for row in record[field]}) == len(record[field]))
note_ids = {n['id'] for n in record['notes']}
check('All check events refer to an actual note ID', all(e['statement_id'] in note_ids for e in record['check_events']))
check('Six separate implicit superscript decisions remain undecided', len(record['implicit_decisions']) == 6 and all(d['decision'] == 'undecided' for d in record['implicit_decisions']))
check('All six in-place superscript alternatives occur in TEX', tex.count(r'\unsure{\deleted{\prime}|*}') == 6)
check('Both insertions and all three definite/possible prose cancellations are retained', r'\inserted{$\bar K\' not in tex and all(s in tex for s in [r"\inserted{$\bar K'$}",r'\inserted{alg}',r'\deleted{clôture}',r'\deleted{)}',r'\unsure{sép|\deleted{sép}}']))
check('Explicit accent, capital Topos and de groupes are present', all(s in tex for s in ['réconstituer','de Topos','un hom de groupes']))
check('Doubtful numeric labels and both marginal annotations present', all(s in tex for s in [r'(1)\qquad',r'(\unsure{2|1})',r'\unsure{(3)|3)}',r'\margin{\unsure{1}}',r'\margin{3}']))
check('Last source clause remains unfinished with no supplied point', 'qui correspond à la sous-extension\n'+r'\margin{3}' in tex)
manifest = json.loads((BASE/'proposed'/f'{PAGE}_crop_manifest.json').read_text())
boundary = json.loads((BASE/'proposed'/f'{PAGE}_boundary_manifest.json').read_text())
crops = manifest['crops']+[boundary]
check('Ten places and eleven retained evidence versions', record['places_cropped'] == 10 and len(crops) == 11)
check('All eleven evidence files exist and were viewed', all(Path(c['path']).is_file() and c['viewed'] for c in crops))
known = {tuple(c['box']): 'crops/'+Path(c['path']).name for c in crops}
for field in ['changes','decisions','implicit_decisions']:
    check(f'Every {field} crop and box maps to retained evidence', all(known.get(tuple(row['box'])) == row['crop'] for row in record[field]))
check('Pale lower folio has explicitly uncertain writer attribution', any(e['first_words_or_objects'] == r'\margin{3}' and e['hand'] == 'unnamed hand (folio annotation; attribution uncertain)' for e in record['inventory']))
check('All inventory passages use ordinary text sheet kind', all(e['sheet_kind'] == 'text' for e in record['inventory']))
report = {'page': PAGE, 'validation_scope': 'Structural metadata and literal TEX only; no compilation, rendering, OCR, or source-image reinspection.',
          'passed': True, 'checks': checks,
          'counts': {k:len(record[k]) for k in ['changes','decisions','implicit_decisions','doubts','inventory','second_boxes']},
          'diff_c_rows': sum(r['diff_c'] for r in record['changes']), 'diff_h_rows': sum(r['diff_h'] for r in record['changes'])}
(BASE/'proposed'/f'{PAGE}_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'page': PAGE, 'passed': True, 'checks':len(checks), 'counts':report['counts'], 'diff_c_rows':report['diff_c_rows'],'diff_h_rows':report['diff_h_rows']}, indent=2))
