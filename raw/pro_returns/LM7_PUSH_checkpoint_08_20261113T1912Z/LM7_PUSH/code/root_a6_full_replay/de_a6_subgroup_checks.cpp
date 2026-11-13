// Exact containment and normality checks against a fully replayed
// Schreier certificate.  Every comparison is a complete permutation sift.
#define main schreier_engine_main
#include "de_a6_schreier.cpp"
#undef main

int main(int argc,char**argv){try {
  if(argc!=5)throw std::runtime_error("usage: subgroup_checks subgroup.bin source.input output.json mode(normal|contains)");
  auto C=Engine::replay(argv[1]);
  std::ifstream in(argv[2]);int n,m;in>>n>>m;
  if(!in||n!=C->n||m<1)throw std::runtime_error("source header");
  std::vector<P> source(m,P(n));
  for(auto &p:source) {
    for(auto &v:p){unsigned x;in>>x;if(!in||x>=(unsigned)n)throw std::runtime_error("source entry range");v=x;}
    P sorted=p;std::sort(sorted.begin(),sorted.end());
    if(sorted!=C->id)throw std::runtime_error("source permutation");
  }
  std::string mode=argv[4];uint64_t checks=0;
  if(mode=="normal") {
    for(auto &a:source)for(auto &g:C->gens) {
      ++checks;if(!C->contains(C->conjugate(a,g.p)))throw std::runtime_error("normality failed");
    }
  } else if(mode=="contains") {
    for(auto &a:source){++checks;if(!C->contains(a))throw std::runtime_error("containment failed");}
  } else throw std::runtime_error("mode");
  std::ofstream out(argv[3]);if(!out)throw std::runtime_error("output file");
  out<<"{\"status\":\"PASS\",\"mode\":\""<<mode<<"\",\"subgroup_order\":\""<<C->order()
     <<"\",\"degree\":"<<n<<",\"source_generators\":"<<m<<",\"complete_checks\":"<<checks<<"}\n";
  std::cout<<"PASS "<<mode<<", checks "<<checks<<", subgroup order "<<C->order()<<std::endl;
  return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
