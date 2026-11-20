from pathlib import Path
import json,sys,csv,datetime,shutil,subprocess
O=Path(__file__).resolve().parents[1];p=sys.argv[1];reader=sys.argv[2]
rpath=O/'work'/f'{p}_decided.json'
r=json.loads(rpath.read_text() if rpath.exists() else (O/'work'/f'{p}_report.json').read_text())
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');r['decided_utc']=now;r['first_reader']=reader
for c in r['changes']:
 if c.get('crop'):c['crop']='crops/'+Path(c['crop']).name
 if c.get('supporting_crops'):c['supporting_crops']=['crops/'+Path(p).name for p in c['supporting_crops']]
for i in r['inventory']:
 if i.get('sheet_kind','').startswith('typescript'):i['sheet_kind']='typescript'
 if i.get('kind') not in ['text','display','diagram','drawing','margin note','insertion','deletion']:i['kind']='text'
valid=['targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found']
kept_events=[]
for e in r.get('check_events',[]):
 if 'visual transcription check only' in e.get('outcome','').lower() or (e.get('type') not in valid and not e.get('type','').startswith('refuted')):
  r.setdefault('visual_audit_events',[]).append(e)
 else:kept_events.append(e)
r['check_events']=kept_events
rpath.write_text(json.dumps(r,ensure_ascii=False,indent=2))
page=O/'pages'/f'{p}.tex'
if not page.exists():shutil.copyfile(O/'work'/f'{p}_draft.tex',page)
for suffix,headers in [('boxes',['box','kind','x0','y0','x1','y1']),('first',['box','reading'])]:
 with (O/'second'/f'{p}_{suffix}.tsv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=headers,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(r.get('boxes',[]))
subprocess.run([sys.executable,str(O/'scripts/assemble.py')],check=True)
with (O/'progress.log').open('a') as f:
 f.write(f"{p}: scan {p.rsplit('scan',1)[1]} done {now}: {r['line_count']} lines read, {len(list((O/'crops').glob(p+'*.png')))} places cropped, {len(r['changes'])} rows; first reader {reader}; primary reviewed return and saved evidence.\n")
print(p,'committed')
