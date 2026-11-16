"""Exhaust all four-sheet permutation covers for the exact marginal data.

Simultaneous conjugation by the stabilizer of sheet zero removes duplicates.
The test is the actual lift-fixing-sheet condition, not an affine surrogate.
No absence of an obstruction in this one finite degree implies equality.
"""
from pathlib import Path
import itertools,json,subprocess
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'positive_fiber_data.json').read_text())
perms=list(itertools.permutations(range(4))); index={p:i for i,p in enumerate(perms)}
def mul(p,q):return tuple(p[q[i]] for i in range(4))
def inv(p):return tuple(p.index(i) for i in range(4))
M=[[index[mul(p,q)] for q in perms] for p in perms]
I=[index[inv(p)] for p in perms]
ST=[i for i,p in enumerate(perms) if p[0]==0]
def conj(h,g):return M[M[h][g]][I[h]]
def reps(elements,group):
    rem=set(elements);ans=[]
    while rem:
        g=min(rem);ans.append(g);rem-={conj(h,g) for h in group}
    return ans
pairs=[]
for p7 in reps(ST,ST):
    centralizer=[h for h in ST if conj(h,p7)==p7]
    for p1 in reps(range(24),centralizer):pairs.append([p1,p7])
assert sum(len({(conj(h,p1),conj(h,p7)) for h in ST}) for p1,p7 in pairs)==24*6
F=[D['new_fiber_words'][str(i)] for i in [17,14,11,16,18,12,13]] #15 is x7^-1.
A=[[D['old_actions'][str(i)][str(j)] for j in range(1,8)] for i in range(11)]
order=sorted(range(11),key=lambda i:sum(map(len,A[i])))
def cpp(x):return '{'+','.join(map(cpp,x))+'}' if isinstance(x,list) else str(x)
source=r'''
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
const int M[24][24]=@M@, I[24]=@I@, P[24][4]=@P@;
const vector<int> ST=@ST@, ORDER=@ORDER@;
const vector<vector<int>> PAIRS=@PAIRS@, F=@F@;
const vector<vector<vector<int>>> A=@A@;
int eval(const vector<int>&w,const array<int,7>&p){int r=0;for(int x:w)r=M[r][x>0?p[x-1]:I[p[-x-1]]];return r;}
bool fixes(const vector<int>&w,const array<int,7>&p){
  int v=0;for(auto it=w.rbegin();it!=w.rend();++it){int x=*it;v=P[x>0?p[x-1]:I[p[-x-1]]][v];}return v==0;
}
bool connected(const array<int,7>&p){
  bool reached[4]={true,false,false,false};
  for(int k=0;k<4;k++)for(int a:p)for(int i=0;i<4;i++)if(reached[i])reached[P[a][i]]=true;
  return reached[0]&&reached[1]&&reached[2]&&reached[3];
}
int main(){
  uint64_t tested=0,transitive=0,fiber_ok=0,old_pass[12]={};
  array<int,7>p;array<int,11>q;auto start=chrono::steady_clock::now();
  uint64_t total=24ULL*24*24*24*24;
  cout<<"gauge_pairs "<<PAIRS.size()<<" remaining_tuples_each "<<total<<endl;
  for(const auto& pair:PAIRS){
    p[0]=pair[0];p[6]=pair[1];
    for(uint64_t n=0;n<total;n++){
      uint64_t v=n;for(int j=1;j<6;j++){p[j]=v%24;v/=24;}tested++;
      if(p[0]==0&&p[2]==0&&p[4]==0&&p[6]==0)continue;
      if(!connected(p))continue;transitive++;
      bool ok=true;for(const auto&w:F)if(!fixes(w,p)){ok=false;break;}
      if(!ok)continue;fiber_ok++;old_pass[0]++;
      for(int oi=0;oi<11;oi++){
        int a=ORDER[oi],mask=63;
        for(int j=0;j<7&&mask;j++){
          int e=eval(A[a][j],p);
          for(int k=0;k<6;k++)if((mask>>k)&1){int z=ST[k];if(M[M[z][p[j]]][I[z]]!=e)mask&=~(1<<k);}
        }
        if(!mask){ok=false;break;}q[a]=ST[__builtin_ctz((unsigned)mask)];old_pass[oi+1]++;
      }
      if(ok){cout<<"WITNESS peripherals";for(int a:p)cout<<' '<<a;cout<<" source";for(int a:q)cout<<' '<<a;cout<<endl;return 0;}
    }
    cout<<"pair_finished "<<pair[0]<<' '<<pair[1]<<" tested "<<tested<<" fiber_ok "<<fiber_ok<<" elapsed "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
  }
  cout<<"NO_WITNESS_DEGREE4 tested "<<tested<<" transitive_nontrivial_normal "<<transitive<<" fiber_ok "<<fiber_ok<<endl;
  cout<<"successive_old_action_passes";for(int k=0;k<12;k++)cout<<' '<<old_pass[k];cout<<endl;
  cout<<"elapsed_seconds "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
}
'''
for name,value in {'M':M,'I':I,'P':[list(p) for p in perms],'ST':ST,'ORDER':order,'PAIRS':pairs,'F':F,'A':A}.items():source=source.replace('@'+name+'@',cpp(value))
(HERE/'search_all_S4_cover.cpp').write_text(source)
(HERE/'search_all_S4_cover_data.json').write_text(json.dumps({'permutations':perms,'gauge_pairs':pairs,'stabilizer':ST,'action_order':order},indent=2)+'\n')
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search_all_S4_cover.cpp'),'-o',str(HERE/'search_all_S4_cover.bin')],check=True)
subprocess.run([str(HERE/'search_all_S4_cover.bin')],check=True)
