from pathlib import Path
from datetime import datetime,timezone
import sys,json,csv,shutil,subprocess
W=Path(__file__).resolve().parents[1]
page=sys.argv[1]
p=W/'reports'/f'{page}.json'
r=json.loads(p.read_text())
if r.get('adjudicated'): raise SystemExit('Page already committed; use explicit revision.')
r['adjudicated']=True
r['adjudicated_at']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
shutil.copyfile(W/'reports'/f'{page}_draft.tex',W/'pages'/f'{page}.tex')
for suffix,fields in [('boxes',['box','kind','x0','y0','x1','y1']),('first',['box','reading'])]:
    with (W/'second'/f'{page}_{suffix}.tsv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');wr.writeheader();wr.writerows(r.get('second_boxes',[]))
subprocess.run([sys.executable,str(W/'scripts/build_outputs.py')],check=True)
cropcount=len(list((W/'crops').glob(page+'_*')))
with (W/'progress.log').open('a') as f:
    f.write(f"scan {int(r['scan']):03d} done {r['adjudicated_at']} cote {r['cote']}: {r['line_count']} lines read, {cropcount} places cropped, {len(r['changes'])} rows\n")
print(page,'committed')
