#!/usr/bin/env python3
"""Prepare exact ORIGINAL-presentation positive words for the native collector."""
import argparse,hashlib,json
from pathlib import Path

def load_source(path):
 d=json.loads(path.read_text())
 n=len(d['relative_orders'])
 if 'conjugates_nested' in d:
  con=d['conjugates_nested']
 else:
  con=[[] for _ in range(n)]
  for i,j,w in d['conjugates']:
   while len(con[i-1])<j:con[i-1].append(None)
   con[i-1][j-1]=w
 return d,con

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('source',type=Path)
 ap.add_argument('output',type=Path)
 ap.add_argument('--trace',type=Path)
 args=ap.parse_args()
 d,con=load_source(args.source);n=len(d['relative_orders'])
 power=[None]*(n+1);conj=[[None]*(n+1) for _ in range(n+1)]
 k=n
 for i in range(1,n+1):
  k+=1;power[i]=d['powers'][i-1]+[k,1]
  for j in range(1,i):
   k+=1;conj[i][j]=con[i-1][j-1]+[k,1]
 s,r=d['s'],d['r'];bs,br=d['left_s_frame'],d['left_r_frame']
 sim,rim=d['s_image'],d['r_image']
 cs,cr=d['s_centralizers'],d['r_centralizers']
 extras=[(s+s,[]),(r+r+r,[])]+[(a+s,s+a) for a in cs]+[(a+r,r+a) for a in cr]
 tasks=[('target_s',bs+s,sim+bs),('target_r',br+r,rim+br),('target_product',sim+rim,s+r)]
 expected={};task_kinds={};excluded_exterior=0
 if args.trace:
  for line in args.trace.read_text().splitlines():
   row=json.loads(line)
   if row[0]!='leaf':continue
   _,node,kind,meta,value=row
   label=f'leaf_{node}'
   if kind=='target':
    expected['target']=value;continue
   if kind=='extra':
    lhs,rhs=extras[meta[0]-1]
   elif kind=='identity':
    typ,*indices=meta
    if typ==2:
     # The retained exterior row is a bilinear combination of original
     # identities, not the single raw associativity word below.
     # Its standard replay is already checked separately; omit it
     # from this equality-of-collector-normal-forms test.
     excluded_exterior+=1;continue
    if typ in (1,2):
     i,j,k=indices
     lhs=[k,1,i,1]+conj[j][i]
     rhs=[j,1]+conj[k][j]+[i,1]
    elif typ==3:
     i,j=indices
     lhs=[j,d['relative_orders'][j-1]-1,i,1]+conj[j][i]
     rhs=power[j]+[i,1]
    elif typ==4:
     i,k=indices
     lhs=[k,1]+power[i]
     rhs=[i,1]+conj[k][i]+[i,d['relative_orders'][i-1]-1]
    elif typ==5:
     i,=indices;lhs=power[i]+[i,1];rhs=[i,1]+power[i]
    else:raise ValueError(meta)
   else:raise ValueError(kind)
   tasks.append((label,lhs,rhs));expected[label]=value;task_kinds[label]=[kind,meta]
 else:
  tasks.extend((f'extra_{i+1}',*words) for i,words in enumerate(extras))
 def emitword(f,w):
  assert len(w)%2==0 and all(x>0 for x in w)
  f.write(' '.join(map(str,[len(w)]+w))+'\n')
 with args.output.open('w') as f:
  f.write(str(n)+'\n'+' '.join(map(str,d['relative_orders']))+'\n')
  for w in d['powers']:emitword(f,w)
  for i in range(1,n):
   for j in range(i):emitword(f,con[i][j])
  f.write(str(len(tasks))+'\n')
  for name,lhs,rhs in tasks:
   f.write(name+'\n');emitword(f,lhs);emitword(f,rhs)
 provenance={'source':str(args.source),'source_sha256':hashlib.sha256(args.source.read_bytes()).hexdigest(),
             'input_sha256':hashlib.sha256(args.output.read_bytes()).hexdigest(),'tasks':len(tasks),
             'base_generators':n,'formal_central_tails':n*(n+1)//2,'expected':expected,
             'task_kinds':task_kinds,'excluded_exterior_bilinear_rows':excluded_exterior}
 args.output.with_suffix('.inputs.json').write_text(json.dumps(provenance,indent=2)+'\n')
 print(json.dumps({k:v for k,v in provenance.items() if k not in ('expected','task_kinds')}))

if __name__=='__main__':main()
