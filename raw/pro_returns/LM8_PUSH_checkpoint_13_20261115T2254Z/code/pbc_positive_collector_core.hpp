// Extracted without algorithm changes from pbc_positive_collector.cpp
// SHA256 8a115eae60b4337309842a16c9a00d25241e81b90defbbc8d9945faf84e6b300
// Positive-word native port of PBC_CentralCollectV2.
// Original algorithm: GAP 4.16.1 / Polycyclic 2.18 colftl.gi.
// The existing retained package/source license and attribution apply.
// Positive central coefficients use checked 64-bit integers. Every
// addition is overflow-checked with a 128-bit intermediate; an overflow
// aborts rather than reducing a coefficient. No quotient of the formal
// central module is imposed by this collector.
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using Word=std::vector<std::pair<int,long long>>;
struct Frame {const Word* w; long long repeat; size_t pos; long long exponent;};
struct Normal {std::vector<long long> base; std::vector<uint64_t> tail;};
struct Collector {
 int n,m;
 std::vector<int> order,comm,powertail;
 std::vector<Word> powers,generator;
 std::vector<std::vector<Word>> conjugates;
 std::vector<std::vector<int>> conjugatetail;
 std::vector<std::vector<bool>> changed;
 unsigned long long steps=0;
 std::chrono::steady_clock::time_point began=std::chrono::steady_clock::now();
 Word readword(std::istream& in) {
  int len;in>>len;assert(in.good() && len>=0 && len%2==0);
  Word w; for(int k=0;k<len;k+=2) {
   int g;long long e;in>>g>>e;assert(e>0);w.push_back({g,e});
  }return w;
 }
 explicit Collector(std::istream& in) {
  in>>n;m=n*(n+1)/2;
  order.resize(n+1);comm.resize(n+1);powertail.resize(n+1);
  powers.resize(n+1);generator.resize(n+m+1);
  conjugates.assign(n+1,std::vector<Word>(n+1));
  conjugatetail.assign(n+1,std::vector<int>(n+1,0));
  changed.assign(n+1,std::vector<bool>(n+1,false));
  for(int i=1;i<=n;i++)in>>order[i];
  for(int i=1;i<=n;i++)powers[i]=readword(in);
  for(int i=2;i<=n;i++)for(int j=1;j<i;j++)
   conjugates[i][j]=readword(in);
  int tail=0;
  for(int i=1;i<=n;i++) {
   powertail[i]=++tail;powers[i].push_back({n+tail,1});
   for(int j=1;j<i;j++) {
    conjugatetail[i][j]=++tail;
    changed[i][j]=!(conjugates[i][j].size()==1 &&
     conjugates[i][j][0]==std::make_pair(i,1LL));
    if(changed[i][j])conjugates[i][j].push_back({n+tail,1});
   }
  }
  assert(tail==m);
  for(int i=1;i<=n+m;i++)generator[i]={{i,1}};
  comm[n]=n;
  for(int g=n-1;g>=1;g--) {
   int h=n;
   while(h>comm[g+1] && !changed[h][g])--h;
   comm[g]=(h==g+1 && !changed[h][g])?g:h;
  }
 }
 Normal collect(const Word& input) {
  Normal v{std::vector<long long>(n+1,0),std::vector<uint64_t>(m+1,0)};
  auto addtail=[&](int index,unsigned __int128 amount) {
   if(amount>std::numeric_limits<uint64_t>::max()-v.tail[index])
    throw std::overflow_error("exact central coefficient exceeds 64-bit storage");
   v.tail[index]+=static_cast<uint64_t>(amount);
  };
  std::vector<Frame> stack;
  auto push=[&](const Word& w,long long repeat) {
   assert(repeat>0 && !w.empty());stack.push_back({&w,repeat,0,w[0].second});
  };
  if(input.empty())return v;
  push(input,1);
  while(!stack.empty()) {
   ++steps;
   if(steps%100000000ULL==0) {
    double secs=std::chrono::duration<double>(std::chrono::steady_clock::now()-began).count();
    std::cerr<<"steps "<<steps<<" seconds "<<secs<<" stack "<<stack.size()<<std::endl;
   }
   auto &top=stack.back();
   if(top.exponent==0) {
    ++top.pos;
    if(top.pos==top.w->size()) {
     if(--top.repeat==0) {stack.pop_back();continue;}
     top.pos=0;
    }
    top.exponent=(*top.w)[top.pos].second;continue;
   }
   int g=(*top.w)[top.pos].first;
   assert(g>=1 && g<=n+m);
   if(stack.size()>1 && top.pos==0 && g>n) {
    for(auto [h,e]:*top.w) {
     assert(h>n);addtail(h-n,static_cast<unsigned __int128>(e)*top.repeat);
    }
    stack.pop_back();continue;
   }
   if(g>n) {
    addtail(g-n,top.exponent);top.exponent=0;continue;
   }
   if(g==comm[g]) {
    long long exponent=top.exponent;
    for(int h=g+1;h<=n;h++)
     if(v.base[h] && !changed[h][g])
      addtail(conjugatetail[h][g],static_cast<unsigned __int128>(exponent)*v.base[h]);
    v.base[g]+=exponent;top.exponent=0;
   } else {
    assert(top.exponent>0);--top.exponent;++v.base[g];
    for(int h=g+1;h<=n;h++)
     if(v.base[h] && !changed[h][g])
      addtail(conjugatetail[h][g],v.base[h]);
    int h=comm[g];
    while(h>g && !(v.base[h]!=0 && changed[h][g]))--h;
    if(h>g || v.base[g]>=order[g]) {
     for(int hh=comm[g];hh>h;--hh)if(v.base[hh]) {
      push(generator[hh],v.base[hh]);v.base[hh]=0;
     }
    }
    while(h>g) {
     if(v.base[h]) {
      push(changed[h][g]?conjugates[h][g]:generator[h],v.base[h]);
      v.base[h]=0;
     }
     --h;
    }
   }
   if(v.base[g]>=order[g]) {
    v.base[g]-=order[g];push(powers[g],1);
   }
  }
  for(int i=1;i<=n;i++)assert(v.base[i]>=0 && v.base[i]<order[i]);
  return v;
 }
};
