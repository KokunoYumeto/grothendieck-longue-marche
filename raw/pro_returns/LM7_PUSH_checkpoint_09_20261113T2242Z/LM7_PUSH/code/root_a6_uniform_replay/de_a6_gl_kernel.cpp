// Exact elementary-binary extension over the actual A6/A5 joint source.
// The unchanged Schreier engine supplies the complete base presentation.
#define main de_a6_schreier_existing_main
#include "de_a6_schreier.cpp"
#undef main
#include <array>
#include <map>

constexpr int EW=6+36*78, BW=2052, NW=(BW+63)/64;
using Element=std::array<uint8_t,EW>;
using Bits=std::array<uint64_t,NW>;

struct BinarySpan {
  std::map<int,Bits> rows;
  std::vector<Bits> basis;
  std::vector<uint32_t> words;
  static bool zero(const Bits&v){for(auto x:v)if(x)return false;return true;}
  Bits reduce(Bits v) const {
    for(const auto&[p,row]:rows)if((v[p/64]>>(p%64))&1)
      for(int j=0;j<NW;++j)v[j]^=row[j];
    return v;
  }
  bool contains(const Bits&v)const{return zero(reduce(v));}
  bool add(const Bits&v,uint32_t w){
    Bits r=reduce(v);if(zero(r))return false;
    int p=0;while(!r[p/64])p+=64;
    p+=__builtin_ctzll(r[p/64]);
    if(p>=BW)throw std::runtime_error("binary width");
    rows.emplace(p,r);basis.push_back(v);words.push_back(w);return true;
  }
};

struct Model {
  uint8_t sm[120][120],si[120],om[120][120],oi[120],au[120][120];
  uint8_t rm[4][16],cm[16][4],mm[16][16],mi[16],dot[4][4];
  uint32_t sid,z,oid;
  Element one;std::vector<Element> original;
  std::vector<P> base_original;
  BinarySpan upper;
  unsigned controls=0,kernel_controls=0;
  template<class T>static T integer(std::istream&f){T v;f.read((char*)&v,sizeof(T));if(!f)throw std::runtime_error("short model");return v;}
  static Element element(std::istream&f){Element a;f.read((char*)a.data(),EW);if(!f)throw std::runtime_error("short element");return a;}
  static int parity(unsigned x){return __builtin_parity(x);}
  void tables(){
    for(int e=0;e<4;++e)for(int f=0;f<4;++f)dot[e][f]=parity(e&f);
    for(int m=0;m<16;++m){
      mi[m]=((m&1)<<3)|(m&6)|((m&8)>>3);
      for(int e=0;e<4;++e){
        rm[e][m]=parity(e&((m&1)|((m&4)>>1)))
                 |(parity(e&((m&2)>>1|((m&8)>>2)))<<1);
        cm[m][e]=parity((m&3)&e)|(parity(((m>>2)&3)&e)<<1);
      }
    }
    for(int m=0;m<16;++m)for(int n=0;n<16;++n)
      mm[m][n]=rm[m&3][n]|(rm[(m>>2)&3][n]<<2);
  }
  void hmul(const uint8_t*a,const uint8_t*b,uint8_t*c)const {
    const unsigned M=a[57],N=b[57],u=b[77];
    for(int j=0;j<19;++j){
      unsigned p=a[j],aut=a[19+j];
      c[j]=b[p];c[19+j]=om[aut][b[19+p]];
      c[38+j]=rm[a[38+j]][N]^b[38+p];
      unsigned acted=au[aut][b[58+p]];
      if(dot[a[38+j]][u])acted=sm[z][acted];
      c[58+j]=sm[a[58+j]][acted];
    }
    c[57]=mm[M][N];c[77]=a[77]^cm[M][u];
  }
  void hinv(const uint8_t*a,uint8_t*b)const {
    unsigned M=mi[a[57]],t=a[77];
    for(int j=0;j<19;++j)b[a[j]]=j;
    for(int j=0;j<19;++j){
      unsigned q=b[j],aut=oi[a[19+q]];
      b[19+j]=aut;b[38+j]=rm[a[38+q]][M];
      unsigned k=au[aut][si[a[58+q]]];
      if(dot[b[38+j]][t])k=sm[z][k];
      b[58+j]=k;
    }
    b[57]=M;b[77]=cm[M][t];
  }
  Element mul(const Element&a,const Element&b)const {
    Element c;
    for(int q=0;q<6;++q){c[q]=b[a[q]];
      for(int i=0;i<6;++i)hmul(a.data()+6+(6*q+i)*78,
        b.data()+6+(6*a[q]+i)*78,c.data()+6+(6*q+i)*78);
    }return c;
  }
  Element inv(const Element&a)const {
    Element b;for(int q=0;q<6;++q)b[a[q]]=q;
    for(int q=0;q<6;++q)for(int i=0;i<6;++i)
      hinv(a.data()+6+(6*b[q]+i)*78,b.data()+6+(6*q+i)*78);
    return b;
  }
  Element comm(const Element&a,const Element&b)const{return mul(mul(mul(a,b),inv(a)),inv(b));}
  Element conj(const Element&a,const Element&b)const{return mul(mul(a,b),inv(a));}
  Bits vector(const Element&a)const {
    Bits v{};
    for(int q=0;q<6;++q)if(a[q]!=q)throw std::runtime_error("nonkernel coset action");
    auto bit=[&](int i){v[i/64]|=uint64_t(1)<<(i%64);};
    for(int k=0;k<36;++k){const uint8_t*h=a.data()+6+k*78;
      if(h[57]!=9||h[77])throw std::runtime_error("nonkernel affine action");
      for(int j=0;j<19;++j){
        if(h[j]!=j||h[19+j]!=oid)throw std::runtime_error("nonkernel A5 action");
        if(h[58+j]!=sid&&h[58+j]!=z)throw std::runtime_error("noncentral SL2 value");
        if(h[58+j]==z)bit(57*k+j);
        if(h[38+j]&1)bit(57*k+19+2*j);
        if(h[38+j]&2)bit(57*k+20+2*j);
      }
    }return v;
  }
  Element kernel(const Bits&v)const {
    Element a=one;
    auto bit=[&](int i){return(v[i/64]>>(i%64))&1;};
    for(int k=0;k<36;++k){uint8_t*h=a.data()+6+k*78;
      for(int j=0;j<19;++j){h[58+j]=bit(57*k+j)?z:sid;
        h[38+j]=bit(57*k+19+2*j)|(bit(57*k+20+2*j)<<1);}
    }return a;
  }
  static Bits readbits(std::istream&f){
    Bits b{};for(int j=0;j<BW;++j){unsigned v=integer<uint8_t>(f);if(v>1)throw std::runtime_error("invalid binary coordinate");if(v)b[j/64]|=uint64_t(1)<<(j%64);}return b;
  }
  explicit Model(const std::string&name){
    tables();std::ifstream f(name,std::ios::binary);
    if(integer<uint32_t>(f)!=0xA6F105C1||integer<uint32_t>(f)!=1||integer<uint32_t>(f)!=EW)
      throw std::runtime_error("model header");
    sid=integer<uint32_t>(f);z=integer<uint32_t>(f);oid=integer<uint32_t>(f);
    if(sid>=120||z>=120||oid>=120)throw std::runtime_error("identity indices");
    f.read((char*)sm,sizeof(sm));f.read((char*)si,sizeof(si));
    f.read((char*)om,sizeof(om));f.read((char*)oi,sizeof(oi));f.read((char*)au,sizeof(au));
    if(!f)throw std::runtime_error("short tables");
    one=element(f);original={element(f),element(f)};
    if(mul(one,one)!=one||inv(one)!=one)throw std::runtime_error("model identity");
    std::vector<Element> values{one,original[0],original[1]};
    controls=integer<uint32_t>(f);
    for(unsigned i=0;i<controls;++i){unsigned op=integer<uint32_t>(f),a=integer<uint32_t>(f),b=integer<uint32_t>(f);
      if(a>=values.size()||b>=values.size())throw std::runtime_error("control DAG");
      Element c=op==2?mul(values[a],values[b]):op==3?inv(values[a]):op==4?comm(values[a],values[b]):conj(values[a],values[b]);
      if(c!=element(f))throw std::runtime_error("Python/C++ multiplication control");values.push_back(c);
    }
    if(integer<uint32_t>(f)!=BW||integer<uint32_t>(f)!=44)throw std::runtime_error("upper kernel size");
    for(int i=0;i<44;++i)if(!upper.add(readbits(f),i))throw std::runtime_error("upper kernel rank");
    kernel_controls=integer<uint32_t>(f);
    for(unsigned i=0;i<kernel_controls;++i){Element a=element(f);Bits b=readbits(f);
      if(vector(a)!=b||kernel(b)!=a||!upper.contains(b))throw std::runtime_error("kernel coordinate control");
    }
    unsigned n=integer<uint32_t>(f),m=integer<uint32_t>(f);if(m!=2||n>65535)throw std::runtime_error("base header");
    base_original.resize(m,P(n));for(auto&p:base_original)f.read((char*)p.data(),n*sizeof(uint16_t));
    if(!f||f.peek()!=EOF)throw std::runtime_error("model file length");
    if(mul(original[0],original[0])!=one||mul(mul(original[1],original[1]),original[1])!=one)
      throw std::runtime_error("actual B source relations");
  }
};

struct Lifted {
  Model&m;Engine&e;std::vector<Node> nodes;std::vector<Element> values;
  BinarySpan span;uint64_t relations=0,normal_additions=0;
  Lifted(Model&model,Engine&engine):m(model),e(engine){
    // Rebuild the same transversals with their literal word nodes retained.
    std::vector<int> bases;for(auto&l:e.chain)bases.push_back(l.base);
    e.chain.clear();for(int b:bases)e.new_level(b);
    for(unsigned j=0;j<e.gens.size();++j)for(int k=0;k<=e.gens[j].depth;++k)e.extend(k,j,true);
    nodes=e.nodes;values.reserve(nodes.size()+20000);
    for(unsigned j=0;j<nodes.size();++j){auto n=nodes[j];Element v;
      if(n.op==0)v=m.one;else if(n.op==1)v=m.original.at(n.a);
      else if(n.op==2)v=m.mul(values.at(n.a),values.at(n.b));
      else if(n.op==3)v=m.inv(values.at(n.a));
      else if(n.op==4)v=m.comm(values.at(n.a),values.at(n.b));
      else if(n.op==5)v=m.conj(values.at(n.a),values.at(n.b));
      else throw std::runtime_error("word operation");values.push_back(v);
    }
  }
  uint32_t product(uint32_t a,uint32_t b){if(!a)return b;if(!b)return a;
    auto v=m.mul(values.at(a),values.at(b));nodes.push_back({2,a,b});values.push_back(v);return nodes.size()-1;}
  uint32_t inverse(uint32_t a){if(!a)return 0;auto v=m.inv(values.at(a));nodes.push_back({3,a,0});values.push_back(v);return nodes.size()-1;}
  void normal_close(){
    for(unsigned at=0;at<span.basis.size();++at)for(unsigned j=0;j<m.original.size();++j){
      auto a=m.conj(m.original[j],m.kernel(span.basis[at]));Bits v=m.vector(a);
      if(!m.upper.contains(v))throw std::runtime_error("normal image exceeds known GL kernel");
      if(!span.contains(v)){
        uint32_t g=e.original_nodes.empty()?j+1:e.original_nodes[j];
        // Replay does not populate original_nodes; the original DAG has the
        // two generator nodes immediately after its identity.
        if(nodes.at(g).op!=1||nodes[g].a!=j)throw std::runtime_error("original word node");
        uint32_t w=product(product(g,span.words[at]),inverse(g));
        if(values[w]!=a)throw std::runtime_error("normal word lift");
        span.add(v,w);++normal_additions;
      }
    }
  }
  bool solve(){
    for(int lev=(int)e.chain.size()-1;lev>=0;--lev){auto&l=e.chain[lev];
      unsigned old=span.basis.size();
      for(unsigned at=0;at<l.orbit.size();++at)for(unsigned gi=0;gi<e.gens.size();++gi){
        if(e.gens[gi].depth<lev)continue;
        int to=l.pos[e.gens[gi].p[l.orbit[at]]];if(to<0)throw std::runtime_error("base orbit edge");
        P h=e.mul(e.mul(l.trans[at],e.gens[gi].p),l.inv[to]);
        Element v=m.mul(m.mul(values[l.word[at]],values[e.gens[gi].node]),m.inv(values[l.word[to]]));
        std::vector<std::pair<uint32_t,bool>> history{{l.word[at],false},{e.gens[gi].node,false},{l.word[to],true}};
        for(int k=lev+1;k<(int)e.chain.size();++k){auto&c=e.chain[k];int b=h[c.base];if(b==c.base)continue;
          int pos=c.pos[b];if(pos<0)throw std::runtime_error("complete base relation missing");
          h=e.mul(h,c.inv[pos]);v=m.mul(v,m.inv(values[c.word[pos]]));history.push_back({c.word[pos],true});
        }
        if(!e.identity(h))throw std::runtime_error("nonidentity base relator");
        ++relations;Bits b=m.vector(v);
        if(!m.upper.contains(b))throw std::runtime_error("relator exceeds known GL kernel");
        if(!span.contains(b)){
          uint32_t w=0;for(auto[a,inv]:history)w=product(w,inv?inverse(a):a);
          if(values[w]!=v)throw std::runtime_error("relator word lift");
          span.add(b,w);normal_close();
          std::cout<<"new kernel rank "<<span.basis.size()<<" relations "<<relations<<" level "<<lev<<std::endl;
          if(span.basis.size()==m.upper.basis.size())return false;
        }
      }
      std::cout<<"Schreier level "<<lev<<" orbit "<<l.orbit.size()<<" relations "<<relations
               <<" kernel rank "<<span.basis.size()<<" new "<<span.basis.size()-old<<std::endl;
    }
    return true;
  }
  void save(const std::string&file,bool complete,double seconds){
    normal_close();
    for(const auto&b:span.basis)for(auto&g:m.original)
      if(!span.contains(m.vector(m.conj(g,m.kernel(b)))))throw std::runtime_error("final normal closure");
    if(!complete&&span.basis.size()!=44)throw std::runtime_error("incomplete kernel bound");
    if(complete&&relations!=e.final_relations)throw std::runtime_error("Schreier count mismatch");
    std::ofstream f(file);if(!f)throw std::runtime_error("kernel output");
    f<<"{\n\"status\":\"PASS_COMPLETE_JOINT_KERNEL\",\n\"base_order\":\""<<e.order()<<"\",\n"
     <<"\"base_degree\":"<<e.n<<",\n\"kernel_width\":"<<BW<<",\n\"kernel_dimension\":"<<span.basis.size()<<",\n"
     <<"\"known_GL_kernel_dimension\":44,\n\"full_base_chain_replayed\":true,\n"
     <<"\"all_Schreier_relators_evaluated\":"<<(complete?"true":"false")<<",\n"
     <<"\"exact_upper_bound_attained\":"<<(span.basis.size()==44?"true":"false")<<",\n"
     <<"\"lifted_relators_evaluated\":"<<relations<<",\n\"complete_base_relator_count\":"<<e.final_relations<<",\n"
     <<"\"normal_closure_additions\":"<<normal_additions<<",\n"
     <<"\"literal_word_DAG\":[";
    for(unsigned i=0;i<nodes.size();++i){if(i)f<<",";auto n=nodes[i];f<<"["<<n.op<<","<<n.a<<","<<n.b<<"]";}f<<"],\n";
    f<<"\"kernel_basis_word_nodes\":[";for(unsigned i=0;i<span.words.size();++i){if(i)f<<",";f<<span.words[i];}f<<"],\n";
    f<<"\"kernel_basis_supports\":[";for(unsigned i=0;i<span.basis.size();++i){if(i)f<<",";f<<"[";bool first=true;
      for(int p=0;p<BW;++p)if((span.basis[i][p/64]>>(p%64))&1){if(!first)f<<",";first=false;f<<p;}f<<"]";}f<<"],\n";
    f<<"\"independent_Python_operation_controls\":"<<m.controls<<",\n\"kernel_coordinate_controls\":"<<m.kernel_controls
     <<",\n\"seconds\":"<<seconds<<"\n}\n";
  }
};

int main(int argc,char**argv){try{
  if(argc!=4)throw std::runtime_error("usage: executable model.bin base_certificate.bin output.json");
  auto start=std::chrono::steady_clock::now();Model model(argv[1]);
  std::cout<<"exact Python/model controls passed; replaying complete base certificate"<<std::endl;
  auto e=Engine::replay(argv[2]);
  if(e->original!=model.base_original)throw std::runtime_error("literal original source generators differ");
  std::cout<<"base replay passed; order "<<e->order()<<" relators "<<e->final_relations<<std::endl;
  Lifted lifted(model,*e);bool complete=lifted.solve();
  double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  lifted.save(argv[3],complete,seconds);
  std::cout<<"PASS joint kernel dimension "<<lifted.span.basis.size()<<" complete "<<complete<<" seconds "<<seconds<<std::endl;
  return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
