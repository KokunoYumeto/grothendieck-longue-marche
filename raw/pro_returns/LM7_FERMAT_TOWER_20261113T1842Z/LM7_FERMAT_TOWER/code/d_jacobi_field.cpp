// Exact cyclotomic-number enumeration in F_p[t]/(primitive polynomial).
// The polynomial and primitive element are certified in d_jacobi.py.
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 int p=atoi(argv[1]),f=atoi(argv[2]),n=atoi(argv[3]);
 vector<int> c(f),d(f,0);for(int j=0;j<f;j++)c[j]=atoi(argv[4+j]);
 uint64_t q=1;for(int j=0;j<f;j++)q*=p;
 if(q>300000000ULL){cerr<<"enumeration limit";return 2;}
 vector<uint8_t> cl(q,255);d[0]=1;uint64_t x=1;
 for(uint64_t k=0;k<q-1;k++){
  if(x==0 || cl[x]!=255){cerr<<"nonprimitive polynomial";return 3;}
  cl[x]=uint8_t(k%n);int hi=d[f-1];
  for(int j=f-1;j>0;j--){int z=(d[j-1]-hi*c[j])%p;d[j]=(z+p)%p;}
  d[0]=((-hi*c[0])%p+p)%p;
  x=0;for(int j=f-1;j>=0;j--)x=x*p+d[j];
 }
 if(x!=1){cerr<<"cycle failure";return 4;}
 vector<uint32_t> neg(q/p,0);for(uint64_t a=1;a<q/p;a++)neg[a]=p*neg[a/p]+(p-a%p)%p;
 vector<uint64_t> cnt(n*n,0);
 for(uint64_t a=2;a<q;a++){
  uint64_t b=uint64_t(neg[a/p])*p+(1+p-a%p)%p;
  if(!b || cl[a]==255 || cl[b]==255){cerr<<"class failure";return 5;}
  cnt[cl[a]*n+cl[b]]++;
 }
 for(int i=0;i<n;i++){for(int j=0;j<n;j++)cout<<cnt[i*n+j]<<" ";cout<<"\n";}
 return 0;
}
