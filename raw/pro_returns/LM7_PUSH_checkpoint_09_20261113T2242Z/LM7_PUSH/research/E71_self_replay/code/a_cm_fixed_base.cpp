// Exact prescribed-prefix variant of the unchanged complete Schreier engine.
// Every final relation and every literal word uses the existing verifier.
#define main lm7_original_schreier_main
#include "de_a6_schreier.cpp"
#undef main

int main(int argc,char**argv){try {
  if(argc!=4)throw std::runtime_error("usage: fixed_base input.txt base.txt certificate.bin");
  std::ifstream in(argv[1]);int n,m;in>>n>>m;
  if(!in)throw std::runtime_error("input header");
  std::vector<P> input(m,P(n));
  for(auto &p:input)for(auto &x:p){unsigned a;in>>a;x=a;}
  if(!in)throw std::runtime_error("input permutations");
  std::ifstream bases(argv[2]);int count;bases>>count;
  if(!bases||count<0||count>n)throw std::runtime_error("base header");
  Engine e(n);std::vector<bool> used(n,false);
  for(int i=0;i<count;++i){int b;bases>>b;
    if(!bases||b<0||b>=n||used[b])throw std::runtime_error("invalid prescribed base");
    used[b]=true;e.new_level(b);
  }
  e.initialize(input);e.discover();e.save(argv[3]);e.report();return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
