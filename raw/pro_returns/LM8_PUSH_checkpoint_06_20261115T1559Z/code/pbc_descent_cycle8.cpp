// Lift the six-coordinate mod-four cycle locus through the actual
// mod-eight envelope kernel, using Schreier relators and GF(2).
// Necessary finite equations only: no full profinite lift is asserted.
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;using U=uint64_t;
struct MatrixGroup{
 int n,bits,e;vector<array<int,4>>m;vector<vector<int>>mt;vector<int>iv;
 MatrixGroup(int mod,int width):n(mod),bits(width){
  for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int c=0;c<n;c++)for(int d=0;d<n;d++)if((a*d-b*c+n*n)%n==1)m.push_back({a,b,c,d});
  mt.assign(m.size(),vector<int>(m.size()));iv.resize(m.size());e=idx({1,0,0,1});
  for(size_t i=0;i<m.size();i++)for(size_t j=0;j<m.size();j++){auto a=m[i],b=m[j];mt[i][j]=idx({(a[0]*b[0]+a[1]*b[2])%n,(a[0]*b[1]+a[1]*b[3])%n,(a[2]*b[0]+a[3]*b[2])%n,(a[2]*b[1]+a[3]*b[3])%n});if(mt[i][j]==e)iv[i]=j;}
 }
 int idx(array<int,4>a){return int(find(m.begin(),m.end(),a)-m.begin());}
 U mul(U a,U b){U c=0;for(int k=0;k<6;k++)c|=U(mt[(a>>(bits*k))&((1<<bits)-1)][(b>>(bits*k))&((1<<bits)-1)])<<(bits*k);return c;}
 U inv(U a){U c=0;for(int k=0;k<6;k++)c|=U(iv[(a>>(bits*k))&((1<<bits)-1)])<<(bits*k);return c;}
 U cj(U a,U b){return mul(mul(a,b),inv(a));}
 array<U,3> gens(){int ss=idx({0,1,n-1,0}),tt=idx({1,n-1,0,1}),zz=iv[mt[ss][tt]];int tr[3]={ss,tt,zz};U X=0,Y=0,I=0;int k=0;for(int a=0;a<3;a++)for(int b=0;b<3;b++)if(a!=b){X|=U(tr[a])<<(bits*k);Y|=U(tr[b])<<(bits*k);I|=U(e)<<(bits*k);k++;}return{X,Y,I};}
 uint32_t kv(U a){assert(n==8);uint32_t v=0;for(int k=0;k<6;k++){auto b=m[(a>>(9*k))&511];assert(b[0]%4==1&&b[1]%4==0&&b[2]%4==0&&b[3]%4==1);int d=(b[0]-1)/4,u=b[1]/4,l=b[2]/4;assert((b[3]-1)/4==d);v|=uint32_t(d|(u<<1)|(l<<2))<<(3*k);}return v;}
 U vk(uint32_t v){assert(n==8);U a=0;for(int k=0;k<6;k++){int z=(v>>(3*k))&7,d=z&1,u=(z>>1)&1,l=z>>2;a|=U(idx({1+4*d,4*u,4*l,1+4*d}))<<(9*k);}return a;}
};
struct Rel{uint32_t v=0,th=0,ro=0,rr=0;};
int main(){
 MatrixGroup A(4,6),B(8,9);auto ag=A.gens(),bg=B.gens();U X=ag[0],Y=ag[1],I=ag[2],X8=bg[0],Y8=bg[1],I8=bg[2],Z8=B.inv(B.mul(X8,Y8));
 vector<U> G{I},vs{I8},ts{I8},rs{I8},rrs{I8};vector<unsigned char> ex{0},ey{0};
 unordered_map<U,uint32_t> index;index.reserve(2200000);index[I]=0;vector<array<uint32_t,2>>edges;
 Rel piv[20];int dim=0;
 auto insert=[&](Rel q){for(int k=19;k>=0;k--)if((q.v>>k)&1){if(!piv[k].v){piv[k]=q;dim++;return;}q.v^=piv[k].v;q.th^=piv[k].th;q.ro^=piv[k].ro;q.rr^=piv[k].rr;}assert(q.th==0&&q.ro==0&&q.rr==0);};
 for(uint32_t i=0;i<G.size();i++){
  array<uint32_t,2>ed;
  for(int j=0;j<2;j++){
   U val=A.mul(G[i],j?Y:X);auto it=index.find(val);uint32_t ni;
   if(it==index.end()){
    ni=G.size();index.emplace(val,ni);G.push_back(val);
    vs.push_back(B.mul(vs[i],j?Y8:X8));ts.push_back(B.mul(ts[i],j?X8:Y8));rs.push_back(B.mul(rs[i],j?Z8:Y8));rrs.push_back(B.mul(rrs[i],j?X8:Z8));
    ex.push_back((ex[i]+!j)%8);ey.push_back((ey[i]+j)%8);
   }else ni=it->second;
   ed[j]=ni;
   int dx=(ex[i]+!j-ex[ni]+8)%8,dy=(ey[i]+j-ey[ni]+8)%8;assert(dx%4==0&&dy%4==0);
   Rel q;
   q.v=B.kv(B.mul(B.mul(vs[i],j?Y8:X8),B.inv(vs[ni])))|(uint32_t(dx/4)<<18)|(uint32_t(dy/4)<<19);
   q.th=B.kv(B.mul(B.mul(ts[i],j?X8:Y8),B.inv(ts[ni])));
   q.ro=B.kv(B.mul(B.mul(rs[i],j?Z8:Y8),B.inv(rs[ni])));
   q.rr=B.kv(B.mul(B.mul(rrs[i],j?X8:Z8),B.inv(rrs[ni])));
   insert(q);
  }
  edges.push_back(ed);
 }
 cerr<<"base_order "<<G.size()<<" augmented_kernel_dimension "<<dim<<endl;
 vector<Rel>basis;for(auto q:piv)if(q.v)basis.push_back(q);
 auto reduce4=[&](U a){U c=0;for(int k=0;k<6;k++){auto z=B.m[(a>>(9*k))&511];for(auto&v:z)v%=4;c|=U(A.idx(z))<<(6*k);}return c;};
 ofstream out("LM8_PUSH/code/pbc_descent_cycle8.json");out<<"{\n\"scope\":\"Necessary actual-envelope mod8 cycle lifts with abelian exponents zero mod8; no full lift asserted\",\n\"base_order\":"<<G.size()<<",\n\"augmented_kernel_dimension\":"<<dim<<",\n\"rows\":[\n";
 int nc=0,ns=0;
 for(size_t i=0;i<G.size();i++){
  if(ex[i]%4||ey[i]%4)continue;
  if(A.mul(G[i],reduce4(ts[i]))!=I||A.mul(A.mul(reduce4(rrs[i]),reduce4(rs[i])),G[i])!=I)continue;
  U f=vs[i],th=ts[i],ro=rs[i],rr=rrs[i];
  U base2=B.mul(f,th),base3=B.mul(B.mul(rr,ro),f);
  uint64_t target=B.kv(base2)|(uint64_t(B.kv(base3))<<18)|(uint64_t(ex[i]/4)<<36)|(uint64_t(ey[i]/4)<<37);
  uint64_t columns[38]={};int rank=0;
  for(auto q:basis){
   uint32_t k=q.v&((1<<18)-1);
   uint32_t l2=k^B.kv(B.cj(f,B.vk(q.th)));
   uint32_t l3=q.rr^B.kv(B.cj(rr,B.vk(q.ro)))^B.kv(B.cj(B.mul(rr,ro),B.vk(k)));
   uint64_t c=l2|(uint64_t(l3)<<18)|(uint64_t((q.v>>18)&3)<<36);
   for(int j=37;j>=0;j--)if((c>>j)&1){if(!columns[j]){columns[j]=c;rank++;break;}c^=columns[j];}
  }
  uint64_t rem=target;for(int j=37;j>=0;j--)if((rem>>j)&1){if(!columns[j])break;rem^=columns[j];}
  bool ok=rem==0;if(ok)ns++;
  if(nc++)out<<",\n";
  out<<"{\"f_mod4\":"<<G[i]<<",\"lifts\":"<<(ok?(1ULL<<(dim-rank)):0)<<",\"rank\":"<<rank<<",\"first_v\":[";
  auto v=A.m[G[i]&63];for(int j=0;j<4;j++){if(j)out<<",";out<<v[j];}out<<"]}";
 }
 out<<"\n],\n\"base_cycles\":"<<nc<<",\n\"surviving_base_cycles\":"<<ns<<"\n}\n";
 cout<<"base_order "<<G.size()<<"\naugmented_kernel_dimension "<<dim<<"\nbase_cycles "<<nc<<"\nsurviving_base_cycles "<<ns<<"\n";
}
