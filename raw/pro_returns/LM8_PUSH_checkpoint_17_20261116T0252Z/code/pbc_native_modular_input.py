#!/usr/bin/env python3
"""Serialize an original pc source and already replayed raw target/extra rows."""
import argparse,gzip,hashlib,json,math
from pathlib import Path
from pbc_native_collector_input import load_source
from pbc_source_coordinate_bounds import coordinate_bounds

ap=argparse.ArgumentParser()
ap.add_argument('source',type=Path)
ap.add_argument('initial',type=Path)
ap.add_argument('output',type=Path)
ap.add_argument('--trace',action='store_true')
args=ap.parse_args()
d,con=load_source(args.source);n=len(d['relative_orders'])
count=len(d['s_centralizers'])+len(d['r_centralizers'])+2
if args.trace:
    target=None;extras=[[] for _ in range(count)];seen=set()
    opener=gzip.open if args.initial.suffix=='.gz' else open
    with opener(args.initial,'rt') as stream:
        for line in stream:
            row=json.loads(line)
            if row[0]!='leaf':continue
            if row[2]=='target':target=row[4]
            elif row[2]=='extra':extras[row[3][0]-1]=row[4];seen.add(row[3][0])
            if target is not None and len(seen)==count-2:break
    assert seen==set(range(3,count+1)) and target is not None
else:
    raw=json.loads(args.initial.read_text());target=raw['target'];extras=raw['extras']
    assert raw['source_sha256']==hashlib.sha256(args.source.read_bytes()).hexdigest()
    assert len(extras)==count
bounds,proofs=coordinate_bounds(d)
def word(out,v):out.write(' '.join(map(str,[len(v)]+v))+'\n')
with args.output.open('w') as out:
    out.write(str(n)+'\n'+' '.join(map(str,d['relative_orders']))+'\n')
    for v in d['powers']:word(out,v)
    for i in range(1,n):
        for j in range(i):word(out,con[i][j])
    out.write(hashlib.sha256(args.source.read_bytes()).hexdigest()+'\n')
    out.write(str(math.prod(d['relative_orders']))+'\n')
    out.write(f"{len(d['s_centralizers'])} {len(d['r_centralizers'])}\n")
    out.write(' '.join(map(str,bounds))+'\n')
    word(out,target)
    for v in extras:word(out,v)
meta={'source':str(args.source),'initial_rows':str(args.initial),'input':str(args.output),
      'source_sha256':hashlib.sha256(args.source.read_bytes()).hexdigest(),
      'input_sha256':hashlib.sha256(args.output.read_bytes()).hexdigest(),
      'generators':n,'tails':n*(n+1)//2,'s_count':len(d['s_centralizers']),
      'r_count':len(d['r_centralizers']),'proper_coordinate_bounds':len(proofs),
      'forbidden_power_rows_not_inserted':True}
args.output.with_suffix('.inputs.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
