// Experimental exact memoization of the ORIGINAL positive collector.
// Every cache key includes the known word/repetition and the entire affected
// base suffix. Central increments are retained integrally; there is no modular
// reduction or change of collection order. Validation is mandatory before use.
#include "pbc_positive_collector_control.hpp"
#include <unordered_map>
#include <memory>
#include <cstring>

struct MemoCollector : Collector {
 using Delta=std::vector<std::pair<int,uint64_t>>;
 struct Acc {
  std::vector<uint64_t> a;std::vector<int> used;
  explicit Acc(int m):a(m+1,0){}
  void add(int i,unsigned __int128 v){
   if(!v)return;
   if(v>std::numeric_limits<uint64_t>::max()-a[i])throw std::overflow_error("memo central coefficient exceeds64bits");
   if(!a[i])used.push_back(i);a[i]+=static_cast<uint64_t>(v);
  }
  void clear(){for(int i:used)a[i]=0;used.clear();}
  Delta take(){Delta d;d.reserve(used.size());for(int i:used){d.push_back({i,a[i]});a[i]=0;}used.clear();return d;}
 };
 struct Entry {std::string after;Delta delta;};
 struct Info {uint32_t id;int first;bool central;};
 std::unordered_map<const Word*,Info> info;
 std::unordered_map<std::string,Entry> cache;
 std::vector<std::unique_ptr<Acc>> acc;
 uint64_t hits=0,misses=0,atoms=0,cache_bytes=0,cache_limit=256ULL<<20;
 uint64_t max_atoms_per_collection=20000000,initial_atoms=0;
 explicit MemoCollector(std::istream&in):Collector(in){
  uint32_t id=0;
  auto reg=[&](const Word&w){
   if(w.empty())return;int first=n+1;for(auto[g,e]:w)first=std::min(first,g);
   info.emplace(&w,Info{++id,first,first>n});
  };
  for(int i=1;i<=n;i++){reg(powers[i]);reg(generator[i]);for(int j=1;j<i;j++)if(changed[i][j])reg(conjugates[i][j]);}
  for(int i=0;i<n+8;i++)acc.push_back(std::make_unique<Acc>(m));
 }
 void atom(int g,long long exponent,std::vector<long long>&base,int depth,Acc&out){
  while(exponent){
   ++atoms;
   if(max_atoms_per_collection&&atoms-initial_atoms>max_atoms_per_collection)throw PBCCollectionBudget();
   if((atoms&4095)==0&&PBCControlPending())PBCControlHook();
   if(g>n){out.add(g-n,exponent);return;}
   std::vector<std::pair<const Word*,long long>> pending;
   if(g==comm[g]){
    for(int h=g+1;h<=n;h++)if(base[h]&&!changed[h][g])out.add(conjugatetail[h][g],static_cast<unsigned __int128>(exponent)*base[h]);
    base[g]+=exponent;exponent=0;
   }else{
    --exponent;++base[g];
    for(int h=g+1;h<=n;h++)if(base[h]&&!changed[h][g])out.add(conjugatetail[h][g],base[h]);
    int h=comm[g];while(h>g&&!(base[h]&&changed[h][g]))--h;
    if(h>g||base[g]>=order[g])for(int hh=comm[g];hh>h;--hh)if(base[hh]){pending.push_back({&generator[hh],base[hh]});base[hh]=0;}
    while(h>g){if(base[h]){pending.push_back({changed[h][g]?&conjugates[h][g]:&generator[h],base[h]});base[h]=0;}--h;}
   }
   if(base[g]>=order[g]){base[g]-=order[g];pending.push_back({&powers[g],1});}
   for(auto it=pending.rbegin();it!=pending.rend();++it)word(*it->first,it->second,base,depth+1,out);
  }
 }
 void word(const Word&w,long long repeat,std::vector<long long>&base,int depth,Acc&parent){
  assert(repeat>0&&depth<int(acc.size()));if(w.empty())return;
  auto wi=info.find(&w);bool known=wi!=info.end();
  if(known&&wi->second.central){for(auto[g,e]:w){assert(g>n);parent.add(g-n,static_cast<unsigned __int128>(e)*repeat);}return;}
  std::string key;int first=1;
  if(known){
   first=wi->second.first;key.resize(12+n-first+1);
   uint32_t id=wi->second.id;uint64_t r=repeat;std::memcpy(key.data(),&id,4);std::memcpy(key.data()+4,&r,8);
   for(int i=first;i<=n;i++){assert(base[i]>=0&&base[i]<256);key[12+i-first]=char(base[i]);}
   auto found=cache.find(key);
   if(found!=cache.end()){
    ++hits;for(int i=first;i<=n;i++)base[i]=static_cast<unsigned char>(found->second.after[i-first]);
    for(auto[i,v]:found->second.delta)parent.add(i,v);return;
   }
   ++misses;
  }
  Acc&out=*acc[depth];assert(out.used.empty());
  for(long long r=0;r<repeat;r++)for(auto[g,e]:w)atom(g,e,base,depth,out);
  Delta delta=out.take();
  if(known){
   size_t bytes=key.size()+n-first+1+delta.size()*sizeof(Delta::value_type)+128;
   if(cache_bytes+bytes<=cache_limit){
    std::string after(n-first+1,'\0');for(int i=first;i<=n;i++){assert(base[i]>=0&&base[i]<256);after[i-first]=char(base[i]);}
    cache.emplace(std::move(key),Entry{std::move(after),delta});cache_bytes+=bytes;
   }
  }
  for(auto[i,v]:delta)parent.add(i,v);
 }
 Normal collect(const Word&input){
  initial_atoms=atoms;Normal v{std::vector<long long>(n+1,0),std::vector<uint64_t>(m+1,0)};
  Acc&out=*acc[0];assert(out.used.empty());
  try{
   // Root is deliberately not cached; its local Word address is not stable.
   for(auto[g,e]:input)atom(g,e,v.base,0,out);
   for(int i=1;i<=n;i++)assert(v.base[i]>=0&&v.base[i]<order[i]);
   for(int i:out.used)v.tail[i]=out.a[i];out.clear();return v;
  }catch(...){for(auto&a:acc)a->clear();throw;}
 }
};
