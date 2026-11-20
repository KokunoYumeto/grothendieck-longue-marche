"""Snapshot the next page's brief/notation before the main launches fresh readers."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,shutil,sys
O=Path(__file__).resolve().parents[1];ROOT=O.parent;n=int(sys.argv[1]);brief=sys.argv[2]
prior=[int(p.stem[4:]) for p in sorted((O/'decisions').glob('scan[0-9][0-9][0-9].json')) if json.loads(p.read_text()).get('committed')]
assert prior==list(range(6,n)),prior
p=ROOT/f'packets/scan{n:03}'
assert p.exists()
shutil.copyfile(O/'notation.md',p/'notation.md');shutil.copyfile(O/'briefs'/brief,p/'brief.md')
snapshot=O/f'briefs/notation_scan{n:03}.md'
assert not snapshot.exists(),'Do not replace the notation supplied to an earlier trio'
shutil.copyfile(O/'notation.md',snapshot)
with (O/'reader_runs.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for i in range(1,4):
        (O/f'readers/scan{n:03}/R{i}').mkdir(parents=True,exist_ok=True)
        w.writerow([n,f'R{i}',f'/root/scan{n:03}_r{i}',f'briefs/{brief}',f'briefs/notation_scan{n:03}.md',f'packets/scan{n:03}','fork_turns=none; no other page or reader supplied'])
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (O/'progress.log').open('a') as f:f.write(f'scan {n:03} reader packet prepared {stamp}; brief {brief}\n')
print(f'Prepared scan {n:03}, preserving notation snapshot. Launch three fresh independent readers now.')
