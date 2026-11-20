from pathlib import Path
import sys,json,shutil,datetime
out=Path(__file__).resolve().parents[1];base=out.parent
key,version=sys.argv[1:3]
order=json.loads((out/'page_order.json').read_text())
keys=[f"{r['cote']}_{int(r['our_scan']):03d}" for r in order]
i=keys.index(key)
if i and not (out/'decisions'/(keys[i-1]+'.json')).exists():raise SystemExit('Previous page has not been adjudicated.')
if i:
    prev=order[i-1]
    if not any(line.startswith(f"scan {int(prev['our_scan']):03d} done ") and f"cote {prev['cote']}" in line for line in (out/'progress.log').read_text().splitlines()):raise SystemExit('Previous page has not yet been saved and marked done.')
snapshot=out/'briefs'/('notation_for_'+key+'.md')
shutil.copy(out/'notation.md',snapshot)
for r in ['R1','R2','R3']:
    p=out/'readers'/key/r;p.mkdir(parents=True,exist_ok=True)
    text=f'''# Assignment {key} — {r}

Read ONE page independently. Execute {out}/briefs/brief_{version}.md in full.
Packet: {base}/page_packets/{key}. Read its metadata for the three images.
Notation snapshot: {snapshot}.
Output directory: {p}.
Reader identity: {r}. Use no other reader's files and no previous pages or outside sources. Do not delegate. View whole once, each half once, then one own tight crop per open place; no OCR. Write reading.tex, report.json, crops and inspection log. Finish this page fully before returning.
'''
    (p/'assignment.md').write_text(text)
with (out/'progress.log').open('a') as f:f.write(f'{key}: reader assignments prepared; brief {version}; {datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")}\n')
print(key,version,snapshot)
