// Exact factorization tests for the actual19 A5 epikernels of F.
#define main de_a6_schreier_existing_main
#include "de_a6_schreier.cpp"
#undef main

struct Probe {
  Engine&e;Engine q;std::vector<Node> nodes;std::vector<P> values;
  std::vector<int> rejected=std::vector<int>(19,-1);
  uint64_t relations=0;
  Probe(Engine&base,const std::vector<P>&original):e(base),q(570){
    if(e.derived_mode||e.original.size()!=2)throw std::runtime_error("ordinary two-generator base required");
    for(unsigned j=0;j<2;++j){bool found=false;for(auto&g:e.gens)
      if(g.node==j+1&&g.p==e.original[j])found=true;
      if(!found)throw std::runtime_error("original strong generator missing");}
    std::vector<int>bases;for(auto&c:e.chain)bases.push_back(c.base);e.chain.clear();
    for(int b:bases)e.new_level(b);
    for(unsigned j=0;j<e.gens.size();++j)for(int k=0;k<=e.gens[j].depth;++k)e.extend(k,j,true);
    nodes=e.nodes;values.reserve(nodes.size()+1000);
    for(auto n:nodes){P v;
      if(n.op==0)v=q.id;else if(n.op==1)v=original.at(n.a);
      else if(n.op==2)v=q.mul(values.at(n.a),values.at(n.b));
      else if(n.op==3)v=q.inverse(values.at(n.a));
      else if(n.op==4)v=q.commutator(values.at(n.a),values.at(n.b));
      else if(n.op==5)v=q.conjugate(values.at(n.a),values.at(n.b));
      else throw std::runtime_error("word operation");values.push_back(v);
    }
  }
  uint32_t product(uint32_t a,uint32_t b){if(!a)return b;if(!b)return a;auto v=q.mul(values[a],values[b]);nodes.push_back({2,a,b});values.push_back(v);return nodes.size()-1;}
  uint32_t inverse(uint32_t a){if(!a)return 0;auto v=q.inverse(values[a]);nodes.push_back({3,a,0});values.push_back(v);return nodes.size()-1;}
  void run(){
    for(int lev=(int)e.chain.size()-1;lev>=0;--lev){auto&l=e.chain[lev];
      for(unsigned at=0;at<l.orbit.size();++at)for(auto&g:e.gens){if(g.depth<lev)continue;
        int to=l.pos[g.p[l.orbit[at]]];
        P h=e.mul(e.mul(l.trans[at],g.p),l.inv[to]);
        P v=q.mul(q.mul(values[l.word[at]],values[g.node]),q.inverse(values[l.word[to]]));
        std::vector<std::pair<uint32_t,bool>> history{{l.word[at],false},{g.node,false},{l.word[to],true}};
        for(int k=lev+1;k<(int)e.chain.size();++k){auto&c=e.chain[k];int b=h[c.base];if(b==c.base)continue;
          int pos=c.pos[b];if(pos<0)throw std::runtime_error("base relator outside chain");
          h=e.mul(h,c.inv[pos]);v=q.mul(v,q.inverse(values[c.word[pos]]));history.push_back({c.word[pos],true});}
        if(!e.identity(h))throw std::runtime_error("nonidentity base relation");++relations;
        std::vector<int> failures;
        for(int j=0;j<19;++j)if(rejected[j]<0){bool good=true;for(int p=30*j;p<30*j+30;++p)if(v[p]!=p)good=false;if(!good)failures.push_back(j);}
        if(!failures.empty()){
          uint32_t w=0;for(auto[a,inv]:history)w=product(w,inv?inverse(a):a);
          if(values[w]!=v)throw std::runtime_error("saved rejection word");
          for(int j:failures)rejected[j]=w;
          std::cout<<"nonfactoring epikernels";for(int j:failures)std::cout<<" "<<j;std::cout<<" relation "<<relations<<std::endl;
        }
      }
      if(lev%10==0)std::cout<<"level "<<lev<<" relations "<<relations<<std::endl;
    }
    if(relations!=e.final_relations)throw std::runtime_error("complete relation count");
  }
  void save(const std::string&name,double seconds){std::ofstream f(name);if(!f)throw std::runtime_error("output");
    f<<"{\n\"status\":\"PASS_COMPLETE_EPIKERNEL_FACTORIZATION\",\n\"base_order\":\""<<e.order()<<"\",\n\"base_degree\":"<<e.n
     <<",\n\"complete_relator_count\":"<<relations<<",\n\"factoring_epikernel_indices\":[";
    bool first=true;for(int j=0;j<19;++j)if(rejected[j]<0){if(!first)f<<",";first=false;f<<j;}f<<"],\n\"rejection_word_nodes\":[";
    for(int j=0;j<19;++j){if(j)f<<",";f<<rejected[j];}f<<"],\n\"literal_word_DAG\":[";
    for(unsigned i=0;i<nodes.size();++i){if(i)f<<",";auto n=nodes[i];f<<"["<<n.op<<","<<n.a<<","<<n.b<<"]";}f<<"],\n\"seconds\":"<<seconds<<"\n}\n";
  }
};

int main(int argc,char**argv){try{
  if(argc!=4)throw std::runtime_error("usage: executable base.bin quotients.input output.json");
  std::ifstream in(argv[2]);int n,m;in>>n>>m;if(n!=570||m!=2)throw std::runtime_error("quotient header");
  std::vector<P> original(m,P(n));for(auto&p:original){for(auto&x:p){unsigned v;in>>v;if(v>=570)throw std::runtime_error("quotient range");x=v;}auto sorted=p;std::sort(sorted.begin(),sorted.end());for(int j=0;j<n;++j)if(sorted[j]!=j)throw std::runtime_error("quotient permutation");}
  if(!in)throw std::runtime_error("short quotient input");
  auto start=std::chrono::steady_clock::now();auto e=Engine::replay(argv[1]);std::cout<<"base complete replay passed"<<std::endl;
  Probe p(*e,original);p.run();double secs=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();p.save(argv[3],secs);
  std::cout<<"PASS complete factoring epikernels";for(int j=0;j<19;++j)if(p.rejected[j]<0)std::cout<<" "<<j;std::cout<<" seconds "<<secs<<std::endl;return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
