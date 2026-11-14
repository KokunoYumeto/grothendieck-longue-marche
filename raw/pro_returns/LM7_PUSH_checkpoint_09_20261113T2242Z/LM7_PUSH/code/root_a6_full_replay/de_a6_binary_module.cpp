// Actual last elementary-2 layer of the full A6 solvable source quotient.
// All probes are literal permutations, compared modulo the replayed C.
#define main schreier_engine_main
#include "de_a6_schreier.cpp"
#undef main
#include <unordered_map>

P canon(const Engine&e,P h){for(const auto &l:e.chain){size_t at=0;
  for(size_t j=1;j<l.orbit.size();++j)if(h[l.orbit[j]]<h[l.orbit[at]])at=j;
  h=e.mul(l.trans[at],h);}return h;}
uint64_t hashp(const P&p){uint64_t h=1469598103934665603ULL;for(auto v:p){h^=v;h*=1099511628211ULL;}return h;}
std::vector<P> read_perms(const char*path,const Engine&e,unsigned wanted){
  std::ifstream in(path);unsigned n,m;in>>n>>m;
  if(!in||n!=(unsigned)e.n||m!=wanted)throw std::runtime_error("input header");
  std::vector<P> out(m,P(n));for(auto &p:out){for(auto &v:p){unsigned x;in>>x;
    if(!in||x>=n)throw std::runtime_error("input entry");v=x;}
    P sorted=p;std::sort(sorted.begin(),sorted.end());if(sorted!=e.id)throw std::runtime_error("input permutation");}
  return out;
}
std::string times64(std::string s){unsigned carry=0;for(int i=(int)s.size()-1;i>=0;--i){
  unsigned z=(s[i]-'0')*64+carry;s[i]='0'+z%10;carry=z/10;}
  while(carry){s.insert(s.begin(),'0'+carry%10);carry/=10;}return s;}

int main(int argc,char**argv){try{
  if(argc!=8)throw std::runtime_error("usage: binary_module C.bin E1.bin Wbasis.input G.input Ebasis.input V.input output.json");
  auto C=Engine::replay(argv[1]);auto E1=Engine::replay(argv[2]);
  if(E1->n!=C->n||E1->order()!=times64(C->order()))throw std::runtime_error("actual index64");
  for(auto &g:C->gens)if(!E1->contains(g.p))throw std::runtime_error("C not in E1");
  auto w=read_perms(argv[3],*C,6),source=read_perms(argv[4],*C,2),eb=read_perms(argv[5],*C,9);
  if(eb!=E1->original)throw std::runtime_error("original E basis comparison");
  for(auto &g:source)for(auto &h:C->gens)if(!C->contains(C->conjugate(g,h.p)))throw std::runtime_error("C not source-normal");
  for(auto &a:w){if(!E1->contains(a)||!C->contains(C->mul(a,a)))throw std::runtime_error("basis square/membership");
    for(auto &b:w)if(!C->contains(C->commutator(a,b)))throw std::runtime_error("basis commutator");}
  std::vector<P> reps(64,C->id),canonical(64);
  std::unordered_map<uint64_t,std::vector<unsigned>> buckets;
  for(unsigned k=0;k<64;++k){for(unsigned j=0;j<6;++j)if(k&(1u<<j))reps[k]=C->mul(reps[k],w[j]);
    canonical[k]=canon(*C,reps[k]);auto &bucket=buckets[hashp(canonical[k])];
    for(auto q:bucket)if(canonical[q]==canonical[k])throw std::runtime_error("dependent binary basis");bucket.push_back(k);}
  auto coordinates=[&](P p)->unsigned{P c=canon(*C,p);auto it=buckets.find(hashp(c));
    if(it!=buckets.end())for(auto k:it->second)if(c==canonical[k])return k;
    throw std::runtime_error("probe outside E1/C");};
  // Split E/C over its odd elementary-abelian quotient.  Every trial
  // is one of the complete64 literal lifts of the specified basis value.
  std::vector<P> ec;std::vector<unsigned> corrections;
  for(auto &a:eb){bool found=false;for(unsigned k=0;k<64&&!found;++k){P g=C->mul(a,reps[k]);
      if(!C->contains(C->mul(C->mul(g,g),g)))continue;
      bool good=true;for(auto &b:ec)if(!C->contains(C->commutator(g,b))){good=false;break;}
      if(good){ec.push_back(std::move(g));corrections.push_back(k);found=true;}}
    if(!found)throw std::runtime_error("no complete complement lift");}
  std::ifstream vin(argv[6]);int VM[4][9][9],cv[9];
  for(auto &M:VM)for(auto &row:M)for(auto &z:row){vin>>z;if(!vin||z<0||z>=3)throw std::runtime_error("V matrix");}
  for(auto &z:cv){vin>>z;if(!vin||z<0||z>=3)throw std::runtime_error("commutator V value");}
  P s=source[0],r=source[1],ri=C->inverse(r);
  P x=C->mul(C->mul(C->mul(ri,s),ri),s),y=C->mul(C->mul(C->mul(s,ri),s),ri);
  std::vector<P> conjugators{s,r,x,y};conjugators.insert(conjugators.end(),ec.begin(),ec.end());
  std::vector<std::vector<unsigned>> actions;
  for(auto &g:conjugators){std::vector<unsigned> columns;for(auto &a:w)columns.push_back(coordinates(C->conjugate(g,a)));actions.push_back(columns);}
  auto section=[&](const std::vector<int>&v){P a=C->id;for(unsigned j=0;j<9;++j)for(int k=0;k<v[j];++k)a=C->mul(a,ec[j]);return a;};
  std::vector<std::vector<unsigned>> twists;
  for(unsigned k=0;k<4;++k){std::vector<unsigned> row;
    for(unsigned j=0;j<9;++j){std::vector<int> v(9);for(unsigned i=0;i<9;++i)v[i]=VM[k][i][j];
      P residual=C->mul(C->inverse(section(v)),C->conjugate(conjugators[k],ec[j]));row.push_back(coordinates(residual));}
    twists.push_back(row);}
  std::vector<int> commv(cv,cv+9);
  unsigned commw=coordinates(C->mul(C->inverse(section(commv)),C->commutator(x,y)));
  for(auto &a:ec){if(!C->contains(C->mul(C->mul(a,a),a)))throw std::runtime_error("complement order");
    for(auto &b:ec)if(!C->contains(C->commutator(a,b)))throw std::runtime_error("complement commutation");}
  std::ofstream out(argv[7]);if(!out)throw std::runtime_error("output file");
  auto arr=[&](const auto &v){out<<'[';for(unsigned i=0;i<v.size();++i){if(i)out<<',';out<<v[i];}out<<']';};
  auto mat=[&](const auto &M){out<<'[';for(unsigned i=0;i<M.size();++i){if(i)out<<',';arr(M[i]);}out<<']';};
  out<<"{\"status\":\"PASS\",\"dimension\":6,\"field\":2,\"actual_index\":64,\"all64_exact_cosets_distinct\":true,\"source_normality_checked\":true,\"C_in_E1_checked\":true,\"complement_basis_corrections\":";
  arr(corrections);out<<",\"binary_conjugation_columns\":";mat(actions);
  out<<",\"conjugator_labels\":[\"s\",\"r\",\"x\",\"y\",\"e0\",\"e1\",\"e2\",\"e3\",\"e4\",\"e5\",\"e6\",\"e7\",\"e8\"]";
  out<<",\"complement_conjugation_binary_twists\":";mat(twists);
  out<<",\"commutator_x_y_complement_V\":";arr(commv);
  out<<",\"commutator_x_y_binary_coordinate\":"<<commw<<",\"complete_complement_cube_checks\":9,\"complete_complement_commutator_checks\":81}\n";
  std::cout<<"PASS actual F2^6 layer, literal odd complement, all thirteen conjugation actions, and four full complement actions."<<std::endl;
  return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
