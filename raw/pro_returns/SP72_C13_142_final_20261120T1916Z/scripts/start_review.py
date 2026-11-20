from pathlib import Path
import json, sys, subprocess, shutil

out=Path(__file__).resolve().parents[1]
n=int(sys.argv[1])
src=out/'readers'/f'scan{n:03}'
dest=out/'documentation/reviews'/f'scan{n:03}'
dest.mkdir(parents=True,exist_ok=True)
if (dest/'report.json').exists():raise SystemExit('Review exists: continue that review.')
r=json.loads((src/'report.json').read_text())
manifest=[json.loads(s) for s in (out/'crops/crop_manifest.jsonl').read_text().splitlines()]
manifest=[m for m in manifest if m['scan']==n]
todo=[]
for c in r['changes']:
    if not (c.get('c_changed') or c.get('h_changed')):continue
    if c.get('crop') and c['crop']!='page':continue
    box=c.get('box')
    if not box:raise ValueError('Missing box '+c['id'])
    matches=[m for m in manifest if m['box'][0]<=box[0] and m['box'][1]<=box[1] and m['box'][2]>=box[2] and m['box'][3]>=box[3]]
    if matches:
        chosen=min(matches,key=lambda m:(m['box'][2]-m['box'][0])*(m['box'][3]-m['box'][1]))
        c['crop']=chosen['file']
        c['evidence_crop_box']=chosen['box']
    else:
        place='root_'+c['id']
        args=[sys.executable,str(out/'scripts/crop.py'),str(n),place,*map(str,box)]
        if (box[3]-box[1]) > 12*(box[2]-box[0]): args.extend(['--rotate','90'])
        subprocess.run(args,check=True,stdout=subprocess.DEVNULL)
        manifest=[json.loads(s) for s in (out/'crops/crop_manifest.jsonl').read_text().splitlines() if s.strip()]
        manifest=[m for m in manifest if m['scan']==n]
        c['crop']=f'crops/scan{n:03}_{place}.jpg'
        todo.append(c['crop'])
(dest/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
shutil.copyfile(src/'proposed.tex',dest/'page.tex')
print(json.dumps({'scan':n,'new_crops':todo,'all_crops':sorted(set(c['crop'] for c in r['changes'] if c.get('crop') and c['crop']!='page'))},ensure_ascii=False,indent=2))
