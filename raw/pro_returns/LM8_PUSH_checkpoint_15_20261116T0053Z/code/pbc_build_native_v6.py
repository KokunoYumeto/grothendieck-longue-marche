#!/usr/bin/env python3
"""Add a bounded-integer cache; preserve every exact proof operation."""
from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'pbc_native_modular_v5.cpp').read_text()
s='// Version6: exact bounded-integer cache when modulus is at most2^31.\n'+s
s=s.replace('Sparse target;std::vector<Sparse> extras,basis;', 'Sparse target;std::vector<Sparse> extras,basis;\n bool small_enabled=false;uint64_t small_modulus=0;std::vector<std::vector<std::pair<int,uint32_t>>> smallbasis;')
s=s.replace('in>>source_hash>>modulus>>s_count>>r_count;extra_count=s_count+r_count+2;', 'in>>source_hash>>modulus>>s_count>>r_count;extra_count=s_count+r_count+2;\n  small_enabled=(modulus>0&&modulus<=Z(1UL<<31));if(small_enabled)small_modulus=modulus.get_ui();')
s=s.replace('  abel_start=n;', '  if(small_enabled){smallbasis.resize(m+1);for(int i=1;i<=m;i++)rebuild_small(i);}\n  abel_start=n;',1)
a=s.index(' void reduce(Sparse&');b=s.index(' void insert(',a)
old=s[a:b].replace(' void reduce(', ' void reduce_gmp(',1)
new=r''' void rebuild_small(int i){
  if(!small_enabled)return;auto&out=smallbasis[i];out.clear();out.reserve(basis[i].size());
  for(auto&[k,a]:basis[i]){assert(a>=0&&a<=modulus);out.push_back({k,static_cast<uint32_t>(a.get_ui())});}
 }
 void reduce(Sparse&v,Weights&weights,uint64_t&proof){
  if(!small_enabled){reduce_gmp(v,weights,proof);return;}
  for(auto&[i,a]:v)if(!mpz_fits_slong_p(a.get_mpz_t())){reduce_gmp(v,weights,proof);return;}
  if(v.empty())return;
  std::vector<int64_t>acc(m+1);for(auto&[i,a]:v)acc[i]=a.get_si();int first=v[0].first;
  for(int i=first;i<=m;i++){
   if(i%64==0&&PBCControlPending())PBCControlHook();
   if(acc[i]==0)continue;auto&row=smallbasis[i];assert(!row.empty()&&row[0].first==i);
   int64_t pivot=row[0].second,rem=acc[i]%pivot,q=acc[i]/pivot;
   if(rem<0){rem+=pivot;--q;}
   if(q==0)continue;acc[i]=rem;
   int64_t qn=q%static_cast<int64_t>(small_modulus);if(qn<0)qn+=small_modulus;
   int q2=q%2,q3=q%3;if(q2<0)q2+=2;if(q3<0)q3+=3;
   for(size_t j=1;j<row.size();j++){
    auto[k,a]=row[j];assert(k>i);int d=small_coordinate[k];
    if(d==1){acc[k]=0;continue;}
    if(d){int64_t x=acc[k]%d-(d==2?q2:q3)*int64_t(a);x%=d;if(x<0)x+=d;acc[k]=x;}
    else {
     assert(coordinate[k]==modulus);
     int64_t previous=acc[k];if(previous<0||previous>=static_cast<int64_t>(small_modulus)){previous%=static_cast<int64_t>(small_modulus);if(previous<0)previous+=small_modulus;}
     uint64_t product=uint64_t(qn)*a%small_modulus;
     acc[k]=uint64_t(previous)>=product?uint64_t(previous)-product:uint64_t(previous)+small_modulus-product;
    }
   }
   Z quotient(static_cast<long>(q));subweights(weights,quotient,basisweights[i]);proof=trace.sub(proof,quotient,basisproof[i]);
  }
  v.clear();for(int i=first;i<=m;i++)if(acc[i]!=0)v.push_back({i,Z(static_cast<long>(acc[i]))});
 }
'''
s=s[:a]+old+new+s[b:]
s=s.replace('std::swap(proof,basisproof[i]);','std::swap(proof,basisproof[i]);rebuild_small(i);')
s=s.replace('native_version5_pid','native_version6_pid')
(P/'pbc_native_modular_v6.cpp').write_text(s)
print('Generated native version6 exact bounded-integer cache.')
