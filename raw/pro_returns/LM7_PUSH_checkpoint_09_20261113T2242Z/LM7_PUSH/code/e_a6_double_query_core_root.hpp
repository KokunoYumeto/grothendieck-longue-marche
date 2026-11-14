// Exact central coinvariant presentation over the certified perfect C.
// Original generator coefficients and every central shift are retained.
#define main de_a6_schreier_existing_main
#include "de_a6_schreier.cpp"
#undef main
#include "e_a6_double_core_root.hpp"

constexpr unsigned NG=10,NC=30,RC=NG+NC;
using Row=std::array<uint8_t,RC>;
using Exponents=std::array<uint8_t,NG>;

struct CentralData {
  Model&m;std::array<unsigned,128>pivots;uint8_t projection[NC][128];
  BinarySpan upper;std::vector<Element>original;std::vector<P>base_original;
  CentralData(Model&model,const std::string&name):m(model){
    std::ifstream f(name,std::ios::binary);
    if(Model::integer<uint32_t>(f)!=0xA62CE001||Model::integer<uint32_t>(f)!=1
       ||Model::integer<uint32_t>(f)!=NG||Model::integer<uint32_t>(f)!=128||Model::integer<uint32_t>(f)!=NC)
      throw std::runtime_error("central header");
    unsigned n=Model::integer<uint32_t>(f);if(n>65535||Model::integer<uint32_t>(f)!=BW)throw std::runtime_error("central dimensions");
    for(auto&p:pivots){p=Model::integer<uint32_t>(f);if(p>=BW)throw std::runtime_error("central pivot range");}
    f.read((char*)projection,sizeof(projection));if(!f)throw std::runtime_error("central projection");
    for(auto&row:projection)for(auto a:row)if(a>1)throw std::runtime_error("central coefficient range");
    for(unsigned i=0;i<128;++i)if(!upper.add(Model::readvector(f),i))throw std::runtime_error("known kernel rank");
    for(unsigned i=0;i<NG;++i)original.push_back(Model::element(f));
    base_original.resize(NG,P(n));for(auto&p:base_original)f.read((char*)p.data(),2*n);
    if(!f||f.peek()!=EOF)throw std::runtime_error("central model length");
  }
  std::array<uint8_t,NC>central(const Element&e)const{
    auto v=m.vector(e);if(!upper.contains(v))throw std::runtime_error("central relator outside full source kernel");
    unsigned a[128];for(unsigned j=0;j<128;++j)a[j]=BinarySpan::coefficient(v,pivots[j]);
    std::array<uint8_t,NC>out{};for(unsigned i=0;i<NC;++i){unsigned z=0;
      for(unsigned j=0;j<128;++j)z+=projection[i][j]*a[j];out[i]=z%2;}
    return out;
  }
};

struct CentralProbe {
  Engine&e;Model&m;CentralData&c;std::vector<Node>nodes;
  std::vector<Element>values,inverses;std::vector<Exponents>exponents;
  std::map<unsigned,Row>rows;std::vector<Row>basis;std::vector<uint32_t>basis_words;
  uint64_t relations=0;unsigned original_relations=0;
  static Exponents plus(const Exponents&a,const Exponents&b,int sign=1){Exponents r;
    for(unsigned i=0;i<NG;++i)r[i]=(a[i]+2+sign*b[i])%2;return r;}
  CentralProbe(Engine&engine,Model&model,CentralData&central):e(engine),m(model),c(central){
    if(e.original!=c.base_original)throw std::runtime_error("literal C originals differ");
    std::vector<int>bases;for(auto&l:e.chain)bases.push_back(l.base);e.chain.clear();
    for(int b:bases)e.new_level(b);
    for(unsigned j=0;j<e.gens.size();++j)for(int k=0;k<=e.gens[j].depth;++k)e.extend(k,j,true);
    nodes=e.nodes;values.reserve(nodes.size()+2000);inverses.reserve(nodes.size()+2000);
    for(auto n:nodes){Element v;Exponents a{};
      if(n.op==0)v=m.one;else if(n.op==1){v=c.original.at(n.a);a[n.a]=1;}
      else if(n.op==2){v=m.mul(values.at(n.a),values.at(n.b));a=plus(exponents[n.a],exponents[n.b]);}
      else if(n.op==3){v=inverses.at(n.a);a=plus(a,exponents[n.a],-1);}
      else if(n.op==4)v=m.mul(m.mul(m.mul(values.at(n.a),values.at(n.b)),inverses.at(n.a)),inverses.at(n.b));
      else if(n.op==5){v=m.mul(m.mul(values.at(n.a),values.at(n.b)),inverses.at(n.a));a=exponents[n.b];}
      else throw std::runtime_error("central word operation");
      values.push_back(v);inverses.push_back(m.inv(v));exponents.push_back(a);
    }
  }
  Row reduce(Row v)const{for(auto[p,row]:rows)if(v[p]){unsigned a=v[p];for(unsigned j=0;j<RC;++j)v[j]=(v[j]+6-a*row[j])%2;}return v;}
  uint32_t product(uint32_t a,uint32_t b){if(!a)return b;if(!b)return a;Element v=m.mul(values[a],values[b]);
    nodes.push_back({2,a,b});values.push_back(v);inverses.push_back(m.inv(v));exponents.push_back(plus(exponents[a],exponents[b]));return nodes.size()-1;}
  uint32_t inverse(uint32_t a){if(!a)return 0;Element v=inverses[a];Exponents z{};
    nodes.push_back({3,a,0});values.push_back(v);inverses.push_back(values[a]);exponents.push_back(plus(z,exponents[a],-1));return nodes.size()-1;}
  void relation(const Element&v,const Exponents&ab,const std::vector<std::pair<uint32_t,bool>>&history){
    auto cv=c.central(v);Row row{};for(unsigned j=0;j<NG;++j)row[j]=ab[j];
    // The literal relation is R(c_i)=k: exponent sum minus its central
    // kernel coordinate; subtraction agrees with addition in characteristic two.
    for(unsigned j=0;j<NC;++j)row[NG+j]=(2-cv[j])%2;
    auto r=reduce(row);unsigned pivot=0;while(pivot<RC&&!r[pivot])++pivot;if(pivot==RC)return;
    unsigned scale=r[pivot];for(auto&a:r)a=scale*a%2;
    uint32_t w=0;for(auto[a,invert]:history)w=product(w,invert?inverse(a):a);
    if(values[w]!=v||exponents[w]!=ab)throw std::runtime_error("central relation word replay");
    rows.emplace(pivot,r);basis.push_back(row);basis_words.push_back(w);
    std::cout<<"central relation rank "<<basis.size()<<" relators "<<relations<<" originals "<<original_relations<<std::endl;
  }
  void original_links(){
    for(unsigned j=0;j<NG;++j){uint32_t node=j+1;
      if(nodes.at(node).op!=1||nodes[node].a!=j)throw std::runtime_error("C original node");
      P h=e.original[j];Element v=values[node];Exponents ab=exponents[node];
      std::vector<std::pair<uint32_t,bool>>history{{node,false}};
      for(auto&l:e.chain){int b=h[l.base];if(b==l.base)continue;int at=l.pos[b];if(at<0)throw std::runtime_error("C original normal form");
        h=e.mul(h,l.inv[at]);v=m.mul(v,inverses[l.word[at]]);ab=plus(ab,exponents[l.word[at]],-1);history.push_back({l.word[at],true});}
      if(!e.identity(h))throw std::runtime_error("C original residue");++original_relations;relation(v,ab,history);
    }
  }
  bool run(){
    original_links();
    for(int lev=(int)e.chain.size()-1;lev>=0;--lev){auto&l=e.chain[lev];
      for(unsigned at=0;at<l.orbit.size();++at)for(auto&g:e.gens){if(g.depth<lev)continue;
        int to=l.pos[g.p[l.orbit[at]]];if(to<0)throw std::runtime_error("C orbit edge");
        P h=e.mul(e.mul(l.trans[at],g.p),l.inv[to]);
        Element v=m.mul(m.mul(values[l.word[at]],values[g.node]),inverses[l.word[to]]);
        Exponents ab=plus(plus(exponents[l.word[at]],exponents[g.node]),exponents[l.word[to]],-1);
        std::vector<std::pair<uint32_t,bool>>history{{l.word[at],false},{g.node,false},{l.word[to],true}};
        for(int k=lev+1;k<(int)e.chain.size();++k){auto&z=e.chain[k];int b=h[z.base];if(b==z.base)continue;
          int at2=z.pos[b];if(at2<0)throw std::runtime_error("C relation outside complete chain");
          h=e.mul(h,z.inv[at2]);v=m.mul(v,inverses[z.word[at2]]);ab=plus(ab,exponents[z.word[at2]],-1);history.push_back({z.word[at2],true});}
        if(!e.identity(h))throw std::runtime_error("nonidentity C base relation");++relations;relation(v,ab,history);
        if(basis.size()==RC)return false;
      }
      if(lev%10==0)std::cout<<"C level "<<lev<<" relators "<<relations<<" rank "<<basis.size()<<std::endl;
    }
    if(relations!=e.final_relations)throw std::runtime_error("complete C relation count");return true;
  }
  void save(const std::string&name,bool complete,double seconds){
    if(!complete&&basis.size()!=RC)throw std::runtime_error("incomplete rank bound");
    if(original_relations!=NG)throw std::runtime_error("missing C original links");
    std::ofstream f(name);if(!f)throw std::runtime_error("output");
    f<<"{\n\"status\":\"PASS_EXACT_CENTRAL_COINVARIANT_PRESENTATION\",\n\"base_C_order\":\""<<e.order()<<"\",\n"
     <<"\"base_degree\":"<<e.n<<",\n\"original_generator_count\":"<<NG
     <<",\n\"central_quotient_dimension\":"<<NC<<",\n\"all_original_central_shift_parameters\":"<<NG*NC
     <<",\n\"abelian_relation_rank\":"<<basis.size()<<",\n\"preimage_abelianization_dimension\":"<<RC-basis.size()
     <<",\n\"Schreier_relations_evaluated\":"<<relations<<",\n\"complete_base_relation_count\":"<<e.final_relations
     <<",\n\"all_complete_relations_evaluated\":"<<(complete?"true":"false")
     <<",\n\"full_abelian_rank_upper_bound_attained\":"<<(basis.size()==RC?"true":"false")
     <<",\n\"all_ten_original_to_normal_form_relations_evaluated\":true,\n\"relation_basis_rows\":[";
    for(unsigned i=0;i<basis.size();++i){if(i)f<<",";f<<"[";for(unsigned j=0;j<RC;++j){if(j)f<<",";f<<unsigned(basis[i][j]);}f<<"]";}
    f<<"],\n\"relation_basis_word_nodes\":[";for(unsigned i=0;i<basis_words.size();++i){if(i)f<<",";f<<basis_words[i];}
    f<<"],\n\"literal_C_generator_word_DAG\":[";
    for(unsigned i=0;i<nodes.size();++i){if(i)f<<",";auto n=nodes[i];f<<"["<<n.op<<","<<n.a<<","<<n.b<<"]";}
    f<<"],\n\"seconds\":"<<seconds<<"\n}\n";
  }
};

