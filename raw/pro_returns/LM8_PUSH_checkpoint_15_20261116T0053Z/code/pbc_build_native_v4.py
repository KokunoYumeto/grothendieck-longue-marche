#!/usr/bin/env python3
"""Build a bounded, checkpointable positive-certificate native search.

Budgeted source rows are omitted entirely; a negative remainder has no
nonlifting interpretation. Every successful proof still expands solely
into completed original source identities and genuine boundary commutators.
"""
from pathlib import Path
import hashlib,json
b=Path(__file__).parent
h=(b/'pbc_positive_collector_core.hpp').read_text()
h=h.replace('struct Collector {','''void PBCControlHook();
bool PBCControlPending();
struct PBCCollectionBudget : std::runtime_error {
 PBCCollectionBudget():std::runtime_error("original row collection budget"){}
};
struct Collector {''')
h=h.replace('unsigned long long steps=0;', 'unsigned long long steps=0,max_steps_per_collection=0;')
h=h.replace('Normal collect(const Word& input) {','Normal collect(const Word& input) {\n  unsigned long long local_steps=0;')
h=h.replace('   ++steps;','''   ++steps;++local_steps;
   if(max_steps_per_collection && local_steps>max_steps_per_collection)throw PBCCollectionBudget();
   if(local_steps%100000==0 && PBCControlPending())PBCControlHook();''')
hp=b/'pbc_positive_collector_control.hpp';hp.write_text(h)
t=(b/'pbc_native_modular_v3.cpp').read_text()
t=t.replace('#include "pbc_positive_collector_core.hpp"','#include "pbc_positive_collector_control.hpp"\n#include <csignal>\n#include <thread>\n#include <unistd.h>')
t=t.replace(' gzFile file;uint64_t serial=0;',' gzFile file;uint64_t serial=0;std::string path;')
t=t.replace(' explicit Trace(const char* path){file=gzopen(path,"wb1");',' explicit Trace(const char* name):path(name){file=gzopen(name,"wb1");')
t=t.replace(' ~Trace(){if(file)gzclose(file);}', ''' ~Trace(){if(file)gzclose(file);}
 void closeForCheckpoint(){if(file){if(gzclose(file)!=Z_OK)throw std::runtime_error("gzip close failed");file=nullptr;}}
 void reopenAfterCheckpoint(){assert(!file);file=gzopen(path.c_str(),"ab1");if(!file)throw std::runtime_error("gzip append failed");gzbuffer(file,1<<20);}''')
needle='struct Witness {'
control='''volatile sig_atomic_t PBCPauseRequested=0,PBCResumeRequested=0,PBCStopRequested=0;
Trace* PBCActiveTrace=nullptr;
struct PBCStopped : std::exception {};
void PBCSignal(int signal){if(signal==SIGUSR1)PBCPauseRequested=1;else if(signal==SIGUSR2)PBCResumeRequested=1;else PBCStopRequested=1;}
bool PBCControlPending(){return PBCPauseRequested||PBCStopRequested;}
void PBCControlHook(){
 if(PBCStopRequested)throw PBCStopped();
 if(!PBCPauseRequested)return;
 PBCPauseRequested=0;PBCResumeRequested=0;assert(PBCActiveTrace);
 PBCActiveTrace->closeForCheckpoint();
 std::cerr<<"native_checkpoint_PAUSED_valid_gzip_footer pid "<<getpid()<<" proof_nodes "<<PBCActiveTrace->serial<<std::endl;
 while(!PBCResumeRequested&&!PBCStopRequested)std::this_thread::sleep_for(std::chrono::milliseconds(100));
 if(PBCStopRequested)throw PBCStopped();
 PBCResumeRequested=0;PBCActiveTrace->reopenAfterCheckpoint();
 std::cerr<<"native_checkpoint_RESUMED_new_gzip_member pid "<<getpid()<<std::endl;
}
'''
assert needle in t;t=t.replace(needle,control+needle)
t=t.replace('  in>>source_hash>>modulus>>s_count>>r_count;', '  PBCActiveTrace=&trace;c.max_steps_per_collection=2000000;\n  std::cerr<<"native_version4_pid "<<getpid()<<" original_collection_step_budget "<<c.max_steps_per_collection<<std::endl;\n  in>>source_hash>>modulus>>s_count>>r_count;')
t=t.replace('  for(int i=first;i<=m;i++){\n   if(acc[i]==0)continue;', '  for(int i=first;i<=m;i++){\n   if(i%64==0&&PBCControlPending())PBCControlHook();\n   if(acc[i]==0)continue;')
old='''  auto start=std::chrono::steady_clock::now();Normal a=c.collect(lhs),b=c.collect(rhs);assert(a.base==b.base);Sparse v;
  for(int i=1;i<=m;i++)if(a.tail[i]!=b.tail[i])v.push_back({i,Z(a.tail[i])-Z(b.tail[i])});
  collection_seconds+=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();relation(v,meta);'''
new='''  auto start=std::chrono::steady_clock::now();
  try {
   Normal a=c.collect(lhs),b=c.collect(rhs);assert(a.base==b.base);Sparse v;
   for(int i=1;i<=m;i++)if(a.tail[i]!=b.tail[i])v.push_back({i,Z(a.tail[i])-Z(b.tail[i])});
   collection_seconds+=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();relation(v,meta);
  } catch(const PBCCollectionBudget&) {
   collection_seconds+=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
   std::cerr<<"native_OMITTED_budgeted_original_row ";writeInts(std::cerr,meta);std::cerr<<" seconds "<<seconds()<<std::endl;
  }'''
assert old in t;t=t.replace(old,new)
oldmain=''' assert(argc==4);std::ifstream in(argv[1]);assert(in.good());Witness w(in,argv[2],argv[3]);w.run();return 0;'''
newmain=''' assert(argc==4);
 std::signal(SIGUSR1,PBCSignal);std::signal(SIGUSR2,PBCSignal);std::signal(SIGINT,PBCSignal);std::signal(SIGTERM,PBCSignal);
 std::ifstream in(argv[1]);assert(in.good());
 try {Witness w(in,argv[2],argv[3]);w.run();}
 catch(const PBCStopped&){std::cerr<<"native_GRACEFUL_STOP_incomplete_search_valid_gzip_footer"<<std::endl;return 130;}
 return 0;'''
assert oldmain in t;t=t.replace(oldmain,newmain)
out=b/'pbc_native_modular_v4.cpp';out.write_text('// Version4: source-row budget and signal-controlled valid-gzip checkpoints.\n'+t)
meta={'purpose':'Positive source-row certificate search only; budgeted rows are omitted and no negative conclusion follows.',
      'signals':{'SIGUSR1':'pause and close gzip footer','SIGUSR2':'resume with next gzip member','SIGINT/SIGTERM':'graceful stop with valid footer'},
      'original_collection_step_budget':2000000,'hashes':{}}
for p in [Path(__file__),b/'pbc_native_modular_v3.cpp',b/'pbc_positive_collector_core.hpp',hp,out]:meta['hashes'][str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
(b/'pbc_native_modular_v4_build.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
