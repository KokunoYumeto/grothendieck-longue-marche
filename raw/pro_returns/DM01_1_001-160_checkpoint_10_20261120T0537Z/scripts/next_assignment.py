#!/usr/bin/env python3
"""Read-only page allocation: 3 readers at >=18 marks, 2 at >=6, otherwise 1."""
from pathlib import Path
import argparse,json,math
from reconcile import Project
parser=argparse.ArgumentParser()
parser.add_argument('--workspace',type=Path,default=Path.cwd())
parser.add_argument('--scan',type=int)
parser.add_argument('--threshold',type=int,default=6,help='Minimum marks for two readers')
parser.add_argument('--three-threshold',type=int,default=18,help='Minimum marks for three readers')
parser.add_argument('--readers',type=int,choices=[1,2,3],help='Override automatic reader count')
args=parser.parse_args()
p=Project(args.workspace)
receipts=p.receipts()
if args.scan is None:
    if len(receipts)==len(p.scans_order):
        print(json.dumps({'complete':True,'marks':len(p.marks_rows),'pages':len(receipts)}))
        raise SystemExit
    scan=p.scans_order[len(receipts)]
else:
    scan=args.scan
marks=p.marks[scan]
count=len(marks)
readers=args.readers or (3 if count>=args.three_threshold else 2 if count>=args.threshold else 1)
cuts=[0]
for group in range(1,readers):
    cut=math.ceil(count*group/readers)
    while cut<count and marks[cut].parent is not None:
        cut+=1
    if cut<=cuts[-1] or cut>=count:
        raise ValueError('Requested partition cannot keep all nested marks together; use fewer readers')
    cuts.append(cut)
cuts.append(count)
parts=[marks[a:b] for a,b in zip(cuts,cuts[1:])]
print(json.dumps({'scan':scan,'count':count,'reader_count':len(parts),'parts':[
    {'suffix':chr(97+i) if len(parts)>1 else '', 'count':len(part),
     'first':part[0].id,'last':part[-1].id,'ids':[m.id for m in part]}
    for i,part in enumerate(parts)]},ensure_ascii=False))
