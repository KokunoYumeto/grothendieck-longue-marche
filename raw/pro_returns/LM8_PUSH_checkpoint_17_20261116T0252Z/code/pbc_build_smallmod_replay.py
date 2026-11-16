#!/usr/bin/env python3
"""Build exact replay of native-v6 from retained original source leaves.

The reducer is copied without arithmetic changes. Explicit phase-end checks
match native-v6's power, exterior, and triple phases; every250-row checks
remain inside the original relation method. Acceptance requires comparison
of every captured output byte, not a merely matching terminal lattice.
"""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[1];CODE=ROOT/'code'
native=(CODE/'pbc_native_modular_v6.cpp').read_text()
old=(CODE/'pbc_trace_replay_boundary.cpp').read_text()
trace=old[old.index('struct ReplayDone'):old.index('struct Witness {')]
trace+='bool PBCControlPending(){return false;}\nvoid PBCControlHook(){}\n'
src=native[:native.index('struct Trace {')]+trace+native[native.index('struct Witness {'):]
src=src.replace('PBCActiveTrace=&trace;c.max_steps_per_collection=2000000;','c.max_steps_per_collection=2000000;')
replay=r''' void replay(std::istream&rows){
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
'''
src=src.replace(' void run(){',replay+' void run(){',1)
src=src[:src.index('int main(')]+old[old.index('int main('):]
cpp=CODE/'pbc_trace_replay_smallmod.cpp';exe=CODE/'pbc_trace_replay_smallmod'
cpp.write_text(src)
args=['g++','-std=c++17','-O3',str(cpp),'-lgmpxx','-lgmp','-lz','-o',str(exe)]
subprocess.run(args,check=True)
report={'native_source_sha256':hashlib.sha256(native.encode()).hexdigest(),
 'replay_source_sha256':hashlib.sha256(cpp.read_bytes()).hexdigest(),
 'replay_executable_sha256':hashlib.sha256(exe.read_bytes()).hexdigest(),
 'compiler_command':args,'status':'Built only; entire captured-byte verification is mandatory.'}
(CODE/'pbc_smallmod_replay_build.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2),flush=True)
