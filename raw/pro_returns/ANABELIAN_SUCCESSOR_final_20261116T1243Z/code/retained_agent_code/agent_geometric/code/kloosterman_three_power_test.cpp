// Exact small fixed-3-primary tests for the family y^2+xy=x^3+a.
// This is a finite certificate; no asymptotic assertion is encoded.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
struct GF {
  uint32_t d, q, mod;
  uint32_t mul(uint32_t a,uint32_t b) const {uint32_t c=0;while(b){if(b&1)c^=a;b>>=1;a<<=1;if(a&q)a^=mod;}return c;}
  uint32_t power(uint32_t a,uint32_t n) const {uint32_t c=1;while(n){if(n&1)c=mul(c,a);a=mul(a,a);n>>=1;}return c;}
  uint32_t tr(uint32_t a) const {uint32_t c=0;for(uint32_t i=0;i<d;i++){c^=a;a=mul(a,a);}assert(c<2);return c;}
};
vector<uint32_t> factors(uint32_t n){vector<uint32_t> p;for(uint32_t d=2;d*d<=n;d++)if(n%d==0){p.push_back(d);while(n%d==0)n/=d;}if(n>1)p.push_back(n);return p;}
int main(){
 cout<<"{\n  \"scope\": \"Exact finite fixed-3-primary tests, not a theorem of unbounded growth\",\n  \"records\": [\n";
 uint32_t ord=3;
 for(uint32_t n=1;n<=3;n++,ord*=3){
  uint32_t m=ord/3,d=2*m; GF k{d,1u<<d,(1u<<d)|(1u<<m)|1u};
  uint32_t a=2, N=k.q-1, g=2;auto ps=factors(N);
  for(;;g++){bool good=true;for(auto p:ps)if(k.power(g,N/p)==1){good=false;break;}if(good&&k.power(g,N)==1)break;}
  vector<uint32_t> ex(N); vector<int> logs(k.q,-1);uint32_t z=1;
  for(uint32_t i=0;i<N;i++){assert(z!=0&&logs[z]==-1);ex[i]=z;logs[z]=i;z=k.mul(z,g);}assert(z==1);
  for(uint32_t x=1;x<k.q;x++)assert(logs[x]>=0);
  assert(k.power(a,ord)==1&&k.power(a,ord/3)!=1);
  uint32_t mask=0;for(uint32_t i=0;i<d;i++)if(k.tr(1u<<i))mask|=1u<<i;
  uint32_t count=2; long kloosterman=1;
  for(uint32_t i=0;i<N;i++){
    int j=(int(logs[a])-2*int(i))%int(N);if(j<0)j+=N;
    uint32_t w=ex[i]^ex[j];bool trace=__builtin_parity(w&mask);
    if(!trace)count+=2;kloosterman+=trace?-1:1;
    if(k.q<=64)assert(trace==k.tr(w));
  }
  assert((long)count==(long)k.q+kloosterman);
  uint32_t v=__builtin_ctz(count),orbit=1;z=k.power(a,4);while(z!=a){orbit++;z=k.power(z,4);}assert(orbit==m);
  cout<<"    {\"n\":"<<n<<",\"parameter_order\":"<<ord<<",\"degree_over_F4\":"<<m<<",\"q\":"<<k.q<<",\"binary_modulus\":"<<k.mod<<",\"parameter_encoding\":2,\"multiplicative_generator\":"<<g<<",\"trace_mask\":"<<mask<<",\"point_count\":"<<count<<",\"frobenius_trace\":"<<(long(k.q)+1-count)<<",\"kloosterman_including_zero\":"<<kloosterman<<",\"v2_unit_root_minus_one\":"<<v<<"}"<<(n<3?",":"")<<"\n";
 }
 cout<<"  ],\n  \"all_checks_passed\": true\n}\n";
}
