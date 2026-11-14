// Complete abelianization of the actual threefold universal pullback on C_A6.
// Every original-generator sign freedom is retained in the first ten bits.
#define main de_a6_schreier_existing_main
#include "de_a6_schreier.cpp"
#undef main
#include <array>
#include <map>

struct CentralModel {
  using Value=std::array<uint8_t,3>;
  uint8_t sm[120][120],si[120];unsigned sid,z,n,m;
  std::vector<Value> original;std::vector<P> base_original;
  static uint32_t integer(std::istream&f){uint32_t x;f.read((char*)&x,4);if(!f)throw std::runtime_error("short central model");return x;}
  explicit CentralModel(const std::string&path){
    std::ifstream f(path,std::ios::binary);
    if(integer(f)!=0xA6C6CE13||integer(f)!=1)throw std::runtime_error("central model header");
    sid=integer(f);z=integer(f);m=integer(f);n=integer(f);
    if(sid>=120||z>=120||m!=10||n>65535)throw std::runtime_error("central model indices");
    f.read((char*)sm,sizeof(sm));f.read((char*)si,sizeof(si));
    original.resize(m);for(auto&v:original)f.read((char*)v.data(),3);
    base_original.resize(m,P(n));for(auto&p:base_original)f.read((char*)p.data(),2*n);
    if(!f||f.peek()!=EOF)throw std::runtime_error("central model length");
    for(int i=0;i<120;++i){
      if(si[i]>=120||sm[i][sid]!=i||sm[sid][i]!=i||sm[i][si[i]]!=sid||sm[z][i]!=sm[i][z])
        throw std::runtime_error("central model table identity");
      for(int j=0;j<120;++j)if(sm[i][j]>=120)throw std::runtime_error("central table range");
    }
    if(sm[z][z]!=sid||z==sid)throw std::runtime_error("central sign order");
    for(auto&v:original)for(auto x:v)if(x>=120)throw std::runtime_error("original lift range");
  }
  Value one()const{return{uint8_t(sid),uint8_t(sid),uint8_t(sid)};}
  Value mul(const Value&a,const Value&b)const{Value c;for(int i=0;i<3;++i)c[i]=sm[a[i]][b[i]];return c;}
  Value inv(const Value&a)const{Value b;for(int i=0;i<3;++i)b[i]=si[a[i]];return b;}
  Value comm(const Value&a,const Value&b)const{return mul(mul(mul(a,b),inv(a)),inv(b));}
  Value conj(const Value&a,const Value&b)const{return mul(mul(a,b),inv(a));}
  unsigned central(const Value&a)const{unsigned v=0;for(int i=0;i<3;++i){if(a[i]==z)v|=1U<<i;else if(a[i]!=sid)throw std::runtime_error("noncentral relator value");}return v;}
};

struct CentralProbe {
  using Value=CentralModel::Value;
  Engine&e;CentralModel&m;std::vector<Node>nodes;std::vector<Value>values;
  std::vector<unsigned>exponents;std::map<unsigned,unsigned>rows;
  std::vector<unsigned>basis,basis_words;uint64_t relations=0;unsigned original_relations=0;
  CentralProbe(Engine&engine,CentralModel&model):e(engine),m(model){
    if(e.original!=m.base_original)throw std::runtime_error("literal central input generators");
    std::vector<int>bases;for(auto&l:e.chain)bases.push_back(l.base);e.chain.clear();
    for(int b:bases)e.new_level(b);
    for(unsigned j=0;j<e.gens.size();++j)for(int k=0;k<=e.gens[j].depth;++k)e.extend(k,j,true);
    nodes=e.nodes;
    for(auto node:nodes){Value v;unsigned a=0;
      if(node.op==0)v=m.one();
      else if(node.op==1){v=m.original.at(node.a);a=1U<<node.a;}
      else if(node.op==2){v=m.mul(values.at(node.a),values.at(node.b));a=exponents[node.a]^exponents[node.b];}
      else if(node.op==3){v=m.inv(values.at(node.a));a=exponents[node.a];}
      else if(node.op==4)v=m.comm(values.at(node.a),values.at(node.b));
      else if(node.op==5){v=m.conj(values.at(node.a),values.at(node.b));a=exponents[node.b];}
      else throw std::runtime_error("central word operation");
      values.push_back(v);exponents.push_back(a);
    }
  }
  unsigned reduce(unsigned v)const{for(auto[p,w]:rows)if(v&(1U<<p))v^=w;return v;}
  uint32_t product(uint32_t a,uint32_t b){if(!a)return b;if(!b)return a;
    nodes.push_back({2,a,b});values.push_back(m.mul(values[a],values[b]));exponents.push_back(exponents[a]^exponents[b]);return nodes.size()-1;}
  uint32_t inverse(uint32_t a){if(!a)return 0;
    nodes.push_back({3,a,0});values.push_back(m.inv(values[a]));exponents.push_back(exponents[a]);return nodes.size()-1;}
  void relation(const Value&v,unsigned ab,const std::vector<std::pair<uint32_t,bool>>&history){
    unsigned row=ab|(m.central(v)<<10),r=reduce(row);if(!r)return;
    unsigned w=0;for(auto[a,inv]:history)w=product(w,inv?inverse(a):a);
    if(values[w]!=v||exponents[w]!=ab)throw std::runtime_error("central literal relation replay");
    rows.emplace(__builtin_ctz(r),r);basis.push_back(row);basis_words.push_back(w);
    std::cout<<"relation rank "<<basis.size()<<" at "<<relations<<" originals "<<original_relations<<std::endl;
  }
  void original_links(){
    for(unsigned j=0;j<e.original.size();++j){
      unsigned node=j+1;if(nodes.at(node).op!=1||nodes[node].a!=j)throw std::runtime_error("original DAG position");
      P h=e.original[j];Value v=values[node];unsigned ab=exponents[node];
      std::vector<std::pair<uint32_t,bool>>history{{node,false}};
      for(auto&l:e.chain){int b=h[l.base];if(b==l.base)continue;int pos=l.pos[b];
        if(pos<0)throw std::runtime_error("original outside certified group");
        h=e.mul(h,l.inv[pos]);v=m.mul(v,m.inv(values[l.word[pos]]));ab^=exponents[l.word[pos]];history.push_back({l.word[pos],true});}
      if(!e.identity(h))throw std::runtime_error("original sift residual");
      ++original_relations;relation(v,ab,history);
    }
  }
  void run(){
    original_links();
    for(int lev=(int)e.chain.size()-1;lev>=0;--lev){auto&l=e.chain[lev];
      for(unsigned at=0;at<l.orbit.size();++at)for(auto&g:e.gens){if(g.depth<lev)continue;
        int to=l.pos[g.p[l.orbit[at]]];P h=e.mul(e.mul(l.trans[at],g.p),l.inv[to]);
        Value v=m.mul(m.mul(values[l.word[at]],values[g.node]),m.inv(values[l.word[to]]));
        unsigned ab=exponents[l.word[at]]^exponents[g.node]^exponents[l.word[to]];
        std::vector<std::pair<uint32_t,bool>>history{{l.word[at],false},{g.node,false},{l.word[to],true}};
        for(int k=lev+1;k<(int)e.chain.size();++k){auto&c=e.chain[k];int b=h[c.base];if(b==c.base)continue;
          int pos=c.pos[b];if(pos<0)throw std::runtime_error("central relation outside chain");
          h=e.mul(h,c.inv[pos]);v=m.mul(v,m.inv(values[c.word[pos]]));ab^=exponents[c.word[pos]];history.push_back({c.word[pos],true});}
        if(!e.identity(h))throw std::runtime_error("nonidentity central base relation");
        ++relations;relation(v,ab,history);
      }
      if(lev%10==0)std::cout<<"level "<<lev<<" relations "<<relations<<" rank "<<basis.size()<<std::endl;
    }
    if(relations!=e.final_relations||original_relations!=10)throw std::runtime_error("incomplete central presentation");
  }
  void save(const std::string&path,double seconds){
    std::ofstream f(path);if(!f)throw std::runtime_error("central output");
    f<<"{\n\"status\":\"PASS_COMPLETE_CENTRAL_PULLBACK\",\n\"base_order\":\""<<e.order()<<"\",\n"
     <<"\"base_degree\":"<<e.n<<",\n\"complete_Schreier_relations\":"<<relations<<",\n"
     <<"\"complete_original_to_normal_form_relations\":"<<original_relations<<",\n"
     <<"\"original_generator_sign_freedoms\":10,\n\"universal_center_dimension\":3,\n"
     <<"\"full_abelian_relation_rank\":"<<basis.size()<<",\n\"pullback_abelianization_dimension\":"<<13-basis.size()<<",\n"
     <<"\"all_relator_images_central\":true,\n\"all_complete_relations_evaluated\":true,\n"
     <<"\"relation_basis_rows\":[";
    for(unsigned i=0;i<basis.size();++i){if(i)f<<",";f<<basis[i];}f<<"],\n\"relation_basis_word_nodes\":[";
    for(unsigned i=0;i<basis_words.size();++i){if(i)f<<",";f<<basis_words[i];}f<<"],\n\"literal_word_DAG\":[";
    for(unsigned i=0;i<nodes.size();++i){if(i)f<<",";auto n=nodes[i];f<<"["<<n.op<<","<<n.a<<","<<n.b<<"]";}
    f<<"],\n\"seconds\":"<<seconds<<"\n}\n";
  }
};

int main(int argc,char**argv){try{
  if(argc!=4)throw std::runtime_error("usage: executable model.bin perfect_base.bin output.json");
  auto start=std::chrono::steady_clock::now();CentralModel model(argv[1]);auto e=Engine::replay(argv[2]);
  std::cout<<"complete perfect base replay passed"<<std::endl;
  CentralProbe probe(*e,model);probe.run();double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  probe.save(argv[3],seconds);std::cout<<"PASS central pullback rank "<<probe.basis.size()<<" abelian dimension "<<13-probe.basis.size()<<" seconds "<<seconds<<std::endl;return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
