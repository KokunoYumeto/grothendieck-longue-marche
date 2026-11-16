// Exact active-support optimization of the original positive collector.
// Rewriting words, their order, integral central coefficients and step counts
// are unchanged. Bitsets only replace scans over zero base coordinates.
#include "pbc_positive_collector_control.hpp"
struct BitCollector:Collector {
 int blocks;
 std::vector<std::vector<uint64_t>> unchanged_mask,changed_mask,affected_mask;
 explicit BitCollector(std::istream&in):Collector(in),blocks((n+64)/64),
  unchanged_mask(n+1,std::vector<uint64_t>(blocks)),
  changed_mask(n+1,std::vector<uint64_t>(blocks)),
  affected_mask(n+1,std::vector<uint64_t>(blocks)){
  for(int g=1;g<=n;g++)for(int h=g+1;h<=n;h++){
   (changed[h][g]?changed_mask[g]:unchanged_mask[g])[h/64]|=uint64_t(1)<<(h%64);
   if(h<=comm[g])affected_mask[g][h/64]|=uint64_t(1)<<(h%64);
  }
 }
 Normal collect(const Word&input){
  unsigned long long local_steps=0;
  Normal v{std::vector<long long>(n+1,0),std::vector<uint64_t>(m+1,0)};
  std::vector<uint64_t>active(blocks);
  auto mark=[&](int i){if(v.base[i])active[i/64]|=uint64_t(1)<<(i%64);else active[i/64]&=~(uint64_t(1)<<(i%64));};
  auto addtail=[&](int i,unsigned __int128 amount){
   if(amount>std::numeric_limits<uint64_t>::max()-v.tail[i])throw std::overflow_error("exact central coefficient exceeds64bits");
   v.tail[i]+=static_cast<uint64_t>(amount);
  };
  std::vector<Frame>stack;
  auto push=[&](const Word&w,long long repeat){assert(repeat>0&&!w.empty());stack.push_back({&w,repeat,0,w[0].second});};
  if(input.empty())return v;push(input,1);
  while(!stack.empty()){
   ++steps;++local_steps;
   if(max_steps_per_collection&&local_steps>max_steps_per_collection)throw PBCCollectionBudget();
   if(local_steps%100000==0&&PBCControlPending())PBCControlHook();
   auto&top=stack.back();
   if(top.exponent==0){++top.pos;if(top.pos==top.w->size()){if(--top.repeat==0){stack.pop_back();continue;}top.pos=0;}top.exponent=(*top.w)[top.pos].second;continue;}
   int g=(*top.w)[top.pos].first;assert(g>=1&&g<=n+m);
   if(stack.size()>1&&top.pos==0&&g>n){for(auto[h,e]:*top.w){assert(h>n);addtail(h-n,static_cast<unsigned __int128>(e)*top.repeat);}stack.pop_back();continue;}
   if(g>n){addtail(g-n,top.exponent);top.exponent=0;continue;}
   long long exponent=(g==comm[g]?top.exponent:1);
   for(int b=0;b<blocks;b++){
    uint64_t mask=active[b]&unchanged_mask[g][b];
    while(mask){int bit=__builtin_ctzll(mask),h=64*b+bit;mask&=mask-1;addtail(conjugatetail[h][g],static_cast<unsigned __int128>(exponent)*v.base[h]);}
   }
   if(g==comm[g]){v.base[g]+=exponent;top.exponent=0;mark(g);}
   else{
    assert(top.exponent>0);--top.exponent;++v.base[g];mark(g);
    bool has_changed=false;for(int b=0;b<blocks;b++)if(active[b]&changed_mask[g][b]){has_changed=true;break;}
    if(has_changed||v.base[g]>=order[g]){
     for(int b=blocks-1;b>=0;b--){
      uint64_t mask=active[b]&affected_mask[g][b];
      while(mask){int bit=63-__builtin_clzll(mask),h=64*b+bit;mask&=~(uint64_t(1)<<bit);
       push(changed[h][g]?conjugates[h][g]:generator[h],v.base[h]);v.base[h]=0;active[b]&=~(uint64_t(1)<<bit);
      }
     }
    }
   }
   if(v.base[g]>=order[g]){v.base[g]-=order[g];mark(g);push(powers[g],1);}
  }
  for(int i=1;i<=n;i++)assert(v.base[i]>=0&&v.base[i]<order[i]);return v;
 }
};
