#!/usr/bin/env python3
"""Generate an exact CRT-cache replay; whole-byte validation is mandatory."""
from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'pbc_trace_replay_boundary.cpp').read_text()
s=s.replace('#include <zlib.h>','#include <zlib.h>\n#include <array>\n#include <random>\n#include <cstdint>')
pos=s.index('struct ReplayDone')
crt=r'''
// CRT cache for N=2^146*3^30. Every quotient and emitted proof coefficient
// remains a GMP integer. Only dense modular subtraction uses these residues.
static constexpr uint64_t OddMod=205891132094649ULL;
static constexpr uint64_t TopMask=(uint64_t(1)<<18)-1;
struct Residue {
 std::array<uint64_t,3> a{0,0,0};uint64_t b=0;
 bool zero()const{return a[0]==0&&a[1]==0&&a[2]==0&&b==0;}
};
uint64_t OddInverse=0;
Residue residue(const Z& x){
 Residue r;
 if(mpz_fits_ulong_p(x.get_mpz_t())){
  r.a[0]=x.get_ui();r.b=r.a[0]%OddMod;return r;
 }
 Z y;mpz_fdiv_r_2exp(y.get_mpz_t(),x.get_mpz_t(),146);
 size_t count=0;mpz_export(r.a.data(),&count,-1,sizeof(uint64_t),0,0,y.get_mpz_t());assert(count<=3);
 r.b=mpz_fdiv_ui(x.get_mpz_t(),OddMod);return r;
}
Z reconstruct(const Residue&r){
 if(r.a[1]==0&&r.a[2]==0&&r.a[0]%OddMod==r.b)return Z(r.a[0]);
 uint64_t a3=0;
 for(int i=2;i>=0;i--)a3=(static_cast<__uint128_t>(a3)*(static_cast<__uint128_t>(1)<<64)+r.a[i])%OddMod;
 uint64_t diff=r.b>=a3?r.b-a3:r.b+OddMod-a3;
 uint64_t k=static_cast<__uint128_t>(diff)*OddInverse%OddMod;
 Z out;mpz_import(out.get_mpz_t(),3,-1,sizeof(uint64_t),0,0,r.a.data());
 if(k){Z high(k);mpz_mul_2exp(high.get_mpz_t(),high.get_mpz_t(),146);out+=high;}
 return out;
}
void sub_product(Residue&v,const Residue&q,const Residue&a){
 __uint128_t t=static_cast<__uint128_t>(q.a[0])*a.a[0];
 uint64_t p0=t;uint64_t carry=t>>64;
 __uint128_t t01=static_cast<__uint128_t>(q.a[0])*a.a[1];
 __uint128_t t10=static_cast<__uint128_t>(q.a[1])*a.a[0];
 __uint128_t middle=static_cast<__uint128_t>(carry)+uint64_t(t01)+uint64_t(t10);
 uint64_t p1=middle;
 uint64_t p2=(uint64_t(middle>>64)+uint64_t(t01>>64)+uint64_t(t10>>64)
   +q.a[0]*a.a[2]+q.a[1]*a.a[1]+q.a[2]*a.a[0])&TopMask;
 uint64_t borrow0=v.a[0]<p0;v.a[0]-=p0;
 uint64_t before=v.a[1],middle_sub=before-p1;
 uint64_t borrow1=(before<p1)||(middle_sub<borrow0);
 v.a[1]=middle_sub-borrow0;v.a[2]=(v.a[2]-p2-borrow1)&TopMask;
 uint64_t product=static_cast<__uint128_t>(q.b)*a.b%OddMod;
 v.b=v.b>=product?v.b-product:v.b+OddMod-product;
}
void init_and_test_crt(){
 Z power=Z(1)<<146,odd(OddMod),inverse;
 assert(mpz_invert(inverse.get_mpz_t(),power.get_mpz_t(),odd.get_mpz_t())!=0);OddInverse=inverse.get_ui();
 Z N=power*odd;std::mt19937_64 random(0xC31C7A);
 for(int i=0;i<10000;i++){
  auto make=[&](){Residue r;r.a={random(),random(),random()&TopMask};r.b=random()%OddMod;return r;};
  Residue v=make(),q=make(),a=make();Z zv=reconstruct(v),zq=reconstruct(q),za=reconstruct(a);
  assert(zv>=0&&zv<N&&residue(zv).a==v.a&&residue(zv).b==v.b);
  sub_product(v,q,a);assert(reconstruct(v)==mod(zv-zq*za,N));
 }
 std::cerr<<"CRT_exact_arithmetic_randomized_crosscheck_10000_PASS"<<std::endl;
}
struct FastTerm {int i;Residue value;};
'''
s=s[:pos]+crt+s[pos:]
s=s.replace('Sparse target;std::vector<Sparse> extras,basis;','Sparse target;std::vector<Sparse> extras,basis;\n bool crt_enabled=false;std::vector<std::vector<FastTerm>> fastbasis;')
s=s.replace('in>>source_hash>>modulus>>s_count>>r_count;extra_count=s_count+r_count+2;', 'in>>source_hash>>modulus>>s_count>>r_count;extra_count=s_count+r_count+2;\n  crt_enabled=(modulus==(Z(1)<<146)*Z(OddMod));')
s=s.replace('  abel_start=n;', '  if(crt_enabled){fastbasis.resize(m+1);for(int i=1;i<=m;i++)rebuild_fast(i);}\n  abel_start=n;',1)
a=s.index(' void reduce(Sparse&');b=s.index(' void insert(',a)
old=s[a:b].replace(' void reduce(', ' void reduce_gmp(',1)
new=r''' void rebuild_fast(int i){
  if(!crt_enabled)return;auto&out=fastbasis[i];out.clear();out.reserve(basis[i].size());
  for(const auto&[j,a]:basis[i])out.push_back({j,residue(a)});
 }
 void reduce(Sparse&v,Weights&weights,uint64_t&proof){
  if(!crt_enabled){reduce_gmp(v,weights,proof);return;}
  if(v.empty())return;
  std::vector<Z>acc(m+1);std::vector<Residue>cache(m+1);std::vector<bool>dirty(m+1,false);
  for(auto&[i,a]:v){acc[i]=a;cache[i]=residue(a);dirty[i]=(a<0||a>=modulus);}
  int first=v[0].first;
  for(int i=first;i<=m;i++){
   if(!dirty[i]&&cache[i].zero()){acc[i]=0;continue;}
   if(!dirty[i])acc[i]=reconstruct(cache[i]);
   const auto&row=basis[i];const auto&fastrow=fastbasis[i];assert(row.size()==fastrow.size());
   Z rem=mod(acc[i],row[0].second),q=(acc[i]-rem)/row[0].second;
   if(q==0)continue;acc[i]=rem;
   Residue qr=residue(q);
   unsigned long q2=mpz_fdiv_ui(q.get_mpz_t(),2),q3=mpz_fdiv_ui(q.get_mpz_t(),3);
   for(size_t j=1;j<row.size();j++){
    int k=fastrow[j].i;int d=small_coordinate[k];
    if(d==1){cache[k]=Residue{};dirty[k]=false;continue;}
    if(d){
     // Both 2 and3 divide N, so the cached components retain the exact
     // original residue even if the initial row coefficient was negative.
     uint64_t previous=d==2?(cache[k].a[0]&1):(cache[k].b%3);
     uint64_t coefficient=fastrow[j].value.a[0];assert(coefficient<uint64_t(d));
     long x=static_cast<long>(previous)-static_cast<long>((d==2?q2:q3)*coefficient);
     x%=d;if(x<0)x+=d;cache[k]=Residue{};cache[k].a[0]=cache[k].b=x;
    }else {assert(coordinate[k]==modulus);sub_product(cache[k],qr,fastrow[j].value);}
    dirty[k]=false;
   }
   subweights(weights,q,basisweights[i]);proof=trace.sub(proof,q,basisproof[i]);
  }
  v.clear();for(int i=first;i<=m;i++)if(acc[i]!=0)v.push_back({i,std::move(acc[i])});
 }
'''
s=s[:a]+old+new+s[b:]
s=s.replace('std::swap(proof,basisproof[i]);', 'std::swap(proof,basisproof[i]);rebuild_fast(i);')
s=s.replace('ReplayLimit=std::stoull(argv[4]);','init_and_test_crt();ReplayLimit=std::stoull(argv[4]);')
(P/'pbc_trace_replay_v5_crt.cpp').write_text(s)
print('Generated exact CRT-cache replay from the validated boundary reducer.')
