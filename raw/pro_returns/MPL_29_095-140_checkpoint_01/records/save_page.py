"""Save a manually transcribed page and its hand-checked inventory (no OCR)."""
import csv
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def save_page(scan, tex, elements, doubts=(), leads=(), sheet_kind='text'):
    target = ROOT / 'pages' / f'MPL_29_095-140_29_scan{scan:03}.tex'
    if target.exists():
        raise RuntimeError(f'Page already saved: {target}')
    target.write_text(tex.strip() + '\n', encoding='utf-8')
    with (ROOT / 'MPL_29_095-140_inventory.csv').open('a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for n, (kind, position, first) in enumerate(elements, 1):
            writer.writerow([29, scan, sheet_kind, f'{scan:03}-{n:02}', kind, position, first, 'yes'])
    with (ROOT / 'MPL_29_095-140_doubts.md').open('a', encoding='utf-8') as f:
        for place, reading, alternative, confidence in doubts:
            values = [29, scan, place, reading, alternative, confidence]
            f.write('| ' + ' | '.join(str(v).replace('|', '\\|').replace('\n', ' ') for v in values) + ' |\n')
    with (ROOT / 'records/research_leads.md').open('a', encoding='utf-8') as f:
        for lead in leads:
            f.write(f'\n- Scan {scan:03}: {lead}\n')
    record = {'scan': scan, 'sheet_kind': sheet_kind, 'elements': elements, 'doubts': doubts, 'leads': leads}
    (ROOT / 'records' / f'{scan:03}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT / 'progress.log').open('a', encoding='utf-8') as f:
        f.write(f'29 scan {scan:03} done {now}\n')
    print(f'Saved scan {scan:03}: {len(elements)} inventory elements, {len(doubts)} doubt entries. {now}')
