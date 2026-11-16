from pathlib import Path
import csv, datetime, json, sys
root=Path(__file__).resolve().parents[1]
cote, scan=sys.argv[1], int(sys.argv[2])
stem=f'MPL_22+23_002-016_{cote}_scan{scan:03d}'
page=root/'pages'/f'{stem}.tex'
assert page.exists()
meta=json.loads((root/'records'/f'{stem}.json').read_text())
inv=root/'MPL_22+23_002-016_inventory.csv'
fields=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
existing=[]
if inv.exists():
    with inv.open(newline='') as f: existing=list(csv.DictReader(f))
assert not any(r['cote']==cote and int(r['scan'])==scan for r in existing), 'Already committed'
with inv.open('a',newline='') as f:
    w=csv.writer(f)
    if not existing: w.writerow(fields)
    for i,(kind,position,words) in enumerate(meta['elements'],1):
        w.writerow([cote,f'{scan:03d}',meta['sheet_kind'],f'{cote}-{scan:03d}-{i:02d}',kind,position,words,'yes'])
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'{cote} scan {scan:03d} done {now}\n')
print(f'{cote} scan {scan:03d} done {now}; {len(meta["elements"])} inventory elements')
