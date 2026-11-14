// Exact factorization test of the specified small signed quotient through X2.
#define main de_a6_schreier_existing_main
#include "de_a6_schreier.cpp"
#undef main
#include "e_a6_double_core_root.hpp"

constexpr int CBW=BW+6,CNW=(CBW+63)/64;
struct CandidateBits{std::array<uint64_t,CNW>bits{};};
struct CandidateElement{
  Element binary;std::array<uint8_t,6>signed_values;
  bool operator==(const CandidateElement&b)const{return binary==b.binary&&signed_values==b.signed_values;}
  bool operator!=(const CandidateElement&b)const{return !(*this==b);}
};
struct CandidateSpan{
  std::map<int,CandidateBits>rows;std::vector<CandidateBits>basis;std::vector<uint32_t>words;
  static unsigned coefficient(const CandidateBits&v,int p){return(v.bits[p/64]>>(p%64))&1;}
  static void put(CandidateBits&v,int p,unsigned a){if(p<0||p>=CBW||a>1)throw std::runtime_error("candidate bit");if(a)v.bits[p/64]|=uint64_t(1)<<(p%64);}
  static bool zero(const CandidateBits&v){for(auto a:v.bits)if(a)return false;return true;}
  CandidateBits reduce(CandidateBits v)const{for(auto&[p,r]:rows)if(coefficient(v,p))for(int j=0;j<CNW;++j)v.bits[j]^=r.bits[j];return v;}
  bool contains(const CandidateBits&v)const{return zero(reduce(v));}
  bool add(const CandidateBits&v,uint32_t word){auto r=reduce(v);if(zero(r))return false;int j=0;while(!r.bits[j])++j;
    int p=64*j+__builtin_ctzll(r.bits[j]);if(p>=CBW)throw std::runtime_error("candidate width");
    rows.emplace(p,r);basis.push_back(v);words.push_back(word);return true;}
};
struct CandidateModel{
  Model&d;uint8_t sm[120][120],si[120];unsigned sid,z,controls,kernel_controls;
  CandidateElement one;std::vector<CandidateElement>original;std::vector<P>base_original;BinarySpan upper;
  CandidateModel(Model&model,const std::string&name):d(model){
    std::ifstream f(name,std::ios::binary);
    if(Model::integer<uint32_t>(f)!=0xA62CA005||Model::integer<uint32_t>(f)!=1)throw std::runtime_error("candidate header");
    sid=Model::integer<uint32_t>(f);z=Model::integer<uint32_t>(f);
    if(sid>=120||z>=120||Model::integer<uint32_t>(f)!=128)throw std::runtime_error("candidate dimensions");
    f.read((char*)sm,sizeof(sm));f.read((char*)si,sizeof(si));
    std::array<std::array<uint8_t,6>,2>values,perms;f.read((char*)values.data(),sizeof(values));f.read((char*)perms.data(),sizeof(perms));
    for(unsigned i=0;i<128;++i)if(!upper.add(Model::readvector(f),i))throw std::runtime_error("candidate known kernel rank");
    if(!f||f.peek()!=EOF)throw std::runtime_error("candidate model length");
    one.binary=d.one;one.signed_values.fill(sid);base_original=d.base_original;
    controls=d.controls;kernel_controls=d.kernel_controls;
    for(unsigned j=0;j<2;++j){for(unsigned q=0;q<6;++q)if(d.original[j][q]!=perms[j][q])throw std::runtime_error("literal six coset action");
      original.push_back({d.original[j],values[j]});}
    if(mul(original[0],original[0])!=one||mul(mul(original[1],original[1]),original[1])!=one)
      throw std::runtime_error("candidate actual B relations");
  }
  CandidateElement mul(const CandidateElement&a,const CandidateElement&b)const{
    CandidateElement v;v.binary=d.mul(a.binary,b.binary);
    for(unsigned q=0;q<6;++q)v.signed_values[q]=sm[a.signed_values[q]][b.signed_values[a.binary[q]]];return v;}
  CandidateElement inv(const CandidateElement&a)const{
    CandidateElement v;v.binary=d.inv(a.binary);
    for(unsigned q=0;q<6;++q)v.signed_values[q]=si[a.signed_values[v.binary[q]]];return v;}
  CandidateElement conj(const CandidateElement&a,const CandidateElement&b)const{return mul(mul(a,b),inv(a));}
  CandidateBits vector(const CandidateElement&a)const{
    CandidateBits v;auto k=d.vector(a.binary);if(!upper.contains(k))throw std::runtime_error("candidate exceeds proved source kernel");
    for(int j=0;j<BW;++j)CandidateSpan::put(v,j,BinarySpan::coefficient(k,j));
    for(unsigned q=0;q<6;++q){unsigned value=a.signed_values[q];
      if(value!=sid&&value!=z)throw std::runtime_error("candidate base relator not central");
      CandidateSpan::put(v,BW+q,value==z);}
    return v;}
  CandidateElement kernel(const CandidateBits&v)const{
    Binary k;for(int j=0;j<BW;++j)BinarySpan::put(k,j,CandidateSpan::coefficient(v,j));
    CandidateElement a;a.binary=d.kernel(k);
    for(unsigned q=0;q<6;++q)a.signed_values[q]=CandidateSpan::coefficient(v,BW+q)?z:sid;return a;}
};

#include "de_a6_double_candidate_lifted.hpp"

int main(int argc,char**argv){try{
  if(argc!=5)throw std::runtime_error("usage: executable binary_model.bin candidate_model.bin base_certificate.bin output.json");
  auto start=std::chrono::steady_clock::now();Model d(argv[1]);CandidateModel model(d,argv[2]);
  auto e=Engine::replay(argv[3]);if(e->original!=model.base_original)throw std::runtime_error("candidate actual base generators");
  std::cout<<"complete actual base replay passed"<<std::endl;
  CandidateLift lift(model,*e);lift.solve();
  double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();lift.save(argv[4],seconds);
  std::cout<<"PASS complete candidate kernel rank "<<lift.span.basis.size()<<" relations "<<lift.relations<<" seconds "<<seconds<<std::endl;return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
