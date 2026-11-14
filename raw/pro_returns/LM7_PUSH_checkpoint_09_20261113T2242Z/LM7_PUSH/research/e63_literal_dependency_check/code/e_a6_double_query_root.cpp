// Exact normal-form evaluation in the abelianization of the C-preimage.
#include "e_a6_double_query_core_root.hpp"

int main(int argc,char**argv){try{
  if(argc!=6)throw std::runtime_error("usage: executable source_model central_model C_certificate queries output");
  auto started=std::chrono::steady_clock::now();Model m(argv[1]);CentralData c(m,argv[2]);
  auto e=Engine::replay(argv[3]);CentralProbe probe(*e,m,c);
  std::ifstream f(argv[4],std::ios::binary);
  if(Model::integer<uint32_t>(f)!=0xA62C0032||Model::integer<uint32_t>(f)!=1)throw std::runtime_error("query magic");
  unsigned nq=Model::integer<uint32_t>(f),n=Model::integer<uint32_t>(f),dim=Model::integer<uint32_t>(f);
  if(n!=e->n||dim!=3)throw std::runtime_error("query dimensions");
  std::array<unsigned,128>piv;for(auto&a:piv){a=Model::integer<uint32_t>(f);if(a>=BW)throw std::runtime_error("query pivot");}
  uint8_t L[3][128],hom[3][10];f.read((char*)L,sizeof(L));f.read((char*)hom,sizeof(hom));
  std::ofstream out(argv[5]);if(!out)throw std::runtime_error("query output");
  out<<"{\n\"status\":\"PASS_EXACT_C_PREIMAGE_NORMAL_FORM_QUERIES\",\n\"query_count\":"<<nq<<",\n\"records\":[";
  for(unsigned qi=0;qi<nq;++qi){Element v=Model::element(f);P h(n);f.read((char*)h.data(),2*n);
    Exponents ex{};std::vector<unsigned>history;
    for(auto&l:e->chain){int b=h[l.base];if(b==l.base)continue;int at=l.pos[b];
      if(at<0)throw std::runtime_error("query outside C");
      h=e->mul(h,l.inv[at]);v=m.mul(v,probe.inverses[l.word[at]]);
      ex=CentralProbe::plus(ex,probe.exponents[l.word[at]]);history.push_back(l.word[at]);}
    if(!e->identity(h))throw std::runtime_error("query C residue");
    auto kernel=m.vector(v);if(!c.upper.contains(kernel))throw std::runtime_error("query kernel residue");
    std::array<unsigned,3>value{};
    for(unsigned i=0;i<3;++i){unsigned z=0;
      for(unsigned j=0;j<128;++j)z+=L[i][j]*BinarySpan::coefficient(kernel,piv[j]);
      for(unsigned j=0;j<10;++j)z+=hom[i][j]*ex[j];value[i]=z%2;}
    if(qi)out<<",";out<<"{\"coordinate\":["<<value[0]<<","<<value[1]<<","<<value[2]<<"],\"normal_form_nodes\":[";
    for(unsigned j=0;j<history.size();++j){if(j)out<<",";out<<history[j];}
    out<<"],\"C_generator_exponents\":[";for(unsigned j=0;j<10;++j){if(j)out<<",";out<<unsigned(ex[j]);}
    out<<"],\"kernel_residue\":[";bool first=true;
    for(int j=0;j<BW;++j){unsigned a=BinarySpan::coefficient(kernel,j);if(a){if(!first)out<<",";first=false;out<<"["<<j<<","<<a<<"]";}}
    out<<"]}";
  }
  if(!f||f.peek()!=EOF)throw std::runtime_error("query file length");
  out<<"],\n\"normal_form_word_DAG\":[";
  for(unsigned j=0;j<probe.nodes.size();++j){if(j)out<<",";auto q=probe.nodes[j];out<<"["<<q.op<<","<<q.a<<","<<q.b<<"]";}
  double secs=std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();
  out<<"],\n\"seconds\":"<<secs<<"\n}\n";
  std::cout<<"PASS exact C-preimage queries "<<nq<<" seconds "<<secs<<std::endl;return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
