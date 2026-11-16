"""Generate and run an exact, restricted four-sheet cover obstruction search.

The peripheral images are restricted to identity or transpositions in S4.
A witness would separate the actual marginal source subgroup from its normal
closure.  Failure is only a bounded negative search and proves no equality.
"""
from pathlib import Path
import itertools,json,subprocess,time
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'positive_fiber_data.json').read_text())
perms=list(itertools.permutations(range(4)))
idx={p:i for i,p in enumerate(perms)}
def mul(p,q): return tuple(p[q[i]] for i in range(4))
def inv(p): return tuple(p.index(i) for i in range(4))
M=[[idx[mul(p,q)] for q in perms] for p in perms]
I=[idx[inv(p)] for p in perms]
choices=[i for i,p in enumerate(perms) if sum(p[j]!=j for j in range(4)) in (0,2)]
stabilizer=[i for i,p in enumerate(perms) if p[0]==0]
def involution_reduce(w):
    ans=[]
    for x in w:
        x=abs(x)-1
        if ans and ans[-1]==x: ans.pop()
        else: ans.append(x)
    return ans
F=[involution_reduce(D['new_fiber_words'][str(i)]) for i in range(11,19)]
A=[[involution_reduce(D['old_actions'][str(i)][str(j)]) for j in range(1,8)] for i in range(11)]
order=sorted(range(11),key=lambda i:sum(map(len,A[i])))
def cpp(x):
    if isinstance(x,list):return '{'+','.join(map(cpp,x))+'}'
    return str(x)
source=r'''
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
const int M[24][24]=@M@;
const int I[24]=@I@;
const int P[24][4]=@P@;
const vector<int> CH=@CH@, ST=@ST@, ORDER=@ORDER@;
const vector<vector<int>> F=@F@;
const vector<vector<vector<int>>> A=@A@;
int eval(const vector<int>&w,const array<int,7>&p){int r=0;for(int x:w)r=M[r][p[x]];return r;}
bool connected(const array<int,7>&p){
  bool reached[4]={true,false,false,false};
  for(int k=0;k<4;k++)for(int a:p)for(int i=0;i<4;i++)if(reached[i])reached[P[a][i]]=true;
  return reached[0]&&reached[1]&&reached[2]&&reached[3];
}
int main(){
  uint64_t tested=0,transitive=0,fiber_ok=0,old_pass[12]={};
  array<int,7> p; array<int,11> q;
  auto start=chrono::steady_clock::now();
  uint64_t total=1;for(int j=0;j<7;j++)total*=CH.size();
  cout<<"choices "<<CH.size()<<" tuples "<<total<<" action_order";
  for(int a:ORDER)cout<<' '<<a;cout<<endl;
  for(uint64_t n=0;n<total;n++){
    uint64_t v=n;for(int j=0;j<7;j++){p[j]=CH[v%CH.size()];v/=CH.size();}
    tested++;
    if(P[p[6]][0]!=0 || !connected(p))continue;
    bool any_killed=false;for(int j:{0,2,4,6})any_killed|=p[j]!=0;
    if(!any_killed)continue;
    transitive++;
    bool ok=true;
    for(const auto&w:F)if(P[eval(w,p)][0]!=0){ok=false;break;}
    if(!ok)continue;fiber_ok++;old_pass[0]++;
    for(int oi=0;oi<11;oi++){
      int a=ORDER[oi],mask=63;
      for(int j=0;j<7 && mask;j++){
        int e=eval(A[a][j],p);
        for(int k=0;k<6;k++)if((mask>>k)&1){int z=ST[k];if(M[M[z][p[j]]][I[z]]!=e)mask&=~(1<<k);}
      }
      if(!mask){ok=false;break;}
      q[a]=ST[__builtin_ctz((unsigned)mask)];old_pass[oi+1]++;
    }
    if(ok){
      cout<<"WITNESS peripherals";for(int a:p)cout<<' '<<a;cout<<" source";for(int a:q)cout<<' '<<a;cout<<endl;
      return 0;
    }
  }
  cout<<"NO_WITNESS_IN_RESTRICTED_CLASS tested "<<tested<<" transitive_nontrivial_normal "<<transitive<<" fiber_ok "<<fiber_ok<<endl;
  cout<<"successive_old_action_passes";for(int k=0;k<12;k++)cout<<' '<<old_pass[k];cout<<endl;
  cout<<"elapsed_seconds "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
}
'''
for name,value in {'M':M,'I':I,'P':[list(p) for p in perms],'CH':choices,'ST':stabilizer,'ORDER':order,'F':F,'A':A}.items():
    source=source.replace('@'+name+'@',cpp(value))
(HERE/'search_S4_cover.cpp').write_text(source)
(HERE/'search_S4_cover_data.json').write_text(json.dumps({'permutations':perms,'choices':choices,'stabilizer':stabilizer,'action_order':order,'original_action_total_lengths':[sum(len(w) for w in D['old_actions'][str(i)].values()) for i in range(11)],'involutive_action_total_lengths':[sum(map(len,a)) for a in A]},indent=2)+'\n')
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search_S4_cover.cpp'),'-o',str(HERE/'search_S4_cover.bin')],check=True)
run=subprocess.run([str(HERE/'search_S4_cover.bin')],capture_output=True,text=True,check=True)
print(run.stdout,end='')
(HERE/'search_S4_cover_exact.out').write_text(run.stdout)
for line in run.stdout.splitlines():
    if line.startswith('WITNESS peripherals '):
        first,second=line.split(' source ')
        p=list(map(int,first.split()[2:]));q=list(map(int,second.split()))
        (HERE/'S4_cover_witness.json').write_text(json.dumps({'peripheral_indices':p,'source_indices':q,'permutations':perms},indent=2)+'\n')

