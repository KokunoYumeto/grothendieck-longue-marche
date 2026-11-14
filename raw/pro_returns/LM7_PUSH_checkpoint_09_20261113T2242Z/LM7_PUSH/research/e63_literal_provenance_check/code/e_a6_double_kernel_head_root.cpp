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
