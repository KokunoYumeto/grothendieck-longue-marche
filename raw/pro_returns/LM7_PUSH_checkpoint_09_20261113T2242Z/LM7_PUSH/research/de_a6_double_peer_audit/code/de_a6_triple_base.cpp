// Complete the actual A6/affine-three base from literal saved strong words.
#define main de_a6_schreier_existing_main
#include "de_a6_schreier.cpp"
#undef main

int main(int argc,char**argv){try{
  if(argc!=3)throw std::runtime_error("usage: executable seed.bin complete_certificate.bin");
  std::ifstream in(argv[1],std::ios::binary);
  if(Engine::get<uint32_t>(in)!=0x41365354)throw std::runtime_error("seed magic");
  int n=Engine::get<uint32_t>(in);if(Engine::get<uint32_t>(in))throw std::runtime_error("derived seed");
  Engine e(n);unsigned m=Engine::get<uint32_t>(in);if(m!=2)throw std::runtime_error("source generators");
  std::vector<P>original(m,P(n));for(auto&p:original)in.read((char*)p.data(),2*n);
  unsigned nb=Engine::get<uint32_t>(in);std::vector<int>base(nb);for(auto&b:base)b=Engine::get<uint32_t>(in);
  unsigned ng=Engine::get<uint32_t>(in);std::vector<P>strong(ng,P(n));std::vector<uint32_t>words(ng),depths(ng);
  for(unsigned j=0;j<ng;++j){words[j]=Engine::get<uint32_t>(in);depths[j]=Engine::get<uint32_t>(in);in.read((char*)strong[j].data(),2*n);}
  unsigned nn=Engine::get<uint32_t>(in);std::vector<Node>nodes(nn);
  for(auto&v:nodes){v.op=Engine::get<uint32_t>(in);v.a=Engine::get<uint32_t>(in);v.b=Engine::get<uint32_t>(in);}
  if(!in||in.peek()!=EOF)throw std::runtime_error("seed length");
  e.set_original(original);if(nodes.size()<3)throw std::runtime_error("short seed DAG");
  for(unsigned i=0;i<3;++i)if(nodes[i].op!=e.nodes[i].op||nodes[i].a!=e.nodes[i].a||nodes[i].b!=e.nodes[i].b)
    throw std::runtime_error("original DAG nodes");
  std::vector<unsigned>refs(nn);std::vector<std::vector<unsigned>>checks(nn);
  for(unsigned j=0;j<ng;++j){if(words[j]>=nn)throw std::runtime_error("strong word index");checks[words[j]].push_back(j);}
  for(unsigned i=0;i<nn;++i){auto v=nodes[i];
    if(v.op>=2&&v.op<=5){if(v.a>=i)throw std::runtime_error("word first ancestor");++refs[v.a];}
    if(v.op==2||v.op==4||v.op==5){if(v.b>=i)throw std::runtime_error("word second ancestor");++refs[v.b];}}
  std::vector<std::unique_ptr<P>>values(nn);
  for(unsigned i=0;i<nn;++i){auto v=nodes[i];P p;
    if(v.op==0)p=e.id;else if(v.op==1)p=original.at(v.a);
    else if(v.op==2)p=e.mul(*values.at(v.a),*values.at(v.b));
    else if(v.op==3)p=e.inverse(*values.at(v.a));
    else if(v.op==4)p=e.commutator(*values.at(v.a),*values.at(v.b));
    else if(v.op==5)p=e.conjugate(*values.at(v.a),*values.at(v.b));
    else throw std::runtime_error("word operation");
    for(unsigned j:checks[i])if(p!=strong[j])throw std::runtime_error("literal strong seed mismatch");
    values[i]=std::make_unique<P>(std::move(p));
    if(v.op>=2&&v.op<=5){if(!--refs[v.a])values[v.a].reset();}
    if(v.op==2||v.op==4||v.op==5){if(!--refs[v.b])values[v.b].reset();}
    if(!refs[i])values[i].reset();
  }
  e.nodes=std::move(nodes);for(int b:base){if(b<0||b>=n)throw std::runtime_error("base range");e.new_level(b);}
  for(unsigned j=0;j<ng;++j){P sorted=strong[j];std::sort(sorted.begin(),sorted.end());if(sorted!=e.id)throw std::runtime_error("strong permutation");
    e.add(strong[j],words[j]);if(e.gens.back().depth!=(int)depths[j])throw std::runtime_error("seed depth");}
  std::cout<<"all literal seed words replayed; completing joint source"<<std::endl;
  e.selected_original_indices={0,1};e.discover();for(auto p:original)if(!e.contains(p))throw std::runtime_error("original not generated");
  e.save(argv[2]);e.report();return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<std::endl;return 1;}}
