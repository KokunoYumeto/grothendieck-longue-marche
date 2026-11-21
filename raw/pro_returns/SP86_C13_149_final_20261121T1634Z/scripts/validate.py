"""Structural delivery checks only; no OCR and no TeX compilation."""
from pathlib import Path
import csv, hashlib, json, re, sys
from audit_compare import reader_name, utc_datetime

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]

def audit_evidence_errors(page, report, expected_boxes, comparison_meta):
    """Check recorded reading provenance and coverage, without deciding ink."""
    errors = []
    metadata_path = BASE/'second'/f'{page}_reader.json'
    if not metadata_path.exists():
        return [page+': independent-reader metadata absent']
    metadata = json.loads(metadata_path.read_text())
    if metadata.get('page') != page:
        errors.append(page+': independent metadata has wrong page')
    if reader_name(metadata['reader']) == reader_name(report['reader']):
        errors.append(page+': second reader also made first reading')
    attestations = metadata.get('attestations', {})
    if not (metadata.get('only_permitted_inputs_opened') is True or
            attestations.get('only_permitted_authoritative_inputs_opened') is True or
            attestations.get('only_permitted_authoritative_inputs_opened_during_assignment') is True or
            attestations.get('only_permitted_authoritative_inputs_opened_current_assignment') is True):
        errors.append(page+': permitted-input attestation absent')
    attestation_keys = ['all_listed_crops_visually_read', 'every_listed_crop_visually_read',
                        'all_crops_visually_read']
    if not any(metadata.get(k) is True or attestations.get(k) is True for k in attestation_keys):
        errors.append(page+': all-crops visual-reading attestation absent')
    if metadata.get('ocr_used') is True or metadata.get('comparison_performed') is True:
        errors.append(page+': independent reading records a prohibited operation')
    if metadata['completed_utc'] != comparison_meta['reader_completed_utc']:
        errors.append(page+': reader completion timestamp changed')
    if utc_datetime(comparison_meta['compared_utc']) > utc_datetime(report['audit']['completed_utc']):
        errors.append(page+': root audit timestamp precedes comparison')
    frozen_path = BASE/'second'/f'{page}_boxes.tsv'
    with frozen_path.open() as f:
        frozen = {x['box']: [int(x[k]) for k in ['x0','y0','x1','y1']]
                  for x in csv.DictReader(f, delimiter='\t')}
    records = metadata.get('boxes', [])
    ids = [x.get('id', x.get('box')) for x in records]
    if len(ids) != len(set(ids)) or set(ids) != set(expected_boxes):
        errors.append(page+': reader metadata box coverage mismatch')
    for x in records:
        box = x.get('id', x.get('box'))
        coords = x.get('original_coordinates', x.get('coordinates', x.get('coords')))
        if coords != frozen.get(box):
            errors.append(page+': second crop coordinates differ from frozen list '+str(box))
        if x.get('visually_read') is not True:
            errors.append(page+': individual visual-reading record absent '+str(box))
        crop = Path(x.get('crop_path', x.get('crop', '')))
        crop = crop if crop.is_absolute() else BASE/crop
        expected_crop = BASE/'crops'/f'{page}_{box}_second.png'
        if crop.resolve() != expected_crop.resolve() or not expected_crop.is_file():
            errors.append(page+': fresh crop absent or wrong path '+str(box))
    with (BASE/'second'/f'{page}_comparison.tsv').open() as f:
        comparison = list(csv.DictReader(f, delimiter='\t'))
    differing = {x['box'] for x in comparison if x['different']=='yes'}
    decisions = report.get('audit_adjudications', [])
    if {x['box'] for x in decisions} != differing or len(decisions) != len(differing):
        errors.append(page+': root decisions do not cover exactly the differing boxes')
    viewed = set(report.get('audit_root_viewed', []))
    for x in decisions:
        if x['crop'] not in viewed or not (BASE/x['crop']).is_file():
            errors.append(page+': root crop inspection record absent '+x['box'])
        if not x.get('evidence') or not x.get('final'):
            errors.append(page+': root decision is incomplete '+x['box'])
    audit = report['audit']
    if (audit['boxes'], audit['differences'], audit['changed_boxes']) != (
            len(comparison), len(differing), sum(bool(x['changed']) for x in decisions)):
        errors.append(page+': audit counts disagree with recorded decisions')
    return errors

def grouping_errors(tex):
    depth = 0
    math_delimiters = 0
    i = 0
    while i < len(tex):
        char = tex[i]
        if char == '\\':
            i += 2
            continue
        if char == '%':
            end = tex.find('\n', i)
            i = len(tex) if end < 0 else end + 1
            continue
        if char == '{': depth += 1
        if char == '}':
            depth -= 1
            if depth < 0: return 'unmatched closing brace'
        if char == '$': math_delimiters += 1
        i += 1
    if depth: return 'unmatched opening brace'
    if math_delimiters % 2: return 'unpaired dollar delimiter'
    return None

def table_errors():
    """Verify the requested delivery schemas and controlled values."""
    errors = []
    schemas = {
        'SP86_C13_149_collation.tsv': ('\t', ['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']),
        'decisions.tsv': ('\t', ['id','cote','scan','decision','reading','what the ink shows','crop','confidence']),
        'SP86_C13_149_inventory.csv': (',', ['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']),
    }
    kinds = {'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
    element_kinds = {'text','display','diagram','drawing','margin note','insertion','deletion'}
    sheet_kinds = {'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
    for name, (delimiter, columns) in schemas.items():
        path = BASE/name
        if not path.is_file():
            errors.append(name+': required file absent')
            continue
        with path.open(newline='') as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            if reader.fieldnames != columns:
                errors.append(name+': header differs from requested schema')
            for rowno, row in enumerate(reader, 2):
                if None in row or any(row.get(key) is None for key in columns):
                    errors.append(f'{name}:{rowno}: malformed record')
                    continue
                if name.endswith('_collation.tsv'):
                    if row['kind'] not in kinds or row['marked_in_H'] not in {'yes','no'} or row['confidence'] not in {'high','medium','low'}:
                        errors.append(f'{name}:{rowno}: invalid controlled value')
                    if int(row['our_scan']) != int(row['their_page'])+1:
                        errors.append(f'{name}:{rowno}: witness-page correspondence changed')
                if name.endswith('_inventory.csv'):
                    if row['kind'] not in element_kinds or row['sheet_kind'] not in sheet_kinds or row['transcribed'] != 'yes' or not row['hand']:
                        errors.append(f'{name}:{rowno}: invalid or incomplete inventory record')
    return errors

def validate(final=False):
    reports = [json.loads(p.read_text()) for p in sorted((BASE/'reviews').glob('149_scan*.json'))]
    expected = [p.stem for p in sorted((ROOT/'source/SP86_C13_149_scans').glob('*.jpg'))]
    errors=[]
    seen_decisions=[]
    for r in reports:
        page=r['page']; tex=(BASE/'pages'/f'{page}.tex').read_text()
        grouping = grouping_errors(tex)
        if grouping: errors.append(page+': '+grouping)
        if not tex.startswith('\\scanpage{'+str(r['scan'])+'}'): errors.append(page+': wrong scan marker')
        forbidden=re.findall(r'\\(?:struck|marginal|uncertain|ill|add|note)(?=[{\s])',tex)
        if forbidden: errors.append(page+': foreign witness macros '+str(forbidden))
        for field in ['changes','decisions','inventory','doubts','notes','check_events','hand','notation','abbreviations','audit_boxes','diff_coverage','deletion_insertion_review']:
            if field not in r: errors.append(page+': missing '+field)
        for x in r['changes']:
            if not (x.get('against_C') or x.get('against_H')): errors.append(page+': change against neither witness '+x['id'])
            if not x.get('crop') or not (BASE/x['crop']).exists(): errors.append(page+': missing crop '+x['id'])
            if x.get('confidence') not in ['high','medium','low']: errors.append(page+': invalid confidence '+x['id'])
            if len(x.get('box',[]))!=4: errors.append(page+': invalid coordinates '+x['id'])
        expected_rows=len((ROOT/'packets'/page/'differences.tsv').read_text().splitlines())-1
        rows=[x['row'] for x in r['diff_coverage']]
        if sorted(rows)!=list(range(1,expected_rows+1)): errors.append(page+': C/H difference coverage mismatch')
        for x in r['inventory']:
            if x['transcribed']!='yes': errors.append(page+': inventory incomplete '+x['element'])
        marks=[line.split('\t')[0] for line in (ROOT/'packets'/page/'marks.tsv').read_text().splitlines()[1:]]
        decs=[x['id'] for x in r['decisions']]
        if decs!=marks: errors.append(page+': MARKS order or coverage mismatch')
        seen_decisions.extend(decs)
        for x in r['decisions']:
            if x['decision'] not in ['first','alternative','other','undecided']: errors.append(page+': invalid mark decision '+x['id'])
            if x['decision']!='undecided' and x['crop']=='page': errors.append(page+': resolved mark lacks crop '+x['id'])
        boxes=[x['box'] for x in r['audit_boxes']]
        if len(boxes)!=len(set(boxes)): errors.append(page+': duplicate audit boxes')
        if final:
            for suffix in ['boxes','first','second','comparison','adjudication']:
                if not (BASE/'second'/f'{page}_{suffix}.tsv').exists(): errors.append(page+': missing audit '+suffix)
            audit=r.get('audit',{})
            if not audit.get('reader') or reader_name(audit['reader'])==reader_name(r['reader']): errors.append(page+': independent reader not recorded')
            if not audit.get('completed_utc'): errors.append(page+': audit not completed')
            manifest_path=BASE/'second'/'input_manifest.json'
            comparison_path=BASE/'second'/f'{page}_comparison.json'
            if not manifest_path.exists() or not comparison_path.exists():
                errors.append(page+': audit integrity metadata absent')
            else:
                manifest=json.loads(manifest_path.read_text())['pages'][page]
                comparison_meta=json.loads(comparison_path.read_text())
                if audit.get('completed_utc'):
                    errors.extend(audit_evidence_errors(page, r, boxes, comparison_meta))
                for suffix in ['boxes','first','second']:
                    path=BASE/'second'/f'{page}_{suffix}.tsv'
                    if path.exists():
                        actual=hashlib.sha256(path.read_bytes()).hexdigest()
                        expected_hash=comparison_meta['second_sha256'] if suffix=='second' else manifest[suffix+'_sha256']
                        if actual!=expected_hash: errors.append(page+': immutable audit '+suffix+' changed')
                if utc_datetime(comparison_meta['reader_completed_utc'])>utc_datetime(comparison_meta['compared_utc']):
                    errors.append(page+': comparison preceded completed independent reading')
                for suffix in ['boxes','first','second','comparison','adjudication']:
                    path=BASE/'second'/f'{page}_{suffix}.tsv'
                    if path.exists():
                        with path.open() as f: ids=[row['box'] for row in csv.DictReader(f,delimiter='\t')]
                        if len(ids)!=len(set(ids)) or set(ids)!=set(boxes): errors.append(page+': audit '+suffix+' box coverage mismatch')
    if final:
        errors.extend(table_errors())
        pages=[r['page'] for r in reports]
        if pages!=expected: errors.append('Supplied scan/page coverage mismatch')
        ordered_marks=[line.split('\t')[0] for line in (ROOT/'source/SP86_C13_149_texts/MARKS.tsv').read_text().splitlines()[1:]]
        if seen_decisions!=ordered_marks: errors.append('Global MARKS coverage or order mismatch')
        combined = '\\cotefile{149}\n\n'+'\n\n'.join(
            (BASE/'pages'/f'{page}.tex').read_text().rstrip() for page in expected)+'\n'
        if (BASE/'SP86_C13_149_transcription.tex').read_text()!=combined:
            errors.append('Combined transcription differs from ordered page fragments')
    result={'mode':'final' if final else 'first-pass progress','pages':len(reports),'marks':len(seen_decisions),'errors':errors}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__=='__main__':
    raise SystemExit(bool(validate('--final' in sys.argv)['errors']))
