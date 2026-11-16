// Reconstructed exact Gray-code search. The output is a witness, not a claim
// of unsatisfiability of any larger frame family.
#include <cstdint>
#include <iostream>
#include <vector>
struct W { uint64_t a,b; W operator^(const W& y)const{return {a^y.a,b^y.b};}
 bool operator==(const W& y)const{return a==y.a&&b==y.b;}};
int main(){unsigned n; if(!(std::cin>>n)||n>31)return 2;
 std::vector<W> q(n),p(n*n),d;W target;
 for(auto&v:q)std::cin>>v.a>>v.b;
 for(auto&v:p)std::cin>>v.a>>v.b;
 std::cin>>target.a>>target.b;if(!std::cin)return 3;
 for(unsigned i=0;i<n;i++)for(unsigned j=0;j<n;j++)
  if(!(p[i*n+j]==p[j*n+i])||(i==j&&!(p[i*n+j]==W{0,0})))return 4;
 d=q;W value{0,0};uint64_t mask=0;
 if(value==target){std::cout<<"SOLUTION 0 visited 1\n";return 0;}
 for(uint64_t step=1;step<(uint64_t(1)<<n);step++){
  unsigned i=__builtin_ctzll(step);value=value^d[i];mask^=uint64_t(1)<<i;
  for(unsigned j=0;j<n;j++)d[j]=d[j]^p[i*n+j];
  if(value==target){std::cout<<"SOLUTION "<<mask<<" visited "<<step+1<<"\n";return 0;}
 }
 std::cout<<"EXHAUSTED "<<(uint64_t(1)<<n)<<"\n";return 1;
}
