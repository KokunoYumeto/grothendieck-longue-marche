// Complete actual joint source above the already certified A6/A5 base.
#define main de_a6_schreier_existing_main
#include "de_a6_schreier.cpp"
#undef main
#include "e_a6_double_core_root.hpp"
#include "de_a6_double_signed_gl_core.hpp"

constexpr int JBW=BW+Signed::BW,JNW=(JBW+63)/64;
using JointBits=std::array<uint64_t,JNW>;
struct JointElement {
  Element binary;Signed::Element signed_part;
  bool operator==(const JointElement&b)const{return binary==b.binary&&signed_part==b.signed_part;}
  bool operator!=(const JointElement&b)const{return !(*this==b);}
};
struct JointSpan {
  std::map<int,JointBits>rows;std::vector<JointBits>basis;std::vector<uint32_t>words;
  static bool zero(const JointBits&v){for(auto a:v)if(a)return false;return true;}
  static unsigned coefficient(const JointBits&v,int p){return(v[p/64]>>(p%64))&1;}
  static void put(JointBits&v,int p,unsigned a){if(p<0||p>=JBW||a>1)throw std::runtime_error("joint bit");if(a)v[p/64]|=uint64_t(1)<<(p%64);}
  JointBits reduce(JointBits v)const{for(auto&[p,r]:rows)if(coefficient(v,p))for(int j=0;j<JNW;++j)v[j]^=r[j];return v;}
  bool contains(const JointBits&v)const{return zero(reduce(v));}
  bool add(const JointBits&v,uint32_t word){auto r=reduce(v);if(zero(r))return false;
    int j=0;while(!r[j])++j;int p=64*j+__builtin_ctzll(r[j]);if(p>=JBW)throw std::runtime_error("joint span width");
    rows.emplace(p,r);basis.push_back(v);words.push_back(word);return true;}
};
struct JointModel {
  Model&d;Signed::Model&s;JointElement one;std::vector<JointElement>original;
  std::vector<P>base_original;JointSpan upper;unsigned controls,kernel_controls;
  JointModel(Model&binary,Signed::Model&signs,const std::string&name):d(binary),s(signs){
    one={d.one,s.one};for(unsigned i=0;i<2;++i)original.push_back({d.original[i],s.original[i]});
    base_original=s.base_original;controls=d.controls+s.controls;kernel_controls=d.kernel_controls+s.kernel_controls;
    std::ifstream f(name,std::ios::binary);
    if(Model::integer<uint32_t>(f)!=0xA62F105B||Model::integer<uint32_t>(f)!=1
       ||Model::integer<uint32_t>(f)!=BW||Model::integer<uint32_t>(f)!=Signed::BW
       ||Model::integer<uint32_t>(f)!=128||Model::integer<uint32_t>(f)!=42)
      throw std::runtime_error("joint upper header");
    for(unsigned i=0;i<170;++i){JointBits v{};int width=i<128?BW:Signed::BW,offset=i<128?0:BW;
      for(int j=0;j<width;++j)JointSpan::put(v,offset+j,Model::integer<uint8_t>(f));
      if(!upper.add(v,i))throw std::runtime_error("joint upper rank");}
    unsigned n=Model::integer<uint32_t>(f);if(n!=d.base_original[0].size())throw std::runtime_error("joint projection size");
    P projection(n);f.read((char*)projection.data(),2*n);
    if(!f||f.peek()!=EOF)throw std::runtime_error("joint upper length");
    for(unsigned j=0;j<2;++j)for(unsigned i=0;i<n;++i){
      if(projection[i]>=base_original[j].size()||projection[d.base_original[j][i]]!=base_original[j][projection[i]])
        throw std::runtime_error("actual joint to A6 projection");}
    if(mul(original[0],original[0])!=one||mul(mul(original[1],original[1]),original[1])!=one)
      throw std::runtime_error("joint B torsion relations");
  }
  JointElement mul(const JointElement&a,const JointElement&b)const{return {d.mul(a.binary,b.binary),s.mul(a.signed_part,b.signed_part)};}
  JointElement inv(const JointElement&a)const{return {d.inv(a.binary),s.inv(a.signed_part)};}
  JointElement comm(const JointElement&a,const JointElement&b)const{return mul(mul(mul(a,b),inv(a)),inv(b));}
  JointElement conj(const JointElement&a,const JointElement&b)const{return mul(mul(a,b),inv(a));}
  JointBits vector(const JointElement&a)const{JointBits v{};auto x=d.vector(a.binary);auto y=s.vector(a.signed_part);
    for(int j=0;j<BW;++j)JointSpan::put(v,j,BinarySpan::coefficient(x,j));
    for(int j=0;j<Signed::BW;++j)JointSpan::put(v,BW+j,(y[j/64]>>(j%64))&1);
    return v;}
  JointElement kernel(const JointBits&v)const{Binary x;Signed::Bits y{};
    for(int j=0;j<BW;++j)BinarySpan::put(x,j,JointSpan::coefficient(v,j));
    for(int j=0;j<Signed::BW;++j)if(JointSpan::coefficient(v,BW+j))y[j/64]|=uint64_t(1)<<(j%64);
    return {d.kernel(x),s.kernel(y)};}
};

#include "de_a6_double_signed_lifted.hpp"

int main(int argc,char**argv){try{
  if(argc!=6)throw std::runtime_error("usage: executable double_model.bin signed_model.bin joint_upper.bin base_certificate.bin output.json");
  auto start=std::chrono::steady_clock::now();Model binary(argv[1]);Signed::Model signs(argv[2]);JointModel model(binary,signs,argv[3]);
  auto engine=Engine::replay(argv[4]);if(engine->original!=model.base_original)throw std::runtime_error("actual joint source originals");
  std::cout<<"complete joint base replay passed"<<std::endl;
  Lifted lifted(model,*engine);bool complete=lifted.solve();
  double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();lifted.save(argv[5],complete,seconds);
  std::cout<<"PASS full actual joint kernel dimension "<<lifted.span.basis.size()<<" seconds "<<seconds<<std::endl;return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
