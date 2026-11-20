from pathlib import Path
import json
import re

OUT = Path('/workspace/scratch/94548b74fbe0/out/readers/017/B')
text = (OUT / 'reading.tex').read_text(encoding='utf-8')
report = json.loads((OUT / 'report.json').read_text(encoding='utf-8'))
body = re.sub(r'(?<!\\)%[^\n]*', '', text)
errors = []
depth = 0
for match in re.finditer(r'(?<!\\)[{}]', body):
    depth += 1 if match.group() == '{' else -1
    if depth < 0:
        errors.append('Closing brace precedes opening brace.')
if depth:
    errors.append(f'Final brace depth {depth}.')
stack = []
envs = []
for match in re.finditer(r'\\(begin|end)\{([^{}]+)\}', body):
    command, env = match.groups()
    if command == 'begin':
        stack.append(env)
        envs.append(env)
    elif not stack or stack.pop() != env:
        errors.append(f'Environment mismatch at {env}.')
if stack:
    errors.append(f'Unclosed environments: {stack}.')
if body.count(r'\[') != body.count(r'\]'):
    errors.append('Display delimiters mismatch.')
if len(re.findall(r'(?<!\\)\$', body)) % 2:
    errors.append('Odd number of inline math delimiters.')
in_display = False
for number, line in enumerate(text.splitlines(), 1):
    if r'\[' in line:
        in_display = True
    if in_display and not line.strip():
        errors.append(f'Empty physical line inside display at {number}.')
    if r'\]' in line:
        in_display = False
allowed = set('scanpage uline forall in deleted unsure Sigma inserted setminus begin overline cup end mathbin vcenter hbox useasboundingbox draw figure reversemarginpar margin fill normalmarginpar subset amalg node notin coprod alpha pi displaystyle mathord mathop limits Pi bigcup circ'.split())
macros = sorted(set(re.findall(r'\\([A-Za-z]+)', body)))
unknown = sorted(set(macros) - allowed)
if unknown:
    errors.append(f'Macros outside explicit local standard/preamble list: {unknown}.')
for row in report['differences']:
    name = row['readers_crop']
    if name and not (OUT / name).is_file():
        errors.append(f'Missing crop {name}.')
for crop in report['crops']:
    if not (OUT / crop['path']).is_file():
        errors.append(f'Missing manifest crop {crop["path"]}.')
for graphic in report['graphics']:
    if f'% {graphic["id"]}:' not in text:
        errors.append(f'Missing TeX graphic tag {graphic["id"]}.')
declared_paths = sum(g['paths'] for g in report['graphics'])
actual_paths = len(re.findall(r'\\(?:draw|fill)\b', body))
if declared_paths != actual_paths:
    errors.append(f'Path command count mismatch: {declared_paths}/{actual_paths}.')
rows = [r['row'] for r in report['C_source_row_map']]
if rows != list(range(1,13)):
    errors.append('Original C source-row identities are incomplete or reordered.')
ids = [d['id'] for d in report['differences']]
if len(set(ids)) != len(ids):
    errors.append('Duplicate difference ID.')
for row in report['C_source_row_map']:
    for part in row['parts']:
        if part['difference_id'] not in ids:
            errors.append('Missing source-row local-part difference.')
positions = {'017.01':80,'017.02':208,'017.03':235,'017.04':183,'017.05':319,
             '017.06':408,'017.07':627,'017.08':738,'017.09':936,'017.10':1158,
             '017.11':958,'017.12':1035,'017.13':1146,'017.14':1108,
             '017.15':1280,'017.16':1282,'017.17':1418,'017.18':1367,
             '017.19':1520,'017.20':1630,'017.21':1750,'017.22':1975,
             '017.23':2070,'017.24':2162,'017.25':2188,'017.B36':2310}
for g in report['graphics']:
    positions[g['element']] = g['bbox'][1]
for item in report['inventory']:
    item['position_order_y'] = positions[item['element']]
report['inventory'].sort(key=lambda item:(item['position_order_y'],item['element']))
for d in report['differences']:
    if d['id'] == 'N02':
        d['shape_confidence'] = 'medium'
        d['role_and_hand'] = 'unresolved'
    if d['id'] == 'N09':
        d['shape_confidence'] = 'high'
        d['role_and_hand'] = 'unresolved'
result = {'brace_depth':depth,'environment_instances':len(envs),'display_pairs':body.count(r'\['),
          'inline_math_delimiters':len(re.findall(r'(?<!\\)\$', body)),
          'macro_names':macros,'graphic_path_commands':actual_paths,'declared_graphic_path_commands':declared_paths,
          'crop_file_count':len(report['crops']),'difference_count':len(ids),
          'source_row_count':len(rows),'inventory_count':len(report['inventory']),
          'errors':errors,'scope':'Structural source inspection only; no compilation, rendering, mathematical proof or image comparison.'}
event_id = 'P06' if any(event['id'] == 'P05' for event in report['processing_events']) else 'P05'
report['processing_events'].append({'id':event_id,'type':'structural source validation','inputs':'Complete reading.tex, report.json and existing named crop files.',
    'mapping':'Comment-aware brace/environment/delimiter scans; explicit macro allow-list; file existence; graphic-tag and path-command counts; source-row/local-part identity references; inventory page-position ordering.',
    'result':result,'scope':result['scope'], 'note':'The first allow-list omitted standard bigcup and circ; the second run adds those two standard commands. No TeX repair was required.' if event_id == 'P06' else ''})
(OUT / 'source_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT / 'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
if errors:
    raise SystemExit(1)
