// Formatting-only replay optimization. Reducer and retained-source checks unchanged.
// Version6: exact bounded-integer cache when modulus is at most2^31.
// Version5: shared-filesystem pause/stop controls for isolated process namespaces.
// Version4: source-row budget and signal-controlled valid-gzip checkpoints.
// Version3: genuine original power relations and source-generator triples first.
// Version2: exact small-coordinate arithmetic; proof operations unchanged.
// Exact original-presentation modular centralization witness.
// Native port of pbc_hermite_modular_boundary_witness.g. Every proof operation
// is retained in the independently checked JSONL DAG. No probabilistic or
// floating-point linear algebra is used. The source collector is separately
// validated against GAP's original presentation collector.
#include "pbc_positive_collector_control.hpp"
#include <csignal>
#include <thread>
#include <unistd.h>
#include <gmpxx.h>
#include <algorithm>
#include <sstream>
#include <charconv>
#include <zlib.h>
using Z=mpz_class;
using Sparse=std::vector<std::pair<int,Z>>;
using Weights=std::vector<int>;
Z mod(Z a,const Z& b) {a%=b;if(a<0)a+=b;return a;}
Z gcdz(Z a,Z b) {if(a<0)a=-a;if(b<0)b=-b;while(b!=0){Z c=a%b;a=b;b=c;}return a;}
std::pair<Z,Z> gcdcoeff(Z a,Z b) {
 Z oldr=a,r=b,oldx=1,x=0;
 while(r!=0){Z q=oldr/r;Z rr=oldr-q*r;oldr=r;r=rr;Z xx=oldx-q*x;oldx=x;x=xx;}
 if(oldr<0){oldr=-oldr;oldx=-oldx;}return {oldr,oldx};
}
void writeSparse(std::ostream& out,const Sparse& v) {
 out<<'[';bool first=true;for(auto& [i,c]:v){if(!first)out<<',';first=false;out<<i<<','<<c;}out<<']';
}
void writeInts(std::ostream& out,const std::vector<int>& v) {
 out<<'[';bool first=true;for(int x:v){if(!first)out<<',';first=false;out<<x;}out<<']';
}
struct ReplayDone : std::exception {};
uint64_t ReplayLimit=0,ReplayRecords=0;
std::ifstream ReplayRaw;
struct Trace {
 uint64_t serial=0;
 explicit Trace(const char* name){ReplayRaw.open(name);if(!ReplayRaw)throw std::runtime_error("raw source lines missing");}
 void flush(){std::cout.flush();}
 void line(const std::string&s){
  std::string output=s;
  if(s.rfind("[\"source\",",0)==0||s.rfind("[\"leaf\",",0)==0){
   std::string original;if(!std::getline(ReplayRaw,original))throw std::runtime_error("raw source line missing");original+='\n';
   std::string compact;for(char c:original)if(c!=' ')compact+=c;
   if(compact!=s)throw std::runtime_error("retained source line does not match exact replay");output=original;
  }
  std::cout.write(output.data(),output.size());if(!std::cout)throw std::runtime_error("replay output error");
  if(++ReplayRecords==ReplayLimit){std::cout.flush();throw ReplayDone();}
 }
 uint64_t leaf(const std::string&kind,const std::vector<int>&meta,const Sparse&v){std::ostringstream o;o<<"[\"leaf\","<<++serial<<",\""<<kind<<"\",";writeInts(o,meta);o<<',';writeSparse(o,v);o<<"]\n";line(o.str());return serial;}
 static void appendUnsigned(std::string& out,uint64_t x){char buf[32];auto r=std::to_chars(buf,buf+sizeof(buf),x);out.append(buf,r.ptr);}
 static void appendInteger(std::string& out,const Z& x){
  if(mpz_fits_slong_p(x.get_mpz_t())){char buf[32];auto r=std::to_chars(buf,buf+sizeof(buf),x.get_si());out.append(buf,r.ptr);}
  else out+=x.get_str();
 }
 void operation(const std::string& output){
  std::cout.write(output.data(),output.size());if(!std::cout)throw std::runtime_error("replay output error");
  if(++ReplayRecords==ReplayLimit){std::cout.flush();throw ReplayDone();}
 }
 uint64_t sub(uint64_t a,const Z&q,uint64_t b){std::string o;o.reserve(112);o="[\"sub\",";appendUnsigned(o,++serial);o+=',';appendUnsigned(o,a);o+=',';appendInteger(o,q);o+=',';appendUnsigned(o,b);o+="]\n";operation(o);return serial;}
 uint64_t neg(uint64_t a){std::string o;o.reserve(64);o="[\"neg\",";appendUnsigned(o,++serial);o+=',';appendUnsigned(o,a);o+="]\n";operation(o);return serial;}
 uint64_t mul(const Z&u,uint64_t a){std::string o;o.reserve(96);o="[\"mul\",";appendUnsigned(o,++serial);o+=',';appendInteger(o,u);o+=',';appendUnsigned(o,a);o+="]\n";operation(o);return serial;}
};
bool PBCControlPending(){return false;}
void PBCControlHook(){}
struct Witness {
 Collector c;int n,m,s_count,r_count,extra_count,abel_start;
 Z modulus;std::vector<Z> coordinate;std::vector<int> small_coordinate;
 Sparse target;std::vector<Sparse> extras,basis;
 bool small_enabled=false;uint64_t small_modulus=0;std::vector<std::vector<std::pair<int,uint32_t>>> smallbasis;
 std::vector<Weights> basisweights;
 std::vector<uint64_t> basisproof;
 Weights targetweights;uint64_t targetproof=0,relations=0,pivots=0;
 Trace trace;std::string source_hash,certificate_path;
 bool found=false;double reduction_seconds=0,collection_seconds=0;
 std::chrono::steady_clock::time_point began=std::chrono::steady_clock::now();
 Sparse readSparse(std::istream& in){int len;in>>len;assert(len>=0 && len%2==0);Sparse v;for(int i=0;i<len;i+=2){int k;Z a;in>>k>>a;assert(k>=1&&k<=m&&a!=0&&(v.empty()||k>v.back().first));v.push_back({k,a});}return v;}
 double seconds(){return std::chrono::duration<double>(std::chrono::steady_clock::now()-began).count();}
 Witness(std::istream& in,const char* trace_path,const char* cert_path):c(in),n(c.n),m(c.m),trace(trace_path),certificate_path(cert_path){
  c.max_steps_per_collection=2000000;
  std::cerr<<"native_version6_pid "<<getpid()<<" original_collection_step_budget "<<c.max_steps_per_collection<<std::endl;
  in>>source_hash>>modulus>>s_count>>r_count;extra_count=s_count+r_count+2;
  small_enabled=(modulus>0&&modulus<=Z(1UL<<31));if(small_enabled)small_modulus=modulus.get_ui();
  coordinate.resize(m+1);for(int i=1;i<=m;i++){in>>coordinate[i];assert(coordinate[i]>0&&modulus%coordinate[i]==0);}
  small_coordinate.assign(m+1,0);for(int i=1;i<=m;i++)if(coordinate[i]<=3)small_coordinate[i]=coordinate[i].get_si();
  target=readSparse(in);for(int i=0;i<extra_count;i++)extras.push_back(readSparse(in));
  assert(in.good());
  std::ostringstream o;o<<"[\"source\",\""<<source_hash<<"\","<<n<<','<<m<<','<<modulus<<",[";
  for(int i=1;i<=m;i++){if(i>1)o<<',';o<<coordinate[i];}o<<"]]\n";trace.line(o.str());
  basis.resize(m+1);basisweights.assign(m+1,Weights(extra_count,0));basisproof.resize(m+1);
  targetweights.assign(extra_count,0);targetproof=trace.leaf("target",{},target);
  for(int i=1;i<=m;i++){
   basis[i]={{i,coordinate[i]}};
   basisproof[i]=trace.leaf(coordinate[i]==modulus?"modulus":"coordinate",{i},basis[i]);
  }
  if(small_enabled){smallbasis.resize(m+1);for(int i=1;i<=m;i++)rebuild_small(i);}
  abel_start=n;
  while(abel_start>1){bool ok=true;for(int j=abel_start;j<=n;j++)if(c.changed[j][abel_start-1])ok=false;if(!ok)break;--abel_start;}
  std::cerr<<"native_source "<<n<<" tails "<<m<<" abelian_suffix "<<abel_start<<" extras "<<extra_count<<" target_support "<<target.size()<<std::endl;
 }
 void subweights(Weights& w,const Z& q,const Weights& b){
  assert(w[0]==0&&w[1]==0&&b[0]==0&&b[1]==0);
  int q2=mod(q,Z(2)).get_si(),q3=mod(q,Z(3)).get_si();
  for(int i=2;i<extra_count;i++){
   int d=i<2+s_count?2:3;int x=w[i]-(d==2?q2:q3)*b[i];x%=d;if(x<0)x+=d;w[i]=x;
  }
 }
 void mulweights(Weights& w,const Z& q){
  int q2=mod(q,Z(2)).get_si(),q3=mod(q,Z(3)).get_si();
  for(int i=2;i<extra_count;i++){int d=i<2+s_count?2:3;int x=w[i]*(d==2?q2:q3);x%=d;if(x<0)x+=d;w[i]=x;}
 }
 void reduce_gmp(Sparse& v,Weights& weights,uint64_t& proof){
  if(v.empty())return;
  std::vector<Z> acc(m+1);for(auto& [i,a]:v)acc[i]=a;
  int first=v[0].first;
  for(int i=first;i<=m;i++){
   if(i%64==0&&PBCControlPending())PBCControlHook();
   if(acc[i]==0)continue;
   auto& row=basis[i];assert(!row.empty()&&row[0].first==i);
   Z rem=mod(acc[i],row[0].second),q=(acc[i]-rem)/row[0].second;
   if(q==0)continue;acc[i]=rem;
   unsigned long q2=mpz_fdiv_ui(q.get_mpz_t(),2),q3=mpz_fdiv_ui(q.get_mpz_t(),3);
   for(size_t j=1;j<row.size();j++){
    auto& [k,a]=row[j];assert(k>i);
    int d=small_coordinate[k];
    if(d==1){acc[k]=0;continue;}
    if(d){
     assert(a>=0&&a<d);
     long remsmall=static_cast<long>(mpz_fdiv_ui(acc[k].get_mpz_t(),d))-static_cast<long>((d==2?q2:q3)*a.get_ui());
     remsmall%=d;if(remsmall<0)remsmall+=d;acc[k]=remsmall;
    }else acc[k]=mod(acc[k]-q*a,coordinate[k]);
   }
   subweights(weights,q,basisweights[i]);proof=trace.sub(proof,q,basisproof[i]);
  }
  v.clear();for(int i=first;i<=m;i++)if(acc[i]!=0)v.push_back({i,std::move(acc[i])});
 }
 void rebuild_small(int i){
  if(!small_enabled)return;auto&out=smallbasis[i];out.clear();out.reserve(basis[i].size());
  for(auto&[k,a]:basis[i]){assert(a>=0&&a<=modulus);out.push_back({k,static_cast<uint32_t>(a.get_ui())});}
 }
 void reduce(Sparse&v,Weights&weights,uint64_t&proof){
  if(!small_enabled){reduce_gmp(v,weights,proof);return;}
  for(auto&[i,a]:v)if(!mpz_fits_slong_p(a.get_mpz_t())){reduce_gmp(v,weights,proof);return;}
  if(v.empty())return;
  std::vector<int64_t>acc(m+1);for(auto&[i,a]:v)acc[i]=a.get_si();int first=v[0].first;
  for(int i=first;i<=m;i++){
   if(i%64==0&&PBCControlPending())PBCControlHook();
   if(acc[i]==0)continue;auto&row=smallbasis[i];assert(!row.empty()&&row[0].first==i);
   int64_t pivot=row[0].second,rem=acc[i]%pivot,q=acc[i]/pivot;
   if(rem<0){rem+=pivot;--q;}
   if(q==0)continue;acc[i]=rem;
   int64_t qn=q%static_cast<int64_t>(small_modulus);if(qn<0)qn+=small_modulus;
   int q2=q%2,q3=q%3;if(q2<0)q2+=2;if(q3<0)q3+=3;
   for(size_t j=1;j<row.size();j++){
    auto[k,a]=row[j];assert(k>i);int d=small_coordinate[k];
    if(d==1){acc[k]=0;continue;}
    if(d){int64_t x=acc[k]%d-(d==2?q2:q3)*int64_t(a);x%=d;if(x<0)x+=d;acc[k]=x;}
    else {
     assert(coordinate[k]==modulus);
     int64_t previous=acc[k];if(previous<0||previous>=static_cast<int64_t>(small_modulus)){previous%=static_cast<int64_t>(small_modulus);if(previous<0)previous+=small_modulus;}
     uint64_t product=uint64_t(qn)*a%small_modulus;
     acc[k]=uint64_t(previous)>=product?uint64_t(previous)-product:uint64_t(previous)+small_modulus-product;
    }
   }
   Z quotient(static_cast<long>(q));subweights(weights,quotient,basisweights[i]);proof=trace.sub(proof,quotient,basisproof[i]);
  }
  v.clear();for(int i=first;i<=m;i++)if(acc[i]!=0)v.push_back({i,Z(static_cast<long>(acc[i]))});
 }
 void insert(Sparse v,Weights weights,uint64_t proof){
  while(!v.empty()){
   reduce(v,weights,proof);if(v.empty())return;
   if(v[0].second<0){for(auto& kv:v)kv.second=-kv.second;mulweights(weights,Z(-1));proof=trace.neg(proof);}
   auto [g,x]=gcdcoeff(v[0].second,coordinate[v[0].first]);Z step=coordinate[v[0].first]/g,u=mod(x,modulus);
   int tries=0;while(gcdz(u,modulus)!=1){u=mod(u+step,modulus);assert(++tries<=6);}
   assert(mod(u*v[0].second,coordinate[v[0].first])==g);
   if(u!=1){
    Sparse vv;for(auto& [i,a]:v){Z z=mod(u*a,coordinate[i]);if(z!=0)vv.push_back({i,std::move(z)});}v=std::move(vv);
    mulweights(weights,u);proof=trace.mul(u,proof);
   }
   assert(!v.empty());int i=v[0].first;assert(v[0].second<basis[i][0].second);
   if(basis[i][0].second==modulus)++pivots;
   std::swap(v,basis[i]);std::swap(weights,basisweights[i]);std::swap(proof,basisproof[i]);rebuild_small(i);
  }
 }
 bool check(){
  reduce(target,targetweights,targetproof);if(!target.empty())return false;
  assert(targetweights[0]==0&&targetweights[1]==0);found=true;
  std::ostringstream o;o<<"[\"success\","<<targetproof<<',';writeInts(o,targetweights);o<<"]\n";trace.line(o.str());trace.flush();
  std::ofstream out(certificate_path);assert(out.good());
  out<<"{\"success\":true,\"source_sha256\":\""<<source_hash<<"\",\"coefficients\":";writeInts(out,targetweights);
  out<<",\"relations\":"<<relations<<",\"pivots\":"<<pivots<<",\"proof_node\":"<<targetproof<<",\"s_count\":"<<s_count<<",\"r_count\":"<<r_count<<"}\n";
  std::cerr<<"native_witness_found relations "<<relations<<" proof_nodes "<<trace.serial<<" seconds "<<seconds()<<" coefficients ";writeInts(std::cerr,targetweights);std::cerr<<std::endl;return true;
 }
 void relation(const Sparse& v,const std::vector<int>& meta){
  if(v.empty()||found)return;++relations;
  auto start=std::chrono::steady_clock::now();insert(v,Weights(extra_count,0),trace.leaf("identity",meta,v));
  reduction_seconds+=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  if(relations%250==0){check();trace.flush();std::cerr<<"native_relations "<<relations<<" pivots "<<pivots<<" target_support "<<target.size()<<" seconds "<<seconds()<<" reduction "<<reduction_seconds<<" collection "<<collection_seconds<<" nodes "<<trace.serial<<std::endl;}
 }
 Word formalConjugate(int i,int j){Word w=c.conjugates[i][j];if(!c.changed[i][j])w.push_back({n+c.conjugatetail[i][j],1});return w;}
 static Word cat(Word a,const Word& b){a.insert(a.end(),b.begin(),b.end());return a;}
 void collectedRelation(const Word& lhs,const Word& rhs,const std::vector<int>& meta){
  auto start=std::chrono::steady_clock::now();
  try {
   Normal a=c.collect(lhs),b=c.collect(rhs);assert(a.base==b.base);Sparse v;
   for(int i=1;i<=m;i++)if(a.tail[i]!=b.tail[i])v.push_back({i,Z(a.tail[i])-Z(b.tail[i])});
   collection_seconds+=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();relation(v,meta);
  } catch(const PBCCollectionBudget&) {
   collection_seconds+=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
   std::cerr<<"native_OMITTED_budgeted_original_row ";writeInts(std::cerr,meta);std::cerr<<" seconds "<<seconds()<<std::endl;
  }
 }
 void exterior(int i,int j,int k){
  std::vector<Z> acc(m+1);acc[c.conjugatetail[k][j]]+=1;
  const Word& a=c.conjugates[k][i];const Word& b=c.conjugates[j][i];
  for(auto [l,e]:a)if(l<=n)for(auto [h,f]:b)if(h<=n){
   assert(l>=abel_start&&h>=abel_start);
   if(l>h)acc[c.conjugatetail[l][h]]-=Z(static_cast<long>(e))*static_cast<long>(f);
   else if(l<h)acc[c.conjugatetail[h][l]]+=Z(static_cast<long>(e))*static_cast<long>(f);
  }
  Sparse v;for(int t=1;t<=m;t++)if(acc[t]!=0)v.push_back({t,std::move(acc[t])});relation(v,{2,i,j,k});
 }
 void replay(std::istream&rows){
  for(int i=2;i<extra_count;i++){Weights w(extra_count,0);w[i]=1;insert(extras[i],w,trace.leaf("extra",{i+1},extras[i]));}
  if(check())return;
  int phase=0;
  for(;;){
   int len;if(!(rows>>len))break;assert(len>0);std::vector<int>meta(len);for(auto&v:meta)rows>>v;
   int next=meta[0]==1?2:(meta[0]==2?1:0);assert(next>=phase);
   while(phase<next){if(check())return;++phase;}
   Sparse v=readSparse(rows);relation(v,meta);if(found)return;
  }
  // This also reproduces a capture within a phase-end reduction: the
  // exact record limit interrupts before any later phase can be read.
  if(check())return;
  std::ostringstream o;o<<"[\"failure\","<<targetproof<<',';writeSparse(o,target);o<<"]\n";trace.line(o.str());trace.flush();
  throw std::runtime_error("source leaves ended before the exact terminal record");
 }
 void run(){
  for(int i=2;i<extra_count;i++){Weights w(extra_count,0);w[i]=1;insert(extras[i],w,trace.leaf("extra",{i+1},extras[i]));}
  if(check())return;
  // Search order version3: genuine power-consistency rows first, then
  // boundary-generator exterior rows, then original triples with source
  // generators1,2. Skipped one-coordinate rows are already the proved
  // coordinate bounds. This changes only search order, not the proof gate.
  for(int i=n;i>=1;i--){
   if(c.powers[i].size()>1)collectedRelation(cat(c.powers[i],Word{{i,1}}),cat(Word{{i,1}},c.powers[i]),{5,i});
   if(found)return;
  }
  for(int i=n;i>=1;i--)for(int j=n;j>i;j--){
   if(!c.changed[j][i]&&c.powers[j].size()==1)continue;
   Word lhs=cat(Word{{j,c.order[j]-1},{i,1}},formalConjugate(j,i));
   Word rhs=cat(c.powers[j],Word{{i,1}});collectedRelation(lhs,rhs,{3,i,j});if(found)return;
  }
  for(int i=n;i>=1;i--)for(int k=n;k>i;k--){
   if(!c.changed[k][i]&&c.powers[i].size()==1)continue;
   Word lhs=cat(Word{{k,1}},c.powers[i]);
   Word rhs=cat(cat(Word{{i,1}},formalConjugate(k,i)),Word{{i,c.order[i]-1}});
   collectedRelation(lhs,rhs,{4,i,k});if(found)return;
  }
  if(check())return;
  std::cerr<<"native_v3_power_prefix_complete "<<relations<<" support "<<target.size()<<" seconds "<<seconds()<<std::endl;
  for(int i=1;i<=2;i++)for(int j=n;j>=abel_start;j--)for(int k=n;k>j;k--){exterior(i,j,k);if(found)return;}
  if(check())return;
  std::cerr<<"native_v3_boundary_exterior_complete "<<relations<<" support "<<target.size()<<" seconds "<<seconds()<<std::endl;
  std::vector<int> triple_order{1,2};for(int i=n;i>=3;i--)triple_order.push_back(i);
  for(int i:triple_order){for(int j=n;j>i;j--)for(int k=n;k>j;k--){
   if((!c.changed[j][i]&&!c.changed[k][i]&&!c.changed[k][j])||j>=abel_start)continue;
   Word lhs=cat(Word{{k,1},{i,1}},formalConjugate(j,i));
   Word rhs=cat(cat(Word{{j,1}},formalConjugate(k,j)),Word{{i,1}});
   collectedRelation(lhs,rhs,{1,i,j,k});if(found)return;
  }if(i%5==0||i<=2)std::cerr<<"native_v3_triples_remaining "<<i<<" support "<<target.size()<<" seconds "<<seconds()<<std::endl;}
  if(check())return;
  std::ostringstream o;o<<"[\"failure\","<<targetproof<<',';writeSparse(o,target);o<<"]\n";trace.line(o.str());trace.flush();
  std::cerr<<"native_positive_search_nonzero_remainder_NOT_a_nonlifting_claim support "<<target.size()<<" seconds "<<seconds()<<std::endl;
 }
};
int main(int argc,char**argv){try{
 std::ios::sync_with_stdio(false);std::cin.tie(nullptr);assert(argc==5);
 ReplayLimit=std::stoull(argv[4]);std::ifstream in(argv[1]),rows(argv[3]);assert(in&&rows);
 Witness w(in,argv[2],"unused_replay_certificate.json");w.replay(rows);
 }catch(const ReplayDone&){std::cerr<<"EXACT_REPLAY_TERMINAL_RECORD "<<ReplayRecords<<'\n';return 0;}
 catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 1;}return 1;}
