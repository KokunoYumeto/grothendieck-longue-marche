"""Assemble the statement register and complete task ledger from written work."""
import csv
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prompt = (root.parent / 'upload' / 'PROMPT(1).md').read_text()
inventory = []
for match in re.finditer(r'^- \*\*Lead (\d+)[^\n]*', prompt, re.M):
    inventory.append({'item': f'Lead {match[1]}', 'request': match[0]})
part = None
for line in prompt.splitlines():
    match = re.match(r'\*\*([PABCDEFGH])\. ', line)
    if match:
        part = match[1]
    match = re.match(r'(\d+)\. (.*)', line)
    if part and match:
        inventory.append({'item': f'Task {part}.{match[1]}', 'request': match[2]})
    if line == 'RULES OF PROOF (they bind every statement you deliver)':
        part = None
(root / 'notes' / 'task_inventory.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2)+'\n')

rows = []
for path in sorted((root/'notes').glob('*_results.json')):
    content = json.loads(path.read_text())
    rows.extend(content if isinstance(content, list) else content.get('results', []))
seen = set()
for row in rows:
    if row['id'] in seen:
        raise ValueError('Duplicate statement '+row['id'])
    seen.add(row['id'])
    for key in ['depends_on','answers']:
        if isinstance(row.get(key), list):
            row[key] = '; '.join(row[key])
fields = ['id','statement','status','where_proved','depends_on','answers (lead or task)','notes']
part_order = {p:i for i,p in enumerate('PABCDEFGH')}
rows.sort(key=lambda r: (part_order.get(r['id'].split('.')[0],99),
                        int(re.search(r'\d+',r['id'])[0]),r['id']))
# Accept the compact plural forms used by the independent proof sections, and
# keep subpart qualifications in the CSV rather than silently dropping them.
valid_items = {item['item'] for item in inventory}
lead_aliases = {
    'C.1': [8, 9], 'C.2': [10, 24], 'C.7': [11, 25], 'C.8': [11],
    'B.4': [23], 'B.5': [23], 'C.10': [27], 'C.11': [27],
}
def answered_items(row):
    answer = row.get('answers', '')
    items = {'Task '+m[0] for m in re.finditer(r'\b[PABCDEFGH]\.\d+\b', answer)}
    for match in re.finditer(r'\bLeads?\s*(\d+(?:\s*,\s*\d+)*)', answer):
        items.update('Lead '+number.strip() for number in match[1].split(','))
    items.update('Lead '+str(number) for number in lead_aliases.get(row['id'], []))
    return items & valid_items

for row in rows:
    extra = ['Lead '+str(number) for number in lead_aliases.get(row['id'], [])]
    if extra:
        row['answers'] = '; '.join([row.get('answers','')] + extra)
with (root/'LM8_PUSH_results.csv').open('w',newline='') as handle:
    writer = csv.DictWriter(handle,fields,extrasaction='ignore')
    writer.writeheader()
    writer.writerows(dict(r, **{'answers (lead or task)':r.get('answers','')}) for r in rows)

report = ['INCOMPLETE', '', '| Lead or task | Statements | State reached |',
          '|---|---|---|']
for item in inventory:
    matched = [r for r in rows if item['item'] in answered_items(r)]
    if matched:
        ids = ', '.join(r['id'] for r in matched)
        state = '; '.join(r['status']+': '+r['statement'] for r in matched)
    else:
        ids, state = '—', 'Unsettled: no completed argument registered yet.'
    report.append('| '+item['item']+' | '+ids+' | '+state.replace('|','\\|').replace('\n',' ')+' |')
report += ['', '## Status and scope', '',
           'This is an incomplete working return. A proved subsidiary statement does not by itself settle a task whose requested classification remains unfinished. The paper labels each actual assertion separately. No priority is claimed.',
           '', '## Work records', '']
for p in sorted((root/'notes').glob('*.md')):
    if p.name not in {'task_ledger.md'}:
        report += ['### '+p.stem,'',p.read_text(),'']
(root/'LM8_PUSH_report.md').write_text('\n'.join(report)+'\n')
print(json.dumps({'inventory_items':len(inventory),'registered_statements':len(rows),
                  'statuses':{s:sum(r['status']==s for r in rows) for s in sorted({r['status'] for r in rows})},
                  'unmapped_items':[i['item'] for i in inventory
                                    if not any(i['item'] in answered_items(r) for r in rows)]},indent=2))
