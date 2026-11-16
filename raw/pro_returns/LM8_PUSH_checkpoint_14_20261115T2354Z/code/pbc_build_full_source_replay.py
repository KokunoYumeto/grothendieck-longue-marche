#!/usr/bin/env python3
"""Build an exact record-limited replay of the complete suffix3 calculation."""
from pathlib import Path
import hashlib,json,subprocess
b=Path(__file__).resolve().parent
p=b/'pbc_suffix3_native_search.cpp';s=p.read_text()
start=s.index('struct Trace {');end=s.index('struct Witness {')
old=s[start:s.index('volatile sig_atomic_t',start)]
methods=old[old.index(' uint64_t leaf('):old.rindex('};')]
replacement='''struct ReplayDone:std::exception{};
uint64_t ReplayLimit=0,ReplayRecords=0;
struct Trace{
 uint64_t serial=0;
 explicit Trace(const char*){}
 void flush(){std::cout.flush();}
 void line(const std::string&s){
  std::cout.write(s.data(),s.size());if(!std::cout)throw std::runtime_error("replay output failure");
  if(++ReplayRecords==ReplayLimit){std::cout.flush();throw ReplayDone();}
 }
'''+methods+'''};
bool PBCControlPending(){return false;}
void PBCControlHook(){}
'''
s=s[:start]+replacement+s[end:]
s=s.replace('PBCActiveTrace=&trace;','')
s=s[:s.index('int main(int argc,char**argv)')]+'''int main(int argc,char**argv){
 assert(argc==3);ReplayLimit=std::stoull(argv[2]);assert(ReplayLimit>0);
 std::ifstream in(argv[1]);assert(in);std::ios::sync_with_stdio(false);
 try{Witness w(in,"unused","/dev/null");w.run();}
 catch(const ReplayDone&){std::cerr<<"FULL_SOURCE_REPLAY_COMPLETE records "<<ReplayRecords<<std::endl;return 0;}
 assert(ReplayRecords==ReplayLimit);return 0;
}
'''
cpp=b/'pbc_suffix3_full_source_replay.cpp';cpp.write_text(s)
exe=b/'pbc_suffix3_full_source_replay'
cmd=['g++','-std=c++17','-O3',str(cpp),'-lgmpxx','-lgmp','-lz','-o',str(exe)]
subprocess.run(cmd,check=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report={'compiler_command':cmd,'original_source_sha256':sha(p),'replay_source_sha256':sha(cpp),'executable_sha256':sha(exe),
 'changes':'Replace gzip trace by direct standard output with exact record cap; disable pause controls; run the unchanged complete source-row collection and exact reducer.',
 'status':'Built only. Complete byte comparison is mandatory before using this storage representation.'}
(b/'pbc_suffix3_full_source_replay_build.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
