from pathlib import Path
import json
import re

dest = Path('/workspace/scratch/94548b74fbe0/out/readers/017/C')
tex = (dest/'reading.tex').read_text()
report = json.loads((dest/'report.json').read_text())
body = '\n'.join(re.split(r'(?<!\\)%', line, maxsplit=1)[0] for line in tex.splitlines() if not line.lstrip().startswith('%'))
errors = []
depth = 0
for i,ch in enumerate(body):
    if ch in '{}':
        preceding = 0
        j = i - 1
        while j >= 0 and body[j] == '\\':
            preceding += 1
            j -= 1
        if preceding % 2:
            continue
        depth += 1 if ch == '{' else -1
        if depth < 0:
            errors.append('Unmatched closing brace')
            break
if depth:
    errors.append(f'Brace balance final depth {depth}')
stack = []
for match in re.finditer(r'\\(begin|end)\{([^}]+)\}', body):
    action, env = match.groups()
    if action == 'begin':
        stack.append(env)
    elif not stack or stack.pop() != env:
        errors.append('Environment mismatch at '+match.group())
if stack:
    errors.append('Unclosed environments: '+repr(stack))
displays = re.findall(r'\\\[(.*?)\\\]', body, re.S)
if len(re.findall(r'\\\[',body)) != len(re.findall(r'\\\]',body)):
    errors.append('Display delimiter mismatch')
if any(re.search(r'\n\s*\n', d) for d in displays):
    errors.append('Blank physical line inside display math')
if len(re.findall(r'(?<!\\)\$',body)) % 2:
    errors.append('Odd unescaped dollar count')
allowed = set('scanpage uline forall in deleted unsure inserted Sigma setminus begin end overline cup hspace mathpunct coordinate path fill mathbin draw amalg figure reversemarginpar margin normalmarginpar subset Pi node coprod alpha pi jmath raisebox displaystyle bigcup mathop limits circ'.split())
commands = set(re.findall(r'\\([A-Za-z]+)', body))
unknown = sorted(commands - allowed)
if unknown:
    errors.append('Unreviewed macro names: '+repr(unknown))
kinds = {'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for d in report['differences']:
    if d['kind'] not in kinds:
        errors.append('Unknown difference category: '+d['id']+' '+d['kind'])
    if d['readers_crop'] and not (dest/d['readers_crop']).is_file():
        errors.append('Missing difference crop: '+d['id'])
ids = [d['id'] for d in report['differences']]
if len(ids) != len(set(ids)):
    errors.append('Duplicate difference IDs')
elements = [i['element'] for i in report['inventory']]
if len(elements) != len(set(elements)):
    errors.append('Duplicate inventory element IDs')
for row in report['C_source_row_map']:
    for part in row['local_parts']:
        if part['difference'] not in ids:
            errors.append('Missing source-row difference '+part['difference'])
for c in report['crops']:
    if not (dest/c['path']).is_file():
        errors.append('Missing crop '+c['path'])
if tex.count('\\scanpage{17}') != 1:
    errors.append('Scan identifier count differs from one')
if '% archive sheet number: 16' not in tex:
    errors.append('Missing archive-number comment')
result = dict(passed=not errors, errors=errors, brace_final_depth=depth, open_environments=stack, display_blocks=len(displays), reviewed_macro_names=sorted(commands), differences=len(ids), inventory_elements=len(elements), C_source_rows=len(report['C_source_row_map']), crops=len(report['crops']), scope='Structural source checks only; no compilation, rendering, manuscript recognition, numerical geometry or mathematical proof check.')
(dest/'structural_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
report['final_validation'] = {'structural_source_check':result, 'complete_tex_report_joint_read':False}
report['processing_events'].append(dict(type='structural source validation',script='verify_source.py',inputs=['reading.tex','report.json','existing crop files'],operations='TeX comment removal for structural parsing; brace/environment/display/dollar checks; reviewed macro set; allowed kind and identifier checks; source-row and file-reference checks.',results=result,scope='Source integrity only; no mathematical statement is tested.'))
(dest/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors:
    raise SystemExit(1)
