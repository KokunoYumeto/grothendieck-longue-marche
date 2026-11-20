"""Record one fresh three-reader assignment, enforcing archive order."""
from pathlib import Path
import argparse,json,shutil,subprocess
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parents[1];ROOT=OUT.parent
p=argparse.ArgumentParser();p.add_argument('stem');p.add_argument('brief');a=p.parse_args()
rows=json.loads((ROOT/'work/page_map.json').read_text());stems=[Path(x['codex_file']).stem for x in rows];idx=stems.index(a.stem)
if idx and not (OUT/'decisions'/(stems[idx-1]+'.json')).exists():raise RuntimeError('Previous page has not been adjudicated')
subprocess.run(['python',str(OUT/'scripts/refresh_prior_questions.py'),a.stem],check=True)
for r in ['r1','r2','r3']:(OUT/'readers'/a.stem/r/'crops').mkdir(parents=True,exist_ok=True)
(OUT/'notation_snapshots').mkdir(exist_ok=True)
snap=OUT/'notation_snapshots'/(a.stem+'.md')
shutil.copyfile(OUT/'notation.md',snap);shutil.copyfile(snap,ROOT/'work'/a.stem/'notation_snapshot.md')
assignment={'stem':a.stem,'brief':a.brief,'notation_snapshot':str(snap.relative_to(OUT)),'meta':json.loads((ROOT/'work'/a.stem/'meta.json').read_text()),'reader_policy':'three new independent agents; one page only; no other reader output','assigned_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}
(OUT/'readers'/a.stem/'assignment.json').write_text(json.dumps(assignment,ensure_ascii=False,indent=2))
print(json.dumps(assignment,ensure_ascii=False))
