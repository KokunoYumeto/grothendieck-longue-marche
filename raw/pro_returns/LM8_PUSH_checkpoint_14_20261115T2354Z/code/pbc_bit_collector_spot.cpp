#include "pbc_positive_collector_bits.hpp"
#include <gmpxx.h>
bool PBCControlPending(){return false;}
void PBCControlHook(){}
using Z=mpz_class;
Word cat(Word a,const Word&b){a.insert(a.end(),b.begin(),b.end());return a;}
int main(int argc,char**argv){
 assert(argc==6);std::ifstream input(argv[1]),reference_input(argv[1]);BitCollector c(input);Collector reference(reference_input);
 int type=std::stoi(argv[2]),i=std::stoi(argv[3]),j=std::stoi(argv[4]),k=std::stoi(argv[5]);
 Word lhs,rhs;auto formal=[&](int a,int b){Word w=c.conjugates[a][b];if(!c.changed[a][b])w.push_back({c.n+c.conjugatetail[a][b],1});return w;};
 if(type==1){lhs=cat(Word{{k,1},{i,1}},formal(j,i));rhs=cat(cat(Word{{j,1}},formal(k,j)),Word{{i,1}});}
 else if(type==3){lhs=cat(Word{{j,c.order[j]-1},{i,1}},formal(j,i));rhs=cat(c.powers[j],Word{{i,1}});}
 else if(type==4){lhs=cat(Word{{j,1}},c.powers[i]);rhs=cat(cat(Word{{i,1}},formal(j,i)),Word{{i,c.order[i]-1}});}
 else return 2;
 auto start=std::chrono::steady_clock::now();Normal a=c.collect(lhs),b=c.collect(rhs);assert(a.base==b.base);
 double optimized_seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
 std::cerr<<"bit_collector_finished steps "<<c.steps<<" seconds "<<optimized_seconds<<std::endl;
 reference.max_steps_per_collection=100000000;
 start=std::chrono::steady_clock::now();Normal x=reference.collect(lhs),y=reference.collect(rhs);
 assert(a.base==x.base&&b.base==y.base&&a.tail==x.tail&&b.tail==y.tail&&c.steps==reference.steps);
 std::cerr<<"PASS original individual word equality and exact same step count "<<reference.steps<<" reference_seconds "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<std::endl;
 std::cout<<"["<<type<<','<<i<<','<<j<<','<<k<<"] [";bool first=true;
 for(int t=1;t<=c.m;t++)if(a.tail[t]!=b.tail[t]){if(!first)std::cout<<',';first=false;std::cout<<t<<','<<Z(a.tail[t])-Z(b.tail[t]);}
 std::cout<<"]\n";
}
