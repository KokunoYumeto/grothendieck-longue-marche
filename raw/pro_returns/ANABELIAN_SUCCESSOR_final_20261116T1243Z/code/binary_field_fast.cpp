// Exact polynomial-basis arithmetic for GF(2^n), 1 <= n <= 256.
// This is an optional speed helper. Irreducibility is checked independently.
#include <cstdint>
#include <cstring>
static void reduce(uint64_t* t,int n,const uint64_t* low,uint64_t* out){
  for(int k=2*n-2;k>=n;--k) if((t[k/64]>>(k%64))&1){
    t[k/64]^=uint64_t(1)<<(k%64);
    int s=k-n,w=s/64,b=s%64;
    for(int j=0;j<4;++j){
      if(w+j<8)t[w+j]^=low[j]<<b;
      if(b && w+j+1<8)t[w+j+1]^=low[j]>>(64-b);
    }
  }
  for(int j=0;j<4;++j)out[j]=t[j];
  if(n%64)out[n/64]&=(uint64_t(1)<<(n%64))-1;
  for(int j=(n+63)/64;j<4;++j)out[j]=0;
}
extern "C" void gf_mul(const uint64_t* a,const uint64_t* b,uint64_t* out,int n,const uint64_t* low){
  uint64_t t[8]={};
  for(int i=0;i<4;++i){uint64_t x=a[i];while(x){
    int k=__builtin_ctzll(x);x&=x-1;
    for(int j=0;j<4;++j){
      t[i+j]^=b[j]<<k;
      if(k)t[i+j+1]^=b[j]>>(64-k);
    }
  }}
  reduce(t,n,low,out);
}
extern "C" void gf_square(const uint64_t* a,uint64_t* out,int n,const uint64_t* low){
  uint64_t t[8]={};
  for(int i=0;i<4;++i){uint64_t x=a[i];while(x){
    int k=2*(64*i+__builtin_ctzll(x));x&=x-1;t[k/64]^=uint64_t(1)<<(k%64);
  }}
  reduce(t,n,low,out);
}
