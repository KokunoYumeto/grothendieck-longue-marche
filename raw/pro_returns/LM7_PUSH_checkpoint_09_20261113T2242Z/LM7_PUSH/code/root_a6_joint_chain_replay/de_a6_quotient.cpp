// Exact quotient action on the left cosets C*g of a certified normal C.
// Canonical cosets are compared as complete permutations; hashes only
// select a bucket and are never treated as equality certificates.
#define main schreier_engine_main
#include "de_a6_schreier.cpp"
#undef main
#include <unordered_map>

P canonical_coset(const Engine&e,P h) {
  for(const auto &l:e.chain) {
    size_t at=0;
    for(size_t j=1;j<l.orbit.size();++j)
      if(h[l.orbit[j]]<h[l.orbit[at]])at=j;
    h=e.mul(l.trans[at],h);
  }
  return h;
}
uint64_t hash_permutation(const P&p) {
  uint64_t h=1469598103934665603ULL;
  for(auto v:p){h^=v;h*=1099511628211ULL;}
  return h;
}
int main(int argc,char**argv){try {
  if(argc!=5)throw std::runtime_error("usage: quotient subgroup.bin source.input output.json maximum_cosets");
  auto C=Engine::replay(argv[1]);
  std::ifstream in(argv[2]);int n,m;in>>n>>m;
  if(!in||n!=C->n)throw std::runtime_error("source header");
  std::vector<P> originals(m,P(n));
  for(auto &p:originals)for(auto &v:p){unsigned x;in>>x;if(!in||x>=(unsigned)n)throw std::runtime_error("source entry range");v=x;}
  for(auto &p:originals){P sorted=p;std::sort(sorted.begin(),sorted.end());if(sorted!=C->id)throw std::runtime_error("source permutation");}
  unsigned bound=std::stoul(argv[4]);uint64_t normal_checks=0;
  for(auto &a:originals)for(auto &g:C->gens){++normal_checks;if(!C->contains(C->conjugate(a,g.p)))throw std::runtime_error("subgroup is not source-normal");}
  // At each base point, choose the least available image.  Successive
  // choices leave exactly the next point stabilizer on the left.
  // Thus the resulting permutation is the unique lexicographically
  // least member of its left coset, for the saved base order.
  std::vector<P> reps{canonical_coset(*C,C->id)};
  std::unordered_map<uint64_t,std::vector<unsigned>> buckets;
  buckets[hash_permutation(reps[0])]={0};
  std::vector<unsigned> parent{0},letter{0};
  std::vector<std::vector<unsigned>> images(m);
  uint64_t exact_comparisons=0;
  for(size_t at=0;at<reps.size();++at) {
    for(int j=0;j<m;++j) {
      P h=canonical_coset(*C,C->mul(reps[at],originals[j]));
      auto key=hash_permutation(h);auto &bucket=buckets[key];unsigned found=reps.size();
      for(auto k:bucket){++exact_comparisons;if(reps[k]==h){found=k;break;}}
      if(found==reps.size()) {
        if(reps.size()>=bound)throw std::runtime_error("specified coset bound exceeded");
        bucket.push_back(found);reps.push_back(std::move(h));parent.push_back(at);letter.push_back(j);
      }
      images[j].push_back(found);
    }
    if((at+1)%1000==0)std::cout<<"processed "<<at+1<<" cosets, known "<<reps.size()<<std::endl;
  }
  for(auto &p:images){auto sorted=p;std::sort(sorted.begin(),sorted.end());for(unsigned i=0;i<sorted.size();++i)if(sorted[i]!=i)throw std::runtime_error("quotient generator not permutation");}
  for(auto &g:C->gens)if(canonical_coset(*C,g.p)!=reps[0])throw std::runtime_error("canonical subgroup check");
  std::ofstream out(argv[3]);if(!out)throw std::runtime_error("output file");
  auto array=[&](const auto &v){out<<'[';for(size_t i=0;i<v.size();++i){if(i)out<<',';out<<v[i];}out<<']';};
  out<<"{\"status\":\"PASS\",\"subgroup_order\":\""<<C->order()<<"\",\"quotient_order\":"<<reps.size()
     <<",\"source_degree\":"<<n<<",\"complete_normal_conjugation_checks\":"<<normal_checks
     <<",\"exact_full_permutation_coset_comparisons\":"<<exact_comparisons<<",\"generators\":[";
  for(size_t j=0;j<images.size();++j){if(j)out<<',';array(images[j]);}
  out<<"],\"BFS_parent\":";array(parent);out<<",\"BFS_generator\":";array(letter);out<<"}\n";
  std::cout<<"PASS exact normal quotient order "<<reps.size()<<", subgroup order "<<C->order()
           <<", normal checks "<<normal_checks<<", exact comparisons "<<exact_comparisons<<std::endl;
  return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
