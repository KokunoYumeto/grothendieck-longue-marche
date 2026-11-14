#pragma once
#include <array>
#include <map>
constexpr int HW=214,EW=6+36*HW,BW=36*159,NW=(BW+63)/64;
using Element=std::array<uint16_t,EW>;
struct Ternary {std::array<uint64_t,NW>one{},two{};};

struct TernarySpan {
  std::map<int,Ternary>rows;
  std::vector<Ternary>basis;
  std::vector<uint32_t>words;
  static unsigned coefficient(const Ternary&v,int p){
    uint64_t b=uint64_t(1)<<(p%64);return (v.one[p/64]&b)?1:(v.two[p/64]&b)?2:0;
  }
  static void put(Ternary&v,int p,unsigned a){
    if(p<0||p>=BW||a>2)throw std::runtime_error("ternary coordinate");
    if(a==1)v.one[p/64]|=uint64_t(1)<<(p%64);
    if(a==2)v.two[p/64]|=uint64_t(1)<<(p%64);
  }
  static bool zero(const Ternary&v){for(int j=0;j<NW;++j)if(v.one[j]|v.two[j])return false;return true;}
  static bool equal(const Ternary&a,const Ternary&b){return a.one==b.one&&a.two==b.two;}
  static void subtract(Ternary&v,const Ternary&r,unsigned scalar){
    if(!scalar)return;if(scalar>2)throw std::runtime_error("ternary scalar");
    for(int j=0;j<NW;++j){
      const uint64_t a=v.one[j],b=v.two[j];
      const uint64_t c=scalar==1?r.two[j]:r.one[j],d=scalar==1?r.one[j]:r.two[j];
      v.one[j]=(a&~(c|d))|(c&~(a|b))|(b&d);
      v.two[j]=(b&~(c|d))|(d&~(a|b))|(a&c);
    }
  }
  Ternary reduce(Ternary v)const{
    for(const auto&[p,row]:rows)subtract(v,row,coefficient(v,p));return v;
  }
  bool contains(const Ternary&v)const{return zero(reduce(v));}
  bool add(const Ternary&v,uint32_t word){
    Ternary r=reduce(v);if(zero(r))return false;
    int j=0;while(!(r.one[j]|r.two[j]))++j;
    int p=64*j+__builtin_ctzll(r.one[j]|r.two[j]);if(p>=BW)throw std::runtime_error("ternary width");
    if(coefficient(r,p)==2)std::swap(r.one,r.two);
    rows.emplace(p,r);basis.push_back(v);words.push_back(word);return true;
  }
};

struct Model {
  std::vector<uint16_t>um,ui,am,ai,au;
  std::array<uint8_t,1440>character;
  uint8_t add[9][9],scale[3][9],dot[9][9],rm[9][81],cm[81][9],mm[81][81],mi[81];
  uint16_t zact[3][1080],zp[3];std::array<int,1080>zlog;
  uint32_t uid,z,autone,controls=0,kernel_controls=0;
  Element one;std::vector<Element>original;std::vector<P>base_original;
  template<class T>static T integer(std::istream&f){T v;f.read((char*)&v,sizeof(T));if(!f)throw std::runtime_error("short model");return v;}
  static Element element(std::istream&f){Element a;f.read((char*)a.data(),2*EW);if(!f)throw std::runtime_error("short element");return a;}
  static std::vector<uint16_t>table(std::istream&f,size_t n){std::vector<uint16_t>v(n);f.read((char*)v.data(),2*n);if(!f)throw std::runtime_error("short table");return v;}
  void tables(){
    for(int a=0;a<9;++a)for(int b=0;b<9;++b){
      add[a][b]=((a%3+b%3)%3)+3*((a/3+b/3)%3);dot[a][b]=((a%3)*(b%3)+(a/3)*(b/3))%3;
    }
    for(int c=0;c<3;++c)for(int a=0;a<9;++a)scale[c][a]=(c*(a%3)%3)+3*(c*(a/3)%3);
    for(int m=0;m<81;++m){int a=m%3,b=m/3%3,c=m/9%3,d=m/27;
      int det=(a*d-b*c+9)%3;
      mi[m]=det?((det*d)%3)+3*((det*(3-b))%3)+9*((det*(3-c))%3)+27*((det*a)%3):0;
      for(int v=0;v<9;++v){int u=v%3,w=v/3;
        rm[v][m]=(u*a+w*c)%3+3*((u*b+w*d)%3);
        cm[m][v]=(a*u+b*w)%3+3*((c*u+d*w)%3);
      }
    }
    for(int m=0;m<81;++m)for(int n=0;n<81;++n)
      mm[m][n]=rm[m%9][n]+9*rm[m/9][n];
    if(mi[28]!=28||mm[28][28]!=28)throw std::runtime_error("matrix identity table");
    for(unsigned a=0;a<3;++a)for(unsigned b=0;b<3;++b)for(unsigned c=0;c<3;++c){
      Ternary v,r;TernarySpan::put(v,0,a);TernarySpan::put(r,0,b);TernarySpan::subtract(v,r,c);
      if(TernarySpan::coefficient(v,0)!=(a+9-c*b)%3)throw std::runtime_error("packed ternary arithmetic");
    }
  }
  void hmul(const uint16_t*a,const uint16_t*b,uint16_t*c)const{
    unsigned M=a[159],N=b[159],u=b[213];
    for(int j=0;j<53;++j){unsigned p=a[j],alpha=a[53+j];
      c[j]=b[p];c[53+j]=am[1440*alpha+b[53+p]];
      c[106+j]=add[rm[a[106+j]][N]][scale[character[alpha]][b[106+p]]];
      unsigned acted=au[1080*alpha+b[160+p]];
      c[160+j]=um[1080*a[160+j]+zact[dot[a[106+j]][u]][acted]];
    }
    c[159]=mm[M][N];c[213]=add[a[213]][cm[M][u]];
  }
  void hinv(const uint16_t*a,uint16_t*b)const{
    unsigned M=mi[a[159]],t=a[213];if(!M)throw std::runtime_error("singular affine matrix");
    for(int j=0;j<53;++j)b[a[j]]=j;
    for(int j=0;j<53;++j){unsigned q=b[j],beta=ai[a[53+q]];
      b[53+j]=beta;b[106+j]=scale[3-character[beta]][rm[a[106+q]][M]];
      unsigned k=au[1080*beta+ui[a[160+q]]];
      b[160+j]=zact[(3-dot[b[106+j]][t])%3][k];
    }
    b[159]=M;b[213]=scale[2][cm[M][t]];
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
  Ternary vector(const Element&a)const{
    Ternary v;
    for(int q=0;q<6;++q)if(a[q]!=q)throw std::runtime_error("nonkernel coset permutation");
    for(int k=0;k<36;++k){const uint16_t*h=a.data()+6+k*HW;
      if(h[159]!=28||h[213])throw std::runtime_error("nonkernel affine value");
      for(int j=0;j<53;++j){
        if(h[j]!=j||h[53+j]!=autone)throw std::runtime_error("nonkernel A6 automorphism");
        if(h[160+j]>=1080||zlog[h[160+j]]<0)throw std::runtime_error("noncentral cover value");
        TernarySpan::put(v,159*k+j,zlog[h[160+j]]);
        TernarySpan::put(v,159*k+53+2*j,h[106+j]%3);
        TernarySpan::put(v,159*k+54+2*j,h[106+j]/3);
      }
    }return v;
  }
  Element kernel(const Ternary&v)const{
    Element a=one;for(int k=0;k<36;++k){uint16_t*h=a.data()+6+k*HW;
      for(int j=0;j<53;++j){h[160+j]=zp[TernarySpan::coefficient(v,159*k+j)];
        h[106+j]=TernarySpan::coefficient(v,159*k+53+2*j)+3*TernarySpan::coefficient(v,159*k+54+2*j);}
    }return a;
  }
  static Ternary readvector(std::istream&f){Ternary v;
    for(int j=0;j<BW;++j)TernarySpan::put(v,j,integer<uint8_t>(f));return v;}
  explicit Model(const std::string&name){
    tables();std::ifstream f(name,std::ios::binary);
    if(integer<uint32_t>(f)!=0xA63F1C01||integer<uint32_t>(f)!=1||integer<uint32_t>(f)!=EW)throw std::runtime_error("model header");
    uid=integer<uint32_t>(f);z=integer<uint32_t>(f);autone=integer<uint32_t>(f);
    if(uid>=1080||z>=1080||autone>=1440)throw std::runtime_error("identity indices");
    um=table(f,1080*1080);ui=table(f,1080);am=table(f,1440*1440);ai=table(f,1440);au=table(f,1440*1080);
    for(auto v:um)if(v>=1080)throw std::runtime_error("cover table range");
    for(auto v:ui)if(v>=1080)throw std::runtime_error("cover inverse range");
    for(auto v:am)if(v>=1440)throw std::runtime_error("automorphism table range");
    for(auto v:ai)if(v>=1440)throw std::runtime_error("automorphism inverse range");
    for(auto v:au)if(v>=1080)throw std::runtime_error("automorphism action range");
    f.read((char*)character.data(),1440);if(!f)throw std::runtime_error("central character table");
    for(auto v:character)if(v!=1&&v!=2)throw std::runtime_error("central character value");
    zp[0]=uid;zp[1]=z;zp[2]=um[1080*z+z];zlog.fill(-1);
    for(int j=0;j<3;++j){zlog[zp[j]]=j;for(int k=0;k<1080;++k)zact[j][k]=um[1080*zp[j]+k];}
    one=element(f);original={element(f),element(f)};
    if(mul(one,one)!=one||inv(one)!=one)throw std::runtime_error("model identity");
    std::vector<Element>values{one,original[0],original[1]};controls=integer<uint32_t>(f);
    for(unsigned i=0;i<controls;++i){unsigned op=integer<uint32_t>(f),a=integer<uint32_t>(f),b=integer<uint32_t>(f);
      if(a>=values.size()||b>=values.size()||op<2||op>5)throw std::runtime_error("control DAG");
      Element v=op==2?mul(values[a],values[b]):op==3?inv(values[a]):op==4?comm(values[a],values[b]):conj(values[a],values[b]);
      if(v!=element(f))throw std::runtime_error("independent Python group control");values.push_back(v);
    }
    if(integer<uint32_t>(f)!=BW)throw std::runtime_error("kernel width");kernel_controls=integer<uint32_t>(f);
    for(unsigned i=0;i<kernel_controls;++i){Element e=element(f);Ternary v=readvector(f);
      if(!TernarySpan::equal(vector(e),v)||kernel(v)!=e)throw std::runtime_error("independent Python kernel control");}
    unsigned n=integer<uint32_t>(f),m=integer<uint32_t>(f);if(n>65535||m!=2)throw std::runtime_error("base size");
    base_original.resize(2,P(n));for(auto&p:base_original)f.read((char*)p.data(),2*n);
    if(!f||f.peek()!=EOF)throw std::runtime_error("model file length");
    if(mul(original[0],original[0])!=one||mul(mul(original[1],original[1]),original[1])!=one)throw std::runtime_error("B source torsion relations");
  }
};

