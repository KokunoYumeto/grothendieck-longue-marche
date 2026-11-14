#pragma once
struct Lifted {
  JointModel&m;Engine&e;std::vector<Node> nodes;std::vector<JointElement> values;
  JointSpan span;uint64_t relations=0,normal_additions=0;
  Lifted(JointModel&model,Engine&engine):m(model),e(engine){
    // Rebuild the same transversals with their literal word nodes retained.
    std::vector<int> bases;for(auto&l:e.chain)bases.push_back(l.base);
    e.chain.clear();for(int b:bases)e.new_level(b);
    for(unsigned j=0;j<e.gens.size();++j)for(int k=0;k<=e.gens[j].depth;++k)e.extend(k,j,true);
    nodes=e.nodes;values.reserve(nodes.size()+20000);
    for(unsigned j=0;j<nodes.size();++j){auto n=nodes[j];JointElement v;
      if(n.op==0)v=m.one;else if(n.op==1)v=m.original.at(n.a);
      else if(n.op==2)v=m.mul(values.at(n.a),values.at(n.b));
      else if(n.op==3)v=m.inv(values.at(n.a));
      else if(n.op==4)v=m.comm(values.at(n.a),values.at(n.b));
      else if(n.op==5)v=m.conj(values.at(n.a),values.at(n.b));
      else throw std::runtime_error("word operation");values.push_back(v);
    }
  }
  uint32_t product(uint32_t a,uint32_t b){if(!a)return b;if(!b)return a;
    auto v=m.mul(values.at(a),values.at(b));nodes.push_back({2,a,b});values.push_back(v);return nodes.size()-1;}
  uint32_t inverse(uint32_t a){if(!a)return 0;auto v=m.inv(values.at(a));nodes.push_back({3,a,0});values.push_back(v);return nodes.size()-1;}
  void normal_close(){
    for(unsigned at=0;at<span.basis.size();++at)for(unsigned j=0;j<m.original.size();++j){
      auto a=m.conj(m.original[j],m.kernel(span.basis[at]));JointBits v=m.vector(a);
      if(!m.upper.contains(v))throw std::runtime_error("normal image exceeds known full product kernel");
      if(!span.contains(v)){
        uint32_t g=e.original_nodes.empty()?j+1:e.original_nodes[j];
        // Replay does not populate original_nodes; the original DAG has the
        // two generator nodes immediately after its identity.
        if(nodes.at(g).op!=1||nodes[g].a!=j)throw std::runtime_error("original word node");
        uint32_t w=product(product(g,span.words[at]),inverse(g));
        if(values[w]!=a)throw std::runtime_error("normal word lift");
        span.add(v,w);++normal_additions;
      }
    }
  }
  bool solve(){
    for(int lev=(int)e.chain.size()-1;lev>=0;--lev){auto&l=e.chain[lev];
      unsigned old=span.basis.size();
      for(unsigned at=0;at<l.orbit.size();++at)for(unsigned gi=0;gi<e.gens.size();++gi){
        if(e.gens[gi].depth<lev)continue;
        int to=l.pos[e.gens[gi].p[l.orbit[at]]];if(to<0)throw std::runtime_error("base orbit edge");
        P h=e.mul(e.mul(l.trans[at],e.gens[gi].p),l.inv[to]);
        JointElement v=m.mul(m.mul(values[l.word[at]],values[e.gens[gi].node]),m.inv(values[l.word[to]]));
        std::vector<std::pair<uint32_t,bool>> history{{l.word[at],false},{e.gens[gi].node,false},{l.word[to],true}};
        for(int k=lev+1;k<(int)e.chain.size();++k){auto&c=e.chain[k];int b=h[c.base];if(b==c.base)continue;
          int pos=c.pos[b];if(pos<0)throw std::runtime_error("complete base relation missing");
          h=e.mul(h,c.inv[pos]);v=m.mul(v,m.inv(values[c.word[pos]]));history.push_back({c.word[pos],true});
        }
        if(!e.identity(h))throw std::runtime_error("nonidentity base relator");
        ++relations;JointBits b=m.vector(v);
        if(!m.upper.contains(b))throw std::runtime_error("relator exceeds known full product kernel");
        if(!span.contains(b)){
          uint32_t w=0;for(auto[a,inv]:history)w=product(w,inv?inverse(a):a);
          if(values[w]!=v)throw std::runtime_error("relator word lift");
          span.add(b,w);normal_close();
          std::cout<<"new kernel rank "<<span.basis.size()<<" relations "<<relations<<" level "<<lev<<std::endl;
          if(span.basis.size()==m.upper.basis.size())return false;
        }
      }
      std::cout<<"Schreier level "<<lev<<" orbit "<<l.orbit.size()<<" relations "<<relations
               <<" kernel rank "<<span.basis.size()<<" new "<<span.basis.size()-old<<std::endl;
    }
    return true;
  }
  void save(const std::string&file,bool complete,double seconds){
    normal_close();
    for(const auto&b:span.basis)for(auto&g:m.original)
      if(!span.contains(m.vector(m.conj(g,m.kernel(b)))))throw std::runtime_error("final normal closure");
    if(!complete&&span.basis.size()!=170)throw std::runtime_error("incomplete kernel bound");
    if(complete&&relations!=e.final_relations)throw std::runtime_error("Schreier count mismatch");
    std::ofstream f(file);if(!f)throw std::runtime_error("kernel output");
    f<<"{\n\"status\":\"PASS_COMPLETE_JOINT_KERNEL\",\n\"base_order\":\""<<e.order()<<"\",\n"
     <<"\"base_degree\":"<<e.n<<",\n\"kernel_width\":"<<JBW<<",\n\"kernel_dimension\":"<<span.basis.size()<<",\n"
     <<"\"known_joint_kernel_dimension\":170,\n\"full_base_chain_replayed\":true,\n"
     <<"\"all_Schreier_relators_evaluated\":"<<(complete?"true":"false")<<",\n"
     <<"\"exact_upper_bound_attained\":"<<(span.basis.size()==170?"true":"false")<<",\n"
     <<"\"lifted_relators_evaluated\":"<<relations<<",\n\"complete_base_relator_count\":"<<e.final_relations<<",\n"
     <<"\"normal_closure_additions\":"<<normal_additions<<",\n"
     <<"\"literal_word_DAG\":[";
    for(unsigned i=0;i<nodes.size();++i){if(i)f<<",";auto n=nodes[i];f<<"["<<n.op<<","<<n.a<<","<<n.b<<"]";}f<<"],\n";
    f<<"\"kernel_basis_word_nodes\":[";for(unsigned i=0;i<span.words.size();++i){if(i)f<<",";f<<span.words[i];}f<<"],\n";
    f<<"\"kernel_basis_supports\":[";for(unsigned i=0;i<span.basis.size();++i){if(i)f<<",";f<<"[";bool first=true;
      for(int p=0;p<JBW;++p)if((span.basis[i][p/64]>>(p%64))&1){if(!first)f<<",";first=false;f<<p;}f<<"]";}f<<"],\n";
    f<<"\"independent_Python_operation_controls\":"<<m.controls<<",\n\"kernel_coordinate_controls\":"<<m.kernel_controls
     <<",\n\"seconds\":"<<seconds<<"\n}\n";
  }
};

