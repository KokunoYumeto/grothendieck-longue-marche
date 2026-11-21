"""Validate documentary completeness without TeX compilation or image recognition."""
from pathlib import Path
import csv, hashlib, json, re, sys

WORK = Path(__file__).resolve().parents[1]
BASE = WORK.parent
FINAL = '--final' in sys.argv
state = json.loads((WORK/'run_state.json').read_text())
order = state['order']
done = [p for p in order if p in state['completed']]
errors = []
def check(ok, message):
    if not ok: errors.append(message)
def rows(path, delimiter='\t'):
    with path.open(newline='') as f: return list(csv.DictReader(f, delimiter=delimiter))
def tex_structure(text, name):
    text = re.sub(r'(?<!\\)%[^\n]*', '', text)
    braces = 0
    for token in re.findall(r'\\[{}%]|[{}]', text):
        if token == '{': braces += 1
        elif token == '}': braces -= 1
        if braces < 0: break
    check(braces == 0, name+': unmatched ordinary braces')
    stack = []
    for match in re.finditer(r'\\(begin|end)\{([^{}]+)\}', text):
        op, env = match.groups()
        if op == 'begin': stack.append(env)
        elif not stack or stack.pop() != env: errors.append(name+': mismatched environment '+env)
    check(not stack, name+': unclosed environments '+str(stack))
    check('\\documentclass' not in text and '\\begin{document}' not in text,
          name+': fragment unexpectedly contains a preamble/document wrapper')

check(len(order) == len(set(order)) == 24, 'Expected 24 distinct pages in source order')
check(len(state['completed']) == len(set(state['completed'])), 'Duplicate completed pages')
if FINAL:
    check(set(done) == set(order), 'Not every first reading is committed')
    check(set(state['audited']) == set(order), 'Not every page has a completed second audit')
    assignments = state.get('blind_assignments', {})
    check(set(assignments) == set(order), 'Incomplete blind-reader assignment record')
    for page, assignment in assignments.items():
        check(assignment['reader'] != state['assignments'][page],
              page+': same reader on both passes')
    snapshot_path = WORK/'audit'/'first_readings_before_blind_sha256.json'
    check(snapshot_path.exists(), 'Missing pre-blind first-reading snapshot')
    if snapshot_path.exists():
        for name, digest in json.loads(snapshot_path.read_text())['sha256'].items():
            check(hashlib.sha256((WORK/name).read_bytes()).hexdigest() == digest,
                  name+': original first reading or box list was changed after blind phase began')

source_marks = rows(BASE/'source/SP94_C13_151_texts/MARKS.tsv')
expected_marks = [r['id'] for r in source_marks if '151_scan'+str(r['scan']).zfill(3) in done]
check([r['id'] for r in rows(WORK/'decisions.tsv')] == expected_marks,
      'decisions.tsv lacks exact source mark coverage/order')
allowed_checks = {'targeted proof check','independent re-proof','computation or formal certificate',
                  'used and rechecked in this run','carried as background without fault found',
                  'refuted (with refined id)'}
for row in rows(WORK/'CHECK_EVENTS.tsv'):
    check(row['type'] in allowed_checks or row['type'].startswith('refuted'),
          'Unknown check-event type '+row['type'])

all_counts = {'C':0,'H':0,'places':0,'boxes':0}
for page in done:
    path = WORK/'pages'/(page+'.tex')
    text = path.read_text()
    tex_structure(text,page)
    check(re.findall(r'\\scanpage\{(\d+)\}',text) == [str(int(page[-3:]))],
          page+': wrong/multiple scan markers')
    report = json.loads((WORK/'reports'/(page+'.json')).read_text())
    check(bool(report.get('reviewed_utc')),page+': absent main-reader review time')
    check(all(i['transcribed']=='yes' for i in report['inventory']),page+': incomplete inventory')
    ids = [c['id'] for c in report['changes']]
    check(len(ids)==len(set(ids)),page+': duplicate change identifiers')
    for row in report['changes']+report['decisions']:
        crop=row.get('crop','')
        if crop and crop!='page': check((WORK/crop).is_file(),page+': missing '+crop)
    for row in report['decisions']:
        check(row['decision']=='undecided' or row.get('crop') not in ('','page',None),
              page+': resolved mark without crop '+row['id'])
    for row in report['changes']:
        all_counts['C']+=bool(row.get('diff_c'))
        all_counts['H']+=bool(row.get('diff_h'))
        all_counts['places']+=bool(row.get('diff_c') or row.get('diff_h'))
    boxes=rows(WORK/'second'/(page+'_boxes.tsv'))
    first=rows(WORK/'second'/(page+'_first.tsv'))
    names=[r['box'] for r in boxes]
    check(len(names)==len(set(names)),page+': duplicate box identifiers')
    check([r['box'] for r in first]==names,page+': first readings do not match boxes')
    all_counts['boxes']+=len(boxes)
    if page in state['audited'] or FINAL:
        for suffix in ('second.tsv','comparison.tsv','independent_notes.md'):
            check((WORK/'second'/(page+'_'+suffix)).is_file(),page+': missing '+suffix)
        second_path=WORK/'second'/(page+'_second.tsv')
        comparison_path=WORK/'second'/(page+'_comparison.tsv')
        if second_path.exists(): check([r['box'] for r in rows(second_path)]==names,page+': second reading box mismatch')
        if comparison_path.exists():
            comparison=rows(comparison_path)
            check([r['box'] for r in comparison]==names,page+': comparison box mismatch')
            first_by_box = {r['box']:r['reading'] for r in first}
            second_by_box = {r['box']:r['reading'] for r in rows(second_path)} if second_path.exists() else {}
            for row in comparison:
                check(row['decision'] not in ('','PENDING'),page+'/'+row['box']+': unadjudicated difference')
                if row['same_tokens']=='no': check(bool(row['evidence']),page+'/'+row['box']+': difference without crop evidence')
                check(row['first']==first_by_box.get(row['box']),page+'/'+row['box']+': comparison changed first reading')
                check(row['second']==second_by_box.get(row['box']),page+'/'+row['box']+': comparison changed independent reading')
                check((WORK/'crops'/('second_'+page+'_'+row['box']+'.jpg')).exists(),
                      page+'/'+row['box']+': missing independent crop')

combined=(WORK/'SP94_C13_151_transcription.tex').read_text()
expected='\\cotefile{151}\n\n'+'\n\n'.join((WORK/'pages'/(p+'.tex')).read_text().rstrip() for p in done)+'\n'
check(combined==expected,'Combined transcription differs from page files or their source order')
tex_structure(combined,'combined')
check(len(rows(WORK/'SP94_C13_151_collation.tsv'))==all_counts['H'],'H collation count mismatch')
inventory=rows(WORK/'SP94_C13_151_inventory.csv',',')
check(all(r['transcribed']=='yes' for r in inventory),'Aggregate inventory contains unfinished elements')
result={'stage':'final' if FINAL else 'in progress','pages':len(done),**all_counts,'errors':errors}
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors: sys.exit(1)
