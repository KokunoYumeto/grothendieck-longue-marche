#!/usr/bin/env python3
"""Retain the read joint kernel collector over the literal enlarged base."""
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent


def main():
    source = HERE / 'de_a6_double_signed.cpp'
    text = source.read_text()
    prefix = text[:text.index('int main(int argc')]
    body = r'''
int main(int argc,char**argv){try{
  if(argc!=6)throw std::runtime_error("usage: executable double_model.bin signed_model.bin joint_upper.bin base_certificate.bin output.json");
  auto start=std::chrono::steady_clock::now();
  Model binary(argv[1]);Signed::Model signs(argv[2]);JointModel model(binary,signs,argv[3]);
  auto engine=Engine::replay(argv[4]);
  if(engine->n!=15774||engine->original.size()!=2||model.base_original[0].size()!=11010)
    throw std::runtime_error("literal enlarged base dimensions");
  for(unsigned g=0;g<2;++g){
    for(unsigned i=0;i<11010;++i)
      if(engine->original[g][i]!=model.base_original[g][i])
        throw std::runtime_error("old common base projection changed");
    for(unsigned i=11010;i<15774;++i)
      if(engine->original[g][i]<11010||engine->original[g][i]>=15774)
        throw std::runtime_error("E62 block not preserved");
  }
  model.base_original=engine->original;
  std::cout<<"complete enlarged A6/A5/E62 base replay passed"<<std::endl;
  Lifted lifted(model,*engine);bool complete=lifted.solve();
  double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  lifted.save(argv[5],complete,seconds);
  std::cout<<"PASS enlarged actual joint kernel dimension "<<lifted.span.basis.size()
           <<" seconds "<<seconds<<std::endl;
  return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
'''
    target = HERE / 'e_a6_double_E62_kernel_root.cpp'
    target.write_text(prefix + body)
    record = {'status': 'PASS_EXACT_ENLARGED_BASE_KERNEL_COLLECTOR_DERIVATION',
              'source_sha256': sha256(source.read_bytes()).hexdigest(),
              'new_source_sha256': sha256(target.read_bytes()).hexdigest(),
              'entire_joint_model_and_collector_retained_without_change': True,
              'new_main_checks_both_literal_old_projection_generators': True,
              'literal_E62_block_verified_by_base_preparation_and_independent_replay': True,
              'base_degree': 15774, 'old_projection_degree': 11010,
              'E62_degree': 4764}
    (HERE / 'e_a6_double_E62_kernel_build_root.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
