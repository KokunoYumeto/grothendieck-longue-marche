"""Focused diagonal S3xS3 obstruction using the actual marginal words.

Both factors are required to be surjective and individually preserved by
all eleven old actions, with a common implementing inner conjugator. This
does not exhaust factor-swapping normalizers or other finite quotients.
"""
from pathlib import Path
import itertools,json,subprocess
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'positive_fiber_data.json').read_text())
P=list(itertools.permutations(range(3)));ind={p:i for i,p in enumerate(P)}
def mul(p,q):return tuple(p[q[j]] for j in range(3))
M=[[ind[mul(p,q)] for q in P] for p in P]
I=[ind[tuple(p.index(j) for j in range(3))] for p in P]
odd=[i for i,p in enumerate(P) if sum(p[j]!=j for j in range(3))==2]
A=[[D['old_actions'][str(i)][str(j)] for j in range(1,8)] for i in range(11)]
F=[D['new_fiber_words'][str(i)] for i in range(11,19)]
order=sorted(range(11),key=lambda i:sum(map(len,A[i])))
def cpp(x):return '{'+','.join(map(cpp,x))+'}' if isinstance(x,list) else str(x)
src=r'''
#include <array>
#include <iostream>
#include <vector>
using namespace std;
const int M[6][6]=@M@,I[6]=@I@;
const vector<int> ODD=@ODD@,ORDER=@ORDER@;
const vector<vector<int>>F=@F@;
const vector<vector<vector<int>>>A=@A@;
int ev(const vector<int>&w,const array<int,7>&p){int r=0;for(int x:w)r=M[r][x>0?p[x-1]:I[p[-x-1]]];return r;}
int main(){
  int total=1;for(int j=0;j<7;j++)total*=6;
  for(int n=0;n<total;n++){
    int v=n;array<int,7>p;array<int,11>q;bool has_odd=false;
    for(int j=0;j<7;j++){p[j]=v%6;v/=6;for(int o:ODD)has_odd|=p[j]==o;}
    if(!has_odd)continue;
    bool cyclic=false;for(int o:ODD){bool inside=true;for(int x:p)inside&=(x==0||x==o);cyclic|=inside;}
    if(cyclic)continue;
    bool ok=true;
    for(int i:ORDER){
      int mask=63;
      for(int j=0;j<7&&mask;j++){
        int e=ev(A[i][j],p);
        for(int h=0;h<6;h++)if((mask>>h)&1)if(M[M[h][p[j]]][I[h]]!=e)mask&=~(1<<h);
      }
      if(!mask){ok=false;break;}
      if(mask&(mask-1))return 2;
      q[i]=__builtin_ctz((unsigned)mask);
    }
    if(ok){for(int x:p)cout<<x<<' ';for(const auto&w:F)cout<<ev(w,p)<<' ';for(int x:q)cout<<x<<' ';cout<<'\n';}
  }
}
'''
for n,x in {'M':M,'I':I,'ODD':odd,'ORDER':order,'F':F,'A':A}.items():src=src.replace('@'+n+'@',cpp(x))
(HERE/'check_paired_S3_source.cpp').write_text(src)
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'check_paired_S3_source.cpp'),'-o',str(HERE/'check_paired_S3_source.bin')],check=True)
r=subprocess.run([str(HERE/'check_paired_S3_source.bin')],capture_output=True,text=True,check=True)
(HERE/'paired_S3_eligible_representations.txt').write_text(r.stdout)
rows=[tuple(map(int,line.split())) for line in r.stdout.splitlines()]
assert all(len(row)==26 for row in rows)
print('Surjective S3 representations invariant up to inner automorphism under all11 actual actions:',len(rows))
buckets={}
for row in rows:buckets.setdefault(row[7:],[]).append(row[:7])
print('Buckets with identical8 seed images and11 literal implementing conjugators:',len(buckets))
def evalword(w,p):
    r=0
    for x in w:r=M[r][p[x-1] if x>0 else I[p[-x-1]]]
    return r
def pairmul(a,b):return (M[a[0]][b[0]],M[a[1]][b[1]])
def pairinv(a):return (I[a[0]],I[a[1]])
tested=0;witness=None
for key,pp in buckets.items():
    for p,q in itertools.combinations(pp,2):
        tested+=1;generators=[(p[j],q[j]) for j in range(7)]
        seen={(0,0):()};todo=[(0,0)]
        for at in todo:
            for j,g in enumerate(generators,1):
                end=pairmul(at,g)
                if end not in seen:seen[end]=seen[at]+(j,);todo.append(end)
        for g,word in seen.items():
            for j in (1,3,5,7):
                h=pairmul(pairmul(g,generators[j-1]),pairinv(g))
                if h[0]!=h[1]:
                    detected=word+(j,)+tuple(-x for x in reversed(word))
                    witness={'plus':p,'minus':q,'seed_images':key[:8],'source_conjugators':key[8:],
                             'detected_word':detected,'detected_images':h,'permutations':P}
                    break
            if witness:break
        if witness:break
    if witness:break
print('Paired candidates checked:',tested)
if witness:
    p,q=witness['plus'],witness['minus']
    for i in range(11):
        h=witness['source_conjugators'][i]
        for j in range(7):
            assert evalword(A[i][j],p)==M[M[h][p[j]]][I[h]]
            assert evalword(A[i][j],q)==M[M[h][q[j]]][I[h]]
    for w in F:assert evalword(w,p)==evalword(w,q)
    assert evalword(witness['detected_word'],p)!=evalword(witness['detected_word'],q)
    (HERE/'paired_S3_source_witness.json').write_text(json.dumps(witness,indent=2)+'\n')
    print('WITNESS',json.dumps(witness))
else:
    print('NO_WITNESS in the stated fixed-factor S3xS3 class. No source-image equality follows.')
(HERE/'paired_S3_source_summary.json').write_text(json.dumps({'eligible':len(rows),'buckets':len(buckets),'paired_candidates':tested,'witness':bool(witness),'scope':__doc__},indent=2)+'\n')

