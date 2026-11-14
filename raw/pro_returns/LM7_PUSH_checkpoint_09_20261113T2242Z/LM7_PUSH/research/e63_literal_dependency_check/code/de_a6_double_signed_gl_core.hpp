#pragma once
namespace Signed {
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


}
