// Exact dense Schreier--Sims with an independently replayable word DAG.
// Permutations act on the right: (p*q)[i]=q[p[i]].
// Every added generator is a literal Schreier word in earlier generators.
// Termination is certified by sifting EVERY final Schreier relation.
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <memory>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using P=std::vector<uint16_t>;
struct Node { uint32_t op,a,b; };
struct Gen { P p; uint32_t node; int depth; };
struct Level {
  int base; std::vector<int> pos,orbit;
  std::vector<P> trans,inv;
  std::vector<uint32_t> word;
};
struct Engine {
  int n; P id; std::vector<P> original;
  std::vector<Node> nodes{{0,0,0}};
  std::vector<Gen> gens; std::vector<Level> chain;
  uint64_t scanned=0,final_relations=0;
  uint64_t normal_checks=0;
  bool derived_mode=false;
  int next_start=0;
  std::vector<uint32_t> original_nodes,selected_original_indices;
  std::chrono::steady_clock::time_point start=std::chrono::steady_clock::now();
  explicit Engine(int degree):n(degree),id(n) {
    if(n<1||n>65535)throw std::runtime_error("degree range");
    std::iota(id.begin(),id.end(),0);
  }
  P mul(const P&a,const P&b)const {P c(n);for(int i=0;i<n;++i)c[i]=b[a[i]];return c;}
  P inverse(const P&a)const {P c(n);for(int i=0;i<n;++i)c[a[i]]=i;return c;}
  bool identity(const P&a)const {for(int i=0;i<n;++i)if(a[i]!=i)return false;return true;}
  uint32_t product_node(uint32_t a,uint32_t b) {
    if(!a)return b;if(!b)return a;
    nodes.push_back({2,a,b});return nodes.size()-1;
  }
  uint32_t inverse_node(uint32_t a) {
    if(!a)return 0;nodes.push_back({3,a,0});return nodes.size()-1;
  }
  uint32_t commutator_node(uint32_t a,uint32_t b) {
    nodes.push_back({4,a,b});return nodes.size()-1;
  }
  uint32_t conjugate_node(uint32_t a,uint32_t b) {
    nodes.push_back({5,a,b});return nodes.size()-1;
  }
  P commutator(const P&a,const P&b)const {return mul(mul(mul(a,b),inverse(a)),inverse(b));}
  P conjugate(const P&a,const P&b)const {return mul(mul(a,b),inverse(a));}
  void new_level(int b) {
    Level l;l.base=b;l.pos.assign(n,-1);l.pos[b]=0;l.orbit={b};
    l.trans.push_back(id);l.inv.push_back(id);l.word.push_back(0);
    chain.push_back(std::move(l));
  }
  void extend(int lev,int gi,bool record=true) {
    Level &l=chain[lev];size_t old=l.orbit.size();
    auto edge=[&](size_t at,int j) {
      int target=gens[j].p[l.orbit[at]];
      if(l.pos[target]>=0)return;
      P t=mul(l.trans[at],gens[j].p);
      if(t[l.base]!=target)throw std::runtime_error("transversal image");
      uint32_t w=record?product_node(l.word[at],gens[j].node):0;
      l.pos[target]=l.orbit.size();l.orbit.push_back(target);
      l.inv.push_back(inverse(t));l.trans.push_back(std::move(t));l.word.push_back(w);
    };
    for(size_t at=0;at<old;++at)edge(at,gi);
    for(size_t at=old;at<l.orbit.size();++at)
      for(size_t j=0;j<gens.size();++j)if(gens[j].depth>=lev)edge(at,j);
  }
  void add(P p,uint32_t node) {
    if(identity(p))return;
    int depth=0;
    while(depth<(int)chain.size()&&p[chain[depth].base]==chain[depth].base)++depth;
    if(depth==(int)chain.size()) {
      int b=0;while(p[b]==b)++b;new_level(b);
    }
    gens.push_back({std::move(p),node,depth});
    for(int i=0;i<=depth;++i)extend(i,gens.size()-1);
  }
  void set_original(const std::vector<P>&input) {
    original=input;
    for(size_t j=0;j<input.size();++j) {
      P p=input[j];P sorted=p;std::sort(sorted.begin(),sorted.end());
      if(sorted!=id)throw std::runtime_error("invalid original permutation");
      nodes.push_back({1,(uint32_t)j,0});original_nodes.push_back(nodes.size()-1);
    }
  }
  void initialize(const std::vector<P>&input) {
    set_original(input);
    for(size_t j=0;j<input.size();++j){add(input[j],original_nodes[j]);selected_original_indices.push_back(j);}
  }
  bool contains(P h)const {
    for(auto &c:chain){int b=h[c.base];if(b==c.base)continue;int pos=c.pos[b];if(pos<0)return false;h=mul(h,c.inv[pos]);}
    return identity(h);
  }
  bool pass(bool discovery,int start_at=-1) {
    uint64_t count=0;
    if(start_at<0)start_at=(int)chain.size()-1;
    for(int lev=start_at;lev>=0;--lev) {
      for(size_t at=0;at<chain[lev].orbit.size();++at) {
        for(size_t gi=0;gi<gens.size();++gi) {
          if(gens[gi].depth<lev)continue;
          ++count;++scanned;
          auto &l=chain[lev];int target=gens[gi].p[l.orbit[at]];
          int to=l.pos[target];if(to<0)throw std::runtime_error("orbit not closed");
          P h=mul(mul(l.trans[at],gens[gi].p),l.inv[to]);
          std::vector<std::pair<uint32_t,bool>> history;
          if(discovery)history={{l.word[at],false},{gens[gi].node,false},{l.word[to],true}};
          for(int k=lev+1;k<(int)chain.size();++k) {
            auto &c=chain[k];int b=h[c.base];
            if(b==c.base)continue;
            int pos=c.pos[b];if(pos<0)break;
            h=mul(h,c.inv[pos]);
            if(discovery)history.push_back({c.word[pos],true});
          }
          if(!identity(h)) {
            if(!discovery)throw std::runtime_error("nonzero final Schreier residue");
            uint32_t word=0;
            for(auto [w,inv]:history)word=product_node(word,inv?inverse_node(w):w);
            add(std::move(h),word);
            next_start=gens.back().depth;
            if(gens.size()%20==0) {
              double secs=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
              std::cout<<"strong generators "<<gens.size()<<" base "<<chain.size()
                       <<" word nodes "<<nodes.size()<<" seconds "<<secs<<std::endl;
            }
            return false;
          }
        }
      }
    }
    final_relations=count;return true;
  }
  void discover() {
    next_start=(int)chain.size()-1;
    while(!pass(true,next_start)){}
    pass(false);
  }
  void greedy(const std::vector<P>&input) {
    set_original(input);
    for(size_t j=0;j<input.size();++j)if(!contains(input[j])) {
      add(input[j],original_nodes[j]);selected_original_indices.push_back(j);discover();
      std::cout<<"selected original "<<j<<" count "<<selected_original_indices.size()
               <<" subgroup order "<<order()<<std::endl;
    }
  }
  void derived(const std::vector<P>&input) {
    derived_mode=true;set_original(input);
    for(size_t i=0;i<input.size();++i)for(size_t j=i+1;j<input.size();++j)
      add(commutator(input[i],input[j]),commutator_node(original_nodes[i],original_nodes[j]));
    discover();
    bool changed=true;
    while(changed) {
      changed=false;
      for(size_t i=0;i<input.size()&&!changed;++i)for(size_t j=0;j<gens.size();++j) {
        ++normal_checks;P h=conjugate(input[i],gens[j].p);
        if(!contains(h)) {
          uint32_t word=conjugate_node(original_nodes[i],gens[j].node);
          add(std::move(h),word);discover();changed=true;break;
        }
      }
    }
    check_derived();
  }
  void check_derived() {
    for(size_t i=0;i<original.size();++i)for(size_t j=i+1;j<original.size();++j)
      if(!contains(commutator(original[i],original[j])))throw std::runtime_error("missing derived commutator");
    for(auto &a:original)for(auto &g:gens){++normal_checks;if(!contains(conjugate(a,g.p)))throw std::runtime_error("derived image not normal");}
  }
  std::string order()const {
    std::string digits="1";
    for(auto &c:chain) {
      unsigned carry=0;
      for(int i=(int)digits.size()-1;i>=0;--i) {
        unsigned v=(digits[i]-'0')*c.orbit.size()+carry;
        digits[i]='0'+v%10;carry=v/10;
      }
      while(carry){digits.insert(digits.begin(),'0'+carry%10);carry/=10;}
    }
    return digits;
  }
  template<class T> static void put(std::ostream&o,const T&x){o.write((const char*)&x,sizeof(T));}
  template<class T> static T get(std::istream&i){T x;i.read((char*)&x,sizeof(T));if(!i)throw std::runtime_error("short certificate");return x;}
  void save(const std::string&path)const {
    std::ofstream out(path,std::ios::binary);if(!out)throw std::runtime_error("certificate output");
    put<uint32_t>(out,0x41365354);put<uint32_t>(out,n);put<uint32_t>(out,derived_mode?1:0);put<uint32_t>(out,original.size());
    for(auto &p:original)out.write((const char*)p.data(),n*sizeof(uint16_t));
    put<uint32_t>(out,chain.size());for(auto &c:chain)put<uint32_t>(out,c.base);
    put<uint32_t>(out,gens.size());
    for(auto &g:gens){put<uint32_t>(out,g.node);put<uint32_t>(out,g.depth);out.write((const char*)g.p.data(),n*sizeof(uint16_t));}
    put<uint32_t>(out,nodes.size());for(auto &v:nodes){put(out,v.op);put(out,v.a);put(out,v.b);}
  }
  static std::unique_ptr<Engine> replay(const std::string&path) {
    std::ifstream in(path,std::ios::binary);if(!in)throw std::runtime_error("certificate input");
    uint32_t magic=get<uint32_t>(in);
    if(magic!=0x41365353&&magic!=0x41365354)throw std::runtime_error("certificate magic");
    int n=get<uint32_t>(in);auto e=std::make_unique<Engine>(n);
    if(magic==0x41365354)e->derived_mode=get<uint32_t>(in)!=0;
    unsigned m=get<uint32_t>(in);e->original.resize(m,P(n));
    for(auto &p:e->original)in.read((char*)p.data(),n*sizeof(uint16_t));
    for(auto &p:e->original){P sorted=p;std::sort(sorted.begin(),sorted.end());if(sorted!=e->id)throw std::runtime_error("invalid original certificate permutation");}
    unsigned b=get<uint32_t>(in);std::vector<int> base;
    for(unsigned i=0;i<b;++i)base.push_back(get<uint32_t>(in));
    unsigned ng=get<uint32_t>(in);
    for(unsigned i=0;i<ng;++i){uint32_t w=get<uint32_t>(in),depth=get<uint32_t>(in);P p(n);in.read((char*)p.data(),n*sizeof(uint16_t));e->gens.push_back({std::move(p),w,(int)depth});}
    unsigned nn=get<uint32_t>(in);e->nodes.clear();
    for(unsigned i=0;i<nn;++i)e->nodes.push_back({get<uint32_t>(in),get<uint32_t>(in),get<uint32_t>(in)});
    if(!in)throw std::runtime_error("truncated certificate");
    // Verify each generator as an ACTUAL original-generator word,
    // evaluating the supplied DAG, retaining only live values.
    std::vector<unsigned> refs(nn,0);std::vector<std::vector<unsigned>> checks(nn);
    for(unsigned j=0;j<ng;++j)checks.at(e->gens[j].node).push_back(j);
    for(unsigned i=0;i<nn;++i){auto v=e->nodes[i];
      if(v.op>=2&&v.op<=5){if(v.a>=i)throw std::runtime_error("DAG order");++refs[v.a];}
      if(v.op==2||v.op==4||v.op==5){if(v.b>=i)throw std::runtime_error("DAG order");++refs[v.b];}
    }
    std::vector<std::unique_ptr<P>> values(nn);
    std::vector<bool> derived_word(nn,false);
    for(unsigned i=0;i<nn;++i){auto v=e->nodes[i];P p;
      if(v.op==0){if(i)throw std::runtime_error("identity node");p=e->id;derived_word[i]=true;}
      else if(v.op==1)p=e->original.at(v.a);
      else if(v.op==2){p=e->mul(*values.at(v.a),*values.at(v.b));derived_word[i]=derived_word[v.a]&&derived_word[v.b];}
      else if(v.op==3){p=e->inverse(*values.at(v.a));derived_word[i]=derived_word[v.a];}
      else if(v.op==4){p=e->commutator(*values.at(v.a),*values.at(v.b));derived_word[i]=true;}
      else if(v.op==5){p=e->conjugate(*values.at(v.a),*values.at(v.b));derived_word[i]=derived_word[v.b];}
      else throw std::runtime_error("DAG operation");
      for(unsigned j:checks[i]){
        if(p!=e->gens[j].p)throw std::runtime_error("literal word mismatch");
        if(e->derived_mode&&!derived_word[i])throw std::runtime_error("strong word lacks derived membership");
      }
      values[i]=std::make_unique<P>(std::move(p));
      if(v.op>=2&&v.op<=5){if(!--refs[v.a])values[v.a].reset();}
      if(v.op==2||v.op==4||v.op==5){if(!--refs[v.b])values[v.b].reset();}
      if(!refs[i])values[i].reset();
    }
    for(int b:base)e->new_level(b);
    for(unsigned j=0;j<ng;++j){auto &g=e->gens[j];
      P sorted=g.p;std::sort(sorted.begin(),sorted.end());if(sorted!=e->id)throw std::runtime_error("invalid strong permutation");
      for(int k=0;k<g.depth;++k)if(g.p[base[k]]!=base[k])throw std::runtime_error("strong prefix");
      if(g.depth>=(int)b||g.p[base[g.depth]]==base[g.depth])throw std::runtime_error("strong depth");
      for(int k=0;k<=g.depth;++k)e->extend(k,j,false);
    }
    e->pass(false);
    // The original generators must also sift completely through this chain.
    if(e->derived_mode)e->check_derived();
    else for(auto h:e->original)if(!e->contains(h))throw std::runtime_error("original residue");
    return e;
  }
  void report()const {
    double secs=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::cout<<"{\"status\":\"PASS\",\"degree\":"<<n<<",\"order\":\""<<order()
      <<"\",\"strong_generators\":"<<gens.size()<<",\"word_DAG_nodes\":"<<nodes.size()
      <<",\"derived_mode\":"<<(derived_mode?"true":"false")
      <<",\"complete_final_Schreier_relations\":"<<final_relations
      <<",\"normal_conjugation_checks\":"<<normal_checks
      <<",\"total_discovery_relation_scans\":"<<scanned<<",\"selected_original_indices\":[";
    for(size_t i=0;i<selected_original_indices.size();++i){if(i)std::cout<<",";std::cout<<selected_original_indices[i];}
    std::cout<<"],\"base\":[";
    for(size_t i=0;i<chain.size();++i){if(i)std::cout<<",";std::cout<<chain[i].base;}
    std::cout<<"],\"orbit_lengths\":[";
    for(size_t i=0;i<chain.size();++i){if(i)std::cout<<",";std::cout<<chain[i].orbit.size();}
    std::cout<<"],\"seconds\":"<<secs<<"}"<<std::endl;
  }
};
int main(int argc,char**argv){try {
  if(argc==3&&std::string(argv[1])=="--replay") {auto e=Engine::replay(argv[2]);e->report();return 0;}
  bool derived=argc==4&&std::string(argv[1])=="--derived";
  bool greedy=argc==4&&std::string(argv[1])=="--greedy";
  if(argc!=3&&!derived&&!greedy)throw std::runtime_error("usage: executable [--derived|--greedy] input.txt certificate.bin | --replay certificate.bin");
  int shift=(derived||greedy)?1:0;
  std::ifstream in(argv[1+shift]);int n,m;in>>n>>m;if(!in)throw std::runtime_error("input header");
  std::vector<P> input(m,P(n));for(auto &p:input)for(auto &x:p){unsigned a;in>>a;x=a;}
  if(!in)throw std::runtime_error("input permutations");
  Engine e(n);
  if(derived)e.derived(input);
  else if(greedy)e.greedy(input);
  else {e.initialize(input);e.discover();}
  e.save(argv[2+shift]);e.report();return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
