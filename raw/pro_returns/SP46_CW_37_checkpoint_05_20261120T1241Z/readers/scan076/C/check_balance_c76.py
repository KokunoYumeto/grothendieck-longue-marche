from pathlib import Path
import json, re

root = Path('/workspace/scratch/006c0e32b2af/out/readers/scan076/C')
raw = (root/'reading.tex').read_text()
text = '\n'.join(re.split(r'(?<!\\)%', line)[0] for line in raw.splitlines())
stack = []
errors = []
for m in re.finditer(r'(?<!\\)[{}]',text):
    if m.group() == '{':
        stack.append(m.start())
    elif stack:
        stack.pop()
    else:
        errors.append(f'Unmatched closing brace at {m.start()}')
if stack:
    errors.append(f'Unmatched opening braces: {stack}')
envs = []
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',text):
    if m.group(1) == 'begin':
        envs.append(m.group(2))
    elif not envs or envs.pop() != m.group(2):
        errors.append(f'Environment mismatch at {m.start()}')
if envs:
    errors.append(f'Unclosed environments: {envs}')
for left,right in ((r'\(',r'\)'),(r'\[',r'\]')):
    if text.count(left) != text.count(right):
        errors.append(f'Math delimiter mismatch {left} {right}')
if len(re.findall(r'(?<!\\)\$',text)) % 2:
    errors.append('Odd count of dollar delimiters')
report = json.loads((root/'report.json').read_text())
required = ['scan','reader','image_views','reading_path','crops','decisions','inventory','notes','math_reading_decisions','check_events','notation','abbreviations','slips','completion']
for key in required:
    if key not in report:
        errors.append(f'Missing report key: {key}')
for d in report['decisions']:
    if d['h_reading'] is not None or d['diff_h']:
        errors.append(f'Invalid H collation in {d["id"]}')
    if len(d['bbox']) != 4:
        errors.append(f'Invalid bbox in {d["id"]}')
for r in report['crops']:
    if not Path(r['file']).exists():
        errors.append(f'Missing crop {r["file"]}')
result = {'scan':76,'reader':'C','method':'Static delimiter, environment and JSON checks only; no TeX engine','balanced':not errors,'errors':errors,'decisions':len(report['decisions']),'c_doubt_rows':sum(d['c_doubt'] for d in report['decisions']),'source_views':len(report['image_views']),'crops':len(report['crops'])}
(root/'balance_check_c76.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
if not errors:
    report['completion'] = report['completion'].replace('Balance checks, without TeX compilation, follow file creation.','Static brace, math-delimiter and environment checks passed after writing; report JSON and all evidence paths also validated. No TeX compilation was attempted.')
    (root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
