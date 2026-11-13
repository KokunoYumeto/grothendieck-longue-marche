#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <deque>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

// Exhaust every subgroup mapping onto the actual V4 outer quotient.
// Starting pairs represent every inner conjugacy class in outer coset1;
// arbitrary adjoining of inner elements then exhausts all such subgroups.
constexpr int N = 1440;
constexpr int W = (N+63)/64;
using Bits = std::array<std::uint64_t,W>;
struct Hash {
  std::size_t operator()(Bits const& b) const {
    std::size_t h=0x9e3779b97f4a7c15ULL;
    for (auto x:b) h ^= x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);
    return h;
  }
};
struct Subgroup { std::vector<int> members, generators; int representative; };

int main(int argc,char**argv) {
  if(argc!=3) {std::cerr<<"usage: table.bin subgroups.json\n";return 2;}
  std::ifstream in(argv[1],std::ios::binary);
  auto rd=[&]() {unsigned char a,b;in.read((char*)&a,1);in.read((char*)&b,1);return int(a)+256*int(b);};
  int n=rd(),one=rd();assert(n==N);
  std::vector<int> inv(N),outer(N);
  for(auto&x:inv)x=rd(); for(auto&x:outer)x=rd();
  std::vector<std::uint16_t> table(N*N);
  for(auto&x:table)x=rd(); assert(in.good());
  auto mul=[&](int a,int b){return int(table[a*N+b]);};
  auto conjugate=[&](int a,int b){return mul(mul(a,b),inv[a]);};
  auto bitset=[&](std::vector<int> const&v){Bits b{};for(auto x:v)b[x/64]|=1ULL<<(x%64);return b;};
  auto generate=[&](std::vector<int> gens){
    auto old=gens;for(auto x:old)gens.push_back(inv[x]);
    std::array<bool,N> seen{};std::vector<int> v{one};seen[one]=true;
    for(std::size_t i=0;i<v.size();++i)for(auto g:gens){int x=mul(v[i],g);if(!seen[x]){seen[x]=true;v.push_back(x);}}
    std::sort(v.begin(),v.end());return v;
  };
  std::unordered_map<Bits,int,Hash> index;
  std::vector<Subgroup> actual,representatives;
  auto register_group=[&](std::vector<int> const&v,std::vector<int> const&gens){
    if(index.count(bitset(v)))return;
    int ri=representatives.size();representatives.push_back({v,gens,ri});
    for(int g=0;g<N;++g){
      std::vector<int> conjugated;conjugated.reserve(v.size());
      for(auto x:v)conjugated.push_back(conjugate(g,x));
      auto bits=bitset(conjugated);
      if(index.count(bits)){assert(actual[index.at(bits)].representative==ri);continue;}
      std::sort(conjugated.begin(),conjugated.end());
      std::vector<int> conjugated_gens;for(auto x:gens)conjugated_gens.push_back(conjugate(g,x));
      int ai=actual.size();index.emplace(bits,ai);
      actual.push_back({conjugated,conjugated_gens,ri});
    }
    std::cerr<<"new outer-surjective conjugacy class "<<ri<<" order "<<v.size()
             <<"; total actual "<<actual.size()<<"\n";
  };
  std::array<bool,N> covered{};
  std::vector<int> first_reps;
  for(int x=0;x<N;++x)if(outer[x]==1&&!covered[x]){
    first_reps.push_back(x);
    for(int h=0;h<N;++h)if(outer[h]==0)covered[conjugate(h,x)]=true;
  }
  std::size_t seed_pairs=0,adjoin_tests=0;
  for(auto x:first_reps)for(int y=0;y<N;++y)if(outer[y]==2){
    register_group(generate({x,y}),{x,y});++seed_pairs;
  }
  for(std::size_t i=0;i<representatives.size();++i){
    auto current=representatives[i];auto bits=bitset(current.members);
    for(int g=0;g<N;++g)if(outer[g]==0&&!(bits[g/64]&(1ULL<<(g%64)))){
      auto gens=current.generators;gens.push_back(g);
      register_group(generate(gens),gens);++adjoin_tests;
    }
  }
  std::ofstream out(argv[2]);
  auto arr=[&](std::vector<int> const&v){out<<'[';for(std::size_t i=0;i<v.size();++i){if(i)out<<',';out<<v[i];}out<<']';};
  out<<"{\"status\":\"PASS_EXHAUSTIVE_OUTER_SURJECTIVE_SUBGROUPS\",\"seed_pairs\":"<<seed_pairs
     <<",\"adjoining_tests\":"<<adjoin_tests<<",\"first_inner_class_representatives\":";arr(first_reps);
  out<<",\"representatives\":[";
  for(std::size_t i=0;i<representatives.size();++i){if(i)out<<',';auto const&s=representatives[i];
    out<<"{\"members\":";arr(s.members);out<<",\"generators\":";arr(s.generators);out<<'}';}
  out<<"],\"all_subgroups\":[";
  for(std::size_t i=0;i<actual.size();++i){if(i)out<<',';auto const&s=actual[i];
    out<<"{\"representative\":"<<s.representative<<",\"members\":";arr(s.members);
    out<<",\"generators\":";arr(s.generators);out<<'}';}
  out<<"]}\n";
  std::cout<<"PASS_EXHAUSTIVE_OUTER_SURJECTIVE_SUBGROUPS classes="<<representatives.size()
           <<" actual="<<actual.size()<<" seed_pairs="<<seed_pairs<<" adjoining_tests="<<adjoin_tests<<"\n";
}
