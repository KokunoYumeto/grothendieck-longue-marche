// Independent comparison of the experimental collector with retained original
// integer relation rows. It does not read any Hermite or modular quotient basis.
#include "pbc_positive_collector_bits.hpp"
#include <gmpxx.h>
bool PBCControlPending(){return false;}
void PBCControlHook(){}
using Z=mpz_class;
Word cat(Word a,const Word&b){a.insert(a.end(),b.begin(),b.end());return a;}
int main(int argc,char**argv){
 assert(argc==3);std::ifstream in(argv[1]),rows(argv[2]);assert(in&&rows);BitCollector c(in);
 uint64_t count=0;auto start=std::chrono::steady_clock::now();
 for(;;){
  int len;if(!(rows>>len))break;std::vector<int>meta(len);for(int&i:meta)rows>>i;
  int sz;rows>>sz;assert(sz%2==0);std::vector<Z>expected(c.m+1);for(int p=0;p<sz;p+=2){int k;Z x;rows>>k>>x;expected[k]=x;}
  int type=meta[0],i=meta[1],j=len>2?meta[2]:0,k=len>3?meta[3]:0;
  Word lhs,rhs;auto formal=[&](int a,int b){Word w=c.conjugates[a][b];if(!c.changed[a][b])w.push_back({c.n+c.conjugatetail[a][b],1});return w;};
  if(type==5){lhs=cat(c.powers[i],Word{{i,1}});rhs=cat(Word{{i,1}},c.powers[i]);}
  else if(type==3){lhs=cat(Word{{j,c.order[j]-1},{i,1}},formal(j,i));rhs=cat(c.powers[j],Word{{i,1}});}
  else if(type==4){lhs=cat(Word{{j,1}},c.powers[i]);rhs=cat(cat(Word{{i,1}},formal(j,i)),Word{{i,c.order[i]-1}});}
  else if(type==1){lhs=cat(Word{{k,1},{i,1}},formal(j,i));rhs=cat(cat(Word{{j,1}},formal(k,j)),Word{{i,1}});}
  else {assert(type==2);continue;}
  Normal a=c.collect(lhs),b=c.collect(rhs);assert(a.base==b.base);
  for(int t=1;t<=c.m;t++)if(Z(a.tail[t])-Z(b.tail[t])!=expected[t]){
   std::cerr<<"MISMATCH row "<<count<<" meta";for(int x:meta)std::cerr<<' '<<x;
   std::cerr<<" coordinate "<<t<<" expected "<<expected[t]<<" actual "<<Z(a.tail[t])-Z(b.tail[t])<<std::endl;return 2;
  }
  ++count;
  if(count%250==0)std::cout<<"verified_original_rows "<<count<<" atoms "<<c.steps<<" seconds "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<std::endl;
 }
 std::cout<<"PASS all retained original collected rows "<<count<<" atoms "<<c.steps<<" seconds "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<std::endl;
}
