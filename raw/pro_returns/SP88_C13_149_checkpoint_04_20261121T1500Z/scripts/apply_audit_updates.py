"""Apply an explicit root adjudication plan; never infer a reading.

Plans contain exact, count-checked text replacements and explicit metadata
patches. Frozen first/second TSV files and their audit-box readings are never
modified. The plan is retained beside the independent readings.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
plan_path = Path(sys.argv[1])
plan = json.loads(plan_path.read_text())
stem = f"149_scan{int(plan['scan']):03d}"
page_path = ROOT / "pages" / f"{stem}.tex"
meta_path = ROOT / "review/accepted" / f"{stem}.json"
text = page_path.read_text()
data = json.loads(meta_path.read_text())
if plan.get('applied'):
    raise SystemExit('Plan already applied.')
for change in plan.get('page_replacements', []):
    old, new = change['old'], change['new']
    expected = change.get('expected_count', 1)
    actual = text.count(old)
    if actual != expected:
        raise ValueError(f"{stem}: expected {expected} occurrences, found {actual}: {old!r}")
    text = text.replace(old, new)
for section, key in [('changes', 'id'), ('decisions', 'id'),
                     ('doubts', 'place'), ('inventory', 'element')]:
    records = data.get(section, [])
    for update in plan.get(section + '_updates', []):
        found = [record for record in records if record.get(key) == update[key]]
        if len(found) != 1:
            raise ValueError(f"{stem}: expected one {section} record {update[key]!r}")
        found[0].update(update['patch'])
    remove = set(plan.get(section + '_remove', []))
    records = [record for record in records if record.get(key) not in remove]
    records.extend(plan.get(section + '_append', []))
    data[section] = records
for section in ['notes', 'hand_observations', 'notation', 'abbreviations', 'checks']:
    data.setdefault(section, []).extend(plan.get(section + '_append', []))
page_path.write_text(text)
meta_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
plan['applied'] = True
plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'scan': plan['scan'], 'text_replacements': len(plan.get('page_replacements', []))}))
