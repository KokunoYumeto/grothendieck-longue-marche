"""Exact monodromy of q^2=lambda and its five-point double-cover family."""
from pathlib import Path
import json
p=Path(__file__).parent
ns={};exec((p/'b_genus_zero.py').read_text().split('\ndata={}')[0],ns)
words={'u0':[2,2],'u1':[1,1,3,3],'um':[2,1,1,3,3,-2]}
result={}
for k,w in words.items():
 c,n=ns['normalized'](4,tuple(w));result[k]=dict(braid=w,central_power=c,normalized_pure_word=n)
 print(k,'braid',w,'central power',c,'normalized pure word',n)
result['covering']='q^2=lambda; pi1(M04)=F(l0,l1), parity(l0)=1, parity(l1)=0; subgroup basis u0=l0^2,u1=l1,um=l0*l1*l0^-1.'
result['family']='Four branch/base marks0,infinity,1,lambda. Take z^2=w, retain infinity and the ordered lifts of1,lambda, forget ramification point0. Result is(infinity,-q,q,-1,1) up to the displayed fixed label order.'
f=p/'b_cover_map.json';t=f.with_suffix('.json.tmp');t.write_text(json.dumps(result,indent=2)+'\n');t.replace(f)
