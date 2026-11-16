#!/usr/bin/env python3
"""Exact quotient by the original normal elementary-two pc suffix.

The source map kills pc generators105..176. Its kernel has order2^72,
so it induces an isomorphism on integral3-adic homology. No actual lifting
conclusion is made by preparing the quotient or truncating its source rows.
"""
from pathlib import Path
import hashlib,json,math
from pbc_source_coordinate_bounds import coordinate_bounds
b=Path(__file__).resolve().parent
p=b/'pbc_iterated_shortcut_v2_original_source.json';d=json.loads(p.read_text())
cut=104;n=len(d['relative_orders']);assert n==176
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def word(w):return [x for i in range(0,len(w),2) if w[i]<=cut for x in w[i:i+2]]
assert all(e==2 for e in d['relative_orders'][cut:])
assert all(w==[] for w in d['powers'][cut:])
for i,j,w in d['conjugates']:
 if i>cut:assert all(k>cut for k in w[::2])
 if j>cut:assert w==[i,1]
q={'order':math.prod(d['relative_orders'][:cut]),'relative_orders':d['relative_orders'][:cut],
 'powers':[word(w) for w in d['powers'][:cut]],
 'conjugates':[[i,j,word(w)] for i,j,w in d['conjugates'] if i<=cut],
 'quotient_of_sha256':sha(p),'normal_suffix_start':cut+1,'normal_suffix_order':2**(n-cut),
 'normal_suffix_is_elementary_abelian_two':True,
 'scope':'Actual pc quotient, with the canonical original-generator map. Its3-adic H2 is identified with the source by the coprime-kernel homology spectral sequence.'}
for k in ('s','r','f','left_s_frame','left_r_frame','s_image','r_image'):q[k]=word(d[k])
for k in ('s_centralizers','r_centralizers'):q[k]=[word(w) for w in d[k]]
out=b/'pbc_suffix3_original_source.json';out.write_text(json.dumps(q,separators=(',',':'))+'\n')
tokens=iter((b/'pbc_native_smallmod_v1_iterated.dat').read_text().split())
assert int(next(tokens))==n
for _ in range(n):next(tokens)
def readword():return [int(next(tokens)) for _ in range(int(next(tokens)))]
for _ in range(n+n*(n-1)//2):readword()
assert next(tokens)==sha(p)
oldmod=int(next(tokens));sc=int(next(tokens));rc=int(next(tokens))
for _ in range(n*(n+1)//2):next(tokens)
target=readword();extras=[readword() for _ in range(sc+rc+2)]
assert next(tokens,None) is None
tails=cut*(cut+1)//2
def tail(w):return [x for i in range(0,len(w),2) if w[i]<=tails for x in w[i:i+2]]
initial={'source_sha256':sha(out),'target':tail(target),'extras':[tail(w) for w in extras],
 'projection':'The triangular positive collector cannot alter lower generator or tail coordinates when higher generators are omitted. These initial rows will also be independently recollected.'}
(b/'pbc_suffix3_initial_rows.json').write_text(json.dumps(initial,separators=(',',':'))+'\n')
bounds,_=coordinate_bounds(q);modulus=3**8;bounds=[math.gcd(x,modulus) for x in bounds]
dest=b/'pbc_suffix3_primary.dat'
def emit(f,w):f.write(' '.join(map(str,[len(w)]+w))+'\n')
with dest.open('w') as f:
 f.write(str(cut)+'\n'+' '.join(map(str,q['relative_orders']))+'\n')
 for w in q['powers']:emit(f,w)
 for i,j,w in q['conjugates']:emit(f,w)
 f.write(sha(out)+'\n'+str(modulus)+'\n'+str(sc)+' '+str(rc)+'\n'+' '.join(map(str,bounds))+'\n')
 emit(f,initial['target'])
 for w in initial['extras']:emit(f,w)
report={'original_source_sha256':sha(p),'quotient_source_sha256':sha(out),'input_sha256':sha(dest),
 'original_group_order':d['order'],'quotient_order':q['order'],'kernel_order':q['normal_suffix_order'],
 'kernel_normal_and_elementary_two_from_all_original_pc_relations':True,
 'source_generators':n,'quotient_generators':cut,'quotient_tails':tails,'modulus':modulus,
 'target_and_frames_are_actual_projected_words':True,
 'homology_comparison':'H_i(G,Z3) -> H_i(G/N,Z3) is an isomorphism for everyi because N is a finite2-group.',
 'scope':'Preparation and homology comparison only. No success claim; full independent target/source replay is still required.'}
(b/'pbc_suffix3_quotient_provenance.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
# Independent full search, retaining only the permitted order-three corrections.
s=(b/'pbc_native_primary_search.cpp').read_text()
s=s.replace('#include "pbc_positive_collector_control.hpp"','#include "pbc_positive_collector_bits.hpp"')
s=s.replace('Collector c;int n,m,','BitCollector c;int n,m,')
s=s.replace('c.max_steps_per_collection=2000000;','c.max_steps_per_collection=20000000;')
s=s.replace('for(int i=2;i<extra_count;i++){Weights w(extra_count,0);','for(int i=2+s_count;i<extra_count;i++){Weights w(extra_count,0);')
s=s[:s.index('int main(int argc,char**argv)')]+'''int main(int argc,char**argv){
 assert(argc==4);std::signal(SIGUSR1,PBCSignal);std::signal(SIGUSR2,PBCSignal);std::signal(SIGINT,PBCSignal);std::signal(SIGTERM,PBCSignal);
 std::ifstream in(argv[1]);assert(in);
 try{Witness w(in,argv[2],argv[3]);w.run();}
 catch(const PBCStopped&){std::cerr<<"native_GRACEFUL_STOP_incomplete_search_valid_gzip_footer"<<std::endl;return130;}
 return0;
}
'''.replace('return130','return 130').replace('return0','return 0')
(b/'pbc_suffix3_native_search.cpp').write_text(s)
