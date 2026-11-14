// Exact binary kernel over the unchanged complete A6 source certificate.
// The appended Schreier enumeration is shared with the audited ternary collector.
#define main de_a6_schreier_existing_main
#include "de_a6_schreier.cpp"
#undef main
#include <array>
#include <map>

constexpr int HW=212,EW=6+36*HW,BW=36*159,NW=(BW+63)/64;
using Element=std::array<uint16_t,EW>;
struct Binary {std::array<uint64_t,NW>bits{};};

struct BinarySpan {
  std::map<int,Binary>rows;
  std::vector<Binary>basis;
  std::vector<uint32_t>words;
  static unsigned coefficient(const Binary&v,int p){return (v.bits[p/64]>>(p%64))&1;}
  static void put(Binary&v,int p,unsigned a){
    if(p<0||p>=BW||a>1)throw std::runtime_error("binary coordinate");
    if(a)v.bits[p/64]|=uint64_t(1)<<(p%64);
  }
  static bool zero(const Binary&v){for(auto w:v.bits)if(w)return false;return true;}
  static bool equal(const Binary&a,const Binary&b){return a.bits==b.bits;}
  Binary reduce(Binary v)const{
    for(const auto&[p,row]:rows)if(coefficient(v,p))for(int j=0;j<NW;++j)v.bits[j]^=row.bits[j];
    return v;
  }
  bool contains(const Binary&v)const{return zero(reduce(v));}
  bool add(const Binary&v,uint32_t word){
    Binary r=reduce(v);if(zero(r))return false;
    int j=0;while(!r.bits[j])++j;int p=64*j+__builtin_ctzll(r.bits[j]);
    if(p>=BW)throw std::runtime_error("binary width");
    rows.emplace(p,r);basis.push_back(v);words.push_back(word);return true;
  }
};

struct Model {
  std::vector<uint16_t>um,ui,am,ai,au;
  std::array<uint8_t,1440>character;
  uint16_t zp[2];std::array<int,720>zlog;
  uint32_t uid,z,autone,controls=0,kernel_controls=0;
  Element one;std::vector<Element>original;std::vector<P>base_original;
  template<class T>static T integer(std::istream&f){T v;f.read((char*)&v,sizeof(T));if(!f)throw std::runtime_error("short model");return v;}
  static Element element(std::istream&f){Element a;f.read((char*)a.data(),2*EW);if(!f)throw std::runtime_error("short element");return a;}
  static std::vector<uint16_t>table(std::istream&f,size_t n){std::vector<uint16_t>v(n);f.read((char*)v.data(),2*n);if(!f)throw std::runtime_error("short table");return v;}
  void hmul(const uint16_t*a,const uint16_t*b,uint16_t*c)const{
    for(int j=0;j<53;++j){unsigned p=a[j],alpha=a[53+j];
      c[j]=b[p];c[53+j]=am[1440*alpha+b[53+p]];
      c[106+j]=a[106+j]^b[106+p];
      c[159+j]=um[720*a[159+j]+au[720*alpha+b[159+p]]];
    }
  }
  void hinv(const uint16_t*a,uint16_t*b)const{
    for(int j=0;j<53;++j)b[a[j]]=j;
    for(int j=0;j<53;++j){unsigned q=b[j],beta=ai[a[53+q]];
      b[53+j]=beta;b[106+j]=a[106+q];
      b[159+j]=au[720*beta+ui[a[159+q]]];
    }
  }
  Element mul(const Element&a,const Element&b)const{
    Element c;for(int q=0;q<6;++q){c[q]=b[a[q]];
      for(int i=0;i<6;++i)hmul(a.data()+6+(6*q+i)*HW,b.data()+6+(6*a[q]+i)*HW,c.data()+6+(6*q+i)*HW);
    }return c;
  }
  Element inv(const Element&a)const{
    Element b;for(int q=0;q<6;++q)b[a[q]]=q;
    for(int q=0;q<6;++q)for(int i=0;i<6;++i)hinv(a.data()+6+(6*b[q]+i)*HW,b.data()+6+(6*q+i)*HW);
    return b;
  }
  Element comm(const Element&a,const Element&b)const{return mul(mul(mul(a,b),inv(a)),inv(b));}
  Element conj(const Element&a,const Element&b)const{return mul(mul(a,b),inv(a));}
  Binary vector(const Element&a)const{
    Binary v;
    for(int q=0;q<6;++q)if(a[q]!=q)throw std::runtime_error("nonkernel coset permutation");
    for(int k=0;k<36;++k){const uint16_t*h=a.data()+6+k*HW;
      for(int j=0;j<53;++j){
        if(h[j]!=j||h[53+j]!=autone)throw std::runtime_error("nonkernel A6 automorphism");
        if(h[159+j]>=720||zlog[h[159+j]]<0)throw std::runtime_error("noncentral cover value");
        if(h[106+j]>=4)throw std::runtime_error("binary character range");
        BinarySpan::put(v,159*k+j,zlog[h[159+j]]);
        BinarySpan::put(v,159*k+53+2*j,h[106+j]%2);
        BinarySpan::put(v,159*k+54+2*j,h[106+j]/2);
      }
    }return v;
  }
  Element kernel(const Binary&v)const{
    Element a=one;for(int k=0;k<36;++k){uint16_t*h=a.data()+6+k*HW;
      for(int j=0;j<53;++j){h[159+j]=zp[BinarySpan::coefficient(v,159*k+j)];
        h[106+j]=BinarySpan::coefficient(v,159*k+53+2*j)+2*BinarySpan::coefficient(v,159*k+54+2*j);}
    }return a;
  }
  static Binary readvector(std::istream&f){Binary v;
    for(int j=0;j<BW;++j)BinarySpan::put(v,j,integer<uint8_t>(f));return v;}
  explicit Model(const std::string&name){
    std::ifstream f(name,std::ios::binary);
    if(integer<uint32_t>(f)!=0xA62F1C01||integer<uint32_t>(f)!=1||integer<uint32_t>(f)!=EW)throw std::runtime_error("model header");
    uid=integer<uint32_t>(f);z=integer<uint32_t>(f);autone=integer<uint32_t>(f);
    if(uid>=720||z>=720||autone>=1440)throw std::runtime_error("identity indices");
    um=table(f,720*720);ui=table(f,720);am=table(f,1440*1440);ai=table(f,1440);au=table(f,1440*720);
    for(auto v:um)if(v>=720)throw std::runtime_error("cover table range");
    for(auto v:ui)if(v>=720)throw std::runtime_error("cover inverse range");
    for(auto v:am)if(v>=1440)throw std::runtime_error("automorphism table range");
    for(auto v:ai)if(v>=1440)throw std::runtime_error("automorphism inverse range");
    for(auto v:au)if(v>=720)throw std::runtime_error("automorphism action range");
    f.read((char*)character.data(),1440);if(!f)throw std::runtime_error("central character table");
    for(auto v:character)if(v!=1)throw std::runtime_error("nontrivial binary central character");
    zp[0]=uid;zp[1]=z;zlog.fill(-1);zlog[uid]=0;zlog[z]=1;
    if(z==uid||um[720*z+z]!=uid)throw std::runtime_error("central involution");
    one=element(f);original={element(f),element(f)};
    if(mul(one,one)!=one||inv(one)!=one)throw std::runtime_error("model identity");
    std::vector<Element>values{one,original[0],original[1]};controls=integer<uint32_t>(f);
    for(unsigned i=0;i<controls;++i){unsigned op=integer<uint32_t>(f),a=integer<uint32_t>(f),b=integer<uint32_t>(f);
      if(a>=values.size()||b>=values.size()||op<2||op>5)throw std::runtime_error("control DAG");
      Element v=op==2?mul(values[a],values[b]):op==3?inv(values[a]):op==4?comm(values[a],values[b]):conj(values[a],values[b]);
      if(v!=element(f))throw std::runtime_error("independent Python group control");values.push_back(v);
    }
    if(integer<uint32_t>(f)!=BW)throw std::runtime_error("kernel width");kernel_controls=integer<uint32_t>(f);
    for(unsigned i=0;i<kernel_controls;++i){Element e=element(f);Binary v=readvector(f);
      if(!BinarySpan::equal(vector(e),v)||kernel(v)!=e)throw std::runtime_error("independent Python kernel control");}
    unsigned n=integer<uint32_t>(f),m=integer<uint32_t>(f);if(n>65535||m!=2)throw std::runtime_error("base size");
    base_original.resize(2,P(n));for(auto&p:base_original)f.read((char*)p.data(),2*n);
    if(!f||f.peek()!=EOF)throw std::runtime_error("model file length");
    if(mul(original[0],original[0])!=one||mul(mul(original[1],original[1]),original[1])!=one)throw std::runtime_error("B source torsion relations");
  }
};

struct LiftedKernel {
  Model&m;Engine&e;std::vector<Node>nodes;std::vector<Element>values,inverses;
  BinarySpan span;uint64_t relations=0,normal_additions=0;
  LiftedKernel(Model&model,Engine&engine):m(model),e(engine){
    if(e.derived_mode||e.original.size()!=2)throw std::runtime_error("ordinary base required");
    for(unsigned j=0;j<2;++j){bool found=false;for(auto&g:e.gens)if(g.node==j+1&&g.p==e.original[j])found=true;
      if(!found)throw std::runtime_error("original strong generator missing");}
    std::vector<int>bases;for(auto&c:e.chain)bases.push_back(c.base);e.chain.clear();
    for(int b:bases)e.new_level(b);
    for(unsigned j=0;j<e.gens.size();++j)for(int k=0;k<=e.gens[j].depth;++k)e.extend(k,j,true);
    nodes=e.nodes;values.reserve(nodes.size()+5000);inverses.reserve(nodes.size()+5000);
    for(auto n:nodes){Element v;
      if(n.op==0)v=m.one;else if(n.op==1)v=m.original.at(n.a);
      else if(n.op==2)v=m.mul(values.at(n.a),values.at(n.b));
      else if(n.op==3)v=inverses.at(n.a);
      else if(n.op==4)v=m.mul(m.mul(m.mul(values.at(n.a),values.at(n.b)),inverses.at(n.a)),inverses.at(n.b));
      else if(n.op==5)v=m.mul(m.mul(values.at(n.a),values.at(n.b)),inverses.at(n.a));
      else throw std::runtime_error("word operation");values.push_back(v);inverses.push_back(m.inv(v));
    }
  }
  uint32_t product(uint32_t a,uint32_t b){if(!a)return b;if(!b)return a;
    Element v=m.mul(values.at(a),values.at(b));nodes.push_back({2,a,b});values.push_back(v);inverses.push_back(m.inv(v));return nodes.size()-1;}
  uint32_t inverse(uint32_t a){if(!a)return 0;Element v=inverses.at(a);nodes.push_back({3,a,0});values.push_back(v);inverses.push_back(values[a]);return nodes.size()-1;}
  void normal_close(){
    for(unsigned at=0;at<span.basis.size();++at)for(unsigned j=0;j<2;++j){
      Element v=m.conj(m.original[j],m.kernel(span.basis[at]));Binary b=m.vector(v);
      if(!span.contains(b)){uint32_t g=j+1;
        if(nodes.at(g).op!=1||nodes[g].a!=j)throw std::runtime_error("original word node");
        uint32_t w=product(product(g,span.words[at]),inverse(g));
        if(values[w]!=v)throw std::runtime_error("normal literal word");span.add(b,w);++normal_additions;}
    }
  }
  void solve(){
    for(int lev=(int)e.chain.size()-1;lev>=0;--lev){auto&l=e.chain[lev];unsigned old=span.basis.size();
      for(unsigned at=0;at<l.orbit.size();++at)for(unsigned gi=0;gi<e.gens.size();++gi){
        const auto&g=e.gens[gi];if(g.depth<lev)continue;
        int to=l.pos[g.p[l.orbit[at]]];if(to<0)throw std::runtime_error("base orbit edge");
        P h=e.mul(e.mul(l.trans[at],g.p),l.inv[to]);
        Element v=m.mul(m.mul(values[l.word[at]],values[g.node]),inverses[l.word[to]]);
        std::vector<std::pair<uint32_t,bool>>history{{l.word[at],false},{g.node,false},{l.word[to],true}};
        for(int k=lev+1;k<(int)e.chain.size();++k){auto&c=e.chain[k];int b=h[c.base];if(b==c.base)continue;
          int pos=c.pos[b];if(pos<0)throw std::runtime_error("incomplete base relation");
          h=e.mul(h,c.inv[pos]);v=m.mul(v,inverses[c.word[pos]]);history.push_back({c.word[pos],true});}
        if(!e.identity(h))throw std::runtime_error("nonidentity base relation");++relations;Binary b=m.vector(v);
        if(!span.contains(b)){uint32_t w=0;for(auto[a,invert]:history)w=product(w,invert?inverse(a):a);
          if(values[w]!=v)throw std::runtime_error("relator literal word");span.add(b,w);normal_close();
          std::cout<<"kernel rank "<<span.basis.size()<<" relators "<<relations<<" level "<<lev<<std::endl;}
      }
      if(lev%5==0||span.basis.size()!=old)std::cout<<"level "<<lev<<" orbit "<<l.orbit.size()<<" relators "<<relations<<" kernel rank "<<span.basis.size()<<std::endl;
    }
    if(relations!=e.final_relations)throw std::runtime_error("complete relator count");
    normal_close();for(const auto&b:span.basis)for(const auto&g:m.original)
      if(!span.contains(m.vector(m.conj(g,m.kernel(b)))))throw std::runtime_error("final normal closure");
  }
  void save(const std::string&name,double seconds){std::ofstream f(name);if(!f)throw std::runtime_error("output");
    f<<"{\n\"status\":\"PASS_COMPLETE_BINARY_SOURCE_KERNEL\",\n\"base_order\":\""<<e.order()<<"\",\n\"base_degree\":"<<e.n
     <<",\n\"kernel_ambient_dimension\":"<<BW<<",\n\"kernel_dimension\":"<<span.basis.size()
     <<",\n\"all_Schreier_relators_evaluated\":true,\n\"relators_evaluated\":"<<relations
     <<",\n\"complete_base_relator_count\":"<<e.final_relations<<",\n\"normal_closure_additions\":"<<normal_additions
     <<",\n\"independent_Python_operation_controls\":"<<m.controls<<",\n\"kernel_coordinate_controls\":"<<m.kernel_controls
     <<",\n\"literal_word_DAG\":[";
    for(unsigned i=0;i<nodes.size();++i){if(i)f<<",";auto n=nodes[i];f<<"["<<n.op<<","<<n.a<<","<<n.b<<"]";}
    f<<"],\n\"kernel_basis_word_nodes\":[";for(unsigned i=0;i<span.words.size();++i){if(i)f<<",";f<<span.words[i];}
    f<<"],\n\"kernel_basis_coordinates\":[";
    for(unsigned i=0;i<span.basis.size();++i){if(i)f<<",";f<<"[";bool first=true;
      for(int p=0;p<BW;++p){unsigned a=BinarySpan::coefficient(span.basis[i],p);if(a){if(!first)f<<",";first=false;f<<"["<<p<<","<<a<<"]";}}f<<"]";}
    f<<"],\n\"seconds\":"<<seconds<<"\n}\n";
  }
};

int main(int argc,char**argv){try{
  if(argc!=4)throw std::runtime_error("usage: executable model.bin base_certificate.bin output.json");
  auto started=std::chrono::steady_clock::now();Model m(argv[1]);
  std::cout<<"all independent Python/packed-model controls passed; replaying base"<<std::endl;
  auto e=Engine::replay(argv[2]);if(e->original!=m.base_original)throw std::runtime_error("actual base generators differ");
  std::cout<<"complete actual base replay passed; relators "<<e->final_relations<<std::endl;
  LiftedKernel lift(m,*e);lift.solve();
  double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();lift.save(argv[3],seconds);
  std::cout<<"PASS complete binary source kernel rank "<<lift.span.basis.size()<<" relations "<<lift.relations<<" seconds "<<seconds<<std::endl;
  return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
