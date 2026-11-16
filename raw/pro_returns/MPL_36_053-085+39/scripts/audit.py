from pathlib import Path
from datetime import datetime, timezone
import json, csv, runpy
ROOT=Path('/workspace/scratch/b8e2c31cadf4/work')
BASE='MPL_36_053-085+39'
def stamp(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def audit(cote,scan,changes=(),comment='Compared all visible text and marks against the image.',add_elements=()):
    log=(ROOT/'progress.log').read_text()
    assert 'transcription frozen ' not in log
    assert f'{cote} scan {scan:03d} audited ' not in log
    p=ROOT/'pages'/f'{BASE}_{cote}_scan{scan:03d}.tex'
    text=p.read_text()
    for old,new in changes:
        assert old in text, (p.name,old)
        text=text.replace(old,new)
    if changes: p.write_text(text)
    if add_elements:
        rp=ROOT/'records'/f'{cote}_{scan:03d}.json'
        rec=json.loads(rp.read_text());rec['elements'].extend(add_elements)
        rp.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
        rebuild_inventory()
    with (ROOT/'audit_journal.md').open('a') as f:
        f.write(f'\n## {cote} / {scan:03d}\n\n{comment}\n')
        for old,new in changes: f.write(f'\n- Revised `{old}` → `{new}` after visual comparison.\n')
    with (ROOT/'progress.log').open('a') as f:f.write(f'{cote} scan {scan:03d} audited {stamp()}\n')
    rebuild()
    print(f'Audited {cote}/{scan:03d}; {len(changes)} revisions.')
def rebuild_inventory():
    with (ROOT/(BASE+'_inventory.csv')).open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for p in sorted((ROOT/'records').glob('*.json')):
            r=json.loads(p.read_text())
            for n,(kind,pos,words) in enumerate(r['elements'],1):w.writerow([r['cote'],r['scan'],r['sheet_kind'],n,kind,pos,words,'yes'])
def rebuild():
    (ROOT/(BASE+'_transcription.tex')).write_text('\n'.join(p.read_text().rstrip()+'\n' for p in sorted((ROOT/'pages').glob('*.tex'))))
    runpy.run_path(str(ROOT/'scripts'/'build_doubts.py'),run_name='__main__')
