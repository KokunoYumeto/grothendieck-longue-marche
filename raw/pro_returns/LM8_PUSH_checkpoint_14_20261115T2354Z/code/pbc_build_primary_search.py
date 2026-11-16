#!/usr/bin/env python3
"""Prepare separate exact primary searches from the retained original rows.

No original row is reduced or replaced. Only the coefficient modulus and
its Bezout-justified coordinate bounds change. Each primary certificate is
partial; the combined integral gate is notes/pbc_C31_primary_split_gate.md.
"""
from pathlib import Path
import hashlib,json,math,subprocess,collections
ROOT=Path(__file__).resolve().parents[1];CODE=ROOT/'code'
source=CODE/'pbc_iterated_shortcut_v2_original_source.json';raw=json.loads(source.read_text())
bound=json.loads((CODE/'pbc_derived_h2_bound.json').read_text());M=bound['bound'];N=math.prod(raw['relative_orders'])
assert M==math.prod(e*e for e in bound['factor_exponents']) and bound['group_order']==N
old=CODE/'pbc_native_modular_iterated.dat';lines=old.read_text().splitlines(keepends=True)
sh=hashlib.sha256(source.read_bytes()).hexdigest();pos=lines.index(sh+'\n');assert int(lines[pos+1])==N
original_bounds=list(map(int,lines[pos+3].split()));reports=[]
for p in (2,3):
 m=1;t=M
 while t%p==0:m*=p;t//=p
 assert m>1 and M%m==0
 new=list(lines);new[pos+1]=str(m)+'\n';coordinates=[math.gcd(d,m) for d in original_bounds]
 new[pos+3]=' '.join(map(str,coordinates))+'\n'
 path=CODE/f'pbc_native_primary{p}_iterated.dat'
 if path.exists():assert path.read_text()==''.join(new)
 else:path.write_text(''.join(new))
 reports.append({'prime':p,'modulus':m,'global_homology_annihilator':M,'original_group_order':N,
  'source_sha256':sh,'input_path':str(path.relative_to(ROOT)),'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
  'coordinate_counts':dict(collections.Counter(coordinates)),
  'source_words_target_and_all_frame_rows_unchanged':True,
  'proper_bound_rule':'gcd(d,m), justified by retained Bezout coefficients against m during independent verification',
  'corrections_used':'Only s-centralizer commutators of order2' if p==2 else 'Only r-centralizer commutators of order3',
  'scope':'Only this primary component. No integral lifting conclusion without the other component and original-source replay.'})
native=(CODE/'pbc_native_modular_v6.cpp').read_text()
rows=r''' void run_rows(std::istream&rows,int prime){
  assert(prime==2||prime==3);
  for(int i=2;i<extra_count;i++){
   bool sframe=(i<2+s_count);if((prime==2)!=sframe)continue;
   Weights w(extra_count,0);w[i]=1;insert(extras[i],w,trace.leaf("extra",{i+1},extras[i]));
  }
  if(check())return;
  for(;;){
   int len;if(!(rows>>len))break;assert(len>0);std::vector<int>meta(len);for(auto&v:meta)rows>>v;
   Sparse v=readSparse(rows);relation(v,meta);if(found)return;
  }
  if(check())return;
  std::ostringstream o;o<<"[\"failure\","<<targetproof<<',';writeSparse(o,target);o<<"]\n";trace.line(o.str());trace.flush();
  std::cerr<<"PRIMARY_SOURCE_PREFIX_EXHAUSTED_NOT_A_NONLIFTING_CLAIM prime "<<prime<<" support "<<target.size()<<" seconds "<<seconds()<<std::endl;
 }
'''
src=native.replace(' void run(){',rows+' void run(){',1)
src=src[:src.index('int main(')]+r'''int main(int argc,char**argv){
 assert(argc==6);int prime=std::stoi(argv[5]);assert(prime==2||prime==3);
 std::signal(SIGUSR1,PBCSignal);std::signal(SIGUSR2,PBCSignal);std::signal(SIGINT,PBCSignal);std::signal(SIGTERM,PBCSignal);
 std::ifstream in(argv[1]),rows(argv[4]);assert(in&&rows);
 try{Witness w(in,argv[2],argv[3]);w.run_rows(rows,prime);}
 catch(const PBCStopped&){std::cerr<<"native_GRACEFUL_STOP_incomplete_search_valid_gzip_footer"<<std::endl;return 130;}
 return 0;
}
'''
cpp=CODE/'pbc_native_primary_search.cpp';exe=CODE/'pbc_native_primary_search';cpp.write_text(src)
args=['g++','-std=c++17','-O3',str(cpp),'-lgmpxx','-lgmp','-lz','-o',str(exe)]
subprocess.run(args,check=True)
capture=json.loads((CODE/'pbc_smallmod_v2_replay_recipe.json').read_text())
report={'inputs':reports,'native_reducer_source_sha256':hashlib.sha256(native.encode()).hexdigest(),
 'search_source_sha256':hashlib.sha256(cpp.read_bytes()).hexdigest(),'search_executable_sha256':hashlib.sha256(exe.read_bytes()).hexdigest(),
 'compiler_command':args,'original_identity_row_count':capture['identity_rows'],
 'original_identity_rows_sha256':capture['identity_data_sha256'],
 'identity_rows_retained_exactly_by':'code/pbc_smallmod_v2_replay_recipe.json and its included source-leaf payload',
 'status':'Built; no search result or lifting conclusion yet.'}
(CODE/'pbc_primary_search_inputs.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2),flush=True)
